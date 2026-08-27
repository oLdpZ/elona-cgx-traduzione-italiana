# -*- coding: utf-8 -*-
"""109a - Lotto 004 di `db_item.hsp`: il rapporto degli ATTREZZI.

`FILTER_ITEM_TOOL`, `description(3)`: **166 righe del sorgente, 143 firme**.
E' la seconda categoria per peso dopo il mobilio, e la prima dove la formula
della 108a incontra una coda **quadrupla** invece che doppia.

### Le code fisse, e perche' sono quattro

Il giapponese chiude quasi ogni rapporto di questa categoria con una delle
quattro frasi che dicono **quante volte** l'oggetto si usa, e sono un fatto di
gioco, non un riempitivo: 何度でも e' illimitato, 何度か sono cariche contate,
定期的に e' un tempo di ricarica, 使い捨て e' una volta sola.

    何度でも使用することができる   ->  Si può usare sempre.
    何度か使用することができる     ->  Si può usare più volte.
    定期的に使用することができる   ->  Si può usare ogni tanto.
    使用することができる（使い捨て） -> Si usa (usa e getta).
    投げつけて使う（使い捨て）     ->  Si lancia (usa e getta).
    投げることができる             ->  Si può lanciare.

⚠️ **La coda lunga costa fino a 27 caratteri degradati su 69**, e dove il fatto
di testa non ci sta nei quaranta che restano **il modale cade**: «Si usa
sempre», «Si usa ogni tanto», «Si usa più volte». Non e' una seconda formula, e'
la stessa che si stringe — la 108a lo aveva gia' fatto sulle pergamene, dove la
testa «Una pergamena che …» cadeva a favore del verbo.

### ⚠️ Le famiglie che l'inglese distingue e il giapponese no

Come i dieci atti dei mezzi di trasporto della 108a, e per la stessa ragione —
la distinzione la porta gia' il **nome dell'oggetto**:

- **i quattro fucili anestetici** (`:42418`-`:42646`): un giapponese solo,
  「対象の体重で効果変動する麻酔銃だ」, e quattro inglesi che ci scrivono la
  fascia di peso (500-1000, 100-500, 30-100, <30 kg). Ma le fasce **sono i nomi
  degli oggetti**: TZ500-K, TZC-500, TZ30-C, TZ-30. Una resa per quattro firme;
- **le quattro carte dei semi** (`:46550`), i **quattro Potioman** (`:50477`),
  i **tre globi oscuri** (`:50948`), i **cinque nuclei di transizione**
  (`:63940`), i **tre frammenti** (`:49850`), i **quattro attrezzi da fumo**
  (`:60917`): stesso giapponese **e** stesso inglese, quindi una firma sola —
  le raggruppa gia' l'estrattore.

### ⚠️⚠️ Un difetto di monte verificato nel sorgente

**`:62023`, il lanciamissili atomico: l'inglese dice «(Reusable)» e il
giapponese 「使用することができる（使い捨て）」.** Non e' un'aggiunta, e' una
contraddizione, e stavolta non serve dedurla: `action.hsp:10130`, dentro
`EFFECT_ATOMIC_LAUNCHER`, fa `inv(INV_ITEM_NUM, ci)--`. L'oggetto **si
consuma**. Vince il giapponese, come per la razione della 108a.

### ⓘ Tre righe dove l'inglese racconta un'altra cosa, e vince il giapponese

- **`:80927`**, la statua del Creatore: il giapponese dice 「ショウルーム用」,
  *serve nella sala d'esposizione*; l'inglese racconta il Creatore del mondo del
  Moongate e che «the power is lost now»;
- **`:83081`**, l'esperienza segreta di Lomias: l'inglese dice «changes the past
  of the future», che non vuol dire niente; il giapponese dice che qualcosa
  cambiera' piu' avanti;
- **`:92392`**, il disco video: per il giapponese e' un disco con dei filmati
  incisi, per l'inglese «seem's to play your memories».

⚠️ **`:116606`, la corda robusta:** il giapponese ha **solo la coda**,
「何度でも使用することができる。」 — e l'inglese ci ha infilato la riga della
categoria («<Category: Punishment») e un «you should use them NOW!» che non c'e'
da nessuna parte. La resa e' la coda e basta.

### ⓘ «(non attivo)» si tiene, e non e' un'eccezione alla regola

`:50948` (i globi oscuri) e `:73831` (lo scanner degli effetti) hanno
«(Unimplemented)» solo in inglese. La regola di `decisioni.md` direbbe di
tacerlo, ma il dizionario ha gia' un caso identico tenuto — «You can add a
recipe … (Not implemented yet)», il cui giapponese **non** ha 未実装 e che e'
reso «(non implementato)». Le altre tre occorrenze tenute hanno 未実装 anche in
giapponese. Si tiene, nella forma piu' corta gia' in uso, «(non attivo)».

### ⓘ I termini che il lotto porta, tutti gia' decisi altrove

労働エナジー → «energia da lavoro» · フィート → «talento» · ゲージ → «barra» ·
はく製 → «statuetta» · ショウルーム → «sala d'esposizione» ·
クラムベリー → «crimberry» · 生きている武器 → «arma vivente» ·
アーティファクト → «artefatto» · 補正 → «modificatore» · ランク → «rango» ·
職業 → «classe» · 種族 → «razza» · 部位 → «parte del corpo» ·
鍵開け → «scasso» · 発言力 → «autorita'» · 名声 → «fama» · スキル → «abilita'» ·
技能 → «capacita'» · 狂気度 → «Follia» · 素材 → «materiale» · 栓 → «tappo» ·
矢弾 → «munizioni» · 味方/仲間 → «compagni» · `<Little Sister>` invariato ·
`AP`, `HP`, `MP`, `DV`, `PV`, `SP` invariati.

⚠️ **ペット non aveva una voce**, e il dizionario lo rende dieci volte
«animale» e dodici «compagno». Qui e' reso **«compagno»** in tutt'e due i posti
dove compare (`:81133` la frusta del domatore, `:85301` la macchina genetica),
perche' in Elona+ un ペット puo' benissimo essere umano e «animale» sarebbe
falso su meta' dei casi. Va in `glossario.md`.

⚠️ **Le stelle non si scrivono** (`:80221`, il martello di Garok): il giapponese
dice 「☆化する」 e ☆ e' a doppia larghezza in CP932. Si scrive quel che la
stella significa — la qualita' 4 e 5, «eccezionale».
"""
