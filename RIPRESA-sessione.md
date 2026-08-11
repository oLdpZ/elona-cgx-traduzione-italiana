# Ripresa sessione

Aggiornato: 2026-08-11, fine della ventitreesima sessione.

## La prima cosa da fare

**`text.hsp` è all'89%**: 1.549 firme su 1.740, ne restano **191** (169 in coda a
`estrai --da-tradurre`, le altre sono rinviate o invariate). Si prosegue per zona
di riga da **riga 12121**, col metodo qui sotto.

⚠️ **Prima però c'è un collaudo aperto da due sessioni, e costa due minuti.** La
resa dei cibi di carne mette la creatura **fra parentesi** — «bistecca (il
cane)» — e non è mai stata vista a schermo. Adesso vale il doppio, perché la
ventitreesima sessione ha tradotto la famiglia delle **uova e del formaggio**
(`text.hsp:4216-4342`) e quella interpola `refchara(..., NAME_ORG, 1)`
**esattamente come la carne**: stessa forma, stesso idioma. Se legge male si
cambia in due posti soli (`:3221-3356` e `:4222-4345`).

```
F12 → spawn_item 256      attrezzo da cucina portatile (defines/mod.hsp:5001)
F12 → spawn_chara 165     il cane (defines/mod.hsp:6236)
ESC → uccidi il cane, raccogli con , l'attrezzo e il cadavere
usa l'attrezzo → scegli il cadavere → guarda il nome in inventario
```

### Le sei verifiche d'apertura

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 372 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 320, doppie 0, senza razza 0
python -m strumenti.larghezze              # atteso: 0 fuori misura su 75 menu
python -m strumenti.diario                 # atteso: 0 fuori misura su 214 siti
```

⚠️ `strumenti/diario.py` è **nuovo di questa sessione**: è la sesta verifica e
prima non c'era.

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.606 | 1.606 | **100%** |
| `item_data.hsp` | 318 | 318 | **100%** |
| `skill.hsp` | 885 | 885 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `action.hsp` | 1.286 | 1.288 | **100%** (le 2 mancanti sono rinviate a toppa) |
| `text.hsp` | **1.549** | 1.740 | **89%** |
| gli altri tre | 0 | 2.775 | 0% |
| **totale Fase 1** | **5.656** | **8.624** | **66%** |

Fuori dalla Fase 1: `db_creature.hsp` a 1.452 su 3.655;
`custom_enemyevolution.hsp` **chiuso**; `ai.hsp` 6 su 100; `event.hsp` 5 su
654; `chara_func.hsp` 45 su 331; `init.hsp` 6 su 133.

**372 test** (erano 357), prova d'identità **72/72 e 27.813**, **9.694
sostituzioni**, il compilatore non dice nulla.

## Le due scoperte di questa sessione, che valgono per tutto il progetto

### 1. ⚠️ La build inglese non sa disegnare un carattere a due byte

Il puntino d'elenco 「・」 è uscito a schermo come **`E`**. `init.hsp:1391`
sceglie il carattere con `lang(cfg_font1, cfg_font2)`, e per l'inglese
`cfg_font2` è **Courier New** (`config.txt:75`): `mes` disegna **un glifo per
byte**, e `0x81 0x45` diventa nulla + `E`. I quattro punti che riconoscono un
byte guida (`init.hsp:1295`, `module.hsp:57` e `:4932`, `system.hsp:4050`)
controllano solo dentro `if ( jp )`.

Erano **186 voci**, per due terzi da sessioni vecchie: `…` (130), `“”` (54),
`・` (17), `《》` (1). Riparate tutte.

⚠️ **Questo rovescia una regola che stava scritta qui.** Le virgolette
tipografiche `“”` **non si usano più**: si scrive la virgoletta protetta `\"`,
come fa l'inglese upstream (`text.hsp:9879`). E i puntini di sospensione si
scrivono `...`, non `…`.

⚠️ `non_ascii_residuo` non bastava: chiede se CP932 **sa rappresentare** il
carattere, e `…` lo rappresenta benissimo — su due byte. La guardia giusta conta
i **byte**, ed è `accenti.doppi_byte_cp932()`. Unico ammesso: `♪`, perché
`init.hsp:1374` lo intercetta e ci disegna un'icona (ed è l'unico che si permette
anche l'inglese upstream, una volta in 9.000 stringhe).

