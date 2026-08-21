# -*- coding: utf-8 -*-
"""La resa italiana dei siti che si nominano, cercata per FIRMA e non per riga.

⚠️ Nel dizionario ogni voce porta la riga della **prima** occorrenza della sua
firma: cercare per numero di riga non trova la resa di un sito che ripete una
firma piu' avanti nel file. Questo strumento estrae il file, prende la firma del
sito chiesto e la cerca nel dizionario.

    python scratchpad/resa-di.py chat.hsp 9777 9780 11216
"""
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti import estrai, percorsi


def main() -> int:
    nome = sys.argv[1]
    righe = {int(a) for a in sys.argv[2:]}
    testo = (percorsi.SORGENTE_HSP / nome).read_bytes().decode('cp932', errors='replace')
    voci = [v for v in estrai.estrai_da_testo(nome, testo) if v['riga'] in righe]
    diz = {}
    percorso = percorsi.DIZIONARIO / (nome + '.jsonl')
    for l in io.open(percorso, encoding='utf-8'):
        if l.strip():
            v = json.loads(l)
            diz[v['firma']] = v
    for v in voci:
        d = diz.get(v['firma'])
        print('--- %s:%d' % (nome, v['riga']))
        print('EN  %s' % (v.get('en_grezzo') or ''))
        if d is None:
            print('IT  <NON TRADOTTA>')
        else:
            print('IT  %s   (dizionario, riga %s)' % (d.get('it'), d.get('riga')))
    return 0


if __name__ == '__main__':
    sys.exit(main())
