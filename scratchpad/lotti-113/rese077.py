import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :109020
    (109020, 'A type of food that is loaded into carts. It has extremely high shelf life and the taste is not bad. However, this type of food is more about quantity than quality, and on a journey, the quantity of food packed often outweighs the taste. The set also includes a drink, so you can quench your thirst a little. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Un cibo del tipo che si carica sul carretto. Si conserva benissimo, e nemmeno il sapore è male. Ma roba così è quantità più che qualità: in viaggio, spesso è quanto ne hai stipato a contare più di com'è buono. Nella dotazione c'è anche da bere, così anche la sete si placa un poco. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

# 1 voci, 0 ambigue
}
