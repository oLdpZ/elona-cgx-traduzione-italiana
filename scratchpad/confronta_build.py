"""Due build della stessa traduzione differiscono: di quanto, e dove?

Serve a sapere se l'eseguibile che si costruisce l'utente e' lo stesso che
costruiamo noi. «Stessa dimensione, impronta diversa» non e' una risposta: o
sono due o tre byte di data e ora, e allora e' lo stesso programma, oppure no.
"""
import sys
from pathlib import Path

A = Path(sys.argv[1])
B = Path(sys.argv[2])
a, b = A.read_bytes(), B.read_bytes()
print("%s  %d byte" % (A.name, len(a)))
print("%s  %d byte" % (B.name, len(b)))

if len(a) != len(b):
    print("dimensioni diverse: non ha senso confrontare byte per byte")
    raise SystemExit

diversi = [i for i in range(len(a)) if a[i] != b[i]]
print()
print("byte diversi: %d su %d  (%.6f%%)"
      % (len(diversi), len(a), 100.0 * len(diversi) / len(a)))
if not diversi:
    raise SystemExit

print("primo a %d, ultimo a %d" % (diversi[0], diversi[-1]))

# raggruppa in tratti contigui, per capire se sono pochi punti o tutto il file
tratti = []
inizio = prec = diversi[0]
for i in diversi[1:]:
    if i > prec + 8:
        tratti.append((inizio, prec))
        inizio = i
    prec = i
tratti.append((inizio, prec))
print("tratti diversi: %d" % len(tratti))
for inizio, fine in tratti[:10]:
    print("  %8d - %8d  (%d byte)" % (inizio, fine, fine - inizio + 1))
    print("     A: %r" % a[inizio:min(fine + 1, inizio + 40)])
    print("     B: %r" % b[inizio:min(fine + 1, inizio + 40)])
if len(tratti) > 10:
    print("  ... e altri %d" % (len(tratti) - 10))
