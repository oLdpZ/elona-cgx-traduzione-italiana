# Ripresa sessione

Aggiornato: 2026-08-11, fine della ventiduesima sessione.

## La prima cosa da fare

**`text.hsp` è al 70%**: 1.221 firme su 1.740, ne restano **519**. Si prosegue
per zona di riga da **riga 4213**, col metodo qui sotto.

⚠️ **Prima però c'è un collaudo aperto, e costa due minuti.** La resa dei cibi
di carne mette la creatura **fra parentesi** — «bistecca (il cane)» — ed è
l'unica scelta della ventiduesima sessione mai vista a schermo. Se legge male si
cambia in un posto solo (`text.hsp:3221-3356`), ma va guardata **prima** di
accumularci sopra altri lotti.

```
F12 → spawn_item 256      attrezzo da cucina portatile
F12 → spawn_chara 165     il cane
ESC → uccidi il cane, raccogli con , l'attrezzo e il cadavere
usa l'attrezzo → scegli il cadavere → guarda il nome in inventario
```

### Le cinque verifiche d'apertura

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 357 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 320, doppie 0, senza razza 0
python -m strumenti.larghezze              # atteso: 0 fuori misura su 75 menu
```

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.606 | 1.606 | **100%** |
| `item_data.hsp` | 318 | 318 | **100%** |
| `skill.hsp` | 885 | 885 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `action.hsp` | 1.286 | 1.288 | **100%** (le 2 mancanti sono rinviate a toppa) |
| `text.hsp` | **1.221** | 1.740 | **70%** |
| gli altri tre | 0 | 2.775 | 0% |
| **totale Fase 1** | **5.328** | **8.624** | **62%** |

Fuori dalla Fase 1: `db_creature.hsp` a 1.452 su 3.655;
`custom_enemyevolution.hsp` **chiuso**; `ai.hsp` 6 su 100; `event.hsp` 5 su
654; `chara_func.hsp` 45 su 331; `init.hsp` 0 su 133.

**357 test**, prova d'identità **72/72 e 27.813**, **9.214 sostituzioni**, il
compilatore non dice nulla.

## Le tre regole nuove di questa sessione

### 1. L'ordine di una concatenazione non è un vincolo: si toppa

`decisioni.md` aveva scritto che i prefissi delle Nefia dovevano restare davanti
al nome perché «l'ordine lo fissa il codice». **Non era vero**: due toppe da una
riga svuotano l'accumulatore e riaccodano il prefisso, e ottanta nomi sono
passati da «Fatale Miniera» a «Miniera Fatale».

⚠️ **Ma una toppa può agganciarsi solo a una riga che il dizionario lascia
identica, cioè a una riga senza `lang()`.** Il test
`test_le_toppe_del_progetto_si_applicano_al_sorgente_pinnato` prova le toppe
contro il **sorgente pinnato**, dove la riga dice ancora `"Cave"`, mentre in
build dice già `"Grotta"`. Il primo tentativo, otto toppe agganciate a
`s += lang("洞窟", "Cave")`, era verde in build e rosso al test.

⚠️ **Se la voce è dinamica non serve nessuna toppa**: la resa è l'espressione
intera, quindi l'ordine è già nostro. Guardare lì per primo.

### 2. Una coda «in fondo» è relativa a chi scrive dopo

⚠️ **Il difetto più costoso della sessione, e la catena era verde.** Lo stato
degli oggetti («con benedizione») veniva riversato su `*skipName`, creduto il
punto dove tutti i rami convergono. Non lo è: per il **cibo cotto** il nome del
piatto lo appende `gosub *itemNameSub`, che sta dopo, e a schermo usciva
«un piatto di  con benedizionepane alle noci».

Ora lo stato si appende **prima del controllo di lunghezza a 66 caratteri**, che
è l'ultima riga prima del ritorno di `itemname()`. Materiale ed ego restano su
`*skipName`.

> Prima di riversare una coda, elencare **tutti** i punti che appendono alla
> variabile del nome dopo il candidato. Se ce n'è anche uno solo, il candidato
> non è la fine.

### 3. ⚠️ Non correggere una toppa che qualcuno genera

`toppe.jsonl` è **262 toppe: 230 a mano, 32 da `genera_toppe_nomi.py`, il resto
da `genera_toppe_casuali.py`**. La prima correzione della benedizione fu fatta
sul file: build giusta, verificata, difetto chiuso. Due lotti dopo la
benedizione compariva **due volte**, perché `genera_toppe_nomi` aveva riscritto
la sua versione sopra la modifica.

> Prima di correggere una riga di `toppe.jsonl`, guardare se uno strumento la
> genera. Se sì, la correzione va **nello strumento**.

## Il sistema dei cibi, che è chiuso ma va guardato

`foodname` (`text.hsp:3211-4213`) compone il nome di ogni cibo cucinato: sette
famiglie, ~60 piatti. **Interpola due cose di forma diversa**, e la differenza
decide la resa:

| ramo | interpola | forma | resa |
|---|---|---|---|
| carne | `refchara(id, NAME_ORG)` | **con l'articolo** — «il minotauro» | parentesi: «bistecca (il minotauro)» |
| verdura, frutta, dolci, pesce, pane | `ioriginalnameref` / `fishdatan` | **nuda** — «carota», «carpa» | «di»: «insalata di carota» |

Non è un capriccio: per le **creature** l'articolo sta dentro il nome
(`contratto-nomi.md` §4), per gli **oggetti** lo compone `itemname()`. La
parentesi è l'idioma che il sorgente stesso usa a `item_func.hsp:2159`.

⚠️ Visto in vetrina dal panettiere di Palmia e **tutto giusto** tranne la carne,
che il panettiere non vende. Comportamenti di monte, da **non** riaprire:
«2 sacchi di torta di mele» (il classificatore resta quello dell'ingrediente —
l'oggetto base è un sacco di farina) e «(Rank: 3) con benedizione» (il rango si
infila fra nome e coda; in italiano si legge bene).

## Il tetto di un menu

⚠️ **Il riquadro taglia**: non manda a capo, non restringe il carattere.

Il metro sta nel sorgente: è il terzo argomento che il chiamante passa a
`*prompt_key`. `caratteri = (pixel − 46) / 7,7`. Lo fa `strumenti/larghezze.py`;
`--tutti` elenca i 75 menu col loro tetto. **Va lanciato a ogni lotto di menu.**

⚠️ **La stringa inglese non è il budget**: in dieci menu su venti sfora anche lei.
⚠️ **La larghezza può dipendere dalla lingua**: `450 - 50 * en` vale **400** per
noi, che compiliamo la build inglese.

## Le due righe di `action.hsp` che non si traducono

Sono decisioni, non arretrato, e **vanno scartate a mano quando si compone un
lotto** (`estrai --da-tradurre` le toglie già, ma il conto delle non tradotte le
porta per sempre).

- **`:4584`** — l'articolo inglese davanti al nome di un'arma unica. Toppa.
- **`:9631`** — `his(tc, 1)`, il possessivo che in italiano si omette. Toppa.
  ⚠️ **Il testo di una toppa non passa da `degrada` e non può portare accenti.**

## 391 stringhe fuori perimetro

⚠️ **Un oggetto di Elona ha due nomi, e ne traduciamo uno.** `iknownnameref` è
quello che il gioco mostra **prima dell'identificazione**, e l'estrattore non lo
guarda: `_ASSEGNA_NOME` (`estrai.py:65`) accetta solo `ioriginalnameref`.

**Deciso: si annota e si prosegue col piano.** Il perimetro nuovo si affronta
dopo la Fase 1, e prima si scrive lo strumento che lo misura.
⚠️ Conseguenza: il 100% di `db_item.hsp` e di `custom_tweaks.hsp` **è falso**.

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

⚠️ `lavoro/_r.jsonl` **non si versiona** (è in `.gitignore`): si rigenera.

⚠️ **Una riga può portare più voci, e la riga da sola non è una chiave.** Chi
scrive il lotto deve indicizzare per **(riga, giapponese)**.

⚠️ **La zona di riga non è un dogma**: quando due pezzi si concatenano, il lotto
segue la concatenazione e non la riga.

💡 **Lo script del lotto porta le sue guardie**, e conviene copiarle: rifiuta una
resa che porti ancora `_s(`, `is(`, `your(`, `his(`, e una che metta una
preposizione **fusa** (`al `, `del `, `dalla `…) davanti a un nome interpolato.
E controlla che la resa stia in CP932 **dopo** `degrada`, non prima — «È» non ci
sta, «E'» sì.

## Le regole di resa

Terza persona sempre; mai `_s()`, `is()`, `was()`, `your()`, `have()`,
`does()`, `yourself()`; mai una preposizione davanti a `name()` o `itemname()`,
mentre `con`, `per`, `tra`, `sopra`, `dentro`, `contro` e **`verso`** reggono
(non si fondono con l'articolo); la preposizione sta nel valore, non nella
frase; invarianza di genere prima di tutto; un nome di abilità o di oggetto si
copia, non si traduce; una `statica` si scrive **nuda**, con le virgolette
tipografiche `“”`.

⚠️ **`his(x)` a un argomento si può togliere, `his(x, 1)` no.**

Dalle sessioni recenti:

- **Un prefisso che precede sostantivi di genere diverso può solo essere un
  aggettivo in -e.** Ma se può andare **dopo**, ci va: vedi la regola 1.
- **Nessun participio quando il soggetto non ha genere noto.** 「より強くなった」
  non è «è diventato più forte» ma «sente i muscoli più saldi».
- **`your()` diventa «proprio»**, che concorda con la cosa posseduta: «sente
  crescere la propria forza vitale».
- **Una frase d'amore non porta participi.**
- **In un menu la valuta si abbrevia.**

## Le cose da non riscoprire

### Il giapponese arbitra sul significato, il codice sullo stato del gioco

⚠️ Due quiz (`text.hsp:998` e `:1214`) portano **lo stesso giapponese** ma hanno
risposte giuste diverse. Ad arbitrare non è nessuna delle due lingue:
`map.hsp:2271` mette Azzrssil nel forte `<Collapsed>` e `map.hsp:9009` mette
Ulzassil in quello `<Hell>`. Le risposte combaciano con **l'inglese**: lì il
copia-incolla è del giapponese, e le rese in dizionario sono giuste. **Non
toccarle.**

### Se l'inglese rende un nome in più modi, vince quello della prosa

⚠️ ルストール compare tre volte e l'inglese lo rende `Lustor` (prosa,
`chat.hsp:13645`), `Rust Plaza` (etichetta) e `Ruoza` (esca di quiz) — e `Ruoza`
è **già** il nome di ルオザ. Prima di accettare un nome proprio dall'inglese,
cercare il suo giapponese **in tutto il sorgente**.

### Metà delle voci di menu erano già decise altrove

Cercare **prima** di scrivere: i tipi di negozio, gli elementi, i verbi della
pianta, gli assetti tattici, le parti del corpo (`bodyn`), il tipo di Nefia
(`_nefiatype`).

### Aggiungere una funzione che l'inglese non aveva non si può

`verifica` confronta l'elenco delle interpolazioni. Si possono **togliere** le
morfologiche, non se ne possono **aggiungere**.

### La frase di combattimento vive in due file

`action.hsp` scrive «… e» e imposta `gdata(GDATA_DMG_TYPE) = 2`;
`chara_func.hsp:6323` legge il flag e stampa il resto con `txtcontinue`.
`init.hsp:1666` aggiunge già lo spazio: **la giuntura non va spaziata a mano**.

### Le stringhe che sembrano testo e sono codice

`EN` (`action.hsp:4816`) è una chiave; ` Lv` (`action.hsp:12383`) è ciò che il
gioco cerca in coda al nome per togliere il suffisso di livello. **Prima di
tradurre una stringa corta, guardare chi la consuma.**

### Le altre, invariate

- la carta di `db_card.hsp` dice cosa la creatura rappresenta;
- l'articolo sta sulla testa del sintagma, non sulla persona;
- `ドレイク` è «draco», confermato a schermo;
- un nome già preso non si può riusare, **e vale anche per le esche del quiz**.

## L'ordine che resta

1. **`text.hsp`**, 519 firme dal 70% in su, da riga 4213;
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

⚠️ **`Cyber Dome` fu deciso sull'inglese.** Il giapponese è アクリ・テオラ, un
nome **opaco** che per la regola dei nomi propri resterebbe invariato. La resa è
già in `db_creature.hsp`: riaprirla tocca più file. Segnalata, non toccata.

⚠️ **`spawn_item` ha prodotto due volte l'oggetto sbagliato**, poi ha ripreso.
L'unica pista è lo stato dei filtri: `spawn_item` **non chiama `flt`**, mentre
`spawn_set_item` sì.

⚠️ **La toppa dell'ordine delle Nefia rompe l'ordine giapponese**, dove il
genitivo precede. Innocuo finché compiliamo la build inglese; se un giorno se ne
facesse una giapponese, le due toppe vanno escluse.

## Cose che valgono sempre

⚠️ **Il sorgente è pinnato al tag `2.31.2.0`**, e l'integrità si verifica col
manifesto SHA-256, **mai** con `git status`, che in quel clone è permanentemente
sporco. Gli hash del manifesto sono in MAIUSCOLO.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp`; chi copia nomi di creatura fuori da
`db_creature.hsp`; chi confronta un letterale contro un valore tradotto.

⚠️ **CP932 non codifica tutto.** Niente `«»` (si usano le tipografiche `“”`),
niente dieresi tedesche, niente `å`. Gli accenti veri si scrivono nel dizionario
e li degrada `applica`; ⚠️ **guardare dove cade l'accento**: a fine parola è
gratis, a metà no. ⚠️ **Le toppe non passano da `degrada`**.

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

⚠️ La copia fallisce se il gioco è aperto — successo due volte in una sessione.
⚠️ Se `applica` viene interrotta lascia l'albero di build **incompleto**, e
`compila` poi dice «main.hsp non è in ...»: si rilancia `applica` e basta.

⚠️ **Controllare la data dell'exe prima di fidarsi di uno screenshot.**

**L'eseguibile in `cgx-test.exe` è aggiornato a fine ventiduesima sessione
(11/08/2026 01:26).**

### La console di debug

**Si apre con F12** (`main.hsp:3322`; F11 è `dump_chara`). Esce con ESC. Parte in
modalità **HSP, non Lua**: `spawn_chara <id>` funziona subito.

ID di creatura: **165** il cane e **50** il segugio → la zanna d'argento;
**267** il cavallo zoppo → l'unicorno; **386** la giraffa → il Kirin; **210** la
sorella gatta minore; **482** Yacatect.

`spawn_item <id>` lascia l'oggetto **per terra**: si raccoglie con `,`.
ID utili: **256** l'attrezzo da cucina portatile, **204** il cadavere generico,
**746** la frusta da domatore, **1249** l'Aurtehom, **1097** la banca di
Yacatect, **1180** la tessera YacaPoint, **1068** il cuore del crepuscolo,
**907** il kit del cioccolato, 1037 l'occhio elementale, 1023 il kit di pronto
soccorso, 684 la macchina genetica.
⚠️ **`733` è il sacco da boxe**, non un cibo. Verificare un ID in
`defines/mod.hsp` prima di darlo.

⚠️ **`spawn_item` non può produrre un piatto cucinato**: il nome composto esce
solo se `INV_ITEM_PARAM2` è diverso da zero, e `item.hsp:2694-2705` lo riempie
solo quando il cibo nasce **dentro un negozio** (`MODELIST_SHOP`, cotto una
volta su due) o quando lo **cucini tu**.

⚠️ **Generare mostri a mano è un modo pessimo di provare l'evoluzione**:
`chara.hsp:2319` la tira con `rnd(300) < gdata(GDATA_LEVEL)`, dove
`GDATA_LEVEL` è **il piano del dungeon**. La prova buona è entrare in una
**Nefia profonda** con *Spawn evolved enemies* su **always**.

### Dove sta il cibo cotto

I venditori di cibo veri (`ROLE_SHOP_FOOD`) stanno a **Porto Kapul**, **Ol-dran**
e sul **dirigibile**. A Palmia c'è solo il **panettiere** (`ROLE_SHOP_BAKERY`,
`map.hsp:2571`), che tiene pane e pasta. Il negozio generico non tiene cibo:
`FILTER_CARGO_FOOD` è merce da trasporto.

### Il collaudo, punto per punto

- ✅ **L'evoluzione degli alleati**, ✅ **i nomi a schermo**, ✅ **«draco»**,
  ✅ **il combattimento in italiano**, ✅ **il menu degli ordini al compagno**,
  ✅ **il libro dell'abisso**: provati.
- ✅ **I quattro menu a oggetto** (banca, YacaPoint, difficoltà, cioccolato) e
  ✅ **la vetrina del panettiere**: provati il 2026-08-11.
- ❌ **L'evoluzione dei nemici**: **mai vista**. È la prova mancante più vecchia.
- ❌ **La carne fra parentesi**: mai vista. È il primo punto di questa ripresa.
- 🆕 **Da provare**: i nomi delle Nefia sulla mappa del mondo con l'ordine nuovo
  («Miniera Fatale»), le descrizioni delle località di South Tyris, il gioco di
  carte, la banca.
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
| nome di oggetto | 66 | oltre, passa da `zentohan` | `item_func.hsp:2254` |

⚠️ Il nome di creatura compare in messaggi **senza limite**. Il più lungo del
dizionario è `<Ratin> l'investigatrice della Gilda dei Guerrieri`, 50 caratteri:
visto a schermo, non tronca.

Vedi [[l-ordine-di-una-concatenazione-si-toppa]],
[[correggere-il-generatore-non-il-generato]],
[[genere-ignoto-si-risolve-col-complemento]], [[larghezza-per-campo]],
[[una-guardia-vale-solo-dove-guarda]], [[guardia-troppo-severa]],
[[il-testo-dentro-la-stringa-non-e-codice]],
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
