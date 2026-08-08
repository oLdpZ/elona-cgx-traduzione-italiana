# Ripresa sessione

Aggiornato: 2026-08-08, fine della settima sessione.

## La prima cosa da fare domani

**Il secondo lotto di nomi di `db_item.hsp`.** Il primo è in gioco e la catena
regge; restano **1.520 nomi**. I prossimi per visibilità sono il cibo e le erbe
(mela, uva, carota, `tomato`…) e le pozioni e pergamene rimaste (`cure major
wound`, `restore body`, `teleport other`).

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 236 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre
python -m strumenti.estrai db_item.hsp --uscita lavoro/fase1-db_item-002.jsonl --da-tradurre --max 120
```

⚠️ **L'ordine del file non è l'ordine di visibilità.** I primi per riga sono gli
oggetti aggiunti da CGX (righe 133934+), che per vederli a schermo bisogna
andarseli a cercare; gli oggetti vanilla stanno in **coda** (151853→152820), ed è
da lì che è venuto il primo lotto. Il cibo sta intorno a 150085-150400.

Il lotto va tradotto su **due colonne**, `it` e `plurale`, e ora il cancello lo
pretende davvero. Le 43 parole-contatore sono in `contatori.jsonl` e non si
derogano.

## Dove siamo

**La catena dei nomi è in gioco e funziona**, vista a schermo in quattro
collaudi. Otto commit, tutti verdi.

- Branch `fase-0`, **34 commit avanti su origin**, niente pushato
- [PR #1](https://github.com/oLdpZ/elona-cgx-traduzione-italiana/pull/1) sempre
  aperta verso `master`, mai unita
- Sorgente pinnato al tag `2.31.2.0` (`a9135a6`), manifesto 72/72
- **236 test**, prova d'identità **72/72 byte per byte, 27.813 sostituzioni**,
  **32 toppe** (7 a mano, 25 generate), la build compila

| file | tradotte | firme | % |
|---|---|---|---|
| `text.hsp` | 646 | 1.740 | 37% |
| `db_item.hsp` | 86 | 1.606 | 5% |
| `item_data.hsp` | 83 | 318 | 26% |
| gli altri cinque | 0 | 4.948 | 0% |
| **totale** | **815** | **8.612** | **9%** |

## Cosa si legge a schermo adesso

```
2 pozioni di cura delle ferite lievi        6 pergamene di identificazione
8 bottiglie di juice                        7 carichi di traveler's food
un mantello leggero di platino con benedizione
una freccia di vetro                        un paio di stivali pesanti di cuoio
```

## I quattro difetti chiusi, in ordine di scoperta

**1. `verifica.py` non guardava il campo `plurale`** (`770df34`). Un lotto con
`it` pieno e `plurale` vuoto passava senza un fiato. Ora è preteso su ogni nome
tradotto, coi tre controlli di carattere del singolare.

**2. Le tre toppe della concatenazione avevano perso una guardia** (`e6694a7`).
Il pluralizzatore inglese spento era protetto da `locvar_itemname_s2 == ""`: si
flette la parola-contatore **oppure** il nome, mai tutti e due. Senza, «3
pergamene di identificazion**i**».

**3. `rinviate.jsonl` era indicizzato per firma, e la firma non porta il file**
(`7d2f48f`). 15 nomi di `db_item.hsp` sparivano da **ogni** lotto perché una
decisione presa su `text.hsp` glieli toglieva. Si vedeva solo dal fatto che
`verifica` ne contava 1.606 ed `estrai` ne offriva 1.591.

**4. Gli array del plurale sono sparsi e non erano dimensionati** (`fdf0c6a`).
`Array overflow`, crash aprendo la lista di un negoziante. L'autoespansione di
`sdim` vale **in scrittura**, non in lettura.

## Cosa è stato costruito

- **86 nomi** di `db_item.hsp`, scelti per visibilità (la coda del file, cioè il
  corredo vanilla) invece che per ordine di riga
- **le sei parole-contatore cablate** in `item_func.hsp` (`bottle`, `cup` ×2,
  `cargo`, `pair`, `dish`): non stanno in `db_item.hsp` e non passano da
  `lang()`, e il loro plurale inglese lo faceva il pluralizzatore che avevamo
  spento — era una **regressione**, non un pezzo mancante
- **i 38 materiali, i 38 epiteti e le 7 piante** di `item_data.hsp`, con
  l'ordine spostato: il materiale segue il nome
- **benedizione, maledizione e dannazione** come complementi in coda

## Le lezioni, che valgono più del codice

**Il giunto sta nel codice, il dato resta nudo.** Imparata due volte: sul
`" of "` dei nomi composti, e sul materiale — `command.hsp:16289` dice «It is
made of » + `mtname(...)`, quindi col «di» cotto nel dato uscirebbe «fatto di di
cuoio».

**Il genere ignoto si risolve sempre allo stesso modo: complemento o
sostantivo.** Quattro volte ormai — etichette di stato, qualità dell'oggetto,
epiteti del materiale, benedizione. Un aggettivo anteposto a un oggetto di
genere sconosciuto non si può scegliere.

**Un array sparso si dimensiona.** L'autoespansione vale in scrittura. La
sparsità era il disegno (il ripiego sul singolare esiste apposta), quindi era
prevedibile leggendo.

**Il denominatore si misura sul sorgente, mai sull'uscita di uno strumento che
filtra.** Il numero sbagliato in `avanzamento.md` portava dentro il difetto che
avrebbe dovuto segnalare.

**Un rinvio con un motivo scritto si può riaprire quando il motivo scade.**
`blessed` era rinviata «finché i nomi di `db_item.hsp` non si risolvono»: quella
premessa è caduta, e il motivo scritto ha permesso di accorgersene.

Vedi [[plurale-e-un-dato-non-una-regola]], [[toppe-generate-dal-sorgente]] e
[[genere-ignoto-si-risolve-col-complemento]].

## Cosa resta, in ordine

1. i **1.520 nomi** restanti di `db_item.hsp`, a lotti
2. **l'articolo inglese** `a`/`an`/`the` (`item_func.hsp:1809-1821`), l'ultima
   parola inglese su *ogni* oggetto. Nota buffa che conferma il sito: sceglie
   già «**an** arco lungo» leggendo la prima lettera della stringa **italiana**
3. le **154 voci rinviate** di `text.hsp`, di cui 30 sono il sistema dei nomi
   casuali — aggettivi condivisi fra sei classi di sostantivo di genere diverso,
   «pozione chiara» ma «anello chiaro»
4. le altre **235 voci** di `item_data.hsp`, mai guardate
5. `_bookselfs` (7 valori), che finisce nella parola-contatore
6. i nomi di **creatura** — lavoro **atomico** insieme ai 424 `evold`/`evname`
   di `action.hsp`, mai prima e mai dopo (§5 di `contratto-nomi.md`)

## Il prezzo dei nomi di creatura — da non dimenticare

`db_creature.hsp` fa `cdatan(CDATAN_NAME, rc) = lang(…)`: **scrive i nomi nel
salvataggio**. Sono la stessa classe di `CDATAN_NEWSEX`, e sono ciò contro cui
si confrontano i **424 `evold`/`evname`** di `action.hsp`. Vanno tradotti nello
stesso momento di quelli, o il confronto fallisce **in silenzio**.

## Cosa rifare a ogni giro

**La prova d'identità**, che attraversa tutti i 27.813 siti e non dipende da
quali casi qualcuno si è ricordato di coprire.

```powershell
python -m strumenti.prova_identita     # atteso: 72/72, 27.813, ambigue 0
```

⚠️ **Non giudica le toppe**, che girano dopo in un giro loro. Il loro guardiano
è la regola «esiste esatto e una volta sola», più il compilatore, **più il
collaudo in gioco** — e oggi il collaudo ha preso un crash che nessun test
poteva prendere.

**Il generatore delle toppe** è il primo comando da rilanciare quando arriva una
versione CGX nuova:

```powershell
python -m strumenti.genera_toppe_nomi   # atteso: 25 generate, tutte «ok»
```

Se upstream ha riscritto uno dei blocchi lo dice lì, invece che alla build. Il
controllo di unicità ha già cambiato la forma di quattro toppe invece di lasciar
passare un'ambiguità.

## Per rifare la prova in gioco

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -Force
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

Il titolo mostra **2.31.1.0**: è la costante di versione che il tag non ha
aggiornato al rilascio, non un errore di build. Copia dei salvataggi in
`C:\Games\Elona\save-backup\`.

⚠️ **Il posto dove guardare è la lista di un negoziante**, non l'inventario:
serve vedere pile da due o più, ed è lì che il plurale, il materiale e il crash
si sono manifestati. Al primo avvio esce «Invalid screen resolution»: si dà OK e
si prosegue.

## Cosa deve esistere fuori dal repo

| percorso | come ottenerlo |
|---|---|
| `C:\Games\Elona\_traduzione\hsp34\` | `hsp34a.zip` da <https://www.onionsoft.net/hsp/file/hsp34a.zip>, estratto **specificando CP932 per i nomi delle voci** |
| `C:\Games\Elona\_traduzione\sorgente\` | `git clone --depth 1 --branch 2.31.2.0 https://github.com/JianmengYu/ElonaPlusCustom-GX.git sorgente` — **il tag, non il branch `work`** |
| `C:\Games\Elona\_traduzione\manifesto-sorgente.txt` | SHA-256 dei 72 `.hsp`. ⚠️ **gli hash sono in MAIUSCOLO**: confrontarli case-sensitive dà 0/72 e sembra un disastro |
| `C:\Games\Elona\elonaplus2.31\` | il gioco installato |

I percorsi si ridefiniscono con `ELONA_IT_LAVORO`, `ELONA_IT_GIOCO` e
`ELONA_IT_DIZIONARIO`.

⚠️ **`git status` dentro `sorgente\` è permanentemente sporco.** Per l'integrità
si usa il manifesto, mai `git status`. Vedi `SPEC.md` §2.

Vedi [[terminologia-prima-del-testo]], [[larghezza-per-campo]],
[[stringhe-che-sono-dati]], [[toppe-fuori-dal-dizionario]],
[[plurale-e-un-dato-non-una-regola]], [[toppe-generate-dal-sorgente]],
[[genere-ignoto-si-risolve-col-complemento]],
[[prova-identita-pipeline-trasformazione]] e [[cp932-perdite-silenziose]].
