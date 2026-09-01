import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :43044
    (43044, "Once upon a time, an evil secret society developed this hairpiece as part of their world domination scheme. It can change into various hairstyles, and once dyed, it's nearly impossible to identify the wearer. Even more terrifying, it can be controlled with brainwaves and used like a whip or drill to mercilessly kill unsuspecting victims. Only a few have been unearthed and restored by skilled craftsmen to this day. \\n# ~Irva Fantasy Encyclopedia~"):
        "Lo sviluppò un'organizzazione segreta che un tempo puntava alla conquista del mondo. È una parrucca che si trasforma in ogni acconciatura, e se poi viene pure tinta riconoscere chi la porta diventa quasi impossibile. Per giunta si comanda con le onde cerebrali, e ci sono casi di gente che l'ha adoperata come una frusta o un trapano per ammazzare uno dopo l'altro gli avversari distratti. Oggi ne restano sì e no i pochi esemplari dissotterrati e rimessi in sesto da qualche artigiano. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :43112
    (43112, "Once upon a time, an evil secret society developed this hairpiece as part of their world domination scheme. It can change into various hairstyles and was used for disguises, but cleverly, it could also double as a makeshift bulletproof helmet, concealing the fact that it was even being worn on one's head. Nowadays, only a few have been salvaged and painstakingly restored by skilled craftsmen. \\n# ~Irva Fantasy Encyclopedia~"):
        "Lo sviluppò un'organizzazione segreta che un tempo puntava alla conquista del mondo. È una parrucca che si trasforma in ogni acconciatura. La usavano per travestirsi, ma siccome protegge la testa senza lasciar vedere che la si porta, a volte serviva anche da giubbotto antiproiettile per il capo. Oggi ne restano sì e no i pochi esemplari dissotterrati e rimessi in sesto da qualche artigiano. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :65398
    (65398, 'Recovered from drifting in space. Analysis revealed that it was a helmet-shaped mechanical life form, but it was already unconscious when it was found. Part of its system has been successfully restored, and it is capable of simple gravity control and body function assistance. \\n# ~Irva Fantasy Encyclopedia~'):
        "L'hanno recuperato mentre andava alla deriva nello spazio. Dalle analisi è risultato una forma di vita meccanica a forma di casco, ma quando è stato trovato pare non avesse più coscienza di sé. Una parte dei suoi sistemi è stata rimessa in funzione, e riesce a controllare la gravità in modo elementare e ad assistere le funzioni del corpo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :66977
    (66977, 'The head of a Sunbararian. Shaped like a nautilus, it is covered with a hard shell and is surprisingly protective. Since it is probably completely dead, it is surely safe to wear, probably. \\n# ~Irva Fantasy Encyclopedia~'):
        "La testa di un alieno di Sunbararia. Fatta come un nautilo, è coperta da un guscio duro e difende sorprendentemente bene. Probabilmente è morta del tutto, quindi a mettersela in testa quasi di sicuro non dovrebbe succedere niente, si spera. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :66979
    (66979, '\\"ＡＳＤＪＵＲＨＦＫ＞ＲＯＷＲＷ＜ＭＷ！\\" \\n# ~words of a Sunbararian~'):
        "\\\"ASDJURHFK>ROWRW<MW!\\\" \\n# ~Parole di un alieno di Sunbararia~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :72418
    (72418, 'Special magical hats made of mana of wizards who were contacted by the abyss of magic. It is worn by wizards who have been resurrected as the undead, but there are rare wizards who create it while still alive. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un cappello magico speciale, fatto da un mago che in punto di morte ha sfiorato l'abisso della magia e ci ha messo dentro il mana che aveva da vivo. Lo portano i maghi tornati come non morti, ma qualche raro mago se lo fabbrica ancora da vivo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :76181
    (76181, 'Favorite toy of the Goddess of Fortune. If you touch it, your luck will be sucked out of you. \\n# ~Irva Fantasy Encyclopedia~'):
        "Il giocattolo preferito della dea della sorte. Se un mortale lo tocca male, la sorte gliela succhia via. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :80424
    (80424, 'Shiny black helmet characterized by its horns protruding forward. It is said that only one horn is unusually long because it mimics the characteristics of the creature from which it was devised. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un elmo di un nero lucido, che si riconosce dalle corna sporgenti in avanti. Dicono che una sola delle corna sia lunga in modo anomalo perché hanno copiato pari pari il tratto della creatura da cui l'hanno pensato. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :89077
    (89077, "Helmet made by a sage to attain a higher level. It is said that by wearing it, one can deepen one's knowledge and even see invisible beings. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un elmo che un saggio si fabbricò per puntare più in alto. A portarlo la conoscenza si fa più profonda, e dicono che si arrivi a vedere perfino ciò che non si potrebbe vedere. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :99872
    (99872, 'Helmets that combine special materials to provide stronger protection. While many of these examples exist, there seem to be few examples that compensate for the inimitable weakness of weight. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un elmo che, incrociando materiali speciali, ha ottenuto una protezione più solida. Di pezzi che sfruttano i pregi di un materiale e ne coprono i difetti se ne vedono tanti, ma pare che pochi riescano a coprire il difetto senza pari che è il peso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99937
    (99937, 'Armor made to protect the head. It has a wider range of protection than a hat, but is naturally heavier. There are some funny stories about people getting stiff shoulders after using it for a long time. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'armatura fatta per proteggere la testa. Copre più di un cappello, ma è chiaro che pesa anche di più. Girano perfino le storielle di chi, a portarlo per ore, si è ritrovato con le spalle indolenzite. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100002
    (100002, 'A prestigious helmet made for a knight. It is elaborately carved and decorated to suit the user, but it is not merely ceremonial and offers a certain degree of protection. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un elmo di gran classe, fatto per i cavalieri. Porta cesellature e ornamenti studiati su misura di chi lo indossa, ma non è roba da sola cerimonia: una certa protezione la dà davvero. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100067
    (100067, 'A helmet built thicker than normal helmets. The defensive power is certainly improved, but the weight is sacrificed, so care must be taken when wearing it. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un elmo fatto più spesso del normale. La difesa sale di sicuro, ma in cambio ci si rimette in peso, e a indossarlo conviene starci attenti. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100132
    (100132, 'A fashionable hat with bird feathers. It is often worn by bards because they liken their singing voice to that of birds. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un cappello elegante, ornato di penne d'uccello. Lo portano spesso i menestrelli, e pare sia perché paragonano la propria voce a quella degli uccelli. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :130844
    (130844, 'A very light hat worn by fairies. Perhaps because they consider themselves fragile, these hats have the ability to protect them from the mutations of the outside world. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un cappello leggerissimo che dicono portino le fate. Forse perché si ritengono creature fragili, quel cappello ha la facoltà di proteggere dalle mutazioni che vengono da fuori. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :130909
    (130909, 'A tall pointed cone hat that a mage would wear. There is no special effect of this shape, but wearing it makes you feel somewhat smarter. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un cappello a punta come quelli che uno si aspetta addosso a un mago. Effetti non ne dà nessuno, ma a metterlo in testa un vago senso di essere diventati più saggi lo mette. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 15 voci, 0 ambigue
}
