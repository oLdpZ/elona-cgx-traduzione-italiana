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
| `lotto-fase2-buffdesc-001.py`, `lotto-fase4-proc-001.py`, `lotto-fase4-proc-002.py`, `lotto-fase4-proc-003.py` | i lotti della 33ª, tenuti come **modelli**: dizionario `{(riga, en): resa}` più le cinque reti del metodo | da copiare per il prossimo lotto |

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
