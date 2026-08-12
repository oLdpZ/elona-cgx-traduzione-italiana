# Ripresa sessione

Aggiornato: 2026-08-11, fine della **ventisettesima** sessione.

## La prima cosa da fare

Si va avanti su **due fronti insieme**:

1. **le battute di `db_creature.hsp`**, **882 da fare**, per **creatura
   intera** e in **ordine di livello** — lo strumento compone il lotto da solo,
   vedi più sotto. È il fronte a frequenza più alta del gioco;
2. **`proc.hsp`**, a 127 su 1.098, per zona di riga dalla **riga 1716** in
   avanti (le esibizioni sono chiuse fino a 1665; 1716-1780 sono le reazioni
   degli dèi alla predica).

⚠️ **I nomi di creatura sono chiusi**: l'ultimo che i conteggi mostravano da
fare era su una riga commentata. Vedi «Le righe commentate» più sotto.

### Le sette verifiche d'apertura

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 398 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 2466, doppie 0, senza razza 0
python -m strumenti.larghezze              # atteso: 0 fuori misura su 75 menu
python -m strumenti.diario                 # atteso: 0 fuori misura su 214 siti
python -m strumenti.battute --divergenti   # atteso: 11, tutte legittime
```

Se `--divergenti` sale, qualcuno ha reso due volte in modo diverso la stessa
frase giapponese. Le due nuove della 27ª sono volute: 「きゅう…」 («*sbuffo*»
altrove, «Quu...» sulla forma di vita quantistica, dove l'inglese fa il gioco
di parole con Q) e 「わん！」 («*bau!*» dove l'inglese descrive un'azione,
«Bau!» dove passa da `cnvtalk`, che mette le virgolette).

💡 Vale anche il manifesto del sorgente, che nessuno strumento controlla:

```powershell
$base="C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx"
Get-Content "C:\Games\Elona\_traduzione\manifesto-sorgente.txt" | ForEach-Object {
  $p=$_ -split '\s+',2
  if ((Get-FileHash "$base\$($p[1].Trim())" -Algorithm SHA256).Hash -ne $p[0]) { $p[1] } }
