# -*- coding: utf-8 -*-
"""124a - Il cancello dei NOMI DI MAPPA: dodici caratteri, non sedici.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_124-nomi-mappa.py

⚠️⚠️⚠️ **PERCHE' ESISTE, E NESSUNO L'AVEVA MAI MISURATO.** Il nome della mappa si
disegna nella barra in alto, e `screen.hsp:153` lo **taglia**:

    if ( strlen(mdatan(MDATAN_NAME)) > 16 - (maplevel() != "") * 4 ) {
        mes cnven(strmid(mdatan(MDATAN_NAME), 0, 16 - (maplevel() != "") * 4))
    }

Sedici caratteri se la mappa non mostra il livello, **dodici se lo mostra** — e
`maplevel()` (`text.hsp:2595`) lo mostra per Lesimas, i sotterranei casuali,
`AREA_QUEST` e ogni mappa di tipo dungeon. Non c'e' nessun avviso: il nome esce
tagliato a meta' parola e basta.

⭐⭐⭐ **IL MODELLO LO CONFERMA MONTE, e non e' un ragionamento circolare**: il
tetto e' scritto nel codice, non ricavato dai dati. I dati servono a vedere se
monte ci sta dentro — e se ci sta, una resa che sfora e' lavoro nostro da
sistemare, non un tetto da allargare.

⚠️ **Questo cancello e' a due livelli e li tiene separati**:

    oltre 16  ->  tagliato SEMPRE, ovunque:            difetto
    13 .. 16  ->  tagliato solo dove si mostra il livello:  da guardare

La seconda riga non e' un difetto automatico, perche' sapere se una mappa mostra
il livello vuol dire sapere il suo `adata(ADATA_TYPE)` a tempo di esecuzione. Si
stampano tutte e due le liste, e la seconda si giudica a mano — con l'etichetta
HSP accanto, che dice di che mappa si tratta.

ⓘ Le cinque mappe rese nella 124a (`map_rand.hsp`) sono tutte `AREA_QUEST`,
cioe' **mostrano il livello**: per loro il tetto e' dodici, e infatti stanno a
9, 12, 5, 10 e 11.
"""
import io
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
sys.path.insert(0, RADICE)

from strumenti import percorsi  # noqa: E402

TETTO_SENZA_LIVELLO = 16
TETTO_CON_LIVELLO = 12

# `mdatan(MDATAN_NAME) = lang("jp", "en")`  oppure  `= "letterale"`
RE_LANG = re.compile(
    r'mdatan\(MDATAN_NAME\)\s*=\s*lang\("((?:[^"\\]|\\.)*)",\s*"((?:[^"\\]|\\.)*)"\)')
RE_NUDO = re.compile(r'mdatan\(MDATAN_NAME\)\s*=\s*"((?:[^"\\]|\\.)*)"\s*$')
RE_ETICHETTA = re.compile(r'^\*(\w+)')


def nomi(cartella):
    """[(file, riga, etichetta, nome)] — i nomi di mappa scritti come letterale."""
    fuori = []
    for nome_file in sorted(os.listdir(cartella)):
        if not nome_file.endswith('.hsp'):
            continue
        percorso = os.path.join(cartella, nome_file)
        etichetta = ''
        testo = io.open(percorso, encoding='cp932', errors='replace').read()
        for numero, riga in enumerate(testo.split('\n'), 1):
            m = RE_ETICHETTA.match(riga)
            if m:
                etichetta = m.group(1)
            m = RE_LANG.search(riga)
            if m:
                fuori.append((nome_file, numero, etichetta, m.group(2)))
                continue
            m = RE_NUDO.search(riga.rstrip())
            if m and m.group(1):
                fuori.append((nome_file, numero, etichetta, m.group(1)))
    return fuori


def referto(cartella, titolo):
    tutti = nomi(cartella)
    sempre = [v for v in tutti if len(v[3]) > TETTO_SENZA_LIVELLO]
    forse = [v for v in tutti if TETTO_CON_LIVELLO < len(v[3]) <= TETTO_SENZA_LIVELLO]
    print()
    print('  === %s' % titolo)
    print('    nomi di mappa letti: %d   il piu\' lungo: %d caratteri'
          % (len(tutti), max(len(v[3]) for v in tutti)))
    print('    TAGLIATI SEMPRE (oltre %d): %d' % (TETTO_SENZA_LIVELLO, len(sempre)))
    for f, n, e, s in sorted(sempre, key=lambda v: -len(v[3])):
        print('       %2d  %-26s %s:%d  *%s' % (len(s), s, f, n, e))
    print('    tagliati DOVE SI MOSTRA IL LIVELLO (%d-%d): %d'
          % (TETTO_CON_LIVELLO + 1, TETTO_SENZA_LIVELLO, len(forse)))
    for f, n, e, s in sorted(forse, key=lambda v: -len(v[3])):
        print('       %2d  %-26s %s:%d  *%s' % (len(s), s, f, n, e))
    return sempre, forse, tutti


