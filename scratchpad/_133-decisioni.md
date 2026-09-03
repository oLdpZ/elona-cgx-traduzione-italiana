
## La centotrentatreesima — il lotto B, mezzo lotto C, e i nomi propri che si sbagliano copiando — 2026-09-03

**797 rese** in `scene2.hsp` (da 95 a 892 su 1.701): lotto B chiuso (239, scene
7-30) e lotto C fino alla scena 131 (558 su 632).

### ⚠️⚠️⚠️ Le grafie inglesi dentro le rese italiane, e perché sono un cancello

`Ylva` è l'inglese; il progetto scrive **`Irva`** in 1.058 rese. Le **due sole**
eccezioni in tutto il dizionario erano le scene della 132ª — il lotto A, cioè
esattamente il lotto da cui stavo per copiare la grafia fino a fine fase.

**Non l'ho trovato traducendo:** stavo per scrivere `Ylva` nel lotto C e sono
andato a controllare come lo scrive il resto del gioco. Il modo in cui si
sbaglia un nome proprio non è inventarlo, è **guardare come l'ha reso chi ha
tradotto prima** — che è anche il modo in cui un difetto di una sessione
diventa una convenzione.

| grafia inglese | resa | perché |
|---|---|---|
| `Ylva` | **Irva** | イルヴァ. 1.058 rese con `Irva`, 2 con `Ylva` (la 132ª) |
| `Sierre Terre` | **Sierra Terre** | シエラ・テール. ⚠️⚠️ **L'inglese si contraddice da solo**: `scene2.hsp` scrive «Sierra» 8 volte, `chat.hsp` «Sierre» 7. Il giapponese ne ha **una**, e le 10 rese col refuso lo copiavano. Deroga della 79ª: dove il monte è incoerente decide il giapponese |
| `Port Kapul` | **Porto Kapul** | 24 rese già giuste contro 1 rimasta inglese (`db_item.hsp:108457`) |
| `Rosura` | **Lothria** | ロスリア. Refuso di `scene2.hsp:1139` e solo lì: nello stesso file «Lothria» compare 29 volte |
| `North Tyris` | **Tyris del Nord** | 164 rese su 165, **zero** eccezioni in italiano: entra nella tabella per completezza |

Vive in **`strumenti/scene.py`, costante `GRAFIE`**, letta da `problemi()` per
tutti e tre i tipi di blocco. Ogni riga porta accanto il conto che l'ha decisa.

⚠️ **Condizione che chi aggiunge una riga deve verificare:** nessuna forma
italiana contiene quella inglese, altrimenti la sostituzione di
`_133-grafie.py` si morde la coda. C'è un test che lo misura invece di darlo
per buono (`test_la_forma_italiana_NON_si_accende`).

⭐ **La prova al contrario non è una riga inventata**: è la resa del prologo
com'era scritta nel dizionario fino al mattino del 2026-09-03, parola per
parola. Se il cancello sparisce, quel test fallisce.

💡 **`Rehmido` NON è nella tabella, e la ragione va scritta.** L'inglese lo usa
sia per レム・イド (la **civiltà**, → `Rehm-Ido`) sia per レミード (le
**rovine**, → `Remido`, glossario 104ª): una sostituzione meccanica
sbaglierebbe metà dei casi. `scene2.hsp` scrive «Rehmido Depth» dove il
giapponese dice レミード遺跡・深層 — reso «le Rovine di Remido, strato
profondo».

### ⚠️⚠️ `applica` contava ogni resa di scena come «voce orfana»

`dizionario/scene2.hsp.jsonl` sta nella cartella dei dizionari ma non è fatto di
firme `lang()`: lo inietta `scene --applica`. Il ciclo di `applica.py` lo
trattava come gli altri, faceva 0 sostituzioni e contava tutto come orfano.
L'`ATTENZIONE` in coda diceva **86** alla 132ª, **258** dopo il lotto B, e
sarebbe arrivata a 1.701.

**Un allarme che suona sempre e cresce è peggio di nessun allarme**, perché
seppellisce l'orfana vera — quella che dice che il monte si è mosso sotto una
resa, cioè il motivo per cui quell'`ATTENZIONE` esiste. Stessa forma del guasto
della 96ª, ma più subdola: qui il numero **saliva**, e un numero che sale sembra
informativo.

### ⚠️⚠️ Un carattere che CP932 non sa scrivere passava il cancello

Le caporali `«»` — la punteggiatura che il progetto usa **nei documenti** — non
sono toccate da `degrada()` e non erano guardate da `problemi()`. Sarebbero
morte molto più tardi, dentro `--applica`, a lotto già reimportato.

    «quella cosa»   CP932 non lo scrive: UnicodeEncodeError
    perché          degrada -> "perche'" -> ok
    “virgolette”    CP932 LE SCRIVE, a doppia larghezza ⚠️

⭐ **Il cancello va dove si scrive la resa, non dove si costruisce l'albero.**
⚠️ Le virgolette curve restano un buco che il codice non può vedere.

### Il blocco a margine negativo non ha chiesto una decisione di struttura

