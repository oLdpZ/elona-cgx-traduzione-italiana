# -*- coding: utf-8 -*-
"""125a - Quante sostituzioni in piu' deve fare `applica` dopo questo lotto.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_125-previsione.py

⚠️ La previsione si fa **contando il sorgente**, non leggendo la tabella (116a):
una riga puo' avere una **gemella** con giapponese e inglese identici byte per
byte, cioe' stessa firma, e allora una resa sola copre due righe. In questo file
succede piu' volte — «むむむ。», «すまんのう。», «出直す», «足りないんよ» sono
ripetute nei due rami — e contare le voci del dizionario darebbe 26 dove le
righe toccate sono di piu'.
"""
import io
import json
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
sys.path.insert(0, RADICE)

from strumenti import estrai, percorsi  # noqa: E402

FILE = 'custom_itemenchantment.hsp'


def main():
    dizionario = {}
    percorso = os.path.join(RADICE, 'dizionario', FILE + '.jsonl')
    for r in io.open(percorso, encoding='utf-8'):
        v = json.loads(r)
        dizionario[v['firma']] = v

    sorgente = percorsi.SORGENTE_HSP / FILE
    testo = sorgente.read_text(encoding='cp932')

    conta = {}
    for sito in estrai.siti(testo):
        numero_riga, chiave = sito[0], sito[1]
        conta.setdefault(chiave, []).append(numero_riga)

    righe = 0
    for firma, voce in sorted(dizionario.items(), key=lambda x: x[1]['riga']):
        dove = conta.get(firma, [])
        righe += len(dove)
        if len(dove) != 1:
            print('  :%-5d %-2d righe  %s' % (voce['riga'], len(dove),
                                              ', '.join(str(d) for d in dove)))
    print('')
    print('voci di dizionario   %d' % len(dizionario))
    print('righe del sorgente   %d   <- la previsione, piu\' 3 di toppa = %d'
          % (righe, righe + 3))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
