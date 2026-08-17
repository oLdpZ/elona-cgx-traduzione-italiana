# -*- coding: utf-8 -*-
"""La prova che la correzione della rete 4 (57a) non le toglie potere.

La rete 4 raggruppava per `(giapponese, funzioni di contenuto)` e bocciava due
rese diverse nello stesso gruppo. Dalla 57a la chiave porta anche **l'inglese**,
perche' upstream distingue anche con le parole e non solo con le funzioni
(`main.hsp:4151` e `:4232`, i due finali di Tyris del Sud).

La domanda da misurare e' una sola: **fra i giapponesi che il progetto ha reso
in piu' di un modo, quanti avevano anche l'inglese diverso?** Quelli sono i casi
che la rete vecchia avrebbe bocciato a torto; gli altri sono quelli per cui la
rete e' nata, e la rete nuova continua a prenderli.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import sys

_spec = importlib.util.find_spec('strumenti.funzioni')
if _spec is None:
    sys.exit('serve PYTHONPATH sulla radice del repo')
from strumenti.funzioni import funzioni_di_contenuto

LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


def firma_di(v) -> tuple:
    if v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v.get('en_grezzo') or ''))


voci = []
for p in sorted(glob.glob('dizionario/*.jsonl')):
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            voci.append(d)

# la chiave VECCHIA: (giapponese, funzioni)
gruppi = collections.defaultdict(list)
for v in voci:
    gruppi[(v['jp'], firma_di(v))].append(v)

divergenti = {k: g for k, g in gruppi.items()
              if len({parole(v['it']) for v in g}) > 1}

inglese_uguale = []
inglese_diverso = []
for k, g in divergenti.items():
    if len({v['en'] for v in g}) > 1:
        inglese_diverso.append((k, g))
    else:
        inglese_uguale.append((k, g))

print(f'voci col giapponese e la resa: {len(voci)}')
print(f'gruppi (giapponese, funzioni): {len(gruppi)}')
print(f'gruppi resi in piu\' di un modo: {len(divergenti)}')
print()
print(f'  con lo stesso inglese  : {len(inglese_uguale):>4}'
      f'   <- la rete vecchia e la nuova li prendono tutt\'e due')
print(f'  con inglese diverso    : {len(inglese_diverso):>4}'
      f'   <- la rete vecchia li bocciava a torto')
print()
print('I primi dieci con inglese diverso, cioe' + chr(39) + ' quelli che la correzione libera:')
for (jp, _f), g in sorted(inglese_diverso, key=lambda x: str(x[0]))[:10]:
    print(f'  jp={jp[:46]!r}')
    for v in g:
        print(f'     {v["file"]}:{v["riga"]}  en={v["en"][:58]!r}')
        print(f'        it={v["it"][:58]!r}')

print()
print('=' * 70)
print('TUTTI quelli con lo STESSO inglese: sono la famiglia per cui la rete e'
      + chr(39) + ' nata,')
print('e vanno guardati uno per uno — una divergenza qui non ha nessuna scusa')
print('di monte, o e' + chr(39) + ' una scelta consapevole o e'
      + chr(39) + ' una svista.')
for (jp, _f), g in sorted(inglese_uguale, key=lambda x: str(x[0])):
    print()
    print(f'  jp={jp[:60]!r}')
    print(f'  en={g[0]["en"][:60]!r}')
    for v in g:
        print(f'     {v["file"]}:{v["riga"]}  it={v["it"][:66]!r}')
