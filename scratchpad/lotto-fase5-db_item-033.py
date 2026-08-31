# -*- coding: utf-8 -*-
"""114a - Lotto 033 di `db_item.hsp`: GLI ATTREZZI, prima parte.

`FILTER_ITEM_TOOL`, righe 0-48.000: **50 righe** su 31 oggetti — 31 dell'indice
0, 6 dell'indice 1 e 13 dell'indice 2. E' il primo lotto del corpo fuori dal
mobilio, e non somiglia a nessuno dei precedenti: sono oggetti **aggiunti dal
CGX**, con prosa lunga, tecnica, e piena di termini che il gioco usa altrove.

### ⭐⭐⭐ QUI UNA RESA NON COPRE UNA RIGA SOLA

I quattro fucili anestetici (`:42415`, `:42491`, `:42567`, `:42643`) hanno
descrizioni di indice 0 diverse solo nella **fascia di peso**, ma le loro righe
di indice 1 e 2 sono **identiche parola per parola in tutti e quattro**: una
firma sola, `:42416` e `:42417`, che copre otto righe del sorgente. E' il
moltiplicatore che il mobilio non aveva e il cibo si', e vuol dire che
`applica` sale di **piu'** di 50.

⚠️ Il numero atteso, quindi, **non e' il numero delle rese**: si guarda quanto
sale `applica` e si controlla che sia coerente con le firme gemelle, non che
faccia 50.

### ⭐⭐⭐ LE QUATTRO CARTE HANNO IL GIAPPONESE IDENTICO, E L'INGLESE NO

`:46547`, `:46615`, `:46683` e `:46751` — i quattro «signori» di quadri, cuori,
fiori e picche — hanno **lo stesso identico giapponese**, che dice «tutti gli
spiriti delle carte **corrispondenti al seme dell'oggetto**». L'inglese invece
nomina lo spirito preciso di ciascun seme (Diamond Eyes, Heart Witch, Club
Feathers, Spade Warrior).

Le quattro rese sono **identiche**, come il giapponese: il seme il giocatore lo
legge nel **nome** della carta, che e' gia' reso («signore di quadri»…), e una
resa generica e' vera per tutt'e quattro. ⓘ Cosi' `_coerenza.py` — che si
accende quando lo stesso giapponese ha rese diverse — resta a zero senza che si
sia dovuto forzare niente.

### ⭐⭐⭐ IL CODICE SMENTISCE IL GIAPPONESE, E VINCE IL CODICE

Il giapponese di `:46950` (l'estensore di sopravvivenza Y) comincia con
**（未実装）**, «non implementato». Ma l'oggetto **funziona**:
`action.hsp:8721` ha il suo ramo di effetto e `:8782` mette
`CDATA_PREGNANCY_MALE_CHILD`, esattamente come la X fa con
`CDATA_PREGNANCY_FEMALE_CHILD`. Il giapponese e' fermo a una versione vecchia.

E' la quinta fonte della 110a — *il codice vince quando il giapponese e' in
disaccordo su un fatto di gioco* — e qui non e' un'ambiguita': e' una riga che
direbbe al giocatore di non usare un oggetto che funziona. Il marcatore non si
rende, e le due rese restano identiche come lo sono i due inglesi.

### ⭐⭐ L'INGLESE SBAGLIA UN ATTRIBUTO, E TAGLIA TRE VOLTE

- **`:46952` e' attribuito alla persona SBAGLIATA.** L'inglese firma
  `# Lead Developer <Dr. Gavela>`, la stessa firma di `:46886`; il giapponese
  dice 生化学者『イコール』, **il biochimico <Icolle>**. Se ne accorge
  `lotti-113/_code.py`, che passa dal giapponese e non dall'inglese.
- **`:46403` cita il LIBRO sbagliato.** L'inglese scrive
  `#~Thousands of pieces of Junk I love~`, il giapponese `～ゴミの山に光るもの～`
  — sono due libri diversi, e la coda giusta e'
  `~Quel che Brilla nel Mucchio dei Rifiuti~`. Stessa rete, stessa ragione.
- **`:45745` (il Res upper) butta via che fine facevano le fate**: 鱗粉を奪われ
  翅がハゲてスカスカになる妖精が続出した — a molte fate strapparono la polvere
  delle ali, e le ali restarono spelacchiate. L'inglese al suo posto **aggiunge**
  una «Elea misinformation» che il giapponese non ha.
- **`:47016` (la fibra stellare) perde これだけでは何の役にも立たない**, «da sola
  non serve a niente», che e' la frase che dice a che cosa serve l'oggetto.
- **`:45811` e `:45877` perdono la terza frase**, quella che dice che il farmaco
  da' il meglio quando e' un buon equipaggiamento ad amplificarlo.

### ⚠️⚠️ LA SPAZIATURA PRIMA DEL `\\n` QUI NON E' UNIFORME

Nel mobilio era quasi sempre uno spazio. Qui l'inglese ne mette **uno**, **zero**
o **due** (`:45549`, `:45615`, `:45681`), e `:45944` porta perfino un `\\n` **in
coda** che nessun'altra riga del lotto ha. Ogni riga copia il suo, verbatim.

### ⚠️⚠️ DUE RIGHE HANNO PERSO IL `#` DAVANTI ALLA FONTE, E NON GLIELO RIMETTIAMO

`:47287` e `:47288` (le due battute sui calzini) hanno in giapponese
`#～…の言葉～` col cancelletto, e in inglese `~Bandit Leader~` **senza**. Senza
il `#` il gioco non la disegna come riga-fonte (`command.hsp:16758`): cade
nell'impaginatore e va a sinistra.

Il `#` **non** si aggiunge, per due ragioni:

1. il cancello di `_112-corpo-descrizioni.py` conta i `#` **contro l'inglese**
   (`en.count('#') != it.count('#')`), e aggiungerlo lo accenderebbe su due
   righe;
2. e' un difetto di **monte**, come i 110 inglesi oltre il tetto dell'indice 3:
   non si contano contro di noi e non si riparano di nascosto.

ⓘ Per questo `lotti-113/_code.py` esce con **1** su questo lotto, dicendo «2
righe senza resa in tabella»: cerca il segmento che comincia per `#`, e qui non
c'e'. Non e' un guasto della rete — e' la rete che vede il difetto di monte. Le
due code sono state scritte a mano nella forma della famiglia, cosi' che se
l'upstream un giorno rimette il `#` il testo sia gia' giusto.

### ⭐ I TERMINI CERCATI A MANO

    カード精霊   -> spiriti delle carte    (`db_creature.hsp`, i quattro semi)
    深淵魔力     -> potere abissale        (`action.hsp`)
    魔道具(abilita') -> Dispositivi magici (`skill.hsp`)
    暗記         -> Memoria                (`skill.hsp`)
    罠の知識     -> Disarmo trappole       (`skill.hsp`)
    ポーショマン -> potioman               (`chat.hsp`)
    モンスターボール -> sfera dei mostri   (`chat.hsp`)
    変装セット   -> set da travestimento   (`db_item.hsp`)
    姉波動       -> Onda Sororale          (`chat.hsp`)
    魔石         -> pietra magica          (`chat.hsp`)
    パワーゲージ -> barra di potenza       (`chat.hsp`)
    防御態勢     -> difesa                 (`text.hsp`)
    エウダーナ / ザナン -> Eulderna / Zanan  (nomi propri)

⚠️ **魔導体 non e' nel dizionario**: e' l'organo che conduce la magia, e
l'inglese lo chiama ora «magical conductors» ora «Conductive Cells». Reso
**«conduttore magico»**, e la scelta va nel glossario.
⚠️ **電磁波 non e' nel dizionario**, e «elettromagnetiche» e' di **17
caratteri**: sopra la soglia dei 14, l'impaginatore la spezzerebbe. Reso
«radiazioni», che nel contesto — la reclame truffaldina contro le onde e la
lettura del pensiero — dice la stessa cosa e ci sta.
"""
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
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-033.jsonl'
RIGHE = {
    42415, 42416, 42417, 42491, 42567, 42643, 42709, 43240, 44097, 44163,
    44229, 45481, 45547, 45549, 45613, 45615, 45679, 45681, 45745, 45747,
    45811, 45813, 45877, 45879, 45944, 45945, 45946, 46076, 46142, 46144,
    46403, 46404, 46405, 46479, 46547, 46615, 46683, 46751, 46818, 46884,
    46885, 46886, 46950, 46951, 46952, 47016, 47083, 47286, 47287, 47288,
}
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_item.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_107-daitem.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if v['riga'] in RIGHE]
# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006), col `//` (100a) o dentro un
# blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
# ⚠️ Lo strumento, non lo scratch: `strumenti/commenti.py` e' la stessa funzione
# di `scratchpad/commenti-blocco.py` ma con dei test, e dalla 100a sa anche del
# commento di riga `//`.
from strumenti import commenti as _cb
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    testo = sorgente[riga - 1]
    return (testo.lstrip().startswith(';')
            or _cb.lang_spenta_da_barre(testo)
            or riga in SPENTE)


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _testa = sorgente[_righe[0] - 1]
        if _testa.lstrip().startswith(';'):
            _come = "e' commentata nel sorgente"
        elif _cb.lang_spenta_da_barre(_testa):
            _come = "e' spenta da un commento `//`"
        else:
            _come = 'sta dentro un commento di BLOCCO'
        errori.append(f"rete 6: riga {v['riga']} {_come}, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"\U0001f4a1 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `command.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
        if attese != trovate:
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[chiave(v)]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
