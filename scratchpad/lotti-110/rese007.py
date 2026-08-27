import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :48808
    (48808, 'It is a gem that would make a great gift.'):
        "Una gemma adatta a farne un regalo.",

    # ---------------------------------------------------------- :49711
    (49711, "It's a expensive but heavy statue."):
        "Una statua di valore, ma pesante.",

    # ---------------------------------------------------------- :52173
    (52173, 'These are artworks of the deep sea.'):
        "L'arte del mare profondo.",

    # ---------------------------------------------------------- :52316
    (52316, 'It is an ore that could be used as a material for armaments.'):
        "Un minerale che può servire come materiale per armi e armature.",

    # ---------------------------------------------------------- :66140
    (66140, 'It is an item used for artifact fusion.'):
        "Un oggetto per la sintesi.",

    # ---------------------------------------------------------- :69051
    (69051, 'It is a processed rubynus ore.'):
        "Del rubynus lavorato.",

    # ---------------------------------------------------------- :69121
    (69121, 'It is a processed emerald.'):
        "Una tavoletta fatta di smeraldo.",

    # ---------------------------------------------------------- :69191
    (69191, 'It is a processed diamond.'):
        "Un diamante lavorato.",

    # ---------------------------------------------------------- :82216
    (82216, 'It is a token for your friends, it deepens your relationship.'):
        "Stringe il legame con chi è più di un amico. Si può dare.",

    # ---------------------------------------------------------- :82613
    (82613, 'These are tickets given out to promising musicians. Some collect these.'):
        "Un foglio senza alcun effetto. Cerca qualcuno che li collezioni.",

    # ---------------------------------------------------------- :89422
    (89422, 'It is currency with high collection value, rarely found.'):
        "Dicono che da qualche parte ci sia chi le colleziona.",

    # ---------------------------------------------------------- :117321
    (117321, 'These are knockoffs.'):
        "Una riproduzione.",

    # ---------------------------------------------------------- :128176
    (128176, 'It is an insignificant pebble.'):
        "Un sassolino da niente.",

    # ---------------------------------------------------------- :128308
    (128308, 'It is an ore that contain traces of diamonds.'):
        "Un minerale che contiene tracce di diamante.",

    # ---------------------------------------------------------- :128378
    (128378, 'It is an ore that contain traces of emerald.'):
        "Un minerale che contiene tracce di smeraldo.",

    # ---------------------------------------------------------- :128448
    (128448, 'It is a white-colored ore.'):
        "Un minerale di colore bianco.",

    # ---------------------------------------------------------- :128518
    (128518, 'It is an ore that contain traces of rubynus.'):
        "Un minerale che contiene tracce di rubynus.",

    # ---------------------------------------------------------- :128588
    (128588, 'It is a golden, shining metal bar.'):
        "Un minerale che brilla d'oro.",

    # ---------------------------------------------------------- :128658
    (128658, 'It is a yellowish ore.'):
        "Un minerale di colore giallo.",

    # ---------------------------------------------------------- :128728
    (128728, 'It is a reddish ore.'):
        "Un minerale di colore rosso.",

    # ---------------------------------------------------------- :128798
    (128798, 'It is an orange-ish ore.'):
        "Un minerale di colore arancione.",

# 21 voci, 0 ambigue
}
