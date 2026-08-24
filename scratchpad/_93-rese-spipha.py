# -*- coding: utf-8 -*-
"""93a - SPIPHA la cacciatrice di draghi (`chat.hsp:9724`-`:9793`, 12 su 15).

《竜狩り》スピファ / `<Spipha>` (`db_card.hsp:6926`, reso **«<Spipha> la
cacciatrice di draghi»**) sta a Ulm-Leson e da' la missione del drago del
vulcano (`text.hsp:11502`, `:11510`). Da bambina l'ha maledetta un drago e il
suo corpo e' **mezzo drago**: e' cosi' che sente il mana dei draghi a distanza.

⭐ IL REGISTRO ERA GIA' FISSATO da tre righe rese prima d'oggi:

    chat.hsp:9777   «Ehi, ehi, ti interessa una caccia al drago?»
    chat.hsp:9775   «\"Pare\"?»   (la voce di menu del giocatore)
    screen.hsp:1738 «Ma guarda, non mezzo drago ma mezzo serpente...»

Da' del tu, parla svelta e sbrigativa, con gli intercalari di chi ti ferma per
strada. ⚠️ **Ed e' donna**: le sue rese sono al femminile («non sono riuscita»,
«l'ho vista»), che qui non e' una scelta ma un dato — `db_card.hsp:6926` la
chiama *la cacciatrice*.

LESSICO EREDITATO (non deciso qui):
  - ドラゴンハンター  «cacciatrice di draghi»  db_card.hsp:6926, chat.hsp:13146
  - 半竜              «mezzo drago»            screen.hsp:1738
  - 災厄              «calamita'»              db_card.hsp:9227, chat.hsp:7652
  - ネフィアの守護者  «i guardiani di Nefia»   chat.hsp:24374
  - サブクエスト      «missione secondaria»    text.hsp:10005 (`@QS[...]`)

⭐⭐ DEROGA 1 — `:9740`, LA CLAUSOLA CHE L'INGLESE BUTTA E CHE CHIUDE LA TRAMA.
Il giapponese comincia con 「今回は違ったけれど」, cioe' **stavolta non era
quello**: il drago appena abbattuto non e' il drago nero dagli occhi d'argento
che lei cerca da tutta la vita. L'inglese la salta e attacca da «Let me know
if...», e la riga diventa una richiesta generica invece della chiusura della
missione appena finita. Torna dentro.

⚠️ DEROGA 2 — `:9754`, 頑張った君 SENZA NOME DI MESTIERE.
「ドラゴンハンターとして頑張った君」 chiama il giocatore *cacciatore di
draghi*, e in italiano il mestiere porta il genere (e per giunta il **suo**
titolo e' al femminile). Si gira sul verbo, con una forma che il genere non ce
l'ha: «per come te la sei cavata a caccia di draghi». ⚠️ Stessa famiglia delle
deroghe di NORNE e di LEIKI, oggi.

⭐ DEROGA 3 — `:9728`, LA FORMULA E' UNA PARODIA E RESTA SPEZZATA IN DUE.
「ドラゴン種族殺すべし。慈悲はないわ。」 e' il calco di una formula sentenziosa
(「◯◯殺すべし。慈悲はない」): il senso non sta nelle parole, sta nella
**forma** — due frasi mozze, l'obbligo e poi la negazione. L'italiano la tiene
tale e quale, senza scioglierla in un periodo solo come fa l'inglese.

⚠️⚠️ DEROGA 5 — `:9744`, «SEI STATO TU» DAVA UN GENERE AL GIOCATORE, e il
referto non lo vede. La prima resa diceva «Sei stato tu ad abbatterlo, vero?»:
`referti.py` guarda i participi di `essere` in certe forme e questa gli e'
passata sotto, perche' quello che sale a **9** e' l'innocuo «te la sei cavata»
di `:9754` (idiomatico, concorda col clitico, gemello di `:22872` gia' dichiarato).
Trovata **leggendo le rese una per una** dopo il referto, non dal referto: si
scioglie con «L'hai abbattuto tu, vero?», che di participi non ne ha.
💡 La lezione e' che il numero del referto va **letto**, non solo confrontato: e'
salito per la ragione giusta e nascondeva quella sbagliata.

⭐ DEROGA 4 — `:9753`, 火の鳥 NON E' UNA CREATURA DEL GIOCO.
La parola compare **una volta sola in tutto il sorgente** (questa riga): non e'
un identificativo e non ha un nome nel progetto, quindi non si va a cercare la
creatura che non c'e'. L'inglese sceglie «phoenixes», che in italiano
tirerebbe dentro la fenice e la sua leggenda; il giapponese dice quel che si
vede, cioe' uccelli di fuoco, e si rende alla lettera.

⚠️ MISURA: **zero fuori misura**, ma sei righe piu' lunghe dell'inglese al primo
giro, diventate **quattro** (`:9740`, `:9753`, `:9780`, `:9788`) dopo la
potatura. Le due riassorbite erano prolissita' mia; le quattro che restano sono
di forma — l'inglese di questo blocco **comprime sistematicamente** (a `:9740`
butta via una clausola intera, vedi la deroga 1) e le due righe piu' lunghe del
blocco, `:9781` e `:9732`, stanno sotto il tetto senza sforzo. Nessuna arriva
vicino alle 13 righe di `chatMore`.

PERIMETRO: 12 firme da fare su 15 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 9724`) e **zero firme gia' rese altrove**.

MENU: uno solo (`:9775`-`:9776`), **gia' reso** tutto: il lotto non lo tocca.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte
(i puntini di sospensione si scrivono con tre punti).
"""

