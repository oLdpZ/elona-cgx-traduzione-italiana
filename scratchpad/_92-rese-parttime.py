# -*- coding: utf-8 -*-
"""92a - L'AIUTANTE A ORE DEL MAESTRO SPADA ROSSA (`chat.hsp:14525`-`:14659`,
18 firme).

『赤剣先生のバイト』 = **«l'aiutante a ore del maestro Spada Rossa»**
(`db_creature.hsp:54727`, `db_card.hsp:3169`). E' chi sta all'ingresso del
**Seminario d'Avventura** (`text.hsp:2866`) e vende i corsi: e' il banco di
iscrizione del tutorial del gioco, cioe' una delle prime cose che un
giocatore nuovo legge.

⭐ IL BLOCCO E' DUE MENU IN FILA, non un dialogo: prima la materia (quattro
corsi), poi l'incontro (dal primo al quarto, col prezzo che cambia). Le
quattro materie e i quattro docenti sono **gia' resi nella 87a**, e i nomi non
si ridecidono qui.

LESSICO EREDITATO (non deciso qui):
  - 冒険ゼミ        «il Seminario d'Avventura»      text.hsp:2866
  - 生活講座        «corso di vita quotidiana»      chat.hsp:13954 (Ajira)
  - 道具講座        «corso sugli oggetti»           chat.hsp:14103 (Cresce)
  - 育成講座        «corso di crescita»             chat.hsp:14245 (Iduru)
  - 戦闘講座        «corso di combattimento»        chat.hsp:14385 (Mitorin)
  - 第N回           «N incontro»                    chat.hsp:14117, :14123, :14397
  - gp              «oro»                           chat.hsp:8825, :8832, :8835
  - 赤剣先生        «maestro Spada Rossa»           db_creature.hsp:54727

REGISTRO: e' un ragazzo che fa un lavoretto e ci mette entusiasmo — 「キミ」 in
katakana, esclamativi dappertutto, tono da volantino. Italiano vivo e
informale, mai burocratico: e' la voce che deve far venire voglia di entrare.

⭐⭐⭐ DEROGA 1 — `:14529`, L'INGLESE CANCELLA IL DATORE DI LAVORO.
Il giapponese e' 「全ての講座を修了したキミには、赤剣先生の問題を…昔なら受け
てもらうところなんだけどね。」: a chi ha finito tutti i corsi toccherebbe **la
prova del maestro Spada Rossa**, e una volta gliel'avrebbe fatta fare. L'inglese
butta via il maestro e scrive «You kinda remind me of myself from back in the
day...», che dice un'altra cosa.
⚠️ E il maestro non e' un dettaglio di colore: **e' nel nome di chi parla**
(«l'aiutante a ore del **maestro Spada Rossa**»). Toltolo, la battuta finale
del ramo piu' difficile del tutorial non nomina piu' nessuno, e il giocatore
non sa piu' di chi sia il seminario dove ha passato quattro lezioni.

⭐⭐ DEROGA 2 — `:14548`, L'INGLESE GIRA L'INVITO IN CONSTATAZIONE.
「キミに合った講座を選んで、華麗にスタートダッシュを決めよう！」 e' un
incoraggiamento **prima** della scelta («scegli il corso che fa per te e...»);
l'inglese scrive «The course fit for you has been chosen. What a magnificent
decision!», cioe' un complimento **dopo**. ⚠️ Ma la riga e' il `buff` che sta
sopra il menu delle quattro materie (`:14543`-`:14547`): a schermo il giocatore
la legge **mentre sceglie**, e la versione inglese si congratula per una scelta
che non e' ancora stata fatta. Si segue il giapponese.

⚠️ DEROGA 3 — 努力賞 QUI NON E' IL «PREMIO DI CONSOLAZIONE» DI `:13082`.
La' (「一応努力賞出しておくね。一応、ね。」) e' il contentino di chi non ha
vinto, e «premio di consolazione» ci sta. Qui e' il premio di chi ha finito
**tutti e sedici** i pezzi del seminario (`:14527` somma sedici bandiere): e'
«il premio per l'impegno», e chiamarlo di consolazione lo rovescerebbe.

💡 `:14616` in inglese e' «**Forth** Time», refuso di upstream. Non si ricopia.

PERIMETRO: 18 firme su 19 dentro il blocco, zero occorrenze fuori
(`python scratchpad/_85-blocco.py 14525`). La diciannovesima e' 「！！」
(`:14528`), gia' resa.

MENU: due. Il primo ha 5 voci, il secondo 5: sotto le dieci, quindi **una
colonna sola** e tetto 58 caratteri (`strumenti/menu_dialogo.py`) — le due
colonne e il loro tetto 24 non mordono. La voce piu' lunga scritta qui e'
«Seminario d'Avventura - corso di vita quotidiana», 48.

⚠️ Le quattro voci col prezzo sono **dinamiche**: `gp1`..`gp4` cambiano da 20 a
5 quando il corso e' gia' stato fatto (`:14556`-`:14611`), quindi la variabile
va conservata dov'e'.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte
(le parentesi tonde sono ASCII, non （）).
"""

RESE = {
    # --- il ramo di chi ha finito tutto: sedici bandiere a 100
    14529: 'Adesso che li hai finiti tutti, ci sarebbe la prova del maestro '
           'Spada Rossa... Una volta te l\'avrei fatta fare, sai.',
    14530: 'Ecco, questo è il premio per l\'impegno. E continua così!',

    # --- il ramo "hai gia' studiato oggi"
    14539: 'Imparare tante cose in una volta è dura, vero? Ecco perché '
           'ognuno può seguire un corso solo al giorno. Quello che hai '
           'imparato oggi, mettilo subito in pratica!',

    # --- primo menu: la materia
    14542: 'Al Seminario d\'Avventura anche tu puoi cominciare alla grande la '
           'tua vita d\'avventura. Che ne dici?',
    14548: 'Scegli il corso che fa per te e parti col piede giusto, in '
           'bellezza!',
    14543: 'No, grazie',
    14544: 'Seminario d\'Avventura - corso di vita quotidiana',
    14545: 'Seminario d\'Avventura - corso sugli oggetti',
    14546: 'Seminario d\'Avventura - corso di crescita',
    14547: 'Seminario d\'Avventura - corso di combattimento',

    # --- secondo menu: quale incontro, e quanto costa
    14617: 'Quale incontro vuoi seguire? Il consiglio è di farli in ordine!',
    14612: 'Ripensandoci, lascio stare',
    14613: '"Primo incontro (" + gp1 + " oro)"',
    14614: '"Secondo incontro (" + gp2 + " oro) - serve livello 2"',
    14615: '"Terzo incontro (" + gp3 + " oro) - serve livello 4"',
    14616: '"Quarto incontro (" + gp4 + " oro) - serve livello 6"',

    # --- gli esiti
    14634: 'Ehi? I requisiti non ci sono. Ricontrolla bene!',
    14642: 'Mi raccomando, studia sul serio! Se ascolti distrattamente, butti '
           'via tempo e soldi!',
}
