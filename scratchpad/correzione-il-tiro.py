# -*- coding: utf-8 -*-
"""`text.hsp:2503`: le due voci del menu «Mano o Tiro?» non si accordavano.

⚠️ **Trovata nel collaudo della 49ª**, cercando dove si legge « (tiro)». Quando
si equipaggia con `w` un'arma che puo' stare in **due** slot, `command.hsp:15307`
chiede quale, e `txtsetequipw` (`text.hsp:2498`-`:2505`) offre le due voci:

    :2500   lang("手",   "la mano")     <- con l'articolo
    :2503   lang("遠隔", "tiro")        <- senza

L'inglese le ha tutte e due nude — `"hand"` e `"range"` — quindi non poteva far
da guida. In italiano una delle due ha preso l'articolo e l'altra no, e si
leggono **una sotto l'altra** in un riquadro da 150 px.

⚠️⚠️ **E la strada ovvia era chiusa.** Le due voci sembrano gli slot «Mano» e
«Tiro» di `bodyn` (`text.hsp:136`), che e' anche come le nomina la domanda
appena sopra — «e' equipaggiamento da **Tiro**… si puo' portare anche in
**Mano**». Ma `:2500` **non si puo' toccare**: la sua firma (`jp=手`, `en=hand`)
e' la stessa di `_melee(0, 0)` e `_melee(0, 6)` (`text.hsp:161` e `:167`), dove
«la mano» e' la parte del corpo delle frasi d'attacco — la famiglia di
«l'artiglio», «la gamba», «la zanna», «il ramo». Una resa sola per tre siti, e
li' l'articolo serve.

💡 **Ne' si poteva toppare `:2500`.** Una toppa aggancia il **sorgente pinnato**
(`test_toppe.py:104`), e quella riga il dizionario la riscrive prima che le
toppe girino; per liberarla servirebbe un rinvio, ma il rinvio e' **per firma** e
si porterebbe dietro anche i due `_melee`. E quelle due righe hanno tre `lang()`
ciascuna, quindi nemmeno una toppa di riga le puo' sistemare — «una toppa e una
resa non stanno sulla stessa riga».

✅ **Quindi si accorda l'altra**, che ha firma **unica** (`jp=遠隔`, `en=range`,
usata solo a `:2503`; il 「遠隔」 di `bodyn` a `:136` sta con `en=Shoot` ed e'
un'altra firma). «Quale scegli?» → «la mano» / «il tiro»: sette caratteri
ciascuna, dentro i 150 px, e con lo stesso registro.

💡 La lezione: quando due voci di un menu non si accordano, si guarda **quale
delle due e' libera** prima di decidere in che direzione accordarle.

⚠️ Lo script compone e valida tutto in memoria prima di aprire un file in
scrittura, come `correzione-schivata.py`.
"""
import io
import json
import sys

CORREZIONI = {
    'dizionario/text.hsp.jsonl': {
        2503: ('tiro', 'il tiro'),
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
        # ⚠️ rete 0: la riga 2503 ha una voce sola, ma il file ne ha altre con
        #    lo stesso numero se il sito ne porta piu' d'una: si filtra sull'en.
        if d.get('en') != 'range':
            continue
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

# rete 3: la firma dev'essere davvero UNICA, o la resa nuova finisce altrove
for d in corrette:
    gemelle = [json.loads(l) for l in io.open('dizionario/text.hsp.jsonl', encoding='utf-8')
               if l.strip() and json.loads(l)['firma'] == d['firma']]
    if len(gemelle) != 1:
        sys.exit(f"rete 3: la firma di :{d['riga']} ha {len(gemelle)} voci, non una")
print('rete 3: firma unica')

# rete 4: le rese nuove devono passare `verifica` come se fossero un lotto
if corrette:
    from strumenti.verifica import controlla_lotto
    problemi = controlla_lotto(corrette)
    if problemi:
        for chiave, elenco in problemi.items():
            print(f'rete 4: {chiave}: ' + '; '.join(elenco))
        sys.exit('le rese nuove non passano verifica')
    print(f'rete 4: {len(corrette)} rese nuove passano verifica')

for percorso, dati in da_scrivere.items():
    with io.open(percorso, 'wb') as f:
        f.write(dati)

print(f"--- {fatte} rese corrette, {saltate} gia' a posto")
