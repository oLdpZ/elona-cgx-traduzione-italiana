# -*- coding: utf-8 -*-
"""94a - SAIMEF il dio cane (`chat.hsp:9693`-`:9723`, 7 su 7).

白氷の『サイメーブ』 / `<Saimef> the doggod`, reso **«<Saimef> il bianco
ghiaccio»** (`db_card.hsp:3936`, `db_creature.hsp:59285`). ⚠️ Il nome italiano
viene dal giapponese 白氷 e non dall'inglese `doggod`: e' gia' deciso.

⭐ IL REGISTRO E' GIA' FISSATO dalle sue **due battute** rese in un lotto
precedente (`db_creature.hsp:59265`, `:59271`): «Che cosa mai...» e ⭐ «Che
almeno il tuo sonno sia sereno.» — solenne, mite, e **da' del tu**. In chat usa
ですます con 君 e si chiama 自分, quindi la cortesia c'e' ma non e' il keigo che
farebbe scattare la regola del voi dell'88a: e la sua battuta gia' resa lo
conferma con un possessivo di seconda persona singolare.

LESSICO EREDITATO (non deciso qui):
  - 犬神        «dio cane»            `text.hsp:3030` (la Foresta del Dio Cane)
  - 神の間      «il Sigillo Eterno»   `chat.hsp:7829`, `:7830`, `action.hsp:3008`
  - 神力        «potere divino»       `chat.hsp:10179`, `adv.hsp:69`
  - ヨロテオトル «Yoloteotl»          `item.hsp:110` — **e' il nome dell'oggetto**
  - ノイエル / メイルーン  «Noyel» / «Mayroon»   `chat.hsp:2124`, `:2125`
  - 銀髪の子    Marka, «i capelli d'argento»   `main.hsp:5393`, `chat.hsp:2125`
  - 混沌の神    «il dio del caos»     30 siti
  - 露払い      «ripulire la strada»  `chat.hsp:18160` — **e AIKAGE, oggi**

⚠️⚠️⚠️ DEROGA 1 — `:9703`, L'INGLESE SBAGLIA LA FRASE CHE SPIEGA PERCHE' E' LI'.
Il giapponese e' 「後続のためにここで露払いをしているというわけです」: sta li' a
**ripulire la strada per quelli che verranno dopo**. L'inglese scrive «For the
sake of my **followers**, I must **stop my quest** here» — 後続 non sono i suoi
fedeli ma chi viene dietro, e 露払い sparisce del tutto. ⭐ E' la **seconda
volta oggi** che 露払い compare (l'altra e' AIKAGE a `:15078`) e la **seconda
volta** che l'inglese la butta: la resa e' la stessa in tutt'e due, come vuole
il precedente di `chat.hsp:18160`.

⚠️ DEROGA 2 — `:9697`, ヨロテオトル NON E' UN VOCATIVO.
Sembra il nome di qualcuno a cui si rivolge; e' invece il **nome dell'oggetto**
che ha appena strappato dal petto — `item.hsp:110` lo elenca fra gli `evitemn`
come la resa giapponese di `god heart`, gia' resa «Yoloteotl». La riga sta
nominando quello che ha dato, non chiamando nessuno.

⚠️⚠️ DEROGA 3 — `:9705`, IL GIAPPONESE E' DINAMICO E L'INGLESE NO, QUINDI
L'ITALIANO **NON PUO'** ESSERE DINAMICO. Il sito e'

    lang("(突然、" + name(tc) + "は自らの胸を抉りぬいた！)",
         "(Suddenly, Saimef reaches into his own chest and pulls out his heart!)")

Il giapponese concatena `name(tc)`; l'inglese inchioda «Saimef» in un letterale
nudo. ⚠️ E la voce e' classificata **`statica`** proprio per questo: la classe
la decide l'**inglese**, che e' il lato che si sostituisce. `applica.riscrivi_statica`
mette la resa dentro `"..."` e basta, quindi un'espressione HSP scritta qui
finirebbe **a schermo come testo**. Il nome si scrive per esteso, come fa
l'inglese: non e' una scelta di resa, e' cio' che il sito consente.
💡 E 抉りぬいた e' piu' forte di «reaches into»: e' scavare **da parte a parte**.

⚠️ DEROGA 4 — `:9702`, 君たち E' PLURALE.
Saimef ha portato **due** persone — il giocatore e Marka l'orsa d'argento
(`chat.hsp:2125`, «Andrai a Mayroon via terra da Noyel, insieme all'orsa
d'argento... a Marka») — e la riga dopo, `:9704`, nomina proprio lei. L'inglese
mette «you» e il plurale si perde; in italiano si dice «voi due», che e' anche
l'unica forma che non attribuisce un genere al giocatore.

PERIMETRO: 7 firme su 7 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 9693`), zero gia' rese altrove.

MENU: nessuno. `:9697` e `:9708` chiudono (`strbye` / `chat_end`).

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- dopo il dono, quando lo si ritrova
    9697: 'Yoloteotl... Anche senza il cuore di un dio, finché mi resta il '
          'potere divino il corpo regge. Non stare in pensiero per me.',

    # --- l'incontro nella Culla del Caos
    9701: 'Oh, tu... Ci incontriamo di nuovo.',
    9702: 'Non ti ricordi di me? Sono il dio cane che ha portato voi due da '
          'Noyel a Mayroon. Attraversare di corsa il grande ghiacciaio stanca, '
          'come è ovvio, e alla battaglia contro il demone non ho potuto '
          'prendere parte; ma il vostro scontro l\'ho seguito con gli occhi.',
    9703: 'Perché sono qui? Ho pensato che qualcosa potessi farla anch\'io, e '
          'sono venuto in questo continente puntando al Sigillo Eterno... ma '
          'mi hanno avvertito che a un dio che scende fino al piano più '
          'profondo il potere divino viene risucchiato via. Sì, me l\'ha detto '
          'una fata incontrata per strada. Così non mi è restato altro: sto '
          'qui a ripulire la strada per quelli che verranno dietro.',
    9704: 'Che ci si incontri qui è un segno... Beh, l\'ho incontrata anche '
          'quella dai capelli d\'argento che quella volta era con te, ma non '
          'ha voluto starmi a sentire. Io voglio scommettere su di te, che hai '
          'salvato Mayroon, la mia terra.',
    9705: '(Di colpo Saimef si squarcia il petto da parte a parte!)',
    9708: 'Agh... Aaah...! È... è poca cosa, ma fanne buon uso. Ti prego, il '
          'dio del caos...!',
}
