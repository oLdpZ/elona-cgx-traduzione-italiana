# -*- coding: utf-8 -*-
"""I blocchi `if ( en ) { ... }` con letterali nudi fuori da `lang()`.

Sono invisibili a `estrai.py`: la meta' inglese della frase non e' nel dizionario
e resta inglese anche quando la meta' dentro `lang()` e' tradotta. E' la stessa
classe della scoperta 1 della 28ª su `bufftxt`.

⚠️ **Struttura e lingua sono due misure diverse, e confonderle da' un numero
falso.** La prima stesura leggeva solo la build e contava **136** righe «da
fare»: ma la build contiene anche quelle **gia' sistemate** — gli articoli
italiani di `item_func.hsp` (`locvar_itemname_s8 = "una "`) sono letterali nudi
dentro `if ( en )` esattamente come quelli inglesi, e finivano nel conto.

Quindi si misurano tutt'e due:

- **struttura**: quante righe cosi' fatte ci sono nel **sorgente pinnato**;
- **da fare**: quelle che nella **build** sono ancora **identiche al sorgente**,
  cioe' che nessuno ha ancora toccato ne' con una toppa ne' altrimenti.
"""
import glob
import io
import os
import re
import sys

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'

_LETTERALE = re.compile(r'"[^"]*[A-Za-z][^"]*"')
_APRE = re.compile(r'^if\s*\(\s*en\s*\)\s*\{?\s*$')


def righe_nude(righe: list[str]) -> list[int]:
    """Gli indici (0-based) delle righe con letterali nudi dentro `if ( en )`."""
    trovati = []
    dentro = False
    for i, riga in enumerate(righe):
        s = riga.strip()
        if _APRE.match(s):
            dentro = True
            continue
        if dentro:
            if 'lang(' not in riga and _LETTERALE.search(riga):
                trovati.append(i)
            if s.startswith('}'):
                dentro = False
    return trovati


def main(argv: list[str]) -> None:
    nomi = argv or sorted(os.path.basename(p) for p in glob.glob(SORGENTE + r'\*.hsp'))
    tot_struttura = tot_da_fare = 0
    for nome in nomi:
        sorg = io.open(os.path.join(SORGENTE, nome), encoding='cp932').read().split('\n')
        percorso_build = os.path.join(BUILD, nome)
        build = (io.open(percorso_build, encoding='cp932').read().split('\n')
                 if os.path.exists(percorso_build) else sorg)
        indici = righe_nude(sorg)
        if not indici:
            continue
        # ⚠️ La build puo' avere piu' righe del sorgente (gli inserimenti di
        #    `applica_dati_nome`): allora l'allineamento per indice non vale e la
        #    riga si cerca per contenuto in tutto il file.
        allineata = len(build) == len(sorg)
        if allineata:
            intatte = [i for i in indici if build[i] == sorg[i]]
        else:
            insieme = set(build)
            intatte = [i for i in indici if sorg[i] in insieme]
        tot_struttura += len(indici)
        tot_da_fare += len(intatte)
        stato = '' if allineata else '  (build piu\' lunga: confronto per contenuto)'
        print(f'=== {nome}: {len(indici)} righe, {len(intatte)} ancora intatte{stato}')
        for i in intatte:
            print(f'  {i+1:6d} | {sorg[i].strip()[:120]}')
    print(f'--- struttura: {tot_struttura} righe | ancora da fare: {tot_da_fare}')


if __name__ == '__main__':
    main(sys.argv[1:])
