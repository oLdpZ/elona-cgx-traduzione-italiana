# -*- coding: utf-8 -*-
"""119a - Lotto 051 di `db_item.hsp`: LE PERGAMENE E GLI ATTI, prima meta'.

`FILTER_ITEM_SCROLL`, righe da `:44031` a `:99025`: **50 righe** su 43 oggetti —
42 dell'indice 0, **5 dell'indice 1** e 3 dell'indice 2. La categoria era intatta
(73 da fare su 73): dopo questo lotto ne restano **23**, e chiudono il 052.

⚠️⚠️ Previsione di `applica`: **+56** per 50 rese. Il moltiplicatore c'e', ed e'
la cosa che spiega tutto il lotto: quattro firme coprono sei righe in piu'.

### ⭐⭐⭐ LA NOTA DELLA NAVE E' UNA SCALA A QUATTRO GRADINI, E L'INGLESE LA APPIATTISCE

Sei mezzi di mare — zattera, peschereccio, nave pirata, nave da crociera, nave
da guerra, sottomarino — portano nell'indice 1 la stessa nota del manuale di
viaggio. In **inglese sono sei stringhe identiche**, tutte con «It is
tremendously vulnerable to thunderstorms and ether winds». In giapponese cambia
**una parola**, ed e' un fatto di gioco:

    :45061  zattera                   雷雨やエーテル風に **とてつもなく弱い**
    :45132  peschereccio, nave pirata                  **かなり弱い**
    :45274  nave da crociera                           **結構弱い**
    :45345  nave da guerra, sottomarino                **弱い**

Quattro gradini di fragilita', dal legno che affonda al sottomarino. La resa
tiene la scala con quattro avverbi e una parola sola, come la scala della
gittata della 110a: **debolissima / parecchio debole / abbastanza debole /
debole**.

⭐ **E la scala e' anche la ragione delle gemelle.** `estrai.firma()` e'
`sha1(giapponese + \\x00 + inglese)`: dove il giapponese coincide, coincide la
firma. Peschereccio e nave pirata dicono tutt'e due かなり弱い, nave da guerra e
sottomarino tutt'e due 弱い — quindi **due rese coprono quattro righe**. Non e'
un caso e non e' un difetto: e' il modo in cui l'autore ha raggruppato i mezzi
per fragilita'.

ⓘ Chi avesse reso le sei note dall'inglese avrebbe scritto sei volte
«debolissima», cioe' avrebbe cancellato una scala che il gioco usa. Nessuna rete
poteva vederlo: le sei righe inglesi sono uguali, e il dossier le mostra una per
volta.

⚠️ La nota dei mezzi di **terra** (`:51360`) e' invece davvero una sola per
quattro: corazzata, locomotiva, autocarro e carrozza hanno lo stesso giapponese
identico. Una resa, quattro righe.

### ⚠️⚠️ L'INGLESE È ROTTO ALTRE DUE VOLTE, E SEMPRE COPIANDO LA RIGA VICINA

Fa **quattro** in questa sessione: il te' nero (049), il liquido antiacido
(050), e qui:

    :96060  l'atto del MUSEO
      JP   博物館を建てる権利が得られる証書
      EN   «A deed gives the right to create a **shop**»
           (e' la riga del negozio, `:95990`; la seconda meta' dell'inglese
            parla poi di collezionisti, quindi la copia e' della prima frase)

    :97128  la pergamena di potenziamento dell'ARMA
      JP   武器の強度が増し (la robustezza dell'ARMA)
      EN   «increases the strength of the **armour**»
           (e' la riga dell'armatura, `:96986`)

⭐ **La forma del guasto e' sempre la stessa**: due righe gemelle per
costruzione, e monte ricopia l'una nell'altra senza cambiare la parola che le
distingue. Si vede solo mettendo le due righe **una accanto all'altra**, e in
tre casi su quattro le due righe stavano in lotti diversi.

### ⚠️ E UNA VOLTA L'INGLESE SBAGLIA IL CETO

`:51359`, la corazzata terrestre: ちょっとした金持ち程度では維持費を工面できない
e' «uno **appena benestante** non riesce a pagarne il mantenimento» — cioe'
serve essere ricchi sul serio. L'inglese scrive «even the richest person cannot
afford to maintain», che dice il contrario: che non se la puo' permettere
nessuno. Segue il giapponese.

### ⓘ I nomi che venivano da altre tabelle

    死神        -> **la Morte**, femminile e con la maiuscola (`item_func.hsp`,
                   «stringe un patto con la Morte»)
    ベルム家    -> **casa Bellum** (`chat.hsp`), non «Belm» come l'inglese
    エウダーナ  -> **Eulderna**
    すくつ      -> **il Vuoto** ⚠️ e' il refuso voluto di 巣窟; l'inglese scrive
                   «the sanctuary», che sarebbe un terzo nome per lo stesso
                   posto. Lo decide il rapporto di identificazione della
                   licenza stessa, che dice gia' «il Vuoto»
    形見のカバン -> **la borsa dei ricordi**
    魔具全典    -> `~Compendio Completo degli Oggetti Magici~` ⓘ l'inglese lo
                   scrive «Arcane Alamanac», col refuso, in tutte e diciotto

### ⓘ Le parole lunghe, e perche' restano

Il preflight segnala sei parole da 15 caratteri: `l'assicurazione` (quattro
volte, nella nota della nave) ed `equipaggiamento` (due). Sono dentro la
finestra di rinculo, che e' un **indizio** e non un vincolo (113a): a decidere
e' dove cade il taglio, e quello lo sa solo `_107-descrizioni-item`. Sciogliere
`equipaggiamento` vorrebbe dire scrivere un'altra parola per un termine che il
progetto usa dappertutto, compreso il nome degli oggetti. Misurate dopo il
reimport: parole spezzate introdotte **0**.

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le code del lotto sono **undici**, tutte gia' in tabella (`_code.py 051`: righe
senza resa **0**). Il cancello «titoli resi in PIU' modi» resta a **7**.

⚠️ La forma: **37** righe su 50 hanno lo spazio prima del `\\n` e 13 no; **26**
code hanno lo spazio dopo il `#` e 24 no.
ⓘ `:52519` e' il caso in cui l'inglese la coda non la scrive nemmeno come coda —
`# Witch's words, written in the corner`, senza le tilde. La coda italiana la
decide la **tabella**, che ha le tilde: `#~Parole di una Strega Scritte in un
Angolo~`.
"""
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
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-051.jsonl'
RIGHE = {
    44031, 44300, 44371, 45060, 45061, 45131, 45132, 45202, 45273, 45274,
    45344, 45345, 45415, 51359, 51360, 51361, 51430, 51432, 51501, 51572,
    52517, 52519, 55211, 58396, 70197, 71028, 81399, 81740, 83411, 83626,
    88346, 88741, 89490, 89884, 92654, 94246, 94670, 94739, 95990, 96060,
    96497, 96782, 96915, 96986, 97057, 97128, 97396, 97467, 97538, 99025,
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
