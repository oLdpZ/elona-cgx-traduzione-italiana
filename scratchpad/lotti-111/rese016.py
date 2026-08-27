import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :56270
    (56270, 'It is a cargo of painting.'):
        "Merce da commercio.",

    # ---------------------------------------------------------- :56336
    (56336, 'It is a cargo of rabbit foot.'):
        "Merce da commercio.",

    # ---------------------------------------------------------- :73897
    (73897, 'It is a cargo of marimo.'):
        "Merce da commercio.",

    # ---------------------------------------------------------- :73963
    (73963, 'It is a cargo of ration.'):
        "Merce da commercio.",

    # ---------------------------------------------------------- :86269
    (86269, 'It is a cargo of canvas.'):
        "Merce da commercio.",

    # ---------------------------------------------------------- :86335
    (86335, 'It is a cargo of art supplies.'):
        "Merce da commercio.",

    # ---------------------------------------------------------- :90963
    (90963, 'It is a cargo of snow men.'):
        "Merce da commercio.",

    # ---------------------------------------------------------- :91029
    (91029, 'It is a heavy cargo of pine trees.'):
        "Merce da commercio pesante.",

    # ---------------------------------------------------------- :103718
    (103718, 'It is a cargo of lifebuoy rings.'):
        "Merce da commercio.",

    # ---------------------------------------------------------- :103784
    (103784, "It is a cargo of high value children's toys."):
        "Merce da commercio.",

    # ---------------------------------------------------------- :103850
    (103850, 'It is a cargo of alchohol.'):
        "Merce da commercio.",

    # ---------------------------------------------------------- :103916
    (103916, 'It is a cargo of seafood.'):
        "Merce da commercio.",

    # ---------------------------------------------------------- :103982
    (103982, 'It is a very heavy cargo of grave slabs.'):
        "Merce da commercio molto pesante.",

    # ---------------------------------------------------------- :104114
    (104114, 'It is a cargo of coffins.'):
        "Merce da commercio.",

    # ---------------------------------------------------------- :104180
    (104180, 'It is a cargo of rope.'):
        "Merce da commercio.",

    # ---------------------------------------------------------- :104246
    (104246, 'It is a cargo of pianos.'):
        "Merce da commercio pesante.",

    # ---------------------------------------------------------- :104312
    (104312, 'It is a cargo of barrels.'):
        "Merce da commercio.",

    # ---------------------------------------------------------- :104378
    (104378, "It is a cargo of children's toys."):
        "Merce da commercio.",

# 18 voci, 0 ambigue
}
