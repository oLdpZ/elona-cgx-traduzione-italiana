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
| `lotto-fase2-buffdesc-001.py`, `lotto-fase4-proc-001.py` … `-003.py` | i lotti della 33ª, tenuti come **modelli** storici: dizionario `{(riga, en): resa}` più le prime cinque reti | superati dai modelli qui sotto |
| ⭐ `lotto-fase4-proc-005.py` … `-010.py` | i sei lotti della 35ª. **`-010` è il modello da copiare**: ha tutte e nove le reti | per ogni lotto nuovo |
| `rinvia-proc-4958.py`, `rinvia-proc-navi.py` | come si scrive un rinvio in `rinviate.jsonl` col motivo per esteso | quando una rete 6 o 7 scatta |
| `correzione-bolt.py` | come si corregge una resa **già entrata nel dizionario** senza passare da un lotto, con le reti che impediscono di correggerne una di troppo o una di meno | quando due file dicono la stessa cosa in due modi |

### Le nove reti dello script di lotto

Ognuna nasce da un caso vero, non da un'idea. Le prime cinque sono della 33ª e
della 31ª, le altre della 35ª.

| # | che cosa impedisce | il caso che l'ha fatta nascere |
|---|---|---|
| 0 | che la chiave `(riga, en)` identifichi più di una voce | il riciclo inglese, 84 stringhe su 231 giapponesi |
| 1 | che una voce della zona resti senza resa | — |
| 2 | che una resa non agganci nessuna voce | due lotti scritti sulla voce sbagliata (27ª) |
| 3 | che si renda in un modo nuovo un giapponese **già reso altrove** | ⭐ nella 35ª ha parlato **quattro volte**, e aveva sempre ragione: `:6481` (7 siti), `:6492` (5 siti), `:6951`, `:4310` |
| 4 | che lo stesso giapponese abbia due rese **dentro lo stesso lotto** | i due Yerleswood, lotto `039` |
| 5 | che l'accento sia **decomposto** (`a` + U+0300) invece che precomposto | cinque rese su 43 nel lotto `-005`: a occhio identiche, e CP932 non ha il combinante |
| 6 | che si traduca una voce su una **riga commentata** | `proc.hsp:4958`, il blocco `MANUSCRIPT HINT` spento per intero |
| 7 | che si traduca un **operando di confronto** | `:5584`, i due nomi di nave che `map.hsp` assegna e `proc.hsp` confronta |
| 8 | una **preposizione che si fonde** (`di`/`da`/`in`/`su`/`a`) davanti a `name`/`itemname`/`valn`/`cdatan` | `valn` è un `itemname()` sotto falso nome, e l'inglese ci mette «from» e «in» |
| 9 | che una **testa di frase** (l'inglese finisce in « and») non si chiuda col connettivo | le dieci teste del log di combattimento, che si saldano alla coda di danno di `chara_func.hsp` |

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

💡 `simili.py` e `gia_rese.py` leggono `lavoro/_buff.jsonl`: per un file diverso
si cambia quella riga. Non è un difetto da sistemare — sono scratch, e il costo
di parametrizzarli è più alto di quello di cambiarli.
