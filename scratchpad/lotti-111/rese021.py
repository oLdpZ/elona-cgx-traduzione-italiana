import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :59065
    (59065, 'These are wings that automatically assault the enemy.'):
        "Delle ali che caricano il nemico da sole.",

    # ---------------------------------------------------------- :63655
    (63655, 'It is a pair of mechanical side arms.'):
        "Delle braccia in più, meccaniche.",

    # ---------------------------------------------------------- :76590
    (76590, 'It is a pair of mechanical wings.'):
        "Delle ali meccaniche.",

    # ---------------------------------------------------------- :77357
    (77357, 'It is a cloak used, shabby, and worn out.'):
        "Un mantello portato fino a ridurlo sciatto.",

    # ---------------------------------------------------------- :93695
    (93695, 'It is a cloak that protects against the etherwind.'):
        "Un mantello che protegge dal vento di etere.",

    # ---------------------------------------------------------- :94025
    (94025, 'It is a feather ornament to be worn on the back.'):
        "Un ornamento di piume da mettere sulla schiena.",

    # ---------------------------------------------------------- :100200
    (100200, 'It is a heavy cloak designed for travel.'):
        "Un'armatura da buttarsi sulle spalle.",

    # ---------------------------------------------------------- :100265
    (100265, 'It is a reinforced cloak designed for protection.'):
        "Un mantello lavorato per il combattimento.",

    # ---------------------------------------------------------- :126780
    (126780, 'It is a light mantle.'):
        "Un mantello leggero.",

# 9 voci, 0 ambigue
}
