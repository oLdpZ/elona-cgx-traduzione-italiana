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
| ⭐ `lang-nel-ramo-jp.py` | ⚠️ **il QUINTO punto cieco, ed è il rovescio di `else_jp.py`**: le `lang()` chiuse dentro un `if ( jp ) { … }`, che in italiano non girano mai. Nato nella 45ª su `command.hsp:2954`, il diario delle statistiche: settanta righe nel ramo giapponese con dentro sette `lang()` vere, e un `else` che stampa le stesse cifre in inglese nudo. È la **terza famiglia di riga morta** dopo il `;` e il `/* … */`, e la prima che non si vede: la riga è viva, il file è vivo, la `lang()` è vera — a spegnerla è il **ramo della lingua**. Atteso: **21 righe, 0 già tradotte** — 11 in `command.hsp` (tutte rinviate), 9 in `main.hsp` (la finestra dei comandi per principianti, che in inglese non esiste: le nove righe hanno tutte lo stesso segnaposto «Essential is normal mode.»), 1 in `item_func.hsp`. ⚠️ **Se «già tradotte» sale sopra 0, un lotto ha speso lavoro su testo morto.** 💡 Il filtro del letterale non è un dettaglio: senza, `font lang(cfg_font1, cfg_font2)` gonfiava il conto a 24 e faceva comparire `system.hsp`, che di testo non ne ha nemmeno una riga | all'apertura di un file, insieme a `blocchi_en.py` e `else_jp.py` |
| `commenti-blocco.py` | ⚠️ **le righe dentro un commento di blocco `/* ... */`**, cioè il codice di monte che il mod ha spento. Nato nella 37ª su `proc.hsp:11796`, dove la rete 6 — che guardava solo il `;` — avrebbe fatto tradurre testo morto. `proc.hsp` ne ha **99**, `action.hsp` 132, `custom_tweaks.hsp` 100. ⚠️ Legge il **`SORGENTE`** pinnato, non la build | dalla rete 6 di ogni lotto, e all'apertura di un file |
| `misura-blocchi-spenti.py` | quante voci **già tradotte** stanno dentro un blocco spento: lavoro speso su testo che il giocatore non legge. Atteso al 14/08: **7** — 6 in `action.hsp`, 1 in `proc.hsp` (`:1000`, l'incasso delle esibizioni sostituito dal blocco `ANNA CUSTOM`). ⚠️ Misurato sulla **build** ne accusava 9, e le due di `text.hsp` erano giuste: quella build ha **una riga in più** del sorgente perché una toppa ce l'ha aggiunta, e i numeri di riga del dizionario vengono dal sorgente | quando si tocca `commenti-blocco.py` |
| `lotto-fase2-buffdesc-001.py`, `lotto-fase4-proc-001.py` … `-003.py` | i lotti della 33ª, tenuti come **modelli** storici: dizionario `{(riga, en): resa}` più le prime cinque reti | superati dai modelli qui sotto |
| ⭐⭐ `modello-rete9.py` | **il modello da copiare** (43ª): ha tutte e quattordici le reti con la **rete 9 corretta** — faceva `.rstrip()` sull'inglese e cancellava la differenza fra una testa di frase (« and» in coda) e una congiunzione infissa (« and »), bocciando una resa giusta. ⚠️ **Un modello non può essere un lotto che rinvia qualcosa**: `assembla-lotto.py` vuole l'ancora `RINVIATE = set()`, e per questo il file vive separato invece di essere l'ultimo lotto. Stessa forma di `modello-chiave-lunga.py` della 41ª | per ogni lotto nuovo — ma **non a mano**, vedi `assembla-lotto.py` |
| `lotto-fase4-proc-026.py` | il modello **fino alla 42ª**, ultimo lotto di `proc.hsp` (39ª). Tenuto come storia: i lotti dal `proc-005` in poi si leggono da lì | mai più come modello: vedi la riga sopra |
| ⭐⭐ `assembla-lotto.py` | **copia le reti VERBATIM dal modello** e cambia solo le cinque costanti che devono cambiare — `USCITA`, `DA, A`, `RINVIATE`, `SORGENTE` e il percorso dell'estrazione — poi **rilegge quel che ha scritto** e lo confronta col modello carattere per carattere. Rende meccanica la regola «si copia il file, non si riscrive a memoria», che la ripresa ripeteva da cinque sessioni senza poterla imporre. Vuole due file scritti a mano (`testaNNN.py` col docstring, `reseNNN.py` col dizionario) più un `rinviateNNN.py` facoltativo. ⚠️ Il **sesto argomento è il file `.hsp`**, e senza si intende `proc.hsp` | per **ogni** lotto |
| ⭐ `dossier.py` | le tre letture che ogni lotto rifaceva a mano: il sorgente intorno alla riga, le rese gemelle per **giapponese** e quelle per **inglese**. È la regola «cercare prima di scrivere» resa meccanica — nella 39ª ha pescato **dodici copie su trentaquattro** in un lotto solo, e ha trovato il caso `:20200` (stesso inglese di `action.hsp:11649`, giapponese diverso). ⚠️ Legge il **`SORGENTE`**, non la build | **prima** di scrivere le rese, su ogni zona |
| `perimetro.py` | il conto vero di quanto manca, descrizioni degli oggetti e file di `data/` compresi. ⚠️ **Non si deduce sommando `verifica --dizionario`**, che misura solo il perimetro `lang()`. Atteso a fine 39ª: perimetro **49%**, totale vero **36%** | all'apertura, e quando serve rispondere «a che punto siamo» |
| `variabili_en.py` | ⚠️ **il terzo punto cieco**, dopo `blocchi_en.py` e `else_jp.py`: le variabili che si portano dentro un letterale inglese e finiscono interpolate in una `lang()`, dove nessuno dei due referti le vede perché l'assegnamento è **incondizionato**. Atteso: **66 variabili, 3 trappole** — se sale a 4 qualcuno ne ha creata una, se scende a 2 `economy.hsp:319` è stato risolto | all'apertura |
| `rinvia-proc-4958.py`, `rinvia-proc-navi.py`, `rinvia-proc-11796.py` | come si scrive un rinvio in `rinviate.jsonl` col motivo per esteso | quando una rete 6 o 7 scatta |
| ⭐ `toppa-action-15221.py`, `toppa-proc-24107.py`, `toppa-chara_func-3037.py` | **rinvio + toppa insieme**, per la riga che il dizionario non può aggiustare: la toppa riporta il ramo inglese alla forma del giapponese e il rinvio dice perché. ⚠️ Le toppe **non passano da `degrada()`**: la sostituzione non deve portare accenti, e va scritta per non averne bisogno. 💡 **E si compone, si codifica in memoria e solo allora si apre il file**: vedi il riquadro qui sotto | quando la rete 11 boccia la resa giusta |
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
