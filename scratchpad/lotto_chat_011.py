# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-011.jsonl: le schede dell'informatore su Lesimas
(chat.hsp:24357-:24380) — i non morti delle spedizioni, Gilphem, e Zeome.

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib

RESE = {
    # ------------------------------ i pericoli di Lesimas (2): i non morti
    24357: "Ti racconto una storia un po' spaventosa.",
    24358: "A Lesimas, fin dall'antichità, sono andate molte spedizioni, e ci "
           "hanno lasciato la vita. Ecco: escono. I non morti delle squadre di "
           "esplorazione.",
    24359: "Non si sono accorti di essere morti e continuano a esplorare ancora "
           "oggi. Chi li ostacola si ritrova il corpo paralizzato, e muore "
           "torturato dal soffio d'oltretomba. E per quanto ti dibatta, agli "
           "spettri dentro la nebbia gli attacchi non arrivano...",
    24360: "...Con un equipaggiamento che annulla la paralisi, o con la magia "
           "Pietra protettrice, o con una pozione di gemma, si può prevenire, "
           "no? Certo, se hai basse le resistenze ai nervi e all'oltretomba, il "
           "danno potresti non reggerlo.",
    24361: "Essendo non morti, il fuoco li fa soffrire: con un attacco potente "
           "d'elemento fuoco secondo me è vinta facile. Al contrario oscurità, "
           "oltretomba e nervi non fanno niente. Pare che tirino fuori una "
           "nebbia che fa mancare i colpi fisici, ma la nebbia si disperde con "
           "le molotov o con le ragnatele.",
    # ------------------------------ i pericoli di Lesimas (3): Gilphem
    24365: "Zeome era un mago famoso perfino a Palmia. Una delle sue ricerche "
           "era un guardiano a congegno magico dotato di mente. Il nome, se non "
           "sbaglio, era... Gilphem, la sentinella d'acciaio magico.",
    24366: "Ai tempi in cui stava con la casa reale non riusciva a portarlo a "
           "termine, e ci si tormentava. E se uno così mettesse le mani sulla "
           "massa di informazioni dell'<occhio delle tenebre eterne>? Ovvio: "
           "Gilphem l'ha finito.",
    24367: "Già in fase di ricerca gli avevano messo le contromisure contro la "
           "magia, e le magie d'elemento magia... il Dardo magico soprattutto..."
           " non facevano proprio niente. Con magie di altro elemento forse "
           "qualcosa si ottiene.",
    24368: "Nei documenti il progetto partiva da un'armatura, quindi anche gli "
           "attacchi normali servono a poco. Con le abilità c'è da sperare che "
           "passino.",
    24369: "Sembra fatto per difendersi, ma c'è anche un rapporto che dice che, "
           "quando si è indebolito, si è tolto da solo i dispositivi di "
           "sicurezza e si è scatenato. Se si scatena non scappare per lo "
           "spavento: spingi fino in fondo e distruggilo.",
    # ------------------------------------------- il boss di Lesimas: Zeome
    24373: "Zeome il falso profeta conviene ormai considerarlo un mostro. Già "
           "prima di farsi ammaliare da Lesimas era un mago capace di evocare "
           "mostri, di governare il vortice caotico e di rimarginarsi in un "
           "attimo anche le ferite profonde. E adesso il potere magico di "
           "Lesimas l'ha senz'altro rinforzato.",
    24374: "Il guardiano che c'era prima di Zeome pare fosse di livello 55, "
           "quindi Zeome oggi starà lì intorno. E c'è anche un rapporto che "
           "dice che nella camera del tesoro di Lesimas ha preso una falce che "
           "fa volare e amplifica la magia. Senza resistenza al caos, per "
           "quanta gente ti porti dietro, in un attimo siete spazzati via.",
    24375: "Se ti chiudi intorno un muro con la magia o con la bacchetta di "
           "creazione di muri, evocare mostri gli diventa difficile. Però anche "
           "a chiudersi con calma, intanto gli attacchi bisogna reggerli.",
    24376: "Se può servire: Zeome di allora tendeva ad avvicinarsi in linea "
           "retta e a cercare il corpo a corpo. Se è rimasto così, forse lo "
           "puoi guidare dove vuoi tu, o seminarlo accelerando.",
    24377: "C'è anche il problema di superare la sua magia di cura. Se vuoi "
           "fargli finire gli MP, procurati armi e abilità che li consumano e "
           "mettiti in guerra di logoramento.",
    24378: "Se invece vuoi fare più danno di quanto lui ne recuperi, la via "
           "solida è portare la barra di potenza oltre il 100% e scaricargliela "
           "addosso tutti insieme coi compagni, con <Forza liberata> o con "
           "<Attacco combinato>. I compagni fuori dall'ordine di Assalto "
           "tengono da parte la barra, quindi regola i tempi.",
    24379: "Se li fai infuriare tirandogli addosso pomodori marci, natto o "
           "yogurt, il danno raddoppia; ma raddoppia anche quello che prendono, "
           "quindi va visto quanto regge la tua squadra. Poi... o gli fai "
           "passare per forza la magia Nebbia di silenzio. Senza un livello di "
           "magia sufficiente non c'è speranza.",
    24380: "Se ti va bene e metti le mani sull'<occhio delle tenebre eterne>, "
           "dividi un po' di informazioni anche con me. In bocca al lupo.",
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
    with io.open(radice / "lavoro" / "fase4-chat-011.jsonl", "wb") as f:
        f.write(dati)
    doppi = set("—–“”«»…・《》")
    guasti = [d["riga"] for d in voci if doppi & set(d["it"])]
    print("%d voci scritte | caratteri a due byte: %s" % (len(voci), guasti or "nessuno"))


if __name__ == "__main__":
    main()
