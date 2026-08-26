# -*- coding: utf-8 -*-
"""102a - Lotto 1 di `db_card.hsp`: le prime 46 carte (righe 1-600).

E' `scratchpad/modello-rete6-barre.py` con le rese di questa zona: le reti sono
quelle, riga per riga, e non vanno toccate qui.

⚠️⚠️ **QUESTA PROSA NON STA NELLA CARTA: STA NEL PANNELLO `x`.**
`command.hsp:16025` mette `cardrefskill` in `description(0)` quando si esamina
un **cadavere**, una **carta** o una **figurina**. E li' l'impaginazione non e'
una `gmes`: e' un taglio a conteggio di caratteri scritto a mano
(`command.hsp:16802`-`:16829`), che spezza a 70 caratteri e torna indietro al
massimo di 15 per cercare uno spazio, una virgola o un punto. Se in quella
finestra non ne trova, **spezza la parola di netto**. La rete che lo misura e'
`scratchpad/_102-carta-conoscenza.py`, e va lanciata dopo ogni lotto.

⭐ **Si traduce dal giapponese, e l'inglese di monte taglia.** Quattro carte di
questo lotto hanno in giapponese una frase che l'inglese non porta — la piu'
netta e' `:4`, dove manca il punto debole di Momalaria (senza invito in casa non
entra), che e' la battuta su cui sta in piedi tutta la carta.

⚠️ **Il nome della creatura e' gia' reso** in `dizionario/db_card.hsp.jsonl`
(il `cardrefn` poche righe sotto): quando la prosa nomina la creatura, la nomina
con quello. Il dossier che appaia le due cose e' `scratchpad/_102-dossier.py`.

⚠️ **Niente virgolette e niente caporali**: in tutto il dizionario non c'e' un
solo `"` dentro una statica, e `«»` non ci sono affatto. In CP932 diventerebbero
caratteri a doppia larghezza.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :4 Momalaria
    # ⚠️ L'inglese lascia cadere l'ultima frase del giapponese — 招かれないと家に
    #    入れないのが弱点 — che e' la battuta sul vampiro e il senso della carta.
    (4, 'Big Mosquito Mutant: A special variant with enlarged head and limbs. If accidentally invited into homes, they breed rapidly and aggressively attack inhabitants. These incidents cause citizens to be unable to return home, congregating in the streets.'):
        "Esemplare speciale della zanzara gigante, con testa e zampe mutate. Visita le case, e se per distrazione la si invita a entrare si moltiplica senza freni e aggredisce gli abitanti. È anche la ragione per cui certi cittadini non tornano più a casa e restano a bighellonare per le strade. Il punto debole: senza invito, in casa non entra.",

    # ---------------------------------------------------------- :17 la zanzara gigante
    (17, "Mosquito: The number one human killer in modern Irva. Most deaths occur at home, crushed by these unassuming insects. Even an Indian Elephant or mammoth is no match, as mosquitoes don't discriminate by gender or breeding season."):
        "Il primo ammazzauomini dell'Irva di oggi. Non dà nell'occhio, ma il settanta-ottanta per cento delle morti porta la sua firma: quasi tutti muoiono in casa propria, sotto la zanzara gigante. Elefante indiano o mammut per lei è lo stesso, li stende a pugni; e succhia il sangue senza badare al sesso né alla stagione della deposizione.",

    # ---------------------------------------------------------- :30 Regina Sedona
    (30, "Queen Sedona: A sailing ship that sank during its maiden voyage to Port Kapul due to an Etherwind. Though its hull was torn apart, it inexplicably transformed into a humanoid form and reached its destination. It acts haughty like a queen, but being originally a merchant vessel, it's quite money-oriented and lacks combat strength."):
        "Un veliero che sarebbe dovuto affondare per il vento d'etere durante il viaggio inaugurale verso Porto Kapul. Lo scafo si squarciò e finì in pasto al mare, ma in quel momento accadde qualcosa di strano: prese una forma umana e arrivò lo stesso al porto di destinazione. Si dà arie da regina, ma era una nave mercantile: tiene ai soldi e in battaglia vale poco.",

    # ---------------------------------------------------------- :43 Propa-gandar
    (43, 'The official PR character of the Yerles Army. Created to spend leftover promotion funds, it was made using surplus and rejected parts, resulting in an overly powerful machine for just PR purposes.'):
        "La mascotte ufficiale dell'esercito di Yerles. Per esaurire il budget pubblicitario avanzato fecero costruire al capo progettista un esemplare vero da esposizione, e quello riciclò gli scarti di lavorazione e i pezzi bocciati delle armi decisive. Ne è uscita una macchina assurdamente potente, e solo per farsi pubblicità.",

    # ---------------------------------------------------------- :56 Carrello Deviato
    # ⓘ E' il dilemma del carrello, e il giapponese lo dice con i numeri: cinque
    #    operai sul percorso, uno sul binario di scarto. Si tengono.
    (56, 'Character designated to educate about the dangers of minecart accidents. If encountered with 5 workers ahead and 1 at a fork, it will do a multi-track drift to run all of them down.'):
        "Un personaggio nato per sensibilizzare sui pericoli degli incidenti in miniera. Se davanti ha cinque operai e sul binario di scarto uno solo, è il tipo che esce dalle rotaie e va ad arrotarli tutti quanti. Il carico è minerale tinto del sangue delle vittime.",

    # ---------------------------------------------------------- :69 lo zibetto divino
    (69, "Also known as the Hakubishin. As its name suggests, it is characterized by a white stripe on its nose. Said to harbor a shard of the Lightning God within, enabling it to move at high speeds by riding lightning currents, earning it the moniker of the 'Thunder Beast'. While often mistaken for a raccoon, it is more closely related to cats and is adept at climbing trees."):
        "Lo zibetto delle palme mascherato. Come dice il nome, lo si riconosce dalla riga bianca sul dorso del naso. Porta in sé una scheggia del dio del fulmine e cavalca la folgore per spostarsi velocissimo: per questo lo chiamano anche la bestia del tuono. Lo scambiano spesso per un cane procione, ma è piuttosto parente del gatto ed è bravissimo ad arrampicarsi sugli alberi.",

    # ---------------------------------------------------------- :82 il tasso arroccato
    # ⚠️ 同じ穴のムジナ e' un modo di dire — due che stanno nella stessa buca, cioe'
    #    della stessa risma. Si rende il modo di dire, non le parole.
    (82, 'Also known as the Badger (Mujina). It forms a dense, defensive formation by surrounding allies. Despite their similar appearance, they are not related to raccoons. Sometimes, they occupy holes dug by raccoons, causing confusion within them.'):
        "Detto anche mujina. Circonda i compagni e forma uno schieramento serrato dall'ottima difesa. Non è parente del cane procione, ma gli somiglia, e capita che il cane procione si installi senza permesso nella tana che il tasso ha scavato: una confusione continua. Il modo di dire su quei due che stanno nella stessa buca non aiuta.",

    # ---------------------------------------------------------- :95 il magicervo
    (95, 'A creature that should never be placed next to a horse. It has an enormous appetite - having just a few of these in a mountain can strip it bare, turning it into a barren, bald mountain. It is covered in parasites and leaves a trail of these parasites in the areas it has ravaged by feeding on plants.'):
        "Una creatura che non va messa accanto a un cavallo. Ha una fame smisurata: bastano pochi esemplari su un monte perché il monte diventi davvero pelato. È coperto di parassiti fino all'inverosimile, e li lascia dietro di sé in ogni zona che ha spogliato delle piante.",

    # ---------------------------------------------------------- :108 la zecca magica
    # ⚠️ L'inglese scrive `a Magic` per マジカ: e' il magicervo, e il nome e' gia' reso.
    (108, 'Ginat ticks that usually lives attached to a Magic. It subsists by drawing a minimal amount of blood and magical power from its host. When the host dies, it drinks as much as it can and detaches in a bloated state. Be careful not to poke it, as it may burst.'):
        "Una zecca di taglia grossa. Di solito vive attaccata al magicervo e ne succhia il minimo indispensabile di sangue e di potere magico. Quando si accorge che l'ospite è morto, succhia tutto quello che può e si stacca gonfia da scoppiare. E attenzione a stuzzicarla male, perché scoppia davvero.",

    # ---------------------------------------------------------- :121 il procione stizzoso
    (121, 'Crop destroying pests. Many people naively try to keep it as a pet because of its cute appearance, but its wild temperament eventually makes it unbearable to keep. This is part of its strategy to expand its habitat - careless owners intentionally release them in new areas. It often gets blamed for the crop destruction and has the raccoon dog (tanuki) taking the fall because of their similar appearance.'):
        "Un animale nocivo che devasta i campi. Molti ignoranti lo prendono in casa perché ha l'aria carina, ma ha un pessimo carattere e tenerlo diventa via via più duro. E questa è la sua strategia: farsi abbandonare apposta dove non viveva, e allargare così il proprio territorio. Somigliandogli, il cane procione si prende spesso la colpa delle sue razzie.",

    # ---------------------------------------------------------- :134 il furgoncino ladro
    (134, "A light truck that has derailed into evil paths due to abduction and trafficking. It steals and unroots entire crops before they're fully ripe, then sells them for a paltry sum on the streets. Even if caught, it deliberately only speaks in truck language, making it impossible to understand what it's saying, which is utterly frustrating."):
        "Un furgoncino finito al servizio del male fra rapimenti e compravendite. Ruba fino all'ultima radice i raccolti ancora acerbi e li rivende per strada a prezzi da fame. Anche quando lo si prende parla apposta soltanto la lingua dei furgoncini, e non si capisce niente di quello che dice: il peggio.",

    # ---------------------------------------------------------- :147 lo sbudellatore
    (147, 'Motuhegui (Organ-Mauler), having become addicted to the taste of organs, they can no longer revert to their previous diet. Even if prey is still alive, they cannot resist the urge to tear open its belly and feed. Compared to other bears and monsters, their physical prowess is in a completely different league, making them extremely dangerous.'):
        "Ha assaggiato le interiora, ne è rimasto schiavo e non è più tornato alla dieta di prima. Non aspetta nemmeno che la preda sia morta: le apre il ventre e divora. Anche fra gli altri mostri della famiglia degli orsi la sua stazza è di un altro ordine, ed è pericolosissimo.",

    # ---------------------------------------------------------- :160 lo sbudellatore marmocchio
    (160, 'A Motuhegui (Organ-Mauler) Cub, already boasting significant power and toughness. A person punching it with all their might would barely faze it, while a single scratch could easily take off their face. Together with its mother, it gleefully tears out and devours the organs of children.'):
        "È il cucciolo dello sbudellatore, e già così vanta una forza e una resistenza notevoli. Un uomo comune può tirargli in faccia un pugno con tutta la disperazione che ha, e quello non si sposta; una sua zampata, invece, la faccia la porta via. Insieme alla mamma tira fuori le interiora dei bambini e se le gusta.",

    # ---------------------------------------------------------- :173 la strega di cuori
    # ⚠️ `ランク×5％` si scrive `rango x 5%`, come fa l'inglese: il segno `×` in
    #    CP932 e' un carattere a doppia larghezza.
    (173, 'Spirits that inhabit the cards. By synchronising with the user through the card, it powers up and changes its appearance. A witch who bewitches people\'s hearts with her lovely gestures and smiles. Apart from the normal magic control judgement, this monster has a rank x 5% chance to not hit allies.'):
        "Uno spirito che abita nelle carte. Sincronizzandosi con chi la usa attraverso la carta cresce di potenza e cambia aspetto. È una strega che semina sorrisi con gesti graziosi e confonde il cuore della gente. Fuori squadra, questo mostro ha una probabilità di rango x 5% di non coinvolgere gli alleati, oltre alla normale prova di controllo del potere magico.",

    # ---------------------------------------------------------- :186 gli occhi di quadri
    (186, 'Spirits that inhabit the cards. By synchronising with the user through the card, it powers up and changes its appearance. The crimson diamonds on its body are said to function as eyes. Damage taken by this monster is reduced by rank x 2%.'):
        "Uno spirito che abita nelle carte. Sincronizzandosi con chi lo usa attraverso la carta cresce di potenza e cambia aspetto. Pare che i diamanti scarlatti che porta sul corpo gli facciano anche da occhi. Fuori squadra, questo mostro subisce rango x 2% di danno in meno.",

    # ---------------------------------------------------------- :199 la piuma di fiori
    (199, 'Spirits that inhabit the cards. By synchronising with the user through the card, it powers up and changes its appearance. Monstrous bird that attacks enemies by creating tremendous winds with its magical wings. The speed of this monster is increased by rank x 2%.'):
        "Uno spirito che abita nelle carte. Sincronizzandosi con chi la usa attraverso la carta cresce di potenza e cambia aspetto. È un uccellaccio che con le ali intrise di magia solleva venti tremendi e con quelli attacca. Fuori squadra, questo mostro guadagna rango x 2% di velocità.",

    # ---------------------------------------------------------- :212 il guerriero di picche
    (212, 'Spirits that inhabit the cards. By synchronising with the user through the card, it powers up and changes its appearance. Armoured warrior wielding a spade-shaped sword. Not particularly interested in speed. Damage inflicted by this monster is increased by rank x 2%.'):
        "Uno spirito che abita nelle carte. Sincronizzandosi con chi lo usa attraverso la carta cresce di potenza e cambia aspetto. È un guerriero in armatura che brandisce una spada a forma di picca. La velocità non lo interessa granché. Fuori squadra, questo mostro infligge rango x 2% di danno in più.",

    # ---------------------------------------------------------- :225 Lupo Divino
    (225, 'Giant blue wolf god. Likes to crunch bones and sip marrow. As a result of chewing up quite a few gods during the War of the Gods, he was regarded as dangerous and sealed away. The werewolves are working in the dark to break the seal.'):
        "Il dio lupo, azzurro e immenso. Gli piace stritolare le ossa a morsi e succhiarne il midollo. Nella grande guerra delle divinità ne sbranò un buon numero, e per questo lo giudicarono pericoloso e lo sigillarono. I licantropi tramano nell'ombra per spezzare quel sigillo.",

    # ---------------------------------------------------------- :238 Nove Code Dorate
    # ⚠️ rete 3: le prime due frasi giapponesi stanno anche in
    #    `tcg_custom.hsp:1956`, gia' rese nella carta del gioco di carte. La
    #    seconda si ricopia parola per parola: e' la stessa frase, e il
    #    giocatore puo' vederle a poca distanza.
    (238, 'Fox god with nine fluffy tails. It is apparently difficult to move each tail separately. It lost its power and turned to stone, but was found to be able to revive itself by taking over the rituals of the werewolves. Today, the foxes, continue to deceive people and wolves alike.'):
        "La divinità delle volpi magiche, con nove code morbidissime. Muoverle una per una, dicono, non è affatto semplice. Aveva perso il potere ed era diventata pietra, finché non si scoprì che poteva risorgere impadronendosi del rito dei licantropi. Anche oggi le volpi al suo servizio giocano d'inganno con uomini e lupi.",

    # ---------------------------------------------------------- :251 Kamikakushi
    (251, 'Origami in which a higher spirit is imbued by a hidden technique. A higher level being of the Shiki-Origami. It instantly absorbs in the surrounding Shiki-Origami and displays its mighty power.'):
        "Un origami in cui una tecnica segreta ha fatto abitare uno spirito di rango alto. È la forma superiore delle divinità di carta piegata. Assorbe in un istante quelli che ha attorno e sprigiona una forza enorme.",

    # ---------------------------------------------------------- :264 il ratto fortissimo
    # ⚠️ Il nome della regione, サイキョウ, suona come 最強 «il piu' forte»: senza
    #    dirlo l'equivoco di tutta la carta non si capisce. L'inglese lo spiega
    #    e fa bene.
    (264, 'Yokai rats hail from a region called Saikyo. Its specialities are hypnosis and foretelling. They are frequently misunderstood due to Saikyo means the strongest and get into trouble, and each time they have been let down when their misunderstandings are cleared up. After years of humiliation, he has decided to actually become the strongest and is continuing his efforts.'):
        "Un ratto stregato originario della regione di Saikyo. È bravo nell'ipnosi e nella profezia. Siccome Saikyo suona come il più forte, lo scambiano di continuo per tale e finisce in guai noiosissimi; e ogni volta che chiarisce l'equivoco qualcuno resta deluso, come se fosse colpa sua. Umiliato per anni, ha deciso di diventare davvero il più forte, e continua ad allenarsi.",

    # ---------------------------------------------------------- :277 la cavia suprema
    (277, 'In biochemical civilisation, guinea pigs were also used for animal experiments. There is a record of a guinea pig that escaped from a research institute after becoming more powerful than expected when used as an baseline specimen for ultimate enhancement experiments. Apparently, they were bred in the field, and their offspring are still making pui-pui sounds even today.'):
        "Anche nella civiltà biochimica le cavie servivano per gli esperimenti sugli animali. Resta agli atti che una di esse, usata come base per l'esperimento di potenziamento supremo, crebbe di forza oltre ogni previsione e fuggì dal laboratorio. A quanto pare si è riprodotta all'aperto, e ancora oggi i suoi discendenti vanno in giro a fare pui pui.",

    # ---------------------------------------------------------- :290 il topolino della montagna
    # ⭐ 大山鳴動して鼠一匹 e' un proverbio che l'italiano ha uguale: la montagna
    #    partorisce un topolino. Il nome della carta ci sta gia' sopra.
    (290, "Its legs are substandardly developed and its serious kicks have enough impact to shake a mountain. If this rat comes down from a moving mountain that rumbles, don't just take it easy, take it seriously. It may have been chased from its home by a monster that even its kicks cannot defeat."):
        "Ha le zampe sviluppate fuori da ogni misura, e un suo calcio dato sul serio scuote la montagna. Se la montagna rimbomba e trema e poi ne esce questo topo, invece di restare delusi conviene prenderla sul serio: può darsi che dalla tana lo abbia cacciato un mostro che nemmeno i suoi calci abbattono.",

    # ---------------------------------------------------------- :303 la cavia dopata
    (303, 'Experimental animals used for potion development in Eulderna. They mutated during repeated experiments and formed organs that store and synthesise the administered drugs... commonly known as a potion bag. They disperse the paralysing drugs synthesised in their bodies, incapacitating the researchers, and then escaped.'):
        "Un animale da laboratorio usato a Eulderna per mettere a punto le pozioni. A furia di esperimenti è mutata e le si è formato un organo che immagazzina e sintetizza i farmaci somministrati: la cosiddetta sacca delle pozioni. Ha sparso attorno il paralizzante prodotto dentro il proprio corpo, ha messo fuori gioco i ricercatori ed è fuggita.",

    # ---------------------------------------------------------- :316 il degu pistolero
    (316, 'They have particularly good eyes and ears among rats, and perform mercenary work as scouts. They are also highly sociable and often get together with their friends for strategy meetings.'):
        "Fra i roditori è quello con la vista e l'udito migliori, e si vende come mercenario nel ruolo di esploratore. È anche molto socievole, e spesso si raduna con i compagni per fare consiglio di guerra.",

    # ---------------------------------------------------------- :329 il ratto impetuoso
    (329, 'Humanoid giant gerbils. There are no humans inside. They are not very good at direct combat, and will approach and attack at full speed when their prey is fighting other creatures. The large rats are classified as rats and the small ones as mice, although this is not important.'):
        "Un enorme ratto di fogna dalla forma umana. Dentro non c'è nessuno. Nello scontro diretto non è granché: aspetta che la preda sia impegnata contro un'altra creatura, poi le piomba addosso a tutta velocità. Nota inutile: i roditori grossi si chiamano ratti, quelli piccoli topi.",

    # ---------------------------------------------------------- :342 il ratto saltatore
    (342, 'Rats that stand up on their long hind legs and move around by hopping around. When it gets serious, it can leap vertically to a considerable altitude, and its small body is sure to lose sight of you. They crush the skulls of their enemies with a dropkick that carries the momentum of their fall.'):
        "Un topo che si rizza sulle lunghe zampe posteriori e si sposta a balzi. Quando fa sul serio salta in verticale a un'altezza notevole, e siccome è anche piccolo lo si perde di vista di sicuro. Con un calcio di tallone caricato dalla caduta sfonda il cranio del nemico.",

    # ---------------------------------------------------------- :355 il cincillà mastodontico
    (355, 'A type of rat that is damn large in size. When attacked by enemies, they resist by spraying smelly liquid. Because of their large size and athleticism, if you want to keep one, you will need damn big furnitures and a damn big house.'):
        "Una specie di roditore mastodontico. Se lo assalgono si difende spruzzando un liquido puzzolente. È grosso e pieno di energie, quindi per tenerlo in casa servono mobili mastodontici e una casa mastodontica.",

    # ---------------------------------------------------------- :368 l'aeroplanino di carta
    (368, 'Origami paper in which minor deities or spirits dwell. It flies straight ahead regardless of the crosswind. The tip is not only a little painful when it stings, but also very dangerous because it explodes when it concentrates magic power.'):
        "Un origami in cui abita un dio o uno spirito di rango basso. Vola dritto anche con il vento di traverso. E quando la punta si conficca non fa un male sopportabile: concentra il potere magico ed esplode, il che lo rende pericolosissimo.",

    # ---------------------------------------------------------- :381 lo shuriken di carta
    (381, 'Origami paper in which minor deities or spirits dwell. It has jagged edges like a hacksaw, and is designed to cut through the skin and suck up blood. It flies while spinning at high speed, making it dangerous.'):
        "Un origami in cui abita un dio o uno spirito di rango basso. Ha i bordi seghettati come una lama da taglio, fatti apposta per aprire la pelle e risucchiare il sangue. Vola ruotando ad alta velocità, ed è pericoloso.",

    # ---------------------------------------------------------- :394 la gru di carta ammaliante
    (394, 'Origami paper in which minor deities or spirits dwell. It uses illusionary movements and magic to bewitch opponents, and can be dispatched in large quantities causing them to incur unimaginable costs for storage and disposal.'):
        "Un origami in cui abita un dio o uno spirito di rango basso. Confonde l'avversario con movenze inspiegabili e con la magia, e se lo si spedisce a qualcuno in grande quantità gli si fa spendere in custodia e smaltimento molto più di quanto immagini.",

    # ---------------------------------------------------------- :407 il kappa redivivo
    (407, 'Extinct from the wild, when their numbers were declining due to water pollution, they were exterminated by cucumber farmers. Individuals caught by sushi restaurants and forced to work underground could not withstand the harsh working conditions. They were also apparently robbed of their plates and used as shop crockery.'):
        "Il numero era già calato per l'inquinamento delle acque quando i coltivatori di cetrioli finirono di sterminarli: allo stato brado si sono estinti. Nemmeno gli esemplari catturati dai ristoranti di sushi e costretti ai lavori forzati nei sottoscala hanno retto a quelle condizioni. Pare che togliessero loro anche il piatto dalla testa, per usarlo come stoviglia del locale.",

    # ---------------------------------------------------------- :420 la tigre dai denti a sciabola rediviva
    (420, 'Ancient tiger. It specialised in hunting large, slow-moving beasts with its large sabre-shaped tusks. It was too specialised to hunt smaller beasts, so they perished together with it when its main prey became extinct. Sometimes their tusks and jawbones were damaged by biting too vigorously.'):
        "Una tigre antica. Con le grandi zanne a sciabola cacciava di preferenza le bestie grosse e lente. Si era specializzata troppo per prendere prede piccole, e quando la sua preda principale si estinse si estinse con lei. Si dice che a volte, mordendo con troppa foga, si rompesse zanne e mascella.",

    # ---------------------------------------------------------- :433 il lupo atroce redivivo
    (433, 'Ancient wolves with sharp eyes. They used to hunt in packs, but as a result of climate change, which reduced prey in their habitat, they were unable to sustain their packs and perished.'):
        "Un lupo antico dallo sguardo tagliente. Cacciava guidando il branco, ma il mutare del clima ridusse le prede del suo territorio: non riuscì più a tenere insieme il branco e si estinse.",

    # ---------------------------------------------------------- :446 il panda gigante redivivo
    (446, 'Ancient bear with distinctive black-and-white pattern. Bamboo is its staple food, but as it is too nutritionally depleted, it sometimes attacks and eats fish and animals, as bears do. They perished because their habitat was continually fragmented by humans and because they had a severe predilection for the opposite sex, making it difficult for them to reproduce.'):
        "Un orso antico dalla livrea bianca e nera inconfondibile. Si nutre soprattutto di bambù, ma il bambù nutre troppo poco, e allora ogni tanto fa l'orso e assale pesci e animali per mangiarli. Si è estinto perché gli uomini gli hanno spezzettato il territorio e perché in fatto di partner era troppo schizzinoso: riprodursi gli era diventato difficile.",

    # ---------------------------------------------------------- :459 il megacanguro redivivo
    (459, 'Ancient beast that evolved into a behemoth, if not a million times larger. The continuous attacks produced by the love between parent and child were too strong by the standards of the time and thoroughly destroyed the environment. It was greatly weakened by humans, who saw it as dangerous, and then exterminated en masse.'):
        "Una bestia antica evolutasi fino a farsi gigantesca, se non proprio un milione di volte più grande. La raffica di colpi che nasce dall'amore fra madre e figlio era, per gli standard di allora, troppo forte, e devastò l'ambiente da cima a fondo. Gli uomini la giudicarono pericolosa, la indebolirono parecchio e poi la sterminarono tutta in una volta.",

    # ---------------------------------------------------------- :472 la capra rediviva
    (472, "Ancient beast resembling a shorn sheep. When it was about to be sacrificed to the devil, it made a contract with the devil in a moment of desperation and became almost immortal. It is said to have brought destruction and chaos, but was destroyed when the repercussions of breaking too many of the world's laws came at once."):
        "Una bestia antica identica a una pecora tosata. Quando stava per essere offerta in sacrificio a un demone, nella disperazione strinse lei stessa un patto con il demone e divenne quasi immortale. Portò distruzione e caos, ma si dice che il contraccolpo di tutte le leggi del mondo che aveva infranto le arrivò addosso in un colpo solo, e la annientò.",

    # ---------------------------------------------------------- :485 la vacca marina rediviva
    (485, "Ancient sea beast with a kind heart. Because of their nature, they cannot abandon their friends in danger and escape, so they all gather together to help and everyone gets trap. That's why they became extinct."):
        "Una bestia marina antica dal cuore gentile. Per come è fatta non sa abbandonare un compagno in difficoltà e scappare: si radunano tutte per aiutarlo e finiscono tutte in trappola. Ecco perché si è estinta.",

    # ---------------------------------------------------------- :498 l'ibis nipponico redivivo
    (498, 'Ancient bird that was endangered for a long time. Somehow they managed to survive the nuclear war of the time, but their bodies, weakened by over exposure to the ashes of death, were unable to survive the turbulent times that followed.'):
        "Un uccello antico che per moltissimo tempo si temette di perdere. Alla guerra nucleare di allora sopravvisse a fatica, ma con un corpo indebolito da troppa cenere di morte non riuscì a superare i tempi sconvolti che vennero dopo.",

    # ---------------------------------------------------------- :511 il piccione migratore redivivo
    (511, 'Ancient birds that like to travel in large numbers. It is believed that there were once billions of them, but they were hunted down when humans discovered how tasty they were.'):
        "Un uccello antico a cui piaceva viaggiare in gran compagnia. Si dice che un tempo fossero miliardi, ma gli uomini scoprirono che erano buoni da mangiare e li cacciarono fino all'ultimo.",

    # ---------------------------------------------------------- :524 l'alca impenne rediviva
    (524, 'Ancient bird that swims instead of flying. Unwary and friendly. This species was the original penguin race, but it was destroyed by a plot by another species of bird, depriving them of the name penguin as well.'):
        "Un uccello antico che non vola e nuota. Poco diffidente e affettuoso. Questa specie era il vero pinguino, ma un'altra specie di uccelli la rovinò con un intrigo e le portò via perfino il nome di pinguino.",

    # ---------------------------------------------------------- :537 il dodo redivivo
    (537, 'Ancient flightless bird. They lived peacefully on an island with no natural enemies for a long time. As a natural consequence, it had no means of resisting foreign enemies, and was overrun without resistance by the vicious humans who came to the island, leading to its extinction.'):
        "Un uccello antico incapace di volare. Visse a lungo in pace su un'isola senza predatori. Per naturale conseguenza non aveva alcun modo di opporsi a un nemico venuto da fuori, e quando sull'isola arrivarono uomini malvagi si lasciò travolgere senza resistere, fino a sparire.",

    # ---------------------------------------------------------- :550 lo spirito della lancia di bambù
    # ⓘ 門松 e' l'addobbo di capodanno con bambu' e pino che si mette ai lati
    #    della porta: qui e' un lavoretto stagionale, e la battuta e' quella.
    (550, 'Bamboo that has been spiritualized over a long period of time. At the time of spiritualization, it has somehow increased to a trio, known as the Bamboo Trio. They leave the village where they have lived since the age of bamboo, and find a hole dug by humans to live in. They usually have poison or filth smeared on the tips, however they are clean and tidy when they work part-time on the kadomatsu in January.'):
        "Un bambù che con gli anni si è fatto spirito. Nel farsi spirito, chissà come, si è moltiplicato per tre: lo chiamano anche il Trio di Bambù. Lascia il villaggio in cui viveva fin da germoglio e cerca una buca scavata dagli uomini per andarci ad abitare. Di solito tiene la punta spalmata di veleno o di sozzura, ma a gennaio, quando fa la stagione come addobbo di capodanno, si presenta pulito.",

    # ---------------------------------------------------------- :563 la ragazza mina anticarro
    # ⚠️ Le tre ragazze mina condividono le prime due frasi in giapponese e
    #    cambiano la terza: la resa fa lo stesso, se no la rete 4 direbbe il vero.
    # ⚠️ E niente seconda persona: 一緒に死のうとしてくる parla di chi le sta
    #    vicino, non del giocatore.
    (563, 'Mentally ill girl who lives in a minefield just for the appeal of \\"poor me\\". They are troublesome because they can easily let their emotions go out and try to die together with you. Even though it is an anti-tank, it does not mean that people can treat it with care.'):
        "Una ragazza dall'umore instabile che vive in un campo minato solo per far vedere quanto sia da compatire. Fa esplodere le emozioni per un nulla e cerca di morire insieme a chi le sta accanto: è una bella grana. Anticarro non vuol dire che una persona possa trattarla con leggerezza.",

    # ---------------------------------------------------------- :576 la ragazza mina a rimbalzo
    (576, 'Mentally ill girl who lives in a minefield just for the appeal of \\"poor me\\". They are troublesome because they can easily let their emotions go out and try to die together with you. They are usually quiet, but when they are caught off guard, they will suddenly jump on you and harm you, making them dangerous.'):
        "Una ragazza dall'umore instabile che vive in un campo minato solo per far vedere quanto sia da compatire. Fa esplodere le emozioni per un nulla e cerca di morire insieme a chi le sta accanto: è una bella grana. Di solito se ne sta buona, ma appena l'altro abbassa la guardia salta su all'improvviso e colpisce: pericolosa.",

    # ---------------------------------------------------------- :589 la ragazza mina direzionale
    (589, 'Mentally ill girl who lives in a minefield just for the appeal of \\"poor me\\". They are troublesome because they can easily let their emotions go out and try to die together with you. They use visible land mines normally, but it is difficult to avoid them because they spray bullets at you in a fan-like pattern.'):
        "Una ragazza dall'umore instabile che vive in un campo minato solo per far vedere quanto sia da compatire. Fa esplodere le emozioni per un nulla e cerca di morire insieme a chi le sta accanto: è una bella grana. È una mina che si vede, ma spara una rosa di pallettoni a ventaglio, e schivarla è difficile.",
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

# ⚠️ Le due righe spente col `;` di `db_card.hsp:11405` e `:11412` non stanno in
# questa zona: si rinviano nel lotto che le incontra.
RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-001.jsonl'
DA, A = 0, 600
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_card.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_102-dacard.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]
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
