# -*- coding: utf-8 -*-
"""106a - `イツパロトル` era reso in DUE modi, e uno dei due viene dall'inglese.

    Itzpalt      52 volte, in nove file — `god.hsp:84` e' il nome del dio,
                 `text.hsp:546` la risposta giusta del quiz, `db_card:8590` e
                 `db_creature:87235` il nome della carta e della creatura
    Itzparotl     2 volte, tutt'e due in `db_card.hsp` — `:8220` e `:8597`

⚠️ **La causa non e' una svista: e' l'inglese di monte.** L'inglese di quelle due
carte scrive `Itzparotl` (e solo li'), mentre dappertutto altrove scrive
`Itzpalt`. Chi ha reso quelle due prose ha preso il nome dalla riga che aveva
davanti invece che dal dizionario — la stessa forma dei quattro sbagli della 105a
e dei due nomi della 104a (`キッカス`, `エルン`).

⚠️ **Le tre grafie storpiate di `text.hsp` NON si toccano**: `:549` `Itzpatl`,
`:552` `Itzpait`, `:555` `Itspalt` sono le risposte **sbagliate** del quiz sul
nome del dio degli elementi (`:542`), e sbagliate devono restare.

💡 La rete che avrebbe visto questo non esiste ancora: e' il punto 14 della
ripresa, i **nomi propri dentro le prose**. La rete 3 guarda i giapponesi interi,
e qui gli interi sono due prose diverse che contengono lo stesso nome.
"""
import io
import json

FILE = 'dizionario/db_card.hsp.jsonl'
ATTESE = {8220, 8597}

voci = [json.loads(l) for l in io.open(FILE, encoding='utf-8') if l.strip()]
toccate = set()
for v in voci:
    it = v.get('it') or ''
    if 'Itzparotl' in it:
        v['it'] = it.replace('Itzparotl', 'Itzpalt')
        toccate.add(v['riga'])

if toccate != ATTESE:
    raise SystemExit(f'righe toccate {sorted(toccate)}, attese {sorted(ATTESE)}: '
                     'il dizionario non e\' nello stato previsto, non scrivo niente')

with io.open(FILE, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'corrette {len(toccate)} rese: {sorted(toccate)}')
