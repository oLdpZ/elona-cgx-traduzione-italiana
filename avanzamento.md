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
| `text.hsp` | 721 | 1.740 | 41% | 2.127 |
| `command.hsp` | 0 | 1.304 | 0% | 1.481 |
| `action.hsp` | 0 | 1.288 | 0% | 1.502 |
| `proc.hsp` | 0 | 1.098 | 0% | 1.327 |
| `skill.hsp` | **885** | 885 | **100%** | 894 |
| `trait.hsp` | 0 | 373 | 0% | 406 |
| `db_item.hsp` | **1.605** | 1.606 | **100%** | 1.607 |
| `item_data.hsp` | **318** | 318 | **100%** | 318 |
| `custom_tweaks.hsp` | **12** | 12 | **100%** | 28 |
| **totale** | **3.541** | **8.624** | **41%** | **9.690** |

## `skill.hsp` è chiuso — 2026-08-09, tredicesima sessione

**Quarto file completo**, 885 su 885, e il più grosso dei quattro dopo
`db_item.hsp`. L'ultimo blocco erano le **276 mosse speciali**, tetto 24
caratteri già misurato il giorno prima.

Quindici nomi restano inglesi per scelta, dichiarati in `invariati.md`.
⚠️ **La regola della marca 《》 degli artefatti non si applica alle mosse**: il
nome di un artefatto è un nome proprio, quello di una mossa è un'etichetta
funzionale che si sceglie da un elenco. Vedi `decisioni.md`.

## Le rinviate scendono da 120 a 80 — 2026-08-09, tredicesima sessione

Tre dei cinque motivi erano scaduti o falsi.

| gruppo | voci | esito |
|---|---|---|
| risposte del quiz sui grimori | 4 | il rinvio era a `skill.hsp`, che oggi è chiuso |
| parti meccaniche `Change …` | 6 | ⚠️ **la dipendenza dichiarata non esisteva**: in `db_item.hsp` non ce n'è nessuna |
| nomi casuali degli oggetti | 30 | risolti con 213 toppe generate, vedi sotto |
| risposte del quiz su creature | 59 | rinvio **vivo**: aspettano i nomi di creatura |
| `elename()` | 20 | rinvio **vivo**: aspettano `proc.hsp` |
| `<Pants of Ogre>` | 1 | rinvio **vivo**: aspetta `orc`/`ogre` |

I nomi casuali hanno chiesto il primo ribaltamento d'ordine del progetto:
`db_item.hsp` compone «aggettivo + nome» in **213 siti**, e in italiano
l'aggettivo segue il nome. L'ordine sta nel codice, non nelle stringhe, quindi
il dizionario non lo raggiunge: le toppe le genera
`strumenti/genera_toppe_casuali.py`, una per sito, ognuna con l'aggancio unico
del proprio `ITEM_ID`.

⚠️ **Il genere è una proprietà dell'array, non della riga**, come l'articolo dei
pesci: le rese si accordano una volta per famiglia. Le sei firme condivise fra
due famiglie prendono la **forma invariabile** — quattro sono materiali e lo
sono già, due l'hanno presa apposta.

## `item_data.hsp` è chiuso — 2026-08-09, undicesima sessione

**Secondo file completo**, e a differenza del primo senza nemmeno un rinvio:
318 su 318.

I 235 rimasti a inizio sessione non erano un mucchio. La classe qui non è
`reftype` come in `db_item.hsp` ma **l'array che dichiara la voce**, e con
quella chiave si sciolgono in cinque discipline diverse, chiuse in tre lotti:

| lotto | criterio | voci |
|---|---|---|
| ego | `egoname` + `egominorn` | 29 |
| pesci | `fishdatan` | 113 (10 invariati) |
| incantamenti | `encDisp`, le dinamiche di `*item_encdetail`, `ammoname` | 93 (2 invariati) |

Le tre cose che il file ha insegnato, in ordine di prezzo:

1. **Il posto decide se i dati arrivano in tempo.**
   `ioriginalnameref(ITEM_ID_FISH)` è la stringa vuota: il nome della specie è
   *tutto* il nome e arriva da `itemNameSub`, che gira **dopo** l'articolo.
   Tradurre i 113 nomi e basta avrebbe dato «a salmone», e nessun test lo
   avrebbe visto.
