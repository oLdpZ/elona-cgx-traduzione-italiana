import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :62020
    (62020, 'A weapon that fires nuclear rockets. Intended for front-line use and pinpoint target destruction, the range and blast radius are quite modest. However, the power per range is rather enhanced, so care must be taken not to get caught in the middle. It cannot be reloaded and is disposable in terms of barrel strength. Since it is too heavy to be carried individually, it is usually carried in a vehicle. \\n# ~You Can Use it too! Excavated Weapons~'):
        "Un'arma che spara razzi nucleari. È pensata per la prima linea e per distruggere un bersaglio preciso, quindi la gittata e il raggio dello scoppio sono piuttosto contenuti. La forza per area però è alzata, e bisogna stare attenti a non restarci dentro. Non si ricarica, e per come regge la canna è comunque usa e getta. Col peso che ha, portarla addosso è dura: di solito la si carica su un veicolo. \\n# ~Puoi Usarle Anche Tu! Le Armi Riesumate~",

    # ---------------------------------------------------------- :62096
    (62096, 'This is a portable weapon that fires incendiary rockets from four barrels, one at a time. It has been greatly improved and has high accuracy at short distances. The special combustion agent mixed with the rockets generates a tremendous amount of heat, and direct exposure to the flying droplets can cause severe burns. Although it has the firepower to burn an entire area, it is bulky and is rarely used in the Yerles military. Because of its shape, it is sometimes mistaken as to which side the shell comes out from. \\n# ~You Can Use it too! Excavated Weapons~'):
        "Un'arma portatile che spara razzi incendiari uno alla volta da quattro canne. È molto migliorata, e sulla distanza corta è precisa. La miscela speciale che ci bruciano dentro scalda in modo tremendo, e gli schizzi addosso danno ustioni gravi. Ha fuoco da bruciare un'intera area, ma è ingombrante e fra gli Yerles non la usa quasi nessuno. Per la forma che ha, ogni tanto ci si sbaglia su da che parte esca il colpo. \\n# ~Puoi Usarle Anche Tu! Le Armi Riesumate~",

    # ---------------------------------------------------------- :62098
    (62098, '\\"Aim towards the enemy!\\" \\n# ~attached manual~'):
        "\\\"Sparare in direzione del nemico.\\\" \\n# ~Il Foglietto delle Istruzioni Allegato~",

    # ---------------------------------------------------------- :62172
    (62172, 'An anti-tank rocket launcher believed to have been used by past civilizations. Its special rocket propulsion, which is resistant to crosswinds, provides high accuracy. Molded explosive warheads penetrate armor and metal armor to channel the blast and inflict damage. Its disadvantage is that it is heavy for the number of rounds it can carry. \\n# ~You Can Use it too! Excavated Weapons~'):
        "Un lanciarazzi anticarro che, dicono, si usava nelle civiltà passate. La spinta speciale del razzo tiene bene il vento di lato, e il tiro è preciso. La testata a carica cava buca la corazza e le armature di metallo, ci infila dentro lo scoppio e fa danno. Il difetto è che pesa molto per quanti colpi porta. \\n# ~Puoi Usarle Anche Tu! Le Armi Riesumate~",

    # ---------------------------------------------------------- :62234
    (62234, 'A thin but fluffy blanket. Provides a comfortable sleep, but makes it hard to get up in the morning. VERY hard. \\n# ~Palmian Winter Fashion~'):
        "Una coperta sottile e però soffice. Fa dormire bene, ma alzarsi la mattina diventa dura. Molto dura. \\n# ~Palmia: Collezione Autunno-Inverno~",

    # ---------------------------------------------------------- :62236
    (62236, '\\"I have to get up and make breakfast soon...and finish the gloves I made last night... No... I\'m sleepy...I\'ll sleep a little longer...... just a little more.\\" \\n# ~words of a girl wrapped in a blanket~'):
        "\\\"Ora devo alzarmi e fare colazione... e finire i guanti di ieri sera... No... ho sonno... ancora un po'... solo un altro pochino.\\\" \\n# ~Parole di una Bambina Avvolta in una Coperta~",

    # ---------------------------------------------------------- :62600
    (62600, "Toolbox containing disposable medicines and medical instruments. It can heal wounds according to the user's dexterity and knowledge of biochemistry. It also greatly reduces the symptoms of paralysis, blindness, poisoning, and bleeding. \\n#~First aid at home~"):
        "Una cassetta con dentro medicine e attrezzi da medico usa e getta. Cura le ferite secondo la destrezza di chi la usa e quanta biochimica sa. E riduce di molto i sintomi di paralisi, cecità, veleno e sanguinamento. \\n#~Primo Soccorso in Casa~",

    # ---------------------------------------------------------- :62666
    (62666, 'A box of bullet and arrows. It can replenish arrow ammunition to the maximum except for time-stopping ammunition, but it is quite heavy. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una cassa con dentro frecce e munizioni. Ricarica al massimo tutto tranne le munizioni fermatempo, ma pesa parecchio. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :63521
    (63521, 'When used, the lion causes a nuclear explosion after the count. Although the lion is dead, it does not matter because it can be used as an atomic bomb. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un leone che, se lo si usa, dopo un conto alla rovescia fa un'esplosione nucleare. Il leone è morto, ma siccome funziona da bomba atomica non è un problema. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :63523
    (63523, '\\"A dead lion beats a live dog.\\" \\n# ~scribbling in a mysterious notebook~'):
        "\\\"Un leone morto val più di un cane vivo.\\\" \\n# ~Scarabocchi su un Quaderno Misterioso~",

    # ---------------------------------------------------------- :63937
    (63937, "Magical tool with a special gemstone built into it. By linking with the user, it changes the user's appearance and abilities. The change in appearance is largely dependent on the state of the user. They have the power to temporarily increase the user's strength and perception. Once used, it becomes unusable for a while. \\n# ~Arcane Almanac~"):
        "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco alza la Forza e la Percezione di chi lo usa. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64005
    (64005, "Magical tool with a special gemstone built into it. By linking with the user, it changes the user's appearance and abilities. The change in appearance is largely dependent on the state of the user. They have the power to temporarily increase the user's magical power and dexterity. Once used, it becomes unusable for a while. \\n# ~Arcane Almanac~"):
        "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco alza la Magia e la Destrezza di chi lo usa. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64073
    (64073, "Magical tool with a special gemstone built into it. By linking with the user, it changes the user's appearance and abilities. The change in appearance is largely dependent on the state of the user. They have the power to temporarily increase the user's speed and agility. Once used, it becomes unusable for a while. \\n# ~Arcane Almanac~"):
        "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco rende più veloci e alza la Schivata. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64141
    (64141, "Magical tool with a special gemstone built into it. By linking with the user, it changes the user's appearance and abilities. The change in appearance is largely dependent on the state of the user. They have the power to temporarily increase the user's defense and recovery capabilities. Once used, it becomes unusable for a while. \\n# ~Arcane Almanac~"):
        "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco alza la difesa e la capacità di recupero. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64209
    (64209, "Magical tool with a special gemstone built into it. By linking with the user, it changes the user's appearance and abilities. The change in appearance is largely dependent on the state of the user. They have the power to temporarily increase the user's all abilities in exchange for life. Once used, it becomes unusable for a while. \\n# ~Arcane Almanac~"):
        "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco alza tutte le doti di chi lo usa, ma il carico è forte e rode la vita. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64553
    (64553, "A mirror that connects to the fourth dimensional space by means of filled magic power. It can be used only a limited number of times, but it is useful for organizing luggage. There is an urban legend that if the mirror likes you, a hand will reach out from the mirror's surface and drag you in. In fact, there is a report of a girl who was grabbed by the sleeve while organizing her belongings and fought back by breaking all the fingers of her hand. \\n# ~Arcane Almanac~"):
        "Uno specchio che, con la forza magica di cui è carico, si collega allo spazio a quattro dimensioni. Si usa un numero limitato di volte, ma è comodo per mettere in ordine il carico. Gira una leggenda di città: se piaci allo specchio, dalla superficie esce una mano e ti tira dentro. E infatti c'è il rapporto di una ragazza che, mentre metteva in ordine, si è vista afferrare per la manica e l'ha respinta rompendo alla mano tutte le dita. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64678
    (64678, "A fine basket filled to the brim with food. Everyone can eat to their heart's content. It is ideal for a picnic with many people, but it is difficult to prepare the food and heavy because of the quantity. \\n# ~Supporting Roles in Kitchen~"):
        "Un bel cesto pieno zeppo di cibo. Ci si sazia tutti insieme. È l'ideale per un picnic in tanti, ma preparare tutto quel cibo è una fatica e, per la quantità, pesa. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :64741
    (64741, 'The key to the Cemetery of a Different Dimension, which is located between this world and the underworld. Since this key was produced, we have heard strange stories of people wandering into an eerie world full of coffins. It may be that the interference opens entrances to other places as well. \\n# ~Arcane Almanac~'):
        "La chiave del cimitero DD, che starebbe fra questo mondo e l'oltretomba. Da quando è stata fatta si sentono storie strane di gente finita per sbaglio in un mondo sinistro pieno di bare. Forse l'interferenza apre un ingresso anche altrove. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :64807
    (64807, 'A mysterious substance that cannot be understood with current technology. Think of an arm for an arm or a leg for a leg, and it is said that the part is attached to the body before you know it, as if it had been there from the beginning. The few people who have discovered it all say that it was lying around their feet when they came across it. Its origin is unknown. Only the discoverers can use its power, and its characteristic of disappearing after use makes it difficult to study. \\n# ~Bizarre Gossip~'):
        "Una materia misteriosa che la tecnica di oggi non sa spiegare. Basta pensare a un braccio, o a una gamba, e quel pezzo, dicono, ti si attacca addosso senza accorgersene, come se ci fosse sempre stato. I pochi che l'hanno trovata dicono tutti solo che se la sono vista rotolare ai piedi, e da dove venga non si sa. La usano soltanto loro e sparisce appena usata: per questo studiarla è difficile. \\n# ~Dicerie Bizzarre~",

    # ---------------------------------------------------------- :65195
    (65195, "A glove used to challenge someone to a duel. It possesses the power of a curse, and the person who throws the glove at the opponent will not be able to escape from the map until the duel is settled. The winner of the duel will take a larger amount of his or her opponent's possessions.\\n# ~Heated Duelists~"):
        "Il guanto che si usa per sfidare a duello. Che nel duello l'altro resti ferito o ci muoia, il karma non ne risente. Ha una forza come di maledizione: chi lancia il guanto non può più fuggire da quella mappa finché la cosa non è decisa. Chi vince il duello si prende una parte più grossa delle cose dell'altro.\\n# ~Duellanti Ardenti~",

    # ---------------------------------------------------------- :65197
    (65197, '\\"Scut!\\" \\n# ~words of the victim to the curse~'):
        "\\\"Menti.\\\" \\n# ~Parole di Chi è Stato Maledetto~",

    # ---------------------------------------------------------- :65464
    (65464, 'Magical tool with the name of [insight]. When you look into an object while holding it to your eyes, you can temporarily burn information about the object into the lenses. It is expensive and disposable, so it is not used by informants. \\n# ~Arcane Almanac~'):
        "Un oggetto magico che porta il nome di Intuito. Tenendolo all'occhio e guardandoci dentro un bersaglio, la lente ne imprime per un poco i dati. Costa il suo e si usa una volta sola, quindi gli informatori non lo adoperano. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :65466
    (65466, '\\"Well, isn\'t it rude to stare at people with something like that?\\" \\n# ~Worried Citizen~'):
        "\\\"M-ma non è scortese fissare la gente con un affare simile?\\\" \\n# ~Parole di un Cittadino in Affanno~",

    # ---------------------------------------------------------- :66075
    (66075, 'Amulet is blessed by the eight gods and one other mysterious deity who oversees the current Irva. At the center of the amulet is a small symbol of an eye or a pillar, which is not clear. It has no particular power to repel demons, but it is said that wearing it will keep you from being deceived by the voice of the god who urges you to convert to a new religion. \\n# ~Arcane Almanac~'):
        "Un amuleto che ha la protezione delle otto divinità che reggono l'Irva di oggi e di una nona, misteriosa. Al centro c'è disegnato piccolo un segno che non si capisce se sia un occhio o un pilastro. Non ha una vera forza contro i demoni, ma pare che a portarlo addosso non ci si lasci più confondere dalla voce che spinge a cambiare dio. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :67666
    (67666, 'Machine with many music discs built in. It has a row of song titles and buttons that allow you to select and play any song you wish. It shines beautifully with colorful lighting. \\n# ~Music of the Melodious Irva~'):
        "Una macchina con dentro tanti dischi musicali. Ha una fila di titoli e di pulsanti, e si sceglie il brano da far suonare. Brilla bella di luci colorate. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :68587
    (68587, "Illegal smoking paraphernalia handled on the black market. Those who use it are punished. When traded, it is disguised as an ordinary pack of cigarettes. It contains a narcotic made from dried crimberries, and when used, it instantly elevates the smoker's mood. The side effect is known to be depression, so unless the recipient is a submissive, the drug is likely to be rejected. \\n# ~Special Edition! Behind-the-scenes Favorites!~"):
        "Un attrezzo da fumo fuorilegge, di quelli che passano dal mercato nero. Chi lo usa viene punito. Nelle trattative, di nome, lo mascherano da kiseru comune. Dentro ha una droga fatta di crimberry essiccate, e a usarlo l'umore si alza di colpo. Si sa che come effetto secondario porta malinconia, quindi offrirlo a chi non ti obbedisce non serve: rifiuterà. \\n# ~Selezione! I Piaceri Clandestini~",

    # ---------------------------------------------------------- :68717
    (68717, 'Treasure that activates the core of Nefia and awakens its true power. Its power also affects the monsters inside Nefia, causing them to go berserk. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una gemma che attiva il nucleo della Nefia e ne sveglia la vera forza. Quella forza agisce anche sui mostri dentro la Nefia, e li fa imbestialire. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :68783
    (68783, "A red thread of destiny, spun by the souls of those bound together with a bond. No matter how the world changes, no matter how time goes, it will bring them together again at the end of time, beyond the infinite worlds. \\n# ~Aion's Prophecy~"):
        "Il filo rosso del destino, filato con le anime di chi è legato da un vincolo. Per quante volte il mondo cambi e il tempo giri, in capo al tempo, di là dai mondi infiniti, li legherà di nuovo l'uno all'altro. \\n# ~La Profezia di Aion~",

    # ---------------------------------------------------------- :69454
    (69454, "It can provide nutrients to plants, resulting in rapid growth and improved quality. Because of the unusual rate of nutrient absorption in many of Irva's crops, the effect is immediate but not sustainable. \\n# ~Agriculture and its New Possibilities~"):
        "Dà nutrimento alle piante, e porta crescita rapida e qualità migliore. Molte colture di Irva assorbono il nutrimento a una velocità fuori dal comune, quindi l'effetto è immediato ma non dura. \\n# ~L'Agricoltura e le sue Nuove Possibilità~",

    # ---------------------------------------------------------- :70333
    (70333, "A complete set of ingredients and utensils that can be used up. Even if you have no cooking skills, you can easily complete homemade chocolates. As long as you don't mess around too much. \\n# ~Supporting Roles in Kitchen~"):
        "Un attrezzo usa e getta con dentro tutto, dagli ingredienti agli arnesi. Anche senza una briciola di Cucina il cioccolato fatto in casa viene bene. Purché non ci si metta a fare gli scemi. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :70598
    (70598, "Using the magical crystals as the nucleus, a pseudo-body is constructed with the cultured remains in a coffin. After completion, it is used mainly as a vessel for carrying around. The strength of the undead that emerges depends on the user's anatomy and alchemical skills. \\n# ~Necromancy for Noobs~"):
        "Con un cristallo di forza magica per nucleo, dentro la bara si costruisce un corpo provvisorio con i resti coltivati. Finito che è, serve soprattutto da recipiente per portarlo in giro. Quanto è forte il non morto che ne esce dipende da Anatomia e Alchimia di chi lo fa. \\n# ~Negromanzia per Principianti~",

    # ---------------------------------------------------------- :70817
    (70817, 'A quill pen imbued with astral light. It interferes exclusively with the existence records of life in this world...the Akashic Records, and rewrites them so that the subject exists as another person. The resulting person is the identical person with the same memories and personality, but free from any original role or destiny. However, the user is required to have at least half the existence level of the subject. Intervention requires material \\"magic ink\\" according to the subject\'s level of existence, and will fail if the subject does not sincerely desire it. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una penna d'oca intrisa di luce astrale. Interviene, entro un limite, sul registro akashico, dove sta scritta l'esistenza di ogni vita di questo mondo, e lo riscrive perché del soggetto ne esista un secondo. Quello in più è la stessa persona, con gli stessi ricordi e lo stesso carattere, ma è sciolto dal ruolo e dal destino che aveva. Chi la usa però deve avere almeno metà del grado di esistenza del soggetto. E l'intervento chiede, secondo quel grado, l'inchiostro magico come materia: se il soggetto non lo vuole con tutto il cuore, fallisce. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71924
    (71924, 'Doll that has been passed down from generation to generation as a charm among cleaners. It is said to move by itself in the night and hunt the G-demons. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una bambola che fra gli addetti alle pulizie si tramanda da tempo come amuleto. Si dice che nel cuore della notte si metta in moto da sola e vada a caccia dei demoni neri e marroni. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :72484
    (72484, 'Providing an occupation after the name, no matter how bullshit it may sound, will get you the job. However, it does not necessarily mean that you will be competent for that position. \\n# ~Extra Issue: Weird Items~'):
        "Se dopo il nome ci si scrive un mestiere, per quanto assurdo sia scritto, quel mestiere lo si ottiene. Non è detto però che vengano anche le doti che gli si addicono. \\n# ~Speciale: Oggetti Sospetti Comprati e Provati~",

    # ---------------------------------------------------------- :72486
    (72486, '\\"It is up to the customer to decide how to use this item.\\" \\n# ~Words from an Shady, Old Shopkeeper~'):
        "\\\"Come usare questo articolo sta al cliente deciderlo.\\\" \\n# ~Parole del Vecchio Bottegaio del Vicolo~",

    # ---------------------------------------------------------- :72550
    (72550, 'Mysterious stone mask. With the power of the red stone of the philosopher, it is said that when worn, the body is reconstructed and reborn into a different race. \\n# ~Extra Issue: Weird Items~'):
        "Una maschera misteriosa. Dicono che, per la forza della pietra rossa del saggio che ci è incastonata, a portarla il corpo si ricompone e si rinasce in un'altra razza. \\n# ~Alchimia: Grande Compendio dei Divieti~",

    # ---------------------------------------------------------- :72552
    (72552, '\\"Stop playing the race card!\\" \\n# ~Jonah, the Adventurer~'):
        "\\\"E piantala di giocarti la carta della razza!\\\" \\n# ~<Jonah> l'avventuriero~",

# 7 voci, 0 ambigue

    # ---------------------------------------------------------- :72620
    (72620, 'A whistle that produces a sound that can only be heard by dogs. It may look like a simple flute, but it is in fact a magical tool, and is absolutely inaudible to all but the dogs. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un fischietto che fa un suono che sentono solo i cani. Sembra un fischietto qualunque, ma è un oggetto magico a tutti gli effetti, e a parte i cani non lo sente proprio nessuno, mai, in nessun modo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :73020
    (73020, 'It is a gemstone that is supposed to bring about evolution when used on certain allies who meet the requirements.\\n# ~Irva Fantasy Encyclopedia~'):
        "È una gemma che, usata su certi compagni che ne abbiano i requisiti, porterebbe un'evoluzione.\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :73288
    (73288, 'A flag used by commanders and others to communicate orders. It can be used to give instructions to fellow allies even when your voices cannot be heard. \\n# ~Command and Control on the Battlefield~'):
        "Una bandiera che i comandanti e simili usano per trasmettere gli ordini. Serve a dare istruzioni ai compagni anche quando la voce non arriva. \\n# ~Comando e Controllo sul Campo di Battaglia~",

    # ---------------------------------------------------------- :73698
    (73698, 'A statue in the shape of the God of Elements. created by a renowned artist. Its appearance is full of dignity. \\n# ~Lumiest Art Catalogue~'):
        "Una statua che raffigura il dio degli elementi, opera di un artista famoso. Il portamento è pieno di dignità. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :73765
    (73765, 'A statue in the shape of the Goddess of Wealth, created by a renowned artist. The artist was required to sign a contract to give 30% of the sale price to the Yacatect. \\n# ~Lumiest Art Catalogue~'):
        "Una statua che raffigura la dea della ricchezza, opera di un artista famoso. Per farla, l'artista fu costretto a firmare un patto: tre decimi del prezzo di vendita vanno a Yacatect. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :73828
    (73828, "① At the start of your turn: You can draw until you had 5 card in your hand. ② Once per turn: you can discard 1 card; Send cards from the top of your Deck to the GY equal to this card's rank. ③ At the end of the turn, if you have no cards left in your Deck, you lose the Duel. And if you do, shuffle all cards in your GY into your Deck. ④ You can skip your action for 30 turns. If you do, shuffle all cards in your GY into your Deck. Then, you can select any available deck for the rest of this duel.\\n# ~Heated Duelists~"):
        "(effetto non attivo) 1) All'inizio del turno peschi dal mazzo fino ad avere cinque carte in mano. 2) Una volta per turno puoi scartare una carta dalla mano e attivarne l'effetto; poi scarti dal mazzo tante carte quanto vale la carta attivata. 3) Alla fine del turno in cui il mazzo resta a zero carte, chi comanda questo oggetto va a 0 HP. Dopo, tutte le carte scartate tornano nel mazzo e si mescola. 4) Per 30 turni puoi saltare il tuo agire. Se riesce, tutte le carte scartate tornano nel mazzo e si mescola; poi scegli un mazzo qualunque fra quelli che puoi usare, e da lì in avanti giochi con quello.\\n# ~Duellanti Ardenti~",

# 36 voci, 0 ambigue
}
