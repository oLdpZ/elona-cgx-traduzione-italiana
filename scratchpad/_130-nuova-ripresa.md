# Ripresa sessione

Aggiornato: 2026-09-03, fine della **centotrentesima** sessione (**le toppe
entrano in due reti, «Gauge» aveva tre rese, e il fronte che il conto diceva di
sessanta righe era di quattro**).

⚠️⚠️⚠️ **L'ESEGUIBILE IN GIOCO E' QUELLO DELLE 22:56 DEL 02/09**, ricompilato e
ricopiato dopo le quattro rese nude. Se la data e' quella, non c'e' niente da
rifare. ⓘ Si legge con `ls -l C:\Games\Elona\elonaplus2.31\cgx-test.exe`.

---

## ⚠️⚠️⚠️ LA COSA PIU' GROSSA DELLA 130a: UN CONTO DI COSE INTATTE NON E' UN CONTO DI LAVORO

La 129a lasciava scritto che il fronte della traduzione erano **60 righe nude di
classe `testo`**, «il lavoro vero». Misurate:

    righe nude di classe `testo`      60
      gia' decise nei documenti       38
      RESIDUO, da leggere             22
      di quelle, VIVE                  4

**Il fronte era il 7% del numero che lo annunciava.** Le 38 erano decisioni
prese e scritte — le sigle `Hp:`/`Lv.`/`Dv:`/`Pv:` della colonna da venti
caratteri, le chiavi di `config.txt`, il TSV dell'autopick, `helloworld.hsp` che
non sta nemmeno nella build.

⚠️⚠️ **E il progetto lo sapeva gia'.** `invariati.md` lo scrive dalla 127a:

> quei referti contano i letterali **intatti**, e una riga che deve restare
> intatta e' indistinguibile da una che nessuno ha guardato.

Sapere non basta. La nota stava nel documento delle **decisioni**; il numero
sbagliato stava nel documento che si legge in **apertura**.

⭐ **La cura non e' cambiare il contatore** — deve continuare a contare anche il
deciso, altrimenti una decisione sbagliata diventa invisibile. Si aggiunge un
**secondo numero**, il residuo, e si porta quello a zero:

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-residuo-delle-righe-nude.py

        righe nude di classe `testo`   :  56
          gia' nominate nei documenti  :  56
          RESIDUO, da leggere          :   0

⚠️ L'incrocio si fa sui **siti** (`file:riga`), non sulle parole. E un intervallo
scritto `:692`-`:699` l'incrocio lo trova due volte su otto: gli intervalli si
scrivono **esplosi**, o il residuo mente al ribasso. Successo oggi, corretto
oggi. Vedi `wiki/concepts/un-conto-di-cose-intatte-non-e-un-conto-di-lavoro.md`.

---

## LE QUATTRO RESE, E LA PAROLA ACCANTO CHE NON SI TOCCA

    init.hsp:537     "unknown user"           -> «utente sconosciuto»
    quest.hsp:782    "You harvest rating…"    -> «Voto del raccolto: … (…s)!»
    text.hsp:11912   "Performance Score: …"   -> «Punteggio dell'esibizione: …»
    text.hsp:12104   "[News] "                -> «[Notizie] »

⭐ **`[Notizie]` non era una scelta di parola: era gia' scritta altrove.** Il
diario intitola la sezione `" - Notizie - "` (`command.hsp:2854`), dice «Nessuna
notizia» quando e' vuota (`:2851`), e le testate sono italiane da sessioni
(«Scoperta», «Nuova forza», «Guarigione»). Quel prefisso era l'unico pezzo
inglese di un sistema tutto tradotto. ⓘ E «Esibizione» viene dal glossario
(`skill.hsp:357`, `Performer`), non dall'orecchio.

⚠️ La `s` di `(3s)` si e' **ricopiata**: `seedp` non e' il numero dei semi
(quelli sono `1 + (seedp - 120) / 150`) e il sorgente non dice che unita' sia.
Un'unita' opaca si ricopia; inventarla vuol dire scrivere un dato che il gioco
non ha.

### ⚠️⚠️⚠️ `init.hsp:536` torna `"user"` e NON si tocca

Non e' testo: e' **l'operando che due `sreplace` cercano**
(`item_func.hsp:967` e `:1073`) per mettere il nome del PNG personalizzato
dentro il nome di carte, statuette e parti di creatura. Renderla «utente»
spegnerebbe tutt'e due i siti **in silenzio**.

⭐ E' la famiglia della 128a — un ramo ucciso dalla traduzione — da un lato che
**nessuna rete guarda**: `_128-confronti-contro-un-nome-assegnato.py` cerca
`X == lang(J, E)`, e un `sreplace` non e' un confronto.

