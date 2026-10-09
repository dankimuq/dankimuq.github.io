"""Regenerate assets/search-data.js after editing any page.
Run from the repository root:  python3 tools/build_search.py
"""
import glob, html, json, os, re

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
entries = []
for path in sorted(glob.glob(root + '/**/*.html', recursive=True)):
    rel = os.path.relpath(path, root).replace(os.sep, '/')
    src = open(path, encoding='utf-8').read()
    art = re.search(r'<article[^>]*>(.*)</article>', src, re.S)
    if not art:
        continue
    title = re.search(r'name="search-title" content="([^"]*)"', src)
    context = re.search(r'name="search-context" content="([^"]*)"', src)
    slug = 'home' if rel == 'index.html' else rel[:-5]
    text = re.sub(r'<(script|style).*?</\1>', '', art.group(1), flags=re.S)
    text = html.unescape(re.sub(r'<[^>]+>', ' ', text))
    text = re.sub(r'\s+', ' ', text).strip()
    entries.append({
        'slug': slug,
        'url': '/' if slug == 'home' else '/' + rel,
        'title': html.unescape(title.group(1)) if title else slug,
        'context': html.unescape(context.group(1)) if context else '',
        'text': text,
    })
entries.sort(key=lambda e: (e['slug'] != 'home', e['slug']))
with open(root + '/assets/search-data.js', 'w', encoding='utf-8') as f:
    f.write('window.SEARCH_DATA=' + json.dumps(entries, ensure_ascii=False) + ';\n')
print(len(entries), 'pages indexed')
