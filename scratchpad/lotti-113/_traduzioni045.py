# -*- coding: utf-8 -*-
"""Le rese del lotto 045 — I CIBI, seconda parte: uova, semi, erbe e pesci.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 045 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa045.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️ La forma di questo lotto e' di nuovo disomogenea, e si legge da
`scratchpad/lotti-113/_forma.py 045`: 11 righe su 28 hanno lo spazio prima del
`\\n` e 17 no; 7 code su 28 sono `# ~` con lo spazio e 21 sono `#~` senza.
Le due cose **non coincidono**, e la tabella si legge riga per riga.

⚠️ Previsione di `applica`: **+28** su 28 rese, dal referto di
`scratchpad/lotti-113/_previsione.py 045` — nessuna riga gemella in questo lotto.

⭐⭐ TRE FAMIGLIE tengono insieme il lotto, e vanno scritte uguali:

  - i **sette semi** condividono la seconda frase parola per parola, e la terza
    si sdoppia in due varianti che l'inglese **appiattisce in una sola**;
  - le **sei erbe** aprono tutte con 〜で有名なハーブ, «un'erba famosa per»;
  - i **dieci pesci** non hanno una frase comune, ma due spiegano il proprio
    nome, e li' l'italiano ha dovuto rifare il gioco (vedi `testa045.py`).
"""

