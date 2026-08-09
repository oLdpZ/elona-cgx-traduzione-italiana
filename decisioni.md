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

Chiuso tutto il 2026-08-07.

1. ~~Sostituzione dentro `cnvtalk(` / `cnven(`~~ — **fatta** (Task 2).
2. ~~La decisione sulla firma delle dinamiche, §3.2~~ — **fatta**, vedi sopra.
3. ~~Spostare a monte il rilevamento delle statiche avvolte~~ — **decaduta**: dal
   momento in cui si sostituiscono, non c'è più niente da segnalare a monte.
4. ~~La whitelist `invariati.md`~~ — **fatta** (Task 3).
5. ~~`verifica --dizionario`~~ — **fatta** (Task 4).

---

## La quarta sessione — 2026-08-07

### Il registro: terza persona, e `init.hsp` risale alla Fase 1

Il piano della Fase 1 affermava che qui il «tu» fosse sicuro, «perché le righe
del giocatore e quelle dei PNG sono chiamate `lang()` diverse». **È falso**, e la
guida di stile stava per essere scritta su quella premessa.

`init.hsp:1699` — `name()` risolve da sé chi è il soggetto:

```hsp
if ( name_arg1 == CHARA_PLAYER ) { return lang("あなた", "you") }
...
return "the " + cdatan(CDATAN_NAME, name_arg1)
```

Una sola `lang()` serve entrambi, come il `#1` di Elin. Il caso canonico è
`text.hsp:3137`: `name(X) + " lose" + _s(X) + " patience."` diventa «you lose
patience.» oppure «the putit loses patience.» L'inglese se la cava con `_s()`,
che è morfologia; l'italiano no, e il Task 1 aveva già stabilito che `_s()` va
tolta. Resta una forma verbale sola, e la seconda persona non regge: «il putit
perdi la pazienza».

Misurato sui sei file di Fase 1: 1.522 dinamiche, **901 con `name()`**, **472
(31%) con un marcatore di morfologia**, cioè dimostrabilmente condivise.

**Decisione: terza persona singolare presente indicativo**, l'unica forma senza
accordo di genere. `you` → «il viandante», `he`/`she` → «lui»/«lei».

**Conseguenza sul piano: `init.hsp` non è lavoro di Fase 4, è una premessa della
Fase 1.** Sei voci tradotte subito, 16 sostituzioni.

Elin era arrivata alla stessa conclusione dopo averlo visto a schermo; qui è
arrivata prima, leggendo il codice.

### Le stringhe che sono dati — la trappola peggiore trovata finora

Le otto stringhe di `CDATAN_NEWSEX` (`male`, `female`, `none`, `hermaphrodite`,
`male?`, `female?`, `trans-male`, `trans-female`) stanno **nella stessa funzione**
dei pronomi appena tradotti, dentro `lang()` identiche a quelle dei messaggi.
Sembrano testo. Non lo sono: `chara.hsp:2790` e `4390` le **scrivono** nei dati
del personaggio, `init.hsp:1813-1823` le rilegge come **operandi di confronto**, e
i dati del personaggio finiscono nel salvataggio.

Tradurle non rompe niente il giorno stesso: rompe il genere di ogni personaggio
creato **prima** della traduzione, cioè vanifica in silenzio proprio ciò che il
cancello della Fase 0 aveva verificato con cura — che i salvataggi esistenti si
carichino.

Sono in `invariati.md`, sezione «valori di dato, non testo». La ricerca da fare
prima di tradurre un file nuovo:

```
grep -nE '(=|==|!=|instr\().*lang\(' <file>.hsp
```

**La prova d'identità non le prende**, ed è importante saperlo: la stringa cambia
legittimamente, la forma resta valida, ed è il significato a rompersi. Contro
questa classe serve la lettura, non il round-trip.

### `toppe.jsonl` — le sostituzioni fuori da `lang()`

`init.hsp:1718` concatena `"the "` davanti al nome dei PNG **fuori** da una
`lang()`: il dizionario non lo raggiunge, e senza quel pezzo la decisione sul
registro non sta in piedi. Sul sorgente intero i casi così sono **dieci**, in
quattro file.

Non è una deroga alla §3.1: come il dizionario, le toppe sono dati esterni
applicati all'albero di build. Verificato col manifesto dopo la build, 72/72 hash
concordi. Hanno un giro proprio in `applica.main()` e **la prova d'identità non ci
passa**, quindi la garanzia byte per byte resta quella di prima.

**La toppa toglie invece di scegliere.** L'articolo italiano dipende da genere ed
elisione — *il* putit, *lo* gnomo, *l'* orco — che si sanno per nome e non per
regola. Il prefisso si rimuove e l'articolo lo porterà il nome della creatura in
`db_creature.hsp`, **dove a decidere è un umano**. È una decisione di Fase 2 e
vale per ogni uso di `cdatan()`, non solo per `name()`.

`custom_dmgpop.hsp:224-231` *legge* la stringa `"the "` per toglierla dagli
alias: era il rischio di accoppiamento silenzioso. È protetto da `instr(...) !=
-1`, quindi senza `"the "` diventa un no-op — verificato leggendolo.

### La re-revisione di `dfe530b`: un fratello del difetto

I due punti che il rilievo chiedeva reggevano. Ma il controllo lasciava passare
`cnvtalk("x"), cnvtalk("y")`: il gruppo greedy ne cattura `"x"), cnvtalk("y"`, un
frammento con le parentesi **sbilanciate**, dove `virgola_nuda` arriva con la
profondità già a -1 e non vede la virgola di primo livello. La ricostruzione
avrebbe prodotto `cnvtalk("Ciao")`, facendo sparire la seconda chiamata.

La causa era contare sulla struttura di un frammento che per costruzione può
essere sbilanciato. `_e_letterale_singolo` non la interpreta: pretende che fra le
parentesi ci sia un letterale e nient'altro. Zero occorrenze nel sorgente
pinnato: era latente.

### Il primo lotto, visto a schermo

50 stringhe di `text.hsp`, **composte** e non prese in ordine: la prima dinamica
con morfologia sta alla voce 642, e seguire il piano alla lettera avrebbe voluto
`--max 646`. Il lotto è 44 statiche di testa più le 6 dinamiche delle righe
276-290, che sono la prova della decisione sul registro.

