# -*- coding: utf-8 -*-
"""125a - Le «non ancora tradotte» di `verifica --dizionario` sono le rinviate?

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_125-non-tradotte.py

⚠️ `RIPRESA-sessione.md` dava come valore atteso «tutti 0 e 0, tranne etc.hsp 1
non tradotta». In apertura della 125a il referto ne conta **molte di piu'**, in
diciannove file. La domanda non e' «e' un guasto?» ma **«di chi sono quelle
righe?»**: `confronta_col_sorgente` (`verifica.py:619`) fa
`nel_sorgente - set(tradotte)` e **non toglie le rinviate**, quindi il valore
atteso non poteva essere zero nemmeno il giorno in cui e' stato scritto.

Questo script risponde alla domanda giusta: le non tradotte coincidono con
`rinviate.jsonl`, oppure ce n'e' qualcuna che nessuno ha deciso di rinviare?
Il numero da guardare e' l'ultimo — **fuori dalle rinviate**, che e' il lavoro
vero che nessun referto stava mostrando.
"""
import io
import json
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
sys.path.insert(0, RADICE)

from strumenti import percorsi  # noqa: E402
from strumenti.estrai import estrai_da_testo  # noqa: E402


def main():
    rinviate = set()
    for r in io.open(os.path.join(RADICE, 'rinviate.jsonl'), encoding='utf-8'):
        if r.strip():
            rinviate.add(json.loads(r)['firma'])
    print('rinviate.jsonl: %d firme\n' % len(rinviate))

    totale = coperte = scoperte = 0
    for percorso in sorted(percorsi.DIZIONARIO.glob('*.jsonl')):
        nome = percorso.stem
        sorgente = percorsi.SORGENTE_HSP / nome
        if not sorgente.exists():
            continue
        tradotte = set()
        for r in io.open(percorso, encoding='utf-8'):
            v = json.loads(r)
            if v.get('it'):
                tradotte.add(v['firma'])
        testo = sorgente.read_bytes().decode('cp932')
        nel_sorgente = {v['firma'] for v in estrai_da_testo(nome, testo)}
        mancanti = nel_sorgente - tradotte
        if not mancanti:
            continue
        fuori = mancanti - rinviate
        totale += len(mancanti)
        coperte += len(mancanti & rinviate)
        scoperte += len(fuori)
        print('  %-28s %3d non tradotte, %3d rinviate, %3d FUORI'
              % (nome, len(mancanti), len(mancanti & rinviate), len(fuori)))
        for f in sorted(fuori)[:5]:
            print('        %s' % f)

    print('')
    print('non tradotte in tutto          %d' % totale)
    print('  di cui rinviate (decise)     %d' % coperte)
    print('  FUORI dalle rinviate         %d   <- il numero che conta' % scoperte)
    return 1 if scoperte else 0


if __name__ == '__main__':
    raise SystemExit(main())
