"""Le grafie inglesi rimaste dentro le rese italiane, e la loro correzione.

Tocca **solo** il campo `it` dei dizionari: `en` e `jp` sono il monte.

Le quattro grafie qui sotto non sono gusti miei: ognuna porta il conto che l'ha
decisa, misurato sul dizionario il 2026-09-03. La regola e' quella del
progetto dalla 79a -- **dove l'inglese di monte e' incoerente si segue il
giapponese** -- applicata a nomi propri invece che a prosa.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_133-grafie.py [--scrivi]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from strumenti import scene

DIZIONARIO = Path("dizionario")


def main() -> int:
    scrivi = "--scrivi" in sys.argv
    totale = 0
    for percorso in sorted(DIZIONARIO.rglob("*.jsonl")):
        voci = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines()
                if r.strip()]
        toccate = 0
        for voce in voci:
            reso = voce.get("it")
            if not isinstance(reso, str) or not reso:
                continue
            nuovo = reso
            for inglese, italiano in scene.GRAFIE.items():
                nuovo = nuovo.replace(inglese, italiano)
            if nuovo == reso:
                continue
            voce["it"] = nuovo
            toccate += 1
            print("%s riga %s" % (percorso.stem, voce.get("riga")))
            print("    - %s" % reso[:150])
            print("    + %s" % nuovo[:150])
        if toccate and scrivi:
            percorso.write_text(
                "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in voci),
                encoding="utf-8")
            print("  scritto %s (%d rese)" % (percorso, toccate))
        totale += toccate

    print("\nrese con una grafia inglese dentro: %d" % totale)
    if not scrivi:
        print("(prova a vuoto: aggiungi --scrivi)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
