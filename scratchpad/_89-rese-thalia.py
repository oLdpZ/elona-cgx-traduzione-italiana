# -*- coding: utf-8 -*-
"""89b - THALIA la guardastelle (`chat.hsp:11086`-`:11205`, 28 firme).

La nipote di Dain, l'unica del villaggio che parli con Irma e l'unica che
conosca la tecnica della collina. `CDATA_SEX = 1` (`db_creature.hsp:74168`):
donna, e il suo parlato in prima persona si accorda. Zona chiusa: nessuna delle
28 firme vive fuori.

IL REGISTRO NON SI DECIDE, SI LEGGE (82a). Il repertorio di
`db_creature.hsp:74088`-`:74106` e' gia' reso e detta tutto:
«Quel vecchiaccio...», «Che futuro ha la gente della collina?», «Le usanze sono
una gran seccatura.», «Quanta foga...», «Che nausea.», «Proprio come avevo
giudicato.» — brusca, disillusa, del tu con chiunque.

⭐ E da li' arriva la parola piu' importante del lotto: ジジイ e' **vecchiaccio**,
non «the old man» dell'inglese. La stessa parola in bocca alla stessa persona,
gia' scritta: `:11145`, `:11155`, `:11180`, `:11192`, `:11198`. Il nome neutro
di Dain resta «l'anziano della collina» (il diario), «vecchiaccio» e' come lo
chiama lei.

LESSICO EREDITATO (non deciso qui):
  - «officina»                    text.hsp:2962, il NOME SULLA MAPPA
                                  («Officina Nascosta di Irma e Thalia»)
  - «casa abbandonata ai piedi del monte», «a nord»   text.hsp:11495, il diario
  - «la tecnica tradizionale»     chat.hsp:11689 (Irma, 88a)
  - «vicolo cieco»                chat.hsp:11764 (Irma, 88a) per 八方ふさがり
  - «artefatto», «incantamento»   chat.hsp:11290, :14125
  - «potenza»                     chat.hsp:11290 (Irma): «quella scala di
                                  potenza che dice Thalia» e' PROPRIO il
                                  servizio di `:11090`-`:11121`. Le due
                                  schermate devono dire la stessa parola.
  - «armaiola»                    deciso nel lotto di DAIN (`_89-rese-dain.py`)
  - «erede», «gente di fuori»     idem
  - «villaggio», «capanna»        chat.hsp:11071 (Dain)

LESSICO DECISO QUI (va in glossario):
  - 心の友 / «my precious friend», «my treasured friend»  ->  **anima gemella**.
    E' un VOCATIVO rivolto al giocatore, il quarto bersaglio del divieto di
    genere (77a), e torna tre volte (`:11130`, `:11170`, `:11171`): «amico» si
    accorderebbe tutt'e tre le volte. «anima gemella» e' la scappatoia del nome
    comune femminile (85a) nella sua forma piu' comoda: l'accordo cade su una
    parola nostra, non sul giocatore — «Non sono la tua anima gemella».

DEROGHE DICHIARATE
1. `:11089` - l'inglese scrive «(Pretend you saw nothing)», il giapponese
   「聞かなかったことにする」 = *far finta di non aver sentito*. Ha ragione il
   giapponese — quel che il giocatore ha appena colto e' la canzoncina di
   `:11091` — ma non serve derogare: «(Far finta di niente)» regge tutt'e due.
2. `:11091` - 「猫 イズ フリ～ダ～ム♪」 e' inglese maccheronico dentro il
   giapponese, e l'inglese di monte lo conserva. Si conserva anche in italiano:
   una traduzione «Il gatto e' liberta'» spegnerebbe la battuta. Il `♪` si puo'
   scrivere (sta gia' nella build, `db_creature.hsp:121290`); il `~` no, si
   allungano le vocali.
3. `:11180` - «from the viewpoint of an adventurer»: e' il giocatore, quindi
   niente «avventuriero» (84a). Si usa la forma che il progetto ha gia', «chi
   va all'avventura» (`chat.hsp:1469`).
4. `:11192` - il giapponese dice che il vecchio la vuole armaiola 「名声のため」
   (*per la propria fama*), l'inglese «for the reputation of the village». Si
   segue l'inglese: sta in piedi, e il giapponese non porta niente che serva al
   giocatore.

L'ECO col lotto di IRMA (84a): `:11198` («la tecnica tradizionale») risponde a
`chat.hsp:11689`, dove Irma dice «La tecnica tradizionale che mi ha insegnato
Thalia»; `:11189` («vicolo cieco») risponde a `:11764`, dove Irma dice «Sono in
un vicolo cieco»; `:11094`-`:11121` («potenza») e' il servizio che Irma cita a
`:11290`. Tre righe di Thalia sono la meta' di una frase che il giocatore ha
gia' letto in italiano.
"""

