# -*- coding: utf-8 -*-
"""`command.hsp:17435` diceva « piano» e va detto « liv.», per via del numero.

La riga e' `promptAdd mapname(i) + " " + cnvrank(...) + lang("階", " Lv")`, cioe'
la lista dei luoghi dove si puo' tornare: «Palmia 5 Lv». Il lotto `command-022`
l'aveva resa « piano» — che e' quel che dice il giapponese 「階」 — e a schermo
sarebbe uscito «**Palmia 5 piano**».

⚠️ **Il numero non e' un ordinale, e in italiano non lo diventa.** «5° piano»
vorrebbe il grado, e il grado in CP932 e' un carattere a **doppia larghezza** che
`scratchpad/guardie.py` vieta. «5 piani» sarebbe giusto al plurale e sbagliato a
1. ✅ **« liv.»** e' invariabile e regge tutt'e due: «Palmia 1 liv.», «Palmia 5
liv.». E' la stessa manovra di «Schiv.» e «Prot.» della 43ª — la resa distesa
tagliata dove il sito la taglia — con in piu' il fatto che qui a tagliare non e'
la larghezza ma la **grammatica**.

💡 Va insieme a `scratchpad/toppa-init-cnvrank.py`: senza quella, `cnvrank`
restituisce «5th» e la riga direbbe «Palmia 5th liv.».
"""
import io
import json
import sys

CORREZIONI = {
    'dizionario/command.hsp.jsonl': {
        17435: (' piano', ' liv.'),
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
        print(f"{percorso.split('/')[-1]}:{d['riga']}\n    {d['it']!r}\n -> {nuova!r}")
        d['it'] = nuova
        corrette.append(dict(d))
        fatte += 1
    # rete 2: nessuna correzione deve restare senza voce
    if viste != set(correzioni):
        sys.exit(f'rete 2: correzioni senza voce -> {sorted(set(correzioni) - viste)}')
    # ⚠️ si compone e si codifica PRIMA di aprire il file in scrittura
    da_scrivere[percorso] = ''.join(
        json.dumps(d, ensure_ascii=False) + '\n' for d in righe).encode('utf-8')

# rete 3: le rese nuove devono passare `verifica` come se fossero un lotto
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
