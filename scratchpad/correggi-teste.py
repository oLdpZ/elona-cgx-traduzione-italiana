# -*- coding: utf-8 -*-
"""Le tre teste della scena vanno SENZA punteggiatura finale.

⚠️ Misurato sul giapponese: 「よかった」+_yo(3) non porta mai il punto — la
punteggiatura la mette la **coda** (`！さあ…」` a :3383 e :3629, oppure il solo
「」 a :3376/:3402/:3537/:3621). La prima stesura aveva copiato l'inglese, che
invece il punto ce l'ha nella testa («You are awesome!»), e il risultato sarebbe
stato «"Che bello...! Ecco, prendi questi spiccioli."»
"""
import io, json

from strumenti.accenti import degrada

TESTE = ['Che bello', 'I-incredibile', 'N-non ne posso piu\'',
         'C-che impeto', 'H-ho perso su tutta la linea']
NUOVA = 'txt ' + ', '.join(f'"\\"{b}"' for b in TESTE)

righe = [json.loads(l) for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]
cambiate = 0
for t in righe:
    if t['file'] != 'proc.hsp':
        continue
    blocco = t['sostituisci'] if isinstance(t['sostituisci'], list) else [t['sostituisci']]
    if 'Che bello' not in blocco[-1]:
        continue
    originale = blocco[-1]
    indent = originale[:len(originale) - len(originale.lstrip())]
    nuova = indent + degrada(NUOVA)
    if nuova == originale:
        continue
    blocco[-1] = nuova
    t['sostituisci'] = blocco if len(blocco) > 1 else blocco[0]
    t['motivo'] += (' ⚠️ La testa va senza punteggiatura finale, come il ramo '
                    'giapponese: il punto lo porta la coda (:3383, :3629) o il '
                    'solo segno di chiusura (:3376, :3402, :3537, :3621).')
    cambiate += 1

if cambiate != 3:
    raise SystemExit(f'attese 3 teste, cambiate {cambiate}')

with io.open('toppe.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for t in righe:
        f.write(json.dumps(t, ensure_ascii=False) + '\n')
print(f'{cambiate} teste corrette in toppe.jsonl')
