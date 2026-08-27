# -*- coding: utf-8 -*-
"""Le rese del lotto 005 (il MOBILIO), indicizzate per RIGA e nient'altro.

`_monta005.py` prende questo file e `chiavi005.txt` e ne fa `rese005.py`,
copiando l'inglese verbatim dal template.

Le formule ricorrenti, oltre alle quattro code del lotto 004:

    座る為の家具。       ->  Un mobile per sedersi.        (7 firme)
    眠る為の家具（ランクN）->  Un letto (rango N).
    演奏用の道具。       ->  Uno strumento per suonare.    (4 firme)
    観賞用の鉢植えだ。   ->  Una pianta ornamentale in vaso.
    とても重い建造物だ。 ->  Una costruzione molto pesante. (7 firme, le tombe)
    使用することはできない -> Non si può usare.
    装備することはできない -> Non si può equipaggiare.
    本類を100種類まで…   ->  Ci stanno fino a 100 tipi di libri.

E la scala della LUCE, che il giapponese grada in cinque scalini e che qui
diventa un nome con un aggettivo, cosi' l'ordine si legge:

    常に周囲を照らす。          ->  Illumina sempre intorno.        (già 108a/109a)
    常に周囲を明るく照らす。    ->  Illumina sempre di luce viva.
    夜間、周囲を弱く照らす。    ->  Di notte fa una luce fioca.
    夜間、周囲をやや弱く照らす。->  Di notte fa una luce un po' fioca.
    夜間、周囲をやや明るく照らす->  Di notte fa una luce abbastanza viva.
    夜間、周囲を明るく照らす。  ->  Di notte fa una luce viva.
"""

