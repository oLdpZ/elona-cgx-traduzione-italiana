# -*- coding: utf-8 -*-
"""108a - La rete 5 fuori dal lotto: gli accenti DECOMPOSTI nel dizionario.

La rete 5 del modello di lotto normalizza le rese a NFC prima di scriverle
(`RESE = {k: unicodedata.normalize('NFC', v) ...}`). E' una riga sola, e nei
lotti delle carte dalla 103a in poi **non c'e' piu'**: e' sparita copiando il
lotto 06 nel 07 e non l'ha ripresa nessuno.

Nessuno strumento la sostituisce: `accenti.TABELLA` sostituisce le vocali
**precomposte**, quindi una «é» scritta come `e` + U+0301 gli passa davanti
intatta, arriva a CP932 e diventa un carattere di sostituzione muto.

Questo script guarda il dizionario **intero** e dice quante voci hanno una resa
che non e' in NFC. E' un referto: il valore atteso e' zero.

    PYTHONIOENCODING=utf-8 python scratchpad/_108-accento-decomposto.py

⚠️ La prova al contrario e' in coda e **stampa il punto in cui si accende**, non
un ✅: una prova che passa in silenzio non distingue «ho cercato» da «non ho
trovato».
"""
import collections
import glob
import io
import json
import os
import sys
import unicodedata


def scorri():
    per_file = collections.Counter()
    esempi = []
    voci = 0
    for percorso in sorted(glob.glob(os.path.join('dizionario', '*.jsonl'))):
        nome = os.path.basename(percorso)
        for linea in io.open(percorso, encoding='utf-8'):
            if not linea.strip():
                continue
            voce = json.loads(linea)
            it = voce.get('it') or ''
            if not it:
                continue
            voci += 1
            if it != unicodedata.normalize('NFC', it):
                per_file[nome] += 1
                if len(esempi) < 10:
                    esempi.append((nome, voce.get('riga'), it))
    return voci, per_file, esempi


def prova_al_contrario():
    """Cerca il caso peggiore invece di ipotizzarlo, e dice dove si accende."""
    sano = 'Perché è così: la città è già cadùta.'
    assert sano == unicodedata.normalize('NFC', sano)
    for posizione, carattere in enumerate(sano):
        if unicodedata.normalize('NFD', carattere) == carattere:
            continue
        guasto = (sano[:posizione]
                  + unicodedata.normalize('NFD', carattere)
                  + sano[posizione + 1:])
        if guasto != unicodedata.normalize('NFC', guasto):
            return (f'la prova al contrario si accende sul carattere {posizione} '
                    f'({carattere!r} scomposto in {unicodedata.normalize("NFD", carattere)!r})')
    return None


def main():
    voci, per_file, esempi = scorri()
    for nome, riga, it in esempi:
        print(f'  {nome}:{riga}  {it!r}')
    print()
    print(f'rese con accento DECOMPOSTO: {sum(per_file.values())} su {voci}   (atteso: 0)')
    if per_file:
        for nome, quante in per_file.most_common():
            print(f'    {nome}: {quante}')
    acceso = prova_al_contrario()
    if acceso is None:
        sys.exit('⚠️ la prova al contrario NON si e\' accesa: la rete non prova niente')
    print(acceso)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
