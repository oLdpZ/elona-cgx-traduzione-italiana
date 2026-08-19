# -*- coding: utf-8 -*-
"""L'unica descrizione di abilita' che esce dalla finestra della lista.

Trovata a schermo nella 64a, nella schermata di scelta dell'abilita' di spicco
alla creazione del personaggio: la riga usciva dal bordo destro della pergamena
e finiva sul marmo nudo, dove il collaudo l'ha letta come «...nemici.» staccata
dal resto.

    skill.hsp:268   SKILL_NORMAL_MEMORIZATION
    en  Memorize spells. Enhance scrolls. Analyse enemies.      49
    it  Memorizza incantesimi. Migliora pergamene. Analizza nemici.   59
                                                          tetto 51

Il tetto e' quello di [[effetti_abilita.py]], la rete 18: la colonna «Effetto»
comincia a `wx + 330` dentro una finestra larga 700, e il `mes` non taglia.
Misurato al pixel sulla schermata: il testo arrivava a x=1342 con la pergamena
che finisce a x=1307, cioe' **35 px fuori**.

⚠️ E' una regressione nostra e non un difetto di monte: l'inglese di quella
voce sta dentro. Le altre 414 descrizioni italiane sono tutte sotto il tetto --
questa era l'unica.

⚠️ Si compone in memoria e si scrive solo alla fine (regola della 39a).
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import effetti_abilita as E

PERCORSO = "dizionario/skill.hsp.jsonl"
RIGA = 268
VECCHIO = "Memorizza incantesimi. Migliora pergamene. Analizza nemici."
NUOVO = "Memorizza magie, potenzia pergamene, studia nemici."


def main():
    if len(NUOVO) > E.TETTO:
        raise SystemExit(f"la resa nuova e' {len(NUOVO)}, il tetto e' {E.TETTO}")

    righe = []
    trovata = 0
    with open(PERCORSO, encoding="utf-8") as f:
        for l in f:
            if not l.strip():
                continue
            d = json.loads(l)
            if d["riga"] == RIGA and d["it"] == VECCHIO:
                d["it"] = NUOVO
                trovata += 1
            righe.append(json.dumps(d, ensure_ascii=False))

    if trovata != 1:
        raise SystemExit(f"attese 1 voce da correggere, trovate {trovata}: non tocco niente")

    testo = "\n".join(righe) + "\n"
    io.open(PERCORSO, "w", encoding="utf-8", newline="").write(testo)
    print(f"corretta 1 voce: {len(VECCHIO)} -> {len(NUOVO)} caratteri (tetto {E.TETTO})")


if __name__ == "__main__":
    main()
