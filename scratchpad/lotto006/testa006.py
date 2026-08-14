# -*- coding: utf-8 -*-
"""Lotto fase4-chara_func-006: i versi del dolore, il corpo che cambia e chi si
sdoppia (chara_func.hsp 8000-8999).

27 rese. Il blocco del corpo: peso, statura, vomito, anoressia, i presentimenti
del cibo e la scissione.

⭐ **`:8317` e' una delle righe dello screenshot della 39ª, ed era gia' decisa.**
「は漏らした。」 sta anche a `chara_func.hsp:3377`, reso «X se la fa addosso.»
nel lotto 001 di ieri: la stessa firma in due punti dello stesso file, e il
dossier l'ha pescata. E' la riga per cui `chara_func.hsp` e' stato aperto —
compariva in inglese nel collaudo — e si chiude copiando, non decidendo.

⚠️⚠️ **`:8629` e' il trentacinquesimo errore di monte, e stampa una lettera
sola.** Il giapponese e' 「name(A)の生命核はname(B)の遺伝子を獲得した。」, due
personaggi; l'inglese scrive `name(A) + " get genes of " + _s(B) + "."`, cioe'
mette **`_s()` dove andava `name()`**. `_s()` restituisce «s» o niente
(morfologia della terza persona), quindi a schermo la build inglese stampa
«`X get genes of s.`» oppure «`X get genes of .`» ⚠️ **E la rete 11 non lascia
scrivere la resa giusta**, perche' l'inglese dichiara **un** `name()` solo: e'
esattamente `proc.hsp:18280` della 38ª. ✅ Reso nominando il soggetto e
lasciando implicito il donatore — «X acquisisce i geni nel nucleo vitale» —
come la 38ª aveva stabilito.

⚠️ **Le sei voci di `:8007` stanno tutte sulla STESSA RIGA**, sei `lang()` una
di fila all'altra dentro un `txt`, ed e' il numero piu' alto del progetto su una
riga sola. Sono i versi di chi incassa un colpo, dentro `cnvtalk()`: statiche,
quindi la resa e' **testo nudo** e non un'espressione (la lezione della 36ª,
quando la rete 11 nata sbagliata avrebbe bocciato undici rese giuste).
⚠️ **E l'inglese ne ha inventata una**: 「くっ！」 e' un mugolio di dolore, e la
riga inglese dice «`Kill me already!`», che e' un'altra cosa. Reso sul
giapponese.

⚠️ **`:8751` e `:8754` sono un inglese solo per due giapponesi, e il codice
decide quale.** «`X splits!`» sta per 分身 — lo sdoppiamento del ninja, l'ombra
che non e' viva — e per 分裂, la scissione vera, quella della melma che diventa
due. Il ramo li separa: `instr(locvar_dmghp_s, 0, "/man/")` piu' l'arpia e il
ninja rosso da una parte, tutto il resto dall'altra. ✅ «si sdoppia» e «si divide
in due». 💡 E «si sdoppia» non l'ho scelta io: e' gia' di `action.hsp:12361`,
sotto lo stesso inglese.

⚠️ **Il peso vuole un aggettivo INVARIABILE, e ce n'era gia' uno.**
`proc.hsp:10612` rende 「は太った。」 «X diventa piu' pesante», e «pesante» sta
bene con tutt'e due i generi: si copia, e la rete 3 lo pretende. ⚠️ Ma il
gemello 「は痩せた。」 non puo' fare «piu' leggero», che invece **concorda**.
✅ Girato col verbo: «X perde peso». E' la strada del participio applicata a un
aggettivo, e la coppia esce asimmetrica apposta.

💡 **E i due blocchi del cibo sono ricopiati, come `resistmod`/`resistmodh` del
lotto 002**: `eatstatus` (`:8655`, `:8661`) e `eatstatusfood` (`:8677`, `:8683`)
dicono le stesse due frasi con una variabile diversa. Quattro voci, due rese.
"""
