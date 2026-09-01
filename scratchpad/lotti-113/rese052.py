import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :102250
    (102250, "A scroll that allows people to deepen their faith by conversing with God. It's probably more like a letter to God than a scroll. \\n#~Arcane Alamanac~"):
        "Una pergamena che permette di approfondire la fede parlando col proprio dio. Più che una pergamena sarà una specie di lettera indirizzata a lui. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :102321
    (102321, 'These precious scrolls are enchanted to develop your body. Reading it will make you even stronger. \\n#~Arcane Alamanac~'):
        "Una pergamena preziosa, su cui è posata una magia che fa crescere il corpo. A leggerla diventerai più tenace. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :103576
    (103576, 'Scrolls that allow the user to detect the location of objects. It can detect objects behind walls, or even invisible objects, so it should be readied when searching for something. \\n#~Arcane Alamanac~'):
        "Una pergamena che fa avvertire dove c'è qualcosa. Sente anche al di là di un muro, dove non si sa cosa ci sia, e perfino gli oggetti invisibili: conviene tenerne pronta una quando si esplora. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :104446
    (104446, 'A scroll that makes you smarter temporarily. It is said that during the examination season, the tool shops are temporarily crowded with customers who rely on these scrolls without studying as far as they are concerned. \\n#~Arcane Alamanac~'):
        "Una pergamena che rende svegli per un po'. Si dice che nella stagione degli esami le botteghe si riempiano per un momento di clienti che, invece di studiare, contano su questa. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :104663
    (104663, 'Strange scrolls that, when read, cause materials to fall from the sky. It is still unclear why materials fall from the sky when the scroll is read. \\n#~Arcane Alamanac~'):
        "Una strana pergamena che, a leggerla, fa cadere dei materiali dal cielo. Perché a leggere una pergamena piovano materiali, questo legame non si è ancora capito. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :105013
    (105013, 'A scroll that, when read, instantly fills the body with mana. They say that having a scroll with you in an emergency is more useful than you think. \\n#~Arcane Alamanac~'):
        "Una pergamena che, letta, riempie di mana il corpo in un istante. Pare che averne una addosso nei momenti critici serva più di quanto si creda. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :105084
    (105084, 'A scroll that cancels all curses on the body. It does not cancel curses on equipment. \\n#~Arcane Alamanac~'):
        "Una pergamena che annulla tutte le maledizioni che si hanno addosso. Quelle su un oggetto indossato no: là, chissà perché, non funziona. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :105155
    (105155, 'A scroll that cancels 1 curses on the body. It does not cancel curses on equipment. \\n#~Arcane Alamanac~'):
        "Una pergamena che annulla una maledizione che si ha addosso. Quelle su un oggetto indossato no: là, chissà perché, non funziona. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :105452
    (105452, 'It is a scroll that temporarily deploys a sacred robe that is said to protect the body from curses. \\n#~Arcane Alamanac~'):
        "Una pergamena che stende per un po' un velo sacro, che si dice protegga dalle maledizioni che piombano addosso. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :106981
    (106981, 'Scrolls that break the curse of worn equipment. It is more powerful and thus never fails to break the curse. \\n#~Arcane Alamanac~'):
        "Una pergamena che toglie la maledizione a un oggetto indossato. Essendo più forte, la purificazione non fallisce mai. Dovrebbe. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :107052
    (107052, 'A scroll that appraises unappraised items. It is more powerful, but if the item still cannot be appraised, have it investigated by a mage instead. \\n#~Arcane Alamanac~'):
        "Una pergamena che identifica gli oggetti non identificati. È più forte del solito, ma se anche così l'oggetto non si lascia identificare, tanto vale farlo esaminare da un mago. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :108327
    (108327, 'A deed gives the right to a house. Even adventurers cannot always camp out in the wilderness. \\n# ~an Adventurer is You! Guide for Travels~'):
        "L'atto che serve come pratica per comprare una casa. Anche a essere avventurieri, non si può dormire sempre all'addiaccio. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :111921
    (111921, 'Dangerous scrolls that cast a curse on worn equipment. In some rare cases when it is used, it may not work and turn to dust, probably as a result of daily conduct. \\n#~Arcane Alamanac~'):
        "Una pergamena pericolosa, che getta una maledizione su un oggetto indossato. Certe rare volte, quando la si usa, non fa effetto e si sbriciola: sarà il frutto della condotta di tutti i giorni. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :114859
    (114859, 'A scroll that creates a small distortion in space, allowing a person to travel instantaneously. Because its potency is rather weak, there are some funny stories about people who used it when they were leaving someone, only to have it reappear nearby, causing them to feel awkward. \\n#~Arcane Alamanac~'):
        "Una pergamena che, creando una piccola piega nello spazio, sposta in un istante. Ha un effetto piuttosto debole, e si racconta per ridere di gente che l'ha usata per accomiatarsi da qualcuno e si è ritrovata a ricomparirgli accanto, con tutto l'imbarazzo del caso. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :114930
    (114930, 'Scrolls of magical knowledge. One theory is that they are fragments of pages that fell out of a book in which the gods had written down their magic so that they would not forget it. \\n#~Arcane Alamanac~'):
        "Una pergamena che fa affiorare di colpo nella testa una conoscenza magica. Secondo una teoria sono pezzi di pagina caduti dal libro in cui gli dei avevano messo per iscritto la propria magia, per non dimenticarla. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :115001
    (115001, 'Precious scrolls that are said to give new abilities when read. In distant, far away foreign lands, these scrolls were called Master Recipe Tomes. \\n#~Arcane Alamanac~'):
        "Una pergamena preziosa, che a leggerla darebbe una capacità nuova. Si dice che in terre lontane e straniere queste pergamene le chiamassero hidensho. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :115072
    (115072, "A scroll that instantly reads the surrounding terrain. This scroll is mainly for Nefia, so you can't use it to break into the house of that girl you're interested in. \\n#~Arcane Alamanac~"):
        "Una pergamena che legge in un istante il terreno intorno. Serve soprattutto dentro Nefia, quindi la trovata poco pulita di intrufolarsi in casa della ragazza che ti piace per usarla lì non funziona. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :115453
    (115453, 'A scroll that invokes a gate leading to the specified location. If used by mistake, it can be undone by reading it again. Naturally, two copies are consumed, but consider it a tuition fee. \\n#~Arcane Alamanac~'):
        "Una pergamena che chiama un portale collegato a un luogo preciso. Anche se la si usa per sbaglio, niente panico: rileggendola si annulla. Ovviamente se ne consumano due, ma pazienza: consideralo il prezzo della lezione. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :117256
    (117256, 'Scrolls that break the curse of worn equipment. It sometimes fails on strong curses. \\n#~Arcane Alamanac~'):
        "Una pergamena che toglie la maledizione a un oggetto indossato. Se la maledizione è troppo forte la purificazione fallisce, e allora conviene pensare a un'altra strada. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :130101
    (130101, 'A scroll that allows you to impersonate someone else in an instant. When you use it, you feel like a great thief who steals the country. \\n#~Arcane Alamanac~'):
        "Una pergamena che in un istante permette di farsi passare per un altro. Usandola ci si sente il grande ladro che tiene in scacco un regno. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :130172
    (130172, 'A scroll that creates a distortion in space, allowing you to travel elsewhere instantaneously. It is useful in emergencies, but the destination cannot be specified, so it cannot be used if you are late for a meeting, for example. \\n#~Arcane Alamanac~'):
        "Una pergamena che, creando una piega nello spazio, porta in un istante da un'altra parte. Nei momenti critici è comoda, ma la meta non si può scegliere: per quando si è in ritardo a un appuntamento, non serve. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :130243
    (130243, "The scrolls are supposed to tell you about the existence of legendary items. It doesn't even tell you who has it, God is not that friendly to you. \\n#~Arcane Alamanac~"):
        "Una pergamena che, si dice, faccia sapere dell'esistenza degli oggetti leggendari. Chi ce li abbia non lo dice: il dio non ti è amico fino a quel punto. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :130314
    (130314, 'A scroll that appraises unappraised items. It is useless agains powerful items, you will need a mage instead. \\n#~Arcane Alamanac~'):
        "Una pergamena che identifica gli oggetti non identificati. Con gli oggetti potenti certe volte non ce la fa, e in quei casi conviene farsi dare una mano da un mago. \\n#~Compendio Completo degli Oggetti Magici~",

# 23 voci, 0 ambigue
}
