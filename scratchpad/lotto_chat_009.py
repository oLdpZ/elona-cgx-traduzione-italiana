# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-009.jsonl: il menu dell'informatore sui boss
(chat.hsp:24236-:24321). Ventisei voci di `chatList` piu' la domanda.

⚠️ Il taglio duro a 24 caratteri di `chat.hsp:25167` NON si applica qui: scatta
solo con `keyrange > 10`, e le condizioni di trama di questo menu ne lasciano
passare al massimo **sei** insieme (misurato con scratchpad/menu_informatore.py).
Vale il tetto ordinario della rete 15, che menu_dialogo.py controlla da se'.

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib

RESE = {
    24236: "Per adesso non mi pare che ti serva.",
    24239: "Non mi serve nessuna informazione.",
    24241: "Il boss della Torre Rovente",
    24244: "Il boss del Castello Antico",
    24247: "Il boss della grotta dei morti",
    24251: "I pericoli di Lesimas (1)",
    24256: "I pericoli di Lesimas (2)",
    24261: "I pericoli di Lesimas (3)",
    24265: "Il boss di Lesimas",
    24268: "Il boss del Tempio Caos",
    24271: "Il boss della Fortezza Meccanica",
    24274: "Il boss della Valle degli Inferi",
    24277: "I pericoli di Remido (1)",
    24280: "I pericoli di Remido (2)",
    24283: "Il boss del Passo di Montagna",
    24286: "Il boss di Remido",
    24289: "I pericoli della Culla del Caos (1)",
    24292: "Il boss delle Acque di Valm",
    24295: "Le armi biologiche di Zanan",
    24298: "Il demone comparso a Mayroon",
    24301: "Il demone comparso a Eulderna",
    24304: "Il demone comparso a Kikkasu",
    24307: "I pericoli della Culla del Caos (2)",
    24310: "I pericoli della Culla del Caos (3)",
    24313: "I pericoli della Culla del Caos (4)",
    24316: "Notizie su Tezcatlipoca",
    24319: "Il boss della Culla del Caos",
    24321: "Sono 300 monete per ogni informazione.",
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
    with io.open(radice / "lavoro" / "fase4-chat-009.jsonl", "wb") as f:
        f.write(dati)
    print("%d voci scritte" % len(voci))
    lunga = max(voci, key=lambda d: len(d["it"]))
    print("la piu' lunga: %d caratteri (tetto 58)  %s" % (len(lunga["it"]), lunga["it"]))


if __name__ == "__main__":
    main()
