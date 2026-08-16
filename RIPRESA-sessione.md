# Ripresa sessione

Aggiornato: 2026-08-16, fine della **cinquantaduesima** sessione (il collaudo
arretrato fatto e tre difetti trovati, il **sesto punto cieco** nato e chiuso
nello stesso giorno, e **tre file finiti**: `custom_ai.hsp`, `tcg.hsp`,
`tcg_custom.hsp`).

⭐⭐⭐ **Il collaudo ha trovato tre difetti, e nessuno dei tre era in lista.** Il
pannello dei ritocchi della 51ª non l'aveva mai visto nessuno; aperto, ha detto:

    (Ora: ERRORE)          non era un errore, era «sfida fallita»
    (Ora: spento)% in piu' il suffisso in MEZZO alla frase, che regge solo acceso
    la quinta riga         la finestra ne regge QUATTRO, non sei come diceva il conto

💡 **E il primo l'ha trovato la porta, non la schermata.** Cercando *come si
arriva* al pannello è saltato fuori che la voce del menu di Esc diceva
«Regolazioni» mentre tutto il pannello dice «Ritocchi» dalla 50ª: era l'unica
voce del dizionario con «tweak» nell'inglese, e nessun conteggio interno al
pannello poteva vederla. **Chi cercava i ritocchi non trovava la porta.**

⭐⭐⭐ **«(Ora: ERRORE)» era la resa sbagliata di uno stato normale, e la vedeva
chiunque.** `GetTStatusProgress` cade sul ramo finale quando il valore è
**negativo**, e `-1` non è un valore che nessun ramo riconosce: è «la sfida non è
più in corso», e gliela assegnano `action.hsp:2159` (esci dalla grotta degli
accattoni salutando gli Elea), `map.hsp:776` (rientri a Vernis), `chat.hsp:3933`
(superi i 7000 di fama). L'inglese scrive `FAILED` nel senso di **fallita**, e la
resa l'aveva letto come **malfunzionamento**. ✅ Il ramo di guasto vero è
l'altro — `GetTStatus:500`, « FAILED» nudo senza «Currently» — e resta «ERRORE»:
zero chiamate a `GetTStatus` con `TWEAK_CATEGORY_CHALLENGE`, misurato.
💡 **La lezione è quella di «Bandits Killed» e del prefisso `dbg_`, per la terza
volta: si guarda il sito, non la parola.**

⭐⭐⭐ **Il SESTO punto cieco è nato e morto oggi: `scratchpad/tabelle_en.py`.**

    AITextData(0, 1) = "Not Set", "Self", "Target", "Ally", "Player", "Enemy"

Una riga sola, sette parole che il giocatore legge in una colonna. `nudi_en`
cerca le righe che **disegnano** e quelle che **compongono**: questa non è né
l'una né l'altra — è un'assegnazione di array, e il testo arriva a schermo molto
più tardi, **per indice**, da una riga che di letterali non ne ha nessuno
(`s = AITextData(CAIComparator(cnt, tc), 2)`). Sono **7 in tutto il sorgente**,
tutte in `custom_ai.hsp`: 6 fatte, 1 decisa, **0 da fare**.
⚠️ **E il referto ha dovuto togliersi due famiglie di falsi positivi in ordine**:
`traitrefn(0) = lang(…), lang(…)` ha la stessa forma ma sta nel dizionario (159
tabelle → 89, e un regex non basta perché dentro quelle `lang()` ci sono
parentesi annidate: si contano a mano), e le righe che **compongono** — un `+`
fuori dalle stringhe — le vede già `nudi_en` (89 → 51).

⭐⭐⭐ **Le dodici classi non si traducono, e non è una rinuncia: è una misura.**
`custom_ai.hsp:493` e `:508` non le **leggono**, le **confrontano** con
`cdatan(CDATAN_CLASS, …)`, che porta la chiave inglese: la scrivono
`action.hsp:13670`-`:13703` e `command.hsp:4591`-`:4626`, la rileggono
`chara.hsp:2875`-`:2962`, `ai.hsp:2546`, `calculation.hsp:888`, `:953`, `:992`,
`action.hsp:5704`, `:5723`, `chara_func.hsp:5010`. Tradurle lascerebbe l'IA
**senza nessuna classe da riconoscere**. È la lezione della 46ª sulle stringhe
che il giocatore DIGITA in forma nuova: **quel che serve a un confronto non è
testo.**
⚠️ Non poteva finire in `rinviate.jsonl`, che indicizza per **firma** e una
tabella non ne ha: sta in `DECISE` dentro il referto, che confronta sorgente e
build e sa dire «fatta / decisa / da fare».

⭐⭐ **Il gioco di carte si chiama «Gioco delle Ombre», e a deciderlo è stato il
codice.** Era una delle tre incoerenze aperte — «Tenebre» in `command.hsp:6166`,
«Ombre» in `chara_func.hsp:7002` e `:7004` — e non si è scelto a maggioranza: è
il termine italiano ufficiale di Yu-Gi-Oh! per «Shadow Game», e il mod cita
quella serie **apertamente**, perché `tcg_custom.hsp:1587` sigilla l'avversario
**dentro una carta** e `:1556` gli lascia **l'anima danneggiata**. Il riferimento
è il contenuto della scena, non un'eco lontana.
⭐ E **«amur-cage» è stato reso per la prima volta**: `chara_func.hsp` l'aveva
sempre **aggirato** riscrivendo la frase, ma a `:1608` la gabbia è il soggetto e
non si può aggirare → «Finisci nella gabbia di Amur!».

⭐⭐ **Il figlio può essere maschio o femmina, e l'inglese non se ne accorge.**
Le 54 battute di `event.hsp:random_eventProc` in inglese non mostrano mai il
sesso di chi parla; in italiano quasi tutte lo mostrerebbero. Ogni resa è scritta
per **non accordarsi col parlante**, e dove la via corta avrebbe accordato la
frase gira intorno all'ostacolo:

    I'm going to be an adventurer   →  «Tanto andrò all'avventura»
    too different from everyone     →  «non mi va di stonare in mezzo agli altri»
    recognize me as an adult        →  «mi consideri una persona adulta»

💡 È la disciplina degli helper `_s(rc)`/`his(rc)` **al contrario**: lì si toglie
una funzione che l'inglese ha, qui si evita un accordo che l'italiano
aggiungerebbe da solo.

⭐ **«Identica» vuol dire identica coi tab davanti.** Due parole chiave delle
carte sono sfuggite a una toppa `tutte` perché `:887` sta dentro tre `if`
annidati e `:1010` dentro quattro: il conteggio delle occorrenze si legge sulla
**riga intera**, non sul letterale.

⚠️ **Due parole restano inglesi apposta, e i conteggi le accuseranno per sempre**:
«Immune» (`tcg.hsp:969`) e «Mana» (`:3480`) in italiano si scrivono uguali, e una
toppa che sostituisce una parola con sé stessa è rumore che ogni sessione futura
dovrebbe rileggere per capire che non fa niente. Stessa scelta di «Abnormal».

---

## I punti della cinquantunesima, che restano validi

⭐⭐⭐ **Il pannello dei ritocchi è finito, e `custom_tweaks.hsp` con lui.** Le
190 righe che la 50ª aveva lasciato in sei menu, più le **3 che non stavano nei
menu** e che nessun conteggio per schermata vedeva: 193 toppe, **264 applicate**
in tutto il file, e zero righe inglesi rimaste a parte una lasciata apposta.
`nudi_en` scende da 849 a **656**, `triage_nudi` da 647 a **454** righe di testo.
💡 **La coda che il conteggio per schermata non vede è reale e si misura**: il
criterio della 50ª — «il testo sta in blocchi, e un blocco è una schermata sola»
— ha trovato le 190 dei menu e non le tre fuori, che però sono **due domande a
cui il giocatore deve rispondere** (le conferme delle sfide) e **una battuta in
mezzo a uno scontro** (Zeome). Chiudere un file vuol dire guardare anche fuori
dai blocchi.

⭐⭐⭐ **La regola di forma che la 50ª chiedeva non esiste, e provarlo era il
lavoro.** Il debito diceva: «serve una regola di forma che distingua» i `return`
di testo da quelli di chiave. Messa alla prova:

    text.hsp   return "vernis"   chiave di mappa      NON è testo
    init.hsp   return "st"       suffisso ordinale    È testo

Tutt'e due un token minuscolo, senza spazi, senza punteggiatura: **nessuna
regola che guardi il letterale può separarli**, e inventarne una avrebbe
ripetuto per la quinta volta l'errore di `_PERCORSO`.
✅ La regola vera guarda **dove va a finire il valore**: un `#defcfunc` non è un
letterale, è una funzione, e conta chi la chiama. Se anche una sola chiamata sta
su una riga che disegna o compone, quel che restituisce arriva a schermo. È la
stessa lezione di «Bandits Killed» e del prefisso `dbg_`: **si guarda il sito,
non la parola**. `scratchpad/return_en.py`, **121 `return` → 0 da fare**.

⭐⭐ **E il banco di prova che la 50ª indicava era già chiuso da una sessione
passata.** «Il caso su cui provarla è `init.hsp:155`-`:168`, i suffissi
ordinali»: li aveva risolti `toppa-init-cnvrank.py` facendo diventare `if ( jp )`
un `if ( jp | en )`, e quel ramo non lo raggiunge più nessuno. Le quattro righe
stanno ancora lì **identiche al sorgente**, e un conteggio ingenuo le chiamerebbe
«da fare» per sempre. 💡 **È il rovescio del rinvio della 50ª**: là un debito
dipendeva da un fatto e ha aspettato in ordine; qui dipendeva da un ricordo, e il
ricordo era vecchio di una sessione. **Prima di contare, si guarda la build.**

⭐⭐ **Tre incoerenze vecchie, tutte trovate traducendo e nessuna cercata.**

    l'oggetto delle tasse  fattura (db_item:144367)   bollette (toppe del diario, 50ª)
    il gioco di carte      Gioco delle Tenebre (command:6166)  Gioco delle Ombre (chara_func:7004)
    la radice di necromancy  negromanzia (db_item:139896)  necromantica (skill:1492)

In tutt'e tre ho nominato la cosa **col nome che porta a schermo nel punto in cui
la riga ne parla** — è la stessa regola in tutti e tre — ma ⚠️ **la scelta vera
resta da fare**, e nessuna si scioglie con una toppa perché stanno nel dizionario
con plurale e articolo attaccati. ⚠️ E sulla terza **ho spostato io il
conteggio**: i lotti di oggi hanno scritto «negromanzia» altre due volte, quindi
adesso è 3 a 1.

⭐ **Una voce di menu può portare due letterali inglesi sulla stessa riga.** Le
voci del menu di difficoltà chiamano `GetTStatusProgress` e le passano
l'etichetta del contatore (`"Days Survived"`), che esce a schermo dentro il
suffisso: « (Ora: 12 giorni di sopravvivenza)». Tradotta la voce e lasciata
l'etichetta, la riga resta mezza inglese — e **nessun conteggio per riga se ne
accorge**, perché le due stringhe stanno sulla stessa riga. Stessa forma a
`:1283`, `:1284` e `:829`, dove il secondo letterale sta in **coda** al suffisso
(`+ "% increase."`).

---

## La cinquantaduesima sessione

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** — nove spinte — e l'albero di lavoro è pulito. Si riparte da
`git fetch && git status -sb` e dalle otto verifiche d'apertura. La sessione si è
aperta su `DESKTOP-1O339MR` con `origin/fase-0` allineato: è la **nona prova** di
fila che il «cambio di terminale» annunciato in chiusura è solo un cambio di
finestra.

⚠️⚠️ **I valori cambiati, e uno strumento nuovo:**

    python scratchpad/nudi_en.py      atteso: struttura 1044 | da fare 473   (era 656)
    python scratchpad/triage_nudi.py  atteso: testo 271, sigla 87, dbg 93, spenta 22
    python scratchpad/tabelle_en.py   NUOVO: testo 7 tabelle e 73 voci, tutte in
                                      custom_ai.hsp — 6 fatte, 1 decisa, 0 da fare;
                                      sigla 2/6, numerica 2/22, jp 58/143

`toppe.jsonl` sale a **815** (di cui 10 `tutte` della 50ª più quelle nuove),
`rinviate.jsonl` resta a **43**. Tutto il resto è **fermo dov'era**: `pytest` 420
passed 6 skipped, `prova_identita` 72/72 e 27.813, `verifica --dizionario` 0 da
ritradurre ovunque e **124** non tradotte in `command.hsp`, `creature`
1131/2466/0/0, `larghezze` 0 su 75, `diario` 0 su 214, `riquadri` 0 su 38 e 0 su
71, `battute --divergenti` 13; `referti.py` 0 e 0, `return_en.py` 0 da fare.

✅ **`cgx-test.exe` rifatto nove volte** e già in `elonaplus2.31\`.

### ▶ Che cosa il collaudo ha detto, e che cosa resta da guardare

Il giocatore ha collaudato **il pannello dei ritocchi** e ha detto «tutto ok» tre
volte, dopo le correzioni. Verificato a schermo:

✅ Il pannello si apre col nome giusto («Ritocchi» anche dalla porta).
✅ Le 16 voci dei ritocchi di comodità stanno in una pagina senza sfondare.
✅ «Le magie attivano l'incantamento dell'arma» — era la riga più stretta (74
caratteri contro i 75 dell'inglese) e regge.
✅ Il tetto d'altezza delle descrizioni: **quattro righe**, misurato e non più
contato. `custom_tweaks.hsp:654` ne aveva cinque e la quinta finiva sotto la
barra dei comandi.
✅ I quattro menu che restavano (interfaccia, IA, gioco, vari), comprese le tre
descrizioni più larghe del pannello — 77, 76 e 75 colonne.

⚠️ **Il collaudo arretrato NON è stato fatto**, e la scaletta era pronta: le
cinque schermate della 47ª (ritratto/PCC con «Su misura» che compare solo su un
alleato, specchio, cambio di immagine, tono di voce, la riga d'aiuto «Dx,Sx
[Cambia]  Shift,Esc [Chiudi]»), la scheda dell'equipaggiamento riequipaggiando
l'arma, gli **88 ranghi** della 41ª (`F12` → wizard, poi iscriviti a arena, gilda
e museo) e il platino a quattro cifre nella barra di stato.

⚠️⚠️ **E adesso c'è un arretrato nuovo, tutto di oggi**: il pannello dell'IA
(`c` su un alleato), il **gioco di carte** — tavolo, carte, editor del mazzo,
premi — e le **nove scene dei figli**, che sono 271 righe di testo nuovo mai
viste a schermo. Le carte sono le più a rischio: il tetto è la **carta** (72 px),
non la finestra, ed è la misura più stretta di tutto il progetto.

### ▶ I lotti, e che cosa ha insegnato ciascuno

    la porta del pannello    1 voce    «Regolazioni» ≠ «Ritocchi»: il nome era fuori dal pannello
    (Ora: sfida fallita)     1 toppa   FAILED era «fallita», non «errore»
    le tre % in mezzo        3 toppe   l'unità di misura passa nella testa
    il cimitero DD           1 toppa   la finestra regge QUATTRO righe, non sei
    tabelle_en.py            —         il sesto punto cieco: 7 tabelle, 73 voci
    ai-tabelle              19 toppe   39 righe: le `tutte` coprono più schermate
    ai-menu                 28 toppe   e una correzione a una toppa di due ore prima
    ai-coda                  3 toppe   il menu d'importazione
    ai-sparse                6 toppe   la coda che il conteggio per routine non mostra
    tcg-carte               33 toppe   il tetto è la carta: 72 px, corpo 9, 15 caratteri
    tcg-tavolo              24 toppe   «identica» vuol dire identica coi tab davanti
    tcg-premi               15 toppe   il nome del gioco, e «amur-cage» reso per la prima volta
    event-figli             27 toppe   54 battute che non possono accordarsi col parlante

⭐ **Una toppa corretta due ore dopo averla scritta, ed è la regola giusta.**
L'intestazione della prima colonna del pannello IA diceva «Chi», che regge da
sola ma **non regge la voce di menu che ci si appoggia**: `:1692` dice «Cambia il
soggetto.», e «Cambia chi.» non è italiano. È la regola delle «due letterali per
riga» della 51ª vista da un altro lato: **due righe che parlano della stessa cosa
vanno decise insieme, anche quando stanno in routine diverse.**

💡 **Chiudere un file vuol dire guardarlo con TUTT'E DUE i referti.** Le dodici
righe sparse di `custom_ai.hsp` — otto «Back», un «Blank», un «Not Set», due
frasi — non le mostrava il riassunto per **routine**, perché stanno una per
routine e l'elenco è ordinato per numero decrescente. A trovarle è stato
`nudi_en`, che elenca per **file**: «82 righe, 12 ancora intatte».

### ▶ Il vocabolario fissato oggi, e da dove viene

    Gioco delle Ombre    il TCG          Yu-Gi-Oh! italiano, e il mod lo cita
    gabbia di Amur       amur-cage       mai reso prima in tutto il progetto
    Barra                Gauge           action.hsp:11476, buff.hsp:530, :845
    Potenziamento        Buff            la resa già data a «Boost»
    nucleo di transizione Shift Core     db_item.hsp:138463
    Soggetto/Condizione/Confronto/Valore/Azione   le cinque colonne dell'IA
    Vigilanza, Travolgere, Portata, Volo, Legame vitale   i nomi affermati delle carte
    Anticipo             First Strike    «Attacco improvviso» (18) sfonda di 20 px
    Raffica              Windfury        «Furia del vento» (15) arriva esatto al bordo
    Tocco letale         Deathtouch      tre caratteri di margine su «Tocco micidiale»
    Condanna             Deathword       «Parola di morte» (15) non ci stava
    Comune / Speciale    Good / Unique   i gradini che il gioco chiama common e special
    Allontanati/Avvicinati  Move (Away)/(Forward)  un verbo dove l'inglese ha la parentesi
    di adesso            Current         «corrente» è un calco
    Mazzo / Cimitero / Dominio / Pag.    il tavolo del gioco di carte

⚠️ **Due refusi di monte non ricalcati**: «severedly» per «severely»
(`tcg_custom.hsp:1556`), e «consecutive lethal game victory» al **singolare** con
un contatore davanti (`:1568`), che in italiano diventa «vittorie di fila in
partite mortali».

### ▶ Che cosa fare

1. ⭐⭐⭐ **Il collaudo di quel che è stato fatto oggi**, che è tutto arretrato:
   il pannello dell'IA, il gioco di carte (e lì il tetto è la **carta**), le nove
   scene dei figli. Più il collaudo vecchio che non è sparito — le cinque
   schermate della 47ª e gli **88 ranghi** della 41ª, il debito più antico.
2. ⭐⭐ **Le schermate grosse che restano.** `triage_nudi` le ordina: adesso le
   prime sono `item_func.hsp` **24** (`skipName` 13 + `itemname` 11),
   `proc.hsp:jump_changeCreature` **13**, `txtadv.hsp:adv_casinoSlots` **12**,
   `system.hsp:game_title` **10**, `custom_pet.hsp:PetOptionMenu` **9**,
   `command.hsp:com_charainfo_loop` **9**, `map_rand.hsp` **9**.
3. ⭐ **Le due incoerenze che restano**, che sono lavoro da dizionario:
   **fattura/bolletta** (la più urgente, il giocatore le incontra tutt'e due
   nella stessa mezza giornata) e **negromanzia/necromantica** (`skill.hsp:1492`
   contro tre siti). La terza — il nome del gioco di carte — è sciolta.
   Più quella vecchia: `db_item.hsp:135432` dice «borraccia filtrante»,
   `action.hsp:8267` dice «**bottiglia** filtrante».
4. ⭐ **Il referto che manca dalla 49ª**: uno che scorra le chiamate a
   `display_window` e misuri `s(1)` contro `(larghezza − 58 − 40) / 6,6`.
5. 💡 **E un sospetto da verificare, nato oggi e non misurato**: in
   `tcg.hsp:2804`-`:2810` ci sono sette righe della forma
   `if ( … ) { buff = "…" }`, cioè **assegnazione e condizione sulla stessa
   riga**, e `nudi_en` non le elenca. Se la forma è cieca davvero, è un settimo
   punto cieco che costa un pomeriggio misurare.

---

## La cinquantunesima sessione (per storia)

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** — nove spinte — e l'albero di lavoro è pulito. Si riparte da
`git fetch && git status -sb` e dalle otto verifiche d'apertura. La sessione si è
aperta su `DESKTOP-1O339MR` con `origin/fase-0` allineato: è l'**ottava prova**
di fila che il «cambio di terminale» annunciato in chiusura è solo un cambio di
finestra. ⚠️ Stavolta la chiusura lo dice davvero — *«riprendo in un altro
terminale»* — e vale come le altre sette: si vedrà all'apertura.

⚠️⚠️ **Quattro valori attesi sono cambiati e uno strumento è nuovo:**

    python scratchpad/nudi_en.py      atteso: struttura 1044 | da fare 656   (era 849)
    python scratchpad/triage_nudi.py  atteso: testo 454, sigla 87, dbg 93, spenta 22
    python scratchpad/return_en.py    NUOVO: 0 da fare, 2 decise, 35 toccate (4 residui),
                                             49 morfologia, 35 chiavi, 121 in tutto

`toppe.jsonl` sale a **660** (di cui **10 `tutte`**), `rinviate.jsonl` resta a
**43**. Tutto il resto è **fermo dov'era**: `pytest` 420 passed 6 skipped,
`prova_identita` 72/72 e 27.813, `verifica --dizionario` 0 da ritradurre ovunque
e **124** non tradotte in `command.hsp`, `creature` 1131/2466/0/0, `larghezze` 0
su 75, `diario` 0 su 214, `riquadri` 0 su 38 e 0 su 71, `battute --divergenti`
13; `blocchi_en.py` 99 e **54**, `referti.py` 0 e 0, `else_jp.py` 6.984 righe in
13 file, `rete8_dizionario.py` 3, `misura-blocchi-spenti.py` 4 e 5,
`variabili_en.py` 60 e 4, `perimetro.py` 57% e 42%, `cnv_str_en.py` 49 e 24,
`lang-nel-ramo-jp.py` 21 righe e 0 già rese.

✅ **`cgx-test.exe` rifatto sei volte** e già in `elonaplus2.31\` (l'ultimo dopo
le quattro righe fuori dai menu).

### ⚠️ Che cosa NON è stato fatto: il collaudo

⚠️⚠️ **Zero collaudo.** La 50ª si era chiusa dicendo che il giocatore aveva
provato tre volte in corsa; questa non ha aperto il gioco nemmeno una volta. Il
pannello intero — sette menu, 193 righe — è dentro `cgx-test.exe` e **non l'ha
mai visto nessuno**. 💡 La 49ª ha dimostrato che una sessione di solo collaudo
trova quel che nessuna lettura del sorgente trova: questa è l'opposto esatto, e
il debito è tutto da una parte.

I tre punti che meritano di essere guardati per primi, perché sono i soli dove il
conto potrebbe non tenere:

1. **Il suffisso col contatore** nel menu di difficoltà — « (Ora: 12 giorni di
   sopravvivenza)» — è l'unico posto dove la voce cresce a runtime.
2. **`custom_tweaks.hsp:654`** (il cimitero DD) è l'**unica descrizione su cinque
   righe** di tutto il pannello. Il conto dice che la finestra ne regge sei
   (`mes` parte da `wy + 343` su 448, cioè 105 px, a corpo 13), ma è un conto,
   **non una misura a schermo**.
3. **`:1293`** («Le magie attivano l'incantamento dell'arma») è la riga più
   stretta: 74 caratteri col suffisso, contro i **75 dell'inglese**.

### ▶ I sette lotti, e che cosa ha insegnato ciascuno

    menu dell'IA            14 righe   negromanzia, non «necromanzia»
    menu di difficoltà      14 righe   due letterali per riga (GetTStatusProgress)
    menu dei ritocchi vari  29 su 30   una riga lasciata in inglese apposta
    ritocchi extra          28 righe   il tetto non è «74», è «non peggiorare l'inglese»
    ritocchi di comodità    36 righe   sette righe nominano comandi che il gioco ha già
    ritocchi al gioco       69 righe   quasi solo rimandi da andare a prendere
    fuori dai menu           3 righe   la coda che il conteggio per schermata non vede

⚠️ **`:1679` «Nani?!» si lascia in inglese, ed è voluto.** È la descrizione della
«Modalità Ken il guerriero», e il motivo è lo stesso per cui la 50ª ha lasciato
«Sp 12/23»: **l'inglese non l'ha tradotta neanche lui**. Chi ha scritto il mod
aveva «What?!» e ha scelto il giapponese, perché la battuta *è* la citazione — e
in italiano la voce di menu il riferimento lo dà già. `triage_nudi` continuerà a
contarla fra le «da fare»: non è una dimenticanza.

### ▶ Il vocabolario fissato oggi, e da dove viene

Quasi niente è stato inventato: il lavoro è stato **andare a prendere** i nomi
che il gioco già usa, con `scratchpad/rende.py` (nuovo: cerca un frammento
inglese in tutto il dizionario e mostra come è stato reso).

    AI                  IA                        già dalla 50ª
    necromancy          negromanzia               db_item.hsp:139896
    Shadow Step         Passo d'ombra             skill.hsp:932
    Healing Rain        Pioggia curativa          skill.hsp:429
    Undead call/return  Raduna / Ritira i non-morti  text.hsp:2101, :2089
    Necro Fusion        Fusione dei morti         action.hsp:11702
    Necro Force         Forza necromantica        skill.hsp:1492 ⚠️ vedi l'incoerenza
    Party time!         Si balla!                 text.hsp:131
    Etherwind           Vento d'etere             text.hsp:46
    Elea (plurale)      gli Elea                  map.hsp:770
    Curtain Call        Chiamata alla ribalta     proc.hsp:4650
    Gauge Release       Forza liberata            custom_tweaks.hsp:1255
    Deep-Sea Castle     Castello del Drago a Nove Teste   map.hsp:8408
    sandbag             sacco da botte            action.hsp:10916
    Wetting / Dim       Idratazione / Stordimento text.hsp:64, :71
    burst / rapid ammo  munizioni a raffica / rapide  text.hsp:2472, :2484
    Impress             amicizia                  command.hsp:4196
    tag-team            coppia                    action.hsp:10861
    Feed / Give         Dai da mangiare / Dai qualcosa   command.hsp:5976, :5970
    Pickpocket/Mining   Borseggio / Scavo         action.hsp:7302, :7224
    Show House          Cupola delle Case         text.hsp:2848
    Devil Cape          Capo del Diavolo          text.hsp:2845
    HP / DV / Dojo      HP / DV / Dojo            non si traducono
    Abnormal            Abnormal                  command.hsp:10415 (anche il jp lo lascia)
    <Little Sister>     <Little Sister>           db_creature.hsp:124417

⭐ **Quattro parole nuove, tutte con un perché:**
- **«casella»** per il quadretto di mappa: nessuna resa del progetto aveva mai
  avuto bisogno di nominarlo, e serviva due volte.
- **«Ken il guerriero»** per «Fist of the North Star»: è il titolo italiano della
  serie, e tradurre alla lettera avrebbe perso proprio quel che la riga dice.
- **«Tutto deve sparire!»** per «Everything must go!»: la formula italiana dei
  saldi di liquidazione.
- **«sfondare i muri come un ariete»** per il **Kool-Aid Man**, che in Italia non
  conosce nessuno: si tiene l'immagine e si lascia cadere il nome.

⭐ **E due parole che sembravano da tradurre e non lo erano:**
- **«red book» è semplicemente «libro»**: `ITEM_ID_RED_BOOK` ha
  `ioriginalnameref = "book"` (`db_item.hsp:152478`). Il «red» è il colore dello
  sprite nel nome interno, non una parola che il giocatore legga.
- **«Split Monsters» non è il nome di una creatura**: sono le creature col bit
  `CHARA_BIT_SPLIT_*`, e il gioco annuncia quel che fanno con «si sdoppia!»
  (`chara_func.hsp:8751`).

### ▶ Che cosa fare

1. ⭐⭐⭐ **Il collaudo del pannello**, che è tutto arretrato: vedi i tre punti in
   cima. E con esso il collaudo vecchio, che non è sparito — gli **88 ranghi**
   della 41ª (il debito più antico) e le cinque schermate della 47ª
   (ritratto/PCC, specchio, cambio di immagine, tono di voce, evocazione dei PNG),
   più il **platino a quattro cifre** nella barra di stato.
2. ⭐⭐ **Le altre schermate grosse del punto cieco.** `triage_nudi --routine` le
   ordina, e adesso che `custom_tweaks.hsp` è chiuso le prime sono:
   `tcg.hsp` **46** (`tcgdrawcard` 33 + `tcg_drawInterface` 13, le parole chiave
   delle carte), `event.hsp:random_eventProc` **27** (le battute dei figli),
   `custom_ai.hsp` **~54** sparse in cinque routine (`AIMainMenu` 13,
   `AIConfigMenu` 11, `AITacticConfigMenu` 10, `PrintAIInfo` 7,
   `AITeachConfigMenu` 6) — ⭐ e lì «IA» e «IA personalizzata» sono **già
   decise**, la seconda proprio da questa sessione. Poi `item_func.hsp` 24
   (`skipName` 13 + `itemname` 11), `proc.hsp:jump_changeCreature` 13,
   `custom_pet.hsp` 17.
3. ⭐⭐ **Le tre incoerenze in cima**, che sono lavoro da dizionario e non da
   toppa. Quella di **fattura/bolletta** è la più urgente perché il giocatore le
   incontra tutt'e due nella stessa mezza giornata di gioco (il diario e
   l'inventario); quella di **negromanzia** è la più facile, perché è un'unica
   voce (`skill.hsp:1492`) contro tre.
4. ⭐ **Il referto che manca dalla 49ª**: uno che scorra le chiamate a
   `display_window` e misuri `s(1)` contro `(larghezza − 58 − 40) / 6,6`.
5. **L'incoerenza vecchia rimasta**: `db_item.hsp:135432` dice «borraccia
   filtrante», `action.hsp:8267` dice «**bottiglia** filtrante».

### ⚠️⚠️ Le sette cose che la prossima sessione deve sapere

1. ⭐⭐⭐ **Il tetto di larghezza non è «74 caratteri», è «non peggiorare
   l'inglese».** `custom_tweaks.hsp:1293` in inglese fa **già 75** caratteri sui
   74 del metro prudente, perché il suo suffisso di stato è « (Ora: tutte le armi
   indossate)». Bocciare la resa italiana lì avrebbe voluto dire chiedere
   all'italiano di stare dove l'inglese non sta. ✅ La regola scritta in
   `toppa-tweaks-extra.py` e `toppa-tweaks-gioco.py`: il tetto effettivo è
   `max(74, larghezza_inglese)`, e quando scatta lo **dice**. È la stessa cosa
   che la 50ª aveva scoperto a mano su `screen.hsp:1811`, messa nella forma.
2. ⭐⭐⭐ **Il suffisso di stato NON è uguale per tutte le voci.** `GetTStatus`
   (`custom_tweaks.hsp:417`-`:500`) ha rami dedicati per certi ritocchi e per
   tutti gli altri cade sul generico « (Ora: acceso)». Misurare ogni voce col
   suffisso peggiore in assoluto (32 caratteri) bocciava voci larghe la metà: il
   controllo va fatto **col ramo più lungo che quella voce può davvero
   prendere**.
3. ⭐⭐ **`he`, `his` e `him` hanno due rami, e solo uno è contenuto.** Dentro
   `if ( arg2 )` ogni `return` passa da `lang()` ed è già reso — «lui», «lei»,
   «il tuo», «il suo»; sotto, il ramo a un argomento solo restituisce l'inglese
   nudo — «it», «you», «he», «she». È esattamente la distinzione che
   `strumenti/funzioni.py` descrive a parole, ed è la ragione per cui i loro 15
   `return` nudi **non sono lavoro**: la resa italiana li toglie dal sito.
4. ⚠️⚠️ **Le toppe non saltano solo `accenti.py`: saltano anche la rete 11.**
   `proc.hsp:11481` è stato chiuso con una toppa che sostituisce
   `his2(tc) + your2(tc)` con `name(tc)`. Come **voce di dizionario** la rete 11
   l'avrebbe bocciata — `funzioni_di_contenuto` dà `['his2']` contro `['name']` —
   e come toppa è passata senza che nessuno la guardasse. La resa è giusta, ma
   nessuna guardia lo ha verificato.
5. ⚠️ **Una descrizione può stare su cinque righe, ma è la prima volta.**
   `custom_tweaks.hsp:654` ha dovuto prenderne una in più perché i tre nomi presi
   dal gioco («Ritira i non-morti», «Fusione dei morti», «Forza necromantica»)
   sono più lunghi delle abbreviazioni inglesi. Il conto dice che ce ne stanno
   sei; **il conto non è una misura**.
6. ⚠️ **CP932 non ha `«»`.** Misurato: le uniche virgolette alte che ci stanno
   (`“”`, `0x81 0x67`) sono a **doppia larghezza**, che `scratchpad/guardie.py`
   vieta. Dove l'inglese cita fra apici, l'italiano usa l'apostrofo semplice; per
   il parlato restano le virgolette dritte di `cnvtalk`, che sono l'unica forma
   scrivibile e sono italiano corretto.
7. 💡 **Quando l'inglese e il giapponese non concordano, e quando l'inglese
   sbaglia da solo.** «Wind God» è **una dea** — è Lulwy, che il progetto tratta
   al femminile dappertutto — e ricalcare l'inglese avrebbe cambiato sesso a un
   personaggio che il giocatore conosce. Stessa famiglia: `:835` diceva il
   contrario se tradotta di slancio, perché «revert the 4x exp bonus» vuol dire
   **togliere** il bonus, non rimetterlo.

---

## La cinquantesima sessione (per storia)

⭐⭐⭐ **Le toppe hanno imparato a dire «tutte le occorrenze», e ne erano
bloccate 125.** Su 717 righe di testo inglese nudo, **125 non erano raggiungibili
da nessuna toppa** — e non perché mancasse la resa: perché la schermata ripete sé
stessa e `applica_toppe`, giustamente, si ferma sull'ambiguità. Gli otto menu di
`custom_tweaks.hsp` hanno lo stesso titolo, le dodici schermate di creazione del
personaggio ripetono «Press F1 to show help.», `command.hsp:2901` (« Rank.») sta
identica nel diario e nella scheda. E il blocco non salvava: **le uniche righe
che distinguono i siti portano rese che il dizionario riscrive**, quindi un
blocco che le raggiunge aggancia il sorgente pinnato — come `test_toppe.py:104`
pretende — ma non aggancia più la build, dove le toppe girano davvero.
✅ `"tutte": true`, otto test nuovi (412 → **420**). ⚠️ **Non è un allentamento**:
l'ambiguità resta un errore per difetto (c'è un test che lo verifica sia senza il
campo sia con `false`), un `tutte` non booleano è un errore di caricamento, le
occorrenze sovrapposte non si contano due volte e la sostituzione va dall'ultima
alla prima, perché `sostituisci` può avere un numero di righe diverso da `cerca`.

⭐⭐⭐ **Tre difetti di misura di `nudi_en.py` in un giorno solo, e il terzo l'ho
lasciato aperto apposta.**
1. ✅ **`_PERCORSO` scartava ogni letterale con una barra rovesciata** — e le
   sequenze di a-capo e tabulazione ne portano una. Erano invisibili **tutte le
   descrizioni su più righe**: solo in `custom_tweaks.hsp` sono 75, cioè il
   pannello delle opzioni descritto voce per voce. Struttura 913 → 1038.
2. ✅ **`_ESTENSIONE` scartava ogni letterale con un nome di file dentro** —
   «Re-parse ItemList.txt.» è una voce di menu, non un percorso. Stessa cura: un
   nome di file è un **token**, non ha spazi dentro. 1038 → **1044**.
3. ⚠️ **`return "…"` dentro un `#defcfunc` non lo vede nessuno**, e sono **120
   righe** (`init.hsp` 56, `text.hsp` 35, `custom_tweaks.hsp` 29). **Non
   corretto**, e il motivo è che non sono tutte testo: i 35 di `text.hsp` sono
   chiavi di mappa (`"vernis"`, `"kapul"`, `"fighterguild"`), ma
   `init.hsp:155`-`:168` restituiscono i suffissi ordinali inglesi del `cnvrank`
   (`"st"`, `"nd"`, `"rd"`, `"th"`), che il giocatore legge. Serve una regola di
   forma che distingua, e improvvisarla a fine sessione sarebbe stato ripetere
   pari pari l'errore del punto 1.
💡 **La lezione è la stessa scritta per la quarta volta: un filtro si prova su
una riga che si è vista a schermo, non sul totale.** Tutt'e tre sono venuti fuori
traducendo, non misurando: la 49ª li aveva già incontrati con ` gp` e `Page.`.

