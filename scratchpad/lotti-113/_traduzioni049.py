# -*- coding: utf-8 -*-
"""Le rese del lotto 049 — LE POZIONI, il CORPO, prima parte.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 049 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa049.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri** — la degradazione ad apostrofo la fa
`applica` in build, e `verifica` boccia chi la scrive a mano.

⚠️ Forma, da `scratchpad/lotti-113/_forma.py 049`: **21** righe su 41 hanno lo
spazio prima del `\\n` e 20 no; **18** code portano lo spazio dopo il `#` e 23
no. Le due cose non vanno insieme e si copiano riga per riga.

⚠️⚠️ Previsione di `applica`: **+41** per 41 rese. `_previsione.py 049` non
trova gemelle: 41 righe, 41 firme distinte. E `_gia-reso.py 049` dice 0 su 41.
"""

IT = {
    # =====================================================================
    # LE POZIONI SUPERIORI (上級ポーション): nove righe con la stessa testa.
    #   Il nome dell'oggetto dice gia' «pozione superiore», e la prosa lo
    #   ripete perche' lo ripete il giapponese: e' la formula della classe.
    # =====================================================================

    # ⚠️ 労働エナジー e' «Energia da Lavoro» (`chat.hsp`, la prigione), スタミナ
    #    sono gli **SP** (`skilldesc`: スタミナの減少を無効化 -> «Gli SP non
    #    calano») e 生命力 e' «la vita» (`chat.hsp:16738`).
    43900: "Bevanda a base di Energia da Lavoro. Anticipa le forze, e impedisce una volta sola che gli SP calino o che la vita scenda per il lavoro o la mungitura. Si dice che a berne troppa si rovini la salute, ma nell'Irva di oggi non esiste creatura tanto gracile.\\n#~Bevande da Bere e Bevande da Non Bere~",

    44442: "Una pozione superiore in cui sono stipate sofferenze d'ogni sorta. Se il nemico non è davvero forte, una bottiglia sola basta a renderlo inoffensivo.\\n#~Bevande da Bere e Bevande da Non Bere~",

    44513: "Una pozione superiore in cui sono stipate molte maledizioni. È tanto sinistra che l'avversario più tenace si indebolisce di colpo.\\n#~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️ 一時的に -> «per un po'», mai «temporaneamente» (glossario, 108a).
    44584: "Una pozione superiore che affina per un po' le doti fisiche. È un preparato nuovo, la cui formula è stata messa a punto solo di recente.\\n#~Bevande da Bere e Bevande da Non Bere~",

    58849: "Una pozione superiore che affina per un po' corpo e mente. Si dice l'abbia creata un antico personaggio che era imperatore e insieme un ottimo alchimista.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️ «gli dei» senza accento: `reimporta` rifiuta l'accento DENTRO la
    #    parola, e il progetto scrive «degli dei» dappertutto (`chat.hsp`).
    71997: "Il ricostituente che usano gli dei. Rinforza corpo e mente, spazza via fatica e sonnolenza e guarisce d'un colpo perfino le malattie. Attenzione però: è così forte che si arriva a vedere le allucinazioni.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    72070: "La riproduzione del liquore d'immortalità che si dice bevessero gli dei antichi. Sta bene con qualunque cibo, ed è così buono da far dimenticare perfino l'inappetenza. Ma la riproduzione è imperfetta: per quanto allungato, ubriaca di brutto.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    72141: "Una pozione superiore che tiene chiusa dentro una sciagura. Si dice l'abbia creata per caso un mago che ardeva di vendetta.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    72212: "Un liquido pericoloso: esposto all'aria, se prende un urto o del calore fa una piccola esplosione. Un tempo lo si usava per punire i criminali.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # =====================================================================
    # LE POZIONI CHE PORTANO IL NOME DI UN EFFETTO
    # =====================================================================

    49646: "Un liquore d'un elegante color oro, fatto con il miele. A berlo, lo spirito si stacca per un po' dal corpo e si può passeggiare in giro a piacere. \\n#~Il Mondo Profondo dei Liquori~",

    58920: "Una pozione che, a berla, avvolge in un luccichio come di gemme che danzano tutt'intorno. Dura poco, ma per darsi un'aria sfolgorante basta e avanza.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    65671: "Una pozione che d'un tratto fa sentire come un uccello che corre per il cielo. Indebolisce per un po' la gravità, e per un po' il corpo si fa leggero.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    65742: "Una pozione che d'un tratto alza la capacità di concentrarsi. La testa si fa lucida e dà resistenza al sonno, ma intelligenti non si diventa.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    74432: "Una pozione che un alchimista famoso ha ottenuto dopo anni di ricerche. Il modo di prepararla è troppo complicato perché gli altri alchimisti ci capiscano qualcosa.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    83482: "Una pozione che rimette insieme il corpo di chi la beve secondo ragione. Di che cosa sia fatta non si sa; si sa soltanto che il gruppo della cupola misteriosa pare tenere in mano un pezzo del segreto.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️ 過去のあなた: la stessa immagine di :89149, e le due rese la dicono
    #    nello stesso modo. Il genere del giocatore non si conosce
    #    (`guida-stile.md`), e «il te di ieri» non lo chiede.
    # ⓘ «pericolosissima» sono 15 caratteri, dentro la finestra di rinculo:
    #    il preflight l'ha segnalata e la parola e' stata sciolta prima di
    #    reimportare, invece di aspettare che `_107` dica dove cade il taglio.
    83835: "Una pozione molto pericolosa: nell'istante in cui la si beve si ha la sensazione che qualcosa di quel che si è costruito fin lì stia franando. Sta' in guardia: adesso sei il te di ieri!\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️ L'inglese di questa riga chiude con un `\\n` DOPO la coda — e' l'unica
    #    delle 41 — e la resa lo tiene: il preflight conta i segmenti.
    89149: "Un liquido strano, così caldo che lo si sente attraverso il vetro. Quando ti farai coraggio e lo manderai giù, ci vedrai dentro il te di ieri!\\n# ~Dizionario Fantastico di Irva~\\n",

    84367: "Una pozione con dentro sale in eccesso. Il sale è sciolto del tutto, quindi in cucina non si può usare; pare però che i netturbini della città ne portino con sé parecchie, per sterminare gli insetti nocivi.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    89561: "Una pozione seducente: già solo il nome fa battere il cuore. Chi è privo di delicatezza prova a consegnarla di persona e si becca uno schiaffo sonoro; ma chi ha quel gusto lì faccia pure. Su chi è già più che amico non ha effetto. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # =====================================================================
    # LE BEVANDE VERE: tè, cola, succo, caffè, gazzosa
    # =====================================================================

    # ⚠️⚠️ Le due frasi che il giapponese mette qui — il rutto e la montagna —
    #    l'inglese le sposta nell'indice 2, in bocca al vecchio (`:55346`).
    #    Renderle in tutt'e due i posti le farebbe leggere DUE VOLTE nello
    #    stesso pannello: restano una sola volta, dove il giocatore le vede.
    55344: "Una bevanda gassata dal caratteristico sapore di cannella e vaniglia. Il nome viene dal frutto di un albero, la cola, che all'inizio se ne usava. Contiene molto zucchero: a berne troppa si ingrassa. \\n#~Bevande da Bere e Bevande da Non Bere~",

    55346: "\\\"Se bevi una cola, il rutto arriva!! Sicuro come chi va in montagna senza sapere la strada e ci resta! Sicurissimo! Non c'è scampo!\\\" \\n#~un vecchio bizzarro~",

    # ⚠️ 万能ムギ e' «bannou mugi» nel dizionario: coniato e traslitterato, e un
    #    termine coniato che l'inglese traslittera resta traslitterato (111a).
    55415: "Un tè fatto con i semi del bannou mugi, tostati e messi in infusione. Non venendo da foglie di tè non contiene caffeina. Ha un gusto tostato e pulito, e migliora anche la circolazione del sangue. \\n#~Bevande da Bere e Bevande da Non Bere~",

    59385: "Una bevanda voluttuaria molto amata. Si fa lasciando fermentare le foglie il meno possibile. Oltre a calmare l'animo, rinforza le difese del corpo e aiuta a bruciare i grassi. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️⚠️ L'INGLESE È ROTTO: ricopia la frase del tè verde («minimizing the
    #    fermentation») su un tè che il giapponese dice 完全発酵, fermentato
    #    del tutto. È il tè nero, e il senso di tutta la riga sta lì.
    59456: "Una bevanda voluttuaria molto amata. Si fa lasciando fermentare le foglie fino in fondo. Il mana rimasto nelle foglie, con la fermentazione, prende una forma che il corpo assorbe facilmente: ridà MP e toglie la fatica. \\n#~Bevande da Bere e Bevande da Non Bere~",

    63794: "Una bevanda fatta col succo di frutta, di verdura e di frutti degli alberi. Le sostanze nutrienti si assorbono senza sprechi. Secondo i gusti si possono mescolare più qualità per farne un misto, oppure allungarlo con il latte. \\n#~Bevande da Bere e Bevande da Non Bere~",

    68521: "Una bevanda voluttuaria molto amata. Il sapore cambia con il grado di tostatura, con la macinatura, con il modo di prepararlo e con gli arnesi che si usano, e non ne esiste uno che vada bene a tutti. Va molto anche allungato con il latte. \\n#~Bevande da Bere e Bevande da Non Bere~",

    79574: "Si vende alle bancarelle delle feste, e la possono bere anche i bambini: solletica la lingua. È dolce al punto giusto, e a berla pare che la stanchezza voli via.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    63384: "Uno sciroppo strano: più lo si impasta, più cambia colore e più cresce l'effetto. La strega, per ammazzare il tempo, l'ha impastato e reimpastato per anni, e il risultato è così buono che si sviene.\\n#~Il Cibo Mutevole di Tyris~",

    # =====================================================================
    # I LIQUIDI CHE NON SI BEVONO
    # =====================================================================

    53772: "Un preparato che va a genio ai maniaci della pulizia. Con la forza della purificazione e con la chimica indebolisce microbi e virus e li rende innocui. Sterilizzare non sterilizza, ma contro veleni e malattie funziona. Ha lo stesso ingrediente principale dei liquori, ma essendo purificato non ubriaca. \\n#~Primo Soccorso in Casa~",

    56130: "Un preparato che concentra le sostanze con cui gli animali si mettono d'istinto in allarme. Spruzzato di tanto in tanto intorno a sé mentre si cammina, evita gli assalti delle bestie selvatiche. Ne basta pochissimo, e una boccetta dura per 400 miglia buone. Berlo si può, ma il corpo va oltre l'allarme e lo rigetta: meglio di no. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️ Il nome dell'oggetto è già «benzina», e il giapponese dice il
    #    contrario — 揮発油 («olio volatile») «che chiamano anche gasolina».
    #    Detta com'è scritta, la frase spiegherebbe il nome col nome. Si
    #    gira: è la regola della 117a, il metro è la verità a schermo.
    61652: "Detta anche olio volatile. Pare che le civiltà antiche la usassero come carburante. È molto volatile, e nell'aria dell'Irva di oggi evapora in poco tempo. Prende fuoco ed è pericolosa: se proprio ce la si vuole versare addosso, che sia dove non c'è fiamma. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️ Stessa cosa: il nome è «olio essenziale» e il giapponese 精油 dice
    #    «che chiamano anche olio essenziale». Girata come sopra.
    61723: "Lo chiamano anche essenza. Costa caro, perché per ricavarlo serve una gran quantità di piante. È molto volatile, e nell'aria dell'Irva di oggi evapora in poco tempo. Di solito si usa a gocce, come profumo: a metterne troppo l'odore diventa pesante, quindi non si esageri. È anche infiammabile. \\n#~Bevande da Bere e Bevande da Non Bere~",

    70065: "Un preparato che, mescolato a un cibo, gli impedisce per sempre di marcire, ma dimezza la crescita che quel cibo dà. Va diluito e mescolato al cibo: bevuto com'è, fa male. Su ciò che è già marcio, naturalmente, non ha effetto: darlo da bere a un non morto non gli impedirà di decomporsi.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    81811: "Una pozione che stende una pellicola resistente alle fiamme su ciò che vi si immerge. Funziona solo sugli oggetti: a berla, le tue viscere non opporranno la minima resistenza alle scottature di quando si mangia qualcosa di bollente. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # =====================================================================
    # I DUE SCARTI DEL CORPO, E LE DUE VOCI CHE LI COMMENTANO
    # =====================================================================

    56471: "Escrementi liquidi, fatti di scorie e d'acqua in eccesso. Igienico non lo è affatto, eppure fatto fermentare serve per il bucato: c'è più di quel che sembra. Non è una pozione, ma bere si può... Attenzione però, il sale è parecchio. \\n#~Il Sogno di Riusare gli Scarti~",

    # ⚠️ Il giapponese è un cartello — 「ここにおしっこをさせないでください」 — e
    #    la coda lo dice («Il Cartello Bagnato alla Base»). L'inglese ci mette
    #    una battuta sua, «Dare you enter my magical realm?», firmata «the
    #    Whizzard»: la coda italiana viene dal giapponese, e il corpo pure.
    56473: "\\\"Non fate pipì qui.\\\" \\n#~Il Cartello Bagnato alla Base~",

    83972: "Si esagera con il bere, oppure si mangia qualcosa di andato a male: è la materia tragica che il corpo produce difendendosi in quei frangenti. Non è una pozione, ma bere si può. Si può... bere... \\n#~In Cerca di uno Stomaco di Ferro: Piatti Finiti~",

    83974: "\\\"Finché si è vivi capita anche di vomitare, lo so. Ma dentro la città non lo permetto, mai. Provaci davanti a me, e te lo ricaccio in bocca all'istante!\\\" \\n#~Parole di <Balzak> il custode~",

    # =====================================================================
    # LE DUE CARAMELLE E LA CAPSULA
    # =====================================================================

    77634: "Una caramella tradizionale, fatta a Vernis da tempo immemorabile. Gira soltanto fra i ricchi e la gente che conta, e alla gente comune non capita di assaggiarla. Non capita nemmeno di vederla. \\n# ~Dizionario Fantastico di Irva~",

    77636: "\\\"La caramella che il nonno mi dà sempre è cremosa e buonissima, però... a dirla tutta preferirei la paghetta.\\\" \\n# ~Parole di un Nipote Speciale~",

    79503: "Un piccolo oggetto cilindrico fatto di una materia azzurra. Si dice sia un cibo che rimette in moto il corpo, ma con quell'aspetto nessuno pare avere voglia di provarlo. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
}
