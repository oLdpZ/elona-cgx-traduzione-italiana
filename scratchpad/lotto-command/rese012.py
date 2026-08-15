import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1796-:1840 i dodici elementi. ⭐ i nomi vengono da action.hsp:6918-:7044,
    #     le ventiquattro righe di «Add X Resistance» / «Add X Damage».
    (1796, 'Physical damage'):
        'Attacchi fisici',
    (1800, 'Fire damage'):
        'Attacchi di fuoco',
    (1804, 'Cold damage'):
        'Attacchi di gelo',
    (1808, 'Lightning damage'):
        'Attacchi di fulmine',
    (1812, 'Darkness damage'):
        'Attacchi di oscurità',
    (1816, 'Mind damage'):
        'Attacchi mentali',
    (1820, 'Poison damage'):
        'Attacchi di veleno',
    (1824, 'Nether damage'):
        "Attacchi dell'oltretomba",
    (1828, 'Sound damage'):
        'Attacchi di suono',
    (1832, 'Nerve damage'):
        'Attacchi ai nervi',
    (1836, 'Chaos damage'):
        'Attacchi caotici',
    (1840, 'Magic damage'):
        'Attacchi di magia',

    # --- :1844-:1864 i sei stati che subisce.
    (1844, 'Confuse status'):
        'Confusione',
    (1848, 'Blind status'):
        'Cecità',
    # ⭐ «Terrore» e «Sonno» sono le etichette di text.hsp:100 e :95
    (1852, 'Fear status'):
        'Terrore',
    (1856, 'Sleep status'):
        'Sonno',
    (1860, 'Paralyze status'):
        'Paralisi',
    (1864, 'Poison status'):
        'Avvelenamento',

    # --- :1884-:1900 le cinque cose fisiche.
    # ⭐ copiata: 「酸」 e' gia' «l'acido» a proc.hsp:22094
    (1884, 'Acid'):
        "l'acido",
    (1888, 'Bleeding'):
        'Sanguinamento',
    (1892, 'Trap'):
        'Trappole',
    (1896, 'Invisible enemy'):
        'Nemici invisibili',
    (1900, 'Parasite'):
        'Parassiti',

    # --- :1904-:1920 i cinque scherzi: paure legate a un CREATURE_ID preciso.
    #     ⭐ tutti e cinque i nomi vengono dal progetto, articolo compreso.
    (1904, 'Puff puff bread'):
        'pane soffice',
    (1908, 'Salt'):
        'sale',
    (1912, 'Yeek'):
        'lo yeek',
    (1916, 'Cat'):
        'il gatto',
    (1920, 'Shark'):
        'lo squalo',

    # --- :1928 il titolo della finestra.
    (1928, 'In the heart'):
        'Dentro il cuore',

    # --- :1985, :1999 le due intestazioni di *com_knowSelf.
    # ⚠️ il giapponese ha name(tc) e l'inglese no: la resa non puo' nominare
    #    nessuno, e il soggetto puo' essere un alleato invece del giocatore.
    # 💡 l'asterisco torna DENTRO <title1>, dove :1999 e il giapponese lo mettono
    (1985, '*<title1> Your bonuses and penalties.<def>\\n'):
        '<title1>*Effetti in corso<def>\\n',
    (1999, '<title1>*Effects of Blessings and Hexes<def>\\n'):
        '<title1>*Benedizioni e maledizioni<def>\\n',
}