Sulle sei, la resa evita i **sostantivi di genere**: «un cittadino rispettoso
della legge» non regge con `he(tc,1)` che può valere «lei». Si traduce con un
verbo — «rispetta la legge di questa pacifica città». Regola generale per le
condivise.

**Il collaudo a schermo è passato il 2026-08-07**: `Non e' roba tua.` letta in
gioco, con l'apostrofo. La degradazione CP932 non è più verificata sui byte, è
osservata. Era il punto in cui il piano diceva di fermare tutto.

Un artefatto atteso dello stato intermedio: «il viandante pick up a book», con il
verbo inglese senza `s` perché `_s(cc)` restituisce `""` per il giocatore.
Sparisce quando `action.hsp` sarà tradotto. E la minuscola iniziale non è una
regressione: nella catena `txt` → `txt_select` → `txt_conv` non c'è nessuna
capitalizzazione, e in inglese quella riga esce «you pick up…» uguale.

## La quinta sessione — 2026-08-07

### I sei termini: cinque erano misura, uno era già deciso altrove

I sei di «Da decidere» sembravano sei scelte di gusto. Misurandoli, quattro
avevano una risposta nei dati e due erano già vincolati da Elin.

**`Gauge` non è prosa.** 60 occorrenze su 75 sono etichette dell'elenco delle
mosse speciali, a larghezza compressa: `[50% Gauge] Party Shooting`. La scelta
non era fra sinonimi ma fra lunghezze — «Barra» costa 5 caratteri come
l'inglese, «Indicatore» ne costava 6 in più su ogni riga. In prosa «barra di
potenza», che si aggancia a `Power` → «Potenza» invece di derogarci.

**La collisione di `Skill` non esisteva.** Il timore era che «Abilità» si
scontrasse con *ability*. Nel sorgente non si incontrano mai: `Skill` è sempre
il concetto di motore, *ability* è quasi sempre prosa generica («enhances your
ability to hide»), che in italiano vuole «capacità». Un dubbio che si scioglie
guardando, non discutendo.

**`Chaos` e `Abyss` erano già decisi**, in `Elin - Traduzione Italiana`: «Caos»
e «Abisso». Sono termini di universo, non di motore, e il glossario dichiara
che quelli devono coincidere fra i due progetti. Non erano da decidere: erano
da andare a leggere.

**`Body` non era un termine, erano tre.** Lo slot d'equipaggiamento
(`text.hsp:136`, giapponese 胴), l'aspetto nell'editor del ritratto (giapponese
体) e la prosa. «Torso» per il primo, perché in fila con Testa · Collo ·
Schiena · Mano · Braccio · Gamba un «Corpo» metterebbe il tutto insieme alle
parti. Registrato anche un vincolo che non si vede dal glossario: l'editor è a
**larghezza fissa di 8 caratteri**, e «Colore corpo» per `Body CL ` non ci sta.

### La regola dei nomi propri, che vale più delle cinque decisioni che l'hanno prodotta

I cinque toponimi aperti si potevano chiudere uno per uno. Ma altri ne
arriveranno a ogni file, e cinque decisioni singole non dicono niente al
prossimo. La regola:

- nome **descrittivo**, fatto di parole comuni → si traduce (`Fort of Chaos
  <Beast>` → «Forte del Caos `<Bestia>`», come `Mages Guild` → «Gilda dei
  Maghi» che era già in glossario);
- nome **opaco**, inventato → resta (`Vernis`, `Larna`, `Arcbelc`, `Lesimas`);
- nome **misto** → si divide (`Port Kapul` → «Porto Kapul»).

È lo stesso criterio con cui Elin ha reso `Blessing of the Abyss`. Chiude anche
il sotto-caso di `Chaos`, che era la ragione per cui quel termine era in
«Da decidere»: l'elemento e i luoghi si decidono insieme perché li decide la
stessa regola.

### 424 nomi di creatura travestiti da testo, in un file di Fase 1

Trovato cercando le occorrenze di `Sister`. `Wolf Sister`, `older sister`,
`younger sister` in `action.hsp` non sono prosa: sono `evname`/`evold`, il
sistema di evoluzione dei nemici. **424 assegnazioni, 232 valori `evold`
distinti, 203 dei quali sono nomi di creatura letterali di `db_creature.hsp`** —
che è Fase 2.

```
if ( strmid(cdatan(CDATAN_NAME, cc), 0, strlen(evold)) == evold ) {
    cdatan(CDATAN_NAME, cc) = evname + strmid(cdatan(CDATAN_NAME, cc), ...)
```

`evold` è l'**operando** confrontato col nome memorizzato del personaggio;
`evname` è il pezzo che lo **sostituisce**, e che poi si legge a schermo come
nome della creatura evoluta. In inglese `evname` non è mai stampato
direttamente: l'unico `txt` che lo contiene (`action.hsp:18632`) lo ha solo nel
ramo giapponese.

È la stessa classe di `CDATAN_NEWSEX`, ma con un vincolo in più: non basta
lasciarli stare. **Vanno tradotti in blocco con `db_creature.hsp`, mai prima** —
se uno dei due è italiano e l'altro no il confronto fallisce e l'evoluzione
smette di rinominare **in silenzio**; e sui salvataggi esistenti si rompono
comunque, perché lì il nome è già inglese. La prova d'identità non li prende.

Non sono fra gli invariati: dichiararli tali deciderebbe di lasciare i nomi
delle creature in inglese per sempre, che è una decisione di Fase 2 e non è
stata presa. Hanno una sezione propria in `invariati.md`.

### Il difetto che rendeva obbligatorio cadere nella trappola

Le otto stringhe di `CDATAN_NEWSEX` **non erano protette**. Verificato:
`carica_invariati()` restituiva dieci valori, e `male` non era fra loro.

La difesa scritta nella seconda sessione era «`carica_invariati` si ferma al
primo `##`», per non leggere i candidati di «Da decidere». Ragionamento giusto,
difesa fragile: quando la sezione «Valori di dato» fu inserita **in mezzo**,
ereditò l'esclusione senza che nessuno lo decidesse.

