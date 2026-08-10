# Ripresa sessione

Aggiornato: 2026-08-11, fine della diciannovesima sessione.

## La prima cosa da fare

Continuare `action.hsp`, che è a **838 firme su 1.288 (65%)**. Restano **450
firme**: si prendono **per zona di riga**, dalla 8274 in avanti, senza separare
statiche e dinamiche — vedi «Il metodo, cambiato».

⚠️ **Restano non provate in gioco le rinomine all'evoluzione dei nemici.**
Questa sessione le ha però verificate meccanicamente: 249 `evold` su 250
combaciano con un nome che possono davvero incontrare, e la sola rotta —
`<Gwen>` — è stata riparata. La prova a schermo serve ormai solo a confermare
l'innesco, non i nomi. Vedi «Per rifare la prova in gioco».

### Le quattro verifiche d'apertura

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 343 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 320, doppie 0, senza razza 0
```

I test sono **343**, non più 338: cinque nuovi, tutti armati su difetti veri
trovati in questa sessione.

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.606 | 1.606 | **100%** |
| `item_data.hsp` | 318 | 318 | **100%** |
| `skill.hsp` | 885 | 885 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `action.hsp` | 838 | 1.288 | **65%** |
| `text.hsp` | 780 | 1.740 | 45% |
| gli altri tre | 0 | 2.775 | 0% |
| **totale Fase 1** | **4.439** | **8.624** | **51%** |

Fuori dalla Fase 1: `db_creature.hsp` a 1.452 su 3.655;
`custom_enemyevolution.hsp` **chiuso**; `ai.hsp` 6 su 100; `event.hsp` 5 su
654; `chara_func.hsp` **45 su 331**, entrato in questa sessione.

**343 test**, prova d'identità **72/72 e 27.813**, **7.922 sostituzioni**, il
compilatore non dice nulla.

## Quello che questa sessione ha cambiato negli strumenti

Sono quattro guardie riparate, e tre rendevano certe voci **intraducibili**. Il
dettaglio sta in `decisioni.md`; qui il minimo per non rifare la strada.

1. **La guardia sulla rinomina leggeva solo `action.hsp`** — `evoluzioni_con_jp()`
   ha quel percorso come default. Ora il controllo copre anche
   `custom_enemyevolution.hsp`, `ai.hsp` ed `event.hsp`, e ha trovato `<Gwen>`.
2. **`is2` mancava dalla morfologia inglese** (`init.hsp:1768`). L'elenco ora
   si rilegge dal sorgente invece di fidarsi di quello scritto a mano.
3. **Il parser leggeva il testo dentro le stringhe come codice**: `production (`
   in una frase inglese sembrava una chiamata di funzione. Aggiunta
   `_maschera_letterali`.
4. **Una resa vuota non si può dichiarare**, e va bene così: si risolve con una
   toppa più una riga in `rinviate.jsonl`.

> Ogni guardia nuova l'ho vista **fallire** rimettendo il difetto, prima di
> tenerla. Un controllo mai visto rosso non è una guardia.

## Il metodo, cambiato

**I lotti si prendono per zona di riga**, non separando statiche e dinamiche.

```powershell
python -m strumenti.estrai action.hsp --da-tradurre --uscita lavoro/_r.jsonl
# si ordina per (riga, occorrenza) e si prendono le prime ~50
python -m strumenti.verifica lavoro/<lotto>.jsonl
python -m strumenti.reimporta lavoro/<lotto>.jsonl
python -m pytest strumenti/tests -q
python -m strumenti.prova_identita
python -m strumenti.genera_toppe_nomi
python -m strumenti.genera_toppe_casuali
```

Perché: separando i tipi, le otto metà di frase che finiscono in « and » erano
finite in un lotto e le loro gemelle in un altro. Per zona, il sorgente attorno
si legge una volta sola e le frasi spezzate restano insieme.

⚠️ **La firma di `action.hsp:4584` non si traduce** ma resta contata fra le non
tradotte: è in `rinviate.jsonl`, risolta da toppa. Va scartata a mano quando si
compone un lotto (`x['riga'] != 4584`).

## Le regole di resa, aggiornate

Le tre di prima valgono ancora — terza persona sempre; mai `_s()`, `is()`,
`was()`, `your()`, `have()`, `does()`, `yourself()`; mai una preposizione
davanti a `name()` o `itemname()`. **`con`, `per`, `tra`, `sopra`, `dentro` e
`contro` invece reggono**, perché non si fondono con l'articolo.

Tre aggiunte di questa sessione:

- **La preposizione sta nel valore, non nella frase.** Se quattro frasi
  concatenano tutte « di » davanti alla stessa variabile, la preposizione va
  **dentro i valori** («d'erbe», «di gemme») e tolta dalle frasi. Stesso
  criterio dell'articolo dentro il nome di creatura.
- **Invarianza di genere prima di tutto.** Il bersaglio può essere qualunque
  creatura e l'oggetto qualunque cosa: «Non ha più cariche» e non «è scarico»,
  «vibra di malumore» e non «è scontento», «Il peso ti schiaccia» e non «Sei
  schiacciato». Nelle continuazioni del danno il complemento si omette del
  tutto, perché il bersaglio è già nella prima metà della frase.
- **Un nome di abilità o di oggetto non si traduce: si copia** dal file che
  genera l'etichetta vera. ⚠️ E il nome interno può essere un altro:
  `Sense Quality` è l'abilità che a schermo si chiama «Analisi»
  (`skill.hsp:252`).

## Le cose da non riscoprire

### La frase di combattimento vive in due file

`action.hsp` scrive «… e» e imposta `gdata(GDATA_DMG_TYPE) = 2`;
`chara_func.hsp:6323` legge il flag e stampa il resto con `txtcontinue`, che
sopprime la maiuscola (`init.hsp:1663`). `init.hsp:1666` aggiunge già lo spazio
fra due messaggi: **la giuntura non va spaziata a mano**.

Per ogni contenuto servono due rese: una che si aggancia, una autonoma.

### Le stringhe che sembrano testo e sono codice

`EN` (`action.hsp:4816`) è la chiave con cui il gioco cerca `%txtName,EN` nei
file `user\item\plan*.txt`: tradotta, il nome dell'oggetto sparisce. Sta in
`invariati.md` col motivo. **Prima di tradurre una stringa corta e maiuscola,
guardare chi la consuma.**

### Un letterale confrontato muore quando l'altro lato è tradotto

La battuta dell'orso (`chara_func.hsp:6852`) era già morta: `cnv_str` cercava
«was killed by motuhegui» dove ora c'è «lo sbudellatore». ⚠️ Le due toppe che
la riparano vanno in **ordine invertito** rispetto al sorgente, perché in
italiano la forma corta è prefisso di quella lunga e `cnv_str` sostituisce sul
primo riscontro.

### Le altre, invariate dalle sessioni prima

- il giapponese arbitra, e sulle voci l'inglese inventa;
- la carta di `db_card.hsp` dice cosa la creatura rappresenta;
- l'articolo sta sulla testa del sintagma, non sulla persona;
- `ドレイク` è «draco», confermato a schermo;
- un nome già preso non si può riusare, **e vale anche per le esche del quiz**.

## L'ordine che resta

1. **`action.hsp`**: 450 firme, per zona dalla 8274;
2. `text.hsp` dal 45% in su;
3. `proc.hsp` — chiude le 20 rinviate e il gemello di «mordes»;
4. `command.hsp`, `trait.hsp`;
5. `ai.hsp` (94) ed `event.hsp` (649);
6. `chara_func.hsp`, le 286 rimanenti — ⚠️ dentro ci sono le tre pietre di
   Lesimas e l'ankh del sole, già fissate dal quiz in `glossario.md`: quelle
   rese si **copiano**. E c'è la causa di morte (`:6850`), che però va insieme
   a `main.hsp:4409`;
7. le 2.203 righe di `db_creature.hsp` e le 2.555 descrizioni di `db_item.hsp`.

## Cose che valgono sempre

⚠️ **Il sorgente è pinnato al tag `2.31.2.0`**, e l'integrità si verifica col
manifesto SHA-256, **mai** con `git status`, che in quel clone è permanentemente
sporco. Gli hash del manifesto sono in MAIUSCOLO.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp`; cercare chi copia nomi di creatura fuori da
`db_creature.hsp`; **e adesso anche** cercare chi confronta un letterale contro
un valore che abbiamo tradotto — `cnv_str`, `instr`, `==` su stringhe.

⚠️ **CP932 non codifica tutto.** Niente `«»` (si usano le tipografiche `“”`),
niente dieresi tedesche, niente `å`. Gli accenti veri si scrivono nel dizionario
e li degrada `applica`; ⚠️ **guardare dove cade l'accento**: a fine parola è
gratis, a metà no («dèi» → `de'i`, e infatti si è scritto «le divinità»).
L'apostrofo è quello ASCII, non il tipografico.

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
subito, ed è nativo (`system.hsp:4831`), quindi va anche in `cgx-test.exe`, che
è l'eseguibile che si spedisce.

ID utili, tutti con un'evoluzione: **165** il cane e **50** il segugio → la
zanna d'argento; **267** il cavallo zoppo → l'unicorno; **386** la giraffa → il
Kirin; **210** la sorella gatta minore.

⚠️ **Generare mostri a mano è un modo pessimo di provare l'evoluzione**:
`chara.hsp:2319` la tira con `rnd(300) < gdata(GDATA_LEVEL)`, dove
`GDATA_LEVEL` è **il piano del dungeon**. Al piano 1 è lo 0,3% per mostro. La
prova buona è entrare in una **Nefia profonda** con *Spawn evolved enemies* su
**always**, dove la mappa genera decine di mostri in un colpo solo.

### Il collaudo, punto per punto

- ✅ **L'evoluzione degli alleati**: provata il 2026-08-10.
- ✅ **I nomi a schermo**, ✅ **«draco»**: provati.
- ✅ **Il combattimento in italiano**: provato il 2026-08-11 («tutto ok»
  riferito dall'utente dopo l'avvio di `cgx-test.exe`).
- ❌ **L'evoluzione dei nemici**: **mai vista**. Resta la sola prova mancante,
  ma dopo il controllo meccanico sulle 250 rinomine vale come conferma
  dell'innesco, non dei nomi.
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

Vedi [[una-guardia-vale-solo-dove-guarda]],
[[il-testo-dentro-la-stringa-non-e-codice]],
[[la-frase-che-si-compone-in-due-file]],
[[il-nome-interno-non-e-quello-a-schermo]],
[[coerenza-fra-due-file-uno-solo-tracciato]], [[guardia-troppo-severa]],
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
