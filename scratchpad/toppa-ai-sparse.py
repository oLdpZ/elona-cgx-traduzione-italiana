# -*- coding: utf-8 -*-
"""52a, lotto `ai-sparse`: le dodici righe sparse di custom_ai.hsp.

⚠️ **Sono la coda che il conteggio per routine non mostra**, ed e' la stessa
lezione delle tre righe fuori dai menu della 51a in forma nuova: li' il criterio
era «il testo sta in blocchi», e le tre fuori non le vedeva nessuno; qui le
righe stanno in routine, ma **una per routine**, e il riassunto per routine —
ordinato per numero decrescente — le lascia in fondo. A trovarle e' stato
`nudi_en.py`, che elenca per FILE: «82 righe, 12 ancora intatte».
💡 Chiudere un file vuol dire guardarlo con tutt'e due i referti.

Otto sono lo stesso «Back» sulla stessa riga identica, quindi una toppa `tutte`.
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
    (1246, '\t\tlistn(0, cnt) = "Vuoto"',
     "Lo slot di tattica non ancora impostato, nell'elenco da cui si sceglie "
     "quale configurare. ⭐ «Vuoto» e non «Libero»: dice che dentro non c'e' "
     "niente, che e' quel che il giocatore deve capire per andarci a scrivere."),
    (1255, '\tlistn(0, 20) = "Indietro"',
     "L'unico «Back» con un indice fisso, quindi la sua toppa e' a se'."),
    (1331, '\t\tlistn(0, NumActions) = "Indietro"',
     "«Back» sulla riga identica in sette menu del pannello — la coda di ogni "
     "elenco che si sfoglia. Una toppa sola con `tutte` li chiude tutti."),
    (1358, '\t\t\ttxt "" + name(tc) + " conosce gia\' quella magia."',
     "⚠️ `name(tc)` e' una funzione di CONTENUTO e resta dov'e' (`funzioni.py`): "
     "l'inglese la usa e quindi la resa italiana la deve usare, ne' in piu' ne' "
     "in meno. Cambia solo la coda della frase. ⭐ «gia'» prima del complemento, "
     "che in italiano e' la posizione naturale dell'avverbio col verbo."),
    (1489, '\t\t\ttxt "" + name(tc) + " conosce gia\' quell\'abilita\'."',
     "La gemella per le abilita'. Stessa forma, stessa funzione conservata."),
    (3097, '\t\tlistn(0, NumActions) = "Non impostato"',
     "Lo stesso «Not Set» delle tabelle, qui costruito a mano dentro un elenco "
     "invece che letto da `AITextData`: la resa dev'essere la stessa o la stessa "
     "voce cambierebbe nome da una schermata all'altra."),
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
        print(f"  :{n:<5} x{quante}  {resa.strip()[:70]}")

    uscita = REPO / "lavoro" / "_toppe-ai-sparse.jsonl"
    dati = "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in toppe).encode("utf-8")
    uscita.write_bytes(dati)

    esito = subprocess.run(
        [sys.executable, str(REPO / "scratchpad" / "aggiungi-toppe.py"), str(uscita)],
        cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    print(esito.stdout.strip() or esito.stderr.strip())


if __name__ == "__main__":
    main()
