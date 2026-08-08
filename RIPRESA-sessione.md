# Ripresa sessione

Aggiornato: 2026-08-08, fine della nona sessione.

## La prima cosa da fare domani

**Il collaudo in gioco di tutto quel che è stato fatto oggi.** Sono sei blocchi
e nessuno è stato visto a schermo. Non è pigrizia: nessuno di essi si vede da un
negoziante qualsiasi, e servono posti diversi.

| cosa guardare | dove | cosa deve uscire |
|---|---|---|
| equipaggiamento (94 nomi) | **fabbro** | «uno scudo», «un elmo da cavaliere», «degli stivali corazzati» |
| cibo e pesci (48 nomi) | **negoziante di cibo**, pesca | «una capasanta», «un pesce sciabola», «delle patatine fritte» |
| qualità dell'arredo | **magazzino di casa** | «un tavolo moderno **di fattura scadente**», non «un shabby tavolo moderno» |
| taglia | un oggetto da **quest** | «… **di taglia enorme**», non «grown huge» |
| qualità del manoscritto | un **manoscritto** | «(sublime)» fra parentesi |
| libro prodotto | un **libro scritto dal giocatore** | «un libro sublime», e al plurale «2 libri sublimi» |

Il fabbro e il negoziante di cibo coprono i due lotti grossi e si fanno in
cinque minuti. Gli altri quattro sono rari e possono aspettare l'occasione.

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 291 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre
```

## Dove siamo

**Dodici commit oggi, tutti verdi, e per la prima volta il branch è pushato.**
`db_item.hsp` è passato dal 47% al 63% in una sessione.

- Branch `fase-0`, **allineato con `origin`** (`ae93f63`). Il conto esatto lo dà
  `git status -sb`, non questo documento
- [PR #1](https://github.com/oLdpZ/elona-cgx-traduzione-italiana/pull/1) sempre
  aperta verso `master`, mai unita
- Sorgente pinnato al tag `2.31.2.0` (`a9135a6`), manifesto 72/72
- **291 test** (erano 281), prova d'identità **72/72 byte per byte, 27.813
  sostituzioni**, **35 toppe** (7 a mano, 28 generate), 1.907 sostituzioni nella
  build, il compilatore non dice nulla

| file | tradotte | firme | % |
|---|---|---|---|
| `text.hsp` | 681 | 1.740 | 39% |
| `db_item.hsp` | **1.007** | 1.606 | **63%** |
| `item_data.hsp` | 83 | 318 | 26% |
| gli altri cinque | 0 | 4.948 | 0% |
| **totale** | **1.777** | **8.612** | **21%** |

Rinviate: **119** (erano 154).

## Le due cose imparate oggi, che valgono oltre oggi

### «Stessa forma» è un'ipotesi, non un fatto

Questo documento, ieri, dava `_furniture`, `_bookself`, `_weight` e
`_bookselfs` per «la stessa identica forma». Sono quattro array di aggettivi
prefissi in `text.hsp`: nel **dizionario** si somigliano. Nel **codice** no, e
hanno chiesto quattro cure diverse:

- `_furniture` — prefisso vero: toppa che lo sposta in `locvar_itemname_s6`;
- `_bookself` — esce **già fra parentesi**, dove la parola sta da sola:
  **nessuna toppa**, solo dato. L'unico caso in cui il sorgente andava bene;
- `_weight` — già suffisso, ma con giunto « grown ». La cura non è la posizione
  ma **il giunto**: « di taglia » introduce una testa femminile fissa, e
  l'accordo smette di dipendere dal genere dell'oggetto;
- `_bookselfs` — finisce nello **slot della parola-contatore**: vuole il
  trattamento di `contatori.jsonl`, non quello di `_furniture`.

**La regola: prima di scrivere la toppa si guarda il sito di concatenazione.**
La somiglianza nel dizionario non dice niente su dove il codice mette la
stringa. Vedi [[stessa-forma-va-verificata-nel-codice]].

### Il criterio della classe ha finito il suo lavoro

I lotti dal terzo al sesto sono stati scelti per `filter_item`, e ha funzionato
ogni volta: una classe raccoglie oggetti che pongono la **stessa domanda**.
Adesso in `db_item.hsp` restano **599 nomi, ed è esattamente il gruppo senza
filtro** — cioè un residuo, non una classe.

Dentro ci sono **169 artefatti fra `<>`**. Per quelli la domanda non è di resa
ma di **invarianza**: nome opaco (resta, e va in `invariati.md` con la sua
ragione) contro nome descrittivo (si traduce, come `<Abyss Princess>` →
«`<Principessa dell'Abisso>`»). È lavoro di decisione, e il criterio nuovo sarà
la **forma del nome**, non più il filtro.

## Il pezzo fragile costruito oggi

Fra `contatori.jsonl` e il dizionario il legame è **per stringa**: il `case`
dello switch confronta la resa del primo con quella che l'array porta a runtime,
che viene dal secondo. Se divergono il `case` non aggancia mai, e **restano
verdi sia il compilatore sia la prova d'identità**.

Ora lo pretendono `genera_toppe_nomi.py` (alla generazione) e un test (a ogni
giro). Chi tocca una delle sette rese di `_bookselfs` deve toccarle tutte e due
le volte.

## Il disegno dei nomi, in una riga

> Il **plurale** e il **genere** sono dati, perché l'italiano non li deduce.
> L'**articolo** no: è una derivata del genere, e la calcola `strumenti/articolo.py`.

