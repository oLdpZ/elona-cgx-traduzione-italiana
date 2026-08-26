# scratchpad

Script che non sono strumenti — non hanno test e non stanno nella catena delle
verifiche — ma che **servono a ogni lotto** e che finora ogni sessione riscriveva
da capo.

⚠️ **Fino alla 33ª questa cartella non esisteva.** `RIPRESA-sessione.md` citava
`scratchpad/scheletro.py` e `scratchpad/fuori_lang.py` come se fossero qui: non
c'erano, erano scratch di sessione ed erano andati persi. È la stessa trappola
della 28ª — lavoro fuori da git — in forma minore. Quello che serve due volte
si committa.

| file | a cosa serve | quando si lancia |
|---|---|---|
| `simili.py` | risponde alla domanda della 29ª (*questo file nomina cose che un altro ha già nominato?*) **per somiglianza** e non per stringa esatta: `difflib` a 0,55 sul giapponese, tre candidati per voce, scrive `lavoro/_<x>_simili.txt` | all'apertura di ogni file nuovo, **prima** di tradurre |
| `gia_rese.py` | la stessa domanda per **identità esatta**: veloce, ma da solo dà un falso no | insieme a `simili.py` |
| `guardie.py` | le tre guardie che `verifica` non fa: doppia larghezza tranne `♪`, caratteri proibiti (`…` `“”` `～` `«»`), inglese residuo nelle statiche | su ogni JSONL di lotto, dopo `verifica` |
| `referti.py` | la nona e la decima verifica d'apertura: participi che concordano col giocatore, ed elisioni davanti a consonante. **Referti da leggere, non guardie** — i falsi positivi sono legittimi | all'apertura e a ogni lotto |
| `cerca.py` | cerca nel dizionario le voci il cui giapponese contiene un termine, o il cui inglese è esattamente uno: serve a costruire il glossario di un file nuovo | prima di tradurre |
| `repertorio.py` | il repertorio già reso di una creatura: la sua riga di nome più le battute intorno. **Il modo di ritrovare il registro di un personaggio invece di ridecidérlo** | quando un file fa parlare qualcuno che `db_creature.hsp` ha già fatto parlare |
| `zona.py` | dump di una zona di righe dell'estrazione con jp/en grezzi | per scegliere e leggere il lotto |
| `chiavi.py` | le chiavi `(riga, en)` esatte di una zona, da incollare nello script del lotto | subito dopo `zona.py` |
| `istogramma.py` | dove si addensano le voci che restano, per scegliere la zona | all'apertura di un file grosso |
| `trova.py` | cerca frammenti inglesi nell'estrazione: serve a trovare una scena, non una riga | quando si cerca «dov'è il log di combattimento» |
| `rese.py` | le voci **già rese** di un file che contengono un frammento: il modo di scoprire la convenzione che le sessioni passate hanno applicato senza dichiararla | ⚠️ prima di scegliere tempo verbale o stile |
| `blocchi_en.py` | ⚠️ **le righe con letterali inglesi nudi dentro `if ( en )`**, che `estrai.py` non vede e che nessun conteggio di «non tradotte» include. Senza argomenti misura tutto il sorgente. È il filtro non rumoroso che la 28ª cercava: lì dentro tutto è testo che il giocatore legge, per costruzione | all'apertura di ogni file, **prima** di fidarsi del conteggio |
| `genera-toppe-en.py` | genera le toppe su quelle righe: allarga il blocco `cerca` finché non è **unico** (`applica` si ferma anche sulle toppe ambigue) e **degrada gli accenti**, che per le toppe `applica` non degrada | dopo `blocchi_en.py` |
| `aggiungi-toppe.py` | aggiunge toppe a `toppe.jsonl` senza duplicare, con identità `(file, cerca)` | dopo il generatore |
| `code-virgolette.py` | trova le teste e le code di una frase spezzata fra `if ( en )` e `lang()` | quando una voce è un frammento |
| `fuori_elenco.py` | i file del sorgente con `lang()` e **senza file di dizionario**: chiude con una misura la domanda della 26ª («esiste un file che nessun elenco nomina?»). Atteso al 14/08: **54 file con `lang()`, 14 col dizionario, 40 senza, per 12.620 stringhe**. ⚠️ «Senza dizionario» vuol dire **non ancora cominciato**, non «fuori perimetro»: `SPEC.md` §6 mette in Fase 4 «i restanti 63 file minori», che li copre tutti | quando viene il sospetto che un file sia sfuggito |
| `tetti_buffdesc.py` | i `buffdesc` contro i **tre** tetti che li tagliano (34 nei menu `a` e `W`, 40 nel menu di lancio, 46 nella scheda), italiano **contro l'inglese di monte**. Nato nella 34ª, quando a schermo è uscito `Res+ gra`. Atteso: l'italiano sfonda **meno** dell'inglese a tutti e tre (43/32/23 contro 46/38/31) — se un giorno lo supera, allora sì che c'è da accorciare. ⚠️ Stima le variabili interpolate a due cifre: il confronto regge, i valori assoluti hanno ±1 per voce | quando si tocca un `buffdesc` |
| `else_jp.py` | ⚠️ **il punto cieco di `blocchi_en.py`**: gli stessi letterali inglesi nudi, ma nella forma `if ( jp ) { … } else { … }`, che il fratello non vede perché cerca `if ( en )`. Nato nella 34ª, quando la follia di `calculation.hsp:2352` è uscita in inglese a schermo. Atteso: **6.984 righe in 13 file**, di cui 6.840 sono le descrizioni di `db_item.hsp` già fuori perimetro — le vive sono **144** | insieme a `blocchi_en.py`, all'apertura di ogni file |
| ⭐ `lang-nel-ramo-jp.py` | ⚠️ **il QUINTO punto cieco, ed è il rovescio di `else_jp.py`**: le `lang()` chiuse dentro un `if ( jp ) { … }`, che in italiano non girano mai. Nato nella 45ª su `command.hsp:2954`, il diario delle statistiche: settanta righe nel ramo giapponese con dentro sette `lang()` vere, e un `else` che stampa le stesse cifre in inglese nudo. È la **terza famiglia di riga morta** dopo il `;` e il `/* … */`, e la prima che non si vede: la riga è viva, il file è vivo, la `lang()` è vera — a spegnerla è il **ramo della lingua**. Atteso: **21 righe, 0 già tradotte** — 11 in `command.hsp` (tutte rinviate), 9 in `main.hsp` (**rinviate nella 58ª**: la finestra dei comandi per principianti, che in inglese non esiste — le nove righe hanno tutte lo stesso segnaposto «Essential is normal mode.»), 1 in `item_func.hsp`. ⭐ Nella 58ª questa spia ha **fermato nove rese gia' pronte**: erano le ultime voci di `main.hsp` e sembravano lavoro da fare. ⚠️ **Se «già tradotte» sale sopra 0, un lotto ha speso lavoro su testo morto.** 💡 Il filtro del letterale non è un dettaglio: senza, `font lang(cfg_font1, cfg_font2)` gonfiava il conto a 24 e faceva comparire `system.hsp`, che di testo non ne ha nemmeno una riga | all'apertura di un file, insieme a `blocchi_en.py` e `else_jp.py` |
| ⭐⭐ `tetto-equip.py` | **il nome dell'oggetto contro i tetti della finestra dell'equipaggiamento** (58ª), trovati **a schermo durante il collaudo** e poi confermati dal codice: `command.hsp:12741`, del mod MMAH, fa `strmid(s, 0, 12 + (showresist == 1) * 14)`. Col tasto `z` spento **nessun taglio**; con le sigle degli elementi **26**; con le pagine delle abilità **12** — «un elmo di b», «un paio di s». ⚠️ **Non è un `sdim` frainteso**, che è la trappola in cui il progetto è caduto quattro volte: è uno `strmid`. ⚠️ **E non è una regressione nostra** — degli stessi sette oggetti ne sforavano tre anche in inglese — ma l'italiano lo sfonda quasi sempre, perché le qualifiche vanno in **coda**: «a cursed bronze helmet [0,1]» sta in 28 caratteri, «un elmo di bronzo [0,1] con maledizione» in 39. ✅ La toppa alza il primo addendo da 12 a 14 (26→28, 12→14) recuperando i **28 px** misurati fra la fine del nome e la prima sigla. Atteso: col solo articolo e i numeri in coda, **13%** dei nomi fuori nella vista delle sigle (inglese 3%) e **91%** in quella delle abilità (inglese **84%**). ⚠️ **Referto da leggere**: la seconda vista è rotta per costruzione e per tutti, e il rimedio è il tasto `z` | quando si tocca un nome di oggetto, o la finestra dell'equipaggiamento |
| ⭐ `if-zero.py` | ⚠️ **la QUARTA famiglia di riga morta, e la prima che non e' un commento**: le `lang()` dentro un `if ( 0 )`, cioe' un ramo che il compilatore compila e che non e' mai vero. Nato nella 58ª su `main.hsp:8490`, una stampa di **debug** dei due numeri del calcolo dell'esperienza di viaggio, spenta lasciandola dov'era. ⭐ Che non fosse testo lo diceva anche l'inglese, **copiato pari pari dalla riga viva tre righe sotto**: chi l'ha spenta non le ha dato un inglese suo. Il conto e' sul **blocco**, non sulla riga: si segue l'annidamento delle graffe come farebbe il compilatore. Atteso: **11 righe** dentro `if ( 0 )` in tutto il sorgente, di cui **2 con una `lang()`** — quella rinviata e `map_user.hsp:2182`, in un file che non ha ancora un dizionario. ⭐ Il punto cieco c'era davvero e **non e' grande**: misurarlo e' servito a saperlo invece di sospettarlo | all'apertura di un file, insieme a `commenti-blocco.py` e `lang-nel-ramo-jp.py` |
| `commenti-blocco.py` | ⚠️ **le righe dentro un commento di blocco `/* ... */`**, cioè il codice di monte che il mod ha spento. Nato nella 37ª su `proc.hsp:11796`, dove la rete 6 — che guardava solo il `;` — avrebbe fatto tradurre testo morto. `proc.hsp` ne ha **99**, `action.hsp` 132, `custom_tweaks.hsp` 100. ⚠️ Legge il **`SORGENTE`** pinnato, non la build | dalla rete 6 di ogni lotto, e all'apertura di un file |
| `misura-blocchi-spenti.py` | quante voci **già tradotte** stanno dentro un blocco spento: lavoro speso su testo che il giocatore non legge. ⚠️⚠️ **Rifatto nella 45ª, e per otto sessioni il conto era gonfio**: guardava la riga e non la **firma**, e `estrai --da-tradurre` ancora una voce alla prima occorrenza, che può essere spenta mentre le altre sono vive. Atteso adesso: **4 sprecate** (`action.hsp:931`, `:9321`, `:17554`, `:17555`) e **5 vive altrove**, dove il conto vecchio diceva 7 sprecate. ⭐ Fra le riabilitate c'è `proc.hsp:1000`, che la ripresa citava da sessioni come esempio di lavoro perso: la sua firma vive a `:1039` e `:1298`. ⚠️ Misurato sulla **build** ne accusava di più, e le due di `text.hsp` erano giuste: quella build ha **una riga in più** del sorgente perché una toppa ce l'ha aggiunta, e i numeri di riga del dizionario vengono dal sorgente | quando si tocca `commenti-blocco.py` |
| `lotto-fase2-buffdesc-001.py`, `lotto-fase4-proc-001.py` … `-003.py` | i lotti della 33ª, tenuti come **modelli** storici: dizionario `{(riga, en): resa}` più le prime cinque reti | superati dai modelli qui sotto |
| ⭐⭐⭐ `modello-rete4.py` | **il modello da copiare** (57ª): è `modello-rete6.py` con la **rete 4 corretta**, che raggruppava per `(giapponese, funzioni)` e non guardava l'**inglese**. `main.hsp:4151` e `:4232` hanno lo stesso giapponese e lo stesso `cnvtalk`, ma l'inglese ci mette il nome del boss — sono i due finali di Tyris del Sud, e le rese devono differire. La chiave le mancava per una ragione storica: la 37ª le aveva insegnato che la rete 11 pretende le **funzioni** dell'inglese, e nessuno aveva pensato alle **parole**. ⭐ Misurata prima di usarla con `misura-rete4.py`: su 12.014 gruppi ne libera **459** e non ne perde **nessuno** degli 8 per cui la rete è nata. È la **quinta rete che si corregge**, dopo la 8, la 4, la 9 e la 6 | per ogni lotto nuovo — ma **non a mano**, vedi `assembla-lotto.py` |
| ⭐⭐ `misura-rete4.py` | **la rete 4 passata all'indietro su tutto il dizionario** (57ª), come `rete8_dizionario.py` fa con la rete 8. Nato per **misurare una correzione prima di applicarla**, ed è diventato un referto: i gruppi resi in più di un modo **con lo stesso inglese** non hanno nessuna scusa di monte. Atteso: **8** con lo stesso inglese, 459 con inglese diverso. ⚠️ Al primo giro ne ha trovato uno vero — «Tiro oltre il limite» (`buff.hsp:263`) contro «Lancio oltre il limite» (`skill.hsp:1240`), che sono la **stessa mossa**. **Se salgono, un lotto ha reso due volte in modo diverso una cosa che upstream scrive uguale** | quando si tocca la rete 4, e all'apertura di una sessione lunga |
| ⭐⭐ `misura-larghezze-promptadd.py` | **quanto valeva il punto cieco della rete 5** (60ª), misurato **prima** di allargarla: `larghezze.py` guardava i soli menu costruiti dai `#deffunc` di `text.hsp`, cioè 20 riquadri su 92. Gli altri sono corse di `promptAdd lang(...)` chiuse dallo stesso `gosub *prompt_key` — stesso riquadro, stesso carattere da 13, stesso taglio. ⚠️ **Il primo modello scritto quel giorno dava due falsi positivi**, perché cercava `promptx, prompty, N`: la larghezza è il **terzo campo** di `val` comunque siano scritti i primi due (`system.hsp:4275` fa `gfini val(2) - 17`), e la lingua allarga il riquadro **in tutt'e due i versi** (`180 + ( en * 50 )` è 230 in inglese, non 180). Atteso: **92 siti, 261 voci, 151 con `lang()`, 83 già rese**. ⚠️ La colonna che conta di più non sono gli sfori: sono i **file con voci di menu e nessun dizionario** — `map_user.hsp` 34, `chara.hsp` 9, `blend.hsp` 3 — che nessun conteggio guarda. La rete vera è ora in `strumenti/larghezze.py`: questo resta il referto che ne mostra la **composizione per file** | quando si apre un file che ha dei menu, **prima** di scrivere le rese |
| ⭐⭐ `misura-re-select.py` | **la rete 15 passata all'indietro su tutto il sorgente** (58ª), e il referto che ha misurato la sua correzione **prima** di applicarla. Un `chatList` riempie la lista, ma a disegnarla e' il `gosub` che viene dopo, e i posti sono piu' d'uno: **1240** righe nella pergamena di `chat.hsp` (tetto 52), **177 in `*re_select`** (`event.hsp:4119`), 148 in `talk_quest`, 46 in `com_txtadv_loop`. Il tetto di `*re_select` non e' nemmeno una costante: dipende dal **BMP di sfondo**, `(tx + 36 - 12 - 64) / 7,7`, da **36** (`bg_re15`) a **50** (`bg_re20`). ✅ Delle 32 voci gia' tradotte la' dentro non ne sforava nessuna: la correzione **toglie un permesso**, non ripara un danno. ⚠️ Il contenitore si cerca **senza limite di righe**, fermandosi su un'etichetta o un `return`: con una finestra di sessanta ne restavano 208 senza risposta, perche' il negozio delle carte ne impagina **253** prima del suo `gosub` | quando si tocca la rete 15, o si traduce un menu fuori da `chat.hsp` |
| ⭐⭐⭐ `buff_en.py` | **l'UNDICESIMO punto cieco: il CORPO della finestra, composto fuori da `lang()`** (59ª). `*re_select` disegna tre cose — il titolo `s`, il corpo `buff`, la lista di `chatList` — e il progetto ha una rete per la terza (la 15) e il dizionario per le `lang()` delle altre due. Ma `buff` si può scrivere **senza** `lang()`, con un letterale inglese nudo, e allora cade **fra le due reti**: `nudi_en.py` guarda i letterali che *disegnano* e qui il letterale sta in un'assegnazione; `variabili_en.py` guarda le variabili *interpolate in una `lang()`* e `buff` non ci finisce mai, viene stampato tal quale; `verifica --dizionario` indicizza per firma `lang()`, e la `lang()` non c'è. ⚠️ È testo che il giocatore legge **in grande in mezzo allo schermo**. ⚠️⚠️ **E la prima versione ne vedeva un terzo**: guardava solo `buff = "…"` e non `buff += "…"`, la forma con cui un corpo si compone **a pezzi** — **lo stesso identico difetto che la 47ª aveva corretto in `variabili_en.py`**, nello stesso progetto e per la stessa ragione. Da 44 a **124**, e in due passi: prima il `+=`, poi lo **escape** dello HSP — `command.hsp:8073` contiene una virgoletta protetta e una regex che si ferma alla prima virgoletta la faceva sparire dal conto senza dire niente (lo dice il docstring di `estrai.py` da sempre). Il pezzo grosso è `command.hsp:8049`-`:8175`, la **scheda dell'avventuriero conosciuto** (`knowCNPC`): 79 righe, una finestra da capo a fondo in inglese, che nessun conteggio nominava. Atteso: **124 siti, 44 già resi, 80 da fare** — `tcg.hsp` è chiuso (43 su 43: 18 esiti del gioco di carte, che si leggono alla fine di **ogni partita**, e 23 rifiuti degli dèi, più 2 già fatti prima), e restano le **80 della scheda dell'avventuriero**. 💡 **Tre correzioni in un giorno allo stesso referto, e nessuna era un'idea nuova**: il `+=` lo aveva già imparato `variabili_en.py` nella 47ª, lo escape lo dice `estrai.py`, la distinzione dal ramo di lingua è `else_jp.py`. Un referto nuovo sbaglia dove il progetto ha già sbagliato. 💡 Le due forme restano distinte nel referto: il `+=` dentro un ramo `if ( jp ) … else …` è già materia di `else_jp.py`, e contarlo qui sarebbe contarlo due volte. 💡 `tcg.hsp:2803` era **già reso** e i diciotto fratelli intorno no — la forma di `item_func.hsp` nella 34ª, un caso toppato per volta senza sapere che era una famiglia. ⚠️ Non è una guardia, è un metro | quando si tocca `tcg.hsp` o `command.hsp`, o si collauda una finestra di `*re_select` |
| ⭐ `correzione-lancio.py` | la correzione che ne è uscita, ed è **`correzione-il-tiro.py` della 49ª con un passo in più**: lì la regola era «si guarda quale delle due voci è LIBERA», qui non lo era nessuna delle due — «Lancio oltre il limite» sfora il tetto di 20 di `buffname`, «Tiro» è la parola di un'altra cosa (`text.hsp:136`, lo slot `Shoot`) — e a fare da arbitro è stata la **terza voce del gruppo**, il messaggio `buff.hsp:264` che dice già «mette l'**anima** nel **lancio**». ⭐ Porta una rete 0 che misura la resa nuova contro il tetto **prima** di scriverla | quando due nomi della stessa cosa non coincidono |
| ⭐⭐ `modello-rete6.py` | il modello **fino alla 56ª** (45ª): è `modello-rete9.py` con la **rete 6 corretta**, che guardava la riga d'ancoraggio invece della firma. `estrai --da-tradurre` ancora una voce alla prima occorrenza: se quella sta in un blocco spento e le altre no, la vecchia rete bocciava una riga viva. È capitato sul menu d'uscita — `command.hsp:17285` sta nell'`ORIGINAL` spento e rivive a `:17316` — cioè su un menu che si apre a ogni uscita dal gioco. ⭐ **Misurato prima di toccarla**: 36 firme toccano un blocco spento, **28 spente del tutto** (rete giusta) e **8 miste**, sette con l'ancora morta. Adesso boccia solo se sono spente **tutte** le occorrenze, e quando l'ancora è spenta ma il testo vive lo dice con un 💡. ⚠️ È la **quarta rete che si corregge**, dopo la 8, la 4 e la 9 | per ogni lotto nuovo — ma **non a mano**, vedi `assembla-lotto.py` |
| `modello-rete9.py` | il modello **fino alla 44ª** (43ª): ha tutte e quattordici le reti con la **rete 9 corretta** — faceva `.rstrip()` sull'inglese e cancellava la differenza fra una testa di frase (« and» in coda) e una congiunzione infissa (« and »), bocciando una resa giusta. ⚠️ **Un modello non può essere un lotto che rinvia qualcosa**: `assembla-lotto.py` vuole l'ancora `RINVIATE = set()`, e per questo il file vive separato invece di essere l'ultimo lotto. Stessa forma di `modello-chiave-lunga.py` della 41ª | per ogni lotto nuovo — ma **non a mano**, vedi `assembla-lotto.py` |
| `lotto-fase4-proc-026.py` | il modello **fino alla 42ª**, ultimo lotto di `proc.hsp` (39ª). Tenuto come storia: i lotti dal `proc-005` in poi si leggono da lì | mai più come modello: vedi la riga sopra |
| ⭐⭐ `assembla-lotto.py` | **copia le reti VERBATIM dal modello** e cambia solo le cinque costanti che devono cambiare — `USCITA`, `DA, A`, `RINVIATE`, `SORGENTE` e il percorso dell'estrazione — poi **rilegge quel che ha scritto** e lo confronta col modello carattere per carattere. Rende meccanica la regola «si copia il file, non si riscrive a memoria», che la ripresa ripeteva da cinque sessioni senza poterla imporre. Vuole due file scritti a mano (`testaNNN.py` col docstring, `reseNNN.py` col dizionario) più un `rinviateNNN.py` facoltativo. ⚠️ Il **sesto argomento è il file `.hsp`**, e senza si intende `proc.hsp` | per **ogni** lotto |
| ⭐ `dossier.py` | le tre letture che ogni lotto rifaceva a mano: il sorgente intorno alla riga, le rese gemelle per **giapponese** e quelle per **inglese**. È la regola «cercare prima di scrivere» resa meccanica — nella 39ª ha pescato **dodici copie su trentaquattro** in un lotto solo, e ha trovato il caso `:20200` (stesso inglese di `action.hsp:11649`, giapponese diverso). ⚠️ Legge il **`SORGENTE`**, non la build | **prima** di scrivere le rese, su ogni zona |
| `perimetro.py` | il conto vero di quanto manca, descrizioni degli oggetti e file di `data/` compresi. ⚠️ **Non si deduce sommando `verifica --dizionario`**, che misura solo il perimetro `lang()`. Atteso a fine 39ª: perimetro **49%**, totale vero **36%** | all'apertura, e quando serve rispondere «a che punto siamo» |
| ⭐⭐⭐ `_97-listn.py` | ⚠️ **IL PUNTO CIECO DELLA 74a, ED E' DI MISURA E NON DI TRADUZIONE**: le 128 righe `listn(...) = lang(...)` in cinque file sono menu scritti a mano, e nessuna guardia le misurava — `larghezze.py` guarda i menu **dichiarati** (`s(cnt) = lang(...)`, `promptAdd`), `riquadri.py` le piastrelle, `menu_dialogo.py` il dialogo. La rete trova, per ogni riga, la routine che la contiene, il `display_window` che porta la larghezza e il `pos wx + N, ... cnt ...` dove le voci si posano, e ne ricava il tetto col metro di `larghezze.py` (7,7 px). ⚠️⚠️ **L'ancora dev'essere dentro il ciclo**: al primo giro bastava un `pos wx + N` qualunque, e su `*com_charainfo` prendeva quello dello **sfondo** (`wx + 4`) dando un tetto inventato di 86 — verde su una misura falsa. ⚠️ E dove le ascisse sono piu' d'una il pannello e' **a colonne** e il metro non si indovina: quelle righe si contano «senza metro», e il metro giusto entra a mano in `METRO_A_MANO`, una riga per pannello **col sito da cui e' stata letta**. Atteso: **128 righe, 120 rese, 113 misurate, 0 fuori misura, 0 introdotte dall'italiano** | quando si tocca un pannello a lista, e all'apertura di `chara.hsp`, `net.hsp`, `event.hsp` |
| `_97-conoscenza-larghezza.py` | il tetto del pannello «Conoscenza dell'oggetto» (`command.hsp:16054`-`:16867`): 600 px, testo a `wx + 68`, **65 caratteri**. Nato prima di `_97-listn.py`, che ora lo comprende — resta perche' tiene le **code** che il sorgente appende fuori dalla `lang()` (`[Lv:… Esp:…%]` di `:16349`, `(1d5 perfora 30%)` di `:16365`), che il fratello generale non conosce. Atteso: **0 introdotte dall'italiano** | quando si tocca quel pannello |
| `_97-vive.py` | per ogni voce «da fare» di un file, **tutte** le occorrenze della firma e se sono vive o morte (commento di blocco, ramo `if ( jp )`, `;`). ⚠️ Nasce da `command.hsp:16289`, che `estrai --da-tradurre` registra dentro un `/* ORIGINAL */` spento: rinviarla per quello sarebbe stato un errore, perche' **la stessa firma vive a `:16303`**. Il referto distingue MORTA (tutte le occorrenze spente) da MISTA (qualcuna viva) | all'apertura di un file, prima di rinviare una voce per la riga in cui e' registrata |
| `_97-dead-jp-command.py` | quale delle 11 righe morte di `command.hsp:2954` sia stata **tradotta**, con la resa accanto. Serviva a rispondere a `lang-nel-ramo-jp.py` quando quello dice «gia' tradotte: 1» e non dice quale | quando il referto del ramo `jp` sale sopra zero |
| ⭐⭐⭐ `nudi_accanto_a_lang.py` | ⚠⚠ **il DODICESIMO punto cieco (61ª): i letterali inglesi nudi sulla STESSA RIGA di una `lang()`.** `nudi_en.py` scarta la riga intera appena ci legge un `lang(` — `if 'lang(' in s: continue` — quindi una riga mista non la guarda nessuno: il dizionario prende le `lang()` e il nudo accanto resta inglese. Trovato aprendo `config.hsp:618`, l'elenco delle voci di «Messaggi e registro», dove quattro voci passano dal dizionario e **due no** (`"  Display log instead*"`, `"Capitalize item names"`): sono aggiunte del mod che upstream non ha mai avvolto in `lang()`. ⚠ Il filtro su che cosa è testo si **importa** da `nudi_en.py` invece di riscriverlo, così i due referti non divergono. 💡 L'unica regola in più è che `"null"` non è testo: è la lettera di scelta di `promptAdd`, e senza scartarla sono 96 righe su 130. ⚠⚠ **Il «da fare» si misura sui NUDI, non sulla riga**, e la prima versione sbagliava proprio lì: su una riga mista la riga cambia sempre fra sorgente e build perché il dizionario ci ha riscritto le `lang()`, quindi `config.hsp:805` risultava fatta appena il file ha avuto un dizionario e `MCI` non l'aveva toccato nessuno — contava 7 da fare dove ce n'erano 15. È la lezione della 60ª (una misura presa su un insieme più largo di quello che si vuole misurare) ripetuta dentro il referto che la citava. Atteso: **19 di struttura, 0 da fare, 6 decise** — chiuso lo stesso giorno in cui è nato, con nove toppe che hanno tutte chiesto la forma `prima` di `applica.py`. Le sei decise sono `" cm"`/`" kg"` (unità SI), `",Tab "` due volte (nome di un tasto), `MCI`/`GuruGuruSMF4` (driver) e `"dead"` (prefisso di `net_send`) | all'apertura di ogni file, insieme a `nudi_en.py` |
| ⭐⭐ `nudi_en.py` | ⚠️⚠️ **il QUINTO punto cieco (49ª): i letterali inglesi che non passano da NESSUNA `lang()`.** Non è un ramo di lingua come `blocchi_en.py` e `else_jp.py` — qui il ramo non c'è, la riga è la stessa per giapponese e inglese ed è inglese per tutti — e non è `cnv_str_en.py`, dove il letterale è *input*: qui è **uscita**, e si legge a schermo. Trovato dal piede dell'inventario: `command.hsp:14175` (`" items"`), `:14366` (`" gp"`), `module.hsp:4141` (`"Page."`). Nessun lotto li raggiunge: **si toccano solo con una toppa**. ⭐ **È lo strumento che la decisione del 2026-08-10 chiedeva come primo passo e nessuno aveva scritto**, e porta anche l'«elenco di ciò che è dato» chiesto lì — messo nella **forma** invece che a mano: `listn(0, …)` è la colonna che si legge, `listn(1, …)` è la chiave (`db_race.hsp:315` = `"kobolt"`). Atteso: **913** di struttura, **872** da fare. ⚠️ Il numero è grezzo e vuole un triage per file: `custom_tweaks.hsp` 183 è il menu opzioni del mod, `tcg.hsp` 50 il gioco di carte | quando a schermo compare inglese che nessun conteggio dichiara |
| ⭐⭐ `return_en.py` | ⚠️⚠️ **il punto cieco di `nudi_en.py`, chiuso nella 51ª**: i `return "…"` dentro un `#defcfunc`, che non disegnano e non compongono, e che il testo lo restituiscono lo stesso — è così che il suffisso di stato del pannello dei ritocchi (« (Currently: Off)») è rimasto invisibile fino alla 50ª. ⭐ **La 50ª aveva chiesto «una regola di forma che distingua» il testo dalle chiavi: non esiste**, e provarla è stato il lavoro. `text.hsp` `return "vernis"` (chiave di mappa) e `init.hsp` `return "st"` (suffisso ordinale) sono tutt'e due un token minuscolo senza spazi: nessuna regola sul **letterale** li separa. ✅ La regola vera guarda **dove va a finire il valore** — se anche una sola chiamata sta su una riga che disegna o compone, quel che la funzione restituisce arriva a schermo. È la stessa lezione di «Bandits Killed» e del prefisso `dbg_`: **si guarda il sito, non la parola**. Cinque classi: `testo`, `decisa` (si lascia, col motivo scritto), `toccata` (il blocco è già stato lavorato — guardare, non contare), `morfologia` (l'elenco che `strumenti/funzioni.py` già tiene), `chiave`. Atteso: **121 totali → 0 da fare, 2 decise, 35 toccate (4 residui), 49 morfologia, 35 chiavi** | quando si sospetta che una funzione restituisca testo |
| `variabili_en.py` | ⚠️ **il terzo punto cieco**, dopo `blocchi_en.py` e `else_jp.py`: le variabili che si portano dentro un letterale inglese e finiscono interpolate in una `lang()`, dove nessuno dei due referti le vede perché l'assegnamento è **incondizionato**. Atteso: **66 variabili, 3 trappole** — se sale a 4 qualcuno ne ha creata una, se scende a 2 `economy.hsp:319` è stato risolto | all'apertura |
| `rinvia-proc-4958.py`, `rinvia-proc-navi.py`, `rinvia-proc-11796.py` | come si scrive un rinvio in `rinviate.jsonl` col motivo per esteso | quando una rete 6 o 7 scatta |
| ⭐ `toppa-action-15221.py`, `toppa-proc-24107.py`, `toppa-chara_func-3037.py` | **rinvio + toppa insieme**, per la riga che il dizionario non può aggiustare: la toppa riporta il ramo inglese alla forma del giapponese e il rinvio dice perché. ⚠️ Le toppe **non passano da `degrada()`**: la sostituzione non deve portare accenti, e va scritta per non averne bisogno. 💡 **E si compone, si codifica in memoria e solo allora si apre il file**: vedi il riquadro qui sotto | quando la rete 11 boccia la resa giusta |
| ⭐ `toppa-command-4335.py`, `toppa-command-4653.py` | le altre due toppe della 46ª, tutte e due **rinvio + toppa** e tutte e due nate da una rete che aveva ragione in generale e torto lì. `4335`: due `lang()` col **giapponese identico** e due inglesi che differiscono per uno **spazio** (`"skill "` e `"skill"`), che serve perché `:4887` fa il punteggio sui prefissi di `inputlog`; la rete 4 pretende una resa sola. `4653`: la stessa `lang()` è **etichetta di menu e valore di `CDATAN_NEWSEX`**, e il dizionario deve seguire il mestiere più severo — a schermo ci arriva per toppa, come `text.hsp` fa già sei volte | quando una rete blocca la resa giusta, o quando una `lang()` ha due mestieri |
| ⭐⭐ `toppa-command-15489.py` | **la famiglia nuova della 46ª: un letterale inglese concatenato in coda a una `lang()`**, `txt lang(...) + "(" + punti + " Guild Point)"`. Non è un ramo, non è una variabile, non è una `cnv_str`: nessuno dei **cinque punti ciechi** lo guarda, e il dizionario non lo raggiunge perché sostituisce solo il secondo argomento di `lang()`. ⚠️⚠️ **E qui è nata la regola che mancava — vedi il riquadro «una toppa e una resa» qui sotto.** ⭐ Da copiare anche per come sceglie il testo: il termine («Punti gilda») era già deciso quaranta righe più su, a `:14115`, dentro una `lang()` vera | quando un letterale inglese sta **fuori** dalla `lang()` sulla riga di una voce |
| ⭐⭐ `toppa-chara_func-orso.py` | **la toppa che non ricopia: la ricava.** (49ª) Le due `cnv_str` della battuta dell'orso erano morte **due volte** — la prima quando i nomi di creatura sono stati tradotti, la seconda quando è stato tradotto il necrologio (`chara_func.hsp:6850`, da `"was killed by "` a `"perse la vita contro "`) — e il motivo della toppa vecchia **aveva scritto per iscritto quando sarebbe scaduta**, senza che nessuno tornasse a leggerlo. ✅ La forma giusta: la chiave si **ricava** dalle voci di dizionario da cui dipende (prefisso da `:6850`, nomi da `db_creature.hsp:37656` e `:37748`) con dieci reti che fermano lo script se una cambia. 💡 **Una toppa che tiene una copia congelata di una resa che sta altrove è già scaduta, aspetta solo di scoprirlo.** ⚠️ E l'ordine delle due righe è **incrociato** apposta: la chiave corta è prefisso della lunga e `cnv_str` aggancia il primo riscontro | quando una toppa dipende da una resa che vive in un altro file |
| ⭐ `correzione-unisce.py`, `correzione-il-tiro.py` | le due correzioni del **collaudo** della 49ª, tutt'e due su un registro sbagliato e non su un errore. `unisce`: `skill.hsp:1561` era l'unica descrizione alla terza **plurale** su venticinque — l'inglese non ha persona e non poteva far da guida, la colonna aveva già scelto. `il tiro`: le due voci di `txtsetequipw` non si accordavano («la mano» / «tiro»), e **l'ovvio era chiuso** perché «la mano» condivide la firma con `_melee(0, 0)`, dove l'articolo serve. 💡 **Quando due voci di un menu non si accordano, si guarda quale delle due è LIBERA prima di decidere in che direzione accordarle** | quando una resa è giusta ma stona con le sue vicine |
| `correzione-bolt.py`, `correzione-014.py`, `correzione-rete8.py`, `correzione-mana.py`, `correzione-schivata.py` | come si corregge una resa **già entrata nel dizionario** senza passare da un lotto, con le reti che impediscono di correggerne una di troppo o una di meno. ⚠️ **`correzione-rete8.py` porta la rete che mancava**: le rese nuove vanno passate a `controlla_lotto`, perché `verifica --dizionario` **non le guarda** — confronta il dizionario col sorgente e conta orfane e non tradotte. 💡 **`correzione-schivata.py` è il modello più recente** ed è nato da un **collaudo**, non da una misura: «Il viandante schiva Kefry» compariva cinque volte in uno schermo | quando due file dicono la stessa cosa in due modi, o quando lo schermo mostra una frase storta |
| `rete8_dizionario.py` | la **rete 8 all'indietro**, su tutto quello che è già entrato: le rese che stampano «di il», «a il», «in il», «su il». Nella 37ª ne ha trovate sei, di cinque lotti diversi, tutte scritte prima che la rete esistesse. Atteso adesso: **3**, tutti dichiarati falsi positivi | quando si tocca la rete 8, o all'apertura di una sessione lunga |
| `ricerca-014.py`, `ricerca-015.py`, `ricerca-016.py` | il modello di come si interroga il dizionario **prima** di scrivere un lotto: una lista di domande `(titolo, filtro)` su `jp`/`en`/`it` di tutti i file insieme. Nella 37ª ha pescato «bacchetta», «mana di ricarica», «medaglietta», «barra», «Tornado magnetico», «la sorella cane maggiore» | insieme a `dossier.py`, prima di tradurre |

