import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :62801
    (62801, 'Sturdy white leather strap with metal fittings hammered into it. It is worn around the forearm and fist like a bandage. The metal fittings made of meteoric iron are said to contain magical power. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una cinghia di cuoio bianca e robusta, con delle borchie di metallo conficcate dentro. Si equipaggia avvolgendola dall'avambraccio fino al pugno, come una fasciatura. Pare che nelle borchie, fatte di ferro meteorico, ci sia dentro del potere magico. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :75647
    (75647, 'Flashy chains that the God of Wealth had custom-made. It is so gorgeous that just looking at it makes you feel sick. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una catena vistosissima, che la dea della ricchezza si è fatta fare su misura. È di uno sfarzo tale che a guardarla viene il voltastomaco. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :75714
    (75714, 'A blue glove with a mysterious pattern on its surface. It holds a spirit. \\n# ~Irva Fantasy Encyclopedia~'):
        "Dei guanti d'arme azzurri, con un disegno misterioso sulla superficie. Ci abita dentro uno spirito. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :101114
    (101114, 'A bracer made of a combination of special materials to provide stronger protection. It is mainly worn with armor. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Dei guanti d'arme che, incrociando materiali speciali, hanno ottenuto una protezione più solida. Si portano soprattutto in accordo con l'armatura di piastre. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101180
    (101180, 'These gloves are made to stick snugly to the skin. They are so light that you may forget you are wearing them. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Dei guanti fatti per aderire perfettamente alla pelle. Sono leggerissimi, tanto che ci si dimentica di averli addosso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101247
    (101247, 'These are warrior-style kote, made with an emphasis on protection above all else. They are somewhat heavy, but still have more than enough performance. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Dei guanti d'arme rozzi, fatti mettendo la protezione davanti a tutto. Pesano un po', ma rendono molto più di quel poco che pesano in più. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101314
    (101314, 'This armor is also meant to be a cold-weather gear. Not only that, it is also said to have no small effect as an anti-slip device for weapons. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'armatura che vale anche come riparo dal freddo. E non solo: dicono che serva non poco anche a non far scivolare l'arma di mano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :107527
    (107527, 'Made from parts of flame dragons. True to the rumor, it is always enveloped in flames, but the wearer does not feel the heat, let alone burn. \\n# ~Irva Fantasy Encyclopedia~'):
        "Dei guanti d'arme che dicono ricavati da un drago di fuoco. Come vuole la voce sono sempre avvolti nelle fiamme, eppure chi li porta, altro che bruciare, non sente nemmeno il caldo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :130582
    (130582, 'Armor made to protect the wrist and forearm. It does take away some of the freedom of the fingers, but it is better than losing a hand. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'armatura fatta per proteggere dal polso in avanti. Toglie un po' di libertà alle dita, ma è meglio che perdere una mano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :130649
    (130649, 'Fine gloves covered with assorted ornaments. Despite its ceremonial aspect, it still provides some protection through its decoration. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Dei guanti d'arme di pregio, cosparsi di lavorazioni d'ogni sorta. Contano soprattutto per la cerimonia, ma anche così quegli ornamenti una qualche protezione la danno. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 10 voci, 0 ambigue
}
