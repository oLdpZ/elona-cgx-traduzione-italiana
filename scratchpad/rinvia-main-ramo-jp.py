# -*- coding: utf-8 -*-
"""Rinvia le nove `lang()` di `main.hsp:874`-`:898`, chiuse nel ramo `if ( jp )`.

E' la finestra di aiuto ai comandi che si apre all'avvio: `:871` e' un
`if ( jp ) {` e tutto quel che c'e' dentro **l'italiano non lo vede mai**.

⭐ **La prova che non e' testo la da' anche l'inglese**: tutte e nove le righe
hanno lo stesso secondo argomento, `"Essential is normal mode."` — un
segnaposto ripetuto nove volte, che con quel che c'e' scritto sopra non
c'entra niente. Chi ha portato il gioco in inglese ha lasciato la finestra
giapponese dov'era e non ha nemmeno provato a tradurla.

⚠️ E il giapponese e' fatto di **tasti**: 「q:quaff(飲む)　w:wear(装備)」. Anche
volendo, tradurre le glosse fra parentesi non servirebbe a nessuno, perche' la
finestra non si apre.

💡 **A fermare il lavoro e' stato un referto d'apertura**, non l'occhio:
`scratchpad/lang-nel-ramo-jp.py` contava «21 righe, 0 gia' tradotte», e nove di
quelle ventuno sono queste. Tradurle avrebbe fatto salire la spia da 0 a 9 —
cioe' avrebbe rotto proprio la misura che serve a non fare questo errore. E'
la stessa spia che nella 57a aveva costretto a rinviare `item_func.hsp:2581`.

La forma segue la regola della 39a: si compone tutto in memoria, si codifica, e
solo allora si apre il file in scrittura.
"""
import io
import json
import re

FILE = 'main.hsp'
RIGHE = (874, 877, 880, 883, 886, 889, 892, 895, 898)
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\main.hsp'

MOTIVO = (
    "La `lang()` sta dentro il ramo `if ( jp )` di `main.hsp:871`, cioe' nella "
    "finestra di aiuto ai comandi che si apre **solo in giapponese**: in "
    "italiano quel ramo non si percorre mai e la riga non arriva a schermo. "
    "⭐ Lo conferma l'inglese, che per tutte e nove le righe e' lo stesso "
    "segnaposto — «Essential is normal mode.» — senza rapporto con quel che il "
    "giapponese scrive: chi ha portato il gioco in inglese ha lasciato la "
    "finestra dov'era. ⚠️ E il contenuto sono **tasti** (`q:quaff(飲む)`), non "
    "prosa. Trovate da `scratchpad/lang-nel-ramo-jp.py`, la spia che vale zero."
)

# --- le voci non sono nel dizionario: e' un rinvio prima della traduzione ---

percorso_diz = f'dizionario/{FILE}.jsonl'
voci_diz = [json.loads(l) for l in io.open(percorso_diz, encoding='utf-8').read().splitlines()
            if l.strip()]
gia = [v for v in voci_diz if v['riga'] in RIGHE]
if gia:
    raise SystemExit(f'{len(gia)} di queste voci sono gia\' nel dizionario: '
                     f'il rinvio va scritto come quello di item_func:2581')

# --- e stanno davvero dentro un `if ( jp )` --------------------------------

righe_sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')
apertura = None
for i in range(RIGHE[0] - 2, max(0, RIGHE[0] - 12), -1):
    if re.match(r'^\s*if\s*\(\s*jp\s*\)\s*\{', righe_sorgente[i]):
        apertura = i + 1
        break
if apertura is None:
    raise SystemExit(f'nessun `if ( jp )` sopra la riga {RIGHE[0]}: fermo tutto')
print(f'ramo `if ( jp )` aperto a :{apertura}')

# --- l'inglese e' lo stesso segnaposto per tutte e nove --------------------

SEGNAPOSTO = 'Essential is normal mode.'
voci_estratte = {v['riga']: v for v in
                 (json.loads(l) for l in io.open('lavoro/_main.jsonl', encoding='utf-8')
                  if l.strip())
                 if v['riga'] in RIGHE}
mancanti = [r for r in RIGHE if r not in voci_estratte]
if mancanti:
    raise SystemExit(f'righe non presenti nell\'estrazione: {mancanti}')
diversi = {r: v['en'] for r, v in voci_estratte.items() if v['en'] != SEGNAPOSTO}
if diversi:
    raise SystemExit(f'l\'inglese non e\' il segnaposto atteso: {diversi}')
print(f'tutte e {len(RIGHE)} hanno lo stesso inglese: {SEGNAPOSTO!r}')

# --- il rinvio non c'e' gia' -----------------------------------------------

righe_rin = [l for l in io.open('rinviate.jsonl', encoding='utf-8').read().splitlines()
             if l.strip()]
firme_rin = {json.loads(l)['firma'] for l in righe_rin}
da_scrivere = [v for r, v in sorted(voci_estratte.items()) if v['firma'] not in firme_rin]
if not da_scrivere:
    raise SystemExit('rinvii gia\' presenti: niente da fare')

# --- si compone tutto, e solo allora si scrive ------------------------------

rin_nuovo = righe_rin + [json.dumps({
    'firma': v['firma'],
    'file': FILE,
    'en': v['en'],
    'rinviata_a': 'nessuna fase: la lang() sta nel ramo `if ( jp )`',
    'motivo': MOTIVO,
}, ensure_ascii=False) for v in da_scrivere]

dati = ('\n'.join(rin_nuovo) + '\n').encode('utf-8')
with io.open('rinviate.jsonl', 'wb') as f:
    f.write(dati)

print(f'rinviate.jsonl: {len(righe_rin)} -> {len(rin_nuovo)}')
