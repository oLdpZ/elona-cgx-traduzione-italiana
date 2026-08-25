# -*- coding: utf-8 -*-
"""Ritaglia un lotto di `book.txt` sui blocchi che si stanno traducendo.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_99-lotto-book.py \
        lavoro/book-002.jsonl 9 27 31

⚠️⚠️ **Serve perche' `dati_reimporta` fonde per firma e sovrascrive**: un lotto
estratto dall'intero file porta `it: ""` su tutte le righe, e promuoverlo
**cancellerebbe** le rese gia' nel dizionario (le 224 del `%1` della 98a). Il
lotto quindi contiene **solo** i blocchi in lavorazione.

Le rese gia' presenti nel dizionario per quei blocchi vengono riportate nel
lotto, cosi' che un secondo giro sullo stesso blocco non le perda.
"""
import io
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def main(destinazione, blocchi):
    blocchi = set(blocchi)
    with tempfile.TemporaryDirectory() as tmp:
        intero = Path(tmp) / "book-intero.jsonl"
        subprocess.run(
            [sys.executable, "-m", "strumenti.dati_estrai", "book.txt",
             "--lotto", str(intero)],
            check=True, stdout=subprocess.DEVNULL)
        voci = [json.loads(r) for r in
                io.open(intero, encoding="utf-8") if r.strip()]

    gia = {}
    dizionario = Path("dizionario/dati/book.txt.jsonl")
    if dizionario.exists():
        for riga in io.open(dizionario, encoding="utf-8"):
            if riga.strip():
                vecchia = json.loads(riga)
                if vecchia["it"]:
                    gia[vecchia["firma"]] = vecchia["it"]

    scelte = [v for v in voci if v["blocco"] in blocchi]
    mancanti = blocchi - {v["blocco"] for v in scelte}
    if mancanti:
        raise SystemExit(f"blocchi che non esistono: {sorted(mancanti)}")

    riportate = 0
    for voce in scelte:
        if voce["firma"] in gia:
            voce["it"] = gia[voce["firma"]]
            riportate += 1

    percorso = Path(destinazione)
    percorso.parent.mkdir(parents=True, exist_ok=True)
    with io.open(percorso, "w", encoding="utf-8", newline="\n") as f:
        for voce in scelte:
            f.write(json.dumps(voce, ensure_ascii=False) + "\n")

    print(f"{percorso}: {len(scelte)} righe in {len(blocchi)} blocchi "
          f"(%{', %'.join(sorted(blocchi, key=int))}); "
          f"rese riportate dal dizionario: {riportate}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
