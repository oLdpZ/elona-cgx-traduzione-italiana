# -*- coding: utf-8 -*-
"""Mostra un blocco di `book.txt`: l'inglese numerato e il giapponese di monte.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_99-dump-book.py 9

Il numero di riga stampato e' quello della **firma** (righe piene del blocco,
numerate da 1), cioe' l'indice a cui la resa deve restare. Accanto, la
lunghezza in caratteri: il tetto di `book.txt` e' 43 e il gioco **non manda a
capo** (`command.hsp:8412` fa `mes s` e basta).
"""
import io
import json
import sys

TETTO = 43


def main(blocco, con_jp=True):
    voci = [json.loads(r) for r in
            io.open("dizionario/dati/book.txt.jsonl", encoding="utf-8") if r.strip()]
    gruppo = sorted((v for v in voci if v["blocco"] == blocco), key=lambda v: v["riga"])
    if not gruppo:
        raise SystemExit(f"%{blocco}: nessuna riga")

    if con_jp:
        print(f"--- %{blocco}: giapponese di monte ---")
        for riga in gruppo[0]["jp_contesto"]:
            print(f"    {riga}")
        print()

    print(f"--- %{blocco}: {len(gruppo)} righe inglesi (tetto {TETTO}) ---")
    for voce in gruppo:
        lunghezza = len(voce["en"])
        segno = " !" if lunghezza > TETTO else "  "
        print(f"{voce['riga']:>4}{segno}{lunghezza:>3}  {voce['en']}")


if __name__ == "__main__":
    main(sys.argv[1], "--senza-jp" not in sys.argv)
