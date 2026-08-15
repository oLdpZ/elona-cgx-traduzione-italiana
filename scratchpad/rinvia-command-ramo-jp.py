# -*- coding: utf-8 -*-
"""Aggiunge a rinviate.jsonl le sette `lang()` chiuse nel ramo `if ( jp )` del
diario delle statistiche (`command.hsp:2954`-`:3021`).

E' una famiglia nuova di riga morta, la terza dopo il `;` e il `/* ... */`: la
riga e' viva, il file e' vivo, la `lang()` e' vera — non gira mai il **ramo**.
"""
import io
import json

MOTIVO = (
    "La riga sta dentro il ramo `if ( jp )` di `command.hsp:2954`-`:3021`, cioe' "
    "le statistiche dell'avventura che il diario stampa solo in giapponese. Il "
    "ramo `else` (`:3022`) stampa le stesse cifre **in inglese nudo**, dentro un "
    "blocco `ANNA CUSTOM` e fuori da ogni `lang()`: «Your stats so far:», "
    "«@BL   Deepest Lvl : », «@BL   Miles Traveled: ». Chi gioca in italiano "
    "legge quelle, e questa `lang()` non viene valutata mai. "
    "⚠️ **E' una famiglia nuova di riga morta**, la terza dopo la riga commentata "
    "col `;` e il blocco `/* ... */`: qui la riga e' viva, il file e' vivo, la "
    "`lang()` e' vera — e' il **ramo della lingua** a non girare. La rete 6 non "
    "la vede, `commenti-blocco.py` nemmeno, e nessun conteggio di «non tradotte» "
    "la distingue dal lavoro utile. "
    "💡 `else_jp.py` guarda lo stesso costrutto dall'altro lato — l'inglese nudo "
    "dentro l'`else` — e il rovescio non lo cercava nessuno. "
    "✅ Si sblocca il giorno in cui qualcuno **traduce il ramo `else`**, che e' "
    "lavoro da toppa e non da dizionario; allora queste sette non serviranno "
    "comunque, perche' il testo giusto sara' quello."
)

NUOVE = [
    # il primo blocco, `cfg_record >= 1` (la zona 2000-2999)
    (2956, ' level'),
    (2962, ' Miles'),
    (2970, ' Hours'),
    (2971, ' Days'),
    (2976, ' Guest'),
    (2982, ' Plat'),
    (2986, ' points'),
    # ⭐ le quattro gemelle del blocco `cfg_record == 2` (`:2991`-`:3019`), che
    #    stanno nella zona dopo e le ha trovate `lang-nel-ramo-jp.py`: sono
    #    dentro lo stesso `if ( jp )`, annidate un livello piu' giu'. Rinviate
    #    subito invece di aspettare che qualcuno apra la zona 3000-3999 e le
    #    ritrovi da capo.
    (3003, ' Sisters'),
    (3014, ' trees'),
    (3015, ' Peoples'),
    (3016, ' bottles'),
]

# ⚠️ **l'estrazione INTERA, non quella `--da-tradurre`**: appena la prima
# tornata di rinvii entra in `rinviate.jsonl`, quelle voci spariscono dal lavoro
# che resta, e rilanciare questo script contro `lavoro/_command.jsonl` muore con
# «chiave che non aggancia nessuna voce» su una riga che aveva appena rinviato
# lui. Si rigenera con:
#     python -m strumenti.estrai command.hsp --uscita lavoro/_command_tutto.jsonl
voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_command_tutto.jsonl', encoding='utf-8')
                  if l.strip())}

righe = []
for riga, en in NUOVE:
    if (riga, en) not in voci:
        raise SystemExit(f'chiave che non aggancia nessuna voce: {(riga, en)}')
    v = voci[(riga, en)]
    righe.append({
        'firma': v['firma'],
        'file': 'command.hsp',
        'en': v['en'],
        'rinviata_a': 'mai: `lang()` dentro il ramo `if ( jp )`, che in italiano non gira',
        'motivo': MOTIVO,
    })

esistenti = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
firme = {json.loads(l)['firma'] for l in esistenti}
nuove = [r for r in righe if r['firma'] not in firme]
if not nuove:
    print('gia presenti, niente da fare')
else:
    # ⚠️ si compone e si codifica prima di toccare il file (la 39a)
    dati = ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in nuove).encode('utf-8')
    with io.open('rinviate.jsonl', 'ab') as f:
        f.write(dati)
    print(f'{len(nuove)} rinviate aggiunte (totale {len(esistenti) + len(nuove)})')
