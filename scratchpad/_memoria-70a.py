"""Aggiorna i file di memoria del progetto con quel che ha insegnato la 70a."""
from pathlib import Path

MEM = Path(r"C:\Users\old_p\.claude\projects\C--Games-Elona\memory")

DUE_MACCHINE = """
⚠️⚠️⚠️ **E dalla 70a le cose che NON stanno nel repo sono CINQUE, non tre, e l'ordine conta.** Ai tre CSV degli epiteti, a `cgx-test.exe` e all'albero di build si aggiungono **`_traduzione\\dati-sorgente\\`** (la copia pinnata dei sette file di `elonaplus2.31\\data\\`, che `applica` pretende: senza si ferma) e i **file dati italiani** `data\\board_it.txt` e `data\\talk_it.txt`. L'ordine su una macchina nuova è: `python -m strumenti.dati_sorgente --pinna`, poi `python -m strumenti.applica`, poi — **non incatenato** — `python -m strumenti.compila --eseguibile`, poi le copie in `elonaplus2.31\\`. 💡 Nel vault c'è `dati/manifesto.json` con byte, md5 e **fine riga** dei sette file: serve proprio a verificare che l'altra macchina abbia gli stessi byte, e `python -m strumenti.dati_sorgente` lo dice in due secondi.

⭐⭐ **E nella 70a il collaudo l'ho fatto io con `collaudo/schermo.ps1`, ed è andato — con due correzioni al suo docstring.** ⚠️ **I tasti del tastierino (`NUM2`, `NUM8`…) NON muovono il personaggio**: il gioco risponde «Premi ? per vedere l'elenco dei comandi». Funzionano le **frecce**. Il docstring dice «4/6/8/2 ma anche le frecce»: è il contrario, e chi pilota perde un giro a scoprirlo. ⚠️ E il filtro va scritto `-Titolo "Elona\\+ Custom-GX"` (con la barra rovescia davanti al più, perché è una regex): `"Elona"` da solo pesca anche il terminale. 💡 Il giro costa poco: aprire il gioco, `ENTER` per il riquadro delle condizioni, la lettera del salvataggio, e poi le frecce. Da «Terra di Tregua» a una bacheca di città sono bastate sei frecce, perché il personaggio esce dalla mappa e attraversa il mondo da solo.
"""

CONVENZIONI = """
⚠️⚠️⚠️ **UNA RETE PUNTATA SUL FILE SBAGLIATO NON TACE: MENTE** (2026-08-20, 70ª). La rete dei segnaposto dei file dati è stata girata su `talk.txt` col profilo di `board.txt` e ha «trovato» sei `{nptc}`, che ho riportato a voce come refuso di monte. Non lo erano: **ogni file dati ha il suo espansore, e non conoscono gli stessi nomi** — `board.txt` passa da `*talktxt_conv` (`text.hsp:11922`, 33 nomi), `talk.txt` da `*convert_word` (`text.hsp:6900`, **46**, fra cui `nptc`, `npcc` e diciannove codici di faccia e di suono). È la domanda della 53ª — *finito per quale referto?* — nella forma **«misurato con quale rete?»**, ed è peggiore dell'originale: un referto sbagliato non si distingue da un reperto. 💡 Prima di credere a un elenco di difetti, si guarda **da dove viene il metro**, non solo che numero dà. Adesso c'è `PROFILI` in `strumenti/dati_verifica.py`.

⚠️⚠️ **E l'ostacolo di un tetto NON è il `pos` che viene dopo leggendo il sorgente** (70ª, la seconda volta dopo la 68ª). Il tetto del titolo di un incarico era stato messo a 34 prendendo la scadenza a `wx + 344`, il primo `pos` successivo nel testo; ma `command.hsp:3391` disegna le **stellette del livello** a `wx + 270` — più a sinistra, e **dopo** il titolo, quindi ci passa sopra. Tetto vero **24**. L'ha trovato il collaudo misurando i pixel: testo a 781 (`wx = 681`), stellette a 951, scadenza a 1027, cliente a 1073. 💡 *Una cosa disegnata dopo copre quel che c'era prima, e l'ordine di lettura del sorgente non dice qual è la più a sinistra.* ⭐ E i 7 px per carattere a corpo 12 si sono confermati sulla schermata stessa: «Si fa festa!», dodici caratteri, finiva a 865 = 781 + 12×7.

⚠️⚠️ **Il genere di chi PARLA, non solo di chi ascolta** (70ª). Il cliente della bacheca degli incarichi è un PNG estratto a caso, e il suo nome sta stampato accanto al testo (`command.hsp:3363`): ogni predicato nominale in prima persona porta il genere in italiano e l'inglese non lo marca mai. Tre rese su venticinque lo facevano — «Faccio **il cuoco**», «**Pazzo** per la pasta», «da **solo** non ce la faccio» — e sono state girate in forme che non si accordano. È la lezione della 58ª spostata dal **destinatario** al **parlante**.

⭐⭐ **E c'è una via d'uscita in più per l'articolo: le preposizioni che non si fondono** (70ª). `mapname()` non è omogeneo — le città sono nude (`Vernis`, `Yowyn`, `Palmia`) ma i luoghi portano l'articolo (`la Torre Rovente`, `il Castello Antico`, `il Vuoto`) — e i nomi di creatura l'articolo ce l'hanno sempre (`contratto-nomi.md` §4). Quindi «a {map}» e «sottospecie di {objective}» reggono solo per fortuna. 💡 **«verso» e «per» non si fondono mai con l'articolo, e il complemento oggetto nudo nemmeno**: «verso Vernis» e «verso la Torre Rovente» stanno in piedi insieme. Dove serve un genitivo si usa l'apposizione col due punti — «abita qui: {map}», «la creatura è questa: {objective}» — che è la giuntura che `map.hsp:891` già usava per `mapname()`. È la 64ª applicata alla preposizione invece che all'aggettivo.
"""

