# Worldful Software Design

An illustrated textbook and development reference for software with a coherent creative point of view. Includes theoretical foundations, twelve principles, detailed grug and Poolsuite case studies, native-app observations, evaluation tools, and reusable templates.

**Read online:** https://jaeyonge.github.io/worldful-software-design/

## Editing

Edit `manuscript.md` as the authoritative text. Images and provenance records live in `src/assets/case-studies/`. Chapter files and navigation are generated during the build.

## Local preview

Install [mdBook 0.5.4](https://github.com/rust-lang/mdBook/releases/tag/v0.5.4), Node.js 22 or later, and Python 3.

```sh
npm ci
npm run build
python3 -m http.server 4321 --directory dist
```

Open http://localhost:4321/ for a local preview. Set `MDBOOK_BIN` if mdBook is not on PATH.

## Publishing

GitHub Actions builds and publishes the book when changes reach `main`. Configure repository Settings → Pages → Source as **GitHub Actions**. The deployment belongs to this repository and does not modify the résumé site.

The project path is configured in `book.toml`. Update `site-url` if the repository name or public address changes.

## How the build works

1. `scripts/prepare.py` divides the manuscript into chapters and rewrites internal references.
2. mdBook generates navigation, search, reading themes, and printable HTML.
3. Mermaid is bundled locally for the diagram.
4. `scripts/finalize.py` prepares the browser runtime and downloadable manuscript.

The `dist/` directory is generated, not committed. It is uploaded by the deployment workflow.

## Sources and image credits

The book distinguishes documented facts, direct observations, reported experiences, interpretations, and proposed methods. Product screenshots and designs remain the property of their respective creators. Figure provenance is recorded in `src/assets/case-studies/sources.json`; screenshots are included for design criticism and analysis. No blanket license is granted for third-party assets.
