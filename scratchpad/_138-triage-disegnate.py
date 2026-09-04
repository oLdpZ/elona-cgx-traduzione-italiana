"""Il censimento di `disegnate` riga per riga, per triarlo a mano."""
from strumenti import copertura, disegnate, percorsi
from strumenti.commenti import righe_in_commento

toppe = copertura._righe_con_toppa()
rese = disegnate._rese_note()
invarianti = disegnate._invarianti()

for percorso in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
    nome = percorso.name
    if nome in copertura.MECCANISMI:
        continue
    testo = percorso.read_bytes().decode("cp932")
    righe_del_file = testo.split("\n")
    scoperte = []
    for numero, come, letterale in disegnate.tutte_di(
            nome, testo, righe_in_commento(percorso)):
        if letterale in rese.get(nome, set()) or letterale in invarianti:
            continue
        if righe_del_file[numero - 1].strip() in toppe.get(nome, set()):
            continue
        scoperte.append((numero, come, letterale))
    if not scoperte:
        continue
    print("=" * 72)
    print("%s: %d siti, %d distinte"
          % (nome, len(scoperte), len({s[2] for s in scoperte})))
    for numero, come, letterale in scoperte:
        print("  %6d %-14s %r" % (numero, come, letterale))
