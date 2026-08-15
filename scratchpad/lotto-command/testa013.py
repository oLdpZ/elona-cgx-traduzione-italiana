# -*- coding: utf-8 -*-
"""Lotto `command-013`: le 36 voci del menu che si apre su un compagno, piu' una
rinviata.

E' il menu che compare puntando un alleato, una bestia del ranch, un
prigioniero o un sacco da pugni: dai un nome, insegna a parlare, cambia
l'aspetto, sciogli la coppia, e — se e' bestiame — **scuoia**. Trentasette
`promptAdd` in un `if` a testa, tutti dentro `*com_chara`.

⭐⭐ **E qui il budget non e' una stima: e' il modello di `larghezze.py`
applicato a mano.** `command.hsp:6172` fa `val = promptx, prompty, 275, 1`
prima di `gosub *prompt_key`, quindi il riquadro e' largo **275 px** e
`larghezze.budget(275)` da' **29 caratteri**. E' la stessa formula che misura i
75 menu di `text.hsp` — solo che `larghezze.py:68` legge un file solo e questo
non lo vede. ⚠️ Se un giorno la guardia imparasse a leggere piu' file, questo
lotto e' gia' dentro il tetto: la resa piu' lunga ne fa 28.
💡 L'inglese piu' lungo ne fa 27, quindi le due misure — il modello e
`tetto-en.py` — dicono la stessa cosa. E' la prima zona della sessione in cui
si possono confrontare.

⚠️ **DUE righe sono commentate, e la seconda l'ha trovata la rete 6.** `:6148`
e' `; promptAdd lang("カスタムＡＩ", "Custom AI"), "null", 998` — la voce «Custom
AI» esiste nel sorgente ma non nel menu — e l'avevo vista leggendo. `:6070`
«Item mark adjust» no: sta dentro un `if` spento a tre righe (`:6069`-`:6071`,
`;` su tutt'e tre) in mezzo a quattro comandi vivi, e a occhio si perde.
✅ Sono le **prime due rinviate della sessione**, dopo nove lotti che non ne
avevano avuto bisogno. 💡 E il conto dice la cosa piu' utile: **una l'ho vista
io e una l'ha vista la guardia**, che e' esattamente il motivo per cui la
guardia esiste.

⚠️ Delle quattro voci «Item mark», quindi, ne restano tre: si mette l'icona, la
si sposta, la si toglie. **Regolarla non si puo'**, e il menu non lo offre.

⚠️ **Due inglesi stanno per due giapponesi diversi, e sono due comandi
diversi.** «Release» e' 「縄を解く」 a `:6110` — il sacco da pugni, che e'
*legato con una corda* — e 「檻から解き放つ」 a `:6116`, il prigioniero *in
gabbia*: «Slega» e «Libera dalla gabbia». «Information» e' 「能力の開示」 a
`:6144`, che apre la scheda delle capacita' di un alleato, e 「情報」 a `:6147`,
che e' il dump di sviluppo dietro `if ( develop | gdata(GDATA_WIZARD) )`:
«Mostra le capacita'» e «Informazioni».

💡 **Due nomi non possono avere un genere**, e la strada e' l'aggettivo
invariabile: 「大事な仲間に指定」 non e' «segna come prezioso» — che
concorderebbe col compagno — ma «Metti fra gli **indispensabili**», col suo
contrario «Togli dagli indispensabili».

⭐ **「闇のゲーム!」 ha un nome italiano gia' fatto e non e' «Play TCG (Lethal)».**
E' la citazione di *Yu-Gi-Oh!*, che in italiano e' il **«Gioco delle Tenebre»**;
e 「決闘!」 e' «Duello!», non «Play TCG!». L'inglese spiega la meccanica, il
giapponese fa la citazione — e qui vince il giapponese, che e' anche piu' corto.

Tetto 29 caratteri. Zero copie di giapponese, una di inglese.
"""
