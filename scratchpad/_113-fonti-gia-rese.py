# -*- coding: utf-8 -*-
"""113a - I titoli-fonte il cui GIAPPONESE e' gia' reso altrove nel dizionario.

⚠️⚠️ **La rete che mancava alla famiglia della 112a.** `_112-nomi-fonti.py`
cerca i **nomi** per inglese; questa cerca il **titolo intero**, per giapponese,
dentro le voci gia' rese. Se la stessa stringa giapponese e' gia' a schermo con
una resa diversa, il titolo la contraddice — e il giocatore vede due nomi per la
stessa cosa, senza che nessuna rete testuale possa accorgersene: giapponesi
uguali, inglesi diversi, file diversi.

L'ha trovata subito: `異形の森の使者『ロミアス』` sta in `db_card.hsp:10579` e in
`db_creature.hsp:100005`, reso **«<Lomias> il messaggero di Vindale»**, mentre
la tabella della 112a scriveva «messo della foresta deforme» — una terza forma
che nel dizionario non esiste.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_113-fonti-gia-rese.py

Non e' un cancello: e' un referto. Un titolo che il dizionario nomina non e'
per forza un guasto — va **letto**, e il valore atteso non e' zero.
"""
import glob
import importlib.util
import io
import json
import os
import sys

TABELLA = 'scratchpad/lotti-112/titoli_fonte.py'
SOGLIA = 6   # sotto i sei caratteri il giapponese e' una parola comune, non un nome


def titoli():
    spec = importlib.util.spec_from_file_location('titoli_fonte', TABELLA)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.TITOLI_JP


def dizionario():
    """(jp, it, dove) per ogni voce resa, jp non vuoto."""
    fuori = []
    for percorso in sorted(glob.glob('dizionario/*.jsonl')):
        nome = os.path.basename(percorso).replace('.jsonl', '')
        with io.open(percorso, encoding='utf-8') as f:
            for linea in f:
                if not linea.strip():
                    continue
                voce = json.loads(linea)
                jp = (voce.get('jp') or '').strip()
                it = (voce.get('it') or '').strip()
                if jp and it:
                    fuori.append((jp, it, '%s:%d' % (nome, voce['riga'])))
    return fuori


def main():
    tavola = titoli()
    voci = dizionario()

    trovati = 0
    for jp_titolo, it_titolo in sorted(tavola.items()):
        nudo = jp_titolo.strip('～?〜').strip()
        if len(nudo) < 4:
            continue
        # ⚠️ NON l'uguaglianza: il titolo e' la voce del dizionario PIU' una
        #    coda che dice di che tipo di riga si tratta — 『ロミアス』 e poi
        #    「の言葉」, «le parole di». Cercando l'uguale la rete ha detto
        #    «0 su 200» e taceva proprio sul caso che l'aveva fatta nascere.
        colpi = sorted(
            ((jp, it, dove) for jp, it, dove in voci
             if len(jp) >= SOGLIA and jp in nudo),
            key=lambda t: -len(t[0]))
        visti = set()
        unici = []
        for jp, it, dove in colpi:
            if it in visti:
                continue
            visti.add(it)
            unici.append((jp, it, dove))
        colpi = unici
        if not colpi:
            continue
        trovati += 1
        print('### %s' % jp_titolo)
        print('    tabella    %s' % it_titolo)
        for jp, it, dove in colpi[:4]:
            print('    gia\' reso  %-26s  %-40s  %s' % (jp[:26], it[:40], dove))
        print()

    print('titoli il cui giapponese e\' gia\' reso altrove: %d su %d'
          % (trovati, len(tavola)))
    print('ⓘ non e\' un cancello: ogni riga va letta. Una resa che coincide va bene;')
    print('  una che diverge e\' un nome doppio a schermo.')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
