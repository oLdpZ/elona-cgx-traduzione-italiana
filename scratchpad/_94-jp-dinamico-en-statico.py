# -*- coding: utf-8 -*-
"""I siti dove il GIAPPONESE concatena e l'INGLESE no.

    python scratchpad/_94-jp-dinamico-en-statico.py [--tutte]

Trovato nella 94a su `chat.hsp:9705`:

    lang("(突然、" + name(tc) + "は自らの胸を抉りぬいた！)",
         "(Suddenly, Saimef reaches into his own chest and pulls out his heart!)")

Il giapponese mette il nome con `name(tc)`; l'inglese lo **inchioda** in un
letterale. ⚠️ La conseguenza non e' solo stilistica: `estrai` classifica la voce
guardando **l'inglese**, che e' il lato che si sostituisce, quindi la voce e'
`statica`, e `applica.riscrivi_statica` avvolge la resa in `"..."` e basta. Un
`" + name(tc) + "` scritto nel dizionario finirebbe **a schermo come testo**.

Cioe': in questi siti l'italiano **non puo'** essere dinamico, qualunque cosa
faccia il giapponese. Se il nome inchiodato dall'inglese e' sbagliato — un
mostro rinominato, un compagno, il giocatore — la resa lo eredita e nessuna
rete lo vede.

⚠️ Il contrario (`inglese dinamico / giapponese statico`) e' innocuo e non si
conta qui: li' la voce e' `dinamica` e la resa porta le sue variabili.
"""
import glob
import io
import json
import os
import sys


def nudo(s: str) -> bool:
    """Vero se `s` e' un letterale HSP nudo: virgolette in testa e in coda, e
    nessun `+` fuori dalle virgolette."""
    s = s.strip()
    if len(s) < 2 or not s.startswith('"') or not s.endswith('"'):
        return False
    dentro = False
    i = 0
    while i < len(s):
        c = s[i]
        if c == chr(92):
            i += 2
            continue
        if c == '"':
            dentro = not dentro
        elif not dentro and c == '+':
            return False
        i += 1
    return True


def main() -> int:
    tutte = '--tutte' in sys.argv
    totale = 0
    casi = []
    for f in sorted(glob.glob('dizionario/*.jsonl')):
        nome = os.path.basename(f)
        for l in io.open(f, encoding='utf-8'):
            if not l.strip():
                continue
            v = json.loads(l)
            jg, eg = v.get('jp_grezzo'), v.get('en_grezzo')
            if not jg or not eg:
                continue
            totale += 1
            if not nudo(jg) and nudo(eg):
                casi.append((nome, v['riga'], bool((v.get('it') or '').strip()),
                             jg, eg))

    print('voci con i due grezzi          : %d' % totale)
    print('giapponese dinamico, inglese no: %d' % len(casi))
    rese = sum(1 for c in casi if c[2])
    print('   di cui gia rese             : %d' % rese)
    per = {}
    for c in casi:
        per[c[0]] = per.get(c[0], 0) + 1
    print()
    for k in sorted(per, key=lambda k: -per[k]):
        print('   %-28s %d' % (k, per[k]))
    print()
    for c in (casi if tutte else casi[:20]):
        print('%s:%d  %s' % (c[0], c[1], 'RESA' if c[2] else 'da fare'))
        print('   JP %s' % c[3][:150])
        print('   EN %s' % c[4][:150])
    if not tutte and len(casi) > 20:
        print('\n(%d non elencate: --tutte)' % (len(casi) - 20))
    return 0


if __name__ == '__main__':
    sys.exit(main())
