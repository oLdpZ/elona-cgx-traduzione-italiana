# -*- coding: utf-8 -*-
"""La voce che sforava il riquadro: `command.hsp:7770`, e la sua gemella.

    promptAdd "Evoca come amichevole. (" + ppcost1@NE + " pp)", "null", 1

Riquadro da 280px dichiarato a `:7774`, cioe' un tetto di **30 caratteri**. Col
costo a tre cifre — `ppcost1` e' il livello del PNG personalizzato, che
`system.hsp:1324` limita a 350 — la voce ne misura **31**: il riquadro taglia,
non manda a capo.

⚠️⚠️ **L'inglese ci stava**: «Summon as friendly. (350 pp)» sono 28 caratteri.
Non e' un tetto ereditato da monte, e' un difetto che ha aggiunto la traduzione.

⚠️⚠️⚠️ **E il `motivo` della toppa dichiara la larghezza**: «ⓘ Il prompt e' largo
280 (:7774)». Chi l'ha scritta aveva il dato sotto gli occhi e non l'ha
convertito in caratteri, perche' niente lo faceva per lui: `strumenti/larghezze.py`
scorre il **dizionario**, e una toppa non ha voce di dizionario. Il numero era
in mano, la misura no.

## La correzione: cade il punto, non la parola

«Amichevole», «neutrale» e «ostile» restano — il `motivo` spiega perche' non
possono diventare «alleato» e «nemico»: concorderebbero col personaggio evocato,
di cui non si conosce il sesso, e la guida di stile lo vieta. Cade il **punto
fermo** prima della parentesi, sulle due voci che portano un costo: in una voce
di menu la parentesi e' un suffisso dell'etichetta, non una frase nuova.

    Evoca come amichevole (999 pp)   30 su 30
    Evoca come neutrale (999 pp)     28 su 30

⚠️ Le altre due voci — «Evoca come ostile.» e «Annulla.» — tengono il punto: non
hanno suffisso, e la simmetria da rispettare e' quella della **forma**, non
quella del carattere finale.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-accorcia-le-evocazioni.py
"""
import io
import json
import sys

from strumenti import percorsi

CAMBI = [
    ('"Evoca come amichevole. ("', '"Evoca come amichevole ("'),
    ('"Evoca come neutrale. ("', '"Evoca come neutrale ("'),
]

NOTA = (" ⚠️ Il punto prima della parentesi e' caduto il 2026-09-03: col costo a "
        "tre cifre la voce misurava 31 caratteri contro il tetto di 30 del "
        "riquadro da 280px, e il riquadro taglia. L'inglese ci stava (28). "
        "Trovata da `_130-larghezze-sulla-build.py`, che misura i menu "
        "sull'albero della build e quindi vede anche le toppe.")


def main() -> int:
    percorso = percorsi.PROGETTO / "toppe.jsonl"
    linee = io.open(percorso, encoding="utf-8").read().splitlines()
    toccate = 0
    fuori = []
    for linea in linee:
        if not linea.strip():
            fuori.append(linea)
            continue
        toppa = json.loads(linea)
        sostituisci = toppa["sostituisci"]
        if isinstance(sostituisci, str):
            for vecchio, nuovo in CAMBI:
                if vecchio in sostituisci:
                    toppa["sostituisci"] = sostituisci.replace(vecchio, nuovo)
                    toppa["motivo"] = toppa["motivo"] + NOTA
                    toccate += 1
                    break
        fuori.append(json.dumps(toppa, ensure_ascii=False))
    if toccate != len(CAMBI):
        print("⚠️ toccate %d toppe su %d attese: non scrivo niente"
              % (toccate, len(CAMBI)))
        return 1
    io.open(percorso, "w", encoding="utf-8", newline="\n").write(
        "\n".join(fuori) + "\n")
    print("toppe corrette: %d" % toccate)
    return 0


if __name__ == "__main__":
    sys.exit(main())
