# -*- coding: utf-8 -*-
"""Toglie da rinviate.jsonl le due voci di `" guest"` e le rende.

Erano rinviate perche' la frase che le incornicia non stava nel sorgente ma in
`data/talk.txt` — «You have {ref} waiting for you.» — che allora era fuori
perimetro. Adesso quella riga e' resa (`MAID|1` del lotto talk-002), quindi la
coppia si puo' chiudere insieme, che era esattamente la condizione scritta nel
motivo del rinvio.

⭐ La resa NON traduce «guest»: lo **toglie**. `{ref}` diventa il numero nudo,
cioe' lo stesso che gia' rende il ramo giapponese, e il sostantivo passa nella
frase italiana con l'apposizione a due punti:

    Eccoti a casa, {player}! Ospiti in attesa: {ref}. Li ricevi subito?

💡 Cosi' il plurale sparisce come problema invece di essere risolto: «Ospiti in
attesa: 1.» regge come «Ospiti in attesa: 3.», mentre qualunque resa che porti
il sostantivo dentro {ref} sbaglia su uno dei due. E' la 64a — *esiste una
costruzione italiana che non chiede accordo?* — applicata al numero.

⚠️ `_s3` e `_s2` sono il plurale inglese, cioe' MORFOLOGIA: si tolgono, e
l'elenco delle funzioni di contenuto resta ['gdata'] da tutt'e due le parti.

⚠️ Le due voci non sono un doppione: `:6924` e' l'espansore di `data/talk.txt`
(`*convert_word`) e `:8178` quello di `guide/guide.txt` (`*convert_guide`).
La seconda si chiude con la stessa resa perche' `talkref` lo mette a 1 un solo
sito — `text.hsp:9413`, il ramo della cameriera — e perche' `guide/guide.txt`
in questa installazione **non esiste** (dentro `guide` ci sono solo `dummy.txt` e
un bmp).
"""
import io
import json
from pathlib import Path

from strumenti import estrai, percorsi

RESE = {
    '849d81b33d7a4f88b4651597c35a380c4aca4e77': '"" + gdata(GDATA_GUEST)',  # :6924 talk.txt
    'b8a2637089f07ca110b5dcd4a92fa97fc3760f33': '"" + gdata(GDATA_GUEST)',  # :8178 guide.txt
}

voci = estrai.estrai_da_file(percorsi.SORGENTE_HSP / 'text.hsp')
scelte = [v for v in voci if v['firma'] in RESE]
if len(scelte) != 2:
    raise SystemExit(f'attese 2 voci, trovate {len(scelte)}')

for v in scelte:
    v['it'] = RESE[v['firma']]
    print(f"  text.hsp:{v['riga']}  {v['en_grezzo']}\n            -> {v['it']}")

with io.open('lavoro/text-ospiti.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for v in scelte:
        f.write(json.dumps(v, ensure_ascii=False) + '\n')

righe = [json.loads(l) for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
restano = [r for r in righe if r['firma'] not in RESE]
with io.open('rinviate.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for r in restano:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f'{len(righe) - len(restano)} rinviate tolte, ne restano {len(restano)}')
