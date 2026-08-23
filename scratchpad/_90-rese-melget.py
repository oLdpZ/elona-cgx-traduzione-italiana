# -*- coding: utf-8 -*-
"""90a - MELGET l'informatrice (`chat.hsp:12907`-`:13181`, 32 firme).

「情報屋『メルゲット』」, «<Melget> l'informatrice» (`db_creature.hsp:69199`):
il genere e' **scritto nel nome**, quindi i participi che parlano di lei si
accordano al femminile («mi ha bloccata», «sono scappata», «mi sono accorta»).
Nel giapponese lo dicono anche le desinenze 〜の / 〜わ / 〜のよ delle dodici
curiosita'.

Il blocco fa tre mestieri:
  - due battute nella Culla del Caos (`:12911`, `:12915`);
  - il **quiz** dell'1 e del 15 (le dieci domande le tirano fuori i
    `txtsetquizN` di `text.hsp`, che non sono in questo lotto);
  - il servizio a pagamento: dove stanno gli artefatti, e la curiosita' del
    mese — dodici, una per mese.

⭐ LE CURIOSITA' SONO UN INDICE DEL RESTO DEL GIOCO. Ognuna nomina qualcosa che
sta gia' altrove, quindi qui non si e' inventato quasi niente:
  - «Sigillo Eterno»          chat.hsp:16200 e altri 46 siti
  - «Lothria»                 chat.hsp:24497 — ed e' proprio la squadra
                              speciale di `:12915`
  - «la dea dei desideri»     command.hsp:4449
  - «Jure», «la dea della guarigione»   god.hsp:303
  - «il gufo spaziale»        db_creature.hsp:69392
  - «penna d'oca lucente»     db_item.hsp:139945
  - «<Gigante Castagna>»      db_creature.hsp:76097
  - «riccio»                  action.hsp:125 — 「うに」 gridato dagli alchimisti
  - «calzini»                 chat.hsp:12430, la missione dei calzini
  - «<Fron> l'organizzatrice di viaggi»  db_creature.hsp:71217
  - «una certa cacciatrice di draghi»    db_creature.hsp:77428 (<Spipha>)
  - «Zanan», «istituto»       chat.hsp:2116
  - «giorno sfortunato»       il rovescio di «Giorno fortunato», event.hsp:2764
  - «Tyris»                   chat.hsp:1622
  - «(10000 oro)»             chat.hsp:8825 — la forma di `(10000gp)` nei menu
  - «Arrivederci»             chat.hsp:22112, la voce di menu さようなら
  - «alchimista»              db_item.hsp:141724

⭐⭐ E LA CURIOSITA' DI NOVEMBRE E' L'ECO DEL LOTTO DI IERI. 「丘の民の集落長」
e' **Dain**, reso «l'anziano della collina» nella 89a
(`db_creature.hsp:74213`, `text.hsp:11455`): Melget lo accusa di spargere
notizie false per stroncare chi non gli va a genio, e chi ha giocato la 89a ha
appena sentito Dain fare esattamente quello con la nipote. La riga si scrive
rileggendo il dizionario, non inventandola (89a) — e qui l'eco attraversa due
personaggi invece che due scene.

LESSICO DECISO QUI (va in glossario):
  - 貴重品 / «valuable items» -> **oggetti preziosi**. Non e' una categoria con
    un nome fisso: i cinque siti del sorgente lo dicono ogni volta a modo suo, e
    `chara.hsp:4271` l'ha gia' reso «quel che hanno di prezioso». Si tiene la
    stessa parola.
  - 努力賞 / «Effort Award» -> **premio di consolazione**. Il giapponese e' un
    premio di incoraggiamento, e il 「一応、ね」 che segue lo svuota: in italiano
    la parola che porta gia' quella presa in giro e' «consolazione».

DEROGHE DICHIARATE
1. `:13075` e `:13079` - L'INGLESE BUTTA VIA IL RECORD. Il giapponese dice il
   punteggio **e** il primato precedente («il record era N punti, quindi... e'
   un record nuovo!»); l'inglese tiene solo il punteggio. E' un dato che il
   giocatore usa — e' un gioco a punti — e la variabile e' li' nella riga. Si
   segue il giapponese (57a).
2. `:12932` - 「なんてこったい。」 contro «Sorry!». Il giapponese e'
   un'esclamazione comica di sconforto **di lei**, non una scusa **del
   giocatore**; il sito le da' ragione, perche' e' la battuta che Melget dice
   quando il giocatore rifiuta il quiz. Si segue il giapponese.
3. `:12926` - 「キミなら」 non diventa «per uno come te»: accorderebbe al
   maschile il giocatore, che non ha genere (75a). Si dice «per te».
4. `:13093` e `:13096` - il giapponese scrive `(10000gp)`, e il progetto quel
   suffisso lo rende «(10000 oro)» da nove siti (`chat.hsp:8825` e fratelli).
   Non e' una scelta di questo lotto: e' la forma di casa.

PERIMETRO: 32 firme, zero occorrenze fuori dal blocco e zero in altri file.
Nessun contraccolpo.

MENU: due file, di 2 e di 3 voci — **sotto** la soglia delle dieci
(`SOGLIA_DUE_COLONNE`, 89a), quindi il tetto delle due colonne non morde. Vale
quello dei 58 caratteri di `*chat_select`, e la voce piu' lunga ne fa 47.

⚠️ Gli accenti si scrivono VERI: la degradazione per CP932 la fa `applica.py`
(README, §Accenti). ⚠️⚠️ E «dèi» **non si scrive**: la degradazione mette
l'apostrofo *dentro* la parola («de'i») e a schermo non si legge. `verifica` lo
ha bocciato al primo giro, e la riparazione e' cambiare parola, non togliere
l'accento: `:13152` chiude con «Che paura fa, un dio».

⭐ LA MISURA HA DIVISO SEI RIGHE LUNGHE IN DUE FAMIGLIE. `chat-lotto-misura` ne
segnalava sei piu' lunghe dell'inglese. Cinque erano **mie**, cioe' italiano
prolisso su un inglese di pari contenuto: quelle si accorciano, e accorciate
leggono meglio. Una — `:13075` — e' la **deroga 1**, dove l'inglese ha buttato
via il primato: li' il metro misura contro un inglese che ha perso testo
apposta, e si tiene (come `:15214` e `:15328` nel lotto di BYSYMLHA). La
domanda giusta davanti a una riga lunga non e' «accorcio?» ma «di chi e' la
riga in piu'?».
"""

