# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-004.jsonl: il filo di Gaius Vis, prima meta'
(chat.hsp:9423-:9474) — i doni di Loyter, l'arrivo nel mondo gemello, le
bestie dell'oblio e il lume della memoria.

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib

RESE = {
    9423: "Parli del padre ignoto, del nostro primo padre: <Propator "
          "dell'Abisso>. Anche noi ne sappiamo una cosa sola, che è \\\"un "
          "essere trascendente che nessuno potrà mai conoscere, in eterno\\\". "
          "Noi in qualche modo ci siamo rassegnati; Sophia, allora, non ci "
          "riuscì. Avere in mano la sapienza e non sapere niente del proprio "
          "padre: dev'essere stata un'angoscia da impazzire.",
    9434: "C'è una cosa che voglio darti.",
    9436: "Ottieni la [collana di Elsia] e il [biglietto per la <Regina "
          "Sedona>]!",
    9438: "Appartenevano all'ultimo viandante che ho guidato in questa terra. "
          "Nell'ultimo ciclo, in fin di vita, me li ha affidati.",
    9439: "Non ti serviranno a niente, probabilmente. Eppure voglio che li "
          "tenga tu, perché non conosco nessun altro che li meriti.",
    9440: "In bocca al lupo.",
    9441: "Che imbarazzo.",
    9442: "Ehi, piantala, scemo.",
    9443: "(Un pugno nello stomaco, senza dire niente.)",
    9444: "...Bene, io vado a raccontare di Gaius Vis alla gente di Irva. Ah, "
          "giusto! E già che ci sono dirò a tutti quelli che conosci che ti "
          "batti contro il Caos!",
    9448: '"Bgheh?! Ma che fai, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + "?!"',
    9455: "Ecco! In questo istante hai messo piede per la prima volta a Gaius "
          "Vis!",
    9456: "Quanta strada... In questo mondo è passato sì e no un anno, ma io, "
          "contando i cicli, ci lavoro da più di dieci. Alla fine il Fattore "
          "Decisivo l'ho trovato, e sei tu: e sono riuscito a portarti qui.",
    9457: "Mmh. Però la tua percezione non ha ancora seguito il salto fra le "
          "dimensioni. Probabilmente ai tuoi occhi molte cose appariranno "
          "sostituite da cose di Irva.",
    9458: "Dunque... a quanto vedo, le bestie dell'oblio dilagano ancora... "
          "Chissà se quella persona sta bene. Andiamo a cercarla insieme!",
    9459: "Eh? Chi sarebbe \\\"quella persona\\\", dici? Ah, giusto: non te "
          "l'ho ancora spiegato.",
    9460: "Sophia la conosci, no? La divinità di medio rango che ha in mano la "
          "sapienza. Ebbene, quella persona è un dio trascendente: ventotto "
          "fra i fratelli e le sorelle di Sophia, fusi in uno solo. Pare fosse "
          "una contromisura contro il dio del Caos, che di divinità ne aveva "
          "assorbite parecchie. E pare che Sophia, per via di quella volta che "
          "cadde dal cielo, nella fusione non sia riuscita a entrare bene.",
    9461: "Quella persona ha saputo com'è ridotta Gaius Vis, e ci ha agevolati "
          "in molti modi. Adesso dovrebbe essere in prima linea contro la dea "
          "dell'oblio. E finché io me ne ricordo così, come adesso, vuol dire "
          "per forza che sta bene. Almeno, dovrebbe...",
    9462: "Se a un certo punto vuoi tornare indietro, passa dal Loyter di "
          "questo lato. Dovrebbe stare nella città mineraria qui vicino... "
          "Zaile.",
    9469: "Ah, giusto: avevo una cosa da darti.",
    9471: "Ottieni il [lume della memoria]!",
    9473: "È una massa di luce astrale che registra le informazioni della vita. "
          "Tiene una copia dei ricordi, quindi pare che attutisca parecchio "
          "gli attacchi che cancellano la memoria.",
    9474: "E poi è anche uno strumento per andare da un mondo all'altro. Prova "
          "a usarlo rivolto verso Loyter: al momento non c'è nessuno legato a "
          "Gaius Vis più di lui. Anche dall'altra parte esiste qualcuno che "
          "gli somiglia moltissimo, e il lume della memoria illumina quel "
          "legame e ti ci porta.",
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
    with io.open(radice / "lavoro" / "fase4-chat-004.jsonl", "wb") as f:
        f.write(dati)
    print("%d voci scritte" % len(voci))
    for d in voci:
        print("  %d  %s" % (d["riga"], d["it"]))


if __name__ == "__main__":
    main()