```
Nessun output = 72/72. ✅ Ricontrollato l'11/08 a fine 27ª.

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.606 | 1.606 | **100%** |
| `item_data.hsp` | 318 | 318 | **100%** |
| `skill.hsp` | 885 | 885 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `adv.hsp` | 12 | 12 | **100%** ⭐ chiuso il 2026-08-11 |
| `action.hsp` | 1.286 | 1.288 | **100%** (le 2 mancanti sono rinviate a toppa) |
| `text.hsp` | 1.718 | 1.720 | **100%** (le 2 mancanti aspettano `talk.txt`) |
| `proc.hsp` | **127** | 1.098 | 12% |
| `command.hsp`, `trait.hsp` | 0 | ~1.680 | 0% |

`db_creature.hsp`: **1.131 nomi** (chiusi, sul serio: vedi sotto) + **1.637
battute rese**, **882 da fare**. Era a 1.563 all'apertura della 27ª:
**677 rese** più 4 rinviate, sui lotti `015`-`026`, che coprono i livelli **6-45** — cioè
tutte le creature di città, i PNG di trama e i primi sotterranei.

⚠️ I conti per classe si rifanno così, e non si deducono: le classi si leggono
dal `dbmode` che precede la riga nel sorgente, incrociando `dizionario/` per le
rese e `lavoro/_c.jsonl` per quelle da fare. `2.092 + 1.563 = 3.655`, che è il
totale delle firme del file.

Altri fuori Fase 1: `custom_enemyevolution.hsp` **chiuso**; `ai.hsp` 6 su 100;
`event.hsp` 5 su 654; `chara_func.hsp` 45 su 331; `init.hsp` 6 su 133.

**398 test**, prova d'identità **72/72 e 27.813**, **11.815 sostituzioni**, il
compilatore non dice nulla, manifesto del sorgente **72/72**.

## Le quattro scoperte della ventisettesima sessione

### 1. ⚠️ Le righe commentate: l'ultimo «nome da fare» non esisteva

`estrai.py` **non salta i commenti HSP**. Misurato su tutto il sorgente:
**28 voci su 27.813** stanno su righe che cominciano per `;`, di cui **17 in
`db_creature.hsp`**. Quattro cadevano nel lavoro che restava, e una era l'unico
`nome` ancora aperto: `ハードゲイ` a `db_creature.hsp:105060`, commentata,
mentre la riga viva subito sotto (`:105061`) dà `explosioman`, **già reso**
«l'uomo esplosivo». Le altre tre erano i versi 「フーーー」 dello stesso mostro,
commentati in tutte e cinque le occorrenze.

Registrate in `rinviate.jsonl` col motivo, così spariscono dai lotti e restano
contate fra le non tradotte. **I nomi di `db_creature.hsp` sono chiusi.**

💡 **Da decidere**: far saltare i commenti a `estrai.py` sposterebbe la prova
d'identità da **27.813 a 27.785**, numero ancorato in mezzo progetto. Rinviata
apposta, non dimenticata.

### 2. ⚠️ I file «fuori da ogni elenco» non esistono, ma la lezione di `adv.hsp` sì

Cercati per davvero: `SPEC.md:413-418` li nomina **tutti**, `chat.hsp` come
Fase 3 e gli altri 63 come Fase 4. Il TODO della 26ª si chiude con un no.

⚠️ **Ma la cosa che rendeva `adv.hsp` importante non era l'elenco: era la
frequenza.** Dentro la Fase 4 — cioè *ultima* — stanno:

| file | firme | che cosa contiene |
|---|---|---|
| `buff.hsp` | 199 | i **nomi degli status** («Holy Shield», «Speed», «Regeneration») e i messaggi «X inizia / svanisce». Stanno nell'HUD **in permanenza** |
| `chara.hsp` | 258 | «You have learned a new ability, X.» e simili |
| `item_func.hsp` | 263 | i messaggi di quando raccogli, lasci cadere, un oggetto va perduto |
| `screen.hsp` | 103 | «Gauge Ready», «Autopickup»: etichette fisse dell'interfaccia |
| `item.hsp` | 206 | fasce di prezzo del negozio, «cheap», «expensive» |
| `main.hsp` | 330 | messaggi del ciclo principale |

Sono ~1.360 firme che il giocatore legge a ogni partita, in coda a tutto.
**Da valutare come lotto fuori ordine**, con lo stesso argomento che ha
spostato le battute davanti a tutto.

### 3. ⚠️ Il giapponese può essere inglese, e allora l'inglese si tiene

Lo `<Spazzino di sotterranei>` dice `lang("「Target Acquired.」", "Target
Acquired.")`: **le due lingue sono la stessa**, cioè l'autore fa parlare
inglese la macchina anche al giocatore giapponese. Quattro battute
(`Target Acquired.`, `Resistance is futile!`, `Pwned!`, `WTF`) dichiarate in
`invariati.md`. Tradurle darebbe all'italiano una macchina che parla la lingua
di chi legge, che né il giapponese né l'inglese hanno.
Stesso criterio già usato per `user`.

### 4. ⚠️ L'inglese riusa il repertorio di un'altra creatura

Non «amplia» o «restringe»: **incolla**. Le battute dell'**erudito**
(`P-please, no sir...`, `You are cruel.`, `Ha ha ha!`) escono identiche in bocca
al **profugo degli Elea**, al **viaggiatore** e — le tre di morte — al **saggio
della collina** e al **pescatore**. In giapponese sono quattro creature diverse
con quattro registri diversi: l'erudito è sprezzante, il profugo ha fame e
nostalgia, il viaggiatore viene rapinato, il saggio muore riconoscendo di non
aver saputo abbastanza.

💡 **Come si riconosce**: due creature lontane nel file con la **stessa lista
inglese** e giapponesi che non si somigliano. Vale la pena cercarne altre in
blocco invece di scoprirle un lotto per volta.

## Le tre scoperte della ventiseiesima sessione

### 1. ⚠️ L'ordine dei lotti era cieco alla frequenza

L'ordine di riga metteva l'accattone di livello 2 accanto a una divinità di
livello 1200. Misurato: delle 1.975 voci che restavano, **605 stavano su
creature di livello 1-10** e **528 oltre il livello 100**.

`battute.py` ora ordina per **livello crescente**, a parità di livello prima chi
ha più battute; `--per-riga` rimette l'ordine vecchio. Il livello è una
**procura**, non una misura: nel sorgente non esiste un campo «quanto spesso
esce» — `DBSPEC_CHARA_RARE` non lo è.

### 2. ⚠️ La stessa battuta giapponese può avere due firme

Il punk e il teppista dicono **tredici battute giapponesi identiche** con
tredici inglesi diversi: due firme, due voci da tradurre, a lotti di distanza.
Se le rese divergono **nessuna guardia lo vede** — sono entrambe italiano
valido. Misurati **88 giapponesi ripetuti**.

⚠️ **Otto divergenze su dieci erano legittime**: l'inglese *specializza* ciò che
il giapponese lascia generico (「がおー」 è `*creaking*` su un golem di legno e
`*growl*` su una divinità serpente). Quindi **promemoria, non divieto**: il
referto del lotto stampa «⚠️ GIÀ RESO ALTROVE» accanto a ogni voce che ha già
una resa, e `--divergenti` le elenca per giudicarle a mano.

### 3. ⚠️ `adv.hsp` era in perimetro e in nessun elenco

Uno screenshot ha mostrato «Hedorre il fratello volpe **joins your party!**».
Dodici voci ad alta frequenza mai toccate, ora chiuse. 💡 **Da rifare: cercare
altri file che gli strumenti sanno leggere e che nessun elenco nomina.**

## Il metodo per le battute di `db_creature.hsp`

⚠️ **Il lotto prende creature intere**, tutte le classi insieme
(`FLAVOR_PASSIVE`, `_ANGERED`, `_DEATH`, `_KILL`, `_WELCOME`). Il registro di un
mostro è uno. ⚠️ E serve anche a vedere quando **l'inglese ha cambiato il
personaggio**, che in una battuta sola non si nota.

```powershell
python -m strumenti.estrai db_creature.hsp --da-tradurre --uscita lavoro/_c.jsonl
python -m strumenti.battute --conto      # quanto resta, per classe
python -m strumenti.battute              # il lotto, in ordine di livello
python -m strumenti.verifica lavoro/<lotto>.jsonl
python -m strumenti.reimporta lavoro/<lotto>.jsonl
python -m pytest strumenti/tests -q
python -m strumenti.prova_identita
python -m strumenti.creature
python -m strumenti.battute --divergenti
python -m strumenti.genera_toppe_nomi
python -m strumenti.genera_toppe_casuali
```

Fatti `fase2-battute-001` … `-022`. Dopo aver rigenerato l'estrazione le
creature già fatte spariscono, quindi si riparte sempre da `[0]`.

💡 **Il lotto si scrive con uno script, non a mano.** Dalla 27ª il metodo è: un
file Python nello scratchpad con un dizionario `{(riga, jp): resa}` e un
controllo che **muore** se una resa non aggancia nessuna voce. Chiave `(riga,
jp)` e non la firma, perché il referto stampa riga e giapponese. Costa dieci
righe e ha già evitato due lotti scritti sulla voce sbagliata.

💡 **Tre guardie che `verifica` non fa e che conviene rilanciare a mano** sul
JSONL del lotto: nessun carattere a doppia larghezza tranne `♪`; nessuno dei
proibiti (`…`, `“”`, `～`, `«»`); nessuna parola inglese residua (`the`, `you`,
`your`, `is`, `my`…) in una statica che non sia dichiarata invariata.

💡 **Lo script del lotto tiene tre reti**, e conviene copiarle: nessuna voce
senza resa, nessuna resa che non aggancia niente, e **nessuna resa che diverge
da una già decisa** per lo stesso giapponese.

💡 Le altre guardie dei lotti: niente morfologia inglese residua; nessun
carattere a due byte tranne `♪`; nessun **participio che concorderebbe col
giocatore**. ⚠️ Quest'ultima **non** è automatizzabile: provata a mano su un
lotto, ha dato **3 falsi positivi su 4** («bella figura», «Nessuna ferita?»,
«la ferita» sono sostantivi).

## Le regole di resa

Terza persona sempre; mai `_s()`, `is()`, `was()`, `your()`, `have()`,
`does()`, `yourself()`; mai una preposizione davanti a `name()` o `itemname()`,
mentre `con`, `per`, `tra`, `sopra`, `dentro`, `contro` e `verso` reggono; la
preposizione sta nel valore, non nella frase; invarianza di genere prima di
tutto; un nome di abilità o di oggetto si copia; una `statica` si scrive **nuda**,
e se deve citare usa `\"`, **mai** le tipografiche.

⚠️ **`his(x)` a un argomento si può togliere, `his(x, 1)` no.**

### Gli appellativi che cambiano col sesso del giocatore

⚠️ Sono **due**, e la guardia ora li copre entrambi: `_onii` (`text.hsp:111`)
«Fratellone»/«Sorellona», 36 siti di chiamata; e `_syujin` (`text.hsp:112`)
«Padrone»/«Padroncina». **Non portano l'articolo dentro** — a differenza di
`name()` — quindi la preposizione nuda regge («di Fratellone», «per
Fratellone») e l'articolo no («il mio Fratellone» sbaglia genere metà delle
partite).

