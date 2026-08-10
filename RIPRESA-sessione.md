# Ripresa sessione

Aggiornato: 2026-08-10, fine della ventunesima sessione.

## La prima cosa da fare

**`text.hsp` è al 60%**: 1.038 firme su 1.740, ne restano **702**. Si prosegue
per zona di riga da **riga 2836** (le descrizioni della mappa del mondo,
Noyel in poi), col metodo qui sotto.

⚠️ **C'è un controllo nuovo nella catena, e va lanciato a ogni lotto di menu:**

```powershell
python -m strumenti.larghezze
```

Deve dire `voci fuori misura: 0 su 75 menu misurati`. Se dice altro, la resa non
sta nel riquadro e va accorciata **prima** di reimportare: a schermo verrebbe
tagliata a metà parola. Vedi «Il tetto di un menu».

### Le cinque verifiche d'apertura

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 357 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 320, doppie 0, senza razza 0
python -m strumenti.larghezze              # atteso: 0 fuori misura su 75 menu
```

I test sono **357**, non più 344: tredici nuovi, tutti in
`test_larghezze.py`.

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.606 | 1.606 | **100%** |
| `item_data.hsp` | 318 | 318 | **100%** |
| `skill.hsp` | 885 | 885 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `action.hsp` | 1.286 | 1.288 | **100%** (le 2 mancanti sono rinviate a toppa) |
| `text.hsp` | **1.038** | 1.740 | **60%** |
| gli altri tre | 0 | 2.775 | 0% |
| **totale Fase 1** | **5.145** | **8.624** | **60%** |

Fuori dalla Fase 1: `db_creature.hsp` a 1.452 su 3.655;
`custom_enemyevolution.hsp` **chiuso**; `ai.hsp` 6 su 100; `event.hsp` 5 su
654; `chara_func.hsp` 45 su 331; `init.hsp` 0 su 133.

**357 test**, prova d'identità **72/72 e 27.813**, **8.962 sostituzioni**, il
compilatore non dice nulla.

## Il tetto di un menu

⚠️ **Il riquadro taglia**: non manda a capo, non restringe il carattere. Visto a
schermo il 2026-08-10, dove otto frasi diverse finivano allo stesso pixel.

Il metro sta nel sorgente, non a occhio: è il terzo argomento che il chiamante
passa a `*prompt_key`.

```hsp
val = promptx, prompty, 300, 1      ← 300 pixel
```

`caratteri = (pixel − 46) / 7,7`, misurato su due riquadri. Lo fa
`strumenti/larghezze.py`; `--tutti` elenca i 75 menu col loro tetto.

⚠️ **La stringa inglese non è il budget.** In dieci menu su venti sfora anche
lei: `txtsettamer` ha una voce inglese da 46 caratteri in un riquadro da 32.
Prendere a modello una resa precedente senza misurarla è come sono nate sette
delle 41 voci corrette in questa sessione.

⚠️ **La larghezza può dipendere dalla lingua**: `450 - 50 * en` vale **400** per
noi, che compiliamo la build inglese.

## Le due righe di `action.hsp` che non si traducono

Sono decisioni, non arretrato, e **vanno scartate a mano quando si compone un
lotto** se un giorno si torna su questo file (`estrai --da-tradurre` le toglie
già lui, ma il conto delle non tradotte le porta per sempre).

- **`:4584`** — l'articolo inglese davanti al nome di un'arma unica. Toppa.
- **`:9631`** — `his(tc, 1)`, il possessivo che in italiano si omette. Toppa.
  ⚠️ **Il testo di una toppa non passa da `degrada` e non può portare accenti**:
  è per questo che la resa è «ha cambiato elemento» e non «ha cambiato affinità
  elementale». Il dettaglio in `decisioni.md`.

## 391 stringhe fuori perimetro, trovate a schermo

⚠️ **Un oggetto di Elona ha due nomi, e ne traduciamo uno.** `iknownnameref` è
quello che il gioco mostra **prima dell'identificazione** — l'occhio elementale
si presenta come `colorful eyes` — e l'estrattore non lo guarda:
`_ASSEGNA_NOME` (`estrai.py:65`) accetta solo `ioriginalnameref`.

**Deciso il 2026-08-10: si annota e si prosegue col piano.** Il perimetro nuovo
si affronta dopo la Fase 1, e prima si scrive lo strumento che lo misura. Il
censimento e l'ordine stanno in `decisioni.md`.

⚠️ Conseguenza: il 100% di `db_item.hsp` e di `custom_tweaks.hsp` **è falso**.
Il denominatore conta solo ciò che l'estrattore sa vedere.

## Il metodo

**I lotti si prendono per zona di riga**, non separando statiche e dinamiche.

```powershell
python -m strumenti.estrai text.hsp --da-tradurre --uscita lavoro/_r.jsonl
# si ordina per (riga, occorrenza) e si prendono le prime ~50
python -m strumenti.verifica lavoro/<lotto>.jsonl
python -m strumenti.reimporta lavoro/<lotto>.jsonl
python -m strumenti.larghezze
python -m pytest strumenti/tests -q
python -m strumenti.prova_identita
python -m strumenti.genera_toppe_nomi
python -m strumenti.genera_toppe_casuali
```

⚠️ **Una riga può portare più voci, e la riga da sola non è una chiave.**
`text.hsp:2588` ha due prefissi sulla stessa riga. Chi scrive il lotto deve
indicizzare per **(riga, giapponese)** o per (riga, inglese).

⚠️ **Ma la zona di riga non è un dogma.** I dieci prefissi di `text.hsp:2588` si
concatenano col tipo di Nefia che sta a `:3058`: si sono presi insieme, perché
separati non si possono scrivere. Quando due pezzi si concatenano, il lotto
segue la concatenazione e non la riga.

## Le regole di resa, aggiornate

Valgono le precedenti — terza persona sempre; mai `_s()`, `is()`, `was()`,
`your()`, `have()`, `does()`, `yourself()`; mai una preposizione davanti a
`name()` o `itemname()`, mentre `con`, `per`, `tra`, `sopra`, `dentro` e
`contro` reggono; la preposizione sta nel valore, non nella frase; invarianza di
genere prima di tutto; un nome di abilità o di oggetto si copia, non si traduce;
una `statica` si scrive **nuda**, con le virgolette tipografiche `“”`.

⚠️ **`his(x)` a un argomento si può togliere, `his(x, 1)` no.**

Tre aggiunte di questa sessione:

- **Un prefisso che precede sostantivi di genere diverso può solo essere un
  aggettivo in -e.** I dieci prefissi delle Nefia stanno davanti a Grotta,
  Torre, Forte, Lago: Iniziale, Mite, Audace, Palpitante, Ingannevole,
  Illustre, Mortale, Impenetrabile, Fatale, Informe. Qualche fedeltà si perde,
  ed è il prezzo del vincolo.
- **Una frase d'amore non porta participi.** Né chi parla né chi ascolta ha un
  genere noto: `You deceived me!?` è «Mi stavi ingannando!?»; `I'm fed up with
  you` è «Mi dai sui nervi», non «Mi hai stufato».
- **In un menu la valuta si abbrevia.** «Energia da lavoro» → «Energia» dentro
  il suo negozio, come l'inglese abbrevia `Toil-Energy`. Per esteso resta nella
  prosa.

## Le cose da non riscoprire

### Metà delle voci di menu erano già decise altrove

È il difetto più facile da introdurre in `text.hsp`, e ne ho evitati sei in una
sessione sola cercando **prima** di scrivere:

- i **tipi di negozio** (`txtsetshop`) sono gli stessi giapponesi dei titoli del
  negoziante a `text.hsp:420-460`: 何でも屋 → «del bazar» → «Bazar»;
- gli **elementi** dell'occhio elementale (`txtseteyes`) sono fissati da
  `action.hsp:9588-9628`, dove l'occhio li ripete;
- i **verbi dei menu della pianta** sono quelli dei messaggi di
  `action.hsp:18881-18910`;
- gli **assetti tattici** sono i messaggi di conferma di `action.hsp:15232-15250`;
- le **parti del corpo** di `txtplusbody` sono `bodyn` (`text.hsp:136`), che
  compone il messaggio dopo la scelta;
- il **tipo di Nefia** è `_nefiatype` (`text.hsp:50`).

⚠️ **L'inglese di `txtplusbody` non è mai stato tradotto**: dice `bodyHead`,
`bodyNeck`, `bodyFinger`. Il giapponese sì.

### Aggiungere una funzione che l'inglese non aveva non si può

`verifica` confronta l'elenco delle interpolazioni. Si possono **togliere** le
morfologiche, non se ne possono **aggiungere**.

### La frase di combattimento vive in due file

`action.hsp` scrive «… e» e imposta `gdata(GDATA_DMG_TYPE) = 2`;
`chara_func.hsp:6323` legge il flag e stampa il resto con `txtcontinue`, che
sopprime la maiuscola (`init.hsp:1663`). `init.hsp:1666` aggiunge già lo spazio:
**la giuntura non va spaziata a mano**.

### Le stringhe che sembrano testo e sono codice

`EN` (`action.hsp:4816`) è la chiave con cui il gioco cerca `%txtName,EN`. E
` Lv` (`action.hsp:12383`) è la stringa che il gioco **cerca in coda al nome**
per togliere il suffisso di livello. **Prima di tradurre una stringa corta,
guardare chi la consuma.**

### Un letterale confrontato muore quando l'altro lato è tradotto

La battuta dell'orso (`chara_func.hsp:6852`): `cnv_str` cercava «was killed by
motuhegui» dove ora c'è «lo sbudellatore». ⚠️ Le due toppe che la riparano vanno
in **ordine invertito** rispetto al sorgente.

### Un'etichetta può parlare dello stato del gioco, e lì arbitra il codice

`text.hsp:2271` è annotata 未実装, «non implementato», e l'inglese dice
`Summon Joker`. Il codice sta con l'inglese: `proc.hsp:20175-20185` spende 50 di
barra e trasforma un compagno in `{Variable Joker}`. **Il giapponese arbitra sul
significato, non sullo stato del gioco.**

### Le altre, invariate dalle sessioni prima

- il giapponese arbitra, e sulle voci l'inglese inventa — in questa sessione ha
  arbitrato otto volte, fra cui 頼りにしている («mi fido di te», non «I'm in your
  debt»), 勇者の («dell'eroe», non `Servant's`) e 収容所 («campo di prigionia»,
  non un `Camp` qualsiasi);
