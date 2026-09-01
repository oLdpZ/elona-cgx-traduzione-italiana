import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :62463
    (62463, "A crystal sphere in the image of the supreme deity of the planet Yekub, and has the power to strengthen one's spirit. It is a popular souvenir among some aliens, who say that wearing it enables one to resist Sunbararian's hypnotism and mind absorption. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una sfera di cristallo fatta a immagine del dio supremo del pianeta Yekub, e porta in dono un rafforzamento dello spirito. A portarla addosso si resiste anche all'ipnosi degli Shan e all'assorbimento del pensiero dei Sakyubalorin: così dicono certi alieni, fra i quali è un souvenir molto apprezzato. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :76247
    (76247, 'Special collar that the Goddess of the wind puts on her prized pets. It has an invisible chain. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un collare speciale che la dea del vento mette al suo animale prediletto. Ci sta attaccata una catena che non si vede. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :81536
    (81536, 'A shell-shaped ornament made of mica with beautiful spirals. It is said to have been left behind by the gods. It is said that if you hold it gently to your ear, you can hear someone talking. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un ornamento a forma di conchiglia, fatto di mica, con una spirale bellissima. Chi l'abbia fatto non si sa affatto, e c'è chi dice che sia roba caduta agli dei. Pare che accostandolo piano all'orecchio si senta qualcuno che parla. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :82676
    (82676, 'Necklace that looks like a pair of tiny swords. When worn, it is said to give the wearer the ability to move quickly, as if he or she had two extra arms. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una collana che pare fatta di due piccole spade gemelle. Dicono che a portarla si acquisti un movimento svelto, come se le braccia fossero diventate due di più. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :82742
    (82742, 'Purple necklace that looks like a broken crossbow. It is said that when you wear it, covering fire will come out of nowhere. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una collana viola che pare una balestra spezzata. Dicono che a portarla addosso, da chissà dove, arrivi un tiro di copertura. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :83901
    (83901, 'Shabby necklace made of iron. It looks more like some kind of tag than an ornament, but it is said that this is because it is a symbol for lower class people to distinguish between friend and foe. \\n# ~Intel of the Informant Wiesem~'):
        "Una collana misera, fatta di ferro. Più che un ornamento sembra una targhetta, e si dice sia perché alla gente di bassa condizione serve da segno per distinguere gli amici dai nemici. \\n# ~Le Notizie Raccolte da <Wiesem> l'informatore~",

    # ---------------------------------------------------------- :99448
    (99448, 'Amulet of love is given to the bride-to-be at the wedding ceremony. Naturally, this amulet is considered the property of the spouse, and forcible attempts to take it away from him or her will incur his or her wrath. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una collana carica d'amore, che nel rito nuziale si dona a chi diventa compagno di vita. È chiaro che da quel momento la collana appartiene a lui, e a strappargliela per forza ci si tira addosso una collera furiosa. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99519
    (99519, 'An ornament with a polished surface. It is more of a jewelry item and is often used as a gift. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un ornamento con la superficie lucidata a specchio. A dirla tutta è più un gioiello che altro, e spesso si usa per farne dono. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99591
    (99591, 'Small ornaments are meant to ward off evil spirits. The ornaments are said to carry a variety of feelings. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un piccolo ornamento che vale soprattutto come scongiuro contro il male. Dicono che in quei fregi siano racchiusi i sentimenti più vari. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99663
    (99663, 'Armor made to protect the neck. It is more like a piece of armor than something to be worn. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un ornamento fatto per proteggere il collo. Più che indossarlo si direbbe che lo si equipaggia, ed è di fattura piuttosto rozza. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99735
    (99735, 'Accessories with special magic inside. It is not expected to provide direct protection, but it is said to often contain special abilities. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un ornamento in cui è racchiusa una magia particolare. Una protezione diretta non c'è da aspettarsela, ma spesso, dicono, nasconde dentro qualche facoltà fuori dal comune. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99807
    (99807, 'An ornament with a bright green gemstone at its center. Cut into a distinctive oval shape, it glows even at night and is considered by some to be a symbol of exceptional vitality. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un ornamento con al centro una gemma di un verde acceso. Tagliata in quella caratteristica forma d'uovo, brilla anche di notte, e c'è chi la dice simbolo di una forza vitale senza pari. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99809
    (99809, '\\"Well, what a lovely shape. It\'s round and green with a hint of red in it, perfect for him, who is like a transparent canvas. I bet when he sees this necklace...oh no!\\" \\n# ~Rianna the Daydreamer~'):
        "\\\"Oh, ma che forma graziosa. Tonda, verde, e dentro un rosso appena accennato: perfetta per lui, che è tutto una tela trasparente. Se quella persona vedesse questa collana, di sicuro... ohhh, che vergogna!\\\" \\n# ~Parole di <Rianna> la sognatrice~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :126647
    (126647, 'Ornaments worn around the neck. They can be made of a variety of materials and shapes, but those made of rare materials are often the most expensive. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un ornamento da portare intorno al collo. Ce n'è di ogni materiale e di ogni forma, e spesso i più cari sono quelli fatti con materiali rari. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 13 voci, 0 ambigue
}