### Le quattordici reti dello script di lotto

Ognuna nasce da un caso vero, non da un'idea. Le prime cinque sono della 33ª e
della 31ª, le altre della 35ª, della 36ª e della 37ª.

| # | che cosa impedisce | il caso che l'ha fatta nascere |
|---|---|---|
| 0 | che la chiave `(riga, en)` identifichi più di una voce | il riciclo inglese, 84 stringhe su 231 giapponesi |
| 1 | che una voce della zona resti senza resa | — |
| 2 | che una resa non agganci nessuna voce | due lotti scritti sulla voce sbagliata (27ª) |
| 3 | che si renda in un modo nuovo un giapponese **già reso altrove** | ⭐ nella 35ª ha parlato **quattro volte**, e aveva sempre ragione: `:6481` (7 siti), `:6492` (5 siti), `:6951`, `:4310` |
| 4 | che lo stesso giapponese abbia due rese **dentro lo stesso lotto** | i due Yerleswood, lotto `039` |
| 5 | che l'accento sia **decomposto** (`a` + U+0300) invece che precomposto | cinque rese su 43 nel lotto `-005`: a occhio identiche, e CP932 non ha il combinante |
| 6 | che si traduca una voce su una **riga spenta** — commentata col `;` **o dentro un blocco `/* ... */`** | `proc.hsp:4958`, il blocco `MANUSCRIPT HINT`; e nella 37ª `:11796`, dentro l'`/* ORIGINAL */` che il mod ha spento per togliere il tetto ai punti bonus |
| 7 | che si traduca un **operando di confronto** | `:5584`, i due nomi di nave che `map.hsp` assegna e `proc.hsp` confronta |
| 8 | una **preposizione che si fonde** (`di`/`da`/`in`/`su`/`a`) davanti a `name`/`itemname`/`valn`/`cdatan` | `valn` è un `itemname()` sotto falso nome, e l'inglese ci mette «from» e «in» |
| 9 | che una **testa di frase** (l'inglese finisce in « and») non si chiuda col connettivo | le dieci teste del log di combattimento, che si saldano alla coda di danno di `chara_func.hsp` |
| 10 | che `his(x, 1)` regga un nome che non sia **maschile singolare** | `:8849`, «il suo sangue»: la funzione sceglie sul possessore, l'italiano accorda col posseduto |
| 11 | che le **funzioni di contenuto** della resa non coincidano con quelle dell'inglese | `:10312` e `:11481`, dove nominare il soggetto come fa il giapponese aggiungeva una funzione che l'inglese non ha. ⚠️ **È anche l'unica rete che a volte non lascia scampo**, e allora la strada è rinvio + toppa: `proc.hsp:11481` (36ª), `proc.hsp:24107` (39ª, l'inglese nomina **due** personaggi dove il giapponese ne nomina uno perché `tc == cc`), `chara_func.hsp:3037` (39ª, `gdata` conta come contenuto). Quando la rete 11 boccia, la prima domanda è **se la resa giusta è scrivibile**; se non lo è, non si piega la resa |
| 12 | che la resa di una **dinamica** sia testo nudo invece di un'espressione HSP | ⚠️ `:11534` nella 37ª: l'inglese porta `his(tc)`, in italiano la morfologia sparisce e resta una frase sola. Senza virgolette `applica.py` l'ha scritta come **codice**, e il compilatore ha letto «qualche» come nome di variabile |
| 13 | che passi inosservato un **inglese solo per due giapponesi diversi** — è un referto, non un errore | `:14521` e `:14573` nella 37ª: «The air around you gradually loses power» sta per 「脱出を中止した」 e per 「帰還を中止した」, cioè per due incantesimi diversi con due pergamene diverse |

