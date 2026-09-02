# Avanzamento

Aggiornato a mano dopo ogni reimportazione. I numeri si rifanno con:

```powershell
python -m strumenti.verifica --dizionario
```

**L'unità è la firma, non l'occorrenza.** Il piano della Fase 1 contava le
occorrenze (2.127 per `text.hsp`), ma il dizionario è indicizzato per contenuto:
una stringa che compare tre volte è **una** voce da tradurre e tre sostituzioni
in fase di build. Tradurre si conta in firme; l'effetto a schermo si vede nelle
occorrenze. Le due colonne stanno qui entrambe perché servono a cose diverse.

| file | tradotte | firme | % | occorrenze |
|---|---|---|---|---|
| `text.hsp` | **1.718** | 1.720 | **100%** | 2.127 |
| `command.hsp` | **795** | 1.304 | 61% | 1.481 |
| `action.hsp` | **1.286** | 1.288 | **100%** | 1.502 |
| `proc.hsp` | **127** | 1.098 | 12% | 1.327 |
| `skill.hsp` | **885** | 885 | **100%** | 894 |
| `trait.hsp` | 0 | 373 | 0% | 406 |
| `db_item.hsp` | **1.828** | 1.828 | **100%** | 1.867 |
| `item_data.hsp` | **318** | 318 | **100%** | 318 |
| `custom_tweaks.hsp` | **12** | 12 | **100%** | 28 |
| **totale** | **5.952** | **8.604** | **69%** | **9.690** |

⚠️ **La riga di `db_item.hsp` è stata rifatta il 2026-08-22 (83ª)**: da 1.606 a
**1.828** firme, e da 1.607 a **1.867** occorrenze. Non sono traduzioni nuove su
un perimetro vecchio: è il **perimetro** che si è allargato di 222 firme e 260
occorrenze, perché `estrai` ha imparato il blocco a sei righe dei **nomi non
identificati** (`contratto-nomi.md` §1-ter). ⚠️ Fino a ieri quel 100% era vero
per la rete che guardava e falso a schermo — la lezione della 53ª, «finito per
quale referto?», su un file che tutti davano per chiuso da quindici sessioni.

⚠️ **Questa tabella è ferma, e la riga di `command.hsp` è l'unica riaggiornata
(2026-08-15, 45ª: 795 su 1.304, più 20 rinviate).** `proc.hsp` dice 12% ed è chiuso dalla 39ª; il totale in
fondo somma valori di sessioni diverse. Il conto vivo lo danno
`python -m strumenti.verifica --dizionario` per il perimetro `lang()` e
`python scratchpad/perimetro.py` per il totale vero, descrizioni degli oggetti e
file di `data/` compresi. Finché nessuno rifà la tabella intera, **si guardano
quelli**.

⚠️⚠️ **E dalla 124ª `perimetro.py` non stampa più una percentuale ricavata da un
rapporto.** Il suo «91%» era sbagliato di dieci punti — contava le descrizioni
degli oggetti **due volte** al denominatore — e il numero che stampa adesso è
una sottrazione: `fatte` e `da fare` contati con lo stesso `estrai`. Chi legge
in giro per questo file un «perimetro 90%, totale 94%» sta leggendo il vecchio
conto, non un arretramento.

## Il fronte delle righe nude si apre: 40 toppe e 14 righe che erano morte — 2026-09-02, centoventiseiesima sessione

Il fronte aperto dalla 125ª scende da **181 a 141** righe vive in una sessione:
40 toppate e 14 dichiarate morte senza tradurne nessuna.

    _126-nudi-nel-ramo-jp   181 vive  ->  141          il numero che conta
    triage_nudi             testo 198 ->  158
    toppe                   1.048     ->  1.088, agganciate 1.088 su 1.088
    pytest                  794 passed, 6 skipped      invariato
    prova_identita          72/72 e 30.905             invariato
    applica                 30.764 sostituzioni        invariato

| blocco | righe | che cos'era |
|---|---|---|
| `proc.hsp` | 14 | le battute delle mosse speciali: provocazione, insulto, `<Clementia>`, il colpo di Ken |
| `item_func.hsp` | 18 | i pezzi di nome degli oggetti: le nove parti del corpo, «decoded», «custom», le code fra parentesi |
| `system.hsp` + `screen.hsp` | 8 | i sette crediti del titolo e l'etichetta «AUTO TURN» |
| `map_rand.hsp` | **9 morte** | un tabellone di parametri dentro un `if ( FALSE )` |
| `item_func.hsp` | **5 morte** | il pluralizzatore inglese, che una nostra toppa aveva già spento |

### ⭐⭐⭐ Una riga può essere morta perché l'abbiamo uccisa noi

La sesta famiglia di riga morta è il blocco spento da una **costante**, e la
guardia va cercata **nella build, non solo nel sorgente**: il pluralizzatore
inglese di `item_func.hsp:1842` nel sorgente ha una guardia vera, e nella build
una nostra toppa l'ha sostituita con `if ( 0 )` perché il plurale italiano viene
da `ioriginalnamerefplur`. Le sue cinque righe restano intatte, quindi il triage
le contava come lavoro: erano morte da sessioni, e per mano nostra.

### ⭐⭐ E le nove parti del corpo erano già decise, in un'altra finestra

`item_func.hsp:1338` compone il nome delle parti necromantiche, e le nove parole
il progetto le aveva già rese nel menu in cui le parti si comprano. ⚠️ «chest»
non è «petto» ma **torso**, e «waist» non è «vita» ma **fianchi**: «vita di
putit» in italiano si legge *la vita del putit*, e su un pezzo di cadavere quella
non è imprecisione, è ambiguità.

## Il primo blocco del fronte: 14 toppe in `proc.hsp` — 2026-09-02, centoventiseiesima sessione

`proc.hsp` teneva **quindici** righe inglesi nude vive: le battute che i
personaggi si dicono addosso quando usano una mossa speciale — la provocazione,
l'insulto, `<Clementia>` e il colpo di Ken il guerriero. Quattordici sono state
toppate, una resta invariata apposta.

### ⭐⭐⭐ Le righe nude avevano una seconda fonte, e nessuno la leggeva

Una riga nuda non ha firma né voce di dizionario, e per questo si legge come se
l'inglese fosse l'unica fonte che ha. Non è vero: quasi sempre il giapponese sta
**tre righe sopra**, dentro il ramo `if ( jp )` di cui quella riga è l'`else`.
`scratchpad/_126-sorella-jp.py` lo misura — **37 righe su 195** ce l'hanno — e
`decisioni.md` racconta perché l'accoppiamento riga-per-riga sbaglia in silenzio.

### ⭐⭐⭐ E letta così, la provocazione diceva le battute dell'insulto

`:19733` e `:19736` stanno sotto `SKILL_SPACT_PROVOKE` — 挑発, il richiamo — e
il loro inglese è **lo stesso identico pool** che sta sotto `SKILL_SPACT_INSULT`
a `:26024` e `:26027`, sette stringhe su sette. Il giapponese delle due mosse
non si somiglia per niente. È il difetto della 119ª alla scala di un pool
intero, e la provocazione si rende dal giapponese; l'insulto resta dall'inglese,
che lì fa quel che deve.

### ⚠️⚠️⚠️ E le toppe erano l'unico italiano che nessuna rete avesse mai letto

`referti.py` legge il dizionario; ogni altra rete guarda le firme, e una toppa
una firma non ce l'ha. Erano **1.062 righe di italiano fuori da ogni referto**.
`scratchpad/_126-referti-toppe.py` ci gira sopra i due referti di `referti.py`, e
alla prima passata ha trovato **due participi maschili riferiti al giocatore** —
in `command.hsp` e `custom_tweaks.hsp`, tutt'e due di sessioni vecchie, dietro
una catena tutta verde. Corretti.

## Il perimetro `lang()` si chiude al 100%: 167 rese in tre file — 2026-09-02, centoventicinquesima sessione

`custom_itemenchantment.hsp` (26), `net.hsp` (24) e `txtadv.hsp` (117) chiudono
**l'ultimo fronte di `lang()` del progetto**.

    perimetro.py    26.326 fatte, 0 da fare = 100,0%   (era 26.159 / 167)
    applica         30.764 sostituzioni più 17 toppe   (era 30.532)
    toppe           1.048                              (erano 1.031)
    nudi_en         400 ancora da fare                 (erano 417)
    menu_dialogo    0 fuori misura su 1.423 misurate   (erano 1.383)

I due file che restano nell'elenco, `custom_pet.hsp` e `custom_dmgpop.hsp`,
hanno **una firma sola ciascuno ed è muta**: erano già finiti dalla 124ª.

### ⚠️⚠️⚠️ Il 100% non è la fine: restano 198 righe di testo che nessun lotto raggiunge

`nudi_en.py` conta **400** letterali inglesi ancora intatti, e `triage_nudi.py`
li spacca: **198 sono testo**, 87 sigle (i nomi delle tracce del jukebox), 93
`dbg` (la console da mago), 22 spente dentro un commento. Le 198 non passano da
nessuna `lang()` — niente firma, niente voce di dizionario — e si toccano solo
con una toppa. Stanno in **blocchi**, e un blocco è una schermata sola:
`item_func.hsp:*skipName` 13, `proc.hsp:*jump_changeCreature` 13,
`item_func.hsp:*itemname` 11, `map_rand.hsp:*map_randomDungeon` 9,
`system.hsp:*game_title` 9.

💡 **È il fronte da aprire nella prossima sessione**, ed è l'unico rimasto che
sia lavoro di traduzione. Si comincia da `triage_nudi.py`, non da `nudi_en.py`.

### Che cosa avevano dentro i tre file

