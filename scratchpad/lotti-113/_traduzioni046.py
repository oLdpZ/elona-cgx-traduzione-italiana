# -*- coding: utf-8 -*-
"""Le rese del lotto 046 — I CIBI, terza e ultima parte: la categoria si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 046 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa046.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `scratchpad/lotti-113/_forma.py 046`: solo **2** righe su 31 hanno
lo spazio prima del `\\n` (`:113940` e `:115652`) e solo **1** ha la coda con lo
spazio dopo il `#` (`:115652`).

⚠️⚠️ Previsione di `applica`: **+32** per 31 rese. `_previsione.py 046` trova
una **gemella**: `:113814` e `:113879` hanno il giapponese vuoto e lo stesso
inglese, quindi una firma sola, e la resa copre tutt'e due. La seconda non e'
in nessuna tabella. Vedi `testa046.py`.
"""

IT = {
    # === IL PESCE, LA FARINA, LA PASTA E IL PANE ==========================
    # ⚠️ l'inglese aggiunge le fiamme: はじける e' «scoppiare», non «bruciare».
    113749: "Uno dei pesci più comuni di Tyris del Nord. Ha molte spine sottili, ma il sapore è abbastanza leggero e sta bene con qualunque piatto. Dicono che fra i suoi parenti stretti ce ne siano di quelli che, quando muoiono, scoppiano.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️⚠️ l'inglese SOSTITUISCE la seconda frase, e la sostituisce con la
    #    STESSA per la farina e per la pasta fresca: «Taste a lot better when
    #    cooked, but some prefer to ate it raw.» Il giapponese dice due cose
    #    diverse, e nessuna delle due e' quella.
    113812: "Farina di grano macinato. Lavorandola se ne fanno pani di ogni tipo. Ogni tanto c'è il tipo strano che se la mangia così com'è, ma avrà le sue ragioni: lasciamolo in pace.\\n#~Il Cibo Mutevole di Tyris~",

    # ⭐ la QUARTA firma generica dell'indice 2 dei cibi, e l'unica ancora da
    #    fare: le altre tre dicono «A type of vegetable / seafood / fruit».
    #    Questa dice «Food» e basta, e la resa segue la famiglia gia' in gioco.
    # ⚠️ copre anche `:113879` (la pasta fresca), che nessuna tabella offre.
    113814: "Un cibo che sazia, e che entra in molte ricette.\\n#~Rapporto di Identificazione: categoria <Cibo>~",

    113877: "La materia madre di tutte le paste, da cui può venire qualunque formato. È famosa anche per quanto in fretta si guasta. Ogni tanto c'è chi se la mangia così com'è, e a sentir loro \\\"quel sapore gentile e un po' dolce non si scorda\\\".\\n#~Il Cibo Mutevole di Tyris~",

    113940: "Un pane piccolino, a forma di bastoncino sottile. È più piccolo del pane normale, quindi la fame non la leva del tutto, ma per un morso al volo quando ti brontola lo stomaco basta e avanza. \\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️ l'inglese lascia cadere la battuta su cui la riga si chiude: それに
    #    比例してか味の方は絶望的な出来栄えである — il sapore e' disperato.
    115652: "Un cibo che, dicono, i soldati dei tempi antichi si portavano sempre dietro quando andavano in battaglia. Essendo cibo da viaggio si conserva benissimo e non marcisce affatto; ma, forse proprio per questo, quanto al sapore il risultato è disperato. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    117599: "Una creatura così com'è, che a metterla in bocca in quello stato ti fa senso. Da qui in poi, come la si cucina è dove il cuoco fa vedere quanto vale.\\n#~Il Cibo Mutevole di Tyris~",

    # === LE VERDURE =======================================================
    117832: "Una verdura che somiglia moltissimo alla lattuga. Le foglie sono un po' più sotto i denti, e più che cruda si presta ai piatti passati sul fuoco. Proprio giocando su questo, da qualche anno si è preso l'uso di avvolgerci dentro la carne alla griglia.\\n#~Il Cibo Mutevole di Tyris~",

    117905: "Una verdura ovale, piena d'acqua. Mangiarla cruda per goderne l'acqua e la consistenza va benissimo, ma quando la si fa bollire si scioglie in bocca in un modo che non si dimentica.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️ l'inglese scrive «cucumber family» dove il giapponese dice ウリの仲間,
    #    ed e' il MELONE di `:117905`, che sta in questo stesso lotto.
    # ⭐ e パンプキン, il mostro, in italiano si chiama gia' «zucca»
    #    (`db_creature.hsp`): la battuta si rifa' sul nome, non sulle sillabe.
    117978: "Parente del melone, con la buccia durissima. Proprio per questo cruda non va, e di regola la si passa sul fuoco. E c'è chi insiste a dire che abbia a che fare col mostro che porta il suo stesso nome, ma la cosa non pare riconosciuta da nessuno.\\n#~Il Cibo Mutevole di Tyris~",

    118051: "Una verdura in granelli piccoli. È un seme che si mangia, quindi il valore nutritivo è ottimo. La si usa soprattutto nelle minestre, e quel verde acceso mette una gran fame.\\n#~Il Cibo Mutevole di Tyris~",

    # === LA FRUTTA ========================================================
    # ⚠️ ROVESCIAMENTO: 大凡の果実のように…止めておいた方がよい vuol dire che
    #    con questo NON si fa quel che si fa con quasi tutti gli altri frutti.
    #    L'inglese scrive «like most fruits, should not be eaten», cioe' che a
    #    non doversi mangiare sono anche gli altri.
    118116: "Un frutto a fuso che tiene dentro un sapore pungente. È aspro da non potersi dire a parole, quindi meglio non mangiarlo tale e quale a fine pasto per pulirsi la bocca, come invece si fa con quasi tutti gli altri frutti.\\n#~Il Cibo Mutevole di Tyris~",

    118181: "Un frutto dalla polpa piena di succo. L'acqua che ha dentro è più che sufficiente a togliere la sete, e va da sé che i modi di cucinarlo migliori sono quelli che vanno in quella direzione.\\n#~Il Cibo Mutevole di Tyris~",

    118246: "Un frutto piccolo che, dicono, viene dal paese dove il sole non tramonta. È di un arancione così acceso che pare un piccolo sole, e la polpa è dello stesso colore; il sapore, come in tutti i frutti di quella specie, è un dolce con dentro molta acidità.\\n#~Il Cibo Mutevole di Tyris~",

    118311: "Un frutto prezioso che, a seconda di come batte la luce, si vede di colori diversi. Piace a molti non solo per come si presenta, ma perché anche il sapore cambia via via, dall'acerbo al maturo. Il rovescio è che per chi cucina è difficile trovare il sapore che cerca.\\n#~Il Cibo Mutevole di Tyris~",

    118382: "Una delle tante erbe di campo che fin dai tempi antichi si dicono buone per rimettere in sesto il corpo. Essendo una verdura che si mangia come si fa coi rimedi della nonna, effetto immediato non ne ha, anzi: perfino che serva a qualcosa è dubbio. Il sapore è amaro da morire, ma qualche raro tipo lo trova buonissimo.\\n#~Il Cibo Mutevole di Tyris~",

    118447: "Un frutto rosso di forma piccola. La polpa è acidula e dà una scossa piacevole al corpo stanco; ma se la scaldi l'acidità se ne va, e al suo posto ti balla sulla lingua una dolcezza lenta e piena, che ti avvolge tutto.\\n#~Il Cibo Mutevole di Tyris~",

    118510: "Il frutto che cade dagli alberi da frutto che crescono in tutta Tyris del Nord. Dà un sapore dolce con dentro un filo che allappa; ma a seccarlo quel filo sparisce, il dolce si fa più forte e ci si mette anche un poco d'acido. Si conserva benissimo, e sono in molti fra chi va all'avventura a portarselo dietro.\\n#~Il Cibo Mutevole di Tyris~",

    # === I DUE TUBERI, CHE SI GUARDANO ====================================
    # ⭐ l'imo si misura sulla patata dolce e la patata dolce sulla zucca: tre
    #    righe dello stesso lotto che si tengono per mano. In italiano i tre
    #    nomi sono quelli gia' a schermo, e i rimandi restano veri.
    118581: "Una verdura di cui si mangia la parte del fusto che sta sotto terra. È un po' più piccola della patata dolce, ma a differenza di quella col calore non diventa dolce, e la si tratta come il cibo di tutti i giorni. Fuori che cruda, sta bene con qualunque modo di cucinare: una verdura buona a tutto.\\n#~Il Cibo Mutevole di Tyris~",

    118716: "Una verdura che pare un mazzo di foglie. Cruda, certe volte viene un po' amara, ma il modo comune di usarla è soprattutto in insalata. C'è anche chi la passa sul fuoco, ma quell'uso non ha preso molto piede.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️ l'inglese perde il paragone con la zucca («カボチより更に生食に
    #    向かず») e ci mette una frase generica.
    118787: "Una verdura di cui si mangia la radice, che si fa grossa. È ancora meno adatta della zucca a essere mangiata cruda, tanto che un potente del tempo disse: \\\"cruda la mangia soltanto uno yeek\\\". Con gli altri modi di cucinarla però ci sta bene, e certe varietà, cotte a vapore, vengono dolci da confonderle con un dolce di lusso.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️⚠️ l'inglese SOSTITUISCE l'ultima frase da capo: il giapponese dice che
    #    da bambini ci si giocava a duello e si finiva sgridati in due,
    #    l'inglese scrive una battaglia di cibo dei bambini di Noyel — che nel
    #    giapponese non c'e', ne' la battaglia ne' Noyel.
    118860: "Una verdura che si riconosce dal suo bianco. Basta tagliarla e l'acqua trabocca. Saranno in tanti quelli che da bambini ci hanno giocato a spade, in due, e in due si sono presi la sgridata.\\n#~Il Cibo Mutevole di Tyris~",

    118933: "Una verdura a forma di corno rosso. La sua particolarità è che al calore tira fuori un filo di dolce. Cruda o cotta va bene sempre, ma quel dolce della cottura a qualcuno non piace: quando la porti a tavola per altri, occhio.\\n#~Il Cibo Mutevole di Tyris~",

    # === LA FRUTTA, SECONDA PARTE =========================================
    118998: "Un frutto venuto, dicono, dai paesi del sud, con la polpa di un rosa che è bello da vedere. È molto dolce e aspro insieme, un sapore che mette fame, ma l'odore è tutto suo e quindi si sceglie chi lo apprezza.\\n#~Il Cibo Mutevole di Tyris~",

    119063: "Un frutto che porta bacche piccole e graziose, che qualcuno chiama gemme rosse. Ce ne sono di dolci e di aspre, ma le migliori, dicono, sono quelle dei dintorni di Yowyn: piccole, e dolcissime.\\n#~Il Cibo Mutevole di Tyris~",

    119128: "Un frutto venuto dal paese dell'estate senza fine, che dà un'acidità fresca. La buccia pare pelo d'animale, e la polpa invece è di un verde acceso: a vederlo, viene voglia di saperne di più. La polpa è morbida, quindi si presta a mangiarlo crudo.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️ l'inglese perde 一粒は子供の口に入るほど小さい, il chicco che sta
    #    nella bocca di un bambino.
    119193: "Un frutto blu scuro che fa i chicchi attaccati uno all'altro. Un chicco è piccolo, sta nella bocca di un bambino, ma basta assaggiarne uno e il profumo dolce tutto suo ti riempie la bocca: sarai suo prigioniero all'istante. Pare che lo usino anche per fare il vino.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️ l'inglese perde 様々な調理方法が生まれいる, i modi di cucinarla nati
    #    lungo quella storia — che e' proprio la premessa della battuta finale.
    119258: "Un frutto di un rosso pieno di succo. Fin dai tempi antichi la chiamano sorgente della sapienza o cristallo della fortuna, tanto la sua storia con noi è lunga, e insieme sono nati modi di cucinarla di ogni sorta. Eppure, chissà perché, l'unica cosa che dalla mela non si riesce a fare è la torta di mele.\\n#~Il Cibo Mutevole di Tyris~",

    119331: "Una di quelle verdure che chiamano erbe di campo, e che crescono nei prati. Quel suo sapore semplice, per chi ama la natura, è un lusso che non ha prezzo.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️ l'inglese fonde la prima frase nella seconda e perde 瑞々しい葉をもつ.
    119396: "Una pianta dalle foglie piene di succo. La polpa, che fin dai tempi antichi dicono si usasse anche in medicina, pare rimetta a posto l'intestino, ma niente di sicuro si è mai concluso. A Tyris del Nord la polpa ha dentro un poco di dolce, e per questo la trattano come si tratta la frutta.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️ l'inglese legge もいで («staccare») come «wriggling»: le foglie si
    #    colgono, non si dimenano.
    119461: "Una pianta dei paesi del sud, rara al mondo: le foglie si staccano e si mangiano così come sono. La consistenza sotto i denti, l'acqua giusta e quel filo d'acido ti daranno di sicuro un'esperienza che non hai mai fatto.\\n#~Il Cibo Mutevole di Tyris~",
}