⚠️ **La rete 4 raggruppa per `(giapponese, funzioni di contenuto)`, non per il
solo giapponese**, e il motivo è che nella 37ª ha litigato con la rete 11:
`:12837` e `:13298` hanno lo stesso giapponese e un inglese che nomina un numero
diverso di personaggi. La rete 11 pretende le funzioni dell'inglese, la rete 4
pretendeva le stesse parole — e con un nome in meno non si può. La differenza la
impone il sorgente, non la traduzione.

⚠️ **La rete 8 nella 37ª ha bocciato due rese giuste**, e la colpa era sua:
`valn` non è sempre un `itemname()`. A `proc.hsp:11893` il sorgente scrive
`valn = skillname(i)` due righe sopra, e i nomi di abilità non portano articolo
(«Forza»), quindi «di » ci sta. Adesso la rete **legge l'assegnamento più
vicino** e si arrabbia solo se `valn` viene da un `itemname()`.

⚠️ **E la rete 3 gridava su rese identiche**, perché confrontava le
**espressioni**: `proc.hsp:12287` e `action.hsp:18755` dicono le stesse parole su
variabili diverse (`name(cc)` di qua, `name(cnt)` di là). Adesso confronta i
**letterali**, come la rete 4 dal lotto 011, e quando le parole coincidono lo
dice con un 💡 invece che con un ⚠️.

