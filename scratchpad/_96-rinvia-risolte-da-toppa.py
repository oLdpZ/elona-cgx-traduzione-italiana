# -*- coding: utf-8 -*-
"""96a - Le quattro firme che una toppa aveva gia' risolto, e che nessuno aveva rinviato.

Trovate da `scratchpad/_96-morte-nella-build.py`, rete nuova della 96a: cerca
nella **build** le firme che il conto delle «non ancora tradotte» considera
lavoro, e le trova sparite. Su tutto il progetto sono quattro.

Non sono difetti: sono toppe che hanno **riscritto la riga**, cioe' il modo in
cui il progetto risolve quel che una resa non puo' — un prefisso da spostare, un
nome di file da cambiare. Il difetto e' che nessuna delle quattro era in
`rinviate.jsonl`, quindi restavano contate come lavoro da fare: un numero che
non sarebbe mai sceso a zero, e prima o poi una resa scritta in buona fede per
una riga che il giocatore non incontra.

    command.hsp:16405   lang("それは", "It ") + s      ->  lang("それは", "") + s
    etc.hsp:335         "data\\ndata-e.csv"           ->  "data\\ndata-i.csv"
    item_func.hsp:1399  mtname(…) + lang("細工の","work ")
    item_func.hsp:1404       ->  locvar_itemname_s6 += " di manifattura in " + mtname(…)

⭐⭐ Le due di `item_func.hsp` sono la scoperta che cambia il piano del file: il
**muro del materiale** per i mobili **e' gia' abbattuto**, da una toppa che
sposta il materiale in `locvar_itemname_s6`, cioe' in coda al nome, dove
l'italiano lo vuole. La 96a era partita convinta che quelle 24 firme fossero
tutte bloccate.
"""
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti import estrai

SORGENTE = Path('C:/Games/Elona/_traduzione/sorgente/2.05-custom-gx')

BERSAGLI = {
    ('command.hsp', 16405): (
        "Il «It » che l'inglese mette davanti alla voce di una lista "
        "(`command.hsp:16405`, `listn(0, p) = lang(\"それは\", \"It \") + s`). "
        "⚠️ **Risolta da toppa**: nella build la riga e' `lang(\"それは\", \"\")`, "
        "cioe' il prefisso e' **svuotato**, perche' in italiano quel «It » non "
        "regge davanti a un nome che porta gia' il proprio articolo — la stessa "
        "decisione del «The » di `action.hsp` e di `init.hsp:1718`. Una resa qui "
        "non arriverebbe mai a schermo. Rinviata nella 96a, dopo che "
        "`scratchpad/_96-morte-nella-build.py` l'ha trovata ancora contata come "
        "lavoro."
    ),
    ('etc.hsp', 335): (
        "Il nome del file dei dati caricato da `noteload` (`etc.hsp:335`): "
        "l'inglese e' `data\\\\ndata-e.csv`. ⚠️ **Risolta da toppa**, che nella "
        "build lo cambia in `data\\\\ndata-i.csv`, il file italiano — la stessa "
        "disciplina di `board_it.txt` e `talk_it.txt`. Non e' testo, e' un "
        "**indirizzo**, e la famiglia sta gia' in `invariati.md` sotto «Chiavi e "
        "nomi di file». Rinviata nella 96a."
    ),
    ('item_func.hsp', 1399): (
        "Il 細工の / «work » che l'inglese mette **davanti** al nome di un "
        "mobile, dopo il materiale (`item_func.hsp:1399`). ⚠️ **Risolta da "
        "toppa**: nella build la riga diventa `locvar_itemname_s6 += \" di "
        "manifattura in \" + mtname(…)`, cioe' il materiale **si sposta in "
        "coda** al nome, dove l'italiano lo vuole — «una sedia di manifattura in "
        "mithril» invece di «mithril work sedia». E' `contratto-nomi.md` §3 "
        "applicato: dove i pezzi si uniscono e' codice nostro. "
        "⭐ Vuol dire che il **muro del materiale** per i mobili e' gia' "
        "abbattuto, e la 96a era partita credendo il contrario. Rinviata nella "
        "96a."
    ),
    ('item_func.hsp', 1404): (
        "Lo stesso 細工の / «work » del ramo dei fiori selvatici "
        "(`item_func.hsp:1404`): la stessa toppa lo sposta in "
        "`locvar_itemname_s6`. Vedi `:1399`. Rinviata nella 96a."
    ),
}

righe_rin = [l for l in io.open('rinviate.jsonl', encoding='utf-8').read().splitlines()
             if l.strip()]
firme_rin = {json.loads(l)['firma'] for l in righe_rin}

nuove = []
for (nome, riga), motivo in sorted(BERSAGLI.items()):
    trovate = [v for v in estrai.estrai_da_file(SORGENTE / nome) if v['riga'] == riga]
    if len(trovate) != 1:
        raise SystemExit(f'attesa 1 firma a {nome}:{riga}, trovate {len(trovate)}')
    v = trovate[0]
    if v['firma'] in firme_rin:
        print(f'  {nome}:{riga} gia\' rinviata')
        continue
    nuove.append(json.dumps({
        'firma': v['firma'],
        'file': nome,
        'en': v['en'],
        'rinviata_a': 'nessuna fase: risolta da toppa',
        'motivo': motivo,
    }, ensure_ascii=False))

if not nuove:
    raise SystemExit('niente da fare')

with io.open('rinviate.jsonl', 'wb') as f:
    f.write(('\n'.join(righe_rin + nuove) + '\n').encode('utf-8'))
print('rinviate.jsonl: %d -> %d' % (len(righe_rin), len(righe_rin) + len(nuove)))
