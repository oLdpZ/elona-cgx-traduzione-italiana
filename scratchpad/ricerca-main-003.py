# -*- coding: utf-8 -*-
"""Terza tornata: come il progetto chiama le nefia casuali, il maltempo e i vicini."""
import glob
import io
import json
import re

DOMANDE = [
    ('nefia casuali',   lambda d: 'ランダムネフィア' in d['jp'] or re.search(r'random.{0,4}nefia', d['en'], re.I)
                                  or 'casual' in d['it'].lower() and 'efia' in d['it']),
    ('dungeon / labirinto', lambda d: re.search(r'\bdungeon', d['en'], re.I)),
    ('quiet / si calma', lambda d: re.search(r'\bquiet', d['en'], re.I)),
    ('etere (it)',      lambda d: 'etere' in d['it'].lower()),
    ('maltempo',        lambda d: 'maltempo' in d['it'].lower() or 'weather' in d['en'].lower()),
    ('nap it',          lambda d: 'pisolin' in d['it'].lower() or 'sonnellin' in d['it'].lower()),
    ('endure',          lambda d: re.search(r'\bendure', d['en'], re.I)),
    ('Day breaks',      lambda d: re.search(r'day break|dawn|daybreak', d['en'], re.I)),
    ('vento (it)',      lambda d: re.search(r'\bvento\b', d['it'], re.I)),
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
