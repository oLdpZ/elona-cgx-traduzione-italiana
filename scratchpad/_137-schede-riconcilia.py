"""Perche' il riconoscitore ne trova 72 e il censimento ne dichiarava 76.

⚠️ La regola del progetto e' che un numero atteso che non torna vuol dire «il
conto va rifatto», non «la costante va aggiustata». Rifarlo vuol dire far
vedere **quali** stringhe stanno da una parte e non dall'altra, non scegliere
il numero che piace.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strumenti import copertura, percorsi, schede  # noqa: E402


def main() -> int:
    mie = {v["en"] for v in schede.tutte()}
    print("il riconoscitore di `schede.py` : %d letterali" % len(mie))

    toppe = copertura._righe_con_toppa()
    censite = set()
    for nome in ("tcg_skill.hsp", "tcg.hsp"):
        testo = (percorsi.SORGENTE_HSP / nome).read_text(encoding="cp932")
        scoperte = set(copertura.scoperte_di(nome, testo,
                                             toppe.get(nome, set())))
        for numero, riga in enumerate(testo.splitlines(), 1):
            if "carddetailneff@tcg(" not in riga:
                continue
            spoglia = riga.lstrip()
            if spoglia.startswith(";") or spoglia.startswith("//"):
                continue
            for stringa in scoperte:
                if '"%s"' % stringa in riga:
                    censite.add(stringa)
    print("il censimento della copertura   : %d letterali" % len(censite))
    print()

    solo_censimento = censite - mie
    solo_mie = mie - censite
    print("--- viste dal censimento e NON dal riconoscitore: %d"
          % len(solo_censimento))
    for stringa in sorted(solo_censimento):
        print("    %s" % stringa[:100])
    print()
    print("--- viste dal riconoscitore e NON dal censimento: %d"
          % len(solo_mie))
    for stringa in sorted(solo_mie):
        print("    %s" % stringa[:100])
    print()
    print("--- le giunture, dichiarate e fuori da tutt'e due: %d"
          % len(schede.GIUNTURE))
    for stringa, perche in schede.GIUNTURE.items():
        print("    %-22r %s" % (stringa, perche))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
