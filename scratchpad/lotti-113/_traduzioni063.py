# -*- coding: utf-8 -*-
"""Le rese del lotto 063 — GLI ELMI E I CAPPELLI: `FILTER_HELM` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 063 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa063.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 063`: **16 righe su 16** con lo spazio prima del `\\n`,
16 su 16 con lo spazio dopo il `#`.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 063`: **+16** per 16 rese,
nessuna gemella. ⓘ `_gia-reso.py 063`: 0 su 16.

⚠️⚠️⚠️ **DUE FAMIGLIE ATTRAVERSANO ALTRI LOTTI, E NESSUNO STRUMENTO LE VEDE.**
E' il «sesto posto dove guardare» della 111a, e stavolta si e' cercato apposta
con `_cerca.py` invece che per fortuna:

  - `:99872` apre con 特殊な素材をかけ合わせてより強固な防護を得た**兜**, che
    e' la **terza** riga della famiglia: `:100849` (盾, lotto 058) e `:101769`
    (鎧, lotto 060). L'apertura italiana e' **la stessa parola per parola**;
  - `:43044` e `:43112` aprono con かつて世界征服を目論んだ秘密組織によって
    開発された e chiudono con 現在はわずかに発掘された…程度, tutt'e due, e la
    stessa coppia di frasi sta gia' in gioco su un **terzo** oggetto in
    un'altra categoria. Le due frasi sono copiate dal dizionario, non
    riscritte.
"""