La conseguenza non era quella che sembrava. Il conteggio «non ancora tradotte»
non ha mai consultato gli invariati. `invariati` entra in un punto solo,
`controlla_voce`, sulla regola «traduzione identica all'inglese». Un lotto che
lasciava `male` → `male`, cioè che faceva **esattamente ciò che `invariati.md`
prescrive**, inciampava in quella regola e `controlla_lotto` rifiutava il lotto
**intero**. L'unico modo di farlo passare era tradurle.

Il controllo non sollecitava la trappola: la **imponeva**.

La correzione non sposta il confine — sarebbe il sintomo, e il prossimo che
aggiunge una sezione rifarebbe il buco. `carica_invariati` legge sezione per
sezione e le **classifica**, e **non c'è un default**: una sezione che porta
valori senza essere classificata alza `ValueError` con scritto cosa fare. Una
sezione di sola prosa non è una decisione, e si ignora.

La lezione, che vale oltre questo file: una difesa fatta di «fermati al primo
X» presume che nessuno inserisca niente prima di X. Una fatta di «ogni caso va
classificato, e il silenzio è un errore» no.

## L'ottava sessione — 2026-08-08

Il secondo lotto dei nomi di `db_item.hsp`: **166 firme**, da riga 150006 a
151839, cioè tutto quel che restava del **corredo vanilla** in coda al file —
cibo ed erbe, l'arredamento della casa, le bacchette, i grimori e le pozioni.
Il lotto non è stato scelto con `--max`: quello prende le prime per **riga**,
che sono gli oggetti aggiunti da CGX e si vedono solo andandoseli a cercare.

### Quattro decisioni di resa che valgono oltre il lotto

**Il giunto è sempre «di», quindi la testa del nome composto può portarsi
dietro il participio.** `grave` + `ornamented with flowers` non poteva diventare
«tomba di fiori ornamentali» senza perdere l'ornamento. La soluzione non è nel
modificatore ma nella **testa**: `ioriginalnameref2` → «tomba ornata»,
`ioriginalnameref` → «fiori», e il giunto cablato fa il resto — «tomba ornata
di fiori», «tombe ornate di fiori». Il pezzo che si flette al plurale è la
testa, quindi l'accordo del participio viene gratis.

**I nomi di divinità restano complemento, e l'epiteto diventa sostantivo.**
`potion of sacred healer <Jure>` non poteva essere «pozione di sacra guaritrice
<Jure>»: il giunto fisso «di» non diventa «della», e senza articolo il
sintagma non regge. Le quattro pozioni curative diventano una scala di
sostantivi — «guarigione», «guarigione <Odina>», «guarigione bianca <Eris>»,
«guarigione sacra <Jure>» — che dopo «pozione di» si leggono tutte. È la
**quinta** volta che il genere ignoto si risolve col sostantivo invece che con
l'aggettivo, ed è la prima in cui il vincolo non è il genere ma la preposizione.

**Quando la parola italiana coincide con l'inglese si dichiara, non si evita.**
Dodici voci su 166: due artefatti che il giapponese traslittera
(《エーテルダガー》, 《ラグナロク》), quattro frutti inventati da Elona
(`leccho`, `qucche`, `imo`, `quwapana`), cinque nomi botanici che l'italiano
scrive uguale (`guava`, `kiwi`, `aloe`, `anemone`, `gazania`) e `whisky`. Sono
tutte righe di `invariati.md` con un motivo scritto, perché senza `verifica.py`
rifiuta il lotto intero — ed è il comportamento voluto: una coincidenza
dichiarata e una traduzione dimenticata si somigliano troppo per distinguerle
a occhio.

⚠️ **Un nome opaco può collidere con una parola comune italiana.**
`api nut` (アピの実) reso «noce di api» si legge «noce di insetti». La maiuscola
lo rimette dov'era: «noce di **A**pi». Da rifare a ogni nome opaco che, tradotto
alla lettera, produce una parola italiana esistente.

### Due rese scelte per non collidere con un'etichetta

`cheap chair` e `cheap bed` sono «sedia **dozzinale**» e «letto dozzinale», non
«scadente»: `scadente` è già la prima delle sei qualità dell'oggetto
(`text.hsp:106`), e le due escono **attaccate** — «una sedia scadente
(Scadente)». Stessa logica di «l'etichetta si legge dove esce» in
`guida-stile.md`, applicata al verso opposto: lì si sceglieva l'etichetta
guardando il nome, qui si sceglie il nome guardando l'etichetta.

### L'articolo: il genere e' il dato, l'articolo e' una derivata

L'inglese sceglie `a`/`an` guardando la **prima lettera** della stringa gia'
composta (`item_func.hsp:1816`), piu' un caso speciale scritto a mano per
`unicorn horn`. Funziona perche' in inglese l'articolo non ha genere: e'
fonetica pura. In italiano l'articolo dipende dal **genere della testa**, che
nella stringa composta sta in mezzo — «una pozione di cura delle ferite lievi»
— e nessuna lettera lo rivela.

Il genere entra quindi nel dizionario come quinta colonna dei nomi, accanto al
plurale, e per la stessa ragione: non si deduce. Ma **l'articolo no**. Una
volta noto il genere, la scelta fra «un» e «uno», fra «la» e «l'», e' una
regola meccanica sulla forma della parola che segue — s impura, z, gn, ps, pn,
x, y, semiconsonante, h muta. Chiederla a chi traduce vorrebbe dire chiedergli
di applicare a mano una regola che una macchina applica meglio, e raddoppiare
le occasioni di sbagliarla. La deriva `strumenti/articolo.py`; nel gioco arriva
la stringa gia' fatta, come per il plurale.

**Il numero fa parte del genere**, e i valori sono quattro: `m`, `f`, `mp`,
`fp`. Non e' pignoleria: in `db_item.hsp` i nomi che esistono solo al plurale
non sono pochi — «cianfrusaglie», «attrezzi», «armi», «vestiti» — e su quelli
l'articolo indeterminativo **non esiste**. Ci vuole il partitivo, «delle
cianfrusaglie», che e' esattamente cio' che l'inglese sbaglia gia' oggi
scrivendo «a goods».

⚠️ **Le parole-contatore cablate vincono sull'array, al contrario del
plurale.** Quando `itemname()` mette «paio» davanti al nome, la testa del
sintagma diventa «paio» e l'articolo lo regge lui: «un paio di stivali
pesanti», non «uno stivali pesanti». Il plurale non ha lo stesso problema
perche' li' l'array e la parola cablata non sono mai pieni tutti e due.

