# Ripresa sessione

Aggiornato: 2026-08-07, fine della quarta sessione.

## La prima cosa da fare domani

**Decidere i sei termini aperti di `glossario.md`**, sezione «Da decidere». Sono
lessico, non codice: nessuno può prenderli al posto tuo, e ogni lotto del Task 7
che li contiene resta bloccato finché non sono chiusi.

| termine | occorrenze | il nodo |
|---|---|---|
| Skill | 98 | «Abilità» collide con l'uso italiano di *ability* |
| Gauge | 75 | la barra delle mosse speciali. «Indicatore» è lungo, «Carica» collide con `Charge` |
| Body | 57 | parte anatomica, slot d'equipaggiamento e sigla convivono |
| Chaos | 54 | è insieme elemento (`Chaos`) e nome proprio (`Fort of Chaos <Beast>`) |
| Sister | 37 | quasi sempre dentro nomi di missione (`H Sister`) |
| Abyss | 33 | «Abisso» regge per il luogo, meno per la risorsa (`abyss power`) |

Restano aperti anche i cinque nomi di luogo nella sezione «Da decidere nel
glossario» di `invariati.md`: Larna, Port Kapul, Cyber Dome, Arcbelc, Lesimas.
`Port Kapul` è quello che decide la regola per tutti: `Porto Kapul` o invariato.

Poi il **Task 7**: i lotti restanti di `text.hsp` (1.690 stringhe ancora da
tradurre) e `avanzamento.md`.

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 163 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 26.206, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre
```

## Dove siamo

**La Fase 1 è arrivata a schermo.** Le prime 50 stringhe di `text.hsp` sono
tradotte, compilate e **viste in gioco** il 2026-08-07: le accentate si leggono
`e'`, «il viandante» funziona, nessuna riga esce dal riquadro. Il rischio numero
uno del progetto — la degradazione CP932 — non è più un'ipotesi verificata sui
byte: è un fatto osservato.

