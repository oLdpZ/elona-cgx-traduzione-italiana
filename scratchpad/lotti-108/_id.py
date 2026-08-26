# -*- coding: utf-8 -*-
"""Il numero di un ITEM_ID, letto da `defines/mod.hsp` del sorgente pinnato.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-108/_id.py ITEM_ID_RATION ...

⚠️ Serve alla lista di passi: `spawn_item` vuole il **numero**, e un
identificativo ricordato a memoria costa piu' di un errore in un file, perche'
la lista si esegue alla cieca. Qui il numero si legge dal sorgente, non si
ricorda.
"""
import re
import sys

from strumenti.percorsi import SORGENTE_HSP

DEFINIZIONE = re.compile(r'^\s*#\w+\s+(?:global\s+)?(ITEM_ID_[A-Z0-9_]+)\s+(\S+)')


def main():
    testo = (SORGENTE_HSP / 'defines' / 'mod.hsp').read_text(encoding='cp932')
    mappa = {}
    for riga in testo.splitlines():
        trovato = DEFINIZIONE.match(riga)
        if trovato:
            mappa.setdefault(trovato.group(1), trovato.group(2))
    mancanti = []
    for nome in sys.argv[1:]:
        numero = mappa.get(nome)
        print(f'{numero if numero else "??":>6}  {nome}')
        if numero is None:
            mancanti.append(nome)
    if mancanti:
        sys.exit(f'⚠️ non definiti in mod.hsp: {mancanti}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