L'articolo si scrive **solo sulla testa**: 207 oggetti su 252 voci tradotte,
perche' i composti hanno due voci e una testa sola.

### I 252 composti, e la terminologia degli incantesimi

Le teste non si sono decise nel lotto: erano gia' in `contatori.jsonl`. Il
lavoro erano i **218 modificatori distinti**, e il giapponese e' servito piu'
di una volta a non sbagliare — `butuzou` e' 仏像, la statua di Budda; `soul` e'
リンカネイト, la reincarnazione; `acid ground` e' 酸の海, che alla lettera e' un
mare d'acido ma in gioco e' un suolo.

Da qui in avanti questa terminologia vincola `skill.hsp`, che gli stessi
incantesimi li nomina di nuovo:

- **la famiglia dei dardi** segue quella gia' a schermo (dardo di fuoco, di
  ghiaccio, di fulmine). Per l'elemento si usa **l'aggettivo dove l'italiano ce
  l'ha** — mentale, caotico, oscuro, sonoro, neurale, che e' anche cio' che il
  glossario aveva gia' deciso per `Mind` e `Chaos` — e il **complemento dove
  no**: di veleno, d'oltretomba, d'acqua;
- `magic bolt` e `magic missile` **convivono nel sorgente**, quindi devono
  convivere anche in italiano: «dardo arcano» e «dardo magico». Una resa sola
  per due nomi diversi fonderebbe due oggetti distinti in uno;
- `magical map` (pergamena) e `magic mapping` (grimorio e bacchetta) hanno lo
  **stesso giapponese** 魔法の地図 e nomi inglesi diversi: «mappa magica» e
  «cartografia magica». Quando l'inglese distingue e il giapponese no, la
  distinzione si tiene: e' l'inglese la lingua da cui si traduce.

⚠️ **`Mani` entra negli invariati con una nota che vale oltre lui.** La
divinita' si chiama Mani, e «mani» minuscolo e' una parola italiana
comunissima: la maiuscola non e' decorativa, e' cio' che tiene «statua di Mani»
distinto da «statua di mani». Stessa classe di `noce di Api` del lotto
precedente, ed e' la seconda volta in un giorno.

### Due rese di `contatori.jsonl` riviste

Il secondo lotto aveva reso `lot` e `variety` senza guardare il termbase, e ci
sono finite dentro due deviazioni. Non si e' derogato nel lotto: si e'
cambiato il termbase, che e' la regola scritta in testa a `glossario.md`.

- `lot` → **mucchio**, non «lotto»: 本の山 e' una pila di libri, e «un lotto di
  libri» e' gergo commerciale;
- `variety` → **assortimento**, non «varietà»: regge meglio dopo «di» e non
  porta un accento in un punto molto visibile.

## La nona sessione — 2026-08-08

Sei blocchi, dodici commit, il primo push. `db_item.hsp` dal 47% al 63%.

### «Stessa forma» era un'ipotesi, e quattro array su quattro l'hanno smentita

Il documento di ripresa dava `_furniture`, `_bookself`, `_weight` e
`_bookselfs` per «la stessa identica forma»: sono tutti aggettivi prefissi in
`text.hsp`, e nel **dizionario** si somigliano davvero. Nel **codice** no.

| array | dove esce | cura |
|---|---|---|
| `_furniture` | prefisso (`item_func.hsp:1324`) | toppa: in coda su `locvar_itemname_s6` |
| `_bookself` | già fra parentesi (`:988`) | **nessuna toppa**, solo dato |
| `_weight` | già suffisso, giunto « grown » (`:974`) | toppa **sul giunto** |
| `_bookselfs` | slot parola-contatore (`:1233`) | trattamento `contatori.jsonl` |

**La regola che ne resta: prima di scrivere la toppa si guarda il sito di
concatenazione.** La somiglianza nel dizionario non dice niente su dove il
codice mette la stringa, e la cura la decide il codice.

Il caso più istruttivo è `_weight`. Era già un suffisso, quindi «spostarlo» non
voleva dire nulla; ma un aggettivo italiano in coda si sarebbe accordato lo
stesso col nome, di genere ignoto. **La leva non era la posizione ma il
giunto**: « grown » → « di taglia » introduce una testa femminile e fissa, e da
lì in poi l'accordo è con «taglia». È un modo nuovo di risolvere il genere
ignoto, il terzo dopo il complemento e il sostantivo al posto dell'aggettivo.

E `_bookself` è il primo caso della famiglia in cui **il sorgente andava bene
com'era**: esce fra parentesi, dove la parola sta da sola e non si accorda con
niente. Valeva la pena guardare prima di toccare.

### Un legame per stringa, che nessun controllo esistente vedeva

`_bookselfs` finisce in `locvar_itemname_s2`, e i due `switch` generati
confrontano la resa di `contatori.jsonl` con quella che l'array porta a
runtime, che viene dal dizionario. **Se divergono, il `case` non aggancia mai —
e restano verdi sia il compilatore sia la prova d'identità.**

Non è un difetto della prova d'identità: lei giudica la pipeline delle
sostituzioni, e le toppe girano dopo, in un giro loro. È una classe di errore
che nessuno dei due guardiani copre. Ora lo pretendono `genera_toppe_nomi.py`
alla generazione e un test a ogni giro.

### Il criterio della classe, e dove finisce

I lotti dal terzo al sesto sono stati scelti per `filter_item(ITEM_ID_X)`, che
sta in un blocco lontano dai nomi. Ha funzionato ogni volta, per un motivo che
conviene scrivere: **una classe raccoglie oggetti che pongono la stessa
domanda**, e una domanda posta una volta si risponde una volta.

Ha smesso di funzionare quando le classi sono finite. Le 599 voci rimaste sono
esattamente quelle **senza** filtro: non una classe, un residuo. Dentro ci sono
169 artefatti fra `<>`, per i quali la domanda non è di resa ma di
**invarianza** — e il criterio nuovo sarà la forma del nome.

### Quattro decisioni di resa dell'equipaggiamento

- `gauntlets` → «guanti d'arme» contro `gloves` → «guanti». L'inglese distingue
  protezione e indumento, e l'italiano può seguirlo. **Eccezione dichiarata**:
  `decorated gloves` è «guanti d'arme decorati» benché l'inglese dica *gloves*,
  perché il sorgente lo tratta come guanto d'arme (`item_func.hsp:1849-1850`);
