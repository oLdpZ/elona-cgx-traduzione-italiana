# -*- coding: utf-8 -*-
"""93a - NORNE la guida (`chat.hsp:9431`-`:9600`, 11 firme su 56).

ガイドの『ノルン』 / `<Norne> the guide` (`db_creature.hsp:17329`, `:77957`,
`db_card.hsp:7009`) e' l'elun che accompagna il giocatore dall'inizio: e' lui
che ti convoca a Irva Perduta, che ti riporta a Tyris del Nord, e che a fine
trama racconta Gaius Vis. Il blocco era gia' lavorato per due terzi (45 firme su
56): quello che resta sono i **quattro punti di servizio** — i due traghetti,
il richiamo al Santuario e il primo incontro dopo la convocazione.

⭐ IL REGISTRO E' GIA' FISSATO, e non si decide qui. Le 45 rese del blocco piu'
le quattro battute di creatura danno un ragazzo sbrigativo e un po' impertinente,
che da' del tu e non fa mai il solenne:

    db_creature.hsp:77931  «Io non sono una fata cattiva.»
    db_creature.hsp:77931  «Ma insomma, qui c'e' da insegnarti un po' di cose.»
    db_creature.hsp:77943  «Ripassa un'altra volta.»
    chat.hsp:9457          «Mmh. Pero' la tua percezione non ha ancora seguito...»
    chat.hsp:9469          «Ah, giusto: avevo una cosa da darti.»

LESSICO EREDITATO (non deciso qui):
  - ロストイルヴァ   «Irva Perduta»      text.hsp:2917, e 12 siti in chat.hsp
  - ノースティリス   «Tyris del Nord»    chat.hsp:9519 (la voce gemella di questo menu)
  - 中央神殿         «Santuario Centrale» text.hsp:2941
  - エウダーナ       «Eulderna»          db_race.hsp:1193
  - 案内する         «accompagnare»      chat.hsp:1410, :6913, :8355, :8362, :24886

⭐ DEROGA 1 — 「ご案内～」, E IL SEGNO DELLA VOCE STRASCICATA.
`:9527` e `:9556` sono la voce di servizio di Norne, con la 「～」 finale che ne
allunga la vocale. ⚠️ La 「～」 a doppia larghezza e' fra i caratteri proibiti
(la guardia di `guardie.py`), ma il progetto ha gia' due modi di renderla e
tutt'e due usano la **tilde ASCII**: `chat.hsp:809` («a come disponi i mobili~»),
`:813`, `:3732`. Si segue quella strada invece di raddoppiare la vocale, che qui
cadrebbe su un nome proprio.

⭐ DEROGA 2 — `:9542`, 冷やかし NON E' «MI STAI PRENDENDO IN GIRO?».
La stessa parola nuda e' gia' resa cosi' a `chat.hsp:19990` e `:20093`, ma li'
e' la **voce di un menu** con cui si declina un'offerta. Qui e' il predicato di
una frase che Norne dice **dopo** che il giocatore ha risposto «Lascia stare»:
non lo accusa di scherzare, si lamenta di aver perso tempo. L'inglese lo scioglie
in «Don't bother me then.», ed e' la stessa cosa. ⚠️ Va tenuto il **motivo** che
il giapponese mette e l'inglese butta (se non fai sul serio), perche' e' quello
che rende la riga una lamentela e non un rifiuto.

⚠️⚠️ DEROGA 3 — `:9587` e `:9590`, DUE PARTICIPI CHE DAREBBERO UN GENERE AL
GIOCATORE. 立派な冒険者になった e 戸惑っている sono tutt'e due riferiti a chi
legge: «sei diventato un avventuriero» e «sei disorientato» sbagliano meta' delle
partite. Si esce dal participio con un **sostantivo** e con la formula che il
progetto usa gia' per 冒険者 rivolto al giocatore (`chat.hsp:3495`, `:3517`:
«chi va all'avventura», «tu che vai all'avventura»): «di strada ne hai fatta» e
«un po' di smarrimento, eh?». ⚠️ E' la stessa mossa della deroga 4 della 92a.

⚠️ 神々 e' «gli dei» senza accento: `verifica` boccia «dèi» perche' la
degradazione a CP932 ci mette l'apostrofo dentro («de'i»), e il progetto scrive
gia' «gli dei» / «degli dei» in dodici siti (`chat.hsp:10179`, `:10193`,
`:10224`, `:10261`, `:13642`).

⭐ DEROGA 4 — `:9577`, 地上へ降りる E' «SCENDERE IN SUPERFICIE», ALLA LETTERA.
Il richiamo si legge stando a **Irva Perduta**, che e' un continente che fluttua
sopra Eulderna (lo dice `:9590`, due battute piu' sotto): il verbo «scendere» non
e' una metafora e va tenuto.

PERIMETRO: 11 firme da fare su 56 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 9431`) e **zero firme gia' rese altrove**
(ricerca per firma su tutti i `dizionario/*.jsonl`).

MENU: i tre menu del blocco (`:9517`-`:9518`, `:9546`-`:9547`, `:9575`-`:9576`,
`:9588`-`:9589`) sono **gia' resi**: il lotto non ne tocca nessuno.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte
(i puntini di sospensione si scrivono con tre punti).
"""

RESE = {
    # --- il traghetto per Tyris del Nord (Santuario Centrale)
    9527: 'Bene! Ti accompagno io a Tyris del Nord~',
    9542: 'Se non fai sul serio, mi fai solo perdere tempo.',

    # --- il traghetto per Irva Perduta (Larna)
    9548: 'Vuoi andare a Irva Perduta?',
    9556: 'Bene! Ti accompagno io a Irva Perduta~',

    # --- il richiamo al Santuario, a strada aperta
    9577: 'Ah, eri qui! Capiti a proposito. Con la forza degli dei si è '
          'aperta la via che porta a Tyris del Nord. Se anche tu vuoi '
          'scendere in superficie, vieni al Santuario Centrale. Ti aspetto.',
    9580: 'Uff. Ma che stai dicendo?',
    9582: 'Allora, alla prossima.',

    # --- il primo incontro dopo la convocazione a Irva Perduta
    9587: 'Quanto tempo... o no? Non ti vedevo da un po\' e a quanto pare, '
          'nell\'avventura, di strada ne hai fatta parecchia. Vuol dire che '
          'ho fatto bene a farti da guida.',
    9590: 'Un po\' di smarrimento, eh, a farsi convocare così di colpo? Qui '
          'siamo a Irva Perduta, il continente che fluttua sopra Eulderna. '
          'In quelle rovine c\'è un mucchio di gente chiamata qui prima di '
          'te: per i dettagli conviene che lo chieda a loro.',
    9593: 'Mh? Scusa, ma non sono così libero da stare ai tuoi scherzi.',
    9595: 'Allora io vado. Ci sono altri avventurieri da accompagnare, sai. '
          'Uff, che daffare.',
}
