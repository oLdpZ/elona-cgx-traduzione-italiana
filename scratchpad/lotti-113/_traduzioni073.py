# -*- coding: utf-8 -*-
"""Le rese del lotto 073 — I POZZI: `FILTER_FURNITURE_WELL` si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 073 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa073.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️⚠️ Forma, da `_forma.py 073`: **4 su 4** con lo spazio prima del `\\n`;
code, **3 con lo spazio dopo il `#` e 1 senza**. Quella senza e' `:87574`, la
Grande Enciclopedia, che nell'inglese ha lo spazio **dentro**: `#~ Great…`.
Quattro righe e **tre titoli diversi**.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 073`: **+4** per 4 rese,
nessuna gemella. ⓘ `_gia-reso 073`: 0 su 4. `_122-sorelle-per-frase 073`: 0.
`_119-togli-rinviate 073`: nessuna rinviata.

⚠️⚠️⚠️ **«WATER PILLS» NON ESISTE.** L'inglese di `:90707` dice «if you throw
water **pills** into it»: e' 水薬, che nel glossario e' **pozione** e che monte
ha tradotto a pezzi (水 acqua + 薬 medicina). Il gioco intende la pozione che
si getta in un pozzo, ed e' un fatto di gioco vero.

⭐⭐ **E `:119757` REGGE SU UNA PAROLA RIPETUTA APPOSTA.** Il giapponese dice
清浄 due volte — 清浄な音 e お世辞にも清浄といえる — ed e' li' che sta la
battuta: la fontana fa un suono *limpido*, ma l'acqua *limpida* non e'. Se in
italiano le due parole divergono, la frase perde il suo perno e resta una
constatazione qualunque.
"""

IT = {
    # =====================================================================
    # IL GABINETTO
    # =====================================================================
    # ⓘ ノースティリス -> «Tyris del Nord» (dizionario e glossario).
    #   水洗 e' lo sciacquone. 変わり者 -> «un tipo strano».
    #   全てを捨て去った者 e' «uno che ha buttato via tutto», e il giapponese
    #   lo dice per far ridere: il gabinetto e' una fonte d'acqua nel gioco.
    87574: "Va da sé che i gabinetti esistono anche a Tyris del Nord, e per giunta con lo sciacquone. Ma chi, solo perché ha sete, si mettesse a saziarla in un posto come questo, o è un tipo assai strano o è uno che ha buttato via tutto. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # =====================================================================
    # IL POZZO SACRO
    # =====================================================================
    # ⚠️ 水薬 -> «pozione» (glossario). L'inglese dice «water pills», che e' il
    #   composto tradotto a pezzi e non e' niente.
    # ⓘ 聖なる水 -> «acqua santa», come l'indice 3 di questa stessa voce.
    #   決して汚すことなかれ e' un imperativo arcaico: «Guardati dal profanarlo».
    90707: "Un pozzo pieno d'acqua santa, che dicono esista in un solo posto al mondo. Guardati dal profanarlo: se a cuor leggero ci gettassi dentro una pozione, di sicuro te ne pentiresti. \\n# ~I Mondi che Non Hai Mai Visto~",

    # =====================================================================
    # LA FONTANA — LA PAROLA CHE DEVE TORNARE DUE VOLTE
    # =====================================================================
    # ⭐⭐ 清浄 sta in tutt'e due le frasi, e la battuta e' quella: il suono e'
    #   limpido, l'acqua no. «limpido» / «limpida» tiene il perno.
    #   避暑設備 e' l'impianto per rinfrescare l'estate. 設備 -> «impianto»,
    #   come gli indici 3 di questa categoria.
    119757: "Un impianto per rinfrescare l'estate, che tutt'intorno crea un suono limpido e uno spazio fresco. Detta così suona bene, ma alla fine è acqua di Tyris del Nord che gira in tondo, e nemmeno per cortesia si potrebbe chiamarla limpida. \\n# ~I Grandi Comprimari della Città~",

    # =====================================================================
    # IL POZZO
    # =====================================================================
    # ⓘ 生命線 -> «linfa vitale», che e' quel che l'italiano dice davvero.
    #   社交場 -> «il ritrovo». 浄水技術 -> «la tecnica per depurare l'acqua».
    #   殺菌 -> «disinfettare».
    # ⓘ 雨の日にはしばしば燃えている光景を目にする: il giapponese e'
    #   impersonale e canzonatorio, e la resa lo tiene — «capita spesso di
    #   vederlo che brucia».
    123936: "È la linfa vitale dei cittadini, e un impianto dove si beve acqua senza tante cerimonie. È anche il ritrovo delle signore; ma a Tyris del Nord la tecnica per depurare l'acqua scarseggia, e i guai di chi l'ha bevuta si vedono. Sarà per questo che, forse per disinfettarla, nei giorni di pioggia capita spesso di vederlo che brucia. \\n# ~I Grandi Comprimari della Città~",
}
