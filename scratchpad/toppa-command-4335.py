# -*- coding: utf-8 -*-
"""`command.hsp:4335`: la variante con lo spazio che la rete 4 non lascia scrivere.

⚠️⚠️ `*wish_fix` toglie il prefisso dal desiderio digitato dal giocatore:

    inputlog = del_str(inputlog, lang("アイテム", "item"))
    inputlog = del_str(inputlog, lang("スキル", "skill "))     <- :4335
    inputlog = del_str(inputlog, lang("スキル", "skill"))      <- :4336

Le due righe sono la **stessa** `lang()` giapponese con due inglesi diversi, e
l'ordine conta: la prima porta via anche lo **spazio**, la seconda prende il caso
senza. Il giapponese non ha bisogno della distinzione perche' il suo ramo gli
spazi li ha gia' tolti a `:4328`.

⚠️ **La rete 4 raggruppa per giapponese e pretende una resa sola**, e in generale
ha ragione — nel lotto 024 ha giustamente legato le due 「いらん」 di `:15188` e
`:15196`. Qui a distinguere le due voci non e' il senso, e' uno spazio, e una
resa sola lascerebbe **uno spazio in testa** a `inputlog`. ⚠️ E quello spazio
rompe la ricerca: `:4887` da' il punteggio sui **prefissi** di `inputlog`
(`strmid(inputlog, 0, cnt)`), quindi con uno spazio davanti i prefissi diventano
« », « s», « sp» e l'oggetto giusto non vince piu'.

✅ Rinvio + toppa, la forma della 46a: `:4336` prende la resa «abilita» dal
dizionario, `:4335` esce dal dizionario e la scrive questa toppa.
⚠️ **Le due righe sono diverse**, quindi la regola «una toppa e una resa non
stanno sulla stessa riga» e' rispettata: `:4335` non ha piu' nessuna voce.

⚠️⚠️ **«abilita» e' senza accento di proposito.** La stringa non deve apparire a
schermo: deve **coincidere con quello che il giocatore batte**. In CP932 la `à`
non esiste, quindi nessuno puo' digitarla, e un `del_str` su «abilita'» non
aggancerebbe mai niente. E' il rovescio della regola degli accenti del progetto.

⚠️ Sostituzione 1:1 sulle righe; il ramo giapponese resta intatto.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\command.hsp'
NOME = 'command.hsp'
RIGA = 4335

INGLESE = '"skill "'
ITALIANO = '"abilita "'

MOTIVO = (
    "command.hsp:4335, `*wish_fix`. Le righe `:4335` e `:4336` sono la stessa "
    "`lang(\"スキル\", …)` con due inglesi diversi — «skill » con lo spazio e «skill» "
    "senza — e l'ordine conta: la prima porta via anche lo spazio. La rete 4 "
    "raggruppa per giapponese e pretende una resa sola, e in generale ha ragione; "
    "qui a distinguerle e' uno **spazio**, e il giapponese non ne ha bisogno perche' "
    "il suo ramo li ha gia' tolti a `:4328`. "
    "⚠️ Con una resa sola resterebbe uno spazio in testa a `inputlog`, e `:4887` "
    "fa il punteggio sui **prefissi** della stringa: con lo spazio davanti "
    "diventano « », « s», « sp» e l'oggetto giusto non vince piu'. "
    "✅ Rinvio + toppa: `:4336` prende «abilita» dal dizionario, `:4335` esce dal "
    "dizionario e la scrive questa toppa. "
    "⚠️⚠️ «abilita» e' senza accento di proposito: la stringa non si legge, si "
    "**digita**, e in CP932 la à non esiste. Un `del_str` su «abilita'» non "
    "aggancerebbe mai niente. "
    "⚠️ Sostituzione 1:1 sulle righe."
)

righe = io.open(SORGENTE, encoding='cp932').read().split('\n')
originale = righe[RIGA - 1]

if INGLESE not in originale or 'del_str' not in originale:
    raise SystemExit(f'{NOME}:{RIGA} non ha la forma attesa: {originale.strip()[:120]}')

nuova = originale.replace(INGLESE, ITALIANO)
if nuova == originale:
    raise SystemExit('la toppa non cambierebbe niente')

quante = sum(1 for r in righe if r == originale)
if quante != 1:
    raise SystemExit(f'la riga compare {quante} volte, non una: toppa ambigua')

nuova_toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova, 'motivo': MOTIVO}

esistenti = [l for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]


def _chiave(t: dict) -> tuple:
    cerca = t['cerca']
    return (t['file'], tuple(cerca) if isinstance(cerca, list) else cerca)


gia = {_chiave(json.loads(l)) for l in esistenti}
if _chiave(nuova_toppa) in gia:
    print('toppa gia presente')
else:
    dati = (json.dumps(nuova_toppa, ensure_ascii=False) + '\n').encode('utf-8')
    with io.open('toppe.jsonl', 'ab') as f:
        f.write(dati)
    print(f'toppa aggiunta (totale {len(esistenti) + 1})')
    print(f'  - {originale.strip()}')
    print(f'  + {nuova.strip()}')

# --- il rinvio, che e' l'altra meta' --------------------------------------
CHIAVE = (RIGA, 'skill ')
voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_command.jsonl', encoding='utf-8') if l.strip())}
if CHIAVE not in voci:
    raise SystemExit(f'chiave che non aggancia nessuna voce: {CHIAVE}')
v = voci[CHIAVE]
rinviata = {
    'firma': v['firma'],
    'file': NOME,
    'en': v['en'],
    'rinviata_a': 'mai: la riga la sistema la toppa su command.hsp:4335',
    'motivo': MOTIVO,
}

esistenti_r = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
firme = {json.loads(l)['firma'] for l in esistenti_r}
if rinviata['firma'] in firme:
    print('rinvio gia presente')
else:
    dati = (json.dumps(rinviata, ensure_ascii=False) + '\n').encode('utf-8')
    with io.open('rinviate.jsonl', 'ab') as f:
        f.write(dati)
    print(f'rinvio aggiunto (totale {len(esistenti_r) + 1})')
