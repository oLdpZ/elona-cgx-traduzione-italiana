# -*- coding: utf-8 -*-
"""112a - Il dossier della famiglia delle righe-fonte: giapponese, inglese,
frequenza e margine, un titolo per blocco.

⚠️ Il titolo si decide dal **giapponese**, non dall'inglese: e' la regola delle
cinque fonti della 110a, e qui serve piu' che altrove perche' i titoli inglesi
portano refusi di monte (`Secrt`, `Alamanac`, `excutioner`) e perche' in due
casi l'inglese scioglie in una parola comune quel che il giapponese nomina.

⚠️⚠️ E il titolo va cercato **dentro** il giapponese della descrizione, non
preso da un campo suo: la riga-fonte non e' una voce del dizionario: e' l'ultimo
segmento di una descrizione che e' tutt'uno. Chi la cerca come voce non la trova.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_112-dossier-fonti.py
    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_112-dossier-fonti.py --da 1 --a 40
"""
import argparse
import collections
import importlib.util
import io
import json
import re
from pathlib import Path

from strumenti.estrai import estrai_da_testo, spezza_righe
from strumenti.percorsi import SORGENTE_HSP

_qui = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    '_112_corpo', _qui / '_112-corpo-descrizioni.py')
_112 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_112)
_107 = _112._107

ACAPO, CANCELLO, TABULA = _112.ACAPO, _112.CANCELLO, _112.TABULA
FILE = 'db_item.hsp'
_INDICE = re.compile(r'^\s*description\((\d+)\)\s*=')


def voluta_da(testo):
    """Il segmento marcato dal `#`, in un testo grezzo (jp o en)."""
    if not testo:
        return None
    for pezzo in testo.replace(TABULA, '').split(ACAPO):
        if pezzo.startswith(CANCELLO):
            return pezzo[1:].strip()
    return None


def coppie():
    """(riga, indice, jp, en) delle descrizioni del corpo, col giapponese."""
    testo = (SORGENTE_HSP / FILE).read_text(encoding='cp932')
    righe, _, _ = spezza_righe(testo)
    fuori = []
    for voce in estrai_da_testo(FILE, testo):
        if 'array' in voce:
            continue
        trovato = _INDICE.match(righe[voce['riga'] - 1])
        if trovato is None:
            continue
        indice = int(trovato.group(1))
        if indice not in (0, 1, 2):
            continue
        fuori.append((voce['riga'], indice, voce.get('jp') or '', voce['en']))
    return fuori


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--da', type=int, default=1)
    ap.add_argument('--a', type=int, default=10**6)
    args = ap.parse_args()

    famiglia = collections.OrderedDict()
    for riga, indice, jp, en in coppie():
        t_en = voluta_da(en)
        if not t_en:
            continue
        t_jp = voluta_da(jp)
        voce = famiglia.setdefault(t_en, {'n': 0, 'jp': collections.Counter(),
                                          'muti': 0, 'dove': []})
        voce['n'] += 1
        if t_jp:
            voce['jp'][t_jp] += 1
        else:
            voce['muti'] += 1
        if len(voce['dove']) < 2:
            voce['dove'].append(f'{FILE}:{riga}')

    ordinata = sorted(famiglia.items(), key=lambda kv: -kv[1]['n'])
    print(f'# La famiglia delle righe-fonte: {len(ordinata)} titoli distinti, '
          f'{sum(v["n"] for _, v in ordinata)} righe')
    print(f'# tetto: {_112.SOGLIA} caratteri (degradati). Oltre, la riga smette '
          f'di essere una fonte.')
    print()
    for n, (t_en, voce) in enumerate(ordinata, 1):
        if not (args.da <= n <= args.a):
            continue
        print(f'## {n:>3}  {voce["n"]:>4}x   margine {_112.SOGLIA - len(t_en):>3}'
              f'   {voce["dove"][0]}')
        for t_jp, quante in voce['jp'].most_common():
            marca = '' if (len(voce['jp']) == 1 and not voce['muti']) \
                else f'  ({quante}x)'
            print(f'   jp  {t_jp}{marca}')
        if voce['muti']:
            print(f'   jp  ⚠️ MUTO su {voce["muti"]}x — il ramo giapponese non ha')
            print(f'       questa riga: o e\' vuoto, o la mette in un altro indice.')
            print(f'       Li\' l\'inglese e\' l\'unica fonte, e va guardato il ramo jp')
            print(f'       dello STESSO oggetto prima di decidere.')
        print(f'   en  {t_en}')
        print(f'   it  ')
        print()


if __name__ == '__main__':
    main()
