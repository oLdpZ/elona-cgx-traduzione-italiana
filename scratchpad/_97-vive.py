# -*- coding: utf-8 -*-
"""Per ogni voce «da fare» di un file: TUTTE le occorrenze, e se sono vive o morte.

    python scratchpad/_97-vive.py <file.hsp> <restante.jsonl> <tutto.jsonl>

⚠️ Nasce nella 97a da `command.hsp:16289`. `estrai --da-tradurre` registra una
firma sulla **prima** occorrenza, e quella prima stava dentro un tratto
`/* ORIGINAL - BEGINNING … ENDING */` che il mod ha spento: sembrava una riga da
rinviare. Non lo era — **la stessa firma vive a `:16303`**, dentro l'`ANNA
CUSTOM` che ha sostituito il blocco vecchio.

Il referto distingue due casi, e la distinzione e' tutto il punto:

    MORTA   tutte le occorrenze della firma sono spente  ->  si puo' rinviare
    MISTA   almeno una e' viva                           ->  si traduce

Le tre forme di spegnimento che guarda sono quelle che si vedono dalla riga: il
commento di blocco, il ramo `if ( jp )`, il `;` in testa. ⚠️ Non vede la quinta
famiglia — la riga morta **per assegnazione** (`command.hsp:11066`) — perche'
quella non si legge da dove sta la riga.
"""
import collections
import io
import os
import re
import sys

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'

FILE = sys.argv[1] if len(sys.argv) > 1 else 'command.hsp'
RESTANTE = sys.argv[2] if len(sys.argv) > 2 else 'lavoro/_97-command-restante.jsonl'
TUTTO = sys.argv[3] if len(sys.argv) > 3 else 'lavoro/_97-command-tutto.jsonl'

import json

righe = io.open(os.path.join(SORGENTE, FILE), encoding='cp932',
                errors='replace').read().splitlines()

# righe dentro un commento di blocco
dentro_blocco = set()
aperto = False
for n, r in enumerate(righe, 1):
    if not aperto and '/*' in r and '*/' not in r.split('/*', 1)[1]:
        aperto = True
        continue
    if aperto:
        dentro_blocco.add(n)
        if '*/' in r:
            aperto = False
            dentro_blocco.discard(n)

# righe dentro un ramo if ( jp )
APRE_JP = re.compile(r'^\s*if\s*\(\s*jp\s*\)\s*\{')
STRINGA = '"(?:[^"' + chr(92) * 2 + ']|' + chr(92) * 2 + '.)*"'
dentro_jp, prof = set(), None
for n, r in enumerate(righe, 1):
    if prof is None:
        if APRE_JP.match(r):
            prof = 1
        continue
    dentro_jp.add(n)
    f = re.sub(STRINGA, '', r)
    prof += f.count('{') - f.count('}')
    if prof <= 0:
        dentro_jp.discard(n)
        prof = None

tutte = collections.defaultdict(list)
for l in io.open(TUTTO, encoding='utf-8'):
    if l.strip():
        v = json.loads(l)
        tutte[v['firma']].append(v['riga'])

dafare = [json.loads(l) for l in io.open(RESTANTE, encoding='utf-8') if l.strip()]


def stato(n):
    s = []
    if n in dentro_blocco:
        s.append('BLOCCO')
    if n in dentro_jp:
        s.append('IF-JP')
    if righe[n - 1].lstrip().startswith(';'):
        s.append('PUNTOEVIRGOLA')
    return '+'.join(s) or 'viva'


morte = miste = 0
for v in dafare:
    occ = sorted(set(tutte[v['firma']]))
    stati = [stato(n) for n in occ]
    if all(s != 'viva' for s in stati):
        morte += 1
        print(f"MORTA  {v['riga']:6d} en={v['en']!r}")
        for n, s in zip(occ, stati):
            print(f'          :{n} {s}')
    elif any(s != 'viva' for s in stati):
        miste += 1
        print(f"MISTA  {v['riga']:6d} en={v['en']!r}  ->  "
              + ', '.join(f':{n} {s}' for n, s in zip(occ, stati)))
print(f'--- {FILE}: {len(dafare)} da fare, {morte} tutte morte, {miste} miste')
