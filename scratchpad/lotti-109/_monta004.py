# -*- coding: utf-8 -*-
"""Monta `rese004.py` da `chiavi004.txt` (l'inglese verbatim) e `_traduzioni004.py`.

L'inglese e' la meta' della chiave e non si ricopia a mano: `_107-chiavi-item.py`
lo emette dal sorgente, e questo script si limita a sostituire la resa vuota.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta004.py

⚠️ Se una riga del template non ha una resa, o una resa non ha una riga, lo
script muore invece di scrivere un file mezzo buono: e' lo stesso patto di
`assembla-lotto.py`.
"""
import importlib.util
import io
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(QUI, 'chiavi004.txt')
USCITA = os.path.join(QUI, 'rese004.py')

INTESTAZIONE = """import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
"""


def carica_traduzioni():
    percorso = os.path.join(QUI, '_traduzioni004.py')
    spec = importlib.util.spec_from_file_location('traduzioni004', percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.IT


def main():
    it = carica_traduzioni()
    righe = io.open(TEMPLATE, encoding='utf-8').read().splitlines()
    # il template comincia col blocco RIGHE = {...}: si salta fino alla riga
    # di commento che conta le righe, che e' l'ultima cosa prima delle voci
    inizio = next(i for i, r in enumerate(righe) if r.startswith('# ') and 'righe, da' in r)
    corpo = righe[inizio + 1:]

    fuori = []
    viste = set()
    for i, riga in enumerate(corpo):
        # ⚠️ l'inglese col carattere `'` dentro esce fra virgolette doppie:
        # la prima versione di questa regex cercava solo l'apice, e nove voci
        # su 143 sembravano «rese senza riga nel template»
        m = re.match(r"^    \((\d+), ['\"]", riga)
        if not m:
            continue
        n = int(m.group(1))
        viste.add(n)
        if n not in it:
            fuori.append(f'riga {n}: nel template ma senza resa')
            continue
        successiva = corpo[i + 1]
        if successiva != '        "",':
            fuori.append(f'riga {n}: la riga dopo non e\' la resa vuota ({successiva!r})')
            continue
        corpo[i + 1] = '        "' + it[n] + '",'

    for n in sorted(set(it) - viste):
        fuori.append(f'riga {n}: c\'e\' una resa ma il template non ha quella riga')

    if fuori:
        sys.exit('\n'.join(['⚠️ montaggio fermo:'] + fuori))

    testo = INTESTAZIONE + '\n'.join(corpo).rstrip() + '\n}\n'
    io.open(USCITA, 'w', encoding='utf-8', newline='\n').write(testo)
    print(f'{len(viste)} rese montate in {USCITA}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