⚠️ **`cdatan(CDATAN_NAME, rc)` invece l'articolo lo porta dentro**, come
`name()`: il nome italiano è «il fratello volpe». Niente «di» davanti.

### Dalle battute

⚠️ **Il giocatore è l'interlocutore e non ha genere noto.** «Welcome home!» è
«Eccoti a casa!», «Rieccola a casa.», «Eccoti di ritorno.». Vale per i
**vocativi**: `You thief!` è «Al ladro!», e allo stesso modo «Al maniaco!»,
«All'assassino!». 💡 **Il registro può risolvere il genere**: chi dà del lei o
del voi — il maggiordomo, la monaca, la signorina dal cuore nero, l'accattone —
non concorda mai.

**Un verso si rende in ortografia italiana, non si copia dall'inglese.**
`Woof..` sull'ululato 「ワオーン…」 è «Auuuh...»; 「めぇめぇ」 è «Bee bee»;
「ぴよぴよ」 (il pigolio) è «Pio pio»; 「こーん」 (la volpe) è «Cooon...». Dove il
giapponese identifica l'animale la resa lo segue.

💡 **Il tic di una creatura si porta in italiano**: la sorella cane chiude con
«bau», la sorella gatta con «miao».

💡 **L'inglese storpiato in katakana si rende storpiato**: 「カモンベイベー」 è
«Camon beibi!», 「グッド！」 è «Gud!», 「ざっつあぷりちーふらわー」 è «Zatsa priti
flauer!».

⚠️ **Quando una concatenazione si spezza in due `lang()`** i due frammenti sono
**un lotto solo**. E se un frammento resterebbe identico all'inglese, gli si fa
portare qualcosa che il giapponese ha e l'inglese ha perso — l'allungamento di
ポピー diventa «Poppyyy!», il ギャ di 「ギャハハハハ」 diventa «Ghiahahaha!».

⚠️ **Vale anche per le dinamiche.** `_syujin(...) + "!"` è **per costruzione**
identico all'espressione inglese, perché la funzione porta dentro la
traduzione. Il giapponese di `db_creature.hsp:93453` è 「ー！」, cioè il grido è
**allungato**: la resa diventa `+ "!!"`, e la guardia si scioglie senza inventare
niente.

### Trovate nella ventisettesima

- ⚠️ **Un vocativo non può portare un aggettivo che concordi col giocatore.**
  «questo scemo» sbaglia metà delle partite; **«quell'imbecille» no**, perché
  `quell'` vale per entrambi i generi. Altre che reggono: «mezza cartuccia»,
  «pappamolla», «carogna», «idiota», «debole», «canaglia», «soggetto».
- 💡 **Il registro di chi parla può risolvere il genere anche in avanti**: la
  cameriera, la guaritrice e l'attrazione del locale danno del **lei** al
  cliente, e così `お客さま` non ha bisogno di un vocativo che concordi
  («Aaah! Tutto bene?!»).
- ⚠️ **`_syujin` e `_onii` vanno lasciati soli a portare il genere**: tutto ciò
  che li circonda dev'essere invariante. «Bentornato, Padrone!» sbaglia,
  «Eccoti a casa, Padrone!» no.
