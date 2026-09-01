# -*- coding: utf-8 -*-
"""122a - La riga SORELLA per FRASE, su tutto `db_item.hsp`.

E' lo strumento che la 121a chiedeva, e che questa sessione ha reso urgente
tre volte in tre lotti diversi:

    :99872  (063)  特殊な素材をかけ合わせて…得た**兜**   <- sorella di :100849 (058)
                                                          e di :101769 (060)
    :43044  (063)  かつて世界征服を目論んだ秘密組織…    <- sorella di :43112 e di
                                                          un terzo oggetto reso mesi fa
    :99162  (065)  婚礼の儀において…愛のこめられた**指輪**  <- sorella di :99448 (064),
                                                          chiuso venti minuti prima

Tutte e tre trovate **a mano**, con `_cerca.py` o rileggendo un dossier ancora
aperto. Zero trovate da uno strumento, e su una sessione che riprendesse il
giorno dopo non se ne sarebbe trovata nessuna.

⚠️⚠️ **Perche' gli strumenti che ci sono non bastano, e non sono difettosi:**

    _gia-reso.py             cerca la PROSA INTERA: due righe che differiscono
                             di un carattere sono due prose diverse -> 0
    _120-serie-bacchette.py  raggruppa DENTRO il lotto: la sorella sta fuori
    _coerenza.py             stessa ragione, piu' il fatto che confronta
                             stringhe intere e non frasi
    _122-inglese-doppio      guarda l'INGLESE, non il giapponese

La domanda che nessuno pone e': *questa **frase** del giapponese esiste, quasi
uguale, in un'altra riga del file?* Se la risposta e' si' e quella riga e' gia'
resa, la resa nuova non puo' inventarsi parole diverse per le parti in comune.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_122-sorelle-per-frase.py NNN scratchpad/lotti-113
    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_122-sorelle-per-frase.py --prova

⚠️ Referto da leggere, non un cancello: il valore atteso non e' zero, e una
sorella non e' un difetto. Il difetto e' **non saperlo**.

⭐ `--prova` cerca il caso peggiore invece di ipotizzarlo: punta la rete sulle
tre coppie note qui sopra, che stanno in lotti diversi, e stampa **dove si
accende** — 0.96, 0.98, 1.00. Poi la punta su una riga che sorelle non ne ha
(`:95672`, la battuta di <Barius>) e verifica che **taccia**.

⚠️⚠️ **E al primo giro la prova ha trovato un difetto in questa rete**: due
delle tre coppie si accendevano e la terza no. Il filtro scartava le frasi
**identiche** — scritte per togliere rumore — e `:43044`/`:43112` condividono
la prima e l'ultima frase **parola per parola**. Cioe' la rete taceva
esattamente sul caso piu' forte. Una rete che si prova solo dove ci si aspetta
che funzioni non e' provata.
"""
import collections
import difflib
import importlib.util
import io
import json
import os
import re
import sys
from pathlib import Path

from strumenti.estrai import estrai_da_testo
from strumenti.percorsi import SORGENTE_HSP

FILE = 'db_item.hsp'
DIZIONARIO = Path(__file__).resolve().parent.parent / 'dizionario' / (FILE + '.jsonl')

# sotto questa lunghezza una frase giapponese e' una formula, non una frase
CORTA = 12
# quanto simili devono essere due frasi per essere sorelle
SIMILE = 0.72
# quante 3-grammi in comune servono per passare il prefiltro
SOGLIA_PREFILTRO = 0.45


def frasi(jp):
    """Le frasi di una stringa giapponese, senza la coda del titolo."""
    testo = jp.split('\\n#')[0].replace('\\t', '')
    fuori = [f.strip() for f in re.split('。', testo) if len(f.strip()) >= CORTA]
    return fuori


def trigrammi(f):
    return {f[i:i + 3] for i in range(len(f) - 2)} or {f}


