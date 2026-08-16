# -*- coding: utf-8 -*-
"""La QUARTA famiglia di riga morta: le `lang()` dentro un commento `//`.

Le prime tre sono il `;` (lotto 006), il blocco `/* … */` (`commenti-blocco.py`,
37ª) e il ramo `if ( jp )` (`lang-nel-ramo-jp.py`, 45ª). La rete 6 dei lotti
guarda le prime due — `sorgente[riga-1].lstrip().startswith(';')` e le righe di
`commenti-blocco` — e **non guarda `//`**, che in HSP spegne la riga esattamente
come il `;`.

Trovata dalla 53ª aprendo `tcg.hsp`: `:1505` e'

    // rtvaln += lang("  ランク:", "  Rank:") + cardrefcost

cioe' il rango della carta, che `estrai` mette nell'estrazione come qualunque
altra voce e che nessuna rete avrebbe fermato. Tradurla e' lavoro speso su testo
che il giocatore non legge — la stessa perdita che le altre tre reti esistono
per impedire.

⚠️ Il conto e' sul **sorgente pinnato**, come `commenti-blocco.py`.
⚠️ E si guarda la **firma**, non la riga sola, per la lezione della 45ª: se la
stessa firma vive altrove, la voce si traduce e la riga morta non conta.
"""
import collections
import glob
import io
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))
from strumenti import estrai, percorsi

SORGENTE = percorsi.SORGENTE_HSP


def righe_barrate(percorso: Path) -> set[int]:
    """Le righe (1-based) spente da un `//` a inizio riga."""
    righe = percorso.read_bytes().decode('cp932', 'replace').split('\n')
    return {i for i, r in enumerate(righe, 1) if r.lstrip().startswith('//')}


def _firme_tradotte(nome: str) -> set[str]:
    return estrai.firme_tradotte(nome)


def main(argv: list[str]) -> None:
    nomi = argv or sorted(os.path.basename(p) for p in glob.glob(str(SORGENTE / '*.hsp')))
    tot_morte = tot_vive_altrove = tot_sprecate = 0
    for nome in nomi:
        percorso = SORGENTE / nome
        if not percorso.exists():
            continue
        barrate = righe_barrate(percorso)
        if not barrate:
            continue
        voci = list(estrai.estrai_da_file(percorso))
        per_firma = collections.defaultdict(list)
        for v in voci:
            per_firma[v['firma']].append(v['riga'])
        morte, vive_altrove = [], []
        for v in voci:
            if v['riga'] not in barrate:
                continue
            righe = per_firma[v['firma']]
            (morte if all(r in barrate for r in righe) else vive_altrove).append(v)
        if not morte and not vive_altrove:
            continue
        # ⚠️ La misura che conta non e' quante sono: e' quante il progetto ha
        #    GIA' tradotto, cioe' il lavoro speso su testo che nessuno legge.
        #    E' la stessa domanda di `misura-blocchi-spenti.py` per il `/* */`
        #    e di `lang-nel-ramo-jp.py` per il ramo giapponese.
        tradotte = _firme_tradotte(nome)
        tot_morte += len(morte)
        tot_vive_altrove += len(vive_altrove)
        sprecate = [v for v in morte if v['firma'] in tradotte]
        tot_sprecate += len(sprecate)
        print(f'=== {nome}: {len(morte)} morte del tutto, '
              f'{len(vive_altrove)} spente qui ma vive altrove, '
              f'{len(sprecate)} GIA\' TRADOTTE')
        for v in morte:
            marca = ' ⚠️ gia tradotta' if v['firma'] in tradotte else ''
            print(f"  {v['riga']:6d} | {v['en'][:90]}{marca}")
    print(f'--- lang() dentro un `//`: {tot_morte} morte del tutto | '
          f'{tot_vive_altrove} vive altrove | {tot_sprecate} gia tradotte')


if __name__ == '__main__':
    main(sys.argv[1:])
