# -*- coding: utf-8 -*-
"""Lotto `command-038`: **mangiare, bere, equipaggiare**. Tredici rese, da
`:14741` a `:14828`, ancora dentro `*com_inventory_loop`.

⭐⭐ **Il quartetto della sete era già scritto, e quello della fame no — e la
scoperta è che sono la stessa scena due volte.** `:14799` e `:14741` hanno la
stessa identica struttura: una `txt` con **tre** `lang()` di fila, che il gioco
sceglie a caso, per dire che non ci sta più niente nello stomaco. Le tre della
sete hanno lo **stesso giapponese** di `action.hsp:8274` — 「これ以上飲めない…。」,
「膀胱がやぶける…」, 「まだ喉は渇いていない。」 — quindi non si riscrivono: si
**ricopiano**, e la rete 3 deve tacere. Le tre della fame non hanno precedente, e
sono state scritte **sulla forma delle tre della sete**, una per una:

    Non riesci a mangiare altro.      Non riesci a bere altro.
    La pancia sta per scoppiarti...   La vescica sta per scoppiarti...
    Non hai ancora fame.              Non hai ancora sete.

💡 È il caso in cui «cercare prima di scrivere» non serve a riusare una resa, ma
a **riusare un registro**: tre frasi nuove che suonano come tre già spedite.

⚠️ **E la terza coppia è un inglese solo su due giapponesi diversi**, che la
rete 13 segnalerà: `:14741` e `:14799` dicono tutt'e due «Your stomach can't
digest any more.», ma il giapponese di `:14741` è 「まだ腹は減っていない。」 (non hai
fame) e quello di `:14799` è 「まだ喉は渇いていない。」 (non hai sete). Upstream ha
copiaincollato la riga della fame dentro il ramo della sete; l'italiano no.

⭐ **Tre rese riscosse senza decidere.** `:14758` ha lo stesso giapponese di
`:12795` ed è ricopiata parola per parola; «equipaggiare» è già il verbo di
questo stesso schermo (`:13924`, «Che cosa vuoi equipaggiare?», e `:17020`);
l'icona di `:14828` è la stessa di `:6068`-`:6076` e la resa è il **gemello
speculare** di `:6825`, che dice «name(tc) + " ha perso l'icona."».

⚠️⚠️ **Quattro rese su tredici hanno dovuto schivare un accordo di genere**, e
tutte per lo stesso motivo: il soggetto è chi gioca, di cui non si sa il sesso,
oppure è l'oggetto, di cui non si sa il genere.
- `:14752` «È troppo pesante da equipaggiare» e non «troppo pesante per essere
  equipaggiato»: `pesante` è invariabile, il participio no.
- `:14778` «qualcosa veglia su di te» e non «ti senti protetto».
- `:14772` «ti prende un brivido» e non «resti raggelato».
- `:14775` «hai mosso un passo» e non «sei più vicino».
💡 Non è prudenza: sono le tre righe che il gioco stampa quando equipaggi un
oggetto **maledetto, votato alla rovina o benedetto**, e le vede chiunque.

💡 **`:14775` è l'unica resa che tiene tutt'e due gli originali.** Il giapponese
è 「破滅への道を歩み始めた。」, «ha cominciato a percorrere la via della rovina»;
l'inglese è «You are now one step closer to doom.», che conta i passi. «Hai mosso
un passo sulla via della rovina» dice le due cose insieme, e «rovina» è la parola
che `skill.hsp:1576` usa già per 「破滅の歌」, il «Canto di rovina».
"""