IT = {
    55676: "Una bambola di porcellana: usandola diventa una compagna.",
    55738: "Una ceramica magnifica.",
    55800: "Una ceramica bizzarra.",

    # --- i quattro simulacri divini che si usano da sé stando addosso
    57449: "Un pendolo del dio della terra. Si usa da sé se lo porti.",
    57511: "Un peluche del dio del raccolto. Fa effetto se sta nel campo.",
    57710: "Un busto del dio degli elementi. Si usa da sé se lo porti.",
    57772: "Un dipinto della dea della fortuna. Fa effetto se sta in casa.",
    57834: "Una sveglia del dio delle macchine. Si usa da sé se lo porti.",

    60000: "Una pianta ornamentale.",
    63872: "Un mobile che fa succo di frutta, verdura e frutti a guscio.",
    65334: "Un letto (rango 5). Chi lo tiene a volte viene a dormirti accanto.",
    66388: "Una statua misteriosa.",
    66454: "Un golem non attivato: usandolo diventa un compagno.",

    # ⚠️ il giapponese di questa riga e' copiato da `:87005` e dice «paravento»,
    #    ma la SUA riga di categoria dice ＜彫像＞ e l'inglese «statua». Il
    #    giapponese si contraddice da solo, e a decidere e' la sua categoria.
    66516: "Una statua austera.",

    66578: "Una statua solenne.",
    66706: "Una casetta per i piccoli animali.",

    # --- i quattro strumenti musicali: un giapponese, quattro ranghi inglesi
    68851: "Uno strumento per suonare. Si può usare sempre.",
    68916: "Uno strumento per suonare. Si può usare sempre.",
    68981: "Uno strumento per suonare. Si può usare sempre.",
    74571: "Uno strumento per suonare. Si può usare sempre.",

    70130: "Una miniatura di una nave magica.",
    72825: "Una statua a forma di koma-inu.",
    73355: "Si può usare sempre al posto di una sedia.",
    76523: "Un bel castello fatto di sabbia.",
    78792: "Un recipiente piatto su cui si posa il cibo.",
    78922: "Un mobile ricavato da una bestia.",

    # --- le sette sedute: un giapponese, sette inglesi
    79047: "Un mobile per sedersi. Si può usare sempre.",
    87710: "Un mobile per sedersi. Si può usare sempre.",
    90640: "Un mobile per sedersi. Si può usare sempre.",
    108957: "Un mobile per sedersi. Si può usare sempre.",
    124374: "Un mobile per sedersi. Si può usare sempre.",
    124437: "Un mobile per sedersi. Si può usare sempre.",
    125939: "Un mobile per sedersi. Si può usare sempre.",

    79306: "Un armadietto costoso.",
    79369: "Una libreria grande. Ci stanno fino a 100 tipi di libri.",
    79639: "Un piccolo abete.",
    79701: "Un ornamento solenne fatto per il capodanno.",
    79767: "Un cuscino da bei sogni (rango 0). Si può usare sempre.",
    79829: "Un negozietto per le feste.",
    79953: "Un tavolo da negozio.",
    80015: "Una piattaforma rialzata.",
    80085: "Una corona fatta per un giorno speciale.",
    80152: "Uno strumento che inebria il pubblico. Si può usare sempre.",
    80615: "Una bambola dalla forma unica.",
    80677: "Un tavolo per la stagione fredda. Ci si può infilare sotto.",
    80801: "Gradini di pietra per scendere. Ci si può passare.",
    80863: "Gradini di pietra per salire. Ci si può passare.",
    82278: "Dato a qualcuno, alza la simpatia.",
    82878: "Un letto eccellente (rango 9). Si può usare sempre.",
    83767: "Suonandolo si prendono mance migliori. Si può usare sempre.",
    84647: "Un pannello che divide lo spazio.",
    87005: "Un paravento in stile orientale.",
    87067: "Un lume semplice straniero. Di notte fa una luce fioca.",
    87129: "Una finestra tonda. Di notte fa una luce fioca.",
    87191: "Un lume straniero e pesante. Illumina sempre intorno.",
    87322: "Un letto (rango 7). Si può usare sempre.",
    87384: "Non serve a niente in particolare.",
    87446: "Un grande lavello. Non si può usare.",
    87508: "Una credenza fatta da un maestro artigiano.",
    87647: "Un'aiuola con una recinzione.",
    87772: "Una tavola su cui scrivere e cancellare. Non si può usare.",
    87834: "Una tavola con scritto il menù.",
    87896: "Una cassettiera da re.",
    87958: "Una finestra con un divisorio. Di notte fa una luce fioca.",
    88086: "Un sacco pieno di granaglie.",
    88806: "Un cancello per la sala d'esposizione (usa e getta).",
    89215: "Un portale che accoglie le divinità straniere.",
    89949: "Una costruzione a semicerchio ornata di fiori.",
    90015: "Un letto da re, eccellente (rango 8). Si può usare.",
    # ⚠️ la testa e' identica a quella di `:91091`, che col suo scalino di luce
    #    piu' lungo arrivava a 68 su 69: si stringe QUI, cosi' le due restano
    #    uguali fra loro come lo sono i due giapponesi
    90077: "Fa entrare la luce da fuori. Di notte fa una luce fioca.",
    90202: "Un albero potato ad angolo.",
    90388: "Una pianta ornamentale in vaso.",
    110093: "Una pianta ornamentale in vaso.",

    # --- i sei fornelli, uno per rango: la formula e' quella del lotto 004
    90452: "Ci si cucinano i piatti fino al rango 9.",
    110736: "Ci si cucinano i piatti fino al rango 8.",
    120886: "Ci si cucinano i piatti fino al rango 6.",
    123745: "Ci si cucinano i piatti fino al rango 7.",

    91091: "Fa entrare la luce da fuori. Di notte fa una luce un po' fioca.",
    91153: "Una colonna pesante.",
    91215: "Una grande croce splendente.",
    91277: "Un lume fisso. Di notte fa una luce viva.",
    91339: "Un recipiente per liquidi, coperto di neve. Non si può usare.",
    91401: "Un pupazzo di neve piccolo.",
    91783: "Un lume d'artista famoso. Di notte fa una luce viva.",
    91845: "Un lume semplice di cera. Illumina sempre intorno.",
    92127: "Uno scaffale comune.",
    94804: "Una statua fatta di neve.",
    94866: "Un enorme minerale nero.",
    94928: "Una colonna a forma di gatto.",
    94990: "C'è dipinta una pianta.",
    95052: "C'è dipinto un paesaggio.",
    95114: "C'è dipinta una donna.",
    95177: "Un tavolo molto grande. Si può usare sempre.",
    95301: "Un forno per cuocere. Non si può usare.",
    95363: "Un mobile che scalda la stanza.",
    95425: "Una costruzione che scalda il metallo.",
    97876: "Un disco senza dati dentro. Non si può usare.",
    97946: "Un frammento di informazioni.",
    98008: "Una scatola dove buttare le lattine.",
    98078: "Una scatola dove mettere qualcosa.",
    98148: "Una scatola dove mettere informazioni.",
    98218: "Un attrezzo da cucina rotto. Non si può usare.",
    98288: "Uno strumento che ritrae un soggetto. Non si può usare.",
    98359: "Allena gli attributi base. Si può usare sempre.",
    98429: "Un cervello antico.",
    98499: "Lampeggia a caso e fa uno strano rumore a intervalli.",
    103363: "Una macchina che sputa sfere del tesoro. Si può usare sempre.",
    108396: "Serve ad andare nella sala d'esposizione (usa e getta).",
    108832: "Una statua molto vistosa.",
    108894: "Un piedistallo per candele. Di notte fa una luce viva.",
    109086: "Un piano con le gambe per lavorarci. Si può usare sempre.",
    109148: "Un abito dai colori vivaci. Non si può equipaggiare.",
    109273: "Una costruzione simbolica.",
    109401: "Una sedia larga. Si può usare sempre.",
    109463: "Uno scaffale lineare.",

    # --- i letti, uno per rango (il cuscino di Jure, rango 0, sta piu' su:
    #     il suo giapponese dice 枕 e non 家具, quindi e' una formula sua)
    109529: "Un letto (rango 4). Si può usare sempre.",
    110672: "Un letto (rango 4). Si può usare sempre.",
    109906: "Un letto (rango 0). Si può usare sempre.",
    110868: "Un letto (rango 1). Si può usare sempre.",
    125751: "Un letto (rango 1). Si può usare sempre.",
    110934: "Un letto (rango 3). Si può usare sempre.",
    111327: "Un letto (rango 6). Si può usare sempre.",
    119690: "Un letto (rango 2). Si può usare sempre.",

    109591: "Un piccolo altare. Non si può usare.",
    109653: "Una credenza piuttosto grande.",
    109716: "Uno specchio per guardarsi. Si può usare sempre.",
    110544: "Uno specchio per guardarsi. Si può usare sempre.",
    109778: "Uno scaffale pulito e ordinato.",
    109840: "Un tavolo sbilenco.",
    109969: "Una libreria vecchia. Ci stanno fino a 100 tipi di libri.",
    110031: "Uno scaffale pieno di polvere.",
    110158: "Un tavolo da gioco a lanci. Si può usare sempre.",
    110223: "Un tavolo da gioco a numeri. Si può usare sempre.",
    110288: "Un tavolo con giochi di ogni tipo. Si può usare sempre.",
    110353: "Un tavolo da gioco a pallini. Si può usare sempre.",
    110415: "Un mobile pieno d'acqua. Non si può usare.",
    110606: "Uno scaffale spartano.",
    110996: "Una cassettiera per i vestiti.",
    111128: "Un armadietto che tiene molta roba.",
    111191: "Uno specchio costoso per guardarsi. Si può usare sempre.",
    111261: "Un vaso fatto di buon materiale.",
    111389: "Un armadietto per i liquori.",
    111452: "Un tavolo storto. Si può usare sempre.",
    111514: "Un tessuto fatto di cotone.",
    111576: "Uno scaffale con sopra dei soprammobili.",
    111638: "Uno scaffale con sopra roba di tutti i giorni.",
    111700: "Un'armatura in ordine. Non si può equipaggiare.",
    112323: "Una mappa suggestiva. Non si può usare.",
    112385: "Uno strumento di salvataggio.",
    112448: "Un tavolo sobrio.",
    112510: "Una tinozza d'acqua, pesantissima.",
    112634: "Una colonna spezzata. È pesantissima.",
    112696: "Una colonna lunga e grossa. È pesantissima.",
    115323: "La riproduzione di una spada.",
    115385: "La riproduzione di un berserker.",
    118646: "Piatti impilati.",

    # --- le sette tombe: un giapponese, sette inglesi che raccontano ognuno
    #     una storia diversa (Norland, Eulderna, un eroe, il nome ancora
    #     leggibile). Il giapponese dice solo che pesano.
    119946: "Una costruzione molto pesante.",
    120008: "Una costruzione molto pesante.",
    120070: "Una costruzione molto pesante.",
    120132: "Una costruzione molto pesante.",
    120194: "Una costruzione molto pesante.",
    120256: "Una costruzione molto pesante.",
    120318: "Una costruzione molto pesante.",

    120380: "Fili tessuti insieme. Non si può usare.",
    120442: "Vestiti sparsi. Non si può usare.",
    120636: "Uno scaffale semplice.",
    120698: "Un candelabro lavorato con arte. Di notte fa una luce viva.",
    120760: "Un tavolo da nobili.",
    120822: "Un tavolo stretto fatto per mangiare.",
    121076: "Liquore andato a male, e in quantità. Non si può usare.",
    121139: "Una libreria da maestro. Ci stanno fino a 100 tipi di libri.",
    121201: "Una cassettiera fatta da un maestro.",
    121263: "Libri impilati. Non si può usare.",
    121325: "Libri sparsi. Non si può usare.",
    121387: "Una statua in armatura completa. Non si può equipaggiare.",
    121449: "Un'armatura da esposizione. Non si può equipaggiare.",
    121511: "Un abito da esposizione. Non si può equipaggiare.",
    121573: "Armi legate in fascio. Non si può equipaggiare.",
    121635: "Archi impilati. Non si può equipaggiare.",
    # ⚠️ l'inglese di questa riga e di `:124249` finisce con uno SPAZIO, che e'
    #    la giuntura col pezzo che segue: la resa deve tenerlo, e `reimporta`
    #    rifiuta l'intero lotto se non c'e'
    121770: "Una mappa del continente. Si può leggere. ",
    121894: "Una colonna con sopra dei fiori.",
    121956: "Una colonna con sopra delle piante.",
    122616: "Un cerchio disegnato per terra.",
    122744: "Una bottiglia speciale per i liquidi. Non si può usare.",
    122887: "Uno scaffale per il pane. Ci stanno fino a 20 tipi di pane.",
    123557: "Una tavola con delle informazioni. Non si può leggere.",
    123619: "Una tavola che indica una direzione ignota.",
    123681: "Una tavola che fa da segnale.",
    123807: "Un forno col metallo incandescente. Illumina sempre di luce viva.",
    123869: "Un ripiano con sopra dei vestiti. Non si può usare.",
    124001: "Un ripiano con sopra delle cianfrusaglie. Non si può usare.",
    124063: "Un ripiano con sopra degli attrezzi. Non si può usare.",
    124125: "Uno scaffale per riporre le cose.",
    124187: "Uno scaffale con un reggilibri.",
    124249: "Un mobile dove stipare le cose. Non si può usare. ",
    124311: "Uno scaffale per riporre le stoviglie.",
    124500: "Uno scaffale per le pozioni. Ci stanno fino a 60 tipi.",
    124563: "Un tavolo fatto per studiare. Si può usare sempre.",
    124625: "Un vaso con la bocca aperta. Non si può usare.",
    124687: "Un vaso con la bocca chiusa. Non si può usare.",
    124749: "Un banco per raffinare i metalli.",
    124811: "Una bella armatura. Non si può equipaggiare.",
    124873: "Un lume facile da portare. Di notte fa una luce abbastanza viva.",
    124935: "Uno strumento da scavo. Non si può usare.",
    124998: "Una sedia lavorata con arte. Si può usare sempre.",
    125060: "Un recipiente per i liquidi. Non si può usare.",
    125122: "Un tavolo da osteria.",
    125249: "Uno strumento enorme e pesantissimo. Si può usare sempre.",
    125311: "Un ripiano con esposti dei soprammobili.",
    125373: "Un ripiano con esposte delle cianfrusaglie.",
    125435: "Un ripiano con esposte delle armature.",
    125497: "Un tavolo fatto per mangiare.",
    125560: "Un tavolo all'ultima moda. Si può usare sempre.",
    125622: "Un gioco per bambini.",
    125685: "Una bambola morbidissima. Si può usare sempre.",
    125813: "Una cassettiera di buon materiale.",
    125876: "Una libreria comune. Ci stanno fino a 100 tipi di libri.",
    127610: "Una lastra di pietra con delle scritte.",
}