⚠️ **La rete 9 ha bocciato tre rese giuste alla prima scrittura**, perché cercava
`+ " e"` come pezzo a sé e non vedeva il connettivo in coda a un letterale più
lungo (`" strappandone la carne e"`). Si guarda il **testo prodotto**, non la
forma dell'espressione. Quando una rete accusa una resa che sembra giusta, la
prima domanda è se sbaglia la rete.

💡 **E `verifica` sa cose che le reti non sanno.** Nella 35ª ha fermato due volte
quello che le nove reti avevano lasciato passare: `proc.hsp:6016`, dove avevo
**aggiunto** un `itemname` che l'inglese non ha («attese `['name']`, trovate
`['itemname', 'name']`»), e `:8849`, dove avevo **tolto** un `his(tc, 1)` che con
due argomenti è contenuto. Le interpolazioni sono il contratto con la riga, non
una scelta di stile: si lancia sempre anche `verifica`, non solo lo script.

Si lanciano dalla radice del repo, con l'interprete giusto:

```powershell
$repo = "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
$py = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
Set-Location $repo
$env:PYTHONPATH = $repo      # ⚠️ serve a chi importa `strumenti`
& $py scratchpad/simili.py
& $py scratchpad/guardie.py lavoro/<lotto>.jsonl
```

