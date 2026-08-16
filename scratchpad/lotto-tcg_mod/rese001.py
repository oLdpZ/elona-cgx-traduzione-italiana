import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :3479-:3486 gli otto domini, in maiuscolo come l'inglese.
    (3479, 'BLUE'):
        'BLU',
    (3480, 'GREEN'):
        'VERDE',
    (3481, 'WHITE'):
        'BIANCO',
    (3482, 'BLACK'):
        'NERO',
    # ⭐ «NEUTRO» qualifica una carta, non una persona che si dichiara neutrale.
    (3483, 'NEUTRAL'):
        'NEUTRO',
    # ⭐ L'aggettivo, come l'inglese: sta accanto a sette colori.
    (3484, 'LEGENDARY'):
        'LEGGENDARIO',
    (3485, 'GRAY'):
        'GRIGIO',
    (3486, 'RED'):
        'ROSSO',
}
