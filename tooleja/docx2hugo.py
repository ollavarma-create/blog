#!/usr/bin/env python3
"""
docx2hugo.py - Convert a Word document into a Hugo leaf bundle (page bundle).

Usage:
    python3 docx2hugo.py <file.docx> <slug> <hugo-root>

Example:
    python3 docx2hugo.py Kilpirauhanen.docx kilpirauhanen-toiminta ~/Blogi

Output:
    <hugo-root>/content/posts/<slug>/index.md
    <hugo-root>/content/posts/<slug>/media/   (if images present)

Dependencies:
    - pandoc (apt install pandoc)
    - Python 3.8+
"""

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def run_pandoc(docx_path: Path, out_md: Path, extract_dir: Path) -> None:
    """Run pandoc to convert DOCX -> Markdown, extracting media files."""
    cmd = [
        "pandoc",
        str(docx_path),
        "--from", "docx",
        "--to", "markdown",
        f"--extract-media={extract_dir}",
        "-o", str(out_md),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"✗ Pandoc error:\n{result.stderr}", file=sys.stderr)
        sys.exit(1)


def fix_media_paths(content: str, tmp_media_dir: Path) -> str:
    """Replace absolute tmp media paths with relative ./media/ paths.

    Pandoc writes absolute paths like /tmp/tmpXXX/media/image.png into the
    markdown. We replace the tmp prefix so Hugo can find the files.
    """
    # Replace e.g. /tmp/tmpXXX/media/ → ./media/
    abs_prefix = str(tmp_media_dir).rstrip("/") + "/"
    return content.replace(abs_prefix, "./media/")


def remove_image_size_attrs(content: str) -> str:
    """Remove pandoc-generated {width=... height=...} from image tags.

    Handles both single-line and two-line attribute blocks (re.DOTALL).
    """
    return re.sub(
        r'(!\[[^\]]*\]\([^)]*\))\{[^}]*\}',
        r'\1',
        content,
        flags=re.DOTALL,
    )


def remove_heading_attrs(content: str) -> str:
    """Remove Word-generated heading IDs like {#id .TOC-Heading}."""
    return re.sub(r'\s*\{#[^}]*\}', '', content)


def remove_file_links(content: str) -> str:
    """Replace internal file:/// hyperlinks (Word cross-refs) with plain #."""
    return re.sub(r'\(file:///[^)]*\)', '(#)', content)


def remove_toc_section(content: str) -> str:
    """Remove the Word-generated table of contents section.

    Matches from a heading containing 'sisällysluettelo' (case-insensitive)
    up to (but not including) the next heading at any level.
    """
    return re.sub(
        r'#+\s*Sisällysluettelo.*?(?=\n#)',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL,
    )


def fix_paragraphs(content: str) -> str:
    """Join soft-wrapped lines within paragraphs into single lines.

    Pandoc wraps at ~80 chars. We join those soft wraps so Hugo renders
    clean paragraphs regardless of the hardWraps setting.

    Skips: front matter, headings, standalone images, code blocks,
    tables, list items, and footnote definitions.
    """
    blocks = re.split(r'\n{2,}', content)
    fixed = []

    for block in blocks:
        lines = block.strip().split('\n')

        if not lines:
            continue

        # Front matter fence
        if block.startswith('---'):
            fixed.append(block)
            continue

        # Headings (every line starts with #)
        if all(l.startswith('#') for l in lines):
            fixed.append(block)
            continue

        # Standalone image — single line only
        if len(lines) == 1 and re.match(r'^!\[', lines[0]):
            fixed.append(block)
            continue

        # Fenced code block
        if block.startswith('```'):
            fixed.append(block)
            continue

        # Table
        if any(l.startswith('|') for l in lines):
            fixed.append(block)
            continue

        # List items and footnote definitions
        if all(re.match(r'^\s*([-*]|\d+\.|\[\^)', l) for l in lines if l.strip()):
            fixed.append(block)
            continue

        # Join soft-wrapped lines within the paragraph
        joined = re.sub(r'(?<!\n)\n(?!\n)', ' ', block)

        # Add missing space before a markdown link — but NOT inside image tags.
        # [^\s!] ensures we don't insert a space after '!' (which would break ![).
        joined = re.sub(r'([^\s!])\[', r'\1 [', joined)

        # Collapse multiple spaces (preserve code spans)
        joined = re.sub(r'(?<!`)\s{2,}(?!`)', ' ', joined)

        fixed.append(joined.strip())

    return '\n\n'.join(fixed)


def clean(content: str, tmp_media_dir: Path) -> str:
    """Apply all cleaning steps in order."""
    content = fix_media_paths(content, tmp_media_dir)
    content = remove_image_size_attrs(content)
    content = remove_heading_attrs(content)
    content = remove_file_links(content)
    content = remove_toc_section(content)
    content = fix_paragraphs(content)
    # Strip trailing whitespace from every line
    content = '\n'.join(line.rstrip() for line in content.split('\n'))
    # Ensure single trailing newline
    return content.rstrip('\n') + '\n'


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) != 4:
        print("Usage: python3 docx2hugo.py <file.docx> <slug> <hugo-root>")
        sys.exit(1)

    docx_path = Path(sys.argv[1]).resolve()
    slug      = sys.argv[2]
    hugo_root = Path(sys.argv[3]).resolve()

    if not docx_path.exists():
        print(f"✗ File not found: {docx_path}", file=sys.stderr)
        sys.exit(1)

    bundle_dir = hugo_root / "content" / "posts" / slug
    out_md     = bundle_dir / "index.md"

    print(f"→ Source : {docx_path}")
    print(f"→ Bundle : {bundle_dir}")

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path  = Path(tmp)
        tmp_md    = tmp_path / "index.md"
        # Pandoc creates a 'media' subdirectory inside the given extract path,
        # so point it at tmp_path to get tmp_path/media/
        tmp_media = tmp_path / "media"

        # Step 1: Convert with pandoc
        print("→ Running pandoc…")
        run_pandoc(docx_path, tmp_md, tmp_path)

        # Step 2: Read and clean
        print("→ Cleaning markdown…")
        content = tmp_md.read_text(encoding="utf-8")
        content = clean(content, tmp_media)

        # Step 3: Write Hugo leaf bundle
        bundle_dir.mkdir(parents=True, exist_ok=True)
        out_md.write_text(content, encoding="utf-8")

        # Step 4: Copy media/ if present
        if tmp_media.exists():
            dest_media = bundle_dir / "media"
            if dest_media.exists():
                shutil.rmtree(dest_media)
            shutil.copytree(tmp_media, dest_media)
            image_count = sum(1 for f in dest_media.rglob("*") if f.is_file())
            print(f"→ Copied {image_count} image(s) → media/")
        else:
            print("→ No images found")

    print(f"\n✓ Done: {out_md}")
    print("  Check for merged words before publishing:")
    print(f"  grep -oP '\\w{{20,}}' {out_md}")


if __name__ == "__main__":
    main()
