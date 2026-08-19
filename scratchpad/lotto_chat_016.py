# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-016.jsonl: le ultime schede dell'informatore —
Tezcatlipoca, il boss della Culla del Caos su cui nemmeno lui ha notizie, e il
rito del lupo mannaro (chat.hsp:24516-:24537).

Con questo lotto il PNG e' chiuso per intero: chat.hsp:24236-:24537.

⚠️ :24534 e :24535 portano un `\\n` LETTERALE dentro la stringa inglese (due
caratteri, non un a capo): va tenuto, e negli stessi punti in cui sta l'inglese.

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib

RESE = {
    # ------------------------------------------------------- Tezcatlipoca
    24516: "Anche a te Tezcatlipoca ha detto di andare al Sigillo Eterno, eh?",
    24517: "Dalle mie ricerche, Tezcatlipoca un tempo era un dio che stava alla "
           "pari con Ehekatl. Ma adesso, dicono, gli hanno confiscato la forza "
           "ed è caduto fino al livello 200.",
    24518: "È il dio della notte, del fumo e della guerra, quindi potrebbe usare "
           "la tattica di spargere fumo, farti girare a vuoto e colpirti al "
           "buio. Se non hai qualcosa che spanda su un'area larga colonne di "
           "fuoco, ragnatele o Nebbia d'oscurità, o delle esplosioni per "
           "spazzare via il fumo, le prendi e basta.",
    24519: "Non ne sono sicuro, ma probabilmente conviene avere resistenza al "
           "caos e resistenza mentale.",
    24520: "Lo specchio che porta addosso, dicono, resiste al caos e alla magia, "
           "e riflette anche una parte delle altre magie. Puntando soprattutto "
           "sull'attacco magico farai fatica, quindi tieni pronti anche oggetti "
           "e abilità d'attacco che possano servire. Se proprio vuoi attaccare "
           "con la magia, usa qualcosa che non sia caos né elemento magia. E "
           "non dimenticare di alzare anche la tua resistenza a quegli "
           "elementi.",
    # ------------------------------ il boss della Culla: nemmeno lui lo sa
    24524: "Qui davvero le informazioni sono troppo poche e non ci arrivo. Ma "
           "non faccio l'informatore da tanti anni per finta. Fammici pensare "
           "un attimo.",
    24525: "Intanto sarà legato e non potrà muoversi, ma potrebbe tirarti a sé "
           "col potere magico, quindi niente distrazioni. Con un "
           "equipaggiamento che impedisce il teletrasporto forse non c'è "
           "nemmeno da preoccuparsi.",
    24526: "Dato che governa il caos, la resistenza al caos ce l'avrà alta, ed è "
           "pensabile che evochi spiriti del caos. Meglio prepararsi contro le "
           "evocazioni e con un modo per recuperare MP.",
    24527: "Anche i suoi attacchi saranno soprattutto d'elemento caos? No, "
           "potrebbe usare anche altro, e avere tutte le resistenze in ordine "
           "non fa male. I buchi che restano spero si tappino con una pozione "
           "di resistenza.",
    24528: "Se ti trovi davanti uno che ti ammazza solo ad avvicinarti per "
           "sbaglio, ci sta anche scappare in tondo per capire gli schemi e "
           "guadagnare tempo. Intanto gli avventurieri che vengono dopo ti "
           "raggiungono, e la situazione può cambiare.",
    # --------------------------------------------- il rito del lupo mannaro
    24534: "A vedere come stanno le cose, non c'è dubbio: è un rito che viene "
           "dalla notte dei tempi... \\nsi chiama <Il Gioco Rituale del Lupo "
           "Mannaro>.",
    24535: "Il rito funziona così: \\nun lupo prende sembianze umane, si infila "
           "fra la gente e a notte fonda offre in sacrificio gli abitanti, uno "
           "per volta. \\nPiù forte è chi viene offerto, più il rito corre; e "
           "arrivato a un certo punto scende il <Lupo Divino>. Da lì in poi il "
           "posto finisce a fare da mangiatoia sotto il dominio dei lupi. Se "
           "quattro lupi si mettessero a menare così com'è li sterminerebbero "
           "in un attimo: ecco perché prendono questa strada.",
    24536: "La cosa fastidiosa di questo rito è che non finisce nemmeno "
           "sterminando i lupi mannari col metodo normale. Bisogna fare il "
           "contrario di come avanza il rito... si dice che il rito si annulli "
           "soltanto giustiziando i lupi mannari uno per volta, in pieno "
           "giorno, con un metodo speciale.",
    24537: "Anche a sorvegliare tutto il giorno le persone sospette per trovare "
           "il lupo mannaro, probabilmente i giorni non bastano. E per "
           "complicare le cose, a volte ci si mette in mezzo una volpe "
           "ammaliatrice che punta a impadronirsi del rito. Comunque: conto "
           "anche sul tuo fiuto di avventuriero.",
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
    with io.open(radice / "lavoro" / "fase4-chat-016.jsonl", "wb") as f:
        f.write(dati)
    doppi = set("—–“”«»…・《》")
    guasti = [d["riga"] for d in voci if doppi & set(d["it"])]
    print("%d voci scritte | caratteri a due byte: %s" % (len(voci), guasti or "nessuno"))
    for d in voci:
        if "\\n" in d["en_grezzo"]:
            print("  %d  \\n nell'inglese: %d | nella resa: %d"
                  % (d["riga"], d["en_grezzo"].count("\\n"), d["it"].count("\\n")))


if __name__ == "__main__":
    main()
