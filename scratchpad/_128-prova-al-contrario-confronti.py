# -*- coding: utf-8 -*-
"""La prova al contrario del cancello dei confronti morti.

⚠️ Una guardia nuova non si crede finche' non la si e' puntata dove il difetto
c'e' di sicuro (regola della 97a, e la 107a ha aggiunto che la prova stessa puo'
essere spenta senza dirlo). Qui il caso peggiore non si ipotizza: si **ricostruisce**
l'albero di ieri, cioe' la build senza le quattro toppe della 128a, e si pretende
che il cancello si accenda su tutte e quattro nominandole.

Non tocca ne' `toppe.jsonl` ne' l'albero di build: copia i `.hsp` in una cartella
di lavoro e li' disfa le quattro sostituzioni.
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
QUI = os.path.dirname(os.path.abspath(__file__))
REFERTO = os.path.join(QUI, '_128-confronti-contro-un-nome-assegnato.py')

# le quattro toppe della 128a che riparano un confronto, prese da toppe.jsonl
# per nome di file: si disfano rimettendo `cerca` al posto di `sostituisci`
ATTESE = 4


def toppe_dei_confronti():
    fuori = []
    for riga in io.open('toppe.jsonl', encoding='utf-8'):
        t = json.loads(riga)
        if not isinstance(t['cerca'], str):
            continue
        if 'OPERANDO TRADOTTO PER COLLISIONE' in t['motivo'] or \
           'RINVIATA CON CONDIZIONE' in t['motivo']:
            fuori.append(t)
    return fuori


def main():
    toppe = toppe_dei_confronti()
    if len(toppe) != ATTESE:
        raise SystemExit('attese {} toppe di confronto in toppe.jsonl, trovate {}'
                         .format(ATTESE, len(toppe)))

    lavoro = tempfile.mkdtemp(prefix='confronti-ieri-')
    try:
        for nome in os.listdir(BUILD):
            if nome.endswith('.hsp'):
                shutil.copy2(os.path.join(BUILD, nome), os.path.join(lavoro, nome))
        for d in os.listdir(os.path.join(BUILD, 'defines')) if os.path.isdir(
                os.path.join(BUILD, 'defines')) else []:
            pass

        for t in toppe:
            percorso = os.path.join(lavoro, t['file'])
            # ⚠️⚠️ NON si disfa rimettendo `cerca`: la toppa di text.hsp e'
            # dichiarata `prima`, quindi nella build la sua riga porta ANCHE la
            # sostituzione del dizionario («none» -> «Nessuna») e non somiglia
            # ne' a `cerca` ne' a `sostituisci`. Quel che tutte e quattro hanno
            # in comune e' la forma: allargano una condizione, cioe' infilano
            # una CODA prima del ` ) {`. Si toglie quella.
            if not t['cerca'].endswith(' ) {') or not t['sostituisci'].endswith(' ) {'):
                raise SystemExit('{}: non e\' un allargamento di condizione'.format(t['file']))
            coda = t['sostituisci'][len(t['cerca']) - 4:-4]
            if not coda.startswith(' | '):
                raise SystemExit('{}: coda inattesa {!r}'.format(t['file'], coda[:40]))
            righe = io.open(percorso, encoding='cp932').read().split('\n')
            quante = sum(1 for r in righe if coda in r)
            if quante == 0:
                # ⓘ le due toppe dello scavo (:5584 e :5685) portano la STESSA
                # coda su due righe: la prima delle due la toglie da tutt'e due,
                # e quando arriva la seconda non c'e' piu' niente da togliere.
                print('gia\' disfatta  {}  coda{}'.format(t['file'], coda[:56]))
                continue
            righe = [r.replace(coda, '') if coda in r else r for r in righe]
            with io.open(percorso, 'w', encoding='cp932', newline='') as f:
                f.write('\n'.join(righe))
            print('disfatte {} righe  {}  coda{}'.format(quante, t['file'], coda[:56]))

        print('\n--- il cancello, puntato sull\'albero di ieri:\n')
        esito = subprocess.call(
            [sys.executable, REFERTO, '--albero', lavoro],
            env=dict(os.environ, PYTHONIOENCODING='utf-8'))
        if esito == 0:
            raise SystemExit('\n⚠️⚠️⚠️ LA PROVA AL CONTRARIO NON SI E\' ACCESA: '
                             'il cancello non vede i quattro difetti che ci sono.')
        print('\n✅ il cancello si accende dove il difetto c\'e\'.')
    finally:
        shutil.rmtree(lavoro, ignore_errors=True)


if __name__ == '__main__':
    main()
