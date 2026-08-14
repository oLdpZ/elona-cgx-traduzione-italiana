# -*- coding: utf-8 -*-
"""Le ricerche nel dizionario che servono al lotto 014, tutte in un colpo."""
import glob
import io
import json

voci = []
for p in sorted(glob.glob('dizionario/*.jsonl')):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it'):
            voci.append((nome, d.get('riga'), d.get('jp') or '', d.get('en') or '', d['it']))

DOMANDE = [
    ('attributi (skill.hsp, prime voci)',
     lambda n, jp, en, it: n == 'skill.hsp.jsonl' and any(
         x in en for x in ('Strength', 'Constitution', 'Dexterity', 'Perception',
                           'Learning', 'Will', 'Magic', 'Charisma', 'Speed', 'Luck'))),
    ('dèi', lambda n, jp, en, it: any(x in en for x in ('Lulwy', 'Ehekatl', 'Mani ', 'Itzpalt',
                                                        'Jure', 'Kumiromi', 'Opatos', 'Yacatect'))),
    ('fede / faith', lambda n, jp, en, it: 'faith' in en.lower() or '信仰' in jp),
    ('livello / level', lambda n, jp, en, it: 'レベル' in jp and len(jp) < 40),
    ('bonus', lambda n, jp, en, it: 'bonus' in en.lower() and len(en) < 50),
    ('消え去った / vanish', lambda n, jp, en, it: 'vanish' in en.lower() or '消え去' in jp),
    ('察知/感知 sense', lambda n, jp, en, it: '察知' in jp or '感知' in jp),
    ('時を止め / stop time', lambda n, jp, en, it: '時' in jp and ('止' in jp or 'time' in en.lower())),
    ('記憶 / memory', lambda n, jp, en, it: '記憶' in jp),
    ('巻物 scroll (frasi)', lambda n, jp, en, it: '消費する' in jp or 'Which scroll' in en),
    ('絡みつ / entangle', lambda n, jp, en, it: 'entangl' in en.lower() or '絡みつ' in jp),
    ('proc.hsp: sangue/forza', lambda n, jp, en, it: n == 'proc.hsp.jsonl' and ('血' in jp or 'sangue' in it)),
]

for titolo, prova in DOMANDE:
    print('=' * 70)
    print('###', titolo)
    trovate = [v for v in voci if prova(v[0], v[2], v[3], v[4])]
    for nome, riga, jp, en, it in trovate[:16]:
        print(f'  {nome}:{riga}  jp={jp[:34]}  en={en[:50]}\n      -> {it[:88]}')
    if len(trovate) > 16:
        print(f'  ... e altre {len(trovate) - 16}')
    if not trovate:
        print('  (niente)')
