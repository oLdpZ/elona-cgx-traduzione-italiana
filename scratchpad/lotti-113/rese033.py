import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :42415
    (42415, 'A dart-firing tranquilizer repeater-rifle designed for targets weighing between 500 to 1000 kg. It uses specialized anesthetizing rounds to incapacitate large creatures, though the effect takes a moment to manifest. Overdosing can destroy nerve tissue, and its efficacy greatly diminishes for subjects outside the proper weight range. Utilizing a low-velocity gas propulsion system to minimize impact damage, the darts may fail to penetrate at longer distances, presenting a notable drawback. \\n#~Future Monster Damage Countermeasures~'):
        "Un fucile anestetico a ripetizione. Spara dardi speciali che fanno svenire i bersagli di peso fra i 500 e i 1000 chili, ma l'effetto ci mette un po' ad arrivare. Una dose eccessiva distrugge i nervi, e su chi supera il peso giusto l'effetto cala di molto. Per non ferire con l'urto il lancio è a gas e ha poca forza: da lontano il dardo non si pianta, ed è un altro difetto. \\n#~Difendersi dai Mostri, da Qui in Avanti~",

    # ---------------------------------------------------------- :42416
    (42416, 'No need for time-consuming individualized mixtures. Guaranteed penetration and impact within range. Consistent onset and follow-up shots possible. Unquestionably the best tranquilizer gun series today. \\n# ~words of Expert Marksman~'):
        "\\\"Non c'è la seccatura di cambiare la miscela caso per caso; dentro la gittata utile il colpo va a segno e si pianta, l'effetto arriva puntuale dopo un tempo fisso, e per giunta si spara a ripetizione. È senza dubbio la miglior serie di fucili anestetici che ci sia oggi\\\" \\n# ~Parole del Tiratore Anestetista~",

    # ---------------------------------------------------------- :42417
    (42417, "For eradication, isn't it quicker and more certain to just shoot them dead? \\n# ~words of Expert Huntsman~"):
        "\\\"Se lo scopo è liberarsene, non è più rapido e più sicuro sparargli e basta?\\\" \\n# ~Parole del Cacciatore Esperto~",

    # ---------------------------------------------------------- :42491
    (42491, 'A dart-firing tranquilizer repeater-rifle designed for targets weighing between 100 to 500 kg. It uses specialized anesthetizing rounds to incapacitate large creatures, though the effect takes a moment to manifest. Overdosing can destroy nerve tissue, and its efficacy greatly diminishes for subjects outside the proper weight range. Utilizing a low-velocity gas propulsion system to minimize impact damage, the darts may fail to penetrate at longer distances, presenting a notable drawback. \\n#~Future Monster Damage Countermeasures~'):
        "Un fucile anestetico a ripetizione. Spara dardi speciali che fanno svenire i bersagli di peso fra i 100 e i 500 chili, ma l'effetto ci mette un po' ad arrivare. Una dose eccessiva distrugge i nervi, e su chi supera il peso giusto l'effetto cala di molto. Per non ferire con l'urto il lancio è a gas e ha poca forza: da lontano il dardo non si pianta, ed è un altro difetto. \\n#~Difendersi dai Mostri, da Qui in Avanti~",

    # ---------------------------------------------------------- :42567
    (42567, 'A dart-firing tranquilizer repeater-rifle designed for targets weighing between 30 to 100 kg. It uses specialized anesthetizing rounds to incapacitate large creatures, though the effect takes a moment to manifest. Overdosing can destroy nerve tissue, and its efficacy greatly diminishes for subjects outside the proper weight range. Utilizing a low-velocity gas propulsion system to minimize impact damage, the darts may fail to penetrate at longer distances, presenting a notable drawback. \\n#~Future Monster Damage Countermeasures~'):
        "Un fucile anestetico a ripetizione. Spara dardi speciali che fanno svenire i bersagli di peso fra i 30 e i 100 chili, ma l'effetto ci mette un po' ad arrivare. Una dose eccessiva distrugge i nervi, e su chi supera il peso giusto l'effetto cala di molto. Per non ferire con l'urto il lancio è a gas e ha poca forza: da lontano il dardo non si pianta, ed è un altro difetto. \\n#~Difendersi dai Mostri, da Qui in Avanti~",

    # ---------------------------------------------------------- :42643
    (42643, 'A dart-firing tranquilizer repeater-rifle designed for targets weighing lower than 30 kg. It uses specialized anesthetizing rounds to incapacitate large creatures, though the effect takes a moment to manifest. Overdosing can destroy nerve tissue, and its efficacy greatly diminishes for subjects outside the proper weight range. Utilizing a low-velocity gas propulsion system to minimize impact damage, the darts may fail to penetrate at longer distances, presenting a notable drawback. \\n#~Future Monster Damage Countermeasures~'):
        "Un fucile anestetico a ripetizione. Spara dardi speciali che fanno svenire i bersagli di peso inferiore ai 30 chili, ma l'effetto ci mette un po' ad arrivare. Una dose eccessiva distrugge i nervi, e su chi supera il peso giusto l'effetto cala di molto. Per non ferire con l'urto il lancio è a gas e ha poca forza: da lontano il dardo non si pianta, ed è un altro difetto. \\n#~Difendersi dai Mostri, da Qui in Avanti~",

    # ---------------------------------------------------------- :42709
    (42709, "Wooden Chopsticks, crafted using off-cuts from boards. Can be used as a feint, reducing the opponent's power gauge and preventing them from using their own gauge-based attacks. May also be planted on the ground. \\n#~Supporting Roles in Kitchen~"):
        "Bacchette di legno, ricavate dagli scarti della lavorazione del legname. Usate contro chi si ha davanti servono a fingere un colpo: abbassano la barra di potenza del nemico e gli impediscono di usare le tecniche che la consumano. Si possono anche piantare per terra. \\n#~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :43240
    (43240, "An arcane device containing a magic stone. When a card of a creature is inserted into its lower case, the device emits a light from its upper mirror that transforms the user into the card's depicted creature. The effect lasts until the device is used again or the user dies, but it lacks a camouflage set-like mind-altering ability, so caution is advised. The device is called the Mimicry Mirror, based on the mimic's metamorphic mechanism.\\n#~Arcane Almanac~"):
        "Un oggetto magico con dentro una pietra magica. Mettendo una carta nella cassetta in basso, dallo specchio in alto esce un raggio che trasforma nell'aspetto della creatura sulla carta. L'effetto non si scioglie finché non lo si usa di nuovo o non si muore, ma attenzione: non confonde chi guarda come fa il set da travestimento. È costruito sul meccanismo con cui il mimic si mimetizza, e per questo lo chiamano anche specchio mimetico.\\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :44097
    (44097, 'Restraint devices developed in Eulderna. It was mainly used to take in experimental animals and felonious mages. In recent years, it has become an antique due to the spread of monster balls and domination magic that make them instantly obedient. It turns blue when activated, but to save money, levitation magic is not always activated and it only floats when the cage is moved. \\n#~ History of Bondage ~'):
        "Uno strumento di costrizione messo a punto a Eulderna. Serviva soprattutto a portare via gli animali da esperimento e i maghi colpevoli di reati gravi. Da qualche anno le sfere dei mostri e la magia del dominio, che rendono obbedienti sul momento, si sono diffuse, e questa gabbia è diventata un pezzo da antiquario. Accendendola diventa azzurra, ma per risparmiare la magia di levitazione non resta accesa: la gabbia fluttua solo quando la si sposta. \\n#~Storia degli Strumenti di Costrizione~",

    # ---------------------------------------------------------- :44163
    (44163, "A device that allows slaves to spin round and round to gain energy. Older versions were so heavy that they could only be spun by several people, but in recent years, in line with the boom in slave economy, types that are light enough to be spun by a single person have become mainstream. \\n#~ Let's Slavery - Today ~"):
        "Un arnese che ricava energia facendolo girare a uno schiavo. I modelli vecchi erano così pesanti che ci volevano più persone per muoverli, ma con la moda recente del risparmio di schiavi si è imposto il tipo leggero, che una persona sola riesce a far girare. \\n#~Gestire uno Schiavo, da Oggi~",

    # ---------------------------------------------------------- :44229
    (44229, "Equipment that makes slaves run to gain energy. Hamsters enjoy turning it and even if they are not hamsters, it is a healthy way to get exercise. So forcing them to run is probably not abusive. \\n#~ Let's Slavery - Today ~"):
        "Un arnese che ricava energia facendo correre uno schiavo. I criceti la fanno girare che sembrano divertirsi, e anche chi criceto non è ci trova un po' di moto e ci guadagna in salute. Quindi farci correre qualcuno a forza, probabilmente, non conta come maltrattamento. \\n#~Gestire uno Schiavo, da Oggi~",

    # ---------------------------------------------------------- :45481
    (45481, "A white orb said to contain the power of a demonic deity. Classified as a type of magic stone, but the method of production is vastly different. It consumes abyssal power to create simple magic traps at the user's current location. The strength of the trap depends on the Magic Device and Trapping skill of the user, as well as the depth of the Nefia. \\n#~Irva Fantasy Encyclopedia~"):
        "Una pietra bianca che, dicono, racchiude la forza di un dio demoniaco. Per classificazione è una pietra magica, ma il modo di farla è tutt'altro. Spende potere abissale e piazza una trappola magica semplice dove sta chi la usa. Si dice anche che con una dote particolare la si possa far scattare da lontano, ma finora nessuno l'ha dimostrato. La forza della trappola dipende da Dispositivi magici, da Disarmo trappole e anche dalla profondità del piano. \\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :45547
    (45547, 'Manifested experience of the strong, semi-embodied due to a confluence of various conditions. When used, they get an overwhelming inspiration as if an electricity shock has been applied.\\n#~Irva Fantasy Encyclopedia~'):
        "L'esperienza di chi è forte, mezza fatta materia per il concorso di più condizioni. A usarla si riceve un'intuizione travolgente, come una scarica di corrente.\\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :45549
    (45549, "It's a stone that gives you AP.  \\n#~ Identification Report <Item> Category~"):
        "Una pietra che dà AP.  \\n#~Rapporto di Identificazione: categoria <Oggetti>~",

    # ---------------------------------------------------------- :45613
    (45613, 'Conductive Cells infuesd with Coagulated Mana Clots, the creation process is extremelt painful. But its great for restoring magic circulations.\\n#~Irva Fantasy Encyclopedia~'):
        "Il conduttore magico dentro le cellule, addensato dal contraccolpo del mana. Quel che succede è in sostanza una distruzione di cellule, e il processo fa un male tremendo. A usarla il conduttore si ripara un poco e la magia torna a circolare meglio.\\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :45615
    (45615, "It's a stone that gives you magical powers (MP).  \\n#~ Identification Report <Item> Category~"):
        "Una pietra che dà poteri magici (MP).  \\n#~Rapporto di Identificazione: categoria <Oggetti>~",

    # ---------------------------------------------------------- :45679
    (45679, 'Solidified Ether Compound containing hardened fighting spirits, giving it a flame-like shape. It eases its users fatigue.\\n#~Irva Fantasy Encyclopedia~'):
        "Ardore di combattimento sprigionato di colpo, che si è combinato con l'etere e si è rappreso. Prende quella forma di fiamma, dicono, per come l'etere si distribuisce e per i sussulti dell'animo. È come un grumo di voglia di fare: a usarla la stanchezza si allenta e viene da credere di poter reggere ancora un po'.\\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :45681
    (45681, 'The stone provides endurance and stamina.  \\n#~ Identification Report <Item> Category~'):
        "La pietra dà costituzione e SP.  \\n#~Rapporto di Identificazione: categoria <Oggetti>~",

    # ---------------------------------------------------------- :45745
    (45745, "Drugs made to let user's immune system improvise, adapt, and overcome harsh environments. There were fake news which said it was made from fairy scales, but that's just untrustworthy Elea misinformation.\\n#~ Administration of Medicines ~"):
        "Un farmaco messo a punto per adattarsi agli ambienti più duri. Attivando le difese del corpo, dicono, dà resistenze senza bisogno di quel che si porta addosso. Ci fu un periodo in cui girava la fandonia che si ricavasse dalla polvere delle ali delle fate, e le fate a cui la strapparono, con le ali spelacchiate e rade, furono parecchie: ma sono cose di molto tempo fa.\\n#~Veleno o Medicina: Modo e Dose~",

    # ---------------------------------------------------------- :45747
    (45747, 'A tool to raise each resistance to a certain level. \\n#~ Identification Report <Item> Category~'):
        "Uno strumento che alza ogni resistenza fino a un certo livello. \\n#~Rapporto di Identificazione: categoria <Oggetti>~",

    # ---------------------------------------------------------- :45811
    (45811, "A medicine that permanently enhances the user's reflexes. However, it is not very effective without good equipment. \\n#~ Administration of Medicines ~"):
        "Un farmaco che rafforza per sempre la prontezza dei riflessi e alza l'evasione. Detto questo, se quel che si ha addosso è scadente non serve a molto: dà il meglio quando è roba buona ad amplificarlo. \\n#~Veleno o Medicina: Modo e Dose~",

    # ---------------------------------------------------------- :45813
    (45813, 'It is a tool to increase DV modifier. \\n#~ Identification Report <Item> Category~'):
        "È uno strumento che alza il modificatore DV. \\n#~Rapporto di Identificazione: categoria <Oggetti>~",

    # ---------------------------------------------------------- :45877
    (45877, "A medicine that permanently strengthens the skin's durability. However, it is not very effective without good equipment. \\n#~ Administration of Medicines ~"):
        "Un farmaco che rafforza per sempre la tenuta della pelle e alza la difesa. Detto questo, se quel che si ha addosso è scadente non serve a molto: dà il meglio quando è roba buona ad amplificarlo. \\n#~Veleno o Medicina: Modo e Dose~",

    # ---------------------------------------------------------- :45879
    (45879, 'It is a tool to increase PV modifier. \\n#~ Identification Report <Item> Category~'):
        "È uno strumento che alza il modificatore PV. \\n#~Rapporto di Identificazione: categoria <Oggetti>~",

    # ---------------------------------------------------------- :45944
    (45944, 'Parts that can be disassembled and reassembled to change their gimmick according to the situation, allowing transformation into a further six forms. It was originally intended as add-ons for large mechanoids, but was deemed too complex to be practical and ended up on the paper plan. A miniature model was also made to illustrate the mechanism, but only a few were able to transform it properly.\\n# ~Irva Fantasy Encyclopedia~\\n'):
        "Un pezzo che, smontato e rimontato, cambia prestazioni secondo la situazione: dalla forma a X si trasforma in altre sei. In origine era un accessorio per le grandi macchine da guerra, ma fu giudicato troppo complicato per servire a qualcosa e restò sulla carta. Ne fecero anche un modellino per spiegarne il meccanismo, e a trasformarlo come si deve riuscirono in pochi.\\n# ~Dizionario Fantastico di Irva~\\n",

    # ---------------------------------------------------------- :45945
    (45945, '\\"I can feel the romance in its transformation mechanics, the performance is not bad either, if only we have the budget..\\" \\n#~<Heinrich> the Armored General~'):
        "\\\"Le prestazioni non erano male e nella trasformazione ci sentivo del romanticismo: a dirla tutta il budget avrei voluto darglielo...\\\" \\n#~Parole di <Heinrich> il generale corazzato~",

    # ---------------------------------------------------------- :45946
    (45946, '\\"Regardless of it\'s performance, it\'s useless if we can\'t mass-produce nor maintain it.\\" \\n#~<Milis> Captain of the Special Forces~'):
        "\\\"Un pezzo che dà pena a produrre in serie e pena a mantenere, e che per giunta è pesante e ingombra, non va bene neanche se rende\\\" \\n#~Parole di <Milis> la comandante delle forze speciali~",

    # ---------------------------------------------------------- :46076
    (46076, 'A collection of special slime molds. It functions like a computer and moves freely with electrical signals. Former civilizations had the technology to download personalities and skills to this slime mold. Undead weapons composed of slime mold are said to have radically changed the warfare of that time.\\n#~a Glimpse of Lost Technology~'):
        "Un aggregato di muffe melmose particolari. Funziona come un calcolatore e si muove a piacere per segnali elettrici. La civiltà di un tempo sapeva perfino scaricare in questa muffa il carattere e le abilità di una persona. Le armi non morte fatte di muffa, dicono, cambiarono da cima a fondo le guerre di allora.\\n#~Tecnologia Perduta: un Barlume~",

    # ---------------------------------------------------------- :46142
    (46142, 'Dismembered Corpse, filled with constituent mucus. When attached to the subject, they can be moved at will, but modern technology will not allow them to be attached if they already have the relevant parts of the body due to rejection.\\n#~a Glimpse of Lost Technology~'):
        "Un cadavere fatto a pezzi e riempito di muffa melmosa. Attaccato a qualcuno si muove a piacere, ma con la tecnica di oggi, se quella parte del corpo già c'è, il rigetto impedisce l'innesto.\\n#~Tecnologia Perduta: un Barlume~",

    # ---------------------------------------------------------- :46144
    (46144, '\\"If you wanna grow an arm, would you prefer a beautiful one? a eldritch one? or a giant robot arm?! If you\'re going to do it, you WILL pay attention to the details! Customise your own and win the battle!\\" \\n# a Bored Necromancer'):
        "\\\"Anche solo per farti crescere un braccio: lo vuoi bello? deforme? meccanico? Già che lo monti, vorrai curare anche i pezzi piccoli! Componitelo come piace a te e vinci le tue battaglie!\\\" \\n#~Parole di un Negromante Annoiato~",

    # ---------------------------------------------------------- :46403
    (46403, 'An assortment of cork stoppers used as poton plugs. They look almost identical, but slightly different due to the manufacturer. Only a true cork maniac and tell the difference.\\n#~Thousands of pieces of Junk I love~'):
        "Un assortimento di tappi di sughero, di quelli che chiudono le bottiglie delle pozioni. Siccome c'era, chissà perché, un certo numero di clienti che voleva solo i tappi, è nato un prodotto che ricicla gli scarti. A vederli sono quasi tutti uguali per forma e misura, ma l'alchimista o l'officina che li ha fatti ci mette un segno tutto suo, e cambia anche il materiale: un appassionato, pare, li riconosce tutti.\\n#~Quel che Brilla nel Mucchio dei Rifiuti~",

    # ---------------------------------------------------------- :46404
    (46404, '\\"They are the same plugs, no?\\" \\n# a bewildered amateur'):
        "\\\"Ma non sono tutti uguali?!\\\" \\n#~Parole di un Profano Disorientato~",

    # ---------------------------------------------------------- :46405
    (46405, '\\"And that\'s why they call you an amateur!!\\" \\n# angry potio-plug nerd'):
        "\\\"Ecco perché i profani non vanno bene! Guarda meglio!\\\" \\n#~Parole di un Fissato in Piena Spiegazione~",

    # ---------------------------------------------------------- :46479
    (46479, "Large-calibre photon cannon. Therefore, despite the name 'bazooka', it does not fire rockets and is structurally classified as a recoilless gun. However, the common name for the rocket launcher bazooka also derives from the fact that it originally resembled the shape of a musical instrument bazooka, so it is probably fair to call it a bazooka regardless of its structure if its shape is similar to a bazooka.\\n# ~You Can Use it too! Excavated Weapons~"):
        "Un cannone a fotoni di grosso calibro. Per questo, pur chiamandosi bazooka, non spara razzi, e per costruzione rientra fra i cannoni senza rinculo. D'altra parte anche il bazooka lanciarazzi si chiama così perché somigliava allo strumento musicale che porta quel nome: se la forma è quella, forse è giusto chiamarlo bazooka comunque sia fatto.\\n# ~Puoi Usarle Anche Tu! Le Armi Riesumate~",

    # ---------------------------------------------------------- :46547
    (46547, 'Cards imbued with special magical powers. Once per turn: You can pay 10% of your MP, then activate 1 of these effects;\\n(1) If you control 5 or more \\"Card Spirit\\", change \\"Card Spirit - Diamond Eyes\\" you control into Attack Position, they gain 1 rank if cards of higher rank doesn\'t exists. \\n(2) If you control 4 or less \\"Card Spirit\\", summon random \\"Card Spirit\\" until you control 5 of them. \\"Card Spirit\\" summoned this way change into Defense Position after attacking.\\n#~Irva Fantasy Encyclopedia~'):
        "Una carta in cui è chiusa una magia particolare. Si attiva spendendo il 10% degli MP massimi. (1) Se sulla mappa ci sono cinque spiriti delle carte che non sono compagni, alza di un grado tutti gli spiriti del seme dell'oggetto e li mette in attacco; se però un altro spirito ha lo stesso seme e lo stesso grado, il grado torna com'era. Uno spirito che subisce danno passa in difesa. (2) Se sulla mappa gli spiriti che non sono compagni sono meno di cinque, ne evoca cinque di seme e grado a caso, in difesa, a un livello che dipende da Dispositivi magici e Memoria. Quando chi gioca lascia la mappa, gli spiriti che non sono compagni spariscono tutti.\\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :46615
    (46615, 'Cards imbued with special magical powers. Once per turn: You can pay 10% of your MP, then activate 1 of these effects;\\n(1) If you control 5 or more \\"Card Spirit\\", change \\"Card Spirit - Heart Witch\\" you control into Attack Position, they gain 1 rank if cards of higher rank doesn\'t exists. \\n(2) If you control 4 or less \\"Card Spirit\\", summon random \\"Card Spirit\\" until you control 5 of them. \\"Card Spirit\\" summoned this way change into Defense Position after attacking.\\n#~Irva Fantasy Encyclopedia~'):
        "Una carta in cui è chiusa una magia particolare. Si attiva spendendo il 10% degli MP massimi. (1) Se sulla mappa ci sono cinque spiriti delle carte che non sono compagni, alza di un grado tutti gli spiriti del seme dell'oggetto e li mette in attacco; se però un altro spirito ha lo stesso seme e lo stesso grado, il grado torna com'era. Uno spirito che subisce danno passa in difesa. (2) Se sulla mappa gli spiriti che non sono compagni sono meno di cinque, ne evoca cinque di seme e grado a caso, in difesa, a un livello che dipende da Dispositivi magici e Memoria. Quando chi gioca lascia la mappa, gli spiriti che non sono compagni spariscono tutti.\\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :46683
    (46683, 'Cards imbued with special magical powers. Once per turn: You can pay 10% of your MP, then activate 1 of these effects;\\n(1) If you control 5 or more \\"Card Spirit\\", change \\"Card Spirit - Club Feathers\\" you control into Attack Position, they gain 1 rank if cards of higher rank doesn\'t exists. \\n(2) If you control 4 or less \\"Card Spirit\\", summon random \\"Card Spirit\\" until you control 5 of them. \\"Card Spirit\\" summoned this way change into Defense Position after attacking.\\n#~Irva Fantasy Encyclopedia~'):
        "Una carta in cui è chiusa una magia particolare. Si attiva spendendo il 10% degli MP massimi. (1) Se sulla mappa ci sono cinque spiriti delle carte che non sono compagni, alza di un grado tutti gli spiriti del seme dell'oggetto e li mette in attacco; se però un altro spirito ha lo stesso seme e lo stesso grado, il grado torna com'era. Uno spirito che subisce danno passa in difesa. (2) Se sulla mappa gli spiriti che non sono compagni sono meno di cinque, ne evoca cinque di seme e grado a caso, in difesa, a un livello che dipende da Dispositivi magici e Memoria. Quando chi gioca lascia la mappa, gli spiriti che non sono compagni spariscono tutti.\\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :46751
    (46751, 'Cards imbued with special magical powers. Once per turn: You can pay 10% of your MP, then activate 1 of these effects;\\n(1) If you control 5 or more \\"Card Spirit\\", change \\"Card Spirit - Spade Warrior\\" you control into Attack Position, they gain 1 rank if cards of higher rank doesn\'t exists. \\n(2) If you control 4 or less \\"Card Spirit\\", summon random \\"Card Spirit\\" until you control 5 of them. \\"Card Spirit\\" summoned this way change into Defense Position after attacking.\\n#~Irva Fantasy Encyclopedia~'):
        "Una carta in cui è chiusa una magia particolare. Si attiva spendendo il 10% degli MP massimi. (1) Se sulla mappa ci sono cinque spiriti delle carte che non sono compagni, alza di un grado tutti gli spiriti del seme dell'oggetto e li mette in attacco; se però un altro spirito ha lo stesso seme e lo stesso grado, il grado torna com'era. Uno spirito che subisce danno passa in difesa. (2) Se sulla mappa gli spiriti che non sono compagni sono meno di cinque, ne evoca cinque di seme e grado a caso, in difesa, a un livello che dipende da Dispositivi magici e Memoria. Quando chi gioca lascia la mappa, gli spiriti che non sono compagni spariscono tutti.\\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :46818
    (46818, "A mysterious metallic body said to have come from outer space. Because it is beautiful and rare, it is treated as a precious metal by the rich. There is an urban legend that if you press it against your head it will change your personality because it emits weak psychic waves. I tried it on my friend becuase why not, but it only made him more aware of his own personality. So I wouldn't deny the probability that this effect is the result of Self-Hypnosis.\\n#~Embark! Occultists~"):
        "Un corpo metallico misterioso che, dicono, è caduto dal cielo. È bello e raro, e i ricchi lo trattano come un metallo prezioso. Emette onde mentali debolissime, e da qui la leggenda che premendoselo sulla testa cambi il carattere. L'ho provato su un conoscente per passare il tempo, e purtroppo è servito soltanto a fargli riconoscere il carattere che aveva. Che a uno molto suggestionabile venga l'autoipnosi, però, non lo escludo.\\n#~Avanti! Squadra Esploratrice dell'Occulto~",

    # ---------------------------------------------------------- :46884
    (46884, 'Amidst the mechanical civilisation ... the human body became more fragile with every generation due to the deteriorating environment. They were on the verge of extinction, but were spared by the development of technology to extend the human survival capabilities. Nanomachines that record and reproduce characteristics that are advantageous to survival, both organic and inorganic, and rewrite them by assimilating them into the cells of their offspring... these are the Survivability Extenders. Similar nanomachines, albeit with reduced function, remain in the cells of most modern organisms. This is largely responsible for the phenomenon that genes can be left behind across species.\\n#~Irva Fantasy Encyclopedia~'):
        "Metà dell'età delle macchine... l'ambiente peggiorava, e a ogni generazione il corpo umano si faceva più fragile. Si arrivò sull'orlo dell'estinzione, ma la scampammo grazie a una tecnica che allargava la capacità di sopravvivere. Nanomacchine che registrano e riproducono i tratti utili a sopravvivere, organici o no, e li riscrivono assimilandoli nelle cellule dei figli: ecco che cosa sono gli estensori di sopravvivenza. Con funzioni ridotte, nanomacchine simili restano nelle cellule di quasi tutti i viventi di oggi. Ed è proprio questo che c'entra molto col fenomeno per cui i geni passano oltre la specie.\\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :46885
    (46885, '\\"The cells of primordial life were not equipped with mitochondria, nanomachines nor magical conductors. So life evolved by incorporating things that gave it an extra edge at the cellular level.\\" \\n# a Zanan Researcher'):
        "\\\"Dicono che le cellule della vita primordiale non avessero né mitocondri né nanomacchine né conduttori magici. La vita si è evoluta prendendo dentro di sé le cose che le davano un vantaggio a livello di cellula\\\" \\n#~Parole di un Ricercatore di Zanan~",

    # ---------------------------------------------------------- :46886
    (46886, '\\"Many mechanical life forms were spawned with humans by these nanomachines. Of course, some were born of a completely different lineage of technology... but only the types that could eat, sleep, have the ability to heal and reproduce eventually survived. Maybe it\'s called convergent evolution.\\" \\n# Lead Developer <Dr. Gavela>'):
        "\\\"Fra le forme di vita meccaniche, molte sono nate da un essere umano proprio grazie a queste nanomacchine. Certo, alcune vengono da tecniche di tutt'altra linea... ma alla fine sono sopravvissuti solo i tipi che mangiano, dormono, sanno guarire e sanno riprodursi. Sarà quella che chiamano evoluzione convergente\\\" \\n#~Parole di <Gavela> l'ingegnere capo~",

    # ---------------------------------------------------------- :46950
    (46950, 'Amidst the mechanical civilisation ... the human body became more fragile with every generation due to the deteriorating environment. They were on the verge of extinction, but were spared by the development of technology to extend the human survival capabilities. Nanomachines that record and reproduce characteristics that are advantageous to survival, both organic and inorganic, and rewrite them by assimilating them into the cells of their offspring... these are the Survivability Extenders. Similar nanomachines, albeit with reduced function, remain in the cells of most modern organisms. This is largely responsible for the phenomenon that genes can be left behind across species.\\n#~Irva Fantasy Encyclopedia~'):
        "Metà dell'età delle macchine... l'ambiente peggiorava, e a ogni generazione il corpo umano si faceva più fragile. Si arrivò sull'orlo dell'estinzione, ma la scampammo grazie a una tecnica che allargava la capacità di sopravvivere. Nanomacchine che registrano e riproducono i tratti utili a sopravvivere, organici o no, e li riscrivono assimilandoli nelle cellule dei figli: ecco che cosa sono gli estensori di sopravvivenza. Con funzioni ridotte, nanomacchine simili restano nelle cellule di quasi tutti i viventi di oggi. Ed è proprio questo che c'entra molto col fenomeno per cui i geni passano oltre la specie.\\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :46951
    (46951, '\\"Hee hee hee... it was good that I created a synthetic beast by crossing many creatures with this tool, but it was too hard to raise them, so I guess I\'ll work steadily with synthetic magic after all!\\" \\n# a Evil Wizard'):
        "\\\"Ih ih ih... con questo arnese ho tirato fuori una bestia composita incrociando un mucchio di creature, e va bene, ma allevarla era una fatica impossibile: e allora niente, mi tocca tornare a sgobbare con la magia di sintesi!\\\" \\n#~Parole di un Mago Malvagio~",

    # ---------------------------------------------------------- :46952
    (46952, '\\"I\'ve heard the folklore that a child born with the traits of a beast left the human village because he couldn\'t control his wild nature. I guess some of the modern beastmen have their roots in that kind of thing.\\" \\n# Lead Developer <Dr. Gavela>'):
        "\\\"Ho sentito una tradizione che racconta di un bambino nato coi tratti di una bestia, che non riuscendo a tenere a freno la parte selvatica se ne andò lontano dagli uomini. Fra gli uomini-bestia di oggi ci sarà pure qualche stirpe che viene di lì\\\" \\n#~Parole di <Icolle> il biochimico~",

    # ---------------------------------------------------------- :47016
    (47016, 'A fibrous substance with miraculous powers. If there is a weapon that can incorporate it, it will help in its growth.\\n#~Blacksmithing History~'):
        "Una sostanza filamentosa che ospita una forza miracolosa. Da sola non serve a niente. Ma se esistesse un'arma capace di assorbirla, le gioverebbe per crescere.\\n#~La Storia delle Armi Raccontata da un Artigiano~",

    # ---------------------------------------------------------- :47083
    (47083, "A thin ring-like crystalline substance. Note that there are some infidels who sell screw-fastening parts similar to these, which have no effect, at exorbitant prices as electromagnetic wave countermeasures and items to prevent thought eavesdropping.This is a shameful practice that preys on people suffering from hallucinations and delusions, so don't say it's safe because it's a win-win situation, but repent quickly....Rest assured that the Anering contains sisterly energy waves and can be bathed in if cracked open.\\n#~Big Sister Energy Waves~"):
        "Un cristallo sottile a forma di anello. Attenzione: c'è gente senza scrupoli che vende rondelle da vite molto simili e del tutto inutili a prezzi da rapina, spacciandole per schermo contro le radiazioni e contro chi ti legge nel pensiero. È una vergogna, perché campa su chi soffre di allucinazioni e di manie: invece di dire che tanto ci guadagnano tutti e due, si pentano in fretta. ...L'anering, quello vero, l'Onda Sororale ce l'ha dentro davvero, e a spezzarlo ci si può fare il bagno: state tranquilli.\\n#~Il Testo Sacro dell'Onda Sororale~",

    # ---------------------------------------------------------- :47286
    (47286, 'A pair of garments. They are not intended to be used as weapons or as armour, but there are enthusiasts who collect even these. Note that the socks of people who are not in the habit of washing their feet smell quite bad. Incidentally, when washing socks, turning them inside out makes it easier to remove sebum stains from the parts in contact with the feet.\\n# ~Palmian Winter Fashion~'):
        "Un capo di vestiario che va a coppie. Non è pensato per essere usato come arma e non fa nemmeno da armatura, ma c'è chi colleziona perfino questo. Attenzione: i calzini di chi non ha l'abitudine di lavarsi i piedi puzzano parecchio. E comunque, a lavarli rovesciati viene via meglio l'unto della parte che stava a contatto col piede.\\n# ~Palmia: Collezione Autunno-Inverno~",

# 31 voci, 0 ambigue

    # ---------------------------------------------------------- :47287
    (47287, '\\"Wash my feet? Don\'t be ridiculous.\\"\\n~Bandit Leader~'):
        "\\\"Lavarmi i piedi? Ma neanche per sogno\\\"\\n~Parole del Capo dei Briganti~",

# 6 voci, 0 ambigue

    # ---------------------------------------------------------- :47288
    (47288, '\\"Wash my socks? Don\'t be ridiculous.\\"\\n~Socks Enthusiast~'):
        "\\\"Lavare i calzini? Ma neanche per sogno!!!!\\\"\\n~Parole di un Amante del Calzino Appena Sfilato~",

# 13 voci, 0 ambigue
}