- `mail` → «corazza», non «cotta» — tranne `chain mail` → «cotta di maglia»,
  dove la cotta è davvero la cosa;
- `lance`/`spear`: l'inglese ha due parole, l'italiano una. La distinzione si
  tiene col **complemento** («lancia da cavaliere» contro «lancia»), non
  inventando un secondo sostantivo. È la stessa cura del giunto dei composti;
- `claymore` → «spadone», `bardish` → «ascia lunga»: il giapponese dice 大剣 e
  大斧, e i nomi scozzese e slavo in italiano non aggiungono nulla.

### La storia naturale: nome vero se esiste, invariante se inventato

`hotate` → «capasanta», `cutlassfish` → «pesce sciabola», `spotted garden eel`
→ «anguilla giardiniera». E quando due pesci rischiano lo stesso nome si
separano apposta: `manboo` → «pesce luna» (mola mola), `moonfish` → «pesce re»
(Lampris), che è il nome italiano vero del secondo.

Restano invariati e dichiarati i nomi inventati da Elona — `mesugaki`, `sazae`,
`fane`, `dernefia` e le quattro erbe del canone.

### Una deroga dichiarata: i diari delle sorelle

`dog sister's diary` e `cat sister's diary` traducono 姉の秘密の日記 e
妹の秘密の日記, cioè «il diario **segreto** della sorella maggiore/minore».
Tradurre dall'inglese avrebbe dato «diario della sorella cane», che non vuol
dire nulla in nessuna lingua.

**Qui si è derogato alla regola «si traduce dall'inglese», perché l'inglese è
una svista e non una scelta.** Le rese sono «diario segreto della sorella
maggiore/minore», e restano distinte dalle due non segrete, che nel gioco sono
oggetti diversi. La deroga è dichiarata perché la prossima volta il criterio
sia già scritto: si deroga quando l'inglese perde informazione che il giapponese
ha, e la resa letterale produrrebbe una frase priva di senso.

### Il verificatore che rifiuta il lotto intero è un pregio

Ha bloccato l'equipaggiamento finché i sette prestiti giapponesi — `katana`,
`wakizashi`, `kunai`, `shuriken`, `nunchaku`, `shakujo`, `tomahawk` — non erano
in `invariati.md`. È la regola «si dichiara, non si evita» che morde invece di
lasciar passare, ed è costato cinque minuti contro un elenco di invarianti che
sarebbe rimasto incompleto per sempre.

### Un caso in cui i due campi del dizionario dicono cose diverse

`unicorn horn` ha genere `m` e plurale «corna di unicorno». In italiano «corno»
fa «corna» quando sono di un animale: il genere del singolare e la forma del
plurale non si deducono l'uno dall'altra, ed è esattamente il motivo per cui
sono due campi.

## La decima sessione — 2026-08-09

### Il residuo non esisteva: la categoria che il sorgente dichiara

I lotti dal terzo al sesto erano stati scelti per `filter_item`, e quando quel
criterio si è esaurito ciò che restava di `db_item.hsp` si chiamava «il gruppo
senza filtro»: un residuo da affrontare a occhio.

Non era un residuo. La categoria c'è, solo che non sta in `filter_item` ma
**dentro il blocco di ogni oggetto**:

```
if ( dbid == ITEM_ID_HAMBURGER ) {
    ...
    reftype = FILTER_ITEM_FOOD
```

Sono **1.320 oggetti classificati dal sorgente**. Letto con quella chiave, il
residuo torna a essere fatto di classi — `FILTER_ITEM_TOOL`, `FILTER_FURNITURE`,
`FILTER_JUNK`, `FILTER_ITEM_FOOD`, `FILTER_CONTAINER` — e i cinque lotti che
hanno chiuso il file sono usciti tutti da lì.

**La regola: prima di dichiarare che una cosa non ha struttura, si cerca dove il
codice la struttura.** Il criterio è diventato `strumenti/categorie.py`, con
cinque test, perché uno script usa e getta avrebbe costretto la prossima
sessione a riscoprirlo. Il quinto test è la rete: **ogni nome ancora da tradurre
ha una categoria**, così se domani ne arrivasse uno senza, il criterio non
tornerebbe a essere un occhio senza che nessuno lo dica.

### La marca 《》: l'invarianza degli artefatti si legge nei dati

I 169 artefatti fra `<>` ponevano una domanda di invarianza, non di resa. La
regola che ne è uscita ha tre gradini in ordine di precedenza:

1. l'inglese è già una **romanizzazione, una coniazione o una sigla** →
   invariato. Si traduce dall'inglese, e se l'inglese non dice niente non c'è
   niente da rendere;
2. il giapponese sta fra 《》 **ed è traslitterato in katakana** → invariato:
   quando l'originale traslittera, non legge il nome come descrizione;
3. il giapponese è **descrittivo in kanji**, o non porta la marca 《》 →
   tradotto, tenendo le `<>`.

Il pezzo nuovo è la **marca 《》**, e viene dai dati: 157 nomi su 169 ce l'hanno,
dodici no — e quei dodici sono esattamente quelli che si leggono come oggetti
ordinari a cui l'inglese ha messo le `<>` per decorazione (`<Dog Whistle>` 犬笛,
`<Amulet of Jure>` 健康のお守り).

**La prova che la regola non è stata cucita addosso al lotto: riproduce tutti e
otto i precedenti già presi**, compresi i due che tirano in direzioni opposte —
`<Zantetsuken>` 《斬鉄剣》 invariato benché kanji, perché l'inglese è
romanizzazione, e `<Scythe of the Void>` 《虚無の大鎌》 tradotto benché porti la
marca, perché il kanji descrive.

Esito: 105 invariati e 63 tradotti.

### Quando l'inglese sceglie una lingua, la scelta è informazione

Tre casi diversi della stessa idea, trovati in tre lotti diversi:

- **`hamaki`** (葉巻). Il giapponese usa la **parola comune** per «sigaro», ma
  l'inglese ha scelto di romanizzarla. È il caso di `wakizashi` rifatto: si
  traduce dall'inglese, quindi resta. E poiché `cigarette` (紙巻タバコ) nello
  stesso lotto diventa «sigaretta», la distinzione che l'inglese fa fra i due
  resta visibile anche in italiano.