⚠️ **`PYTHONPATH` non è un dettaglio.** Lanciando `python scratchpad/x.py` il
primo elemento di `sys.path` è `scratchpad/`, non la radice, quindi
`from strumenti.accenti import degrada` muore con `ModuleNotFoundError`. Gli
script che ne hanno bisogno sono `genera-toppe-en.py`, `correggi-teste.py`,
`toppa-action-15221.py`. 💡 Nella 33ª è successo, e il sintomo era ingannevole:
il generatore falliva, ma lo script che ne stampava il risultato leggeva il file
**vecchio** e mostrava tutto a posto.

💡 `simili.py` e `gia_rese.py` **prendono l'estrazione dal primo argomento**
(`python scratchpad/simili.py lavoro/_command.jsonl`), col vecchio
`lavoro/_buff.jsonl` come default. ⚠️ Fino alla 43ª era cablata dentro, e questa
riga diceva che parametrizzarli costava più che cambiarli: alla quinta volta che
si riscriveva la stessa riga non era più vero. `simili.py` ricava anche il nome
dell'uscita dall'estrazione — `lavoro/_command_simili.txt`.

💡 **La convenzione dei nomi, dalla 39ª**: il file `nome.hsp` vuole l'estrazione
in `lavoro/_nome.jsonl` e produce i lotti `lavoro/fase4-nome-NNN.jsonl`.
`assembla-lotto.py` la dà per buona, quindi rispettarla costa niente e romperla
costa un'ora.

