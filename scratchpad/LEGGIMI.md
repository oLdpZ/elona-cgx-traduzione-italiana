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
| `lotto-fase2-buffdesc-001.py` | il lotto della 33ª, tenuto come **modello**: dizionario `{(riga, en): resa}` più le cinque reti del metodo | da copiare per il prossimo lotto |

Si lanciano dalla radice del repo, con l'interprete giusto:

```powershell
$py = "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"
& $py scratchpad/simili.py
& $py scratchpad/guardie.py lavoro/<lotto>.jsonl
```

💡 `simili.py` e `gia_rese.py` leggono `lavoro/_buff.jsonl`: per un file diverso
si cambia quella riga. Non è un difetto da sistemare — sono scratch, e il costo
di parametrizzarli è più alto di quello di cambiarli.
