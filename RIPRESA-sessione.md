# Ripresa sessione

Aggiornato: 2026-08-10, fine della ventesima sessione.

## La prima cosa da fare

**`action.hsp` è chiuso.** Il prossimo file è **`text.hsp`**, che è a **780
firme su 1.740 (45%)**: restano **960 firme**, e si prendono **per zona di
riga**, col metodo qui sotto.

⚠️ **Restano non provate in gioco le rinomine all'evoluzione dei nemici.**
Verificate meccanicamente nella sessione scorsa: 249 `evold` su 250 combaciano
con un nome che possono davvero incontrare, e la sola rotta — `<Gwen>` — è
riparata. La prova a schermo serve ormai solo a confermare l'innesco. Vedi «Per
rifare la prova in gioco».

### Le quattro verifiche d'apertura

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 344 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 320, doppie 0, senza razza 0
```

I test sono **344**, non più 343: uno nuovo, `test_la_deroga_all_evname_vale_per_una_riga_sola`,
che tiene ferma l'unica deroga della guardia sulle rinomine.

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.606 | 1.606 | **100%** |
| `item_data.hsp` | 318 | 318 | **100%** |
| `skill.hsp` | 885 | 885 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `action.hsp` | 1.286 | 1.288 | **100%** (le 2 mancanti sono rinviate a toppa) |
| `text.hsp` | 780 | 1.740 | 45% |
| gli altri tre | 0 | 2.775 | 0% |
| **totale Fase 1** | **4.887** | **8.624** | **57%** |

Fuori dalla Fase 1: `db_creature.hsp` a 1.452 su 3.655;
`custom_enemyevolution.hsp` **chiuso**; `ai.hsp` 6 su 100; `event.hsp` 5 su
654; `chara_func.hsp` 45 su 331; `init.hsp` 0 su 133.

**344 test**, prova d'identità **72/72 e 27.813**, **8.682 sostituzioni**, il
compilatore non dice nulla.

## Le due righe di `action.hsp` che non si traducono

Sono decisioni, non arretrato, e **vanno scartate a mano quando si compone un
lotto** se un giorno si torna su questo file (`estrai --da-tradurre` le toglie
già lui, ma il conto delle non tradotte le porta per sempre).

- **`:4584`** — l'articolo inglese davanti al nome di un'arma unica. Toppa.
- **`:9631`** — `his(tc, 1)`, il possessivo che in italiano si omette. Toppa.
  ⚠️ **Il testo di una toppa non passa da `degrada` e non può portare accenti**:
  è per questo che la resa è «ha cambiato elemento» e non «ha cambiato affinità
  elementale». Il dettaglio in `decisioni.md`.

## Il metodo

**I lotti si prendono per zona di riga**, non separando statiche e dinamiche.

```powershell
python -m strumenti.estrai text.hsp --da-tradurre --uscita lavoro/_r.jsonl
# si ordina per (riga, occorrenza) e si prendono le prime ~50
python -m strumenti.verifica lavoro/<lotto>.jsonl
python -m strumenti.reimporta lavoro/<lotto>.jsonl
python -m pytest strumenti/tests -q
python -m strumenti.prova_identita
python -m strumenti.genera_toppe_nomi
python -m strumenti.genera_toppe_casuali
```

⚠️ **Una riga può portare più voci, e la riga da sola non è una chiave.**
`action.hsp:11442` ha quattro grida sulla stessa riga, e **due hanno lo stesso
inglese** (`Transform!`) con giapponesi diversi. Chi scrive il lotto deve
indicizzare per **(riga, giapponese)**, altrimenti ne perde tre su quattro senza
accorgersene. Non è ambiguo per `applica`, che aggancia la coppia `lang()`
intera.

## Le regole di resa, aggiornate

Valgono le precedenti — terza persona sempre; mai `_s()`, `is()`, `was()`,
`your()`, `have()`, `does()`, `yourself()`; mai una preposizione davanti a
`name()` o `itemname()`, mentre `con`, `per`, `tra`, `sopra`, `dentro` e
`contro` reggono; la preposizione sta nel valore, non nella frase; invarianza di
genere prima di tutto; un nome di abilità o di oggetto si copia, non si traduce.

⚠️ **`his(x)` a un argomento si può togliere, `his(x, 1)` no.** Il primo è
morfologia inglese, il secondo passa da `lang()`. La guardia lo sa e distingue.

Tre aggiunte di questa sessione:

- **Quando il valore interpolato ha genere variabile, la frase rinuncia
  all'articolo.** `_seikaku()` dà nomi astratti di generi misti («Allegria»,
  «Coraggio») e `bodyn()` dà parti del corpo di generi misti: si scrive «ha
  scoperto di avere Allegria» e «ha una parte nuova: Mano!». I due punti
  prendono il posto dell'articolo.
- **L'invarianza di genere costa una parola, non una perifrasi.** «prende
  fuoco» invece di «è avvolto dalle fiamme»; «Quella creatura è già appesa»
  invece di «È già appeso», dove il genere lo fissa il nome comune aggiunto. Per
  gli insulti rivolti al giocatore c'è una parola che li risolve quasi tutti:
  **«idiota»**, invariante.
- **Una `statica` si scrive nuda.** Il suo `it` è testo, non espressione:
  incapsularlo fra virgolette come si fa con le dinamiche fa fallire `verifica`
  su sedici voci in un colpo. E dentro una statica le virgolette sono le
  tipografiche `“”`.

## Le cose da non riscoprire

### Aggiungere una funzione che l'inglese non aveva non si può

`verifica` confronta l'elenco delle interpolazioni. Si possono **togliere** le
morfologiche (`_s`, `your`, `is`, `was`, `its2`, `_s2`, `is2`), non se ne
possono **aggiungere**: un `cnvtalk()` messo per far parlare qualcuno che in
inglese non parlava fa fallire il lotto.

### La frase di combattimento vive in due file

`action.hsp` scrive «… e» e imposta `gdata(GDATA_DMG_TYPE) = 2`;
`chara_func.hsp:6323` legge il flag e stampa il resto con `txtcontinue`, che
sopprime la maiuscola (`init.hsp:1663`). `init.hsp:1666` aggiunge già lo spazio
fra due messaggi: **la giuntura non va spaziata a mano**.

### Le stringhe che sembrano testo e sono codice

`EN` (`action.hsp:4816`) è la chiave con cui il gioco cerca `%txtName,EN` nei
file `user\item\plan*.txt`: tradotta, il nome dell'oggetto sparisce. Sta in
`invariati.md` col motivo. ⚠️ E adesso c'è anche **` Lv`**
(`action.hsp:12383`): non è un'etichetta, è la stringa che il gioco **cerca in
coda al nome** per togliere il suffisso di livello. **Prima di tradurre una
stringa corta, guardare chi la consuma.**

### Un letterale confrontato muore quando l'altro lato è tradotto

La battuta dell'orso (`chara_func.hsp:6852`) era già morta: `cnv_str` cercava
«was killed by motuhegui» dove ora c'è «lo sbudellatore». ⚠️ Le due toppe che la
riparano vanno in **ordine invertito** rispetto al sorgente.

### Le altre, invariate dalle sessioni prima

- il giapponese arbitra, e sulle voci l'inglese inventa — in questa sessione ha
  arbitrato su `praise`/`authority`, dove l'inglese usa due parole per un
  giapponese solo;
- la carta di `db_card.hsp` dice cosa la creatura rappresenta;
- l'articolo sta sulla testa del sintagma, non sulla persona;
- `ドレイク` è «draco», confermato a schermo;
- un nome già preso non si può riusare, **e vale anche per le esche del quiz**.

## L'ordine che resta

1. **`text.hsp`**, 960 firme dal 45% in su — ⚠️ dentro ci sono le etichette
   degli elementi (`:1951` e seguenti, `txtseteyes`), e le rese sono già fissate
   da `action.hsp:9588`-`9628`: si **copiano**;
2. `proc.hsp` — chiude le 20 rinviate e il gemello di «mordes»;
3. `command.hsp`, `trait.hsp`;
4. `ai.hsp` (94) ed `event.hsp` (649);
5. `chara_func.hsp`, le 286 rimanenti — ⚠️ dentro ci sono le tre pietre di
   Lesimas e l'ankh del sole, già fissate dal quiz in `glossario.md`: quelle
   rese si **copiano**. E c'è la causa di morte (`:6850`), che però va insieme a
   `main.hsp:4409`;
6. `init.hsp` (133) — ⚠️ **lì sta la decisione sul possessivo** `his(x, 1)`, che
   ha 36 siti di chiamata e nessuna resa che vada bene ovunque. Vedi
   `decisioni.md`, 2026-08-10;
7. le 2.203 righe di `db_creature.hsp` e le 2.555 descrizioni di `db_item.hsp`.

## Cose che valgono sempre

⚠️ **Il sorgente è pinnato al tag `2.31.2.0`**, e l'integrità si verifica col
manifesto SHA-256, **mai** con `git status`, che in quel clone è permanentemente
sporco. Gli hash del manifesto sono in MAIUSCOLO.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp`; cercare chi copia nomi di creatura fuori da
`db_creature.hsp`; cercare chi confronta un letterale contro un valore che
abbiamo tradotto — `cnv_str`, `instr`, `==` su stringhe.