- la carta di `db_card.hsp` dice cosa la creatura rappresenta;
- l'articolo sta sulla testa del sintagma, non sulla persona;
- `ドレイク` è «draco», confermato a schermo;
- un nome già preso non si può riusare, **e vale anche per le esche del quiz**.

## L'ordine che resta

1. **`text.hsp`**, 702 firme dal 60% in su, da riga 2836;
2. `proc.hsp` — chiude le 20 rinviate e il gemello di «mordes»;
3. `command.hsp`, `trait.hsp`;
4. `ai.hsp` (94) ed `event.hsp` (649);
5. `chara_func.hsp`, le 286 rimanenti — ⚠️ dentro ci sono le tre pietre di
   Lesimas e l'ankh del sole, già fissate dal quiz in `glossario.md`, e la causa
   di morte (`:6850`), che va insieme a `main.hsp:4409`;
6. `init.hsp` (133) — ⚠️ **lì sta la decisione sul possessivo** `his(x, 1)`, che
   ha 36 siti di chiamata. Vedi `decisioni.md`, 2026-08-10;
7. le 2.203 righe di `db_creature.hsp` e le 2.555 descrizioni di `db_item.hsp`.

## Domande aperte

⚠️ **`Cyber Dome` fu deciso sull'inglese.** Il 2026-08-07 → «Cupola
Cibernetica», ma il giapponese è アクリ・テオラ, un nome **opaco** che per la
regola dei nomi propri resterebbe invariato. La resa è già in `db_creature.hsp`:
riaprirla tocca più file. Segnalata, non toccata.

