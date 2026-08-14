# -*- coding: utf-8 -*-
"""Lotto fase4-init-003: gli edifici, il genere, i possessivi, l'orologio, il
log e il messaggio d'errore (init.hsp, righe 408-2873).

32 rese **+1 rinviata**, e **chiude `init.hsp`**. E' il lotto piu' vario del
progetto: ci sono sei nomi di edificio, nove valori che **non si traducono**,
cinque possessivi, sette separatori di data e un paragrafo di prosa.

⚠️⚠️ **I nove valori di `CDATAN_NEWSEX` restano inglesi, e la decisione non e'
di questo lotto: e' della Fase 0.** `male`, `female`, `none`, `hermaphrodite`,
`male?`, `female?`, `trans-male`, `trans-female` sono **scritti nel salvataggio**
(`chara.hsp:2790`, `:4390`, `item.hsp:4118`-`:4175`) e **riletti come operandi di
confronto** in cinque file (`init.hsp`, `text.hsp`, `command.hsp`, `item.hsp`,
`action.hsp`). Tradurli farebbe fallire ogni confronto su un salvataggio
esistente, e il gioco sbaglierebbe il genere di ogni personaggio gia' creato.
`invariati.md` lo dichiara dal 2026-08-07, sezione «Valori di dato».

⭐⭐ **Ma il modo di lasciarli inglesi e' cambiato, e a deciderlo e' stata la rete
7.** Il primo giro di questo lotto li aveva messi in dizionario **identici
all'inglese**, che e' il meccanismo che `invariati.md` descrive e che
`db_creature.hsp` usa per `Qy@` e `HAPPY END!!`. La rete 7 li ha fermati tutti e
nove — «riga 1813 e' un confronto, non un testo: va rinviata» — ed **ha ragione
lei**: quel testo `invariati.md` e' del 2026-08-07 e la rete 7 e' nata nel lotto
`007`, dopo. ✅ Sono **rinviati**, che e' piu' forte che renderli identici: la
resa identica passa comunque da `applica.py`, la rinviata non tocca il sito
nemmeno per riscriverci sopra la stessa stringa. Ed e' la convenzione che il
progetto usa gia' per dire «guardato, e si lascia stare» — le quattro di
`chara_func.hsp`, le sette di `proc.hsp`.
💡 **E l'asimmetria con `text.hsp` e' giusta, non un'incoerenza**: `text.hsp:123`
ha la **stessa firma** di `init.hsp:1813` e la tiene in dizionario resa
identica, perche' li' il sito e' un **assegnamento a `strmale`**, cioe' testo che
si stampa; qui e' un operando di `==`. La rete 7 guarda il sito, non la stringa.
💡 A schermo `male` e `female` arrivano lo stesso tradotti, per **sei toppe** su
`text.hsp`, che separano le righe di display dagli operandi.

⭐⭐ **E qui salta fuori un errore di monte NEL GIAPPONESE, che e' rarissimo.**
`his()` a `:1973` confronta `lang("自称男性", "female?")` — cioe' il ramo che
restituisce 「彼女？の」, «di lei?», controlla se il personaggio si dichiara
**maschio**. Le due funzioni sorelle non sbagliano: `he()` a `:1830` e `him()` a
`:2011` scrivono tutt'e due 自称女**性**. E' un refuso, ed e' nel giapponese,
mentre i quarantasei errori di monte contati finora erano quasi tutti
nell'inglese. 💡 **Ed e' innocuo per un pelo**: il secondo operando della stessa
riga e' `lang("自称女性", "trans-female")`, il cui ramo giapponese e' proprio
自称女性, quindi il caso viene preso lo stesso — un byte piu' in la' della riga.
Con questo la serie passa da quarantasei a **quarantasette**.

⭐⭐ **Il punto interrogativo di `his()` non si traduce, e quello di `he()` si:
e' la stessa marca, e in italiano vale in un caso e non nell'altro.** Upstream
distingue `his` da `his?` e `her` da `her?` per dire che il genere e'
**dichiarato** dal personaggio e non accertato. In italiano il possessivo
concorda col **posseduto**, non col possessore: «il suo» copre maschio, femmina e
chiunque altro, quindi tutt'e quattro i valori diventano **«il suo»** e il «?»
segnerebbe un dubbio su una distinzione che l'italiano **non fa**. ✅ Le cinque
rese sono «il tuo» per `your` e «il suo» per gli altri quattro.
⚠️ **Invece `he()` il «?» se lo tiene** — «lui?», «lei?», gia' in dizionario dal
lotto di Fase 1 — perche' li' il pronome soggetto in italiano il genere **lo
distingue davvero**, e il dubbio ha qualcosa su cui cadere.
💡 **E l'articolo ci vuole**: i tre siti che gia' usano `his(x, 1)` sono scritti
per riceverlo — `proc.hsp:8849` «succhi **il suo** sangue», `:9605` e `:9612`
«interrompe **il suo** daffare» — e ognuno ha accanto un nome **maschile
singolare**, che e' quel che la rete 10 pretende dal 2026-08-11.

⚠️ **`:510` e' RINVIATA, e l'ha vista la rete 6: la riga e' spenta.**
`; cdatan(CDATAN_NAME, ...) = lang("残りカス", "a garbage")` sta dentro il blocco
`// Original:` che il mod di James ha commentato — il nome che il gioco dava a un
personaggio andato perso. Tradurla sarebbe lavoro su testo morto, che
`misura-blocchi-spenti.py` conta gia' sette volte nel dizionario.

⚠️ **I sette separatori di data e orologio non sono testo, e sei su sette
restano.** `:2225` compone la data come `anno + " " + mese + "/" + giorno + " "`,
`:2227` aggiunge `ora + "h"`, `:2235` fa `ore + ":" + minuti + ":" + secondi +
" Sec"`. La barra, i due punti e la «h» l'italiano li scrive uguali; lo spazio
era **gia' dichiarato** in `invariati.md` da `text.hsp:198` (`strblank`).
✅ L'unica che cambia e' l'ultima: « Sec» diventa « sec», perche' l'italiano
abbrevia i secondi in minuscolo.
⚠️ **E qui sono le altre due chiavi ambigue del file**: lo spazio sta per 年 e
per 日, i due punti per 時間 e per 分. Chiave lunga `(riga, en, jp)` per tutt'e
quattro.

💡 **`:2082` era gia' tradotto, in un altro file, e serviva lo stesso.**
`text.hsp:363` rende 「性別不明」 «sconosciuto» ed e' la **stessa firma**; ma
`applica.py:618` cicla su `dizionario/<file>.jsonl` e applica ogni dizionario al
**suo** file soltanto. La firma e' globale, il dizionario no: la stessa voce va
scritta una volta per ogni `.hsp` che la contiene. ✅ Copiata identica.

💡 **E il file si chiude con 10 voci fuori dizionario, tutte volute**: le nove
del genere e la riga spenta di `:510`. `verifica --dizionario`
dira' «10 non ancora tradotte» per sempre, come dice «4» per `chara_func.hsp` e
«7» per `proc.hsp`.

⚠️ **Una grida della rete 3 che non e' una divergenza**: 日 e' « » qui, dove e' il
suffisso del giorno in una data, e «g» a `text.hsp:11695`, dove e' l'unita' di
misura in una scadenza («3g»). Stesso kanji, due mestieri.

💡 **Gli edifici, e un ladro diventato contrabbandiere.** `:412` e'
「盗賊の隠れ家」, e 盗賊 e' la stessa parola della «Gilda dei Ladri» del lotto 002:
l'inglese ci ha messo `Smuggler's`, che e' un altro mestiere. ✅ «Covo dei ladri».
"""
