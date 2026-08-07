# Ripresa sessione

Aggiornato: 2026-08-07, fine della sesta sessione.

## La prima cosa da fare domani

**Il primo lotto di nomi di `db_item.hsp`, e subito dopo il collaudo in gioco.**

La catena dei nomi è finita e nessuno l'ha ancora esercitata davvero: senza
traduzioni il gioco gira sui **rami di ripiego** delle otto toppe nuove, cioè
sul singolare. Il primo lotto è anche il primo vero collaudo di quel codice.

Il lotto va tradotto su **due colonne**, non una: `it` e `plurale`. Le rese delle
43 parole-contatore sono già decise in `contatori.jsonl` e vanno rispettate
(`scroll` → pergamena/pergamene, `pair` → paio/**paia**).

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 212 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre
python -m strumenti.estrai db_item.hsp --uscita lotti/db_item-001.jsonl --da-tradurre --max 250
```

⚠️ **`verifica.py` non guarda ancora il campo `plurale`.** Un lotto con `it`
pieno e `plurale` vuoto passa senza un fiato. È il primo buco da chiudere, ed è
lo stesso difetto di forma che questo progetto ha già corretto due volte:
una difesa che non copre un campo nuovo tace invece di parlare.

## Dove siamo

**La catena dei nomi è chiusa, dalla scansione fino al gioco.** Quattro commit
oggi, tutti verdi. Il Task 7 di `text.hsp` è fermo dov'era: la sessione è andata
tutta sui nomi, che erano la premessa.

- Branch `fase-0`, **22 commit avanti su origin**, niente pushato
- [PR #1](https://github.com/oLdpZ/elona-cgx-traduzione-italiana/pull/1) sempre
  aperta verso `master`, mai unita
- Sorgente pinnato al tag `2.31.2.0` (`a9135a6`), manifesto **72/72 concordi**
- **212 test**, prova d'identità **72/72 byte per byte, 27.813 sostituzioni**,
  **15 toppe**, la build compila

| file | tradotte | firme | % |
|---|---|---|---|
| `text.hsp` | 643 | 1.740 | 37% |
| `db_item.hsp` | 0 | 1.591 | 0% |
| gli altri cinque | 0 | 4.948 | 0% |

La percentuale totale è **scesa dal 10% all'8%** e nessuno ha disfatto niente:
il denominatore era incompleto di 1.591 firme. Una metrica che scende perché ha
smesso di mentire è una metrica migliore.

## Cosa è stato costruito, in ordine

**1. Il secondo tipo di sito** (`499b772`). `siti()` non scandisce più solo
`lang()`: riconosce le sette righe di `if ( jp ) … else …` di `db_item.hsp`. Il
riconoscimento è tollerante sull'indentazione e **severo sulla struttura** —
pretende l'ordine delle righe e lo stesso identificatore in tutte e quattro le
assegnazioni — così i 1.581 `if ( jp )` che non sono nomi non si agganciano. La
prova d'identità è passata da 26.206 a 27.813 sostituzioni: esattamente i 1.607
siti nuovi, senza toccarne uno dei vecchi.

**2. Le toppe imparano il blocco** (`1c8bf4d`). `cerca` e `sostituisci`
accettano una lista di righe consecutive, di lunghezza anche diversa. Le
garanzie valgono per il blocco intero: se non esiste più, o se compare due
volte, la catena si ferma.

**3. Il plurale diventa un dato** (`09791b5`). Le voci dei nomi portano
`plurale`, `array`, `oggetto`; `applica_plurali` scrive la riga gemella accanto
al singolare in due array nuovi.

**4. Le otto toppe della composizione** (`f0a4149`), generate da
`strumenti/genera_toppe_nomi.py`.

## Le due lezioni che valgono più del codice

**Il plurale non si deduce, e si flette dove si compone.** L'inglese appiccica
la `s` in fondo alla stringa composta perché il sostantivo testa sta alla fine;
in italiano sta **in mezzo**. Al punto in cui il codice inglese pluralizzava,
`locvar_itemowner_s` era già `«maledetta spada lunga di ferro <Distruttore>»`.
La flessione va fatta **dove il nome si concatena**, e lì i siti apparenti erano
sei ma tre erano morti: due dentro blocchi `/* ORIGINAL */` in commento, uno nel
ramo `jp`. I vivi: `item_func.hsp:1731, 1747, 1770`.

**Le toppe si generano dal sorgente.** `cerca` è una fetta del file vero, e lo
strumento rifiuta di emettere una toppa il cui blocco non compaia **esattamente
una volta**. Ha già impedito un errore: la riga che spegne il pluralizzatore
inglese compare **due volte**, perché upstream tiene l'originale in commento
poco sopra. È ripetibile — marca le sue toppe con `"generata": "nomi"` — ed è
**il primo comando da rilanciare** quando arriverà una nuova versione CGX.

Vedi [[plurale-e-un-dato-non-una-regola]] e [[toppe-generate-dal-sorgente]].

## L'ordine dei passaggi, che non è libero

`applica_plurali` prende **due** testi, e il motivo è che i due vincoli tirano in
direzioni opposte:

- **prima** dell'inserimento, perché le righe aggiunte spezzano la forma
  canonica a sette righe e i nomi non verrebbero più riconosciuti;
- **dopo** la sostituzione, perché i siti si cercano per firma e nel tradotto la
  firma non c'è più: l'inglese è diventato italiano.

Quindi le firme si leggono dal **sorgente** e le righe si inseriscono nel
**tradotto**. Se i due testi hanno un numero di righe diverso, la catena si
ferma.

## Cosa resta, in ordine

1. `verifica.py` deve guardare il campo `plurale` (vedi l'avvertenza sopra)
2. i **1.591 nomi** con i loro plurali, a lotti — e il collaudo in gioco presto
3. `_bookselfs` (7 valori in `text.hsp`, oggi rinviati) finisce nella
   parola-contatore: senza traduzione ripiega, ma è un buco noto
4. le **157 voci rinviate** di `text.hsp`, che i nomi sbloccano
5. i nomi di **creatura** — lavoro **atomico** insieme ai 424 `evold`/`evname`
   di `action.hsp`, mai prima e mai dopo (vedi §5 di `contratto-nomi.md`)

## Il prezzo dei nomi di creatura — da non dimenticare

`db_creature.hsp` fa `cdatan(CDATAN_NAME, rc) = lang(…)`: **scrive i nomi nel
salvataggio**. Sono la stessa classe di `CDATAN_NEWSEX`, e sono ciò contro cui
si confrontano i **424 `evold`/`evname`** di `action.hsp`. Vanno tradotti nello
stesso momento di quelli, o il confronto fallisce **in silenzio**.

## Una cosa che si sblocca da sola

`command.hsp:4880` confronta il nome dell'oggetto con **quello che il giocatore
digita** — è il sistema dei desideri (bacchetta e libro del desiderio). Non è un
problema: nome e input si muovono insieme, quindi tradurre i nomi localizza
anche i desideri.

## I meccanismi, e cosa protegge cosa

| file | cosa dichiara | chi lo legge |
|---|---|---|
| `glossario.md` | rese vincolanti + la regola dei nomi propri | umani |
| `contatori.jsonl` | le 43 parole-contatore, resa e plurale | umani (per ora) |
| `invariati.md` | stringhe che restano inglesi, per sezione classificata | `verifica.py` |
| `rinviate.jsonl` | voci rinviate, con motivo obbligatorio | `estrai --da-tradurre` |
| `toppe.jsonl` | sostituzioni fuori dal dizionario (15: 7 a mano, 8 generate) | `applica.py` |
| `avanzamento.md` | firme tradotte per file, e i rinvii | umani |
| `contratto-nomi.md` | dove stanno i nomi, come si compongono, e il plurale | umani |

## Cosa rifare a ogni giro

**La prova d'identità**, che attraversa tutti i 27.813 siti e non dipende da
quali casi qualcuno si è ricordato di coprire.

```powershell
python -m strumenti.prova_identita     # atteso: 72/72, 27.813, ambigue 0
```

⚠️ **Non giudica le toppe.** Attraversa solo il percorso del dizionario: le
toppe girano dopo, in un giro loro. Il loro guardiano è la regola «esiste
esatto e una volta sola», più il compilatore, più il collaudo in gioco.

E non prende le **stringhe-dato**: lì la forma resta giusta ed è il significato
che si rompe. La ricerca da fare prima di un file nuovo è in `avanzamento.md`;
su `db_item.hsp` è già stata fatta, e ha trovato le tre cose scritte sopra.

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

Artefatto atteso dello stato intermedio: **«colpisces»** nei messaggi di
mischia. Sparisce con `action.hsp`.

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
[[prova-identita-pipeline-trasformazione]] e [[cp932-perdite-silenziose]].
