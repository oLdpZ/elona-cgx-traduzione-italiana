# -*- coding: utf-8 -*-
"""Le rese del lotto 029 — il MOBILIO, terza parte del corpo.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 029 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa029.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️ Tre righe sono **citazioni** (`:94927`, `:98007`, `:98356`): portano le
virgolette doppie **con l'escape**, come `_traduzioni026.py:23`.
"""

IT = {
    # === I TRE LUMI =======================================================
    91718: "Un lampione ornato con un tocco di eleganza. Quando viene notte brilla di luce propria, tenue, e dà a tutto quello che ha intorno un'aria sfarzosa. \\n# ~I Grandi Comprimari della Città~",
    91780: "Un apparecchio per fare luce che si dice costruito, un tempo, da un genio del secolo. La sua fattura ardita è ancora oggi fra le più amate dai nobili. \\n# ~Casalinghi che Danno Colore alla Casa~",
    91842: "Un lume di cera, di quelli che fanno atmosfera. Quella piccola fiamma che ondeggia, dicono, accorcia ancora di più la distanza fra due innamorati. \\n# ~Casalinghi che Danno Colore alla Casa~",

    92124: "Uno scaffale di quelli che circolano dappertutto. Non serve a niente di più di quel che ci si aspetta, ma il minimo indispensabile lo fa: un mobile senza rischi. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    94801: "Una statua di neve dall'espressione buffissima. Quando nevica, dicono, i bambini si radunano, fanno ciascuno il pupazzo che ha in mente e poi se li mostrano a vicenda. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    # ⭐ l'inglese butta via la frase che dice l'oggetto: che rifrange la luce
    #    del sole e sfolgora.
    94863: "Un minerale enorme che, dicono, scaccia gli influssi maligni. Rifrange la luce del sole in ogni direzione e sfolgora, e fin dall'antichità occupa un posto importante nelle arti magiche. \\n#~Compendio Completo degli Oggetti Magici~",

    # === IL GATTO DI PIETRA, e chi non lo sopporta ========================
    94925: "Una colonna di pietra con in cima un gatto grazioso. Quella schiena piena di garbo, si dice, l'artista l'ha scolpita dopo aver colto il capriccio che è proprio dei gatti. \\n# ~Catalogo d'Arte di Lumiest~",
    94927: "\\\"Tempo fa sono stato a Vernis, e c'era quella cosa! La coda spaventosa, e quelle orecchie: solo a pensarci non smetto di tremare... Ma chi mai avrà fatto una colonna del genere? L'unica consolazione è che non era girata verso di me\\\" \\n# ~Parole di <Tam> il nemico dei gatti~",

    # === I TRE QUADRI =====================================================
    94987: "Una natura morta che si dice dipinta da un pittore famoso. I molti girasoli che riempiono la tela, dicono, prendono l'occhio e il cuore di chi guarda e non li lasciano più. \\n# ~Catalogo d'Arte di Lumiest~",
    95049: "Un paesaggio che si dice dipinto da un pittore famoso. In questo quadro, che desta un'aria di nostalgia venuta chissà da dove, ognuno finisce per rivedere il proprio paese. \\n# ~Catalogo d'Arte di Lumiest~",
    # ⚠️ «Quell'espressione» e' di 17 caratteri e l'impaginatore la spezzava:
    #    il cancello si e' acceso su questa riga sola. «Quella sua espressione»
    #    dice la stessa cosa in parole che ci stanno.
    95111: "Un ritratto che si dice dipinto da un pittore famoso. Quella sua espressione velata di malinconia, dicono, ha in sé qualcosa che smuove il cuore di chi guarda. \\n# ~Catalogo d'Arte di Lumiest~",

    95174: "Un tavolo generoso, capace di far posto anche all'ospite che arriva all'improvviso. Quella larghezza di cuore sarebbe da imparare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    95236: "Una pianta in vaso così alta da sfiorare il soffitto. Ogni stelo, tutti quanti, si allunga verso il sole e non guarda altro. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # === IL FUOCO =========================================================
    95298: "Un'attrezzatura per cuocere e bollire i cibi. Ogni volta che la si guarda è occupata, e perciò non ci si può cucinare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    95360: "Un apparecchio che serve a scaldare gli ambienti. La fiamma che divampa crepitando dentro il focolare scioglierà piano il corpo intirizzito fino al midollo. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    95422: "Un forno per fondere i metalli. Dentro è tenuto caldo di continuo da legna arroventata. \\n# ~Verso una Lama Migliore~",

    # === LE COSE DELLA CUPOLA CIBERNETICA =================================
    97873: "Un disco ancora da usare. Non essendo utilizzabile non vale niente, ma di rado, dicono, qualche contadino di Yowyn venuto in gita se lo compra per ricordo. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    97943: "Un piccolo frammento misterioso, inciso con un disegno regolare. Tanto è bello che lo si suppone un ornamento, ma non si può equipaggiare. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    98005: "Una scatola fatta per raccogliere certi rifiuti e non altri. In quella della Cupola Cibernetica, dicono, a metterci dentro qualcosa di diverso gli abitanti fanno una faccia storta. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    98007: "\\\"Avvicinatevi, avvicinatevi! Guardate che pezzo mi sono procurato. Roba che non si trova in giro, eh. Intanto il colore, e poi questa forma. Ha un'aria allegra. E, detto fra noi, questo qui ha un segreto... ehi, ehi, quello ve lo godete dopo che l'avete comprato\\\" \\n# ~La Cantilena di <Moyer> l'imbonitore~",
    98075: "Un corpo di metallo a forma di cilindro, che serviva a conservare qualcosa. A che cosa di preciso ormai è perduto, e così di solito dentro ci si trova spazzatura. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    98145: "Un misterioso apparecchio di memoria in cui, si dice, sono sigillati i ricordi antichi. Così vuole la voce; ma finora nessuno è riuscito ad aprirli. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    98215: "Una scatola prodigiosa che, dicono, distrugge quello che le si mette dentro sottoponendolo a un calore fortissimo. Adesso è rotta, o così pare, e non si può usare. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    98285: "Un apparecchio prodigioso che, dicono, sa imprigionare l'esistenza di una cosa. Adesso è rotto, o così pare, e non si può usare. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    98426: "Una scatola strana che manda un suono sordo. Non ha nessun punto da cui aprirla, e perciò dentro non ci si può mettere niente. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    98496: "Uno strano oggetto che manda lampi. A che serva non si sa, ma passa per ornamento da stanza, e di rado, dicono, qualche riccone se lo compra. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # === L'ATTREZZO DA PALESTRA, e la sua reclame =========================
    98356: "\\\"Cinque minuti al giorno, bastano cinque minuti al giorno, provate! Anche quel vostro corpo grasso e sgraziato, con cinque minuti al giorno qui sopra, in qualche modo si sistema! L'efficacia? Tutta da vedere!\\\" \\n# ~Istruzioni Misteriose in un Angolo dell'Attrezzo~",
    98358: "Una macchina che, a usarla, fa crescere il fisico. Fra le guardie di Palmia, che sul corpo ci campano, c'è perfino chi se l'è comprata apposta per usarla in casa. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # === LE DUE MACCHINE DEI TESORI =======================================
    103360: "Una macchina che, a metterci una moneta straniera, sputa fuori una sfera con dentro un oggetto. Vuole un materiale di più valore di quella rossa, ma in cambio da quel che ne esce c'è da aspettarsi di più. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",
    103425: "Una macchina che, a metterci una moneta straniera, sputa fuori una sfera con dentro un oggetto. Chissà perché, pare che lì attorno ci siano spesso dei bambini a bighellonare. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",
}
