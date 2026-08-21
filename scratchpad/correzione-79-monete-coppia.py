# -*- coding: utf-8 -*-
"""79a — correzione di `chat.hsp:21867`: il soggetto sbagliato.

`chatval` 80 e' «<Dare 100.000 oro>» dentro l'evochat. Se l'evochat e' in
coppia, il codice divide la somma fra i due compagni e stampa:

    txt lang(name(tc) + "はパートナーに金貨を分けてあげた。",
             name(cc) + " shared coins with partner.")

⚠️ **In `*chat_default` `name(cc)` e' il GIOCATORE** (`cc = CHARA_PLAYER`; lo
conferma `:22124`, dove `name(cc)` decapita il prigioniero). Ma a dividere le
monete col proprio partner e' il **compagno**: lo dice il giapponese, e lo dice
il codice — le due righe subito sotto sono `cdata(CDATA_GOLD, tc) += 50000` e
`cdata(CDATA_GOLD, ttc) += 50000`. La resa vecchia seguiva l'inglese e diceva
«Tu hai diviso le monete con il compagno», cioe' nominava il personaggio
sbagliato e faceva di `ttc` «il compagno **del giocatore**».

E' la 77a, caso 1 («la riga giusta dell'evento sbagliato»): si segue il codice.
`verifica` lo permette perche' `name(tc)` compare nel ramo **giapponese**, e la
guardia sulle chiamate sottrae l'unione dei due rami, non il solo inglese.

Trovata leggendo il codice per il lotto degli evochat, non da una rete: nessuna
delle quindici guarda **quale** personaggio nomina una resa.
"""
import io
import json
import sys

DIZIONARIO = 'dizionario/chat.hsp.jsonl'
RIGA = 21867
VECCHIA = 'name(cc) + " ha diviso le monete con il compagno."'
NUOVA = 'name(tc) + " divide le monete con il compagno."'


def main() -> int:
    righe = [json.loads(l) for l in io.open(DIZIONARIO, encoding='utf-8') if l.strip()]
    tocche = [v for v in righe if v['riga'] == RIGA and v.get('it') == VECCHIA]
    if len(tocche) != 1:
        print('atteso 1 sito con la resa vecchia, trovati %d' % len(tocche))
        return 1
    tocche[0]['it'] = NUOVA
    with io.open(DIZIONARIO, 'w', encoding='utf-8', newline='\n') as f:
        for v in righe:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('chat.hsp:%d corretta' % RIGA)
    print('  da: %s' % VECCHIA)
    print('  a : %s' % NUOVA)
    return 0


if __name__ == '__main__':
    sys.exit(main())
