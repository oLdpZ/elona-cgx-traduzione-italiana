"""«Ylva» nelle rese di `scene2.hsp` doveva essere «Irva».

L'inglese di monte scrive `Ylva`; il progetto rende イルヴァ **«Irva»** in
1.058 punti (`db_item` 266, `chat` 34, `db_card` 27...). Le rese della 132a
sono le uniche due che hanno lasciato in italiano la grafia inglese, e senza
questo comando le avrei imitate lotto dopo lotto -- che e' il modo in cui un
difetto di una sessione diventa una convenzione.

Tocca **solo** il campo `it` del dizionario delle scene: `en` e `jp` sono il
monte e non si riscrivono. Dopo, `scene --referto` rivalida tutto.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_133-irva.py [--scrivi]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

DIZIONARIO = Path("dizionario/scene2.hsp.jsonl")


def main() -> int:
    scrivi = "--scrivi" in sys.argv
    voci = [json.loads(r) for r in DIZIONARIO.read_text(encoding="utf-8").splitlines()
            if r.strip()]
    toccate = 0
    for voce in voci:
        reso = voce.get("it") or ""
        if "Ylva" not in reso:
            continue
        voce["it"] = reso.replace("Ylva", "Irva")
        toccate += 1
        print("scena %s blocco %s (%s)" % (voce["scena"], voce["blocco"], voce["tipo"]))
        for riga in voce["it"].split("\n"):
            if "Irva" in riga:
                print("    %s" % riga)

    print("\nrese toccate: %d" % toccate)
    if scrivi and toccate:
        DIZIONARIO.write_text(
            "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in voci),
            encoding="utf-8")
        print("scritto %s -- ora `scene --referto`" % DIZIONARIO)
    elif not scrivi:
        print("(prova a vuoto: aggiungi --scrivi)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
