import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :56267
    (56267, "In some parts of Gaius Vis, a rabbit's foot, not its tail, is a lucky charm. It has been handed down since ancient times and is a popular travel companion among adventurers. \\n# ~the Aimwell tale of trade~"):
        "Una stampa che dicono disegnata sul posto, durante l'eruzione: un pezzo leggendario, ma in un altro senso. Da quella scena, che pare la fine del mondo, arrivano un calore soffocante e tutto il suo furore. \\n# ~Racconti di Commercio di Aimwell~",

    # ---------------------------------------------------------- :56333
    (56333, "In some parts of Gaius Vis, a rabbit's foot, not its tail, is a lucky charm. It has been handed down since ancient times and is a popular travel companion among adventurers. \\n# ~the Aimwell tale of trade~"):
        "In certe zone di Gaius Vis il portafortuna è la zampa del coniglio, non la coda. Si tramanda da tempi antichi, e fra gli avventurieri va per la maggiore come compagna di viaggio. \\n# ~Racconti di Commercio di Aimwell~",

    # ---------------------------------------------------------- :73894
    (73894, "Marimo that grows in a lake in South Tyris, is ripped off and artificially rounded up. The lake's marimo is in danger of extinction due to the mass harvesting. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Marimo che cresce nel lago di Tyris del Sud, strappato e poi arrotondato a mano. Per fabbricarlo se ne raccoglie tanto che il marimo del lago rischia l'estinzione. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :73960
    (73960, "Old military ration that was dispensed to the civilian by the Yerles Army as an ornamental item. Long since ruined as food. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una vecchia razione militare che l'esercito di Yerles ha ceduto ai civili come soprammobile. Come cibo è andata a male da un pezzo. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :86266
    (86266, "Trade goods filled with a set of painting tools. It cannot be used because paints and other materials will be scattered around when the package is opened. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio con dentro tutto l'occorrente per dipingere. Non si può usare: ad aprirla, i colori e il resto finiscono sparsi dappertutto. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :86332
    (86332, "The trade goods are a collection of paintings by various artists. Even so, they are kept in a minimum amount of storage, so there seems to be no trouble such as opening them at a trading partner and finding that they are worthless. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio che mette insieme alla rinfusa quadri di artisti diversi. Detto questo, il minimo della conservazione c'è, e non risulta che qualcuno l'abbia aperta davanti al compratore trovandoci dentro roba senza alcun valore. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :90960
    (90960, "Cute trading goods made of snow. Many of them feel comforted by their bland expressions and purchase them. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una graziosa merce da commercio fatta di neve. Quell'aria svagata consola, e pare che in molti la comprino per questo. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :91026
    (91026, "Very heavy traded goods made of felled fir trees decorated with many ornaments. It is said that people who cannot travel to Noyel buy it to celebrate at home. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio molto pesante: un abete abbattuto e carico di addobbi. La comprano, dicono, quelli che a Noyel non ci possono arrivare e vogliono festeggiare a casa loro. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :103715
    (103715, "A trade item consisting of several bundles of lifebuoy. They cannot be sold separately because they are difficult to sell. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio fatta di salvagenti legati in più mazzi. Sciolti diventano difficili da smerciare, e infatti non si vendono a uno a uno. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :103781
    (103781, "An intricately crafted trading item that is a joy to behold. It is heavy and should be handled with care. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio con dentro un congegno complicato, che diverte chi la guarda. È pesante, e a maneggiarla ci vuole attenzione. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :103847
    (103847, "A trading item that is nice to receive. It cannot be used because its value drops dramatically once it is opened. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio che fa piacere ricevere. Non si può usare: ad aprirla, il valore crolla. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :103913
    (103913, "Tuna is too huge to be eaten by individuals. It is mainly traded as a commodity. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Un tonno decisamente troppo grosso perché una persona sola se lo mangi. Si tratta soprattutto come merce da commercio. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :103979
    (103979, "Very heavy trading goods made of stone. Do not be reckless and let the grave carrier be buried in the grave. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio di pietra, molto pesante. Meglio non strafare: non sia mai che chi porta la tomba finisca sepolto sotto la tomba. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :104045
    (104045, "Mamboos that are too huge to be eaten by individuals. It is mainly traded as a commodity. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Un pesce luna decisamente troppo grosso perché una persona sola se lo mangi. Si tratta soprattutto come merce da commercio. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :104111
    (104111, "A carefully crafted trade item made of high quality wood. It is not available for use because of prior commitments. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio fatta con cura, in legno di qualità. Non si può usare: c'è già chi l'ha prenotata. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :104177
    (104177, "Tightly bound trade goods. You cannot use it because it would be very troublesome if it gets loose. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio legata stretta. Non si può usare: se si scioglie, sono guai. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :104243
    (104243, "A brightly colored, very heavy trade item. Although it produces sound, it cannot be used properly because it was only made for ornamental purposes. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio dai colori vivaci, molto pesante. Il suono lo fa, ma in fondo è roba costruita per far scena, e a usarla sul serio non si va da nessuna parte. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :104309
    (104309, "The trade goods are so polished that they mirror each other. Each one is handmade to a luxurious specification. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio lucidata al punto che ci si vede dentro. Ogni pezzo è fatto a mano, in versione di lusso. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :104375
    (104375, "Carefully wrapped trade goods. Once opened, it cannot be used because its value will decrease. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio impacchettata con cura. Non si può usare: ad aprirla, il valore cala. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

# 19 voci, 0 ambigue
}
