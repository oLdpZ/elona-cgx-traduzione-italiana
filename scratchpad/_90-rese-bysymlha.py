# -*- coding: utf-8 -*-
"""90a - BYSYMLHA occhi d'ambra (`chat.hsp:15200`-`:15330`, 38 firme).

「琥珀眼の悪魔『バイシルフ』」, «<Bysymlha> il demone dagli occhi d'ambra»
(`db_creature.hsp:50617`). Non e' un personaggio di trama: e' il **pannello
delle difficolta'** travestito da tentatrice. Da lei si cambiano tre numeri —
il moltiplicatore di esperienza di Overdose, le vite in piu' di Purge, e
l'esperienza minima garantita — e ogni scelta ha la sua battuta, che invita
sempre a sceglierne una piu' alta.

Registro: です/ます mielosi, allungamenti, `♪` e 「うふふふふ」. In italiano il
**tu**, come tutto il progetto anche per i parlanti formali
(`chat.hsp:1599`, giapponese pieno di cortesie e italiano che da' del tu): a
portare la cortesia e' il lessico, non l'allocuzione.
⚠️ E il **tu evita anche il genere**: col «lei» ogni participio riferito al
giocatore avrebbe chiesto un accordo che il giocatore non ha (75a).

LESSICO EREDITATO — quasi tutto, e quasi tutto dalla stessa pagina:
`chara.hsp:4225`-`:4314` e' la **descrizione delle modalita'**, cioe' il testo
che spiega proprio questo menu. Di li' vengono:
  - «3x», «30x»              chara.hsp:4231 — la forma del moltiplicatore, ed
                             e' letteralmente questo menu: «Di base e' 3x, e in
                             un certo posto si arriva fino a 30x». Quel «certo
                             posto» e' lei.
  - «Overdose», «Purge»      chara.hsp:4177 e :4180, invariati
  - «esperienza»             chara.hsp:4228
  - «il potenziale»          chara.hsp:4311, ai.hsp:1893, chat.hsp:416
  - «gli attributi»          buff.hsp:1096, chara.hsp:3999
  - «il demone»              db_creature.hsp:50617 e altri 53 siti
  - «l'universo»             chat.hsp:6601
  - «(predefinito)»          text.hsp:1643, «Nessun limite (predefinito)»
  - la virgola decimale      buff.hsp:707, «Lancio x1,5»

LESSICO DECISO QUI (va in glossario):
  - 残機 / «remaining lives» -> **vite in piu'**. Non c'era: 残機 non compare in
    nessun dizionario. «Vite extra» e' il calco da sala giochi; il progetto
    scrive gia' «Punti bonus in piu'» per la stessa idea (`chara.hsp:4305`), e
    la forma con «in piu'» e' quella di casa.

DEROGHE DICHIARATE
1. `:15328` - L'INGLESE TAGLIA LA BATTUTA. Il giapponese chiude con
   「頭ではわかっていても…私の身体がわかってくれないのです」 — *la testa lo
   capisce, il mio corpo no* — e l'inglese la butta via, lasciando solo la
   morale. Quella coda **e' il personaggio**: e' la riga che si legge se non si
   sceglie niente, e dice che la tentatrice e' la prima a non resistere. Si
   segue il giapponese (57a).
2. `:15223` - L'INGLESE RISCRIVE LA CHIUSA. Giapponese:
   「どうせ、遅かれ早かれ最終的には最大倍率を選ぶのですから」 — *tanto prima o
   poi il massimo lo scegli comunque*. L'inglese ci mette un generico «tell me
   what you desire». La frase giapponese e' la stessa tesi di tutte le altre
   battute del blocco, quindi qui l'inglese non regge il blocco: si segue il
   giapponese.
3. `:15313` - Stessa forma. Giapponese:
   「どこまでがセーフかなんて、気持ち次第じゃありませんか？」 — *fin dove sia
   "sicuro" dipende da come ti senti*, che risponde al 「セーフ」 fra
   virgolette di `:15242`. L'inglese perde il rimando e mette una domanda
   qualunque.
4. `:15253` - 「残機0にする（デフォルト）」 contro «I do not need it.». Gli altri
   quattro della stessa fila l'inglese li rende alla lettera («Get 3 remaining
   lives.»): qui cambia forma solo per il valore predefinito. Si tiene la fila
   **uniforme**, che e' quello che una fila di menu deve essere (49a), e con
   essa il «(predefinito)» che l'inglese lascia cadere in tutt'e tre le file
   pur avendolo il giapponese. Il giocatore quel dato lo usa.
5. `:15247` e `:15323` - LO STESSO GIAPPONESE IN DUE INGLESI DIVERSI, quindi
   due firme. Ma qui — al contrario di `:12394`/`:12473` della 89a — il **sito
   e' lo stesso mestiere**: e' la battuta dell'opzione piu' alta, una volta per
   il moltiplicatore e una per l'esperienza minima. Due firme, **una sola
   resa**: se differissero, `battute --divergenti` avrebbe ragione a segnalarle.
6. `:15318` - 「ダ・メ♪」 spezza la parola con il 「・」, che e' a doppia
   larghezza e non si scrive (guardia dei proibiti). Si spezza con i trattini,
   che fanno lo stesso mestiere: «Non de-vi a-ver pa-u-ra♪».

PERIMETRO: 38 firme, zero occorrenze fuori dal blocco e zero in altri file.
Nessun contraccolpo.

MENU: quattro file, di 2-5, 5, 5 e 6 voci. Tutte **sotto** la soglia delle
dieci (`SOGLIA_DUE_COLONNE`, 89a): il tetto delle due colonne non morde, vale
solo quello dei 58 caratteri di `*chat_select`.

⚠️ Gli accenti si scrivono VERI («così», «più», «sì»): la degradazione ad
apostrofo per CP932 la fa `applica.py`, e `verifica.py` boccia la forma con
l'apostrofo scritta a mano (README, §Accenti).

⭐⭐ LE DUE «PEGGIORATE» SI TENGONO, ED E' MISURATO PERCHE'.
`chat-lotto-misura` segnala `:15214` (4 righe contro 2) e `:15328` (4 contro
3). Sono **esattamente** le due righe delle deroghe 1 e 2, cioe' le due dove
l'inglese butta via un pezzo di giapponese: il metro «l'italiano non faccia
piu' righe dell'inglese» (73a) misura contro un inglese che ha perso testo
apposta, e accorciare vorrebbe dire ributtarlo via.
E il tetto non morde: un `chatMore` da un bottone ne tiene **13**
((324 - 19 - 43) // 19), l'italiano ne fa 4. La regola della 89a — *prima di
accorciare una resa si guarda se il tetto puo' mordere* — vale anche al
contrario: dove non morde, la riga lunga non e' un difetto da riparare.
"""

