# -*- coding: utf-8 -*-
"""Il **settimo punto cieco**: le righe nude che `nudi_en.py` non guarda.

Sospettato dalla 52ª su `tcg.hsp:2804`-`:2810` (`if ( … ) { buff = "…" }`) e
misurato dalla 53ª, che l'ha trovato per un'altra strada: l'intestazione
dell'editor del mazzo (`tcg.hsp:3348`-`:3360`) e' **tutta inglese** e nessun
referto la elencava.

Le due cause sono INDIPENDENTI, e stanno tutt'e due in `nudi_en.py:43`-`:50`:

1. **l'ancora `^`.** `_DISEGNA` e `_COMPONE` si applicano alla riga *strippata*,
   quindi un'assegnazione o un `mes` scritti **dopo** un `if ( … ) {` sulla
   stessa riga non fanno scattare niente.
2. **il suffisso di modulo.** `_COMPONE` elenca `s`, `buff`, `valn`… e in HSP
   una variabile di modulo si scrive `s@tcg`: **`s@tcg` non e' `s`**.

⚠️ Non e' `blocchi_en.py` (li' il ramo di lingua c'e'), non e' `else_jp.py`,
non e' `tabelle_en.py` (li' il testo arriva a schermo per **indice**). Qui la
riga disegna o compone come tutte le altre: e' solo scritta in una forma che il
quinto referto non riconosce.

Come `nudi_en`, struttura e lingua sono due misure diverse: **struttura** e'
quante righe cosi' fatte ci sono nel sorgente pinnato, **da fare** quelle che
nella build sono ancora identiche al sorgente.
"""
import glob
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nudi_en import (BUILD, SORGENTE, _DISEGNA, _COMPONE, _LETTERALE,
                     _PER_CHIAVE, _e_testo, righe_nude)

# Quel che sta dentro le graffe di un `if`/`else` sulla stessa riga, e che
# `nudi_en` non guarda perche' le sue regole partono da `^`.
# ⚠️ Le graffe di HSP sono anche quelle di `repeat`/`loop`: la forma da cercare
#    e' «qualcosa, poi `{`, poi codice» — non solo `if`.
_DOPO_GRAFFA = re.compile(r'\{\s*(.+?)\s*\}?\s*$')
# La stessa `_COMPONE` di `nudi_en`, ma con il suffisso di modulo ammesso.
# ⚠️ Il suffisso e' `@nome` oppure `@` nudo (in HSP `s@` vuol dire «di questo
#    modulo»), e va messo PRIMA dell'eventuale indice: `s@tcg(3)`.
# ⚠️⚠️ E l'indice non e' per forza una CIFRA. Scritta `\(\s*\d+\s*\)` questa
#    regola perdeva `s@tcg(cnt) += " [Use]"` (`tcg.hsp:2484`), cioe' proprio
#    l'etichetta del mazzo in uso nel menu di scelta del mazzo — una riga che si
#    legge ogni volta che si apre l'editor. E' la lezione di `_PERCORSO` e di
#    ` gp` per l'ennesima volta: **una regola si prova su una riga vista a
#    schermo**. Dentro le parentesi ci puo' stare qualunque espressione, e a
#    distinguere non e' l'indice: e' il nome della variabile.
_COMPONE_MODULO = re.compile(
    r'^(s|s\d|buff|valn|strhint\w*|locvar_\w*_s\d*|refstr|cardrefskill)'
    r'@\w*\s*(\([^)]*\))?\s*(\+?=)\s'
)


def _e_riga_di_uscita(frammento: str) -> bool:
    """Le due regole di `nudi_en`, piu' quella del suffisso di modulo."""
    return bool(_DISEGNA.match(frammento)
                or _COMPONE.match(frammento)
                or _COMPONE_MODULO.match(frammento))


def righe_cieche(righe: list[str]) -> dict[int, str]:
    """Gli indici (0-based) delle righe che `nudi_en` NON vede, col motivo."""
    gia_viste = set(righe_nude(righe))
    trovate = {}
    for i, riga in enumerate(righe):
        if i in gia_viste:
            continue
        s = riga.strip()
        # ⚠️ In HSP il commento e' anche `;`, e `nudi_en` non lo scarta: qui
        #    serve, perche' `tcg.hsp:2577` e' una riga SPENTA che avrebbe fatto
        #    numero da sola («…forbids Mani…», identica alla :2586 che e' viva).
        if not s or s[0] == ';' or s.startswith('//') or s.startswith('#') or s.startswith('/*'):
            continue
        if 'lang(' in s or s.startswith('cnv_str') or _PER_CHIAVE.search(s):
            continue
        if not any(_e_testo(m) for m in _LETTERALE.findall(s)):
            continue
        # Causa 2: la riga comincia gia' con una composizione, ma di modulo.
        if _COMPONE_MODULO.match(s):
            trovate[i] = 'modulo'
            continue
        # Causa 1: la parte utile sta dopo una graffa.
        m = _DOPO_GRAFFA.search(s)
        if m and _e_riga_di_uscita(m.group(1)):
            trovate[i] = 'dopo-graffa'
    return trovate


def main(argv: list[str]) -> None:
    nomi = argv or sorted(os.path.basename(p) for p in glob.glob(SORGENTE + r'\*.hsp'))
    tot_struttura = tot_da_fare = 0
    per_causa = {'dopo-graffa': 0, 'modulo': 0}
    for nome in nomi:
        sorg = io.open(os.path.join(SORGENTE, nome), encoding='cp932').read().split('\n')
        percorso_build = os.path.join(BUILD, nome)
        build = (io.open(percorso_build, encoding='cp932').read().split('\n')
                 if os.path.exists(percorso_build) else sorg)
        trovate = righe_cieche(sorg)
        if not trovate:
            continue
        # ⚠️ Stessa cautela di `nudi_en`: se la build ha piu' righe del sorgente
        #    l'allineamento per indice non vale, e la riga si cerca per contenuto.
        allineata = len(build) == len(sorg)
        insieme = set(build)
        if allineata:
            intatte = [i for i in sorted(trovate) if build[i] == sorg[i]]
        else:
            intatte = [i for i in sorted(trovate) if sorg[i] in insieme]
        tot_struttura += len(trovate)
        tot_da_fare += len(intatte)
        for causa in trovate.values():
            per_causa[causa] += 1
        stato = '' if allineata else "  (build piu' lunga: confronto per contenuto)"
        print(f'=== {nome}: {len(trovate)} righe, {len(intatte)} ancora intatte{stato}')
        for i in intatte:
            print(f'  {i+1:6d} | [{trovate[i]}] {sorg[i].strip()[:110]}')
    print(f'--- per causa: dopo-graffa {per_causa["dopo-graffa"]}, '
          f'suffisso di modulo {per_causa["modulo"]}')
    print(f'--- struttura: {tot_struttura} righe | ancora da fare: {tot_da_fare}')


if __name__ == '__main__':
    main(sys.argv[1:])
