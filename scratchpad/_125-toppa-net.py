# -*- coding: utf-8 -*-
"""125a - Le righe inglesi nude di `net.hsp` che il giocatore legge.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_125-toppa-net.py

`nudi_en.py` ne trova **tre**; se ne toppano **due**, e la terza non si tocca
per un motivo scritto qui sotto.

⭐ **:108** — `txt "[Chat Skipped]"`. E' quel che il gioco scrive quando premi
Esc mentre sta leggendo la chat dal server (`net_read`, il ciclo che aspetta
fino a diecimila giri). Va nel registro dei messaggi come una riga qualunque.

⭐ **:597** — `listn(0, cnt) = "Could not connect to the server."`, ripetuta su
tutte e sei le caselle prima di `net_read 5`. Se il server non risponde, quelle
caselle restano com'erano e `:601` stampa la prima: e' il messaggio d'errore
**vero e proprio** della funzione, e oggi il CGI di nifty.com non risponde
quasi mai. E' la riga di questo file che l'utente italiano vedrebbe piu' spesso.

⚠️⚠️ **:263 NON SI TOCCA, ED E' UNA COSA MISURATA E NON DECISA.**
`listn(0, listmax) = "" + locvar_net_dllist_s, "net"` assegna due caselle:
la prima e' il testo che arriva dal server, la seconda — `listn(1, listmax)` —
finisce nella **colonna di destra** dell'urna (`:686`, `mes s(1)`), quella la
cui intestazione e' resa «Voti». Che cosa ci faccia li' la parola «net» non si
capisce dal sorgente: potrebbe essere un segnaposto di monte, potrebbe essere
una sigla che il server rimpiazza. **Non si decide senza vederlo a schermo**, e
a schermo ci si arriva solo con un server che risponde. Resta nell'elenco di
`nudi_en.py` apposta: e' li' che qualcuno la ritrovera'.

⚠️ La toppa e' in **ASCII, commenti compresi** (123a). «Impossibile collegarsi
al server.» non lo e' — non ha accenti, quindi lo e'.
"""
import io
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
TOPPE = os.path.join(RADICE, 'toppe.jsonl')

VOCI = [
    ('\t\t\ttxt "[Chat Skipped]"',
     '\t\t\ttxt "[Chat saltata]"',
     "net.hsp:108. LETTERALE INGLESE NUDO: non passa da nessuna lang(), quindi "
     "non ha firma ne' voce di dizionario e nessun lotto puo' raggiungerlo "
     "(quinto punto cieco, nudi_en.py, 49a). E' quel che il gioco scrive nel "
     "registro quando premi Esc mentre net_read sta aspettando il server."),
    ('\t\tlistn(0, cnt) = "Could not connect to the server."',
     '\t\tlistn(0, cnt) = "Impossibile collegarsi al server."',
     "net.hsp:597. LETTERALE INGLESE NUDO (quinto punto cieco, nudi_en.py, "
     "49a). Riempie tutte e sei le caselle prima di `net_read 5`: se il server "
     "non risponde restano com'erano e :601 stampa la prima, quindi e' il "
     "messaggio d'errore vero della funzione. Col CGI di nifty.com fermo e' la "
     "riga di questo file che si legge piu' spesso."),
]


def main():
    toppe = []
    for cerca, sostituisci, motivo in VOCI:
        assert all(ord(c) < 128 for c in cerca + sostituisci), cerca
        toppe.append({
            'file': 'net.hsp',
            'motivo': motivo,
            'cerca': [cerca],
            'sostituisci': [sostituisci],
        })
    with io.open(TOPPE, 'a', encoding='utf-8', newline='\n') as f:
        for t in toppe:
            f.write(json.dumps(t, ensure_ascii=False) + '\n')
    print('%d toppe aggiunte a %s' % (len(toppe), TOPPE))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