IT = {
    # =====================================================================
    # LA FAMIGLIA DEL SEGRETO: due parrucche, e la cornice e' gia' in gioco
    # =====================================================================
    # ⭐⭐⭐ La prima e l'ultima frase di queste due righe sono identiche fra
    #    loro E identiche a quelle di un terzo oggetto gia' reso (l'oggetto
    #    d'infiltrazione, `db_item.hsp`). Copiate dal dizionario:
    #      «Lo sviluppò un'organizzazione segreta che un tempo puntava alla
    #       conquista del mondo.»
    #      «Oggi ne restano sì e no i pochi esemplari dissotterrati e rimessi
    #       in sesto da qualche artigiano.»
    #    Quel che cambia sta in mezzo, ed e' l'unica cosa che si scrive.
    # ⓘ 防弾チョッキ -> «giubbotto antiproiettile», come nel lotto 060.

    43044: "Lo sviluppò un'organizzazione segreta che un tempo puntava alla conquista del mondo. È una parrucca che si trasforma in ogni acconciatura, e se poi viene pure tinta riconoscere chi la porta diventa quasi impossibile. Per giunta si comanda con le onde cerebrali, e ci sono casi di gente che l'ha adoperata come una frusta o un trapano per ammazzare uno dopo l'altro gli avversari distratti. Oggi ne restano sì e no i pochi esemplari dissotterrati e rimessi in sesto da qualche artigiano. \\n# ~Dizionario Fantastico di Irva~",

    43112: "Lo sviluppò un'organizzazione segreta che un tempo puntava alla conquista del mondo. È una parrucca che si trasforma in ogni acconciatura. La usavano per travestirsi, ma siccome protegge la testa senza lasciar vedere che la si porta, a volte serviva anche da giubbotto antiproiettile per il capo. Oggi ne restano sì e no i pochi esemplari dissotterrati e rimessi in sesto da qualche artigiano. \\n# ~Dizionario Fantastico di Irva~",

    # =====================================================================
    # LA FAMIGLIA DEI MATERIALI: la TERZA riga, dopo lo scudo e la corazza
    # =====================================================================
    # ⭐⭐⭐ :100849 (058) «Uno scudo che, incrociando materiali speciali, ha
    #    ottenuto una protezione più solida.»
    #    :101769 (060) «Una corazza che, incrociando…»
    #    :99872  (063) «Un elmo che, incrociando…»   <- questa
    #    Le tre aperture devono essere la stessa frase, e lo sono.
    # ⓘ 無二の短所 e' «il difetto senza pari»: il giapponese ci scherza sopra,
    #   perche' il peso e' l'unico che nessun materiale compensa.

    99872: "Un elmo che, incrociando materiali speciali, ha ottenuto una protezione più solida. Di pezzi che sfruttano i pregi di un materiale e ne coprono i difetti se ne vedono tanti, ma pare che pochi riescano a coprire il difetto senza pari che è il peso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # GLI ELMI COMUNI — la stessa raccolta del 058 e del 060
    # =====================================================================
    # ⓘ Le rese dell'indice 3 di questi stessi oggetti sono gia' in gioco, e
    #   la descrizione lunga usa le loro parole: «Un'armatura per proteggere
    #   la testa», «Un elmo per i cavalieri», «Un elmo di un certo peso».

    99937: "Un'armatura fatta per proteggere la testa. Copre più di un cappello, ma è chiaro che pesa anche di più. Girano perfino le storielle di chi, a portarlo per ore, si è ritrovato con le spalle indolenzite. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    100002: "Un elmo di gran classe, fatto per i cavalieri. Porta cesellature e ornamenti studiati su misura di chi lo indossa, ma non è roba da sola cerimonia: una certa protezione la dà davvero. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    100067: "Un elmo fatto più spesso del normale. La difesa sale di sicuro, ma in cambio ci si rimette in peso, e a indossarlo conviene starci attenti. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # 吟遊詩人 -> «menestrello» (dizionario).
    100132: "Un cappello elegante, ornato di penne d'uccello. Lo portano spesso i menestrelli, e pare sia perché paragonano la propria voce a quella degli uccelli. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # 変異 -> «mutazione» (la pozione di cura della mutazione, dizionario).
    130844: "Un cappello leggerissimo che dicono portino le fate. Forse perché si ritengono creature fragili, quel cappello ha la facoltà di proteggere dalle mutazioni che vengono da fuori. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⓘ La battuta della riga sta nell'ultima frase: non serve a niente, ma
    #   fa sentire più saggi. L'italiano tiene il 何となく, quel «vago».
    130909: "Un cappello a punta come quelli che uno si aspetta addosso a un mago. Effetti non ne dà nessuno, ma a metterlo in testa un vago senso di essere diventati più saggi lo mette. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # I PEZZI UNICI 《…》, che stanno tutti nel Dizionario Fantastico di Irva
    # =====================================================================

    65398: "L'hanno recuperato mentre andava alla deriva nello spazio. Dalle analisi è risultato una forma di vita meccanica a forma di casco, ma quando è stato trovato pare non avesse più coscienza di sé. Una parte dei suoi sistemi è stata rimessa in funzione, e riesce a controllare la gravità in modo elementare e ad assistere le funzioni del corpo. \\n# ~Dizionario Fantastico di Irva~",

    # ⭐ スンバラリア星人 -> «l'alieno di Sunbararia» (dizionario). E il
    #   giapponese accumula TRE esitazioni di fila — たぶん, おそらく, きっと,
    #   e chiude con はず: la battuta sta nel mucchio, e l'italiano lo tiene.
    66977: "La testa di un alieno di Sunbararia. Fatta come un nautilo, è coperta da un guscio duro e difende sorprendentemente bene. Probabilmente è morta del tutto, quindi a mettersela in testa quasi di sicuro non dovrebbe succedere niente, si spera. \\n# ~Dizionario Fantastico di Irva~",

    # ⓘ La battuta dell'alieno e' un VERSO, non una frase, e monte la lascia
    #   identica in tutt'e tre le lingue.
    # ⚠️⚠️ MA NON SI COPIA COM'E': monte la scrive in caratteri a **doppia
    #   larghezza** (ＡＳＤ…), e `reimporta` ha respinto l'intero lotto per
    #   questo. La build italiana passa da CP932 e ne disegna **uno per
    #   byte**: a schermo uscirebbero lettere latine a caso. Il verso si
    #   riscrive a larghezza singola, lettera per lettera, senza cambiarlo.
    66979: "\\\"ASDJURHFK>ROWRW<MW!\\\" \\n# ~Parole di un alieno di Sunbararia~",

    72418: "Un cappello magico speciale, fatto da un mago che in punto di morte ha sfiorato l'abisso della magia e ci ha messo dentro il mana che aveva da vivo. Lo portano i maghi tornati come non morti, ma qualche raro mago se lo fabbrica ancora da vivo. \\n# ~Dizionario Fantastico di Irva~",

    # ⭐ 幸運の神 e' Ehekatl, e in gioco la sua epiteto e' «Ehekatl della
    #   Sorte»: la riga usa quella parola. 定命 -> «mortale» (dizionario).
    76181: "Il giocattolo preferito della dea della sorte. Se un mortale lo tocca male, la sorte gliela succhia via. \\n# ~Dizionario Fantastico di Irva~",

    80424: "Un elmo di un nero lucido, che si riconosce dalle corna sporgenti in avanti. Dicono che una sola delle corna sia lunga in modo anomalo perché hanno copiato pari pari il tratto della creatura da cui l'hanno pensato. \\n# ~Dizionario Fantastico di Irva~",

    89077: "Un elmo che un saggio si fabbricò per puntare più in alto. A portarlo la conoscenza si fa più profonda, e dicono che si arrivi a vedere perfino ciò che non si potrebbe vedere. \\n# ~Dizionario Fantastico di Irva~",
}
