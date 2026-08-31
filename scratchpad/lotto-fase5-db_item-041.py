# -*- coding: utf-8 -*-
"""116a - Lotto 041 di `db_item.hsp`: LE ARMI, il primo lotto della categoria.

`FILTER_WEAPON`, righe da `:43558` a `:66910`: **41 righe** su 39 oggetti — 39
dell'indice 0, nessuna dell'indice 1 e 2 dell'indice 2. La categoria e' la piu'
grossa fra quelle intatte, **110 su 110**, e come gli scarti non ha
moltiplicatore: «da fare» e «vive» coincidono, quindi `applica` deve salire di
**41 esatte**.

⚠️ L'intervallo si e' scelto in due tentativi, come vuole la 115a: `0 200000`
ha detto 110 righe da `:43558` a `:131182` (la categoria intera), e `0 67000`
ne ha dato 41. Le armi **non sono distribuite in modo uniforme**: fra `:43558`
e `:51779` c'e' un vuoto di ottomila righe, e poi trentotto righe stanno
addensate in quindicimila.

### ⭐⭐⭐ IL TITOLO-FONTE DICEVA UN TERZO NOME, E IL GLOSSARIO SI SMENTIVA DA SOLO

`:53420` porta la coda ～ソックスソードマンの評価～, che la tabella della 112a
rendeva `~Il Giudizio del Sockswordman~`. Ma ソックスソードマン e' gia' a
schermo, in `chat.hsp:12731`, come **«lo Spadaccino dei Calzini»**: e' il nome
da eroe che Kuroya si da' quando passa alle maniere forti.

⚠️⚠️ Le due forme stavano **nello stesso file**: `glossario.md:482` diceva
«lo Spadaccino dei Calzini» e `glossario.md:2221` diceva «Sockswordman». Un
documento che si contraddice da solo a millesettecento righe di distanza.

**Come si e' trovato:** non da una rete. `_113-fonti-gia-rese.py` cerca il
titolo **intero** e questo giapponese intero non e' reso altrove, quindi dice 0
su 41 con serenita'. L'ha trovato la ricerca a mano nel glossario, che la 111a
ha reso uno strumento (`lotti-111/_cerca.py`): e' la regola «le reti del lotto
non leggono il glossario», applicata e ripagata.

⭐ **La famiglia e' di una riga sola**, e si e' misurato prima di toccare:
ソックスソードマン compare **1 volta** in tutto `db_item.hsp`, ed e' questa. La
correzione della tabella non tocca nessuna resa gia' fatta. E' la lezione della
115a sulla tilde («la prima domanda e' quanto e' grande la famiglia»)
applicata a un difetto nostro invece che di monte.

Corretti `scratchpad/lotti-112/titoli_fonte.py` e `glossario.md:2221`.

### ⭐⭐ IL CANCELLO DEI TITOLI: LA PREVISIONE E' **6**, CIOE' INVARIATO

Le cinque code di questo lotto, e perche' nessuna ne aggiunge una settima:

    ~Irva Fantasy Encyclopedia~   26 righe  -> Dizionario Fantastico di Irva
                                  ⓘ e' gia' uno dei sei: l'altro giapponese,
                                    ～イムウエル幻想辞典～, va in «Aimwell».
                                    Qui il giapponese e' sempre ～イルヴァ～
    ~Collection of Armaments...~  12 righe  -> Raccolta di Armi e Armature...
    ~Book of Wisdom~               1 riga   -> Il Libro della Sapienza
    ~words of <Loyter>...~         1 riga   -> Parole di <Loyter>...
    ~words of a sockswordman~      1 riga   -> Il Giudizio dello Spadaccino...

Nessuno di questi inglesi copre due giapponesi diversi (controllato nella
tabella del glossario, righe 2116-2221), quindi **il cancello resta a 6**.
⭐ Il numero e' scritto qui **prima** del montaggio, come vuole la 115a: una
previsione, non una scusa.

### ⭐⭐ L'INGLESE LASCIA CADERE TRE FRASI INTERE

Non appiattimenti: frasi che nel giapponese ci sono e nell'inglese no.

  - `:53206` (<Engoku>): 見た目によらずかなりのハイテク武装で —
    «a dispetto dell'aspetto e' un'arma di alta tecnologia». L'inglese scrive
    «Pewter staff discovered in the ruins.» e salta diritto alla lama;
  - `:54316` (falce d'ossa): 一般的に見かけよりも軽く、鋭い —
    «di solito e' piu' leggera e piu' affilata di quel che sembra». L'inglese
    attacca con «However», che senza la frase prima non regge;
  - `:65879` (<Ivy Spine>): 下手に触れると死にたくなるような痛みと激しい吐き気
    に襲われる — il dolore da farsi venir voglia di morire e la nausea violenta.

⚠️ **Nessun cancello le vede**: l'inglese e' coerente con se' stesso e la resa
nostra e' piu' lunga, che non e' un difetto. Le vede solo chi legge il
giapponese accanto.

### ⭐ E DUE VOLTE L'INGLESE APPIATTISCE

  - `:52717` (<ANNINDOFU TIPO SPADA LASER>): il giapponese scrive **tre volte**
    杏仁豆腐 — l'oggetto e' budino di mandorle, l'elsa e' budino di mandorle, la
    lama e' budino di mandorle — ed e' tutta la battuta. L'inglese ne perde uno
    e scrive «Tofu attached to an Annin», che sono due cose diverse;
  - `:52996` (<Gouten>): 水中潜航や飛行 sono **due** capacita', immergersi e
    volare. L'inglese le fonde in «dive and fly underwater», che ne dice una
    sola e sbagliata.

### ⚠️ E UNA VOLTA CAMBIA LA RISORSA, COME I GLOBI OSCURI DEL 034

`:52857` (<Go-Renge>): il giapponese dice ＳＰ, l'inglese scrive «stamina». Si
segue il giapponese e si scrive **SP**, che e' la forma che il dizionario usa
gia' (`chat.hsp`, il consiglio sul recupero).

### ⭐ IL NOME DEL SOLDATO NON E' IL NOME DELLA SPADA

`:63723` (<The White Hawk>): l'oggetto e' **invariato**, perche' il giapponese
lo scrive in katakana (ウィーテハウク). Ma il soprannome del soldato di Zanan,
tre frasi dopo, e' 「白き鷹」 — giapponese vero, non katakana — e allora si
rende: **«il Falco Bianco»**.

ⓘ Il giapponese fa la stessa distinzione che facciamo noi: nome dell'oggetto
traslitterato, soprannome della persona in lingua. Non e' una scelta nostra, e'
la struttura della riga.

### ⚠️ LA RIGA DI GIOCO: <Necromantis> E QUATTRO TERMINI DEL DIZIONARIO

`:60786` e' l'unica riga del lotto che descrive un **effetto vero**, e i suoi
quattro termini si sono cercati invece di inventarli:

    パワーゲージ    -> la barra di potenza    (`chat.hsp`, il consiglio sulle gemme)
    使役           -> soggiogare             («Se ne puo' soggiogare uno solo»)
    棺             -> la bara                («Rimetti nella bara»)
    アンデッド      -> i non morti

⚠️ 融合アンデッド nel dizionario **non c'e'**. Si e' scritto «un non morto di
fusione», sulla forma dell'abilita' *Fusione dei morti* (`*死者融合*`), che e'
il nome che il giocatore vede per la stessa meccanica.

### ⚠️ TRE ECCEZIONI DI SPAZIATURA, TUTTE DICHIARATE PRIMA DEL MONTAGGIO

    :43558   la coda e' `#~` SENZA spazio; le altre venticinque di Irva l'hanno
    :63723   il corpo NON ha lo spazio prima del `\\n`
    :65265   idem

ⓘ Non si vedono leggendo il dossier: le da' `_scheda034.py 041` col `repr()`,
ed e' l'unica ragione per cui quello strumento esiste.

### ⓘ Il preflight ha detto una cosa sola, e aveva ragione

«dell'indipendenza», 17 caratteri, oltre la finestra di rinculo di 15. Riscritto
in «il simbolo di libertà e indipendenza» (12). Non si e' discusso se la parola
fosse lontana dal confine: costava una parola cambiarla.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :43558
    (43558, 'Spears made in the shape of a bone. Not made of bone. It can be chewed to relieve stress or eaten as a snack. As a weapon, it is used like a battle axe. \\n#~Irva Fantasy Encyclopedia~'):
        "Una picca fatta a somiglianza di un osso. Di osso, però, non è. A morderla e rimorderla si scarica lo stress, e volendo si mangia come merenda. Come arma, si usa nel modo dell'ascia da battaglia. \\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :51779
    (51779, 'A black sword, surrounded with an aura of dread, was created from the idea of using an even more powerful evil to exorcise evil. There are multiple alter egos of this sword across the world, each with slightly different appearances and abilities. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una spada nera, nata dall'idea di usare un male ancora più grande per scacciare il male. Ne esistono più d'una, oltre i confini del mondo, che si potrebbero dire suoi sdoppiamenti: ognuna ha forma e poteri appena diversi. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :51849
    (51849, 'Legendary bamboo spear symbolizing freedom and independence. It is said to slay a ninja with a single thrust, but also to shoot down bombers and killing Gods. \\n# ~Irva Fantasy Encyclopedia~'):
        "La leggendaria lancia di bambù che è il simbolo di libertà e indipendenza. Dicono che, in mano a chi la merita, non solo uccide un ninja con un colpo solo, ma abbatte perfino i bombardieri e riesce ad ammazzare anche un dio. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :51917
    (51917, 'Kalpa hands. Kalpa is the time it takes for a world to come into being and cease to exist. An enormous flow of time runs through the surface of the blade. If wielded with divine power, it can cut through time and space, and is also used as a means of transportation. \\n# ~Book of Wisdom~'):
        "La Mano del Kalpa. Il kalpa è il tempo che passa dalla nascita di un mondo alla sua fine. Sulla superficie della lama scorre un flusso di tempo smisurato. Chi la impugna caricandola di forza divina può squarciare lo spazio e il tempo, e c'è chi se ne serve anche per spostarsi. \\n# ~Il Libro della Sapienza~",

    # ---------------------------------------------------------- :52717
    (52717, 'A long, thin, luminescent, penetrating Tofu attached to an Annin shaped like a handle. The sharpness is somewhat inferior to that of a lightsaber. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un budino di mandorle: a un budino di mandorle a forma d'elsa ne è attaccato un altro, lungo, sottile, luminoso e capace di trapassare. Taglia un po' meno di una spada laser. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :52787
    (52787, "A giant third hand created by the crab to resemble its own scissors. It is composed of the shells and pseudo-muscles of its prey, and seems to be moved through a neural connection. It looks like a crab's scissors, but it is not the crab's scissors. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una terza mano gigantesca che il granchio si è fatta a somiglianza della propria chela. È composta dai gusci delle creature che ha divorato e da muscoli finti, e pare che la muova con un innesto nervoso. Una cosa che sembra una chela di granchio e non è una chela di granchio. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :52857
    (52857, 'This is a special kind of throwing blade that has been handed down from one school of ninja to another. It is said that to obtain it, one must go through an ordeal in the mountains during a blizzard. It is easy to hit as it is thrown in batches, but it is bulky and heavy. It has the power to drain stamina of the person it hits. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un kunai da lancio particolare, tramandato da una scuola di ninja. Pare che per averlo bisogni superare una prova in mezzo alla bufera, sulle montagne. Si lanciano tutti insieme e per questo colpiscono facile, ma sono ingombranti e pesanti. Hanno il potere di togliere SP a chi colpiscono. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :52927
    (52927, 'This thin sword is said to have fallen from the heavens with a bolt of lightning one stormy day. It is characterized by its ability to finely manipulate the electricity it generates. It is possible to store electricity in the blade and release electric blasts, and even to forcefully increase the reaction speed by channeling the electricity to its user, although it places a heavy burden on the user. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un fioretto che, dicono, un giorno di tempesta cadde dal cielo insieme a un fulmine. Quel che lo distingue è che sa comandare nel minimo l'elettricità che produce. Può accumularla nella lama e scagliare scariche, e può perfino farla passare in chi lo impugna per spingergli a forza i riflessi, anche se il prezzo da pagare è alto. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :52996
    (52996, 'A versatile drill for breaking through all kinds of obstacles in the air, land, and sea. It easily crushes hard bedrock and ice blocks, and can also dive and fly underwater. It is also equipped with a cryogenic cannon. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un trapano buono a tutto, fatto per sfondare ogni ostacolo e andare avanti in cielo, in terra e in mare. Sbriciola senza fatica la roccia dura e i blocchi di ghiaccio, e sa immergersi sott'acqua e volare. E poi, già che c'era, monta pure un cannone congelante. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :53067
    (53067, 'An oddly shaped throwing axe, far from a typical tomahawk. It is equipped with a nanomachine trajectory control system. Because it spins on its own axis, it does not lose momentum when it hits its target. Conversely, when it returns to the hand, the rotation is slowed down to make it easier to catch. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un tomahawk deforme, lontanissimo dal tomahawk comune. Monta un sistema di controllo della traiettoria a nanomacchine. Gira su sé stesso, e per questo non perde slancio nemmeno quando prende il bersaglio. Al contrario, mentre torna in mano rallenta la rotazione perché sia facile riprenderlo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :53137
    (53137, 'Sickle said to have been made by a bird-man craftsman and is intended for use in aerial combat. It has two blades resembling an elongated beak. Since it is double-edged, it can cut by pressing down without pulling, and it can also shear objects by pinching them. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una falce che si dice fatta da un artigiano uomo uccello, pensata anche per il combattimento in volo. Ha due lame che paiono un becco lungo e sottile. Essendo a doppio taglio, taglia anche premendo senza tirare, e può stringere il bersaglio in mezzo e reciderlo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :53206
    (53206, 'Pewter staff discovered in the ruins. The heated nanomachine blade boasts tremendous sharpness. The sound that the ring makes is also designed so that it can be handled without relying on the sense of sight. \\n# ~Irva Fantasy Encyclopedia~'):
        "Uno shakujo con la lama nascosta dentro, ritrovato fra le rovine. A dispetto dell'aspetto è un'arma di alta tecnologia, e la lama di nanomacchine arroventate vanta un taglio spaventoso. Perché si possa usare senza l'aiuto della vista, anche il suono degli anelli è studiato apposta. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :53278
    (53278, 'Originally, they were three staves, each with a different blessing. After the deaths of the three wielders, they were processed by a mutual disciple into a single jointed stick. Various abilities are enhanced, but they may or may not mesh. \\n# ~Irva Fantasy Encyclopedia~'):
        "In origine erano tre bastoni, ciascuno con una benedizione diversa. Morti i tre guerrieri che li portavano, un discepolo che avevano in comune li lavorò e ne fece un nunchaku solo. Rafforza parecchie doti; poi, se fra loro si incastrino davvero, è un altro discorso. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :53418
    (53418, "Highly regarded by enthusiasts, the odor is not removed even after washing, it's as smelly as a pair of socks that hasn't been washed for half a year. The wearer discards it when he or she notices the unusual odor, but in the name of protection it is recovered and found on the back market. \\n# ~Irva Fantasy Encyclopedia~"):
        "Fra gli appassionati sono valutati altissimo: l'odore non se ne va nemmeno lavandoli, e di base valgono quanto un paio tenuto addosso sei mesi. Chi li porta li butta appena si accorge del fetore, ma qualcuno li recupera con la scusa di metterli al sicuro, e finiscono al mercato nero. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :53420
    (53420, '\\"This is more than just a smelly thing. I can easily feel the daily effort from the sweat soaked to the point of being sweltering. I have to work hard too.\\" \\n# ~words of a sockswordman~'):
        "\\\"Questo non è solo un oggetto che puzza. Da tutto quel sudore, entrato dentro fino a far tossire, si sente subito la fatica di ogni giorno. ...Devo darci dentro anch'io.\\\" \\n# ~Il Giudizio dello Spadaccino dei Calzini~",

    # ---------------------------------------------------------- :53840
    (53840, 'Survival knives from the world of the ninja. It seems to have been valued since ancient times as a multi-purpose tool that is safe to have one with you. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un coltello da sopravvivenza che viene dal mondo dei ninja. Pare che fin dall'antichità sia stato tenuto caro come attrezzo buono a tutto: portarne uno con sé mette tranquilli. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :53908
    (53908, 'A thin sword derived from the rapier. It is lightweight and can be handled even by the weak. Although it is thin and unreliable, it can kill by accurately aiming at gaps in armor. When force is applied to the tip of the sword, electricity flows. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una spada sottile che deriva dalla rapiera. È alleggerita, così la maneggia anche chi ha poca forza. Sottile e all'apparenza fragile, uccide lo stesso se si mira preciso alle fessure dell'armatura. Quando la punta preme, ci passa dentro l'elettricità. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :53975
    (53975, 'A rotating conical spiral-shaped machine. When the tip is pierced, the blades in the groove section cut and shred the object. Ancient writings are scattered with descriptions of tanks and battleships using it to burrow into the ground. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una macchina a spirale, a forma di cono, che gira. Conficcata la punta, le lame dentro le scanalature tritano e sbriciolano quel che trovano. Negli scritti antichi si incontra qua e là la descrizione di carri armati e navi da guerra che se ne servivano per infilarsi sottoterra. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :54042
    (54042, "Spears are designed to be thrust by the horse's thrusting power. Because it is designed for charging, it is heavy and sturdy, and is not suitable for melee fighting. If you want to use it while dismounting from a horse, you must use your arm strength to overcome its weight and poor maneuverability. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Una lancia disegnata per infilzare lasciando fare allo slancio del cavallo. Essendo da carica è fatta pesante e robusta, e nella mischia non va bene. Se la vuoi usare a piedi, il peso e la scomodità te li devi risolvere con la forza delle braccia. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :54112
    (54112, 'A hand-held axe. The center of gravity and the shape of the handle have been adjusted so that it sticks well when thrown. However, it should be remembered that the main usage is to slash while holding it. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'ascia maneggevole. Il baricentro e la forma del manico sono regolati perché, tirandola, si pianti bene. Non bisogna però dimenticare che l'uso principale resta tenerla in mano e colpire. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :54180
    (54180, 'Machines that rotate a chain with blades at high speed. It can be used to cut down trees. If used in battle, be careful not to be pushed back and injure yourself. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una macchina che fa girare a gran velocità una catena piena di lame. Serve ad abbattere gli alberi. Se la usi per combattere, attento a non ferirti quando ti torna indietro di rimbalzo. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :54248
    (54248, 'A scythe shaped like a pair of scissors. It is heavy, but its sub-blades strike in slightly different trajectories, making it difficult for opponents to avoid it. Since it is double-edged, it can also cut through with a thrust, unlike ordinary scythes. Some scythes have a mechanism that closes and cuts like a pair of scissors. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una falce a forma di forbice. Pesa, ma la lama secondaria arriva su una traiettoria appena diversa e per il nemico schivarla è difficile. Essendo a doppio taglio, a differenza della falce comune ferisce anche di punta. E ce n'è qualcuna che ha davvero il meccanismo per chiudersi e tranciare, come una forbice. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :54316
    (54316, 'A sickle made by grafting together bones. However, it is not as strong as it should be, and if not maintained properly, the sharpness of the blade will deteriorate rapidly. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una falce fatta di ossa messe insieme. Di solito è più leggera e più affilata di quel che sembra. Regge però poco, e se non la si tiene in ordine il taglio se ne va in fretta. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :54384
    (54384, 'A striking weapon for combat, derived from a tool. A hammer head is joined at right angles to the tip of the tool, which is struck to create an impact. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'arma d'urto da combattimento che deriva da un attrezzo da lavoro. In cima ha una testa di martello innestata ad angolo retto: è quella che si batte per dare il colpo. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :54453
    (54453, 'It is a type of mace, but the handle is chained to a star-shaped iron ball with spikes. The reach is increased and the power is improved by centrifugal force. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "È un tipo di mazza, ma la palla di ferro a stella, irta di punte, è legata al manico da una catena. Arriva più lontano, e la forza centrifuga ne aumenta anche la potenza. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :54521
    (54521, 'A walking stick used in some sects. It has a large loop at the tip through which multiple rings are threaded, and it makes a sound when waved. This sound is believed to have a beneficial effect in repelling evil spirits and eliminating troubles. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un bastone che usano certe scuole religiose. Nell'anello grande in cima ne sono infilati altri, e a scuoterlo suona. Si crede che quel suono abbia effetti benedetti: tiene lontano il male e leva i desideri che tormentano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :54591
    (54591, 'A staff with two or more sections. Each is connected to the other by a chain and can be split. It takes a good deal of practice to swing it around without hitting yourself while it is split. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un bastone fatto di due o più sezioni. Sono legate fra loro da catene e si possono separare. Per girarlo da separato senza prendersi in faccia ci vuole la sua pratica. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :56808
    (56808, 'A natural weapon created by a dinosaur. It is said to have been made overly heavy to increase its power, which hindered its daily life. Connected by graviton-coated muscle fibers and bones, it does not break even when swung with all your might. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'arma naturale che un dinosauro si è fatta da sé. Pare che, per aumentarne la forza, l'abbia resa così pesante da rendersi difficile la vita di ogni giorno. È attaccata al corpo da fibre muscolari rivestite di gravitoni e da ossa, e per quanto la si giri con tutta la forza non si stacca. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :60195
    (60195, 'A lightweight battle axe for its size. It has been adjusted so that it can be wielded with one hand. In addition to being equipped with magical auxiliary mechanisms in each part, the blade dissipates the surrounding air to create a vacuum state, ignoring air resistance. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'ascia da battaglia leggera per quanto è grande. È regolata in modo da poterla girare anche con una mano sola. Oltre ad avere in ogni sua parte dei meccanismi che aiutano la magia, la lama disperde l'aria intorno e si fa il vuoto, così l'attrito dell'aria non la tocca. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :60786
    (60786, 'Seemingly created by some god, it somehow found its way into the human world and was used as a toy for necromancers and the powers that be. By reducing the power gauge by 25%, it sends a predetermined combination of serving undead within view to the coffin and fusion summon a powerful undead. You can only control one fusion undead of the same type, at the same time. The fusion undead summoned by this effect will not become a coffin, and will self-destruct if the user leaves the map. \\n# ~Irva Fantasy Encyclopedia~'):
        "Pare l'abbia fatta un dio di chissà dove, ma a un certo punto è finita nel mondo degli uomini ed è diventata il giocattolo di negromanti e potenti. Calando del 25% la barra di potenza, rimanda nella bara una combinazione stabilita di non morti al tuo servizio che hai in vista, e chiama un non morto di fusione. Dello stesso tipo, però, non se ne può soggiogare più d'uno per volta. Il non morto di fusione chiamato così non diventa bara, e si distrugge da sé quando chi l'ha evocato lascia la mappa. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :61248
    (61248, 'War hammer modified to resemble a walking cane in appearance. It is heavy and strong enough to crush a skull. It blows off the head of an unwary opponent from the neck. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un martello da guerra rifatto perché sembri un bastone da passeggio. Ha peso e robustezza che bastano a sfondare un cranio. A chi si distrae, la testa gliela stacca di netto. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :61793
    (61793, 'Pink chain sickle. The blade is round, the weight is low, and the power itself appears to be of little importance. In reality, it is a ninja tool that manipulates energy vortexes, and it is dangerous to be careless with its appearance. Normally, the scythe is hidden and hung as a fashionable chain. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una falce a catena rosa. La lama è tonda, il contrappeso è piccolo, e a vederla non pare capace di gran che. In realtà è un arnese da ninja che comanda vortici di energia, e fidarsi dell'aspetto è pericoloso. Di solito la parte della falce sta nascosta e il resto pende come una catenina alla moda. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :63454
    (63454, "The staff converts the user's MP into attack power, depending on the amount of MP, it can be said to be the most powerful weapon in the world. However, it requires a good judgment to use it well, because the more you attack, the more it is depleted. Also, if your MP is low, it is just a sturdy stick. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un bastone che converte in forza d'attacco gli MP di chi lo usa. Con abbastanza MP tira fuori una potenza tale che chiamarlo l'arma più forte non sarebbe esagerato. Ma ogni colpo li consuma, e per servirsene bene ci vuole fiuto. E con pochi MP diventa un bastone e basta, robusto e nient'altro. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :63723
    (63723, 'Longsword with a hawk motif. No matter what it slashes, it does not catch any blood and keeps its morbid whiteness. Many people find its appearance eerie. The Zanan soldier who found this sword in the ruins became famous as the \\"White Hawk\\" over the course of his battles.\\n# ~Irva Fantasy Encyclopedia~'):
        "Una spada lunga disegnata con la figura di un falco. Qualunque cosa tagli, non le si attacca addosso una goccia di sangue, e resta bianca fino a parere malata. In molti trovano la cosa inquietante. Il soldato di Zanan che trovò questa spada fra le rovine, di battaglia in battaglia, diventò famoso come \\\"il Falco Bianco\\\".\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :63725
    (63725, '\\"The sharpness seems perfect... a little too clean for me.\\" \\n# ~words of <Loyter> the crimson of Zanan~'):
        "\\\"Il taglio pare non abbia nulla da ridire... ma per me è un po' troppo pulita.\\\" \\n# ~Parole di <Loyter> l'eroe cremisi di Zanan~",

# 2 voci, 0 ambigue

    # ---------------------------------------------------------- :64485
    (64485, 'It has a name that means ace of spades. It is said to be a refurbished version of a shovel that was once stuck in the battlefield. It can be used like a spear by slashing and poking, and by utilizing its wide blade, made of bulletproof steel, as a shield. In addition to combat, it is also used for digging holes and cutting branches in the way of advancing troops. The handle is extremely heavy as a result of the telescopic function and strength of the handle, making it difficult to handle. \\n# ~Irva Fantasy Encyclopedia~'):
        "Porta un nome che vuol dire asso di picche. Pare sia il rifacimento di una pala che stava piantata in un campo di battaglia. Taglia e punge come un'alabarda, e la lama larga, fatta di acciaio antiproiettile, fa anche da scudo. Fuori dal combattimento serve a scavare buche e a tagliare i rami che intralciano la marcia. Per tenere insieme il manico allungabile e la robustezza è venuta pesantissima, ed è scomoda: questo è il difetto. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :65133
    (65133, 'Blunt weapon coated with black metal and embedded with pieces of metal shaped like crushed almonds. It was originally not a weapon, but an object that had been displayed in the center of a village. According to the story, it is said to be a statue of a hero who once hid and saved a village that was about to be destroyed in a conflict. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'arma contundente rivestita di metallo nero, con incastonate schegge di metallo a forma di mandorle spezzate. Sorpresa: in origine non era un'arma, ma un ornamento che stava in mezzo a un villaggio. A quel che si dice, sarebbe la statua dell'eroe che nascose e salvò quel villaggio quando una guerra stava per cancellarlo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :65265
    (65265, 'A whip of exorcism created by a dark ritual to destroy demons. It is said that many lives, both human and demon, were spent in the ritual. It has something like a ego, and appears before those it chooses. It is said to have been passed down through time, along with the whip of the beginning and the vampire-killing whip.\\n# ~Irva Fantasy Encyclopedia~'):
        "Una frusta scacciademoni, nata da un rito oscuro per annientare i mostri malvagi. Nel rito, dicono, furono spese moltissime vite, di uomini e di demoni senza distinzione. Ha qualcosa come una volontà propria, e si mostra a chi ha scelto. Pare che, insieme alla frusta delle origini e alla frusta ammazzavampiri, passi di mano in mano ancora oggi, attraverso il tempo.\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :65879
    (65879, 'Ivy vines are cut off and used as whips. The surface is covered with cilia, each of which is a sharp, poisonous thorn. Even a graze wound will cause blood to gush from everywhere in the body if left untreated, so be careful how you handle them. At the very least, it is best not to wield it with bare hands. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un tralcio d'edera tagliato e ridotto a frusta. La superficie è tutta coperta di peluria fitta, ma ogni pelo è una spina acuminata e velenosissima: a toccarla male ti prende un dolore da farti venir voglia di morire e una nausea violenta. Anche solo un graffio, se lo si trascura, fa sprizzare sangue da tutte le mucose del corpo, quindi va maneggiata con attenzione. Come minimo, meglio non girarla a mani nude. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :66840
    (66840, 'A dagger that is said to play the tone in your mind. However, it is quite difficult to use it as a musical instrument because it requires a high level of concentration to produce a melody with no noise mixed in. As a blade, it does not have much killing power, but depending on the user, it can produce everything from hypnotic sound waves to explosive sounds at will, making it a formidable weapon. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un pugnale che, dicono, suona il timbro che ti passa per la testa. Solo che per farne una melodia senza rumore in mezzo ci vuole una gran concentrazione, e da strumento è parecchio difficile. Come lama non uccide granché, ma in certe mani sa tirare fuori di tutto, dall'onda che addormenta al boato, e allora diventa un'arma spaventosa. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :66910
    (66910, 'Greatsword that can be wielded and attacked like a whip by connecting the multi-sectioned blade with magical power extracted from the wielder. In the connected state, the blade parts are only folded over each other, and if left as they are, the blade will fall apart when slashed. Therefore, it is necessary to maintain the strength of the blade by covering it with magical power supplied by the wielder. \\n# ~Irva Fantasy Encyclopedia~'):
        "Uno spadone che, tenendo insieme con la forza magica estratta da chi lo porta una lama divisa in più segmenti, si può girare e menare come una frusta. Da unito, i pezzi della lama stanno soltanto sovrapposti l'uno all'altro, e così com'è la lama andrebbe in pezzi al primo colpo. Per questo bisogna coprirla con la forza magica che il portatore le fornisce, e tenerla salda. \\n# ~Dizionario Fantastico di Irva~",

# 39 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-041.jsonl'
RIGHE = {
    43558, 51779, 51849, 51917, 52717, 52787, 52857, 52927, 52996, 53067,
    53137, 53206, 53278, 53418, 53420, 53840, 53908, 53975, 54042, 54112,
    54180, 54248, 54316, 54384, 54453, 54521, 54591, 56808, 60195, 60786,
    61248, 61793, 63454, 63723, 63725, 64485, 65133, 65265, 65879, 66840,
    66910,
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
