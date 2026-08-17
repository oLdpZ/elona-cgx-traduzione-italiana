# -*- coding: utf-8 -*-
"""Domande per il lotto della morte e dei due finali di Tyris del Sud."""
import glob
import io
import json
import re

DOMANDE = [
    ('災厄の根源 / source of disaster',
     lambda d: '災厄' in d['jp'] or re.search(r'source of disaster|root of', d['en'], re.I)),
    ('Meshera',
     lambda d: re.search(r'meshera', d['en'], re.I) or 'メシェーラ' in d['jp']),
    ('Enthumesis',
     lambda d: re.search(r'enthumesis', d['en'], re.I) or 'エンテュメシス' in d['jp']),
    ('dio del caos / 混沌の神',
     lambda d: '混沌の神' in d['jp'] or re.search(r'god of chaos', d['en'], re.I)),
    ('seppellire / buried',
     lambda d: re.search(r'\bburied|\bbury\b|grave', d['en'], re.I)),
    ('crawl / risalire',
     lambda d: re.search(r'crawl', d['en'], re.I)),
    ('reload / ricarica',
     lambda d: re.search(r'reload|last save', d['en'], re.I)),
    ('ultime parole / dying message',
     lambda d: re.search(r'dying message|last word', d['en'], re.I) or '遺言' in d['jp']),
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
        if len(visti) > 12:
            print(f'    ... e altre {len(trovate) - 12}')
            break
        print(f"    {d['_file']}:{d['riga']}")
        print(f"      en: {d['en'][:100]}")
        print(f"      it: {d['it'][:100]}")
    print()
