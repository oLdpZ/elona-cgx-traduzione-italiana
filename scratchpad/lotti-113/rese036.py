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
