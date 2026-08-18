# -*- coding: utf-8 -*-
"""Il nome dell'oggetto contro i tetti della finestra dell'equipaggiamento.

⚠️ **Referto da leggere, non guardia**: qui non c'e' una soglia da tenere a
zero. I nomi sforano per costruzione, e quel che serve sapere e' **quanto** e
**se piu' dell'inglese**. Stesso mestiere di `tetti_buffdesc.py`.

## Da dove viene il tetto

Misurato a schermo il 2026-08-18 (58a), su tre schermate della stessa finestra.
Il taglio sta in `command.hsp:12741` ed e' di upstream (il mod MMAH):

    if ( showresist ) {
        equipinfo_mmah p(1), wx + 260 + (showresist == 1) * 100, ...
        s = strmid(s, 0, 12 + (showresist == 1) * 14)
    }

    showresist == 0   nessun taglio     il nome si vede INTERO (visto a schermo)
    showresist == 1   26 -> 28 caratteri   le sigle degli elementi
    showresist >= 2   12 -> 14 caratteri   le pagine delle abilita'

⚠️ **Non e' un `sdim` frainteso**: e' uno `strmid`, cioe' un taglio vero — la
distinzione che la 55a ha pagato per imparare. E il rimedio esiste gia' nel
gioco: il tasto `z` spegne la colonna e il nome torna intero.

## Perche' l'italiano soffre piu' dell'inglese

Perche' le qualifiche vanno in **coda**:

    a cursed bronze helmet [0,1]              28
    un elmo di bronzo [0,1] con maledizione   39

Non e' una resa lunga: e' la struttura della lingua. ⚠️ E il tetto **mordeva
gia' l'inglese**: degli stessi sette oggetti visti a schermo ne sforavano tre
anche in inglese.

## La toppa, e quel che NON fa

`toppe.jsonl` alza il primo addendo da 12 a 14, cioe' 26 -> 28 e 12 -> 14.
⭐ Non allarga la colonna: **recupera lo spazio che il taglio buttava via**, 28
px misurati fra la fine del nome e la prima sigla. ⚠️ Due caratteri su nomi che
ne vogliono trentadue: non risolve, e questo referto serve a non dimenticarlo.
"""
import io
import json
from pathlib import Path

from strumenti.accenti import degrada

# i tetti dopo la toppa; prima erano 26 e 12
TETTO_RESISTENZE = 28
TETTO_ABILITA = 14

# quel che la finestra aggiunge al nome base e che questo referto NON vede:
# l'articolo («un », «una », «uno ») e i numeri fra parentesi («[0,3]»).
# Misurato sulle sette righe della schermata del 2026-08-18: fra 5 e 15 caratteri.
CODA_MINIMA = 3 + 6


def lungo(testo: str) -> int:
    return len(degrada(testo))


def nomi_di(percorso: Path) -> list[dict]:
    voci = [json.loads(l) for l in
            io.open(percorso, encoding='utf-8').read().splitlines() if l.strip()]
    return [v for v in voci if v.get('it') and v.get('en') and len(v['en']) < 60]


def main() -> int:
    nomi = nomi_di(Path('dizionario/db_item.hsp.jsonl'))
    righe = [(lungo(v['it']), lungo(v['en']), v['riga'], v['it']) for v in nomi]

    print(f'nomi di oggetto misurati: {len(righe)}\n')
    print('                                 italiano      inglese')
    for nome, tetto in (('sigle degli elementi', TETTO_RESISTENZE),
                        ('pagine delle abilita', TETTO_ABILITA)):
        it = sum(1 for r in righe if r[0] > tetto)
        en = sum(1 for r in righe if r[1] > tetto)
        print(f'  {nome:<22} tetto {tetto:2d}   {it:5d} ({100 * it // len(righe):2d}%)'
              f'   {en:5d} ({100 * en // len(righe):2d}%)')

    print(f'\n⚠️ e col solo articolo e i numeri in coda (+{CODA_MINIMA}), che a schermo '
          f'ci sono sempre:')
    for nome, tetto in (('sigle degli elementi', TETTO_RESISTENZE),
                        ('pagine delle abilita', TETTO_ABILITA)):
        vero = tetto - CODA_MINIMA
        it = sum(1 for r in righe if r[0] > vero)
        en = sum(1 for r in righe if r[1] > vero)
        print(f'  {nome:<22} restano {vero:2d}   {it:5d} ({100 * it // len(righe):2d}%)'
              f'   {en:5d} ({100 * en // len(righe):2d}%)')

    piu_lunghe = [r for r in righe if r[0] > r[1]]
    print(f'\nrese piu\' lunghe dell\'inglese: {len(piu_lunghe)} su {len(righe)} '
          f'({100 * len(piu_lunghe) // len(righe)}%), in media '
          f'{sum(r[0] - r[1] for r in piu_lunghe) / len(piu_lunghe):.1f} caratteri in piu\'')

    print('\nle dieci rese piu\' lunghe:')
    for n, m, riga, it in sorted(righe, reverse=True)[:10]:
        print(f'  {n:3d} (en {m:3d})  db_item.hsp:{riga}  {it[:60]}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