Tutti e tre sono lo stesso caso, ed è il rovescio della regola di sempre: **il
giapponese è la fonte copiata e l'inglese quella scritta.** Custom-GX ricopia il
giapponese di monte e riscrive l'inglese, e nelle slot di `txtadv.hsp` il
segnaposto non è nemmeno la riga giusta (`:1183` porta la spiegazione del
blackjack sotto l'inglese delle slot).

⭐⭐ **E tre punti dell'esplorazione sono lo stesso caso dentro il codice di
monte**, dove a smentire il giapponese sono le **abilità controllate due righe
sopra**: falegnameria e sollevamento pesi non frugano fra i resti, tagliano e
sollevano un tronco.

Due difetti di monte trovati leggendo il codice: `txtadv.hsp:665` stampa la
parentesi due volte in giapponese, e `net.hsp:375` porta un inglese ricopiato da
un'altra riga che dice tutt'altro (`WEREWOLF_STAGE` contro `NEXT_VOTE`).

### ⭐⭐⭐ Un test ha fermato il lotto, ed è la prima volta

Dopo il reimporta di `txtadv.hsp`, `pytest` è passato da 794 verdi a 1 rosso:
`test_le_voci_tradotte_stanno_tutte_in_un_contenitore_misurabile`.
`menu_dialogo.py` elencava `com_txtadv_loop` fra i «non misurati» dalla 72ª e
nessuno ci aveva mai messo una resa dentro; con questo lotto ce ne sono finite
quaranta in un colpo. **Non ha trovato un danno: ha impedito un permesso.**

La geometria è stata letta e il tetto — 48 caratteri, ed è una **scia** e non un
taglio — è entrato in `menu_dialogo.py` come **quinto contenitore**.

### ⭐⭐ Il referto dei participi ha trovato sei rese al maschile

`referti.py` è passato da 9 a 15 dopo il lotto, e tutte e sei le nuove davano
del maschile al giocatore, che in Elona può essere donna. **Il rimedio è il
presente**, non una perifrasi: cinque su sei si risolvono cambiando tempo.
⚠️ Le ha viste solo perché è stato rilanciato **in chiusura** (regola della
120ª): in apertura avrebbe detto 9, cioè il numero di ieri.

### Il debito di collaudo

⚠️⚠️ **Nessuna delle 167 rese è stata vista a schermo**, e nemmeno le 17 toppe.
Il debito sale da 9.349 a **9.516**. ⚠️ E quel numero **non è misurato da
niente**: è tenuto a mano nel documento di ripresa.

⭐ Le due schermate nuove si guardano in pochi minuti: il **menu del fabbro**
(`chatval 114514` e `69000`) e la **schermata testuale** (esplorazione, blackjack
e slot). La seconda è l'unico posto dove si vede se i tetti tengono davvero,
perché il passo del font 14 non è mai stato misurato a schermo.

---

## `custom_itemenchantment.hsp` si chiude: 26 rese, 17 già decise — 2026-09-02, centoventicinquesima sessione

Il fronte aperto dalla 123ª scende da tre file a **due**. Restano **141 firme**:
`txtadv.hsp` 117 e `net.hsp` 24. Gli altri due file senza dizionario,
`custom_pet.hsp` e `custom_dmgpop.hsp`, hanno una firma sola ciascuno ed è muta:
sono già finiti (124ª).

    perimetro.py    26.185 fatte, 141 da fare = 99,5%   (era 26.159 / 167)
    applica         30.562 sostituzioni più 3 toppe     (era 30.532)
    toppe           1.034                               (erano 1.031)

⭐⭐⭐ **Diciassette rese su ventisei erano già decise**, e le ha trovate
`scratchpad/_125-sorelle-itemench.py`: il giapponese di questo file è ricopiato
**identico** da `chat.hsp:11290`-`:11661`, cioè dal fabbro di monte. Il file è
la copia che Custom-GX ha fatto di quel dialogo, e le due versioni sono
**tutt'e due vive** — `chat.hsp:23306` manda qui su `chatval == 114514`,
`chat.hsp:11287` tiene l'originale su `chatval == 1`. Stesso fabbro, due voci di
menu vicine: le diciassette si copiano, non si riscrivono.

⚠️⚠️ **Le nove nuove sono quelle in cui il giapponese è un moncone**: むむむ。,
すまんのう。, どうだろう. Lì la fonte scritta è l'inglese — è la regola della
109ª usata per la prima volta al rovescio — e senza di essa il giocatore
italiano leggerebbe «Mmm.» dove l'inglese gli dice quanto oro costa e quale
pozione serve.

### Le tre toppe

`nudi_en.py` trovava tre righe inglesi nude, tutte lette a schermo nel menu
della disincantazione. `custom_itemenchantment.hsp` passa da **3 intatte a 0**,
e il totale del progetto da 417 a **414**.

    :256   "[N gold] "                        -> "[N oro] "
    :278   "Try to remove the enchantment?"   -> "Indebolire? (…)"
    :280   "Remove the enchantment?"          -> "Cancellare? (…)"

⭐ **«Try to remove» era l'indebolimento**, e lo dice `p_rem == val(1)`: la
stessa condizione con cui `:324` sceglie fra «…removed!» e «…**weakened**!».

### Un cancello verde su un denominatore che escludeva le righe a rischio

`menu_dialogo` diceva «0 su 1383» con **tre voci fuori misura** dentro quella
schermata: legge il dizionario, e una riga di toppa non ci sta; e per `:276`
conta `cnvitemname()` come lunga zero, dove a schermo sono fino a 38 caratteri.
Le misura ora `scratchpad/_125-larghezze-menu-incanti.py`, con la prova al
contrario sulle **tre stesure vere scartate**.

⚠️ «pergamena di acquisizione di attributi» sono **38** caratteri contro i 24 di
«scroll of gain attribute», su un tetto di 58: è il posto misurato finora dove
il nome italiano di un oggetto costa di più dell'inglese dentro un tetto stretto.

### Due valori attesi del referto d'apertura erano falsi

Non erano regressioni, ed è la **quarta** volta che questo referto porta un
numero scritto a mano che non torna. `verifica --dizionario` non toglie le
rinviate, quindi «tutti 0 e 0» non poteva essere vero il giorno che fu scritto;
e `_97-quanto-resta` era già 112 al commit della 124ª, che ne scriveva 111.
`scratchpad/_125-non-tradotte.py` fa la domanda giusta e risponde **112 non
tradotte, 112 rinviate, 0 fuori**.

### Il debito di collaudo

⚠️⚠️ **Nessuna delle 26 rese è stata vista a schermo**, e nemmeno le tre toppe.
Il debito sale da 9.349 a **9.375**.

⭐ **La lista di collaudo di questa sessione è corta e si fa in due minuti**: il
menu del fabbro, fusione (`chatval 114514`) e disincantazione (`69000`). Lì si
leggono le tre voci nuove, il prefisso del punteggio e l'etichetta del prezzo.

---

## Sei file mai estratti si chiudono, e il 91% era 99% — 2026-09-02, centoventiquattresima sessione

Non `db_item.hsp`: il fronte aperto dalla 123ª, cioè i file che portano `lang()`
e **non hanno mai avuto un dizionario**, invisibili a `_97-quanto-resta` perché
non compaiono nemmeno come riga.

    material.hsp             17 rese    il pannello della produzione
    quest.hsp                22 rese    esiti di incarico, arena, autorità
    etc.hsp                  11 rese    gli dèi che ti dicono di smettere
    map_rand.hsp              6 rese    cinque nomi di mappa e un presagio
    custom_nefiatypes.hsp     2 rese    il boss del Vuoto
    scene.hsp                 1 resa    un nome di file, dichiarato invariato

    file senza dizionario: 238 firme in 11 -> **174 in 5**, di cui 7 mute
    applica: 30.466 -> **30.532**   (+19, +21, +26 — tre previsioni, tre esatte)
    toppe:   1028 -> **1031**, e 1031 su 1031 agganciate

### ⚠️⚠️⚠️ Il referto diceva 91%, e sbagliava due volte nello stesso senso

L'ha chiesto l'utente — «siamo quasi alla fine?» — e i due modi di rispondere
non tornavano: `perimetro.py` diceva che mancava il 9% (2.563 firme) e
`verifica --dizionario` diceva che ogni file col dizionario è chiuso e che fuori
ne restano 174. Mentiva il referto.

1. `nomi_oggetto` **non è un conto del sorgente**: è `rese['db_item.hsp']`, cioè
   *tutte* le voci di quel dizionario — e dalla 107ª le descrizioni stanno
   **dentro** quel dizionario (2.831 su 4.407; le altre 1.576 sono i nomi).
   Sommare `descrizioni` accanto le metteva al denominatore una seconda volta:
   **2.832 di lavoro inesistente**, il 10% del progetto.
2. Corretta quella veniva **101%**, e il 101 è la spia dell'altro guasto:
   numeratore **vero** diviso per un denominatore **stimato per difetto del
   2-4%**. Il rapporto fra un conteggio e una stima non è una percentuale.

⭐ Il conto onesto è una **sottrazione**: quel che resta si conta con lo stesso
`estrai` che scrive il dizionario, così «fatte» e «da fare» sono numeri della
stessa specie.

    firme rese                              26.159
    firme ancora da fare, contate              167
    --- fatto 26.159 su 26.326             = 99,4%

⚠️ È la **terza** volta che questo referto sbaglia — la 98ª (rese dei file dati
contate solo al denominatore), la 107ª (2.452 stringhe vuote), oggi — e tutte e
tre mettendo al denominatore lavoro che non esisteva. Un denominatore gonfiato
non desta sospetti in nessuno: rassicura chi teme di aver dimenticato qualcosa.

### ⚠️⚠️ Una firma non è sempre lavoro

`perimetro.firme_lang()` raccoglie l'argomento inglese di ogni `lang()`, e
alcune non portano **nessun letterale**: `font lang(cfg_font1, cfg_font2)`
sceglie il carattere. Sono **45** in tutto il sorgente, 26 delle quali
`cfg_font2`, e `material.hsp` diceva 18 dove il lavoro vero era 17.
`custom_pet.hsp` e `custom_dmgpop.hsp` hanno **una firma sola ciascuno ed è
quella**: non si chiuderanno mai traducendoli, sono già finiti.

### ⭐⭐ Quattordici rese su 59 erano già decise altrove — e una era sbagliata

Una ricerca per **somiglianza del giapponese** su tutto il dizionario (la regola
della 113ª applicata a un lotto intero) ha trovato quattordici gemelle già rese.
E ha trovato un difetto nel lavoro **già in gioco**: `screen.hsp:1450` scriveva
«Larneire» con una `n` sola, contro «Larnneire» in dodici rese su dodici.
Nessuna rete lo vedeva — guardano la forma, l'inglese di monte e il dizionario,
e un nome proprio storpiato di una lettera passa tutte e tre.

> **La riga sorella non serve solo a copiare una resa: serve anche a
> controllarla.**

### ⚠️⚠️ Due pannelli misurati per la prima volta, e tutti e due sforavano

**Il pannello della produzione** ha tre colonne e **due font diversi nella stessa
finestra** (12 per l'elenco a `:299`, 11 per il dettaglio a `:252`). La colonna
dei materiali richiesti è la più stretta del progetto — 192 px a font 11 fanno
27 caratteri — e **27 combinazioni su 113 sforavano**, la peggiore a 31.
Allargata con una toppa a due colonne da 288.

**E i nomi di mappa hanno un tetto di 12 caratteri, non 16**: `screen.hsp:153`
taglia con `strmid`, e sono 12 dove la mappa mostra il livello. Il cancello è
sul **peggioramento** e non sullo zero assoluto, perché monte stesso sfora: al
tetto pieno l'italiano non peggiora niente, al tetto stretto **peggiora ventuno
rese già in gioco**. Fronte aperto, misurato e non deciso.

## Tre lotti, 67 rese, e si chiudono SCUDI, LIBRI e ARMATURE — 2026-09-01, centoventunesima sessione

`db_item.hsp`, il **corpo** delle descrizioni. Tre categorie intere, una per
lotto: la tredicesima, la quattordicesima e la quindicesima.

    058  FILTER_SHIELD     24 rese  (23 idx0, 1 idx2)   la categoria intera
    059  FILTER_ITEM_BOOK  23 rese  (21 idx0, 2 idx2)   la categoria intera
    060  FILTER_ARMOR      20 rese  (20 idx0)           la categoria intera

    corpo (indici 0-2): 1.306 -> **1.374** rese su 1.513 vive
    non tradotte di db_item.hsp: 206 -> **139**   (-67 esatte)
    applica: 30.142 -> **30.210**   (+24, +24, +20)
    ⚠️ il secondo +24 e' per 23 rese: nel 059 c'e' una GEMELLA

⭐ In apertura le verifiche erano **ventisei su ventisei** ai valori attesi: la
prima volta dalla 119ª che non c'è un difetto da correggere prima di cominciare.

### ⭐⭐⭐ La stessa domanda, tre risposte diverse: il collaudo non si eredita

La 120ª aveva deciso che la pergamena del collaudo è la **362**, dopo che la
lista della 119ª sarebbe stata muta sulle armi a distanza. Questa sessione ha
misurato i due numeri su **tre** categorie di fila, e ha avuto tre risposte:

    categoria           reftype   IDENTIFY_LEVEL       la pergamena 14 basta?
    FILTER_SHIELD       14.000    500 su 16 di 23      NO
    FILTER_ITEM_BOOK    55.000    0 su 21 di 21        SI, e per due ragioni
    FILTER_ARMOR        16.000    500 su 7, 0 su 13    NO su metà categoria

⭐ È la prova più solida possibile della decisione della 120ª: **la domanda va
rifatta a ogni categoria**, perché la premessa non sta nel passo, sta nella
categoria. Sui libri la 14 basterebbe due volte — `item_func.hsp:641` dà FULL
già perché `efp >= 0`, e `:646` lo darebbe comunque perché 55.000 supera
`FILTER_ITEM_MIN` — e sulle armature basterebbe per dodici oggetti su venti.
La regola «usa la 362» resta giusta perché **non è mai sbagliata**, e adesso si
sa anche quando sarebbe stata di troppo.

### ⭐⭐⭐ Due famiglie hanno attraversato due lotti della stessa sessione

Il lotto 060 ha due righe la cui apertura è **identica** a due righe del lotto
058, chiuso un'ora prima, e cambia **un carattere**:

    :100717 (058)  非常に分厚く作られた盾。  ->  Uno scudo fatto spessissimo.
    :101964 (060)  非常に分厚く作られた鎧。  ->  Una corazza fatta spessissima.
    :100849 (058)  特殊な素材を…得た盾。     ->  Uno scudo che, incrociando…
    :101769 (060)  特殊な素材を…得た鎧。     ->  Una corazza che, incrociando…

⚠️⚠️ **Tre strumenti hanno risposto giusto e tutti e tre hanno mancato il
punto**: `_gia-reso` dice 0 su 20 perché cerca la prosa intera e le stringhe
differiscono; `_120-serie-bacchette` dice «nessuna serie» perché guarda dentro
il lotto e la sorella sta fuori; `_coerenza` non le vede per lo stesso motivo.
È la forma del 014 contro il 024 — un lotto rende, il lotto dopo disfa — e non
è successo **solo perché le rese del 058 erano ancora sotto gli occhi**. Su una
sessione che riprende domani non lo sarebbero.

### ⭐⭐ Una coppia che si nomina a vicenda, e l'inglese che slega il nodo

`:101574` (軽鎧) e `:101964` (厚鎧) chiudono con la stessa frase e ciascuna
**nomina l'altra**: 「厚鎧とどちらを取るかは冒険者の好み」 e
「軽鎧とどちらを取るかは冒険者の好み」. Sono due oggetti che il giocatore ha
davvero, e la riga gli sta dicendo *questo o quello, scegli*. L'inglese perde
tutt'e due i nomi — «standard thick armor», «lighter armor» — e non manda il
lettore da nessuna parte. Le due rese usano i nomi veri, «corazza a bande» e
«corazza leggera», e per il resto sono identiche parola per parola.

### ⭐⭐ Quattro diari che devono restare uguali, e uno che deve restare diverso

Nel 059, 「◯がしたためたとされる日記。」 si ripete **quattro** volte — il
maggiordomo, qualcuno, la sorella maggiore, la signorina — e la resa è «Un
diario che si dice vergato da ◯.» in tutte e quattro. Ma `:97200` dice
妹が**書いた**日記, il verbo comune, e la resa dice «Il diario che ha scritto la
sorella minore».

⭐ È la lezione della 119ª **al rovescio**: là l'inglese aveva ricopiato righe
che dovevano differire, qui il rischio era appiattire righe che il giapponese
distingue di proposito. Uniformare avrebbe «migliorato» il testo cancellando una
differenza che l'autore ha scritto.

### ⚠️⚠️ Il preflight ha preso quattro rese, e l'errore era di lettura

Nel 059 quattro rese sono uscite dal montaggio con la coda **attaccata al punto
finale** e il segmento `\n` in meno. La causa: `_forma.py` stampa due cose sulla
stessa riga — lo spazio prima del `\n` e lo spazio dopo il `#` — e io ho letto
«senza lo spazio prima del `\n`» come «senza il `\n`».

⭐ `_preflight034.py` le ha prese tutte e quattro («segmenti diversi: en 1, it
0») **prima** del reimporta e prima della build. È il suo punto 3, scritto nella
115ª per un guasto diverso, che qui ha pescato un errore di lettura di chi
scrive le rese — non un errore di battitura.

## Tre lotti, 90 rese, e si chiudono MINERALI, BACCHETTE e CONTENITORI — 2026-09-01, centoventesima sessione (seconda parte)

`db_item.hsp`, il **corpo** delle descrizioni. Tre categorie intere, una per
lotto: la decima, l'undicesima e la dodicesima.

    055  FILTER_ORE        33 rese  (33 idx0)   la categoria intera
    056  FILTER_ITEM_ROD   32 rese  (32 idx0)   la categoria intera
    057  FILTER_CONTAINER  25 rese  (22 idx0, 3 idx2)

    corpo (indici 0-2): 1.216 -> **1.306** rese su 1.513 vive
    non tradotte di db_item.hsp: 296 -> **206**   (-90 esatte)
    applica: 30.052 -> **30.142**   (+33, +32, +25: tutte previste, nessuna gemella)

⭐ Con i lotti 053-054 della prima parte fanno **150 rese e quattro categorie
chiuse** in una sessione sola.

### ⭐⭐⭐ La ricerca delle serie e' diventata uno strumento

`scratchpad/_120-serie-bacchette.py` prende un lotto e risponde a tre domande
che il dossier non risponde, perche' mostra una voce per volta:

  1. quante righe **aprono identiche**, e quale diverge;
  2. quali righe hanno il **giapponese identico** fra loro — perche' allora le
     rese devono essere identiche;
  3. dove il giapponese porta una parola che l'inglese lascia cadere.

⭐⭐ Sulle 32 bacchette del 056 ha trovato due cose che l'occhio avrebbe perso:

  - **31 righe su 32 aprono identiche**, e l'unica che diverge e' `:111777` —
    la bacchetta dei **desideri**, la piu' rara del gioco — che dice 貴重な杖,
    «una bacchetta **preziosa**». L'inglese non lo porta. Il gradino sta in due
    caratteri dentro una formula ripetuta trentadue volte: e' esattamente cio'
    che l'occhio salta, perche' sta leggendo la parte che cambia (la gemma);
  - **`:71856` e `:106766` hanno il giapponese IDENTICO** — l'eclissi e il
    silenzio — e due inglesi che differiscono per **una virgola**. Le due rese
    puntano a una **costante sola** nel file, cosi' non possono divergere per
    distrazione; `battute --divergenti` e' rimasto a 13.

⭐ E il **valore atteso** dello strumento e' «nessuna serie»: sul 057 l'ha detto
in un secondo (25 righe, 24 aperture distinte, nessuna coppia). Sapere che non
c'e' niente da cercare vale quanto trovare qualcosa.

ⓘ E' la lezione della 119a (cercare per struttura, sull'originale) salita di un
gradino: **la' la struttura si cercava a mano, qui si conta**. La domanda
«questa riga ha delle sorelle?» ha smesso di dipendere da quanto sto attento.

### ⚠️⚠️⚠️ Otto code su venticinque scritte a memoria, e otto sbagliate

Nel 057 ho ricostruito i titoli-fonte **a senso** dal giapponese invece di
copiarli dall'uscita di `_code.py`. Otto su venticinque, tutti plausibili e
tutti diversi da quello in tabella:

    «Alla Faccia della Chiusura! Box Mania, Numero Primo»
                          -> «Chiudeteci Pure! Box Mania, Numero Uno»
    «Manuale dei Giochi: Edizione per Tutte le Età»
                          -> «Grande Compendio dei Giochi: Per Tutte le Età»
    «Cose Belle da Ricevere in Regalo» -> «Regali che Fa Piacere Ricevere»
    «Libro da Donare a Chi Sta per Morire» -> «Libro in Dono a Chi Sta Morendo»
    «I Cinquanta Articoli Più Amati dai Carcerati»
                          -> «I 50 Prodotti Preferiti dai Detenuti»
    … e altre tre.

⚠️ **Il preflight non le prende**: guarda la spaziatura e la struttura, non il
testo del titolo. A prenderle sarebbe stato `_112-corpo-descrizioni`, il cui
«titoli resi in PIU' modi» sarebbe salito da 7 a **15** — ma solo **dopo** il
reimporta, cioe' dopo aver scritto nel dizionario quindici titoli doppi.
Corrette prima, il cancello e' rimasto a 7.

⭐ La regola non e' «stare piu' attento»: e' che i titoli si **copiano**
dall'uscita dello strumento, come le righe si copiano dal template. Un titolo
somiglia abbastanza al giusto da non insospettire chi lo rilegge.

### ⚠️⚠️ La quinta riga gemella ricopiata, e la piu' grossa

`:69118`, la **tavoletta di smeraldo** del lotto 055. Il giapponese dice
錬金術の基本思想を記したエメラルドの碑文 — «l'iscrizione su smeraldo che riporta
il pensiero fondamentale dell'alchimia», cioe' la Tavola Smeraldina. L'inglese
ci scrive **parola per parola** la frase del rubynus e del diamante: «Large
emerald are cut from collected gemstones that have been fused together through
alchemy...».

⚠️ Qui il guasto e' piu' grosso dei quattro della 119a, perche' la riga copiata
**non ha senso sull'oggetto**: una tavoletta incisa non e' una gemma tagliata.
⭐ E a confermarlo non serviva il solo giapponese: l'**indice 3**, reso e chiuso
da sessioni, dice «Una tavoletta fatta di smeraldo», e i due indici il pannello
li disegna uno sotto l'altro.

### ⭐ Le dodici pietre dei mesi, e una distinzione che l'italiano tiene a meta'

Il giapponese usa **due nomi diversi** per la stessa pietra: il nome
dell'oggetto e' in katakana (サードニクス, アレキサンドライト), la descrizione
usa il nome mineralogico (メノウ **l'agata**, 金緑石 **il crisoberillo**).
L'inglese scrive due volte la stessa parola.

In italiano le due coincidono quasi sempre — granato, ametista, rubino — ma nei
**due** casi in cui la coppia esiste davvero la resa la tiene: il giocatore vede
«M08-Sardonice» e legge «un'agata lavorata ad arte», che e' quello che legge
anche il giocatore giapponese.

⚠️ **E una cosa che questo lotto NON puo' riparare.** I dodici **nomi** portano
in giapponese un epiteto — 真実 la verita', 高貴 la nobilta', 聡明 la sagacia,
無垢 la purezza, 誠実 la sincerita', 情熱 la passione, 威厳 la dignita', 円満
l'armonia, 慈愛 l'affetto, 希望 la speranza, 友情 l'amicizia, 成功 il successo —
e l'inglese ci mette «jewel» su **dodici righe su dodici**. L'italiano ha
seguito l'inglese. Non e' materia del corpo, ed e' la stessa forma delle due
questioni aperte dalla 118a sui grimori: va **decisa**, non ereditata.

## Due lotti, 60 rese, e si chiude ARMI A DISTANZA — 2026-09-01, centoventesima sessione

`db_item.hsp`, il **corpo** delle descrizioni (indici 0-2). La sessione ha
aperto e chiuso **una** categoria, la nona, ed era la più grossa rimasta:

    053  FILTER_RANGE  righe      0- 90.000   50 rese  (46 idx0, 1 idx1, 3 idx2)
    054  FILTER_RANGE  righe 90.000 in su     10 rese  (10 idx0)

    corpo (indici 0-2): 1.156 -> **1.216** rese su 1.513 vive
    non tradotte di db_item.hsp: 356 -> **296**   (-60 esatte)
    applica: 29.992 -> **30.052**   (+60: nessuna gemella, previsto)
    perimetro: 90%; totale: 94%

⚠️ La zona del 053 non è l'intera categoria per scelta: `0 200000` dava **60**
righe, sopra il tetto di 55 che la 115ª dichiara sano. `0 90000` ne dà 50, e il
054 raccoglie le dieci che restano.

⭐ `_previsione.py` ha detto **+50** e **+10** prima che `applica` girasse, e
`applica` ha detto 30.042 e 30.052. Nessuna delle 60 firme ha una gemella nel
sorgente: è la prima categoria intera senza moltiplicatori da quattro
sessioni.

### ⭐⭐⭐ Una serie di tre, e la parola che cambia è un attributo del gioco

`:75515`, `:77075` e `:77145` chiudono con la stessa formula, parola per parola:

    人では扱えない程の重さだが、使いこなす者が現れた時
    この武器は使用者に ◯◯ を授けるだろう。それと少しばかりの気まぐれを。

    :75515  la moneta di pietra      魅力            -> carisma
    :77075  la balestra gigantesca   飛びぬけた器用さ  -> destrezza fuori dal comune
    :77145  il cannone a gravità     超感覚           -> percezione fuori dall'umano

Le tre parole sono **CHR, DEX e PER**: le statistiche che il giocatore legge
nella propria scheda, e che quelle tre armi danno davvero. Le rese vengono dal
dizionario (`_cerca.py`: 魅力の成長 -> «Cresce carisma», 器用の成長 ->
«Cresce destrezza») e non dall'inglese, che scrive «a tremendous **charm**»:
renderlo «fascino» avrebbe spezzato il legame con la voce che a schermo si
chiama **carisma**.

⭐ E la formula si ripete **identica** nelle tre rese, di proposito: variare i
verbi avrebbe cancellato la serie, che è come il giocatore riconosce la terza
arma come parente delle prime due. È la scala delle navi della 119ª al
rovescio — là l'inglese aveva appiattito quattro gradini in uno, qui tre righe
devono restare **uguali** tranne una parola.

⚠️ Nessuna rete poteva vederle: firme diverse, tre oggetti di tre tipi, e
ognuna presa da sola è a posto. Nel dossier stanno a dodici voci di distanza.

### ⭐⭐ E una scala che era già metà in gioco: il lavoro è stato non romperla

Sei armi base del 054 dicono, ciascuna a modo suo, quanto la forza cali
allontanandosi. La scala **era già resa nell'indice 3**, chiuso da sessioni:

    光子銃   pistola laser     殆どない   -> «con la distanza non cala quasi»
    機関銃   mitragliatrice    少ない     -> «con la distanza cala poco»
    拳銃     pistola           減衰する   -> «con la distanza perde forza»
    散弾銃   fucile a pompa    射程が短い -> «porta poco lontano»

Il pannello disegna il corpo e l'indice 3 **uno sotto l'altro**: un verbo
diverso nel corpo — «diminuire», «scemare», «indebolirsi» — avrebbe spezzato la
stessa scala **nella stessa schermata**. Tutte le rese del corpo dicono
**calare**. I due archi la chiudono dall'altro capo (近～中距離 per il corto,
中～遠距離 per il lungo).

### ⚠️⚠️ Il referto dei participi era salito a 10, e a farlo salire era la 119ª

`scratchpad/referti.py` in apertura accusava `db_item.hsp:96060`, l'atto del
museo: «la collezione **che ti sei fatto da solo**», participio e aggettivo al
maschile in una riga rivolta al giocatore. La chiusura della 119ª aveva scritto
«`referti` fermo a 9», e non mentiva: la misura era stata presa **prima** delle
rese dei lotti 051-052. È la lezione della 112ª — una catena verde misurata su
un albero che non è quello finale — applicata a un **referto** invece che a
`pytest`.

Corretto sul giapponese, che il problema non ce l'ha: 自分で集めた収集品 è «i
pezzi raccolti da sé», e il participio si appoggia alla collezione, non a chi la
possiede. La resa nuova fa lo stesso — «la collezione **raccolta di persona**» —
e in più recupera 一手に («tutta in una volta»), che la resa vecchia lasciava
cadere. `scratchpad/_120-correzione-museo.py`, e il referto è tornato a **9**.

### ⭐ Il doppio senso della foglia, che l'italiano tiene per intero

`:43632`: 「おぬしにハッパをかけてやろうぞ…ドカーン！」. ハッパ è insieme
葉っぱ **la foglia** (l'oggetto), 発破 **la carica esplosiva** (che è il nome
dell'oggetto, 金毛発破) e ハッパをかける **dare la carica, incitare**. Tre sensi
in una parola, e l'italiano ne ha una che ne tiene due: «ti do io **la
carica**» è insieme l'incitamento e l'esplosivo, e il «BUM!» fa scattare il
secondo. L'inglese («Lemme give you a little nudge») tiene solo il primo.

### ⚠️ Due righe dello stesso oggetto dove l'inglese ha riscritto

  - `:52650`, il gambero fritto esplosivo: in giapponese parla un **commesso
    confuso** (「エビフライ５本くらいぶつけんぞ」), in inglese un **bandito
    eccentrico** con un bisticcio suo su shrimp/shrimping. ⭐ A dire quale sia
    la fonte non è stato il giudizio ma `_code.py`, che assegna il titolo
    passando dal **giapponese** e scrive «Parole di un Commesso Confuso»:
    rendere dall'inglese avrebbe messo la battuta del bandito sotto il titolo
    del commesso, **nello stesso pannello**;
  - `:52648`, due voci sopra e stesso oggetto: il giapponese chiude con
    「悪魔の兵器」の別称でも知られている — *lo chiamano anche l'arma del
    diavolo*, che è un fatto sull'oggetto. L'inglese lo butta per un altro
    bisticcio («shrimply devilish»). La resa tiene il fatto.

## Quattro lotti, 154 rese, e si chiudono POZIONI e PERGAMENE — 2026-09-01, centodiciannovesima sessione

`db_item.hsp`, il **corpo** delle descrizioni (indici 0-2). La sessione ha
aperto e chiuso **due** categorie, la settima e l'ottava:

    049  ITEM_POTION  righe       0- 90.000   41 rese  (37 idx0, 4 idx2)
    050  ITEM_POTION  righe  90.000 in su     40 rese  (40 idx0)  + 1 RINVIATA
    051  ITEM_SCROLL  righe       0-100.000   50 rese  (42 idx0, 5 idx1, 3 idx2)
    052  ITEM_SCROLL  righe 100.000 in su     23 rese  (23 idx0)

    corpo (indici 0-2): 996 -> **1.156** rese su 1.513 vive
    non tradotte di db_item.hsp: 510 -> **356**   (-154 esatte)
    applica: 29.832 -> **29.992**   (+160, non +154: vedi sotto)
    perimetro: 90% (28.367); totale: 94% (31.300)

### ⚠️ Perché `applica` è salito di 160 e le rese sono 154

Sei righe del sorgente sono **gemelle** di righe del lotto 051: stessa firma,
cioè stesso giapponese *e* stesso inglese, quindi una resa sola le copre tutte e
due. `lotti-113/_previsione.py` le ha contate **prima** che `applica` girasse:

    :45132 -> anche :45203        la nota della nave, かなり弱い
    :45345 -> anche :45416        la nota della nave, 弱い
    :51360 -> anche :51431, :51502, :51573   la nota del mezzo di terra
    :58396 -> anche :58458        il certificato fiscale, 12 milioni e 1,2

Lotto per lotto: **+41, +40, +56 per 50 rese, +23**. Tutti e quattro previsti
prima, tutti e quattro esatti.

### ⚠️ Una riga rinviata, e due strumenti che non filtravano le rinviate

`:129299` — `description(1)` della pozione di confusione — ha `\t\t\n\n` in
tutt'e due le lingue: uno slot vuoto, non una frase. Resa identica, `reimporta`
la rifiuta e si porta dietro il lotto intero; resa vuota non è esprimibile. È in
`rinviate.jsonl`, che sale da **113 a 114**.

Conseguenze sui conti, tutte volute e tutte scritte:

    verifica --dizionario   356   (le rinviate le conta)
    _97-quanto-resta        355   (le toglie: colonna «rinviate» 110 -> 111)
    _114-corpo-da-fare      356 totale, e FILTER_ITEM_POTION legge «1 su 82»

⚠️ Il «1» di `FILTER_ITEM_POTION` **non è lavoro**, e da questa sessione lo dice
lo strumento: in fondo alla tabella c'è «di cui RINVIATE, cioè non lavoro: 1 —
:129299». Sottrarle avrebbe rotto in silenzio l'invariante «il totale coincide
con `verifica --dizionario`».

E `scratchpad/_107-chiavi-item.py` le rinviate non le filtra affatto — legge
l'estrazione dritta, senza passare da `estrai.da_tradurre` come fa
`categorie.py` — quindi la riga restava nel template e `_monta` moriva di
`KeyError`. Strumento nuovo: **`scratchpad/_119-togli-rinviate.py`**, da lanciare
dopo ogni `_corpo.py`.

### ⭐⭐ Il cancello delle parole spezzate si è acceso davvero

Dopo il 051, `_107-descrizioni-item` ha detto «parole spezzate introdotte: 1», e
`--peggiori` ha dato il nome: `:81740`, dove «equipaggiamento» andava a capo
spezzato. Riscritta, riassemblata **dal passo che copia**, rimisurata: 0. ⚠️ La
stessa parola a `:95990` non si spezza — conta dove cade il taglio, non la
lunghezza (113ª), e questa è la prima verifica su un caso vero.

### Quel che resta

    60  FILTER_RANGE       <- la più grossa
    33  FILTER_ORE
    32  FILTER_ITEM_ROD
    25  FILTER_CONTAINER
    24  FILTER_SHIELD
    23  FILTER_ITEM_BOOK
    ... e una coda di categorie minori

⚠️ Debito di collaudo: **8.812** rese mai viste a schermo. Le due liste di passi
stanno in `RIPRESA-sessione.md`, con gli identificativi letti in
`defines/mod.hsp` e la nota che pozioni e pergamene **non nascono identificate**.

## Due lotti, 92 rese, i GRIMORI si chiudono, e il rango era detto — 2026-09-01, centodiciottesima sessione

`db_item.hsp`, il **corpo** delle descrizioni (indici 0-2). La sessione ha
aperto e chiuso `FILTER_ITEM_SPELLBOOK`, la categoria più grande rimasta:

    047  ITEM_SPELLBOOK  righe      0-100.000   44 rese  (40 idx0, 4 idx2)
    048  ITEM_SPELLBOOK  righe 100.000 in su    48 rese  (42 idx0, 4 idx1, 2 idx2)
    -----------------------------------------------------------------
    **92 rese**, che coprono **92 righe** del sorgente
    applica 29.740 -> **29.832**   (+92 per 92 rese, previsto prima, zero gemelle)
    db_item non tradotte 602 -> **510**   (-92 esatte)
    rese del corpo: 904 -> **996** su 1.513
    FILTER_ITEM_SPELLBOOK   92 -> **0 da fare su 92**   ⭐ CHIUSA

⭐⭐⭐ **Il nome dell'incantesimo non sta nel nome del libro, e in italiano
diverge 37 volte su 80.** In giapponese il libro e la magia si chiamano uguale
su **78 righe su 80** (le due eccezioni sono `:91976`, 扉生成 contro ドア生成, e
`:102031`, 自己変容 contro 自己の変容). In italiano no: la tabella dei nomi degli
oggetti e `skillname()` sono stati resi in sessioni diverse, e su **37 grimori
su 80** dicono due cose — «cartografia magica» contro *Mappa magica*, «mani
guaritrici» contro *Tocco curativo*, «gemma» contro *Pietra protettrice*.

Nel corpo si è scritto il nome dell'**incantesimo**, preso dal codice:
`scratchpad/lotti-113/_incantesimo.py` va dall'`efid` di `DBMODE_ON_READ`
allo `skillname()` di `skill.hsp`, 80 righe su 80, zero non rese. Il motivo è
che quella riga serve al giocatore per **cercare la magia nella lista**: col
nome del libro non la troverebbe.

⚠️ Ma le 37 divergenze restano, e adesso si vedono **nello stesso pannello** —
il nome in testa e la descrizione sotto. Il rimedio vero è allineare i 37 nomi
di oggetto allo `skillname`, ed è un lavoro suo: nessuno strumento del progetto
confronta quelle due tabelle.

⚠️⚠️⚠️ **E il rango era detto: la 110ª aveva deciso su una premessa falsa.** Il
glossario dice, dei 82 inglesi dell'indice 3, «il giapponese non lo dice mai —
non su una sola riga». Cercato 「ランク…魔法」 nel sorgente: è su **80 righe**,
una per ogni grimorio, in `description(1)` del ramo `if ( jp )`. Le 76 dove
l'inglese lascia la stringa vuota non arrivano nell'estrazione, e per questo in
otto sessioni non si erano mai viste. Oggi il giocatore italiano è **l'unico
dei tre** che il rango non lo legge. Decisione da riaprire, e non in questo
lotto: l'indice 3 è chiuso a 1.319 su 1.319 e ha il tetto secco a 69.

**Sei categorie del corpo chiuse**: `FILTER_FURNITURE` (261),
`FILTER_ITEM_TOOL` (204), `FILTER_ITEM_FOOD` (148), `FILTER_JUNK` (124),
`FILTER_WEAPON` (110) e `FILTER_ITEM_SPELLBOOK` (92). Totale del corpo da fare:
**510 su 1.449**.

## Due lotti, 59 rese, e i CIBI si chiudono — 2026-08-31, centodiciassettesima sessione

`db_item.hsp`, il **corpo** delle descrizioni (indici 0-2). La sessione ha
chiuso `FILTER_ITEM_FOOD`, che la 116ª aveva cominciato:

    045  ITEM_FOOD   righe  88.300-110.000   28 rese  (28 idx0)
    046  ITEM_FOOD   righe 110.000 in su     31 rese  (30 idx0, 1 idx2)
    -----------------------------------------------------------------
    **59 rese**, che coprono **60 righe** del sorgente
    applica 29.680 -> **29.740**   (+60 per 59 rese, previsto prima)
    db_item non tradotte 661 -> **602**   (-59 esatte)
    rese del corpo: 844 -> **904** su 1.513
    FILTER_ITEM_FOOD   59 -> **0 da fare su 148**   ⭐ CHIUSA

⭐ **Il +60 su 59 rese era scritto prima**, non scoperto dopo: `:113814` e
`:113879` (indice 2, giapponese vuoto, stesso inglese) sono una firma sola, e a
dirlo e' stato `scratchpad/lotti-113/_previsione.py`, nato in questa sessione
dalla lezione della 116ª. Nella 116ª lo stesso fatto era arrivato come un numero
che non tornava.

**Cinque categorie del corpo chiuse**: `FILTER_FURNITURE` (261),
`FILTER_ITEM_TOOL` (204), `FILTER_ITEM_FOOD` (148), `FILTER_JUNK` (124) e
`FILTER_WEAPON` (110). Totale del corpo da fare: **602 su 1.449**.

## Quattro lotti, 149 rese, e le ARMI si chiudono — 2026-08-31, centosedicesima sessione

`db_item.hsp`, il **corpo** delle descrizioni (indici 0-2). La sessione ha
chiuso `FILTER_WEAPON` (lotti 041-043) e ha cominciato `FILTER_ITEM_FOOD`:

    041  WEAPON      righe       0-67.000   41 rese  (39 idx0, 2 idx2)
    042  WEAPON      righe  67.000-82.000   35 rese  (33 idx0, 2 idx2)
    043  WEAPON      righe  82.000 in su    34 rese  (32 idx0, 2 idx2)
    044  ITEM_FOOD   righe  68.000-90.000   39 rese  (34 idx0, 5 idx2)
    -----------------------------------------------------------------
    **149 rese**, che coprono **150 righe** del sorgente
    applica 29.530 -> **29.680**   (+150 per 149 rese)
    db_item non tradotte 810 -> **661**   (-149 esatte)
    rese del corpo: 694 -> **844** su 1.513
    FILTER_WEAPON     110 -> **0 da fare su 110**   ⭐ CHIUSA
    FILTER_ITEM_FOOD   98 -> **59 da fare su 148**

⚠️⚠️ **150 righe per 149 rese, e la riga in più non è un errore.** Nel lotto 042
`:76863` (<Stormbringer>) e `:126849` (<Mournblade>) hanno il **giapponese e
l'inglese identici byte per byte**: stessa firma, una resa copre due oggetti.
La gemella **non è in `lavoro/_107-daitem.jsonl`** — l'estrazione tiene una voce
per firma, 2.580 voci e 2.580 firme — quindi non è in nessun dossier e in
nessuna tabella di lotto. Il dettaglio è in `decisioni.md`.

⭐ **Le due unità di misura del corpo, e perché differiscono di 64.**
`_107-descrizioni-item` conta **per riga** e dice 1.513 vive;
`_114-corpo-da-fare` conta **per firma** e dice 1.449. Le 64 righe di differenza
sono quelle che nessun lotto potrà scegliere e che si riempiono da sole quando
si rende la gemella. È la stessa distinzione fra firma e occorrenza che questo
documento dichiara in testa, vista dentro un file solo.

ⓘ Il conto delle rese e quello delle righe **non coincideranno più**: da qui in
avanti si scrivono tutt'e due.

## Sette lotti, 278 rese, e si chiudono DUE categorie — 2026-08-31, centoquindicesima sessione

`db_item.hsp`, il **corpo** delle descrizioni (indici 0-2). La sessione ha
chiuso `FILTER_ITEM_TOOL` (lotti 034-037) e `FILTER_JUNK` (lotti 038-040):

    034  ITEM_TOOL   righe  48.000-62.000   44 rese  (39 idx0, 1 idx1, 4 idx2)
    035  ITEM_TOOL   righe  62.000-75.000   43 rese  (36 idx0, 7 idx2)
    036  ITEM_TOOL   righe  75.000-90.000   42 rese  (39 idx0, 3 idx2)
    037  ITEM_TOOL   righe  90.000 in su    25 rese  (21 idx0, 4 idx2)
    038  JUNK        righe       0-62.000   44 rese  (36 idx0, 4 idx1, 4 idx2)
    039  JUNK        righe  62.000-76.000   51 rese  (34 idx0, 8 idx1, 9 idx2)
    040  JUNK        righe  76.000 in su    29 rese  (26 idx0, 3 idx2)
    -----------------------------------------------------------------
    **278 rese**, che coprono **278 righe** del sorgente (nessun doppione)
    applica 29.252 -> **29.530**   (+278 esatte)
    db_item non tradotte 1.088 -> **810**   (-278 esatte)
    rese del corpo: 416 -> **694** su 1.513
    perimetro 27.635 -> **27.913** (90%), totale 30.568 -> **30.846** (94%)
    cancello dei tagli: introdotte dall'italiano **0/0/0**, mai acceso
    rinviate: nessuna   toppe: nessuna   test: **794**, invariato
    strumenti nuovi: 5   build: SI', **16:57 del 31/08**
    -----------------------------------------------------------------
    ⭐⭐⭐ **CHIUSE**: `FILTER_ITEM_TOOL` 204/204 (033-037) e
    `FILTER_JUNK` 124/124 (038-040). Col mobilio della 114a fanno **tre**
    categorie chiuse su ventitre'.

⚠️⚠️ **Il cancello «titoli resi in piu' modi» passa da 2 a 6, e tutti e sei
sono difetti dell'inglese**, che appiattisce o sbaglia titoli-fonte che il
giapponese distingue:

    Lead Developer <Dr. Gavela>      -> Gavela / Icolle              (114a)
    ~Thousands of pieces of Junk~    -> Cianfrusaglie / Brilla       (114a)
    ~Irva Fantasy Encyclopedia~      -> Irva / Aimwell               (034)
    ~Extra Issue: Weird Items~       -> Oggetti Sospetti / Alchimia  (035)
    ~ Great Encyclopedia of North Tyris Furnitures~
                                     -> Mobili / Manuale di Viaggio  (037)
    ~Vernis Ore Catalogue~           -> Vernis / Lumiest             (038)

Il valore atteso e' **6, con questi sei accanto**. Un 7 e' un difetto nuovo.
⭐ Quattro su sei sono stati **annunciati prima di misurarli**, leggendo il
giapponese del lotto; solo quello del 035 e' arrivato senza preavviso.

**Il conto del corpo, categoria per categoria**, con
`python scratchpad/_114-corpo-da-fare.py`:

    chiuse   mobilio 261/261 · attrezzi 204/204 · junk 124/124
    restano  FILTER_WEAPON         110/110   FILTER_ORE             33/33
             FILTER_ITEM_FOOD       98/148   FILTER_ITEM_ROD        32/32
             FILTER_ITEM_SPELLBOOK   92/92   FILTER_CONTAINER       25/25
             FILTER_ITEM_POTION      82/82   FILTER_SHIELD          24/24
             FILTER_ITEM_SCROLL      73/73   FILTER_ITEM_BOOK       23/23
             FILTER_RANGE            60/60   FILTER_ARMOR           20/20
             piu' una coda di diciotto minori
    -----------------------------------------------------------------
    694 righe fatte su 1.449 vive; **810 restano**

ⓘ Il totale coincide con quello di `verifica --dizionario` a ogni lotto: sette
volte di fila in questa sessione.

### Il dettaglio dei primi quattro lotti (gli attrezzi)

`db_item.hsp`, il **corpo** delle descrizioni (indici 0-2), tutta
`FILTER_ITEM_TOOL`:

    034  ITEM_TOOL   righe  48.000-62.000   44 rese  (39 idx0, 1 idx1, 4 idx2)
    035  ITEM_TOOL   righe  62.000-75.000   43 rese  (36 idx0, 7 idx2)
    036  ITEM_TOOL   righe  75.000-90.000   42 rese  (39 idx0, 3 idx2)
    037  ITEM_TOOL   righe  90.000 in su    25 rese  (21 idx0, 4 idx2)
    -----------------------------------------------------------------
    **154 rese**, che coprono **154 righe** del sorgente (nessun doppione)
    applica 29.252 -> **29.406**   (+44/+43/+42/+25 esatte)
    db_item non tradotte 1.088 -> **934**   (-154 esatte)
    rese del corpo: 416 -> **570** su 1.513
    perimetro 27.635 -> **27.789** (90%), totale 30.568 -> **30.722** (94%)
    cancello dei tagli: introdotte dall'italiano **0/0/0**, mai acceso
    rinviate: nessuna   toppe: nessuna   test: **794**, invariato
    -----------------------------------------------------------------
    ⭐⭐⭐ **`FILTER_ITEM_TOOL` e' CHIUSA**: 204 righe su 204, lotti 033-037

⚠️⚠️ **Il moltiplicatore degli attrezzi era di UN lotto solo.** La 114a
chiudeva scrivendo che negli attrezzi «da fare» (154) e «vive» (204) non
coincidono per le righe condivise fra oggetti gemelli, e che quindi `applica`
sarebbe salito di piu' delle rese. E' successo **solo nel lotto 033**, dove i
quattro fucili anestetici condividono due righe: nei lotti 034-037 il rapporto
e' **uno a uno**, e le 154 rese hanno fatto 154 sostituzioni esatte. Il
moltiplicatore stava in quattro oggetti, non nella categoria.

### Il dettaglio degli ultimi tre lotti (gli scarti)

    038  JUNK   righe      0-62.000   44 rese   36 oggetti
    039  JUNK   righe 62.000-76.000   51 rese   34 oggetti
    040  JUNK   righe 76.000 in su    29 rese   27 oggetti

⚠️ **La categoria non ha moltiplicatore**: «da fare» e «vive» coincidevano a
124, e le 124 rese hanno fatto 124 sostituzioni. Dopo il caso degli attrezzi
questa e' la conferma che il moltiplicatore e' una proprieta' di **certi
oggetti gemelli**, non di una categoria.

⭐⭐ **Il lotto 039 e' il piu' denso di indici 1 e 2 di tutta la sessione**, e la
ragione e' una famiglia sola: gli **otto oggetti personali degli dei**, dove
ogni pannello e' una scenetta a due voci (l'enciclopedia, poi la battuta di un
dio e la risposta di un altro).

⚠️⚠️ **La tilde di monte non e' sempre una tilde.** `_code.py` ha aperto il
lotto 038 dicendo «righe senza resa in tabella: 1», e la riga era `:46213`, la
cui coda giapponese porta **due punti interrogativi ASCII** al posto della tilde
larga. Misurate con `scratchpad/_115-fonti-storpiate.py`: sono **7 code su
2.542**, tutte fra `:46213` e `:46340`, cioe' tre oggetti soli. Due erano gia'
in tabella dalla 112a, con i punti interrogativi dentro la chiave; questa e' la
terza e si e' aggiunta allo stesso modo.

## Cinque lotti, 223 rese, e il mobilio si chiude — 2026-08-31, centoquattordicesima sessione

`db_item.hsp`, il **corpo** delle descrizioni (indici 0-2):

    029  FURNITURE   righe  91.500-108.000   30 rese  (27 idx0, 3 idx2)
    030  FURNITURE   righe 108.000-113.000   53 rese  (51 idx0, 2 idx2)
    031  FURNITURE   righe 113.000-122.000   36 rese  (35 idx0, 1 idx2)
    032  FURNITURE   righe 122.000 in su     54 rese  (51 idx0, 3 idx2)
    033  ITEM_TOOL   righe      0-48.000     50 rese  (31 idx0, 6 idx1, 13 idx2)
    -----------------------------------------------------------------
    **223 rese**, che coprono **229 righe** del sorgente
    applica 29.023 -> **29.252**   (+30/+53/+36/+54 esatte, **+56** il 033)
    db_item non tradotte 1.311 -> **1.088**   (-223 esatte)
    rese del corpo: 187 -> **416** su 1.513
    perimetro 27.412 -> **27.635** (90%), totale 30.345 -> **30.568** (94%)
    cancello dei tagli: introdotte dall'italiano **0/0/0**, acceso una
      volta in corso d'opera (`:95111`, «Quell'espressione», 17 caratteri)
    rinviate: nessuna   toppe: nessuna   test: **794**, invariato
    strumenti nuovi: 2 (`lotti-113/_gia-reso.py`, `_114-corpo-da-fare.py`)
    build: SI', **14:36 del 31/08**
    -----------------------------------------------------------------
    ⭐⭐⭐ **`FILTER_FURNITURE` e' CHIUSA**: 261 righe su 261, lotti 027-032

⚠️⚠️ **Il lotto 033 ha 50 rese e ha fatto +56, e il perche' conta per tutti i
lotti di attrezzi che verranno.** I quattro fucili anestetici hanno le righe di
indice 1 e 2 **identiche parola per parola**: sono due firme sole, e ciascuna
copre quattro righe del sorgente. Negli attrezzi «da fare» e «vive» non
coincidono (154 su 204) proprio per questo, come nel cibo — e a differenza del
mobilio, dove il rapporto era uno a uno.

⚠️⚠️ **E lo stesso lotto ha alzato un cancello da 0 a 2, per un difetto di
monte.** `_112-corpo-descrizioni` conta i «titoli resi in piu' modi» chiavando
sull'**inglese**, e l'inglese attribuisce `:46952` a <Gavela> quando il
giapponese dice <Icolle>, e cita per `:46403` un libro che non e' quello del
giapponese. Le rese giuste divergono, il cancello se ne accorge, e il valore
atteso diventa **2 con i due nomi accanto**. Un 3 e' un difetto nuovo.

**Il conto del corpo, categoria per categoria**, con
`python scratchpad/_114-corpo-da-fare.py` — che dalla 114a **non si scrive piu'
a mano**, ed e' questo il punto:

    fatte    mobilio 261/261 (027-032) · cibo 50/148 (026)
             attrezzi 50/204 (033)
    restano  FILTER_ITEM_TOOL      154/204   FILTER_ITEM_SCROLL     73/73
             FILTER_JUNK           124/124   FILTER_RANGE           60/60
             FILTER_WEAPON         110/110   FILTER_ORE             33/33
             FILTER_ITEM_FOOD       98/148   FILTER_ITEM_ROD        32/32
             FILTER_ITEM_SPELLBOOK   92/92   FILTER_CONTAINER       25/25
             FILTER_ITEM_POTION      82/82   FILTER_SHIELD          24/24
             piu' una coda di diciannove minori
    -----------------------------------------------------------------
    416 righe fatte su 1.449 vive; **1.088 restano**

⚠️ **Dove «da fare» e «vive» non coincidono, c'e' un moltiplicatore**, e sono
due categorie: il cibo (98 su 148), per le quattro firme generiche dell'indice 2
che il lotto 026 ha sfruttato, e gli attrezzi (154 su 204), per le righe di
indice 1 e 2 condivise fra oggetti gemelli. Nel mobilio il rapporto era uno a
uno, e il lotto rendeva quanto pesava.

⚠️⚠️ **E il totale di questa tabella deve coincidere con quello di
`verifica --dizionario`.** Sono due conti fatti da due parti diverse — uno
partendo dalle categorie del sorgente, l'altro dal dizionario — e la 114a li ha
visti coincidere tre volte: **1.281** in apertura, **1.138** dopo il mobilio,
**1.088** in chiusura. Un totale che torna da due strade e' l'unica ragione per
credere alla tabella.

## Due lotti, 361 rese, 417 righe a schermo — 2026-08-27, centonovesima sessione

`db_item.hsp`, indice 3 (il rapporto di identificazione), due categorie:

    004  FILTER_ITEM_TOOL    143 firme -> 166 righe   margine 3
    005  FILTER_FURNITURE    218 firme -> 251 righe   margine 3
    -----------------------------------------------------------------
    **361 firme rese**, che coprono **417 righe** del sorgente
    applica 27.793 -> **28.210**   (+417 esatte)
    db_item non tradotte 2.394 -> **2.033**   (-361 esatte)
    rese dell'indice 3: 442 -> **693** su 1.319
    tetto secco: introdotte dall'italiano **0** in tutt'e due i lotti
    rinviate: nessuna   toppe: nessuna   test: **794**, invariato
    strumenti nuovi: 3 (`_monta`, `_coerenza`, `_elenco`, in `scratchpad/lotti-109/`)
    build: SI', **03:05 del 27/08**
    -----------------------------------------------------------------

**Il conto dell'indice 3, categoria per categoria**, con
`python scratchpad/_107-lotti-per-categoria.py --indice 3`:

    fatte    cibo 133/56 · pozioni 77/65 · pergamene 66/65 (108a)
             attrezzi 166/143 · mobilio 251/218 (109a)
    restano  FILTER_WEAPON        105/105    FILTER_ITEM_ROD       32/30
             FILTER_JUNK           97/81     FILTER_SHIELD         23/23
             FILTER_ITEM_SPELLBOOK 82/82     FILTER_ITEM_BOOK      23/20
             FILTER_RANGE          56/55     FILTER_CONTAINER      22/21
             FILTER_ORE            33/21     FILTER_ARMOR          20/20
             piu' una coda di venti minori
    -----------------------------------------------------------------
    693 righe fatte su 1.319; **626 restano**

⚠️ **Il rapporto righe/firme non si ripete da una categoria all'altra**, e
decide quanto rende un lotto: il cibo stava a 2,4 righe per firma, il mobilio a
1,15, gli attrezzi a 1,16, e quasi tutte le altre stanno a **una firma per
riga** — cioè costano quanto pesano. Le eccezioni utili che restano sono
`FILTER_JUNK` (97/81), `FILTER_ORE` (33/21) e `FILTER_ITEM_BOOK` (23/20).

## ⭐⭐⭐ Il conto vivo, e da oggi si misura — 2026-08-25, novantasettesima

    python scratchpad/_97-quanto-resta.py

    file                     non tradotte  rinviate  DA FARE
    db_card.hsp                         2         2        0   ⭐ CHIUSO nella 106a
    tcg.hsp                             2         2        0   ⭐ CHIUSO
    system.hsp                          1         1        0   ⭐ CHIUSO
    proc.hsp                            7         7        0   ⭐ CHIUSO
    map_user.hsp                        1         1        0   ⭐ CHIUSO
    map.hsp                             1         1        0   ⭐ CHIUSO
    main.hsp                           10        10        0   ⭐ CHIUSO
    item_func.hsp                      37        37        0   ⭐ CHIUSO
    item.hsp                            2         2        0   ⭐ CHIUSO
    init.hsp                            1         1        0   ⭐ CHIUSO
    db_creature.hsp                     4         4        0   ⭐ CHIUSO
    custom_ai.hsp                       1         1        0   ⭐ CHIUSO
    command.hsp                        26        26        0   ⭐ CHIUSO
    chat.hsp                            6         6        0   ⭐ CHIUSO
    chara_func.hsp                      4         4        0   ⭐ CHIUSO
    action.hsp                          2         2        0   ⭐ CHIUSO
    -----------------------------------------------------------------
    TOTALE                            110       110        0   ⭐⭐⭐ zero da fare

