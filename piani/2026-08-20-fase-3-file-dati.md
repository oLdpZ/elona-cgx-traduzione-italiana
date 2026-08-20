# Fase 3 — I file dati di `data\`

Aperto nella **settantesima** sessione, 2026-08-20.

## Perché esiste questa fase

Cinque file di `elonaplus2.31\data\` contengono **155.140 caratteri** di testo
inglese che il giocatore legge, e **nessun contatore del progetto li ha mai
visti**. Non sono un file dimenticato: sono una *categoria* fuori dal perimetro,
perché ogni rete del progetto guarda le `lang()` degli `.hsp` e lì di `lang()`
non ce n'è nessuna.

| file | righe EN | caratteri EN | chi lo carica | cosa contiene |
|---|---:|---:|---|---|
| `book.txt` | 2.208 | 67.184 | `item.hsp:112`, `command.hsp:8371` | i libri che si leggono in gioco |
| `talk.txt` | 569 | 44.166 | `text.hsp:9361` | le chiacchiere dei PNG, per area |
| `manual_ENG.txt` | 591 | 33.048 | `help.hsp:331` | il manuale in gioco |
| `exhelp.txt` | 185 | 6.701 | `help.hsp:227` | l'aiuto esteso |
| `board.txt` | 25 | 4.041 | `init.hsp:2574` | la bacheca degli incarichi |

È la lezione della 54ª — *un file senza file di dizionario non è un file finito,
è un file che nessun conteggio guarda* — applicata a un formato invece che a un
file.

## Le due famiglie

⭐⭐ **La riga non vuol dire la stessa cosa nei cinque file, e il conto lo
dimostra.** Contando le righe dei blocchi appaiati:

    book.txt     un blocco da  33 righe JP contro 224 EN
    exhelp.txt   un blocco da   7 righe JP contro  20 EN
    talk.txt     68 blocchi su 88 hanno righe pari
    board.txt    2 righe JP contro 1 EN, sistematicamente

In `book.txt` e `exhelp.txt` l'inglese è **spezzato a mano a larghezza fissa**
dove il giapponese non lo è: la riga è un'unità di **disegno**, l'unità di
traduzione è il blocco, e l'italiano va reimpaginato. In `board.txt` e
`talk.txt` la riga è un'unità di **senso** e si traduce così com'è.

**Questa fase apre la famiglia facile e comincia da `board.txt`**, che è il file
più piccolo e sta dalla parte giusta. La famiglia dell'impaginazione è un
seguito, e vuole prima una misura della colonna presa dalla geometria del
disegno (regola della 55ª), non dal numero di caratteri che l'inglese usa.

## Quel che il sito dice di `board.txt`

`text.hsp:11644 *talk_quest_load`:

    p = instr(buffboard, 0, s + "," + lang("JP", "EN"))   ; trova il blocco
    buff2 = strmid(buffboard, p, instr(buffboard, p, "%END"))
    if ( noteinfo(0) <= 1 ) { buff2 = "no txt" : return } ; blocco vuoto
    p = rnd(noteinfo(0) - 1) + 1                          ; UNA RIGA A CASO
    noteget buff2, p
    p = instr(buff2, 0, ":")                              ; spacca al PRIMO due punti
    s(3) = strmid(buff2, 0, p)                            ; titolo dell'incarico
    buff2 = strmid(buff2, p + 1, ...)                     ; corpo

Ne discendono quattro vincoli che diventano reti:

1. una riga = un incarico intero, pescato a caso: **le righe sono
   intercambiabili**, quindi nessuna può dipendere da un'altra;
2. il **primo** due punti divide titolo e corpo: un due punti nel titolo
   italiano sposta il taglio;
3. una riga vuota o un `%` in mezzo spaccano il blocco;
4. il corpo lo manda a capo `talk_conv buff, 70` (`command.hsp:3367`), che nel
   ramo non giapponese spezza **sulle spaziature**: niente da impaginare a mano,
   ma una parola italiana lunga senza spazi sfora.

I segnaposto li espande `*talktxt_conv` (`text.hsp:11922`). Due famiglie:

- **contenuto**, che vale anche in italiano: `{objective}` `{reward}` `{ref}`
  `{map}` `{client}` `{me}` `{you}` `{player}` `{aka}` `{npc}` `{deadline}`, più
  `{n}` che è un a-capo;
- **grammatica giapponese**, che in italiano non deve comparire mai: `{だ}`
  `{のだ}` `{くれ}` `{よ}` `{う}` `{かな}` `{る}` `{な}` `{が}` `{だな}` `{だろ}`
  `{た}` `{ある}` `{か}` `{たのむ}`.

⚠️ Un nome fuori da tutt'e due le famiglie **resta a schermo fra graffe**:
`talktxt_conv` sostituisce solo quel che riconosce.

## ⭐ L'inglese di `board.txt` non è appaiato al giapponese

Misurato: `COOK,1` ha un inglese che rende la **seconda** riga giapponese, non
la prima; `COOK,3` non ne rende nessuna delle due; `COOK,8` ha un giapponese
**identico** a quello di `COOK,GENERAL` e un inglese tutto suo. Sessantatré
righe giapponesi contro venticinque inglesi: monte ne ha buttate via trentotto.

Non è sciatteria, **è dichiarato nel file stesso** (righe 22-24):

> Text written after %xxx,x,EN will be displayed in the English version of
> Elona. The translation doesn't have to be precise. You can even add your own
> sentences if you like to.

È l'unico posto del progetto dove monte autorizza per iscritto a scrivere righe
nuove. Conseguenza per il dizionario: il giapponese si porta dietro come
**contesto del blocco**, non come coppia della riga, perché coppia non è.

**Primo lotto: le 25 righe inglesi.** Rimettere le 38 varianti perdute è un
secondo lotto, da decidere quando il primo ha funzionato — e allora COOK,8 va
scritto a mano, perché il suo giapponese è un doppione.

## Il progetto

### 1. Il sorgente pinnato

`applica` ricopia `sorgente/` in `build/` da zero, e il working tree di
`sorgente/` ha i file dati **cancellati** (git li traccia sotto
`dist/2.05-custom-gx/data/`, `status` li dà `D`). Il riferimento va preso
altrove.

`_traduzione\dati-sorgente\` — riempita **una volta sola dal gioco installato**
e mai riscritta. Perché dal gioco e non da monte: è il file che l'eseguibile
legge davvero, e per `talk.txt` e `autopick.txt` il gioco installato è più
recente del commit pinnato (`board`, `book`, `exhelp` invece combaciano a meno
dei fine riga).

Nel vault va solo `dati/manifesto.json`: md5 e byte dei cinque file. Serve
all'altra macchina per verificare di avere gli stessi byte, e fa vedere subito
un aggiornamento del gioco invece di lasciarlo corrompere un lotto in silenzio.

`percorsi.py` guadagna `DATI_SORGENTE` e `BUILD_DATI`.

### 2. Il formato, in un modulo solo

`strumenti/dati.py` sa com'è fatto un file a blocchi, e nessun altro:

    analizza(testo) -> [Blocco(intestazione, chiave, lingua, righe)]
    serializza(blocchi) -> testo

con **round-trip byte per byte**, CRLF compresi. È il pezzo che decide se la
strada esiste: se il round-trip non è esatto sui cinque file veri, il resto non
si scrive.

⚠️ **I file dati vogliono i CRLF** — `noteinfo(0)` conta le righe sui CRLF, e un
file a LF soltanto per HSP è una riga sola (lezione della 65ª, costò il gioco
piantato alla creazione del personaggio).

### 3. Il dizionario

`dizionario/dati/board.txt.jsonl` — sottocartella apposta, perché `applica` fa
`DIZIONARIO.glob("*.jsonl")` non ricorsivo e i due rami non si devono pestare.
Una voce per riga inglese:

```json
{"firma": "<sha1 di file|blocco|indice|en>", "file": "board.txt",
 "blocco": "COOK,GENERAL", "riga": 1,
 "en": "A new recipe!:...", "jp_contesto": ["料理家の野望:...", "美味しいものが食べたい:..."],
 "it": ""}
