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