⚠️ **CP932 non codifica tutto.** Niente `«»` (si usano le tipografiche `“”`),
niente dieresi tedesche, niente `å`. Gli accenti veri si scrivono nel dizionario
e li degrada `applica`; ⚠️ **guardare dove cade l'accento**: a fine parola è
gratis, a metà no («dèi» → `de'i`, e infatti si è scritto «le divinità»).
L'apostrofo è quello ASCII, non il tipografico. ⚠️ **Le toppe non passano da
`degrada`**: lì gli accenti non si scrivono proprio.

⚠️ Un guardiano dell'ambiente blocca i messaggi di commit che contengono `/man/`
letto come percorso: passare il testo con `git commit -F <file>`.

## Per rifare la prova in gioco

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -Force
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

⚠️ La copia fallisce se il gioco è aperto. ⚠️ Se `applica` viene interrotta da un
blocco di file lascia l'albero di build **incompleto**, e `compila` poi dice
«main.hsp non è in ...»: si rilancia `applica` e basta.

### La console di debug

**Si apre con F12** (`main.hsp:3322`, codice tasto 123; F11 è `dump_chara`).
Esce con ESC. Parte in modalità **HSP, non Lua**: `spawn_chara <id>` funziona
subito, ed è nativo (`system.hsp:4831`), quindi va anche in `cgx-test.exe`.