def righe_del_lotto(numero, cartella):
    percorso = os.path.join(cartella, 'righe%s.py' % numero)
    spec = importlib.util.spec_from_file_location('righe%s' % numero, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return sorted(modulo.RIGHE)


def carica():
    testo = (SORGENTE_HSP / FILE).read_text(encoding='cp932')
    voci = estrai_da_testo(FILE, testo)
    rese = {}
    if DIZIONARIO.exists():
        with io.open(DIZIONARIO, encoding='utf-8') as f:
            for linea in f:
                d = json.loads(linea)
                if d.get('it'):
                    rese[d['firma']] = d['it']
    return voci, rese


def indice(voci):
    """3-gramma -> [(riga, frase, insieme di 3-grammi)]"""
    tutte = []
    per_gramma = collections.defaultdict(list)
    for v in voci:
        for f in frasi(v.get('jp') or ''):
            k = len(tutte)
            g = trigrammi(f)
            tutte.append((v['riga'], f, g, v['firma']))
            for t in g:
                per_gramma[t].append(k)
    return tutte, per_gramma


def sorelle(riga, f, g, tutte, per_gramma):
    conta = collections.Counter()
    for t in g:
        for k in per_gramma.get(t, ()):
            conta[k] += 1
    fuori = []
    for k, n in conta.items():
        altra_riga, altra, altri_g, firma = tutte[k]
        # ⚠️ si scarta solo la riga stessa, MAI la frase identica: due righe
        # diverse che dicono la stessa frase sono il caso piu' forte, non il
        # piu' debole. Scartarle era il difetto che la prova al contrario ha
        # preso al primo giro — :43044 e :43112 condividono la prima e
        # l'ultima frase parola per parola, e la rete taceva.
        if altra_riga == riga:
            continue
        if n / max(len(g), len(altri_g)) < SOGLIA_PREFILTRO:
            continue
        r = difflib.SequenceMatcher(None, f, altra).ratio()
        if r >= SIMILE:
            fuori.append((r, altra_riga, altra, firma))
    return sorted(fuori, reverse=True)


def differenza(a, b):
    """Le parti che cambiano fra due frasi, in forma leggibile."""
    pezzi = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b).get_opcodes():
        if tag != 'equal':
            pezzi.append('%s -> %s' % (a[i1:i2] or '∅', b[j1:j2] or '∅'))
    return '   |   '.join(pezzi)


def guarda(righe, voci, rese, tutte, per_gramma, silenzioso=False):
    per_riga = {v['riga']: v for v in voci}
    trovate = []
    for riga in righe:
        v = per_riga.get(riga)
        if v is None:
            continue
        for f in frasi(v.get('jp') or ''):
            for r, altra_riga, altra, firma in sorelle(riga, f, trigrammi(f), tutte, per_gramma):
                trovate.append((riga, f, r, altra_riga, altra, rese.get(firma)))
    if silenzioso:
        return trovate

    print('=== LE FRASI CON UNA SORELLA ALTROVE NEL FILE: %d' % len(trovate))
    print()
    vista = None
    for riga, f, r, altra_riga, altra, resa in trovate:
        if riga != vista:
            print(':%d' % riga)
            vista = riga
        print('    %.2f  contro :%d' % (r, altra_riga))
        print('       qui   %s' % f[:100])
        print('       la    %s' % altra[:100])
        d = differenza(f, altra)
        if d:
            print('       cambia %s' % d[:160])
        if resa:
            print('       ⭐ GIA\' RESA: %s' % resa[:150])
        else:
            print('       ⓘ la sorella non e\' ancora resa')
        print()
    return trovate


def prova(voci, rese, tutte, per_gramma):
    print('=== LA PROVA AL CONTRARIO, sui tre casi noti di questa sessione')
    noti = [
        (99872, 100849, 'i materiali speciali: elmo (063) contro scudo (058)'),
        (99162, 99448, 'il rito nuziale: anello (065) contro collana (064)'),
        (43044, 43112, 'l\'organizzazione segreta: le due parrucche (063)'),
    ]
    esito = 0
    for riga, attesa, che in noti:
        trovate = guarda([riga], voci, rese, tutte, per_gramma, silenzioso=True)
        viste = {t[3] for t in trovate}
        if attesa in viste:
            migliore = max((t[2] for t in trovate if t[3] == attesa))
            print('  ⭐ :%d trova :%d a %.2f  — %s' % (riga, attesa, migliore, che))
        else:
            print('  ⚠️ :%d NON trova :%d, e la sorella c\'e\': la rete e\' rotta — %s'
                  % (riga, attesa, che))
            esito = 1

    # e deve tacere dove sorelle non ce ne sono
    muta = 95672  # la battuta di <Barius>, un indice 2 che non somiglia a niente
    trovate = guarda([muta], voci, rese, tutte, per_gramma, silenzioso=True)
    if trovate:
        print('  ⚠️ si accende su :%d, che sorelle non ne ha: %d frasi'
              % (muta, len(trovate)))
        esito = 1
    else:
        print('  ⭐ tace su :%d, la battuta di <Barius>, che sorelle non ne ha' % muta)
    return esito


def main():
    voci, rese = carica()
    tutte, per_gramma = indice(voci)

    if '--prova' in sys.argv:
        return prova(voci, rese, tutte, per_gramma)

    if len(sys.argv) != 3:
        sys.exit(__doc__)
    righe = righe_del_lotto(sys.argv[1], sys.argv[2])
    trovate = guarda(righe, voci, rese, tutte, per_gramma)

    con_resa = sum(1 for t in trovate if t[5])
    print('lotto %s: %d righe, %d frasi con una sorella, di cui %d gia\' rese'
          % (sys.argv[1], len(righe), len(trovate), con_resa))
    print()
    print('ⓘ referto, non cancello: una sorella non e\' un difetto, non saperlo si\'.')
    print('  Dove la sorella e\' GIA\' RESA, le parti in comune si ricopiano da li\'.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
