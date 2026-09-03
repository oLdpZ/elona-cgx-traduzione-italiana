"""Il terreno del lotto B di `scene2.hsp` (scene 7-30), prima di tradurre.

Non decide niente e non e' un cancello: conta. Serve a sapere da dove si
comincia, e soprattutto **quali blocchi hanno margine zero**, che il piano
della Fase 4 vuole tradotti per primi -- perche' se l'italiano non ci sta la
risposta non e' una resa piu' corta, e' spezzare il blocco, e quella e' una
decisione di struttura che conviene prendere sul primo caso e non sul settimo.

⚠️ Le soglie NON si riscrivono qui: si importano da `strumenti.scene`, che le
tiene col loro perche' (la 132a ha gia' pagato una volta per aver ricalcolato
il soffitto del riquadro invece di cercare da dove venisse).

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_133-lotto-b-terreno.py
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

from strumenti import scene

LOTTO = Path("lavoro/scene2-7-30.jsonl")


def main() -> int:
    if not LOTTO.exists():
        print(f"{LOTTO} non c'e': lancia `python -m strumenti.scene --estrai 7-30`")
        return 1

    voci = [json.loads(r) for r in LOTTO.read_text(encoding="utf-8").splitlines()
            if r.strip()]
    tradotte = sum(1 for v in voci if v.get("it"))
    print(f"{LOTTO.name}: {len(voci)} voci, {tradotte} gia' tradotte")
    print(f"  soffitti in forza: chat {scene.SOFFITTO_CHAT} righe a colonna "
          f"{scene.COLONNA_CHAT}, coda {scene.CODA_MASSIMA}, "
          f"targa {scene.LARGHEZZA_TXT} caratteri")

    print("\n  per tipo:")
    for tipo, quante in sorted(Counter(v["tipo"] for v in voci).items()):
        print(f"    {tipo:<12} {quante:>4}")

    caratteri = 0

    # --- i {chat_N}: il vincolo e' l'altezza -------------------------------
    altezze: list[tuple[int, int, dict]] = []
    for voce in voci:
        if not voce["tipo"].startswith("chat"):
            continue
        caratteri += len(voce["en"])
        righe = scene.righe_a_capo(voce["en"])
        coda = len(righe[-1]) if righe else 0
        altezze.append((len(righe), coda, voce))

    print(f"\n  {{chat_N}}: {len(altezze)} blocchi, altezza in righe disegnate")
    distribuzione = Counter(n for n, _, _ in altezze)
    for n in sorted(distribuzione):
        marca = ""
        if n > scene.SOFFITTO_CHAT:
            marca = "   <- OLTRE IL SOFFITTO gia' in inglese"
        elif n == scene.SOFFITTO_CHAT:
            marca = "   <- al soffitto, margine 0"
        print(f"    {n:>2} righe : {distribuzione[n]:>3}{marca}")

    stretti = [t for t in altezze if t[0] >= scene.SOFFITTO_CHAT - 1]
    print(f"\n    da tradurre per primi -- margine <= 1 riga ({len(stretti)}):")
    for n, _coda, voce in sorted(stretti, key=lambda t: -t[0]):
        print(f"      scena {voce['scena']:>3} blocco {voce['blocco']:>3} "
              f"riga {voce['riga']:>5}  {n} righe su {scene.SOFFITTO_CHAT}, "
              f"margine {scene.SOFFITTO_CHAT - n}")

    lunghe = [t for t in altezze if t[1] > scene.CODA_MASSIMA]
    print(f"\n    code oltre {scene.CODA_MASSIMA} caratteri: {len(lunghe)}")
    for _n, coda, voce in sorted(lunghe, key=lambda t: -t[1]):
        print(f"      scena {voce['scena']:>3} blocco {voce['blocco']:>3}  "
              f"coda di {coda}")

    # --- i {txt}: il vincolo e' la larghezza -------------------------------
    fuori = []
    piu_lunga = (0, None, "")
    quanti_txt = 0
    for voce in voci:
        if voce["tipo"] != "txt":
            continue
        quanti_txt += 1
        for riga in voce["en"].split("\n"):
            caratteri += len(riga)
            if len(riga) > piu_lunga[0]:
                piu_lunga = (len(riga), voce, riga)
            if len(riga) > scene.LARGHEZZA_TXT:
                fuori.append((len(riga), voce, riga))

    print(f"\n  {{txt}}: {quanti_txt} blocchi, targa da {scene.LARGHEZZA_TXT} caratteri")
    if piu_lunga[1] is not None:
        print(f"    la piu' lunga in inglese: {piu_lunga[0]} caratteri "
              f"(scena {piu_lunga[1]['scena']}, blocco {piu_lunga[1]['blocco']})")
        print(f"      {piu_lunga[2]!r}")
    print(f"    righe inglesi gia' oltre la targa: {len(fuori)}")
    for lunghezza, voce, riga in sorted(fuori, key=lambda t: -t[0]):
        print(f"      scena {voce['scena']:>3} blocco {voce['blocco']:>3}  "
              f"{lunghezza} caratteri: {riga!r}")

    # --- gli {actor_N}: nomi, non prosa ------------------------------------
    attori = sorted({v["en"].split(",")[0] for v in voci
                     if v["tipo"].startswith("actor")})
    print(f"\n  {{actor_N}}: {len(attori)} etichette distinte")

    print(f"\n  caratteri inglesi da tradurre: {caratteri}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
