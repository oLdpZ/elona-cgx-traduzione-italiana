"""La struttura delle descrizioni degli oggetti di `db_item.hsp`, misurata.

Il perimetro dice «5.284 descrizioni MAI contate» e `else_jp.py` dice «6.840
righe» per lo stesso file: due numeri diversi per la stessa cosa, e nessuno dei
due e' l'unita' di lavoro. Questo script conta le cose che servono a decidere
come si agganciano:

  * quanti blocchi `if ( dbmode == DBMODE_DESC )`, cioe' quanti OGGETTI;
  * quante righe `description(N) = "..."` nel ramo jp e quante nel ramo else;
  * i blocchi ASIMMETRICI (il ramo jp e il ramo en non hanno gli stessi indici):
    li' la chiave `(riga, en)` non basta a ritrovare il giapponese;
  * le descrizioni che NON sono un letterale puro (interpolazione, `+`,
    variabili): quelle non le puo' toccare una sostituzione di stringa;
  * i doppioni di inglese, che dicono quanto lavoro e' ripetuto;
  * la lunghezza, che dice quanto pesa il lotto.

Legge il SORGENTE pinnato, non la build.
"""
import collections
import re

from strumenti.percorsi import SORGENTE_HSP

FILE = "db_item.hsp"

LETTERALE = re.compile(r'^\s*description\((\d+)\)\s*=\s*"(.*)"\s*$')
ASSEGNA = re.compile(r'^\s*description\((\d+)\)\s*=')


def blocchi_desc(righe):
    """Ogni blocco `if ( dbmode == DBMODE_DESC ) { ... }`, coi suoi due rami.

    Il confine si segue con le graffe come farebbe il compilatore, non a
    occhio: dentro il blocco ci sono altri `if`.
    """
    fuori = []
    n = 0
    while n < len(righe):
        if righe[n].strip().startswith("if ( dbmode == DBMODE_DESC )"):
            inizio = n
            profondita = righe[n].count("{") - righe[n].count("}")
            n += 1
            while n < len(righe) and profondita > 0:
                profondita += righe[n].count("{") - righe[n].count("}")
                n += 1
            fuori.append((inizio + 1, righe[inizio:n]))
        else:
            n += 1
    return fuori


def rami(corpo):
    """Le righe del ramo jp e quelle del ramo else, per indice di riga relativo."""
    jp, en, altri = [], [], []
    dove = None
    profondita = 0
    for i, riga in enumerate(corpo):
        nudo = riga.strip()
        if dove is None:
            if nudo == "if ( jp ) {":
                dove, profondita = "jp", 1
                continue
            if nudo == "else {":
                dove, profondita = "en", 1
                continue
            if ASSEGNA.match(riga):
                altri.append((i, riga))
            continue
        profondita += riga.count("{") - riga.count("}")
        if profondita <= 0:
            dove = None
            continue
        (jp if dove == "jp" else en).append((i, riga))
    return jp, en, altri


def voci(coppie, base):
    """Le assegnazioni a `description(N)`, separate fra letterali e non."""
    pure, sporche = [], []
    for i, riga in coppie:
        if not ASSEGNA.match(riga):
            continue
        m = LETTERALE.match(riga)
        if m:
            pure.append((base + i, int(m.group(1)), m.group(2)))
        else:
            sporche.append((base + i, riga.strip()[:100]))
    return pure, sporche


def main() -> None:
    righe = (SORGENTE_HSP / FILE).read_text(encoding="cp932").splitlines()
    blocchi = blocchi_desc(righe)

    tot_jp = tot_en = 0
    solo_jp = []
    asimmetrici = []
    sporche_tutte = []
    fuori_ramo = []
    inglesi = []

    for inizio, corpo in blocchi:
        r_jp, r_en, r_altri = rami(corpo)
        p_jp, s_jp = voci(r_jp, inizio - 1)
        p_en, s_en = voci(r_en, inizio - 1)
        p_altri, s_altri = voci(r_altri, inizio - 1)

        tot_jp += len(p_jp)
        tot_en += len(p_en)
        sporche_tutte += s_jp + s_en + s_altri
        fuori_ramo += p_altri
        inglesi += [(n, t) for n, _, t in p_en]

        if p_jp and not p_en:
            solo_jp.append(inizio)
        elif sorted(i for _, i, _ in p_jp) != sorted(i for _, i, _ in p_en):
            asimmetrici.append((inizio,
                                sorted(i for _, i, _ in p_jp),
                                sorted(i for _, i, _ in p_en)))

    print(f"blocchi DBMODE_DESC (= oggetti con descrizione) : {len(blocchi)}")
    print(f"righe description() letterali, ramo jp          : {tot_jp}")
    print(f"righe description() letterali, ramo en          : {tot_en}")
    print(f"assegnazioni FUORI dai due rami                 : {len(fuori_ramo)}")
    print(f"blocchi con jp e senza else                     : {len(solo_jp)}")
    if solo_jp:
        print("   ", ", ".join(f":{x}" for x in solo_jp[:12]))
    print(f"blocchi ASIMMETRICI (indici jp != indici en)    : {len(asimmetrici)}")
    for riga, a, b in asimmetrici[:12]:
        print(f"    :{riga}   jp {a}   en {b}")
    print(f"assegnazioni NON letterali                      : {len(sporche_tutte)}")
    for n, t in sporche_tutte[:12]:
        print(f"    :{n}  {t}")

    testi = [t for _, t in inglesi]
    doppi = [(t, c) for t, c in collections.Counter(testi).items() if c > 1]
    ripetute = sum(c for _, c in doppi) - len(doppi)
    print(f"inglesi distinti                                : {len(set(testi))}")
    print(f"inglesi ripetuti                                : {len(doppi)} testi, "
          f"{ripetute} righe che non sono lavoro nuovo")
    print(f"caratteri inglesi totali                        : {sum(len(t) for t in testi)}")
    if testi:
        lung = sorted(len(t) for t in testi)
        print(f"lunghezza inglese: mediana {lung[len(lung) // 2]}, "
              f"massima {lung[-1]}, minima {lung[0]}")

    indici = collections.Counter(i for _, corpo in blocchi
                                 for _, i, _ in voci(rami(corpo)[1], 0)[0])
    print("indici description(N) nel ramo en               :",
          ", ".join(f"{k}→{v}" for k, v in sorted(indici.items())))
    print(f"inglesi col marcatore di attribuzione `\\n#`     : "
          f"{sum(1 for t in testi if chr(92) + 'n#' in t)}")


if __name__ == "__main__":
    main()
