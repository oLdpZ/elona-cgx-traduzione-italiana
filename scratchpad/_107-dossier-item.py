# -*- coding: utf-8 -*-
"""107a - Il dossier di un lotto di descrizioni di `db_item.hsp`.

⚠️ **La descrizione non si traduce da sola.** E' la stessa lezione per cui
esiste `_102-dossier.py` sulle carte: la prosa di un oggetto e il **nome** di
quell'oggetto sono l'unico posto in cui il giocatore vede le due cose vicine, e
se la prosa lo nomina deve nominarlo con quel nome. Qui pero' il nome non sta
venti righe sotto come nelle carte: le descrizioni stanno fra la riga 42.408 e
la 132.000, i nomi fra la 133.931 e la 152.824 — a novantamila righe di
distanza. A tenerli insieme e' l'`ITEM_ID`, che dalla 107a le descrizioni
portano.

⚠️⚠️ E i nomi da guardare sono **due**, non uno. `ioriginalnameref` e' il nome
dell'oggetto identificato; `iknownnameref` e' quello che porta **prima** di
essere identificato — «una gemma divina» contro «un anello di velocita'» — e
una descrizione che si legge sul pannello di un oggetto non identificato deve
tenerne conto. Vedi `contratto-nomi.md` §1-ter.

    python scratchpad/_107-dossier-item.py --categoria FILTER_ITEM_FOOD --indice 3
    python scratchpad/_107-dossier-item.py --da 42400 --a 43000
    python scratchpad/_107-dossier-item.py --categoria FILTER_WEAPON --solo-da-fare
"""
import argparse
import collections
import io
import json
import re
import sys

from strumenti.categorie import categorie
from strumenti.estrai import estrai_da_testo, spezza_righe
from strumenti.percorsi import DIZIONARIO, SORGENTE_HSP

FILE = 'db_item.hsp'
_INDICE = re.compile(r'^\s*description\((\d+)\)')


def _rese():
    """firma -> italiano, per le sole voci gia' rese."""
    percorso = DIZIONARIO / (FILE + '.jsonl')
    fuori = {}
    if percorso.exists():
        with io.open(percorso, encoding='utf-8') as f:
            for linea in f:
                if linea.strip():
                    voce = json.loads(linea)
                    if voce.get('it'):
                        fuori[voce['firma']] = voce['it']
    return fuori


def carica():
    testo = (SORGENTE_HSP / FILE).read_text(encoding='cp932')
    righe, _, _ = spezza_righe(testo)
    reso = _rese()
    voci = estrai_da_testo(FILE, testo)

    # i nomi, per ITEM_ID: la testa, il secondo pezzo, il non identificato
    nomi = collections.defaultdict(dict)
    for voce in voci:
        if 'array' not in voce:
            continue
        nomi[voce['oggetto']][voce['array']] = (
            voce['jp'], voce['en'], reso.get(voce['firma']))

    descrizioni = collections.defaultdict(dict)
    for voce in voci:
        if 'array' in voce:
            continue
        trovato = _INDICE.match(righe[voce['riga'] - 1])
        if trovato is None:
            continue
        descrizioni[voce['oggetto']][int(trovato.group(1))] = (
            voce['riga'], voce['jp'], voce['en'], reso.get(voce['firma']))
    return nomi, descrizioni


def _nome_composto(pezzi, quale):
    """(jp, en, it) del nome identificato, ricomposto dai suoi due riferimenti."""
    testa = pezzi.get(quale)
    if testa is None:
        return None
    coda = pezzi.get('ioriginalnameref2') if quale == 'ioriginalnameref' else None
    if coda is None or not coda[1]:
        return testa
    return tuple(
        (a or '') + ' ' + (b or '') if (a or b) else None
        for a, b in zip(testa, coda))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--categoria')
    ap.add_argument('--indice', type=int)
    ap.add_argument('--da', type=int)
    ap.add_argument('--a', type=int)
    ap.add_argument('--solo-da-fare', action='store_true')
    a = ap.parse_args()

    nomi, descrizioni = carica()
    mappa = categorie()

    quanti_oggetti = quante_righe = 0
    for oggetto in sorted(descrizioni,
                          key=lambda o: min(r for r, *_ in descrizioni[o].values())):
        categoria = mappa.get(oggetto, '(nessuna)')
        if a.categoria and categoria != a.categoria:
            continue
        voci = descrizioni[oggetto]
        scelte = {i: v for i, v in voci.items()
                  if (a.indice is None or i == a.indice)
                  and (a.da is None or v[0] >= a.da)
                  and (a.a is None or v[0] <= a.a)
                  and (not a.solo_da_fare or v[3] is None)}
        if not scelte:
            continue

        quanti_oggetti += 1
        pezzi = nomi.get(oggetto, {})
        identificato = _nome_composto(pezzi, 'ioriginalnameref')
        sconosciuto = pezzi.get('iknownnameref')

        print(f'=== {oggetto}   [{categoria}]')
        if identificato:
            print(f'    NOME      jp {identificato[0]}')
            print(f'              en {identificato[1]}')
            print(f'              IT {identificato[2]}')
        else:
            print('    ⚠️ NOME    non trovato nel dizionario: la prosa non ha '
                  'un nome a cui obbedire')
        if sconosciuto:
            print(f'    non ident. IT {sconosciuto[2]}   (en {sconosciuto[1]})')
        for indice in sorted(scelte):
            riga, jp, en, it = scelte[indice]
            quante_righe += 1
            marca = ' ⚠️ TETTO SECCO 69' if indice == 3 else ''
            print(f'    --- description({indice})  :{riga}{marca}')
            print(f'        JP  {jp}')
            print(f'        EN  {en}')
            if it:
                print(f'        IT  {it}')
        print()

    print(f'== {quanti_oggetti} oggetti, {quante_righe} descrizioni')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
