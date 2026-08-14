# -*- coding: utf-8 -*-
"""«ha di nuovo il mana pieno» non e' vero in nessuno dei due siti.

Trovata scrivendo il lotto 016: `proc.hsp:14597` ha lo **stesso giapponese** di
`action.hsp:1096` — 「name(tc)のマナが回復した。」, «il mana si e' ripreso» — e la
resa vecchia diceva «ha di nuovo il mana **pieno**».

⚠️ **Il codice dice che pieno non lo e' mai.** A `action.hsp:1095` la riga sopra
e' `healmp 0, inv(INV_ITEM_CHARGE, ci) * 5 * inv(INV_ITEM_NUM, ci)`, cioe' tante
unita' quante ne ha in carica la bacchetta; a `proc.hsp:14594` e'
`healmp tc, cdata(CDATA_MAX_MP, tc) / 10 + rnd(sdata(SKILL_ATTR_MAG, tc)) + 5`,
cioe' un decimo del massimo piu' un dado. Nessuno dei due riempie la barra, e il
giapponese non lo dice: 回復した e' «si e' ripreso», non «e' pieno».

E' la stessa classe della 33a — «per una riga che descrive un effetto l'arbitro
non e' una lingua, e' il codice» — su una resa che l'inglese (`mana is restored`)
non bastava a smentire.

Lo script e' ripetibile.
"""
import io
import json

CORREZIONI = {
    'dizionario/action.hsp.jsonl': {
        (1096, ' mana is restored.'): (
            'name(CHARA_PLAYER) + " ha di nuovo il mana pieno."',
            'name(CHARA_PLAYER) + " recupera mana."',
        ),
    },
}

fatte, saltate, corrette = 0, 0, []
for percorso, correzioni in CORREZIONI.items():
    righe = [json.loads(l) for l in io.open(percorso, encoding='utf-8') if l.strip()]
    viste = set()
    for d in righe:
        k = (d['riga'], d.get('en'))
        if k not in correzioni:
            continue
        vecchia, nuova = correzioni[k]
        viste.add(k)
        if d.get('it') == nuova:
            saltate += 1
            continue
        if d.get('it') != vecchia:
            raise SystemExit(f'rete 1: {percorso}{k} non dice la resa attesa ma {d.get("it")!r}')
        print(f"{percorso.split('/')[-1]}:{d['riga']}\n    {d['it']}\n -> {nuova}")
        d['it'] = nuova
        corrette.append(dict(d))
        fatte += 1
    if viste != set(correzioni):
        raise SystemExit(f'rete 2: correzioni senza voce -> {sorted(set(correzioni) - viste)}')
    with io.open(percorso, 'w', encoding='utf-8', newline='\n') as f:
        for d in righe:
            f.write(json.dumps(d, ensure_ascii=False) + '\n')

# rete 3: le rese nuove devono passare `verifica` come un lotto (vedi
# correzione-rete8.py: `verifica --dizionario` non le guarda).
if corrette:
    from strumenti.verifica import controlla_lotto
    problemi = controlla_lotto(corrette)
    if problemi:
        for chiave, elenco in problemi.items():
            print(f'rete 3: {chiave}: ' + '; '.join(elenco))
        raise SystemExit('le rese nuove non passano verifica')
    print(f'rete 3: {len(corrette)} rese nuove passano verifica')

print(f"--- {fatte} rese corrette, {saltate} gia' a posto")
