"""Monta la ripresa nuova: la testa scritta a mano + la coda storica.

⚠️ La coda (dalle «trappole che la 136a ha trovato» in giu') e' memoria che
vale per chiunque tocchi il progetto e non si riscrive a ogni sessione: si
taglia la vecchia testa e si incolla quella nuova, invece di rifare il file.
"""
from pathlib import Path

from strumenti import percorsi

TESTA = Path(r"C:\Users\old_p\AppData\Local\Temp\claude\C--Games-Elona"
             r"\a68c153d-9dfb-4066-abf4-a41a975e444e\scratchpad\ripresa-testa.md")
MARCA = "## Le trappole che la 136a ha trovato"

bersaglio = percorsi.PROGETTO / "RIPRESA-sessione.md"
vecchio = bersaglio.read_text(encoding="utf-8")
taglio = vecchio.index(MARCA)
if vecchio.count(MARCA) != 1:
    raise SystemExit("la marca non e' unica: il taglio sarebbe cieco")

nuovo = TESTA.read_text(encoding="utf-8") + vecchio[taglio:]
bersaglio.write_text(nuovo, encoding="utf-8")
print("ripresa montata: %d righe (erano %d)"
      % (nuovo.count("\n") + 1, vecchio.count("\n") + 1))