⚠️⚠️ **`verifica --dizionario` conta le rinviate dentro le «non tradotte»**, e
da quando i file si chiudono quel numero non risponde piu' alla domanda «quanto
manca». La 95a l'ha scritto a mano per `chat.hsp` («il 6 vuol dire zero»), la
96a per `item_func.hsp` («il 37 vuol dire zero»), la 97a per altri cinque file:
una frase per file, ricopiata di sessione in sessione. Adesso e' un comando, e la
tabella qui sopra si rifa' con quello.

⭐⭐⭐ **E dalla 106a il perimetro `lang()` e' CHIUSO.** `db_card.hsp` era
l'ultimo file, aperto dalla 102a con 239 rese su 1.144: la 106a ha reso le
ultime **444** e lo ha portato a zero. La colonna «DA FARE» e' zero su **tutti**
i file che hanno un dizionario, e le 110 «non tradotte» che restano sono le 110
**rinviate**.

⚠️ **Zero da fare non vuol dire finito**, e i tre numeri che restano lo dicono:
`perimetro.py` da' **86%** contando anche il testo fuori dal perimetro `lang()`,
le **5.284 descrizioni degli oggetti** di `db_item.hsp` non sono mai entrate in
nessuna di queste tabelle, e i **nove file senza dizionario** nemmeno.

⚠️⚠️ **Il numero di partenza era sbagliato di due, e nessuno lo aveva
misurato.** `estrai --da-tradurre` rende **1.146** voci, ma `:11405` e `:11412`
sono **spente con un `;`** — la vecchia `hard gay` sostituita da
`explosioman`. `estrai` le righe morte non le filtra: le filtra il modello di
lotto, cioe' un passo dopo. Quindi il lavoro vero e' **1.144**, non 1.145.

⚠️ La tabella grande qui sopra resta ferma e somma sessioni diverse: il conto
vivo lo danno questo modulo per il perimetro `lang()` e
`python scratchpad/perimetro.py` per il totale vero (**95%** dichiarato, **70%**
col testo fuori perimetro).

⚠️ **E i file senza dizionario non compaiono in nessuna delle due tabelle**: sono
nove, punto 17 della ripresa, e il piu' grosso e' `txtadv.hsp` con 170 `lang()`.

---

## Fuori dalla Fase 1

`db_creature.hsp` non è in Fase 1, ma dal 2026-08-11 è il file su cui si lavora
insieme a `proc.hsp`: le sue **battute** sono le stringhe a frequenza più alta di
tutto il gioco. Vedi `decisioni.md`, 2026-08-11.

Le 3.655 firme del file, misurate con `strumenti/creature.py` più il dizionario:

| classe | rese | da fare |
|---|---|---|
| nome | **1.131** | 0 ⭐ chiusi |
| battuta (`voce`) | **2.519** | 0 ⭐ chiuse |
| senza classe | 1 | 0 |
| rinviate (righe commentate) | — | 4 |
| **totale** | **3.651** | **4** |

⭐ **Aggiornato a fine trentunesima sessione (2026-08-13): il file è chiuso.**
Le quattro voci che restano sono le righe commentate rinviate apposta, e
`verifica --dizionario` continuerà a contarle per sempre. Fuori conto resta
`86293`, la battuta col ramo inglese vuoto, che `estrai.py` non vede nemmeno.

Le battute si sono chiuse in tre tappe: i lotti `015`-`026` della 27ª coprono i
livelli **6-45** — le creature di citta', i PNG di trama e i primi sotterranei;
i dieci lotti `027`-`036` della 30ª i livelli **45-157**, cioè i PNG delle
gilde, i boss di trama e i mostri di Nefia profonda; i sei lotti `037`-`042`
della 31ª tutto il resto, **159-1200**: i demoni, gli dèi del Patto Eterno, gli
otto dèi di Elona e le loro forme potenziate.

⚠️ **Il file è chiuso nel dizionario, non a schermo.** Delle 2.519 battute rese
ne sono state viste in gioco poche decine. Vedi `RIPRESA-sessione.md`, «Il
collaudo, punto per punto».

⚠️ **I nomi risultano chiusi solo dopo la 27ª**, e l'ultimo che i conteggi
mostravano da fare **non esisteva**: stava su una riga commentata
(`db_creature.hsp:105060`), e la riga viva sotto era gia' tradotta. Le 4
rinviate sono tutte righe commentate senza nessuna occorrenza viva: `estrai` le
toglie dai lotti, `verifica --dizionario` continua a contarle fra le non
tradotte. Vedi `decisioni.md`, 2026-08-12.

Quanto segue vale da fine ventiseiesima sessione (2026-08-11). Le battute rese
sono passate da 546 a 960 in un giorno — quattordici lotti, `fase2-battute-001`
… `-014` — e sono **tutte su creature di livello 1-6**, cioe' gli abitanti delle
citta'. Non e' un caso: da questa sessione i lotti si compongono in **ordine di
livello crescente** e non piu' in ordine di riga. Vedi `decisioni.md`, la
sezione sull'ordine dei lotti.

⚠️ **Il conto delle battute è cambiato di significato il 2026-08-11.**
`strumenti.creature` ne dichiarava **320** e il numero era sbagliato: il ramo
inglese di una battuta sta dentro `cnvtalk()`, e la classificazione ne vedeva un
ottavo. Ora sono **2.465** firme in tutto. Un confronto con un numero scritto qui
prima di quella data non ha senso.

⚠️ `strumenti.creature` stampa **2.466** e non 2.465: conta le **coppie
(giapponese, inglese)** delle righe, e una di esse non diventa una firma a sé.
I due numeri misurano cose diverse e non vanno sommati fra loro.

⚠️ **Il denominatore di `text.hsp` è sceso da 1.740 a 1.720** il 2026-08-11: le
20 firme di `elename()` non erano arretrato ma **rinviate**, e ora che sono
tradotte sono passate dal fuori-conto al numeratore. Le 2 che restano aspettano
`data/talk.txt`, e il file è **chiuso**.

⚠️ **Due di questi 100% sono falsi, e il 2026-08-10 si è misurato di quanto.**
`db_item.hsp` ha **261** `iknownnameref` — i nomi che il gioco mostra prima
dell'identificazione, tipo `colorful eyes` — e `custom_tweaks.hsp` ha **77**
etichette del menu opzioni: nessuna delle due classi passa da `lang()` né
dall'estrattore, quindi non sta né al numeratore né al denominatore. In tutto
sono **391 stringhe visibili** sparse su nove file. Non è un errore di calcolo:
il denominatore conta solo ciò che l'estrattore sa vedere. Il dettaglio, il
censimento e l'ordine con cui affrontarle stanno in `decisioni.md`, 2026-08-10.

⚠️ Le 2 firme che mancano ad `action.hsp` **non sono arretrato**: sono le due
righe rinviate a toppa (`:4584`, l'articolo inglese davanti a un'arma unica, e
`:9631`, il possessivo `his(tc, 1)` che in italiano si omette). Il file è
chiuso; il conto le porterà per sempre. Vedi `decisioni.md`, 2026-08-10.

Fuori dalla Fase 1, con conteggio proprio: `db_creature.hsp`, **1.452 firme su
3.655** — tutti e 1.131 i nomi, l'epiteto e le **320 stringhe di voce**, chiuse
il 2026-08-10. Le 2.203 righe rimanenti del file sono dialoghi e descrizioni.

⚠️ **Tre file nuovi nel perimetro dal 2026-08-10**, entrati per riparare le
rinomine all'evoluzione (vedi `decisioni.md`, diciottesima sessione). Non erano
nel piano della Fase 1 e hanno un conteggio proprio:

| file | tradotte | resta | perché è entrato |
|---|---|---|---|
| `custom_enemyevolution.hsp` | **368** | **0 — chiuso** | 418 letterali `evold`/`evname` rimasti inglesi |
| `ai.hsp` | 6 | 94 | 16 letterali, stessa causa |
| `event.hsp` | 5 | 649 | 6 letterali, stessa causa |
| `init.hsp` | 6 | 133 | già nel perimetro da prima |
| `chara_func.hsp` | **45** | 286 | 2026-08-11: chiude la frase di combattimento, vedi sotto |
| `buff.hsp` | **136** | 63 | 2026-08-13: `buffname` (29ª) e `bufftxt` (31ª) chiusi; restano i `buffdesc` |

## Sette lotti, 73 rese, e `chat.hsp` si chiude — 2026-08-25, novantacinquesima sessione

Sette lotti in due giri, **73 rese** piu' una rifatta, e `chat.hsp` va da **79
firme a zero**. Il file piu' grande del progetto e' **finito**.

Primo giro: CRAY + MARY + JENNA, che chiude l'imbocco della Valle di Raskilis
(8); TONI + NANCY + CARTER, che e' **Raskilis Sud per intero** (14); NERES +
RYUTYE, i due smemorati (8). Secondo giro: la **Gabbia di Amur**, cinque
parlanti in una mappa sola (14); HALION + FRON + RENAI (11); WEL + ROVID + BURT
(12); e la coda del file — NEW_CITIZEN, l'apparecchio di comunicazione, RATIN e
il Re dei Gusci di Vindale (6).

**Il conto di `chat.hsp` alla chiusura:**

    verifica --dizionario   chat.hsp   0 da ritradurre, 6 non ancora tradotte
    _87-parlanti-oltre.py              0 da fare dentro i blocchi, 0 fuori

⚠️ Le **6** non sono lavoro: sono tutte in `rinviate.jsonl` e sono tutte righe
**commentate a monte** — `:13991`, `:14036`, `:14037`, `:14038` (il blocco
vecchio di AJETALIO) e `:19327`, `:19334`. Rilette una per una in chiusura. Il
numero va **letto**, non confrontato: da qui in avanti resta 6 e vuol dire zero.

⚠️⚠️ **E per otto sessioni quel conto era diverso da quello vero.** La mappa dei
parlanti non toglieva le rinviate e tre script decidevano «tradotta» con
`.strip()` mentre `verifica.py` no. Tutti e tre allineati oggi; vedi
`decisioni.md`.

**La resa rifatta:** `chat.hsp:15440` (JENNA, 91a) diceva «fessura» dove
`action.hsp:2854` — la riga che il giocatore legge **camminando sulla casella** —
dice «fenditura». Stesso oggetto, stessa mappa, due nomi.

**Il perimetro dopo oggi** (`python scratchpad/perimetro.py`): perimetro
dichiarato **23.311 firme, 95% fatto**; totale col testo fuori perimetro
**31.528, 70%**. I grossi che restano:

| file | non ancora tradotte |
|---|---|
| `db_card.hsp` | **1.146** |
| `command.hsp` | **93** |
| `system.hsp` | **41** |
| `init.hsp`, `main.hsp` | 10 e 10 |
| `proc.hsp` | 7 |
| il resto (nove file) | 1-4 ciascuno |

