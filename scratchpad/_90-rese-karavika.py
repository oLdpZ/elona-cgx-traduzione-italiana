# -*- coding: utf-8 -*-
"""90a - KARAVIKA la cantante (`chat.hsp:12064`-`:12331`, 41 firme).

L'idol di Ol-dran: 《歌踊のカラヴィカ》, «<Karavika> del canto e della danza»
(`text.hsp:11347`). Tiene un concerto a fine mese e assolda il giocatore per la
sicurezza della sala. Il blocco ha tre scene: la missione, il menu delle
chiacchiere con la stretta di mano, e la scena degli stalker.

Il registro sta gia' scritto nel suo repertorio (`db_creature.hsp:72012`-
`:72036`): bambinesca, entusiasta, vocali allungate — «Ciao a tuttiii...»,
«Iuppiii!», «Mi sto caricandooo!», «Grazie del tifo...», «E mi raccomando, le
mance!». Dice あたし, da' del tu a tutti, e il `♪` si scrive (89a).

LESSICO EREDITATO (non deciso qui):
  - «<Karavika>»              db_creature.hsp:72050, sempre fra angolari
  - «il concerto»             text.hsp:11358, map.hsp:599, il diario della missione
  - «la sicurezza»            text.hsp:11368, il diario: «le manca sempre
                              qualcuno per la sicurezza»
  - «stalker»                 map.hsp:15212, il nome della creatura di questa
                              stessa missione
  - «il cavaliere dorato»     db_creature.hsp:122898
  - «Yacatect», «la dea del Tesoro»  god.hsp:89, chat.hsp:13658 («del Tesoro»
                              e' l'epiteto fisso di 富の)
  - «maniaco»                 db_creature.hsp:68205, 変質者 -> «Al maniaco!»
  - «offerta», «potere divino»   chat.hsp:13971 e adv.hsp:69
  - «Rifiuto»                 chat.hsp:2351, la voce di menu 断る
  - «Accetto»                 chat.hsp:3657 e :7370, la voce di menu 引き受ける
  - «Stretta di mano con Karavika»  text.hsp:2136, il premio da 100 YacaPoint
  - «<...>»                   la forma delle voci di menu 【...】 (chat.hsp:835,
                              :4867, :16200 e altre otto)

LESSICO DECISO QUI (va in glossario):
  - 限定コンサート / «limited-time concert» -> **il concerto esclusivo**. Il
    diario lo chiama solo «un concerto a fine mese» (`text.hsp:11368`), quindi
    la parola per 限定 mancava. «A tempo limitato» e' burocratico; «esclusivo»
    e' come un'idol vende una data sola, ed e' quel che 限定 fa qui.
  - ヤカ姐 / «big sis Yacatect» -> **sorellona Yacatect**. 姐 e' la sorella
    maggiore di strada, non di sangue: Karavika la imita e la cita due volte
    (`:12262`, `:12282`). Il nome per esteso perche' a `:12282` non c'e' nessun
    contesto che lo disambigui, e l'inglese fa la stessa scelta.

ECO — tre, e tutte gia' scritte altrove:
  1. `:12153` 「テンション上がってきた」 e' **parola per parola** la battuta del
     suo repertorio a `db_creature.hsp:72018`, resa «Mi sto caricandooo!». La
     coda 「愛してるぜベイベー！」 e' la stessa frase di `screen.hsp:1486`
     (「イェーイ！愛してるぜベイベー！」), resa «Ti amo, bella!». La riga si
     scrive rileggendo il dizionario, non inventandola (89a).
  2. `:12256` 応援 -> «tifo», come `db_creature.hsp:72036` («Grazie del
     tifo...»).
  3. `:12249` おひねり -> «le mance», come `db_creature.hsp:72012` — ma qui
     l'inglese la mette e il giapponese no: vedi la deroga 3.

DEROGHE DICHIARATE
1. `:12323` - L'INGLESE SCAMBIA CHI HA PAURA. Il giapponese dice
   「(騎士に引きずられていくあなたを見ながら、怯えている…)」: il soggetto di
   怯えている e' **lei**, e あなた e' l'oggetto di 見ながら — Karavika guarda il
   giocatore trascinato via ed e' terrorizzata. L'inglese fa paralizzare dalla
   paura **il giocatore**. Il sito da' ragione al giapponese: e' un `chatMore`,
   cioe' una riga sotto il ritratto di chi parla. Si segue il giapponese (57a).
2. `:12314` - 「変質者め、おとなしくしろ」. La parola c'e' gia'
   (`db_creature.hsp:68205`, «Al maniaco!») ma «maniaco» accorderebbe al
   maschile il **giocatore**, che non ha genere (75a). Si tiene la parola e si
   sposta il bersaglio: il cavaliere la grida ai suoi («Al maniaco!») e al
   giocatore da' l'ordine, che e' senza genere. L'effetto a schermo e' lo
   stesso e il termine ereditato non si perde.
3. `:12249` - L'INGLESE AGGIUNGE. Il giapponese e'
   「…月末の限定コンサートもよろしくっ！」 e basta; l'inglese ci mette
   «...and all donations are welcome!», che e' おひねり — una battuta che lei ha
   davvero, ma nel **repertorio** (`db_creature.hsp:72012`), non qui. Non si
   rimette: il criterio non e' rendere il testo piu' ricco (89a, deroga 7).
4. `:12275` - ベイベー AL GIOCATORE. A `:12153` lo grida dal palco al pubblico e
   la resa e' l'eco di `screen.hsp:1486` («Ti amo, bella!»); qui lo dice **al
   giocatore**, e «bella» gli darebbe un genere. Si usa «beibi», che e' la
   traslitterazione con cui il progetto rende gia' ベイベー in
   `db_creature.hsp:89694` e `:104390` («Camon beibi!»). Due siti, due rese, e
   la differenza la detta chi ascolta (89a, deroga 3).
5. `:12275` - `cnvrank` E' MORFOLOGIA INGLESE (85a): la desinenza ordinale non
   si traduce, e l'argomento si concatena nudo. Qui si evita anche l'ordinale
   italiano, che vorrebbe la 'ª' — un carattere che CP932 non porta: si conta
   in avanti («Con questa fanno N strette di mano»), che dice la stessa cosa.
6. `:12297` - ス、ストーカー？. Il giapponese non dice «sei»: e' un'esclamazione,
   non una predicazione sul giocatore, e resta tale anche in italiano. Cosi' la
   parola ereditata («stalker») entra senza portare un genere.

PERIMETRO: 41 firme, zero occorrenze fuori dal blocco e zero in altri file
(`_85-blocco.py` e la ricerca per firma su tutti i `dizionario/*.jsonl`).
Nessun contraccolpo.

MENU: quattro, di 2, 3-4, 2 e 2 voci. Tutti **sotto** la soglia delle dieci
(`SOGLIA_DUE_COLONNE`, 89a), quindi il tetto delle due colonne non morde: vale
solo quello dei 58 caratteri di `*chat_select`.
"""

