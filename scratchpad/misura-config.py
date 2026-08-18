# -*- coding: utf-8 -*-
"""I due tetti del pannello delle opzioni, misurati sul dizionario di `config.hsp`.

Il pannello non passa da nessuna delle reti di geometria: `larghezze.py` guarda
i menu di `*prompt_key`, `riquadri.py` le piastrelle dell'HUD, `menu_dialogo.py`
le voci di `chatList`, `linguette.py` le schede in cima alle finestre grandi.
`config.hsp` disegna da se', con `cs_list` e `mes`, e nessuno lo misurava.

## Da dove vengono i numeri

Il passo del carattere lo dichiara il disegnatore (`module.hsp:72`):

    locvar_cs_list_tx = limit(strlen(cs_list_arg1) * 7 + 32 + cs_list_arg5, 10, 480)

**7 px**, e regge: il carattere inglese e' `Courier New` (`config.txt`,
`font2.`), monospaziato, chiesto a corpo `14 - en * 2` = 12 (`config.hsp:716`).
Il passo del Courier e' 0,6 em, cioe' 7,2 px a corpo 12.

I confini stanno nel disegnatore del pannello (`config.hsp:738`-`:747`):

    cs_list s, wx + 56 + x, ...   l'etichetta comincia a wx + 60 (cs_list aggiunge 4)
    pos wx + 220 : gcopy ...      la freccia sinistra
    pos wx + 250 : mes s(...)     il valore
    pos wx + 358 : gcopy ...      la freccia destra

    etichetta   (220 - 60) / 7 = 22
    valore      (358 - 250) / 7 = 15

⚠️ `mes` non taglia e non manda a capo: quel che sfora si stampa **sopra** la
freccia e poi sopra il valore.

⚠️ Le voci dell'elenco delle sezioni (`:580`, `:581`) hanno un riquadro proprio
(`dx = 370`, `:583`) e nessuna freccia: si misurano contro il bordo, non contro
i 22. La linguetta del titolo cresce da sola (`module.hsp:4328`).

⚠️ La nota in fondo (`:1038`, `:1046`) ha un carattere piu' piccolo
(`12 + sizefix - en * 2` = 11 con `fontSfix1. "1"`) e parte da `wx + 40`:
(440 - 40 - 20) / 7 = 54 caratteri per riga.

## ⚠️ Si misura la resa DEGRADATA

`applica.py` scrive `perche'` dove il dizionario dice `perché`: un accento vero
diventa **due** caratteri. Misurare la resa come sta nel dizionario darebbe un
carattere in meno per ogni accento.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from strumenti import accenti

PIXEL_PER_CARATTERE = 7

INIZIO_ETICHETTA = 60      # wx + 56 + 4, con submenu != 0 (x = 0)
FRECCIA_SINISTRA = 220
INIZIO_VALORE = 250
FRECCIA_DESTRA = 358

TETTO_ETICHETTA = (FRECCIA_SINISTRA - INIZIO_ETICHETTA) // PIXEL_PER_CARATTERE
TETTO_VALORE = (FRECCIA_DESTRA - INIZIO_VALORE) // PIXEL_PER_CARATTERE
TETTO_NOTA = (440 - 40 - 20) // PIXEL_PER_CARATTERE

# Le righe dell'elenco delle sezioni e l'intestazione: riquadro da 370, nessuna
# freccia, e il titolo si allarga da solo.
FUORI_COLONNA = {580, 581, 587, 592, 598, 604, 610, 617, 622, 628, 635, 681}
# Le due note in fondo al pannello.
NOTE = {1038, 1046}


def _degradata(it: str) -> str:
    return accenti.degrada(it)


def misura(percorsi):
    fuori = []
    contate = collassate = 0
    for percorso in percorsi:
        for riga in io.open(percorso, encoding='utf-8'):
            if not riga.strip():
                continue
            d = json.loads(riga)
            it = d.get('it') or ''
            if not it:
                continue
            # una resa che e' un'espressione HSP non si misura da qui
            if d.get('tipo') == 'dinamica':
                collassate += 1
                continue
            n = d['riga']
            if n in FUORI_COLONNA:
                continue
            testo = _degradata(it)
            if n in NOTE:
                tetto = TETTO_NOTA
                lunghezza = max(len(p) for p in testo.split('\\n'))
                dove = 'nota'
            elif n <= 700:
                tetto = TETTO_ETICHETTA
                lunghezza = len(testo)
                dove = 'etichetta'
            else:
                tetto = TETTO_VALORE
                lunghezza = len(testo)
                dove = 'valore'
            contate += 1
            if lunghezza > tetto:
                fuori.append((n, dove, lunghezza, tetto, it, d.get('en', '')))
    return fuori, contate, collassate


def main(argv):
    percorsi = argv or ['dizionario/config.hsp.jsonl']
    percorsi = [p for p in percorsi if os.path.exists(p)]
    if not percorsi:
        sys.exit('nessun file da misurare')
    fuori, contate, collassate = misura(percorsi)
    for n, dove, lunghezza, tetto, it, en in sorted(fuori):
        print(f'⚠️ :{n} {dove} {lunghezza}/{tetto}  {it!r}   (l\'inglese: {en!r} = {len(en)})')
    print(f'\nvoci misurate: {contate} '
          f'(tetti: etichetta {TETTO_ETICHETTA}, valore {TETTO_VALORE}, nota {TETTO_NOTA})')
    print(f'dinamiche non misurabili da qui: {collassate}')
    print(f'fuori misura: {len(fuori)}')


if __name__ == '__main__':
    main(sys.argv[1:])
