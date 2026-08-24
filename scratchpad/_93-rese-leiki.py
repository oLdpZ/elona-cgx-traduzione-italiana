# -*- coding: utf-8 -*-
"""93a - LEIKI la tartaruga nera (`chat.hsp:8695`-`:8774`, 15 firme su 20).

玄武の『レイキ』 / `<Leiki>` (`db_creature.hsp:86680`, `db_card.hsp:8499`, reso
**«<Leiki> la tartaruga nera»**) e' il servitore della principessa degli abissi
di Valm. Fa da traghetto per il castello sommerso e sta sulla spiaggia:
`text.hsp:10843` («Dalla spiaggia di Valm devo farmi portare al castello dalla
tartaruga») e' la voce di diario che manda il giocatore da lui.

⭐ IL REGISTRO E' GIA' FISSATO DA DUE PARTI, e nessuna delle due si decide qui:

  - **Leiki da' del TU** — `map.hsp:15070`, l'unica sua riga gia' resa fuori da
    questo blocco: «Oltre non si puo', la mente si spezzerebbe! Ti tiro fuori
    io!». Quindi niente «lei» da maggiordomo, per quanto il giapponese sia in
    keigo fitto: e' deferente **verso la principessa**, non verso chi ascolta;
  - **la principessa e' vecchia e parla in わし/じゃ** (`:8490`-`:8557`, gia'
    rese): «Ti sto dando un bel po' di pensieri, eh...», «Guarda che disastro».
    Leiki le sta sotto e la chiama 姫様: «la principessa», con l'articolo.

LESSICO EREDITATO (non deciso qui):
  - 精神波     «onde mentali»   chat.hsp:8537 e :24451 (la principessa e il
               bollettino del drago a nove teste). ⚠️ `proc.hsp:18353` e
               `:25071` dicono «onda psichica», ma sono i messaggi di
               combattimento di una mossa qualunque: qui la cosa e' quella di
               `:8537`, cioe' la telepatia dell'antenato, e la parola la sceglie
               quel filo.
  - ヴァルム   «Valm»           text.hsp:762, map.hsp:4063
  - 亀         «tartaruga»      chat.hsp:8512, :8516, item_data.hsp:1715

⚠️⚠️ DEROGA 1 — 冒険者様 NON DIVENTA «AVVENTURIERO».
`:8702` e `:8734` chiamano il giocatore per mestiere, e in italiano il nome del
mestiere porta un genere. Il progetto ha gia' la formula per il vocativo:
«tu che vai all'avventura» / «ecco chi va all'avventura» (`chat.hsp:1469`,
`:1498`, `:1502`, `:3495`, `:3517`). ⚠️ Vale anche a `:8706`, dove pero'
冒険者様 non e' un vocativo ma un indefinito («portare **un** avventuriero»):
li' diventa «qualcuno che va all'avventura».

⚠️ DEROGA 2 — `:8745`, 準備ができたら SENZA PARTICIPIO.
«Quando sei pronto» concorda col giocatore. Il progetto scioglie gia' questa
formula in tre modi che il genere non ce l'hanno: «Quando sei in ordine fammi un
cenno» (`chat.hsp:6913`), «Fammi un cenno quando e' il momento» (`:8355`). Qui:
«Quando e' il momento, fammi un cenno».

⭐⭐ DEROGA 3 — `:8741`, 亀助け E' UN GIOCO DI PAROLE E VA RIFATTO.
Il giapponese storpia 人助け («dare una mano al prossimo») in 亀助け, cioe'
sostituisce **il prossimo con la tartaruga**: e' la stessa forma della battuta
di Alice nella 92a — il senso non sta nelle parole ma nella sostituzione.
L'inglese la scioglie in una frase piana («a favor for this old tortoise»). In
italiano l'espressione fissa c'e' («aiutare il prossimo») e la sostituzione si
puo' fare uguale, marcandola con un «cioe'» che la rende volontaria e non un
lapsus del traduttore.

⭐ DEROGA 4 — `:8706`, LA CITAZIONE CHE L'INGLESE BUTTA.
Il giapponese dice **perche'** i forti della citta' non ci sono piu': se ne sono
andati dicendo 「戦争中の国を説得してやろうと思う」. L'inglese lascia solo
«apparently they're all gone!». La frase fra virgolette torna dentro: e' l'unica
riga del blocco che lega Valm al resto della trama.

💡 CONTROLLO DEL VICINATO (la rete della 92a): `text.hsp:1022`-`:1035` e' il
quiz «qual e' il nome esatto della tartaruga di Valm?», dove l'inglese **cambia
la domanda** (il giapponese chiede il nome della principessa, 深海の姫, e
risponde ミヅキ). Le quattro voci italiane seguono l'inglese **tutte e quattro**,
domanda compresa: il quiz e' coerente e non c'e' niente da riparare.

⚠️ La citazione di `:8706` porta le virgolette **protette** (`\\"`), come fa
l'inglese di monte: una `"` nuda spezzerebbe la stringa HSP che scrive
`applica.py`, e `verifica` la boccia. Le tipografiche non sono un'alternativa
(due byte in CP932, un glifo per byte a schermo).

PERIMETRO: 15 firme da fare su 20 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 8695`) e **zero firme gia' rese altrove**.

MISURA (`chat-lotto-misura`): 0 fuori misura, **1 riga in piu' dell'inglese**, ed
e' `:8706` (8 righe contro 7). La domanda della 90a — *di chi e' la riga in
piu'?* — qui ha due risposte diverse: su `:8702` era **mia** (il vocativo lungo
al posto di «Adventurer») e la riga si e' riassorbita girando la frase; su
`:8706` e' **dell'inglese**, che la citazione dei forti partiti non ce l'ha. La
prima si accorcia, la seconda si tiene.

MENU: due, da 3 e da 2 voci. Del primo (`:8703`-`:8705`) erano gia' rese due
voci su tre e la terza sta nel dizionario da un altro sito; del secondo
(`:8750`-`:8751`) sono nuove tutt'e due.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte
(i puntini di sospensione si scrivono con tre punti).
"""

