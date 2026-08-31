# -*- coding: utf-8 -*-
"""Le rese del lotto 038 — gli SCARTI, prima parte del corpo.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 038 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa038.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️⚠️ `:46213` **non ha coda in italiano**, perche' non ce l'ha in inglese: e'
la terza riga del corpo in questa condizione, dopo `:47287` e `:47288` del lotto
033, e si conserva com'e' (il cancello conta il `#` contro l'inglese).
⚠️ I nomi delle abilita' vengono da `skill.hsp`, dove sono gia' resi. Si
cercano con `lotti-113/_abilita038.py`, non a memoria.
"""

IT = {
    # === LA CARTA VUOTA ===================================================
    42914: "Una carta su cui non è ancora scritta nessuna informazione. Ha addosso una magia particolare, e registra i dati di chi colpisce. È come portarsi via i dati di una persona senza permesso: usarla su chi non è di casa fa arrabbiare di sicuro. \\n#~Catalogo d'Arte di Lumiest~",

    # === I SEI ESPLOSIVI DA LANCIO ========================================
    # ⚠️ famiglia larga: ognuno dice da quali DUE abilita' dipende la
    #    potenza, e i nomi vengono da skill.hsp.
    42976: "Non è un gelato alla fragola. È uno sterco venuto in una forma fin troppo artistica. Essendo arte a tutti gli effetti, va da sé che esplode. La sua potenza, dicono, dipende dalle tecniche di Oreficeria e di Ingegneria genetica.\\n# ~Catalogo d'Arte di Lumiest~",
    43174: "Quel che resta di una conserva che nella scatola ha continuato a fermentare. A leggerla pare fosse pesce salato dei tempi antichi. È gonfia da scoppiare, e a darle un colpo forte sprigiona il fetore e fa un'esplosione che dipende dalle tecniche di Ingegneria genetica e di Cucina. Aprirla è pericoloso, e sondandone dentro la materia si è scoperto che il contenuto si è decomposto ed è quasi tutto allo stato di gas.\\n#~Il Cibo Mutevole di Tyris~",
    43302: "Un cristallo di neve fin troppo grosso, fabbricato da un mago. Pare che verificasse una teoria sospetta: che l'acqua, se le si parla con dolcezza e poi la si congela, diventi un bel cristallo. Il suo malumore (non sia mai che siano gli uomini a decidere che cosa è bello; e non mi si parli con parole d'uomo; e soprattutto non mi si congeli senza permesso) fa un'esplosione che dipende dalle tecniche di Meditazione e di Oreficeria, e ferisce i nemici. \\n#~Compendio Completo degli Oggetti Magici~",
    43364: "Un'arma non letale che avvolge di buio tutto intorno. La sua potenza, dicono, dipende dalle tecniche di Tattica e di Mira. Secondo i documenti, un tempo questo mondo era pieno di colpi accecanti; poi comparve di colpo il colpo oscuro, li batté, e i colpi accecanti furono sepolti nel buio della storia. \\n#~Ancora Armi e Armature da Usare Domani~",
    43426: "Un apparecchio nato dal parafulmine. Con una protezione magica l'ago stesso accumula l'energia dei fulmini, e la scarica quando serve. La forza della scarica, pare, dipende da Controllo magia e da Capacità magica. Di solito lo tengono al chiuso per paura dei ladri e dei danni, ma quando viene il temporale i maghi cominciano a piantarlo all'aperto. \\n#~Compendio Completo degli Oggetti Magici~",
    43488: "Detta anche la scatola della pestilenza. È mascherata da regalo, ma è un'arma chimica che le volpi usano per stregare e uccidere. La fanno coi parassiti: agisce sul cervello e porta disturbi di coscienza. Poi la stregoneria propaga quelle onde ai nemici intorno e fa danni di rimbalzo. La sua potenza, dicono, dipende dalle tecniche di Disarmo trappole e di Ingegneria genetica. \\n#~Non ci Casco Più! Come Scoprire i Trucchi dei Mostri~",

    # === IL BIGLIETTO D'ADDESTRAMENTO =====================================
    43767: "È stato introdotto come rimedio a un problema sociale: i compagni maleducati erano sempre di più. Dandolo a un compagno, in cambio del biglietto viene addestrato. Lo distribuiscono gratis a ogni famiglia, e chi un compagno non ce l'ha pare lo regali a chi ce l'ha, per farsi offrire da bere. \\n#~Bollettino di Palmia~",
    43768: "\\\"Col biglietto si arriva al corso base e non oltre. Più in là non conviene, se non si paga in contanti.\\\"\\n# ~Parole dell'Addestratore di Bestie~",
    43769: "\\\"Il biglietto si può usare, ma la pratica è una noia: meglio pagare in contanti!\\\"\\n# ~Avviso Affisso alla Palestra~",

    # === IL TAPPO E LA CATENA =============================================
    43829: "Il tappo di pozione che si usa comunemente oggi. Per la gente normale è spazzatura. \\n#~Le Mille Cianfrusaglie che Amo~",
    43962: "Una catena tanto bella da vantarsene. Piace perché il disegno la lascia mettere dove si vuole, al collo, al polso, alla caviglia; ma il modo più comune è portarla al collo e lasciarla pendere come una cravatta.\\n#~Scegliamo un Dono per Chi ci sta a Cuore~",
    43963: "\\\"Gli altri schiavi, da un po', mi sventolano davanti le loro belle catene e se ne vantano di continuo. La voglio anch'io una catena bella così!\\\" \\n#~Parole di uno Schiavo Fiero delle Sue Catene~",

    # === IL FUKAGURUMI ====================================================
    # ⚠️ il giapponese fa un gioco di parole (ジョーズ, «Jaws» e «ben fatto»)
    #    che l'inglese rende con «jawsome». L'italiano ha «a pinna d'arte».
    46010: "Un pupazzo di squalo bello grosso. È fatto proprio a pinna d'arte, e morbidissimo. Solo che a Irva, per i pupazzi di squalo, di regola è chi li fa a dare loro un nome. Per questo chi il nome vuole darlo da sé lo evita, e chi ai pupazzi il nome non lo dà lo trova infantile: di richiesta ce n'è poca.\\n#~Grande Compendio dei Fedeli dello Squalo~",

    # === LA DERNEFIA ======================================================
    # ⚠️⚠️ :46213 SENZA CODA: l'inglese non ce l'ha. Vedi testa038.py.
    46213: "Un fiore che all'aperto non cresce. Nasce spontaneo nelle Nefia e ne succhia la forza magica dalle radici, ma le piante fatte così, tranne la dernefia, sono quasi tutte diventate mostri. Perché solo la dernefia non diventi un mostro lo studiano da anni, e pare che non ne vengano a capo. Ai piani sicuri attecchisce male, e in più ha virtù che curano, così che mostri e avventurieri se la mangiano volentieri: di campioni ce n'è pochi.",
    46214: "\\\"Pare che ci sia un fiore introvabile che a Jure donerebbe... Se glielo porto, di sicuro, per quanto faccia la difficile a parole, ci resta contenta... Vado un attimo giù in una Nefia.\\\" \\n# ~Monologo di un Fanatico di Jure~",
    # ⚠️ :46215 non ha giapponese: l'inglese e' la sola fonte, ed e' la
    #    stessa frase dell'indice 3, che l'inglese ripete.
    46215: "È una pianta che, a mangiarla, cura un poco. \\n#~Rapporto di Identificazione: categoria <Piante>~",

    # === IL TAPPO DI BOTTIGLIA E LA BIGLIA ================================
    46275: "Un coperchio di plastica. Leggero, resistente e riciclabile. Ai tempi in cui andavano le bottiglie di plastica ne era pieno il mondo. Solo che in tanti li buttavano nel riciclo senza lavarli, i costi e la fatica sono cresciuti e il recupero è saltato. Per colpa degli imbecilli che li gettavano per strada l'inquinamento è andato avanti, e sono scoppiati anche attentati di ecoterroristi che avevano sbagliato bersaglio. È perfino comparso un malvivente che voleva tenere in pugno la società con un arnese che sparava tappi ad alta velocità. Si dice che i fabbricanti non abbiano retto ai problemi accumulati per più di cent'anni e abbiano smesso di produrli. Oggi che si è diffuso il vetro finto, che costa poco e si lavora facile, sono del tutto roba del passato.\\n#~Le Mille Cianfrusaglie che Amo~",
    46337: "Una pallina di vetro. Da qualche anno se ne fanno anche con fantasie e colori vari, che servono da ornamento. Da dove venga il nome non si sa: le tre spiegazioni più accreditate sono che venga da biidoro, che in lingua antica vuol dire vetro; che fossero palline di grado B; e che siano palline che rispondono all'anima B. Quelle col disegno dentro hanno un disegno che a volte chiamano fiamma, e anche qui le spiegazioni più accreditate sono due: che a una cosa senza nome si sia attaccato un termine inventato, e che si chiami fiamma perché a volte, rispondendo all'anima B, pare una fiamma che brucia.\\n#~Le Mille Cianfrusaglie che Amo~",

    # === IL FISCHIETTO DI COMANDO =========================================
    47149: "Un fischietto d'allarme. Soffiandoci un colpo corto e secco, chi lo sente si fa attento. Il volume in sé non è granché, quindi per svegliare chi dorme non va bene.\\n#~Le Melodie della Limpida Irva~",

    # === LA CICALA MORENTE ================================================
    48735: "Una cicala che in tutta la vita non è mai piaciuta a nessuno. Dopo anni chiusa sottoterra ha deciso che così non poteva andare ed è scesa in città a cercare compagnia. Ha continuato a corteggiare come poteva, ma senza mai un premio, e alla fine le forze le sono venute meno. Se morire deve, vuole morire buttandosi in avanti fino all'ultimo, e si dimena con tutta l'anima. \\n#~Grande Enciclopedia degli Insetti di Irva~",
    48736: "A colpirla si spaventa e manda un'onda di fragore che dipende da Ingegneria genetica, da Lancio e dal livello. Certe volte non regge l'urto e ci lascia la pelle. \\n#~Grande Enciclopedia degli Insetti di Irva: Note~",
    48737: "\\\"Nel tramonto, sul ciglio dove il caldo ancora dura, si spegne la voce della cicala che si contorce.\\\" \\n#~Le Liriche di un Bardo Senza Nome~",

    # === IL MANOSCRITTO E IL MAGAICE ======================================
    50878: "Un foglio con sopra scritti e disegni di ogni sorta. Lo tengono con cura dentro una busta, ma così com'è, in genere, non vale niente. \\n#~Il Libro dei Libri~",
    # ⚠️ l'inglese dice «hot air» due volte: il giapponese dice 冷気, il GELO.
    52579: "Una pietra ricurva con la forza magica di assorbire il gelo. Quando si manda gelo, facendoci passare la magia come attraverso una lente, si trattiene la rottura da congelamento. Ma il raggio in cui agisce è strettissimo, e per ripararsi dal gelo che copre tutt'intorno non serve. \\n#~Misteriosi Ornamenti Antichi~",

    # === IL BARILE ESPLOSIVO ==============================================
    55273: "Un barile con dentro più blocchi di polvere da sparo. A colpirlo genera una fiammata che brucia tutt'intorno. E per conto suo, se prende fuoco, sputa fuori quel che resta della fiamma. In tutt'e due i casi la potenza dipende dalle tecniche di Falegnameria e di Ingegneria genetica.\\n# ~Manuale per il Maneggio di Materiali Pericolosi~",

    # === IL FOSSILE, L'ARGILLA, LO ZOLFO ==================================
    55859: "I resti di esseri vissuti un tempo, chiusi dentro una roccia sedimentaria. Nei terreni antichi i tessuti sono stati sostituiti da minerali, ma in quelli più recenti a volte restano. Nell'era della civiltà biochimica, dicono, si era arrivati anche alla tecnica per ricostruire dal fossile l'essere di partenza. \\n# ~Catalogo d'Arte di Lumiest~",
    55921: "Terra fatta di grani molto fini. La si lavora impastandola a mano, e scaldandola diventa dura. È per questa sua qualità che ci si fanno le ceramiche. \\n#~Catalogo d'Arte di Lumiest~",
    55983: "Un minerale che ha per soprannome pietra che brucia. Nelle civiltà passate, pare, era materia prima in molti campi, ma nell'Irva di oggi non se ne cerca granché. \\n#~Atlante dei Minerali di Vernis~",

    # === LA BIOBATTERIA E IL BIGLIETTO D'ABILITÀ ==========================
    56533: "Un arnese da sopravvivenza che si usava nella civiltà biochimica. È come del grasso attaccato fuori. Sa cambiare la massa in più in una riserva di energia, tenerla a lungo e restituirla quando serve. Siccome l'hanno fatto sulla costituzione degli uomini di allora, sui viventi di oggi l'effetto arriva sì e no a mantenere altezza e peso. Di fame non ti salva, quindi mangia come si deve. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    57893: "Un biglietto che Palmia emette da qualche anno. Serve a imparare gratis le abilità che il lavoro richiede. Lo scopo è alleggerire il più possibile chi cerca lavoro e dare una spinta all'economia. Arriva insieme allo stipendio ai cittadini che vengono giudicati bisognosi d'aiuto. \\n#~Bollettino di Palmia~",

    # === I SEI MATERIUM ===================================================
    # ⚠️ famiglia di sei: la «hai» ha in piu' «con tecnica avanzata» e la
    #    frase sulla gente delle colline, e serve a FABBRICARE; quella
    #    normale serve a RIMETTERE A POSTO. Cambia solo l'aggettivo.
    58024: "Materia lavorata con tecnica avanzata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si fabbricano armi e armature affilate. Pare che il modo di lavorarla l'abbia scoperto tanto tempo fa la gente delle colline. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    58086: "Materia lavorata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si rimettono a posto armi e armature affilate. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    58148: "Materia lavorata con tecnica avanzata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si fabbricano armi e armature robuste. Pare che il modo di lavorarla l'abbia scoperto tanto tempo fa la gente delle colline. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    58210: "Materia lavorata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si rimettono a posto armi e armature robuste. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    58272: "Materia lavorata con tecnica avanzata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si fabbricano armi e armature morbide. Pare che il modo di lavorarla l'abbia scoperto tanto tempo fa la gente delle colline. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    58334: "Materia lavorata e fissata nell'esistenza allo stato di semi-materia. Torna comoda quando si rimettono a posto armi e armature morbide. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # === IL MAZZO DI FIORI E L'OHUDA ======================================
    59728: "Un dono di fiori recisi messi insieme e decorati. Solo che dice fin troppo bene quanto uno ci tenga, e finisce per pesare. A regalarlo a qualcuno con cui non si va molto d'accordo lo si mette a disagio: pensa bene a chi lo dai. \\n#~Scegliamo un Dono per Chi ci sta a Cuore~",
    59790: "A prima vista è solo un foglio con sopra un disegno, ma dentro ci hanno messo forza magica. Lanciandolo vola leggero senza curarsi dell'aria, fa danno magico a chi tocca e cancella anche l'effetto della benedizione. La potenza dipende anche da Dispositivi magici e da Lancio di chi lo usa. \\n# ~Compendio Completo degli Oggetti Magici~",

    # === IL REGALO E IL MOZZICONE =========================================
    60125: "Una scatola misteriosa che, in certi periodi, al risveglio ti ritrovi accanto senza ricordarti di averla messa lì. Regalandola, dicono, dà dolore a chi ti è nemico e sollievo a chi ti è amico: un oggetto che nessuno capisce. L'involucro non si stacca in nessun modo, così che il contenuto non si può vedere; ma secondo una voce ci sono dentro la sciagura e la speranza. \\n# ~Compendio Completo degli Oggetti Magici~",
    60848: "Quel che resta di una sigaretta fumata e buttata via. Attenzione: anche così può prendere fuoco. La fiamma che fa è debole, ma non ti venga in mente di gettarlo in giro. \\n#~I Pericoli sul Ciglio della Strada~",

    # === IL TABACCO E LA MONETA DI BRONZO =================================
    61178: "Una pianta parente della melanzana. La lavorano in tanti modi e serve per fumare. Nell'antichità faceva male, ma nell'era della civiltà biochimica l'hanno migliorata. La specie di oggi non è velenosa, anzi ha dentro molte sostanze che curano, quindi si sta tranquilli... o quasi: dà dipendenza, e va tenuto a mente. Anche masticando la foglia così com'è si sente il sapore e si prende la nicotina. Se è di buona qualità può perfino aiutare a smettere. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",
    61310: "Non è una moneta di rame, perché è fatta di bronzo e non di rame puro. L'hanno pensata per quando si vuole dire grazie ma non al punto di tirare fuori una moneta di platino. Ha cominciato a girare da poco, e rispetto alla moneta di platino è ancora poco familiare. \\n# ~Le Monete del Mondo: Tyris~",
    61312: "\\\"Quando ho scoperto che anche da queste parti c'erano le monete di bronzo mi sono stupita.\\\" \\n# ~Parole di <Norne> la guida~",
}
