# scratchpad/_100-commento-barre.py
"""La QUINTA famiglia di riga morta: il commento di riga `//`.

`commenti.py` conosce il commento di blocco `/* ... */` e si ferma sul `;`,
che e' il commento di riga che il progetto ha sempre guardato. Ma HSP3 accetta
**anche** `//`, e il sorgente lo usa: `custom_autopick.hsp:200`-`:217` tiene
spenti cosi' due selettori interi (` zombie ` e ` dragon's `), che `estrai` ha
estratto come se fossero vivi.

Il conto e' sulla **riga**, non sul blocco: `//` spegne fino a fine riga.
⚠️ Le due barre si cercano **fuori dalle stringhe** — `"http://..."` non e' un
commento — e fuori dai commenti di blocco, che `commenti.py` gia' copre.

    python scratchpad/_100-commento-barre.py

Atteso: le righe con una `lang()` dopo un `//`, e quante di quelle siano gia'
state **tradotte** — cioe' lavoro speso su testo che il giocatore non legge.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti import commenti, percorsi


colonna_barre = commenti.colonna_commento_riga   # la regola sta nello strumento


def rese_per_file() -> dict[str, set[int]]:
    """Le righe che il dizionario ha gia' reso, per file."""
    reso: dict[str, set[int]] = {}
    for percorso in sorted(percorsi.DIZIONARIO.glob("*.jsonl")):
        righe = set()
        for testo in percorso.read_text(encoding="utf-8").splitlines():
            if not testo.strip():
                continue
            voce = json.loads(testo)
            if voce.get("it"):
                righe.add(voce["riga"])
        reso[percorso.stem] = righe
    return reso


def main() -> None:
    reso = rese_per_file()
    totale = totale_rese = 0
    for percorso in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
        in_blocco = commenti.righe_in_commento(percorso)
        righe = percorso.read_bytes().decode("cp932", "replace").split("\r\n")
        trovate: list[tuple[int, str, bool]] = []
        for numero, riga in enumerate(righe, 1):
            if numero in in_blocco:
                continue          # gia' materia di commenti.py: non si conta due volte
            colonna = colonna_barre(riga)
            if colonna is None:
                continue
            coda = riga[colonna:]
            if "lang(" not in coda:
                continue
            gia = numero in reso.get(percorso.name, set())
            trovate.append((numero, riga.strip()[:96], gia))
        if not trovate:
            continue
        quante_rese = sum(1 for _, _, g in trovate if g)
        totale += len(trovate)
        totale_rese += quante_rese
        marchio = "  ⚠️ GIA' RESE" if quante_rese else ""
        print(f"{percorso.name:30} {len(trovate):3} righe, {quante_rese} gia' rese{marchio}")
        for numero, testo, gia in trovate:
            print(f"    {'⚠️' if gia else '  '} :{numero:<6} {testo}")

    print(f"\nrighe con lang() spente da `//`: {totale}   di cui gia' rese: {totale_rese}")
    print("⚠️ Se «gia' rese» sale sopra 0, un lotto ha speso lavoro su testo morto.")


if __name__ == "__main__":
    main()
