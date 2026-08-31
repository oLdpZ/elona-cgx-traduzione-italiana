# -*- coding: utf-8 -*-
"""117a - Lotto 046 di `db_item.hsp`: I CIBI, il lotto che CHIUDE la categoria.

`FILTER_ITEM_FOOD`, righe da `:113749` a `:119461`: **31 righe** su 30 oggetti —
30 dell'indice 0 e **1** dell'indice 2. Con questo lotto `FILTER_ITEM_FOOD` va a
**0 da fare su 148 vive**: e' la **quinta** categoria del corpo che si chiude,
dopo mobilio, attrezzi, scarti e armi.

⚠️⚠️ Previsione di `applica`: **+32** per 31 rese.

### ⭐⭐⭐ LA RETE NUOVA HA TROVATO LA SECONDA GEMELLA DEL PROGETTO, SUBITO

`_previsione.py 046`, nata nel lotto 045 di questa stessa sessione, si e'
accesa al primo lotto in cui c'era qualcosa da trovare:

    :113814  ->  anche :113879   ⚠️ FUORI DAL LOTTO
    previsione di `applica`: +32 sostituzioni per 31 rese

`:113814` (il sacco di farina) e `:113879` (la pasta fresca) sono tutt'e due
l'**indice 2**, hanno il giapponese **vuoto** e lo stesso identico inglese:
`estrai.firma()` e' `sha1(jp + \\x00 + en)`, quindi una firma sola e una resa
che copre due righe.

⚠️ `:113879` **non e' nel lotto e non poteva esserci**: l'estrazione tiene una
voce per firma, quindi `_107-chiavi-item.py` non la emette. E' una delle **64
righe** che nessun lotto potra' mai scegliere (la differenza fra le 1.513 righe
di `_107-descrizioni-item` e le 1.449 firme di `_114-corpo-da-fare`), e si
riempie da sola quando si rende la gemella.

⭐ **Il valore della rete non e' aver detto 32.** E' che il 32 e' stato scritto
**prima** di lanciare `applica`, dove nel 042 lo stesso fatto era stato scoperto
dopo, guardando un numero che non tornava.

### ⭐⭐ LA QUARTA FIRMA GENERICA DELL'INDICE 2, E LA FAMIGLIA ERA GIA' SCRITTA

`:113814` e' la quarta e ultima delle firme generiche dell'indice 2 dei cibi —
il **moltiplicatore** che la 114a aveva annunciato leggendo «98 da fare su 148
vive». Le altre tre erano gia' rese, e la resa nuova le segue parola per parola:

    A type of vegetable that restores satiety...  Una verdura che sazia, e che
                                                  entra in molte ricette.
    A type of seafood  ...                        Un cibo di mare che sazia...
    A type of fruit    ...                        Un frutto che sazia...
    Food that restores satiety...     <- QUESTA    Un cibo che sazia, e che
                                                  entra in molte ricette.

ⓘ Le prime tre dicono «A type of X», questa dice «Food» e basta: e' la voce
generica per i cibi che non sono ne' verdura, ne' pesce, ne' frutta — la farina
e la pasta fresca.

### ⭐⭐ TRE ORTAGGI SI GUARDANO L'UN L'ALTRO, E L'INGLESE NE ROMPE DUE RIMANDI

Il giapponese incatena tre righe **dello stesso lotto**:

    :117978  la zucca      «parente della ウリ»          -> il MELONE, :117905
    :118787  la patata d.  «meno adatta della カボチ»     -> la ZUCCA,  :117978
    :118581  l'imo         «più piccolo della さつまいも» -> la PATATA DOLCE, :118787

L'inglese rompe i primi due: scrive «cucumber family» dove il giapponese dice
melone, e sostituisce il paragone con la zucca con un generico «It tastes
terrible when eaten wrong». In italiano i tre nomi sono quelli gia' a schermo —
melone, zucca, patata dolce — e i tre rimandi restano veri.

⚠️ **Nessuna rete puo' vederlo**: sono tre stringhe diverse, con tre inglesi
diversi, e il legame sta in una parola dentro la prosa. E' la lezione della
111a — «le altre righe della stessa famiglia» — applicata dentro un lotto solo.

### ⭐⭐ IL MOSTRO SI CHIAMA GIA' COME L'ORTAGGIO, E LA BATTUTA CI GUADAGNA

`:117978` chiude dicendo che c'e' chi sostiene che la カボチャ abbia a che fare
col mostro chiamato パンプキン. In giapponese sono **due parole diverse**, e la
battuta e' che qualcuno ci veda una parentela.

In italiano il mostro e' gia' **«zucca»** (`db_creature.hsp`, cercato con
`_cerca.py`), esattamente come l'ortaggio. Reso alla lettera, «il mostro
chiamato zucca» sarebbe una tautologia; reso **sul nome** — «il mostro che porta
il suo stesso nome» — la battuta funziona meglio che in giapponese, perche' in
italiano i due nomi coincidono davvero.

### ⚠️⚠️ L'INGLESE SOSTITUISCE DUE VOLTE, E UNA VOLTA INVENTA

  - `:113812` (la farina) e `:113877` (la pasta fresca): l'inglese scrive per
    **tutt'e due** la stessa frase — «Taste a lot better when cooked, but some
    prefer to ate it raw.» — e il giapponese dice due cose diverse, nessuna
    delle quali e' quella: nella farina «ci sara' pure una ragione, lasciamolo
    in pace», nella pasta la citazione di chi la mangia cruda;
  - `:118860` (il ravanello): il giapponese dice che da bambini ci si giocava a
    duello con questi in mano e ci si prendeva la sgridata **in due**;
    l'inglese scrive «It is often used in food fights by the childrens of
    Noyel». Ne' la battaglia di cibo ne' **Noyel** stanno nel giapponese;
  - `:115652` (la razione): l'inglese lascia cadere
    それに比例してか味の方は絶望的な出来栄えである, cioe' la battuta su cui la
    riga si chiude — si conserva benissimo, e il sapore e' disperato.

### ⚠️ UN ROVESCIAMENTO, UNA PAROLA LETTA MALE E UN'AGGIUNTA

  - `:118116` (il limone) — 大凡の果実のように…止めておいた方がよい dice che
    con **questo** non si fa quel che si fa con quasi tutti gli altri frutti.
    L'inglese scrive «like most fruits, should not be eaten directly», cioe'
    che a non doversi mangiare sono anche gli altri: il contrario;
  - `:119461` (la quwapana) — もいで e' «staccare, cogliere». L'inglese legge
    «wriggling», dimenare: le foglie si colgono, non si agitano;
  - `:113749` (il pesce bomba) — はじける e' «scoppiare». L'inglese scrive
    «burst into flames», e le fiamme nel giapponese non ci sono.

E due tagli piu' piccoli: `:119193` (l'uva) perde il chicco che sta nella bocca
di un bambino, e `:119258` (la mela) perde i modi di cucinarla nati lungo la
storia — che e' proprio la premessa della battuta sulla torta di mele.

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le code del lotto sono tre, tutte gia' in tabella con una sola resa italiana:
`~Il Cibo Mutevole di Tyris~` (29 righe), `~Rapporto di Identificazione:
categoria <Cibo>~` (1) e `~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~`
(1). Il cancello «titoli resi in PIU' modi» resta a **7**.

⚠️ La forma e' quasi uniforme, all'opposto del 044 e del 045: **2** righe su 31
hanno lo spazio prima del `\\n` (`:113940` e `:115652`) e **1** sola ha la coda
`# ~` (`:115652`). Uniforme non vuol dire deducibile: si legge lo stesso
`scratchpad/lotti-113/_forma.py 046`.
"""
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
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-046.jsonl'
RIGHE = {
    113749, 113812, 113814, 113877, 113940, 115652, 117599, 117832, 117905, 117978,
    118051, 118116, 118181, 118246, 118311, 118382, 118447, 118510, 118581, 118716,
    118787, 118860, 118933, 118998, 119063, 119128, 119193, 119258, 119331, 119396,
    119461,
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