def coppie():
    """(en, it, file, riga) per ogni nome di mappa che ha una resa.

    ⚠️⚠️ SI LEGGE IL DIZIONARIO, NON DUE ALBERI. Le righe della build sono
    slittate dalle toppe, quindi appaiare per numero di riga sarebbe appaiare a
    caso; il dizionario tiene en e it sulla stessa voce, ed e' l'unico appaiamento
    che non puo' sbagliare.
    """
    import glob
    import json
    # ⚠️ Per una voce STATICA il campo `contesto` e' vuoto, quindi non si puo'
    #    riconoscere un nome di mappa dal dizionario: si riconosce dal SORGENTE,
    #    che dice file e riga, e il dizionario si interroga con quella chiave —
    #    e' la stessa `riga` che `estrai` ci ha scritto dentro.
    #    ⓘ La prima stesura provava col `contesto` e appaiava ZERO voci: la
    #    prova al contrario l'ha detto invece di lasciar passare uno zero.
    siti = {(f, n): s for f, n, _, s in nomi(percorsi.SORGENTE_HSP)}
    fuori = []
    for percorso in sorted(glob.glob(str(percorsi.DIZIONARIO / '*.jsonl'))):
        for riga in io.open(percorso, encoding='utf-8'):
            if not riga.strip():
                continue
            v = json.loads(riga)
            chiave = (v.get('file'), v.get('riga'))
            if chiave not in siti or not v.get('it'):
                continue
            if v['it'].startswith('"') or ' + ' in v['it']:
                continue          # dinamica: non e' un nome intero
            fuori.append((siti[chiave], v['it'], v['file'], v['riga']))
    return fuori


def main():
    print()
    print('  il tetto lo scrive `screen.hsp:153`: %d caratteri, %d se la mappa'
          % (TETTO_SENZA_LIVELLO, TETTO_CON_LIVELLO))
    print('  mostra il livello (`maplevel()`, text.hsp:2595)')

    sempre_en, forse_en, tutti_en = referto(percorsi.SORGENTE_HSP,
                                            'inglese di monte')
    sempre_it, forse_it, tutti_it = referto(percorsi.BUILD_HSP, 'build italiana')

    # ⚠️⚠️⚠️ IL CANCELLO NON E' «l'italiano sfora», PERCHE' MONTE SFORA ANCHE
    # LUI: cinque nomi inglesi passano i sedici caratteri, e il gioco li taglia
    # da sempre. Un cancello tarato su zero assoluto chiederebbe all'italiano di
    # essere migliore dell'originale, e verrebbe allentato alla prima resa
    # scomoda. Il difetto vero e' il **peggioramento**: un nome che in italiano
    # si taglia dove l'inglese non si tagliava. E' la forma che usa gia'
    # `menu_dialogo` («0 rese peggiorate rispetto all'inglese»).
    print()
    print('  === il cancello: RESE PEGGIORATE rispetto all\'inglese')
    tutte = coppie()
    peggiorate = {}
    for tetto, nome_tetto in ((TETTO_SENZA_LIVELLO, 'sempre'),
                              (TETTO_CON_LIVELLO, 'dove si mostra il livello')):
        peggio = [(en, it, f, r) for en, it, f, r in tutte
                  if len(it) > tetto >= len(en)]
        peggiorate[tetto] = peggio
        print('    tetto %2d (%s): %d peggiorate su %d rese'
              % (tetto, nome_tetto, len(peggio), len(tutte)))
        for en, it, f, r in sorted(peggio, key=lambda v: -len(v[1])):
            print('       %2d  %-26s <- %2d  %-26s %s:%d'
                  % (len(it), it, len(en), en, f, r))

    # ⚠️ Prova al contrario: non una stringa finta. Il tetto piu' stretto e' il
    # 12, e li' il cancello DEVE accendersi su qualcosa, perche' l'italiano e'
    # una lingua piu' lunga dell'inglese su nomi di questa misura. Se non si
    # accendesse nemmeno li', vorrebbe dire che l'appaiamento non trova niente.
    print()
    stretto = peggiorate[TETTO_CON_LIVELLO]
    if stretto:
        peggio = max(stretto, key=lambda v: len(v[1]))
        print('  prova al contrario: al tetto stretto (%d) il cancello SI ACCENDE'
              % TETTO_CON_LIVELLO)
        print('    su %d rese, la peggiore «%s» (%d) contro «%s» (%d).'
              % (len(stretto), peggio[1], len(peggio[1]), peggio[0], len(peggio[0])))
        print('    ⓘ non e\' un difetto automatico: dipende dal tipo della mappa,')
        print('      e le %d qui sopra vanno giudicate una per una.' % len(stretto))
    else:
        print('  ⚠️ prova al contrario MUTA: nemmeno al tetto %d si accende niente.'
              % TETTO_CON_LIVELLO)
        print('    Molto probabilmente l\'appaiamento non trova le voci.')
    print()
    print('  ⓘ per confronto: monte ha %d nomi oltre i %d e %d fra %d e %d.'
          % (len(sempre_en), TETTO_SENZA_LIVELLO, len(forse_en),
             TETTO_CON_LIVELLO + 1, TETTO_SENZA_LIVELLO))
    print()
    return 1 if peggiorate[TETTO_SENZA_LIVELLO] or not stretto else 0


if __name__ == '__main__':
    sys.exit(main())