piu' la **famiglia dell'impaginazione** di `data\` che nessun conteggio `lang()`
copre: `book.txt` 2.208 righe, `manual_ENG.txt` 591, `exhelp.txt` 185.

## Otto lotti, 55 rese, e una parola che l'inglese butta due volte — 2026-08-25, novantaquattresima sessione

Otto lotti in due giri da quattro, **55 rese**, e `chat.hsp` scende da 134 a
**79**: il 41% delle firme rimaste. Primo giro AIKAGE il ninja dalla maschera
demoniaca (8), KARATA la mascotte del seminario (8), MANSON l'avventuriero
prudente (7), RAIZEL il vecchio mago (7, il resto del suo blocco); secondo giro
SAIMEF il dio cane (7), BONYAC il merciaio (6), MELUGAST type0 (6), ZISILION il
re sfaccendato delle miniere (6). `menu_dialogo` misura **1.374** voci (erano
1.369), 0 fuori misura e 0 peggiorate a due colonne. Zero toppe, zero rinvii,
zero rese rifatte, zero dichiarazioni nuove in `invariati.md`; **una rete
nuova**, una sezione di glossario con 14 voci e un concept nuovo nel vault.

⭐⭐⭐ **La stessa parola, buttata dall'inglese due volte nello stesso giorno.**
露払い — chi va avanti a sgombrare la strada — regge la scena di AIKAGE
(`:15078`) e quella di SAIMEF (`:9703`), due personaggi che non si incontrano
mai. Nella prima l'inglese la **capovolge** («personal bodyguards», cioe' chi
sta a fianco invece di chi apre il varco); nella seconda la fa sparire dentro un
«For the sake of my followers, I must stop my quest here», dove 後続 — quelli che
vengono dietro — e' letto come i suoi fedeli. Il progetto l'aveva gia' resa
nell'88a: «se non aveste **ripulito la strada**, non sarei arrivata in tempo». I
due lotti, scritti a ore di distanza, si sono tenuti per la mano solo perche' la
parola e' stata **cercata** e non tradotta a orecchio.

⭐⭐⭐ **Una resa dinamica puo' essere vietata dal sito.** `chat.hsp:9705` in
giapponese e' `"(突然、" + name(tc) + "は…"` e in inglese e' un letterale che
inchioda «Saimef». La voce risulta `statica` — la classe la decide il lato che
si **sostituisce** — e `applica.riscrivi_statica` avvolge la resa in virgolette
e basta: un `" + name(tc) + "` scritto nel dizionario finirebbe a schermo come
testo. Rete nuova, `scratchpad/_94-jp-dinamico-en-statico.py`: **335 siti su
21.801**, in undici file, `chat.hsp` da solo 286, e **tutti gia' resi**.

⚠️⚠️ **E la stessa rete ha trovato una cosa peggiore, non riparata.** In alcuni
di quei 335 l'inglese non traduce, dice **un'altra frase**: `action.hsp:8694`
(«la forza di X e' cresciuta») ha per inglese il testo di `:9375`;
`action.hsp:15276` («X e' passato a Y») ha «Current Ammo Type»;
`calculation.hsp:1556` ha «A dimensional door opens in front of you». Le rese
italiane hanno seguito l'inglese e si sono portate dietro l'errore. **Da
guardare.**

⭐⭐ **Il conteggio delle firme non dice dove sta un parlante.** La ripresa dava
BONYAC per «un negozio, che si apre molte volte per partita»; `map.hsp:5042` lo
mette in `ras05`, la bottega abbandonata in fondo alla Valle di Raskilis. La
priorita' era giusta per la ragione sbagliata, e lo dice **`map.hsp`**, non il
conteggio.

⭐ **Il perimetro di `chat.hsp` dopo oggi.** Restano **79** firme e il blocco
piu' grosso ne ha **7**: SAIMEF chiuso, la testa e' ora TONI il pescatore (5),
CARTER (5), ALFRED (5), HALION (5), RENAI (5), CHILD_WEL (5). Da qui in avanti
il costo per resa e' al massimo storico e conviene **raggruppare quattro
blocchi per giro**, come si e' fatto oggi due volte.

## Otto lotti, 87 rese, e tre registri gia' decisi altrove — 2026-08-24, novantatreesima sessione

Otto lotti, **87 rese**, e `chat.hsp` scende da 221 a **134**: il 39% delle
firme rimaste, come ieri. NORNE la guida (11), LEIKI la tartaruga nera (15),
MELUGAST AO-I (12), SPIPHA la cacciatrice di draghi (12), ARIBEL la monella
(10), ALSAPIA la maschera bianca (9), SINAHA (9), ARASIEL della tempesta di
sabbia (9). `menu_dialogo` misura **1.369** voci (erano 1.357), 0 fuori misura
e 0 peggiorate a due colonne. Zero toppe, zero rinvii, zero reti nuove, zero
strumenti toccati, zero dichiarazioni nuove in `invariati.md`; una sezione nuova
di glossario con 18 voci e un concept nuovo nel vault.

⭐⭐⭐ **In cinque lotti su otto il registro non si decideva nel lotto**, e in
ogni caso stava in un posto diverso: in un altro file del gioco (Leiki da' del
tu per `map.hsp:15070`, malgrado il keigo), nelle battute di combattimento della
creatura (Aribel e le sue «sette regole», `db_creature.hsp:62712`), in un lotto
precedente **dello stesso parlante** (il blocco del Melugast non e' di una
creatura ma di una **radio**: parla Gavela, reso nell'85a), o in una particella
gia' risolta su un'altra creatura (il ニャ di Sinaha, tre precedenti). Nel
vault: [[il-registro-non-si-decide-si-trova]].

⭐⭐⭐ **Un refuso di monte si conta, non si ricopia.** `chat.hsp:13191` scrive
«A0-I» **con lo zero**, in giapponese e in inglese; sei altri siti scrivono
AO-I con la lettera O, in tutt'e due le lingue, e cosi' fa l'identificativo.
Ricopiarlo avrebbe dato **due nomi alla stessa macchina** a un menu di distanza.

⚠️⚠️ **Il numero di un referto va letto, non confrontato.** `referti.py` e'
salito da 8 a **9** dentro il lotto di Spipha, e la riga nuova era innocua
(l'idiomatico «te la sei cavata», gemello di `:22872` gia' dichiarato). Ma nello
stesso lotto ce n'era **una vera che il referto non vede** — «Sei stato tu ad
abbatterlo, vero?», participio riferito al giocatore — trovata solo rileggendo
le nove rese una per una. ⭐ Il conto resta **9** in chiusura, e il nono e'
dichiarato.

⭐⭐ **La domanda della 90a ha dato due risposte opposte nello stesso lotto.**
Su `chat.hsp:8702` la riga in piu' era **mia** (il vocativo lungo che evita il
genere al posto di «Adventurer») e si e' riassorbita girando la frase; su
`:8706` era **dell'inglese**, che butta la citazione dei forti partiti. E
`:13201` ha **sfondato il tetto** — 15 righe contro le 13 di `chatMore`, mentre
l'inglese ci sta esatto — e per rientrare sono serviti due giri di potatura
senza togliere nessuna delle nove voci dell'elenco tecnico: su un elenco di
termini composti l'italiano paga circa il **15%** in piu'.

⚠️⚠️ **Il conto delle rese non e' il conto delle prove.** 87 rese costruite e
controllate dagli strumenti; **zero viste a schermo**. Con oggi l'arretrato del
collaudo e' di **undici sessioni e 2.003 rese** — ma stavolta c'e' un punto
facile, perche' NORNE e' il personaggio che ogni partita nuova incontra per
primo.

⭐ **Il perimetro di `chat.hsp` dopo oggi.** Restano **134** firme e non c'e'
piu' niente sopra le **otto**: AIKAGE (8), KARATA il mascotte del seminario (8),
MANSON (7), RAIZEL (7), SAIMEF il dio cane (7), BONYAC (6), ZISILION (6),
MELUGAST type0 (6). La mappa
(`python scratchpad/_87-parlanti-oltre.py`) e' quasi piatta: da qui in avanti i
lotti valgono meno di dieci rese l'uno.

## Nove lotti, 143 rese, e due elenchi che andavano riconosciuti — 2026-08-24, novantaduesima sessione

Nove lotti, **143 rese**, e `chat.hsp` scende da 364 a **221**: il 39% delle
firme rimaste in un giorno. AMURDAD (12), l'AIUTANTE DEL MAESTRO SPADA ROSSA
(18), MIKRAANESIS (18), SHURAIDA (17), ALICE (17), LANKATA (16), MANYTIA (15),
BETHEL (15), BELPHAT (15). `menu_dialogo` misura **1.357** voci (erano 1.323),
0 fuori misura e 0 peggiorate a due colonne. Zero toppe, zero rinvii, zero reti
nuove, zero strumenti toccati; **due** dichiarazioni nuove in `invariati.md` e
una sezione nuova di glossario con 22 voci.

⭐ **Nove zone chiuse su nove, contraccolpo zero.** `_85-blocco.py` non ha mai
segnalato occorrenze fuori: la lezione della 91ª è stata applicata in apertura
di ogni lotto, e stavolta non ha mai dovuto mordere. Tre blocchi erano **tutti
da fare** (LANKATA, BETHEL, e MIKRAANESIS a meno di due firme).

⭐⭐⭐ **Due elenchi di katakana non chiedevano una traduzione: chiedevano di
essere riconosciuti.** I ventotto nomi di Mikraanesis (`:9409`-`:9412`) sono gli
**eoni valentiniani** — e la prova non sta nell'elenco ma nella trama, che usa
già Sophia, il Propator dell'Abisso (`:9423`) ed Enthumesis, che nel mito è la
passione di Sophia staccata da lei (`:10213`). Il diario di viaggio di Belphat
(`:12576`-`:12594`) è il **Ciclo di Cthulhu**, e lì la prova sta nel dizionario:
«lo shoggoth» (`db_creature.hsp:80712`) e «la Grande Razza di Yith»
(`db_card.hsp:14390`). L'inglese traslittera a orecchio in tutti e due i casi:

    アウトピュエース  Outpuece    -> Autophyes     ユゴス      Yugos      -> Yuggoth
    アキネートス     Aquinatos   -> Akinetos      バイアクヘー Bayakhae   -> Byakhee
    ヌース           Nuus        -> Nous          サイクラノーシュ Cyclanorch -> Cykranosh

💡 E su **due** voci l'errore di riconoscimento cambia la parola, non la grafia:
独り子のモノゲーネス è l'**Unigenito** e l'inglese scrive «Monogenes of
Solitude»; イス焼き è **Yith alla piastra** (in coppia con たこやき nella stessa
frase) e l'inglese, leggendo イス come *ice*, scrive «fried ice cream». Nuovo
concept nel vault: [[un-nome-non-si-traduce-si-riconosce]].

⭐⭐⭐ **Un parente regalato al giocatore, e il codice che lo smentisce.**
`:13837`, l'inglese: «I was able to rescue **your** father». Il padre di Lankata
ha un identificativo, `CREATURE_ID_ALFRED_THE_CANGNAN_WIND`, e la scena in cui
lo trova sta venti righe più in là ed è **già resa**: `:18131` lo crea, `:18138`
è lei che dice «Padre!», `:18155` è **lui** che chiede «Io... sono salvo?». Il
giocatore in Elona un padre non ce l'ha. 💡 *Un pronome possessivo inglese si
verifica come un identificativo: dice chi è parente di chi.*

⭐⭐ **Tre righe già nel dizionario riparate, e nessuna era raggiungibile dalle
reti.** `:269` dava **un genere al giocatore** in una delle prime battute della
storia («Norne, hai fatto bene a guidare *la tua amica* fin qui», dove il
giapponese non ha oggetto); `:10211` chiamava lo stesso 《深淵のプロパトル》
`<Prophatorl dell'abisso>` mentre `:9423` dice `<Propator dell'Abisso>`;
`:13714` diceva `99999gp` dove le due voci gemelle dello stesso menu dicono
`99999 oro`. ⚠️ Sono tutte e tre **frasi diverse fra loro**, quindi
`battute --divergenti` non le confronta e `verifica --dizionario` guarda solo le
firme: le ha trovate la lettura del vicinato, non uno strumento.

⭐ **E una quarta correzione è arrivata dentro il lotto:** `referti.py` è salito
a 9 e ha visto «dove *sarai finito*» (`:12602`), un participio in più che il
giapponese non ha — 「どこにいるんだ」 è «dove sei». È il quarto lotto di fila in
cui quella rete guadagna il suo posto **durante** il lavoro e non in chiusura.

⭐⭐ **Le battute doppie e le parodie hanno un vincolo di forma, non di senso.**
「アリーヴェデルチ！」 di Alice è insieme una parola straniera e una parola che
comincia per アリ, *formica*, come il suo nome: rifatta come il «formicalità»
della 90ª sullo stesso personaggio, **ARRIFORMICARCI!**. 「サンキューベリマッチ」
resta in inglese perché lo suggerisce l'inglese stesso, che scrive «Arigatou
gozaimashita!». E `:13852` («posate **la statuetta** e lasciate **questo
mondo**») è la parodia di `:13856` («posate **le armi** e lasciate **questo
piano**»), che è il `buff` sopra il menu: si leggono nello stesso istante,
quindi devono usare gli stessi verbi.

⚠️⚠️ **Il conto delle rese non è il conto delle prove.** 143 rese costruite e
controllate dagli strumenti; **zero viste a schermo**. Con oggi l'arretrato del
collaudo è di **dieci sessioni e 1.916 rese**.

⭐ **Il perimetro di `chat.hsp` dopo oggi.** Restano **221** firme e il blocco
più grosso è LEIKI (15); poi MELUGAST (12), SPIPHA (12), NORNE la guida (11),
ARIBEL (10). La mappa (`python scratchpad/_87-parlanti-oltre.py`) non ha più
niente sopra le quindici: il costo per resa continua a salire, come previsto
dalla 91ª.

## Otto lotti, 153 rese, e la rete che ha chiesto il lotto — 2026-08-24, novantunesima sessione

Otto lotti, **153 rese**, e `chat.hsp` scende da 517 a **364**: un altro quinto
delle firme rimaste. NEIN (24), ALLEN (23), GARZIEM (22), SSIL (20), L'ANIMA
SMARRITA (20), JIN (19), REGULUS (19), RAIZEL (6). `menu_dialogo` misura
**1.323** voci (erano 1.292), 0 fuori misura e 0 peggiorate a due colonne. Zero
toppe, zero rinvii, zero reti nuove, zero strumenti toccati.

⭐⭐⭐ **L'ottavo lotto non era in programma: l'ha chiesto `bilingui`.**
Chiuso REGULUS, `strumenti.bilingui` è passato da **0 a 1**:

    chat.hsp:12832-12833   2 voci, 1 rese, 1 no
            :12832  'Hold on a minute.'

La firma di 「ちょっと待って」 ha **due occorrenze**, `:10398` e `:12832`, e
`estrai --da-tradurre` la assegna alla prima: rendendo `:12833` senza di lei il
menu di Regulus era rimasto metà in italiano e metà in inglese. ⚠️ E renderla
da sola avrebbe **spostato** il difetto di quaranta righe, perché sarebbe
diventato bilingue il menu dell'altro blocco. La riparazione è stata chiudere
il blocchetto di RAIZEL per intero, sei firme. 💡 *Una firma condivisa non
appartiene al lotto che la incontra per primo: appartiene a tutti i menu in cui
compare, e si chiude con loro.* `bilingui` è tornato **0**.

⭐ **Sette zone chiuse su otto, contraccolpo zero.** L'unico blocco con una
occorrenza fuori era REGULUS, ed era proprio quella firma condivisa —
`_85-blocco.py` l'aveva detto in apertura di lotto, e la conseguenza si è vista
solo dopo la reimportazione, quando `bilingui` ha parlato. La misura c'era, la
lettura no.

⚠️⚠️ **Il conto delle rese non è il conto delle prove.** 153 rese costruite e
controllate dagli strumenti; **zero viste a schermo**. Con oggi l'arretrato del
collaudo è di **nove sessioni e 1.773 rese**.

⭐ **Il perimetro di `chat.hsp` si è appiattito.** Dopo oggi non c'è più nessun
blocco sopra le **18** firme: la mappa (`python scratchpad/_87-parlanti-oltre.py`)
comincia con PART_TIME_WORKER_THE_RED_SWORD (18), MIKRAANESIS (18), SHURAIDA
(17) e ALICE_THE_BIG_ANT (17) — che è la formica di MARY, resa ieri. Le
sessioni che vengono non avranno più un lotto grosso da cui partire: saranno
molti blocchi piccoli, e il costo per resa sale.

⭐⭐ **Le reti hanno fermato tre difetti prima del dizionario**, e nessuna delle
tre era quella che ci si aspettava: `referti.py` (da 8 a 9 participi) ha visto
un «ci sei riuscito» riferito al giocatore che `verifica` e `chat-lotto-misura`
non potevano vedere; `verifica` ha bocciato **due trattini lunghi** (CP932 li
codifica su due byte) e una **virgoletta nuda** dentro una statica.

⭐ **Sulle righe più lunghe dell'inglese la regola della 90ª ha retto e si è
affinata.** Diciannove segnalate in tutto: **dodici** erano prolissità nostra e
sono state accorciate; **cinque** erano righe dove l'inglese aveva buttato un
pezzo (il *prezzo* dell'occhio finto di Quruiza, il 超生命, la frase in cui
Regulus dice che alla sorella darà pace, il 旧型 del Meshera, la frase del
titolo della missione di Jin); **due** sono state dichiarate per quel che sono,
italiano più lungo e basta. 💡 Il terzo mucchio è nuovo: dire «qui non ho una
scusa» costa una riga di modulo e vale più di una scusa inventata.

## Cinque lotti, 174 rese, e un quarto di `chat.hsp` in un giorno — 2026-08-23, novantesima sessione

Cinque lotti, **174 rese**, e `chat.hsp` scende da 691 a **517**: il file perde
un quarto delle firme rimaste in una sessione sola. KARAVIKA (41), BYSYMLHA
(38), MELGET (32), MARKA (32), MARY (31). `menu_dialogo` misura **1.292** voci
(erano 1.245), 0 fuori misura e 0 peggiorate a due colonne; `chat-lotto-misura`
**0 fuori misura** in tutti e cinque i lotti. Zero toppe, zero rinvii, zero
reti nuove, zero strumenti toccati.

⭐ **Cinque zone chiuse su cinque, e il contraccolpo misurato dieci volte.**
Ogni lotto è stato passato due volte prima di cominciare: `_85-blocco.py` per le
occorrenze fuori dal blocco, e una ricerca per **firma** su tutti i
`dizionario/*.jsonl` per gli altri file. Tutte e dieci le misure hanno dato
zero. Non è fortuna: è che dopo la 89ª restavano in cima alla mappa i blocchi
che il referto dei parlanti dichiarava chiusi, e sceglierli in quell'ordine
costa zero contraccolpo per costruzione.

⚠️⚠️ **Il conto delle rese non è il conto delle prove.** 174 rese costruite e
controllate dagli strumenti; **zero viste a schermo**. Con oggi l'arretrato del
collaudo è di **otto sessioni e 1.620 rese**. Vedi `RIPRESA-sessione.md`, punto
2 di «Quel che resta aperto», dove stanno i tre punti più facili da guardare.

⭐⭐⭐ **La misura che ha cambiato metodo: «di chi è la riga in più?».**
`chat-lotto-misura` ha segnalato **ventitré** rese più lunghe dell'inglese.
Venti erano prolissità nostra e sono state accorciate; **tre no**, ed erano
esattamente le righe dove l'inglese aveva tagliato il giapponese — accorciarle
avrebbe ributtato via lo stesso testo una seconda volta. Il tetto non mordeva in
nessuno dei ventitré casi (13 righe contro 7 al massimo). Vedi `decisioni.md`,
la 90ª.

## La collina di Dain: tre lotti, 98 rese, e un tetto ristretto — 2026-08-23, ottantanovesima sessione

Tre lotti, **98 rese**, e `chat.hsp` scende da 789 a **691**. `menu_dialogo`
misura **1.245** voci (erano 1.219), 0 fuori misura e 0 peggiorate a due
colonne; `chat-lotto-misura` **0 fuori misura e 0 peggiorate in tutt'e tre i
lotti**; `bilingui` **0** a fine giornata. `pytest` da 732 a **736**: quattro
prove nuove per la correzione di `menu_dialogo`. `referti.py` resta **8**.

    :10982-:11085  DAIN l'anziano della collina    38   1 fuori (reciproca)
    :11086-:11205  THALIA la guardastelle          28   zona chiusa
    :12332-:12559  URCAGUARY la gemma tenace       32   1 fuori (reciproca)

⭐⭐⭐ **I tre lotti sono una catena sola, e la catena e' stata misurata in
apertura.** `chat.hsp:11069` (「残念だ」 / «That's too bad.») e' una **voce di
menu** che DAIN e URCAGUARY si dividono: renderla per uno solo avrebbe lasciato
un menu a meta'. `_85-blocco.py` dato ai due blocchi nella stessa invocazione ha
mostrato che la catena e' **reciproca e si chiude li'** — quella firma e nessuna
altra — quindi il costo vero era 98 firme e zero fuori. THALIA e' entrata perche'
e' la coda della stessa missione, «Oltre centinaia di ere», e il diario
(`text.hsp:11428`-`:11508`) nomina tutt'e tre.

⚠️ **`bilingui` e' stato 1 nel mezzo**, fra la prima e la terza spinta: e' il
prezzo di lavorare per lotti, ed era previsto.

⚠️⚠️ **La correzione di rete e' il punto 5 della ripresa della 88a.**
`menu_dialogo` applicava il tetto delle due colonne (24 caratteri) a ogni voce
piu' lunga dell'inglese, dichiarando che il numero di voci di un menu «non e'
decidibile dal sorgente». Per un menu scritto a mano in `chat.hsp` lo e':
`init.hsp:47` fa `listmax++` e `chat.hsp:25217` azzera `listmax` in coda a
`*chat_select`, quindi le voci di un menu sono esattamente le `chatList` fra un
`gosub` e il successivo. Il taglio sta sotto `keyrange > 10` (`:25166`): delle
1.073 voci della pergamena, **166** stanno in menu sopra le dieci e 907 no.

## Due lotti e un referto: 99 rese, e la 87a riletta — 2026-08-23, ottantottesima sessione

Due lotti, **99 rese** piu' **cinque rifatte**, e `chat.hsp` scende da 888 a
**789**. `menu_dialogo` misura **1.219** voci (erano 1.193), 0 fuori misura e 0
peggiorate a due colonne; `bilingui` **zero al primo giro in tutt'e due i
lotti**, e MAILE ha dato **0 peggiorate** anche a `chat-lotto-misura`.
`pytest` resta **732**: nessuno strumento della catena e' stato toccato.

    :11206-:11770  IRMA la forgiatrice straniera      51   zona chiusa
    :13266-:13516  MAILE la sacerdotessa fantoccio    48   zona chiusa

⚠️⚠️ **Le cinque rifatte non vengono da un lotto: vengono dal REFERTO.**
`referti.py` gira su tutto il dizionario e all'apertura segnalava **14**
participi dove la 86a ne contava 6. Letti uno per uno: otto falsi positivi
legittimi e **cinque difetti veri** — `:14435` (due), `:14448`, `:14490`,
`:16586` e `:14113`. Tre erano della 87a, che non aveva rilanciato il referto
in chiusura; uno stava li' dalla 82a. Adesso il referto dice **8**, ed e' un
valore atteso d'apertura.

⭐ **`referti.py` e' l'unico numero del progetto che sale da solo** quando
qualcuno scrive rese senza rileggerle. Per questo entra nelle verifiche di
chiusura e non solo in quelle d'apertura.

⚠️ **Il tetto delle due colonne ha morso per la prima volta sul serio**: il
menu di MAILE ha **undici** voci, e sopra le dieci `chat.hsp:25164`-`:25166`
taglia con `strmid` a 24 caratteri. Fino a oggi `menu_dialogo` lo segnalava
solo come «peggiorata rispetto all'inglese».

## Il seminario e' CHIUSO: quattro lotti, 281 rese — 2026-08-23, ottantasettesima sessione

Quattro lotti, **281 rese** (piu' due rifatte), e `chat.hsp` scende da 1.169 a
**888**. `menu_dialogo` misura **1.193** voci (erano 1.129), 0 fuori misura e 0
peggiorate a due colonne; `bilingui` ha dato **zero al primo giro in tutti e
quattro i lotti**. `pytest` scende a **732**: dodici prove tolte, non rotte
(vedi sotto).

    :13950-:14098  AJETALIO, il corso di vita quotidiana                    73
    :14099-:14240  CRESCE, il corso sugli oggetti                           70
    :14241-:14380  IDURU, il corso di crescita                              68
    :14381-:14524  MITO, il corso di combattimento                          70
    economy.hsp:357, text.hsp:18   due nomi che il tutorial smentiva  2 rifatte
    :13991, :14036-:14038          quattro righe morte               4 rinviate

⭐⭐⭐ **Il confine di ARASIEL non era un blocco: era una graffa commentata.**
`_86-parlanti-oltre.py` gli dava 958 firme e sedicimila righe, cioe' tutto il
resto del file; il blocco vero e' `:10729`-`:10876`, **148 righe e 9 firme**.
Il contatore toglieva solo i commenti `/* ... */` di **una riga sola**, e in
`chat.hsp` ce ne sono tre multiriga che portano una graffa spaiata (`:169`,
`:10752` proprio dentro ARASIEL, `:19629`). Tolti prima di contare, la
profondita' a fine file torna a **0**. `_87-parlanti-oltre.py` e' la mappa
giusta: 85 blocchi, e tutto quel che resta sta in blocchi sotto `:15490`.

⭐⭐ **Il tutorial e' il posto dove un nome sbagliato si vede.** Due rese
vecchie sono cadute per questo: `economy.hsp:357` diceva «Influenza» dove il
gioco dice «autorita'» in **otto** altri siti — era il punto aperto della 74a,
la statistica con due nomi sullo schermo — e `text.hsp:18` mandava il giocatore
«dal menu <examine>», che in italiano si chiama **<Esamina>**.

⭐⭐ **Chiusa meta' del punto aperto dalla 85a**: `chat-lotto-misura.opzioni()`
contava **sedici** bottoni dove il menu ne mostra quattro, perche' sommava le
`chatList` di guardie che si escludono a vicenda. Con sedici il tetto diventa
NEGATIVO e qualunque battuta risulta fuori misura. Adesso si raggruppano per
guardia e per ogni sinistra di `==` si prende il gruppo piu' numeroso.

⚠️⚠️⚠️ **E le sette etichette del potenziale non passano da `lang()`**
(`command.hsp:10676`-`:10700`, letterali nudi): nessuna rete le vede e a
schermo restano inglesi. E' il punto cieco della 74a un gradino piu' sotto.

⚠️ **Le dodici prove tolte da `pytest`** sono
`test_l_etichetta_italiana_non_porta_accenti`: vietavano l'accento nelle
etichette del prospetto cittadino per non dover contare l'imbottitura su una
forma che il file non mostra. Il conto pero' lo fa gia'
`test_l_etichetta_italiana_e_lunga_come_l_inglese`, sulla forma degradata, a
ogni giro. 💡 *Una precauzione si ritira quando la cosa da cui proteggeva e'
diventata una misura* — e si ritira invece di aggirarla con un'eccezione per un
sito solo.


## `*chat_unique` e' CHIUSA: cinque lotti, 326 rese — 2026-08-22, ottantaseiesima sessione

Cinque lotti, **326 rese** (piu' una rifatta), e `chat.hsp` scende da 1.495 a
**1.169**. `menu_dialogo` misura **1.129** voci (erano 1.076), 0 fuori misura e
0 peggiorate a due colonne; `bilingui` ha dato **zero al primo giro in tutti e
cinque i lotti**. `pytest` resta **744**: nessuno strumento e' stato toccato.

    :8459-:8694 + :12633-:12757  MIZUKI e KUROYA, legati da una voce di menu  74
    :951-:1586    la testa del file: Zeome, Orphe, i due Loyter, Miches, Shena 52
    :3316-:3463 + :3794-:3970    Raphael, Ainc, Renton, Marks, Noel            55
    :7114-:7430 + :7597 + :8253  Mefan, Caim, il bambu', Guo, Naplus           61
    gli ultimi otto blocchi       Karam, Balzak, i banditi, gli Elea, Siraha    84
    :2973                         il participio che accordava col giocatore      1

⭐⭐⭐ **`python scratchpad/_84-parlanti.py` adesso dice 0 su 86 blocchi.**
`*chat_unique` (`:947`-`:8629`) e' una **zona chiusa**: era 287 firme in 28
blocchi a inizio sessione. Quel che resta di `chat.hsp` — **1.169** firme —
sta tutto oltre `:8694`, e adesso ne esiste la mappa
(`scratchpad/_86-parlanti-oltre.py`, 25 blocchi).

⚠️⚠️ **La lezione: il divieto di genere non vale solo sul giocatore.** Il capo
dei banditi (`db_creature.hsp:115501`) e l'istigatore degli Elea (`:40979`)
**non assegnano `CDATA_SEX`**: leggono quello che il gioco ha tirato a caso e
cambiano solo la faccia. Vale su chiunque il codice non fissi, e si scopre solo
leggendo il blocco della creatura — nessuna rete lo vede.

⭐ E il SESSO si legge li' anche quando l'epiteto sembra bastare: MEFAN ha
`CDATA_SEX = 1`, cioe' femmina, e «la pifferaia» del nome della carta non era
una scelta di stile ma il dato.

⭐ **Una correzione che nessuna guardia avrebbe trovato**: `:2973` (Miral,
resa nella 84a) chiudeva con «Vabbe', **sei venuto** fin quaggiu'», un
participio accordato col giocatore. L'ha trovato `scratchpad/referti.py`, che
e' un REFERTO e gira su tutto il dizionario, non sul lotto.


## Tre blocchi legati da due firme, e una morfologia mai dichiarata — 2026-08-22, ottantacinquesima sessione

Tre lotti, **336 rese**, e `chat.hsp` scende da 1.831 a **1.495**.
`menu_dialogo` misura **1.076** voci (erano 1.017), 0 fuori misura e 0
peggiorate a due colonne; `bilingui` chiude a **0**. `pytest` resta **744**:
l'unico strumento toccato e' `funzioni.py`, e il test che lo copre esisteva
gia'.

    :1962-:2369   ERYSTIA la studiosa di storia: il filo principale di Palmia     107
    :7795-:8193   il Dr. GAVELA: la navigazione dimensionale, i quattro incarichi 118
    :10022-:10334 SOPHIA la Saggia: la cosmogonia in venticinque punti            111

⚠️ **Non sono tre lotti scelti, sono un lotto solo diviso in tre.** Due firme
condivise legavano Erystia a Gavela e a Sophia, e tutt'e due erano **voci di
menu** dentro menu che Erystia doveva avere interi: renderle apriva tre menu
bilingui in zone ancora inglesi. Il perimetro allargato si e' **misurato prima**
(`scratchpad/_85-blocco.py`, il confine sulla graffa per un blocco qualsiasi del
file, anche fuori da `*chat_unique`) e la misura ha deciso di prenderli tutti e
tre. Nel mezzo, pero', `bilingui` e' stato **3**: fra il primo commit e il terzo
l'albero portava tre menu a meta'.

⭐⭐⭐ **E la sessione ha trovato una morfologia inglese mai dichiarata.**
`cnvrank` (`init.hsp:149`) e' la desinenza ordinale — `2` in giapponese, `2nd`
in inglese — e non stava in `MORFOLOGIA_INGLESE`: **quattro rese italiane gia'
in dizionario scrivevano a schermo «Rango del museo: 2nd» e «Livello di
sotterraneo piu' profondo: 25th»**. La sonda del test cercava funzioni i cui
`return` fossero letterali nudi, e `cnvrank` invece **concatena** l'argomento
col suffisso: e' la seconda famiglia, e ora la sonda la riconosce. Le quattro
rese sono state rifatte.

⚠️ `*chat_unique` scende da 512 a **287** firme in 28 blocchi; il resto di
`chat.hsp` (1.208) sta oltre `:8694`.

## Nove lotti in chat.hsp, tutti presi sul parlante — 2026-08-22, ottantaquattresima sessione

Nove lotti, **301 rese**, e `chat.hsp` scende da 2.132 a **1.831**.
`menu_dialogo` misura **1.017** voci (erano 945) — oltre il migliaio — e
`bilingui` resta a **0**, zero al primo giro in tutti e nove i lotti.
`chat-lotto-misura` 0 fuori misura e 0 peggiorate. `pytest` **744**, invariato:
nessuno strumento e' stato toccato.

    :2399-:3124  i due FABBRI leggendari: Garok e Miral                     32
    :7431-:7596  LUNE la capo cameriera: la villa in vendita                39
    :6308-:6445  SILVIA la principessa: i tre gradini di carisma            29
    :8309-:8400  i tre NINJA di Tyris, piu' le cinque «Fama richiesta»      25
    :3971-:4812  ICOLLE il biochimico: le cinque cavie, le parti tolte      22
    :3464-:3793 + :7191-:7269  i CANI E I GATTI, piu' Naive Kyle            39
    :3581-:3709 + :5629-:5671  l'ESERCITO: Gilbert, Arnord, Conery          34
    :7645-:7794  IRVA PERDUTA: Milos, Carla, Stoke, Arma, Aile              36
    :6720-:7113  YERLES: Heinrich, Zernard, il Cane poliziotto, Milis, Orville  45

⭐ Il perimetro di ogni lotto e' stato preso sul **parlante**, non
sull'etichetta: `scratchpad/_84-parlanti.py` mappa i blocchi
`if ( _switch_val == CREATURE_ID_... )` di `*chat_unique` col confine vero
(la graffa che li chiude) e, per ognuno, le firme non tradotte e quante di
quelle vivono anche fuori. Sono 86 blocchi; a fine sessione ne restano 33 con
lavoro dentro.

⚠️ E ha corretto un confine che la ripresa dava sbagliato di 171 righe: il
blocco di **Mizuki** comincia a `:8459`, non a `:8630`.

## Sette zone chiuse in chat.hsp, e un buco nel perimetro dei nomi — 2026-08-21, ottantaduesima sessione

Sette lotti, **312 rese**, e `chat.hsp` scende da 2.444 a **2.132**.
`menu_dialogo` misura **945** voci (erano 881), `bilingui` resta a **0** — zero
al primo giro in tutt'e sette i lotti — `chat-lotto-misura` 0 fuori misura e 0
peggiorate, `pytest` **733** (erano 730).

    :16511-:16640  Leold ordinario: consigli d'avventura, obiettivi, risveglio   45
    :16047-:16510  la Culla del Caos: il finale, Orphe, Tezcatlipoca            103
    :1-:946 + :18805-:18840  le due code: guardie, Alfred, la coppia in tag      24
    otto pezzi     il pantheon: gli otto dei che si invitano a casa              27
    :6475-:6719    le sorelle e la Chiesa dell'Onda Sororale                     61
    :3125-:3315    Pael e Lily: la malattia dell'etere                           39
    :1587-:1961    la corte di Palmia: Stersha, Xabi, l'esploratore              13

⭐ **Sette zone, sette volte chiuse**: `perimetro-zona.py` ha dato zero firme con
occorrenze fuori in tutte, e il confine si e' preso sul **parlante**, non
sull'etichetta. Il pantheon e' una zona chiusa **a otto pezzi**.

⭐⭐ **Il lessico non si e' deciso, si e' ripreso dal DATO**: Sigillo Eterno,
Fattore Decisivo, zanna della luce nascente, Figlio del Caos, incarnazione,
Onda Sororale, Sguardo della sorella, malattia dell'etere, Risveglio di Nefia.
E per gli otto dei il **registro** era gia' scritto in `main.hsp:7201`-`:7229`,
la scena in cui il dio invitato arriva a casa.

⚠️ **Due rese vecchie corrette**: `screen.hsp:1388` faceva parlare Orphe al
femminile (ma `db_creature.hsp:46159` mette `CDATA_SEX` a 0 = maschio), e
`chat.hsp:6505` chiamava una creatura «H Sister» dove `db_creature.hsp:97006`
la chiama «la sorella minore sicaria».

⚠️ **Una guardia corretta**: `cnven` entra in `TRASPARENTI`
(`strumenti/funzioni.py`), perche' alza la prima lettera e non porta nessun
dato. Senza, `chat.hsp:18813` era intraducibile. Tre test nuovi.

⚠️⚠️⚠️ **E un buco nel perimetro**: `db_item.hsp` ha **261 righe
`iknownnameref` col ramo inglese**, **217 stringhe distinte** — i nomi che
l'oggetto porta prima di essere identificato — e `estrai.py` non le vede.
Chiuderlo non e' allargare una regex: articolo e plurale sono per `ITEM_ID` e
appartengono al nome **identificato**. Vedi `decisioni.md`.

## Gli inquilini, Aime e Jaldabaoth — e una toppa che nessuna rete vedeva — 2026-08-21, ottantunesima sessione

Due lotti, **97 rese**, e `chat.hsp` scende da 2.541 a **2.444**.
`menu_dialogo` misura **881** voci (erano 841), `bilingui` resta a **0** —
zero al primo giro in tutt'e due i lotti — `chat-lotto-misura` 0 fuori misura e
0 peggiorate, `pytest` 730.

Il primo lotto (**54 rese**) è la casa: **Telhureza** il geco di guardia,
**Imarituka** lo sberleffo, **Oxode** l'ape stregina, **Scard** la rondine
felice, **Talka** al tempio (devozione, offerte, incarnazioni, il libro nero),
**Kyu-bi** col tofu fritto e la **Signora Cicogna**. Il secondo (**43 rese**) è
**Aime** la narratrice coi suoi tredici racconti e **Jaldabaoth** il Figlio del
Caos — la lancia divina, la luce dei desideri, la sconfitta.

⚠️⚠️⚠️ **Il perimetro della zona era sbagliato, e non per colpa dello
strumento**: `:15509` è un'etichetta HSP e taglia in due il blocco di
Telhureza. Le 47 firme che `perimetro-zona.py` dava avrebbero prodotto un
sottodialogo italiano sotto un menu inglese. Il lotto si è preso sul
**parlante** — `:15491`-`:15764` — e sono 54. *Un'etichetta è un indirizzo di
salto, non un confine di senso.*

⭐⭐⭐ **La toppa 1018 sistema un difetto che nessuna rete poteva vedere**: in
italiano ogni desiderio di una creatura dava la statuetta di **`@`**. Le quattro
parole d'innesco stanno in `lang()` e sono tradotte; le righe di `fix_wish`
(`module.hsp`) che le tolgono dalla stringa **non** stanno in `lang()` e sono
rimaste inglesi, quindi il nome non combaciava mai. Provata sul banco HSP.
È una **classe di difetto nuova**: la `lang()` tradotta il cui *partner* sta
fuori da `lang()`.

⭐⭐⭐ **E il collaudo è tornato**, per la prima volta dalla 70ª: sette schermate
guardate una per una, tutte a posto. La strada nuova è **F12 → `wizard` →
`spawn_chara <ID>`**, e non dipende più da dove è arrivato il salvataggio.

Una resa vecchia corretta: `db_creature.hsp:43882` faceva dire a Oxode «Ah,
**padrone di casa**, sei di ritorno.» al giocatore, accordandosi con un genere
che non si conosce.

## La zona di Leold chiusa intera — 2026-08-21, ottantesima sessione

Due lotti, **124 rese**, e la zona `chat.hsp:16641`-`:18601` passa a **247 firme
su 247**. Perimetro misurato prima di cominciare con `perimetro-zona.py`: 124
firme da fare, e `bilingui` ha dato **zero al primo giro** in tutt'e due i lotti
— terza e quarta zona chiusa di fila dopo gli evochat e `*chat_event`.

`chat.hsp` scende da 2.665 a **2.541**. `menu_dialogo` misura **841** voci (erano
797), `bilingui` resta a **0**, `chat-lotto-misura` 0 fuori misura e 0
peggiorate, `pytest` 730.

Il primo lotto (**90 rese**) è il sistema di **Leold**: gli slot
d'equipaggiamento pagati in Vita, il cambio di modalità di bilanciamento, i tre
rifiuti, i risvegli del giocatore e i tredici poteri del compagno. Il secondo
(**34 rese**) è quel che restava: il selettore delle pose, la madre malata, e le
tre scene di trama — Enthumesis, Lankata, Jaldabaoth.

⭐⭐⭐ **Il lessico non è stato deciso: è stato ripreso dal DATO.** Ogni voce di
questi menu vende un `CHARA_BIT_AWAKE_*` o uno `SKILL_SPACT_*`, e un `grep` sul
nome della **variabile** porta in venti righe al pannello dei talenti di
`command.hsp:2355`-`:2452`, dove ognuno di quei bit ha già la sua frase
italiana. Su 90 rese, i venti nomi propri del sistema erano tutti già scritti
altrove, e nessuna rete avrebbe protestato se li avessimo scelti diversi.

⚠️⚠️ **Due difetti di monte, tutt'e due trovati leggendo il codice.** (1) Il
**prezzo** di `:17864`: l'inglese etichetta «Variable Breath (300AP)», il
giapponese dice 消費AP400 e `:17925` fa `leoap = 400` — verificati tutti e
ventisei i prezzi dei due menu, è l'unico che diverge. (2) I **nomi delle parti
del corpo** di `:16741` e `:16743`: l'inglese offre «Chest» e «Finger» ma gli
slot sono `EQUIP_SLOT_BODY` e `EQUIP_SLOT_RING`, che `bodyn()` chiama «Body» e
«Ring». Il secondo apre una **decisione ancora da prendere** (vedi
`decisioni.md`, 80ª, punto 4).

⭐ **Misurato il pannello delle modalità**, che è il pezzo di `chat.hsp` del
punto cieco della 74ª (le sette righe `listn(...) = lang(...)`): colonna dei
nomi **14 caratteri**, colonna delle descrizioni **73** — e la riga inglese più
lunga ne fa 73 esatti, la firma della 63ª. Le trentasette descrizioni erano già
tradotte da una sessione vecchia e mai misurate: la più lunga ne usa **72**.

💡 **E chiudendo la zona se n'è chiusa un'altra**: `*label_6452` era «239 firme,
1 sparsa», e quella sparsa era la battuta di Jaldabaoth duplicata a `:15967`.
Adesso è **238 e zona chiusa** — l'unico blocco grosso che resta con quella
proprietà.

## `*chat_event` chiuso intero — 2026-08-21, settantanovesima sessione

Secondo lotto della giornata, **103 rese**: il blocco degli eventi
(`chat.hsp:302`-`:944`), cioè chi bussa alla porta, chi passa a trovarti, chi ti
assalta per strada e le feste. Perimetro misurato prima di cominciare: 103
firme, 109 occorrenze, **zero** con occorrenze fuori dalla zona — la seconda
zona chiusa di fila.

`chat.hsp` scende da 2.768 a **2.665**. `menu_dialogo` misura **797** voci (erano
766), `bilingui` resta a **0**, `chat-lotto-misura` 0 fuori misura e 0
peggiorate.

Le famiglie: capodanno, il rancoroso con la molotov, il bambino, il compagno che
allena, la visita col regalo, il brindisi, il maestro di gilda e l'allenatore,
il mendicante, Halloween, la guardia, i **cinque aspiranti inquilini**, il
caposquadra del Dock.

### ⭐⭐ I cinque inquilini: il registro stava in `db_creature.hsp`

Cinque creature bussano alla porta di casa e chiedono di restare, e ognuna ha
una voce sua. Nessuna di quelle voci andava inventata: `db_creature.hsp` è
chiuso dalla 31ª, e `scratchpad/repertorio.py` esiste apposta per ritrovarla.

| chi | nome reso | le parole che aveva già |
|---|---|---|
| `SCARD_THE_HAPPY_SWALLOW` | «<Scard> la rondine felice» | «Felice! FELICE!», «Che daffare! Che FELICITÀ!» |
| `OXODE_THE_QUEEN_BEE` | «<Oxode> l'ape stregina» | «Ara ara, tesoro~», «dolce miele», «padrone di casa» |
| `IMARITUKA_THE_ZASIKI_WARAI` | «<Imarituka> lo sberleffo di casa» | «lmao», «a scrocco», «Che imbarazzo!» |
| `TELHUREZA_THE_HOUSE_GUARD` | «<Telhureza> il geco di guardia» | «Fuehehe~», «gli insetti cattivi», «la casa che proteggo» |
| `MOMALARIA_THE_BLOODSUCKER` | «<Momalaria> la gravida succhiasangue» | il giapponese le spezza le parole in katakana |

💡 E le figlie di Oxode, le **api magiche** che entrano in casa con lei, dicono
già «mamma» e «Paaapa!»: la resa della madre si legge accanto alla loro.

### ⚠️⚠️ A Halloween l'inglese ha scambiato le due voci

`chatList 2` è 「イタズラされる」 — *farsi* fare lo scherzetto — e infatti porta alla
pioggia di molotov di `:699`; `chatList 1` è 「イタズラする」, ed è il giocatore che
fa lo scherzetto (karma −2, «Guardie! Guardie!»). Monte le ha etichettate
«Trick.» e «Treat.», che vogliono dire il contrario. Si segue il **codice**, non
l'etichetta: «Farsi fare lo scherzetto» e «Fare lo scherzetto», sotto «Dolcetto
o scherzetto?».

### ⚠️ E appiattisce cinque risposte in una

«Welcome!» sta su cinque righe diverse e «Get out!» pure, ma il giapponese ne ha
cinque forme distinte, tarate sul personaggio: 「いいよ」, 「いいね」, 「そんなぁ」,
「これからよろしく」, 「【ちょっとだけよ】」. Stessa cosa per «Okay, no turning back
now!» a `:754`, che a `:740` era già reso — la firma è diversa perché il
giapponese è diverso. Si segue il giapponese, come nel lotto degli evochat.

### ⚠️ Dieci rese respinte dalla misura, e il motivo è sempre lo stesso

`chat-lotto-misura` ne ha bocciate **dieci** al primo giro, tutte per «una riga
in più dell'inglese» — e tutte e dieci erano righe dove il **giapponese è molto
più lungo dell'inglese**, perché monte aveva riassunto. Seguire il giapponese
costa righe, e la finestra del dialogo non le ha. Accorciate tutte: nessuna
perde il pezzo che conta.

## Gli EVOCHAT, il sistema intero — 2026-08-21, settantanovesima sessione

Un lotto solo, **109 rese**, piu' una correzione, due invariati e una guardia
aggiornata. Nessuna toppa, nessuna rete nuova.

| pezzo | righe | contenuto |
|---|---|---|
| le reazioni del compagno | 18866-19235 | i cinque stati (`hyouzyou`) dei quattro modi di evochat |
| i cinque menu | 19242-19319 | scasso del cuore, evochat, evochat oscuro, gesti, scena |
| i venticinque `chatval` | 21362-21979 | le dieci vie, i due esiti dello scasso, il potere di scasso |

`chat.hsp` scende da 2.877 a **2.768**. `menu_dialogo` misura **766** voci
(erano 731), `bilingui` resta a **0** — e qui ha dato zero al primo giro per
una ragione misurata prima di cominciare: delle 109 firme, **zero** hanno
un'occorrenza fuori dalla zona.

### ⭐⭐⭐ E' il difetto della 78a girato: risposta italiana sotto un menu inglese

I tre ingressi — «<evochat>», «<evochat in coppia>», «<evochat oscuro>» — erano
**gia' italiani dalla 73a**, e sotto c'era un sottosistema interamente inglese.
Nessuna delle quindici reti lo vedeva: `bilingui` guarda i gruppi di
`chatList`, e **un menu tutto inglese non e' bilingue**. Si trova solo
chiedendo *dove porta* una voce gia' resa, che e' l'unica domanda che nessuna
rete pone.

### ⭐⭐⭐ Il lessico non si e' deciso: si e' ripreso, e stava in `text.hsp`

Le dieci «route» non sono dieci parole nuove: ogni `chatval` scrive
`CDATA_HEART_LOCK_RELATION` e quel valore **sceglie una delle dieci scale di
rapporto** di `text.hsp:33`-`43` (`_impressiona1`-`7`, `_impressionb1`-`3`),
tradotte da tempo e stampate sotto il ritratto (`chat.hsp:25620`) e nel
messaggio di `chara_func.hsp:1080`, «Il rapporto con X diventa <Y>...».

| voce | scala | la parola |
|---|---|---|
| Comrade | `_impressiona1` | **Compagno** |
| Friend | `_impressiona2` | **Amico** |
| Rival | `_impressiona3` | **Rivale** |
| Affection | `_impressiona4` | **Innamoramento** |
| Student | `_impressiona5` | **Tutela** |
| Master | `_impressiona6` | **Insegnamento** |
| Family | `_impressiona7` | **Famiglia** |
| Contract | `_impressionb1` | **Contratto** |
| Owner | `_impressionb2` | **Appartenenza** |
| Loyalty | `_impressionb3` | **Lealta'** |

Stessa cosa per i due esiti dello scasso: `command.hsp:2502` e `:2507`
chiamano i due tratti «Nessun **cruccio**» e «**Passatempo pericoloso**», e le
due righe di `:21732` e `:21750` dicono adesso quelle parole.

### ⚠️⚠️ `name(cc)` in `*chat_default` e' il GIOCATORE, e monte lo usa per il compagno

`cc = CHARA_PLAYER` (lo conferma `:22124`, dove `name(cc)` decapita il
prigioniero). Tre righe che parlano del **compagno** lo nominano lo stesso:
`:21732`, `:21750` e `:21867`. Il giapponese dice `name(tc)` tutt'e tre le
volte e il codice gli da' ragione (`cbitmod ..., tc`; `cdata(CDATA_GOLD, tc)`).
Le prime due sono rese di oggi; la terza era una resa vecchia che diceva «Tu hai
diviso le monete con il compagno» — **corretta**. 💡 Nessuna delle quindici reti
guarda *quale* personaggio nomina una resa.

### ⚠️⚠️ L'inglese di monte ha perso dodici battute, e le ha sostituite con due segnaposto

Otto righe portano lo stesso inglese («name is staring at you with a happy
expression») e due un altro («name seems to be a little pounding»); il
giapponese ne ha otto diverse. Deroga dichiarata, come `:1744` e `:1866` nella
78a: si segue il giapponese. Il nome resta in testa perche' `verifica` pretende
le funzioni di contenuto dell'inglese — e perche' attribuisce la battuta.

### ⚠️⚠️ Un segnaposto troppo largo produce un difetto di monte che non esiste

`chat.hsp:19256` e' entrata fra le «rotte anche in inglese», ottava della lista,
e **non lo e'**: `reso()` suppone quattro cifre per ogni valore interpolato, ma
`ulp3` e' `limit(..., 0, 80)`, quindi il massimo vero della voce inglese fa
**58 esatti**, cioe' il tetto. E' la lezione della 72a girata — li' era un
tetto troppo stretto — con una differenza: le quattro cifre servono davvero
altrove, e la correzione vera e' leggere il `limit(..., 0, N)`. Non e' stata
fatta: la riga sta nella guardia **col motivo scritto**.

## `*chat_default` chiuso, le gilde e il tutorial — 2026-08-21, settantottesima sessione

Tre lotti grossi invece di nove piccoli, e ognuno chiude una cosa intera.
**270 rese**, nessuna toppa, nessuna rete nuova.

| lotto | rese | esito |
|---|---|---|
| `*chat_default` | 81 | **CHIUSO** salvo la famiglia evochat, dichiarata fuori |
| il sistema delle gilde | 97 | tre maestri, tre guardiani, tre investigatori |
| l'inizio della storia e il tutorial | 92 | Larnneire, Rianna, Lomias, il tutorial intero |

`chat.hsp` scende da 3.147 a **2.877**. `menu_dialogo` misura **731** voci
(erano 675), `bilingui` resta a **0** — e in tutt'e tre i lotti ha dato zero al
**primo** giro, che non era mai successo.

### ⚠️⚠️⚠️ Il conteggio `--da-tradurre` mente sul perimetro di un blocco

`estrai --da-tradurre` ancora una voce per **firma** alla **prima**
occorrenza. Chi legge quell'elenco per sapere «che cosa manca in questo
blocco» prende un numero sbagliato per difetto, e non se ne accorge: in
`*chat_default` le firme erano **89**, non le 77 che l'elenco mostrava. Le
dodici mancanti avevano la prima occorrenza altrove.

E due delle dodici erano **voci di menu**: «Sorry.» vive anche nel menu della
gatta Sinaha (`:10880`), «Hold on.» in quello della barca di Regulus
(`:13590`). Tradurre le 77 dell'elenco avrebbe lasciato **due menu a meta'** in
posti che nessuno stava guardando.

💡 La regola: *per sapere che cosa manca in una zona si guardano tutte le
occorrenze di tutte le firme, non l'elenco del lavoro che resta.* Il conto
giusto e' «firme non tradotte con **almeno un'occorrenza** nella zona».

⭐ Nel lotto del tutorial la stessa cosa e' successa in grande: 「わかった」 vive
in **sette** menu lontani (`:9575`, `:9588`, `:10671`, `:11830`, `:15186` per
«Alright.», `:2210` e `:2215` per «Will do.»), ognuno con la sorella ancora
inglese. Otto sorelle aggiunte al lotto, e `bilingui` a zero al primo giro.

### ⭐⭐ In `*chat_unique` si prende un SISTEMA, non un parlante

`*chat_unique` e' uno smistamento `_switch_val == CREATURE_ID_x`, quindi la
tentazione e' il lotto per personaggio. Ma le tre gilde sono **sei blocchi
quasi identici fra loro** piu' tre investigatori a Tyris del Sud: prese
insieme, il glossario si decide una volta e le sei schermate parallele dicono
le stesse parole.

⭐ **E il glossario non si e' deciso: si e' ripreso.** Gilda dei Maghi /
Guerrieri / Ladri e «il maestro della gilda» stavano gia' in `command.hsp` e
`text.hsp`; «il guardiano» e «l'investigatrice» nelle domande del quiz; «punti
gilda», «obiettivo» (per la ノルマ), «grimorio», «refurtiva», «Nefia casuali di
tipo X di livello Y o piu'» nelle voci di diario che annotano le stesse prove.
Le tre prove d'ingresso adesso dicono **le parole del diario che le annota**.

Lo stesso nel tutorial: `<Mangia>`, `<Leggi>`, `<Scava>`, `<Equipaggia>`,
`Tiro` e i tasti `g` e `d` si copiano da `text.hsp`, che il progetto ha gia'
tradotto. Un tutorial che nomina i menu con parole sue sarebbe peggio che
inglese.

### ⚠️⚠️ Il perimetro si taglia dove il menu di monte e' ancora inglese

Le tredici rese della famiglia **evochat** — le dieci «route», i due esiti del
cuore, il potere di scasso — sono rimaste fuori da `*chat_default` apposta: il
menu che le accende (`:19250`-`:19278`) e' ancora tutto inglese, e tradurne il
solo esito produce la meta' **peggiore**, menu inglese e risposta italiana.

💡 *La direzione conta.* Menu italiano e risposta inglese e' il difetto che la
73a ha corretto in massa; il rovescio — risposta italiana sotto un menu inglese
— e' lo stesso difetto girato, e nessuna rete lo misura perche' `bilingui`
guarda i gruppi di `chatList`, non i percorsi.

### ⭐ Un referto che nessuno leggeva aveva ragione

`scratchpad/referti.py` segnalava da sessioni tre participi. Due sono falsi
positivi legittimi («te lo sei preso» concorda con l'extraterrestre, «te la sei
cavata» e' l'idioma), il terzo no: `chat.hsp:18483` diceva **«non sei
riuscito»** al giocatore. Corretto; il referto scende da 3 a 2.

## `*chat_default` svuotato a meta', e la firma condivisa come regola — 2026-08-21, settantasettesima sessione

Nove lotti dentro `*chat_default` e nei blocchi che le firme si sono tirati
dietro. **152 rese e una toppa**, senza reti nuove: le quindici c'erano gia' e
hanno lavorato tutte.

| pezzo | rese | esito |
|---|---|---|
| le due arene | 17 | duello, rissa, animali, squadre, EX, punteggio |
| l'informatore | 12 | la lista, il messaggio, la sequenza del compleanno |
| il dojo di Nazuna | 37 | il blocco `:8812`-`:9186` chiuso intero, piu' cinque menu lontani |
| l'ingaggio e il reclutamento | 11 | `chatval` 50 e 51 |
| il mercante di schiavi | 9 | vendere, comprare, la madre di Pael |
| quel che i PNG rispondono | 21 | confessione, sfratto, portafogli, spostati |
| il nome della casa | 12 + toppa | l'ordine girato, provato sul banco HSP |
| il dio e l'indulgenza | 14 | il numero nuovo, l'offerta, il prete |
| i servizi che si pagano | 19 | identificare, curare, il rifugio, il veicolo |

`chat.hsp` scende da 3.299 a **3.147**. `menu_dialogo` misura **675** voci (erano
629), `bilingui` resta a **0** e `maiuscole` passa da 9 appesi a **7**.

### ⚠️⚠️⚠️ La firma condivisa non e' un caso limite: e' la forma normale del file

Tre volte su nove lotti una resa ha acceso menu che non stavo guardando, e ogni
volta l'ha detto `bilingui` **dopo** la reimportazione, mai una lettura del
codice — perche' finche' un menu e' tutto inglese non c'e' niente da vedere.

| firma | rappresentante | menu accesi |
|---|---|---|
| 「やめる」/«No way!» | `:9051` | il blocco 47 dell'informatore |
| 「断る」/«I refuse.» | `:2351` | Erystia, le monete di bronzo, la droga in capsula, la tartaruga |
| 「いいよ」/«Sure.» | `:8197` | la lettera di Siraha, la tartaruga della principessa |

💡 E chiuderne uno ne apre un altro: la resa delle **monete di bronzo**, scritta
per chiudere il menu di `:2996`, ha acceso il menu del potioman a `:3029`. Tre
giri di rete per arrivare a zero. *La rete va rilanciata dopo ogni giro, non una
volta sola.*

⭐ **E l'altra faccia paga**: `:20576` e' la firma di **tutti** i «Thanks!» del
file (`_thanks(2)`), quindi una resa sola ne ha resi una decina.

### ⭐⭐⭐ Il nome della casa: la soluzione non era una resa, era l'ordine

`chat.hsp:22500` **appende** all'epiteto uno degli undici suffissi di `:22498`
(«Silver Spectre Hovel»). In italiano l'epiteto e' gia' un sintagma intero —
«fragore della dipendenza» (64a) — e il suffisso in coda non e' italiano. Il
giapponese ha la struttura **nostra**, 「<epiteto>の家」 = «casa DI <epiteto>»:
la toppa 1017 gira la concatenazione nel solo ramo inglese e i suffissi
diventano prefissi che finiscono in «di».

⚠️ «di» e' la sola preposizione che regge: qualunque articolo si accorderebbe
col primo nome dell'epiteto, che cambia a ogni tiro. ✅ Provato sul **banco HSP**
fuori dal gioco: «Castello di Quiete del figlio», «Tana di Dea dell'uccello»,
dodici tiri, nessuno storto.

### ⚠️⚠️ E un test ha corretto una cosa che avevo scritto in un commit

`strumenti/maiuscole.py` legge la **build**, non il sorgente pinnato. Le due
rese di `:22375` e `:24739` mettono il nome in testa, quindi quei due siti sono
usciti dagli «appesi» da soli e i loro permessi in `GIUDICATI` restavano
attaccati al vuoto: l'ha detto `test_i_giudicati_esistono_ancora`, che esiste
apposta.

## I menu bilingui, e la rete che li conta — 2026-08-21, settantaseiesima sessione

Nata da un difetto trovato traducendo: il dizionario è per **firma**, quindi una
voce di menu resa in un punto del file ne rende un'altra in una schermata
lontana, che resta metà italiana. **121 rese, una rete nuova, 11 test.**

| pezzo | rese | esito |
|---|---|---|
| `chat.hsp`, l'oste | 18 | i cinque `chatval` della taverna e il kiseru |
| `chat.hsp`, il figlio | 11 | il menu dell'istruzione, sette voci |
| `chat.hsp`, il lupo mannaro | 13 | i sette toni dell'accusa e l'indagine |
| `chat.hsp`, le indicazioni | 21 | le direzioni, la guida, e la scena di Jure per forza |
| `chat.hsp`, i menu bilingui | 58 | quindici schermate chiuse, in tre lotti |
| `strumenti/bilingui.py` | — | rete nuova, quindicesima verifica, 6 test |
| `strumenti/menu_dialogo.py` | — | due difetti nella misura delle dinamiche, 5 test |

`chat.hsp` scende da 3.420 a **3.299**. `menu_dialogo` misura **629** voci (erano
572) e `bilingui` ne trova **0** a metà, su tutti i file con dizionario.

⚠️ `rinviate.jsonl` sale a **75**: le due righe **commentate** di `chat.hsp:19327`
e `:19334`, che erano state tradotte e per questo erano entrate nelle misure.

## Le gemelle, e i quattordici menu di `chat.hsp` — 2026-08-20, settantatreesima sessione

Nata dalla misura della 72ª: 417 rese che esistevano già in un altro file di
dizionario e che nessun referto nominava. **296 rese, una rete nuova, 22 test.**

| pezzo | rese | esito |
|---|---|---|
| `strumenti/gemelle.py` | — | rete nuova, tre classi, 22 test |
| `chat.hsp` fuori dai menu | 120 | la finestra delle modalità, i materiali del compagno |
| `chat.hsp`, i quattordici menu | 152 | 76 gemelle + 78 sorelle + 2 correzioni di misura |
| `event.hsp` fuori dal generatore | 24 | e il menu `4504-4509` chiuso intero |
| `event.hsp:1070` | 1 | la sorella mancante di un menu da due voci |
| il generatore di `event.hsp` | 193 | 158 pezzi e 35 cornici, con la grammatica nuova |
| intorno al generatore | 16 | dal collaudo: titoli, bottoni, registro, la paga |

`chat.hsp` scende da 3.920 a **3.648** e `event.hsp` da 622 a **394**: nessuno
dei due ha più gemelle. **505 rese in tutto, in dieci spinte.**

### ⭐⭐⭐ La schermata di collaudo che ha trovato una cornice mancante

La frase del generatore era arrivata e stava in piedi; **intorno** c'erano il
titolo inglese di ogni evento, l'unico bottone della finestra, le due righe di
registro che escono sempre — e una riga **mezza italiana** fatta da noi la
mattina stessa: «As a salary, 215 monete d'oro e 2 oggetti have been sent to
your house.» I pezzi erano fra le 24 gemelle importate, la cornice di
`event.hsp:4467` no. 💡 *Una resa può essere giusta e fare danno perché la
cornice che la incornicia non è arrivata.*

### Le tre classi, misurate su tutto il progetto

    gemelle      392 -> 59     la firma combacia: valida per costruzione
    divergenti    13 ->  2     già resa in due modi: sceglie chi legge
    quasi        201 -> 162    solo il giapponese: da leggere, mai da travasare

Delle 59 che restano, **21 sono `custom_autopick.hsp`**, che è delicato: il
resto è pulviscolo su quindici file. La famiglia è, in pratica, chiusa.

### ⭐⭐ Il generatore degli eventi di viaggio

Le 116 gemelle ferme in `event.hsp` erano i **pezzi di un generatore**: `hito`,
`mon`, `tori`, `item`, `drink`, `tree` più i due modificatori `donna` e
`nagara`, montati a caso in 35 cornici (`3523-3629`). La grammatica — articolo
dentro il pezzo, `donna` invariabile e postposto, cornici senza participi che si
accordino — sta in `decisioni.md`.

⭐ **Provata componendo tutte e 35 le cornici due volte**, una con i pezzi tutti
femminili e una con tutti maschili, e **leggendole**: tre riscritte, e nessuna
delle tre per un accordo (una reggenza, una ripetizione, un'ambiguità).

⭐ **La geometria misurata, non stimata**: `talk_conv` va a capo a 34 caratteri
in mare (`bg_re25`) e 48 in viaggio (`bg_re13`), e la finestra **cresce di 15 px
a riga**. Caso peggiore: una riga più dell'inglese, cinque in tutto.

### ⭐⭐⭐ 82 gemelle su 194 stavano dentro un menu, e nessun menu si chiudeva

È il pezzo che vale più della rete, e non era nel piano. Il menu dello stile di
combattimento (`8991-9004`) aveva **tre** gemelle su quattordici voci:
importarle sole avrebbe portato la schermata da inglese e coerente a metà
italiano e incoerente. I quattordici menu sono stati chiusi **interi**, con 78
sorelle scritte a mano:

    2630-2745   i materiali del fabbro            40 voci
    20318-20351 che cosa pensi del compagno       30 voci   (due colonne)
    8991-9004   lo stile a mani nude              14 voci
    20296-20307 le regole del compagno            12 voci   (due colonne)
    11253-11263 l'elemento da imparare            11 voci
    16737-16746 la parte del corpo da far crescere 10 voci
    13650-13658 quale dio                          9 voci
    7012-7021   il sindaco                         7 voci
    17702-17716 le azioni AP del compagno          6 voci
    9195-9209   i biglietti del casinò             4 voci
    13772-13775 il mercante di scorte              4 voci
    + 1376, 7370, 10997, 22111                     4 menu da due voci

⚠️ **Sei gemelle scartate**: `claw`, `spore` e `branch` perché in `text.hsp`
sono il **verbo** del colpo e qui serve il nome dello stile; tre perché
`text.hsp:1523-1556` è lo stesso elenco visto da un pannello con la colonna più
larga, e qui il tetto delle due colonne è 24.

`menu_dialogo`: 0 fuori misura su **417** misurate (erano 257) e 0 peggiorate a
due colonne — e la rete ha preso due righe nostre troppo lunghe prima che
arrivassero a schermo.

### Altre decisioni prese leggendo il sito, non la stringa

- 腰 nella lista delle parti del corpo diventa **«Fianchi»**, non «Vita»: la voce
  dice già «(Vita -3)», e due «Vita» nella stessa riga sono illeggibili.
- le azioni AP prendono il nome che `skill.hsp` ha già («Sincronia delle anime»,
  «Guardia metallica»): un'azione non può chiamarsi in due modi fra il menu che
  la compra e la barra che la usa.
- `準備中` è **«In preparazione»**, non «Cancel»: nessun ramo raccoglie quella
  scelta, e l'inglese di monte lo nasconde.

---

## Due file chiusi e il menu del dialogo — 2026-08-20, settantaduesima sessione

Nata da un collaudo di quattro schermate. 289 rese, due file chiusi, tre reti
toccate (due nuove), otto toppe.

| pezzo | rese | esito |
|---|---|---|
| i quattro inglesi del collaudo | 4 | `displace`, i due `gp`, «Premi un tasto per chiudere» |
| il menu del dialogo di `chat.hsp` | 125 | 100 voci di `*talk_main` più 19 del pannello |
| le dieci tagliate a due colonne | 10 | correzioni, **nove di sessioni precedenti** |
| `help.hsp` | 46 | ⭐ **CHIUSO**, 0 / 0 |
| `screen.hsp` | 98 | ⭐ **CHIUSO**, 0 / 0 (20 di combattimento + 78 cori) |

`chat.hsp` scende da 4.046 a **3.920**. I file con `lang()` e senza dizionario
passano da dodici a **dieci**.

### ⭐ Il menu del dialogo: 125 voci, raggruppate per SCHERMATA e non per file

Il perimetro non si sceglie per riga ma per **quello che si apre insieme**: le
100 voci di `*talk_main` (`chat.hsp:19340`-`19876`) e le 19 del pannello che
sta a sinistra (`:25480`-`:25610`) sono la stessa schermata, e il registro si
decide una volta sola.

⚠️ **E l'elenco per riga ne perdeva sei.** `estrai` raccoglie per **firma** e
riporta il **primo sito**: «Let's talk.» risultava a `chat.hsp:1326`, non a
`:19348`, e un filtro sul numero di riga non la vedeva. Il perimetro si prende
per firma, calcolando i siti.

### ⭐ `help.hsp` chiuso — 46 rese

Il più piccolo dei dodici file senza dizionario, e dentro ci sono due schermate
che si aprono il primo giorno: la ruota dei comandi e l'elenco dei tasti.

⚠️ Il tetto è **10 caratteri**, e non viene da un `sdim`: il testo è **centrato**
su piastrelle da 48 px (`help.hsp:105`, `x(cnt) + tx + 25 - strlen(s) * 3`) e
gli slot 0, 4 e 8 — i nomi delle quattro pagine — hanno passo 75 px.

Tre valori restano inglesi e sono in `invariati.md`, sezione nuova **«Chiavi e
nomi di file — non sono testo, sono indirizzi»**: `EN` è la chiave del blocco che
`:228` cerca dentro `manual_ENG.txt` con `instr`; `manual_ENG.txt` e
`scene2.hsp` sono argomenti di `noteload`. ⚠️ Il giorno che il manuale si
traduce, quella riga non diventa una resa ma una **toppa** con `manual_IT.txt` e
il ramo `exist` di ripiego — la disciplina di `board_it.txt` e `talk_it.txt`.

### ⭐ `screen.hsp` chiuso — il decimo punto cieco della 55ª

⚠️ **Non è l'HUD, come diceva l'elenco: sono due cose sotto un nome solo.**

    20 righe   combattimento e livello: « have gained a level.» era ancora
               inglese, ed è una delle righe più lette del gioco
    78 righe   i cori della battaglia finale, una voce per personaggio — gli
               otto dei, i compagni, i negozianti, la sorella, il cane poliziotto

La forma dei cori è `"<Nome> <verbo>, " + cnvtalk("<battuta>")`, e il
**giapponese non ha nessun verbo**: scrive 名前「battuta」 e basta. I verbi sono
un'aggiunta inglese ma sono caratterizzanti e si tengono, con i **due punti** al
posto della virgola — la punteggiatura italiana del discorso diretto, e lo stile
che il progetto usa già in `action.hsp:14051`.

I nomi restano quelli di monte, che il dizionario ha già da altri file. Si
traducono i quattro parlanti senza nome (la scienziata misteriosa, il cane
poliziotto, il guerriero leopardo, la sorella) e i due che un nome reso ce
l'hanno: «la principessa dell'abisso» (`db_creature.hsp:86765`) e il «vento
d'etere» (`chat.hsp:9500`).

### ⭐ Tre volte l'inglese aveva buttato via quel che il giapponese ha

    screen.hsp:6759   「はレベルNになった！」 dice a QUALE livello si sale
    screen.hsp:8076   シャキーン e ズバシュッ sono due onomatopee diverse — il lampo
    e :8099           della lama e il taglio — appiattite su un « *vorpal* »
    screen.hsp:1442   il giapponese saluta il giocatore per nome nella battuta
    help.hsp:866      il giapponese ha una seconda riga che l'inglese non ha

Tutte e quattro sono tornate. È lo stesso fenomeno dei 38 blocchi giapponesi che
`board.txt` ha perso e delle 13 righe di `ZAILE` in `talk.txt`: **l'inglese di
monte non è una copia del giapponese, è una riduzione.**

### Le otto toppe: 1009 → **1016**

    1010a-1012a   la gronda della scheda: wx+68 -> 79, wx+310 -> 325,
                  wx+410 -> 418. Curano ClasseGuerriero, Altezza157 cm,
                  Velocita70(70), AliasGiustizia del sole e Prossimo 3024
    1013a-1016a   i quattro cnven() appesi: chat.hsp:25573 («il cittadino
                  Femmina»), item_func.hsp (il suffisso di qualità di OGNI
                  oggetto identificato) e le due dell'elenco dei compagni

### Le reti

    menu_dialogo   +*talk_quest fra i gosub che NON disegnano: da 156 a 257
                   voci misurate, e dentro c'erano due difetti DI MONTE
                   +tagliate_a_due_colonne(): il secondo tetto, 24 caratteri
    gronde.py      NUOVA: lo spazio fra etichetta e valore. Legge la BUILD
    maiuscole.py   NUOVA: cnven() e la maiuscola in mezzo alla frase
    verifica.py    il metro delle interpolazioni è inglese PIÙ giapponese
    funzioni.py    cnvtalk è trasparente, non è una chiamata di contenuto

`pytest` da 653 a **684**.

---

## `item.hsp` chiuso — 2026-08-20, sessantanovesima sessione

**244 `lang()`, 242 rese, 2 rinviate.** Il file era il **quindicesimo punto
cieco**: aveva `lang()` e nessun file di dizionario, quindi non compariva in
`verifica --dizionario` e nessun conteggio lo guardava — la lezione della 54ª,
*un file senza file di dizionario non è un file finito, è un file che nessun
conteggio guarda*.

Otto lotti, in ordine di quel che il giocatore legge più spesso:

| lotto | righe | rese | che cos'è |
|---|---|---|---|
| `fase4-item-001` | `:3304`-`:3397` | 31 | che sapore ha quel che mangi |
| `fase4-item-002` | `:3471`-`:3888` | 22 | le erbe, la carne umana, i cibi speciali |
| `fase4-item-003` | `:3925`-`:4046` | 17 | il cioccolato, la mesugaki, la fortuna |
| `fase4-item-004` | `:4066`-`:4217` | 17 | i cibi che cambiano il corpo (6 invariati) |
| `fase4-item-005` | `:4258`-`:4324` | 7 | le abilità e la «Fase 2» (+ 2 toppe) |
| `fase4-item-006` | `:4335`-`:4648` | 36 | le carni e gli effetti |
| `fase4-item-007` | `:107`-`:127` | 42 | le cinque tabelle in testa al file |
| `fase4-item-008` | sparse | 32 | il parassita, la stima, la cronaca, la cucina |

Le due che il conto porterà per sempre sono `:4291` e `:4294`, terzo esemplare
della famiglia di `his2()` dopo `proc.hsp:11481` (36ª) e `proc.hsp:24107` (39ª):
risolte da toppa, come le altre due.

⚠️ **I file senza dizionario scendono da 13 a 12, e le `lang()` fuori da ogni
conteggio da 811 a 567.** Restano `txtadv.hsp` 170, `material_data.hsp` 118,
`custom_autopick.hsp` 90, `help.hsp` 52, `net.hsp` 37.

## `item_func.hsp` — gli stati del nome, 2026-08-20, sessantanovesima sessione

Non un lotto: **tre toppe e una resa**, nate da un collaudo che ha letto «un
piatto di **rotten** pasta fresca».

`item_func.hsp` è il compositore dei nomi degli oggetti: incolla una sessantina
di pezzi attorno al nome vero, quasi tutti **suffissi fra parentesi**
(`(Scary)`, `(Empty)`, `(Herb)`, `(Antiseptic)`, `(Poisoned)`…) e pochi
**prefissi**. I prefissi sono il problema: l'aggettivo italiano prima del nome
concorda col genere, e `rotten ` serve *ogni cibo del gioco*.

| pezzo | esito | perché |
|---|---|---|
| `rotten ` | **toppa** → ` (marcio)` in coda | nessun genere sicuro: serve ogni cibo |
| `sample ` | **toppa** → ` (campione)` in coda | idem |
| `[Growable] ` | **resa normale** → `[Coltivabile] ` | «coltivabile» è in **-e**, invariabile al singolare |

💡 La differenza fra i tre non è il posto in cui stanno: è **se l'italiano ha o
no una forma che non concorda**.

⚠️ **Lo stesso muro aspetta il prefisso del materiale** — `mtname(…) + lang("製の", " ")`
in tre siti, più le 118 righe di `material_data.hsp`: `mithril sword` in
italiano è «spada **di** mithril», postposta.

⭐⭐⭐ **`item_func.hsp` E' CHIUSO — 2026-08-25, novantaseiesima.** 203 rese in
quattro lotti, e il conto per intero: **274 siti = 226 resi + 37 rinviati**, zero
aperti. Le 37 non sono lavoro e hanno tutte una causa scritta — 9 spente nel ramo
`& jp`, 5 bloccate a monte, 4 il muro dei prefissi, 4 risolte da toppa, 1 in un
commento di blocco, 14 sigle a un kanji gia' rinviate.

⚠️ **E il muro del materiale qui sopra era gia' mezzo abbattuto.** Le due righe
`mtname(…) + lang("細工の", "work ")` dei mobili **nella build non esistono
piu'**: una toppa le trasforma in `locvar_itemname_s6 += " di manifattura in " +
mtname(…)`, cioe' il materiale in coda al nome. Restano da toppare le **quattro**
del prefisso vero (`:1308` la taglia in cm, `:1386` il kit di materiali, `:1390`
il cioccolatino, `:1458` «eternal force») e le 118 righe di
`material_data.hsp`.

## I 71 `bufftxt` di `buff.hsp` — 2026-08-13, trentunesima sessione

**65 firme distinte coprono i 71 siti**: i tre 「装備の力を引き出した」 e i
cinque cambi di forma condividono la firma.

Non erano un lotto di rese ma **lavoro strutturale**, e sono servite due toppe:
una riporta il ramo inglese di `chara_func.hsp:2316-2375` alla forma giapponese
(63 righe diventano una, e `bufftxt(1)` — letterale nudo fuori da `lang()` in
tutte e 71 le righe — smette di essere letto); l'altra allarga
`sdim bufftxt, 30, 2, MAX_BUFF` a 128, perché l'italiano porta la frase intera e
arriva a 59 byte dove il giapponese si fermava a 28. Il ragionamento sta in
`RIPRESA-sessione.md`, «Le due toppe di `buff.hsp`».

⚠️ **Dei 71, zero erano già resi altrove** — l'opposto dei `buffname`, dove 44
su 71 si copiavano da `skill.hsp`. La differenza è che un nome di status è
anche il nome di un incantesimo, mentre il messaggio che lo annuncia non
compare da nessun'altra parte.

## I 71 `buffname` di `buff.hsp` — 2026-08-13, ventinovesima sessione

Prima fetta del blocco di Fase 4 anticipato dalla decisione 0. **71 voci, tutte
`statica`, tutte dentro `lang()` e autonome**: nessuna dipendenza strutturale,
che era il motivo per cui erano state scelte.

⚠️ **La ripresa diceva «~90 `buffname`»: sono 71.** Le 199 voci del file si
dividono in **71 `buffname`**, **65 `bufftxt`** (quelle spezzate in due, lavoro
strutturale) e **63 `buffdesc`**, che nessun documento nominava. La variabile
non sta nel JSONL: si legge rileggendo la riga del sorgente.

💡 **Solo 27 delle 71 sono state decise qui.** Le altre **44 avevano gia' una
resa**, quasi tutte in `skill.hsp`: un buff e l'incantesimo che lo concede sono
la stessa cosa per chi gioca, e il giapponese e' identico. Copiate dal
dizionario, non ridecise — vedi `decisioni.md`, «Un buff e' l'incantesimo che lo
concede».

Le 27 nuove, per gruppo:

- **i dieci `Grow X`** prendono il nome d'attributo gia' chiuso in `skill.hsp`
  (`Crescita della forza`, `… della costituzione`, `… dell'apprendimento`);
