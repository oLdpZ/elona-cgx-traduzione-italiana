# -*- coding: utf-8 -*-
"""107a - Le descrizioni di `db_item.hsp` divise per CATEGORIA dell'oggetto.

Dalla 107a ogni descrizione porta l'`oggetto` del suo `if ( dbid == ITEM_ID_X )`,
e `categorie.py` sa mappare un ITEM_ID sulla sua categoria (`FILTER_ITEM_FOOD`,
`FILTER_FURNITURE`, …). Da cui: i lotti si scelgono per **famiglia di oggetti**
invece che per intervallo di righe.

⚠️ Non e' solo comodita'. Un lotto per categoria mette sotto gli occhi tutte le
armi insieme, e le decisioni di registro si prendono una volta per la famiglia
invece che una volta per riga — che e' il modo in cui, sulle carte, i nomi
sdoppiati sono sfuggiti fino alla 106a.

⭐ E dice anche quante descrizioni NON trovano il loro oggetto: quelle sono le
righe per cui il dossier non potra' pescare il nome italiano gia' reso, e vanno
sapute prima, non scoperte a lotto aperto.

    python scratchpad/_107-lotti-per-categoria.py
    python scratchpad/_107-lotti-per-categoria.py --indice 3
"""
import argparse
import collections

from strumenti.categorie import categorie
from strumenti.estrai import descrizioni_per_riga, estrai_da_testo, spezza_righe
from strumenti.percorsi import SORGENTE_HSP

FILE = 'db_item.hsp'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--indice', type=int, default=None,
                    help='solo un indice di description() (0-3)')
    a = ap.parse_args()

    testo = (SORGENTE_HSP / FILE).read_text(encoding='cp932')
    righe, _, _ = spezza_righe(testo)
    per_riga = descrizioni_per_riga(righe)
    mappa = categorie()

    import re
    indice_di = re.compile(r'^\s*description\((\d+)\)')

    voci = []
    for voce in estrai_da_testo(FILE, testo):
        if 'array' in voce:
            continue
        trovato = indice_di.match(righe[voce['riga'] - 1])
        if trovato is None:
            continue
        n = int(trovato.group(1))
        if a.indice is not None and n != a.indice:
            continue
        voci.append((voce['riga'], n, voce.get('oggetto'), voce['firma']))

    senza = [r for r, _, o, _ in voci if o is None]
    print(f'{FILE}: {len(voci)} descrizioni vive'
          + (f' (solo indice {a.indice})' if a.indice is not None else ''))
    print(f'  con l\'oggetto : {len(voci) - len(senza)}')
    print(f'  ⚠️ SENZA       : {len(senza)}'
          + ('   -> il dossier non potra\' pescare il nome' if senza else ''))
    for r in senza[:10]:
        print(f'      :{r}')

    conta = collections.Counter()
    firme = collections.defaultdict(set)
    for _, _, oggetto, firma in voci:
        categoria = mappa.get(oggetto, '(nessuna)') if oggetto else '(senza oggetto)'
        conta[categoria] += 1
        firme[categoria].add(firma)

    print()
    print('  righe  firme  categoria')
    print('  ' + '-' * 46)
    for categoria, quante in conta.most_common():
        print(f'  {quante:>5}  {len(firme[categoria]):>5}  {categoria}')
    print(f'  {sum(conta.values()):>5}  {len(set(f for s in firme.values() for f in s)):>5}  TOTALE')


if __name__ == '__main__':
    main()
