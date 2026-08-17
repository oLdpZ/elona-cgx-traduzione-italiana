# -*- coding: utf-8 -*-
"""Le quattro domande rimaste della zona 5000: il libro della verita', la
formula «vuole unirsi», le voci di parentela, il matrimonio."""
import glob
import io
import json
import re

DOMANDE = [
    ('真実の書 / Book of Truth',
     lambda d: '真実の書' in d['jp'] or re.search(r'book of truth', d['en'], re.I)),
    ('«si unisce» / joins your party',
     lambda d: re.search(r'joins your party|becomes your ally|your ally|join(s)? you\b', d['en'], re.I)),
    ('«vuole unirsi» / wants to join',
     lambda d: re.search(r'wants? to join|want to be your|ally\?', d['en'], re.I)),
    ('妹 sorella minore',  lambda d: d['jp'].strip('"') in ('妹', '妹だ！') or re.search(r'^(a )?(younger )?sister!?$', d['en'].strip(), re.I)),
    ('弟 fratello minore', lambda d: '弟' in d['jp'] or re.search(r'^(a )?(younger )?brother!?$', d['en'].strip(), re.I)),
    ('兄 fratello maggiore', lambda d: '兄' in d['jp'] and len(d['jp']) < 12),
    ('お嬢様 / young lady', lambda d: 'お嬢様' in d['jp']),
    ('クマ / bear',        lambda d: re.search(r'\bbear\b', d['en'], re.I)),
    ('犬・猫 / dog, cat',  lambda d: re.search(r'^(a )?(dog|cat)!?$', d['en'].strip(), re.I)),
    ('誓う / pledge, vow', lambda d: re.search(r'pledge|\bvow\b|eternal love', d['en'], re.I) or '誓' in d['jp']),
    ('祝儀 / gift, ceremony', lambda d: re.search(r'wedding|ceremony', d['en'], re.I)),
    ('生涯 / life has no meaning', lambda d: '生涯' in d['jp'] or re.search(r'life has no meaning', d['en'], re.I)),
    ('プレゼント / present', lambda d: re.search(r'^present$|a present', d['en'], re.I)),
    ('屍 / corpse', lambda d: '屍' in d['jp'] or re.search(r'\bcorpses?\b', d['en'], re.I)),
    ('銀髪 / silver hair', lambda d: '銀髪' in d['jp'] or re.search(r'silver.hair', d['en'], re.I)),
    ('同族 / same genus', lambda d: '同族' in d['jp'] or re.search(r'same genus|same kind', d['en'], re.I)),
    ('目的地 / destination', lambda d: '目的地' in d['jp'] or re.search(r'destination', d['en'], re.I)),
    ('咆哮 / roar', lambda d: '咆哮' in d['jp'] or re.search(r'\broar', d['en'], re.I)),
    ('間に合った / went well', lambda d: '間に合' in d['jp']),
    ('こんごともよろしく', lambda d: 'よろしく' in d['jp'] or re.search(r'thanks in advance', d['en'], re.I)),
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
        if len(visti) > 7:
            print(f'    ... e altre {len(trovate) - 7}')
            break
        print(f"    {d['_file']}:{d['riga']}")
        print(f"      jp: {d['jp'][:88]}")
        print(f"      en: {d['en'][:88]}")
        print(f"      it: {d['it'][:88]}")
    print()
