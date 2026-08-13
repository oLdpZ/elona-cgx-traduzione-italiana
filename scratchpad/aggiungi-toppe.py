# -*- coding: utf-8 -*-
"""Aggiunge a toppe.jsonl le toppe di un file, senza duplicare.

L'identita' di una toppa e' (file, cerca): due toppe con lo stesso `cerca` sullo
stesso file si escluderebbero a vicenda, e `applica` si fermerebbe sulla seconda
dicendo che il blocco «non esiste piu'» — perche' la prima l'ha gia' cambiato.
"""
import io, json, sys

NUOVE = sys.argv[1]

def chiave(t):
    cerca = t['cerca']
    return (t['file'], tuple(cerca) if isinstance(cerca, list) else (cerca,))

esistenti = [json.loads(l) for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]
viste = {chiave(t) for t in esistenti}

nuove = [json.loads(l) for l in io.open(NUOVE, encoding='utf-8') if l.strip()]
da_aggiungere = [t for t in nuove if chiave(t) not in viste]
gia = len(nuove) - len(da_aggiungere)

# e nessuna delle nuove deve collidere con un'altra delle nuove
fra_loro = {}
for t in da_aggiungere:
    k = chiave(t)
    if k in fra_loro:
        raise SystemExit(f'due toppe nuove con lo stesso cerca: {k}')
    fra_loro[k] = t

if da_aggiungere:
    with io.open('toppe.jsonl', 'a', encoding='utf-8', newline='\n') as f:
        for t in da_aggiungere:
            f.write(json.dumps(t, ensure_ascii=False) + '\n')
print(f'{len(da_aggiungere)} toppe aggiunte, {gia} gia presenti, '
      f'totale {len(esistenti) + len(da_aggiungere)}')
