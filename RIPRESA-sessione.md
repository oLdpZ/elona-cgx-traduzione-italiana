# Ripresa sessione

Aggiornato: 2026-08-15, fine della **quarantaquattresima** sessione.

⭐⭐ **La schermata del «Background» è CHIUSA per intero: 222 rese in cinque
lotti, tutte e cinque le righe di `*setHistory`.** È la schermata che ogni
personaggio nuovo vede alla creazione — origine, perché sei partito, un pregio,
un difetto, un vizio privato — e la stessa che `chat.hsp:8588` fa raccontare a
Mizuki su un **alleato**. Il perimetro dichiarato passa dal 53% al **54%** e il
totale vero dal 39% al **40%**: è la terza volta di fila che si muovono tutt'e
due. Catena verde fino in fondo, `cgx-test.exe` rifatto (15/08, **10:48**).

⭐⭐ **E il registro nominale non è una preferenza qui: è l'unica forma che
regge.** Le righe 3 e 4 sono mezza frase ciascuna e si tirano a sorte
**separatamente** — 45 pregi per 43 difetti, **1.935 frasi possibili** — quindi
la testa non può concordare con la coda in niente. Vedi il punto 1 delle cinque
cose e le tre voci nuove di `decisioni.md`.

⚠️ **`command.hsp` resta il file grosso: da 1.172 firme a 950.** La zona
9000-9999 passa da 179 voci a **2**.

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** (cinque spinte, una per lotto, più questa chiusura) e
l'albero di lavoro è pulito: si riparte da `git fetch && git status -sb` e dalle
otto verifiche d'apertura.
⚠️ **Due valori attesi sono cambiati**, e per lo stesso motivo di sempre:
`verifica --dizionario` dice «command.hsp: 0 da ritradurre, **950** non ancora
tradotte», e `perimetro.py` dice **54%** e **40%** dove diceva 53 e 39.
💡 **Il modello per `assembla-lotto.py` resta `scratchpad/modello-rete9.py`**:
nessuno dei cinque lotti di stanotte rinvia niente, quindi il modello non è
cambiato e non c'era motivo di sostituirlo.

1. ⭐⭐ **Ancora `command.hsp`, e adesso le zone dense sono i MENU.** Le tre più
   grosse sono **1000-1999 (156 voci)**, **6000-6999 (109)** e **2000-2999
   (103)**, e le prime due si leggono a colpo d'occhio:
   - `1000-1999` sono gli **elenchi degli alleati e dei prigionieri** —
     «Imprison who?», «Prisoner List», «Who to recall?», «Who to sell off?»,
     «Whose power will you awaken?» — con le loro intestazioni di colonna
     (`Name`, `Status`, `Value`);
   - `6000-6999` è il **banco del necromante**: «Return to the coffin», «Take
     out bone», «Take out heart», «Take out eye», «Take out blood», «Take out
     skin», più «Teach Words» e «Change Tone».
   ⭐ Sono **menu**, quindi `larghezze.py` li misura da solo: è l'opposto della
   schermata di stanotte, dove la guardia non c'era e il tetto se l'è dovuto
   costruire il lotto.
2. ⭐ **Oppure `:3556` e `:7623`, che sono ancora lì.** Due righe sole —
   `Level` e `Name` — e chiudono la scheda del personaggio, che dalla 43ª ha
   **due etichette inglesi in cima** con tutto il resto italiano. ⚠️ I budget
   sono 60 px e 38 px e stanno in `decisioni.md`: da quelle due righe non si
   vedono.
3. **Oppure il COLLAUDO**, che adesso ha **354 rese** mai viste a schermo — 132
   dalla 43ª e 222 da questa — e una schermata nuova da guardare per intera.
   Vedi la tabella più sotto. ⚠️ E gli **88 ranghi** della 41ª restano il debito
   più vecchio: non li ha ancora visti nessuno.
4. **Oppure `item_func.hsp` (263), il « of » di ogni cadavere**, col nodo
   grammaticale che la 42ª ha lasciato aperto (punto 3 delle sue cinque cose).

### ⚠️⚠️ Le cinque cose che la prossima sessione deve sapere

