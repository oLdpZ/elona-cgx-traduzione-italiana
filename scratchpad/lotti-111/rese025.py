import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :44866
    (44866, 'It is seaweed.'):
        "Un'alga. Si può mangiare.",

    # ---------------------------------------------------------- :44929
    (44929, 'It is seaweed.'):
        "Un'alga gigantesca. Si può mangiare.",

    # ---------------------------------------------------------- :44992
    (44992, 'It is seaweed.'):
        "Un'alga grande. Si può mangiare.",

    # ---------------------------------------------------------- :65950
    (65950, 'These are ammos to be equipped with guns (pistols only).'):
        "Un'arma da equipaggiare insieme a una pistola (solo pistole).",

    # ---------------------------------------------------------- :87577
    (87577, '(Re-drinkable) facility that supplies water.'):
        "Un impianto che usa l'acqua. Si può bere più volte.",

    # ---------------------------------------------------------- :90710
    (90710, '(Drinkable) well that contains holy water.'):
        "Un pozzo pieno d'acqua santa. Si può bere.",

    # ---------------------------------------------------------- :96637
    (96637, 'It is a weapon to be equipped together with a gun.'):
        "Un'arma da equipaggiare insieme a un'arma da fuoco.",

    # ---------------------------------------------------------- :97266
    (97266, 'It is a card with information about creature. You can put them in decks.'):
        "Un foglio con i dati di una creatura. Si mette nel mazzo.",

    # ---------------------------------------------------------- :97328
    (97328, 'These are statues in the shape of monsters.'):
        "Una statua che riproduce un mostro.",

    # ---------------------------------------------------------- :98728
    (98728, 'It is a weapon to be equipped together with a crossbow.'):
        "Un'arma da equipaggiare insieme a una balestra.",

    # ---------------------------------------------------------- :108522
    (108522, 'It is the bone of a creature.'):
        "L'osso di una creatura.",

    # ---------------------------------------------------------- :108584
    (108584, 'It is the heart of a creature.'):
        "Il cuore di una creatura.",

    # ---------------------------------------------------------- :108646
    (108646, 'It is the eye of a creature.'):
        "L'occhio di una creatura.",

    # ---------------------------------------------------------- :108708
    (108708, 'It is the blood of a creature.'):
        "Il sangue di una creatura.",

    # ---------------------------------------------------------- :108770
    (108770, 'It is the skin of a creature.'):
        "La pelle di una creatura.",

    # ---------------------------------------------------------- :109023
    (109023, 'It is a cargo of travel rations often used by merchants.'):
        "Un cibo del tipo che si carica sul carretto.",

    # ---------------------------------------------------------- :119822
    (119822, "It is an altar for ritual's to give tribute to the gods."):
        "Un altare semplice. Ci si possono fare offerte.",

    # ---------------------------------------------------------- :119884
    (119884, "It is a podium for ritual's to give tribute to the gods."):
        "Un piedistallo in lode del dio. Ci si possono fare offerte.",

    # ---------------------------------------------------------- :123939
    (123939, '(Re-drinkable) facility that supplies water.'):
        "Un impianto che raccoglie l'acqua. Si può bere.",

    # ---------------------------------------------------------- :127065
    (127065, 'It is a weapon to be equipped together with a bow.'):
        "Un'arma da equipaggiare insieme a un arco.",

    # ---------------------------------------------------------- :127486
    (127486, 'These are rare coins used by the guilds as currency.'):
        "Una moneta speciale e lucente. Serve a pagare l'istruttore.",

    # ---------------------------------------------------------- :127548
    (127548, 'It is the standard currency of Irva.'):
        "La moneta corrente in tutto il mondo.",

    # ---------------------------------------------------------- :131247
    (131247, 'not used in the game'):
        "Non è usato nel gioco.",

# 1131 voci, 0 ambigue
}