⚠️ **Misurato, e oggi i rami sono vivi**: nella build `db_creature.hsp:97539`
torna ancora `lang("user", "user")`. Moriranno il giorno in cui un lotto di
`db_creature.hsp` rendera' quel nome, e il rimedio e' quello di «Your Home»
(42a): si allarga il sito che cerca, non si tocca il nome.

ⓘ Due righe adiacenti nella stessa funzione con trattamenti opposti: e' la
distinzione fra sigla e parola sul confine piu' sottile che il progetto abbia
incontrato. Scritta in `invariati.md`, 130a.

---

## LE DUE RETI NUOVE SULLE TOPPE, E LA PREMESSA CHE ERA FALSA IN DUE PUNTI SU TRE

La 129a diceva che le **910 toppe con testo** non hanno nessuna rete che guardi
glossario, larghezze e maiuscole. Rimisurata prima di costruire:

- **`maiuscole` legge gia' la build**, quindi le toppe le vede per costruzione —
  ma di toppe con `cnven(` ce ne sono **sei**: non e' una rete assente, e' una
  rete quasi muta. Il numero che conta non e' «le vede», e' «quante ne ha
  giudicate»;
- **`larghezze` non puo' vederle in nessun caso**: scorre il dizionario e cerca
  `(file, riga)`, e una toppa **non ha il campo `riga`** — `toppe.jsonl` porta
  `file`, `cerca`, `sostituisci`, `motivo`, e basta;
- **il glossario non lo legge nessuno**, ne' sulle toppe ne' sul dizionario.

⚠️⚠️ **E il primo tentativo di misurare la seconda rispondeva 0**, perche' il
ciclo saltava tutte e 1.172 le voci sul campo che non esiste. Lo zero era la
spia rotta, non il dato — la lezione della 109a, incassata il giorno dopo averla
riscritta.

### `_130-larghezze-sulla-build.py` — il metro sull'ESITO

Gira la macchina di `strumenti/larghezze.py` (`menu_per_riga`, `larghezze`,
`_siti`, `budget`, `reso`) sull'**albero della build**, dove dizionario e toppe
sono gia' dentro. Un metro solo per tutt'e due le strade, e **nessun numero di
riga da far combaciare** fra due alberi che non ne hanno lo stesso numero.

    voci di menu misurate nella build : 714
      di cui scritte da una toppa     :  86   <- il fronte che nessuna rete leggeva
    voci fuori misura                 :   0

⭐ **Ha trovato due cose al primo giro, e una era della mia misura.**
`larghezze.reso` sbaglia quando il valore dinamico sta **in testa**: la sua
espressione cerca `" + qualcosa + "`, cioe' un valore *fra due letterali*, e
`mapname(i) + " " + cnvrank(...)` risultava lungo **92 caratteri** — il codice,
non la frase. Non si era mai visto perche' nella rete del sorgente il testo
arriva dal campo `it` del dizionario, che e' sempre un letterale: e' un limite
che **solo questa strada poteva incontrare**.

### `_130-glossario-nelle-toppe.py` — e la maiuscola che lo rende un filtro

La prima stesura bocciava **87 voci su 163**. Piu' della meta': non un filtro,
l'elenco completo con un passaggio in piu'. La causa stava tutta nel conto dei
termini che bocciavano — `will` **trentacinque volte**, ed era il futuro
inglese; poi `change`, `attack`, `bow` («**Bow** down before me»), `body` («wash
your **body**»).

⭐ **La discriminante non e' la lunghezza del testo, e' la MAIUSCOLA.** Un
termine di glossario e' un termine d'interfaccia; quando l'inglese lo scrive
maiuscolo **in mezzo a una frase** lo sta usando come termine, non come parola.

    restrizione                     contenevano  giudicate  divergenze
    nessuna                                 163        163          87
    solo inglese <= 40 caratteri             68         68          15
    solo termine maiuscolo                  163         46           6   <- questa
    maiuscolo + inglese <= 40                68         33           5

⚠️ Si sceglie la terza e non la quarta **anche se boccia una voce di piu'**: la
quarta lascia fuori meta' delle toppe **prima di guardarle**, per la lunghezza,
che col glossario non c'entra niente. Un filtro si sceglie sul rapporto, non sul
totale.

⚠️⚠️ **La taratura vale per le TOPPE, e sul dizionario NO.** `--dizionario` da'
**1.239 giudicate, 458 divergenze**, il 37%: le toppe sono etichette, le rese
sono prosa, e in prosa `Darkness` -> «buio» e' giusto anche se il glossario dice
«oscurita'». Il numero e' stampato perche' nessuno l'aveva mai preso, **non**
perche' sia un cancello.

---

## ⭐⭐ «GAUGE» AVEVA TRE RESE, E IL GLOSSARIO NE AVEVA DECISA UNA NELLA 5a