IT = {
    # === L'UOVO E LA CARNE SECCA ==========================================
    # ⚠️ l'inglese scrive «our home d?cor»: la `é` di «décor» e' andata persa a
    #    monte e al suo posto c'e' un punto interrogativo vero (0x3F). Misurata
    #    la famiglia: e' l'UNICA in tutto il sorgente. L'italiano non ci passa.
    # ⚠️ e 我が家 qui e' la casa di chi legge (あなた), non «our».
    92585: "Un oggetto ovale, pieno zeppo della sorgente della vita. Va da sé che è un blocco di sostanze nutrienti. Le uova di Tyris del Nord non marciscono, quindi puoi anche romperlo subito e farne nutrimento per crescere, oppure tenerlo lì e metterlo in mostra come un pezzo d'arredo di casa tua.\\n#~Il Cibo Mutevole di Tyris~",

    # ⓘ 申し訳程度の料理: un piatto che si chiama piatto per modo di dire.
    92717: "Carne cruda messa sotto sale perché non si guasti e poi seccata al sole, così pesa poco da portare e dura a lungo. Come piatto è poca cosa, ma pare che con la birra crim ci stia benissimo, e i tipi robusti se la rosicchiano spesso alla taverna. \\n#~Il Cibo Mutevole di Tyris~",

    # === I SETTE SEMI =====================================================
    # ⭐ la seconda frase e' identica in tutti e sette, e in italiano lo resta.
    # ⚠️⚠️ la terza no: quattro semi dicono «aspetta che cresca, vale più
    #    domani di oggi», tre dicono «non ne caverai una sazietà che valga la
    #    promessa del seme». L'inglese scrive per tutti e sette la PRIMA, e
    #    cosi' appiattisce tre righe su sette.
    # ⓘ 杖 qui e' la BACCHETTA, non il bastone: `action.hsp:19811` fa cadere
    #    ITEM_ID_ROD_* dall'albero magico. Il codice conferma il giapponese.
    93890: "Un seme che, seminato per terra, dà un raccolto di bacchette. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma piuttosto che farlo aspetta un poco che cresca. Vale più domani di oggi. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    93957: "Un seme che, seminato per terra, dà un raccolto di minerali. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma piuttosto che farlo aspetta un poco che cresca. Vale più domani di oggi. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    103104: "Un seme che, seminato per terra, dà un raccolto di frutta. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma piuttosto che farlo aspetta un poco che cresca. Vale più domani di oggi. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    103171: "Un seme che, seminato per terra, dà un raccolto di verdura. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma piuttosto che farlo aspetta un poco che cresca. Vale più domani di oggi. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ⚠️ i tre che l'inglese appiattisce: qui il giapponese dice un'altra cosa.
    102903: "Un seme che, seminato per terra, dà un raccolto di artefatti. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma non ne verrà una sazietà che stia alla pari con quello che il seme promette. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    102970: "Un seme che, seminato per terra, dà un raccolto delle cose più diverse. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma non ne verrà una sazietà che stia alla pari con quello che il seme promette. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    103037: "Un seme che, seminato per terra, dà un raccolto di erbe. Dentro ci sono mescolati geni di ogni sorta, e quel che si raccoglie cambia con l'ambiente. Mangiarlo si può, ma non ne verrà una sazietà che stia alla pari con quello che il seme promette. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # === I DUE SNACK E LO SNACK CIBERNETICO ===============================
    # ⚠️ l'inglese ripete due volte la stessa frase — «But it is delicious! But
    #    it is really tasty!» — dove il giapponese la dice una volta sola.
    97601: "Ingredienti e ricetta: ignoti del tutto! Però è buono! Un articolo misterioso. A mangiarlo sono quasi solo i bambini, ma dicono che perfino l'adulto che per caso ci prova resti prigioniero di quel sapore tutto suo, che sa di roba che fa male. \\n#~Il Cibo Mutevole di Tyris~",

    # ⭐ le patatine e i popcorn condividono la frase del monopolio, e in
    #    italiano la condividono: cambia solo la coda, che il giapponese fa
    #    diversa apposta (chi non vuole crescere / chi si accontenta).
    97664: "Uno snack che va fortissimo fra i giovani: una certa verdura fritta nell'olio. Oggi la ricetta ce l'hanno in mano pochi commercianti che se la tengono stretta, quindi in giro non se ne trova; e siccome quei commercianti, chissà perché, non puntano a crescere, l'economia sta in un equilibrio bizzarro. \\n#~Il Cibo Mutevole di Tyris~",
    97727: "Uno snack che va fortissimo fra i giovani: una certa verdura rifatta da capo con una lavorazione tutta loro. Oggi la ricetta ce l'hanno in mano pochi commercianti, quindi in giro non se ne trova; ma sono in tanti a comprarne per ricordo, e ai commercianti pare che basti così. \\n#~Il Cibo Mutevole di Tyris~",

    # === LE SEI ERBE ======================================================
    # ⭐ tutte e sei aprono con 〜で有名なハーブ: «un'erba famosa per».
    102521: "Un'erba famosa per le foglie spesse e piene di succo. Resta scritto che nei tempi antichi, a seccarla e poi darle acqua, si gonfiava più di quanto pesasse. Oggi c'è chi si serve proprio di questo e se la porta dietro come scorta d'emergenza.\\n#~Atlante Illustrato del Giardinaggio di Tyris~",

    # ⚠️ l'inglese appiattisce 舞踏会 in «social occasions» e perde l'orto
    #    delle erbe: qui il quadro e' la gran dama che si profuma per il ballo.
    102584: "Un'erba famosa per il profumo dolce e gentile che manda in giro. Quel profumo piace anche ai nobili, e quasi tutte le gran dame se la coltivano nell'orto delle erbe, se ne fanno impregnare il corpo e poi vanno al ballo.\\n#~Atlante Illustrato del Giardinaggio di Tyris~",

    102647: "Un'erba famosa per i fiorellini bianchi che mette. Si riproduce meglio delle altre, quindi cresce spesso da sola, e sotto questo aspetto si può ben dire un'erba alla portata di tutti.\\n#~Atlante Illustrato del Giardinaggio di Tyris~",

    # ⚠️ l'inglese perde 奮発して: il cittadino non la compra, ci si sforza.
    102710: "Un'erba famosa per il profumo fresco che manda in giro. Quel profumo calma l'animo di chi lo annusa, e dicono che molti cittadini facciano lo sforzo di comprarla prima di un lavoro importante o di un esame.\\n#~Atlante Illustrato del Giardinaggio di Tyris~",

    # ⚠️ l'inglese appiattisce 他の香辛料にも劣らぬ in «for it's kick».
    102773: "Un'erba famosa per il profumo pungente che manda in giro. È rara, quindi non la si usa molto, ma quel profumo non ha niente da invidiare alle altre spezie, tanto che a volte lo mettono come tocco finale nella cucina di lusso.\\n#~Atlante Illustrato del Giardinaggio di Tyris~",

    # ⚠️⚠️ ROVESCIAMENTO dell'inglese: 食欲減退に効果がある e' «fa effetto
    #    CONTRO il calo dell'appetito», e l'inglese scrive «effective in
    #    reducing appetite», cioe' il contrario. Lo dice la frase dopo: la si
    #    mangia da malati, come piatto medicinale.
    102836: "Un'erba famosa per il profumo selvatico che manda in giro. La dicono efficace contro il calo della fame, e a quanto pare, quando il male è leggero, la si mangia come piatto medicinale.\\n#~Atlante Illustrato del Giardinaggio di Tyris~",

    # === I DIECI PESCI ====================================================
    # ⓘ イーモ resta «imo» (dizionario), e la battuta e' il pesce fritto con
    #    l'imo fritto: il fish and chips di Palmia.
    107600: "Un pesce piccolo, che sta in due mani. Per i piatti in grande non va bene, ma per friggerlo o farlo in tempura sì. Corre voce che a Palmia vada di moda portarselo dietro fritto, insieme all'imo fritto, e mangiarli così.\\n#~Il Cibo Mutevole di Tyris~",

    # ⓘ il nome spiega se stesso e in italiano regge: 舶刀「カトラス」 e' la
    #    sciabola d'arrembaggio, e il pesce da noi si chiama «pesce sciabola».
    107673: "Un pesce che luccica al sole di un bagliore duro, e per questo l'hanno paragonato alla sciabola d'arrembaggio. Come dice il nome è lunghissimo e sottile, e non ha una squama addosso. Il sapore è delicato, quindi si presta ai piatti fini.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️ l'inglese perde 一尾で二度おいしい, che e' la battuta della riga.
    107746: "Sta un po' dappertutto, ma i più famosi sono quelli che vivono nel mare vicino a Porto Kapul. La carne è di un rosso acceso ed è ottima in sashimi, ma passata sul fuoco dà anche una consistenza che pare carne: un pesce solo, e buono due volte.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️⚠️ il nome spiega se stesso e in italiano NON regge: グローブ e' il
    #    guanto, e da noi il pesce si chiama «pesce palla». Rifatto il gioco
    #    sul nostro nome tenendo l'immagine del guanto — il guanto imbottito
    #    e' tondo. Vedi `testa045.py`.
    107819: "Un pesce di color marrone. Vive sui fondali bassi e, dicono, aspetta la preda trattenendo il fiato. Il nome, si racconta, gli venne dalla forma d'insieme, tonda come un guanto imbottito da infilare in mano.\\n#~Il Cibo Mutevole di Tyris~",

    107892: "Un pesce di mare largo quanto le spalle di un adulto. A seconda della stagione il sapore cambia moltissimo, in bene o in male. Quelli tirati su nel momento giusto hanno la carne di un rosa acceso, e per quel colore così suo, un tempo, bastò la parola di un tintore a farlo entrare fra i colori da tintura.\\n#~Il Cibo Mutevole di Tyris~",

    107965: "Un pesce dalle squame così vivaci che diverte anche solo a guardarlo. Anche il sapore è di quelli sicuri, e quel gusto sottile è tenuto prezioso da tempi antichi. Dicono che nei paesi stranieri, per le occasioni liete, l'usanza sia di cuocerlo intero sul fuoco e portarlo in tavola così.\\n#~Il Cibo Mutevole di Tyris~",

    108038: "Un pesce che ha una presenza da schiacciarti. Per molto tempo nessuno se lo mangiò, ma un cuoco che aveva per motto \\\"meglio mangiarne e restarci che non mangiarne affatto\\\" si fece coraggio e lo assaggiò: solo di recente si è saputo che veleno non ne ha, e che il sapore è anzi piuttosto fine.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️ l'inglese scrive «Palmyre» dove il giapponese dice パルミア: e' Palmia.
    108111: "Come dice il nome, un pesce dalla forma piatta e quadrata. Si racconta che in passato, a Palmia, in un'epoca in cui la carta scarseggiava, lo usassero al posto suo: è una bugia bella e buona. E della storia che con la coda lunga ci scrivessero come con una penna non c'è nemmeno da parlare.\\n#~Il Cibo Mutevole di Tyris~",

    108184: "Un pesce che da tempi antichi qualcuno chiamava \\\"la gemma viva di Porto Kapul\\\". E non solo per il sapore, dicono: tenerlo fresco è difficile assai, e i cuochi lo maneggiavano come si maneggia una gemma.\\n#~Il Cibo Mutevole di Tyris~",

    # ⚠️⚠️ l'altro nome che spiega se stesso e che in italiano non regge: il
    #    giapponese fa venire ムーンフィッシュ dalla falce di luna presa a
    #    forza, e da noi il pesce si chiama «pesce re». Rifatto sul nostro
    #    nome, tenendo il «prendere a forza». Vedi `testa045.py`.
    108257: "Un pesce pieno di vita, che si riconosce dalla bocca a punta, come un punteruolo. Il nome gli venne da come si dibatte quando lo tiri su: resiste con una tale ostinazione che pare di star prendendo a forza un re che non vuole saperne di arrendersi.\\n#~Il Cibo Mutevole di Tyris~",
}
