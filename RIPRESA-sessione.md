# Ripresa sessione

Aggiornato: 2026-08-07, fine della terza sessione.

## La prima cosa da fare domani

**La re-revisione mirata della correzione `dfe530b`.** È l'unico passo saltato
alla chiusura: il codice è committato e verificato dai numeri, ma nessun revisore
ha letto quel diff.

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q      # atteso: 138 passed, 2 skipped
python -m strumenti.prova_identita       # atteso: 72/72, 26.206, ambigue 0
```

Il diff da rivedere è `38a6d7e..dfe530b`, e il rilievo che chiudeva è: `_AVVOLTA`
accettava `cnvtalk("x", "y")` e la ricostruzione ne avrebbe fatto sparire il
secondo argomento. Cosa verificare: che il controllo guardi la virgola di **primo
livello** (`cnvtalk("a, b")` è legittimo e deve continuare a passare) e che
`_analizza_involucro` sia davvero condiviso fra `riscrivi_statica` e il messaggio
d'errore, così che non possano disallinearsi.

Poi restano i **Task 3 e 4** del piano, entrambi non iniziati.

## Dove siamo

**Il cancello della Fase 0 è passato per intero.** Il sorgente non modificato
ricompila, l'eseguibile che ne esce si avvia e **carica un salvataggio
esistente** — provato in gioco il 2026-08-06. Non è più una catena verificata: è
un gioco verificato, e la Fase 1 può cominciare.

- Branch `fase-0`, **138 test verdi** (140 col cancello acceso)
- [PR #1](https://github.com/oLdpZ/elona-cgx-traduzione-italiana/pull/1) aperta verso `master`, non ancora unita
- `dizionario/` è **vuoto**: nessuna stringa è ancora tradotta
- Sorgente **pinnato al tag `2.31.2.0`** (`a9135a6`), non più alla testa di `work`

## Per riprendere da un altro terminale

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
git fetch origin; git checkout fase-0; git pull
python -m pytest strumenti/tests -q          # atteso: 138 passed
python -m strumenti.compila --cancello       # atteso: #No error detected.
```

Se il repo non c'è ancora su quella macchina:

```powershell
git clone https://github.com/oLdpZ/elona-cgx-traduzione-italiana.git
```

### Cosa deve esistere fuori dal repo

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

🗑️ `C:\Games\Elona\_traduzione\sorgente-work-2.32-obsoleto\` è il vecchio clone
sulla testa di `work`, tenuto solo per confronto. Si può cancellare.

## La Fase 1 è cominciata

Il piano è `piani/2026-08-06-fase-1-ui-e-messaggi.md`, sette task. Si esegue con
un subagente per task e una revisione dopo ciascuno; il registro di avanzamento
sta in `.superpowers/sdd/2026-08-06-fase-1-ui-e-messaggi/progress.md` (non
versionato, è scratch).

| task | stato |
|---|---|
| 1 — le funzioni grammaticali inglesi | **chiuso**, 1 giro di correzione |
| 2 — sostituzione dentro `cnvtalk(`/`cnven(` | codice fatto, **manca la re-revisione** di `dfe530b` |
| 3 — `invariati.md` e la regola «identica all'inglese» | non iniziato |
| 4 — `verifica --dizionario` | non iniziato |
| 5 — glossario e guida di stile | **tuo**: vuole le tue scelte lessicali |
| 6 — primo lotto di 50 stringhe + collaudo a schermo | **tuo** |
| 7 — i lotti restanti | **tuo** |

I documenti di partenza per il Task 5 esistono già nel progetto gemello
[[Elin - Traduzione Italiana]]: si eredita quello che è di universo (i nomi del
canone Elona), non quello che è di motore (i segnaposto `#1`, i tag Unity).

Per rifare la prova in gioco quando serve:

```powershell
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe"
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

Il titolo mostra **2.31.1.0**, non 2.31.2.0: è la costante di versione che il tag
non ha aggiornato al rilascio, non un errore di build. Il dettaglio è in
`decisioni.md`.

Copia dei salvataggi di prima della prima prova: `C:\Games\Elona\save-backup\`.

## La decisione che aveva una finestra: chiusa

**La firma delle dinamiche include l'espressione**, con gli spazi normalizzati;
le statiche restano com'erano. Decisa e implementata il 2026-08-06, finché
`dizionario/` era ancora vuoto: nessun debito di migrazione.

Le 77 firme collidenti non esistono più. Prezzo misurato: +235 stringhe da
tradurre, 324 occorrenze che erano irraggiungibili tornano traducibili. Il
ragionamento completo è in `decisioni.md`.

## L'elenco di `decisioni.md`, aggiornato

1. ~~sostituzione dentro `cnvtalk(` / `cnven(`~~ — **fatta** (Task 2). Ha sciolto
   anche le 3 firme ambigue residue, come previsto
2. ~~la decisione sulla firma, §3.2~~ — **fatta**
3. ~~spostare a monte il rilevamento delle statiche avvolte~~ — **decaduta**: dal
   momento in cui si sostituiscono, non c'è più niente da segnalare a monte. Va
   tolta da `decisioni.md` alla chiusura della fase
4. la whitelist `invariati.md`, che `SPEC.md` §7 promette e che non esiste — è il
   **Task 3** del piano
5. `verifica --dizionario`, la coda di ritraduzione su cui `SPEC.md` §3.1 fonda
   l'intera architettura — è il **Task 4**

## Cosa rifare a ogni giro

**La prova d'identità**, che ora è un comando e non più una procedura a mano:

```powershell
python -m strumenti.prova_identita     # atteso: 72/72, 26.206 sostituzioni
```

Un dizionario che traduce ogni stringa in sé stessa deve riprodurre i file byte
per byte. Non dipende da quali casi qualcuno si è ricordato di coprire: attraversa
tutti i 26.206 siti. Ha trovato i due difetti peggiori del progetto quando 83 test
erano verdi. Sul sorgente pinnato: **72/72**, **26.206 sostituzioni**, **0 firme
ambigue**. Le statiche avvolte non sono piu' escluse: da quando `applica.py`
prende l'involucro dal sito, la prova le attraversa tutte — e' piu' forte di
prima, non piu' debole. Il contatore delle ambigue va guardato lo stesso: se
risalisse senza che nessuno abbia toccato niente, qualcosa e' cambiato a monte.

Ora ha un seguito naturale: **ricompilare dopo la prova d'identità**. Se i file
identici producono anche un `.ax` identico, la prova si estende dal testo al
bytecode. È il primo esperimento da fare in Fase 1.

Vedi [[prova-identita-pipeline-trasformazione]] e [[cp932-perdite-silenziose]].
