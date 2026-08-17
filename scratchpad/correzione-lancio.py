# -*- coding: utf-8 -*-
"""La stessa mossa con due nomi, e uno dei due usa la parola sbagliata.

⭐ **Trovata dal referto nuovo della 57ª**, `scratchpad/misura-rete4.py`, che
passa la rete 4 all'indietro su tutto il dizionario. Su 11.982 gruppi
`(giapponese, funzioni)` ce ne sono **nove** resi in piu' di un modo **con lo
stesso inglese**, cioe' senza nessuna scusa di monte. Questo e' uno dei nove:

    jp='一投入魂'  en='OverLimit-Throw'
        buff.hsp:263    «Tiro oltre il limite»
        skill.hsp:1240  «Lancio oltre il limite»

Non sono due cose diverse: `SKILL_SPACT_OVERLIMIT_THROW` e' l'azione speciale
che si lancia, `BUFF_OVERLIMIT_THROW` e' il potenziamento che ne esce. Chi la usa
la sceglie da un elenco con un nome e se la ritrova nella barra di stato con un
altro.

⚠️⚠️ **E «Tiro» non e' solo diverso: e' la parola di un'ALTRA cosa.** Il progetto
ha gia' fissato, e in due posti che nessuno puo' confondere:

    skill.hsp:186   投擲  Throwing   ->  «Lancio»
    text.hsp:136    遠隔  Shoot      ->  «Tiro»      (lo slot dell'equipaggiamento)

Cioe' «Tiro» e' il **tiro con l'arma a distanza**, e questa e' una mossa di
**lancio** — il suo stesso `skilldesc` dice 「通常投擲強化」, «potenzia il lancio
normale». Le altre cinque mosse di lancio del gioco portano tutte quella parola:
«Lancio rotante» (`skill.hsp:1452`), «Lancio tutt'intorno» (`:1465`), «Lancio
splendente» (`:1844`).

⚠️ **Ma «Lancio oltre il limite» non e' scrivibile per il potenziamento**: fa 22
caratteri e il tetto di `buffname` e' **20** (`riquadri.py`, colonna da 145 px).
Allineare il potenziamento all'elenco avrebbe rotto la barra di stato; allineare
l'elenco al potenziamento avrebbe tenuto la parola sbagliata.

✅ **La resa giusta gliela dava il suo stesso messaggio.** `buff.hsp:264` e' gia'
reso «mette l'**anima** nel **lancio**», che traduce 「投擲に魂を込めた」 — e il nome
della mossa, 「一投入魂」, dice letteralmente *un lancio, l'anima dentro*. Da li'
esce **«Lancio dell'anima»**: sedici caratteri, dentro il tetto, con la parola
giusta, e il nome torna a dire quel che il suo messaggio annuncia.
💡 E' la stessa disciplina di `correzione-il-tiro.py` della 49ª — «quando due
voci non si accordano, si guarda quale delle due e' LIBERA» — con un passo in
piu': qui nessuna delle due era libera, e la terza voce del gruppo ha fatto da
arbitro.

⚠️ Lo script compone e valida tutto in memoria prima di aprire un file in
scrittura, per la ragione scritta in `LEGGIMI.md`.
"""
import io
import json
import sys

NUOVA = "Lancio dell'anima"

CORREZIONI = {
    # il potenziamento: aveva la parola del TIRO su una mossa di LANCIO
    'dizionario/buff.hsp.jsonl': {
        263: ('Tiro oltre il limite', NUOVA),
    },
    # l'azione speciale: parola giusta, ma 22 caratteri contro un tetto di 20
    'dizionario/skill.hsp.jsonl': {
        1240: ('Lancio oltre il limite', NUOVA),
    },
}

# rete 0: la resa nuova deve stare nel tetto di `buffname` (riquadri.py)
TETTO_BUFFNAME = 20
if len(NUOVA) > TETTO_BUFFNAME:
    sys.exit(f'rete 0: {NUOVA!r} fa {len(NUOVA)} caratteri, il tetto e\' {TETTO_BUFFNAME}')
print(f'rete 0: {NUOVA!r} fa {len(NUOVA)} caratteri su {TETTO_BUFFNAME}')

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