La rete ha segnalato una toppa che scrive «Forza liberata» dove `glossario.md`
dice **Barra**. La divergenza non era della toppa: era del progetto, su sei
siti.

    barra    ~12 siti   action, buff, chat, command, config, custom_ai, custom_tweaks
    forza      3 siti   skill.hsp:1528, custom_tweaks.hsp:1255 e :1260, piu' due toppe
    carica     2 siti   command.hsp:1361 (dizionario) e :191 (toppa)

⚠️⚠️⚠️ **La prova che chiude la questione sta su due righe adiacenti.** Il nome
di una mossa speciale e la sua descrizione si leggono **sulla stessa riga
dell'elenco**:

    skill.hsp:1528          «<Serba/libera la forza>»
    skill.hsp:1529          «Attiva o disattiva la barra»

E lo stesso pannello d'aiuto diceva «la barra», «Forza liberata» e «la barra»
**dentro un paragrafo solo**.

⚠️ **Il giapponese e' `【力の解放】`, e «Forza» era la resa piu' FEDELE**:
`<Gauge Release>` e' gia' una scelta del localizzatore inglese, che ha
battezzato la mossa col nome dello strumento invece che della risorsa. Si e'
scelto lo stesso l'inglese, e non per fedelta' ma per **riconoscibilita'**: la
5a aveva deciso `Gauge` -> «Barra» **misurando** — 60 occorrenze su 75 sono le
etichette di costo `[Barra 50%]` — e una mossa che si chiama «Forza» e costa
«Barra» chiede al giocatore due nomi per una cosa sola. «Carica» non era una
resa: era una deroga.

    <Gauge Release>       -> <Libera la barra>
    <Gauge Save/Release>  -> <Serba/libera la barra>
    PGauge: / Gauge:      -> Barra:

### Le altre cinque divergenze sono LETTE e DICHIARATE

In `GIUDICATI`, come fa `strumenti/maiuscole.py`: **il referto non chiede zero
divergenze, chiede che quell'elenco non si allunghi da solo.** Due meritavano il
glossario, e ci sono scritte:

- **«Pagnotte mangiate:» resta**, ed e' un'eccezione dichiarata: quella riga sta
  in una colonna di contabili al plurale — «Mutandine mangiate», «Umani
  mangiati», «Oggetti rubati», «Sorelline» — e «Pane mangiato» spezzerebbe il
  verso della colonna per far combaciare un termine che li' nessuno puo'
  confondere. Il **nome dell'oggetto** resta «pane» dappertutto;
- **«Nome Livello Effetto» non e' una divergenza**: il giapponese dice
  `特徴の効果`, «l'effetto del tratto», e la colonna di «Talenti e tratti»
  mostra proprio l'effetto. `Detail` era la scelta larga dell'inglese.

⭐ **Il term base tiene l'autorita':** le due eccezioni sono scritte in
`glossario.md`, non lasciate nei siti. E' quel che il glossario dice di se' nella
prima riga.

---

## LA RESA CHE LA RETE DELLE LARGHEZZE HA TROVATO

`command.hsp:7770`, «Evoca come amichevole. (350 pp)»: **31 caratteri** in un
riquadro da 280px, cioe' un tetto di 30, e il riquadro **taglia**. L'inglese ci
stava — «Summon as friendly. (350 pp)» sono 28. Non un tetto ereditato da monte:
un difetto che ha aggiunto la traduzione.

⚠️⚠️ **E il `motivo` della toppa dichiarava la larghezza**: «ⓘ Il prompt e' largo
280 (:7774)». Chi l'ha scritta aveva il dato sotto gli occhi e non l'ha
convertito in caratteri, perche' niente lo faceva per lui. **Il numero era in
mano, la misura no.**

Cade il **punto** prima della parentesi, non la parola: «amichevole»,
«neutrale» e «ostile» restano — concorderebbero col personaggio evocato, di cui
non si conosce il sesso, e la guida di stile lo vieta.

---

