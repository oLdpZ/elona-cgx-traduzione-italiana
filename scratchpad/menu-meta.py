# -*- coding: utf-8 -*-
"""I menu che il giocatore leggerebbe META' IN ITALIANO E META' IN INGLESE.

⚠️⚠️ **La rete che manca**, trovata nella 76a. `gemelle.annota_menu()` misura
quanto di un menu copre *un lotto*, e lo fa mentre si prepara il lotto; ma
nessuno guarda **lo stato del file**, cioe' quali menu sono gia' oggi a meta'.
E un menu si puo' bucare anche senza che se ne tocchi una riga: le firme sono
condivise, quindi tradurre una voce in un punto del file ne traduce un'altra a
diciottomila righe di distanza, dentro un menu che nessuno stava guardando.
(76a: il «No.» di `chat.hsp:24653` e' lo stesso di `:6277`, che sta nel menu del
venditore di Jure a Noyel.)

Un menu e' un gruppo di `chatList` vicine (`gemelle.blocchi_menu`), cioe' quel
che il giocatore vede in una schermata sola. Il referto elenca i gruppi in cui
almeno una voce e' tradotta e almeno una no.

    python scratchpad/menu-meta.py chat.hsp [altro.hsp ...]
"""
import io
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti import estrai, gemelle, percorsi


def meta_e_meta(nome: str) -> list[dict]:
    """I menu a meta' di un file.

    ⚠️ **Le rinviate contano come fatte.** `chat.hsp:19327` e `:19334` sono due
    righe **commentate** a monte (`// chatList 84, ...`): non le disegna nessuno,
    e sono in `rinviate.jsonl` per questo. Senza toglierle, la rete lascerebbe un
    menu «a meta'» per sempre, e l'unico modo di chiuderlo sarebbe tradurre codice
    morto — che e' proprio quel che il rinvio esiste per non fare.
    """
    testo = (percorsi.SORGENTE_HSP / nome).read_bytes().decode('cp932', errors='replace')
    tradotte = estrai.firme_tradotte(nome) | estrai.carica_rinviate(None, nome)
    per_riga: dict[int, list[dict]] = {}
    for voce in estrai.estrai_da_testo(nome, testo):
        per_riga.setdefault(voce['riga'], []).append(voce)

    referto = []
    for blocco in gemelle.blocchi_menu(testo):
        voci = [v for n in blocco for v in per_riga.get(n, [])]
        if not voci:
            continue
        fatte = [v for v in voci if v['firma'] in tradotte]
        restano = [v for v in voci if v['firma'] not in tradotte]
        if fatte and restano:
            referto.append({
                'da': blocco[0], 'a': blocco[-1], 'voci': len(voci),
                'fatte': len(fatte), 'restano': restano,
            })
    return referto


def main() -> int:
    nomi = sys.argv[1:] or ['chat.hsp']
    totale = 0
    for nome in nomi:
        referto = meta_e_meta(nome)
        totale += len(referto)
        for m in referto:
            print('%s:%d-%d   %d voci, %d tradotte, %d no'
                  % (nome, m['da'], m['a'], m['voci'], m['fatte'], len(m['restano'])))
            for v in m['restano'][:6]:
                print('        :%-6d %r' % (v['riga'], (v['en'] or '')[:60]))
            if len(m['restano']) > 6:
                print('        ... e altre %d' % (len(m['restano']) - 6))
    print()
    print('menu a meta\': %d' % totale)
    return 0


if __name__ == '__main__':
    sys.exit(main())
