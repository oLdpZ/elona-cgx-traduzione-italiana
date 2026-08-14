# Ripresa sessione

Aggiornato: 2026-08-14, fine della **trentottesima** sessione.

⭐ **La 38ª è la sessione che ha scoperto quanto manca davvero.** Tre lotti su
`proc.hsp` — `017`, `018`, `019` — **129 rese, dal 65% al 76%**, cinque spinte,
zero collaudo. Ma la cosa che conta non è un lotto: è che alla domanda «a che
punto siamo» il progetto rispondeva **47%** e la risposta vera è **35%**.

### ⚠️⚠️ Le quattro cose che la prossima sessione deve sapere

1. ⭐⭐ **Il perimetro dichiarato non è il gioco: 47% e 35% sono due risposte
   diverse, e vanno tenute distinte.** Misurato con
   **`scratchpad/perimetro.py`**, che rifà il conto da capo. Dentro il perimetro
   `lang()` siamo a 10.940 firme su ~23.089, cioè **47%**. Ma due blocchi di
   testo che il giocatore legge non erano **mai stati contati da nessuna parte**:
   - **le descrizioni degli oggetti, 5.284, zero tradotte.** `db_item.hsp` le
     scrive `description(0..3) = "..."` dentro un `if ( jp ) ... else`, **non**
     dentro `lang()`: `estrai.py` non le vede, quindi non sono tradotte **e non
     risultano fra quelle da fare**. `else_jp.py` le contava come «6.840 righe
     già dichiarate fuori perimetro» senza mai dire **quante voci** fossero;
   - **i quattro file di `data/`, ~2.900 righe inglesi, zero tradotte**:
     `book.txt` (i 33 libri, **67.184 caratteri d'inglese**), `talk.txt`,
     `exhelp.txt`, `board.txt`. Il gioco li carica con `noteload` a runtime;
     `SPEC.md` §6 li chiama «aggiuntivi» e non li ha mai aperti.

   **Totale reale ~31.306, fatto il 35%.** ⚠️ E in **caratteri** il divario è
   peggiore: quella roba è prosa continua, non righe di log. 💡 In compenso è il
   lavoro **meno insidioso** del progetto — niente `name()` da accordare, niente
   participi, niente reti — ma vuole una **catena di strumenti diversa**, perché
   non ha firma `lang()` e non passa da `applica.py`.
2. ⭐ **Una variabile può portarsi dentro l'inglese, ed è il terzo punto cieco.**
   `proc.hsp:16980` fa `studybuddy = "your friends"` fuori da `lang()` e `:16991`
   lo interpola: la resa naturale avrebbe stampato «Cominci un circolo di lettura
   con **your friends**». ⚠️ **Non la vede nessuno dei due referti**:
   `blocchi_en.py` guarda dentro `if ( en )`, `else_jp.py` dentro
   `if ( jp ) ... else`, e quello è un **assegnamento incondizionato**.
   ✅ Misurato con **`scratchpad/variabili_en.py`**: 66 variabili, **3 trappole**
   vere. ⚠️ **La terza è ancora da fare**: `economy.hsp:319` (`s1` =
   «Neutral»/«Law»/«Chaos», in tutt'e due i rami di `lang()`). La seconda,
   `performerpal` a `:19178`, è stata schivata nel lotto 019 lo stesso giorno.
3. ⚠️⚠️ **Quattro righe dove l'inglese nomina il personaggio sbagliato**, tutte
   nel lotto 019, e ogni volta giapponese **e codice** dicono la stessa cosa
   contro di lui: `:18280` (dice `tc`, ma la riga sopra scrive in
   `cdata(cnt, CHARA_PLAYER)`), `:18309` e `:18429` (dicono `tc` dove chi agisce
   è `cc`), `:18744` (dice `tc` dove il giapponese dice `name(0)`). Con le tre
   dei lotti 017-018 la serie degli errori di monte passa da 11 a **diciannove**.
4. ⚠️ **`:18280` mostra il limite della rete 11 meglio di qualunque esempio
   finora.** La rete pretende che le funzioni di contenuto coincidano con quelle
   dell'**inglese**, e lì l'inglese ha **un** `name()` mentre il giapponese ne ha
   **due**. Quindi la resa non può nominarli tutt'e due **nemmeno sapendo che il
   giapponese ha ragione**: nomina il soggetto — quello che il codice conferma —
   e lascia implicito il resto.

### Le tre cose più piccole, che servono lo stesso

- 💡 **Una firma copre più siti, e il lotto 017 ne ha avuto la prova.**
  `proc.hsp` ha **due blocchi identici** per Tiro a segno (`_switch_val == 738` a
  `:16079` e `SKILL_SPACT_STRUCK_OUT` a `:16251`): il secondo non entra
  nell'estrazione, ma nel sorgente di build sono tradotti **tutt'e due**. Non
  cercare la voce mancante: non manca.
- ⚠️ **`verifica` ha fermato «Ensemble!»** per «traduzione identica
  all'inglese». Il nome della mossa era già invariato in `skill.hsp`, ma **col
  punto esclamativo è un'altra stringa** e il confronto è sulla stringa intera.
  Dichiarato in `invariati.md`. Succederà di nuovo con ogni verso di una mossa
  già invariata.
- ✅ **`dossier.py` adesso legge il `SORGENTE`**, non la build, come la 37ª
  chiedeva. (`proc.hsp` ha lo stesso numero di righe nei due alberi, quindi non
  aveva ancora ingannato nessuno.)

### I tre lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `-017` | 15500-16999 | navi, ricarica, muri e porte, azioni speciali di barra, meteore, cannone di sabbia, circolo di lettura | 49 |
| `-018` | 17000-17999 | scrigni, Duplibacchetta, jujitsu, X-Frame, il legame, la richiesta d'aiuto | 42 |
| `-019` | 18000-19999 | plagio, ipnosi, scansione dati, trasfusione, ensemble, pesca dimensionale, origami | 38 |

💡 **Il lotto 018 ha la percentuale di copie più alta di tutto `proc.hsp`: nove
su quarantadue.** Otto vengono dallo stesso posto — i versi dell'**X-Frame**
(`:17415`-`:17444`) stanno già in `action.hsp:12960`-`:12989` parola per parola,
perché il mod stampa la stessa sequenza da due punti.

⚠️ **E il 019 mostra il rovescio**: `:19303` e `:19307` hanno lo **stesso inglese**
di `proc.hsp:5332` e `:5063` ma un giapponese **diverso** — 亜空釣り è la **Pesca
dimensionale** (`skill.hsp:1608`), non la pesca normale. Copiare sull'inglese
avrebbe perso la distinzione. **Si copia sul giapponese, mai sull'inglese.**

💡 **La strada del participio regge da tre lotti**: venti rese in tutto girate
per non far concordare un participio o un aggettivo. La sostanza diventa
soggetto («Le schegge colpiscono X», «Il luccichio abbaglia X»), il verbo diventa
riflessivo («si ricarica», «cambia forma»), o l'accordo si sposta su un **nome**
(«acquista la leggerezza di una piuma», «acquista il peso di un macigno»).
⚠️ Il caso più stretto è `:19102`, la trasfusione: l'inglese dice «from X to Y» e
in italiano **tutt'e due** le preposizioni si fondono con l'articolo che `name()`
porta dentro. I tre nomi diventano soggetti — «X trasfonde il sangue: lo cede Y e
lo riceve Z».

---

## La trentasettesima sessione

⭐ **La 37ª è la sessione che ha trovato più difetti fuori dai lotti che dentro.**
Tre lotti su `proc.hsp` — `014`, `015`, `016` — **146 rese, dal 51% al 65%**, e
per arrivarci sono saltati fuori **nove difetti veri in rese già entrate**, più
**sei reti nuove o rifatte**, di cui tre sbagliavano loro. Cinque spinte.

### ⚠️⚠️ Le tre cose che la prossima sessione deve sapere

1. ⭐ **La rete 6 non vedeva i commenti di BLOCCO, e adesso sì.**
   `proc.hsp:11796` sta dentro un `/* ORIGINAL - BEGINNING ... ENDING */` — il
   codice di monte che il mod spegne per togliere il tetto ai punti bonus — e la
   rete guardava solo le righe che cominciano per `;`. ✅ Allargata con
   `scratchpad/commenti-blocco.py`, che legge il **`SORGENTE` pinnato**.
   💡 E la misura sul dizionario intero dice che era già successo: **7 voci
   tradotte stanno dentro un blocco spento** (6 in `action.hsp`, `proc.hsp:1000`).
   Non è un difetto a schermo, è lavoro speso su testo morto.
   ⚠️ **E la misura ha ingannato prima di dare il numero giusto**: fatta sulla
   **build** ne accusava 9, e le due di `text.hsp` erano giuste. Quella build ha
   **una riga in più** del sorgente (12.528 contro 12.527) perché una toppa ce
   l'ha aggiunta, e da lì in giù i numeri di riga del dizionario non tornano.
   **Chi incrocia numeri di riga e dizionario deve leggere il `SORGENTE`.**
   ⚠️ Vale anche per `dossier.py`, che oggi legge la build.
2. ⚠️⚠️ **Sei rese già entrate stampavano «di il», «a il», «in il», «su il».**
   La rete 8 è del lotto 009 (35ª) e da allora ferma i lotti nuovi, ma **nessuno
   l'aveva mai passata all'indietro**. `scratchpad/rete8_dizionario.py` lo fa:
   `action.hsp:11810`, `:12706`, `:18997` (due in una riga), `:19004`,
   `proc.hsp:1966`. ✅ Corrette. Il referto adesso dà **3**, tutti dichiarati
   falsi positivi («con» non si fonde, «hai tirato **su**» è un verbo
   sintagmatico, e `valn = skillname` non porta articolo).
   💡 Il perché `cdatan` conta quanto `name` sta in una toppa: `init.hsp:1717`
   diceva `return "the " + cdatan(...)`, la toppa toglie il `"the "`, e da lì
   `name(x)` e `cdatan(CDATAN_NAME, x)` **restituiscono la stessa stringa**,
   articolo italiano compreso.
3. ⚠️ **`verifica --dizionario` NON valida le rese**: confronta il dizionario col
   sorgente e conta orfane e non tradotte. Una correzione scritta a mano nel
   dizionario **non incontrava nessuna guardia**. ✅ Adesso gli script di
   correzione passano le rese nuove a `controlla_lotto` (vedi
   `scratchpad/correzione-rete8.py`).

### Le sei reti nuove o rifatte, e tre sbagliavano loro

| # | che cosa | il caso |
|---|---|---|
| 6 allargata | i blocchi `/* ... */` | `:11796`, vedi sopra |
| **12 nuova** | la resa di una **dinamica** dev'essere un'espressione HSP, non testo nudo | ⚠️ **l'ha trovata il compilatore, non le reti**: `:11534` è dinamica perché l'inglese porta `his(tc)`, ma in italiano la morfologia sparisce e resta una frase sola. Senza virgolette `applica.py` l'ha scritta come **codice** — `error 4`, con «qualche» letto come nome di variabile. Undici reti, `verifica` e le guardie l'avevano lasciata passare |
| **13 nuova** | un **inglese solo per due giapponesi diversi** (referto, non errore) | `:14521`/`:14573`: «The air around you gradually loses power» sta per la **fuga** e per il **ritorno**, due incantesimi diversi con due pergamene diverse |
| 8 rifatta | sbagliava lei: `valn` non è sempre un `itemname()` | a `:11893` il sorgente dice `valn = skillname(i)` due righe sopra, e i nomi di abilità non portano articolo. Adesso **legge l'assegnamento più vicino**. ⚠️ Ma a `:14755` `valn` **è** un `itemname(i, 1, 1)`: la rete aveva ragione lì |
| 4 rifatta | sbagliava lei: litigava con la rete 11 | `:12837` e `:13298` hanno lo **stesso giapponese** e un inglese che nomina **un numero diverso di personaggi**. La 11 pretende le funzioni dell'inglese, la 4 pretendeva le stesse parole: non si può, e la differenza **la impone il sorgente**. Adesso raggruppa per **(giapponese, funzioni di contenuto)** |
| 3 rifatta | gridava su rese identiche | confrontava le **espressioni**: `:12287` e `action.hsp:18755` dicono le stesse parole su variabili diverse. Adesso confronta i **letterali** e dice 💡 invece di ⚠️ |

### Le tre divergenze vecchie corrette, e una lasciata apposta

1. **«Nothing happens...»** esisteva in due rese, e una delle due è il
   `#define global txt_nothinghappens` di `text.hsp:1`, cioè quella che il gioco
   stampa **dappertutto**. `action.hsp:8936` diceva «Non succede *nulla*...».
   Vince il macro.
2. 「小さなメダル」 è **«medaglietta»** in `db_item.hsp:144256`, ma
   `action.hsp:6254` diceva «Trovi una **monetina**!»: si trovava una monetina e
   nello zaino c'era una medaglietta. ⚠️ **A sviare è l'inglese di monte**, che
   scrive `small coin` nel messaggio e `small medal` nel nome. È il `Bolt` della
   35ª in miniatura.
3. **«ha di nuovo il mana pieno» non è vero in nessuno dei due siti che lo
   dicono.** `proc.hsp:14597` ha lo stesso giapponese di `action.hsp:1096`, e il
   codice dice che pieno non lo è mai: `healmp 0, charge*5*num` di là,
   `MAX_MP/10 + rnd(...) + 5` di qua. È la lezione della 33ª — per una riga che
   descrive un effetto **l'arbitro è il codice** — su una resa che l'inglese
   («mana is restored») non bastava a smentire.
4. ⚠️ **Lasciata apposta**: 「この場所では効果がない。」 è «Qui non funziona.» a
   `action.hsp:196` e «In questo luogo non ha effetto.» a `:8552`. A distinguerli
   è **l'inglese**, e `:196` sta accanto a `:179`, che ha un giapponese diverso e
   la stessa resa breve. Non toccare.

### ⚠️ Il genitivo davanti a `name()` non esiste, e le tre zone ne chiedevano dieci

`name()` porta già l'articolo («il putit») ma non sempre («Sinaha»), quindi né
«di » né «del » funzionano. La strada è quella che `proc.hsp:8759` e `:8786`
avevano già aperto senza dichiararla — il **`-ne` enclitico** («colpisce X
facendo**ne** saltare la testa») — o il nome come **complemento oggetto**
(«attacca X puntando alla testa»). 💡 E per le tre parate del lotto 015 la forma
**«X attacca, ma Y para»** risolve tutto in un colpo: i due nomi diventano
tutt'e due soggetti, e la differenza resta dove il sorgente la mette (a mani
nude, con l'arma, con lo scudo).

💡 **Stesso problema, stessa strada, per il participio.** Nel lotto 016 undici
rese descrivono qualcosa che *succede a* `tc` e l'inglese le scrive col
participio («is hit by poison», «was showered by acid»): in italiano
concorderebbe col personaggio. La sostanza diventa **soggetto** — «Il veleno
investe X», «Il torpore prende X».

### ⚠️ Undici errori dell'inglese di monte, e la serie continua

Alle sei della 35ª questa sessione ne aggiunge cinque: `:12837` (dice che a
parare è chi attacca), `:14021` (dice `cc` dove il `cbitmod` sotto fa `tc`),
`:11870` (ricopia parola per parola la riga sopra), `:14521`/`:14573` (un inglese
per due incantesimi), `:14673` (un tanfo al posto di un mal di testa). **Tutti
raddrizzati sul giapponese**, e `verifica` lo permette perché accetta ogni
chiamata che compaia in **una delle due** forme di monte (`verifica.py:384`).

### 💡 `his2` della 36ª ha un fratello: `godname()` restituisce inglese

`god.hsp:81-89` scrive `godname(2) = lang("風のルルウィ", "Lulwy of Wind")`, e
`god.hsp` **non ha dizionario** — è uno dei 40 file mai estratti. Quindi
`proc.hsp:11749` a schermo dirà «lo sguardo benevolo di **Lulwy of Wind**» finché
non si traduce. Non è un difetto della resa, è la dipendenza nota di
`his(tc, 1)` a `:8849` in forma nuova. ⚠️ E quando si tradurrà:
`sdim godname, 20, 9` dà 20 byte, «Kumiromi del Raccolto» ne occupa 21.

💡 **Un invariante nuovo**: `proc.hsp:12101` è `"*" + skillname(efid) + "* "`,
l'intestazione dell'azione speciale. Tutto il testo viene da `skillname()`, fuori
restano due asterischi e uno spazio: dichiarato in `invariati.md`, sezione
«Versi senza contenuto linguistico».

---

## La trentaseiesima sessione

### Quello che il collaudo ha trovato, ed è la parte che conta

1. ✅ **Le dieci teste «… e» del log funzionano**, viste due volte a schermo
   («`<Sinaha> colpisce da lontano l'artista di strada e (3899) ne fa brandelli
   di carne.`»). Era il rischio più temuto della 35ª e non c'era: lo spazio lo
   mette `msgtemp += " "` a `init.hsp:1666`, che gira su **ogni** `txt`.
2. ⚠️⚠️ **La maiuscola d'ufficio non gira, e la ripresa diceva il contrario.**
   A schermo ogni riga che comincia con `name(cc)` era minuscola: «`[19:07] il
   viandante finisce di mangiare una razione.`». Il prefisso dell'orologio
   (`cfg_msgaddtime`) si attacca a `msgtemp` alla riga **1578**, cioè 81 righe
   **prima** del controllo di `:1659`, e a quel punto `peek(msgtemp, 0)` legge
   `[`. Con il timestamp acceso la maiuscola **non scatta mai, su nessuna riga,
   in nessuna lingua** — nemmeno per l'inglese di monte, che scrive «`you finish
   eating.`». ✅ Toppato maiuscolando subito dopo `tnew = 0` (`init.hsp:1568`),
   prima che i prefissi si attacchino, con le stesse due guardie dell'originale.
   **Riguardato a schermo: «`Il viandante finisce di mangiare una razione.`»**
3. ⚠️ **`valn` da soggetto vuole il determinativo, e `itemname()` non lo dà.**
   A schermo: «`Un pozzo disseta <Sinaha>.`» `itemname()` mette il determinativo
   **solo agli artefatti identificati** (`item_func.hsp:1944`) e
   l'indeterminativo a tutto il resto: è il calco di `a well` / `the Painful
   Master`. Da complemento andava bene, da soggetto no. ✅ Toppato usando
   `ioriginalnamearticolodet` — **1.309 articoli determinativi già in
   `db_item.hsp`, mai usati così** — più `itemname(ci, 1, 1)`, che è l'idioma con
   cui upstream chiede il nome nudo.

> 💡 **Il filo delle ultime tre sessioni, in tre forme.** La 34ª: la catena
> verde non dice niente sulla lingua che il giocatore legge. La 35ª: non dice
> niente sulla coerenza fra due file. La 36ª: **non dice niente su un'opzione
> del giocatore.** Nessuna verifica accende `cfg_msgaddtime`, e il difetto viveva
> o moriva su una casella delle impostazioni.

### ⚠️ Il pozzo NON è stato riguardato a schermo

La toppa è compilata e installata dalle 11:34, ma al collaudo il personaggio era
troppo pieno per bere e il messaggio non è mai partito. **È la prima cosa da
fare aprendo il gioco**: cammina finché non ti viene sete, poi `h` su un pozzo.

| cosa | atteso |
|---|---|
| bevi al pozzo | `Il pozzo disseta il viandante.` |
| bevi alla fontana | `La fontana disseta il viandante.` (prova che il genere segue) |
| pozzo prosciugato | `Il pozzo non ha più acqua.` |
| benedici l'equipaggiamento | `<nome> ha l'equipaggiamento avvolto in una luce bianca.` (toppa `his2`) |

💡 `You see un pozzo placed here.` **è giusto così**: è `command.hsp:30`, un sito
diverso dove il pozzo è complemento oggetto. La toppa tocca solo `*drinkWell`.

### Le tre reti nuove, e una che era sbagliata

⭐ **Rete 11 — le funzioni di contenuto devono coincidere, e non se ne può
AGGIUNGERE nessuna.** `verifica.py:367` confronta `funzioni_di_contenuto` di
inglese e resa: stesse funzioni, stesso ordine. Il caso che l'ha imposta è
`:10312`, dove l'inglese ha solo `his(tc)` (morfologia, zero contenuto) e il
giapponese invece **nomina il soggetto**: la resa italiana non può nominarlo.
⚠️ **Ed è nata sbagliata**: girava anche sulle statiche dentro `cnvtalk()`, dove
l'`en_grezzo` porta l'involucro ma la resa è testo nudo — avrebbe bocciato
**undici rese giuste**. Ora gira solo sulle dinamiche, che è dove `verifica.py`
la mette.
⭐ **E si è guadagnata il posto un lotto dopo**, bocciando `:11481` con
«mancanti `['his2']`»: vedi la rinviata qui sotto.

💡 **Rete 10** — `his(x, 1)` è contenuto e resta, ma in italiano varrà «il suo» /
«il tuo» per **tutti** i siti, perché la funzione sceglie sul genere del
**possessore** mentre l'italiano accorda col **posseduto**. Quindi ogni sito che
la usa deve metterle accanto un **nome maschile singolare**. La 35ª l'aveva già
rispettato senza dirlo (`:8849`, «sangue»); la rete adesso stampa il nome retto.

💡 **Rete 4 rifatta**: confrontava le rese di uno stesso giapponese come
**espressioni** e avrebbe bocciato `:9605`/`:9612`, che dicono le stesse identiche
parole su due variabili diverse. Adesso confronta i **letterali di testo**.

### ⚠️ La rinviata: `his2()` non è traducibile, e non per il motivo che sembrava

`init.hsp:1881`:

```hsp
#defcfunc his2 int EntityID
    if ( EntityID == CHARA_PLAYER ) { return "your" }
    return name(EntityID)
```

**Porta il nome** — per questo è contenuto e `verifica` pretende che resti — ma
nel ramo del giocatore restituisce il letterale nudo `"your"` **fuori da
`lang()`**. Quel «your» resta inglese per sempre: non lo raggiunge il dizionario
oggi e non lo raggiungerà la traduzione di `init.hsp` domani, perché non c'è
niente da tradurre. Stessa classe di `bufftxt(1)` della 28ª. ⚠️ **E nessuna resa
regge tutt'e due gli esiti**, perché `his2()` dà un **possessivo** in un caso e un
**nome con l'articolo** nell'altro. Quindi `proc.hsp:11481` è **rinviata a
toppa**, e la toppa è fatta.

💡 **Da qui una domanda aperta e misurabile**: `blocchi_en.py` conta i letterali
inglesi nudi **nel sorgente**, ma non quelli che escono da una **funzione** come
`his2()`. Nessuno ha mai contato le `#defcfunc` di `init.hsp` che restituiscono
inglese senza `lang()`. `his2` e `your2` sono due; quante sono in tutto?

### Nuovo strumento: `scratchpad/dossier.py`

Mette insieme le tre letture che ogni lotto rifaceva a mano — il sorgente
intorno alla riga, le rese gemelle per **giapponese**, quelle per **inglese**.
Sui tre lotti ha pescato **undici copie** da non ridecidere: `Tyris del Nord`,
`Tyris del Sud`, `Irva Perduta`, `filtro d'amore`, `benzina`, `olio essenziale`,
`coppia`, `non morti`, `spazzatura`, `Grazie!`, più due rese di `proc.hsp`
stesso. È la regola «cercare prima di scrivere» resa meccanica.

⭐ **La 35ª è stata la sessione più produttiva del progetto su un file solo:
`proc.hsp` passa da 207 rese a 442, cioè da 19% a 40%,** in sei lotti
(`fase4-proc-005` … `-010`) più una correzione. **235 rese, 298 siti**, sette
spinte, zero regressioni. Quello che ha trovato conta più dei numeri:

1. ⭐ **`valn` è un `itemname()`** (`proc.hsp:6950`, `:6965`, `:6970`), quindi
   porta l'articolo italiano e non regge `di`/`da`/`in`/`su` davanti. L'inglese
   ce ne mette quattro in una zona sola. È la scoperta di `itemname()` del lotto
   005 **travestita da variabile**: guardando la riga non c'è modo di saperlo.
2. ⭐ **Una regola scritta e non sorvegliata**: `glossario.md` dice `Bolt` →
   «Saetta» dal 2026-08-09, e `db_item.hsp` diceva «dardo» in **15 nomi**. Si
   comprava il libro del *dardo* e si imparava la *saetta*. Non è una decisione
   presa due volte: è una decisione presa una volta e **mai applicata**, perché
   **nessuno strumento confronta il glossario col dizionario**.
3. ⚠️ **Sei errori dell'inglese di monte**, tutti raddrizzati sul giapponese:
   due code scambiate a `:4872`, un «robs **me**» a `:4906`, `name(tc)` per
   `name(cc)` a `:6200`, «cliche» per 王道 a `:6148`, «regretted being born» per
   una frase che parla d'allucinazioni a `:6876`, e «The ball hits» copiato su un
   fulmine a `:8334`.
4. ⚠️ **Due voci che non erano testo**: `:5584` «Merchant ship» e «Pirate ship»
   sono **operandi di confronto** con `map.hsp`. È la seconda «Party Room» dello
   stesso file.
5. 💡 **Cinque reti nuove** negli script dei lotti (5-9), e **ognuna nasce da un
   caso reale di questa sessione**, non da un'idea.

💡 **Il filo che le tiene insieme**: la 34ª aveva mostrato che la catena verde
non dice niente sulla lingua che il giocatore legge. La 35ª mostra il gemello —
**la catena verde non dice niente sulla coerenza fra due file**. Il `Bolt` stava
lì da otto mesi con tutte le verifiche a posto.

### ⚠️ Il debito di collaudo è tornato a salire, ed è la cosa da sapere

**235 rese nuove e nessuna vista a schermo.** La 34ª aveva fatto scendere il
debito per la prima volta; questa lo raddoppia. `cgx-test.exe` è rifatto e
aggiornato (14/08, 10:30), quindi il collaudo si può fare subito, e la roba nuova
è **facile da vedere**: dormire, mangiare, pescare, scavare, viaggiare sulla
mappa e un combattimento qualsiasi coprono quasi tutta la zona 3401-9200.

💡 **Da guardare per primi, perché sono quelli dove ho cambiato la struttura e
non solo le parole:**

| cosa | dove esce | perché guardarla |
|---|---|---|
| il pozzo e la fontana | bevi a un pozzo, cadici dentro | `valn` è diventato **soggetto**: «Il pozzo disseta il viandante» invece di «beve dal pozzo». Se l'articolo sbaglia si vede subito |
| le teste «… e» del log | un combattimento qualsiasi | dieci rese si saldano alla coda di danno di `chara_func.hsp`. Basta uno spazio storto e si legge «colpisce il putit einfligge una ferita» |
| il portello del rifugio | usa un rifugio portatile | l'unica resa dove ho girato la frase per togliere un «di » + `itemname` |
| i sei gradini della sazietà | mangia sei volte con fame diversa | venti rese pescate a caso; è dove l'accordo di genere rischiava di più |
| `his(tc, 1)` a `:8849` | fatti succhiare il sangue da un alleato | ⚠️ **stamperà ancora `his`/`her`/`your`** finché `init.hsp` non è tradotto. Non è un difetto della resa, è la dipendenza nota |

## ⚠️ Prima di tutto: il progetto vive su due macchine

**La 29ª è stata fatta dal portatile**, non dalla macchina di Firenze. È la prima
volta, e va saputo perché spiega tutto quello che sembrava rotto: all'apertura
**nessuno strumento partiva**, c'erano solo Python **3.7** (Anaconda) e **3.8**,
e gli strumenti usano `str | None`, quindi `strumenti.creature` moriva alla riga
67 prima di leggere un file. Non era un guasto e non era una macchina ripulita:
era **una macchina dove non era mai stato installato niente**. Idem per Elin,
l'identità git e i plugin.

**Risolto installando Python 3.12.10** (`winget install Python.Python.3.12
--scope user`) più `pytest`. Se succede di nuovo, il sintomo è
`TypeError: 'type' object is not subscriptable`, e non è un guasto del codice.

⚠️ **Da qui nasce il rischio vero: le due copie possono divergere.** All'inizio
della 29ª `origin/fase-0` era fermo a `8a10f82`, cioè **38 commit indietro**:
tutto il lavoro dalla 26ª in poi — 1.089 battute più i 71 `buffname` — stava
solo sul disco del portatile. È la stessa trappola della 28ª (lavoro fuori da
git), in una forma nuova: dentro git, ma su una macchina sola.

💡 **La regola: si spinge a fine sessione, sempre**, e la prima cosa che si fa
aprendo una sessione su una macchina qualsiasi è `git fetch && git status -sb`.
Chi apre a Firenze senza guardare riparte da prima di ferragosto.

✅ **Spinto di nuovo a fine 30ª, 31ª, 32ª, 33ª, 34ª, 35ª, 36ª, 37ª e 38ª**, sempre
dal portatile. Tutt'e nove hanno aperto con `git fetch && git status -sb` e
tutt'e nove hanno trovato le copie allineate: la regola ha tenuto **nove volte di
fila**. 💡 La 38ª ha spinto **cinque volte** — tre lotti e due referti — una per
risultato chiuso.
💡 **La 36ª ha spinto cinque volte** — due toppe, tre lotti — e **la 37ª cinque**
— tre lotti, le sei preposizioni, la chiusura — una per risultato chiuso.
💡 **La 34ª ha spinto quattro volte e la 35ª sette**, una per risultato chiuso
invece che tutto in fondo: se la sessione si fosse interrotta a metà, il lavoro
fatto era già al sicuro. Con sei lotti in una sessione non è più una comodità, è
il modo normale di lavorare. Al 14/08 **il lavoro prosegue dal portatile**: la
macchina di Firenze riprende a fine vacanze, e lì la prima cosa è `git pull`, non
`git push`.

Sul portatile ogni comando degli strumenti va aperto così, perché `python`
nudo è il segnaposto del Microsoft Store e non esegue niente:

```powershell
$py = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
& $py -m strumenti.<nome>
```

💡 Due comodità rimesse lo stesso giorno, se mancassero: la barra del contesto
(`~/.claude/statusline.py` + `statusLine` in `~/.claude/settings.json`) e
Windows Terminal — il console host classico usa Consolas, che **non ha il
giapponese** e lo stampa come `?`, il che rende illeggibili le colonne `jp`.

## La prima cosa da fare

⚠️⚠️⚠️ **Il collaudo, e adesso il debito è a 396 rese mai viste a schermo.** Sono
le 121 della 36ª, le 146 della 37ª e le **129 della 38ª**, e né la 37ª né la 38ª
hanno aperto il gioco una sola volta. **Due sessioni di fila senza collaudo: non
era mai successo.** `cgx-test.exe` è stato rifatto a fine 38ª e contiene tutto.

💡 **Le 129 della 38ª sono log di combattimento e azioni speciali**, quindi si
vedono con un combattimento qualsiasi e la barra piena. Da guardare per primi,
perché sono quelli dove è cambiata la struttura e non solo le parole:

| cosa | come | perché |
|---|---|---|
| ⚠️ **il pozzo e la fontana** | cammina finché non ti viene sete, poi `h` su un pozzo | è la toppa della 36ª **mai riguardata**, e adesso sono tre sessioni |
| la trasfusione | azione speciale **Trasfusione diretta** | i **tre nomi come soggetti**: «X trasfonde il sangue: lo cede Y e lo riceve Z». È la forma più forzata di tutta la sessione |
| il circolo di lettura e l'ensemble | azioni speciali **Circolo di lettura** e **Ensemble**, con almeno **due** alleati vicini | è il ramo dove il gioco scriveva «your friends»: deve dire «i tuoi compagni» |
| il richiamo di un alleato | azione speciale **Chiama alleato** | `:19066` è la coda di una frase che comincia col nome **fuori** da `lang()`: se lo spazio iniziale è sbagliato si legge «Xappare dal nulla» |
| l'X-Frame | azione speciale **X-Frame Change** | otto versi copiati da `action.hsp`: devono uscire identici a quelli di là |
| il plagio | fatti plagiare da un nemico con Carisma alta | `:18280` dice «si toglie l'equipaggiamento, obbedendo all'ordine» e il soggetto dev'essere **il giocatore** |

💡 **E le 146 nuove sono le più facili da collaudare di tutto il progetto**,
perché sono il **log di combattimento**: basta un combattimento qualsiasi con
un'azione speciale. Da guardare in quest'ordine:

| cosa | come | perché |
|---|---|---|
| ⚠️ **il pozzo e la fontana** | cammina finché non ti viene sete, poi `h` su un pozzo | è la toppa della 36ª **mai riguardata**: atteso «`Il pozzo disseta il viandante.`» |
| le mosse di barra | un'azione speciale qualsiasi con la barra piena | 20 rese del lotto 015, una per arma. Le tre parate («X attacca, ma Y para») sono la forma nuova |
| le decapitazioni | azione speciale Decapitazione | `facendone saltare la testa` e `decapita`: è dove il genitivo è stato girato |
| i cinque malanni | fatti colpire da veleno, cecità, confusione, paralisi, sonno | 11 rese dove il participio è stato rovesciato: «Il veleno investe X» |
| i terreni | lancia Ragnatela, Muro di fuoco, Nebbia di tenebra | 7 statiche, si vedono subito |
| il potenziale | bevi una pozione del potenziale | «vede crescere il potenziale di Forza» |
| ⚠️ `:11749` | prega il tuo dio | **dirà «di Lulwy of Wind»**, ed è la dipendenza nota da `god.hsp`, non un difetto |

⚠️⚠️ **Il debito di collaudo, che la 36ª ha aggredito e la 37ª ha raddoppiato.**
Delle 235 rese della 35ª ne è stata guardata **una parte** — le teste del log, la
sazietà, la maiuscola — e sono arrivate le **121 rese nuove** dei tre lotti, mai
viste. Se una sessione può fare una cosa sola, faccia il collaudo: vale dalla 32ª
e la 36ª è la prova più forte che sia vero, perché in un'ora di prove ha trovato
due difetti strutturali che otto sessioni di catena verde non avevano visto.

💡 **La roba nuova è facile da vedere**, sta tutta in quel che si fa giocando:
bere alcolici (le due liste di ubriacatura, `:10274` e `:10280`), le pozioni
maledette (le tre sventure in scala — tormento, sventura, flagello), pescare,
salire e scendere da una cavalcatura, benedire l'equipaggiamento.

Da guardare, in ordine di rischio:

0. ⚠️ **Le due toppe della 36ª** — il pozzo (**mai visto**) e la maiuscola
   d'ufficio (✅ vista). Poi le **121 rese** dei lotti `011`-`013`.

1. ✅ **La scena ricucita: guardata il 2026-08-14, e aveva un difetto.** I tre
   pezzi si agganciavano e le virgolette chiudevano, ma a schermo usciva
   «`"Che bello ! Questo e' tutto quello che ho nel portafogli.`» — **uno spazio
   prima del punto esclamativo**. Lo mette `init.hsp:1666`, che nel **solo ramo
   inglese** accoda uno spazio a ogni `txt`; il ramo giapponese no. Per questo
   upstream punteggia la **testa** e fa ripartire la coda con la maiuscola,
   mentre il giapponese fa l'opposto — e noi avevamo copiato il giapponese.
   ✅ Corretto (tre toppe, due voci di dizionario), ricompilato e **riguardato lo
   stesso giorno**: esce «`"I-incredibile! Questo e' tutto quello che ho nel
   portafogli."`». Il dettaglio sta in `decisioni.md`.
   ⚠️ **Resta lo spazio prima della virgoletta di chiusura** («`"Che bello! `»),
   dove la coda è il solo `txt lang("」", "\"")`: ce l'ha anche l'inglese di
   monte, non è nostro.
   ⚠️ **E la regola vale oltre questa scena**: ogni resa che continua un `txt`
   precedente e comincia per punteggiatura mostrerà lo spazio.
   ⚠️⚠️ **La seconda metà di questa frase era falsa, e la 36ª l'ha corretta a
   schermo.** Diceva che «ogni resa che comincia per minuscola verrà maiuscolata
   d'ufficio (`init.hsp:1659-1661`)». **Con l'orologio del log acceso non
   succede mai**: il prefisso `"[H:MM] "` si attacca a `msgtemp` alla riga
   **1578**, cioè 81 righe prima del controllo, e `peek(msgtemp, 0)` legge `[`
   (91), fuori da 97-122. A schermo si leggeva «`[19:07] il viandante finisce di
   mangiare una razione.`». ✅ **Toppato nella 36ª** maiuscolando subito dopo
   `tnew = 0` (`init.hsp:1568`), prima che i prefissi si attacchino. Vedi
   `decisioni.md`, «La maiuscola d'ufficio non gira».
   **La misura su tutto il dizionario non è stata fatta**: è materiale da
   guardia.
2. ✅ **I 63 `buffdesc`**: guardati il 14/08 in tutti e **quattro** i siti —
   scheda del personaggio (`command.hsp:10800`), schermata di analisi
   (`:2005`, che apre l'azione speciale **«Specchio»**), menu abilità (`:5389`,
   taglia a 34) e menu di lancio (`:8851`, taglia a **40**). Chiuso: la
   troncatura è di monte, l'italiano ne sfonda meno dell'inglese.
3. **Le 23 toppe sui blocchi `if ( en )`**: ✅ **7 viste nella 34ª** — le sei
   della scena (`3319`, `3372`, `3487`, `3533`, `3574`, `3617`) e la prima
   dell'equitazione (`10847`, «`Vacci piano, mi raccomando♪`», la cavalcatura che
   parla mentre le sali sopra). **Ne restano 16**, e i triggeri sono tutti noti:

   | come | toppe | nome italiano dell'azione |
   |---|---|---|
   | `a` → azione speciale su un alleato adiacente | 3 | **Equitazione** (20 Sp) — ⚠️ si impara **solo** a Yowyn, Palmia, Eirel, Melkawn (`command.hsp:9040`); il maestro di Yowyn è a **(20, 14)** e si chiama «*… della gilda*»; `spawn_item 1093` è il biglietto abilità che evita il platino |
   | `a` → su un nemico | 3 | **Inferno del solletico** |
   | `a` → su un PNG | 2 | **Ammaliamento** |
   | `a` → su un nemico | 1 | **Sguardo di follia** |
   | `a` → su un alleato con la barra di rottura guardia > 0 | 1 | **Istruzione individuale** |
   | `D` su un muro · raccolta in un campo | 2 | — |
   | viaggio su neve o sabbia · sotto pioggia forte | 3 | — |
   | ⚠️ **Ordini tattici** rifiutato, su un alleato **che ha partorito**, 1 volta su 2 | 1 | condizione troppo stretta: **non cercarla apposta** |

   💡 **Sei di queste si fanno da fermo**, con un alleato e un nemico a portata:
   solletico, ammaliamento, sguardo di follia. Non serve andare da nessuna parte.
4. Le liste arretrate 27ª-30ª e le 169 battute degli dèi.

⭐ **`buff.hsp` è chiuso.** La 33ª ha fatto i **63 `buffdesc`** in un lotto solo,
`fase2-buffdesc-001`: il file passa da 63 non tradotte a **0**, ed è il primo
file di Fase 4 chiuso per intero. Catena verde, compilatore muto, `cgx-test.exe`
rifatto. ⚠️ **Ma non è ancora stato guardato a schermo**: vedi «Il debito di
collaudo» più sotto — è la prima cosa che deve provare la 34ª, e i tre siti
dove esce sono la lista abilità (`command.hsp:5389`), la schermata di analisi
(`:2005`) e la scheda del personaggio (`:10800`).

💡 **La scoperta della 33ª è che per una riga che descrive un effetto l'arbitro
non è una lingua, è il codice.** Tre `buffdesc` su 63 avevano giapponese e
inglese che dicevano cose diverse, e il blocco sotto la riga ha chiuso la
domanda in dieci righe di lettura: a `656` l'inglese sbaglia **due volte** (dice
«10%» dove non c'è e `RES+ confusion` dove il codice alza la resistenza alla
**magia**); a `1195` perde il `軽装備+20%`; a `1315` — ed è il caso che rovescia
la regola — **l'inglese è più preciso del giapponese** e il codice gli dà
ragione, ma il giapponese porta la barra che l'inglese ha perso, **e le due metà
si sommano invece di scegliersi**. Il dettaglio sta in `decisioni.md`.