⚠️ **`spawn_item` ha prodotto due volte l'oggetto sbagliato**, poi ha ripreso.
Escluso il parsing e la generazione a caso; l'unica pista è lo stato dei filtri:
`spawn_item` **non chiama `flt`**, mentre `spawn_set_item` sì. Se ricapita,
guardare lì.

## Cose che valgono sempre

⚠️ **Il sorgente è pinnato al tag `2.31.2.0`**, e l'integrità si verifica col
manifesto SHA-256, **mai** con `git status`, che in quel clone è permanentemente
sporco. Gli hash del manifesto sono in MAIUSCOLO.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp`; chi copia nomi di creatura fuori da
`db_creature.hsp`; chi confronta un letterale contro un valore tradotto —
`cnv_str`, `instr`, `==` su stringhe.

⚠️ **CP932 non codifica tutto.** Niente `«»` (si usano le tipografiche `“”`),
niente dieresi tedesche, niente `å`. Gli accenti veri si scrivono nel dizionario
e li degrada `applica`; ⚠️ **guardare dove cade l'accento**: a fine parola è
gratis, a metà no. L'apostrofo è quello ASCII. ⚠️ **Le toppe non passano da
`degrada`**.

⚠️ Un guardiano dell'ambiente blocca i messaggi di commit che contengono `/man/`
letto come percorso: passare il testo con `git commit -F <file>`.

⚠️ **La shell di PowerShell mangia il backtick**: scrivere un documento che
contiene `` `codice` `` da riga di comando lo corrompe in silenzio. Passare da
un file `.py`.

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

⚠️ **Controllare la data dell'exe prima di fidarsi di uno screenshot.** Il
2026-08-10 un menu è sembrato non tradotto per venti minuti: era l'eseguibile
della sessione prima.

**L'eseguibile in `cgx-test.exe` è aggiornato a fine ventunesima sessione.**

### La console di debug

**Si apre con F12** (`main.hsp:3322`; F11 è `dump_chara`). Esce con ESC. Parte in
modalità **HSP, non Lua**: `spawn_chara <id>` funziona subito.

ID utili, tutti con un'evoluzione: **165** il cane e **50** il segugio → la
zanna d'argento; **267** il cavallo zoppo → l'unicorno; **386** la giraffa → il
Kirin; **210** la sorella gatta minore.

`spawn_item <id>` lascia l'oggetto **per terra**: si raccoglie con `,`. ID utili:
**746** la frusta da domatore (apre il menu degli ordini al compagno), **1249**
l'Aurtehom (il libro dell'abisso), 1037 l'occhio elementale, 1275 l'orbe
bianco-nero, 1023 il kit di pronto soccorso, 478 lo stetoscopio, 634 il
guinzaglio, 684 la macchina genetica.

⚠️ **Generare mostri a mano è un modo pessimo di provare l'evoluzione**:
`chara.hsp:2319` la tira con `rnd(300) < gdata(GDATA_LEVEL)`, dove
`GDATA_LEVEL` è **il piano del dungeon**. La prova buona è entrare in una
**Nefia profonda** con *Spawn evolved enemies* su **always**.

### Il collaudo, punto per punto

- ✅ **L'evoluzione degli alleati**, ✅ **i nomi a schermo**, ✅ **«draco»**,
  ✅ **il combattimento in italiano**: provati.
- ✅ **Il menu degli ordini al compagno e il libro dell'abisso**: provati il
  2026-08-10, ed è da lì che è venuta la misura dei riquadri.
- ❌ **L'evoluzione dei nemici**: **mai vista**. È la sola prova mancante, e
  dopo il controllo sulle 250 rinomine vale come conferma dell'innesco.
- 🆕 **Da provare**: i menu tradotti in questa sessione che non si sono ancora
  visti — il negozio a YacaPoint (`spawn_chara` di Yacatect), la banca, il
  gioco di carte, la mappa del mondo con i nomi delle città.
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
| **voce di menu** | **(px − 46) / 7,7** | sinistra, taglia | il chiamante di `*prompt_key`, e `strumenti/larghezze.py` |

⚠️ Il nome di creatura compare in messaggi **senza limite**. Il più lungo del
dizionario è `<Ratin> l'investigatrice della Gilda dei Guerrieri`, 50 caratteri:
visto a schermo, non tronca.

