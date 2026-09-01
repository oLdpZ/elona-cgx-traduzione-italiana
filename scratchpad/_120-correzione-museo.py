# -*- coding: utf-8 -*-
"""Toglie l'accordo al maschile da `db_item.hsp:96060`, l'atto del museo.

La 119a ha reso «...mostrare al pubblico la collezione **che ti sei fatto da
solo**...». Participio e aggettivo concordano al maschile in una riga rivolta
al giocatore, che puo' essere femmina: e' esattamente il difetto che
`scratchpad/referti.py` cerca, e infatti in apertura della 120a quel referto
leggeva **10** invece di 9. Gli altri nove stanno in `chat.hsp` e sono gia'
giudicati.

⚠️ La 119a lo ha chiuso scrivendo «`referti` fermo a 9»: la misura era stata
presa **prima** delle rese dei lotti 051-052. E' la forma della 112a — una
catena verde misurata su un albero che non e' quello finale.

Il giapponese non ha il problema: 自分で集めた収集品 e' «i pezzi raccolti da
se'», e il participio si appoggia alla collezione, non a chi la possiede. La
resa nuova fa lo stesso — «la collezione raccolta di persona» — e in piu'
recupera 一手に («tutta in una volta», in esclusiva), che la resa vecchia
lasciava cadere.

⚠️ La riga gemella e' `:95990`, l'atto del **negozio**, ed e' quella da cui
l'inglese di questa ha ricopiato «shop» (119a). Non si tocca: il suo italiano
dice gia' «negozio», e non ha accordi col giocatore.

Lo script e' ripetibile: se la voce e' gia' corretta, si salta.
"""
import io, json

RIGA = 96060
VECCHIA = ('Un atto che dà il diritto di costruire un museo. Lo stipendio che '
           'passa lo Stato è una miseria, ma mostrare al pubblico la collezione '
           'che ti sei fatto da solo è la gioia più grande per chi colleziona. '
           '\\n# ~Immobiliare Derphy: Catalogo~')
NUOVA = ('Un atto che dà il diritto di costruire un museo. Lo stipendio che '
         'passa lo Stato è una miseria, ma esporre al pubblico, tutta in una '
         'volta, la collezione raccolta di persona è la gioia più grande per '
         'chi colleziona. \\n# ~Immobiliare Derphy: Catalogo~')

P = 'dizionario/db_item.hsp.jsonl'
righe = [json.loads(l) for l in io.open(P, encoding='utf-8') if l.strip()]

# rete 1: nessun'altra voce del file porta lo stesso accordo. Se ce ne fossero,
# correggerne una sola lascerebbe `referti` a 10 e sembrerebbe che la
# correzione non abbia agganciato.
altre = [d['riga'] for d in righe
         if d['riga'] != RIGA and 'ti sei fatto' in (d.get('it') or '')]
if altre:
    raise SystemExit(f'rete 1: altre voci con lo stesso accordo -> {altre}')

# rete 2: la coda della fonte non cambia. E' la riga che `_112-corpo-descrizioni`
# e `_116-code-discordi` leggono, e spostarla muoverebbe due referti per sbaglio.
if VECCHIA.split('\\n')[-1] != NUOVA.split('\\n')[-1]:
    raise SystemExit('rete 2: la coda della fonte e\' cambiata')

fatte, saltate, viste = 0, 0, 0
for d in righe:
    if d['riga'] != RIGA:
        continue
    viste += 1
    if d.get('it') == NUOVA:
        saltate += 1
        continue
    # rete 3: si corregge solo la resa che ci si aspetta di trovare
    if d.get('it') != VECCHIA:
        raise SystemExit(f'rete 3: :{RIGA} non porta la resa attesa, ma\n'
                         f'  {d.get("it")!r}')
    if d.get('oggetto') != 'ITEM_ID_DEED_MUSEUM':
        raise SystemExit(f'rete 3b: :{RIGA} non e\' l\'atto del museo, '
                         f'ma {d.get("oggetto")!r}')
    print(f'{RIGA}  {d["oggetto"]}')
    print(f'  prima : ...{VECCHIA[95:160]}...')
    print(f'  dopo  : ...{NUOVA[95:165]}...')
    d['it'] = NUOVA
    fatte += 1

# rete 4: la voce dev'essere stata trovata, una e una sola volta
if viste != 1:
    raise SystemExit(f'rete 4: :{RIGA} trovata {viste} volte, attesa 1')

if fatte:
    with io.open(P, 'w', encoding='utf-8', newline='\n') as f:
        for d in righe:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')

print(f'--- {fatte} corretta, {saltate} gia\' a posto, in {P}')
print('    ora `python scratchpad/referti.py` deve dire «participi: 9»')
