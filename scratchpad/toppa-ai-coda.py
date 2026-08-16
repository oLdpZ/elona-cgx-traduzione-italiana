# -*- coding: utf-8 -*-
"""52a, lotto `ai-coda`: le ultime tre righe di custom_ai.hsp, e il file e' chiuso.

Il menu d'importazione ed esportazione delle istruzioni tattiche. Sta in un
`promptAdd`, quindi in una colonnina stretta: le tre voci fanno 22, 22 e 16
caratteri in inglese, e l'italiano 24, 24 e 16.

⚠️ Il prompt di questa schermata e' largo 280 px (`val = promptx, prompty, 280`
poco sotto), cioe' una cinquantina di caratteri a corpo 12: ci sta comodo.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\custom_ai.hsp")
FILE = "custom_ai.hsp"
TESTO = SORGENTE.read_bytes().decode("cp932").splitlines()

LOTTO = [
    (3473, '\tpromptAdd "Esporta le istruzioni", "a"',
     "⭐ «AI Instructions» diventa «le istruzioni» e non «le istruzioni dell'IA»: "
     "la schermata da cui si arriva qui e' il pannello dell'IA e il titolo lo "
     "dice gia', quindi ripeterlo non aggiunge niente e allunga la voce. Il nome "
     "pieno resta dove serve: «Istruzioni tattiche» e' il titolo (`:1088`)."),
    (3474, '\tpromptAdd "Importa le istruzioni", "b"', "Il gemello, stessa scelta."),
    (3475, '\tpromptAdd "Azzera l\'IA di adesso", "c"',
     "«Reset Current AI»: azzera le tattiche impostate su questo alleato. ⭐ "
     "«di adesso» e non «corrente», che in italiano e' un calco — «Current» qui "
     "vuol dire quella caricata ora su questo alleato, non «la corrente»."),
]


def main() -> None:
    toppe = []
    for n, resa, motivo in LOTTO:
        cerca = TESTO[n - 1]
        quante = TESTO.count(cerca)
        if quante == 0 or cerca == resa:
            raise SystemExit(f":{n} non aggancia niente")
        for c in resa:
            if ord(c) > 0x7F:
                raise SystemExit(f":{n} carattere fuori ASCII: {c!r}")
        toppa = {"file": FILE, "cerca": cerca, "sostituisci": resa, "motivo": motivo}
        if quante > 1:
            toppa["tutte"] = True
            toppa["motivo"] += f" ⭐ `tutte`: la riga sta identica in {quante} punti."
        toppe.append(toppa)

    uscita = REPO / "lavoro" / "_toppe-ai-coda.jsonl"
    dati = "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in toppe).encode("utf-8")
    uscita.write_bytes(dati)
    print(f"{len(toppe)} toppe in {uscita.name}")

    esito = subprocess.run(
        [sys.executable, str(REPO / "scratchpad" / "aggiungi-toppe.py"), str(uscita)],
        cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    print(esito.stdout.strip() or esito.stderr.strip())


if __name__ == "__main__":
    main()
