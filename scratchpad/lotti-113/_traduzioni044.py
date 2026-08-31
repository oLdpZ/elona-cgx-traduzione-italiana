# -*- coding: utf-8 -*-
"""Le rese del lotto 044 — I CIBI, prima parte: verdura, frutta e piatti.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 044 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa044.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️⚠️ **QUESTO LOTTO E' IL PRIMO DISOMOGENEO, E DI MOLTO.** 24 righe su 39 hanno
lo spazio prima del `\\n` e 15 no; 30 code su 39 sono `#~` senza spazio e 9 sono
`# ~` con lo spazio. Non c'e' una regola: la forma di ogni riga si legge da
`scratchpad/lotti-113/_forma.py 044`, che e' nato qui apposta.
"""

IT = {
    # === LA BACCA E GLI ORTAGGI ===========================================
    68650: "Una bacca piccola che ha proprietà medicinali. A farla fermentare il veleno se ne va e ne viene una birra come si deve. A seccarla, invece, diventa una droga che dà una dipendenza fortissima, e per questo chi la lavora di nascosto non finisce mai. \\n#~Il Cibo Mutevole di Tyris~",
    69527: "Una verdura viola con una lucentezza lucida. La polpa è come una spugna e si beve facilmente l'acqua e l'olio. Ha un sapore delicato e sta bene insieme agli altri ingredienti.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️ l'inglese lascia cadere la frase della barba del mais, che fa venire
    #    da urinare (ちなみにヒゲのような部分には利尿作用がある).
    69598: "Una pianta bella da vedere, coi chicchi gialli allineati per bene. Cruda non va tanto, e il sapore fresco che ha appena colta lo perde subito dopo. Fra l'altro, la parte che pare una barba fa venire da urinare.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️ l'inglese lascia cadere la PRIMA frase: che la patata e' quasi la
    #    stessa specie dell'imo, ma piu' grande e sgraziata.
    69669: "È quasi la stessa specie dell'imo, ma più grande e un po' sgraziata. Bollendola non si sfa, quindi va bene per gli stufati. Buccia e germogli contengono veleno, e se prima di mangiarla non li togli con cura è pericolosa.\\n#~Il Cibo Mutevole di Tyris~",

    69734: "Un frutto che tiene insieme un'acidità fresca e una dolcezza piena. Contiene sostanze che aiutano a disfare la carne, e sa anche renderla tenera. Attento a non mangiarne troppo: disfa anche i tessuti dentro la bocca.\\n#~Il Cibo Mutevole di Tyris~",
    69799: "Un frutto che sotto i denti fa croc. È dolce e pieno di succo, ma come nella mela la parte vicina al torsolo è molto acida. Di base si mangia cruda, e cucinarla è raro.\\n#~Il Cibo Mutevole di Tyris~",
    69864: "Un frutto giallo, lungo e ricurvo. Piace molto come merenda, ma dà molto nutrimento e molto raccolto, e in certi paesi è il cibo principale. Attento: una banana matura, se la lasci lì, si guasta in fretta.\\n#~Il Cibo Mutevole di Tyris~",
    69929: "Un frutto famoso per essere carissimo. Molti contadini puntano a fare fortuna con meloni di gran qualità. Perché sia finito così lontano dall'anguria non si sa.\\n#~Il Cibo Mutevole di Tyris~",

    # ⓘ 長棒 e' il «bastone lungo», che nel gioco e' un'arma vera: il
    #    giapponese fa la battuta apposta.
    69994: "Una verdura parente stretta della zucca... ma per quanto è dolce la trattano da frutto e basta. E ci si può anche giocare a spaccarla con un bastone lungo: un frutto splendido.\\n#~Il Cibo Mutevole di Tyris~",

    # === LA CASTAGNA E IL RICCIO, CORPO E BATTUTA =========================
    # ⓘ la battuta degli alchimisti sta gia' nel dizionario (`chat.hsp`):
    #    «quando tirano una castagna, insistono» che sia un riccio.
    70396: "Un frutto chiuso in un riccio pieno di spine. Fino a poco tempo fa lo confondevano col riccio di mare, e forse per questo c'è ancora chi lo chiama riccio. Rispetto al riccio di mare ha le spine più corte, quindi si tira meglio.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️⚠️ :70398 — il giapponese e' la battuta di <Naplus>, l'inglese e' il
    #    testo generico del rapporto di identificazione: due testi diversi,
    #    non un appiattimento. Si rende il GIAPPONESE (decisione della 116a),
    #    e il titolo e' stato aggiunto alla tabella. ⚠️ Il cancello «titoli
    #    resi in PIU' modi» passa da 6 a 7: e' questa riga.
    70398: "\\\"R-rovinare un riccio porta castigo!\\\"\\n#~Parole di <Naplus> l'alchimista spaventata~",

    # ⚠️ l'inglese perde 弱りはするが: il granchio si indebolisce, ma bollirlo
    #    non basta a ucciderlo. Senza quel «si', ma» la frase e' un'altra.
    70671: "Somiglia molto a un granchio, ma è parente del paguro. Se non lo si cuoce le fibre restano dure e il sapore è poco, quindi in giro lo si trova quasi sempre già bollito. Prima di bollirlo il colore del corpo è viola scuro. Si indebolisce, sì, ma di regola bollirlo tanto non basta a ucciderlo.\\n#~Il Cibo Mutevole di Tyris~",

    71163: "Un'insalata fatta con la parte vegetale del cadavere di una mandragora. Forza magica non ne contiene, ma è piena di sostanze che la magia la producono.\\n#~Il Cibo Mutevole di Tyris~",

    # === I PIATTI E I DOLCI ===============================================
    71706: "Un dolce. Da qualche anno sta prendendo piede l'usanza curiosa di regalare cioccolato in certi giorni per dire grazie. \\n#~Il Cibo Mutevole di Tyris~",
    73153: "Un piatto fatto tagliando a pezzi i tentacoli della stirpe degli yith, mettendoli in un impasto di farina e cuocendoli a palline. L'ingrediente segreto è la piccola dose di sostanze che fanno vedere le allucinazioni. \\n#~Il Cibo Mutevole di Tyris~",
    74164: "Composizione ignota. Manda un odore sospetto che fa venir voglia di rifiutarsi di mangiarlo. Che lo mangi solo chi si è deciso davvero. \\n#~Il Cibo Mutevole di Tyris~",
    74298: "Un pranzo al sacco misterioso: a mangiarlo si torna bambini in un attimo. \\n#~Il Cibo Mutevole di Tyris~",
    74361: "Un pranzo al sacco in cui è chiuso il tempo. Non si deve mangiare per nessun motivo. \\n#~Il Cibo Mutevole di Tyris~",
    74631: "Un dolce di ghiaccio, fatto versando lo sciroppo sul ghiaccio tritato. A mangiarlo di fretta viene una fitta alla testa, e il motivo è che il cervello scambia per mal di testa quel che si sente in gola. \\n#~Il Cibo Mutevole di Tyris~",

    # === LA CARAMELLA DELLA FINE, CORPO E BATTUTA =========================
    75847: "L'ultima cosa che fece un caramellaio disperato perché il lavoro non gli andava. Chiama la fine del mondo. \\n#~Il Cibo Mutevole di Tyris~",
    75849: "\\\"Domani viene chi riscuote il debito e i soldi non li ho... magari domani il mondo finisse...\\\" \\n# ~Parole di un Caramellaio sull'Orlo del Fallimento~",

    76719: "Un piatto semplice: riso stretto in mano fino a compattarlo e insaporito. Quel che lo distingue è che si mangia in fretta, anche mentre fai altro. \\n#~Il Cibo Mutevole di Tyris~",

    # === IL PUTITORO, CORPO E BATTUTA =====================================
    78115: "Un cibo che piace per come mette insieme il morbido che si scioglie e i granelli che scrocchiano sotto i denti. Un tempo si usavano putit lavati e basta, ma siccome è successo più volte che un cliente distratto finisse mangiato dal putit, adesso si usano putit messi in morte apparente. \\n#~Il Cibo Mutevole di Tyris~",
    78117: "\\\"Guarda un po', <Lily>, questo putit è proprio vivace... uwaaa!!\\\" \\n# ~Le Ultime Parole della Vittima~",

    # === IL PANE SOFFICE, CORPO E BATTUTA =================================
    78462: "Un pane a cui, aggiungendo qualcosa di proprio alla lavorazione, hanno dato una consistenza più soffice. La morbidezza si sente già a toccarlo, ma in bocca si capisce molto meglio. \\n#~Il Cibo Mutevole di Tyris~",
    78464: "\\\"I-il pane soffice che ha fatto la mia sorella maggiore è buonissimo!\\\" \\n# ~Parole di una Bambina che Trattiene la Nausea~",

    # === LO ZUCCHERO E IL SALE, CHE SONO SPECULARI ========================
    # ⚠️ in giapponese le due righe sono la stessa frase con dolce e salato
    #    scambiati. L'inglese rompe lo specchio e riscrive la seconda da capo;
    #    l'italiano lo tiene.
    78529: "Uno dei condimenti di base che decidono se un piatto riesce o no. Aggiunge dolcezza, certo, ma è anche un ottimo condimento perché, usato in poca quantità, tira fuori il sapore pieno e il salato che l'ingrediente ha già. \\n#~Il Cibo Mutevole di Tyris~",
    78596: "Uno dei condimenti di base che decidono se un piatto riesce o no. Aggiunge sapore salato, certo, ma è anche un ottimo condimento perché, usato in poca quantità, tira fuori il sapore pieno e il dolce che l'ingrediente ha già.\\n#~Il Cibo Mutevole di Tyris~\\n",

    # === IL PANINO DI CARNE, CORPO E BATTUTA ==============================
    79241: "Un piatto buonissimo che, appena te lo metti in bocca, ti riempie di un sugo che trabocca. Chiedere che cosa ci sia dentro sarebbe soltanto di cattivo gusto. \\n#~Il Cibo Mutevole di Tyris~",
    79243: "\\\"Uhm. La consistenza appena entra in bocca, il sugo che ne esce fuori con impeto, quel sapore tutto suo che resta. Questo piatto merita il posto più alto fra quanti ne ho mangiati. ...A proposito, che carne ci mettono dentro?\\\" \\n# ~Parole di <Gratona>, grande critico gastronomico~",

    79431: "Una verdura molto acida che si è presa addosso tutto il bene del sole. La si cucina in molti modi, ma fra i più strani c'è chi la taglia a fette da cruda e la mangia con lo zucchero sopra.\\n#~Il Cibo Mutevole di Tyris~",

    # === I DUE MOCHI ======================================================
    80487: "Il demone bianco venuto da un paese straniero. Ti chiama con l'odore invitante e con la morbidezza, ma una volta che l'hai mangiato si ferma di colpo in gola e ti toglie di botto i movimenti e i sensi! Se ti succede, fatti aiutare da chi ti sta vicino.\\n#~Il Cibo Mutevole di Tyris~",
    80550: "Un mochi speciale, ornato con le cose di festa. È un mochi benedetto e degno di riconoscenza, ma lo si può mangiare senza pensarci. Contro un mochi che va di traverso, però, non può niente nemmeno un dio: quando lo mangi, guardati bene intorno. \\n# ~Regali che Fa Piacere Ricevere~",

    # === I CIBI CHE CAMBIANO QUALCOSA =====================================
    81669: "Fortuna per te e fortuna per me! Fortuna! Se ne dai un morso piano piano, la felicità di sicuro ti arriva. Se lo mangi tutto in un colpo, ti arriva il responso di un dio. \\n# ~Postilla Scritta sul Retro del Sacco~",
    84100: "La parte della coda del coniglio, che fin dai tempi antichi è segno di fortuna. Pare che in certe zone se ne faccia un ornamento, ma l'insegnamento antico di Tyris del Nord è che mangiandola la fortuna te la prendi dentro direttamente. \\n#~In Cerca di uno Stomaco di Ferro: Piatti Finiti~",
    86466: "Un pranzo al sacco che tua sorella minore ha fatto solo per te. C'è dentro l'amore, quindi non va mai a male. Dicono che soltanto a mangiarlo intorno si formino ioni negativi e che l'effetto di rilassamento sia straordinario, ma io non l'ho ancora mai mangiato... \\n# ~Studio di <Moxis>, massimo esperto di sorelle minori~",
    86800: "Un frutto che, dicono, a mangiarlo fa sgorgare in testa una fonte di sapere. Un mago di gran fama, per averne per sempre, ci spese sopra tutto il suo sapere; ma alla fine a farlo crescere non ci riuscì. \\n# ~Dizionario Fantastico di Irva~",
    87253: "Un formaggio profumato che, dicono, a mangiarlo riempie di forza vitale. Fin dai tempi antichi, si racconta, era il preferito degli eroi coraggiosi e arditi. \\n#~Il Cibo Mutevole di Tyris~",
    88275: "Una mela rara che luccica appena di un colore d'oro. Dentro, dicono, c'è miele in abbondanza e insieme la fortuna, e in passato la gente vagò per il continente in cerca di questo frutto miracoloso. \\n# ~Dizionario Fantastico di Irva~",
}
