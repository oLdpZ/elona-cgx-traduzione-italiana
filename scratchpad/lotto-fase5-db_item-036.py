# -*- coding: utf-8 -*-
"""115a - Lotto 036 di `db_item.hsp`: GLI ATTREZZI, quarta parte.

`FILTER_ITEM_TOOL`, righe 75.000-90.000: **42 righe** su 39 oggetti — 39
dell'indice 0, nessuna dell'indice 1 e 3 dell'indice 2. Segue il 035.

### ⭐⭐ DUE FAMIGLIE CHE ATTRAVERSANO I LOTTI

Le **otto statue degli dei** e le **cinque gemme divine** non stanno tutte
qui: `:73698` (Itzpalt) e `:73765` (Yacatect) erano nel lotto 035, e la loro
resa e' il modello. E' la regola della 111a — la famiglia batte il lotto — e
qui si vede in avanti invece che indietro: chi apre il lotto 037 e trovasse
un'altra statua deve copiare da qui.

    statue    Una statua che raffigura <il dio X>, opera di un artista
              famoso. <la frase finale, che cambia sempre>
    gemme     La gemma miracolosa che ha portato <il dio X>. Ha il potere,
              dicono, di <...>

⭐ **I nomi degli dei non si decidono qui: stanno gia' nell'indice 3**, che e'
chiuso dalla 111a. 機械の神 «il dio delle macchine», 収穫の神 «il dio del
raccolto», 幸運な女神 «la dea della fortuna», 癒しの女神 «la dea della
guarigione», 風の女神 «la dea del vento», 大地の神 «il dio della terra»,
富の女神 «la dea della ricchezza». Bastava leggerli.

⚠️ Il giapponese delle statue chiude sempre con どことなく〜, «un non so che
di ~», e l'inglese lo scioglie ogni volta in modo diverso («somehow»,
«rather», «irresistibly», o niente). L'italiano tiene la formula, perche' in
giapponese la formula c'e'.

### ⚠️⚠️ DUE RIGHE SENZA GIAPPONESE ANCORA, E ADESSO SONO QUATTRO IN TRE LOTTI

`:80994` (il cristallo di evocazione) e `:84969` (la ghigliottina) hanno il
giapponese **vuoto**, come `:50410` nel 034 e `:72552` nel 035. Fanno **quattro
su 545 rese del corpo**, e sono tutte righe di indice 2 — le battute.

⭐ La spiegazione probabile: sono **aggiunte del CGX in inglese**, scritte
direttamente nel ramo `en` senza passare dal giapponese. Se e' cosi', non c'e'
niente da riparare e il numero crescera' piano; se invece salisse di colpo,
vorrebbe dire che l'estrazione perde il ramo giapponese, e sarebbe un guasto.
ⓘ **Il conto va tenuto**, ed e' per questo che sta scritto qui.

⚠️ `:84969` e' per giunta un gioco di parole intraducibile alla lettera: «You
are sure to get ahead in life», dove *get ahead* e' «farsi strada» e *a head*
e' la testa che la ghigliottina taglia. L'italiano non ha quel doppio senso,
ma ne ha un altro che serve la stessa battuta: «si va avanti: gli altri
restano indietro **di una testa**».

### ⚠️ IL NOME DELL'OGGETTO VIENE DALL'INGLESE, E IL GIAPPONESE DICE ALTRO

`:88869` e' 素材槌, il **martello** dei materiali, e la prosa giapponese parla
di un martello per tutta la riga. Il nome italiano dell'oggetto pero' e' «kit
di materiali», perche' e' stato reso a suo tempo dall'inglese `material kit`.

Qui il contratto dei nomi (107a: *la prosa nomina l'oggetto col nome che il
giocatore vede*) e la fonte giapponese si contraddicono. Ha vinto il
giapponese, perche' la prosa **descrive** l'oggetto e un martello e' quello che
descrive; il nome resta com'e' e la sua correzione, se si vorra' fare, e' un
lavoro dell'indice dei nomi, non di un lotto del corpo.
ⓘ La stessa cosa vale al contrario per `:52380` nel 034, dove la prosa
obbedisce al nome non identificato. Il criterio e': si obbedisce al nome quando
il nome e' **giusto**.

### ⓘ L'inglese sbaglia ancora due volte, e stavolta nella CODA

`:81130` (la frusta) e `:88604` (il guinzaglio) hanno per fonte giapponese
～巻かれる為の長いもの～, «cose lunghe fatte per essere avvolte». L'inglese
scrive per tutt'e due `~Battles, Dragons, Swords and Magic~`, che e' il titolo
di un **altro libro**.

ⓘ Il cancello «titoli resi in piu' modi» non se ne accorge, perche' chiava
sull'inglese e le due righe hanno lo stesso inglese e la stessa resa. Si vede
solo leggendo il giapponese, ed e' l'ennesima ragione per cui la coda si
assegna con `_code.py`, che passa **dal giapponese**, e non a occhio.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :76314
    (76314, 'Miraculous jewel brought by the God of Machine. It is said that if you hold it up to the sky, a rain of charged particle beams will rain down from a satellite orbit. It is said that the beam is simultaneously projected with a laser to prevent diffusion and attenuation of the charged particles, but the details are not known. \\n# ~Irva Fantasy Encyclopedia~'):
        "La gemma miracolosa che ha portato il dio delle macchine. Alzandola al cielo, dicono, dall'orbita di un satellite piove una pioggia di raggi di particelle cariche. Pare che insieme lancino anche un laser per impedire che le particelle si sparpaglino e si smorzino, ma di preciso non si sa. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77773
    (77773, 'Miraculous treasure brought by the Goddess of Wealth. They are given to persons she want to give allowance to. \\n# ~Irva Fantasy Encyclopedia~'):
        "La gemma miracolosa che ha portato la dea della ricchezza. La si regala, dicono, a chi si vuole passare la paghetta. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :78256
    (78256, 'A boiling pot used by alchemists for item synthesis. Materials are boiled together with special chemicals to change the structure of matter at the atomic level through mutual reactions. \\n# ~An Introduction to Alchemy~'):
        "Il paiolo che gli alchimisti usano per la fusione. I materiali si fanno bollire insieme a certi preparati, e la reazione fra loro cambia la struttura della materia a livello di atomi. \\n# ~Manuale d'Introduzione all'Alchimia~",

    # ---------------------------------------------------------- :78322
    (78322, 'Items placed inside are magically fused with each other to create something else. It is a state-of-art magical tool. \\n# ~Lumiest Art Catalogue~'):
        "Ci hanno messo sopra una magia che fonde fra loro certi oggetti e ne fa un altro. Anche a guardarlo come opera d'arte è un bel pezzo. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :79111
    (79111, 'A statue in the shape of the God of Machine, created by a renowned artist. Even the intricately made complex parts are recreated. \\n# ~Lumiest Art Catalogue~'):
        "Una statua che raffigura il dio delle macchine, opera di un artista famoso. I punti fatti a incastro qua e là hanno un non so che di grintoso. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :79178
    (79178, 'A statue in the shape of the God of Harvest. created by a renowned artist. The melancholy expression on his face is somehow dignified. \\n# ~Lumiest Art Catalogue~'):
        "Una statua che raffigura il dio del raccolto, opera di un artista famoso. L'aria mesta del volto ha un non so che di fiero. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :80218
    (80218, "Garok's hammer is a master craftsman's hammer that instantly transforms any piece of junk into a one-of-a-kind item. However, since the craftsman's difficult temperament is directly reflected in his hammer, he does not seem to listen to our wishes. \\n# ~Irva Fantasy Encyclopedia~"):
        "Il martello di Garok, maestro artigiano, che di qualunque ciarpame fa in un attimo un pezzo unico. Però l'indole difficile dell'artigiano è passata tale e quale nel martello, e a quanto pare le nostre richieste non le ascolta. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :80924
    (80924, "Indescribable statue made by an unknown artist. It appears to be a strangely dressed figure, but the word 'Creator' is engraved on the side, so perhaps this is the figure of the Creator. \\n# ~Lumiest Art Catalogue~"):
        "Una statua indefinibile, opera di un artista di cui non si sa il nome. Comunque la si guardi è la figura di una persona vestita in modo strano, ma sul fianco c'è inciso Creatore: forse allora è questo il suo aspetto. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :80992
    (80992, 'Giant crystals created by time immemorial. It is said that its light projects the heart of the beholder and reveals it in this world. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un cristallo enorme, che un tempo lunghissimo ha messo insieme. La sua luce, dicono, riflette il cuore di chi guarda e lo porta in questo mondo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :80994
    (80994, '\\"Just summon adventurers from another world to do the chores for you, neat, right?\\" \\n# ~Lane, the Fairy Invoker~'):
        "\\\"Ti basta evocare avventurieri da un altro mondo e le faccende te le sbrigano loro. Comodo, no?\\\" \\n# ~<Lane>, evocatrice di fate~",

    # ---------------------------------------------------------- :81130
    (81130, 'Leather whip used by circus leaders and others. Once wielded, it will make any beast of prey obedient. \\n# ~Battles, Dragons, Swords and Magic~'):
        "Una frusta di cuoio, che flette bene, di quelle che usano i capi del circo. Basta schioccarla una volta e qualunque belva diventa docile. \\n# ~Cose Lunghe Fatte per Essere Avvolte~",

    # ---------------------------------------------------------- :81196
    (81196, 'This work of art utilizes special materials to depict anguished hearts. The intertwined materials are said to move slightly like a real heart. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'opera d'arte che, con materiali particolari, rappresenta un animo in pena fra due sentimenti che non stanno insieme. I materiali, intrecciati l'uno all'altro, si muovono appena, come farebbe un cuore vero. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :82004
    (82004, 'Vertical exercise equipment designed to relieve daily stress and to train oneself. The only difference between this and the typical North Tyris sandbag is that it uses weak victims instead of sand as its material. \\n# ~Daily Necessities for the Home~'):
        "Un attrezzo da ginnastica alto e stretto, fatto per scaricare lo stress di ogni giorno e per allenarsi. La piccola differenza fra quello di Tyris del Nord e quello comune, forse, è che come materiale dentro non ci va la sabbia ma una vittima indebolita. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :82809
    (82809, 'A statue in the shape of the Goddess of Luck. created by a renowned artist. Her carefree smile is irresistibly endearing. \\n# ~Lumiest Art Catalogue~'):
        "Una statua che raffigura la dea della fortuna, opera di un artista famoso. Il sorriso spensierato ha un non so che di tenero. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :83078
    (83078, 'A mysterious gemstone that makes you feel uncomfortable just by looking at it. It can be used, but no one has confirmed its effectiveness. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una gemma misteriosa che, solo a guardarla, mette a disagio. Si può usare, ma pare che nessuno abbia mai visto che effetto faccia. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :83209
    (83209, 'Another miracle given by the God of Harvest. It is said that when you use it, it emits light and you can have an unforgettable experience there. \\n# ~Irva Fantasy Encyclopedia~'):
        "L'altro miracolo che il dio del raccolto ha concesso. A usarla manda luce, e lì dentro, dicono, si fa un'esperienza che non si sa dire. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :84035
    (84035, 'A whistle that produces a high-pitched sound when used. The sound, which can wake even the most sleepy person instantly, is like a horn of calamity that evokes the apocalypse. ...at least for those who have been asleep. \\n# ~Music of the Melodious Irva~'):
        "Un fischietto che, a usarlo, manda intorno un suono acuto. Quel suono sveglia in un attimo chiunque, per quanto dorma sodo: pare il corno della sciagura che chiama la fine del mondo. ...Almeno per chi stava dormendo. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :84163
    (84163, 'A container for storing cards. Some aristocrats were not satisfied with the collection and even came up with the idea of using it for games. \\n# ~Censored! Box Mania, First Issue~'):
        "Un contenitore per tenerci le carte. Fra i nobili, dicono, c'è stato perfino chi, non contento di collezionarle, si è inventato un gioco da farci. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # ---------------------------------------------------------- :84296
    (84296, 'Suspiciously glowing mechanical balls made to capture special beings. The ball is so mechanically reckless in its attempt to create a comfortable space inside that it breaks and disappears when thrown unsuccessfully. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Una sfera meccanica dalla luce sospetta, fatta per catturare esseri speciali. Per ricavarci dentro uno spazio comodo hanno forzato parecchio il meccanismo, e basta sbagliare il lancio perché si rompa e sparisca. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :84967
    (84967, "This is a horrifying device that once existed for executions. It is so simple in structure that it was made only for the purpose of decapitating the victim's head. It may not be used anymore, but never be too careful. The blade always glints dully above your head. \\n# ~Worlds you've Never Seen~"):
        "Uno strumento di pena orribile come pochi, che un tempo serviva alle esecuzioni. Ha una struttura così semplice perché è fatto per una cosa sola: far cadere la testa alla vittima. Pare che oggi non si usi più, ma non abbassare la guardia: la lama sopra di te manda sempre un luccichio spento. \\n# ~I Mondi che Non Hai Mai Visto~",

    # ---------------------------------------------------------- :84969
    (84969, '\\"You are sure to get ahead in life with one of these!\\" \\n# ~words of a ex-excutioner~'):
        "\\\"Con uno di questi, nella vita, si va avanti: gli altri restano indietro di una testa!\\\" \\n# ~parole di un ex boia~",

    # ---------------------------------------------------------- :85030
    (85030, "This is a horrifying device that once existed for torture. The front of the structure opens to the left and right, and inside the structure are bloodthirsty iron needles protruding toward the center. According to the story, some of them start to move, so it would be better not to touch them out of curiosity. \\n# ~Worlds you've Never Seen~"):
        "Uno strumento di pena orribile come pochi, che un tempo serviva a far parlare. Il davanti si apre in due, e dentro ci sono aghi di ferro assetati di sangue che sporgono verso il centro. Si racconta che qualcuno si metta in moto da solo: meglio non toccarlo per curiosità. \\n# ~I Mondi che Non Hai Mai Visto~",

    # ---------------------------------------------------------- :85168
    (85168, 'A statue in the shape of the Goddess of Healing. created by a renowned artist. Its modest posture is somehow pure and innocent. \\n# ~Lumiest Art Catalogue~'):
        "Una statua che raffigura la dea della guarigione, opera di un artista famoso. Il portamento schivo dà un non so che di puro. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :85234
    (85234, 'A mechanical ball that is thrown to capture weakened enemies. The detailed manufacturing process is unknown, but it is believed that the rise of genetics had much to do with the evolution of this tool. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Una sfera meccanica che, lanciata, cattura i nemici indeboliti. Come sia fatta di preciso non si sa, ma si pensa che il fiorire della genetica c'entri molto con l'evoluzione di questo arnese. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :85298
    (85298, 'A strange machine in the shape of a transparent cylinder. It is a devilish machine that deviates from the norm, capable of breaking down living organisms into particles, extracting only their abilities, and then adding those abilities to other living organisms. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Una macchina strana, un cilindro trasparente. In verità è una macchina diabolica e fuori da ogni regola: scompone un essere vivente in particelle, ne cava fuori le sole doti e quelle doti le aggiunge a un altro essere. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :85367
    (85367, 'Mysterious high-energy crystals from outer space. It is said to contain the wisdom of warriors from another planet, but the details are unknown. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un cristallo misterioso ad alta energia, arrivato dallo spazio. C'è chi dice che dentro ci sia il sapere di guerrieri di un altro pianeta, ma di preciso non si sa. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :85434
    (85434, 'Miraculous treasure from the God of Harvest. It is said to have the power to bestow fertility. \\n# ~Irva Fantasy Encyclopedia~'):
        "La gemma miracolosa che ha portato il dio del raccolto. Ha il potere, dicono, di dare abbondanza in un punto solo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :85503
    (85503, 'Miraculous treasure from the Goddess of Healing. It is said to have the power to sprinkle life force around it. \\n# ~Irva Fantasy Encyclopedia~'):
        "La gemma miracolosa che ha portato la dea della guarigione. Ha il potere, dicono, di spargere vita tutt'intorno. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :85572
    (85572, 'Miraculous treasure from the Goddess of Wind. It is said to have the power to wind up time. \\n# ~Irva Fantasy Encyclopedia~'):
        "La gemma miracolosa che ha portato la dea del vento. Ha il potere, dicono, di far sentire il vento del tempo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :86132
    (86132, "Gemstone that is said to bring about new changes in one's own body when used. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una gemma che, a usarla, porterebbe al proprio corpo un cambiamento nuovo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :86200
    (86200, '\\"The bomb isn\'t the evil, it\'s what you use it for that is evil. \\" \\n# ~the last page of the instruction manual~'):
        "\\\"Non è la cosa in sé a essere il male: il male è chi l'ha usata.\\\" \\n# ~Le Parole sull'Ultima Pagina del Manuale~",

    # ---------------------------------------------------------- :86533
    (86533, 'A statue in the shape of the Goddess of Wind. created by a renowned artist. The curves of body is elegant and beautiful. \\n# ~Lumiest Art Catalogue~'):
        "Una statua che raffigura la dea del vento, opera di un artista famoso. Le membra, fatte come se scorressero, hanno un non so che di bello. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :86600
    (86600, 'A statue in the shape of the God of Earth. created by a renowned artist. Its dynamic posture is rather heroic. \\n# ~Lumiest Art Catalogue~'):
        "Una statua che raffigura il dio della terra, opera di un artista famoso. La posa piena di slancio ha un non so che di fiero e virile. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :88021
    (88021, 'This type of bedding was introduced from a foreign land, and the mattress is laid directly on the ground. Although it is made of cloth, it is not very comfortable because it is placed on the back of the bed against the hard ground. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Un giaciglio venuto da un paese straniero, che si stende in terra e basta. Anche se in mezzo c'è la stoffa, si sta schiena contro schiena col terreno duro, e a dormirci non pare granché comodo. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :88210
    (88210, 'The horn of the mythical unicorn. It is said to remove anxiety and madness from the body when decocted and consumed. \\n# ~Irva Fantasy Encyclopedia~'):
        "Il corno dell'unicorno, che nessuno ha mai visto. Bollito e bevuto, dicono, porta via dal corpo l'inquietudine e la follia. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :88410
    (88410, 'Special item that can be used in conjunction with a lockpick to make locks easier to unlock. It is speculated that it is a relic from the old days, as it fits perfectly no matter what keyhole it is inserted into. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un oggetto speciale che, usato insieme al grimaldello, rende più facile aprire le serrature. Siccome in qualunque toppa lo si infili entra a pennello, si pensa che sia un resto di un'altra epoca. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :88472
    (88472, 'An essential tool for opening locks. Although it may break down from time to time, if you are good at it, you can open any treasure chest. There are keys to open locks, but there are no keys to close locks in this world. \\n# ~an Adventurer is You! Guide for Travels~'):
        "L'arnese che, per aprire una serratura, si può dire d'obbligo. Il difetto è che ogni tanto si rompe, ma con una buona mano non c'è forziere che tenga. Chiavi per aprire ce ne sono; per chiudere, in questo mondo, nessuna. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :88538
    (88538, 'A weapon that, when used, buries itself in the ground and becomes completely invisible. It is said that if you step on the spot without knowing anything about it, it will be obliterated without a trace in the end. Yes, that is even if you step on it... \\n# ~Gifts that I am Happy to Receive~'):
        "Un'arma che, a usarla, si sotterra e sparisce del tutto alla vista. Chi calpesta quel punto senza saperne niente, dicono, salta via che non ne resta traccia. Sì: anche se a calpestarla fossi tu... \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :88604
    (88604, 'Cord that binds the object by using it. It is recommended for lonely people who want someone to be there, but they might get angry if you tie them up without asking them to. \\n# ~Battles, Dragons, Swords and Magic~'):
        "Una corda che, a usarla, lega il bersaglio. Se sei di quelli che si sentono soli e vogliono qualcuno lì vicino te la consigliamo, ma a legare chiunque capiti forse qualcuno si arrabbia. \\n# ~Cose Lunghe Fatte per Essere Avvolte~",

    # ---------------------------------------------------------- :88869
    (88869, 'A hammer that can smash a material into a specific and completely different material. This miraculous item is the work of two brothers, artisans who live quietly in the snowfields, and is considered a tool for their use. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un martello che sa battere il materiale di una cosa fino a farne un altro materiale, del tutto diverso. Questo pezzo miracoloso è opera di due fratelli artigiani che vivono ritirati nelle nevi, ed è anche l'arnese che adoperano. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :88937
    (88937, 'Tool that allows a person to escape difficulties by disguising themselves as someone else with a quick change of clothes in an instant. Even if you are short on time, you can use this tool with peace of mind, because when you use it, a white mist blows out vigorously, giving you time to disguise yourself. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Un arnese che permette di cambiarsi in un lampo, farsi passare per un altro e cavarsi dai guai. Anche senza tempo lo puoi usare tranquillo: quando lo apri sbuffa fuori di forza una nebbia bianca, e quella il tempo di travestirti te lo dà. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

# 39 voci, 0 ambigue

    # ---------------------------------------------------------- :88939
    (88939, '\\"I wasn\'t even ten when I stole for the first time. I was just trying to survive back then. I\'m still as bold as I was then, just a little savvier.\\" \\n# ~words of <Sin> the thief guildmaster~'):
        "\\\"La prima volta che ho rubato non avevo ancora dieci anni. Allora cercavo solo di restare vivo. Sfacciato lo sono ancora come allora: solo, un po' più furbo.\\\" \\n# ~Parole di <Sin> il maestro della Gilda dei Ladri~",

# 3 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-036.jsonl'
RIGHE = {
    76314, 77773, 78256, 78322, 79111, 79178, 80218, 80924, 80992, 80994,
    81130, 81196, 82004, 82809, 83078, 83209, 84035, 84163, 84296, 84967,
    84969, 85030, 85168, 85234, 85298, 85367, 85434, 85503, 85572, 86132,
    86200, 86533, 86600, 88021, 88210, 88410, 88472, 88538, 88604, 88869,
    88937, 88939,
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
