# -*- coding: utf-8 -*-
"""Il buco di `nudi_en`: le righe che portano un letterale nudo E una `lang()`.

`nudi_en.py:127` fa `if 'lang(' in s: continue`, e la ragione c'era: una riga
con `lang()` e' materia del dizionario, non delle toppe. Ma **una riga puo'
avere tutt'e due le cose**, e allora la parte fuori dalla `lang()` non la guarda
nessuno — ne' `estrai.py` (che cerca `lang()`), ne' `nudi_en` (che salta la riga).

Il caso che l'ha fatto vedere e' il titolo del pannello delle tattiche:

    custom_ai.hsp:1530
      s = "Tactical Instructions", lang("Shift,Esc [戻る]…", "Shift,Esc [Back]…")

Il pannello e' stato chiuso nella 51a con 193 toppe e collaudato nella 52a, che
ci ha trovato tre difetti. Il **titolo in cima alla finestra** e' rimasto
inglese, e nessuna rete poteva dirlo.

⚠️ **Il conto va fatto con un analizzatore di parentesi, non con una regex.**
Il primo tentativo mascherava le `lang()` con `lang\\s*\\((?:[^()]|\\([^()]*\\))*\\)`,
che regge un solo livello di annidamento: su `lang("…" + name(x) + "…", …)` la
maschera si rompe a meta' e i pezzi di lang che restano fuori vengono contati
per nudi. Dava **540** righe, quasi tutte false. Qui le `lang()` si saltano
contando le parentesi e rispettando le virgolette.
"""
import glob
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nudi_en  # noqa: E402


def fuori_dalle_lang(riga: str) -> str:
    """La riga con il contenuto di ogni `lang(...)` sostituito da un segnaposto."""
    fuori = []
    i = 0
    n = len(riga)
    while i < n:
        if riga.startswith("lang(", i) and (i == 0 or not (riga[i - 1].isalnum() or riga[i - 1] == "_")):
            livello = 0
            dentro = False
            j = i + 4
            while j < n:
                c = riga[j]
                if c == '"' and riga[j - 1] != "\\":
                    dentro = not dentro
                elif not dentro:
                    if c == "(":
                        livello += 1
                    elif c == ")":
                        livello -= 1
                        if livello == 0:
                            break
                j += 1
            fuori.append("LANG")
            i = j + 1
            continue
        fuori.append(riga[i])
        i += 1
    return "".join(fuori)


# ⚠️ I marcatori passati come argomento, che non si vedono a schermo. `"null"` e'
#    il secondo argomento di `promptAdd testo, "null", indice` — 34 righe di
#    `map_user.hsp` erano tutte questo, e senza il filtro il referto diceva 130
#    dove i casi veri erano molti meno. Stessa famiglia di `%txtAggro` in
#    `nudi_en`: forma di marcatore, non parola.
_MARCATORI = frozenset({"null", "dead"})


def righe_miste(righe: list[str]) -> list[int]:
    """Gli indici (0-based) delle righe di uscita con un nudo FUORI dalla lang()."""
    trovati = []
    for i, riga in enumerate(righe):
        s = riga.strip()
        if not s or s.startswith(("//", "#", "/*")):
            continue
        if "lang(" not in s:
            continue          # queste le vede gia' `nudi_en`
        if s.startswith("cnv_str") or nudi_en._PER_CHIAVE.search(s):
            continue
        if not (nudi_en._DISEGNA.match(s) or nudi_en._COMPONE.match(s)):
            continue
        resto = fuori_dalle_lang(s)
        letterali = [m for m in nudi_en._LETTERALE.findall(resto)
                     if m.strip() not in _MARCATORI]
        if any(nudi_en._e_testo(m) for m in letterali):
            trovati.append(i)
    return trovati


def main(argv: list[str]) -> int:
    tot = intatte = 0
    for percorso in sorted(glob.glob(nudi_en.SORGENTE + r"\*.hsp")):
        nome = os.path.basename(percorso)
        sorg = io.open(percorso, encoding="cp932").read().split("\n")
        costruito = os.path.join(nudi_en.BUILD, nome)
        build = (io.open(costruito, encoding="cp932").read().split("\n")
                 if os.path.exists(costruito) else sorg)
        indici = righe_miste(sorg)
        if not indici:
            continue
        allineata = len(build) == len(sorg)
        if allineata:
            ferme = [i for i in indici if build[i] == sorg[i]]
        else:
            insieme = set(build)
            ferme = [i for i in indici if sorg[i] in insieme]
        tot += len(indici)
        intatte += len(ferme)
        print("=== %s: %d righe miste, %d ancora intatte" % (nome, len(indici), len(ferme)))
        for i in ferme:
            print("  %6d | %s" % (i + 1, sorg[i].strip()[:120]))
    print("--- struttura: %d righe miste | ancora da fare: %d" % (tot, intatte))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