- **`Taktstock`** (コマンドタクト). L'inglese ha scelto il **tedesco**, e il
  tedesco resta tedesco come il latino resta latino in `aqua sanctio`. Renderlo
  «bacchetta» perderebbe la scelta di lingua che l'originale ha fatto.
- **`anering`** (アネワッシャー). Invariato per una ragione che si vede solo
  guardando le due lingue **insieme**: coniano cose diverse — il giapponese dice
  «rondella», l'inglese «anello». Quando le due lingue non descrivono la stessa
  cosa, non stanno descrivendo: stanno nominando.

### Il registro e il segmento: due livelli, non due verità

Chiudendo `db_item.hsp` una voce non tornava: `contatori.jsonl` registra
`grave` → «tomba», il dizionario rende lo stesso `grave` con «tomba ornata».

Sembrava una divergenza da sanare, e a dire di no è stato il **sito di
concatenazione**, come sempre. Il nome si monta `s2 + " " + s3 + " " + s1`, e la
toppa 3 fissa il giunto a «di». Per `ITEM_ID_GRAVE_ORNAMENTED_WITH_FLOWERS` le
due parti sono «tomba ornata» e «fiori»: a schermo esce **«tomba ornata di
fiori»**, e al plurale «3 tombe ornate di fiori».

L'aggettivo sta in `s2` perché **è lì che può accordarsi con la testa**. Con
«tomba» in `s2` uscirebbe «tomba di ornata di fiori»; con «tomba» più «fiori» si
perderebbe l'«ornamented». Il giunto è fisso: l'unico posto dove l'accordo può
vivere è la testa.

**Quindi il registro dice il termine e il dizionario dice il segmento.** Sono
due livelli, non due verità in conflitto — e allineare i due file avrebbe rotto
una resa giusta per far tornare un confronto sbagliato.

Il test nuovo vive al livello che li tiene insieme: la resa del dizionario
**comincia con** il termine del registro. Prende i 38 casi identici, accetta la
variante contestuale senza costringere a dichiarare un'eccezione falsa, e se un
domani una variante non fosse un prefisso lo dice — perché allora sarebbe una
testa diversa, e le teste diverse si dichiarano.

### Il primo rinvio deciso da `db_item.hsp`, e una procura che si è rotta

`<Pants of Ogre>` è rinviato alla Fase 2: il nome contiene `ogre`, e in
`db_creature.hsp` `orc` e `ogre` convivono come creature distinte (`orc
warrior`, `black orc` contro `slash ogre`, `shine ogre`). «Orco» non può
coprirle entrambe, e quale delle due se lo prenda è una decisione dei nomi di
creatura.

Il test `test_i_nomi_di_db_item_non_sono_rinviati_da_text` è caduto, e non
perché la proprietà che difende fosse violata. Diceva `== set()`: una
**procura**, vera solo finché `db_item.hsp` non aveva rinvii suoi. La proprietà
— nessuna rinviata di `text.hsp` toglie lavoro alla coda di `db_item.hsp` — è
rimasta vera per tutto il tempo. Adesso è scritta com'è: ogni firma che esce per
`db_item.hsp` viene da una riga **di** `db_item.hsp`.

**La lezione: un test che passa per procura passa finché il mondo somiglia a
quando l'hai scritto.** Quando cade, la prima domanda è se sia caduta la
proprietà o la procura.

## L'undicesima sessione — 2026-08-09

### `item_data.hsp` è chiuso, e la classe era di nuovo nel sorgente

Le 235 voci rimaste non erano un residuo. La chiave qui non è `reftype` come
in `db_item.hsp` ma **l'array che dichiara la voce**, e con quella si sciolgono
in cinque discipline: `fishdatan` 113, `encDisp` 62, le dinamiche di
`*item_encdetail` 21, i due ego 29, `ammoname` 6. Tre lotti, nessun rinvio,
318 su 318.

### Il posto decide se i dati arrivano in tempo

`ioriginalnameref(ITEM_ID_FISH)` è la **stringa vuota**: il nome della specie
non è un pezzo del nome dell'oggetto, è tutto il nome, e arriva da
`itemNameSub` (`item_func.hsp:997`), che gira a riga 1936 — cioè **dopo** che
l'articolo è stato messo davanti e dopo che il plurale è stato scelto.

Tradurre i 113 nomi e basta avrebbe dato «a salmone». E **nessun test lo
avrebbe visto**: `verifica` non chiede plurale e genere a una voce che non
dichiara un array, e i pesci non lo dichiaravano.

> Prima di tradurre un nome si guarda **dove** il gioco lo mette. Il posto
> decide se i dati che porta arrivano in tempo.

I pesci usano ora la stessa macchina di `db_item` invece di una nuova:
`ARRAY_IN_LANG` in `estrai.py` riconosce la forma su una riga sola dentro
`lang()`, `ARTICOLO_DI` in `applica.py` fa dell'array dell'articolo una
proprietà della **famiglia** e non della riga, e `siti()` non riemette il nome
che il ciclo di `lang()` ha già visto — erano 113 sostituzioni doppie.

### Prima di scegliere la forma di una frase si contano i posti da cui esce

La descrizione d'incantamento (`s` di `*item_encdetail`) esce da **quattro
siti** e solo uno le mette un soggetto davanti — `command.hsp:16405` scrive
`lang("それは", "It ") + s`; gli altri tre la usano nuda. Un soggetto italiano
cablato lì andrebbe bene in un sito e male negli altri tre.

Le rese sono quindi **verbi alla terza persona senza soggetto**, e il prefisso
si spegne con una toppa a mano — `command.hsp` non è fra i file estratti.

### La stessa cura, tre cose ignote diverse

«Non accordarsi con ciò che non si conosce» ha scelto la forma tre volte in
questa sessione, e ogni volta l'ignoto era un altro:

| dove | cosa non si conosce |
|---|---|
| ego, `egominorn` | il genere dell'**oggetto** |
| `"deals X damage."` | il genere dell'**abilità**, che è pure ancora inglese |
| `skillencdesc` | il genere del **giocatore** — «ti rende letterato/letterata» |

### La `h` muta non rende pura la `s` impura

