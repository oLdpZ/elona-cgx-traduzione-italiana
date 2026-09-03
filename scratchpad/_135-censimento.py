"""Censimento della copertura, file per file del SORGENTE (non del dizionario).

Il buco che questo referto misura: `verifica --dizionario` scorre
`DIZIONARIO/*.jsonl`, cioe' i file che qualcuno ha gia' deciso di coprire. Un
file senza dizionario non risulta «scoperto»: non risulta affatto. E
`_123-file-senza-dizionario.py` guarda i file **con `lang()` e senza
dizionario**, quindi non vede quelli che non hanno ne' l'uno ne' l'altro —
che e' esattamente la forma di `tcg_skill.hsp`.

Qui si parte dall'elenco degli `.hsp` del sorgente e si chiede, per ciascuno:
quanto testo inglese NUDO contiene, e chi lo copre.
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from strumenti import percorsi

# Un letterale HSP, con la regola del backslash: `\"` non chiude la stringa.
_LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')

# «Prosa»: almeno due parole alfabetiche separate da spazio, di cui una lunga
# almeno tre lettere. Serve a separare una frase da un identificatore
# (`"dragon"`, `"bg3"`, `"\t"`, `"ITEM_ID_X"`), che una lingua non tocca.
_PROSA = re.compile(r"[A-Za-z]{3}[a-z]*\s+[A-Za-z]")


def letterali_di_prosa(testo: str) -> list[str]:
    fuori = []
    for riga in testo.split("\n"):
        spoglia = riga.strip()
        # il commento HSP e' `;` oppure `//`: la riga morta non e' testo a
        # schermo, ed e' la quarta volta che il progetto ci inciampa (rinviate)
        if spoglia.startswith(";") or spoglia.startswith("//"):
            continue
        for m in _LETTERALE.finditer(riga):
            s = m.group(1)
            if _PROSA.search(s):
                fuori.append(s)
    return fuori


def main() -> None:
    toppe = Counter()
    for r in (percorsi.PROGETTO / "toppe.jsonl").read_text(encoding="utf-8").splitlines():
        if r.strip():
            toppe[json.loads(r)["file"]] += 1

    righe = []
    for f in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
        testo = f.read_bytes().decode("cp932")
        prosa = letterali_di_prosa(testo)
        righe.append({
            "file": f.name,
            "righe": testo.count("\n") + 1,
            "lang": len(re.findall(r"\blang\(", testo)),
            "diz": (percorsi.DIZIONARIO / f"{f.name}.jsonl").exists(),
            "toppe": toppe.get(f.name, 0),
            "prosa": len(prosa),
            "prosa_distinta": len(set(prosa)),
            "campioni": sorted(set(prosa))[:3],
        })

    scoperti = [r for r in righe if r["prosa"] and not r["diz"] and not r["toppe"]]
    print(f"  {'file':<30} {'righe':>6} {'lang':>5} {'diz':>4} {'toppe':>6} {'prosa':>6} {'dist':>5}")
    print("  " + "-" * 72)
    for r in sorted(righe, key=lambda r: -r["prosa"]):
        if r["prosa"] == 0:
            continue
        marchio = "  <== SCOPERTO" if r in scoperti else ""
        print(f"  {r['file']:<30} {r['righe']:>6} {r['lang']:>5} "
              f"{'si' if r['diz'] else 'NO':>4} {r['toppe']:>6} "
              f"{r['prosa']:>6} {r['prosa_distinta']:>5}{marchio}")

    print()
    print(f"  file con prosa inglese nuda e NESSUNA copertura: {len(scoperti)}")
    for r in scoperti:
        print(f"\n  --- {r['file']}: {r['prosa_distinta']} stringhe distinte")
        for c in r["campioni"]:
            print(f"        {c[:100]!r}")

    # file senza prosa: sono quelli che una lista di esenzioni dovrebbe
    # dichiarare, e il numero serve a sapere quanto e' lunga quella lista
    muti = [r for r in righe if r["prosa"] == 0]
    print(f"\n  file senza nessuna prosa inglese nuda: {len(muti)} su {len(righe)}")


if __name__ == "__main__":
    main()
