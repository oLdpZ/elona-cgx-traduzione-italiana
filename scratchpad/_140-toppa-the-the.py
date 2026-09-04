# -*- coding: utf-8 -*-
"""La toppa della 140ª su `tcg_custom.hsp:4565-:4566`: il nome della carta Novizio.

Scrive `lavoro/_140-toppa-the-the.jsonl`, da dare a `scratchpad/aggiungi-toppe.py`.

⚠️ Non e' una traduzione: e' una GIUNTURA. `", the "` unisce un nome proprio a un
titolo, e in italiano il titolo non regge l'articolo inglese. La regola c'e' gia',
ed e' dell'82ª: l'epiteto italiano e' un sintagma intero e senza articolo, e la
forma che tiene e' l'**apposizione** — `nome + ", " + titolo`.

⭐ Le due righe diventano una: `sreplace cardrefn, cardrefn, "the The", "the"` e'
la pulizia inglese di un articolo raddoppiato, e in italiano non c'e' niente da
raddoppiare. Verificato che i titoli italiani non portano articolo: nessuna delle
365 righe di `data/ndata-i.csv` — il file che la build carica al posto di
`ndata-e.csv` (`etc.hsp:335`) — comincia per «il », «la », «lo » o «the ».
"""
import io
import json
import pathlib

TOPPA = {
    "file": "tcg_custom.hsp",
    "cerca": [
        '\t\tcardrefn = "" + randomname() + ", the " + random_title()',
        '\t\tsreplace cardrefn, cardrefn, "the The", "the"',
    ],
    "sostituisci": [
        '\t\tcardrefn = "" + randomname() + ", " + random_title()',
    ],
    "motivo": (
        "tcg_custom.hsp:4565-:4566, il nome della carta Novizio. ⚠️ Non e' una "
        "resa, e' una GIUNTURA: `randomname() + \", the \" + random_title()` "
        "attacca un nome proprio a un titolo con l'articolo inglese, e il "
        "titolo italiano non lo regge. La regola e' dell'82a, presa su "
        "`chat.hsp:16472`, l'unica altra riga del progetto che concatena "
        "epiteto e nome: l'epiteto italiano e' un sintagma intero e senza "
        "articolo, e la forma che tiene e' l'APPOSIZIONE — «Zaine, principe». "
        "⭐ E le due righe diventano una: `sreplace ..., \"the The\", \"the\"` "
        "e' la pulizia inglese di un articolo raddoppiato, e in italiano non "
        "c'e' niente da raddoppiare. ✅ Verificato che nessuno dei 365 titoli "
        "di `data/ndata-i.csv` — il file che la build carica al posto di "
        "`ndata-e.csv`, `etc.hsp:335` — comincia per «il », «la », «lo » o "
        "«the »: la giuntura non puo' ricreare il doppione che quella riga "
        "toglieva. ⚠️ `random_title()` e' lo stesso che scrive gli epiteti di "
        "`cdatan(CDATAN_AKA, ...)` in tutto il gioco, quindi la carta dice "
        "adesso quel che dice la scheda."
    ),
}


def main() -> None:
    fuori = pathlib.Path("lavoro/_140-toppa-the-the.jsonl")
    fuori.parent.mkdir(exist_ok=True)
    with io.open(fuori, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(TOPPA, ensure_ascii=False) + "\n")
    print("scritta %s" % fuori)


if __name__ == "__main__":
    main()
