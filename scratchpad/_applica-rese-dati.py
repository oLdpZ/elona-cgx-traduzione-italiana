"""Scrive le rese di un file `blocco|riga -> italiano` dentro un lotto di file dati.

    python scratchpad/_applica-rese-dati.py lavoro/talk-001.jsonl scratchpad/_talk-rese-001.json

Le chiavi che cominciano con `_` sono note e si saltano. Dice quante voci ha
toccato e quante rese non hanno trovato la loro voce: una resa che non aggancia
niente e' un errore di battitura nella chiave, non una riga in piu'.
"""
import json
import sys
from pathlib import Path


def main() -> None:
    percorso_lotto = Path(sys.argv[1])
    percorso_rese = Path(sys.argv[2])

    rese = {k: v for k, v in
            json.loads(percorso_rese.read_text(encoding="utf-8")).items()
            if not k.startswith("_")}

    lotto = [json.loads(r) for r in
             percorso_lotto.read_text(encoding="utf-8").splitlines() if r.strip()]

    usate = set()
    toccate = 0
    for voce in lotto:
        chiave = f"{voce['blocco']}|{voce['riga']}"
        if chiave in rese:
            voce["it"] = rese[chiave]
            usate.add(chiave)
            toccate += 1

    percorso_lotto.write_text(
        "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in lotto),
        encoding="utf-8")

    orfane = sorted(set(rese) - usate)
    print(f"rese scritte: {toccate}")
    print(f"tradotte in tutto: {sum(1 for v in lotto if v['it'])} / {len(lotto)}")
    if orfane:
        print(f"⚠️  {len(orfane)} rese non hanno trovato la voce:")
        for chiave in orfane:
            print("     ", chiave)


if __name__ == "__main__":
    main()
