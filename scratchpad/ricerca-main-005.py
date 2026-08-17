# -*- coding: utf-8 -*-
"""Due domande di forma: come si scrivono le virgolette dentro una resa, e chi
e' 時の管理者 (il custode del tempo che manda in prigione)."""
import glob
import io
import json
import re

voci = []
for p in sorted(glob.glob('dizionario/*.jsonl')):
    nome = p.replace('\\', '/').split('/')[-1].replace('.jsonl', '')
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it'):
            d['_file'] = nome
            voci.append(d)

print('=== rese STATICHE che portano una virgoletta protetta')
n = 0
for d in voci:
    if d['tipo'] == 'statica' and '\\"' in d['it']:
        n += 1
        if n <= 8:
            print(f"    {d['_file']}:{d['riga']}")
            print(f"      en: {d['en'][:100]}")
            print(f"      it: {d['it'][:100]}")
print(f'    --- {n} in tutto')
print()

print('=== 時の管理者 / controller of time / prigione')
for d in voci:
    if '時の管理者' in d['jp'] or re.search(r'controller of time|keeper of time', d['en'], re.I) \
       or '管理者' in d['jp']:
        print(f"    {d['_file']}:{d['riga']}")
        print(f"      jp: {d['jp'][:80]}")
        print(f"      en: {d['en'][:100]}")
        print(f"      it: {d['it'][:100]}")
print()

print('=== jail / prigione')
for d in voci:
    if re.search(r'\bjail\b|\bprison\b', d['en'], re.I):
        print(f"    {d['_file']}:{d['riga']}  en={d['en'][:60]!r}  it={d['it'][:70]!r}")
