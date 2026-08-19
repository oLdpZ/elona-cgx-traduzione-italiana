# -*- coding: utf-8 -*-
"""Le righe dei trascorsi che si sovrappongono nella SCHEDA del personaggio.

Il secondo sito dei trascorsi, trovato nella 65a: `command.hsp:10539` e gli
altri quattro passano la riga da `talk_conv s, 32`, che manda a capo, e
disegnano l'avanzo a **+7 px** dove il passo fra una voce e l'altra e' **15**.
La seconda riga finisce *sopra* la voce successiva.

Il tetto e' quello di [[trascorsi.py]], la rete 17, **sito B**: la riga deve
venire di **una riga sola**.

⚠️⚠️ **La 65a aveva contato 24 righe da riparare, e sono 7.** Il conto era
`len() > 32`, ma `talk_conv` (`init.hsp:1326`) e' un a-capo greedy sulle parole
e **l'ultimo pezzo dopo l'ultimo spazio viene appeso senza controllo**: va a
capo se e solo se

    coda = somma di (len(parola) + 1) su tutte le parole TRANNE L'ULTIMA  >  32

La lunghezza totale non c'entra. Tre delle sette hanno l'inglese di monte **piu'
lungo del nostro** e stanno lo stesso in una riga, perche' finiscono con una
parola lunga:

    en 45  Though have a strong sense of responsibility,   coda 30 -> 1 riga
    it 44  Un senso di responsabilita' come nessuno, ma    coda 42 -> 2 righe

💡 La leva non e' accorciare la riga: e' **portare a 32 la coda**. Tutte e sette
finiscono con «ma», che di coda ne lascia due, quindi qui vuol dire stare in 34
caratteri in tutto.

⚠️ **Non si toccano le righe che vanno a capo anche in inglese**: sono 42 in
italiano contro 82 di monte, e le altre 35 hanno le scuse di monte. Restano
lavoro possibile, non perimetro.

⚠️ **La lunghezza si conta sulla forma DEGRADATA**: `applica` scrive «perche'»
dove il dizionario dice «perché», e l'apostrofo e' un carattere in piu'.

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
# Tutte in *setHistory3, la prima meta' della frase sul carattere.
NUOVE = {
    # Though you are the life of the party,
    9756: "Allegria che contagia tutti, ma",
    # Though good at supporting others,
    9780: "Un gran talento nell'aiutare, ma",
    # Though enduring hardships,
    9783: "Tempra contro le sventure, ma",
    # Though adapt to different environments,
    9792: "Adattamento a ogni ambiente, ma",
    # Though have a strong sense of responsibility,
    9804: "Responsabilità come nessuno, ma",
    # Though doesn't sweat the small stuff,
    9840: "Nessun pensiero per le inezie, ma",
    # Though work hard for others,
    9858: "Ogni sforzo è per gli altri, ma",
}


def perimetro():
    """{riga del sorgente: (vecchio italiano, inglese)} per le righe da riparare."""
    sorgente = {(b, n): t for b, n, t in T.righe(T.SORGENTE)}
    build = {(b, n): t for b, n, t in T.righe(T.BUILD)}
    sfora = lambda t: len(T.talk_conv(t, T.A_CAPO)) > T.TETTO_RIGHE
    nostre, peggio = T.perimetro(sorgente, build, sfora,
                                 lambda t: len(T.talk_conv(t, T.A_CAPO)))
    return {k[1]: (it, en) for k, en, it in nostre + peggio}


def main():
    da_fare = perimetro()
    print(f"il referto nomina {len(da_fare)} righe da riparare")

    # 1. il tavolo delle rese nuove sta in una riga sola, in forma degradata?
    guai = []
    for riga, resa in NUOVE.items():
        if riga not in da_fare:
            guai.append(f"la riga {riga} non sta fra quelle da riparare")
            continue
        degradata = degrada(resa)
        quante = len(T.talk_conv(degradata, T.A_CAPO))
        if quante > T.TETTO_RIGHE:
            guai.append(f"«{degradata}» viene in {quante} righe: "
                        f"coda {T.coda(degradata)}, il tetto e' {T.A_CAPO}")
        if len(degradata) > T.TETTO_CREAZIONE:
            guai.append(f"«{degradata}» e' {len(degradata)} caratteri: sfora il "
                        f"sito A, tetto {T.TETTO_CREAZIONE}")
    for riga in sorted(set(da_fare) - set(NUOVE)):
        guai.append(f"la riga {riga} non ha una resa nuova: «{da_fare[riga][0]}»")
    if guai:
        for g in guai:
            print("  ⚠️", g)
        raise SystemExit("il tavolo non e' a posto: non tocco niente")

    for riga, resa in sorted(NUOVE.items()):
        vecchio = da_fare[riga][0]
        d = degrada(resa)
        print(f"   {riga}  coda {T.coda(vecchio):3d} -> {T.coda(d):3d}   "
              f"{vecchio}  ->  {d}")

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