⚠️ **E la domanda della 29ª va posta con una misura di somiglianza, non per
stringa esatta.** Sui 63 `buffdesc` il confronto esatto trovava **1** gemello e
avrebbe chiuso la domanda con un no; `difflib` a 0,55 sul giapponese ne ha
trovati **14**, e tre sono state copiate perché dicono la stessa cosa di
`skill.hsp` con altre parole. Lo script sta in `scratchpad/simili.py`.

⭐ **La 32ª è stata una sessione di sole prove in gioco**, la prima da molto, e
ha reso più di quanto costasse: **due tetti che nessuno aveva mai misurato**,
tutti e due sfondati, **33 rese corrette**, e la spiegazione di perché le liste
di collaudo non tornano mai. Il dettaglio sta in `decisioni.md`, in tre voci
datate 13/08. In breve:

1. ⚠️ **Le piastrelle degli stati nell'HUD tagliano** — a schermo si leggeva
   «Marchio letal». Il carattere della build inglese è `Courier New`, cioè
   **monospaziato**: 11 caratteri sulla piastrella da 80 px, 13 su quella da
   95. Sfondavano **19 etichette su 61**, e l'inglese di upstream ne sfonda 2.
   ✅ **Corretto e riverificato a schermo lo stesso giorno**: l'etichetta esce
   intera, con «Stanchezza» e «Fardello!» comode nella loro piastrella. La
   prova sta in fondo al ciclo giusto — difetto visto, misurato sul sorgente,
   corretto nel dizionario, ricompilato, riguardato.
   ⚠️ **E la riguardata ha prodotto una correzione della correzione**: il primo
   accorciamento era «Marchio», che sta nel tetto ma perde il 死 del 刻死紋.
   Adesso è **«Segno letale»**, e il gemello «Veleno!» è diventato **«Gran
   veleno»**. Vedi `decisioni.md`, «Accorciare puo' togliere il significato».