- 💡 **Il bisticcio di mestiere si tiene**: il pescatore dice 活きのいい («bello
  fresco», di pesce) e 雑魚 («pesciolino»), e in italiano diventano «Che bel
  pescione vivace» e «che pesciolino da niente».
- 💡 **Una parlata da bambino piccolo si rende con la erre che diventa elle**:
  il gatto randagio storpia かえる in かえう, e in italiano «Tolno a casetta».
- 💡 **Il katakana che scrive una parola giapponese è enfasi, non prestito**:
  カガク è 科学, e si rende «SCIENZA» in maiuscolo. Diverso da エクスプロージョン,
  che è inglese e va storpiato («Ecsplosgion»).
- ⚠️ **Un nome proprio che compare in una battuta è quasi sempre già deciso
  altrove**: `ヴェセル` è **Bethel** (dal nome della creatura), `ジャビ王` è **re
  Xabi**, `巫女` è **sacerdotessa**, `異形の森` è **Vindale**, `サイモア` e
  `ヴァリウス` restano **Saimore** e **Barius** perché li usa già `chat.hsp`.
- ⚠️ **Il prefisso col nome di chi parla non si porta dentro `cnvtalk`.** Il
  giapponese di Moyer è `モイアー「…」`, col nome **fuori** dalle virgolette
  giapponesi; `cnvtalk` avvolge tutto fra virgolette, quindi il prefisso
  finirebbe dentro. L'inglese lo lascia cadere e si fa lo stesso.
- ⚠️ **Un imperativo con pronome atono concorda col giocatore**: «arrestatelo»,
  «portatelo» sbagliano metà delle partite. Si toglie il pronome
  («Immobilizzate e torturate!») o si mette un nome che porti il proprio genere
  («quell'imbecille», «un cane bastonato», «Che lumaca!»).
- 💡 **Le citazioni si rendono con la versione italiana che esiste già**:
  「真実はいつだってひとつ！」 è il tormentone di Conan, «C'è sempre una sola
  verità!»; 「灰色の脳細胞」 sono «le cellule grigie» di Poirot;
  「ピーキーすぎて…」 è la battuta di Kaneda in AKIRA. La citazione si riconosce
  dal giapponese, non dall'inglese, che spesso l'ha già persa.
- ⚠️ **Il katakana può nascondere un dialetto**: il corvo mercante dice
  「ナンデヤネン」 e 「マイドアリ」, cioè parla **in kansaiben**, la parlata del
  bottegaio di Osaka. Si rende con la lingua viva del mercante, non con la
  lettera.
- ⚠️ **`estrai` tiene distinte due voci con lo stesso giapponese e inglesi
  diversi sulla stessa riga** (il carbonchio rubino, `67563`): sono due firme,
  e vanno rese **uguali**, non a caso.

### Dalle sessioni precedenti

- **Il giocatore non ha genere noto.** Non «sono sopravvissuto» ma «sono ancora
  in piedi»; non «quando sono pronto» ma «quando sarà tutto pronto».
- **Un elenco di compiti si rende all'infinito** («Bere qualcosa»).
- Un prefisso davanti a sostantivi di genere diverso può solo essere un aggettivo
  in -e. Ma se può andare **dopo**, ci va.
- **Nessun participio quando il soggetto non ha genere noto.**
- **`your()` diventa «proprio»**, che concorda con la cosa posseduta.
- **In un menu la valuta si abbrevia.**

## Le cose da non riscoprire

### L'inglese non traduce: riscrive, e in cinque modi

Tutti visti l'11/08. **Inventa** (`<Gwen>`, `<Mia>`, il gorgoglio di chi affoga
diventato «I'm sorry I failed you»); **amplia** (una risatina di tre sillabe →
venti parole); **restringe**; **scambia** (`<Tam>` ha le prime due battute
invertite); e ⚠️ **cambia il personaggio** — la macchina delle pulizie è
infantile in giapponese e robotica in inglese.

**L'originale arbitra sul significato; l'inglese conserva il diritto di
specializzare** quando sa qualcosa che il giapponese non dice.

### Un gioco di parole va rifatto, non tradotto

Il gioco della recluta è **visivo** (矢 e 失 si somigliano a vederli), non
fonetico. Reso con **suono/sonno** — e «Suono» è una resistenza che esiste
davvero. ⚠️ Il materiale del bisticcio dev'essere roba che nel gioco esiste.

### Una stringa che il giocatore legge può stare fuori da `lang()`

Sette intestazioni del diario (`command.hsp`) **e `main.hsp:227`**, il primo
messaggio del log. Toppate **a mano**: un generatore riscriverebbe sopra.

### Il nome di una funzione può mentire

`cnvarticle` (`init.hsp:173`) **non mette un articolo**. `cnvtalk` avvolge fra
virgolette — per questo il testo dentro conta come contenuto. E ⚠️ **l'aiuto
della console mente**: `add_ally` dice «by character index» ma fa
`characreate` dall'ID di database (`system.hsp:4882`).

### Una preposizione può agire a venti righe di distanza

`s(12)` si compone a `text.hsp:11837` e finisce dopo «da » a `:11859`.

### Il giapponese arbitra sul significato, il codice sullo stato del gioco

⚠️ Il diario dice スライム, il dialogo di Miches dice プチ: vince il codice.
⚠️ Due quiz (`text.hsp:998` e `:1214`) portano lo stesso giapponese con risposte
diverse: arbitrano `map.hsp:2271` e `:9009`. **Non toccarle.**

