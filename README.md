# hiltsu.codeberg.page

Personal blog by Jari Hiltunen (OH4CMA).  
Built with [Hugo](https://gohugo.io), hosted on [Codeberg Pages](https://codeberg.page).

## Quick start

### 1. Install Hugo

```bash
# Fedora
sudo dnf install hugo

# macOS
brew install hugo

# Or download binary from https://github.com/gohugoio/hugo/releases
# Recommended: Hugo Extended v0.128+
```

### 2. Local development

```bash
git clone https://codeberg.org/hiltsu/pages.git
cd pages
hugo server -D
# Open http://localhost:1313
```

### 3. Create a new post

Hugo leaf bundles keep content and images together:

```bash
# Finnish post
mkdir -p content/fi/posts/my-new-post
hugo new content/fi/posts/my-new-post/index.md

# English post
mkdir -p content/en/posts/my-new-post
hugo new content/en/posts/my-new-post/index.md
```

Edit the generated file. Remove `draft: true` when ready to publish.

**Directory naming rules** — Hugo slugifies directory names to URLs:
- Use lowercase ASCII and hyphens: `my-post-title`
- No spaces, em-dashes (—), smart quotes, or parentheses
- No special characters: ä→a, ö→o, å→a (or keep Finnish as-is for Unicode URLs)
- Run `./tooleja/slug-check.sh` to audit existing content

### 4. Bilingual posts

To link Finnish and English versions, use the same `translationKey` in both files:

```yaml
# content/fi/posts/aiheeni/index.md
translationKey: "my-topic"

# content/en/posts/my-topic/index.md
translationKey: "my-topic"
```

Hugo will then show a language switcher on those pages.

### 5. Deploy

The `deploy.sh` script handles everything in one step:

```bash
chmod +x deploy.sh   # first time only
./deploy.sh "Optional commit message"
```

It will:
1. Commit and push source changes to `main`
2. Build the site with `hugo --minify`
3. Force-push the built output to the `pages` branch (Codeberg Pages)

Your site will be live at **https://hiltsu.codeberg.page**

### 6. Importing articles

To convert HTML exports (LinkedIn, Medium, etc.) to Markdown:

```bash
pandoc -f html -t markdown article.html -o article.md
```

Then add front matter and place in the correct content directory. See
`tooleja/docx2hugo.py` for Word document conversion.

## Project structure

```
.
├── hugo.toml                     # Site configuration + [related] + [pagination]
├── deploy.sh                     # One-command build & deploy
├── i18n/
│   ├── fi.toml                   # Finnish UI strings
│   └── en.toml                   # English UI strings
├── content/
│   ├── fi/                       # Finnish content
│   │   ├── about.md
│   │   └── posts/
│   │       └── post-name/        # Leaf bundle (dir + index.md)
│   │           ├── index.md
│   │           └── image.jpg     # Images live alongside the post
│   └── en/                       # English content
│       ├── about.md
│       └── posts/
├── themes/hiltsu-clean/
│   ├── layouts/
│   │   ├── index.html            # Home page
│   │   ├── _default/
│   │   │   ├── baseof.html       # Base HTML template
│   │   │   ├── list.html         # Post listing (tags, sections)
│   │   │   └── single.html       # Single post + about page
│   │   └── partials/
│   │       ├── header.html
│   │       ├── footer.html
│   │       ├── jsonld.html       # JSON-LD structured data
│   │       ├── post-nav.html     # Previous / next post
│   │       └── related-posts.html
│   └── static/css/style.css      # Theme styles
├── static/                       # Site-wide static files (images etc.)
└── tooleja/
    ├── slug-check.sh             # Audit content dirs for URL issues
    ├── docx2hugo.py              # Word → Markdown converter
    └── hugo-artikkeli-muistiinpanot.md
```

## i18n — adding UI strings

All button labels and UI text live in `i18n/fi.toml` and `i18n/en.toml`.
Templates use `{{ i18n "key" }}`. To add a new string:

```toml
# i18n/fi.toml
[myNewString]
other = "Suomenkielinen teksti"

# i18n/en.toml
[myNewString]
other = "English text"
```

```html
<!-- in a template -->
{{ i18n "myNewString" }}
```

## Related posts

Configured in `hugo.toml` under `[related]`. Matches by shared tags (weight 100)
with a small recency bonus (weight 10). Threshold 60 = moderately related.

- Lower threshold (e.g. 40) → more results
- Higher threshold (e.g. 80) → stricter matching

## Tags in use

**Technical:** `esp32`, `lorawan`, `iot`, `embedded`, `micropython`,
`ai`, `ml`, `3d-printing`, `steganography`, `ham-radio`

**Non-technical:** `innovation`, `philosophy`, `psychology`,
`sociology`, `society`

## License

Content: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)  
Code: [MIT](https://opensource.org/licenses/MIT)
