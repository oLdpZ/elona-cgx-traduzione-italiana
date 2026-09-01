# -*- coding: utf-8 -*-
"""119a - Lotto 050 di `db_item.hsp`: LE POZIONI, il CORPO, e la categoria CHIUDE.

`FILTER_ITEM_POTION`, righe da `:90769` a `:129439`: **41 righe** su 40 oggetti —
40 dell'indice 0 e **1 dell'indice 1**. Con questo lotto `FILTER_ITEM_POTION` va
a **0 da fare su 82 vive**, ed e' la **settima** categoria del corpo che si
chiude, dopo mobilio, attrezzi, cibi, scarti, armi e grimori.

⚠️⚠️ Previsione di `applica`: **+41** per 41 rese, nessuna gemella.
`_gia-reso.py 050`: 0 su 41.

### ⚠️⚠️⚠️ `:129299` NON E' UNA FRASE: E' UNO SLOT VUOTO, E VA RESO IDENTICO

L'indice 1 della pozione di confusione ha, in tutt'e due le lingue, lo stesso
contenuto:

    JP  \\t\\t\\n\\n
    EN  \\t\\t\\n\\n

Due tabulazioni e due a capo. Non c'e' niente da tradurre, e `_code.py` lo dice
a modo suo — «righe senza resa in tabella: 1», perche' una coda `#...` non c'e'.

**La decisione**: si rende **identica**. Le altre due strade non stanno in piedi:

  - una resa **vuota** non e' esprimibile — e' la lezione della rinviata di
    `tcg.hsp:2470`, dove `estrai.firme_tradotte` conta come non tradotta ogni
    voce con `it` falso, e per spegnere quella riga ci volle una toppa;
  - **lasciarla fuori** terrebbe `FILTER_ITEM_POTION` a «1 da fare» per sempre,
    cioe' un cancello che non si chiude mai e che nessuno saprebbe piu' leggere.

ⓘ Il precedente vicino e' della 110a — «due righe dell'indice 3 hanno il
giapponese VUOTO... la riga si rende com'e'». Qui e' vuoto **anche l'inglese**,
ed e' il caso limite di quella stessa decisione.

### ⚠️⚠️ L'INGLESE E' ROTTO DUE VOLTE, E LE DUE VOLTE HA RICOPIATO UN'ALTRA RIGA

Il lotto 049 ne aveva trovata una (il te' nero con la frase del te' verde).
Qui ce n'e' un'altra, ed e' la stessa forma di guasto:

    :93069  il liquido ANTIACIDO
      JP   ...飲みすぎた日の強烈な胃酸に対して何ら耐性を得ることはないだろう
           (i succhi gastrici feroci del giorno dopo una bevuta)
      EN   ...the burns that occur when you eat something hot
           (che e' la chiusa del liquido IGNIFUGO, `:81811`, lotto 049)

Le due righe sono gemelle per costruzione — stessa struttura, un liquido che
protegge dal fuoco e uno che protegge dall'acido — e monte ha ricopiato la
chiusa dall'una all'altra senza cambiare l'ultima parola. Il giapponese
distingue, e la resa lo segue.

⭐ **Come si trovano**: non le trova nessuna rete, si vedono solo mettendo le due
righe **una accanto all'altra**, e in questo caso le due righe stanno in due
lotti diversi. E' la stessa forma della famiglia sparsa della 111a.

### ⭐ TRE FAMIGLIE CHE ATTRAVERSANO IL LOTTO

  - **le sette pozioni di cura** (`:126007`-`:126576`) sono una **scala**, e il
    giapponese la scrive con l'ironia crescente: la sacra guaritrice in cima,
    il bastone del goblin sciamano in fondo — «l'efficacia si sa gia' dove
    arriva». Le rese tengono la scala, e non alzano il registro di quelle
    basse;
  - **le due del ripristino** (`:112063` e `:112134`) sono la stessa frase due
    volte, una per la mente e una per il corpo, e cambia solo la battuta
    finale: 格好よかったあの頃 contro スラっとしていたあの頃. Rese in
    parallelo, e nessuna delle due chiede il genere del giocatore;
  - **i quattro liquori** (`:114277`, `:117531`, `:129085`, piu' l'idromele del
    049) portano tutti la coda `~Il Mondo Profondo dei Liquori~`.

### ⓘ I nomi che venivano da altre tabelle, e che il dossier non dava

Cinque termini della prosa sono nomi gia' decisi altrove, e copiarli
dall'inglese li avrebbe sdoppiati:

    スライム        -> **la melma** (non «slime»), e la riga la nomina due volte
    ハウンド        -> **il segugio** (glossario), due volte nella stessa riga
    パラライザー    -> **il paralizzatore**
    パンプキン      -> **la zucca**
    ダイオウサソリ  -> **lo scorpione re** ⚠️ l'inglese scrive «giant scorpion»
    沈黙の霧        -> **Nebbia di silenzio**, l'incantesimo (lotto 048)
    悪夢 / 元素の傷 -> **Incubo** / **Cicatrice elementale** (lotto 048)
    ポート・カプール -> **Porto Kapul** (non «Port Kapul»)

### ⓘ Due cose che il preflight ha fermato prima del dizionario

  - una **lineetta lunga** su `:106108`: CP932 non ce l'ha;
  - due **caporali** su `:126078`: nel dizionario non ce n'e' uno su 25.000
    rese. Il nome dell'oggetto si cita senza virgolette.

E tre parole dentro la finestra di rinculo (`proprietà` per «caratteristiche»,
`tensione` per «agitazione», e la perifrasi al posto di «dell'invisibilità»,
che era da 17): sciolte prima di reimportare invece che dopo.

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le code del lotto sono **cinque**, tutte gia' in tabella (`_code.py 050`: una
sola riga «senza resa», ed e' `:129299`, che una coda non ce l'ha). Il cancello
«titoli resi in PIU' modi» resta a **7**.

⚠️ La forma: **9** righe su 41 hanno lo spazio prima del `\\n` e 32 no; **32**
code hanno lo spazio dopo il `#` e 9 no. E **cinque** righe chiudono con un
`\\n` DOPO la coda: `:92522`, `:93554`, `:114277`, `:117531`, `:129085`.
ⓘ `:114277` porta anche la **tilde larga** nella coda inglese — e' una delle due
che `_112-corpo-descrizioni` conta come «titoli scritti con la tilde LARGA», e
la coda italiana usa quella normale, come vuole la tabella.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :90769
    (90769, 'Empty bottles that have contained something or are waiting to be filled. It is of no use as it is, but it can be used to draw water from a well or other source as emergency water. \\n#~Daily Necessities for the Home~'):
        "Una bottiglia vuota, che ha contenuto qualcosa o che aspetta con impazienza di contenerlo. Così com'è non serve a niente, ma ci si può prendere l'acqua da un pozzo, come scorta per le emergenze. \\n#~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :91656
    (91656, "It is made of white flakes that fall from the sky. This substance is very cold and instantly transforms into water when thrown, but it has the very rare property of never transforming as long as it is in one's possession. \\n# ~North Tyris Travels, Winter Edition~"):
        "Granelli bianchi che scendono dal cielo, raccolti e stretti in un pugno. È una materia freddissima: tirata, diventa acqua all'istante, ma finché la si tiene addosso non cambia mai, ed è una proprietà rara come poche. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    # ---------------------------------------------------------- :92323
    (92323, 'Dangerous potion with the obvious intention of setting the object ablaze. It can be thrown to create a pillar of fire in a designated area, but dangerous fire games should be played only when accompanied by a parent or guardian and after securing a supply of water. \\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione pericolosa, fatta senza nascondere l'intenzione di dare fuoco al bersaglio. Tirandola si alza una colonna di fiamme nel punto scelto; ma con il fuoco non si scherza: meglio farlo accompagnati da un adulto e con l'acqua a portata di mano. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :92522
    (92522, "A milky white liquid extracted from creatures by squeezing them. Highly nutritious, it's thought to support healthy growth and development. It's the primary ingredient for countless dairy products, though many enjoy drinking it straight. \\n#~Everchanging Food of Tyris~\\n"):
        "Un liquido bianco latteo, che si ricava mungendo gli animali. È molto nutriente e si ritiene conti molto per la crescita. È la materia prima dei latticini, ma non sono pochi quelli che se lo bevono così com'è.\\n#~Il Cibo Mutevole di Tyris~\\n",

    # ---------------------------------------------------------- :93069
    (93069, 'Potion that applies a acud-resistant protective coating to the item in which it is immersed. It is only effective on the item, so when you drink it, your internal organs will not show any resistance to the burns that occur when you eat something hot. \\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione che stende una pellicola resistente agli acidi su ciò che vi si immerge. Funziona solo sugli oggetti: a berla, le tue viscere non acquisteranno nessuna resistenza contro i succhi gastrici feroci del giorno dopo una bevuta. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :93554
    (93554, "A miraculous potion, it's the only effective treatment for the Ether Disease that inevitably plagues all living things. Whether it's extra eyeballs or poison glands in your hands, this potion can cure them all. But do keep in mind what a price such a valuable item could fetch.\\n# ~Irva Fantasy Encyclopedia~\\n"):
        "L'unica pozione miracolosa che guarisce la malattia dell'etere, che a vivere si prende per forza. Che ti siano spuntati occhi in più o che dalle mani ti coli veleno, cura tutto sul momento; ma è roba preziosa, quindi almeno identificarla conviene sempre.\\n# ~Dizionario Fantastico di Irva~\\n",

    # ---------------------------------------------------------- :96195
    (96195, "Objects can be soaked in this liquid to dye them in its color. It isn't a beverage of course, so drinking is not recommended. But if you want to add a splash of color to yourself, this author won't stop you.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Un liquido che esiste in molti colori e che, immergendovi un oggetto, glielo tinge del proprio. Non è una bevanda, ovviamente, quindi meglio non berlo; ma se vuoi conoscere una versione più sgargiante di te, nessuno ti ferma.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :96426
    (96426, 'In Tyris, few things are as precious as pure, untainted water. Despite the existence of distillation technology, pure water is nearly impossible to produce due to the presence of latent ether in the atmosphere, which can contaminate the liquid. It takes an immense amount of effort just to decontaminate the air of it on a daily basis.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "In Tyris l'acqua pura è una cosa preziosa. La tecnica della distillazione c'è, eppure l'acqua non si riesce a produrla, e la ragione è l'etere che si mescola di nascosto ai liquidi. Toglierlo dall'aria, dove ogni giorno abbonda, costa una fatica enorme.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :102108
    (102108, 'A very rare potion that can revert changes to your physical makeup. Unfortunately, it cannot cure the Ether Disease, but it can reverse the mutations that occur as a symptom of the illness. Yes, even the beneficial ones.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione rara come poche, che permette di rimettere gli occhi su ciò che si è diventati. La malattia dell'etere, purtroppo, non la guarisce, ma i sintomi che ti sono piombati addosso li cura tutti. Sì: anche le mutazioni buone.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :102179
    (102179, "A potion that causes the user's body to spontaneously develop monstrous features. Drinking it just to see what happens is not advised. Recommended for those who want to leave their humanity behind.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione che, a berla, fa crescere di colpo qualcosa che umano non è. Berla per curiosità è meglio di no. Consigliata solo a te che vuoi smettere di essere umano.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :102392
    (102392, 'A hazardous potion that allows its user to enjoy Nightmares and Elemental Scars at the same time. Never throw it at a friend just to see what happens.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione molto pericolosa, che fa assaggiare Incubo e Cicatrice elementale nello stesso momento. Non tirarla mai addosso a un amico per curiosità.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :104862
    (104862, "A potion with similar properties to a Slime's body fluids. Just as a Slime can melt anything it touches, this liquid dissolves things on contact. This, of course, can cause grievous bodily harm, so it should never be drunk to quench your thirst.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione con le stesse proprietà degli umori della melma. Come la melma scioglie qualunque cosa, questa corrode il materiale che tocca. Fa male anche al corpo umano, naturalmente: per quanta sete si abbia, non la si beva mai.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :105596
    (105596, 'When this dangerous potion is swallowed, the user is suddenly forced to remember their past mistakes, causing them to neglect their defenses. Its exact creation process is unclear, but it is certain that the bottle must be jam-packed with the insults of a Silver-Eyed Witch.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione pericolosa: a berla ti tornano in mente di colpo gli errori del passato e la guardia si abbassa. Come la si ricavi non si sa, ma di sicuro nella bottiglia ci sono stipati fino all'orlo gli insulti di una mietitrice dagli occhi d'argento.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :105813
    (105813, 'A potion that deludes the user into feeling like a god of battle. Though this effect is only temporary, it never fails, and so rookie guards keep it on hand at all times to stave off nerves on the job.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione che dà l'illusione che ti sia sceso addosso di colpo il dio della guerra. Dura poco, certo, ma l'effetto è reale, tanto che pare le guardie alle prime armi se la portino dietro giorno e notte per non farsi prendere dalla tensione sul lavoro. O almeno così si dice.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :106037
    (106037, "When this dangerous potion is ingested, the user's body becomes heavy like it's full of lead. On the flip side, it creates the illusion that the world around has sped up. This has led to a recent trend of problem users, half-addicted to drinking these potions and marveling at the rushing world around them.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione pericolosa: a berla il corpo si fa pesante come se avessi ingoiato del piombo e, di contro, sembra che il mondo intorno si sia messo a correre. Negli ultimi anni fa problema chi, preso da quel mondo fuori dall'ordinario, se la beve quasi per vizio.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :106108
    (106108, 'Drinking this potion makes it feel as if the timestream is flowing along your skin. A very useful potion that makes action as effortless as thought, but be careful: repeat abuse can lead to becoming so lazy you forget to breathe.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione che dà l'illusione di sentire sulla pelle lo scorrere del tempo. È preziosissima, perché basta pensare un gesto e il gesto viene da sé, ma attenzione a non abusarne fino a diventare così pigri da dimenticarsi di respirare.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :106325
    (106325, 'A decoction of fangs from every breed of Hound, this potion claims to confer resistance to all of their corresponding elements when consumed. This effect lasts for a very short time, so the mixture is probably heavily diluted.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Dice di rendere forti contro gli elementi dei segugi, perché mette insieme il decotto delle zanne di ogni razza di segugio. L'effetto dura pochissimo: probabilmente è parecchio allungata.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :106469
    (106469, "A potion that makes the user feel like a mighty Troll. Potentially as a psychosomatic effect, the user's body will regenerate at a staggering pace until the potion's effects wear off.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione che fa sentire di colpo un troll gagliardo. Che l'illusione prenda anche il corpo? Sta di fatto che, finché l'effetto dura, il ricambio di chi l'ha bevuta diventa una cosa mostruosa.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :106613
    (106613, 'A potion formulated by distilling condensed Mist of Silence, and grinding up the solids left behind. When this dangerous substance is ingested, it evokes a feeling of having a frog in your throat, making it impossible to verbalize magic spells.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione fatta distillando la Nebbia di silenzio raccolta e macinando quel che resta di solido. Basta berla una volta e in gola resta la sensazione di un corpo estraneo: altro che recitare formule. Roba pericolosa.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :106910
    (106910, "This potion makes the imbiber feel as if they've become an all-protecting shield. As a side effect of the ingredients, it also seems to relieve mild anxiety.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione che fa sentire di colpo uno scudo che protegge ogni cosa. Per via di quel che contiene, pare che anche un po' d'inquietudine smetta di dare fastidio.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :111992
    (111992, 'This potion causes permanent physical development for the user, through stimulation of the nervous system deep inside the body. Said to be highly beneficial for longevity, the ultra-rich are often sighted taking trips into town to purchase it.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione che fa crescere per sempre, stimolando dall'interno i nervi del corpo. Scalda a poco a poco, e la si ritiene ottima per campare a lungo: pare che i grandi ricchi scendano spesso in città apposta per comprarla.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :112063
    (112063, "A tonic that rids the drinker's mind of malign effects, restoring it to normal. All it does is return you to your usual self; so you can't use it to, for instance, turn your mind back to the good old days when you used to be cool.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione che, bevuta, riporta alla normalità i danni che avevano preso la mente. Riporta soltanto al te di sempre, quindi non serve, per dire, a tornare a quei tempi in cui facevi ancora la tua figura.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :112134
    (112134, "A tonic that rids the drinker's body of malign effects, restoring it to normal. All it does is return you to your usual self; so you can't use it to, for instance, turn your body back to the good old days when you used to be thin.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione che, bevuta, riporta alla normalità i danni che avevano preso il corpo. Riporta soltanto al te di sempre, quindi non serve, per dire, a tornare a quei tempi in cui la linea era un'altra.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :113676
    (113676, 'Poison extracted from the tail of a giant scorpion said to live in the pyramids is diluted with sewage water to make this potion. If taken, it is naturally poisonous, but with a smell like rotten fish, no one would like to drink it. \\n#~Drinks to Drink, Drinks Not to Drink~'):
        "Il veleno estratto dalla coda dello scorpione re, che si dice viva nelle piramidi, allungato con acqua sporca. A berlo ci si avvelena, com'è ovvio; ma con questa puzza di pesce marcio nessuno lo beve per suo piacere. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :114277
    (114277, "An alcoholic drink made from the fermentation of barley. Known for its pleasantly tongue-tingling carbonation, and a refreshing bitter aftertaste. If you visit the bar in Vernis, you'll find miners gulping it down like water.\\n#~The Wide World of Alcohol～\\n"):
        "Un liquore fatto fermentando l'orzo. Ha un modo di bere che formicola sulla lingua e un amaro pulito che resta a lungo. Alla taverna di Vernis si vedono i minatori che se la scolano come se fosse acqua.\\n#~Il Mondo Profondo dei Liquori~\\n",

    # ---------------------------------------------------------- :117531
    (117531, "Distilled liquor made from fermented grains. It's a common drink of choice in Noyel, though it also enjoys popularity in its main trade hub, Port Kapul. There are countless ways to drink it, but they say real men prefer to drink it straight.\\n#~The Wide World of Alcohol~\\n"):
        "Un liquore che si ottiene facendo fermentare l'orzo e poi distillandolo. A Noyel se ne beve molto, ma va forte anche a Porto Kapul, che è il suo principale sbocco commerciale. Di modi per berlo ce n'è più d'uno, ma si dice che un vero uomo lo beva liscio.\\n#~Il Mondo Profondo dei Liquori~\\n",

    # ---------------------------------------------------------- :126007
    (126007, "An amazing potion bearing the name of the sacred healer. Its formula has long been lost. The potion has an iridescent shine to it, but it's said that drinking it can leave wounds healed as if they were never real to begin with.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione da far tremare, che porta il nome della sacra guaritrice. Che cosa ci sia dentro non lo sa più nessuno, e il liquido ha il luccichio cangiante dell'iride; ma si dice che basti berne un sorso perché le ferite guariscano come se fossero state un sogno.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :126078
    (126078, 'Owing to its namesake, Eris the \\"White Healer\\", this potion has a milky white appearance. Unlike most potions, rather than being a product of various extracts, it consists of magical energy directly compounded with water. As a result, it\'s said to deliver fast-acting healing, even to patients on death\'s doorstep. \\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Come dice il nome di <Eris>, la guarigione bianca, è una pozione di un bianco latteo. A differenza delle altre non nasce da un estratto: è potere magico legato direttamente all'acqua. Per questo agisce in fretta, e si dice tenga dentro la forza di guarire perfino chi è ferito in fin di vita. \\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :126149
    (126149, 'An expensive potion named after the great healer Odina. Its azure color evokes an image of pure seawater. Wounds are said to disappear when immersed in it, like writing in the sand washed away by ocean waves. \\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione cara, che porta il nome di <Odina>, grande fra i guaritori. Si dice che a immergere una ferita in quel liquido color mare trasparente, il taglio sparisca come una scritta sulla sabbia. \\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :126292
    (126292, "A potion made using a secret herbal remedy, its formula closely guarded by healers since time immemorial. Sketchy as it may be, its  healing properties are undeniable, and it's worth having on hand in case of emergency. \\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Erbe medicinali che i guaritori custodiscono in silenzio da tempi antichi, ridotte in polvere e mescolate a una pozione. Ha un'aria molto sospetta, ma funziona sul serio: nelle emergenze conviene averne qualcuna dietro. \\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :126363
    (126363, 'A potion with an easy-to-understand and believable name. Though it shows a degree of efficacy in preventing wounds from getting worse, it may be a bit inadequate for healing preexisting injuries.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione dall'aria credibile, con un nome che si capisce al volo. L'effetto è quel che è: contro una ferita che si allarga funziona, ma su un taglio che continua a sanguinare c'è poco da fidarsi.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :126434
    (126434, "This potion is made with water from a secluded mountain spring, infused with extract of Cobra and the prayers of a healer. It actually does have moderate healing properties, though it's impossible to tell whether it's the Cobra extract or the prayers that are responsible.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Acqua sgorgata da una montagna silenziosa, in cui sono stati messi l'estratto di cobra e le parole di preghiera di un guaritore. Cura discretamente davvero; ma se il merito sia dell'estratto o della preghiera non c'è modo di saperlo.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :126505
    (126505, "This potion is formulated with all kinds of herbs said to have medicinal properties, thrown together and boiled down into one single concoction. The taste is overwhelmingly bitter, which gives the impression that it must be highly effective, but it actually isn't that powerful.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Tutte le erbe che si dicono buone per ogni male, ammucchiate insieme e fatte bollire a forza fino a farne una pozione che ne ha tutta l'aria. Il sapore è amarissimo e dà l'idea di chissà quale effetto, ma in realtà non è granché.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :126576
    (126576, "A potion made by extracting magic energy from a Goblin Shaman's staff. Much like said Goblin Shaman, its potency is rather weak. Some adventurers use it as a simple thirst-quencher. \\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Una pozione ricavata estraendo il potere magico dal bastone di un goblin sciamano. Visto che il bastone è pur sempre di un goblin, l'efficacia si sa già dove arriva. Pare che certi avventurieri se la portino dietro solo per togliersi la sete. \\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :129085
    (129085, 'Alcoholic drink with unknown ingredients, produced at an undisclosed location in Derphy. Like beer, it leaves a bubbly tingle in your mouth, but its fruity aroma gives rise to a splendid aftertaste. Furthermore, prolonged use of this alcohol is said to cause hallucinations, but the details are unclear. \\n#~The Wide World of Alcohol~\\n'):
        "Un liquore di ingredienti ignoti, prodotto di nascosto a Derphy. Formicola come la birra, ma un profumo di frutta gli mette in ordine il retrogusto. Si dice anche che a berlo di continuo faccia venire le allucinazioni, ma i dettagli non si sanno.\\n#~Il Mondo Profondo dei Liquori~\\n",

    # ---------------------------------------------------------- :129156
    (129156, 'A sweet-smelling liquid drug. It is said that it can bring sudden calm to even the most ferocious beasts. Highly recommended for insomniacs.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione dal profumo dolce. Si dice che, spruzzata addosso, calmi all'istante anche la belva più feroce. E una bottiglia è quel che ci vuole anche per te che non riesci a dormire.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :129227
    (129227, "A potion made with a decoction of Paralyzers. Consumption results in full-body paralysis. If accidentally ingested, don't worry; the effects wear off soon enough. But take care not to make a habit of it.\\n# ~Drinks to Drink, Drinks Not to Drink~"):
        "Il decotto di paralizzatore mescolato a una pozione. A berlo viene un formicolio tale da bloccare il corpo. Se lo si beve per sbaglio non c'è da preoccuparsi, perché passa; ma un consiglio: che non diventi un vizio.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :129298
    (129298, 'A tonic that causes severe headaches. Though temporary, the headaches seriously impair motor functions, reading ability, and speech skills. These symptoms can easily be mistaken for drunkenness, so take care not to accidentally consume it.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Una pozione che, bevuta, scatena un dolore acuto alla testa. Il mal di testa passa, ma intanto fa crollare l'equilibrio, la capacità di leggere e quella di parlare. E siccome i sintomi somigliano a quelli della sbornia, chi la beve per sbaglio viene scambiato per un ubriaco fradicio: da maneggiare con attenzione.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :129369
    (129369, 'Made from extract of Pumpkins, this potion was a born as a failed attempt at an invisibility potion. Though it was meant to make the drinker invisible, the monster extract concentrates entirely in the eyes, making it impossible to see anything but yourself.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "Un fallimento nato durante gli studi per ricavare dall'estratto delle zucche una pozione che rendesse invisibili. Doveva far sparire alla vista chi la beveva, ma l'estratto del mostro reagisce prima di tutto con gli occhi, e finisce per non far più riconoscere nient'altro che se stessi.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ---------------------------------------------------------- :129439
    (129439, 'In North Tyris, citizens gather this sort of water in empty bottles for everyday use. However, water pollution levels in North Tyris are off the charts, so drinking this common water is ill-advised.\\n# ~Drinks to Drink, Drinks Not to Drink~'):
        "L'acqua che in Tyris del Nord i cittadini usano tutti i giorni, messa in una bottiglia vuota. Sarà pure acqua per uso domestico, ma oggi in Tyris del Nord l'inquinamento è alto, e berla alla leggera non conviene.\\n# ~Bevande da Bere e Bevande da Non Bere~",

# 40 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-050.jsonl'
RIGHE = {
    90769, 91656, 92323, 92522, 93069, 93554, 96195, 96426, 102108, 102179,
    102392, 104862, 105596, 105813, 106037, 106108, 106325, 106469, 106613, 106910,
    111992, 112063, 112134, 113676, 114277, 117531, 126007, 126078, 126149, 126292,
    126363, 126434, 126505, 126576, 129085, 129156, 129227, 129298, 129369, 129439,
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
