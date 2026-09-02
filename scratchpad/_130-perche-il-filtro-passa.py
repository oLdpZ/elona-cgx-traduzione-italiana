# -*- coding: utf-8 -*-
"""Perche' il filtro del glossario lascia passare meta' dell'insieme.

Prima stesura: 163 voci con un termine da giudicare, **87 divergenze**. Un
filtro che boccia piu' della meta' non e' un filtro, e' l'elenco completo con un
passaggio in piu' — lezione della 129a, sul `grep` delle condizioni.

Qui non si tira a indovinare quale restrizione salva: si **contano** i termini
che producono le bocciature, e si guarda che forma hanno. Poi si misurano due o
tre restrizioni candidate una accanto all'altra, e si sceglie con un numero.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-perche-il-filtro-passa.py
"""
import re
import sys

from strumenti.accenti import degrada

sys.path.insert(0, __file__.rsplit("\\", 1)[0].rsplit("/", 1)[0])
import importlib.util as _u

_spec = _u.spec_from_file_location(
    "g130", __file__.replace("_130-perche-il-filtro-passa.py",
                             "_130-glossario-nelle-toppe.py"))
g = _u.module_from_spec(_spec)
_spec.loader.exec_module(g)


def giudizio(inglese, italiano, termini, solo_maiuscolo, tetto):
    """Le divergenze di una coppia, sotto una certa restrizione."""
    basso = inglese.lower()
    it_stem = degrada(italiano).lower()
    fuori = []
    for termine in termini:
        if not re.search(r"\b%s\b" % re.escape(termine), basso):
            continue
        if tetto is not None and len(inglese) > tetto:
            continue
        if solo_maiuscolo:
            # il termine, scritto com'e' nel testo: maiuscolo e non a inizio frase
            maiuscolo = False
            for m in re.finditer(r"\b%s\b" % re.escape(termine), inglese, re.I):
                scritto = inglese[m.start():m.end()]
                if not scritto[0].isupper():
                    continue
                prima = inglese[:m.start()].rstrip()
                if prima and prima[-1] in ".!?":
                    continue
                if not prima:
                    continue
                maiuscolo = True
            if not maiuscolo:
                continue
        va_bene = any(all(s in it_stem for s in stems)
                      for stems in termini[termine])
        if not va_bene:
            fuori.append(termine)
    return fuori


def main() -> int:
    termini = g.glossario()
    coppie = list(g.coppie_delle_toppe())

    print("le restrizioni, una accanto all'altra\n")
    print("%-34s %9s %9s" % ("restrizione", "giudicate", "divergenze"))
    varianti = [
        ("nessuna (la prima stesura)", False, None),
        ("solo inglese <= 40 caratteri", False, 40),
        ("solo inglese <= 25 caratteri", False, 25),
        ("solo termine maiuscolo", True, None),
        ("maiuscolo + inglese <= 40", True, 40),
    ]
    quali = {}
    for nome, maiuscolo, tetto in varianti:
        giudicate = 0
        div = []
        for dove, inglese, italiano in coppie:
            if tetto is not None and len(inglese) > tetto:
                continue
            if any(re.search(r"\b%s\b" % re.escape(t), inglese.lower())
                   for t in termini):
                giudicate += 1
            for termine in giudizio(inglese, italiano, termini, maiuscolo, tetto):
                div.append((dove, termine, inglese, italiano))
        print("%-34s %9d %9d" % (nome, giudicate, len(div)))
        quali[nome] = div

    print("\ni termini che producono piu' bocciature, senza restrizione:")
    conta = {}
    for dove, termine, inglese, italiano in quali["nessuna (la prima stesura)"]:
        conta[termine] = conta.get(termine, 0) + 1
    for termine, n in sorted(conta.items(), key=lambda x: -x[1])[:15]:
        print("   %-14s %3d   rese: %s" % (
            termine, n, " | ".join(sorted(" ".join(s) for s in termini[termine]))))

    scelta = "maiuscolo + inglese <= 40"
    print("\ncon «%s» restano %d divergenze:\n" % (scelta, len(quali[scelta])))
    for dove, termine, inglese, italiano in quali[scelta]:
        print("  %-20s «%s»" % (dove, termine))
        print("      en: %s" % inglese[:100])
        print("      it: %s" % italiano[:100])
    return 0


if __name__ == "__main__":
    sys.exit(main())
