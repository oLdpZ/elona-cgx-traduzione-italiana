"""L'ultimo operando di `Effect: ` rimasto inglese.

`tcg_skill.hsp:2003` e' la **seconda** ricomposizione della scheda di una carta:
quando un lich sale di grado, la scheda viene rifatta come
`lines@tcg(0) + "\\nEffect: " + effdesc@tcg(...)`. La toppa 1230 aveva reso il
primo sito (`tcg.hsp:1473`) e nessuno aveva cercato il secondo, cosi' quel ramo
scrive `Effect:` in inglese davanti a una descrizione italiana.

⚠️ Qui NON c'e' `talk_conv`: questa ricomposizione non manda a capo niente, a
differenza di `tcg.hsp:1475`. Una descrizione lunga esce su una riga sola. Non
lo ripara questa toppa e non e' un guasto che introduce la traduzione: sta
scritto in `RIPRESA-sessione.md` fra le cose aperte.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strumenti import percorsi  # noqa: E402

FILE = "tcg_skill.hsp"
AGO = 'lines@tcg(0) + "\\nEffect: " + effdesc@tcg('

MOTIVO = (
    "La SECONDA ricomposizione della scheda (`tcg_skill.hsp:2003`, il lich che "
    "sale di grado): `lines@tcg(0) + \"\\nEffect: \" + effdesc@tcg(...)`. La "
    "toppa 1230 aveva reso il primo sito, `tcg.hsp:1473`, e nessuno aveva "
    "cercato il secondo -- cosi' quel ramo scriveva `Effect:` in inglese "
    "davanti a una descrizione italiana. ⚠️ E' lo stesso modo di sbagliare "
    "dell'operando di `\"Bits:  \"`: una stringa scritta in due posti, tradotta "
    "in uno."
)


def main() -> int:
    percorso = percorsi.SORGENTE_HSP / FILE
    righe = percorso.read_text(encoding="cp932").splitlines()
    if len(righe) < 1000:
        raise SystemExit("divisione fallita: %d righe" % len(righe))

    trovate = [r for r in righe if AGO in r]
    if len(trovate) != 1:
        raise SystemExit("«%s»: %d righe, ne serviva 1" % (AGO, len(trovate)))
    riga = trovate[0]
    toppa = {"file": FILE, "cerca": riga,
             "sostituisci": riga.replace('"\\nEffect: "', '"\\nEffetto: "'),
             "motivo": MOTIVO}
    if toppa["cerca"] == toppa["sostituisci"]:
        raise SystemExit("la sostituzione non cambia niente: il letterale non"
                         " e' quello che credevo")

    bersaglio = percorsi.PROGETTO / "toppe.jsonl"
    for testo in bersaglio.read_text(encoding="utf-8").splitlines():
        if testo.strip() and json.loads(testo)["cerca"] == toppa["cerca"]:
            print("c'e' gia'")
            return 0
    with bersaglio.open("a", encoding="utf-8") as scrittura:
        scrittura.write(json.dumps(toppa, ensure_ascii=False) + "\n")
    print("toppa aggiunta: %s" % riga.strip()[:80])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
