# Decisioni

Scelte non ovvie e il perché. Le decisioni numerate stanno in `SPEC.md` §10;
qui c'è il ragionamento che non ci stava in una riga di tabella, e le domande
ancora aperte.

---

## Come è andata la Fase 0

La catena `estrai → verifica → reimporta → applica` esiste, è coperta da **83
test** ed è stata provata end-to-end sul sorgente vero. Ma il **cancello vero
della Fase 0 non è ancora passato**: ricompilare l'eseguibile da sorgente non
modificato richiede la GUI dell'SDK HSP 3.4. Finché non passa, quella che
abbiamo è una *catena verificata*, non un *gioco verificato*.

### La prova che conta più di tutti i test

Un **dizionario identità** — ogni stringa tradotta in sé stessa — deve
riprodurre i file byte per byte. È la verifica più forte disponibile su questa
catena, perché non dipende da quali casi qualcuno si è ricordato di scrivere:
copre ogni sito del corpus reale.

Esito: **73 file su 73 identici**, con 22.602 sostituzioni eseguite.

È stata questa prova, e non i test, a trovare i due difetti più gravi del
progetto.

### I quattro difetti che i test non hanno visto

Tutti e quattro producevano **corruzione silenziosa**: virgolette pari,
parentesi bilanciate, nessun errore, sorgente rotto.

1. **Il parser era cieco all'escape `\"`.** 195 righe del sorgente lo usano.
   Costo misurato: 11 `lang()` perse, 295 voci con l'inglese mutilato, e 5 span
   sbagliati su cui `applica.py` sostituiva facendo **sparire dal sorgente** una
   chiamata `_onii(cdata(...))` e un'intera coppia `lang()`. Perdita di logica di
   gioco, non di testo.
2. **`e_dinamica` cercava il `+` anche dentro il testo.** 163 stringhe statiche
   contengono un `+` (`"Enchantment Bonus + 4"`, `"RES+ magic"`) e venivano
   classificate dinamiche, il che faceva finire l'italiano **nudo** nel sorgente.
   86 in file di Fase 1.
3. **Statiche avvolte in una chiamata.** `lang("…", cnvtalk("Urchinn!"))` non ha
   un `+` di primo livello, quindi è statica — ma sostituire l'intero span fa
   sparire `cnvtalk`. Sono **3.499**, in due sole forme: `cnvtalk(` (3.423) e
   `cnven(` (76).
4. **Firme che collidono su espressioni diverse.** La firma si calcola sui soli
   letterali, quindi `name(gdata(GDATA_RIDER)) + " glare"` e
   `cdatan(CDATAN_NAME, ttc) + " glare"` condividono la chiave: la traduzione
   dell'una finirebbe sull'altra portandosi dietro **le variabili sbagliate**.
   Sono **77 firme**, 334 occorrenze.

I primi due sono corretti. Il terzo e il quarto sono **rifiutati con un errore
esplicito** che nomina file, riga, firma e causa: la catena si ferma invece di
corrompere. Non è la soluzione definitiva, è il rifiuto onesto.

### Perché rifiutare invece di risolvere

Il cancello della Fase 0 è «la catena non corrompe il sorgente», e rifiutare lo
soddisfa in modo dimostrabile. Il caso 4 in particolare è una modifica allo
schema della chiave, cioè a `SPEC.md` §3.2: va decisa a mente fredda, non
improvvisata dentro una correzione.

---

## Il cancello è passato — 2026-08-06, seconda sessione

Il sorgente non modificato **ricompila**, l'eseguibile che ne esce si avvia dalla
cartella del gioco e **carica un salvataggio esistente**, provato in gioco. Da
*catena verificata* a *gioco verificato*: il salto che il progetto aspettava.

Il caricamento del salvataggio chiude anche la questione aperta dal pin: l'exe
ricompilato dal tag `2.31.2.0` e i dati della 2.31.2.0 installata sono
compatibili, nonostante la costante di versione discordante. Il disallineamento
è nominale, non sostanziale.

### La GUI non era un vincolo, era un'assunzione

`hspcmp.dll` espone l'intera API del compilatore: `hsc_ini`, `hsc_comp`,
`hsc3_make`. L'unico ostacolo reale è che la DLL è a **32 bit** e un Python a 64
non la carica. Windows ha però già un host a 32 bit installato di serie,
`SysWOW64\WindowsPowerShell`, e da lì si pilota tutto.

