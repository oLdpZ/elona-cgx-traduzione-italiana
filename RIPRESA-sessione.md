# Ripresa sessione

Aggiornato: 2026-08-09, fine della decima sessione.

## La prima cosa da fare domani

**Il collaudo in gioco di `db_item.hsp`**, che oggi è arrivato al 100% e di cui
non si è visto a schermo quasi niente. Il gioco è già pronto:
`C:\Games\Elona\elonaplus2.31\cgx-test.exe` è la build di stasera.

| cosa guardare | dove | cosa deve uscire |
|---|---|---|
| arredamento, 146 nomi | **magazzino di casa** | «un tavolo moderno **di fattura scadente**», «una toeletta pregiata», «un letto matrimoniale» |
| nomi composti | magazzino, cimitero | «**tomba ornata di fiori**», «atto dell'accampamento» — il giunto è « di » e il plurale viene dal dizionario |
| attrezzi, 107 nomi | **negoziante generico**, fabbro | «una canna da pesca», «un sacco a pelo», «un kit di pronto soccorso» |
| cibo, 51 nomi | **negoziante di cibo** | «una polpetta di riso», «della carne secca», «un uovo» → al plurale «2 uova» |
| artefatti | un artefatto qualsiasi | «`<Mantello dell'Eroe>`» tradotto, «`<Turahagi>`» invariato |

⚠️ **Il posto dove guardare è la lista di un negoziante**, non l'inventario:
serve vedere pile da due o più. Per l'arredamento serve il **magazzino di casa**.