`articolo.py` teneva la `h` fra le vocali, perché a inizio di parola è muta e
chiede l'elisione («l'hotel»). Ma `_s_impura` interrogava lo stesso insieme
per una domanda **diversa** — «la lettera dopo la `s` è una consonante?» — e
per `sh` le due danno risposte opposte: usciva «un shuriken».

> Due domande che si somigliano non sono la stessa domanda. Il posto dove si
> separano è un caso solo, e lo trova il collaudo, non i test.

### Il giunto del materiale non è uno solo: sette elidono

« di » era cablato nella toppa, e lì deve restare — `command.hsp` legge
`mtname` nudo, e «fatto di» + «di cuoio» direbbe due volte la preposizione. Ma
una preposizione sola non copre 38 materiali: sette cominciano per vocale.
Terza via, quella già usata per plurale e articolo: `mtcomplemento`, un array
italiano accanto a quello inglese col complemento già montato.

### `skill.hsp`: solo le prime tre lettere arrivano a schermo

`chara.hsp:4679` fa `strmid(skillname(r), 0, 4 - (jp == 0))`: nella schermata
di razza e classe gli attributi sono **tagliati a 3 caratteri**.

Le scelte del glossario sopravvivono tutte — Vit, Man, For, Cos, Des, Per,
App, Vol, Mag, Car, Vel, undici distinte, e coincidono con le sigle già
fissate in `text.hsp:61`. La collisione che ci sarebbe (`Forza` e `Fortuna`
tagliano entrambe a «For») **non arriva a schermo**: il campo mostra
STR…SPD più Vita e Mana, e `Luck` non ci passa. Lo dice il sorgente stesso:
`MAX_SKILL_ATTR_BASIC 8 // this basically excludes luck and speed`.

⚠️ Vale per gli attributi, non per le 445 voci di `skillname`: il resto del
file va in altri campi, che vanno guardati prima di tradurlo.

### La misura dei campi di `skillname` — 2026-08-09

Fatta **prima** di tradurre, come per i pesci. Quattro campi, misurati sul
sorgente e non a occhio:

| campo | dove | larghezza | chi ci passa |
|---|---|---|---|
| tracciatore abilità (HUD) | `screen.hsp:2002` e `:2029` | **6 caratteri** | i 77 nomi tracciabili |
| razza e classe | `chara.hsp:4679`, `:4682`, `:4686` | **3 caratteri** | gli 11 attributi |
| lista abilità, nome | `command.hsp:5383` | ~**29 caratteri** | tutti i 445 |
| lista abilità, descrizione | `command.hsp:5389` | **34 caratteri** | i 415 `skilldesc` |

**Il 6 non è un numero a caso, è una misura.** Il nome sta a `pos 16` e il
valore a `pos 66`: cinquanta pixel, e il sorgente stesso assume 7 px per
carattere (`command.hsp:5385` fa `288 - strlen(s) * 7`). 50/7 = 7,14 — sei
caratteri con un carattere di margine.

Stessa aritmetica per la lista: nome a `wx+84`, costo allineato a destra a
`wx+288`, cioè 204 px ≈ 29 caratteri. L'inglese più lungo ne ha 24
(`Critical Particle Cannon`), quindi il margine c'è ma è sottile.

**I 34 caratteri della descrizione non sono un tetto da rispettare**: 41 delle
415 descrizioni inglesi lo superano già, e il gioco le tronca. È invece la
**finestra**: i primi 34 caratteri devono portare il senso.

#### Il vincolo che morde è il 6, e in inglese quasi non si vede

Fra i 77 nomi tracciabili le collisioni inglesi nei primi sei caratteri sono
**due**: `Magic`/`magic` (attributo e resistenza, distinte solo dal caso) e
`Magic Capacity`/`Magic Device`, che è una collisione vera già oggi.

In italiano il rischio è più alto, e per una ragione strutturale: **l'inglese
mette il qualificatore davanti, l'italiano dietro**, quindi la parte che
distingue esce dalla finestra. Le famiglie a rischio, trovate sul set vero:

| inglese | italiano naturale | primi 6 |
|---|---|---|
| Heavy / Medium / Light Armor | Armatura pesante / media / leggera | `Armatu` ×3 |
| Long / Short Sword | Spada lunga / corta | `Spada ` ×2 |
| Evasion / Greater Evasion | Evasione / Evasione superiore | `Evasio` ×2 |
| Throwing / Casting | Lancio / Lancio incantesimi | `Lancio` ×2 |

Da notare che l'italiano **risolve** l'unica collisione vera dell'inglese:
`Magic Capacity` e `Magic Device` diventano «Capacità magica» e «Dispositivi
magici», cioè `Capaci` e `Dispos`.

⚠️ **Decisione ancora aperta**, e va presa prima del lotto di `skillname`: se
scegliere teste diverse per le famiglie che collidono, abbreviare la testa, o
accettare la collisione nel solo tracciatore (dove il nome intero resta
visibile nella lista).

### I nove gradi di `_resist`: un campo che non tronca, invade — 2026-08-09

Trovato **in gioco**, non dai test: nella lista abilità (`a`, pagina delle
resistenze) «Resistenza debole» finiva sopra `Resist Fulmine`.

Il campo non è come quelli misurati finora. Gli altri **tagliano**, e il taglio
si vede nel campo stesso. Questo è **ancorato a destra**:

```
command.hsp:11002   pos wx + 280 - strlen(s) * 7, ...   ← la colonna dei gradi
command.hsp:10893   x = 54                              ← da dove parte il nome
```

> Un campo allineato a destra non ha un tetto: cresce verso sinistra finché
> non copre il vicino. **Il difetto non compare nel campo lungo, compare in
> quello accanto** — e nessun test che guardi una stringa alla volta lo vede.

Lo spazio fra i due estremi è **226 px**, e va diviso fra il nome e il grado.
Il caso peggiore è la coppia più lunga possibile, non la media: `Resist
Oltretomba` (17 caratteri, il nome più lungo dei nostri) col grado più lungo.
L'inglese nel suo peggiore ne impegna 30, `Resist Lightning` + `Criticaly Weak`.

Sette gradi su nove sforavano, e per la stessa ragione strutturale del campo da
6: **ripetevano una testa che la colonna non deve dire.** «Resistenza debole»
accanto a una riga che si chiama già `Resist Fulmine` dice «resistenza» due
volte. La cura è la stessa già usata per i nomi tracciabili — **togliere la
testa, tenere ciò che distingue**:

