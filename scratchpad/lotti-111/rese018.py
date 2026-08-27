import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :62466
    (62466, 'It is a sphere that strengthen the spiritual aspect of the body.'):
        "Una sfera che rinforza lo spirito.",

    # ---------------------------------------------------------- :76250
    (76250, 'It is a godly gift that when worn, transforms into a collar.'):
        "Se lo indossi, si trasforma in un collare.",

    # ---------------------------------------------------------- :81539
    (81539, "It is a necklace that allows you to hear God's whisper."):
        "Una collana che fa sentire la parola divina.",

    # ---------------------------------------------------------- :82679
    (82679, 'It is a necklace that provides a chance for extra strikes.'):
        "Una collana che dà la probabilità di un attacco extra in mischia.",

    # ---------------------------------------------------------- :82745
    (82745, 'It is a necklace that gives a chance for an additional shot.'):
        "Una collana che dà la probabilità di un attacco extra a distanza.",

    # ---------------------------------------------------------- :83904
    (83904, 'It is a necklace that protects you from unfortunate events.'):
        "Una collana che protegge dalle disgrazie.",

    # ---------------------------------------------------------- :99451
    (99451, "It is an amulet that show's one's love, cannot be returned."):
        "Data a qualcuno, alza la simpatia. Non torna indietro.",

    # ---------------------------------------------------------- :99522
    (99522, 'It is a polished, jeweled amulet.'):
        "Una collana ben lucidata.",

    # ---------------------------------------------------------- :99594
    (99594, 'It is a charm that ward off evil.'):
        "Una collana in cui è racchiuso un sentimento.",

    # ---------------------------------------------------------- :99666
    (99666, 'It is an armor plate that is processed to fit on the neck.'):
        "Una collana per proteggersi.",

    # ---------------------------------------------------------- :99738
    (99738, 'It is a talisman infused with mana.'):
        "Una collana in cui è racchiuso il potere magico.",

    # ---------------------------------------------------------- :99810
    (99810, 'It is a green gem attached to a neck chain.'):
        "Una collana con una gemma.",

    # ---------------------------------------------------------- :126650
    (126650, 'It is an ornate amulet.'):
        "Una collana con delle decorazioni.",

# 13 voci, 0 ambigue
}
