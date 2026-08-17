# -*- coding: utf-8 -*-
"""Le domande strette: la prima tornata pescava «brain» e «train» dentro «rain»."""
import glob
import io
import json
import re

DOMANDE = [
    ('pioggia (jp 雨)',    lambda d: '雨' in d['jp']),
    ('neve (jp 雪)',       lambda d: '雪' in d['jp']),
    ('sonno (jp 眠)',      lambda d: '眠' in d['jp']),
    ('alba / notte',       lambda d: '夜が明' in d['jp'] or '朝' in d['jp'] or 'ightfall' in d['en']),
    ('giorno buono 日和',   lambda d: '日和' in d['jp']),
    ('shelter',            lambda d: re.search(r'\bshelter', d['en'], re.I)),
    ('un giorno passa',    lambda d: '一日' in d['jp'] or '日付' in d['jp']),
    ('熱狂 / frenesia',     lambda d: '熱狂' in d['jp'] or 'frenes' in d['it'].lower()),
    ('静ま / si calma',     lambda d: '静ま' in d['jp']),
    ('brace/no escape',    lambda d: 'no escape' in d['en'].lower() or 'brace' in d['en'].lower()),
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
