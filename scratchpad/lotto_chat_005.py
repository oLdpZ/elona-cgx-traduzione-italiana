# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-005.jsonl: il filo di Gaius Vis, seconda meta'
(chat.hsp:9481-:9519) — il racconto del mondo perduto, l'incarnazione
dell'oblio, i cicli, e la scena dell'extraterrestre.

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib

RESE = {
    9481: "Su, è arrivato il momento!",
    9483: "Sì!",
    9484: "Non me lo ricordo.",
    9485: "Ho bisogno del tuo aiuto. Ti ricordi quello di cui abbiamo parlato, "
          "vero?",
    9488: "Il potere della dea dell'oblio arriva perfino fin qui! Ormai sembra "
          "che il tempo sia finito...",
    9490: "Voglio che tu venga alla taverna di Vernis. Fra i posti che restano, "
          "quello è il punto in cui il legame è più forte.",
    9495: "Quando verrà quel momento, vorrei che dessi una mano anche tu. E "
          "vorrei che ti ricordassi di quel che ti ho detto su Gaius Vis: "
          "perché una persona, come un mondo, muore davvero solo quando "
          "nessuno se la ricorda più.",
    9498: "Ah, finalmente libero: quell'extraterrestre te lo sei preso tu. "
          "Allora vengo al punto... Voglio che tu sappia qual è la vera "
          "minaccia.",
    9499: "In realtà io non sono nato in questo mondo: vengo da un altro mondo, "
          "che si chiama Gaius Vis. Sono di una stirpe speciale, dentro il "
          "popolo delle fate: gli Elun, che di là, storpiando il nome, "
          "chiamavano anche elfi.",
    9500: "Gaius Vis è il mondo gemello di Irva. Anche lì soffia il vento "
          "d'etere, e anche lì la gente voleva estirpare la Foresta Eretica. "
          "Ma proprio in quel momento è arrivata di colpo l'incarnazione "
          "dell'oblio: il 95% del mondo è sparito dall'esistenza insieme al "
          "ricordo di sé, e Gaius Vis è finita. Che cosa ci fosse nella parte "
          "scomparsa, che gente ci vivesse, non riesco più a ricordarlo "
          "nemmeno io.",
    9501: "E in quel momento, mentre disperavo, davanti a me è comparsa quella "
          "persona! Con la sua forza ho riavvolto il tempo e ho cercato di "
          "cambiare il destino. Ho guidato molti viandanti che potevano "
          "diventare Irregolari, e ho combattuto al loro fianco molte volte. "
          "In quelle battaglie si è risvegliata anche la forza di Norne, la "
          "dea del destino, che è mia antenata. E ho collaborato con i "
          "discendenti dei giganti e dei nani, che di quella dea hanno il mio "
          "stesso sangue.",
    9502: "Ma per quante migliaia di volte lo rifacessi, niente! Sono riuscito "
          "a salvare l'esistenza di una città sola e di poco altro intorno; "
          "sulla gran parte del mondo, che era destinata a sparire, non ho "
          "potuto nemmeno intervenire. I viandanti che avevo guidato non "
          "arrivavano da nessuna parte: si logoravano, smettevano di pensare, "
          "e alla fine sparivano sempre nel mare dell'oblio. Lo capisci, "
          "questo sconforto? Questa rabbia?",
    9503: "E poi quella persona me l'ha detto: anche Irva, il mondo gemello, è "
          "nel mirino dell'incarnazione dell'oblio. La tragedia di Gaius Vis "
          "non deve ripetersi. Con questo in testa ci siamo trasferiti da "
          "questa parte e abbiamo cominciato a preparare la difesa. Dai molti "
          "mondi che l'incarnazione dell'oblio ha distrutto abbiamo raccolto i "
          "sopravvissuti, e li abbiamo messi insieme come fattori di mutamento "
          "del destino.",
    9504: "E così siamo riusciti a respingere la loro avanguardia. Uno "
          "l'abbiamo cancellato del tutto; un altro se l'è sottomesso il "
          "vecchio mago di Eulderna, e lo tiene a bada. Ne resta uno, mezzo "
          "morto, che pare si nasconda a Tyris del Sud: ma quello la sua forza "
          "vera non la riprende più, quindi non è un problema.",
    9505: "Ma la faccenda non è chiusa. Il destino si è aggiornato appena "
          "appena. Loro sono l'oblio stesso, come concetto... prima o poi il "
          "grosso delle loro forze arriverà, e il mondo è destinato a finire. "
          "Lo so bene. E fino all'ultimo mi ci opporrò con le unghie e coi "
          "denti. Sì: con qualunque mezzo.",
    9510: "Ah! Arrivi al momento giusto. Stavo scendendo qui e mi si è "
          "attaccato un extraterrestre che non conosco. Insiste perché sono "
          "una guida, ma io che ne so di chi cerca un extraterrestre. E chi "
          "sarebbe un ragazzo dai capelli neri di nome Kuroya?",
    9511: "Avrei una cosa da dirti, ma... prima portami via di qui "
          "quell'extraterrestre insistente. È una seccatura.",
    9517: "Andiamo.",
    9518: "Lascia stare.",
    9519: "Vuoi andare a Tyris del Nord?",
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
    with io.open(radice / "lavoro" / "fase4-chat-005.jsonl", "wb") as f:
        f.write(dati)
    print("%d voci scritte" % len(voci))
    for d in voci:
        print("  %d  %s" % (d["riga"], d["it"][:100]))


if __name__ == "__main__":
    main()
