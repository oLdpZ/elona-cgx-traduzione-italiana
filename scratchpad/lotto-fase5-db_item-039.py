# -*- coding: utf-8 -*-
"""115a - Lotto 039 di `db_item.hsp`: GLI SCARTI, seconda parte.

`FILTER_JUNK`, righe 62.000-76.000: **51 righe** su 34 oggetti — 34 dell'indice
0, 8 dell'indice 1 e 9 dell'indice 2. E' il lotto con piu' righe di indice 1 e 2
di tutta la sessione, e la ragione e' una famiglia sola.

### ⭐⭐⭐ GLI OTTO OGGETTI DEGLI DEI: UN PANNELLO E' UNA SCENETTA A DUE VOCI

`:62865`, `:62929`, `:62993`, `:63057`, `:63121`, `:63185`, `:63249`, `:63313`
sono oggetti personali di otto divinita', e hanno tutti la stessa forma:
l'indice 0 e' la voce d'enciclopedia, e gli indici 1 e 2 sono **due battute di
due dei diversi**, che si rispondono.

    il manubrio    Urcaguary «me lo prendo un attimo» / Opatos «ridammelo»
    l'amuleto      Rovid mostra la scritta / Jure si vergogna
    la candela     Arasiel ride dello schiavo / Lulwy «la prossima sei tu»

⚠️ **Vanno rese come una scena, non come tre righe**: la seconda battuta e' la
risposta alla prima, e nel manubrio la risposta e' perfino un gioco fonetico —
「フゥハハハハハハハハハー！かえして」, dove la risata **diventa** «ridammelo».
L'inglese lo tiene («Muwahahahahahahave it back!»), l'italiano pure
(«Muahahahaha ridammelo»).
⚠️ Ma non attaccato: 15 caratteri di fila li spezza l'impaginatore, e il
preflight l'ha visto. Lo spazio e' quello che salva la battuta.

### ⭐⭐⭐ I NOMI DEGLI DEI SI COPIANO, E UNO NON E' QUELLO CHE SEMBRA

Tutti e otto i nomi sono gia' nel dizionario nella forma `<Nome>`, e si trovano
con `lotti-111/_cerca.py`. ⚠️⚠️ **ネヘルタード e' `<Amurdad>`**, non
«Nehertard»: e' il nome che l'inglese di monte gli da', ed e' gia' a schermo in
`chat.hsp` e nelle chiamate di soccorso. Traslitterare il giapponese avrebbe
prodotto un dio nuovo.

⭐ Gli **epiteti in prosa** (剛石の女神, 砂嵐の女神…) non stanno nel dizionario
come voci a se': si ricavano dalle righe di livello 150, che sono gia' rese —
`<Urcaguary> la gemma tenace`, `<Arasiel> della tempesta di sabbia`,
`<Karavika> del canto e della danza`, `<Sophia> la Saggia`.

⚠️ **Quattro epiteti non hanno nessun precedente** e sono stati coniati qui:
守護の神 «il dio della protezione», 鉄騎の神 «il dio dei cavalieri di ferro»,
不幸の女神 «la dea della sventura», 永遠の神 «il dio dell'eternita'». Sta
scritto perche' una passata futura sull'elenco degli dei li trovi e li accordi,
invece di scoprirli per caso.

### ⭐⭐ L'INGLESE SALTA DUE FRASI, E TUTT'E DUE DICONO A CHE SERVE L'OGGETTO

  - `:62865`, il manubrio: il giapponese dice «usandolo mentre ti alleni
    l'effetto sale di parecchio», che e' **l'unica frase che spieghi l'oggetto**.
    L'inglese la salta e tiene solo l'aneddoto sui due fratelli;
  - `:63249`, la tazza: il giapponese racconta che la dea della sventura ha
    continuato ad assalirla e che oggi ne ha in quantita'. L'inglese salta al
    referto finale.

### ⭐⭐ E SULLA SPADA L'INGLESE INVENTA DUE VOLTE NELLA STESSA RIGA

`:63583`, la spada del teschio furiosa:

    giapponese   il taglio e' migliorato, ma l'impugnatura succhia la vita;
                 la potenza dipende dall'**Alchimia di quando e' stata fatta**
    inglese      «powered up with the power of nether and magic»;
                 la potenza dipende da «throwing techniques and their
                 magical device experience»

Nessuna delle due invenzioni e' innocua: la seconda dice al giocatore di
allenare le abilita' sbagliate. Si segue il giapponese, e la riga gemella
`:64993` (la spada non furiosa) lo conferma, perche' li' l'inglese la frase
sull'alchimia la traduce giusta.

### ⭐ LE TRE PERLE RICURVE, E L'INGLESE CHE SI CONTRADDICE DENTRO UNA RIGA

`:66009` (acqua), `:68045` (fuoco) e `:52579` (gelo, lotto 038) sono la stessa
frase con l'elemento cambiato. L'inglese di `:68045` e di `:52579` e' la stessa
copia: dice «absorb **hot** air», poi «suppress **freezing** damage» in uno e
«burning damage» nell'altro, e chiude in tutt'e due con «the **cold** air that
covers the surroundings». Una riga che si smentisce da sola in tre punti.

Il giapponese dice 火 in uno e 冷気 nell'altro, e i nomi degli oggetti — 火吸
e 冷吸, «che assorbe il fuoco» e «che assorbe il freddo» — lo confermano.

### ⓘ I dodici materiali da sintesi

`:74693`-`:75375` sono dodici oggetti che hanno tutti lo stesso indice 3 («un
oggetto per la sintesi») e un indice 0 di **una o due frasi**, ognuno da un
libro diverso. Sono le rese piu' corte del lotto e non hanno trappole; l'unica
cosa da guardare e' che l'inglese di `:74817` porta una **«s» spaiata** prima
del `\\n` («The slight brightness is stylish. s»), che non si riporta.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :62732
    (62732, "The so-called conductor's stick. By magnifying the movement of the hand, it makes it easier to give directions with gestures. It is originally used for conducting performances, but it could easily be used to instruct allies on the target of an attack. \\n# ~Music of the Melodious Irva~"):
        "La cosiddetta bacchetta del direttore. Ingrandendo il movimento della mano, rende facile dare indicazioni a gesti. In origine serve a dirigere la musica, ma indicare ai compagni chi attaccare sarà una sciocchezza. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :62865
    (62865, "Dumbbells that the Urcaguary forcefully borrowed from her brother, the God of Earth. The God of Earth is troubled by the fact that she's too lazy to look for her own personal belongings, and just take his instead. But he cannot resist his big sister.\\n# ~Irva Fantasy Encyclopedia~"):
        "Il manubrio che la dea della gemma tenace si è fatta prestare a forza dal fratello minore, il dio della terra. Usandolo mentre ti alleni l'effetto sale di parecchio. Da sempre le pesa cercare la propria roba e si porta via quella del fratello che le capita sott'occhio, così il dio della terra è in imbarazzo. Ma alla sorella maggiore non si può dire di no.\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :62866
    (62866, '\\"Muwahahahaha! I\'m gonna have these dumbbells for a while!\\" \\n# ~words of <Urcaguary>~'):
        "\\\"Muahaha! Questo manubrio me lo prendo un attimo in prestito!\\\" \\n# ~Parole di <Urcaguary>~",

    # ---------------------------------------------------------- :62867
    (62867, '\\"Muwahahahahahahave it back!\\" \\n# ~words of <Opatos>~'):
        "\\\"Muahahahaha ridammelo.\\\" \\n# ~Parole di <Opatos>~",

    # ---------------------------------------------------------- :62929
    (62929, 'Amulet was distributed to guardian deities and defenders on the pretext that it would be a nuisance if they became bedridden due to illness. It is not effective in preventing illness, but it cures the illness at high speed the moment it occurs. \\n# ~Irva Fantasy Encyclopedia~'):
        "L'amuleto distribuito al dio della protezione e ai difensori con la scusa che se si ammalano e stanno a letto è un disturbo. Non ha il potere di prevenire le malattie, ma se la malattia non è complicata la cura in un lampo, appena viene, e la guarisce del tutto. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :62930
    (62930, '\\"Here, take a closer look at this amulet. The centerpiece of the amulet is too small to contain all the letters of her blessings, and after that one big \\\'Health\\\', the letters are rapidly getting smaller to fit in the space... It is easy to imagine how flustered Lady Jure was when she was writing this. Ahh.. isn\'t that really soothing?\\" \\n# ~words of <Rovid>~'):
        "\\\"Ecco, guardate quest'amuleto. In mezzo ha scritto Salute a lettere così grandi che poi non ci stavano più, e da lì in avanti, per farle entrare nello spazio, si fanno di colpo minute... Si immagina benissimo la fretta di Jure mentre lo scriveva. Ah, che pace, vero?\\\" \\n# ~Parole di <Rovid>~",

    # ---------------------------------------------------------- :62931
    (62931, '\\"W-what did you..  you idiot! Ahhhh!!!! This is so embarrassing, stop looking at it!!!!\\" \\n# ~words of <Jure>~'):
        "\\\"E-ehi, scemo! Che vergogna, smettila!\\\" \\n# ~Parole di <Jure>~",

    # ---------------------------------------------------------- :62993
    (62993, 'Bewitching red candle containing a suspicious medicine. When burned, the ingredients vaporize and diffuse, uplifting the spirit of the subject. The Goddess of Wind prepared a large quantity of candles in order to torture the subject with them endlessly, but the Goddess of Sandstorms went down after only one candle. The Goddess of Wind was so amused that she must have dumped them all in the desert afterwards. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una candela rossa inquietante, con dentro una medicina sospetta. Bruciando, le sostanze evaporano e si spargono, e a chi le respira monta l'eccitazione. La dea del vento ne aveva preparate in quantità per un supplizio di candele senza fine, ma la dea della tempesta di sabbia è andata giù con una sola. Alla dea del vento è passata la voglia e dopo, si dice, le buttò tutte nel deserto... \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :62994
    (62994, '\\"Ahahaha! Look how cute our Slave-kun is when he rolls his little eyes in ecstacy! This candle is amazing, big sister!\\" \\n# ~words of <Arasiel>~'):
        "\\\"Ahah! Lo schiavo sta godendo con gli occhi all'insù! Questa candela è incredibile, sorellona!\\\" \\n# ~Parole di <Arasiel>~",

    # ---------------------------------------------------------- :62995
    (62995, '\\"Arasiel, you\'re next.\\" \\n# ~words of <Lulwy>~'):
        "\\\"Arasiel, la prossima sei tu.\\\" \\n# ~Parole di <Lulwy>~",

    # ---------------------------------------------------------- :63057
    (63057, "Set of specialized signal bullets. It has the ability to easily change the shot's colors and patterns. It was given by the God of Machine to the God of Pharact who was having trouble operating in areas with poor radio reception. It emits enough light to be recognized even in daylight and appears to shine even in a storm, so that instructions can be quickly transmitted to the other party in a position where their voice cannot be heard. It also consumes no turns. \\n# ~Irva Fantasy Encyclopedia~"):
        "Viene insieme ai suoi razzi di segnale. Sa cambiare facilmente colore e disegno del colpo. Il dio delle macchine l'ha data al dio dei cavalieri di ferro, che penava a condurre le operazioni dove le onde arrivano male. Manda una luce che si riconosce anche di giorno e brilla perfino dentro la tempesta, così l'ordine arriva in fretta anche a chi sta dove la voce non giunge. E non consuma il turno. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :63058
    (63058, '\\"Even if there is signal interference, I can use this to give instructions. It\'s a primitive means, though.\\" \\n# ~words of <Mani>~'):
        "\\\"Anche se le onde sono disturbate, da vicino con questa gli ordini si danno. È un mezzo primitivo, però.\\\" \\n# ~Parole di <Mani>~",

    # ---------------------------------------------------------- :63059
    (63059, '\\"As expected of Lord Mani!\\" \\n# ~words of <Garziem>~'):
        "\\\"Il signor Mani non delude mai!\\\" \\n# ~Parole di <Garziem>~",

    # ---------------------------------------------------------- :63121
    (63121, 'Glasses worn by the Goddess of Wealth when she carefully assesses the strength of her opponent. It is said that she also wore them when she discovered the talent of the Goddess of Opera. She usually takes them off because they tire her eyes, and sometimes she forgets to put them back on. \\n# ~Irva Fantasy Encyclopedia~'):
        "Gli occhiali che la dea della ricchezza si mette quando vuole giudicare bene quanto vale chi ha davanti. Pare li portasse anche quando scoprì il talento della dea del canto e della danza. Di solito li tiene via perché le stancano gli occhi, e ogni tanto li dimentica in giro. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :63122
    (63122, '\\"Hey! my glasses fits you well~\\" \\n# ~words of <Yacatect>~'):
        "\\\"Sono occhiali che ai miei occhi vanno proprio bene!\\\" \\n# ~Parole di <Yacatect>~",

    # ---------------------------------------------------------- :63123
    (63123, '\\"Yaca-ne, you forgot to wear your glasses again..\\" \\n# ~words of <Karavika>~'):
        "\\\"Sorella Yaca, ha di nuovo lasciato gli occhiali in camerino...\\\" \\n# ~Parole di <Karavika>~",

    # ---------------------------------------------------------- :63185
    (63185, 'Bookmarks said to have been gifted to the Goddess of Wisdom by the God of Element. The God of Element made several thousand of these bookmarks and was at a loss when he came back to himself, but the Goddess of Wisdom was happy to receive all of them and uses them all as usual. It is said that when the bookmark is inserted, it makes the reader feel an irresistible desire to read the rest of the book. \\n# ~Irva Fantasy Encyclopedia~'):
        "Il segnalibro che, dicono, il dio degli elementi mandò alla dea della sapienza. Si era messo d'impegno e ne aveva fatti per qualche migliaio; tornato in sé non sapeva più che farne, ma la dea della sapienza li accettò tutti volentieri e li usa tutti, normalmente. Dicono che, a infilarlo, venga una voglia matta di sapere come va avanti il libro. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :63186
    (63186, '\\"Reading is always good. Not just for knowledge. But to read and to think. It is time well spent.\\" \\n# ~words of <Sophia>~'):
        "\\\"Leggere fa bene. Non è solo prendere sapere: si legge e si pensa. Lì c'è un tempo pieno.\\\" \\n# ~Parole di <Sophia>~",

    # ---------------------------------------------------------- :63187
    (63187, '\\"So you are fond of books, well then, here is a gift for you.\\" \\n# ~words of <Itzpalt>~'):
        "\\\"Capisco, ami i libri. Allora il dono che ti concedo è questo.\\\" \\n# ~Parole di <Itzpalt>~",

    # ---------------------------------------------------------- :63249
    (63249, 'This mug originally belonging to the Goddess of Fortune, was noticed by the Goddess of Misfortune who was passing by, and she snatched it away from her without putting up a fight. According to investigations, this mug has the effect of making even dangerous well water safe to drink. \\n# ~Irva Fantasy Encyclopedia~'):
        "Era la tazza della dea della fortuna, ma un giorno la dea della sventura, che passava di lì a spasso, ci mise gli occhi e se la portò via senza lasciarle il tempo di opporsi. Alla dea della sventura dev'essere piaciuta parecchio, perché ha continuato ad assalirla e a derubarla, e il sospetto che oggi ne abbia in quantità tutte uguali è forte assai. Stando alle indagini, questa tazza ha la virtù di rendere bevibile senza rischio perfino l'acqua cattiva di un pozzo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :63250
    (63250, '\\"Ehekatl! I want this! It\'s cute! It\'s cute! Give it to me! Gimme!\\" \\n# ~words of <Sinaha>~'):
        "\\\"Ehekatl! Questa è carina, me la prendo io, miao! Dammela buona buona, miao!\\\" \\n# ~Parole di <Sinaha>~",

    # ---------------------------------------------------------- :63251
    (63251, '\\"Kitty loves her kitty cup? Kitty can have it~\\" \\n# ~words of <Ehekatl>~'):
        "\\\"Uau! Ti piace la tazza col gattino? Ti piace? Te la regalo!\\\" \\n# ~Parole di <Ehekatl>~",

    # ---------------------------------------------------------- :63313
    (63313, 'Shears said to have been created by the God of Harvest from his own feathers and passed on to the God of Eternity. They are used to completely separate the soul from the body after it has met its fateful death and return it to the flow of reincarnation. It is possible to draw out some of the power without the corresponding divine power, and if used to harvest crops, it is easier for new sprouts to appear. \\n# ~Irva Fantasy Encyclopedia~'):
        "Le cesoie che, dicono, il dio del raccolto ricavò da una propria piuma e consegnò al dio dell'eternità. Servono a staccare del tutto dal corpo l'anima che ha avuto la morte che le spettava, e a rimetterla nel flusso delle rinascite. Anche senza la forza divina che ci vorrebbe se ne può tirare fuori una parte, e usandole per raccogliere i frutti i germogli nuovi vengono più facili. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :63314
    (63314, '\\"Have.. this..\\" \\n# ~words of <Kumiromi>~'):
        "\\\"Queste... puoi... usarle...\\\" \\n# ~Parole di <Kumiromi>~",

# 8 voci, 0 ambigue

    # ---------------------------------------------------------- :63315
    (63315, '\\"The soul leaves the body... and returns to the light...\\" \\n# ~words of <Amurdad>~'):
        "\\\"L'anima si stacca dal corpo... e torna dentro la luce...\\\" \\n# ~Parole di <Amurdad>~",

    # ---------------------------------------------------------- :63583
    (63583, "The sword has been fused by alchemy again and transformed into a magnificent magic sword. It has been powered up with the power of nether and magic, but its rampancy has increased, so it is better to throw it at enemies. The power depends on user's throwing techniques and thier magical device experience.\\n# ~Arcane Almanac~"):
        "Fusa di nuovo dall'alchimia, è rinata come una bella spada magica. Taglia meglio, ma a tenerla in mano a lungo l'impugnatura ti succhia la vita: meglio scagliarla contro il nemico. La potenza dell'urto dipende dalla tecnica di Alchimia di quando è stata fatta.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64615
    (64615, 'A large basket with nothing inside. It is mainly used as a container when eating outdoors. It is carefully woven and very sturdy. \\n# ~Supporting Roles in Kitchen~'):
        "Un cesto grande senza niente dentro. Si usa soprattutto da contenitore quando si mangia all'aperto. È intrecciato con cura e molto robusto. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :64869
    (64869, "A powerful magic bomb made by alchemy. It is said to have been developed by an old alchemist for self-defense. It is characterized by the multi-stage explosion of the released magic power. Its power depends on the user's magical device and magic control skills. \\n# ~Arcane Almanac~"):
        "Una potente bomba magica fatta con l'alchimia. Pare l'abbia messa a punto per difendersi un alchimista di un tempo. La sua particolarità è che la forza magica liberata esplode a più riprese. La potenza dipende dalle tecniche di Controllo magia e di Dispositivi magici. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64931
    (64931, "Alchemy altered crystals of magic power. The enclosed magic power is unstable, and when the pin is pulled out and a shock is given, a magical explosion occurs. Its power depends on the user's magical device and magic control skills. \\n# ~Arcane Almanac~"):
        "Un cristallo di forza magica a cui l'alchimia ha rimescolato la composizione. La magia chiusa dentro è instabile, e togliendo la spina e dandogli un colpo scoppia in un'esplosione magica. La potenza dipende dalle tecniche di Controllo magia e di Dispositivi magici. È famoso come materiale pericoloso facile da fare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64993
    (64993, 'A sword that was once broken, but has been reborn through alchemy. The sword is afraid of being broken again and goes wild when you try to hold it up. It is not suitable for wielding, so throw the sword without giving it a chance to flail about. Show no mercy. The power of the sword depends on the technique of alchemy at the time of its creation. \\n# ~Arcane Almanac~'):
        "Una spada che una volta si era spezzata e che l'alchimia ha fatto rinascere. Ha paura di rompersi di nuovo, e appena la impugni si dimena. Non è fatta per essere brandita: lanciala senza darle il tempo di agitarsi. Non avere pietà. La potenza dell'urto dipende dalla tecnica di Alchimia di quando è stata fatta. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :66009
    (66009, 'A curved stone with magical powers. It has the property of reacting to mana and agglomerating atmospheric moisture, so the moment you put it in your pocket, you are sure to get soaked. Due to its principle, it does not function well in arid areas such as deserts. \\n#~Mysterious Ancient Ornaments~'):
        "Una pietra ricurva che ha forza magica. Ha la proprietà di rispondere alla mana e di raccogliere l'umidità dell'aria: appena te la metti in tasca, è sicuro che ti bagni tutto. Per come funziona, nelle terre secche come il deserto non rende bene. \\n#~Misteriosi Ornamenti Antichi~",

    # ---------------------------------------------------------- :66261
    (66261, 'A disk on which all kinds of information about a person, including memories and thoughts, are copied and engraved. It is a lost technology that only the manufacturing process is transmitted, and it is unknown how it can be read or what it can be used for. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un disco su cui hanno copiato e inciso ogni informazione di una persona, ricordi e pensieri compresi. È una tecnica perduta di cui resta solo il modo di fabbricarlo; come si legga e a che serva non si sa. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :66323
    (66323, 'Egg-shaped organic capsules brought to the couple by storks. There are rumors that they are harvested in a special garden, but anyone who has ever gotten to the bottom of the matter has been lost. \\n# ~Irva Fantasy Encyclopedia~'):
        "La capsula organica a forma di uovo che la cicogna porta agli sposi. Gira anche la voce che si raccolga in certi campi, ma chi si è avvicinato alla verità è sparito, senza eccezioni. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :66765
    (66765, 'Quarried stone block. Mainly used to make sculptures and walls. \\n# ~Lumiest Art Catalogue~'):
        "Un blocco di pietra tagliato dalla cava. Serve soprattutto a fare sculture e muri. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :68045
    (68045, 'A curved stone with magical power to absorb hot air. When it is used as a lens when exposed to hot air, it can pass the magic power through it to suppress burning damage. However, its range of effect is very narrow and it is useless to protect oneself from the cold air that covers the surroundings. \\n#~Mysterious Ancient Ornaments~'):
        "Una pietra ricurva con la forza magica di assorbire il fuoco. Quando si manda fuoco, facendoci passare la magia come attraverso una lente, si trattiene la combustione. Ma il raggio in cui agisce è strettissimo, e per ripararsi dal fuoco che si allarga non serve. \\n#~Misteriosi Ornamenti Antichi~",

    # ---------------------------------------------------------- :68388
    (68388, 'Trees that are cut down and processed into building materials and tools. Insufficiently dried wood is heavier, more susceptible to rot, shrinkage and deformation, and less strong than dried wood. \\n# ~Forest Economics, Sawmill Edition~'):
        "Alberi abbattuti e lavorati per farne materiale da costruzione e arnesi. Il legno non seccato abbastanza è pesante, marcisce facilmente, si ritira e si deforma, e come resistenza è peggio di quello secco. \\n# ~Foreste ed Economia: la Segheria~",

    # ---------------------------------------------------------- :69388
    (69388, 'Large brush for livestock. Frequent brushing improves blood circulation, congestion, and health by eliminating dirt and insects. \\n# ~Living with Livestock~'):
        "Una spazzola grande da allevamento. Spazzolare spesso migliora la circolazione e il pelo, e togliendo sporco e insetti fa anche bene alla salute. \\n# ~Vivere Insieme al Bestiame~",

    # ---------------------------------------------------------- :71643
    (71643, 'It uses ordinary fishing bait attached as its energy source to automatically search for and capture prey in an instant. After the capture, the fishes are automatically propelled into air, so there is very little for humans to do, and fishing skills are rarely improved. \\n# ~Daily Necessities for the Home~'):
        "Usa come fonte d'energia la normale esca montata insieme, e in un attimo cerca da sé la preda e la cattura. Anche dopo torna su da solo, così all'uomo non resta quasi niente da fare e nella pesca non si migliora quasi per niente. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :71645
    (71645, '\\"This is certainly useful, but it moves so fast and drains a lot of my stamina. So I prefer to fish in a more normal, leisurely manner.\\" \\n# ~words of a fisherman proud of his catch~'):
        "\\\"Comodo lo è di sicuro, ma si muove che è una furia e a chi tiene la canna consuma un mucchio di resistenza. Io preferisco pescare con calma, alla maniera normale.\\\" \\n# ~Parole di un Pescatore Fiero della Sua Preda~",

# 9 voci, 0 ambigue

    # ---------------------------------------------------------- :74693
    (74693, 'Frozen water containing magical powers. It is good for nerve damage.\\n# ~Life-saving First-aid~'):
        "Acqua con dentro forza magica, congelata. Fa bene ai dolori dei nervi.\\n# ~Il Primo Soccorso che Salva la Vita~",

    # ---------------------------------------------------------- :74755
    (74755, 'Black water droplets. It looks bad for you, but on the contrary, it has a detoxifying effect.\\n# ~Encyclopedia of Poison~'):
        "Una goccia nera. Sembra faccia male, e invece è il contrario: toglie il veleno.\\n# ~Dizionario dei Veleni e dei Farmaci~",

    # ---------------------------------------------------------- :74817
    (74817, 'Lighting fixture made of glowing grass. The slight brightness is stylish. s\\n# ~Interior Paradise: Extra Issue~'):
        "Una lampada fatta con erba che brilla. Quella luce appena accennata è elegante.\\n# ~Interior Paradise: Numero Straordinario~",

    # ---------------------------------------------------------- :74879
    (74879, 'Processed ores that are a mixture of various components. \\n#~Vernis Ore Catalogue~'):
        "Un minerale con dentro mescolate sostanze di ogni sorta, poi lavorato. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :74941
    (74941, 'A mirror made of ether. It emits a mysterious radiance.\\n# ~Stylish Item Special~'):
        "Uno specchio fatto d'etere. Manda un bagliore misterioso.\\n# ~Grande Speciale sugli Oggetti alla Moda~",

    # ---------------------------------------------------------- :75003
    (75003, 'Wings made by sewing together bird feathers. They are not solidified with wax, so they do not fall apart when heated. \\n# ~The Encyclopedia of Sewing~'):
        "Ali fatte cucendo insieme penne d'uccello. Non sono tenute insieme dalla cera, quindi a scaldarle non si sfasciano. \\n# ~Grande Enciclopedia del Cucito~",

    # ---------------------------------------------------------- :75065
    (75065, 'Cultured troll cells. Developed for therapeutic use but not practical because it erodes other cells. \\n# ~Mysterious Report~'):
        "Cellule di troll coltivate. Le avevano messe a punto per curare, ma siccome divorano le altre cellule non si sono rivelate pratiche. \\n# ~Rapporto Misterioso~",

    # ---------------------------------------------------------- :75127
    (75127, 'The music it plays drives people crazy. The more sane you are, the more damage it does. \\n# ~Music of the Melodious Irva~'):
        "A farlo suonare esce una musica che ti fa girare la testa. Più uno è sano di mente, più il danno è grosso. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :75189
    (75189, 'An old-fashioned heating appliance. Please ventilate frequently as it produces large amounts of carbon monoxide and other harmful flammable gases. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un apparecchio da riscaldamento di una volta. Siccome fa molto gas nocivo, ossido di carbonio compreso, arieggia spesso. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :75251
    (75251, 'Battery. Can be recharged for repeated use. \\n# ~the Legacy of Mechanical Civilization~'):
        "Una batteria. Ricaricandola si usa più volte. \\n# ~Speciale: l'Eredità della Civiltà Meccanica~",

    # ---------------------------------------------------------- :75313
    (75313, "The ingredients contained in trace amounts in pebbles are collected and reconstituted by alchemy. It can only be processed at a fairly high heat. \\n# ~Zaile's Book of Mineralogy~"):
        "Le sostanze contenute in tracce dentro i sassi, raccolte e ricomposte con l'alchimia. Non si lavora se non a un calore parecchio alto. \\n# ~Atlante dei Minerali di Zaile~",

    # ---------------------------------------------------------- :75375
    (75375, 'Statue of a dragon made from scraps. A heap of dust makes a heap. Even scraps can become art if they are processed. \\n# ~Lumiest Art Catalogue~'):
        "Una statua di drago fatta di scarti. A furia di granelli si fa una montagna: anche gli scarti, lavorati, diventano arte. \\n# ~Catalogo d'Arte di Lumiest~",

# 34 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-039.jsonl'
RIGHE = {
    62732, 62865, 62866, 62867, 62929, 62930, 62931, 62993, 62994, 62995,
    63057, 63058, 63059, 63121, 63122, 63123, 63185, 63186, 63187, 63249,
    63250, 63251, 63313, 63314, 63315, 63583, 64615, 64869, 64931, 64993,
    66009, 66261, 66323, 66765, 68045, 68388, 69388, 71643, 71645, 74693,
    74755, 74817, 74879, 74941, 75003, 75065, 75127, 75189, 75251, 75313,
    75375,
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
