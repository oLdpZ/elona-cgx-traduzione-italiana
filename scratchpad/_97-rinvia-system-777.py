# -*- coding: utf-8 -*-
"""97a - `system.hsp:777`: dentro un commento di blocco, e la gemella e' gia' resa.

    777   txt lang("注意！スペルボーナス…100以上所持していると新たに獲得できない。",
                    "Caution! While the spell bonus is 100 or more, you cannot get new.")

La riga sta dentro un tratto `/* … */` che il mod ha spento: `_97-vive.py` dice
MORTA, cioe' **tutte** le occorrenze della firma in questo file sono spente.

⭐ E non e' testo perduto: lo **stesso avviso** vive in `screen.hsp:6792`, ed e'
gia' reso — «Attenzione! Con un bonus magia di 100 o piu' non se ne ottengono
altri.» Quindi il giocatore quella frase la legge, e la legge in italiano; qui
non c'e' niente da tradurre, c'e' una copia spenta da togliere dalla coda.
"""
import io
import json

FILE = 'system.hsp'
RIGA = 777
EN = 'Caution! While the spell bonus is 100 or more, you cannot get new.'

MOTIVO = (
    "`system.hsp:777` sta dentro un commento di blocco `/* … */`: il mod ha "
    "spento il tratto e la riga non si compila. `python scratchpad/_97-vive.py "
    "system.hsp …` la da' **MORTA**, cioe' non esiste nessuna occorrenza viva "
    "della firma in questo file. "
    "⭐ E l'avviso non manca al giocatore: lo stesso testo e' vivo in "
    "`screen.hsp:6792` ed e' **gia' reso** («Attenzione! Con un bonus magia di "
    "100 o piu' non se ne ottengono altri.»). Qui non c'e' lavoro da fare, c'e' "
    "una copia spenta che gonfiava il conto di `verifica --dizionario`. "
    "✅ Si sblocca solo se qualcuno riaccende quel tratto; e allora la resa "
    "giusta e' gia' scritta e si copia da `screen.hsp`."
)

voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_97-system-tutto.jsonl',
                                                 encoding='utf-8') if l.strip())}
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
    'rinviata_a': 'mai: riga dentro un commento di blocco, e la gemella viva '
                  'e\' gia\' resa in `screen.hsp:6792`',
    'motivo': MOTIVO,
}

# ⚠️ si compone e si codifica prima di toccare il file (la 39a)
dati = (json.dumps(nuova, ensure_ascii=False) + '\n').encode('utf-8')
with io.open('rinviate.jsonl', 'ab') as f:
    f.write(dati)
print(f'rinviata aggiunta (totale {len(esistenti) + 1})')
