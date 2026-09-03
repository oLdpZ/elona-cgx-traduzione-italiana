"""Le stringhe scoperte, una per una, col comando che le ospita.

Il referto di `copertura --referto` dice QUANTE sono; per dichiararle serve
sapere COSA sono. Qui ogni stringa esce con la riga e con la testa
dell'istruzione, che e' il dato che dice dove finisce: `dialog` e' una finestra,
`mes` e' testo a schermo, `proc` e' una traccia di debug, `mci` e' il sistema
operativo, un `==` e' un operando di confronto.
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from strumenti import copertura, percorsi
from strumenti.estrai import siti

# la testa dell'istruzione: il primo identificatore della riga
_TESTA = re.compile(r"^\s*([A-Za-z_][\w@]*)")


def scoperte_con_riga(nome: str, testo: str, toppe: set[str]):
    span = defaultdict(list)
    for s in siti(testo):
        span[s[0]].append((s[7], s[8]))
    for n, riga in enumerate(testo.split("\n"), 1):
        spoglia = riga.lstrip()
        if spoglia.startswith(";") or spoglia.startswith("//"):
            continue
        for m in copertura._LETTERALE.finditer(riga):
            if not copertura._PROSA.search(m.group(1)):
                continue
            if any(a <= m.start(1) and m.end(1) <= b for a, b in span.get(n, [])):
                continue
            if riga.strip() in toppe:
                continue
            testa = _TESTA.match(riga)
            yield n, (testa.group(1) if testa else "?"), m.group(1), riga.strip()


def main() -> None:
    quali = sys.argv[1:] or sorted(copertura.DA_TRIARE)
    toppe = copertura._righe_con_toppa()
    for nome in quali:
        percorso = percorsi.SORGENTE_HSP / nome
        testo = percorso.read_bytes().decode("cp932")
        voci = list(scoperte_con_riga(nome, testo, toppe.get(nome, set())))
        distinte = {v[2] for v in voci}
        teste = Counter(v[1] for v in voci)
        print(f"\n{'='*78}\n{nome}  —  {len(voci)} scoperte, {len(distinte)} distinte")
        print(f"  teste: {', '.join(f'{t}×{c}' for t, c in teste.most_common(8))}")
        viste = set()
        for n, testa, s, riga in voci:
            if s in viste:
                continue
            viste.add(s)
            print(f"  :{n:<6} {testa:<16} {s[:110]!r}")


if __name__ == "__main__":
    main()