### ⚠️⚠️ Una toppa e una resa non possono stare sulla stessa riga

Nata nella 46ª su `command.hsp:15489`, e la trappola è che **la strada sbagliata
funziona**. `applica.py` fa girare le toppe **dopo** il dizionario
(`applica.py:530`), quindi si può agganciare `cerca` alla riga **già tradotta**,
leggendola dall'albero di build: la toppa si applica, l'italiano esce giusto, il
gioco compila.

A fermarla è `strumenti/tests/test_toppe.py:104`, che pretende che **ogni toppa
si applichi al SORGENTE pinnato**. Non è un capriccio: è quella prova a diventare
rossa il giorno in cui upstream riscrive la riga, prima che la build produca
qualcosa di sbagliato. Una toppa agganciata al testo italiano non ha più nessun
rapporto col sorgente, e quella prova non varrebbe più niente — resterebbe verde
per sempre, su una riga che nessuno controlla più.

✅ La forma giusta è quella già in tabella qui sopra: **rinvio + toppa insieme**.
Il rinvio toglie la voce dal dizionario, così `applica` non tocca la riga, e la
toppa la riscrive tutta intera partendo dal sorgente.

💡 In una riga sola: **o la riga la sistema il dizionario, o la sistema la
toppa.** Chi sceglie la toppa deve rinviare la voce, e chi trova una riga con
tutt'e due ha già un difetto sotto gli occhi.

