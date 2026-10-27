#!/usr/bin/env python3
"""
medium_to_hugo.py
=================
Convert Medium HTML export files to Hugo/Jekyll-compatible Markdown,
downloading all images locally and rewriting references to relative paths.

Usage:
    python medium_to_hugo.py --input /path/to/medium_export --output /path/to/hugo_site

    # Dry run (no image downloads):
    python medium_to_hugo.py --input ./medium_export --output ./hugo --dry-run

    # Custom directory layout:
    python medium_to_hugo.py \\
        --input ./medium_export \\
        --output ./my_blog \\
        --images-dir static/images \\
        --content-dir content/posts \\
        --image-url-prefix /images

Expected Medium export structure:
    medium_export/
    └── posts/
        ├── 2024-10-25_Article-Title-abc123.html
        └── 2024-10-29_Another-Article-def456.html

Output structure (Hugo):
    hugo_site/
    ├── content/posts/
    │   ├── article-title.md
    │   └── another-article.md
    └── static/images/
        ├── article-title/
        │   ├── image-a1b2c3d4.jpg
        │   └── image-e5f6a7b8.png
        └── another-article/
            └── image-c9d0e1f2.jpg

Dependencies:
    pip install beautifulsoup4==4.14.3 markdownify==1.2.2 requests==2.33.1 python-slugify==8.0.4
"""

from __future__ import annotations

import argparse
import hashlib
import logging
import mimetypes
import re
import sys
import time
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup, Tag
from markdownify import markdownify as html_to_md
from slugify import slugify

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Polite delay between CDN requests (seconds)
DOWNLOAD_DELAY: float = 0.4

# Browser-like UA to reduce 403s from Medium CDN
REQUEST_HEADERS: dict[str, str] = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64; rv:126.0) "
        "Gecko/20100101 Firefox/126.0"
    ),
    "Accept": "image/avif,image/webp,*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://medium.com/",
}