1. ⭐⭐ **Una schermata può PRETENDERE il registro nominale invece di
   preferirlo, e il motivo sta nel `rnd()`.** Le righe 3 e 4 del «Background»
   sono `ohanasi3` e `ohanasi4`, due `rnd(45) + 1` **indipendenti**
   (`chara.hsp:3261`-`:3262`), disegnate una sotto l'altra e lette come una
   frase sola: 45 teste per 43 code, 1.935 combinazioni. Una resa che
   concordasse la testa con la coda sbaglierebbe quasi sempre.
   ✅ **Le tre manovre che tolgono il participio dal soggetto**, e adesso hanno
   un nome perché in 222 rese tornano continuamente: il **nome astratto** («Un
   passato di schiavitù»), il **participio appeso a una cosa** («Genitori
   perduti troppo presto» — l'accordo cade su `genitori`), il **nome di genere
   fisso** («Cavia», «una creatura maledetta», «Un'arma», «Il clone»).
   ⭐ La seconda non era mai stata scritta ed è la più utile: **il participio non
   si evita, si sposta**. È la famiglia del dativo riflessivo della 40ª e del
   «ci si dorme» della 43ª, applicata al participio invece che al verbo.
   💡 E la congiunzione va **in coda**: tutte e 45 le teste finiscono in «, ma»,
   dove il giapponese mette 「〜が、」. L'inglese mette «Though» in testa, che in
   italiano vorrebbe due aggettivi accordati col soggetto.
2. ⚠️⚠️ **Il soggetto di una schermata può non essere quello che sembra, e a
   dirlo è un ALTRO file.** «You were a slave.» sembra parlare al giocatore, e
   invece `chat.hsp:8588`-`:8593` rilegge gli stessi cinque valori da
   `cdata(CDATA_BACKGROUND_PART_*, c)` e li fa raccontare a Mizuki, dove `c` è
   un **alleato** scelto con `*com_ally`. Non c'è una `lang()` gemella che
   distingua i due casi: è la stessa riga, e va bene per tutt'e due.
   💡 **La lezione generale**: prima di decidere il registro di una schermata si
   cerca chi altro legge le sue **variabili**, non chi altro chiama le sue
   `lang()`. Qui bastava un `grep ohanasi *.hsp`, e ha cambiato la resa di 222
   righe.
3. ⚠️ **Una tabella a `rnd(N)` può avere meno di N voci distinte, e nessuna
   verifica lo dice.** `*setHistory4` e `*setHistory5` dichiarano 45 valori e ne
   hanno **43**: `:9933` ripete `:9924`, `:9972` ripete `:9966`, `:10059` ripete
   `:10047`, `:10089` ripete `:10068`. Quei quattro tratti escono col **doppio**
   della probabilità degli altri.
   ✅ Per la traduzione non cambia niente — `estrai --da-tradurre` le fonde per
   firma e `applica.py` scrive la resa in tutt'e due i siti — ma è una
   **famiglia nuova** negli errori di monte: fin qui erano traduzioni sbagliate,
   questa è la tabella del gioco a essere scritta male. 💡 Chi apre un elenco a
   `rnd(N)` conti le voci distinte prima di fidarsi di N.
4. ⚠️ **Il tetto di una schermata senza guardia si può ricavare dall'INGLESE, e
   costa tre righe di Python.** Le cinque righe del «Background» si disegnano
   con `mes` dentro una finestra da 360 px, e nessuna guardia le guarda — come
   la scheda del personaggio della 43ª. Ma lì il budget era la differenza fra
   due `pos` scritte vicine; qui il valore non c'è, la riga arriva al bordo.
   ✅ Il metro è quello di `tetti_buffdesc.py`: **l'italiano contro l'inglese di
   monte**, col tetto fissato alla voce inglese più lunga dello **stesso
   gruppo** — quella la finestra la contiene già, per il fatto che upstream ci
   gira. Lo misura `scratchpad/misura-background.py`, che è un **referto**, non
   una guardia: si rilancia a mano quando si tocca uno dei cinque gruppi.
5. ⚠️ **Il giapponese ha vinto sette volte sull'inglese in una sessione sola**,
   ed è il record. Quattro sono errori di monte veri (vedi più sotto), tre sono
   appiattimenti: `:9615` 「ロマン」 è la **meraviglia** e l'inglese scrive
   «romance»; `:9672` non nomina nessuna nave e l'inglese ci mette **«the Queen
   Sedona»**; e le tre code giapponesi 「旅に出る」/「冒険に出る」/「冒険者になる」
   diventano tutt'e tre «left on adventure». 💡 Le tre code sono state rese
   diverse — «In viaggio per…», «All'avventura…», «Avventura, …» — e restituire
   una distinzione che l'inglese aveva perso è costato **zero**: bastava
   guardare la colonna giapponese prima di scrivere.

### ⚠️ La serie degli errori di monte passa da quarantotto a cinquantadue

Quattro nuovi, e una **famiglia nuova** che non è un errore di traduzione (vedi
il punto 3):

- ⭐ **il soggetto girato**: `:9873` 「熱中すると周りが見えなくなる。」 è «quando ci
  si appassiona non si vede più niente intorno», e l'inglese scrive «you drain
  the enthusiasm from those around you», cioè che l'entusiasmo lo **togli agli
  altri**. Non è una sfumatura, è il contrario;
- ⭐ **il passivo girato in attivo, che appiattisce due voci in una**: `:9978`
  「周囲からよく誤解される。」 è «gli altri ti fraintendono spesso», e l'inglese fa
  «you often misunderstand situations» — che è **quasi identico** a `:9966`
  「勘違いが激しい。」, il quale invece dice proprio «capisci fischi per fiaschi».
  Due voci diverse dell'elenco diventano la stessa;
- `:10065` 「他人を否定することが快感。」 è il piacere di **dare torto** agli altri,
  e l'inglese legge 否定 come «privare» e scrive «You enjoy denying pleasure to
  others»;
- `:9930` 「肝心なところで失敗する。」 è «sbagli nel momento decisivo», non «you
  fail at basic things»;
- 💡 minore, ma è un difetto di forma vero: **quattro code su quarantatre
  cominciano con la maiuscola** — `:9996`, `:9999`, `:10002`, `:10005` — dentro
  un elenco di code di frase dove le altre trentanove sono minuscole. In
  italiano sono minuscole tutte e quarantatre.

### ⭐ Quello che il collaudo deve guardare

`cgx-test.exe` è aggiornato (15/08, **10:48**) e contiene **354 rese** mai viste
a schermo. Resta valida tutta la tabella della 43ª più in basso, e ci si
aggiunge questa schermata — che ha il pregio di essere **immediata**: si vede
facendo un personaggio nuovo, senza dover provocare niente.

| cosa | come arrivarci | perché guardarla |
|---|---|---|
| **le cinque righe del Background** | fai un personaggio nuovo e arriva alla schermata del passato | ⭐⭐ **è la prova della sessione**. Cinque righe, 222 rese dietro |
| ⚠️ la terza e la quarta riga insieme | la stessa schermata, e premi «Reroll» qualche volta | **è il punto 1**: la terza finisce in «, ma» e la quarta ci si deve saldare. Dieci tiri diversi e si vede se la frase regge sempre |
| la larghezza delle cinque righe | la stessa schermata | ⚠️ nessuna guardia la misura: se una riga tocca il bordo della finestra, il tetto è in `decisioni.md` e si accorcia lì |
| il passato di un alleato | Mizuki, e chiedigli di farsi raccontare il passato di un compagno | ⚠️ **è l'altro lettore delle stesse righe**, ed è quello che ha deciso il registro. Se lì suona bene, suona bene ovunque |
| «Level» e «Name» sulla scheda | apri la scheda del personaggio | **devono ancora uscire in inglese**: non è un difetto, è il punto 2 della ripresa |
| gli 88 ranghi | F12 → wizard, poi iscriviti a arena/gilda/museo | ⚠️ il debito più vecchio, dalla 41ª |

### I cinque lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `command-004` | 9454-9594 | **le origini**: la famiglia, la schiavitù, il laboratorio | 46 |
| `command-005` | 9595-9732 | **le partenze**: perché sei per strada | 45 |
| `command-006` | 9733-9870 | **i pregi**, teste di frase in «, ma» | 45 |
| `command-007` | 9871-10008 | **i difetti**, code di frase minuscole | 43 |
| `command-008` | 10009-10146 | **i vizi privati**, otto dei quali «Passatempo: …» | 43 |

⭐ Sono **222 rese in una sessione**, il totale più alto dopo le 243 della 40ª,
e tutte e cinque le zone hanno dato **zero copie** a `dossier.py`: la schermata
del passato non parla la lingua di nessun'altra parte del gioco. È la prima
volta che succede per cinque zone di fila.

### 💡 Quello che i cinque lotti hanno insegnato sul metodo

⭐⭐ **Il participio non si evita, si sposta.** «You lost your parents early» non
diventa «Hai perso i genitori» per aggirare il participio: diventa «**Genitori
perduti** troppo presto», dove il participio c'è e concorda con `genitori`. Lo
stesso per «Il paese natale, **distrutto** dai mostri» e «Origini **tenute**
nascoste». ⚠️ La regola vecchia — «mai un participio riferito al giocatore» —
resta intatta: quel che cambia è che non obbliga a rinunciare al participio, ma
solo a dargli un altro referente.

⭐ **Il nome di genere fisso è la strada anche quando la persona va nominata per
forza.** Sette rese lo usano: «Cavia» (feminile), «una creatura maledetta»,
«Un'arma nata da una tecnologia proibita», «Il clone», «Un frutto nascosto»,
«Una guida forte per gli altri», «Un ex militare». 💡 E tre nomi sono
**invariabili in genere** e si possono usare tali e quali — «criminale»,
«erede», «militare» — che è la scoperta minore ma pratica: prima di girare la
frase, si guarda se il nome un genere ce l'ha davvero.

⭐ **Il registro giusto era già nel giapponese, e l'inglese lo aveva perso.**
Otto voci su 43 di `*setHistory5` sono 「趣味は…」/「…が趣味」, cioè letteralmente
«passatempo: …», e l'inglese le gira tutte in «You like to…». La resa copia il
giapponese — «Passatempo: il pisolino», «Passatempo: la caccia» — e la colonna
esce più corta e più uniforme. 💡 È la stessa lezione delle etichette di stato di
`guida-stile.md`: **la scelta neutra non è un ripiego italiano, è la forma
dell'originale**.

💡 **Zero invariati nuovi e zero toppe**: nessuna delle 222 righe ha avuto
bisogno né dell'uno né dell'altra. Sono statiche pure, senza funzioni
interpolate, e le reti 8, 10, 11 e 12 non hanno avuto niente da dire.

### 💡 I numeri

**Il perimetro dichiarato passa dal 53% al 54% e il totale vero dal 39% al 40%**:
terza volta di fila che si muovono tutt'e due, e non era mai successo. Le firme
rese passano da 12.165 a **12.387** (+222). I dizionari restano **19 su 54** —
`command.hsp` il suo ce l'aveva già dalla 43ª. Le rinviate restano **23** e le
toppe **308**: questa sessione non ne ha scritta nessuna né dell'una né
dell'altra specie. Tutti gli altri referti sono fermi: `blocchi_en` 68,
`rete8_dizionario` 3, blocchi spenti 7, `cnv_str` 17 chiavi inglesi su 41.
⚠️ **Il quadro della 38ª non cambia**: quel che resta è più grande di quel che è
stato fatto, e la parte più grossa **non ha firma `lang()`** — 5.284 descrizioni
di oggetto e 117.977 caratteri nei file di `data/`.

---

## La quarantatreesima sessione

⭐⭐ **`command.hsp` è APERTO, ed è il file che aveva indicato lo schermo.** Tre
lotti, **132 rese** e 4 rinviate: è il **diciannovesimo dizionario su 54**, e il
perimetro dichiarato passa dal 52% al **53%** mentre il totale vero passa dal 38%
al **39%** — tutt'e due, come nella 41ª. Catena verde fino in fondo:
`applica` + `compila` girati, `cgx-test.exe` rifatto (15/08, **03:56**).

⭐⭐ **E il pezzo più letto è dentro: `:13924` è UNA RIGA SOLA con ventotto
`lang()`**, cioè la domanda che il gioco fa a **ogni singola azione
sull'inventario** — «Quale oggetto vuoi posare? », «Che cosa vuoi mangiare? »,
«Che cosa vuoi agitare? ». Con `:23` («Vedi X per terra.», che parte a ogni passo
su un oggetto) e la **scheda del personaggio** al completo, questa sessione ha
tradotto tre delle schermate che si guardano più spesso in tutto il gioco.

⚠️⚠️ **La RETE 9 sbagliava lei, ed è la terza rete che si corregge.** Vedi il
punto 1 delle cinque cose. Il modello nuovo è `scratchpad/modello-rete9.py`.

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** (quattro spinte, una per lotto più la chiusura) e l'albero di
lavoro è pulito: si riparte da `git fetch && git status -sb` e dalle otto
verifiche d'apertura.
⚠️ **Due valori attesi sono cambiati**, e tutt'e due perché `command.hsp` adesso
ha un dizionario: `verifica --dizionario` ha **una riga in più**, «command.hsp: 0
da ritradurre, **1172** non ancora tradotte», e `perimetro.py` dice **53%** e
**39%** dove diceva 52 e 38.
⚠️ **Il modello da passare ad `assembla-lotto.py` non è più l'ultimo lotto**: è
`scratchpad/modello-rete9.py`. Il lotto `command-003` rinvia una riga, quindi non
ha più l'ancora `RINVIATE = set()` e non può fare da modello.

1. ⭐⭐ **Ancora `command.hsp`: restano 1.172 firme.** Le zone più dense sono
   **9000-9999 (179 voci)** e **10000-10999** (117, di cui 76 fuori dalla scheda),
   e per frequenza restano nominati dalla 42ª `:14280` « (Ground)» e `:16054`
   «You estimate this item would sell for…».
2. ⭐ **Oppure `:3556` e `:7623`, che sono due righe e chiudono la scheda.** Sono
   le prime firme di 「レベル」/`Level` e 「名前」/`Name`, e finché restano inglesi
   la scheda del personaggio ha **due etichette inglesi in cima** con tutto il
   resto italiano. ⚠️ I budget da rispettare sono quelli della scheda — 60 px e
   38 px — e da quelle due righe **non si vedono**: stanno in `decisioni.md`.
3. **Oppure il COLLAUDO**, che adesso ha 132 rese nuove e tre schermate ad alta
   frequenza da guardare. Vedi la tabella più sotto. ⚠️ E gli **88 ranghi** della
   41ª restano il debito più vecchio: non li ha ancora visti nessuno.
4. **Oppure `item_func.hsp` (263), il « of » di ogni cadavere**, col nodo
   grammaticale che la 42ª ha lasciato aperto (punto 3 delle sue cinque cose).

### ⚠️⚠️ Le cinque cose che la prossima sessione deve sapere

1. ⭐⭐ **Una TESTA di frase finisce in « and» SENZA spazio, e la rete 9
   cancellava proprio quella differenza.** Faceva
   `v['en'].rstrip().endswith(' and')`: lo `.rstrip()` rende identiche una testa
   (`" and"`, che deve chiudersi col connettivo perché una coda le si salda
   dietro) e una **congiunzione infissa** (`" and "`, che il connettivo lo è già).
   Ha bocciato « e » di `command.hsp:13`, il ciclo che elenca gli oggetti su una
   casella.
   ✅ **Misurato prima di toccarla**, ed è la parte che conta: sul dizionario
   intero ci sono **29 teste vere**, tutte in `" and"` esatto, e **una sola** voce
   in `" and "` con lo spazio — `text.hsp:11685`, infissa. Ventinove contro uno.
   💡 **È la terza rete che sbaglia lei** dopo la 8 e la 4 della 37ª, e la regola
   che ne esce è stabile: quando una rete boccia, prima si chiede *se la resa
   giusta è scrivibile*, poi *che cosa dice il sorgente su tutti gli altri siti
   della stessa specie*. Un caso non cambia una guardia; ventinove sì.
2. ⚠️⚠️ **Nessuna guardia misura la scheda del personaggio, e il metro sta nel
   sorgente.** `larghezze.py` conosce solo i menu di `*prompt_key`, `riquadri.py`
   l'HUD e le tattiche: le etichette della scheda si disegnano con `mes` a `pos`
   fisse e non le guarda nessuno. ✅ Il budget è la **differenza fra la `pos`
   dell'etichetta e quella del valore**, che il sorgente scrive a poche righe di
   distanza — nove budget misurati, dai **33 px** di `Desc:` ai **63** di
   `SpellPow`, con **~6,3 px per carattere** ricavati da `Cargo Lmt` (nove
   caratteri in 57 px). La tabella completa è in `decisioni.md`.
   💡 **Upstream abbrevia perché è stretto, e l'italiano abbrevia uguale**:
   `Prot`, `Evade`, `SpellPow`, `InSAN`, `Cargo Wt` sono già sigle. «Schivata» di
   `skill.hsp:307` vuole 46 px dove ce ne sono 43, e diventa «Schiv.» — non una
   resa nuova, la stessa tagliata dove taglia il riquadro.
3. ⚠️⚠️ **Una rinviata della rete 6 può togliere di mezzo un vincolo della rete
   4, e non era mai successo.** `:10825` e `:10837` hanno lo **stesso** giapponese
   「説明:」 e due inglesi diversi (`Hint:` e `Desc:`); la prima sta dentro
   l'`ORIGINAL` che il mod ha spento. Senza il rinvio la rete 4 avrebbe preteso
   una resa sola per tutt'e due — cioè un vincolo sulla riga **viva** imposto da
   **testo morto**. 💡 Fin qui la rete 6 serviva a non sprecare lavoro; questa
   volta ha protetto una resa.
4. ⚠️ **`estrai --da-tradurre` dà una voce per FIRMA, e per una schermata questo
   vuol dire che le sue etichette possono stare altrove.** La scheda del
   personaggio è a `:10495`-`:10526`, ma `Level` e `Name` non ci sono: le loro
   prime occorrenze sono a `:3556` e `:7623`. **Una zona non è una schermata**, e
   chi apre un lotto per zona deve chiedersi che cosa della schermata è già stato
   estratto altrove. 💡 Vale al contrario per il lavoro: quelle due righe, quando
   si faranno, chiuderanno la scheda senza che il lotto sappia di farlo.
5. ⚠️ **`applica.py` applica ogni dizionario al suo file soltanto** (la scoperta 4
   della 42ª) e questo si è visto **in positivo**: le tre gilde di `:10621`-`:10627`
   hanno la stessa firma di `init.hsp:373`-`:379`, già resa, e **non erano
   applicate** — comparivano nell'estrazione da fare. Si copiano parola per
   parola, e `dossier.py` le pesca da solo. 💡 Delle 132 rese, **una su dieci era
   già decisa altrove**: sei etichette della scheda, le tre gilde, «Non c'è nessun
   bersaglio in vista.». Cercare prima di scrivere continua a rendere.

### ⭐ Quello che il collaudo deve guardare

`cgx-test.exe` è aggiornato (15/08, **03:56**) e contiene le 132 rese. Il
salvataggio di scorta della 42ª è in `save-backup\pre-collaudo-20260815-42a`.

| cosa | come arrivarci | perché guardarla |
|---|---|---|
| **la scheda del personaggio** | aprila e basta | ⭐⭐ 41 etichette nuove in nove riquadri a larghezza stretta: **è la prova della sessione**. Se una tocca il suo valore, il budget è in `decisioni.md` e si abbrevia lì |
| ⚠️ «Level» e «Name» | la stessa schermata | **devono ancora uscire in inglese**: non è un difetto, è il punto 2 della ripresa |
| i ventotto prompt | apri l'inventario e fai qualunque cosa | posa, raccogli, mangia, bevi, leggi, compra, vendi, cucina, lancia, ruba: uno per azione |
| «Vedi X per terra.» | cammina su un oggetto | parte a ogni passo. ⚠️ Guardarla con **una pila** («3 pozioni») e con **due oggetti** sulla stessa casella, che è il caso di « e » |
| i sei giudizi sul letto | passa su un letto | «Ci si dorme benissimo!». Deve saldarsi alla riga di sopra senza attaccarsi al punto |
| i cinque barili | fai un alchimista e passa su un barile | «Baaarile...», «Bariiile~» |
| «Rank.5» | la pagina dei ranghi | ⚠️ **resta inglese ed è giusto**: è il letterale nudo di `:2901`, il quinto punto cieco della 41ª |
| gli 88 ranghi | F12 → wizard, poi iscriviti a arena/gilda/museo | ⚠️ il debito più vecchio, dalla 41ª |

### I tre lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `command-001` | 13-993 | quel che c'è per terra, i letti, i barili, il bersaglio | 37 **+3 rinviate** |
| `command-002` | 13013-14193 | **i ventotto prompt**, l'inventario, il furto | **54** |
| `command-003` | 10495-10948 | **la scheda del personaggio** | 41 **+1 rinviata** |

### 💡 Quello che i tre lotti hanno insegnato sul metodo

⭐⭐ **«Vedi X» e non «Si vede X»: a decidere è il numero.** `text.hsp:3095` rende
「がある。」 «Si vede " + s + ".», ma lì `s` è un **edificio**, sempre singolare;
qui `rtvaln` è una **pila** e porta il conteggio dentro. «Si vede 3 pozioni» è
sgrammaticato. ✅ La seconda persona con oggetto diretto non concorda con niente,
e i sei giudizi sul letto fanno lo stesso al contrario — «**ci si** dorme
comodi», dove l'accordo cade sul «si» e non sul letto. 💡 È la famiglia del
dativo riflessivo della 40ª: **si sposta l'accordo su qualcosa che la resa
controlla**.

⭐ **Due prompt di scambio, e a distinguerli è la PARTICELLA giapponese.**
「何を交換する？」 e 「何と交換する？」 differiscono per を contro と — che cosa
dai, contro che cosa ricevi — e l'inglese li appiattisce tutt'e due su *trade*,
distinguendoli solo per caso con due giri di frase. ✅ «Quale oggetto vuoi
scambiare? » e «Con che cosa vuoi fare il cambio? ».

⭐ **Il nome che non può stare nella frase esce e va fra parentesi.** Il prompt
del miscuglio vuole «l'effetto **di** valn», e `valn` è `itemname()`: è la rete 8.
✅ «Su quale oggetto applicare l'effetto? (X) », che è anche la forma del
giapponese — il quale la spiegazione la mette in parentesi tale e quale. È la
strada dei due punti del `map-005` con le parentesi al posto loro.

⚠️ **Lo stesso giapponese in due siti impone lo spazio a tutt'e due.** 「ターン」
è l'etichetta di colonna `Turns` a `:10526` e il suffisso ` Turns` dopo un numero
a `:10754`: la rete 4 pretende una resa sola. ✅ « Turni» con lo spazio — il
valore ne ha bisogno, l'etichetta lo assorbe come un rientro di tre pixel. È la
lezione del brusio del `map-005`, applicata a un'etichetta invece che a una
battuta.

💡 **Tre invariati nuovi**, tutti dichiarati in `invariati.md`: ` + ` (il segno
che unisce i due membri di una coppia, giapponese ＋ a larghezza intera), `HP/MP`
(il giapponese scrive la stessa sigla) e `AP` (giapponese 「ＡＰ」, e la colonna
ha 50 px). ⚠️ **`Karma` e `Mana` sembravano nuovi e c'erano già** — si guarda
prima di aggiungere, come diceva la 41ª.

💡 **Due strumenti parametrizzati invece che riscritti**: `scratchpad/simili.py` e
`scratchpad/gia_rese.py` erano cablati su `lavoro/_buff.jsonl` e adesso prendono
l'estrazione dal primo argomento, col vecchio percorso come default.

### 💡 I numeri

**Il perimetro dichiarato passa dal 52% al 53% e il totale vero dal 38% al 39%**:
è la seconda volta dopo la 41ª che si muovono tutt'e due. Le firme rese passano da
12.033 a **12.165** (+132). I dizionari da 18 a **19 su 54**. Le rinviate da 19 a
**23**. Le toppe restano **308** — questa sessione non ne ha scritta nessuna.
Tutti gli altri referti sono fermi: `blocchi_en` 68, `rete8_dizionario` 3,
blocchi spenti 7, `cnv_str` 17 chiavi inglesi su 41.
⚠️ **Il quadro della 38ª non cambia**: quel che resta è più grande di quel che è
stato fatto, e la parte più grossa **non ha firma `lang()`** — 5.284 descrizioni
di oggetto e 117.977 caratteri nei file di `data/`.

---

## La quarantaduesima sessione

⭐⭐ **Il COLLAUDO è stato fatto, dopo tre sessioni che lo rimandavano, e ha
risposto alla domanda della 40ª: il log di combattimento è italiano.** Poi ha
cambiato la coda del progetto, come nella 39ª — l'inglese che resta non è più
nel log, è **la cornice del mondo**, e sta quasi tutto in `command.hsp`.

⭐⭐ **E `map.hsp` è CHIUSO: 259 su 260, cinque lotti in una notte.** È il
**diciassettesimo file al 100%** e **il primo che il progetto apre e chiude
nella stessa sessione**. Il perimetro dichiarato passa dal 51% al **52%**, le
firme rese da 11.774 a **12.033**, i dizionari da 17 a **18 su 54**.
⚠️ Il totale vero resta **38%**: 259 firme non muovono quel numero.

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** e l'albero di lavoro è pulito: si riparte da
`git fetch && git status -sb` e dalle otto verifiche d'apertura.
⚠️ **Un valore atteso è cambiato**: `verifica --dizionario` adesso dice
«map.hsp: 0 da ritradurre, **1** non ancora tradotta», ed è `:1396`, rinviata
apposta (punto 2).

1. ⭐⭐ **`command.hsp`, e stavolta a dirlo è lo SCHERMO.** È la stessa cosa che
   nella 39ª fece aprire `chara_func.hsp`. La 40ª e la 41ª lo mettevano al
   secondo posto dicendo «si legge nei menu, non nel log, quindi dopo il
   collaudo»: il collaudo è arrivato e dice il contrario. Sono **1.304 firme**,
   otto o dieci lotti, e dentro ci sono:
   - `:23` **«You see X here.»**, che parte **ogni volta che cammini su un
     oggetto**;
   - `:13924`, **una riga sola con ventinove prompt** — «Which item do you want
     to pick up?», «Examine what?», «Drop what?», «Eat what?», «What do you want
     to buy?»… — cioè la domanda che il gioco fa a **ogni singola azione su un
     oggetto**;
   - `:10504` le etichette della scheda del personaggio (`Name`, `Aka`, `Race`,
     `Sex`, `Class`), `:2900` la pagina dei ranghi, `:14280` « (Ground)»,
     `:16054` «You estimate this item would sell for…».
   💡 **La scheda del personaggio non è un menu che apri una volta**: è la
   schermata che guardi più di ogni altra dopo il log, e i valori dentro sono
   **già italiani** (`Maschio`, `Nessuna`, `FOR COS DES PER APP VOL MAG CAR`).
   Manca solo la cornice.
2. **Oppure `item_func.hsp` (263), che è il « of » di ogni cadavere.** Vedi il
   punto 3 delle cinque cose: è la stringa più letta che il progetto non abbia
   mai guardato, ma ha un **nodo grammaticale da sciogliere prima** di poter
   scrivere un lotto.
3. **Oppure `termini.py`**, che dopo stanotte non è più un'idea: vedi il punto 1.
4. **Oppure gli 88 ranghi, che restano NON collaudati** — vedi «Quello che il
   collaudo deve ancora guardare».

### ⚠️⚠️ Le cinque cose che la prossima sessione deve sapere

1. ⭐⭐ **`termini.py` non è più un desiderio: stanotte è servito due volte in un
   lotto solo, e senza di lui undici rese sarebbero uscite incoerenti.**
   Nel lotto `map-003` avevo scritto 「神の間」 «Sala del Dio» e 「冥宮」
   «Palazzo dei Morti», tutti e due guardando il giapponese. ⚠️ Ma `text.hsp`
   rendeva già 神の間 **«il Sigillo Eterno»** in due righe di trama, e
   `db_creature.hsp` rendeva 冥宮の悪鬼 «il demone del **palazzo infero**».
   ✅ A trovarli è stata una ricerca per **sottostringa giapponese** dentro tutti
   i dizionari, fatta a mano in tre righe di Python.
   💡 **È il `Bolt` della 35ª in forma nuova** — una scelta presa in un file che
   torna a chiedere il conto in un altro — ma con una differenza che pesa: i due
   termini **non erano in `glossario.md`**. Stavano solo in dizionario, dove
   nessuno li cerca. La 40ª aveva già scritto che `dossier.py` non pesca i
   termini annegati dentro una frase (punto 5): questo ne è la prova sul campo.
2. ⚠️⚠️ **Un valore scritto nel salvataggio si migra dove viene CARICATO, non
   dove viene assegnato — e questa è la lezione che mi è costata due toppe.**
   `map.hsp:1396` ha la guardia che chiama la casa «Casa tua», e allargarla
   sembrava bastare. Non bastava: `:1325`-`:1344` è il bivio fra caricare e
   generare, e per una mappa **già salvata** fa `goto *map_preBegin`, saltando
   `*map_init_main` — dove la guardia sta. Casa tua è persistente: dalla seconda
   visita in poi si passa **sempre** dal ramo che salta.
   ✅ La migrazione vera sta a `:1328`, **subito dopo `gosub *game_ctrlFile`**, e
   copia il nome da `mapname()` invece di scrivere l'italiano nel sorgente.
   ⚠️ **Sono le PRIME DUE TOPPE DI MIGRAZIONE del progetto**: le altre 306
   correggono un errore di monte, queste convertono un dato vecchio.
   💡 **E a dirmi che sbagliavo è stato lo schermo**: dopo la prima toppa il log
   diceva «Entri qui: **Casa tua**.» e due righe sotto ancora «Vuoi lasciare
   **Your Home**?». Nessuna misura poteva vederlo.
3. ⚠️⚠️ **Il « of » di `item_func.hsp` è la stringa più letta che nessuno ha mai
   guardato, e il dizionario da solo non la aggiusta.**
   `item_func.hsp:1007`, `:1024` e `:1092` fanno
   `lang("", " of ") + refchara(inv(INV_ITEM_SUB_NAME, ...), DBSPEC_CHARA_NAME_ORG, 1)`,
   e coprono **ogni oggetto che porta il nome di una creatura**: cadaveri, carte,
   figurine, latte, escrementi, atti di proprietà, il fuso delle anime, il
   vomito. A schermo si legge «un cadavere **of** la mandragora zappatrice»,
   «un'urina **of** lo yeek».
   ⚠️ **E tradurre in «di» non basta**: `refchara(..., 1)` restituisce il nome
   **con l'articolo**, quindi verrebbe «un cadavere **di la** mandragora». Serve
   «della», e l'articolo sta **dentro la funzione**, dove il dizionario non
   arriva. È la rete 8 in una forma nuova: il genitivo non è una scelta da
   girare, è **incollato dalla struttura**. Il giapponese non ha il problema
   perché mette il possessore prima, con の.
   💡 `item_func.hsp` ha già **29 toppe**, tutte in forma a lista di righe: è il
   file che il progetto toppa più di ogni altro, e la strada probabile è quella.
4. ⚠️⚠️ **Una firma duplicata fra un file col dizionario e uno senza DIVERGE IN
   SILENZIO, e nessuna verifica lo dice.**
   `text.hsp:2764` e `map.hsp:1397` avevano la **stessa identica**
   `lang("わが家", "Your Home")`. Il primo era reso «Casa tua», il secondo no, e
   il giocatore leggeva i due nomi **a due righe di distanza**. La causa è
   `applica.py:618`, che applica ogni dizionario **al suo file soltanto**: la
   firma è globale, il dizionario no. La 41ª aveva incontrato lo stesso
   meccanismo in forma innocua (「性別不明」 riscritto due volte); qui produceva
   un difetto visibile.
   ⚠️ **Finché 36 file restano senza dizionario, ogni loro firma duplicata
   altrove è un difetto latente**, e nessun referto lo conta. È il candidato
   naturale al prossimo strumento dopo `termini.py`.
5. ⭐⭐ **La rete 4 ha corretto una formula della 41ª: gli spazi fanno parte
   della resa.** La 41ª aveva scritto, su クスクス, che «gli spazi attorno li
   mette **il sito**, copiando il suo inglese». Nel lotto `map-005` ho seguito
   quella frase alla lettera — «\*brusio\*» dove l'inglese diceva «\*noise\*» e
   « \*brusio\* » dove diceva « \*murmur\* », stesso giapponese 「 \*ざわざわ\* 」 —
   e **la rete 4 ha fermato il lotto**.
   ✅ Ha ragione lei: lo stesso giapponese non può avere due rese, e la
   spaziatura ne fa parte. Vince « \*brusio\* » di `db_creature.hsp:99492`.
   💡 **Perché la 41ª non se n'era accorta**: le tre rese di クスクス stavano in
   **tre file diversi**, e la rete 4 non le ha mai messe a confronto. Qui
   stavano nello stesso lotto. La formula giusta è che gli spazi li porta il
   **giapponese**, non il sito inglese.

### ⭐⭐ Quello che ha trovato il collaudo, ed è la parte che conta

**Cinque screenshot, e hanno ridisegnato le priorità.**

1. ✅ **Il log di combattimento è italiano, ed è la risposta alla domanda della
   40ª.** Rintracciate a schermo: «Il pipistrello **si rimette in piedi**»
   (`calculation.hsp:1917`, una delle due righe che avevano fatto aprire quel
   file, inglese nello screenshot della 39ª); «Il pipistrello attacca, ma
   \<Sinaha\> **schiva con maestria**» (la correzione della 39ª ad
   `action.hsp:5616` — il «Il viandante schiva Kefry» che compariva cinque volte
   in uno schermo **non c'è più**); i **sette cali del Death-Crest** tutti di
   fila (il lotto `chara_func-002` al completo); «ne fa polpette», «uccide sul
   colpo», «infligge una ferita mortale», «perde la ragione e si spegne».
2. ⚠️⚠️ **L'inglese che resta ha cambiato natura: è la cornice del mondo.**
   `command.hsp` (vedi il punto 1 della ripresa), `map.hsp` — adesso chiuso —,
   e `main.hsp:4409`, che stampa **«Purple Witch Runa was killed by butterspy in
   Plain Field»**: è la dipendenza dell'epigrafe che la 40ª aveva dichiarato
   senza poterla vedere. Adesso è vista.
3. ⚠️ **Gli 88 ranghi NON sono collaudati e non è colpa del salvataggio.**
   `command.hsp:2900` stampa un rango solo `if ( gdata(STARTING_GDATA_RANK + cnt)
   < 10000 )`, cioè **solo per le scale in cui sei iscritto**. Il personaggio di
   prova è `*Debug*`, Level 1, Fame 0, Guild Nessuna: la pagina esce **vuota**.
   ✅ Serve un personaggio con delle iscrizioni, o wizard mode (F12).
4. ⚠️ **«Rank.5» resta inglese, ed è il quinto punto cieco della 41ª visto a
   schermo.** `command.hsp:2901` fa `noteadd "" + ranktitle(cnt) + " Rank." +
   …`: letterale nudo fuori da ogni `lang()`. **Non è un difetto della resa.**

### ⭐ Quello che il collaudo deve ancora guardare

`cgx-test.exe` è aggiornato (15/08, 03:10) e contiene tutto. Il salvataggio è
in `save-backup\pre-collaudo-20260815-42a`.

| cosa | come arrivarci | perché guardarla |
|---|---|---|
| gli 88 ranghi | F12 → wizard, poi iscriviti a arena/gilda/museo | ⚠️ **il debito più vecchio**: sono della 41ª e non li ha ancora visti nessuno |
| «Vuoi lasciare Casa tua?» | ✅ **già provato e funziona** | era il difetto che ha aperto la sessione |
| i nomi delle mappe | entra e esci da una mappa qualsiasi | «Entri qui: …», «Lasci …», «Scendi le scale» |
| i quattordici Meshera | il laboratorio di armi biologiche | ⚠️ `cdatan` è nel salvataggio: quelli **già generati** restano «tester» |
| i sussurri di Amurdad | il Labirinto, con un salvataggio di scorta | ⚠️ **la cosa più discutibile della notte**: se l'enigma non si risolve più in italiano, le storpiature vanno rifatte |
| le folle del museo | dona qualcosa al museo e guarda i visitatori | sedici battute su tre righe |

### I cinque lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `map-001` | 500-1500 | i viaggi, le porte sbarrate, **il nome di casa tua** | 43 **+1 rinviata** |
| `map-002` | 1858-4210 | le mappe, i negozianti, **i quattordici Meshera** | 64 |
| `map-003` | 4210-9000 | i sotterranei, il Sigillo Eterno, i famigli | 52 |
| `map-004` | 9000-13000 | **i sussurri di Amurdad**, gli incarichi, il tempo | 51 |
| `map-005` | 13000-16000 | la fine del mondo, la prigione, le folle del museo | 49 |

⭐ Il `map-002` è il **secondo lotto più grosso del progetto** dopo le 68 del
`chara_func-003`.

### 💡 Quello che i cinque lotti hanno insegnato sul metodo

⭐⭐ **Il mestiere del negoziante non si traduce: si traduce la BOTTEGA.**
L'inglese fa «Gilbert the baker» con `sncnv()`, che prende la prima parola del
nome (`text.hsp:417`). Il primo giro del `map-002` scriveva «il tintore», «lo
stalliere», «il ricettatore» — e sarebbe stato un errore, perché **metà dei
negozianti di Elona sono femmine**. ✅ `text.hsp:420`-`:460` aveva già risolto
per **undici** mestieri seguendo il giapponese: «della panetteria», «della
locanda», «dell'armeria». Il negozio ha un genere fisso suo, chi ci lavora resta
senza. 💡 È la strada del «nome di genere fisso» della 40ª trovata **già fatta**:
bastava guardare la famiglia `sn*` invece di inventare.

⭐⭐ **Il giapponese è l'arbitro sul contenuto, ma la coerenza lo batte.**
Quattro volte ho seguito il giapponese e mi sono sbagliato: 神の間 («Sigillo
Eterno» vince), 冥宮 («palazzo infero» vince), ネヘルタード («Amurdad», il nome
inglese, vince perché è in sei righe del progetto), e `:9914`, dove la mia resa
più letterale ha perso contro «Qualcosa viene posato per terra» di `text.hsp:3`.
⚠️ **E una volta il giapponese era la fonte peggiore**: `map.hsp:5839` dice
「仮」, «provvisorio», che è un **segnaposto di sviluppo**. Lì ha vinto l'inglese.

⭐ **Un enigma storpiato va RI-storpiato, non tradotto.** I tredici sussurri di
`:10511`-`:10547` dicono quale scala prendere, e le lettere cadono in tutt'e due
le lingue: 「みぎの…どに……」 è 「右の**かど**に」 con due sillabe sparite, e
l'inglese fa «...ig...t co....r...». ✅ Tradurre la frase intera avrebbe
**regalato in italiano una risposta che altrove si paga**. Le tre righe che il
giapponese scrive intere restano intere: sono le conferme finali.
💡 È il controesempio che tiene onesto tutto il resto: il criterio non è rendere
il testo più ricco, è rendere quel che il gioco intende dire — **compreso quando
intende non dirlo**.

⭐ **Il genitivo davanti a `mapname()` si risolve mettendo il nome FUORI dalla
frase.** I nomi di area portano l'articolo dentro («la Torre Rovente», «il
Vuoto»), quindi «la superficie **di** X» e «entri **in** X» sono chiuse dalla
rete 8, e le preposizioni che non si fondono qui non servono perché il rapporto
è locativo. ✅ Tre forme nuove: «Entri qui: X.» (dopo i due punti), «X: torni in
superficie.» (in testa, che è anche l'ordine del giapponese), e soprattutto
**«Lasci X.»** — «lasciare» regge l'**oggetto diretto**, quindi la preposizione
non c'è proprio. ⚠️ Quest'ultima è la più economica e va **provata per prima**:
ha risolto anche `:11988` («da quando **hai lasciato** X») senza girare niente.
💡 E nel `map-002` il problema **non si è posto**: i nomi propri di città non
prendono l'articolo, quindi «di Derphy», «di Yowyn», «di Vernis» passano lisci.

⚠️ **`cerca`/`sostituisci` di una toppa vogliono una LISTA DI RIGHE.** Le ho
scritte due volte come stringa unica coi fine-riga dentro — prima `\n`, poi
`\r\n` — e non hanno agganciato niente: `applica_toppe` spezza il testo in righe
**da sé** (`applica.py:536`) e confronta liste. ✅ La forma a lista c'era già da
`item_func.hsp` (`applica.py:507`-`:516`). 💡 **Tutte e due le volte il guardiano
di `applica.py` ha detto «non esiste più» invece di sostituire a caso**: nessun
sorgente rotto, solo un errore in faccia.

### ⚠️ La serie degli errori di monte passa da quarantasette a quarantotto

Uno solo di famiglia nuova, ma `map.hsp` ne aggiunge una intera di **un'altra
specie**, che non è un errore ma un modo di tradurre:

- ⭐ **`map.hsp:10873` ha la riga di sopra ricopiata sopra.** Il giapponese è
  「進化プログラムの再構成を完了…。」, «riconfigurazione del programma di
  evoluzione completata», e l'inglese ci mette «Detect the abnormal material.
  ... Erase operation is complete.», che è **la riga di `:10847`**. Due cose che
  non c'entrano niente.

⚠️⚠️ **E poi c'è il quadro di `map.hsp`, che non è una serie di errori: sono
SETTE appiattimenti in un file solo.** «Hall» sta per **cinque piani diversi**;
«The Eternal Seal» per **tre stati** dello stesso posto; «moor» per la grande
palude di Merca e per una palude qualsiasi; «basement» per una cantina **e per
un covo di demoni**; «The Mine» per la miniera degli slime **e per il presidio
di Eulderna**; «It's hot!» per un'esclamazione e per una folata rovente;
**«tester» per quattordici Meshera con nome proprio**.
💡 E tre volte l'inglese non appiattisce, **butta via**: «Deep-Sea Castle» per il
castello del **drago a nove teste**, «Eulderna city» per «nei pressi del palazzo
reale», e i quattordici nomi di cui sopra.
⚠️ **Non è sciatteria isolata: è il modo in cui quel file è stato tradotto in
inglese.** Chi aprirà un file nuovo faccia girare la rete 13 aspettandosi il
peggio.

### 💡 I numeri

**Il perimetro dichiarato passa dal 51% al 52%; il totale vero resta 38%.**
Le firme rese passano da 11.774 a **12.033** (+259). I dizionari passano da 17 a
**18 su 54**. Le toppe da 306 a **308**, e le due nuove sono di **specie nuova**.
Tutti i referti restano dove li aveva lasciati la 40ª: `blocchi_en` 68,
`rete8_dizionario` 3, blocchi spenti 7, `variabili_en` 3 trappole, `cnv_str` 17
chiavi inglesi su 41.
⚠️ **Il quadro della 38ª non cambia**: quel che resta è più grande di quel che è
stato fatto, e la parte più grossa **non ha firma `lang()`** — 5.284 descrizioni
di oggetto e 117.977 caratteri nei file di `data/`.

---

## La quarantunesima sessione

⭐⭐ **Due file chiusi, `ai.hsp` e `init.hsp`, e sono il quindicesimo e il
sedicesimo al 100%.** Sei lotti — tre per file — **217 rese**, e il perimetro
dichiarato passa dal 50% al **51%** mentre il totale vero passa dal 37% al
**38%**: un punto su tutt'e due, che non capitava dalla 38ª. Catena verde,
`cgx-test.exe` rifatto (14/08, 22:45).

- **`ai.hsp` è il file più pulito che il progetto abbia mai chiuso: 94 su 94,
  zero rinviate, zero toppe.** È il file dell'intelligenza artificiale — quel che
  gli alleati e i nemici fanno da soli — e quindi **log ad alta frequenza**:
  i compagni che mangiano, bevono, frugano nello zaino, contrattano col
  negoziante, si medicano, sfondano le porte;
- **`init.hsp` è il più delicato del progetto, e si chiude con 123 rese e 10
  rinviate volute.** Ci stanno le `#defcfunc` che restituiscono inglese fuori da
  `lang()` — `he()`, `his()`, `him()`, `gendername()` — gli otto elenchi di
  ranghi, e i nove valori di `CDATAN_NEWSEX`, che sono **scritti nel
  salvataggio**.

⭐⭐ **E lo strumento ha imparato una cosa che gli mancava da ventitré lotti: la
chiave `(riga, en)` non è univoca.** Vedi il punto 1. Il modello nuovo è
`scratchpad/modello-chiave-lunga.py`, ed è provato che non cambia niente di quel
che c'era prima.

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** e l'albero di lavoro è pulito: si riparte da
`git fetch && git status -sb` e dalle otto verifiche d'apertura.
⚠️ **Un valore atteso è cambiato**: `verifica --dizionario` adesso dice
«init.hsp: 0 da ritradurre, **10** non ancora tradotte», e sono tutte e dieci
rinviate apposta (punto 3).

1. ⭐⭐ **Il COLLAUDO, e il debito è salito a 504 rese mai viste a schermo** —
   287 dalla 40ª, 217 da questa. È il doppio abbondante di qualunque debito
   precedente, ed è la terza sessione di fila che lo rimanda. ⚠️ **E adesso non
   è più solo il log di combattimento**: `ai.hsp` fa partire righe da solo
   appena hai un alleato al seguito, e `init.hsp` cambia **la scheda del
   personaggio, i ranghi e l'orologio**, che sono le prime cose che si vedono
   aprendo una partita. Vedi «Quello che il collaudo deve guardare».
2. **Oppure `command.hsp`/`trait.hsp`**, che sono ~1.680 firme e i due file
   nominati più grossi che restano. ⚠️ Si leggono nei **menu** e non nel log:
   la lezione della 26ª dice di lasciarli dopo il collaudo. `trait.hsp` da solo
   vale **406** firme.
3. **Oppure i due strumenti che il lavoro ha chiesto**, e adesso sono due:
   `termini.py` (dalla 40ª) e `rete3_dizionario.py` (dal punto 2 qui sotto).
4. **Oppure il quinto punto cieco**, se si vuole misurare invece che tradurre:
   vedi il punto 5.

### ⚠️⚠️ Le cinque cose che la prossima sessione deve sapere

1. ⭐⭐ **La chiave `(riga, en)` dei lotti non è univoca, e adesso il modello sa
   cosa farne.** Due `lang()` sulla stessa riga possono avere lo **stesso
   inglese** quando il giapponese distingue e l'inglese no. È successo quattro
   volte in due file: `ai.hsp:4576` (「変身！」 e 「トランスフォーム！」 sono
   tutt'e due `cnvtalk("Transform!")`), `init.hsp:358` («Great museum» per
   大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per
   日), `:2235` (i due punti per 時間 e per 分).
   ✅ La voce ambigua si dichiara con la **chiave lunga `(riga, en, jp)`**; le
   altre tengono quella corta, quindi **i lotti già scritti valgono tal quale**.
   La rete 0 passa da errore a referto e dice quali chiavi vogliono la forma
   lunga. ⚠️ E il controllo della rete 1 è salito **prima** delle altre reti:
   da adesso una resa mancante esce col suo messaggio invece che come `KeyError`
   nudo, che era un difetto noto dalla 38ª.
   💡 **Provato, non dedotto**: `ai-001`, `ai-002` e `calculation-001`
   rigenerati col modello nuovo danno jsonl **identici byte per byte**.
   ⚠️ La `firma` sarebbe altrettanto univoca, ma è un sha1: illeggibile in un
   file che si rilegge a mano. `ai-003` è scritto così ed è l'unico lotto del
   progetto che non passa da `assembla-lotto.py`.
2. ⭐⭐ **`battute --divergenti` legge SOLO `db_creature.hsp.jsonl`.**
   `battute.py:143` fa `percorsi.DIZIONARIO / f"{FILE}.jsonl"`: uno stesso
   giapponese reso in due modi in **due file diversi** non lo vede nessuno
   strumento. Questa sessione ne ha scritte tre apposta — 「痛っ！」, 「いいぞ！」
   e 「観光客」 — e il referto è rimasto **13**. ✅ A vederle è stata solo la
   **rete 3 dentro il lotto**, che gira mentre si scrive un lotto nuovo e **non
   è mai stata passata all'indietro** su tutto il dizionario. 💡 È la situazione
   della rete 8 prima della 37ª, quando `rete8_dizionario.py` trovò sei rese già
   entrate che stampavano «di il».
3. ⚠️⚠️ **I valori scritti nel salvataggio si RINVIANO, non si rendono
   identici — e a stabilirlo è stata la rete 7 contro `invariati.md`.** I nove
   valori di `CDATAN_NEWSEX` (`male`, `female`, `none`, `hermaphrodite`,
   `male?`, `female?`, `trans-male`, `trans-female`) sono scritti nei dati del
   personaggio e riletti come operandi di confronto in cinque file: tradurli
   farebbe sbagliare il genere di ogni personaggio già creato.
   Il primo giro del lotto `init-003` li aveva messi in dizionario **identici
   all'inglese**, che è il meccanismo descritto in `invariati.md` e usato da
   `db_creature.hsp` per `Qy@`. La **rete 7** li ha fermati tutti e nove — «riga
   1813 è un confronto, non un testo: va rinviata» — e ha ragione lei: quel
   testo di `invariati.md` è del 2026-08-07, la rete 7 è nata nel lotto `007`,
   dopo. ✅ Rinviati: la resa identica passa comunque da `applica.py`, la
   rinviata non tocca il sito nemmeno per riscriverci sopra la stessa stringa.
   💡 **E l'asimmetria con `text.hsp` è giusta, non un'incoerenza**:
   `text.hsp:123` ha la **stessa firma** e la tiene resa identica, perché lì il
   sito è un assegnamento a `strmale`, cioè testo che si stampa. **La rete 7
   guarda il sito, non la stringa.**
   ⚠️ E `applica.py:618` cicla su `dizionario/<file>.jsonl` applicando ogni
   dizionario **al suo file soltanto**: la firma è globale, il dizionario no.
   Per questo 「性別不明」 è stato riscritto in `init.hsp.jsonl` benché
   `text.hsp:363` lo avesse già.
4. ⭐ **`his(x, 1)` diventa «il suo» per tutt'e quattro i generi, e il «?» cade —
   mentre `he()` se lo tiene.** Upstream distingue `his` da `his?` e `her` da
   `her?` per dire che il genere è **dichiarato** dal personaggio e non
   accertato. In italiano il possessivo concorda col **posseduto**: «il suo»
   copre tutti, quindi il «?» segnerebbe un dubbio su una distinzione che
   l'italiano **non fa**. ✅ «il tuo» per `your`, «il suo» per gli altri quattro.
   ⚠️ Invece «lui?»/«lei?» restano, perché lì il pronome soggetto il genere lo
   distingue davvero e il dubbio ha su cosa cadere. 💡 **E l'articolo ci vuole**:
   i tre siti che già la usano sono scritti per riceverlo — `proc.hsp:8849`
   «succhi **il suo** sangue», `:9605` e `:9612` «interrompe **il suo**
   daffare» — e ognuno ha accanto un nome maschile singolare, che è quel che la
   rete 10 pretende.
5. ⚠️ **Un quinto punto cieco, trovato per caso e non ancora misurato.**
   `command.hsp:2901` e `:17848` fanno
   `noteadd "" + ranktitle(cnt) + " Rank." + gdata(...)`: **`" Rank."` è un
   letterale inglese nudo, fuori da qualunque `lang()`**, dentro l'istruzione
   che stampa. Non lo vede nessuno dei quattro referti — `blocchi_en.py` guarda
   dentro `if ( en )`, `else_jp.py` dentro `if ( jp ) … else`, `variabili_en.py`
   gli **assegnamenti** a variabile, `cnv_str_en.py` le chiavi di sostituzione —
   perché qui il letterale sta come **argomento di un `noteadd`**, senza
   condizione e senza variabile di mezzo. ⚠️ Quindi la scheda del personaggio
   dirà «Campione dell'arena **Rank.**5» per sempre, e nessun conteggio di «non
   tradotte» lo include. 💡 **Quanti siano non lo sa nessuno**: è il candidato
   naturale al referto dopo `rete3_dizionario.py`.

### ⚠️ La serie degli errori di monte passa da trentasei a quarantasette

Undici in una sessione, ed è il record. Due famiglie sono **nuove**:

- ⭐ **le battute rimescolate** (famiglia nuova): l'ordine dei `lang()` sulla
  riga è giusto, ma le coppie giapponese-inglese non si corrispondono.
  `ai.hsp:472` è il **sacco da pugni** e 「もっとぶって」 è «picchiami ancora»,
  ma l'inglese ci mette «`Release me now.`», che è la battuta del **prigioniero**
  di `:482`; `ai.hsp:658` è il **pubblico dell'arena** e le ultime due sono
  scambiate — 「頑張って！」 («forza!») porta «`Use your brain!`»;
- ⭐ **il gradino sbagliato** (famiglia nuova, tutta in `init.hsp`): `:358` mette
  «Great museum» su **due** gradini e chiama «Unknown **Ruin**» un museo;
  `:357` chiama «Famous tourist» quello che il giapponese sfotte come
  ちんけな遺跡荒らし e «Tomb robber» quello che il giapponese chiama 探検者;
  `:356` copia «New hope» da `:355` dove il giapponese dice ペットの母;
  `:362` mette **«Novice»**, che è un grado, dove va il **nome della categoria** —
  le altre sette righe ci mettono `Arena`, `Museum`, `Home`, `Shop`…;
- **il continente sbagliato**: `init.hsp:359` e `:360` dicono イルヴァ (**Irva**,
  il mondo) e l'inglese scrive «Tyris», che è il continente. Il progetto ha già
  i due nomi separati;
- **il personaggio sbagliato**: `ai.hsp:406` dice `name(tc)` dove il giapponese
  e il codice dicono `cc`;
- ⭐⭐ **e uno NEL GIAPPONESE, che è rarissimo**: `init.hsp:1973`, dentro `his()`,
  confronta 「自称男性」 dove le due funzioni sorelle `he()` (`:1830`) e `him()`
  (`:2011`) scrivono 「自称女性」. 💡 **Innocuo per un pelo**: il secondo operando
  della stessa riga è `lang("自称女性", "trans-female")`, il cui ramo giapponese
  è proprio 自称女性, quindi il caso viene preso lo stesso.

### ⭐⭐ Quello che il collaudo deve guardare

**504 rese mai viste a schermo.** Resta valida tutta la tabella della 40ª più
in basso — il log di combattimento è la prova che conta — e ci si aggiungono le
righe di questi due file. ⭐ Quelle di `init.hsp` hanno il pregio di essere
**immediate**: si vedono aprendo una partita, senza dover provocare niente.

| cosa | come arrivarci | perché guardarla |
|---|---|---|
| gli otto ranghi | scheda del personaggio, la pagina dei ranghi | **88 titoli nuovi** in otto scale. ⚠️ La prova è che la scala si senta scendere: «Campione dell'arena» → «Gladiatore invitto» → … → «Gladiatore senza nome» |
| «Cambio di rango (…)» | vendi qualcosa, o dona un oggetto al museo | è l'undicesima voce di ogni scala, cioè il **nome della categoria**: deve dire «Museo», «Gilda», «Arena delle bestie» — non un grado |
| l'orologio e la data | qualunque schermata che le mostri | sette separatori, e sei restano com'erano. L'unico che cambia è « sec» |
| «il suo sangue» | fatti succhiare il sangue da un vampiro (`proc.hsp:8849`) | è `his(x, 1)`, il possessivo che vale per tutto il gioco: se lì suona bene, suona bene ovunque |
| la scheda del personaggio | apri la scheda | ⚠️ ci si legge ancora «**Rank.**5» in inglese — è il punto 5, non un difetto della resa |
| i compagni che mangiano e bevono | cammina con un alleato al seguito e aspetta | otto righe (`ai.hsp:1009`-`:1252`) che partono da sole: «fruga nello zaino e non trova niente da mangiare» |
| la tag-team a tavola | metti due alleati in coppia e lascia mangiare uno dei due | cinque reazioni a scala d'affetto, **tutte copiate da `action.hsp`** |
| il pubblico dell'arena | porta una bestia all'arena delle bestie | otto grida, e due sono rese **contro l'inglese** |
| la canzone rumena | tieni un alleato che canta e aspetta | ⚠️ **la scelta più discutibile della sessione**: «Numa numa iei!!», poi «Numera♪ numera♪ ehi!♪», poi «Una mano♪ una mano♪ ehi!♪». Se non fa ridere, va rifatta |
| i figli che crescono | fai nascere un figlio e aspetta | cinque versi con l'accordo appeso ad «aria»: «guarda altrove con aria curiosa!» |

### I sei lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `ai-001` | 79-1468 | il sacco da pugni, il prigioniero, il pubblico dell'arena, i compagni a tavola, *Dragostea din tei* | 48 |
| `ai-002` | 1525-4525 | chi tira i sassi, il gioielliere che contratta, la tag-team, i figli che crescono | 42 |
| `ai-003` | 4576 | le quattro grida della trasformazione | 4 |
| `init-001` | 23-358 | il bottone Ok, l'errore di rete, arena, bestie, Nefia, museo | 46 |
| `init-002` | 359-390 | casa, negozio, comunità, gilda, le tre gilde, le cariche cittadine | 54 |
| `init-003` | 408-2873 | gli edifici, il genere, i possessivi, l'orologio, il log, l'errore | 23 **+10 rinviate** |

⭐ **L'`ai-002` ha la percentuale di copie più alta mai vista in un lotto: dodici
su quarantadue**, tutte pescate da `dossier.py` per **giapponese intero** — il
blocco della tag-team a tavola, che `action.hsp:1860`-`:2023` ha già parola per
parola in tre varianti. Col `ai-003`, che è **quattro copie su quattro**, la coda
di `ai.hsp` è quasi tutta lavoro già fatto altrove.

⭐ **L'`init-002` è il secondo lotto più grosso del progetto** dopo le 68 del
`chara_func-003`.

### 💡 Quello che i sei lotti hanno insegnato sul metodo

⚠️⚠️ **Gli accenti DENTRO la parola sono vietati, e nessuno l'aveva mai scritto.**
`accenti.py` degrada **ogni** accento in lettera + apostrofo, non solo quelli
finali: «élite» diventerebbe «e'lite» a schermo. Negli otto ranghi la parola era
la prima che veniva in mente — «gladiatore d'élite» — ed è stata evitata ovunque
(«Gladiatore **scelto**», «Domatore **scelto**»). 💡 Gli accenti **finali** vanno
benissimo — «piu'», «perche'», «citta'» — perché l'apostrofo lì è quello che
l'italiano scrive comunque.

⭐ **Un giapponese solo per TRE inglesi, e la resa è una sola: cambia solo lo
spazio.**  *クスクス*  è `*chuckle*` ad `action.hsp:250`, ` *Snicker* ` a
`db_creature.hsp:95622` e ` *grin* ` ad `ai.hsp:1570`: l'italiano dice
«*risatina*» in tutt'e tre, e gli spazi attorno li mette **il sito**, copiando il
suo inglese. È il rovescio della rete 13.

⭐ **«Verso» si aggiunge alle preposizioni che non si fondono, e stavolta ha
salvato una resa già decisa invece di una frase.** 「睨み付けた」 è «lanciare
un'occhiataccia» da `action.hsp:1854`-`:2011`, ma lì il bersaglio è sempre «ti»,
un clitico; ad `ai.hsp:2074` sono **due nomi**, e «un'occhiataccia **a**
name(cc)» è chiusa dalla rete 8. ✅ «lancia un'occhiataccia **verso** X»: la resa
già decisa si tiene tale e quale invece di essere girata. L'elenco della 40ª —
«con», «contro», «per», «tra», «sotto», «sopra» — prende «verso», e la lezione si
affina: la preposizione che non si fonde serve anche a **non dover riscrivere una
frase vecchia**.

⚠️ **Un titolo che il gioco appiccica al giocatore non può avere un genere.**
`init.hsp:356` gradino 7 è 「ペットの母」, «madre delle bestie», e metà dei
giocatori non sono madri. ✅ «**Balia** delle bestie»: nome di **ruolo**,
grammaticalmente femminile ma buono per chiunque, come «una guida» o «una spia».
È la strada del nome di genere fisso della 40ª usata su un titolo.

⚠️ **Tre aggettivi appesi a un nome di genere fisso.** I cinque versi dei figli
(`ai.hsp:2317`-`:2341`) in inglese sono participi che concorderebbero col figlio.
✅ «con **aria** curiosa», «con **aria** seria»: l'accordo cade su «aria».

💡 **Il file `rinviate<NNN>.py` non può portare commenti.** `assembla-lotto.py`
lo incolla al posto di `RINVIATE = set()` e poi confronta le reti col modello
carattere per carattere: un commento in coda alla riga resta nel file generato,
il modello non ce l'ha, e il confronto fallisce con «le reti NON sono
identiche». Scoperto scrivendo `init-003`. La spiegazione va nel docstring del
lotto, non lì.

💡 **Quattro invariati nuovi**, tutti dichiarati in `invariati.md`: `Ok`
(`init.hsp:23`), `/`, `:` e `h` (i separatori di data e orologio). ⚠️ **E due che
sembravano nuovi e c'erano già**: `Arena` era dichiarato dalla 30ª su
`text.hsp:2782`, e lo spazio ` ` da `text.hsp:198` (`strblank`). **Si guarda
prima di aggiungere**: il file ha 522 righe e la tabella non è in ordine.

### 💡 I numeri

**Il perimetro dichiarato passa dal 50% al 51% e il totale vero dal 37% al 38%**:
è la prima volta dalla 38ª che si muovono tutt'e due. Le firme rese passano da
11.651 a **11.774**. I dizionari restano **17 su 54** — `init.hsp` ne aveva già
uno con sei voci, `ai.hsp` è quello nuovo. Tutti i referti sono fermi dove li
aveva lasciati la 40ª: `blocchi_en` 68, `rete8_dizionario` 3, blocchi spenti 7,
`variabili_en` 3 trappole, `cnv_str` 17 chiavi inglesi su 41.
⚠️ **Il quadro della 38ª non cambia**: quel che resta è più grande di quel che è
stato fatto, e la parte più grossa **non ha firma `lang()`**.
---

## La quarantesima sessione

⭐⭐ **`chara_func.hsp` è CHIUSO, in una sessione sola.** Sei lotti — `002`…`007`
— **243 rese**, da 84 su 331 a **327 su 331**: le quattro che restano sono tutte
rinviate apposta. È il **tredicesimo file al 100%**. Catena verde,
`cgx-test.exe` rifatto.

⭐⭐ **E anche `calculation.hsp` è CHIUSO, in un lotto solo: 44 su 44, zero
rinviate.** Sono **due file chiusi in una sessione**, il tredicesimo e il
quattordicesimo del progetto, e `calculation.hsp` è il **sedicesimo dei 54 con
`lang()` ad avere un dizionario** (erano 15). Sette spinte in tutto.

⭐⭐ **Ed è la prima volta che i file si aprono e si chiudono perché l'ha chiesto
lo SCHERMO.** Né `chara_func.hsp` né `calculation.hsp` erano in un elenco di
priorità — il secondo `SPEC.md` §6 lo copre solo con la designazione collettiva
«i restanti 63 file `.hsp` minori». Ci sono finiti perché lo screenshot del
collaudo della 39ª mostrava il log ancora mezzo inglese **con `proc.hsp` al
100%**, e ogni riga inglese veniva da uno dei due.
✅ **Le tre fonti inglesi di quello screenshot sono adesso tutte chiuse**:
`proc.hsp` (39ª), `chara_func.hsp` e `calculation.hsp` (40ª). Le righe nominate
una per una — `:2021`, `:2047`, `:6441`, `:8317`, `calculation:1917`
(`stands up`), `calculation:1929` (`released from bind`) — sono tutte rese, e
**due di loro si sono chiuse copiando** una resa già scritta altrove.
💡 È la lezione della 26ª — *la frequenza, non l'elenco* — portata fino in
fondo: dieci minuti di gioco hanno deciso due file interi meglio di qualunque
conteggio di firme.

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** e l'albero di lavoro è pulito: si riparte da
`git fetch && git status -sb` e dalle otto verifiche d'apertura.

1. ⭐⭐ **Il COLLAUDO, ed è la prima volta che questa pagina lo mette al primo
   posto.** **287 rese nuove mai viste a schermo**, ed è il debito più alto mai
   accumulato in una sessione — più delle 235 della 35ª. Ma non è solo il
   numero: le tre fonti inglesi del log sono chiuse tutte e tre, quindi
   **stavolta il collaudo risponde a una domanda vera** — «il log di
   combattimento è italiano, adesso?» — e nessuna misura può rispondere al posto
   suo. Vedi «Quello che il collaudo deve guardare» qui sotto. `cgx-test.exe` è
   aggiornato (14/08) e contiene tutto, le sei toppe di `chara_func` comprese.
2. **Oppure `command.hsp`/`trait.hsp`**, che sono ~1.680 firme e i due file
   nominati più grossi che restano. ⚠️ Si leggono nei **menu** e non nel log: la
   lezione della 26ª dice di lasciarli dopo il collaudo, non prima. `trait.hsp`
   da solo vale **406** firme.
3. **Oppure `ai.hsp` (94) o `init.hsp` (133)**, che sono piccoli e già estratti.
   💡 `init.hsp` ha un interesse suo: è il file delle `#defcfunc` — `his2()`,
   `your()`, `godname()` — cioè le funzioni che **restituiscono inglese fuori da
   `lang()`** e su cui il progetto ha già tre dipendenze dichiarate.

### ⚠️⚠️ Le cinque cose che la prossima sessione deve sapere

1. ⭐⭐ **Le preposizioni che non si fondono sono la scorciatoia che il progetto
   non aveva mai dichiarato, e in questa sessione è servita quattro volte.**
   `name()` e `cdatan()` portano l'articolo dentro («il putit»), quindi «di », «a
   », «da », «in », «su » davanti a loro sono vietate — è la rete 8, che esiste
   dal lotto 009. ✅ Ma **«con», «contro», «per», «tra», «sotto», «sopra» NON si
   fondono**, e davanti a `name()` sono utilizzabili così come sono: «perse la
   vita **contro** X» (`:6850`), «si accasciò **sotto** il carico» (`:7039`), «il
   rapporto **con** X» (`:1080`), «la cera **sopra** X» (`:1169`).
   ⚠️ **E l'ha imposto la rete 8 sul campo**: `:1169` era scritta con «su», la
   rete l'ha fermata, e la correzione è stata cambiare **una parola** invece di
   riscrivere la frase. In nove lotti è il caso più economico che quella rete
   abbia mai prodotto. 💡 Fino a ieri la risposta al genitivo era sempre *girare
   la frase* — participio, `-ne` enclitico, sostanza soggetto. Adesso ce n'è una
   più a buon mercato, e va provata **per prima**.
2. ⭐⭐ **Un frammento che segue un nome vuole il PASSATO REMOTO, ed è la
   scoperta del lotto 003.** Le ventitré cause di morte si scrivono due volte:
   una riga di log che nomina chi muore, e un **frammento d'epigrafe** assegnato
   a `ndeathcause` che non nomina nessuno. `main.hsp:4409` lo incolla dentro
   «`cdatan(AKA) + cdatan(NAME) + <frammento> + " in " + mdatan(NAME)`», cioè
   subito **dopo il nome del morto**: in italiano «è morto di fame» concorderebbe
   col personaggio, e metà dei personaggi di Elona sono femmine. ✅ Il passato
   remoto italiano **non ha genere**: «morì di fame», «cadde dalle scale e morì»,
   «si tolse la vita», «bruciò fino a sparire». È la strada del participio della
   37ª spostata su un **tempo verbale**, e serve una frase intera per usarla.
   ⚠️⚠️ **E la cornice è in `main.hsp`, che non ha dizionario**: finché resta
   inglese l'epigrafe si leggerà «`<Il viandante> Sinaha morì di fame in
   Vernis`», metà e metà, con la preposizione sbagliata. È la dipendenza nota di
   `godname()` della 37ª in forma nuova. ⚠️ E quando si tradurrà la cornice:
   **il giapponese mette il luogo PRIMA del frammento e l'inglese dopo**, e
   l'italiano vuole «… morì di fame **a** Vernis».
3. ⚠️⚠️ **Il QUARTO punto cieco, e la battuta che era già morta da mesi.**
   `cnv_str` è la sostituzione di sottostringa di HSP, e il mod la usa per
   riscrivere una stringa **già composta**: `chara_func.hsp:6852` fa `cnv_str
   ndeathcause, "was killed by motuhegui", "was mauled to death by a bear"`. La
   chiave è scritta nell'**inglese di monte**, quindi appena la resa entra — o
   appena cambia una delle funzioni che compongono la stringa — non aggancia più.
   ⚠️ **Nessuno dei tre referti la vede**: `blocchi_en.py` guarda dentro
   `if ( en )`, `else_jp.py` dentro `if ( jp ) ... else`, `variabili_en.py` gli
   assegnamenti; qui non c'è nessun letterale da tradurre, c'è una **chiave che
   deve continuare a combaciare**. ✅ Misurato con **`scratchpad/cnv_str_en.py`**:
   **41 chiamate, 17 con la chiave in inglese**. ⚠️⚠️ **E quella dell'orso era
   già rotta**: `db_creature.hsp:37656` rende モツヘグイ «lo sbudellatore», quindi
   `cdatan(CDATAN_NAME, cc)` restituisce «lo sbudellatore» e la chiave non
   aggancia **da mesi**. La battuta è morta quando si è tradotto il bestiario e
   nessuna verifica l'ha detto. 💡 Le altre 15 stanno in `module.hsp` (il parser
   dei desideri) e `help.hsp`: sono **input**, non uscita, e vanno guardate
   quando si aprirà `module.hsp`.
4. ⚠️⚠️ **`:4520` è la QUARTA riga che il dizionario non può aggiustare, e la
   causa è una `lang()` che `estrai.py` NON VEDE.** `:4491` fa
   `locvar_item_cold_s = name(item_cold_arg1) + lang("の", your(item_cold_arg1))`,
   e `:4520` usa quella variabile come **prefisso**. Il ramo inglese di quella
   `lang()` è **una sola chiamata di funzione, senza letterale**: non produce
   firma — le firme di `chara_func.hsp` sono 342 e `:4491` non è fra loro —
   quindi il dizionario non la raggiunge né oggi né domani. `your()` restituisce
   `"'s"` o `"r"` (`init.hsp:2045`) fuori da `lang()`, e la riga leggerebbe «il
   putit**'s** …». ⚠️ **E la resa non può rimediare nemmeno nominando il
   proprietario**, perché il `name()` sta **dentro la variabile** e
   `funzioni_di_contenuto` non lo vede: l'inglese dichiara `['itemname']` e la
   rete 11 boccerebbe una resa che aggiunge `name()`. ✅ Toppata in due punti: il
   possessivo passa da **prefisso a suffisso** («, che X porta addosso»), che è
   la forma che l'italiano vuole comunque. 💡 **È una classe nuova da cercare
   altrove**: una `lang()` il cui ramo inglese è **solo funzioni** non compare in
   nessun conteggio, e nessuno ha mai contato quante siano.
5. ⚠️ **`dossier.py` non pesca i TERMINI, solo le frasi intere — e nel lotto 005
   sono state otto rese su trentacinque.** I sette premi di trama dicono
   「[愚者の魔石]を手に入れた！」 e `text.hsp:11576`-`:11630` aveva già reso
   **`[愚者の魔石]`**, la stessa parentesi quadra: il dossier non le aggancia
   perché confronta la **stringa intera**, e lì il termine è annegato dentro una
   frase più lunga. ✅ Trovate a mano cercando il termine. 💡 Otto su trentacinque
   è troppo per lasciarlo al caso: **è il candidato naturale al prossimo
   strumento** — un `termini.py` che cerchi le sottostringhe giapponesi del
   dizionario dentro le voci da fare.
   ⭐ **E il lotto di `calculation.hsp`, lo stesso giorno, mostra il rovescio
   esatto**: lì **sette rese su quarantaquattro** erano già decise e `dossier.py`
   le ha pescate **tutte e sette**, perché la frase giapponese coincideva per
   intero. Lo stesso strumento, i due estremi, in due lotti: **quando la frase è
   la stessa non sbaglia mai, quando il termine è annegato non vede niente.**
   Il confine è netto e si sa dov'è, ed è quello che rende lo strumento nuovo
   facile da scrivere.

### ⭐⭐ Quello che il collaudo deve guardare

**287 rese mai viste a schermo, ed è il debito più alto di sempre.**
⭐ **La prova che conta è una sola**: apri un combattimento e guarda se il log è
italiano. `proc.hsp`, `chara_func.hsp` e `calculation.hsp` sono le tre fonti
delle righe inglesi dello screenshot della 39ª e adesso sono chiuse tutte e tre
— se resta ancora inglese, viene da un file che **nessuno ha ancora sospettato**,
e trovarlo vale più di un altro lotto.

Poi le cose dove ho cambiato la struttura e non solo le parole:

| cosa | come arrivarci | perché guardarla |
|---|---|---|
| i ventidue di resistenza | bevi una pozione di mutazione, o fatti colpire da un elemento a cui resisti | «X **si sente il corpo** in fiamme», «X **si sente la pelle** avvolta in un'aura magica»: il **dativo riflessivo** è la forma nuova della sessione, e se suona male si vede subito |
| l'epigrafe della morte | muori (⚠️ **con un salvataggio di scorta**) | è l'unica riga con il **passato remoto**, e la cornice intorno sarà ancora inglese: serve a vedere quanto stona |
| il log di combattimento | un combattimento qualsiasi | ⚠️ **la prova vera della sessione**: dopo `proc.hsp` e `chara_func.hsp` il log dovrebbe essere quasi tutto italiano. Quel che resta inglese viene da `calculation.hsp` |
| «X storce il naso» | attacca un cittadino amichevole | parte a **ogni** azione ostile: è la riga più frequente di tutto il lotto 002 |
| la sella | cavalca un alleato | la parentesi si apre in una `lang()` e si chiude **undici righe dopo**, fuori da ogni traduzione: se la velocità non compare, la testa è rotta |
| il gelo sull'equipaggiamento | fatti colpire dal gelo con oggetti fragili addosso | è la **toppa** di `:4520`: deve dire «Il gelo manda in frantumi la spada, che il putit porta addosso», senza nessun «'s» |
| la sete e la fame | cammina finché non ti viene fame, e non mangiare | **quattordici** gradini nuovi, tre soglie per due bisogni: la scala deve sentirsi salire, da «Hai fame.» a «Di questo passo muori di fame!» |
| «si rimette in piedi» | fatti ribaltare, poi aspetta | è `calculation.hsp:1917`, una delle due righe che hanno fatto aprire il file: era inglese nello screenshot della 39ª |

### I sette lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `-002` | 2000-2999 | lo sguardo storto, l'ira, il velo sacro, i ventidue di resistenza | 58 **+1 rinviata** |
| `-003` | 6000-6999 | il danno, le tre urla, le ventitré morti e le loro epigrafi | **68** |
| `-004` | 4000-4999 | l'equipaggiamento aggredito dagli elementi, i sei modi buffi di morire | 33 **+2 rinviate** |
| `-005` | 7000-7999 | le ultime morti, i sette premi di trama, il cadavere da cui si scende | 35 |
| `-006` | 8000-8999 | i versi del dolore, peso e statura, il vomito, chi si sdoppia | 27 |
| `-007` | il resto | i rapporti, la tag-team, la sella, la coda sparsa | 22 |

E poi il file nuovo, chiuso in un colpo:

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `calculation-001` | tutto il file | il vortice di mana, la sete e la fame, i recuperi di stato | 44 |

⭐ **Il `-003` è il lotto più grosso mai fatto**, e batte le 59 del `proc-021`.

### 💡 Quello che i sei lotti hanno insegnato sul metodo

⭐⭐ **La duplicazione più alta mai vista in un lotto: 44 voci su 59.**
`resistmod` (`:2675`-`:2741`) e `resistmodh` (`:2769`-`:2835`) sono i due punti
da cui il gioco annuncia che una resistenza è salita o scesa — undici elementi
per due segni — e upstream li ha **ricopiati parola per parola**, cambiando solo
il nome della variabile. **Ventidue rese coprono quarantaquattro siti.** Batte il
menu delle tattiche del `proc-026` (dodici su trentaquattro) e l'X-Frame del
`-018` (nove su quarantadue). 💡 E succede di nuovo in piccolo nel `-006`:
`eatstatus` ed `eatstatusfood` sono la stessa coppia di frasi due volte.

⭐ **Il dativo riflessivo è la risposta italiana al possessivo inglese.** I
ventidue di resistenza dicono tutti 「name **の**身体は…」, 「name **の**魂は…」,
e l'inglese ci mette sopra il participio («is struck by», «is covered by»): due
trappole in una riga. ✅ «X **si sente** il corpo in fiamme», «X **si sente** la
pelle avvolta in un'aura magica» — il possesso resta implicito e la concordanza
cade su un nome di **genere fisso** («pelle» femminile, «corpo» maschile), non
sul personaggio. 💡 È la scoperta dei sedici recuperi del lotto 001 in forma
nuova: lì bastava il nome soggetto, qui serviva un costrutto che l'italiano ha e
l'inglese no.

⚠️ **La rete 13 ha gridato QUATTRO volte in un lotto solo (`-003`), ed è il
record.** «`<Medium damaged>`» per 中破 **e** 大破 (danno medio e danno grave
dello scafo, e il ramo lo conferma: `HP > MAX/4` contro `HP <= MAX/4`); «`melt
down`» per il cioccolato bollente **e** per l'acido; «`melted down`» per gli
stessi due nei frammenti; «`is healed`» per 再生した **e** 回復した. Tutt'e
quattro le distinzioni le fa il giapponese e le conferma il codice.

⚠️ **`itemname()` può essere plurale, e allora l'elemento diventa soggetto.**
`:4274`-`:4520` dicono tutte 「name の itemname は…」, e una resa come «X si vede
ridurre in cenere Y» dovrebbe accordare il verbo col **numero**, che non si
conosce. ✅ Il fuoco, il gelo e l'acido diventano **soggetti** — «Il fuoco riduce
in cenere Y», «Il gelo manda in frantumi Y» — così il verbo resta singolare
qualunque cosa arrivi, e il possesso si attacca in coda con «che X porta
addosso».

⚠️ **Un aggettivo invariabile vale quanto una frase girata.** `proc.hsp:10612`
rende 「は太った。」 «X diventa **più pesante**», e «pesante» sta bene con tutt'e
due i generi: si copia. Ma il gemello 「は痩せた。」 non può fare «più leggero»,
che **concorda**. ✅ Girato col verbo, «X perde peso», e la coppia esce
asimmetrica apposta.

⚠️ **Il gradino 1 di `txteledmg` è una CODA, e il possesso resta implicito.**
`txteledmg_arg1` vale 0, 1 o 2 — ferito, ucciso da chi attacca, morto — e il
gradino 1 il giapponese lo scrive **senza soggetto** («殺した。», «千切りにし
た。»), perché si attacca alla riga di sopra. ✅ La forma era già nel dizionario:
`:6843` dice «uccide sul colpo.» ⚠️ **E una coda italiana non può portare il
clitico** che l'inglese si concede (`him(...)`): «lo fa a listarelle»
concorderebbe.
⚠️ **Ma non è sempre una coda, e a deciderlo è l'INGLESE**: a `:4786` e `:4823`
il giapponese non ha soggetto e l'inglese ci ha rimesso un `name()`, che la rete
11 pretende. Le due forme convivono nello stesso blocco, ed è l'incoerenza di
monte che la rete propaga.

### ⚠️ La serie degli errori di monte passa da trentatré a trentasei

- ⭐ **`chara_func.hsp:8629` stampa una lettera sola.** Il giapponese è
  「name(A)の生命核はname(B)の遺伝子を獲得した。」, due personaggi; l'inglese
  scrive `name(A) + " get genes of " + _s(B) + "."`, cioè mette **`_s()` dove
  andava `name()`**. `_s()` restituisce «s» o niente, quindi la build inglese
  stampa «`X get genes of s.`» È la forma più povera della famiglia «personaggio
  sbagliato»: non ne nomina uno sbagliato, ne stampa la **desinenza**;
- `:2021` dice «`glares at you`» dove il giapponese dice solo 「嫌な顔をした」, e
  il ramo (`RELATION == 10` e basta) non sa chi sia la sorgente: l'inglese
  **nomina il giocatore** in una riga che non può saperlo;
- `:6196` scrive «`<Medium damaged>`» anche per 大破, il danno **grave**.

💡 **E tre righe dicono due cose opposte nelle due lingue**, tutte risolte sul
giapponese: `:1668` («questa creatura è perfetta da cavalcare» contro «`You feel
comfortable`» — il ramo guarda una proprietà **della bestia**), `:8007`
(「くっ！」, un mugolio, contro «`Kill me already!`») e `:7002` (闇のゲーム, il
**Gioco delle Ombre** di Yu-Gi-Oh, contro «`a card game`» con una gabbia
inventata).

💡 **Il perimetro dichiarato passa dal 49% al 50% e il totale vero dal 36% al
37%.** Le 287 rese valgono **un punto** sul conto vero: il quadro della 38ª non
cambia di una virgola — quel che resta è più grande di quel che è stato fatto, e
la parte più grossa **non ha firma `lang()`**.
💡 E i file con `lang()` che hanno un dizionario passano da **15 a 16 su 54**:
le stringhe **mai estratte** scendono da 12.620 a **12.573**. Quarantasette in
meno su dodicimila — è la proporzione vera del lavoro che resta, e serve a non
farsi ingannare da due file chiusi in un giorno.

---

## La trentanovesima sessione

⭐⭐ **`proc.hsp` è CHIUSO.** Quattro lotti — `023`, `024`, `025`, `026` — **97
rese e una rinviata a toppa**, dal 91% al **100%**: 1.091 firme su 1.098, e le
sette che restano sono tutte rinviate apposta. Si aggiunge a `db_item`,
`item_data`, `skill`, `custom_tweaks`, `adv`, `action`, `text`, `buff`,
`db_creature`, `chips` e `custom_enemyevolution` — ed è **il più letto di
tutti**, perché è il log che scorre a ogni singolo combattimento. Otto spinte,
catena verde, `cgx-test.exe` rifatto.

⭐⭐ **E poi la sessione ha fatto il collaudo, dopo tre che non lo facevano, e il
collaudo ha cambiato la coda del progetto.** Vedi «Quello che ha trovato il
collaudo» qui sotto: in un solo screenshot c'era la prova che le rese nuove
funzionano, una resa da correggere che compariva **cinque volte in uno schermo**,
e la scoperta che il log è ancora mezzo inglese **e non per colpa di
`proc.hsp`**. Da lì è partito `chara_func.hsp`, che è il file nuovo.

### ▶ Il punto esatto in cui si riprende

Tutto è **spinto** e l'albero di lavoro è pulito: non c'è niente da recuperare,
si riparte da `git fetch && git status -sb` e dalle otto verifiche d'apertura.

1. **`chara_func.hsp`, lotto 2.** Il primo (`3000-3999`, gli stati) è fatto.
   L'estrazione è già in `lavoro/_chara_func.jsonl` — **è aggiornata a prima**
   del lotto 1, quindi la prima cosa è rifarla:
   `python -m strumenti.estrai chara_func.hsp --da-tradurre --uscita lavoro/_chara_func.jsonl`
   (attese **247** voci). Poi `dossier.py` sulla zona scelta e
   `assembla-lotto.py NNN scratchpad/lotto-fase4-proc-026.py <da> <a> <cartella> chara_func.hsp`.
   💡 La zona più densa è `6000-6999` (**68**: cure, urla e tutte le cause di
   morte); la più letta dopo gli stati è `2000-2999` (**59**, e dentro ci sono
   `glares at you` e `gets furious!`, che partono a **ogni** azione ostile).
2. **Oppure `calculation.hsp`, che sono 44 voci e chiude un file intero** —
   `lavoro/_calculation.jsonl` è già estratto. Ci stanno `stands up` e
   `released from bind`, viste a schermo.
3. **Oppure il collaudo**, che resta il debito più grosso: vedi «La prima cosa
   da fare». `cgx-test.exe` è aggiornato (14/08, 18:25) e contiene tutto,
   correzione della schivata compresa. Il salvataggio è salvato in
   `save-backup\pre-collaudo-20260814-39a` **prima** che `gain_spact` lo
   modificasse.

### ⚠️⚠️ Le cinque cose che la prossima sessione deve sapere

1. ⭐⭐ **Il file da fare adesso è `chara_func.hsp`, e a dirlo è stato lo
   schermo, non una misura.** La 39ª aveva scritto in questa stessa pagina che
   dopo `proc.hsp` venivano `command.hsp`/`trait.hsp` oppure il testo fuori
   perimetro. **Lo screenshot del collaudo ha ribaltato la risposta**: con
   `proc.hsp` al 100% il log di combattimento è ancora mezzo inglese, e ogni
   riga inglese viene da `chara_func.hsp` (`glares at you`, `gets furious!`,
   `is frozen in fear`, `is incontinent`) o da `calculation.hsp` (`stands up`,
   `released from bind`). Sono le righe che si infilano **fra** una riga
   italiana e l'altra.
   💡 **`chara_func` + `calculation` = 330 firme, cinque o sei lotti**, contro
   le 1.560 di `command.hsp`, che si legge nei **menu** e non nel log. È la
   lezione della 26ª — *la frequenza, non l'elenco* — trovata guardando lo
   schermo invece che contando le firme. ✅ Il primo lotto è fatto
   (`fase4-chara_func-001`, 39 rese); ne restano **247** più le 44 di
   `calculation.hsp`.
   ⚠️ **Attenzione ai numeri di riga**: `chara_func.hsp` nella build ha
   **62 righe in meno** del sorgente (8.923 contro 8.985) per via delle toppe,
   quindi chi incrocia dizionario e build guarda la riga sbagliata di sessanta
   posizioni. È il caso di `text.hsp` della 37ª moltiplicato per sessanta: **si
   legge il `SORGENTE`**, sempre.
2. ⭐⭐ **`:24107` è la seconda riga del progetto che il dizionario non può
   aggiustare**, dopo `:11481` della 36ª, e la ragione è nuova.
   `SKILL_SPACT_JYUSOU_GOUSHIN` è dichiarata **`TARGET_TYPE_SELF_ONLY`**
   (`skill.hsp:1411`) e `proc.hsp:7565` fa **`tc = cc`**: chi lancia e chi
   subisce sono lo stesso personaggio. Il giapponese lo dice
   (「自分自身に強烈な呪いをかけた！」) e `skill.hsp:1413` lo conferma («Si
   maledice e si rafforza»). ⚠️ **L'inglese di monte invece nomina due
   personaggi**, perché è `proc.hsp:14703` — l'incantesimo Maledizione, dove i
   due sono davvero due — **ricopiata parola per parola**: a schermo stampa lo
   stesso nome due volte. 💡 **È il rovescio esatto di `:18280` della 38ª**: lì
   l'inglese aveva **un** `name()` e il giapponese due, e bastava nominare il
   soggetto; qui l'inglese ne ha **due** e il giapponese uno, e nessuna frase
   italiana nomina due volte lo stesso personaggio senza sembrare rotta.
   ✅ Toppata e rinviata. `toppe.jsonl` passa da 302 a **303**, `rinviate.jsonl`
   da 14 a **15**.
3. ⚠️⚠️ **Un inglese solo per TRE giapponesi diversi, ed è il record del
   progetto.** `:26080`, `:26120` e `:26158` hanno tutt'e tre
   «`name(cc) + " gaze" + _s(cc) + " " + name(tc) + "."`» e sono **tre azioni
   speciali diverse**: `EYE_OF_MANA` (「魔力を込めて睨み付けた」, `dmgcon
   CONDITION_MPOISON`), `EYE_OF_ILLUSION` (「幻影を見せた」, danno
   `SKILL_RES_MIND`) e `EYE_OF_STIFFEN` (「妖しい眼光を放った」, danno
   `SKILL_RES_NERVE` più `CONDITION_BIND`). L'inglese ha appiattito tre effetti
   in una riga; il giapponese e il codice li distinguono. La rete 13 è nata
   nella 37ª su una coppia: qui trova una **terna**.
4. ⭐ **Nasce un termine che servirà a un altro file: 姉波動 è l'«Onda
   Sororale».** `proc.hsp:25798`-`:25823` sono le **prime** righe del progetto
   a nominarlo, ma il grosso della materia — una catechesi intera sul culto
   delle sorelle maggiori — sta in `chat.hsp:6575`-`:6676`, che è uno dei 40
   file **senza dizionario**. ⚠️ **E l'inglese lo chiama in tre modi**: «Big
   Sister Energy», «sisterly energy», «Sistergy Wave»; il giapponese sempre
   姉波動. ✅ Messo in `glossario.md` **subito**, perché è esattamente la
   situazione del `Bolt` della 35ª — una scelta presa una volta e da applicare
   in un altro file mesi dopo.
5. ⚠️ **Il tipo della voce decide la resa, non il senso.** `:26940` è
   `lang(cdatan(CDATAN_NAME, tc) + "は矢弾を装備していない。", "You need to
   equip ammo.")`: il ramo giapponese **nomina** il personaggio, quello inglese
   no, e `estrai.py` classifica sul ramo che la resa sostituisce. Quindi è una
   **statica**, la resa è testo nudo, e **non può portare il nome** che il
   gemello `action.hsp:15268` ha — lì l'inglese era dinamico. Stessa riga, due
   tipi, due rese diverse, e la rete 3 grida per una ragione giusta.

### ⭐⭐ Quello che ha trovato il collaudo, ed è la parte che conta

**Un solo screenshot del log, e ha reso tre cose diverse.** La console di debug
lo rende possibile in dieci minuti: **F12 → `wizard`, `gain_spact`,
`gain_spell`** dà tutte le azioni speciali e tutti gli incantesimi, e senza
`gain_spact` metà delle rese della 39ª non è raggiungibile.

1. ✅ **Le rese nuove funzionano, e la toppa di `:24107` è entrata.** A schermo:
   «`Il viandante si scaglia addosso una maledizione tremenda!`» — **un nome
   solo**, che era il rischio. Più «`Il viandante porta addosso un elmo di
   bronzo [0,1], che brilla di luce nera.`», i **tre sguardi tutt'e tre
   diversi**, «`copre d'insulti`», «`ricuce il punk in un lampo!`», e le teste
   «… e» con il `-ne` enclitico in combattimento vero.
   💡 E «`Lui rispetta la legge di questa pacifica citta'.`» **non è un
   difetto**: è `he(tc, 1)`, che `init.hsp:1822` traduce già in «lui»/«lei».
2. ⚠️⚠️ **Una resa sbagliata che compariva CINQUE volte in uno schermo**, e che
   otto mesi di catena verde non avevano visto: «`Il viandante schiva Kefry.`»
   (`action.hsp:5616`). Il giapponese dice 「name(cc) **の攻撃を** 避けた」,
   cioè «l'attacco **di** cc», e l'inglese butta via 攻撃 lasciando il nome
   nudo: in inglese «X evades Y» regge, in italiano «schiva Kefry» dice
   un'altra cosa. ⚠️ E il genitivo era chiuso in partenza (rete 8: «l'attacco
   di il putit»). ✅ Corretta con la forma della 37ª — «**X attacca, ma Y
   schiva**» — **e con lei la parata due righe sopra** (`:5598`), che aveva lo
   stesso difetto e che nessuno aveva mai guardato. `:5601` e `:5619` restano:
   lì l'inglese aveva scelto il soggetto giusto.
   💡 **È la lezione della 32ª e della 36ª una terza volta**: la catena verde
   non dice niente su come suona una frase a schermo.
3. ⭐⭐ **Il log è ancora mezzo inglese, e non per colpa di `proc.hsp`** — vedi
   il punto 1 delle cinque cose. Ogni riga inglese dello screenshot è stata
   rintracciata: `chara_func.hsp:2021`/`:2033`/`:2040` (`glares at you`, e parte
   a **ogni** azione ostile), `:2047` (`gets furious!`), `:6441`, `:8317`;
   `calculation.hsp:1917` (`stands up`) e `:1929`; `command.hsp:16987`
   (`Really attack X?`) e `:17278`; `event.hsp` (venti siti identici per
   `travel experience`).

### ⚠️ La serie degli errori di monte passa da ventotto a trentatré

Tre sono della famiglia «personaggio sbagliato» e uno è di forma nuova:

- `:25071` e `:25119` dicono `name(tc)` dove ad agire è `cc` — è il
  purificatore che emette l'onda, non chi la riceve — e stanno **nella stessa
  azione, a cinquanta righe di distanza**;
- ⭐ `:25178` scrive **`name(tc)` due volte**: `name(tc) + " slashed " +
  name(tc) + " with holy power."` Il primo dei due è `cc`, lo dice il
  giapponese e lo conferma il codice, che fa partire l'animazione su `tc`. È il
  gemello di `:24107` — lì l'inglese aggiunge un personaggio che non c'è, qui
  ne sbaglia uno che c'è;
- `:24107`, la riga toppata del punto 2;
- ⭐ **`chara_func.hsp:3037`, ed è la TERZA riga del progetto che il dizionario
  non può aggiustare** dopo `proc.hsp:11481` (36ª) e `:24107`. La coppia
  「濡れた」/「姿があらわになった」 compare **tre volte** nello stesso blocco —
  chi subisce, il compagno di tag-team, chi ti cavalca — e nel ramo inglese
  dell'ultima upstream ha ricopiato quella del tag-team cambiando **due**
  riferimenti su tre: `is(gdata(GDATA_RIDER))` e `his(gdata(GDATA_RIDER))` sono
  giusti, il `name()` è rimasto `name(ttc@con)`. 💡 La rete 11 non lascia
  scampo perché `funzioni_di_contenuto` conta **`gdata` come contenuto**:
  l'inglese dichiara `['name']`, la resa giusta dichiarerebbe
  `['name', 'gdata']`. ✅ Toppata e rinviata.

💡 **E `:26948` è un difetto di un'altra classe: upstream butta via
l'informazione.** Il giapponese dice 「name は <tipo> に切り替えた。」, l'inglese
dice **«Current Ammo Type»** e basta: il tipo di munizione che `:26945` prepara
in `s` — «Normali» / «Illimitate» — nel ramo inglese **non compare da nessuna
parte**, e la resa italiana non può rimetterlo. Non è un errore, è una perdita.

### 💡 Quello che i quattro lotti hanno insegnato sul metodo

⭐ **Il lotto 026 ha la percentuale di copie più alta di tutto il file: dodici
su trentaquattro**, e otto vengono da un posto solo — `action.hsp:15232`-`:15313`,
il **menu delle tattiche**, che `proc.hsp:26858`-`:26986` ristampa parola per
parola. È l'X-Frame del lotto 018 in grande, e `dossier.py` le ha pescate tutte
e dodici senza che servisse cercarle.

⚠️ **Lo stesso giapponese può avere DUE inglesi diversi**, ed è il rovescio
della rete 13. 「パワーゲージが足りない。」 sta a `:20054` e a `:20150`, e
l'inglese lo scrive in due modi per **due soglie diverse** (5 e 50 punti di
barra). La resa è una sola, e la impone la rete 4. La differenza non la impone
il sorgente: la impone lo stile di chi ha tradotto in inglese.

⭐ **I quattro versi della necromanzia non stanno in `skill.hsp`: esistono solo
in `proc.hsp`.** 「魔力増強」, 「生命の転換」, 「外道式炸裂弾」,
「コールアンデッド」 sono le intestazioni che il gioco stampa quando scegli una
voce del menu `SKILL_SPACT_NECRO_FORCE`, e cercarle nel dizionario non dà
niente. ✅ L'ancora sono le **etichette del menu**, che `text.hsp:2089`-`:2101`
ha già rese: «Potenzia / Cura / Fai esplodere / Raduna i non-morti». 💡 E
「コールアンデッド」 si traduce lo stesso, benché sia katakana: `invariati.md`
dichiara invariato **il nome che nemmeno l'originale legge come descrizione**,
non il katakana in sé, e le altre tre della serie sono kanji che si rendono.

⚠️ **`:25206` e `:25216` sono i due rami dello stesso `if` con lo stesso
inglese.** «`name(cc) + " sewed " + name(tc) + " up quickly!"`» sta per
「縫い**つけた**」 sul nemico — e il codice mette `CONDITION_BIND` — e per
「**縫合**した」 sull'alleato, dove **dimezza** `CONDITION_BLEED`. Inchiodare e
ricucire. La rete 13 le ha viste, il codice ha deciso.

💡 **La strada del participio e quella del genitivo reggono da sette lotti**, e
in questa sessione hanno lavorato più delle reti: **diciassette rese** girate
in partenza per non far concordare un aggettivo o non far fondere una
preposizione con `name()`. La rete 8 non ha gridato **nemmeno una volta** in
quattro lotti — non perché sia stata indulgente, ma perché dopo quattro
sessioni il genitivo davanti a `name()` non si scrive più. Il caso più stretto
è `:26347`, che ne aveva **due nella stessa frase** («la voce **di** X risuona
nel cuore **di** Y»): risolto coi due nomi soggetti, «X fa risuonare la voce, e
Y la sente nel cuore!».

### ⚠️ Lo strumento che ha rischiato di mangiarsi `toppe.jsonl`

⚠️⚠️ **Uno script di questa sessione ha troncato `toppe.jsonl` a ZERO byte, e a
salvarlo è stato solo `git checkout`.** Apriva il file in scrittura e componeva
il testo dentro `write()`: un surrogato nel motivo ha fatto esplodere
`UnicodeEncodeError` **dopo** che l'apertura aveva già troncato il file. 231.878
byte di toppe, spariti per un `\ud83d` scritto a mano invece di un 💡.
✅ **La forma giusta è: comporre, codificare in memoria, e solo allora aprire.**
`riscrivi()` nello script della toppa lo fa. 💡 Ed è un'altra faccia della
regola delle due macchine: il lavoro era spinto, quindi c'era da dove tornare
indietro. Se fosse successo a fine sessione, prima della spinta, sarebbe stato
irrecuperabile.

✅ **`assembla-lotto.py` ha imparato la terza ancora, `RINVIATE`.** Il blocco
copiato dal modello porta `RINVIATE = set()`, e senza l'ancora l'unico modo di
dichiarare una rinviata era **modificare a mano il file generato** — cioè
esattamente la cosa che quello script esiste per impedire. Adesso basta un
`rinviate<numero>.py` facoltativo nella cartella.

### I quattro lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `-023` | 20000-20999 | il poker, il jolly variabile, i soldi per farsi risparmiare, il finto dogeza, il menu della necromanzia | 20 |
| `-024` | 24000-24999 | l'automaledizione, lo Scambio da squalo, la posa, la marcatura del territorio, le scosse elettriche | 13 **+1 rinviata** |
| `-025` | 25000-25999 | le onde, il filo e l'ago, l'esplosivo, la gravità, l'etere, l'Onda Sororale | 30 |
| `-026` | 26000-26999 | i tre sguardi, la voce, le pozioni, lo zaino, il menu delle tattiche | 34 |

E poi, dopo il collaudo, il primo lotto del file nuovo:

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `chara_func-001` | 3000-3999 | i dodici stati, i sedici recuperi, il bagnato | 39 **+1 rinviata** |

⭐ **È il blocco più partecipiale del progetto: l'inglese scrive DODICI stati su
dodici col participio** — «`is blinded`», «`was knocked down`», «`is
paralyzed`», «`is poisoned`»… — e in italiano concorderebbero tutti col
personaggio. Il giapponese non ha il problema perché usa 「は…た」, che è
neutro. ✅ Le due strade si dividono il lavoro a metà: il **verbo riflessivo o
intransitivo** («si addormenta», «si ubriaca», «si ammala», «cade a terra») e la
**sostanza come soggetto** («La cecità coglie X», «La paralisi coglie X», «Il
veleno invade X»). 💡 La forma «La \<cosa\> coglie X» non è nuova: era già di
`proc.hsp:13389`, ed era l'unica delle cinque già decisa.
⚠️ **E i sedici recuperi hanno il problema gemello, di genitivo**: l'inglese
dice «`X` `your(X)` `bleeding stops`», «`recover from` `his(X)` `illness`», e in
italiano diventerebbe «il sangue **di** X». Tutti girati col nome soggetto e il
possesso implicito — «X non sanguina più», «X si rimette dalla malattia».

💡 **Il perimetro dichiarato passa dal 47% al 49%**, e il totale vero resta al
**36%**: le 97 rese valgono due punti dentro `lang()` e nemmeno uno sul conto
che comprende le 5.284 descrizioni degli oggetti e i quattro file di `data/`.
Il quadro della 38ª non cambia — quello che resta è più grande di quello che è
stato fatto, e la parte più grossa **non ha firma `lang()`**.

---

## La trentottesima sessione

⭐ **La 38ª è la sessione più produttiva del progetto su un file solo, e quella
che ha scoperto quanto manca davvero.** Sei lotti su `proc.hsp` — `017`…`022` —
**285 rese, dal 65% al 91%**, otto spinte, zero collaudo. Ma la cosa che conta
non è un lotto: è che alla domanda «a che punto siamo» il progetto rispondeva
**47%** e la risposta vera è **36%**.

⭐ **E la zona densa è chiusa.** I lotti `020`-`022` hanno fatto tutto il
`21000-23999` — **156 voci in tre lotti**, il 61% di quel che restava — e `020`
e `021` sono i due lotti più grossi mai fatti (55 e 59 rese). Di `proc.hsp`
restano **98 voci**, tutte oltre la riga 20000.

### ⚠️⚠️ Le quattro cose che la prossima sessione deve sapere

1. ⭐⭐ **Il perimetro dichiarato non è il gioco: 47% e 35% sono due risposte
   diverse, e vanno tenute distinte.** Misurato con
   **`scratchpad/perimetro.py`**, che rifà il conto da capo. Dentro il perimetro
   `lang()` siamo a 10.940 firme su ~23.089, cioè **47%**. Ma due blocchi di
   testo che il giocatore legge non erano **mai stati contati da nessuna parte**:
   - **le descrizioni degli oggetti, 5.284, zero tradotte.** `db_item.hsp` le
     scrive `description(0..3) = "..."` dentro un `if ( jp ) ... else`, **non**
     dentro `lang()`: `estrai.py` non le vede, quindi non sono tradotte **e non
     risultano fra quelle da fare**. `else_jp.py` le contava come «6.840 righe
     già dichiarate fuori perimetro» senza mai dire **quante voci** fossero;
   - **i quattro file di `data/`, ~2.900 righe inglesi, zero tradotte**:
     `book.txt` (i 33 libri, **67.184 caratteri d'inglese**), `talk.txt`,
     `exhelp.txt`, `board.txt`. Il gioco li carica con `noteload` a runtime;
     `SPEC.md` §6 li chiama «aggiuntivi» e non li ha mai aperti.

   **Totale reale ~31.306, fatto il 36%** (era 35% a metà sessione: i sei lotti
   valgono un punto). ⚠️ E in **caratteri** il divario è
   peggiore: quella roba è prosa continua, non righe di log. 💡 In compenso è il
   lavoro **meno insidioso** del progetto — niente `name()` da accordare, niente
   participi, niente reti — ma vuole una **catena di strumenti diversa**, perché
   non ha firma `lang()` e non passa da `applica.py`.
2. ⭐ **Una variabile può portarsi dentro l'inglese, ed è il terzo punto cieco.**
   `proc.hsp:16980` fa `studybuddy = "your friends"` fuori da `lang()` e `:16991`
   lo interpola: la resa naturale avrebbe stampato «Cominci un circolo di lettura
   con **your friends**». ⚠️ **Non la vede nessuno dei due referti**:
   `blocchi_en.py` guarda dentro `if ( en )`, `else_jp.py` dentro
   `if ( jp ) ... else`, e quello è un **assegnamento incondizionato**.
   ✅ Misurato con **`scratchpad/variabili_en.py`**: 66 variabili, **3 trappole**
   vere. ⚠️ **La terza è ancora da fare**: `economy.hsp:319` (`s1` =
   «Neutral»/«Law»/«Chaos», in tutt'e due i rami di `lang()`). La seconda,
   `performerpal` a `:19178`, è stata schivata nel lotto 019 lo stesso giorno.
3. ⚠️⚠️ **Quattro righe dove l'inglese nomina il personaggio sbagliato**, tutte
   nel lotto 019, e ogni volta giapponese **e codice** dicono la stessa cosa
   contro di lui: `:18280` (dice `tc`, ma la riga sopra scrive in
   `cdata(cnt, CHARA_PLAYER)`), `:18309` e `:18429` (dicono `tc` dove chi agisce
   è `cc`), `:18744` (dice `tc` dove il giapponese dice `name(0)`). Con le tre
   dei lotti 017-018 la serie degli errori di monte passa da 11 a **diciannove**.
4. ⚠️ **`:18280` mostra il limite della rete 11 meglio di qualunque esempio
   finora.** La rete pretende che le funzioni di contenuto coincidano con quelle
   dell'**inglese**, e lì l'inglese ha **un** `name()` mentre il giapponese ne ha
   **due**. Quindi la resa non può nominarli tutt'e due **nemmeno sapendo che il
   giapponese ha ragione**: nomina il soggetto — quello che il codice conferma —
   e lascia implicito il resto.

### ⭐ E la scoperta dei tre lotti della zona densa

⚠️⚠️ **Le otto parole del terreno portano il loro ARTICOLO dentro.** A
`proc.hsp:22088`-`:22112` il sorgente costruisce `s` scegliendo fra otto parole —
糸/web, 闇/darkness, 酸/acid, エーテル/ether, 炎/fire, 液体/potion, 光/light,
煙/smoke — e a `:22117` la usa come **soggetto**. In italiano quelle otto hanno
**generi diversi** («la ragnatela», «l'acido», «il fuoco», «la luce»), quindi la
frase ospite non può mettere un articolo fisso: ✅ l'articolo va **dentro
ciascuna delle otto**, come `db_item.hsp` fa con `ioriginalnamearticolodet`. E la
frase dice «Quasi avesse **vita propria**», perché «Come se fosse vivo» avrebbe
concordato con `s`.
💡 **È la terza forma dello stesso problema**, dopo `itemname()` della 35ª e
`valn` da soggetto della 36ª: *una variabile che porta un nome porta anche il
suo genere, e la frase che la ospita non lo sa*.

⚠️⚠️ **`proc.hsp:21110` interpola `tc` NUDO, cioè il numero della creatura dove
va il nome**: `name(cc) + " explode with " + tc + "."`. La build inglese stampa
«explode with 37.» ⚠️ **È un candidato a toppa, non a traduzione** — la riga
andrebbe corretta `+ tc +` → `+ name(tc) +` — e finché non si fa, la rete 11
concede un solo `name()` e il bersaglio resta implicito.

⚠️ **La serie degli errori di monte è a ventotto**, e la 38ª ne ha aggiunti
diciassette. Le famiglie sono tre e adesso hanno un nome:
il **personaggio sbagliato** (`:18280`, `:18309`, `:18429`, `:18744`, `:22228`,
`:22896`, `:23613`), la **riga ricopiata da un'altra** (`:16001`, `:16679`,
`:17149`, `:21572`, `:22620`, `:22639`, `:22690`), e **un inglese per due
giapponesi** (`:17114`/`:17120`, `:21991`/`:21994`).

⚠️ **`verifica` ferma i versi delle mosse già invariate**, e succederà ancora:
`Ensemble!` (lotto 019) e `*Kamikakushi* ` (lotto 022) sono **stringhe diverse**
da `Ensemble` e `Kamikakushi`, perché il confronto è sulla stringa intera.
Vanno dichiarate a parte in `invariati.md`.

⚠️ **E una statica con una battuta fra virgolette vuole le virgolette
protette** (`\"`), come fa l'inglese di monte: una `"` nuda chiuderebbe in
anticipo la stringa HSP che scrive `applica.py`. Capitato la prima volta nel
lotto 020, sulle cinque code della spazzolatura.

💡 **Nota per chi copia le reti**: se manca una resa, il messaggio della rete 1
**non si vede mai** — la rete 8 dereferenzia `RESE` prima del controllo di
`errori`, e quel che esce è un `KeyError` nudo. Vale la pena spostare il
controllo subito dopo la rete 2.

### Le tre cose più piccole, che servono lo stesso

- 💡 **Una firma copre più siti, e il lotto 017 ne ha avuto la prova.**
  `proc.hsp` ha **due blocchi identici** per Tiro a segno (`_switch_val == 738` a
  `:16079` e `SKILL_SPACT_STRUCK_OUT` a `:16251`): il secondo non entra
  nell'estrazione, ma nel sorgente di build sono tradotti **tutt'e due**. Non
  cercare la voce mancante: non manca.
- ⚠️ **`verifica` ha fermato «Ensemble!»** per «traduzione identica
  all'inglese». Il nome della mossa era già invariato in `skill.hsp`, ma **col
  punto esclamativo è un'altra stringa** e il confronto è sulla stringa intera.
  Dichiarato in `invariati.md`. Succederà di nuovo con ogni verso di una mossa
  già invariata.
- ✅ **`dossier.py` adesso legge il `SORGENTE`**, non la build, come la 37ª
  chiedeva. (`proc.hsp` ha lo stesso numero di righe nei due alberi, quindi non
  aveva ancora ingannato nessuno.)

### I sei lotti

| lotto | zona | che cosa | rese |
|---|---|---|---|
| `-017` | 15500-16999 | navi, ricarica, muri e porte, azioni speciali di barra, meteore, cannone di sabbia, circolo di lettura | 49 |
| `-018` | 17000-17999 | scrigni, Duplibacchetta, jujitsu, X-Frame, il legame, la richiesta d'aiuto | 42 |
| `-019` | 18000-19999 | plagio, ipnosi, scansione dati, trasfusione, ensemble, pesca dimensionale, origami | 38 |
| `-020` | 21000-21999 | necromanzia, incitamento, taglialegna, spazzolatura e coccole | **55** |
| `-021` | 22000-22999 | la melma che scioglie, il magnetismo, il ranch, la stretta e il bacio | **59** |
| `-022` | 23000-23999 | polline, ShikiOrigami, tortura, i dadi del destino, le sette invocazioni di Kamui | 42 |

💡 **Il lotto 018 ha la percentuale di copie più alta di tutto `proc.hsp`: nove
su quarantadue.** Otto vengono dallo stesso posto — i versi dell'**X-Frame**
(`:17415`-`:17444`) stanno già in `action.hsp:12960`-`:12989` parola per parola,
perché il mod stampa la stessa sequenza da due punti.

⚠️ **E il 019 mostra il rovescio**: `:19303` e `:19307` hanno lo **stesso inglese**
di `proc.hsp:5332` e `:5063` ma un giapponese **diverso** — 亜空釣り è la **Pesca
dimensionale** (`skill.hsp:1608`), non la pesca normale. Copiare sull'inglese
avrebbe perso la distinzione. **Si copia sul giapponese, mai sull'inglese.**

💡 **La strada del participio regge da tre lotti**: venti rese in tutto girate
per non far concordare un participio o un aggettivo. La sostanza diventa
soggetto («Le schegge colpiscono X», «Il luccichio abbaglia X»), il verbo diventa
riflessivo («si ricarica», «cambia forma»), o l'accordo si sposta su un **nome**
(«acquista la leggerezza di una piuma», «acquista il peso di un macigno»).
⚠️ Il caso più stretto è `:19102`, la trasfusione: l'inglese dice «from X to Y» e
in italiano **tutt'e due** le preposizioni si fondono con l'articolo che `name()`
porta dentro. I tre nomi diventano soggetti — «X trasfonde il sangue: lo cede Y e
lo riceve Z».

---

## La trentasettesima sessione

⭐ **La 37ª è la sessione che ha trovato più difetti fuori dai lotti che dentro.**
Tre lotti su `proc.hsp` — `014`, `015`, `016` — **146 rese, dal 51% al 65%**, e
per arrivarci sono saltati fuori **nove difetti veri in rese già entrate**, più
**sei reti nuove o rifatte**, di cui tre sbagliavano loro. Cinque spinte.

### ⚠️⚠️ Le tre cose che la prossima sessione deve sapere

1. ⭐ **La rete 6 non vedeva i commenti di BLOCCO, e adesso sì.**
   `proc.hsp:11796` sta dentro un `/* ORIGINAL - BEGINNING ... ENDING */` — il
   codice di monte che il mod spegne per togliere il tetto ai punti bonus — e la
   rete guardava solo le righe che cominciano per `;`. ✅ Allargata con
   `scratchpad/commenti-blocco.py`, che legge il **`SORGENTE` pinnato**.
   💡 E la misura sul dizionario intero dice che era già successo: **7 voci
   tradotte stanno dentro un blocco spento** (6 in `action.hsp`, `proc.hsp:1000`).
   Non è un difetto a schermo, è lavoro speso su testo morto.
   ⚠️ **E la misura ha ingannato prima di dare il numero giusto**: fatta sulla
   **build** ne accusava 9, e le due di `text.hsp` erano giuste. Quella build ha
   **una riga in più** del sorgente (12.528 contro 12.527) perché una toppa ce
   l'ha aggiunta, e da lì in giù i numeri di riga del dizionario non tornano.
   **Chi incrocia numeri di riga e dizionario deve leggere il `SORGENTE`.**
   ⚠️ Vale anche per `dossier.py`, che oggi legge la build.
2. ⚠️⚠️ **Sei rese già entrate stampavano «di il», «a il», «in il», «su il».**
   La rete 8 è del lotto 009 (35ª) e da allora ferma i lotti nuovi, ma **nessuno
   l'aveva mai passata all'indietro**. `scratchpad/rete8_dizionario.py` lo fa:
   `action.hsp:11810`, `:12706`, `:18997` (due in una riga), `:19004`,
   `proc.hsp:1966`. ✅ Corrette. Il referto adesso dà **3**, tutti dichiarati
   falsi positivi («con» non si fonde, «hai tirato **su**» è un verbo
   sintagmatico, e `valn = skillname` non porta articolo).
   💡 Il perché `cdatan` conta quanto `name` sta in una toppa: `init.hsp:1717`
   diceva `return "the " + cdatan(...)`, la toppa toglie il `"the "`, e da lì
   `name(x)` e `cdatan(CDATAN_NAME, x)` **restituiscono la stessa stringa**,
   articolo italiano compreso.
3. ⚠️ **`verifica --dizionario` NON valida le rese**: confronta il dizionario col
   sorgente e conta orfane e non tradotte. Una correzione scritta a mano nel
   dizionario **non incontrava nessuna guardia**. ✅ Adesso gli script di
   correzione passano le rese nuove a `controlla_lotto` (vedi
   `scratchpad/correzione-rete8.py`).

### Le sei reti nuove o rifatte, e tre sbagliavano loro

| # | che cosa | il caso |
|---|---|---|
| 6 allargata | i blocchi `/* ... */` | `:11796`, vedi sopra |
| **12 nuova** | la resa di una **dinamica** dev'essere un'espressione HSP, non testo nudo | ⚠️ **l'ha trovata il compilatore, non le reti**: `:11534` è dinamica perché l'inglese porta `his(tc)`, ma in italiano la morfologia sparisce e resta una frase sola. Senza virgolette `applica.py` l'ha scritta come **codice** — `error 4`, con «qualche» letto come nome di variabile. Undici reti, `verifica` e le guardie l'avevano lasciata passare |
| **13 nuova** | un **inglese solo per due giapponesi diversi** (referto, non errore) | `:14521`/`:14573`: «The air around you gradually loses power» sta per la **fuga** e per il **ritorno**, due incantesimi diversi con due pergamene diverse |
| 8 rifatta | sbagliava lei: `valn` non è sempre un `itemname()` | a `:11893` il sorgente dice `valn = skillname(i)` due righe sopra, e i nomi di abilità non portano articolo. Adesso **legge l'assegnamento più vicino**. ⚠️ Ma a `:14755` `valn` **è** un `itemname(i, 1, 1)`: la rete aveva ragione lì |
| 4 rifatta | sbagliava lei: litigava con la rete 11 | `:12837` e `:13298` hanno lo **stesso giapponese** e un inglese che nomina **un numero diverso di personaggi**. La 11 pretende le funzioni dell'inglese, la 4 pretendeva le stesse parole: non si può, e la differenza **la impone il sorgente**. Adesso raggruppa per **(giapponese, funzioni di contenuto)** |
| 3 rifatta | gridava su rese identiche | confrontava le **espressioni**: `:12287` e `action.hsp:18755` dicono le stesse parole su variabili diverse. Adesso confronta i **letterali** e dice 💡 invece di ⚠️ |

### Le tre divergenze vecchie corrette, e una lasciata apposta

1. **«Nothing happens...»** esisteva in due rese, e una delle due è il
   `#define global txt_nothinghappens` di `text.hsp:1`, cioè quella che il gioco
   stampa **dappertutto**. `action.hsp:8936` diceva «Non succede *nulla*...».
   Vince il macro.
2. 「小さなメダル」 è **«medaglietta»** in `db_item.hsp:144256`, ma
   `action.hsp:6254` diceva «Trovi una **monetina**!»: si trovava una monetina e
   nello zaino c'era una medaglietta. ⚠️ **A sviare è l'inglese di monte**, che
   scrive `small coin` nel messaggio e `small medal` nel nome. È il `Bolt` della
   35ª in miniatura.
3. **«ha di nuovo il mana pieno» non è vero in nessuno dei due siti che lo
   dicono.** `proc.hsp:14597` ha lo stesso giapponese di `action.hsp:1096`, e il
   codice dice che pieno non lo è mai: `healmp 0, charge*5*num` di là,
   `MAX_MP/10 + rnd(...) + 5` di qua. È la lezione della 33ª — per una riga che
   descrive un effetto **l'arbitro è il codice** — su una resa che l'inglese
   («mana is restored») non bastava a smentire.
4. ⚠️ **Lasciata apposta**: 「この場所では効果がない。」 è «Qui non funziona.» a
   `action.hsp:196` e «In questo luogo non ha effetto.» a `:8552`. A distinguerli
   è **l'inglese**, e `:196` sta accanto a `:179`, che ha un giapponese diverso e
   la stessa resa breve. Non toccare.

### ⚠️ Il genitivo davanti a `name()` non esiste, e le tre zone ne chiedevano dieci

`name()` porta già l'articolo («il putit») ma non sempre («Sinaha»), quindi né
«di » né «del » funzionano. La strada è quella che `proc.hsp:8759` e `:8786`
avevano già aperto senza dichiararla — il **`-ne` enclitico** («colpisce X
facendo**ne** saltare la testa») — o il nome come **complemento oggetto**
(«attacca X puntando alla testa»). 💡 E per le tre parate del lotto 015 la forma
**«X attacca, ma Y para»** risolve tutto in un colpo: i due nomi diventano
tutt'e due soggetti, e la differenza resta dove il sorgente la mette (a mani
nude, con l'arma, con lo scudo).

💡 **Stesso problema, stessa strada, per il participio.** Nel lotto 016 undici
rese descrivono qualcosa che *succede a* `tc` e l'inglese le scrive col
participio («is hit by poison», «was showered by acid»): in italiano
concorderebbe col personaggio. La sostanza diventa **soggetto** — «Il veleno
investe X», «Il torpore prende X».

### ⚠️ Undici errori dell'inglese di monte, e la serie continua

Alle sei della 35ª questa sessione ne aggiunge cinque: `:12837` (dice che a
parare è chi attacca), `:14021` (dice `cc` dove il `cbitmod` sotto fa `tc`),
`:11870` (ricopia parola per parola la riga sopra), `:14521`/`:14573` (un inglese
per due incantesimi), `:14673` (un tanfo al posto di un mal di testa). **Tutti
raddrizzati sul giapponese**, e `verifica` lo permette perché accetta ogni
chiamata che compaia in **una delle due** forme di monte (`verifica.py:384`).

### 💡 `his2` della 36ª ha un fratello: `godname()` restituisce inglese

`god.hsp:81-89` scrive `godname(2) = lang("風のルルウィ", "Lulwy of Wind")`, e
`god.hsp` **non ha dizionario** — è uno dei 40 file mai estratti. Quindi
`proc.hsp:11749` a schermo dirà «lo sguardo benevolo di **Lulwy of Wind**» finché
non si traduce. Non è un difetto della resa, è la dipendenza nota di
`his(tc, 1)` a `:8849` in forma nuova. ⚠️ E quando si tradurrà:
`sdim godname, 20, 9` dà 20 byte, «Kumiromi del Raccolto» ne occupa 21.

💡 **Un invariante nuovo**: `proc.hsp:12101` è `"*" + skillname(efid) + "* "`,
l'intestazione dell'azione speciale. Tutto il testo viene da `skillname()`, fuori
restano due asterischi e uno spazio: dichiarato in `invariati.md`, sezione
«Versi senza contenuto linguistico».

---

## La trentaseiesima sessione

### Quello che il collaudo ha trovato, ed è la parte che conta

1. ✅ **Le dieci teste «… e» del log funzionano**, viste due volte a schermo
   («`<Sinaha> colpisce da lontano l'artista di strada e (3899) ne fa brandelli
   di carne.`»). Era il rischio più temuto della 35ª e non c'era: lo spazio lo
   mette `msgtemp += " "` a `init.hsp:1666`, che gira su **ogni** `txt`.
2. ⚠️⚠️ **La maiuscola d'ufficio non gira, e la ripresa diceva il contrario.**
   A schermo ogni riga che comincia con `name(cc)` era minuscola: «`[19:07] il
   viandante finisce di mangiare una razione.`». Il prefisso dell'orologio
   (`cfg_msgaddtime`) si attacca a `msgtemp` alla riga **1578**, cioè 81 righe
   **prima** del controllo di `:1659`, e a quel punto `peek(msgtemp, 0)` legge
   `[`. Con il timestamp acceso la maiuscola **non scatta mai, su nessuna riga,
   in nessuna lingua** — nemmeno per l'inglese di monte, che scrive «`you finish
   eating.`». ✅ Toppato maiuscolando subito dopo `tnew = 0` (`init.hsp:1568`),
   prima che i prefissi si attacchino, con le stesse due guardie dell'originale.
   **Riguardato a schermo: «`Il viandante finisce di mangiare una razione.`»**
3. ⚠️ **`valn` da soggetto vuole il determinativo, e `itemname()` non lo dà.**
   A schermo: «`Un pozzo disseta <Sinaha>.`» `itemname()` mette il determinativo
   **solo agli artefatti identificati** (`item_func.hsp:1944`) e
   l'indeterminativo a tutto il resto: è il calco di `a well` / `the Painful
   Master`. Da complemento andava bene, da soggetto no. ✅ Toppato usando
   `ioriginalnamearticolodet` — **1.309 articoli determinativi già in
   `db_item.hsp`, mai usati così** — più `itemname(ci, 1, 1)`, che è l'idioma con
   cui upstream chiede il nome nudo.

> 💡 **Il filo delle ultime tre sessioni, in tre forme.** La 34ª: la catena
> verde non dice niente sulla lingua che il giocatore legge. La 35ª: non dice
> niente sulla coerenza fra due file. La 36ª: **non dice niente su un'opzione
> del giocatore.** Nessuna verifica accende `cfg_msgaddtime`, e il difetto viveva
> o moriva su una casella delle impostazioni.

### ⚠️ Il pozzo NON è stato riguardato a schermo

La toppa è compilata e installata dalle 11:34, ma al collaudo il personaggio era
troppo pieno per bere e il messaggio non è mai partito. **È la prima cosa da
fare aprendo il gioco**: cammina finché non ti viene sete, poi `h` su un pozzo.

| cosa | atteso |
|---|---|
| bevi al pozzo | `Il pozzo disseta il viandante.` |
| bevi alla fontana | `La fontana disseta il viandante.` (prova che il genere segue) |
| pozzo prosciugato | `Il pozzo non ha più acqua.` |
| benedici l'equipaggiamento | `<nome> ha l'equipaggiamento avvolto in una luce bianca.` (toppa `his2`) |

💡 `You see un pozzo placed here.` **è giusto così**: è `command.hsp:30`, un sito
diverso dove il pozzo è complemento oggetto. La toppa tocca solo `*drinkWell`.

### Le tre reti nuove, e una che era sbagliata

⭐ **Rete 11 — le funzioni di contenuto devono coincidere, e non se ne può
AGGIUNGERE nessuna.** `verifica.py:367` confronta `funzioni_di_contenuto` di
inglese e resa: stesse funzioni, stesso ordine. Il caso che l'ha imposta è
`:10312`, dove l'inglese ha solo `his(tc)` (morfologia, zero contenuto) e il
giapponese invece **nomina il soggetto**: la resa italiana non può nominarlo.
⚠️ **Ed è nata sbagliata**: girava anche sulle statiche dentro `cnvtalk()`, dove
l'`en_grezzo` porta l'involucro ma la resa è testo nudo — avrebbe bocciato
**undici rese giuste**. Ora gira solo sulle dinamiche, che è dove `verifica.py`
la mette.
⭐ **E si è guadagnata il posto un lotto dopo**, bocciando `:11481` con
«mancanti `['his2']`»: vedi la rinviata qui sotto.

💡 **Rete 10** — `his(x, 1)` è contenuto e resta, ma in italiano varrà «il suo» /
«il tuo» per **tutti** i siti, perché la funzione sceglie sul genere del
**possessore** mentre l'italiano accorda col **posseduto**. Quindi ogni sito che
la usa deve metterle accanto un **nome maschile singolare**. La 35ª l'aveva già
rispettato senza dirlo (`:8849`, «sangue»); la rete adesso stampa il nome retto.

💡 **Rete 4 rifatta**: confrontava le rese di uno stesso giapponese come
**espressioni** e avrebbe bocciato `:9605`/`:9612`, che dicono le stesse identiche
parole su due variabili diverse. Adesso confronta i **letterali di testo**.

### ⚠️ La rinviata: `his2()` non è traducibile, e non per il motivo che sembrava

`init.hsp:1881`:

```hsp
#defcfunc his2 int EntityID
    if ( EntityID == CHARA_PLAYER ) { return "your" }
    return name(EntityID)
```

**Porta il nome** — per questo è contenuto e `verifica` pretende che resti — ma
nel ramo del giocatore restituisce il letterale nudo `"your"` **fuori da
`lang()`**. Quel «your» resta inglese per sempre: non lo raggiunge il dizionario
oggi e non lo raggiungerà la traduzione di `init.hsp` domani, perché non c'è
niente da tradurre. Stessa classe di `bufftxt(1)` della 28ª. ⚠️ **E nessuna resa
regge tutt'e due gli esiti**, perché `his2()` dà un **possessivo** in un caso e un
**nome con l'articolo** nell'altro. Quindi `proc.hsp:11481` è **rinviata a
toppa**, e la toppa è fatta.

💡 **Da qui una domanda aperta e misurabile**: `blocchi_en.py` conta i letterali
inglesi nudi **nel sorgente**, ma non quelli che escono da una **funzione** come
`his2()`. Nessuno ha mai contato le `#defcfunc` di `init.hsp` che restituiscono
inglese senza `lang()`. `his2` e `your2` sono due; quante sono in tutto?

### Nuovo strumento: `scratchpad/dossier.py`

Mette insieme le tre letture che ogni lotto rifaceva a mano — il sorgente
intorno alla riga, le rese gemelle per **giapponese**, quelle per **inglese**.
Sui tre lotti ha pescato **undici copie** da non ridecidere: `Tyris del Nord`,
`Tyris del Sud`, `Irva Perduta`, `filtro d'amore`, `benzina`, `olio essenziale`,
`coppia`, `non morti`, `spazzatura`, `Grazie!`, più due rese di `proc.hsp`
stesso. È la regola «cercare prima di scrivere» resa meccanica.

⭐ **La 35ª è stata la sessione più produttiva del progetto su un file solo:
`proc.hsp` passa da 207 rese a 442, cioè da 19% a 40%,** in sei lotti
(`fase4-proc-005` … `-010`) più una correzione. **235 rese, 298 siti**, sette
spinte, zero regressioni. Quello che ha trovato conta più dei numeri:

1. ⭐ **`valn` è un `itemname()`** (`proc.hsp:6950`, `:6965`, `:6970`), quindi
   porta l'articolo italiano e non regge `di`/`da`/`in`/`su` davanti. L'inglese
   ce ne mette quattro in una zona sola. È la scoperta di `itemname()` del lotto
   005 **travestita da variabile**: guardando la riga non c'è modo di saperlo.
2. ⭐ **Una regola scritta e non sorvegliata**: `glossario.md` dice `Bolt` →
   «Saetta» dal 2026-08-09, e `db_item.hsp` diceva «dardo» in **15 nomi**. Si
   comprava il libro del *dardo* e si imparava la *saetta*. Non è una decisione
   presa due volte: è una decisione presa una volta e **mai applicata**, perché
   **nessuno strumento confronta il glossario col dizionario**.
3. ⚠️ **Sei errori dell'inglese di monte**, tutti raddrizzati sul giapponese:
   due code scambiate a `:4872`, un «robs **me**» a `:4906`, `name(tc)` per
   `name(cc)` a `:6200`, «cliche» per 王道 a `:6148`, «regretted being born» per
   una frase che parla d'allucinazioni a `:6876`, e «The ball hits» copiato su un
   fulmine a `:8334`.
4. ⚠️ **Due voci che non erano testo**: `:5584` «Merchant ship» e «Pirate ship»
   sono **operandi di confronto** con `map.hsp`. È la seconda «Party Room» dello
   stesso file.
5. 💡 **Cinque reti nuove** negli script dei lotti (5-9), e **ognuna nasce da un
   caso reale di questa sessione**, non da un'idea.

💡 **Il filo che le tiene insieme**: la 34ª aveva mostrato che la catena verde
non dice niente sulla lingua che il giocatore legge. La 35ª mostra il gemello —
**la catena verde non dice niente sulla coerenza fra due file**. Il `Bolt` stava
lì da otto mesi con tutte le verifiche a posto.

### ⚠️ Il debito di collaudo è tornato a salire, ed è la cosa da sapere

**235 rese nuove e nessuna vista a schermo.** La 34ª aveva fatto scendere il
debito per la prima volta; questa lo raddoppia. `cgx-test.exe` è rifatto e
aggiornato (14/08, 10:30), quindi il collaudo si può fare subito, e la roba nuova
è **facile da vedere**: dormire, mangiare, pescare, scavare, viaggiare sulla
mappa e un combattimento qualsiasi coprono quasi tutta la zona 3401-9200.

💡 **Da guardare per primi, perché sono quelli dove ho cambiato la struttura e
non solo le parole:**

| cosa | dove esce | perché guardarla |
|---|---|---|
| il pozzo e la fontana | bevi a un pozzo, cadici dentro | `valn` è diventato **soggetto**: «Il pozzo disseta il viandante» invece di «beve dal pozzo». Se l'articolo sbaglia si vede subito |
| le teste «… e» del log | un combattimento qualsiasi | dieci rese si saldano alla coda di danno di `chara_func.hsp`. Basta uno spazio storto e si legge «colpisce il putit einfligge una ferita» |
| il portello del rifugio | usa un rifugio portatile | l'unica resa dove ho girato la frase per togliere un «di » + `itemname` |
| i sei gradini della sazietà | mangia sei volte con fame diversa | venti rese pescate a caso; è dove l'accordo di genere rischiava di più |
| `his(tc, 1)` a `:8849` | fatti succhiare il sangue da un alleato | ⚠️ **stamperà ancora `his`/`her`/`your`** finché `init.hsp` non è tradotto. Non è un difetto della resa, è la dipendenza nota |

## ⚠️ Prima di tutto: il progetto vive su due macchine

**La 29ª è stata fatta dal portatile**, non dalla macchina di Firenze. È la prima
volta, e va saputo perché spiega tutto quello che sembrava rotto: all'apertura
**nessuno strumento partiva**, c'erano solo Python **3.7** (Anaconda) e **3.8**,
e gli strumenti usano `str | None`, quindi `strumenti.creature` moriva alla riga
67 prima di leggere un file. Non era un guasto e non era una macchina ripulita:
era **una macchina dove non era mai stato installato niente**. Idem per Elin,
l'identità git e i plugin.

**Risolto installando Python 3.12.10** (`winget install Python.Python.3.12
--scope user`) più `pytest`. Se succede di nuovo, il sintomo è
`TypeError: 'type' object is not subscriptable`, e non è un guasto del codice.

⚠️ **Da qui nasce il rischio vero: le due copie possono divergere.** All'inizio
della 29ª `origin/fase-0` era fermo a `8a10f82`, cioè **38 commit indietro**:
tutto il lavoro dalla 26ª in poi — 1.089 battute più i 71 `buffname` — stava
solo sul disco del portatile. È la stessa trappola della 28ª (lavoro fuori da
git), in una forma nuova: dentro git, ma su una macchina sola.

💡 **La regola: si spinge a fine sessione, sempre**, e la prima cosa che si fa
aprendo una sessione su una macchina qualsiasi è `git fetch && git status -sb`.
Chi apre a Firenze senza guardare riparte da prima di ferragosto.

✅ **Spinto di nuovo a fine 30ª, 31ª, 32ª, 33ª, 34ª, 35ª, 36ª, 37ª, 38ª, 39ª e
40ª**, sempre dal portatile. Tutt'e undici hanno aperto con
`git fetch && git status -sb` e tutt'e undici hanno trovato le copie allineate:
la regola ha tenuto **undici volte di fila**.
💡 La 40ª ha spinto **sette volte** — quattro lotti, la chiusura dei tre finali,
la ripresa e `calculation.hsp` — una per risultato chiuso, ed è il numero più
alto del progetto.
⚠️⚠️ **E nella 39ª la spinta ha fatto da rete di sicurezza per la prima volta,
non da comodità.** Uno script della sessione ha troncato `toppe.jsonl` a **zero
byte** — 231.878 byte di dati — e a salvarlo è stato `git checkout`, cioè il
fatto che il lavoro fosse **già spinto**. Se fosse successo prima della prima
spinta, non ci sarebbe stato niente da cui tornare indietro.
💡 La 39ª ha spinto **otto volte** — quattro lotti di `proc.hsp`, la chiusura,
la correzione trovata a schermo, il primo lotto di `chara_func` e la seconda
chiusura. È la seconda sessione dopo la 38ª a chiudersi **due volte**, ed è
giusto così: fra la prima e la seconda ci sono stati il collaudo e un cambio di
rotta sul file successivo, cioè le due cose che la prossima sessione deve sapere
più di ogni altra.
💡 La 38ª ha spinto **otto volte** — sei lotti e due referti — una per
risultato chiuso, ed è il numero più alto del progetto dopo le sette della 35ª.
💡 **La 36ª ha spinto cinque volte** — due toppe, tre lotti — e **la 37ª cinque**
— tre lotti, le sei preposizioni, la chiusura — una per risultato chiuso.
💡 **La 34ª ha spinto quattro volte e la 35ª sette**, una per risultato chiuso
invece che tutto in fondo: se la sessione si fosse interrotta a metà, il lavoro
fatto era già al sicuro. Con sei lotti in una sessione non è più una comodità, è
il modo normale di lavorare. Al 14/08 **il lavoro prosegue dal portatile**: la
macchina di Firenze riprende a fine vacanze, e lì la prima cosa è `git pull`, non
`git push`.

Sul portatile ogni comando degli strumenti va aperto così, perché `python`
nudo è il segnaposto del Microsoft Store e non esegue niente:

```powershell
$py = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
& $py -m strumenti.<nome>
```

💡 Due comodità rimesse lo stesso giorno, se mancassero: la barra del contesto
(`~/.claude/statusline.py` + `statusLine` in `~/.claude/settings.json`) e
Windows Terminal — il console host classico usa Consolas, che **non ha il
giapponese** e lo stampa come `?`, il che rende illeggibili le colonne `jp`.

## La prima cosa da fare

⚠️⚠️ **Il collaudo, e il debito è sceso per la prima volta dalla 36ª.** La 39ª
ha aperto il gioco dopo tre sessioni che non lo facevano, e in un solo
screenshot ha confermato una dozzina di rese nuove e trovato **una resa
sbagliata che compariva cinque volte in uno schermo** (vedi «Quello che ha
trovato il collaudo» in cima). ⚠️ **Ma il grosso resta**: le 121 della 36ª, le
146 della 37ª e le **285 della 38ª** non sono ancora state guardate, e delle 97
della 39ª ne è stata vista **una dozzina**. `cgx-test.exe` è stato rifatto a
fine 39ª e contiene tutto.

⭐ **E adesso si sa come farlo in dieci minuti**: **F12 → `wizard`,
`gain_spact`, `gain_spell`**. `gain_spact` dà **tutte** le azioni speciali in un
colpo, ed è la chiave: senza, metà delle liste qui sotto non è raggiungibile.
⚠️ Modifica il salvataggio per sempre, quindi prima si copia
`elonaplus2.31\save\sav_oldpz` in `save-backup\pre-collaudo-<data>`.

💡 **Le 97 della 39ª chiudono `proc.hsp` e stanno tutte in azioni speciali
identificabili**, quindi si collaudano una per una. ✅ Già viste: la toppa
dell'**automaledizione** (un nome solo), i **tre sguardi** (tre frasi diverse),
l'**Insulto**, la **Sutura istantanea** sul ramo alleato. ⚠️ Da guardare, in
ordine:

| cosa | come | perché |
|---|---|---|
| ✅ **l'automaledizione** | azione speciale **Jyusou Goushin** (`skill.hsp:1412`) | **guardata il 14/08 e la toppa è entrata**: «`Il viandante si scaglia addosso una maledizione tremenda!`», un nome solo |
| ✅ i tre sguardi | **Sguardo di mana**, **Sguardo illusorio**, **Sguardo irrigidente** | **guardati**: tre frasi diverse dove l'inglese ne diceva una sola |
| ⚠️ la **Sutura istantanea** su un **nemico** | ↑ il ramo alleato è già stato visto («ricuce X in un lampo!») | manca il ramo ostile: deve dire «**cuce** X **sul posto** in un lampo!» |
| il menu della necromanzia | azione speciale **Forza necromantica**, tutte e quattro le voci | i quattro versi (`*Potenziamento magico*`, `*Conversione vitale*`, `*Ordigno spietato*`, `*Richiamo dei non-morti*`) e la voce di menu **Evoca non-morti**, che è l'unica riga della sessione che passa da `*prompt_key` |
| il poker | azione speciale **Forza del poker**, con la barra sotto il 100% | «La barra non basta.», «Non hai formato nessuna combinazione.», e «**Le carte** colpiscono X» al plurale — non «La carta», che è lo ShikiOrigami |
| il jolly variabile | azione speciale **Cambio jolly** su un alleato | il nome della creatura diventa `{Jolly Variabile}`: si legge nella lista alleati, non solo nel log |
| il menu delle tattiche | il menu degli ordini agli alleati, tutte le voci | otto rese **copiate da `action.hsp`**: devono uscire identiche a quelle di là. È la prova che le dodici copie del lotto 026 sono giuste |
| l'Onda Sororale | usa lo **Sguardo soggiogante** su una sorella maggiore, che lo para | quattro rese col termine nuovo. ⚠️ `chat.hsp` dirà ancora «Big Sister Energy» in inglese: **non è un difetto della resa**, è la dipendenza nota dai 40 file senza dizionario |
| la marcatura del territorio | fatti marcare da un animale | «X freme di **umiliazione**», non «di rabbia»: è la riga dove l'inglese aveva riciclato la frase dell'ira |
| il filo e l'ago | azione speciale **Sutura istantanea** su un **nemico** e poi su un **alleato** | stesso inglese, due rese opposte: «cuce X sul posto» contro «**ricuce** X» |

💡 **Le 285 della 38ª sono log di combattimento e azioni speciali**, quindi si
vedono con un combattimento qualsiasi e la barra piena. Da guardare per primi,
perché sono quelli dove è cambiata la struttura e non solo le parole:

| cosa | come | perché |
|---|---|---|
| ⚠️ **il pozzo e la fontana** | cammina finché non ti viene sete, poi `h` su un pozzo | è la toppa della 36ª **mai riguardata**, e adesso sono tre sessioni |
| la trasfusione | azione speciale **Trasfusione diretta** | i **tre nomi come soggetti**: «X trasfonde il sangue: lo cede Y e lo riceve Z». È la forma più forzata di tutta la sessione |
| il circolo di lettura e l'ensemble | azioni speciali **Circolo di lettura** e **Ensemble**, con almeno **due** alleati vicini | è il ramo dove il gioco scriveva «your friends»: deve dire «i tuoi compagni» |
| il richiamo di un alleato | azione speciale **Chiama alleato** | `:19066` è la coda di una frase che comincia col nome **fuori** da `lang()`: se lo spazio iniziale è sbagliato si legge «Xappare dal nulla» |
| l'X-Frame | azione speciale **X-Frame Change** | otto versi copiati da `action.hsp`: devono uscire identici a quelli di là |
| il plagio | fatti plagiare da un nemico con Carisma alta | `:18280` dice «si toglie l'equipaggiamento, obbedendo all'ordine» e il soggetto dev'essere **il giocatore** |
| ⭐ **le otto parole del terreno** | lancia Ragnatela, Nebbia di tenebra, Muro di fuoco… poi **Vincolo informe** su un nemico che ci sta dentro | è la scoperta della sessione: dev'uscire «Quasi avesse vita propria, **la ragnatela** avvolge X!» con l'articolo giusto per tutt'e otto. Se una esce senza articolo, o con quello sbagliato, si vede subito |
| la spazzolatura | spazzola un animale del ranch cinque volte | i cinque gradini sono **code** che si attaccano al nome, e portano una battuta fra virgolette: se le virgolette non escono, la protezione `\"` è saltata |
| la mungitura | mungi un animale del ranch | quattro rese dove il giapponese non nominava nessuno e l'inglese sì |
| la tortura e i dadi | azioni speciali **Tortura** e **Dadi del destino** | `:23613` deve dire che cede **chi subisce**, e i dadi devono stampare il numero dopo «Il tiro dà...» |
| le sette invocazioni | azione speciale **Kamui**, sette volte di fila | escono in italiano fra `<>`; l'ottava, `*Kamikakushi* `, resta in giapponese romanizzato **apposta** |

💡 **E le 146 nuove sono le più facili da collaudare di tutto il progetto**,
perché sono il **log di combattimento**: basta un combattimento qualsiasi con
un'azione speciale. Da guardare in quest'ordine:

| cosa | come | perché |
|---|---|---|
| ⚠️ **il pozzo e la fontana** | cammina finché non ti viene sete, poi `h` su un pozzo | è la toppa della 36ª **mai riguardata**: atteso «`Il pozzo disseta il viandante.`» |
| le mosse di barra | un'azione speciale qualsiasi con la barra piena | 20 rese del lotto 015, una per arma. Le tre parate («X attacca, ma Y para») sono la forma nuova |
| le decapitazioni | azione speciale Decapitazione | `facendone saltare la testa` e `decapita`: è dove il genitivo è stato girato |
| i cinque malanni | fatti colpire da veleno, cecità, confusione, paralisi, sonno | 11 rese dove il participio è stato rovesciato: «Il veleno investe X» |
| i terreni | lancia Ragnatela, Muro di fuoco, Nebbia di tenebra | 7 statiche, si vedono subito |
| il potenziale | bevi una pozione del potenziale | «vede crescere il potenziale di Forza» |
| ⚠️ `:11749` | prega il tuo dio | **dirà «di Lulwy of Wind»**, ed è la dipendenza nota da `god.hsp`, non un difetto |

⚠️⚠️ **Il debito di collaudo, che la 36ª ha aggredito e la 37ª ha raddoppiato.**
Delle 235 rese della 35ª ne è stata guardata **una parte** — le teste del log, la
sazietà, la maiuscola — e sono arrivate le **121 rese nuove** dei tre lotti, mai
viste. Se una sessione può fare una cosa sola, faccia il collaudo: vale dalla 32ª
e la 36ª è la prova più forte che sia vero, perché in un'ora di prove ha trovato
due difetti strutturali che otto sessioni di catena verde non avevano visto.

💡 **La roba nuova è facile da vedere**, sta tutta in quel che si fa giocando:
bere alcolici (le due liste di ubriacatura, `:10274` e `:10280`), le pozioni
maledette (le tre sventure in scala — tormento, sventura, flagello), pescare,
salire e scendere da una cavalcatura, benedire l'equipaggiamento.

Da guardare, in ordine di rischio:

0. ⚠️ **Le due toppe della 36ª** — il pozzo (**mai visto**) e la maiuscola
   d'ufficio (✅ vista). Poi le **121 rese** dei lotti `011`-`013`.

1. ✅ **La scena ricucita: guardata il 2026-08-14, e aveva un difetto.** I tre
   pezzi si agganciavano e le virgolette chiudevano, ma a schermo usciva
   «`"Che bello ! Questo e' tutto quello che ho nel portafogli.`» — **uno spazio
   prima del punto esclamativo**. Lo mette `init.hsp:1666`, che nel **solo ramo
   inglese** accoda uno spazio a ogni `txt`; il ramo giapponese no. Per questo
   upstream punteggia la **testa** e fa ripartire la coda con la maiuscola,
   mentre il giapponese fa l'opposto — e noi avevamo copiato il giapponese.
   ✅ Corretto (tre toppe, due voci di dizionario), ricompilato e **riguardato lo
   stesso giorno**: esce «`"I-incredibile! Questo e' tutto quello che ho nel
   portafogli."`». Il dettaglio sta in `decisioni.md`.
   ⚠️ **Resta lo spazio prima della virgoletta di chiusura** («`"Che bello! `»),
   dove la coda è il solo `txt lang("」", "\"")`: ce l'ha anche l'inglese di
   monte, non è nostro.
   ⚠️ **E la regola vale oltre questa scena**: ogni resa che continua un `txt`
   precedente e comincia per punteggiatura mostrerà lo spazio.
   ⚠️⚠️ **La seconda metà di questa frase era falsa, e la 36ª l'ha corretta a
   schermo.** Diceva che «ogni resa che comincia per minuscola verrà maiuscolata
   d'ufficio (`init.hsp:1659-1661`)». **Con l'orologio del log acceso non
   succede mai**: il prefisso `"[H:MM] "` si attacca a `msgtemp` alla riga
   **1578**, cioè 81 righe prima del controllo, e `peek(msgtemp, 0)` legge `[`
   (91), fuori da 97-122. A schermo si leggeva «`[19:07] il viandante finisce di
   mangiare una razione.`». ✅ **Toppato nella 36ª** maiuscolando subito dopo
   `tnew = 0` (`init.hsp:1568`), prima che i prefissi si attacchino. Vedi
   `decisioni.md`, «La maiuscola d'ufficio non gira».
   **La misura su tutto il dizionario non è stata fatta**: è materiale da
   guardia.
2. ✅ **I 63 `buffdesc`**: guardati il 14/08 in tutti e **quattro** i siti —
   scheda del personaggio (`command.hsp:10800`), schermata di analisi
   (`:2005`, che apre l'azione speciale **«Specchio»**), menu abilità (`:5389`,
   taglia a 34) e menu di lancio (`:8851`, taglia a **40**). Chiuso: la
   troncatura è di monte, l'italiano ne sfonda meno dell'inglese.
3. **Le 23 toppe sui blocchi `if ( en )`**: ✅ **7 viste nella 34ª** — le sei
   della scena (`3319`, `3372`, `3487`, `3533`, `3574`, `3617`) e la prima
   dell'equitazione (`10847`, «`Vacci piano, mi raccomando♪`», la cavalcatura che
   parla mentre le sali sopra). **Ne restano 16**, e i triggeri sono tutti noti:

   | come | toppe | nome italiano dell'azione |
   |---|---|---|
   | `a` → azione speciale su un alleato adiacente | 3 | **Equitazione** (20 Sp) — ⚠️ si impara **solo** a Yowyn, Palmia, Eirel, Melkawn (`command.hsp:9040`); il maestro di Yowyn è a **(20, 14)** e si chiama «*… della gilda*»; `spawn_item 1093` è il biglietto abilità che evita il platino |
   | `a` → su un nemico | 3 | **Inferno del solletico** |
   | `a` → su un PNG | 2 | **Ammaliamento** |
   | `a` → su un nemico | 1 | **Sguardo di follia** |
   | `a` → su un alleato con la barra di rottura guardia > 0 | 1 | **Istruzione individuale** |
   | `D` su un muro · raccolta in un campo | 2 | — |
   | viaggio su neve o sabbia · sotto pioggia forte | 3 | — |
   | ⚠️ **Ordini tattici** rifiutato, su un alleato **che ha partorito**, 1 volta su 2 | 1 | condizione troppo stretta: **non cercarla apposta** |

   💡 **Sei di queste si fanno da fermo**, con un alleato e un nemico a portata:
   solletico, ammaliamento, sguardo di follia. Non serve andare da nessuna parte.
4. Le liste arretrate 27ª-30ª e le 169 battute degli dèi.

⭐ **`buff.hsp` è chiuso.** La 33ª ha fatto i **63 `buffdesc`** in un lotto solo,
`fase2-buffdesc-001`: il file passa da 63 non tradotte a **0**, ed è il primo
file di Fase 4 chiuso per intero. Catena verde, compilatore muto, `cgx-test.exe`
rifatto. ⚠️ **Ma non è ancora stato guardato a schermo**: vedi «Il debito di
collaudo» più sotto — è la prima cosa che deve provare la 34ª, e i tre siti
dove esce sono la lista abilità (`command.hsp:5389`), la schermata di analisi
(`:2005`) e la scheda del personaggio (`:10800`).

💡 **La scoperta della 33ª è che per una riga che descrive un effetto l'arbitro
non è una lingua, è il codice.** Tre `buffdesc` su 63 avevano giapponese e
inglese che dicevano cose diverse, e il blocco sotto la riga ha chiuso la
domanda in dieci righe di lettura: a `656` l'inglese sbaglia **due volte** (dice
«10%» dove non c'è e `RES+ confusion` dove il codice alza la resistenza alla
**magia**); a `1195` perde il `軽装備+20%`; a `1315` — ed è il caso che rovescia
la regola — **l'inglese è più preciso del giapponese** e il codice gli dà
ragione, ma il giapponese porta la barra che l'inglese ha perso, **e le due metà
si sommano invece di scegliersi**. Il dettaglio sta in `decisioni.md`.

⚠️ **E la domanda della 29ª va posta con una misura di somiglianza, non per
stringa esatta.** Sui 63 `buffdesc` il confronto esatto trovava **1** gemello e
avrebbe chiuso la domanda con un no; `difflib` a 0,55 sul giapponese ne ha
trovati **14**, e tre sono state copiate perché dicono la stessa cosa di
`skill.hsp` con altre parole. Lo script sta in `scratchpad/simili.py`.

⭐ **La 32ª è stata una sessione di sole prove in gioco**, la prima da molto, e
ha reso più di quanto costasse: **due tetti che nessuno aveva mai misurato**,
tutti e due sfondati, **33 rese corrette**, e la spiegazione di perché le liste
di collaudo non tornano mai. Il dettaglio sta in `decisioni.md`, in tre voci
datate 13/08. In breve:

1. ⚠️ **Le piastrelle degli stati nell'HUD tagliano** — a schermo si leggeva
   «Marchio letal». Il carattere della build inglese è `Courier New`, cioè
   **monospaziato**: 11 caratteri sulla piastrella da 80 px, 13 su quella da
   95. Sfondavano **19 etichette su 61**, e l'inglese di upstream ne sfonda 2.
   ✅ **Corretto e riverificato a schermo lo stesso giorno**: l'etichetta esce
   intera, con «Stanchezza» e «Fardello!» comode nella loro piastrella. La
   prova sta in fondo al ciclo giusto — difetto visto, misurato sul sorgente,
   corretto nel dizionario, ricompilato, riguardato.
   ⚠️ **E la riguardata ha prodotto una correzione della correzione**: il primo
   accorciamento era «Marchio», che sta nel tetto ma perde il 死 del 刻死紋.
   Adesso è **«Segno letale»**, e il gemello «Veleno!» è diventato **«Gran
   veleno»**. Vedi `decisioni.md`, «Accorciare puo' togliere il significato».
2. ⚠️ **Le colonne del menu tattiche del mod si sovrappongono** — la domanda
   aperta dalla 29ª si chiude sull'ipotesi peggiore: `cs_list` **non taglia**,
   sconfina sulla colonna accanto. 20 caratteri il tetto, **10 `buffname` su
   71** lo passavano, **0 inglesi**.
3. ⚠️ **Undici creature su ventisette sono mute se aspetti**: non hanno
   `DBMODE_FLAVOR_PASSIVE`, e il metodo «`add_ally` e tieni premuto `5`» per
   loro non produce niente. Vedi «Il collaudo, punto per punto», riscritto per
   classe di battuta.

💡 **E il collaudo ha dato la prova sul campo dell'ordine già deciso.** Il log
di un combattimento qualsiasi è pieno di inglese — «is drawn», «was knocked
down», «stands up», «aims at nearby enemies», «teleports toward», «crushes with
hip!» — e **viene tutto da `proc.hsp`**. Non lo si trovava col grep perché le
frasi sono spezzate dall'helper morfologico: nel sorgente c'è
`" aim" + _s(cc) + " at nearby enemies."`, non la frase intera. È il file che
il giocatore legge a **ogni singolo combattimento**, ed è il numero 2 della coda.

✅ **E i due tetti nuovi hanno la loro guardia**, scritta nella stessa sessione:
**`strumenti/riquadri.py`**, più 18 test. Sta nelle verifiche d'apertura. 💡 Due
cose le ha trovate il test, non l'occhio: la prima versione prendeva la
`gcopy` «entro sei righe sopra», e un'etichetta senza piastrella si sarebbe
presa in silenzio quella dell'etichetta precedente; e leggeva il passo della
colonna dalla **prima** `cs_list` del file, che è un altro menu con un passo di
150 — verdetto giusto per sbaglio, perché 150 / 7,2 fa comunque 20.

⭐ **`db_creature.hsp` è chiuso.** La 31ª ha fatto sei lotti, dal `037` al `042`:
**315 rese**, 51 creature, catena verde a ogni lotto. Le battute sono passate da
**316 a 0** e le creature da fare da 51 a **0**. Il file era a 1.563 da fare
all'apertura della 27ª.

Restano **quattro** voci non tradotte in quel file, e sono le quattro **rinviate
apposta**: le righe commentate nel sorgente, registrate in `rinviate.jsonl` col
motivo. Più `86293`, la battuta col ramo inglese vuoto, che `estrai.py` non vede
nemmeno. Nient'altro.

⚠️ **Resta valida la domanda della 29ª all'apertura di ogni file nuovo**: *questo
file nomina cose che un altro file ha già nominato?* La riga di comando che
risponde sta in `decisioni.md`. E resta la **ricerca dei participi** di
`decisioni.md`, da rilanciare a ogni lotto: nella 31ª ha dato **0** ogni volta,
su tutto il dizionario, il che vuol dire che le sei correzioni della 30ª hanno
tenuto e che nessuna delle 315 rese nuove ne ha introdotte.

✅ **E i `bufftxt` di `buff.hsp` sono chiusi**, sempre il 13/08: la toppa
strutturale su `chara_func.hsp` più le 65 rese che coprono i 71 messaggi. Vedi
«Le due toppe di `buff.hsp`» più sotto. `buff.hsp` passa da 128 non tradotte a
**63**, e le 63 sono tutte `buffdesc`.

**Il lavoro che riparte, in ordine:**

0. ✅ **La guardia sui due tetti nuovi**: fatta nella 32ª, `strumenti/riquadri.py`.
1. ✅ **I 63 `buffdesc`**: fatti nella 33ª, `buff.hsp` è chiuso.
   ✅ **Guardati a schermo il 2026-08-14 e la questione è chiusa**, in tutti e
   quattro i siti: scheda del personaggio (`Accelerazione: 7(13) Velocita' +60`,
   intero), schermata di analisi (intero), menu abilità e menu di lancio.
   ⚠️ **E i siti erano quattro, non tre, con tre tetti diversi** — la ripresa ne
   registrava uno solo:

   | sito | routine | taglio |
   |---|---|---|
   | menu `a` | `*com_applySkill_loop` | 34 |
   | menu `W` | `*com_applyWideSkill_loop` | 34 |
   | menu di lancio | `*com_spell_loop` | **40** |
   | scheda, pagina incantesimi | `*com_charainfo_loop_WHILE1` | **46** |

   💡 **Il conto della 33ª — «46 inglesi su 63 sfondano già» — valeva solo per il
   34**, e delle 21 abilità che mostrano un `buffdesc` **solo 4 sono azioni
   speciali**: le altre 17 sono incantesimi e cadono nei tetti da 40 e 46.
   Rimisurato per tetto con `scratchpad/tetti_buffdesc.py`:

   | tetto | italiano sfonda | inglese sfonda |
   |---|---|---|
   | 34 | 43 su 62 | **46** su 62 |
   | 40 | 32 su 62 | **38** su 62 |
   | 46 | 23 su 62 | **31** su 62 |

   ✅ **L'italiano sfonda meno dell'inglese a tutti e tre**, quindi la troncatura
   è comportamento di monte e **non c'è niente da accorciare**. A schermo si
   vedono `Res+ gra`, `Res+ sonno,confu`, `oltretomb` — sembrano refusi e non lo
   sono: le stesse righe inglesi si tagliano nello stesso modo, perché elencano
   dieci resistenze in tutte e due le lingue. ⚠️ Accorciarle peggiorerebbe i siti
   dove la riga ci sta comoda.
   ⚠️ Cautela sul numero: lo strumento stima a due cifre le variabili
   interpolate, quindi c'è un margine di ±1 carattere per voce. Il metodo è lo
   stesso sulle due lingue, quindi il **confronto** regge; i valori assoluti no.
2. ✅ **`proc.hsp` è CHIUSO nella 39ª**, a **1.091 su 1.098 (100%)**: le 7 che
   restano sono tutte rinviate apposta (una riga commentata, «Party Room», i due
   nomi di nave, `:11481`, `:11796` e `:24107`, tutt'e tre risolte da toppa o
   dentro un blocco spento). I quattro lotti della 39ª sono `-023`
   (20000-20999), `-024` (24000-24999), `-025` (25000-25999) e `-026`
   (26000-26999).

   ⚠️ **Prima di aprire il file dopo, copiare le quattordici reti** da
   **`scratchpad/lotto-fase4-proc-026.py`**, che è il modello più recente. ⚠️ Le
   reti 3, 4 e 8 sono state **corrette perché sbagliavano loro**, e la 12 e la 13
   sono nuove: si copia il file, non si riscrive a memoria.
   ✅ **E adesso la regola è meccanica**: `scratchpad/assembla-lotto.py` copia il
   blocco dal modello, cambia `USCITA`, `DA, A` e — dalla 39ª — `RINVIATE`, e
   **rilegge quel che ha scritto** confrontandolo col modello carattere per
   carattere. Bastano due file scritti a mano — la testa col docstring e le rese
   — più un `rinviate<numero>.py` facoltativo, e il resto è copiato:

   ```powershell
   & $py scratchpad/assembla-lotto.py 027 scratchpad/lotto-fase4-proc-026.py 0 99999 <cartella>
   ```

   ⚠️ **Le reti hanno un difetto noto e ancora aperto**: se manca una resa, il
   messaggio della rete 1 **non si vede mai**, perché la rete 8 dereferenzia
   `RESE` prima del controllo di `errori` e quel che esce è un `KeyError` nudo.
   Vale la pena spostare il blocco `if errori:` subito dopo la rete 2.

   La 33ª ha fatto i lotti `fase4-proc-001` … `-004` (1716-3400: le reazioni
   degli dèi, le tattiche, bugia/minaccia/canto/pasto). **La 35ª ha fatto i sei
   lotti `-005` … `-010`, cioè tutto il 3401-9200**, e ⭐ **la 36ª i tre lotti
   `-011` … `-013`, cioè 9201-11499:**

   | lotto | zona | che cosa |
   |---|---|---|
   | `-005` | 3401-4200 | le attività continuate, le due trappole, il furto |
   | `-006` | 4201-5000 | il sonno, il risveglio, il riposo, il viaggio |
   | `-007` | 5001-5900 | pesca, scavo, miniera, i pasti |
   | `-008` | 5901-6800 | la sazietà, la lettura, l'abisso, i lanci falliti |
   | `-009` | 6801-7700 | bere, i pozzi, le pergamene, le bacchette |
   | `-010` | 7701-9200 | il log di combattimento: proiettili, cure, morsi |
   | `-011` | 9201-10100 | azioni speciali, borseggio, soffio, mappe del tesoro |
   | `-012` | 10101-10600 | pozioni, latte, ubriacature, oli, acido |
   | `-013` | 10601-11499 | bibite, sale, equitazione, pesca, mutazioni |
   | `-014` | 11500-12500 | pergamene, potenziale, dèi, decapitazioni |
   | `-015` | 12501-14499 | il log delle azioni speciali, arma per arma |
   | `-016` | 14500-15499 | fuga e ritorno, veleni, maledizioni, terreni, artefatti |

   ⚠️ **Prima di riprendere, rileggere le undici reti** dello script di lotto: il
   modello più completo è **`scratchpad/lotto-fase4-proc-013.py`**, che le ha
   tutte. Le cinque della 35ª (5-9) e le due della 36ª (10 e 11) sono nate ognuna
   da un caso reale, non da un'idea. ⚠️ **La rete 11 è quella che vale di più e
   anche quella che è nata sbagliata due volte** — troppo severa sulle statiche,
   poi giusta e decisiva su `his2` — quindi si copia, non si riscrive;
   ✅ **La toppa sui blocchi `if ( en )` è fatta**: 23 righe di questo file
   avevano letterali inglesi **nudi** fuori da `lang()`, invisibili
   all'estrattore. `toppe.jsonl` passa da 273 a **296** ed erano zero su
   `proc.hsp`. Vedi `decisioni.md`, «Ventitré righe di `proc.hsp` parlano inglese
   fuori da `lang()`».
   ✅ **E la misura è stata fatta su tutto il sorgente**: **99 righe** così in 14
   file, di cui **68 ancora intatte** — `event.hsp` 27, `screen.hsp` 14,
   `command.hsp` 10, `system.hsp` 4, `material.hsp`/`item_func.hsp`/`main.hsp` 3
   ciascuno. 💡 Il grosso viaggia con file non ancora tradotti, quindi non ha
   fretta. ⚠️ **Ma circa metà delle righe dei file piccoli non è testo** —
   entità HTML, operandi di confronto, chiavi di dati — quindi il numero è un
   punto di partenza, non un elenco di lavoro;
3. ⭐⭐ **`chara_func.hsp`, e la scelta l'ha fatta il collaudo.** Questo punto
   diceva «`command.hsp`/`trait.hsp` oppure il fuori perimetro», ed era
   **sbagliato**: lo screenshot ha mostrato che il log resta mezzo inglese
   anche con `proc.hsp` al 100%, e le righe che lo sporcano stanno qui.

   - ✅ **`chara_func.hsp`, 247 firme, e `calculation.hsp`, 44.** Primo lotto
     fatto (3000-3999, gli stati e i recuperi). Le zone restanti, tutte
     tematicamente pulite: `6000-6999` **68** (cure, urla e **tutte le cause di
     morte**, log e giornale), `2000-2999` **59** (azioni ostili, i due blocchi
     gemelli di 22 messaggi di resistenza, la malattia dell'etere),
     `4000-4999` **35** (danni elementali agli oggetti, le morti scherzose),
     `7000-7999` **35** (premi, pietre magiche, cadaveri), `8000-8999` **27**
     (peso, altezza, anoressia, geni), `1000-1999` **18** (relazioni,
     cavalcature, tag-team). ⚠️ `calculation.hsp` **non ha ancora un
     dizionario**: è un file intero da aprire, e ci stanno `stands up` e
     `released from bind`, che si leggono a ogni combattimento.
   - **`command.hsp` e `trait.hsp`**, ~1.966 firme mai toccate. È la strada
     nota, ma si legge nei **menu**, non nel log. ⚠️ `command.hsp` è anche il
     file che **disegna** i `buffdesc`, quello di «`Really attack X?`» e
     «`Do you want to save the game and exit?`», e quello che porta 10 delle 68
     righe inglesi fuori da `lang()` ancora intatte.
   - ⚠️ **Il testo fuori perimetro**, cioè le **5.284 descrizioni degli
     oggetti** di `db_item.hsp` e i **quattro file di `data/`** (~2.900 righe,
     117.977 caratteri di prosa inglese). È la scoperta della 38ª, ed è il
     motivo per cui il progetto sta al 36% e non al 49%. 💡 È il lavoro **meno
     insidioso** — niente `name()` da accordare, niente participi, niente reti
     — ma vuole una **catena di strumenti diversa**, perché non ha firma
     `lang()` e non passa da `applica.py`. Nessuno l'ha ancora scritta, e
     scriverla è mezza giornata prima di tradurre la prima riga.

   💡 **La domanda giusta è quale il giocatore legge di più, e la risposta si
   guarda, non si calcola.** Il progetto ce l'aveva già dalla 26ª — *la
   frequenza, non l'elenco* — ma per tre file di fila l'aveva applicata
   contando le firme. La 39ª l'ha applicata **aprendo il gioco**, e la risposta
   è cambiata al primo screenshot.

⭐ **`chips.hsp` è chiuso**, trovato e fatto a schermo il 14/08. Ha **tre**
`lang()` in tutto — i nomi delle caselle di terreno — e uscivano da
`action.hsp:2681` dentro una frase **già tradotta**, quindi a schermo si leggeva
«`a field si trova ai tuoi piedi.`»: metà inglese e metà italiana, a ogni passo
mentre si coltiva. È la lezione di `adv.hsp` della 26ª (**la frequenza, non
l'elenco**), stavolta su un file che l'elenco copre ma che nessuno aveva ragione
di aprire.

| riga | giapponese | resa | perché |
|---|---|---|---|
| 833 | 日干し岩 | `una pietra da essiccazione` | al ranch, col bel tempo, quel che ci lasci sopra si secca e un cadavere diventa carne secca (`item.hsp:1819-1835`); «essiccazione» tiene la famiglia di `pesce essiccato` |
| 834 | 畑の土 | `un campo coltivato` | **copiata** da `action.hsp`, «Si concima solo il campo coltivato.» |
| 835 | コンポスト | `del compost` | **copiata** da `action.hsp`, «Il compost funziona solo nei campi di tua proprietà.» Partitivo: è un mucchio, non un oggetto numerabile |

💡 **Due rese su tre sono copie**: la regola «cercare prima di scrivere» ha reso
due volte su tre in un lotto da tre voci. ⚠️ E ogni resa porta **il proprio
articolo**, perché lo porta l'inglese (`a field`) e la frase che le ospita non ne
mette.
✅ **E ha dato la prova più forte finora sulla scoperta 2 della 28ª.**
`sdim tname, 16` dà 16 byte a voce; «una pietra da essiccazione» ne occupa **26**
e «un campo coltivato» **18**. Guardato a schermo il 14/08: la frase esce
**intera**. Fin qui la controprova migliore era `sdim buffname, 20` col
giapponese di monte da 22 byte, cioè un +10% scritto **da upstream**; questa è un
**+62% scritto da noi**, su una stringa che il giocatore legge a ogni passo.
`sdim` non è un tetto in scrittura, e adesso lo si sa con un margine largo.

💡 **Il debito di collaudo è stato aggredito nella 32ª, non estinto, e la 33ª
l'ha aumentato.** Provati nella 32ª: i messaggi dei potenziamenti (la toppa
strutturale, mai vista prima), il menu tattiche, le etichette di stato
dell'HUD, `<Aribel>`, e un combattimento coi due Yerleswood. **Restano da
guardare** le liste 27ª-30ª, le 169 battute degli dèi e — nuovi — i **63
`buffdesc`** della 33ª, che nessuno ha ancora visto a schermo. ⚠️ Ma adesso si
sa **come** guardarle: per classe di battuta, non mettendosi ad aspettare.

💡 **I `buffdesc` si guardano senza aspettare niente**: basta avere un
potenziamento addosso e aprire la scheda del personaggio (`command.hsp:10800`,
non taglia e manda a capo), la schermata di analisi (`:2005`, non taglia) e la
**lista abilità** (`:5389`, che taglia a 34 e va guardata per ultima, perché è
lì che si vede quanto la troncatura di upstream costa in italiano).

⚠️ **I nomi di creatura sono chiusi**: l'ultimo che i conteggi mostravano da
fare era su una riga commentata. Vedi «Le righe commentate» più sotto.

### Le otto verifiche d'apertura

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m pytest strumenti/tests -q        # atteso: 412 passed, 6 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 2466, doppie 0, senza razza 0
python -m strumenti.larghezze              # atteso: 0 fuori misura su 75 menu
python -m strumenti.diario                 # atteso: 0 fuori misura su 214 siti
python -m strumenti.riquadri               # atteso: 0 su 38 piastrelle, 0 su 71 buffname
python -m strumenti.battute --divergenti   # atteso: 13, tutte legittime
```

💡 **`riquadri.py` è nato nella 32ª**, il giorno stesso in cui i due tetti che
misura sono stati scoperti sfondati. Copre le piastrelle degli stati nell'HUD e
la colonna del menu tattiche, che `larghezze.py` non vede perché non passano da
`*prompt_key`.

⚠️ **I quattro test in più che saltano sono la chiusura di `db_creature.hsp`**,
non un guasto. Leggono `lavoro/_c.jsonl` e provano proprietà dell'**ordinamento
di un elenco**: su un elenco vuoto tre di loro morivano — `max()` di niente, una
divisione per zero, due ordini vuoti che «coincidono». Il 13/08 sono diventati
rossi tutti insieme per la prima volta, e nessuno dei tre aveva trovato un
difetto. Adesso `estrazione_da_fare()` salta anche sul file **vuoto**, oltre che
sul file assente. 💡 Provato che il guardiano non li ha spenti: con
un'estrazione piena (`estrai` senza `--da-tradurre`) tornano a girare e passano.

💡 **E i referti, che non sono guardie e vanno letti**, adesso tutti in
`scratchpad/` (vedi `scratchpad/LEGGIMI.md`):

```powershell
$env:PYTHONPATH = $repo
python scratchpad/referti.py              # participi col giocatore: 0 | elisioni: 0
python scratchpad/blocchi_en.py           # struttura 99 | ancora da fare 68
python scratchpad/else_jp.py              # else-di-jp: 6.984 righe in 13 file
python scratchpad/rete8_dizionario.py     # 3, tutti dichiarati falsi positivi
python scratchpad/misura-blocchi-spenti.py  # 7 voci dentro un blocco spento
python scratchpad/variabili_en.py         # 66 variabili | 3 trappole in 3 siti
python scratchpad/perimetro.py            # perimetro 50% | col fuori perimetro 37%
python scratchpad/cnv_str_en.py           # 41 chiamate | 17 con la chiave inglese
```

⚠️ **L'ultimo è della 40ª, ed è il QUARTO punto cieco.** `cnv_str` riscrive una
stringa **già composta** usando come chiave l'**inglese di monte**: la resa
italiana la spegne, e in un caso l'aveva già spenta il bestiario mesi fa (vedi
il punto 3 delle cinque cose). **Se le 17 salgono, qualcuno ne ha scritta una
nuova; se scendono, una è stata toppata.** ⚠️ E delle 17, **2 sono uscita**
(`chara_func.hsp`) e **15 sono input** (`module.hsp`, `help.hsp`): solo le prime
due riguardano quel che il giocatore legge.

⚠️ **I due ultimi sono della 38ª.** `variabili_en.py` è il **terzo punto cieco**
dopo `blocchi_en.py` e `else_jp.py`: le variabili che si portano dentro un
letterale inglese e finiscono dentro una `lang()`. **Se sale a 4, qualcuno ne ha
creata una nuova; se scende a 2, `economy.hsp:319` è stato risolto.**
`perimetro.py` è il conto vero di quanto manca, descrizioni degli oggetti e file
di `data/` compresi: **non si deduce sommando `verifica --dizionario`**, che
misura solo il perimetro `lang()`.

⚠️ **I due ultimi sono della 37ª.** `rete8_dizionario.py` è la rete 8 passata
all'indietro su tutto il dizionario: **se sale a 4, qualcuno ha scritto un
genitivo davanti a un nome**. `misura-blocchi-spenti.py` conta le voci tradotte
dentro un `/* ... */`: se sale, un lotto ha tradotto testo morto. Tutt'e due
leggono il **`SORGENTE`**, non la build — vedi la nota in cima sulla riga in più
di `text.hsp`.

⚠️ **`else_jp.py` è nato nella 34ª ed è il punto cieco di `blocchi_en.py`.** Gli
stessi letterali inglesi nudi, ma scritti `if ( jp ) { … } else { … }` invece che
`if ( en ) { … }`: il fratello non li vede, e nessun conteggio di «non tradotte»
li include. Trovato perché la follia di `calculation.hsp:2352` — `"Forgive me!
Forgive me!"`, `"P-P-Pika!"`, `"You snail!"` — è uscita **in inglese a schermo**
durante il collaudo. Delle 6.984 righe, **6.840 sono le descrizioni di
`db_item.hsp`** già dichiarate fuori perimetro: le vive sono **144**, e le
interessanti sono `proc.hsp` 13, `ai.hsp` 3, `calculation.hsp` 2, `chat.hsp` 2.
💡 `item_func.hsp` ne ha 30 con **0 intatte**: quella famiglia era già stata
toppata a mano, un caso per volta, senza che nessuno sapesse che era una
famiglia.

⚠️ **E qui la 34ª ha scritto una cosa falsa e l'ha corretta un'ora dopo**: che
`calculation.hsp` «non stesse in nessun elenco di fase» e «non avesse firme». Ha
**44 `lang()`**, e `SPEC.md` §6 mette in Fase 4 «i restanti **63 file** `.hsp`
minori», che è una designazione **collettiva**: copre ogni file non nominato
prima. Non è `adv.hsp` della 26ª — è coda non ancora cominciata.
✅ **La domanda della 26ª è chiusa con una misura**, non con una lettura:
`scratchpad/fuori_elenco.py` dice che dei **54** file con `lang()` ne hanno un
dizionario **14**, e i **40** restanti valgono **12.620** stringhe mai estratte.
Nessun file è fuori elenco; l'elenco è solo collettivo.

`referti.py` fa la nona e la decima verifica — i participi che concordano col
giocatore e le elisioni davanti a consonante. Attese **0** tutt'e due: adesso che
sono a zero, un valore diverso significa qualcosa.

⚠️ `blocchi_en.py` è **un referto, non una guardia**, e per due motivi: circa
metà delle righe dei file piccoli non è testo (entità HTML, operandi di
confronto, chiavi di dati), e il numero **cala solo quando si fa una toppa**, non
quando si traduce. Non deve tornare a 92: se lo fa, qualcuno ha ricreato
l'albero di build senza applicare le toppe.

Se `--divergenti` sale, qualcuno ha reso due volte in modo diverso la stessa
frase giapponese. Le due nuove della 27ª sono volute: 「きゅう…」 («*sbuffo*»
altrove, «Quu...» sulla forma di vita quantistica, dove l'inglese fa il gioco
di parole con Q) e 「わん！」 («*bau!*» dove l'inglese descrive un'azione,
«Bau!» dove passa da `cnvtalk`, che mette le virgolette).

⚠️ **Le due della 30ª (da 11 a 13) sono la stessa resa in due involucri diversi**:
la sorella minore chiama il giocatore con `_onii` in due punti, e upstream avvolge
un sito in `cnvtalk(...)` e l'altro in virgolette nude `"\"" + ... + "\""`. Il
testo che il giocatore legge è identico; a differire è il codice HSP intorno. È la
stessa classe di 「お、カモだ…」, che stava già fra le undici.

⚠️ **Ma `--divergenti` guarda solo `db_creature.hsp`** — misurato nella 29ª,
`rese_gia_decise()` apre quel file e basta. Una divergenza introdotta in
qualunque altro file **non alza quel numero**. Non fidarsi dell'11 come se
coprisse il dizionario intero: vedi `decisioni.md`, «Un buff è l'incantesimo che
lo concede».

💡 Vale anche il manifesto del sorgente, che nessuno strumento controlla:

```powershell
$base="C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx"
Get-Content "C:\Games\Elona\_traduzione\manifesto-sorgente.txt" | ForEach-Object {
  $p=$_ -split '\s+',2
  if ((Get-FileHash "$base\$($p[1].Trim())" -Algorithm SHA256).Hash -ne $p[0]) { $p[1] } }
```
Nessun output = 72/72. ✅ Ricontrollato a fine 33ª: nessuna differenza. Il
sorgente pinnato non è mai stato scritto, nemmeno dalle 24 toppe — le toppe sono
**dati applicati all'albero di build**, e `compila.py` rifiuta per costruzione di
scrivere dentro `SORGENTE`.

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.606 | 1.606 | **100%** |
| `item_data.hsp` | 318 | 318 | **100%** |
| `skill.hsp` | 885 | 885 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `adv.hsp` | 12 | 12 | **100%** ⭐ chiuso il 2026-08-11 |
| `action.hsp` | 1.286 | 1.288 | **100%** (le 2 mancanti sono rinviate a toppa). ⚠️ Aveva **una riga inglese** che nessun conteggio vedeva, `:15221`, fuori da `lang()`: toppata il 2026-08-13 |
| `text.hsp` | 1.718 | 1.720 | **100%** (le 2 mancanti aspettano `talk.txt`) |
| `proc.hsp` | **1.091** | 1.098 | **100%** ⭐⭐ **chiuso il 2026-08-14** — +97 nella 39ª (era 994), più 23 righe fuori da `lang()` ✅ toppate, e **7 rinviate**: una riga commentata, «Party Room», i due nomi di nave, `:11481` (`his2()`, ✅ toppata nella 36ª), `:11796` (dentro un blocco `/* ... */` spento) e `:24107` (`tc == cc` e l'inglese nomina due personaggi, ✅ toppata nella 39ª) |
| `buff.hsp` | 199 | 199 | **100%** ⭐ chiuso il 2026-08-13 — `buffname`, `bufftxt` e `buffdesc` |
| `command.hsp`, `trait.hsp` | 0 | ~1.680 | 0% |

`db_creature.hsp`: **1.131 nomi** + **2.519 battute rese**, **0 da fare**. ⭐
**Chiuso il 2026-08-13**, a parte le quattro righe commentate rinviate apposta.
Era a 1.563 da fare all'apertura della 27ª. I lotti `015`-`026` coprono i livelli
**6-45** — le creature di città, i PNG di trama e i primi sotterranei — i dieci
lotti `027`-`036` della 30ª i livelli **45-157**, cioè i PNG delle gilde, i boss
di trama e i mostri di Nefia profonda, e i sei lotti `037`-`042` della 31ª tutto
il resto: **159-1200**, cioè i demoni, gli dèi del Patto Eterno, gli otto dèi di
Elona e le loro forme potenziate.

⚠️ I conti per classe si rifanno così, e non si deducono: le classi si leggono
dal `dbmode` che precede la riga nel sorgente, incrociando `dizionario/` per le
rese e `lavoro/_c.jsonl` per quelle da fare. Rifatti il 13/08 a fine 31ª:
`2.519 voce + 1.131 nome + 1 senza classe + 4 rinviate = 3.655`, che è il totale
delle firme del file. 💡 **Dedurli sbagliava**: la ripresa portava «2.199
battute rese» e sommandoci i lotti veniva 2.515, quattro in meno del vero.

Altri fuori Fase 1: `custom_enemyevolution.hsp` **chiuso**; `chips.hsp`
**chiuso** ⭐ 2026-08-14 (3 su 3); `ai.hsp` 6 su 100; `event.hsp` 5 su 654;
`init.hsp` 6 su 133.

⭐⭐ **`chara_func.hsp`: 327 su 331, chiuso il 2026-08-14** — +243 nella 40ª (era
84), sei lotti in una sessione sola. Le **4 rinviate** sono `:2310` (dentro un
blocco `/* ... */` spento), `:3037` e `:4520` (✅ toppate), `:4369` (riga
commentata). Il file porta **6 toppe**.

⭐⭐ **`calculation.hsp`: 44 su 44, chiuso il 2026-08-14** — un lotto solo, **zero
rinviate**, ed è l'unico file del progetto chiuso senza lasciare niente indietro
al primo passaggio. ⚠️ **Ma «100%» qui vuol dire «tutte le firme `lang()`»**:
`:2352` porta 「Forgive me! Forgive me!」, 「P-P-Pika!」, 「You snail!」 dentro un
`if ( jp ) … else` **fuori da `lang()`** — la scoperta di `else_jp.py` della 34ª,
uscita in inglese a schermo durante quel collaudo. Non hanno firma, non entrano
in nessun conteggio, e vanno **per toppa**.

⚠️ **E il quadro d'insieme, misurato il 14/08 con `scratchpad/fuori_elenco.py`**:
dei **54** file con `lang()` ne hanno un dizionario **14**; i **40** restanti
valgono **12.620 stringhe mai estratte**. Non sono file dimenticati — sono la
Fase 4, che `SPEC.md` §6 definisce collettivamente («i restanti 63 file `.hsp`
minori»). Il numero serve a tenere le proporzioni: quello che resta è più grande
di quello che è stato fatto.

**412 test più 6 saltati**, prova d'identità **72/72 e 27.813**, **14.534
sostituzioni** applicate alla build — erano **14.239** alla chiusura della 39ª,
più le **251** dei sei lotti di `chara_func.hsp` e le **44** di
`calculation.hsp`. **`toppe.jsonl` è a 306** (+2
nella 40ª, tutt'e due per `:4520`: `chara_func.hsp:4491` e `:4520`), e
`chara_func.hsp` ne porta **6**, `proc.hsp` **28**. **`rinviate.jsonl` è a 19**
(`proc.hsp` 7, `db_creature.hsp` 4, `chara_func.hsp` 4, `action.hsp` 2,
`text.hsp` 2). Il compilatore non dice nulla, manifesto del sorgente **72/72**.
Perimetro `lang()` **50%**, totale vero **37%**.

💡 **Le sostituzioni crescono più delle rese anche stavolta**: 243 rese hanno
prodotto **251 siti**. Il caso più netto della 40ª è `chara_func.hsp:8317`, che
ha la stessa firma di `:3377` — la stessa riga, in due punti dello stesso file —
e `:6859`, che copre anche `:6865`, e `:6877`, che copre `:6883`.

💡 **Le sostituzioni crescono più delle rese anche stavolta**: 97 rese hanno
prodotto **111 siti**. Una firma esce in più punti, e il caso più netto della
39ª è `:20200`, che copre anche `:20886` — la stessa domanda «non c'è nessun
bersaglio in vista» posta da due rami diversi della necromanzia — e `:24783`,
che copre `:24798`. Nessuno dei due secondi siti compare nell'estrazione.

💡 **E le sostituzioni crescevano più delle rese anche nella 38ª**: 285 rese
hanno prodotto **300 siti**, e il caso più netto era `:16087`, che ne copre
**due** senza che il secondo compaia nell'estrazione.

💡 **Le sostituzioni crescono più delle rese, ed è il motivo per cui vale la pena
contarle**: 235 rese hanno prodotto 298 siti, perché una firma può uscire in più
punti. Nella 35ª il record è «`name(tc)` si indebolisce», **otto siti** con una
resa sola, e «Il tuo diario è stato aggiornato.» ne copre **sei**. Il conto per
lotto si rifà così, e non si deduce:

```powershell
& $py -c "import io,json,collections; ..."   # vedi i commit dei lotti 005-010
``` ✅ Tutta la batteria
rilanciata a fine 33ª dopo le **165 rese nuove**: **identica in ogni valore**,
niente si è mosso, e `verifica --dizionario` dà `buff.hsp: 0 da ritradurre, 0 non
ancora tradotte`. ✅ E stavolta l'eseguibile è **davvero** quello nuovo: vedi i
due passi che il metodo non nominava.

## Le due toppe di `buff.hsp`, e perché ce ne volevano due

### 1. La toppa strutturale: 63 righe diventano una

Il ramo giapponese (`chara_func.hsp:2377`) compone il messaggio «X comincia
a...» con un **frammento unico**, `name(id) + bufftxt(0, id)`. Il ramo inglese
(`:2316-2375`) ne compone quattro — `name + bufftxt(0) + _s(id) + bufftxt(1)` —
più **sette casi speciali** con `his(id)`. Nessuna delle due conseguenze si
risolve traducendo: `bufftxt(1)` è un letterale nudo **fuori** da `lang()` in
tutte e 71 le righe, e `_s()`/`his()` sono morfologia inglese che le regole
vietano.

La toppa riporta il ramo inglese alla forma giapponese. ✅ **Tolto anche
`cnven()`**, che il ramo inglese applicava **al solo giocatore**: il resto della
build non capitalizza il nome a inizio messaggio (`chara_func.hsp:6846`,
«`name(id) + " perde la vita."`»), e tenerlo qui darebbe la maiuscola al
giocatore e non alle creature, dentro lo stesso messaggio.

💡 **La domanda della ripresa aveva risposta netta**: dei 71 `bufftxt`, **0**
erano già resi altrove. Non c'era riuso da raccogliere.

### 2. ⚠️ La toppa che non era nel piano: `sdim` non basta più

`sdim bufftxt, 30, 2, MAX_BUFF` dà 30 byte per elemento, e **il numero non è
casuale**: il giapponese più lungo ne occupa 28. L'inglese ci sta comodo perché
in `bufftxt(0)` mette solo il verbo. Dopo la toppa l'italiano porta la frase
intera e il più lungo ne occupa **59**, e accorciare non è una via d'uscita:
qualunque italiano che porti la frase intera passa i 30 byte.

💡 **La 28ª aveva ragione — `sdim` non è un tetto — e la controprova migliore
sta nel gioco**, meglio di `skilldesc`: `sdim buffname, 20, MAX_BUFF` e il
buffname **giapponese** più lungo ne occupa **22**. Upstream scrive già oltre il
dichiarato, e funziona.

⚠️ **Ma quella prova vale per un array a UNA dimensione.** `bufftxt` ne ha due,
e per il caso a due dimensioni **non c'è nessuna controprova nel gioco**, perché
né il giapponese né l'inglese ci arrivano mai. Il buffer è stato allargato a
128: costa `2 * MAX_BUFF * 98` byte e toglie la domanda invece di scommetterci.

💡 **Il vincolo delle rese è più stretto del solito**, e vale per il prossimo
che ci mette mano: il soggetto è `name(addbuff_charid)`, che può essere
**qualunque creatura** — «il cane», «la strega» — oltre al giocatore. Niente
participio e niente aggettivo che concordi col soggetto; dove ne serviva uno
l'accordo si è spostato su un nome che porta il proprio genere («una giornata
fortunata», «catene intrise di magia», «il corpo leggero come una piuma»).

## Le tre scoperte della trentunesima sessione

### 1. ⚠️ Due inglesi che si contraddicono, e chi arbitra è il giapponese

Il verso 「ガウッ」 sta in due punti del file: a `44170` l'inglese dice `*gulp*`,
a `52145` dice `*Growl*`. La resa vecchia era **`*gnam*`**, cioè seguiva
`*gulp*`. Ma ガウ è un **ringhio**, non un boccone, e la riga accanto —
「ガルル！」, `*grrr!*` — conferma il repertorio della bestia.

💡 **È una famiglia diversa da quella già nota.** Nella 26ª si era visto
l'inglese che *specializza* un giapponese generico (「がおー」 = `*creaking*` su
un golem di legno e `*growl*` su una divinità serpente): lì le due letture
convivono ed è legittimo. **Qui una delle due è semplicemente sbagliata**, e non
c'è modo di accorgersene senza aprire il giapponese.

⚠️ **Corrette tutte e due a `*ringhio*`**, e la correzione vecchia è andata **nel
dizionario**, non nel lotto. Il punto è che `--divergenti` **non si è mosso**:
rendendo solo il sito nuovo sarebbe salito a 14 e la divergenza sarebbe stata
mia. Costa una riga togliere il problema invece di registrarlo.

💡 **A trovarla è stata una rete dello script del lotto, non l'occhio.**

### 2. 💡 La chiave del lotto conviene che sia `(riga, en)`, non `(riga, jp)`

Il metodo della 27ª dice di chiavare il dizionario delle rese su `(riga, jp)`,
perché il referto stampa riga e giapponese. **Ma il giapponese va scritto a
mano, e due volte in questa sessione un codepoint era sbagliato** — `喧` scritto
`U+5583`, `鉾` scritto `U+9243`. Tutt'e due le volte si è fermata la prima rete,
quindi il danno è stato zero; ma è tempo perso a ogni lotto.

Dal lotto `041` la chiave è **`(riga, en)`**: l'inglese è ASCII e non si sbaglia
a copiarlo. ⚠️ Serve **una rete in più**, perché `(riga, en)` identifichi
davvero: due voci sulla stessa riga con lo stesso inglese e giapponesi diversi
esistono (è il riciclo inglese, 84 stringhe su 231 giapponesi), e in quel caso
la chiave va cambiata per quella voce. Nei lotti `041` e `042` non è successo.

⚠️ **`scratchpad/scheletro.py` non esiste** — la 33ª è andata a cercarlo e la
cartella `scratchpad/` non era mai stata creata. Generava le chiavi giapponesi
dall'estrazione, esatte per costruzione, ma era scratch di sessione ed è andato
perso. Chi preferisce `(riga, jp)` se lo riscrive, oppure usa `(riga, en)`.
✅ Da adesso la cartella c'è e i suoi script sono committati: vedi
`scratchpad/LEGGIMI.md`.

### 3. 💡 Una rete nuova: lo stesso giapponese due volte **dentro** lo stesso lotto

`rese_gia_decise()` legge il **dizionario**, quindi non vede due voci dello
stesso lotto che condividono il giapponese: non ci sono ancora. È la trappola
della 26ª (il punk e il teppista) in forma nuova, e nel lotto `039` era reale —
i due Yerleswood condividono 「突撃モード継続」 e 「対象ノ行動パターン解析中」 con
inglesi diversi, quattro firme in tutto.

La rete costa quattro righe: raggruppa le rese del lotto per giapponese e
**muore** se un giapponese ne ha due diverse. Da copiare in ogni lotto futuro.

## Le quattro scoperte della trentesima sessione

### 1. ⚠️ Sei rese facevano concordare col giocatore, e una era di quel giorno

Cercando la resa gemella di una battuta della sorella maggiore ne è saltata fuori
una vecchia — «Dove **sei andata** a finire» — che sbaglia in metà delle partite.
La ricerca estesa a tutto il dizionario ne ha trovate **sei su 9.254 voci**, e la
sesta l'avevo scritta io **nel lotto 029**, due ore dopo aver scritto la ricerca.
Tutte corrette. Il dettaglio, la tabella e la riga di comando stanno in
`decisioni.md`. 💡 **Va rilanciata a ogni lotto**: è un referto da leggere, non
una guardia, perché i falsi positivi sono legittimi.

### 1-bis. 💡 Le lettere latine dentro il giapponese non sono tutte uguali

La bolla drago (`db_creature.hsp`) dice due cose scritte in alfabeto latino, e
vanno in due direzioni opposte:

- 「Pon」 è un'**onomatopea giapponese** scritta in latino — non è inglese, e si
  rende in italiano: «Pop»;
- 「HAPPY END！！」 è **inglese anche per chi legge in giapponese**, come
  `Target Acquired.` dello spazzino, e si tiene. Dichiarato in `invariati.md`.

⚠️ Idem 「URYYYYYYYYYY」 del vampiro (lotto 030): non è inglese, è il grido di Dio
in JoJo, e sta in lettere latine in tutte e due le lingue. La domanda da farsi non
è «sono lettere latine?» ma **«è una parola inglese, o è un suono?»**.

### 2. ⚠️ Copiare una resa già decisa può renderla identica all'inglese

Due volte in otto lotti. 「スシ！」 è già reso «Sushi!» a `104858`, dove l'inglese
urla `SUSHI!!!`; a `83627` **lo stesso giapponese** ha inglese `Sushi!`, e la
copia — che è ciò che il progetto chiede — fa scattare la guardia sull'identità.
Non è un difetto della resa, è una proprietà di quel sito: si dichiara in
`invariati.md`, **citando sempre l'altro sito come prova**. Aggiunte due righe,
`Sushi!` e `...!`.

⚠️ **Il caso opposto esiste**: 「はああああ…っ！」 reso `Haaaaah...!` era davvero la
grafia inglese copiata, ed è diventato `Aaaaaah...!`. La differenza: chiedersi se
la resa sarebbe stata quella **anche senza** l'inglese sotto gli occhi.

### 3. ⚠️ Una battuta può avere il ramo inglese vuoto, e allora è fuori perimetro

`db_creature.hsp:86293` è `lang("「この格好じゃ動きにくい…！」", cnvtalk(""))`: il
giapponese ha la battuta, l'inglese ha la stringa vuota, e l'inglese che le
spetterebbe è slittato sul `lang()` successivo. `estrai.py` non la vede — non c'è
niente da sostituire — quindi non è né tradotta né contata. In tutto il sorgente i
rami inglesi vuoti sono **31**, e **30 sono legittimi** (particelle come `位`,
`歳`, `耐性`): questo è l'unico che è una frase. **Non si può toppare** (la riga ha
tre `lang()`). Annotata, come `iknownnameref`.

### 4. ⚠️ L'avviso «NOME NON TRADOTTO» di `battute.py` può essere falso

Scatta quando una creatura **condivide il nome** con una che il file elenca prima:
il dizionario è indicizzato per contenuto e tiene la voce alla **prima** riga, che
sta in un blocco `DBMODE_SET`, mentre lo strumento cerca `DBMODE_REF_SPEC`.
Successo con la sorella minore, il cui nome era reso da sessioni. Si legge come
«non l'ho trovato», e si controlla cercando il giapponese in dizionario.

## Le due scoperte della ventottesima sessione

### 1. ⚠️ Il conteggio dell'estrattore non era il costo, e la motivazione era falsa

La decisione 0 diceva: anticipare `buff.hsp` (199), `chara.hsp` (258),
`item_func.hsp` (263), `screen.hsp` (103) perché sono ~830 firme ad alta
frequenza in coda a tutto. I numeri sono giusti — rimisurati tutti — ma **non
sono il costo**, e per il file che portava l'argomento erano metà della verità.

**Ogni messaggio di `buff.hsp` è spezzato in due e solo la prima metà sta in
`lang()`:**

```hsp
bufftxt(0, BUFF_HOLY_SHIELD) = lang("は光り輝いた。", " begin"), " to shine."
```

È un'assegnazione di **due** elementi. Il secondo (`" to shine."`) è un
letterale nudo, invisibile al dizionario: **70** in quel file. Tradurre le 199
voci contate darebbe «Nome inizia to shine.»

**E il messaggio si compone solo nel ramo inglese**, in un blocco custom del mod
(`chara_func.hsp:2316-2375`, `BLOODYSHADE CUSTOM`) che usa `_s()` e **sette casi
speciali** anch'essi scritti come letterali nudi (` mind...`, ` out the power of
his armor.`). ⚠️ **La riga originale, l'unica con `lang()`, è commentata**
(`:2310`). Il ramo giapponese (`:2377`) usa invece un **frammento unico**:
`name(id) + bufftxt(0, id)`.

💡 **Quindi la strada è una toppa, non 90 rese**: riportare il ramo inglese alla
forma giapponese — frammento unico, via `_s()`, via i sette casi — scioglie ~90
messaggi in un colpo. Togliere una morfologica si può; il resto è lavoro
strutturale e va fatto **prima** delle rese, non dentro un lotto.

⚠️ **E la motivazione scritta nella ripresa era inventata.** Diceva che i nomi
degli status «stanno nell'HUD in permanenza»: l'HUD ne disegna le **icone**
(`gcopy`, `screen.hsp`), non il testo. Il nome come testo esce nel popup sopra la
testa (`chara_func.hsp:2389`, `:2455`), in «The effect of X ends.» (`:2404`) e
nella lista dei potenziamenti della scheda (`command.hsp:2005`, `:10800`).
Frequenza alta comunque, conclusione salva — ma la prova era falsa.

⚠️ **`screen.hsp` non è «etichette fisse dell'interfaccia».** Solo **9** delle
103 voci sono statiche (`Gauge Ready`, `Autopickup`, `Blood`): le altre **94**
sono dinamiche, ed è la scena degli dèi che ti parlano mentre stai morendo.

💡 **`chara.hsp` invece costa molto meno di quanto dice il numero**: 258 firme ma
**143 testi distinti**, e **87** sono la stessa frase, «You have learned a new
ability, X.»

**La misura da rifare, con lo strumento che ancora non c'è:** contare i letterali
inglesi **fuori** da `lang()` per file, filtrando percorsi, nomi di file e chiavi
di `#define`. ⚠️ **La prima passata grezza era in `scratchpad/fuori_lang.py`,
che non esiste più** (vedi sopra: la cartella non era in git, e il file è andato
perso con lo scratch della sessione). I numeri che aveva dato — da rifare, non
da fidarsene — erano 70 (`buff.hsp`), 55 (`chara.hsp`), 120
(`item_func.hsp`), 175 (`screen.hsp`), 204 (`main.hsp`), 13 (`item.hsp`) — ma
per tutti tranne `buff.hsp` è **quasi tutto rumore**, e senza il filtro il costo
di quei file resta ignoto. È la stessa classe delle sette intestazioni del
diario e di `main.hsp:227`.

Concetto nuovo: [[un-conteggio-non-e-una-stima-di-costo]] nel vault.

### 2. 💡 `sdim` non è un tetto: HSP riespande in scrittura

`sdim buffname, 20, MAX_BUFF` sembra dire che un nome di status non può passare
i 19 byte, e un tetto del genere in italiano si sfonda subito. **Non è così.**
La controprova sta già in gioco: `skilldesc` è `sdim skilldesc, 40, MAX_SKILL` e
contiene una resa da **59 caratteri** («Memorizza incantesimi. Migliora
pergamene. Analizza nemici.»), vista a schermo nella lista abilità.

⚠️ Vale in **scrittura**. Il limite vero resta quello del **riquadro** che
disegna, che si misura a parte — e l'altra faccia, già nota, è che
l'autoespansione **non** vale in lettura: un array sparso letto oltre l'ultimo
indice assegnato è un `Array overflow`.

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
| `buff.hsp` | 199 | i **nomi degli status** («Holy Shield», «Speed», «Regeneration») e i messaggi «X inizia / svanisce». ⚠️ **«Stanno nell'HUD in permanenza» era falso** — l'HUD disegna le icone; e le 199 voci sono **metà** dei messaggi: vedi la scoperta 1 della 28ª |
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

### ⚠️ E poi i due passi che questo elenco non nominava

`reimporta` scrive **nel dizionario e basta**. L'albero di build resta com'era, e
`compila` senza argomenti produce solo `start.ax`, **non** l'eseguibile. Chi si
ferma qui vede la catena tutta verde e prova in gioco una build **che non
contiene le rese nuove** — ed e' successo nella 33ª, che ha annunciato due volte
un `cgx-test.exe` rifatto quando l'eseguibile era quello del giorno prima.

```powershell
python -m strumenti.applica                # dizionario + toppe -> albero di build
python -m strumenti.compila --eseguibile   # e SOLO cosi' esce l'exe
copy "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" `
     "C:\Games\Elona\elonaplus2.31\cgx-test.exe"
```

💡 **Come ci si accorge che manca `applica`**: si apre il `.hsp` di build alla
riga appena tradotta e ci si legge ancora l'inglese. La catena delle verifiche
**non** lo vede, perche' legge il dizionario e il sorgente pinnato, non la build.
⚠️ E `applica` **ricrea l'albero da zero**, quindi cancella l'exe che c'era: se
dopo `applica` non si ricompila, in `build/` non c'e' nessun eseguibile.

Fatti `fase2-battute-001` … `-042`, e con il `042` **il file è chiuso**. Il
metodo resta scritto qui perché serve tale e quale al prossimo file a battute.
Dopo aver rigenerato l'estrazione le creature già fatte spariscono, quindi si
riparte sempre da `[0]`.

💡 **Il referto stampa solo l'inglese, e l'inglese non arbitra.** Serve il
giapponese sotto gli occhi: nella 30ª il lotto si è sempre letto con uno script
di dieci righe che chiama `battute.repertori()` e scrive `riga / classe / jp / en`
su un file di testo, comprese le note «GIÀ RESO ALTROVE» e la forma grezza delle
dinamiche. Senza quello si traduce l'inglese, che è la cosa che il progetto ha
deciso di non fare.

💡 **Il lotto si scrive con uno script, non a mano.** Dalla 27ª il metodo è: un
file Python nello scratchpad con un dizionario `{(riga, jp): resa}` e un
controllo che **muore** se una resa non aggancia nessuna voce. Chiave `(riga,
jp)` e non la firma, perché il referto stampa riga e giapponese. Costa dieci
righe e ha già evitato due lotti scritti sulla voce sbagliata.

💡 **Tre guardie che `verifica` non fa e che conviene rilanciare a mano** sul
JSONL del lotto: nessun carattere a doppia larghezza tranne `♪`; nessuno dei
proibiti (`…`, `“”`, `～`, `«»`); nessuna parola inglese residua (`the`, `you`,
`your`, `is`, `my`…) in una statica che non sia dichiarata invariata.

💡 **Lo script del lotto tiene cinque reti**, e conviene copiarle tutte:

0. la chiave **identifica una voce sola** (serve solo se si chiava su `en`);
1. nessuna voce senza resa;
2. nessuna resa che non aggancia niente;
3. nessuna resa che **diverge da una già decisa** per lo stesso giapponese —
   ⚠️ questa **non deve uccidere lo script**, deve stampare: nella 31ª la
   divergenza segnalata era giusta ed era la resa *vecchia* a essere sbagliata;
4. ⚠️ **nessun giapponese reso in due modi dentro il lotto stesso**, che la 3
   non vede perché legge il dizionario.

Nella 31ª la 1 ha fermato due volte un codepoint sbagliato e la 3 ha trovato
`*gnam*`. Le reti hanno lavorato più dell'occhio.

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

### Trovate nella trentunesima

- ⚠️ **Il maiuscolo dei robot lo porta il katakana, non l'essere una macchina.**
  Metal Vesda (`92618`) e i due Yerleswood scrivono le particelle in katakana
  (`ノ`, `ヲ`, `スル`) e vanno in maiuscolo; l'androide di `122654` e `<Mani>`,
  che è il **dio delle macchine**, parlano giapponese normale e restano in
  minuscolo. La domanda è sul katakana, non sul personaggio.
- 💡 **Un bisticcio di segmentazione si rifà tenendo insieme le due letture.**
  「この先生きのこるためには！」 si legge «sopravvivere d'ora in poi» e «questo
  maestro fa i funghi»; l'inglese lo butta via e scrive `Live!`. Reso «Di qui in
  avanti, o si sopravvive o si fa da concime ai funghi!», che dice tutt'e due.
  Stessa famiglia: 「受けて断つ…もとい、受けて立つ！」 → «Ti faccio a fette...
  cioè, ti faccio fronte!».
- ⚠️ **Un idioma tradotto alla lettera dall'inglese non è una specializzazione,
  è un errore.** 「腕が鳴る」 è «mi prudono le mani» e l'inglese scrive `It's
  called arm ringing`; 「引き際を間違えた」 è il momento sbagliato per ritirarsi
  e l'inglese ci legge un grilletto; 「引導を渡す」 è dare l'estremo saluto e
  l'inglese scrive `I'll give you guidance`.
- 💡 **Una citazione in bocca a un personaggio si rende con la versione italiana
  che esiste già**, e la lista continua: 「計画通り」 è Light in Death Note
  («Tutto secondo i piani»); 「テケリ・リ」 è Lovecraft e in italiano si scrive
  uguale; 「でーんでんむーしむし」 è la filastrocca della chiocciola e si rende
  con quella italiana; 「ご飯にするん？お風呂にするん？それとも…」 è la battuta
  della moglie che aspetta a casa, dove `<Yacatect>` mette l'obolo al posto di
  sé stessa.
- ⚠️ **Il contrario esiste e va nell'altra direzione**: 「Destroy！Dynamite！」 e
  「Noooooooooo！」 stanno in **lettere latine anche nel giapponese**, quindi si
  tengono. La domanda resta quella della 30ª — «è una parola inglese, o è un
  suono?» — con una seconda prova quando la resa coincide con l'inglese:
  *sarebbe stata questa anche senza l'inglese sotto gli occhi?*
- 💡 **Il nome di un incantesimo dentro una battuta si copia, e se il giapponese
  lo tronca si tronca uguale.** 「ファイアボル…？」 è `ファイアボルト` mangiato
  dalla memoria di `<Raizel>`: la resa parte da «Saetta di fuoco»
  (`skill.hsp:509`) e diventa «saetta di fuo...?».
- ⚠️ **Un vocativo sbagliato di proposito resta sbagliato di proposito.**
  `<Raizel>` scambia il giocatore per sua moglie e lo chiama `ばあさん`
  **comunque sia il giocatore**: il vocativo porta lo scherzo — «nonnina» — e
  tutto il resto della frase resta invariante. È la stessa forma di `_syujin`.
- 💡 **Il ♪ è l'unico carattere a due byte che ci resta, e il ☆ si perde.**
  「シャドウシスター推参ッ☆」 ha perso la stella: CP932 non la codifica. È una
  perdita silenziosa, non una scelta.

### Trovate nella trentesima

- ⚠️ **Un vocativo che il giapponese non declina non può diventare italiano
  declinato.** La `マスター` del terminale Xeren non è `_syujin`: è un letterale, e
  «Padrone» sbaglierebbe metà delle partite. Reso **«Comandante»**, che vale per
  entrambi i generi ed è anche giusto per un'arma da guerra. Stessa famiglia:
  `先生` dell'insegnante, il cui nome italiano non porta genere.
- 💡 **Il katakana come tic si rende in maiuscolo.** Vale per i robot (Gilphem,
  Metal Vesda, l'apparato di comunicazione), per la carota ninja che parla tutta
  in katakana, e **a metà parola** per il soldato yerles infetto, dove il
  giapponese si sfalda dentro la parola: «A... A... che maLE... CHE MALE...».
- 💡 **Una citazione si riconosce dal giapponese e si rende con la versione
  italiana che esiste già**: 「またつまらぬものを噛んでしまった」 è Goemon di Lupin
  III col morso al posto del taglio; 「お前もまた、強敵（とも）だった」 è la
  convenzione di Hokuto no Ken, dove «nemico forte» si legge «amico», e la resa
  tiene tutte e due le letture.
- 💡 **Un bisticcio si rifà sul materiale italiano già deciso**: il giapponese
  「HはHでもHitmanの方だがなぁーっ！」 gioca sulla lettera H, e in italiano la
  lettera diventa la **S** del nome che il progetto aveva già scelto, «La S sta
  per Sicaria, mica per Sesso!». Idem 「イガいとやるな…」, dove イガ è il riccio
  della castagna nascosto dentro 意外と: «e io di ricci me ne intendo».
- ⚠️ **L'allungamento giapponese si porta con le vocali ripetute**, e quando la
  parola allungata la scrive una funzione — `_onii` — l'allungamento passa nella
  coda: i sette modi in cui la sorella minore chiama il giocatore diventano
  `!`, `!!`, `...`, `...♪`, `...?`, `...!`.
- 💡 **Una preghiera non si translittera: si rende con la formula italiana.**
  「南無三ッ」 della samuraformica è «Che il cielo mi assista!», 「南無阿弥陀仏」
  dell'infernello è «Pace all'anima sua».
- 💡 **Le citazioni continuano ad arrivare, e le riconosce solo il giapponese**:
  「時を止めた者が…」 è JoJo (l'inglese al suo posto scrive «Hey, c'mon c'mon!»),
  「わけがわからないよ」 in bocca a una fata è Kyubey, 「あくまでメイドですから」
  è il maggiordomo di Kuroshitsuji col bisticcio su «diavolo».
- 💡 **La narrazione dentro `cnvtalk` si rende narrazione lo stesso**, anche se
  le virgolette che la funzione aggiunge la fanno sembrare parlato: è quello che
  il progetto fa già dal fratellino di `82821`, visto a schermo.

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

0. ✅ **Deciso il 12/08, e la premessa era sbagliata**: il blocco di Fase 4
   **non** si anticipa in blocco. Si anticipano solo i **~90 `buffname`**; i
   `bufftxt` diventano lavoro strutturale a parte; `chara.hsp`, `item_func.hsp`,
   `screen.hsp` e `main.hsp` restano dove sono finché non c'è il conteggio dei
   letterali fuori da `lang()`. Vedi la scoperta 1 della 28ª.
   ✅ **Fatto il 13/08**: `buffname` e `bufftxt` sono chiusi, restano i
   `buffdesc`. ⚠️ **Il conteggio dei letterali fuori da `lang()` non è ancora
   stato fatto**, e finché non c'è, il costo di `chara.hsp`, `item_func.hsp`,
   `screen.hsp` e `main.hsp` resta ignoto. 💡 Adesso però si sa che cosa
   cercare: `buff.hsp` è il caso risolto, e la forma del difetto — una frase
   spezzata in due con solo la prima metà dentro `lang()` — è quella che lo
   strumento deve saper riconoscere.
1. ✅ **le battute di `db_creature.hsp`**: chiuse il 2026-08-13, lotti `015`-`042`;
2. **`proc.hsp`**, 971 firme, per zona di riga da **1716**;
3. `command.hsp`, `trait.hsp`;
4. `ai.hsp` (94) ed `event.hsp` (649);
5. `chara_func.hsp`, le 286 rimanenti — ⚠️ dentro ci sono le tre pietre di
   Lesimas e l'ankh del sole, **già rese** in `text.hsp:11576-11594`: si
   **copiano**. E la causa di morte (`:6850`), che va insieme a `main.hsp:4409`;
6. `init.hsp` (133) — ⚠️ lì sta la decisione sul possessivo `his(x, 1)`;
7. i nomi non identificati di `db_item.hsp` e le 2.555 descrizioni.

## Domande aperte

⚠️ **`CDATA_SEX` e il registro giapponese si contraddicono, e capita più di una
volta.** L'`<Ex spazzino>` (`95309`) ha `CDATA_SEX = 0`, cioè maschio, ma parla
al femminile (`やだー`, `ですよ`, `ところね`); `<Urcaguary>` (`71913`) ha
`CDATA_SEX = 1` e parla da vecchio guerriero (`フハハ`, `殺せ`, `肉を食え`);
`<Egelveil>` (`63370`) è femmina e usa `〜のだ`. Nella 31ª **la questione non è
stata decisa**: dove serviva un accordo la frase è stata girata («non ho
combinato niente»), che è la stessa tecnica usata per il giocatore. 💡 La regola
scritta dice che *il codice arbitra sullo stato del gioco*, quindi in teoria
vince `CDATA_SEX` — ma non è mai stata messa alla prova su una creatura che
parla chiaramente dell'altro genere, e **a schermo non l'ha vista nessuno**.

⚠️ **`db_creature.hsp:86293`, la battuta col ramo inglese vuoto**: si allarga
`estrai.py` alle voci con inglese vuoto — e allora `applica` deve saper scrivere
dentro un `cnvtalk("")` — oppure resta fuori perimetro per sempre. Rinviata, non
dimenticata. È l'unica frase fra i 31 rami vuoti del sorgente.

⚠️ **`battute.py` aggancia i nomi per riga e non per `dbid`**, e per questo dà
«NOME NON TRADOTTO» a chi condivide il nome con una creatura elencata prima. La
correzione tocca la funzione che compone i lotti e non si fa dentro un lotto.

✅ **Il menu tattiche del mod è stato guardato il 13/08, e la risposta è la
peggiore delle tre: `cs_list` non taglia, sconfina.** Le colonne si
sovrapponevano davvero — «Crescita della destre**Cambio di forma (A)**». Il
tetto vero è **20 caratteri** (145 px / 7,2), non 13 come si stimava, e lo
passavano **10 `buffname` su 71**, adesso zero. ⚠️ Restano da sistemare due
cose: la stima vecchia diceva `Schivata d'emergenza` fuori misura e **non lo
era** (20 esatti), e il sito che conta di più — l'elenco degli status sul
personaggio — **manda a capo da solo a 70 caratteri** e non è a rischio. Vedi
`decisioni.md`, «Due tetti che nessuno aveva misurato» e «Dove finisce un nome
di status».

⚠️ **Gli altri tre elenchi a colonne di `custom_ai.hsp` non sono guardati, e
lì l'ancora dice il contrario.** Sono `:1263`, `:1337` e `:1821`, con un passo
di **150 px su quindici righe** (contro i 145 su ventidue del menu dei
potenziamenti), ed elencano azioni e **nomi di incantesimo**, che sono tradotti
al 100%. Il tetto è sempre 20 caratteri, e lo sfondano **15 nomi italiani su
445** — ma lo sfondano anche **5 inglesi**, fino a 24 (`Critical Particle
Cannon`, `Thread of Innervation`). 💡 **È la famiglia dei `buffdesc`, non
quella dei `buffname`**: un tetto che upstream accetta già rotto, quindi non è
un vincolo che la resa italiana debba rispettare. E accorciare un nome di
incantesimo per far stare un menu del mod lo peggiorerebbe in tutti gli altri
posti dove sta benissimo. ⚠️ **Prima di decidere va guardato a schermo**: si
apre parlando a un alleato → *Teach a spell or ability*.

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
niente della causa. Successo l'11/08. ⚠️ **E di nuovo il 13/08**, con un
sintomo diverso e più chiaro — `PermissionError: [WinError 32] ... utilizzato
da un altro processo` sulla `rmtree` di `applica`. La colpevole era una shell
di lavoro entrata lì dentro per leggere il sorgente. Si esce e si rilancia:
`applica` riparte da capo senza danni.
⚠️ Se `applica` viene interrotta lascia l'albero **incompleto**: si rilancia e
basta.

⚠️ **Controllare la data dell'exe prima di fidarsi di uno screenshot.**

**L'eseguibile in `cgx-test.exe` è della 34ª (14/08/2026 02:45, 17.588.604
byte)** e contiene tutto quello di prima — le battute di `db_creature.hsp`, i
`buffname`, le due toppe di `buff.hsp`, i 71 messaggi dei potenziamenti, i 63
`buffdesc` e le 24 toppe della 33ª — più la correzione dello spazio nella scena
ricucita. Compilato senza errori, **13.146 sostituzioni**, e con le tre rese di `chips.hsp`.

✅ **I messaggi dei potenziamenti sono stati visti a schermo il 13/08, e la
toppa regge.** Con `add_ally 249` e una bacchetta di velocità (`spawn_item 377`,
si punta con `z`) è uscito «**Aranart la sorella minore diventa piu' agile.**»:
nome minuscolo con l'articolo dentro — cioè `cnven()` è tolto per davvero —
frase unica, nessun residuo tipo « up.», nessun accordo. ✅ Provato anche sul
**giocatore**, che è il caso da cui il `cnven()` era stato tolto: regge.
💡 «Aranart» non è nostro: `db_creature.hsp:117782` compone
`randomname() + " " + nome`, ed è la stessa cosa che upstream fa in inglese.

💡 **Come si prova un potenziamento**: la console **non ha un comando** che li
applichi. La via corta è la **bacchetta di velocità**, `spawn_item 377`, che si
raccoglie con `,` e si punta su chiunque con `z`.

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
- 🆕 **La lista data a fine 28ª, mai tornata** (l'eseguibile attuale la mostra
  già, non serve ricompilare):
  ```
  add_ally 408   <Lune>: deve chiamare «Padrone!!», due punti esclamativi
  add_ally 326   il menestrello: canticchia, non canta parodie inglesi
  add_ally 620   il corvo mercante: parla come un bottegaio
  add_ally 709   il gufo spaziale: tre versi storpiati DI PROPOSITO
  ESC, poi tenere premuto 5 per ~40 turni
  spawn_chara 32    lo spazzino: parla INGLESE per scelta; se stona si ridiscute
  spawn_chara 471   l'addetto del casinò: attaccarlo e ucciderlo
  ```
- 🆕 **Dai lotti 027-034 della 30ª** (ID verificati in `defines/mod.hsp`).
  ⚠️ **La colonna «come» non è un dettaglio**: quattro di queste creature non
  hanno battute oziose e davanti a loro si aspetta invano. Corretto il 13/08.
  ```
  ASPETTA (add_ally, poi tieni premuto 5)
  249   la sorella minore: sette modi di chiamarti, tutti su _onii
  364   la sorella maggiore: parla di se' come «la sorellona»
  773   il toro blu: quattro muggiti, uno e' «Mo' basta...»
  829   la carota ninja: parla TUTTA IN MAIUSCOLO, e' voluto
  508   l'apparato di comunicazione: robot, tutto maiuscolo
  616   la samuraformica (parla da samurai)
  351   il guerriero dalla testa di leopardo: Janus, <Silvia>, torque

  ATTACCA (spawn_chara, e fatti attaccare: escono le offese)
  465   il soldato yerles infetto: le maiuscole a meta' parola
  627   il Gigante Castagna
  829   616   351   (hanno anche le offese, oltre alle oziose)

  TORNA A CASA (solo il bentornato: entrare in AREA_HOME con loro nell'area)
  502   il terminale Xeren: deve dire «Comandante», non «Padrone»
  492   <Pascal>: abbaia, e le tre rese sono bau / bau bau / arf
  ```
  ⚠️ **502 e 492 non hanno oziose**: la lista vecchia diceva di aspettarle, ed
  è per questo che non tornava niente. Il loro bentornato è l'unica via comoda;
  le altre battute che hanno sono morte e uccisioni.
  Il toro e la carota servono a decidere una cosa che solo lo schermo decide:
  **se il maiuscolo del katakana regge o urla troppo**.
- 🆕 **Dai sei lotti 037-042 della 31ª** (ID verificati in `defines/mod.hsp`).
  ⚠️ Sono tutte creature di livello altissimo: `add_ally` serve proprio perché
  incontrarle per caso non capita. Lista rifatta per classe il 13/08 — **otto
  di queste quindici non parlano se aspetti**.
  ```
  ASPETTA (add_ally, poi tieni premuto 5)
  796   <Aribel>: le sette regole — ✅ vista la numero uno il 13/08
  805   <Renai>: fratello e sorella, «forma umana»
  628   <Raizel>: ti chiama «nonnina», e «saetta di fuo...?» mangiata
  842   la <Kunoichi alla moda>: «Sorella dell'Ombra»
  654   <Marka>: «Orsa a chi!»
  383   l'<Ex spazzino>: «con le chiocciole ho fatto pace»
  382   la <Lumaca> in sella all'androide: la filastrocca, e
        «Destroy! Dynamite!» che resta in inglese di proposito

  ATTACCA (spawn_chara, e fatti attaccare: escono le offese)
  601 e 664   i due Yerleswood: MAIUSCOLO, e le due frasi in comune
              devono uscire IDENTICHE — ⚠️ mezza prova il 13/08
  686   <Regulus>: il fratello, «forma umana»
  379   <Siva>: quattro versi da cane, non «Woof»
  911   <Tezcatlipoca>: «Mi prudono le mani», «Ti avvolgo nel fumo»
  756   <Shuraida>: il concime ai funghi
  534   <Aile>: annunci di bordo, poi il dialetto ruvido

  UCCIDI (la battuta esce morendo)
  640   <Sinaha>: «Miaosa... come...» — ⚠️ livello 250
  331   <Ehekatl>: ripete l'ultima parola — ⚠️ ha solo uccisione e bentornato
  ```
  💡 **Le tre cose che solo lo schermo decide**, aggiornate al 13/08:
  1. se «Miaosa» si legge o sembra un refuso — **ancora aperta**, ed è una
     battuta di **morte** su una creatura di livello 250;
  2. se le due frasi dei Yerleswood escono uguali — **mezza prova**: «AVVIO
     L'AGGIORNAMENTO DEI DATI DI COMBATTIMENTO.» è uscita due volte identica,
     ma il log non dice *chi* l'ha detta, quindi potrebbero essere due volte
     lo stesso. Serve vederne una seconda, o la riga lunga;
  3. ✅ **se il maiuscolo dei robot regge: sì.** «AVVIO L'AGGIORNAMENTO DEI
     DATI DI COMBATTIMENTO.» si legge bene e non urla. Manca la riga più lunga
     («ANALISI DEGLI SCHEMI DI COMPORTAMENTO DEL BERSAGLIO IN CORSO.»), ma il
     dubbio era sul principio e il principio tiene.
  ⚠️ **E in quel combattimento è saltato fuori «l'Yerleswood di serie»**,
  corretto in «**lo** Yerleswood»: vedi `decisioni.md`.
- ⚠️ **Il non tradotto esce in inglese, non in giapponese.**

## I tetti misurati, con la loro ancora

| campo | tetto | ancora | fonte |
|---|---|---|---|
| tracciatore HUD | 6 | sinistra, taglia | `screen.hsp:2002` |
| razza e classe | 3 | sinistra, taglia | `chara.hsp:4679` |
| slot d'equipaggiamento | 6 | sinistra, taglia | osservato a schermo |
| gradi di resistenza | 9 | **destra, invade** | `command.hsp:11002` |
| nome nella lista abilità | **24** | sinistra, invade il costo | `command.hsp:5382` |
| descrizione, menu `a` | 34 | taglia (`strmid`) | `command.hsp:5389` |
| descrizione, menu `W` | 34 | idem | `command.hsp:5599` |
| **descrizione, menu di lancio** | **40** | idem | `command.hsp:8851` |
| **descrizione, scheda incantesimi** | **46** | idem | `command.hsp:10996` |
| **voce di menu** | **(px − 46) / 7,7** | sinistra, taglia | `strumenti/larghezze.py` |
| **riga di diario** | **36** | **manda a capo, ultima parola scappa** | `strumenti/diario.py` |
| **riga di notizia** | **33** | idem | `addnews2`, `text.hsp:12106` |
| **riga del compenso** | **30** | idem | `text.hsp:11885` |
| pagina del diario | ~40 | taglia | osservato a schermo |
| nome di oggetto | 66 | oltre, passa da `zentohan` | `item_func.hsp:2254` |
| **colonna del menu tattiche** | **20** = 145 / 7,2 | **destra, sconfina sulla colonna** | `custom_ai.hsp:3173` |
| **etichetta di stato, HUD** | **11** = (80 − 6) / 6,6 | destra, taglia al bordo | `screen.hsp`, `gcopy 65+en*15` |
| **etichetta di stato larga** | **13** = (95 − 6) / 6,6 | idem | `screen.hsp`, `gcopy 65+en*30` |

💡 **I tre tetti nuovi si contano in caratteri e non si stimano**, perché il
carattere della build inglese è **`Courier New`** (`config.txt`, `font2.`), che
è monospaziato: 7,2 px a 12 px di corpo, 6,6 px a 11. Misurati e verificati a
schermo il 13/08 — «Marchio letal» sono esattamente 13 caratteri.
⚠️ **Nessuno dei tre ha una guardia**: `larghezze.py` guarda solo i menu che
passano da `*prompt_key`. È il lavoro numero 0 della prossima sessione.
⚠️ **E il tetto si misura sulla forma degradata**: `volonta'` è 15 caratteri,
`volontà` 14, e a schermo ci va la prima.

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
