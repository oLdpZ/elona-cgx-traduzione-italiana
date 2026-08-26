# -*- coding: utf-8 -*-
"""RETE: la geometria di `book.txt`, cioe' le due pagine aperte di un libro.

    python scratchpad/_98-book-mes.py            # la build (book_it.txt)
    python scratchpad/_98-book-mes.py --monte    # l'inglese di monte, per taratura

⚠️⚠️ **QUI NON C'E' NESSUN A CAPO, E QUESTO CAMBIA TUTTO.** `board.txt` e
`talk.txt` passano da `talk_conv`, `exhelp.txt` da `gmes`: tutt'e tre, a modo
loro, mandano a capo da soli. `command.hsp:8412` invece fa `mes s` e basta. Una
riga troppo lunga non va a capo e non si accorcia: **entra nella colonna
accanto**, e se e' nella colonna di destra esce dalla pagina.

    x = wx + 80 + cnt / 20 * 306      command.hsp:8399
    y = wy + 45 + cnt \\ 20 * 16       command.hsp:8400
    pagesize = 40                     command.hsp:8380   20 righe per colonna

Le due colonne distano **306 px**, e il passo del carattere e' **7 px**: e' lo
stesso `font ..., 12 + sizefix - en * 2` della scheda del personaggio
(`command.hsp:10492` contro `:8409`, espressione identica), dove il passo e'
misurato sulle schermate del collaudo della 72a. Vedi `strumenti/gronde.py`.
Quindi il tetto e' **306 / 7 = 43 caratteri**.

⚠️ **Il tetto geometrico e quello del corpus NON coincidono, e qui va detto.**
Su `exhelp.txt` i due numeri erano lo stesso (6 righe) e il tetto non era una
stima; qui la geometria dice 43 e l'inglese di monte si ferma a **39**. Il
tetto vero e' 43 — e' li' che il testo sfonda — ma fra 40 e 43 si sta in un
margine che monte non ha mai usato, quindi la rete le stampa a parte invece di
tacere. E' la forma di `linguette.py`: «fuori misura» e «strette ma dentro».

💡 **L'altezza qui non e' un problema**, al contrario di `exhelp.txt`:
`page_change` impagina da solo, e `dati_applica` **sostituisce** righe senza
aggiungerne, quindi il conto delle righe di un libro non puo' cambiare.

⚠️⚠️ **E c'e' un pezzo che questa rete NON guarda, ed e' giusto cosi': i 33
titoli del blocco `%DEFINE`.** `item.hsp:121` li legge dalla CSV con
`booktitle(int(s)) = lang(s(1), s(2))`, colonna 3, e non finiscono nella pagina
del libro: `item_func.hsp:907` li incolla al **nome dell'oggetto** (« dal titolo
<...>»), dove questa colonna da 306 px non c'entra niente. Misurarli col metro
del corpo sarebbe una rete giusta puntata sul posto sbagliato, che non tace: mente.

⭐ Dalla 101a i titoli **sono tradotti**: `dati.COLONNE_CSV` insegna alla catena
che quel blocco e' una CSV e che l'unita' e' una colonna. Il conto si stampa lo
stesso qui sotto, perche' e' la riga che ricorda che sono due cose diverse.
"""
import argparse
import io
import os
import re
import sys

PASSO = 7                      # px per carattere, gronde.py
COLONNA = 306                  # command.hsp:8399
TETTO = COLONNA // PASSO       # 43
TETTO_CORPUS = 39              # il piu' lungo dell'inglese di monte
RIGHE_PER_COLONNA = 20         # command.hsp:8400

BUILD = r"C:\Games\Elona\_traduzione\build\dati\book_it.txt"
MONTE = r"C:\Games\Elona\_traduzione\dati-sorgente\book.txt"

