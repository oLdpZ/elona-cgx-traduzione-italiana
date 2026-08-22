# -*- coding: utf-8 -*-
"""Le rese della TESTA di `*chat_unique` (chat.hsp :951-:1586), otto blocchi.

Perimetro: 52 firme, **zona chiusa** — nessuna ha occorrenze fuori, quindi
`bilingui` deve dare zero al primo giro.

    :1215  il `vanq` degli eventi (dentro CREATURE_ID_USER)
    :1236  ZEOME il falso profeta
    :1249  ORPHE il figlio del caos, davanti al piedistallo del libro
    :1261  CHI STRISCIA NEL VUOTO
    :1277  LOYTER il sangue cremisi di Dole, i cinque monologhi
    :1336  LOYTER l'eroe cremisi di Zanan, l'incarico dell'incubo
    :1475  MICHES l'apprendista: le carte e i putit che mangiano i peluche
    :1542  SHENA l'attrazione del locale: i barili rubati

Registri, uno per parlante:
  ZEOME    mago antico e sprezzante, da' del voi al gruppo (お前達)
  ORPHE    giovane altero e filosofeggiante, parla al LIBRO prima che a te
  LOYTER/Dole  eroe finito, monologhi amari rivolti a un morto
  LOYTER/Zanan duro, militare, sprezzante (貴様); non e' mai gentile
  MICHES   ragazza allegra, ♪, «あら…わ»
  SHENA    cameriera cortese, ♪, forma di cortesia

Lessico ereditato: «<occhio delle tenebre eterne>» (`chat.hsp:2316`), «Sierre
Terre», «Rehm-Ido», «Eyth Terre», «il lume della memoria» (`chat.hsp:1268`,
`:9471`), «<Loyter> il sangue cremisi di Dole» e «l'eroe cremisi di Zanan»
(`db_card.hsp`), «<Bethel> il falco bianco», «Chi striscia nel vuoto»,
«il diario del ricercatore» (`db_item.hsp:138165`), «putit» e «melma»
(glossario), «peluche» (`command.hsp:10029`).

⚠️ 冒険者さん rivolto al giocatore e' **«tu che vai all'avventura»**, la forma
senza genere gia' in uso a `:1469` e `:1595`. E l'epiteto
`cdatan(CDATAN_AKA, ...)` resta un sintagma nudo, senza articolo.

⚠️ `:1249` monte usa `_sex(cdata(CDATA_SEX, CHARA_PLAYER))` nel solo ramo
GIAPPONESE: l'inglese dice «this one» e non chiama nessuna funzione. Si segue
l'inglese, quindi la funzione cade — `verifica` lo permette perche' sottrae
l'unione dei due rami.
"""

RESE = {}

# --- il `vanq` degli eventi
# ⚠️ `_s(tc)` e' morfologia inglese e cade; il presente evita l'accordo con un
# personaggio di cui non si sa il sesso.
RESE[1215] = 'name(tc) + " svanisce nel nulla."'

# --- ZEOME il falso profeta
RESE[1236] = ("Grazie... di questa terra e dei suoi dei nemmeno l'occhio delle tenebre eterne "
              "sapeva. Vedremo se fermerete il <Caos>. E lui? Perché non è qui?")
# ⚠️ deroga: «it seems they have left me no choice but to whip you!» e'
# un'invenzione dell'inglese. Il giapponese dice しかし、私とてここで死ぬつもり
# などないのだ — «ma non ho nessuna intenzione di morire qui».
RESE[1240] = ("Dunque ce l'hai fatta fin qui... Si vede che il <Caos> non vuole stabilità nemmeno "
              "dentro Nefia, che pure è opera sua. Ma io non ho nessuna intenzione di morire qui.")

# --- ORPHE il figlio del caos
RESE[1249] = ("Ah, sapiente <occhio delle tenebre eterne>! Pare che chi ti ha adesso non conosca il "
              "tuo valore... Ma non temere. Il vecchio che giace lì ti apriva ogni tanto per ridere "
              "delle menzogne del mondo di sotto; chi ti tiene ora saprà trovarti un uso migliore.")
RESE[1250] = ("(Il giovane ride con aria di scherno e si volta verso di te.) Su, non deludermi "
              "tenendo ancora quell'aria di sciocca curiosità. Il libro che stai guardando conserva "
              "la storia vera di questo mondo, incisa dalla magia di una civiltà antica.")
