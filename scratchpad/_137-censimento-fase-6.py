"""Le 199 stringhe scoperte della Fase 6, con riga e forma sintattica.

Il censimento della copertura dice *quante* sono e *perche'* sono li'; per
lavorarle serve sapere **dove** stanno e **in che costrutto**, perche' e' il
costrutto a decidere se una stringa ha una chiave stabile o no.
"""
import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strumenti import copertura, percorsi  # noqa: E402

FILE = ["tcg_skill.hsp", "tcg.hsp", "tcg_custom.hsp", "db_card.hsp"]

# Le forme che ci si aspetta di trovare, in ordine di specificita': la prima che
# aggancia vince, cosi' `carddetailneff` non finisce dentro «assegnazione».
FORME = [
    ("scheda",        re.compile(r"carddetailneff@tcg\s*\(")),
    ("etichetta",     re.compile(r"rtvaln2?\s*(\+=|=)")),
    ("battuta",       re.compile(r"efllistaddchat|cnvtalk|eflistaddchat")),
    ("randomchat",    re.compile(r"randomchat@tcg")),
    ("markerword",    re.compile(r"markerwords")),
    ("traccia",       re.compile(r"\bproctcg\b|\bproc\b|poptext@tcg")),
    ("sostituzione",  re.compile(r"\bsreplace\b|\binstr\s*\(|\bstrmid\s*\(")),
    ("menu",          re.compile(r"\bs@tcg\s*(\+=|=)|\bmes\b|\bcfname@tcg\b")),
]


def main() -> int:
    toppe = copertura._righe_con_toppa()
    totale = Counter()
    for nome in FILE:
        percorso = percorsi.SORGENTE_HSP / nome
        testo = percorso.read_text(encoding="cp932", errors="replace")
        righe = testo.splitlines()
        scoperte = set(copertura.scoperte_di(nome, testo, toppe.get(nome, set())))
        if not scoperte:
            continue
        print("=" * 72)
        print("%s   %d stringhe distinte scoperte" % (nome, len(scoperte)))
        print("=" * 72)
        per_forma = {}
        for numero, riga in enumerate(righe, 1):
            presenti = [s for s in scoperte if '"%s"' % s in riga]
            if not presenti:
                continue
            forma = "altro"
            for etichetta, modello in FORME:
                if modello.search(riga):
                    forma = etichetta
                    break
            for stringa in presenti:
                per_forma.setdefault(forma, []).append((numero, stringa))
        for forma in sorted(per_forma, key=lambda f: -len(per_forma[f])):
            voci = per_forma[forma]
            distinte = {s for _, s in voci}
            totale[forma] += len(distinte)
            print("\n--- %s: %d siti, %d stringhe distinte"
                  % (forma, len(voci), len(distinte)))
            for numero, stringa in voci[:8]:
                print("    %5d  %s" % (numero, stringa[:88]))
            if len(voci) > 8:
                print("    ... e altri %d siti" % (len(voci) - 8))
        print()
    print("=" * 72)
    print("per forma, su tutti e quattro i file:")
    for forma, quante in totale.most_common():
        print("   %-14s %d" % (forma, quante))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
