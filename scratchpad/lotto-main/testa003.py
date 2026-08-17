# -*- coding: utf-8 -*-
"""Lotto fase4-main-003: il campo che brucia, gli alleati che dormono, la
rivista e l'ubriaco (main.hsp, righe 2007-2333).

Ventisette rese. E' il primo lotto di `main.hsp` fatto di **dinamiche**: undici
delle ventisette portano `name()` o `cdatan()`, cioe' vanno in terza persona
singolare e non possono avere un participio o un aggettivo riferito al soggetto.

⚠️⚠️ **L'inglese di monte ha SCAMBIATO due giapponesi a `:2274`, e la resa
rimette le cose a posto.** Le quattro battute dell'ubriaco stanno su una riga
sola, quattro `lang()` in fila:

    lang("一杯どうだい？",   cnvtalk("Have a drink baby."))        ✓ combaciano
    lang("飲んでないよ",     cnvtalk("What are you looking at?"))  ✗ scambiate
    lang("何見てるのさ",     cnvtalk("I ain't drunk."))            ✗ scambiate
    lang("遊ぼうぜ",         cnvtalk("Let's have fun."))           ✓ combaciano

「飲んでないよ」 vuol dire *non ho bevuto* e 「何見てるのさ」 *che cos'hai da
guardare*: chi ha tradotto in inglese le ha messe l'una al posto dell'altra.
Al giocatore non cambia niente — le quattro escono a sorte da un `txt` solo — ma
al **dizionario** si': la chiave e' `(riga, inglese)` e la colonna che si legge
accanto alla resa e' il **giapponese**. Scritte secondo l'inglese, quattro righe
del dizionario direbbero una cosa e ne mostrerebbero un'altra per sempre.
✅ Percio' le rese seguono il **giapponese**, che e' anche quel che vuole la rete
3: 「一杯どうだい？」 era gia' reso «Che ne dici di un bicchiere?» in
`db_creature.hsp:50914`, e da li' si ricopia.

⭐ **`:2007` e la rete 3, che aveva ragione.** 「は酸に焼かれた。」 e' **la stessa
identica** riga di `chara_func.hsp:4754`, resa «brucia nell'acido»: li' e' il
colpo di un nemico, qui e' la pozza d'acido sul pavimento, e la frase e' la
stessa perche' il giapponese e' lo stesso. ⚠️ Il **suo inglese**, invece,
combacia con `chara_func.hsp:4761` («melt» -> «L'acido scioglie...»), che e' un
altro messaggio: e' il caso in cui seguire l'inglese avrebbe prodotto una resa
gia' presa da un'altra voce. Si segue il giapponese, e la rete tace.
💡 Per la stessa ragione `:2075` (「は燃えた。」) **non** riusa «prende fuoco», che
in `chara_func.hsp:4614` rende 「は燃え上がった。」: due giapponesi diversi, due
rese diverse.

⚠️ **Le quattro battute degli alleati che si addormentano non possono avere un
participio.** «si e' addormentato» concorderebbe col genere di `cdatan(CDATAN_NAME,
cc)`, che non si conosce: sono le quattro taglie di cucciolo
(`CDATA_SPRITE_SIZE_MILK` da -5 a -2). Le rese girano intorno all'ostacolo —
«scivola in un sonno profondo», «prende sonno», «si addormenta piano» — che e' la
stessa disciplina delle battute dei figli nella 52ª.
⚠️ Per lo stesso motivo `:2272` dice «alza il gomito» e non «e' ubriaco», e
`:2280` «perde la pazienza» e non «e' spazientito». 💡 «perde la pazienza» e'
letteralmente l'esempio canonico della guida di stile.

⭐ **`actlistn` non porta l'articolo, e lo dice l'unico sito che lo usa gia':**
`command.hsp:17267` scrive «Interrompere " + actlistn(...) + "? "». `:2333` gli
si accoda con «interrompe», stesso verbo e stessa forma.

💡 **`:2219`-`:2242` sono le due tornate di commenti alla rivista** che un
alleato legge (`snd SOUNDLIST_BOOK1`, poi `dmgcon CONDITION_CONFUSE`): tre
battute stupite alla prima lettura, tre sconcertate alla seconda. Sono `statica`
anche se l'inglese e' `cnvtalk("...")`, perche' l'estrazione guarda dentro la
chiamata.
"""
