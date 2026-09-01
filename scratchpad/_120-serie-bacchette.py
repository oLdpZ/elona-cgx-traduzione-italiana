# -*- coding: utf-8 -*-
"""120a - Misura la SERIE delle bacchette (`FILTER_ITEM_ROD`, lotto 056).

Trentadue righe che aprono tutte con la stessa formula. La domanda che il
dossier non risponde da solo, perche' mostra una voce per volta:

  1. quante aprono **esattamente** uguale, e quale diverge;
  2. quali righe hanno il **giapponese identico** fra loro — perche' allora le
     rese devono essere identiche, o si finisce con due rese diverse per lo
     stesso originale (che e' cio' che `battute --divergenti` misura);
  3. se all'inglese la divergenza sia arrivata o no.

E' la lezione della 119a — cercare per struttura, sull'originale — resa
meccanica su un lotto dove la struttura e' dichiarata.
"""
import collections
import importlib.util
import io
import json
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
LAVORO = 'lavoro/_107-daitem.jsonl'
APERTURA = '特定の魔法が封じ込められた'


def righe_del_lotto(numero, cartella):
    p = os.path.join(cartella, 'righe%s.py' % numero)
    spec = importlib.util.spec_from_file_location('righe', p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.RIGHE


def main():
    numero = sys.argv[1] if len(sys.argv) > 1 else '056'
    cartella = sys.argv[2] if len(sys.argv) > 2 else 'scratchpad/lotti-113'
    righe = righe_del_lotto(numero, cartella)

    voci = {}
    for l in io.open(LAVORO, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d['riga'] in righe:
            voci[d['riga']] = d

    print('lotto %s: %d righe' % (numero, len(voci)))

    # 1. l'apertura: chi non dice esattamente la stessa cosa
    print('\n=== L\'APERTURA (fino al primo punto giapponese)')
    aperture = collections.Counter()
    for r, d in voci.items():
        jp = d['jp'].replace('\\t', '')
        aperture[jp.split('。')[0] + '。'] += 1
    for testa, n in aperture.most_common():
        segno = '  ' if n > 1 else '⚠️'
        print('%s %3d x  %s' % (segno, n, testa))
    if len(aperture) == 1:
        print('  ⓘ tutte uguali: la serie non ha gradini nell\'apertura')

    # 2. il giapponese identico fra due righe: le rese devono coincidere
    print('\n=== LE RIGHE COL GIAPPONESE IDENTICO')
    per_jp = collections.defaultdict(list)
    for r, d in voci.items():
        per_jp[d['jp']].append(r)
    doppie = {jp: rr for jp, rr in per_jp.items() if len(rr) > 1}
    if not doppie:
        print('  nessuna: ogni riga ha un giapponese suo')
    for jp, rr in doppie.items():
        print('  ⚠️ %s' % ', '.join(':%d' % r for r in sorted(rr)))
        print('     jp %s' % jp.replace('\\t', '').replace('\\n', ' / ')[:120])
        for r in sorted(rr):
            print('     en :%d  %s' % (r, voci[r]['en'].split('\\n')[0][:100]))
        print('     ⚠️ le rese di queste righe devono essere IDENTICHE: il')
        print('        giapponese e\' lo stesso, e l\'inglese differisce per')
        print('        una sciocchezza che non e\' una differenza di senso.')

    # 3. dove il giapponese distingue e l'inglese no
    print('\n=== DOVE IL GIAPPONESE DISTINGUE E L\'INGLESE APPIATTISCE')
    trovati = 0
    for r, d in sorted(voci.items()):
        jp = d['jp'].replace('\\t', '')
        if jp.startswith(APERTURA) and not jp.startswith(APERTURA + '杖'):
            extra = jp[len(APERTURA):jp.index('杖')]
            print('  ⚠️ :%d  il giapponese dice «%s» prima di 杖' % (r, extra))
            print('        en  %s' % d['en'].split('\\n')[0][:110])
            trovati += 1
    print('  righe con un aggettivo che le altre non hanno: %d' % trovati)
    if trovati:
        print('  ⚠️ se l\'inglese non lo porta, e\' un gradino della serie che')
        print('     si perde rendendo da li\'.')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