Tre trappole, nell'ordine in cui sono costate:

1. **I nomi puliti di `hspcmp.as` non esistono nella tabella di export.** Sono
   tutti decorati: `_hsc_ini@16`.
2. **L'ABI dei plugin HSP passa sempre quattro slot, e non nello stesso ordine
   per tutti.** Dal disassemblato: chi prende una stringa la legge da `[esp+8]`,
   cioè lo **slot 2**, con lo slot 1 inutilizzato; chi prende un buffer lo legge
   da `[esp+4]`, lo **slot 1**. Passare la stringa nel primo slot non dà errore:
   fa saltare il processo con una access violation. Questo è il motivo per cui
   `test_compila.py` verifica le firme dichiarate — è l'unica difesa contro una
   "semplificazione" che riporterebbe il crash.
3. **`Set-Location` non sposta la cwd del processo**, solo quella di PowerShell.
   La DLL legge la cwd vera e rispondeva `Source file not found` su un file che
   esisteva. Gli `#include` del sorgente sono relativi, quindi la cwd conta.

Il cancello è ora un comando: `python -m strumenti.compila --cancello`. Gli
strumenti si rifiutano di scrivere dentro `sorgente/`, e la costruzione dell'exe
è ammessa solo fuori, perché `#pack` scrive `packfile` nella cartella corrente.

### Il sorgente era sul ref sbagliato

Il clone era sulla testa di `work`, che dichiara **2.32.1.2** — una versione non
rilasciata — mentre `SPEC.md` decisione 7 sceglie la base 2.31. Il tag `2.31.2.0`
esiste, compila, ed è immutabile: il sorgente è stato pinnato lì (`a9135a6`).

Un branch che si muove è la peggiore base possibile per questo progetto: al primo
`git pull` manifesto e conteggi diventerebbero falsi **senza alcun segnale**. Il
pin costa una rimisura del corpus, e il momento più economico per pagarla è
adesso, con `dizionario/` vuoto.

Un fatto emerso strada facendo, che non è un difetto nostro: **il binario
installato non è riproducibile da nessun ref pubblico**. Il tag `2.31.2.0`
dichiara `VARIANT_TITLE "… 2.31.1.0"` e produce un eseguibile intitolato così;
nessun commit della storia dichiara `2.31.2.0`. La costante non è stata aggiornata
al rilascio. Tocca solo il numero nel titolo, non il testo da tradurre.

### I numeri, rimisurati sul tag

| | prima (testa di `work`) | ora (tag `2.31.2.0`) |
|---|---|---|
| occorrenze `lang()` | 26.817 | 26.588 |
| traducibili | 26.434 | 26.206 |
| da tradurre (uniche per file) | 21.965 | 21.795 |

**Il 21.965 non era sbagliato**, contrariamente a quanto sembrava a prima vista:
è l'unicità **per file**, che è l'ambito dichiarato in `SPEC.md` §3.2 e realizzato
dal partizionamento del dizionario in un `.jsonl` per file sorgente. Le firme
distinte sull'intero corpus sono invece 19.399: la differenza, 2.396 traduzioni
pari all'11% del lavoro, è il prezzo misurato dell'ambito per-file. Da conoscere
prima di discuterlo, non una proposta di cambiarlo.

---

## Domande aperte, da decidere prima della Fase 1

### 1. La firma delle dinamiche include l'espressione — DECISA il 2026-08-06

**Sì, ma solo per le dinamiche**, e con gli spazi normalizzati.

Il nodo: `firma = sha1(giapponese + NUL + inglese)` usava i soli letterali, e per
le dinamiche faceva collidere espressioni diverse che condividono il testo — 77
firme, 327 occorrenze. Includere `en_grezzo` risolve la collisione ma rende la
chiave fragile: rinominare una variabile a monte la rompe a testo invariato.

**Quello che scioglie il nodo è che i due errori non costano uguale.** Una chiave
troppo debole scrive codice sbagliato **in silenzio** — la traduzione di
`name(gdata(GDATA_RIDER)) + " glare"` iniettata su `cdatan(CDATAN_NAME, ttc) + " glare"`
si porta dietro le variabili sbagliate. Una chiave troppo fragile manda la stringa
in **coda di ritraduzione**, dove una persona la guarda. È la stessa asimmetria su
cui il progetto aveva già deciso con le decisioni 13 e 14: preferire il guasto
rumoroso a quello silenzioso.

