# -*- coding: utf-8 -*-
"""Il MARGINE delle rese del lotto contro il tetto secco di 69, degradate.

Lo zero della rete dice «nessuna sfora»; questo dice **di quanto**, che e' il
numero che serve per sapere se la formula regge anche sulle categorie dopo.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-108/_margine.py
"""
import io
import json
import sys

from strumenti.accenti import degrada

TETTO = 69


def main():
    voci = [json.loads(l) for l in io.open('lavoro/fase5-db_item-001.jsonl',
                                           encoding='utf-8') if l.strip()]
    misurate = sorted(((len(degrada(v['it'])), len(v['en']), v['riga'], v['it'])
                       for v in voci), reverse=True)
    for lunghezza, en, riga, it in misurate[:5]:
        print(f'  :{riga:<7} {lunghezza:>3} car. degradati (inglese {en:>3})   {it}')
    print()
    piu_lunga = misurate[0][0]
    print(f'{len(voci)} rese: la piu\' lunga misura {piu_lunga} caratteri degradati '
          f'su {TETTO} di budget, margine {TETTO - piu_lunga}')
    piu_lunghe_dell_inglese = [m for m in misurate if m[0] > m[1]]
    print(f'rese piu\' lunghe del loro inglese: {len(piu_lunghe_dell_inglese)} su {len(voci)}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
