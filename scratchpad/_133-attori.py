"""Per ogni etichetta `{actor_N}` di un lotto, che cosa il progetto ha gia' deciso.

Le etichette hanno la forma `<Nome> epiteto`, la stessa delle «aka» delle
creature che la Fase 2 ha gia' deciso -- ma **non sono le stesse stringhe**:
il piano della Fase 4 ha contato 6 identiche, 27 con lo stesso `<Nome>` e un
epiteto diverso, e 57 senza corrispondenza. Quindi la resa e' una decisione,
non un riscontro; ma prenderla senza guardare che cosa il progetto scrive gia'
per quel nome e' il modo di avere due epiteti per la stessa persona.

    ... _133-attori.py lavoro/scene2-101-135.jsonl
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

from strumenti import percorsi

NOME = re.compile(r"[<{]([^>}]+)[>}]")


def rese_del_nome(nome: str) -> Counter:
    """Come il progetto rende, altrove, le stringhe che nominano `nome`."""
    fuori: Counter = Counter()
    marca = "<%s>" % nome
    for percorso in sorted(percorsi.DIZIONARIO.rglob("*.jsonl")):
        if percorso.stem == "scene2.hsp":
            continue          # e' il file che stiamo traducendo
        for riga in percorso.read_text(encoding="utf-8").splitlines():
            if not riga.strip() or marca not in riga:
                continue
            voce = json.loads(riga)
            inglese = voce.get("en") or ""
            reso = voce.get("it") or ""
            if not isinstance(inglese, str) or not isinstance(reso, str):
                continue
            # solo dove il nome e' TUTTA la stringa o quasi: una battuta lunga
            # che lo nomina non e' una resa del nome
            if marca in inglese and len(inglese) < 80 and reso:
                fuori[(inglese, reso)] += 1
    return fuori


def main() -> int:
    lotto = Path(sys.argv[1])
    voci = [json.loads(r) for r in lotto.read_text(encoding="utf-8").splitlines()
            if r.strip()]
    etichette: Counter = Counter()
    for voce in voci:
        if voce["tipo"].startswith("actor"):
            etichette[voce["en"]] += 1

    senza = []
    for etichetta, quante in etichette.most_common():
        pezzi = NOME.search(etichetta)
        print("%3dx  %s" % (quante, etichetta))
        if pezzi is None:
            print("      (nessun <Nome>: e' un ruolo)")
            senza.append(etichetta)
            continue
        rese = rese_del_nome(pezzi.group(1))
        if not rese:
            print("      il progetto non ha ancora reso <%s> da nessuna parte"
                  % pezzi.group(1))
            senza.append(etichetta)
            continue
        for (inglese, reso), volte in rese.most_common(4):
            uguale = "=" if inglese == etichetta else " "
            print("    %s %3dx  %s" % (uguale, volte, inglese))
            print("           -> %s" % reso)

    print("\netichette: %d   senza precedente: %d" % (len(etichette), len(senza)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
