"""Chiusura della settantesima sessione: RIPRESA e avanzamento."""
from pathlib import Path

RIPRESA = Path("RIPRESA-sessione.md")
AVANZAMENTO = Path("avanzamento.md")

TESTA = """# Ripresa sessione

Aggiornato: 2026-08-20, fine della **settantesima** sessione (**il sedicesimo
punto cieco non era un file: era una CATEGORIA — i file dati di `data\\`, 155.140
caratteri di testo inglese che nessuna rete del progetto aveva mai guardato**).

⭐⭐⭐ **La lezione che vale per tutto il lavoro che viene: UNA RETE PUNTATA SUL
FILE SBAGLIATO NON TACE, MENTE.** La rete dei segnaposto e' stata girata su
`talk.txt` col profilo di `board.txt` e ha «trovato» sei `{nptc}`, riportati a
voce come refuso di monte. Non lo erano: `board.txt` passa da `*talktxt_conv`
(`text.hsp:11922`, 33 nomi) e `talk.txt` da **`*convert_word`**
(`text.hsp:6900`, **46** nomi), che conosce benissimo `nptc`, `npcc` e
diciannove codici di espressione e di suono. E' la domanda della 53a — *finito
per quale referto?* — nella sua forma piu' insidiosa: **misurato con quale
rete?** Un referto sbagliato non si distingue da un reperto: va guardato da
dove viene il metro, non solo che numero da'. Adesso c'e' `PROFILI` in
`dati_verifica.py`, e il profilo porta l'espansore, se la riga e' `titolo:corpo`
e la larghezza dell'a capo.

⚠️⚠️ **E la lezione della 68a e' stata presa in pieno una seconda volta:
l'ostacolo non e' il `pos` che viene dopo leggendo il sorgente.** Il tetto del
titolo di un incarico era stato messo a 34 prendendo la scadenza a `wx + 344`,
che e' il primo `pos` successivo nel testo. Ma `command.hsp:3391` disegna le
**stellette del livello** a `wx + 270` — piu' a sinistra, e **dopo** il titolo.
Tetto vero: **24**. A trovarlo e' stato il collaudo, misurando i pixel della
bacheca di Yowyn: testo a 781 (`wx = 681`), stellette a 951, scadenza a 1027,
cliente a 1073; e «Si fa festa!», dodici caratteri, finiva a 865 = 781 + 12x7.
\U0001f4a1 *Una cosa disegnata dopo copre quel che c'era prima, e l'ordine di lettura
del sorgente non dice qual e' la piu' a sinistra.*

⭐⭐ **E il collaudo ha mostrato una cosa che nessun ragionamento aveva
convinto: due richieste identiche, affiancate.** La bacheca di Yowyn mostrava
«Si fa festa!» due volte, stesso testo, due clienti diversi. Non e' un difetto
della traduzione: `board.txt` ha **una** riga inglese per blocco dove il
giapponese ne ha due o tre — monte ne ha buttate via 38. Finche' la bacheca
mostra un avviso per volta non si nota; con tre dello stesso tipo affiancati, il
taglio di monte diventa visibile. Il secondo lotto di `board.txt` adesso ha una
ragione **misurata**.

---

## La settantesima sessione

### ▶ Il punto esatto in cui si riprende

Tutto e' **spinto** e l'albero di lavoro e' pulito. Si riparte da
`git fetch && git status -sb` e dalle **dodici** verifiche d'apertura (la
dodicesima e' nuova). La sessione si e' aperta su `DESKTOP-1O339MR` con
`origin/fase-0` allineato: e' la **ventisettesima prova** di fila, e le undici
verifiche di allora hanno dato undici volte i valori attesi della 69a.

⚠️⚠️ **I valori cambiati, da usare alla prossima apertura:**

    pytest                  636 passed 6 skipped   (erano 528: +108 test dei file dati)
    toppe.jsonl             1009                   (erano 1006: +1 board, +2 talk)
    dizionario/dati/        NUOVO ramo: board.txt.jsonl (25), talk.txt.jsonl (569, 64 rese)
    dati/manifesto.json     NUOVO: 7 file pinnati, zero LF soli

⭐ **E una verifica d'apertura in piu', la dodicesima:**

    python -m strumenti.dati_applica --identita   # atteso: 4 file, 2.987 righe, tutti ok

⚠️ Vale la pena lanciare anche `python -m strumenti.dati_sorgente` (atteso:
7/7 intatti, gioco difforme su 0): non e' una verifica d'apertura ma dice se il
gioco e' stato aggiornato sotto i piedi del dizionario.

Tutto il resto e' **fermo dov'era**: `prova_identita` 72/72 e 27.813, `creature`
1131/2466/0/0, `larghezze` 0 fuori misura, `diario` 0 su 205, `riquadri` 0 su 38
e 0 su 71, `menu_dialogo` 0 su 151, `linguette` 0 e 0, `battute --divergenti`
**13**, `intestazioni_larghezze` banco ok e perimetro 0, `verifica --dizionario`
0 da ritradurre ovunque. `rinviate.jsonl` 75 e `invariati.md` non sono stati
toccati.

✅ **`cgx-test.exe` e' FRESCO**, e con lui **due file dati nuovi** in
`elonaplus2.31\\data\\`: `board_it.txt` e `talk_it.txt`.

### ▶ Che cosa e' stato fatto

    dati.py                 il formato a blocchi, round-trip sui byte      26 test
    dati_sorgente.py        la copia pinnata e il manifesto                12 test
    dati_estrai.py          il lotto da un file dati                       15 test
    dati_verifica.py        sei reti, coi profili per file                 38 test
    dati_reimporta.py       la promozione a dizionario                      4 test
    dati_applica.py         la costruzione e la prova d'identita'          13 test
    board.txt               il sedicesimo punto cieco, CHIUSO             25 rese
    talk.txt                DEFAULT e le quattro PERSONALITY              64 rese
    IL COLLAUDO             la bacheca di Yowyn, un tetto sbagliato trovato
    ------------------------------------------------------------------------
                            89 rese, 3 toppe, 6 moduli nuovi, 108 test, 6 spinte

### ▶ ⭐⭐⭐ Il pezzo che vale piu' di tutti: la categoria che nessuno guardava

Cinque file di `elonaplus2.31\\data\\` contengono **155.140 caratteri** di testo
inglese che il giocatore legge, e nessun contatore del progetto li aveva mai
visti — perche' ogni rete guarda le `lang()` degli `.hsp`, e li' dentro di
`lang()` non ce n'e' nessuna.

    book.txt        2.208 righe EN   67.184 caratteri   i libri che si leggono
    talk.txt          569            44.166             le chiacchiere dei PNG
    manual_ENG.txt    591            33.048             il manuale in gioco
    exhelp.txt        185             6.701             l'aiuto esteso
    board.txt          25             4.041             la bacheca degli incarichi

⭐ **E hanno la stessa forma di `lang()`**: ogni blocco esiste due volte,
marcato `%…,JP` e `%…,EN`, e il codice sceglie con `lang("JP", "EN")`. C'e' un
giapponese da cui leggere e un inglese da riscrivere: e' il mestiere della
catena, su un formato che gli strumenti non conoscevano.

⚠️ **Ma la riga non vuol dire la stessa cosa nei cinque file**, e il conto lo
dimostra: `book.txt` ha blocchi da 33 righe giapponesi contro **224** inglesi,
`exhelp.txt` 7 contro 20. Li' l'inglese e' **spezzato a mano a larghezza fissa**
e la riga e' un'unita' di **disegno**; in `board.txt` e `talk.txt` e' un'unita'
di **senso**, e il gioco ne pesca una a caso con `rnd`. Questa fase ha aperto la
famiglia facile. Il piano sta in `piani/2026-08-20-fase-3-file-dati.md`.

### ▶ ⭐⭐ Come arriva in gioco: la disciplina di `cgx-test.exe`

Il nome del file dati e' un letterale nudo, fuori da ogni `lang()`. Le toppe
**1007a-1009a** lo cambiano in `board_it.txt` / `talk_it.txt`, e il file
italiano si posa **accanto** a quello di monte invece che al posto suo:
l'eseguibile inglese continua a girare col suo file, e il riferimento pulito
resta sul disco.

⚠️ **E la toppa non cambia solo un nome: mette un ramo `exist` col ripiego.**
La riga di monte fa `noteload` senza guardia, e un `noteload` su un file assente
e' un **errore di esecuzione**: senza ripiego, chi copiasse l'eseguibile senza i
file dati non vedrebbe una bacheca inglese, vedrebbe il gioco morire all'avvio.
L'idioma `exist` + `strsize != (-1)` e' quello che `custom_autopick.hsp` usa
gia' per i propri file.

⚠️ **Due trappole d'ordine chiuse mentre le si trovava:** `applica.py` fa
`rmtree(BUILD)`, quindi un `dati_applica` lanciato prima sarebbe stato
cancellato senza un rumore — i file dati adesso si costruiscono **dentro**
`applica`, perche' e' lo stesso giro che applica la toppa; e i due sono la
stessa consegna.

### ▶ ⭐⭐ La prova d'identita' dei file dati

Un dizionario che traduce ogni riga in se' stessa deve riprodurre il file **byte
per byte**: **2.987 righe** su quattro file, CRLF compresi. E' la stessa
verifica che sugli `.hsp` ha trovato i due difetti peggiori del progetto mentre
83 test erano verdi, ed e' la dodicesima verifica d'apertura.

⭐ Il round-trip si tiene **senza rami che possano sbagliare**: il documento
tiene le righe con `splitlines(keepends=True)`, quindi `"".join(righe)` *e'* il
testo di partenza per costruzione — CRLF, LF misti, file senza a-capo finale. La
lezione della 65a messa dove non si puo' dimenticare invece che in un controllo.

### ▶ ⚠️ Il genere di CHI PARLA, che l'inglese non marca mai

Il cliente della bacheca e' un **PNG a caso**, e il suo nome sta stampato
accanto al testo (`command.hsp:3363`). Ogni predicato nominale in prima persona
porta il genere in italiano: tre rese su venticinque lo facevano — «Faccio **il
cuoco**», «**Pazzo** per la pasta», «da **solo** non ce la faccio» — e sono state
girate. E' la lezione della 58a spostata dal **destinatario** al **parlante**.

⚠️ E la sintassi l'hanno decisa due misure: `mapname()` **non e' omogeneo**
(le citta' sono nude — `Vernis`, `Yowyn`, `Palmia` — ma i luoghi portano
l'articolo: `la Torre Rovente`, `il Castello Antico`, `il Vuoto`), e
`{objective}` di `HUNTEX`/`CONQUER` e' un **nome di creatura**, che per
`contratto-nomi.md` §4 l'articolo ce l'ha sempre. \U0001f4a1 La via d'uscita e' la 64a
applicata alla preposizione: **«verso» e «per» non si fondono con l'articolo**,
e il complemento oggetto nudo nemmeno; dove serviva un genitivo si e' usata
l'apposizione col due punti — «abita qui: {map}» — che `map.hsp:891` gia' usava.

### ▶ Quel che resta da guardare, in ordine

1. ⭐⭐⭐ **Le 64 rese di `talk.txt` non sono state viste a schermo.** La
   bacheca si', il parlato dei cittadini no.
2. ⭐⭐⭐ Il debito che viene da prima e non e' rientrato: le **243 rese della
   69a** (di cui si e' visto un nome di oggetto), la toppa degli stati del nome
   (` (marcio)`, ` (campione)`) **mai riprovata**, le nove rese di
   `scheda-inglesi` della 68a e le **308 di `chat.hsp`** della 67a.
3. ⭐⭐⭐ **Le colonne della scheda che si sovrappongono** (68a): «Classe» e
   «Guerriero» una sopra l'altra, «Altezza157 cm», «Velocita70(70)». Nessuna
   rete guarda questa famiglia. ⚠️ E adesso si sa **perche'** serve: e' la
   stessa forma del tetto sbagliato di oggi.
4. ⭐⭐ Il **registro dei messaggi**: `You displace Azilarg la guardia.` visto in
   gioco, accanto a «Ti scambi di posto con \\<Gwen\\> l'innocente» — la stessa
   azione con due rese, una fatta e una no.
5. ⭐⭐ La toppa dei trascorsi, `talk_conv s, 32` → **36**. ⚠️ E c'e' un motivo
   in piu': `righe_a_capo` ha misurato che **una parola piu' lunga del tetto fa
   mandare a capo mille volte** (difetto di monte, `init.hsp:1326`). A 70 non si
   raggiunge, a 32 forse si': va provato al banco.
6. ⭐ Le 55 intestazioni «senza ostacolo a destra» della rete 20.

### ▶ Quel che resta aperto

1. ⭐⭐⭐ `talk.txt`: **505** righe da fare. Chiusi: `DEFAULT`,
   `PERSONALITY,0`-`,3`. \U0001f4a1 Un inglese ripetuto aspetta la propagazione: «I'm so
   bored!» e' reso «Che noia mortale!» in `DEFAULT,9`.
2. ⭐⭐⭐ `board.txt` **secondo lotto**: le 38 varianti giapponesi che monte ha
   buttato via. Serve estendere `dati_applica` ad **aggiungere** righe, non solo
   a sostituirle — e la prova d'identita' deve continuare a valere.
3. ⭐⭐ La **famiglia dell'impaginazione**: `book.txt` (2.208 righe),
   `manual_ENG.txt` (591), `exhelp.txt` (185). ⚠️ `help.hsp:273` disegna con
   `gmes` a larghezza 330 px e conta **dieci righe di FILE per pagina**: una
   resa piu' lunga sposta le pagine. Vuole il suo giro di progetto.
4. ⭐⭐ `autopick.txt` e `custom_autopick.hsp`: **78 delle 90 `lang()` sono
   confronti** dentro `instr`, contro il file che il **giocatore scrive**. E il
   muro della 69a al terzo giro: `" cursed "`, `" blessed "`, `" rotten "` sono
   aggettivi che servono ogni nome. \U0001f4a1 La via d'uscita esiste ed e' misurata:
   `custom_autopick.hsp:358` cerca il residuo dentro `cnvitemname()`, quindi
   **l'ordine delle parole e' libero** e la chiave puo' essere un'etichetta
   invariabile. ⚠️ E `autopick.txt` e' scritto in **UTF-8**, non in CP932 come
   gli altri sei: il suo blocco di documentazione giapponese e' mojibake **anche
   in gioco**.
5. ⭐⭐⭐ `chat.hsp`: **4.046** da fare.
6. ⭐⭐ **Dodici file con `lang()` e senza dizionario**, per **567** `lang()`:
   `txtadv.hsp` 170, `material_data.hsp` 118, `custom_autopick.hsp` 90,
   `help.hsp` 52, `net.hsp` 37, `custom_itemenchantment.hsp` 31, `quest.hsp` 26,
   `material.hsp` 19.
7. ⭐⭐ Il **muro del materiale**: `mithril sword` in italiano e' «spada **di**
   mithril», postposta. 118 righe piu' i tre siti di `item_func.hsp`.
8. ⭐ Le 93 di `command.hsp`, le 98 di `screen.hsp`, le 41 di `system.hsp`, le
   622 di `event.hsp`, le 241 di `item_func.hsp`; i 1.146 di `db_card.hsp`.

### ▶ Il collaudo

Fatto, e ha fruttato subito. Il gioco pilotato con `collaudo/schermo.ps1` fino a
Yowyn; salvataggi copiati prima in
`save-backup\\pre-collaudo-20260820-70a` (390 file).

⚠️ **I tasti del tastierino non muovono il personaggio** in questa
configurazione (il gioco risponde «Premi ? per vedere l'elenco dei comandi»):
funzionano le **frecce**. Il docstring di `schermo.ps1` dice «4/6/8/2 ma anche
le frecce»: e' il contrario, e chi piloterebbe perderebbe un giro a scoprirlo.

✅ Visto e misurato: il riquadro delle condizioni d'uso, «Quale avventura vuoi
riprendere?», «Scelta dell'avventuriero», la bacheca di Yowyn con titolo, corpo
mandato a capo, `{ref}` espanso in «131 punti» e il nome del cliente.

### ▶ Come si e' chiusa

⚠️⚠️ **La sessione si chiude annunciando un CAMBIO DI TERMINALE.** E' la
tredicesima volta; tutte le volte verificate finora la sessione dopo si e'
riaperta sulla **stessa** macchina, `DESKTOP-1O339MR`.

⚠️⚠️ Se questa volta e' davvero un'altra macchina, le cose che **non stanno
nel repo** sono adesso **cinque**:

    i tre CSV degli epiteti    python scratchpad/epiteti_vocabolario.py   (vogliono i CRLF)
    cgx-test.exe               python -m strumenti.compila --eseguibile
    l'albero di build          python -m strumenti.applica
    dati-sorgente\\            python -m strumenti.dati_sorgente --pinna   <- NUOVO
    data\\board_it.txt e talk_it.txt   li scrive `applica` in build\\dati\\, poi si copiano

⚠️ L'ordine conta: prima `dati_sorgente --pinna` (senza la copia pinnata
`applica` si ferma), poi `applica`, poi — **non incatenato** —
`compila --eseguibile`. E vale [[elona-ambiente-python]]: serve un Python 3.10+.
\U0001f4a1 Da questa shell `strumenti.battute` vuole `PYTHONIOENCODING=utf-8` davanti, o
muore di `UnicodeEncodeError`.

---

"""

