"""Mette le rese dentro un lotto di scene, e le misura PRIMA di reimportare.

    ... _133-inserisci.py lavoro/scene2-11.jsonl scratchpad/rese/11.json

Il file delle rese e' un oggetto `{"scena.blocco": "resa"}`. Per i `{txt}` la
resa porta gli a capo come `\\n`, per i `{chat_N}` e' una riga sola.

⚠️ Non scrive niente nel dizionario: quello lo fa `scene --reimporta`, che
valida tutto il lotto e rifiuta in blocco. Questo comando serve al giro di
prima -- vedere quante righe verranno e di quanto si sfora -- perche' un
cancello che dice solo si'/no non dice il margine, e senza il margine si
riscrive alla cieca.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from strumenti import scene
from strumenti.accenti import degrada


def main() -> int:
    analizzatore = argparse.ArgumentParser()
    analizzatore.add_argument("lotto")
    analizzatore.add_argument("rese")
    analizzatore.add_argument("--scrivi", action="store_true",
                              help="riscrive il lotto con le rese dentro")
    argomenti = analizzatore.parse_args()

    percorso = Path(argomenti.lotto)
    voci = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines()
            if r.strip()]
    rese = json.loads(Path(argomenti.rese).read_text(encoding="utf-8"))

    per_chiave = {"%s.%s" % (v["scena"], v["blocco"]): v for v in voci}
    ignote = sorted(set(rese) - set(per_chiave))
    if ignote:
        print("chiavi che non stanno nel lotto: %s" % ", ".join(ignote))
        return 1

    guasti = 0
    for chiave, resa in rese.items():
        voce = per_chiave[chiave]
        voce["it"] = resa
        tipo = voce["tipo"]
        if tipo.startswith("chat_"):
            righe = scene.righe_a_capo(degrada(resa))
            inglesi = scene.righe_a_capo(voce["en"])
            piu_lunga = max(len(r) for r in righe)
            print("%-8s %-8s %2d/%d righe (inglese %2d), riga piu' lunga %2d/%d"
                  % (chiave, tipo, len(righe), scene.SOFFITTO_CHAT,
                     len(inglesi), piu_lunga, scene.CODA_MASSIMA))
        elif tipo == "txt":
            righe = degrada(resa).split("\n")
            piu_lunga = max(len(r) for r in righe)
            print("%-8s %-8s %2d righe (inglese %2d), riga piu' lunga %2d/%d"
                  % (chiave, tipo, len(righe), len(voce["en"].split("\n")),
                     piu_lunga, scene.LARGHEZZA_TXT))
        else:
            print("%-8s %-8s %s" % (chiave, tipo, resa))
        for guaio in scene.problemi(voce):
            print("    FUORI: %s" % guaio)
            guasti += 1
        for avviso in scene.avvisi(voce):
            print("    guarda: %s" % avviso)

    mancanti = [k for k, v in per_chiave.items() if not v.get("it")]
    print("\nrese messe: %d   ancora senza: %d   fuori misura: %d"
          % (len(rese), len(mancanti), guasti))
    # ⚠️ elencarle tutte su un lotto da 632 voci vuol dire seppellire le tre
    # righe che contano sotto trecento chiavi: un comando che stampa troppo e'
    # muto quanto uno che non stampa niente.
    if mancanti and len(mancanti) <= 30:
        print("  senza resa: %s" % ", ".join(mancanti))
    elif mancanti:
        print("  senza resa, le prime: %s ..." % ", ".join(mancanti[:10]))

    if argomenti.scrivi:
        if guasti:
            print("non scrivo: prima si rientra nelle misure")
            return 1
        percorso.write_text(
            "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in voci),
            encoding="utf-8")
        print("scritto %s" % percorso)
    return 1 if guasti else 0


if __name__ == "__main__":
    sys.exit(main())