RESE = {

    # --- la Culla del Caos
    12911: 'Beeene, e nel Sigillo Eterno che segreti ci saranno nascosti? '
           'Ehehe, che bello scoperchiare i segreti, vero!',
    12915: 'Toh. Mi chiedevo perché di quelli di Lothria non se ne incontrasse '
           'quasi nessuno: il grosso della squadra è ancora ai piani di sopra. '
           'Eh, pochi e buoni si va più leggeri! Con troppa gente appresso non '
           'si avanza come si vorrebbe, no?',

    # --- il quiz dell'1 e del 15
    12923: 'Devo aumentare il numero di domande... Ah, il prossimo quiz lo '
           'faccio il 1 e il 15 del mese prossimo. Al mestiere vero ci torno '
           'da domani.',
    12926: 'Iehiii! È il Quiz dell\'avventuriero a quattro risposte! Le regole '
           'sono semplici: dieci domande di fila, e devi rispondere giusto e in '
           'fretta! Il punteggio viene dal tempo che ci metti e dalle risposte '
           'giuste, ma il limite è di 60 secondi: passati quelli fai 0 punti '
           'anche se hai azzeccato tutto, quindi occhio! Ehm, per te... '
           'facciamo le domande sul continente di Tyris?',
    12927: 'Lascio perdere',
    12928: 'OK!',
    12929: 'Allora, tutto pronto? Il testo della domanda te lo metto giù in '
           'basso!',
    12932: 'Ma dai, che peccato.',
    12937: 'Via!',
    13070: '"Bel lavoro! Tempo impiegato: " + endsec + " secondi, risposte '
           'giuste: " + seikai + "."',
    13075: '"Il punteggio finale è " + gdata(GDATA_FLAG_MELGET_SCORE) + '
           '" punti! Il primato di prima era " + '
           'gdata(GDATA_FLAG_MELGET_HISCORE) + " punti, quindi... è un record '
           'nuovo! Complimenti!"',
    13079: '"Il punteggio finale è " + gdata(GDATA_FLAG_MELGET_SCORE) + '
           '" punti! ...Mah, il primato di " + '
           'gdata(GDATA_FLAG_MELGET_HISCORE) + " punti non l\'hai battuto. '
           'Riprova, eh."',
    13082: 'Hai superato i 200 punti, quindi un premio di consolazione te lo do. '
           'Di consolazione, eh.',

    # --- il servizio a pagamento
    13091: 'Arrivederci',
    13093: 'Che cos\'hanno gli altri avventurieri (10000 oro)',
    13096: 'La curiosità del mese (500 oro)',
    13098: 'Ah, ho un prurito addosso dalla voglia di raccontare un sacco di '
           'cose! Che faccio? Che cosa ti insegno?',
    13101: 'Mah... dirti tutto sarebbe noioso: degli artefatti unici e degli '
           'oggetti preziosi che hanno addosso gli altri avventurieri te ne '
           'dico \\"al massimo uno\\" per ciascuno. Carta e penna? Lo dico una '
           'volta sola.',
    13130: 'cdatan(CDATAN_AKA, rc) + " " + cdatan(CDATAN_NAME, rc) + '
           '" non ha niente di prezioso."',
    13133: 'cdatan(CDATAN_AKA, rc) + " " + cdatan(CDATAN_NAME, rc) + " ha " + '
           'valn + "."',

    # --- le dodici curiosità, una per mese
    13143: 'A me la cioccolata non piace. Così ho chiesto che San Valentino '
           'venisse abolito, e la dea dei desideri mi ha mandato dei '
           'cioccolatini fatti a mano. Buttarli era un peccato e me li sono '
           'mangiati per forza... Anche lei ne ha di grane...',
    13146: 'Gli attacchi di una certa cacciatrice di draghi fanno un 10% di '
           'danno in più sui draghi. Non che gli attacchi di drago siano '
           'superefficaci sui draghi: è che ci mette dentro tutta la voglia di '
           'ammazzarli.',
    13149: 'Guardando la lista dei reclusi dell\'istituto sperimentale di Zanan '
           'mi sono accorta di una cosa: se leggi i nomi di tutti uno dietro '
           'l\'altro, viene fuori una frase. Non ti pare una coincidenza '
           'pazzesca?',
    13152: 'Chissà quanto è fissato per Jure il dio del tempio centrale. Ho '
           'provato a molestare un po\' la dea della guarigione proprio davanti '
           'a lui, e mi ha bloccata ogni volta. Se ne accorge e ti ferma '
           'perfino da dietro un muro, capisci? Che paura fa, un dio.',
    13155: 'Fra gli angeli c\'è chi porta addosso una penna d\'oca lucente, ma '
           'gli angeli che stanno di stanza in certe città o in certi edifici '
           'la penna non ce l\'hanno mai.',
    13158: 'Volevo la sua carta, così ho attaccato briga con la dea che stava '
           'nella torre del deserto, e in mezzo alla battaglia mi è arrivato un '
           'giorno sfortunato. Sono scappata di corsa, ma per un bel po\' dopo '
           'è stata dura.',
    13161: 'Il gufo spaziale, se lo accarezzi, si esalta in un modo quasi '
           'disgustoso. E più siete in confidenza, più diventa violento...',
    13164: 'Il gigante che compare davanti a chi spreca le castagne, se gli tiri '
           'una castagna pare che si faccia molto male. L\'ho provato anch\'io: '
           'si lamentava da matti.',
    13167: 'Quelli che si dicono alchimisti, quando tirano una castagna, '
           'insistono sempre che è un \\"riccio\\". Poi, detto questo, non è che '
           'cambi granché.',
    13170: 'Un tale che passa il tempo a fantasticare sull\'universo, di '
           'nascosto, raccoglie calzini di chiunque: uomini e donne, giovani e '
           'vecchi. Già che c\'ero mi sono fatta cambiare dei calzini con '
           'degli oggetti.',
    13173: 'L\'anziano della collina va in giro a dire cose vere e cose false '
           'per stroncare socialmente chi non gli va a genio. Mettere in giro '
           'informazioni sbagliate apposta, e senza nemmeno la scusa del pesce '
           'd\'aprile: da informatrice non posso lasciar correre...!',
    13176: 'L\'altro giorno ho visto qui in giro l\'organizzatrice di viaggi, ma '
           'dopo pochi giorni è ripartita. Pare che stia sempre in movimento a '
           'preparare il viaggio dopo, quindi con un po\' di fortuna la '
           'incontri anche tu.',
}
