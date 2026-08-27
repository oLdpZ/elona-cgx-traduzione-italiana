import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :61584
    (61584, "(Reusable) belt buckle that changes one's attribute of some skills."):
        "Cambia l'attributo di certe abilità. Si può usare sempre.",

    # ---------------------------------------------------------- :64279
    (64279, 'It is a broom that floats when you ride it.'):
        "Una scopa che ti fa levitare quando ci sali.",

    # ---------------------------------------------------------- :64346
    (64346, "It is not underwear, it's hot pants."):
        "Non sono mutande: sono pantaloni corti.",

    # ---------------------------------------------------------- :68115
    (68115, 'It is a belt studded with defensive magic.'):
        "Una cintura con una magia di difesa dentro.",

    # ---------------------------------------------------------- :76052
    (76052, 'It is a godly gift that when worn, transforms and becomes a waist belt.'):
        "Se lo indossi, si trasforma in una cintura.",

    # ---------------------------------------------------------- :82345
    (82345, 'It is a waistband that prevents bleeding and burning.'):
        "Una cintura che ferma il sanguinamento e le fiamme.",

    # ---------------------------------------------------------- :100330
    (100330, 'It is a reinforced girdle.'):
        "Una cintura fatta di più pezzi in fila.",

    # ---------------------------------------------------------- :100395
    (100395, 'It is a girdle reinforced with composite materials.'):
        "Una cintura dura.",

    # ---------------------------------------------------------- :126715
    (126715, 'It is armor for your waists.'):
        "Un'armatura per proteggere i fianchi.",

# 9 voci, 0 ambigue
}
