"""Le toppe che fanno leggere book_it.txt, col ripiego su book.txt.

⚠️ **I siti sono DUE, e leggono due cose diverse dello stesso file.**

    item.hsp:112       il blocco %DEFINE, cioe' i 33 TITOLI dei libri
    command.hsp:8371   il corpo del libro aperto (*com_book)

Vanno toppati tutt'e due o il file si sdoppia: i titoli verrebbero da monte e le
pagine da noi. E vanno toppati **anche prima** che i titoli siano tradotti —
finche' il blocco %DEFINE di `book_it.txt` e' identico a quello di monte, il
sito di `item.hsp` legge le stesse identiche righe, e il giorno che i titoli si
traducono non c'e' una seconda toppa da ricordarsi.
"""
import json
from pathlib import Path

from strumenti import percorsi

RIGA = '\tnoteload exedir + "data\\\\book.txt"'
SITI = ("item.hsp", "command.hsp")

NUOVE = [
    '\texist exedir + "data\\\\book_it.txt"',
    '\tif ( strsize != (-1) ) {',
    '\t\tnoteload exedir + "data\\\\book_it.txt"',
    '\t}',
    '\telse {',
    '\t\tnoteload exedir + "data\\\\book.txt"',
    '\t}',
]

MOTIVO = (
    "Il nome del file dati e' un letterale nudo, fuori da ogni lang(): il dizionario "
    "non lo raggiunge. La toppa fa leggere book_it.txt, che applica costruisce in "
    "build\\dati\\ dal dizionario dei file dati (dizionario/dati/book.txt.jsonl). "
    "E' la quarta e la quinta della famiglia, dopo board.txt (init.hsp:2574), "
    "talk.txt (text.hsp) ed exhelp.txt (help.hsp:227). "
    "⚠️ I SITI SONO DUE E LEGGONO DUE COSE DIVERSE: item.hsp:112 prende il blocco "
    "%DEFINE, cioe' i 33 titoli dei libri (item.hsp:121, booktitle = lang(s(1), "
    "s(2)), colonna 3); command.hsp:8371 prende il corpo del libro aperto "
    "(*com_book). Toppato uno solo, il file si sdoppia: titoli da monte e pagine da "
    "noi. "
    "Il ramo `exist` non e' prudenza generica: la riga di monte fa noteload senza "
    "guardia, e un noteload su un file assente e' un errore di esecuzione. Qui il "
    "sito di item.hsp e' dentro *item_init, cioe' l'avvio: senza ripiego il gioco "
    "morirebbe prima del titolo, non al primo libro aperto. "
    "Vedi piani/2026-08-20-fase-3-file-dati.md e decisioni.md 98a."
)


def main() -> None:
    percorso = Path("toppe.jsonl")
    esistenti = [json.loads(r) for r in
                 percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    tenute = [t for t in esistenti if not (t["file"] in SITI and t["cerca"] == RIGA)]
    rimpiazzate = len(esistenti) - len(tenute)

    for nome in SITI:
        sorgente = (percorsi.SORGENTE_HSP / nome).read_bytes().decode("cp932").splitlines()
        quante = sorgente.count(RIGA)
        print(f"{nome}: la riga aggancia {quante} volte")
        if quante != 1:
            raise SystemExit(f"{nome}: la toppa deve agganciare esattamente una riga")
        tenute.append({"file": nome, "cerca": RIGA, "sostituisci": NUOVE, "motivo": MOTIVO})

    percorso.write_text(
        "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in tenute),
        encoding="utf-8", newline="\n")
    print(f"toppe: {len(tenute)} (rimpiazzate {rimpiazzate})")


if __name__ == "__main__":
    main()
