# -*- coding: utf-8 -*-
"""`chat.hsp:15440` chiamava «fessura» la casella che il gioco chiama «fenditura».

裂け目 nella Valle di Raskilis non e' una parola qualunque: e' **un oggetto
della mappa**, la casella che in `ras0` sta al posto della scala in giu'.
`action.hsp:2853` lo dice per esteso — nella sola `AREA_WEST_RASKILIS` la
casella non annuncia una scala ma 「空間の裂け目」 — e quella riga e' resa da
tempo **«C'e' una fenditura nello spazio.»** (`action.hsp:2854` e `:2862`). E'
testo che il giocatore legge **camminandoci sopra**, ogni volta che ci passa.

La resa di Jenna della 91a (`:15440`) chiamava lo stesso oggetto «fessura», due
volte nella stessa riga. Nessuna rete poteva vederlo: sono due file diversi, due
firme diverse, e la rete 4 guarda il **giapponese uguale**, che qui non c'e' —
`action.hsp` dice 空間の裂け目, Jenna dice 小さな裂け目.

Trovato nella 95a traducendo `:15407` di CRAY, che parla della **stessa
casella** («la fenditura a est»): scrivendo la resa nuova e' saltato fuori che
la vicina ne aveva gia' un'altra.

Non e' un difetto di senso — «fessura» dice la cosa giusta — ma sulla stessa
mappa un oggetto solo prende due nomi, e a distinguerli il giocatore non ha
nessun appiglio. Vince il nome che sta nel messaggio della casella.

⚠️ Si compone tutto in memoria e si scrive solo alla fine (regola della 39a).
"""
import io
import json

PERCORSO = 'dizionario/chat.hsp.jsonl'
FIRMA = 'f113f9338bfe88e78fa4ef1440884f9c794e5f20'
PRIMA = ('Appena siamo arrivati qui lo spazio si è richiuso, e ne è rimasta '
         'solo una fessura piccolissima. Se guardi dentro la fessura vedi il '
         'fondo della valle: ormai è pieno di bestie nere.')
DOPO = ('Appena siamo arrivati qui lo spazio si è richiuso, e ne è rimasta '
        'solo una fenditura piccolissima. Se guardi dentro la fenditura vedi '
        'il fondo della valle: ormai è pieno di bestie nere.')

righe = io.open(PERCORSO, encoding='utf-8').read().split('\n')
fatte = 0
nuove = []
for riga in righe:
    if not riga.strip():
        nuove.append(riga)
        continue
    d = json.loads(riga)
    if d.get('firma') == FIRMA:
        if d.get('it') != PRIMA:
            raise SystemExit('la voce %s dice %r, non quella attesa' % (FIRMA, d.get('it')))
        d['it'] = DOPO
        fatte += 1
        nuove.append(json.dumps(d, ensure_ascii=False))
        continue
    nuove.append(riga)

if fatte != 1:
    raise SystemExit('la firma %s aggancia %d voci, non una' % (FIRMA, fatte))

io.open(PERCORSO, 'w', encoding='utf-8', newline='\n').write('\n'.join(nuove))
print('%s:15440  fessura -> fenditura (2 occorrenze nella riga)' % PERCORSO)
