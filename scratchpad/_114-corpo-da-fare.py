# -*- coding: utf-8 -*-
"""114a - Quante righe del CORPO restano da fare, categoria per categoria.

`_107-lotti-per-categoria.py` conta le righe **vive**, tradotte comprese, e
`_107-chiavi-item.py` le emette tutte allo stesso modo: nessuno dei due dice
quanto resta. La tabella «da dove si comincia la prossima volta» dei documenti
si scriveva a mano, e un numero scritto a mano invecchia senza dirlo.

Il corpo sono gli indici **0, 1 e 2** — l'indice 3 e' il rapporto di
identificazione, chiuso dalla 113a, e non si impagina.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_114-corpo-da-fare.py
"""
import io
import json
import subprocess
import sys

LAVORO = 'lavoro/_107-daitem.jsonl'
DIZIONARIO = 'dizionario/db_item.hsp.jsonl'
INDICI = (0, 1, 2)


def categorie():
    uscita = subprocess.run(
        [sys.executable, 'scratchpad/_107-lotti-per-categoria.py'],
        capture_output=True, text=True, encoding='utf-8', check=True).stdout
    nomi = []
    for linea in uscita.splitlines():
        pezzi = linea.split()
        if len(pezzi) == 3 and pezzi[2].startswith('FILTER_'):
            nomi.append(pezzi[2])
    return nomi


def righe_di(categoria, indice):
    uscita = subprocess.run(
        [sys.executable, 'scratchpad/_107-chiavi-item.py',
         '--categoria', categoria, '--indice', str(indice),
         '--da', '0', '--a', '999999', '--solo-righe'],
        capture_output=True, text=True, encoding='utf-8', check=True).stdout
    dentro = set()
    for linea in uscita.splitlines():
        if linea.startswith('    '):
            for pezzo in linea.replace(',', ' ').split():
                if pezzo.isdigit():
                    dentro.add(int(pezzo))
    return dentro


def main():
    # ⚠️ «reso» vuol dire che il dizionario ha un `it` non vuoto per QUELLA
    #    riga: e' la stessa domanda che fa `verifica --dizionario`, non un
    #    conteggio di firme.
    rese = set()
    for linea in io.open(DIZIONARIO, encoding='utf-8'):
        if linea.strip():
            d = json.loads(linea)
            if d.get('it'):
                rese.add(d['riga'])

    tabella = []
    for categoria in categorie():
        vive = set()
        for indice in INDICI:
            vive |= righe_di(categoria, indice)
        if vive:
            tabella.append((len(vive - rese), len(vive), categoria))

    tabella.sort(reverse=True)
    print('il CORPO di db_item.hsp (indici 0-2), quanto resta per categoria')
    print()
    print('  da fare   vive   categoria')
    print('  ---------------------------------------------')
    for da_fare, vive, categoria in tabella:
        print('  %7d %6d   %s' % (da_fare, vive, categoria))
    print()
    print('  TOTALE da fare: %d su %d vive'
          % (sum(t[0] for t in tabella), sum(t[1] for t in tabella)))
    return 0


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
