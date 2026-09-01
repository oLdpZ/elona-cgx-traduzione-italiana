import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :76115
    (76115, 'The training equipment of the God of Earth. It is not heavy, but when you put it on, you can hardly move and even feel as if you are fixed to the earth. \\n# ~Irva Fantasy Encyclopedia~'):
        "L'attrezzo da allenamento del dio della terra. Non è che pesi, eppure a metterlo addosso non ci si muove quasi più, e viene perfino la sensazione di essere fissati alla terra. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :86867
    (86867, 'A solid shoe made of leather. They are more comfortable than expected and will be your one and only friend on a long trip. \\n# ~Irva Fantasy Encyclopedia~'):
        "Delle scarpe solide, fatte di cuoio. Si adattano al piede più di quanto ci si aspetti, e in un viaggio lungo diventeranno l'amico che non ha pari. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :93757
    (93757, 'A pair of shoes with a magic that allows you to run long distances in an instant. A famous peddler, who had been traveling around the world thanks to these shoes, achieved his current position. \\n# ~Irva Fantasy Encyclopedia~'):
        "Delle scarpe su cui è stata posata una magia che fa correre in un istante distanze lunghissime. E non è una vanteria: pare che un mercante ambulante di gran fama, grazie a queste scarpe, abbia girato il mondo in lungo e in largo e si sia guadagnato la posizione che ha oggi. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :100456
    (100456, 'Shoes that completely cover the feet and legs. The structure of the shoes is designed to provide perfect protection, but it seems that all such shoes are heavy. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Delle scarpe che coprono per intero dal piede alla gamba. Quella struttura, che non lascia scoperto un varco, punta alla protezione perfetta; ma le cose di quel genere, si sa, pesano tutte. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100521
    (100521, "Well-made shoes. Their careful craftsmanship shows the craftsman's strong desire. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Delle scarpe fatte bene. In quella cura si sente quanto ci ha tenuto l'artigiano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100586
    (100586, 'Footwear that completely covers the feet. Although somewhat inadequate for combat use, this is sufficient for daily use. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Delle calzature che coprono il piede per intero. Per il combattimento c'è poco da fidarsi, ma per l'uso di tutti i giorni tanto basta. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100651
    (100651, 'A simple piece of protective gear made to protect the feet. It is somewhat inadequate for combat use, but it is sufficient for daily use. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'armatura fatta alla buona per proteggere i piedi. Per il combattimento c'è poco da fidarsi, ma per l'uso di tutti i giorni tanto basta. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :130450
    (130450, 'Shoes made of a special composite material to provide stronger protection. They are extremely hard and are said to make a pleasant sound around the area just by walking. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Degli stivali che, incrociando materiali speciali, hanno ottenuto una protezione più solida. Sono durissimi, e dicono che al solo camminare mandino intorno un suono piacevole. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :130515
    (130515, 'Shoes covered with numerous pieces of material. Naturally, they are heavier than usual, but they offer better protection. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Delle scarpe a cui sono stati applicati moltissimi pezzetti di materiale. Pesano più del normale, è ovvio, ma in cambio la protezione ne esce più dura. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 9 voci, 0 ambigue
}
