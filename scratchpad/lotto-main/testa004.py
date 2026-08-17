# -*- coding: utf-8 -*-
"""Lotto fase4-main-004: il turno del giocatore — carico, opzioni, uscita, e la
fine di Lesimas (main.hsp, righe 2625-3999).

Quindici rese sparse, tenute insieme dal fatto che escono tutte dal **giro del
turno**: il carico che schiaccia, la raccolta automatica che si accende e si
spegne, l'ora di gioco che passa, la domanda dell'arena, il tasto della guida,
e in fondo le due righe della vittoria finale.

⚠️⚠️ **`:3130` e' il caso in cui l'italiano non ha il trucco dell'inglese, e la
frase si riscrive invece di storpiarla.** L'inglese fa
`" hour" + _s3(hour_played)`, cioe' aggiunge la `s` **solo se le ore sono piu'
di una**: `_s3` sta in `MORFOLOGIA_INGLESE` e `verifica` pretende che sparisca.
Tolta, «da " + hour_played + " ore» direbbe «da 1 ore» alla prima ora, e non c'e'
nessuna funzione italiana da mettere al suo posto — aggiungerne una e' proprio
quel che la rete 11 vieta.
✅ La via d'uscita e' la stessa che il progetto usa gia' per i materiali
(`command.hsp:6357`, «Materiale ricevuto: neve (3)»): si mette il numero
**dietro i due punti**, dove singolare e plurale non si pongono. «Ore di gioco
su ElonaPlus: 1.» e «...: 12.» sono tutt'e due giuste.
💡 E' la stessa famiglia dell'accordo evitato invece che scelto, come le battute
dei figli della 52ª e i cuccioli del lotto 003: **quando la morfologia non c'e',
si cambia la forma della frase, non si accetta la forma sbagliata.**

⭐ **Due etichette dell'interfaccia decidono le due righe della raccolta
automatica.** `action.hsp:1067` la chiama «[Raccolta automatica]» nel menu che la
accende, `screen.hsp:1004` «Raccolta» nell'HUD dove non c'e' spazio: `:3343` e
`:3347` sono i due messaggi che annunciano il passaggio, e usano il nome per
esteso perche' li' lo spazio c'e'.

⭐ **`:3024` tiene gli asterischi**, come le altre 137 rese `*...*` del progetto:
`*ぷちゅ*` -> `*sciac*`, `*必殺セミファイナル！*` -> `*COLPO SEMI-FINALE!*`. Non
sono decorazione tipografica, sono il modo in cui Elona scrive un cartello. ⚠️ Il
gemello `*Win*` (`main.hsp:4050`) non e' in questo lotto e restera' in tinta.

💡 **`:3937`-`:3964` sono lo scherzo dell'uscita**, e vanno lette in fila: il
gioco reagisce riga per riga mentre si scrive la parola per uscire (`key == "Q"`,
poi `"y"`, poi `"sc"`), e alla fine evoca dieci `CREATURE_ID_AT_SIGN` — le
chiocciole che sono il giocatore nei roguelike di una volta. Le tre rese salgono
di tono come l'inglese: «Come...», «Non dirai sul serio...», «Aaaaahh!!».

💡 **`:3999` non traduce il giapponese, e va bene cosi'.** 「お前がここに辿り着く
ことは」台座から、何かの声が聞こえる。 comincia a meta' frase, con la parentesi di
chiusura di una battuta che il testo non ha mai aperto — e' un residuo di
upstream. L'inglese ha tenuto solo la seconda meta', che e' quella che ha senso,
e la resa segue l'inglese.

⭐ **«Lesimas» resta «Lesimas»**, come nelle undici rese che gia' lo nominano
(`text.hsp:2770`, `map.hsp:4112` «Fondo di Lesimas», `db_item.hsp:135481`).
"""
