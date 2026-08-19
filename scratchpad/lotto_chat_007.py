# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-007.jsonl: due scene che nominano l'oblio e
l'Irregolare — la morte del vecchio mago di Eulderna (chat.hsp:10339-:10369),
che e' lo stesso che a :9504 «se l'e' sottomesso» una delle belve, e il colpo
di grazia di :15927-:15937.

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib

RESE = {
    # ------------------------------------- il vecchio mago di Eulderna e Nagarew
    10339: "Bel lavoro, ragazzi. Avete tenuto duro fino al mio arrivo. Al resto "
           "ci pensa questo vecchiaccio.",
    10340: "A ripensarci, è stata una vita votata alla magia. Per sfruttare il "
           "mio talento ho voltato le spalle al maestro e sono entrato "
           "nell'esercito, e ho combattuto senza pensare a niente... e quando "
           "me ne sono accorto ero vecchio.",
    10341: "Non morire!",
    10342: "Vuoi prenderti tu la scena?",
    10343: "L'incarnazione? La belva?",
    10344: "È il momento di usarla... la forza della belva, l'incarnazione del "
           "male!",
    10347: "Non muoio. Mi tocca soltanto qualcosa di molto peggio della morte.",
    10350: "Eh eh, scusate... Almeno alla fine lasciatemi fare la mia figura.",
    10353: "Come segno che un mondo sta per sparire, compare l'incarnazione "
           "della dea dell'oblio. Quelle cancellano il ricordo dalla gente, e "
           "così le persone e il mondo vengono dimenticati del tutto e "
           "incontrano la morte vera... Ebbene, una di quelle bestie la tengo "
           "in pugno io, con la magia.",
    10355: "Va', Nagarew! Brucia i miei ricordi e corrodi quella cosa!",
    10364: '"...(A quanto pare non capisce nemmeno più le parole)"',
    10369: "Ho consigliato a Sua Maestà di rivedere il modo in cui si trattano "
           "i maghi di grado basso, ma i valori della gente non cambiano tanto "
           "in fretta. Speriamo che cambino in meglio, anche poco per volta.",
    # ----------------------------------------------------- il colpo di grazia
    15927: "...? Ma guarda. Credevo fosse cenere che svolazza, e invece qui "
           "c'è ancora qualcosa che non ha finito di bruciare.",
    15928: "E con questo?",
    15929: "La partita non è ancora chiusa.",
    15930: "Farò vendetta.",
    15931: "Non sei che un mucchio di cenere, e vuoi ancora opporti? La "
           "differenza di forze è sotto gli occhi di tutti.",
    15934: "No. È la fine, Irregolare.",
    15937: "<ESTINZIONE>",
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
    dati = "".join(json.dumps(d, ensure_ascii=False) + "\n" for d in voci).encode("utf-8")
    with io.open(radice / "lavoro" / "fase4-chat-007.jsonl", "wb") as f:
        f.write(dati)
    print("%d voci scritte" % len(voci))
    for d in voci:
        print("  %d  %s" % (d["riga"], d["it"][:95]))


if __name__ == "__main__":
    main()
