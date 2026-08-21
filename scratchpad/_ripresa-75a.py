# -*- coding: utf-8 -*-
"""75a — mette la nuova testa in `RIPRESA-sessione.md` e manda la 74a in storia.

Il file e' un registro che cresce in cima: la sessione appena finita prende il
posto della testa, e quella di prima diventa «(per storia)». Si fa con uno
script e non a mano perche' il file e' lungo 660 KB e una `Write` intera lo
riscriverebbe tutto.
"""
import io
import sys
from pathlib import Path

RIPRESA = Path('RIPRESA-sessione.md')
NUOVA = Path(r'C:\Users\old_p\AppData\Local\Temp\claude\C--Games-Elona'
             r'\06fe3995-31b7-4b26-bc2f-7f3bcb682873\scratchpad\ripresa75.md')

VECCHIA_TESTA = '## La settantaquattresima sessione\n'
NUOVA_TESTA = '## La settantaquattresima sessione (per storia)\n'


def main() -> int:
    testo = io.open(RIPRESA, encoding='utf-8').read()
    taglio = testo.find(VECCHIA_TESTA)
    if taglio < 0:
        print('non trovo %r' % VECCHIA_TESTA)
        return 1
    if testo.count(VECCHIA_TESTA) != 1:
        print('%r compare %d volte' % (VECCHIA_TESTA, testo.count(VECCHIA_TESTA)))
        return 1

    coda = NUOVA_TESTA + testo[taglio + len(VECCHIA_TESTA):]
    nuova = io.open(NUOVA, encoding='utf-8').read()
    io.open(RIPRESA, 'w', encoding='utf-8', newline='\n').write(nuova + coda)
    print('RIPRESA-sessione.md: testa nuova (%d caratteri), la 74a va in storia'
          % len(nuova))
    return 0


if __name__ == '__main__':
    sys.exit(main())
