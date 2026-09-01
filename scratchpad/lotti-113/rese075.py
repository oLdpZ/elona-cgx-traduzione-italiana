import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :127483
    (127483, "A platinum coin used for special occasions. It cannot be used as money and vice versa. Its main use is when expressing one's gratitude instead, etc. This usage is widely recognized and a considerable number of coins are in circulation. \\n# ~Coins of this World - Tyris Edition~"):
        "Una moneta di platino che si adopera in occasioni particolari. Come denaro non si può spendere, e il denaro non la sostituisce. Serve soprattutto a esprimere la propria gratitudine al posto delle parole; è un uso che tutti conoscono, e ne circolano parecchie. \\n# ~Le Monete del Mondo: Tyris~",

# 1 voci, 0 ambigue
}
