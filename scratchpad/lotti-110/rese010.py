import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :57128
    (57128, '(Openable) paper bag that are not visible through.'):
        "Un sacchetto di carta: dentro non si vede. Si può aprire.",

    # ---------------------------------------------------------- :78661
    (78661, 'It is a pack of 5 cards.'):
        "Un pacchetto di carte a caso, numerate di seguito.",

    # ---------------------------------------------------------- :80739
    (80739, '(Openable) container that all sorts of things.'):
        "Un sacco pieno di cose di ogni genere. Si può aprire.",

    # ---------------------------------------------------------- :81263
    (81263, '(Openable) container that contains a cat.'):
        "Una scatola con dentro un gatto. Si può aprire.",

    # ---------------------------------------------------------- :81944
    (81944, '(Openable) container with coins inside and rarely ,large sums of money.'):
        "Una scatola con spiccioli, e di rado un tesoro. Si può aprire.",

    # ---------------------------------------------------------- :88150
    (88150, '(Openable) container that can hold 4 types of food.'):
        "Tiene 4 cibi senza farli marcire. Si può aprire.",

    # ---------------------------------------------------------- :89824
    (89824, '(Openable) container that hold the tax bill and the accompanying tax.'):
        "Una scatola per la fattura e i soldi delle tasse. Si può aprire.",

    # ---------------------------------------------------------- :90835
    (90835, '(Openable) fetters that restrains a giant.'):
        "I ceppi che tengono legato un gigante. Si può aprire.",

    # ---------------------------------------------------------- :92189
    (92189, '(Openable) container keep 15 different types of food from spoiling.'):
        "Tiene 15 cibi senza farli marcire. Si può aprire.",

    # ---------------------------------------------------------- :93423
    (93423, "(Openable) safe for the store's sales."):
        "La cassaforte con l'incasso del negozio. Si può aprire.",

    # ---------------------------------------------------------- :93486
    (93486, '(Openable) container that holds designated items.'):
        "Una scatola per riporre le cose indicate. Si può aprire.",

    # ---------------------------------------------------------- :94384
    (94384, '(Openable) box to receive the earned salary.'):
        "Una scatola dove arriva la paga. Si può aprire.",

    # ---------------------------------------------------------- :96847
    (96847, '(Openable) trunk to receive ancestral relics left by past characters.'):
        "Una borsa con l'eredità dei personaggi passati. Si può aprire.",

    # ---------------------------------------------------------- :103236
    (103236, '(Openable) sphere that contains a rare item.'):
        "Una sfera piena di oggetti. Si può aprire.",

    # ---------------------------------------------------------- :104728
    (104728, '(Openable) box filled with materials.'):
        "Una scatola con materiali da lavorazione. Si può aprire.",

    # ---------------------------------------------------------- :107117
    (107117, '(Openable) trunk containing weapons and armor.'):
        "Una borsa con armi e armature. Si può aprire.",

    # ---------------------------------------------------------- :112199
    (112199, '(Openable) wallet lost by a tourist.'):
        "Un sacchetto con denaro e beni. Si può aprire.",

    # ---------------------------------------------------------- :112261
    (112261, '(Openable) suitcase lost by a tourist.'):
        "Una borsa con denaro e beni. Si può aprire.",

    # ---------------------------------------------------------- :115137
    (115137, '(Openable) container containing money and goods.'):
        "Una scatola con denaro e beni. Si può aprire.",

    # ---------------------------------------------------------- :115199
    (115199, '(Openable) very heavy chest.'):
        "Una scatola pesantissima con denaro e beni. Si può aprire.",

    # ---------------------------------------------------------- :115261
    (115261, '(Openable) ancient jeweled chest.'):
        "Una scatola con denaro e beni. Si può aprire.",

# 21 voci, 0 ambigue
}