Vedi [[larghezza-per-campo]], [[una-guardia-vale-solo-dove-guarda]],
[[guardia-troppo-severa]], [[il-testo-dentro-la-stringa-non-e-codice]],
[[la-frase-che-si-compone-in-due-file]],
[[il-nome-interno-non-e-quello-a-schermo]],
[[coerenza-fra-due-file-uno-solo-tracciato]],
[[toppe-fuori-dal-dizionario]], [[la-forma-memorizzata-non-e-quella-scritta]],
[[una-chiave-che-collide-non-e-una-chiave]],
[[il-campo-che-il-sorgente-dichiara]], [[la-testa-porta-il-genere]],
[[una-decisione-nel-posto-sbagliato]], [[una-guardia-agganciata-a-se-stessa]],
[[ultima-scrittura-vince]], [[percentuale-senza-denominatore]],
[[una-procura-non-e-una-proprieta]], [[la-categoria-che-il-sorgente-dichiara]],
[[il-posto-decide-quando-arriva-il-dato]], [[dato-o-derivata]],
[[toppe-generate-dal-sorgente]], [[stessa-forma-va-verificata-nel-codice]],
[[strumento-di-diagnosi-assente-non-guasto]],
[[il-database-che-spiega-invece-di-dichiarare]], [[omofono-base-kanji-patina]]
e [[cp932-perdite-silenziose]].
