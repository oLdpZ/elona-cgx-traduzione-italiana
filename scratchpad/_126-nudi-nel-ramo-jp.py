# -*- coding: utf-8 -*-
"""La classe che mancava al triage delle righe nude: il **ramo giapponese**.

`triage_nudi.py` (125a) spacca le righe inglesi nude in quattro classi trovate
nella FORMA: `spenta` (dentro un `/* ... */`), `dbg` (routine `dbg_*`), `sigla`
(un identificatore camelCase) e `testo` (tutto il resto). Ma «tutto il resto»
porta dentro una quinta famiglia di riga morta, e la 45a l'aveva gia' nominata
per un'altra domanda: **la riga chiusa in un ramo `if ( jp )`**.

⚠️⚠️⚠️ **La build italiana e' il ramo `en`.** Si legge sul titolo:
`system.hsp:3536` apre `if ( jp )` e dentro c'e' l'elenco bilingue del menu,
`:3539` apre `if ( en )` e dentro c'e' quello che la toppa ha reso in italiano.
Le due righe stanno una sotto l'altra, tutt'e due sono «testo» per il triage, e
**una sola delle due il giocatore la legge**.

⚠️ Una riga cosi' non e' come una `spenta`: nel file e' viva, non ha un
carattere che la spenga, e chi la legge nell'elenco la scambia per lavoro.
Toparla e' lavoro speso su testo che nessuno leggera' — la stessa lezione di
`lang-nel-ramo-jp.py`, dall'altro lato dello stesso `if`.

Referto, non guardia: dice quante delle 198 sono da togliere dal conto e quante
restano davvero da fare, spaccate per routine.

ⓘ **Quanto vale il conto.** Il ramo si riconosce con la regola della 45a,
`^if ( jp ) {`, che nel sorgente copre **3.076 aperture su 3.083**: restano
fuori due guardie composte (`... & jp`, `... & en != TRUE`) e cinque condizioni
dove `jp` e' un addendo aritmetico e non un ramo. Il referto quindi puo'
sbagliare **per difetto** di poche righe, mai per eccesso.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_126-nudi-nel-ramo-jp.py
    ... --elenco jp      le righe morte, per controllarle a mano
    ... --elenco vive    le righe che restano da fare
"""
import collections
import contextlib
import glob
import importlib.util
import io
import os
import sys

_QUI = os.path.dirname(os.path.abspath(__file__))


def _carica(nome: str, percorso: str):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


tr = _carica('triage_nudi', os.path.join(_QUI, 'triage_nudi.py'))
nu = _carica('nudi_en', os.path.join(_QUI, 'nudi_en.py'))
# ⚠️ `lang-nel-ramo-jp.py` stampa il suo referto **all'import**: qui serve solo
# `righe_nel_ramo_jp`, e il suo referto in mezzo a questo sarebbe rumore che
# nasconde i numeri veri.
with contextlib.redirect_stdout(io.StringIO()):
    rj = _carica('lang_nel_ramo_jp', os.path.join(_QUI, 'lang-nel-ramo-jp.py'))


def raccogli() -> list:
    """(file, riga, routine, testo, dentro_il_ramo_jp) per ogni riga di classe `testo`."""
    fuori = []
    for percorso in sorted(glob.glob(nu.SORGENTE + r'\*.hsp')):
        nome = os.path.basename(percorso)
        righe = io.open(percorso, encoding='cp932').read().split('\n')
        dentro = rj.righe_nel_ramo_jp(righe)
        for riga, classe, eti, testo in tr.classifica(nome):
            if classe != 'testo':
                continue
            fuori.append((nome, riga, eti, testo, riga in dentro))
    return fuori


def main(argv: list) -> None:
    elenco = argv[argv.index('--elenco') + 1] if '--elenco' in argv else None

    tutto = raccogli()
    morte = [t for t in tutto if t[4]]
    vive = [t for t in tutto if not t[4]]

    if elenco:
        scelte = morte if elenco == 'jp' else vive
        for nome, riga, eti, testo, _ in scelte:
            print('%-20s %6d  %-28s %s' % (nome, riga, eti, testo[:100]))
        print('--- %d righe' % len(scelte))
        return

    print('=== le %d righe nude di classe `testo` (triage_nudi), spaccate per ramo'
          % len(tutto))
    print('  dentro un `if ( jp )`, che la build en non esegue : %4d' % len(morte))
    print('  vive, e sono il lavoro vero                       : %4d' % len(vive))

    print()
    print('=== le morte, per file')
    for nome, quante in collections.Counter(t[0] for t in morte).most_common():
        print('  %4d  %s' % (quante, nome))

    print()
    per_routine = collections.Counter((t[0], t[2]) for t in vive)
    print('=== il lavoro vero, per routine (%d righe in %d routine)'
          % (len(vive), len(per_routine)))
    for (nome, eti), quante in per_routine.most_common(20):
        print('  %4d  %-22s %s' % (quante, nome, eti))
    coda = sum(q for _, q in per_routine.most_common()[20:])
    if coda:
        print('  %4d  (altre %d routine)' % (coda, len(per_routine) - 20))


if __name__ == '__main__':
    main(sys.argv[1:])