RESE[1251] = ("Sì: quel che è scritto in questo libro è storia senza menzogne. Vi sono segnate la "
              "gloria e la caduta di Sierre Terre, di Rehm-Ido, di Eyth Terre e di tutte le grandi "
              "civiltà del passato. Non credo di doverti spiegare quanto valga.")
RESE[1252] = ("Un avvertimento: staccato dal piedistallo perde il suo potere e diventa un libro "
              "qualunque. Nessuna storia nuova vi si scriverà, e non ci sarà più modo di provarne "
              "l'autenticità.")
RESE[1253] = ("E chi possiede questo libro dovrà anche difendere la propria vita da chi ha interesse "
              "a falsificare la storia: tanto vale questo manufatto. E tu... tu che hai incontrato "
              "l'elea che ascolta il vento e le hai parlato... anche senza capire quanto significhi... "
              "sì, almeno mi divertirai.")
RESE[1254] = ("Naturalmente, portare il libro giù nel mondo di sotto sta a te deciderlo... ammesso "
              "che tu creda che in una scelta ci sia un caso che io non abbia già previsto.")

# --- CHI STRISCIA NEL VUOTO
RESE[1261] = "Vattene altrove..."

# --- LOYTER il sangue cremisi di Dole
RESE[1277] = "Dal lume della memoria si spande una luce calda..."
# ⚠️ deroga: l'inglese rovescia la frase. «you should be hanged, or worse»
# traduce せめて貴様が首を吊らなければな, che dice il contrario — Yuri si e'
# impiccato, e Loyter rimpiange che l'abbia fatto.
RESE[1305] = ("Yuri... se solo non ti fossi impiccato. Temevi che le bestie ti divorassero e ti "
              "facessero dimenticare Alicia, immagino... Zaletta è ancora là, in pena per te...!")
RESE[1308] = ("Va bene così: di Dole non ho ancora dimenticato tutto. Vuol dire che il paese in "
              "qualche modo regge.")
RESE[1311] = ("Se doveva finire così, avrei fatto meglio a parlare con Zaletta prima di partire da "
              "Dole. ...Già. Un rimpianto ce l'avevo ancora. Roba da femminucce.")
RESE[1314] = ("A pensarci adesso, il principe Ozmu voleva farsi di Elsia un nemico comune. Forse "
              "tramava qualcosa d'accordo con Rufus dai capelli azzurri. Ma ormai non ha più nessuna "
              "importanza...")
RESE[1317] = ("Chi l'avrebbe detto: in un paese di campagna come questo il falco bianco è morto e al "
              "sangue cremisi non resta che aspettare la fine. Ehi, Yuri... dove si sono inceppati i "
              "nostri ingranaggi?")
RESE[1319] = "...Che vuoi? Non fissarmi. Sparisci."

# --- LOYTER l'eroe cremisi di Zanan
RESE[1336] = "Dal lume della memoria si spande una luce calda..."
RESE[1364] = "Sei d'intralcio. Non rivolgermi la parola."
RESE[1370] = "Non prenderti confidenze."
RESE[1378] = "...Sta' lontano. Sei una piattola."
RESE[1383] = "Vuoi che legga questo? ...Va bene, ma appena finito sparisci."
RESE[1386] = "Questo è..."
# ⚠️ deroga: l'inglese taglia la seconda meta' — il risarcimento alle famiglie
# e il passaggio degli altri centri sotto controllo. E' quel che chiude la
# missione, e il giapponese ce l'ha.
# ⚠️ E la deroga si paga in righe: sei contro quattro. La regola prudente
# della 73a — l'italiano non faccia piu' righe dell'inglese — qui non puo'
# valere, perche' l'inglese ha meta' del contenuto. Dentro il tetto ci sta.
RESE[1390] = ("La faccenda è già chiusa. Il personale è morto tutto dentro l'impianto, e l'unico "
              "scappato, il direttore, è già stato \\\"smaltito\\\". Alle famiglie dei soggetti e del "
              "ricercatore l'esercito ha pagato un risarcimento, e gli altri centri sono passati "
              "sotto controllo come si deve.")
RESE[1391] = "Ho detto tutto. Non c'è spazio per te in questa storia. Se hai capito, sparisci."
RESE[1400] = ('"Ehi, tu. Fermati un attimo. Quella faccia l\'ho già vista... " + '
              'cdatan(CDATAN_AKA, CHARA_PLAYER) + "... ma certo. Dicono che ultimamente qui a '
              'Tyris ti stai facendo un nome."')
