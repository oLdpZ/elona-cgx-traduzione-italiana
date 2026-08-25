# -*- coding: utf-8 -*-
"""96a - Rinvia le nove parti del corpo di `item_func.hsp`, spente nel ramo `jp`.

`:1036`-`:1060` rendono i nove pezzi di cadavere che la negromanzia stacca —
あたま, くび, せなか, どうたい, て, ゆび, うで, こし, あし — e sono
`lang("あたま", "head")` e fratelli, cioe' `lang()` vere, con un inglese vero.

⚠️ Ma stanno dentro `if ( inv(INV_ITEM_ID, …) == ITEM_ID_NECRO_PARTS & jp ) {`
(`:1034`), e quel `& jp` le spegne: quando il gioco non e' in giapponese il
blocco non si esegue, il secondo argomento di `lang()` non arriva a schermo
nemmeno una volta, e l'italiano che ci mettessimo non lo leggerebbe nessuno.

E' la stessa famiglia di `rinvia-command-ramo-jp.py` e `rinvia-main-ramo-jp.py`,
e la terza forma di riga morta accanto al `;` e al `/* … */`: **la riga e' viva,
il file e' vivo, la `lang()` e' vera — a spegnerla e' il ramo della lingua.**

⭐ A trovarle e' stata `scratchpad/_96-rami-jp.py`, scritta oggi: nessuna rete
del progetto misurava chi **accende** una stringa, e `verifica`, `estrai` e la
prova d'identita' guardano la riga, non chi la raggiunge. Sul resto del file la
rete dice zero, quindi queste nove sono tutte.

⚠️ Nessuna delle nove e' mai stata tradotta: il rinvio le toglie dalla coda, non
dal dizionario.

💡 Se un giorno si volesse dare un ramo inglese a quel blocco — cioe' far
uscire «testa», «collo», «schiena» anche fuori dal giapponese — sarebbe una
**toppa**, non una resa: qui non c'e' niente da tradurre, c'e' del codice da
scrivere. E allora tornerebbero, con le parti del corpo gia' decise altrove.
"""
import io
import json

FILE = 'item_func.hsp'
RIGHE = (1036, 1039, 1042, 1045, 1048, 1051, 1054, 1057, 1060)

MOTIVO = (
    "Una delle nove parti del corpo staccate dalla negromanzia "
    "(`item_func.hsp:1036`-`:1060`). La `lang()` e' vera e l'inglese c'e' "
    "(«head», «neck», «back»…), ma il blocco che la contiene e' guardato da "
    "`if ( inv(INV_ITEM_ID, itemowner_itemid) == ITEM_ID_NECRO_PARTS & jp ) {` "
    "(`:1034`): il `& jp` lo spegne in ogni lingua che non sia il giapponese, e "
    "il secondo argomento non arriva a schermo nemmeno una volta. "
    "⚠️ E' la terza famiglia di riga morta oltre al `;` e al `/* … */` — la "
    "riga e' viva, a spegnerla e' il **ramo della lingua** — ed e' la stessa di "
    "`rinvia-command-ramo-jp.py` e `rinvia-main-ramo-jp.py`. Trovata dalla rete "
    "nuova `scratchpad/_96-rami-jp.py` (96a), che misura chi **accende** una "
    "stringa: `verifica`, `estrai` e la prova d'identita' guardano la riga, non "
    "chi la raggiunge. 💡 Darle un ramo inglese sarebbe una **toppa**, non una "
    "resa: qui non c'e' niente da tradurre, c'e' del codice da scrivere."
)

voci = [json.loads(l) for l in io.open('lavoro/_item_func.jsonl', encoding='utf-8')
        if l.strip()]
per_riga = {}
for v in voci:
    per_riga.setdefault(v['riga'], []).append(v)

bersagli = []
for riga in RIGHE:
    trovate = per_riga.get(riga, [])
    if len(trovate) != 1:
        raise SystemExit(f'attesa 1 voce a :{riga}, trovate {len(trovate)}')
    bersagli.append(trovate[0])

diz = {json.loads(l)['firma'] for l in io.open(f'dizionario/{FILE}.jsonl', encoding='utf-8')
       if l.strip()}
gia_rese = [v['riga'] for v in bersagli if v['firma'] in diz]
if gia_rese:
    raise SystemExit(f'queste sono gia\' nel dizionario, il rinvio le perderebbe: {gia_rese}')

righe_rin = [l for l in io.open('rinviate.jsonl', encoding='utf-8').read().splitlines()
             if l.strip()]
firme_rin = {json.loads(l)['firma'] for l in righe_rin}
nuove = [v for v in bersagli if v['firma'] not in firme_rin]
if not nuove:
    raise SystemExit('rinvii gia\' presenti: niente da fare')

rin_nuovo = righe_rin + [
    json.dumps({
        'firma': v['firma'],
        'file': FILE,
        'en': v['en'],
        'rinviata_a': "nessuna fase: la lang() sta in un ramo `& jp`",
        'motivo': MOTIVO,
    }, ensure_ascii=False)
    for v in nuove
]

with io.open('rinviate.jsonl', 'wb') as f:
    f.write(('\n'.join(rin_nuovo) + '\n').encode('utf-8'))

print('rinviate.jsonl: %d -> %d' % (len(righe_rin), len(rin_nuovo)))
