# SPEC — Elona+ Custom-GX, Traduzione Italiana

Design approvato il 2026-08-06. Questo documento è vincolante: le decisioni qui
dentro si cambiano modificando questo file, non improvvisando in sessione.

Stato: **design approvato; il cancello della Fase 0 è passato per intero.**

Fatto: la catena `estrai → verifica → reimporta → applica` esiste, è sotto test
(122 test verdi) ed è stata provata end-to-end sul sorgente vero, con round-trip
CP932 e CRLF verificati e il manifesto di `sorgente/` intatto. **Il sorgente non
modificato ricompila, l'eseguibile prodotto si avvia e carica un salvataggio
esistente** (§6, prova 1), e la compilazione è automatica: `compila.py`, nessuna
GUI.

Da fare:

1. `installa.py`;
2. vedere le ~50 stringhe tradotte a schermo in gioco, con l'accentata resa
   `perche'` (§6, prova 2);
3. individuare dove risiedono i nomi degli oggetti (§2, punto aperto).

---

## 1. Scopo

Tradurre in italiano il roguelike **Elona+ Custom-GX**, sorgente pinnato al tag
`2.31.2.0`, con il gioco di riferimento installato in
`C:\Games\Elona\elonaplus2.31\`.

Destinazione: uso personale, ma il progetto è strutturato fin dall'inizio come
pubblicabile (git, dizionario separabile, licenza da verificare prima di
pubblicare). La pubblicazione non è un obiettivo di questa fase.

Progetto gemello e modello di riferimento: [[Elin - Traduzione Italiana]], che
condivide universo, lessico e metodo di lavoro.

---

## 2. Contesto tecnico

Fatti verificati il 2026-08-06, non stime.

**Il gioco.** Elona+ Custom-GX è una variante di Elona+ mantenuta da
[JianmengYu](https://github.com/JianmengYu/ElonaPlusCustom-GX) (l'originale di
Ruin0x11 è fermo alla 2.15R). Il gioco installato è **2.31.2.0** (24/05/2026),
basato su Elona+ 2.31.

**Il sorgente è pinnato al tag `2.31.2.0`** (commit `a9135a6`, 15/05/2026), non
alla testa del branch `work`: un branch che si muove invaliderebbe in silenzio il
manifesto e ogni conteggio di questo documento. Vedi la decisione 16.

Due fatti misurati che il pin porta con sé, e che non vanno confusi con errori:

- il tag `2.31.2.0` dichiara `VARIANT_TITLE "Elona+ Custom-GX 2.31.1.0"`, e
  l'eseguibile che se ne ricava si intitola così. Nessun commit della storia
  pubblica dichiara `2.31.2.0`: la costante non è stata aggiornata al rilascio,
  quindi **il binario installato non è riproducibile byte per byte da nessun ref
  pubblico**. Non tocca la traduzione, tocca solo il numero mostrato nel titolo;
- la testa di `work` è già alla 2.32.1.2, non rilasciata. Resta la base naturale
  per un futuro riallineamento, non per questa fase.

**Dove sta il testo.**

| Collocazione | Volume | Note |
|---|---|---|
| Sorgente HSP (`2.05-custom-gx/*.hsp`, 72 file) | 26.588 occorrenze di `lang()`, di cui **26.206 traducibili** | Il grosso del gioco |
| File esterni in `data/` | ~250 KB | `book.txt` 115 KB, `talk.txt` 86 KB, `exhelp.txt` 17 KB, `board.txt` 15 KB |

Le 382 occorrenze non traducibili hanno l'argomento inglese **vuoto di proposito**:
sono particelle giapponesi che in inglese non esistono, come `lang("層", "")`.

Delle 26.206 traducibili, **22.682 sono statiche e 3.524 dinamiche** (contengono
concatenazioni). Il 13,4% di stringhe dinamiche è la quota che richiede attenzione
grammaticale — vedi §5.

**Il lavoro effettivo è però inferiore: 22.030 stringhe uniche.** Il 15,9% delle
occorrenze sono duplicati esatti — stessa coppia giapponese/inglese ripetuta più
volte nello stesso file — e il dizionario è indicizzato per firma, quindi si
traducono una volta sola e la traduzione si applica a tutte le occorrenze. Il
campo `occorrenza` resta a fini diagnostici, non moltiplica il lavoro.

Distribuzione sui file principali:

| File | grezze | traducibili | statiche | dinamiche |
|---|---|---|---|---|
| `db_creature.hsp` | 5.718 | 5.717 | 5.494 | 223 |
| `chat.hsp` | 4.772 | 4.762 | 4.277 | 485 |
| `db_card.hsp` | 2.326 | 2.308 | 2.308 | 0 |
| `text.hsp` | 2.134 | 2.127 | 1.896 | 231 |
| `command.hsp` | 1.560 | 1.481 | 1.248 | 233 |
| `action.hsp` | 1.502 | 1.502 | 1.129 | 373 |
| `proc.hsp` | 1.332 | 1.327 | 662 | 665 |
| `skill.hsp` | 913 | 894 | 894 | 0 |
| `trait.hsp` | 406 | 406 | 386 | 20 |

Conteggi ottenuti eseguendo l'algoritmo di estrazione sul sorgente reale, non
stimati. **Rimisurati il 2026-08-06 sul tag `2.31.2.0`** dopo il pin: i numeri
precedenti venivano dalla testa di `work`, che è un albero diverso. Prima ancora
erano stati rimisurati dopo la revisione finale della Fase 0, che
ha corretto due difetti del parser: la cecità all'escape `\"` (11 `lang()`
scartate e 295 voci con l'inglese mutilato) e la ricerca del `+` anche dentro i
letterali, che classificava dinamiche 163 stringhe statiche il cui testo contiene
un `+` — `"Enchantment Bonus + 4"`, `"RES+ magic"`. Prima della correzione i
totali erano 26.423 traducibili, 394 non traducibili e 22.727/3.696 fra statiche
e dinamiche.

**Forma delle stringhe.** Il sorgente usa ovunque la macro `lang(giapponese, inglese)`:

```hsp
#define global txt_invfull txt lang("バックパックが一杯だ。", "Your inventory is full.")
#define global txt_guard txt lang(name(tc) + "は" + name(...) + "をかばった！", name(tc) + " guarded " + name(...) + ".")
```

Estrazione e reinserimento sono quindi **meccanici e scriptabili**. È la
premessa che rende il progetto fattibile.

**Encoding.** Il repo salva i `.hsp` in UTF-8 e li estrae in CP932 tramite
`.gitattributes` (`working-tree-encoding=CP932`). Il compilatore HSP lavora in
CP932.

**Trappola: `git status` nel clone del sorgente è permanentemente sporco.**
Su un clone appena fatto e mai toccato, `git status` segnala **1198 file
modificati**, tra cui tre `.hsp` che dobbiamo tradurre: `ai.hsp`, `command.hsp`,
`main.hsp`. Non è una scrittura nostra. È l'ambiguità storica fra Shift-JIS e
Unicode sul byte `0x8160`: git lo *scrive* partendo da `～` (U+FF5E, tilde a
larghezza intera) e lo *rilegge* come `〜` (U+301C, wave dash). La conversione di
iconv è asimmetrica, quindi ogni file che contiene quel byte risulta modificato
appena git è costretto a rileggerlo.

Due conseguenze operative:

1. **`git status` non è un controllo d'integrità utilizzabile** sul clone del
   sorgente. Per verificare che nessuno strumento abbia scritto in `sorgente/`
   serve un manifesto di hash preso al momento del clone.
2. **Non si committa mai dentro il clone del sorgente.** Un commit lì
   riscriverebbe 1198 blob con caratteri diversi da quelli di upstream.

Il round-trip di **Python** è invece **byte-esatto**: verificato su tutti e 72 i
file `.hsp`, `bytes → decode("cp932") → encode("cp932")` restituisce byte
identici. Gli strumenti del progetto sono quindi al sicuro; il problema è
circoscritto a git.

**Punto chiuso il 2026-08-07.** Era: `db_item.hsp` (4,6 MB) contiene **zero**
`lang()`, i nomi degli oggetti passano da `ioriginalnameref` e risiedono altrove.

Non risiedono altrove: **risiedono lì**, fuori da `lang()`. La forma è un ramo
sulla lingua invece che una chiamata:

```
if ( jp ) {
    ioriginalnameref(ITEM_ID_BANANA) = "バナナ"
}
else {
    ioriginalnameref(ITEM_ID_BANANA) = "banana"
    ioriginalnameref2(ITEM_ID_BANANA) = ""
}
```

Sono **1.321 nomi**, e tutti e 1.321 corrispondono a **una sola forma canonica**
— verificato con una espressione regolare sola, zero eccezioni su 1.321. Non
erano irraggiungibili: erano fuori dal tipo di sito che `siti()` sa scandire.

`ndata.csv` / `ndata-e.csv` restano quello che dicevamo: liste di parole per i
nomi casuali, non il database.

**298 dei 1.321** si compongono come `ioriginalnameref2 + " of " + ioriginalnameref`
(`init.hsp:189`) — `deed of camp`, `scroll of harvest` — con un `" of "` inglese
cablato **fuori da `lang()`**, come il `"the "` di `init.hsp:1718`.

La conseguenza sul dimensionamento della Fase 2 e la decisione presa
(«un secondo tipo di sito nella catena») stanno in `contratto-nomi.md`.

---

## 3. Architettura

### 3.1 Il sorgente upstream non viene mai modificato

La traduzione **non** è un fork del sorgente CGX. È un **dizionario esterno**
applicato a un clone pulito solo al momento della build:

```
clone upstream (intatto)  +  dizionario/  --applica.py-->  albero di build  --HSP-->  elonapluscgx-it.exe
```

Motivazioni:

- **Riallineamento alle release.** A ogni nuova versione CGX si fa `git pull` sul
  clone e si riapplica il dizionario. Nessun conflitto di merge su 27.000 punti.
  `verifica.py` produce l'elenco delle stringhe cambiate o sparite a monte, che
  diventa la coda di ritraduzione.
- **Pubblicazione.** Si pubblicano dizionario e strumenti (pochi MB), non un fork
  di un progetto di terzi. Semplifica nettamente la questione licenza.
- **Coerenza col progetto gemello.** È lo stesso principio adottato su Elin: i
  file originali del gioco non vengono mai modificati.

### 3.2 Chiave di identificazione della stringa

`sha1(giapponese + "\x00" + inglese)` per le **statiche**;
`sha1(giapponese + "\x00" + inglese + "\x00" + espressione)` per le **dinamiche**,
dove `espressione` è l'argomento inglese grezzo con gli spazi normalizzati. Ambito
**per-file**: `dizionario/<nome>.hsp.jsonl` è indicizzato per firma e basta.

**Perché l'espressione entra solo nelle dinamiche.** Sui soli letterali,
`name(gdata(GDATA_RIDER)) + " glare"` e `cdatan(CDATAN_NAME, ttc) + " glare"`
condividono la chiave: 77 firme, 327 occorrenze. Tradurne una porterebbe
sull'altra **le variabili sbagliate**. Includere l'espressione rende la chiave più
fragile — rinominare una variabile a monte la rompe a testo invariato — ma i due
errori non costano uguale: una chiave debole scrive codice sbagliato in silenzio,
una chiave fragile manda la stringa in coda di ritraduzione, dove una persona la
guarda. È la stessa asimmetria delle decisioni 13 e 14.

Due correttivi riducono la fragilità a poco: la firma **normalizza gli spazi**,
quindi reindentare a monte non rompe nulla; e la voce conserva `jp` ed `en`,
quindi una firma orfana la cui coppia corrisponde a una sola firma nuova si
riaggancia meccanicamente. Per le statiche l'involucro **non** entra: cambiarle
sarebbe churn senza guadagno.

Costo misurato della decisione: **+235 stringhe da tradurre** (21.795 → 22.030),
e 324 occorrenze che erano irraggiungibili tornano traducibili.

Il giapponese è la componente stabile: se a monte cambia solo la formulazione
inglese, la firma si rompe **di proposito** e la stringa entra in coda di
revisione invece di restare tradotta su un testo che non esiste più.

**Il contatore `occorrenza` non entra nella chiave.** È diagnostico: dice quante
volte quella coppia si era già vista nel file, serve a ordinare il dizionario e a
orientarsi leggendo un lotto. I duplicati esatti **non si disambiguano**, perché
non c'è niente da disambiguare: sono la stessa stringa, si traducono una volta
sola e `applica.py` applica la traduzione a **tutte** le occorrenze. È quello che
dice il §2 e quello che fa il codice. Una versione precedente di questo paragrafo
affermava il contrario: era il documento a sbagliare, non il codice.

### 3.3 Dove finisce l'italiano

L'italiano **sostituisce il secondo argomento** di `lang()`, producendo un
eseguibile separato `elonapluscgx-it.exe`. La macro `lang()` non viene toccata e
i 26.588 siti di chiamata restano invariati. L'inglese resta disponibile nella
build ufficiale, che non viene sovrascritta.

### 3.4 Struttura della cartella

| percorso | contenuto |
|---|---|
| `SPEC.md` | questo documento |
| `README.md` | orientamento rapido e stato |
| `glossario.md` | termine EN → IT, vincolante |
| `guida-stile.md` | registro, marcatori da conservare, strategie per l'accordo di genere |
| `invariati.md` | stringhe che restano in inglese per scelta documentata |
| `decisioni.md` | scelte non ovvie e il perché |
| `avanzamento.md` | tradotte / totali per file e per fase |
| `RIPRESA-sessione.md` | punto di ripresa per la sessione successiva |
| `piani/` | piani di fase |
| `dizionario/` | **la traduzione — sorgente di verità** |
| `lavoro/` | lotti JSONL in lavorazione |
| `strumenti/` | script Python e relativi test |

Nel vault sta **solo testo**: documenti, dizionario, lotti, script. Tutto ciò che
è pesante e rigenerabile vive fuori, in `C:\Games\Elona\_traduzione\`:

| percorso | contenuto |
|---|---|
| `_traduzione\hsp34\` | SDK HSP 3.4 (~35 MB) |
| `_traduzione\sorgente\` | clone upstream CGX (~20 MB), mai modificato |
| `_traduzione\build\` | albero di build: clone + dizionario applicato |
| `_traduzione\dist\` | `elonapluscgx-it.exe` (~17 MB) |

Motivo: il vault contiene 16.500 note, viene indicizzato da Obsidian ed è o è
stato sincronizzato su Google Drive (`.tmp.driveupload`). Un clone git da 20 MB e
build da 17 MB rigenerate a ogni compilazione non hanno niente da fare lì dentro.
Il percorso della radice di lavoro è configurabile e vale come unico parametro
d'ambiente degli strumenti.

`glossario.md` nasce come copia del glossario Elin (451 righe, in larga parte
interfaccia e termini generici) e da lì diverge.

---

## 4. Encoding e accenti — risolto

**CP932 non contiene le vocali accentate italiane, e non segnala l'errore.**
Verificato empiricamente: ogni accentata viene sostituita silenziosamente con la
vocale nuda.

| carattere | byte in CP932 | risultato |
|---|---|---|
| `è` `é` | `65` | `e` |
| `à` | `61` | `a` |
| `ì` | `69` | `i` |
| `ò` | `6F` | `o` |
| `ù` | `75` | `u` |

Siccome git fa checkout in CP932, la perdita avverrebbe **automaticamente e senza
un solo avviso**: `perché` → `perche`, `città` → `citta`.

Le strade possibili erano tre:

| | Strada | Valutazione |
|---|---|---|
| **A** | Forma con apostrofo — `perche'`, `citta'`, `piu'` | Funziona con certezza, tutto ASCII. Estetica da localizzazione anni '90. |
| **B** | Byte CP1252 diretti (`0xE8` = `è`) nel sorgente | `0xE8` è un lead byte Shift-JIS valido: il compilatore HSP può inglobare il carattere successivo. Inaffidabile. |
| **C** | Stringhe tradotte in tabella esterna caricata a runtime | Risolve accenti e manutenzione insieme; Elona legge già `book.txt`/`talk.txt` esterni. Ma è modifica al codice del gioco, non solo traduzione. |

### Decisione: strada A, con degradazione in fase di build

Adottata la **forma con apostrofo**. Ma con una separazione che vale la pena
tenere ferma:

> **Il dizionario conserva l'italiano corretto, con gli accenti veri, in UTF-8.
> È `applica.py` a degradarli in forma con apostrofo mentre costruisce l'albero
> di build.**

`perché` resta scritto `perché` nel dizionario e diventa `perche'` solo nel
sorgente che va al compilatore. Conseguenze:

- se la strada C diventasse praticabile in futuro, si disattiva la degradazione e
  tutte le stringhe già tradotte acquistano gli accenti veri, **senza ritradurre
  nulla**;
- il dizionario resta italiano leggibile e riusabile fuori da questo gioco;
- la conversione avviene in un punto solo, testabile, invece che nella testa di
  chi traduce.

Regola di degradazione: `à è é ì ò ù` → `a' e' e' i' o' u'`, e le maiuscole
corrispondenti. Applicata solo alle vocali accentate italiane; qualsiasi altro
carattere non-ASCII che arrivi all'albero di build è un errore e va segnalato,
non convertito.

### Virgolette: `“ ”`, mai `"` e mai `«»`

Una traduzione **statica** non può contenere la virgoletta dritta `"`: finirebbe
dentro il letterale HSP e produrrebbe sorgente che non compila. Per le
**dinamiche** invece è legittima, perché lì fa parte dell'espressione.

Le caporali `«»`, che sarebbero lo standard tipografico italiano, **non esistono
in CP932**. Verificato: in Python sollevano `UnicodeEncodeError`, in .NET
diventano silenziosamente `≪≫`, i simboli matematici di molto-minore e
molto-maggiore.

Sopravvivono al round-trip CP932, verificate una per una: `“ ”` (U+201C/U+201D,
byte `0x8167`/`0x8168`), `‘ ’` e `「 」`. Adottate le doppie tipografiche `“ ”`,
che sono l'equivalente semantico diretto delle dritte.

`verifica.py` blocca le statiche con virgolette dritte e il messaggio d'errore
nomina l'alternativa: chi traduce migliaia di stringhe non deve indagare ogni
volta.

---

## 5. Rischio secondario: l'accordo grammaticale

`estrai.py` classifica ogni stringa in due binari:

- **Statiche** — nessuna interpolazione (`"Your inventory is full."`). Traduzione
  ordinaria.
- **Dinamiche** — contengono concatenazioni
  (`name(tc) + " guarded " + name(...)`, `"You successfully create " + itemname(ci,1) + "!"`).
  Estratte **insieme al codice circostante come contesto** e lavorate a parte.

L'inglese non ha accordo di genere e numero; l'italiano sì. Tradurre le dinamiche
alla cieca produce sgrammaticature su scala industriale. `guida-stile.md` fissa
le strategie standard:

- costruzioni impersonali e neutre rispetto al genere;
- nessun articolo determinativo davanti a un nome interpolato;
- riordino della frase per spostare il segnaposto dove l'accordo non serve.

Ciò che resta irrisolvibile va in `invariati.md`: inglese **per scelta
documentata**, non per dimenticanza.

---

## 6. Fasi

Ogni fase termina con un gioco installabile e più italiano della precedente.
Interrompere il progetto dopo una qualsiasi di esse lascia un risultato usabile.

| Fase | Contenuto | Occorrenze | **Da tradurre** | Risultato |
|---|---|---|---|---|
| **0** | Prototipo tecnico | ~50 | ~50 | Le due prove passano, posizione dei nomi oggetto individuata |
| **1** | UI e messaggi — `text` `command` `action` `proc` `skill` `trait` | 7.737 | **6.688** | Interfaccia e messaggistica in italiano |
| **2** | Nomi — `db_creature` `db_card`, più i nomi oggetto una volta localizzati | 8.025 | **5.942** + nomi oggetto | Gioco sostanzialmente italiano |
| **3** | Dialoghi — `chat.hsp` | 4.762 | **4.373** | Conversazioni con NPC in italiano |
| **4** | Coda — i restanti 63 file `.hsp` minori e i testi esterni | 5.682 | **5.027** + 250 KB | Copertura completa |

Somma verificata: 6.688 + 5.942 + 4.373 + 5.027 = **22.030** stringhe uniche da
tradurre, su 26.206 occorrenze. La colonna che conta per stimare il lavoro è
"da tradurre": i duplicati si traducono una volta sola. L'unicità è **per file**,
coerentemente con l'ambito della firma (§3.2): la stessa stringa presente in due
file diversi si traduce due volte.

Per confronto, le firme distinte sull'intero corpus sono **19.659**: un dizionario
a chiave globale risparmierebbe 2.371 traduzioni, il 10,8% del lavoro. Non è una
proposta — è il prezzo misurato dell'ambito per-file, da conoscere prima di
discuterlo. Sommare gruppi di file non dà mai il totale globale, e questa è la
distanza esatta fra le due letture.

La Fase 2 è quella che ci guadagna di più — 8.076 occorrenze per 5.976 stringhe,
il 26% in meno — perché i database di creature e carte ripetono molte formule
identiche.

I 250 KB di testi esterni (`book.txt`, `talk.txt`, `exhelp.txt`, `board.txt`)
sono aggiuntivi e non passano da `lang()`.

### Fase 0 — il cancello

Due prove. Nessuna traduzione in volume inizia prima che passino entrambe.

1. **L'exe si ricompila?** SDK HSP 3.4, build da sorgente **non modificato**;
   l'eseguibile prodotto deve avviarsi e caricare un salvataggio. Senza una build
   riproducibile dall'originale, il resto è teoria. **È il vero cancello del
   progetto.**

   **Passato per intero il 2026-08-06**, e automatizzato nella parte
   automatizzabile: `python -m strumenti.compila --cancello`. Il sorgente pinnato
   compila con `#No error detected.`, l'exe che ne esce (17.396.351 byte) si
   avvia dalla cartella del gioco **e carica un salvataggio esistente** — provato
   a mano, che è l'unico modo di provarlo. Il manifesto è stato verificato prima
   e dopo: 72 file su 72, nessuna scrittura nel sorgente.

   Da qui in avanti la base non è più teorica: è una build riproducibile
   dall'originale, indistinguibile dal gioco installato per quel che riguarda i
   dati salvati.
2. **Il ciclo gira end-to-end?** ~50 stringhe scelte apposta (metà statiche, metà
   dinamiche, e almeno cinque con vocali accentate) attraverso `estrai → traduci
   → applica → compila → installa → verifica → visto a schermo`. Verifica anche
   che la degradazione degli accenti della §4 funzioni: `perché` nel dizionario,
   `perche'` a schermo.

La questione accenti non è più una prova aperta: la §4 la chiude in favore della
forma con apostrofo. Resta da confermare che la degradazione sia corretta, cosa
che la prova 2 copre.

In parallelo: individuare dove risiedono i nomi degli oggetti (§2, punto aperto).

---

## 7. Controllo qualità

`verifica.py` **blocca** il reimport quando:

- le interpolazioni non combaciano con l'originale — stesso numero di `+` e
  stesse chiamate di funzione;
- una traduzione è identica all'inglese e non è in whitelist in `invariati.md`;
- il glossario è violato;
- una traduzione nel **dizionario** contiene una forma con apostrofo scritta a mano
  (`perche'`, `citta'`) invece dell'accento vero — la degradazione è compito di
  `applica.py`, non di chi traduce;
- nell'**albero di build** sopravvive un carattere non-ASCII che non sia
  giapponese preesistente: significa che la degradazione della §4 ha mancato
  qualcosa e CP932 lo cancellerebbe in silenzio;
- una stringa di interfaccia supera la larghezza massima del suo riquadro;
- l'eseguibile non compila.

`applica.py` inoltre **conta e stampa le voci di dizionario non consumate**, per
file: sono le firme che non esistono più nel sorgente. Al riallineamento a una
nuova versione CGX (§3.1) sono la coda di ritraduzione, e sparire in silenzio
significherebbe tornare in inglese a macchia di leopardo senza accorgersene. Il
modo completo `verifica --dizionario`, che le classificherebbe in *cambiate a
monte* e *sparite*, entra nel piano della Fase 1.

### Due limiti noti, oggi rifiutati a voce alta

Scoperti applicando un dizionario **identità** a tutti e 72 i file: sostituire
ogni stringa con se stessa deve riprodurre il sorgente byte per byte, e non lo
faceva. Entrambi corrompevano il sorgente in silenzio; entrambi ora sollevano un
errore che nomina file, riga e firma, invece di scrivere codice sbagliato.

1. **Statiche avvolte in una chiamata — 3.499 occorrenze** (2.726 in
   `db_creature.hsp`, 425 in file di Fase 1). `lang("…", cnvtalk("Urchinn!"))`
   non ha un `+` di primo livello, quindi è classificata statica; ma l'argomento
   inglese non è un letterale nudo. Sostituire l'intero span con `"Ricciooo!"`
   **farebbe sparire `cnvtalk` dal sorgente**. La correzione vera è sostituire il
   letterale *dentro* l'involucro, lasciando la chiamata al suo posto: è lavoro
   di Fase 1, e senza di essa la Fase 2 non può partire (`db_creature.hsp` è il
   file più colpito).
2. **Firme che collidono su espressioni diverse — 77 casi** (23 in file di
   Fase 1). La firma si calcola sui soli letterali, quindi due dinamiche con lo
   stesso giapponese e lo stesso testo inglese ma **espressioni diverse** —
   `name(gdata(GDATA_RIDER)) + " glare" …` e `cdatan(CDATAN_NAME, ttc) + " glare" …`
   — condividono la chiave. La traduzione scritta su una finirebbe nell'altra,
   portandoci le variabili sbagliate. La correzione vera è includere `en_grezzo`
   nella firma delle dinamiche, che è una modifica alla §3.2: da decidere in
   Fase 1, prima che il dizionario si riempia.

Dopo queste esclusioni il dizionario identità riproduce **tutti e 72 i file byte
per byte**, con 22.602 sostituzioni e 3.832 occorrenze rifiutate.


---

## 8. Strumenti

Contratti, non implementazione. Python, coerente con il progetto Elin.

| script | responsabilità |
|---|---|
| `estrai.py` | dal clone upstream produce un lotto JSONL per un intervallo di file/righe; classifica statica/dinamica; allega il contesto di codice alle dinamiche |
| `applica.py` | inietta il dizionario su un clone pulito producendo l'albero di build; non scrive mai dentro `sorgente/` |
| `reimporta.py` | valida un lotto tradotto (firma, campi presenti, controlli di contenuto) e solo se pulito lo scrive nel dizionario |
| `verifica.py` | esegue le regole della §7 su un lotto o sull'intero dizionario |
| `compila.py` | pilota `hspcmp.dll` senza GUI e produce `.ax` ed eseguibile; `--cancello` verifica che il sorgente non modificato ricompili, senza produrre nulla |
| `installa.py` | copia la build in `C:\Games\Elona\elonaplus2.31\`, preservando l'eseguibile inglese e i salvataggi |
| `prova_identita.py` | applica un dizionario identità a tutto il corpus: i 72 file devono tornare byte per byte. Da rifare a ogni giro, prima di fidarsi dei test |

Ogni script è indipendente, con ingresso e uscita su file, invocabile da solo e
testabile senza gli altri.

---

## 9. Fuori ambito

Deliberatamente esclusi, per non gonfiare il progetto:

- traduzione del giapponese (si traduce **dall'inglese**: è la versione mantenuta
  da CGX e quella che l'autore del progetto legge);
- supporto multi-lingua o selettore in gioco — la build italiana è un eseguibile
  separato;
- traduzione della documentazione del gioco (`manual_ENG.txt`, changelog);
- port alla 2.32 finché CGX non la rilascia;
- pubblicazione, packaging delle release e verifica della licenza — si affrontano
  quando il progetto sarà maturo, e la §3.1 è progettata per renderli possibili.

---

## 10. Decisioni prese

Registrate anche in `decisioni.md` man mano che se ne aggiungono.

| # | Decisione | Motivo |
|---|---|---|
| 1 | Dizionario esterno, non fork del sorgente | Riallineamento senza conflitti a ogni release CGX; pubblicabilità; coerenza con Elin |
| 2 | Chiave = `sha1(jp + \0 + en)` per-file | Il giapponese è stabile; una modifica dell'inglese a monte deve rompere la firma di proposito |
| 3 | L'italiano sostituisce l'argomento inglese di `lang()` | Nessuna modifica alla macro né ai 26.817 siti di chiamata |
| 12 | La chiave è la sola firma; `occorrenza` è diagnostica | I duplicati esatti sono la stessa stringa: si traducono una volta e la traduzione vale per tutte le occorrenze |
| 13 | Il parser onora l'escape `\"` e cerca il `+` fuori dai letterali | Ignorarli scartava 11 `lang()`, produceva span che cancellavano codice dal sorgente e classificava dinamiche 163 statiche, facendo finire l'italiano nudo nel sorgente HSP |
| 14 | `applica.py` rilegge ogni riga che ha modificato | Quattro classi di traduzione passano `verifica.py` e producono sorgente rotto; una di esse — la virgola nuda — non dà alcun altro segnale |
| 15 | La scansione del sorgente è una sola, in `estrai.siti()` | Estrazione e applicazione devono percorrere gli stessi siti per costruzione, non per disciplina |
| 4 | Traduzione dall'inglese, non dal giapponese | È la versione mantenuta da CGX |
| 5 | Copertura per priorità a fasi giocabili | Ogni fase ha valore autonomo; l'abbandono a metà lascia comunque un risultato |
| 6 | Prova encoding **prima** di ogni traduzione in volume | Il rischio più grave del progetto; costa ore, non settimane |
| 7 | Base 2.31, non 2.32 | CGX non ha ancora rilasciato il port alla 2.32 |
| 16 | Sorgente pinnato al **tag** `2.31.2.0`, non alla testa di `work` | La testa di `work` è alla 2.32.1.2 non rilasciata, e si muove: ogni suo spostamento invaliderebbe in silenzio manifesto e conteggi. Il pin costa una rimisura, e il momento più economico per pagarla è con il dizionario vuoto |
| 17 | La compilazione si pilota da `hspcmp.dll`, non dalla GUI | La GUI non era un vincolo dell'SDK ma un'assunzione: la DLL espone tutta l'API. Serviva solo un host a 32 bit, e Windows ne ha già uno. Il cancello diventa così un comando ripetibile invece di un rito manuale |
| 8 | Accenti in forma con apostrofo (`perche'`) | CP932 non contiene le vocali accentate e le cancella senza avviso; è l'unica strada affidabile |
| 9 | Il dizionario conserva gli accenti veri, `applica.py` degrada in build | Tiene aperta la strada C senza ritraduzioni; converte in un punto solo e testabile |
| 10 | Virgolette `“ ”`, mai `"` nelle statiche, mai `«»` | `"` rompe il letterale HSP; `«»` non esiste in CP932 |
| 11 | Controllo d'integrità del sorgente con manifesto SHA-256, non `git status` | Nel clone del sorgente `git status` è permanentemente sporco per l'asimmetria di iconv sul byte `0x8160` |
