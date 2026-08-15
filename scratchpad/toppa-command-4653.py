# -*- coding: utf-8 -*-
"""`command.hsp:4653`-`:4655`: le tre etichette del menu del sesso, rimaste inglesi.

⚠️⚠️ Il menu del desiderio «sex» (`:4649`-`:4658`) offre sei voci, e fin qui ne
usciva **meta' in italiano**:

    promptAdd cnven(strmale), "null", 0                              -> «maschio» (toppa su text.hsp)
    promptAdd cnven(strfemale), "null", 1                            -> «femmina» (toppa su text.hsp)
    promptAdd cnven(lang("自称男性", "male?")), "null", 2             -> «male?»
    promptAdd cnven(lang("自称女性", "female?")), "null", 3           -> «female?»
    promptAdd cnven(lang("両性具有", "hermaphrodite")), "null", 4     -> «hermaphrodite»
    promptAdd cnven(lang("性別不明", "unknown")), "null", 5           -> «sconosciuto»

Le tre in mezzo restano inglesi per due motivi diversi, tutti e due giusti.

⚠️ **`male?` e `female?` sono valori di dato**: `invariati.md` li tiene inglesi
perche' finiscono in `CDATAN_NEWSEX` e tradurli romperebbe i salvataggi. Le loro
firme sono **ancorate in `text.hsp`**, e `applica.py:618` applica ogni dizionario
al **suo** file soltanto: nessuna resa di `command.hsp` puo' toccarle. Erano
irraggiungibili per costruzione.

⚠️ **`hermaphrodite` e' la stessa `lang()` che a `:4686` scrive `locvar_newsex`**,
cioe' l'etichetta e il dato sono **la stessa stringa**. Una resa la cambierebbe in
tutt'e due i posti. La voce e' percio' **rinviata** (lotto 029).

✅ Questa toppa tocca solo le tre righe `promptAdd`, che sono **visualizzazione e
basta**, e lascia intatti gli assegnamenti di `:4678`, `:4682` e `:4686`. E' la
strada che `text.hsp` batte gia' con sei toppe della stessa specie: la' e' il
sito che **stampa** il valore, qui e' il sito che lo **offre in un menu**.

💡 La regola generale: quando una `lang()` serve **due volte con due mestieri
diversi** — etichetta e dato — il dizionario segue il mestiere piu' severo, e
l'altro si sistema con una toppa sul solo sito di visualizzazione.

⚠️ **Quel che questa toppa NON fa.** `text.hsp:359` confronta `CDATAN_NEWSEX` con
«hermaphorodite», che e' un **refuso di monte**: la grafia salvata e'
«hermaphrodite». Quel ramo e' morto anche in inglese, quindi chi sceglie
l'ermafrodito si vede la stringa grezza sulla scheda. Aggiustarlo vorrebbe dire
**rendere vivo un ramo che oggi non gira**, ed e' un cambio di comportamento che
vuole un collaudo a schermo. Sta scritto nella ripresa.

⚠️ Il tetto: `val = promptx, prompty, 200, 1`, cioe' 200 pixel — con la misura di
`larghezze.py` sono **20 caratteri**. «ermafrodito» ne prende 11, «maschio?» 8.

⚠️ Sostituzione 1:1 sulle righe; i rami giapponesi restano intatti.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\command.hsp'
NOME = 'command.hsp'
DA, A = 4653, 4655

CAMBI = [
    ('"male?"', '"maschio?"'),
    ('"female?"', '"femmina?"'),
    ('"hermaphrodite"', '"ermafrodito"'),
]

MOTIVO = (
    "command.hsp:4653-:4655, le tre etichette del menu del sesso (il desiderio "
    "«sex»). Restavano inglesi in un menu che per il resto e' italiano — `strmale` "
    "e `strfemale` arrivano gia' toppati da `text.hsp`, 「性別不明」 e' reso "
    "«sconosciuto» — e per due motivi diversi, tutti e due giusti. "
    "⚠️ `male?` e `female?` sono **valori di dato** (`invariati.md`): finiscono in "
    "`CDATAN_NEWSEX` e tradurli romperebbe i salvataggi. Le loro firme sono ancorate "
    "in `text.hsp`, e `applica.py:618` applica ogni dizionario al suo file soltanto: "
    "nessuna resa di `command.hsp` poteva raggiungerle. "
    "⚠️ `hermaphrodite` e' la **stessa `lang()`** che a `:4686` scrive "
    "`locvar_newsex`: etichetta e dato sono la stessa stringa, quindi la voce e' "
    "rinviata (lotto 029). "
    "✅ La toppa tocca solo le tre righe `promptAdd`, che sono visualizzazione e "
    "basta, e lascia intatti gli assegnamenti di `:4678`, `:4682` e `:4686`. E' la "
    "stessa specie delle sei toppe su `text.hsp`: la' il sito che stampa il valore, "
    "qui il sito che lo offre in un menu. "
    "💡 Quando una `lang()` serve due volte con due mestieri diversi — etichetta e "
    "dato — il dizionario segue il mestiere piu' severo e l'altro si toppa. "
    "⚠️ Tetto 200 px, cioe' 20 caratteri: «ermafrodito» ne prende 11. "
    "⚠️ Sostituzione 1:1 sulle righe."
)

righe = io.open(SORGENTE, encoding='cp932').read().split('\n')
CERCA = righe[DA - 1:A]

if len(CERCA) != len(CAMBI):
    raise SystemExit('il blocco non ha tre righe')

METTI = []
for riga, (vecchio, nuovo) in zip(CERCA, CAMBI):
    if vecchio not in riga or 'promptAdd' not in riga:
        raise SystemExit(f'riga inattesa: {riga.strip()[:120]}')
    METTI.append(riga.replace(vecchio, nuovo))

quante = sum(1 for i in range(len(righe) - len(CERCA) + 1)
             if righe[i:i + len(CERCA)] == CERCA)
if quante != 1:
    raise SystemExit(f'il blocco compare {quante} volte, non una: toppa ambigua')

nuova_toppa = {'file': NOME, 'cerca': CERCA, 'sostituisci': METTI, 'motivo': MOTIVO}

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
    for prima, dopo in zip(CERCA, METTI):
        print(f'  - {prima.strip()}')
        print(f'  + {dopo.strip()}')

# --- il rinvio di :4655, che e' l'altra meta' ------------------------------
CHIAVE = (4655, 'hermaphrodite')
voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_command.jsonl', encoding='utf-8') if l.strip())}
if CHIAVE not in voci:
    raise SystemExit(f'chiave che non aggancia nessuna voce: {CHIAVE}')
v = voci[CHIAVE]
rinviata = {
    'firma': v['firma'],
    'file': NOME,
    'en': v['en'],
    'rinviata_a': 'mai: e\' un valore di CDATAN_NEWSEX, e a schermo ci arriva per toppa',
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