RESE = {

    # --- la missione compiuta: il compenso
    12070: 'Il concerto esclusivo è stato un successone♪ Ed è tutto merito tuo, '
           'che me l\'hai difeso! Tieni, questo è il mio ringraziamento!',

    # --- l'incarico: la sicurezza della sala
    12115: 'Rifiuto',
    12116: 'Accetto',
    12118: 'Ehi, tu, tu! Sì, dico a te! Per il concerto esclusivo di fine mese '
           'non ho nessuno da mettere alla sicurezza dentro la sala. Ti pago, '
           'eh: non è che me lo fai tu? È una cosa urgente sul serio!',
    12121: 'Ah, arrivi al momento giusto! Vorrei affidare di nuovo a te la '
           'sicurezza della sala: va bene?',
    12130: 'Evviva! Allora è deciso: corriamo subito alla sala!',
    12131: 'Appena arriviamo si comincia! Se il mio spettacolo si interrompe o '
           'muore qualcuno del pubblico, è un disastro. Credo che gli stalker '
           'sfonderanno la sicurezza di fuori e proveranno a entrare in sala: '
           'mi raccomando, difendi il concerto fino in fondo.',
    12144: 'Mmh. Mi dispiace per i fan, ma se non riesco a garantire la '
           'sicurezza tocca annullare...',

    # --- il concerto comincia
    12149: 'Scusate l\'attesaaa! Forza, anche oggi si canta, si balla e si '
           'suonaaa!',
    12153: 'Bene! Mi sto caricandooo!!! Ti amo, bella!',
    12160: 'Difendiamo il concerto esclusivo fino in fondo!',

    # --- il menu delle chiacchiere
    12239: 'Scusami',
    12240: 'Mi fai un autografo?',
    12241: 'Esci con me',
    12243: '<Usare la stretta di mano>',
    12245: 'Ehm... vorrei restare concentrata, quindi non parlarmi troppo, va '
           'bene?',
    12248: 'Basta che tu capisca. E goditi il mio concerto!',
    12249: '...E mi raccomando, vieni anche al concerto esclusivo di fine mese!',

    # --- la stretta di mano, una battuta per ogni volta
    12253: 'La stretta di mano? Aspetta un attimo...',
    12254: 'Ecco, tutto a posto! Su, dammi la mano!',
    12256: 'Mmh, con chi non conosco la stretta di mano mi mette un po\' '
           'd\'ansia. ...Continua a fare il tifo per me!',
    12259: 'Un\'altra stretta di mano? Ehehe. Sai, la faccia dei fan a cui l\'ho '
           'stretta me la ricordo tutta.',
    12262: 'Grazie della preferenza! ...Ehehe, ho fatto il verso a sorellona '
           'Yacatect. Nessuno ti obbliga a credere, ma un pensiero anche alla '
           'dea del Tesoro, mi raccomando!',
    12265: 'Bene, oggi ci do dentro più del solito. Goditi il mio canto, il mio '
           'ballo e la mia musica!',
    12268: 'A pensare che c\'è gente che mi fa il tifo fin qui, un po\' mi '
           'commuovo. Sì... sono contenta e basta!',
    12271: 'A te la stretta di mano piace proprio, eh. ...Anche a me, però! È '
           'come se mi ricaricasse. Chissà se ricevere il potere divino da '
           'un\'offerta è una cosa così.',
    12275: '"Con questa fanno " + p + " strette di mano, no? Anche oggi ci '
           'scateniamo, beibi!"',

    # --- l'autografo
    12282: 'Ah... L\'autografo neanche sorellona Yacatect me l\'ha insegnato...',
    12283: 'Faccio pratica e poi la prossima volta, eh?',

    # --- la proposta, e l'insistenza
    12288: 'Esci con me!',
    12289: 'Q-quello no, guarda. Devi passare dall\'agenzia...',
    12293: 'Escii con meee!!',
    12294: 'Scusa. Certe cose mi mettono in imbarazzo. E poi ho ancora dei pezzi '
           'da fare...',

    # --- i cavalieri dorati
    12297: 'Hii...!? U-uno stalker?',
    12298: 'Guardie! Guardie!',
    12306: 'I cavalieri dorati arrivano di corsa.',
    12310: 'Che ti salta in mente!',
    12314: 'Al maniaco! Non fare storie.',
    12318: 'E ti presenti pure qui come niente fosse!',
    12322: 'Arrenditi!',
    12323: '(Ti guarda mentre i cavalieri ti trascinano via, ed è '
           'terrorizzata...)',
}
