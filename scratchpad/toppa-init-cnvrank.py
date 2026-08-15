# -*- coding: utf-8 -*-
"""`cnvrank` costruisce l'ordinale INGLESE con letterali nudi, fuori da `lang()`.

⚠️⚠️ `init.hsp:149`-`:168` e' `#defcfunc cnvrank int cnvrank_rank`: il ramo
giapponese (`:150`-`:152`) restituisce il numero e basta, e tutto il resto
attacca `"st"`, `"nd"`, `"rd"`, `"th"` secondo la regola inglese. Nessuna di
quelle quattro stringhe sta dentro una `lang()`, quindi **il dizionario non le
raggiunge** e in italiano il gioco stampa «5th», «21st», «3rd».

E' il **secondo punto cieco** (`blocchi_en.py`) in una forma che nemmeno quello
vede: i letterali non stanno dentro un `if ( en )`, stanno **dopo** un
`if ( jp ) { return }`, cioe' in un ramo inglese implicito.

⚠️ **Sedici siti la chiamano**, in sei file: `command.hsp` (3, fra cui la lista
dei luoghi di ritorno `:17435` e l'arena EX `:2911`), `main.hsp` (5),
`map_user.hsp` (3), `chat.hsp` (2), `net.hsp` (2), `text.hsp` (1). Una toppa sola
li sistema tutti.

✅ **La toppa restituisce il numero nudo anche in italiano**, cioe' fa fare al
ramo inglese quel che fa gia' il ramo giapponese: `if ( jp )` diventa
`if ( jp | en )`. L'ordinale, dove serve, lo mette la **resa italiana del sito** —
a `:17435` «5 liv.» — e non una funzione che non sa in che frase finira'.
⚠️ **E l'italiano non poteva scriverlo comunque**: l'ordinale sarebbe «5°», ma il
grado in CP932 e' un carattere a **doppia larghezza** (`0x81 0x8b`) e
`scratchpad/guardie.py` li vieta tutti tranne `♪`. La strada del numero nudo non
e' un ripiego: e' l'unica.

⚠️ **La sostituzione e' 1:1 sulle righe**, di proposito: aggiungere anche una
sola riga a `init.hsp` sfaserebbe i numeri di riga fra build e sorgente, e il
dizionario e' indicizzato sul **sorgente** (la nota della 37ª su `text.hsp`).
"""
import io
import json

# ⚠️ `applica.py` cerca **per righe**, non nel testo intero: una toppa che ne
# tocca due si scrive come LISTA di righe. La prima riga da sola non basterebbe,
# perche' `if ( jp ) {` compare decine di volte in `init.hsp`, e la coppia
# `#defcfunc cnvrank` + la sua guardia e' unica.
CERCA = ['#defcfunc cnvrank int cnvrank_rank', '\tif ( jp ) {']
METTI = ['#defcfunc cnvrank int cnvrank_rank', '\tif ( jp | en ) {']

MOTIVO = (
    "`cnvrank` costruisce l'ordinale inglese con letterali nudi fuori da "
    "`lang()`: dopo il `return` del ramo giapponese attacca \"st\", \"nd\", "
    "\"rd\", \"th\" secondo la regola inglese, e in italiano il gioco stampa "
    "«5th», «21st», «3rd». Il dizionario non arriva: non e' testo dentro una "
    "`lang()`. ⚠️ Nemmeno `blocchi_en.py` lo vede, perche' i letterali non "
    "stanno in un `if ( en )` ma **dopo** un `if ( jp ) { return }`, cioe' in un "
    "ramo inglese implicito. Sedici siti la chiamano, in sei file. "
    "✅ La toppa fa fare al ramo italiano quel che fa gia' il giapponese — "
    "restituire il numero nudo — e lascia l'ordinale alla resa del singolo sito, "
    "che sa in che frase finisce. ⚠️ L'italiano non poteva scriverlo comunque: "
    "«5°» vorrebbe il grado, che in CP932 e' a doppia larghezza e le guardie del "
    "progetto lo vietano. "
    "⚠️ Sostituzione 1:1 sulle righe: aggiungerne una sfaserebbe i numeri di "
    "riga fra build e sorgente, e il dizionario e' indicizzato sul sorgente."
)

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\init.hsp'

righe_sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')
quante = sum(1 for i in range(len(righe_sorgente) - len(CERCA) + 1)
             if righe_sorgente[i:i + len(CERCA)] == CERCA)
if quante != 1:
    raise SystemExit(f'il blocco cercato compare {quante} volte, non una: toppa ambigua')
if len(CERCA) != len(METTI):
    raise SystemExit('la sostituzione cambia il numero di righe')

nuova = {'file': 'init.hsp', 'cerca': CERCA, 'sostituisci': METTI, 'motivo': MOTIVO}

esistenti = [l for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]


def _chiave(t: dict) -> tuple:
    """⚠️ `cerca` puo' essere una stringa o una LISTA di righe: `item_func.hsp`
    ha ventinove toppe scritte cosi', e una `set` di liste non si costruisce."""
    cerca = t['cerca']
    return (t['file'], tuple(cerca) if isinstance(cerca, list) else cerca)


gia = {_chiave(json.loads(l)) for l in esistenti}
if _chiave(nuova) in gia:
    print('gia presente, niente da fare')
else:
    # ⚠️ si compone e si codifica prima di toccare il file (la 39a)
    dati = (json.dumps(nuova, ensure_ascii=False) + '\n').encode('utf-8')
    with io.open('toppe.jsonl', 'ab') as f:
        f.write(dati)
    print(f'toppa aggiunta (totale {len(esistenti) + 1})')
