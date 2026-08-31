import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :90137
    (90137, 'A board with various drawings detailed on it. It is an excellent tool to use on buildings you own to rearrange your home without wasting muscle power. \\n# ~Supporting Roles on the Streets~'):
        "Una tavola con sopra disegnati per esteso vari progetti. Usata in un edificio di tua proprietà, cambia la disposizione della casa senza sprecare forza nelle braccia: un bell'arnese. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :91909
    (91909, 'People have always lived with fire. With fire we got heat to warm the space, and with fire we got light to illuminate the night. Now you are holding the spark of civilization! \\n# ~an Adventurer is You! Guide for Travels~'):
        "In ogni tempo l'uomo è stato insieme al fuoco. Dal fuoco il calore che scalda lo spazio, dal fuoco la luce che rischiara la notte. E ora la scintilla della civiltà è nelle tue mani! \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :91911
    (91911, '\\"Just by clutching it in one hand, your Nefia life will become much more adventurous. You should definitely try this excellent light-up tool.\\" \\n# ~notice of good store of Vernis~'):
        "\\\"Basta stringerla in una mano e la tua vita nelle Nefia diventa molto più da avventuriero. Prova anche tu questo ottimo arnese per far luce!\\\" \\n# ~Reclame Affissa al Bazar di Vernis~",

    # ---------------------------------------------------------- :92252
    (92252, 'A box that allows you to put a certain amount of money in it every time you use it and keep it. The fact that it gets a little heavier each time it is used is surely due to the happiness of storing it. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una cassetta dove a ogni uso si mette dentro una certa somma e la si tiene da parte. Che a ogni uso si faccia un po' più pesante sarà di sicuro merito della felicità di mettere da parte. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :92389
    (92389, 'Disks containing videos. The use of these disks can bring back past memories in the form of videos, but unfortunately all other techniques have been forgotten today except for their use. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un disco con dentro delle immagini. Usandolo si richiamano in forma di filmato le memorie del passato, ma purtroppo oggi, di tutta quella tecnica, non è rimasto che il modo di usarlo. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :92934
    (92934, 'Blankets developed against icy blades of wind. Although it completely prevents freezing damage to the potion, overconfidence is not advised, as there are limits to what can be achieved. \\n# ~Palmian Winter Fashion~'):
        "Una coperta messa a punto contro le lame di ghiaccio che sferzano. Impedisce del tutto che il gelo rovini le pozioni, ma tutto ha un limite e fidarsi troppo è vietato. \\n# ~Palmia: Collezione Autunno-Inverno~",

    # ---------------------------------------------------------- :92998
    (92998, 'Blankets developed against an approaching flame. It completely prevents the destruction of items due to combustion, but it has its limitations and one should not be overconfident. \\n# ~Palmian Summer Fashion~'):
        "Una coperta messa a punto contro le fiamme che avanzano. Impedisce del tutto che gli oggetti, bruciando, si riducano in carbone, ma tutto ha un limite e fidarsi troppo è vietato. \\n# ~Palmia: Collezione Primavera-Estate~",

    # ---------------------------------------------------------- :93358
    (93358, 'An indispensable machine for buying and selling money and goods. For security purposes, the system allows only one person registered to use it. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~'):
        "Una macchina indispensabile quando si comprano e si vendono denaro e merci. Per sicurezza il sistema la rende usabile a una sola persona, quella registrata. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :93360
    (93360, 'This machine is essential in assigning personnel. It is here that you can change the assignment of your fellow workers. \\"If you lose it by accident, don\'t worry. Everything is available at the Palmia Embassy, the keystone of the economy.\\" \\n# ~Tyris Armor Compendium, page of advertisements~'):
        "Una macchina indispensabile per assegnare la gente. Qui si cambia l'incarico dei compagni. \\\"Se per un caso sfortunato la perdete, state tranquilli: all'ambasciata di Palmia, cardine dell'economia, si trova tutto.\\\" \\n# ~Grande Compendio delle Armi di Tyris: le Reclame~",

    # ---------------------------------------------------------- :93823
    (93823, 'A simple shelter that can be set up in an emergency. After the crisis has passed, it can be picked up and reused. \\n# ~Daily Necessities for the Home~'):
        "Un rifugio semplice che si può montare in caso di bisogno. Passato il pericolo lo si raccoglie e si riusa: un arnese buono a tutto. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :94601
    (94601, 'A disc containing music. These discs play a specific enclosed song when used, but unfortunately, the technology to do anything but play them is lost to the present day.\\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un disco con dentro della musica. Usandolo suona il brano che ci hanno chiuso, ma purtroppo oggi, di tutta quella tecnica, non è rimasto che il modo di usarlo.\\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :99091
    (99091, "Medical equipment that, when used, determines a person's physical condition. Everyone may have played doctor when they were a child, but sensible adventurers should never use it for anything nefarious. \\n# ~an Adventurer is You! Guide for Travels~"):
        "Un arnese da medico che, a usarlo, dice sul momento come sta il corpo. Da bambini tutti avranno giocato al dottore, ma un avventuriero di buon senso non lo adoperi mai per fini poco puliti. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :102458
    (102458, 'A simple bedding mainly intended for sleeping outdoors. When you are sleepy, you can get temporary peace of mind by being completely enclosed in this bedding, cut off from the outside world. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Un giaciglio semplice, pensato soprattutto per dormire all'aperto. Quando hai sonno ti ci infili tutto e resti chiuso fuori dal mondo: per un poco è pace. \\n#~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :104791
    (104791, 'Basic tool necessary for jewelry processing. Naturally, it cannot be handled without skill. \\n# ~Daily Necessities for the Home~'):
        "L'attrezzo di base che serve per lavorare le gemme. Va da sé che senza l'abilità non si può adoperare. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :108457
    (108457, 'Tool needed to catch fish. On holidays, the docks of Port Kapul are said to be filled with anglers, or even tourists, who are struggling alone, clutching their gear in their hands, dreaming of catching a big fish. \\n# ~Daily Necessities for the Home~'):
        "L'arnese che serve per pescare. Nei giorni di festa, sulla banchina di Port Kapul, si dice che parecchi pescatori, anzi turisti, se lo stringano in mano sognando di tirare su un pesce grosso, e combattano da soli la loro battaglia. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :108459
    (108459, '\\"To catch fish, the bait is the most important. The rest is easy, just swing the rod, wait, and profit. And yes, of course, if you don\'t have the skill, you\'d be just waiting and waiting.\\" \\n# ~words of a fisherman proud of his catch~'):
        "\\\"Per pescare conta l'esca, certo, ma più di tutto conta questo. Il resto è facile: butti la lenza e stai fermo ad aspettare. Ah, e va da sé: se l'abilità non ce l'hai, aspetti e basta.\\\" \\n# ~Parole di un Pescatore Fiero della Sua Preda~",

    # ---------------------------------------------------------- :114077
    (114077, 'Small cooking set that can do a whole range of cooking. However, its only advantage is its light weight, so if you want to become a professional, we recommend you buy more expensive cooking equipment. \\n# ~Supporting Roles in Kitchen~'):
        "Un piccolo set da cucina con cui, solo a usarlo, si prepara un po' di tutto. Detto questo, il suo unico pregio è quanto pesa poco: se punti a diventare un professionista, meglio comprare attrezzi da cucina più cari. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :114141
    (114141, 'It is not only a cooking utensil, but also serves as a lightsource, and even produces the gentle sound of flames just by placing it on the table. However, from the standpoint of a cooking utensil, it is a little underpowered, and is often used as interior decoration. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Non serve solo da attrezzo da cucina: fa anche luce, e basta posarlo perché aggiunga il suono gentile della fiamma. Tre cose in una. Come attrezzo da cucina però è un po' debole, e finisce che lo si tiene per arredo. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :116346
    (116346, 'This revolutionary cooking utensil allows you to throw ingredients into it and cook a dish just by using it. However, as one might expect, it is difficult to make complicated dishes since the ingredients are simply thrown into the cooker. \\n# ~Supporting Roles in Kitchen~'):
        "Un attrezzo da cucina che cambia tutto: ci butti dentro gli ingredienti, lo usi, e il piatto è fatto. Però, come c'era da aspettarsi, siccome li butti dentro e basta, i piatti complicati vengono male. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :116603
    (116603, 'A strong rope that will not come undone no matter how hard it is pulled. It is a tool to be used for objects, so it is not suitable for attaching to people. \\n# ~Battles, Dragons, Swords and Magic~'):
        "Una corda forte che, per quanto la si tiri, non si sfilaccia. È un arnese da usare sulle cose, quindi per legarci una persona pare che non vada bene. \\n# ~Cose Lunghe Fatte per Essere Avvolte~",

    # ---------------------------------------------------------- :116605
    (116605, '\\"I said, \'Hey, hey, hey, what are you mad about?\' I answered as I was asked. I don\'t think I deserve your thanks or your abuse. And I didn\'t just say, \'Use it.\' I said, \'It\'s one of the many options you have to try.\'\\" \\n# ~<Lomias> the messenger from Vindale~'):
        "\\\"Ehi, ehi, che cos'è che ti fa arrabbiare? Io ho risposto a quel che mi è stato chiesto. Semmai mi si dovrebbe ringraziare; prendermi a male parole mi pare fuori luogo. E poi io non ho detto di usarla: ho detto che provare è una delle tante scelte che hai.\\\" \\n# ~Parole di <Lomias> il messaggero di Vindale~",

# 4 voci, 0 ambigue

    # ---------------------------------------------------------- :120505
    (120505, 'Basic tool necessary for carpentry. Naturally, it cannot be handled without skill. \\n# ~Daily Necessities for the Home~'):
        "L'attrezzo di base che serve per i lavori di falegname. Va da sé che senza l'abilità non si può adoperare. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :120571
    (120571, 'Basic tool necessary for tailoring. Naturally, it cannot be handled without skill. \\n# ~Daily Necessities for the Home~'):
        "Il set di base che serve per cucire. Va da sé che senza l'abilità non si può adoperare. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :121829
    (121829, 'A complete set of tools necessary for painting. If you have an artistic mind, it would be a good idea to use it. If you have a good mind for painting, you should try it. \\n# ~Gifts that I am Happy to Receive~'):
        "Un insieme con tutti gli arnesi che servono per dipingere. Se hai mano per il disegno, provalo. Sempre che tu ce l'abbia, la mano. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :122679
    (122679, 'This is the basic kit required to perform alchemy. Naturally, it cannot be handled without skill. \\n# ~Arcane Almanac~'):
        "Il kit di base che serve a fare alchimia. Va da sé che senza l'abilità non si può adoperare. \\n# ~Compendio Completo degli Oggetti Magici~",

# 21 voci, 0 ambigue
}
