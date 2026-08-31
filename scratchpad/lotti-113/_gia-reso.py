# -*- coding: utf-8 -*-
"""114a - Il CORPO di una riga del lotto puo' essere gia' reso altrove.

`_113-fonti-gia-rese.py` fa questa domanda per le **code** (i titoli-fonte).
Questa la fa per il **corpo**: prende il giapponese di ogni riga del lotto,
gli toglie la coda `\\n#...` e i `\\t` di testa, e cerca quella prosa in tutto
il dizionario. Se c'e' gia' una resa, la resa nuova non deve contraddirla.

⚠️ E' un REFERTO, non un cancello: il valore atteso non e' zero, e ogni riga
trovata va letta. Esce sempre con 0.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-113/_gia-reso.py 029
"""
import glob
import importlib.util
import io
import json
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
LAVORO = 'lavoro/_107-daitem.jsonl'


def corpo(testo):
    """La prosa senza la coda-fonte e senza le tabulazioni di testa."""
    pezzi = (testo or '').split('\\n')
    vivi = [p for p in pezzi if p and not p.startswith('#')]
    return ' '.join(p.replace('\\t', '').strip() for p in vivi).strip()


def main():
    numero = sys.argv[1]
    spec = importlib.util.spec_from_file_location(
        'righe', os.path.join(QUI, 'righe%s.py' % numero))
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    righe = modulo.RIGHE

    voci = []
    for linea in io.open(LAVORO, encoding='utf-8'):
        if linea.strip():
            voce = json.loads(linea)
            if voce['riga'] in righe:
                voci.append(voce)

    # ⚠️ il dizionario si legge una volta sola: e' grande, e riaprirlo per
    #    ogni riga del lotto trasforma un referto di due secondi in un minuto.
    dizionario = []
    for percorso in sorted(glob.glob('dizionario/*.jsonl')):
        for linea in io.open(percorso, encoding='utf-8'):
            if not linea.strip():
                continue
            d = json.loads(linea)
            if d.get('it'):
                dizionario.append((corpo(d.get('jp')), d, os.path.basename(percorso)))

    trovate = 0
    for voce in sorted(voci, key=lambda v: v['riga']):
        mio = corpo(voce.get('jp'))
        if len(mio) < 12:
            continue
        # ⚠️ il contenimento vuole la soglia sui DUE lati. Senza, ogni voce del
        #    dizionario il cui giapponese e' corto (una particella, un `。`) sta
        #    dentro qualunque prosa, e il referto dice «30 su 30» dicendo niente:
        #    e' successo alla prima versione, il 2026-08-31.
        colpi = [(d, dove) for jp, d, dove in dizionario
                 if len(jp) >= 12 and (mio in jp or jp in mio)]
        if not colpi:
            continue
        trovate += 1
        print(':%d' % voce['riga'])
        print('   jp  %s' % mio[:90])
        for d, dove in colpi[:3]:
            print('   IT  %-70s  %s' % ((d.get('it') or '')[:70], dove))
        print()

    print('righe del lotto il cui giapponese e\' gia\' reso altrove: %d su %d'
          % (trovate, len(voci)))
    print("ⓘ referto, non cancello: il valore atteso non e' zero, ogni riga va letta.")
    return 0


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
