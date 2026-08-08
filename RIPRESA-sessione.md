# Ripresa sessione

Aggiornato: 2026-08-08, fine dell'ottava sessione.

## La prima cosa da fare domani

**Gli 11 aggettivi di `_furniture`** (`text.hsp:56`): `shabby`, `comfy`,
`royal`, `masterpiece`… Sono l'ultima cosa brutta che si legge, e adesso si
legge peggio di prima: da quando l'articolo è italiano escono frasi come «**un**
shabby tavolo moderno». Non è una regressione — prima era «a shabby tavolo
moderno» — ma è il pezzo col miglior rapporto fra fatica e resa.

Sono **prefissi a un nome di genere ignoto**, cioè esattamente la forma già
chiusa due volte: materiale ed epiteti (2026-08-08 mattina),
`blessed`/`cursed`/`doomed` (stessa mattina). La cura è la stessa: **una toppa
che li sposta in coda** con `locvar_itemname_s6`/`s7`, e la traduzione come
complemento o aggettivo posposto. Il sito è `item_func.hsp:1324`, dentro il ramo
`if ( en )`, e le voci stanno in `rinviate.jsonl` col loro motivo.

Dopo quelli, in ordine: `_bookself`/`_bookselfs` (14 voci) e `_weight` (10), che
sono la stessa identica forma.

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 281 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre
```

## Dove siamo

**La catena dei nomi è completa**: nome, plurale, genere, articolo. Quattro
commit oggi, tutti verdi, `db_item.hsp` è passato dal 5% al 47% in una sessione.

- Branch `fase-0`, **4 commit avanti su origin**, niente pushato
- [PR #1](https://github.com/oLdpZ/elona-cgx-traduzione-italiana/pull/1) sempre
  aperta verso `master`, mai unita
- Sorgente pinnato al tag `2.31.2.0` (`a9135a6`), manifesto 72/72
- **281 test** (erano 236), prova d'identità **72/72 byte per byte, 27.813
  sostituzioni**, **33 toppe** (7 a mano, 26 generate), la build compila

| file | tradotte | firme | % |
|---|---|---|---|
| `text.hsp` | 646 | 1.740 | 37% |
| `db_item.hsp` | **756** | 1.606 | **47%** |
| `item_data.hsp` | 83 | 318 | 26% |
| gli altri cinque | 0 | 4.948 | 0% |
| **totale** | **1.485** | **8.612** | **17%** |

## Cosa si legge a schermo adesso

```
una pozione di cura delle ferite lievi      6 pergamene di identificazione
un grimorio di dardo caotico                una pozione superiore di calamità
un atto di nave da guerra                   uno scudo da cavaliere
un mucchio di bottiglie vuote               un paio di stivali pesanti
```

⚠️ Le due righe verificate **a schermo** sono quelle dei nomi e del plurale
(collaudo delle 10:53). **L'articolo e i 252 composti sono compilati ma non
ancora visti in gioco**: il collaudo è la prima cosa da fare, prima di
`_furniture`.

## Il disegno dei nomi, in una riga

> Il **plurale** e il **genere** sono dati, perché l'italiano non li deduce.
> L'**articolo** no: è una derivata del genere, e la calcola `strumenti/articolo.py`.

Chiedere l'articolo a chi traduce sarebbe raddoppiare le occasioni di sbagliare,
e nessun controllo se ne accorgerebbe — «un scudo» è una stringa valida quanto
«uno scudo». Il genere invece ha quattro valori leciti e `verifica.py` li
pretende. Vedi [[dato-o-derivata]].

I quattro valori sono `m`, `f`, `mp`, `fp`: il **numero fa parte del dato**,
perché «cianfrusaglie», «attrezzi» e «armi» esistono solo al plurale e su quelli
l'articolo indeterminativo non c'è — ci vuole il partitivo, che è ciò che
l'inglese sbaglia già oggi scrivendo «a goods».

⚠️ **Le parole-contatore cablate vincono sull'array dell'articolo**, al
contrario di quel che fanno col plurale. Quando `itemname()` mette «paio»
davanti al nome la testa del sintagma diventa quella: «un paio di stivali
pesanti», non «uno stivali pesanti».

## Cosa è stato costruito, in ordine

1. **166 nomi**, il resto del corredo vanilla (righe 150006-151839): cibo, erbe,
   arredamento della casa, bacchette, grimori, pozioni;
2. **la colonna `genere`** nel dizionario, `strumenti/articolo.py` con le regole
   dell'elisione, due array HSP nuovi e la toppa che li legge; riempite a
   ritroso le 252 voci già tradotte;
3. **i 252 oggetti composti** (504 firme), cioè la lista di un negoziante per
   intero.

## Le lezioni

**L'euristica della regione è più debole di quella della classe.** Avevo scelto
il secondo lotto per zona di file — «il corredo vanilla sta in coda» — e la
lista del negoziante l'ha smentito: `restore body`, `speed`, `beer`, `molotov`
sono roba vanilla di tutti i giorni e stanno **sopra** riga 150000, in mezzo agli
oggetti aggiunti da CGX. Il criterio buono è la **classe dell'oggetto**, ed è
per questo che il terzo lotto è stato «tutti i composti».

**Il termbase si guarda prima di tradurre, non dopo.** Due rese del secondo
lotto — `lot` e `variety` — deviavano da `contatori.jsonl` senza che me ne
accorgessi. La correzione non è stata allineare il lotto ma **cambiare il
termbase**, che è la regola scritta in testa a `glossario.md`: «se una resa non
funziona si cambia qui, non si deroga nel lotto».

**Un nome opaco può collidere con una parola comune italiana, ed è successo due
volte in un giorno**: `api nut` → «noce di **A**pi» (minuscolo sarebbe gli
insetti) e la divinità `Mani` (minuscolo sarebbe le mani). La maiuscola non è
decorativa, è ciò che tiene distinti i due sensi.

**Quando l'inglese distingue e il giapponese no, si tiene la distinzione.**
`magical map` e `magic mapping` hanno lo stesso giapponese 魔法の地図 e nomi
inglesi diversi: «mappa magica» e «cartografia magica». Si traduce dall'inglese.

**Il giunto sta nel codice, il dato resta nudo — terza applicazione.** Il giunto
dei composti è cablato a «di», quindi «tomba ornata di fiori» si ottiene
spostando il participio sulla **testa** (`ioriginalnameref2` = «tomba ornata»),
non arricchendo il complemento.

**Un'immagine piccola non è una prova.** Ho letto «6 pergamena» in uno
screenshot e ho aperto un'indagine su una regressione che non esisteva:
ingrandendo, diceva «6 pergamene». Prima di dare la caccia a un difetto, ingrandire.

Vedi [[dato-o-derivata]], [[plurale-e-un-dato-non-una-regola]],
[[toppe-generate-dal-sorgente]] e [[genere-ignoto-si-risolve-col-complemento]].

## Cosa resta, in ordine

1. **il collaudo in gioco** di articolo e composti, mai visti a schermo
2. gli **11 `_furniture`** più `_bookself` (14) e `_weight` (10): stessa forma,
   una toppa che li sposta in coda
3. gli **850 nomi** restanti di `db_item.hsp`, ormai quasi tutti oggetti semplici
   aggiunti da CGX
4. le altre **235 voci** di `item_data.hsp`, mai guardate
5. le **154 voci rinviate** di `text.hsp`, di cui 30 sono il sistema dei nomi
   casuali — aggettivi condivisi fra sei classi di sostantivo di genere diverso
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
collaudo in gioco**.

**Il generatore delle toppe** è il primo comando da rilanciare quando arriva una
versione CGX nuova:

```powershell
python -m strumenti.genera_toppe_nomi   # atteso: 26 generate, tutte «ok»
```

Legge anche `contatori.jsonl`: cambiare lì una resa o un genere e rilanciare
aggiorna singolare, plurale e articolo delle sei parole-contatore cablate.

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
serve vedere pile da due o più. Per l'arredamento serve invece il **magazzino di
casa**. Al primo avvio esce «Invalid screen resolution»: si dà OK e si prosegue.

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
[[dato-o-derivata]], [[plurale-e-un-dato-non-una-regola]],
[[toppe-generate-dal-sorgente]], [[genere-ignoto-si-risolve-col-complemento]],
[[prova-identita-pipeline-trasformazione]] e [[cp932-perdite-silenziose]].
