import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :127545
    (127545, 'Currency widely circulated in the world. It has recently been established as an alternative to barter, but the downside is that it tends to concentrate wealth in one place, making it vulnerable to thieves, especially when traveling, and the wealthy are demanding that the government issue more valuable currency. \\n# ~Coins of this World - Tyris Edition~'):
        "La moneta che circola dappertutto nel mondo. Di recente si è imposta al posto del baratto, ma ha il difetto di far ammassare le ricchezze in un punto solo: così in viaggio si finisce facilmente nel mirino dei ladri, e i ricchi chiedono allo Stato di battere una moneta di valore ancora maggiore. \\n# ~Le Monete del Mondo: Tyris~",

# 1 voci, 0 ambigue
}
