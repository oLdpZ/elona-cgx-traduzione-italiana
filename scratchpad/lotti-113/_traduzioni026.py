# -*- coding: utf-8 -*-
"""Le rese del lotto 026 — IL PRIMO LOTTO DI PROSA DEL CORPO, per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 026 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa026.py`. Lo scheletro lo fa
`lotti-113/_corpo.py`, che unisce i tre indici del corpo sulle stesse righe.

⚠️⚠️ **OGNI RESA FINISCE CON `\\n#<titolo>`**, e quel backslash e' un carattere
vero: e' l'a capo che il gioco usa per staccare la riga-fonte. La coda non si
sceglie a mano — la da' `lotti-113/_code.py`, che passa dal giapponese alla
tabella della 112a. ⚠️ Dove l'inglese scrive `# ~`, con lo spazio, lo spazio
resta; dove scrive `#~`, no.

⚠️ **Gli accenti si scrivono VERI** (`perché`, `più`, `è`): la degradazione ad
apostrofo la fa `applica.py`, e scriverli a mano `perche'` e' un errore che
`verifica.py` segnala. La prima stesura di questo file li aveva sbagliati tutti.
"""

IT = {
    # === LE CONCHIGLIE ====================================================
    42782: "Un mollusco dal sapore cremoso e dalla polpa soda. Sarebbe un bivalve, ma si apre apposta per godersi le reazioni di chi passa. Fra i mesugaki capita spesso l'esemplare nocivo, e a chi ci finisce contro toccano giorni interi di dignità calpestata. Quelli a cui la lezione è stata insegnata bene sono sicuri; quelli lasciati a metà, ancora sfrontati, sono pericolosi. Molti hanno conosciuto l'inferno perdendo contro un mesugaki, eppure continuano a sfidarli affidandosi alla sorte. \\n#~Il Cibo Mutevole di Tyris~",
    42783: "\\\"Mangio il mesugaki / e mi brontola il ventre / mentre vado al lavoro\\\"\\n# ~Il Gemito dello Sconfitto~",
    42784: "\\\"È un essere infame, mi diffama! Sto valutando le vie legali\\\"\\n# ~Parole del Calamaro Provocatore con gli Occhi Lucidi~",

    44656: "Una grossa chiocciola di mare. La riconosci dalle spine e dalla conchiglia a spirale, che pare la punta di un trapano. La si mangia cruda a fettine, ma in certe regioni la si arrostisce così com'è, nel guscio.\\n#~Il Cibo Mutevole di Tyris~",
    44658: "Un cibo di mare che sazia, e che entra in molte ricette.\\n#~Rapporto di Identificazione: categoria <Cibo>~",

    44728: "Un bivalve dal sapore pieno e intenso. Un tempo era più piccolo, ma pare che il cambiamento dell'ambiente lo stia facendo crescere a poco a poco. È famoso perché le sue due valve combaciano solo se vengono dallo stesso animale.\\n#~Il Cibo Mutevole di Tyris~",
    44730: "Un cibo di mare che sazia, e che ovviamente si può arrostire sul set da barbecue.\\n#~Rapporto di Identificazione: categoria <Cibo>~",

    44800: "Un grosso bivalve. Il muscolo, spesso e carnoso, è tutto sapore. Le due valve hanno colori diversi: di solito vive sul fondale con quella rosso-bruna in alto e quella bianca in basso.\\n#~Il Cibo Mutevole di Tyris~",

    # === LE PIANTE D'ACQUA E I PESCI ======================================
    52108: "Una pianta che si era adattata alla vita sulla terraferma e poi è tornata a vivere sott'acqua. Si usa molto per ornamento, ma non è che non si possa mangiare.\\n#~Il Cibo Mutevole di Tyris~",
    52110: "Una verdura che sazia, e che entra in molte ricette.\\n#~Rapporto di Identificazione: categoria <Cibo>~",

    52243: "Un pesciolino dalla faccia buffa. Sta quasi sempre mezzo sepolto nel fondale e mangia solo quel che gli passa davanti: per questo non abbocca mai, e anche tirato fuori dall'acqua cerca subito un posto dove infilarsi. Il nome che porta viene da una razza di cane dal muso somigliante. A strapparla fuori dalla tana, è lunga più di quanto ci si aspetti.\\n#~Il Cibo Mutevole di Tyris~",

    # === LE DUE ERBE GEMELLE, che il giapponese distingue riga per riga ===
    54948: "Un'erba che cresce spontanea in tutta la Tyris del Nord di Aimwell. Si riproduce in fretta, e pare che a un certo punto spuntasse perfino in mezzo alle città. Dalle foglie esce un succo dolce che si usa come dolcificante, e la radice, grossa e lunga, è buona da mangiare.\\n#~Il Cibo Mutevole di Tyris~",
    55011: "Un'erba che cresce spontanea in tutta la Tyris del Nord di Aimwell. A prima vista somiglia in tutto alla fane, ma ha le foglie spinose e la radice sottile, dall'odore pungente. Tolte le spine, le foglie sono buone più di quanto si creda, e la radice serve a preparare medicine.\\n#~Il Cibo Mutevole di Tyris~",

    55074: "La cura della corruzione, fatta rapprendere in un solido. Si conserva più a lungo, ma alterandosi ha perso efficacia. In generale non la si considera nemmeno una cura della corruzione.\\n#~Il Cibo Mutevole di Tyris~",

    # === LE DUE GOMME =====================================================
    55544: "Una gomma che ha perso ogni sapore. A ingannare la fame serve ancora, ma è dura e non sa di niente. Meglio buttarla, però non per terra.\\n#~Il Cibo Mutevole di Tyris~",
    55607: "Una resina detta base per gomme, con l'aggiunta di dolcificanti e aromi. Dà gusto e piacere alla bocca. Non nutre e non riempie la pancia, ma masticandola a lungo la fame si inganna. Certi teppisti la masticano rumorosamente e ne fanno una specie di minaccia.\\n#~Il Cibo Mutevole di Tyris~",

    56400: "Esca da gettare ai pesci in acqua. Mangiarla si può, ma sa di pesce marcio ed è cattiva. Per i pesci invece è nutrientissima: le squame si fanno belle e le carni sode. Siccome ne migliora la qualità, conviene darla ai pesci che si allevano. Sui pesci mostruosi pare non avere alcun effetto, e da dove venga la differenza resta un mistero.\\n#~Il Cibo Mutevole di Tyris~",

    56871: "Un piatto ricostruito a partire da testi antichi. È parente del panino imbottito, ma sembra puntare tutto sulla carne. È enorme, pesante e scomodo da mangiare, e molti studiosi dubitano che questa fosse davvero la misura normale.\\n#~Il Cibo Mutevole di Tyris~",

    # === I DUE PIATTI DI MOCHI, che l'inglese confonde ====================
    56934: "Un dolce che ha il mochi per ingrediente. Nacque per smaltire i kagami mochi ormai duri e secchi, buttandoli in un brodo di fagioli azuki. C'è però chi sostiene che al posto del mochi vadano messi gnocchetti o castagne, ed è saltato fuori anche un piatto somigliante chiamato zenzai: negli ambienti accademici se ne discute ancora.\\n#~Il Cibo Mutevole di Tyris~",
    56997: "Una zuppa che ha il mochi per ingrediente. Nacque per smaltire i kagami mochi ormai duri e secchi, mettendoli in un brodo. All'inizio la chiamavano brodo di mochi; poi in certi testi antichi si trovò un piatto somigliante, e da allora ne porta il nome. I dettagli però cambiano da un documento all'altro, e nemmeno gli esperti sanno fin dove i due piatti coincidano.\\n#~Il Cibo Mutevole di Tyris~",

    # === I TRE ESSICCATI, e i due dei che non gradiscono ==================
    57188: "Pesce messo in salamoia e poi seccato al sole perché non si guasti: così si trasporta meglio e dura di più. Arrostito profuma moltissimo. Chissà perché, alla dea della fortuna non fa piacere.\\n#~Il Cibo Mutevole di Tyris~",
    57251: "Verdura seccata al sole perché non si guasti: così si trasporta meglio e dura di più. Persa l'acqua, il dolce e il sapore si concentrano. Chissà perché, al dio del raccolto non fa piacere.\\n#~Il Cibo Mutevole di Tyris~",
    57314: "Frutta candita nello zucchero o seccata al sole perché non si guasti: persa l'acqua, si trasporta meglio e dura di più. Anche la buccia, che cruda è scomoda da mangiare, diventa facile. C'è chi non sopporta quel dolce così particolare.\\n#~Il Cibo Mutevole di Tyris~",

    # === LA SOIA E I SUOI TRE FIGLI =======================================
    58589: "Un alimento ricavato dalla soia: fette sottili di tofu fritte. Fin dall'antichità remota è il cibo preferito delle volpi, e per molto tempo nessuno seppe perché; si diceva che facesse le veci della carne di topo. Ricerche recenti hanno mostrato che dentro quella pasta spugnosa c'è materia magica, e che le volpi la fiutano d'istinto.\\n#~Il Cibo Mutevole di Tyris~",
    58652: "Un alimento ricavato dalla soia, fatto fermentare con il bacillo del natto. È di una viscosità tremenda, e mangiarlo con garbo richiede pratica. Oltre a filare ha un odore tutto suo, e a rovesciarlo addosso a qualcuno ci si prende una sfuriata.\\n#~Il Cibo Mutevole di Tyris~",
    58715: "Un alimento ricavato dalla soia, ottenuto rassodandone il latte. Aiuta a farsi un corpo sano e, se lo si tira, lo spigolo si conficca nella testa dell'avversario. È di quelli già conditi: non serve versarci sopra la salsa di soia.\\n#~Il Cibo Mutevole di Tyris~",
    58778: "L'unica pianta che contenga tanta proteina quanta la carne: per questo la chiamano la carne dei campi. Buona da mangiare, buona da tirare. Dicono che serva anche a scacciare i demoni.\\n#~Il Cibo Mutevole di Tyris~",

    # === I TRE LATTICINI ==================================================
    59125: "Un alimento ricavato dal latte: se ne estrae la parte solida e la si fa rapprendere. Si conserva a lungo, e lo si produce soprattutto dove l'allevamento da latte è fiorente.\\n#~Il Cibo Mutevole di Tyris~",
    59188: "Un alimento ricavato dal latte: il grasso separato e fatto rapprendere. A temperatura ambiente si spappola. È in pratica un blocco di unto e prende fuoco con niente, quindi meglio badarci quando lo si rovescia addosso a qualcuno.\\n#~Il Cibo Mutevole di Tyris~",
    59251: "Un alimento ricavato dal latte, fatto fermentare con fermenti particolari che tengono a bada i germi più deboli: per questo, contro ogni apparenza, si conserva bene. Aiuta a farsi un corpo sano, ma a rovesciarlo addosso a qualcuno ci si prende una sfuriata.\\n#~Il Cibo Mutevole di Tyris~",

    59314: "Alimenti e altro tritati fino a ridurli in granuli. Le calorie sono concentrate: sazia poco e fa ingrassare molto, ed è fatto apposta. Al gusto e alla consistenza però non ha pensato nessuno. Si può dare anche al bestiame affamato. \\n# ~Vivere Insieme al Bestiame~",

    # === LE DUE BEVANDE ===================================================
    60258: "Foglie appena colte. A seconda di come le si fa fermentare cambiano colore e profumo. In tutto il mondo sono preziose come materia prima del tè. Mangiarle così come sono si può, volendo... \\n# ~Bevande da Bere e Bevande da Non Bere~",
    60321: "La materia prima del caffè. In origine, pare, senza cottura non avveniva nessuna trasformazione chimica e non ne uscivano né aroma né sapore decenti. Le varietà coltivate oggi però sono tutte migliorate, e la trasformazione comincia già alla raccolta: tostarle non serve più. \\n# ~Bevande da Bere e Bevande da Non Bere~",

    # === I DUE CEREALI ====================================================
    60384: "Di suo è un cereale da terreni umidi, ma è stato reso resistente alla siccità e cresce bene anche lasciato in un campo qualunque. Anzi, dargli troppa acqua non fa che aumentare la fatica e la difficoltà della coltivazione.\\n#~Il Cibo Mutevole di Tyris~",
    60447: "Un cereale che, per selezione, unisce le qualità del frumento e dell'orzo. L'80% della farina che oggi circola non viene dal frumento puro, ma da lui.\\n#~Il Cibo Mutevole di Tyris~",

    # === I DUE CONDIMENTI =================================================
    60514: "Uno dei condimenti di base, di quelli che decidono se un piatto riesce o no. Un liquido rosso-bruno dall'odore inconfondibile. Sotto il salato ha un sapore pieno e dolce.\\n#~Il Cibo Mutevole di Tyris~",
    60581: "Uno dei condimenti che decidono se un piatto riesce o no, e la spezia per eccellenza. Un tempo era preziosa per conservare a lungo il cibo, e c'è stata un'epoca in cui si vendeva a caro prezzo. Sta bene con la carne.\\n#~Il Cibo Mutevole di Tyris~",

    60712: "Quel che resta di una creatura alata al servizio del Re in Giallo. Per il suo signore faceva il corriere, suonava, produceva idromele... amava servire più di ogni altra cosa, e non contenta si è fatta carne secca da accompagnare al bere. Va benissimo con l'alcol.\\n#~Il Cibo Mutevole di Tyris~",

    # === LA ZUPPA E LA BAMBINA ============================================
    61373: "Una zuppa fatta con i funghi misteriosi che una bambina, svegliandosi da un sogno a occhi aperti, si ritrovò in mano senza sapere come. Il dosaggio è perfetto: a mangiarla il corpo si fa più grande o più piccolo. Ha un colore strano, ma il sapore non è male. Si dice che chi continua a mangiarne finisca per avvicinarsi alla corporatura di quella bambina.\\n#~Il Cibo Mutevole di Tyris~",
    61375: "\\\"A ieri non posso tornare. La me di ieri era un'altra persona\\\" \\n# ~Le Parole nel Sonno di una Bambina~",

    65527: "Una lanterna ricavata svuotando una zucca. Il potere di respingere gli spiriti maligni, quello che la tradizione le attribuisce, non ce l'ha; ma un po' di forza misteriosa dentro ce l'ha davvero. Volendo, si può anche mangiare. \\n# ~Alle Radici degli Antichi Riti~",

    67321: "Un piatto che racchiude il sapore dei molluschi e delle alghe raccolti negli abissi. Di pesce non ce n'è. Per prepararlo, dicono, si ricorre all'alta magia; o forse no.\\n#~Il Cibo Mutevole di Tyris~",

    67729: "Un trifoglio con quattro foglie. Le foglie stanno per speranza, sincerità, amore e fortuna. Lo si può tenere come portafortuna, ma a mangiarlo forse si diventa più felici. \\n# ~Erbe che si Mangiano ed Erbe che Non si Mangiano~",

    # === IL DOLCE CHE PORTA IL NOME DI UN PERSONAGGIO =====================
    67792: "Un dolce che si riconosce dalla forma di fiore. La pasta frolla, sottile e friabile, insieme al profumo tostato della mandorla è una delizia. Per far uscire l'impasto dalla sacca ci vuole una certa mano.\\n#~Il Cibo Mutevole di Tyris~",
    67794: "\\\"...perché guardi me? Il mio nome si scrive in un altro modo\\\" \\n# ~Parole di <Lomias> il messaggero di Vindale~",

    67857: "Un frutto largo e schiacciato come un pomodoro. Maturando diventa dolcissimo. È ricco di vitamine e di sali minerali, e c'è stata un'epoca in cui lo trattavano da panacea: quando il caco si fa rosso, dicevano, il medico si fa pallido.\\n#~Il Cibo Mutevole di Tyris~",
    67859: "Un frutto che sazia, e che entra in molte ricette.\\n#~Rapporto di Identificazione: categoria <Cibo>~",

    # === LE DUE GHIANDE ===================================================
    67920: "Una ghianda leggendaria che brilla d'oro. Non è poi così rara, ma perché nasca non si è ancora capito, e per gli studiosi vale moltissimo: più di un lingotto d'oro vero. Di polpa non ne ha quasi, quindi cucinarla non si può; il sapore in sé non sembra male. Mangiarla resta uno spreco. \\n#~Il Cibo Mutevole di Tyris~",
    67983: "Un frutto dal guscio liscio. Accumula molto amido e se ne produce in quantità, perciò è un cibo importante per chi vive nel bosco. Spesso lo si trova sotterrato ai piedi degli alberi, messo da parte. Crudo è molto allappante, ma cucinato pare venga discreto.\\n#~Il Cibo Mutevole di Tyris~",
    67985: "Un frutto a guscio che sazia, e con cui si fanno dolciumi.\\n#~Rapporto di Identificazione: categoria <Cibo>~",
}
