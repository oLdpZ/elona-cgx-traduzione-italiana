# -*- coding: utf-8 -*-
"""Le rese del lotto 052 — LE PERGAMENE, seconda meta': la categoria CHIUDE.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 052 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa052.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 052`: **tutte e 23** le righe hanno lo spazio prima del
`\\n`, e una sola coda porta lo spazio dopo il `#` — `:108327`, l'unica che non
viene dal `~Compendio Completo degli Oggetti Magici~`.

⚠️⚠️ Previsione di `applica`: **+23** per 23 rese, nessuna gemella.
`_gia-reso.py 052`: 0 su 23.
"""

IT = {
    # =====================================================================
    # LE PERGAMENE CHE CAMBIANO CHI LEGGE
    # =====================================================================

    102250: "Una pergamena che permette di approfondire la fede parlando col proprio dio. Più che una pergamena sarà una specie di lettera indirizzata a lui. \\n#~Compendio Completo degli Oggetti Magici~",

    102321: "Una pergamena preziosa, su cui è posata una magia che fa crescere il corpo. A leggerla diventerai più tenace. \\n#~Compendio Completo degli Oggetti Magici~",

    104446: "Una pergamena che rende svegli per un po'. Si dice che nella stagione degli esami le botteghe si riempiano per un momento di clienti che, invece di studiare, contano su questa. \\n#~Compendio Completo degli Oggetti Magici~",

    105013: "Una pergamena che, letta, riempie di mana il corpo in un istante. Pare che averne una addosso nei momenti critici serva più di quanto si creda. \\n#~Compendio Completo degli Oggetti Magici~",

    114930: "Una pergamena che fa affiorare di colpo nella testa una conoscenza magica. Secondo una teoria sono pezzi di pagina caduti dal libro in cui gli dei avevano messo per iscritto la propria magia, per non dimenticarla. \\n#~Compendio Completo degli Oggetti Magici~",

    # ⚠️ ヒデンショ e' 秘伝書 scritto in katakana: dal punto di vista del
    #    giapponese e' una parola di «terre lontane e straniere», ed e' la
    #    battuta. L'inglese la traduce («Master Recipe Tomes») e la perde.
    #    Resta traslitterata, per la regola della 111a.
    115001: "Una pergamena preziosa, che a leggerla darebbe una capacità nuova. Si dice che in terre lontane e straniere queste pergamene le chiamassero hidensho. \\n#~Compendio Completo degli Oggetti Magici~",

    # =====================================================================
    # LE MALEDIZIONI: quattro pergamene e una scala
    # =====================================================================

    # ⚠️ In queste cinque righe 装備品 NON si rende «equipaggiamento»: con la
    #    preposizione articolata sono 19-20 caratteri, ben oltre la finestra
    #    di rinculo dell'impaginatore, e la parola si spezzerebbe. Si dice
    #    «un oggetto che si indossa», che e' anche la forma del rapporto di
    #    identificazione di queste stesse pergamene.

    # 全浄化: TUTTE le maledizioni di dosso.
    105084: "Una pergamena che annulla tutte le maledizioni che si hanno addosso. Quelle su un oggetto indossato no: là, chissà perché, non funziona. \\n#~Compendio Completo degli Oggetti Magici~",

    # 清浄なる光: UNA sola, e la frase e' la stessa.
    105155: "Una pergamena che annulla una maledizione che si ha addosso. Quelle su un oggetto indossato no: là, chissà perché, non funziona. \\n#~Compendio Completo degli Oggetti Magici~",

    105452: "Una pergamena che stende per un po' un velo sacro, che si dice protegga dalle maledizioni che piombano addosso. \\n#~Compendio Completo degli Oggetti Magici~",

    # *解呪*, la superiore: 失敗することはない、はずだ — «non fallisce mai,
    # dovrebbe». Il giapponese si rimangia la promessa con l'ultima parola, e
    # l'inglese la scrive senza («never fails to break the curse»).
    106981: "Una pergamena che toglie la maledizione a un oggetto indossato. Essendo più forte, la purificazione non fallisce mai. Dovrebbe. \\n#~Compendio Completo degli Oggetti Magici~",

    117256: "Una pergamena che toglie la maledizione a un oggetto indossato. Se la maledizione è troppo forte la purificazione fallisce, e allora conviene pensare a un'altra strada. \\n#~Compendio Completo degli Oggetti Magici~",

    111921: "Una pergamena pericolosa, che getta una maledizione su un oggetto indossato. Certe rare volte, quando la si usa, non fa effetto e si sbriciola: sarà il frutto della condotta di tutti i giorni. \\n#~Compendio Completo degli Oggetti Magici~",

    # =====================================================================
    # LE DUE COPPIE: identificazione e teletrasporto
    # =====================================================================

    107052: "Una pergamena che identifica gli oggetti non identificati. È più forte del solito, ma se anche così l'oggetto non si lascia identificare, tanto vale farlo esaminare da un mago. \\n#~Compendio Completo degli Oggetti Magici~",

    130314: "Una pergamena che identifica gli oggetti non identificati. Con gli oggetti potenti certe volte non ce la fa, e in quei casi conviene farsi dare una mano da un mago. \\n#~Compendio Completo degli Oggetti Magici~",

    114859: "Una pergamena che, creando una piccola piega nello spazio, sposta in un istante. Ha un effetto piuttosto debole, e si racconta per ridere di gente che l'ha usata per accomiatarsi da qualcuno e si è ritrovata a ricomparirgli accanto, con tutto l'imbarazzo del caso. \\n#~Compendio Completo degli Oggetti Magici~",

    130172: "Una pergamena che, creando una piega nello spazio, porta in un istante da un'altra parte. Nei momenti critici è comoda, ma la meta non si può scegliere: per quando si è in ritardo a un appuntamento, non serve. \\n#~Compendio Completo degli Oggetti Magici~",

    115453: "Una pergamena che chiama un portale collegato a un luogo preciso. Anche se la si usa per sbaglio, niente panico: rileggendola si annulla. Ovviamente se ne consumano due, ma pazienza: consideralo il prezzo della lezione. \\n#~Compendio Completo degli Oggetti Magici~",

    # =====================================================================
    # LE PERGAMENE CHE GUARDANO
    # =====================================================================

    103576: "Una pergamena che fa avvertire dove c'è qualcosa. Sente anche al di là di un muro, dove non si sa cosa ci sia, e perfino gli oggetti invisibili: conviene tenerne pronta una quando si esplora. \\n#~Compendio Completo degli Oggetti Magici~",

    # ⓘ ネフィア e' «Nefia», il nome dei labirinti (`chat.hsp`).
    115072: "Una pergamena che legge in un istante il terreno intorno. Serve soprattutto dentro Nefia, quindi la trovata poco pulita di intrufolarsi in casa della ragazza che ti piace per usarla lì non funziona. \\n#~Compendio Completo degli Oggetti Magici~",

    130243: "Una pergamena che, si dice, faccia sapere dell'esistenza degli oggetti leggendari. Chi ce li abbia non lo dice: il dio non ti è amico fino a quel punto. \\n#~Compendio Completo degli Oggetti Magici~",

    # =====================================================================
    # LE ALTRE
    # =====================================================================

    # ⓘ マテリアル e' «materiale» (glossario, 111a).
    104663: "Una strana pergamena che, a leggerla, fa cadere dei materiali dal cielo. Perché a leggere una pergamena piovano materiali, questo legame non si è ancora capito. \\n#~Compendio Completo degli Oggetti Magici~",

    130101: "Una pergamena che in un istante permette di farsi passare per un altro. Usandola ci si sente il grande ladro che tiene in scacco un regno. \\n#~Compendio Completo degli Oggetti Magici~",

    108327: "L'atto che serve come pratica per comprare una casa. Anche a essere avventurieri, non si può dormire sempre all'addiaccio. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",
}
