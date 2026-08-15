# -*- coding: utf-8 -*-
"""Lotto `command-042`: **la bacheca, l'elenco dei PNG, le prenotazioni e il
jukebox**. Ventotto rese, da `:3120` a `:3845`, più sei voci tenute fuori. Con
questo la zona 3000-3999 si chiude, ed è la terza della sessione.

⚠️⚠️⚠️ **Le sei fuori sono il nodo `CDATAN_NEWSEX` che la 46ª aveva segnalato —
e la lezione della sessione è che NON era da decidere: era già deciso dalla Fase
0, e io stavo per deciderlo una seconda volta in un altro modo.**
`invariati.md` ha dal **2026-08-07** una sezione intera intitolata «Valori di
dato, non testo — tradurli rompe i salvataggi», che nomina per riga proprio
`command.hsp:3639-3654` e dichiara invariate `male`, `female`, `none`,
`hermaphrodite`, `male?`, `female?`, `trans-male`, `trans-female`. E
`text.hsp:123` ha già in dizionario `en='male'` con `it='male'`.
❌ La prima stesura di questo lotto le **rinviava**, con tanto di motivo scritto.
Il motivo era giusto e la mossa sbagliata: una rinviata resta aperta per sempre e
ritorna a galla a ogni sessione, mentre queste sei sono **chiuse da nove mesi** —
mancava solo la riga in dizionario. Le mette
`scratchpad/invariati-command-newsex.py`, fuori dal lotto perché la rete 7 le
ferma (sono confronti) e ha ragione a fermarle: quel che non sa è che per questa
famiglia c'è una decisione più specifica.
💡 **La lezione è più larga del caso**: prima di scrivere il motivo di un rinvio,
si cerca il valore in `invariati.md`. Il motivo che stavo per scrivere era una
riscoperta, non una scoperta.

⚠️ Perché la famiglia non si traduca, comunque, vale la pena riassumerlo: il
valore di `CDATAN_NEWSEX` fa **quattro mestieri con una firma sola** — etichetta
di menu (`:4653`-`:4656`), valore **salvato** (`:4678`-`:4690`, `:4707`), chiave
di confronto (qui, in `init.hsp:1813`-`:2008` dentro `he()`/`his()`/`him()`, e in
`text.hsp:359`-`:375`) e testo stampato nudo (`:3640`-`:3655`, `:17834`,
`init.hsp:2085`). Un salvataggio inglese contiene la stringa inglese.
✅ E che sia così lo dice upstream: `init.hsp:1816` confronta con «male?» **e**
«trans-male», cioè tiene un ramo di compatibilità per il nome vecchio.

💡 **Una cosa nuova però c'era, ed è finita in `invariati.md`: `bisexual`.**
`:3639` confronta `CDATAN_NEWSEX` con «bisexual», ma chi il valore lo **scrive**
— `chara.hsp:2790` e `command.hsp:4686` — scrive «hermaphrodite». Il ramo è
**morto nella build inglese**, e con lui la riga di stampa `:3640`; in giapponese
la stringa è 「両性具有」 da tutt'e due le parti e funziona. È il gemello esatto di
`hermaphorodite`, che sta in quella lista dal 2026-08-07 per la stessa ragione.

⭐⭐ **Sette rese su ventotto sono state riscosse, non decise.** 「情報」 è
«Informazioni» (`:6147`), e la rete 3 lo pretende; 「 gold」 è « oro»
(`text.hsp:193`), stesso giapponese; ガードブレイク è **«Rottura guardia»**
(`skill.hsp:957` e `:1789`); 依頼 è «Incarico» (`text.hsp:11875`) e 依頼人
«cliente» (`:11877`); 掲示板 è «bacheca» (`db_item.hsp:151223`); 予約 è «Prenota»
(`text.hsp:135`); ジャーナル è «diario» in cinque file.

⭐ **`:3643` invece si traduce, e la rete 7 lo conferma da sola.** 「性別不明」 /
«unknown» non è mai una chiave: `:4656` la usa come **etichetta** di menu, ma la
scelta 5 scrive `lang("なし", "none")`, non «unknown». Ed è già resa
«sconosciuto» in `init.hsp:2082`, dove `gendername()` la restituisce: si ricopia.
💡 Provata la rete 7 riga per riga sulle sette: confronto a `:3639`, `:3642`,
`:3645`, `:3648`, `:3651`, `:3654`; **passa** a `:3643`. Esattamente il taglio
giusto.

💡 **Quattro rese sono invariati, e sono dichiarati in `invariati.md`, non fatti
passare.** `$` e `$ x ` (`:3392`, `:3397`) sono il simbolo della ricompensa in
bacheca, dove il giapponese usa 「★」: l'inglese ha scelto un altro segno e
l'italiano non ne ha un terzo. `(` e `)` (`:3634`) sono punteggiatura.
⚠️ **E la parentesi non è pigrizia, è misura**: la riga dell'età vive in **19**
caratteri, fra `wx + 372` e la colonna dei valori a `wx + 512`, e
«Lv.100 female?(999)» ne fa esattamente 19. « anni)» ne costerebbe cinque.

💡 **Le altre larghezze, col corpo giusto del lotto 041.** Le intestazioni passano
da `display_topic`, corpo 11 e 26 px d'icona: «Informazioni» ha 17 caratteri fra
`wx + 350` e `wx + 490`, «Assunzione (paga)» ne ha 21 fra `wx + 490` e il bordo,
«Stato» ne ha 12. Le righe girano invece a corpo 12 (`:3589`, `14 - en * 2`),
7,2 px: quella di `allyctrl == 4` — «Hp:100%» più «/contrasto/» (`:1356`, già
spedita) più « Rottura guardia:100%» — fa **39 caratteri su 44**, contro i 33
dell'inglese.
"""
