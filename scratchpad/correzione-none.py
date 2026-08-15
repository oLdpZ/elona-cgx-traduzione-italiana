# -*- coding: utf-8 -*-
"""`text.hsp:49` lasciava «none» in inglese, e si legge nella lista degli avventurieri.

⚠️ **Trovata dalla RETE 3 del lotto `command-009`**, non a schermo e non da un
referto. Traducendo 「なし」 di `command.hsp:1445` la rete ha detto che lo stesso
giapponese era gia' reso altrove in due modi diversi — «Nessuna» a
`init.hsp:371` e **«none»** a `text.hsp:49` — e il secondo non e' una resa: e'
l'inglese rimasto li'.

💡 **Non era un invariato.** `invariati.md:437` dichiara «none» invariato, ma per
un'altra cosa: e' uno dei nove valori di `CDATAN_NEWSEX`, scritti nel
salvataggio e riletti come operandi di confronto (la 41a, punto 3). Qui la
stringa e' la stessa e il sito e' un altro — `_dengon`, il messaggio che un
avventuriero ti ha lasciato — e li' non c'e' niente da preservare.
⚠️ **E' la trappola di `invariati.md` al contrario**: una voce dichiarata
invariata per un sito puo' far sembrare voluta la stessa stringa in un sito
dove e' solo una dimenticanza. La dichiarazione vale per il **sito**, non per
la stringa.

⚠️ **Si legge, e accanto ha cinque parole italiane.** `command.hsp:4247` fa
`_dengon(dengon) + "(" + _impression(...) + ")"` nella lista degli avventurieri,
e gli altri cinque valori di `_dengon` sono resi da un pezzo: «Collaborazione»,
«Invito», «Dichiarazione», «Incoraggiamento», «Disprezzo». Il primo diceva
`none(Cordiale)`.

✅ **«Nessuna», che e' quel che 「なし」 dice gia' a `init.hsp:371`.** Il nome a
cui si riferirebbe — «messaggio» — a schermo non c'e' mai: la parola sta da sola
in colonna, quindi il genere non si vede e conviene la resa che rende uniformi
tutti e tre i siti del giapponese (`init.hsp:371`, `text.hsp:49`,
`command.hsp:1445`). Da qui in avanti la rete 3 su 「なし」 tace.

⚠️ Le voci di `text.hsp:49` sono **sei sulla stessa riga**, quindi la chiave e'
`(riga, jp)` e non la sola riga: il modello di `correzione-schivata.py` andava
bene per `action.hsp`, dove ogni riga ha una voce sola.

⚠️ **Si compone e si codifica in memoria PRIMA di aprire il file in scrittura**,
che e' la lezione della 39a: `toppe.jsonl` a zero byte per un errore di codifica
dentro `write()`.
"""
import io
import json
import sys

CORREZIONI = {
    'dizionario/text.hsp.jsonl': {
        (49, 'なし'): ('none', 'Nessuna'),
    },
}

fatte, saltate, corrette, da_scrivere = 0, 0, [], {}
for percorso, correzioni in CORREZIONI.items():
    righe = [json.loads(l) for l in io.open(percorso, encoding='utf-8') if l.strip()]
    viste = set()
    for d in righe:
        chiave = (d['riga'], d['jp'])
        if chiave not in correzioni:
            continue
        vecchia, nuova = correzioni[chiave]
        viste.add(chiave)
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
# ⚠️ `verifica --dizionario` NON le guarda: confronta il dizionario col sorgente
#    e conta orfane e non tradotte.
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
