"""Quante stringhe di prosa di ogni file NON le raggiunge nessuno.

⚠️ Il primo censimento della 135a chiedeva «questo file ha un dizionario o una
toppa?» e per questo dava `tcg_mod.hsp` per coperto: dizionario di 8 voci,
1 toppa, **809 stringhe inglesi distinte**. La copertura e' una proprieta'
della singola stringa, non del file.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from strumenti import copertura, percorsi
from strumenti.estrai import siti


def righe_con_toppa() -> dict[str, list[str]]:
    per_file = defaultdict(list)
    for r in (percorsi.PROGETTO / "toppe.jsonl").read_text(encoding="utf-8").splitlines():
        if r.strip():
            d = json.loads(r)
            # `cerca` e' quasi sempre una riga sola, ma alcune toppe ne
            # portano un elenco (il blocco di piu' righe)
            cerca = d["cerca"]
            if isinstance(cerca, list):
                per_file[d["file"]].extend(cerca)
            else:
                per_file[d["file"]].append(cerca)
    return per_file


def main() -> None:
    toppe = righe_con_toppa()
    esito = []
    for percorso in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
        testo = percorso.read_bytes().decode("cp932")
        righe = testo.split("\n")

        # 1. gli span che il dizionario raggiunge, riga per riga
        span_diz = defaultdict(list)
        try:
            for s in siti(testo):
                span_diz[s[0]].append((s[7], s[8]))
        except Exception as e:                      # noqa: BLE001
            print(f"  ⚠️ {percorso.name}: siti() {type(e).__name__}: {e}")

        # 2. le righe che una toppa riscrive
        toccate = {c.strip() for c in toppe.get(percorso.name, [])}

        scoperte, raggiunte = [], 0
        for n, riga in enumerate(righe, 1):
            spoglia = riga.lstrip()
            if spoglia.startswith(";") or spoglia.startswith("//"):
                continue
            for m in copertura._LETTERALE.finditer(riga):
                if not copertura._PROSA.search(m.group(1)):
                    continue
                dentro_lang = any(a <= m.start(1) and m.end(1) <= b
                                  for a, b in span_diz.get(n, []))
                if dentro_lang or riga.strip() in toccate:
                    raggiunte += 1
                else:
                    scoperte.append(m.group(1))

        if scoperte:
            esito.append({
                "file": percorso.name,
                "raggiunte": raggiunte,
                "scoperte": len(scoperte),
                "distinte": len(set(scoperte)),
                "campioni": sorted(set(scoperte))[:2],
            })

    esito.sort(key=lambda r: -r["distinte"])
    print(f"\n  {'file':<30} {'raggiunte':>10} {'scoperte':>9} {'distinte':>9}")
    print("  " + "-" * 62)
    for r in esito:
        print(f"  {r['file']:<30} {r['raggiunte']:>10} {r['scoperte']:>9} {r['distinte']:>9}")
    print(f"\n  file con almeno una stringa scoperta: {len(esito)}")
    print(f"  stringhe scoperte in tutto: {sum(r['scoperte'] for r in esito)} "
          f"({sum(r['distinte'] for r in esito)} distinte)")
    print("\n  --- i primi cinque, con un campione ---")
    for r in esito[:5]:
        print(f"\n  {r['file']} ({r['distinte']} distinte)")
        for c in r["campioni"]:
            print(f"      {c[:96]!r}")


if __name__ == "__main__":
    main()