AVANZAMENTO_NUOVO = """
## Fase 3 — i file dati di `data\\` (dalla 70a)

L'unita' e' la **riga inglese** dentro un blocco `%…,EN`. Il conto vivo:

```powershell
python -m strumenti.dati_verifica lavoro/<file>-001.jsonl
```

| file | tradotte | righe EN | % | famiglia |
|---|---|---|---|---|
| `board.txt` | **25** | 25 | **100%** | senso |
| `talk.txt` | **64** | 569 | 11% | senso |
| `exhelp.txt` | 0 | 185 | 0% | impaginazione |
| `manual_ENG.txt` | 0 | 591 | 0% | impaginazione |
| `book.txt` | 0 | 2.208 | 0% | impaginazione |
| **totale** | **89** | **3.578** | **2%** | |

⚠️ **La famiglia decide l'unita' di traduzione.** Dove la riga e' un'unita' di
**senso** il gioco ne pesca una a caso (`rnd`) e si traduce riga per riga; dove
e' un'unita' di **disegno** l'inglese e' spezzato a mano a larghezza fissa
(`book.txt`: 33 righe giapponesi contro 224 inglesi) e l'unita' e' il blocco.

⚠️ **E ogni file ha il suo espansore di segnaposto**: `board.txt` passa da
`*talktxt_conv` (33 nomi), `talk.txt` da `*convert_word` (46). Stanno in
`PROFILI`, dentro `strumenti/dati_verifica.py`.

Blocchi di `talk.txt` chiusi: `DEFAULT`, `PERSONALITY,0`-`,3`.
"""


def main() -> None:
    testo = RIPRESA.read_text(encoding="utf-8")
    segno = "## La sessantanovesima sessione"
    taglio = testo.index(segno)
    coda = testo[taglio:].replace(segno, segno + " (per storia)", 1)
    RIPRESA.write_text(TESTA + coda, encoding="utf-8")
    print("RIPRESA riscritta:", len(TESTA + coda), "caratteri")

    avanzamento = AVANZAMENTO.read_text(encoding="utf-8")
    if "## Fase 3 — i file dati" not in avanzamento:
        AVANZAMENTO.write_text(avanzamento.rstrip() + "\n\n" + AVANZAMENTO_NUOVO,
                               encoding="utf-8")
        print("avanzamento aggiornato")


if __name__ == "__main__":
    main()
