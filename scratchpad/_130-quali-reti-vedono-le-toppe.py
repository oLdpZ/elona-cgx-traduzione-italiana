# -*- coding: utf-8 -*-
"""Misura la premessa della 129a: quali reti vedono davvero le toppe.

La ripresa della 129a scrive che le toppe «hanno tre referti — participi,
elisioni, caratteri a doppia larghezza — e **nessuno** che guardi il glossario,
le larghezze o le maiuscole».

Tre affermazioni, e non hanno la stessa forma. Prima di scrivere una rete si
guarda **da dove ciascuna di quelle reti prende il testo**, perche' una rete che
legge la build vede le toppe per costruzione, e una che legge il dizionario non
puo' vederle nemmeno per sbaglio.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-quali-reti-vedono-le-toppe.py
"""
import io
import json
import re
import sys

from strumenti import larghezze, percorsi

LETTERALE = re.compile(r'"(?:[^"\\]|\\.)*"')
CNVEN = re.compile(r"\bcnven\s*\(")


def righe(valore) -> list:
    return list(valore) if isinstance(valore, list) else [valore]


def testo_aggiunto(toppa: dict) -> list:
    """I letterali che `sostituisci` porta e `cerca` non aveva: l'italiano.

    Stessa definizione di `_126-referti-toppe.py`, apposta: due reti che
    cercano la stessa cosa con due regole diverse danno due numeri che non si
    possono confrontare.
    """
    vecchi = set()
    for r in righe(toppa["cerca"]):
        vecchi.update(LETTERALE.findall(r))
    fuori = []
    for r in righe(toppa["sostituisci"]):
        for x in LETTERALE.findall(r):
            if x not in vecchi:
                fuori.append(x[1:-1])
    return fuori


def main() -> int:
    toppe = [json.loads(l) for l in
             io.open(percorsi.PROGETTO / "toppe.jsonl", encoding="utf-8")
             if l.strip()]
    con_testo = [t for t in toppe if testo_aggiunto(t)]

    print("toppe                       : %d" % len(toppe))
    print("toppe che aggiungono testo  : %d" % len(con_testo))
    print()

    # ------------------------------------------------------------------ 1
    # `maiuscole` legge percorsi.BUILD_HSP: le toppe ci sono gia' dentro.
    # Ma una rete che non ha casi da giudicare passa verde per costruzione:
    # il numero che conta non e' «le vede», e' «quante ne ha giudicate».
    con_cnven = [t for t in toppe
                 if any(CNVEN.search(r) for r in righe(t["sostituisci"]))]
    print("MAIUSCOLE (legge la build)")
    print("  toppe che il suo occhio potrebbe giudicare (con `cnven(`) : %d"
          % len(con_cnven))
    for t in con_cnven:
        print("    %s:%s" % (t["file"], t.get("riga", "?")))
    print()

    # ------------------------------------------------------------------ 2
    # `larghezze.fuori_misura` scorre il DIZIONARIO e cerca (file, riga) nelle
    # mappe dei menu ricavate dal SORGENTE. Una toppa non ha una voce di
    # dizionario: non entra nel ciclo in nessun caso.
    # Il numero da misurare e': quante toppe cadono su una riga che il
    # sorgente dichiara essere una voce di menu con un riquadro noto?
    per_riga = larghezze.menu_per_riga(percorsi.SORGENTE_HSP / larghezze.FILE)
    px_per_menu = larghezze.larghezze(percorsi.SORGENTE_HSP)
    diretti = larghezze.menu_diretti(percorsi.SORGENTE_HSP)

    dentro_un_riquadro = []
    for t in toppe:
        nome = t["file"]
        riga = t.get("riga")
        if not isinstance(riga, int):
            continue
        px = None
        if nome == larghezze.FILE and riga in per_riga:
            px = px_per_menu.get(per_riga[riga])
        if px is None:
            px = diretti.get((nome, riga))
        if px is not None:
            dentro_un_riquadro.append((nome, riga, px, testo_aggiunto(t)))

    print("LARGHEZZE (legge sorgente + dizionario)")
    print("  voci di menu con riquadro noto, da text.hsp   : %d"
          % len([r for r in per_riga if px_per_menu.get(per_riga[r])]))
    print("  voci di menu con riquadro noto, altrove       : %d" % len(diretti))
    print("  toppe che cadono dentro uno di quei riquadri  : %d"
          % len(dentro_un_riquadro))
    for nome, riga, px, testi in dentro_un_riquadro:
        tetto = larghezze.budget(px)
        print("    %-18s %6d  %4dpx  tetto %2d" % (nome, riga, px, tetto))
        for testo in testi:
            misurato = larghezze.reso(testo)
            segno = "SFORA" if len(misurato) > tetto else "     "
            print("      %s %3d  %s" % (segno, len(misurato), misurato[:70]))
    print()

    # ------------------------------------------------------------------ 3
    print("GLOSSARIO")
    print("  strumenti che leggono glossario.md: 0 "
          "(nessuna rete, ne' sul dizionario ne' sulle toppe)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
