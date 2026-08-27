# -*- coding: utf-8 -*-
"""Le rese del lotto 008 (i LIBRI, `FILTER_ITEM_BOOK`), indicizzate per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 008 scratchpad/lotti-110

**23 righe del sorgente, 20 firme.**

La categoria ha **una coda sola**, e il giapponese la scrive in due gradi che
il dizionario ha gia' resi (108a, i dieci atti dei mezzi):

    何度でも読むことができる -> Si può rileggere sempre.
    読むことができる         -> Si può leggere.

e **una famiglia**: sette libri che fanno di qualcuno un compagno.

⚠️ `:129513`, il libro bacato: `description(3)` giapponese e' **vuota** e
l'inglese e' una nota per chi programma — «generated when failed to create an
item». Non e' testo morto (il rapporto compare se il giocatore identifica
l'oggetto): si rende quel che c'e'.
"""

IT = {
    # --- i sette libri che fanno un compagno
    56058: "Un libro che fa del maggiordomo un compagno. Si legge.",
    76794: "Un libro che fa della sorella cane maggiore un compagno. Si legge.",
    76938: "Un libro che fa della sorella maggiore un compagno. Si legge.",
    89287: "Un libro che fa della signorina un compagno. Si legge.",
    89359: "Un libro che fa della sorella gatta minore un compagno. Si legge.",
    97203: "Un libro che fa della sorella minore un compagno. Si legge.",
    81067: "Un libro che fa di qualcosa un compagno. Si legge.",

    # --- i due che dicono quel che NON fanno
    62537: "Si può rileggere sempre. Il ricercatore non diventa un compagno.",
    74104: "Si può rileggere sempre. Il folle non diventa un compagno.",

    # --- le raccolte di notizie
    50819: "Un libro con notizie di ogni genere. Si può rileggere sempre.",
    51224: "Un taccuino con notizie di ogni genere. Si può rileggere sempre.",
    56204: "Un rapporto con notizie astruse. Si può rileggere sempre.",
    86406: "Un libro scritto da un autore di fiabe. Si può rileggere sempre.",

    # --- il resto
    47223: "Un libro per usare la magia dell'Abisso. Si può rileggere sempre.",
    57580: "Un album di foto della dea del vento. A terra, distrae.",
    71103: "Si può leggere. Di chi sia il diario non si sa.",
    83700: "Un libro che riporta in vita i morti. Si può leggere.",
    84236: "Un libro che dice come va in città. Si può leggere.",
    93295: "Un libro che alza il potenziale di un'abilità scelta. Si legge.",
    129513: "Compare quando la creazione di un oggetto fallisce.",
}
