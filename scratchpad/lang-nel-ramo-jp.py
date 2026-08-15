# -*- coding: utf-8 -*-
"""Il QUINTO punto cieco: una `lang()` chiusa dentro un ramo `if ( jp )`.

Trovato il 2026-08-15 (45a) aprendo `command.hsp:2954`, il diario delle
statistiche: settanta righe dentro `if ( jp ) { ... }` con dentro sette `lang()`
vere — « level», « Miles», « Hours», « Days», « Guest», « Plat», « points» — e
un ramo `else` che stampa le stesse cifre **in inglese nudo**. In italiano quel
ramo non gira: tradurre quelle sette e' lavoro su testo che nessuno leggera'.

E' la **terza famiglia di riga morta**, dopo la riga commentata col `;` e il
blocco `/* ... */` (`commenti-blocco.py`). Le prime due si vedono: c'e' un
carattere che le spegne. Questa no — la riga e' viva, il file e' vivo, la
`lang()` e' vera — e a spegnerla e' il **ramo della lingua**.

⚠️ Non e' il gemello di `else_jp.py`, e' il suo **rovescio**. Quello cerca
l'inglese nudo dentro l'`else` di un `if ( jp )`, cioe' il testo che il
giocatore legge e che nessuna `lang()` copre. Questo cerca la `lang()` che sta
**dall'altra parte** e che nessuno leggera'. Sono i due lati dello stesso `if`,
e fin qui se ne guardava uno solo.

Referto, non guardia: dice quante ce ne sono, quante sono gia' state tradotte
(lavoro speso) e quante restano da fare (lavoro da non fare).

    python scratchpad/lang-nel-ramo-jp.py
"""
import glob
import io
import json
import os
import re

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'

APRE_JP = re.compile(r'^\s*if\s*\(\s*jp\s*\)\s*\{')
LANG = re.compile(r'\blang\s*\(')
# ⚠️ `font lang(cfg_font1, cfg_font2), 13 - en * 2, 0` e' una `lang()` vera che
# non porta testo: sceglie il **nome del font**. Senza questo filtro il referto
# contava 24 righe dove le voci sono 19, e tre dei quattro file erano gonfiati
# da righe di `font`. Una `lang()` e' testo solo se ha un letterale dentro.
LETTERALE = re.compile(r'"(?:[^"\\]|\\.)*"')


def righe_nel_ramo_jp(righe: list) -> set:
    """I numeri di riga (1-based) che stanno dentro un `if ( jp ) { ... }`.

    Il conteggio delle graffe basta perche' HSP le scrive sempre esplicite in
    questo sorgente: `if ( jp ) {` apre, e il ramo finisce dove il contatore
    torna a zero. ⚠️ Le graffe dentro una stringa non esistono in questi file,
    ma per prudenza si contano solo quelle fuori dalle virgolette.
    """
    dentro = set()
    profondita = None
    for numero, riga in enumerate(righe, 1):
        if profondita is None:
            if APRE_JP.match(riga):
                profondita = 1
            continue
        dentro.add(numero)
        fuori_dalle_virgolette = re.sub(r'"(?:[^"\\]|\\.)*"', '', riga)
        profondita += fuori_dalle_virgolette.count('{') - fuori_dalle_virgolette.count('}')
        if profondita <= 0:
            dentro.discard(numero)   # la riga della graffa che chiude non e' corpo
            profondita = None
    return dentro


# le rese gia' entrate, per (file, riga)
rese = {}
for percorso in sorted(glob.glob('dizionario/*.jsonl')):
    nome = os.path.basename(percorso).replace('.jsonl', '')
    for l in io.open(percorso, encoding='utf-8'):
        if not l.strip():
            continue
        v = json.loads(l)
        if v.get('it'):
            rese.setdefault((nome, v['riga']), 0)
            rese[(nome, v['riga'])] += 1

totale = gia_reso = da_fare = 0
per_file = []
for percorso in sorted(glob.glob(os.path.join(SORGENTE, '*.hsp'))):
    nome = os.path.basename(percorso)
    righe = io.open(percorso, encoding='cp932').read().split('\n')
    dentro = righe_nel_ramo_jp(righe)
    if not dentro:
        continue
    con_lang = [n for n in sorted(dentro)
                if LANG.search(righe[n - 1]) and LETTERALE.search(righe[n - 1])]
    if not con_lang:
        continue
    spese = [n for n in con_lang if (nome, n) in rese]
    totale += len(con_lang)
    gia_reso += len(spese)
    da_fare += len(con_lang) - len(spese)
    per_file.append((nome, len(con_lang), len(spese), con_lang[:6]))

print(f'{totale} righe con `lang()` dentro un ramo `if ( jp )`\n')
print(f'  gia\' tradotte (lavoro speso su testo che l\'italiano non legge): {gia_reso}')
print(f'  ancora da fare (lavoro da non fare)                            : {da_fare}\n')
for nome, quante, spese, prime in sorted(per_file, key=lambda x: -x[1]):
    esempi = ', '.join(f':{n}' for n in prime)
    print(f'  {nome:28} {quante:4} righe, {spese:3} gia\' rese   {esempi}')
