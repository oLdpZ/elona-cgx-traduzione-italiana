import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :42914
    (42914, "An unregistered card with special magic. It records information from the person hit by it. Using it on anyone other than close friends will definitely make them angry, as it's like stealing personal information. \\n#~Lumiest Art Catalogue~"):
        "Una carta su cui non è ancora scritta nessuna informazione. Ha addosso una magia particolare, e registra i dati di chi colpisce. È come portarsi via i dati di una persona senza permesso: usarla su chi non è di casa fa arrabbiare di sicuro. \\n#~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :42976
    (42976, 'This is not mere strawberry ice cream. But a masterpiece of shit, sculpted with such artistic perfection. And like any true art, it naturally explodes, the magnum poopus. Its explosive power depends on the techniques of gem-cutting and gene-engineering.\\n# ~Lumiest Art Catalogue~'):
        "Non è un gelato alla fragola. È uno sterco venuto in una forma fin troppo artistica. Essendo arte a tutti gli effetti, va da sé che esplode. La sua potenza, dicono, dipende dalle tecniche di Oreficeria e di Ingegneria genetica.\\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :43174
    (43174, "The result of a preserved food that has been fermenting in a can. According to analysis, it appears to be an ancient salted fish. The can is extremely bloated, and if subjected to strong impact, it will release a powerful stench, causing an explosion dependent on user's gene engineering and cooking skills. It is dangerous to open, as scans reveal the contents have mostly degraded into a gaseous state.\\n#~Everchanging Food of Tyris~"):
        "Quel che resta di una conserva che nella scatola ha continuato a fermentare. A leggerla pare fosse pesce salato dei tempi antichi. È gonfia da scoppiare, e a darle un colpo forte sprigiona il fetore e fa un'esplosione che dipende dalle tecniche di Ingegneria genetica e di Cucina. Aprirla è pericoloso, e sondandone dentro la materia si è scoperto che il contenuto si è decomposto ed è quasi tutto allo stato di gas.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :43302
    (43302, "Too-big-to-be-true snowflakes manufactured by wizards. Apparently, they tested a dubious theory that if you speak kind words to water and freeze it, it will turn into beautiful crystals. The wizard's hypothesis- that humans should not be allowed to decide what is beautiful or ugly, that he should not speak in human terms, and that humans should not freeze these without permission in the first place - which cause explosions that rely on user's meditation and gem cutting skills. \\n#~Arcane Almanac~"):
        "Un cristallo di neve fin troppo grosso, fabbricato da un mago. Pare che verificasse una teoria sospetta: che l'acqua, se le si parla con dolcezza e poi la si congela, diventi un bel cristallo. Il suo malumore (non sia mai che siano gli uomini a decidere che cosa è bello; e non mi si parli con parole d'uomo; e soprattutto non mi si congeli senza permesso) fa un'esplosione che dipende dalle tecniche di Meditazione e di Oreficeria, e ferisce i nemici. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :43364
    (43364, "Non-lethal weapons that envelops its surroundings in darkness. Its power is said to depend on user's tactics and marksmanship skills. According to documents, the world used to be full of flashbangs. However, they were defeated by the sudden appearance of darkbangs, and the flashbangs were buried in the darkness of history. \\n#~Collection of Armaments you can Use Tomorrow Cont.~"):
        "Un'arma non letale che avvolge di buio tutto intorno. La sua potenza, dicono, dipende dalle tecniche di Tattica e di Mira. Secondo i documenti, un tempo questo mondo era pieno di colpi accecanti; poi comparve di colpo il colpo oscuro, li batté, e i colpi accecanti furono sepolti nel buio della storia. \\n#~Ancora Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :43426
    (43426, "Device based on the lightning conductor. The needle itself stores the energy of lightning strikes through magical protection and can discharge it as needed. The output of the discharge is said to depend on the user's Control Magic and Magic Capacity skills. Normally, they are stored away for fear of theft or damage, but when a thunderstorm occurs, mages begin to set them up in the open air. \\n#~Arcane Almanac~"):
        "Un apparecchio nato dal parafulmine. Con una protezione magica l'ago stesso accumula l'energia dei fulmini, e la scarica quando serve. La forza della scarica, pare, dipende da Controllo magia e da Capacità magica. Di solito lo tengono al chiuso per paura dei ladri e dei danni, ma quando viene il temporale i maghi cominciano a piantarlo all'aperto. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :43488
    (43488, "Also known as box of plagues. Disguised as a gift, it is a chemical armament used by foxes as deterrants. It is made from cultivated parasites, which acts on the opponent's brain and causes disorientation. The brain waves are then transmitted by sorcery to surrounding enemies, causing secondary damage. Its power is said to depend on the skills of Disarm Traps and Gene Engineering of the user. \\n#~Fool me twice, Shame on me!~"):
        "Detta anche la scatola della pestilenza. È mascherata da regalo, ma è un'arma chimica che le volpi usano per stregare e uccidere. La fanno coi parassiti: agisce sul cervello e porta disturbi di coscienza. Poi la stregoneria propaga quelle onde ai nemici intorno e fa danni di rimbalzo. La sua potenza, dicono, dipende dalle tecniche di Disarmo trappole e di Ingegneria genetica. \\n#~Non ci Casco Più! Come Scoprire i Trucchi dei Mostri~",

    # ---------------------------------------------------------- :43767
    (43767, 'Introduced as a solution to the increasing number of untrained pets, which was becoming a social problem. Pets can be trained in exchange for this coupon. They are distributed free of charge to each household, and people who do not have pets can use them as gifts for those who do. \\n#~Palmia Public Services~'):
        "È stato introdotto come rimedio a un problema sociale: i compagni maleducati erano sempre di più. Dandolo a un compagno, in cambio del biglietto viene addestrato. Lo distribuiscono gratis a ogni famiglia, e chi un compagno non ce l'ha pare lo regali a chi ce l'ha, per farsi offrire da bere. \\n#~Bollettino di Palmia~",

    # ---------------------------------------------------------- :43768
    (43768, 'The training ticket will only take them up to the basic course. Anything beyond that is not covered.\\n# ~words of a Pet Trainer~'):
        "\\\"Col biglietto si arriva al corso base e non oltre. Più in là non conviene, se non si paga in contanti.\\\"\\n# ~Parole dell'Addestratore di Bestie~",

    # ---------------------------------------------------------- :43769
    (43769, 'Saving tickets is annoying! Pay in Cash!\\n# ~words at the Training Center ~'):
        "\\\"Il biglietto si può usare, ma la pratica è una noia: meglio pagare in contanti!\\\"\\n# ~Avviso Affisso alla Palestra~",

    # ---------------------------------------------------------- :43829
    (43829, 'A potion plug commonly used in modern times. To the average person, they are garbage. \\n#~Thousands of pieces of Junk I love~'):
        "Il tappo di pozione che si usa comunemente oggi. Per la gente normale è spazzatura. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :43962
    (43962, 'A magnificent chain to be proud of. The design is popular because it can be worn anywhere, on the neck, wrist, or ankle, but the most standard is to wear it around the neck and drape it like a necktie.\\n#~Gift for your loved ones~'):
        "Una catena tanto bella da vantarsene. Piace perché il disegno la lascia mettere dove si vuole, al collo, al polso, alla caviglia; ma il modo più comune è portarla al collo e lasciarla pendere come una cravatta.\\n#~Scegliamo un Dono per Chi ci sta a Cuore~",

    # ---------------------------------------------------------- :43963
    (43963, '\\"Don\'t hate me chains because they beautiful, maybe get yourself some cool ass golden chains you\'d be braggin \'bout them like me.\\" \\n# a Slave showing off his chains.'):
        "\\\"Gli altri schiavi, da un po', mi sventolano davanti le loro belle catene e se ne vantano di continuo. La voglio anch'io una catena bella così!\\\" \\n#~Parole di uno Schiavo Fiero delle Sue Catene~",

    # ---------------------------------------------------------- :46010
    (46010, 'Large stuffed shark. It is quite jawsome and very fluffy. However, sharks in Ylva are usually named by their creators on their plush toys. For this reason, they are shunned by humans who want to name their plush toys themselves, and are considered childish by humans who do not name their plush toys, and are not in great demand.\\n#~Shark Believer Compendium~'):
        "Un pupazzo di squalo bello grosso. È fatto proprio a pinna d'arte, e morbidissimo. Solo che a Irva, per i pupazzi di squalo, di regola è chi li fa a dare loro un nome. Per questo chi il nome vuole darlo da sé lo evita, e chi ai pupazzi il nome non lo dà lo trova infantile: di richiesta ce n'è poca.\\n#~Grande Compendio dei Fedeli dello Squalo~",

    # ---------------------------------------------------------- :46213
    (46213, 'A flower that does not grow outdoors. It grows wild in Nefia and absorb its magic using the roots, but almost all plants in this form are monstrous except Dernefia. This very oddity has been studied for many years, but alas fruitless. In addition to the fact that it is difficult to grow in safe layers, it has great medicinal value, which is why there are so few samples of it.'):
        "Un fiore che all'aperto non cresce. Nasce spontaneo nelle Nefia e ne succhia la forza magica dalle radici, ma le piante fatte così, tranne la dernefia, sono quasi tutte diventate mostri. Perché solo la dernefia non diventi un mostro lo studiano da anni, e pare che non ne vengano a capo. Ai piani sicuri attecchisce male, e in più ha virtù che curano, così che mostri e avventurieri se la mangiano volentieri: di campioni ce n'è pochi.",

    # ---------------------------------------------------------- :46214
    (46214, '\\"YES OF COURSE IT SUITS JUA! SHE WILL DEFINITELY GET ALL FLUSTERED WHEN I GIVE IT TO HER! YES I AM GOING NEFIA DIVING\\" \\n# Monologue of a Jure Fanatic'):
        "\\\"Pare che ci sia un fiore introvabile che a Jure donerebbe... Se glielo porto, di sicuro, per quanto faccia la difficile a parole, ci resta contenta... Vado un attimo giù in una Nefia.\\\" \\n# ~Monologo di un Fanatico di Jure~",

    # ---------------------------------------------------------- :46215
    (46215, "It's a plant that heals you a bit when you eat it. \\n#~Identification Report: <Plants> Category~"):
        "È una pianta che, a mangiarla, cura un poco. \\n#~Rapporto di Identificazione: categoria <Piante>~",

    # ---------------------------------------------------------- :46275
    (46275, 'Plastic lid. Light, strong and recyclable. Abundant in the world when plastic bottles were still used. However, many of them were not washed and sent for recycling, and there are idiots who discard them and cause environmental pollution, and eco-terrorist attacks have also broken out because of it. A villain even attempts to control society with a weapon that ejects bottle caps at high speed. It is said that the manufacturers could not stand the various social problems accumulated, leading to the discontinuation of production. Today, with the spread of cheap, easy-to-process pseudo-glass, they have completely become a relic of the past.\\n#~Thousands of pieces of Junk I love~'):
        "Un coperchio di plastica. Leggero, resistente e riciclabile. Ai tempi in cui andavano le bottiglie di plastica ne era pieno il mondo. Solo che in tanti li buttavano nel riciclo senza lavarli, i costi e la fatica sono cresciuti e il recupero è saltato. Per colpa degli imbecilli che li gettavano per strada l'inquinamento è andato avanti, e sono scoppiati anche attentati di ecoterroristi che avevano sbagliato bersaglio. È perfino comparso un malvivente che voleva tenere in pugno la società con un arnese che sparava tappi ad alta velocità. Si dice che i fabbricanti non abbiano retto ai problemi accumulati per più di cent'anni e abbiano smesso di produrli. Oggi che si è diffuso il vetro finto, che costa poco e si lavora facile, sono del tutto roba del passato.\\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :46337
    (46337, 'Small glass beads. In recent years, they have been given a variety of patterns and colours for ornamental purposes. The origin of the name is unknown, there are theories that B-dama is a ball that reacts to the B soul. The pattern inside is sometimes called Flame, because it looks like the Burning Flame inside of a Burning Soul.\\n#~Thousands of pieces of Junk I love~'):
        "Una pallina di vetro. Da qualche anno se ne fanno anche con fantasie e colori vari, che servono da ornamento. Da dove venga il nome non si sa: le tre spiegazioni più accreditate sono che venga da biidoro, che in lingua antica vuol dire vetro; che fossero palline di grado B; e che siano palline che rispondono all'anima B. Quelle col disegno dentro hanno un disegno che a volte chiamano fiamma, e anche qui le spiegazioni più accreditate sono due: che a una cosa senza nome si sia attaccato un termine inventato, e che si chiami fiamma perché a volte, rispondendo all'anima B, pare una fiamma che brucia.\\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :47149
    (47149, 'Warning whistle. A short, sharp blast is used to alert anyone who hears it.The volume itself is not very loud, so it is not suitable for waking sleeping people.\\n#~Tunes of Irva~'):
        "Un fischietto d'allarme. Soffiandoci un colpo corto e secco, chi lo sente si fa attento. Il volume in sé non è granché, quindi per svegliare chi dorme non va bene.\\n#~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :48735
    (48735, 'Cicada had never been popular in its life. After years of being cooped up in the dirt, it decided that it could not go on like this and entered a town. It kept on trying to court females in a way it was not accustomed to. It desperately wants to stay in the forefront until the end of its life if its going to die anyway. \\n#~Irva Insect Encyclopedia~'):
        "Una cicala che in tutta la vita non è mai piaciuta a nessuno. Dopo anni chiusa sottoterra ha deciso che così non poteva andare ed è scesa in città a cercare compagnia. Ha continuato a corteggiare come poteva, ma senza mai un premio, e alla fine le forze le sono venute meno. Se morire deve, vuole morire buttandosi in avanti fino all'ultimo, e si dimena con tutta l'anima. \\n#~Grande Enciclopedia degli Insetti di Irva~",

    # ---------------------------------------------------------- :48736
    (48736, "When hit, they are startled and generate a wave of roars, depending on thrower's gene-engineering and throwing skills. Normal human may not be able to withstand the impact and will probably die. \\n#~Irva Insect Encyclopedia (Footnote)~"):
        "A colpirla si spaventa e manda un'onda di fragore che dipende da Ingegneria genetica, da Lancio e dal livello. Certe volte non regge l'urto e ci lascia la pelle. \\n#~Grande Enciclopedia degli Insetti di Irva: Note~",

