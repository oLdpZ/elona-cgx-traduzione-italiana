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