### 2. ⚠️ `talk_conv` manda a capo, ma l'ultima parola scappa

Il ramo inglese (`init.hsp:1326-1369`) accumula parole cercando lo spazio
successivo; sull'ultima parola lo spazio non c'è, esce dai due cicli e fa
`talk_conv_arg1 += msgtemp` — **senza controllo di larghezza**. Difetto di
monte: l'inglese lo sfiora, l'italiano ci cade dentro.

`strumenti/diario.py` lo misura: tetto **36** (`40 - en * 4`, con `en` = 1),
simulatore che **riproduce il difetto**, 214 siti. **Va lanciato a ogni lotto
che tocchi il diario o le notizie.**

⚠️ **Il verso giusto è accorciare, non imbottire.** La prima stesura infilava
zeppe («…e le 23:59 *di sera*») per spostare l'a capo: è peggiorare la prosa per
far quadrare il riquadro.

⚠️ **Quando la riga si compone a runtime il misuratore non la vede**, e va fatta
a mano — ma l'intuizione «più corto è meglio» **è sbagliata**: nella riga del
compenso, `monete d'oro` (29 nel caso peggiore) batte `oro` (36), perché la
frase più lunga provoca l'a capo prima e salva la parola finale.

## Il metodo

**I lotti si prendono per zona di riga**, non separando statiche e dinamiche.

