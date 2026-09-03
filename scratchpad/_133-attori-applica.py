"""Espande una tabella di etichette `{actor_N}` su tutte le voci di un lotto.

Le etichette si ripetono: nel lotto C sono 41 distinte su 155 voci. Deciderle
una volta e scriverle a mano 155 e' il modo di averne due diverse per lo
stesso personaggio, che e' esattamente il difetto che il piano della Fase 4
teme sui nomi.

    ... _133-attori-applica.py lavoro/scene2-101-135.jsonl scratchpad/rese/C-attori.json

Scrive un file di rese `{"scena.blocco": "resa"}` pronto per `_133-inserisci.py`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    lotto = Path(sys.argv[1])
    tabella_percorso = Path(sys.argv[2])
    uscita = Path(sys.argv[3]) if len(sys.argv) > 3 else Path("scratchpad/rese/C-attori-espansi.json")

    voci = [json.loads(r) for r in lotto.read_text(encoding="utf-8").splitlines()
            if r.strip()]
    tabella = {k: v for k, v in
               json.loads(tabella_percorso.read_text(encoding="utf-8")).items()
               if not k.startswith("_")}

    rese: dict[str, str] = {}
    ignote: set[str] = set()
    for voce in voci:
        if not voce["tipo"].startswith("actor"):
            continue
        etichetta = voce["en"]
        if etichetta not in tabella:
            ignote.add(etichetta)
            continue
        rese["%s.%s" % (voce["scena"], voce["blocco"])] = tabella[etichetta]

    if ignote:
        print("etichette del lotto che la tabella non copre:")
        for etichetta in sorted(ignote):
            print("    %s" % etichetta)
        return 1

    inutili = sorted(set(tabella) - {v["en"] for v in voci
                                     if v["tipo"].startswith("actor")})
    if inutili:
        print("⚠️ righe della tabella che il lotto non usa (un refuso?):")
        for etichetta in inutili:
            print("    %s" % etichetta)

    uscita.write_text(json.dumps(rese, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8")
    print("%d etichette distinte -> %d voci in %s"
          % (len(tabella), len(rese), uscita))
    return 0


if __name__ == "__main__":
    sys.exit(main())