2. ⚠️ **Le colonne del menu tattiche del mod si sovrappongono** — la domanda
   aperta dalla 29ª si chiude sull'ipotesi peggiore: `cs_list` **non taglia**,
   sconfina sulla colonna accanto. 20 caratteri il tetto, **10 `buffname` su
   71** lo passavano, **0 inglesi**.
3. ⚠️ **Undici creature su ventisette sono mute se aspetti**: non hanno
   `DBMODE_FLAVOR_PASSIVE`, e il metodo «`add_ally` e tieni premuto `5`» per
   loro non produce niente. Vedi «Il collaudo, punto per punto», riscritto per
   classe di battuta.

💡 **E il collaudo ha dato la prova sul campo dell'ordine già deciso.** Il log
di un combattimento qualsiasi è pieno di inglese — «is drawn», «was knocked
down», «stands up», «aims at nearby enemies», «teleports toward», «crushes with
hip!» — e **viene tutto da `proc.hsp`**. Non lo si trovava col grep perché le
frasi sono spezzate dall'helper morfologico: nel sorgente c'è
`" aim" + _s(cc) + " at nearby enemies."`, non la frase intera. È il file che
il giocatore legge a **ogni singolo combattimento**, ed è il numero 2 della coda.

✅ **E i due tetti nuovi hanno la loro guardia**, scritta nella stessa sessione:
**`strumenti/riquadri.py`**, più 18 test. Sta nelle verifiche d'apertura. 💡 Due
cose le ha trovate il test, non l'occhio: la prima versione prendeva la
`gcopy` «entro sei righe sopra», e un'etichetta senza piastrella si sarebbe
presa in silenzio quella dell'etichetta precedente; e leggeva il passo della
colonna dalla **prima** `cs_list` del file, che è un altro menu con un passo di
150 — verdetto giusto per sbaglio, perché 150 / 7,2 fa comunque 20.

⭐ **`db_creature.hsp` è chiuso.** La 31ª ha fatto sei lotti, dal `037` al `042`:
**315 rese**, 51 creature, catena verde a ogni lotto. Le battute sono passate da
**316 a 0** e le creature da fare da 51 a **0**. Il file era a 1.563 da fare
all'apertura della 27ª.

Restano **quattro** voci non tradotte in quel file, e sono le quattro **rinviate
apposta**: le righe commentate nel sorgente, registrate in `rinviate.jsonl` col
motivo. Più `86293`, la battuta col ramo inglese vuoto, che `estrai.py` non vede
nemmeno. Nient'altro.

⚠️ **Resta valida la domanda della 29ª all'apertura di ogni file nuovo**: *questo
file nomina cose che un altro file ha già nominato?* La riga di comando che
risponde sta in `decisioni.md`. E resta la **ricerca dei participi** di
`decisioni.md`, da rilanciare a ogni lotto: nella 31ª ha dato **0** ogni volta,
su tutto il dizionario, il che vuol dire che le sei correzioni della 30ª hanno
tenuto e che nessuna delle 315 rese nuove ne ha introdotte.

✅ **E i `bufftxt` di `buff.hsp` sono chiusi**, sempre il 13/08: la toppa
strutturale su `chara_func.hsp` più le 65 rese che coprono i 71 messaggi. Vedi
«Le due toppe di `buff.hsp`» più sotto. `buff.hsp` passa da 128 non tradotte a
**63**, e le 63 sono tutte `buffdesc`.

**Il lavoro che riparte, in ordine:**

0. ✅ **La guardia sui due tetti nuovi**: fatta nella 32ª, `strumenti/riquadri.py`.
1. ✅ **I 63 `buffdesc`**: fatti nella 33ª, `buff.hsp` è chiuso.
   ✅ **Guardati a schermo il 2026-08-14 e la questione è chiusa**, in tutti e
   quattro i siti: scheda del personaggio (`Accelerazione: 7(13) Velocita' +60`,
   intero), schermata di analisi (intero), menu abilità e menu di lancio.
   ⚠️ **E i siti erano quattro, non tre, con tre tetti diversi** — la ripresa ne
   registrava uno solo:

   | sito | routine | taglio |
   |---|---|---|
   | menu `a` | `*com_applySkill_loop` | 34 |
   | menu `W` | `*com_applyWideSkill_loop` | 34 |
   | menu di lancio | `*com_spell_loop` | **40** |
   | scheda, pagina incantesimi | `*com_charainfo_loop_WHILE1` | **46** |

   💡 **Il conto della 33ª — «46 inglesi su 63 sfondano già» — valeva solo per il
   34**, e delle 21 abilità che mostrano un `buffdesc` **solo 4 sono azioni
   speciali**: le altre 17 sono incantesimi e cadono nei tetti da 40 e 46.
   Rimisurato per tetto con `scratchpad/tetti_buffdesc.py`:

   | tetto | italiano sfonda | inglese sfonda |
   |---|---|---|
   | 34 | 43 su 62 | **46** su 62 |
   | 40 | 32 su 62 | **38** su 62 |
   | 46 | 23 su 62 | **31** su 62 |

   ✅ **L'italiano sfonda meno dell'inglese a tutti e tre**, quindi la troncatura
   è comportamento di monte e **non c'è niente da accorciare**. A schermo si
   vedono `Res+ gra`, `Res+ sonno,confu`, `oltretomb` — sembrano refusi e non lo
   sono: le stesse righe inglesi si tagliano nello stesso modo, perché elencano
   dieci resistenze in tutte e due le lingue. ⚠️ Accorciarle peggiorerebbe i siti
   dove la riga ci sta comoda.
   ⚠️ Cautela sul numero: lo strumento stima a due cifre le variabili
   interpolate, quindi c'è un margine di ±1 carattere per voce. Il metodo è lo
   stesso sulle due lingue, quindi il **confronto** regge; i valori assoluti no.
2. **`proc.hsp`**, a **838 su 1.098 (76%)**, per zona di riga **dalla riga 20000**
   in avanti. Restano **260** non tradotte, di cui 6 rinviate: **254 da fare**.

   💡 **Dove si addensa quel che resta** (`scratchpad/istogramma.py`, passo 1000,
   rifatto a fine 38ª sulle 254): `22000-22999` **59**, `21000-21999` **55**,
   `23000-23999` **42**, `26000-26999` **34**, `25000-25999` **30**,
   `20000-20999` **20**, `24000-24999` **14**. ⭐ **Non c'è più niente prima della
   20000**: da qui in avanti l'ordine di riga e l'ordine di densità coincidono
   quasi, e `21000-23000` da solo vale **156 voci**, il **61%** di quel che resta.
   Due lotti grossi, o tre normali, e il file è chiuso.

   ⚠️ **Prima di riprendere, copiare le quattordici reti** da
   **`scratchpad/lotto-fase4-proc-019.py`**, che è il modello più recente. ⚠️ Le
   reti 3, 4 e 8 sono state **corrette perché sbagliavano loro**, e la 12 e la 13
   sono nuove: si copia il file, non si riscrive a memoria. 💡 Il modo che ha
   funzionato tre volte di fila nella 38ª: si estrae il blocco che comincia con
   `# rete 5: l'accento` e lo si incolla dopo le rese, poi si **verifica** con un
   `diff` che sia identico al modello meno `USCITA` e `DA, A`.

   La 33ª ha fatto i lotti `fase4-proc-001` … `-004` (1716-3400: le reazioni
   degli dèi, le tattiche, bugia/minaccia/canto/pasto). **La 35ª ha fatto i sei
   lotti `-005` … `-010`, cioè tutto il 3401-9200**, e ⭐ **la 36ª i tre lotti
   `-011` … `-013`, cioè 9201-11499:**

   | lotto | zona | che cosa |
   |---|---|---|
   | `-005` | 3401-4200 | le attività continuate, le due trappole, il furto |
   | `-006` | 4201-5000 | il sonno, il risveglio, il riposo, il viaggio |
   | `-007` | 5001-5900 | pesca, scavo, miniera, i pasti |
   | `-008` | 5901-6800 | la sazietà, la lettura, l'abisso, i lanci falliti |
   | `-009` | 6801-7700 | bere, i pozzi, le pergamene, le bacchette |
   | `-010` | 7701-9200 | il log di combattimento: proiettili, cure, morsi |
   | `-011` | 9201-10100 | azioni speciali, borseggio, soffio, mappe del tesoro |
   | `-012` | 10101-10600 | pozioni, latte, ubriacature, oli, acido |
   | `-013` | 10601-11499 | bibite, sale, equitazione, pesca, mutazioni |
   | `-014` | 11500-12500 | pergamene, potenziale, dèi, decapitazioni |
   | `-015` | 12501-14499 | il log delle azioni speciali, arma per arma |
   | `-016` | 14500-15499 | fuga e ritorno, veleni, maledizioni, terreni, artefatti |

   💡 **Dove si addensa quel che resta** (`scratchpad/istogramma.py`, passo 500,
   rifatto a fine 36ª sulle 535 rimaste): `11500-11999` **28**, `14500-14999`
   **30**, `12000-12499` **23**, `15500-15999` **24**. Non c'è più un picco come
   il `10000-12000` di prima: da qui in avanti è terreno piatto, e la zona
   successiva — `11500-12500` — vale una cinquantina di voci.

   ⚠️ **Prima di riprendere, rileggere le undici reti** dello script di lotto: il
   modello più completo è **`scratchpad/lotto-fase4-proc-013.py`**, che le ha
   tutte. Le cinque della 35ª (5-9) e le due della 36ª (10 e 11) sono nate ognuna
   da un caso reale, non da un'idea. ⚠️ **La rete 11 è quella che vale di più e
   anche quella che è nata sbagliata due volte** — troppo severa sulle statiche,
   poi giusta e decisiva su `his2` — quindi si copia, non si riscrive;
   ✅ **La toppa sui blocchi `if ( en )` è fatta**: 23 righe di questo file
   avevano letterali inglesi **nudi** fuori da `lang()`, invisibili
   all'estrattore. `toppe.jsonl` passa da 273 a **296** ed erano zero su
   `proc.hsp`. Vedi `decisioni.md`, «Ventitré righe di `proc.hsp` parlano inglese
   fuori da `lang()`».
   ✅ **E la misura è stata fatta su tutto il sorgente**: **99 righe** così in 14
   file, di cui **68 ancora intatte** — `event.hsp` 27, `screen.hsp` 14,
   `command.hsp` 10, `system.hsp` 4, `material.hsp`/`item_func.hsp`/`main.hsp` 3
   ciascuno. 💡 Il grosso viaggia con file non ancora tradotti, quindi non ha
   fretta. ⚠️ **Ma circa metà delle righe dei file piccoli non è testo** —
   entità HTML, operandi di confronto, chiavi di dati — quindi il numero è un
   punto di partenza, non un elenco di lavoro;
3. `command.hsp` e `trait.hsp`, che sono ~1.680 firme mai toccate. ⚠️
   `command.hsp` è anche il file che **disegna** i `buffdesc` appena fatti.

⭐ **`chips.hsp` è chiuso**, trovato e fatto a schermo il 14/08. Ha **tre**
`lang()` in tutto — i nomi delle caselle di terreno — e uscivano da
`action.hsp:2681` dentro una frase **già tradotta**, quindi a schermo si leggeva
«`a field si trova ai tuoi piedi.`»: metà inglese e metà italiana, a ogni passo
mentre si coltiva. È la lezione di `adv.hsp` della 26ª (**la frequenza, non
l'elenco**), stavolta su un file che l'elenco copre ma che nessuno aveva ragione
di aprire.

| riga | giapponese | resa | perché |
|---|---|---|---|
| 833 | 日干し岩 | `una pietra da essiccazione` | al ranch, col bel tempo, quel che ci lasci sopra si secca e un cadavere diventa carne secca (`item.hsp:1819-1835`); «essiccazione» tiene la famiglia di `pesce essiccato` |
| 834 | 畑の土 | `un campo coltivato` | **copiata** da `action.hsp`, «Si concima solo il campo coltivato.» |
| 835 | コンポスト | `del compost` | **copiata** da `action.hsp`, «Il compost funziona solo nei campi di tua proprietà.» Partitivo: è un mucchio, non un oggetto numerabile |

💡 **Due rese su tre sono copie**: la regola «cercare prima di scrivere» ha reso
due volte su tre in un lotto da tre voci. ⚠️ E ogni resa porta **il proprio
articolo**, perché lo porta l'inglese (`a field`) e la frase che le ospita non ne
mette.
✅ **E ha dato la prova più forte finora sulla scoperta 2 della 28ª.**
`sdim tname, 16` dà 16 byte a voce; «una pietra da essiccazione» ne occupa **26**
e «un campo coltivato» **18**. Guardato a schermo il 14/08: la frase esce
**intera**. Fin qui la controprova migliore era `sdim buffname, 20` col
giapponese di monte da 22 byte, cioè un +10% scritto **da upstream**; questa è un
**+62% scritto da noi**, su una stringa che il giocatore legge a ogni passo.
`sdim` non è un tetto in scrittura, e adesso lo si sa con un margine largo.

💡 **Il debito di collaudo è stato aggredito nella 32ª, non estinto, e la 33ª
l'ha aumentato.** Provati nella 32ª: i messaggi dei potenziamenti (la toppa
strutturale, mai vista prima), il menu tattiche, le etichette di stato
dell'HUD, `<Aribel>`, e un combattimento coi due Yerleswood. **Restano da
guardare** le liste 27ª-30ª, le 169 battute degli dèi e — nuovi — i **63
`buffdesc`** della 33ª, che nessuno ha ancora visto a schermo. ⚠️ Ma adesso si
sa **come** guardarle: per classe di battuta, non mettendosi ad aspettare.