- **le cinque `Form Shift`**, `Cambio di forma (A)`/`(B)`/`(G)`/`(D)` e
  `Cambio di forma finale`;
- **dodici sparse**, fra cui `Punizione divina`, `Fortuna`, `Sfortuna`,
  `Distrazione`, `Malinconia`, `Maledizione della fame`.

Le tre etichette di stato pure — `Distracted`, `Melancholy`, `Unlucky` — sono
rese **sostantivi** e non aggettivi, come impone la guida di stile: `Distrazione`
e non `Distratto`, che vorrebbe il genere di chi lo subisce.

Catena verde: `verifica` 0 problemi al primo colpo, **398 test**, prova
d'identita' **72/72 e 27.813**, larghezze 0/75, diario 0/214.

## `chara_func.hsp` entra per 45 firme — 2026-08-11, diciannovesima sessione

Quarto file fuori piano, ed entrato per la stessa ragione dei tre della
sessione prima: un valore che il perimetro produce e che qualcuno fuori
consuma. Qui però non è un confronto, è **una frase**.

`action.hsp` scrive la prima metà del messaggio d'attacco — «il putit morde il
viandante e» — e imposta `gdata(GDATA_DMG_TYPE) = 2`; `chara_func.hsp:6323`
legge quel flag e stampa la seconda metà, «infligge una lieve ferita.», con
`txtcontinue` che sopprime la maiuscola. Sono 45 firme su 331: **solo la zona
del danno**, non il file intero.

Il criterio del taglio è quello che vale la pena tenere: si allarga il
perimetro alla **zona che chiude la frase**, non al file che la contiene. Le
altre 286 firme di `chara_func.hsp` restano fuori finché non serviranno.

⚠️ La causa di morte (`chara_func.hsp:6850`) è rimasta fuori di proposito: la
frase la compone `main.hsp:4409`, che non è nel perimetro. Tradurla darebbe
«<epiteto> <nome> per mano di il putit in Vernis» — metà italiano, metà
inglese, e una preposizione che non si fonde.

## Il perimetro si allarga di tre file — 2026-08-10, diciottesima sessione

Sessione aperta per collaudare i nomi, chiusa con **464 firme in più** e un
difetto sistemico riparato.

**379 rinomine all'evoluzione, in tre file che non erano nel perimetro.** Il
dettaglio sta in `decisioni.md`. Qui conta il precedente di metodo: un file
entra nel dizionario **anche se non è nel piano**, quando il piano lo esclude
per una ragione che nel frattempo è caduta. `custom_enemyevolution.hsp` non era
in Fase 1 perché non contiene interfaccia né messaggi — contiene solo copie di
nomi di creatura. Ed era proprio quello il problema: erano copie **da tenere
allineate**, e nessuno le teneva.

Le 379 sono state risolte automaticamente cercando il **giapponese** nel
dizionario esistente: zero ambigue, zero mancanti su 379. Vale la pena tenerlo
come tecnica: quando un file duplica valori di un altro file già tradotto, la
traduzione non si scrive, si **risolve**, e la chiave è il campo che i due
condividono per costruzione — qui il giapponese, non l'inglese.

**320 stringhe di voce** (`db_creature.hsp`, classe `voce`): chiuse tutte.

**59 rinviate del quiz**: chiuse. `rinviate.jsonl` scende da 79 a **20**, e le
20 che restano aspettano tutte `proc.hsp`.

**26 dinamiche di `action.hsp`** su 318. Poche perché la strada era bloccata da
una guardia che rendeva certe voci intraducibili; sbloccarla ha richiesto di
correggere `strumenti/funzioni.py` e due test. Il modello per le restanti 292 è
ora fissato:

- terza persona, mai `_s()`, `is()`, `was()`, `your()`, `have()`, `does()`:
  non passano da `lang()` e resterebbero inglesi;
- mai una preposizione davanti a `name()` o `itemname()`, che portano già
  l'articolo (`guida-stile.md:212`) — il controllo va rifatto a ogni lotto;
- `name(giocatore)` è «il viandante», quindi la terza persona regge per tutti.

### Il debito che questa sessione lascia

- **292 dinamiche + 597 statiche** in `action.hsp`.
- `chara_func.hsp` **non è nel perimetro** ma il quiz ne ha già fissato quattro
  nomi (`glossario.md`): finché non entra, il giocatore riceve le pietre di
  Lesimas in inglese e le ritrova in italiano nel quiz.
- Le rinomine riparate **non sono state viste in gioco**: la lettura del
  sorgente dice che ora combaciano, ma è una deduzione.

## Cinquantasei lotti, e i nomi finiti — 2026-08-10, diciassettesima sessione

I 455 nomi rimasti sono stati chiusi tutti, a lotti per razza, in dieci commit.
Il metodo era quello della sedicesima sessione e non è cambiato: `--razza` per
il taglio, la carta di `db_card.hsp` per i nomi opachi e per il sesso, il
blocco della creatura per ciò che il sistema dichiara, e le quattro verifiche a
ogni giro.

### Il test dell'articolo ha avuto ragione due volte

La prima sui quattro nomi del ciclo di Cthulhu (`クトゥグア`, `ツァトゥグァ`,
`ナイアーラトテップ`, `シュブ＝ニグラス`), scritti nudi come gli dèi. Ma gli
dèi stanno fra `<>` e questi no, e `name()` riconosce i nomi propri **dalla
prima lettera** (`init.hsp:1713-1716`): per il motore sono specie, e l'inglese
infatti scrive `the cthugha`. Vanno con l'articolo. Regola in `guida-stile.md`.

### `ドレイク` è un gradino sotto `ドラゴン`, e questo chiude il preteso refuso

La razza è **亜竜**, sub-drago, e le carte lo ripetono per tutti. L'italiano ha
la parola: **«draco»**, il nome del *Draco volans*. Da qui viene che
`action.hsp:17390` non era un errore di battitura: `Electric Drake` (電気竜) è
«il draco elettrico», e renderlo «drago» lo farebbe **collidere** con
エレキドラゴン, che quel nome ce l'ha già. La voce esce dalle cose in sospeso.

### Un nome già preso non si può riusare, ed è successo tre volte

| nome | prima scelta | perché no | resa |
|---|---|---|---|
| `メイド` | «la cameriera» | è già di `メイドさん` | «la domestica» |
| `沙羅曼蛇` | «la salamandra» | è già di `メガサラマンダー` | «la salamandra d'oriente» |
| `ローパー` | «la melma tentacolare» | è già di `スライムローパー` | «il tentacolare» |

⚠️ E una collisione la crea **l'inglese**, non noi: `<Orphe> the chaos child`
è il 混沌の**寵児**, ma `<The Chaos Child>` è già il 混沌の**超児** del lotto
`god`, «<Il Figlio del Caos>». Un carattere li separa in giapponese —
寵 «prediletto» contro 超 «oltre» — e si segue quello.

### Due giochi di parole che solo la carta rivela

- `先生きのこ` sembra «fungo insegnante»; la carta finisce con
  「この先生きのこれないだろう」, cioè 「この先 生きのこれる」 «sopravvivere»
  letto come 「この先生 きのこれる」. Il nome **è** la battuta →
  **«il professore champignon»**;
- `闘駐火草` si legge *tochukaso* ed è **冬虫夏草**, il cordiceps, scritto con
  ateji. Vale la regola degli omofoni: si traduce la base → **«il cordiceps»**.
- `邪拳王` la carta lo dichiara origine di じゃんけん, e in italiano il gioco ha
  il suo nome → **«il re della morra»**.

### Tre carte inglesi sono sbagliate nel sorgente

`マンドレザッパー` (`db_card.hsp:4131`) ha la prosa di `胡瓜の怪物`, `世界樹`
(`9643`) quella di `ヘブンズビートル`, e `ガイドの『ノルン』` (`7017`) quella
di `メルガスト`. Il **giapponese è sempre corretto** ed è da lì che si è
tradotto. Non toccate: sono upstream.

### Il registro dei nomi che l'inglese sbaglia si è allungato

| giapponese | inglese | cosa dice davvero |
|---|---|---|
| 機甲将軍 | `iron colonel` | è un **generale**, e la carta lo ripete |
| 生化学者 | `biologist` | **biochimico**, la carta dice 生化学専門 |
| 剣客 | `the cosmic sword` | uno **spadaccino**: perde la persona |
| ネザーマッドゴーレム | `mad mud golem` | è **mud**, 地獄の泥から作られた |
| マルチプルゴーレム | `ultimate golem` | è **multiplo**, 多数の素材を複合 |
| ファラオの呪い | `cursed coffin` | la **maledizione del faraone** |
| デビルコボルト | `dark kobold` | **diabolico** |
| 暗黒宇宙蟹 | `dark dome` | un granchio spaziale nato in un buco nero |
| 自走雷撃砲 | `electric tank` | un **semovente**, e a fulmini |

## Otto lotti, e un arbitro nuovo — 2026-08-10, sedicesima sessione

**122 nomi**, da 577 a 455: `karune` 18, `ghost` 17, `roran` 17, `worm` 15,
`dragon` 15, `cat` 14, `metal` 14, `largeanimal` 13. La macchina del taglio per
razza non è cambiata; è cambiato **dove si va a chiedere**.

### `db_card.hsp` descrive in prosa ogni creatura, e decide i nomi opachi

Ogni creatura ha una carta del gioco di carte con `cardrefskill`, due o tre
frasi che dicono **cos'è**. Dal blocco della creatura non si ricavano: il blocco
dà razza, classe, sesso, azioni. La carta dà l'intenzione.

```powershell
# la descrizione sta poche righe sopra il cardrefn che porta il nome
python -c "..."   # vedi strumenti/, oppure cerca cardrefn e risali a cardrefskill
```

