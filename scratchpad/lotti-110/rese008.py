import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :47223
    (47223, 'It is the book of collected knowledge of abyssal magic practices.'):
        "Un libro per usare la magia dell'Abisso. Si può rileggere sempre.",

    # ---------------------------------------------------------- :50819
    (50819, 'It is a book with miscellaneous information. Can be read more than once.'):
        "Un libro con notizie di ogni genere. Si può rileggere sempre.",

    # ---------------------------------------------------------- :51224
    (51224, 'It is a memo with miscellaneous information. Can be read more than once.'):
        "Un taccuino con notizie di ogni genere. Si può rileggere sempre.",

    # ---------------------------------------------------------- :56058
    (56058, '(Readable) diary of a butler, it befriends them when read.'):
        "Un libro che fa del maggiordomo un compagno. Si legge.",

    # ---------------------------------------------------------- :56204
    (56204, 'It is a report with misc. information. Can be read more than once.'):
        "Un rapporto con notizie astruse. Si può rileggere sempre.",

    # ---------------------------------------------------------- :57580
    (57580, 'It is a set of photograph of the Wind Goddess, very eye-catching.'):
        "Un album di foto della dea del vento. A terra, distrae.",

    # ---------------------------------------------------------- :62537
    (62537, "(Readable) report, it won't make you a real researcher."):
        "Si può rileggere sempre. Il ricercatore non diventa un compagno.",

    # ---------------------------------------------------------- :71103
    (71103, '(Readable) diary of unknown author, it befriends them when read.'):
        "Si può leggere. Di chi sia il diario non si sa.",

    # ---------------------------------------------------------- :74104
    (74104, "(Readable) diary, won't make you a real madman."):
        "Si può rileggere sempre. Il folle non diventa un compagno.",

    # ---------------------------------------------------------- :76794
    (76794, '(Readable) diary of a dog-eared big sister, it befriends them when read.'):
        "Un libro che fa della sorella cane maggiore un compagno. Si legge.",

    # ---------------------------------------------------------- :76938
    (76938, '(Readable) diary of a older sister, it befriends them when read.'):
        "Un libro che fa della sorella maggiore un compagno. Si legge.",

    # ---------------------------------------------------------- :81067
    (81067, '(Readable) wampeter of karass, it brings zah-mah-ki-bo to them when read.'):
        "Un libro che fa di qualcosa un compagno. Si legge.",

    # ---------------------------------------------------------- :83700
    (83700, '(Readable) book that can resurrect dead people.'):
        "Un libro che riporta in vita i morti. Si può leggere.",

    # ---------------------------------------------------------- :84236
    (84236, "(Readable) book about what's going on in town."):
        "Un libro che dice come va in città. Si può leggere.",

    # ---------------------------------------------------------- :86406
    (86406, "(Readable) book written by an author of children's stories."):
        "Un libro scritto da un autore di fiabe. Si può rileggere sempre.",

    # ---------------------------------------------------------- :89287
    (89287, '(Readable) diary of a young lady, it befriends them when read.'):
        "Un libro che fa della signorina un compagno. Si legge.",

    # ---------------------------------------------------------- :89359
    (89359, '(Readable) secret diary of a younger sister, it befriends them when read.'):
        "Un libro che fa della sorella gatta minore un compagno. Si legge.",

    # ---------------------------------------------------------- :93295
    (93295, '(Readable) book that increases the potential of a given skill.'):
        "Un libro che alza il potenziale di un'abilità scelta. Si legge.",

    # ---------------------------------------------------------- :97203
    (97203, '(Readable) diary of a younger sister, it befriends them when read.'):
        "Un libro che fa della sorella minore un compagno. Si legge.",

    # ---------------------------------------------------------- :129513
    (129513, 'generated when failed to create an item.'):
        "Compare quando la creazione di un oggetto fallisce.",

# 20 voci, 0 ambigue
}