### Se l'inglese rende un nome in più modi, vince quello della prosa

⚠️ ルストール è `Lustor` (prosa), `Rust Plaza` (etichetta) e `Ruoza` (esca di
quiz) — e `Ruoza` è **già** il nome di ルオザ.

### L'ordine di una concatenazione non è un vincolo: si toppa

⚠️ Ma una toppa si aggancia **solo a una riga senza `lang()`**. Se la voce è
**dinamica** non serve nessuna toppa. E `funzioni_di_contenuto` confronta le
interpolazioni **ordinate**.

### Non correggere una toppa che qualcuno genera

`toppe.jsonl` è in larga parte generato. **Se uno strumento la genera, la
correzione va nello strumento.** ✅ Verificato l'11/08 che le toppe **a mano
sopravvivono** ai due generatori.

### Cercare prima di scrivere

Tipi di negozio, elementi, verbi della pianta, assetti tattici, parti del corpo,
tipo di Nefia, categorie di filtro. E per le battute: i **nomi delle creature**
sono già tutti in dizionario. ⚠️ Anche i termini di contorno: «campo di
prigionia», «pannello di comando», «Porto Kapul», «Poppy», le resistenze —
erano **tutti già decisi altrove**.

### Aggiungere una funzione che l'inglese non aveva non si può

Si possono **togliere** le morfologiche, non se ne possono **aggiungere**.

### La frase di combattimento vive in due file

`action.hsp` scrive «… e» e imposta `gdata(GDATA_DMG_TYPE) = 2`;
`chara_func.hsp:6323` legge il flag e stampa il resto. `init.hsp:1666` aggiunge
già lo spazio.

### Le stringhe che sembrano testo e sono codice

`EN` (`action.hsp:4816`, `text.hsp:9361`) è la chiave che `*convert_talk` cerca.
` Lv` (`action.hsp:12383`) è ciò che il gioco cerca in coda al nome.

### Un letterale può essere l'operando di un confronto fra due file

⚠️ `Party Room` (`proc.hsp:1123`) è confrontato col nome che assegna
`map_rand.hsp:1287`, fuori perimetro. **Rinviata.**

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

⚠️ **Il riquadro taglia**: non manda a capo, non restringe il carattere. Il
metro è il terzo argomento passato a `*prompt_key`:
`caratteri = (pixel − 46) / 7,7`. Lo fa `strumenti/larghezze.py`. **Va lanciato
a ogni lotto di menu.**

⚠️ **La stringa inglese non è il budget.** ⚠️ **La larghezza può dipendere dalla
lingua**: `450 - 50 * en` vale **400**.

⚠️ **`talk_conv` manda a capo ma l'ultima parola scappa** (`init.hsp:1326-1369`).
`strumenti/diario.py` lo misura: tetto **36**, 214 siti. Il verso giusto è
**accorciare, non imbottire** — ma quando la riga si compone a runtime
l'intuizione «più corto è meglio» è **sbagliata**.

⚠️ **Le battute non hanno tetto**: passano da `txt`, non da `talk_conv`.

## Le due righe di `action.hsp` che non si traducono

- **`:4584`** — l'articolo inglese davanti a un'arma unica. Toppa.
- **`:9631`** — `his(tc, 1)`, il possessivo che in italiano si omette. Toppa.
  ⚠️ **Il testo di una toppa non passa da `degrada` e non può portare accenti.**

## 391 stringhe fuori perimetro

⚠️ **Un oggetto di Elona ha due nomi, e ne traduciamo uno.** `iknownnameref` è
quello prima dell'identificazione, e l'estrattore non lo guarda
(`estrai.py:65`). **Deciso: si annota e si prosegue.** Conseguenza: il 100% di
`db_item.hsp` e `custom_tweaks.hsp` **è falso**.

⚠️ **E un secondo perimetro fuori: `data/talk.txt`** (86 KB), che non passa da
`lang()` — `SPEC.md:436`. Due voci di `text.hsp` sono rinviate lì.

## L'ordine che resta

0. ⚠️ **Da decidere prima di tutto**: se anticipare il blocco ad alta frequenza
   che oggi sta in Fase 4 — `buff.hsp`, `chara.hsp`, `item_func.hsp`,
   `screen.hsp` (~830 firme fra tutti e quattro). Vedi la scoperta 2 della 27ª.
1. **le battute di `db_creature.hsp`**, 882, per creatura intera in ordine di
   livello;
2. **`proc.hsp`**, 971 firme, per zona di riga da **1716**;
3. `command.hsp`, `trait.hsp`;
4. `ai.hsp` (94) ed `event.hsp` (649);
5. `chara_func.hsp`, le 286 rimanenti — ⚠️ dentro ci sono le tre pietre di
   Lesimas e l'ankh del sole, **già rese** in `text.hsp:11576-11594`: si
   **copiano**. E la causa di morte (`:6850`), che va insieme a `main.hsp:4409`;
6. `init.hsp` (133) — ⚠️ lì sta la decisione sul possessivo `his(x, 1)`;
7. i nomi non identificati di `db_item.hsp` e le 2.555 descrizioni.

## Domande aperte

⚠️ **`Cyber Dome` fu deciso sull'inglese.** Il giapponese è アクリ・テオラ, nome
**opaco** che per la regola resterebbe invariato. Segnalata, non toccata.

⚠️ **`spawn_item` ha prodotto due volte l'oggetto sbagliato**, poi ha ripreso.
L'unica pista è lo stato dei filtri: `spawn_item` **non chiama `flt`**.

⚠️ **La toppa dell'ordine delle Nefia rompe l'ordine giapponese.** Innocuo finché
compiliamo la build inglese.

