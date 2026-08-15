# -*- coding: utf-8 -*-
"""Lotto `command-040`: **la testa del menu di interazione**. Undici rese, da
`:5952` a `:5996`.

⚠️⚠️ **Questa zona TAGLIA una famiglia, ed è la trappola del lotto 031 al
rovescio: qui la coda è già spedita e manca la testa.** Il menu che si apre con
`i` su un personaggio è una sequenza di `promptAdd` che comincia a `:5952` e
finisce a `:6068`, cioè **a cavallo del confine di zona**; le voci da `:6002` in
giù sono state rese in una sessione precedente — trentacinque — e queste undici
sono quelle rimaste indietro. Chi avesse aperto la sola 5000-5999 senza guardare
avrebbe deciso la larghezza di una colonna già decisa da qualcun altro.

⭐⭐ **E la larghezza si misura, perché nessuna guardia la controlla.**
`larghezze.py` legge **solo `text.hsp`** e solo le voci scritte `s(cnt) = lang(…)`
(`larghezze.py:68`, `:78`): un menu costruito con `promptAdd` in `command.hsp`
non lo vede nessuno. Il metro però è lo stesso e sta nel sorgente: `:6172` chiude
la sequenza con `val = promptx, prompty, 275, 1`, cioè un riquadro da **275 px**,
che con la formula misurata a schermo — `(275 − 46) / 7,7` — fa **29 caratteri**.
✅ **E il tetto ha tenuto senza che nessuno lo misurasse**: delle trentacinque
voci già spedite la più lunga è `:6038`, «Metti fra gli indispensabili», che ne
fa **28**. Nessuna sfora. Le undici nuove stanno tutte sotto: la più lunga è
«Di' quello che provi», venti caratteri.

💡 **Due voci di questo menu non hanno una riga tutta loro, e non è un errore.**
`:6085` è un secondo `promptAdd lang("攻撃する", "Attack")` e `:6078` un secondo
「名前をつける」: l'estrazione àncora la firma alla **prima** occorrenza, quindi
`:5955` governa anche `:6085` e `:6019` («Dai un nome») governava già `:6078`.
È la stessa meccanica di `:14193`/`:14207` nel lotto 037.

⭐ **Le quattro carte erano già decise, e non da me.** `db_creature.hsp` chiama le
quattro creature-seme «il guerriero di **picche**» (`:38006`), «la piuma di
**fiori**» (`:37943`), «gli occhi di **quadri**» (`:37880`) e «la strega di
**cuori**» (`:37816`), e `command.hsp:6790`-`:6811` — i messaggi che escono
premendo proprio queste quattro voci — dicono già «conta come il guerriero di
picche». Le etichette non potevano dire altro.

⚠️⚠️ **Ma la quinta voce ha scoperto un'incoerenza già spedita, e la correzione
va insieme al lotto.** 「ランク」 qui è il **numero della carta**: `:6772` chiede un
valore da 1 a 13 e lo scrive in `CDATA_EVOLUTION_STAGE`. Ora:
- `proc.hsp:20184` è la frase che **insegna** la cosa — «Dal menu d'interazione
  puoi cambiarne **seme e valore** a piacere» — ed è già spedita;
- `command.hsp:6770`, cioè il prompt che compare **un clic dopo** questa voce,
  dice «Quale **rango**?»;
- e «rango» in questo stesso file è già il grado dell'avventuriero (`:4192`,
  «Rango degli avventurieri», `:4194`) e delle gilde.
✅ Quindi l'etichetta è «<Cambia valore>», e `:6770` diventa «Quale valore?» con
`scratchpad/correzione-rango-carta.py`. Tre stringhe che si rimandano l'una
all'altra adesso dicono la stessa parola.

💡 **「気持ちを伝える」 non è una dichiarazione d'amore, ed è stato il menu a dirlo.**
La voce porta a `txtselectkimoti0/1/2` (`:6842`-`:6851`), undici battute che
in `text.hsp:1756`-`:1790` sono già rese e vanno da «Ti amo.» e «Vuoi sposarmi?»
fino a «Fai schifo.» e «Ti detesto.». «Confess feelings» copre metà della lista;
«Di' quello che provi» la copre tutta.

💡 E «Feed» (`:5976`) non è l'inventario che dice il giapponese (「所持品」): `:6229`
mette `Filter_Food = 1` prima di aprirlo. Si dà da mangiare, e l'etichetta lo dice.
"""
