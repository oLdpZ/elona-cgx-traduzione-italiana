# Ripresa sessione

Aggiornato: 2026-08-06, seconda sessione.

## Dove siamo

**Il cancello della Fase 0 è passato.** Il sorgente non modificato ricompila e
l'eseguibile che ne esce si avvia. Resta da provare a mano una cosa sola di quel
cancello: che carichi un salvataggio.

- Branch `fase-0`, **106 test verdi**
- [PR #1](https://github.com/oLdpZ/elona-cgx-traduzione-italiana/pull/1) aperta verso `master`, non ancora unita
- `dizionario/` è **vuoto**: nessuna stringa è ancora tradotta
- Sorgente **pinnato al tag `2.31.2.0`** (`a9135a6`), non più alla testa di `work`

## Per riprendere da un altro terminale

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
git fetch origin; git checkout fase-0; git pull
python -m pytest strumenti/tests -q          # atteso: 106 passed
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

## Il prossimo passo

**Provare in gioco che l'eseguibile ricompilato carichi un salvataggio.** È
l'ultimo pezzo manuale del cancello, e nessun codice lo può sostituire.

```powershell
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe"
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

Il titolo mostrerà **2.31.1.0**, non 2.31.2.0: è la costante di versione che il
tag non ha aggiornato al rilascio, non un errore di build. Il dettaglio è in
`decisioni.md`.

Se un salvataggio esistente non si carica, il problema è il disallineamento fra
l'exe ricompilato dal tag e i dati della 2.31.2.0 installata — e va risolto prima
di tradurre, non dopo.

## La decisione che ha una finestra, e si chiude

**Se la firma delle dinamiche debba includere l'espressione.** Oggi
`firma = sha1(giapponese + NUL + inglese)` usa i soli letterali, e **77 firme
collidono** su espressioni diverse: la traduzione di una porterebbe all'altra le
variabili sbagliate.

Includere `en_grezzo` risolve la collisione ma rende la chiave fragile: qualunque
ritocco all'espressione a monte, anche rinominare una variabile, manderebbe la
stringa in coda di ritraduzione a testo invariato.

**Va decisa finché `dizionario/` è vuoto.** Il ragionamento completo è in
`decisioni.md`.

## Da mettere nel piano della Fase 1

In quest'ordine — l'elenco completo con le motivazioni è in `decisioni.md`:

1. sostituzione dentro `cnvtalk(` / `cnven(` — bloccante per la Fase 2, ma sono
   due sole forme: poche righe
2. la decisione sulla firma, §3.2
3. spostare a monte il rilevamento dei casi rifiutati: oggi il traduttore lo
   scopre solo a build abortito
4. la whitelist `invariati.md`, che `SPEC.md` §7 promette e che non esiste
5. `verifica --dizionario`, la coda di ritraduzione su cui `SPEC.md` §3.1 fonda
   l'intera architettura

## Cosa rifare a ogni giro

**La prova d'identità**, che ora è un comando e non più una procedura a mano:

```powershell
python -m strumenti.prova_identita     # atteso: 72/72 byte per byte
```

Un dizionario che traduce ogni stringa in sé stessa deve riprodurre i file byte
per byte. Non dipende da quali casi qualcuno si è ricordato di coprire: attraversa
tutti i 26.206 siti. Ha trovato i due difetti peggiori del progetto quando 83 test
erano verdi. Sul sorgente pinnato: **72/72**, 22.414 sostituzioni, con 3.465
statiche avvolte e 327 firme collidenti escluse per costruzione — sono le due
classi che `applica.py` rifiuta, e i loro conteggi vanno guardati: se calano senza
che nessuno abbia implementato niente, la prova sta misurando meno.

Ora ha un seguito naturale: **ricompilare dopo la prova d'identità**. Se i file
identici producono anche un `.ax` identico, la prova si estende dal testo al
bytecode. È il primo esperimento da fare in Fase 1.

Vedi [[prova-identita-pipeline-trasformazione]] e [[cp932-perdite-silenziose]].
