"""Mostra un pezzo del lotto in chiaro, per leggerlo e tradurlo.

    ... _133-mostra.py --scene 11          tutte le voci della scena 11
    ... _133-mostra.py --scene 8 --da 10   dalla decima voce in poi
    ... _133-mostra.py --attori            solo le etichette {actor_N}, con jp
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from strumenti import scene

LOTTO = Path("lavoro/scene2-7-30.jsonl")


def carica() -> list[dict]:
    return [json.loads(r) for r in LOTTO.read_text(encoding="utf-8").splitlines()
            if r.strip()]


def main() -> None:
    analizzatore = argparse.ArgumentParser()
    analizzatore.add_argument("--scene", nargs="*", default=None)
    analizzatore.add_argument("--da", type=int, default=0)
    analizzatore.add_argument("--attori", action="store_true")
    argomenti = analizzatore.parse_args()

    voci = carica()

    if argomenti.attori:
        conto: Counter[str] = Counter()
        esempio: dict[str, dict] = {}
        for voce in voci:
            if not voce["tipo"].startswith("actor"):
                continue
            conto[voce["en"]] += 1
            esempio.setdefault(voce["en"], voce)
        for etichetta, quante in conto.most_common():
            voce = esempio[etichetta]
            print(f"{quante:>3}x  {etichetta}")
            print(f"       jp: {voce['jp']}")
        return

    for voce in voci:
        if argomenti.scene and voce["scena"] not in argomenti.scene:
            continue
        if voce["blocco"] < argomenti.da:
            continue
        testa = (f"--- scena {voce['scena']} blocco {voce['blocco']} "
                 f"[{voce['tipo']}] riga {voce['riga']}")
        if voce["tipo"].startswith("chat"):
            righe = scene.righe_a_capo(voce["en"])
            testa += f"  {len(righe)}/{scene.SOFFITTO_CHAT} righe"
        print(testa)
        print(voce["en"])
        if voce.get("jp"):
            print(f"    jp: {voce['jp']}")
        print()


if __name__ == "__main__":
    main()
