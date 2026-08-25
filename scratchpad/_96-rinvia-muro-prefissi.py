# -*- coding: utf-8 -*-
"""96a - Le quattro firme che restano del muro dei prefissi di `item_func.hsp`.

Sono l'ultimo pezzo delle 24 che stanno in `itemname()` **prima** del nome
dell'oggetto (`:1731`, `:1747`, `:1770`). In inglese quella posizione regge —
«mithril material kit», «34cm sandwich», «eternal force long sword» — in
italiano il complemento va **dopo** la testa del sintagma, e nessuna resa della
`lang()` puo' spostarlo: il pezzo che si potrebbe tradurre e' gia' incollato al
posto sbagliato.

⭐⭐⭐ MA LA STRADA E' GIA' TRACCIATA, E STA NELLO STESSO FILE. La 96a ha
scoperto — con `scratchpad/_96-morte-nella-build.py` — che il gemello di queste
quattro, `:1399`/`:1404`, **non e' bloccato affatto**: una toppa gia' scritta lo
trasforma in

    locvar_itemname_s6 += " di manifattura in " + mtname(0, …)

e `locvar_itemname_s6` si appende a `:1899`, cioe' **in coda al nome**. Il
mobile dice gia' «una sedia di manifattura in mithril».

Quindi queste quattro non aspettano una decisione: aspettano **quattro toppe
della stessa forma**, ognuna con la sua preposizione e il suo giro a schermo.
Non sono state fatte nella 96a per una ragione precisa: in quella sessione una
toppa di questo file si era gia' disinnescata in silenzio, e quattro toppe nuove
sul compositore dei nomi vogliono essere **viste in gioco** una per una, non
infilate a fine giornata.

⚠️ E una di loro (`:1386`) tocca `mtname()`, cioe' i materiali, che non sono
ancora tradotti: la preposizione giusta («di mithril» / «d'acciaio») dipende
dalla parola che arrivera'. `strumenti/articolo.py` ha gia' `preposizione_di()`
per questo, ma va scelta a valle del lessico dei materiali, non prima.
"""
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti import estrai

SORGENTE = Path('C:/Games/Elona/_traduzione/sorgente/2.05-custom-gx')
FILE = 'item_func.hsp'

COMUNE = (
    " ⭐ La strada e' gia' tracciata nello stesso file: `:1399` era lo stesso "
    "problema ed e' risolto da una toppa che scrive `locvar_itemname_s6 += "
    "\" di manifattura in \" + mtname(…)`, cioe' sposta il pezzo **in coda al "
    "nome** (`:1899`). Serve una toppa della stessa forma, con la sua "
    "preposizione, e un giro a schermo suo. Rinviata nella 96a."
)

RINVII = {
    1308: (
        "La taglia del pesce, in centimetri, davanti al nome del cibo "
        "(`item_func.hsp:1308`): `… + lang(\"cmの\", \"cm \")` e poi il nome. In "
        "inglese esce «34cm sandwich»; in italiano la misura va dopo — «sandwich "
        "da 34cm» — e questa `lang()` sta prima del nome, quindi non ci arriva."
        + COMUNE
    ),
    1386: (
        "Il materiale del kit di materiali (`item_func.hsp:1386`): "
        "`mtname(0, …) + lang(\"製の\", \" \")` davanti al nome. L'inglese se la "
        "cava con lo spazio — «mithril material kit» — l'italiano vuole «kit di "
        "materiali **di mithril**», cioe' il materiale dopo."
        " ⚠️ E qui c'e' un secondo strato: la preposizione giusta dipende dalla "
        "parola che `mtname()` restituisce a runtime («di mithril», ma "
        "«d'acciaio»), e i materiali non sono ancora tradotti. "
        "`strumenti/articolo.py` ha gia' `preposizione_di()`, ma la scelta va "
        "fatta a valle del lessico dei materiali, non prima."
        + COMUNE
    ),
    1390: (
        "Il «Wish Goddess » davanti al cioccolatino fatto a mano "
        "(`item_func.hsp:1390`, `PARAM3 == 6`), giapponese 願いの女神の. In "
        "italiano e' «un cioccolatino **della Dea dei Desideri**», cioe' un "
        "complemento che va dopo il nome, e questa `lang()` sta prima."
        + COMUNE
    ),
    1458: (
        "L'«eternal force» davanti al nome di un oggetto definitivo "
        "(`item_func.hsp:1458`, `ITEM_BIT_ULTIMATE`), giapponese "
        "エターナルフォース. E' un marchio di qualita' incollato in testa: "
        "l'italiano lo vuole dopo — «una spada lunga della forza eterna» — o "
        "fra parentesi in coda, come i quaranta stati che lo stesso compositore "
        "gia' emette li'."
        + COMUNE
    ),
}

righe_rin = [l for l in io.open('rinviate.jsonl', encoding='utf-8').read().splitlines()
             if l.strip()]
firme_rin = {json.loads(l)['firma'] for l in righe_rin}

siti = {v['riga']: v for v in estrai.estrai_da_file(SORGENTE / FILE)
        if v['riga'] in RINVII}
if len(siti) != len(RINVII):
    raise SystemExit(f'attese {len(RINVII)} firme, trovate {sorted(siti)}')

diz = {json.loads(l)['firma'] for l in io.open(f'dizionario/{FILE}.jsonl', encoding='utf-8')
       if l.strip()}
gia = [r for r, v in siti.items() if v['firma'] in diz]
if gia:
    raise SystemExit(f'queste sono gia\' nel dizionario: {gia}')

nuove = [json.dumps({
    'firma': v['firma'],
    'file': FILE,
    'en': v['en'],
    'rinviata_a': 'Fase 4: vuole la toppa che sposta la concatenazione',
    'motivo': RINVII[r],
}, ensure_ascii=False) for r, v in sorted(siti.items()) if v['firma'] not in firme_rin]

if not nuove:
    raise SystemExit('rinvii gia\' presenti')

with io.open('rinviate.jsonl', 'wb') as f:
    f.write(('\n'.join(righe_rin + nuove) + '\n').encode('utf-8'))
print('rinviate.jsonl: %d -> %d' % (len(righe_rin), len(righe_rin) + len(nuove)))
