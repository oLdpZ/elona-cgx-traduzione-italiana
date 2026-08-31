import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :113749
    (113749, 'The most popular type of fish in North Tyris. It has many small bones, but has a relatively light flavour and seems to go well with any dish. Some of its relatives are said to burst into flames at the end of their lives.\\n#~Everchanging Food of Tyris~'):
        "Uno dei pesci più comuni di Tyris del Nord. Ha molte spine sottili, ma il sapore è abbastanza leggero e sta bene con qualunque piatto. Dicono che fra i suoi parenti stretti ce ne siano di quelli che, quando muoiono, scoppiano.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :113812
    (113812, 'Grounded wheat flour that can be made into various type of bread after processing. Taste a lot better when cooked, but some prefer to ate it raw.\\n#~Everchanging Food of Tyris~'):
        "Farina di grano macinato. Lavorandola se ne fanno pani di ogni tipo. Ogni tanto c'è il tipo strano che se la mangia così com'è, ma avrà le sue ragioni: lasciamolo in pace.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :113814
    (113814, "Food that restores satiety, it's used in many cooking dishes.\\n#~Identification Report: <Food> Category~"):
        "Un cibo che sazia, e che entra in molte ricette.\\n#~Rapporto di Identificazione: categoria <Cibo>~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :113877
    (113877, 'Raw material that is said to be the ancestor of all noodles. Taste a lot better when cooked, but some prefer to ate it raw.\\n#~Everchanging Food of Tyris~'):
        "La materia madre di tutte le paste, da cui può venire qualunque formato. È famosa anche per quanto in fretta si guasta. Ogni tanto c'è chi se la mangia così com'è, e a sentir loro \\\"quel sapore gentile e un po' dolce non si scorda\\\".\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :113940
    (113940, "A rather small loaf of bread in the shape of a thin stick. Smaller than regular bread, it is unlikely to fill one's stomach, but it seems to be enough for a quick bite when one is feeling hungry. \\n#~Everchanging Food of Tyris~"):
        "Un pane piccolino, a forma di bastoncino sottile. È più piccolo del pane normale, quindi la fame non la leva del tutto, ma per un morso al volo quando ti brontola lo stomaco basta e avanza. \\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :115652
    (115652, 'This food is said to have been carried by soldiers in ancient times when they went to battlefields, because it is portable, an has an extremely high shelf life which does not spoil at all. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Un cibo che, dicono, i soldati dei tempi antichi si portavano sempre dietro quando andavano in battaglia. Essendo cibo da viaggio si conserva benissimo e non marcisce affatto; ma, forse proprio per questo, quanto al sapore il risultato è disperato. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :117599
    (117599, 'The creature is in its natural state, and it is not suitable to be eaten raw as it is. How to cook them from this point on is where the skill of the chef really comes into play.\\n#~Everchanging Food of Tyris~'):
        "Una creatura così com'è, che a metterla in bocca in quello stato ti fa senso. Da qui in poi, come la si cucina è dove il cuoco fa vedere quanto vale.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :117832
    (117832, 'Vegetable very similar to lettuce. The leaves are slightly crunchy and are more suited to cooked dishes than raw. In recent years, a style of eating grilled meat wrapped in these leaves has been established that takes advantage of this point.\\n#~Everchanging Food of Tyris~'):
        "Una verdura che somiglia moltissimo alla lattuga. Le foglie sono un po' più sotto i denti, e più che cruda si presta ai piatti passati sul fuoco. Proprio giocando su questo, da qualche anno si è preso l'uso di avvolgerci dentro la carne alla griglia.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :117905
    (117905, 'Oval-shaped vegetable with a high water content. It can be eaten raw to enjoy its water content and tactile qualities, but when stewed, its smooth mouthfeel is unforgettable.\\n#~Everchanging Food of Tyris~'):
        "Una verdura ovale, piena d'acqua. Mangiarla cruda per goderne l'acqua e la consistenza va benissimo, ma quando la si fa bollire si scioglie in bocca in un modo che non si dimentica.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :117978
    (117978, 'A member of the cucumber family with very hard skin. Because of its characteristics, it is not suitable for eating raw and is usually cooked. There are also those who insist that it is related to the pumpkin monster, but this does not seem to be recognised by the public.\\n#~Everchanging Food of Tyris~'):
        "Parente del melone, con la buccia durissima. Proprio per questo cruda non va, e di regola la si passa sul fuoco. E c'è chi insiste a dire che abbia a che fare col mostro che porta il suo stesso nome, ma la cosa non pare riconosciuta da nessuno.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118051
    (118051, 'Small, granular vegetable. As an edible seed, it is highly nutritious. It is mainly used in soups, etc., and its bright green colour is very appetising.\\n#~Everchanging Food of Tyris~'):
        "Una verdura in granelli piccoli. È un seme che si mangia, quindi il valore nutritivo è ottimo. La si usa soprattutto nelle minestre, e quel verde acceso mette una gran fame.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118116
    (118116, 'A spindle-shaped fruit with a pungent taste. Its taste is indescribably sour and, like most fruits, should not be eaten directly as an after-dinner palate cleanser.\\n#~Everchanging Food of Tyris~'):
        "Un frutto a fuso che tiene dentro un sapore pungente. È aspro da non potersi dire a parole, quindi meglio non mangiarlo tale e quale a fine pasto per pulirsi la bocca, come invece si fa con quasi tutti gli altri frutti.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118181
    (118181, 'Fruit with fresh and rich texture. Its moisture content is more than sufficient to quench thirst, and naturally it is preferable to prepare it accordingly.\\n#~Everchanging Food of Tyris~'):
        "Un frutto dalla polpa piena di succo. L'acqua che ha dentro è più che sufficiente a togliere la sete, e va da sé che i modi di cucinarlo migliori sono quelli che vanno in quella direzione.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118246
    (118246, 'This small fruit is said to come from the land where the sun never sets. The bright orange colour of the fruit is so bright that it could be mistaken for a small sun, as is the flesh, and the taste is, as is typical of such fruits, very sour and sweet.\\n#~Everchanging Food of Tyris~'):
        "Un frutto piccolo che, dicono, viene dal paese dove il sole non tramonta. È di un arancione così acceso che pare un piccolo sole, e la polpa è dello stesso colore; il sapore, come in tutti i frutti di quella specie, è un dolce con dentro molta acidità.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118311
    (118311, 'A valuable fruit that can be seen in different colours depending on the light. Many people like them not only for their appearance, but also for their taste, which varies from unripe to fully ripe. On the other hand, it is difficult for cooks to find the flavour they are looking for.\\n#~Everchanging Food of Tyris~'):
        "Un frutto prezioso che, a seconda di come batte la luce, si vede di colori diversi. Piace a molti non solo per come si presenta, ma perché anche il sapore cambia via via, dall'acerbo al maturo. Il rovescio è che per chi cucina è difficile trovare il sapore che cerca.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118382
    (118382, 'A variety of wild herbs that have been believed to be beneficial for physical improvement since ancient times. As a vegetable eaten as an extension of folk medicine, it has no fast-acting effect and even its efficacy is questionable. It tastes extremely bitter, but there are rare people who find it irresistible.\\n#~Everchanging Food of Tyris~'):
        "Una delle tante erbe di campo che fin dai tempi antichi si dicono buone per rimettere in sesto il corpo. Essendo una verdura che si mangia come si fa coi rimedi della nonna, effetto immediato non ne ha, anzi: perfino che serva a qualcosa è dubbio. Il sapore è amaro da morire, ma qualche raro tipo lo trova buonissimo.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118447
    (118447, 'A red fruit with a small shape. It is sour and gives a pleasant kick, but when heated, it loses its acidity and instead a wrapping, leisurely sweetness dances on your tongue.\\n#~Everchanging Food of Tyris~'):
        "Un frutto rosso di forma piccola. La polpa è acidula e dà una scossa piacevole al corpo stanco; ma se la scaldi l'acidità se ne va, e al suo posto ti balla sulla lingua una dolcezza lenta e piena, che ti avvolge tutto.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118510
    (118510, 'Nuts that is found in all regions of North Tyris. It produces a sweet taste with a slight astringency, but when dried, the sweet taste increases, and the astringency transforms into a slight sour taste. It has a very high shelf life and many adventurers carry it with them.\\n#~Everchanging Food of Tyris~'):
        "Il frutto che cade dagli alberi da frutto che crescono in tutta Tyris del Nord. Dà un sapore dolce con dentro un filo che allappa; ma a seccarlo quel filo sparisce, il dolce si fa più forte e ci si mette anche un poco d'acido. Si conserva benissimo, e sono in molti fra chi va all'avventura a portarselo dietro.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118581
    (118581, 'Vegetable whose underground part of the stem is eaten. Although slightly smaller than sweet potatoes, these do not become sweeter when heated and are regarded as an everyday staple food. It is a versatile vegetable that can be used in all kinds of cooking methods except when eaten raw.\\n#~Everchanging Food of Tyris~'):
        "Una verdura di cui si mangia la parte del fusto che sta sotto terra. È un po' più piccola della patata dolce, ma a differenza di quella col calore non diventa dolce, e la si tratta come il cibo di tutti i giorni. Fuori che cruda, sta bene con qualunque modo di cucinare: una verdura buona a tutto.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118716
    (118716, 'It is vegetable that looks like a bunch of leaves. Some of them can be slightly bitter when eaten raw, but they are most popularly used in salads and other dishes. It can also be cooked, but this method seems to be less popular.\\n#~Everchanging Food of Tyris~'):
        "Una verdura che pare un mazzo di foglie. Cruda, certe volte viene un po' amara, ma il modo comune di usarla è soprattutto in insalata. C'è anche chi la passa sul fuoco, ma quell'uso non ha preso molto piede.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118787
    (118787, "Vegetable with enlarged edible roots. It tastes terrible when eaten wrong, and was said by a powerful man to be 'only a Yeek will eat it raw'. However, it is also suitable for other cooking, and some species are so sweet when steamed that they can be mistaken for expensive pastries.\\n#~Everchanging Food of Tyris~"):
        "Una verdura di cui si mangia la radice, che si fa grossa. È ancora meno adatta della zucca a essere mangiata cruda, tanto che un potente del tempo disse: \\\"cruda la mangia soltanto uno yeek\\\". Con gli altri modi di cucinarla però ci sta bene, e certe varietà, cotte a vapore, vengono dolci da confonderle con un dolce di lusso.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118860
    (118860, 'Vegetable with a characteristic white colour. They are so rich in water that they overflow even when cut. It is often used in food fights by the childrens of Noyel.\\n#~Everchanging Food of Tyris~'):
        "Una verdura che si riconosce dal suo bianco. Basta tagliarla e l'acqua trabocca. Saranno in tanti quelli che da bambini ci hanno giocato a spade, in due, e in due si sono presi la sgridata.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118933
    (118933, 'Vegetable with a red, horn-like shape. It is characterised by a subtle sweetness when cooked. It is a versatile vegetable, both raw and cooked, but some people do not like the sweetness when cooked, so be careful when serving it to others.\\n#~Everchanging Food of Tyris~'):
        "Una verdura a forma di corno rosso. La sua particolarità è che al calore tira fuori un filo di dolce. Cruda o cotta va bene sempre, ma quel dolce della cottura a qualcuno non piace: quando la porti a tavola per altri, occhio.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :118998
    (118998, 'A fruit with a peach-coloured flesh that is said to have been introduced from the tropics. The taste is very sweet and sour and appetising, but the smell is peculiar, so it is said to be eater-picky.\\n#~Everchanging Food of Tyris~'):
        "Un frutto venuto, dicono, dai paesi del sud, con la polpa di un rosa che è bello da vedere. È molto dolce e aspro insieme, un sapore che mette fame, ma l'odore è tutto suo e quindi si sceglie chi lo apprezza.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :119063
    (119063, 'Fruit with small, pretty berries, also known as red jewels. The fruits range from sweet to sour, but those from the suburbs of Yowyn are said to be of the best quality, small but very sweet.\\n#~Everchanging Food of Tyris~'):
        "Un frutto che porta bacche piccole e graziose, che qualcuno chiama gemme rosse. Ce ne sono di dolci e di aspre, ma le migliori, dicono, sono quelle dei dintorni di Yowyn: piccole, e dolcissime.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :119128
    (119128, 'A refreshingly sour fruit from the land of everlasting summer. The flesh is bright green in contrast to the outer skin, which is reminiscent of animal hair, and attracts the interest of those who see it. Its soft flesh is suitable for eating raw.\\n#~Everchanging Food of Tyris~'):
        "Un frutto venuto dal paese dell'estate senza fine, che dà un'acidità fresca. La buccia pare pelo d'animale, e la polpa invece è di un verde acceso: a vederlo, viene voglia di saperne di più. La polpa è morbida, quindi si presta a mangiarlo crudo.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :119193
    (119193, 'Dark blue fruit grown in a cluster like berries. Once eaten, its distinctive sweet flavour fills the mouth and you are instantly captivated by the fruit. It is sometimes used to make wine.\\n#~Everchanging Food of Tyris~'):
        "Un frutto blu scuro che fa i chicchi attaccati uno all'altro. Un chicco è piccolo, sta nella bocca di un bambino, ma basta assaggiarne uno e il profumo dolce tutto suo ti riempie la bocca: sarai suo prigioniero all'istante. Pare che lo usino anche per fare il vino.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :119258
    (119258, 'Fruit with a fresh red colour. Since ancient times, it has been called the source of wisdom and the fruit of good fortune, and has a long history with us. However, for some reason, apple pie cannot be made from apples.\\n#~Everchanging Food of Tyris~'):
        "Un frutto di un rosso pieno di succo. Fin dai tempi antichi la chiamano sorgente della sapienza o cristallo della fortuna, tanto la sua storia con noi è lunga, e insieme sono nati modi di cucinarla di ogni sorta. Eppure, chissà perché, l'unica cosa che dalla mela non si riesce a fare è la torta di mele.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :119331
    (119331, 'A type of vegetable known as wild herbs that grows in the wild. Its simple taste is a tremendous luxury for nature lovers.\\n#~Everchanging Food of Tyris~'):
        "Una di quelle verdure che chiamano erbe di campo, e che crescono nei prati. Quel suo sapore semplice, per chi ama la natura, è un lusso che non ha prezzo.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :119396
    (119396, 'A plant which is said to have been used in medicine since ancient times, is believed to have a bowel-regulating effect, but no firm conclusions have been reached. Aloe in North Tyris has a slightly sweet taste and is therefore treated in the same way as the fruit.\\n#~Everchanging Food of Tyris~'):
        "Una pianta dalle foglie piene di succo. La polpa, che fin dai tempi antichi dicono si usasse anche in medicina, pare rimetta a posto l'intestino, ma niente di sicuro si è mai concluso. A Tyris del Nord la polpa ha dentro un poco di dolce, e per questo la trattano come si tratta la frutta.\\n#~Il Cibo Mutevole di Tyris~",

    # ---------------------------------------------------------- :119461
    (119461, 'An unusual tropical plant whose leaves are eaten by wriggling them. The tactile sensation when you bite into it, its moderate moisture and good acidity will surely give you a new experience.\\n#~Everchanging Food of Tyris~'):
        "Una pianta dei paesi del sud, rara al mondo: le foglie si staccano e si mangiano così come sono. La consistenza sotto i denti, l'acqua giusta e quel filo d'acido ti daranno di sicuro un'esperienza che non hai mai fatto.\\n#~Il Cibo Mutevole di Tyris~",

# 30 voci, 0 ambigue
}
