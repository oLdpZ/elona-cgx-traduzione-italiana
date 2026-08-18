# -*- coding: utf-8 -*-
"""Le tre guardie che `verifica` non fa, sul JSONL del lotto."""
import io, json, re, sys

LOTTO = sys.argv[1]
PROIBITI = '…“”～«»'
INGLESI = re.compile(r'\b(the|you|your|is|was|are|my|his|her|and|of|with|for|by|to|'
                     r'increases?|enhances?|reduces?|damage|chance|attack|speed|'
                     r'resist|when|each|turn|equipment|skill|skills)\b', re.I)

voci = [json.loads(l) for l in io.open(LOTTO, encoding='utf-8') if l.strip()]
p1 = p2 = p3 = 0
for v in voci:
    it = v['it']
    # 1. nessun carattere a doppia larghezza tranne ♪
    doppi = [c for c in it if c != '♪' and len(c.encode('cp932', 'ignore')) > 1]
    if doppi:
        print(f"DOPPIA LARGHEZZA riga {v['riga']}: {doppi} in {it!r}")
        p1 += 1
    # 2. nessuno dei proibiti
    vietati = [c for c in it if c in PROIBITI]
    if vietati:
        print(f"PROIBITO riga {v['riga']}: {vietati} in {it!r}")
        p2 += 1
    # 3. nessuna parola inglese residua nelle statiche
    #
    # ⚠️ `FOR` **maiuscolo** e' la sigla italiana di Forza (`text.hsp:61`, la
    #    fila FOR COS DES PER APP VOL MAG CAR), non la preposizione inglese: si
    #    legge in ogni marcatore di statistica, tipo `[FOR+3]`. Senza questa
    #    esclusione la guardia gridava sei volte su un lotto solo di `trait.hsp`,
    #    e una guardia che grida sempre non la guarda piu' nessuno. L'inglese
    #    vero scrive `for` minuscolo, che resta agganciato.
    if v['tipo'] != 'dinamica':
        m = INGLESI.findall(re.sub(r'\bFOR\b', '', it))
        if m:
            print(f"INGLESE riga {v['riga']}: {m} in {it!r}")
            p3 += 1
print(f'doppia larghezza: {p1} | proibiti: {p2} | inglese residuo: {p3}')
