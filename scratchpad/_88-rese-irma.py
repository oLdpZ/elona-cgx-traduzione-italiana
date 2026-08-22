# -*- coding: utf-8 -*-
"""Le rese di IRMA la forgiatrice straniera (`chat.hsp:11206`-`:11770`).

Perimetro: 68 firme dentro, **51 da fare**, zona chiusa, nessuna occorrenza
fuori (`_85-blocco.py 11206`). Le 17 gia' rese sono la testa del menu e i dieci
attributi elementali.

REGISTRO. Irma e' una **nana** (`db_creature.hsp:15838`, `fltnrace == "dwarf"`)
e **donna**: `CDATA_SEX = 1` a `:74075`. Il genere si sa, quindi si usa — e' la
regola della 80a. Parla da vecchia (じゃ / のう / わし / おぬし) e da artigiana:
concreta, brusca e affettuosa. ⚠️ Il tono italiano non si inventa: lo fissa la
resa gia' in build a `:11223` — «Fa davvero cosi' freddo? O sono io che ci ho
fatto il callo...» — colloquiale, senza arcaismi. Le altre due gia' rese che
tengono la mano sono «Bah.» (`:11250`) e «Lascia com'e'» (`:11253`).

⚠️ Irma chiama il giocatore **〜殿**, che l'inglese butta. Si butta anche in
italiano: un vocativo di rispetto in italiano vorrebbe un genere, e il
giocatore non ce l'ha.

LESSICO, cercato e non deciso:

  <Irma> la forgiatrice straniera   `db_creature.hsp:74027`
  <Thalia> la guardastelle          `:74120` — in giapponese si chiama サリム,
                                    l'inglese la ribattezza e noi seguiamo lui
  <Dain> l'anziano della collina    `:74213`, e il diario lo conferma
  pugnale                           `db_item.hsp:152794` e `text.hsp:11436`
  potioman                          `chat.hsp:3017`, `action.hsp:12938`
  incantamento                      `item_func.hsp:2502`, `action.hsp:7716`
  nucleo di Nefia                   `db_item.hsp:138961`
  pergamena di acquisizione di attributi   `db_item.hsp:149507`-`:149508`
  oggetto evolutivo                 `blend.hsp:1124`
  artefatto unico                   `text.hsp:2151` (固定アーティファクト)
  eccezionale / celestiale          `text.hsp:106`, la scala di `_quality`
  Irva Perduta                      `text.hsp:2917`

⚠️⚠️ **IL DIARIO E' UN VINCOLO** (79a): `text.hsp:11436` dice gia' «Devo
parlare con <Irma> e poi mostrare un suo **pugnale** a <Dain>, l'anziano della
collina», e `text.hsp:11618` chiama l'oggetto «[pugnale di Irma]». Le battute
di questo lotto devono usare quelle parole.

⚠️⚠️⚠️ LE DEROGHE DICHIARATE

1. **`:11348` e `:11347` — l'inglese descrive una meccanica che non esiste, e
   costa al giocatore il materiale.** Il giapponese dice che con quindici
   incantamenti pieni «ci monta soltanto roba dello stesso tipo»; l'inglese
   dice «one of them will have to be replaced». **Il codice sta col
   giapponese**: `encadd` (`item_data.hsp:959`-`:973`) cerca uno slot con lo
   STESSO incantamento oppure uno VUOTO, e se non lo trova fa `return 0` —
   nessuna sostituzione, mai. Ma il materiale viene consumato lo stesso
   (`chat.hsp:11653`) e con lui la pergamena (`:11667`): chi si fida
   dell'inglese sceglie «Nessun problema» e perde tutt'e due per niente.
   ⭐ Stessa riga, stesso errore a valle: `:11347` in inglese dice «Sorry.»
   dove il giapponese dice «cancella un incantamento», che e' esattamente quel
   che il codice fa a `:11362`-`:11363`. Una voce di menu deve dire che cosa
   fa.

2. **`:11234`** — l'inglese legge 細工 («lavorazione») come «mystery». E' il
   mestiere di Irma, non un mistero.

3. **`:11247`** — l'inglese taglia 「言っておくが種類は仕上がりに影響せんからの」,
   che e' **l'istruzione**: il tipo di oggetto evolutivo non cambia il
   risultato, e senza quella riga il giocatore va a caccia dell'oggetto
   giusto per niente. Il codice conferma: `:11239` cerca un `ITEM_ID_EVITEM`
   qualsiasi e l'attributo lo sceglie il giocatore a `:11254`-`:11263`.

4. **`:11689`** — l'inglese **ribalta teoria e pratica** («what I need to do
   now is to fully grasp the theory through large amounts of practice» contro
   「理論はわかるんじゃが実践が難しくて」, la teoria la capisco, e' la pratica
   che e' difficile) e **cambia la parentela fra le due tecniche**: per il
   giapponese erano una sola e si sono divise dentro e fuori dalla collina,
   per l'inglese la sua discende da quella della collina. Si segue il
   giapponese: e' la ragione per cui la sua meta' vale quanto l'altra.

5. **`:11705`** — 「どうもよく思われていないようじゃからな」 vuol dire che non
   vedono di buon occhio **lei**; l'inglese lo legge come il giudizio andato
   male («I get the impression that it didn't»). E perde l'ultima mezza frase:
   a non firmarlo, avrebbero trovato da ridire lo stesso.

6. **`:11733`** — 「武骨なデザインじゃが、考えるのに一番悩んだ」 e' un vanto
   sottinteso (il disegno e' rozzo, ma e' quello che le ha dato piu' da
   pensare); l'inglese lo gira in un dubbio su se stessa, «I do worry a bit
   about its design though».

7. **`:11755`** — il giapponese **chiede** al giocatore di portare il pugnale
   all'anziano (「見せてやってくれんかのう」); l'inglese dice solo che lei non
   puo' andarci. La richiesta e' l'istruzione della missione, e il diario
   (`text.hsp:11436`) la da' per fatta.

8. **`:11345`** — 出直す e' «torno un'altra volta», e il codice fa `goto
   *chat_end`: la conversazione finisce. «Let's start over» direbbe che
   ricomincia.

9. **`:11764`** — l'inglese taglia 「他の民は技法を知らぬようじゃし」, cioe' il
   secondo motivo per cui e' bloccata: non e' solo l'anziano che tace, e' che
   gli altri la tecnica non la sanno.

10. **`:11756`** — l'inglese scrive «the dagger(s)» perche' il numero cambia
    col ramo scelto (`GDATA_FLAG_SUB_IRMA_DAGGER` 1-3 e' un pugnale, 4 sono
    tre). L'italiano non ha quella parentesi: si dice «il lavoro di <Irma>»,
    che vale per uno e per tre.
"""

