# -*- coding: utf-8 -*-
"""Lotto fase4-main-001: il registro del mondo — meteo, vento d'etere, ciclo del
giorno (main.hsp, righe 1174-1635).

⭐ **`main.hsp` e' l'ultimo dei «mezzi fatti» della 55ª, ed e' l'undicesimo file
senza dizionario**: 384 `lang()` che nessun referto nominava, perche'
`verifica --dizionario` elenca solo i file che hanno un `dizionario/*.jsonl`.
Aprirlo anche per una voce sola lo fa entrare nel conteggio. Questa e' la
formula che la 54ª aveva scritto e la 56ª ha applicato in serie su altri quattro.

Trentaquattro rese, e la zona non e' scelta a caso: sono i messaggi che il
giocatore legge **piu' spesso di qualunque altro**, perche' escono da soli col
passare delle ore — «comincia a piovere», «spunta l'alba», «il tuo diario e'
stato aggiornato».

⚠️⚠️ **L'inglese di `:1307` e' sbagliato, e la resa italiana lo corregge.**
Il giapponese e' 「雪は止んだ。」 (*la neve e' cessata*) e il ramo che la contiene e'
`if ( p == WEATHER_SNOW )` (`:1304`); l'inglese ci ha copiato sopra
`"It stops raining."`, la stessa stringa che sta gia' a `:1274` per la pioggia.
Sono due voci con **firma diversa** — la firma e' sul contenuto, e il giapponese
differisce — quindi il dizionario le distingue senza bisogno di toppe. ⚠️ La
rete 13 lo dira' come referto: «un inglese solo per due giapponesi diversi». E'
esattamente il caso che quella rete esiste per far vedere.

⭐ **Quattro etichette gia' decise hanno deciso quattro rese**, e nessuna delle
quattro e' stata scelta qui:

  - `text.hsp:46` e' l'array `_weather`, cioe' i nomi del tempo nell'HUD:
    «Vento d'etere», «Neve», «Pioggia», «Temporale». Percio' `:1279`
    (RAIN -> HARD_RAIN) dice «diventa un temporale» e `:1286` (HARD_RAIN ->
    RAIN) dice «si attenua in pioggia»: il messaggio nomina lo stato in cui
    l'HUD sta passando, con la parola che l'HUD usa.
  - `text.hsp:60` sono le ore del giorno, e la sesta e' «Alba». `:1399` scatta
    a `if ( gdata(GDATA_HOUR) == 6 )`, cioe' **nell'ora che si chiama cosi'**:
    «Spunta l'alba» e l'orologio concordano.
  - `text.hsp:48` sono le cinque giornate bonus — «Giornata da allenamento»,
    «da battaglia», «da lavoro», «da esplorazione», «da studio» — e i cinque
    messaggi di `:1524`-`:1540` le annunciano. Portano lo **stesso sostantivo**,
    percio' chi legge il messaggio ritrova la parola nella barra.
  - ⭐⭐ La toppa di `custom_tweaks.hsp:1846` chiama la sfida **«Vento d'etere
    perenne»**, ed e' la voce del pannello dei ritocchi da cui la si accende.
    Percio' il titolo di `:1626` e l'etichetta `(Permanent Etherwind)` di
    `:1213`, `:1217` e `:1294` dicono tutte quella, e non una quinta variante.
    ⚠️ Quella riga non e' una `lang()`: e' un letterale **nudo**, e a trovarla
    e' stato `nudi_en`. Senza guardare anche li', il titolo qui sarebbe stato
    scelto a orecchio.

⭐ **Il blocco `:1626`-`:1635` ha un gemello gia' tradotto**, e non e' una
somiglianza: e' lo stesso codice con un'altra sfida dentro. `command.hsp:15560`
(«Tasse doppie ogni mese») ha la stessa forma riga per riga — `s`, `file`,
`buff`, `listmax`, sei `chatList`, `gosub *re_select` — e le sei battute sono
**le stesse identiche `lang()`**, gia' rese in `command.hsp` e in `text.hsp`.
Qui si ricopiano, e la rete 3 lo confermera' su tutte e sei.
💡 Da li' viene anche la forma del `buff` di `:1628`: «Incredibile! Hai pagato
le tasse per N mesi!» -> «Incredibile! Hai resistito al vento d'etere per N
giorni!». ⚠️ **«Sei sopravvissuto» non e' scrivibile**: e' un participio riferito
al giocatore, di cui non si conosce il genere (guida-stile, «Registro»).
«Hai resistito» prende l'ausiliare che non accorda, e per giunta combacia col
contatore del pannello, che la toppa rende «giorni di sopravvivenza».

⚠️ **`:1630`-`:1635` sono `chatList`, cioe' passano dalla RETE 15** (il tetto di
52 caratteri delle voci della finestra del dialogo, misurato nella 55ª). La piu'
lunga delle sei rese ne fa 27: nessuna ci si avvicina. Entrano comunque nel
denominatore di `menu_dialogo`, che passa da 50 a 56 voci misurate.

💡 **«Le Nefie», al plurale, e non «Le Nefia».** Il plurale l'ha gia' scelto il
pannello dei ritocchi — «Nefie casuali risvegliate», «tutte le Nefie casuali» —
mentre il singolare sta in `text.hsp:9935` («una Nefia casuale»). Le due voci di
`:1174` e `:1187` sono le due meta' della stessa cosa: `:1187` accende
`GDATA_FLAG_NEFIA_FEVER_ACTIVE` a 100 e `:1174` lo rimette a zero.

⚠️ **Le nove righe di `:874`-`:898` NON sono in questo lotto e non vanno
tradotte mai.** Sono la finestra dei comandi per principianti, chiusa dentro un
`if ( jp )`: in inglese non esiste, e tutte e nove portano lo stesso segnaposto
«Essential is normal mode.». Le conta `scratchpad/lang-nel-ramo-jp.py`, che
all'apertura di questa sessione ha trovato la sua prima voce **gia' tradotta**
in `item_func.hsp` e l'ha fatta rinviare.
"""
