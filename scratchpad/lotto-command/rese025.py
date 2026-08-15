import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :15309-:15312 l'oggetto che sta in due spazi. I nomi degli spazi sono
    #     quelli di text.hsp:136 — «Tiro» e «Mano» — e vanno maiuscoli perché
    #     sono le etichette che il giocatore ha davanti.
    (15309, 'Although this is a ranged equipment it can be equipped in your hands. Which will you choose?'):
        'È equipaggiamento da Tiro, ma si può portare anche in Mano. Quale scegli?',
    (15312, 'Although this is a short distance equipment it can be equipped as ranged. Which will you choose?'):
        'È equipaggiamento da Mano, ma si può portare anche nel Tiro. Quale scegli?',
    # 「何番目の手？」: le creature con più di due mani
    (15332, 'Which hand?'): 'Quale mano?',

    # --- :15364 l'alleato che non prende l'oggetto.
    #     `_s(tc)` è morfologia inglese e sparisce; restano name e itemname.
    (15364, ' refuse to take .'):
        'name(tc) + " non accetta " + itemname(ci, 1) + "."',

    # --- :15372-:15379 l'identificazione.
    (15372, 'You need higher identification to gain new knowledge.'):
        "Non hai scoperto niente di nuovo: serve un'identificazione superiore.",
    # ⚠️ «identificato» accorderebbe col genere dell'oggetto: il nome astratto
    #    toglie l'accordo di mezzo, ed è la stessa manovra del lotto 024.
    (15376, 'The item is half-identified as .'):
        '"È " + itemname(ci, 1) + ": identificazione incompleta."',
    (15379, 'The item is fully identified as .'):
        '"È " + itemname(ci, 1) + ": identificazione completa."',

    # --- :15444 lo scambio. Due itemname, e la rete 11 guarda l'insieme.
    (15444, 'You receive  in exchange for .'):
        '"Hai scambiato " + itemname(ci) + " con " + itemname(citrade) + "."',

    # --- :15489 è RINVIATA: fuori dalla lang() il sorgente attacca
    #     « Guild Point)», che il dizionario non raggiunge. La riga la riscrive
    #     tutta la toppa. Vedi il docstring e scratchpad/toppa-command-15489.py.

    # ⭐ «quota» è l'incarico della gilda, e il progetto lo chiama «obiettivo»
    #    da chara_func.hsp:7247, proc.hsp:241 e command.hsp:13895.
    (15493, 'You fulfill the quota!'): 'Obiettivo raggiunto!',

    # --- :15499 la consegna della missione di raccolta, con la riga di stato.
    (15499, 'You deliver .'):
        '"Hai consegnato " + itemname(ci) + "."',
    # gli spazi sono quel che stacca l'etichetta dai due conti fra parentesi
    (15499, ' Delivered '): ' Consegnato ',
    (15499, 'Quota '): 'Obiettivo ',
}
