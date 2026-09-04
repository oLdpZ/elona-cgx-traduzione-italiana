"""Rimette nella ripresa le trappole della 137a, che il montaggio ha tagliato.

⚠️ La testa nuova partiva dal marcatore della 136a, e in mezzo c'era la sezione
della 137a: memoria del progetto, non cronaca della sessione. Si ripesca dalla
versione in git invece di riscriverla a memoria.
"""
import subprocess

from strumenti import percorsi

MARCA_137 = "## Le trappole che la 137a ha trovato"
MARCA_136 = "## Le trappole che la 136a ha trovato"

vecchio = subprocess.run(
    ["git", "show", "HEAD:RIPRESA-sessione.md"],
    cwd=percorsi.PROGETTO, capture_output=True, check=True).stdout.decode("utf-8")

inizio = vecchio.index(MARCA_137)
fine = vecchio.index(MARCA_136)
sezione = vecchio[inizio:fine]
if len(sezione) < 500:
    raise SystemExit("la sezione ripescata e' troppo corta: %d byte" % len(sezione))

bersaglio = percorsi.PROGETTO / "RIPRESA-sessione.md"
nuovo = bersaglio.read_text(encoding="utf-8")
if MARCA_137 in nuovo:
    raise SystemExit("c'e' gia': niente da rimettere")
taglio = nuovo.index(MARCA_136)
bersaglio.write_text(nuovo[:taglio] + sezione + nuovo[taglio:], encoding="utf-8")
print("rimesse le trappole della 137a: %d byte" % len(sezione))
