#!/usr/bin/env python3
"""Deterministic slide splicer for talk.html.

Usage: python3 design/splice.py <talk.html> <ops.json>

ops.json is a list of operations, applied in order:
  {"op":"delete",        "id":"s-foo"}
  {"op":"replace",       "id":"s-foo", "file":"fragment.html"}
  {"op":"insert_after",  "id":"s-foo", "file":"fragment.html"}
  {"op":"insert_before", "id":"s-foo", "file":"fragment.html"}
  {"op":"replace_block", "start":"<!-- MD-BLOCK-START -->", "end":"<!-- MD-BLOCK-END -->", "file":"fragment.html"}
  {"op":"insert_after_block_end", "end":"<!-- MD-BLOCK-END -->", "file":"fragment.html"}
A slide is the text from '<section class="slide...' id="ID">' to its matching '</section>' (sections never nest).
'file' paths are resolved relative to the ops.json directory. Fragments are inserted verbatim.
"""
import json, re, sys, os
html_path, ops_path = sys.argv[1], sys.argv[2]
base = os.path.dirname(os.path.abspath(ops_path))
html = open(html_path, encoding='utf-8').read()
ops = json.load(open(ops_path, encoding='utf-8'))

def span(html, sid):
    m = re.search(r'<section class="slide[^"]*" id="%s"[^>]*>' % re.escape(sid), html)
    if not m: raise SystemExit(f"no section id={sid}")
    e = html.find('</section>', m.end())
    if e < 0: raise SystemExit(f"unterminated section {sid}")
    return m.start(), e + len('</section>')

def frag(op):
    return open(os.path.join(base, op['file']), encoding='utf-8').read().rstrip('\n') + '\n'

for op in ops:
    k = op['op']
    if k == 'delete':
        s, e = span(html, op['id']); html = html[:s] + html[e:]
    elif k == 'replace':
        s, e = span(html, op['id']); html = html[:s] + frag(op).rstrip('\n') + html[e:]
    elif k == 'insert_after':
        s, e = span(html, op['id']); html = html[:e] + '\n\n' + frag(op) + html[e:]
    elif k == 'insert_before':
        s, e = span(html, op['id']); html = html[:s] + frag(op) + '\n' + html[s:]
    elif k == 'replace_block':
        s = html.find(op['start']); e = html.find(op['end'])
        if s < 0 or e < 0: raise SystemExit('block markers not found')
        e += len(op['end'])
        html = html[:s] + op['start'] + '\n' + frag(op) + op['end'] + html[e:]
    elif k == 'insert_after_block_end':
        e = html.find(op['end'])
        if e < 0: raise SystemExit('end marker not found')
        e += len(op['end'])
        html = html[:e] + '\n\n' + frag(op) + html[e:]
    else:
        raise SystemExit(f'unknown op {k}')
    print('ok', k, op.get('id') or op.get('start') or op.get('end'))
open(html_path, 'w', encoding='utf-8').write(html)
print('sections now:', len(re.findall(r'<section class="slide', html)))