💡 **I `buffdesc` si guardano senza aspettare niente**: basta avere un
potenziamento addosso e aprire la scheda del personaggio (`command.hsp:10800`,
non taglia e manda a capo), la schermata di analisi (`:2005`, non taglia) e la
**lista abilità** (`:5389`, che taglia a 34 e va guardata per ultima, perché è
lì che si vede quanto la troncatura di upstream costa in italiano).

⚠️ **I nomi di creatura sono chiusi**: l'ultimo che i conteggi mostravano da
fare era su una riga commentata. Vedi «Le righe commentate» più sotto.

### Le otto verifiche d'apertura

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 412 passed, 6 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 2466, doppie 0, senza razza 0
python -m strumenti.larghezze              # atteso: 0 fuori misura su 75 menu
python -m strumenti.diario                 # atteso: 0 fuori misura su 214 siti
python -m strumenti.riquadri               # atteso: 0 su 38 piastrelle, 0 su 71 buffname
python -m strumenti.battute --divergenti   # atteso: 13, tutte legittime
```

💡 **`riquadri.py` è nato nella 32ª**, il giorno stesso in cui i due tetti che
misura sono stati scoperti sfondati. Copre le piastrelle degli stati nell'HUD e
la colonna del menu tattiche, che `larghezze.py` non vede perché non passano da
`*prompt_key`.

⚠️ **I quattro test in più che saltano sono la chiusura di `db_creature.hsp`**,
non un guasto. Leggono `lavoro/_c.jsonl` e provano proprietà dell'**ordinamento
di un elenco**: su un elenco vuoto tre di loro morivano — `max()` di niente, una
divisione per zero, due ordini vuoti che «coincidono». Il 13/08 sono diventati
rossi tutti insieme per la prima volta, e nessuno dei tre aveva trovato un
difetto. Adesso `estrazione_da_fare()` salta anche sul file **vuoto**, oltre che
sul file assente. 💡 Provato che il guardiano non li ha spenti: con
un'estrazione piena (`estrai` senza `--da-tradurre`) tornano a girare e passano.

💡 **E i referti, che non sono guardie e vanno letti**, adesso tutti in
`scratchpad/` (vedi `scratchpad/LEGGIMI.md`):

```powershell
$env:PYTHONPATH = $repo
python scratchpad/referti.py              # participi col giocatore: 0 | elisioni: 0
python scratchpad/blocchi_en.py           # struttura 99 | ancora da fare 68
python scratchpad/else_jp.py              # else-di-jp: 6.984 righe in 13 file
python scratchpad/rete8_dizionario.py     # 3, tutti dichiarati falsi positivi
python scratchpad/misura-blocchi-spenti.py  # 7 voci dentro un blocco spento
python scratchpad/variabili_en.py         # 66 variabili | 3 trappole in 3 siti
python scratchpad/perimetro.py            # perimetro 47% | col fuori perimetro 35%
```

⚠️ **I due ultimi sono della 38ª.** `variabili_en.py` è il **terzo punto cieco**
dopo `blocchi_en.py` e `else_jp.py`: le variabili che si portano dentro un
letterale inglese e finiscono dentro una `lang()`. **Se sale a 4, qualcuno ne ha
creata una nuova; se scende a 2, `economy.hsp:319` è stato risolto.**
`perimetro.py` è il conto vero di quanto manca, descrizioni degli oggetti e file
di `data/` compresi: **non si deduce sommando `verifica --dizionario`**, che
misura solo il perimetro `lang()`.

⚠️ **I due ultimi sono della 37ª.** `rete8_dizionario.py` è la rete 8 passata
all'indietro su tutto il dizionario: **se sale a 4, qualcuno ha scritto un
genitivo davanti a un nome**. `misura-blocchi-spenti.py` conta le voci tradotte
dentro un `/* ... */`: se sale, un lotto ha tradotto testo morto. Tutt'e due
leggono il **`SORGENTE`**, non la build — vedi la nota in cima sulla riga in più
di `text.hsp`.

⚠️ **`else_jp.py` è nato nella 34ª ed è il punto cieco di `blocchi_en.py`.** Gli
stessi letterali inglesi nudi, ma scritti `if ( jp ) { … } else { … }` invece che
`if ( en ) { … }`: il fratello non li vede, e nessun conteggio di «non tradotte»
li include. Trovato perché la follia di `calculation.hsp:2352` — `"Forgive me!
Forgive me!"`, `"P-P-Pika!"`, `"You snail!"` — è uscita **in inglese a schermo**
durante il collaudo. Delle 6.984 righe, **6.840 sono le descrizioni di
`db_item.hsp`** già dichiarate fuori perimetro: le vive sono **144**, e le
interessanti sono `proc.hsp` 13, `ai.hsp` 3, `calculation.hsp` 2, `chat.hsp` 2.
💡 `item_func.hsp` ne ha 30 con **0 intatte**: quella famiglia era già stata
toppata a mano, un caso per volta, senza che nessuno sapesse che era una
famiglia.

⚠️ **E qui la 34ª ha scritto una cosa falsa e l'ha corretta un'ora dopo**: che
`calculation.hsp` «non stesse in nessun elenco di fase» e «non avesse firme». Ha
**44 `lang()`**, e `SPEC.md` §6 mette in Fase 4 «i restanti **63 file** `.hsp`
minori», che è una designazione **collettiva**: copre ogni file non nominato
prima. Non è `adv.hsp` della 26ª — è coda non ancora cominciata.
✅ **La domanda della 26ª è chiusa con una misura**, non con una lettura:
`scratchpad/fuori_elenco.py` dice che dei **54** file con `lang()` ne hanno un
dizionario **14**, e i **40** restanti valgono **12.620** stringhe mai estratte.
Nessun file è fuori elenco; l'elenco è solo collettivo.

`referti.py` fa la nona e la decima verifica — i participi che concordano col
giocatore e le elisioni davanti a consonante. Attese **0** tutt'e due: adesso che
sono a zero, un valore diverso significa qualcosa.

⚠️ `blocchi_en.py` è **un referto, non una guardia**, e per due motivi: circa
metà delle righe dei file piccoli non è testo (entità HTML, operandi di
confronto, chiavi di dati), e il numero **cala solo quando si fa una toppa**, non
quando si traduce. Non deve tornare a 92: se lo fa, qualcuno ha ricreato
l'albero di build senza applicare le toppe.

Se `--divergenti` sale, qualcuno ha reso due volte in modo diverso la stessa
frase giapponese. Le due nuove della 27ª sono volute: 「きゅう…」 («*sbuffo*»
altrove, «Quu...» sulla forma di vita quantistica, dove l'inglese fa il gioco
di parole con Q) e 「わん！」 («*bau!*» dove l'inglese descrive un'azione,
«Bau!» dove passa da `cnvtalk`, che mette le virgolette).

⚠️ **Le due della 30ª (da 11 a 13) sono la stessa resa in due involucri diversi**:
la sorella minore chiama il giocatore con `_onii` in due punti, e upstream avvolge
un sito in `cnvtalk(...)` e l'altro in virgolette nude `"\"" + ... + "\""`. Il
testo che il giocatore legge è identico; a differire è il codice HSP intorno. È la
stessa classe di 「お、カモだ…」, che stava già fra le undici.

⚠️ **Ma `--divergenti` guarda solo `db_creature.hsp`** — misurato nella 29ª,
`rese_gia_decise()` apre quel file e basta. Una divergenza introdotta in
qualunque altro file **non alza quel numero**. Non fidarsi dell'11 come se
coprisse il dizionario intero: vedi `decisioni.md`, «Un buff è l'incantesimo che
lo concede».

💡 Vale anche il manifesto del sorgente, che nessuno strumento controlla:

```powershell
$base="C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx"
Get-Content "C:\Games\Elona\_traduzione\manifesto-sorgente.txt" | ForEach-Object {
  $p=$_ -split '\s+',2
  if ((Get-FileHash "$base\$($p[1].Trim())" -Algorithm SHA256).Hash -ne $p[0]) { $p[1] } }
```
Nessun output = 72/72. ✅ Ricontrollato a fine 33ª: nessuna differenza. Il
sorgente pinnato non è mai stato scritto, nemmeno dalle 24 toppe — le toppe sono
**dati applicati all'albero di build**, e `compila.py` rifiuta per costruzione di
scrivere dentro `SORGENTE`.

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.606 | 1.606 | **100%** |
| `item_data.hsp` | 318 | 318 | **100%** |
| `skill.hsp` | 885 | 885 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `adv.hsp` | 12 | 12 | **100%** ⭐ chiuso il 2026-08-11 |
| `action.hsp` | 1.286 | 1.288 | **100%** (le 2 mancanti sono rinviate a toppa). ⚠️ Aveva **una riga inglese** che nessun conteggio vedeva, `:15221`, fuori da `lang()`: toppata il 2026-08-13 |
| `text.hsp` | 1.718 | 1.720 | **100%** (le 2 mancanti aspettano `talk.txt`) |
| `proc.hsp` | **838** | 1.098 | **76%** ⭐ +129 nella 38ª (era 709) — più 23 righe fuori da `lang()`, ✅ toppate, e **6 rinviate**: una riga commentata, «Party Room», i due nomi di nave, `:11481` (`his2()`, ✅ toppata nella 36ª) e `:11796` (dentro un blocco `/* ... */` spento) |
| `buff.hsp` | 199 | 199 | **100%** ⭐ chiuso il 2026-08-13 — `buffname`, `bufftxt` e `buffdesc` |
| `command.hsp`, `trait.hsp` | 0 | ~1.680 | 0% |

`db_creature.hsp`: **1.131 nomi** + **2.519 battute rese**, **0 da fare**. ⭐
**Chiuso il 2026-08-13**, a parte le quattro righe commentate rinviate apposta.
Era a 1.563 da fare all'apertura della 27ª. I lotti `015`-`026` coprono i livelli
**6-45** — le creature di città, i PNG di trama e i primi sotterranei — i dieci
lotti `027`-`036` della 30ª i livelli **45-157**, cioè i PNG delle gilde, i boss
di trama e i mostri di Nefia profonda, e i sei lotti `037`-`042` della 31ª tutto
il resto: **159-1200**, cioè i demoni, gli dèi del Patto Eterno, gli otto dèi di
Elona e le loro forme potenziate.

⚠️ I conti per classe si rifanno così, e non si deducono: le classi si leggono
dal `dbmode` che precede la riga nel sorgente, incrociando `dizionario/` per le
rese e `lavoro/_c.jsonl` per quelle da fare. Rifatti il 13/08 a fine 31ª:
`2.519 voce + 1.131 nome + 1 senza classe + 4 rinviate = 3.655`, che è il totale
delle firme del file. 💡 **Dedurli sbagliava**: la ripresa portava «2.199
battute rese» e sommandoci i lotti veniva 2.515, quattro in meno del vero.

Altri fuori Fase 1: `custom_enemyevolution.hsp` **chiuso**; `chips.hsp`
**chiuso** ⭐ 2026-08-14 (3 su 3); `ai.hsp` 6 su 100; `event.hsp` 5 su 654;
`chara_func.hsp` 45 su 331; `init.hsp` 6 su 133.

⚠️ **E il quadro d'insieme, misurato il 14/08 con `scratchpad/fuori_elenco.py`**:
dei **54** file con `lang()` ne hanno un dizionario **14**; i **40** restanti
valgono **12.620 stringhe mai estratte**. Non sono file dimenticati — sono la
Fase 4, che `SPEC.md` §6 definisce collettivamente («i restanti 63 file `.hsp`
minori»). Il numero serve a tenere le proporzioni: quello che resta è più grande
di quello che è stato fatto.

**412 test più 6 saltati**, prova d'identità **72/72 e 27.813**, **13.925
sostituzioni** applicate alla build — erano **13.786** all'apertura della 38ª,
più le **139** dei tre lotti. **`toppe.jsonl` è fermo a 302** (né la 37ª né la
38ª ne hanno fatte: i loro difetti erano nel dizionario, non nel sorgente), e
`proc.hsp` ne porta **27**. **`rinviate.jsonl` è a 14** (`proc.hsp` 6,
`db_creature.hsp` 4, `action.hsp` 2, `text.hsp` 2). Il compilatore non dice
nulla, manifesto del sorgente **72/72** (ricontrollato il 14/08 a inizio 38ª).

💡 **Le sostituzioni crescono più delle rese anche stavolta**: 129 rese hanno
prodotto **139 siti**. Una firma esce in più punti, e il caso più netto della 38ª
è `:16087`, che ne copre **due** senza che il secondo compaia nell'estrazione.

💡 **Le sostituzioni crescono più delle rese, ed è il motivo per cui vale la pena
contarle**: 235 rese hanno prodotto 298 siti, perché una firma può uscire in più
punti. Nella 35ª il record è «`name(tc)` si indebolisce», **otto siti** con una
resa sola, e «Il tuo diario è stato aggiornato.» ne copre **sei**. Il conto per
lotto si rifà così, e non si deduce:

```powershell
& $py -c "import io,json,collections; ..."   # vedi i commit dei lotti 005-010
``` ✅ Tutta la batteria
rilanciata a fine 33ª dopo le **165 rese nuove**: **identica in ogni valore**,
niente si è mosso, e `verifica --dizionario` dà `buff.hsp: 0 da ritradurre, 0 non
ancora tradotte`. ✅ E stavolta l'eseguibile è **davvero** quello nuovo: vedi i
due passi che il metodo non nominava.

## Le due toppe di `buff.hsp`, e perché ce ne volevano due

### 1. La toppa strutturale: 63 righe diventano una

Il ramo giapponese (`chara_func.hsp:2377`) compone il messaggio «X comincia
a...» con un **frammento unico**, `name(id) + bufftxt(0, id)`. Il ramo inglese
(`:2316-2375`) ne compone quattro — `name + bufftxt(0) + _s(id) + bufftxt(1)` —
più **sette casi speciali** con `his(id)`. Nessuna delle due conseguenze si
risolve traducendo: `bufftxt(1)` è un letterale nudo **fuori** da `lang()` in
tutte e 71 le righe, e `_s()`/`his()` sono morfologia inglese che le regole
vietano.

La toppa riporta il ramo inglese alla forma giapponese. ✅ **Tolto anche
`cnven()`**, che il ramo inglese applicava **al solo giocatore**: il resto della
build non capitalizza il nome a inizio messaggio (`chara_func.hsp:6846`,
«`name(id) + " perde la vita."`»), e tenerlo qui darebbe la maiuscola al
giocatore e non alle creature, dentro lo stesso messaggio.

💡 **La domanda della ripresa aveva risposta netta**: dei 71 `bufftxt`, **0**
erano già resi altrove. Non c'era riuso da raccogliere.

### 2. ⚠️ La toppa che non era nel piano: `sdim` non basta più

`sdim bufftxt, 30, 2, MAX_BUFF` dà 30 byte per elemento, e **il numero non è
casuale**: il giapponese più lungo ne occupa 28. L'inglese ci sta comodo perché
in `bufftxt(0)` mette solo il verbo. Dopo la toppa l'italiano porta la frase
intera e il più lungo ne occupa **59**, e accorciare non è una via d'uscita:
qualunque italiano che porti la frase intera passa i 30 byte.

💡 **La 28ª aveva ragione — `sdim` non è un tetto — e la controprova migliore
sta nel gioco**, meglio di `skilldesc`: `sdim buffname, 20, MAX_BUFF` e il
buffname **giapponese** più lungo ne occupa **22**. Upstream scrive già oltre il
dichiarato, e funziona.

⚠️ **Ma quella prova vale per un array a UNA dimensione.** `bufftxt` ne ha due,
e per il caso a due dimensioni **non c'è nessuna controprova nel gioco**, perché
né il giapponese né l'inglese ci arrivano mai. Il buffer è stato allargato a
128: costa `2 * MAX_BUFF * 98` byte e toglie la domanda invece di scommetterci.

💡 **Il vincolo delle rese è più stretto del solito**, e vale per il prossimo
che ci mette mano: il soggetto è `name(addbuff_charid)`, che può essere
**qualunque creatura** — «il cane», «la strega» — oltre al giocatore. Niente
participio e niente aggettivo che concordi col soggetto; dove ne serviva uno
l'accordo si è spostato su un nome che porta il proprio genere («una giornata
fortunata», «catene intrise di magia», «il corpo leggero come una piuma»).

## Le tre scoperte della trentunesima sessione

### 1. ⚠️ Due inglesi che si contraddicono, e chi arbitra è il giapponese

Il verso 「ガウッ」 sta in due punti del file: a `44170` l'inglese dice `*gulp*`,
a `52145` dice `*Growl*`. La resa vecchia era **`*gnam*`**, cioè seguiva
`*gulp*`. Ma ガウ è un **ringhio**, non un boccone, e la riga accanto —
「ガルル！」, `*grrr!*` — conferma il repertorio della bestia.

💡 **È una famiglia diversa da quella già nota.** Nella 26ª si era visto
l'inglese che *specializza* un giapponese generico (「がおー」 = `*creaking*` su
un golem di legno e `*growl*` su una divinità serpente): lì le due letture
convivono ed è legittimo. **Qui una delle due è semplicemente sbagliata**, e non
c'è modo di accorgersene senza aprire il giapponese.

⚠️ **Corrette tutte e due a `*ringhio*`**, e la correzione vecchia è andata **nel
dizionario**, non nel lotto. Il punto è che `--divergenti` **non si è mosso**:
rendendo solo il sito nuovo sarebbe salito a 14 e la divergenza sarebbe stata
mia. Costa una riga togliere il problema invece di registrarlo.

💡 **A trovarla è stata una rete dello script del lotto, non l'occhio.**

### 2. 💡 La chiave del lotto conviene che sia `(riga, en)`, non `(riga, jp)`

Il metodo della 27ª dice di chiavare il dizionario delle rese su `(riga, jp)`,
perché il referto stampa riga e giapponese. **Ma il giapponese va scritto a
mano, e due volte in questa sessione un codepoint era sbagliato** — `喧` scritto
`U+5583`, `鉾` scritto `U+9243`. Tutt'e due le volte si è fermata la prima rete,
quindi il danno è stato zero; ma è tempo perso a ogni lotto.

