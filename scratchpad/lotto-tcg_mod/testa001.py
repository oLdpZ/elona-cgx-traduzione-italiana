# -*- coding: utf-8 -*-
"""Lotto fase4-tcg_mod-001: gli otto domini del gioco di carte, e **chiude
`tcg_mod.hsp`** (tcg_mod.hsp, righe 3479-3486).

Otto rese, tutte di una parola. Sono i «colori» del gioco — il concetto che in
Magic si chiama colore e che qui si chiama dominio, come la 52ª ha gia' fissato
traducendo `Domain` con «Dominio» nel pannello del tavolo.

⚠️ **Prima di tradurle ho cercato chi le CONFRONTA, e non le confronta
nessuno.** E' la disciplina della 52ª sulle dodici classi di `custom_ai.hsp`:
un'etichetta che qualcuno usa come chiave non e' testo. Qui i quattro siti sono
tutti d'uscita — `tcg.hsp:3488` (il pannello della carta), `:3544` (le schede
della colonna), `:4661` (l'esportazione dell'elenco carte, dentro `cnvcase`) —
e il dominio vero viaggia come **numero**, `cardrefdomain`, non come parola.

💡 **Il tetto sta nel `sdim`, in due punti, e vince il piu' stretto.**
`tcg_mod.hsp:3466` dichiara `sdim domname@tcg, 20, 10` (19 caratteri), ma questi
otto finiscono anche dentro `cfname@tcg`, che `tcg.hsp:3543` dichiara
`sdim …, 16, 10`: **quindici**. «LEGGENDARIO» ne fa 11 ed e' il piu' lungo.

⚠️ **Le schede in cima all'editor NON sono queste**, e non vanno confuse. Quando
il filtro e' per dominio, `tcg.hsp:3557` **riscrive** `cfname@tcg` con dei
letterali **nudi** — `"Blue", "Green", "White"…` — che dicono le stesse parole
ma non passano da nessuna `lang()`. Quelli vogliono una toppa, e hanno un tetto
diverso e molto piu' stretto: la linguetta e' un'immagine da **63 px**
(`gcopy 7, 360, 96, 63, 20`) col testo a corpo 9, cioe' una dozzina di caratteri.

⭐ **«NEUTRO» e non «NEUTRALE».** Il giapponese e' 中立, che vale tutt'e due, ma
qui la parola qualifica una carta — «una carta neutra» — e non una persona che
si dichiara neutrale. ⭐ **«LEGGENDARIO» e non «LEGGENDA»**: 伝説 e' il
sostantivo, ma l'inglese ha scelto l'aggettivo e la parola sta accanto ad altri
sette aggettivi di colore.
"""
