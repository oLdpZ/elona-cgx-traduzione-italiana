# strumenti/dati_reimporta.py
"""Promuove un lotto tradotto a dizionario dei file dati.

Il lotto e il dizionario hanno la **stessa forma**: promuovere e' fondere per
firma. Quel che questo passo aggiunge non e' una conversione, e' il **rifiuto**
— un lotto con problemi non entra, perche' al dizionario, che e' la sorgente di
verita' del progetto, ci si arriva solo passando dalle reti.

    python -m strumenti.dati_reimporta lavoro/board-001.jsonl
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from strumenti import dati_verifica, percorsi, verifica


def reimporta(voci: list[dict], destinazione: Path, tetto_a_capo: int = 70,
              invariati: set[str] | None = None) -> int:
    # ⚠️ Gli invariati dichiarati valgono anche qui. Fino alla 99a questa
    # chiamata non li passava, e la catena dei file dati era l'unica del
    # progetto a non vedere `invariati.md`: `%26` di `book.txt` — gli appunti
    # di stregoneria — ha per titoletti `Mana` e `MP`, che in italiano si
    # scrivono uguali e che `invariati.md` dichiara **gia'** (riga 76).
    # Il lotto veniva rifiutato per una resa giusta.
    if invariati is None:
        invariati = verifica.carica_invariati()
    problemi = dati_verifica.controlla(voci, invariati=invariati,
                                       tetto_a_capo=tetto_a_capo)
    if problemi:
        for problema in problemi:
            print(problema)
        raise SystemExit(f"{len(problemi)} problemi: il lotto non entra nel dizionario")

    dizionario: dict[str, dict] = {}
    if destinazione.exists():
        for riga in destinazione.read_text(encoding="utf-8").splitlines():
            if riga.strip():
                vecchia = json.loads(riga)
                dizionario[vecchia["firma"]] = vecchia
    for voce in voci:
        dizionario[voce["firma"]] = voce

    ordinate = sorted(dizionario.values(), key=lambda v: (v["blocco"], v["riga"]))
    destinazione.parent.mkdir(parents=True, exist_ok=True)
    destinazione.write_text(
        "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in ordinate),
        encoding="utf-8")
    return len(voci)


def main() -> None:
    analizzatore = argparse.ArgumentParser(
        description="Promuove un lotto di file dati a dizionario.")
    analizzatore.add_argument("lotto", help="percorso del lotto JSONL tradotto")
    analizzatore.add_argument("--tetto", type=int, default=70,
                              help="larghezza a cui il gioco manda a capo il corpo")
    argomenti = analizzatore.parse_args()

    voci = [json.loads(r) for r in
            Path(argomenti.lotto).read_text(encoding="utf-8").splitlines() if r.strip()]
    if not voci:
        raise SystemExit("lotto vuoto")

    nomi = {v["file"] for v in voci}
    if len(nomi) != 1:
        raise SystemExit(f"il lotto nomina piu' file: {sorted(nomi)}")
    nome_file = nomi.pop()

    destinazione = percorsi.DIZIONARIO / "dati" / f"{nome_file}.jsonl"
    quante = reimporta(voci, destinazione, argomenti.tetto)
    print(f"{quante} voci -> {destinazione}")


if __name__ == "__main__":
    main()
