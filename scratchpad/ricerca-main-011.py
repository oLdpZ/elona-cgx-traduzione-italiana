# -*- coding: utf-8 -*-
"""Domande per la zona 5000-5999 di main.hsp: Lesimas, le riunioni, i dieci
compagni che si rialzano, il matrimonio."""
import glob
import io
import json
import re

DOMANDE = [
    # --- i luoghi e gli artefatti della trama principale
    ('神の間 / Eternal Seal',
     lambda d: '神の間' in d['jp'] or re.search(r'eternal seal', d['en'], re.I)),
    ('来光の牙 / Origin of Light',
     lambda d: '来光の牙' in d['jp'] or re.search(r'origin of light', d['en'], re.I)),
    ('常闇の眼 / Origin of Vice',
     lambda d: '常闇の眼' in d['jp'] or re.search(r'origin of vice', d['en'], re.I)),
    ('真実の書 / bottom of Lesimas',
     lambda d: '真実の書' in d['jp'] or re.search(r'lesimas', d['en'], re.I)),
    ('Enthumesis',
     lambda d: 'エンテュメイシス' in d['jp'] or 'nthumesis' in d['en']),
    ('アストラル / astral',
     lambda d: 'アストラル' in d['jp'] or re.search(r'astral', d['en'], re.I)),

    # --- il messaggio del compagno che si rialza (il classico di Elona)
    ('仲間になりたそう / wants to be friends',
     lambda d: '仲間になりたそう' in d['jp'] or re.search(r'want to be friends|befriend', d['en'], re.I)),
    ('トドメを刺す / stab .. coffin',
     lambda d: 'トドメ' in d['jp'] or re.search(r'in the coffin', d['en'], re.I)),

    # --- i nomi delle nove creature che si rialzano
    ('orco / orc',      lambda d: re.search(r'\borcs?\b', d['en'], re.I)),
    ('mad scientist',   lambda d: re.search(r'mad scientist', d['en'], re.I)),
    ('fallen angel',    lambda d: re.search(r'fallen angel|\bIsca\b', d['en'], re.I)),
    ('dungeon cleaner', lambda d: re.search(r'dungeon cleaner', d['en'], re.I)),
    ('white tiger',     lambda d: re.search(r'white tiger|\bLityou\b', d['en'], re.I)),
    ('knight (Muder)',  lambda d: re.search(r'murder knight|muder', d['en'], re.I)),
    ('Sunrise / drago', lambda d: re.search(r'\bSunrise\b', d['en'])),
    ('wing snail',      lambda d: re.search(r'wing snail|winged snail', d['en'], re.I)),
    ('Pascal / cane',   lambda d: re.search(r'\bPascal\b', d['en'])),
    ('Goda',            lambda d: re.search(r'\bGoda\b', d['en'])),

    # --- le voci di parentela dei due menu di riunione
    ('sorella/fratello/maggiordomo',
     lambda d: re.search(r"^(an? )?(older |little )?(sister|brother|girl|boy|butler|young lady)!?$", d['en'].strip(), re.I)),
    ('cane/gatto/orso di menu',
     lambda d: re.search(r"^a (dog|cat|bear)!$", d['en'].strip(), re.I)),

    # --- il matrimonio
    ('matrimonio / marriage',
     lambda d: re.search(r'\bmarriage\b|\bwedding\b|eternal love|united in marriage', d['en'], re.I)),
    ('compleanno / birthday',
     lambda d: re.search(r'happy birthday|birthday', d['en'], re.I)),
    ('destinazione / arrive at your destination',
     lambda d: re.search(r'arrive at your destination', d['en'], re.I)),
    ('cadaveri che si rialzano / corpses rise',
     lambda d: re.search(r'corpses rise|set foot on this floor', d['en'], re.I)),
    ('Marka the silver bear',
     lambda d: re.search(r'\bMarka\b|silver bear', d['en'], re.I)),
    ('assassini di Zanan',
     lambda d: re.search(r'zanan', d['en'], re.I)),
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
        print(f"      jp: {d['jp'][:90]}")
        print(f"      en: {d['en'][:90]}")
        print(f"      it: {d['it'][:90]}")
    print()
