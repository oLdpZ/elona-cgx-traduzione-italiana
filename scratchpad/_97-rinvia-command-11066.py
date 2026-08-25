# -*- coding: utf-8 -*-
"""97a - `command.hsp:11066`: la QUINTA famiglia di riga morta, morta per assegnazione.

    11064   if ( csctrl == 300 & (sdata(i, cc) != 0 | sorg(i, cc) != 0) ) {
    11065       s = ""
    11066       s += lang("*", "#")
    11067       /********** JAMES CUSTOM - SHOW BONUS BY DEFAULT - BEGINNING **********/
    11068       color 0, 0, 0
    11069       s = "Have"
    11070       /********** JAMES CUSTOM - SHOW BONUS BY DEFAULT - ENDING **********/
    11071       pos wx + 282, wy + 66 + cnt * 19 + 2
    11072       mes s

`:11066` appende il segno a `s`, e tre righe dopo `:11069` **riassegna `s`**.
Quel che `mes` disegna e' `"Have"`: il valore della `lang()` non arriva a
schermo nemmeno una volta.

⚠️ E' una famiglia che il progetto non aveva ancora incontrato. Le quattro note
sono il `;` (rete 6), il commento di blocco `/* … */` (`commenti-blocco.py`), il
ramo `if ( jp )` (`lang-nel-ramo-jp.py`) e l'`if ( 0 )` (`if-zero.py`), e le
riconoscono tutte guardando **dove sta la riga**. Questa no: la riga e' viva, il
blocco e' vivo, la `lang()` e' vera, e a spegnerla e' **la riga dopo**. Nessuna
delle quattro reti la vede, e nemmeno `_96-morte-nella-build.py`, che confronta
il sorgente con la build e qui trova la riga in tutt'e due.

⚠️⚠️ **E c'e' una seconda cosa, ed e' piu' grossa del rinvio:** `:11069` scrive
`s = "Have"`, cioe' un **letterale inglese nudo** che il giocatore legge nel
pannello «Scelta delle abilità» (`csctrl == 300`). Non passa da nessuna `lang()`,
quindi non e' nel dizionario, non e' in nessun conteggio di «non tradotte», e si
ripara con una **toppa**, non con una resa. Sta gia' nell'elenco di
`scratchpad/blocchi_en.py` (`command.hsp`: 10 righe, tutte da fare).
"""
import io
import json

FILE = 'command.hsp'
RIGA, EN = 11066, '#'

MOTIVO = (
    "`command.hsp:11066` e' `s += lang(\"*\", \"#\")`, e tre righe dopo `:11069` "
    "**riassegna** `s = \"Have\"` prima che `:11072` faccia `mes s`: il valore "
    "della `lang()` viene buttato, e a schermo non ci arriva mai. "
    "⚠️ **E' la quinta famiglia di riga morta del progetto, e la prima che non "
    "si riconosce da dove sta la riga**: non e' il `;`, non e' il commento di "
    "blocco, non e' il ramo `if ( jp )`, non e' l'`if ( 0 )`. La riga e' viva, "
    "il blocco e' vivo, la `lang()` e' vera — a spegnerla e' **la riga dopo**, e "
    "nessuna delle quattro reti esistenti guarda quel che succede al valore "
    "dopo che e' stato costruito. ⭐ Il segno che resta a schermo e' un "
    "letterale inglese nudo, `\"Have\"` (`:11069`), che vuole una **toppa** e "
    "non una resa: sta nell'elenco di `scratchpad/blocchi_en.py`. "
    "✅ Si sblocca il giorno in cui quella toppa dara' un italiano a `\"Have\"`; "
    "allora questa `lang()` non servira' comunque, perche' il testo giusto sara' "
    "quello della toppa."
)

voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_97-command-tutto.jsonl', encoding='utf-8')
                  if l.strip())}
if (RIGA, EN) not in voci:
    raise SystemExit(f'chiave che non aggancia nessuna voce: {(RIGA, EN)}')
v = voci[(RIGA, EN)]

esistenti = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
if any(json.loads(l)['firma'] == v['firma'] for l in esistenti):
    raise SystemExit('gia presente, niente da fare')

nuova = {
    'firma': v['firma'],
    'file': FILE,
    'en': v['en'],
    'rinviata_a': "con la toppa che dara' un italiano al letterale nudo `\"Have\"` di `:11069`",
    'motivo': MOTIVO,
}

# ⚠️ si compone e si codifica prima di toccare il file (la 39a)
dati = (json.dumps(nuova, ensure_ascii=False) + '\n').encode('utf-8')
with io.open('rinviate.jsonl', 'ab') as f:
    f.write(dati)
print(f'rinviata aggiunta (totale {len(esistenti) + 1})')
