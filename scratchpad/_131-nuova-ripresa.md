# Ripresa sessione

Aggiornato: 2026-09-03, fine della **centotrentunesima** sessione (**quattro
schermate del giocatore, e sotto ognuna una spia rotta: 1.060 oggetti dicevano
«a borraccia filtrante», i tredici fiori vivevano dentro l'uscita di un
generatore, e `scene2.hsp` non l'ha mai aperto nessuno**).

⚠️⚠️⚠️ **L'ESEGUIBILE IN GIOCO E' QUELLO DELLE 02:00 DEL 03/09**, ricompilato e
ricopiato dopo la cura dell'articolo e il singolare del piede. Se la data e'
quella, non c'e' niente da rifare. ⓘ Si legge con
`ls -l C:\Games\Elona\elonaplus2.31\cgx-test.exe`.

---

## ⚠️⚠️⚠️ LA COSA PIU' GROSSA DELLA 131a: L'ARTICOLO ERA CALCOLATO, SALVATO, E BUTTATO UNA RIGA DOPO

Il giocatore manda una schermata «Raccogli»: **«a borraccia filtrante»**. Nome
italiano, articolo inglese. E `db_item.hsp` nella build ha la riga esatta:

    ioriginalnamearticolo(ITEM_ID_FILTRATION_BOTTLE) = "una "

Ce l'ha, ed e' corretta. **Non veniva mai usata.** Il blocco dell'articolo,
generato da `genera_toppe_nomi.py`, faceva cosi':

    if ( locvar_itemname_s8 == "" ) {
        locvar_itemname_s8 = ioriginalnamearticolo(...)      <- "una "
        if ( locvar_itemname_ignoto != "" ) {
            if ( locvar_itemname_s2 == "" ) {
                locvar_itemname_s8 = iknownnamearticolo(...) <- "", e SOVRASCRIVE

Sull'oggetto **non ancora identificato** l'articolo buono veniva sovrascritto da
quello del nome ignoto, che `db_item.hsp` assegna a **261** oggetti su 1.321.
Vuoto, si cadeva nel ripiego inglese `"a "`/`"an "`.

    1.060 oggetti su 1.321      ->  dopo la cura: 4, letti e dichiarati

⭐ **La cura non aggiunge un dato: rende vera una frase gia' scritta.**
`strumenti/estrai.py` lo dichiarava da sessioni —

> 847 rimandano al nome identificato (`= ioriginalnameref(...)`, **e allora
> articolo e plurale di quello vanno bene anche qui**)

— ed era esattamente cio' che il codice **non** faceva. Adesso c'e' una terza
guardia: si scavalca solo se c'e' con che scavalcare.

### ⚠️⚠️⚠️ E LA RETE C'ERA, E RISPONDEVA ZERO

`scratchpad/_83-banco-nome.py` stampa in coda, da sessioni:

    senza articolo (ripiegherebbero sull'inglese a/an): 0

Zero, mentre il gioco scriveva «a borraccia filtrante». Il ciclo parte da
`noti = d["iknownnameref"]`, cioe' dai soli 261 oggetti che hanno una **voce di
dizionario** per quell'array. **Gli altri 1.060 non entravano nell'insieme, e
chi non entra non puo' essere contato fuori.**

> Uno zero misurato sull'insieme sbagliato non e' un dato: e' una spia rotta.

E' la 109a e la 130a da un terzo lato, con un'aggravante: le altre due volte il
ciclo saltava le voci su un campo mancante, **qui l'insieme di partenza era
legittimo** — solo, non era quello della domanda. Percio' le reti nuove non
partono dal dizionario: leggono `db_item.hsp` nella **build** e simulano il
blocco riga per riga, prendendo dalla build **anche il fatto che la guardia ci
sia**. Se un giorno sparisse, il numero risale invece di restare zero.

---

## ⭐⭐ UNA COINCIDENZA CHE REGGEVA SUL 97% NON E' UNA REGOLA

`genera_toppe_casuali.py` dichiarava nella propria intestazione che l'articolo
dei **213 nomi casuali** non era un problema, «perche' la testa del nome vero e'
la stessa parola di famiglia». Vero su 208. **Falso su cinque**, e la rete nuova
li ha nominati al primo giro:

    ITEM_ID_ACIDPROOF_LIQUID   «liquido antiacido» (un )  ma ignoto e' «pozione …»
    ITEM_ID_FIREPROOF_LIQUID   idem
    ITEM_ID_POISON             idem
    ITEM_ID_SLEEPING_DRUG      idem
    ITEM_ID_NECK_GUARD         «gorgiera» (una )         ma ignoto e' «amuleto …»

Quei cinque non sono pozioni ne' amuleti: sono un liquido, un veleno, un
farmaco, una gorgiera. ⚠️⚠️ **Con la sola guardia si sarebbe letto «un pozione
torbida» e «una amuleto d'ambra»: cinque difetti nuovi introdotti da una cura.**

Adesso l'articolo del nome casuale si **emette**, per tutti e 213 e non per i
cinque, derivandolo dalla parola di famiglia. ⓘ E la parola si legge dal
dizionario per firma: se «pozione» diventasse «ampolla», l'articolo la
seguirebbe da solo. Nel file resta solo il **genere**, che e' l'unica cosa che
non si deduce.

---

## ⭐ IL RIPIEGO NON ERA SOLO DEI NON IDENTIFICATI

Allargata la stessa domanda a **tutti** gli oggetti, sono usciti **dodici** che
ripiegavano **sempre**, anche da identificati: quelli il cui nome `db_item.hsp`
non scrive affatto (`ioriginalnameref` e' la stringa vuota in tutt'e due i rami)
e che `item_func.hsp` compone con un `if` sull'identita' — «caffe'»,
«caffelatte», «te' nero», i quattro `potioman`.

    due gia' curati      FISH, FISH_JUNK (fishdatanarticolo, un array suo)
    sei curati oggi      testa di genere COSTANTE -> una riga in db_item.hsp
    quattro DICHIARATI   testa di genere VARIABILE -> invariati.md

I quattro sono `JUICE` (la testa e' il frutto), `NECRO_PARTS` (la parte del
corpo), `PRODUCED_BOOK` (il titolo generato) ed `EVITEM` (un nome fra `<>`, che
prima dell'articolo vuole la decisione sulla marca). ⭐ **E l'elenco non e' una
nota: e' un dato che la rete legge**, e fallisce in tutt'e due i versi —
`SCONOSCIUTO` se ne compare un quinto, `STANTIO` se uno di questi smette di
ripiegare e la riga in `invariati.md` diventa una bugia.

---

## ⚠️⚠️⚠️ UN DATO CHE VIVE DENTRO L'USCITA DI UN GENERATORE E' UN DATO CHE IL GENERATORE CANCELLA

Rigenerando le toppe, `pytest` ha dato due rossi in `test_maiuscole.py`: un sito
«giudicato» si era spostato di **dodici righe in su**. Ma la guardia nuova
aggiunge righe, non le toglie.

Erano spariti **i tredici articoli dei fiori selvatici** — «una rosa», «una
margherita», «un'ortensia» — scritti nella 96a. Stavano **a mano dentro una
toppa marcata `generata: nomi`**, e `genera_toppe_nomi.py` sostituisce le
proprie toppe a ogni giro. La sua stessa intestazione dice che rilanciarlo e'
«il primo comando da rilanciare» al riallineamento a una versione CGX nuova:
era una mina, armata dalla 96a e innescata oggi.

Adesso i fiori stanno nel generatore (`articolo_del_fiore`), accanto al pesce
che ha la stessa forma. ⭐ **E a dirlo e' stato l'unico controllo che poteva:**
il test dei giudicati di `maiuscole`, che sorveglia una coordinata nella build
per una ragione che coi fiori non c'entra niente. Coordinata aggiornata da
`:2366` a `:2368`; il commento accanto raccontava gia' due spostamenti, adesso
ne racconta tre, **e uno dei tre ha trovato un guasto che non era suo**.

---

## ⚠️⚠️ «1 OGGETTI»: UN MOTIVO DI QUINDICI RIGHE CHE NON NOMINA IL NUMERO

    command.hsp:14175   s = "" + listmax + " items"   -> " oggetti"
    blend.hsp:1390      idem

Con un oggetto solo si leggeva **«1 oggetti»**. ⚠️ L'inglese sbagliava allo
stesso modo («1 items»), quindi la traduzione il difetto **l'ha ricopiato, non
aggiunto**: leggere il sorgente non bastava, ci voleva la schermata.

⚠️⚠️ E il `motivo` di quella toppa e' lungo quindici righe — misura i pixel del
piede, l'allineamento a destra di `display_note`, la regola della 46a, il quinto
punto cieco della 49a — e **non nomina il numero**. Si puo' guardare a lungo la
larghezza di una riga senza mai guardarne la grammatica.

Adesso il numero sceglie fra le due stringhe; lo zero resta col plurale.
ⓘ «oggetto» e «oggetti» hanno le stesse sette lettere: la misura del piede
scritta in quel motivo vale ancora.

---

## I COMANDI NUOVI

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_131-articolo-sul-nome-ignoto.py
    ... --elenco     ogni oggetto che ripiega, con nome e famiglia
    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_131-quanti-articoli-inglesi.py
    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_131-prova-al-contrario-articolo.py

⚠️ **13 prove su 13**, e una pretende che il cancello resti **SPENTO**: rimessa
la guardia dov'era, non deve accendersi nulla. ⓘ Due prove sono nate spente
perche' il mio `replace` cercava un `\n` dove la build ha CRLF — la prova non
guastava niente e sembrava che la rete non vedesse il caso. **Un guasto che non
guasta e' un successo finto**, ed e' proprio la cosa contro cui serve quel file.

---

## I VALORI DA ASPETTARSI IN APERTURA, DOPO LA 131a

    pytest                   **798 passed**, 6 skipped, invariato
    prova_identita           72/72 e 30.905, invariato
    applica                  30.766 sostituzioni, invariato
    perimetro.py             26.327 fatte, 0 da fare, 100,0%, invariato
    toppe                    **1.182** (erano 1.176: +6, i nomi composti a mano),
                             agganciate 1.182/1.182
    triage_nudi              testo 56, sigla 87, dbg 93, spenta 22, invariato
    _130-residuo-righe-nude  56 contate, 56 nominate, RESIDUO 0
    _126-nudi-nel-ramo-jp    53 vive, invariato
    _126-spente-da-una-costante  39 vive davvero, invariato
    _126-referti-toppe       participi 0, elisioni 0 su **1.133** toppe con testo
                             ⚠️ erano 914: +219 perche' le 213 toppe dei nomi
                                casuali adesso portano anche le due righe
                                dell'articolo, e quelle sono testo
    _130-larghezze-sulla-build   714 misurate, 86 da toppa, 0 fuori misura
    _130-glossario-nelle-toppe   46 giudicate, 5 dichiarate, 0 NUOVE
    _130-prova-al-contrario-reti-toppe   9 su 9
    **_131-articolo-sul-nome-ignoto**  guardia c'e', **ripiegano 4**, divergenze 0
    **_131-quanti-articoli-inglesi**   SCONOSCIUTI **0**, orfani 0, dichiarati 4
    **_131-prova-al-contrario-articolo**  **13 su 13**
    _129-condizioni-dei-rinvii   MATURATE 0, ROTTE 0, SENZA CONDIZIONE 0 su 113
    _129-prova-al-contrario      8 famiglie su 8
    _128-confronti               di monte 3, aggiunti dalla traduzione 0
    _97-toppe-agganciate     1.182 su 1.182
    _97-quanto-resta         111 / 111 / 0
    _125-non-tradotte        111 / 111 / 0 FUORI dalle rinviate
    verifica --dizionario    111 non tradotte, 0 da ritradurre
    larghezze                0 fuori misura, 412 + 304 voci nel riquadro
    maiuscole                143 siti, 6 appesi, 1 accumulato, 7 giudicati, 0 da guardare
    riquadri                 0 su 38 e 0 su 71
    linguette                0 e 0
    gemelle                  9
    creature                 0 firme in due classi, 0 nomi senza razza
    diario                   0 su 205
    gronde                   0 su 5
    bilingui                 0
    menu_dialogo             0 rese peggiorate (rotte anche in inglese: 10)
    dati_sorgente            7 / 7 intatti, gioco difforme su 0
    referti                  participi 9, elisioni 0 (il dizionario, invariato)

⚠️ **Nessuno di questi numeri si eredita da qui**: si rilanciano. E in chiusura
si rilancia **tutto cio' che produce un numero atteso**, dopo l'ultima modifica
ai documenti — `_130-residuo-delle-righe-nude.py` legge `invariati.md`, quindi
cambiare quel documento **cambia un numero**.

---

## ⚠️⚠️⚠️ IL FRONTE NUOVO E GROSSO: `scene2.hsp`, UN FILE INTERO MAI APERTO

Tre delle quattro schermate del giocatore erano **inglese puro**: il prologo
della Foresta di Vindale, il naufragio della Queen Sedona, e il dialogo di
`<Saimore> The Crown Prince of Zanan`. Vengono tutte dallo stesso posto.

    scene2.hsp:12     «A month of rain plagued the frontier lands of Karune…»
    scene2.hsp:31     «The dawn will soon arrive…»
    scene2.hsp:47     {actor_1}  "<Saimore> The Crown Prince of Zanan,54"

`help.hsp:819` fa `noteload lang("scene1.hsp", "scene2.hsp")`: **sono due file
diversi, uno per lingua** — `scene1.hsp` e' il giapponese, `scene2.hsp`
l'inglese. `invariati.md` tiene il **nome del file** fra gli invarianti, e ha
ragione; ma il **contenuto** non e' mai stato toccato.

    scene2.hsp    5.731 righe, 147 blocchi {txt}, ~1.675 righe di prosa
    scene1.hsp    5.860 righe, 152 blocchi {txt}   <- il giapponese c'e', quasi allineato

⚠️ **Era una cosa aperta fino alla ~111a** («`scene2.hsp` non e' nel
dizionario»), poi **e' uscita dall'elenco della ripresa senza essere chiusa**. E
la 130a scriveva «da tradurre non resta niente che qualcuno abbia chiesto»: e'
vero per il perimetro `lang()`, e queste 1.675 righe stanno fuori da quel
perimetro. **Un fronte che esce da un elenco non e' un fronte chiuso.**

⚠️ `main.hsp:1`-`:2` fanno `#pack "scene1.hsp"` / `#pack "scene2.hsp"`: quel file
**sta dentro l'eseguibile**, quindi tradurlo richiede di ricompilare — non e'
come i dati di `data\`.

ⓘ Due fili che il progetto ha gia' e che chi lo aprira' deve sapere:
`<Minea> The Puppeteer` (`scene2.hsp:2581`) e' la **sorella di Nein** e non e'
sparita in una Nefia — sta scritto in `_91-rese-nein.py`, unico posto dove i due
fili si toccano; e «Heretical Forest» -> «Foresta Eretica» e' gia' in
dizionario.

---

## Che cosa guardare adesso: le cose aperte

1. ⭐⭐⭐ **`scene2.hsp`: ~1.675 righe di prosa, e va aperto come una fase con un
   piano suo.** E' il fronte piu' grosso che il progetto abbia oggi, ed e' il
   solo che il giocatore abbia chiesto guardando lo schermo.
2. ⭐⭐⭐ **Il debito di collaudo.** ~9.650 rese mai viste a schermo, e nessuno
   strumento che le conti. ⓘ **La 131a e' la prova di quanto pesa**: quattro
   schermate mandate da un umano hanno trovato quattro difetti che tutta la
   catena verde non vedeva — e uno era una rete che rispondeva zero.
3. ⭐⭐ **Le quattro teste variabili senza articolo** (`JUICE`, `NECRO_PARTS`,
   `PRODUCED_BOOK`, `EVITEM`). Vanno curate dove il nome si compone, non dove il
   tipo si dichiara. ⓘ `NECRO_PARTS` dipende dalle nove `lang()` nel ramo `& jp`
   della 129a: e' un difetto con una data di nascita futura.
4. ⭐⭐ **Chi altro vive dentro l'uscita di un generatore?** I fiori ci sono
   stati dalla 96a alla 131a. La domanda non e' «i fiori», e' **quante altre
   toppe `generata:` sono state ritoccate a mano**: un referto che confronti
   `toppe.jsonl` con quel che i generatori producono oggi non esiste, e sarebbe
   corto.
5. ⭐⭐ **La rete che cerca l'operando di una SOSTITUZIONE** (`sreplace`,
   `instr`, `strmid` con un letterale): `init.hsp:536` l'ha trovata un umano
   leggendo. Invariata dalla 130a.
6. ⭐⭐ **Le reti sulle toppe: ne restano fuori due** — le maiuscole del testo e
   le larghezze fuori dai menu. Invariata dalla 130a.
7. ⭐ **La coda nuda di una `lang()` gia' resa** (`chat.hsp:17065`, 127a): un
   referto che nessuno ha scritto.
8. 💡 **Il frammento inglese morto per flusso ha una casa, non una rete.**
9. 💡 **La gemella viva di una firma rinviata.**
