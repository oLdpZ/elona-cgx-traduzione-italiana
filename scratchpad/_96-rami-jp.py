# -*- coding: utf-8 -*-
"""96a - Chi ACCENDE la stringa: le firme spente nel ramo giapponese.

`lang(jp, en)` restituisce `en` quando il gioco non e' in giapponese, ma se il
`lang()` sta **dentro un blocco guardato da `jp`** l'italiano non esce mai.
`item_func.hsp:1034` e' cosi': `if ( ... & jp ) {` racchiude le nove parti del
corpo (`あたま`, `くび`, ...), che nel ramo inglese non si stampano.

Nessuna delle reti del progetto lo vede: `verifica`, `estrai` e la prova
d'identita' guardano la **riga**, non chi la raggiunge.

Uso:  python scratchpad/_96-rami-jp.py [file.hsp] [estrazione.jsonl]
"""
import io, json, re, sys

SORGENTE = 'C:/Games/Elona/_traduzione/sorgente/2.05-custom-gx/'

file_hsp = sys.argv[1] if len(sys.argv) > 1 else 'item_func.hsp'
lotto    = sys.argv[2] if len(sys.argv) > 2 else 'lavoro/_item_func.jsonl'

righe = io.open(SORGENTE + file_hsp, encoding='cp932').read().split('\n')

# --- lo stack dei blocchi: per ogni riga, l'elenco delle condizioni che la
#     racchiudono. HSP usa le graffe come C, e le condizioni stanno su una riga.
guardie = {}          # numero di riga (1-based) -> lista di condizioni
pila = []
ultima_cond = None

for n, riga in enumerate(righe, 1):
    nuda = re.sub(r'//.*$', '', riga)
    guardie[n] = [c for c in pila]
    aperte  = nuda.count('{')
    chiuse  = nuda.count('}')
    m = re.search(r'\bif\s*\((.*)\)\s*\{\s*$', nuda)
    if m:
        pila.append(m.group(1).strip())
        ultima_cond = m.group(1).strip()
        continue
    m = re.search(r'^\s*(\})?\s*else\s*\{\s*$', nuda)
    if m:
        # ⚠️ `} else {` chiude il blocco QUI: la condizione da negare e' quella
        #    che si toglie adesso dalla pila. Se invece la graffa stava sulla
        #    riga prima, e' gia' stata tolta ed e' in `ultima_cond`. Confondere
        #    i due casi fa negare la condizione sbagliata (il primo giro diceva
        #    `NON(PRODUCED_BOOK)` dove il sorgente dice `NON(jp)`).
        if m.group(1) and pila:
            cond = pila.pop()
        else:
            cond = ultima_cond or '?'
        pila.append('NON(' + cond + ')')
        continue
    # blocchi aperti senza `if` (repeat/loop non usano graffe, ma i deffunc si')
    for _ in range(max(0, aperte - chiuse)):
        pila.append('(blocco)')
    for _ in range(max(0, chiuse - aperte)):
        if pila:
            ultima_cond = pila.pop()

def solo_jp(conds):
    """La riga e' raggiungibile SOLO col gioco in giapponese?"""
    for c in conds:
        if c.startswith('NON('):
            continue
        if re.search(r'(^|[\s&(!])jp([\s&)]|$)', c) and '!jp' not in c and 'jp ==' not in c:
            return c
    return None

def solo_en(conds):
    for c in conds:
        if c.startswith('NON(') and re.search(r'(^|[\s&(])jp([\s&)]|$)', c):
            return c
    return None

voci = [json.loads(l) for l in io.open(lotto, encoding='utf-8') if l.strip()]
spente, inglesi = [], []
for v in voci:
    conds = guardie.get(v['riga'], [])
    g = solo_jp(conds)
    if g:
        spente.append((v, g))
    elif solo_en(conds):
        inglesi.append(v)

print('%s: %d firme da fare' % (file_hsp, len(voci)))
print()
print('SPENTE NEL RAMO GIAPPONESE (l\'italiano non esce mai): %d' % len(spente))
for v, g in spente:
    print('  %6d  %-22s | %-22s   guardia: %s'
          % (v['riga'], v['jp'][:22], v['en'][:22], g[:60]))
print()
print('dentro un ramo NON-giapponese (l\'italiano esce di sicuro): %d' % len(inglesi))
print('senza guardia di lingua: %d' % (len(voci) - len(spente) - len(inglesi)))
