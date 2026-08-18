# -*- coding: utf-8 -*-
"""Le ultime parole da fissare per chiudere main.hsp."""
import glob
import io
import json
import re
from pathlib import Path

DOMANDE = [
    ('死紋 / Death-Crest',
     lambda d: '死紋' in d['jp'] or re.search(r'death.?crest', d['en'], re.I)),
    ('守護者 / lord of, guardian',
     lambda d: '守護者' in d['jp'] or re.search(r'\blord of\b|\bguardian\b', d['en'], re.I)),
    ('護衛 / escort',
     lambda d: '護衛' in d['jp'] or re.search(r'\bescort\b', d['en'], re.I)),
    ('封印 / seal',
     lambda d: '封印' in d['jp'] or re.search(r'\bseal\b', d['en'], re.I)),
    ('名声 / fame',
     lambda d: '名声' in d['jp'] or re.search(r'\bfame\b', d['en'], re.I)),
    ('ether blaster',
     lambda d: re.search(r'ether ?blaster', d['en'], re.I) or 'エーテルブラスター' in d['jp']),
    ('肉塊 / mass of flesh',
     lambda d: '肉塊' in d['jp'] or re.search(r'mass of flesh', d['en'], re.I)),
    ('chestnut giant / 栗',
     lambda d: re.search(r'chestnut', d['en'], re.I) or '栗' in d['jp']),
    ('Meshera',
     lambda d: re.search(r'meshera', d['en'], re.I)),
    ('最深層 / deepest level',
     lambda d: '最深層' in d['jp'] or re.search(r'deepest level', d['en'], re.I)),
    ('クエスト / quest',
     lambda d: re.search(r'^quest$|for the quest', d['en'], re.I) or 'クエスト' in d['jp']),
    ('asterisco nudo',
     lambda d: d['en'].strip() == '*'),
    ('マダニ / tick, deer',
     lambda d: re.search(r'\btick\b|\bdeer\b', d['en'], re.I)),
]

voci = []
for p in sorted(glob.glob('dizionario/*.jsonl')):
    nome = Path(p).name.replace('.jsonl', '')
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
        if len(visti) > 6:
            print(f'    ... e altre {len(trovate) - 6}')
            break
        print(f"    {d['_file']}:{d['riga']}")
        print(f"      jp: {d['jp'][:80]}")
        print(f"      en: {d['en'][:80]}")
        print(f"      it: {d['it'][:80]}")
    print()
