# -*- coding: utf-8 -*-
"""La spiegazione del potenziale nominava due etichette che nel gioco italiano
non esistono piu'.

`chat.hsp:14246` e' la lezione dell'istruttore sugli attributi, e la resa dice
«Supreme e' il massimo, Hopeless e' il minimo»: le due etichette erano state
lasciate in inglese perche' a schermo la scala ERA inglese. Poi sette toppe
hanno reso la scala nella scheda del personaggio (`command.hsp:10677`-`:10700`
-> Supremo / Enorme / Ottimo / Notevole / Buono / Scarso / Nullo), e da quel
giorno la lezione manda il giocatore a cercare due parole che non ci sono.

⚠️ Nessuna rete se ne e' accorta, e non poteva: la resa e' una voce di
dizionario e le etichette sono toppe, cioe' due mondi che nessun referto mette
a confronto (e' la scoperta della 126a, «le toppe erano l'unico italiano che
nessuna rete avesse mai letto», vista dall'altro lato).

⭐ E il giapponese dava gia' la risposta: 「Supreme（至高）」 e 「Hopeless（絶望的）」
sono glossate in giapponese proprio perche' l'etichetta a schermo e' inglese.
In italiano l'etichetta e' italiana, quindi la glossa non serve: si nomina
l'etichetta e basta.
"""
import io
import json

PERCORSO = 'dizionario/chat.hsp.jsonl'
RIGA = 14246

VECCHIA = ('Roba come Forza e Costituzione sono i tuoi attributi base. Il '
           'potenziale dice quanto è facile farli salire: Supreme è il '
           'massimo, Hopeless è il minimo.')
NUOVA = ('Roba come Forza e Costituzione sono i tuoi attributi base. Il '
         'potenziale dice quanto è facile farli salire: Supremo è il '
         'massimo, Nullo è il minimo.')

voci = [json.loads(r) for r in io.open(PERCORSO, encoding='utf-8') if r.strip()]

toccate = 0
for v in voci:
    if v.get('riga') != RIGA:
        continue
    if VECCHIA not in (v.get('it') or ''):
        raise SystemExit('la voce {} non ha piu\' la forma attesa: {}'
                         .format(RIGA, (v.get('it') or '')[:120]))
    v['it'] = v['it'].replace(VECCHIA, NUOVA)
    toccate += 1

if toccate != 1:
    raise SystemExit('attese 1 voce, toccate {}'.format(toccate))

# ⚠️ si compone e si valida PRIMA di aprire il file (regola della 39a)
dati = ''.join(json.dumps(v, ensure_ascii=False) + '\n' for v in voci).encode('utf-8')
with io.open(PERCORSO, 'wb') as f:
    f.write(dati)
print('{} voce corretta, {} voci riscritte in {}'.format(toccate, len(voci), PERCORSO))
