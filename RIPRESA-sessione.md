# Ripresa sessione

Aggiornato: 2026-08-11, fine della venticinquesima sessione.

## La prima cosa da fare

Si va avanti su **due fronti insieme**, e il secondo è nuovo:

1. **`proc.hsp`**, a 127 su 1.098, per zona di riga dalla **riga 1716** in avanti
   (le esibizioni sono chiuse fino a 1665; 1716-1780 sono le reazioni degli dèi
   alla predica, ancora da fare);
2. **le battute di `db_creature.hsp`**, 1.919 da fare, per **creatura intera**.
   Lo strumento che compone il lotto sta più sotto.

⚠️ **Perché le battute sono salite di priorità.** Erano al punto 7 dell'ordine,
ultime. Uno screenshot del 2026-08-11 ha mostrato che il log del gioco è
**dominato** da quattro battute inglesi del menestrello ripetute una ventina di
volte in due ore, in mezzo a un log per il resto italiano. Un nome di creatura si
legge **una volta**, quando la incontri; una battuta oziosa **a ogni turno** in
cui la creatura ti sta accanto. Vedi `decisioni.md`, 2026-08-11.

### Le sei verifiche d'apertura

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 385 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 2466, doppie 0, senza razza 0
python -m strumenti.larghezze              # atteso: 0 fuori misura su 75 menu
python -m strumenti.diario                 # atteso: 0 fuori misura su 214 siti
```

⚠️ **`creature` dice ora `voce 2466`, non `voce 320`.** Il numero vecchio era
sbagliato, non è cambiato il sorgente: vedi il difetto 2 qui sotto.

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.606 | 1.606 | **100%** |
| `item_data.hsp` | 318 | 318 | **100%** |
| `skill.hsp` | 885 | 885 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `action.hsp` | 1.286 | 1.288 | **100%** (le 2 mancanti sono rinviate a toppa) |
| `text.hsp` | 1.718 | 1.720 | **100%** (le 2 mancanti aspettano `talk.txt`) |
| `proc.hsp` | **127** | 1.098 | 12% |
| `command.hsp`, `trait.hsp` | 0 | ~1.680 | 0% |
| **totale Fase 1** | **5.952** | **8.604** | **69%** |

⚠️ Il denominatore di Fase 1 è **8.604**, non 8.624: qui c'era scritto il numero
vecchio, calcolato quando `text.hsp` contava 1.740 firme invece di 1.720.

`db_creature.hsp`: 1.680 su 3.655 — **1.131 nomi** (chiusi), **546 battute**,
1.919 battute da fare, 56 dinamiche fuori classificazione.
Altri fuori Fase 1: `custom_enemyevolution.hsp` **chiuso**; `ai.hsp` 6 su 100;
`event.hsp` 5 su 654; `chara_func.hsp` 45 su 331; `init.hsp` 6 su 133.

**381 test**, prova d'identità **72/72 e 27.813**, **10.440 sostituzioni**, il
compilatore non dice nulla.

## Le tre scoperte della venticinquesima sessione

Tutte e tre della stessa forma: **una guardia verde perché misurava qualcosa di
adiacente a ciò che doveva misurare.**

### 1. `name(cc)` e `name(tc)` erano la stessa cosa per ogni controllo

`proc.hsp:763` faceva **tirare il sasso all'artista** invece che allo spettatore.
`funzioni_di_contenuto` confronta i **nomi** delle chiamate, e i due nomi sono
entrambi `name`; il compilatore tace perché `cc` e `tc` sono variabili valide.

La guardia nuova, `chiamate_di_contenuto` (`funzioni.py`), confronta la chiamata
**intera con gli argomenti**, e `verifica.py` pretende che ogni chiamata
dell'italiano compaia identica **nell'inglese oppure nel giapponese**.

⚠️ **L'unione delle due, non il solo inglese**: i due rami di `lang()` a volte
scelgono soggetti diversi per lo stesso evento (`action.hsp:1698`), e pretendere
l'inglese rifiuterebbe una resa giusta.

### 2. `creature.py` classificava 320 battute su 2.466

`_LANG` pretendeva un letterale nudo dopo il giapponese, ma **il ramo inglese di
una battuta sta dentro `cnvtalk()`**: 2.939 firme su 5.717 restavano senza
classe, e `nessuna_firma_in_due_classi` girava a vuoto su **metà del file**.

⚠️ **Il test pinnato non poteva accorgersene**: era scritto sul numero che il
codice produceva. Il test nuovo misura il **sorgente** — 1.565 righe `txt lang(`,
1.304 con `cnvtalk` — e non le uscite dello strumento.

> Un test pinnato su un numero che lo strumento produce è una fotografia, non una
> misura.

### 3. ⚠️ La cifra dopo il ♪ non arriva a schermo

`msg_write` (`init.hsp:1372-1386`) legge il carattere **subito dopo** il ♪ come
indice dell'icona e poi **lo toglie dal testo** (riga 1382). Upstream lo usa di
proposito — `item.hsp:3954` scrive `"Wow♪1 Zaaaako♪1♪1♪1 "` — quindi è una
notazione, non un difetto di monte. Ma una cifra che ci finisse per caso
sparirebbe **in silenzio**: il ♪ è l'unico due-byte ammesso, quindi passa
`doppi_byte_cp932` per costruzione.

⚠️ **Quattro delle dieci righe con `♪<cifra>` stanno in `item.hsp`**, che non è
ancora tradotto: la trappola è davanti a noi. La guardia pretende che un
`♪<cifra>` italiano venga da monte.

## Il metodo per le battute di `db_creature.hsp`

⚠️ **Il lotto prende creature intere**, tutte e cinque le classi insieme
(`FLAVOR_PASSIVE`, `_ANGERED`, `_DEATH`, `_KILL`, `_WELCOME`). Il registro di un
mostro è uno, e scriverne una situazione per volta spezza la voce.

Lo strumento è **`strumenti/battute.py`**, scritto in chiusura di sessione: legge
`lavoro/_c.jsonl`, associa a ogni riga il suo `dbid` e il suo `dbmode` risalendo
il sorgente, e stampa il repertorio di ogni creatura col **nome italiano** già
deciso in Fase 2 accanto.

```powershell
python -m strumenti.estrai db_creature.hsp --da-tradurre --uscita lavoro/_c.jsonl
python -m strumenti.battute --conto      # 1.975 voci su 349 creature
python -m strumenti.battute              # il lotto: ~60 voci, e dice --da del prossimo
python -m strumenti.verifica lavoro/<lotto>.jsonl
python -m strumenti.reimporta lavoro/<lotto>.jsonl
python -m pytest strumenti/tests -q
python -m strumenti.prova_identita
python -m strumenti.creature
python -m strumenti.genera_toppe_nomi
python -m strumenti.genera_toppe_casuali
```

I lotti fatti sono `fase2-battute-001` … `-004`, 228 rese su 37 creature, in
ordine di riga. Dopo aver rigenerato l'estrazione, `--conto` dice quanto resta e
il referto senza argomenti dà il lotto successivo: si riparte da `[0]`, perché le
creature già fatte spariscono dall'estrazione.

💡 Le guardie che gli script dei quattro lotti portavano, e che conviene copiare:
niente morfologia inglese residua; nessun carattere a due byte tranne `♪`;
nessun **participio che concorderebbe col giocatore** (`bentornato`, `tornato`,
`stanco`, `ferito`, `sicuro`…); nessun **articolo davanti a `_onii`**; e se
l'inglese finisce con uno spazio, la resa lo tiene.

## Le regole di resa

Terza persona sempre; mai `_s()`, `is()`, `was()`, `your()`, `have()`,
`does()`, `yourself()`; mai una preposizione davanti a `name()` o `itemname()`,
mentre `con`, `per`, `tra`, `sopra`, `dentro`, `contro` e `verso` reggono; la
preposizione sta nel valore, non nella frase; invarianza di genere prima di
tutto; un nome di abilità o di oggetto si copia; una `statica` si scrive **nuda**,
e se deve citare usa `\"`, **mai** le tipografiche.

⚠️ **`his(x)` a un argomento si può togliere, `his(x, 1)` no.**

### Dalle battute, che sono regole nuove

⚠️ **Il giocatore è l'interlocutore, e non ha genere noto.** La regola del diario
valeva per la prima persona; nelle battute vale per la **seconda**, ed è più
insidiosa perché «Welcome home!» chiede un participio. Le rese sono «Eccoti a
casa!», «Rieccola a casa.», «Eccoti di ritorno.». Vale anche per i **vocativi**:
`sir` sparisce, `You thief!` è «Al ladro!», `Die thief` è «Muori, canaglia».

💡 **Il registro può risolvere il genere.** Il maggiordomo dà del **lei**: è il
suo tono, e per di più non concorda mai.

**Un verso si rende in ortografia italiana, non si copia dall'inglese**, che
romanizza il katakana a modo suo. `Beep` sta a `Bip` come `Woof` sta a `Bau` — e
`Woof..` traduce l'ululato 「ワオーン…」, quindi è «Auuuh...». Dove il giapponese
identifica l'animale la resa lo segue: 「キーキー！」 su una **cavia** è «Squit».

**Il ♪ che l'inglese ha perso si rimette**, ed è l'unico due-byte permesso.
✅ Verificato a schermo il 2026-08-11: esce come icona.

⚠️ **`_onii` cambia genere col giocatore.** `text.hsp:111` è
`_onii = lang("お兄", "Big bro"), lang("お姉", "Big sis")` — «Fratellone» /
«Sorellona» — e ha **36 siti di chiamata**, 24 in `db_creature.hsp`. Davanti non
ci va un articolo: «a Fratellone» sì, «al mio Fratellone» no. A differenza di
`name()` **non porta l'articolo dentro**, quindi la preposizione nuda regge.

⚠️ **Quando una concatenazione si spezza in due `lang()`** — `db_creature.hsp:49879`
— i due frammenti sono **un lotto solo**: il primo decide cosa il secondo può
dire. E se il secondo frammento resterebbe identico all'inglese, gli si fa
portare qualcosa che il giapponese ha e l'inglese ha perso.

### Dalle sessioni precedenti

- **Il giocatore non ha genere noto.** Non «sono sopravvissuto» ma «sono ancora
  in piedi»; non «quando sono pronto» ma «quando sarà tutto pronto».
- **Un elenco di compiti si rende all'infinito** («Bere qualcosa»).
- Un prefisso davanti a sostantivi di genere diverso può solo essere un aggettivo
  in -e. Ma se può andare **dopo**, ci va.
- **Nessun participio quando il soggetto non ha genere noto.** 「より強くなった」
  non è «è diventato più forte» ma «sente i muscoli più saldi».
- **`your()` diventa «proprio»**, che concorda con la cosa posseduta.
- **In un menu la valuta si abbrevia.**

## Le cose da non riscoprire

### Una stringa che il giocatore legge può stare fuori da `lang()`

Sette intestazioni del diario (`command.hsp:2854, 2865, 2883, 2895, 2916, 2952,
3114`) erano inglesi **anche nella build giapponese**. Toppate **a mano**: un
generatore riscriverebbe sopra.

### Il nome di una funzione può mentire

`cnvarticle` (`init.hsp:173`) **non mette un articolo**: avvolge il nome fra
parentesi quadre. `cnvitemname` compone `X of Y` col `" of "` cablato fuori da
`lang()` — già toppato in `" di "`. E `cnvtalk` (`init.hsp:170`) non fa altro che
avvolgere fra virgolette: **è per questo che il testo dentro conta come
contenuto**, e la classificazione di `creature.py` doveva vederlo.

### Una preposizione può agire a venti righe di distanza

`s(12)` si compone a `text.hsp:11837` e finisce dopo «da » a `:11859`.

### Il giapponese arbitra sul significato, il codice sullo stato del gioco

⚠️ Il diario dice スライム (`text.hsp:10019`), ma il dialogo di Miches dice プチ,
e i putit sono quello che il giocatore trova in casa. Vince il codice.

⚠️ Due quiz (`text.hsp:998` e `:1214`) portano **lo stesso giapponese** con
risposte diverse: arbitrano `map.hsp:2271` e `:9009`. **Non toccarle.**

### Se l'inglese rende un nome in più modi, vince quello della prosa

⚠️ ルストール è `Lustor` (prosa), `Rust Plaza` (etichetta) e `Ruoza` (esca di
quiz) — e `Ruoza` è **già** il nome di ルオザ. Cercare il giapponese in **tutto**
il sorgente prima di accettare un nome proprio dall'inglese.

### L'ordine di una concatenazione non è un vincolo: si toppa

⚠️ Ma una toppa si aggancia **solo a una riga senza `lang()`**, perché il test la
prova contro il sorgente pinnato. ⚠️ Se la voce è **dinamica** non serve nessuna
toppa: l'ordine è già nostro. E `funzioni_di_contenuto` confronta le
interpolazioni **ordinate**, quindi riordinare è permesso.

### Non correggere una toppa che qualcuno genera

`toppe.jsonl` è in larga parte generato (l'11/08: 33 + 213 generate contro
237 + 57 a mano). **Se uno strumento la genera, la correzione va nello
strumento.**

### Metà delle voci di menu erano già decise altrove

Cercare **prima** di scrivere: tipi di negozio, elementi, verbi della pianta,
assetti tattici, parti del corpo (`bodyn`), tipo di Nefia (`_nefiatype`),
categorie di filtro (`fltname`). E per le battute: i **nomi delle creature** sono
già tutti in dizionario, e vanno tenuti sotto gli occhi mentre si scrive la voce.

### Aggiungere una funzione che l'inglese non aveva non si può

Si possono **togliere** le morfologiche, non se ne possono **aggiungere**.

### La frase di combattimento vive in due file

`action.hsp` scrive «… e» e imposta `gdata(GDATA_DMG_TYPE) = 2`;
`chara_func.hsp:6323` legge il flag e stampa il resto. `init.hsp:1666` aggiunge
già lo spazio: **la giuntura non va spaziata a mano**.

### Le stringhe che sembrano testo e sono codice

`EN` (`action.hsp:4816`, `text.hsp:9361`) è la chiave che `*convert_talk` cerca in
`data/talk.txt`. ` Lv` (`action.hsp:12383`) è ciò che il gioco cerca in coda al
nome. **Prima di tradurre una stringa corta, guardare chi la consuma.**

### Un letterale può essere l'operando di un confronto fra due file

⚠️ `Party Room` (`proc.hsp:1123`) è confrontato col nome della mappa che
**assegna `map_rand.hsp:1287`**, fuori perimetro. Tradurre solo il confronto lo
fa fallire in silenzio: il ballo nella sala delle feste torna a 4 turni invece di
41. **Rinviata**, come `evold`/`evname` con `db_creature.hsp`.

### Le altre, invariate

- la carta di `db_card.hsp` dice cosa la creatura rappresenta;
- l'articolo sta sulla testa del sintagma, non sulla persona;
- `ドレイク` è «draco», confermato a schermo;
- un nome già preso non si può riusare, **e vale anche per le esche del quiz**.

## Il sistema dei cibi, che è chiuso ma va guardato

`foodname` (`text.hsp:3211-4356`) compone il nome di ogni cibo cucinato: otto
famiglie, ~70 piatti. **Interpola due cose di forma diversa:**

| ramo | interpola | forma | resa |
|---|---|---|---|
| carne, **uova e formaggio** | `refchara(id, NAME_ORG, 1)` | **con l'articolo** | parentesi: «bistecca (il minotauro)» |
| verdura, frutta, dolci, pesce, pane | `ioriginalnameref` / `fishdatan` | **nuda** | «di»: «insalata di carota» |

⚠️ Visto in vetrina dal panettiere di Palmia e **tutto giusto** tranne la carne,
che il panettiere non vende. Comportamenti di monte, da **non** riaprire:
«2 sacchi di torta di mele» e «(Rank: 3) con benedizione».

## Il tetto di un menu

⚠️ **Il riquadro taglia**: non manda a capo, non restringe il carattere. Diverso
da `talk_conv`, che manda a capo (e lascia scappare l'ultima parola).

Il metro è il terzo argomento passato a `*prompt_key`:
`caratteri = (pixel − 46) / 7,7`. Lo fa `strumenti/larghezze.py`; `--tutti`
elenca i 75 menu. **Va lanciato a ogni lotto di menu.**

⚠️ **La stringa inglese non è il budget**: in dieci menu su venti sfora anche lei.
⚠️ **La larghezza può dipendere dalla lingua**: `450 - 50 * en` vale **400**.

⚠️ **`talk_conv` manda a capo ma l'ultima parola scappa** (`init.hsp:1326-1369`,
difetto di monte). `strumenti/diario.py` lo misura: tetto **36**, 214 siti. **Va
lanciato a ogni lotto che tocchi il diario o le notizie.** Il verso giusto è
**accorciare, non imbottire** — ma quando la riga si compone a runtime
l'intuizione «più corto è meglio» è **sbagliata**: `monete d'oro` (29 nel caso
peggiore) batte `oro` (36), perché la frase più lunga provoca l'a capo prima.

## Le due righe di `action.hsp` che non si traducono

Sono decisioni, e **vanno scartate a mano quando si compone un lotto**.

- **`:4584`** — l'articolo inglese davanti a un'arma unica. Toppa.
- **`:9631`** — `his(tc, 1)`, il possessivo che in italiano si omette. Toppa.
  ⚠️ **Il testo di una toppa non passa da `degrada` e non può portare accenti.**

## 391 stringhe fuori perimetro

⚠️ **Un oggetto di Elona ha due nomi, e ne traduciamo uno.** `iknownnameref` è
quello prima dell'identificazione, e l'estrattore non lo guarda
(`estrai.py:65` accetta solo `ioriginalnameref`). **Deciso: si annota e si
prosegue.** Conseguenza: il 100% di `db_item.hsp` e `custom_tweaks.hsp` **è
falso**.

⚠️ **E un secondo perimetro fuori: `data/talk.txt`** (86 KB), che non passa da
`lang()` — `SPEC.md:436`. Due voci di `text.hsp` (`:6924`, `:8178`) sono rinviate
lì.

## L'ordine che resta

1. **`proc.hsp`**, 971 firme, per zona di riga da **1716**;
2. **le battute di `db_creature.hsp`**, 1.919, per creatura intera — **salite di
   priorità il 2026-08-11**, vedi in cima;
3. `command.hsp`, `trait.hsp`;
4. `ai.hsp` (94) ed `event.hsp` (649);
5. `chara_func.hsp`, le 286 rimanenti — ⚠️ dentro ci sono le tre pietre di
   Lesimas e l'ankh del sole, **già rese** in `text.hsp:11576-11594` e in
   `glossario.md`: si **copiano**. E la causa di morte (`:6850`), che va insieme a
   `main.hsp:4409`;
6. `init.hsp` (133) — ⚠️ lì sta la decisione sul possessivo `his(x, 1)`, 36 siti.
   Vedi `decisioni.md`, 2026-08-10;
7. i nomi non identificati di `db_item.hsp` e le 2.555 descrizioni.

## Domande aperte

⚠️ **`Cyber Dome` fu deciso sull'inglese.** Il giapponese è アクリ・テオラ, nome
**opaco** che per la regola resterebbe invariato. Segnalata, non toccata.

⚠️ **`spawn_item` ha prodotto due volte l'oggetto sbagliato**, poi ha ripreso.
L'unica pista è lo stato dei filtri: `spawn_item` **non chiama `flt`**.

⚠️ **La toppa dell'ordine delle Nefia rompe l'ordine giapponese.** Innocuo finché
compiliamo la build inglese.

⚠️ **`diario.py` non vede le righe che si compongono a runtime.** Quelle vanno
misurate a mano, e il caso peggiore va cercato su **tutte** le lunghezze
dell'interpolazione.

⚠️ **Le 56 dinamiche di `db_creature.hsp` restano fuori classificazione.** È
corretto — `creature.py` classifica i letterali — ma vuol dire che
`nessuna_firma_in_due_classi` non le copre. Nessuna di esse è oggi un nome.

## Cose che valgono sempre

⚠️ **Il sorgente è pinnato al tag `2.31.2.0`**, e l'integrità si verifica col
manifesto SHA-256, **mai** con `git status`, che in quel clone è permanentemente
sporco. Gli hash del manifesto sono in MAIUSCOLO.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp`; chi copia nomi di creatura fuori da
`db_creature.hsp`; chi confronta un letterale contro un valore tradotto.

⚠️ **CP932 non codifica tutto, e quello che codifica non è detto si veda.**
Niente `«»` (non le codifica); e niente `…`, `“”`, `・`, `《》` (le codifica su
**due byte**, e la build inglese ne disegna uno per byte). Unico ammesso: `♪`.
Gli accenti veri si scrivono nel dizionario e li degrada `applica`;
⚠️ **guardare dove cade l'accento**: a fine parola è gratis, a metà no.
⚠️ **Le toppe non passano da `degrada`.**

⚠️ Un guardiano dell'ambiente blocca i messaggi di commit che contengono `/man/`
letto come percorso: passare il testo con `git commit -F <file>`.

⚠️ **La shell mangia il backtick, e un heredoc lungo in bash si rompe.** Scrivere
un documento che contiene codice fra apici inversi **da un file**, non da riga di
comando: si scrive il pezzo in un file e lo si accoda con tre righe di Python.

## Per rifare la prova in gioco

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -Force
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

⚠️ La copia fallisce se il gioco è aperto — è successo **due volte** l'11/08.
⚠️ Se `applica` viene interrotta lascia l'albero di build **incompleto**, e
`compila` poi dice «main.hsp non è in ...»: si rilancia `applica` e basta.

⚠️ **Controllare la data dell'exe prima di fidarsi di uno screenshot.**

🔴 **`cgx-test.exe` è fermo alla build delle 18:50 dell'11/08 e NON contiene il
quarto lotto di battute** (`fase2-battute-004`): la copia è fallita col gioco
aperto. Il binario giusto è già compilato in
`C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe`: **la prima
cosa da fare a gioco chiuso è ricopiarlo.**

### La console di debug

**Si apre con F12** (`main.hsp:3322`; F11 è `dump_chara`). Esce con ESC. Parte in
modalità **HSP, non Lua**: `spawn_chara <id>` funziona subito.

ID di creatura: **165** il cane, **50** il segugio, **267** il cavallo zoppo,
**386** la giraffa, **210** la sorella gatta minore, **482** Yacatect,
**326** il menestrello, **9** il mendicante.
Dalle battute tradotte: **1066** `<Sist>`, **1048** la giovane rondine,
**1047** l'ape magica, **964** il maggiordomo, **1043** `<Imarituka>`,
**1005** il professore champignon, **1025** la mano bianca che chiama,
**1014** `<Mikraanesis>`, **1008** la cthulhick, **1042** `<Telhureza>`,
**1044** `<Oxode>`, **1045** `<Scard>`, **1052** la signorina di ottanta piedi.

`spawn_item <id>` lascia l'oggetto **per terra**: si raccoglie con `,`.
ID utili: **256** l'attrezzo da cucina portatile, **204** il cadavere generico,
**740** la `<Conchiglia Ignota>`, **746** la frusta da domatore, **1249**
l'Aurtehom, **1097** la banca di Yacatect, **1180** la tessera YacaPoint,
**1068** il cuore del crepuscolo, **907** il kit del cioccolato, 1037 l'occhio
elementale, 1023 il kit di pronto soccorso, 684 la macchina genetica.
⚠️ **`733` è il sacco da boxe**, non un cibo. Verificare un ID in
`defines/mod.hsp` prima di darlo.

⚠️ **`spawn_item` non può produrre un piatto cucinato**: il nome composto esce
solo se `INV_ITEM_PARAM2` è diverso da zero, e `item.hsp:2694-2705` lo riempie
solo dentro un negozio o quando **cucini tu**.

⚠️ **Generare mostri a mano è un modo pessimo di provare l'evoluzione**:
`chara.hsp:2319` la tira con `rnd(300) < gdata(GDATA_LEVEL)`, dove
`GDATA_LEVEL` è **il piano del dungeon**. La prova buona è una **Nefia profonda**
con *Spawn evolved enemies* su **always**.

### Come si provano le battute

`ai.hsp:766` chiede `cdata(CDATA_TXT, cc) != 0`, e `db_creature.hsp` lo
incrementa **una volta per ogni classe di battuta che la creatura possiede**:
l'interruttore è acceso per costruzione. Poi serve stare **entro dieci caselle**,
e la battuta esce ogni **5 turni con probabilità 1 su 4** (`ai.hsp:768-771`).
Si aspetta tenendo premuto `5`.

Le pacifiche danno le **oziose** e il **bentornato**; le ostili le **offese**, e
uccidendole le **morti**.

⚠️ **Il ballo e la predica dei PNG non escono mai.** `ai.hsp:1654` e `:1668` li
accendono con `CDATA_AI_CALM` a **7** e **8**, e in tutto il sorgente **nessuno
assegna quei due valori**: codice morto. Si vedono solo usando tu le abilità, e
«Danza ammaliante» vuole un talento.

### Come si provano le esibizioni

Le dieci righe del giudizio finale escono **solo se suoni tu** (`proc.hsp:950`
esce subito se non sei il giocatore), e serve l'abilità **Esibizione**, che si
impara dal maestro a **Derphy** o **Porto Kapul** (`command.hsp:9170`, `:9194`).
Controllabile in un tasto: `a`, e cerca «Esibizione».

**Elemosina accorata** si impara da sé svegliandosi con **meno di 500 monete**
(`proc.hsp:4305`); **Predica** con Fede oltre 9 (`chara.hsp:496`).

### Il diario

**Si apre col tasto `j`** (`config.txt:159`). ⚠️ **Le notizie vecchie restano in
inglese**: `newsbuff` sta dentro il salvataggio (`text.hsp:12107`). Contano solo
quelle che nascono dopo.

### Le 169 battute degli dèi, ancora mai viste

⚠️ **Non escono se non si indossa l'amuleto giusto.** `GDATA_GOD_TALK` parte a
**0** (`screen.hsp:8216`) e lo accende **solo** `ENCHANT_GOD_SIGNALS`, che in
tutto il gioco ce l'ha un oggetto solo — `<Conchiglia Ignota>`, `spawn_item 740`
(`db_item.hsp:81492`). E serve **seguire un dio**.

```
F12 → spawn_item 740      raccogli con , e indossa con w
c                          controlla che il personaggio segua un dio
salva, esci, ricarica      → alla prima mossa esce il «bentornato» (main.hsp:3083)
dormi in un letto          → il «sonno» (proc.hsp:4223), e col caso il «sogno»
uccidi qualche mostro      → l'«uccisione», 1 volta su 20 (chara_func.hsp:7896)
offri un oggetto su un altare → «offerta gradita» (god.hsp:990)
j, pagina di sinistra      → le notizie nuove
```

Ci si converte **pregando** (`p`) **sopra un altare**, e ⚠️ **il dio che prendi è
quello dell'altare** (`god.hsp:551`). ⚠️ **`spawn_item 171` non serve**: l'altare
generato dalla console nasce **senza dio** e pregarci rende «unbeliever». Il posto
giusto è la **Terra della tregua** (`AREA_TRUCE_GROUND`), che tiene tutti e otto
gli altari in una sala (`map.hsp:1651-1692`): Mani (10,8), Lulwy (13,8), Opatos
(10,13), Ehekatl (13,13), Itzpalt (20,8), Kumiromi (23,8), Jure (20,13),
Yacatect (23,13). 💡 Conviene **Ehekatl**, che ripete l'ultima parola di ogni
frase: si vede subito se il tic è passato.

### Il collaudo, punto per punto

- ✅ **L'evoluzione degli alleati**, ✅ **i nomi a schermo**, ✅ **«draco»**,
  ✅ **il combattimento in italiano**, ✅ **il menu degli ordini al compagno**,
  ✅ **il libro dell'abisso**, ✅ **i quattro menu a oggetto**, ✅ **la vetrina
  del panettiere**, ✅ **il diario delle missioni**: provati.
- ✅ **Le esibizioni e l'elemosina**: provate il 2026-08-11 con `spawn_chara 326`
  e `spawn_chara 9`. Dieci rese viste, tutte giuste.
- ✅ **Il ♪**: provato il 2026-08-11 con la cthulhick, esce come icona.
- ❌ **«*X* tira un sasso.»**: il difetto riparato, **mai visto**. Serve uno
  spettatore di livello alto rispetto all'artista (`proc.hsp:755`).
- ❌ **L'evoluzione dei nemici**: **mai vista**. È la prova mancante più vecchia.
- ❌ **La carne fra parentesi**: mai vista, e decide **due** famiglie di cibi
  (`text.hsp:3221-3356` e `:4222-4345`). ⚠️ `spawn_item` non basta: serve
  cucinare col **256**, l'attrezzo da cucina portatile, su un cadavere.
- ❌ **Le 169 battute degli dèi**: mai viste, vedi sopra.
- ❌ **Il tocco elementale** (`proc.hsp:8797`): «tocca X con la zanna di veleno».
- 🆕 **Da provare**: le battute dei quattro lotti nuovi (id qui sopra); la
  **bacheca degli incarichi**; i nomi delle Nefia con l'ordine nuovo; il gioco di
  carte; la banca.
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
| **voce di menu** | **(px − 46) / 7,7** | sinistra, taglia | `strumenti/larghezze.py` |
| **riga di diario** | **36** | **manda a capo, ultima parola scappa** | `strumenti/diario.py` |
| **riga di notizia** | **33** | idem | `addnews2`, `text.hsp:12106` |
| **riga del compenso** | **30** | idem | `text.hsp:11885` |
| pagina del diario | ~40 | taglia | osservato a schermo |
| nome di oggetto | 66 | oltre, passa da `zentohan` | `item_func.hsp:2254` |

⚠️ Il nome di creatura compare in messaggi **senza limite**. Il più lungo è
`<Ratin> l'investigatrice della Gilda dei Guerrieri`, 50 caratteri: visto a
schermo, non tronca. **E le battute non hanno tetto**: passano da `txt`, non da
`talk_conv`.

Vedi [[una-procura-non-e-una-proprieta]] — che dal 2026-08-11 porta anche il
nome-di-chiamata usato al posto della chiamata e il test pinnato sull'uscita
dello strumento — [[la-frequenza-non-si-deduce-dal-file]],
[[il-round-trip-non-basta-conta-i-byte]], [[accorciare-non-imbottire]],
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