I sei blocchi della nona sessione sono già stati collaudati stamattina e sono
usciti tutti giusti.

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 297 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre
python -m strumenti.categorie              # atteso: 0 voci ancora da tradurre
```

## Dove siamo

**`db_item.hsp` è il primo file completo del progetto**: 1.605 firme su 1.606.
La mancante è `<Pants of Ogre>`, **rinviata** alla Fase 2 e non dimenticata.

Dieci commit oggi, tutti verdi, **tutti pushati**. Branch `fase-0` allineato con
`origin` (`55a3f02`), [PR #1](https://github.com/oLdpZ/elona-cgx-traduzione-italiana/pull/1)
sempre aperta verso `master`. Sorgente pinnato al tag `2.31.2.0`, manifesto 72/72.

| file | tradotte | firme | % |
|---|---|---|---|
| `text.hsp` | 681 | 1.740 | 39% |
| `db_item.hsp` | **1.605** | 1.606 | **100%** |
| `item_data.hsp` | 83 | 318 | 26% |
| gli altri cinque | 0 | 4.948 | 0% |
| **totale** | **2.369** | **8.612** | **28%** |

**297 test** (erano 291), prova d'identità **72/72 byte per byte, 27.813
sostituzioni**, **2.505 sostituzioni nella build** (erano 1.907), il compilatore
non dice nulla. Rinviate: **120**. Righe in `invariati.md`: **289**.

## La cosa imparata oggi che vale più di tutte

### Il residuo non esisteva

Ieri questo documento diceva che `db_item.hsp` aveva 599 nomi «senza filtro», un
**residuo** da affrontare a occhio, e che il criterio nuovo sarebbe stata «la
forma del nome». La forma del nome è servita per i 169 artefatti. Gli altri 430
li ha sciolti una cosa che era lì da sempre:

```
if ( dbid == ITEM_ID_HAMBURGER ) {
    ...
    reftype = FILTER_ITEM_FOOD
```

**Ogni oggetto dichiara la propria categoria dentro il proprio blocco.** Sono
1.320 oggetti classificati dal sorgente, e con quella chiave il residuo torna a
essere fatto di classi. Cinque lotti su sei sono usciti da lì.

> **Prima di dichiarare che una cosa non ha struttura, si cerca dove il codice
> la struttura.**

Lo strumento è `strumenti/categorie.py`, con cinque test:

```powershell
python -m strumenti.categorie
python -m strumenti.categorie --categoria FILTER_ITEM_TOOL --uscita lavoro/x.jsonl
```

⚠️ **Non è stato ancora usato sugli altri file.** `item_data.hsp` ha 235 voci e i
cinque file mai guardati ne hanno 4.948: nessuno di loro è stato letto con questa
chiave. È la prima cosa da provare prima di decidere come tagliarli.

## Le altre tre, più corte

### La marca 《》 decide l'invarianza degli artefatti

Per i 169 nomi fra `<>` la domanda non era di resa ma di invarianza. La regola,
in tre gradini di precedenza:

1. l'inglese è **romanizzazione, coniazione o sigla** → invariato;
2. il giapponese è fra 《》 **e traslitterato** → invariato;
3. il giapponese è **descrittivo in kanji**, o non porta la marca → tradotto.

Il pezzo nuovo è la marca 《》, e viene dai dati: 157 su 169 ce l'hanno, e i
dodici che non ce l'hanno sono esattamente quelli che si leggono come oggetti
ordinari (`<Dog Whistle>` 犬笛). La regola **riproduce tutti e otto i precedenti
già presi**, ed è questa la prova che non è stata cucita addosso al lotto.

Esito: 105 invariati, 63 tradotti, 1 rinviato.

### Il registro dice il termine, il dizionario dice il segmento

`contatori.jsonl` registra `grave` → «tomba», il dizionario rende lo stesso
`grave` con «tomba ornata». Sembrava una divergenza; non lo è, e a dirlo è il
**sito di concatenazione**.

Il nome si monta `s2 + " " + s3 + " " + s1`, e la toppa 3 fissa il giunto a «di».
Le due parti sono «tomba ornata» e «fiori» → **«tomba ornata di fiori»**.
L'aggettivo sta in `s2` perché **è lì che può accordarsi con la testa**: con
«tomba» in `s2` uscirebbe «tomba di ornata di fiori».

Il test nuovo pretende quindi che la resa del dizionario **cominci con** il
termine del registro — non che sia uguale. Copre 39 teste che prima non guardava
nessuno.

### Una procura non è una proprietà

`test_i_nomi_di_db_item_non_sono_rinviati_da_text` asseriva `== set()`: vero
solo finché `db_item.hsp` non aveva rinvii suoi. Col primo rinvio legittimo è
caduto **senza che la proprietà difesa fosse violata**.

> Quando un test cade, la prima domanda è se sia caduta la proprietà o la
> procura.

## Cosa resta, in ordine

1. **il collaudo in gioco** di oggi (tabella in cima)
2. **`item_data.hsp`**, 235 voci mai guardate — provare prima `categorie.py`
3. le **119 voci rinviate** di `text.hsp`, di cui 30 sono il sistema dei nomi
   casuali
4. i nomi di **creatura** — lavoro **atomico** insieme ai 424 `evold`/`evname`
   di `action.hsp`, mai prima e mai dopo (§5 di `contratto-nomi.md`)

## Il prezzo dei nomi di creatura — da non dimenticare

`db_creature.hsp` fa `cdatan(CDATAN_NAME, rc) = lang(…)`: **scrive i nomi nel
salvataggio**. Sono la stessa classe di `CDATAN_NEWSEX`, e sono ciò contro cui si
confrontano i **424 `evold`/`evname`** di `action.hsp`. Vanno tradotti nello
stesso momento di quelli, o il confronto fallisce **in silenzio**.

⚠️ Da oggi c'è un vincolo in più, piccolo ma reale: `<Pants of Ogre>` aspetta
quella decisione. In `db_creature.hsp` **`orc` e `ogre` convivono** (`orc
warrior`, `black orc` contro `slash ogre`, `shine ogre`), quindi «orco» non può
coprirle entrambe.

## Il disegno dei nomi, in una riga

> Il **plurale** e il **genere** sono dati, perché l'italiano non li deduce.
> L'**articolo** no: è una derivata del genere, e la calcola `strumenti/articolo.py`.

I quattro generi sono `m`, `f`, `mp`, `fp`: il **numero fa parte del dato**.

⚠️ **Le parole-contatore cablate vincono sull'articolo dell'array**: «un paio di
stivali pesanti», non «degli stivali pesanti».

⚠️ **I due campi possono dire cose diverse, ed è voluto.** `unicorn horn` è `m`
con plurale «corna»; `bone` è `m` con «ossa»; `egg` è `m` con «uova».

## Cosa rifare a ogni giro

**La prova d'identità**, che attraversa tutti i 27.813 siti e non dipende da
quali casi qualcuno si è ricordato di coprire.

```powershell
python -m strumenti.prova_identita     # atteso: 72/72, 27.813, ambigue 0
```

⚠️ **Non giudica le toppe**, che girano dopo in un giro loro. Il loro guardiano è
la regola «esiste esatto e una volta sola», più il compilatore, **più il collaudo
in gioco**.

**Il generatore delle toppe** è il primo comando da rilanciare quando arriva una
versione CGX nuova:

```powershell
python -m strumenti.genera_toppe_nomi   # atteso: 28 generate, tutte «ok»
```

## Per rifare la prova in gioco

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -Force
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

⚠️ **La copia fallisce con «Device or resource busy» se il gioco è aperto.**
Chiuderlo prima.

Il titolo mostra **2.31.1.0**: è la costante di versione che il tag non ha
aggiornato al rilascio, non un errore di build. Al primo avvio esce «Invalid
screen resolution»: si dà OK e si prosegue.

### Il personaggio che cammina da solo — risolto il 2026-08-09

Sintomo: in gioco il personaggio si muoveva **da solo verso nord-est**, e solo
con Elona. Non era la build.

`config.txt` del gioco aveva `joypad. "1"`, e nella macchina ci sono un pad
Bluetooth associato e **due bus che creano pad virtuali** (Nefarius ViGEm,
Virtual Desktop). Un pad che appare per un attimo con lo stick fuori centro
basta: Elona interroga il joystick alla vecchia maniera, i giochi moderni no —
da qui il «solo con Elona».

**Cura: `joypad. "0"` in `C:\Games\Elona\elonaplus2.31\config.txt`.** Backup in
`config.txt.bak-prima-joypad0`. La modifica è di **un solo byte**, verificata col
diff.

⚠️ La diagnosi per esclusione è stata utile e va rifatta così: `joyGetPosEx` su
tutti e 16 gli ID dice se un pad si presenta **adesso**; se dice
`JOYERR_UNPLUGGED` ovunque il joystick non è la causa *in quel momento*, ma
`joypad. "1"` lascia comunque la porta aperta a un pad che compaia dopo.

### Il gioco si può pilotare da qui

`collaudo/schermo.ps1`. Serve quando il collaudo va fatto e non c'è nessuno a
giocare: cattura con `CopyFromScreen`, tasti con `keybd_event`, associazioni
vere in `sorgente/dist/2.05-custom-gx/original/config.txt` (`key_interact` è `i`).

⚠️ È **lento**, e l'utente preferisce una lista di passi da eseguire lui.
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
[[la-categoria-che-il-sorgente-dichiara]], [[registro-e-segmento]],
[[una-procura-non-e-una-proprieta]],
[[prova-identita-pipeline-trasformazione]] e [[cp932-perdite-silenziose]].
