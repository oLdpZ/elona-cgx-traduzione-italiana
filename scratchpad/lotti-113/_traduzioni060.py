# -*- coding: utf-8 -*-
"""Le rese del lotto 060 — LE ARMATURE: `FILTER_ARMOR` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 060 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa060.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 060`: **18 righe su 20** hanno lo spazio prima del
`\\n`; le due senza sono `:65809` e `:101574`. Tutte e 20 le code hanno lo
spazio dopo il `#`.
⚠️⚠️ «senza lo spazio prima del `\\n`» NON vuol dire «senza il `\\n`»: il
`\\n` c'e' sempre. E' l'errore che il preflight ha preso nel lotto 059.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 060`: **+20** per 20 rese,
nessuna gemella. ⓘ `_gia-reso.py 060`: 0 su 20.
"""

IT = {
    # =====================================================================
    # LE DUE FAMIGLIE CHE ATTRAVERSANO IL LOTTO 058
    # =====================================================================
    # ⭐⭐⭐ Queste due righe hanno l'apertura IDENTICA a due righe degli
    #    scudi, e cambia un carattere solo: 盾 -> 鎧. Il lotto 058 e' stato
    #    chiuso un'ora fa, in questa stessa sessione, e `_gia-reso` non le
    #    vede perche' le stringhe differiscono. E' il «sesto posto dove
    #    guardare» della 111a: le altre righe della stessa famiglia, anche
    #    se stanno in un altro lotto.
    #
    #    :100717 (058)  非常に分厚く作られた盾。  -> «Uno scudo fatto spessissimo.»
    #    :101964 (060)  非常に分厚く作られた鎧。  -> «Una corazza fatta spessissima.»
    #    :100849 (058)  特殊な素材を…得た盾。    -> «Uno scudo che, incrociando…»
    #    :101769 (060)  特殊な素材を…得た鎧。    -> «Una corazza che, incrociando…»

    101769: "Una corazza che, incrociando materiali speciali, ha ottenuto una protezione più solida. Ha il comodo di potersi infilare sopra i vestiti come un gilè. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⭐⭐ E questa e' anche META' DELLA COPPIA CHE SI GUARDA: vedi :101574.
    101964: "Una corazza fatta spessissima. Con quegli strati spessi un attacco normale non la scalfisce, ma in cambio ci si perde in prontezza. Se prendere questa o la corazza leggera, si dirà, è gusto dell'avventuriero. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # LA COPPIA CHE SI NOMINA A VICENDA, e che l'inglese slega
    # =====================================================================
    # ⭐⭐⭐ 軽鎧 e 厚鎧 chiudono con la STESSA frase e si nominano l'un
    #    l'altra: 「厚鎧とどちらを取るかは冒険者の好み」 /
    #    「軽鎲とどちらを取るかは冒険者の好み」. L'inglese perde i due nomi
    #    e scrive «standard thick armor» e «lighter armor»: chi legge
    #    l'italiano dall'inglese non ritrova nell'inventario nessuno dei
    #    due oggetti. Le due rese usano i NOMI — «corazza a bande» e
    #    «corazza leggera» — e per il resto sono identiche.
    # ⚠️ :101574 e' senza lo spazio prima del \\n.

    101574: "Una corazza che ha il metallo attaccato solo in certi punti. Essendo leggera lascia muoversi svelti e sciolti, ma ci si perde in robustezza. Se prendere questa o la corazza a bande, si dirà, è gusto dell'avventuriero.\\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # LA COPPIA DOVE CAMBIA UNA PAROLA SOLA
    # =====================================================================
    # ⭐ 服の中に**多数の**素材片を… (il giubbotto antiproiettile) contro
    #    服の中に素材片を… (il cappotto): il giapponese distingue con 多数の
    #    e basta. Le due rese cambiano «molti» e nient'altro.

    101379: "Un'armatura rinforzata infilando molti pezzetti di materiale dentro il vestito. Pare che fra la gente di Yerles ci sia qualche tipo strano che lo porta tutti i giorni. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    101509: "Un'armatura rinforzata infilando pezzetti di materiale dentro il vestito. Siccome a prima vista sembra un vestito qualunque, capita spesso che se lo mettano gli avventurieri eleganti. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # LA COPPIA DEL RIVESTIMENTO A BARRIERA — quello riuscito e quello no
    # =====================================================================
    # ⭐ バリアコーティング non e' nel dizionario: nasce qui, e nasce in DUE
    #    righe che si leggono insieme — il costume da bagno in cui il
    #    trattamento e' **fallito** e la tuta da guerra in cui e' riuscito.
    #    «rivestimento a barriera» in tutt'e tre le righe che lo nominano
    #    (c'e' anche :77561).

    70463: "A furia di risparmiare sui materiali, il rivestimento a barriera è venuto male. Si è degradato al punto che basta un graffio leggero perché la superficie si sbricioli. Anche il colore se n'è andato, e la causa è la stessa: la superficie che si sfoglia. \\n# ~Dizionario Fantastico di Irva~",

    70530: "Una tuta che, grazie al rivestimento a barriera, mette insieme una leggerezza e una difesa che con quelle di prima non si possono nemmeno paragonare. Per via di quanto costava produrla non fu mai adottata davvero, e perfino il prototipo restò in magazzino a metà. \\n# ~Dizionario Fantastico di Irva~",

    77561: "In origine doveva essere una tuta che copriva tutto dal collo in giù, ma i costi sono cresciuti più del previsto, lo sviluppo si è fermato a metà strada e ne è stata fatta solo la parte del busto. Per questo a prima vista non sembra altro che un costume da bagno. La superficie ha il rivestimento a barriera, e una sua difesa ce l'ha. \\n# ~Dizionario Fantastico di Irva~",

    # =====================================================================
    # I PEZZI UNICI
    # =====================================================================
    # ⭐ 世界征服 «la conquista del mondo» e 制服 «l'uniforme» si leggono
    #   uguali in giapponese, ed e' il bisticcio del nome 《世界制服》. In
    #   italiano il bisticcio non c'e', ma le due parole restano tutt'e due
    #   nella riga, vicine, dove il lettore le vede.
    #   ナノマシン e' «nanomacchine», gia' nel dizionario.
    51640: "Lo sviluppò un'organizzazione segreta che un tempo puntava alla conquista del mondo. È un oggetto d'infiltrazione ad alte prestazioni, e si trasforma a piacere nell'uniforme di qualunque organizzazione ci fosse allora al mondo. Oggi ne restano sì e no i pochi esemplari dissotterrati e rimessi in sesto da qualche artigiano. Col decadere del regolatore a nanomacchine, le forme che riesce a prendere si sono fatte pochissime. \\n# ~Dizionario Fantastico di Irva~",

    # 竹鎧 e' «armatura di bambù», il nome non identificato di quest'oggetto.
    51707: "L'opera di un inventore di oggetti magici. Pare che, vedendo un cavaliere che maneggiava bene un'armatura di bambù, si sia accorto di quel che il bambù poteva dare. Progettata da zero, ricavata spaccando bambù di prima qualità, rivestita di vernice pregiata e rinforzata con la magia più e più volte, è diventata un'opera d'arte di primo rango, ben oltre un'armatura. Più tardi la volle regalare al cavaliere che gli aveva dato l'idea, e si dice che quello, con un sorriso difficile da spiegare, l'abbia rifiutata con garbo. \\n# ~Dizionario Fantastico di Irva~",

    # 魔力 e' «potere magico» (glossario 111a); 主人 e' «il padrone», come
    #   nelle battute del maggiordomo.
    56670: "Una garanzia per quando il golem va fuori controllo. A un solo cenno del padrone le cinghie si stringono e tengono fermo chi le porta. E c'è anche di che sfogare il potere magico in eccesso. Siccome era l'unico regalo che il padrone le avesse fatto, è tenuta da conto come un tesoro, e di fango non ne ha quasi. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ :65809 e' senza lo spazio prima del \\n.
    #   メイルーン e' «Mayroon», il paese dell'incarico del demone.
    65809: "Una grande corazza che si tramanda nella casa reale di Mayroon, una di quelle che a suo tempo donò un maestro artigiano. Benché sia pensata da cima a fondo contro il freddo, aprendone qualche parte la si può portare benissimo anche nei paesi caldi. Le imitazioni che la gente comune costruiva a occhio erano assai apprezzate come riparo dal freddo fino a una generazione fa; di questi tempi però la linea rozza non piace più, la dicono fuori moda, e sta sparendo.\\n# ~Dizionario Fantastico di Irva~",

    # 機械の神 e' «il dio delle macchine», una dozzina di voci nel dizionario.
    # ⓘ 脱いだらスゴイことになる e' una battuta che l'inglese legge a modo
    #   suo («It looks cool when taken off»): il giapponese non dice bello,
    #   dice grosso.
    75983: "Il vincolo che il dio delle macchine si porta addosso per tenere a freno la propria forza. A toglierselo, succedono cose grosse. \\n# ~Dizionario Fantastico di Irva~",

    # =====================================================================
    # LE ARMATURE COMUNI — e 防具 «armatura» contro 鎧 «corazza»
    # =====================================================================
    # ⚠️ Il glossario della 111a tiene distinte le due parole, e in questo
    #   lotto compaiono tutt'e due, a volte nella stessa riga.

    101444: "Un'armatura fatta legando al busto del materiale a forma di piastra. Siccome il materiale si usa così com'è, la qualità che si sceglie va dritta nelle prestazioni; ma allora ci va dritto anche il peso, e nello scegliere conviene stare bene attenti. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⭐ 法衣 compare DUE volte in questa riga, ed e' il nome di un altro
    #   oggetto del lotto (:130714, «veste»). Tenere la parola rende
    #   leggibile il paragone: la veste papale e' piu' solida della veste.
    101639: "Una veste tessuta perché la porti chi sta più in alto. È un'armatura che pesa un po' di più, ma sempre meno di una corazza. A furia di ricami d'ogni sorta e di tessiture speciali, è venuta più solida di una veste comune. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    101704: "Una corazza fatta legando con dei lacci dei pezzetti di materiale piccoli come squame. Per come è costruita è insieme flessibile e solida. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    101834: "Una corazza fatta cucendo un gran numero di anelli su una corazza di stoffa. Si dice che i molti anelli in superficie abbiano la proprietà di deviare il colpo di una spada. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⭐ 鎖帷子 e' la maglia di ferro, e in gioco quell'oggetto si chiama
    #   «cotta di maglia» (綴り鎧, :101704 qui sopra). Chiamarla col suo nome
    #   dice al giocatore di che cosa e' fatta questa.
    101899: "Una corazza che sovrappone le piastre alla cotta di maglia, e a guardarla pesa. La difesa che dà è enorme, ma in cambio conviene mettere in conto un peso considerevole. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # 僧侶 e' «monaco» e 詠唱 sono gli «incantesimi», come dice l'indice 3.
    130714: "Un'armatura fatta intrecciando il materiale in un unico pezzo di stoffa, e la portano soprattutto i monaci. Per come è fatta a difendere il corpo non serve, ma non intralcia gli incantesimi di chi la indossa e lascia muoversi leggeri. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    130779: "Un'armatura messa a punto via via che le armi si evolvevano. Il suo peso ce l'ha, ma il compito di non far arrivare un colpo mortale ai punti vitali lo assolve bene. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
}
