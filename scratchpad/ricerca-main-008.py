# -*- coding: utf-8 -*-
"""Domande per il finale di Lesimas: i nomi propri, il codice, il punteggio."""
import glob
import io
import json
import re

DOMANDE = [
    ('Zeome',       lambda d: re.search(r'zeome', d['en'], re.I) or 'ゼーメ' in d['jp']),
    ('codex / 秘宝', lambda d: re.search(r'\bcodex\b', d['en'], re.I) or '秘宝' in d['jp']),
    ('Eternal League / 盟約',
                    lambda d: re.search(r'eternal league|oath of', d['en'], re.I) or '盟約' in d['jp']),
    ('North Tyris', lambda d: re.search(r'north tyris', d['en'], re.I) or 'ノースティリス' in d['jp']),
    ('Remido',      lambda d: re.search(r'remido', d['en'], re.I) or 'レミード' in d['jp']),
    ('Eternal Seal / 神の間',
                    lambda d: re.search(r'eternal seal', d['en'], re.I) or '神の間' in d['jp']),
    ('score / punteggio',
                    lambda d: re.search(r'\bscore\b', d['en'], re.I)),
    ('cnvrank / livello di sotterraneo',
                    lambda d: 'cnvrank' in d['en'] or 'cnvrank' in (d.get('en_grezzo') or '')
                              or 'cnvrank' in (d.get('it') or '')),
    ('AKA / epiteto',
                    lambda d: 'CDATAN_AKA' in (d.get('en_grezzo') or '')),
    ('Trace / 軌跡', lambda d: '軌跡' in d['jp'] or d['en'].strip() == 'Trace'),
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
        print(f"      en: {d['en'][:105]}")
        print(f"      it: {d['it'][:105]}")
    print()
