import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :43047
    (43047, "(Reusable) side-tail wig that changes it's appearance."):
        "Una parrucca che cambia aspetto. Si può usare sempre.",

    # ---------------------------------------------------------- :43115
    (43115, "(Reusable) wig that changes it's appearance."):
        "Una parrucca che cambia aspetto. Si può usare sempre.",

    # ---------------------------------------------------------- :65401
    (65401, 'It is a helmet-shaped machine.'):
        "Una macchina a forma di casco.",

    # ---------------------------------------------------------- :66980
    (66980, "It is a helmet made from an alien's head."):
        "Un elmo ricavato dalla testa di un extraterrestre.",

    # ---------------------------------------------------------- :72421
    (72421, 'It is a hat that amplifies the magic.'):
        "Un cappello che amplifica la magia.",

    # ---------------------------------------------------------- :76184
    (76184, 'It is a godly gift that when worn, transforms into a circlet.'):
        "Se lo indossi, si trasforma in un cerchietto da testa.",

    # ---------------------------------------------------------- :80427
    (80427, 'It is a helmet with offensive capabilities.'):
        "Un elmo con doti offensive.",

    # ---------------------------------------------------------- :89080
    (89080, 'It is a helmet that can see the invisible.'):
        "Un elmo che fa vedere chi non si vede.",

    # ---------------------------------------------------------- :99875
    (99875, 'It is a very sturdy helm.'):
        "Un elmo duro.",

    # ---------------------------------------------------------- :99940
    (99940, 'It is a standard helm.'):
        "Un'armatura per proteggere la testa.",

    # ---------------------------------------------------------- :100005
    (100005, 'It is a helm made for knights.'):
        "Un elmo per i cavalieri.",

    # ---------------------------------------------------------- :100070
    (100070, 'It is a heavy helm designed for good protection.'):
        "Un elmo di un certo peso.",

    # ---------------------------------------------------------- :100135
    (100135, 'It is a hat with a feather often worn by bards.'):
        "Un cappello con una piuma.",

    # ---------------------------------------------------------- :130847
    (130847, 'It is an exotic hat designed for faeries.'):
        "Un cappello per le fate.",

    # ---------------------------------------------------------- :130912
    (130912, 'It is a hat mages often wear.'):
        "Un cappello per i maghi.",

# 15 voci, 0 ambigue
}
