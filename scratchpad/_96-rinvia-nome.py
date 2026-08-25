# -*- coding: utf-8 -*-
"""96a - I sei rinvii del lotto `itemNameSub` di `item_func.hsp`.

Nessuna delle sei e' mai stata tradotta: il rinvio le toglie dalla coda, non
dal dizionario. Tre ragioni diverse, e due sono **strutturali**, cioe' non si
sciolgono scrivendo una resa migliore.

1. **`:704` sta dentro un commento di blocco.** `:702`-`:706` sono
   `/********** ORIGINAL - BEGINNING **********  …  - ENDING **********/`, il
   codice di monte che il mod BLOODYSHADE ha spento per dare il plurale ai nomi
   degli oggetti d'evoluzione. La riga viva e' `:710`.
   ⚠️⚠️ **E `estrai --da-tradurre` l'ha pescata lo stesso.** `strumenti/commenti.py`
   esiste dalla 60a e sa riconoscere questi blocchi, ma **l'estrazione non lo
   chiama**: e' una rete che c'e' e che nessuno interroga sulla coda del lavoro.
   E' la stessa forma del guasto dell'87a — un lotto costruito su righe
   commentate a monte. Trovata solo perche' il lotto e' stato passato a mano per
   `righe_in_commento()` prima di scrivere.

2. **Le quattro del succo (`:926`, `:930`, `:933`, `:936`): il frutto viene
   prima.** `:924` scrive `iknownnameref(sottonome) + lang("", " ")`, cioe' il
   nome del frutto, e solo dopo arrivano ミックス / オーレ / ジュース. In inglese
   il risultato e' «apple juice» e l'ordine regge; in italiano la testa del
   sintagma e' **succo**, e va davanti: «succo di mela». Il pezzo che si potrebbe
   tradurre e' l'ultimo dei tre, e nessuna resa lo puo' spostare.
   ⚠️ **Non e' il muro del materiale, ma e' lo stesso muro.** `contratto-nomi.md`
   §3 dice gia' come si scioglie: **dove i pezzi si uniscono e' codice nostro**,
   quindi si sposta la concatenazione con una toppa, invece di piegare il
   lessico all'ordine inglese.
   💡 Il caffe' e il te' (`:941`-`:952`) **non** sono rinviati: li' il nome base
   e' vuoto e non c'e' nessun frutto davanti, quindi «caffelatte» e «te' al
   latte» escono interi e nell'ordine giusto. La differenza fra le due famiglie
   e' una riga sola, `:924`.

3. **`:974` dipende da una voce gia' rinviata.** La riga e'
   `lang("", " grown ") + _weight(...) + lang("育った", "")`: la parola che
   conta la scrive `_weight()`, che sta fra i **35 modificatori di qualita'**
   rinviati dal contratto dei nomi (`contratto-nomi.md` §6). Tradurre la
   cornice prima del suo contenuto vuol dire scegliere una preposizione senza
   sapere che parola reggera'.

La forma dello script segue la regola della 39a: si compone tutto in memoria, si
codifica, e solo allora si apre il file in scrittura.
"""
import io
import json

FILE = 'item_func.hsp'

