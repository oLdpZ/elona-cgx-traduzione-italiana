# -*- coding: utf-8 -*-
"""Monta `reseNNN.py` da `chiaviNNN.txt` (l'inglese verbatim) e `_traduzioniNNN.py`.

Generalizza `_monta004.py`, che aveva il numero del lotto scritto dentro.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 005
    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 006 scratchpad/lotti-110

⚠️ La cartella del lotto e' il **secondo argomento**, e senza di lui e' quella
dello script. Fino alla 109a i tre file stavano accanto a `_monta.py`, e la 110a
li ha messi in `lotti-110/`: senza l'argomento lo script cercava `_traduzioni006`
in `lotti-109/` e moriva dicendo che non c'era. Copiare lo script nella cartella
nuova sarebbe stata la quarta copia di un file che la 108a ha gia' pagato caro
(vedi `modello-rete4.py`).

L'inglese e' la meta' della chiave e non si ricopia a mano: `_107-chiavi-item.py`
lo emette dal sorgente, e questo script si limita a sostituire la resa vuota.

Tre guasti silenziosi che qui diventano rumorosi, e lo script muore invece di
scrivere un file mezzo buono:

  1. una riga del template senza resa, o una resa senza riga nel template;
  2. ⚠️⚠️ una **chiave ripetuta** nel dizionario `IT`. Python non protesta e
     tiene l'ultima: due rese diverse per la stessa riga sparirebbero una
     nell'altra senza che niente lo dica. Si conta sul TESTO del file, non sul
     dizionario, perche' nel dizionario il doppione non c'e' piu';
  3. una resa vuota rimasta tale.
"""
import importlib.util
import io
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))

INTESTAZIONE = """import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
"""


def carica_traduzioni(numero, cartella):
    percorso = os.path.join(cartella, f'_traduzioni{numero}.py')
    testo = io.open(percorso, encoding='utf-8').read()

    # (2) il doppione si cerca nel TESTO, prima che Python lo faccia sparire
    chiavi = re.findall(r'^\s{4}(\d+):', testo, re.M)
    ripetute = sorted({k for k in chiavi if chiavi.count(k) > 1})

    spec = importlib.util.spec_from_file_location(f'traduzioni{numero}', percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.IT, ripetute


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    numero = sys.argv[1]
    cartella = sys.argv[2] if len(sys.argv) == 3 else QUI
    template = os.path.join(cartella, f'chiavi{numero}.txt')
    uscita = os.path.join(cartella, f'rese{numero}.py')

    it, ripetute = carica_traduzioni(numero, cartella)
    righe = io.open(template, encoding='utf-8').read().splitlines()
    inizio = next(i for i, r in enumerate(righe) if r.startswith('# ') and 'righe, da' in r)
    corpo = righe[inizio + 1:]

    fuori = [f'riga {k}: chiave RIPETUTA nel dizionario IT' for k in ripetute]
    viste = set()
    for i, riga in enumerate(corpo):
        # ⚠️ l'inglese col carattere `'` dentro esce fra virgolette doppie
        m = re.match(r"^    \((\d+), ['\"]", riga)
        if not m:
            continue
        n = int(m.group(1))
        viste.add(n)
        if n not in it:
            fuori.append(f'riga {n}: nel template ma senza resa')
            continue
        if not it[n].strip():
            fuori.append(f'riga {n}: la resa e\' vuota')
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
    io.open(uscita, 'w', encoding='utf-8', newline='\n').write(testo)
    print(f'{len(viste)} rese montate in {uscita}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
