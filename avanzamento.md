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
| `text.hsp` | 646 | 1.740 | 37% | 2.127 |
| `command.hsp` | 0 | 1.304 | 0% | 1.481 |
| `action.hsp` | 0 | 1.288 | 0% | 1.502 |
| `proc.hsp` | 0 | 1.098 | 0% | 1.327 |
| `skill.hsp` | 0 | 885 | 0% | 894 |
| `trait.hsp` | 0 | 373 | 0% | 406 |
| `db_item.hsp` | 86 | 1.606 | 5% | 1.607 |
| `item_data.hsp` | 83 | 318 | 26% | 318 |
| **totale** | **815** | **8.612** | **9%** | **9.662** |

`item_data.hsp` è entrato il 2026-08-08, e non era nel piano: ci sono i **45
materiali** (`mtname`), che il primo collaudo ha mostrato anteposti al nome in
ordine inglese — «bronze corazza». Le 83 voci fatte sono i 38 materiali, i 38
epiteti e le 7 piante dei semi; le altre 235 sono altri dati degli oggetti,
ancora da guardare.

L'ordine è quello del piano, per visibilità decrescente: quello che si vede di
più si traduce prima, così ogni lotto ha valore anche se il progetto si ferma lì.

`db_item.hsp` è entrato in coda il 2026-08-07, quando `siti()` ha imparato il
**secondo tipo di sito** (`contratto-nomi.md` §2). La percentuale totale è scesa
dal 10% all'8% senza che nessuno abbia disfatto niente: il denominatore era
incompleto, e i nomi degli oggetti erano lavoro che il conteggio non vedeva.
Una metrica che scende perché ha smesso di mentire è una metrica migliore.

I 1.607 siti sono 1.321 blocchi canonici meno 12 nomi inglesi vuoti, più i 298
`ioriginalnameref2` non vuoti — i nomi che si compongono (`deed of camp`). Le
firme sono **1.606**, una sola in meno dei siti: una coppia giapponese-inglese
ripetuta.

⚠️ **Corretto il 2026-08-08: qui c'era scritto 1.591, e la differenza erano
esattamente le 15 firme che `estrai --da-tradurre` non offriva.** Il numero era
stato preso dall'uscita dell'estrazione invece che dalla scansione, e portava
dentro il suo difetto: `rinviate.jsonl` è indicizzato per firma, e 15 voci
rinviate su `text.hsp` (risposte del quiz, nomi casuali) hanno lo stesso
contenuto di 15 nomi di oggetto. Quei nomi sparivano da ogni lotto, e la
metrica li aveva già dimenticati.

**La regola che ne resta: il denominatore si misura sul sorgente, mai
sull'uscita di uno strumento.** Uno strumento che filtra fa passare il suo
filtro dentro il numero, e una metrica costruita così non può segnalare il
difetto che la produce. Le due misure vanno tenute separate e confrontate: se
`verifica --dizionario` e `estrai --da-tradurre` non tornano, è un difetto, non
un arrotondamento.

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
| nomi casuali degli oggetti (`text.hsp:176-192`) | 30 | `_namepotion`+`strpotion` costruiscono «clear potion». In italiano cambia **l'ordine** («pozione trasparente») oltre al genere, e gli aggettivi sono condivisi fra sei classi di sostantivo con generi diversi: «pozione chiara» ma «anello chiaro» |
| `elename()` (`text.hsp:203-271`) | 20 | → **con `proc.hsp`, in questa fase.** Aggettivo elementale che modifica la parte del corpo di `_melee(2,…)`: `proc.hsp:8797` compone `elename(ele) + " " + _melee(2,…)`. In italiano l'aggettivo segue il nome e ne prende il genere, e i nomi sono di generi misti (mano, artiglio, zanna, occhio). L'ordine si sistema traducendo `proc.hsp`, che è una dinamica e permette di riordinare la concatenazione |
| nomi di magia nel quiz (`text.hsp:978-987`) | 4 | → **con `skill.hsp`, in questa fase** |
| nomi di creatura e oggetto nel quiz | 59 | risposte del quiz che nominano creature e oggetti. Il nome vero sta in `db_creature.hsp`/`db_item.hsp`: tradurlo qui prima farebbe divergere la risposta dal nome che il giocatore legge |
| parti meccaniche (`text.hsp:1387-1402`) | 6 | verificato che compaiono anche in `db_item.hsp` |
| **totale** | **154** | |

**Tre uscite il 2026-08-08: `blessed`, `cursed`, `doomed`.** Erano rinviate
perché si antepongono al nome e in italiano un participio si accorderebbe con
un oggetto di genere ignoto. La premessa del rinvio — «i nomi di `db_item.hsp`
non li risolviamo in questa fase» — è caduta quando i nomi sono entrati nella
catena, e la forma è la stessa degli epiteti del materiale: **complemento**,
«con benedizione», che non chiede accordo a nessuno. Le tre stringhe si
spostano in coda con `locvar_itemname_s7` (`item_func.hsp:1204, 1207, 1210`,
solo il ramo inglese).

Il resto del loro motivo **non** è caduto: il sistema dei nomi casuali resta
rinviato, ed è un problema suo.

⚠️ **Il conto è cresciuto da 68 a 157 in un lotto solo**, ed è quasi tutto la
stessa dipendenza: i nomi di creature e oggetti della Fase 2. Vale la pena
guardarlo prima di tirare avanti — la Fase 1 sta accumulando debito verso una
decisione che non ha preso, esattamente come `init.hsp` accumulava debito
verso il registro finché non è stato promosso da Fase 4 a Fase 1.

Sono **aggettivi prefissi al nome di un oggetto**, e in italiano un aggettivo
prefisso vuole il genere del nome che segue. Quel nome vive in `db_item.hsp`,
e il piano della Fase 1 dice esplicitamente di non risolvere dove stanno i nomi
degli oggetti (SPEC §2, punto ancora aperto). Tradurli ora significherebbe
scegliere un genere al posto di quella decisione, in 35 punti, in silenzio.

È lo stesso nodo dell'articolo di `name()`, risolto nella quarta sessione
rimandando la scelta a chi conosce il nome. Qui si rimanda allo stesso posto.