RESE = {
    # --- la proposta: la caccia al drago del vulcano
    9780: 'Ah, il \\"pare\\" te lo spiego. Da bambina mi ha maledetta un drago '
          'cattivo e il mio corpo è mezzo drago. In cambio, si fa per dire, '
          'il mana che i draghi emanano io lo sento.',
    9781: 'Il mana che sentivo dentro il vulcano non era roba normale: quello '
          'è di classe calamità. Solo che al vulcano ci sono andata più volte '
          'per abbatterlo e non ho trovato nemmeno un draghetto. Il mana lo '
          'sento eccome, quindi magari sa nascondersi alla vista.',
    9782: 'Se ne trovi uno del genere, abbattilo tu al posto mio. È la mia '
          'missione secondaria del drago!',
    9788: 'Ehm. Se me lo rifiuti così di netto non posso mica andare avanti a '
          'parlare, ecco...',

    # --- mentre la caccia è aperta
    9771: 'Il mana del drago è ancora bello vivo... Ma dove diavolo si '
          'nasconde?',

    # --- il ritorno con il drago abbattuto
    9744: 'Dal vulcano non sento più il mana di quel drago enorme. L\'hai '
          'abbattuto tu, vero? Me lo racconti?',
    9753: 'Ah, ecco: era un drago vestito di fuoco. Mmh... di uccelli di '
          'fuoco ne ho visti parecchi: sarà stato camuffato fra quelli?',
    9754: 'Ah, giusto: per come te la sei cavata coi draghi, questo è per te. '
          'E d\'ora in poi draghi a raffica!',
    9740: 'Stavolta non era quello. Ma se trovi un drago nero con gli occhi '
          'd\'argento, dimmelo: è una delle ragioni per cui faccio la '
          'cacciatrice di draghi.',

    # --- nella Culla del Caos
    9732: 'Ho sentito più di un mana potente di drago e sono venuta a dare '
          'un\'occhiata, ma... mamma mia, che tosto questo castello. I mostri '
          'sono forti da matti e avanzare è una faticaccia. Che siano '
          'potenziati con lo stesso principio dei guardiani di Nefia?',
    9733: 'Uff... Sarà il caso che torni indietro un momento e mi riallenti.',
    9728: 'La stirpe dei draghi va sterminata. Nessuna pietà.',
}
