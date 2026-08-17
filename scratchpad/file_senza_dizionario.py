# -*- coding: utf-8 -*-
"""I file che hanno `lang()` e NON hanno un file di dizionario.

Il nono punto cieco (`db_card.hsp`, 54a) e il decimo (`screen.hsp`, 55a) sono
stati trovati **uno alla volta, per caso**: il primo aprendo il negozio delle
carte, il secondo guardando una schermata di collaudo. Ogni volta la scoperta e'
stata la stessa — *«questo file non lo nomina `verifica --dizionario`»* — e ogni
volta e' costata mezza sessione.

Questo referto la fa in un comando. Un file senza `dizionario/<nome>.jsonl` non
e' un file finito: e' un file che **nessun conteggio guarda**. Aprirlo anche per
una voce sola lo fa entrare nel referto.

⚠️⚠️ **E il caso peggiore non e' il file intatto: e' il file MEZZO fatto.**
`custom_ai.hsp` ha 82 letterali nudi tradotti con altrettante toppe (`nudi_en`
dice «0 ancora intatte») e le sue `lang()` sono tutte inglesi, perche' nessun
lotto puo' raggiungerle. Il pannello dell'IA e' quindi italiano nei letterali e
inglese nelle `lang()`, **nella stessa finestra**: e' esattamente il paragrafo
bilingue di `tcg.hsp` della 53a, in un posto dove nessuno l'aveva cercato.

La colonna «toppe» serve a distinguere i due casi:

    lang() alte, toppe 0    -> file mai aperto, il caso semplice
    lang() alte, toppe alte -> META' TRADOTTO, e la finestra e' bilingue
"""
import json
import re
import sys
from collections import Counter

from strumenti import percorsi

_LANG = re.compile(r"\blang\s*\(")
# ⚠️ `font lang(cfg_font1, cfg_font2), 14 - en * 2, 0` NON e' testo: e' la scelta
#    del carattere fra giapponese e inglese, e ce n'e' una a ogni cambio di
#    corpo. Contandola, `custom_ai.hsp` risultava 32 dove le stringhe vere sono
#    **7**, e il totale usciva gonfio. Si scarta per il nome della variabile,
#    non per il verbo `font`: la stessa forma compare anche fuori da `font`.
_FONT = re.compile(r"\blang\s*\(\s*cfg_font")


def conta_toppe() -> Counter:
    percorso = percorsi.PROGETTO / "toppe.jsonl"
    quante: Counter = Counter()
    if not percorso.exists():
        return quante
    for linea in percorso.read_text(encoding="utf-8").splitlines():
        if linea.strip():
            quante[json.loads(linea)["file"]] += 1
    return quante


def censimento() -> list[tuple[str, int, int, bool]]:
    """(file, quante lang(), quante toppe, ha il dizionario) per ogni .hsp."""
    toppe = conta_toppe()
    fuori = []
    for percorso in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
        testo = percorso.read_bytes().decode("cp932", "replace")
        quante = len(_LANG.findall(testo)) - len(_FONT.findall(testo))
        if not quante:
            continue
        ha = (percorsi.DIZIONARIO / f"{percorso.name}.jsonl").exists()
        fuori.append((percorso.name, quante, toppe[percorso.name], ha))
    return fuori


def main(argv: list[str] | None = None) -> int:
    righe = censimento()
    senza = [r for r in righe if not r[3]]
    senza.sort(key=lambda r: -r[1])

    print("%-30s %8s %7s" % ("file SENZA dizionario", "lang()", "toppe"))
    for nome, quante, toppe, _ in senza:
        nota = "  <- META' TRADOTTO: finestra bilingue" if toppe else ""
        print("%-30s %8d %7d%s" % (nome, quante, toppe, nota))

    print("\nfile con lang(): %d, di cui SENZA dizionario: %d"
          % (len(righe), len(senza)))
    print("lang() fuori da ogni conteggio: %d" % sum(r[1] for r in senza))
    misti = [r for r in senza if r[2]]
    if misti:
        print("⚠️ file mezzo tradotti (toppe si', dizionario no): %d — %s"
              % (len(misti), ", ".join(r[0] for r in misti)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
