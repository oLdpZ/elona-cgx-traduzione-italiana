# -*- coding: utf-8 -*-
"""Domande per il terzo lotto: `actlistn` porta l'articolo? e come si scrivono
gli striscioni dell'arena?"""
import glob
import io
import json
import re

DOMANDE = [
    ('actlistn (i nomi delle azioni di fila)',
     lambda d: 'actlistn' in (d.get('contesto') or '') or 'actlistn' in d['en']),
    ('striscioni *…* dell arena',
     lambda d: re.search(r'^\*.*\*$', d['en'].strip()) or re.search(r'^<.+>$', (d.get('it') or '').strip())),
    ('ubriaco / drunk',
     lambda d: re.search(r'\bdrunk', d['en'], re.I) or 'ubriac' in (d.get('it') or '').lower()),
    ('zaino / backpack',
     lambda d: re.search(r'backpack', d['en'], re.I) or 'zaino' in (d.get('it') or '').lower()),
    ('give up the game / ritiro',
     lambda d: re.search(r'give up', d['en'], re.I)),
    ('change equipment',
     lambda d: re.search(r'change your equipment|equipment', d['en'], re.I) and len(d['en']) < 45),
    ('ore giocate',
     lambda d: 'ElonaPlus' in d['en'] or 'hour' in d['en'] and 'playing' in d['en']),
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
        print(f"      en: {d['en'][:100]}")
        print(f"      it: {d['it'][:100]}")
    print()