```

La firma sull'**inglese** e non sulla posizione: se monte riscrive una riga la
voce resta **orfana** e il referto lo dice, invece di applicare una resa a un
testo che non è più quello.

### 4. Consegna

Toppa su `init.hsp:2574` → `"data\\board_it.txt"`. `applica` scrive
`_traduzione\build\dati\board_it.txt`; l'installazione lo copia in
`elonaplus2.31\data\`, **accanto** all'originale che resta intatto.

⭐ È la disciplina di `cgx-test.exe`, che non sovrascrive `elonapluscgx.exe`:
l'eseguibile inglese continua a girare col suo file, e un confronto è sempre a
portata di mano.

⚠️ `manual_ENG.txt` non avrà bisogno di toppa: il suo nome sta **già dentro una
`lang()`** (`help.hsp:331`), quindi è una voce di dizionario normale.

### 5. Le reti

| rete | cosa guarda | perché |
|---|---|---|
| **prova d'identità dati** | dizionario che traduce ogni riga in sé → file ricostruito identico byte per byte | la verifica più forte della catena, la stessa logica della `prova_identita` degli `.hsp`. Diventa la **dodicesima verifica d'apertura** |
| **segnaposto** | l'insieme dei `{...}` in `it` uguale a quello in `en`, e nessuno della famiglia grammaticale giapponese | un nome che `talktxt_conv` non conosce resta a schermo fra graffe |
| **due punti** | ogni resa ha almeno un `:`, e il titolo davanti non è vuoto | `text.hsp:11656` spacca al primo due punti |
| **struttura** | nessuna resa contiene a-capo, è vuota, o comincia per `%` | spaccherebbero il blocco o `%END` |
| **doppi byte CP932** | `accenti.doppi_byte_cp932()` sulle rese | la regola di ogni lotto |

### 6. Ordine di lavoro

1. `dati.py` + test di round-trip **sui cinque file veri**, non su un caso
   costruito (regola della 56ª: un caso costruito prova la funzione, non il
   corpus)
2. `percorsi`, `dati-sorgente\`, manifesto
3. estrazione del lotto → `lavoro/board-001.jsonl`, 25 voci
4. le reti in `verifica.py`, coi test
5. le 25 rese
6. `reimporta` → `applica` → la toppa → `compila --eseguibile`
7. **collaudo**: aprire la bacheca degli incarichi di una città e leggere una
   richiesta

## Quel che questa fase NON fa

- `book.txt`, `exhelp.txt`, `manual_ENG.txt`: famiglia dell'impaginazione, e
  vogliono prima la misura della colonna dalla geometria del disegno.
- `talk.txt`: stessa famiglia di `board.txt` ma venti volte più grosso, e venti
  blocchi su ottantotto hanno righe dispari — va guardato prima di prometterlo.
- `autopick.txt`: è il file che il **giocatore scrive**, e le sue chiavi sono
  confronti (`custom_autopick.hsp`, 78 `lang()` dentro `instr`). Vuole una
  decisione sua, che è la stessa della 69ª: un aggettivo prefisso non si traduce
  se serve più di un nome.
