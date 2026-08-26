# -*- coding: utf-8 -*-
"""103a - Lotto 7 di `db_card.hsp`: le carte fra la riga 3101 e la 3600 (38).

Vedi `scratchpad/_102-rese-card-01.py` per il meccanismo del pannello: questa
prosa non sta nella carta, sta in `description(0)` del pannello che si apre con
`x` su un cadavere, una carta o una figurina, e l'impaginazione e' il taglio a
mano di `command.hsp:16802`-`:16829`. La rete che lo misura e'
`scratchpad/_102-carta-conoscenza.py`, e va lanciata dopo il `reimporta`.

⭐ **Gia' deciso altrove:** `ロスリア` → **Lothria**, `エウダーナ` →
**Eulderna**, `ザナン` → **Zanan**, `エレア` → **Elea**, `ネフィア` →
**Nefia**, `冒険ゼミ` → **Seminario d'Avventura** (`chat.hsp:14544`),
`カオス・スピリット` → **lo spirito del caos**, `カオス・シード` → **il seme
del caos**, `サヴァントクイーン` → **la regina savant**, `マンモス` → **il
mammut**, `クイックリング` → **il quickling**, `イーク` → **lo yeek**,
`生化学文明` → **la civilta' biochimica** (`:277`, `:1603`, `:2630`).

⚠️⚠️ **`ヴァリウス` e' Barius, non Vallius.** L'inglese di `:3345` scrive
*Vallius*, ma il personaggio e' lo stesso di `chat.hsp:13927` e
`db_creature.hsp:55752`, dove l'inglese di monte dice *Lord Barius* e il
progetto ha reso **Barius**. Si tiene il nome del progetto: e' quello che il
giocatore legge quando gli parla.

⚠️⚠️ **`カブ` NON e' un cucciolo, ed e' stato corretto oggi.** `:3423` si
presenta come 「カブの仲間だが」 e la carta di `カブ` (`:13955`) lo dice senza
margini: 機械の馬, un cavallo meccanico robusto che consuma poco. E' la Honda
Super Cub, sorella minore de «la moto grossa». Il nome diceva «il cucciolo»
dalla fase dei nomi, per l'inglese `cub` preso alla lettera. Sei voci corrette
in quattro dizionari da `scratchpad/correzione-cub.py`: ora e' **il Cub**.

⚠️ **L'inglese di monte rovescia `:3124`.** 他力本願 vuol dire *che conta sugli
altri*; l'inglese scrive *self sufficient*, cioe' il contrario esatto. Si
traduce dal giapponese, come sempre.

⚠️ **E sbaglia anche `:3306`:** `アールキング` e' l'Erlkonig, e il giapponese
lo scioglie in ハンノキの王, *il re degli ontani*. L'inglese dice *King of the
ents*. Il nome della carta era gia' reso **il re degli ontani**, e la prosa lo
segue. La scena e' quella della ballata di Goethe, e non si spiega.

⚠️ **`:3579` l'inglese lo sfigura in due punti**: 記憶力と洞察力で賭博に逆転
勝利し — *ribalto' la partita al gioco d'azzardo con memoria e intuito* — che
l'inglese legge come *winning the gamble to regain her memory*; e chiude su
*he meets a man*, mentre il giapponese ha 一人の行き倒れ, *uno stramazzato per
strada*, senza genere. E' Rianna che incontra qualcuno, non un lui.

⚠️ **Niente virgolette, niente caporali, niente lineette lunghe**: nel
dizionario non c'e' un solo `"` dentro una statica e l'unico carattere sopra il
Latin-1 e' `♪`. In CP932 il resto diventa doppia larghezza.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :3111 la falena badante
    # ⚠️ 知らぬが仏 e' un proverbio: «chi non sa, e' beato». Non si spiega.
    (3111, "They were weak and unfit to live without being cared for but through breeding they became healthy enough to take care of humans. They come closer fluttering their wings as hard as they can to return the favor. Originally it was human beings who made them unable to live on their own but they don't know this."):
        "Era una creatura gracile e imbranata che senza le cure degli umani non sapeva campare, ma la selezione della specie ha rovesciato la faccenda: adesso sta così bene in salute da poter assistere lei gli umani. Per sdebitarsi ti viene incontro sbattendo le ali con tutta la forza che ha. A ridurla a un corpo che da solo non stava in piedi erano stati proprio gli umani, ma lei non lo sa, e beata lei.",

    # ---------------------------------------------------------- :3124 il bruco cecchino
    # ⚠️ 他力本願 = «che conta sugli altri». L'inglese scrive «self sufficient»,
    #    cioe' il contrario: la carta e' tutta su quanto e' scansafatiche.
    (3124, 'A self sufficient caterpillar. He stayed prone almost motionless to avoid being targeted and waits for someone to take down the enemy. When the enemy approaches it fights back in a flurry. The other insect weapons have a poor opinion of him and he is scolded for doing his job properly.'):
        "Un bruco che campa sul lavoro degli altri. Sta disteso e quasi immobile per non farsi prendere di mira, e aspetta che sia qualcun altro ad abbattere il nemico. Se il nemico gli arriva addosso, si mette a rispondere al fuoco tutto trafelato. Anche fra le altre armi-insetto ha pessima fama, e lo sgridano perché faccia la sua parte.",

    # ---------------------------------------------------------- :3137 <Karata> la mascotte
    # ⚠️ ゼミ創始者 e' Vanessa, ed e' una donna: `chat.hsp:14918` e `:14921`.
    (3137, "His soul was caught up by a treasure chest that had been plucked clean of its contents and abandoned. He has a history of devouring people to fill his empty self and destroying two small villages. He was defeated by the founder of the seminar and was made a mascot forcibly but now he seems to be living a pretty fulfilling life."):
        "In uno scrigno a cui avevano portato via solo il contenuto, e che poi era stato abbandonato lì, germogliò una coscienza. Per riempire il proprio vuoto andò avanti a divorare gente, e ha alle spalle due piccoli villaggi rasi al suolo. Sconfitto dalla fondatrice del Seminario, fu fatto mascotte a forza, ma pare che oggi passi giornate abbastanza appagate.",

    # ---------------------------------------------------------- :3150 la recluta
    (3150, "They heard that the adventurer life is interesting so they tried it but it's complicated and confusing. they have a distracted attention span failing to notice how unwell they are skimming descriptions missing annotations and memorizing proper nouns incorrectly."):
        "Ha sentito dire che la vita dell'avventuriero è divertente e ha voluto provarci anche lui, il che va benissimo, se non fosse che è tutto complicato e lui ci si perde. Ha l'attenzione che gli va dove vuole: non si accorge di stare male, salta le spiegazioni, si lascia sfuggire le note e i nomi propri se li impara sbagliati.",

    # ---------------------------------------------------------- :3163 l'aiutante a ore del maestro Spada Rossa
    (3163, "A part-time job with a red sword. Apparently there's proper training and manuals. Compensation is commission-based. Many of those who were instructed by this teacher were surprised to learn later that they were part-time workers."):
        "Un lavoratore a ore, con la spada rossa in dotazione. Pare che ci siano davvero un periodo di addestramento e un manuale. Il compenso è a provvigione. Fra quelli che hanno ricevuto la lezione da questo maestro, in molti restano di sasso quando poi scoprono che era un ragazzo a ore.",

    # ---------------------------------------------------------- :3176 <Mito> la docente
    (3176, "She used to work as a part-time teacher for Red Sword Sensei and that's when she became interested in becoming a seminar teacher. She advocates calling each other by nicknames with other instructors and they are quite familiar with each other. She is secretly concerned about a fellow lecturer Ajetalio."):
        "Un tempo ha fatto l'aiutante a ore del maestro Spada Rossa, e da lì le è venuta la voglia di insegnare al Seminario. È stata lei a proporre che i docenti si chiamassero per soprannome, e la cosa ha attecchito parecchio. Di nascosto le interessa Ajetalio, che insegna lì come lei.",

    # ---------------------------------------------------------- :3189 <Iduru> il docente
    # ⚠️ L'inglese scivola in prima persona («and I became a seminar
    #    instructor»): il giapponese parla di lui per tutta la carta.
    (3189, "Even while on active duty he was concerned about the declining quality of warriors. When his daughter became a full-fledged member of the family he let her take over his family's dojo and I became a seminar instructor to teach her from a fundamental point of view."):
        "Già ai tempi in cui era in attività si rammaricava di come calasse la qualità dei guerrieri. Quando la figlia si è fatta adulta le ha lasciato il dojo di famiglia, e lui si è messo a insegnare al Seminario per prendere la faccenda dalle fondamenta.",

    # ---------------------------------------------------------- :3202 <Cresce> la docente
    (3202, "He used to work as a communications officer for the Zanan Army but decided it wasn't the right fit for him so he became a seminar instructor. He is an item enthusiast and is rumored to have a variety of collections at home. What was meant to be just a walk often turned into a collection of items."):
        "Prima si occupava di comunicazione nell'esercito di Zanan, poi ha deciso che non faceva per lei ed è passata a insegnare al Seminario. È una maniaca di oggetti, e si dice che in casa abbia collezioni d'ogni genere. Capita spesso che quella che doveva essere una passeggiata e basta finisca in una raccolta di oggetti.",

    # ---------------------------------------------------------- :3215 <Ajetalio> il docente
    (3215, "He is a former graduate of the Adventure Seminar so to speak. He has a distrust of a fellow lecturer Mito and every day he is torn between fear and fear that he will be duped and stripped to the ground at any moment. He likes the nicknames he's been given."):
        "A suo tempo il Seminario d'Avventura lo ha avuto come allievo: insomma, è un ex diplomato. Non si fida di Mito, che insegna lì come lui, e passa le giornate col batticuore, aspettandosi da un momento all'altro di essere raggirato e ripulito di tutto. Il soprannome che gli hanno messo, a dire il vero, gli piace.",

    # ---------------------------------------------------------- :3228 il serpente del caos
    (3228, 'The chaos spirit that had grown up merged into a half-beast half-snake demon. Serving as a production base the spheres in each part fall to the ground as they ripen producing countless chaos seeds. What they hate are unicorns.'):
        "Nasce dagli spiriti del caos che, una volta cresciuti, si fondono in un mostro metà bestia e metà serpente. Ha il compito di fare da impianto di produzione: le sfere che porta sulle varie parti del corpo, quando maturano, cadono a terra e generano semi del caos a non finire. Quello che proprio non sopporta sono gli unicorni.",

    # ---------------------------------------------------------- :3241 il seme del caos
    (3241, "The seeds of malice that an evil god scattered throughout the world on the verge of being sealed. It takes in humans with mana and grows into a humanoid. The gods are working hard to eradicate them but their numbers don't decrease easily because they have a high ability to multiply in addition to hiding."):
        "I semi di malanimo che un dio malvagio sparse per il mondo un attimo prima di essere sigillato. Si prende gli umani, mana compreso, e cresce fino alla forma umana. Gli dei si danno da fare per estirparli, ma stanno acquattati e si moltiplicano in fretta, così il loro numero non cala tanto facilmente.",

    # ---------------------------------------------------------- :3254 <Zisilion> il re sfaccendato delle miniere
    (3254, "The owner of the world's largest platinum mine. An eccentric who gets excited about the fact that something from his own mine has been processed to such an extent that it no longer resembles its original form and is now in the hands of people he doesn't know well. He keeps a large number of geese at home as a hobby."):
        "Il padrone della più grande miniera di platino del mondo. Un tipo strambo che si entusiasma all'idea che quel che esce dalla sua miniera venga lavorato fino a non somigliare più a niente, passi in mano a gente che lui non conosce e finisca in uso da qualche parte. In casa alleva per passatempo una quantità di oche.",

    # ---------------------------------------------------------- :3267 il re del legno maledetto
    (3267, 'The trees that grew on the battlefields where many died absorbing the bodies mana and souls of the dead in their entirety became powerful demons. A cursed being made into a collection of grudges.'):
        "Gli alberi cresciuti sui campi di battaglia dove i morti si contavano a mucchi hanno assorbito dei caduti il corpo, il mana e l'anima senza lasciarne niente, e a furia di assorbire sono diventati una creatura mostruosa e potentissima. Un ammasso di rancore, e un essere maledetto.",

    # ---------------------------------------------------------- :3280 l'albero drago verdecupo
    (3280, 'Having who longed for the good looks of a dragon it transformed its own body over the years. The green moss on its body surface stores magical power and it can also fly. When flying for long periods of time it holds on to soil by the roots and carries it along.'):
        "Un albero sacro che, ammirato da quanto sono belli i draghi, si è trasformato il corpo nel giro di lunghissimi anni. Nel muschio verde che ha in superficie accumula potere magico, e sa anche volare. Quando il volo si fa lungo, afferra un po' di terra con le radici e se la porta dietro.",

    # ---------------------------------------------------------- :3293 l'albero della dea irata
    (3293, 'A goddess who was transformed into a tree after a conflict but somehow managed to return to almost humanoid form after an unbearable number of years. She is no longer powerful enough to gather religious beliefs and every day she takes it out on the world while photosynthesizing.'):
        "Una dea che alla fine di una contesa fu ridotta ad albero, e che dopo un numero di anni da far girare la testa è in qualche modo tornata quasi alla forma umana. Non ha più la forza di raccogliere fede intorno a sé, e passa le giornate a prendersela col mondo mentre fa la fotosintesi.",

    # ---------------------------------------------------------- :3306 il re degli ontani
    # ⚠️ ハンノキの王 e' l'ontano, non l'ente: l'inglese scrive «King of the
    #    ents». La scena e' l'Erlkonig di Goethe, e non si spiega.
    (3306, 'King of the ents. His personality is evil itself and he misleads and guides humans to their destruction. Specifically he talks to a sick child who is being carried on a horse as a demon king and gives him a terrifying vision and shocks him to death.'):
        "Il re degli ontani. Il carattere è la malvagità in persona: confonde gli uomini e li porta alla rovina. In concreto, per dire, parla come un re dei demoni al bambino malato che stanno portando via a cavallo, gli mostra visioni da far paura e lo fa morire di spavento.",

    # ---------------------------------------------------------- :3319 il fico strangolatore
    (3319, 'It has multiple trunks that are undulating. It walks with an outstretched trunk and grows by taking in the living in its path. Also known as the tree of strangulation. It is said that the reason the trunk is undulating is because the thing that has been taken in is violently struggling until the very end.'):
        "Ha più tronchi, tutti contorti. Cammina allungando i tronchi, e cresce inghiottendo vivo quello che gli capita sul percorso. Lo chiamano anche l'albero che strangola. Si dice che i tronchi siano contorti perché quel che ha inghiottito si dibatte fino all'ultimo.",

    # ---------------------------------------------------------- :3332 la skogsra
    (3332, "A tree mimicking a human. Don't be misguided by her long hair she is not disfigured but her back is completely wooden. If there's a self-proclaimed forest girl whose back is unusually rough and branches are protruding from her back when she hugs you she' s usually this thing."):
        "Un albero-spettro che si finge donna. Si copre con i capelli lunghi, ma la trasformazione non le è riuscita fino in fondo e la schiena è rimasta tutta di legno. Se abbracciandola le senti la schiena ruvida in modo sospetto, o se ti capita una sedicente ragazza dei boschi a cui spuntano rami dalla schiena, quella nove volte su dieci è lei.",

    # ---------------------------------------------------------- :3345 <Alfred> il vento azzurro di Lothria
    # ⚠️ ヴァリウス: l'inglese qui scrive «Vallius», ma il progetto lo rende
    #    **Barius** (`chat.hsp:13927`, `db_creature.hsp:55752`, `:56299`).
    (3345, "After losing his wife in the war he fled his hometown in search of a way to end the conflict. While wandering around the country with his daughter he met Vallius and sympathized with his ideas. I'm a little glad I'm walking with my daughter and being mistaken for a brother."):
        "Perse la moglie travolto dalla guerra, e per questo lasciò il paese natale in cerca di un modo per sradicarla. Mentre girava di terra in terra con la figlia incontrò Barius, e ne condivise il pensiero. Quando cammina con la figlia e li scambiano per fratello e sorella, un po' gli fa piacere.",

    # ---------------------------------------------------------- :3358 il Konigskatze
    (3358, 'A tank used in the final war of a mechanical civilization. It was so agile that it reminded me of a cat and it made fighters and humanoid weapons tremble. Its successor aimed to be even more mobile but was purposely named Mammoth in order to fool the enemy.'):
        "Un carro armato usato nella guerra finale della civiltà meccanica. Aveva una mobilità così alta da far pensare a un gatto, e faceva tremare i caccia e le armi dalla forma umana. Il modello che venne dopo puntava a una mobilità ancora più spinta, ma lo chiamarono apposta Mammut per far credere al nemico il contrario.",

    # ---------------------------------------------------------- :3371 lo zoibo
    (3371, "Initially built as a pet robot it was eventually enlarged to be used as a fighter beast. Rooted in machine dogs imported from other planets and a hybrid of machine dogs from this planet. It's hard to get the best performance out of it because it moves so violently."):
        "All'inizio fu costruito come robot da compagnia, poi lo ingrandirono e lo impiegarono come bestia da combattimento. Alla radice c'è l'incrocio fra i cani meccanici importati da altri pianeti e quelli di questo. Si muove in modo scomposto, e tirargli fuori tutto quello che sa fare è un'impresa.",

    # ---------------------------------------------------------- :3384 la ruspa colossale Buildion
    (3384, 'An ancient monster machine with superior power speed and technique it acts autonomously to destroy and reproduce repeatedly. It is also recorded that it defeated the fighting vehicles of the time head-on. It has an environment-adaptive function and can be used even in poor conditions.'):
        "Un antico mostro-macchina che eccelle in potenza, velocità e tecnica, e che di sua iniziativa non fa che distruggere e ricostruire. Resta agli atti che sconfisse a viso aperto i veicoli da combattimento dell'epoca. Ha una funzione di adattamento all'ambiente, e anche nel peggiore dei cantieri non si scompone.",

    # ---------------------------------------------------------- :3397 il chierico da sella
    # ⚠️ 中期 e' la meta' della civilta' meccanica; l'inglese scrive «in the
    #    heights of», che e' un'altra cosa.
    (3397, 'A mass-produced walking machine in the heights of a mechanical civilization. A person can get in the head. It was used for propaganda to spread the splendor of the machine but it also boasted the sturdiness and limb strength of a military-grade aircraft.'):
        "Macchina camminante di serie, della metà della civiltà meccanica. Nella testa ci sale una persona. La usavano per la propaganda che diffondeva le meraviglie del culto della macchina, ma vanta in sordina una robustezza da mezzo militare e braccia che non scherzano.",

    # ---------------------------------------------------------- :3410 il carro automatico Xeren
    (3410, 'The main weapon used in the early days of mechanical civilization. Due to its thin armor it is lightweight and can be used for small turns and is reliable on rough roads. Apparently quite a few had been operating long after other combat weapons had been developed with updated autonomous circuits.'):
        "L'arma principale dei primi tempi della civiltà meccanica. La corazza è sottile, ma in cambio è leggero, gira stretto e se la cava anche sulle strade rotte. Pare che, anche molto dopo che le altre armi da combattimento si erano evolute, parecchi esemplari abbiano aggiornato i circuiti autonomi e siano rimasti in servizio a lungo.",

    # ---------------------------------------------------------- :3423 la moto grossa
    # ⚠️⚠️ カブ e' **il Cub**, corretto oggi: vedi la testa di questo file e
    #     `scratchpad/correzione-cub.py`. Qui il nome compare due volte.
    (3423, "It's a member of the cubs but it's large and capable of considerable speed. It has a shorter lifespan than a cub and is grumpy and rough. It's a relative pain in the ass but if you're used to cubs and are looking for speed it's a good idea to keep one."):
        "È della famiglia del Cub, ma è grossa e sa tirare fuori una bella velocità. Rispetto al Cub ha vita più breve, ed è permalosa e ruvida. Dà il suo daffare, ma se il Cub lo conosci già e quello che cerchi è la velocità, tenerne una può valere la pena.",

    # ---------------------------------------------------------- :3436 <Halion> l'estremista
    (3436, 'For better or worse this young man is a straightforward Elean. Admiring his late father who had a strong sense of justice he was a member of the forest vigilante group. In the past when armies from various countries invaded the forest they formed an impromptu interdiction squad and steadfastly resisted until the end.'):
        "Un giovane Elea tutto d'un pezzo, nel bene e nel male. Ammirava il padre morto, che aveva un forte senso della giustizia, e stava nella ronda del bosco. Quando in passato gli eserciti di più paesi entrarono nel bosco, pare che abbia messo insieme su due piedi un reparto di disturbo e abbia continuato a resistere in sordina fino all'ultimo.",

    # ---------------------------------------------------------- :3449 il re unimorto
    (3449, 'A superlative undead weapon used by the biochemical civilization. It was thought to be extinct but it recently emerged from the ancient ruins of Eulderna accompanied by other weapons. It is said that one woman went to great lengths to destroy it until she managed to get it under control.'):
        "L'arma non morta di grado più alto in uso ai tempi della civiltà biochimica. Si credeva che non ne esistessero più, ma di recente ne è comparsa una dalle rovine antiche di Eulderna, insieme ad altre armi. Si dice che abbia distrutto tutto quello che poteva finché una donna non è riuscita a tenerla a freno.",

    # ---------------------------------------------------------- :3462 la regina unimorta
    (3462, 'An advanced undead weapon used by the biochemical civilization. Unlike the King type which emphasized simple combat power the Queen type was built with an emphasis on logistical support. Her intelligence is quite high and she rivals the Savant Queen.'):
        "Arma non morta di grado alto, in uso ai tempi della civiltà biochimica. A differenza del tipo re, tutto puntato sulla forza di combattimento pura, questa fu costruita puntando sul sostegno alle retrovie. È parecchio intelligente, e nella regina savant vede una rivale con cui misurarsi.",

    # ---------------------------------------------------------- :3475 il fante unimorto
    (3475, 'An advanced undead weapon used by the biochemical civilization. The skeleton is armed with melee weapons but it is not good at fighting because it is attached to the back of a dragon skeleton. If anything it seems to play a larger role as a control unit.'):
        "Arma non morta di grado alto, in uso ai tempi della civiltà biochimica. La parte di ossa umane porta armi da mischia, ma stando attaccata alla schiena di uno scheletro di drago nel corpo a corpo se la cava male. Semmai, pare che conti soprattutto come unità di controllo.",

    # ---------------------------------------------------------- :3488 il jolly unimorto
    (3488, 'A special undead weapon that was used during the biochemical civilization. A half-spirit body is forcibly possessed by a corpse doll. A clown who scrambles around the battlefield laughing in a creepy voice.'):
        "Arma non morta speciale, in uso ai tempi della civiltà biochimica. È un mezzo spirito costretto a impossessarsi di una bambola fatta di cadaveri. Un buffone che ride con una voce da far accapponare la pelle e mette il campo di battaglia sottosopra.",

    # ---------------------------------------------------------- :3501 l'eroyeek
    (3501, 'They are considered heroes among the yeeks having strong power and admirable courage for a yeek. He defeats a boar that has attacked his village or fights head-on with a knight who has come to test his skills.'):
        "Per essere uno yeek ha una forza notevole e un coraggio ammirevole, e fra gli yeek passa per eroe. Abbatte il cinghiale che ha assalito il villaggio, oppure affronta a viso aperto il cavaliere venuto a misurarsi con lui.",

    # ---------------------------------------------------------- :3514 il lunatiyeek
    (3514, "In an accident he gains human-level intelligence but at the cost of his mind losing his reason. That's why he was so easily enchanted by the mighty power of demons and evil gods. The other yeeks recognize him as a dangerous individual if he gets close to them."):
        "Uno yeek che per un incidente si è ritrovato un'intelligenza pari a quella umana, ma in cambio ci ha rimesso la ragione. Per questo si è lasciato incantare senza fatica dalla potenza dei demoni e degli dei malvagi. Gli altri yeek lo tengono per uno a cui è meglio non avvicinarsi.",

    # ---------------------------------------------------------- :3527 l'arcayeek maestro
    (3527, "An ancient species of yeeks. It has the ability to employ yeek tribes regardless of type. He has grand ambitions to create a nation of yeeks by yeeks for yeeks but he doesn't even think about how to go about it concretely."):
        "Specie antica degli yeek. Ha il potere di comandare la stirpe degli yeek, di qualunque tipo siano. Coltiva l'ambizione solenne di fondare uno stato degli yeek, per opera degli yeek e a vantaggio degli yeek, ma su come farlo davvero non ci ha ancora pensato.",

    # ---------------------------------------------------------- :3540 l'arcayeek fuciliere
    (3540, "An ancient species of yeek. He loves guns and often imitates a human gunman. A handgun is scavenged. They don't have the skills to make it themselves."):
        "Specie antica degli yeek. Va matto per le pistole, e spesso, tutto entusiasta, fa il verso ai pistoleri umani. La pistola l'ha trovata per terra: la tecnica per costruirsela da solo non ce l'ha.",

    # ---------------------------------------------------------- :3553 l'arcayeek
    (3553, "An ancient species of yeek. Their bodies are strong and sturdy but they are not as strong as other creatures. Perhaps because of this small highly fertile species of yeek have emerged in modern times. They don't try to flock but they have a strong sense of camaraderie."):
        "Specie antica degli yeek. Ha il corpo robusto e anche la sua forza, ma messo accanto alle altre creature resta comunque indietro. Sarà per questo che oggi hanno preso il sopravvento le specie di yeek piccole e molto prolifiche. Non è tipo da branco, ma tiene molto ai suoi.",

    # ---------------------------------------------------------- :3566 lo yeek lavoratore
    (3566, 'He used to be a terrible slob. However after risking his life to conquer one of the Nefian dungeons he had a change of heart. He has awakened to the joy of adventure and is still working as a ruins vandal today.'):
        "Un tempo era un pigrone da manuale. Poi ha conquistato una Nefia rischiando la pelle, e da lì ha cambiato registro. Si è risvegliato al piacere dell'avventura, e anche oggi è lì che lavora a saccheggiare rovine.",

    # ---------------------------------------------------------- :3579 <Rianna> la sognatrice
    # ⚠️ L'inglese sbaglia due volte: 賭博に逆転勝利 e' una partita ribaltata,
    #    non la memoria riguadagnata; e 行き倒れ non ha genere.
    (3579, "She ran away from home at an early age because she hated being tied to her parents' home. While wandering she accidentally ventured into the underworld but survived by winning the gamble to regain her memory and insight. Later while working behind the scenes in search of thrills he meets a man who has fallen."):
        "Non sopportava di stare legata alla casa di famiglia, e da piccola scappò via. Mentre girava senza meta mise per sbaglio piede nel giro losco, ma con la memoria e l'intuito ribaltò la partita al gioco d'azzardo e ne uscì viva. Poi, mentre si dava ai lavori sporchi per il gusto del rischio, si imbatté in una persona stramazzata per strada.",

    # ---------------------------------------------------------- :3592 l'infernello
    (3592, 'Also known as a quickling workman. He uses his small body to blend in with the darkness and ambush his targets. He then manipulates the string to slaughter the target with uncanny speed. His skills are superb.'):
        "Lo chiamano anche il professionista dei quickling. Sfrutta il corpo piccolo per confondersi col buio e aspetta il bersaglio all'agguato. Poi manovra i fili come vuole e lo fa a pezzi a una velocità che l'occhio non segue. Un lavoro pulito.",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-007.jsonl'
DA, A = 3101, 3600
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
