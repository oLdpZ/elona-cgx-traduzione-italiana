# -*- coding: utf-8 -*-
"""Le rese del lotto 069 — LE SCARPE: `FILTER_BOOTS` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 069 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa069.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 069`: **9 righe su 9** con lo spazio prima del `\\n`,
9 su 9 con lo spazio dopo il `#`.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 069`: **+9** per 9 rese,
nessuna gemella.

⭐⭐⭐ `_122-sorelle-per-frase`: **otto** frasi con una sorella, sei gia' rese.
`:130450` e' la **sesta e ultima** riga della famiglia dei materiali speciali,
che questa sessione ha scoperto avere sei membri invece di tre. E `:100586` e
`:100651` condividono **la seconda frase parola per parola**: la resa la tiene
identica costruendola in forma impersonale, cosi' il soggetto diverso delle due
righe non la fa divergere.
"""

IT = {
    # =====================================================================
    # LA FAMIGLIA DEI MATERIALI SPECIALI — SESTA E ULTIMA
    # =====================================================================
    # ⭐⭐⭐ :100849 scudo (058), :101769 corazza (060), :99872 elmo (063),
    #    :101114 guanti (066), :100392 cintura (068), :130450 stivali (069).
    #    La famiglia si chiude qui.
    # ⓘ 非常に硬く -> «durissimi», la stessa parola del frassino (`:95484`,
    #   lotto 062), dove il giapponese diceva anche li' 非常に硬く.
    # ⚠️ Il NOME dell'oggetto e' «stivali compositi», e la resa apre con
    #   «Degli stivali» come vuole la regola della famiglia: il pezzo si
    #   chiama col nome che il giocatore legge in cima al pannello.

    130450: "Degli stivali che, incrociando materiali speciali, hanno ottenuto una protezione più solida. Sono durissimi, e dicono che al solo camminare mandino intorno un suono piacevole. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # LA COPPIA CHE CONDIVIDE LA SECONDA FRASE
    # =====================================================================
    # ⭐⭐⭐ 戦闘用にはやや心もとないが、日常的に使用するにはこれくらいで十分だ
    #    sta identica in tutt'e due. Il giapponese non ha soggetto, e in
    #    italiano i due soggetti sarebbero diversi — «delle calzature»
    #    (plurale) e «un'armatura» (singolare) — quindi il verbo cambierebbe
    #    e la frase condivisa si spezzerebbe.
    #    💡 Rimedio: forma IMPERSONALE, «c'è poco da fidarsi», che regge
    #    tutt'e due i soggetti e resta identica parola per parola.
    #    Senza la rete questa coppia non si sarebbe vista.

    100586: "Delle calzature che coprono il piede per intero. Per il combattimento c'è poco da fidarsi, ma per l'uso di tutti i giorni tanto basta. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⓘ E questa e' anche una variante della famiglia 〜を守る為に作られた
    #   (testa 063, collo 064, polso 066), col 簡易的に in piu': «fatta alla
    #   buona». La rete l'accosta a `:99937` a 0.76.
    100651: "Un'armatura fatta alla buona per proteggere i piedi. Per il combattimento c'è poco da fidarsi, ma per l'uso di tutti i giorni tanto basta. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # LE ALTRE SCARPE
    # =====================================================================
    100456: "Delle scarpe che coprono per intero dal piede alla gamba. Quella struttura, che non lascia scoperto un varco, punta alla protezione perfetta; ma le cose di quel genere, si sa, pesano tutte. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    100521: "Delle scarpe fatte bene. In quella cura si sente quanto ci ha tenuto l'artigiano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    130515: "Delle scarpe a cui sono stati applicati moltissimi pezzetti di materiale. Pesano più del normale, è ovvio, ma in cambio la protezione ne esce più dura. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # I PEZZI UNICI 《…》
    # =====================================================================
    # 大地の神 -> «il dio della terra» (dizionario, il pendolo che lo
    # raffigura). 足枷 -> «ceppi», e l'indice 3 di questo stesso oggetto dice
    # gia' «Se lo indossi, si trasforma in ceppi».
    76115: "L'attrezzo da allenamento del dio della terra. Non è che pesi, eppure a metterlo addosso non ci si muove quasi più, e viene perfino la sensazione di essere fissati alla terra. \\n# ~Dizionario Fantastico di Irva~",

    # ⓘ 唯一無二の友 e' «l'amico che non ha pari»: il giapponese e' enfatico e
    #   l'inglese pure («your one and only friend»).
    86867: "Delle scarpe solide, fatte di cuoio. Si adattano al piede più di quanto ci si aspetti, e in un viaggio lungo diventeranno l'amico che non ha pari. \\n# ~Dizionario Fantastico di Irva~",

    # 行商人 -> «mercante ambulante» (dizionario, tre voci). 伊達ではない e'
    # «non è una vanteria», e il giapponese lo dice per rassicurare.
    93757: "Delle scarpe su cui è stata posata una magia che fa correre in un istante distanze lunghissime. E non è una vanteria: pare che un mercante ambulante di gran fama, grazie a queste scarpe, abbia girato il mondo in lungo e in largo e si sia guadagnato la posizione che ha oggi. \\n# ~Dizionario Fantastico di Irva~",
}