```powershell
python -m strumenti.estrai text.hsp --da-tradurre --uscita lavoro/_r.jsonl
# si ordina per (riga, occorrenza) e si prendono le prime ~50
python -m strumenti.verifica lavoro/<lotto>.jsonl
python -m strumenti.reimporta lavoro/<lotto>.jsonl
python -m strumenti.larghezze
python -m strumenti.diario
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
resa che porti ancora `_s(`, `is(`, `your(`, `his(`; una che metta una
preposizione **fusa** davanti a un nome interpolato — ⚠️ ma solo davanti a un
**nome**, perché davanti a un numero «del 12/3/517» è corretto; una che porti un
carattere a **due byte**; e una che sfori il tetto di `talk_conv`.

## Le regole di resa

Terza persona sempre; mai `_s()`, `is()`, `was()`, `your()`, `have()`,
`does()`, `yourself()`; mai una preposizione davanti a `name()` o `itemname()`,
mentre `con`, `per`, `tra`, `sopra`, `dentro`, `contro` e **`verso`** reggono
(non si fondono con l'articolo); la preposizione sta nel valore, non nella
frase; invarianza di genere prima di tutto; un nome di abilità o di oggetto si
copia, non si traduce; una `statica` si scrive **nuda**, e se deve citare usa
`\"`, **mai** le tipografiche.

⚠️ **`his(x)` a un argomento si può togliere, `his(x, 1)` no.**

Dalle sessioni recenti:

- **Il giocatore non ha genere noto.** Il diario è in prima persona: niente
  participio che concordi col soggetto. Non «sono sopravvissuto» ma «sono ancora
  in piedi»; non «quando sono pronto» ma «quando sarà tutto pronto».
- **Un elenco di compiti si rende all'infinito** («Bere qualcosa», «Mangiare
  della carne»): è la forma italiana dell'elenco e non porta genere.
- Un prefisso che precede sostantivi di genere diverso può solo essere un
  aggettivo in -e. Ma se può andare **dopo**, ci va.
- **Nessun participio quando il soggetto non ha genere noto.** 「より強くなった」
  non è «è diventato più forte» ma «sente i muscoli più saldi».
- **`your()` diventa «proprio»**, che concorda con la cosa posseduta.
- **Una frase d'amore non porta participi.**
- **In un menu la valuta si abbrevia.**

## Le cose da non riscoprire

### Una stringa che il giocatore legge può stare fuori da `lang()`

Sette intestazioni del diario (`command.hsp:2854, 2865, 2883, 2895, 2916, 2952,
3114`) erano scritte nude: inglesi **anche nella build giapponese**. Toppate a
mano. ⚠️ **A mano, non generate**: un generatore riscriverebbe sopra.

> Prima di concludere che una stringa è codice, guardare se è semplicemente
> fuori da `lang()`.

### Il nome di una funzione può mentire

`cnvarticle` (`init.hsp:173`) **non mette un articolo**: nella build inglese
avvolge il nome fra parentesi quadre. `cnvitemname` compone `X of Y` col `" of "`
cablato fuori da `lang()` — già toppato in `" di "`.

### Una preposizione può agire a venti righe di distanza

`s(12)` si compone a `text.hsp:11837` e finisce dopo «da » a `:11859`. Reso «il
bersaglio» darebbe «da il bersaglio»; «chi abita a Vernis» no.

### Il giapponese arbitra sul significato, il codice sullo stato del gioco

⚠️ Il diario dice スライム (`text.hsp:10019`), ma il dialogo di Miches
(`chat.hsp:1505`, `:1517`) dice プチ, e i putit sono quello che il giocatore
trova in casa. Vince il codice.

⚠️ Due quiz (`text.hsp:998` e `:1214`) portano **lo stesso giapponese** ma hanno
risposte giuste diverse: arbitrano `map.hsp:2271` e `:9009`. Le rese in
dizionario sono giuste, **non toccarle**.

### Se l'inglese rende un nome in più modi, vince quello della prosa

⚠️ ルストール compare tre volte e l'inglese lo rende `Lustor` (prosa), `Rust
Plaza` (etichetta) e `Ruoza` (esca di quiz) — e `Ruoza` è **già** il nome di
ルオザ. Prima di accettare un nome proprio dall'inglese, cercare il suo
giapponese **in tutto il sorgente**.

⚠️ Caso gemello aperto: il diario dice «Maria» (`text.hsp:11115`) mentre
`db_creature.hsp:76576` dice `<Mary>`. Ho usato **`<Mary>`**, il nome che il
giocatore vede sul PNG.

### L'ordine di una concatenazione non è un vincolo: si toppa

Due toppe da una riga hanno portato ottanta Nefia da «Fatale Miniera» a «Miniera
Fatale». ⚠️ **Ma una toppa può agganciarsi solo a una riga senza `lang()`**,
perché il test la prova contro il **sorgente pinnato**. ⚠️ **Se la voce è
dinamica non serve nessuna toppa**: l'ordine è già nostro.

### Non correggere una toppa che qualcuno genera

`toppe.jsonl` è **270 toppe: 246 generate** (portano il campo `generata`) **e 24 a
mano**. Una correzione fatta sul file è stata riscritta due lotti dopo. Se uno
strumento la genera, la correzione va **nello strumento**.

### Metà delle voci di menu erano già decise altrove

Cercare **prima** di scrivere: i tipi di negozio, gli elementi, i verbi della
pianta, gli assetti tattici, le parti del corpo (`bodyn`), il tipo di Nefia
(`_nefiatype`), le categorie di filtro (`fltname`).

### Aggiungere una funzione che l'inglese non aveva non si può

`verifica` confronta l'elenco delle interpolazioni. Si possono **togliere** le
morfologiche, non se ne possono **aggiungere**.

### La frase di combattimento vive in due file

`action.hsp` scrive «… e» e imposta `gdata(GDATA_DMG_TYPE) = 2`;
`chara_func.hsp:6323` legge il flag e stampa il resto con `txtcontinue`.
`init.hsp:1666` aggiunge già lo spazio: **la giuntura non va spaziata a mano**.

### Le stringhe che sembrano testo e sono codice

`EN` (`action.hsp:4816` e `text.hsp:9361`) è la chiave che `*convert_talk` cerca
in `data/talk.txt` come `%DEFAULT,EN`: in dizionario ha `it == "EN"`.
` Lv` (`action.hsp:12383`) è ciò che il gioco cerca in coda al nome per togliere
il suffisso di livello. **Prima di tradurre una stringa corta, guardare chi la
consuma.**

### Le altre, invariate

- la carta di `db_card.hsp` dice cosa la creatura rappresenta;
- l'articolo sta sulla testa del sintagma, non sulla persona;
- `ドレイク` è «draco», confermato a schermo;
- un nome già preso non si può riusare, **e vale anche per le esche del quiz**.

## Il sistema dei cibi, che è chiuso ma va guardato

`foodname` (`text.hsp:3211-4356`) compone il nome di ogni cibo cucinato: **otto**
famiglie, ~70 piatti. **Interpola due cose di forma diversa**, e la differenza
decide la resa:

| ramo | interpola | forma | resa |
|---|---|---|---|
| carne, **uova e formaggio** | `refchara(id, NAME_ORG, 1)` | **con l'articolo** — «il minotauro» | parentesi: «bistecca (il minotauro)» |
| verdura, frutta, dolci, pesce, pane | `ioriginalnameref` / `fishdatan` | **nuda** — «carota», «carpa» | «di»: «insalata di carota» |

Non è un capriccio: per le **creature** l'articolo sta dentro il nome
(`contratto-nomi.md` §4), per gli **oggetti** lo compone `itemname()`. La
parentesi è l'idioma che il sorgente stesso usa a `item_func.hsp:2159`.

⚠️ Visto in vetrina dal panettiere di Palmia e **tutto giusto** tranne la carne,
che il panettiere non vende. Comportamenti di monte, da **non** riaprire:
«2 sacchi di torta di mele» e «(Rank: 3) con benedizione».

## Il tetto di un menu

⚠️ **Il riquadro taglia**: non manda a capo, non restringe il carattere. Diverso
da `talk_conv`, che manda a capo (e lascia scappare l'ultima parola).

Il metro sta nel sorgente: è il terzo argomento che il chiamante passa a
`*prompt_key`. `caratteri = (pixel − 46) / 7,7`. Lo fa `strumenti/larghezze.py`;
`--tutti` elenca i 75 menu col loro tetto. **Va lanciato a ogni lotto di menu.**

⚠️ **La stringa inglese non è il budget**: in dieci menu su venti sfora anche lei.
⚠️ **La larghezza può dipendere dalla lingua**: `450 - 50 * en` vale **400** per
noi, che compiliamo la build inglese.

## Le due righe di `action.hsp` che non si traducono

Sono decisioni, non arretrato, e **vanno scartate a mano quando si compone un
lotto**.

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

⚠️ **E c'è un secondo perimetro fuori: `data/talk.txt`** (86 KB), che non passa
da `lang()` — `SPEC.md:436`. Due voci di `text.hsp` (`:6924`, `:8178`) sono
rinviate **lì**: sono la sostituzione `<ref>`, il contatore degli ospiti, e la
frase che le incornicia sta in `talk.txt:1633`. Tradurre solo il pezzo darebbe
«You have 3 ospiti waiting for you».

## L'ordine che resta

1. **`text.hsp`**, 191 firme dall'89% in su, da riga 12121 — le **notizie**
   (`addnews2`, tetto **33**) e la coda del file;
2. `proc.hsp` — chiude le 20 rinviate e il gemello di «mordes»;
3. `command.hsp`, `trait.hsp`;
4. `ai.hsp` (94) ed `event.hsp` (649);
5. `chara_func.hsp`, le 286 rimanenti — ⚠️ dentro ci sono le tre pietre di
   Lesimas e l'ankh del sole, **già rese** in `text.hsp:11576-11594` e in
   `glossario.md`: si **copiano**, non si reinventano. E la causa di morte
   (`:6850`), che va insieme a `main.hsp:4409`;
6. `init.hsp` (133) — ⚠️ **lì sta la decisione sul possessivo** `his(x, 1)`, che
   ha 36 siti di chiamata. Vedi `decisioni.md`, 2026-08-10;
7. le 2.203 righe di `db_creature.hsp` e le 2.555 descrizioni di `db_item.hsp`.

## Domande aperte

⚠️ **`Cyber Dome` fu deciso sull'inglese.** Il giapponese è アクリ・テオラ, un
nome **opaco** che per la regola dei nomi propri resterebbe invariato. La resa
«Cupola Cibernetica» è ora anche in `text.hsp:10609`. Segnalata, non toccata.

⚠️ **`spawn_item` ha prodotto due volte l'oggetto sbagliato**, poi ha ripreso.
L'unica pista è lo stato dei filtri: `spawn_item` **non chiama `flt`**, mentre
`spawn_set_item` sì.

⚠️ **La toppa dell'ordine delle Nefia rompe l'ordine giapponese.** Innocuo finché
compiliamo la build inglese; per una build giapponese le due toppe vanno escluse.

⚠️ **`diario.py` non vede le righe che si compongono a runtime.** Misura il
letterale, non `"Compenso: " + soldi + giunzione + categoria`. Quelle vanno
misurate a mano, e il caso peggiore va cercato su **tutte** le lunghezze
dell'interpolazione, non su una.

## Cose che valgono sempre

⚠️ **Il sorgente è pinnato al tag `2.31.2.0`**, e l'integrità si verifica col
manifesto SHA-256, **mai** con `git status`, che in quel clone è permanentemente
sporco. Gli hash del manifesto sono in MAIUSCOLO.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp`; chi copia nomi di creatura fuori da
`db_creature.hsp`; chi confronta un letterale contro un valore tradotto.

⚠️ **CP932 non codifica tutto, e quello che codifica non è detto si veda.**
Niente `«»` (non le codifica); e niente `…`, `“”`, `・`, `《》` (le codifica su
**due byte**, e la build inglese le sbaglia). Gli accenti veri si scrivono nel
dizionario e li degrada `applica`; ⚠️ **guardare dove cade l'accento**: a fine
parola è gratis, a metà no. ⚠️ **Le toppe non passano da `degrada`**.

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

⚠️ La copia fallisce se il gioco è aperto.
⚠️ Se `applica` viene interrotta lascia l'albero di build **incompleto**, e
`compila` poi dice «main.hsp non è in ...»: si rilancia `applica` e basta.

⚠️ **Controllare la data dell'exe prima di fidarsi di uno screenshot.**

**L'eseguibile in `cgx-test.exe` è aggiornato a fine ventitreesima sessione
(11/08/2026 03:21).**

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
solo quando il cibo nasce **dentro un negozio** o quando lo **cucini tu**.

⚠️ **Generare mostri a mano è un modo pessimo di provare l'evoluzione**:
`chara.hsp:2319` la tira con `rnd(300) < gdata(GDATA_LEVEL)`, dove
`GDATA_LEVEL` è **il piano del dungeon**. La prova buona è entrare in una
**Nefia profonda** con *Spawn evolved enemies* su **always**.

### Il diario, che è dove sta il lavoro di questa sessione

**Si apre col tasto `j`** (`config.txt:159`). La pagina delle missioni tiene in
fila i tre blocchi tradotti: trama principale, giornaliere, secondarie.

### Dove sta il cibo cotto

I venditori di cibo veri (`ROLE_SHOP_FOOD`) stanno a **Porto Kapul**, **Ol-dran**
e sul **dirigibile**. A Palmia c'è solo il **panettiere** (`ROLE_SHOP_BAKERY`,
`map.hsp:2571`), che tiene pane e pasta.

### Il collaudo, punto per punto

- ✅ **L'evoluzione degli alleati**, ✅ **i nomi a schermo**, ✅ **«draco»**,
  ✅ **il combattimento in italiano**, ✅ **il menu degli ordini al compagno**,
  ✅ **il libro dell'abisso**, ✅ **i quattro menu a oggetto**, ✅ **la vetrina
  del panettiere**: provati.
- ✅ **Il diario delle missioni**: provato il 2026-08-11 — ha trovato **due
  difetti veri** (i caratteri a due byte e l'ultima parola di `talk_conv`),
  entrambi chiusi con la loro guardia, e il ricontrollo è passato.
- ❌ **L'evoluzione dei nemici**: **mai vista**. È la prova mancante più vecchia.
- ❌ **La carne fra parentesi**: mai vista. È il primo punto di questa ripresa,
  e ora decide due famiglie di cibi.
- 🆕 **Da provare**: la **bacheca degli incarichi** nelle città (colonne
  *Cliente / Luogo / Scadenza / Compenso / Dettagli* e la riga del compenso con
  `, più`); i nomi delle Nefia con l'ordine nuovo; il gioco di carte; la banca.
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
| **riga di diario** | **36** | **manda a capo, ma l'ultima parola scappa** | `talk_conv`, e `strumenti/diario.py` |
| **riga di notizia** | **33** | idem | `addnews2`, `text.hsp:12106` |
| **riga del compenso** | **30** | idem | `text.hsp:11885` |
| pagina del diario | ~40 | taglia | osservato a schermo il 2026-08-11 |
| nome di oggetto | 66 | oltre, passa da `zentohan` | `item_func.hsp:2254` |

⚠️ Il nome di creatura compare in messaggi **senza limite**. Il più lungo del
dizionario è `<Ratin> l'investigatrice della Gilda dei Guerrieri`, 50 caratteri:
visto a schermo, non tronca.

Vedi [[il-round-trip-non-basta-conta-i-byte]], [[accorciare-non-imbottire]],
[[il-difetto-di-monte-lo-paghiamo-noi]],
[[l-ordine-di-una-concatenazione-si-toppa]],
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
