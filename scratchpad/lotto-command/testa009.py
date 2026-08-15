# -*- coding: utf-8 -*-
"""Lotto `command-009`: le 58 voci di `*com_ally`, la lista degli alleati e dei
prigionieri.

E' la finestra che si apre ogni volta che il gioco chiede **quale compagno** —
richiamarlo, venderlo, iscriverlo alla scuola, metterlo al negozio, portarlo
all'arena, rinchiuderlo. Undici usi diversi della stessa lista, distinti da
`allyctrl`, piu' gli stati che compaiono accanto a ogni nome.

⚠️⚠️ **`larghezze.py` NON misura questo file, e la ripresa della 44a diceva il
contrario.** `larghezze.py:68` dichiara `FILE = "text.hsp"`: i suoi 75 menu sono
tutti di li', e nessuna guardia ha mai guardato un menu di `command.hsp`. Quindi
il tetto se lo costruisce il lotto, come per il «Background».
✅ **Qui pero' il sorgente il budget lo dichiara davvero**, ed e' la strada
migliore della stima sull'inglese: `chara.hsp`… no, `command.hsp:1281`-`:1283`
apre una finestra da **620 px**, mette le voci a `wx + 84` e la seconda colonna
a `wx + 350`. Quindi la prima colonna ha **266 px** e la seconda **~250**, ed e'
lo stesso metro della scheda del personaggio della 43a: la differenza fra due
`pos` scritte a poche righe di distanza.
💡 Il nome del compagno mangia quasi tutta la prima colonna, quindi quel che
conta davvero e' che i **suffissi fra parentesi** non siano piu' lunghi dei
loro inglesi. Il tetto della zona e' 44 caratteri (`scratchpad/tetto-en.py`).

⚠️ **Sette suffissi inglesi non chiudono la parentesi** — `(Riding`,
`(OutRange`, `(offensive`, `(defensive`, `(intercept`, `(talking`, `(Dead` —
mentre `(Waiting)`, `(Alive)`, `(Ash)`, `(Stray)` la chiudono. Il giapponese le
chiude tutte, e per i quattro ordini di combattimento usa le **barre**,
「/突撃/」 「/防御/」 「/迎撃/」 「/交渉/」, che a schermo distinguono l'ordine
dallo stato. La resa segue il giapponese: parentesi chiuse dove il giapponese ha
le parentesi, barre dove ha le barre.

⭐ **E «Ally List» sta per DIECI titoli giapponesi diversi.** 「収容する連行者」,
「呼び戻す仲間」, 「売り飛ばす仲間」, 「出場する仲間」, 「対象候補」,
「門下生候補」, 「放牧候補」, 「店長候補」, 「ブリーダー候補」,
「滞在状態の変更」: ognuno dice **a che serve la lista**, e l'inglese li
appiattisce tutt'e dieci. E' lo stesso appiattimento del `command-005` e della
42a, e disfarlo costa zero perche' la colonna giapponese e' li' accanto.

⚠️ **Tre stati vanno detti senza participio, e sono `txt` di rifiuto**: `:1519`,
`:1524`, `:1529` sono `he(p) + " " + is(p) + " dead."` e sorelle, dove `he` e
`is` sono **morfologia inglese** e quindi spariscono — la resa italiana resta
senza funzioni e senza soggetto, e «è morto» concorderebbe col compagno.
✅ «Non è più in vita», «È in attesa», «È al lavoro»: `essere` piu' locuzione,
che non accorda niente. E' la manovra del nome astratto della 44a in forma
verbale.

💡 **Sei copie su cinquantotto**, tutte pescate da `dossier.py`: «Nome»
(`:453`, `:456`, `:14120`), «Prezzo» (`:14101`), «AP» (`:10504`), «Vita»
(`:10517` e `skill.hsp:9`), «Nessuna» (`init.hsp:371`). Piu' due termini presi
dal glossario invece che inventati: «Trattativa» (`skill.hsp:222`) e
«Ingegneria genetica» (`skill.hsp:197`).
"""