Cosa ha sciolto, che altrimenti sarebbe rimasto opaco o sbagliato:

| nome | senza la carta | con la carta |
|---|---|---|
| `シュイド` | katakana senza significato, l'inglese dice `shadow` | «più `シェイド` fusi insieme, e per questo chiamato così» → un collettivo coniato sul nome base → **«l'ombrame»** |
| `アークレイス` | `アーク` = arch, e poi? | «gli individui più forti si distinguono come rango sovrano e prendono il prefisso `アーク`» — la **regola**, non il caso → «l'arcispettro» |
| `ヴォルガーファントム` | l'inglese si arrende a `vol phantom` | fulmini, energia accumulata, scoppio → `ヴォル` è **volt** → «il fantasma voltaico» |
| `黒お嬢様` | l'inglese dice `white young lady` | «i vestiti sono bianchi ma la sua sostanza è nera senza fine» → «la signorina dal cuore nero» |
| `『Ｈな妹』` | uguale a `えっちな妹`, e l'inglese le rende entrambe `H sister` | «**ヒットマン**な妹», con la motosega → «la sorella minore **sicaria**» |
| `シン・ゴリラ` | l'inglese legge `sin` | generatore nucleare in corpo, sigillato, distrugge per sfogare energia: è `シン・ゴジラ` → «lo Shin Gorilla» |
| `バレットワーム` | l'inglese dice `rock worm` | ingoia minerali, fabbrica pallottole e le sputa → «il verme proiettile» |

⚠️ **La carta non sostituisce il blocco: risponde a un'altra domanda.** Il
blocco dice cosa la creatura *è nel sistema* (razza, sesso, classe, azioni), la
carta cosa *rappresenta*. Su `病兄` servono tutti e due: `CDATA_SEX = 0` dal
blocco, e dalla carta il fatto che i maschi di Roran siano malati sul serio —
che è la ragione per cui **non** segue `病妹` → «la sorella yandere».

### La guardia dell'articolo ha fermato un nome, e aveva ragione

`シルバースカル陛下` era diventato «sua maestà il teschio d'argento», e
`test_ogni_nome_e_ogni_stringa_di_evoluzione_porta_il_proprio_articolo` l'ha
bocciato: non comincia con un articolo. Non è formalismo — la rinomina
all'evoluzione sostituisce la stringa intera e `name()` non antepone più nulla,
quindi il nome sarebbe uscito nudo. Corretto in «la maestà del teschio
d'argento». **È lo stesso meccanismo che il collaudo di questa sessione ha visto
funzionare dal lato buono.**

### Un refuso nel già tradotto, lasciato lì apposta

`action.hsp:17390`, `電気竜` → «il **draco** elettrico»: unica occorrenza di
«draco» contro decine di «drago». Non è una distinzione voluta, è una lettera.
Non corretto perché sta fuori dai lotti e una voce chiusa che si ritocca va
vista in un commit suo.

## Dodici lotti per razza — 2026-08-10, quindicesima sessione

**351 nomi in un giorno**, da 928 a 577. Il nucleo atomico si era preso da sé;
tutto il resto si taglia per **razza**, che è un campo che il sorgente dichiara
— `dbidn`, subito prima di `gosub *db_race` — e non una proprietà che qualcuno
legge nel nome. È la terza volta che il criterio giusto è un campo del sorgente
invece di un giudizio: `reftype` per `db_item.hsp`, l'array che dichiara la voce
per `item_data.hsp`, `dbidn` qui.

```powershell
python -m strumenti.creature --razze              # quanto resta, razza per razza
python -m strumenti.creature --razza dog --uscita lavoro/fase2-dog-001.jsonl
```

⚠️ `--classe nome` da solo emette tutti i 1.131, nucleo compreso: `--razza`
toglie da sé le firme già in dizionario, o ogni lotto sovrascriverebbe il
precedente. La rete del criterio è `firme_senza_razza()`, oggi vuota: se un
domani non lo fosse, «un lotto è una razza» coprirebbe novecento nomi meno uno
**senza dirlo**.

| lotto | nomi | cosa ha insegnato |
|---|---|---|
| `dog` | 27 | i dieci segugi elementali li dichiara `FILTER_RACE_HOUND_<X>` |
| `norland` | 90 | il sesso è dichiarato solo su 52 su 90 → il criterio dell'articolo |
| `god` | 36 | l'inglese tiene il nome proprio e lascia cadere l'epiteto |
| `juere` | 33 | `rogue` copre due giapponesi diversi |
| `zanan` | 25 | la razza sta in `dbidn`, non nel nome |
| `bird` | 24 | due uccelli sbagliati e uno abbandonato dall'inglese |
| `spirit` | 21 | la stessa prova non dà la stessa conclusione |
| `rat` | 21 | una famiglia di giochi di parole che l'inglese aveva spezzato |
| `elea` | 19 | i nomi della trama, già vincolati dal quiz |
| `seamonster` | 19 | una razza fatta di fusioni |
| `machine` | 18 | l'inglese incoerente dove il giapponese non lo è |
| `imp` | 18 | sei fusioni da rifare, non da leggere |

### L'articolo di un nome di persona

Il problema che il nucleo non poneva e che vale per tutti i 577 che restano: un
nome di mestiere descrive una **persona**, e in italiano l'articolo di
«negoziante» dipende da chi lo porta. Il sorgente dichiara `cdata(CDATA_SEX,
rc)` **solo per una parte** — 52 su 90 in `norland`. Il criterio completo sta in
`guida-stile.md`; qui basta la conseguenza pratica, scoperta col lotto `imp`:

⚠️ **l'articolo sta sulla testa del sintagma, non sulla persona.** I cinque
demoni di `imp` hanno sessi diversi e la stessa forma italiana — «il demone di
X» — perché il genere lo dà «demone». `CDATA_SEX` conta solo quando la testa
**è** la persona (`<Neres> la smemorata`). I casi difficili sono meno di quanti
sembrassero.

### Due deroghe alla regola dell'articolo, e nessuna di più

`SENZA_ARTICOLO` in `test_creature.py` ha due voci, e un test pretende che
restino esattamente quelle: `＠`, che è il simbolo del giocatore fatto creatura
e parla «Qy@», e `user`, che non è un nome ma lo **slot** dei PNG definiti dal
giocatore. Il secondo lo firma il sorgente: `lang("user", "user")`, col
giapponese identico all'inglese in un file dove ogni nome vero ha la sua forma
giapponese.

### Un aggancio riparato all'indietro

`text.hsp` chiedeva «Come si chiama l'**investigatore** della Gilda dei Maghi?»,
ma la risposta è `<Lenas>` e `db_creature.hsp` le dà `SEX=1`. Il maschile era
un'ipotesi presa quando i nomi di creatura non c'erano ancora: ora ci sono e
dicono il contrario. **Le domande del quiz sono già a schermo, i nomi no** —
quindi sono i nomi a doversi adeguare, tranne dove è la domanda a essere
sbagliata.

## Il nucleo atomico è dentro — 2026-08-09, quattordicesima sessione

**Il primo lotto della Fase 2**, e il primo che entra in **due dizionari
insieme**: 203 nomi di `db_creature.hsp` più 373 stringhe di evoluzione di
`action.hsp`, 576 voci per 380 firme e 372 rese distinte. 378 stringhe
inglesi, e le firme sono 380 perché due inglesi ne coprono due creature.

Si rifà in un comando:

```powershell
python -m strumenti.creature --nucleo --uscita lavoro/fase2-nucleo-001.jsonl
```

**Le firme sono 380 e le rese 372** perché otto giapponesi compaiono con due
inglesi diversi. Non è rumore: è il motivo per cui il giapponese arbitra (vedi
`decisioni.md`, quattordicesima sessione).

`<Pants of Ogre>` → «`<Mutande dell'Ogre>`» chiude `db_item.hsp` a **1.606 su
1.606**. Rinviate da 80 a **79**: restano le 59 risposte del quiz, che aspettano
gli altri ~930 nomi, e le 20 `elename()` che aspettano `proc.hsp`.

⚠️ **Cinque delle 59 sono già sbloccate nel merito** — `steel golem`, `spider`,
`scorpion`, `black widow`, `paralyzer` sono nel nucleo — ma restano rinviate
perché il motivo dice «insieme a quelli», e «quelli» sono 203 su 1.131. Si
sciolgono col resto.

## `skill.hsp` è chiuso — 2026-08-09, tredicesima sessione

**Quarto file completo**, 885 su 885, e il più grosso dei quattro dopo
`db_item.hsp`. L'ultimo blocco erano le **276 mosse speciali**, tetto 24
caratteri già misurato il giorno prima.

Quindici nomi restano inglesi per scelta, dichiarati in `invariati.md`.
⚠️ **La regola della marca 《》 degli artefatti non si applica alle mosse**: il
nome di un artefatto è un nome proprio, quello di una mossa è un'etichetta
funzionale che si sceglie da un elenco. Vedi `decisioni.md`.

## Le rinviate scendono da 120 a 80 — 2026-08-09, tredicesima sessione

Tre dei cinque motivi erano scaduti o falsi.

| gruppo | voci | esito |
|---|---|---|
| risposte del quiz sui grimori | 4 | il rinvio era a `skill.hsp`, che oggi è chiuso |
| parti meccaniche `Change …` | 6 | ⚠️ **la dipendenza dichiarata non esisteva**: in `db_item.hsp` non ce n'è nessuna |
| nomi casuali degli oggetti | 30 | risolti con 213 toppe generate, vedi sotto |
| risposte del quiz su creature | 59 | rinvio **vivo**: aspettano i nomi di creatura |
| `elename()` | 20 | rinvio **vivo**: aspettano `proc.hsp` |
| `<Pants of Ogre>` | 1 | rinvio **vivo**: aspetta `orc`/`ogre` |

I nomi casuali hanno chiesto il primo ribaltamento d'ordine del progetto:
`db_item.hsp` compone «aggettivo + nome» in **213 siti**, e in italiano
l'aggettivo segue il nome. L'ordine sta nel codice, non nelle stringhe, quindi
il dizionario non lo raggiunge: le toppe le genera
`strumenti/genera_toppe_casuali.py`, una per sito, ognuna con l'aggancio unico
del proprio `ITEM_ID`.

⚠️ **Il genere è una proprietà dell'array, non della riga**, come l'articolo dei
pesci: le rese si accordano una volta per famiglia. Le sei firme condivise fra
due famiglie prendono la **forma invariabile** — quattro sono materiali e lo
sono già, due l'hanno presa apposta.

## `item_data.hsp` è chiuso — 2026-08-09, undicesima sessione

**Secondo file completo**, e a differenza del primo senza nemmeno un rinvio:
318 su 318.

I 235 rimasti a inizio sessione non erano un mucchio. La classe qui non è
`reftype` come in `db_item.hsp` ma **l'array che dichiara la voce**, e con
quella chiave si sciolgono in cinque discipline diverse, chiuse in tre lotti:

| lotto | criterio | voci |
|---|---|---|
| ego | `egoname` + `egominorn` | 29 |
| pesci | `fishdatan` | 113 (10 invariati) |
| incantamenti | `encDisp`, le dinamiche di `*item_encdetail`, `ammoname` | 93 (2 invariati) |

Le tre cose che il file ha insegnato, in ordine di prezzo:

1. **Il posto decide se i dati arrivano in tempo.**
   `ioriginalnameref(ITEM_ID_FISH)` è la stringa vuota: il nome della specie è
   *tutto* il nome e arriva da `itemNameSub`, che gira **dopo** l'articolo.
   Tradurre i 113 nomi e basta avrebbe dato «a salmone», e nessun test lo
   avrebbe visto.
2. **L'ego va dopo il materiale**, il che vuole una coda propria (`s10`)
   riversata fra materiale e stato.
3. **Il soggetto sta fuori dai file estratti.** `lang("それは", "It ")` è in
   `command.hsp`, e `s` compare in quattro siti di cui tre senza soggetto: le
   rese sono verbi alla terza persona senza soggetto, e il prefisso si spegne
   con una toppa.

## `db_item.hsp` è chiuso — 2026-08-09, decima sessione

**Primo file completo del progetto**: 1.605 firme su 1.606. L'unica mancante è
`<Pants of Ogre>`, che è **rinviata** e non dimenticata (vedi più sotto).

Il file è passato da 599 nomi da guardare a zero in una sessione, con sei lotti.
Il criterio non è stato la forma del nome, che era il candidato scritto qui
ieri, ma **la categoria che il sorgente dichiara**.

I lotti dal terzo al sesto erano stati scelti per `filter_item`. Quando quel
criterio si è esaurito, ciò che restava si chiamava «il gruppo senza filtro»: un
residuo da affrontare a occhio. Non era un residuo. La categoria c'è, solo che
sta **dentro il blocco di ogni oggetto** — `reftype = FILTER_ITEM_...` — e
classifica **1.320 oggetti**.

Lo strumento è `strumenti/categorie.py`, con cinque test:

```powershell
python -m strumenti.categorie                                 # il resto, per categoria
python -m strumenti.categorie --categoria FILTER_ITEM_TOOL --uscita lavoro/x.jsonl
```

⚠️ **Vale anche per gli altri file.** `item_data.hsp` e i cinque mai guardati
non sono stati letti con questa chiave: prima di dichiararli senza struttura,
si cerca dove il codice li struttura.

| lotto | criterio | voci |
|---|---|---|
| artefatti fra `<>` | forma del nome più la marca 《》 | 169 (105 invariati, 63 tradotti, 1 rinviato) |
| arredamento da `map_fur_*` | array del generatore di mappe | 46 |
| cibo | `FILTER_ITEM_FOOD` | 51 |
| arredamento | `FILTER_FURNITURE` | 100 |
| attrezzi | `FILTER_ITEM_TOOL` | 107 |
| scarto | `FILTER_JUNK` | 59 |
| code corte | nove categorie insieme | 67 |

**Sui 169 artefatti la domanda era di invarianza, non di resa**, e la regola sta
in `decisioni.md`: l'inglese romanizzato o siglato resta; il giapponese fra
《》 e traslitterato resta; il giapponese descrittivo si traduce. La prova che
non è stata cucita addosso al lotto è che riproduce tutti e otto i precedenti
già presi.

`item_data.hsp` è entrato il 2026-08-08, e non era nel piano: ci sono i **45
materiali** (`mtname`), che il primo collaudo ha mostrato anteposti al nome in
ordine inglese — «bronze corazza». Le 83 voci fatte sono i 38 materiali, i 38
epiteti e le 7 piante dei semi; le altre 235 sono altri dati degli oggetti,
ancora da guardare.

L'ordine è quello del piano, per visibilità decrescente: quello che si vede di
più si traduce prima, così ogni lotto ha valore anche se il progetto si ferma lì.

`db_item.hsp` è entrato in coda il 2026-08-07, quando `siti()` ha imparato il
**secondo tipo di sito** (`contratto-nomi.md` §2). La percentuale totale è scesa
dal 10% all'8% senza che nessuno abbia disfatto niente: il denominatore era
incompleto, e i nomi degli oggetti erano lavoro che il conteggio non vedeva.
Una metrica che scende perché ha smesso di mentire è una metrica migliore.

I 1.607 siti sono 1.321 blocchi canonici meno 12 nomi inglesi vuoti, più i 298
`ioriginalnameref2` non vuoti — i nomi che si compongono (`deed of camp`). Le
firme sono **1.606**, una sola in meno dei siti: una coppia giapponese-inglese
ripetuta.

⚠️ **Corretto il 2026-08-08: qui c'era scritto 1.591, e la differenza erano
esattamente le 15 firme che `estrai --da-tradurre` non offriva.** Il numero era
stato preso dall'uscita dell'estrazione invece che dalla scansione, e portava
dentro il suo difetto: `rinviate.jsonl` è indicizzato per firma, e 15 voci
rinviate su `text.hsp` (risposte del quiz, nomi casuali) hanno lo stesso
contenuto di 15 nomi di oggetto. Quei nomi sparivano da ogni lotto, e la
metrica li aveva già dimenticati.

**La regola che ne resta: il denominatore si misura sul sorgente, mai
sull'uscita di uno strumento.** Uno strumento che filtra fa passare il suo
filtro dentro il numero, e una metrica costruita così non può segnalare il
difetto che la produce. Le due misure vanno tenute separate e confrontate: se
`verifica --dizionario` e `estrai --da-tradurre` non tornano, è un difetto, non
un arrotondamento.

## Prima di cominciare un file nuovo

La ricerca delle stringhe che sono dati. Quella scritta nel piano
(`grep -nE '(=|==|!=|instr\().*lang\('`) è **troppo larga**: su `text.hsp`
restituisce 1.187 righe, quasi tutte array di etichette. Le due che servono:

```powershell
# confronti veri e scritture nei campi del salvataggio
grep -nE '(==|!=|instr\()[^=]*lang\(|cdatan?\([^)]*\) *= *.*lang\(' <file>.hsp
```

E soprattutto la misura **per firma**, che è quella che conta, perché una firma
condivisa fra un sito-dato e un sito-display non si può separare traducendo:
vedi `invariati.md`, sezione «valori di dato», e le sei toppe di `text.hsp`.

Su `text.hsp`: 7 firme su 1.740 toccavano un sito-dato. Trovarle prima è costato
mezz'ora; trovarle dopo sarebbe costato un salvataggio rotto.

## Rinviato alla Fase 2

Voci estratte, **non** tradotte, e non dimenticate: `verifica.py` continua a
segnalarle. Non sono un debito di traduzione ma una dipendenza da una decisione
che questa fase non prende.

L'elenco vero è `rinviate.jsonl`, che `estrai --da-tradurre` legge: senza di
esso queste voci tornerebbero in testa a ogni estrazione e andrebbero riscartate
a mano. Il `motivo` è obbligatorio, come per le toppe.

| gruppo | voci | perché |
|---|---|---|
| nomi casuali degli oggetti (`text.hsp:176-192`) | 30 | `_namepotion`+`strpotion` costruiscono «clear potion». In italiano cambia **l'ordine** («pozione trasparente») oltre al genere, e gli aggettivi sono condivisi fra sei classi di sostantivo con generi diversi: «pozione chiara» ma «anello chiaro» |
| `elename()` (`text.hsp:203-271`) | 20 | → **con `proc.hsp`, in questa fase.** Aggettivo elementale che modifica la parte del corpo di `_melee(2,…)`: `proc.hsp:8797` compone `elename(ele) + " " + _melee(2,…)`. In italiano l'aggettivo segue il nome e ne prende il genere, e i nomi sono di generi misti (mano, artiglio, zanna, occhio). L'ordine si sistema traducendo `proc.hsp`, che è una dinamica e permette di riordinare la concatenazione |
| nomi di magia nel quiz (`text.hsp:978-987`) | 4 | → **con `skill.hsp`, in questa fase** |
| nomi di creatura e oggetto nel quiz | 59 | risposte del quiz che nominano creature e oggetti. Il nome vero sta in `db_creature.hsp`/`db_item.hsp`: tradurlo qui prima farebbe divergere la risposta dal nome che il giocatore legge |
| parti meccaniche (`text.hsp:1387-1402`) | 6 | verificato che compaiono anche in `db_item.hsp` |
| `<Pants of Ogre>` (`db_item.hsp`) | 1 | il nome contiene `ogre`, e in `db_creature.hsp` `orc` e `ogre` convivono come creature distinte (`orc warrior`, `black orc` contro `slash ogre`, `shine ogre`): «orco» non può coprirle entrambe. **Primo rinvio deciso da `db_item.hsp`**, e per questo `test_i_nomi_di_db_item_non_sono_rinviati_da_text` ha smesso di asserire `== set()` — era una procura — e adesso pretende la proprietà vera: ogni firma che esce per `db_item.hsp` viene da una riga **di** `db_item.hsp` |
| **totale** | **120** | |

## Le 35 uscite della nona sessione (2026-08-08)

Sono uscite dal rinvio `_furniture` (11), `_bookself` (7), `_bookselfs` (7) e
`_weight` (10). Il motivo del rinvio era corretto quando fu scritto — «aggettivi
prefissi a un nome di genere ignoto, che vive in `db_item.hsp`» — ed è caduto
quando i nomi sono entrati nella catena.

⚠️ **Ma il rinvio le trattava come un gruppo solo, e non lo erano.** Quattro
array che il documento dava per «la stessa identica forma» hanno chiesto
**quattro cure diverse**, e scoprirlo è stato il lavoro vero della sessione:

| array | dove esce in inglese | cura |
|---|---|---|
| `_furniture` | prefisso al nome | toppa: sposta in `locvar_itemname_s6`, rese a complemento invariante |
| `_bookself` | **già fra parentesi** (`item_func.hsp:988`) | **nessuna toppa**: solo dato. L'unico della famiglia in cui il sorgente andava bene |
| `_weight` | già suffisso, ma con giunto « grown » | toppa **sul giunto**: « di taglia » introduce una testa femminile fissa, e l'accordo smette di dipendere dall'oggetto |
| `_bookselfs` | slot della parola-contatore (`item_func.hsp:1233`) | trattamento di `contatori.jsonl`: singolare, plurale, genere, e un `case` in **entrambi** gli switch |

**La lezione, che vale oltre questi quattro: «stessa forma» è un'ipotesi, non un
fatto, e va verificata guardando il sito di concatenazione prima di scrivere la
toppa.** Il documento di ripresa li dava per identici in buona fede, sulla base
del fatto che sono tutti aggettivi prefissi in `text.hsp`. Lo sono nel
dizionario; non lo sono nel codice, ed è il codice che decide la cura.

⚠️ **Un legame fragile creato qui, da ricordare.** Fra `contatori.jsonl` e il
dizionario il legame è **per stringa**: il `case` dello switch confronta la resa
del primo con quella che l'array porta a runtime, che viene dal secondo. Se
divergono il `case` non aggancia mai — e restano verdi sia il compilatore sia la
prova d'identità. Ora lo pretendono `genera_toppe_nomi.py` (alla generazione) e
un test (a ogni giro).

**Coperte anche le altre 39, il 2026-08-09.** `contatori.jsonl` ha tre fonti:
`text` (le sette del libro prodotto) e `item_func` (le sei cablate) alimentano
il generatore ed erano già difese; le **39 con `fonte: "db_item"`** sono il
registro di ciò che il dizionario dice per lo slot `ioriginalnameref2`, e su di
esse non guardava nessuno.

Il confronto giusto **non è l'uguaglianza**, e a insegnarlo è `grave`: il
registro dice «tomba», il dizionario «tomba ornata», e ha ragione il dizionario,
perché il nome si monta `s2 + " " + s3 + " " + s1` col giunto fissato a «di» e
l'aggettivo deve stare in `s2` per accordarsi con la testa. A schermo esce
«tomba ornata di fiori». Il registro dice il **termine**, il dizionario il
**segmento**: due livelli, non due verità. Il test pretende quindi che la resa
del dizionario **cominci con** il termine del registro.

**Tre uscite precedenti, sempre il 2026-08-08: `blessed`, `cursed`, `doomed`.** Erano rinviate
perché si antepongono al nome e in italiano un participio si accorderebbe con
un oggetto di genere ignoto. La premessa del rinvio — «i nomi di `db_item.hsp`
non li risolviamo in questa fase» — è caduta quando i nomi sono entrati nella
catena, e la forma è la stessa degli epiteti del materiale: **complemento**,
«con benedizione», che non chiede accordo a nessuno. Le tre stringhe si
spostano in coda con `locvar_itemname_s7` (`item_func.hsp:1204, 1207, 1210`,
solo il ramo inglese).

Il resto del loro motivo **non** è caduto: il sistema dei nomi casuali resta
rinviato, ed è un problema suo.

⚠️ **Il conto è cresciuto da 68 a 157 in un lotto solo**, ed è quasi tutto la
stessa dipendenza: i nomi di creature e oggetti della Fase 2. Vale la pena
guardarlo prima di tirare avanti — la Fase 1 sta accumulando debito verso una
decisione che non ha preso, esattamente come `init.hsp` accumulava debito
verso il registro finché non è stato promosso da Fase 4 a Fase 1.

Sono **aggettivi prefissi al nome di un oggetto**, e in italiano un aggettivo
prefisso vuole il genere del nome che segue. Quel nome vive in `db_item.hsp`,
e il piano della Fase 1 dice esplicitamente di non risolvere dove stanno i nomi
degli oggetti (SPEC §2, punto ancora aperto). Tradurli ora significherebbe
scegliere un genere al posto di quella decisione, in 35 punti, in silenzio.

È lo stesso nodo dell'articolo di `name()`, risolto nella quarta sessione
rimandando la scelta a chi conosce il nome. Qui si rimanda allo stesso posto.


## Fase 3 — i file dati di `data\` (dalla 70a)

L'unita' e' la **riga inglese** dentro un blocco `%…,EN`. Il conto vivo:

```powershell
python -m strumenti.dati_verifica lavoro/<file>-001.jsonl
```

| file | tradotte | righe EN | % | famiglia |
|---|---|---|---|---|
| `board.txt` | **25** | 25 | **100%** | senso |
| `talk.txt` | **569** | 569 | **100%** | senso |
| `exhelp.txt` | **185** | 185 | **100%** | impaginazione |
| `book.txt` | **2.241** | 2.241 | **100%** | impaginazione |
| `manual_ENG.txt` | **591** | 591 | **100%** | impaginazione |
| `autopick.txt` | **156** | 156 | **100%** | ⚠️ configurazione |
| **totale** | **3.767** | **3.767** | **100%** | |