Dal lotto `041` la chiave è **`(riga, en)`**: l'inglese è ASCII e non si sbaglia
a copiarlo. ⚠️ Serve **una rete in più**, perché `(riga, en)` identifichi
davvero: due voci sulla stessa riga con lo stesso inglese e giapponesi diversi
esistono (è il riciclo inglese, 84 stringhe su 231 giapponesi), e in quel caso
la chiave va cambiata per quella voce. Nei lotti `041` e `042` non è successo.

⚠️ **`scratchpad/scheletro.py` non esiste** — la 33ª è andata a cercarlo e la
cartella `scratchpad/` non era mai stata creata. Generava le chiavi giapponesi
dall'estrazione, esatte per costruzione, ma era scratch di sessione ed è andato
perso. Chi preferisce `(riga, jp)` se lo riscrive, oppure usa `(riga, en)`.
✅ Da adesso la cartella c'è e i suoi script sono committati: vedi
`scratchpad/LEGGIMI.md`.

### 3. 💡 Una rete nuova: lo stesso giapponese due volte **dentro** lo stesso lotto

`rese_gia_decise()` legge il **dizionario**, quindi non vede due voci dello
stesso lotto che condividono il giapponese: non ci sono ancora. È la trappola
della 26ª (il punk e il teppista) in forma nuova, e nel lotto `039` era reale —
i due Yerleswood condividono 「突撃モード継続」 e 「対象ノ行動パターン解析中」 con
inglesi diversi, quattro firme in tutto.

La rete costa quattro righe: raggruppa le rese del lotto per giapponese e
**muore** se un giapponese ne ha due diverse. Da copiare in ogni lotto futuro.

## Le quattro scoperte della trentesima sessione

### 1. ⚠️ Sei rese facevano concordare col giocatore, e una era di quel giorno

Cercando la resa gemella di una battuta della sorella maggiore ne è saltata fuori
una vecchia — «Dove **sei andata** a finire» — che sbaglia in metà delle partite.
La ricerca estesa a tutto il dizionario ne ha trovate **sei su 9.254 voci**, e la
sesta l'avevo scritta io **nel lotto 029**, due ore dopo aver scritto la ricerca.
Tutte corrette. Il dettaglio, la tabella e la riga di comando stanno in
`decisioni.md`. 💡 **Va rilanciata a ogni lotto**: è un referto da leggere, non
una guardia, perché i falsi positivi sono legittimi.

### 1-bis. 💡 Le lettere latine dentro il giapponese non sono tutte uguali

La bolla drago (`db_creature.hsp`) dice due cose scritte in alfabeto latino, e
vanno in due direzioni opposte:

- 「Pon」 è un'**onomatopea giapponese** scritta in latino — non è inglese, e si
  rende in italiano: «Pop»;
- 「HAPPY END！！」 è **inglese anche per chi legge in giapponese**, come
  `Target Acquired.` dello spazzino, e si tiene. Dichiarato in `invariati.md`.

⚠️ Idem 「URYYYYYYYYYY」 del vampiro (lotto 030): non è inglese, è il grido di Dio
in JoJo, e sta in lettere latine in tutte e due le lingue. La domanda da farsi non
è «sono lettere latine?» ma **«è una parola inglese, o è un suono?»**.

### 2. ⚠️ Copiare una resa già decisa può renderla identica all'inglese

Due volte in otto lotti. 「スシ！」 è già reso «Sushi!» a `104858`, dove l'inglese
urla `SUSHI!!!`; a `83627` **lo stesso giapponese** ha inglese `Sushi!`, e la
copia — che è ciò che il progetto chiede — fa scattare la guardia sull'identità.
Non è un difetto della resa, è una proprietà di quel sito: si dichiara in
`invariati.md`, **citando sempre l'altro sito come prova**. Aggiunte due righe,
`Sushi!` e `...!`.

⚠️ **Il caso opposto esiste**: 「はああああ…っ！」 reso `Haaaaah...!` era davvero la
grafia inglese copiata, ed è diventato `Aaaaaah...!`. La differenza: chiedersi se
la resa sarebbe stata quella **anche senza** l'inglese sotto gli occhi.

### 3. ⚠️ Una battuta può avere il ramo inglese vuoto, e allora è fuori perimetro

`db_creature.hsp:86293` è `lang("「この格好じゃ動きにくい…！」", cnvtalk(""))`: il
giapponese ha la battuta, l'inglese ha la stringa vuota, e l'inglese che le
spetterebbe è slittato sul `lang()` successivo. `estrai.py` non la vede — non c'è
niente da sostituire — quindi non è né tradotta né contata. In tutto il sorgente i
rami inglesi vuoti sono **31**, e **30 sono legittimi** (particelle come `位`,
`歳`, `耐性`): questo è l'unico che è una frase. **Non si può toppare** (la riga ha
tre `lang()`). Annotata, come `iknownnameref`.

### 4. ⚠️ L'avviso «NOME NON TRADOTTO» di `battute.py` può essere falso

Scatta quando una creatura **condivide il nome** con una che il file elenca prima:
il dizionario è indicizzato per contenuto e tiene la voce alla **prima** riga, che
sta in un blocco `DBMODE_SET`, mentre lo strumento cerca `DBMODE_REF_SPEC`.
Successo con la sorella minore, il cui nome era reso da sessioni. Si legge come
«non l'ho trovato», e si controlla cercando il giapponese in dizionario.

## Le due scoperte della ventottesima sessione

### 1. ⚠️ Il conteggio dell'estrattore non era il costo, e la motivazione era falsa

La decisione 0 diceva: anticipare `buff.hsp` (199), `chara.hsp` (258),
`item_func.hsp` (263), `screen.hsp` (103) perché sono ~830 firme ad alta
frequenza in coda a tutto. I numeri sono giusti — rimisurati tutti — ma **non
sono il costo**, e per il file che portava l'argomento erano metà della verità.

**Ogni messaggio di `buff.hsp` è spezzato in due e solo la prima metà sta in
`lang()`:**

```hsp
bufftxt(0, BUFF_HOLY_SHIELD) = lang("は光り輝いた。", " begin"), " to shine."
```

È un'assegnazione di **due** elementi. Il secondo (`" to shine."`) è un
letterale nudo, invisibile al dizionario: **70** in quel file. Tradurre le 199
voci contate darebbe «Nome inizia to shine.»

**E il messaggio si compone solo nel ramo inglese**, in un blocco custom del mod
(`chara_func.hsp:2316-2375`, `BLOODYSHADE CUSTOM`) che usa `_s()` e **sette casi
speciali** anch'essi scritti come letterali nudi (` mind...`, ` out the power of
his armor.`). ⚠️ **La riga originale, l'unica con `lang()`, è commentata**
(`:2310`). Il ramo giapponese (`:2377`) usa invece un **frammento unico**:
`name(id) + bufftxt(0, id)`.

💡 **Quindi la strada è una toppa, non 90 rese**: riportare il ramo inglese alla
forma giapponese — frammento unico, via `_s()`, via i sette casi — scioglie ~90
messaggi in un colpo. Togliere una morfologica si può; il resto è lavoro
strutturale e va fatto **prima** delle rese, non dentro un lotto.

⚠️ **E la motivazione scritta nella ripresa era inventata.** Diceva che i nomi
degli status «stanno nell'HUD in permanenza»: l'HUD ne disegna le **icone**
(`gcopy`, `screen.hsp`), non il testo. Il nome come testo esce nel popup sopra la
testa (`chara_func.hsp:2389`, `:2455`), in «The effect of X ends.» (`:2404`) e
nella lista dei potenziamenti della scheda (`command.hsp:2005`, `:10800`).
Frequenza alta comunque, conclusione salva — ma la prova era falsa.

⚠️ **`screen.hsp` non è «etichette fisse dell'interfaccia».** Solo **9** delle
103 voci sono statiche (`Gauge Ready`, `Autopickup`, `Blood`): le altre **94**
sono dinamiche, ed è la scena degli dèi che ti parlano mentre stai morendo.

💡 **`chara.hsp` invece costa molto meno di quanto dice il numero**: 258 firme ma
**143 testi distinti**, e **87** sono la stessa frase, «You have learned a new
ability, X.»

**La misura da rifare, con lo strumento che ancora non c'è:** contare i letterali
inglesi **fuori** da `lang()` per file, filtrando percorsi, nomi di file e chiavi
di `#define`. ⚠️ **La prima passata grezza era in `scratchpad/fuori_lang.py`,
che non esiste più** (vedi sopra: la cartella non era in git, e il file è andato
perso con lo scratch della sessione). I numeri che aveva dato — da rifare, non
da fidarsene — erano 70 (`buff.hsp`), 55 (`chara.hsp`), 120
(`item_func.hsp`), 175 (`screen.hsp`), 204 (`main.hsp`), 13 (`item.hsp`) — ma
per tutti tranne `buff.hsp` è **quasi tutto rumore**, e senza il filtro il costo
di quei file resta ignoto. È la stessa classe delle sette intestazioni del
diario e di `main.hsp:227`.

Concetto nuovo: [[un-conteggio-non-e-una-stima-di-costo]] nel vault.

### 2. 💡 `sdim` non è un tetto: HSP riespande in scrittura

`sdim buffname, 20, MAX_BUFF` sembra dire che un nome di status non può passare
i 19 byte, e un tetto del genere in italiano si sfonda subito. **Non è così.**
La controprova sta già in gioco: `skilldesc` è `sdim skilldesc, 40, MAX_SKILL` e
contiene una resa da **59 caratteri** («Memorizza incantesimi. Migliora
pergamene. Analizza nemici.»), vista a schermo nella lista abilità.

⚠️ Vale in **scrittura**. Il limite vero resta quello del **riquadro** che
disegna, che si misura a parte — e l'altra faccia, già nota, è che
l'autoespansione **non** vale in lettura: un array sparso letto oltre l'ultimo
indice assegnato è un `Array overflow`.

## Le quattro scoperte della ventisettesima sessione

### 1. ⚠️ Le righe commentate: l'ultimo «nome da fare» non esisteva

`estrai.py` **non salta i commenti HSP**. Misurato su tutto il sorgente:
**28 voci su 27.813** stanno su righe che cominciano per `;`, di cui **17 in
`db_creature.hsp`**. Quattro cadevano nel lavoro che restava, e una era l'unico
`nome` ancora aperto: `ハードゲイ` a `db_creature.hsp:105060`, commentata,
mentre la riga viva subito sotto (`:105061`) dà `explosioman`, **già reso**
«l'uomo esplosivo». Le altre tre erano i versi 「フーーー」 dello stesso mostro,
commentati in tutte e cinque le occorrenze.

Registrate in `rinviate.jsonl` col motivo, così spariscono dai lotti e restano
contate fra le non tradotte. **I nomi di `db_creature.hsp` sono chiusi.**

💡 **Da decidere**: far saltare i commenti a `estrai.py` sposterebbe la prova
d'identità da **27.813 a 27.785**, numero ancorato in mezzo progetto. Rinviata
apposta, non dimenticata.

### 2. ⚠️ I file «fuori da ogni elenco» non esistono, ma la lezione di `adv.hsp` sì

Cercati per davvero: `SPEC.md:413-418` li nomina **tutti**, `chat.hsp` come
Fase 3 e gli altri 63 come Fase 4. Il TODO della 26ª si chiude con un no.

⚠️ **Ma la cosa che rendeva `adv.hsp` importante non era l'elenco: era la
frequenza.** Dentro la Fase 4 — cioè *ultima* — stanno:

| file | firme | che cosa contiene |
|---|---|---|
| `buff.hsp` | 199 | i **nomi degli status** («Holy Shield», «Speed», «Regeneration») e i messaggi «X inizia / svanisce». ⚠️ **«Stanno nell'HUD in permanenza» era falso** — l'HUD disegna le icone; e le 199 voci sono **metà** dei messaggi: vedi la scoperta 1 della 28ª |
| `chara.hsp` | 258 | «You have learned a new ability, X.» e simili |
| `item_func.hsp` | 263 | i messaggi di quando raccogli, lasci cadere, un oggetto va perduto |
| `screen.hsp` | 103 | «Gauge Ready», «Autopickup»: etichette fisse dell'interfaccia |
| `item.hsp` | 206 | fasce di prezzo del negozio, «cheap», «expensive» |
| `main.hsp` | 330 | messaggi del ciclo principale |

Sono ~1.360 firme che il giocatore legge a ogni partita, in coda a tutto.
**Da valutare come lotto fuori ordine**, con lo stesso argomento che ha
spostato le battute davanti a tutto.

### 3. ⚠️ Il giapponese può essere inglese, e allora l'inglese si tiene

Lo `<Spazzino di sotterranei>` dice `lang("「Target Acquired.」", "Target
Acquired.")`: **le due lingue sono la stessa**, cioè l'autore fa parlare
inglese la macchina anche al giocatore giapponese. Quattro battute
(`Target Acquired.`, `Resistance is futile!`, `Pwned!`, `WTF`) dichiarate in
`invariati.md`. Tradurle darebbe all'italiano una macchina che parla la lingua
di chi legge, che né il giapponese né l'inglese hanno.
Stesso criterio già usato per `user`.

### 4. ⚠️ L'inglese riusa il repertorio di un'altra creatura

Non «amplia» o «restringe»: **incolla**. Le battute dell'**erudito**
(`P-please, no sir...`, `You are cruel.`, `Ha ha ha!`) escono identiche in bocca
al **profugo degli Elea**, al **viaggiatore** e — le tre di morte — al **saggio
della collina** e al **pescatore**. In giapponese sono quattro creature diverse
con quattro registri diversi: l'erudito è sprezzante, il profugo ha fame e
nostalgia, il viaggiatore viene rapinato, il saggio muore riconoscendo di non
aver saputo abbastanza.

💡 **Come si riconosce**: due creature lontane nel file con la **stessa lista
inglese** e giapponesi che non si somigliano. Vale la pena cercarne altre in
blocco invece di scoprirle un lotto per volta.

## Le tre scoperte della ventiseiesima sessione

### 1. ⚠️ L'ordine dei lotti era cieco alla frequenza

L'ordine di riga metteva l'accattone di livello 2 accanto a una divinità di
livello 1200. Misurato: delle 1.975 voci che restavano, **605 stavano su
creature di livello 1-10** e **528 oltre il livello 100**.

`battute.py` ora ordina per **livello crescente**, a parità di livello prima chi
ha più battute; `--per-riga` rimette l'ordine vecchio. Il livello è una
**procura**, non una misura: nel sorgente non esiste un campo «quanto spesso
esce» — `DBSPEC_CHARA_RARE` non lo è.

### 2. ⚠️ La stessa battuta giapponese può avere due firme

Il punk e il teppista dicono **tredici battute giapponesi identiche** con
tredici inglesi diversi: due firme, due voci da tradurre, a lotti di distanza.
Se le rese divergono **nessuna guardia lo vede** — sono entrambe italiano
valido. Misurati **88 giapponesi ripetuti**.

⚠️ **Otto divergenze su dieci erano legittime**: l'inglese *specializza* ciò che
il giapponese lascia generico (「がおー」 è `*creaking*` su un golem di legno e
`*growl*` su una divinità serpente). Quindi **promemoria, non divieto**: il
referto del lotto stampa «⚠️ GIÀ RESO ALTROVE» accanto a ogni voce che ha già
una resa, e `--divergenti` le elenca per giudicarle a mano.

### 3. ⚠️ `adv.hsp` era in perimetro e in nessun elenco

Uno screenshot ha mostrato «Hedorre il fratello volpe **joins your party!**».
Dodici voci ad alta frequenza mai toccate, ora chiuse. 💡 **Da rifare: cercare
altri file che gli strumenti sanno leggere e che nessun elenco nomina.**

## Il metodo per le battute di `db_creature.hsp`

⚠️ **Il lotto prende creature intere**, tutte le classi insieme
(`FLAVOR_PASSIVE`, `_ANGERED`, `_DEATH`, `_KILL`, `_WELCOME`). Il registro di un
mostro è uno. ⚠️ E serve anche a vedere quando **l'inglese ha cambiato il
personaggio**, che in una battuta sola non si nota.

```powershell
python -m strumenti.estrai db_creature.hsp --da-tradurre --uscita lavoro/_c.jsonl
python -m strumenti.battute --conto      # quanto resta, per classe
python -m strumenti.battute              # il lotto, in ordine di livello
python -m strumenti.verifica lavoro/<lotto>.jsonl
python -m strumenti.reimporta lavoro/<lotto>.jsonl
python -m pytest strumenti/tests -q
python -m strumenti.prova_identita
python -m strumenti.creature
python -m strumenti.battute --divergenti
python -m strumenti.genera_toppe_nomi
python -m strumenti.genera_toppe_casuali
```

### ⚠️ E poi i due passi che questo elenco non nominava

`reimporta` scrive **nel dizionario e basta**. L'albero di build resta com'era, e
`compila` senza argomenti produce solo `start.ax`, **non** l'eseguibile. Chi si
ferma qui vede la catena tutta verde e prova in gioco una build **che non
contiene le rese nuove** — ed e' successo nella 33ª, che ha annunciato due volte
un `cgx-test.exe` rifatto quando l'eseguibile era quello del giorno prima.

```powershell
python -m strumenti.applica                # dizionario + toppe -> albero di build
python -m strumenti.compila --eseguibile   # e SOLO cosi' esce l'exe
copy "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" `
     "C:\Games\Elona\elonaplus2.31\cgx-test.exe"
