"""La forma esatta delle schede di carta scritte a mano (lotto C della Fase 6).

`carddetailneff@tcg(<indice>) = "<letterale>"`: l'indice e' una **variabile**,
quindi non c'e' una chiave come il nome della costante della Fase 5. Serve
sapere quante siano davvero, quali portino concatenazioni e quali siano
letterali puri, prima di decidere la chiave.
"""
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strumenti import percorsi  # noqa: E402

ASSEGNA = re.compile(r'carddetailneff@tcg\(([^)]*)\)\s*(\+?=)\s*(.*)$')
# Un letterale HSP: virgolette, con `\"` protetto dentro.
LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')


def main() -> int:
    conti = Counter()
    puri, concatenati, senza_letterale = [], [], []
    for nome in ("tcg_skill.hsp", "tcg.hsp", "tcg_custom.hsp"):
        percorso = percorsi.SORGENTE_HSP / nome
        righe = percorso.read_text(encoding="cp932").splitlines()
        if len(righe) < 500:
            raise SystemExit("%s diviso in %d righe: divisione fallita"
                             % (nome, len(righe)))
        for numero, riga in enumerate(righe, 1):
            spoglia = riga.lstrip()
            if spoglia.startswith(";") or spoglia.startswith("//"):
                continue
            trovato = ASSEGNA.search(riga)
            if not trovato:
                continue
            coda = trovato.group(3)
            letterali = LETTERALE.findall(coda)
            conti[nome] += 1
            if not letterali:
                senza_letterale.append((nome, numero, coda[:70]))
            elif LETTERALE.sub("", coda).strip() in ("", "+"):
                puri.append((nome, numero, letterali))
            else:
                concatenati.append((nome, numero, coda[:100]))

    print("assegnazioni per file:", dict(conti))
    print()
    print("letterali PURI            : %d siti, %d letterali"
          % (len(puri), sum(len(l) for _, _, l in puri)))
    print("con CONCATENAZIONE        : %d siti" % len(concatenati))
    print("senza nessun letterale    : %d siti  (variabili: non sono testo)"
          % len(senza_letterale))
    print()

    print("--- i concatenati, che sono quelli che decidono la chiave ---")
    for nome, numero, coda in concatenati:
        print("  %s:%d\n      %s" % (nome, numero, coda))
    print()

    tutti = [l for _, _, ls in puri for l in ls]
    doppi = [s for s, q in Counter(tutti).items() if q > 1]
    print("letterali distinti        : %d su %d" % (len(set(tutti)), len(tutti)))
    print("letterali RIPETUTI        : %d  %s"
          % (len(doppi), [d[:40] for d in doppi[:5]]))
    print()
    print("--- vocabolario della scheda: chi lo scrive a mano ---")
    for chiave in ("No.???", "Rare:", "Effect:", "[Command Card]", "Data:",
                   "<Land>", "<Spell>"):
        quante = sum(1 for s in tutti if chiave in s)
        print("   %-16s %d letterali lo contengono" % (chiave, quante))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