- Branch `fase-0`, **163 test verdi**
- [PR #1](https://github.com/oLdpZ/elona-cgx-traduzione-italiana/pull/1) verso `master`, **ancora non unita**
- `dizionario/`: `text.hsp` 50 voci, `init.hsp` 6 voci
- Sorgente pinnato al tag `2.31.2.0` (`a9135a6`)

| task Fase 1 | stato |
|---|---|
| 1 — funzioni grammaticali inglesi | chiuso |
| 2 — sostituzione dentro `cnvtalk(`/`cnven(` | **chiuso**: re-revisione fatta, un fratello del difetto trovato e corretto |
| 3 — `invariati.md` | **chiuso** |
| 4 — `verifica --dizionario` | **chiuso** |
| 5 — glossario e guida di stile | **chiuso** |
| 6 — primo lotto + collaudo a schermo | **chiuso** |
| 7 — i lotti restanti e `avanzamento.md` | **tuo**, non iniziato |

## La scoperta che ha cambiato il piano

**`init.hsp` è una premessa della Fase 1, non lavoro di Fase 4.**

Il piano dava per acquisito che qui il «tu» fosse sicuro, «perché le righe del
giocatore e quelle dei PNG sono chiamate `lang()` diverse». Il sorgente dice il
contrario: `name()` (`init.hsp:1699`) risolve **da sé** chi è il soggetto —
`lang("あなた", "you")` per il giocatore, `"the " + nome` per un PNG. Una sola
`lang()` serve entrambi, esattamente come il `#1` di Elin.

Misurato sui sei file di Fase 1: 1.522 dinamiche, **901 con `name()`**, **472
(31%) con un marcatore di morfologia inglese**, cioè dimostrabilmente condivise.

Decisione: **terza persona singolare presente indicativo**, l'unica forma senza
accordo di genere. `you` → **«il viandante»**, `he`/`she` → «lui»/«lei». Sei voci
di dizionario, 16 sostituzioni. È la stessa conclusione a cui Elin era arrivata
dopo averlo visto a schermo — qui è arrivata prima, leggendo il codice.

## Due trappole trovate, entrambe silenziose

**1. Le stringhe che sono dati.** Le otto di `CDATAN_NEWSEX` (`male`, `female`,
`none`, `hermaphrodite`, `male?`, `female?`, `trans-male`, `trans-female`) stanno
nella *stessa funzione* dei pronomi appena tradotti e sembrano testo. Non lo
sono: `chara.hsp:2790` e `4390` le **scrivono** nei dati del personaggio,
`init.hsp:1813-1823` le rilegge come **operandi di confronto**, e i dati finiscono
nel salvataggio. Tradurle romperebbe il genere di ogni personaggio già creato —
vanificando in silenzio proprio ciò che il cancello della Fase 0 aveva
verificato. Sono in `invariati.md`, sezione «valori di dato, non testo».
Vedi [[stringhe-che-sono-dati]].

**Prima di tradurre un file nuovo, fai questa ricerca:**

```
grep -nE '(=|==|!=|instr\().*lang\(' <file>.hsp
```

**2. L'accoppiamento della toppa.** `custom_dmgpop.hsp:224-231` *legge* la
stringa `"the "` che la toppa toglie da `init.hsp:1718`. È protetto da
`instr(...) != -1`, quindi diventa un no-op — verificato, non sperato.

## Il meccanismo nuovo: `toppe.jsonl`

Le sostituzioni **fuori da `lang()`**, che il dizionario non raggiunge. Sul
sorgente intero sono dieci, in quattro file; oggi ce n'è una sola:
`init.hsp:1718` toglie l'articolo inglese davanti ai nomi dei PNG.

Non è un fork: come il dizionario, sono dati esterni applicati all'albero di
build. Verificato col manifesto dopo la build, 72/72 hash concordi. Le toppe
hanno un giro proprio e **la prova d'identità non ci passa**, quindi la garanzia
byte per byte resta intatta. Vedi [[toppe-fuori-dal-dizionario]].

**La conseguenza è una decisione di Fase 2:** l'articolo lo porterà il nome della
creatura in `db_creature.hsp` («il putit», «lo gnomo», «l'orco»). Vale per *ogni*
uso di `cdatan()`, non solo per `name()`: prima di tradurre quel file va guardato
dove altro quei nomi compaiono — elenchi, negozi — perché lì l'articolo potrebbe
non starci bene.

## Cosa deve esistere fuori dal repo

Niente di tutto questo è versionato: va ricreato se manca.

| percorso | come ottenerlo |
|---|---|
| `C:\Games\Elona\_traduzione\hsp34\` | `hsp34a.zip` da <https://www.onionsoft.net/hsp/file/hsp34a.zip>, estratto **specificando CP932 per i nomi delle voci** — `Expand-Archive` corrompe i nomi giapponesi e fallisce |
| `C:\Games\Elona\_traduzione\sorgente\` | `git clone --depth 1 --branch 2.31.2.0 https://github.com/JianmengYu/ElonaPlusCustom-GX.git sorgente` — **il tag, non il branch `work`** |
| `C:\Games\Elona\_traduzione\manifesto-sorgente.txt` | SHA-256 dei 72 `.hsp` di `2.05-custom-gx\`, una riga `HASH  nome.hsp` per file |
| `C:\Games\Elona\elonaplus2.31\` | il gioco installato |

I percorsi si ridefiniscono con `ELONA_IT_LAVORO`, `ELONA_IT_GIOCO` e
`ELONA_IT_DIZIONARIO`.

⚠️ **`git status` dentro `sorgente\` è permanentemente sporco.** Non è una
scrittura nostra: vedi `SPEC.md` §2. Per l'integrità usa il manifesto, mai
`git status`.

## Per rifare la prova in gioco

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -Force
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

Il titolo mostra **2.31.1.0**, non 2.31.2.0: è la costante di versione che il tag
non ha aggiornato al rilascio, non un errore di build.

**Per far uscire una stringa accentata a comando:** prova a raccogliere un
oggetto di qualcun altro in una casa. `text.hsp:27` è un `txt` a tre varianti
sorteggiate, e una sola porta l'accento — `Non e' roba tua.` Riprova finché non
esce quella. *(Il pozzo non serve: `Ah, che bonta' l'acqua fresca.` è dietro
`osakana == 100`, che si accende solo con la Mug of Ehekatl in inventario.)*

Copia dei salvataggi di prima della prima prova: `C:\Games\Elona\save-backup\`.

## Cosa rifare a ogni giro

**La prova d'identità.** Un dizionario che traduce ogni stringa in sé stessa deve
riprodurre i file byte per byte: attraversa tutti i 26.206 siti, e non dipende da
quali casi qualcuno si è ricordato di coprire.

```powershell
python -m strumenti.prova_identita     # atteso: 72/72, 26.206, ambigue 0
```

Il contatore delle ambigue va guardato lo stesso: se risalisse senza che nessuno
abbia toccato niente, qualcosa è cambiato a monte.

**Ma non prende tutto.** Le stringhe-dato del paragrafo sopra le attraversa senza
accorgersene: lì la forma resta giusta ed è il significato che si rompe. Contro
quelle serve la lettura, e la lista scritta in `invariati.md`.

Vedi [[prova-identita-pipeline-trasformazione]] e [[cp932-perdite-silenziose]].
