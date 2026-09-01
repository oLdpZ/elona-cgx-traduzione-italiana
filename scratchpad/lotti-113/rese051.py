import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :44031
    (44031, 'A deed gives the right to create a labor camp. It is left to the right holder to decide what to accommodate and what to do with it. \\n# ~Derphy Real Estate - Catalogue~'):
        "Un atto che dà il diritto di aprire un accampamento. Che cosa ci si tenga dentro e che cosa ci si faccia è lasciato a chi lo possiede. \\n# ~Immobiliare Derphy: Catalogo~",

    # ---------------------------------------------------------- :44300
    (44300, 'A scroll containing magic to harvest gold coins. It is best not to think too much about where the gold coins come from.\\n#~Arcane Alamanac~'):
        "Una pergamena che racchiude la magia di raccogliere monete d'oro. Da dove vengano quelle monete è meglio non pensarci troppo.\\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :44371
    (44371, 'Scrolls that pull hostiles to their surroundings. It is used to seek out and destroy enemies who are running and hiding. Be careful not to use it at the wrong time, as it can be dangerous to be surrounded.\\n#~Arcane Alamanac~'):
        "Una pergamena che tira gli ostili intorno a sé. Serve a stanare i nemici che scappano e si nascondono, e a farli fuori. Attenzione a non usarla nel momento sbagliato: ritrovarsi circondati è pericoloso.\\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :45060
    (45060, 'Certificate of ownership of a raft. It is very large, but relies on the buoyancy of the timber, so it has a limited carrying capacity. Although it has a modest sail, it is difficult to row against the waves unless you paddle hard.\\n# ~an Adventurer is You! Guide for Travels~'):
        "Un atto che dà la proprietà di una zattera. È enorme, ma galleggia solo per la spinta del legname, quindi carica poco. Una vela ce l'ha, tanto per dire, ma senza remare di buona lena andare contro le onde è dura.\\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :45061
    (45061, 'You can paint the ship by dyeing the deed. You can call a ship when you read it in a sea-facing town. Note that taxes are calculated on the most expensive ship used during the period. It is tremendously vulnerable to thunderstorms and ether winds, but if it sinks, you do not lose your rights if you have paid the insurance premium.\\n#~note for Travelers~'):
        "Tingendo l'atto si sceglie la vernice. Letto in una città sul mare, chiama la nave. Attenzione: le tasse si calcolano sulla nave più cara che hai usato nel periodo. È debolissima contro i temporali e i venti d'etere, ma se affonda, con l'assicurazione pagata il diritto non si perde.\\n#~Note al Manuale di Viaggio~",

    # ---------------------------------------------------------- :45131
    (45131, 'Certificates of ownership of a fishing boat. It is equipped with nets for catching fish. But be careful... you are the prey in front of a monster that can lightly sink your boat.\\n# ~an Adventurer is You! Guide for Travels~'):
        "Un atto che dà la proprietà di un peschereccio. Ha le reti da pesca, e i pesci si prendono tutti in un colpo. Ma meglio stare attenti... davanti a un mostro che affonda una barca con un buffetto, la preda sei tu.\\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :45132
    (45132, 'You can paint the ship by dyeing the deed. You can call a ship when you read it in a sea-facing town. Note that taxes are calculated on the most expensive ship used during the period. It is tremendously vulnerable to thunderstorms and ether winds, but if it sinks, you do not lose your rights if you have paid the insurance premium.\\n#~note for Travelers~'):
        "Tingendo l'atto si sceglie la vernice. Letto in una città sul mare, chiama la nave. Attenzione: le tasse si calcolano sulla nave più cara che hai usato nel periodo. È parecchio debole contro i temporali e i venti d'etere, ma se affonda, con l'assicurazione pagata il diritto non si perde.\\n#~Note al Manuale di Viaggio~",

    # ---------------------------------------------------------- :45202
    (45202, 'Deed of ownership of a pirate ship. Equipped with a antique cannon and capable of bombarding. The pirate flag flying large is filled with great romance. The problem may be that merchant ships encountered flee at once.\\n# ~an Adventurer is You! Guide for Travels~'):
        "Un atto che dà la proprietà di una nave pirata. Ha un cannone d'altri tempi e può bombardare. La bandiera nera issata bene in alto è piena di romanticismo. Il problema, semmai, è che i mercantili che incontri scappano a gambe levate.\\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :45273
    (45273, 'Certificate of ownership of a cruise ship. The facilities are very comfortable but do not come with even hospitable staff.\\n# ~an Adventurer is You! Guide for Travels~'):
        "Un atto che dà la proprietà di una nave da crociera. Le installazioni sono comodissime, ma il personale che ti serve non è compreso.\\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :45274
    (45274, 'You can paint the ship by dyeing the deed. You can call a ship when you read it in a sea-facing town. Note that taxes are calculated on the most expensive ship used during the period. It is tremendously vulnerable to thunderstorms and ether winds, but if it sinks, you do not lose your rights if you have paid the insurance premium.\\n#~note for Travelers~'):
        "Tingendo l'atto si sceglie la vernice. Letto in una città sul mare, chiama la nave. Attenzione: le tasse si calcolano sulla nave più cara che hai usato nel periodo. È abbastanza debole contro i temporali e i venti d'etere, ma se affonda, con l'assicurazione pagata il diritto non si perde.\\n#~Note al Manuale di Viaggio~",

    # ---------------------------------------------------------- :45344
    (45344, 'Certificate of ownership of a military ship. It is a restored relic of antiquity and it is not clear exactly how the ship was operated. It has some armour and armament and is not slowed by sea monsters, but it is no match for storms.\\n# ~an Adventurer is You! Guide for Travels~'):
        "Un atto che dà la proprietà di una nave da guerra. È un reperto antico rimesso in sesto, e come venisse usata non è tanto chiaro. Ha una corazza e un armamento discreti e non resta indietro nemmeno davanti ai mostri di mare, ma contro le tempeste non ce la fa.\\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :45345
    (45345, 'You can paint the ship by dyeing the deed. You can call a ship when you read it in a sea-facing town. Note that taxes are calculated on the most expensive ship used during the period. It is tremendously vulnerable to thunderstorms and ether winds, but if it sinks, you do not lose your rights if you have paid the insurance premium.\\n#~note for Travelers~'):
        "Tingendo l'atto si sceglie la vernice. Letto in una città sul mare, chiama la nave. Attenzione: le tasse si calcolano sulla nave più cara che hai usato nel periodo. È debole contro i temporali e i venti d'etere, ma se affonda, con l'assicurazione pagata il diritto non si perde.\\n#~Note al Manuale di Viaggio~",

    # ---------------------------------------------------------- :45415
    (45415, 'Certificate of ownership of a submarine. It is not aptly known as the ultimate stealth weapon and cannot be captured by other vessels or demons. It is equipped with torpedoes, but firing them will reveal your existence and position.\\n# ~an Adventurer is You! Guide for Travels~'):
        "Un atto che dà la proprietà di un sottomarino. Non lo chiamano l'arma furtiva definitiva per niente: né le altre navi né i mostri riescono a scovarlo. Ha i siluri, ma a lanciarli si scopre proprio quel che teneva nascosto, cioè di esserci e dove.\\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :51359
    (51359, 'Certificate of ownership of a land battleship. Originally excavated from the ruins of a mechanical civilization, apparently some junk dealer restored it on his own. This is a romantic piece of technology that even the richest person cannot afford to maintain. It may not have the performance of its heyday, but it is still a battleship, even if it is rotten. It can kick the crap out of wild monsters with a preemptive attack. The ship can carry quite heavy cargo, and even if it is too heavy, it does not slow down easily. It is also air-conditioned, so it is comfortable even in the desert. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Un atto che dà la proprietà di una corazzata terrestre. Pare l'abbiano dissotterrata dalle rovine dell'età delle macchine e che un rigattiere l'abbia rimessa a posto per conto suo. Un ammasso di romanticismo, che uno appena benestante non riesce a mantenere. Le prestazioni dei tempi d'oro non le ha più, ma corazzata resta: un mostro di passaggio lo spazza via col primo colpo. Porta carichi molto pesanti, e anche caricata troppo non rallenta facilmente. Ha pure l'aria condizionata, quindi nel deserto si sta comodi. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :51360
    (51360, "You can paint the vehicle by dyeing the deed. You can honk the horns with 's' key. If you want to travel on foot again, just read the same deed. Note that taxes are calculated by the most expensive vehicle used during the month. \\n#~note for Travelers~"):
        "Tingendo l'atto si sceglie la vernice. Col tasto s si fa suonare il clacson, ma non serve a niente. Se ti torna voglia di viaggiare a piedi, rileggi lo stesso tipo di atto. Attenzione: le tasse si calcolano sul mezzo più caro che hai usato nel periodo. \\n#~Note al Manuale di Viaggio~",

# 5 voci, 0 ambigue

    # ---------------------------------------------------------- :51361
    (51361, '\\"I\'m surprised they found this monster out of all things. Well, it wouldn\'t be a problem in this day and age.\\" \\n# ~words of an Expert on the Scene~'):
        "\\\"Proprio questo dovevano tirare fuori, fra tutte le cose. ...Vabbè, di questi tempi non sarà un problema.\\\" \\n# ~Parole di un Esperto che ha Visto la Scena~",

    # ---------------------------------------------------------- :51430
    (51430, 'Certificate of ownership of a magical locomotive. It runs on magically deployed rails, so its movement is unaffected even in snowfields. It can also tow rather heavy loads, and is not likely to slow down if the load is too heavy. However, it has a weak point in that its running is affected if the magic furnace is not activated, so it is necessary to keep putting in even a small amount of MP. Adjusting the power output and maintenance are also troublesome, making it a rare commodity even in Eulderna. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Un atto che dà la proprietà di una locomotiva che va a magia. Stende da sé rotaie magiche, quindi anche sulle nevi il viaggio non ne risente. Traina carichi piuttosto pesanti e, se sono troppo pesanti, non rallenta facilmente. Ha però un punto debole: se il forno magico non è acceso, la corsa ne soffre, e bisogna continuare a metterci MP, sia pure pochi. Regolare la potenza e farne la manutenzione è una noia, tanto che perfino a Eulderna è merce rara. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :51432
    (51432, '\\"I\'m a fOOking genius! My magical locomotive not being appreciated is a scheme of the Belm family!\\" \\n# ~words of a Self-proclaimed Genius Grimoire Technician~'):
        "\\\"Io sono un genio! Se il mio motore magico non lo apprezza nessuno è per un complotto di casa Bellum!\\\" \\n# ~Parole di un Sedicente Genio degli Arnesi Magici~",

    # ---------------------------------------------------------- :51501
    (51501, 'Certificate of ownership of a truck. Designed to travel reasonably fast on rough roads, but can go faster on well-maintained roads. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Un atto che dà la proprietà di un autocarro. È fatto per correre abbastanza anche sulle strade brutte, ma su una strada tenuta bene va più forte. Tingendo l'atto si sceglie la vernice. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :51572
    (51572, 'Certificate of ownership of a carriage. With horses specially trained for this purpose. The journey will be easier than on foot. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Un atto che dà la proprietà di una carrozza grande. Cavalli addestrati apposta compresi. Il viaggio andrà meglio che a piedi. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :52517
    (52517, "During the age of magical civilisation, this scroll was kept by a certain witch for the training of her young apprentices. It contains extremely clear descriptions of the witch's knowledge of witchcraft, which she had spent her entire life acquiring. The information is divided into easy-to-read sections, so that if you read one scroll, you will find different information in the next one. \\n#~Arcane Alamanac~"):
        "Una pergamena che, ai tempi della civiltà magica, una strega lasciò per crescere i suoi giovani discepoli. Ci sono scritte, in modo chiarissimo, le conoscenze magiche che si era guadagnata in una vita intera. Le notizie sono divise in parti che si leggono facilmente, e il congegno è questo: se ne leggi una, nella pergamena dopo ne esce un'altra. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :52519
    (52519, '\\"Power can bring fortune, or misfortune, depending on the way you use it... please don\'t forget that.\\" \\n# Witch\'s words, written in the corner'):
        "\\\"Qualunque potere, secondo come lo si usa, rende le persone felici o infelici... ti prego, non dimenticarlo.\\\" \\n#~Parole di una Strega Scritte in un Angolo~",

# 3 voci, 0 ambigue

    # ---------------------------------------------------------- :55211
    (55211, 'Needed to relocate your own properties. You must register by reading inside that property in advance, and they will relocate it inexpensively and with the exterior and interior intact. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Serve per spostare una tua proprietà che non sia la casa. Bisogna registrarla prima, leggendo l'atto dentro quella proprietà, e poi te la spostano a poco prezzo lasciando fuori e dentro come stanno. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :58396
    (58396, 'It was created to reduce the hassle of issuing and processing monthly invoices. By paying in advance in a large sum, regular invoices are not sent until they are exhausted. It has no effect on invoices that have already come in. \\n# ~Irva Revenue Services~'):
        "Fatto per alleggerire la fatica di emettere e sbrigare la fattura ogni mese. Pagando tutto in anticipo, finché quella somma non finisce le fatture ordinarie non arrivano. Su quelle già arrivate non ha effetto. \\n# ~Come Andare d'Accordo con le Tasse~",

    # ---------------------------------------------------------- :70197
    (70197, 'Deed for a large discarded ranch. Once a large monster ranch, now it is as good as trash. \\n# ~Derphy Real Estate - Unlisted~'):
        "L'atto di un grande allevamento abbandonato. Un tempo era un allevamento di mostri in grande stile, oggi è poco più che spazzatura. \\n# ~Immobiliare Derphy: Immobili Dismessi~",

    # ---------------------------------------------------------- :71028
    (71028, 'Needed to relocate your own home. It is pricey, but with a service that will move the exterior and interior of the house as is, even if it is a cave. \\n# ~an Adventurer is You! Guide for Travels~'):
        "L'atto che serve come pratica per traslocare. Costa caro, ma con il servizio compreso: se è una casa te la spostano com'è, dentro e fuori, foss'anche una caverna. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :81399
    (81399, 'A permit to explore the sanctuary. It is said that numerous treasures and thousands of corpses lie there. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una licenza che permette di esplorare il Vuoto. Si dice che là dentro dormano tesori a non finire e cadaveri a migliaia. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :81740
    (81740, 'A valuable scroll that allows the renaming of equipment by a different name. There are many occasions when it can be used, such as when you want to change your mood, or when your weapon asks you to rename it. \\n#~Arcane Alamanac~'):
        "Una pergamena preziosa, che permette di ribattezzare un'arma o un'armatura. Si usa nelle occasioni più diverse: quando si ha voglia di cambiare aria, o quando è l'arma stessa a chiederti di cambiarle nome. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :83411
    (83411, 'A deed gives the right to create a dungeon. Adventurers who have become addicted to dungeons are buying them to create their own dungeoning experience. \\n# ~Derphy Real Estate - Catalogue~'):
        "Un atto che dà il diritto di creare un sotterraneo in quel luogo. Pare lo comprino gli avventurieri diventati dipendenti dai sotterranei. \\n# ~Immobiliare Derphy: Catalogo~",

    # ---------------------------------------------------------- :83626
    (83626, 'A valuable scroll that nullifies mortal wounds for once by signing a contract with a temperamental Reaper. But be careful, the Reaper is whimsical. Be careful not to spoil the mood of the Reaper...\\n#~Arcane Alamanac~'):
        "Una pergamena preziosa che, stringendo un patto con la Morte, di suo capricciosa, annulla una volta sola una ferita mortale. Ma attenzione: la Morte è lunatica. Guardarsi bene dal guastarle l'umore...\\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :88346
    (88346, 'A scroll that invokes a gate leading to the outside. If used by mistake, it can be undone by reading it again. Naturally, two copies are consumed, but consider it a tuition fee. \\n#~Arcane Alamanac~'):
        "Una pergamena che chiama un portale verso l'esterno. Se la si usa per sbaglio, rileggendola si annulla. Ovviamente se ne consumano due, ma pazienza: consideralo il prezzo della lezione. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :88741
    (88741, "A precious scroll that can lighten the weight of a single item in one's possession. Some believe this scroll is rarely seen because it flies through the air like a migratory bird. \\n#~Arcane Alamanac~"):
        "Una pergamena preziosa che alleggerisce un oggetto fra quelli che porti. C'è chi sostiene che se ne vedano così poche perché questa pergamena vola per aria come un uccello migratore. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :89490
    (89490, 'A map showing the location of a hidden treasure buried somewhere in the world. The fragmentary information makes it extremely difficult to unearth, but you will feel a sense of accomplishment when you somehow find the location. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Una mappa con su il luogo di un tesoro nascosto, sepolto da qualche parte nel mondo. Le notizie sono a pezzi e tirarlo fuori è difficilissimo, ma quando in qualche modo trovi il posto provi una commozione che somiglia alla soddisfazione. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :89884
    (89884, 'A satanic paper that asks for money at a certain time of the year. It is no use burning it or otherwise making it disappear. They will come again in a month with their friends... \\n#~Arcane Alamanac~'):
        "Una carta diabolica che a scadenza fissa chiede soldi. Bruciarla o farla sparire non serve: quelli tornano un mese dopo, e con i compari... \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :92654
    (92654, "A deed gives the right to create a ranch. \\'Your new story begins here\\', is the big sales pitch on this deed. \\n# ~Derphy Real Estate - Catalogue~"):
        "Un atto che dà il diritto di creare un allevamento. Lo slogan scritto in grande su quest'atto dice: la tua nuova storia comincia qui. \\n# ~Immobiliare Derphy: Catalogo~",

    # ---------------------------------------------------------- :94246
    (94246, 'A scroll that sprinkles healing rain on surrounding allies. An tale still survives today of a healing goddess who, long ago, was said to have shyly bestowed it on the villagers in the face of drought. \\n#~Arcane Alamanac~'):
        "Una pergamena che fa cadere sui compagni intorno una pioggia che cura. Si racconta ancora oggi che tanto tempo fa una dea guaritrice, tutta vergognosa, l'abbia donata a dei contadini stremati dalla siccità. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :94670
    (94670, "Deed that gives you the right to build a warehouse. You can rent it when your hands start to get full. Don't forget the monthly maintenance fee. \\n# ~an Adventurer is You! Guide for Travels~"):
        "Un atto che dà il diritto di costruire un magazzino. Quando le mani cominciano a essere piene, conviene prenderne uno in affitto. E non dimenticare il canone mensile. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :94739
    (94739, 'A deed gives the right to create a farm. It would be nice to forget our adventures here and get some rest for a moment. \\n# ~Derphy Real Estate - Catalogue~'):
        "Un atto che dà il diritto di fare un campo. Non sarebbe male dimenticare qui l'avventura e prendersi un po' di riposo. \\n# ~Immobiliare Derphy: Catalogo~",

    # ---------------------------------------------------------- :95990
    (95990, 'A deed gives the right to create a shop. Once, an adventurer became so enthusiastic that he even sold his own equipment and became the owner of his own store. \\n# ~Derphy Real Estate - Catalogue~'):
        "Un atto che dà il diritto di aprire un negozio. Si racconta di un avventuriero che, presosi troppo dalla foga, finì per vendere anche il proprio equipaggiamento e restò lì a fare il bottegaio. \\n# ~Immobiliare Derphy: Catalogo~",

    # ---------------------------------------------------------- :96060
    (96060, "A deed gives the right to create a shop. The salary one gets from the government is meager, but it must be a collector's dream to show off one's own collection to the public. \\n# ~Derphy Real Estate - Catalogue~"):
        "Un atto che dà il diritto di costruire un museo. Lo stipendio che passa lo Stato è una miseria, ma mostrare al pubblico la collezione che ti sei fatto da solo è la gioia più grande per chi colleziona. \\n# ~Immobiliare Derphy: Catalogo~",

    # ---------------------------------------------------------- :96497
    (96497, 'A scroll that can infuse mana back into an item. The scroll is extremely difficult to handle and if not successfully read, causes the destruction of the item. \\n#~Arcane Alamanac~'):
        "Una pergamena capace di soffiare di nuovo il potere magico dentro un oggetto che l'ha perso. È difficilissima da maneggiare: se non si riesce a leggerla per bene, per l'oggetto è la fine. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :96782
    (96782, 'A deed entitling the holder to receive the contents of the bag of mementos. The final receipt of the memento is accepted by reading this. \\n# ~Book for the Dying Ones~'):
        "Un atto che dà il diritto di ricevere quel che c'è nella borsa dei ricordi. Leggendolo, la consegna definitiva del ricordo viene accettata. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :96915
    (96915, 'Scrolls that, when read, clothe the armour in a golden gown. They are stronger than normal ones and are said to be powerful beyond the limits of their performance. \\n#~Arcane Alamanac~'):
        "Una pergamena che, letta, veste l'armatura di un abito d'oro. È più forte di quelle normali, e si dice che porti la forza oltre il limite di ciò che l'armatura può dare. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :96986
    (96986, 'Scrolls that, when read, clothe the armour in a golden gown. Supposedly, this increases the strength of the armour and makes it one step stronger. \\n#~Arcane Alamanac~'):
        "Una pergamena che, letta, veste l'armatura di un abito d'oro. Così l'armatura diventa più robusta, e si dice che salga di un gradino. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :97057
    (97057, 'Scrolls that, when read, wraps the weapon in a golden gown. They are stronger than normal ones and are said to be powerful beyond the limits of their performance. \\n#~Arcane Alamanac~'):
        "Una pergamena che, letta, avvolge l'arma in un abito d'oro. È più forte di quelle normali, e si dice che porti la forza oltre il limite di ciò che l'arma può dare. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :97128
    (97128, 'Scrolls that, when read, wraps the weapon in a golden gown. Supposedly, this increases the strength of the armour and makes it one step stronger. \\n#~Arcane Alamanac~'):
        "Una pergamena che, letta, avvolge l'arma in un abito d'oro. Così l'arma diventa più robusta, e si dice che salga di un gradino. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :97396
    (97396, "Scrolls that change the material. They can easily transform the material into a more powerful and valuable one. Don't ask how the scrolls interact with the material, all those things are done by 'magic'. \\n#~Arcane Alamanac~"):
        "Una pergamena che cambia il materiale. Tende a cambiarlo in uno più forte e più prezioso, ma come la pergamena agisca sul materiale non bisogna chiederlo: sono tutte cose che fa la magia. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :97467
    (97467, 'Scrolls that change the material. Needless to say, most alchemists use these scrolls as a springboard for their own research. \\n#~Arcane Alamanac~'):
        "Una pergamena che cambia il materiale. Va da sé che quasi tutti gli alchimisti si servano di questa pergamena come trampolino per le proprie ricerche. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :97538
    (97538, 'Scrolls that change the material. Most of them change to inferior materials, but some adventurers are said to take advantage of this. \\n#~Arcane Alamanac~'):
        "Una pergamena che cambia il materiale. Di solito lo cambia in uno scadente, ma pare che certi avventurieri sappiano rigirare la cosa a proprio vantaggio. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :99025
    (99025, "Scrolls that summons helpful companions come out of nowhere. If you look closely, you can see small letters in the corner of the scroll that say 'extra charges apply'. \\n#~Arcane Alamanac~"):
        "Una pergamena da cui arriva, non si sa da dove, un compagno che dà una mano. A guardare bene, in un angolo della pergamena ci sarebbe scritto in piccolo: costi a parte. O almeno così si dice. \\n#~Compendio Completo degli Oggetti Magici~",

# 42 voci, 0 ambigue
}