RESE = {

    # --- il menu di partenza
    15202: 'Va bene così com\'è',
    15203: 'Vorrei una vita più facile...',
    15205: 'Voglio cambiare il moltiplicatore di esperienza',
    15208: 'Voglio cambiare le vite in più',
    15209: 'Voglio cambiare l\'esperienza minima',
    15211: 'Questo universo trabocca di sofferenza. Perché non sprofondi '
           'insieme a me... verso qualcosa anche solo un pochino più facile?',
    15214: 'Uffufu...♪ In questo universo non potrai più tornare, ma non ti '
           'dispiace, vero? Su, chiudi piano gli occhi, una volta sola. ...E '
           'poi riaprili, e guarda dentro le mie pupille.',

    # --- il moltiplicatore di esperienza (Overdose)
    15218: 'Portarlo a 3x (predefinito)',
    15219: 'Portarlo a 5x',
    15220: 'Portarlo a 10x',
    15221: 'Portarlo a 20x',
    15222: 'Portarlo a 30x',
    15223: 'Ahaa♪ Lo so, sì, lo so benissimo. Non ti basta, vero? Su, non c\'è '
           'nessun bisogno di esitare sul moltiplicatore: prima o poi finirai '
           'per scegliere il massimo comunque.',
    15227: 'Mmh...? Ma ti bastaaa davvero?',
    15232: 'Stai tirando il freno alla tua voglia, eh. Che tenerezzaaa♪',
    15237: 'Le cose a metà sono quel che fa peggio al corpo... Non vuoi '
           'ripensarci...?',
    15242: '\\"Una volta era così, quindi va bene\\", eh? Ma adesso c\'è anche '
           'di più, sai?',
    15247: 'Va benissimo... Impazziamo insieme per il piacere che ti sei scelto '
           'da te♪',

    # --- le vite in più (Purge)
    15253: 'Nessuna vita in più (predefinito)',
    15254: '3 vite in più',
    15255: '9 vite in più',
    15256: '20 vite in più',
    15257: '99 vite in più',
    15258: 'Su, quante ne vuoi... Se non me lo dici io non posso saperlo, no? E '
           'quando non ti bastano più, te ne rifornisco quante ne vuoi...',
    15262: 'Ohi ohi. Tirare fuori l\'orgoglio adesso non serve a niente, non '
           'trovi?',
    15277: 'Così poche non ti mettono in ansia? Non vuoi aumentarle ancora un '
           'po\'...?',
    15282: 'Perfino un demone resterebbe di sasso, sai? Che ingordigia... che '
           'ingordigiaaa♪',

    # --- l'esperienza minima garantita
    15288: 'Esperienza minima garantita 0,001 (predefinito)',
    15289: 'Esperienza minima garantita 0,01',
    15290: 'Esperienza minima garantita 0,1',
    15291: 'Esperienza minima garantita 1',
    15292: 'Esperienza minima garantita 10',
    15293: 'Esperienza minima garantita 100',
    15294: 'Su, prego? Ah, e con l\'esperienza minima a 1, ogni volta che entra '
           'dell\'esperienza quell\'attributo sale almeno di un livello. Il '
           'potenziale non conta più niente, quindi puoi alzare gli attributi '
           'quanto ti pare. Uffufufufu! Che bella cosa, eh.',
    15313: 'Salire di uno alla volta sarebbe \\"sicuro\\"? Ma fin dove sia sicuro '
           'dipende da come ti senti, non credi?',
    15318: 'Non de-vi a-ver pa-u-ra♪ Cambia solo quanto tempo ci metti: tanto '
           'il posto dove arrivi è lo stesso, no?',
    15323: 'Va benissimo... Impazziamo insieme per il piacere che ti sei scelto '
           'da te♪',

    # --- se non si sceglie niente
    15328: 'Una giusta dose di fatica è quel che fa crescere le persone... e ci '
           'sono gioie che non si ottengono se non la si supera... Sì, lo so '
           'bene. Ma anche se la testa lo capisce... il mio corpo non vuole '
           'capirlo.',
}
