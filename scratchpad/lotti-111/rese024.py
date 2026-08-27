import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :76118
    (76118, 'It is a godly gift that when worn, transforms and become shackles.'):
        "Se lo indossi, si trasforma in ceppi.",

    # ---------------------------------------------------------- :86870
    (86870, 'These are shoes that speed up the journey.'):
        "Delle scarpe che fanno viaggiare più svelti.",

    # ---------------------------------------------------------- :93760
    (93760, 'These are boots magically enhanced to allow faster travel.'):
        "Delle scarpe che fanno viaggiare molto più svelti.",

    # ---------------------------------------------------------- :100459
    (100459, "It is a pair of boot's with armored plating."):
        "Delle scarpe fatte a corazza.",

    # ---------------------------------------------------------- :100524
    (100524, 'It is a tight fitting pair of boots.'):
        "Delle scarpe spesse.",

    # ---------------------------------------------------------- :100589
    (100589, 'It is a standard pair of boots.'):
        "Un'armatura per proteggere la punta dei piedi.",

    # ---------------------------------------------------------- :100654
    (100654, 'These are simple protective gear that protects the feet from the ground.'):
        "Un'armatura semplice, per proteggere i piedi da terra.",

    # ---------------------------------------------------------- :130453
    (130453, 'It is a pair of boots reinforced with composite mesh.'):
        "Delle scarpe dure.",

    # ---------------------------------------------------------- :130518
    (130518, 'It is a pair of extra sturdy boots.'):
        "Delle scarpe pesanti.",

# 9 voci, 0 ambigue
}
