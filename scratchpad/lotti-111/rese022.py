import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :62804
    (62804, 'It is an armguard that allow combo-attacks like a meteor shower.'):
        "Un bracciale che dà raffiche di colpi come uno sciame di meteore.",

    # ---------------------------------------------------------- :75650
    (75650, 'It is a godly gift that when worn, transforms and becomes gauntlets.'):
        "Se lo indossi, si trasforma in un bracciale.",

    # ---------------------------------------------------------- :75717
    (75717, "These are gloves that is called a 'zekki'."):
        "Dei guanti d'arme detti zekki.",

    # ---------------------------------------------------------- :101117
    (101117, 'It is a pair of gauntlets reinforced with composite mesh.'):
        "Dei guanti d'arme duri.",

    # ---------------------------------------------------------- :101183
    (101183, 'It is a pair of gloves with a soft inner lining.'):
        "Dei guanti sottili.",

    # ---------------------------------------------------------- :101250
    (101250, 'It is a pair of very heavy plated gauntlets.'):
        "Dei guanti d'arme pesantissimi.",

    # ---------------------------------------------------------- :101317
    (101317, 'These are pieces of armor that fits on your palm.'):
        "Un'armatura che calza sul palmo.",

    # ---------------------------------------------------------- :107530
    (107530, 'These are gloves with excellent penetrating ability.'):
        "Dei guanti d'arme bravi a perforare.",

    # ---------------------------------------------------------- :130585
    (130585, 'It is a pair of very heavy gauntlet.'):
        "Dei guanti d'arme spessi.",

    # ---------------------------------------------------------- :130652
    (130652, 'These are ornated gloves often worn by nobility.'):
        "Dei guanti d'arme con degli ornamenti.",

# 10 voci, 0 ambigue
}
