# -*- coding: utf-8 -*-
"""Le rese del lotto 061 — LE MERCI DA COMMERCIO: `FILTER_CARGO_TRADE` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 061 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa061.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 061`: **19 righe su 19** hanno lo spazio prima del
`\\n`, e tutte e 19 le code hanno lo spazio dopo il `#`. E' il lotto piu'
uniforme finora su questo punto.
⚠️⚠️ «senza lo spazio prima del `\\n`» NON vuol dire «senza il `\\n`»: il
`\\n` c'e' sempre. E' l'errore che il preflight ha preso nel lotto 059.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 061`: **+19** per 19 rese,
nessuna gemella. ⓘ `_gia-reso.py 061`: 0 su 19; `_120-serie-bacchette 061`:
nessun giapponese ripetuto, 0 aggettivi che distinguono.

⚠️⚠️⚠️ **MA LA SERIE C'E' LO STESSO, E NESSUNO STRUMENTO LA VEDE**: undici
righe su diciannove aprono la frase con 交易品 — «una merce da commercio
[aggettivo]» — e cinque di quelle undici chiudono con la stessa formula
使用することはできない. Le rese tengono la stessa impalcatura: la merce apre la
frase, e il divieto d'uso si rende sempre «Non si può usare: ...».
`_120-serie-bacchette` tace perche' raggruppa per prosa intera.

⚠️⚠️⚠️ **E C'E' UNA COPPIA SORELLA DENTRO IL LOTTO**: `:103913` (ツナ, il
tonno) e `:104045` (マンボー, il pesce luna) hanno il giapponese identico
tranne il nome del pesce. Le due rese sono identiche tranne il nome, di
proposito: e' la lezione della 119a applicata prima che il difetto nasca.

⚠️⚠️⚠️ **`:56267` — L'INGLESE DI MONTE E' QUELLO DELL'OGGETTO DOPO.** La
`description(0)` inglese del dipinto dell'eruzione e' la copia **letterale**
della zampa di coniglio (`:56333`), parola per parola. Il giapponese e'
quello giusto, e la `description(3)` inglese («It is a cargo of painting.»)
pure: monte ha sbagliato solo quella riga. **La resa viene dal giapponese**,
ed e' il precedente della 110a.
ⓘ **La rete 13 del lotto l'ha vista**, perche' le due righe stanno tutt'e due
qui dentro. Quel che manca e' la stessa domanda su **tutto il file**:
`_103-inglese-ripetuto` e `_104-inglese-slittato` la fanno, ma leggono **solo
`db_card.hsp`** (`FILE = 'db_card.hsp'`, prima riga di tutt'e due). Se le due
righe fossero finite in due lotti diversi, niente avrebbe protestato.
"""