Scena 11 blocco 8: 14 righe **in inglese** su un soffitto di 13, il solo punto
del file dove il monte sfora. Il piano prevedeva di spezzarlo in due `{chat_N}`.
La resa italiana ne fa **11**. La ragione vale per tutta la fase: **l'inglese di
monte è una traduzione lunga di un giapponese più asciutto** (690 caratteri
inglesi contro 262 giapponesi), e traducendo dal giapponese il margine si
ricompra. Il blocco a margine zero (scena 8 blocco 15, 13 su 13) è stato
accorciato apposta a 12 per non stare sul filo.

### Gli attori: 41 etichette, 19 già decise altrove

`scratchpad/_133-attori.py` cerca ogni `<Nome>` di un lotto negli altri
dizionari e mostra come il progetto lo rende già. Ha trovato il caso che il
piano annunciava:

- **`<Conerly>` di `scene2.hsp` è il `<Conery>` di tutto il resto del gioco**
  (giapponese コネリー). Reso **`<Conery> il generale di Palmia`**, come
  `db_creature` e `db_card`: è la stessa persona che il giocatore incontra
  nelle missioni, e due grafie ne farebbero due.
- **`Citzen`/`Citizen`** (l'inglese oscilla, il giapponese è 市民 in entrambi)
  → **`Cittadino`**, una resa sola. Stesso trattamento per
  `Security Officer <Orville>` e `<Orville> Captain of the Guard`, che in
  giapponese sono lo stesso 警備部隊長.
- `<Heinrich> The Iron Carnel` — refuso inglese per *Colonel*; il progetto
  aveva già deciso **`<Heinrich> il generale corazzato`** (機甲将軍).
- `<Gavela>` ha **due** etichette diverse e restano due: `Chief Developer`
  (開発主任) → «l'ingegnere capo», già del progetto; `Unscrupulous Doctor`
  (不真面目博士) → «il dottore poco serio» — ⚠️ il giapponese dice «non serio»,
  non «senza scrupoli».

Le 41 etichette stanno in `scratchpad/rese/C-attori.json` e si espandono sulle
155 voci con `_133-attori-applica.py`, che **rifiuta** se il lotto ha
un'etichetta che la tabella non copre.

### Tre punti dove l'inglese di monte dice un'altra cosa, e ha deciso il giapponese

- **scena 18 blocco 15**: l'inglese fa dire a Larnneire «Lomias, **Sevilis**!
  I'm relieved to see that you're safe» — ma Sevilis l'ha appena tradita, e il
  giapponese dice ロミアス、ヴェセル (**Bethel**). Reso col giapponese.
- **scena 11 blocco 7**: l'inglese fa *abbandonare* al ragazzo la propria
  morale («he betrayed them all»); il giapponese è una **presa di coscienza**
  («non era forse che uno strumento…»), che è anche l'unica lettura coerente
  col blocco successivo.
- **scena 115 blocco 30**: l'inglese ripete quasi parola per parola il blocco
  31; il giapponese è una battuta diversa (il vecchio che sfonda i forzieri col
  contenuto dentro). Reso col giapponese.

### Termini coniati o riusati in questo lotto

| giapponese | inglese | italiano | perché |
|---|---|---|---|
| 空間潜航 | `spatial dive` | **immersione spaziale** | la famiglia di Yerles è già decisa (glossario 122ª): 空間固定 «fissaggio spaziale», 空間干渉 «interferenza spaziale». `db_item` rendeva già 空間潜航 «immersa nello spazio» |
| ムド | `the Plant` | **il Mudo** | è un **nome proprio**, e il progetto lo porta già: `<Meshera Mudo> il semenzaio della calamità` (`db_creature`). L'inglese lo declassa a nome comune |
| 眷属 (混沌の—) | `the Servants` | **i figli del caos** | già deciso, glossario: `chat.hsp:10321` |
| 神の間 | `The Eternal Seal` | **Sigillo Eterno** | già del progetto, 52 rese |
| 混沌の巨城 | `the Cradle of Chaos` | **Culla del Caos** | già del progetto, 25 rese |
| ロストイルヴァ | `Lost Ylva` | **Irva Perduta** | già del progetto, 22 rese |
| 自律戦闘通信機 | `autonomous combat communicator` | **`<Apparato di comunicazione mobile>`** | il nome della creatura, già in `db_creature` e `db_card` |
| メカ | `mecha` | **congegno** | come la carta di Heinrich (`db_card`): «il suo passatempo è progettare congegni» |
| 鉄騎 | `the Iron Horseman` | **il cavaliere di ferro** | 《鉄騎のガルジエム》. Il nome c'era già, l'epiteto no |
| 過激派 | `radical` / `extremist` | **estremista** | 25 rese già nel progetto |
| 星の収穫 | `Star Harvesting` | **il Raccolto delle Stelle** | coniato qui. Si aggancia a «il gigante che divora le stelle», già del progetto |
| ユタス | `Yutasu` | **Yutasu** | nome proprio, invariato. Prima occorrenza nel gioco |
| 探査船アウロラ | `research vessel Aurora` | **la nave d'esplorazione Aurora** | coniato qui |

### Le intestazioni `{txt}` delle scene seguono il giapponese, non l'inglese

`同刻` → «Alla stessa ora», e **dove il giapponese non ce l'ha, l'italiano non
lo mette** anche se l'inglese scrive «Meanwhile». Così `-ザナンの皇子宿営-`
(scene 8 e 11) è «- L'accampamento del principe di Zanan -», identico alla
scena 3 che invece ha 同刻 e quindi tiene «Alla stessa ora». È la forma già
fissata dal lotto A.
