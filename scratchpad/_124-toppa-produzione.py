# -*- coding: utf-8 -*-
"""124a - La toppa che allarga le colonne dei materiali richiesti.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_124-toppa-produzione.py

⚠️⚠️⚠️ **PERCHE'.** `_124-larghezze-produzione.py` ha misurato la colonna piu'
stretta di tutto il progetto: `material.hsp:288` incolonna i materiali che una
ricetta chiede in **tre** colonne con passo **192 px**, e la riga si disegna a
font 11 (`:252`), cioe' **27 caratteri**. Dentro ci sta
`nome + " x " + quanti + "(" + posseduti + ")"`, e in italiano 27 combinazioni
su 113 sforano — «macchina generatrice x 2(99999)» ne fa 31.

⭐ **L'inglese ci sta e questo dice che il modello non e' sbagliato**: il suo
nome di materiale piu' lungo e' 17 caratteri («Sap of Yaggdrasil»,
«Discharging stone») contro i 20 italiani, e sfora solo a cinque cifre di
contatore, dove sono 28 su 27.

⚠️ **La via che NON si prende e' accorciare i tredici nomi.** Sono decisi in
`glossario.md`, ventisette di loro dalla 42a per un altro file, e sono gia'
tarati sul budget dell'ALTRO pannello (`nome + " x N"` in 212 px a font 12,
123a). Accorciarli per questa colonna li romperebbe la' — e sarebbe un modello
a decidere, non uno schermo.

💡 **Si allarga la colonna, che e' l'unica cosa che non toglie niente a
nessuno**: due colonne da 288 px invece di tre da 192, cioe' 41 caratteri, e i
sei materiali entrano lo stesso su tre righe invece di due. C'e' posto in
verticale: le righe cadono a wy+334, +350 e +366, e la riga del suggerimento
che chiude la finestra sta a wy+401 (`module.hsp:4331`, `arg4 - 47`).

⚠️ La toppa e' in **ASCII, commenti compresi**: un commento non si vede in
gioco ma passa dallo stesso codificatore CP932 del codice (123a).
"""
import io
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
TOPPE = os.path.join(RADICE, 'toppe.jsonl')

CERCA = '\t\t\t\tpos wx + 37 + cnt \\ 3 * 192, wy + 334 + cnt / 3 * 16'
SOSTITUISCI = [
    '\t\t\t\t; TOPPA IT: due colonne da 288 px invece di tre da 192.',
    '\t\t\t\t; A font 11 (riga :252) il passo da 192 px vale 27 caratteri, e',
    '\t\t\t\t; "macchina generatrice x 2(99999)" ne fa 31: 27 combinazioni su',
    '\t\t\t\t; 113 sbordavano nella colonna accanto. L\'inglese ci sta perche',
    '\t\t\t\t; il suo nome piu lungo e 17 contro i 20 italiani.',
    '\t\t\t\t; I sei materiali entrano lo stesso: 2 colonne x 3 righe, a',
    '\t\t\t\t; wy+334, +350 e +366, e il suggerimento sta a wy+401.',
    '\t\t\t\tpos wx + 37 + cnt \\ 2 * 288, wy + 334 + cnt / 2 * 16',
]
MOTIVO = (
    "material.hsp:288. Le tre colonne dei materiali richiesti hanno passo 192 "
    "px e la riga si disegna a font 11 (:252), cioe' 27 caratteri: in italiano "
    "27 combinazioni su 113 sforano, la peggiore a 31 "
    "(\"macchina generatrice x 2(99999)\"). L'inglese ci sta perche' il suo "
    "nome piu' lungo e' 17 contro i 20 italiani, e sfora solo a cinque cifre "
    "di contatore. Non si accorciano i nomi: sono decisi in glossario.md e "
    "gia' tarati sul budget dell'ALTRO pannello (nome + \" x N\" in 212 px a "
    "font 12, 123a), dove accorciarli romperebbe la resa. Si allarga la "
    "colonna: due da 288 px invece di tre da 192, cioe' 41 caratteri. I sei "
    "materiali entrano lo stesso, su tre righe invece di due, a wy+334, +350 e "
    "+366; la riga del suggerimento che chiude la finestra sta a wy+401 "
    "(module.hsp:4331, arg4 - 47). Sito fuori da lang(): il dizionario non lo "
    "raggiunge, ed e' un'ancora senza stringhe traducibili, quindi nessun "
    "lotto potra' sganciarla (lezione della 96a)."
)


def main():
    toppa = {
        'file': 'material.hsp',
        'motivo': MOTIVO,
        'cerca': [CERCA],
        'sostituisci': SOSTITUISCI,
    }
    testo = json.dumps(toppa, ensure_ascii=False)
    assert all(ord(c) < 128 for c in ''.join(SOSTITUISCI)), 'la toppa non e\' ASCII'
    with io.open(TOPPE, 'a', encoding='utf-8', newline='\n') as f:
        f.write(testo + '\n')
    print('toppa aggiunta a %s' % TOPPE)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
