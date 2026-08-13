# -*- coding: utf-8 -*-
"""La toppa su `action.hsp:15221`, l'unico buco di un file dato al 100%.

⚠️ `action.hsp` e' dichiarato **100%** nella ripresa, e ha una riga inglese:
`:15221` sta in un blocco `if ( en )` con letterali nudi, quindi il dizionario
non la raggiunge e nessun conteggio la vede. E' la **gemella esatta** di
`proc.hsp:26886` — jp e en identici riga per riga — che la 33ª ha gia' reso:
qui si **copia**, non si ridecide.
"""
import io
import json

from strumenti.accenti import degrada

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\action.hsp'
RIGA = 15221

NUOVA = ('txt cdatan(CDATAN_NAME, tc) + " " + cnvtalk("Non darmi ordini!"), '
         'cdatan(CDATAN_NAME, tc) + " " + cnvtalk("Stavo giusto per farlo, e '
         'adesso mi è passata la voglia.")')

MOTIVO = (
    "action.hsp:15221. Blocco `if ( en )` con letterali **nudi** fuori da `lang()`: "
    "estrai.py non li vede, quindi il dizionario non li raggiunge e la riga resta "
    "inglese benche' `action.hsp` sia dato al 100%. ⚠️ E' la gemella esatta di "
    "`proc.hsp:26886` — ramo giapponese e ramo inglese identici riga per riga — resa "
    "nella 33ª: la resa e' **copiata**, non ridecisa. Trovata da "
    "`scratchpad/blocchi_en.py`, che misura la struttura del sorgente pinnato e non "
    "il conteggio delle non tradotte."
)

righe = io.open(SORGENTE, encoding='cp932').read().split('\n')
originale = righe[RIGA - 1]
indent = originale[:len(originale) - len(originale.lstrip())]
nuova = indent + degrada(NUOVA)
if nuova == originale:
    raise SystemExit('la toppa non cambierebbe niente')

# il blocco piu' corto che finisce qui ed e' unico nel file
for altezza in range(1, 25):
    blocco = righe[RIGA - altezza:RIGA]
    quanti = sum(1 for i in range(len(righe) - len(blocco) + 1)
                 if righe[i:i + len(blocco)] == blocco)
    if quanti == 1:
        break
else:
    raise SystemExit('nessun blocco unico entro 24 righe')

sostituisci = blocco[:-1] + [nuova]
toppa = {
    'file': 'action.hsp',
    'cerca': blocco if len(blocco) > 1 else blocco[0],
    'sostituisci': sostituisci if len(sostituisci) > 1 else sostituisci[0],
    'motivo': MOTIVO,
}
with io.open('lavoro/toppe-action-en.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    f.write(json.dumps(toppa, ensure_ascii=False) + '\n')
print(f'blocco di {len(blocco)} riga/e -> lavoro/toppe-action-en.jsonl')
print('  -', originale.strip()[:150])
print('  +', nuova.strip()[:150])
