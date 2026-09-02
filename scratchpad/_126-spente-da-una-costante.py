# -*- coding: utf-8 -*-
"""La sesta famiglia di riga morta: il blocco spento da una **costante**.

Le prime cinque si conoscono: la riga commentata col `;`, il blocco `/* ... */`
(`commenti-blocco.py`), il ramo `if ( jp )` che la build `en` non esegue
(`_126-nudi-nel-ramo-jp.py`), la routine `dbg_*` e la sigla (`triage_nudi.py`).
Questa e' la sesta, ed e' la piu' silenziosa di tutte:

    map_rand.hsp:683    if ( FALSE ) {
    map_rand.hsp:691        noteadd "atype["+adata(ADATA_TYPE, …)+"];"
    …                       (altre otto)
    map_rand.hsp:704    }

⚠️⚠️⚠️ **Nove delle righe che il triage chiamava «testo da fare» stavano qui
dentro.** Non c'e' niente che le spenga a vederle: nessun `;`, nessun commento,
nessun ramo di lingua. A spegnerle e' una **costante nella condizione**, che sta
ventuno righe piu' su.

⭐ E non erano testo nemmeno se il blocco girasse: `noteadd "atype[…];"` scrive
un **tabellone di parametri** in `mapinfo_NNNNNN.txt`, il dump con cui l'autore
del mod «JAMES CUSTOM - NEFIA LAYOUT» controllava la generazione delle mappe. Il
giocatore non lo legge, e non e' scritto per essere letto. Due motivi
indipendenti per non tradurle, e il triage non ne vedeva nessuno dei due.

⚠️⚠️⚠️ **E LA GUARDIA SI CERCA NELLA BUILD, NON SOLO NEL SORGENTE — PERCHE' A
SPEGNERE UN BLOCCO PUO' ESSERE STATO IL PROGETTO STESSO.** Il pluralizzatore
inglese di `item_func.hsp:1842` nel sorgente ha una guardia vera
(`if ( locvar_itemname_s2 == "" )`); nella build una toppa l'ha sostituita con
`if ( 0 )`, perche' il plurale italiano viene da `ioriginalnamerefplur` dove il
nome si concatena (`contratto-nomi.md` §4-bis). Le sue cinque righe — `"es"`,
`"ves"`, `"ies"`, `"coffins"` — restano **intatte**, quindi `triage_nudi` le
conta come lavoro, e sono **morte da sessioni**. Un referto che leggesse solo il
sorgente non le vedrebbe: quel che gira e' la build.

ⓘ Le guardie costanti sono **sette nel sorgente** — sei spente (`FALSE` o `0`) e
una accesa (`TRUE`, che non conta) — e nella build ce n'e' almeno una in piu',
messa da una toppa.

⚠️ La regola e' solo `^if ( FALSE|0 ) {`: le condizioni sempre false scritte in
un altro modo — un confronto fra due costanti, una variabile mai assegnata — non
le vede nessuno, e questo referto sbaglia **per difetto**.

⚠️ **L'aggancio fra sorgente e build e' per testo, non per numero di riga**: le
toppe fanno scivolare i numeri. Una riga conta come morta solo se **tutte** le
sue occorrenze nella build stanno dentro un blocco spento — `+= "es"` compare due
volte, e mezza risposta non e' una risposta.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_126-spente-da-una-costante.py
    ... --elenco     le righe nude che stanno dentro, per controllarle a mano
"""
import collections
import contextlib
import glob
import importlib.util
import io
import os
import re
import sys

_QUI = os.path.dirname(os.path.abspath(__file__))


def _carica(nome: str, percorso: str):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


tr = _carica('triage_nudi', os.path.join(_QUI, 'triage_nudi.py'))
nu = _carica('nudi_en', os.path.join(_QUI, 'nudi_en.py'))
with contextlib.redirect_stdout(io.StringIO()):
    rj = _carica('lang_nel_ramo_jp', os.path.join(_QUI, 'lang-nel-ramo-jp.py'))

APRE_SPENTO = re.compile(r'^\s*if\s*\(\s*(?:FALSE|0)\s*\)\s*\{')
LETTERALE = re.compile(r'"(?:[^"\\]|\\.)*"')


def righe_spente(righe: list) -> set:
    """I numeri di riga (1-based) dentro un `if ( FALSE ) { ... }`.

    Stesso conteggio di graffe di `lang-nel-ramo-jp.py`, e stessa cautela: le
    graffe dentro una stringa si tolgono prima di contare.
    """
    dentro = set()
    profondita = None
    for numero, riga in enumerate(righe, 1):
        if profondita is None:
            if APRE_SPENTO.match(riga):
                profondita = 1
            continue
        dentro.add(numero)
        senza = LETTERALE.sub('', riga)
        profondita += senza.count('{') - senza.count('}')
        if profondita <= 0:
            dentro.discard(numero)
            profondita = None
    return dentro


def main(argv: list) -> None:
    elenco = '--elenco' in argv

    dentro_tot = 0
    per_file = collections.Counter()
    vive = 0
    for percorso in sorted(glob.glob(nu.SORGENTE + r'\*.hsp')):
        nome = os.path.basename(percorso)
        righe = io.open(percorso, encoding='cp932').read().split('\n')
        spente = righe_spente(righe)
        nel_ramo_jp = rj.righe_nel_ramo_jp(righe)

        percorso_build = os.path.join(nu.BUILD, nome)
        if os.path.exists(percorso_build):
            righe_build = io.open(percorso_build, encoding='cp932').read().split('\n')
            spente_build = righe_spente(righe_build)
            # {testo della riga: sta SOLO dentro blocchi spenti}
            dove = collections.defaultdict(list)
            for n, r in enumerate(righe_build, 1):
                dove[r].append(n in spente_build)
        else:
            dove = {}

        for numero, classe, eti, testo_riga in tr.classifica(nome):
            if classe != 'testo' or numero in nel_ramo_jp:
                continue
            grezza = righe[numero - 1]
            posti = dove.get(grezza, [])
            morta_nella_build = bool(posti) and all(posti)
            if numero in spente or morta_nella_build:
                dentro_tot += 1
                per_file[nome] += 1
                if elenco:
                    dove_e = 'sorgente' if numero in spente else 'build'
                    print('%-20s %6d  %-8s %-24s %s'
                          % (nome, numero, dove_e, eti, testo_riga[:90]))
            else:
                vive += 1

    if elenco:
        print('--- %d righe' % dentro_tot)
        return

    print('=== le righe nude vive secondo `_126-nudi-nel-ramo-jp`, e la costante')
    print('  dentro un `if ( FALSE )`, che non gira mai : %4d' % dentro_tot)
    print('  vive davvero                              : %4d' % vive)
    print()
    for nome, quante in per_file.most_common():
        print('  %4d  %s' % (quante, nome))


if __name__ == '__main__':
    main(sys.argv[1:])