⭐⭐ **Due volte l'inglese sbagliava e il giapponese aveva ragione, e a dirimere
è stato il sito d'assegnazione.**
- «Bandits Killed» conta le **bande**, non i banditi: `GDATA_FLAG_BANDITS_KILLED`
  cresce di uno per scontro (`action.hsp:2514`, i predoni travolti con la nave;
  `quest.hsp:718`, l'incarico contro i ladri respinto), come dice
  「潰した盗賊団**の数**」. → «Bande di banditi sgominate».
- «Max Arena Streak» non è una serie: `quest.hsp:675` incrementa a **ogni**
  vittoria e non azzera mai, come dice 「アリーナ**総勝数**」. ⚠️ Il nome della
  costante (`HIGHEST_ARENA_STREAK`) è d'accordo con l'inglese ed è sbagliato
  quanto lui — la lezione n. 2 della 49ª che si ripresenta identica.
💡 **Quando inglese e giapponese non dicono la stessa cosa, il giudice è chi
assegna il campo.** Costa una ricerca e non sbaglia.

⭐⭐ **Un rinvio aveva scritto da sé quando sarebbe scaduto, ed è scaduto oggi.**
`command.hsp:3067` («Total Platinum») portava un letterale nudo *e* una `lang()`
sulla stessa riga, che la regola della 46ª vieta. La firma era già in
`rinviate.jsonl` da una sessione passata, col motivo che finiva: «*si sblocca il
giorno in cui qualcuno traduce il ramo `else`, che è lavoro da toppa e non da
dizionario*». Quel giorno era oggi, e non è servito toccare niente.
💡 **È l'opposto esatto della toppa dell'orso della 49ª**: là una toppa teneva
una **copia congelata** di una resa che stava altrove ed è scaduta in silenzio;
qui un rinvio dipendeva da un **fatto verificabile** e ha aspettato in ordine.
La regola che ne esce vale in tutt'e due i versi: **quel che dipende da un valore
copiato marcisce, quel che dipende da un fatto no.**

---

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** — undici spinte — e l'albero di lavoro è pulito. Si riparte da
`git fetch && git status -sb` e dalle otto verifiche d'apertura. La sessione si è
aperta su `DESKTOP-1O339MR` con `origin/fase-0` allineato: è la **settima prova**
di fila che il «cambio di terminale» annunciato in chiusura è sempre e solo un
cambio di finestra.

⚠️⚠️ **Tre valori attesi sono cambiati e uno strumento è nuovo:**

    python -m pytest strumenti/tests      atteso: 420 passed, 6 skipped   (era 412)
    python scratchpad/nudi_en.py          atteso: struttura 1044 | da fare 849
    python scratchpad/blocchi_en.py       atteso: struttura 99 | da fare 54  (era 68)
    python scratchpad/triage_nudi.py      NUOVO: testo 647, sigla 87, dbg 93, spenta 22

`toppe.jsonl` sale a **467** (di cui **10 `tutte`**), `rinviate.jsonl` resta a
**43**. Tutto il resto è **fermo dov'era**: `prova_identita` 72/72 e 27.813,
`verifica --dizionario` 0 da ritradurre ovunque e **124** non tradotte in
`command.hsp`, `creature` 1131/2466/0/0, `larghezze` 0 su 75, `diario` 0 su 214,
`riquadri` 0 su 38 e 0 su 71, `battute --divergenti` 13; `referti.py` 0 e 0,
`else_jp.py` 6.984 righe in 13 file, `rete8_dizionario.py` 3,
`misura-blocchi-spenti.py` 4 e 5, `variabili_en.py` 60 e 4, `perimetro.py` 57% e
42%, `cnv_str_en.py` 49 e 24, `lang-nel-ramo-jp.py` 21 righe e 0 già rese.

✅ **`cgx-test.exe` rifatto sette volte** e già in `elonaplus2.31\`.

### ▶ Che cosa è stato chiuso, e che cosa il collaudo ha detto

Il giocatore ha collaudato **tre volte in corsa** e ha detto «tutto ok» tre volte:
il piede dell'inventario, la barra di stato, il diario.

✅ **Il piede dell'inventario** — `17 oggetti`, `30 oro`, `Pag. 1/3` e `Pag.1/2`
in tutte e tre le finestre a scorrimento (`showscroll`, `display_window2`,
`display_window`).
✅ **La barra di stato** — `12345 oro`, `30 pt.`, gli otto effetti di campo, la
battaglia navale, il sacco da allenamento, la resa in arena, la Chiamata alla
ribalta. **18 righe su 23**: `Sp` e `Lv` restano per misura, `"PF"` perché è una
sigla di cui il sorgente non dice il significato, e le due spie di *wizard mode*
perché non sono testo di gioco.
✅ **Il diario (`j`)** — 54 righe: il conto delle bollette (con le cinque voci
incolonnate a nove caratteri: Totale, Personale, Immobili, Tasse, Totale) e le
quaranta voci della «Cronaca delle avventure». Più `command.hsp:3067` col rinvio
già pronto, e ` Rank.` chiuso dopo con la prima toppa `tutte`.
✅ **Il pannello dei ritocchi** — il menu principale, le intestazioni di **tutti e
otto** i menu (otto toppe `tutte`) e il primo menu di dettaglio, più il suffisso
di stato che sta accanto a **ogni** voce del pannello.

### ▶ Il vocabolario fissato oggi, che vale per le 647 righe che restano

    tweak            ritocco          «Impostazioni» era già del menu di
                                      configurazione (command.hsp:17285, :17538)
    AI               IA               mai reso prima in TUTTO il progetto
    toggle           accende e spegne l'italiano non ha il verbo in una parola
    (Currently: X)   (Ora: X)         più corto, e «ora» è quel che dice
    Off / On         spento / acceso  la coppia di «accende e spegne»
    Disabled         disattivato      l'inglese distingue Off da Disabled
    tracker          «osservate»      participio: mai reso prima, e inventare un
                                      sostantivo tecnico sarebbe stato peggio
    stamina          SP               buff.hsp:735, item_data.hsp:613
    gp / gold        oro              command.hsp:3677, text.hsp:193 (strgold)
    pp (barra)       pt.              solo lì: « platino» non ci sta in 62 px
    Page / Page.     Pag. / Pag.      text.hsp:114 rende già «[Page]» «[Pagina]»

⭐ **E sei nomi di effetto di campo erano già decisi altrove**: la barra deve dire
quel che dice il libro degli incantesimi — «Gabbia elettromagnetica»
(`skill.hsp:1812`), «Mondo di fili» (`:1820`), «Giardino violento» (`:1704`),
«Frantumaroccia» (`:1824`), «Teatro impazzito» (`text.hsp:2372`), «Chiamata alla
ribalta» (`proc.hsp:4650`). ⚠️ L'unico senza gemello era `[Reprimand Room]`:
懲罰**結界** è una barriera magica, non una stanza → «[Barriera punitiva]», che
segue il giapponese e non l'inglese, che si era inventato la «Room».

### ▶ Che cosa fare

1. ⭐⭐⭐ **Finire il pannello dei ritocchi**, che adesso è la strada in discesa:
   il vocabolario è fissato, le intestazioni sono chiuse e il suffisso di stato
   pure. Restano **190 righe in sei menu**: `GameplayTweakMenu_loop` **69**,
   `ConvenienceTweakMenu_loop` 36, `MiscTweakMenu_loop` 30,
   `GameplayExtraTweakMenu_loop` 28, `AITweakMenu_loop` 14,
   `ChallengeTweakMenu_loop` 14. Il modello è `scratchpad/toppa-tweaks-ui.py`.
2. ⭐⭐ **La regola di forma per i `return`**, cioè il debito dichiarato del punto
   3 in cima. Prima lo strumento che misura, poi la traduzione: è la stessa
   richiesta che la decisione del 2026-08-10 faceva per i letterali nudi, e che
   `nudi_en.py` ha evaso nella 49ª. ⚠️ Il caso su cui provarla è
   `init.hsp:155`-`:168`: i suffissi ordinali `"st"`/`"nd"`/`"rd"`/`"th"`, che
   sono testo vero e in italiano non hanno un equivalente scrivibile in CP932
   (niente `º`) — quindi lì la domanda non è solo «si vede?», è «che cosa ci si
   mette?».
3. ⭐⭐ **Le altre schermate grosse del punto cieco**: `tcg.hsp` 46 (le parole
   chiave delle carte, `tcgdrawcard` 33 + `tcg_drawInterface` 13),
   `event.hsp:random_eventProc` 27 (le battute dei figli), `custom_ai.hsp` ~60
   («Tactical Instructions», dove «IA» è già deciso), `chara.hsp` 26 (le
   schermate di creazione del personaggio: «Press F1 to show help.» ×12 e «Gene
   from » ×12, **tutt'e due sbloccate da `tutte`**).
4. ⭐ **Il referto che manca ancora dalla 49ª**: uno che scorra le chiamate a
   `display_window` e misuri `s(1)` contro `(larghezza − 58 − 40) / 6,6`.
5. **L'incoerenza vecchia**: `db_item.hsp:135432` dice «borraccia filtrante»,
   `action.hsp:8267` dice «**bottiglia** filtrante».
6. ⚠️ **E il collaudo arretrato non è sparito**: restano gli **88 ranghi** della
   41ª (il debito più vecchio) e le cinque schermate della 47ª (ritratto/PCC,
   specchio, cambio di immagine, tono di voce, evocazione dei PNG). ⚠️ Da
   guardare col resto: il **platino a quattro cifre** nella barra di stato —
   `9999 pt.` sono 8 caratteri, cioè 53 px col metro stretto e **62** con quello
   largo, e 62 è esattamente lo spazio fino al bordo dello schermo.

### ⚠️⚠️ Le sette cose che la prossima sessione deve sapere

1. ⭐⭐⭐ **`tutte` si dichiara dove serve, non per comodità.** In
   `custom_tweaks.hsp` `"Go back."` ha **tre forme** — `listn(0, 15)`,
   `listn(0, 31)`, `listn(0, listmax - 1)` — e solo l'ultima è ripetuta: le
   prime due sono toppe normali. E in ogni copione di toppa `tutte` va messo un
   controllo che **conti le occorrenze e pretenda il numero atteso**
   (`toppa-command-rank.py` è il modello): `tutte` non è una scusa per non
   guardare, è una decisione presa dopo aver guardato.
2. ⭐⭐⭐ **Una toppa può disambiguare solo con righe che il dizionario non
   tocca.** È il motivo per cui `tutte` è dovuta nascere, ed è una regola
   generale: il `cerca` deve agganciare **il sorgente pinnato e la build
   insieme**, e ogni riga tradotta che entra nel blocco rompe la seconda metà.
   Nei copioni di questa sessione il controllo è scritto:
   `if build[riga - 1] != originale: raise`.
3. ⭐⭐ **La larghezza di una schermata si misura sulla `config.txt` vera e poi
   si ricontrolla alla minima.** Per la barra di stato i numeri veri sono
   `clockW. 120` e `windowW. 1920`; il conto è stato rifatto a **800**, che è il
   minimo che il gioco accetta, e lì «[Gabbia elettromagnetica]» finisce a 319 px
   e la «Chiamata alla ribalta» a 693. ⚠️ E si è scoperto che
   `screen.hsp:1811` **in inglese sfonda già da solo** a 800: l'italiano, più
   corto, lo rimette dentro. Non tutto quel che sfora è colpa della traduzione.
4. ⭐⭐ **Quando il giapponese e l'inglese non concordano, si guarda chi assegna
   il campo** — vedi il riquadro in cima. E ⚠️ **il nome della costante non è una
   prova**: `HIGHEST_ARENA_STREAK` è d'accordo con l'inglese ed è sbagliato
   quanto lui. Stessa regola per cui la classe `dbg` di `triage_nudi.py` guarda
   il **prefisso** `dbg_` e non «il nome sa di sviluppatore»: `*dump_chara`
   contiene «superb», «great», «good», «bad», «hopeless», cioè testo vero.
5. ⚠️ **E la regola `dbg_` ha il suo punto cieco, misurato:** `screen.hsp:1125` e
   `:1128` (`"*debug*"`, `"loop…sub…"`) escono solo con `GDATA_WIZARD == 1` ma
   stanno dentro `screen_drawStatus`, che di suo è la barra vera. Il triage le
   chiama `testo` e sbaglia a favore del lavoro. **Il debug guardato da una
   variabile invece che da una routine non si vede.**
6. ⚠️ **Le toppe non passano da `accenti.py`.** È l'unica strada per cui un testo
   italiano arriva al sorgente senza degradazione automatica: nei copioni
   l'apostrofo si scrive **a mano** (`piu'`, `abilita'`, `comodita'`) e ogni
   copione di questa sessione controlla `nuova.encode('cp932')` prima di
   scrivere. ⚠️ E niente `º`: «il 1º del mese» non si può scrivere, si scrive
   «il 1 del mese».
7. 💡 **Una riga che si legge sempre vale più di dieci che si leggono una volta.**
   Le sei toppe del piede dell'inventario e le due della barra di stato sono
   otto righe in tutto, e sono la cosa che il giocatore ha visto per prima. Il
   diario sono 54 righe in una schermata che si apre col tasto `j`. Il criterio
   che ha guidato la sessione è questo, e `triage_nudi.py --routine` serve
   proprio a trovarlo: **il testo non è sparso, sta in blocchi, e un blocco è una
   schermata sola.**

---

## La quarantanovesima sessione (per storia)

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** — sei spinte: la lista di collaudo, la sua correzione,
`nudi_en.py`, le due correzioni del collaudo, il referto stretto, `il tiro`, più
questa chiusura — e l'albero di lavoro è pulito. Si riparte da
`git fetch && git status -sb` e dalle otto verifiche d'apertura. La sessione si è
aperta su `DESKTOP-1O339MR` con `origin/fase-0` allineato: è la **sesta prova**
di fila che il «cambio di terminale» annunciato in chiusura è sempre e solo un
cambio di finestra, mai un cambio di macchina.
⚠️ **Un valore atteso è cambiato e uno è nuovo**: `dizionario/skill.hsp.jsonl` e
`dizionario/text.hsp.jsonl` hanno una resa corretta ciascuno, e **`nudi_en.py`
entra nei referti con 913 e 872**. Tutto il resto è **fermo dov'era**:
`verifica --dizionario` dice «command.hsp: 0 da ritradurre, **124** non ancora
tradotte», `toppe.jsonl` resta a **314** (le due dell'orso sono state
**riscritte**, non aggiunte) e `rinviate.jsonl` a **43**; `perimetro.py` 57% e
42%, `variabili_en.py` 60 e 4, `cnv_str_en.py` 49 e 24,
`misura-blocchi-spenti.py` 4 e 5, `lang-nel-ramo-jp.py` 21 righe e 0 già
tradotte, `blocchi_en.py` 99 e 68, `else_jp.py` 6.984 righe in 13 file,
`rete8_dizionario.py` 3.
⚠️ Il modello per `assembla-lotto.py` resta **`scratchpad/modello-rete6.py`**; i
lotti `037`-`041` restano quelli a zero rinviate da cui copiare.
✅ **`cgx-test.exe` rifatto tre volte** (l'ultimo 16/08, **03:17**) e già in
`elonaplus2.31\`.

### ▶ Che cosa il collaudo ha detto

Il salvataggio è in `save-backup\pre-collaudo-20260816-49a` (202 file). La lista
completa, con i numeri di riga e i tetti accanto a ogni voce, sta in
**`scratchpad/collaudo-49a.md`**: si riparte da lì, non da capo.

✅ **Verificato e a posto** — il **menu delle capacità** (`a`): titolo, colonne
`Nome`/`Costo`/`Effetto`, e la riga di aiuto da **73 su 76**. Il **menu `i` su un
alleato**: venti voci, la più lunga «Metti fra gli indispensabili» = **28 su 29**,
nessuna tagliata. Il riquadro **«Combat Rolls»** (`c`): la toppa della 47ª tiene,
si legge `Mira 64%` con lo spazio. **`Parti:`** coi nomi degli slot — `Mano Mano
Tiro Dardi`. **` (per terra)`** e **` (tiro)`**. La **bacheca degli incarichi**.

⚠️ **Non raggiunte, e ognuna col suo motivo** — la colonna **«Rottura guardia»**
(serve la capacità «Istruzione individuale», che il personaggio non ha); la
**creatura-carta** (il `<Cambia valore>` vuole il ritratto `xy2pic(18, 35)`, che
assegna solo `proc.hsp:20179`, cioè «Forza del poker» a 50 di barra: **non è una
schermata da un tasto**); il **jukebox** (è un oggetto, non un arredo di città);
il **` pz.`** dei due banchi (Miral, Stoke).

💡 **Quel che si vede in inglese e NON è un difetto**, misurato riga per riga:
- `(Light)` viene da `cnveqweight` in `screen.hsp` — **file senza dizionario**;
- `You change your equipment.` è `main.hsp:3089`, **dentro una `lang()` regolare**:
  `main.hsp` non ha dizionario;
- `Autopickup` è `screen.hsp:1004`, stessa storia;
- `un black claws` è **già censito** dalla decisione del 2026-08-10: 261
  `iknownnameref` di `db_item.hsp`, i nomi degli oggetti non identificati. È
  l'articolo italiano (`un `) che si incolla a un nome inglese;
- gli incarichi della bacheca sono `event.hsp`, 649 voci;
- `Informazioni` manca dal menu `i` perché `command.hsp:6146` lo riserva a
  `develop | GDATA_WIZARD` **e ai non-alleati**;
- la **voce vuota in cima al menu delle capacità** è un fuori-di-uno di monte, non
  nostro: il ciclo è `repeat MAX_SKILL - STARTING_SKILL_SPACT` con `cnt` da **0**,
  quindi tocca lo slot **600**, che non ha costante, né nome, né costo (le 276
  `SKILL_SPACT_*` vanno da 601 a 876, senza buchi, tutte con `skillname`). Su un
  personaggio normale `spact(0)` è 0; su questo, che è `*debug*`, è 1. Costruzione
  e disegno del menu sono **identici byte per byte** fra build e sorgente.

### ▶ Che cosa fare

1. ⭐⭐⭐ **Il triage di `nudi_en.py`.** 913 righe di struttura sono un numero
   grezzo: va spaccato in *testo che il giocatore legge* e *dato*. I grossi sono
   `command.hsp` 213, `custom_tweaks.hsp` 183, `custom_ai.hsp` 64, `tcg.hsp` 50,
   `system.hsp` 72. ⚠️ Le più visibili sono le sei di stanotte (` items`, ` gp`,
   `Page`/`Page.`): si leggono a **ogni** apertura d'inventario e vogliono una
   **toppa**, perché nessun dizionario le raggiunge.
2. ⭐⭐ **Le cinque zone che restano in `command.hsp`**, cento firme: 10000-10999
   (30), 8000-8999 (29), 16000-16999 (26), 11000-11999 (13), 9000-9999 (2).
   ⚠️ Prima di aprirne una, le due verifiche di sempre: `lang-nel-ramo-jp.py` e
   **guardare se la zona taglia una famiglia**.
3. ⭐⭐ **Oppure un file nuovo, e adesso si sa quali pesano.** Misurato stanotte,
   fuori dai 19 dizionari attuali (su 72 file) restano **10.465 siti `lang()` in
   34 file**: `chat.hsp` **4.762** (il 45% del residuo), `db_card.hsp` 2.308,
   `trait.hsp` 406, **`main.hsp` 381**, `item_func.hsp` 274, `chara.hsp` 274,
   `item.hsp` 243, `config.hsp` 219, `map_user.hsp` 204, `blend.hsp` 181,
   `txtadv.hsp` 170, `material_data.hsp` 118, `god.hsp` 114, `screen.hsp` 104.
   💡 `material_data.hsp` resta il ventesimo dizionario più economico, ma
   **`main.hsp` (381) e `screen.hsp` (104) sono quelli che il collaudo ha visto
   in faccia**: il messaggio d'equipaggiamento e la colonna di stato.
4. ⭐ **Il referto che manca ancora**: uno che scorra le chiamate a
   `display_window` e misuri `s(1)` contro `(larghezza − 58 − 40) / 6,6`.
5. ⭐ **La toppa a `command.hsp:17658`**, già misurata: «Elona Version 3.03» come
   letterale dove il giapponese usa `VERSION_STRING`. ⚠️ Rinvio **insieme** alla
   toppa.
6. **L'incoerenza vecchia**: `db_item.hsp:135432` dice «borraccia filtrante»,
   `action.hsp:8267` dice «**bottiglia** filtrante».
7. ⚠️ **E il collaudo non è finito**: restano gli **88 ranghi** della 41ª (il
   debito più vecchio) e le cinque schermate della 47ª (ritratto/PCC, specchio,
   cambio di immagine, tono di voce, evocazione dei PNG).

### ⚠️⚠️ Le sette cose che la prossima sessione deve sapere

1. ⭐⭐⭐ **Una toppa che ricopia una resa che sta altrove è già scaduta.** Vedi il
   riquadro in cima. La forma giusta è **ricavare** il valore dalla voce di
   dizionario da cui dipende e mettere una rete che fermi lo script se cambia:
   `scratchpad/toppa-chara_func-orso.py` è il modello.
2. ⭐⭐⭐ **`INV_ITEM_IDENTIFY_LEVEL` non è un livello di identificazione**, e in
   generale **i nomi del decompilatore non sono un'autorità**. `command.hsp:15321`
   lo mette a `100` quando scegli di portare nel **Tiro** un'arma che potrebbe
   stare in Mano: è un flag di slot. Ci ho creduto una volta e ho dato
   un'istruzione di collaudo sbagliata. 💡 Il modo di controllare costa una
   ricerca: **si guarda chi assegna il campo**, non come si chiama.
3. ⭐⭐ **Quando due voci di un menu non si accordano, si guarda quale delle due è
   LIBERA prima di decidere in che direzione accordarle.** `txtsetequipw`
   (`text.hsp:2498`-`:2505`) offriva «la mano» e «tiro». L'ovvio era `Mano`/`Tiro`,
   come `bodyn` e come la domanda appena sopra — ma `:2500` condivide la firma
   (`jp=手`, `en=hand`) con `_melee(0, 0)` e `_melee(0, 6)`, dove «la mano» è la
   parte del corpo delle frasi d'attacco. ⚠️ E **non si poteva nemmeno toppare**:
   una toppa aggancia il sorgente pinnato (`test_toppe.py:104`), il dizionario
   riscrive quella riga prima, e il rinvio che la libererebbe è **per firma** e si
   porterebbe dietro i due `_melee` — che hanno tre `lang()` per riga. ✅ Accordata
   l'altra, che ha firma unica: `tiro` → **«il tiro»**.
4. ⭐⭐ **Una descrizione va scritta nel registro della sua colonna, non
   dell'inglese.** `skill.hsp:1561` era l'unica delle venticinque alla terza
   **plurale** («Uniscono le forze sulla serratura»). L'inglese («Join forces to
   break the lock») non ha persona e non poteva far da guida; la colonna aveva già
   scelto ventiquattro volte, e `:1549` («Legge insieme agli alleati») era il caso
   gemello. ✅ «**Unisce** le forze sulla serratura».
5. ⭐⭐ **Il registro delle cause di morte è senza genere, e non per caso.** Tutte
   e venticinque («morì in una trappola», «cadde in cenere», «si tolse la vita»)
   evitano il participio perché il morto può essere di qualunque sesso. La resa
   nuova dell'orso lo rispetta: «morì fra le zanne di un orso».
   ⚠️ E l'**ordine** delle due `cnv_str` è incrociato apposta: «lo sbudellatore» è
   prefisso di «lo sbudellatore marmocchio» e `cnv_str` aggancia il primo
   riscontro, quindi la riga del sorgente con l'orso adulto prende la chiave del
   cucciolo. Stesso criterio di `fix_wish` (`module.hsp:4805`): forme lunghe prima.
6. ⚠️ **Tre errori miei dentro `nudi_en.py`, tutti trovati misurando.** Il
   marcatore di colore `@BL` va tolto **prima** di cercare la parola, o «`@BL` più
   giapponese» passa per inglese. Le chiavi di config sono in camelCase, quindi il
   corpo dev'essere `[A-Za-z]` — ma **l'iniziale dev'essere minuscola**, o il
   filtro si mangia `"Page."`, che è testo vero. E la regola delle estensioni
   scritta `^\.?[a-z]{2,4}$` si mangia **ogni** parola corta e minuscola: la prima
   a sparire è stata `" gp"`. 💡 Un filtro si prova su una riga che si è **vista a
   schermo**, non solo sul totale.
7. ⚠️ **`cerca` di una toppa può essere una LISTA** (le toppe su più righe): non è
   hashabile, e un `in` su un insieme di chiavi esplode. Va scartata con
   `isinstance(..., str)` prima del confronto.
   💡 **E la disciplina «componi, codifica, poi apri» ha pagato di nuovo**: lo
   script è morto proprio lì, e `toppe.jsonl` non è stato toccato.

---

## La quarantottesima sessione (per storia)

### I riquadri della 48ª

⭐⭐⭐ **Tre zone chiuse e 119 voci in sei lotti** — la 14000-14999, la 5000-5999 e
la 3000-3999, cioè le tre più dense che restavano. L'inventario e il banco del
negozio, i regali a un alleato, il menu delle capacità, il menu che si apre con
`i` su un personaggio, la bacheca degli incarichi. `command.hsp` passa da 243
firme da fare a **124**, cioè dall'81% al **90%** del file; le voci rese sono
**1.180 su 1.304**. Catena verde fino in fondo, `cgx-test.exe` rifatto (16/08,
**01:40**). ⚠️ **Restano cinque zone e cento firme**: 10000-10999 (30),
8000-8999 (29), 16000-16999 (26), 11000-11999 (13) e 9000-9999 (2).

⭐⭐⭐ **La scoperta della sessione corregge un numero che la 47ª aveva scritto
come corretto: `sizefix` NON è zero.** Il collaudo della 47ª aveva stabilito che
`12 + sizefix - en * 2` valesse **10** «con `sizefix` assente da `config.txt` e
quindi 0». Ma in `config.txt` c'è, **dieci righe sotto** il `font2. "Courier New"`
che quella stessa sessione aveva letto:

    config.txt:84   fontSfix1.  "1"     fixes font size
    config.hsp:180  cfgRead "fontSfix1.", sizefix = int(rtvaln)
    config.hsp:436  sizefix = 0     <- solo nel ramo GIAPPONESE

Il ramo inglese (`config.hsp:439`) non lo azzera: `sizefix` resta **1**, il corpo
è **11** e fa **6,6 px** a carattere. Né 10 né 6.
✅ **Nessuna resa già spedita ne esce sbagliata** — l'unico tetto che la 47ª aveva
ricavato dal corpo 10 è quello di 「命中」, 27 px, che fa 4 caratteri tanto a 6 px
quanto a 6,6, e «Mira» ne fa 4.
⚠️ **Ma cambia il tetto di tre funzioni di `module.hsp`** che usano quella stessa
riga di `font`: la riga di aiuto di `display_window` (`:4342`), `display_topic`
(`:4365`) e `display_note` (`:4359`). La formula giusta è
**`(larghezza − 58 − 40) / 6,6`**: per una finestra da 380 fa **42** caratteri e
non 39, per una da 600 ne fa **76** e non 69.
💡 E la decisione della 47ª su `:11849` **resta giusta lo stesso**, perché la resa
ovvia faceva 44 caratteri e sfora anche i 42 veri.

⭐⭐⭐ **E la seconda scoperta è un errore mio, che vale più della prima.** Le sei
stringhe di `CDATAN_NEWSEX` (`command.hsp:3639`-`:3654`) le ho analizzate da capo,
ho ricostruito con cura perché non si possono tradurre, e ho scritto un **rinvio**
con tanto di motivo. Il motivo era giusto e la mossa sbagliata: `invariati.md` ha
dal **2026-08-07** una sezione intitolata «Valori di dato, non testo — tradurli
rompe i salvataggi» che nomina **per riga** proprio `command.hsp:3639-3654`, e
`text.hsp:123` ha già in dizionario `en='male'` con `it='male'`. Quelle sei erano
**chiuse da nove mesi**: mancava la riga in dizionario, non una decisione.
✅ **La regola che ne esce: prima di scrivere il motivo di un rinvio, si cerca il
valore in `invariati.md`.** Un rinvio resta aperto per sempre e ritorna a galla a
ogni sessione; un invariato dichiarato chiude.

### ▶ Il punto in cui si riprendeva allora (48ª)

Tutto è **spinto** — sette spinte, una per lotto, una per la chiusura e una per
questa nota — e l'albero di lavoro è pulito. Si riparte da
`git fetch && git status -sb` e dalle otto verifiche d'apertura. La sessione si è
aperta su `DESKTOP-1O339MR` con `origin/fase-0` allineato: è la **quinta prova**
di fila che il «cambio di terminale» annunciato in chiusura è sempre e solo un
cambio di finestra, mai un cambio di macchina.
⚠️ **E anche questa si chiude annunciandone uno** (16/08/2026, sempre da
`DESKTOP-1O339MR`): è la **quinta volta di fila** che una sessione lo dichiara.
`hostname` accanto al `git fetch` lo dice in un secondo, e finora ha sempre detto
la stessa cosa.
⚠️ **Quattro valori attesi sono cambiati**: `verifica --dizionario` dice
«command.hsp: 0 da ritradurre, **124** non ancora tradotte» (100 da fare più le
24 rinviate, che non cambiano); il dizionario di `command.hsp` ha **1.180** voci;
`toppe.jsonl` resta a **314** e `rinviate.jsonl` a **43** — questa sessione non ne
ha aggiunta nessuna delle due. Tutto il resto è fermo dov'era: `perimetro.py`
**57%** e **42%**, `variabili_en.py` 60 e 4, `cnv_str_en.py` 49 e 24,
`misura-blocchi-spenti.py` 4 e 5, `lang-nel-ramo-jp.py` 21 righe e 0 già tradotte,
`blocchi_en.py` 99 e 68, `else_jp.py` 6.984 righe in 13 file,
`rete8_dizionario.py` 3.
⚠️ Il modello per `assembla-lotto.py` resta **`scratchpad/modello-rete6.py`**. Dei
lotti nuovi, `037`, `038`, `039`, `040` e `041` sono a zero rinviate e tengono
l'ancora `RINVIATE = set()`, quindi possono fare da modello; il `042` no.

### ▶ Che cosa il collaudo ha già detto

⚠️ **Questa sessione non ha collaudato niente.** Vale ancora, parola per parola,
il riquadro omonimo della 47ª qui sotto: il salvataggio è al sicuro in
`save-backup\pre-collaudo-20260815-47a`, `config.txt` ha `language. "1"`, la
scheda dell'equipaggiamento è verificata, e **restano da rifare** le due etichette
di «Combat Rolls» con l'eseguibile nuovo.
⚠️⚠️ **E adesso le rese mai viste a schermo sono 1.180**, cioè tutte. Le 119 di
stanotte sono le più esposte, perché **quattordici sono etichette di menu o di
colonna con un tetto calcolato e mai guardato**.

1. ⭐⭐⭐ **La cosa da fare è il COLLAUDO, e stavolta con una lista precisa.**
   Sei schermate coprono quasi tutte le rese nuove a rischio, e si aprono con un
   tasto sola:
   - **`i` su un alleato** — il menu di interazione, undici voci nuove in cima a
     trentacinque già spedite: «Parla», «Attacca», «Di' quello che provi»,
     «Dai/Ricevi qualcosa», «Dai da mangiare». ⚠️ Il tetto è **29 caratteri**
     (`:6172`, riquadro da 275 px) e la voce più lunga già spedita ne fa 28: se
     una riga esce tagliata, il posto dove guardare è quella.
   - **`i` su una creatura-carta** (guerriero di picche, piuma di fiori, occhi di
     quadri, strega di cuori, o un Jolly Variabile) — «<Cambia valore>» e le
     quattro «[Cambia in …]». ⚠️ E premendo la prima deve uscire «Quale valore?»,
     non «Quale rango?»: è la correzione di stanotte.
   - **l'inventario** (`i` da terra, o un contenitore) — «Parti:» nel riquadro
     dell'equipaggiamento, « (per terra)» e « (tiro)» in coda al nome, e al banco
     delle medagliette la colonna « pz.».
   - **il menu delle capacità** (il tasto delle abilità speciali) — «Capacità»,
     «Nome / Costo / Effetto», e soprattutto la **riga di aiuto in fondo**, che è
     la misura più a rischio della sessione: **73 caratteri su 76**.
   - **l'elenco dei PNG** (dalla scheda degli alleati, e col tasto che cambia
     colonna) — «Informazioni», «Paga», «Assunzione (paga)», «Rottura guardia»,
     «Sanguinamento», e la riga «Lv.10 male(25)», che vive in **19 caratteri**.
     ⚠️ Il sesso resta in inglese ed **è atteso**: vedi il punto 4.
   - **la bacheca degli incarichi** e **il jukebox** — «Incarichi in bacheca», i
     simboli `$`, «Elenco dei brani», «Titolo».
   ⭐ E poi restano i **debiti vecchi**: gli 88 ranghi della 41ª, e le cinque
   schermate che la 47ª aveva lasciato da guardare (ritratto/PCC, specchio,
   cambio di immagine, tono di voce, evocazione dei PNG).
2. ⭐ **Oppure le cinque zone che restano in `command.hsp`**, cento firme in
   tutto: 10000-10999 (30), 8000-8999 (29), 16000-16999 (26), 11000-11999 (13),
   9000-9999 (2). ⚠️ Prima di aprirne una, le due verifiche che stanotte hanno
   pagato tutt'e due: `lang-nel-ramo-jp.py` (le 11 righe morte di `command.hsp`
   stanno tutte in 2954-3016, quindi ormai fuori strada) e **guardare se la zona
   taglia una famiglia** — nella 5000-5999 la tagliava, e al rovescio.
3. ⭐⭐ **Oppure il referto che manca, e adesso è più facile di ieri.** La 47ª ne
   chiedeva uno sulle sottotitolature di `display_window`, e stanotte la formula
   del tetto è diventata giusta: `(larghezza − 58 − 40) / 6,6`. Un referto che
   scorra le chiamate a `display_window` e misuri `s(1)` contro quel tetto
   troverebbe subito i casi come quello del menu delle capacità, che sta dentro
   per **tre caratteri**. ⭐ L'altro, di cui la 46ª aveva chiesto, resta un
   `coda_en.py` per i letterali inglesi concatenati **fuori** dalla parentesi di
   una `lang()`.
4. ⚠️⚠️ **E c'è una famiglia che il collaudo vedrà in inglese e NON va
   «aggiustata»: il sesso dei personaggi.** «male», «female», «male?», «female?»,
   «none», «hermaphrodite» restano inglesi nel menu del desiderio, nell'elenco
   dei PNG e nella scheda. È una decisione della Fase 0 scritta in `invariati.md`:
   quel valore è **salvato nel personaggio** e riletto come operando in
   `init.hsp:1813`-`:2008`, cioè dentro `he()`, `his()` e `him()`. Per portarlo a
   schermo in italiano servono delle **toppe** che separino la chiave salvata
   dall'etichetta mostrata, in **tutti** i siti di stampa insieme
   (`command.hsp:3640`-`:3655`, `:4653`-`:4656`, `:17834`, `init.hsp:2085`) — ed è
   lavoro suo, non di un lotto. `text.hsp` ne ha già sei di quelle toppe.
5. ⭐ **Oppure `material_data.hsp`**, 117 voci di cui 27 nomi già decisi in
   `glossario.md`: resta il candidato più economico al ventesimo dizionario su 54.
6. **Oppure `item_func.hsp` (263), il « of » di ogni cadavere**, col nodo
   grammaticale che la 42ª ha lasciato aperto.
7. ⭐ **Oppure la toppa a `command.hsp:17658`**, già misurata e a buon mercato: il
   rapporto del personaggio dichiara **«Elona Version 3.03»** come letterale dove
   il giapponese usa `VERSION_STRING`. ⚠️ La voce va **rinviata** insieme alla
   toppa, perché una toppa e una resa non stanno sulla stessa riga.
8. ⚠️ **E resta l'incoerenza vecchia da correggere**: `db_item.hsp:135432` chiama
   l'oggetto «borraccia filtrante», `action.hsp:8267` scrive «Hai riempito
   d'acqua la **bottiglia** filtrante». È materiale da `correzione-*.py`.

### ⚠️⚠️ Le nove cose che la prossima sessione deve sapere

1. ⭐⭐⭐ **`sizefix` vale 1, e il corpo di quella famiglia è 11.** Vedi «I riquadri
   della 48ª» qui sopra. La formula `12 + sizefix - en * 2` compare in **decine** di righe
   (`blend.hsp`, `chara.hsp`, `chat.hsp`, `command.hsp`, `module.hsp`…): ovunque
   fa 11, cioè **6,6 px** a carattere. ⚠️ E il posizionamento di monte usa `* 7`
   (`module.hsp:4349`, `:4360`, `:4372`, `command.hsp:14352`): upstream calcola le
   coordinate con **sette** pixel e ne disegna **6,6**, quindi il testo posato a
   destra deriva sempre un po' verso sinistra e quello allineato a destra sfora di
   un pixel ogni cinque caratteri. È un margine, non un errore.
   💡 **La lezione vera è la stessa del collaudo della 47ª, ed è successa due
   volte di fila: il corpo va letto sulla riga.** Stavolta anche `config.txt` va
   letto per intero, non fino alla riga che serviva.
2. ⭐⭐⭐ **Prima di scrivere il motivo di un rinvio, si cerca il valore in
   `invariati.md`.** Vedi «I riquadri della 48ª» qui sopra. `invariati.md` è lungo 539 righe e
   ha **cinque sezioni**, e quella che conta qui — «Valori di dato, non testo» —
   sta a riga 405, cioè fuori dalla prima schermata. ⚠️ Il segnale che avrebbe
   dovuto fermarmi c'era ed era in `verifica.py:57`: il commento che spiega perché
   le sezioni si classificano nomina **«le otto stringhe di `CDATAN_NEWSEX`, che
   devono restare inglesi per non rompere i salvataggi»**. L'avevo letto e non
   l'avevo visto.
3. ⭐⭐ **La rete 4 sa una cosa che l'inglese nasconde: quando due rami hanno lo
   stesso giapponese, a distinguerli è il CODICE, non il testo.** `:14272` e
   `:14275` sono 「 枚」 tutt'e due, e l'inglese ci mette «Coins» e «Tickets» perché
   il ramo `invctrl(1)` è diverso. Ma la distinzione la porta già **l'intestazione
   della colonna** (`:14105` «Medagliette», `:14108` «Biglietti»), disegnata a
   `wx + 526` sopra quegli stessi numeri. ✅ Resa unica, « pz.», che è anche
   l'unica forma che regge il valore **1**. È la stessa lezione di `:7818`/`:7828`
   nel lotto 036.
4. ⭐⭐ **Una zona può tagliare una famiglia AL ROVESCIO: la coda già spedita e la
   testa ancora da fare.** Il menu che si apre con `i` va da `:5952` a `:6068`;
   trentacinque voci da `:6002` in giù erano rese da una sessione precedente, e le
   undici in cima erano rimaste indietro perché stanno sotto il confine della
   zona. ⚠️ Il danno di non accorgersene sarebbe stato **decidere una larghezza
   già decisa**. Il segnale costa niente: se una voce è un `promptAdd`, si cerca
   dove finisce la sequenza e dove sta il suo `val = promptx, prompty, …`.
5. ⭐⭐ **`larghezze.py` misura SOLO `text.hsp`, e solo le voci scritte
   `s(cnt) = lang(…)`** (`larghezze.py:68` e `:78`). Un menu costruito con
   `promptAdd` in un altro file non lo vede nessuno. ✅ Ma il metro è lo stesso e
   sta nel sorgente: `command.hsp:6172` chiude la sequenza con
   `val = promptx, prompty, 275, 1`, e `(275 − 46) / 7,7` fa **29 caratteri**.
   💡 **E il tetto aveva tenuto senza che nessuno lo misurasse**: delle
   trentacinque voci già spedite la più lunga ne fa 28. Adesso sono 46 e nessuna
   sfora.
6. ⭐⭐ **La rete 11 nella forma stretta è comparsa DUE volte in una sera, e va
   riconosciuta a vista.** `command.hsp:14852` è `his(tc) + " inventory is full."`
   e `:5892` è `"… to " + him(tc) + "? "`: in tutt'e due il giapponese ha
   `name(tc)` e l'inglese **non ha nessuna funzione di contenuto**, perché
   `his`/`him` a **un** argomento sono morfologia (`funzioni.py:78`). La resa non
   può nominare nessuno. ✅ E siccome la voce è tipata **dinamica**, va scritta
   come espressione — un letterale fra virgolette — o la rete 12 la ferma.
7. ⭐⭐ **La rete 8 non è una regola di stile: è la forma di ogni frase con
   `name()`.** Misurato su tutto il dizionario: le rese che mettono una
   preposizione davanti a `name()` sono **zero**, perché `name()` per il giocatore
   è «il viandante», cioè un sintagma **con l'articolo**. ✅ Quando serve dire «a
   X», la frase gira sul ricevente: `:15250` lo faceva già — «name(tc) + " riceve "
   + itemname(ci, 1) + "."» — e `:14874` e `:14980` l'hanno ricopiato.
8. ⭐ **Quando due sessioni divergono su una parola, vince quella che INSEGNA la
   cosa.** 「ランク」 è il numero di una carta: `proc.hsp:20184` è la frase che
   spiega il Jolly Variabile e dice già «puoi cambiarne **seme e valore**», mentre
   `command.hsp:6770` diceva «Quale **rango**?» — e «rango» in quello stesso file è
   già il grado dell'avventuriero (`:4192`, `:4194`). ✅ Corretto con
   `scratchpad/correzione-rango-carta.py`: adesso le tre stringhe che si rimandano
   l'una all'altra dicono la stessa parola.
9. ⭐ **Tre coppie di frasi sono state scritte «sulla forma» di frasi già spedite,
   e non è la stessa cosa che riusarle.** Le tre battute della sete (`:14799`)
   avevano lo stesso giapponese di `action.hsp:8274` e si sono **ricopiate**; le
   tre della fame (`:14741`) non avevano precedente e sono state scritte una per
   una accanto alle prime — «Non riesci a mangiare altro.» / «Non riesci a bere
   altro.», «La pancia sta per scoppiarti...» / «La vescica sta per scoppiarti...»,
   «Non hai ancora fame.» / «Non hai ancora sete.». 💡 «Cercare prima di scrivere»
   serve anche quando non c'è niente da riusare: serve a riusare il **registro**.

---

## La quarantasettesima sessione (per storia)

### ▶ Il punto in cui si riprendeva allora (47ª)

Tutto è **spinto** — nove spinte: una per ciascuno dei tre lotti della prima
metà, una per la prima chiusura, una per la correzione di `variabili_en.py`, una
per i tre lotti della zona 7000-7999, una per la seconda chiusura, una per la
toppa nata dal collaudo e questa nota — e l'albero di lavoro è pulito. Si
riparte da `git fetch && git status -sb` e dalle otto verifiche d'apertura. La
sessione si è aperta su `DESKTOP-1O339MR` con `origin/fase-0` allineato: il
cambio di terminale annunciato dalla 46ª non ha fatto danni, ed è la **quarta
prova** di fila della stessa cosa.
⚠️ **E anche questa si chiude annunciandone uno** (16/08/2026, sempre da
`DESKTOP-1O339MR`): è la quarta volta di fila che una sessione lo dichiara, e
finora è stato sempre e solo un cambio di finestra. `hostname` accanto al
`git fetch` lo dice in un secondo.
⚠️ **Sei valori attesi sono cambiati**: `verifica --dizionario` dice
«command.hsp: 0 da ritradurre, **243** non ancora tradotte» (219 da fare più
**24** rinviate); `rinviate.jsonl` ha **43** righe; `toppe.jsonl` ne ha **314**
(erano 312: le due del collaudo); `perimetro.py` dice **57%** e
**42%**; `variabili_en.py` dice **60 variabili e 4 trappole in 4 siti** (diceva
66 e 3, e guardava male). Tutto il resto è fermo dov'era:
`cnv_str_en.py` 49 e 24, `misura-blocchi-spenti.py` 4 e 5,
`lang-nel-ramo-jp.py` 21 righe e 0 già tradotte, `blocchi_en.py` 99 e 68,
`else_jp.py` 6.984 righe in 13 file, `rete8_dizionario.py` 3.
⚠️ Il modello per `assembla-lotto.py` resta **`scratchpad/modello-rete6.py`**. I
lotti `031`, `033`, `034`, `035` e `036` sono a zero rinviate e tengono l'ancora
`RINVIATE = set()`, quindi possono fare da modello; il `032` no.

### ▶ Che cosa il collaudo ha già detto

⭐⭐ **Il collaudo si è fatto**, il primo da sei sessioni, e va letto prima di
rifarlo da capo. Il salvataggio è al sicuro in
`save-backup\pre-collaudo-20260815-47a` (186 file), `config.txt` ha
`language. "1"` — se fosse `0` girerebbe il ramo giapponese e non si vedrebbe una
riga di italiano — e l'eseguibile buono è quello delle **00:29 del 16/08**, cioè
**dopo** la toppa.

✅ **Verificato e a posto** — la **scheda dell'equipaggiamento** (`w`): la colonna
delle parti (`bodyn` più `Mano*`), le intestazioni «Parte/Nome» e «Peso», il
titolo, e soprattutto la riga del peso, che misura **53 caratteri sui 75 di
tetto**. Era il campo che avevo dato per più stretto di tutti, e ha ventidue
caratteri di margine.
💡 `(Medium)` resta in inglese ed **è atteso**: viene da `cnveqweight` in
`screen.hsp`, uno dei quaranta file senza dizionario. Non è un difetto della 47ª.

⚠️⚠️ **Trovato e corretto** — nel riquadro «Combat Rolls» della scheda del
personaggio (`c`) due etichette si saldavano al valore: «Mira64%» e «Pot.
magia100%». Vedi il punto 14. **Da rifare** con l'eseguibile nuovo: deve
leggersi «Mira 64%» e «Pot. magia 100%», con lo spazio.

⚠️ **E il collaudo ha corretto anche un mio conto**: avevo scritto che
l'etichetta di 「命中」 girava a corpo 12, e invece `com_skill_calcAttack:12424`
la mette a **corpo 10** (`12 + sizefix - en * 2`, con `sizefix` assente da
`config.txt` e quindi 0). Sei pixel per carattere, non 7,2. Le altre misure della
sessione restano buone perché usano il corpo 12 giusto, ma **il corpo va letto
sulla riga, non dato per scontato**.

⚠️ **Restano da guardare** le cinque schermate che nessuno ha ancora aperto: il
menu del **ritratto/PCC** (`c` poi `p`), quello dello **specchio** (uno specchio
su un alleato), il **cambio di immagine**, il **tono di voce** e l'**evocazione
dei PNG**. Sono quelle dei punti 1 e 2 dell'elenco qui sotto.
💡 **E le righe d'attacco non compaiono aprendo la scheda**: le disegna
`*show_weaponStat`, che gira solo quando si equipaggia o si toglie qualcosa in
uno slot **mano** (`:12806` e `:14781`). Riequipaggiare l'arma prova in un gesto
solo le righe d'attacco, il messaggio «Ti togli …» e gli avvisi sul peso.

1. ⭐⭐ **Ancora `command.hsp`, e adesso la zona più densa è 14000-14999 (50)**,
   poi 5000-5999 (35), 3000-3999 (34), 10000-10999 (30), 8000-8999 (29),
   16000-16999 (26) e 11000-11999 (13). ⚠️ Prima di aprire una zona nuova,
   `lang-nel-ramo-jp.py` come sempre — le 11 righe morte di `command.hsp` stanno
   tutte in 2954-3016 e sono già rinviate.
   ⚠️⚠️ **E prima di aprirla, guardare se la zona TAGLIA una famiglia.** Questa
   sessione ci è inciampata: il lotto 031 non segue la zona ma la famiglia,
   perché «Done    », «Category» e la riga di aiuto dei tre menu dell'aspetto
   sono ancorate a `:11825`-`:11852`, cioè **fuori** dalla 12000-12999. Chi
   avesse aperto la sola zona avrebbe reso sette etichette di una colonna
   lasciandone fuori la prima, e la larghezza si decide su tutte insieme.
   💡 Il modo di accorgersene costa niente: se una voce della zona è un'etichetta
   di menu, si cerca la firma della prima voce dello stesso `s = ...`.
   ⚠️ **E la 14000-14999 comincia proprio con una di quelle**: `:14127` e
   `:14136` sono le due occorrenze dell'intestazione delle resistenze già
   rinviata in questa sessione, e `:14120` è un `display_topic` accanto a un
   `display_topic s`. Vale la pena guardare `:14115`-`:14165` prima di scegliere
   i confini.
   ⭐ **E 3000-3999 (34) ha ancora il lavoro che aspetta**: `:3639` e `:3651` sono
   i due confronti su `CDATAN_NEWSEX` di cui parlava la 46ª.
2. **Oppure PROSEGUIRE il collaudo**, che stanotte è cominciato e si è fermato
   dopo due schermate — ma quelle due hanno già prodotto una toppa. Restano
   **1.061 rese** mai viste a schermo, 947 dalle sessioni prima più le 114 di
   stanotte. ⚠️ Gli **88 ranghi** della 41ª restano il debito più vecchio.
   💡 Quel che è già stato verificato sta nel riquadro «▶ Che cosa il collaudo ha
   già detto» qui sopra: si riparte da lì, non da capo.
   ⭐ **Della seconda metà valgono soprattutto tre scene**, tutte facili da
   raggiungere: il **congedo di un dio** (evocalo con un desiderio e poi
   rimandalo a casa — otto battute diverse, una per divinità); la **raccolta dei
   pezzi** da un alleato, dove si vede se la distinzione «a forza» arriva a
   schermo; e il **menu del tono di voce**, che è l'unico posto dove si legge la
   riga di aiuto da 54 caratteri su 55 di tetto.
   ⭐⭐ **E stanotte il collaudo è diventato più urgente di prima, perché sei
   delle rese nuove sono LARGHEZZE calcolate e mai viste.** Tutte e sei si aprono
   con un tasto solo e vanno guardate insieme:
   - il menu del **ritratto/PCC** (`*com_portrait_loop`): le etichette devono
     stare a dieci colonne e i numeri devono incolonnarsi. Le righe da guardare
     sono «Ritratto», «Col.cap.» e soprattutto **«Su misura»**, che compare solo
     aprendo la scheda **su un alleato**;
   - il menu dello **specchio** (`*com_mirror_loop`, «Parti da nascondere»): qui
     «On»/«Off» si saldano all'etichetta senza spazio, quindi si legge se esce
     «Mantello Off» o «MantelloOff»;
   - il menu del **cambio di immagine** (`*com_shape_change`): la riga
     «usa:Pic_ 123»;
   - la **riga di aiuto** in fondo a tutt'e tre — «Dx,Sx [Cambia]  Shift,Esc
     [Chiudi]» — che è la misura più a rischio di tutte;
   - la **scheda dell'equipaggiamento** (`*com_wear`): le righe d'attacco
     «Arma1 / Lotta / Tiro» con «Mira» accanto alla percentuale, e la riga del
     peso in basso a destra;
   - il messaggio di **demolizione di un edificio** sulla mappa del mondo, che è
     l'unico posto dove si vede se il registro del log regge una frase da 120
     caratteri.
3. ⭐ **Oppure il referto che manca, e adesso se ne conoscono DUE.** Il primo è
   quello che la 46ª aveva già chiesto: un `coda_en.py` che cerchi i letterali
   inglesi concatenati **fuori** dalla parentesi di una `lang()`.
   ⭐⭐ Il secondo è nato stanotte: un referto sulle **sottotitolature di
   `display_window`**, cioè le righe di aiuto che stanno in `s(1)`.
   `larghezze.py` non le vede — guarda solo `text.hsp` e solo i menu che passano
   da `*prompt_key` — e il tetto è calcolabile dai parametri della finestra
   (`larghezza - 58 - 40`, diviso 7,2). ⚠️ **Il caso che lo motiva non è teorico**:
   l'inglese di `:11849` sta a 38 caratteri su 39, e la resa italiana ovvia ne
   avrebbe fatti 44. Nessuna guardia se ne sarebbe accorta.
4. ⭐ **Oppure `material_data.hsp`**, 117 voci di cui 27 nomi già decisi in
   `glossario.md`: resta il candidato più economico al ventesimo dizionario su 54.
5. **Oppure `item_func.hsp` (263), il « of » di ogni cadavere**, col nodo
   grammaticale che la 42ª ha lasciato aperto.
6. ⭐ **Oppure la toppa a `command.hsp:17658`**, già misurata e a buon mercato: il
   rapporto del personaggio dichiara **«Elona Version 3.03»** come letterale dove
   il giapponese usa `VERSION_STRING`. ⚠️ La voce va **rinviata** insieme alla
   toppa, perché una toppa e una resa non stanno sulla stessa riga.
7. ⚠️ **E resta l'incoerenza vecchia da correggere**: `db_item.hsp:135432` chiama
   l'oggetto «borraccia filtrante», `action.hsp:8267` scrive «Hai riempito
   d'acqua la **bottiglia** filtrante». È materiale da `correzione-*.py`.

### ⚠️⚠️ Le quattordici cose che la prossima sessione deve sapere

1. ⭐⭐⭐ **Il carattere del ramo inglese è monospaziato, e questo trasforma ogni
   «ci starà?» in una sottrazione.** `config.txt` dice `font2. "Courier New"`;
   a corpo 12 (`12 + sizefix - en * 2`) un carattere fa **7,2 px**, a corpo 14 ne
   fa 8,4. Da lì il tetto di un campo si legge nel sorgente, non a occhio: si
   prendono i due `pos` che lo delimitano e si divide.
   ✅ Le cinque misure di stanotte, tutte fatte così: **111 px** fra il testo di
   `cs_list` (`module.hsp:129`, `wx + 64`) e la freccia destra (`wx + 175`);
   **46 px** fra `s(1)` (`:12429`, `wx + 422`) e i dadi del danno (`:12452`,
   `wx + 468`); **27 px** fra l'etichetta di 「命中」 (`wx + 590`) e la percentuale
   (`wx + 617`); **282 px = 39 caratteri** per la riga di aiuto di
   `display_window` (larghezza − 58 − 40); **75 caratteri** per `display_note`
   (`module.hsp:4360`, `ww - strlen * 7 - 140`).
   ⚠️ **E l'inglese non è il budget, per la stessa ragione di `larghezze.py`**:
   «Unarmed» sfora la sua colonna di sette pixel, la riga di aiuto usa 38
   caratteri su 39, la riga del peso arriva esatta a 75. Tre campi su cinque
   sono già al limite di monte.
   ⭐ **E il tetto ha un'eccezione che è una regola**: nel menu del ritratto le
   righe **senza valore** non hanno tetto stretto, perché `:12136` appende il
   numero solo `if ( rtval >= 0 )` e `*portrait_item:11356` dà `rtval = -1` a
   «Set Detail». È per questo che upstream ha potuto scriverci dieci caratteri
   dove le altre ne hanno otto. **L'imbottitura serve alle righe che portano un
   numero, e solo a quelle.**
2. ⭐⭐ **`verifica` sapeva una regola che io non avevo, ed è più stretta della
   mia.** `verifica.py:440` rifiuta una statica il cui inglese finisce con uno
   spazio e la cui resa no, perché quello spazio è la **giuntura** col pezzo che
   segue. Ha fermato due rese che riempivano tutte le colonne senza lasciarne una
   vuota in fondo.
   ⚠️ **E la ragione è più forte di come la guardia la racconta**: nel menu del
   ritratto lo spazio lo aggiunge il codice (`s += " " + rtval(2)`), ma nello
   specchio **no** — `:12333` è `s += "On"`, nudo. Una regola che vale in un menu
   e non nell'altro è una regola che si dimentica.
   ✅ Da qui in avanti, in questa famiglia: **ogni etichetta finisce con almeno
   uno spazio**, e il testo utile è una colonna in meno di quelle disponibili.
   È per questo che 「髪の色」 è «Col.cap.» e non «Col.capel.».
3. ⭐⭐⭐ **Quando la rete 3 accusa, la domanda non è «chi ha ragione»: è «in che
   MESTIERE stava la resa che cita».** Le righe d'attacco di `*show_weaponStat`
   sono il caso puro: 「武器」 la rete 3 lo dava reso «armi» (`text.hsp:59`), 「格闘」
   «Arti marziali» (`skill.hsp:161`), 「射撃」 «Mira» (`skill.hsp:387`) — ma il
   primo lì è una **categoria d'inventario**, gli altri due sono **nomi di
   abilità**, e qui sono tutt'e tre **etichette di riga** larghe sei caratteri.
   ✅ **A sciogliere il nodo è stato un quarto sito**: `buff.hsp:679`, dove
   「射撃力上昇/命中率上昇」 è già reso «Tiro e **mira**». Lì i due termini compaiono
   **affiancati**, cioè nella stessa opposizione di questa colonna: quindi 射撃 è
   «Tiro» e 命中 è «Mira», e `skill.hsp:1277` («+mira» per 命中率上昇) conferma.
   💡 **La lezione**: tre rese su quattro divergono dalla rete 3, e non perché la
   rete sbagli — perché il sito che cita faceva un altro mestiere. Il modo di
   decidere non è il gusto: è **cercare il sito dove i due termini stanno
   insieme**, che è quello che li ha già dovuti distinguere.
4. ⭐⭐ **Un lotto segue la FAMIGLIA, non la zona, e la zona può tagliare a
   metà.** Il lotto 031 sta in 11825-12297 perché i tre menu dell'aspetto
   condividono tre firme — «Done    » (`:11825`), «Category» (`:11852`) e la riga
   di aiuto (`:11849`) — e le prime occorrenze stanno **prima** del confine della
   zona che avevo aperto. ⚠️ Il danno di non accorgersene non è un errore di
   traduzione: è una **colonna decisa a metà**, con sette etichette a una
   larghezza e l'ottava, resa un mese dopo, a un'altra.
   💡 Il segnale c'è ed è a buon mercato: quando una voce della zona è
   un'etichetta di menu (`s = lang(...), lang(...), ...`), si guarda dove è
   ancorata la **prima** `lang()` di quella riga.
5. ⭐⭐ **Una riga può essere morta in TUTTI i siti in cui è scritta, e a dirlo è
   una barra.** 「火 冷 雷 闇 幻 毒 獄 音 神 沌 魔」 compare quattro volte in
   `command.hsp` — `:12636`, `:12645`, `:14127`, `:14136` — e tutte e quattro
   stanno dentro un commento di blocco: le prime nell'`ORIGINAL`, le seconde
   nell'`ANNA CUSTOM`, **spento anche lui**.
   ⚠️ **E la differenza fra un blocco acceso e uno spento è un carattere solo**:
   `:12639` è `/********** ANNA CUSTOM - BEGINNING ********** // Show skills on
   'z' toggle`, **senza la barra finale**, e a chiuderlo è
   `********** ANNA CUSTOM - ENDING **********/`. Dove il blocco è vivo il
   marcatore porta la barra da tutt'e due i lati e apre e chiude sulla stessa
   riga, come `:12673` e `:14118`. A occhio i due casi sono identici.
   ✅ **La rete 6 corretta nella 45ª ha fatto esattamente il lavoro per cui era
   stata corretta**, e stavolta l'ho provato invece di dirlo: tolto il rinvio, il
   lotto si ferma con «rete 6: riga 12636 sta dentro un commento di BLOCCO».
   💡 A disegnare davvero le resistenze è MMAH (`:12672`,
   `display_show_resist`): le due versioni di monte sono state **sostituite**,
   non spente per sbaglio. ⚠️ Se un giorno servisse rendere quell'intestazione,
   il posto è dentro `display_show_resist`, e il vincolo sarà che le undici sigle
   restino di **due caratteri con uno spazio in mezzo**, perché i valori sotto si
   incolonnano su quel passo.
6. ⭐⭐ **L'inglese butta via un avviso che protegge il salvataggio**, ed è la
   sesta famiglia di errore di monte incontrata su questo file.
   `:12955` in giapponese è 「本当にこの建物を撤去する？（注意！建物と中の物は完全に
   失われます）」; in inglese è **«Really remove this building?»**, la domanda senza
   la parte che conta. E quel che segue non torna indietro: `:12963` azzera
   l'area, `:12964` licenzia i lavoranti, `:12967` **salva**.
   ✅ È una statica, nessun contratto di funzioni: la resa segue il giapponese,
   come `:4764` nella 46ª. ⭐ **E il registro c'era già**: `map.hsp:1297` è la
   stessa specie — una conferma distruttiva con l'avviso fra parentesi — resa
   «Vuoi reinizializzare questa mappa? (Attenzione: …)», **222 caratteri già
   spediti**. Cioè: la forma «Vuoi …? (Attenzione: …)» è quella di casa, e il
   registro del log regge frasi di quella lunghezza. Non c'era niente da
   inventare.
7. ⭐⭐ **`init.hsp:1704` decide la persona di ogni frase del gioco, e va saputo
   una volta per tutte.** `name()` per il giocatore non è «tu»: è **«il
   viandante»**, un sintagma di **terza persona**. Quindi una frase che interpola
   `name(cc)` si scrive in terza e regge identica sul compagno; una frase che
   dice «You …» **senza** funzioni si scrive in seconda, che è quel che il
   progetto fa da sempre (`action.hsp:3255`, «Usi anche il passe-partout»).
   💡 Le due persone possono convivere nello stesso lotto — nel 033 lo fanno — e
   non è un'incoerenza: a decidere non è il tono, è **se c'è o no una funzione**.
8. ⚠️⚠️ **E c'è un difetto di monte che la rete 11 non lascia correggere, scritto
   qui perché al collaudo sembrerà un errore di traduzione.** `:12804` è «You
   unequip …», seconda persona — ma `*com_wear` si apre **anche su un alleato**,
   e lo dimostra `:12795`, che di `cc` fa il soggetto con `name(cc)`. Togliere
   l'elmo al compagno fa dire al gioco «Ti togli l'elmo».
   ✅ Correggerlo vorrebbe `name(cc)`, cioè **una funzione che l'inglese non ha**:
   è la rete 11, e qui non lascia scampo. La resa resta in seconda persona come
   l'inglese. ⚠️ Chi lo trovasse a schermo non deve «aggiustarlo» nel dizionario:
   se mai, è materiale da toppa, e allora la voce va rinviata.
9. ⭐⭐⭐ **`variabili_en.py` non vedeva la forma che ACCUMULA, ed è la forma che
   conta di più.** Fino a stanotte il referto prendeva solo `nome = "testo"`.
   Ma `nome += "testo"` non azzera: **aggiunge**, ed è così che si compone una
   frase inglese a pezzi. `command.hsp:7716`-`:7721` carica in `s` sei aggettivi
   di rango — `"Bad "`, `"Common "`, `"Skilled "`, `"Professional "`,
   `"Legendary "`, `"Well-Known "` — ognuno dentro un `if ( … ) { … }` su una riga
   sola, e `:7724` li stampa dentro la `lang()` dell'evocazione.
   ✅ Corretto: il conto passa da **66 variabili e 3 trappole** a **60 e 4**. Col
   `+=` sono arrivati anche i nomi di file che `system.hsp` compone a pezzi
   (`"spells.s1"`), che passavano perché `.s1` non era nell'elenco delle
   estensioni scritto a mano: adesso c'è `_ESTENSIONE`, che li prende per
   **forma** invece che per nome. Provato: scarta 56 letterali, **tutti** nomi di
   file o indirizzi web, nessuna prosa.
   💡 **La lezione è la stessa della 45ª su `cnv_str_en.py`, e adesso è successa
   due volte**: un referto che non ha mai trovato niente in una famiglia non è
   una prova che la famiglia sia pulita. E in tutt'e due i casi il caso è saltato
   fuori **leggendo il sorgente**, non rilanciando lo strumento.
   ⭐ **Che farne resta aperto.** La resa di `:7724` segue il giapponese, che non
   nomina niente — è il precedente della 38ª per `studybuddy`. Il rango si
   recupererebbe con **sei toppe** su `:7716`-`:7721`, e la regola della 46ª non
   lo vieta (righe diverse dalla resa). ⚠️ Ma prima va sciolto un nodo: quegli
   aggettivi stanno **davanti a un nome che scrive il giocatore**, di genere
   ignoto, e «Leggendario Anna» è sbagliato quanto l'inglese.
10. ⚠️⚠️ **In `*wish` il `txt` PRECEDE il suo `characreate`, e chi legge al
    contrario attribuisce ogni battuta al dio sbagliato.** A `:4490` c'è
    «Miaomiaomiaaa!» e a `:4493` `characreate CREATURE_ID_EHEKATL`; a `:4497` la
    battuta arrogante e a `:4500` `LULWY`. L'errore sarebbe invisibile: otto
    battute plausibili, tutte in bocca a qualcun altro.
    ✅ **La prova è `:4547`**, 「きゅー♪」: letta all'indietro sarebbe di **Jure**,
    mentre `:4550` crea la `QUANTUM_CREATURE` — ed è la forma di vita quantistica
    a fare «Quu», come la 46ª aveva già scritto fra le divergenze volute.
    💡 Serve ogni volta che si riscuote un registro dal lotto 028, cioè ogni
    volta che parla un dio.
11. ⭐⭐ **`name()` non sta MAI dopo una preposizione, ed è la ragione per cui
    certe frasi italiane suonano storte finché non si capisce.** `init.hsp:1704`
    rende `name(CHARA_PLAYER)` **«il viandante»**, cioè un sintagma **con
    l'articolo**: «da il viandante» e «a il viandante» sono sgrammaticati, e la
    preposizione non si può fondere a scrittura perché l'articolo non si conosce
    (per un alleato `name()` può essere «Anna», «un cane», «il gattino»).
    ✅ Quindi `name()` o è **soggetto** («X perde un osso») o segue un **verbo**
    («uccidere X», «Hai rimandato a casa X»). È la rete 8, ed è il motivo per cui
    le undici frasi della raccolta non dicono «estrai un osso **da** X», che
    sarebbe l'italiano ovvio.
    💡 E il corollario che fa risparmiare tempo: **gli accordi si spostano sulla
    cosa**, mai su `name()`. «strappato» va con «osso», «strappata» con «pelle»,
    e il genere di chi subisce non entra mai in gioco.
12. ⭐⭐ **Il secondo membro della famiglia `coda_en` è comparso, e stavolta è
    lui a far sforare la riga.** `:7615` è
    `lang("決定 [召喚]  ", "Enter [Details] ") + strhint2 + strhint3 + "* [Eq-Lvl] "`:
    quell'ultimo pezzo è un letterale inglese **fuori da ogni `lang()`**, come i
    «Guild Point» di `:15489` nella 46ª. ⚠️ E la riga di aiuto di quella finestra
    (500 px, tetto 55) arriva a **59 caratteri già in inglese**: senza quei
    dodici starebbe dentro.
    ⭐ Il referto che la 46ª chiedeva adesso ha due casi noti e una ragione in
    più: non è solo inglese che resta inglese, è inglese che **rompe una
    misura**.
13. ⚠️ **La rete 4 può avere ragione anche quando l'inglese distingue.**
    `:7818`, `:7823` e `:7828` hanno lo **stesso** giapponese
    (「name(rc)は興奮して襲い掛かってきた。」) e due inglesi diversi — il terzo dice «is
    confused and attacks you» invece di «is excited!». I tre rami cambiano
    `CDATA_RELATION` (0, −1, −3), non il testo: è l'autore giapponese ad aver
    scelto una frase per tutti e tre.
    💡 È il rovescio del lotto 035, dove a distinguere era il giapponese e ad
    appiattire l'inglese, e la rete 11 autorizzava a riprendersi la distinzione.
    **Qui non c'è nessuna rete che autorizzi**: la resa è una sola.
14. ⭐⭐⭐ **Una toppa può spostare una COORDINATA, e a volte è la strada giusta.**
    Nel riquadro «Combat Rolls» l'etichetta e il valore escono a **due posizioni
    fisse** — `pos wx + 590` per 「命中」, `pos wx + 625 - en * 8` per il valore — e
    il gioco conta sul fatto che l'etichetta ci stia in mezzo. «Hit» è di tre
    caratteri e lascia 9 px; «Mira» è di quattro e ne lascia 3, cioè si salda: a
    schermo «Mira64%». Lo stesso per 「魔法威力」, dove «Pot. magia» (10) sta al posto
    di «SpellPow» (8).
    ⭐ **La strada l'ha indicata upstream tre righe più su**: `:10731` scrive
    `pos wx + 590 - en * 16` per «Evade» e `:10733` `pos wx + 564 - en * 10` per
    «SpellPow». Il **`- en * N` è un idioma di casa**, e serve esattamente a
    compensare quando l'inglese è più largo del giapponese. Alla riga di 「命中」 non
    c'era, perché «Hit» è più **stretto**. La toppa ce lo mette, con valori scelti
    per **pareggiare** lo spazio dell'inglese, non per esagerare.
    ✅ **E non tocca nessuna parola**, che è il punto: l'alternativa era scendere a
    tre caratteri e buttare via «Mira», cioè il termine che `buff.hsp:679` aveva
    già deciso. ⚠️ E non viola la regola della 46ª: le rese stanno sulle righe del
    `mes lang(...)` (`:12428`, `:10734`), le toppe su quelle del `pos`. Righe
    diverse, nessun rinvio.
    💡 **La lezione più larga**: quando una resa non ci sta, prima di accorciarla
    conviene guardare **se il sorgente ha già un modo di fare spazio**. Qui ce
    l'aveva, e a tre righe di distanza.
    ⚠️ **E il corollario amaro**: questo difetto nessuna misura poteva trovarlo,
    perché io il corpo del carattere l'avevo letto sbagliato — 12 invece di 10. A
    trovarlo è stato **guardare lo schermo**. Il collaudo non è la verifica di
    quel che si sa: è l'unico posto dove si scopre quel che non si sapeva.

---

## La quarantaseiesima sessione (per storia)

⭐⭐ **Due zone chiuse e 152 rese in sette lotti** — 15000-15999, la più densa del
file, e 4000-4999, la seconda. Dare un oggetto a un alleato, l'identificazione, le
tasse, le medagliette, la bacheca degli avventurieri, la dea dei desideri e gli
otto dèi che rispondono al proprio nome. `command.hsp` passa da 509 firme da fare
a **357**, cioè dal 61% al **73%** del file; le voci rese sono **947 su 1.304**.
Catena verde fino in fondo, `cgx-test.exe` rifatto (15/08, **19:30**).

⭐⭐⭐ **E la scoperta di quella sessione è che l'inglese di monte sbaglia in CINQUE
modi diversi, e che a decidere non sono io ma la rete che parla.** In sette lotti
sullo stesso file: l'inglese che **dice la cosa sbagliata** (`:15188`, l'array del
rifiuto copiato addosso alla borraccia filtrante), quello che **appiattisce**
(`:15636`/`:15645`, un inglese solo per due scene), quello che **capovolge**
(`:4454` e `:4482`, due negazioni perse), quello che **butta via** (`:4764`, la
presa in giro sul Natale ridotta a «Merry Christmas!»), e quello che **scrive un
valore con una grafia e lo confronta con altre due** (「両性具有」: `hermaphrodite`,
`bisexual`, `hermaphorodite`). ✅ Ogni volta la strada l'ha indicata una rete —
la 3 obbliga, la 11 autorizza — o il fatto che la voce fosse una statica senza
contratto. ⭐ **La 47ª ne ha aggiunta una sesta**: l'inglese che butta via un
avviso di pericolo (`:12955`).

⚠️⚠️ **E quella sessione ha scritto una toppa sbagliata che funzionava.** Le toppe
girano dopo il dizionario, quindi agganciarne una alla riga già tradotta compila
e produce l'italiano giusto — ma `test_toppe.py:104` pretende il sorgente
pinnato, ed è quella prova a fare rumore quando upstream riscrive la riga. Ne è
uscita la regola che mancava in quarantasei sessioni: **una toppa e una resa non
stanno sulla stessa riga**.

### ▶ Il punto in cui si riprendeva allora (46ª)

Tutto era **spinto** — dieci spinte: una per ciascuno dei sette lotti, più le due
chiusure e quella nota — e l'albero di lavoro è pulito. Si riparte da
`git fetch && git status -sb` e dalle otto verifiche d'apertura.
⚠️ **La sessione si è chiusa annunciando un cambio di terminale** (15/08/2026, da
`DESKTOP-1O339MR`), come la 42ª e la 45ª. Le prime due volte non ha fatto danni —
la macchina era la stessa e Python era già a posto — e questa è la **terza prova**
della stessa cosa. `hostname` accanto al `git fetch` costa niente e lo dice.
⚠️ **Tre valori attesi sono cambiati**: `verifica --dizionario` dice «command.hsp:
0 da ritradurre, **357** non ancora tradotte» (334 da fare più **23** rinviate);
`toppe.jsonl` ha **312** toppe e `rinviate.jsonl` **42** righe. Tutto il resto è
fermo dov'era: `perimetro.py` **56%** e **41%**, `cnv_str_en.py` 49 e 24,
`misura-blocchi-spenti.py` 4 e 5, `lang-nel-ramo-jp.py` 21 righe e **0 già
tradotte**, `blocchi_en.py` 99 e 68, `variabili_en.py` 66 e 3.
⚠️ Il modello per `assembla-lotto.py` resta **`scratchpad/modello-rete6.py`**. I
lotti `024`, `026`, `028` e `030` sono a zero rinviate e tengono l'ancora
`RINVIATE = set()`, quindi possono fare da modello; il `025`, il `027` e il `029`
no.

1. ⭐⭐ **Ancora `command.hsp`, e adesso la zona più densa è 12000-12999 (55)**,
   poi 7000-7999 (54), 14000-14999 (50) e 5000-5999 (35). ⚠️ Prima di aprire una
   zona nuova, `lang-nel-ramo-jp.py` come sempre — le 11 righe morte di
   `command.hsp` stanno tutte in 2954-3016 e sono già rinviate.
   ⭐ **E 3000-3999 (34) ha un lavoro che aspetta**: `:3639` e `:3651` sono i due
   confronti su `CDATAN_NEWSEX` di cui parla il punto 3, cioè il posto giusto per
   decidere che farne.
2. **Oppure il COLLAUDO**, che adesso ha **947 rese** mai viste a schermo — 795
   dalle sessioni prima più le 152 di stanotte — e schermate nuove che si aprono
   con un tasto solo. ⚠️ Gli **88 ranghi** della 41ª restano il debito più
   vecchio. ⭐ E ci sono **quattro toppe** da guardare: `cnvrank` (i piani dei
   sotterranei come numeri nudi), i **«punti gilda»** di `:15489` (si vede
   consegnando libri antichi alla Gilda dei Maghi), il **menu del sesso** di
   `:4653` (desiderio «sex»: deve leggersi «maschio?», «femmina?»,
   «ermafrodito») e le tre righe di `*wish_fix`.
   ⭐⭐ **E il desiderio va provato per davvero**, perché è l'unica cosa di questa
   sessione che dipende da quel che il giocatore **digita**: si scrive «oggetto
   spada», «abilita pesca», «carta», «statuetta» e si guarda se arriva la roba.
   Vedi il punto 4.
3. ⭐ **Oppure `material_data.hsp`**, 117 voci di cui 27 nomi già decisi in
   `glossario.md`: resta il candidato più economico al ventesimo dizionario su 54.
4. **Oppure `item_func.hsp` (263), il « of » di ogni cadavere**, col nodo
   grammaticale che la 42ª ha lasciato aperto.
5. ⭐ **Oppure la toppa a `command.hsp:17658`**, già misurata e a buon mercato: il
   rapporto del personaggio dichiara **«Elona Version 3.03»** come letterale dove
   il giapponese usa `VERSION_STRING`. ⚠️ **Adesso si sa come si scrive**: la voce
   va **rinviata** insieme alla toppa, perché una toppa e una resa non stanno
   sulla stessa riga. Vedi il punto 2.
6. ⚠️ **E c'è un'incoerenza vecchia da correggere**, trovata cercando un termine e
   non misurando: `db_item.hsp:135432` chiama l'oggetto «borraccia filtrante»,
   `action.hsp:8267` scrive «Hai riempito d'acqua la **bottiglia** filtrante».
   Stesso oggetto, due nomi. È materiale da `correzione-*.py`, non da lotto.
7. ⭐ **Oppure il referto che questa sessione ha chiesto e non ha scritto**: un
   `coda_en.py` che cerchi i **letterali inglesi concatenati fuori dalla parentesi
   di una `lang()`**. Di quella famiglia se ne conosce **una sola** (`:15489`), e
   nessuno ha mai misurato quante siano. Vedi il punto 3.

### ⚠️⚠️ Le otto cose che la 46ª lasciava in eredità

1. ⭐⭐ **Quando l'inglese e il giapponese non dicono la stessa cosa, a decidere
   non è il gusto: è quale rete parla.** Due casi opposti nella stessa zona.
   ⚠️ A `:15188` l'inglese dice la cosa **sbagliata**: i quattro slot sono i
   quattro esiti della borraccia filtrante (`:15169`-`:15186`) — slot 2 la
   borraccia vuota, slot 4 l'alleato che **beve** (`PARAM2 > 0`,
   `SOUNDLIST_DRINK1`, `THIRST += 2000`) — e il giapponese li dice tutti, mentre
   l'inglese ci mette «No way.» e «Never!», cioè gli slot 2 e 4 dell'array del
   **rifiuto** otto righe più sotto. In inglese l'alleato beve e risponde «mai».
   ✅ Ha deciso la **rete 3**: 「ありがとう！」 era già «Grazie!» in `text.hsp:1994`.
   ⚠️ A `:15636`/`:15645` l'inglese dice **meno**: «name swallows itemname
   angrily» per due scene diversissime — l'anello di fidanzamento ingoiato per
   rabbia, e il cioccolatino ficcato in bocca in fretta mentre si risponde che
   «non ho nessun oggetto del genere». ✅ Qui ha deciso la **rete 11**: confronta
   l'**insieme** delle funzioni di contenuto, e tutt'e due le righe hanno `name`
   più `itemname` in tutt'e due le lingue. Quindi l'italiano può rimettere la
   scenetta che l'inglese aveva buttato.
   💡 **La regola che ne esce**: quando l'inglese sbaglia, si guarda **cosa
   permette la rete**, non cosa suona meglio. La rete 3 obbliga, la rete 11
   autorizza, e in mezzo non c'è spazio per una preferenza.
2. ⚠️⚠️ **Una toppa e una resa non possono stare sulla stessa riga, e la strada
   sbagliata FUNZIONA.** `applica.py` fa girare le toppe **dopo** il dizionario
   (`applica.py:530`), quindi si può agganciare `cerca` alla riga già tradotta
   leggendola dall'albero di build: la toppa si applica, l'italiano esce giusto,
   il gioco compila. Io l'ho fatto, e non me ne sarei accorto.
   ✅ **A fermarmi è stato `strumenti/tests/test_toppe.py:104`**, che pretende che
   ogni toppa si applichi al **sorgente pinnato**. Non è un capriccio: è quella
   prova a diventare rossa il giorno in cui upstream riscrive la riga, prima che
   la build produca qualcosa di sbagliato. Una toppa agganciata al testo italiano
   resterebbe verde per sempre, su una riga che nessuno controlla più.
   ✅ La forma giusta era già in tabella in `LEGGIMI.md`: **rinvio + toppa
   insieme** (`toppa-action-15221.py`, `toppa-proc-24107.py`). Il rinvio toglie la
   voce dal dizionario, così `applica` non tocca la riga, e la toppa la riscrive
   intera partendo dal sorgente.
   💡 In una riga: **o la riga la sistema il dizionario, o la sistema la toppa.**
   Scritto adesso in `LEGGIMI.md`, perché in quarantasei sessioni non c'era.
3. ⭐⭐ **Un letterale inglese può stare in coda a una `lang()`, ed è la famiglia
   che nessuno dei cinque punti ciechi guarda.** `:15489` è
   `txt lang(...) + "(" + punti + " Guild Point)"`: la `lang()` si chiude e il
   letterale sta **dopo**, quindi vale per tutt'e due le lingue — anche il
   giocatore giapponese legge «Guild Point». ⚠️ E non lo vede nessuno, ognuno per
   un motivo suo: `blocchi_en.py` cerca `if ( en )`, `else_jp.py` il ramo `else`,
   `lang-nel-ramo-jp.py` la `lang()` nel ramo giapponese, `variabili_en.py`
   l'**assegnamento** di una variabile, `cnv_str_en.py` le chiavi di `cnv_str`.
   Qui non c'è un ramo, non c'è una variabile, non c'è una conversione: c'è una
   **concatenazione**.
   💡 **E il termine era già deciso quaranta righe più su**: `:14115` è
   `lang("ギルドポイント", "Guild Point")`, reso «Punti gilda». Lo stesso testo, dentro
   una `lang()` vera. La differenza non è il testo: è **dove sta scritto**.
   ⚠️ **Trovato leggendo il sorgente riga per riga**, come il punto cieco di
   `cnv_str_en.py` nella 45ª — non rilanciando uno strumento. ⭐ **Varrebbe la
   pena scriverne il referto**: un `coda_en.py` che cerchi i letterali inglesi
   concatenati **fuori** dalla parentesi di una `lang()`. Questa è una sola, ma
   nessuno ha ancora misurato quante siano.
4. ⚠️⚠️ **Una `lang()` può essere spenta dall'ARITMETICA di un indice, ed è la
   quarta famiglia di riga morta.** `:15615` è
   `s = "", 「やだ」, 「あげないよ」, 「だめ」, 「イヤ！」`, e l'indice `f` due righe sopra
   vale **0 oppure 2**: `f = 0` a `:15610`, `f = 2` a `:15612` se l'oggetto è un
   minerale, e `:15614` entra solo `if ( f != 0 )`. Il gioco stampa **sempre e
   solo lo slot 2**; gli altri tre sono irraggiungibili.
   ⚠️ **Ma non sono testo morto nel senso della rete 6**: la riga è viva, la
   `lang()` gira, il valore finisce dentro `s`. Le prime tre famiglie sono fatti
   del **testo** — un `;`, un `/* */`, un ramo della lingua — questa è un fatto
   del **flusso**, e non la guarda nessuno strumento del progetto.
   ✅ **Si traducono lo stesso**, e per un motivo pratico: basta che upstream
   aggiunga un `f = 3` da qualche parte perché tornino vive, e allora sarebbero
   inglese in mezzo all'italiano. ⚠️ La differenza con le altre tre famiglie è
   proprio questa: là rinviare è giusto, qui sarebbe una scommessa.
5. ⭐ **Cercare prima di scrivere ha battuto il suo record: otto rese su trenta
   in un lotto solo non le ho decise io.** Sei sono il coro dei traguardi —
   «Finalmente!», «Era il risultato naturale.», «Uooooooh!», «Hmpf.», «Stanotte
   non chiudo occhio.», «Stai scherzando.» — che `text.hsp:477`-`:492` ha già
   reso perché la stessa lista serve a **ogni** traguardo del gioco, e `:15564`-
   `:15569` la riscrive tale e quale per la sfida delle tasse doppie. Le altre due
   sono «Non hai abbastanza denaro...» (`proc.hsp:15584`) e «Mai!», che avevo
   scritto io **due lotti prima**.
   💡 **La lezione minore, e costa poco**: la rete 3 le ha nominate tutte e otto
   da sola, senza che le cercassi. Un lotto che la fa parlare molto non è un lotto
   con un problema: è un lotto in un'area che il gioco ha già raccontato altrove.
6. ⭐⭐⭐ **Una `lang()` può non essere testo da leggere: può essere una parola che
   il giocatore DIGITA — e allora la regola dell'accento si capovolge, ma non
   sempre nello stesso verso.** Il sistema dei desideri di `command.hsp` ne ha
   otto, in due famiglie che vogliono decisioni opposte.
   ⚠️ **`*wish_fix` (`:4334`-`:4336`)** toglie il prefisso da quel che è stato
   battuto: «skill fishing» → «fishing». La resa è «oggetto» e **«abilita» senza
   accento**, perché quella parola il giocatore la tira fuori dalla propria testa,
   e in CP932 la `à` non esiste: un `del_str` su «abilita'» non aggancerebbe mai
   niente.
   ⚠️ **Le parole chiave di `:4832`-`:4855`** (`instr(inputlog, 0, lang(…))`)
   fanno l'opposto: la resa è **il nome dell'oggetto come sta in `db_item.hsp`**,
   accento compreso — «biglietto d'abilità», «carta», «statuetta», «bambola
   dorata», «bambola di carne» — perché lì il giocatore il nome **lo legge sullo
   schermo** e lo ricopia, e sullo schermo c'è già la forma degradata
   «biglietto d'abilita'».
   💡 **La regola in una riga**: per una stringa che si digita, l'accento si
   scrive se la parola **viene dallo schermo**, e non si scrive se viene dalla
   testa di chi gioca. La differenza non è una preferenza: è da dove arriva la
   stringa.
   ⚠️ **E le due decisioni devono combaciare**: chi scrive «abilita pesca» viene
   instradato da `:4840` — la stessa firma di `:4336` — verso `*wish_skill`, che a
   `:4860` chiama `*wish_fix`. Se una delle due parole cambia senza l'altra, il
   desiderio smette di funzionare **in silenzio**.
   ⚠️⚠️ **E c'è un limite che non si può togliere e che al collaudo sembrerà un
   guasto**: da `:4481` a `:4780` il desiderio si risolve con una cinquantina di
   `if ( inputlog == "lulwy" )`, cioè **letterali nudi fuori da `lang()`**. Dèi,
   classi, razze, «money», «youth», «merry christmas»: quelli si scrivono **in
   inglese** anche giocando in italiano. Oggetti e abilità no, perché `:4883`
   confronta con `cnvitemname()`, che è tradotto. È come è fatto il gioco.
7. ⭐⭐ **Una `lang()` può servire due volte con due mestieri diversi — etichetta e
   dato — e allora il dizionario segue il mestiere più severo.** `:4655` è la
   quinta voce del menu del sesso; trentun righe più sotto, `:4686`, la **stessa**
   `lang()` scrive `cdatan(CDATAN_NEWSEX, …)`, cioè un campo del salvataggio.
   `invariati.md` tiene `hermaphrodite` fra i «valori di dato, non testo»: una resa
   scriverebbe «ermafrodito» dentro il personaggio salvato.
   ✅ La voce si **rinvia**, e a schermo ci arriva per **toppa** sul solo sito che
   visualizza — che è quel che `text.hsp` fa già con sei toppe della stessa specie.
   ⚠️ **E senza quella toppa il menu era metà in italiano**, con «male?» e
   «female?» irraggiungibili **per costruzione**: la loro firma è ancorata in
   `text.hsp`, e `applica.py:618` applica ogni dizionario **al suo file soltanto**.
   Nessuna resa di `command.hsp` poteva toccarle.
   ⭐⭐ **E sotto c'era un difetto di monte più grosso di come lo raccontava
   `invariati.md`: non due grafie, TRE.** Lo stesso 「両性具有」 si **scrive**
   `hermaphrodite` (`:4686`) e si **confronta** con `bisexual` (`:3639`) e
   `hermaphorodite` (`text.hsp:359`). In giapponese sono tutte e tre la stessa
   stringa e tutto funziona; in inglese **nessuno dei due confronti scatta mai**.
   ⚠️ Non l'ho toccato: una toppa **renderebbe vivo un ramo che oggi non gira**, ed
   è un cambio di comportamento che vuole un collaudo. I due confronti stanno in
   **3000-3999**, cioè in una zona ancora da fare: è lì che si decide.
   💡 **La lezione**: il valore che un programma **salva** e il valore con cui lo
   **confronta** sono due stringhe diverse finché qualcuno non prova che
   coincidono. Qui non coincidono da anni, in due punti su tre.
8. ⭐⭐ **`repertorio.py` serve anche quando le parole sono nuove: a tornare non è
   una battuta, è un REGISTRO.** Il lotto 028 ha reso le otto divinità che
   rispondono al proprio nome, e nessuna di quelle frasi esisteva già; ma
   `action.hsp:14051`-`:14228` aveva deciso **come parla ciascuna**, e quello si
   riscuote: Opatos ride «Muahahah», Jure balbetta «N-non è mica…», Kumiromi parla
   a puntini, Yacatect fa la commerciante in tono familiare, Lulwy apre con un
   sostantivo di disprezzo, Itzpalt invoca al vocativo.
   ⭐ **E il registro decide anche una parola sola**: a Jure la Benedetta
   (`:4806`) l'insulto è **«idiota»**, che in italiano non ha genere ed è già
   quello che `action.hsp:14058` le mette in bocca. «Scemo» o «cretino»
   sceglierebbero il sesso del giocatore al posto suo.
   💡 È il gemello del punto 2 della 45ª un piano più su: là a tornare era una
   **scelta di forma** decisa in un altro file, qui una **voce**. In tutt'e due i
   casi non lo vede nessuno strumento — bisogna andare a cercarlo.

---

## La quarantacinquesima sessione (per storia)

⭐⭐ **Due zone chiuse e 178 rese in sette lotti** — 2000-2999, la scheda dei
talenti, e 17000-17999, i rifiuti e il rapporto del personaggio. Più le due righe
che chiudono la **scheda del personaggio**, ferme da tre riprese. `command.hsp`
passa da 687 firme da fare a **509**, cioè dal 55% al **61%** del file; il
perimetro dichiarato dal 55% al **56%** e il totale vero dal 40% al **41%**.
Catena verde fino in fondo, `cgx-test.exe` rifatto (15/08, **15:58**).

⚠️⚠️ **E la sessione ha corretto due guardie e un referto, tutti per lo stesso
motivo: guardavano la RIGA dove `estrai` ancora la firma, invece della firma.**
La rete 6 bocciava una voce viva perché la sua prima occorrenza sta in un blocco
spento (`command.hsp:17285`, il menu che si apre a ogni uscita dal gioco);
`misura-blocchi-spenti.py` contava sprecate tre rese che sprecate non erano.
Vedi il punto 1 delle cinque cose.

⭐⭐ **E il registro non l'ho scelto io: l'ha imposto il sorgente, e per una
ragione che nessuna sessione aveva ancora incontrato.** `*com_trait` si apre
**anche su un alleato** (`z,x [Ally]`, `:2589`), e quando `tc != CHARA_PLAYER`
il gioco **non ricompone** le frasi: fa `cnv_str` sulla stringa già costruita
(`:2561`-`:2564`) e scambia `"You"` con `him2(tc)`, `"Your"` con `his(tc, 1)`.
Le novanta righe «You are…» sono in seconda persona **apposta**, per farsi
convertire. Una resa italiana non contiene più `You`, quindi la conversione
muore. ✅ La strada è disinnescarla, non subirla: **registro nominale**, e la
riga vale identica per te e per il compagno. Vedi il punto 1 delle cinque cose.

⭐⭐ **Due strumenti hanno cambiato numero, e uno è nato.** `cnv_str_en.py` non
vedeva le chiamate su un elemento di array e contava 41 chiamate invece di
**49**, 17 chiavi inglesi invece di **24** — e le sette che gli sfuggivano sono
proprio quelle che convertono questa schermata. `lang-nel-ramo-jp.py` è il
**quinto punto cieco**, misurato per la prima volta stanotte: **21 righe, zero
già tradotte**.

### ▶ Il punto in cui si riprendeva allora (45ª)

Tutto è **spinto** — undici spinte: una per la correzione a `cnv_str_en.py`, una
per ciascuno dei sette lotti (i `020` e `021` insieme, che sono una riga
ciascuno), una per il referto nuovo, una per la toppa a `cnvrank`, più le due
chiusure — perché la sessione si è chiusa una prima volta dopo i tre lotti della
scheda dei talenti e poi di nuovo, come la 38ª e la 44ª. L'albero di lavoro è
pulito: si riparte da `git fetch && git status -sb` e dalle otto verifiche
d'apertura.
⚠️ **Sei valori attesi sono cambiati**, e quattro sono referti, non guardie:
`verifica --dizionario` dice «command.hsp: 0 da ritradurre, **509** non ancora
tradotte» (489 da fare più 20 rinviate); `perimetro.py` dice **56%** e **41%**;
`cnv_str_en.py` dice **49 chiamate e 24 chiavi inglesi** (diceva 41 e 17, e
guardava male); `misura-blocchi-spenti.py` dice **4 sprecate e 5 vive altrove**
dove diceva 7 sprecate; e c'è un referto in più da lanciare,
`lang-nel-ramo-jp.py`, atteso a **21 righe e 0 già tradotte**.
⚠️⚠️ **Il modello per `assembla-lotto.py` NON è più `modello-rete9.py`: è
`scratchpad/modello-rete6.py`**, che ha la rete 6 corretta. I lotti `017`, `018`,
`020`, `021` e `023` sono a zero rinviate e tengono l'ancora `RINVIATE = set()`,
quindi possono fare da modello; il `019` e il `022` no.

1. ⭐⭐ **Ancora `command.hsp`, e adesso la zona più densa è 15000-15999 (79),
   poi 4000-4999 (76), 12000-12999 (55) e 7000-7999 (54).** ⚠️ **Prima di aprire
   una zona nuova di questo file, lanciare `lang-nel-ramo-jp.py`**: le quattro
   voci di `:3003`-`:3016` erano morte e le ho rinviate senza aprire la zona
   3000-3999.
2. **Oppure il COLLAUDO**, che adesso ha **795 rese** mai viste a schermo — 617
   dalla 43ª e dalla 44ª, più le 178 di stanotte — e **tre** schermate nuove che
   si aprono con un tasto solo (`F`, `c`, `Esc`). Vedi la tabella più sotto.
   ⚠️ E gli **88 ranghi** della 41ª restano il debito più vecchio.
   ⭐ **C'è anche una toppa da guardare a schermo**, ed è la prima volta che
   `cnvrank` viene toccato: i piani dei sotterranei e i livelli dell'arena EX
   devono uscire come **numeri nudi** («Palmia 5 liv.»), non come «5th».
3. ⭐ **Oppure `material_data.hsp`**, 117 voci di cui 27 nomi già decisi in
   `glossario.md`: resta il candidato più economico al ventesimo dizionario su 54.
4. **Oppure `item_func.hsp` (263), il « of » di ogni cadavere**, col nodo
   grammaticale che la 42ª ha lasciato aperto.
5. ⭐ **Oppure la seconda toppa a `command.hsp:17658`**, che è già misurata e
   costa poco: il rapporto del personaggio dichiara **«Elona Version 3.03»** come
   letterale, dove il giapponese della stessa riga usa `VERSION_STRING`. La resa
   non lo può correggere (sarebbe una funzione in più, ed è la rete 11), una
   toppa sì.

### ⚠️⚠️ Le cinque cose che la prossima sessione deve sapere

1. ⭐⭐ **Il registro di una schermata può essere deciso da una `cnv_str`, e
   allora non è una preferenza: è l'unica forma che funziona.** `command.hsp`
   `:2546`-`:2569` è il caso puro. Quando la scheda dei talenti si apre su un
   alleato, il gioco **non rigenera** le novanta righe: le riscrive con quattro
   `cnv_str` che cercano `"You"` e `"Your"` dentro il testo già composto. È
   perché quel trucco funzioni che l'inglese di monte parla in seconda persona.
   ⚠️ **L'italiano non può ereditarlo**: nessuna resa contiene `You`, e la
   sostituzione non aggancia più niente. Non è un difetto da toppare — sarebbe
   una toppa su ogni riga — ✅ è una resa da scrivere **senza persona**, così che
   la conversione non serva. Le tre manovre sono quelle di sempre e qui rendono
   tutte: l'aggettivo in **-bile** («Cavalcabile», «Non cavalcabile»), che al
   singolare non ha genere; il **nome astratto** («Autodistruzione», «Corazza
   speciale», «Neutralizzazione degli attacchi elementali»); l'accordo **spostato
   su una cosa** («Furia al primo attacco *subito*», «Le mine non scattano»).
   💡 **La lezione generale**, che è il gemello del punto 2 della 44ª: là si
   cercava *chi altro legge le variabili di una schermata*, qui *chi riscrive le
   sue stringhe dopo che sono state composte*. Due domande diverse sullo stesso
   sospetto — che il testo non finisca dove sembra.
2. ⭐⭐ **La forma grammaticale di una resa può essere già stata decisa in un
   altro file, e allora si riscuote.** `:2492` è `"You are " + _seikaku(...) +
   ". [...]"`, e `_seikaku` è il vettore dei caratteri di `text.hsp:52`, che chi
   ha chiuso quel file ha reso **al nome astratto** — «Allegria», «Prudenza»,
   «Devozione», «Codardia» — proprio per non far accordare un aggettivo con la
   persona. Quindi «Sei Allegria» non è scrivibile, e l'unica forma che regge è
   l'etichetta: «**Carattere: Allegria**».
   💡 La 42ª aveva scoperto che un **termine** deciso altrove torna a chiedere il
   conto (`termini.py`). Questa è la stessa cosa un piano più su: a tornare non è
   una parola, è una **scelta di forma**. ⚠️ E non la vede nessuno strumento:
   `dossier.py` cerca rese gemelle per giapponese e per inglese, non «che forma
   ha preso la funzione che questa riga interpola».
3. ⚠️⚠️ **Una `lang()` può essere morta perché sta nel ramo sbagliato dell'`if`,
   ed è la terza famiglia di riga morta.** `command.hsp:2954` apre un
   `if ( jp ) { … }` lungo settanta righe — le statistiche del diario — con
   dentro sette `lang()` vere; il ramo `else` (`:3022`) stampa le stesse cifre in
   **inglese nudo**, dentro un blocco `ANNA CUSTOM`. In italiano quelle sette non
   si vedono mai.
   ⚠️ Le prime due famiglie si **vedono** — c'è un `;` o un `/* */` che le
   spegne — questa no: la riga è viva, il file è vivo, la `lang()` è vera, e a
   spegnerla è il **ramo della lingua**. La rete 6 non la prende,
   `commenti-blocco.py` nemmeno, e nessun conteggio di «non tradotte» la
   distingue dal lavoro utile.
   ✅ Adesso c'è `scratchpad/lang-nel-ramo-jp.py`, ed è il **rovescio di
   `else_jp.py`**: quello cerca l'inglese nudo dentro l'`else`, questo la
   `lang()` sprecata dall'altra parte dello stesso `if`. Fin qui se ne guardava
   un lato solo.
   ⭐ **E la misura è la parte che conta: 21 righe, zero già tradotte.** Nessun
   lotto in quarantaquattro sessioni ci era mai caduto, quindi il referto nasce
   come guardia per il futuro e non come bonifica. **Se «già tradotte» sale sopra
   0, qualcuno ha speso lavoro su testo morto.**
4. ⚠️⚠️ **Un referto può avere un punto cieco suo, e questo lo aveva da quattro
   sessioni.** `cnv_str_en.py:32` pretendeva un identificatore semplice come
   primo argomento (`([A-Za-z_@][\w@]*)\s*,`) e non vedeva
   `cnv_str listn(0, cnt), …`, cioè le chiamate su un **elemento di array**.
   Allargata la regex: 41 chiamate → **49**, chiavi inglesi 17 → **24**.
   ⚠️ **E le sette che gli sfuggivano non erano periferiche**: quattro sono la
   conversione della schermata che stavo per tradurre. Il referto che doveva
   avvisarmi del problema era cieco proprio lì.
   💡 La regola che ne esce somiglia a quella delle reti che sbagliano loro: **un
   referto che non ha mai trovato niente in una famiglia di file non è una prova
   che quella famiglia sia pulita** — può essere che non la guardi. Trovato
   leggendo il sorgente, non rilanciando lo strumento.
5. ⭐ **Cercare prima di scrivere ha reso più di sempre: su 96 rese, quattordici
   nomi non li ho decisi io.** Sette stanno in `skill.hsp`, che è chiuso al
   100%, e si copiano — «Insulto», «Salto dimensionale», «Provocazione», «Soffio
   variabile», «Tiro zero», «Carica», «Ammaliamento»; «Imposizione delle mani» è
   in `chara_func.hsp:6258`, la battuta di Jure; «Sentenza di morte» in
   `skill.hsp:1044`; «malattia dell'etere», «la barra», «Follia», «Fama», «monete
   d'oro» in cinque file diversi.
   ⚠️ **Nessuno di questi l'avrebbe pescato la rete 3**, che confronta il
   giapponese **intero**: qui il termine è annegato dentro una frase più lunga.
   È il caso dei materiali della 44ª, e la risposta è la stessa — `glossario.md`.
   ✅ Le sette abilità del **risveglio** invece nascono in `chat.hsp:17854`-`:17865`,
   file **senza dizionario**, e stanno adesso in glossario col numero di riga:
   «Accumulo di mana», «Cura tattica», «Attacco tattico», «Arti marziali
   tattiche», «Maledizione tattica», «Lancio tattico», «Tempesta variabile».

### ⚠️⚠️ Le tre cose in più che la seconda metà della sessione ha insegnato

1. ⭐⭐ **Due guardie e un referto guardavano la RIGA dove `estrai` ancora la
   firma, e la firma può vivere altrove.** È la scoperta 4 della 43ª — «una zona
   non è una schermata» — che tre strumenti diversi non avevano recepito.
   ⚠️ **La rete 6** ha bocciato cinque voci del menu d'uscita perché la loro
   prima occorrenza sta nell'`ORIGINAL` che il mod ha spento; ma **due di quelle
   rivivono** nel blocco che il mod ha messo al suo posto — 「ゲーム設定」 a
   `:17285` e a `:17316`, 「無事に記録された。」 a `:17296` e a `:17330`.
   Rinviarle avrebbe lasciato inglese un menu che si apre **a ogni uscita dal
   gioco**.
   ⭐ **Misurato prima di toccarla**, com'è d'obbligo: su tutto il sorgente **36
   firme** toccano un blocco spento, **28 sono spente del tutto** — e lì la rete
   aveva ragione — e **8 sono miste**, sette con l'ancora nella riga morta.
   Ventotto contro otto: la rete resta, cambia solo che ora guarda **tutte** le
   occorrenze e boccia se sono spente tutte. Il modello nuovo è
   `scratchpad/modello-rete6.py`, ed è la **quarta rete che si corregge** dopo la
   8, la 4 e la 9.
   ⚠️ **E la stessa correzione rifà `misura-blocchi-spenti.py`**, che per otto
   sessioni ha contato gonfio: **4 sprecate e 5 vive altrove**, dove diceva 7
   sprecate. Fra le riabilitate c'è `proc.hsp:1000`, che questa stessa pagina
   citava da sessioni come esempio di lavoro perso: la sua firma vive a `:1039` e
   `:1298`.
   💡 La regola generale: **quando una guardia parla di una firma, deve guardare
   tutti i suoi siti.** Un numero di riga in un dizionario indicizzato per
   contenuto è un indirizzo di comodo, non il posto dove la stringa vive.
2. ⭐⭐ **Un ordinale può essere inglese senza che nessuna `lang()` lo dica.**
   `init.hsp:149`-`:168` è `cnvrank`, e dopo il `return` del ramo giapponese
   attacca `"st"`, `"nd"`, `"rd"`, `"th"` secondo la regola inglese: **sedici
   siti** in sei file stampavano «5th», «21st», «3rd» in italiano.
   ⚠️ **Nemmeno `blocchi_en.py` lo vede**, perché i letterali non stanno dentro
   un `if ( en )` ma **dopo** un `if ( jp ) { return }`, cioè in un ramo inglese
   implicito. È il secondo punto cieco in una forma che il suo stesso referto non
   copre.
   ✅ La toppa fa fare al ramo italiano quel che fa già il giapponese —
   restituire il numero nudo — e lascia l'ordinale alla **resa del singolo
   sito**, che sa in che frase finisce.
   ⚠️ **E l'italiano non poteva scriverlo comunque**: «5°» vorrebbe il grado, che
   in CP932 è a **doppia larghezza** e `guardie.py` li vieta tutti tranne `♪`.
   La strada del numero nudo non è un ripiego, è l'unica. A `:17435` la resa è
   diventata « liv.», invariabile, perché «5 piani» sbaglierebbe a 1.
   💡 **Due cose imparate scrivendo la toppa**: `applica.py` cerca **per righe**,
   non nel testo intero, quindi una toppa che ne tocca due si scrive come **lista
   di righe**; e la sostituzione va tenuta **1:1 sulle righe**, perché
   aggiungerne una sfaserebbe i numeri fra build e sorgente.
3. ⭐ **Un file di testo esportato ha un tetto ESATTO, non un massimo.** Il
   rapporto del personaggio (`:17658`-`:17855`) allinea i due punti scrivendo gli
   spazi dentro la stringa: «`Life      : `», «`Sanity    : `», dodici caratteri
   ciascuna. Una resa di undici o tredici storce la colonna di tutte le righe
   sotto. ⚠️ È l'**opposto** del lavoro sui menu, dove il tetto è un massimo da
   non superare: qui anche più corto è sbagliato.
   💡 E per una volta l'italiano lungo non dà fastidio: «Schivata» e «Protezione»
   ci stanno per intero, mentre nella scheda del personaggio della 43ª gli stessi
   due termini erano dovuti diventare «Schiv.» e «Prot.» per stare in 43 e 46 px.
   La stessa parola, tagliata dove taglia il sito e distesa dove il sito la
   lascia stare.
   ⚠️ **Quattro etichette restano identiche all'inglese** e vanno in
   `invariati.md` **fra apici inversi**, perché gli spazi di allineamento fanno
   parte della stringa: `_valore_di_riga` legge verbatim solo quel che sta fra i
   backtick, una previdenza scritta per `text.hsp:62` che qui serve per la prima
   volta a quattro voci in un colpo.

### ⭐ Quello che il collaudo deve guardare

`cgx-test.exe` è aggiornato (15/08, **15:58**) e contiene **795 rese** mai viste
a schermo. Resta valida tutta la tabella della 44ª più in basso, e ci si
aggiungono tre schermate che hanno il pregio di aprirsi **con un tasto solo**.

| cosa | come arrivarci | perché guardarla |
|---|---|---|
| **la scheda del personaggio** | premi `c` | ⭐ «Livello» e «Nome» **adesso sono italiani**: era il punto 2 della ripresa da tre sessioni. Se una delle due tocca il suo valore, i budget sono 60 px e 38 px in `decisioni.md` |
| **il menu dell'uscita** | premi `Esc` | ⭐⭐ «Esci dal gioco», «Impostazioni», «Regolazioni», «Annulla». ⚠️ **È la prova della rete 6 corretta**: due di quelle voci hanno l'ancora in un blocco spento e sarebbero rimaste inglesi |
| ⚠️ il salvataggio | dal menu, esci davvero | «L'avventura è stata registrata.», poi «Gli occhi si chiudono, e tutto svanisce in pace.» |
| **i piani dei sotterranei** | lancia Ritorno e guarda la lista | ⭐⭐ **è la prova della toppa a `cnvrank`**: deve uscire «Palmia 5 liv.», non «Palmia 5th». Se leggi ancora «th», la toppa non è entrata |
| il rapporto del personaggio | esportalo dal menu personalizzato | ⭐ 37 rese, e sono **colonne**: se i due punti non cadono tutti incolonnati, una resa non è di dodici caratteri |
| ⚠️ «Elona Version 3.03» nel rapporto | la prima riga del file | **deve uscire così ed è un difetto di monte**: il giapponese usa `VERSION_STRING`, l'inglese scrive la versione a mano. È il punto 5 della ripresa |
| i tre rifiuti del tiro | prova a sparare senza arco o senza frecce | «Devi equipaggiare un'arma da tiro.», «Le munizioni equipaggiate non sono adatte.» |
| le munizioni | cambia tipo di munizione | «Munizioni caricate:», «Normali», «Illimitate» |

| cosa | come arrivarci | perché guardarla |
|---|---|---|
| **la scheda dei talenti** | premi `F` | ⭐⭐ **è la prova della sessione**: 96 rese, e sotto `[bit]` c'è una riga per ogni cosa che il personaggio è |
| ⚠️ **la stessa scheda su un COMPAGNO** | dalla scheda, premi `z` o `x` | ⭐⭐ **è il punto 1, ed è la sola prova che conta**: lì l'inglese cambiava persona con `cnv_str` e l'italiano no. Ogni riga deve funzionare **senza soggetto** — e va guardata su una compagna, non su un compagno |
| le sei immunità | un personaggio che ne abbia una | «Immunità alla confusione», «al terrore», «al veleno»: sono le più frequenti |
| ⚠️ le tredici abilità del risveglio | spendi 600 AP con un compagno risvegliato | «Cura tattica appresa», «Accumulo di mana appreso». ⚠️ Il **menu degli AP** (`chat.hsp`) è ancora inglese: i due nomi non combaceranno finché quel file non si apre. **Non è un difetto, è il punto 5** |
| i cinque tratti da negoziante | un personaggio con un negozio | «Eleganza [clientela migliore]». Sono le righe più lunghe della schermata: se una tocca il bordo, è lì che si vede |
| ⚠️ i due caratteri | la stessa scheda, in fondo | «Carattere: Allegria», «Anche un lato di Prudenza». ⚠️ Vengono da `text.hsp` e sono **nomi**: se leggessi un aggettivo, la resa di quel file è cambiata |
| il diario dei ranghi | apri il diario (`j`) | «Fama: », «Paga: circa N monete d'oro», «Scadenza: N giorni» |
| ⚠️ le statistiche dell'avventura | lo stesso diario, più in basso | **devono uscire in inglese, ed è giusto**: è il punto 3, il ramo `if ( jp )`. Se un giorno si vogliono in italiano, è lavoro da **toppa** sul ramo `else`, non da dizionario |
| «Level» e «Name» sulla scheda | apri la scheda (`c`) | **devono ancora uscire in inglese**: è il punto 2 della ripresa |
| gli 88 ranghi | F12 → wizard, poi iscriviti a arena/gilda/museo | ⚠️ il debito più vecchio, dalla 41ª |

### I sette lotti, più una toppa e una correzione

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `command-017` | 2005-2330 | le intestazioni e le **quarantasei righe di stato** sotto `[bit]` | 46 |
| `command-018` | 2336-2507 | il **risveglio**, le tredici abilità, il negoziante, i caratteri | 38 |
| `command-019` | 2543-2999 | la coda della scheda e il **diario dei ranghi** | 12 **+7 rinviate** |
| `command-020` | 3556 | 「レベル」/`Level`, e chiude la prima colonna della scheda | 1 |
| `command-021` | 7623 | 「名前」/`Name`, e **la scheda del personaggio è finita** | 1 |
| `command-022` | 17014-17635 | i rifiuti, **l'uscita dal gioco**, il menu personalizzato | 43 **+3 rinviate** |
| `command-023` | 17658-17920 | il **rapporto del personaggio** e le munizioni | 37 |
| `toppa-init-cnvrank` | `init.hsp:149` | l'ordinale inglese di sedici siti in sei file | — |
| `correzione-piano` | `:17435` | « piano» → « liv.», che il numero non rende ordinale | 1 |

⭐ Sono **178 rese** e **14 rinvii**: le sette del `019`, le quattro gemelle di
`:3003`-`:3016` trovate dal referto nuovo, e le tre del menu d'uscita che sono
morte davvero. Rinviare subito le gemelle è costato niente e toglie a chi aprirà
la 3000-3999 il lavoro di ritrovarle da capo.
💡 **Cinque invariati nuovi**: `[bit]`, e le quattro etichette del rapporto che
in italiano restano tali e quali — `Mana      : `, `Karma     : `, `DV        : `,
`PV        : ` — dichiarate **con gli spazi**, fra apici inversi. **Una toppa
nuova**, la prima da tre sessioni.

### 💡 Quello che i tre lotti hanno insegnato sul metodo

⭐⭐ **L'aggettivo in `-bile` è la manovra nuova, ed è la più economica di
tutte.** «Cavalcabile» e «Non cavalcabile» non hanno genere al singolare, quindi
reggono su chiunque senza girare la frase, senza nome astratto e senza spostare
l'accordo. ⚠️ Vale **solo al singolare** — «cavalcabili» resta invariato ma
«adatti/adatte» no — e in una lista di stati il singolare è garantito.

⭐ **La parentesi del giapponese è informazione, non decorazione.** Le righe del
risveglio hanno la forma 「frase[effetto]」 e l'inglese tiene solo la frase:
`:2362` perde «[meno HP, più schivata e critici]», `:2372` perde «[consuma MP
pari al danno]», `:2357` perde perfino il **fascino** che è il motivo per cui i
nemici si stordiscono. ✅ La resa tiene la parentesi, ed è ciò che rende la riga
**utile**: dice che cosa fa, non come suona. 💡 È lo stesso movimento della 44ª
sui materiali — la parentesi come contatore — applicato all'informazione.

⭐ **Il genitivo sassone si scioglie coi due punti.** `:2640` è
`cnven(cdatan(CDATAN_NAME, tc)) + lang("の特性", "'s Trait")`: il nome arriva
**prima** e la resa può solo seguirlo, quindi «Tratti di X» non è scrivibile.
✅ «X: i tratti» — la strada del `map-005`, e la stessa cosa che fa il giapponese
col の.

💡 **E una riga della schermata PUÒ dare del tu**, che è il contrappunto al punto
1: `:2637` sta dentro `if ( tc == CHARA_PLAYER )` e nel ramo `else` il sorgente
scrive un'altra frase. Dove la persona la garantisce il sorgente, il registro
nominale non serve — anche se lì l'ho tenuto lo stesso, perché accorcia.

### ⚠️ La serie degli errori di monte passa da cinquantasette a sessantadue

I due della seconda metà:

- ⭐ **un appiattimento che un gemello ha reso visibile**: `:17367` e
  `proc.hsp:14527` hanno l'inglese **identico** — «Returning while taking a quest
  is forbidden» — ma il giapponese distingue 「脱出」 (la **fuga**, l'incantesimo
  Escape) da 「帰還」 (il **ritorno**, l'incantesimo Return). Sono due comandi
  diversi con due tasti diversi. La resa li separa, e la rete 13 lo segnalerà come
  referto: ha ragione a farlo. 💡 `dossier.py` serve a copiare, e qui è servito a
  **distinguere**: senza il gemello non avrei guardato il giapponese di una frase
  che l'inglese dava per identica;
- `:17658` scrive **«Elona Version 3.03»** come letterale, dove il giapponese
  della stessa riga usa `VERSION_STRING`: il rapporto dichiara una versione fissa
  e sbagliata a ogni esportazione. ⚠️ La resa non lo può correggere — sarebbe una
  funzione in più, ed è la rete 11 — quindi aspetta una toppa (punto 5 della
  ripresa).

E i tre della prima metà:

- ⚠️ **una coppia rotta in due modi**: `:2275` 「乗馬に適さない」 è «non adatto
  alla cavalcatura», il semplice contrario di `:2260`, e l'inglese scrive **«You
  are too weak to carry you.»** — sgrammaticato, e per giunta dice un'altra cosa,
  che sei tu troppo debole per portare te stesso;
- ⚠️ **una condizione spostata di riga**: `:2265` 「あなたは分裂できる」 è «puoi
  dividerti», secco, e `:2285` 「元気な場合分裂する」 è «ti dividi **se sei in
  forze**». L'inglese mette «when attacked easily» sulla prima e «when attacked»
  sulla seconda: sposta la condizione **e** la cambia;
- `:2347` 「生もの製のアイテム」 sono gli oggetti **fatti di roba fresca** — il
  cuoio crudo, la carne — e l'inglese scrive «You eat raw items», che in un gioco
  dove si mangia di tutto non distingue niente.

### 💡 I numeri

Le firme rese passano da 12.650 a **12.828** (+178). **Il perimetro dichiarato
passa dal 55% al 56% e il totale vero dal 40% al 41%.** `command.hsp` da 687
firme da fare a **509**: dal 55% al **61%** del file, ed è il quarto file per
grandezza del progetto. I dizionari restano **19 su 54**, le toppe passano da 308
a **309** — la prima da tre sessioni. Le rinviate da 25 a **39**, ed è il salto
più grosso del progetto: quattordici in una sessione, undici delle quali della
stessa famiglia.
⚠️⚠️ **Tre referti hanno un valore atteso nuovo, e nessuno perché sia cambiato
il sorgente**: `cnv_str_en` dice 49 e 24 dove diceva 41 e 17;
`misura-blocchi-spenti` dice 4 sprecate e 5 vive altrove dove diceva 7 sprecate;
e `lang-nel-ramo-jp` è nuovo, atteso a 21 e 0. **Tutti e tre guardavano male, non
guardano cose diverse.** Gli altri sono fermi: `blocchi_en` 68,
`rete8_dizionario` 3, `larghezze` 0 su 75, `diario` 0 su 214, `riquadri` 0 su 38
e 0 su 71, `battute --divergenti` 13.

---

## La quarantaquattresima sessione

⭐⭐ **Quattro schermate intere chiuse, 485 rese in tredici lotti**, ed è il
totale più alto del progetto — il primato era delle 243 della 40ª. Sono le
schermate che un giocatore incontra per prime e poi per sempre:

- il **«Background»** della creazione del personaggio — cinque righe di
  `*setHistory`, 222 rese — che `chat.hsp:8588` rilegge anche sugli **alleati**
  per il racconto di Mizuki;
- la **lista degli alleati** (`*com_ally`, 58 rese), la finestra che si apre
  ogni volta che il gioco chiede *quale compagno*, in undici usi diversi;
- la **telepatia** (`*com_knowOther`, 98 rese fra pensieri e vulnerabilità), che
  è chiusa per intero: la finestra non ha più una riga inglese;
- il **menu del compagno** (`*com_chara`, 107 rese fra comandi, materiali e
  reazioni), cioè tutto quello che si può fare a un alleato — dargli un nome,
  insegnargli una frase, scuoiarlo, sposarlo.

Il perimetro dichiarato passa dal 53% al **55%** e il totale vero dal 39% al
**40%**. Catena verde fino in fondo, `cgx-test.exe` rifatto (15/08, **14:16**).

⭐⭐ **E il registro nominale non è una preferenza: in due di quelle schermate è
l'unica forma che regge.** Le righe 3 e 4 del «Background» sono mezza frase
ciascuna e si tirano a sorte **separatamente** — 45 pregi per 43 difetti,
**1.935 frasi possibili** — quindi la testa non può concordare con la coda in
niente. Vedi il punto 1 delle cinque cose e le voci nuove di `decisioni.md`.

⚠️⚠️ **E una correzione a questo stesso file, scritta a metà sessione: `larghezze.py`
NON misura `command.hsp`.** La prima versione di questa ripresa diceva che le
zone di menu erano coperte dalla guardia. Non è vero: `larghezze.py:68` dichiara
`FILE = "text.hsp"`, e i suoi 75 menu sono tutti di lì. **Nessun menu di
`command.hsp` è mai stato misurato da nessuno.** Vedi il punto 4.

⚠️ **`command.hsp` resta il file grosso: da 1.172 firme a 681.** Le zone
9000-9999, 1000-1999 e 6000-6999 sono sparite tutt'e tre.

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** — **sedici spinte**: una per ciascuno dei tredici lotti, una
per la correzione a `text.hsp:49`, e due chiusure, perché la sessione si è
chiusa una prima volta a metà e poi di nuovo (come la 38ª). L'albero di lavoro è
pulito: si riparte da `git fetch && git status -sb` e dalle otto verifiche
d'apertura.
⚠️ **Due valori attesi sono cambiati**, e per lo stesso motivo di sempre:
`verifica --dizionario` dice «command.hsp: 0 da ritradurre, **687** non ancora
tradotte» (681 da fare più 6 rinviate), e `perimetro.py` dice **55%** e **40%**
dove diceva 53 e 39.
💡 **Il modello per `assembla-lotto.py` resta `scratchpad/modello-rete9.py`.**
Il lotto `command-013` rinvia due voci e quindi **non può fare da modello** —
gli manca l'ancora `RINVIATE = set()` — ma tutti gli altri dodici sono a zero
rinviate, e il modello non è cambiato.

1. ⭐⭐ **Ancora `command.hsp`, e la zona più densa adesso è 2000-2999 (103
   voci): la scheda dei talenti.** «[Available feats]», «[Feats and traits]»,
   «(requirement)», più «Analysis» e «Results» in cima. ⚠️ `glossario.md` ha già
   `feat` → **«talento»** (deciso il 2026-08-10 su `action.hsp:15422`), quindi
   la testa della famiglia è ferma prima di cominciare.
   Subito dopo vengono **17000-17999 (83)**, i rifiuti dell'equipaggiamento e
   del salvataggio — «You need to equip a firing weapon.», «You can't save the
   game here. Exit anyway?» — e **15000-15999 (79)**.
   💡 **Il debito dei sette toni NON esiste**, e la ripresa di stamattina
   sbagliava anche su questo: `*com_tone` (`:7476`-`:7505`) elenca i **file
   utente** di `user\talk\*.txt`, e l'unica voce fissa è «Default Tone». I sette
   valori di `CDATA_TONE` non hanno nomi da nessuna parte, quindi le sette rese
   di `command-010` non devono accordarsi con niente.
2. ⭐ **Oppure `:3556` e `:7623`, che sono ancora lì.** Due righe sole —
   `Level` e `Name` — e chiudono la scheda del personaggio, che dalla 43ª ha
   **due etichette inglesi in cima** con tutto il resto italiano. ⚠️ I budget
   sono 60 px e 38 px e stanno in `decisioni.md`: da quelle due righe non si
   vedono.
3. **Oppure il COLLAUDO**, che adesso ha **617 rese** mai viste a schermo — 132
   dalla 43ª e 485 da questa — e **quattro schermate nuove** da guardare per
   intere. Vedi la tabella più sotto. ⚠️ E gli **88 ranghi** della 41ª restano
   il debito più vecchio: non li ha ancora visti nessuno.
4. **Oppure una guardia per i menu che non sono di `text.hsp`**, che stanotte è
   passata da sospetto a misura: `larghezze.py` ne copre 75, tutti di un file
   solo, e gli altri 53 file non li guarda nessuno. `scratchpad/tetto-en.py` è
   il ripiego — l'italiano contro l'inglese di monte — ma il metro vero lo
   dichiara il sorgente, e `command.hsp:1281`-`:1283` lo dimostra: finestra 620
   px, voci a `wx + 84`, seconda colonna a `wx + 350`.
5. ⭐ **Oppure `material_data.hsp`, che adesso è mezzo deciso senza essere
   aperto.** Sono 117 voci — 59 nomi di materiale più 58 descrizioni, tetto 33
   caratteri — e **27 dei 59 nomi stanno già in `glossario.md`**, decisi dal
   lotto `command-014` col numero di riga accanto. È il candidato più economico
   a diventare il **ventesimo dizionario su 54**.
6. **Oppure `item_func.hsp` (263), il « of » di ogni cadavere**, col nodo
   grammaticale che la 42ª ha lasciato aperto (punto 3 delle sue cinque cose).

### ⚠️⚠️ Le cinque cose che la prossima sessione deve sapere

1. ⭐⭐ **Una schermata può PRETENDERE il registro nominale invece di
   preferirlo, e il motivo sta nel `rnd()`.** Le righe 3 e 4 del «Background»
   sono `ohanasi3` e `ohanasi4`, due `rnd(45) + 1` **indipendenti**
   (`chara.hsp:3261`-`:3262`), disegnate una sotto l'altra e lette come una
   frase sola: 45 teste per 43 code, 1.935 combinazioni. Una resa che
   concordasse la testa con la coda sbaglierebbe quasi sempre.
   ✅ **Le tre manovre che tolgono il participio dal soggetto**, e adesso hanno
   un nome perché in 222 rese tornano continuamente: il **nome astratto** («Un
   passato di schiavitù»), il **participio appeso a una cosa** («Genitori
   perduti troppo presto» — l'accordo cade su `genitori`), il **nome di genere
   fisso** («Cavia», «una creatura maledetta», «Un'arma», «Il clone»).
   ⭐ La seconda non era mai stata scritta ed è la più utile: **il participio non
   si evita, si sposta**. È la famiglia del dativo riflessivo della 40ª e del
   «ci si dorme» della 43ª, applicata al participio invece che al verbo.
   💡 E la congiunzione va **in coda**: tutte e 45 le teste finiscono in «, ma»,
   dove il giapponese mette 「〜が、」. L'inglese mette «Though» in testa, che in
   italiano vorrebbe due aggettivi accordati col soggetto.
2. ⚠️⚠️ **Il soggetto di una schermata può non essere quello che sembra, e a
   dirlo è un ALTRO file.** «You were a slave.» sembra parlare al giocatore, e
   invece `chat.hsp:8588`-`:8593` rilegge gli stessi cinque valori da
   `cdata(CDATA_BACKGROUND_PART_*, c)` e li fa raccontare a Mizuki, dove `c` è
   un **alleato** scelto con `*com_ally`. Non c'è una `lang()` gemella che
   distingua i due casi: è la stessa riga, e va bene per tutt'e due.
   💡 **La lezione generale**: prima di decidere il registro di una schermata si
   cerca chi altro legge le sue **variabili**, non chi altro chiama le sue
   `lang()`. Qui bastava un `grep ohanasi *.hsp`, e ha cambiato la resa di 222
   righe.
3. ⚠️ **Una tabella a `rnd(N)` può avere meno di N voci distinte, e nessuna
   verifica lo dice.** `*setHistory4` e `*setHistory5` dichiarano 45 valori e ne
   hanno **43**: `:9933` ripete `:9924`, `:9972` ripete `:9966`, `:10059` ripete
   `:10047`, `:10089` ripete `:10068`. Quei quattro tratti escono col **doppio**
   della probabilità degli altri.
   ✅ Per la traduzione non cambia niente — `estrai --da-tradurre` le fonde per
   firma e `applica.py` scrive la resa in tutt'e due i siti — ma è una
   **famiglia nuova** negli errori di monte: fin qui erano traduzioni sbagliate,
   questa è la tabella del gioco a essere scritta male. 💡 Chi apre un elenco a
   `rnd(N)` conti le voci distinte prima di fidarsi di N.
4. ⚠️⚠️ **`larghezze.py` misura UN FILE SOLO, e per quattordici sessioni
   nessuno l'aveva detto.** `larghezze.py:68` è `FILE = "text.hsp"`: i «75 menu
   misurati» che la verifica d'apertura stampa da sempre sono tutti di lì, e i
   menu degli altri 53 file con `lang()` **non li guarda nessuno**. Non è un
   guasto — il file lo dichiara e il docstring lo dice — ma la ripresa di questa
   stessa sessione ci si era appoggiata sopra per scegliere il lavoro, e
   sbagliava.
   ✅ **Due ripieghi, in quest'ordine.** Primo, il sorgente: dove dichiara due
   `pos` a poca distanza il budget è vero, e `command.hsp:1281`-`:1283` dà 620
   px di finestra, voci a `wx + 84` e seconda colonna a `wx + 350`. Secondo,
   **l'italiano contro l'inglese di monte**, col tetto alla voce inglese più
   lunga della zona — quella la finestra la contiene già, per il fatto che
   upstream ci gira. Lo misura `scratchpad/tetto-en.py`, che è la versione
   riusabile di `misura-background.py`.
   ⚠️ **È un referto, non una guardia**, e stima in caratteri quel che lo schermo
   disegna in pixel. ⭐ Ma sa una cosa che il conto a mano non sa: per le
   **dinamiche** misura il testo prodotto e non l'espressione, perché chiama
   `larghezze.reso()`. Senza, `" Carica:" + cdata(…) + "%"` risultava di 46
   caratteri invece dei 12 che stampa.
5. ⭐⭐ **La rete 3 ha trovato una resa MANCANTE in un file chiuso al 100%.**
   Traducendo 「なし」 di `command.hsp:1445` ha detto che lo stesso giapponese era
   già reso «Nessuna» a `init.hsp:371` e **«none»** a `text.hsp:49` — e il
   secondo non era una resa, era l'inglese rimasto lì. Si legge in
   `command.hsp:4247`, la lista degli avventurieri, accanto a cinque parole
   italiane: `none(Cordiale)`.
   ⚠️ **E `invariati.md:437` lo copriva, ma per un altro sito**: «none» è
   dichiarato invariato perché è uno dei valori di `CDATAN_NEWSEX`, scritti nel
   salvataggio. **La dichiarazione vale per il sito, non per la stringa**, ed è
   la prima volta che la differenza produce un difetto invece di una
   discussione.
   💡 Fin qui la rete 3 serviva a non ridecidere una resa già presa; girata
   all'indietro trova il lavoro vecchio, come `rete8_dizionario.py` nella 37ª.
   ⚠️ **E nessun conteggio poteva vederla**: la voce nel dizionario c'era, con
   un `it` non vuoto. Corretta con `scratchpad/correzione-none.py`, che è anche
   il primo modello di correzione con chiave `(riga, jp)`.

### ⚠️ Le tre cose in più che i quattro lotti del menu hanno insegnato

⭐⭐ **Quando la rete 8 boccia, la strada più economica è togliere il
complemento, non cambiare la preposizione.** Nel lotto `command-015` ha fermato
tre rese di fila — «Che frase vuoi insegnare **a** name(tc)? », «Hai ordinato
**a** name(tc) di…», «Hai detto **a** name(tc) che…» — perché `name()` porta
l'articolo dentro e a schermo sarebbe uscito «a il putit». ✅ Tutte e tre si
sono risolte **mettendo il nome a soggetto**: «name(tc): che frase deve
imparare? », «name(tc) ha l'ordine di non raccogliere…», «name(tc) può fare
come vuole…».
💡 La 40ª e la 41ª avevano risolto lo stesso problema con le preposizioni che
non si fondono («verso», «contro», «con»). Questa è più forte: quelle cambiano
la preposizione, questa **la fa sparire**. Dove l'inglese dice «tu ordini a
lui», l'italiano dice «lui ha l'ordine».

⭐ **Un termine annegato in una frase si decide nel glossario, non nel lotto.**
I 27 materiali di `command.hsp:6289`-`:6557` sono nomi di `material_data.hsp` —
`matname(MATERIAL_PEBBLE)` — che compaiono qui dentro
「マテリアル:**石ころ**を…個受け取った。」: il giapponese **contiene** 石ころ
senza essergli uguale, quindi né `dossier.py` né la rete 3 lo legano. È il caso
che la 42ª aveva descritto senza avere l'occasione di risolverlo. ✅ I 27 nomi
sono in `glossario.md`, col numero di riga di `material_data.hsp` accanto e
**verificato leggendo il file**, non a memoria.

⚠️ **E la parentesi è il contatore italiano.** «You get 3 Pebble.» è
sgrammaticato anche in inglese, e l'italiano non può indovinare il plurale di
una variabile. Il giapponese la soluzione ce l'ha già — 「石ころを3**個**受け
取った」, col contatore che lascia il nome invariato — e in italiano il contatore
è la parentesi: «**Materiale ricevuto: pietruzza (3).**», dove il participio
cade su «materiale». Vale per tutte e ventisette le righe.

### 💡 Il giapponese ha vinto quattordici volte sull'inglese, ed è il record

Sette sono errori di monte veri (vedi più sotto), sette sono appiattimenti
disfatti: `:9615` 「ロマン」 è la **meraviglia** e l'inglese scrive «romance»;
`:9672` non nomina nessuna nave e l'inglese ci mette **«the Queen Sedona»**; le
tre code 「旅に出る」/「冒険に出る」/「冒険者になる」 diventano tutt'e tre «left
on adventure»; **dieci** titoli di finestra diversi diventano tutt'e dieci «Ally
List»; `:1750` è in **katakana**, la lingua di chi non decide più, e l'inglese
scrive «Trying to execute the order»; `:1732` ha una **croma** che l'inglese
butta via; e `:6163`-`:6166` sono 「決闘!」 e 「闇のゲーム!」, cioè la citazione
di *Yu-Gi-Oh!* — «Duello!» e «**Gioco delle Tenebre**!» — dove l'inglese spiega
la meccanica («Play TCG!», «Play TCG (Lethal)!»).
💡 Restituire una distinzione che l'inglese aveva perso è costato **zero** tutte
e sette le volte: bastava guardare la colonna giapponese prima di scrivere.

⚠️ **E una volta ha vinto l'inglese, per la ragione giusta.** 「風切石」 è
«pietra che taglia il vento», ma la costante si chiama
`MATERIAL_ELEMENT_FRAGMENT` e nel gioco ci sono altre quattro **schegge** —
etere, mithril, ferro, memoria, magia. «Scheggia elementale» tiene insieme la
famiglia: è la formula della 42ª, *il giapponese è l'arbitro sul contenuto ma la
coerenza lo batte*, ed è l'unico dei 27 materiali in cui le due lingue non
dicono la stessa cosa.

### ⚠️ La serie degli errori di monte passa da quarantotto a cinquantasette

Nove nuovi, e una **famiglia nuova** che non è un errore di traduzione (vedi il
punto 3). I tre che vengono dal menu del compagno:

- ⭐ **uno NEL GIAPPONESE, ed è la seconda volta nel progetto**: `:6577` scrive
  `lang(itemname(ci) + "彼らはあなたよりずっと体力があるのだから…", "They had a
  lot more health than you…")`, cioè si porta davanti il **nome di un oggetto**
  dentro un avvertimento sui punti vita dell'avversario al gioco di carte.
  L'inglese non ce l'ha ed è la versione sana. 💡 Il primo caso era
  `init.hsp:1973` nella 41ª;
- ⚠️ **un senso ribaltato**: `:6901` 「まんざらでもないようだ」 vuol dire «non gli
  dispiace affatto», cioè che **gli fa piacere**, e l'inglese scrive «doesn't
  seem to be very happy about that»;
- `:6016` 「体液を搾り取る」 è «spremi i **fluidi**», e l'inglese scrive «Take out
  blood».

E i due che vengono dai menu degli alleati:

- ⚠️ **sette parentesi che non si chiudono**: `(Riding`, `(OutRange`,
  `(offensive`, `(defensive`, `(intercept`, `(talking`, `(Dead` — mentre
  `(Waiting)`, `(Alive)`, `(Ash)`, `(Stray)` si chiudono. Il giapponese le
  chiude tutte, e per i quattro ordini di combattimento usa le **barre**,
  「/突撃/」 「/防御/」 「/迎撃/」 「/交渉/」, che a schermo distinguono l'ordine
  dallo stato;
- `:1703` 「なんかどうでもよくなってきた」 è l'**apatia** («comincia a non
  importarmi più niente») e l'inglese scrive «It keeps getting more
  difficult...», che parla di fatica.

E i quattro del «Background»:

- ⭐ **il soggetto girato**: `:9873` 「熱中すると周りが見えなくなる。」 è «quando ci
  si appassiona non si vede più niente intorno», e l'inglese scrive «you drain
  the enthusiasm from those around you», cioè che l'entusiasmo lo **togli agli
  altri**. Non è una sfumatura, è il contrario;
- ⭐ **il passivo girato in attivo, che appiattisce due voci in una**: `:9978`
  「周囲からよく誤解される。」 è «gli altri ti fraintendono spesso», e l'inglese fa
  «you often misunderstand situations» — che è **quasi identico** a `:9966`
  「勘違いが激しい。」, il quale invece dice proprio «capisci fischi per fiaschi».
  Due voci diverse dell'elenco diventano la stessa;
- `:10065` 「他人を否定することが快感。」 è il piacere di **dare torto** agli altri,
  e l'inglese legge 否定 come «privare» e scrive «You enjoy denying pleasure to
  others»;
- `:9930` 「肝心なところで失敗する。」 è «sbagli nel momento decisivo», non «you
  fail at basic things»;
- 💡 minore, ma è un difetto di forma vero: **quattro code su quarantatre
  cominciano con la maiuscola** — `:9996`, `:9999`, `:10002`, `:10005` — dentro
  un elenco di code di frase dove le altre trentanove sono minuscole. In
  italiano sono minuscole tutte e quarantatre.

### ⭐ Quello che il collaudo deve guardare

`cgx-test.exe` è aggiornato (15/08, **14:16**) e contiene **617 rese** mai viste
a schermo. Resta valida tutta la tabella della 43ª più in basso, e ci si
aggiungono **quattro schermate intere** — che hanno il pregio di essere
**immediate**: si aprono con un comando, senza dover provocare niente.

| cosa | come arrivarci | perché guardarla |
|---|---|---|
| **le cinque righe del Background** | fai un personaggio nuovo e arriva alla schermata del passato | ⭐⭐ **è la prova della sessione**. Cinque righe, 222 rese dietro |
| ⚠️ la terza e la quarta riga insieme | la stessa schermata, e premi «Reroll» qualche volta | **è il punto 1**: la terza finisce in «, ma» e la quarta ci si deve saldare. Dieci tiri diversi e si vede se la frase regge sempre |
| la larghezza delle cinque righe | la stessa schermata | ⚠️ nessuna guardia la misura: se una riga tocca il bordo della finestra, il tetto è in `decisioni.md` e si accorcia lì |
| il passato di un alleato | Mizuki, e chiedigli di farsi raccontare il passato di un compagno | ⚠️ **è l'altro lettore delle stesse righe**, ed è quello che ha deciso il registro. Se lì suona bene, suona bene ovunque |
| **la lista degli alleati** | qualunque comando che chieda un compagno | 58 rese. ⚠️ Guardare i **suffissi accanto al nome**: «(in vita)», «(in attesa)», «(in sella)», «/assalto/». Il nome del compagno è lungo e la colonna finisce a `wx + 350` |
| ⚠️ un compagno morto in squadra all'arena | prova a metterlo in squadra | «Non è più in vita.» — è una delle tre righe dove `he()`/`is()` sono spariti e non c'è più soggetto |
| **la telepatia** | il comando che legge il cuore di un compagno | ⭐ 98 rese, e la finestra è **tutta italiana**: pensiero, vulnerabilità, titolo. Rileggerla su un compagno **affamato**, uno **ferito** e uno **ubriaco**: sono blocchi diversi |
| ⚠️ la telepatia su te stesso | lo stesso comando, su di te | deve uscire **una riga sola**, «Guardarsi dentro fa un effetto strano»: `:1783` sovrascrive tutte le altre |
| **il menu su un compagno** | punta un alleato e apri il menu | 35 comandi in un riquadro da **275 px**, cioè 29 caratteri: è il posto dove un tetto sbagliato si vede subito |
| ⚠️ il menu su una bestia del ranch | vai al ranch e puntane una | «Scuoia», «Estrai il cuore», «Cava un occhio»: sono altri comandi, nello stesso riquadro |
| i materiali consegnati | «Raccogli i materiali» con qualche alleato al seguito | ⭐ 27 righe «Materiale ricevuto: X (3).» — ⚠️ guardarne una con **1** e una con **molti**: è lì che si vede se la parentesi regge al posto del plurale |
| le otto reazioni | metti un compagno fra gli indispensabili, poi toglilo | quattro gradi d'affetto per due direzioni. ⚠️ Provarlo su un compagno che ti **adora** e su uno che ti **detesta** |
| «Level» e «Name» sulla scheda | apri la scheda del personaggio | **devono ancora uscire in inglese**: non è un difetto, è il punto 2 della ripresa |
| gli 88 ranghi | F12 → wizard, poi iscriviti a arena/gilda/museo | ⚠️ il debito più vecchio, dalla 41ª |

### I nove lotti, più una correzione

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `command-004` | 9454-9594 | **le origini**: la famiglia, la schiavitù, il laboratorio | 46 |
| `command-005` | 9595-9732 | **le partenze**: perché sei per strada | 45 |
| `command-006` | 9733-9870 | **i pregi**, teste di frase in «, ma» | 45 |
| `command-007` | 9871-10008 | **i difetti**, code di frase minuscole | 43 |
| `command-008` | 10009-10146 | **i vizi privati**, otto dei quali «Passatempo: …» | 43 |
| `command-009` | 1196-1536 | **la lista degli alleati**, undici usi e gli stati | 58 |
| `command-010` | 1575-1698 | **la telepatia**: fame, sete, affetto, i sette caratteri | 39 |
| `command-011` | 1699-1784 | **la telepatia**: stamina, ferite, tredici condizioni | 28 |
| `command-012` | 1796-1999 | **le vulnerabilità**, e le intestazioni di `*com_knowSelf` | 31 |
| `command-013` | 6002-6166 | **il menu del compagno**: dai un nome, scuoia, sposa | 35 **+2 rinviate** |
| `command-014` | 6248-6557 | **i ventisette materiali** che un alleato consegna | 28 |
| `command-015` | 6577-6770 | i rifiuti, la frase da insegnare, **le otto reazioni** | 21 |
| `command-016` | 6790-6998 | le quattro carte, il diario, la notte con chi hai sposato | 23 |
| `correzione-none` | `text.hsp:49` | l'inglese rimasto nella lista degli avventurieri | 1 |

⭐ Sono **485 rese in una sessione**, il totale più alto del progetto — il
primato era delle 243 della 40ª. Le rinviate sono **due**, tutt'e due nel
`command-013` e tutt'e due righe commentate col `;`; toppe e invariati nuovi
restano a **zero**.
💡 **E delle due, una l'ho vista io e una l'ha vista la rete 6.** `:6148` «Custom
AI» si legge subito; `:6070` «Item mark adjust» sta dentro un `if` spento a tre
righe in mezzo a quattro comandi vivi, con lo stesso rientro, e leggendo il
sorgente per scrivere il lotto non l'avevo vista. È il conto più onesto che una
guardia possa dare di sé.

💡 **Le cinque zone del «Background» hanno dato zero copie a `dossier.py`** — la
schermata del passato non parla la lingua di nessun'altra parte del gioco, ed è
la prima volta per cinque zone di fila. ⚠️ **Le quattro dei menu, l'opposto**:
undici copie fra giapponese e inglese, e undici elementi su dodici già decisi in
`action.hsp:6918`-`:7044`. Chi apre una zona di menu cerchi **prima** di
scrivere; chi apre una zona di narrativa non ci perda tempo.

### 💡 Quello che i cinque lotti hanno insegnato sul metodo

⭐⭐ **Il participio non si evita, si sposta.** «You lost your parents early» non
diventa «Hai perso i genitori» per aggirare il participio: diventa «**Genitori
perduti** troppo presto», dove il participio c'è e concorda con `genitori`. Lo
stesso per «Il paese natale, **distrutto** dai mostri» e «Origini **tenute**
nascoste». ⚠️ La regola vecchia — «mai un participio riferito al giocatore» —
resta intatta: quel che cambia è che non obbliga a rinunciare al participio, ma
solo a dargli un altro referente.

⭐ **Il nome di genere fisso è la strada anche quando la persona va nominata per
forza.** Sette rese lo usano: «Cavia» (feminile), «una creatura maledetta»,
«Un'arma nata da una tecnologia proibita», «Il clone», «Un frutto nascosto»,
«Una guida forte per gli altri», «Un ex militare». 💡 E tre nomi sono
**invariabili in genere** e si possono usare tali e quali — «criminale»,
«erede», «militare» — che è la scoperta minore ma pratica: prima di girare la
frase, si guarda se il nome un genere ce l'ha davvero.

⭐ **Il registro giusto era già nel giapponese, e l'inglese lo aveva perso.**
Otto voci su 43 di `*setHistory5` sono 「趣味は…」/「…が趣味」, cioè letteralmente
«passatempo: …», e l'inglese le gira tutte in «You like to…». La resa copia il
giapponese — «Passatempo: il pisolino», «Passatempo: la caccia» — e la colonna
esce più corta e più uniforme. 💡 È la stessa lezione delle etichette di stato di
`guida-stile.md`: **la scelta neutra non è un ripiego italiano, è la forma
dell'originale**.

⭐ **`essere` più locuzione è la forma verbale della stessa manovra.** Nei tre
rifiuti di `*com_ally` (`:1519`, `:1524`, `:1529`) l'inglese è `he(p) + " " +
is(p) + " dead."`: `he` e `is` sono **morfologia**, quindi spariscono, e la resa
resta senza soggetto e senza funzioni. «È morto» concorderebbe col compagno. ✅
«Non è più in vita», «È in attesa», «È al lavoro»: il participio non c'è
proprio, e il verbo non accorda niente. È il nome astratto del «Background»
portato dentro una frase.

⭐ **Il monologo interiore non ha genere finché resta al presente.** I 67
pensieri della telepatia sono in prima persona — «Voglio più emozioni», «Sto
ripensando ai vecchi tempi» — e due sono stati girati apposta: «vorrei che mi
capissi di più» e non «vorrei essere capito», «ho bisogno di sentire l'amore» e
non «vorrei sentirmi amato». ⚠️ L'inglese lì cambia persona a metà elenco
(«Want to eat anything», poi «Wants to eat a lot») e il giapponese no.

💡 **Zero invariati nuovi e zero toppe**: nessuna delle 485 righe ha avuto
bisogno né dell'uno né dell'altra, e i tre quarti sono statiche.

### 💡 I numeri

**Il perimetro dichiarato passa dal 53% al 55% e il totale vero dal 39% al 40%**:
terza volta di fila che si muovono tutt'e due, e non era mai successo. Le firme
rese passano da 12.165 a **12.650** (+485, il totale più alto del progetto in
una sessione). I dizionari restano **19 su 54** — `command.hsp` il suo ce
l'aveva già dalla 43ª. Le rinviate passano da 23 a **25**, le toppe restano
**308**. Tutti gli altri referti sono fermi: `blocchi_en` 68,
`rete8_dizionario` 3, blocchi spenti 7, `cnv_str` 17 chiavi inglesi su 41.
⚠️ **Il quadro della 38ª non cambia**: quel che resta è più grande di quel che è
stato fatto, e la parte più grossa **non ha firma `lang()`** — 5.284 descrizioni
di oggetto e 117.977 caratteri nei file di `data/`.

---

## La quarantatreesima sessione

⭐⭐ **`command.hsp` è APERTO, ed è il file che aveva indicato lo schermo.** Tre
lotti, **132 rese** e 4 rinviate: è il **diciannovesimo dizionario su 54**, e il
perimetro dichiarato passa dal 52% al **53%** mentre il totale vero passa dal 38%
al **39%** — tutt'e due, come nella 41ª. Catena verde fino in fondo:
`applica` + `compila` girati, `cgx-test.exe` rifatto (15/08, **03:56**).

⭐⭐ **E il pezzo più letto è dentro: `:13924` è UNA RIGA SOLA con ventotto
`lang()`**, cioè la domanda che il gioco fa a **ogni singola azione
sull'inventario** — «Quale oggetto vuoi posare? », «Che cosa vuoi mangiare? »,
«Che cosa vuoi agitare? ». Con `:23` («Vedi X per terra.», che parte a ogni passo
su un oggetto) e la **scheda del personaggio** al completo, questa sessione ha
tradotto tre delle schermate che si guardano più spesso in tutto il gioco.

⚠️⚠️ **La RETE 9 sbagliava lei, ed è la terza rete che si corregge.** Vedi il
punto 1 delle cinque cose. Il modello nuovo è `scratchpad/modello-rete9.py`.

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** (quattro spinte, una per lotto più la chiusura) e l'albero di
lavoro è pulito: si riparte da `git fetch && git status -sb` e dalle otto
verifiche d'apertura.
⚠️ **Due valori attesi sono cambiati**, e tutt'e due perché `command.hsp` adesso
ha un dizionario: `verifica --dizionario` ha **una riga in più**, «command.hsp: 0
da ritradurre, **1172** non ancora tradotte», e `perimetro.py` dice **53%** e
**39%** dove diceva 52 e 38.
⚠️ **Il modello da passare ad `assembla-lotto.py` non è più l'ultimo lotto**: è
`scratchpad/modello-rete9.py`. Il lotto `command-003` rinvia una riga, quindi non
ha più l'ancora `RINVIATE = set()` e non può fare da modello.

1. ⭐⭐ **Ancora `command.hsp`: restano 1.172 firme.** Le zone più dense sono
   **9000-9999 (179 voci)** e **10000-10999** (117, di cui 76 fuori dalla scheda),
   e per frequenza restano nominati dalla 42ª `:14280` « (Ground)» e `:16054`
   «You estimate this item would sell for…».
2. ⭐ **Oppure `:3556` e `:7623`, che sono due righe e chiudono la scheda.** Sono
   le prime firme di 「レベル」/`Level` e 「名前」/`Name`, e finché restano inglesi
   la scheda del personaggio ha **due etichette inglesi in cima** con tutto il
   resto italiano. ⚠️ I budget da rispettare sono quelli della scheda — 60 px e
   38 px — e da quelle due righe **non si vedono**: stanno in `decisioni.md`.
3. **Oppure il COLLAUDO**, che adesso ha 132 rese nuove e tre schermate ad alta
   frequenza da guardare. Vedi la tabella più sotto. ⚠️ E gli **88 ranghi** della
   41ª restano il debito più vecchio: non li ha ancora visti nessuno.
4. **Oppure `item_func.hsp` (263), il « of » di ogni cadavere**, col nodo
   grammaticale che la 42ª ha lasciato aperto (punto 3 delle sue cinque cose).

### ⚠️⚠️ Le cinque cose che la prossima sessione deve sapere

1. ⭐⭐ **Una TESTA di frase finisce in « and» SENZA spazio, e la rete 9
   cancellava proprio quella differenza.** Faceva
   `v['en'].rstrip().endswith(' and')`: lo `.rstrip()` rende identiche una testa
   (`" and"`, che deve chiudersi col connettivo perché una coda le si salda
   dietro) e una **congiunzione infissa** (`" and "`, che il connettivo lo è già).
   Ha bocciato « e » di `command.hsp:13`, il ciclo che elenca gli oggetti su una
   casella.
   ✅ **Misurato prima di toccarla**, ed è la parte che conta: sul dizionario
   intero ci sono **29 teste vere**, tutte in `" and"` esatto, e **una sola** voce
   in `" and "` con lo spazio — `text.hsp:11685`, infissa. Ventinove contro uno.
   💡 **È la terza rete che sbaglia lei** dopo la 8 e la 4 della 37ª, e la regola
   che ne esce è stabile: quando una rete boccia, prima si chiede *se la resa
   giusta è scrivibile*, poi *che cosa dice il sorgente su tutti gli altri siti
   della stessa specie*. Un caso non cambia una guardia; ventinove sì.
2. ⚠️⚠️ **Nessuna guardia misura la scheda del personaggio, e il metro sta nel
   sorgente.** `larghezze.py` conosce solo i menu di `*prompt_key`, `riquadri.py`
   l'HUD e le tattiche: le etichette della scheda si disegnano con `mes` a `pos`
   fisse e non le guarda nessuno. ✅ Il budget è la **differenza fra la `pos`
   dell'etichetta e quella del valore**, che il sorgente scrive a poche righe di
   distanza — nove budget misurati, dai **33 px** di `Desc:` ai **63** di
   `SpellPow`, con **~6,3 px per carattere** ricavati da `Cargo Lmt` (nove
   caratteri in 57 px). La tabella completa è in `decisioni.md`.
   💡 **Upstream abbrevia perché è stretto, e l'italiano abbrevia uguale**:
   `Prot`, `Evade`, `SpellPow`, `InSAN`, `Cargo Wt` sono già sigle. «Schivata» di
   `skill.hsp:307` vuole 46 px dove ce ne sono 43, e diventa «Schiv.» — non una
   resa nuova, la stessa tagliata dove taglia il riquadro.
3. ⚠️⚠️ **Una rinviata della rete 6 può togliere di mezzo un vincolo della rete
   4, e non era mai successo.** `:10825` e `:10837` hanno lo **stesso** giapponese
   「説明:」 e due inglesi diversi (`Hint:` e `Desc:`); la prima sta dentro
   l'`ORIGINAL` che il mod ha spento. Senza il rinvio la rete 4 avrebbe preteso
   una resa sola per tutt'e due — cioè un vincolo sulla riga **viva** imposto da
   **testo morto**. 💡 Fin qui la rete 6 serviva a non sprecare lavoro; questa
   volta ha protetto una resa.
4. ⚠️ **`estrai --da-tradurre` dà una voce per FIRMA, e per una schermata questo
   vuol dire che le sue etichette possono stare altrove.** La scheda del
   personaggio è a `:10495`-`:10526`, ma `Level` e `Name` non ci sono: le loro
   prime occorrenze sono a `:3556` e `:7623`. **Una zona non è una schermata**, e
   chi apre un lotto per zona deve chiedersi che cosa della schermata è già stato
   estratto altrove. 💡 Vale al contrario per il lavoro: quelle due righe, quando
   si faranno, chiuderanno la scheda senza che il lotto sappia di farlo.
5. ⚠️ **`applica.py` applica ogni dizionario al suo file soltanto** (la scoperta 4
   della 42ª) e questo si è visto **in positivo**: le tre gilde di `:10621`-`:10627`
   hanno la stessa firma di `init.hsp:373`-`:379`, già resa, e **non erano
   applicate** — comparivano nell'estrazione da fare. Si copiano parola per
   parola, e `dossier.py` le pesca da solo. 💡 Delle 132 rese, **una su dieci era
   già decisa altrove**: sei etichette della scheda, le tre gilde, «Non c'è nessun
   bersaglio in vista.». Cercare prima di scrivere continua a rendere.

### ⭐ Quello che il collaudo deve guardare

`cgx-test.exe` è aggiornato (15/08, **03:56**) e contiene le 132 rese. Il
salvataggio di scorta della 42ª è in `save-backup\pre-collaudo-20260815-42a`.

| cosa | come arrivarci | perché guardarla |
|---|---|---|
| **la scheda del personaggio** | aprila e basta | ⭐⭐ 41 etichette nuove in nove riquadri a larghezza stretta: **è la prova della sessione**. Se una tocca il suo valore, il budget è in `decisioni.md` e si abbrevia lì |
| ⚠️ «Level» e «Name» | la stessa schermata | **devono ancora uscire in inglese**: non è un difetto, è il punto 2 della ripresa |
| i ventotto prompt | apri l'inventario e fai qualunque cosa | posa, raccogli, mangia, bevi, leggi, compra, vendi, cucina, lancia, ruba: uno per azione |
| «Vedi X per terra.» | cammina su un oggetto | parte a ogni passo. ⚠️ Guardarla con **una pila** («3 pozioni») e con **due oggetti** sulla stessa casella, che è il caso di « e » |
| i sei giudizi sul letto | passa su un letto | «Ci si dorme benissimo!». Deve saldarsi alla riga di sopra senza attaccarsi al punto |
| i cinque barili | fai un alchimista e passa su un barile | «Baaarile...», «Bariiile~» |
| «Rank.5» | la pagina dei ranghi | ⚠️ **resta inglese ed è giusto**: è il letterale nudo di `:2901`, il quinto punto cieco della 41ª |
| gli 88 ranghi | F12 → wizard, poi iscriviti a arena/gilda/museo | ⚠️ il debito più vecchio, dalla 41ª |

### I tre lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `command-001` | 13-993 | quel che c'è per terra, i letti, i barili, il bersaglio | 37 **+3 rinviate** |
| `command-002` | 13013-14193 | **i ventotto prompt**, l'inventario, il furto | **54** |
| `command-003` | 10495-10948 | **la scheda del personaggio** | 41 **+1 rinviata** |

### 💡 Quello che i tre lotti hanno insegnato sul metodo

⭐⭐ **«Vedi X» e non «Si vede X»: a decidere è il numero.** `text.hsp:3095` rende
「がある。」 «Si vede " + s + ".», ma lì `s` è un **edificio**, sempre singolare;
qui `rtvaln` è una **pila** e porta il conteggio dentro. «Si vede 3 pozioni» è
sgrammaticato. ✅ La seconda persona con oggetto diretto non concorda con niente,
e i sei giudizi sul letto fanno lo stesso al contrario — «**ci si** dorme
comodi», dove l'accordo cade sul «si» e non sul letto. 💡 È la famiglia del
dativo riflessivo della 40ª: **si sposta l'accordo su qualcosa che la resa
controlla**.

⭐ **Due prompt di scambio, e a distinguerli è la PARTICELLA giapponese.**
「何を交換する？」 e 「何と交換する？」 differiscono per を contro と — che cosa
dai, contro che cosa ricevi — e l'inglese li appiattisce tutt'e due su *trade*,
distinguendoli solo per caso con due giri di frase. ✅ «Quale oggetto vuoi
scambiare? » e «Con che cosa vuoi fare il cambio? ».

⭐ **Il nome che non può stare nella frase esce e va fra parentesi.** Il prompt
del miscuglio vuole «l'effetto **di** valn», e `valn` è `itemname()`: è la rete 8.
✅ «Su quale oggetto applicare l'effetto? (X) », che è anche la forma del
giapponese — il quale la spiegazione la mette in parentesi tale e quale. È la
strada dei due punti del `map-005` con le parentesi al posto loro.

⚠️ **Lo stesso giapponese in due siti impone lo spazio a tutt'e due.** 「ターン」
è l'etichetta di colonna `Turns` a `:10526` e il suffisso ` Turns` dopo un numero
a `:10754`: la rete 4 pretende una resa sola. ✅ « Turni» con lo spazio — il
valore ne ha bisogno, l'etichetta lo assorbe come un rientro di tre pixel. È la
lezione del brusio del `map-005`, applicata a un'etichetta invece che a una
battuta.

💡 **Tre invariati nuovi**, tutti dichiarati in `invariati.md`: ` + ` (il segno
che unisce i due membri di una coppia, giapponese ＋ a larghezza intera), `HP/MP`
(il giapponese scrive la stessa sigla) e `AP` (giapponese 「ＡＰ」, e la colonna
ha 50 px). ⚠️ **`Karma` e `Mana` sembravano nuovi e c'erano già** — si guarda
prima di aggiungere, come diceva la 41ª.

💡 **Due strumenti parametrizzati invece che riscritti**: `scratchpad/simili.py` e
`scratchpad/gia_rese.py` erano cablati su `lavoro/_buff.jsonl` e adesso prendono
l'estrazione dal primo argomento, col vecchio percorso come default.

### 💡 I numeri

**Il perimetro dichiarato passa dal 52% al 53% e il totale vero dal 38% al 39%**:
è la seconda volta dopo la 41ª che si muovono tutt'e due. Le firme rese passano da
12.033 a **12.165** (+132). I dizionari da 18 a **19 su 54**. Le rinviate da 19 a
**23**. Le toppe restano **308** — questa sessione non ne ha scritta nessuna.
Tutti gli altri referti sono fermi: `blocchi_en` 68, `rete8_dizionario` 3,
blocchi spenti 7, `cnv_str` 17 chiavi inglesi su 41.
⚠️ **Il quadro della 38ª non cambia**: quel che resta è più grande di quel che è
stato fatto, e la parte più grossa **non ha firma `lang()`** — 5.284 descrizioni
di oggetto e 117.977 caratteri nei file di `data/`.

---

## La quarantaduesima sessione

⭐⭐ **Il COLLAUDO è stato fatto, dopo tre sessioni che lo rimandavano, e ha
risposto alla domanda della 40ª: il log di combattimento è italiano.** Poi ha
cambiato la coda del progetto, come nella 39ª — l'inglese che resta non è più
nel log, è **la cornice del mondo**, e sta quasi tutto in `command.hsp`.

⭐⭐ **E `map.hsp` è CHIUSO: 259 su 260, cinque lotti in una notte.** È il
**diciassettesimo file al 100%** e **il primo che il progetto apre e chiude
nella stessa sessione**. Il perimetro dichiarato passa dal 51% al **52%**, le
firme rese da 11.774 a **12.033**, i dizionari da 17 a **18 su 54**.
⚠️ Il totale vero resta **38%**: 259 firme non muovono quel numero.

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** e l'albero di lavoro è pulito: si riparte da
`git fetch && git status -sb` e dalle otto verifiche d'apertura.
⚠️ **Un valore atteso è cambiato**: `verifica --dizionario` adesso dice
«map.hsp: 0 da ritradurre, **1** non ancora tradotta», ed è `:1396`, rinviata
apposta (punto 2).

1. ⭐⭐ **`command.hsp`, e stavolta a dirlo è lo SCHERMO.** È la stessa cosa che
   nella 39ª fece aprire `chara_func.hsp`. La 40ª e la 41ª lo mettevano al
   secondo posto dicendo «si legge nei menu, non nel log, quindi dopo il
   collaudo»: il collaudo è arrivato e dice il contrario. Sono **1.304 firme**,
   otto o dieci lotti, e dentro ci sono:
   - `:23` **«You see X here.»**, che parte **ogni volta che cammini su un
     oggetto**;
   - `:13924`, **una riga sola con ventinove prompt** — «Which item do you want
     to pick up?», «Examine what?», «Drop what?», «Eat what?», «What do you want
     to buy?»… — cioè la domanda che il gioco fa a **ogni singola azione su un
     oggetto**;
   - `:10504` le etichette della scheda del personaggio (`Name`, `Aka`, `Race`,
     `Sex`, `Class`), `:2900` la pagina dei ranghi, `:14280` « (Ground)»,
     `:16054` «You estimate this item would sell for…».
   💡 **La scheda del personaggio non è un menu che apri una volta**: è la
   schermata che guardi più di ogni altra dopo il log, e i valori dentro sono
   **già italiani** (`Maschio`, `Nessuna`, `FOR COS DES PER APP VOL MAG CAR`).
   Manca solo la cornice.
2. **Oppure `item_func.hsp` (263), che è il « of » di ogni cadavere.** Vedi il
   punto 3 delle cinque cose: è la stringa più letta che il progetto non abbia
   mai guardato, ma ha un **nodo grammaticale da sciogliere prima** di poter
   scrivere un lotto.
3. **Oppure `termini.py`**, che dopo stanotte non è più un'idea: vedi il punto 1.
4. **Oppure gli 88 ranghi, che restano NON collaudati** — vedi «Quello che il
   collaudo deve ancora guardare».

### ⚠️⚠️ Le cinque cose che la prossima sessione deve sapere

1. ⭐⭐ **`termini.py` non è più un desiderio: stanotte è servito due volte in un
   lotto solo, e senza di lui undici rese sarebbero uscite incoerenti.**
   Nel lotto `map-003` avevo scritto 「神の間」 «Sala del Dio» e 「冥宮」
   «Palazzo dei Morti», tutti e due guardando il giapponese. ⚠️ Ma `text.hsp`
   rendeva già 神の間 **«il Sigillo Eterno»** in due righe di trama, e
   `db_creature.hsp` rendeva 冥宮の悪鬼 «il demone del **palazzo infero**».
   ✅ A trovarli è stata una ricerca per **sottostringa giapponese** dentro tutti
   i dizionari, fatta a mano in tre righe di Python.
   💡 **È il `Bolt` della 35ª in forma nuova** — una scelta presa in un file che
   torna a chiedere il conto in un altro — ma con una differenza che pesa: i due
   termini **non erano in `glossario.md`**. Stavano solo in dizionario, dove
   nessuno li cerca. La 40ª aveva già scritto che `dossier.py` non pesca i
   termini annegati dentro una frase (punto 5): questo ne è la prova sul campo.
2. ⚠️⚠️ **Un valore scritto nel salvataggio si migra dove viene CARICATO, non
   dove viene assegnato — e questa è la lezione che mi è costata due toppe.**
   `map.hsp:1396` ha la guardia che chiama la casa «Casa tua», e allargarla
   sembrava bastare. Non bastava: `:1325`-`:1344` è il bivio fra caricare e
   generare, e per una mappa **già salvata** fa `goto *map_preBegin`, saltando
   `*map_init_main` — dove la guardia sta. Casa tua è persistente: dalla seconda
   visita in poi si passa **sempre** dal ramo che salta.
   ✅ La migrazione vera sta a `:1328`, **subito dopo `gosub *game_ctrlFile`**, e
   copia il nome da `mapname()` invece di scrivere l'italiano nel sorgente.
   ⚠️ **Sono le PRIME DUE TOPPE DI MIGRAZIONE del progetto**: le altre 306
   correggono un errore di monte, queste convertono un dato vecchio.
   💡 **E a dirmi che sbagliavo è stato lo schermo**: dopo la prima toppa il log
   diceva «Entri qui: **Casa tua**.» e due righe sotto ancora «Vuoi lasciare
   **Your Home**?». Nessuna misura poteva vederlo.
3. ⚠️⚠️ **Il « of » di `item_func.hsp` è la stringa più letta che nessuno ha mai
   guardato, e il dizionario da solo non la aggiusta.**
   `item_func.hsp:1007`, `:1024` e `:1092` fanno
   `lang("", " of ") + refchara(inv(INV_ITEM_SUB_NAME, ...), DBSPEC_CHARA_NAME_ORG, 1)`,
   e coprono **ogni oggetto che porta il nome di una creatura**: cadaveri, carte,
   figurine, latte, escrementi, atti di proprietà, il fuso delle anime, il
   vomito. A schermo si legge «un cadavere **of** la mandragora zappatrice»,
   «un'urina **of** lo yeek».
   ⚠️ **E tradurre in «di» non basta**: `refchara(..., 1)` restituisce il nome
   **con l'articolo**, quindi verrebbe «un cadavere **di la** mandragora». Serve
   «della», e l'articolo sta **dentro la funzione**, dove il dizionario non
   arriva. È la rete 8 in una forma nuova: il genitivo non è una scelta da
   girare, è **incollato dalla struttura**. Il giapponese non ha il problema
   perché mette il possessore prima, con の.
   💡 `item_func.hsp` ha già **29 toppe**, tutte in forma a lista di righe: è il
   file che il progetto toppa più di ogni altro, e la strada probabile è quella.
4. ⚠️⚠️ **Una firma duplicata fra un file col dizionario e uno senza DIVERGE IN
   SILENZIO, e nessuna verifica lo dice.**
   `text.hsp:2764` e `map.hsp:1397` avevano la **stessa identica**
   `lang("わが家", "Your Home")`. Il primo era reso «Casa tua», il secondo no, e
   il giocatore leggeva i due nomi **a due righe di distanza**. La causa è
   `applica.py:618`, che applica ogni dizionario **al suo file soltanto**: la
   firma è globale, il dizionario no. La 41ª aveva incontrato lo stesso
   meccanismo in forma innocua (「性別不明」 riscritto due volte); qui produceva
   un difetto visibile.
   ⚠️ **Finché 36 file restano senza dizionario, ogni loro firma duplicata
   altrove è un difetto latente**, e nessun referto lo conta. È il candidato
   naturale al prossimo strumento dopo `termini.py`.
5. ⭐⭐ **La rete 4 ha corretto una formula della 41ª: gli spazi fanno parte
   della resa.** La 41ª aveva scritto, su クスクス, che «gli spazi attorno li
   mette **il sito**, copiando il suo inglese». Nel lotto `map-005` ho seguito
   quella frase alla lettera — «\*brusio\*» dove l'inglese diceva «\*noise\*» e
   « \*brusio\* » dove diceva « \*murmur\* », stesso giapponese 「 \*ざわざわ\* 」 —
   e **la rete 4 ha fermato il lotto**.
   ✅ Ha ragione lei: lo stesso giapponese non può avere due rese, e la
   spaziatura ne fa parte. Vince « \*brusio\* » di `db_creature.hsp:99492`.
   💡 **Perché la 41ª non se n'era accorta**: le tre rese di クスクス stavano in
   **tre file diversi**, e la rete 4 non le ha mai messe a confronto. Qui
   stavano nello stesso lotto. La formula giusta è che gli spazi li porta il
   **giapponese**, non il sito inglese.

### ⭐⭐ Quello che ha trovato il collaudo, ed è la parte che conta

**Cinque screenshot, e hanno ridisegnato le priorità.**

1. ✅ **Il log di combattimento è italiano, ed è la risposta alla domanda della
   40ª.** Rintracciate a schermo: «Il pipistrello **si rimette in piedi**»
   (`calculation.hsp:1917`, una delle due righe che avevano fatto aprire quel
   file, inglese nello screenshot della 39ª); «Il pipistrello attacca, ma
   \<Sinaha\> **schiva con maestria**» (la correzione della 39ª ad
   `action.hsp:5616` — il «Il viandante schiva Kefry» che compariva cinque volte
   in uno schermo **non c'è più**); i **sette cali del Death-Crest** tutti di
   fila (il lotto `chara_func-002` al completo); «ne fa polpette», «uccide sul
   colpo», «infligge una ferita mortale», «perde la ragione e si spegne».
2. ⚠️⚠️ **L'inglese che resta ha cambiato natura: è la cornice del mondo.**
   `command.hsp` (vedi il punto 1 della ripresa), `map.hsp` — adesso chiuso —,
   e `main.hsp:4409`, che stampa **«Purple Witch Runa was killed by butterspy in
   Plain Field»**: è la dipendenza dell'epigrafe che la 40ª aveva dichiarato
   senza poterla vedere. Adesso è vista.
3. ⚠️ **Gli 88 ranghi NON sono collaudati e non è colpa del salvataggio.**
   `command.hsp:2900` stampa un rango solo `if ( gdata(STARTING_GDATA_RANK + cnt)
   < 10000 )`, cioè **solo per le scale in cui sei iscritto**. Il personaggio di
   prova è `*Debug*`, Level 1, Fame 0, Guild Nessuna: la pagina esce **vuota**.
   ✅ Serve un personaggio con delle iscrizioni, o wizard mode (F12).
4. ⚠️ **«Rank.5» resta inglese, ed è il quinto punto cieco della 41ª visto a
   schermo.** `command.hsp:2901` fa `noteadd "" + ranktitle(cnt) + " Rank." +
   …`: letterale nudo fuori da ogni `lang()`. **Non è un difetto della resa.**

### ⭐ Quello che il collaudo deve ancora guardare

`cgx-test.exe` è aggiornato (15/08, 03:10) e contiene tutto. Il salvataggio è
in `save-backup\pre-collaudo-20260815-42a`.

| cosa | come arrivarci | perché guardarla |
|---|---|---|
| gli 88 ranghi | F12 → wizard, poi iscriviti a arena/gilda/museo | ⚠️ **il debito più vecchio**: sono della 41ª e non li ha ancora visti nessuno |
| «Vuoi lasciare Casa tua?» | ✅ **già provato e funziona** | era il difetto che ha aperto la sessione |
| i nomi delle mappe | entra e esci da una mappa qualsiasi | «Entri qui: …», «Lasci …», «Scendi le scale» |
| i quattordici Meshera | il laboratorio di armi biologiche | ⚠️ `cdatan` è nel salvataggio: quelli **già generati** restano «tester» |
| i sussurri di Amurdad | il Labirinto, con un salvataggio di scorta | ⚠️ **la cosa più discutibile della notte**: se l'enigma non si risolve più in italiano, le storpiature vanno rifatte |
| le folle del museo | dona qualcosa al museo e guarda i visitatori | sedici battute su tre righe |

### I cinque lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `map-001` | 500-1500 | i viaggi, le porte sbarrate, **il nome di casa tua** | 43 **+1 rinviata** |
| `map-002` | 1858-4210 | le mappe, i negozianti, **i quattordici Meshera** | 64 |
| `map-003` | 4210-9000 | i sotterranei, il Sigillo Eterno, i famigli | 52 |
| `map-004` | 9000-13000 | **i sussurri di Amurdad**, gli incarichi, il tempo | 51 |
| `map-005` | 13000-16000 | la fine del mondo, la prigione, le folle del museo | 49 |

⭐ Il `map-002` è il **secondo lotto più grosso del progetto** dopo le 68 del
`chara_func-003`.

### 💡 Quello che i cinque lotti hanno insegnato sul metodo

⭐⭐ **Il mestiere del negoziante non si traduce: si traduce la BOTTEGA.**
L'inglese fa «Gilbert the baker» con `sncnv()`, che prende la prima parola del
nome (`text.hsp:417`). Il primo giro del `map-002` scriveva «il tintore», «lo
stalliere», «il ricettatore» — e sarebbe stato un errore, perché **metà dei
negozianti di Elona sono femmine**. ✅ `text.hsp:420`-`:460` aveva già risolto
per **undici** mestieri seguendo il giapponese: «della panetteria», «della
locanda», «dell'armeria». Il negozio ha un genere fisso suo, chi ci lavora resta
senza. 💡 È la strada del «nome di genere fisso» della 40ª trovata **già fatta**:
bastava guardare la famiglia `sn*` invece di inventare.

⭐⭐ **Il giapponese è l'arbitro sul contenuto, ma la coerenza lo batte.**
Quattro volte ho seguito il giapponese e mi sono sbagliato: 神の間 («Sigillo
Eterno» vince), 冥宮 («palazzo infero» vince), ネヘルタード («Amurdad», il nome
inglese, vince perché è in sei righe del progetto), e `:9914`, dove la mia resa
più letterale ha perso contro «Qualcosa viene posato per terra» di `text.hsp:3`.
⚠️ **E una volta il giapponese era la fonte peggiore**: `map.hsp:5839` dice
「仮」, «provvisorio», che è un **segnaposto di sviluppo**. Lì ha vinto l'inglese.

⭐ **Un enigma storpiato va RI-storpiato, non tradotto.** I tredici sussurri di
`:10511`-`:10547` dicono quale scala prendere, e le lettere cadono in tutt'e due
le lingue: 「みぎの…どに……」 è 「右の**かど**に」 con due sillabe sparite, e
l'inglese fa «...ig...t co....r...». ✅ Tradurre la frase intera avrebbe
**regalato in italiano una risposta che altrove si paga**. Le tre righe che il
giapponese scrive intere restano intere: sono le conferme finali.
💡 È il controesempio che tiene onesto tutto il resto: il criterio non è rendere
il testo più ricco, è rendere quel che il gioco intende dire — **compreso quando
intende non dirlo**.

⭐ **Il genitivo davanti a `mapname()` si risolve mettendo il nome FUORI dalla
frase.** I nomi di area portano l'articolo dentro («la Torre Rovente», «il
Vuoto»), quindi «la superficie **di** X» e «entri **in** X» sono chiuse dalla
rete 8, e le preposizioni che non si fondono qui non servono perché il rapporto
è locativo. ✅ Tre forme nuove: «Entri qui: X.» (dopo i due punti), «X: torni in
superficie.» (in testa, che è anche l'ordine del giapponese), e soprattutto
**«Lasci X.»** — «lasciare» regge l'**oggetto diretto**, quindi la preposizione
non c'è proprio. ⚠️ Quest'ultima è la più economica e va **provata per prima**:
ha risolto anche `:11988` («da quando **hai lasciato** X») senza girare niente.
💡 E nel `map-002` il problema **non si è posto**: i nomi propri di città non
prendono l'articolo, quindi «di Derphy», «di Yowyn», «di Vernis» passano lisci.

⚠️ **`cerca`/`sostituisci` di una toppa vogliono una LISTA DI RIGHE.** Le ho
scritte due volte come stringa unica coi fine-riga dentro — prima `\n`, poi
`\r\n` — e non hanno agganciato niente: `applica_toppe` spezza il testo in righe
**da sé** (`applica.py:536`) e confronta liste. ✅ La forma a lista c'era già da
`item_func.hsp` (`applica.py:507`-`:516`). 💡 **Tutte e due le volte il guardiano
di `applica.py` ha detto «non esiste più» invece di sostituire a caso**: nessun
sorgente rotto, solo un errore in faccia.

### ⚠️ La serie degli errori di monte passa da quarantasette a quarantotto

Uno solo di famiglia nuova, ma `map.hsp` ne aggiunge una intera di **un'altra
specie**, che non è un errore ma un modo di tradurre:

- ⭐ **`map.hsp:10873` ha la riga di sopra ricopiata sopra.** Il giapponese è
  「進化プログラムの再構成を完了…。」, «riconfigurazione del programma di
  evoluzione completata», e l'inglese ci mette «Detect the abnormal material.
  ... Erase operation is complete.», che è **la riga di `:10847`**. Due cose che
  non c'entrano niente.

⚠️⚠️ **E poi c'è il quadro di `map.hsp`, che non è una serie di errori: sono
SETTE appiattimenti in un file solo.** «Hall» sta per **cinque piani diversi**;
«The Eternal Seal» per **tre stati** dello stesso posto; «moor» per la grande
palude di Merca e per una palude qualsiasi; «basement» per una cantina **e per
un covo di demoni**; «The Mine» per la miniera degli slime **e per il presidio
di Eulderna**; «It's hot!» per un'esclamazione e per una folata rovente;
**«tester» per quattordici Meshera con nome proprio**.
💡 E tre volte l'inglese non appiattisce, **butta via**: «Deep-Sea Castle» per il
castello del **drago a nove teste**, «Eulderna city» per «nei pressi del palazzo
reale», e i quattordici nomi di cui sopra.
⚠️ **Non è sciatteria isolata: è il modo in cui quel file è stato tradotto in
inglese.** Chi aprirà un file nuovo faccia girare la rete 13 aspettandosi il
peggio.

### 💡 I numeri

**Il perimetro dichiarato passa dal 51% al 52%; il totale vero resta 38%.**
Le firme rese passano da 11.774 a **12.033** (+259). I dizionari passano da 17 a
**18 su 54**. Le toppe da 306 a **308**, e le due nuove sono di **specie nuova**.
Tutti i referti restano dove li aveva lasciati la 40ª: `blocchi_en` 68,
`rete8_dizionario` 3, blocchi spenti 7, `variabili_en` 3 trappole, `cnv_str` 17
chiavi inglesi su 41.
⚠️ **Il quadro della 38ª non cambia**: quel che resta è più grande di quel che è
stato fatto, e la parte più grossa **non ha firma `lang()`** — 5.284 descrizioni
di oggetto e 117.977 caratteri nei file di `data/`.

---

## La quarantunesima sessione

⭐⭐ **Due file chiusi, `ai.hsp` e `init.hsp`, e sono il quindicesimo e il
sedicesimo al 100%.** Sei lotti — tre per file — **217 rese**, e il perimetro
dichiarato passa dal 50% al **51%** mentre il totale vero passa dal 37% al
**38%**: un punto su tutt'e due, che non capitava dalla 38ª. Catena verde,
`cgx-test.exe` rifatto (14/08, 22:45).

- **`ai.hsp` è il file più pulito che il progetto abbia mai chiuso: 94 su 94,
  zero rinviate, zero toppe.** È il file dell'intelligenza artificiale — quel che
  gli alleati e i nemici fanno da soli — e quindi **log ad alta frequenza**:
  i compagni che mangiano, bevono, frugano nello zaino, contrattano col
  negoziante, si medicano, sfondano le porte;
- **`init.hsp` è il più delicato del progetto, e si chiude con 123 rese e 10
  rinviate volute.** Ci stanno le `#defcfunc` che restituiscono inglese fuori da
  `lang()` — `he()`, `his()`, `him()`, `gendername()` — gli otto elenchi di
  ranghi, e i nove valori di `CDATAN_NEWSEX`, che sono **scritti nel
  salvataggio**.

⭐⭐ **E lo strumento ha imparato una cosa che gli mancava da ventitré lotti: la
chiave `(riga, en)` non è univoca.** Vedi il punto 1. Il modello nuovo è
`scratchpad/modello-chiave-lunga.py`, ed è provato che non cambia niente di quel
che c'era prima.

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** e l'albero di lavoro è pulito: si riparte da
`git fetch && git status -sb` e dalle otto verifiche d'apertura.
⚠️ **Un valore atteso è cambiato**: `verifica --dizionario` adesso dice
«init.hsp: 0 da ritradurre, **10** non ancora tradotte», e sono tutte e dieci
rinviate apposta (punto 3).

1. ⭐⭐ **Il COLLAUDO, e il debito è salito a 504 rese mai viste a schermo** —
   287 dalla 40ª, 217 da questa. È il doppio abbondante di qualunque debito
   precedente, ed è la terza sessione di fila che lo rimanda. ⚠️ **E adesso non
   è più solo il log di combattimento**: `ai.hsp` fa partire righe da solo
   appena hai un alleato al seguito, e `init.hsp` cambia **la scheda del
   personaggio, i ranghi e l'orologio**, che sono le prime cose che si vedono
   aprendo una partita. Vedi «Quello che il collaudo deve guardare».
2. **Oppure `command.hsp`/`trait.hsp`**, che sono ~1.680 firme e i due file
   nominati più grossi che restano. ⚠️ Si leggono nei **menu** e non nel log:
   la lezione della 26ª dice di lasciarli dopo il collaudo. `trait.hsp` da solo
   vale **406** firme.
3. **Oppure i due strumenti che il lavoro ha chiesto**, e adesso sono due:
   `termini.py` (dalla 40ª) e `rete3_dizionario.py` (dal punto 2 qui sotto).
4. **Oppure il quinto punto cieco**, se si vuole misurare invece che tradurre:
   vedi il punto 5.

### ⚠️⚠️ Le cinque cose che la prossima sessione deve sapere

1. ⭐⭐ **La chiave `(riga, en)` dei lotti non è univoca, e adesso il modello sa
   cosa farne.** Due `lang()` sulla stessa riga possono avere lo **stesso
   inglese** quando il giapponese distingue e l'inglese no. È successo quattro
   volte in due file: `ai.hsp:4576` (「変身！」 e 「トランスフォーム！」 sono
   tutt'e due `cnvtalk("Transform!")`), `init.hsp:358` («Great museum» per
   大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per
   日), `:2235` (i due punti per 時間 e per 分).
   ✅ La voce ambigua si dichiara con la **chiave lunga `(riga, en, jp)`**; le
   altre tengono quella corta, quindi **i lotti già scritti valgono tal quale**.
   La rete 0 passa da errore a referto e dice quali chiavi vogliono la forma
   lunga. ⚠️ E il controllo della rete 1 è salito **prima** delle altre reti:
   da adesso una resa mancante esce col suo messaggio invece che come `KeyError`
   nudo, che era un difetto noto dalla 38ª.
   💡 **Provato, non dedotto**: `ai-001`, `ai-002` e `calculation-001`
   rigenerati col modello nuovo danno jsonl **identici byte per byte**.
   ⚠️ La `firma` sarebbe altrettanto univoca, ma è un sha1: illeggibile in un
   file che si rilegge a mano. `ai-003` è scritto così ed è l'unico lotto del
   progetto che non passa da `assembla-lotto.py`.
2. ⭐⭐ **`battute --divergenti` legge SOLO `db_creature.hsp.jsonl`.**
   `battute.py:143` fa `percorsi.DIZIONARIO / f"{FILE}.jsonl"`: uno stesso
   giapponese reso in due modi in **due file diversi** non lo vede nessuno
   strumento. Questa sessione ne ha scritte tre apposta — 「痛っ！」, 「いいぞ！」
   e 「観光客」 — e il referto è rimasto **13**. ✅ A vederle è stata solo la
   **rete 3 dentro il lotto**, che gira mentre si scrive un lotto nuovo e **non
   è mai stata passata all'indietro** su tutto il dizionario. 💡 È la situazione
   della rete 8 prima della 37ª, quando `rete8_dizionario.py` trovò sei rese già
   entrate che stampavano «di il».
3. ⚠️⚠️ **I valori scritti nel salvataggio si RINVIANO, non si rendono
   identici — e a stabilirlo è stata la rete 7 contro `invariati.md`.** I nove
   valori di `CDATAN_NEWSEX` (`male`, `female`, `none`, `hermaphrodite`,
   `male?`, `female?`, `trans-male`, `trans-female`) sono scritti nei dati del
   personaggio e riletti come operandi di confronto in cinque file: tradurli
   farebbe sbagliare il genere di ogni personaggio già creato.
   Il primo giro del lotto `init-003` li aveva messi in dizionario **identici
   all'inglese**, che è il meccanismo descritto in `invariati.md` e usato da
   `db_creature.hsp` per `Qy@`. La **rete 7** li ha fermati tutti e nove — «riga
   1813 è un confronto, non un testo: va rinviata» — e ha ragione lei: quel
   testo di `invariati.md` è del 2026-08-07, la rete 7 è nata nel lotto `007`,
   dopo. ✅ Rinviati: la resa identica passa comunque da `applica.py`, la
   rinviata non tocca il sito nemmeno per riscriverci sopra la stessa stringa.
   💡 **E l'asimmetria con `text.hsp` è giusta, non un'incoerenza**:
   `text.hsp:123` ha la **stessa firma** e la tiene resa identica, perché lì il
   sito è un assegnamento a `strmale`, cioè testo che si stampa. **La rete 7
   guarda il sito, non la stringa.**
   ⚠️ E `applica.py:618` cicla su `dizionario/<file>.jsonl` applicando ogni
   dizionario **al suo file soltanto**: la firma è globale, il dizionario no.
   Per questo 「性別不明」 è stato riscritto in `init.hsp.jsonl` benché
   `text.hsp:363` lo avesse già.
4. ⭐ **`his(x, 1)` diventa «il suo» per tutt'e quattro i generi, e il «?» cade —
   mentre `he()` se lo tiene.** Upstream distingue `his` da `his?` e `her` da
   `her?` per dire che il genere è **dichiarato** dal personaggio e non
   accertato. In italiano il possessivo concorda col **posseduto**: «il suo»
   copre tutti, quindi il «?» segnerebbe un dubbio su una distinzione che
   l'italiano **non fa**. ✅ «il tuo» per `your`, «il suo» per gli altri quattro.
   ⚠️ Invece «lui?»/«lei?» restano, perché lì il pronome soggetto il genere lo
   distingue davvero e il dubbio ha su cosa cadere. 💡 **E l'articolo ci vuole**:
   i tre siti che già la usano sono scritti per riceverlo — `proc.hsp:8849`
   «succhi **il suo** sangue», `:9605` e `:9612` «interrompe **il suo**
   daffare» — e ognuno ha accanto un nome maschile singolare, che è quel che la
   rete 10 pretende.
5. ⚠️ **Un quinto punto cieco, trovato per caso e non ancora misurato.**
   `command.hsp:2901` e `:17848` fanno
   `noteadd "" + ranktitle(cnt) + " Rank." + gdata(...)`: **`" Rank."` è un
   letterale inglese nudo, fuori da qualunque `lang()`**, dentro l'istruzione
   che stampa. Non lo vede nessuno dei quattro referti — `blocchi_en.py` guarda
   dentro `if ( en )`, `else_jp.py` dentro `if ( jp ) … else`, `variabili_en.py`
   gli **assegnamenti** a variabile, `cnv_str_en.py` le chiavi di sostituzione —
   perché qui il letterale sta come **argomento di un `noteadd`**, senza
   condizione e senza variabile di mezzo. ⚠️ Quindi la scheda del personaggio
   dirà «Campione dell'arena **Rank.**5» per sempre, e nessun conteggio di «non
   tradotte» lo include. 💡 **Quanti siano non lo sa nessuno**: è il candidato
   naturale al referto dopo `rete3_dizionario.py`.

### ⚠️ La serie degli errori di monte passa da trentasei a quarantasette

Undici in una sessione, ed è il record. Due famiglie sono **nuove**:

- ⭐ **le battute rimescolate** (famiglia nuova): l'ordine dei `lang()` sulla
  riga è giusto, ma le coppie giapponese-inglese non si corrispondono.
  `ai.hsp:472` è il **sacco da pugni** e 「もっとぶって」 è «picchiami ancora»,
  ma l'inglese ci mette «`Release me now.`», che è la battuta del **prigioniero**
  di `:482`; `ai.hsp:658` è il **pubblico dell'arena** e le ultime due sono
  scambiate — 「頑張って！」 («forza!») porta «`Use your brain!`»;
- ⭐ **il gradino sbagliato** (famiglia nuova, tutta in `init.hsp`): `:358` mette
  «Great museum» su **due** gradini e chiama «Unknown **Ruin**» un museo;
  `:357` chiama «Famous tourist» quello che il giapponese sfotte come
  ちんけな遺跡荒らし e «Tomb robber» quello che il giapponese chiama 探検者;
  `:356` copia «New hope» da `:355` dove il giapponese dice ペットの母;
  `:362` mette **«Novice»**, che è un grado, dove va il **nome della categoria** —
  le altre sette righe ci mettono `Arena`, `Museum`, `Home`, `Shop`…;
- **il continente sbagliato**: `init.hsp:359` e `:360` dicono イルヴァ (**Irva**,
  il mondo) e l'inglese scrive «Tyris», che è il continente. Il progetto ha già
  i due nomi separati;
- **il personaggio sbagliato**: `ai.hsp:406` dice `name(tc)` dove il giapponese
  e il codice dicono `cc`;
- ⭐⭐ **e uno NEL GIAPPONESE, che è rarissimo**: `init.hsp:1973`, dentro `his()`,
  confronta 「自称男性」 dove le due funzioni sorelle `he()` (`:1830`) e `him()`
  (`:2011`) scrivono 「自称女性」. 💡 **Innocuo per un pelo**: il secondo operando
  della stessa riga è `lang("自称女性", "trans-female")`, il cui ramo giapponese
  è proprio 自称女性, quindi il caso viene preso lo stesso.

### ⭐⭐ Quello che il collaudo deve guardare

**504 rese mai viste a schermo.** Resta valida tutta la tabella della 40ª più
in basso — il log di combattimento è la prova che conta — e ci si aggiungono le
righe di questi due file. ⭐ Quelle di `init.hsp` hanno il pregio di essere
**immediate**: si vedono aprendo una partita, senza dover provocare niente.

| cosa | come arrivarci | perché guardarla |
|---|---|---|
| gli otto ranghi | scheda del personaggio, la pagina dei ranghi | **88 titoli nuovi** in otto scale. ⚠️ La prova è che la scala si senta scendere: «Campione dell'arena» → «Gladiatore invitto» → … → «Gladiatore senza nome» |
| «Cambio di rango (…)» | vendi qualcosa, o dona un oggetto al museo | è l'undicesima voce di ogni scala, cioè il **nome della categoria**: deve dire «Museo», «Gilda», «Arena delle bestie» — non un grado |
| l'orologio e la data | qualunque schermata che le mostri | sette separatori, e sei restano com'erano. L'unico che cambia è « sec» |
| «il suo sangue» | fatti succhiare il sangue da un vampiro (`proc.hsp:8849`) | è `his(x, 1)`, il possessivo che vale per tutto il gioco: se lì suona bene, suona bene ovunque |
| la scheda del personaggio | apri la scheda | ⚠️ ci si legge ancora «**Rank.**5» in inglese — è il punto 5, non un difetto della resa |
| i compagni che mangiano e bevono | cammina con un alleato al seguito e aspetta | otto righe (`ai.hsp:1009`-`:1252`) che partono da sole: «fruga nello zaino e non trova niente da mangiare» |
| la tag-team a tavola | metti due alleati in coppia e lascia mangiare uno dei due | cinque reazioni a scala d'affetto, **tutte copiate da `action.hsp`** |
| il pubblico dell'arena | porta una bestia all'arena delle bestie | otto grida, e due sono rese **contro l'inglese** |
| la canzone rumena | tieni un alleato che canta e aspetta | ⚠️ **la scelta più discutibile della sessione**: «Numa numa iei!!», poi «Numera♪ numera♪ ehi!♪», poi «Una mano♪ una mano♪ ehi!♪». Se non fa ridere, va rifatta |
| i figli che crescono | fai nascere un figlio e aspetta | cinque versi con l'accordo appeso ad «aria»: «guarda altrove con aria curiosa!» |

### I sei lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `ai-001` | 79-1468 | il sacco da pugni, il prigioniero, il pubblico dell'arena, i compagni a tavola, *Dragostea din tei* | 48 |
| `ai-002` | 1525-4525 | chi tira i sassi, il gioielliere che contratta, la tag-team, i figli che crescono | 42 |
| `ai-003` | 4576 | le quattro grida della trasformazione | 4 |
| `init-001` | 23-358 | il bottone Ok, l'errore di rete, arena, bestie, Nefia, museo | 46 |
| `init-002` | 359-390 | casa, negozio, comunità, gilda, le tre gilde, le cariche cittadine | 54 |
| `init-003` | 408-2873 | gli edifici, il genere, i possessivi, l'orologio, il log, l'errore | 23 **+10 rinviate** |

⭐ **L'`ai-002` ha la percentuale di copie più alta mai vista in un lotto: dodici
su quarantadue**, tutte pescate da `dossier.py` per **giapponese intero** — il
blocco della tag-team a tavola, che `action.hsp:1860`-`:2023` ha già parola per
parola in tre varianti. Col `ai-003`, che è **quattro copie su quattro**, la coda
di `ai.hsp` è quasi tutta lavoro già fatto altrove.

⭐ **L'`init-002` è il secondo lotto più grosso del progetto** dopo le 68 del
`chara_func-003`.

### 💡 Quello che i sei lotti hanno insegnato sul metodo

⚠️⚠️ **Gli accenti DENTRO la parola sono vietati, e nessuno l'aveva mai scritto.**
`accenti.py` degrada **ogni** accento in lettera + apostrofo, non solo quelli
finali: «élite» diventerebbe «e'lite» a schermo. Negli otto ranghi la parola era
la prima che veniva in mente — «gladiatore d'élite» — ed è stata evitata ovunque
(«Gladiatore **scelto**», «Domatore **scelto**»). 💡 Gli accenti **finali** vanno
benissimo — «piu'», «perche'», «citta'» — perché l'apostrofo lì è quello che
l'italiano scrive comunque.

⭐ **Un giapponese solo per TRE inglesi, e la resa è una sola: cambia solo lo
spazio.**  *クスクス*  è `*chuckle*` ad `action.hsp:250`, ` *Snicker* ` a
`db_creature.hsp:95622` e ` *grin* ` ad `ai.hsp:1570`: l'italiano dice
«*risatina*» in tutt'e tre, e gli spazi attorno li mette **il sito**, copiando il
suo inglese. È il rovescio della rete 13.

⭐ **«Verso» si aggiunge alle preposizioni che non si fondono, e stavolta ha
salvato una resa già decisa invece di una frase.** 「睨み付けた」 è «lanciare
un'occhiataccia» da `action.hsp:1854`-`:2011`, ma lì il bersaglio è sempre «ti»,
un clitico; ad `ai.hsp:2074` sono **due nomi**, e «un'occhiataccia **a**
name(cc)» è chiusa dalla rete 8. ✅ «lancia un'occhiataccia **verso** X»: la resa
già decisa si tiene tale e quale invece di essere girata. L'elenco della 40ª —
«con», «contro», «per», «tra», «sotto», «sopra» — prende «verso», e la lezione si
affina: la preposizione che non si fonde serve anche a **non dover riscrivere una
frase vecchia**.

⚠️ **Un titolo che il gioco appiccica al giocatore non può avere un genere.**
`init.hsp:356` gradino 7 è 「ペットの母」, «madre delle bestie», e metà dei
giocatori non sono madri. ✅ «**Balia** delle bestie»: nome di **ruolo**,
grammaticalmente femminile ma buono per chiunque, come «una guida» o «una spia».
È la strada del nome di genere fisso della 40ª usata su un titolo.

⚠️ **Tre aggettivi appesi a un nome di genere fisso.** I cinque versi dei figli
(`ai.hsp:2317`-`:2341`) in inglese sono participi che concorderebbero col figlio.
✅ «con **aria** curiosa», «con **aria** seria»: l'accordo cade su «aria».

💡 **Il file `rinviate<NNN>.py` non può portare commenti.** `assembla-lotto.py`
lo incolla al posto di `RINVIATE = set()` e poi confronta le reti col modello
carattere per carattere: un commento in coda alla riga resta nel file generato,
il modello non ce l'ha, e il confronto fallisce con «le reti NON sono
identiche». Scoperto scrivendo `init-003`. La spiegazione va nel docstring del
lotto, non lì.

💡 **Quattro invariati nuovi**, tutti dichiarati in `invariati.md`: `Ok`
(`init.hsp:23`), `/`, `:` e `h` (i separatori di data e orologio). ⚠️ **E due che
sembravano nuovi e c'erano già**: `Arena` era dichiarato dalla 30ª su
`text.hsp:2782`, e lo spazio ` ` da `text.hsp:198` (`strblank`). **Si guarda
prima di aggiungere**: il file ha 522 righe e la tabella non è in ordine.

### 💡 I numeri

**Il perimetro dichiarato passa dal 50% al 51% e il totale vero dal 37% al 38%**:
è la prima volta dalla 38ª che si muovono tutt'e due. Le firme rese passano da
11.651 a **11.774**. I dizionari restano **17 su 54** — `init.hsp` ne aveva già
uno con sei voci, `ai.hsp` è quello nuovo. Tutti i referti sono fermi dove li
aveva lasciati la 40ª: `blocchi_en` 68, `rete8_dizionario` 3, blocchi spenti 7,
`variabili_en` 3 trappole, `cnv_str` 17 chiavi inglesi su 41.
⚠️ **Il quadro della 38ª non cambia**: quel che resta è più grande di quel che è
stato fatto, e la parte più grossa **non ha firma `lang()`**.
---

## La quarantesima sessione

⭐⭐ **`chara_func.hsp` è CHIUSO, in una sessione sola.** Sei lotti — `002`…`007`
— **243 rese**, da 84 su 331 a **327 su 331**: le quattro che restano sono tutte
rinviate apposta. È il **tredicesimo file al 100%**. Catena verde,
`cgx-test.exe` rifatto.

⭐⭐ **E anche `calculation.hsp` è CHIUSO, in un lotto solo: 44 su 44, zero
rinviate.** Sono **due file chiusi in una sessione**, il tredicesimo e il
quattordicesimo del progetto, e `calculation.hsp` è il **sedicesimo dei 54 con
`lang()` ad avere un dizionario** (erano 15). Sette spinte in tutto.

⭐⭐ **Ed è la prima volta che i file si aprono e si chiudono perché l'ha chiesto
lo SCHERMO.** Né `chara_func.hsp` né `calculation.hsp` erano in un elenco di
priorità — il secondo `SPEC.md` §6 lo copre solo con la designazione collettiva
«i restanti 63 file `.hsp` minori». Ci sono finiti perché lo screenshot del
collaudo della 39ª mostrava il log ancora mezzo inglese **con `proc.hsp` al
100%**, e ogni riga inglese veniva da uno dei due.
✅ **Le tre fonti inglesi di quello screenshot sono adesso tutte chiuse**:
`proc.hsp` (39ª), `chara_func.hsp` e `calculation.hsp` (40ª). Le righe nominate
una per una — `:2021`, `:2047`, `:6441`, `:8317`, `calculation:1917`
(`stands up`), `calculation:1929` (`released from bind`) — sono tutte rese, e
**due di loro si sono chiuse copiando** una resa già scritta altrove.
💡 È la lezione della 26ª — *la frequenza, non l'elenco* — portata fino in
fondo: dieci minuti di gioco hanno deciso due file interi meglio di qualunque
conteggio di firme.

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** e l'albero di lavoro è pulito: si riparte da
`git fetch && git status -sb` e dalle otto verifiche d'apertura.

1. ⭐⭐ **Il COLLAUDO, ed è la prima volta che questa pagina lo mette al primo
   posto.** **287 rese nuove mai viste a schermo**, ed è il debito più alto mai
   accumulato in una sessione — più delle 235 della 35ª. Ma non è solo il
   numero: le tre fonti inglesi del log sono chiuse tutte e tre, quindi
   **stavolta il collaudo risponde a una domanda vera** — «il log di
   combattimento è italiano, adesso?» — e nessuna misura può rispondere al posto
   suo. Vedi «Quello che il collaudo deve guardare» qui sotto. `cgx-test.exe` è
   aggiornato (14/08) e contiene tutto, le sei toppe di `chara_func` comprese.
2. **Oppure `command.hsp`/`trait.hsp`**, che sono ~1.680 firme e i due file
   nominati più grossi che restano. ⚠️ Si leggono nei **menu** e non nel log: la
   lezione della 26ª dice di lasciarli dopo il collaudo, non prima. `trait.hsp`
   da solo vale **406** firme.
3. **Oppure `ai.hsp` (94) o `init.hsp` (133)**, che sono piccoli e già estratti.
   💡 `init.hsp` ha un interesse suo: è il file delle `#defcfunc` — `his2()`,
   `your()`, `godname()` — cioè le funzioni che **restituiscono inglese fuori da
   `lang()`** e su cui il progetto ha già tre dipendenze dichiarate.

### ⚠️⚠️ Le cinque cose che la prossima sessione deve sapere

1. ⭐⭐ **Le preposizioni che non si fondono sono la scorciatoia che il progetto
   non aveva mai dichiarato, e in questa sessione è servita quattro volte.**
   `name()` e `cdatan()` portano l'articolo dentro («il putit»), quindi «di », «a
   », «da », «in », «su » davanti a loro sono vietate — è la rete 8, che esiste
   dal lotto 009. ✅ Ma **«con», «contro», «per», «tra», «sotto», «sopra» NON si
   fondono**, e davanti a `name()` sono utilizzabili così come sono: «perse la
   vita **contro** X» (`:6850`), «si accasciò **sotto** il carico» (`:7039`), «il
   rapporto **con** X» (`:1080`), «la cera **sopra** X» (`:1169`).
   ⚠️ **E l'ha imposto la rete 8 sul campo**: `:1169` era scritta con «su», la
   rete l'ha fermata, e la correzione è stata cambiare **una parola** invece di
   riscrivere la frase. In nove lotti è il caso più economico che quella rete
   abbia mai prodotto. 💡 Fino a ieri la risposta al genitivo era sempre *girare
   la frase* — participio, `-ne` enclitico, sostanza soggetto. Adesso ce n'è una
   più a buon mercato, e va provata **per prima**.
2. ⭐⭐ **Un frammento che segue un nome vuole il PASSATO REMOTO, ed è la
   scoperta del lotto 003.** Le ventitré cause di morte si scrivono due volte:
   una riga di log che nomina chi muore, e un **frammento d'epigrafe** assegnato
   a `ndeathcause` che non nomina nessuno. `main.hsp:4409` lo incolla dentro
   «`cdatan(AKA) + cdatan(NAME) + <frammento> + " in " + mdatan(NAME)`», cioè
   subito **dopo il nome del morto**: in italiano «è morto di fame» concorderebbe
   col personaggio, e metà dei personaggi di Elona sono femmine. ✅ Il passato
   remoto italiano **non ha genere**: «morì di fame», «cadde dalle scale e morì»,
   «si tolse la vita», «bruciò fino a sparire». È la strada del participio della
   37ª spostata su un **tempo verbale**, e serve una frase intera per usarla.
   ⚠️⚠️ **E la cornice è in `main.hsp`, che non ha dizionario**: finché resta
   inglese l'epigrafe si leggerà «`<Il viandante> Sinaha morì di fame in
   Vernis`», metà e metà, con la preposizione sbagliata. È la dipendenza nota di
   `godname()` della 37ª in forma nuova. ⚠️ E quando si tradurrà la cornice:
   **il giapponese mette il luogo PRIMA del frammento e l'inglese dopo**, e
   l'italiano vuole «… morì di fame **a** Vernis».
3. ⚠️⚠️ **Il QUARTO punto cieco, e la battuta che era già morta da mesi.**
   `cnv_str` è la sostituzione di sottostringa di HSP, e il mod la usa per
   riscrivere una stringa **già composta**: `chara_func.hsp:6852` fa `cnv_str
   ndeathcause, "was killed by motuhegui", "was mauled to death by a bear"`. La
   chiave è scritta nell'**inglese di monte**, quindi appena la resa entra — o
   appena cambia una delle funzioni che compongono la stringa — non aggancia più.
   ⚠️ **Nessuno dei tre referti la vede**: `blocchi_en.py` guarda dentro
   `if ( en )`, `else_jp.py` dentro `if ( jp ) ... else`, `variabili_en.py` gli
   assegnamenti; qui non c'è nessun letterale da tradurre, c'è una **chiave che
   deve continuare a combaciare**. ✅ Misurato con **`scratchpad/cnv_str_en.py`**:
   **41 chiamate, 17 con la chiave in inglese**. ⚠️⚠️ **E quella dell'orso era
   già rotta**: `db_creature.hsp:37656` rende モツヘグイ «lo sbudellatore», quindi
   `cdatan(CDATAN_NAME, cc)` restituisce «lo sbudellatore» e la chiave non
   aggancia **da mesi**. La battuta è morta quando si è tradotto il bestiario e
   nessuna verifica l'ha detto. 💡 Le altre 15 stanno in `module.hsp` (il parser
   dei desideri) e `help.hsp`: sono **input**, non uscita, e vanno guardate
   quando si aprirà `module.hsp`.
4. ⚠️⚠️ **`:4520` è la QUARTA riga che il dizionario non può aggiustare, e la
   causa è una `lang()` che `estrai.py` NON VEDE.** `:4491` fa
   `locvar_item_cold_s = name(item_cold_arg1) + lang("の", your(item_cold_arg1))`,
   e `:4520` usa quella variabile come **prefisso**. Il ramo inglese di quella
   `lang()` è **una sola chiamata di funzione, senza letterale**: non produce
   firma — le firme di `chara_func.hsp` sono 342 e `:4491` non è fra loro —
   quindi il dizionario non la raggiunge né oggi né domani. `your()` restituisce
   `"'s"` o `"r"` (`init.hsp:2045`) fuori da `lang()`, e la riga leggerebbe «il
   putit**'s** …». ⚠️ **E la resa non può rimediare nemmeno nominando il
   proprietario**, perché il `name()` sta **dentro la variabile** e
   `funzioni_di_contenuto` non lo vede: l'inglese dichiara `['itemname']` e la
   rete 11 boccerebbe una resa che aggiunge `name()`. ✅ Toppata in due punti: il
   possessivo passa da **prefisso a suffisso** («, che X porta addosso»), che è
   la forma che l'italiano vuole comunque. 💡 **È una classe nuova da cercare
   altrove**: una `lang()` il cui ramo inglese è **solo funzioni** non compare in
   nessun conteggio, e nessuno ha mai contato quante siano.
5. ⚠️ **`dossier.py` non pesca i TERMINI, solo le frasi intere — e nel lotto 005
   sono state otto rese su trentacinque.** I sette premi di trama dicono
   「[愚者の魔石]を手に入れた！」 e `text.hsp:11576`-`:11630` aveva già reso
   **`[愚者の魔石]`**, la stessa parentesi quadra: il dossier non le aggancia
   perché confronta la **stringa intera**, e lì il termine è annegato dentro una
   frase più lunga. ✅ Trovate a mano cercando il termine. 💡 Otto su trentacinque
   è troppo per lasciarlo al caso: **è il candidato naturale al prossimo
   strumento** — un `termini.py` che cerchi le sottostringhe giapponesi del
   dizionario dentro le voci da fare.
   ⭐ **E il lotto di `calculation.hsp`, lo stesso giorno, mostra il rovescio
   esatto**: lì **sette rese su quarantaquattro** erano già decise e `dossier.py`
   le ha pescate **tutte e sette**, perché la frase giapponese coincideva per
   intero. Lo stesso strumento, i due estremi, in due lotti: **quando la frase è
   la stessa non sbaglia mai, quando il termine è annegato non vede niente.**
   Il confine è netto e si sa dov'è, ed è quello che rende lo strumento nuovo
   facile da scrivere.

### ⭐⭐ Quello che il collaudo deve guardare

**287 rese mai viste a schermo, ed è il debito più alto di sempre.**
⭐ **La prova che conta è una sola**: apri un combattimento e guarda se il log è
italiano. `proc.hsp`, `chara_func.hsp` e `calculation.hsp` sono le tre fonti
delle righe inglesi dello screenshot della 39ª e adesso sono chiuse tutte e tre
— se resta ancora inglese, viene da un file che **nessuno ha ancora sospettato**,
e trovarlo vale più di un altro lotto.

Poi le cose dove ho cambiato la struttura e non solo le parole:

| cosa | come arrivarci | perché guardarla |
|---|---|---|
| i ventidue di resistenza | bevi una pozione di mutazione, o fatti colpire da un elemento a cui resisti | «X **si sente il corpo** in fiamme», «X **si sente la pelle** avvolta in un'aura magica»: il **dativo riflessivo** è la forma nuova della sessione, e se suona male si vede subito |
| l'epigrafe della morte | muori (⚠️ **con un salvataggio di scorta**) | è l'unica riga con il **passato remoto**, e la cornice intorno sarà ancora inglese: serve a vedere quanto stona |
| il log di combattimento | un combattimento qualsiasi | ⚠️ **la prova vera della sessione**: dopo `proc.hsp` e `chara_func.hsp` il log dovrebbe essere quasi tutto italiano. Quel che resta inglese viene da `calculation.hsp` |
| «X storce il naso» | attacca un cittadino amichevole | parte a **ogni** azione ostile: è la riga più frequente di tutto il lotto 002 |
| la sella | cavalca un alleato | la parentesi si apre in una `lang()` e si chiude **undici righe dopo**, fuori da ogni traduzione: se la velocità non compare, la testa è rotta |
| il gelo sull'equipaggiamento | fatti colpire dal gelo con oggetti fragili addosso | è la **toppa** di `:4520`: deve dire «Il gelo manda in frantumi la spada, che il putit porta addosso», senza nessun «'s» |
| la sete e la fame | cammina finché non ti viene fame, e non mangiare | **quattordici** gradini nuovi, tre soglie per due bisogni: la scala deve sentirsi salire, da «Hai fame.» a «Di questo passo muori di fame!» |
| «si rimette in piedi» | fatti ribaltare, poi aspetta | è `calculation.hsp:1917`, una delle due righe che hanno fatto aprire il file: era inglese nello screenshot della 39ª |

### I sette lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `-002` | 2000-2999 | lo sguardo storto, l'ira, il velo sacro, i ventidue di resistenza | 58 **+1 rinviata** |
| `-003` | 6000-6999 | il danno, le tre urla, le ventitré morti e le loro epigrafi | **68** |
| `-004` | 4000-4999 | l'equipaggiamento aggredito dagli elementi, i sei modi buffi di morire | 33 **+2 rinviate** |
| `-005` | 7000-7999 | le ultime morti, i sette premi di trama, il cadavere da cui si scende | 35 |
| `-006` | 8000-8999 | i versi del dolore, peso e statura, il vomito, chi si sdoppia | 27 |
| `-007` | il resto | i rapporti, la tag-team, la sella, la coda sparsa | 22 |

E poi il file nuovo, chiuso in un colpo:

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `calculation-001` | tutto il file | il vortice di mana, la sete e la fame, i recuperi di stato | 44 |

⭐ **Il `-003` è il lotto più grosso mai fatto**, e batte le 59 del `proc-021`.

### 💡 Quello che i sei lotti hanno insegnato sul metodo

⭐⭐ **La duplicazione più alta mai vista in un lotto: 44 voci su 59.**
`resistmod` (`:2675`-`:2741`) e `resistmodh` (`:2769`-`:2835`) sono i due punti
da cui il gioco annuncia che una resistenza è salita o scesa — undici elementi
per due segni — e upstream li ha **ricopiati parola per parola**, cambiando solo
il nome della variabile. **Ventidue rese coprono quarantaquattro siti.** Batte il
menu delle tattiche del `proc-026` (dodici su trentaquattro) e l'X-Frame del
`-018` (nove su quarantadue). 💡 E succede di nuovo in piccolo nel `-006`:
`eatstatus` ed `eatstatusfood` sono la stessa coppia di frasi due volte.

⭐ **Il dativo riflessivo è la risposta italiana al possessivo inglese.** I
ventidue di resistenza dicono tutti 「name **の**身体は…」, 「name **の**魂は…」,
e l'inglese ci mette sopra il participio («is struck by», «is covered by»): due
trappole in una riga. ✅ «X **si sente** il corpo in fiamme», «X **si sente** la
pelle avvolta in un'aura magica» — il possesso resta implicito e la concordanza
cade su un nome di **genere fisso** («pelle» femminile, «corpo» maschile), non
sul personaggio. 💡 È la scoperta dei sedici recuperi del lotto 001 in forma
nuova: lì bastava il nome soggetto, qui serviva un costrutto che l'italiano ha e
l'inglese no.

⚠️ **La rete 13 ha gridato QUATTRO volte in un lotto solo (`-003`), ed è il
record.** «`<Medium damaged>`» per 中破 **e** 大破 (danno medio e danno grave
dello scafo, e il ramo lo conferma: `HP > MAX/4` contro `HP <= MAX/4`); «`melt
down`» per il cioccolato bollente **e** per l'acido; «`melted down`» per gli
stessi due nei frammenti; «`is healed`» per 再生した **e** 回復した. Tutt'e
quattro le distinzioni le fa il giapponese e le conferma il codice.

⚠️ **`itemname()` può essere plurale, e allora l'elemento diventa soggetto.**
`:4274`-`:4520` dicono tutte 「name の itemname は…」, e una resa come «X si vede
ridurre in cenere Y» dovrebbe accordare il verbo col **numero**, che non si
conosce. ✅ Il fuoco, il gelo e l'acido diventano **soggetti** — «Il fuoco riduce
in cenere Y», «Il gelo manda in frantumi Y» — così il verbo resta singolare
qualunque cosa arrivi, e il possesso si attacca in coda con «che X porta
addosso».

⚠️ **Un aggettivo invariabile vale quanto una frase girata.** `proc.hsp:10612`
rende 「は太った。」 «X diventa **più pesante**», e «pesante» sta bene con tutt'e
due i generi: si copia. Ma il gemello 「は痩せた。」 non può fare «più leggero»,
che **concorda**. ✅ Girato col verbo, «X perde peso», e la coppia esce
asimmetrica apposta.

⚠️ **Il gradino 1 di `txteledmg` è una CODA, e il possesso resta implicito.**
`txteledmg_arg1` vale 0, 1 o 2 — ferito, ucciso da chi attacca, morto — e il
gradino 1 il giapponese lo scrive **senza soggetto** («殺した。», «千切りにし
た。»), perché si attacca alla riga di sopra. ✅ La forma era già nel dizionario:
`:6843` dice «uccide sul colpo.» ⚠️ **E una coda italiana non può portare il
clitico** che l'inglese si concede (`him(...)`): «lo fa a listarelle»
concorderebbe.
⚠️ **Ma non è sempre una coda, e a deciderlo è l'INGLESE**: a `:4786` e `:4823`
il giapponese non ha soggetto e l'inglese ci ha rimesso un `name()`, che la rete
11 pretende. Le due forme convivono nello stesso blocco, ed è l'incoerenza di
monte che la rete propaga.

### ⚠️ La serie degli errori di monte passa da trentatré a trentasei

- ⭐ **`chara_func.hsp:8629` stampa una lettera sola.** Il giapponese è
  「name(A)の生命核はname(B)の遺伝子を獲得した。」, due personaggi; l'inglese
  scrive `name(A) + " get genes of " + _s(B) + "."`, cioè mette **`_s()` dove
  andava `name()`**. `_s()` restituisce «s» o niente, quindi la build inglese
  stampa «`X get genes of s.`» È la forma più povera della famiglia «personaggio
  sbagliato»: non ne nomina uno sbagliato, ne stampa la **desinenza**;
- `:2021` dice «`glares at you`» dove il giapponese dice solo 「嫌な顔をした」, e
  il ramo (`RELATION == 10` e basta) non sa chi sia la sorgente: l'inglese
  **nomina il giocatore** in una riga che non può saperlo;
- `:6196` scrive «`<Medium damaged>`» anche per 大破, il danno **grave**.

💡 **E tre righe dicono due cose opposte nelle due lingue**, tutte risolte sul
giapponese: `:1668` («questa creatura è perfetta da cavalcare» contro «`You feel
comfortable`» — il ramo guarda una proprietà **della bestia**), `:8007`
(「くっ！」, un mugolio, contro «`Kill me already!`») e `:7002` (闇のゲーム, il
**Gioco delle Ombre** di Yu-Gi-Oh, contro «`a card game`» con una gabbia
inventata).

💡 **Il perimetro dichiarato passa dal 49% al 50% e il totale vero dal 36% al
37%.** Le 287 rese valgono **un punto** sul conto vero: il quadro della 38ª non
cambia di una virgola — quel che resta è più grande di quel che è stato fatto, e
la parte più grossa **non ha firma `lang()`**.
💡 E i file con `lang()` che hanno un dizionario passano da **15 a 16 su 54**:
le stringhe **mai estratte** scendono da 12.620 a **12.573**. Quarantasette in
meno su dodicimila — è la proporzione vera del lavoro che resta, e serve a non
farsi ingannare da due file chiusi in un giorno.

---

## La trentanovesima sessione

⭐⭐ **`proc.hsp` è CHIUSO.** Quattro lotti — `023`, `024`, `025`, `026` — **97
rese e una rinviata a toppa**, dal 91% al **100%**: 1.091 firme su 1.098, e le
sette che restano sono tutte rinviate apposta. Si aggiunge a `db_item`,
`item_data`, `skill`, `custom_tweaks`, `adv`, `action`, `text`, `buff`,
`db_creature`, `chips` e `custom_enemyevolution` — ed è **il più letto di
tutti**, perché è il log che scorre a ogni singolo combattimento. Otto spinte,
catena verde, `cgx-test.exe` rifatto.

⭐⭐ **E poi la sessione ha fatto il collaudo, dopo tre che non lo facevano, e il
collaudo ha cambiato la coda del progetto.** Vedi «Quello che ha trovato il
collaudo» qui sotto: in un solo screenshot c'era la prova che le rese nuove
funzionano, una resa da correggere che compariva **cinque volte in uno schermo**,
e la scoperta che il log è ancora mezzo inglese **e non per colpa di
`proc.hsp`**. Da lì è partito `chara_func.hsp`, che è il file nuovo.

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** e l'albero di lavoro è pulito: non c'è niente da recuperare,
si riparte da `git fetch && git status -sb` e dalle otto verifiche d'apertura.

1. **`chara_func.hsp`, lotto 2.** Il primo (`3000-3999`, gli stati) è fatto.
   L'estrazione è già in `lavoro/_chara_func.jsonl` — **è aggiornata a prima**
   del lotto 1, quindi la prima cosa è rifarla:
   `python -m strumenti.estrai chara_func.hsp --da-tradurre --uscita lavoro/_chara_func.jsonl`
   (attese **247** voci). Poi `dossier.py` sulla zona scelta e
   `assembla-lotto.py NNN scratchpad/lotto-fase4-proc-026.py <da> <a> <cartella> chara_func.hsp`.
   💡 La zona più densa è `6000-6999` (**68**: cure, urla e tutte le cause di
   morte); la più letta dopo gli stati è `2000-2999` (**59**, e dentro ci sono
   `glares at you` e `gets furious!`, che partono a **ogni** azione ostile).
2. **Oppure `calculation.hsp`, che sono 44 voci e chiude un file intero** —
   `lavoro/_calculation.jsonl` è già estratto. Ci stanno `stands up` e
   `released from bind`, viste a schermo.
3. **Oppure il collaudo**, che resta il debito più grosso: vedi «La prima cosa
   da fare». `cgx-test.exe` è aggiornato (14/08, 18:25) e contiene tutto,
   correzione della schivata compresa. Il salvataggio è salvato in
   `save-backup\pre-collaudo-20260814-39a` **prima** che `gain_spact` lo
   modificasse.

### ⚠️⚠️ Le cinque cose che la prossima sessione deve sapere

1. ⭐⭐ **Il file da fare adesso è `chara_func.hsp`, e a dirlo è stato lo
   schermo, non una misura.** La 39ª aveva scritto in questa stessa pagina che
   dopo `proc.hsp` venivano `command.hsp`/`trait.hsp` oppure il testo fuori
   perimetro. **Lo screenshot del collaudo ha ribaltato la risposta**: con
   `proc.hsp` al 100% il log di combattimento è ancora mezzo inglese, e ogni
   riga inglese viene da `chara_func.hsp` (`glares at you`, `gets furious!`,
   `is frozen in fear`, `is incontinent`) o da `calculation.hsp` (`stands up`,
   `released from bind`). Sono le righe che si infilano **fra** una riga
   italiana e l'altra.
   💡 **`chara_func` + `calculation` = 330 firme, cinque o sei lotti**, contro
   le 1.560 di `command.hsp`, che si legge nei **menu** e non nel log. È la
   lezione della 26ª — *la frequenza, non l'elenco* — trovata guardando lo
   schermo invece che contando le firme. ✅ Il primo lotto è fatto
   (`fase4-chara_func-001`, 39 rese); ne restano **247** più le 44 di
   `calculation.hsp`.
   ⚠️ **Attenzione ai numeri di riga**: `chara_func.hsp` nella build ha
   **62 righe in meno** del sorgente (8.923 contro 8.985) per via delle toppe,
   quindi chi incrocia dizionario e build guarda la riga sbagliata di sessanta
   posizioni. È il caso di `text.hsp` della 37ª moltiplicato per sessanta: **si
   legge il `SORGENTE`**, sempre.
2. ⭐⭐ **`:24107` è la seconda riga del progetto che il dizionario non può
   aggiustare**, dopo `:11481` della 36ª, e la ragione è nuova.
   `SKILL_SPACT_JYUSOU_GOUSHIN` è dichiarata **`TARGET_TYPE_SELF_ONLY`**
   (`skill.hsp:1411`) e `proc.hsp:7565` fa **`tc = cc`**: chi lancia e chi
   subisce sono lo stesso personaggio. Il giapponese lo dice
   (「自分自身に強烈な呪いをかけた！」) e `skill.hsp:1413` lo conferma («Si
   maledice e si rafforza»). ⚠️ **L'inglese di monte invece nomina due
   personaggi**, perché è `proc.hsp:14703` — l'incantesimo Maledizione, dove i
   due sono davvero due — **ricopiata parola per parola**: a schermo stampa lo
   stesso nome due volte. 💡 **È il rovescio esatto di `:18280` della 38ª**: lì
   l'inglese aveva **un** `name()` e il giapponese due, e bastava nominare il
   soggetto; qui l'inglese ne ha **due** e il giapponese uno, e nessuna frase
   italiana nomina due volte lo stesso personaggio senza sembrare rotta.
   ✅ Toppata e rinviata. `toppe.jsonl` passa da 302 a **303**, `rinviate.jsonl`
   da 14 a **15**.
3. ⚠️⚠️ **Un inglese solo per TRE giapponesi diversi, ed è il record del
   progetto.** `:26080`, `:26120` e `:26158` hanno tutt'e tre
   «`name(cc) + " gaze" + _s(cc) + " " + name(tc) + "."`» e sono **tre azioni
   speciali diverse**: `EYE_OF_MANA` (「魔力を込めて睨み付けた」, `dmgcon
   CONDITION_MPOISON`), `EYE_OF_ILLUSION` (「幻影を見せた」, danno
   `SKILL_RES_MIND`) e `EYE_OF_STIFFEN` (「妖しい眼光を放った」, danno
   `SKILL_RES_NERVE` più `CONDITION_BIND`). L'inglese ha appiattito tre effetti
   in una riga; il giapponese e il codice li distinguono. La rete 13 è nata
   nella 37ª su una coppia: qui trova una **terna**.
4. ⭐ **Nasce un termine che servirà a un altro file: 姉波動 è l'«Onda
   Sororale».** `proc.hsp:25798`-`:25823` sono le **prime** righe del progetto
   a nominarlo, ma il grosso della materia — una catechesi intera sul culto
   delle sorelle maggiori — sta in `chat.hsp:6575`-`:6676`, che è uno dei 40
   file **senza dizionario**. ⚠️ **E l'inglese lo chiama in tre modi**: «Big
   Sister Energy», «sisterly energy», «Sistergy Wave»; il giapponese sempre
   姉波動. ✅ Messo in `glossario.md` **subito**, perché è esattamente la
   situazione del `Bolt` della 35ª — una scelta presa una volta e da applicare
   in un altro file mesi dopo.
5. ⚠️ **Il tipo della voce decide la resa, non il senso.** `:26940` è
   `lang(cdatan(CDATAN_NAME, tc) + "は矢弾を装備していない。", "You need to
   equip ammo.")`: il ramo giapponese **nomina** il personaggio, quello inglese
   no, e `estrai.py` classifica sul ramo che la resa sostituisce. Quindi è una
   **statica**, la resa è testo nudo, e **non può portare il nome** che il
   gemello `action.hsp:15268` ha — lì l'inglese era dinamico. Stessa riga, due
   tipi, due rese diverse, e la rete 3 grida per una ragione giusta.

### ⭐⭐ Quello che ha trovato il collaudo, ed è la parte che conta

**Un solo screenshot del log, e ha reso tre cose diverse.** La console di debug
lo rende possibile in dieci minuti: **F12 → `wizard`, `gain_spact`,
`gain_spell`** dà tutte le azioni speciali e tutti gli incantesimi, e senza
`gain_spact` metà delle rese della 39ª non è raggiungibile.

1. ✅ **Le rese nuove funzionano, e la toppa di `:24107` è entrata.** A schermo:
   «`Il viandante si scaglia addosso una maledizione tremenda!`» — **un nome
   solo**, che era il rischio. Più «`Il viandante porta addosso un elmo di
   bronzo [0,1], che brilla di luce nera.`», i **tre sguardi tutt'e tre
   diversi**, «`copre d'insulti`», «`ricuce il punk in un lampo!`», e le teste
   «… e» con il `-ne` enclitico in combattimento vero.
   💡 E «`Lui rispetta la legge di questa pacifica citta'.`» **non è un
   difetto**: è `he(tc, 1)`, che `init.hsp:1822` traduce già in «lui»/«lei».
2. ⚠️⚠️ **Una resa sbagliata che compariva CINQUE volte in uno schermo**, e che
   otto mesi di catena verde non avevano visto: «`Il viandante schiva Kefry.`»
   (`action.hsp:5616`). Il giapponese dice 「name(cc) **の攻撃を** 避けた」,
   cioè «l'attacco **di** cc», e l'inglese butta via 攻撃 lasciando il nome
   nudo: in inglese «X evades Y» regge, in italiano «schiva Kefry» dice
   un'altra cosa. ⚠️ E il genitivo era chiuso in partenza (rete 8: «l'attacco
   di il putit»). ✅ Corretta con la forma della 37ª — «**X attacca, ma Y
   schiva**» — **e con lei la parata due righe sopra** (`:5598`), che aveva lo
   stesso difetto e che nessuno aveva mai guardato. `:5601` e `:5619` restano:
   lì l'inglese aveva scelto il soggetto giusto.
   💡 **È la lezione della 32ª e della 36ª una terza volta**: la catena verde
   non dice niente su come suona una frase a schermo.
3. ⭐⭐ **Il log è ancora mezzo inglese, e non per colpa di `proc.hsp`** — vedi
   il punto 1 delle cinque cose. Ogni riga inglese dello screenshot è stata
   rintracciata: `chara_func.hsp:2021`/`:2033`/`:2040` (`glares at you`, e parte
   a **ogni** azione ostile), `:2047` (`gets furious!`), `:6441`, `:8317`;
   `calculation.hsp:1917` (`stands up`) e `:1929`; `command.hsp:16987`
   (`Really attack X?`) e `:17278`; `event.hsp` (venti siti identici per
   `travel experience`).

### ⚠️ La serie degli errori di monte passa da ventotto a trentatré

Tre sono della famiglia «personaggio sbagliato» e uno è di forma nuova:

- `:25071` e `:25119` dicono `name(tc)` dove ad agire è `cc` — è il
  purificatore che emette l'onda, non chi la riceve — e stanno **nella stessa
  azione, a cinquanta righe di distanza**;
- ⭐ `:25178` scrive **`name(tc)` due volte**: `name(tc) + " slashed " +
  name(tc) + " with holy power."` Il primo dei due è `cc`, lo dice il
  giapponese e lo conferma il codice, che fa partire l'animazione su `tc`. È il
  gemello di `:24107` — lì l'inglese aggiunge un personaggio che non c'è, qui
  ne sbaglia uno che c'è;
- `:24107`, la riga toppata del punto 2;
- ⭐ **`chara_func.hsp:3037`, ed è la TERZA riga del progetto che il dizionario
  non può aggiustare** dopo `proc.hsp:11481` (36ª) e `:24107`. La coppia
  「濡れた」/「姿があらわになった」 compare **tre volte** nello stesso blocco —
  chi subisce, il compagno di tag-team, chi ti cavalca — e nel ramo inglese
  dell'ultima upstream ha ricopiato quella del tag-team cambiando **due**
  riferimenti su tre: `is(gdata(GDATA_RIDER))` e `his(gdata(GDATA_RIDER))` sono
  giusti, il `name()` è rimasto `name(ttc@con)`. 💡 La rete 11 non lascia
  scampo perché `funzioni_di_contenuto` conta **`gdata` come contenuto**:
  l'inglese dichiara `['name']`, la resa giusta dichiarerebbe
  `['name', 'gdata']`. ✅ Toppata e rinviata.

💡 **E `:26948` è un difetto di un'altra classe: upstream butta via
l'informazione.** Il giapponese dice 「name は <tipo> に切り替えた。」, l'inglese
dice **«Current Ammo Type»** e basta: il tipo di munizione che `:26945` prepara
in `s` — «Normali» / «Illimitate» — nel ramo inglese **non compare da nessuna
parte**, e la resa italiana non può rimetterlo. Non è un errore, è una perdita.

### 💡 Quello che i quattro lotti hanno insegnato sul metodo

⭐ **Il lotto 026 ha la percentuale di copie più alta di tutto il file: dodici
su trentaquattro**, e otto vengono da un posto solo — `action.hsp:15232`-`:15313`,
il **menu delle tattiche**, che `proc.hsp:26858`-`:26986` ristampa parola per
parola. È l'X-Frame del lotto 018 in grande, e `dossier.py` le ha pescate tutte
e dodici senza che servisse cercarle.

⚠️ **Lo stesso giapponese può avere DUE inglesi diversi**, ed è il rovescio
della rete 13. 「パワーゲージが足りない。」 sta a `:20054` e a `:20150`, e
l'inglese lo scrive in due modi per **due soglie diverse** (5 e 50 punti di
barra). La resa è una sola, e la impone la rete 4. La differenza non la impone
il sorgente: la impone lo stile di chi ha tradotto in inglese.

⭐ **I quattro versi della necromanzia non stanno in `skill.hsp`: esistono solo
in `proc.hsp`.** 「魔力増強」, 「生命の転換」, 「外道式炸裂弾」,
「コールアンデッド」 sono le intestazioni che il gioco stampa quando scegli una
voce del menu `SKILL_SPACT_NECRO_FORCE`, e cercarle nel dizionario non dà
niente. ✅ L'ancora sono le **etichette del menu**, che `text.hsp:2089`-`:2101`
ha già rese: «Potenzia / Cura / Fai esplodere / Raduna i non-morti». 💡 E
「コールアンデッド」 si traduce lo stesso, benché sia katakana: `invariati.md`
dichiara invariato **il nome che nemmeno l'originale legge come descrizione**,
non il katakana in sé, e le altre tre della serie sono kanji che si rendono.

⚠️ **`:25206` e `:25216` sono i due rami dello stesso `if` con lo stesso
inglese.** «`name(cc) + " sewed " + name(tc) + " up quickly!"`» sta per
「縫い**つけた**」 sul nemico — e il codice mette `CONDITION_BIND` — e per
「**縫合**した」 sull'alleato, dove **dimezza** `CONDITION_BLEED`. Inchiodare e
ricucire. La rete 13 le ha viste, il codice ha deciso.

💡 **La strada del participio e quella del genitivo reggono da sette lotti**, e
in questa sessione hanno lavorato più delle reti: **diciassette rese** girate
in partenza per non far concordare un aggettivo o non far fondere una
preposizione con `name()`. La rete 8 non ha gridato **nemmeno una volta** in
quattro lotti — non perché sia stata indulgente, ma perché dopo quattro
sessioni il genitivo davanti a `name()` non si scrive più. Il caso più stretto
è `:26347`, che ne aveva **due nella stessa frase** («la voce **di** X risuona
nel cuore **di** Y»): risolto coi due nomi soggetti, «X fa risuonare la voce, e
Y la sente nel cuore!».

### ⚠️ Lo strumento che ha rischiato di mangiarsi `toppe.jsonl`

⚠️⚠️ **Uno script di questa sessione ha troncato `toppe.jsonl` a ZERO byte, e a
salvarlo è stato solo `git checkout`.** Apriva il file in scrittura e componeva
il testo dentro `write()`: un surrogato nel motivo ha fatto esplodere
`UnicodeEncodeError` **dopo** che l'apertura aveva già troncato il file. 231.878
byte di toppe, spariti per un `\ud83d` scritto a mano invece di un 💡.
✅ **La forma giusta è: comporre, codificare in memoria, e solo allora aprire.**
`riscrivi()` nello script della toppa lo fa. 💡 Ed è un'altra faccia della
regola delle due macchine: il lavoro era spinto, quindi c'era da dove tornare
indietro. Se fosse successo a fine sessione, prima della spinta, sarebbe stato
irrecuperabile.

✅ **`assembla-lotto.py` ha imparato la terza ancora, `RINVIATE`.** Il blocco
copiato dal modello porta `RINVIATE = set()`, e senza l'ancora l'unico modo di
dichiarare una rinviata era **modificare a mano il file generato** — cioè
esattamente la cosa che quello script esiste per impedire. Adesso basta un
`rinviate<numero>.py` facoltativo nella cartella.

### I quattro lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `-023` | 20000-20999 | il poker, il jolly variabile, i soldi per farsi risparmiare, il finto dogeza, il menu della necromanzia | 20 |
| `-024` | 24000-24999 | l'automaledizione, lo Scambio da squalo, la posa, la marcatura del territorio, le scosse elettriche | 13 **+1 rinviata** |
| `-025` | 25000-25999 | le onde, il filo e l'ago, l'esplosivo, la gravità, l'etere, l'Onda Sororale | 30 |
| `-026` | 26000-26999 | i tre sguardi, la voce, le pozioni, lo zaino, il menu delle tattiche | 34 |

E poi, dopo il collaudo, il primo lotto del file nuovo:

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `chara_func-001` | 3000-3999 | i dodici stati, i sedici recuperi, il bagnato | 39 **+1 rinviata** |

⭐ **È il blocco più partecipiale del progetto: l'inglese scrive DODICI stati su
dodici col participio** — «`is blinded`», «`was knocked down`», «`is
paralyzed`», «`is poisoned`»… — e in italiano concorderebbero tutti col
personaggio. Il giapponese non ha il problema perché usa 「は…た」, che è
neutro. ✅ Le due strade si dividono il lavoro a metà: il **verbo riflessivo o
intransitivo** («si addormenta», «si ubriaca», «si ammala», «cade a terra») e la
**sostanza come soggetto** («La cecità coglie X», «La paralisi coglie X», «Il
veleno invade X»). 💡 La forma «La \<cosa\> coglie X» non è nuova: era già di
`proc.hsp:13389`, ed era l'unica delle cinque già decisa.
⚠️ **E i sedici recuperi hanno il problema gemello, di genitivo**: l'inglese
dice «`X` `your(X)` `bleeding stops`», «`recover from` `his(X)` `illness`», e in
italiano diventerebbe «il sangue **di** X». Tutti girati col nome soggetto e il
possesso implicito — «X non sanguina più», «X si rimette dalla malattia».

💡 **Il perimetro dichiarato passa dal 47% al 49%**, e il totale vero resta al
**36%**: le 97 rese valgono due punti dentro `lang()` e nemmeno uno sul conto
che comprende le 5.284 descrizioni degli oggetti e i quattro file di `data/`.
Il quadro della 38ª non cambia — quello che resta è più grande di quello che è
stato fatto, e la parte più grossa **non ha firma `lang()`**.

---

## La trentottesima sessione

⭐ **La 38ª è la sessione più produttiva del progetto su un file solo, e quella
che ha scoperto quanto manca davvero.** Sei lotti su `proc.hsp` — `017`…`022` —
**285 rese, dal 65% al 91%**, otto spinte, zero collaudo. Ma la cosa che conta
non è un lotto: è che alla domanda «a che punto siamo» il progetto rispondeva
**47%** e la risposta vera è **36%**.

⭐ **E la zona densa è chiusa.** I lotti `020`-`022` hanno fatto tutto il
`21000-23999` — **156 voci in tre lotti**, il 61% di quel che restava — e `020`
e `021` sono i due lotti più grossi mai fatti (55 e 59 rese). Di `proc.hsp`
restano **98 voci**, tutte oltre la riga 20000.

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

   **Totale reale ~31.306, fatto il 36%** (era 35% a metà sessione: i sei lotti
   valgono un punto). ⚠️ E in **caratteri** il divario è
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

### ⭐ E la scoperta dei tre lotti della zona densa

⚠️⚠️ **Le otto parole del terreno portano il loro ARTICOLO dentro.** A
`proc.hsp:22088`-`:22112` il sorgente costruisce `s` scegliendo fra otto parole —
糸/web, 闇/darkness, 酸/acid, エーテル/ether, 炎/fire, 液体/potion, 光/light,
煙/smoke — e a `:22117` la usa come **soggetto**. In italiano quelle otto hanno
**generi diversi** («la ragnatela», «l'acido», «il fuoco», «la luce»), quindi la
frase ospite non può mettere un articolo fisso: ✅ l'articolo va **dentro
ciascuna delle otto**, come `db_item.hsp` fa con `ioriginalnamearticolodet`. E la
frase dice «Quasi avesse **vita propria**», perché «Come se fosse vivo» avrebbe
concordato con `s`.
💡 **È la terza forma dello stesso problema**, dopo `itemname()` della 35ª e
`valn` da soggetto della 36ª: *una variabile che porta un nome porta anche il
suo genere, e la frase che la ospita non lo sa*.

⚠️⚠️ **`proc.hsp:21110` interpola `tc` NUDO, cioè il numero della creatura dove
va il nome**: `name(cc) + " explode with " + tc + "."`. La build inglese stampa
«explode with 37.» ⚠️ **È un candidato a toppa, non a traduzione** — la riga
andrebbe corretta `+ tc +` → `+ name(tc) +` — e finché non si fa, la rete 11
concede un solo `name()` e il bersaglio resta implicito.

⚠️ **La serie degli errori di monte è a ventotto**, e la 38ª ne ha aggiunti
diciassette. Le famiglie sono tre e adesso hanno un nome:
il **personaggio sbagliato** (`:18280`, `:18309`, `:18429`, `:18744`, `:22228`,
`:22896`, `:23613`), la **riga ricopiata da un'altra** (`:16001`, `:16679`,
`:17149`, `:21572`, `:22620`, `:22639`, `:22690`), e **un inglese per due
giapponesi** (`:17114`/`:17120`, `:21991`/`:21994`).

⚠️ **`verifica` ferma i versi delle mosse già invariate**, e succederà ancora:
`Ensemble!` (lotto 019) e `*Kamikakushi* ` (lotto 022) sono **stringhe diverse**
da `Ensemble` e `Kamikakushi`, perché il confronto è sulla stringa intera.
Vanno dichiarate a parte in `invariati.md`.

⚠️ **E una statica con una battuta fra virgolette vuole le virgolette
protette** (`\"`), come fa l'inglese di monte: una `"` nuda chiuderebbe in
anticipo la stringa HSP che scrive `applica.py`. Capitato la prima volta nel
lotto 020, sulle cinque code della spazzolatura.

💡 **Nota per chi copia le reti**: se manca una resa, il messaggio della rete 1
**non si vede mai** — la rete 8 dereferenzia `RESE` prima del controllo di
`errori`, e quel che esce è un `KeyError` nudo. Vale la pena spostare il
controllo subito dopo la rete 2.

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

### I sei lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `-017` | 15500-16999 | navi, ricarica, muri e porte, azioni speciali di barra, meteore, cannone di sabbia, circolo di lettura | 49 |
| `-018` | 17000-17999 | scrigni, Duplibacchetta, jujitsu, X-Frame, il legame, la richiesta d'aiuto | 42 |
| `-019` | 18000-19999 | plagio, ipnosi, scansione dati, trasfusione, ensemble, pesca dimensionale, origami | 38 |
| `-020` | 21000-21999 | necromanzia, incitamento, taglialegna, spazzolatura e coccole | **55** |
| `-021` | 22000-22999 | la melma che scioglie, il magnetismo, il ranch, la stretta e il bacio | **59** |
| `-022` | 23000-23999 | polline, ShikiOrigami, tortura, i dadi del destino, le sette invocazioni di Kamui | 42 |

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

✅ **Spinto di nuovo a fine 30ª, 31ª, 32ª, 33ª, 34ª, 35ª, 36ª, 37ª, 38ª, 39ª e
40ª**, sempre dal portatile. Tutt'e undici hanno aperto con
`git fetch && git status -sb` e tutt'e undici hanno trovato le copie allineate:
la regola ha tenuto **undici volte di fila**.
💡 La 40ª ha spinto **sette volte** — quattro lotti, la chiusura dei tre finali,
la ripresa e `calculation.hsp` — una per risultato chiuso, ed è il numero più
alto del progetto.
⚠️⚠️ **E nella 39ª la spinta ha fatto da rete di sicurezza per la prima volta,
non da comodità.** Uno script della sessione ha troncato `toppe.jsonl` a **zero
byte** — 231.878 byte di dati — e a salvarlo è stato `git checkout`, cioè il
fatto che il lavoro fosse **già spinto**. Se fosse successo prima della prima
spinta, non ci sarebbe stato niente da cui tornare indietro.
💡 La 39ª ha spinto **otto volte** — quattro lotti di `proc.hsp`, la chiusura,
la correzione trovata a schermo, il primo lotto di `chara_func` e la seconda
chiusura. È la seconda sessione dopo la 38ª a chiudersi **due volte**, ed è
giusto così: fra la prima e la seconda ci sono stati il collaudo e un cambio di
rotta sul file successivo, cioè le due cose che la prossima sessione deve sapere
più di ogni altra.
💡 La 38ª ha spinto **otto volte** — sei lotti e due referti — una per
risultato chiuso, ed è il numero più alto del progetto dopo le sette della 35ª.
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

⚠️⚠️ **Il collaudo, e il debito è sceso per la prima volta dalla 36ª.** La 39ª
ha aperto il gioco dopo tre sessioni che non lo facevano, e in un solo
screenshot ha confermato una dozzina di rese nuove e trovato **una resa
sbagliata che compariva cinque volte in uno schermo** (vedi «Quello che ha
trovato il collaudo» in cima). ⚠️ **Ma il grosso resta**: le 121 della 36ª, le
146 della 37ª e le **285 della 38ª** non sono ancora state guardate, e delle 97
della 39ª ne è stata vista **una dozzina**. `cgx-test.exe` è stato rifatto a
fine 39ª e contiene tutto.

⭐ **E adesso si sa come farlo in dieci minuti**: **F12 → `wizard`,
`gain_spact`, `gain_spell`**. `gain_spact` dà **tutte** le azioni speciali in un
colpo, ed è la chiave: senza, metà delle liste qui sotto non è raggiungibile.
⚠️ Modifica il salvataggio per sempre, quindi prima si copia
`elonaplus2.31\save\sav_oldpz` in `save-backup\pre-collaudo-<data>`.

💡 **Le 97 della 39ª chiudono `proc.hsp` e stanno tutte in azioni speciali
identificabili**, quindi si collaudano una per una. ✅ Già viste: la toppa
dell'**automaledizione** (un nome solo), i **tre sguardi** (tre frasi diverse),
l'**Insulto**, la **Sutura istantanea** sul ramo alleato. ⚠️ Da guardare, in
ordine:

| cosa | come | perché |
|---|---|---|
| ✅ **l'automaledizione** | azione speciale **Jyusou Goushin** (`skill.hsp:1412`) | **guardata il 14/08 e la toppa è entrata**: «`Il viandante si scaglia addosso una maledizione tremenda!`», un nome solo |
| ✅ i tre sguardi | **Sguardo di mana**, **Sguardo illusorio**, **Sguardo irrigidente** | **guardati**: tre frasi diverse dove l'inglese ne diceva una sola |
| ⚠️ la **Sutura istantanea** su un **nemico** | ↑ il ramo alleato è già stato visto («ricuce X in un lampo!») | manca il ramo ostile: deve dire «**cuce** X **sul posto** in un lampo!» |
| il menu della necromanzia | azione speciale **Forza necromantica**, tutte e quattro le voci | i quattro versi (`*Potenziamento magico*`, `*Conversione vitale*`, `*Ordigno spietato*`, `*Richiamo dei non-morti*`) e la voce di menu **Evoca non-morti**, che è l'unica riga della sessione che passa da `*prompt_key` |
| il poker | azione speciale **Forza del poker**, con la barra sotto il 100% | «La barra non basta.», «Non hai formato nessuna combinazione.», e «**Le carte** colpiscono X» al plurale — non «La carta», che è lo ShikiOrigami |
| il jolly variabile | azione speciale **Cambio jolly** su un alleato | il nome della creatura diventa `{Jolly Variabile}`: si legge nella lista alleati, non solo nel log |
| il menu delle tattiche | il menu degli ordini agli alleati, tutte le voci | otto rese **copiate da `action.hsp`**: devono uscire identiche a quelle di là. È la prova che le dodici copie del lotto 026 sono giuste |
| l'Onda Sororale | usa lo **Sguardo soggiogante** su una sorella maggiore, che lo para | quattro rese col termine nuovo. ⚠️ `chat.hsp` dirà ancora «Big Sister Energy» in inglese: **non è un difetto della resa**, è la dipendenza nota dai 40 file senza dizionario |
| la marcatura del territorio | fatti marcare da un animale | «X freme di **umiliazione**», non «di rabbia»: è la riga dove l'inglese aveva riciclato la frase dell'ira |
| il filo e l'ago | azione speciale **Sutura istantanea** su un **nemico** e poi su un **alleato** | stesso inglese, due rese opposte: «cuce X sul posto» contro «**ricuce** X» |

💡 **Le 285 della 38ª sono log di combattimento e azioni speciali**, quindi si
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
| ⭐ **le otto parole del terreno** | lancia Ragnatela, Nebbia di tenebra, Muro di fuoco… poi **Vincolo informe** su un nemico che ci sta dentro | è la scoperta della sessione: dev'uscire «Quasi avesse vita propria, **la ragnatela** avvolge X!» con l'articolo giusto per tutt'e otto. Se una esce senza articolo, o con quello sbagliato, si vede subito |
| la spazzolatura | spazzola un animale del ranch cinque volte | i cinque gradini sono **code** che si attaccano al nome, e portano una battuta fra virgolette: se le virgolette non escono, la protezione `\"` è saltata |
| la mungitura | mungi un animale del ranch | quattro rese dove il giapponese non nominava nessuno e l'inglese sì |
| la tortura e i dadi | azioni speciali **Tortura** e **Dadi del destino** | `:23613` deve dire che cede **chi subisce**, e i dadi devono stampare il numero dopo «Il tiro dà...» |
| le sette invocazioni | azione speciale **Kamui**, sette volte di fila | escono in italiano fra `<>`; l'ottava, `*Kamikakushi* `, resta in giapponese romanizzato **apposta** |

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
2. ✅ **`proc.hsp` è CHIUSO nella 39ª**, a **1.091 su 1.098 (100%)**: le 7 che
   restano sono tutte rinviate apposta (una riga commentata, «Party Room», i due
   nomi di nave, `:11481`, `:11796` e `:24107`, tutt'e tre risolte da toppa o
   dentro un blocco spento). I quattro lotti della 39ª sono `-023`
   (20000-20999), `-024` (24000-24999), `-025` (25000-25999) e `-026`
   (26000-26999).

   ⚠️ **Prima di aprire il file dopo, copiare le quattordici reti** da
   **`scratchpad/lotto-fase4-proc-026.py`**, che è il modello più recente. ⚠️ Le
   reti 3, 4 e 8 sono state **corrette perché sbagliavano loro**, e la 12 e la 13
   sono nuove: si copia il file, non si riscrive a memoria.
   ✅ **E adesso la regola è meccanica**: `scratchpad/assembla-lotto.py` copia il
   blocco dal modello, cambia `USCITA`, `DA, A` e — dalla 39ª — `RINVIATE`, e
   **rilegge quel che ha scritto** confrontandolo col modello carattere per
   carattere. Bastano due file scritti a mano — la testa col docstring e le rese
   — più un `rinviate<numero>.py` facoltativo, e il resto è copiato:

   ```powershell
   & $py scratchpad/assembla-lotto.py 027 scratchpad/lotto-fase4-proc-026.py 0 99999 <cartella>
   ```

   ⚠️ **Le reti hanno un difetto noto e ancora aperto**: se manca una resa, il
   messaggio della rete 1 **non si vede mai**, perché la rete 8 dereferenzia
   `RESE` prima del controllo di `errori` e quel che esce è un `KeyError` nudo.
   Vale la pena spostare il blocco `if errori:` subito dopo la rete 2.

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
3. ⭐⭐ **`chara_func.hsp`, e la scelta l'ha fatta il collaudo.** Questo punto
   diceva «`command.hsp`/`trait.hsp` oppure il fuori perimetro», ed era
   **sbagliato**: lo screenshot ha mostrato che il log resta mezzo inglese
   anche con `proc.hsp` al 100%, e le righe che lo sporcano stanno qui.

   - ✅ **`chara_func.hsp`, 247 firme, e `calculation.hsp`, 44.** Primo lotto
     fatto (3000-3999, gli stati e i recuperi). Le zone restanti, tutte
     tematicamente pulite: `6000-6999` **68** (cure, urla e **tutte le cause di
     morte**, log e giornale), `2000-2999` **59** (azioni ostili, i due blocchi
     gemelli di 22 messaggi di resistenza, la malattia dell'etere),
     `4000-4999` **35** (danni elementali agli oggetti, le morti scherzose),
     `7000-7999` **35** (premi, pietre magiche, cadaveri), `8000-8999` **27**
     (peso, altezza, anoressia, geni), `1000-1999` **18** (relazioni,
     cavalcature, tag-team). ⚠️ `calculation.hsp` **non ha ancora un
     dizionario**: è un file intero da aprire, e ci stanno `stands up` e
     `released from bind`, che si leggono a ogni combattimento.
   - **`command.hsp` e `trait.hsp`**, ~1.966 firme mai toccate. È la strada
     nota, ma si legge nei **menu**, non nel log. ⚠️ `command.hsp` è anche il
     file che **disegna** i `buffdesc`, quello di «`Really attack X?`» e
     «`Do you want to save the game and exit?`», e quello che porta 10 delle 68
     righe inglesi fuori da `lang()` ancora intatte.
   - ⚠️ **Il testo fuori perimetro**, cioè le **5.284 descrizioni degli
     oggetti** di `db_item.hsp` e i **quattro file di `data/`** (~2.900 righe,
     117.977 caratteri di prosa inglese). È la scoperta della 38ª, ed è il
     motivo per cui il progetto sta al 36% e non al 49%. 💡 È il lavoro **meno
     insidioso** — niente `name()` da accordare, niente participi, niente reti
     — ma vuole una **catena di strumenti diversa**, perché non ha firma
     `lang()` e non passa da `applica.py`. Nessuno l'ha ancora scritta, e
     scriverla è mezza giornata prima di tradurre la prima riga.

   💡 **La domanda giusta è quale il giocatore legge di più, e la risposta si
   guarda, non si calcola.** Il progetto ce l'aveva già dalla 26ª — *la
   frequenza, non l'elenco* — ma per tre file di fila l'aveva applicata
   contando le firme. La 39ª l'ha applicata **aprendo il gioco**, e la risposta
   è cambiata al primo screenshot.

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
python -m pytest strumenti/tests -q        # atteso: 420 passed, 6 skipped
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
python scratchpad/nudi_en.py              # struttura 1044 | ancora da fare 473
python scratchpad/triage_nudi.py          # testo 271, sigla 87, dbg 93, spenta 22
python scratchpad/return_en.py            # 0 da fare, 2 decise, 35 toccate, 49 morf., 35 chiavi
python scratchpad/tabelle_en.py           # testo 7 tabelle / 73 voci: 6 fatte, 1 decisa, 0 da fare
python scratchpad/blocchi_en.py           # struttura 99 | ancora da fare 54
python scratchpad/else_jp.py              # else-di-jp: 6.984 righe in 13 file
python scratchpad/rete8_dizionario.py     # 3, tutti dichiarati falsi positivi
python scratchpad/misura-blocchi-spenti.py  # 4 sprecate | 5 vive altrove
python scratchpad/variabili_en.py         # 60 variabili | 4 trappole in 4 siti
python scratchpad/perimetro.py            # perimetro 57% | col fuori perimetro 42%
python scratchpad/cnv_str_en.py           # 49 chiamate | 24 con la chiave inglese
python scratchpad/lang-nel-ramo-jp.py     # 21 righe | 0 gia' tradotte
```

⭐ **`tabelle_en.py` è della 52ª, ed è il SESTO punto cieco.** Le tabelle di
stringhe inglesi nude — `AITextData(0, 1) = "Not Set", "Self", "Target", …` —
che `nudi_en` non vede perché non disegnano e non compongono: sono
un'assegnazione di **array**, e il testo arriva a schermo per **indice**, da una
riga che di letterali non ne ha nessuno. ⚠️ Il referto **classifica invece di
scartare** (testo / sigla / numerica / jp) e confronta sorgente e build per dire
quali sono già fatte, perché una tabella non ha firma né voce di dizionario e
non c'è nient'altro da guardare — per lo stesso motivo la tabella che **non si
tocca** (le dodici classi) non poteva finire in `rinviate.jsonl`, che indicizza
per firma: sta in `DECISE` dentro il referto.

⚠️ **Il quart'ultimo è della 40ª, ed è il QUARTO punto cieco.** `cnv_str` riscrive una
stringa **già composta** usando come chiave l'**inglese di monte**: la resa
italiana la spegne, e in un caso l'aveva già spenta il bestiario mesi fa (vedi
il punto 3 delle cinque cose). **Se le 17 salgono, qualcuno ne ha scritta una
nuova; se scendono, una è stata toppata.** ⚠️ E delle 17, **2 sono uscita**
(`chara_func.hsp`) e **15 sono input** (`module.hsp`, `help.hsp`): solo le prime
due riguardano quel che il giocatore legge.

⚠️ **I due ultimi sono della 38ª.** `variabili_en.py` è il **terzo punto cieco**
dopo `blocchi_en.py` e `else_jp.py`: le variabili che si portano dentro un
letterale inglese e finiscono dentro una `lang()`. **Se sale a 5, qualcuno ne ha
creata una nuova; se scende a 3, una è stata risolta.**
⚠️⚠️ **Corretto nella 47ª, e per nove sessioni ha guardato male**: prendeva solo
`nome = "testo"` e non vedeva `nome += "testo"`, cioè la forma con cui si compone
una frase inglese **a pezzi**. Il quarto sito è `command.hsp:7724`, dove `s` si
carica sei aggettivi di rango a `:7716`-`:7721`. Col `+=` sono arrivati anche i
nomi di file di `system.hsp`, che adesso `_ESTENSIONE` scarta per forma invece
che per nome. Da 66 e 3 a **60 e 4**. Vedi il punto 9 delle tredici cose.
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
| `proc.hsp` | **1.091** | 1.098 | **100%** ⭐⭐ **chiuso il 2026-08-14** — +97 nella 39ª (era 994), più 23 righe fuori da `lang()` ✅ toppate, e **7 rinviate**: una riga commentata, «Party Room», i due nomi di nave, `:11481` (`his2()`, ✅ toppata nella 36ª), `:11796` (dentro un blocco `/* ... */` spento) e `:24107` (`tc == cc` e l'inglese nomina due personaggi, ✅ toppata nella 39ª) |
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
`init.hsp` 6 su 133.

⭐⭐ **`chara_func.hsp`: 327 su 331, chiuso il 2026-08-14** — +243 nella 40ª (era
84), sei lotti in una sessione sola. Le **4 rinviate** sono `:2310` (dentro un
blocco `/* ... */` spento), `:3037` e `:4520` (✅ toppate), `:4369` (riga
commentata). Il file porta **6 toppe**.

⭐⭐ **`calculation.hsp`: 44 su 44, chiuso il 2026-08-14** — un lotto solo, **zero
rinviate**, ed è l'unico file del progetto chiuso senza lasciare niente indietro
al primo passaggio. ⚠️ **Ma «100%» qui vuol dire «tutte le firme `lang()`»**:
`:2352` porta 「Forgive me! Forgive me!」, 「P-P-Pika!」, 「You snail!」 dentro un
`if ( jp ) … else` **fuori da `lang()`** — la scoperta di `else_jp.py` della 34ª,
uscita in inglese a schermo durante quel collaudo. Non hanno firma, non entrano
in nessun conteggio, e vanno **per toppa**.

⚠️ **E il quadro d'insieme, misurato il 14/08 con `scratchpad/fuori_elenco.py`**:
dei **54** file con `lang()` ne hanno un dizionario **14**; i **40** restanti
valgono **12.620 stringhe mai estratte**. Non sono file dimenticati — sono la
Fase 4, che `SPEC.md` §6 definisce collettivamente («i restanti 63 file `.hsp`
minori»). Il numero serve a tenere le proporzioni: quello che resta è più grande
di quello che è stato fatto.

**412 test più 6 saltati**, prova d'identità **72/72 e 27.813**, **14.534
sostituzioni** applicate alla build — erano **14.239** alla chiusura della 39ª,
più le **251** dei sei lotti di `chara_func.hsp` e le **44** di
`calculation.hsp`. **`toppe.jsonl` è a 306** (+2
nella 40ª, tutt'e due per `:4520`: `chara_func.hsp:4491` e `:4520`), e
`chara_func.hsp` ne porta **6**, `proc.hsp` **28**. **`rinviate.jsonl` è a 19**
(`proc.hsp` 7, `db_creature.hsp` 4, `chara_func.hsp` 4, `action.hsp` 2,
`text.hsp` 2). Il compilatore non dice nulla, manifesto del sorgente **72/72**.
Perimetro `lang()` **50%**, totale vero **37%**.

💡 **Le sostituzioni crescono più delle rese anche stavolta**: 243 rese hanno
prodotto **251 siti**. Il caso più netto della 40ª è `chara_func.hsp:8317`, che
ha la stessa firma di `:3377` — la stessa riga, in due punti dello stesso file —
e `:6859`, che copre anche `:6865`, e `:6877`, che copre `:6883`.

💡 **Le sostituzioni crescono più delle rese anche stavolta**: 97 rese hanno
prodotto **111 siti**. Una firma esce in più punti, e il caso più netto della
39ª è `:20200`, che copre anche `:20886` — la stessa domanda «non c'è nessun
bersaglio in vista» posta da due rami diversi della necromanzia — e `:24783`,
che copre `:24798`. Nessuno dei due secondi siti compare nell'estrazione.

💡 **E le sostituzioni crescevano più delle rese anche nella 38ª**: 285 rese
hanno prodotto **300 siti**, e il caso più netto era `:16087`, che ne copre
**due** senza che il secondo compaia nell'estrazione.

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
