# -*- coding: utf-8 -*-
"""Le domande per il secondo lotto di `main.hsp`: rientro, navigazione, carro."""
import glob
import io
import json
import re

DOMANDE = [
    ('Return / 帰還',    lambda d: '帰還' in d['jp'] or re.search(r'\bReturn\b', d['en'])),
    ('sail / 船出',      lambda d: '船出' in d['jp'] or '乗船' in d['jp']
                                   or re.search(r'\bsail', d['en'], re.I)),
    ('cargo / 荷車',     lambda d: '荷車' in d['jp'] or re.search(r'\bcargo\b', d['en'], re.I)),
    ('Arasiel',          lambda d: 'rasiel' in d['en'] or 'ラシエル' in d['jp']),
    ('Garziem',          lambda d: 'arziem' in d['en'] or 'ガルジエム' in d['jp']),
    ('Amurdad',          lambda d: 'murdad' in d['en'] or 'ネヘルタード' in d['jp']),
    ('crime / 法を犯',    lambda d: '法を犯' in d['jp'] or re.search(r'commit a crime|\bcrime\b', d['en'], re.I)),
    ('burden/overweight', lambda d: re.search(r'overweight|burden|too heavy', d['en'], re.I)),
    ('dimensional door', lambda d: '次元' in d['jp'] or re.search(r'dimensional', d['en'], re.I)),
    ('ship arrived',     lambda d: re.search(r'\bship\b', d['en'], re.I)),
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
        if len(visti) > 14:
            print(f'    ... e altre {len(trovate) - 14}')
            break
        print(f"    {d['_file']}:{d['riga']}")
        print(f"      en: {d['en'][:105]}")
        print(f"      it: {d['it'][:105]}")
    print()
