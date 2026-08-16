# -*- coding: utf-8 -*-
"""`skill.hsp:1561` e' l'unica descrizione di capacita' alla terza PLURALE.

⚠️ **Trovata a schermo nel collaudo della 49ª**, aprendo il menu delle capacita'
col tasto `a`: nella colonna «Effetto» si legge «Uniscono le forze sulla
serratura», e tutte le righe intorno dicono la stessa cosa in terza **singolare**.

    :1513  Colpisce tutt'intorno/esitazione
    :1541  Attira piu' bersagli
    :1549  Legge insieme agli alleati
    :1553  Fa impazzire i nemici in vista
    :1561  Uniscono le forze sulla serratura   <- l'unica plurale
    :1589  Si potenzia

💡 **L'inglese non ha persona e non poteva far da guida**: «Join forces to break
the lock» e' una forma nuda, che in italiano puo' diventare imperativo,
infinito o terza persona. La colonna aveva gia' scelto la terza singolare
ventiquattro volte, e `:1549` («Legge insieme agli alleati») e' proprio il caso
gemello — una capacita' che coinvolge gli alleati, descritta col soggetto
singolare della capacita' stessa.

✅ La resa nuova e' anche piu' corta di due caratteri (31 invece di 33), quindi
nessun tetto puo' peggiorare.

⚠️ Lo script compone e valida tutto in memoria prima di aprire un file in
scrittura, come `correzione-schivata.py`.
"""
import io
import json
import sys

CORREZIONI = {
    'dizionario/skill.hsp.jsonl': {
        1561: (
            'Uniscono le forze sulla serratura',
            'Unisce le forze sulla serratura',
        ),
    },
}

fatte, saltate, corrette, da_scrivere = 0, 0, [], {}
for percorso, correzioni in CORREZIONI.items():
    righe = [json.loads(l) for l in io.open(percorso, encoding='utf-8') if l.strip()]
    viste = set()
    for d in righe:
        if d['riga'] not in correzioni:
            continue
        vecchia, nuova = correzioni[d['riga']]
        viste.add(d['riga'])
        if d.get('it') == nuova:
            saltate += 1
            continue
        # rete 1: si corregge solo quello che dice ancora la resa vecchia
        if d.get('it') != vecchia:
            sys.exit(f"rete 1: {percorso}:{d['riga']} non dice la resa attesa "
                     f"ma {d.get('it')!r}")
        print(f"{percorso.split('/')[-1]}:{d['riga']}\n    {d['it']}\n -> {nuova}")
        d['it'] = nuova
        corrette.append(dict(d))
        fatte += 1
    # rete 2: nessuna correzione deve restare senza voce
    if viste != set(correzioni):
        sys.exit(f'rete 2: correzioni senza voce -> {sorted(set(correzioni) - viste)}')
    # ⚠️ si compone e si codifica PRIMA di aprire il file in scrittura
    da_scrivere[percorso] = ''.join(
        json.dumps(d, ensure_ascii=False) + '\n' for d in righe).encode('utf-8')

# rete 3: le rese nuove devono passare `verifica` come se fossero un lotto.
# ⚠️ `verifica --dizionario` NON le guarda.
if corrette:
    from strumenti.verifica import controlla_lotto
    problemi = controlla_lotto(corrette)
    if problemi:
        for chiave, elenco in problemi.items():
            print(f'rete 3: {chiave}: ' + '; '.join(elenco))
        sys.exit('le rese nuove non passano verifica')
    print(f'rete 3: {len(corrette)} rese nuove passano verifica')

for percorso, dati in da_scrivere.items():
    with io.open(percorso, 'wb') as f:
        f.write(dati)

print(f"--- {fatte} rese corrette, {saltate} gia' a posto")