RESE = {
    # --- il ritorno, a missione fatta
    8698: 'Grazie ancora di quella volta! ...Mi farebbe piacere se scambiassi '
          'due parole anche con la principessa. A dire il vero, da allora se '
          'ne sta sempre chiusa in sé.',

    # --- la chiamata d'emergenza: le onde mentali dell'antenato
    8702: 'Ti prego, aiutaci tu che vai all\'avventura! La principessa è al '
          'limite: non trattiene più le onde mentali!',
    8706: 'Ero venuto in città a chiedere aiuto ai più forti del posto, ma '
          'erano già partiti tutti: \\"andiamo a convincere un paese che è in '
          'guerra\\", pare abbiano detto! La principessa ha sempre sognato il '
          'mondo di superficie... e proprio ora che il sogno si è avverato si '
          'ritrova a far soffrire quella stessa gente... Almeno, almeno '
          'portandole qualcuno che va all\'avventura voglio renderle un '
          'servizio!',
    8709: 'Ti prego! Ti prego...!',
    8717: '...! Grazie infinite... Allora ti porto subito da lei!',

    # --- l'arrivo al castello
    8729: 'La principessa è nella stanza in fondo. Mi raccomando, non farla '
          'arrabbiare. E poi la scala qui davanti è collegata alla superficie '
          'per magia: quando vorrai tornare, passa di là.',

    # --- il primo incontro sulla spiaggia: l'invito alla principessa
    8734: 'Oh, ecco chi va all\'avventura. Capiti proprio a proposito.',
    8738: 'La nostra principessa non può uscire dal castello e si annoia a '
          'morte tutti i giorni. Se ti va, vieni con me e raccontale un po\' '
          'del mondo di superficie.',
    8741: 'Se torno indietro così la principessa mi sgrida! Ti prego, prendilo '
          'come un modo di aiutare il prossimo... cioè, una tartaruga!',
    8745: 'Oh, che emozione. Quando è il momento, fammi un cenno.',

    # --- il traghetto per il castello
    8750: 'Ci vado',
    8751: 'Non ci vado',
    8752: 'Andiamo dalla principessa, allora?',
    8755: 'Ma dai...',
    8763: 'Allora ti ci porto io. Trattieni il respiro per un po\'.',
}
