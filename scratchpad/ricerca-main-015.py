# -*- coding: utf-8 -*-
"""Il vocabolario della zona 7000: gli otto dèi col loro epiteto, il Fattore
Decisivo, il dio del Caos, i ninja, il formato «X says:»."""
import glob
import io
import json
import re
from pathlib import Path

DOMANDE = [
    ('決戦因子 / Deciding Factor',
     lambda d: '決戦因子' in d['jp'] or re.search(r'deciding factor', d['en'], re.I)),
    ('混沌の神 / God of Chaos',
     lambda d: '混沌の神' in d['jp'] or re.search(r'god of chaos', d['en'], re.I)),
    ('Mani, epiteto',     lambda d: 'マニ' in d['jp'] and len(d['jp']) < 30),
    ('Lulwy, epiteto',    lambda d: 'ルルウィ' in d['jp'] and len(d['jp']) < 30),
    ('Itzpalt, epiteto',  lambda d: 'イツパロトル' in d['jp'] and len(d['jp']) < 30),
    ('Ehekatl, epiteto',  lambda d: 'エヘカトル' in d['jp'] and len(d['jp']) < 30),
    ('Opatos, epiteto',   lambda d: 'オパートス' in d['jp'] and len(d['jp']) < 30),
    ('Jure, epiteto',     lambda d: 'ジュア' in d['jp'] and len(d['jp']) < 30),
    ('Kumiromi, epiteto', lambda d: 'クミロミ' in d['jp'] and len(d['jp']) < 30),
    ('Yacatect, epiteto', lambda d: 'ヤカテクト' in d['jp'] and len(d['jp']) < 30),
    ('忍 / ninja',        lambda d: re.search(r'\bninja', d['en'], re.I)),
    ('«X says:» / dice',  lambda d: re.search(r'\bsays:', d['en'])),
    ('害獣 / vermin',     lambda d: '害獣' in d['jp'] or re.search(r'\bvermin\b', d['en'], re.I)),
    ('駆除 / get rid of', lambda d: '駆除' in d['jp']),
    ('合格 / you passed', lambda d: '合格' in d['jp'] or re.search(r'you passed', d['en'], re.I)),
    ('Tezcatlipoca',      lambda d: re.search(r'tezcatlipoca', d['en'], re.I)),
    ('Leold / Talon',     lambda d: re.search(r'\bLeold\b|talon soldier', d['en'], re.I)),
    ('Pael',              lambda d: 'パエル' in d['jp'] or re.search(r'\bPael\b', d['en'])),
    ('cargo / merci',     lambda d: re.search(r'\bcargo\b', d['en'], re.I)),
    ('you lost / perso',  lambda d: re.search(r'^you lost ', d['en'], re.I)),
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
        print(f"      jp: {d['jp'][:85]}")
        print(f"      en: {d['en'][:85]}")
        print(f"      it: {d['it'][:85]}")
    print()