RESE = {

    # --- dopo il finale della missione (IRMA_DAGGER >= 11): il servizio
    11089: "(Far finta di niente)",
    11090: "Valutare un artefatto",
    11091: "Gatto is friiidom♪ Gatto is friiidom♪",
    11094: "Lascia fare a me. Vediamo... di un artefatto ti so dire in numeri la "
           "potenza dell'incantamento che si porta dentro. Quale devo guardare?",
    11121: "\"Mmm... l'incantamento di questo qui sta sui \" + p + \" di potenza.\"",

    # --- il primo incontro alla casa abbandonata (missione conclusa)
    11130: "Ciao. Ti do il benvenuto, anima gemella.",
    11131: "...Questo posto è quel che resta dell'officina di un vecchio che ci "
           "faceva concorrenza. Era strano, ma in fondo buono. Venivo spesso da "
           "lui, di nascosto dal vecchiaccio. Fino a quel giorno...",
    11132: "L'officina l'aveva assalita un mostro, dicevano tutti. Ma io me n'ero "
           "accorta: a un'occhiata distratta sembrava messa a soqquadro alla "
           "rinfusa, e invece erano stati distrutti con cura proprio i pezzi che "
           "valevano. Da lì mi è venuta in mente una cosa terribile... Solo che "
           "prove non ne avevo, e più di tutto non ci volevo credere.",
    11133: "Saranno decenni che non mettevo piede qui. Intanto la lapide e la "
           "capanna Irma le ha tirate su in una notte sola. Lasciare il paese "
           "dove sono nata è dura, ma tornare indietro non posso più. Ho "
           "intenzione di vivere qui con Irma...",

    # --- il congedo dalla Grotta Eremitica
    11141: "\"...\" + cdatan(CDATAN_NAME, CHARA_PLAYER) + \", sono in debito con "
           "te. Esci da questa grotta e va' dritto a nord: ai piedi del monte c'è "
           "una casa abbandonata. La prossima volta vediamoci lì.\"",
    11145: "Com'è andata? Anche quel vecchiaccio scorbutico avrà dovuto "
           "ricredersi un po', no?",
    11154: "Ma che...",
    11155: "Vecchiaccio...! Che rabbia! Non lo sopporto più!",

    # --- dopo aver dato il parere sui pugnali
    11162: "Eh eh eh...",
    11163: "Ma no, alla fine parlare con la gente di fuori è una boccata d'aria. "
           "Mi viene da pensare che un vento nuovo possa cambiare questo "
           "villaggio.",

    # --- il menu dell'amicizia (IMPRESSION >= 150)
    11168: "Un'altra volta",
    11169: "Che cosa devo fare?",
    11170: "Non sono la tua anima gemella",
    11171: "Ehi, anima gemella. Mi daresti una mano con una cosa?",
    11175: "B-beh. Tanto io ho Irma... Sola non ci resto.",
    11179: "Bene... si può contare su di te.",
    11180: "Con i pochi materiali e attrezzi che le sono rimasti ho fatto "
           "preparare a Irma qualche campione. Per me quel che le esce non ha "
           "niente da invidiare a quello che facevamo un tempo. Se in quel "
           "vecchiaccio scorbutico è rimasto un briciolo di orgoglio del "
           "mestiere, gli basterà guardarlo per doverlo ammettere. Ma prima di "
           "portarglielo, dalle un parere tu, con l'occhio di chi va "
           "all'avventura.",

    # --- il menu di sempre
    11187: "Perché non fai l'armaiola?",
    11188: "La forestiera",
    11189: "Questo villaggio è un vicolo cieco. Quando i ragazzini di adesso "
           "saranno grandi non ci sarà più via d'uscita. E anche così, per "
           "l'affezione alla terra, nessuno si deciderà ad andarsene.",
    11192: "Te l'ha messo in bocca il vecchiaccio? Mettiamola così: io lo "
           "detesto. Da sempre fa solo cose meschine... E anche il volermi "
           "armaiola, alla fine è per il buon nome del villaggio. Non ho voglia "
           "di fargli un piacere.",
    11196: "Qui la gente non sopporta che uno di fuori venga a stabilirsi. Quando "
           "Irma ha chiesto di fermarsi è stata la volta peggiore. \\\"Tanto sei "
           "figlia di quelli che secoli fa hanno abbandonato questa collina\\\": "
           "con quella scusa la volevano cacciare, e magari ammazzare. Poi però "
           "ho detto io, che sono la nipote dell'anziano, che le prestavo la "
           "stanza libera, e di colpo si sono zittiti tutti. Adesso in faccia la "
           "trattano bene e alle spalle la sparlano di continuo. Che gente "
           "meschina.",
    11198: "...La tecnica per forgiare le armi di questa collina, dici? Il "
           "vecchiaccio me l'ha ripetuta fino alla nausea da piccola, quindi la "
           "so. Ma a te e a Irma non ho ancora aperto il cuore: prima voglio "
           "capire se siete gente a cui la si possa insegnare.",
}
