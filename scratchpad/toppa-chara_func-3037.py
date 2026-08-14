# -*- coding: utf-8 -*-
"""La toppa di `chara_func.hsp:3037` e il rinvio che la accompagna.

⚠️ **La riga sopra, ricopiata male.** `:3034` e `:3037` sono la coppia
«si bagna» / «diventa visibile» applicata a **chi ti cavalca**, ed e' la terza
copia dello stesso blocco (chi subisce a `:3012`-`:3015`, il compagno di
tag-team a `:3023`-`:3026`). Nel ramo inglese di `:3037` upstream ha copiato la
coppia del tag-team e ha cambiato **due** riferimenti su tre:
`is(gdata(GDATA_RIDER))` e `his(gdata(GDATA_RIDER))` sono giusti, ma il
`name()` e' rimasto **`name(ttc@con)`**. Il giapponese dice
`name(gdata(GDATA_RIDER))`, e il codice conferma: la condizione intorno
(`cbit(CHARA_BIT_INVISIBLE, gdata(GDATA_RIDER))`) gira tutta sul cavaliere.

💡 **E la rete 11 non lascia scampo, come per `proc.hsp:24107` della stessa
sessione.** `funzioni_di_contenuto` conta `gdata` come contenuto, quindi
l'inglese dichiara `['name']` e la resa giusta dichiarerebbe `['name', 'gdata']`:
`verifica.py:367` la rifiuta. Non e' una resa che il dizionario possa scrivere.
✅ La strada e' la stessa: rinvio piu' toppa che riporta il ramo inglese alla
forma del giapponese.

⚠️ Le toppe **non passano da `degrada()`**: la sostituzione non porta accenti.
E si compone e si valida tutto in memoria prima di aprire un file in scrittura.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.getcwd())

from strumenti import percorsi  # noqa: E402

CERCA = ('\t\t\t\ttxt lang(name(gdata(GDATA_RIDER)) + "の姿があらわになった。", '
         'name(ttc@con) + " " + is(gdata(GDATA_RIDER)) + " revealed " '
         '+ his(gdata(GDATA_RIDER)) + " shape.")')
SOSTITUISCI = ('\t\t\t\ttxt lang(name(gdata(GDATA_RIDER)) + "の姿があらわになった。", '
               'name(gdata(GDATA_RIDER)) + " diventa visibile.")')

MOTIVO = (
    "chara_func.hsp:3037. **Non e' una resa mancante: e' una riga che il dizionario "
    "non puo' aggiustare**, ed e' la terza della famiglia dopo proc.hsp:11481 (36a) e "
    "proc.hsp:24107 (39a). La coppia 「濡れた」/「姿があらわになった」 compare **tre "
    "volte** nello stesso blocco — chi subisce (:3012/:3015), il compagno di tag-team "
    "(:3023/:3026) e chi ti cavalca (:3034/:3037) — e nel ramo inglese dell'ultima "
    "upstream ha ricopiato quella del tag-team cambiando **due** riferimenti su tre: "
    "`is(gdata(GDATA_RIDER))` e `his(gdata(GDATA_RIDER))` sono giusti, il `name()` e' "
    "rimasto `name(ttc@con)`. \u26a0\ufe0f Il giapponese dice `name(gdata(GDATA_RIDER))` e il "
    "codice conferma: `cbit(CHARA_BIT_INVISIBLE, gdata(GDATA_RIDER))` due righe sopra. "
    "💡 La rete 11 non lascia scampo perche' `funzioni_di_contenuto` conta `gdata` "
    "come contenuto: l'inglese dichiara ['name'], la resa giusta dichiarerebbe "
    "['name', 'gdata'], e `verifica.py:367` pretende che coincidano. La strada e' la "
    "toppa, che riporta il ramo inglese alla forma del giapponese. Fatta nella 39a "
    "insieme al rinvio."
)


def riscrivi(percorso, righe_nuove) -> int:
    """Compone, valida e solo allora scrive: un errore non deve troncare il file."""
    righe = [r for r in io.open(percorso, encoding='utf-8').read().splitlines() if r.strip()]
    righe.extend(righe_nuove)
    dati = ('\n'.join(righe) + '\n').encode('utf-8')
    with io.open(percorso, 'wb') as f:
        f.write(dati)
    return len(righe)


sorgente = io.open(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chara_func.hsp',
                   encoding='cp932').read()
if sorgente.count(CERCA) != 1:
    sys.exit(f'la riga cercata compare {sorgente.count(CERCA)} volte nel sorgente, non una')
SOSTITUISCI.encode('cp932')

toppe = percorsi.PROGETTO / 'toppe.jsonl'
if any(json.loads(r).get('cerca') == CERCA
       for r in io.open(toppe, encoding='utf-8').read().splitlines() if r.strip()):
    sys.exit('toppa gia\' presente')
print('toppe.jsonl:', riscrivi(toppe, [json.dumps(
    {'file': 'chara_func.hsp', 'cerca': CERCA, 'sostituisci': SOSTITUISCI, 'motivo': MOTIVO},
    ensure_ascii=False)]), 'toppe')

voce = None
for l in io.open('lavoro/_chara_func.jsonl', encoding='utf-8'):
    if l.strip() and json.loads(l)['riga'] == 3037:
        voce = json.loads(l)
if voce is None:
    sys.exit('voce 3037 non trovata nell\'estrazione')

rinviate = percorsi.PROGETTO / 'rinviate.jsonl'
if any(json.loads(r).get('firma') == voce['firma']
       for r in io.open(rinviate, encoding='utf-8').read().splitlines() if r.strip()):
    sys.exit('rinvio gia\' presente')
print('rinviate.jsonl:', riscrivi(rinviate, [json.dumps(
    {'firma': voce['firma'], 'file': 'chara_func.hsp', 'en': voce['en_grezzo'],
     'rinviata_a': 'nessuna fase: risolta da toppa (chara_func.hsp:3037, 39a)',
     'motivo': MOTIVO}, ensure_ascii=False)]), 'rinvii')