```

💡 **Come ci si accorge che manca `applica`**: si apre il `.hsp` di build alla
riga appena tradotta e ci si legge ancora l'inglese. La catena delle verifiche
**non** lo vede, perche' legge il dizionario e il sorgente pinnato, non la build.
⚠️ E `applica` **ricrea l'albero da zero**, quindi cancella l'exe che c'era: se
dopo `applica` non si ricompila, in `build/` non c'e' nessun eseguibile.

Fatti `fase2-battute-001` … `-042`, e con il `042` **il file è chiuso**. Il
metodo resta scritto qui perché serve tale e quale al prossimo file a battute.
Dopo aver rigenerato l'estrazione le creature già fatte spariscono, quindi si
riparte sempre da `[0]`.

💡 **Il referto stampa solo l'inglese, e l'inglese non arbitra.** Serve il
giapponese sotto gli occhi: nella 30ª il lotto si è sempre letto con uno script
di dieci righe che chiama `battute.repertori()` e scrive `riga / classe / jp / en`
su un file di testo, comprese le note «GIÀ RESO ALTROVE» e la forma grezza delle
dinamiche. Senza quello si traduce l'inglese, che è la cosa che il progetto ha
deciso di non fare.

💡 **Il lotto si scrive con uno script, non a mano.** Dalla 27ª il metodo è: un
file Python nello scratchpad con un dizionario `{(riga, jp): resa}` e un
controllo che **muore** se una resa non aggancia nessuna voce. Chiave `(riga,
jp)` e non la firma, perché il referto stampa riga e giapponese. Costa dieci
righe e ha già evitato due lotti scritti sulla voce sbagliata.

💡 **Tre guardie che `verifica` non fa e che conviene rilanciare a mano** sul
JSONL del lotto: nessun carattere a doppia larghezza tranne `♪`; nessuno dei
proibiti (`…`, `“”`, `～`, `«»`); nessuna parola inglese residua (`the`, `you`,
`your`, `is`, `my`…) in una statica che non sia dichiarata invariata.

💡 **Lo script del lotto tiene cinque reti**, e conviene copiarle tutte:

0. la chiave **identifica una voce sola** (serve solo se si chiava su `en`);
1. nessuna voce senza resa;
2. nessuna resa che non aggancia niente;
3. nessuna resa che **diverge da una già decisa** per lo stesso giapponese —
   ⚠️ questa **non deve uccidere lo script**, deve stampare: nella 31ª la
   divergenza segnalata era giusta ed era la resa *vecchia* a essere sbagliata;
4. ⚠️ **nessun giapponese reso in due modi dentro il lotto stesso**, che la 3
   non vede perché legge il dizionario.

Nella 31ª la 1 ha fermato due volte un codepoint sbagliato e la 3 ha trovato
`*gnam*`. Le reti hanno lavorato più dell'occhio.

💡 Le altre guardie dei lotti: niente morfologia inglese residua; nessun
carattere a due byte tranne `♪`; nessun **participio che concorderebbe col
giocatore**. ⚠️ Quest'ultima **non** è automatizzabile: provata a mano su un
lotto, ha dato **3 falsi positivi su 4** («bella figura», «Nessuna ferita?»,
«la ferita» sono sostantivi).

## Le regole di resa

Terza persona sempre; mai `_s()`, `is()`, `was()`, `your()`, `have()`,
`does()`, `yourself()`; mai una preposizione davanti a `name()` o `itemname()`,
mentre `con`, `per`, `tra`, `sopra`, `dentro`, `contro` e `verso` reggono; la
preposizione sta nel valore, non nella frase; invarianza di genere prima di
tutto; un nome di abilità o di oggetto si copia; una `statica` si scrive **nuda**,
e se deve citare usa `\"`, **mai** le tipografiche.

⚠️ **`his(x)` a un argomento si può togliere, `his(x, 1)` no.**

### Gli appellativi che cambiano col sesso del giocatore

⚠️ Sono **due**, e la guardia ora li copre entrambi: `_onii` (`text.hsp:111`)
«Fratellone»/«Sorellona», 36 siti di chiamata; e `_syujin` (`text.hsp:112`)
«Padrone»/«Padroncina». **Non portano l'articolo dentro** — a differenza di
`name()` — quindi la preposizione nuda regge («di Fratellone», «per
Fratellone») e l'articolo no («il mio Fratellone» sbaglia genere metà delle
partite).

⚠️ **`cdatan(CDATAN_NAME, rc)` invece l'articolo lo porta dentro**, come
`name()`: il nome italiano è «il fratello volpe». Niente «di» davanti.

### Dalle battute

⚠️ **Il giocatore è l'interlocutore e non ha genere noto.** «Welcome home!» è
«Eccoti a casa!», «Rieccola a casa.», «Eccoti di ritorno.». Vale per i
**vocativi**: `You thief!` è «Al ladro!», e allo stesso modo «Al maniaco!»,
«All'assassino!». 💡 **Il registro può risolvere il genere**: chi dà del lei o
del voi — il maggiordomo, la monaca, la signorina dal cuore nero, l'accattone —
non concorda mai.

**Un verso si rende in ortografia italiana, non si copia dall'inglese.**
`Woof..` sull'ululato 「ワオーン…」 è «Auuuh...»; 「めぇめぇ」 è «Bee bee»;
「ぴよぴよ」 (il pigolio) è «Pio pio»; 「こーん」 (la volpe) è «Cooon...». Dove il
giapponese identifica l'animale la resa lo segue.

💡 **Il tic di una creatura si porta in italiano**: la sorella cane chiude con
«bau», la sorella gatta con «miao».

💡 **L'inglese storpiato in katakana si rende storpiato**: 「カモンベイベー」 è
«Camon beibi!», 「グッド！」 è «Gud!», 「ざっつあぷりちーふらわー」 è «Zatsa priti
flauer!».

⚠️ **Quando una concatenazione si spezza in due `lang()`** i due frammenti sono
**un lotto solo**. E se un frammento resterebbe identico all'inglese, gli si fa
portare qualcosa che il giapponese ha e l'inglese ha perso — l'allungamento di
ポピー diventa «Poppyyy!», il ギャ di 「ギャハハハハ」 diventa «Ghiahahaha!».

⚠️ **Vale anche per le dinamiche.** `_syujin(...) + "!"` è **per costruzione**
identico all'espressione inglese, perché la funzione porta dentro la
traduzione. Il giapponese di `db_creature.hsp:93453` è 「ー！」, cioè il grido è
**allungato**: la resa diventa `+ "!!"`, e la guardia si scioglie senza inventare
niente.

### Trovate nella trentunesima

- ⚠️ **Il maiuscolo dei robot lo porta il katakana, non l'essere una macchina.**
  Metal Vesda (`92618`) e i due Yerleswood scrivono le particelle in katakana
  (`ノ`, `ヲ`, `スル`) e vanno in maiuscolo; l'androide di `122654` e `<Mani>`,
  che è il **dio delle macchine**, parlano giapponese normale e restano in
  minuscolo. La domanda è sul katakana, non sul personaggio.
- 💡 **Un bisticcio di segmentazione si rifà tenendo insieme le due letture.**
  「この先生きのこるためには！」 si legge «sopravvivere d'ora in poi» e «questo
  maestro fa i funghi»; l'inglese lo butta via e scrive `Live!`. Reso «Di qui in
  avanti, o si sopravvive o si fa da concime ai funghi!», che dice tutt'e due.
  Stessa famiglia: 「受けて断つ…もとい、受けて立つ！」 → «Ti faccio a fette...
  cioè, ti faccio fronte!».
- ⚠️ **Un idioma tradotto alla lettera dall'inglese non è una specializzazione,
  è un errore.** 「腕が鳴る」 è «mi prudono le mani» e l'inglese scrive `It's
  called arm ringing`; 「引き際を間違えた」 è il momento sbagliato per ritirarsi
  e l'inglese ci legge un grilletto; 「引導を渡す」 è dare l'estremo saluto e
  l'inglese scrive `I'll give you guidance`.
- 💡 **Una citazione in bocca a un personaggio si rende con la versione italiana
  che esiste già**, e la lista continua: 「計画通り」 è Light in Death Note
  («Tutto secondo i piani»); 「テケリ・リ」 è Lovecraft e in italiano si scrive
  uguale; 「でーんでんむーしむし」 è la filastrocca della chiocciola e si rende
  con quella italiana; 「ご飯にするん？お風呂にするん？それとも…」 è la battuta
  della moglie che aspetta a casa, dove `<Yacatect>` mette l'obolo al posto di
  sé stessa.
- ⚠️ **Il contrario esiste e va nell'altra direzione**: 「Destroy！Dynamite！」 e
  「Noooooooooo！」 stanno in **lettere latine anche nel giapponese**, quindi si
  tengono. La domanda resta quella della 30ª — «è una parola inglese, o è un
  suono?» — con una seconda prova quando la resa coincide con l'inglese:
  *sarebbe stata questa anche senza l'inglese sotto gli occhi?*
- 💡 **Il nome di un incantesimo dentro una battuta si copia, e se il giapponese
  lo tronca si tronca uguale.** 「ファイアボル…？」 è `ファイアボルト` mangiato
  dalla memoria di `<Raizel>`: la resa parte da «Saetta di fuoco»
  (`skill.hsp:509`) e diventa «saetta di fuo...?».
- ⚠️ **Un vocativo sbagliato di proposito resta sbagliato di proposito.**
  `<Raizel>` scambia il giocatore per sua moglie e lo chiama `ばあさん`
  **comunque sia il giocatore**: il vocativo porta lo scherzo — «nonnina» — e
  tutto il resto della frase resta invariante. È la stessa forma di `_syujin`.
- 💡 **Il ♪ è l'unico carattere a due byte che ci resta, e il ☆ si perde.**
  「シャドウシスター推参ッ☆」 ha perso la stella: CP932 non la codifica. È una
  perdita silenziosa, non una scelta.

### Trovate nella trentesima

- ⚠️ **Un vocativo che il giapponese non declina non può diventare italiano
  declinato.** La `マスター` del terminale Xeren non è `_syujin`: è un letterale, e
  «Padrone» sbaglierebbe metà delle partite. Reso **«Comandante»**, che vale per
  entrambi i generi ed è anche giusto per un'arma da guerra. Stessa famiglia:
  `先生` dell'insegnante, il cui nome italiano non porta genere.
