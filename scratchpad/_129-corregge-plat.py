# -*- coding: utf-8 -*-
"""⚠️ Correzione di quel che ho scritto io mezz'ora fa su ` Plat`.

Avevo riclassificato il rinvio come `attende_toppa` — «il ramo `else` del
diario e' inglese nudo, si aspetta la toppa che lo rende» — ricopiando la
premessa dal `motivo` vecchio invece di misurarla. Il referto ha risposto
**MATURATA** al primo giro: quella toppa **c'e' gia'**. Il ramo `else` di
`command.hsp:3040`-`:3069` nella build e' italiano da cima a fondo («Il tuo
cammino finora:», «Platino raccolto:», «Vittorie all'Arena delle Bestie:»), e
la stessa toppa ha riscritto pure la `lang()`: a schermo esce « pz.», non
« Plat».

⭐ E' la lezione della 128a presa in flagrante nel giro di un'ora: la premessa
di un rinvio ereditato va **rimisurata**, non riletta. Il vecchio motivo diceva
due cose, e tutt'e due erano scadute — «la `lang()` non viene valutata mai»
(falso: :3067 la valuta) e «il ramo else e' inglese nudo» (falso: e' tradotto).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strumenti import percorsi  # noqa: E402

CORREZIONE = (
    ' ⚠️⚠️⚠️ CORRETTO NELLA 129a: PER QUESTA FIRMA IL MOTIVO QUI SOPRA ERA '
    'FALSO DUE VOLTE. La firma non vive solo a :2982 dentro il ramo `if ( jp )`: '
    'vive **anche a :3067**, nel ramo `else`, dove la `lang()` viene valutata '
    'eccome. E il ramo `else` non e\' piu\' inglese nudo: la toppa che lo rende '
    'e\' stata scritta, tutto il blocco :3040-:3069 nella build e\' italiano e '
    'la stessa toppa ha cambiato la `lang()` in « pz.». Il rinvio resta — la '
    'resa non passa dal dizionario ma dalla toppa — e la condizione adesso e\' '
    '«la toppa c\'e\'», che il referto '
    '`scratchpad/_129-condizioni-dei-rinvii.py` misura sulla build. ⭐ Il '
    'vecchio motivo prometteva che «queste sette non serviranno comunque, '
    'perche\' il testo giusto sara\' quello»: e\' andata cosi\'.')


def main() -> int:
    percorso = percorsi.PROGETTO / 'rinviate.jsonl'
    righe = [r for r in percorso.read_text(encoding='utf-8').splitlines() if r.strip()]
    voce = json.loads(righe[27])
    if voce['en'] != ' Plat':
        raise SystemExit('la voce 28 non e\' " Plat" ma %r' % voce['en'])

    # via la riclassificazione sbagliata di poco fa, e via la coda di motivo che
    # aveva aggiunto: si riscrive quella giusta
    coda = voce['motivo'].find(' ⚠️⚠️⚠️ CORRETTO NELLA 129a')
    if coda != -1:
        voce['motivo'] = voce['motivo'][:coda]
    voce['motivo'] += CORREZIONE
    voce['rinviata_a'] = 'nessuna fase: risolta dalla toppa del ramo `else` (command.hsp:3067)'
    voce['condizione'] = {'tipo': 'risolta_da_toppa', 'siti': ['command.hsp:3067']}
    righe[27] = json.dumps(voce, ensure_ascii=False)
    percorso.write_text('\n'.join(righe) + '\n', encoding='utf-8')
    print('corretta la voce 28 (` Plat`): attende_toppa -> risolta_da_toppa')
    return 0


if __name__ == '__main__':
    sys.exit(main())
