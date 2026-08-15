import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # I tre rifiuti (:14842-:14852)
    # ================================================================
    # ⚠️ `is(tc)` e' morfologia e sparisce: resta il solo `name`.
    (14842, '  sleeping.'):
        'name(tc) + " sta dormendo."',
    # 💡 「気絶している」 e' uno STATO: proc.hsp:10303 usa «sviene» per 「気絶した」,
    #    che e' il momento in cui succede. E «ha perso i sensi» non concorda con
    #    niente, che serve perche' l'alleato puo' essere di qualunque genere.
    (14847, '  stunned.'):
        'name(tc) + " ha perso i sensi."',
    # ⚠️⚠️ `his(tc)` a UN argomento e' morfologia: le funzioni di contenuto
    #    dell'inglese sono zero, e la resa non puo' nominare nessuno benche' il
    #    giapponese abbia `name(tc)`. Voce tipata dinamica -> espressione
    #    (rete 12), come :7724 nel lotto 036.
    (14852, ' inventory is full.'):
        '"Non riesce a portare altro."',

    # ================================================================
    # Il regalo (:14860-:14865)
    # ================================================================
    # ⭐ La forma e' quella di :15250 («name(tc) + " riceve " + itemname...»),
    #    imposta dalla rete 8: `name()` non sta mai dopo una preposizione.
    # ⚠️ Giapponese suo — 「プレゼントした」, non 「渡した」 — quindi qui si distingue.
    (14860, 'You give  .'):
        'name(tc) + " riceve in regalo " + itemname(ci, 1) + "."',
    # 「え、これを俺にくれるの？ありがとう」
    (14863, 'Thank you!'):
        'Eh, questo è per me? Grazie!',
    (14865, 'Today is your anniversary with !'):
        '"Oggi è il tuo anniversario con " + name(tc) + "!"',

    # ================================================================
    # Il pegno d'amicizia (:14874-:14887)
    # ================================================================
    # ⭐ Stesso giapponese di :14980: la rete 4 pretende una resa sola, ed e'
    #    quella gia' decisa a :15250.
    (14874, 'You give  .'):
        'name(tc) + " riceve " + itemname(ci, 1) + "."',
    # 「こ、これが俺たちの友情の証！」 — impressione >= 100
    (14878, 'Thank you!'):
        "Q-questa è la prova della nostra amicizia!",
    # 「友情、ねぇ…」 — impressione bassa: tiepido anche in giapponese
    (14887, 'Hmm...'):
        'Amicizia, eh?...',

    # ================================================================
    # La gemma e il mazzo di fiori (:14897-:14993)
    # ================================================================
    (14897, 'How splendid!'):
        'Che meraviglia!',
    (14903, 'Poor taste...'):
        'Che pessimo gusto...',
    # ⭐ Stesso inglese di proc.hsp:1367, gia' reso «Che bellezza...», e il
    #    giapponese 「綺麗だな…」 dice la stessa cosa.
    (14911, 'Beautiful...'):
        'Che bellezza...',
    # ⭐ Stesso giapponese di :14874 (rete 4): resa identica.
    (14980, 'You give the  to .'):
        'name(tc) + " riceve " + itemname(ci, 1) + "."',
    # 「素敵だな！」 — impressione >= 150
    (14984, 'Thank you!'):
        'Che bello!',
    # 「う、うん…」 — un si' esitante
    (14993, 'Hmm...'):
        'U-uhm... sì...',
}
