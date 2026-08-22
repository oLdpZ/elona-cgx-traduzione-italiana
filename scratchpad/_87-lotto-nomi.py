# -*- coding: utf-8 -*-
"""Due rese vecchie che il lotto di AJETALIO smentisce: si rifanno.

1. **`economy.hsp:357`** — la statistica 発言力 aveva **due nomi sullo
   schermo**: «autorita'» in otto siti (`chat.hsp:7032`, `:19563`, `:23940`,
   `:24008`, `:24011`, `:7026`, `action.hsp:8506`, `chat.hsp:22513`) e
   «Influenza» in questo, uno solo. Il tutorial di Ajetalio (`chat.hsp:14047`,
   la voce di menu `:13994`) e' il posto dove il giocatore impara la parola:
   da li' in poi il pannello dell'economia deve dire la stessa.
   ⚠️ La colonna e' larga **20 caratteri** contati sulla forma DEGRADATA
   (`Complaint           `, `Approval rate       `): «Autorita'» ne fa nove,
   quindi undici spazi. Nel dizionario l'accento e' vero, e sono dieci.

2. **`text.hsp:18`** — «Puoi annullarlo dal menu <examine>»: il nome del menu
   e' rimasto inglese dentro una frase italiana, e quel menu nell'interfaccia
   si chiama **<Esamina>** (`text.hsp:135`, `invtitle`; lo stesso in
   `help.hsp:22`). E' il difetto che il tutorial rende visibile: una riga che
   manda il giocatore a cercare una voce che non esiste.

    python scratchpad/_87-lotto-nomi.py [uscita.jsonl]
"""
import io
import json
import sys

NUOVE = {
    ('economy.hsp', 357):
        '"Autorità           " + mdata(MDATA_CITY_AUTHORITY) + " "',
    ('text.hsp', 18):
        'È segnato come non scartabile. Puoi annullarlo dal menu <Esamina>.',
}

VECCHIE = {
    ('economy.hsp', 357): 'Influenza',
    ('text.hsp', 18): '<examine>',
}


def main() -> int:
    uscita = sys.argv[1] if len(sys.argv) > 1 else 'lavoro/_87-nomi.jsonl'
    scelte = []
    for nome in sorted({f for f, _ in NUOVE}):
        for riga in io.open('dizionario/%s.jsonl' % nome, encoding='utf-8'):
            if not riga.strip():
                continue
            v = json.loads(riga)
            chiave = (nome, v['riga'])
            if chiave not in NUOVE:
                continue
            if VECCHIE[chiave] not in (v.get('it') or ''):
                print('%s:%d non dice piu\' %r: %r'
                      % (nome, v['riga'], VECCHIE[chiave], v.get('it')))
                return 1
            v['it'] = NUOVE[chiave]
            scelte.append(v)

    if len(scelte) != len(NUOVE):
        print('trovate %d voci su %d' % (len(scelte), len(NUOVE)))
        return 1

    with io.open(uscita, 'w', encoding='utf-8', newline='\n') as fh:
        for v in scelte:
            fh.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%d voci in %s' % (len(scelte), uscita))
    return 0


raise SystemExit(main())
