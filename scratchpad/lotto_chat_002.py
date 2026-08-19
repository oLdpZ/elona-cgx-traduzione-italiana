# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-002.jsonl: lo scontro con Orphe e la scena
dell'anniversario, cioe' quel che resta del perimetro 18560-18720 di chat.hsp.
Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.

Le rese portano gli accenti VERI, come vuole la guida di stile: la degradazione
ad apostrofo la fa applica.py durante la build.
"""
import io
import json
import pathlib

RESE = {
    # ------------------------------------------------------ *chat_unique_orphe
    18565: "Arrivi tardi. Ho appena finito di distruggere il Sigillo Eterno, "
           "sistema compreso. Anche se mi è costato un po' di fatica.",
    18566: "Orphe... hai intenzione di scatenare qui tutto il tuo potere divino?!",
    18567: "Perché non chiami anche gli altri dèi? Li strangolerò uno a uno, "
           "davanti ai tuoi occhi.",
    18568: "Non ce n'è bisogno. Avevamo previsto anche che il Sigillo Eterno "
           "fosse già distrutto, e ci siamo preparati. ...Splendi ora, zanna "
           "della luce nascente! Dammi la forza di fermare chi combatteva al "
           "mio fianco! Dammi la forza di espiare le colpe della Grande Guerra!",
    18589: "Orphe! Siamo noi a pronunciare la tua fine!",
    18590: "Ah, ecco: avete concentrato la forza di tutti gli dèi in una "
           "divinità sola. Mi risparmia fatica, ma mi toglie anche il "
           "divertimento.",
    18591: "Irregolare, che pena che tocchi anche a te una partita che non "
           "conta più niente. Non era previsto che arrivassi fin qui.",
    18592: "Metterò fine a tutto: a questo mondo e alla tua avventura.",
    # ------------------------------------------------- la scena dell'anniversario
    18720: "È il giorno speciale di noi due!",
    18721: "C'era qualcosa, oggi?",
    18722: "Ecco... è quella cosa, quella lì!",
    18723: "Non ha importanza.",
    18724: "L'ultimo giorno del mondo.",
    18725: "...Che giorno è oggi?",
    18734: "Eh già!",
    18737: '"(" + name(tc) + " è di ottimo umore!)"',
    18743: "...Niente!",
    18744: '"(" + name(tc) + " si mette di malumore, chissà perché)"',
    18749: "Quella lì!",
    18750: "Questa qui!",
    18751: "Quella là!",
    18752: "Che sia... un anniversario?",
    18753: "Com'era... ce l'ho sulla punta della lingua!",
    18754: "...E quale?",
    18757: "Basta così.",
    18758: '"(" + name(tc) + " non sa più che dire...)"',
    18764: "Come sarebbe, non ha importanza...!",
    18765: '"(" + name(tc) + " ci rimane male)"',
    18771: "Scusa, ho ancora il sonno addosso.",
    18772: "<È la fine...!>",
    18773: "Eh?!",
    18777: "Ehi, tu!",
    18781: "C'è ancora speranza! Battiamoci per il domani!",
}


def main():
    radice = pathlib.Path(__file__).resolve().parent.parent
    voci = []
    with io.open(radice / "lavoro" / "_chat.jsonl", encoding="utf-8") as f:
        for riga in f:
            d = json.loads(riga)
            if d["riga"] in RESE:
                d["it"] = RESE[d["riga"]]
                voci.append(d)
    mancanti = set(RESE) - {d["riga"] for d in voci}
    if mancanti:
        raise SystemExit("righe non trovate nel lotto: %s" % sorted(mancanti))
    voci.sort(key=lambda d: (d["riga"], d["occorrenza"]))
    # comporre, codificare in memoria, e solo allora aprire (lezione della 39a)
    dati = "".join(json.dumps(d, ensure_ascii=False) + "\n" for d in voci).encode("utf-8")
    with io.open(radice / "lavoro" / "fase4-chat-002.jsonl", "wb") as f:
        f.write(dati)
    print("%d voci scritte" % len(voci))
    for d in voci:
        print("  %d  %s" % (d["riga"], d["it"]))


if __name__ == "__main__":
    main()