ID utili, tutti con un'evoluzione: **165** il cane e **50** il segugio → la
zanna d'argento; **267** il cavallo zoppo → l'unicorno; **386** la giraffa → il
Kirin; **210** la sorella gatta minore.

C'è anche **`spawn_item <id>`** (`system.hsp:4847`), che lascia l'oggetto **per
terra**, non nello zaino: dopo il comando si raccoglie con `,`. Gli ID sono le
costanti `ITEM_ID_*` di `defines/mod.hsp` — 1037 l'occhio elementale, 1275
l'orbe bianco-nero, 1261 il pacco di tappi, 1023 il kit di pronto soccorso, 478
lo stetoscopio, 634 il guinzaglio, 1248 i calzini, 1116 l'esca, 684 la macchina
genetica.

⚠️ **Domanda aperta, 2026-08-10.** Due volte di fila `spawn_item` ha prodotto un
oggetto diverso da quello chiesto (una mela per il 478, un salvagente per il
1037), e poi ha ripreso a funzionare senza che si capisse cosa fosse cambiato —
e la casella era sgombra in entrambi i casi. **Non è un difetto di parsing**:
misurato con un programmino HSP compilato con l'SDK, `int(" 478\r\n")` dà 478, e
la generazione a caso richiede `dbid == -1`, che con un ID esplicito non si
verifica mai (`item.hsp:2246`, `item_func.hsp:6`). L'unica pista rimasta è lo
stato dei filtri: `spawn_item` **non chiama `flt`**, mentre `spawn_set_item`, tre
righe più sotto, lo chiama a ogni giro. Se ricapita, guardare lì.