2. **L'ego va dopo il materiale**, il che vuole una coda propria (`s10`)
   riversata fra materiale e stato.
3. **Il soggetto sta fuori dai file estratti.** `lang("それは", "It ")` è in
   `command.hsp`, e `s` compare in quattro siti di cui tre senza soggetto: le
   rese sono verbi alla terza persona senza soggetto, e il prefisso si spegne
   con una toppa.

## `db_item.hsp` è chiuso — 2026-08-09, decima sessione

**Primo file completo del progetto**: 1.605 firme su 1.606. L'unica mancante è
`<Pants of Ogre>`, che è **rinviata** e non dimenticata (vedi più sotto).

Il file è passato da 599 nomi da guardare a zero in una sessione, con sei lotti.
Il criterio non è stato la forma del nome, che era il candidato scritto qui
ieri, ma **la categoria che il sorgente dichiara**.

I lotti dal terzo al sesto erano stati scelti per `filter_item`. Quando quel
criterio si è esaurito, ciò che restava si chiamava «il gruppo senza filtro»: un
residuo da affrontare a occhio. Non era un residuo. La categoria c'è, solo che
sta **dentro il blocco di ogni oggetto** — `reftype = FILTER_ITEM_...` — e
classifica **1.320 oggetti**.

Lo strumento è `strumenti/categorie.py`, con cinque test:

```powershell
python -m strumenti.categorie                                 # il resto, per categoria
python -m strumenti.categorie --categoria FILTER_ITEM_TOOL --uscita lavoro/x.jsonl
```

⚠️ **Vale anche per gli altri file.** `item_data.hsp` e i cinque mai guardati
non sono stati letti con questa chiave: prima di dichiararli senza struttura,
si cerca dove il codice li struttura.

| lotto | criterio | voci |
|---|---|---|
| artefatti fra `<>` | forma del nome più la marca 《》 | 169 (105 invariati, 63 tradotti, 1 rinviato) |
| arredamento da `map_fur_*` | array del generatore di mappe | 46 |
| cibo | `FILTER_ITEM_FOOD` | 51 |
| arredamento | `FILTER_FURNITURE` | 100 |
| attrezzi | `FILTER_ITEM_TOOL` | 107 |
| scarto | `FILTER_JUNK` | 59 |
| code corte | nove categorie insieme | 67 |

**Sui 169 artefatti la domanda era di invarianza, non di resa**, e la regola sta
in `decisioni.md`: l'inglese romanizzato o siglato resta; il giapponese fra
《》 e traslitterato resta; il giapponese descrittivo si traduce. La prova che
non è stata cucita addosso al lotto è che riproduce tutti e otto i precedenti
già presi.

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
| nomi casuali degli oggetti (`text.hsp:176-192`) | 30 | `_namepotion`+`strpotion` costruiscono «clear potion». In italiano cambia **l'ordine** («pozione trasparente») oltre al genere, e gli aggettivi sono condivisi fra sei classi di sostantivo con generi diversi: «pozione chiara» ma «anello chiaro» |
| `elename()` (`text.hsp:203-271`) | 20 | → **con `proc.hsp`, in questa fase.** Aggettivo elementale che modifica la parte del corpo di `_melee(2,…)`: `proc.hsp:8797` compone `elename(ele) + " " + _melee(2,…)`. In italiano l'aggettivo segue il nome e ne prende il genere, e i nomi sono di generi misti (mano, artiglio, zanna, occhio). L'ordine si sistema traducendo `proc.hsp`, che è una dinamica e permette di riordinare la concatenazione |
| nomi di magia nel quiz (`text.hsp:978-987`) | 4 | → **con `skill.hsp`, in questa fase** |
| nomi di creatura e oggetto nel quiz | 59 | risposte del quiz che nominano creature e oggetti. Il nome vero sta in `db_creature.hsp`/`db_item.hsp`: tradurlo qui prima farebbe divergere la risposta dal nome che il giocatore legge |
| parti meccaniche (`text.hsp:1387-1402`) | 6 | verificato che compaiono anche in `db_item.hsp` |
| `<Pants of Ogre>` (`db_item.hsp`) | 1 | il nome contiene `ogre`, e in `db_creature.hsp` `orc` e `ogre` convivono come creature distinte (`orc warrior`, `black orc` contro `slash ogre`, `shine ogre`): «orco» non può coprirle entrambe. **Primo rinvio deciso da `db_item.hsp`**, e per questo `test_i_nomi_di_db_item_non_sono_rinviati_da_text` ha smesso di asserire `== set()` — era una procura — e adesso pretende la proprietà vera: ogni firma che esce per `db_item.hsp` viene da una riga **di** `db_item.hsp` |
| **totale** | **120** | |