⭐⭐⭐ **DALLA 101ª `data\` È CHIUSA.** Sei file su sei, e i cinque che vanno nel
gioco (`board_it.txt`, `talk_it.txt`, `exhelp_it.txt`, `book_it.txt`,
`autopick_it.txt`) più `manual_ENG_it.txt`, che è il sesto dalla 101ª. Le 1.984
righe di `book.txt` sono state fatte in **un giorno solo** (99ª), in nove lotti
raggruppati per voce e non per dimensione.

⭐ **Le 2.208 righe di `book.txt` sono diventate 2.241 nella 101ª**, e non è
lavoro comparso dal nulla: sono i **33 titoli del blocco `%DEFINE`**, che fino
alla 100ª nessun conteggio nominava. `item.hsp:112`-`:124` legge quel blocco
come una **CSV** (`csvsort`, virgola per separatore) e ne ricava `booktitle`,
che `item_func.hsp:907` incolla al nome dell'oggetto: « dal titolo <...>».
L'unità lì non è la riga ma la **colonna**, e a saperlo è `dati.COLONNE_CSV`.
Per esteso in `decisioni.md` §101ª.

⚠️ **`autopick.txt` era entrato in tabella nella 98ª, e non era lavoro nuovo:
era un difetto in campo** — `custom_autopick.hsp:358` confronta le regole col
nome dell'oggetto, che da noi è italiano. Chiuso nella 100ª insieme a
`custom_autopick.hsp`, nello stesso lotto. Per esteso in `decisioni.md` §98ª.

⚠️ **Il manuale ha un vincolo che gli altri file dati non hanno: l'altezza della
sezione.** `help.hsp:468` lo disegna con `gmes` in una pagina da **436 px**, e
ogni riga del file ne costa 18: ventiquattro righe e si è pieni. Due sezioni
sfondano **già in inglese** (*Abnormal States*, 624 px; *Ranged Weapons*, 468) e
non c'è resa che le aggiusti, perché l'altezza la fa il numero di righe, che è
fisso. La rete è `scratchpad/_101-manual-gmes.py`, e il valore atteso è **2 e
0**: due sezioni alte di monte, zero titoli oltre i 21 caratteri.

### ⭐⭐⭐ Che cosa ha insegnato `book.txt`, chiuso (99a)

Trentadue libri in nove lotti. Il file e' il piu' vario del progetto — un
manuale commerciale, un articolo scientifico, un volantino da lega per la
temperanza, un regolamento di gioco, un diario di prigionia — e le tre cose che
si portano al file dopo sono queste.

**1. Il metro si misura sulla forma DEGRADATA, e conviene misurarlo prima.**
Nel dizionario «e' » sta in un carattere, nell'albero di build in due
(`accenti.degrada`). Ogni lotto di `book.txt` e' passato da uno script che
degrada e conta **prima** di scrivere il JSONL, e si ferma se una riga supera i
43. Nessuna riga e' mai arrivata alla rete fuori misura: 2.208 su 2.208 dentro,
la piu' larga **39** — cioe' l'italiano non passa mai la misura piu' larga che
monte inglese usa.

**2. Il conto delle righe di ogni paragrafo e' un vincolo, non un consiglio.**
`dati_applica` **sostituisce** righe senza aggiungerne, e le righe vuote fra un
paragrafo e l'altro non sono nel lotto: dentro un paragrafo il testo si
ridistribuisce a piacere, da un paragrafo all'altro no. I confini si leggono
con `scratchpad/_99-para-book.py`, che stampa i gruppi di righe piene.

**3. La spaziatura in testa e' contenuto.** Nessuno di questi file ha un motore
che impagina o centra: monte conta gli spazi a mano. In `book.txt` ci sono
insegne centrate con sei spazi (`%8`), con dodici (`%4`), tabelle incolonnate
alla **colonna 23** e — in un punto solo, `%4` riga 80 — **due tab**. Un
rientro perso non fallisce nessuna rete: si vede a schermo e basta.

⚠️ **E un avvertimento per chi apre il manuale (`manual_ENG.txt`):** il tetto e
il motore di a capo di quel file **non si deducono da `book.txt`**. Vale la
regola della 98a — ogni file di questa famiglia ha il suo motore — e il tetto va
ricavato dal sito che lo disegna, non copiato dal vicino.

### ⭐⭐⭐ La famiglia dell'impaginazione ha TRE metri, e non si prestano (98a)

La regola della 55a — «prima la misura della colonna presa dalla geometria» —
si e' rivelata piu' esigente del previsto: **ogni file di questa famiglia ha un
motore di a capo diverso**, e usare quello del vicino non da' un tetto sbagliato,
da' una **rete che mente**.

| file | chi disegna | come manda a capo | tetto |
|---|---|---|---|
| `board.txt` | `talk_conv` | sulle **spaziature** | 70 caratteri |
| `talk.txt` | `talk_conv` | sulle spaziature | 53 |
| `exhelp.txt` | `gmes` (`module.hsp:4918`) | per **carattere** | 48, ma vince l'**altezza** |
| `book.txt` | `mes` (`command.hsp:8412`) | **non manda a capo affatto** | 43 |

- **`exhelp.txt`**: `help.hsp:227` carica con `noteload`, `:273` disegna con
  `gmes`, che avanza 7 px per carattere ASCII fino a `gmesw` = 330 px. Ma il
  vincolo vero e' verticale: finestra alta 175, testo da `wy + 55`, restano 120,
  e ogni riga di nota costa 18 px — **sei righe**. ⭐ Il tetto geometrico e il
  corpus di monte danno **lo stesso numero** (l'inglese sta a 108 px), e quando
  le due misure coincidono il tetto non e' una stima. Rete:
  `scratchpad/_98-exhelp-gmes.py`.
- **`book.txt`**: due colonne a 306 px di distanza (`command.hsp:8399`), 20
  righe ciascuna, e `mes s` senza alcun a capo — una riga lunga **entra nella
  colonna accanto**, e se e' quella di destra esce dalla pagina. 306 / 7 = 43.
  ⚠️ Qui geometria e corpus **non** coincidono: monte si ferma a 39, e la rete
  stampa a parte le righe fra 40 e 43 («strette ma dentro») invece di tacere.
  Rete: `scratchpad/_98-book-mes.py`.

⚠️⚠️ **Per questo `exhelp.txt` e `book.txt` hanno `tetto_capo: None` in
`PROFILI`**: la rete dell'altezza dentro `dati_verifica` rifa' `talk_conv`, e
puntata su di loro misurerebbe un motore che non c'e'. I loro tetti stanno nelle
due reti in `scratchpad/`, e nessuno dei due file ha un espansore di segnaposto
— `noteload` e via — quindi **qualunque** graffa resterebbe a schermo.

⚠️ **E l'inglese di questa famiglia e' a capo fisso**: una frase sola spezzata a
mano. `dati_applica` **sostituisce** righe senza aggiungerne, quindi ogni blocco
italiano deve avere **lo stesso numero di righe** dell'inglese — lo strumento
delle rese se lo controlla da se' prima di scrivere. In `book.txt` in piu' la
**struttura** (titolo, intestazioni di sezione, elenco geografico, riquadro
dell'esempio) va tenuta **al suo indice**; dentro un paragrafo invece le righe
sono solo un a capo tipografico e il testo si ridistribuisce a piacere.

💡 **Il margine non e' uniforme, e va guardato per gruppo prima di tradurre.**
Su `exhelp.txt` era il 37% complessivo, ma cinque gruppi stavano fra il 10 e il
16% — il peggiore `%1` sui grimori, 219 caratteri in 240. Un margine medio non
dice dove si dovra' comprimere.

⭐ **La famiglia del senso e' CHIUSA** (71a): `board.txt` e `talk.txt` sono
tutt'e due al 100%. Quel che resta e' la famiglia dell'impaginazione, dove la
riga e' un'unita' di **disegno** e vuole prima una misura della colonna presa
dalla geometria (regola della 55a).

⚠️ **La famiglia decide l'unita' di traduzione.** Dove la riga e' un'unita' di
**senso** il gioco ne pesca una a caso (`rnd`) e si traduce riga per riga; dove
e' un'unita' di **disegno** l'inglese e' spezzato a mano a larghezza fissa
(`book.txt`: 33 righe giapponesi contro 224 inglesi) e l'unita' e' il blocco.

⚠️ **E ogni file ha il suo espansore di segnaposto**: `board.txt` passa da
`*talktxt_conv` (33 nomi), `talk.txt` da `*convert_word` (46). Stanno in
`PROFILI`, dentro `strumenti/dati_verifica.py`.

`talk.txt` e' stato chiuso in **otto lotti** (71a), raggruppati per *chi
parla* e non per posizione nel file:

| lotto | che cosa | righe |
|---|---|---|
| 001 (70a) | `DEFAULT` e le quattro `PERSONALITY` | 64 |
| 002 | chi ti parla addosso: compagni, mestieri, figure | 58 |
| 003 | le citta' della Tyris del Nord | 61 |
| 004 | il rifugio e le citta' della Tyris del Sud | 58 |
| 005 | voci sul bottino, feste, dei, campo di battaglia | 56 |
| 006 | Irva Perduta e i suoi presidi | 62 |
| 007 | la nave divina e i biscotti della fortuna | 68 |
| 008 | le varianti d'aprile dei luoghi | 81 |
| 009 | le varianti d'aprile di chi parla | 61 |

⚠️⚠️ **Il conto pari delle righe NON prova l'allineamento fra le due lingue.**
Quattro blocchi lo hanno smentito in modi diversi, e nessuna rete lo vede:

| blocco | forma | che cosa succede |
|---|---|---|
| `MOYER` | 2 contro 2 | **scambiato**: EN|1 rende JP2, EN|2 rende JP1 |
| `AREA,12` | 8 contro 8 | **sfalsato**: da EN|4 in poi scala di uno, JP4 buttata, EN|8 inventata |
| `BSHIP7` | 17 contro 30 | EN|13 e EN|14 scambiate fra loro |
| `AAREA,12` | 5 contro 6 | sfalsato, JP1 buttata |

💡 Uno **sfalsamento** e' piu' insidioso di uno scambio: le prime righe
combaciano e sembrano confermare l'allineamento.

⚠️ **I blocchi con la `A` davanti sono le varianti di APRILE**, non un'altra
famiglia di parlanti: `text.hsp:9609` e seguenti li scelgono con
`gdata(GDATA_MONTH) == 4`. E due sono **morti**: `%ABITCH` e `%AKASHIC` non
sono referenziati da nessuna parte.

## I file dati sono CINQUE, e `autopick.txt` è chiuso — 2026-08-26, centesima

    file             righe   stato
    board.txt           25   ⭐ CHIUSO (92ª)
    talk.txt           569   ⭐ CHIUSO (97ª)
    exhelp.txt         185   ⭐ CHIUSO (98ª)
    book.txt         2.208   ⭐ CHIUSO (99ª)
    autopick.txt       156   ⭐ CHIUSO (100ª)
    ---------------------------------------------
    manual_ENG.txt     591   ⚠️ da fare, il solo che resta in `data\`

⚠️ **`autopick.txt` non era «un sesto file da tradurre»: era un difetto già in
campo**, e la 100ª l'ha misurato invece di stimarlo — **undici regole su undici**
del modello non agganciavano più niente nella nostra build, non sei come diceva
la 98ª (`scratchpad/_100-modello-aggancia.py --scaduto`).

E con lui si chiude anche `custom_autopick.hsp`, che non era un file di `.hsp`
come gli altri: 78 delle sue 90 `lang()` sono **chiavi**, non etichette, e i due
file si sono tradotti nello stesso giro perché il guasto peggiore sta a metà
strada. Vedi `decisioni.md` §98ª e §100ª, e le 54 chiavi in `glossario.md`.

    python scratchpad/_97-quanto-resta.py     custom_autopick.hsp  2 / 2  ⭐ CHIUSO

⚠️⚠️ **E l'elenco dei file senza dizionario andava rimisurato, non ricopiato.**
La ripresa lo portava avanti come «nove file» nominandone otto, e con dei numeri
che erano **occorrenze**. Lo strumento c'era già:

    python scratchpad/fuori_elenco.py     12 file senza dizionario, 447 lang()

        txtadv.hsp                  176        etc.hsp                     17
        material_data.hsp           118        map_rand.hsp                 6
        net.hsp                      39        custom_pet.hsp               4
        custom_itemenchantment.hsp   31        scene.hsp                    3
        quest.hsp                    26        custom_dmgpop.hsp            3
        material.hsp                 22        custom_nefiatypes.hsp        2

⚠️ **Quattro di quei dodici non erano in nessun elenco** — `map_rand.hsp`,
`custom_pet.hsp`, `scene.hsp` e `custom_dmgpop.hsp`, sedici `lang()` in tutto —
e non perché qualcuno li avesse scartati: la riga si ricopiava di sessione in
sessione senza essere rilanciata.

ⓘ In **firme** (l'unità del dizionario) sono 10 file e 344 firme: due di quei
dodici hanno solo `lang()` che `estrai` non estrae. Le due misure rispondono a
due domande diverse e vanno tenute separate, come le colonne qui sopra.

Perimetro onesto (`scratchpad/perimetro.py`): **81%**, era 80%.

## `db_card.hsp`, dal lotto 7 al 10 — 2026-08-26, centotreesima

Quattro lotti in una sessione, righe 3101-5100, **154 rese**. Il conteggio,
rilanciato in chiusura e non ricopiato:

    python scratchpad/_97-quanto-resta.py

        db_card.hsp     861 da fare -> 752      (erano 906 in apertura)
        TOTALE          938 / 109 / 829   ->   861 / 109 / 752

    python scratchpad/perimetro.py            **84%**, era 83%

Il passo è quello della 102ª e non è cambiato: `_102-dossier.py <da> <a>` per
appaiare la prosa al nome già reso, `modello-rete6-barre.py` per le reti,
`_102-carta-conoscenza.py` dopo ogni `reimporta`. Le tre reti hanno detto
**0 code perse e 0 parole spezzate** dopo ognuno dei quattro lotti.

⭐ **Ma il rendimento vero di questi lotti non sta nelle rese.** In quattro
lotti sono usciti **nove errori di monte** verificabili riga per riga, e un
**nome del progetto sbagliato da settanta sessioni**. Le prose delle carte
descrivono creature i cui nomi sono già inchiodati: leggerle è insieme lavoro
nuovo e collaudo di quello vecchio. Vedi `decisioni.md`, sezione della 103ª.

### Gli strumenti nati oggi

| strumento | a cosa serve | quando si lancia |
|---|---|---|
| `scratchpad/_103-chiavi-card.py` | stampa le chiavi `(riga, en)` di una zona col `repr()` dell'inglese, pronte da incollare in `RESE` | all'apertura di ogni lotto di `db_card`, dopo il dossier |
| `scratchpad/_103-inglese-ripetuto.py` | le carte a cui monte ha dato l'inglese di un'altra, su **tutte** le 1.146 voci | referto, non guardia: si legge quando si apre un lotto nuovo |
| `scratchpad/_103-carte-a-rischio.py` | ordina le rese per parola più lunga e riga media più corta, per scegliere quali carte guardare a schermo | prima di scrivere una lista di collaudo |
| `scratchpad/correzione-cub.py` | la correzione di `カブ`, tenuta perché dice **perché** | una volta sola, già girata |

⚠️ `_103-carte-a-rischio.py` **importa** `impagina` e `degrada` da
`_102-carta-conoscenza.py`: non si riscrivono. La prima stesura le riscriveva e
dava numeri che contraddicevano la rete.

Perimetro onesto (`scratchpad/perimetro.py`): **84%**, era 83%.


## `db_card.hsp`, dal lotto 11 al 14 — 2026-08-26, centoquattresima

Quattro lotti, righe 5101-7100, **153 rese**. Il conteggio, rilanciato in
chiusura e non ricopiato:

    python scratchpad/_97-quanto-resta.py

        db_card.hsp     752 da fare -> 599      (erano 752 in apertura)
        TOTALE          861 / 109 / 752   ->   708 / 109 / 599

    python scratchpad/perimetro.py            **84%**, fermo

    dizionario/db_card.hsp.jsonl              1.687 voci
                                              = 1.141 nomi + **546 prose su 1.144**

Il passo è quello della 102ª e non è cambiato. Le reti hanno detto **0 code
perse e 0 parole spezzate** dopo ognuno dei quattro lotti.

### ⭐⭐⭐ Il rendimento vero: una rete della 103ª contava tre e il difetto era nove

`_103-inglese-ripetuto.py` cerca due prose inglesi **uguali**, e con quello
aveva trovato «tre carte con l'inglese di un'altra». Aprendo il lotto 14, il
dossier ha mostrato che `:6959`/`:6972` non è una coppia: è la **testa di una
catena**. L'inglese giusto della carta copiata non si perde — **spinge in
avanti** quello di tutte le successive — e da `:6972` a `:7063` l'inglese di
monte è indietro di un posto per **nove carte**. Monte si riallinea a `:7076`
buttando via l'inglese di `:7063`, che nel sorgente non esiste da nessuna parte.

⭐ **Perché la rete taceva:** dal secondo anello in poi ogni inglese compare
**una volta sola**, e una rete che cerca doppioni vede solo il primo.

⚠️⚠️ **Il guasto ha due forme, e si distinguono solo leggendo.** Verificate le
altre due teste: `:4125` (riparata dalla 103ª) e `:9637` sono **doppioni
isolati** — `:4138` e `:9650` hanno il loro inglese, la catena non parte. Da un
doppione non si può quindi dedurre quale forma sia. **Regola nuova: quando salta
fuori un doppione, si legge il dossier delle venti carte successive.**

### Gli strumenti nati oggi

| strumento | a cosa serve | quando si lancia |
|---|---|---|
| `scratchpad/_104-inglese-slittato.py` | trova le **teste** (l'inglese copiato dalla carta prima) e stampa la finestra delle venti carte successive coi due segnali deboli | referto, non guardia: si legge insieme a `_103-inglese-ripetuto` |
| `scratchpad/correzione-kikkasu.py` | unifica `キッカス` → **Kikkasu** in 3 voci, nome di creatura compreso | una volta sola, già girata |
| `scratchpad/correzione-eln.py` | unifica `エルン` → **Eln** in 1 voce | una volta sola, già girata |

⚠️⚠️ **`_104-inglese-slittato` è stato provato al contrario, e non basta da
solo.** Puntato sul blocco `:6972`-`:7063`, dove il difetto c'è di sicuro, i suoi
due segnali automatici — il nome della carta dentro la prosa, e il rapporto fra
le lunghezze — accendono su **cinque carte su nove**. È dichiarato per quello
che è: un aiuto alla lettura, non un cancello.

⚠️ **E le due reti vanno lette insieme, perché nessuna vede quello che vede
l'altra.** `_104` trova le copie esatte (`:6972`, `:9637`) e cammina lungo la
catena; `:4125` non la trova, perché quel suo inglese non è una copia di `:4112`
ma una **traduzione diversa dello stesso giapponese** — somiglianza **0,30**.
Quella la trova `_103`, che confronta le parole e non la stringa.

Perimetro onesto (`scratchpad/perimetro.py`): **84%**, fermo. Il salto vero
resta il blocco delle 5.284 descrizioni di `db_item.hsp`.

## `db_card.hsp`, dal lotto 15 al 18 — 2026-08-26, centocinquesima

Quattro lotti, righe 7101-9100, **154 rese**. Il conteggio, rilanciato in
chiusura e non ricopiato:

    python scratchpad/_97-quanto-resta.py

        db_card.hsp     599 da fare -> 445      (erano 599 in apertura)
        TOTALE          708 / 109 / 599   ->   554 / 109 / 445

    python scratchpad/perimetro.py            **85%**   (era 84%)

    dizionario/db_card.hsp.jsonl              1.841 voci
                                              = 1.141 nomi + **700 prose su 1.144**

Il passo è quello della 102ª e non è cambiato. Le reti hanno detto **0 code
perse e 0 parole spezzate** dopo ognuno dei quattro lotti. Nessuna toppa nuova
(`toppe.jsonl` resta 1027), nessuna rinviata nuova (112), nessuna rete nuova.

### ⭐⭐⭐ Il rendimento vero: quattro rese sbagliate che tutta la catena ha lasciato passare

Non è un difetto di monte come quello della 104ª: è un difetto **mio**, e le
reti non potevano vederlo perché nessuna di loro legge `glossario.md` o
`invariati.md`.

    手裏剣                          stelline da lancio  ->  shuriken
    レム・イド                      Rehmido             ->  Rehm-Ido
    精霊が◯◯を象って実体化した存在  parole mie          ->  la formula fissa
    眷属 (混沌の—)                  creatura al seguito ->  il figlio del caos

Tutte e quattro erano passate da `verifica` («39 voci, nessun problema»), da
`guardie` (0 0 0), dalle tredici reti dello script di lotto e da `referti`. Le
ho trovate rileggendo i documenti per scrivere la chiusura. Il ragionamento
completo sta in `decisioni.md`, sezione della 105ª; i termini stanno nel
glossario, sezione della 105ª.

⚠️ **Rendimento misurato della rete che manca: quattro su 154 rese, in una
sessione sola.** È il punto 15 di quel che resta aperto, e va provata al
contrario sulle quattro rese di oggi prima di crederle.

### Due proprietà dei blocchi, che non sono decisioni

- **Nel lotto 18, quattordici carte su trentotto hanno l'inglese che finisce con
  uno spazio** (`:8740`, `:8805`, `:8870`, `:8883`, `:8909`, `:8922`, `:8935`,
  `:8961`, `:8974`, `:8987`, `:9000`, `:9013`, `:9078`, `:9091`), e `verifica`
  pretende lo spazio anche in italiano. Conviene guardarlo **prima** di scrivere
  il lotto: la rete lo prende, ma dopo.
- **Due carte a due lotti di distanza raccontano la stessa storia dai due lati**:
  `:9091` è il nonno `<Stoke>` che manda le caramelle, `:8103` il ragazzo `<Wel>`
  che le riceve. Le due prose ora usano le stesse parole.

### La catena, prima e dopo la build

Diciannove verifiche in apertura, **diciannove ai valori attesi della 104ª**.
In chiusura la build è stata rifatta **due volte** — la seconda dopo le quattro
correzioni, perché la prima conteneva le rese sbagliate — e ogni volta con il
`grep` del segnale di guasto sull'output di `applica` (muto, **27.073**
sostituzioni), `_97-toppe-agganciate` **1027 su 1027**, `_96-morte-nella-build`
**0**, `compila --eseguibile` con `#No error detected.`. `cgx-test.exe` ricopiato
alle **15:30 del 26/08**. Nessuno dei sei file dati è cambiato: `cmp -s` li ha
lasciati tutti dov'erano.

## ⭐⭐⭐ `db_card.hsp` si chiude, dal lotto 19 al 30 — 2026-08-26, centoseiesima

Dodici lotti, righe 9101-15075, **444 rese** e **2 rinviate**. Il conteggio,
rilanciato in chiusura e non ricopiato:

    python scratchpad/_97-quanto-resta.py

        db_card.hsp     445 da fare -> **0**     ⭐ CHIUSO
        TOTALE          554 / 109 / 445   ->   **110 / 110 / 0**

    python scratchpad/perimetro.py            **86%**   (era 85%)

    dizionario/db_card.hsp.jsonl              **2.285 voci**
                                              = 1.141 nomi + **1.144 prose su 1.144**

    rinviate.jsonl                            112 -> **113**
    toppe.jsonl                               1027, invariato

⚠️⚠️ **Il registro delle rinviate sale di UNO, non di due, ed è giusto così.**
Le righe morte sono due — `:11405` (la prosa) e `:11412` (il nome), spente col
`;` dentro il blocco di `CREATURE_ID_HARD_GAY` e rimpiazzate una riga sotto
dall'`explosioman` — ma la **firma** di `:11412` era già nel registro, rinviata
da `db_creature.hsp`: stessa creatura spenta nei due file. ⓘ Il registro è
indicizzato per firma, non per riga.

⚠️ E il numero di partenza era **1.144**, non 1.146: `estrai --da-tradurre` non
filtra le righe morte, le filtra il modello di lotto. La 102ª lo aveva già
misurato; oggi è stato confermato dal fatto che le due righe cadono esattamente
nel lotto 23.

### La struttura dei lotti, per chi rifà i conti

    lotto 19   :9101-9600     39      lotto 25   :12101-12600   38
    lotto 20   :9601-10100    38      lotto 26   :12601-13100   39
    lotto 21   :10101-10600   39      lotto 27   :13101-13600   38
    lotto 22   :10601-11100   38      lotto 28   :13601-14100   39
    lotto 23   :11101-11600   38 + 2 rinviate    29   :14101-14600   38
    lotto 24   :11601-12100   39      lotto 30   :14601-15075   **21**

⭐ Il lotto 30 è corto perché le voci da `:14878` in poi **non sono carte di
creature**: sono le otto tessere del terreno (foresta, montagna, mare, isola,
palude, terra morta, pianura, distesa innevata) e le due carte di sistema
(`draw2Card`, `return`). Non hanno prosa.

### Le reti, lotto per lotto

`verifica` **nessun problema** su tutti e dodici; `guardie` **0 | 0 | 0** su
tutti e dodici; le tredici reti dello script di lotto **mute** su tutti e dodici;
`_102-carta-conoscenza` **0 code perse e 0 parole spezzate** dopo ognuno.
⚠️ Tre rese sono state respinte da `verifica` e riscritte: **dèi** (lotto 19),
**élite** (lotto 23) e **elite** (lotto 30), che `degrada()` porta ad avere
l'apostrofo dentro la parola.

### Che cosa è uscito, e sta scritto altrove

- **Tre nomi sdoppiati** — `イツパロトル` corretto, `かたつむり` e `パピー` aperti:
  `decisioni.md`, sezione della 106ª.
- **Una collisione al contrario**, due giapponesi diversi sulla stessa resa
  (`竜人` / `リザードマン` a `:9351`): stessa sezione.
- **Quindici errori di monte** presi dal giapponese, e l'elefante indiano che è
  una gag vera in dieci carte: `glossario.md`, sezione della 106ª.
- **Otto termini coniati** e **quattro formule che si ripetono**: stessa sezione
  del glossario.

### La catena, prima e dopo la build

Diciannove verifiche in apertura, **diciannove ai valori attesi della 105ª** —
sessantatreesima prova di fila con `origin/fase-0` allineato. Due build nella
sessione: la prima alle **16:25** dopo i lotti 19-22, la seconda alle **19:07**
con tutti e dodici. Ogni volta il `grep` del segnale di guasto sull'output di
`applica` è rimasto **muto**, `_97-toppe-agganciate` ha detto **1027 su 1027**,
`_96-morte-nella-build` **0**, `compila --eseguibile` `#No error detected.`.

    applica    27.073 -> 27.227 (dopo i lotti 19-22) -> **27.517**
               ⭐ 27.073 + 444 esatte: il numero atteso c'era e tornava

Nessuno dei sei file dati è cambiato: `cmp -s` li ha lasciati tutti dov'erano.
`pytest` **775 passed, 6 skipped**, `prova_identita` **72/72 e 28.073**,
`dati_applica --identita` **6 file e 3.767 righe**, `referti` fermo a **9**.

### ⚠️ Un numero che è cambiato da solo, e la spiegazione

`_102-carta-conoscenza` è passato da «riga media sotto 61: **1** su 1144» a
«**0**» senza che nessuno toccasse la carta sospetta. Non è un guasto: quel conto
gira su **tutte** le 1.144 carte e per quelle non rese misura **l'inglese**. La
carta era `:10196`, il cui inglese è una riga sola da 48 caratteri e il cui
italiano ne fa 70. ⭐ Verificato con `scratchpad/_106-media-riga.py`, non dedotto.

---

## 107ª sessione — 2026-08-27 — le descrizioni di `db_item.hsp` entrano nel perimetro

Diciannove verifiche in apertura, **diciannove ai valori attesi della 106ª** —
sessantaquattresima prova di fila con `origin/fase-0` allineato.

**Sessione senza una resa e senza una build**, ed è la sua natura, non una
mancanza: il fronte più grosso che restava non era un lotto ma lavoro
strutturale, e la ripresa della 106ª lo diceva («prima di tradurre serve capire
come si agganciano»).

### Che cosa è entrato

Le descrizioni degli oggetti sono il **terzo tipo di sito** di `estrai.siti()`,
dopo le `lang()` e i nomi. Non una catena a parte: così ereditano firma,
`verifica`, coda di ritraduzione e la **prova d'identità**, che è quel che tiene
in piedi la garanzia byte per byte.

    prova_identita   72/72   e 28.073 -> **30.905 sostituzioni**
                             ⭐ +2.832 esatte: il numero atteso c'era e tornava
    pytest           775 -> **792**   (17 test nuovi in test_descrizioni.py)
    verifica         db_item.hsp: 0 da ritradurre, **2.580 non ancora tradotte**
    _97-quanto-resta TOTALE **2.690 / 110 / 2.580**   (era 110 / 110 / 0)
    applica          **27.517**, invariate, col segnale di guasto muto
    toppe            1027 su 1027;  `_96-morte-nella-build` **0**

Il resto della catena è fermo dov'era, riverificato in chiusura.

### ⚠️ Il numero da cui si partiva era falso, non solo vecchio

`perimetro.py` contava le descrizioni con un automa suo che rendeva **5.284**:
tutte le righe, comprese le **2.452 che sono la stringa vuota**. Non era una
stima per difetto come quella delle firme `lang()` — era **quasi metà del
denominatore** di «a che punto siamo» occupata da lavoro che non esiste.

    perimetro dichiarato   100% -> **90%**   (2.832 stringhe vere sono ENTRATE)
    totale                  86% -> **93%**   (2.452 fantasmi sono USCITI)

⚠️ I due si muovono in **direzioni opposte** e vanno letti insieme. ⭐ E il
«salto dall'86% al 94%» che la ripresa della 106ª attribuiva a questo fronte era
gonfio della stessa quantità.

### La forma, misurata e non sperata

    blocchi DBMODE_DESC                          1321
    righe description() per ramo                 5284   (4 per oggetto)
    di cui VIVE (non stringa vuota)              2832
    firme distinte da tradurre                   2580
    traduzioni DAVVERO distinte                  2556
    blocchi asimmetrici / letterali sporchi      0 / 0
    righe `description(` fuori da un blocco      0 su 10.568
    descrizioni che trovano il loro ITEM_ID      **2832 su 2832**

### I quattro indici sono quattro cose diverse

| idx | vive | distinti | mediana | max | lettore |
|---|---|---|---|---|---|
| 0 | 1316 | 1308 | 205 | 716 | corpo del pannello, impaginato |
| 1 | 39 | 28 | 168 | 364 | idem |
| 2 | 158 | 104 | 115 | 343 | idem |
| 3 | **1319** | 1117 | 48 | 73 | ⚠️ **non impaginato: tetto secco 69** |

L'indice 3 è il rapporto di identificazione (`command.hsp:16275`) e finisce in
`listn` senza impaginatore: non va a capo, non si taglia, **sfora e basta**.
**110 sforano già in inglese**, quindi il numero che deve stare a zero è quello
che introduce l'italiano, non il totale.

### Le reti e gli strumenti nuovi

| file | a che serve |
|---|---|
| `_107-zona-sorgente.py` | una zona del sorgente pinnato, decodificata |
| `_107-struttura-db-item.py` | la forma dei blocchi `DBMODE_DESC` |
| ⭐ `_107-descrizioni-item.py` | la rete: corpo e tetto secco, a tre colonne |
| `_107-lotti-per-categoria.py` | le descrizioni per categoria di oggetto |
| ⭐ `_107-dossier-item.py` | la descrizione col **nome già reso** dell'oggetto |
| `_107-chiavi-item.py` | lo scheletro delle chiavi, con gli stessi filtri |
| ⭐ `_107-firme-gemelle.py` | gli inglesi che tornano più volte |

### ⚠️ Le cose andate storto, che sono la parte utile

1. **La prova al contrario della rete nuova era SPENTA al primo giro.** Diceva
   «0 code perdute», ma il testo finto costruito per farla accendere aveva le
   virgole ovunque, quindi righe lunghe, quindi nessuna coda persa. Ora cerca il
   caso peggiore — uno spazio al 57º carattere — e si accende a **911
   caratteri**, restando muta su sei testi innocui. ⭐ E dice anche **perché** lo
   zero è vero: l'inglese più lungo del file ha 716 caratteri, sotto la soglia.
   *Non è merito di nessuno*, e una resa molto più lunga lo riaprirebbe.
2. **Avevo chiamato l'`ITEM_ID` «una comodità per scegliere i lotti».** È invece
   la chiave che lega la descrizione al **nome italiano già reso** dello stesso
   oggetto — la dipendenza esatta per cui esiste il dossier delle carte.
3. **Avevo separato il fattore italiano/inglese per fasce di lunghezza** perché
   sospettavo che le rese corte fossero schiacciate dai tetti dei menu e la prosa
   si allungasse di più. **La misura lo smentisce**: tutte e quattro le fasce
   stanno a ~1,0, e quella dei 200+ caratteri — prosa vera, 1.482 rese — sta a
   **x1,000 esatto**. Il commento nel codice ora dice che il sospetto è caduto.
4. **Due test di conteggio sono caduti, e avevano ragione loro**: dicevano «tutte
   le voci di `db_item` sono nomi». Riportati a filtrare su `array` — ciò che *fa*
   di una voce un nome — invece che su un totale da aggiornare a ogni famiglia.
5. ⚠️ **Un heredoc aperto per niente**, ancora una volta, dentro un comando che
   non ne aveva bisogno. Non ha fatto danni (era un `print` di prova) ma è la
   settima volta che la mano ci va da sola.

### Il lotto da cui si comincia

`FILTER_ITEM_FOOD` indice 3: 133 righe ma **56 firme**, il più economico del
file, e fissa la formula del rapporto di identificazione che poi si ripete su
tutta la categoria.

🔶 **Prima serve un modello di lotto che selezioni per `RIGHE = {...}`** invece
che per `DA, A`: le descrizioni di una categoria sono sparse per novantamila
righe, e un intervallo prenderebbe dentro mezzo file.

## `db_item.hsp`, il primo lotto di descrizioni — 2026-08-27, centottesima

Un lotto solo, `FILTER_ITEM_FOOD` indice 3: **56 firme rese**, che coprono
**133 righe** del sorgente. Il conteggio, rilanciato in chiusura e non ricopiato:

    python -m strumenti.verifica --dizionario

        db_item.hsp     2.580 non tradotte -> **2.524**   (0 da ritradurre)

    python scratchpad/_97-quanto-resta.py

        TOTALE          2.690 / 110 / 2.580   ->   **2.634 / 110 / 2.524**

    python scratchpad/perimetro.py            perimetro **90%**, totale **93%**
                                              (26.199 nel perimetro, erano 26.143)

    python -m strumenti.applica               27.517 -> **27.650**
                                              = 27.517 + 133 esatte
    python -m pytest strumenti/tests -q       775 -> 792 -> **794**

    rinviate.jsonl                            113, invariato
    toppe.jsonl                               1027, invariato — e 1027 agganciate

⚠️⚠️ **Le sostituzioni salgono di 133 e le firme di 56, e non è una discrepanza:**
`estrai --da-tradurre` àncora una firma alla **prima** occorrenza, e le
descrizioni di questa categoria si ripetono parola per parola su tutta la
famiglia. Una resa scritta una volta arriva a schermo su tutte le sue righe. È
il rapporto — 133 su 56, cioè **2,4 righe per firma** — che rende questo file
meno caro di quel che il conteggio delle righe fa credere.

### Il tetto secco, misurato invece che sperato

    python scratchpad/_107-descrizioni-item.py

        indice 3: vive 1.319, **rese 133**
        oltre il tetto — inglese: 110   italiano: **0**
        ⚠️ INTRODOTTE DALL'ITALIANO: **0**   (è il cancello)

⭐ E il numero che il cancello non dice: la resa più lunga del lotto misura
**65 caratteri degradati su 69**, quindi il margine è di **quattro**. Sono i
semi — «Un seme che diventa un albero di artefatti. Si usa (usa e getta).» — e
sono la famiglia da tenere d'occhio nei lotti dopo, non i cibi.
`scratchpad/lotti-108/_margine.py` lo rimisura in un comando.

ⓘ **14 rese su 56 sono più lunghe del loro inglese**, e nessuna sfora: il
fattore italiano/inglese di ~1,0 misurato dalla 107ª regge anche qui.

### Gli strumenti toccati

| file | che cosa |
|---|---|
| `scratchpad/assembla-lotto.py` | il modo `--righe`: la zona per **insieme** di righe invece che per intervallo, riscrivendo due righe del modello unico. Più `--lavoro`, `--fase`, `--hsp` |
| `strumenti/verifica.py` | `oggetto` non basta più a riconoscere un nome: lo riconoscono `plurale`, `genere`, `array`, che solo un nome ha |
| `strumenti/tests/test_verifica.py` | +2 prove: una descrizione col solo `oggetto` non è un nome; un nome senza `oggetto` resta rotto |
| `scratchpad/_108-accento-decomposto.py` | la rete 5 portata fuori dal lotto e misurata sul dizionario intero |
| `scratchpad/lotti-108/` | `testa001.py`, `rese001.py`, `righe001.py` e le due misure usa-e-getta |

### Che cosa resta di questa categoria

Le altre tre caselle di `FILTER_ITEM_FOOD` — gli indici 0, 1 e 2, il **corpo**
del pannello — non sono in questo lotto e sono un'altra cosa: passano
dall'impaginatore, sono prosa vera e la loro mediana è di 205 caratteri contro i
48 dell'indice 3.

### I lotti 002 e 003 — le pozioni e le pergamene, 2026-08-27

Due lotti nella stessa sessione, `FILTER_ITEM_POTION` (77 righe, **65 firme**) e
`FILTER_ITEM_SCROLL` (66 righe, **65 firme**). Il conteggio in chiusura:

    python -m strumenti.verifica --dizionario

        db_item.hsp     2.524 non tradotte -> **2.394**

    python scratchpad/_97-quanto-resta.py

        TOTALE          2.634 / 110 / 2.524   ->   **2.504 / 110 / 2.394**

    python -m strumenti.applica               27.650 -> **27.793**
                                              = 27.650 + 143 esatte
    python scratchpad/perimetro.py            perimetro **90%** (26.329)
    python scratchpad/_107-descrizioni-item.py
        indice 3: vive 1.319, **rese 276**;  introdotte dall'italiano **0**

⭐⭐ **`_margine.py` ha fatto il suo lavoro, e per questo esiste.** Al lotto 003
ha fermato **quattro rese a 73 caratteri** — gli atti dei mezzi di terra, «Si
può rileggere quante volte si vuole» — prima della reimportazione. Il cancello
della rete le avrebbe prese lo stesso, ma **dopo** che stavano nel dizionario;
qui sono state riscritte prima («Si può rileggere sempre», 58 caratteri).

⚠️ **Il margine si stringe di lotto in lotto, ed è il numero da guardare:**

    001  cibi       la più lunga 65 su 69   margine 4   (i semi)
    002  pozioni    la più lunga 60 su 69   margine 9
    003  pergamene  la più lunga 67 su 69   margine 2   (la pergamena della fuga)

ⓘ **E le rese sono più corte del loro inglese quasi sempre**: 0 su 65 lo
superano nel lotto 003, 11 su 65 nel 002, 14 su 56 nel 001. L'inglese
dell'indice 3 è prolisso — «It is a scroll that when read, …» — e l'italiano che
segue il giapponese guadagna spazio invece di perderne.

### Gli strumenti toccati dai lotti 002 e 003

| file | che cosa |
|---|---|
| `scratchpad/lotti-108/_margine.py` | il file da misurare si passa come **argomento**: la prima versione lo aveva fisso e al secondo lotto è stato riscritto con `sed`, cioè un attimo prima di misurare il lotto sbagliato credendo di misurare quello giusto. Ed esce con 1 se il tetto è sfondato |
| `scratchpad/lotti-108/_id.py` | il numero di un `ITEM_ID` letto da `defines/mod.hsp`, per la lista di passi: `spawn_item` vuole il numero, e una lista si esegue alla cieca |

## `db_item.hsp`, cinque lotti dell'indice 3 — 2026-08-27, centodecima

    db_item.hsp   indice 3, il rapporto di identificazione — CINQUE lotti
    -------------------------------------------------------------------------
    006  FILTER_JUNK          81 firme ->  97 righe   margine 3
    007  FILTER_ORE           21 firme ->  33 righe   margine 5
    008  FILTER_ITEM_BOOK     20 firme ->  23 righe   margine 3
    009  FILTER_ITEM_ROD      30 firme ->  32 righe   margine 4
    010  FILTER_CONTAINER     21 firme ->  22 righe   margine 4
    -------------------------------------------------------------------------
    **173 firme rese**, che coprono **207 righe** del sorgente
    applica 28.210 -> **28.417**   (+207 esatte)
    non tradotte di db_item.hsp: 2.033 -> **1.860**   (-173 esatte)
    indice 3: rese 693 -> **900**   vive 1.319
    tetto secco: introdotte dall'italiano **0** — il cancello e' verde
    rinviate: nessuna   toppe: nessuna   test: **794**, invariato
    strumenti toccati: 2 (`_monta.py` prende la cartella, `_coerenza.py` salta
                         il giapponese vuoto)
    build: SI', **10:00 del 27/08**
    -------------------------------------------------------------------------

