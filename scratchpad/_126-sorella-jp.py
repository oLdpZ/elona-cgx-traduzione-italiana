# -*- coding: utf-8 -*-
"""La fonte che le righe nude sembravano non avere: la **sorella giapponese**.

Una riga inglese nuda non ha firma, non ha voce di dizionario e per questo si
legge come se avesse **una fonte sola**, l'inglese. Ma la forma che le produce
quasi tutte e' questa:

    if ( jp ) {
        txt "「カネなら渡すから、許して" + _kure(3) + "！」", ...
    }
    else {
        txt cnvtalk("I'll give you all I have, please don't kill me....!"), ...
    }

⭐ **Il giapponese c'e', sta tre righe sopra, e non e' dentro la stessa
`lang()`.** E' esattamente la coppia di sempre — originale e riscrittura — solo
scritta con un `if` invece che con una funzione. Chi topa leggendo solo l'`else`
lavora con una fonte su due, e la regola della 110a («le fonti sono cinque»)
resta scoperta proprio dove nessuna rete la copre.

⚠️ **La sorella non e' una traduzione: e' spesso una riscrittura.** Nel blocco
degli insulti l'inglese di `proc.hsp:19733` e' lo stesso di `:26024`, e i due
giapponesi non si somigliano per niente: l'inglese ha ricopiato un pool solo
sotto due mosse diverse. La sorella serve a **vedere** questi casi, non a
sostituire l'inglese d'ufficio.

ⓘ Il ramo si riconosce con la regola della 45a (`^if ( jp ) {`) e l'`else` con
quella di `else_jp.py`: l'`else` sta sulla riga della graffa che chiude o su
quella dopo.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_126-sorella-jp.py
    ... --file proc.hsp        il dossier di un file: en, jp e le voci gia' rese
"""
import collections
import contextlib
import glob
import importlib.util
import io
import json
import os
import re
import sys

_QUI = os.path.dirname(os.path.abspath(__file__))
_PROGETTO = os.path.dirname(_QUI)


def _carica(nome: str, percorso: str):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


tr = _carica('triage_nudi', os.path.join(_QUI, 'triage_nudi.py'))
nu = _carica('nudi_en', os.path.join(_QUI, 'nudi_en.py'))
with contextlib.redirect_stdout(io.StringIO()):
    rj = _carica('lang_nel_ramo_jp', os.path.join(_QUI, 'lang-nel-ramo-jp.py'))

APRE_JP = re.compile(r'^\s*if\s*\(\s*jp\s*\)\s*\{')
_LETTERALE = re.compile(r'"(?:[^"\\]|\\.)*"')


def coppie(righe: list) -> dict:
    """{riga del corpo `else`: [righe del ramo `jp` che portano un letterale]}.

    ⚠️⚠️ **La corrispondenza NON e' riga per riga, e provarci sbaglia in
    silenzio.** Il primo giro di questo strumento accoppiava la n-esima riga di
    qua con la n-esima di la', e su `proc.hsp:19733` ha restituito una **graffa
    chiusa**: il ramo giapponese degli insulti ha un `if` sul sesso dentro, e
    l'`else` no, quindi le due liste non hanno ne' la stessa lunghezza ne' lo
    stesso ordine. Un accoppiamento sbagliato e' peggio di nessuno, perche' si
    legge come una fonte.

    Quindi il ramo `jp` si rende **intero**: e' contesto da leggere, non una
    coppia da fidarsi.
    """
    fuori = {}
    for i, riga in enumerate(righe):
        if not APRE_JP.match(riga):
            continue
        profondita = 0
        for k in range(i, len(righe)):
            senza = _LETTERALE.sub('', righe[k])
            profondita += senza.count('{') - senza.count('}')
            if profondita == 0 and k > i:
                break
        else:
            continue
        corpo_jp = [n for n in range(i + 2, k + 1)    # 1-based, senza le graffe
                    if _LETTERALE.search(righe[n - 1])]
        candidata = None
        for c in (k, k + 1):
            if c < len(righe) and re.search(r'\belse\b', righe[c]):
                candidata = c
                break
        if candidata is None:
            continue
        profondita = 0
        corpo_else = []
        for k2 in range(candidata, len(righe)):
            senza = _LETTERALE.sub('', righe[k2])
            profondita += senza.count('{') - senza.count('}')
            if k2 > candidata:
                corpo_else.append(k2 + 1)
            if profondita == 0 and k2 > candidata:
                break
        if corpo_else:
            corpo_else.pop()                          # la graffa che chiude
        for numero in corpo_else:
            fuori[numero] = corpo_jp
    return fuori


def rese_del_file(nome: str) -> dict:
    """{jp: it} da tutto il dizionario, per riconoscere il gia' reso."""
    fuori = {}
    for percorso in sorted(glob.glob(os.path.join(_PROGETTO, 'dizionario', '*.jsonl'))):
        for l in io.open(percorso, encoding='utf-8'):
            if not l.strip():
                continue
            v = json.loads(l)
            if v.get('it') and v.get('jp'):
                fuori.setdefault(v['jp'], v['it'])
    return fuori


def main(argv: list) -> None:
    solo = argv[argv.index('--file') + 1] if '--file' in argv else None

    con = senza = 0
    per_file = collections.Counter()
    for percorso in sorted(glob.glob(nu.SORGENTE + r'\*.hsp')):
        nome = os.path.basename(percorso)
        if solo and nome != solo:
            continue
        righe = io.open(percorso, encoding='cp932').read().split('\n')
        morte = rj.righe_nel_ramo_jp(righe)
        mappa = coppie(righe)
        vive = [(n, e, t) for n, c, e, t in tr.classifica(nome)
                if c == 'testo' and n not in morte]
        if not vive:
            continue
        if solo:
            rese = rese_del_file(nome)
            print('=== %s: %d righe nude vive' % (nome, len(vive)))
        for numero, eti, testo in vive:
            sorella = mappa.get(numero) or []
            if sorella:
                con += 1
                per_file[nome] += 1
            else:
                senza += 1
            if not solo:
                continue
            print()
            print('--- :%d  (%s)' % (numero, eti))
            print('    en  %s' % testo[:400])
            if not sorella:
                print('    jp  (nessuna sorella: la riga non sta in un `else` di `if ( jp )`)')
                continue
            for n in sorella:
                print('    jp  :%d  %s' % (n, righe[n - 1].strip()[:400]))
            if len(sorella) != 1:
                print('    ⚠️  il ramo jp ha %d righe con testo e l\'else una: '
                      'le due liste NON si accoppiano in ordine' % len(sorella))
            for n in sorella:
                for x in _LETTERALE.findall(righe[n - 1]):
                    grezzo = x[1:-1]
                    # ⓘ Un letterale di un carattere e' una graffa giapponese o
                    #    un punto esclamativo: nel dizionario ci finisce come
                    #    pezzo di un'altra resa, e qui sarebbe solo rumore.
                    if len(grezzo) > 2 and grezzo in rese:
                        print('    ⭐ gia\' reso  %s  ->  %s' % (grezzo, rese[grezzo]))
        if solo:
            return

    print('=== le righe nude vive, e quante hanno una sorella giapponese')
    print('  con sorella (due fonti, come tutto il resto) : %4d' % con)
    print('  senza sorella (l\'inglese e\' l\'unica fonte)   : %4d' % senza)
    print()
    print('=== dove stanno quelle con sorella')
    for nome, quante in per_file.most_common():
        print('  %4d  %s' % (quante, nome))


if __name__ == '__main__':
    main(sys.argv[1:])