Due correttivi tolgono quasi tutta la fragilità:

1. **la firma normalizza gli spazi**, quindi reindentare a monte non rompe nulla;
2. **la voce conserva `jp` ed `en`**, quindi una firma orfana la cui coppia
   corrisponde a una sola firma nuova si riaggancia meccanicamente. La fragilità
   diventa recuperabile invece che distruttiva.

Le statiche restano com'erano: includere l'involucro sarebbe churn senza guadagno.

**Il prezzo, misurato e non stimato:**

| | prima | dopo |
|---|---|---|
| da tradurre (uniche per file) | 21.795 | **22.030** (+235) |
| occorrenze irraggiungibili | 327 | **3** |
| sostituzioni nella prova d'identità | 22.414 | **22.738** (+324) |

Le 3 residue non sono una collisione di espressioni: sono la stessa statica
presente sia nuda sia avvolta in `cnvtalk(`, in `db_creature.hsp`. Per le statiche
l'involucro non entra nella chiave, quindi condividono la firma pur volendo
sostituzioni diverse. Spariranno quando la sostituzione dentro l'involucro sarà
implementata — che è comunque il punto 1 del piano di Fase 1.

Il controllo in `applica.py` che rifiutava le collisioni **resta**, ma cambia
significato: il sorgente non le produce più, quindi ora è la difesa contro una
voce di dizionario ritoccata a mano. Confronta le espressioni normalizzate, non
le grezze: differire di soli spazi non è un motivo per abortire un build.

### 2. Il rifiuto arriva troppo tardi nel ciclo

`estrai.py` emette comunque le 3.833 occorrenze dei casi 3 e 4 nei lotti, e
`verifica.py` non le segnala. Un traduttore le traduce, `reimporta` le accetta, e
solo `applica` esplode — abortendo l'intero build su un caso alla volta.

Il rilevamento va spostato a monte, in `estrai`/`verifica`, o le voci vanno
marcate nel lotto. Altrimenti si scopre il problema dopo aver tradotto.

---

## Rilievi parcheggiati

Reali ma non bloccanti, valutati e lasciati:

- `applica.py` importa ancora il privato `estrai._argomenti` per `_profilo`.
- `applica.main()` scrive i file uno alla volta: un errore lascia l'albero di
  build a metà. Innocuo perché `build/` è usa e getta, ma incoerente col rigore
  tutto-o-niente applicato a `reimporta`.
- Il controllo del caso 4 è saltato in silenzio se una voce di dizionario
  ritoccata a mano è priva di `en_grezzo`: `verifica.py` lo pretende, ma
  `applica.main()` legge i `.jsonl` senza passare da `verifica`.
- `_letterali` conserva gli escape come `\"` invece che `"`: fedele e
  reversibile, ma chi traduce lo vede nel campo `en`. Da fissare nella guida di
  stile.

---

## Da portare nel piano della Fase 1

In quest'ordine:

1. Sostituzione dentro `cnvtalk(` / `cnven(` — **bloccante per la Fase 2**, ma è
   lavoro di poche righe: non è una famiglia aperta di involucri, sono due forme
   sole.
2. ~~La decisione sulla firma delle dinamiche, §3.2~~ — **fatta**, vedi sopra.
3. Spostare a monte il rilevamento dei casi 3 e 4. Il caso 4 non si presenta più
   dal sorgente, quindi resta il solo caso 3: `estrai`/`verifica` devono marcare
   le 3.465 statiche avvolte, invece di lasciarle scoprire a build abortito.
4. La whitelist `invariati.md` per la regola «identica all'inglese»: `SPEC.md` §7
   la promette ma non è implementata, e senza di essa i nomi propri e le sigle
   non hanno via d'uscita — il rischio concreto è che si aggiri la regola
   scrivendo traduzioni finte.
5. Il modo `verifica --dizionario` che confronta dizionario e sorgente e produce
   la coda di ritraduzione. `SPEC.md` §3.1 ne fa il cardine dell'architettura, ma
   non esiste: oggi una firma orfana viene solo contata da `applica`.
