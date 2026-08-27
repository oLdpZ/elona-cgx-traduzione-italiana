import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :55676
    (55676, 'It is a porcelain doll. If infused with mana, you can make it an ally.'):
        "Una bambola di porcellana: usandola diventa una compagna.",

    # ---------------------------------------------------------- :55738
    (55738, 'It is a magnificent pottery.'):
        "Una ceramica magnifica.",

    # ---------------------------------------------------------- :55800
    (55800, 'It is a curious pottery.'):
        "Una ceramica bizzarra.",

    # ---------------------------------------------------------- :57449
    (57449, '(Autoused) tool pendulum that looks like the God of Earth.'):
        "Un pendolo del dio della terra. Si usa da sé se lo porti.",

    # ---------------------------------------------------------- :57511
    (57511, 'It is a stuffed doll of God of the Harvest. Useful when placed in farm.'):
        "Un peluche del dio del raccolto. Fa effetto se sta nel campo.",

    # ---------------------------------------------------------- :57710
    (57710, '(Autoused) Bust Statue of the God of Element.'):
        "Un busto del dio degli elementi. Si usa da sé se lo porti.",

    # ---------------------------------------------------------- :57772
    (57772, 'It is a painting of Goddess of Luck. Effective when placed in the house.'):
        "Un dipinto della dea della fortuna. Fa effetto se sta in casa.",

    # ---------------------------------------------------------- :57834
    (57834, '(Autoused) alarm clock in the shape of the God of Machine.'):
        "Una sveglia del dio delle macchine. Si usa da sé se lo porti.",

    # ---------------------------------------------------------- :60000
    (60000, 'It is an ornamental plant.'):
        "Una pianta ornamentale.",

    # ---------------------------------------------------------- :63872
    (63872, '(Reusable) tool that juices fruits, vegetables, nuts.'):
        "Un mobile che fa succo di frutta, verdura e frutti a guscio.",

    # ---------------------------------------------------------- :65334
    (65334, '(Reusable) Rank 5 bed, hugging this makes you feel lonely at night.'):
        "Un letto (rango 5). Chi lo tiene a volte viene a dormirti accanto.",

    # ---------------------------------------------------------- :66388
    (66388, 'It is a mysterious statue.'):
        "Una statua misteriosa.",

    # ---------------------------------------------------------- :66454
    (66454, "It is a golem that hasn't been activated. Infuse with mana to activate."):
        "Un golem non attivato: usandolo diventa un compagno.",

    # ---------------------------------------------------------- :66516
    (66516, 'It is an austere statue.'):
        "Una statua austera.",

    # ---------------------------------------------------------- :66578
    (66578, 'It is an solemn statue.'):
        "Una statua solenne.",

    # ---------------------------------------------------------- :66706
    (66706, 'It is a shed for small animals.'):
        "Una casetta per i piccoli animali.",

    # ---------------------------------------------------------- :68851
    (68851, '(Reusable) Rank 1 instrument for performing.'):
        "Uno strumento per suonare. Si può usare sempre.",

    # ---------------------------------------------------------- :68916
    (68916, '(Reusable) Rank 2 instrument for performing.'):
        "Uno strumento per suonare. Si può usare sempre.",

    # ---------------------------------------------------------- :68981
    (68981, '(Reusable) Rank 3 instrument for performing.'):
        "Uno strumento per suonare. Si può usare sempre.",

    # ---------------------------------------------------------- :70130
    (70130, 'It is a miniature of a Eulderna Blimp.'):
        "Una miniatura di una nave magica.",

    # ---------------------------------------------------------- :72825
    (72825, 'It is a statue of a guardian dog.'):
        "Una statua a forma di koma-inu.",

    # ---------------------------------------------------------- :73355
    (73355, '(Reusable) chair.'):
        "Si può usare sempre al posto di una sedia.",

    # ---------------------------------------------------------- :74571
    (74571, '(Reusable) Rank 4 instrument for performing.'):
        "Uno strumento per suonare. Si può usare sempre.",

    # ---------------------------------------------------------- :76523
    (76523, 'It is a magnificent castle made of sand.'):
        "Un bel castello fatto di sabbia.",

    # ---------------------------------------------------------- :78792
    (78792, 'It is a flat vessel on which food is placed.'):
        "Un recipiente piatto su cui si posa il cibo.",

    # ---------------------------------------------------------- :78922
    (78922, 'It is furniture made from processed beasts.'):
        "Un mobile ricavato da una bestia.",

    # ---------------------------------------------------------- :79047
    (79047, '(Reusable) chair.'):
        "Un mobile per sedersi. Si può usare sempre.",

    # ---------------------------------------------------------- :79306
    (79306, 'It is an expensive cupboard.'):
        "Un armadietto costoso.",

    # ---------------------------------------------------------- :79369
    (79369, '(Openable) large bookshelf for up to 100 different types of books.'):
        "Una libreria grande. Ci stanno fino a 100 tipi di libri.",

    # ---------------------------------------------------------- :79639
    (79639, 'It is a small fir tree.'):
        "Un piccolo abete.",

    # ---------------------------------------------------------- :79701
    (79701, 'It is a solemn decoration made for the New Year.'):
        "Un ornamento solenne fatto per il capodanno.",

    # ---------------------------------------------------------- :79767
    (79767, '(Reusable) Rank 0 bed that allows you to have good dreams.'):
        "Un cuscino da bei sogni (rango 0). Si può usare sempre.",

    # ---------------------------------------------------------- :79829
    (79829, 'It is a simple store for festivities.'):
        "Un negozietto per le feste.",

    # ---------------------------------------------------------- :79953
    (79953, 'It is a desk for the store.'):
        "Un tavolo da negozio.",

    # ---------------------------------------------------------- :80015
    (80015, 'It is a raised platform.'):
        "Una piattaforma rialzata.",

    # ---------------------------------------------------------- :80085
    (80085, 'It is a crown made for a special occasion.'):
        "Una corona fatta per un giorno speciale.",

    # ---------------------------------------------------------- :80152
    (80152, '(Reusable) Rank 5 instrument that makes people drunk.'):
        "Uno strumento che inebria il pubblico. Si può usare sempre.",

    # ---------------------------------------------------------- :80615
    (80615, 'It is an uniquely shaped doll.'):
        "Una bambola dalla forma unica.",

    # ---------------------------------------------------------- :80677
    (80677, 'It is a desk for cold weather. You can hide under it.'):
        "Un tavolo per la stagione fredda. Ci si può infilare sotto.",

    # ---------------------------------------------------------- :80801
    (80801, 'These are stone steps to descend. You can go downstairs here.'):
        "Gradini di pietra per scendere. Ci si può passare.",

    # ---------------------------------------------------------- :80863
    (80863, 'These are stone steps to ascend. You can go upstairs here.'):
        "Gradini di pietra per salire. Ci si può passare.",

    # ---------------------------------------------------------- :82278
    (82278, "It is a gift given to raise affection, won't be returned."):
        "Dato a qualcuno, alza la simpatia.",

    # ---------------------------------------------------------- :82878
    (82878, '(Reusable) Rank 9 bed of luxury quality.'):
        "Un letto eccellente (rango 9). Si può usare sempre.",

    # ---------------------------------------------------------- :83767
    (83767, '(Reusable) Rank 4 instrument that increases the rewords of performing.'):
        "Suonandolo si prendono mance migliori. Si può usare sempre.",

    # ---------------------------------------------------------- :84647
    (84647, 'It is a space divider.'):
        "Un pannello che divide lo spazio.",

    # ---------------------------------------------------------- :87005
    (87005, 'It is an eastern-style partition.'):
        "Un paravento in stile orientale.",

    # ---------------------------------------------------------- :87067
    (87067, 'It is an exotic lighting. Illuminates the surroundings softly at night.'):
        "Un lume semplice straniero. Di notte fa una luce fioca.",

    # ---------------------------------------------------------- :87129
    (87129, 'It is a circular window. Illuminates the surroundings softly at night.'):
        "Una finestra tonda. Di notte fa una luce fioca.",

    # ---------------------------------------------------------- :87191
    (87191, 'It is an exotic heavy lighting. Always illuminates the surroundings.'):
        "Un lume straniero e pesante. Illumina sempre intorno.",

    # ---------------------------------------------------------- :87322
    (87322, '(Reusable) Rank 7 bed.'):
        "Un letto (rango 7). Si può usare sempre.",

    # ---------------------------------------------------------- :87384
    (87384, 'It is useless junk.'):
        "Non serve a niente in particolare.",

    # ---------------------------------------------------------- :87446
    (87446, 'It is a large sink. Cannot be used.'):
        "Un grande lavello. Non si può usare.",

    # ---------------------------------------------------------- :87508
    (87508, 'It is a cupboard made by a master craftsman.'):
        "Una credenza fatta da un maestro artigiano.",

    # ---------------------------------------------------------- :87647
    (87647, 'It is a beautiful bed of flowers, with a partition.'):
        "Un'aiuola con una recinzione.",

    # ---------------------------------------------------------- :87710
    (87710, '(Reusable) sofa.'):
        "Un mobile per sedersi. Si può usare sempre.",

    # ---------------------------------------------------------- :87772
    (87772, 'It is a board that is free to write on and erase. Cannot be used.'):
        "Una tavola su cui scrivere e cancellare. Non si può usare.",

    # ---------------------------------------------------------- :87834
    (87834, 'It is a menu for a restaurant.'):
        "Una tavola con scritto il menù.",

    # ---------------------------------------------------------- :87896
    (87896, "It is a king's royal cabinet."):
        "Una cassettiera da re.",

    # ---------------------------------------------------------- :87958
    (87958, 'It is a window with partitions. illuminates the surroundings softly.'):
        "Una finestra con un divisorio. Di notte fa una luce fioca.",

    # ---------------------------------------------------------- :88086
    (88086, 'It is a barrel for holding rice.'):
        "Un sacco pieno di granaglie.",

    # ---------------------------------------------------------- :88806
    (88806, '(Single-use) tool that oepns a gateway to the showroom world.'):
        "Un cancello per la sala d'esposizione (usa e getta).",

    # ---------------------------------------------------------- :89215
    (89215, 'It is a gate for Gods of foreign lands.'):
        "Un portale che accoglie le divinità straniere.",

    # ---------------------------------------------------------- :89949
    (89949, 'It is an arch structure decorated with flowers.'):
        "Una costruzione a semicerchio ornata di fiori.",

    # ---------------------------------------------------------- :90015
    (90015, '(Reusable) Rank 8 bed made for royalty.'):
        "Un letto da re, eccellente (rango 8). Si può usare.",

    # ---------------------------------------------------------- :90077
    (90077, 'It is a furniture that sheds light. Illuminates surroundings softly.'):
        "Fa entrare la luce da fuori. Di notte fa una luce fioca.",

    # ---------------------------------------------------------- :90202
    (90202, 'It is a tree was trimmed at an angle.'):
        "Un albero potato ad angolo.",

    # ---------------------------------------------------------- :90388
    (90388, 'It is an ornamental potted plant.'):
        "Una pianta ornamentale in vaso.",

    # ---------------------------------------------------------- :90452
    (90452, 'It is a cooking tool allowing the preparation of dishes up to Rank 9.'):
        "Ci si cucinano i piatti fino al rango 9.",

    # ---------------------------------------------------------- :90640
    (90640, '(Reusable) rare chair.'):
        "Un mobile per sedersi. Si può usare sempre.",

    # ---------------------------------------------------------- :91091
    (91091, 'It is a furniture that lets in light, illuminates surroundings softly.'):
        "Fa entrare la luce da fuori. Di notte fa una luce un po' fioca.",

    # ---------------------------------------------------------- :91153
    (91153, 'It is a heavy pillar.'):
        "Una colonna pesante.",

    # ---------------------------------------------------------- :91215
    (91215, 'It is a great gleaming cross from ancient times.'):
        "Una grande croce splendente.",

    # ---------------------------------------------------------- :91277
    (91277, 'It is equipped with a light. Illuminates the surroundings brightly.'):
        "Un lume fisso. Di notte fa una luce viva.",

    # ---------------------------------------------------------- :91339
    (91339, 'It is a snow-covered container that holds liquid. Cannot be used.'):
        "Un recipiente per liquidi, coperto di neve. Non si può usare.",

    # ---------------------------------------------------------- :91401
    (91401, 'It is a small snowman made of snow.'):
        "Un pupazzo di neve piccolo.",

    # ---------------------------------------------------------- :91783
    (91783, 'It is an artisan lighting. Illuminates the surroundings brightly.'):
        "Un lume d'artista famoso. Di notte fa una luce viva.",

    # ---------------------------------------------------------- :91845
    (91845, 'It is a simple lighting made of wax. Always illuminates the surroundings.'):
        "Un lume semplice di cera. Illumina sempre intorno.",

    # ---------------------------------------------------------- :92127
    (92127, 'It is a common shelf.'):
        "Uno scaffale comune.",

    # ---------------------------------------------------------- :94804
    (94804, 'It is a snowman made of snow.'):
        "Una statua fatta di neve.",

    # ---------------------------------------------------------- :94866
    (94866, 'It is a giant black crystal.'):
        "Un enorme minerale nero.",

    # ---------------------------------------------------------- :94928
    (94928, 'It is a pillar in the shape of a cat.'):
        "Una colonna a forma di gatto.",

    # ---------------------------------------------------------- :94990
    (94990, 'It is a painting of a sunflower.'):
        "C'è dipinta una pianta.",

    # ---------------------------------------------------------- :95052
    (95052, 'It is a painting of a landscape.'):
        "C'è dipinto un paesaggio.",

    # ---------------------------------------------------------- :95114
    (95114, 'It is a painting of a lady.'):
        "C'è dipinta una donna.",

    # ---------------------------------------------------------- :95177
    (95177, '(Reusable) very large desk.'):
        "Un tavolo molto grande. Si può usare sempre.",

    # ---------------------------------------------------------- :95301
    (95301, 'It is a stove useful for cooking food. Cannot be used.'):
        "Un forno per cuocere. Non si può usare.",

    # ---------------------------------------------------------- :95363
    (95363, 'It is furniture that warms the room.'):
        "Un mobile che scalda la stanza.",

    # ---------------------------------------------------------- :95425
    (95425, 'It is a metal-warming structure.'):
        "Una costruzione che scalda il metallo.",

    # ---------------------------------------------------------- :97876
    (97876, 'It is a disk that do not contain data. Cannot be used.'):
        "Un disco senza dati dentro. Non si può usare.",

    # ---------------------------------------------------------- :97946
    (97946, 'It is some kind of information piece.'):
        "Un frammento di informazioni.",

    # ---------------------------------------------------------- :98008
    (98008, 'It is a container for dumping the cans.'):
        "Una scatola dove buttare le lattine.",

    # ---------------------------------------------------------- :98078
    (98078, 'It is a box to put something in.'):
        "Una scatola dove mettere qualcosa.",

    # ---------------------------------------------------------- :98148
    (98148, 'It is a box used to hold information.'):
        "Una scatola dove mettere informazioni.",

    # ---------------------------------------------------------- :98218
    (98218, 'It is a broken cookware. Cannot be used.'):
        "Un attrezzo da cucina rotto. Non si può usare.",

    # ---------------------------------------------------------- :98288
    (98288, 'It is a tool for photographing a subject. It cannot be used.'):
        "Uno strumento che ritrae un soggetto. Non si può usare.",

    # ---------------------------------------------------------- :98359
    (98359, '(Reusable) tool that trains your primary attributes.'):
        "Allena gli attributi base. Si può usare sempre.",

    # ---------------------------------------------------------- :98429
    (98429, 'These are ancient minds.'):
        "Un cervello antico.",

    # ---------------------------------------------------------- :98499
    (98499, 'It is an object that is irregular flickering and periodic strange noises.'):
        "Lampeggia a caso e fa uno strano rumore a intervalli.",

    # ---------------------------------------------------------- :103363
    (103363, '(Reusable) treasure machine that produces gacha balls.'):
        "Una macchina che sputa sfere del tesoro. Si può usare sempre.",

    # ---------------------------------------------------------- :108396
    (108396, '(Single-use) tool that oepns a gateway to the showroom world.'):
        "Serve ad andare nella sala d'esposizione (usa e getta).",

    # ---------------------------------------------------------- :108832
    (108832, 'It is a very flashy statue.'):
        "Una statua molto vistosa.",

    # ---------------------------------------------------------- :108894
    (108894, 'It is a pedestal decorated with gold. Illuminates surroundings brightly.'):
        "Un piedistallo per candele. Di notte fa una luce viva.",

    # ---------------------------------------------------------- :108957
    (108957, '(Reusable) royal chair.'):
        "Un mobile per sedersi. Si può usare sempre.",

    # ---------------------------------------------------------- :109086
    (109086, '(Reusable) common table that allows one to author books.'):
        "Un piano con le gambe per lavorarci. Si può usare sempre.",

    # ---------------------------------------------------------- :109148
    (109148, 'These are clothing bright to the eye. Cannot be equipped.'):
        "Un abito dai colori vivaci. Non si può equipaggiare.",

    # ---------------------------------------------------------- :109273
    (109273, 'It is a symbolic structure.'):
        "Una costruzione simbolica.",

    # ---------------------------------------------------------- :109401
    (109401, '(Reusable) wide chair.'):
        "Una sedia larga. Si può usare sempre.",

    # ---------------------------------------------------------- :109463
    (109463, 'It is a neat shelf.'):
        "Uno scaffale lineare.",

    # ---------------------------------------------------------- :109529
    (109529, '(Reusable) Rank 4 bed.'):
        "Un letto (rango 4). Si può usare sempre.",

    # ---------------------------------------------------------- :109591
    (109591, 'It is a small altar, cannot be used.'):
        "Un piccolo altare. Non si può usare.",

    # ---------------------------------------------------------- :109653
    (109653, 'It is a large cupboard that holds a lot of dishes.'):
        "Una credenza piuttosto grande.",

    # ---------------------------------------------------------- :109716
    (109716, '(Reusable) dresser used to adjust your clothes.'):
        "Uno specchio per guardarsi. Si può usare sempre.",

    # ---------------------------------------------------------- :109778
    (109778, 'It is a rack with a framed set of glass doors.'):
        "Uno scaffale pulito e ordinato.",

    # ---------------------------------------------------------- :109840
    (109840, 'It is table made out of recycled wood.'):
        "Un tavolo sbilenco.",

    # ---------------------------------------------------------- :109906
    (109906, '(Reusable) Rank 0 bed made out of recycled parts...'):
        "Un letto (rango 0). Si può usare sempre.",

    # ---------------------------------------------------------- :109969
    (109969, '(Openable) shelf for up to 100 different types of books.'):
        "Una libreria vecchia. Ci stanno fino a 100 tipi di libri.",

    # ---------------------------------------------------------- :110031
    (110031, 'It is a dusty shelf.'):
        "Uno scaffale pieno di polvere.",

    # ---------------------------------------------------------- :110093
    (110093, 'It is an ornamental plant.'):
        "Una pianta ornamentale in vaso.",

    # ---------------------------------------------------------- :110158
    (110158, '(Reusable) game machine that is used to play darts.'):
        "Un tavolo da gioco a lanci. Si può usare sempre.",

    # ---------------------------------------------------------- :110223
    (110223, '(Reusable) game machine that is used to play slots.'):
        "Un tavolo da gioco a numeri. Si può usare sempre.",

    # ---------------------------------------------------------- :110288
    (110288, '(Reusable) game machine that is used to play all sorts of games.'):
        "Un tavolo con giochi di ogni tipo. Si può usare sempre.",

    # ---------------------------------------------------------- :110353
    (110353, '(Reusable) game machine that is used to play pachinko.'):
        "Un tavolo da gioco a pallini. Si può usare sempre.",

    # ---------------------------------------------------------- :110415
    (110415, 'It is a porcelan bathtub. Cannot be used.'):
        "Un mobile pieno d'acqua. Non si può usare.",

    # ---------------------------------------------------------- :110544
    (110544, '(Reusable) common dresser.'):
        "Uno specchio per guardarsi. Si può usare sempre.",

    # ---------------------------------------------------------- :110606
    (110606, 'It is an ordinary inexpensive rack.'):
        "Uno scaffale spartano.",

    # ---------------------------------------------------------- :110672
    (110672, '(Reusable) Rank 4 soft bed meant for a child.'):
        "Un letto (rango 4). Si può usare sempre.",

    # ---------------------------------------------------------- :110736
    (110736, 'It is a cooking tool allowing the preparation of dishes up to Rank 8.'):
        "Ci si cucinano i piatti fino al rango 8.",

    # ---------------------------------------------------------- :110868
    (110868, '(Reusable) Rank 1 bed.'):
        "Un letto (rango 1). Si può usare sempre.",

    # ---------------------------------------------------------- :110934
    (110934, '(Reusable) Rank 3, large and elegant bed.'):
        "Un letto (rango 3). Si può usare sempre.",

    # ---------------------------------------------------------- :110996
    (110996, 'It is a clean set of clothing.'):
        "Una cassettiera per i vestiti.",

    # ---------------------------------------------------------- :111128
    (111128, "It is a bar table with rack's of alchohol and wine."):
        "Un armadietto che tiene molta roba.",

    # ---------------------------------------------------------- :111191
    (111191, '(Reusable) beautifully crafted dresser.'):
        "Uno specchio costoso per guardarsi. Si può usare sempre.",

    # ---------------------------------------------------------- :111261
    (111261, 'It is a vase of high artistic quality on a night stand.'):
        "Un vaso fatto di buon materiale.",

    # ---------------------------------------------------------- :111327
    (111327, '(Reusable) Rank 6 bed.'):
        "Un letto (rango 6). Si può usare sempre.",

    # ---------------------------------------------------------- :111389
    (111389, 'It is a cupboard for liquor.'):
        "Un armadietto per i liquori.",

    # ---------------------------------------------------------- :111452
    (111452, '(Reusable) rustic table.'):
        "Un tavolo storto. Si può usare sempre.",

    # ---------------------------------------------------------- :111514
    (111514, 'It is towel made of cotton.'):
        "Un tessuto fatto di cotone.",

    # ---------------------------------------------------------- :111576
    (111576, 'It is a shelf on which ornaments are placed.'):
        "Uno scaffale con sopra dei soprammobili.",

    # ---------------------------------------------------------- :111638
    (111638, 'It is a shelf on which commodity are placed.'):
        "Uno scaffale con sopra roba di tutti i giorni.",

    # ---------------------------------------------------------- :111700
    (111700, 'It is oiled and polished decorative armor.'):
        "Un'armatura in ordine. Non si può equipaggiare.",

    # ---------------------------------------------------------- :112323
    (112323, 'It is an atmospheric map. Not available for use.'):
        "Una mappa suggestiva. Non si può usare.",

    # ---------------------------------------------------------- :112385
    (112385, 'It is a life-saving item.'):
        "Uno strumento di salvataggio.",

    # ---------------------------------------------------------- :112448
    (112448, 'It is a chic desk.'):
        "Un tavolo sobrio.",

    # ---------------------------------------------------------- :112510
    (112510, 'It is a very heavy tub of water.'):
        "Una tinozza d'acqua, pesantissima.",

    # ---------------------------------------------------------- :112634
    (112634, 'It is a broken pillar. It is very heavy.'):
        "Una colonna spezzata. È pesantissima.",

    # ---------------------------------------------------------- :112696
    (112696, 'It is a long and thick pillar. It is very heavy.'):
        "Una colonna lunga e grossa. È pesantissima.",

    # ---------------------------------------------------------- :115323
    (115323, 'It is a model of a sword.'):
        "La riproduzione di una spada.",

    # ---------------------------------------------------------- :115385
    (115385, 'It is a model of a berserker.'):
        "La riproduzione di un berserker.",

    # ---------------------------------------------------------- :118646
    (118646, 'It is a stack of decorative dishes.'):
        "Piatti impilati.",

    # ---------------------------------------------------------- :119690
    (119690, '(Reusable) Rank 2 makeshift bunk bed.'):
        "Un letto (rango 2). Si può usare sempre.",

    # ---------------------------------------------------------- :119946
    (119946, 'It is a very heavy ancient Norland style tomb.'):
        "Una costruzione molto pesante.",

    # ---------------------------------------------------------- :120008
    (120008, 'It is a very heavy ancient Eulderna style tomb.'):
        "Una costruzione molto pesante.",

    # ---------------------------------------------------------- :120070
    (120070, 'It is a very heavy tomb of a heroic figure.'):
        "Una costruzione molto pesante.",

    # ---------------------------------------------------------- :120132
    (120132, 'It is a recent grave... The name is still readable.'):
        "Una costruzione molto pesante.",

    # ---------------------------------------------------------- :120194
    (120194, 'It is a grave with flowers for the departed.. The name is still readable.'):
        "Una costruzione molto pesante.",

    # ---------------------------------------------------------- :120256
    (120256, 'It is a common style grave that has been destroyed.'):
        "Una costruzione molto pesante.",

    # ---------------------------------------------------------- :120318
    (120318, 'It is a common style grave that has started to crumble.'):
        "Una costruzione molto pesante.",

    # ---------------------------------------------------------- :120380
    (120380, 'It is woven threads. Cannot be used.'):
        "Fili tessuti insieme. Non si può usare.",

    # ---------------------------------------------------------- :120442
    (120442, 'These are scattered clothes. Cannot be used.'):
        "Vestiti sparsi. Non si può usare.",

    # ---------------------------------------------------------- :120636
    (120636, 'It is a simple shelf for your dining room.'):
        "Uno scaffale semplice.",

    # ---------------------------------------------------------- :120698
    (120698, 'It is a beautiful candelabra. Illuminates surroundings brightly.'):
        "Un candelabro lavorato con arte. Di notte fa una luce viva.",

    # ---------------------------------------------------------- :120760
    (120760, 'It is a table for nobles.'):
        "Un tavolo da nobili.",

    # ---------------------------------------------------------- :120822
    (120822, 'It is a narrow desk made for dining.'):
        "Un tavolo stretto fatto per mangiare.",

    # ---------------------------------------------------------- :120886
    (120886, 'It is a cooking tool allowing the preparation of dishes up to Rank 6.'):
        "Ci si cucinano i piatti fino al rango 6.",

    # ---------------------------------------------------------- :121076
    (121076, 'It is some unhandled, damaged liquor. Cannot be used.'):
        "Liquore andato a male, e in quantità. Non si può usare.",

    # ---------------------------------------------------------- :121139
    (121139, '(Openable) craftsman bookshelf for up to 100 different types of books.'):
        "Una libreria da maestro. Ci stanno fino a 100 tipi di libri.",

    # ---------------------------------------------------------- :121201
    (121201, 'It is a nicely crafted piece of cabinet.'):
        "Una cassettiera fatta da un maestro.",

    # ---------------------------------------------------------- :121263
    (121263, 'These are stacked books. Cannot be used.'):
        "Libri impilati. Non si può usare.",

    # ---------------------------------------------------------- :121325
    (121325, 'These are scattered books. Cannot be used.'):
        "Libri sparsi. Non si può usare.",

    # ---------------------------------------------------------- :121387
    (121387, 'It is a statue in full body armor. It cannot be equipped.'):
        "Una statua in armatura completa. Non si può equipaggiare.",

    # ---------------------------------------------------------- :121449
    (121449, 'It is a statue in full body armor for display. Cannot be equipped.'):
        "Un'armatura da esposizione. Non si può equipaggiare.",

    # ---------------------------------------------------------- :121511
    (121511, 'It is a decorative cloth for display. Cannot be equipped.'):
        "Un abito da esposizione. Non si può equipaggiare.",

    # ---------------------------------------------------------- :121573
    (121573, 'It is bundled weapons for display. Cannot be equipped.'):
        "Armi legate in fascio. Non si può equipaggiare.",

    # ---------------------------------------------------------- :121635
    (121635, 'It is bundled bows for display. Cannot be equipped.'):
        "Archi impilati. Non si può equipaggiare.",

    # ---------------------------------------------------------- :121770
    (121770, '(Readable) drawn map of the continent. '):
        "Una mappa del continente. Si può leggere. ",

    # ---------------------------------------------------------- :121894
    (121894, 'It is a pillar decorated with flowers. It is very heavy.'):
        "Una colonna con sopra dei fiori.",

    # ---------------------------------------------------------- :121956
    (121956, 'It is a pillar decorated with plants. It is very heavy.'):
        "Una colonna con sopra delle piante.",

    # ---------------------------------------------------------- :122616
    (122616, 'It is a magical circles drawn on the ground.'):
        "Un cerchio disegnato per terra.",

    # ---------------------------------------------------------- :122744
    (122744, 'It is a special bottle for liquids. Cannot be used.'):
        "Una bottiglia speciale per i liquidi. Non si può usare.",

    # ---------------------------------------------------------- :122887
    (122887, '(Openable) shelf for displaying up to 20 different types of bread.'):
        "Uno scaffale per il pane. Ci stanno fino a 20 tipi di pane.",

    # ---------------------------------------------------------- :123557
    (123557, 'It is a board with information written on it. Cannot be used or read.'):
        "Una tavola con delle informazioni. Non si può leggere.",

    # ---------------------------------------------------------- :123619
    (123619, 'It is a board that points in an unknown direction.'):
        "Una tavola che indica una direzione ignota.",

    # ---------------------------------------------------------- :123681
    (123681, 'It is a board for a landmark.'):
        "Una tavola che fa da segnale.",

    # ---------------------------------------------------------- :123745
    (123745, 'It is a cooking tool allowing the preparation of dishes up to Rank 7.'):
        "Ci si cucinano i piatti fino al rango 7.",

    # ---------------------------------------------------------- :123807
    (123807, 'It is a furnace with hot metal. Illuminates the surroundings brightly.'):
        "Un forno col metallo incandescente. Illumina sempre di luce viva.",

    # ---------------------------------------------------------- :123869
    (123869, 'It is a small shelf with clothes on it. Cannot be used.'):
        "Un ripiano con sopra dei vestiti. Non si può usare.",

    # ---------------------------------------------------------- :124001
    (124001, 'It is a small shelf with commodities on it. Cannot be used.'):
        "Un ripiano con sopra delle cianfrusaglie. Non si può usare.",

    # ---------------------------------------------------------- :124063
    (124063, 'It is a small shelf with items on it. Cannot be used.'):
        "Un ripiano con sopra degli attrezzi. Non si può usare.",

    # ---------------------------------------------------------- :124125
    (124125, 'It is a closet for storing items.'):
        "Uno scaffale per riporre le cose.",

    # ---------------------------------------------------------- :124187
    (124187, 'It is a shelf with a book stand.'):
        "Uno scaffale con un reggilibri.",

    # ---------------------------------------------------------- :124249
    (124249, 'It is a furniture for packing things. Cannot be used. '):
        "Un mobile dove stipare le cose. Non si può usare. ",

    # ---------------------------------------------------------- :124311
    (124311, 'It is a cupboard to store dishes.'):
        "Uno scaffale per riporre le stoviglie.",

    # ---------------------------------------------------------- :124374
    (124374, '(Reusable) stool.'):
        "Un mobile per sedersi. Si può usare sempre.",

    # ---------------------------------------------------------- :124437
    (124437, '(Reusable) everyday chair.'):
        "Un mobile per sedersi. Si può usare sempre.",

    # ---------------------------------------------------------- :124500
    (124500, '(Openable) rack for up to 60 different types of potions.'):
        "Uno scaffale per le pozioni. Ci stanno fino a 60 tipi.",

    # ---------------------------------------------------------- :124563
    (124563, '(Reusable) desk for study.'):
        "Un tavolo fatto per studiare. Si può usare sempre.",

    # ---------------------------------------------------------- :124625
    (124625, 'It is an open-mouthed crucible. Cannot be used.'):
        "Un vaso con la bocca aperta. Non si può usare.",

    # ---------------------------------------------------------- :124687
    (124687, 'It is an sealed-shut crucible. Cannot be used.'):
        "Un vaso con la bocca chiusa. Non si può usare.",

    # ---------------------------------------------------------- :124749
    (124749, 'It is an anvil used for blacksmithing.'):
        "Un banco per raffinare i metalli.",

    # ---------------------------------------------------------- :124811
    (124811, 'It is a set of splendid armor for display. Cannot be equipped.'):
        "Una bella armatura. Non si può equipaggiare.",

    # ---------------------------------------------------------- :124873
    (124873, 'It is a portable lightsource. Illuminates surroundings slightly at night.'):
        "Un lume facile da portare. Di notte fa una luce abbastanza viva.",

    # ---------------------------------------------------------- :124935
    (124935, 'It is a pick originally used for mining, cannot be used.'):
        "Uno strumento da scavo. Non si può usare.",

    # ---------------------------------------------------------- :124998
    (124998, '(Reusable) beautifully crafted chair.'):
        "Una sedia lavorata con arte. Si può usare sempre.",

    # ---------------------------------------------------------- :125060
    (125060, 'It is a container that holds liquid. Cannot be used.'):
        "Un recipiente per i liquidi. Non si può usare.",

    # ---------------------------------------------------------- :125122
    (125122, 'It is a table for a bar.'):
        "Un tavolo da osteria.",

    # ---------------------------------------------------------- :125249
    (125249, '(Reusable) Rank 5, very heavy instrument for performing.'):
        "Uno strumento enorme e pesantissimo. Si può usare sempre.",

    # ---------------------------------------------------------- :125311
    (125311, 'It is a display case for various gift items.'):
        "Un ripiano con esposti dei soprammobili.",

    # ---------------------------------------------------------- :125373
    (125373, 'It is a display case for various commodities.'):
        "Un ripiano con esposte delle cianfrusaglie.",

    # ---------------------------------------------------------- :125435
    (125435, 'It is a shelf of armor on display. Cannot be equipped.'):
        "Un ripiano con esposte delle armature.",

    # ---------------------------------------------------------- :125497
    (125497, 'It is a table made for eating.'):
        "Un tavolo fatto per mangiare.",

    # ---------------------------------------------------------- :125560
    (125560, 'It is a table made with modern Yerles technology.'):
        "Un tavolo all'ultima moda. Si può usare sempre.",

    # ---------------------------------------------------------- :125622
    (125622, "It is a child's toy."):
        "Un gioco per bambini.",

    # ---------------------------------------------------------- :125685
    (125685, '(Reusable) fluffy doll.'):
        "Una bambola morbidissima. Si può usare sempre.",

    # ---------------------------------------------------------- :125751
    (125751, '(Reusable) Rank 1 refurbished bed.'):
        "Un letto (rango 1). Si può usare sempre.",

    # ---------------------------------------------------------- :125813
    (125813, 'It is a cabinet made of fine materials.'):
        "Una cassettiera di buon materiale.",

    # ---------------------------------------------------------- :125876
    (125876, '(Openable) simple shelf for up to 100 different types of books.'):
        "Una libreria comune. Ci stanno fino a 100 tipi di libri.",

    # ---------------------------------------------------------- :125939
    (125939, '(Reusable) small chair.'):
        "Un mobile per sedersi. Si può usare sempre.",

    # ---------------------------------------------------------- :127610
    (127610, 'It is a stone slab with letters written on it.'):
        "Una lastra di pietra con delle scritte.",

# 218 voci, 0 ambigue
}
