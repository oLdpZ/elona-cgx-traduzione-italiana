# -*- coding: utf-8 -*-
"""Lotto `command-034`: **il congedo degli otto dèi, i cioccolatini di San
Valentino e la gabbia**. Sedici rese, e sono l'apertura della zona 7000-7999.

⭐⭐⭐ **Otto rese su sedici non le ho decise io: sono gli stessi otto dèi del
lotto 028, che dicono addio invece di salutare.** `:7015`-`:7050` è il congedo di
Itzpalt, Yacatect, Jure, Lulwy, Ehekatl, Opatos, Kumiromi e Mani; `:4490`-`:4547`
era il loro arrivo, reso nella 46ª. Stessi personaggi, stesso registro, e il
registro **si riscuote**:

| dio | arrivo (46ª) | congedo (qui) |
|---|---|---|
| Lulwy | «Che sfacciataggine, convocarmi così.» | «Per stavolta ti lascio andare, gattino.» |
| Opatos | «Muahahahah! Eccomi qua!» | «Muahahahahahah! Addio.» |
| Kumiromi | «Mi hai chiamato... che gioia...» | «Non dimenticare... veglierò sempre su di te...» |
| Mani | «Hai fatto bene a chiamarmi. Ti concedo il diritto di adorarmi.» | «Per l'ultima volta, guarda di che cosa è capace questo trasferitore spaziale!» |
| Itzpalt | «Imprimilo nella tua anima: anche questo è destino tessuto dall'Elemento.» | «È tempo che io torni al mondo cui appartengo.» |
| Yacatect | «Se mi chiami, arrivo subito! Allora? C'è un affare da fare?» | «E allora ciao, eh!» |
| Jure | «N-non è mica che volessi venire, sai! Per niente!» | «N-non è mica che mi senta sola, sai! Per niente!» |
| Ehekatl | «Miaomiaomiaaa!» | «Torno a casa! A casa!» |

⭐⭐ **E l'eco di Jure non è una mia trovata: è nel giapponese.** L'arrivo è
「べ、別に来たくて来たわけじゃないんだからね！」 e il congedo
「ベ、別に寂しくなんかないんだから！」 — **la stessa costruzione**, balbettio compreso.
La resa italiana la ripete perché la ripete l'originale, non per simmetria.

⚠️⚠️ **E per abbinare dio e battuta ho dovuto capire una cosa che a occhio si
legge al contrario: in `*wish` il `txt` PRECEDE il suo `characreate`.** A
`:4490` c'è «Miaomiaomiaaa!» e a `:4493` `characreate CREATURE_ID_EHEKATL`; a
`:4497` la battuta arrogante e a `:4500` `LULWY`. Chi leggesse la battuta come
appartenente alla creatura creata **sopra** attribuirebbe ogni voce al dio
sbagliato, e lo sbaglio sarebbe invisibile: otto battute plausibili, tutte
sulla bocca di qualcun altro.
✅ Il controllo che lo dimostra è `:4547`, 「きゅー♪」: se la battuta appartenesse al
`characreate` precedente sarebbe di **Jure**, mentre `:4550` crea la
`QUANTUM_CREATURE` — ed è la forma di vita quantistica a fare «Quu», come la 46ª
aveva già scritto a proposito delle divergenze volute.
💡 Qui non serviva, perché `:7015`-`:7050` hanno un `if ( cdata(CDATA_ID, tc) ==
CREATURE_ID_… )` esplicito sopra ciascuna. Ma serviva per leggere il lotto 028,
cioè per sapere **da chi** si riscuote.

⚠️ **Cinque voci su `:7072` sono la stessa riga**, perché `txt` sceglie a caso
fra i suoi argomenti (`init.hsp:44`, `txtc = rnd(txtc)`): sono cinque varianti
della scena dei cioccolatini. Due sono `cnvtalk` (statiche) e tre sono
descrizioni con `name(tc)`.
⚠️ **E l'inglese di monte ci ha perso uno spazio**: `:7072` scrive
`name(tc) + "fidgeted a bit before…"` senza spazio dopo la funzione, quindi in
inglese si legge «Annafidgeted a bit». La resa italiana ce lo rimette — non è una
toppa, è che la resa **è** il letterale e lo spazio ci sta dentro.

⚠️ **Tre accordi evitati, e tutti per lo stesso motivo**: chi parla o di chi si
parla può essere di qualunque genere. `:7098` è «riprende l'aspetto di prima» e
non «è tornato»; `:7072` è «Davvero ti va bene, da una persona come me?» e non
«da uno come me»; `:7056` è «Hai rimandato a casa …» e non «… è tornato a casa».

⚠️ `:7094` porta **`name` due volte** in inglese, e la rete 11 conta le
occorrenze: la resa ne ha due anche lei. 「連行対象」 è chi va consegnato a
qualcuno, da cui «non è più da consegnare».
"""
