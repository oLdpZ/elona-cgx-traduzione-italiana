# -*- coding: utf-8 -*-
"""Quali delle 60 righe nude di classe `testo` NON sono ancora state decise.

⚠️⚠️ **Il conto di `triage_nudi` non e' il conto del lavoro, e lo dice lui
stesso** (`invariati.md`, 127a): quei referti contano i letterali **intatti**, e
una riga che deve restare intatta e' indistinguibile da una che nessuno ha
guardato. La 127a ha dichiarato una ventina di quelle righe in `invariati.md` —
le sigle `Hp:`/`Lv.`/`Dv:`/`Pv:`, le chiavi di `config.txt`, il TSV
dell'autopick, `helloworld.hsp` che non sta nemmeno nella build — e restano
tutte dentro il numero.

Quindi «60 righe da tradurre» e' falso, e questo referto dice di quanto:
incrocia le 60 righe con i **siti nominati** in `invariati.md`, `decisioni.md` e
`rinviate.jsonl`, e stampa quelle che nessuno dei tre nomina.

⚠️ Un sito nominato non e' per forza un sito **deciso**: puo' essere citato di
passaggio. Il referto trova il residuo da leggere, non da tradurre a occhi
chiusi — e infatti stampa accanto a ogni riga la classe che il triage le da'.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-residuo-delle-righe-nude.py
"""
import importlib.util
import io
import os
import re
import sys

from strumenti import percorsi

_QUI = os.path.dirname(os.path.abspath(__file__))


def _carica(nome, percorso):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


T = _carica("triage", os.path.join(_QUI, "triage_nudi.py"))


def siti_nominati() -> set:
    """(file, riga) nominati nei tre documenti che registrano le decisioni.

    Si cerca `nome.hsp:1234` e anche la forma `:1234` che i documenti usano
    quando il file e' gia' detto nel titolo della sezione: per quella si tiene
    il file **piu' vicino sopra**, che e' come la si legge.
    """
    fuori = set()
    for nome_doc in ("invariati.md", "decisioni.md"):
        percorso = percorsi.PROGETTO / nome_doc
        ultimo = None
        for linea in io.open(percorso, encoding="utf-8"):
            for m in re.finditer(r"\b([a-z_0-9]+\.hsp)\s*:\s*`?:?(\d+)", linea):
                fuori.add((m.group(1), int(m.group(2))))
                ultimo = m.group(1)
            for m in re.finditer(r"\b([a-z_0-9]+\.hsp)\b", linea):
                ultimo = m.group(1)
            for m in re.finditer(r"`:(\d+)`", linea):
                if ultimo:
                    fuori.add((ultimo, int(m.group(1))))
    percorso = percorsi.PROGETTO / "rinviate.jsonl"
    import json
    for linea in io.open(percorso, encoding="utf-8"):
        if linea.strip():
            voce = json.loads(linea)
            if isinstance(voce.get("riga"), int):
                fuori.add((voce["file"], voce["riga"]))
    return fuori


def main() -> int:
    nominati = siti_nominati()
    import glob
    righe = []
    for percorso in sorted(glob.glob(os.path.join(T.nu.SORGENTE, "*.hsp"))):
        nome = os.path.basename(percorso)
        for riga, classe, routine, testo in T.classifica(nome):
            if classe == "testo":
                righe.append((nome, riga, routine, testo))

    residuo = [r for r in righe if (r[0], r[1]) not in nominati]
    for nome, riga, routine, testo in sorted(residuo):
        print("%-22s %6d  %-26s %s" % (nome, riga, routine, testo[:80]))
    print()
    print("righe nude di classe `testo`      : %d" % len(righe))
    print("  gia' nominate nei documenti     : %d" % (len(righe) - len(residuo)))
    print("  RESIDUO, da leggere             : %d" % len(residuo))
    return 0


if __name__ == "__main__":
    sys.exit(main())
