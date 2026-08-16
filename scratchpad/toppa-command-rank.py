# -*- coding: utf-8 -*-
"""` Rank.` -> `, grado `: la prima toppa `tutte` del progetto.

`command.hsp:2901` (il diario) e `:17848` (la scheda di `*dump_chara`) sono la
stessa riga byte per byte:

    noteadd "" + ranktitle(cnt) + " Rank." + gdata(STARTING_GDATA_RANK + cnt) / 100

Il lotto del diario della 50a ha dovuto lasciarla fuori, e il motivo era preciso:
le quattro righe sopra e sotto sono identiche nei due siti, e la prima che li
distingue (`:2897`, `noteadd lang("名声: ", "Fame: ")`) porta una **resa**, che
nella build il dizionario ha gia' riscritto — un blocco che la raggiunge aggancia
il sorgente pinnato, come `test_toppe.py:104` pretende, ma non aggancia piu' la
build, dove le toppe girano davvero.

✅ Con `"tutte": true` la domanda «quale delle due?» non si pone piu': **tutt'e
due**, e con la stessa resa. E' il caso per cui la deroga e' nata.

## Che cosa dice, e perche' «grado»

`ranktitle()` (`init.hsp:337`) restituisce il **titolo** della gilda o dell'arena
— quelli tradotti nei ranghi della 41ª, «Campione dell'arena», «Signore di
Nefia» — e il numero che segue e' la posizione dentro quel rango. In inglese esce
«Arena champion Rank.5», che in italiano non si puo' ricalcare: «Rank.» non e'
una parola nostra e il punto fa da separatore solo in inglese.

    Campione dell'arena Rank.5   ->   Campione dell'arena, grado 5

⚠️ La virgola non e' un vezzo: senza, «Campione dell'arena grado 5» si legge come
un titolo unico, e il numero smette di essere una posizione. Con la virgola il
titolo resta il titolo e il grado e' un'aggiunta, che e' esattamente la struttura
del giapponese.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'command.hsp'
RIGHE_ATTESE = (2901, 17848)
CERCA = '" Rank."'
METTI = '", grado "'

MOTIVO = (
    "command.hsp:2901 (il diario) e :17848 (la scheda di *dump_chara): la stessa riga "
    "byte per byte, `noteadd \"\" + ranktitle(cnt) + \" Rank.\" + ...`, cioe' il titolo "
    "di gilda o d'arena col numero di posizione. "
    "⭐ E' la PRIMA toppa `tutte` del progetto, e il caso per cui la deroga e' nata: il "
    "lotto del diario della 50a l'aveva dovuta lasciare fuori perche' le quattro righe "
    "sopra e sotto sono identiche nei due siti, e la prima che li distingue (:2897, "
    "`noteadd lang(\"名声: \", \"Fame: \")`) porta una resa che nella build il dizionario "
    "ha gia' riscritto — un blocco che la raggiunge aggancia il sorgente pinnato, come "
    "test_toppe.py:104 pretende, ma non aggancia piu' la build. Con `tutte` la domanda "
    "«quale delle due?» non si pone: tutt'e due, con la stessa resa. "
    "⚠️ La resa: `ranktitle()` (init.hsp:337) restituisce il TITOLO — quelli tradotti "
    "nei ranghi della 41a, «Campione dell'arena», «Signore di Nefia» — e il numero che "
    "segue e' la posizione dentro quel rango. «Rank.» non e' una parola italiana e il "
    "punto fa da separatore solo in inglese: «Campione dell'arena, grado 5». La virgola "
    "non e' un vezzo, senza di lei «Campione dell'arena grado 5» si legge come un "
    "titolo unico e il numero smette di essere una posizione. "
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo. Quinto punto "
    "cieco (`nudi_en.py`, 49a; `triage_nudi.py`, 50a)."
)

sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')
originale = sorg[RIGHE_ATTESE[0] - 1]

if CERCA not in originale:
    raise SystemExit(f'{NOME}:{RIGHE_ATTESE[0]} non ha la forma attesa: {originale.strip()[:110]}')
# ⚠️ `tutte` non e' una scusa per non guardare: le occorrenze si contano, e devono
#    essere quelle che si e' deciso di toccare, non una di piu'.
for righe, eti in ((sorg, 'sorgente'), (build, 'build')):
    trovate = tuple(i + 1 for i, r in enumerate(righe) if r == originale)
    if trovate != RIGHE_ATTESE:
        raise SystemExit(f'{NOME}: nel {eti} la riga sta a {trovate}, non a {RIGHE_ATTESE}')
if 'lang("' in originale:
    raise SystemExit(f'{NOME}: la riga porta anche una resa')

nuova = originale.replace(CERCA, METTI)
try:
    nuova.encode('cp932')
except UnicodeEncodeError as errore:
    raise SystemExit(f'testo che CP932 non sa scrivere ({errore})')

toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova,
         'tutte': True, 'motivo': MOTIVO}

esistenti = [l for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]


def _chiave(t: dict) -> tuple:
    cerca = t['cerca']
    return (t['file'], tuple(cerca) if isinstance(cerca, list) else cerca)


if _chiave(toppa) in {_chiave(json.loads(l)) for l in esistenti}:
    print('toppa gia presente, niente da fare')
else:
    # ⚠️ Si compone, si codifica in memoria e solo allora si apre: vedi la 39a.
    dati = (json.dumps(toppa, ensure_ascii=False) + '\n').encode('utf-8')
    with io.open('toppe.jsonl', 'ab') as f:
        f.write(dati)
    print(f'1 toppa `tutte` aggiunta (totale {len(esistenti) + 1}), righe {RIGHE_ATTESE}')
    print(f'  - {originale.strip()}')
    print(f'  + {nuova.strip()}')
