# -*- coding: utf-8 -*-
"""Le `lang()` che stanno dentro un `if ( 0 )`, cioe' la QUARTA famiglia di
riga morta — e la prima che non e' un commento.

Trovata nella 58a su `main.hsp:8490`. Le altre tre le guardano gia' qualcuno:
il `;` la rete 6 dei lotti, il `/* ... */` `misura-blocchi-spenti.py`, il ramo
`if ( jp )` `lang-nel-ramo-jp.py`. Gli `if ( 0 )` non li guardava nessuno.

⚠️ **Il conto e' sul blocco, non sulla riga.** Un `if ( 0 ) {` apre un blocco
che puo' contenerne molte: si segue l'annidamento delle graffe fino alla
chiusura, come farebbe il compilatore.

E' un **referto da leggere**, non una guardia: una riga qui dentro non e' un
difetto nostro, e' testo che upstream ha spento. Ma tradurla e' lavoro buttato,
e — peggio — puo' seppellire la differenza con la riga viva che le sta accanto,
che e' quel che sarebbe successo a `:8490`.
"""
import re
from pathlib import Path

SORGENTE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx')

_SPENTO = re.compile(r'^\s*if\s*\(\s*0\s*\)\s*\{\s*$')
_LANG = re.compile(r'\blang\s*\(')


def righe_spente(righe: list[str]) -> set[int]:
    """Le righe (1-based) dentro un `if ( 0 ) { ... }`, annidamento compreso."""
    fuori: set[int] = set()
    for i, riga in enumerate(righe):
        if not _SPENTO.match(riga):
            continue
        livello = 0
        for j in range(i, len(righe)):
            livello += righe[j].count('{') - righe[j].count('}')
            if j > i:
                fuori.add(j + 1)
            if livello <= 0:
                break
    return fuori


totale_righe = 0
totale_lang = 0
for percorso in sorted(SORGENTE.glob('*.hsp')):
    righe = percorso.read_bytes().decode('cp932', 'replace').split('\n')
    spente = righe_spente(righe)
    if not spente:
        continue
    con_lang = sorted(n for n in spente if _LANG.search(righe[n - 1]))
    totale_righe += len(spente)
    totale_lang += len(con_lang)
    print(f'{percorso.name}: {len(spente)} righe dentro `if ( 0 )`, '
          f'{len(con_lang)} con una lang()')
    for n in con_lang:
        print(f'    :{n}  {righe[n - 1].strip()[:120]}')

print()
print(f'totale: {totale_righe} righe spente da un `if ( 0 )`, '
      f'{totale_lang} con una lang()')
