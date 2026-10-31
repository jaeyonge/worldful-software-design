from pathlib import Path
import re,shutil
root=Path(__file__).resolve().parents[1]
t=(root/'manuscript.md').read_text()
parts=re.split(r'(?=^## \d+\. )',t,flags=re.M)
chapters=[]
def slug(s): return re.sub(r'[^\w\- ]','',s.lower()).replace(' ','-')
anchors={}
for i,part in enumerate(parts[1:],1):
 title=part.splitlines()[0][3:]; name=f'{i:02d}-{slug(title.split(". ",1)[1])}.md'
 chapters.append((title,name,part))
 for h in re.findall(r'^#{1,6} (.+)$',part,re.M): anchors[slug(h)]=name[:-3]+'.html#'+slug(h)
summary=['# Summary','','[Start here](index.md)','']
for title,name,part in chapters:
 part=re.sub(r'\]\(#([^)]*)\)',lambda m: ']('+anchors.get(m[1],'#'+m[1])+')',part)
 part=re.sub(r'^## (\d+\. .+)$',r'# \1',part,count=1,flags=re.M)
 part=re.sub(r'^(#{3,6}) ', lambda m: m[1][1:]+' ', part, flags=re.M)
 (root/'src'/name).write_text(part)
 summary.append(f'- [{title.split(". ",1)[1]}]({name})')
(root/'src/SUMMARY.md').write_text('\n'.join(summary)+'\n')
(root/'src/index.md').write_text('''# A world of deliberate decisions

<div class="book-kicker">A DESIGN TEXTBOOK & FIELD GUIDE</div>

Some software feels unmistakably authored. Its language, controls, content, and limits belong together. This book explores why—and how to build that coherence into your own applications.

<div class="book-meta">17 chapters · 12 principles · 11 reusable templates</div>

[Begin with purpose and reading routes →](01-purpose-and-reading-routes.md)

## Find your way

| Your intention | Start here |
|---|---|
| Understand the idea | [Definition and boundaries](02-definition-and-boundaries.md) |
| Explore the foundations | [Theoretical foundations](03-theoretical-foundations.md) |
| Learn from real products | [grug](07-case-study-grug.md) · [Poolsuite FM](08-case-study-poolsuite-fm.md) |
| Build your own application | [Development methodology](10-development-methodology.md) |
| Evaluate your work | [Weighted rubric](11-evaluation-and-weighted-rubric.md) · [Checklists](12-development-checklists.md) |
| Reuse the working tools | [Templates](14-reusable-templates.md) |

## Keep a copy

<a href="downloads/worldful-software-design.md" download>Download the complete Markdown textbook</a> for your editor, personal wiki, or offline reference.

Version 1.2 · Research date: 31 October 2026. “Worldful software” is a provisional working concept. The book distinguishes documented facts, reported experiences, interpretations, and proposed methods.

Use the chapter menu to browse, or the search button to find a topic. Reading themes are available from the theme menu.
''')

