"""Quante righe disegna DAVVERO la scheda di una carta.

`carte.righe_a_capo` modella `talk_conv` (init.hsp:1326-1367) ma ne salta il
blocco JAMES CUSTOM (:1337-1352), che manda a capo su un `\\n` gia' presente
nel testo. Nel sorgente HSP quel `\\n` sono due caratteri; nell'eseguibile e'
un ritorno a capo vero, e il gioco ci spezza la riga.

Questo script rifa il conto con il blocco dentro, e confronta.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strumenti import carte  # noqa: E402


def talk_conv(testo: str, colonna: int = carte.COLONNA_SCHEDA) -> str:
    """`init.hsp:1326-1367`, ramo non giapponese, blocco JAMES CUSTOM COMPRESO.

    `instr` torna l'indice; il codice ci somma 1, quindi `p` e `nl` sono
    lunghezze *incluso* il carattere cercato. `len` si azzera a ogni giro del
    ciclo esterno, e ogni `break` del ciclo interno ci torna: e' cosi' che una
    riga finisce.
    """
    resto, fuori, lunghezza = testo, "", 0
    for _ in range(1000):
        lunghezza = 0
        for _ in range(1000):
            spazio = resto.find(" ")
            p = 0 if spazio == -1 else spazio + 1
            if p == 0:
                break
            acapo = resto.find("\n")
            nl = 0 if acapo == -1 else acapo + 1
            if nl != 0 and nl < p:
                if lunghezza + nl > colonna:
                    fuori += "\n"
                    break
                fuori += resto[:nl]
                lunghezza += nl
                resto = resto[nl:]
                break
            if lunghezza + p > colonna:
                fuori += "\n"
                break
            fuori += resto[:p]
            lunghezza += p
            resto = resto[p:]
        if p == 0:
            break
    return fuori + resto


def disegnate(testo: str, prefisso: str) -> list[str]:
    """Le righe vere: `\\n` del sorgente -> ritorno a capo, accenti degradati."""
    vero = carte.degrada(prefisso + testo).replace("\\n", "\n")
    return talk_conv(vero).split("\n")


def main() -> int:
    righe = carte.leggi()
    diz = carte.carica_dizionario()
    peggio_it, peggio_en, salti = [], [], []
    for voce in carte.voci(righe):
        inglese = voce.get("en") or ""
        reso = diz.get(voce["costante"], {}).get("it")
        if not inglese or not reso:
            continue
        vere = disegnate(reso, carte.PREFISSO)
        stimate = carte._disegnate(reso)
        vere_en = disegnate(inglese, "Effect: ")
        peggio_it.append((len(vere), max(map(len, vere)), voce["costante"]))
        peggio_en.append((len(vere_en), voce["costante"]))
        if len(vere) != len(stimate):
            salti.append((len(stimate), len(vere), voce["costante"]))

    peggio_it.sort(reverse=True)
    peggio_en.sort(reverse=True)
    print("righe VERE, italiano  : massimo %d   (%s)"
          % (peggio_it[0][0], peggio_it[0][2]))
    print("righe VERE, inglese   : massimo %d   (%s)"
          % (peggio_en[0][0], peggio_en[0][1]))
    print("larghezza massima     : %d colonne" % max(x[1] for x in peggio_it))
    print()
    print("rese che il modello di `carte.py` conta CORTE: %d su %d"
          % (len(salti), len(peggio_it)))
    if salti:
        print("  peggiori (stimate -> vere):")
        for stimate, vere, costante in sorted(
                salti, key=lambda x: x[1] - x[0], reverse=True)[:10]:
            print("    %-32s %d -> %d" % (costante, stimate, vere))
    print()
    print("  le 10 rese piu' alte davvero:")
    for alte, largo, costante in peggio_it[:10]:
        print("    %-32s %d righe, %d colonne" % (costante, alte, largo))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
