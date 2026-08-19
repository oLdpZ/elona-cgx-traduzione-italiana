# -*- coding: utf-8 -*-
"""Il ciclo di `random_title` rifatto fedelmente, per capire dove si ferma.

⚠️ Nato nella 65a perche' il gioco si BLOCCA su «Generate an Adventurer», cioe'
sulla prima finestra della creazione (`chara.hsp:3207`), che chiama
`random_title()` diciassette volte. La 64a aveva provato la grammatica in
Python e l'eseguibile **solo all'avvio**: il generatore nel motore non l'aveva
mai girato nessuno.

⭐ La regola della 61a: si prova sull'INGLESE DI MONTE, dove si sa gia' che cosa
deve venire fuori. Se il simulatore non sa riprodurre l'inglese, non dice niente
sull'italiano.

Differenza dagli altri: `epiteti.py` SCOMPONE epiteti gia' visti a schermo,
questo li COMPONE contando i giri. Serve a rispondere a una domanda sola:
quante volte gira il ciclo prima di dare una risposta, e puo' non darla mai?
"""
import sys
from pathlib import Path

DATI = Path(r"C:\Games\Elona\elonaplus2.31\data")
MARK_JOLLY = "\u4e07\u80fd"  # 万能, la categoria jolly che salta il controllo


def griglia(nome):
    """rnlist come lo costruisce *random_titleInit: [colonna][riga]."""
    testo = (DATI / nome).read_bytes().decode("cp932", "replace")
    righe = testo.split("\r\n") if "\r\n" in testo else testo.split("\n")
    if righe and righe[-1] == "":
        righe.pop()
    tabella = []
    for riga in righe:
        campi = riga.split(",")
        campi += [""] * (15 - len(campi))
        tabella.append(campi[:15])
    return tabella


class Motore:
    """Il ciclo di etc.hsp, con un contatore di giri al posto del blocco."""

    def __init__(self, rnlist, rnlist2, italiano, tetto_giri=200000):
        self.g = rnlist
        self.g2 = rnlist2
        self.it = italiano
        self.tetto_giri = tetto_giri
        self.nrighe = len(rnlist)
        self.giri_esterni = 0
        self.giri_interni = 0

    def rnd(self, n):
        import random
        return random.randrange(n)

    def genera(self, arg1=0):
        """Ritorna (epiteto, giri_esterni) oppure (None, giri) se non converge."""
        esterni = 0
        while True:
            esterni += 1
            self.giri_esterni += 1
            if esterni > self.tetto_giri:
                return None, esterni

            # repeat 1 / continue cnt: ripesca finche' la cella non e' vuota
            interni = 0
            while True:
                interni += 1
                self.giri_interni += 1
                if interni > self.tetto_giri:
                    return None, esterni
                p2 = self.rnd(self.nrighe)
                p1 = self.rnd(10 if self.it else 14)
                if self.g[p2][p1] != "":
                    break

            if arg1 in (1, 3):
                if self.g[p2][14] == "\u5973":
                    continue

            randn2_0 = self.g[p2][p1]
            randn2_1 = self.g[p2][14]
            rtval = -1

            if self.it:
                randn2_0 = ""          # TOPPA IT
            else:
                # il ramo inglese di monte: A of B / the A / A B
                if p1 in (0, 1):
                    if self.rnd(6) == 0:
                        randn2_0 += " of"
                    elif self.rnd(6) == 0:
                        randn2_0 = "the " + randn2_0
                        rtval = 1
                if rtval != 1:
                    randn2_0 += " "

            if rtval == 1:
                return randn2_0, esterni

            rtval = -1
            col1 = p1
            for _ in range(100):
                p4 = self.rnd(self.nrighe)
                if p4 == p2:
                    continue
                if self.g[p4][14] == randn2_1:
                    if self.g[p4][14] != MARK_JOLLY:
                        if randn2_1 != MARK_JOLLY:
                            continue
                if p1 < 10:
                    p1 = self.rnd(2)
                else:
                    p1 = self.rnd(2) + 10
                if self.g[p4][p1] == "":
                    continue
                rtval = 1
                break

            if rtval == -1:
                continue

            if self.it:
                s = self.g[p4][p1] + " " + self.g2[p2][col1]
            else:
                s = randn2_0 + self.g[p4][p1]

            if len(s.encode("cp932", "replace")) >= (36 if self.it else 28):
                continue
            return s, esterni


def prova(nome, motore, quanti=200):
    falliti = 0
    campioni = []
    peggio = 0
    for _ in range(quanti):
        s, giri = motore.genera()
        peggio = max(peggio, giri)
        if s is None:
            falliti += 1
        elif len(campioni) < 12:
            campioni.append(s)
    print(f"--- {nome} ---")
    print(f"  righe nella griglia : {motore.nrighe}")
    print(f"  epiteti chiesti     : {quanti}")
    print(f"  NON convergiuti     : {falliti}")
    print(f"  giri esterni totali : {motore.giri_esterni}   (peggiore: {peggio})")
    print(f"  giri interni totali : {motore.giri_interni}")
    for c in campioni:
        print(f"      {c}")
    print()
    return falliti


def main():
    import random
    random.seed(12345)

    e = griglia("ndata-e.csv")
    i = griglia("ndata-i.csv")
    i2 = griglia("ndata-i2.csv")

    falliti_en = prova("INGLESE DI MONTE (rnd(14), ndata-e.csv)",
                       Motore(e, e, italiano=False), 200)
    falliti_it = prova("ITALIANO TOPPATO (rnd(10), ndata-i.csv + i2)",
                       Motore(i, i2, italiano=True), 200)

    if falliti_en:
        print("!! il simulatore non riproduce nemmeno l'inglese: non dice niente")
        return 2
    if falliti_it:
        print("!! l'italiano NON converge: e' il blocco")
        return 1
    print("tutt'e due convergono")
    return 0


if __name__ == "__main__":
    sys.exit(main())
