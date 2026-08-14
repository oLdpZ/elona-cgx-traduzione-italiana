# -*- coding: utf-8 -*-
"""Lotto fase4-ai-003: le quattro grida della trasformazione (ai.hsp:4576).

4 rese, e **chiude `ai.hsp`**. Tutte e quattro sono copiate da
`action.hsp:11442`, che ha lo stesso `txt` con gli stessi quattro giapponesi.

⚠️⚠️ **Questo lotto non passa da `assembla-lotto.py`, ed e' la prima volta.**
A `:4576` due `lang()` diverse hanno lo **stesso inglese** — 「変身！」 e
「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")` — quindi la chiave
`(riga, en)` su cui e' costruito il modello di lotto **identifica due voci, non
una**, e la rete 0 ferma la zona prima di scrivere qualunque cosa. Non e' un
difetto della rete: e' il limite della chiave, e la rete esiste apposta per non
farlo passare in silenzio.

✅ Qui l'indice e' la **`firma`**, che e' l'unica chiave davvero univoca: e'
l'sha1 che `estrai.py` calcola e con cui `applica.py` ritrova il sito. Il
dizionario la collisione la regge gia' — `action.hsp:11442` porta
«Trasformazione!» e «Metamorfosi!» sulla stessa riga con lo stesso inglese.

⚠️ Le reti del modello che qui non girano, e perche' non servono:

- **rete 0** e' esattamente quella che stiamo aggirando, e a ragione veduta;
- **rete 4** (stesso giapponese, stessa resa) non ha niente da dire: i quattro
  giapponesi sono tutti diversi;
- **rete 11 e 12** valgono per le dinamiche, e queste sono quattro statiche;
- **rete 6 e 7** guardano il sorgente: `:4576` e' un `txt lang(...)` vivo, non
  commentato e non dentro un confronto — controllato a mano;
- **`verifica`** gira lo stesso, ed e' la guardia vera.

💡 **Se capitera' di nuovo** — e capitera', perche' `cnvtalk` ripete gli stessi
inglesi dappertutto — la strada giusta e' insegnare al modello la chiave
`firma` invece di `(riga, en)`. Finche' e' un caso solo, questo file basta.
"""
import io
import json

RESE = {
    # 「変身！」 — action.hsp:11442
    '78f628eabc7ac0aeb9bfba138276f54aaed45512': 'Trasformazione!',
    # 「フォームアップ！」 — action.hsp:11442
    '3b253378f1f7b08668f60b8a25277cc0161f17f1': 'Cambio forma!',
    # 「ドレスアップ！」 — action.hsp:11442
    'ba6b1b8c49ad23c255682d0f5a7166f139772951': "Cambio d'abito!",
    # 「トランスフォーム！」 — action.hsp:11442
    '17befb8f1ab42f34503abd80cdb187507063754e': 'Metamorfosi!',
}

USCITA = 'lavoro/fase4-ai-003.jsonl'
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\ai.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_ai.jsonl', encoding='utf-8') if l.strip()]
voci = [v for v in tutte if v['firma'] in RESE]

errori = []
if len(voci) != len(RESE):
    errori.append(f'{len(voci)} voci agganciate su {len(RESE)} rese')
for v in voci:
    if v['riga'] != 4576:
        errori.append(f"la firma {v['firma']} non sta a :4576 ma a :{v['riga']}")
    if v['tipo'] != 'statica':
        errori.append(f"la voce a :{v['riga']} e' {v['tipo']}, non statica")

# rete 6 e 7 a mano, sul SORGENTE: la riga dev'essere viva e non un confronto.
sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')
riga = sorgente[4576 - 1]
if riga.lstrip().startswith(';'):
    errori.append(':4576 e\' commentata nel sorgente')
if '==' in riga.split('lang(')[0] or '!=' in riga.split('lang(')[0]:
    errori.append(':4576 e\' un confronto, non un testo')

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato')

# ⚠️ comporre, codificare in memoria, e SOLO ALLORA aprire: la lezione della 39a,
# quando uno script ha troncato `toppe.jsonl` a zero byte aprendolo per primo.
fuori = []
for v in voci:
    v['it'] = RESE[v['firma']]
    fuori.append(json.dumps(v, ensure_ascii=False))
dati = ('\n'.join(fuori) + '\n').encode('utf-8')
with io.open(USCITA, 'wb') as f:
    f.write(dati)
print(f'{len(voci)} voci scritte in {USCITA}')
