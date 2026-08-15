# -*- coding: utf-8 -*-
"""Lotto `command-037`: **la finestra dell'inventario e il banco del negozio**.
Ventidue rese, da `:14211` a `:14717`.

⭐ **La zona 14000-14999 sta tutta dentro una routine sola**: `*com_inventory_loop`
va da `:13971` a `:15990`, e la 15000-15999 è già chiusa. Non c'è nessuna
famiglia tagliata a metà — la trappola del lotto 031 — e le due intestazioni
delle resistenze di `:14127`/`:14136`, che la 47ª segnalava come primo scoglio
della zona, sono **già rinviate**: la zona da fare comincia a `:14211`.

⭐⭐ **Le cinque etichette della finestra hanno tutte un tetto calcolabile, e per
la prima il carattere NON è quello di corpo 12.** `:14203` scrive
`font lang(cfg_font1, cfg_font2), 12 + en - en * 2, 0`, e `config.hsp:439` mette
`en = 1` nel ramo inglese: fa **corpo 11**, cioè 6,6 px a carattere e non 7,2.
È esattamente l'avvertimento che il collaudo della 47ª ha lasciato scritto —
**il corpo va letto sulla riga, non dato per scontato**.
- `:14211` «Equip:» sta fra `x = wx + 40` (`:14208`) e `x += 60` (`:14212`), da
  dove partono i `bodyn`: **60 px / 6,6 = 9 caratteri**. «Parti:» ne fa 6.
- `:14272` e `:14275` finiscono in `s(1)`, che `:14352` **allinea a destra** con
  `pos wx + 600 - strlen(s(1)) * 7`. ⚠️ Il 7 è di monte ed è **stretto**: il
  corpo lì è quello di `:14243`, `14 - en * 2` = 12, cioè 7,2 px. Una resa di L
  caratteri parte a `wx + 600 - 7L` e finisce davvero a `wx + 600 + 0,2L`, cioè
  sfora di un pixel ogni cinque caratteri. Con « pz.» il conto non si pone.
- `:14280` e `:14325` si **appendono al nome dell'oggetto**; a destra il peso
  occupa cinque o sei caratteri fino a `wx + 600`, quindi nome più coda devono
  stare sotto i ~65 caratteri. « (per terra)» costa due caratteri più di
  « (Ground)»; « (tiro)» ne costa due **meno** di « (Range)».

⭐ **Nessuna delle parole si è dovuta scegliere: erano già decise tutte.**
「部位」 è «Parte» in `:12620` («Parte/Nome») e «Parti» in `:1273`; 「足元」 è
«per terra» in `:6703`, `:6707` e `map.hsp:9914`; 「遠隔」 è **«Tiro»** in
`text.hsp:136`, e `:15309`/`:15312` lo declinano già «da Tiro» e «nel Tiro»
parlando proprio di questo slot.

⚠️⚠️ **E la rete 4 ha fermato le due etichette del banco delle medagliette, e
aveva ragione.** `:14272` e `:14275` hanno lo **stesso giapponese**, 「 枚」, che è
un puro classificatore; l'inglese ci mette «Coins» e «Tickets» perché il ramo
`invctrl(1)` è diverso. Ma la distinzione **la porta già l'intestazione della
colonna** — `:14105` «Medagliette», `:14108` «Biglietti», disegnate a `wx + 526`
sopra questi stessi numeri — e ripeterla nel valore è quello che fa l'inglese,
non quello che fa il gioco. ✅ Resa unica, « pz.»: è il classificatore italiano,
ed è l'unica forma che regge anche il valore **1**, dove « pezzi» non reggerebbe.
È la stessa lezione di `:7818`/`:7828` nel lotto 036 — a distinguere i rami è il
codice, non il testo.

⚠️⚠️ **`:14531`, `:14643` e `:14646` sono tre inglesi IDENTICI dove il giapponese
distingue, e la distinzione si può riprendere senza toccare il contratto.**
Tutt'e tre dicono «How many? (1 to N)»; il giapponese dice 「いくつ落とす？」,
「いくつ買う？」, 「いくつ売る？」 — quante ne lasci, ne compri, ne vendi. Il
giapponese lo fa nominando l'oggetto con `itemname(ci, 1)`, e **quello non si
può fare**: la rete 11 non lascia aggiungere una funzione che l'inglese non ha.
Ma il verbo non è una funzione. ✅ Quindi «Quanti ne lasci?», «Quanti ne compri?»,
«Quanti ne vendi?»: la distinzione torna, il contratto resta `['inv']`.

⚠️ **`:14487` è l'unica resa che ha dovuto cambiare forma per un accordo.**
`name_of_seed_planted` viene da `ioriginalnameref` (`:14455`) ed è un nome
**singolare** — «seme di erba», «seme di frutto» — mentre
`number_of_seeds_planted` può valere 1 come 30. «Hai piantato 3 seme di erba» è
sgrammaticato in italiano quanto «You've planted 3 seed of herb» lo è in inglese,
ma qui si può evitare: «Semi piantati: 3 (seme di erba).» regge tutt'e due i
numeri, perché l'etichetta non concorda con niente. È la forma di `:78` nel lotto
001 («tipi di oggetti»), cioè un nome infilato fra il numero e la variabile.
💡 E le due variabili non sono chiamate: `funzioni_di_contenuto` dell'inglese è
vuota, quindi qui la rete 11 non chiede niente.

⭐ **Riscosse senza decidere due rese e una parola.** `:14717` ha lo **stesso
giapponese** di `action.hsp:3386` ed è ricopiata parola per parola — «Puoi ancora
reclamare … oggetti in eredità» — e da lì viene anche «eredità» per `:14616`.
⚠️ Nell'inglese di `:14717` c'è `_s3(...)`, che è morfologia: sparisce insieme al
suo argomento, e il contratto resta il solo `gdata` di testa.
La parola «portafogli» (`:14683`, `:14692`) la scrive così `proc.hsp` in cinque
righe — `:3389`, `:9474`, `:9482`, `:21991`, `:21994` — mentre
`db_item.hsp:148929` dice «portafoglio»: nel registro del log vince `proc.hsp`.
💡 E le due rese del portafoglio sono **la stessa frase in due persone**: `:14683`
è il giocatore («Apri il portafogli e chini la testa…»), `:14692` è chi vende
(`name(tc)` in tutt'e due le lingue, quindi terza persona per la regola di
`init.hsp:1704`).

💡 **Un inglese che copre due giapponesi diversi, e la rete 13 lo dirà.**
«The container is full.» sta per 「これ以上入らない。」 (`:14569`, non ci entra) e per
「これ以上置けない。」 (`:14583`, non ci si può posare): due contenitori diversi,
stesso evento per chi gioca. Le due rese sono **volutamente identiche**.
"""
