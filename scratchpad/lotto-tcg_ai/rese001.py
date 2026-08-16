import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ⭐ Il ramo mette `gameresult@tcg = -2`, che il gioco chiama «Fuggito!»
    #    (tcg.hsp:2779): non e' la resa, che e' -1 e sta su un altro tasto.
    (308, 'Escape?'):
        'Scappi?',
    # ⚠️ Invariato dichiarato: la parola e' identica nelle due lingue.
    (309, 'No'):
        'No',
}