## Le 35 uscite della nona sessione (2026-08-08)

Sono uscite dal rinvio `_furniture` (11), `_bookself` (7), `_bookselfs` (7) e
`_weight` (10). Il motivo del rinvio era corretto quando fu scritto — «aggettivi
prefissi a un nome di genere ignoto, che vive in `db_item.hsp`» — ed è caduto
quando i nomi sono entrati nella catena.

⚠️ **Ma il rinvio le trattava come un gruppo solo, e non lo erano.** Quattro
array che il documento dava per «la stessa identica forma» hanno chiesto
**quattro cure diverse**, e scoprirlo è stato il lavoro vero della sessione:

| array | dove esce in inglese | cura |
|---|---|---|
| `_furniture` | prefisso al nome | toppa: sposta in `locvar_itemname_s6`, rese a complemento invariante |
| `_bookself` | **già fra parentesi** (`item_func.hsp:988`) | **nessuna toppa**: solo dato. L'unico della famiglia in cui il sorgente andava bene |
| `_weight` | già suffisso, ma con giunto « grown » | toppa **sul giunto**: « di taglia » introduce una testa femminile fissa, e l'accordo smette di dipendere dall'oggetto |
| `_bookselfs` | slot della parola-contatore (`item_func.hsp:1233`) | trattamento di `contatori.jsonl`: singolare, plurale, genere, e un `case` in **entrambi** gli switch |

**La lezione, che vale oltre questi quattro: «stessa forma» è un'ipotesi, non un
fatto, e va verificata guardando il sito di concatenazione prima di scrivere la
toppa.** Il documento di ripresa li dava per identici in buona fede, sulla base
del fatto che sono tutti aggettivi prefissi in `text.hsp`. Lo sono nel
dizionario; non lo sono nel codice, ed è il codice che decide la cura.

⚠️ **Un legame fragile creato qui, da ricordare.** Fra `contatori.jsonl` e il
dizionario il legame è **per stringa**: il `case` dello switch confronta la resa
del primo con quella che l'array porta a runtime, che viene dal secondo. Se
divergono il `case` non aggancia mai — e restano verdi sia il compilatore sia la
prova d'identità. Ora lo pretendono `genera_toppe_nomi.py` (alla generazione) e
un test (a ogni giro).

**Coperte anche le altre 39, il 2026-08-09.** `contatori.jsonl` ha tre fonti:
`text` (le sette del libro prodotto) e `item_func` (le sei cablate) alimentano
il generatore ed erano già difese; le **39 con `fonte: "db_item"`** sono il
registro di ciò che il dizionario dice per lo slot `ioriginalnameref2`, e su di
esse non guardava nessuno.

Il confronto giusto **non è l'uguaglianza**, e a insegnarlo è `grave`: il
registro dice «tomba», il dizionario «tomba ornata», e ha ragione il dizionario,
perché il nome si monta `s2 + " " + s3 + " " + s1` col giunto fissato a «di» e
l'aggettivo deve stare in `s2` per accordarsi con la testa. A schermo esce
«tomba ornata di fiori». Il registro dice il **termine**, il dizionario il
**segmento**: due livelli, non due verità. Il test pretende quindi che la resa
del dizionario **cominci con** il termine del registro.

**Tre uscite precedenti, sempre il 2026-08-08: `blessed`, `cursed`, `doomed`.** Erano rinviate
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