PROGETTO = """
⭐⭐⭐ **Dalla 70ª c'è una seconda gamba: i file dati di `elonaplus2.31\\data\\`.** Cinque file (`book.txt`, `talk.txt`, `manual_ENG.txt`, `exhelp.txt`, `board.txt`) tengono **155.140 caratteri** di inglese che il giocatore legge e che nessuna rete guardava, perché ogni rete guarda le `lang()` degli `.hsp` e lì dentro di `lang()` non ce n'è nessuna. Hanno la stessa forma di `lang()`: ogni blocco esiste due volte, `%…,JP` e `%…,EN`, e il codice sceglie con `lang("JP", "EN")`.

La catena è parallela a quella degli `.hsp` e i moduli si chiamano uguale col prefisso: `dati.py` (il formato, round-trip **sui byte**), `dati_sorgente.py` (la copia pinnata e `dati/manifesto.json`), `dati_estrai.py`, `dati_verifica.py`, `dati_reimporta.py`, `dati_applica.py`. Il dizionario sta in `dizionario/dati/`, e `applica.py` costruisce i file dati **dentro** il suo giro (fa `rmtree(BUILD)`: uno costruito prima sparirebbe in silenzio).

⚠️ **La consegna è la disciplina di `cgx-test.exe`**: una toppa cambia il nome del file (`board_it.txt`, `talk_it.txt`) e l'italiano si posa **accanto** a quello di monte. E la toppa non cambia solo un nome: mette un ramo `exist` col ripiego, perché la riga di monte fa `noteload` **senza guardia** e un `noteload` su un file assente è un errore di esecuzione — cioè il gioco che muore all'avvio, non una bacheca inglese.

⚠️⚠️ **E la riga non vuol dire la stessa cosa nei cinque file.** Dove è un'unità di **senso** il gioco ne pesca una a caso con `rnd` e si traduce riga per riga (`board.txt`, `talk.txt`); dove è un'unità di **disegno** l'inglese è spezzato a mano a larghezza fissa e l'unità è il blocco (`book.txt` ha blocchi da 33 righe giapponesi contro **224** inglesi). Il conto delle righe per blocco è il modo per saperlo prima di cominciare. La famiglia dell'impaginazione è ancora tutta da fare.

La dodicesima verifica d'apertura è `python -m strumenti.dati_applica --identita` (atteso: 4 file, **2.987** righe, tutti ok).
"""


def aggiungi(nome: str, testo: str) -> None:
    percorso = MEM / nome
    corpo = percorso.read_text(encoding="utf-8")
    marchio = testo.strip().splitlines()[0][:60]
    if marchio in corpo:
        print(f"{nome}: gia' aggiornato")
        return
    percorso.write_text(corpo.rstrip() + "\n" + testo, encoding="utf-8")
    print(f"{nome}: +{len(testo)} caratteri")


def main() -> None:
    aggiungi("elona-due-macchine.md", DUE_MACCHINE)
    aggiungi("elona-convenzioni-traduzione.md", CONVENZIONI)
    aggiungi("elona-traduzione-italiana.md", PROGETTO)


if __name__ == "__main__":
    main()
