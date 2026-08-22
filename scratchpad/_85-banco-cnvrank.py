# -*- coding: utf-8 -*-
"""Il banco della 85a: si puo' concatenare una DIVISIONE dentro una stringa?

`cnvrank(x)` e' morfologia inglese (init.hsp:150: `if (jp) return "" + x`), e
per toglierla dalle rese bisogna concatenare l'argomento nudo. Ma due dei
quattro siti passano un'espressione — `cnvrank(rankorg / 100)` — e **HSP non ha
precedenza fra gli operatori**: valuta da sinistra a destra, quindi
`"Rango: " + rankorg / 100` sarebbe `("Rango: " + rankorg) / 100`.

La domanda e' se le parentesi bastano. Si prova sul motore vero.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from banco_hsp import Banco  # noqa: E402

b = Banco("cnvrank")
b.testa(jp=0, en=1)
b.coda('''
*_banco_avvio
	rankorg = 350
	tappa "1 divisione fra parentesi : " + (rankorg / 100)
	tappa "2 divisione nuda          : " + rankorg / 100
	tappa "3 numero nudo             : " + rankorg
	tappa "4 due parentesi           : " + (rankorg / 100) + " -> " + (rankorg / 100 + 1)
''')
print(b.esegui(secondi=40))
