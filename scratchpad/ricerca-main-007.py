# -*- coding: utf-8 -*-
"""Domande per il quarto lotto: raccolta automatica, striscioni dell'arena,
Lesimas, il tasto della guida."""
import glob
import io
import json
import re

DOMANDE = [
    ('autopickup / raccolta',
     lambda d: re.search(r'auto ?pick', d['en'], re.I) or '自動拾い' in d['jp']
               or 'raccolta automatica' in (d.get('it') or '').lower()),
    ('striscioni dell arena (*…*)',
     lambda d: re.search(r'^\*(win|los|draw|ko|judg|giveup|surrend|curtain)', d['en'].strip(), re.I)
               or re.match(r'^\*[^*]+\*$', d['jp'].strip() or ' ')),
    ('Lesimas',
     lambda d: 'esimas' in d['en'] or 'レシマス' in d['jp']),
    ('tasto ? / help',
     lambda d: re.search(r'\? key|display help|press .{0,6}key', d['en'], re.I)),
    ('enabled / disabled',
     lambda d: re.search(r'\b(is now|now) (dis|en)abled', d['en'], re.I)
               or re.search(r'\b(attivat|disattivat|spent|acces)', (d.get('it') or ''), re.I)),
    ('pedestal /台座',
     lambda d: '台座' in d['jp'] or re.search(r'pedestal', d['en'], re.I)),
]

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

for titolo, filtro in DOMANDE:
    trovate = [d for d in voci if filtro(d)]
    print(f'=== {titolo}  ({len(trovate)})')
    visti = set()
    for d in trovate:
        chiave = (d['en'], d['it'])
        if chiave in visti:
            continue
        visti.add(chiave)
        if len(visti) > 16:
            print(f'    ... e altre {len(trovate) - 16}')
            break
        print(f"    {d['_file']}:{d['riga']}")
        print(f"      jp: {d['jp'][:70]}")
        print(f"      en: {d['en'][:95]}")
        print(f"      it: {d['it'][:95]}")
    print()
