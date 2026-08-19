# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-008.jsonl: gli ultimi due siti del perimetro dei
termini — la profuga di Raskilis e la profezia (chat.hsp:15438-:15470), e il
consiglio sull'Irregolare scambiato per un altro (:24411-:24417).

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib

RESE = {
    # ---------------------------------------- Raskilis, la valle e la profezia
    15438: "Un giorno stavo nella valle come sempre, e quella voce è arrivata "
           "da chissà dove.",
    15439: "Diceva di ritirarci subito fino all'imbocco della valle. Quando ho "
           "visto gli animali fuggire uno dopo l'altro, ho capito che il "
           "pericolo era vero. Mentre li seguivo mi sono voltata un attimo, e "
           "dal fondo della valle ho visto scaturire una bestia nera. Che "
           "spavento...",
    15440: "Appena siamo arrivati qui lo spazio si è richiuso, e ne è rimasta "
           "solo una fessura piccolissima. Se guardi dentro la fessura vedi il "
           "fondo della valle: ormai è pieno di bestie nere.",
    15441: "Ah, non è possibile...!",
    15442: "Poter vivere un mistero simile!! In questo momento sono commossa "
           "fino alle lacrime!!!",
    15452: "Scusa il disturbo.",
    15453: "Che cosa vuoi dire?",
    15454: "...Meshera......Il gigante che divora le stelle...Il vento...Oh, "
           "vento effimero......L'immunità della foresta...La foresta "
           "orrenda...Il corvo orrendo......Le cose come sono davvero..."
           "Morte...Rinascita...Rovina......Tenebra senza fine........."
           "Il falco bianco...L'albino......Disperazione...Vuoto...Che cosa si "
           "vedrà, oltre.........Sciagura...Il mondo che si sgretola......"
           "L'essere qual è...",
    15457: "...Il patto eterno......Caos...Il principe del regno perduto......"
           "La dea dell'oblio......Il destino interrotto...Il custode dello "
           "spazio e del tempo......Il mondo che non si dimentica......La "
           "storia che le fate raccontano.........Il figlio del Caos...La "
           "memoria del mondo......La luce di Arkasha...I legami......"
           "L'ultima speranza......La colonia che continua......Il mondo che "
           "viene creato......Il mare in capo al mondo...",
    15458: "...........(Oltre questo non si capisce più niente.)",
    15467: "È meglio mettersi al riparo.",
    15468: "Che cosa vendi?",
    15469: "Vorrei del pane appena sfornato.",
    15470: "Benvenuti a Raskilis.",
    # ------------------------------- il consiglio: scambiato per l'Irregolare
    24411: "Mi è arrivata voce che dentro le rovine un cavallo e un giovane sul "
           "livello 110 hanno aggredito qualcuno. Pare sia stato uno "
           "scambio di persona: cercavano un tale che chiamano l'Irregolare.",
    24412: "Di quei due, e di chi stanno cercando, non si sa il nome. Potrebbe "
           "toccare anche a te, quindi sta' in guardia.",
    24413: "Pare che il giovane, se ti ha a tiro, evochi degli spiriti. Può "
           "servire una cortina di fumo, oppure tagliare la linea di vista con "
           "la creazione di muri, o spazzarli via con una bacchetta di "
           "teletrasporto.",
    24414: "Gli spiriti lanciano uno sguardo che consuma MP... quindi, di "
           "nuovo: stare il meno possibile nel loro campo visivo evita di "
           "prendersi tutti i colpi insieme.",
    24415: "Se ti mettono nello stato in cui gli MP colano via di continuo sono "
           "guai, quindi conviene portarsi dietro parecchie pergamene o "
           "bacchette di mana per rimetterli a posto.",
    24416: "A proposito: il più forte dei due pare sia il cavallo. Se ti "
           "infilza col corno può scatenarsi un vortice caotico coi fiocchi. "
           "Chi ha subito l'attacco se l'è cavata solo perché aveva alzato la "
           "resistenza al caos: senza quella, sarebbe finita lì.",
    24417: "E comunque, tutti quanti hanno una bella resistenza al caos.",
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
    with io.open(radice / "lavoro" / "fase4-chat-008.jsonl", "wb") as f:
        f.write(dati)
    print("%d voci scritte" % len(voci))
    for d in voci:
        print("  %d  %s" % (d["riga"], d["it"][:95]))


if __name__ == "__main__":
    main()
