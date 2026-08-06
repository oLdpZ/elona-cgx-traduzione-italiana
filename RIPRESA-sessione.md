# Ripresa sessione

Aggiornato: 2026-08-06, fine della prima sessione.

## Dove siamo

Fase 0 eseguita per la parte automatizzabile. **Il cancello vero non è ancora
passato**: quella che c'è è una *catena verificata*, non un *gioco verificato*.

- Branch `fase-0`, 18 commit, **83 test verdi**
- [PR #1](https://github.com/oLdpZ/elona-cgx-traduzione-italiana/pull/1) aperta verso `master`, non ancora unita
- `dizionario/` è **vuoto**: nessuna stringa è ancora tradotta

## Per riprendere da un altro terminale

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
git fetch origin
git checkout fase-0
git pull
python -m pytest strumenti/tests -q     # atteso: 83 passed
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
| `C:\Games\Elona\_traduzione\sorgente\` | `git clone --depth 1 --branch work https://github.com/JianmengYu/ElonaPlusCustom-GX.git` |
| `C:\Games\Elona\_traduzione\manifesto-sorgente.txt` | manifesto SHA-256 dei 72 `.hsp`, ricetta nel piano di Fase 0, Task 7 passo 5 |
| `C:\Games\Elona\elonaplus2.31\` | il gioco installato |

I percorsi si ridefiniscono con `ELONA_IT_LAVORO`, `ELONA_IT_GIOCO` e
`ELONA_IT_DIZIONARIO`.

⚠️ **`git status` dentro `sorgente\` è permanentemente sporco** (1198 file su un
clone intatto). Non è una scrittura nostra: vedi `SPEC.md` §2. Per l'integrità
usa il manifesto, mai `git status`.

## Il prossimo passo, e blocca tutto il resto

**Provare a ricompilare l'eseguibile da sorgente non modificato.** Richiede la
GUI, quindi va fatto a mano:

1. avviare `C:\Games\Elona\_traduzione\hsp34\hsed3.exe`
2. aprire `C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\main.hsp`
3. premere `Ctrl+F9`

Atteso: viene prodotto `elonapluscgx.exe` in `2.05-custom-gx\`, si avvia e mostra
il titolo `Elona+ Custom-GX 2.31.2.0`.

Se compare un errore di compilazione **il progetto si ferma lì**, e non c'è
codice che possa aggirarlo. È per questo che è il primo task del piano.

Prima di lanciarlo, copiare `hsplua.dll` dal sorgente nella cartella dell'SDK,
altrimenti il gioco non parte dall'editor:

```powershell
Copy-Item "C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\hsplua.dll" "C:\Games\Elona\_traduzione\hsp34\hsplua.dll"
```

## La decisione che ha una finestra, e si chiude

**Se la firma delle dinamiche debba includere l'espressione.** Oggi
`firma = sha1(giapponese + NUL + inglese)` usa i soli letterali, e **77 firme
collidono** su espressioni diverse: la traduzione di una porterebbe all'altra le
variabili sbagliate.

Includere `en_grezzo` risolve la collisione ma rende la chiave fragile: qualunque
ritocco all'espressione a monte, anche rinominare una variabile, manderebbe la
stringa in coda di ritraduzione a testo invariato.

**Va decisa finché `dizionario/` è vuoto.** Dopo la prima ondata di traduzioni
costa una migrazione. Il ragionamento completo è in `decisioni.md`.

## Da mettere nel piano della Fase 1

In quest'ordine — l'elenco completo con le motivazioni è in `decisioni.md`:

1. sostituzione dentro `cnvtalk(` / `cnven(` — bloccante per la Fase 2, ma sono
   due sole forme su 3.499 occorrenze: poche righe
2. la decisione sulla firma, §3.2
3. spostare a monte il rilevamento dei casi rifiutati: oggi il traduttore lo
   scopre solo a build abortito
4. la whitelist `invariati.md`, che `SPEC.md` §7 promette e che non esiste
5. `verifica --dizionario`, la coda di ritraduzione su cui `SPEC.md` §3.1 fonda
   l'intera architettura

## Cosa rifare a ogni giro

**La prova d'identità.** Un dizionario che traduce ogni stringa in sé stessa
deve riprodurre i file byte per byte. Non dipende da quali casi qualcuno si è
ricordato di coprire: attraversa tutti i 26.434 siti. Ha trovato i due difetti
peggiori del progetto quando 83 test erano verdi.

Vedi [[prova-identita-pipeline-trasformazione]] e [[cp932-perdite-silenziose]].