RINVII = {
    704: (
        'nessuna fase: la riga sta in un commento di blocco',
        "La `lang()` sta dentro `/********** ORIGINAL - BEGINNING **********` "
        "(`item_func.hsp:702`-`:706`), il codice di monte spento dal mod "
        "BLOODYSHADE che dava il plurale ai nomi degli oggetti d'evoluzione. La "
        "riga viva e' `:710`, che fa la stessa cosa e in piu' distingue "
        "singolare e plurale con `:713`/`:716`. "
        "⚠️ `strumenti/commenti.py` sa riconoscere questi blocchi dalla 60a, ma "
        "**`estrai --da-tradurre` non lo chiama**: la voce e' arrivata nel lotto "
        "come se fosse lavoro. E' la stessa forma del guasto dell'87a, dove un "
        "piano intero era stato costruito su righe commentate a monte. La rete "
        "c'e' e non e' agganciata alla coda: e' un difetto della catena, non di "
        "questa riga."
    ),
    926: (
        'Fase 4: vuole la toppa che sposta la concatenazione',
        "Il separatore fra il nome del frutto e la parola «succo» "
        "(`item_func.hsp:926`). `:924` scrive prima `iknownnameref(sottonome)`, "
        "cioe' il frutto, e solo dopo arrivano ミックス/オーレ/ジュース: in "
        "inglese esce «apple juice» e l'ordine regge, in italiano la testa e' "
        "**succo** e va davanti — «succo di mela». Nessuna resa di questa "
        "`lang()` puo' spostare i pezzi. Si scioglie come dice "
        "`contratto-nomi.md` §3: **dove i pezzi si uniscono e' codice nostro**, "
        "quindi con una toppa. ⚠️ Il caffe' (`:941`, `:944`) e il te' (`:949`, "
        "`:952`) non hanno questo problema e sono stati tradotti nella 96a: li' "
        "davanti non c'e' niente."
    ),
    930: (
        'Fase 4: vuole la toppa che sposta la concatenazione',
        "ミックス, la parola che marca il succo con le erbe "
        "(`item_func.hsp:930`). Stessa ragione di `:926`: arriva **dopo** il "
        "nome del frutto scritto da `:924`, e in italiano la testa del sintagma "
        "va davanti. ⚠️ E qui l'inglese e' anche sciatto per conto suo: "
        "`ITEM_BIT_HERBED_IN` e `ITEM_BIT_ACIDPROOF` non si escludono, quindi "
        "un succo con entrambi esce «apple mixjuice», attaccato."
    ),
    933: (
        'Fase 4: vuole la toppa che sposta la concatenazione',
        "オーレ (au lait), il succo al latte (`item_func.hsp:933`). Stessa "
        "ragione di `:926`: viene dopo il nome del frutto."
    ),
    936: (
        'Fase 4: vuole la toppa che sposta la concatenazione',
        "ジュース, la parola «succo» (`item_func.hsp:936`). Stessa ragione di "
        "`:926`, ed e' la voce che rende evidente il problema: e' **la testa del "
        "sintagma italiano**, e il codice la mette per ultima."
    ),
    974: (
        'Fase 4: dipende da `_weight()`, gia\' rinviato',
        "La cornice del cibo cresciuto in una missione: `item_func.hsp:974` fa "
        "`lang(\"\", \" grown \") + _weight(...) + lang(\"育った\", \"\")`. La "
        "parola che porta il senso la scrive `_weight()`, che sta fra i **35 "
        "modificatori di qualita'** rinviati da `contratto-nomi.md` §6 insieme a "
        "`_bookself` e `_furniture`. Tradurre la cornice adesso vuol dire "
        "scegliere una preposizione senza sapere che parola reggera': si fa "
        "quando si fa quella famiglia, e nello stesso lotto."
    ),
}

# --- le voci esistono, e sono quelle che diciamo ----------------------------

voci = [json.loads(l) for l in io.open('lavoro/_item_func.jsonl', encoding='utf-8')
        if l.strip()]
per_riga = {}
for v in voci:
    per_riga.setdefault(v['riga'], []).append(v)

bersagli = []
for riga in RINVII:
    trovate = per_riga.get(riga, [])
    if len(trovate) != 1:
        raise SystemExit(f'attesa 1 voce a :{riga}, trovate {len(trovate)}')
    bersagli.append(trovate[0])

diz = {json.loads(l)['firma'] for l in io.open(f'dizionario/{FILE}.jsonl', encoding='utf-8')
       if l.strip()}
gia_rese = [v['riga'] for v in bersagli if v['firma'] in diz]
if gia_rese:
    raise SystemExit(f'queste sono gia\' nel dizionario, il rinvio le perderebbe: {gia_rese}')

# --- il rinvio non c'e' gia' ------------------------------------------------

righe_rin = [l for l in io.open('rinviate.jsonl', encoding='utf-8').read().splitlines()
             if l.strip()]
firme_rin = {json.loads(l)['firma'] for l in righe_rin}
nuove = [v for v in bersagli if v['firma'] not in firme_rin]
if not nuove:
    raise SystemExit('rinvii gia\' presenti: niente da fare')

# --- si compone tutto, e solo allora si scrive ------------------------------

rin_nuovo = righe_rin + [
    json.dumps({
        'firma': v['firma'],
        'file': FILE,
        'en': v['en'],
        'rinviata_a': RINVII[v['riga']][0],
        'motivo': RINVII[v['riga']][1],
    }, ensure_ascii=False)
    for v in nuove
]

with io.open('rinviate.jsonl', 'wb') as f:
    f.write(('\n'.join(rin_nuovo) + '\n').encode('utf-8'))

print('rinviate.jsonl: %d -> %d' % (len(righe_rin), len(rin_nuovo)))
for v in nuove:
    print('  :%-6d %r' % (v['riga'], v['en']))
