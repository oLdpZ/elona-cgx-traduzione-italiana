import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :42418
    (42418, '(Reusable) Dart rifle that tranquilizes target weight 500-1000 kg.'):
        "Fucile anestetico: l'effetto varia col peso. Si usa più volte.",

    # ---------------------------------------------------------- :42494
    (42494, '(Reusable) Dart rifle that tranquilizes target weight 100-500 kg.'):
        "Fucile anestetico: l'effetto varia col peso. Si usa più volte.",

    # ---------------------------------------------------------- :42570
    (42570, '(Reusable) Dart rifle that tranquilizes target weight 30-100 kg.'):
        "Fucile anestetico: l'effetto varia col peso. Si usa più volte.",

    # ---------------------------------------------------------- :42646
    (42646, '(Reusable) Dart rifle that tranquilizes target weight <30 kg.'):
        "Fucile anestetico: l'effetto varia col peso. Si usa più volte.",

    # ---------------------------------------------------------- :42712
    (42712, '(Single-use) chopsticks.'):
        "Bacchette di legno. Si usa (usa e getta).",

    # ---------------------------------------------------------- :43243
    (43243, "(Reusable) Magical item that changes one's form."):
        "Dà un altro aspetto, a chiunque. Si può usare sempre.",

    # ---------------------------------------------------------- :44100
    (44100, '(Reusable) tool cage that capture and transport a defeated victim.'):
        "Ci si porta via chi è in fin di vita o inerme. Si usa sempre.",

    # ---------------------------------------------------------- :44166
    (44166, '(Reusable) tool that generates work energy using human labor.'):
        "Genera energia da lavoro a forza di braccia. Si può usare sempre.",

    # ---------------------------------------------------------- :45484
    (45484, '(Reusable) tool that set up traps.'):
        "Una pietra che piazza trappole. Si può usare sempre.",

    # ---------------------------------------------------------- :45550
    (45550, '(Single-use) tool used to gain AP.'):
        "Una pietra che dà AP. Si usa (usa e getta).",

    # ---------------------------------------------------------- :45616
    (45616, '(Single-use) tool used to restore mana.'):
        "Una pietra che dà magia e MP. Si usa (usa e getta).",

    # ---------------------------------------------------------- :45682
    (45682, '(Single-use) tool used to restore stamina.'):
        "Una pietra che dà costituzione e SP. Si usa (usa e getta).",

    # ---------------------------------------------------------- :45748
    (45748, '(Single-use) tool used to increase your resistance.'):
        "Alza tutte le resistenze fino a un limite. Si usa (usa e getta).",

    # ---------------------------------------------------------- :45814
    (45814, '(Single-use) tool used to increase your DV modifier.'):
        "Alza il modificatore DV. Si usa (usa e getta).",

    # ---------------------------------------------------------- :45880
    (45880, '(Single-use) tool used to increase your PV modifier.'):
        "Alza il modificatore PV. Si usa (usa e getta).",

    # ---------------------------------------------------------- :45947
    (45947, '(Single-use) exo-skeleton upgrade kit for your Potioman.'):
        "Potenzia il Potioman. Si usa (usa e getta).",

    # ---------------------------------------------------------- :46079
    (46079, '(Single-use) tool to be used on certain corpses.'):
        "Un materiale speciale, per certi cadaveri. Si usa (usa e getta).",

    # ---------------------------------------------------------- :46145
    (46145, '(Single-use) tool that can graft new body parts.'):
        "Una protesi che dà una parte del corpo. Si usa (usa e getta).",

    # ---------------------------------------------------------- :46406
    (46406, '(Single-use) tool containing a large sum of corks.'):
        "Dà una gran quantità di tappi. Si usa (usa e getta).",

    # ---------------------------------------------------------- :46482
    (46482, '(Reusable) large-calibre gun that shoots guard-breaking laser.'):
        "Un'arma che rompe la guardia. Si può usare più volte.",

    # ---------------------------------------------------------- :46550
    (46550, '(Reusable) tool that summons spirits.'):
        "Uno strumento che evoca gli spiriti. Si può usare sempre.",

    # ---------------------------------------------------------- :46821
    (46821, "(Reusable) tool for one to  discover one's personalities."):
        "Rivela una parte del carattere. Si può usare sempre.",

    # ---------------------------------------------------------- :46887
    (46887, '(Single-use) tool that give you a daughter.'):
        "Serve ad avere una figlia forte. Si usa (usa e getta).",

    # ---------------------------------------------------------- :46953
    (46953, '(Single-use) tool that give you a son.'):
        "Serve ad avere un figlio forte. Si usa (usa e getta).",

    # ---------------------------------------------------------- :47019
    (47019, '(Single-use) tool that gives experience to a living weapon.'):
        "Dà esperienza alle armi viventi. Si usa (usa e getta).",

    # ---------------------------------------------------------- :47086
    (47086, '(Single-use) tool that restores your MP.'):
        "Un anello che ridà MP. Si usa (usa e getta).",

    # ---------------------------------------------------------- :47289
    (47289, '(Reusable) tool. But it really is just smelly socks.'):
        "Calzini che puzzano. Si può usare sempre.",

    # ---------------------------------------------------------- :49779
    (49779, '(Reusable) tool that drench your thirst. Can be refilled under water.'):
        "Disseta; si riempie sott'acqua. Si può usare sempre.",

    # ---------------------------------------------------------- :49850
    (49850, "(Reusable) tool that raises one's stats to a certain level."):
        "Alza gli attributi fino a un limite. Si può usare sempre.",

    # ---------------------------------------------------------- :50063
    (50063, '(Reusable) tool that turns a dying enemy into solid gold.'):
        "Trasforma in oro il nemico in fin di vita. Si può usare sempre.",

    # ---------------------------------------------------------- :50134
    (50134, '(Reusable) tool that grants fame and authority.'):
        "Dà fama o autorità. Si può usare sempre.",

    # ---------------------------------------------------------- :50205
    (50205, '(Reusable) tool that allow simutaneous activation of two skills.'):
        "Attiva due capacità insieme. Si può usare sempre.",

    # ---------------------------------------------------------- :50274
    (50274, '(Reusable) tool that allows you to marry non-allies.'):
        "Fa sposare anche chi non è tra i compagni. Si può usare sempre.",

    # ---------------------------------------------------------- :50344
    (50344, '(Reusable) tool used on the world map. May be used periodically.'):
        "Funziona sulla mappa del mondo. Si può usare ogni tanto.",

    # ---------------------------------------------------------- :50411
    (50411, '(Single-use) tool crystal that half your skill to gain a slight bonus.'):
        "Dimezza un'abilità e dà un piccolo bonus. Si usa (usa e getta).",

    # ---------------------------------------------------------- :50477
    (50477, '(Reusable) tool that shoots out potion plugs at lethal velocity.'):
        "Spara tappi di pozione a gran velocità. Si può usare sempre.",

    # ---------------------------------------------------------- :50749
    (50749, '(Reusable) tool for processing vast amounts of information.'):
        "Elabora una mole enorme di informazioni. Si può usare sempre.",

    # ---------------------------------------------------------- :50948
    (50948, '(Unimplemented) (Reusable) tool used to set up or activate traps.'):
        "Piazza e innesca trappole (non attivo). Si può usare sempre.",

    # ---------------------------------------------------------- :51291
    (51291, '(Single-use) tool shard that grants you the memory of a skill.'):
        "Un frammento con la memoria di un'abilità. Si usa (usa e getta).",

    # ---------------------------------------------------------- :51982
    (51982, '(Single-use) throwing tool that creates a smoke screen.'):
        "Stende una cortina di fumo. Si lancia (usa e getta).",

    # ---------------------------------------------------------- :52048
    (52048, '(Reusable) tool that allows you to check and use your Yaca points.'):
        "Una carta per vedere e spendere i punti. Si può usare sempre.",

    # ---------------------------------------------------------- :52383
    (52383, '(Reusable) tool that give you weapon experience through training.'):
        "Allena le abilità con le armi. Si può usare sempre.",

    # ---------------------------------------------------------- :52449
    (52449, '(Reusable) tool that secure the harvest.'):
        "Fissa il raccolto. Si può usare sempre.",

    # ---------------------------------------------------------- :54888
    (54888, '(Single-use) tool that starts a fire.'):
        "Serve ad accendere il fuoco. Si usa (usa e getta).",

    # ---------------------------------------------------------- :55145
    (55145, '(Reusable) tool to enhance the shooting attack power.'):
        "Potenzia l'attacco a distanza. Si può usare sempre.",

    # ---------------------------------------------------------- :55484
    (55484, '(Single-use) tool that grants magic power.'):
        "Un frammento che contiene magia. Si usa (usa e getta).",

    # ---------------------------------------------------------- :56606
    (56606, '(Reusable) tool that cleans your ear.'):
        "Serve a pulirsi le orecchie. Si può usare sempre.",

    # ---------------------------------------------------------- :57066
    (57066, '(Single-use) tool that creates a cake for your allies to eat.'):
        "Non si mangia: usandolo, mangiano tutti i compagni (usa e getta).",

    # ---------------------------------------------------------- :57648
    (57648, '(Reusable) toy modeled after Goddess of Wealth. May be used periodically.'):
        "Riproduce la dea della ricchezza. Si può usare ogni tanto.",

    # ---------------------------------------------------------- :58529
    (58529, "It is a sword made for Seppuku. (Reusable) tool that can't be equipped."):
        "Una spada per il seppuku. Non si equipaggia, ma si usa sempre.",

    # ---------------------------------------------------------- :59661
    (59661, '(Single-use) tool stardust that enhances an artifact.'):
        "Polvere di stelle che potenzia un artefatto (usa e getta).",

    # ---------------------------------------------------------- :59929
    (59929, '(Single-use) tool that 3d-prints target with biological materials.'):
        "Un apparecchio che fa statuette. Si usa (usa e getta).",

    # ---------------------------------------------------------- :60066
    (60066, '(Single-use) tool that brings out the true potential of t equipment.'):
        "Tira fuori le vere doti dell'equipaggiamento (usa e getta).",

    # ---------------------------------------------------------- :60652
    (60652, '(Reusable) tool that launches a ball of gunpowder.'):
        "Spara in aria palle di polvere. Si può usare più volte.",

    # ---------------------------------------------------------- :60917
    (60917, '(Single-use) smoking tool.'):
        "Un attrezzo per fumare. Si usa (usa e getta).",

    # ---------------------------------------------------------- :62023
    (62023, '(Reusable) tactical nuclear weapon.'):
        "Un'arma nucleare tattica. Si usa (usa e getta).",

    # ---------------------------------------------------------- :62099
    (62099, "(Reusable) tool that burns down the area around the target it's aimed at."):
        "Incendia tutto intorno al bersaglio. Si può usare più volte.",

    # ---------------------------------------------------------- :62175
    (62175, '(Reusable) weapon that temporarily lowers the PV of a target.'):
        "Abbassa per un po' il PV del bersaglio. Si usa più volte.",

    # ---------------------------------------------------------- :62237
    (62237, 'It is a blanket that prevents allies from getting up early.'):
        "Il compagno che la porta non riesce più ad alzarsi presto.",

    # ---------------------------------------------------------- :62603
    (62603, '(Single-use) tool box of first aid supplies.'):
        "Una scatola per il primo soccorso. Si usa (usa e getta).",

    # ---------------------------------------------------------- :62669
    (62669, '(Single-use) toolbox filled with specialized ammunitions.'):
        "Una cassa che ricarica le munizioni speciali (usa e getta).",

    # ---------------------------------------------------------- :63524
    (63524, '(Single-use) horrifying weapon of destruction from ancient times.'):
        "Dopo un po' esplode e devasta un'area vasta (usa e getta).",

    # ---------------------------------------------------------- :63940
    (63940, '(Reusable) tool that transforms you. Can be used with 50% gauge.'):
        "Dà un altro aspetto e altra forza. Si usa con la barra al 50%.",

    # ---------------------------------------------------------- :64556
    (64556, '(Reusable) tool that opens a pocket in another dimension to store item.'):
        "Apre una tasca quadridimensionale. Si può usare più volte.",

    # ---------------------------------------------------------- :64681
    (64681, '(Single-use) tool box that allows all your friends to eat together.'):
        "Usandolo, mangiano tutti i compagni (usa e getta).",

    # ---------------------------------------------------------- :64744
    (64744, '(Reusable) tool that holds 15 coffins of necromancy.'):
        "Contiene fino a 15 bare della negromanzia. Si può usare sempre.",

    # ---------------------------------------------------------- :64810
    (64810, '(Single-use) tool that grants a body part you want.'):
        "Dà la parte del corpo che si vuole. Si usa (usa e getta).",

    # ---------------------------------------------------------- :65198
    (65198, '(Single-use) throwing tool that initializes duel with your opponent.'):
        "Un guanto da duello: si lancia all'avversario (usa e getta).",

    # ---------------------------------------------------------- :65467
    (65467, '(Single-use) tool lenses that allow you to see information of the target.'):
        "Una lente che mostra i dati del bersaglio. Si usa (usa e getta).",

    # ---------------------------------------------------------- :66078
    (66078, '(Reusable) tool stone that confirms your faith.'):
        "Una pietra che dice la fede. Si può usare sempre.",

    # ---------------------------------------------------------- :67669
    (67669, '(Reusable) tool that plays any music you want.'):
        "Suona il brano che si vuole. Si può usare sempre.",

    # ---------------------------------------------------------- :68590
    (68590, '(Single-use) tool that used for inhaling dried crimberry smoke.'):
        "Serve a fumare crimberry essiccate. Si usa (usa e getta).",

    # ---------------------------------------------------------- :68786
    (68786, '(Single-use) tool to use in a Showroom.'):
        "Serve nella sala d'esposizione. Si usa (usa e getta).",

    # ---------------------------------------------------------- :69457
    (69457, '(Single-use) tool for crops.'):
        "Concime per le colture. Si usa (usa e getta).",

    # ---------------------------------------------------------- :70336
    (70336, '(Single-use) cooking tool set.'):
        "Un attrezzo da cucina limitato. Si usa (usa e getta).",

    # ---------------------------------------------------------- :70601
    (70601, '(Reusable) tool used for necromancy. May be used periodically.'):
        "Sveglia il mostro che dorme nella bara. Si usa ogni tanto.",

    # ---------------------------------------------------------- :70820
    (70820, '(Single-use) tool that duplicate the existence of target into your team.'):
        "Duplica il bersaglio e lo mette nel gruppo. Si usa (usa e getta).",

    # ---------------------------------------------------------- :71927
    (71927, '(Single-use) tool doll that is 10cm in height.'):
        "Una bambola alta una decina di centimetri. Si usa (usa e getta).",

    # ---------------------------------------------------------- :72487
    (72487, '(Single-use) tool that changes your profession. Write in lower caption.'):
        "Un articolo che cambia la classe. Si usa (usa e getta).",

    # ---------------------------------------------------------- :72553
    (72553, '(Single-use) tool that changes your race. Use in lower caption.'):
        "Un oggetto che cambia la razza. Si usa (usa e getta).",

    # ---------------------------------------------------------- :72623
    (72623, '(Reusable) tool for sound of certain frequency. May be used periodically.'):
        "Un fischietto a frequenza speciale. Si può usare ogni tanto.",

    # ---------------------------------------------------------- :73023
    (73023, '(Single-use) tool that unlocks special abilities.'):
        "Una gemma che serba poteri speciali. Si usa (usa e getta).",

    # ---------------------------------------------------------- :73291
    (73291, '(Reusable) tool that switch between offensive and defensive instructions.'):
        "Alterna ordini d'attacco e di difesa. Si può usare sempre.",

    # ---------------------------------------------------------- :73701
    (73701, 'It is a statue of God of Elements. May be used periodically.'):
        "Una statua del dio degli elementi. Si usa ogni tanto.",

    # ---------------------------------------------------------- :73768
    (73768, 'It is a statue of Goddess of Wealth. May be used periodically.'):
        "Una statua della dea della ricchezza. Si usa ogni tanto.",

    # ---------------------------------------------------------- :73831
    (73831, '(Unimplemented) (Reusable) tool that apply the effect of the cards.'):
        "Tira fuori l'effetto delle carte (non attivo). Si usa sempre.",

    # ---------------------------------------------------------- :76317
    (76317, '(Reusable) tool used shoot every enemy nearby. May be used periodically.'):
        "Danno a tutti i nemici, secondo il Tiro. Si usa ogni tanto.",

    # ---------------------------------------------------------- :77776
    (77776, '(Reusable) tool for monthly allowence. May be used periodically.'):
        "Una volta al mese arriva la paghetta. Si usa ogni tanto.",

    # ---------------------------------------------------------- :78259
    (78259, '(Reusable) tool that allow using of complex fusion recipes.'):
        "Un attrezzo per le fusioni complesse. Si può usare sempre.",

    # ---------------------------------------------------------- :79114
    (79114, 'It is a statue of God of Machine. May be used periodically.'):
        "Una statua del dio delle macchine. Si usa ogni tanto.",

    # ---------------------------------------------------------- :79181
    (79181, 'It is a statue of God of Harvest. May be used periodically.'):
        "Una statua del dio del raccolto. Si usa ogni tanto.",

    # ---------------------------------------------------------- :80221
    (80221, '(Single-use) tool that raises the quality of the equipment.'):
        "Rende eccezionale un'arma o un'armatura. Si usa (usa e getta).",

    # ---------------------------------------------------------- :80927
    (80927, 'It is a statue of creator from the Moongate world. The power is lost now.'):
        "Serve nella sala d'esposizione. Si può usare sempre.",

    # ---------------------------------------------------------- :80995
    (80995, '(Reusable) tool used in showrooms. May be used to summon CNPCs.'):
        "Serve nella sala d'esposizione. Si può usare sempre.",

    # ---------------------------------------------------------- :81133
    (81133, '(Reusable) tool that forbids pet from doing certain actions.'):
        "Vieta ai compagni di raccogliere roba. Si può usare sempre.",

    # ---------------------------------------------------------- :81199
    (81199, '(Reusable) tool that analyzes the mind of the target.'):
        "Analizza l'animo del bersaglio. Si può usare sempre.",

    # ---------------------------------------------------------- :82007
    (82007, '(Reusable) tool that can tie up a weakened monster.'):
        "Ci si appende un mostro indebolito. Si può usare sempre.",

    # ---------------------------------------------------------- :82812
    (82812, 'It is a statue of Goddess of Luck. May be used periodically.'):
        "Una statua della dea della fortuna. Si usa ogni tanto.",

    # ---------------------------------------------------------- :83081
    (83081, '(Reusable?) gem that changes the past of the future.'):
        "Una gemma che, usata, cambierà qualcosa più avanti.",

    # ---------------------------------------------------------- :83212
    (83212, '(Single-use) tool that grants you a feat.'):
        "Una gemma che dà un talento nuovo (usa e getta).",

    # ---------------------------------------------------------- :84038
    (84038, '(Reusable) tool that creates a high pitch noise.'):
        "Manda un suono acuto tutt'intorno. Si può usare sempre.",

    # ---------------------------------------------------------- :84166
    (84166, '(Reusable) tool to store cards.'):
        "Una scatola per le carte. Si può usare sempre.",

    # ---------------------------------------------------------- :84299
    (84299, "It is a throwable tool that can be used to capture 'Little Sister'."):
        "Colpisce e cattura la <Little Sister>. Si può lanciare.",

    # ---------------------------------------------------------- :84970
    (84970, 'It is a horrible looking furniture. It is best not to touch it.'):
        "Un mobile orribile a vedersi. Meglio non toccarlo.",

    # ---------------------------------------------------------- :85171
    (85171, 'It is a statue of Goddess of Healing. May be used periodically.'):
        "Una statua della dea della guarigione. Si usa ogni tanto.",

    # ---------------------------------------------------------- :85237
    (85237, 'It is a throwable tool that can be used to capture monsters.'):
        "Colpisce e cattura un mostro. Si può lanciare.",

    # ---------------------------------------------------------- :85301
    (85301, '(Reusable) tool that erases a pet and transfers its ability to another.'):
        "Cancella un compagno e dà le sue doti a un altro. Si usa sempre.",

    # ---------------------------------------------------------- :85370
    (85370, '(Reusable) tool used the reconstruct material. May be used periodically.'):
        "Ricompone la materia e la muta in altro. Si usa ogni tanto.",

    # ---------------------------------------------------------- :85437
    (85437, '(Reusable) tool used to accelerate crop growth. May be used periodically.'):
        "Accelera la crescita delle colture. Si usa ogni tanto.",

    # ---------------------------------------------------------- :85506
    (85506, "(Reusable) tool used to recover allies' health. May be used periodically."):
        "Cura gli HP dei compagni intorno. Si usa ogni tanto.",

    # ---------------------------------------------------------- :85575
    (85575, '(Reusable) tool used to raise speed. May be used periodically.'):
        "Alza la velocità per un po'. Si può usare ogni tanto.",

    # ---------------------------------------------------------- :86203
    (86203, '(Single-use) bomb that inflicts devastating destruction over a wide area.'):
        "Dopo un po' esplode e devasta un'area vasta (usa e getta).",

    # ---------------------------------------------------------- :86536
    (86536, 'It is a statue of Goddess of Wind. May be used periodically.'):
        "Una statua della dea del vento. Si usa ogni tanto.",

    # ---------------------------------------------------------- :86603
    (86603, 'It is a statue of God of Earth. May be used periodically.'):
        "Una statua del dio della terra. Si usa ogni tanto.",

    # ---------------------------------------------------------- :88024
    (88024, '(Reusable) Rank 4 bed of simple design.'):
        "Un letto semplice (rango 4). Si può usare sempre.",

    # ---------------------------------------------------------- :88213
    (88213, '(Single-use) tool that reduce the insanity level.'):
        "Abbassa la Follia tua e dei compagni intorno (usa e getta).",

    # ---------------------------------------------------------- :88413
    (88413, '(Autoused) tool that enhances your lockpicking capabilities.'):
        "Basta averlo addosso: lo scasso riesce molto più spesso.",

    # ---------------------------------------------------------- :88475
    (88475, '(Autoused) tool that is required for picking locks. It may break.'):
        "Serve per lo scasso. Certe volte si rompe.",

    # ---------------------------------------------------------- :88541
    (88541, '(Single-use) tool that destroys the ones stepped on it when armed.'):
        "Una bomba che dilania chi la calpesta. Si usa (usa e getta).",

    # ---------------------------------------------------------- :88607
    (88607, '(Reusable) tool to tie up friends and keep them from going too far away .'):
        "Lega un compagno perché non si allontani. Si usa sempre.",

    # ---------------------------------------------------------- :88872
    (88872, '(Single-use) tool that re-forge the material of target item.'):
        "Rifà l'oggetto nel materiale scelto (usa e getta).",

    # ---------------------------------------------------------- :88940
    (88940, '(Reusable) tool that reset non-monster hostile situations.'):
        "Azzera l'ostilità di chi non è un mostro. Si usa più volte.",

    # ---------------------------------------------------------- :90140
    (90140, '(Reusable) tool that allows you to change the decor of a room.'):
        "Cambia l'arredo della stanza. Si può usare sempre.",

    # ---------------------------------------------------------- :91912
    (91912, '(Reusable) hand-held simple light.'):
        "Una luce semplice da tenere in mano. Si può usare sempre.",

    # ---------------------------------------------------------- :92255
    (92255, '(Reusable) tool that allows you to save money.'):
        "Ci si mette da parte una somma alla volta. Si usa sempre.",

    # ---------------------------------------------------------- :92392
    (92392, "It is a mysterious disc that seem's to play your memories."):
        "Un disco con dei filmati incisi. Si può usare sempre.",

    # ---------------------------------------------------------- :92937
    (92937, 'It is a blanket that prevents items from being damaged by freezing.'):
        "Una coperta che protegge dal gelo, per qualche volta.",

    # ---------------------------------------------------------- :93001
    (93001, 'It is a blanket that prevents items from being damaged by burning.'):
        "Una coperta che protegge dal fuoco, per qualche volta.",

    # ---------------------------------------------------------- :93361
    (93361, '(Reusable) tool that change assignments.'):
        "Cambia l'incarico. Si può usare sempre.",

    # ---------------------------------------------------------- :93826
    (93826, '(Reusable) tool that can be used to build a shelter in a hurry.'):
        "Un rifugio che si monta in un po' di tempo. Si usa sempre.",

    # ---------------------------------------------------------- :94604
    (94604, 'It is an usable disc etched with music data.'):
        "Un disco con della musica incisa. Si può usare sempre.",

    # ---------------------------------------------------------- :99094
    (99094, "(Reusable) tool that visualizes an ally's health."):
        "Mostra gli HP dei compagni. Si può usare sempre.",

    # ---------------------------------------------------------- :102461
    (102461, '(Reusable) Rank 0 makeshift bed.'):
        "Un letto semplice (rango 0). Si può usare sempre.",

    # ---------------------------------------------------------- :104794
    (104794, '(Reusable) tool made for gem cutting, a necessity for jewelers.'):
        "Serve a lavorare le gemme. Si può usare sempre.",

    # ---------------------------------------------------------- :108460
    (108460, '(Reusable) tool made for fishing, a necessity for the fisherman.'):
        "Serve a pescare. Si può usare sempre.",

    # ---------------------------------------------------------- :114080
    (114080, 'It is a cooking tool allowing the preparation of dishes up to Rank 5.'):
        "Ci si cucinano i piatti fino al rango 5.",

    # ---------------------------------------------------------- :114144
    (114144, 'It is a glowing cooking tool allowing preparation of dishes up to Rank 3.'):
        "Ci si cucina fino al rango 3. Illumina sempre intorno.",

    # ---------------------------------------------------------- :116349
    (116349, 'It is a cooking tool allowing the preparation of dishes up to Rank 4.'):
        "Ci si cucinano i piatti fino al rango 4.",

    # ---------------------------------------------------------- :116606
    (116606, '(Reusable) tool that you should use them NOW! <Category: Punishment.'):
        "Si può usare sempre.",

    # ---------------------------------------------------------- :120508
    (120508, '(Reusable) tool made for carpentry, a necessity for carpenters.'):
        "Serve per i lavori di falegnameria. Si può usare sempre.",

    # ---------------------------------------------------------- :120574
    (120574, '(Reusable) tool made for tailoring, a necessity for the tailors.'):
        "Serve a cucire. Si può usare sempre.",

    # ---------------------------------------------------------- :121832
    (121832, 'It is a tool for painting. Cannot be used.'):
        "Serve a dipingere. Non si può usare.",

    # ---------------------------------------------------------- :122682
    (122682, '(Reusable) tool made for basic alchemy.'):
        "Serve per l'alchimia. Si può usare sempre.",

# 143 voci, 0 ambigue
}