def blocchi(percorso):
    """(blocco, [righe]) della sezione EN, righe piene, nell'ordine di `noteget`.

    ⚠️⚠️ **SI USA `strumenti.dati`, NON UN PARSER SCRITTO QUI.** Il primo giro
    di questa rete ne aveva uno suo, copiato da quello di `exhelp.txt`, che
    trattava una riga iniziata per `#` come un commento. In `exhelp.txt` lo e'
    (`#####...` separa i blocchi); in `book.txt` **e' testo**: il diario di
    `%21` nomina i detenuti `#14` e `#16`. La rete non perdeva soltanto quelle
    due righe — chiudeva il blocco e **si mangiava le 62 successive** senza
    dirlo, e il conto tornava 2.146 invece di 2.208.

    Il parser del progetto e' uno solo, ed e' quello che ha prodotto il lotto:
    una rete che se ne scrive un secondo puo' dissentire dallo strumento che
    misura, e quando dissente non tace.
    """
    from strumenti import dati

    testo = io.open(percorso, encoding="cp932", errors="replace").read()
    documento = dati.analizza(testo)
    uscita = []
    for blocco in documento.blocchi:
        if blocco.lingua != "EN":
            continue
        righe = [documento.riga(i) for i in blocco.indici_pieni()]
        if righe:
            uscita.append((blocco.chiave, righe))
    return uscita


def titoli(percorso):
    """Le righe del blocco %DEFINE: (numero, titolo giapponese, titolo inglese)."""
    testo = io.open(percorso, encoding="cp932", errors="replace").read()
    dentro, uscita = False, []
    for grezza in testo.split("\n"):
        secca = grezza.rstrip("\r").strip()
        if secca.startswith("%DEFINE"):
            dentro = True
            continue
        if dentro and secca.startswith("%END"):
            break
        if dentro and secca and not secca.startswith(("/", "#")):
            pezzi = [p.strip() for p in secca.split(",")]
            if len(pezzi) >= 3:
                uscita.append((pezzi[0], pezzi[1], pezzi[2]))
    return uscita


def main():
    parla = argparse.ArgumentParser(description=__doc__)
    parla.add_argument("--monte", action="store_true",
                       help="misura l'inglese di monte invece della build")
    parla.add_argument("--file", help="un file qualsiasi, per provare la rete al contrario")
    scelte = parla.parse_args()

    percorso = scelte.file or (MONTE if scelte.monte else BUILD)
    if not os.path.exists(percorso):
        raise SystemExit(f"{percorso} non c'e': costruisci con "
                         "`python -m strumenti.dati_applica`")

    fuori, strette = [], []
    quante = massima = 0
    for blocco, righe in blocchi(percorso):
        for numero, riga in enumerate(righe, 1):
            larga = len(riga)
            quante += 1
            massima = max(massima, larga)
            colonna = (numero - 1) // RIGHE_PER_COLONNA % 2
            if larga > TETTO:
                fuori.append((blocco, numero, larga, colonna, riga))
            elif larga > TETTO_CORPUS:
                strette.append((blocco, numero, larga, riga))

    print(f"file: {percorso}")
    for blocco, numero, larga, colonna, riga in fuori:
        dove = "esce dalla pagina" if colonna else "entra nella colonna accanto"
        print(f"  FUORI   %{blocco} riga {numero}: {larga} caratteri, tetto {TETTO} "
              f"({dove}) — {riga!r}")
    for blocco, numero, larga, riga in strette:
        print(f"  stretta %{blocco} riga {numero}: {larga} caratteri — monte non "
              f"passa mai {TETTO_CORPUS} — {riga!r}")

    print(f"\nrighe fuori misura: {len(fuori)} su {quante} misurate   (atteso: 0)")
    print(f"strette ma dentro (da {TETTO_CORPUS + 1} a {TETTO}): {len(strette)}")
    print(f"la piu' larga misura {massima} caratteri su {TETTO} di colonna")

    dei_titoli = titoli(percorso if not scelte.file else MONTE)
    print(f"\n⚠️ e i {len(dei_titoli)} titoli del blocco %DEFINE non sono in questo "
          "conto, e non ci vanno: non stanno nella pagina del libro ma nel nome "
          "dell'oggetto (item_func.hsp:907)")
    return 1 if fuori else 0


if __name__ == "__main__":
    sys.exit(main())
