#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
python3 scripts/prepare.py
"${MDBOOK_BIN:-mdbook}" build
mkdir -p dist/vendor dist/downloads
cp -R node_modules/mermaid/dist/. dist/vendor/
cp manuscript.md dist/downloads/worldful-software-design.md
python3 scripts/finalize.py

mkdir -p dist/downloads/assets
cp -R src/assets/. dist/downloads/assets/
