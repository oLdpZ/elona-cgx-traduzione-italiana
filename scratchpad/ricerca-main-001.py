# -*- coding: utf-8 -*-
"""Le domande da fare al dizionario prima del primo lotto di `main.hsp`.

La zona 1174-1540 e' il registro del mondo: meteo, vento etereo, ciclo del
giorno, nefia. Quasi tutti termini che altri file hanno gia' dovuto nominare.
"""
import glob
import io
import json

DOMANDE = [
    ('Etherwind',        lambda d: 'therwind' in d['en'] or 'エーテルの風' in d['jp']),
    ('Nefia',            lambda d: 'efia' in d['en'] or 'ネフィア' in d['jp']),
    ('fever / 熱狂',      lambda d: 'fever' in d['en'].lower() or '熱狂' in d['jp']),
    ('pioggia',          lambda d: 'rain' in d['en'].lower() or '雨' in d['jp']),
    ('neve',             lambda d: 'snow' in d['en'].lower() or '雪' in d['jp']),
    ('nap / sonno',      lambda d: 'nap' in d['en'].lower() or 'sleepiness' in d['en'].lower()
                                   or '眠気' in d['jp'] or '仮眠' in d['jp']),
    ('Day breaks / alba', lambda d: 'day break' in d['en'].lower() or '夜が明け' in d['jp']),
    ('perfect day',      lambda d: 'perfect day' in d['en'].lower() or '日和' in d['jp']),
    ('shelter / riparo', lambda d: 'shelter' in d['en'].lower()),
    ('brace / rifugio',  lambda d: 'brace' in d['en'].lower()),
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
    for d in trovate[:14]:
        chiave = (d['en'], d['it'])
        if chiave in visti:
            continue
        visti.add(chiave)
        print(f"    {d['_file']}:{d['riga']}")
        print(f"      en: {d['en'][:110]}")
        print(f"      it: {d['it'][:110]}")
    print()
