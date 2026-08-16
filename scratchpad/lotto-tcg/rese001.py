import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1167-:1173 la riga d'aiuto in fondo al tavolo, quando il cursore non
    #     e' su nessuna carta. `cardhelp` (:651), disegnata a :3497.
    (1167, 'End your main phase.'):
        'Chiudi la fase principale.',
    (1170, 'No blocker.'):
        'Non bloccare.',
    (1173, 'Choose Randomly.'):
        'Scegli a caso.',

    # --- :1495-:1610 la scheda della carta, composta in `rtvaln` da `card_ref`.
    # ⚠️ I due spazi davanti sono del sito e vanno tenuti: separano dal nome.
    (1495, '  No.'):
        '  N.',
    (1499, ' <Land>'):
        ' <Terreno>',
    (1503, ' <Spell>'):
        ' <Magia>',
    (1509, '  Rare:'):
        '  Rarità:',
    # ⚠️ Lo spazio in coda e' del sito: quel che segue si attacca qui.
    (1512, 'Data: '):
        'Dati: ',
    (1610, 'Effect: '):
        'Effetto: ',

    # --- :2181-:2273 i tre rifiuti e i due sacrifici, in mezzo al duello.
    (2181, 'You sacrifice the card.'):
        'Sacrifichi la carta.',
    (2184, 'The opponent sacrifices the card.'):
        "L'avversario sacrifica la carta.",
    # ⚠️ rete 13: lo stesso giapponese 「これ以上は場に出せない。」 per due inglesi.
    #    L'inglese distingue chi ha il campo pieno, il giapponese no: si segue
    #    l'inglese, che e' la lingua di monte della resa.
    (2238, 'Your field is full.'):
        'Il tuo campo è pieno.',
    (2264, "Your opponent's field is full."):
        "Il campo dell'avversario è pieno.",
    (2273, "You don't have enough mana."):
        'Non hai abbastanza mana.',

    # --- :2468-:2474 il menu di scelta del mazzo.
    # ⚠️ Il nome sta QUI e non in `:2470`: in italiano viene prima del colore.
    #    Vedi il docstring e la rinviata.
    (2468, 'White'):
        'Mazzo bianco',
    (2468, 'Blue'):
        'Mazzo blu',
    (2468, 'Silver'):
        'Mazzo argento',
    (2468, 'Red'):
        'Mazzo rosso',
    (2468, 'Black'):
        'Mazzo nero',
    # ⚠️ Lo spazio in testa e' del sito: si attacca al nome del mazzo.
    (2474, ' (New)'):
        ' (nuovo)',

    # --- :2497-:2498 il menu del mazzo scelto. Riquadro da 240px -> 25 caratteri.
    (2497, 'Edit Deck'):
        'Costruisci il mazzo',
    (2498, 'Set as Main Deck'):
        'Imposta come principale',

    # --- :2558-:2571 la finestra che esce col mazzo troppo piccolo.
    #     E' la prima schermata che vede chiunque provi il gioco.
    (2558, 'a Proper Deck'):
        'Un mazzo come si deve',
    # ⚠️ Lo spazio in coda e' del sito: `:2563` si attacca qui.
    (2560, 'I should make sure my deck has at least 30 cards before a duel. May be I should get more cards to put them in my deck. '):
        'Prima di un duello devo controllare che il mio mazzo abbia almeno 30 carte. Forse dovrei procurarmi altre carte da metterci dentro. ',
    # ⭐ 「また今度ね」 e' gia' reso a db_creature.hsp:46267.
    (2565, 'Maybe next time.'):
        'Sarà per la prossima volta.',
    (2571, 'a Proper Deck (Lethal)'):
        'Un mazzo come si deve (mortale)',
    (2605, 'Maybe next time.'):
        'Sarà per la prossima volta.',
    (2776, 'Maybe next time.'):
        'Sarà per la prossima volta.',
}