# 4 voci, 0 ambigue

    # ---------------------------------------------------------- :48737
    (48737, '\\"Evening heat lingers, and the sound of cicadas on the roadside fades away.\\" \\n#~Songs of a nameless poet~'):
        "\\\"Nel tramonto, sul ciglio dove il caldo ancora dura, si spegne la voce della cicala che si contorce.\\\" \\n#~Le Liriche di un Bardo Senza Nome~",

    # ---------------------------------------------------------- :50878
    (50878, 'Paper with various texts and drawings on it. They are carefully placed in envelopes, but are generally of little value in this state. \\n#~Big Book of Books~'):
        "Un foglio con sopra scritti e disegni di ogni sorta. Lo tengono con cura dentro una busta, ma così com'è, in genere, non vale niente. \\n#~Il Libro dei Libri~",

    # ---------------------------------------------------------- :52579
    (52579, 'A curved stone with magical power to absorb hot air. When it is used as a lens when exposed to hot air, it can pass the magic power through it to suppress freezing damage. However, its range of effect is very narrow and it is useless to protect oneself from the cold air that covers the surroundings. \\n#~Mysterious Ancient Ornaments~'):
        "Una pietra ricurva con la forza magica di assorbire il gelo. Quando si manda gelo, facendoci passare la magia come attraverso una lente, si trattiene la rottura da congelamento. Ma il raggio in cui agisce è strettissimo, e per ripararsi dal gelo che copre tutt'intorno non serve. \\n#~Misteriosi Ornamenti Antichi~",

    # ---------------------------------------------------------- :55273
    (55273, "A barrel with multiple blocks of gunpowder packed in it. When hit, it produces an explosive flame that burns away the surrounding area. Apart from that, when set on fire, it spews out a residue of flame. The power depends on one's carpentry and engineering techniques.\\n# ~Hazardous Materials Handling Manual~"):
        "Un barile con dentro più blocchi di polvere da sparo. A colpirlo genera una fiammata che brucia tutt'intorno. E per conto suo, se prende fuoco, sputa fuori quel che resta della fiamma. In tutt'e due i casi la potenza dipende dalle tecniche di Falegnameria e di Ingegneria genetica.\\n# ~Manuale per il Maneggio di Materiali Pericolosi~",

    # ---------------------------------------------------------- :55859
    (55859, 'Remains of past organisms encapsulated in sedimentary rocks. Body tissues have been replaced by minerals in older strata, but may remain in relatively newer strata. During the Biogeocenozoic period, the technology to reconstruct original organisms from fossils was established. \\n# ~Lumiest Art Catalogue~'):
        "I resti di esseri vissuti un tempo, chiusi dentro una roccia sedimentaria. Nei terreni antichi i tessuti sono stati sostituiti da minerali, ma in quelli più recenti a volte restano. Nell'era della civiltà biochimica, dicono, si era arrivati anche alla tecnica per ricostruire dal fossile l'essere di partenza. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :55921
    (55921, 'Soil consisting of very fine particles. It can be kneaded by hand and becomes hard when heated. This property is used to make ceramics. \\n#~Vernis Ore Catalogue~'):
        "Terra fatta di grani molto fini. La si lavora impastandola a mano, e scaldandola diventa dura. È per questa sua qualità che ci si fanno le ceramiche. \\n#~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :55983
    (55983, "A mineral with the nickname 'burning stone'. It is said to have been used as a raw material in various fields in former civilizations, but there is not much demand for it in modern Irva. \\n#~Vernis Ore Catalogue~"):
        "Un minerale che ha per soprannome pietra che brucia. Nelle civiltà passate, pare, era materia prima in molti campi, ma nell'Irva di oggi non se ne cerca granché. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :56533
    (56533, 'Survival equipment used in biochemical civilization. It is like an external fat. It has the function of converting excess mass into an energy source, storing it for a long period of time, and then restoring it as needed. Because it was developed for the human physique of the time, it is only as effective as maintaining height and weight for modern organisms. It cannot prevent starvation, so make sure you eat your food. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un arnese da sopravvivenza che si usava nella civiltà biochimica. È come del grasso attaccato fuori. Sa cambiare la massa in più in una riserva di energia, tenerla a lungo e restituirla quando serve. Siccome l'hanno fatto sulla costituzione degli uomini di allora, sui viventi di oggi l'effetto arriva sì e no a mantenere altezza e peso. Di fame non ti salva, quindi mangia come si deve. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :57893
    (57893, 'Tickets issued by Palmia in recent years. They can be used to learn work-related skills for free. The aim is to reduce the burden on jobseekers as much as possible and to stimulate economic activity. They are sent with the salary to citizens who are identified as needing assistance. \\n#~Palmia Public Relations~'):
        "Un biglietto che Palmia emette da qualche anno. Serve a imparare gratis le abilità che il lavoro richiede. Lo scopo è alleggerire il più possibile chi cerca lavoro e dare una spinta all'economia. Arriva insieme allo stipendio ai cittadini che vengono giudicati bisognosi d'aiuto. \\n#~Bollettino di Palmia~",

    # ---------------------------------------------------------- :58024
    (58024, 'Materials processed into a semi-material condition. It is useful in the manufacture of sharp weapons. Apparently the hill people discovered the processing method a long time ago. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Materia lavorata con tecnica avanzata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si fabbricano armi e armature affilate. Pare che il modo di lavorarla l'abbia scoperto tanto tempo fa la gente delle colline. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :58086
    (58086, 'Materials processed into a semi-material condition. It is useful for refurbishing sharp weapons. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Materia lavorata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si rimettono a posto armi e armature affilate. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :58148
    (58148, 'Materials processed into a semi-material condition. It is useful in the manufacture of sturdy armor. It is said that the hill people discovered the processing method a long time ago. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Materia lavorata con tecnica avanzata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si fabbricano armi e armature robuste. Pare che il modo di lavorarla l'abbia scoperto tanto tempo fa la gente delle colline. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :58210
    (58210, 'Materials processed into a semi-material condition. It is useful for refurbishing sturdy armor. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Materia lavorata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si rimettono a posto armi e armature robuste. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :58272
    (58272, 'Materials processed into a semi-material condition. It is useful in the manufacture of soft armor. It is said that the hill people discovered the processing method a long time ago. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Materia lavorata con tecnica avanzata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si fabbricano armi e armature morbide. Pare che il modo di lavorarla l'abbia scoperto tanto tempo fa la gente delle colline. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :58334
    (58334, 'Materials processed into a semi-material condition. It is useful for refurbishing soft armor. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Materia lavorata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si rimettono a posto armi e armature morbide. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :59728
    (59728, "A gift of trimmed flowers, all in one decorative package. However, it conveys too much seriousness and is rather heavy. If you give it to someone you don't get along with very well, they will be turned off, so think carefully about who you give it to. \\n#~Gift for your loved ones~"):
        "Un dono di fiori recisi messi insieme e decorati. Solo che dice fin troppo bene quanto uno ci tenga, e finisce per pesare. A regalarlo a qualcuno con cui non si va molto d'accordo lo si mette a disagio: pensa bene a chi lo dai. \\n#~Scegliamo un Dono per Chi ci sta a Cuore~",

    # ---------------------------------------------------------- :59790
    (59790, "At first glance, it appears to be just a piece of paper with a pattern drawn on it, but it is imbued with magical power. When thrown, it flies lightly through the air, dealing magical damage to anyone it touches and removing blessing effects. Its power depends on the user's magical equipment and throwing technique. \\n# ~Arcane Almanac~"):
        "A prima vista è solo un foglio con sopra un disegno, ma dentro ci hanno messo forza magica. Lanciandolo vola leggero senza curarsi dell'aria, fa danno magico a chi tocca e cancella anche l'effetto della benedizione. La potenza dipende anche da Dispositivi magici e da Lancio di chi lo usa. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :60125
    (60125, 'When you wake up at certain times of the year, this mysterious box is placed beside you before you know it. When presented to others, this mysterious object is said to bring pain to those who are hostile to it and healing to those who are friendly to it. Since the wrapping cannot be removed by any means, the contents cannot be confirmed, but according to one theory, it is said to contain both disaster and hope. \\n# ~Arcane Almanac~'):
        "Una scatola misteriosa che, in certi periodi, al risveglio ti ritrovi accanto senza ricordarti di averla messa lì. Regalandola, dicono, dà dolore a chi ti è nemico e sollievo a chi ti è amico: un oggetto che nessuno capisce. L'involucro non si stacca in nessun modo, così che il contenuto non si può vedere; ma secondo una voce ci sono dentro la sciagura e la speranza. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :60848
    (60848, 'Remnants of shortened and discarded cigarettes. Note that even in this state, it might still ignite. Although the fire is weak, do not throw it on the ground by mistake. \\n#~Dangers on the Road~'):
        "Quel che resta di una sigaretta fumata e buttata via. Attenzione: anche così può prendere fuoco. La fiamma che fa è debole, ma non ti venga in mente di gettarlo in giro. \\n#~I Pericoli sul Ciglio della Strada~",

    # ---------------------------------------------------------- :61178
    (61178, 'A relative of the eggplant. It is processed into various forms and used for smoking. In ancient times it was toxic to the body, but was bred during biochemical civilization. The current species is not toxic, on the contrary, it contains a large amount of medicinal properties, so it is safe...but be careful, it is addictive. You can chew the leaves as they are to enjoy the flavor and provide nicotine. If they are of good quality, they can help you quit smoking. \\n# ~Sickly Taste of Smoke~'):
        "Una pianta parente della melanzana. La lavorano in tanti modi e serve per fumare. Nell'antichità faceva male, ma nell'era della civiltà biochimica l'hanno migliorata. La specie di oggi non è velenosa, anzi ha dentro molte sostanze che curano, quindi si sta tranquilli... o quasi: dà dipendenza, e va tenuto a mente. Anche masticando la foglia così com'è si sente il sapore e si prende la nicotina. Se è di buona qualità può perfino aiutare a smettere. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",

    # ---------------------------------------------------------- :61310
    (61310, 'It is not a copper coin because it is made of bronze, not pure copper. It was created for those who want to show their appreciation but do not have enough money to pay platinum coins. They have only recently come into circulation and are still less familiar than platinum coins. \\n# ~Coins of this World - Tyris Edition~'):
        "Non è una moneta di rame, perché è fatta di bronzo e non di rame puro. L'hanno pensata per quando si vuole dire grazie ma non al punto di tirare fuori una moneta di platino. Ha cominciato a girare da poco, e rispetto alla moneta di platino è ancora poco familiare. \\n# ~Le Monete del Mondo: Tyris~",

# 36 voci, 0 ambigue

    # ---------------------------------------------------------- :61312
    (61312, '\\"I was surprised when I found out we have bronze coins over here.\\" \\n# ~words of <Norne> the guide~'):
        "\\\"Quando ho scoperto che anche da queste parti c'erano le monete di bronzo mi sono stupita.\\\" \\n# ~Parole di <Norne> la guida~",

# 4 voci, 0 ambigue
}
