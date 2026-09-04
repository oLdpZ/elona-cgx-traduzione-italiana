"""Ogni battuta del lotto D col contesto attorno: chi la dice e quando.

Una battuta senza la scena e' una frase sospesa: `"..and done!"` puo' essere
un mago che finisce un incantesimo o un mercante che chiude un conto.
"""
import json

from strumenti import percorsi

testi = {nome: (percorsi.SORGENTE_HSP / nome).read_bytes().decode("cp932").split("\r\n")
         for nome in ("tcg.hsp", "tcg_skill.hsp", "tcg_custom.hsp", "tcg_mod.hsp")}

lotto = percorsi.LAVORO_LOTTI / "dialoghi-138-lotto-d.jsonl"
for numero, riga in enumerate(lotto.read_text(encoding="utf-8").splitlines(), 1):
    voce = json.loads(riga)
    print("=" * 78)
    print("%2d. %r" % (numero, voce["en"]))
    for sito in voce["siti"]:
        righe = testi[sito["file"]]
        i = sito["riga"] - 1
        print("    --- %s:%d (%s)" % (sito["file"], sito["riga"], sito["come"]))
        for j in range(max(0, i - 6), min(len(righe), i + 3)):
            marca = ">>" if j == i else "  "
            print("    %s %5d %s" % (marca, j + 1, righe[j][:150]))
