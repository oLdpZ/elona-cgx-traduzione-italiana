# -*- coding: utf-8 -*-
"""Lotto fase4-chara_func-005: le ultime morti, i sette premi di trama e il
cadavere da cui si scende (chara_func.hsp 7000-7999).

35 rese. La zona e' la coda di `dmghp`: finiscono le cause di morte cominciate
nel lotto 003 e comincia **quello che succede quando muore qualcuno di
importante** — le pietre magiche, l'ankh, le ali del caos, il campanello.

⚠️⚠️ **Otto rese su trentacinque erano gia' decise, e `dossier.py` non ne ha
vista NESSUNA.** I sette premi di trama (`:7347`, `:7353`, `:7359`, `:7448`,
`:7454`, `:7460`, `:7473`, `:7605`) dicono 「[愚者の魔石]を手に入れた！」, e
`text.hsp:11576`-`:11630` ha gia' reso **`[愚者の魔石]`** — la stessa parentesi
quadra, lo stesso nome — come `[pietra magica del folle]`. Il dossier non le
aggancia perche' confronta la **stringa intera**, e qui il termine e' annegato
dentro una frase piu' lunga.
💡 **E' il limite dello strumento della 36ª detto con un numero**: `dossier.py`
pesca le rese gemelle, non i **termini** dentro le rese. La regola «cercare
prima di scrivere» qui va fatta ancora a mano, cercando il termine e non la
frase. Otto su trentacinque e' troppo per lasciarla al caso: e' il candidato
naturale al prossimo strumento.
✅ Copiati tutti: `[pietra magica del folle]`, `[pietra magica del
conquistatore]`, `[pietra magica del saggio]`, `[ankh del sole]`, `[chip di
dati]`, `[ali del caos]`, `[registro di dati]`, `[campanello arrugginito]`. Piu'
`<Amurdad>` (`db_creature.hsp:75293`), `<Big Daddy>`, `<Little Sister>`,
«Sentenza di morte» (`buff.hsp:71`) e «flagello degli dei»
(`item_data.hsp:1361`).

⚠️ **`:7037` e' il `valn` della 35ª in una variabile nuova.** `rtvaln` vale
`itemname(...)` — oppure il letterale 「荷物」 che `:7032` gli assegna — quindi
**porta l'articolo italiano dentro**, e l'inglese lo mette dopo «`squashed
by`»: «schiacciato **da lo** zaino». ⚠️ E la rete 8 **non lo vede**, perche' il
suo elenco e' `name|itemname|valn|cdatan` e questa variabile si chiama
`rtvaln`. ✅ Girato col carico **soggetto** — «Il carico schiaccia X sotto il
peso» — che e' la stessa strada di `valn` da soggetto della 36ª.
💡 E il frammento d'epigrafe `:7039` non poteva fare lo stesso, perche' deve
restare predicato del morto: «si accascio' **sotto** il carico», e «sotto» e'
una delle preposizioni che **non si fondono** con l'articolo. Le altre sono
«contro», «per», «tra»: e' la scorciatoia che il progetto non aveva mai
dichiarato, e in questo lotto serve due volte.

⚠️ **`:7787` ha chiesto la stessa scorciatoia e non l'ha avuta.** 「name の死体
から降りた。」 e' «scende **dal** cadavere **di** X», due fusioni in una riga, e
l'inglese ne dichiara **due** `name()` che la rete 11 pretende. ✅ Risolto con
l'**apposizione**: «X scende di sella e lascia a terra Y, ormai cadavere». Il
genitivo sparisce e i due nomi restano tutt'e due.

💡 **Le cinque morti che restavano seguono la regola del lotto 003**: riga di
log al presente, frammento d'epigrafe al **passato remoto**. «si impicco'»,
«mori' per soffocamento», «si accascio' sotto il carico», «perse il Gioco delle
Ombre contro X». ⚠️ E per l'ultima la scorciatoia di «contro» serve di nuovo,
perche' l'avversario e' un `cdatan()` che porta l'articolo.

💡 **闇のゲーム non e' «a card game»: e' il Gioco delle Ombre.** L'inglese di
`:7002` dice «`was sent to Amur-cage by X`» e inventa la gabbia; il giapponese
dice 「闇のゲームで負けた」, che e' la citazione di Yu-Gi-Oh — 闇のゲーム, il
Gioco delle Ombre, che in italiano ha un nome fatto e finito. Reso sul
giapponese, come sempre.
"""