⚠️ **`diario.py` non vede le righe che si compongono a runtime.**

⚠️ **Le 56 dinamiche di `db_creature.hsp` restano fuori classificazione.**
Nessuna di esse è oggi un nome.

⚠️ **Undici divergenze restano in `--divergenti`**, giudicate legittime. Se una
sessione futura non è d'accordo, il posto per discuterle è `decisioni.md`.

⚠️ **`estrai.py` non salta i commenti HSP.** 28 voci su 27.813. Farlo saltare
sposterebbe la prova d'identità a 27.785: decisione rinviata, vedi la scoperta 1
della 27ª.

⚠️ **Il riciclo inglese è misurato: 84 stringhe inglesi coprono 231 giapponesi
diversi** in `db_creature.hsp`. Non è più una scoperta a sorpresa, è una
quantità nota. Le peggiori: `Huh?` su **6** giapponesi; `Why are you doing
this?`, `P-please, no sir...`, `Don't make a fool of me!`, `You are cruel.`,
`Ahhhh!`, `I don't deserve this...`, `Go to hell!`, `Stop it!` su **5**
ciascuna. Si rimisura così:

```powershell
python -c "import json,io,collections; d=collections.defaultdict(set); [d[v['en']].add(v['jp']) for p in ['lavoro/_c.jsonl','dizionario/db_creature.hsp.jsonl'] for v in map(json.loads, io.open(p,encoding='utf-8')) if v.get('file')=='db_creature.hsp' and v.get('tipo')=='statica']; m=[(e,j) for e,j in d.items() if len(j)>1]; print(len(m), sum(len(j) for e,j in m))"
```

💡 **Come si usa**: quando un lotto tocca una di queste righe, **non si guarda
l'inglese**. Chiuse: 76452/76458/76464 (erudito), 88185/88191/88197
(viaggiatore), 88274/88280/88286 (profugo), 73911 (saggio della collina),
90657 (pescatore), 88363/88369/88375 (addetto del casinò, che in giapponese
minaccia la tortura e chiama i buttafuori), 98449 (la guardia, giapponese
identico al guerriero mercenario: lì si **copia**).
⚠️ **Resta aperta** 102518/102524/102530.

💡 **Il riciclo funziona anche al contrario**: la guardia (`98449`) e il
guerriero mercenario (`115178`) hanno il **giapponese identico** e due inglesi
diversi. Lì la regola si ribalta — non si reinventa, si copia la resa già
decisa.

## Cose che valgono sempre

⚠️ **Il sorgente è pinnato al tag `2.31.2.0`**, e l'integrità si verifica col
manifesto SHA-256, **mai** con `git status`. Gli hash sono in MAIUSCOLO.
✅ Ricontrollato l'11/08: **72/72**.

⚠️ **L'attributo di sola lettura sulle cartelle NON è la protezione del
sorgente.** I 3.374 file del clone sono tutti scrivibili; solo le 34 cartelle
hanno il flag, che su Windows è acceso quasi ovunque. La protezione è la
disciplina più il manifesto.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp`; chi copia nomi di creatura fuori da
`db_creature.hsp`; chi confronta un letterale contro un valore tradotto.

⚠️ **CP932 non codifica tutto, e quello che codifica non è detto si veda.**
Niente `«»`; e niente `…`, `“”`, `・`, `《》`, **`☆`**, **`～`**, né i caratteri a
larghezza intera (`Ｑｙ＠`). Unico ammesso: `♪`.
Gli accenti veri si scrivono nel dizionario e li degrada `applica`;
⚠️ **guardare dove cade l'accento**: a fine parola è gratis, a metà no.
⚠️ **Le toppe non passano da `degrada`.**

⚠️ Un guardiano dell'ambiente blocca i messaggi di commit che contengono `/man/`
letto come percorso: passare il testo con `git commit -F <file>`.

⚠️ **La shell mangia il backtick, e un heredoc lungo in bash si rompe.** Scrivere
un documento che contiene codice fra apici inversi **da un file**, non da riga di
comando. ✅ Successo di nuovo l'11/08 scrivendo `decisioni.md`.

## Per rifare la prova in gioco

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -Force
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

⚠️ La copia fallisce se il gioco è aperto.
⚠️ **Non lasciare una shell con la directory corrente dentro `build\`**: tiene la
cartella occupata, `applica` muore a metà e `compila` accusa
`#Error: in line 112 [main.hsp]`, che è la riga dell'`#include` e non dice
niente della causa. Successo l'11/08.
⚠️ Se `applica` viene interrotta lascia l'albero **incompleto**: si rilancia e
basta.

⚠️ **Controllare la data dell'exe prima di fidarsi di uno screenshot.**

**L'eseguibile in `cgx-test.exe` è aggiornato a fine ventisettesima sessione
(12/08/2026 00:10)** e contiene i lotti 001-026, `adv.hsp` e la toppa di
`main.hsp`.

### La console di debug

**Si apre con F12** (`main.hsp:3322`; F11 è `dump_chara`). Esce con ESC. Parte in
modalità **HSP, non Lua**: `spawn_chara <id>` funziona subito.

⚠️ **`add_ally <id>` genera la creatura E la rende alleata** — l'aiuto dice «by
character index» ma il codice fa `characreate` dall'ID di database
(`system.hsp:4882`). È il modo di far uscire **oziose e benvenuti** da creature
che il database dà ostili.

