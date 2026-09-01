# -*- coding: utf-8 -*-
"""Le rese del lotto 056 — LE BACCHETTE: `FILTER_ITEM_ROD` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 056 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa056.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 056`: **11 righe su 32** hanno lo spazio prima del
`\\n`, e sono `:93149`, `:94102`, `:94534`, `:96355`, `:98576`, `:104942`,
`:105381`, `:122821`, `:123124`, `:123284`, `:129950`. Tutte e 32 le code hanno
lo spazio dopo il `#`.

⚠️⚠️ Previsione di `applica`: **+32** per 32 rese, nessuna gemella.
`_gia-reso.py 056`: 0 su 32.

⭐⭐⭐ E' UNA SERIE DI TRENTADUE, e `scratchpad/_120-serie-bacchette.py` l'ha
misurata invece di farmela indovinare:

  - **31 righe su 32** aprono con la formula identica, 特定の魔法が封じ込め
    られた杖。 L'apertura italiana e' la stessa in tutte e 31, parola per parola;
  - **una** diverge, ed e' `:111777`, la bacchetta dei desideri: dice
    貴重な杖, «una bacchetta **preziosa**». ⚠️ L'inglese non lo porta, e senza
    quella parola la riga piu' rara del lotto diventa uguale alle altre 31;
  - **`:71856` e `:106766` hanno il giapponese IDENTICO** (l'eclissi e il
    silenzio, tutt'e due 黒く濁った宝石) e due inglesi che differiscono per una
    virgola. Le due rese sono **identiche**, altrimenti sarebbero due rese
    diverse per lo stesso originale.
"""

# ⚠️ Le due righe col giapponese identico: una costante sola, cosi' non
#    possono divergere per distrazione.
# ⚠️ SENZA lo spazio prima del `\n`: tutt'e due le righe che la usano stanno
#    fra le ventuno che non ce l'hanno.
NERA_TORBIDA = ("Una bacchetta in cui è chiusa una magia precisa. Ci sta "
                "montata sopra una gemma nera e torbida.\\n# ~Compendio "
                "Completo degli Oggetti Magici~")

IT = {
    # =====================================================================
    # LE BACCHETTE COL SEGNO DI CIO' CHE FANNO — la gemma
    # =====================================================================

    61946: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma fragile, che pare stia per rompersi da un momento all'altro.\\n# ~Compendio Completo degli Oggetti Magici~",

    62314: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma traslucida che brilla.\\n# ~Compendio Completo degli Oggetti Magici~",

    62394: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma di un colore che sa di veleno.\\n# ~Compendio Completo degli Oggetti Magici~",

    70751: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma che manda scintille crepitando.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ⚠️ Stesso giapponese di :106766 — vedi NERA_TORBIDA.
    71856: NERA_TORBIDA,

    92062: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma bianca e opaca, a forma di sfera.\\n# ~Compendio Completo degli Oggetti Magici~",

    92797: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma trasparente, con dentro mescolato del rosso.\\n# ~Compendio Completo degli Oggetti Magici~",

    98954: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma viola enorme, come l'occhio di un essere vivo.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ⚠️ Stesso giapponese di :71856.
    106766: NERA_TORBIDA,

    105966: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma azzurra e opaca.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ⭐⭐ L'UNICA DELLE 32 CHE APRE DIVERSAMENTE: il giapponese dice 貴重な杖,
    #     «una bacchetta preziosa», e l'inglese lo lascia cadere. E' la
    #     bacchetta dei desideri, la piu' rara del gioco, e senza quella
    #     parola diventa uguale alle altre trentuno.
    111777: "Una bacchetta preziosa, in cui è chiusa una magia precisa. Ci sta montata sopra una gemma come un occhio di gatto.\\n# ~Compendio Completo degli Oggetti Magici~",

    117679: "Una bacchetta in cui è chiusa una magia precisa. Ci stanno montate sopra tre piccole gemme rosse.\\n# ~Compendio Completo degli Oggetti Magici~",

    119541: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma rossa e opaca.\\n# ~Compendio Completo degli Oggetti Magici~",

    119621: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma gialla e traslucida.\\n# ~Compendio Completo degli Oggetti Magici~",

    122964: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma rossa e traslucida.\\n# ~Compendio Completo degli Oggetti Magici~",

    123044: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma azzurra e traslucida.\\n# ~Compendio Completo degli Oggetti Magici~",

    123204: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma bianca e traslucida.\\n# ~Compendio Completo degli Oggetti Magici~",

    130030: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma trasparente, che pare veda attraverso ogni cosa.\\n# ~Compendio Completo degli Oggetti Magici~",

    # --- le undici con lo SPAZIO prima del `\n` ---

    104942: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma rosso sangue, tagliata a otto facce. \\n# ~Compendio Completo degli Oggetti Magici~",

    105381: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma azzurra che dà una sensazione di freddo. \\n# ~Compendio Completo degli Oggetti Magici~",

    94534: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma che luccica come un minerale. \\n# ~Compendio Completo degli Oggetti Magici~",

    123124: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una sfera ricavata dall'osso di qualcosa. \\n# ~Compendio Completo degli Oggetti Magici~",

    123284: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una piccola gemma rossa a forma di sfera. \\n# ~Compendio Completo degli Oggetti Magici~",

    129950: "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma verde e trasparente, squadrata. \\n# ~Compendio Completo degli Oggetti Magici~",

    # =====================================================================
    # LE BACCHETTE COL SEGNO INCISO NEL LEGNO, non una gemma
    # =====================================================================

    # ⭐ L'unica senza gemma di tutte e 32: il giapponese lo dice
    #    esplicitamente (宝石が付いておらず) prima di descrivere l'asta.
    93149: "Una bacchetta in cui è chiusa una magia precisa. Di gemme non ne ha, e pare un'asta lunga e sottile con la punta aguzza. \\n# ~Compendio Completo degli Oggetti Magici~",

    94102: "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un motivo come di edera intrecciata. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ⭐ 自分の尾を咥えた竜 — il giapponese lo DESCRIVE, «un drago che si tiene
    #    in bocca la propria coda», e non lo nomina; l'inglese lo nomina
    #    («a Uroboros»). La resa descrive, come l'originale: chi non conosce
    #    l'uroboro se lo vede lo stesso.
    96275: "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un drago che si tiene in bocca la propria coda.\\n# ~Compendio Completo degli Oggetti Magici~",

    96355: "Una bacchetta in cui è chiusa una magia precisa. Ci stanno incisi sopra motivi di geometria sacra. \\n# ~Compendio Completo degli Oggetti Magici~",

    98576: "Una bacchetta in cui è chiusa una magia precisa. Sull'asta è intagliato un motivo a graticcio. \\n# ~Compendio Completo degli Oggetti Magici~",

    103505: "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un motivo come di caratteri minuti.\\n# ~Compendio Completo degli Oggetti Magici~",

    117759: "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un motivo a spirale.\\n# ~Compendio Completo degli Oggetti Magici~",

    122821: "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un motivo come di serpenti intrecciati. \\n# ~Compendio Completo degli Oggetti Magici~",
}
