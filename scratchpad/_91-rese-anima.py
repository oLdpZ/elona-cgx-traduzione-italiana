# -*- coding: utf-8 -*-
"""91a - L'ANIMA SMARRITA (`chat.hsp:10551`-`:10626`, 20 firme).

「迷い子」, «l'anima smarrita» (`db_creature.hsp:44807`, `db_card.hsp:1427`) —
alla lettera *il bambino smarrito*. E' un'anima di bambino prigioniera dei
demoni nella **Gabbia di Amur** (`text.hsp:2929`), e la manda a cercare
<Amurdad>, che dalla Gabbia non puo' uscire (`chat.hsp:10673`, ancora da
rendere). Si trova al livello 60, la si scorta fino al livello 1 e la' la si
saluta.

⭐ IL BLOCCO E' QUASI TUTTO IL GIOCATORE CHE PARLA. Sedici firme su venti sono
`chatList`, cioe' **le battute che il giocatore sceglie**: tre gentili e una
brutale, ogni volta. La quarta e' sempre 「クソガキ」, ed e' la stessa in tutti
e tre i momenti — il gioco offre di essere crudele con un bambino che piange,
tre volte, e va reso senza addolcirlo.

REGISTRO: il bambino parla come un bambino spaventato — frasi mozze,
「こわいよぉ」, 「が、がんばる」. Il giocatore ha quattro registri diversi nello
stesso menu, e vanno tenuti distinti: promessa, incoraggiamento, sfogo, insulto.

LESSICO EREDITATO (non deciso qui):
  - «l'anima smarrita»                db_creature.hsp:44807, db_card.hsp:1427
  - «Gabbia di Amur»                  text.hsp:2929; «Gabbia Oscura» per 闇檻
                                      nudo, text.hsp:11274
  - «<Amurdad>»                       text.hsp:11274, :11284

⭐⭐⭐ DEROGA 1 — IL SESSO DEL BAMBINO E' TIRATO A SORTE, E LO DICE IL CODICE.
Non e' prudenza mia: `db_creature.hsp:44851` fa

    if ( cdata(CDATA_SEX, rc) == 1 ) { cdata(CDATA_PIC, rc) = xy2pic(27, 10) }

cioe' **cambia il ritratto secondo il sesso**, che per questa creatura non e'
fissato da nessuna parte. Il bambino che il giocatore scorta puo' essere un
maschio o una femmina, e cambia da partita a partita.

Quindi qui la regola del genere non vale solo per il giocatore: vale anche per
**l'interlocutore**. Nessun participio e nessun aggettivo riferito al bambino:
  - 「ここまでよく頑張った！」  ->  «Ce l'hai fatta alla grande!», non «sei
    stato bravissimo»;
  - 「黙って走れ」  ->  «Silenzio e corri!», non «zitto/zitta».

⭐⭐ DEROGA 2 — 「クソガキ」 E' «PESTE», NON «MOCCIOSO».
Il progetto ha gia' reso 「出ていけクソガキ」 con «Fuori di qui, moccioso»
(`chat.hsp:804`), e la parola sarebbe quella. Ma li' il bersaglio e' un
personaggio di sesso noto, qui no (DEROGA 1): «moccioso» darebbe un sesso al
bambino, e a schermo uscirebbe sbagliato una volta su due.

**«peste» funziona per tutti e due** («sei una peste» si dice a un maschio e a
una femmina) e tiene la stessa villania. E' lo stesso gesto della 90a — si
tiene la parola e si sposta quel che porta il genere — applicato a un
sostantivo invece che a un bersaglio.

⭐ DEROGA 3 — `:10618`, IL NOME CHE NON PUO' TORNARE.
Il giapponese e' `name(tc) + "を保護した。無事に連れて帰らなければ。"`;
l'inglese e' una stringa **nuda**, «You must return the child safely.», senza
`name()`. Siccome `applica` sostituisce il letterale inglese, la voce e'
**statica** e nel posto dell'italiano non ci puo' stare un'espressione: il nome
non e' recuperabile senza una toppa, e per una riga sola non la vale. Si scrive
«quell'anima», che dice la stessa cosa e non ha bisogno del nome.

ALTRE DEROGHE DICHIARATE
4. `:10578` - 「泣きたいのはこっちだよ～！」 finisce con la tilde a doppio byte,
   che non si puo' scrivere (89a). Lo strascico passa nei puntini.
5. `:10563` e `:10580` - le due dinamiche con `name(tc)`. Terza persona
   presente, come vuole la guida di stile, e l'accordo si appoggia a un
   sostantivo **mio** («la sua figura») invece che a `name()`, che il giocatore
   puo' anche aver rinominato.
6. `:10593` e `:10594` - 「一緒に探してあげる」 non dice **cosa** si cerca:
   lo dice la riga di sopra, 「お母さん…どこ…」. In italiano il pronome basta
   («La cerchiamo insieme»), e la riga dopo nomina il papa', come il
   giapponese.

PERIMETRO: 20 firme su 20 nel blocco, zero occorrenze fuori dal blocco
(`python scratchpad/_85-blocco.py 10551`).

MENU: tre, da 4 voci l'uno — il tetto delle due colonne non morde (soglia 10).

⚠️ Accenti veri; niente virgolette tipografiche e niente caratteri a due byte.
"""

RESE = {
    # --- livello 1: il congedo
    10555: 'Ce l\'hai fatta alla grande!',
    10556: 'Adesso sei al sicuro...',
    10557: 'Eh, qui è caldo?',
    10558: 'E vivi felice, peste',
    10559: 'Qui... si sta al caldo, vero...',
    10563: 'name(tc) + ": la sua figura si fa tenue, e sparisce..."',

    # --- livelli 31-32: il crollo a metà strada
    10575: 'Non ce la faccio più...!',
    10576: 'Ti prometto che ti proteggo!',
    10577: 'Manca poco, resistiamo insieme?',
    10578: 'Quello che vorrebbe piangere sono io...!',
    10579: 'Silenzio e corri, peste',
    10580: '"(" + name(tc) + " si rannicchia e scoppia a piangere...)"',
    10583: 'C-ci provo...',

    # --- livello 60: l'incontro
    10592: 'Sono qui per salvarti!',
    10593: 'La cerchiamo insieme',
    10594: 'Cerchiamo anche il tuo papà, va bene?',
    10595: 'Muoviti e seguimi, peste',
    10596: 'Mamma... dove sei... Ho paura...!',
    10599: 'S-sì...',
    10618: 'Adesso quell\'anima è al tuo riparo: bisogna riportarla a casa '
           'senza un graffio.',
}
