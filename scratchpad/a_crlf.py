"""Porta un file di testo a fine riga CRLF, che e' quel che `cmd.exe` vuole.

⚠️ Un `.bat` con le sole LF gira quasi sempre, ma un `goto` verso un'etichetta
in coda puo' non trovarla: `cmd` legge le etichette riga per riga, e senza il
ritorno a capo giusto l'etichetta si porta dietro caratteri che non ci sono.
"""
import sys
from pathlib import Path

for nome in sys.argv[1:]:
    percorso = Path(nome)
    dati = percorso.read_bytes().replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
    percorso.write_bytes(dati)
    print("CRLF: %s (%d byte)" % (percorso.name, len(dati)))
