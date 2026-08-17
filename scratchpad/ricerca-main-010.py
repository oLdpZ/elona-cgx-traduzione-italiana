# -*- coding: utf-8 -*-
"""Domande per gli esiti degli incarichi e le battute degli dèi."""
import glob
import io
import json
import re

DOMANDE = [
    ('incarichi: consegna / raccolto',
     lambda d: re.search(r'\bharvest\b|deliver|\bsupply\b', d['en'], re.I) or '納入' in d['jp']),
    ('incarichi: mine / bonifica',
     lambda d: re.search(r'\bmine(field|s)?\b|land ?mine', d['en'], re.I) or '撤去' in d['jp']),
    ('incarichi: caccia / conquer',
     lambda d: re.search(r'\bconquer\b|slay the target|hunt', d['en'], re.I) or '討伐' in d['jp']),
    ('festa / party',
     lambda d: re.search(r'\bparty\b', d['en'], re.I) and 'time' not in d['en'].lower()),
    ('Big Daddy / Little Sister',
     lambda d: re.search(r'big daddy|little sister|bubbles', d['en'], re.I)),
    ('Lulwy',   lambda d: 'ulwy' in d['en'] or 'ルルウィ' in d['jp']),
    ('Ehekatl', lambda d: 'hekatl' in d['en'] or 'エヘカトル' in d['jp']),
    ('Itzpalt', lambda d: 'tzpalt' in d['en'] or 'イツパロトル' in d['jp']),
    ('Jure',    lambda d: re.search(r'\bJure\b', d['en']) or 'ジュア' in d['jp']),
    ('Mani',    lambda d: re.search(r'\bMani\b', d['en']) or 'マニ' in d['jp']),
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
        if len(visti) > 8:
            print(f'    ... e altre {len(trovate) - 8}')
            break
        print(f"    {d['_file']}:{d['riga']}")
        print(f"      en: {d['en'][:95]}")
        print(f"      it: {d['it'][:95]}")
    print()
