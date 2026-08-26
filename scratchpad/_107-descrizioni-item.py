# -*- coding: utf-8 -*-
"""107a - Le 5.284 descrizioni di `db_item.hsp` contro il pannello che le disegna.

⚠️ **I quattro indici NON sono la stessa cosa e non hanno lo stesso vincolo.**
E' la cosa che il conteggio «5.284 descrizioni» nasconde, ed e' il motivo per
cui questo file non e' un lotto ma un fronte da aprire con un piano.

    description(0..2)   il CORPO del pannello «Conoscenza dell'oggetto».
                        `command.hsp:16746` fa `repeat 3`, salta le vuote,
                        passa da `trimdesc(desc, 2)` (via i `\t` e TUTTI i `#`),
                        spezza sui `\n` con `notesel`/`noteget`, e **solo** le
                        righe piu' lunghe di 66 caratteri (`:16758`) finiscono
                        nell'impaginatore ANNA CUSTOM di `:16802`-`:16829`.
                        Le altre si stampano intere.

    description(3)      il **rapporto di identificazione**, e passa da tutt'altra
                        parte: `:16275`, `cnven(trimdesc(description(3), 1))`.
                        `trimdesc` con 1 **tronca al primo `#`** e toglie il
                        primo `\n`. ⚠️⚠️ E poi finisce in `listn` **senza
                        nessun impaginatore**: non va a capo, non si taglia,
                        **sfora e basta**. E' l'unica delle quattro con un tetto
                        secco.

L'impaginatore, il rinculo e i tre guasti che ne nascono stanno gia' descritti
in `_102-carta-conoscenza.py`, e da li' si **importano** invece di riscriverli:
e' lo stesso ramo di codice, `command.hsp:16802`, e due copie divergerebbero.

    python scratchpad/_107-descrizioni-item.py            # il quadro per indice
    python scratchpad/_107-descrizioni-item.py --peggiori 15
    python scratchpad/_107-descrizioni-item.py --prova    # la prova al contrario
"""
import argparse
import collections
import importlib.util
import re
from pathlib import Path

from strumenti.percorsi import SORGENTE_HSP

# il fratello ha un trattino nel nome e non si importa con `import`
_spec = importlib.util.spec_from_file_location(
    '_102_carta_conoscenza', Path(__file__).with_name('_102-carta-conoscenza.py'))
_102 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_102)
BUDGET, impagina, spezza_parola = _102.BUDGET, _102.impagina, _102.spezza_parola

FILE = 'db_item.hsp'

# `command.hsp:16758`: sotto questa soglia la riga si stampa intera
SOGLIA_IMPAGINA = 66

# ⚠️ Nel SORGENTE `\n` sono DUE caratteri (barra rovescia + n): e' HSP a
# tradurlo in un a capo a tempo di esecuzione. Chi cerca un `'\n'` vero qui
# non trova niente e conta zero senza dirlo.
ACAPO = chr(92) + 'n'
TABULA = chr(92) + 't'

LETTERALE = re.compile(r'^\s*description\((\d+)\)\s*=\s*"(.*)"\s*$')


def carica():
    """(riga, indice, en) per ogni `description(N)` del ramo `else` di db_item.

    Il ramo si segue con le graffe: dentro `DBMODE_DESC` c'e' `if ( jp ) { }
    else { }` e nient'altro, misurato da `_107-struttura-db-item.py` (1321
    blocchi, 0 asimmetrici, 0 non letterali).
    """
    righe = (SORGENTE_HSP / FILE).read_text(encoding='cp932').splitlines()
    fuori = []
    n = 0
    while n < len(righe):
        if not righe[n].strip().startswith('if ( dbmode == DBMODE_DESC )'):
            n += 1
            continue
        prof = righe[n].count('{') - righe[n].count('}')
        inizio, n = n, n + 1
        while n < len(righe) and prof > 0:
            prof += righe[n].count('{') - righe[n].count('}')
            n += 1
        corpo = righe[inizio:n]

        dove, p = None, 0
        for i, riga in enumerate(corpo):
            nudo = riga.strip()
            if dove is None:
                if nudo == 'if ( jp ) {':
                    dove, p = 'jp', 1
                elif nudo == 'else {':
                    dove, p = 'en', 1
                continue
            p += riga.count('{') - riga.count('}')
            if p <= 0:
                dove = None
                continue
            m = LETTERALE.match(riga)
            if m and dove == 'en':
                fuori.append((inizio + i + 1, int(m.group(1)), m.group(2)))
    return fuori


def trimdesc(testo, modo):
    """`command.hsp:15947`, il ramo `en` (per noi `en = TRUE`, quindi niente virgole)."""
    q = testo.replace(TABULA, '')
    if modo == 1:
        q = q.replace(ACAPO, '', 1)
        taglio = q.find('#')
        if taglio != -1:
            q = q[:taglio]
    if modo == 2:
        q = q.replace('#', '')
    return q


def righe_a_schermo(testo):
    """Il corpo (indici 0-2): trimdesc 2, spezza sui `\n`, impagina solo se > 66.

    Rende (righe, perduti) dove `perduti` sono i caratteri che il pannello non
    scrive mai — la coda che sparisce di `_102`.
    """
    q = trimdesc(testo, 2)
    fuori, perduti = [], 0
    for linea in q.split(ACAPO):
        if len(linea) > SOGLIA_IMPAGINA:
            pezzi, consumati = impagina(linea)
            fuori += pezzi
            perduti += len(linea) - consumati
        else:
            fuori.append(linea)
    return fuori, perduti


