import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :47362
    (47362, 'Book of Rank 6 Magic. Area of Effect spell that does lightning damage.'):
        "Un libro per una magia ad area di fulmine. Si può leggere.",

    # ---------------------------------------------------------- :47435
    (47435, 'Book of Rank 7 Magic. Area of Effect spell that does darkness damage.'):
        "Un libro per una magia ad area d'oscurità. Si può leggere.",

    # ---------------------------------------------------------- :47508
    (47508, 'Book of Rank 7 Magic. Area of Effect spell that does nether damage.'):
        "Un libro per una magia ad area d'oltretomba. Si può leggere.",

    # ---------------------------------------------------------- :47581
    (47581, 'Book of Rank 7 Magic. Area of Effect spell that does poison damage.'):
        "Un libro per una magia ad area velenosa. Si può leggere.",

    # ---------------------------------------------------------- :47654
    (47654, 'Book of Rank 8 Magic. Area of Effect spell that does physical damage.'):
        "Un libro per una magia ad area di tipo PV/DV. Si può leggere.",

    # ---------------------------------------------------------- :47727
    (47727, 'Book of Rank 7 Magic. Area of Effect spell that does mind damage.'):
        "Un libro per una magia ad area mentale. Si può leggere.",

    # ---------------------------------------------------------- :47800
    (47800, 'Book of Rank 7 Magic. Area of Effect spell that does nerve damage.'):
        "Un libro per una magia ad area dei nervi. Si può leggere.",

    # ---------------------------------------------------------- :47873
    (47873, 'Book of Rank 5 Magic. Bolt type spell that does nether damage.'):
        "Un libro per una saetta d'oltretomba. Si può leggere.",

    # ---------------------------------------------------------- :47946
    (47946, 'Book of Rank 5 Magic. Bolt type spell that does poison damage.'):
        "Un libro per una saetta velenosa. Si può leggere.",

    # ---------------------------------------------------------- :48019
    (48019, 'Book of Rank 5 Magic. Bolt type spell that does sound damage.'):
        "Un libro per una saetta sonora. Si può leggere.",

    # ---------------------------------------------------------- :48092
    (48092, 'Book of Rank 5 Magic. Bolt type spell that does chaos damage.'):
        "Un libro per una saetta caotica. Si può leggere.",

    # ---------------------------------------------------------- :48165
    (48165, 'Book of Rank 5 Magic. Bolt type spell that does nerve damage.'):
        "Un libro per una saetta dei nervi. Si può leggere.",

    # ---------------------------------------------------------- :48238
    (48238, 'Book of Rank 2 Magic. Arrow type spell that does fire damage.'):
        "Un libro per una freccia di fuoco. Si può leggere.",

    # ---------------------------------------------------------- :48311
    (48311, 'Book of Rank 2 Magic. Arrow type spell that does cold damage.'):
        "Un libro per una freccia di gelo. Si può leggere.",

    # ---------------------------------------------------------- :48384
    (48384, 'Book of Rank 2 Magic. Arrow type spell that does lightning damage.'):
        "Un libro per una freccia di fulmine. Si può leggere.",

    # ---------------------------------------------------------- :48457
    (48457, 'Book of Rank 3 Magic. Arrow type spell that does mind damage.'):
        "Un libro per una freccia mentale. Si può leggere.",

    # ---------------------------------------------------------- :48530
    (48530, 'Book of Rank 3 Magic. Arrow type spell that does poison damage.'):
        "Un libro per una freccia velenosa. Si può leggere.",

    # ---------------------------------------------------------- :48603
    (48603, 'Book of Rank 3 Magic. Arrow type spell that does sound damage.'):
        "Un libro per una freccia sonora. Si può leggere.",

    # ---------------------------------------------------------- :48676
    (48676, 'Book of Rank 3 Magic. Arrow type spell that does physical damage.'):
        "Un libro per una freccia di tipo PV/DV. Si può leggere.",

    # ---------------------------------------------------------- :58996
    (58996, 'Book of Rank 1 Magic. Increases CON/CHR, give resist to Paralysis/Blind.'):
        "Un libro per alzare Cos e Car e resistere a paralisi e cecità.",

    # ---------------------------------------------------------- :61869
    (61869, 'Book of Rank 5 Magic. Bolt type spell that does physical damage.'):
        "Un libro per una saetta di tipo PV/DV. Si può leggere.",

    # ---------------------------------------------------------- :65603
    (65603, 'Book of Rank 1 Magic. Increases PER/WIL, give resist to Sleep/Confuse.'):
        "Un libro per alzare Per e Vol e resistere a sonno e confusione.",

    # ---------------------------------------------------------- :72960
    (72960, 'Book of Rank 2 Magic. It lets you float and dodge inaccurate attacks.'):
        "Un libro per liberarsi dal peso e schivare meglio.",

    # ---------------------------------------------------------- :78730
    (78730, '(Single-use) paper that teaches you new recipes.'):
        "Un foglio per imparare un piatto difficile. Si usa (usa e getta).",

    # ---------------------------------------------------------- :82080
    (82080, 'Book of Rank 4 Magic. It makes gold pieces rain from the sky.'):
        "Un libro per far piovere monete d'oro dal cielo. Si può leggere.",

    # ---------------------------------------------------------- :82153
    (82153, 'Book of Rank 7 Magic. It summons a rift of pocket realm to storage items.'):
        "Un libro per evocare uno spazio dove tenere gli oggetti.",

    # ---------------------------------------------------------- :83558
    (83558, 'Book of Rank 12 Magic. The blessing negates fatal damage occasionally.'):
        "Un libro per azzerare, a volte, un colpo mortale.",

    # ---------------------------------------------------------- :84443
    (84443, 'Book of Rank 2 Magic. Bolt type spell that does magic damage.'):
        "Un libro per una saetta magica. Si può leggere.",

    # ---------------------------------------------------------- :84516
    (84516, 'Book of Rank 5 Magic. Area of Effect spell that does magical damage.'):
        "Un libro per una magia ad area arcana. Si può leggere.",

    # ---------------------------------------------------------- :85104
    (85104, '(Readable) book with ancient knowledge.'):
        "Un libro con dentro un sapere antico. Si può leggere.",

    # ---------------------------------------------------------- :86943
    (86943, 'Book of Rank 4 Magic. Arrow type spell that does darkness damage.'):
        "Un libro per una freccia d'oscurità. Si può leggere.",

    # ---------------------------------------------------------- :89013
    (89013, 'Book of Rank 3 Magic. It reset memories of hostile situations.'):
        "Un libro per far dimenticare l'ostilità a chi non è un mostro.",

    # ---------------------------------------------------------- :91985
    (91985, 'Book of Rank 3 Magic. It manifests a door on target object.'):
        "Un libro per aprire una porta dove vuoi. Si può leggere.",

    # ---------------------------------------------------------- :92873
    (92873, 'Book of Rank 6 Magic. It can generate walls of flame on targeted spot.'):
        "Un libro per alzare muri di fiamme dove vuoi. Si può leggere.",

    # ---------------------------------------------------------- :93225
    (93225, 'Book of Rank 5 Magic. It can generate pools of acid on targeted spot.'):
        "Un libro per creare una pozza d'acido dove vuoi. Si può leggere.",

    # ---------------------------------------------------------- :94178
    (94178, 'Book of Rank 5 Magic. It can restore HP of the touched ally.'):
        "Un libro per curare te o un compagno che ti sta accanto.",

    # ---------------------------------------------------------- :94322
    (94322, 'Book of Rank 5 Magic. It can restore HP of every nearby ally.'):
        "Un libro per curare i compagni qui intorno. Si può leggere.",

    # ---------------------------------------------------------- :94457
    (94457, 'Book of Rank 3 Magic. It manifests a wall at target location.'):
        "Un libro per alzare un muro dove vuoi. Si può leggere.",

    # ---------------------------------------------------------- :98652
    (98652, 'Book of Rank 2 Magic. It creates spider webs on the targeted spot.'):
        "Un libro per tendere una ragnatela sul bersaglio. Si può leggere.",

    # ---------------------------------------------------------- :98877
    (98877, "Book of Rank 20 Magic. It bends target's will, making them join you."):
        "Un libro per tirare il bersaglio dalla tua parte. Si può leggere.",

    # ---------------------------------------------------------- :102040
    (102040, 'Book of Rank 20 Magic. It lets you mutate yourself.'):
        "Un libro per farsi venire una mutazione. Si può leggere.",

    # ---------------------------------------------------------- :103652
    (103652, 'Book of Rank 3 Magic. It highlights hidden objects around you.'):
        "Un libro per scoprire gli oggetti qui intorno. Si può leggere.",

    # ---------------------------------------------------------- :104522
    (104522, 'Book of Rank 4 Magic. Helps handling various anomalies created by tomes.'):
        "Un libro per farsi aiutare nella lettura. Si può leggere.",

    # ---------------------------------------------------------- :104595
    (104595, 'Book of Rank 5 Magic. It reduces various magical resistance of target.'):
        "Un libro per abbassare per un po' le resistenze mentali altrui.",

    # ---------------------------------------------------------- :105231
    (105231, 'Book of Rank 8 Magic. It dispels various hex on the user.'):
        "Un libro per togliersi di dosso tutte le maledizioni.",

    # ---------------------------------------------------------- :105304
    (105304, 'Book of Rank 5 Magic. It dispels one hex from nearby people.'):
        "Un libro per togliersi di dosso una maledizione.",

    # ---------------------------------------------------------- :105528
    (105528, 'Book of Rank 8 Magic. It enhances your resistance against curses.'):
        "Un libro per resistere un po' alle maledizioni. Si può leggere.",

    # ---------------------------------------------------------- :105672
    (105672, 'Book of Rank 6 Magic. It reduces elemental magical resistance of target.'):
        "Un libro per abbassare per un po' le resistenze elementali altrui.",

    # ---------------------------------------------------------- :105745
    (105745, 'Book of Rank 4 Magic. It reduces physical resilience of target.'):
        "Un libro per abbassare per un po' il PV del bersaglio.",

    # ---------------------------------------------------------- :105889
    (105889, 'Book of Rank 1 Magic. Increases STR/DEX, give resist to Fear/Confuse.'):
        "Un libro per alzare For e Des e resistere a terrore e confusione.",

    # ---------------------------------------------------------- :106184
    (106184, 'Book of Rank 5 Magic. It reduces the speed of the target..'):
        "Un libro per rallentare il bersaglio. Si può leggere.",

    # ---------------------------------------------------------- :106257
    (106257, 'Book of Rank 9 Magic. It increases the speed of user.'):
        "Un libro per accelerare. Si può leggere.",

    # ---------------------------------------------------------- :106401
    (106401, 'Book of Rank 4 Magic. It raises various magical resistance of user.'):
        "Un libro per alzare per un po' le resistenze. Si può leggere.",

    # ---------------------------------------------------------- :106545
    (106545, 'Book of Rank 5 Magic. It activates the healing factor of the user.'):
        "Un libro per alzare per un po' la guarigione. Si può leggere.",

    # ---------------------------------------------------------- :106689
    (106689, 'Book of Rank 6 Magic. It silences the target.'):
        "Un libro per mettere il bersaglio in silenzio. Si può leggere.",

    # ---------------------------------------------------------- :106842
    (106842, 'Book of Rank 2 Magic. Raise ones dodge abilities and give resist to fear.'):
        "Un libro per alzare per un po' il DV e resistere al terrore.",

    # ---------------------------------------------------------- :111853
    (111853, 'Book of Rank 50 Magic. It grants the user a chance to say their wishes.'):
        "Un libro per poter esprimere un desiderio. Si può leggere.",

    # ---------------------------------------------------------- :112955
    (112955, 'Book of Rank 7 Magic. Area of Effect spell that does chaos damage.'):
        "Un libro per una magia ad area caotica. Si può leggere.",

    # ---------------------------------------------------------- :113028
    (113028, 'Book of Rank 7 Magic. Area of Effect spell that does sound damage.'):
        "Un libro per una magia ad area sonora. Si può leggere.",

    # ---------------------------------------------------------- :113101
    (113101, 'Book of Rank 6 Magic. Area of Effect spell that does fire damage.'):
        "Un libro per una magia ad area di fuoco. Si può leggere.",

    # ---------------------------------------------------------- :113174
    (113174, 'Book of Rank 6 Magic. Area of Effect spell that does cold damage.'):
        "Un libro per una magia ad area di gelo. Si può leggere.",

    # ---------------------------------------------------------- :113247
    (113247, 'Book of Rank 6 Magic. Bolt type spell that does mind damage.'):
        "Un libro per una saetta mentale. Si può leggere.",

    # ---------------------------------------------------------- :113320
    (113320, 'Book of Rank 6 Magic. Bolt type spell that does darkness damage.'):
        "Un libro per una saetta d'oscurità. Si può leggere.",

    # ---------------------------------------------------------- :113462
    (113462, 'Book of Rank 3 Magic. Arrow type spell that does nerve damage.'):
        "Un libro per una freccia dei nervi. Si può leggere.",

    # ---------------------------------------------------------- :113535
    (113535, 'Book of Rank 3 Magic. Arrow type spell that does chaos damage.'):
        "Un libro per una freccia caotica. Si può leggere.",

    # ---------------------------------------------------------- :113608
    (113608, 'Book of Rank 3 Magic. Arrow type spell that does nether damage.'):
        "Un libro per una freccia d'oltretomba. Si può leggere.",

    # ---------------------------------------------------------- :114016
    (114016, 'Book of Rank 1 Magic. Arrow type spell that does magical damage.'):
        "Un libro per una freccia magica. Si può leggere.",

    # ---------------------------------------------------------- :114353
    (114353, 'Book of Rank 12 Magic. It heals the spell user greatly.'):
        "Un libro per recuperare HP. Si può leggere.",

    # ---------------------------------------------------------- :114426
    (114426, 'Book of Rank 8 Magic. It heals the spell user.'):
        "Un libro per recuperare HP. Si può leggere.",

    # ---------------------------------------------------------- :114499
    (114499, 'Book of Rank 4 Magic. It heals the spell user.'):
        "Un libro per recuperare HP. Si può leggere.",

    # ---------------------------------------------------------- :114572
    (114572, 'Book of Rank 1 Magic. It heals the spell user.'):
        "Un libro per recuperare HP. Si può leggere.",

    # ---------------------------------------------------------- :114645
    (114645, 'Book of Rank 6 Magic. It teleports user to location across the continent.'):
        "Un libro per tornare in un posto preciso. Si può leggere.",

    # ---------------------------------------------------------- :114718
    (114718, 'Book of Rank 15 Magic. It shows the user location of powerful artifacts.'):
        "Un libro per sapere dove sono finiti gli artefatti apparsi.",

    # ---------------------------------------------------------- :114791
    (114791, 'Book of Rank 5 Magic. It illuminates nearby walls to create a map.'):
        "Un libro per rivelare le zone non esplorate. Si può leggere.",

    # ---------------------------------------------------------- :123360
    (123360, 'Book of Rank 3 Magic. It summons several monsters from a nearby Nefia.'):
        "Un libro per evocare mostri. Si può leggere.",

    # ---------------------------------------------------------- :123495
    (123495, 'Book of Rank 1 Magic. It teleports user for a short distance.'):
        "Un libro per un teletrasporto corto. Si può leggere.",

    # ---------------------------------------------------------- :128871
    (128871, 'Book of Rank 4 Magic. Bolt type spell that does lightning damage.'):
        "Un libro per una saetta di fulmine. Si può leggere.",

    # ---------------------------------------------------------- :128944
    (128944, 'Book of Rank 4 Magic. Bolt type spell that does fire damage.'):
        "Un libro per una saetta di fuoco. Si può leggere.",

    # ---------------------------------------------------------- :129017
    (129017, 'Book of Rank 4 Magic. Bolt type spell that does ice damage.'):
        "Un libro per una saetta di gelo. Si può leggere.",

    # ---------------------------------------------------------- :129727
    (129727, 'Book of Rank 7 Magic. It uncursed equipped items.'):
        "Un libro per purificare gli oggetti. Si può leggere.",

    # ---------------------------------------------------------- :129800
    (129800, 'Book of Rank 8 Magic. It identifies an item for the user.'):
        "Un libro per identificare un oggetto. Si può leggere.",

    # ---------------------------------------------------------- :129873
    (129873, 'Book of Rank 5 Magic. It teleports user for a distance.'):
        "Un libro per il teletrasporto. Si può leggere.",

# 82 voci, 0 ambigue
}