IT = {
    # =====================================================================
    # I DUE OGGETTI DEL PRIMO TITOLO — ～イムウエル交易譚～
    # =====================================================================
    # ⚠️⚠️⚠️ :56267 e' la riga con l'inglese SBAGLIATO di monte (vedi la
    #    testa): l'inglese di quella riga racconta la zampa di coniglio, il
    #    giapponese il dipinto. Si rende dal giapponese.
    # ⓘ 版画 e' la STAMPA, non il dipinto, e il progetto la rende cosi'
    #    gia' altrove (il quadro di Ehekatl, in questo stesso file: «si
    #    indebito' per stamparne una gran quantita'»). Il NOME dell'oggetto
    #    resta «dipinto dell'eruzione», che viene dall'inglese ed e' gia' in
    #    gioco: la descrizione non lo contraddice, lo specifica.
    # ⓘ 違う意味で伝説の一品 e' l'ironia della riga: leggendario si', ma
    #    non per il motivo che uno crede.

    56267: "Una stampa che dicono disegnata sul posto, durante l'eruzione: un pezzo leggendario, ma in un altro senso. Da quella scena, che pare la fine del mondo, arrivano un calore soffocante e tutto il suo furore. \\n# ~Racconti di Commercio di Aimwell~",

    # ガイアス・ヴィス -> «Gaius Vis» (dizionario, decine di battute).
    56333: "In certe zone di Gaius Vis il portafortuna è la zampa del coniglio, non la coda. Si tramanda da tempi antichi, e fra gli avventurieri va per la maggiore come compagna di viaggio. \\n# ~Racconti di Commercio di Aimwell~",

    # =====================================================================
    # LE MERCI CHE VENGONO DA LONTANO — nomi di luogo gia' in gioco
    # =====================================================================
    # サウスティリス -> «Tyris del Sud», マリモ -> «marimo» (il nome
    # dell'oggetto e' gia' «marimo»: la parola si tiene).

    73894: "Marimo che cresce nel lago di Tyris del Sud, strappato e poi arrotondato a mano. Per fabbricarlo se ne raccoglie tanto che il marimo del lago rischia l'estinzione. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # イェルス軍 -> «l'esercito di Yerles» (dizionario). 観賞用 e' il filo
    # della riga: una razione da vetrina, non da mangiare.
    73960: "Una vecchia razione militare che l'esercito di Yerles ha ceduto ai civili come soprammobile. Come cibo è andata a male da un pezzo. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ノイエル -> «Noyel» (dizionario). とても重い -> «molto pesante», come
    # l'indice 3 della tomba: 重い e' «pesante», とても重い e' «molto
    # pesante», e la scala si tiene distinta.
    91026: "Una merce da commercio molto pesante: un abete abbattuto e carico di addobbi. La comprano, dicono, quelli che a Noyel non ci possono arrivare e vogliono festeggiare a casa loro. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # =====================================================================
    # LA COPPIA SORELLA: due pesci troppo grossi per uno solo
    # =====================================================================
    # ⭐⭐ 個人で食すには余りにも巨大な◯。主に交易品として取引される。
    #    Il giapponese e' identico tranne il nome del pesce, e le rese lo
    #    sono di proposito. ツナ -> «tonno», マンボー -> «pesce luna»
    #    (dizionario, due voci).

    103913: "Un tonno decisamente troppo grosso perché una persona sola se lo mangi. Si tratta soprattutto come merce da commercio. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    104045: "Un pesce luna decisamente troppo grosso perché una persona sola se lo mangi. Si tratta soprattutto come merce da commercio. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # =====================================================================
    # LA FAMIGLIA DEL DIVIETO D'USO — 使用することはできない, cinque volte
    # =====================================================================
    # ⭐ Cinque righe chiudono con la stessa formula, e il giapponese
    #   cambia solo la RAGIONE del divieto. Tutte e cinque rendono
    #   «Non si può usare: <ragione>», cosi' che il giocatore riconosca la
    #   regola e legga solo la parte che cambia.
    # ⚠️ E il giapponese distingue due gradi che l'italiano tiene:
    #   :103847 dice 価値が大幅に落ちる (il valore CROLLA), :104375 dice
    #   価値が下がる (il valore CALA). Appiattirli sarebbe la 119a al
    #   rovescio.

    86266: "Una merce da commercio con dentro tutto l'occorrente per dipingere. Non si può usare: ad aprirla, i colori e il resto finiscono sparsi dappertutto. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    103847: "Una merce da commercio che fa piacere ricevere. Non si può usare: ad aprirla, il valore crolla. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # 先約がいる e' la battuta nera della riga: la bara e' gia' prenotata.
    104111: "Una merce da commercio fatta con cura, in legno di qualità. Non si può usare: c'è già chi l'ha prenotata. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    104177: "Una merce da commercio legata stretta. Non si può usare: se si scioglie, sono guai. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    104375: "Una merce da commercio impacchettata con cura. Non si può usare: ad aprirla, il valore cala. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # =====================================================================
    # LE ALTRE MERCI, tutte aperte da «Una merce da commercio...»
    # =====================================================================

    86332: "Una merce da commercio che mette insieme alla rinfusa quadri di artisti diversi. Detto questo, il minimo della conservazione c'è, e non risulta che qualcuno l'abbia aperta davanti al compratore trovandoci dentro roba senza alcun valore. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # とぼけた表情 e' l'aria svagata del pupazzo, e 癒し il conforto che da'.
    90960: "Una graziosa merce da commercio fatta di neve. Quell'aria svagata consola, e pare che in molti la comprino per questo. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # 浮き輪 -> «salvagente» (dizionario, tre voci). 捌きにくい e' il
    # difficile da smerciare, non il difficile da maneggiare.
    103715: "Una merce da commercio fatta di salvagenti legati in più mazzi. Sciolti diventano difficili da smerciare, e infatti non si vendono a uno a uno. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # 機巧 e' il congegno meccanico: e' un giocattolo che si guarda muovere.
    103781: "Una merce da commercio con dentro un congegno complicato, che diverte chi la guarda. È pesante, e a maneggiarla ci vuole attenzione. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ⭐ 墓運びが墓に埋もれる e' un gioco di parole del giapponese — chi
    #   porta la tomba finisce sotto la tomba — e si puo' tenere in
    #   italiano ripetendo la parola.
    103979: "Una merce da commercio di pietra, molto pesante. Meglio non strafare: non sia mai che chi porta la tomba finisca sepolto sotto la tomba. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # 所詮観賞用 e' la stessa idea della razione: costruito per far scena.
    104243: "Una merce da commercio dai colori vivaci, molto pesante. Il suono lo fa, ma in fondo è roba costruita per far scena, e a usarla sul serio non si va da nessuna parte. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    104309: "Una merce da commercio lucidata al punto che ci si vede dentro. Ogni pezzo è fatto a mano, in versione di lusso. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",
}