def quadro(voci):
    per_indice = collections.defaultdict(list)
    for riga, i, en in voci:
        per_indice[i].append((riga, en))

    print(f'{FILE}: {len(voci)} descrizioni nel ramo en, '
          f'{len(set(t for _, _, t in voci))} testi distinti')
    print(f'budget del riquadro: {BUDGET} caratteri '
          f'(600 px meno l\'inset di 68, a 7,7 px/carattere)')
    print()
    print('  idx    n   vuote  distinti  mediana   max   >66  con \\n  con #')
    print('  ' + '-' * 62)
    for i in sorted(per_indice):
        testi = [t for _, t in per_indice[i]]
        vive = [t for t in testi if t]
        lung = sorted(len(t) for t in vive) or [0]
        print(f'  {i:>3} {len(testi):>5}  {sum(1 for t in testi if not t):>5}'
              f'  {len(set(vive)):>8}  {lung[len(lung) // 2]:>7}  {lung[-1]:>5}'
              f'  {sum(1 for t in vive if len(t) > SOGLIA_IMPAGINA):>4}'
              f'  {sum(1 for t in vive if ACAPO in t):>6}'
              f'  {sum(1 for t in vive if "#" in t):>5}')

    print()
    print('IL CORPO (indici 0-2), passato per l\'impaginatore vero:')
    coda, rotte, oltre, totale = 0, 0, 0, 0
    peggio = []
    for i in (0, 1, 2):
        for riga, en in per_indice.get(i, []):
            if not en:
                continue
            totale += 1
            fuori, perduti = righe_a_schermo(en)
            larghe = sum(1 for r in fuori if len(r.rstrip()) > BUDGET)
            q = trimdesc(en, 2)
            spezzate = sum(spezza_parola(l, impagina(l)[0])
                           for l in q.split(ACAPO) if len(l) > SOGLIA_IMPAGINA)
            if perduti:
                coda += 1
                peggio.append((perduti, riga, i, en))
            rotte += spezzate
            oltre += larghe
    print(f'  descrizioni misurate            : {totale}')
    print(f'  con la CODA PERDUTA gia\' in inglese: {coda}')
    print(f'  righe spezzate a meta\' parola   : {rotte}')
    print(f'  righe oltre i {BUDGET} caratteri     : {oltre}')

    print()
    print(f'L\'INDICE 3 (rapporto di identificazione), che NON si impagina:')
    tre = [(r, trimdesc(t, 1)) for r, t in per_indice.get(3, []) if t]
    sforo = [(len(t), r, t) for r, t in tre if len(t) > BUDGET]
    lung = sorted(len(t) for _, t in tre) or [0]
    print(f'  voci vive dopo trimdesc(_, 1)   : {len(tre)}')
    print(f'  mediana {lung[len(lung) // 2]}, massima {lung[-1]}, '
          f'budget {BUDGET}')
    print(f'  ⚠️ gia\' fuori misura in inglese  : {len(sforo)}')
    for n, r, t in sorted(sforo, reverse=True)[:5]:
        print(f'      :{r}  {n} car.  {t[:76]}')

    return peggio


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--peggiori', type=int, default=0)
    ap.add_argument('--prova', action='store_true')
    a = ap.parse_args()

    voci = carica()
    peggio = quadro(voci)

    if a.peggiori:
        print()
        print(f'Le {a.peggiori} che perdono di piu\' (in inglese):')
        for perduti, riga, i, en in sorted(peggio, reverse=True)[:a.peggiori]:
            print(f'  :{riga} desc({i})  -{perduti} car.  {en[:100]}')

    if a.prova:
        print()
        print('PROVA AL CONTRARIO')
        print('  La coda sparisce quando le righe vengono CORTE: i giri sono')
        print('  strlen/61+1 ma ogni riga ne consuma 57 se il confine cade in')
        print('  fondo al rinculo. Un testo con uno spazio al 57o carattere e')
        print('  nessun confine prima e\' il caso peggiore costruibile.')
        modello = 'x' * 56 + ' '
        acceso = None
        for ripetizioni in range(2, 40):
            finto = (modello * ripetizioni).rstrip()
            righe, perduti = righe_a_schermo(finto)
            if perduti:
                acceso = (len(finto), len(righe), perduti)
                break
        if acceso:
            print(f'  ✅ ACCESA: al primo testo di {acceso[0]} caratteri ne perde '
                  f'{acceso[2]} in coda ({acceso[1]} righe scritte)')
        else:
            print('  ⚠️⚠️ SPENTA anche sul caso peggiore: la rete NON vede il '
                  'guasto per cui e\' nata, e il suo zero non vale niente')

        # e il rovescio: un testo innocuo non deve accenderla
        falsi = 0
        for lunghezza in (10, 40, 66, 67, 120, 300):
            testo = ' '.join(['parola'] * (lunghezza // 7 + 1))[:lunghezza]
            _, p = righe_a_schermo(testo)
            if p:
                falsi += 1
                print(f'  ⚠️ FALSO POSITIVO su un testo di {lunghezza} caratteri')
        if not falsi:
            print('  ✅ muta su sei testi innocui da 10 a 300 caratteri')


if __name__ == '__main__':
    main()