RESE[1401] = "Sentiamo"
RESE[1402] = "Lascio perdere"
RESE[1403] = ("Ti do da guadagnare. Un certo ente di Zanan ha bisogno di una cavia per raccogliere i "
              "dati di un esperimento. Anzi, più che cavia: \\\"vittima sacrificale\\\". Se "
              "sopravvivi e torni, il compenso ti basterà a spassartela fino alla vecchiaia. Decidi "
              "adesso.")
RESE[1406] = "Non hai fegato. Sparisci."
RESE[1410] = ("Bene. Quando avrai finito di prepararti a morire fammi un cenno: ti accompagno al "
              "campo di prova.")
# ⚠️ :1415 「いい」/«Yes.» e :1416 「だめ」/«No.» NON stanno nel lotto: sono
# firme gia' rese altrove, e il menu e' gia' italiano.
# ⚠️ deroga: l'inglese tiene solo la domanda finale. Il giapponese comincia con
# フッ。よく逃げ出さずに戻ってきたな — ed e' la sola battuta in cui Loyter
# riconosce che il giocatore non e' scappato.
RESE[1417] = "Ah. Non te la sei data a gambe, dunque. Tutto pronto?"
RESE[1420] = "Sbrigati."
RESE[1429] = "Bene... seguimi."
RESE[1454] = ("Sono sorpreso. Sei la prima persona che va all'avventura a tornare viva da questo "
              "esperimento. Speriamo che adesso ai piani alti di Zanan rivedano quella ricerca. "
              "Girare per i campi di battaglia alla testa di mostri così sgraziati, io non ci penso "
              "proprio.")

# --- MICHES l'apprendista
RESE[1475] = ("Benissimo! Non ci hai mai giocato, vero? Mi è capitato di comprare un set di carte in "
              "più: tieni, è tuo. Metti insieme un mazzo da 30 carte e sfidiamoci!")
RESE[1498] = "Oh, tu che vai all'avventura♪ Ti va un tè?"
RESE[1502] = "Oh, tu che vai all'avventura. Capiti proprio a proposito."
RESE[1505] = ("Da un po', la mattina mi sveglio e trovo i miei peluche tutti rovinati. Allora "
              "stanotte sono rimasta sveglia a spiare di nascosto, e indovina un po': erano dei "
              "putit a mangiarseli! Devono entrare in casa mia dalla finestra dei vicini. Ti prego, "
              "tu che vai all'avventura, non è che vai a levarmeli di torno?")
RESE[1508] = "Va bene... ma se cambi idea torna, mi raccomando."
RESE[1512] = "Che sollievo! La casa è quella qui accanto, subito a sud. In bocca al lupo!"
RESE[1517] = "Uffa! Anche questo peluche se lo sono mangiato. Ti prego, sbrigati a levarmeli di torno!"
RESE[1533] = ("Eh? Le hai sterminate, le melme? Grazie mille♪ Anche i miei peluche sono contenti. "
              "Tieni, non so se ti servirà, ma prendilo.")

# --- SHENA l'attrazione del locale
# ⚠️ deroga: «Oh it's you, our hero» dice un'altra cosa e per giunta darebbe un
# genere al giocatore. Il giapponese e' いらっしゃいませ～♪その節はどうもです —
# il saluto del locale piu' un grazie per quella volta.
RESE[1542] = "Salve♪ E grazie ancora di quella volta."
RESE[1546] = "Salve♪"
RESE[1547] = "Accettare"
RESE[1548] = "Non ne ho voglia"
# ⚠️ deroga: «With all the mud they leave behind» non c'e' nel giapponese, che
# dice invece di quale banda si tratta — quella che ha messo base a Vernis.
RESE[1549] = ("Scusa, hai un momento? Dal bar continuano a sparire i barili e il gestore è "
              "disperato. Se non hai da fare, ci daresti una mano? Su chi sia il ladro un'idea ce "
              "l'ho: dev'essere quella banda di ladruncoli che si è messa a operare a Vernis! Il "
              "covo mi pare stia dalle parti del cimitero.")
RESE[1552] = "Ah, capisco... peccato."
RESE[1556] = "Ah... grazie mille! Conto su di te!"
RESE[1562] = "Salve, salve♪ L'hai trovato il covo dei ladri? Dovrebbe stare vicino al cimitero."
RESE[1581] = ("Sì, la voce è già arrivata. Con quella banda di teppisti fuori dai piedi ci siamo "
              "tolti un peso. Grazie di cuore. È poca cosa, ma il gestore ti manda questo♪")
