# -*- coding: utf-8 -*-
"""95a - WEL, ROVID e BURT (12 rese) — e il buco di memoria prende un nome.

`CHILD_WEL` (`:9188`-`:9235`, 5), `ROVID` (`:11893`-`:11911`, 3) e `BURT`
(`:15132`-`:15144`, 4). Tre posti diversi (Larna, il Santuario del Guardiano,
Zaile): come nel lotto prima, il raggruppamento per mappa e' finito e non si
finge.

⭐⭐⭐ LA COSA DELLA GIORNATA E' QUI, ED E' UNA PAROLA: 忘却.
BURT, a **Zaile**, dice due cose di fila: 「今ではどんな景色だったのか思い出せ
ない」 — non ricorda **piu'** che panorama fosse — e 「やがて忘却に呑まれてしま
うだろう」, prima o poi ci inghiottira' **l'oblio**. E 忘却 non e' una parola
generica in questo gioco: e' il nome della cosa contro cui MIKRAANESIS sta
combattendo (`:18095`-`:18098`, gia' rese: «la **dea dell'oblio**», «un aspetto
dell'oblio che ha preso corpo in forma di divinita'»), ed e' quella che a
`:10353` «cancella il ricordo dalla gente».

Con questa riga i quattro buchi di memoria della giornata smettono di essere
quattro tic e diventano **una cosa sola, che nella trama ha gia' un nome**:
  - NANCY (`:15355`), che viene **da Zaile** — la citta' di Burt — e non ricorda
    che cosa le sia sparito;
  - CRAY (`:15407`), che non ricorda chi si sia buttato nella fenditura;
  - NERES e RYUTYE (`:12876`, `:12897`, `:12898`), a cui manca tutto;
  - MANSON (`:15385`, 94a), che ha perso il senso del tempo.
⚠️ Nessuna delle nove rese alleggerisce il buco, e `:15138` in particolare
tiene il **piu'** che l'inglese pure ha («I can't remember what the view was
like»): senza quello la riga dice che non ha mai saputo, invece che ha
dimenticato.

LESSICO EREDITATO (non deciso qui):
  - 忘却            «l'oblio», «la dea dell'oblio»  `chat.hsp:18095`, `:10353`
  - ジュア様        «Jure», senza titolo            `db_creature.hsp:72943`,
                                                    `chat.hsp:3266`
  - 永遠の盟約      «il patto eterno»               `text.hsp:9695`
  - 神殿 (questo)   «il santuario»                  `text.hsp:2941`
  - 音楽チケット    «biglietto per il concerto»      `db_item.hsp:142700`
  - カードパック    «pacchetto di carte»            `db_item.hsp:141802`
  - パーティを開催  «dare una festa»                 `chat.hsp:7747`

⭐ IL BLOCCO DI WEL HA UNA GEMELLA GIA' RESA, E NON E' SUO NONNO.
`chat.hsp:7747` — RICH_PERSON_STOKE — fa lo **stesso scambio** e lo dice quasi
con le stesse parole: «Hai dei biglietti per il concerto? Restarne senza quando
voglio dare una festa e' sempre una seccatura.» Le due rese si accostano
apposta. ⚠️ Ma Stoke **non e' il nonno di Wel**, per quanto la riga di Wel parli
proprio di un nonno che resta senza biglietti per le feste: `map.hsp:8616` mette
Stoke ad **Arcbelc** e `:2088` mette Wel a **Larna**. Sono due persone e due
citta': la somiglianza e' del mestiere, non della famiglia. (Controllato prima
di scriverlo, perche' scritto qui sarebbe stato creduto.)

⚠️ DEROGA 1 — `:11901`, L'INGLESE E' ROTTO.
«...no matter where people gather, someone who starts business in this sacred
place comes out come and is.» non e' una frase. Il giapponese e' chiaro:
まさか…者が出てくるとは, cioe' *non mi sarei mai aspettato che saltasse fuori
qualcuno che si mette a commerciare qui*. Si segue il giapponese (57a).

⭐ DEROGA 2 — ジュア様 RESTA «JURE» NUDO, E LA DEVOZIONE LA PORTA IL RESTO.
Il progetto non traduce mai il 様 di ジュア様: «Tutto per Jure...»
(`db_creature.hsp:72943`), «Sara' la protezione di Jure?» (`chat.hsp:3266`).
Rovid ne dice tre in tre righe, e il suo trasporto sta gia' nei sospiri
(「はぁ…ジュア様…」) e nel «era stupenda»: aggiungere un titolo qui vorrebbe dire
dargli un tono che le altre rese di Jure non hanno.

⚠️ DEROGA 3 — `:15135`, BURT DA' DEL **TU**, E NON E' UNA SCELTA MIA.
お前 al giocatore, 俺 di se': e' la seconda persona piu' bassa del giapponese.
Nessuna cortesia, quindi, in un lotto dove ROVID parla in 敬語 e WEL e' un
bambino. I tre registri restano distinti perche' lo sono nel giapponese.

PERIMETRO: 12 firme su 12 dentro i tre blocchi, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 9188 11893 15132`), zero gia' rese altrove.

MENU: quello di WEL, ma le sue voci (`:9195`, `:9201`, `:9206`, `:9209`) sono
**gia' rese**: qui c'e' solo il `buff` (`:9210`).

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- WEL, il bambino di Larna che scambia biglietti
    9190: 'Mio nonno dà un sacco di feste, ma resta sempre senza biglietti per '
          'il concerto e non sa che pesci pigliare.',
    9210: 'Senti, non è che vuoi scambiare dei biglietti per il concerto con '
          'qualche oggetto?',
    9222: 'Me ne dai così tanti? E allora tieni, questo è per te!',
    9230: 'Affare fatto! Tieni, questo pacchetto di carte è tuo!',
    9233: 'Ah, no? E va bene, allora niente.',

    # --- ROVID, che custodisce il santuario e sospira per Jure
    11898: 'Questo è anche il luogo dove gli dei strinsero il patto eterno. '
           'Quella volta pure Jure era tesa, ed era stupenda... Ah... Jure...',
    11901: 'Siccome è cominciata l\'invasione vera e propria del caos non '
           'abbiamo avuto scelta: abbiamo aperto il santuario e con una parte '
           'della forza divina l\'abbiamo collegato alla superficie. Ma che, '
           'approfittando della gente che si raduna, saltasse fuori qualcuno '
           'a mettersi a commerciare in un luogo sacro come questo, non me lo '
           'aspettavo.',
    11905: 'A dire il vero vorrei stare al seguito di Jure... ma la guardia '
           'del santuario me l\'ha affidata Jure stessa, e non posso mica '
           'piantarla lì.',

    # --- BURT, a Zaile, dove il panorama non si ricorda più
    15135: 'Fuori dalla città è pericoloso. Ma se tu vuoi andare '
           'all\'avventura, io non ho nessun diritto di fermarti.',
    15138: '...Mi piaceva il panorama che si vede da qui, di là dal mare. Ma '
           'adesso non riesco più a ricordarmi com\'era. Anche di là dal mare '
           'se lo sono mangiato loro, e l\'hanno dipinto tutto di nero.',
    15139: 'Anche noi tiriamo avanti a stento, e prima o poi ci inghiottirà '
           'l\'oblio. Probabilmente è quello, il nostro destino.',
    15140: 'Ma dentro la città i campi si possono coltivare lo stesso, e '
           'l\'acqua dal pozzo si tira su ancora. Io fino all\'ultimo momento '
           'mi ci impunto.',
}