### ⚠️⚠️ Una stringa che si DIGITA non segue la regola degli accenti

Nata nella 46ª sul sistema dei desideri di `command.hsp`. Certe `lang()` non sono
testo da leggere: sono parole che il giocatore **batte sulla tastiera**, e il
codice le cerca dentro quel che ha scritto (`del_str`, `instr`). Lì l'accento non
è una questione di ortografia, è una questione di **coincidenza esatta**, e la
regola si decide da dove arriva la parola.

- **Viene dalla testa di chi gioca** → l'accento **non si scrive**. `*wish_fix`
  toglie il prefisso «skill»/«item», e la resa è «abilita» senza accento: in
  CP932 la `à` non esiste, nessuno può digitarla, e un `del_str` su «abilita'»
  non aggancerebbe mai niente.
- **Viene dallo schermo** → l'accento **si scrive normale**. Le parole chiave di
  `:4832`-`:4855` sono nomi di oggetti, e la resa è quella di `db_item.hsp`
  accento compreso: in build «biglietto d'abilità» diventa «biglietto
  d'abilita'», che è **esattamente** quel che il giocatore legge sull'oggetto e
  poi ricopia.

⚠️ **E le parole di famiglie diverse devono combaciare fra loro**: chi scrive
«abilita pesca» viene instradato da `:4840` (stessa firma di `:4336`) e poi
ripulito da `*wish_fix`. Cambiarne una senza l'altra rompe il desiderio **in
silenzio** — nessuna rete, nessuna guardia, nessun referto se ne accorge.

### ⭐⭐⭐ Il carattere del ramo inglese è MONOSPAZIATO: i tetti si calcolano

Nata nella 47ª sui tre menu dell'aspetto di `command.hsp`. `config.txt` dice
`font2. "Courier New"`, cioè il carattere che il ramo inglese — e quindi
l'italiano — usa a schermo. Da lì la larghezza di un campo **non è più
un'opinione**: si prendono i due `pos` che lo delimitano nel sorgente e si
divide.

```
corpo 12 (`12 + sizefix - en * 2`)  ->  7,2 px per carattere
corpo 14 (`14 - en * 2`, `15 + en - en * 2`)  ->  8,4 px
```

Le misure già fatte, da riusare invece di rifarle:

| campo | dove | tetto |
|---|---|---|
| voce di `cs_list` | testo a `wx + 64` (`module.hsp:129`), freccia a `wx + 175` | **111 px = 15,4 caratteri**, etichetta più valore |
| riga di aiuto di `display_window` (`s(1)`) | `module.hsp:4344`, `wx + 58`; la riga «Page.» accanto tiene 40 px di margine | **(larghezza − 58 − 40) / 7,2** — su 380 fa **39 caratteri** |
| `display_note` | `module.hsp:4360`, `wx + ww - strlen * 7 - 140` | **(ww − 140 − 20) / 7 caratteri** — su 690 fa **75** |
| titolo di finestra (`s`) | `module.hsp:4339`, piatto da `45 * ww / 100` che cresce oltre i 15 caratteri | largo: su 380 stanno **20 caratteri** |
| colonna delle righe d'attacco | `command.hsp:12429` (`wx + 422`) contro `:12452` (`wx + 468`) | **46 px = 6 caratteri** |

⚠️ **E l'inglese non è il budget**, per la stessa ragione che `larghezze.py`
scrive da sempre: dei cinque campi qui sopra, **tre sono già al limite o oltre**
di monte — «Unarmed» sfora la sua colonna, la riga di aiuto usa 38 caratteri su
39, `display_note` arriva esatta a 75.

⭐ **E il tetto ha un'eccezione che è una regola**: nel menu del ritratto le righe
**senza valore** non hanno tetto stretto, perché `:12136` appende il numero solo
`if ( rtval >= 0 )`. È per questo che upstream ha potuto scrivere «Set Detail»,
dieci caratteri, dove le altre ne hanno otto. **L'imbottitura serve alle righe
che portano un numero, e solo a quelle.**

### ⚠️⚠️ Un'etichetta di menu finisce SEMPRE con almeno uno spazio

Il fratello della regola qui sopra, e a insegnarla è stata `verifica.py:440`, che
rifiuta una statica il cui inglese finisce con uno spazio e la cui resa no.

La ragione è più forte di come la guardia la racconta. Nel menu del ritratto lo
spazio in mezzo lo mette il codice (`command.hsp:12138`, `s += " " + rtval(2)`),
ma nel menu dello specchio **no**: `:12333` è `s += "On"` e `:12336` è
`s += "Off"`, nudi. Lì l'imbottitura dell'etichetta è **l'unico separatore**, e
«Mantello» da sola darebbe «MantelloOff».

