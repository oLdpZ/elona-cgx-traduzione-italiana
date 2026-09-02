# -*- coding: utf-8 -*-
"""124a - «Larneire» con una `n` sola, in una resa gia' in gioco.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_124-correzione-larneire.py

⚠️⚠️⚠️ `screen.hsp:1450` scrive **«Larneire»** dove il progetto scrive
**«Larnneire»** in dodici rese su dodici. Non l'ha trovata una rete: le reti
guardano la forma della resa, l'inglese di monte e il dizionario, e un nome
proprio storpiato di una lettera passa tutte e tre. L'ha trovata il confronto
per **somiglianza del giapponese** fatto per il lotto dei file piccoli della
124a — cercavo il gemello di `etc.hsp:542`, ed e' saltato fuori che il gemello
era sbagliato.

⭐ E' la lezione della 122a («l'inglese di una riga puo' essere quello di un
altro oggetto») girata dalla parte dei nomi: la riga sorella non serve solo a
copiare una resa, serve anche a **controllarla**.
"""
import io
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
PERCORSO = os.path.join(RADICE, 'dizionario', 'screen.hsp.jsonl')

RIGA = 1450
SBAGLIATO = 'Larneire'
GIUSTO = 'Larnneire'


def main():
    voci = [json.loads(l) for l in io.open(PERCORSO, encoding='utf-8') if l.strip()]
    toccate = 0
    for v in voci:
        if v.get('riga') == RIGA and SBAGLIATO in (v.get('it') or ''):
            assert GIUSTO not in v['it'], 'gia\' corretta'
            v['it'] = v['it'].replace(SBAGLIATO, GIUSTO)
            print('  :%d  ->  %s' % (RIGA, v['it']))
            toccate += 1
    if toccate == 0:
        print('  niente da correggere: la resa e\' gia\' «%s»' % GIUSTO)
        return 0
    with io.open(PERCORSO, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('  %d resa corretta in %s' % (toccate, PERCORSO))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
