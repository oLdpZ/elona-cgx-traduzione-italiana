# -*- coding: utf-8 -*-
"""75a — toppa: `economy.hsp:357` diceva «Influenza», il glossario dice «autorita'».

`glossario.md:356` fissa 発言力 -> «autorita'» e **nomina `economy.hsp` per
nome**. Il dizionario lo rispettava in due siti su tre:

    action.hsp:8506   «Hai guadagnato 200 punti autorita'.»   ok
    chat.hsp:19563    «Amministrare (autorita' .../2000)»     ok
    economy.hsp:357   «Influenza           »                  ✗

Il giocatore vede il pannello della citta' e il menu del sindaco nella stessa
sessione, quindi la stessa statistica aveva due nomi. ⚠️ Nessuna rete lo vede:
`gemelle` confronta le firme, e qui il giapponese 発言力 sta dentro tre frasi
diverse; `verifica --dizionario` guarda che non ci sia da ritradurre, non che il
glossario sia rispettato.

⚠️⚠️ **E la colonna e' a larghezza fissa: il conto va fatto sul testo DELLA
BUILD.** `economy.hsp:331`-`:365` scrive etichetta e valore in un `mes` solo, con
l'etichetta riempita di spazi fino alla colonna 20. «Influenza» sono 9 caratteri
e voleva 11 spazi. «Autorita'» sono 9 **dopo la degradazione** (`applica`
sostituisce «a» accentata con «a'», che e' due caratteri) ma 8 nel dizionario:
gli spazi restano **11**, non 12. Scriverne 12 — cioe' contare sul testo che si
ha davanti invece che su quello che esce — spostava la colonna di uno.

E' il primo sito del progetto in cui un'etichetta a larghezza fissa porta un
accento: prima di oggi erano zero.

    python scratchpad/toppa-75-autorita.py
"""
import io
import json
import sys

from strumenti import accenti

FILE = 'dizionario/economy.hsp.jsonl'
RIGA = 357
VECCHIA = '"Influenza           " + mdata(MDATA_CITY_AUTHORITY) + " "'
NUOVA = '"Autorità           " + mdata(MDATA_CITY_AUTHORITY) + " "'
COLONNA = 20


def main() -> int:
    etichetta = NUOVA.split('"')[1]
    resa = accenti.degrada(etichetta)
    if len(resa) != COLONNA:
        print('la colonna non torna: %r e\' %d caratteri dopo la degradazione, ne servono %d'
              % (resa, len(resa), COLONNA))
        return 1
    print('colonna ok: %r -> %r, %d caratteri' % (etichetta, resa, len(resa)))

    righe = io.open(FILE, encoding='utf-8').read().split('\n')
    fatte = 0
    for i, l in enumerate(righe):
        if not l.strip():
            continue
        v = json.loads(l)
        if v['riga'] == RIGA and v.get('it') == VECCHIA:
            v['it'] = NUOVA
            righe[i] = json.dumps(v, ensure_ascii=False)
            fatte += 1
    if fatte != 1:
        print('attese 1 riga da correggere, trovate %d' % fatte)
        return 1
    io.open(FILE, 'w', encoding='utf-8', newline='\n').write('\n'.join(righe))
    print('%s:%d corretta' % (FILE, RIGA))
    return 0


if __name__ == '__main__':
    sys.exit(main())
