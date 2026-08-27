import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :68453
    (68453, 'It is a cherry tree that its blossoms is forever falling.'):
        "Un ciliegio i cui fiori cadono per sempre.",

    # ---------------------------------------------------------- :90897
    (90897, 'It is a decorated fir tree.'):
        "Un abete addobbato.",

    # ---------------------------------------------------------- :91525
    (91525, 'It is evergreen with a scented wood.'):
        "Un sempreverde.",

    # ---------------------------------------------------------- :91587
    (91587, 'It is a leafless tree.'):
        "Un albero senza foglie.",

    # ---------------------------------------------------------- :95487
    (95487, 'It is a deciduous tree.'):
        "Un albero che perde le foglie.",

    # ---------------------------------------------------------- :95549
    (95549, 'It is a tropical tree.'):
        "Un albero dei paesi caldi.",

    # ---------------------------------------------------------- :95673
    (95673, 'It is a dead tree.'):
        "Un albero secco.",

    # ---------------------------------------------------------- :95737
    (95737, 'It is a fruit tree.'):
        "Un albero che lascia cadere i frutti.",

    # ---------------------------------------------------------- :95799
    (95799, 'It is a fruit tree with no fruits.'):
        "Un albero rimasto senza frutti.",

# 9 voci, 0 ambigue
}
