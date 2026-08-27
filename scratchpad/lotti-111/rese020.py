import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :56740
    (56740, 'It is a ring created by the dragon.'):
        "Un anello fatto da un drago.",

    # ---------------------------------------------------------- :75584
    (75584, 'It is a godly gift that when worn, transforms into a ring.'):
        "Se lo indossi, si trasforma in un anello.",

    # ---------------------------------------------------------- :86674
    (86674, 'It is a rare magical ring that increases your speed.'):
        "Un anello che alza la velocità.",

    # ---------------------------------------------------------- :93630
    (93630, 'It is a ring that protects you from bad weather.'):
        "Un anello che non fa rallentare col brutto tempo.",

    # ---------------------------------------------------------- :99165
    (99165, "It is a ring given to raise affection, won't be returned."):
        "Dato a qualcuno, alza la simpatia. Non torna indietro.",

    # ---------------------------------------------------------- :99236
    (99236, 'It is a decoration to put on your finger.'):
        "Un cerchio da infilare al dito.",

    # ---------------------------------------------------------- :99308
    (99308, 'It is an armor plate that is processed to fit on the finger.'):
        "Un pezzo lavorato da infilare al dito.",

    # ---------------------------------------------------------- :99380
    (99380, 'It is a sturdy ring.'):
        "Un anello duro.",

    # ---------------------------------------------------------- :107184
    (107184, 'It is a ring that will bring you luck.'):
        "Un anello che alza la fortuna.",

    # ---------------------------------------------------------- :107393
    (107393, 'It is a ring with a very high protective value.'):
        "Un anello dal PV altissimo.",

    # ---------------------------------------------------------- :130388
    (130388, 'It is a pretty ring with a few embellishments.'):
        "Un anello con qualche decorazione.",

# 11 voci, 0 ambigue
}