RESE = {}

# ============ l'evoluzione del potioman ============

RESE[11226] = 'Quale potioman?'   # copiata da action.hsp:12938 e chat.hsp:3017
# ⚠️ deroga 2: 細工 e' la lavorazione, non un «mystery».
RESE[11234] = ("Oh, ma che potioman di qualità è questo!? C-con una fattura così, forse ci "
               "posso usare quel trucco del mestiere che mi tengo da parte...")
RESE[11237] = "Ah, è il cambio di attributo di quello che avevi già fatto evolvere."
RESE[11243] = '"Dare " + itemname(ci, 1)'
RESE[11246] = 'Ci penso su'
# ⚠️ deroga 3: l'inglese taglia l'istruzione, che il codice conferma.
RESE[11247] = ("...Va bene, portami un oggetto evolutivo, uno qualsiasi. E ti avverto: il "
               "tipo non cambia il risultato.")
# ⚠️ undici bottoni lasciano tre righe sole (tetto (324 - 11*19 - 43) // 19):
# la resa lunga diceva «Questo qui rinasce prendendo la forza di un attributo...
# quale ti va bene? Tanto lo puoi cambiare dopo, e sceglierlo dal colore non e'
# una cattiva idea» e ne prendeva quattro.
RESE[11264] = ("Questo rinasce con la forza di un attributo... quale ti va? Lo puoi cambiare "
               "anche dopo, e sceglierlo dal colore non è una cattiva idea.")