⚠️ Non trarne conclusioni sul comando gemello: `spawn_chara` ha la stessa riga di
parsing, e la prova qui sopra **conferma** la conclusione del 2026-08-09, cioè
che l'ID veniva onorato anche allora.

⚠️ **Generare mostri a mano è un modo pessimo di provare l'evoluzione**:
`chara.hsp:2319` la tira con `rnd(300) < gdata(GDATA_LEVEL)`, dove
`GDATA_LEVEL` è **il piano del dungeon**. Al piano 1 è lo 0,3% per mostro. La
prova buona è entrare in una **Nefia profonda** con *Spawn evolved enemies* su
**always**.

### Il collaudo, punto per punto

- ✅ **L'evoluzione degli alleati**: provata il 2026-08-10.
- ✅ **I nomi a schermo**, ✅ **«draco»**: provati.
- ✅ **Il combattimento in italiano**: provato.
- ❌ **L'evoluzione dei nemici**: **mai vista**. È la sola prova mancante.
- 🆕 **Da provare, tutto quello che questa sessione ha tradotto**: i messaggi
  degli oggetti da usare — l'occhio elementale che grida l'elemento
  (`action.hsp:9568`), la spirale di frasi dell'agricoltura (`:18881`-`:18910`),
  la paghetta di Yacatect (`:14240`-`:14320`), la sintesi dei compagni
  (`:18958`-`:19036`). Sono tutte righe che si vedono usando un oggetto, quindi
  la prova è veloce: bastano gli oggetti giusti e un `spawn_chara`.
- ⚠️ **Il non tradotto esce in inglese, non in giapponese.**

## I tetti misurati, con la loro ancora

| campo | tetto | ancora | fonte |
|---|---|---|---|
| tracciatore HUD | 6 | sinistra, taglia | `screen.hsp:2002` |
| razza e classe | 3 | sinistra, taglia | `chara.hsp:4679` |
| slot d'equipaggiamento | 6 | sinistra, taglia | osservato a schermo |
| gradi di resistenza | 9 | **destra, invade** | `command.hsp:11002` |
| nome nella lista abilità | **24** | sinistra, invade il costo | `command.hsp:5382` |
| descrizione nella lista | 34 | taglia (`strmid`) | `command.hsp:5389` |

⚠️ Il nome di creatura compare in messaggi **senza limite**. Il più lungo del
dizionario è `<Ratin> l'investigatrice della Gilda dei Guerrieri`, 50 caratteri:
visto a schermo, non tronca.

Vedi [[una-guardia-vale-solo-dove-guarda]], [[guardia-troppo-severa]],
[[il-testo-dentro-la-stringa-non-e-codice]],
[[la-frase-che-si-compone-in-due-file]],
[[il-nome-interno-non-e-quello-a-schermo]],
[[coerenza-fra-due-file-uno-solo-tracciato]],
[[toppe-fuori-dal-dizionario]], [[la-forma-memorizzata-non-e-quella-scritta]],
[[una-chiave-che-collide-non-e-una-chiave]],
[[il-campo-che-il-sorgente-dichiara]], [[la-testa-porta-il-genere]],
[[una-decisione-nel-posto-sbagliato]], [[una-guardia-agganciata-a-se-stessa]],
[[larghezza-per-campo]], [[ultima-scrittura-vince]],
[[percentuale-senza-denominatore]], [[una-procura-non-e-una-proprieta]],
[[la-categoria-che-il-sorgente-dichiara]],
[[il-posto-decide-quando-arriva-il-dato]], [[dato-o-derivata]],
[[toppe-generate-dal-sorgente]], [[stessa-forma-va-verificata-nel-codice]],
[[strumento-di-diagnosi-assente-non-guasto]],
[[il-database-che-spiega-invece-di-dichiarare]], [[omofono-base-kanji-patina]]
e [[cp932-perdite-silenziose]].