⚠️ **La relazione predefinita decide quale classe di battuta esce.** Con
relazione < 0 la creatura attacca e dà le **offese**; con relazione 0 o da
alleata dà le **oziose** (`ai.hsp:774-796`). Si legge nel blocco `DBMODE_SET`
della creatura, campo `CDATA_RELATION`.

ID di creatura verificati: **165** il cane, **50** il segugio, **267** il cavallo
zoppo, **386** la giraffa, **482** Yacatect, **326** il menestrello, **9** il
mendicante. Dalle battute rese: **538** il fratello volpe (porta `_onii`),
**363** la sorella cane maggiore, **962** il bambino, **352** `<Silvia>`,
**174** il punk, **36** l'anziano, **963** il bambino sadico, **1066** `<Sist>`,
**1043** `<Imarituka>`, **947** `<Burt>`, **949** il barista, **1008** la
cthulhick, **1048** la giovane rondine.

Dai lotti 015-022, tutti letti in `defines/mod.hsp`: **272** l'artista,
**233** il fante juere, **224** `<Ainc>` il cavaliere novizio, **415** la forma
di vita quantistica, **535** il cucciolo di grifone, **623** l'erudito,
**260** il gatto nero, **262** l'androide, **271** la canaglia, **909** il
soldato artiglio, **346** il cucciolo, **263** l'angelo nero, **182**
l'infermiera, **184** il rampollo, **332** il gatto randagio, **472** il profugo
degli Elea, **500** il guardiano del karass, **321** l'uomo esplosivo,
**648** il bimbo della collina, **274** l'aristocratico, **223** `<Raphael>`,
**142** `<Erystia>`, **441** il cittadino, **407** la cameriera, **280**
`<Balzak>`, **203** `<Moyer>`, **302** il capo della banda, **369** il cane
poliziotto, **183** il riccone, **279** `<Icolle>`, **868** `<Rianna>`,
**243** `<Arnord>`, **259** `<Noel>`, **244** il samurai kamikaze, **473** il
viaggiatore, **345** la moto di Kaneda, **253** `<Marks>`, **408** `<Lune>` la
cameriera, **74** la guaritrice, **802** l'angelo apprendista, **32** lo
spazzino di sotterranei.

Dai lotti 023-026: **317** la mietitrice dagli occhi d'argento, **204** il
soldato scelto di Palmia, **519** `<Nazuna>`, **476** `<Naplus>`, **438**
`<Carla>`, **437** `<Milos>`, **709** il gufo spaziale, **925** `<Alsapia>`,
**348** e **518** le due mascotte a ore, **620** il corvo mercante, **374**
`<Mefan>`, **301** `<Conery>`, **650** `<Dain>`, **471** l'addetto del casinò,
**697** il lupo mannaro detective, **893** `<Zisilion>`, **478** `<Eila>`,
**231** `<Colonnello Gilbert>`, **486** l'abitante dell'abisso, **80**
`<Xabi>`, **577** `<Lenas>`.

`spawn_item <id>` lascia l'oggetto **per terra**: si raccoglie con `,`.
ID utili: **256** l'attrezzo da cucina portatile, **204** il cadavere generico,
**740** la `<Conchiglia Ignota>`, **1249** l'Aurtehom, **1097** la banca di
Yacatect, **1068** il cuore del crepuscolo.
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
incrementa **una volta per ogni classe che la creatura possiede**: l'interruttore
è acceso per costruzione. Poi serve stare **entro dieci caselle**, e la battuta
esce ogni **5 turni con probabilità 1 su 4** (`ai.hsp:768-771`). Si aspetta
tenendo premuto `5`. ⚠️ **Non usare l'abilità Esibizione mentre si aspetta**:
`ai.hsp:772` zittisce tutti.

Il **benvenuto a casa** scatta entrando in `AREA_HOME` (`system.hsp:34`), e il
codice richiede relazione neutrale o creatura nell'area (`main.hsp:8449`).

⚠️ **Il ballo e la predica dei PNG non escono mai.** `ai.hsp:1654` e `:1668` li
accendono con `CDATA_AI_CALM` a **7** e **8**, e in tutto il sorgente **nessuno
assegna quei due valori**: codice morto.

### Come si provano le esibizioni

Le dieci righe del giudizio finale escono **solo se suoni tu** (`proc.hsp:950`),
e serve l'abilità **Esibizione**, che si impara dal maestro a **Derphy** o
**Porto Kapul**. **Elemosina accorata** si impara da sé svegliandosi con **meno
di 500 monete**; **Predica** con Fede oltre 9.

### Il diario

**Si apre col tasto `j`**. ⚠️ **Le notizie vecchie restano in inglese**:
`newsbuff` sta dentro il salvataggio. Contano solo quelle che nascono dopo.

### Le 169 battute degli dèi, ancora mai viste

⚠️ **Non escono se non si indossa l'amuleto giusto.** `GDATA_GOD_TALK` parte a
**0** e lo accende **solo** `ENCHANT_GOD_SIGNALS`, che ce l'ha un oggetto solo —
`<Conchiglia Ignota>`, `spawn_item 740`. E serve **seguire un dio**.

```
F12 → spawn_item 740      raccogli con , e indossa con w
c                          controlla che il personaggio segua un dio
salva, esci, ricarica      → alla prima mossa esce il «bentornato»
dormi in un letto          → il «sonno», e col caso il «sogno»
uccidi qualche mostro      → l'«uccisione», 1 volta su 20
offri un oggetto su un altare → «offerta gradita»
j, pagina di sinistra      → le notizie nuove
```