RESE[11282] = "E-ecco fatto! Questo è il tuo potioman rinato! Tienitelo caro."

# ============ la fusione degli incantamenti ============

RESE[11290] = ('"Oh, mi tieni compagnia mentre faccio pratica? E allora, qual è '
               'l\'equipaggiamento da incantare? Se ne ha già addosso di forti può darsi '
               'che resista alla magia e non ci si riesca. Vediamo... a stare a quella '
               'scala di potenza che dice Thalia, per adesso il limite è " + '
               'gdata(GDATA_THALIA_LIMIT) + " per gli artefatti unici, " + kiseki + " per '
               'quelli eccezionali e " + kiseki2 + " per quelli celestiali. E se non fondi '
               'un nucleo di Nefia, ci vuole anche una pergamena di acquisizione di '
               'attributi."')
RESE[11325] = ("Ah! Questo non si può proprio fare. Gli incantamenti che ha addosso "
               "respingono tutto!")
RESE[11344] = "Mmm."
# ⚠️ deroga 8: 出直す e' «torno un'altra volta», e il codice chiude la chiacchierata.
RESE[11345] = "Torno un'altra volta"
RESE[11346] = 'Nessun problema'
# ⚠️ deroga 1: l'inglese dice «Sorry.» dove il giapponese dice che cosa fa la voce.
RESE[11347] = 'Cancellare un incanto'
# ⚠️ deroga 1: la meccanica dell'inglese non esiste, e il codice lo dimostra.
RESE[11348] = ("Gli incantamenti sono già quindici, tutti pieni. Se lo fondo così com'è ci "
               "monta soltanto roba dello stesso tipo: per te va bene?")
RESE[11355] = ("Cancellarlo, dici? Mmm, con questo incantamento... non si può proprio fare. "
               "Mi dispiace.")
RESE[11358] = ("Cancellarlo, dici? Mmm, con questo qualcosa si può fare: gli raschio via il "
               "legame...")
RESE[11364] = 'itemname(cibk) + " perde un incantamento."'
RESE[11367] = "E allora, la forza di quale oggetto devo incastrare nell'artefatto?"
RESE[11377] = ("Mmm, vediamo... ma un momento, non ce l'hai una pergamena di acquisizione "
               "di attributi.")
RESE[11661] = "...Fusione degli incantamenti completata! È stata una bella pratica."

# ============ la sottotrama chiusa: la tecnica delle due metà ============

RESE[11688] = ("Mi sarebbe piaciuto lavorare alla luce del sole nella terra dei miei "
               "antenati, ma ormai è andata così e non c'è rimedio. Del resto starsene a "
               "lavorare con calma in un posto tranquillo non è male.")
# ⚠️ deroga 4: l'inglese ribalta teoria e pratica e cambia la parentela fra le tecniche.
RESE[11689] = ("La tecnica tradizionale che mi ha insegnato Thalia, la teoria la capisco: è "
               "metterla in pratica che è difficile. Dentro e fuori dalla collina si è "
               "divisa in due, e anche se all'origine era una sola, poi ognuna è andata per "
               "la sua strada. Per riportarle a una forma sola, dopo centinaia di "
               "generazioni, mi serve ancora un po' di tempo.")
RESE[11690] = ("Se ti va, passa a trovarmi ogni tanto. E se mi porti qualche oggetto buono "
               "per far pratica di sintesi, mi fai un favore.")

# ============ il giudizio dell'anziano ============

RESE[11699] = 'Meglio non saperlo'
# ⚠️ Irma e' donna e il codice lo dice (CDATA_SEX = 1): l'accordo si fa.
RESE[11700] = 'Ti hanno stroncata'
RESE[11701] = "Perché l'hai firmato?"
RESE[11702] = "Com'è andata?"
# ⚠️ deroga 5: non vedono di buon occhio LEI, e l'inglese perde l'ultima mezza frase.
RESE[11705] = ("Se non lo firmavo, anche con un buon giudizio non avrei potuto dimostrare "
               "che l'ho fatto io. E poi qui non mi vedono di buon occhio... A non "
               "firmarlo, avrebbero trovato da ridire lo stesso.")
