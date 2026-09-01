import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :119819
    (119819, "Simple altar with minimal facilities for offerings. It is said that by praying here, one can commune with the Gods. \\n#~ Worlds you've Never Seen~"):
        "Un altare spoglio, con giusto il minimo che serve per fare offerte. Dicono che pregando qui si entri in comunione col dio. \\n#~I Mondi che Non Hai Mai Visto~",

    # ---------------------------------------------------------- :119881
    (119881, "Huge structure made of stone that creates a solemn atmosphere. It is said that by praying here, one can commune with the Gods. \\n#~ Worlds you've Never Seen~"):
        "Una costruzione enorme fatta di pietra, che spande intorno un'aria solenne. Dicono che pregando qui si entri in comunione col dio. \\n#~I Mondi che Non Hai Mai Visto~",

# 2 voci, 0 ambigue
}
