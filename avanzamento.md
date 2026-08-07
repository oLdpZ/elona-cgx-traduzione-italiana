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
| `text.hsp` | 482 | 1.740 | 28% | 2.127 |
| `command.hsp` | 0 | 1.304 | 0% | 1.481 |
| `action.hsp` | 0 | 1.288 | 0% | 1.502 |
| `proc.hsp` | 0 | 1.098 | 0% | 1.327 |
| `skill.hsp` | 0 | 885 | 0% | 894 |
| `trait.hsp` | 0 | 373 | 0% | 406 |
| **totale** | **482** | **6.688** | **7%** | **7.737** |

L'ordine è quello del piano, per visibilità decrescente: quello che si vede di
più si traduce prima, così ogni lotto ha valore anche se il progetto si ferma lì.

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
| `_bookself`, `_bookselfs` (`text.hsp:54-55`) | 14 | qualità del libro scritto, concatenata al nome |
| `_furniture` (`text.hsp:56`) | 11 | qualità del mobile, concatenata: `_furniture(...) + " " + itemname` |
| `_weight` (`text.hsp:57`) | 10 | taglia dell'oggetto, concatenata |
| nomi casuali degli oggetti (`text.hsp:176-192`) | 33 | `_namepotion`+`strpotion` costruiscono «clear potion»; `strcursed`/`strblessed` li prefissano. In italiano cambia **l'ordine** («pozione trasparente») oltre al genere |
| **totale** | **68** | |

Sono **aggettivi prefissi al nome di un oggetto**, e in italiano un aggettivo
prefisso vuole il genere del nome che segue. Quel nome vive in `db_item.hsp`,
e il piano della Fase 1 dice esplicitamente di non risolvere dove stanno i nomi
degli oggetti (SPEC §2, punto ancora aperto). Tradurli ora significherebbe
scegliere un genere al posto di quella decisione, in 35 punti, in silenzio.

È lo stesso nodo dell'articolo di `name()`, risolto nella quarta sessione
rimandando la scelta a chi conosce il nome. Qui si rimanda allo stesso posto.