RESE[11708] = "...Capisco."

# ============ i tre pugnali ============

RESE[11714] = 'Non vedo l\'ora'
RESE[11715] = 'Cambiare pugnale'
RESE[11716] = ("Chissà come andrà. Se il giudizio è buono, magari mi metto a fare artefatti "
               "con la stessa forma.")
RESE[11723] = ('"Oh, guarda qua, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + "! Su proposta di '
               'Thalia ho provato a fare tre pugnali di gusto diverso."')
RESE[11725] = 'Il pugnale pratico'
RESE[11726] = 'Il pugnale decorato'
RESE[11727] = 'Il pugnale originale'
RESE[11728] = 'Mostrarli tutti e tre'
RESE[11729] = 'Dipende dagli incanti'
RESE[11730] = ("Secondo te quale piacerà di più? Anche se che cosa conta di più, alla fine, "
               "è questione di gusti.")
# ⚠️ deroga 6: l'inglese gira in dubbio quello che e' un vanto.
RESE[11733] = ("Già. Alla fine quel che conta è come ti viene in mano. Questo ha "
               "l'impugnatura regolabile che si adatta al palmo, e una lama di tempra "
               "eccezionale. Il disegno è rozzo, ma forse è quello che mi ha fatto "
               "scervellare di più.")
RESE[11737] = ("Eh. Mettere decorazioni così minute su un pugnale piccolo come questo mi è "
               "costato fatica. Anche la precisione è una misura del mestiere, quindi mi ci "
               "sono messa di buzzo buono.")
RESE[11741] = ("Eh eh. Sembrerà stravagante, ma quella forma ha la sua logica. Con una "
               "struttura tutta sua basta appoggiarlo appena e taglia come nessun pugnale "
               "normale.")
RESE[11745] = ("Giusto... in effetti far vedere quanto è ampia la mia mano non è una cattiva "
               "idea. Su una cosa troppo specializzata i gusti si dividono.")
RESE[11749] = "No, ecco... io parlavo della forma, non intendevo quello..."
RESE[11754] = "Mmm..."
# ⚠️ deroga 7: il giapponese CHIEDE, e la richiesta e' l'istruzione della missione.
RESE[11755] = ('"Scusa. Quel pugnale, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", non è che '
               'lo mostreresti tu all\'anziano della collina? Se ci vado io mi urla dietro '
               'e mi sbatte la porta in faccia, lo so già..."')
# ⚠️ deroga 10: «the dagger(s)» non ha un corrispondente italiano.
RESE[11756] = 'Hai preso in consegna il lavoro di <Irma>.'

# ============ il primo incontro: perché è bloccata ============

RESE[11762] = ("Mmm, che guaio... Mi sono ritrovata avvolta dalla luce e sono finita su "
               "questo continente... e girovagando ho trovato la terra dei miei antenati. "
               "Sul momento mi ero commossa: pensavo fosse proprio il cielo a guidarmi. E "
               "invece...")
RESE[11763] = ("Qui non mi vogliono, si vede... ahimè. Mentre sono fuori mi rompono gli "
               "attrezzi, mi nascondono i materiali: un disastro. E quando chiedo chi è "
               "stato, finisce che mi rinfacciano di tenere male la roba...")
# ⚠️ deroga 9: l'inglese taglia il secondo motivo per cui e' bloccata.
RESE[11764] = ('"Ma io non ci rinuncio! Il mio sogno è imparare la tecnica che si tramanda '
               'su questa collina, unirla alla mia e tirar fuori le armi più belle che si '
               'siano mai viste! Solo che l\'anziano non mi insegna niente, e gli altri la '
               'tecnica pare non la sappiano... Sono in un vicolo cieco. Se vieni a sapere '
               'qualcosa di buono, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", dimmelo..."')