## I COMANDI NUOVI

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-larghezze-sulla-build.py
    ... --elenco     tutte le voci misurate, col margine
    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-glossario-nelle-toppe.py
    ... --dizionario il numero mai preso sulle 26.327 rese (NON e' un cancello)
    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-residuo-delle-righe-nude.py
    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-prova-al-contrario-reti-toppe.py

⚠️ La prova al contrario prende i dati **veri** e sposta di un passo la cosa che
tiene chiuso il cancello: allunga una voce di menu, le toglie la `lang()`,
stringe il riquadro a testo fermo, guasta una resa buona, alza a maiuscolo un
termine minuscolo. **9 prove su 9 si accendono**, e stampano dove.

⭐ Una delle nove pretende che il cancello **NON** si accenda: e' la dinamica in
testa, il difetto di misura trovato oggi. Una prova al contrario che sa anche
dire «qui deve restare spento» e' l'unica che protegge da una correzione
esagerata.

---

## I VALORI DA ASPETTARSI IN APERTURA, DOPO LA 130a

    pytest                   **798 passed**, 6 skipped, invariato
    prova_identita           72/72 e 30.905, invariato
    applica                  30.766 sostituzioni, invariato
    perimetro.py             **26.327** fatte, 0 da fare, 100,0%
                             ⚠️ la 129a scriveva 26.326 «invariato» ed era gia'
                                stale: la sua stessa resa di `command.hsp:10710`
                                valeva +1, e per `perimetro` ha ereditato invece
                                di rilanciare. Verificato che la 130a non l'ha
                                mosso: le voci con `it` sono 26.320 prima e dopo
    toppe                    **1.176** (erano 1.172: +4), agganciate 1.176/1.176
    triage_nudi              testo **56** (erano 60), sigla 87, dbg 93, spenta 22
    _130-residuo-righe-nude  56 contate, 56 nominate, **RESIDUO 0**
    _126-nudi-nel-ramo-jp    **53 vive** (erano 57), 3 nel ramo jp
    _126-spente-da-una-costante  **39 vive davvero** (erano 43)
    _126-referti-toppe       participi 0, elisioni 0 su **914** toppe con testo
                             (erano 910)
    _130-larghezze-sulla-build   714 misurate, 86 da toppa, **0 fuori misura**
    _130-glossario-nelle-toppe   46 giudicate, 5 dichiarate, **0 NUOVE**
    _130-prova-al-contrario-reti-toppe   **9 su 9**
    _129-condizioni-dei-rinvii   MATURATE 0, ROTTE 0, SENZA CONDIZIONE 0 su 113
    _129-prova-al-contrario      8 famiglie su 8
    _128-confronti               di monte 3, aggiunti dalla traduzione 0
    _97-toppe-agganciate     1.176 su 1.176
    _97-quanto-resta         111 / 111 / **0**
    _125-non-tradotte        111 / 111 / **0 FUORI dalle rinviate**
    verifica --dizionario    111 non tradotte in 19 file, 0 da ritradurre
    larghezze                0 fuori misura, 412 + 304 voci nel riquadro
    maiuscole                143 siti, 6 appesi, 1 accumulato, 7 giudicati, **0 da guardare**
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

## Che cosa guardare adesso: le cose aperte

1. ⭐⭐⭐ **Il debito di collaudo, ed e' rimasto l'unico fronte grosso.**
   ~9.650 rese mai viste a schermo, e nessuno strumento che le conti. Oggi il
   perimetro `lang()` e' chiuso al 100%, le righe nude hanno residuo 0 e le
   111 non tradotte sono tutte rinviate decise: **da tradurre non resta niente
   che qualcuno abbia chiesto.** Quel che resta e' guardare.
   ⓘ E le quattro rese di oggi non sono state viste a schermo: `[Notizie]` si
   vede appena una notizia entra nel registro, «Punteggio dell'esibizione»
   consegnando una missione di intrattenimento.
2. ⭐⭐ **La rete che cerca l'operando di una SOSTITUZIONE.** `init.hsp:536` l'ha
   trovata un umano leggendo; `_128-confronti-contro-un-nome-assegnato.py` cerca
   `X == lang(J, E)` e non la vedrebbe mai. Il verbo cambia — `sreplace`,
   `instr`, `strmid` con un letterale — il difetto no: qualcuno cerca una
   stringa che qualcun altro ha tradotto. ⓘ Il caso noto e' **vivo oggi e muore
   da solo** appena `db_creature.hsp` verra' tradotto: e' un difetto con una
   data di nascita futura, e nessuno lo sta aspettando.
3. ⭐⭐ **Le reti sulle toppe: ne restano fuori due.** Adesso le toppe hanno
   participi, elisioni, doppia larghezza, **larghezze dei menu** e **glossario**.
   Non hanno ancora chi guardi le **maiuscole del testo** (non `cnven`, che e'
   un'altra cosa) ne' le **larghezze fuori dai menu** — riquadri, linguette,
   gronde girano tutte sul dizionario.
4. ⭐ **La coda nuda di una `lang()` gia' resa** (il caso `chat.hsp:17065` della
   127a): un referto che nessuno ha scritto. ⓘ Gemello: la resa che cita per
   nome un'etichetta che vive in una toppa.
5. 💡 **Il frammento inglese morto per flusso ha una casa, non una rete.** Il
   tipo `morta_per_flusso` copre le 14 voci dichiarate, ma nessuno **cerca**
   quella famiglia.
6. 💡 **La gemella viva di una firma rinviata.** Il difetto n. 1 della 129a
   l'ha trovato il referto per caso; un referto che lo cercasse di proposito
   guarderebbe tutte le 113 voci e non solo quelle marcate `riga_morta`.