- 💡 **Il katakana come tic si rende in maiuscolo.** Vale per i robot (Gilphem,
  Metal Vesda, l'apparato di comunicazione), per la carota ninja che parla tutta
  in katakana, e **a metà parola** per il soldato yerles infetto, dove il
  giapponese si sfalda dentro la parola: «A... A... che maLE... CHE MALE...».
- 💡 **Una citazione si riconosce dal giapponese e si rende con la versione
  italiana che esiste già**: 「またつまらぬものを噛んでしまった」 è Goemon di Lupin
  III col morso al posto del taglio; 「お前もまた、強敵（とも）だった」 è la
  convenzione di Hokuto no Ken, dove «nemico forte» si legge «amico», e la resa
  tiene tutte e due le letture.
- 💡 **Un bisticcio si rifà sul materiale italiano già deciso**: il giapponese
  「HはHでもHitmanの方だがなぁーっ！」 gioca sulla lettera H, e in italiano la
  lettera diventa la **S** del nome che il progetto aveva già scelto, «La S sta
  per Sicaria, mica per Sesso!». Idem 「イガいとやるな…」, dove イガ è il riccio
  della castagna nascosto dentro 意外と: «e io di ricci me ne intendo».
- ⚠️ **L'allungamento giapponese si porta con le vocali ripetute**, e quando la
  parola allungata la scrive una funzione — `_onii` — l'allungamento passa nella
  coda: i sette modi in cui la sorella minore chiama il giocatore diventano
  `!`, `!!`, `...`, `...♪`, `...?`, `...!`.
- 💡 **Una preghiera non si translittera: si rende con la formula italiana.**
  「南無三ッ」 della samuraformica è «Che il cielo mi assista!», 「南無阿弥陀仏」
  dell'infernello è «Pace all'anima sua».
- 💡 **Le citazioni continuano ad arrivare, e le riconosce solo il giapponese**:
  「時を止めた者が…」 è JoJo (l'inglese al suo posto scrive «Hey, c'mon c'mon!»),
  「わけがわからないよ」 in bocca a una fata è Kyubey, 「あくまでメイドですから」
  è il maggiordomo di Kuroshitsuji col bisticcio su «diavolo».
- 💡 **La narrazione dentro `cnvtalk` si rende narrazione lo stesso**, anche se
  le virgolette che la funzione aggiunge la fanno sembrare parlato: è quello che
  il progetto fa già dal fratellino di `82821`, visto a schermo.

### Trovate nella ventisettesima

- ⚠️ **Un vocativo non può portare un aggettivo che concordi col giocatore.**
  «questo scemo» sbaglia metà delle partite; **«quell'imbecille» no**, perché
  `quell'` vale per entrambi i generi. Altre che reggono: «mezza cartuccia»,
  «pappamolla», «carogna», «idiota», «debole», «canaglia», «soggetto».
- 💡 **Il registro di chi parla può risolvere il genere anche in avanti**: la
  cameriera, la guaritrice e l'attrazione del locale danno del **lei** al
  cliente, e così `お客さま` non ha bisogno di un vocativo che concordi
  («Aaah! Tutto bene?!»).
- ⚠️ **`_syujin` e `_onii` vanno lasciati soli a portare il genere**: tutto ciò
  che li circonda dev'essere invariante. «Bentornato, Padrone!» sbaglia,
  «Eccoti a casa, Padrone!» no.
- 💡 **Il bisticcio di mestiere si tiene**: il pescatore dice 活きのいい («bello
  fresco», di pesce) e 雑魚 («pesciolino»), e in italiano diventano «Che bel
  pescione vivace» e «che pesciolino da niente».
- 💡 **Una parlata da bambino piccolo si rende con la erre che diventa elle**:
  il gatto randagio storpia かえる in かえう, e in italiano «Tolno a casetta».
- 💡 **Il katakana che scrive una parola giapponese è enfasi, non prestito**:
  カガク è 科学, e si rende «SCIENZA» in maiuscolo. Diverso da エクスプロージョン,
  che è inglese e va storpiato («Ecsplosgion»).
- ⚠️ **Un nome proprio che compare in una battuta è quasi sempre già deciso
  altrove**: `ヴェセル` è **Bethel** (dal nome della creatura), `ジャビ王` è **re
  Xabi**, `巫女` è **sacerdotessa**, `異形の森` è **Vindale**, `サイモア` e
  `ヴァリウス` restano **Saimore** e **Barius** perché li usa già `chat.hsp`.
- ⚠️ **Il prefisso col nome di chi parla non si porta dentro `cnvtalk`.** Il
  giapponese di Moyer è `モイアー「…」`, col nome **fuori** dalle virgolette
  giapponesi; `cnvtalk` avvolge tutto fra virgolette, quindi il prefisso
  finirebbe dentro. L'inglese lo lascia cadere e si fa lo stesso.
- ⚠️ **Un imperativo con pronome atono concorda col giocatore**: «arrestatelo»,
  «portatelo» sbagliano metà delle partite. Si toglie il pronome
  («Immobilizzate e torturate!») o si mette un nome che porti il proprio genere
  («quell'imbecille», «un cane bastonato», «Che lumaca!»).
- 💡 **Le citazioni si rendono con la versione italiana che esiste già**:
  「真実はいつだってひとつ！」 è il tormentone di Conan, «C'è sempre una sola
  verità!»; 「灰色の脳細胞」 sono «le cellule grigie» di Poirot;
  「ピーキーすぎて…」 è la battuta di Kaneda in AKIRA. La citazione si riconosce
  dal giapponese, non dall'inglese, che spesso l'ha già persa.
- ⚠️ **Il katakana può nascondere un dialetto**: il corvo mercante dice
  「ナンデヤネン」 e 「マイドアリ」, cioè parla **in kansaiben**, la parlata del
  bottegaio di Osaka. Si rende con la lingua viva del mercante, non con la
  lettera.
- ⚠️ **`estrai` tiene distinte due voci con lo stesso giapponese e inglesi
  diversi sulla stessa riga** (il carbonchio rubino, `67563`): sono due firme,
  e vanno rese **uguali**, non a caso.

### Dalle sessioni precedenti

- **Il giocatore non ha genere noto.** Non «sono sopravvissuto» ma «sono ancora
  in piedi»; non «quando sono pronto» ma «quando sarà tutto pronto».
- **Un elenco di compiti si rende all'infinito** («Bere qualcosa»).
- Un prefisso davanti a sostantivi di genere diverso può solo essere un aggettivo
  in -e. Ma se può andare **dopo**, ci va.
- **Nessun participio quando il soggetto non ha genere noto.**
- **`your()` diventa «proprio»**, che concorda con la cosa posseduta.
- **In un menu la valuta si abbrevia.**

## Le cose da non riscoprire

### L'inglese non traduce: riscrive, e in cinque modi

Tutti visti l'11/08. **Inventa** (`<Gwen>`, `<Mia>`, il gorgoglio di chi affoga
diventato «I'm sorry I failed you»); **amplia** (una risatina di tre sillabe →
venti parole); **restringe**; **scambia** (`<Tam>` ha le prime due battute
invertite); e ⚠️ **cambia il personaggio** — la macchina delle pulizie è
infantile in giapponese e robotica in inglese.

**L'originale arbitra sul significato; l'inglese conserva il diritto di
specializzare** quando sa qualcosa che il giapponese non dice.

### Un gioco di parole va rifatto, non tradotto

Il gioco della recluta è **visivo** (矢 e 失 si somigliano a vederli), non
fonetico. Reso con **suono/sonno** — e «Suono» è una resistenza che esiste
davvero. ⚠️ Il materiale del bisticcio dev'essere roba che nel gioco esiste.

### Una stringa che il giocatore legge può stare fuori da `lang()`

Sette intestazioni del diario (`command.hsp`) **e `main.hsp:227`**, il primo
messaggio del log. Toppate **a mano**: un generatore riscriverebbe sopra.

### Il nome di una funzione può mentire

`cnvarticle` (`init.hsp:173`) **non mette un articolo**. `cnvtalk` avvolge fra
virgolette — per questo il testo dentro conta come contenuto. E ⚠️ **l'aiuto
della console mente**: `add_ally` dice «by character index» ma fa
`characreate` dall'ID di database (`system.hsp:4882`).

### Una preposizione può agire a venti righe di distanza

`s(12)` si compone a `text.hsp:11837` e finisce dopo «da » a `:11859`.

### Il giapponese arbitra sul significato, il codice sullo stato del gioco

⚠️ Il diario dice スライム, il dialogo di Miches dice プチ: vince il codice.
⚠️ Due quiz (`text.hsp:998` e `:1214`) portano lo stesso giapponese con risposte
diverse: arbitrano `map.hsp:2271` e `:9009`. **Non toccarle.**

### Se l'inglese rende un nome in più modi, vince quello della prosa

⚠️ ルストール è `Lustor` (prosa), `Rust Plaza` (etichetta) e `Ruoza` (esca di
quiz) — e `Ruoza` è **già** il nome di ルオザ.

### L'ordine di una concatenazione non è un vincolo: si toppa

⚠️ Ma una toppa si aggancia **solo a una riga senza `lang()`**. Se la voce è
**dinamica** non serve nessuna toppa. E `funzioni_di_contenuto` confronta le
interpolazioni **ordinate**.

### Non correggere una toppa che qualcuno genera

`toppe.jsonl` è in larga parte generato. **Se uno strumento la genera, la
correzione va nello strumento.** ✅ Verificato l'11/08 che le toppe **a mano
sopravvivono** ai due generatori.

### Cercare prima di scrivere

Tipi di negozio, elementi, verbi della pianta, assetti tattici, parti del corpo,
tipo di Nefia, categorie di filtro. E per le battute: i **nomi delle creature**
sono già tutti in dizionario. ⚠️ Anche i termini di contorno: «campo di
prigionia», «pannello di comando», «Porto Kapul», «Poppy», le resistenze —
erano **tutti già decisi altrove**.

### Aggiungere una funzione che l'inglese non aveva non si può

Si possono **togliere** le morfologiche, non se ne possono **aggiungere**.

### La frase di combattimento vive in due file

`action.hsp` scrive «… e» e imposta `gdata(GDATA_DMG_TYPE) = 2`;
`chara_func.hsp:6323` legge il flag e stampa il resto. `init.hsp:1666` aggiunge
già lo spazio.

### Le stringhe che sembrano testo e sono codice

`EN` (`action.hsp:4816`, `text.hsp:9361`) è la chiave che `*convert_talk` cerca.
` Lv` (`action.hsp:12383`) è ciò che il gioco cerca in coda al nome.

### Un letterale può essere l'operando di un confronto fra due file

⚠️ `Party Room` (`proc.hsp:1123`) è confrontato col nome che assegna
`map_rand.hsp:1287`, fuori perimetro. **Rinviata.**

### Le altre, invariate

- la carta di `db_card.hsp` dice cosa la creatura rappresenta;
- l'articolo sta sulla testa del sintagma, non sulla persona;
- `ドレイク` è «draco», confermato a schermo;
- un nome già preso non si può riusare, **e vale anche per le esche del quiz**.

## Il sistema dei cibi, che è chiuso ma va guardato

`foodname` (`text.hsp:3211-4356`) compone il nome di ogni cibo cucinato: otto
famiglie, ~70 piatti. **Interpola due cose di forma diversa:**

| ramo | interpola | forma | resa |
|---|---|---|---|
| carne, **uova e formaggio** | `refchara(id, NAME_ORG, 1)` | **con l'articolo** | parentesi: «bistecca (il minotauro)» |
| verdura, frutta, dolci, pesce, pane | `ioriginalnameref` / `fishdatan` | **nuda** | «di»: «insalata di carota» |

⚠️ Visto in vetrina dal panettiere di Palmia e **tutto giusto** tranne la carne,
che il panettiere non vende. Comportamenti di monte, da **non** riaprire:
«2 sacchi di torta di mele» e «(Rank: 3) con benedizione».

## Il tetto di un menu

⚠️ **Il riquadro taglia**: non manda a capo, non restringe il carattere. Il
metro è il terzo argomento passato a `*prompt_key`:
`caratteri = (pixel − 46) / 7,7`. Lo fa `strumenti/larghezze.py`. **Va lanciato
a ogni lotto di menu.**

⚠️ **La stringa inglese non è il budget.** ⚠️ **La larghezza può dipendere dalla
lingua**: `450 - 50 * en` vale **400**.

⚠️ **`talk_conv` manda a capo ma l'ultima parola scappa** (`init.hsp:1326-1369`).
`strumenti/diario.py` lo misura: tetto **36**, 214 siti. Il verso giusto è
**accorciare, non imbottire** — ma quando la riga si compone a runtime
l'intuizione «più corto è meglio» è **sbagliata**.

⚠️ **Le battute non hanno tetto**: passano da `txt`, non da `talk_conv`.

## Le due righe di `action.hsp` che non si traducono

- **`:4584`** — l'articolo inglese davanti a un'arma unica. Toppa.
- **`:9631`** — `his(tc, 1)`, il possessivo che in italiano si omette. Toppa.
  ⚠️ **Il testo di una toppa non passa da `degrada` e non può portare accenti.**

## 391 stringhe fuori perimetro

⚠️ **Un oggetto di Elona ha due nomi, e ne traduciamo uno.** `iknownnameref` è
quello prima dell'identificazione, e l'estrattore non lo guarda
(`estrai.py:65`). **Deciso: si annota e si prosegue.** Conseguenza: il 100% di
`db_item.hsp` e `custom_tweaks.hsp` **è falso**.

⚠️ **E un secondo perimetro fuori: `data/talk.txt`** (86 KB), che non passa da
`lang()` — `SPEC.md:436`. Due voci di `text.hsp` sono rinviate lì.

## L'ordine che resta

0. ✅ **Deciso il 12/08, e la premessa era sbagliata**: il blocco di Fase 4
   **non** si anticipa in blocco. Si anticipano solo i **~90 `buffname`**; i
   `bufftxt` diventano lavoro strutturale a parte; `chara.hsp`, `item_func.hsp`,
   `screen.hsp` e `main.hsp` restano dove sono finché non c'è il conteggio dei
   letterali fuori da `lang()`. Vedi la scoperta 1 della 28ª.
   ✅ **Fatto il 13/08**: `buffname` e `bufftxt` sono chiusi, restano i
   `buffdesc`. ⚠️ **Il conteggio dei letterali fuori da `lang()` non è ancora
   stato fatto**, e finché non c'è, il costo di `chara.hsp`, `item_func.hsp`,
   `screen.hsp` e `main.hsp` resta ignoto. 💡 Adesso però si sa che cosa
   cercare: `buff.hsp` è il caso risolto, e la forma del difetto — una frase
   spezzata in due con solo la prima metà dentro `lang()` — è quella che lo
   strumento deve saper riconoscere.
1. ✅ **le battute di `db_creature.hsp`**: chiuse il 2026-08-13, lotti `015`-`042`;
2. **`proc.hsp`**, 971 firme, per zona di riga da **1716**;
3. `command.hsp`, `trait.hsp`;
4. `ai.hsp` (94) ed `event.hsp` (649);
5. `chara_func.hsp`, le 286 rimanenti — ⚠️ dentro ci sono le tre pietre di
   Lesimas e l'ankh del sole, **già rese** in `text.hsp:11576-11594`: si
   **copiano**. E la causa di morte (`:6850`), che va insieme a `main.hsp:4409`;
6. `init.hsp` (133) — ⚠️ lì sta la decisione sul possessivo `his(x, 1)`;
7. i nomi non identificati di `db_item.hsp` e le 2.555 descrizioni.

## Domande aperte

⚠️ **`CDATA_SEX` e il registro giapponese si contraddicono, e capita più di una
volta.** L'`<Ex spazzino>` (`95309`) ha `CDATA_SEX = 0`, cioè maschio, ma parla
al femminile (`やだー`, `ですよ`, `ところね`); `<Urcaguary>` (`71913`) ha
`CDATA_SEX = 1` e parla da vecchio guerriero (`フハハ`, `殺せ`, `肉を食え`);
`<Egelveil>` (`63370`) è femmina e usa `〜のだ`. Nella 31ª **la questione non è
stata decisa**: dove serviva un accordo la frase è stata girata («non ho
combinato niente»), che è la stessa tecnica usata per il giocatore. 💡 La regola
scritta dice che *il codice arbitra sullo stato del gioco*, quindi in teoria
vince `CDATA_SEX` — ma non è mai stata messa alla prova su una creatura che
parla chiaramente dell'altro genere, e **a schermo non l'ha vista nessuno**.

⚠️ **`db_creature.hsp:86293`, la battuta col ramo inglese vuoto**: si allarga
`estrai.py` alle voci con inglese vuoto — e allora `applica` deve saper scrivere
dentro un `cnvtalk("")` — oppure resta fuori perimetro per sempre. Rinviata, non
dimenticata. È l'unica frase fra i 31 rami vuoti del sorgente.

⚠️ **`battute.py` aggancia i nomi per riga e non per `dbid`**, e per questo dà
«NOME NON TRADOTTO» a chi condivide il nome con una creatura elencata prima. La
correzione tocca la funzione che compone i lotti e non si fa dentro un lotto.

✅ **Il menu tattiche del mod è stato guardato il 13/08, e la risposta è la
peggiore delle tre: `cs_list` non taglia, sconfina.** Le colonne si
sovrapponevano davvero — «Crescita della destre**Cambio di forma (A)**». Il
tetto vero è **20 caratteri** (145 px / 7,2), non 13 come si stimava, e lo
passavano **10 `buffname` su 71**, adesso zero. ⚠️ Restano da sistemare due
cose: la stima vecchia diceva `Schivata d'emergenza` fuori misura e **non lo
era** (20 esatti), e il sito che conta di più — l'elenco degli status sul
personaggio — **manda a capo da solo a 70 caratteri** e non è a rischio. Vedi
`decisioni.md`, «Due tetti che nessuno aveva misurato» e «Dove finisce un nome
di status».

⚠️ **Gli altri tre elenchi a colonne di `custom_ai.hsp` non sono guardati, e
lì l'ancora dice il contrario.** Sono `:1263`, `:1337` e `:1821`, con un passo
di **150 px su quindici righe** (contro i 145 su ventidue del menu dei
potenziamenti), ed elencano azioni e **nomi di incantesimo**, che sono tradotti
al 100%. Il tetto è sempre 20 caratteri, e lo sfondano **15 nomi italiani su
445** — ma lo sfondano anche **5 inglesi**, fino a 24 (`Critical Particle
Cannon`, `Thread of Innervation`). 💡 **È la famiglia dei `buffdesc`, non
quella dei `buffname`**: un tetto che upstream accetta già rotto, quindi non è
un vincolo che la resa italiana debba rispettare. E accorciare un nome di
incantesimo per far stare un menu del mod lo peggiorerebbe in tutti gli altri
posti dove sta benissimo. ⚠️ **Prima di decidere va guardato a schermo**: si
apre parlando a un alleato → *Teach a spell or ability*.

⚠️ **`Cyber Dome` fu deciso sull'inglese.** Il giapponese è アクリ・テオラ, nome
**opaco** che per la regola resterebbe invariato. Segnalata, non toccata.

⚠️ **`spawn_item` ha prodotto due volte l'oggetto sbagliato**, poi ha ripreso.
L'unica pista è lo stato dei filtri: `spawn_item` **non chiama `flt`**.

⚠️ **La toppa dell'ordine delle Nefia rompe l'ordine giapponese.** Innocuo finché
compiliamo la build inglese.

⚠️ **`diario.py` non vede le righe che si compongono a runtime.**

⚠️ **Le 56 dinamiche di `db_creature.hsp` restano fuori classificazione.**
Nessuna di esse è oggi un nome.

⚠️ **Undici divergenze restano in `--divergenti`**, giudicate legittime. Se una
sessione futura non è d'accordo, il posto per discuterle è `decisioni.md`.

⚠️ **`estrai.py` non salta i commenti HSP.** 28 voci su 27.813. Farlo saltare
sposterebbe la prova d'identità a 27.785: decisione rinviata, vedi la scoperta 1
della 27ª.

⚠️ **Il riciclo inglese è misurato: 84 stringhe inglesi coprono 231 giapponesi
diversi** in `db_creature.hsp`. Non è più una scoperta a sorpresa, è una
quantità nota. Le peggiori: `Huh?` su **6** giapponesi; `Why are you doing
this?`, `P-please, no sir...`, `Don't make a fool of me!`, `You are cruel.`,
`Ahhhh!`, `I don't deserve this...`, `Go to hell!`, `Stop it!` su **5**
ciascuna. Si rimisura così:

```powershell
python -c "import json,io,collections; d=collections.defaultdict(set); [d[v['en']].add(v['jp']) for p in ['lavoro/_c.jsonl','dizionario/db_creature.hsp.jsonl'] for v in map(json.loads, io.open(p,encoding='utf-8')) if v.get('file')=='db_creature.hsp' and v.get('tipo')=='statica']; m=[(e,j) for e,j in d.items() if len(j)>1]; print(len(m), sum(len(j) for e,j in m))"
```

💡 **Come si usa**: quando un lotto tocca una di queste righe, **non si guarda
l'inglese**. Chiuse: 76452/76458/76464 (erudito), 88185/88191/88197
(viaggiatore), 88274/88280/88286 (profugo), 73911 (saggio della collina),
90657 (pescatore), 88363/88369/88375 (addetto del casinò, che in giapponese
minaccia la tortura e chiama i buttafuori), 98449 (la guardia, giapponese
identico al guerriero mercenario: lì si **copia**).
⚠️ **Resta aperta** 102518/102524/102530.

💡 **Il riciclo funziona anche al contrario**: la guardia (`98449`) e il
guerriero mercenario (`115178`) hanno il **giapponese identico** e due inglesi
diversi. Lì la regola si ribalta — non si reinventa, si copia la resa già
decisa.

## Cose che valgono sempre

⚠️ **Il sorgente è pinnato al tag `2.31.2.0`**, e l'integrità si verifica col
manifesto SHA-256, **mai** con `git status`. Gli hash sono in MAIUSCOLO.
✅ Ricontrollato l'11/08: **72/72**.

⚠️ **L'attributo di sola lettura sulle cartelle NON è la protezione del
sorgente.** I 3.374 file del clone sono tutti scrivibili; solo le 34 cartelle
hanno il flag, che su Windows è acceso quasi ovunque. La protezione è la
disciplina più il manifesto.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp`; chi copia nomi di creatura fuori da
`db_creature.hsp`; chi confronta un letterale contro un valore tradotto.

⚠️ **CP932 non codifica tutto, e quello che codifica non è detto si veda.**
Niente `«»`; e niente `…`, `“”`, `・`, `《》`, **`☆`**, **`～`**, né i caratteri a
larghezza intera (`Ｑｙ＠`). Unico ammesso: `♪`.
Gli accenti veri si scrivono nel dizionario e li degrada `applica`;
⚠️ **guardare dove cade l'accento**: a fine parola è gratis, a metà no.
⚠️ **Le toppe non passano da `degrada`.**

⚠️ Un guardiano dell'ambiente blocca i messaggi di commit che contengono `/man/`
letto come percorso: passare il testo con `git commit -F <file>`.

⚠️ **La shell mangia il backtick, e un heredoc lungo in bash si rompe.** Scrivere
un documento che contiene codice fra apici inversi **da un file**, non da riga di
comando. ✅ Successo di nuovo l'11/08 scrivendo `decisioni.md`.

## Per rifare la prova in gioco

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -Force
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

⚠️ La copia fallisce se il gioco è aperto.
⚠️ **Non lasciare una shell con la directory corrente dentro `build\`**: tiene la
cartella occupata, `applica` muore a metà e `compila` accusa
`#Error: in line 112 [main.hsp]`, che è la riga dell'`#include` e non dice
niente della causa. Successo l'11/08. ⚠️ **E di nuovo il 13/08**, con un
sintomo diverso e più chiaro — `PermissionError: [WinError 32] ... utilizzato
da un altro processo` sulla `rmtree` di `applica`. La colpevole era una shell
di lavoro entrata lì dentro per leggere il sorgente. Si esce e si rilancia:
`applica` riparte da capo senza danni.
⚠️ Se `applica` viene interrotta lascia l'albero **incompleto**: si rilancia e
basta.

⚠️ **Controllare la data dell'exe prima di fidarsi di uno screenshot.**

**L'eseguibile in `cgx-test.exe` è della 34ª (14/08/2026 02:45, 17.588.604
byte)** e contiene tutto quello di prima — le battute di `db_creature.hsp`, i
`buffname`, le due toppe di `buff.hsp`, i 71 messaggi dei potenziamenti, i 63
`buffdesc` e le 24 toppe della 33ª — più la correzione dello spazio nella scena
ricucita. Compilato senza errori, **13.146 sostituzioni**, e con le tre rese di `chips.hsp`.

✅ **I messaggi dei potenziamenti sono stati visti a schermo il 13/08, e la
toppa regge.** Con `add_ally 249` e una bacchetta di velocità (`spawn_item 377`,
si punta con `z`) è uscito «**Aranart la sorella minore diventa piu' agile.**»:
nome minuscolo con l'articolo dentro — cioè `cnven()` è tolto per davvero —
frase unica, nessun residuo tipo « up.», nessun accordo. ✅ Provato anche sul
**giocatore**, che è il caso da cui il `cnven()` era stato tolto: regge.
💡 «Aranart» non è nostro: `db_creature.hsp:117782` compone
`randomname() + " " + nome`, ed è la stessa cosa che upstream fa in inglese.

💡 **Come si prova un potenziamento**: la console **non ha un comando** che li
applichi. La via corta è la **bacchetta di velocità**, `spawn_item 377`, che si
raccoglie con `,` e si punta su chiunque con `z`.

### La console di debug

**Si apre con F12** (`main.hsp:3322`; F11 è `dump_chara`). Esce con ESC. Parte in
modalità **HSP, non Lua**: `spawn_chara <id>` funziona subito.

⚠️ **`add_ally <id>` genera la creatura E la rende alleata** — l'aiuto dice «by
character index» ma il codice fa `characreate` dall'ID di database
(`system.hsp:4882`). È il modo di far uscire **oziose e benvenuti** da creature
che il database dà ostili.

⚠️ **La relazione predefinita decide quale classe di battuta esce.** Con
relazione < 0 la creatura attacca e dà le **offese**; con relazione 0 o da
alleata dà le **oziose** (`ai.hsp:774-796`). Si legge nel blocco `DBMODE_SET`
della creatura, campo `CDATA_RELATION`.

ID di creatura verificati: **165** il cane, **50** il segugio, **267** il cavallo
zoppo, **386** la giraffa, **482** Yacatect, **326** il menestrello, **9** il
mendicante. Dalle battute rese: **538** il fratello volpe (porta `_onii`),
**363** la sorella cane maggiore, **962** il bambino, **352** `<Silvia>`,
**174** il punk, **36** l'anziano, **963** il bambino sadico, **1066** `<Sist>`,
**1043** `<Imarituka>`, **947** `<Burt>`, **949** il barista, **1008** la
cthulhick, **1048** la giovane rondine.

Dai lotti 015-022, tutti letti in `defines/mod.hsp`: **272** l'artista,
**233** il fante juere, **224** `<Ainc>` il cavaliere novizio, **415** la forma
di vita quantistica, **535** il cucciolo di grifone, **623** l'erudito,
**260** il gatto nero, **262** l'androide, **271** la canaglia, **909** il
soldato artiglio, **346** il cucciolo, **263** l'angelo nero, **182**
l'infermiera, **184** il rampollo, **332** il gatto randagio, **472** il profugo
degli Elea, **500** il guardiano del karass, **321** l'uomo esplosivo,
**648** il bimbo della collina, **274** l'aristocratico, **223** `<Raphael>`,
**142** `<Erystia>`, **441** il cittadino, **407** la cameriera, **280**
`<Balzak>`, **203** `<Moyer>`, **302** il capo della banda, **369** il cane
poliziotto, **183** il riccone, **279** `<Icolle>`, **868** `<Rianna>`,
**243** `<Arnord>`, **259** `<Noel>`, **244** il samurai kamikaze, **473** il
viaggiatore, **345** la moto di Kaneda, **253** `<Marks>`, **408** `<Lune>` la
cameriera, **74** la guaritrice, **802** l'angelo apprendista, **32** lo
spazzino di sotterranei.

Dai lotti 023-026: **317** la mietitrice dagli occhi d'argento, **204** il
soldato scelto di Palmia, **519** `<Nazuna>`, **476** `<Naplus>`, **438**
`<Carla>`, **437** `<Milos>`, **709** il gufo spaziale, **925** `<Alsapia>`,
**348** e **518** le due mascotte a ore, **620** il corvo mercante, **374**
`<Mefan>`, **301** `<Conery>`, **650** `<Dain>`, **471** l'addetto del casinò,
**697** il lupo mannaro detective, **893** `<Zisilion>`, **478** `<Eila>`,
**231** `<Colonnello Gilbert>`, **486** l'abitante dell'abisso, **80**
`<Xabi>`, **577** `<Lenas>`.

`spawn_item <id>` lascia l'oggetto **per terra**: si raccoglie con `,`.
ID utili: **256** l'attrezzo da cucina portatile, **204** il cadavere generico,
**740** la `<Conchiglia Ignota>`, **1249** l'Aurtehom, **1097** la banca di
Yacatect, **1068** il cuore del crepuscolo.
⚠️ **`733` è il sacco da boxe**, non un cibo. Verificare un ID in
`defines/mod.hsp` prima di darlo.

⚠️ **`spawn_item` non può produrre un piatto cucinato**: il nome composto esce
solo se `INV_ITEM_PARAM2` è diverso da zero, e `item.hsp:2694-2705` lo riempie
solo dentro un negozio o quando **cucini tu**.

⚠️ **Generare mostri a mano è un modo pessimo di provare l'evoluzione**:
`chara.hsp:2319` la tira con `rnd(300) < gdata(GDATA_LEVEL)`, dove
`GDATA_LEVEL` è **il piano del dungeon**. La prova buona è una **Nefia profonda**
con *Spawn evolved enemies* su **always**.

### Come si provano le battute

`ai.hsp:766` chiede `cdata(CDATA_TXT, cc) != 0`, e `db_creature.hsp` lo
incrementa **una volta per ogni classe che la creatura possiede**: l'interruttore
è acceso per costruzione. Poi serve stare **entro dieci caselle**, e la battuta
esce ogni **5 turni con probabilità 1 su 4** (`ai.hsp:768-771`). Si aspetta
tenendo premuto `5`. ⚠️ **Non usare l'abilità Esibizione mentre si aspetta**:
`ai.hsp:772` zittisce tutti.

Il **benvenuto a casa** scatta entrando in `AREA_HOME` (`system.hsp:34`), e il
codice richiede relazione neutrale o creatura nell'area (`main.hsp:8449`).

⚠️ **Il ballo e la predica dei PNG non escono mai.** `ai.hsp:1654` e `:1668` li
accendono con `CDATA_AI_CALM` a **7** e **8**, e in tutto il sorgente **nessuno
assegna quei due valori**: codice morto.

### Come si provano le esibizioni

Le dieci righe del giudizio finale escono **solo se suoni tu** (`proc.hsp:950`),
e serve l'abilità **Esibizione**, che si impara dal maestro a **Derphy** o
**Porto Kapul**. **Elemosina accorata** si impara da sé svegliandosi con **meno
di 500 monete**; **Predica** con Fede oltre 9.

### Il diario

**Si apre col tasto `j`**. ⚠️ **Le notizie vecchie restano in inglese**:
`newsbuff` sta dentro il salvataggio. Contano solo quelle che nascono dopo.

### Le 169 battute degli dèi, ancora mai viste

⚠️ **Non escono se non si indossa l'amuleto giusto.** `GDATA_GOD_TALK` parte a
**0** e lo accende **solo** `ENCHANT_GOD_SIGNALS`, che ce l'ha un oggetto solo —
`<Conchiglia Ignota>`, `spawn_item 740`. E serve **seguire un dio**.

```
F12 → spawn_item 740      raccogli con , e indossa con w
c                          controlla che il personaggio segua un dio
salva, esci, ricarica      → alla prima mossa esce il «bentornato»
dormi in un letto          → il «sonno», e col caso il «sogno»
uccidi qualche mostro      → l'«uccisione», 1 volta su 20
offri un oggetto su un altare → «offerta gradita»
j, pagina di sinistra      → le notizie nuove
```

Ci si converte **pregando** (`p`) **sopra un altare**, e ⚠️ **il dio che prendi è
quello dell'altare**. ⚠️ **`spawn_item 171` non serve**: l'altare generato dalla
console nasce **senza dio**. Il posto giusto è la **Terra della tregua**, che
tiene tutti e otto gli altari in una sala: Mani (10,8), Lulwy (13,8), Opatos
(10,13), Ehekatl (13,13), Itzpalt (20,8), Kumiromi (23,8), Jure (20,13),
Yacatect (23,13). 💡 Conviene **Ehekatl**, che ripete l'ultima parola di ogni
frase.

### Il collaudo, punto per punto

- ✅ **L'evoluzione degli alleati**, ✅ **i nomi a schermo**, ✅ **«draco»**,
  ✅ **il combattimento**, ✅ **il menu degli ordini al compagno**, ✅ **il libro
  dell'abisso**, ✅ **i quattro menu a oggetto**, ✅ **la vetrina del
  panettiere**, ✅ **il diario delle missioni**, ✅ **le esibizioni e
  l'elemosina**, ✅ **il ♪ come icona**: provati.
- ✅ **Le battute e `_onii`**: provate l'11/08 col fratello volpe (`add_ally 538`).
  «Fratellone» interpola correttamente; viste anche «Cooon...», «Il fratellino ha
  una voce triste.». ✅ E `name()` rende «qualcosa» per una creatura non visibile:
  «Qualcosa perde la vita.» **non è un difetto**.
- ❌ **«*X* tira un sasso.»**: il difetto riparato, **mai visto**. Serve uno
  spettatore di livello alto rispetto all'artista (`proc.hsp:755`).
- ❌ **L'evoluzione dei nemici**: **mai vista**. La prova mancante più vecchia.
- ❌ **La carne fra parentesi**: mai vista, e decide **due** famiglie di cibi.
  ⚠️ serve cucinare col **256** su un cadavere.
- ❌ **Le 169 battute degli dèi**: mai viste.
- ❌ **Il tocco elementale** (`proc.hsp:8797`).
- 🆕 **Da provare**: «Buon cammino!» all'ingresso nel mondo; «X si unisce al
  gruppo!» (`add_ally 538`); le battute dei lotti 010-014; la **bacheca degli
  incarichi**; i nomi delle Nefia; il gioco di carte; la banca.
- 🆕 **La lista data a fine 27ª, mai tornata**: `add_ally 500 407 332 223`,
  aspettare tenendo `5`; poi tornare a casa; poi `spawn_chara 472` e `623` da
  attaccare e uccidere. Serve a vedere se le tre volte in cui il giapponese ha
  scavalcato l'inglese hanno retto a schermo. **Da rifare o completare.**
- 🆕 **Dai lotti 023-026, da guardare**: `spawn_chara 471` (l'addetto del
  casinò, dove l'inglese aveva di nuovo le battute dell'erudito); `add_ally
  709` (il gufo spaziale, che in giapponese dice tre versi **sfigurati** resi
  sfigurati anche in italiano — se sembrano refusi, l'ho sbagliato);
  `add_ally 620` (il corvo mercante, in parlata da bottegaio); `add_ally 348`
  (la mascotte che fa il barker per Jure).
- 🆕 **Le tre cose della 27ª che solo uno screenshot decide**: `add_ally 408`
  (`<Lune>`, che chiama col `_syujin` allungato); `spawn_chara 32` (lo spazzino
  che parla **inglese per scelta**: se stona a schermo, la riga di
  `invariati.md` va ridiscussa); `add_ally 326` (il menestrello, che ora
  **canticchia** invece di cantare parodie inglesi).
- 🆕 **La lista data a fine 28ª, mai tornata** (l'eseguibile attuale la mostra
  già, non serve ricompilare):
  ```
  add_ally 408   <Lune>: deve chiamare «Padrone!!», due punti esclamativi
  add_ally 326   il menestrello: canticchia, non canta parodie inglesi
  add_ally 620   il corvo mercante: parla come un bottegaio
  add_ally 709   il gufo spaziale: tre versi storpiati DI PROPOSITO
  ESC, poi tenere premuto 5 per ~40 turni
  spawn_chara 32    lo spazzino: parla INGLESE per scelta; se stona si ridiscute
  spawn_chara 471   l'addetto del casinò: attaccarlo e ucciderlo
  ```
- 🆕 **Dai lotti 027-034 della 30ª** (ID verificati in `defines/mod.hsp`).
  ⚠️ **La colonna «come» non è un dettaglio**: quattro di queste creature non
  hanno battute oziose e davanti a loro si aspetta invano. Corretto il 13/08.
  ```
  ASPETTA (add_ally, poi tieni premuto 5)
  249   la sorella minore: sette modi di chiamarti, tutti su _onii
  364   la sorella maggiore: parla di se' come «la sorellona»
  773   il toro blu: quattro muggiti, uno e' «Mo' basta...»
  829   la carota ninja: parla TUTTA IN MAIUSCOLO, e' voluto
  508   l'apparato di comunicazione: robot, tutto maiuscolo
  616   la samuraformica (parla da samurai)
  351   il guerriero dalla testa di leopardo: Janus, <Silvia>, torque

  ATTACCA (spawn_chara, e fatti attaccare: escono le offese)
  465   il soldato yerles infetto: le maiuscole a meta' parola
  627   il Gigante Castagna
  829   616   351   (hanno anche le offese, oltre alle oziose)

  TORNA A CASA (solo il bentornato: entrare in AREA_HOME con loro nell'area)
  502   il terminale Xeren: deve dire «Comandante», non «Padrone»
  492   <Pascal>: abbaia, e le tre rese sono bau / bau bau / arf
  ```
  ⚠️ **502 e 492 non hanno oziose**: la lista vecchia diceva di aspettarle, ed
  è per questo che non tornava niente. Il loro bentornato è l'unica via comoda;
  le altre battute che hanno sono morte e uccisioni.
  Il toro e la carota servono a decidere una cosa che solo lo schermo decide:
  **se il maiuscolo del katakana regge o urla troppo**.
- 🆕 **Dai sei lotti 037-042 della 31ª** (ID verificati in `defines/mod.hsp`).
  ⚠️ Sono tutte creature di livello altissimo: `add_ally` serve proprio perché
  incontrarle per caso non capita. Lista rifatta per classe il 13/08 — **otto
  di queste quindici non parlano se aspetti**.
  ```
  ASPETTA (add_ally, poi tieni premuto 5)
  796   <Aribel>: le sette regole — ✅ vista la numero uno il 13/08
  805   <Renai>: fratello e sorella, «forma umana»
  628   <Raizel>: ti chiama «nonnina», e «saetta di fuo...?» mangiata
  842   la <Kunoichi alla moda>: «Sorella dell'Ombra»
  654   <Marka>: «Orsa a chi!»
  383   l'<Ex spazzino>: «con le chiocciole ho fatto pace»
  382   la <Lumaca> in sella all'androide: la filastrocca, e
        «Destroy! Dynamite!» che resta in inglese di proposito

  ATTACCA (spawn_chara, e fatti attaccare: escono le offese)
  601 e 664   i due Yerleswood: MAIUSCOLO, e le due frasi in comune
              devono uscire IDENTICHE — ⚠️ mezza prova il 13/08
  686   <Regulus>: il fratello, «forma umana»
  379   <Siva>: quattro versi da cane, non «Woof»
  911   <Tezcatlipoca>: «Mi prudono le mani», «Ti avvolgo nel fumo»
  756   <Shuraida>: il concime ai funghi
  534   <Aile>: annunci di bordo, poi il dialetto ruvido

  UCCIDI (la battuta esce morendo)
  640   <Sinaha>: «Miaosa... come...» — ⚠️ livello 250
  331   <Ehekatl>: ripete l'ultima parola — ⚠️ ha solo uccisione e bentornato
  ```
  💡 **Le tre cose che solo lo schermo decide**, aggiornate al 13/08:
  1. se «Miaosa» si legge o sembra un refuso — **ancora aperta**, ed è una
     battuta di **morte** su una creatura di livello 250;
  2. se le due frasi dei Yerleswood escono uguali — **mezza prova**: «AVVIO
     L'AGGIORNAMENTO DEI DATI DI COMBATTIMENTO.» è uscita due volte identica,
     ma il log non dice *chi* l'ha detta, quindi potrebbero essere due volte
     lo stesso. Serve vederne una seconda, o la riga lunga;
  3. ✅ **se il maiuscolo dei robot regge: sì.** «AVVIO L'AGGIORNAMENTO DEI
     DATI DI COMBATTIMENTO.» si legge bene e non urla. Manca la riga più lunga
     («ANALISI DEGLI SCHEMI DI COMPORTAMENTO DEL BERSAGLIO IN CORSO.»), ma il
     dubbio era sul principio e il principio tiene.
  ⚠️ **E in quel combattimento è saltato fuori «l'Yerleswood di serie»**,
  corretto in «**lo** Yerleswood»: vedi `decisioni.md`.
- ⚠️ **Il non tradotto esce in inglese, non in giapponese.**

## I tetti misurati, con la loro ancora

| campo | tetto | ancora | fonte |
|---|---|---|---|
| tracciatore HUD | 6 | sinistra, taglia | `screen.hsp:2002` |
| razza e classe | 3 | sinistra, taglia | `chara.hsp:4679` |
| slot d'equipaggiamento | 6 | sinistra, taglia | osservato a schermo |
| gradi di resistenza | 9 | **destra, invade** | `command.hsp:11002` |
| nome nella lista abilità | **24** | sinistra, invade il costo | `command.hsp:5382` |
| descrizione, menu `a` | 34 | taglia (`strmid`) | `command.hsp:5389` |
| descrizione, menu `W` | 34 | idem | `command.hsp:5599` |
| **descrizione, menu di lancio** | **40** | idem | `command.hsp:8851` |
| **descrizione, scheda incantesimi** | **46** | idem | `command.hsp:10996` |
| **voce di menu** | **(px − 46) / 7,7** | sinistra, taglia | `strumenti/larghezze.py` |
| **riga di diario** | **36** | **manda a capo, ultima parola scappa** | `strumenti/diario.py` |
| **riga di notizia** | **33** | idem | `addnews2`, `text.hsp:12106` |
| **riga del compenso** | **30** | idem | `text.hsp:11885` |
| pagina del diario | ~40 | taglia | osservato a schermo |
| nome di oggetto | 66 | oltre, passa da `zentohan` | `item_func.hsp:2254` |
| **colonna del menu tattiche** | **20** = 145 / 7,2 | **destra, sconfina sulla colonna** | `custom_ai.hsp:3173` |
| **etichetta di stato, HUD** | **11** = (80 − 6) / 6,6 | destra, taglia al bordo | `screen.hsp`, `gcopy 65+en*15` |
| **etichetta di stato larga** | **13** = (95 − 6) / 6,6 | idem | `screen.hsp`, `gcopy 65+en*30` |

💡 **I tre tetti nuovi si contano in caratteri e non si stimano**, perché il
carattere della build inglese è **`Courier New`** (`config.txt`, `font2.`), che
è monospaziato: 7,2 px a 12 px di corpo, 6,6 px a 11. Misurati e verificati a
schermo il 13/08 — «Marchio letal» sono esattamente 13 caratteri.
⚠️ **Nessuno dei tre ha una guardia**: `larghezze.py` guarda solo i menu che
passano da `*prompt_key`. È il lavoro numero 0 della prossima sessione.
⚠️ **E il tetto si misura sulla forma degradata**: `volonta'` è 15 caratteri,
`volontà` 14, e a schermo ci va la prima.

⚠️ Il nome di creatura compare in messaggi **senza limite**. Il più lungo è
`<Ratin> l'investigatrice della Gilda dei Guerrieri`, 50 caratteri: visto a
schermo, non tronca.

Vedi [[una-chiave-che-si-sdoppia]], [[l-inglese-non-traduce-riscrive]],
[[il-gioco-di-parole-cambia-canale]],
[[una-causa-plausibile-scritta-nel-codice]],
[[la-frequenza-non-si-deduce-dal-file]], [[una-procura-non-e-una-proprieta]],
[[una-guardia-vale-solo-dove-guarda]], [[guardia-troppo-severa]],
[[il-round-trip-non-basta-conta-i-byte]], [[accorciare-non-imbottire]],
[[il-difetto-di-monte-lo-paghiamo-noi]],
[[l-ordine-di-una-concatenazione-si-toppa]],
[[correggere-il-generatore-non-il-generato]],
[[genere-ignoto-si-risolve-col-complemento]], [[larghezza-per-campo]],
[[il-testo-dentro-la-stringa-non-e-codice]],
[[la-frase-che-si-compone-in-due-file]],
[[il-nome-interno-non-e-quello-a-schermo]],
[[coerenza-fra-due-file-uno-solo-tracciato]],
[[toppe-fuori-dal-dizionario]], [[la-forma-memorizzata-non-e-quella-scritta]],
[[una-chiave-che-collide-non-e-una-chiave]],
[[il-campo-che-il-sorgente-dichiara]], [[la-testa-porta-il-genere]],
[[una-decisione-nel-posto-sbagliato]], [[una-guardia-agganciata-a-se-stessa]],
[[ultima-scrittura-vince]], [[percentuale-senza-denominatore]],
[[la-categoria-che-il-sorgente-dichiara]],
[[il-posto-decide-quando-arriva-il-dato]], [[dato-o-derivata]],
[[toppe-generate-dal-sorgente]], [[stessa-forma-va-verificata-nel-codice]],
[[strumento-di-diagnosi-assente-non-guasto]], [[chi-accende-la-stringa]],
[[il-database-che-spiega-invece-di-dichiarare]], [[omofono-base-kanji-patina]]
e [[cp932-perdite-silenziose]].
