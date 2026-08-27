import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :42855
    (42855, "It's a pair of extremely durable and sharp claws."):
        "Degli artigli molto resistenti e affilati.",

    # ---------------------------------------------------------- :57965
    (57965, 'It is a godly gift that when worn, transforms into manacles.'):
        "Se lo indossi, si trasforma in manette.",

    # ---------------------------------------------------------- :59595
    (59595, 'It is a squared small shield.'):
        "Uno scudo piccolo e quadrato.",

    # ---------------------------------------------------------- :59863
    (59863, 'It is a mirror shield made of polished obsidian.'):
        "Uno scudo a specchio, fatto di ossidiana levigata.",

    # ---------------------------------------------------------- :67602
    (67602, 'It is a light, sharp claws.'):
        "Degli artigli leggeri e affilati.",

    # ---------------------------------------------------------- :68253
    (68253, 'These are laws sturdy enough to be used like a shield.'):
        "Degli artigli abbastanza robusti.",

    # ---------------------------------------------------------- :69259
    (69259, 'These are sharp, dreadful claws.'):
        "Degli artigli affilati da far paura.",

    # ---------------------------------------------------------- :71236
    (71236, 'It is a tonfa with a built-in propulsion system.'):
        "Un tonfa con un propulsore incorporato.",

    # ---------------------------------------------------------- :71305
    (71305, 'It is a tonfa that generates photon blades.'):
        "Un tonfa da cui escono lame laser.",

    # ---------------------------------------------------------- :71374
    (71374, 'It is a tonfa that allows quick concessive strikes.'):
        "Un tonfa che attacca a raffica.",

    # ---------------------------------------------------------- :71442
    (71442, 'It is a tonfa with a built-in shield generator.'):
        "Un tonfa con un dispositivo di difesa incorporato.",

    # ---------------------------------------------------------- :71512
    (71512, 'It is a tonfa that suc'):
        "Un tonfa.",

    # ---------------------------------------------------------- :73563
    (73563, 'It is a highly defensive shield.'):
        "Uno scudo con la difesa alta.",

    # ---------------------------------------------------------- :81331
    (81331, 'It is a wooden plank that was used on a ship.'):
        "Un'asse di legno che stava su una nave.",

    # ---------------------------------------------------------- :82413
    (82413, 'It is a shield that induce bleeding.'):
        "Uno scudo che provoca sanguinamento.",

    # ---------------------------------------------------------- :82481
    (82481, 'It is a shield in the shape of an instrument.'):
        "Uno scudo a forma di strumento musicale, difende come un muro.",

    # ---------------------------------------------------------- :100720
    (100720, 'It is a very heavy shields'):
        "Uno scudo pesantissimo.",

    # ---------------------------------------------------------- :100786
    (100786, 'It is a large shield shaped like a kite.'):
        "Uno scudo lungo.",

    # ---------------------------------------------------------- :100852
    (100852, 'It is a large circular shield.'):
        "Uno scudo duro.",

    # ---------------------------------------------------------- :100918
    (100918, 'It is the type of armor you hold on your hands.'):
        "Un'armatura che si equipaggia in mano.",

    # ---------------------------------------------------------- :100984
    (100984, 'It is a round shield.'):
        "Uno scudo rotondo.",

    # ---------------------------------------------------------- :101050
    (101050, 'It is a smaller and lighter shield.'):
        "Uno scudo per chi porta armatura leggera.",

    # ---------------------------------------------------------- :127207
    (127207, 'It is a shield given to knights.'):
        "Uno scudo per i cavalieri.",

# 23 voci, 0 ambigue
}
