import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :61949
    (61949, 'It is a rod that, when zapped, unleash an area-of-effect physical attack.'):
        "Una bacchetta che, agitata, fa un attacco ad area di tipo PV/DV.",

    # ---------------------------------------------------------- :62317
    (62317, 'It is a rod that, when zapped, unleashes a beam of magical torrent.'):
        "Una bacchetta che, agitata, tira una saetta arcana.",

    # ---------------------------------------------------------- :62397
    (62397, 'It is a rod that, when zapped, unleashes an area-of-effect poison attack.'):
        "Una bacchetta che, agitata, fa un attacco ad area di veleno.",

    # ---------------------------------------------------------- :70754
    (70754, 'It is a rod that, when zapped, unleash an area-of-effect electric shock.'):
        "Una bacchetta che, agitata, fa un attacco ad area di fulmine.",

    # ---------------------------------------------------------- :71859
    (71859, 'It is a rod that, when zapped, unleashes an area-of-effect dark pulse.'):
        "Una bacchetta che, agitata, fa un attacco ad area d'oscurità.",

    # ---------------------------------------------------------- :92065
    (92065, 'It is a rod that, when zapped, manifests doorways on nearby walls.'):
        "Una bacchetta che, agitata, apre porte nei muri vicini.",

    # ---------------------------------------------------------- :92800
    (92800, 'It is a rod that, when zapped, creates walls of flame at target location.'):
        "Una bacchetta che, agitata, alza muri di fiamme dove vuoi.",

    # ---------------------------------------------------------- :93152
    (93152, 'It is a rod that, when zapped, creates pools of acid at target location.'):
        "Una bacchetta che, agitata, crea una pozza d'acido dove vuoi.",

    # ---------------------------------------------------------- :94105
    (94105, 'It is a rod that, when zapped, heal wounds of nearby target.'):
        "Una bacchetta che, agitata, cura te o chi ti sta accanto.",

    # ---------------------------------------------------------- :94537
    (94537, 'It is a rod that, when zapped, creates magical walls at target location.'):
        "Una bacchetta che, agitata, alza muri magici dove vuoi.",

    # ---------------------------------------------------------- :96278
    (96278, 'It is a rod that, when zapped, reconstruct targeted items.'):
        "Una bacchetta che, agitata, ricostruisce l'oggetto scelto.",

    # ---------------------------------------------------------- :96358
    (96358, 'It is a rod that, when zapped, forcifully transforms target creature.'):
        "Una bacchetta che, agitata, ricostruisce il bersaglio.",

    # ---------------------------------------------------------- :98579
    (98579, 'It is a rod that, when zapped, creates spider webs at target location.'):
        "Una bacchetta che, agitata, tende una ragnatela sul bersaglio.",

    # ---------------------------------------------------------- :98957
    (98957, 'It is a rod that, when zapped, dominates target creature.'):
        "Una bacchetta che, agitata, ti sottomette il bersaglio.",

    # ---------------------------------------------------------- :103508
    (103508, 'It is a rod that, when zapped, uncurses nearby equipped items.'):
        "Una bacchetta che, agitata, purifica gli oggetti qui intorno.",

    # ---------------------------------------------------------- :104945
    (104945, 'It is a rod that, when zapped, restores your mana.'):
        "Una bacchetta che, agitata, ti recupera gli MP.",

    # ---------------------------------------------------------- :105384
    (105384, 'It is a rod that, when zapped, protects nearby target from curses.'):
        "Una bacchetta che, agitata, para le maledizioni a te e ai vicini.",

    # ---------------------------------------------------------- :105969
    (105969, 'It is a rod that, when zapped, puts nearby target in accelerated status.'):
        "Una bacchetta che, agitata, accelera te o chi ti sta accanto.",

    # ---------------------------------------------------------- :106769
    (106769, 'It is a rod that, when zapped, silences the target.'):
        "Una bacchetta che, agitata, mette il bersaglio in silenzio.",

    # ---------------------------------------------------------- :111780
    (111780, 'It is a rod that, when zapped, grants audience to the wish goddess.'):
        "Una bacchetta che, agitata, dà modo di esprimere un desiderio.",

    # ---------------------------------------------------------- :117762
    (117762, 'It is a rod that, when zapped, scan and maps undiscovered areas.'):
        "Una bacchetta che, agitata, rivela le zone non esplorate.",

    # ---------------------------------------------------------- :119544
    (119544, 'It is a rod that, when zapped, puts a nearby target in slow motion.'):
        "Una bacchetta che, agitata, rallenta il bersaglio.",

    # ---------------------------------------------------------- :119624
    (119624, 'It is a rod that, when zapped, unleashes a beam of electric torrent.'):
        "Una bacchetta che, agitata, tira una saetta di fulmine.",

    # ---------------------------------------------------------- :122824
    (122824, 'It is a rod that, when zapped, heal wounds of nearby target.'):
        "Una bacchetta che, agitata, cura te o chi ti sta accanto.",

    # ---------------------------------------------------------- :122967
    (122967, 'It is a rod that, when zapped, unleashes a beam of heat wave.'):
        "Una bacchetta che, agitata, tira una saetta di fuoco.",

    # ---------------------------------------------------------- :123047
    (123047, 'It is a rod that, when zapped, unleashes a beam of freezing air.'):
        "Una bacchetta che, agitata, tira una saetta di gelo.",

    # ---------------------------------------------------------- :123127
    (123127, 'It is a rod that, when zapped, opens a rift containing hostile creatures.'):
        "Una bacchetta che, agitata, evoca mostri ostili qui intorno.",

    # ---------------------------------------------------------- :123207
    (123207, 'It is a rod that, when zapped, shoots an arrow of concentrated magic.'):
        "Una bacchetta che, agitata, tira un dardo magico.",

    # ---------------------------------------------------------- :129953
    (129953, 'It is a rod that, when zapped, teleports nearby target.'):
        "Una bacchetta che, agitata, teletrasporta a caso.",

    # ---------------------------------------------------------- :130033
    (130033, 'It is a rod that, when zapped, reveal the structure of targeted item.'):
        "Una bacchetta che, agitata, identifica gli oggetti che porti.",

# 30 voci, 0 ambigue
}