| jp | en | prima | ora |
|---|---|---|---|
| 致命的な弱点 | Criticaly Weak | Debolezza critica | **Fatale** |
| 弱点 | Weak | Debolezza | Debolezza |
| 耐性なし | No Resist | Nessuna resistenza | **Nessuna** |
| 弱い耐性 | Little | Resistenza debole | **Scarsa** |
| 普通の耐性 | Normal | Resistenza normale | **Normale** |
| 強い耐性 | Strong | Resistenza forte | **Forte** |
| 素晴らしい耐性 | Superb | Resistenza ottima | **Ottima** |
| 凄まじい耐性 | Amazing | Resistenza enorme | **Enorme** |
| 究極の耐性 | Supreme | Resistenza suprema | **Suprema** |

Il peggiore passa da 17 caratteri a **9**, e i nostri 17 + 9 = 26 stanno sotto
i 30 dell'inglese. Il 9 non è dedotto: la schermata di prima della correzione
mostrava già `Resist Oltretomba` con «Debolezza» **senza toccarsi**.

`Fatale` viene dal giapponese, 致命的 — più fedele di «critica», e in più
inequivocabile: un aggettivo da solo in una colonna di gradi si può leggere al
contrario, e «critica» poteva passare per un pregio.

⚠️ **I due gradi che si somigliano vanno tenuti distinti a vista.**
`Debolezza` (slot 1, si subisce il 133%) e `Scarsa` (slot 3, il 37%) sono
opposti. L'inglese li separa cambiando il sostantivo sottinteso a metà scala —
*Weak* è una debolezza, *Little* è una resistenza — e l'italiano deve fare lo
stesso: nome per la metà cattiva, aggettivo per quella buona.

Il secondo sito che legge `_resist` è `command.hsp:8136`, la scheda di un PNG
conosciuto (`_resist(...) + " " + skilldesc(...)`): testo che scorre, senza
vincolo di larghezza, e il grado corto ci sta come ci stava quello inglese.

⚠️ **Il `#####` accanto ai gradi non è nostro.** È `putenclv`
(`item_data.hsp:145`), disegnato a `wx+282` fisso: un `#` per livello di bonus,
`+` oltre il quinto. Esce identico nel gioco inglese.

### `skilldesc`, tutte e 415 — 2026-08-09

Un solo campo, la finestra da 34 caratteri di `command.hsp:5389`, ma **due
corpora diversi**, e trattarli allo stesso modo sarebbe stato l'errore:

| | quante | forma |
|---|---|---|
| prosa | **67** | `Indicates your skill with axes.` — frasi, termini già in glossario |
| etichette | **348** | `Line(Cold)`, `[100% Gauge] Rapid Slash`, `WIL-Check:Fatigue low-SP enemies` |

Le 348 non si traducono una per una: si traducono **gli atomi**, che stanno ora
in `glossario.md`. Tradurne una alla volta avrebbe prodotto quattordici rese
diverse di `Surround`.

#### Il riempitivo inglese non è contenuto

`Indicates your skill with…` compare **dodici volte** e non dice nulla: la
colonna si chiama già `Detail` e la riga porta già il nome dell'abilità.
Toglierlo fa entrare tutte e dodici nella finestra — `Indicates your skill with
blunt weapons.` (40) → «Abilità con le armi contundenti.» (32).

Il bilancio sulla finestra, che è la misura vera del lotto: **41 delle 415
inglesi la sforano**, delle nostre **cinque**, e quattro di quelle cinque sono
più corte del loro inglese.

#### Il giapponese scioglie le sigle che l'inglese lascia opache

`Con-Attack`, `END`, `PVDV`, `CHR` non sono spiegate da nessuna parte
nell'inglese. Il giapponese le dice tutte — 耐久属性攻撃, 耐久, 魅力 — e ha
mostrato **due sigle che sono la stessa cosa scritta due volte**:

| | inglese | giapponese | italiano |
|---|---|---|---|
| Costituzione | `CON` **e** `END` | 耐久 in entrambi | **Cos** |
| Carisma | `CHA` **e** `CHR` | 魅力 in entrambi | **Car** |

> Una sigla che l'inglese non scioglie va cercata nell'originale, non indovinata
> dal contesto. Due volte su quattro l'originale ha detto che le sigle erano una.

E ha corretto una scelta già fatta: `Surround(X)` è 範囲**攻撃**, «attacco ad
area». Avevo proposto `Attorno(X)` per tenere `Area` libera; con `AOE` che resta
sigla, `Area(X)` è insieme più fedele e più corto.

#### Chiavare sull'inglese avrebbe fuso sette voci distinte

Sette stringhe inglesi si ripetono con un **giapponese diverso**:

```
Create mist   →  濃い霧の発生    nebbia fitta
Create mist   →  眩い霧の発生    nebbia abbagliante
Teleport self →  瞬間移動        teletrasporto
Teleport self →  近くへの瞬間移動 teletrasporto vicino
```

Il lotto è quindi chiavato sull'**indice**, con l'inglese atteso accanto e
verificato a ogni voce. Una mappa `inglese → italiano` avrebbe silenziosamente
tradotto due cose diverse allo stesso modo — e nessuna guardia lo vedeva,
perché ogni firma sarebbe stata comunque tradotta.

#### Tre voci inglesi sono `?`

`skilldesc` 218, 263 e 355 dicono letteralmente `?`: buchi che l'autore inglese
non ha mai riempito. Il giapponese c'è ed è pieno (治癒力超上昇, 能力の変動・
暴れ回る, 煙幕＆能力転写). Sono rese **dal giapponese**: un `?` non è una
stringa da tradurre, è una che manca, e noi la fonte ce l'abbiamo.

#### L'accento a metà parola degrada male

Avevo scritto «dèi», che è la grafia giusta. `applica.py` degrada gli accenti in
apostrofo e ne esce **`de'i`**, con l'apostrofo dentro la parola. Tutti gli
accenti incontrati finora stavano a fine parola — «Abilità» → `Abilita'`, «più»
→ `piu'` — e lì la degradazione è invisibile.

> Prima di scrivere un accento, guardare **dove** cade nella parola. In fondo è
> gratis, in mezzo no.