Le rese e le decisioni stanno in `glossario.md`, sezione della 110ª. Qui restano
le due cose che riguardano il **modo di lavorare**.

### ⚠️⚠️ `_coerenza.py` diceva «una divergenza» e non ne aveva vista nessuna

Il lotto 006 contiene `:89761`, l'esca, la cui `description(3)` giapponese è
**vuota**. `_coerenza.py` raggruppa le rese per giapponese, e la stringa vuota
ha raccolto **trenta voci** del dizionario — segnaposti, concatenazioni HSP,
battute — che di comune hanno soltanto il non avere una fonte giapponese. Rese
diverse, ovviamente: il cancello si è acceso e diceva il falso.

⚠️ **Non è un falso positivo qualunque, è un raggruppamento che non vuol dire
niente.** Riparato saltando le voci col giapponese (o l'inglese) vuoto.
✅ **Controprova sul lotto 005 della 109ª**: 0 divergenze su **7** gruppi
giudicati e 3 divergenze di inglese, cioè esattamente i valori con cui la 109ª
si era chiusa. La riparazione non ha spento niente di vero.

ⓘ E lo zero del lotto 006 resta **0 su 0 gruppi giudicati**: nessuno degli 81
giapponesi compare altrove nel dizionario. È la ragione per cui quel numero si
stampa accanto allo zero — senza, sembrerebbe un risultato.

### ⚠️ `_monta.py` cercava i suoi file accanto a sé

Fino alla 109ª i tre file di un lotto (`_traduzioniNNN.py`, `chiaviNNN.txt`,
`reseNNN.py`) stavano nella cartella dello script. La 110ª li ha messi in
`scratchpad/lotti-110/`, e lo script moriva dicendo che `_traduzioni006.py` non
c'era. La cartella è diventata il **secondo argomento**, che se manca è quella
dello script:

    python scratchpad/lotti-109/_monta.py 006 scratchpad/lotti-110

⚠️ La strada breve era **copiare lo script** nella cartella nuova, ed è la
strada che la 108ª ha pagato caro: `modello-rete4.py` è della 43ª e la sua rete
6 non sapeva del commento `//` della 100ª, perché nessuno aggiorna quattro copie.
✅ Controprova: rilanciato il vecchio comando su `005`, `git status` è rimasto
vuoto — il file prodotto è byte per byte quello di prima.

### ⚠️ E la trappola dell'heredoc vuoto ha colpito una sesta volta

Un `python - <<'PY'` con dentro **niente**, per un comando che non serviva a
nulla: due minuti di terminale bloccato fino al timeout. È la stessa forma che
la 104ª e la 105ª hanno già pagato. La regola non è «attenzione ai backslash»:
è che un file si scrive con lo strumento di scrittura, e uno script di dieci
righe si mette nello scratchpad.

### ⓘ Il margine, lotto per lotto — e dove si è dovuto stringere

    006  scarti        la più lunga 66 su 69   margine 3
    007  minerali      la più lunga 64 su 69   margine 5
    008  libri         la più lunga 66 su 69   margine 3
    009  bacchette     la più lunga 65 su 69   margine 4
    010  contenitori   la più lunga 65 su 69   margine 4

⚠️ **Due lotti sono passati per il misuratore prima di andare bene**, e senza di
lui sarebbero usciti dal riquadro senza che nessuno lo vedesse:

- il **009** (bacchette) misurava **margine 0**: la testa «Una bacchetta che,
  agitata, » costa 28 caratteri, e cinque righe ci arrivavano contro. Accorciato
  il *fatto*, non la testa, così la famiglia resta una;
- il **008** (libri) misurava **margine 1**, e la riparazione ha cambiato la
  regola: vedi `glossario.md`, il modale che cade per tenere insieme la famiglia.

### ⚠️⚠️ La lista di collaudo della 109ª aveva DUE passi muti, e il codice lo dice

La 109ª chiudeva scrivendo che il rapporto compare da sé: *«uno creato con
`spawn_item` nasce a zero e diventa FULL da solo dopo qualche turno nello
zaino»*. Per **queste cinque categorie non succede mai.**

`item.hsp:2086`, `*item_senseQuality`, è la rete che identifica passivamente
quel che si porta addosso. Alle righe 2096-2100:

    if ( sensep > 5 | cdata(CDATA_ROW_ACT, CHARA_PLAYER) == ACTION_NONE ) {
        if ( refitem(..., DBSPEC_TYPE) >= FILTER_ITEM_MIN ) { continue }
    }

`ACTION_NONE` vale **0**, ed è quel che `CDATA_ROW_ACT` vale quando il
giocatore **non sta svolgendo un lavoro** — cioè quasi sempre. E
`FILTER_ITEM_MIN` vale **50.000**, mentre `FILTER_JUNK` vale 64.000 e
`FILTER_ORE` 77.000: tutte e cinque le categorie della 110ª stanno sopra la
soglia. Il ramo le **salta**, in silenzio, per sempre.

⚠️ Chi avesse eseguito quella lista avrebbe aspettato dei turni davanti a uno
schermo che non cambia, e concluso «non è tradotto».

**La via che funziona** è la pergamena di identificazione **maggiore**,
`ITEM_ID_SCROLL_GREATER_IDENTIFY` = **362**: `db_item.hsp:107040` le dà
`efp = 2000`, e `item_func.hsp:640-648` porta a `ITEM_KNOWN_FULL` qualunque
oggetto quando la potenza basta — e per gli oggetti sopra `FILTER_ITEM_MIN` ci
arriva comunque, per la riga 646.

### ⚠️ E il tasto dell'inventario di questa installazione è `X`, non `i`

`config.txt` del gioco dice `key_inventory. "X"` e `key_interact. "i"`: la lista
della 109ª diceva «`i` per l'inventario», che qui apre l'**interazione**. Gli
altri tre sono giusti — `g` raccoglie, `r` legge, e **`x` sulla voce
evidenziata dell'inventario** è `key_identify`, che chiama `*com_identify`
(`command.hsp:15787`).

💡 I tasti si leggono in `elonaplus2.31\config.txt`, non nel sorgente: il
sorgente ha i **valori di partenza**, e questa installazione li ha cambiati.

## `db_item.hsp`, altri tre lotti dell'indice 3 — 2026-08-27, centodecima (seguito)

    db_item.hsp   indice 3 — le TRE categorie piu' grandi rimaste
    -------------------------------------------------------------------------
    011  FILTER_ITEM_SPELLBOOK    82 firme ->  82 righe   margine 3
    012  FILTER_WEAPON           105 firme -> 105 righe   margine 3
    013  FILTER_RANGE             55 firme ->  56 righe   margine 7
    -------------------------------------------------------------------------
    **242 firme rese**, che coprono **243 righe** del sorgente
    applica 28.417 -> **28.660**   (+243 esatte)
    -------------------------------------------------------------------------
    IL TOTALE DELLA 110a, otto lotti:
    **415 firme**, **450 righe**
    applica 28.210 -> **28.660**   (+450 esatte)
    non tradotte di db_item.hsp: 2.033 -> **1.618**   (-415 esatte)
    indice 3: rese 693 -> **1.143**   su 1.319 vive
    ⚠️ scritto **1.130** in chiusura della 110a e riparato in apertura della
       111a: `_107-descrizioni-item` conta **righe**, non firme (a meta' 110a
       registrava 693 -> 900, e 900-693 = 207 = le righe dei primi cinque
       lotti). 693 + 450 = **1.143**, la stessa cifra di `applica`.
    perimetro 26.690 -> **27.105**   dizionario 23.951 -> **24.366**
    tetto secco: introdotte dall'italiano **0** — il cancello e' verde
    rinviate: nessuna   toppe: nessuna   test: **794**, invariato
    build: SI', **14:28 del 27/08**
    -------------------------------------------------------------------------

Le decisioni stanno in `glossario.md`, sezione della 110ª. Qui i numeri e le
tre cose che riguardano il **modo di lavorare**.

### ⭐ Il conto che dice quanto e' costato ogni lotto

    lotto  categoria      firme  righe  righe/firme
    ------------------------------------------------
    007    minerali          21     33     1,57   ⭐ le dodici gemme
    006    scarti            81     97     1,20
    008    libri             20     23     1,15
    009    bacchette         30     32     1,07
    010    contenitori       21     22     1,05
    013    a distanza        55     56     1,02
    011    grimori           82     82     1,00
    012    armi             105    105     1,00   ⚠️ nessun doppione

⭐ **Il rapporto righe/firme e' il prezzo della categoria**, e si legge **prima**
di aprirla con `_107-lotti-per-categoria.py --indice 3`. Chi deve scegliere il
prossimo lotto guardi quella colonna: le gemme hanno reso 33 righe con 21 rese,
le armi 105 con 105.

⚠️ **Ma non e' il solo criterio.** I grimori stanno a 1,00 e sono costati meno
delle armi a parita' di righe, perche' **36 righe su 82 sono una griglia** — tre
classi per dodici elementi — e una griglia si scrive una volta sola. Il rapporto
righe/firme non vede le famiglie **dentro** le firme: le vede solo l'elenco.

### ⚠️ Il margine si e' dovuto stringere DUE volte su tre

    011  grimori    margine 1 al primo giro -> 3   (accorciati 4 fatti)
    012  armi       margine 3 subito
    013  a distanza margine 7 subito

Nei grimori la testa «Un libro per » costa 13 caratteri e la coda «Si può
leggere.» ne costa 17: restano 39 per il fatto, e quattro righe ci sono arrivate
contro. Accorciato il **fatto**, mai la formula.

💡 **La regola che ne esce**: quando una categoria ha una testa fissa e una coda
fissa, il budget vero non e' 69 — e' 69 meno la somma delle due. Conviene
misurarlo **prima** di scrivere le rese, non dopo.

### ⚠️ E l'heredoc ha colpito una settima volta, in un modo nuovo

Un `cat >> glossario.md <<'FINE'` con dentro centosessanta righe di Markdown e'
morto con «unexpected EOF while looking for matching `''`». Non ha scritto
niente — l'ho controllato con `git status` prima di rifare — ma il fallimento e'
**silenzioso sul contenuto**: se avesse scritto meta' file non lo avrei saputo
dal messaggio.

La regola del progetto vale anche per il testo lungo, e stavolta e' costato un
comando invece di due minuti: **il file si scrive con lo strumento di scrittura**
e poi si innesta con tre righe di Python che verificano la marca
(`assert base.count(marca) == 1`).

## ⭐⭐⭐ `db_item.hsp`, l'INDICE 3 SI CHIUDE — 2026-08-27, centoundicesima

    db_item.hsp   indice 3, il rapporto di identificazione — DODICI lotti
    -------------------------------------------------------------------------
    014  FILTER_SHIELD             23 firme ->  23 righe   margine 7
    015  FILTER_ARMOR              20 firme ->  20 righe   margine 15
    016  FILTER_CARGO_TRADE        18 firme ->  19 righe   margine 36
    017  FILTER_HELM               15 firme ->  15 righe   margine 15
    018  FILTER_ACCESSORY_AMULET   13 firme ->  13 righe   margine 2
    019  FILTER_ENVIRONMENT         9 firme ->  12 righe   margine 27
    020  FILTER_ACCESSORY_RING     11 firme ->  11 righe   margine 15
    021  FILTER_CLOAK               9 firme ->  10 righe   margine 22
    022  FILTER_GLOVES             10 firme ->  10 righe   margine 3
    023  FILTER_GIRDLE              9 firme ->   9 righe   margine 10
    024  FILTER_BOOTS               9 firme ->   9 righe   margine 15
    025  la CODA (nove categorie)  23 firme ->  25 righe   margine 8
    -------------------------------------------------------------------------
    **169 firme rese**, che coprono **176 righe** del sorgente
    applica 28.660 -> **28.836**   (+176 esatte)
    non tradotte di db_item.hsp: 1.618 -> **1.449**   (-169 esatte)
    ⭐⭐⭐ indice 3: rese 1.143 -> **1.319 su 1.319 vive — CHIUSO**
    perimetro 27.105 -> **27.274**   dizionario 24.366 -> **24.535**
    tetto secco: introdotte dall'italiano **0** — il cancello e' verde
    rinviate: nessuna   toppe: nessuna   test: **794**, invariato
    strumenti nuovi: 2 (`lotti-111/_cerca.py`, `lotti-111/_coda.py`)
    build: SI', **15:25 del 27/08**
    -------------------------------------------------------------------------

Le decisioni stanno in `decisioni.md`, sezione della 111ª. Qui i numeri e le
quattro cose che riguardano il **modo di lavorare**.

### ⭐⭐⭐ La famiglia degli otto doni divini, e perche' nessuna rete la vedeva

「身に着けると変形して〜になる」 e' la stessa riga otto volte, in otto categorie
diverse, con una parola cambiata. Le otto righe non si incontrano mai — ne' nel
gioco, ne' in un lotto, ne' in una rete:

    :57965  手枷      -> in manette              scudi      (lotto 014)
    :75986  拘束具    -> in una gabbia           armature   (lotto 015)
    :76184  頭につける輪 -> in un cerchietto da testa  elmi  (lotto 017)
    :76250  首輪      -> in un collare           amuleti    (lotto 018)
    :75584  指輪      -> in un anello            anelli     (lotto 020)
    :75650  腕装備    -> in un bracciale         guanti     (lotto 022)
    :76052  腰当      -> in una cintura          cinture    (lotto 023)
    :76118  足枷      -> in ceppi                calzature  (lotto 024)

⚠️⚠️ **Il lotto 014 e' stato rifatto per colpa del lotto 024.** 手枷 (la mano) e
足枷 (il piede) sono la stessa parola con un'altra parte del corpo; il 014 aveva
scritto «ceppi» per il primo, che lasciava il secondo senza parola — e l'oggetto
del secondo si chiama gia' **«Ceppo della Terra»**. Riscritto: 手枷 **manette**,
足枷 **ceppi**.

💡 **Nessuna rete poteva vederlo, e non per una svista.** Le due righe stanno in
categorie diverse, hanno giapponesi diversi e inglesi diversi, e ognuna per
conto suo era giusta. Si vede solo scrivendo la famiglia intera in un colpo, e
la famiglia si vede solo dal **giapponese**: l'inglese la appiattisce tutta su
«It is a godly gift that when worn, transforms into ...».
⚠️ E il rifacimento e' passato per la catena — `_monta` -> `assembla` -> lotto ->
`reimporta` — **non** per una modifica a mano del dizionario.

### ⭐ Il rapporto righe/firme di dodici lotti, e cosa NON dice

    lotto  categoria           firme  righe  righe/firme
    -----------------------------------------------------
    019    alberi                  9     12     1,33  ⭐ tre firme per cinque righe
    016    merci da commercio     18     19     1,06
    021    mantelli                9     10     1,11
    025    la coda                23     25     1,09
    014/015/017/018/020/022/023/024        1,00

⚠️ **Il rapporto non ha previsto niente, stavolta.** Gli alberi stanno a 1,33 e
sono costati **dieci minuti**; gli amuleti stanno a 1,00 e sono costati un'ora,
perche' ognuna delle tredici righe voleva un termine cercato altrove. Il costo
vero non e' nelle righe: e' in **quante parole nuove** la categoria porta.

💡 La misura che avrebbe funzionato e' un'altra: **quanti termini del giapponese
non sono gia' nel dizionario**. Vale la pena scriverla, se un giorno tocca un
altro indice.

### ⭐⭐ Le reti hanno bocciato due lotti, e tutt'e due le volte avevano ragione

- **`:81539`, «degli dèi»** — la rete dell'accento: la degradazione a CP932 fa
  `de'i`, l'apostrofo **dentro** la parola, e a schermo non si legge. Cambiata
  la parola («la parola divina»), non tolto l'accento.
- **`:75717`, «zekki» fra virgolette basse** — la rete dei caratteri
  sconosciuti: CP932 **cancella** « e ». La resa sarebbe arrivata a schermo con
  la parola nuda comunque, e nessuno lo avrebbe saputo.

⚠️ `reimporta` e' tutto-o-niente: tutt'e due le volte **niente** e' stato
scritto nel dizionario, ed e' esattamente quel che deve succedere.

### ⚠️ E l'heredoc ha colpito un'ottava e una nona volta, nello stesso modo

Due `python - <<'PY'` **vuoti**, due minuti di terminale bloccato ciascuno, in
una sessione che aveva letto la regola in apertura. Tutt'e due erano comandi
che non servivano a niente — un controllo di cortesia dopo una scrittura andata
a buon fine.

💡 **La forma nuova della regola**: non e' «i file si scrivono con lo
strumento», che ormai si fa. E' che **`python -` e `cat <<` non si scrivono
proprio**, nemmeno per un no-op: se il corpo e' vuoto la shell aspetta per
sempre, e un comando che non serve costa quanto uno che serve.

## `db_item.hsp`, il CORPO: un fronte misurato e una famiglia decisa — 2026-08-27, centododicesima

**Nessuna resa nuova.** La sessione ha fatto tre cose: riparato una catena
rossa, capito e misurato il fronte del corpo (indici 0-2), e deciso la famiglia
delle 224 righe-fonte. `applica` resta a **28.836**, `db_item` a **1.449** non
tradotte, il debito di collaudo a **7.719**.

### L'apertura era rossa, e l'aveva rotta il commit dei documenti

Sedici test falliti fra `test_verifica`, `test_reimporta` e
`test_dati_reimporta`. L'ultimo commit della 111a aggiungeva a `invariati.md`
la sezione «Termini coniati dentro una DESCRIZIONE», e `_e_invariante()` non ha
un default: una sezione che porta valori e non è classificata alza
`ValueError`. Riparato mettendo il prefisso in `_SEZIONI_INVARIANTI`, e
correggendo l'intestazione della tabella nuova — diceva `| termine | motivo |`
mentre il lettore salta l'intestazione solo se la prima cella è `valore`,
quindi «termine» sarebbe finito **dentro** l'insieme degli invariati.

⚠️ La chiusura della 111a aveva scritto «pytest 794, invariato»: i test erano
stati lanciati **prima** del commit dei documenti. La catena verde era misurata
su un albero diverso da quello spinto.

### Il corpo, misurato

    righe-fonte (marcate da `#`)      1.509 su 1.513 descrizioni
    titoli distinti, per inglese        224
    titoli distinti, per giapponese     200 + 19 righe mute
    i 20 più frequenti coprono           74% delle righe
    tetto della riga-fonte               66 caratteri degradati
    la resa italiana più lunga           55  (margine 11)
    trattini orfani veri                  1  (di monte, `:129299`)

Le quattro cose che possono rompersi, e quali l'italiano raggiunge davvero:

| difetto | si accende a | raggiungibile? |
|---|---|---|
| la fonte smette di esserlo | titolo di **67** caratteri | **sì** |
| trattino orfano | **due** `\n` in coda | no (uno non basta) |
| coda persa | 911 caratteri con parole da 56 | **no** — la parola media è 4,6 |
| parola spezzata | una parola di **17** caratteri | **sì** — «dell'equipaggiamento» ne fa 20 |

💡 Il risultato più utile è negativo: **la geometria non è il problema.** Il
taglio a 70 sta dentro un budget di 77, il pannello sfoglia invece di tagliare,
e la coda non si perde. Restano due numeri veri — il tetto dei 66 e la parola
spezzata — e sono gli unici da guardare quando i lotti cominceranno.

### Tre numeri smentiti da uno schermo

| dicevo | dice lo schermo |
|---|---|
| budget 69 per le righe impaginate | **77** (font 11, non 12) |
| 11 trattini orfani | **1** (`split` ≠ `noteinfo`) |
| la fonte più lunga forse sfora | finisce a **584 px su 600** |

Nessuna delle tre si vedeva rileggendo il sorgente.

### Strumenti nuovi: sei, più una tabella

`_112-corpo-descrizioni.py` (anatomia e quattro prove al contrario),
`_112-dossier-fonti.py`, `_112-nomi-fonti.py` (cerca i nomi **per inglese**,
il verso che mancava), `_112-verifica-fonti.py` (cancello, esce 0/1),
`_112-genera-glossario.py`, `_112-innesta-glossario.py`, e la tabella
eseguibile `lotti-112/titoli_fonte.py` con 234 voci. `glossario.md` +268 righe.

⚠️ E due strumenti vecchi corretti: `_102-carta-conoscenza.py` (il budget, e la
separazione fra i due font) e `_107-descrizioni-item.py` (`segmenti_hsp()` e
`BUDGET_INTERO`).

## `db_item.hsp`, il CORPO: i primi tre lotti di prosa — 2026-08-31, centotredicesima

Aperta con la catena **tutta verde**, ventidue verifiche su ventidue ai valori
della 112ª: albero pulito, `log.md` del vault aggiornato, eseguibile in gioco
delle 15:25 del 27/08. È la prima apertura pulita dopo il guasto della 112ª.

### Tre lotti, 138 rese, 187 righe del sorgente

    lotto  categoria           indici   righe  righe del sorgente coperte
    ------------------------------------------------------------------
    026    FILTER_ITEM_FOOD    0,1,2       50   99
    027    FILTER_FURNITURE    0,2         42   42
    028    FILTER_FURNITURE    0           46   46
                                          ---  ---
                                          138  187

Il corpo (indici 0-2) passa da **0 a 187 righe rese** su 1.513 vive.
`verifica --dizionario` su `db_item.hsp` scende da **1.449 a 1.311** non
tradotte; il perimetro sale da 27.274 a **27.412** (90%), il totale a 30.345
(94%); `applica` da 28.836 a **29.023**, cioè +187 esatte.

⚠️ **Il moltiplicatore 50 → 99 sono quattro firme.** Le righe generiche
dell'indice 2 del cibo — «A type of vegetable/fruit/seafood/nut that restores
satiety...» — tornano **18, 18, 15 e 2** volte in tutto il file: 53 righe da
quattro rese. Nel mobilio il rapporto è 1 a 1.

### Il cancello del corpo

    _107-descrizioni-item   corpo (0-2): 1.513 vive, 187 rese
                            coda persa      : inglese 0   italiano 0
                            righe spezzate  : inglese 2   italiano 0
                            righe oltre i 77: inglese 0   italiano 0
                            ⚠️ INTRODOTTE DALL'ITALIANO: 0 / 0 / 0

Rimisurato dopo ogni lotto, e verde tutte e tre le volte.

### Gli strumenti

Nuovi: `scratchpad/_113-fonti-gia-rese.py` (referto, non cancello),
`scratchpad/lotti-113/_corpo.py` (lo scheletro del corpo, tre indici uniti),
`scratchpad/lotti-113/_code.py` (la coda di ogni riga, assegnata dal
giapponese).

⚠️ **Corretto `scratchpad/lotti-109/_monta.py`**, che avrebbe corrotto ogni resa
del corpo in silenzio: la resa entrava grezza fra virgolette doppie e il
backslash di `\n#~fonte~` tornava indietro come un a capo vero. Ora c'è l'escape
e un **giro di ritorno** che rilegge il file scritto e lo confronta con le rese
di partenza.

⚠️ **Corretta la tabella `lotti-112/titoli_fonte.py` in venti punti**: dieci
titoli che contraddicevano un nome già a schermo e dieci che portavano
l'apostrofo al posto dell'accento. `glossario.md` rigenerato e reinnestato,
2.343 righe prima e dopo.

⚠️ **Corretto un numero della 112ª**: la parola si spezza a **14** caratteri, non
a 17. La finestra di rinculo è 15 e il 17 era la misura di una parola.

### Una parola nuova in `invariati.md`

`zenzai` — il dolce giapponese citato *dentro* la descrizione dell'osiruko
(`db_item.hsp:56934`). Non è il nome di un oggetto: è un termine che la prosa
porta, e il corpo delle descrizioni ne porterà altri. È la prima parola coniata
dal corpo.

### Quel che resta

    164  FILTER_FURNITURE (indice 0)   +9 dell'indice 2
    166  FILTER_ITEM_TOOL
    105  FILTER_WEAPON
     96  FILTER_JUNK
     82  FILTER_ITEM_SPELLBOOK
     ... e una coda di venti categorie minori

⚠️ Debito di collaudo: **7.857** rese mai viste a schermo. La lista di passi è
stata data a metà sessione, con cinque identificativi letti dal sorgente e tutti
verificati a `IDENTIFY_LEVEL = 0`.

---

## 122ª — Nove categorie del corpo, e il fronte scende a 28 righe

Nove lotti, **111 rese**, nove categorie chiuse. Le categorie chiuse del corpo
passano da quindici a **ventiquattro**.

    061  FILTER_CARGO_TRADE       19    le merci da commercio
    062  FILTER_ENVIRONMENT       13    gli alberi
    063  FILTER_HELM              16    gli elmi e i cappelli
    064  FILTER_ACCESSORY_AMULET  14    le collane
    065  FILTER_ACCESSORY_RING    11    gli anelli
    066  FILTER_GLOVES            10    i guanti
    067  FILTER_CLOAK             10    i mantelli e le ali
    068  FILTER_GIRDLE             9    le cinture
    069  FILTER_BOOTS              9    le scarpe

### Il corpo, misurato

    _107-descrizioni-item   corpo (0-2): 1.513 vive, 1.485 rese
                            introdotte dall'italiano: 0 / 0 / 0   (il cancello)
                            indice 3: 1.319 su 1.319 — CHIUSO
    _114-corpo-da-fare      28 su 1.449 firme, di cui 1 rinviata
    verifica --dizionario   db_item.hsp: 0 da ritradurre, 28 non tradotte
    _97-quanto-resta        138 / 111 / 27
    applica                 30.321 sostituzioni   (era 30.210: +111)
    perimetro.py            perimetro 90% (28.695), totale 94% (31.628)

⭐ **Nove previsioni di `applica`, nove esatte.** `_previsione.py` ha detto
«nessuna gemella» nove volte su nove, e nove volte il conteggio è salito
esattamente del numero di rese.

### Quel che resta

    7  FILTER_REMAINS               2  FILTER_FURNITURE_ALTAR
    6  FILTER_ENVIRONMENT_SEABED    1  FILTER_PLATINUM
    5  FILTER_AMMO                  1  FILTER_GOLD
    4  FILTER_FURNITURE_WELL        1  FILTER_CARGO_FOOD

    + 1 in FILTER_ITEM_POTION, che è la RINVIATA e non è lavoro

**Ventisette righe vere, e il corpo di `db_item.hsp` si chiude.**
⚠️ Il lotto **070** su `FILTER_REMAINS` è già aperto — righe, dossier, code e
referto delle sorelle sono sul disco, le rese no.

### Due strumenti nuovi

    scratchpad/_122-inglese-doppio-item.py    l'inglese di un ALTRO oggetto
    scratchpad/_122-sorelle-per-frase.py      la frase sorella su tutto il file

Tutt'e due hanno `--prova`, e la prova del secondo ha trovato un difetto nel
secondo al primo giro. Stanno per esteso in `decisioni.md`.

### Il debito di collaudo

⚠️⚠️ **Nessuna delle 111 rese è stata vista a schermo.** La lista di passi data
a metà sessione copre i lotti **061, 062 e 063** — venti oggetti con
`spawn_item`, la pergamena **362**, e per ognuno che cosa guardare. Per i lotti
064-069 non è mai stata scritta: alla domanda «vado avanti o chiudo?» l'utente
ha risposto «vai avanti».

Il debito sale da 9.029 a **9.140** rese mai viste a schermo.

ⓘ **Costruito, misurato dagli strumenti, provato al contrario e visto a schermo
sono quattro stati distinti**, e qui il quarto manca. Tre scelte forti di questa
sessione — i cinque «Non si può usare» del 061, la forma impersonale del 069, i
due nomi alieni trascritti del 064 — sono **giudicate solo da me**.

---

# La centoventitreesima sessione — 2026-09-01

## Il corpo di `db_item.hsp` si chiude

Otto lotti, **32 rese**, **otto categorie** chiuse — dalla venticinquesima alla
trentaduesima:

    070  FILTER_REMAINS               7 rese   i resti, e i due pezzi da collezione
    071  FILTER_ENVIRONMENT_SEABED    6 rese   le alghe
    072  FILTER_AMMO                  5 rese   le munizioni
    073  FILTER_FURNITURE_WELL        4 rese   i pozzi
    074  FILTER_FURNITURE_ALTAR       2 rese   gli altari
    075  FILTER_PLATINUM              1 resa   la moneta di platino
    076  FILTER_GOLD                  1 resa   la moneta d'oro
    077  FILTER_CARGO_FOOD            1 resa   il cibo da viaggio

Il corpo passa da **1.485 a 1.512 rese su 1.513**, e l'unica rimasta è la
**rinviata** `:129299`, che non ha un testo in nessuna delle due lingue.
`_114-corpo-da-fare` legge **TOTALE da fare 1 su 1.449 vive, di cui rinviate 1**:
zero lavoro.

⭐ Otto previsioni di `applica`, **otto esatte**: nessuna gemella in tutta la
serie.

## Il fronte nuovo: 355 firme che nessun contatore mostrava

Chiuso il corpo, **ogni** file con un dizionario dice `⭐ CHIUSO` e
`_97-quanto-resta` legge «TOTALE da fare 0». Ma `perimetro.py` diceva **90%**, e
il motivo è che `_97-quanto-resta` guarda **solo i file che hanno un
dizionario**.

`scratchpad/_123-file-senza-dizionario.py`, nuovo, fa la domanda dal sorgente:
**355 firme in 12 file mai estratti**. Dopo i materiali sono **238 in 11**.

    firme  lang()  file
      118     176  txtadv.hsp          <- il prossimo per peso
       27      39  net.hsp
       27      31  custom_itemenchantment.hsp
       21      26  quest.hsp
       18      22  material.hsp
       15      17  etc.hsp
        6       6  map_rand.hsp
        2       3  scene.hsp
        2       2  custom_nefiatypes.hsp
        1       4  custom_pet.hsp
        1       3  custom_dmgpop.hsp

## Il primo dei dodici: i 59 materiali

`dizionario/material_data.hsp.jsonl` esiste, **118 rese** (59 nomi e 59
descrizioni, 117 firme distinte perché due descrizioni sono identiche). Il
perimetro passa da **90% a 91%**.

- **27 nomi su 59 erano già decisi** in `glossario.md`, con i numeri di riga.
  Tre delle rese scritte prima di leggerla erano sbagliate.
- **13 rese sforavano** il budget di larghezza del pannello (2 nomi e 11
  descrizioni, la peggiore a 41 su 32). Riscritte.
- Una **toppa** su `material.hsp:120` toglie il suffisso inglese al plurale e
  porta la forma «Materiale ricevuto: pietruzza (3)», già decisa e già in gioco
  su 54 righe altrove. Le toppe passano da **1027 a 1028**.

## Gli strumenti nuovi

    scratchpad/_123-file-senza-dizionario.py   i file con lang() e senza dizionario
    scratchpad/_123-rese-materiali.py          le 118 rese, col referto dei buchi
    scratchpad/_123-toppa-materiali.py         la toppa, con la prova al contrario
                                               sull'ancora commentata di :55
    scratchpad/_123-larghezze-materiali.py     il cancello di larghezza del pannello

## I numeri, a fine sessione

    pytest                       794 passed, 6 skipped   (dopo i documenti)
    prova_identita               72/72 e 30.905          invariato
    applica                      30.321 -> 30.466
    toppe                        1027 -> 1028, agganciate 1028 su 1028
    perimetro                    90% -> 91% (28.722); totale 94% (31.655)
    _123-file-senza-dizionario   355 in 12 -> 238 in 11
    _114-corpo-da-fare           28 -> 1 (di cui rinviate 1), 32 categorie chiuse
    _107-descrizioni-item        corpo 1.485 -> 1.512 su 1.513; cancello 0/0/0
    _123-larghezze-materiali     nomi fuori 0, descrizioni fuori 0
                                 (una eccezione dichiarata)

## Il debito di collaudo

⚠️⚠️ **Nessuna delle 150 rese è stata vista a schermo** — 32 dei lotti e 118 dei
materiali. Il debito sale da 9.140 a **9.290**.

⭐ **Ma la lista di collaudo dei lotti 070-077 c'è ed è verificata**, e sta in
`RIPRESA-sessione.md`: gli identificativi cercati nel sorgente, e le premesse
rimisurate sul caso di oggi invece che ereditate. Due passi della lista vecchia
qui sarebbero stati **muti** — oro e platino non entrano nell'inventario
(`action.hsp:923` li assorbe nel borsellino), e la lista da terra si apre solo
se sulla casella c'è più di un oggetto (`command.hsp:13004`).

⚠️ **La lista dei materiali non si può scrivere**: il pannello elenca solo i
materiali con quantità diversa da zero (`material.hsp:406`) e **non esiste
nessun comando wizard che dia materiali** — l'elenco di `system.hsp:4700`-`5000`
non ne ha. L'unica strada è la raccolta vera ai punti di campionamento.

ⓘ **Costruito, misurato dagli strumenti, provato al contrario e visto a schermo
sono quattro stati distinti**, e qui il quarto manca. Le scelte più forti della
sessione — le cinque righe dei resti col verbo distinto, le tre alghe che devono
restare diverse, i tredici accorciamenti dei materiali — sono **giudicate solo
da me**.
