"""Elenca le stringhe scoperte di un file, con riga e contesto.

`copertura.scoperte_di` restituisce solo il testo: per decidere un lotto serve
sapere DOVE sta ciascuna, perche' una battuta e una traccia di debug hanno la
stessa forma.
"""
import sys
from collections import defaultdict

from strumenti import copertura, percorsi
from strumenti.commenti import righe_in_commento

NOME = sys.argv[1] if len(sys.argv) > 1 else "tcg_skill.hsp"

percorso = percorsi.SORGENTE_HSP / NOME
testo = percorso.read_bytes().decode("cp932")
morte = righe_in_commento(percorso)
toppe = copertura._righe_con_toppa().get(NOME, set())
rese = copertura.rese_da_meccanismo().get(NOME, set())

scoperte = copertura.scoperte_di(NOME, testo, toppe, morte, rese)
conto = defaultdict(int)
for s in scoperte:
    conto[s] += 1

# ritrova la riga di ciascuna
righe_di = defaultdict(list)
for numero, riga in enumerate(testo.split("\n"), 1):
    for s in conto:
        if '"' + s + '"' in riga:
            righe_di[s].append(numero)

print(f"{NOME}: {len(scoperte)} scoperte, {len(conto)} distinte\n")
for s in sorted(conto, key=lambda x: (righe_di[x][:1] or [0])[0]):
    posti = ",".join(str(n) for n in righe_di[s][:4])
    riga_prima = testo.split("\n")[(righe_di[s][0] - 1)] if righe_di[s] else ""
    verbo = riga_prima.strip().split(" ")[0][:22]
    print(f"{posti:>22}  [{verbo:<22}] {s!r}")
