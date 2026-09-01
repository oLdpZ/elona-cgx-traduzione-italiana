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
