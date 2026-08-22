# -*- coding: utf-8 -*-
"""Il lotto di una zona di `chat.hsp`: le firme da fare, una voce per firma.

    python scratchpad/_88-lotto.py <uscita.jsonl> da a [da a ...]

Fino alla 87a ogni sessione se lo scriveva a mano dentro il modulo del lotto
(`lotto-80b-chat-unici.py` e i suoi fratelli tengono le rese e il filtro nello
stesso file). Dalla 84a in poi le rese stanno in un modulo separato e ci si
applicano con `_85-applica-rese.py`: quel che restava a mano era solo questo
taglio, e non c'e' ragione di riscriverlo ogni volta.

Toglie **le gia' rese** (`dizionario/chat.hsp.jsonl` con `it` pieno) e **le
rinviate** (`rinviate.jsonl`, che sono per firma e che nessuna mappa dei
parlanti conosce: i quattro morti di AJETALIO risultano ancora «da fare»).

⚠️ La voce scelta per una firma e' quella della PRIMA occorrenza dentro la
zona, che e' l'ancora su cui `_85-applica-rese.py` chiede le righe.
"""
import collections
import io
import json
import sys

EST = 'scratchpad/_84-chat-tutte.jsonl'
DIZ = 'dizionario/chat.hsp.jsonl'


def main() -> int:
    uscita = sys.argv[1]
    n = sys.argv[2:]
    if not n or len(n) % 2:
        print('serve almeno una coppia "da a"')
        return 1
    zone = [(int(n[i]), int(n[i + 1])) for i in range(0, len(n), 2)]
    dentro = lambda r: any(a <= r <= b for a, b in zone)

    rese = set()
    for l in io.open(DIZ, encoding='utf-8'):
        if l.strip():
            v = json.loads(l)
            if v.get('it', '').strip():
                rese.add(v['firma'])
    rinviate = {json.loads(l)['firma']
                for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()}

    voci = [json.loads(l) for l in io.open(EST, encoding='utf-8') if l.strip()]
    occorrenze = collections.defaultdict(list)
    for v in voci:
        occorrenze[v['firma']].append(v['riga'])

    scelte, viste = [], set()
    for v in sorted(voci, key=lambda v: (v['riga'], v['occorrenza'])):
        f = v['firma']
        if not dentro(v['riga']) or f in viste or f in rese or f in rinviate:
            continue
        viste.add(f)
        v['it'] = ''
        scelte.append(v)

    fuori = [v for v in scelte
             if any(not dentro(r) for r in occorrenze[v['firma']])]

    with io.open(uscita, 'w', encoding='utf-8', newline='\n') as fh:
        for v in scelte:
            fh.write(json.dumps(v, ensure_ascii=False) + '\n')

    print('%s: %d firme da fare' % (uscita, len(scelte)))
    print('   con occorrenze FUORI dalla zona: %d' % len(fuori))
    for v in fuori:
        print('      %d  %s' % (v['riga'], sorted(set(occorrenze[v['firma']]))))
    return 0


if __name__ == '__main__':
    sys.exit(main())