✅ Quindi, in questa famiglia, l'etichetta finisce con uno spazio **sempre**, e la
separazione smette di dipendere da chi concatena. Il testo utile è una colonna in
meno di quelle disponibili: è per questo che 「髪の色」 è «Col.cap.» e non
«Col.capel.», che riempirebbe tutte e dieci le colonne.

### ⭐⭐ Quando la rete 3 accusa, si guarda il MESTIERE del sito che cita

Nata nella 47ª sulle righe d'attacco di `*show_weaponStat`. La rete 3 dava tre
etichette su quattro come già rese altrove — 「武器」 «armi» (`text.hsp:59`), 「格闘」
«Arti marziali» (`skill.hsp:161`), 「射撃」 «Mira» (`skill.hsp:387`) — e tutt'e tre
le rese erano giuste **nel loro sito**: la prima è una categoria d'inventario, le
altre due sono nomi di abilità. Qui sono etichette di riga larghe sei caratteri.

✅ **La strada non è scegliere fra me e la rete: è cercare il sito dove i due
termini stanno INSIEME**, perché quello ha già dovuto distinguerli.
`buff.hsp:679` rende 「射撃力上昇/命中率上昇」 «Tiro e **mira**»: da lì 射撃 è «Tiro» e
命中 è «Mira», e `skill.hsp:1277` («+mira») conferma.

💡 In una riga: **la rete 3 non dice «sbagli», dice «guarda là»** — e quel che si
guarda è in che mestiere stava la resa che cita.

### ⚠️⚠️ Uno script che riscrive un file di dati lo compone PRIMA di aprirlo

Nella 39ª uno script scritto in fretta ha aperto `toppe.jsonl` in scrittura e ha
composto il testo dentro `write()`. Nel motivo c'era una **coppia di surrogati
scritta a mano** al posto del carattere 💡, e `UnicodeEncodeError` è esploso
**dopo** che l'apertura aveva già troncato il file: **231.878 byte di toppe, a
zero**. A salvarlo è stato `git checkout`, cioè il fatto che il lavoro fosse
già spinto.

✅ La forma giusta è quella di `riscrivi()` in `toppa-proc-24107.py`:

```python
def riscrivi(percorso, righe_nuove) -> int:
    righe = [r for r in io.open(percorso, encoding='utf-8').read().splitlines() if r.strip()]
    righe.extend(righe_nuove)
    dati = ('\n'.join(righe) + '\n').encode('utf-8')   # ⚠️ prima si valida
    with io.open(percorso, 'wb') as f:                 # e solo allora si apre
        f.write(dati)
    return len(righe)
```

💡 **E ha funzionato subito dopo**: la stessa cosa è ricapitata mezz'ora più
tardi in `toppa-chara_func-3037.py`, con lo stesso surrogato, e il file non è
stato toccato. Lo stesso vale per `correzione-schivata.py`, che compone tutti i
dizionari in memoria e li scrive solo dopo che `controlla_lotto` ha detto sì.

⚠️ **E la lezione minore**: `cerca.py` esisteva già in questa cartella, e nella
39ª ne è stato riscritto un gemello nello scratch di sessione senza guardare.
Questa tabella si legge **prima** di scrivere uno script nuovo.

---

## 107ª — gli strumenti delle descrizioni di `db_item.hsp`

Dalla 107ª le descrizioni degli oggetti sono un **tipo di sito** di
`estrai.siti()`, non un buco fuori perimetro. Questi sette script sono il fronte
che ne è nato. ⚠️ Leggono il **sorgente pinnato e il dizionario**, non la build:
girano anche su una macchina dove l'albero non è stato costruito.

| file | a cosa serve | quando si lancia |
|---|---|---|
| `_107-zona-sorgente.py` | una zona di righe di un file del sorgente, decodificata in UTF-8. ⚠️ `zona.py` legge l'estrazione e `dossier.py` il dizionario: nessuno dei due serve per un file che il dizionario non ha ancora | quando si apre un file nuovo |
| `_107-struttura-db-item.py` | la forma dei blocchi `DBMODE_DESC`: 1.321 blocchi, 4 indici per ramo, **0 asimmetrici, 0 letterali sporchi**. È la misura che ha reso meccanizzabile il file | una volta, e se il sorgente pinnato cambia |
| ⭐⭐ `_107-descrizioni-item.py` | **la rete**: il corpo (indici 0-2) contro l'impaginatore vero, e l'indice 3 contro il suo **tetto secco di 69**. Tre colonne — inglese, italiano, e l'unica che deve stare a zero: *introdotte dall'italiano*. ⚠️ 110 indici 3 sforano **già in inglese**: un cancello sulla seconda colonna boccerebbe lavoro giusto. ⚠️ L'italiano si misura **degradato**. L'impaginatore si **importa** da `_102-carta-conoscenza.py`, non si riscrive: è lo stesso ramo di codice (`command.hsp:16802`). `--prova` ha quattro capi e si accende davvero; `--previsione` dice quanto è stretto il tetto prima di tradurre | a ogni lotto, e prima del primo |
| `_107-lotti-per-categoria.py` | le descrizioni per **categoria** dell'oggetto (mobilio 512, utensili 376, cibo 331…). Dice anche quante non trovano il loro `ITEM_ID`: sono **0 su 2.832** | per scegliere il lotto |
| ⭐⭐ `_107-dossier-item.py` | la descrizione col **nome italiano già reso** del suo oggetto, e col nome **non identificato**, che è un altro sostantivo con un altro genere (`contratto-nomi.md` §1-ter). ⚠️ È `_102-dossier.py` per gli oggetti, ma qui il nome non sta venti righe sotto: sta a **novantamila** | **prima** di scrivere le rese, su ogni lotto |
| `_107-chiavi-item.py` | lo scheletro delle chiavi `(riga, en)`, con **gli stessi filtri** del dossier — un lotto e il suo dossier che selezionano in modo diverso sono un guasto che non si vede. ⚠️ Emette un `RIGHE = {...}` e non un `DA, A`: le descrizioni di una categoria sono sparse per novantamila righe | subito dopo il dossier |
| ⭐ `_107-firme-gemelle.py` | gli inglesi che tornano più volte con firme diverse: **2.580 firme sono 2.556 traduzioni**. Separa i gruppi col giapponese uguale a meno di spazi (stessa resa, e nessuna rete lo vedrebbe) da quelli col giapponese **davvero diverso**, dove l'inglese di monte ha appiattito una distinzione che l'italiano può ripristinare | all'apertura del fronte, e quando due rese sembrano la stessa frase |

⚠️ Il file di lavoro `lavoro/_107-daitem.jsonl` **non si versiona** e si rigenera:

    python -m strumenti.estrai db_item.hsp --da-tradurre --uscita lavoro/_107-daitem.jsonl

💡 **La lezione della 107ª per questa cartella**: `perimetro.py` aveva un automa
suo per contare le descrizioni e contava **5.284** invece di 2.832, perché
prendeva anche le 2.452 righe vuote. Uno script di questa cartella che rifà una
scansione che `strumenti/` già fa non è più veloce: è un secondo numero che può
divergere dal primo, e diverge in silenzio.
