# -*- coding: utf-8 -*-
"""115a - La prova al contrario del preflight: le frasi che DEVONO accenderlo.

Un cancello che dice zero su un lotto gia' corretto non ha dimostrato niente.
Qui ci sono i tre testi veri per cui `reimporta` ha respinto i lotti della 115a,
piu' i casi che devono restare spenti. Se una riga cambia colonna, la rete e'
cambiata.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-113/_prova_preflight.py
"""
import io
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))

DEVONO_ACCENDERSI = [
    ("l'accento in mezzo (il lotto 035)", "la protezione degli otto dèi che reggono"),
    ('i numeri cerchiati (il lotto 035)', '(effetto non attivo) ① All\'inizio del turno'),
    ('le virgolette a caporale (il lotto 035)', 'che porta il nome di «intuito»'),
    ('la lineetta lunga (il lotto 037)', 'parecchi pescatori — anzi, turisti'),
    ('la tilde larga', 'una coda con la tilde ～ larga'),
]

DEVONO_RESTARE_SPENTI = [
    ("l'accento in fondo, con la punteggiatura", 'una catena bella così!\\"'),
    ("l'accento in fondo, dentro le virgolette", '\\"perché no?\\"'),
    ('la parola con l\'apostrofo', "un'esplosione di qualità"),
    ('la È maiuscola in testa', 'È fatto proprio a pinna d\'arte'),
]


def carica_regole():
    # ⚠️ le regole si LEGGONO dal preflight, non si ricopiano: due copie
    #    divergono, e la prova finirebbe per provare se stessa.
    spazio = {'__file__': os.path.join(QUI, '_preflight034.py')}
    testo = io.open(os.path.join(QUI, '_preflight034.py'), encoding='utf-8').read()
    preambolo = testo.split('\ndef ')[0]
    exec(preambolo, spazio)
    return spazio['PROIBITI'], spazio['ACCENTATE']


def accende(testo, proibiti, accentate):
    motivi = []
    for c in proibiti:
        if c in testo:
            motivi.append('carattere %r' % c)
    for parola in re.findall(r"[^\W\d_]+(?:'[^\W\d_]+)*", testo, re.UNICODE):
        if any(v in parola[:-1] for v in accentate):
            motivi.append('accento dentro %r' % parola)
    return motivi


def main():
    proibiti, accentate = carica_regole()
    guasti = 0

    print('=== DEVONO ACCENDERSI')
    for nome, testo in DEVONO_ACCENDERSI:
        motivi = accende(testo, proibiti, accentate)
        stato = 'ok' if motivi else '⚠️ NON SI ACCENDE'
        if not motivi:
            guasti += 1
        print('  %-42s %s   %s' % (nome, stato, '; '.join(motivi)))

    print()
    print('=== DEVONO RESTARE SPENTI')
    for nome, testo in DEVONO_RESTARE_SPENTI:
        motivi = accende(testo, proibiti, accentate)
        stato = 'ok' if not motivi else '⚠️ FALSO POSITIVO'
        if motivi:
            guasti += 1
        print('  %-42s %s   %s' % (nome, stato, '; '.join(motivi)))

    print()
    print('righe sbagliate: %d su %d'
          % (guasti, len(DEVONO_ACCENDERSI) + len(DEVONO_RESTARE_SPENTI)))
    return 1 if guasti else 0


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
