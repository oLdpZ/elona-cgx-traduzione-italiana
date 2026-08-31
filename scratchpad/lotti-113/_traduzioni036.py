# -*- coding: utf-8 -*-
"""Le rese del lotto 036 — gli ATTREZZI, quarta parte del corpo.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 036 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa036.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️ Niente virgolette a caporale e nessun accento **in mezzo** a una parola:
`degrada()` ci mette l'apostrofo dentro e a schermo la parola si rompe.
⚠️ Niente numeri cerchiati: CP932 li scrive su due byte e la build inglese ne
disegna uno per byte (lezione del lotto 035).
"""

IT = {
    # === LE DUE GEMME DIVINE, prima parte =================================
    # ⚠️ famiglia con :85434, :85503, :85572: stessa apertura, cambia il dio.
    76314: "La gemma miracolosa che ha portato il dio delle macchine. Alzandola al cielo, dicono, dall'orbita di un satellite piove una pioggia di raggi di particelle cariche. Pare che insieme lancino anche un laser per impedire che le particelle si sparpaglino e si smorzino, ma di preciso non si sa. \\n# ~Dizionario Fantastico di Irva~",
    77773: "La gemma miracolosa che ha portato la dea della ricchezza. La si regala, dicono, a chi si vuole passare la paghetta. \\n# ~Dizionario Fantastico di Irva~",

    # === IL CALDERONE E IL VASO ===========================================
    78256: "Il paiolo che gli alchimisti usano per la fusione. I materiali si fanno bollire insieme a certi preparati, e la reazione fra loro cambia la struttura della materia a livello di atomi. \\n# ~Manuale d'Introduzione all'Alchimia~",
    78322: "Ci hanno messo sopra una magia che fonde fra loro certi oggetti e ne fa un altro. Anche a guardarlo come opera d'arte è un bel pezzo. \\n# ~Catalogo d'Arte di Lumiest~",

    # === LE SEI STATUE ====================================================
    # ⚠️ famiglia con :73698 e :73765 (lotto 035): stessa apertura, cambia il
    #    dio e la frase finale. I nomi degli dèi vengono dall'indice 3.
    79111: "Una statua che raffigura il dio delle macchine, opera di un artista famoso. I punti fatti a incastro qua e là hanno un non so che di grintoso. \\n# ~Catalogo d'Arte di Lumiest~",
    79178: "Una statua che raffigura il dio del raccolto, opera di un artista famoso. L'aria mesta del volto ha un non so che di fiero. \\n# ~Catalogo d'Arte di Lumiest~",
    82809: "Una statua che raffigura la dea della fortuna, opera di un artista famoso. Il sorriso spensierato ha un non so che di tenero. \\n# ~Catalogo d'Arte di Lumiest~",
    85168: "Una statua che raffigura la dea della guarigione, opera di un artista famoso. Il portamento schivo dà un non so che di puro. \\n# ~Catalogo d'Arte di Lumiest~",
    86533: "Una statua che raffigura la dea del vento, opera di un artista famoso. Le membra, fatte come se scorressero, hanno un non so che di bello. \\n# ~Catalogo d'Arte di Lumiest~",
    86600: "Una statua che raffigura il dio della terra, opera di un artista famoso. La posa piena di slancio ha un non so che di fiero e virile. \\n# ~Catalogo d'Arte di Lumiest~",

    # === IL MARTELLO DI GAROK =============================================
    80218: "Il martello di Garok, maestro artigiano, che di qualunque ciarpame fa in un attimo un pezzo unico. Però l'indole difficile dell'artigiano è passata tale e quale nel martello, e a quanto pare le nostre richieste non le ascolta. \\n# ~Dizionario Fantastico di Irva~",

    # === LA STATUA DEL CREATORE E IL CRISTALLO ============================
    80924: "Una statua indefinibile, opera di un artista di cui non si sa il nome. Comunque la si guardi è la figura di una persona vestita in modo strano, ma sul fianco c'è inciso Creatore: forse allora è questo il suo aspetto. \\n# ~Catalogo d'Arte di Lumiest~",
    80992: "Un cristallo enorme, che un tempo lunghissimo ha messo insieme. La sua luce, dicono, riflette il cuore di chi guarda e lo porta in questo mondo. \\n# ~Dizionario Fantastico di Irva~",
    # ⚠️ :80994 non ha giapponese: l'inglese e' la sola fonte.
    80994: "\\\"Ti basta evocare avventurieri da un altro mondo e le faccende te le sbrigano loro. Comodo, no?\\\" \\n# ~<Lane>, evocatrice di fate~",

    # === LA FRUSTA E IL CUORE =============================================
    81130: "Una frusta di cuoio, che flette bene, di quelle che usano i capi del circo. Basta schioccarla una volta e qualunque belva diventa docile. \\n# ~Cose Lunghe Fatte per Essere Avvolte~",
    81196: "Un'opera d'arte che, con materiali particolari, rappresenta un animo in pena fra due sentimenti che non stanno insieme. I materiali, intrecciati l'uno all'altro, si muovono appena, come farebbe un cuore vero. \\n# ~Dizionario Fantastico di Irva~",

    # === IL SACCO DA BOXE =================================================
    82004: "Un attrezzo da ginnastica alto e stretto, fatto per scaricare lo stress di ogni giorno e per allenarsi. La piccola differenza fra quello di Tyris del Nord e quello comune, forse, è che come materiale dentro non ci va la sabbia ma una vittima indebolita. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # === LE DUE ESPERIENZE SEGRETE ========================================
    83078: "Una gemma misteriosa che, solo a guardarla, mette a disagio. Si può usare, ma pare che nessuno abbia mai visto che effetto faccia. \\n# ~Dizionario Fantastico di Irva~",
    83209: "L'altro miracolo che il dio del raccolto ha concesso. A usarla manda luce, e lì dentro, dicono, si fa un'esperienza che non si sa dire. \\n# ~Dizionario Fantastico di Irva~",

    # === IL FISCHIETTO E IL MAZZO =========================================
    84035: "Un fischietto che, a usarlo, manda intorno un suono acuto. Quel suono sveglia in un attimo chiunque, per quanto dorma sodo: pare il corno della sciagura che chiama la fine del mondo. ...Almeno per chi stava dormendo. \\n# ~Le Melodie della Limpida Irva~",
    84163: "Un contenitore per tenerci le carte. Fra i nobili, dicono, c'è stato perfino chi, non contento di collezionarle, si è inventato un gioco da farci. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # === LE DUE SFERE DI CATTURA ==========================================
    84296: "Una sfera meccanica dalla luce sospetta, fatta per catturare esseri speciali. Per ricavarci dentro uno spazio comodo hanno forzato parecchio il meccanismo, e basta sbagliare il lancio perché si rompa e sparisca. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    85234: "Una sfera meccanica che, lanciata, cattura i nemici indeboliti. Come sia fatta di preciso non si sa, ma si pensa che il fiorire della genetica c'entri molto con l'evoluzione di questo arnese. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # === I DUE STRUMENTI DI PENA ==========================================
    84967: "Uno strumento di pena orribile come pochi, che un tempo serviva alle esecuzioni. Ha una struttura così semplice perché è fatto per una cosa sola: far cadere la testa alla vittima. Pare che oggi non si usi più, ma non abbassare la guardia: la lama sopra di te manda sempre un luccichio spento. \\n# ~I Mondi che Non Hai Mai Visto~",
    # ⚠️ :84969 non ha giapponese, e l'inglese e' un gioco di parole
    #    («get ahead» / «a head»). Si tiene con un'altra immagine.
    84969: "\\\"Con uno di questi, nella vita, si va avanti: gli altri restano indietro di una testa!\\\" \\n# ~parole di un ex boia~",
    85030: "Uno strumento di pena orribile come pochi, che un tempo serviva a far parlare. Il davanti si apre in due, e dentro ci sono aghi di ferro assetati di sangue che sporgono verso il centro. Si racconta che qualcuno si metta in moto da solo: meglio non toccarlo per curiosità. \\n# ~I Mondi che Non Hai Mai Visto~",

    # === LA MACCHINA GENETICA E LA MATRICE ================================
    85298: "Una macchina strana, un cilindro trasparente. In verità è una macchina diabolica e fuori da ogni regola: scompone un essere vivente in particelle, ne cava fuori le sole doti e quelle doti le aggiunge a un altro essere. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    85367: "Un cristallo misterioso ad alta energia, arrivato dallo spazio. C'è chi dice che dentro ci sia il sapere di guerrieri di un altro pianeta, ma di preciso non si sa. \\n# ~Dizionario Fantastico di Irva~",

    # === LE ALTRE TRE GEMME DIVINE ========================================
    85434: "La gemma miracolosa che ha portato il dio del raccolto. Ha il potere, dicono, di dare abbondanza in un punto solo. \\n# ~Dizionario Fantastico di Irva~",
    85503: "La gemma miracolosa che ha portato la dea della guarigione. Ha il potere, dicono, di spargere vita tutt'intorno. \\n# ~Dizionario Fantastico di Irva~",
    85572: "La gemma miracolosa che ha portato la dea del vento. Ha il potere, dicono, di far sentire il vento del tempo. \\n# ~Dizionario Fantastico di Irva~",

    # === IL TESORO SEGRETO E LA BOMBA =====================================
    86132: "Una gemma che, a usarla, porterebbe al proprio corpo un cambiamento nuovo. \\n# ~Dizionario Fantastico di Irva~",
    86200: "\\\"Non è la cosa in sé a essere il male: il male è chi l'ha usata.\\\" \\n# ~Le Parole sull'Ultima Pagina del Manuale~",

    # === IL LETTO ORIENTALE E IL CORNO ====================================
    88021: "Un giaciglio venuto da un paese straniero, che si stende in terra e basta. Anche se in mezzo c'è la stoffa, si sta schiena contro schiena col terreno duro, e a dormirci non pare granché comodo. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    88210: "Il corno dell'unicorno, che nessuno ha mai visto. Bollito e bevuto, dicono, porta via dal corpo l'inquietudine e la follia. \\n# ~Dizionario Fantastico di Irva~",

    # === IL PASSE-PARTOUT E IL GRIMALDELLO ================================
    88410: "Un oggetto speciale che, usato insieme al grimaldello, rende più facile aprire le serrature. Siccome in qualunque toppa lo si infili entra a pennello, si pensa che sia un resto di un'altra epoca. \\n# ~Dizionario Fantastico di Irva~",
    88472: "L'arnese che, per aprire una serratura, si può dire d'obbligo. Il difetto è che ogni tanto si rompe, ma con una buona mano non c'è forziere che tenga. Chiavi per aprire ce ne sono; per chiudere, in questo mondo, nessuna. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # === LA MINA E IL GUINZAGLIO ==========================================
    88538: "Un'arma che, a usarla, si sotterra e sparisce del tutto alla vista. Chi calpesta quel punto senza saperne niente, dicono, salta via che non ne resta traccia. Sì: anche se a calpestarla fossi tu... \\n# ~Regali che Fa Piacere Ricevere~",
    88604: "Una corda che, a usarla, lega il bersaglio. Se sei di quelli che si sentono soli e vogliono qualcuno lì vicino te la consigliamo, ma a legare chiunque capiti forse qualcuno si arrabbia. \\n# ~Cose Lunghe Fatte per Essere Avvolte~",

    # === IL MARTELLO DEI MATERIALI ========================================
    # ⚠️ il nome dell'oggetto dice «kit», il giapponese dice 槌, martello.
    #    Vedi testa036.py: qui il nome viene dall'inglese, non dal giapponese.
    88869: "Un martello che sa battere il materiale di una cosa fino a farne un altro materiale, del tutto diverso. Questo pezzo miracoloso è opera di due fratelli artigiani che vivono ritirati nelle nevi, ed è anche l'arnese che adoperano. \\n# ~Dizionario Fantastico di Irva~",

    # === IL SET DA TRAVESTIMENTO ==========================================
    88937: "Un arnese che permette di cambiarsi in un lampo, farsi passare per un altro e cavarsi dai guai. Anche senza tempo lo puoi usare tranquillo: quando lo apri sbuffa fuori di forza una nebbia bianca, e quella il tempo di travestirti te lo dà. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",
    88939: "\\\"La prima volta che ho rubato non avevo ancora dieci anni. Allora cercavo solo di restare vivo. Sfacciato lo sono ancora come allora: solo, un po' più furbo.\\\" \\n# ~Parole di <Sin> il maestro della Gilda dei Ladri~",
}
