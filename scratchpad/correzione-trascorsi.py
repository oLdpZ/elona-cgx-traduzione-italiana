# -*- coding: utf-8 -*-
"""Le righe dei trascorsi che uscivano dalla finestra della creazione.

Trovate a schermo nella 64a: nella schermata «Sorteggio dei trascorsi» due righe
su cinque uscivano dal bordo destro della pergamena, sul marmo nudo -- misurate
+45 px e +31 px. Il tetto e' quello di [[trascorsi.py]], la rete 17: **38
caratteri**, da `chara.hsp:3305` (finestra larga 360, testo a `wx + 75`, `mes`
che non taglia).

⚠️ **Non si toccano le righe che sfora anche l'inglese di monte**, come per i
nomi di mappa nella 62a. Il conto:

    fuori misura in italiano                       74 su 226
      di cui l'inglese sta dentro (nostre)         16
      di cui sforiamo PIU' dell'inglese            12
      di cui sfora anche l'inglese, e meno di noi  46   <- non si toccano
    -----------------------------------------------------
    perimetro                                      28

Upstream qui sfonda per conto suo: 97 righe su 226, fino a 61 caratteri, perche'
la finestra e' dimensionata sul giapponese (frasi da 14 caratteri a 14 px) e
l'inglese ci e' stato messo dentro dopo. In media stiamo gia' meglio -- 34,4
caratteri contro 36,6 -- e queste 28 sono la coda che non ha scuse di monte.

⚠️ **La lunghezza si conta sulla forma DEGRADATA**, non su quella del
dizionario: `applica` scrive «perche'» dove il dizionario dice «perché», e
l'apostrofo e' un carattere in piu'. Contare gli accenti veri fa sbagliare il
tetto di uno per ogni accento.

⚠️ Si compone in memoria e si scrive solo alla fine (regola della 39a).
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import trascorsi as T
from strumenti.accenti import degrada

PERCORSO = "dizionario/command.hsp.jsonl"

# riga del sorgente -> resa nuova. La riga fa da chiave, il vecchio testo da
# guardia: se il dizionario non lo dice piu', lo script si ferma.
NUOVE = {
    # --- setHistory1, le origini ------------------------------------------
    9522: "La distruzione del proprio paese.",
    9528: "Un passato da signore locale.",
    9534: "Creatura maledetta, poi l'abbandono.",
    9537: "Avventurieri da generazioni.",
    9540: "Una famiglia di nobili cavalieri.",
    9549: "Una famiglia di guerrieri decaduti.",
    9555: "Un ex militare, l'animo ferito.",
    9591: "Un avventuriero distrusse il paese.",
    # --- setHistory2, perche' si e' partiti -------------------------------
    9600: "In viaggio senza un vero perché.",
    9621: "In viaggio per farsi più forti.",
    9624: "Un ordine: girare i vari paesi.",
    9702: "Il transito da un portale ignoto.",
    9717: "L'accusa di inutilità, e il bando.",
    # --- setHistory3 e 4, il carattere (le seconde parti sono minuscole) --
    9846: "Mai la guardia bassa, ma",
    9876: "nessuna sensibilità per l'affetto.",
    9882: "disprezzo per gli altri.",
    9930: "lo sbaglio nel momento decisivo.",
    9936: "pessime maniere con il vino.",
    # --- setHistory5, i gusti ---------------------------------------------
    10005: "le cose sgradite si rimandano.",
    10011: "Passatempo: le macchine.",
    10020: "Che piacere, una faccia nel dolore.",
    10050: "I ricordi di una vita passata.",
    10113: "Nulla fa paura come il tradimento.",
    10119: "In fondo, il sogno è la quiete.",
    10122: "Un desiderio: farsi ridurre a pezzi.",
    10128: "Vuoti di memoria inspiegabili.",
    10131: "I torti a tavola non si scordano.",
    10140: "Meglio i germogli dei funghi.",
}


def perimetro():
    """{riga del sorgente: (vecchio italiano, inglese)} per le righe da accorciare."""
    sorgente = {(b, n): t for b, n, t in T.righe(T.SORGENTE)}
    build = {(b, n): t for b, n, t in T.righe(T.BUILD)}
    fuori = {}
    for k, it in build.items():
        en = sorgente.get(k, "")
        if len(it) > T.TETTO and (len(en) <= T.TETTO or len(it) > len(en)):
            fuori[k[1]] = (it, en)
    return fuori


def main():
    da_fare = perimetro()
    print(f"il referto nomina {len(da_fare)} righe da accorciare")

    # 1. il tavolo delle rese nuove regge il tetto, in forma degradata?
    guai = []
    for riga, resa in NUOVE.items():
        if riga not in da_fare:
            guai.append(f"la riga {riga} non sta fra quelle da accorciare")
            continue
        quanto = len(degrada(resa))
        if quanto > T.TETTO:
            guai.append(f"«{degrada(resa)}» e' {quanto}, il tetto e' {T.TETTO}")
    for riga in sorted(set(da_fare) - set(NUOVE)):
        guai.append(f"la riga {riga} non ha una resa nuova: «{da_fare[riga][0]}»")
    if guai:
        for g in guai:
            print("  ⚠️", g)
        raise SystemExit("il tavolo non e' a posto: non tocco niente")

    # 2. si compone in memoria, e si scrive solo alla fine
    righe = []
    fatte = 0
    with open(PERCORSO, encoding="utf-8") as f:
        for l in f:
            if not l.strip():
                continue
            d = json.loads(l)
            resa = NUOVE.get(d["riga"])
            if resa is not None and degrada(d["it"]) == da_fare[d["riga"]][0]:
                d["it"] = resa
                fatte += 1
            righe.append(json.dumps(d, ensure_ascii=False))

    if fatte != len(NUOVE):
        raise SystemExit(f"attese {len(NUOVE)} voci, cambiate {fatte}: non scrivo niente")

    testo = "\n".join(righe) + "\n"
    io.open(PERCORSO, "w", encoding="utf-8", newline="").write(testo)
    print(f"cambiate {fatte} voci")


if __name__ == "__main__":
    main()