Ci si converte **pregando** (`p`) **sopra un altare**, e ⚠️ **il dio che prendi è
quello dell'altare**. ⚠️ **`spawn_item 171` non serve**: l'altare generato dalla
console nasce **senza dio**. Il posto giusto è la **Terra della tregua**, che
tiene tutti e otto gli altari in una sala: Mani (10,8), Lulwy (13,8), Opatos
(10,13), Ehekatl (13,13), Itzpalt (20,8), Kumiromi (23,8), Jure (20,13),
Yacatect (23,13). 💡 Conviene **Ehekatl**, che ripete l'ultima parola di ogni
frase.

### Il collaudo, punto per punto

- ✅ **L'evoluzione degli alleati**, ✅ **i nomi a schermo**, ✅ **«draco»**,
  ✅ **il combattimento**, ✅ **il menu degli ordini al compagno**, ✅ **il libro
  dell'abisso**, ✅ **i quattro menu a oggetto**, ✅ **la vetrina del
  panettiere**, ✅ **il diario delle missioni**, ✅ **le esibizioni e
  l'elemosina**, ✅ **il ♪ come icona**: provati.
- ✅ **Le battute e `_onii`**: provate l'11/08 col fratello volpe (`add_ally 538`).
  «Fratellone» interpola correttamente; viste anche «Cooon...», «Il fratellino ha
  una voce triste.». ✅ E `name()` rende «qualcosa» per una creatura non visibile:
  «Qualcosa perde la vita.» **non è un difetto**.
- ❌ **«*X* tira un sasso.»**: il difetto riparato, **mai visto**. Serve uno
  spettatore di livello alto rispetto all'artista (`proc.hsp:755`).
- ❌ **L'evoluzione dei nemici**: **mai vista**. La prova mancante più vecchia.
- ❌ **La carne fra parentesi**: mai vista, e decide **due** famiglie di cibi.
  ⚠️ serve cucinare col **256** su un cadavere.
- ❌ **Le 169 battute degli dèi**: mai viste.
- ❌ **Il tocco elementale** (`proc.hsp:8797`).
- 🆕 **Da provare**: «Buon cammino!» all'ingresso nel mondo; «X si unisce al
  gruppo!» (`add_ally 538`); le battute dei lotti 010-014; la **bacheca degli
  incarichi**; i nomi delle Nefia; il gioco di carte; la banca.
- 🆕 **La lista data a fine 27ª, mai tornata**: `add_ally 500 407 332 223`,
  aspettare tenendo `5`; poi tornare a casa; poi `spawn_chara 472` e `623` da
  attaccare e uccidere. Serve a vedere se le tre volte in cui il giapponese ha
  scavalcato l'inglese hanno retto a schermo. **Da rifare o completare.**
- 🆕 **Dai lotti 023-026, da guardare**: `spawn_chara 471` (l'addetto del
  casinò, dove l'inglese aveva di nuovo le battute dell'erudito); `add_ally
  709` (il gufo spaziale, che in giapponese dice tre versi **sfigurati** resi
  sfigurati anche in italiano — se sembrano refusi, l'ho sbagliato);
  `add_ally 620` (il corvo mercante, in parlata da bottegaio); `add_ally 348`
  (la mascotte che fa il barker per Jure).
- 🆕 **Le tre cose della 27ª che solo uno screenshot decide**: `add_ally 408`
  (`<Lune>`, che chiama col `_syujin` allungato); `spawn_chara 32` (lo spazzino
  che parla **inglese per scelta**: se stona a schermo, la riga di
  `invariati.md` va ridiscussa); `add_ally 326` (il menestrello, che ora
  **canticchia** invece di cantare parodie inglesi).
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
schermo, non tronca.

Vedi [[una-chiave-che-si-sdoppia]], [[l-inglese-non-traduce-riscrive]],
[[il-gioco-di-parole-cambia-canale]],
[[una-causa-plausibile-scritta-nel-codice]],
[[la-frequenza-non-si-deduce-dal-file]], [[una-procura-non-e-una-proprieta]],
[[una-guardia-vale-solo-dove-guarda]], [[guardia-troppo-severa]],
[[il-round-trip-non-basta-conta-i-byte]], [[accorciare-non-imbottire]],
[[il-difetto-di-monte-lo-paghiamo-noi]],
[[l-ordine-di-una-concatenazione-si-toppa]],
[[correggere-il-generatore-non-il-generato]],
[[genere-ignoto-si-risolve-col-complemento]], [[larghezza-per-campo]],
[[il-testo-dentro-la-stringa-non-e-codice]],
[[la-frase-che-si-compone-in-due-file]],
[[il-nome-interno-non-e-quello-a-schermo]],
[[coerenza-fra-due-file-uno-solo-tracciato]],
[[toppe-fuori-dal-dizionario]], [[la-forma-memorizzata-non-e-quella-scritta]],
[[una-chiave-che-collide-non-e-una-chiave]],
[[il-campo-che-il-sorgente-dichiara]], [[la-testa-porta-il-genere]],
[[una-decisione-nel-posto-sbagliato]], [[una-guardia-agganciata-a-se-stessa]],
[[ultima-scrittura-vince]], [[percentuale-senza-denominatore]],
[[la-categoria-che-il-sorgente-dichiara]],
[[il-posto-decide-quando-arriva-il-dato]], [[dato-o-derivata]],
[[toppe-generate-dal-sorgente]], [[stessa-forma-va-verificata-nel-codice]],
[[strumento-di-diagnosi-assente-non-guasto]], [[chi-accende-la-stringa]],
[[il-database-che-spiega-invece-di-dichiarare]], [[omofono-base-kanji-patina]]
e [[cp932-perdite-silenziose]].
