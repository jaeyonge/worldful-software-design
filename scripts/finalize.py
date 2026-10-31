from pathlib import Path
import re,shutil
root=Path(__file__).resolve().parents[1]; dist=root/'dist'
for p in dist.glob('*.html'):
 t=p.read_text()
 scripts=re.findall(r'<script src="([^"]+)"></script>',t)
 common=[s for s in scripts if any(s.startswith(n) for n in ['elasticlunr-','mark-','searcher-','clipboard-','highlight-','book-'])]
 if common:
  bundle='\n;\n'.join((dist/s).read_text() for s in common)
  (dist/'reader-runtime.js').write_text(bundle)
  for s in common:
   t=t.replace(f'<script src="{s}"></script>', '<script src="reader-runtime.js"></script>' if s==common[-1] else '')
 t=t.replace('href="downloads/worldful-software-design.html"','href="downloads/worldful-software-design.md"')
 p.write_text(t)
# Only the ESM runtime is served; source maps and type declarations are not needed.
for p in (dist/'vendor').rglob('*'):
 if p.is_file() and p.suffix != '.mjs': p.unlink()
