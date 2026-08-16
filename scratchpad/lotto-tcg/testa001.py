# -*- coding: utf-8 -*-
"""Lotto fase4-tcg-001: il tavolo del duello e la fine della partita
(tcg.hsp, righe 0-2999).

33 rese, e sono le prime `lang()` mai tradotte dei file del gioco di carte.
⚠️ **`tcg.hsp` non era nel perimetro**, e non per una svista: i file del
dizionario erano diciannove e nessun `tcg` fra loro. La 52ª ha chiuso le righe
**nude** di `tcg.hsp` e `tcg_custom.hsp` e la ripresa li ha chiamati «finiti» —
che era vero per quel che il referto guardava, e falso a schermo.

⭐⭐⭐ **A dimostrarlo e' stato il collaudo, alla prima schermata.** La finestra
«a Proper Deck» — quella che esce quando il mazzo ha meno di 30 carte, cioe' la
prima che vede chiunque provi il gioco — mostra un paragrafo inglese con
**incollata in coda una frase italiana**:

    :2560  buff  = lang("…", "I should make sure my deck has at least 30…")
    :2563  buff += "A Miches di Vernis piacciono tutti i giochi da tavolo…"

⭐ **E' una classe nuova: un letterale nudo che si SOMMA a una `lang()`.** Le
«due letterali per riga» della 51ª stavano sulla stessa riga e si vedevano; qui
stanno a tre righe di distanza, in due reti diverse — una dentro il perimetro,
l'altra fuori — e finiscono nello **stesso paragrafo**. Tradurre solo la meta'
che il referto vede da' un risultato **peggiore** di lasciare tutto inglese.
💡 La stessa forma torna identica alla fine di ogni partita: `:2803` e' gia'
italiano («Esito imprevisto…») e i ventuno esiti veri di `:2804`-`:2821` sono
inglesi. Titolo italiano, corpo inglese, bottone inglese.

⚠️ **`:1505` e' rinviata perche' e' MORTA, e nessuna rete l'avrebbe fermata.**
La riga e' `// rtvaln += lang("  ランク:", "  Rank:") + cardrefcost`: un
commento `//`, che in HSP spegne la riga come il `;`. La rete 6 guarda il `;` e
i blocchi `/* … */` e **non guarda `//`** — quarta famiglia di riga morta dopo
il `;`, il blocco e il ramo `if ( jp )`. Misurata con `scratchpad/barre_spente.py`:
**9 in tutto il sorgente, e una gia' tradotta** (`command.hsp:17515`), cioe'
lavoro gia' speso su testo che nessuno legge.

⚠️ **`:2470` e' rinviata per l'ORDINE DELLE PAROLE, e vuole una toppa.** Il menu
dei mazzi si compone cosi': `s@tcg(cnt) = lang("白", "White")` e poi
`s@tcg(cnt) += lang("のデッキ", " Deck")`. In italiano il nome viene **prima** del
colore, quindi la resa sta tutta nel colore — «Mazzo bianco» — e a `:2470` non
resta niente da dire. Una resa vuota non e' esprimibile (`firme_tradotte` la
conta come non tradotta), quindi la riga si spegne con una toppa.
💡 E sulla stessa schermata ci sono altri tre letterali nudi che nessun referto
elencava — `" (NG 12/30)"` a `:2478` e `:2481`, `" [Use]"` a `:2484` — perche'
`s@tcg(cnt) +=` porta il **suffisso di modulo**: `s@tcg` non e' `s`.

⭐ **«Sarà per la prossima volta.» non e' stata scelta: e' stata trovata.**
`db_creature.hsp:46267` rende cosi' 「また今度ね」, ed e' lo stesso giapponese di
tutte e quattro le occorrenze qui. ⚠️ Ma `:2786` e `:2791` hanno **lo stesso
giapponese e un inglese diverso** — «To the Amur-cage you go!» e
«Noooooooooooooo!» — perche' il mod ha riusato la `lang()` senza toccare il
primo argomento: li' si segue l'inglese, che e' la lingua di monte della resa.

⭐ **«gabbia di Amur» viene dalla 52ª**, che l'aveva resa per la prima volta in
tutto il progetto a `tcg_custom.hsp:1608`.

⚠️ **«Noooooooooooooo!» resta identica, e va detto perche' non e' una
dimenticanza**: e' un urlo, si scrive uguale nelle due lingue. Stessa scelta di
«Mana», «Immune» e «Abnormal».

💡 **Il tetto dei due menu si misura, e `larghezze.py` non lo fa.** I menu di
`tcg.hsp` si costruiscono con `promptAdd` e non con `s(cnt) = lang()` dentro un
`#deffunc`, quindi la forma che lo strumento cerca non c'e'. Ma il riquadro e'
lo stesso — `*prompt_key@` in HSP e' l'etichetta del **modulo principale**, cioe'
proprio `*prompt_key` — e vale lo stesso metro, `(pixel − 46) / 7,7`:

    :2499  riquadro da 240px  ->  25 caratteri   «Costruisci il mazzo» (19)
                                                 «Imposta come principale» (23)
"""