I quattro generi sono `m`, `f`, `mp`, `fp`: il **numero fa parte del dato**.
Oggi è servito parecchio — «stivali», «guanti», «calzini» sono `mp`; «cesoie»,
«scarpe», «mutandine», «patatine fritte» sono `fp`.

⚠️ **Le parole-contatore cablate vincono sull'array dell'articolo**, al
contrario di quel che fanno col plurale: «un paio di stivali pesanti», non
«degli stivali pesanti».

⚠️ **`unicorn horn` ha genere `m` e plurale «corna di unicorno».** Non è
un'incoerenza: in italiano «corno» fa «corna» quando sono di un animale, ed è il
caso in cui i due campi del dizionario dicono davvero cose diverse.

## Cosa è stato costruito, in ordine

1. **`_furniture`** — 11 rese a complemento, una toppa a `item_func.hsp:1324`;
2. **`_weight` + `_bookself`** — 17 rese, una toppa **sul giunto**;
3. **`_bookselfs`** — 7 teste con singolare, plurale, genere e i `case` nei due
   switch; riallineata anche la scala del manoscritto, perché le due scale sono
   **la stessa scala** e due rese diverse si leggerebbero come due cose diverse;
4. **equipaggiamento** — 94 nomi (`/metal/`, `/sharp/`, `/soft/`) e la sezione
   «Armi e armature» del glossario;
5. **cibo, piante e pesci** — 48 nomi;
6. **tutte le classi dichiarate** — 108 nomi, undici filtri.

## Le lezioni di resa

**Dove l'italiano ha un nome vero, si usa quello.** `hotate` → «capasanta»,
`cutlassfish` → «pesce sciabola», `spotted garden eel` → «anguilla giardiniera».
E quando due pesci rischiano lo stesso nome si separano: `manboo` → «pesce
luna», `moonfish` → «pesce re».

**L'inglese si traduce, tranne quando è una svista.** `dog sister's diary` e
`cat sister's diary` traducono 姉の秘密の日記 e 妹の秘密の日記, cioè «il diario
**segreto** della sorella maggiore/minore». La resa letterale avrebbe dato
«diario della sorella cane». Qui si è derogato, e la deroga è dichiarata.

**Il verificatore che rifiuta il lotto intero è un pregio.** Ha bloccato
l'equipaggiamento finché i sette prestiti giapponesi non erano in
`invariati.md`. È la regola «si dichiara, non si evita» che morde invece di
lasciar passare.

**Un'immagine piccola non è una prova — seconda volta in due giorni.** Un «1 un
mucchio di bottiglie vuote» letto di fretta ha aperto un'indagine su un difetto
che non esisteva. Prima di dare la caccia, ingrandire.

Vedi [[dato-o-derivata]], [[plurale-e-un-dato-non-una-regola]],
[[toppe-generate-dal-sorgente]], [[genere-ignoto-si-risolve-col-complemento]]
e [[stessa-forma-va-verificata-nel-codice]].

## Cosa resta, in ordine

1. **il collaudo in gioco** dei sei blocchi di oggi (tabella in cima)
2. i **599 nomi** senza filtro di `db_item.hsp`, di cui **169 artefatti fra
   `<>`**: lavoro di decisione sull'invarianza, non di traduzione
3. le altre **235 voci** di `item_data.hsp`, mai guardate
4. le **119 voci rinviate** di `text.hsp`, di cui 30 sono il sistema dei nomi
   casuali — aggettivi condivisi fra sei classi di sostantivo di genere diverso
5. i nomi di **creatura** — lavoro **atomico** insieme ai 424 `evold`/`evname`
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
python -m strumenti.genera_toppe_nomi   # atteso: 28 generate, tutte «ok»
```

Legge anche `contatori.jsonl`: cambiare lì una resa o un genere e rilanciare
aggiorna singolare, plurale e articolo delle parole-contatore, **comprese le
sette di `_bookselfs`**, che però vanno cambiate anche nel dizionario.

## Per rifare la prova in gioco

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -Force
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

Il titolo mostra **2.31.1.0**: è la costante di versione che il tag non ha
aggiornato al rilascio, non un errore di build. Copia dei salvataggi in
`C:\Games\Elona\save-backup\`, più `pre-collaudo-20260808\` fatta oggi.

⚠️ **Il posto dove guardare è la lista di un negoziante**, non l'inventario:
serve vedere pile da due o più. Per l'arredamento serve invece il **magazzino di
casa**. Al primo avvio esce «Invalid screen resolution»: si dà OK e si prosegue.

### Il gioco si può pilotare da qui

Scoperto oggi, in `collaudo/schermo.ps1`. Serve quando il collaudo va fatto e
non c'è nessuno a giocare:

- la finestra si cattura con `CopyFromScreen` — **non** è DirectX esclusivo, la
  cattura funziona;
- i tasti si mandano con `keybd_event`, e il gioco li riceve;
- **le associazioni vere stanno in `sorgente/dist/2.05-custom-gx/original/config.txt`**,
  non nella documentazione: `key_interact` è `i`, non Invio. Leggerle lì è
  costato un minuto e ha evitato di tirare a indovinare;
- il personaggio si trova col **puntino blu della minimappa** in basso a
  sinistra: la pioggia animata rende inutile il confronto fra due fotogrammi.

⚠️ Pilotarlo è **lento**: ci vogliono molti giri per attraversare una città.
Conviene solo se non c'è alternativa.

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
[[stessa-forma-va-verificata-nel-codice]],
[[prova-identita-pipeline-trasformazione]] e [[cp932-perdite-silenziose]].
