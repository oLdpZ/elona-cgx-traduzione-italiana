# -*- coding: utf-8 -*-
"""Le rese del lotto 004, indicizzate per RIGA e nient'altro.

Le chiavi vere del lotto sono coppie `(riga, inglese)`, e l'inglese si copia
**verbatim** dal sorgente: qui non si scrive, cosi' non lo si puo' sbagliare.
`_monta004.py` prende questo file e `chiavi004.txt` e ne fa `rese004.py`.

Le quattro code fisse del rapporto, che il giapponese ripete su tutta la
categoria (la formula della 108a, estesa agli attrezzi):

    何度でも使用することができる  ->  Si può usare sempre.
    何度か使用することができる    ->  Si può usare più volte.
    定期的に使用することができる  ->  Si può usare ogni tanto.
    使用することができる（使い捨て）-> Si usa (usa e getta).
    投げつけて使う（使い捨て）    ->  Si lancia (usa e getta).
    投げることができる            ->  Si può lanciare.
"""

IT = {
    # --- i quattro fucili anestetici: un solo giapponese, quattro inglesi.
    # Il peso lo dice il NOME dell'oggetto (TZ500-K, TZC-500, TZ30-C, TZ-30),
    # e il giapponese dice solo che l'effetto ne dipende. Come i dieci atti
    # dei mezzi di trasporto della 108a: si segue il giapponese.
    42418: "Fucile anestetico: l'effetto varia col peso. Si usa più volte.",
    42494: "Fucile anestetico: l'effetto varia col peso. Si usa più volte.",
    42570: "Fucile anestetico: l'effetto varia col peso. Si usa più volte.",
    42646: "Fucile anestetico: l'effetto varia col peso. Si usa più volte.",

    42712: "Bacchette di legno. Si usa (usa e getta).",
    43243: "Dà un altro aspetto, a chiunque. Si può usare sempre.",
    44100: "Ci si porta via chi è in fin di vita o inerme. Si usa sempre.",
    44166: "Genera energia da lavoro a forza di braccia. Si può usare sempre.",

    45484: "Una pietra che piazza trappole. Si può usare sempre.",
    45550: "Una pietra che dà AP. Si usa (usa e getta).",
    45616: "Una pietra che dà magia e MP. Si usa (usa e getta).",
    45682: "Una pietra che dà costituzione e SP. Si usa (usa e getta).",
    45748: "Alza tutte le resistenze fino a un limite. Si usa (usa e getta).",
    45814: "Alza il modificatore DV. Si usa (usa e getta).",
    45880: "Alza il modificatore PV. Si usa (usa e getta).",
    45947: "Potenzia il Potioman. Si usa (usa e getta).",

    46079: "Un materiale speciale, per certi cadaveri. Si usa (usa e getta).",
    46145: "Una protesi che dà una parte del corpo. Si usa (usa e getta).",
    46406: "Dà una gran quantità di tappi. Si usa (usa e getta).",
    46482: "Un'arma che rompe la guardia. Si può usare più volte.",
    # le quattro carte dei semi (quadri, cuori, fiori, picche) sono una firma sola
    46550: "Uno strumento che evoca gli spiriti. Si può usare sempre.",
    46821: "Rivela una parte del carattere. Si può usare sempre.",
    46887: "Serve ad avere una figlia forte. Si usa (usa e getta).",
    46953: "Serve ad avere un figlio forte. Si usa (usa e getta).",

    47019: "Dà esperienza alle armi viventi. Si usa (usa e getta).",
    47086: "Un anello che ridà MP. Si usa (usa e getta).",
    47289: "Calzini che puzzano. Si può usare sempre.",

    49779: "Disseta; si riempie sott'acqua. Si può usare sempre.",
    # i tre frammenti (Caos, Rehmido, Lesimas) sono una firma sola
    49850: "Alza gli attributi fino a un limite. Si può usare sempre.",

    50063: "Trasforma in oro il nemico in fin di vita. Si può usare sempre.",
    50134: "Dà fama o autorità. Si può usare sempre.",
    50205: "Attiva due capacità insieme. Si può usare sempre.",
    50274: "Fa sposare anche chi non è tra i compagni. Si può usare sempre.",
    50344: "Funziona sulla mappa del mondo. Si può usare ogni tanto.",
    50411: "Dimezza un'abilità e dà un piccolo bonus. Si usa (usa e getta).",
    # i quattro Potioman sono una firma sola
    50477: "Spara tappi di pozione a gran velocità. Si può usare sempre.",
    50749: "Elabora una mole enorme di informazioni. Si può usare sempre.",
    # i tre globi oscuri (verde, blu, cremisi) sono una firma sola
    50948: "Piazza e innesca trappole (non attivo). Si può usare sempre.",

    51291: "Un frammento con la memoria di un'abilità. Si usa (usa e getta).",
    51982: "Stende una cortina di fumo. Si lancia (usa e getta).",
    52048: "Una carta per vedere e spendere i punti. Si può usare sempre.",
    52383: "Allena le abilità con le armi. Si può usare sempre.",
    52449: "Fissa il raccolto. Si può usare sempre.",

    54888: "Serve ad accendere il fuoco. Si usa (usa e getta).",
    55145: "Potenzia l'attacco a distanza. Si può usare sempre.",
    55484: "Un frammento che contiene magia. Si usa (usa e getta).",
    56606: "Serve a pulirsi le orecchie. Si può usare sempre.",
    57066: "Non si mangia: usandolo, mangiano tutti i compagni (usa e getta).",
    57648: "Riproduce la dea della ricchezza. Si può usare ogni tanto.",
    58529: "Una spada per il seppuku. Non si equipaggia, ma si usa sempre.",

    59661: "Polvere di stelle che potenzia un artefatto (usa e getta).",
    59929: "Un apparecchio che fa statuette. Si usa (usa e getta).",

    60066: "Tira fuori le vere doti dell'equipaggiamento (usa e getta).",
    60652: "Spara in aria palle di polvere. Si può usare più volte.",
    # kiseru, pipa, hamaki e sigaretta sono una firma sola
    60917: "Un attrezzo per fumare. Si usa (usa e getta).",

    # ⚠️ il giapponese dice 使い捨て e l'inglese «(Reusable)»: il sorgente dà
    #    ragione al giapponese — `action.hsp:10130` fa `inv(INV_ITEM_NUM, ci)--`
    62023: "Un'arma nucleare tattica. Si usa (usa e getta).",
    62099: "Incendia tutto intorno al bersaglio. Si può usare più volte.",
    62175: "Abbassa per un po' il PV del bersaglio. Si usa più volte.",
    62237: "Il compagno che la porta non riesce più ad alzarsi presto.",
    62603: "Una scatola per il primo soccorso. Si usa (usa e getta).",
    62669: "Una cassa che ricarica le munizioni speciali (usa e getta).",

    63524: "Dopo un po' esplode e devasta un'area vasta (usa e getta).",
    # i cinque nuclei di transizione (alfa, beta, gamma, delta, omega) sono una firma
    63940: "Dà un altro aspetto e altra forza. Si usa con la barra al 50%.",

    64556: "Apre una tasca quadridimensionale. Si può usare più volte.",
    64681: "Usandolo, mangiano tutti i compagni (usa e getta).",
    64744: "Contiene fino a 15 bare della negromanzia. Si può usare sempre.",
    64810: "Dà la parte del corpo che si vuole. Si usa (usa e getta).",

    65198: "Un guanto da duello: si lancia all'avversario (usa e getta).",
    65467: "Una lente che mostra i dati del bersaglio. Si usa (usa e getta).",
    66078: "Una pietra che dice la fede. Si può usare sempre.",
    67669: "Suona il brano che si vuole. Si può usare sempre.",
    68590: "Serve a fumare crimberry essiccate. Si usa (usa e getta).",
    68786: "Serve nella sala d'esposizione. Si usa (usa e getta).",
    69457: "Concime per le colture. Si usa (usa e getta).",

    70336: "Un attrezzo da cucina limitato. Si usa (usa e getta).",
    70601: "Sveglia il mostro che dorme nella bara. Si usa ogni tanto.",
    70820: "Duplica il bersaglio e lo mette nel gruppo. Si usa (usa e getta).",
    71927: "Una bambola alta una decina di centimetri. Si usa (usa e getta).",

    72487: "Un articolo che cambia la classe. Si usa (usa e getta).",
    72553: "Un oggetto che cambia la razza. Si usa (usa e getta).",
    72623: "Un fischietto a frequenza speciale. Si può usare ogni tanto.",
    73023: "Una gemma che serba poteri speciali. Si usa (usa e getta).",
    73291: "Alterna ordini d'attacco e di difesa. Si può usare sempre.",
    73701: "Una statua del dio degli elementi. Si usa ogni tanto.",
    73768: "Una statua della dea della ricchezza. Si usa ogni tanto.",
    73831: "Tira fuori l'effetto delle carte (non attivo). Si usa sempre.",

    76317: "Danno a tutti i nemici, secondo il Tiro. Si usa ogni tanto.",
    77776: "Una volta al mese arriva la paghetta. Si usa ogni tanto.",
    # il calderone dell'alchimista e il vaso della fusione sono una firma sola
    78259: "Un attrezzo per le fusioni complesse. Si può usare sempre.",
    79114: "Una statua del dio delle macchine. Si usa ogni tanto.",
    79181: "Una statua del dio del raccolto. Si usa ogni tanto.",

    # ☆ non si scrive: marca la qualità 4 e 5, «eccezionale» e «celestiale»
    80221: "Rende eccezionale un'arma o un'armatura. Si usa (usa e getta).",
    80927: "Serve nella sala d'esposizione. Si può usare sempre.",
    80995: "Serve nella sala d'esposizione. Si può usare sempre.",

    81133: "Vieta ai compagni di raccogliere roba. Si può usare sempre.",
    81199: "Analizza l'animo del bersaglio. Si può usare sempre.",
    82007: "Ci si appende un mostro indebolito. Si può usare sempre.",
    82812: "Una statua della dea della fortuna. Si usa ogni tanto.",

    83081: "Una gemma che, usata, cambierà qualcosa più avanti.",
    83212: "Una gemma che dà un talento nuovo (usa e getta).",
    84038: "Manda un suono acuto tutt'intorno. Si può usare sempre.",
    84166: "Una scatola per le carte. Si può usare sempre.",
    84299: "Colpisce e cattura la <Little Sister>. Si può lanciare.",
    # la ghigliottina e la vergine di ferro sono una firma sola
    84970: "Un mobile orribile a vedersi. Meglio non toccarlo.",

    85171: "Una statua della dea della guarigione. Si usa ogni tanto.",
    85237: "Colpisce e cattura un mostro. Si può lanciare.",
    85301: "Cancella un compagno e dà le sue doti a un altro. Si usa sempre.",
    85370: "Ricompone la materia e la muta in altro. Si usa ogni tanto.",
    85437: "Accelera la crescita delle colture. Si usa ogni tanto.",
    85506: "Cura gli HP dei compagni intorno. Si usa ogni tanto.",
    85575: "Alza la velocità per un po'. Si può usare ogni tanto.",

    86203: "Dopo un po' esplode e devasta un'area vasta (usa e getta).",
    86536: "Una statua della dea del vento. Si usa ogni tanto.",
    86603: "Una statua del dio della terra. Si usa ogni tanto.",

    88024: "Un letto semplice (rango 4). Si può usare sempre.",
    88213: "Abbassa la Follia tua e dei compagni intorno (usa e getta).",
    88413: "Basta averlo addosso: lo scasso riesce molto più spesso.",
    88475: "Serve per lo scasso. Certe volte si rompe.",
    88541: "Una bomba che dilania chi la calpesta. Si usa (usa e getta).",
    88607: "Lega un compagno perché non si allontani. Si usa sempre.",
    88872: "Rifà l'oggetto nel materiale scelto (usa e getta).",
    88940: "Azzera l'ostilità di chi non è un mostro. Si usa più volte.",

    90140: "Cambia l'arredo della stanza. Si può usare sempre.",
    91912: "Una luce semplice da tenere in mano. Si può usare sempre.",
    92255: "Ci si mette da parte una somma alla volta. Si usa sempre.",
    92392: "Un disco con dei filmati incisi. Si può usare sempre.",
    92937: "Una coperta che protegge dal gelo, per qualche volta.",
    93001: "Una coperta che protegge dal fuoco, per qualche volta.",
    93361: "Cambia l'incarico. Si può usare sempre.",
    93826: "Un rifugio che si monta in un po' di tempo. Si usa sempre.",
    94604: "Un disco con della musica incisa. Si può usare sempre.",

    99094: "Mostra gli HP dei compagni. Si può usare sempre.",
    102461: "Un letto semplice (rango 0). Si può usare sempre.",
    104794: "Serve a lavorare le gemme. Si può usare sempre.",
    108460: "Serve a pescare. Si può usare sempre.",

    114080: "Ci si cucinano i piatti fino al rango 5.",
    114144: "Ci si cucina fino al rango 3. Illumina sempre intorno.",
    116349: "Ci si cucinano i piatti fino al rango 4.",
    116606: "Si può usare sempre.",

    120508: "Serve per i lavori di falegnameria. Si può usare sempre.",
    120574: "Serve a cucire. Si può usare sempre.",
    121832: "Serve a dipingere. Non si può usare.",
    122682: "Serve per l'alchimia. Si può usare sempre.",
}