# Recognised image extensions - used for extension sniffing
KNOWN_IMAGE_EXTENSIONS: frozenset[str] = frozenset(
    {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".avif"}
)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Convert Medium HTML exports to Hugo/Jekyll Markdown "
            "with locally downloaded images."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--input",
        required=True,
        metavar="DIR",
        help="Medium export root directory (must contain a 'posts/' subdirectory)",
    )
    parser.add_argument(
        "--output",
        required=True,
        metavar="DIR",
        help="Output root directory (Hugo/Jekyll site root)",
    )
    parser.add_argument(
        "--images-dir",
        default="static/images",
        metavar="PATH",
        help="Image output path relative to --output (default: static/images)",
    )
    parser.add_argument(
        "--content-dir",
        default="content/posts",
        metavar="PATH",
        help="Markdown output path relative to --output (default: content/posts)",
    )
    parser.add_argument(
        "--image-url-prefix",
        default="/images",
        metavar="URL",
        help="URL prefix used in Markdown image links (default: /images)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Convert without downloading images (useful for testing)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show debug-level output",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def make_slug(text: str, max_length: int = 80) -> str:
    """Return a URL-safe slug from arbitrary text."""
    return slugify(text, max_length=max_length, separator="-")


def guess_image_extension(url: str, content_type: Optional[str] = None) -> str:
    """
    Determine the file extension for a downloaded image.
    Priority: URL path suffix → Content-Type header → fallback .jpg
    """
    parsed = urlparse(url)
    suffix = Path(parsed.path).suffix.lower().split("?")[0]
    if suffix in KNOWN_IMAGE_EXTENSIONS:
        return suffix

    if content_type:
        # Strip charset / quality params
        mime = content_type.split(";")[0].strip()
        ext = mimetypes.guess_extension(mime)
        if ext and ext != ".jpe":          # mimetypes returns .jpe for JPEG
            return ext.replace(".jpe", ".jpg")

    return ".jpg"


def stable_image_filename(url: str, index: int) -> str:
    """
    Build a deterministic local filename for an image URL.
    Format: <url-stem-truncated>-<md5-8chars><ext>
    """
    url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
    parsed = urlparse(url)
    stem = Path(parsed.path).stem[:40] or f"image-{index:03d}"
    # Clean stem – strip anything that isn't alphanumeric / dash / underscore
    stem = re.sub(r"[^a-zA-Z0-9_-]", "-", stem).strip("-")
    ext = guess_image_extension(url)
    return f"{stem}-{url_hash}{ext}"


# ---------------------------------------------------------------------------
# Image download
# ---------------------------------------------------------------------------


def download_image(
    url: str,
    dest: Path,
    session: requests.Session,
) -> bool:
    """
    Download an image from *url* and save it to *dest*.
    Returns True on success, False on recoverable failure.
    """
    try:
        response = session.get(url, timeout=20, stream=True)
        response.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(response.content)
        log.debug("  ↓ %s", url)
        return True
    except requests.Timeout:
        log.warning("  ✗ Timeout downloading: %s", url)
    except requests.HTTPError as exc:
        log.warning("  ✗ HTTP %s for: %s", exc.response.status_code, url)
    except requests.RequestException as exc:
        log.warning("  ✗ Request error for %s: %s", url, exc)
    except OSError as exc:
        log.warning("  ✗ Cannot write %s: %s", dest, exc)
    return False


# ---------------------------------------------------------------------------
# HTML parsing
# ---------------------------------------------------------------------------


def extract_metadata(soup: BeautifulSoup) -> dict[str, str]:
    """Pull title, ISO date, and subtitle from a Medium HTML export."""
    meta: dict[str, str] = {}

    # Title: first <h1> in the document
    h1 = soup.find("h1")
    if h1:
        meta["title"] = h1.get_text(strip=True)
    else:
        title_tag = soup.find("title")
        meta["title"] = title_tag.get_text(strip=True) if title_tag else "Untitled"

    # Date: <time class="dt-published" datetime="…">
    time_tag = soup.find("time", class_="dt-published")
    if time_tag and time_tag.get("datetime"):
        meta["date"] = str(time_tag["datetime"])[:10]   # Keep YYYY-MM-DD part
    else:
        meta["date"] = ""

    # Subtitle: first <h2> (Medium uses it as a lede/description)
    h2 = soup.find("h2")
    meta["description"] = h2.get_text(strip=True) if h2 else ""

    return meta


def extract_article_body(soup: BeautifulSoup) -> Optional[Tag]:
    """Return the main content tag from a Medium HTML export."""
    return soup.find("article") or soup.find("section")   # type: ignore[return-value]


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------


def yaml_quote(value: str) -> str:
    """Wrap a string in double quotes, escaping internal quotes."""
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def build_frontmatter(meta: dict[str, str]) -> str:
    """Generate Hugo/Jekyll YAML frontmatter block."""
    lines = ["---"]
    lines.append(f"title: {yaml_quote(meta.get('title', 'Untitled'))}")
    if meta.get("date"):
        lines.append(f"date: {meta['date']}")
    if meta.get("description"):
        lines.append(f"description: {yaml_quote(meta['description'])}")
    lines.append("draft: false")
    lines.append("---")
    lines.append("")          # Blank line after closing ---
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Core conversion
# ---------------------------------------------------------------------------


def process_file(
    html_path: Path,
    output_md_dir: Path,
    output_img_dir: Path,
    image_url_prefix: str,
    session: requests.Session,
    dry_run: bool,
) -> bool:
    """
    Convert one Medium HTML file to Markdown.
    Downloads images into output_img_dir/<slug>/ and rewrites src attributes.
    Returns True on success.
    """
    log.info("Processing: %s", html_path.name)

    try:
        raw_html = html_path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        log.error("Cannot read %s: %s", html_path, exc)
        return False

    soup = BeautifulSoup(raw_html, "html.parser")
    meta = extract_metadata(soup)
    body = extract_article_body(soup)

    if body is None:
        log.warning("No <article> or <section> found in %s – skipping.", html_path.name)
        return False

    # Build slug from title, fall back to the HTML filename stem
    title_slug = make_slug(meta["title"]) if meta["title"] else ""
    slug = title_slug or make_slug(html_path.stem) or html_path.stem

    article_img_dir = output_img_dir / slug
    article_img_prefix = f"{image_url_prefix}/{slug}"

    # ------------------------------------------------------------------
    # Image processing
    # ------------------------------------------------------------------
    images_found = 0
    images_ok = 0

    for idx, img_tag in enumerate(body.find_all("img")):
        src = img_tag.get("src") or img_tag.get("data-src") or ""
        if not src or src.startswith("data:"):
            continue

        images_found += 1
        local_filename = stable_image_filename(src, idx)
        local_path = article_img_dir / local_filename
        local_url = f"{article_img_prefix}/{local_filename}"

        if not dry_run:
            if not local_path.exists():
                success = download_image(src, local_path, session)
                time.sleep(DOWNLOAD_DELAY)
            else:
                log.debug("  ↷ Already exists: %s", local_path.name)
                success = True

            if not success:
                # Leave the original URL intact so content isn't silently broken
                log.warning("  ! Keeping original URL for image %d", idx)
                continue

        # Rewrite src to local URL
        img_tag["src"] = local_url
        img_tag["loading"] = "lazy"

        # Remove srcset – it still points at Medium CDN
        if img_tag.get("srcset"):
            del img_tag["srcset"]

        # Ensure alt text is present (accessibility + Hugo)
        if not img_tag.get("alt"):
            img_tag["alt"] = Path(local_filename).stem

        images_ok += 1

    # ------------------------------------------------------------------
    # Clean up elements that shouldn't appear in the output
    # ------------------------------------------------------------------

    # Remove <footer> (Medium export metadata: author, canonical link, etc.)
    for tag in body.find_all("footer"):
        tag.decompose()

    # Remove the first <h1> – it lives in frontmatter instead
    first_h1 = body.find("h1")
    if first_h1:
        first_h1.decompose()

    # ------------------------------------------------------------------
    # HTML → Markdown
    # ------------------------------------------------------------------
    markdown_body = html_to_md(
        str(body),
        heading_style="ATX",        # Use # ## ### style headings
        bullets="-",                # Unordered lists use -
        strip=["script", "style", "figure"],
        newline_style="backslash",  # Preserve explicit line breaks
    )

    # Normalise excessive blank lines produced by markdownify
    markdown_body = re.sub(r"\n{3,}", "\n\n", markdown_body).strip()

    # ------------------------------------------------------------------
    # Write output
    # ------------------------------------------------------------------
    output_md_dir.mkdir(parents=True, exist_ok=True)
    output_md_path = output_md_dir / f"{slug}.md"

    output_md_path.write_text(
        build_frontmatter(meta) + markdown_body + "\n",
        encoding="utf-8",
    )

    log.info(
        "  ✓ Written: %s  [images: %d/%d downloaded]",
        output_md_path.relative_to(output_md_path.parents[2]),
        images_ok,
        images_found,
    )
    return True


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    args = parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Locate the posts/ directory
    input_root = Path(args.input).resolve()
    posts_dir = input_root / "posts"

    if not posts_dir.is_dir():
        # Allow pointing directly to the posts/ directory
        if any(input_root.glob("*.html")):
            posts_dir = input_root
        else:
            log.error(
                "Cannot find a 'posts/' directory under %s.\n"
                "Point --input to the root of your Medium export "
                "(the folder that contains 'posts/').",
                input_root,
            )
            sys.exit(1)

    html_files = sorted(posts_dir.glob("*.html"))
    if not html_files:
        log.error("No .html files found in %s", posts_dir)
        sys.exit(1)

    log.info("Found %d HTML file(s) in %s", len(html_files), posts_dir)
    if args.dry_run:
        log.info("DRY RUN – images will not be downloaded.")

    output_root = Path(args.output).resolve()
    output_md_dir = output_root / args.content_dir
    output_img_dir = output_root / args.images_dir

    session = requests.Session()
    session.headers.update(REQUEST_HEADERS)

    success, failed = 0, 0

    for html_file in html_files:
        ok = process_file(
            html_path=html_file,
            output_md_dir=output_md_dir,
            output_img_dir=output_img_dir,
            image_url_prefix=args.image_url_prefix,
            session=session,
            dry_run=args.dry_run,
        )
        if ok:
            success += 1
        else:
            failed += 1

    log.info(
        "Done: %d converted, %d failed.  Output → %s",
        success,
        failed,
        output_root,
    )

    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
