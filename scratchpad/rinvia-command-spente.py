# -*- coding: utf-8 -*-
"""Aggiunge a rinviate.jsonl le tre righe spente di `command.hsp` (43a, lotto 001).

`:115` e' commentata col `;`, `:265` e `:271` stanno dentro un blocco `/* ... */`.
Tutt'e tre le ha fermate la rete 6 del lotto `fase4-command-001`.
"""
import io
import json

MOTIVO_115 = (
    "command.hsp:115. Riga **commentata col `;`** nel sorgente, e non da sola: "
    "e' l'ultima di un tratto spento (`:110`-`:120`) che stampava i "
    "potenziamenti attivi sul bersaglio — `calcbuff`, poi "
    "`buffname(...) + \": \" + turni + lang(\"ﾀｰﾝ\", \"turns \")`. Il mod l'ha "
    "sostituito col tratto vivo di `:124`-`:130`, che stampa gli **stati** e non "
    "i potenziamenti, e la cui coda 「ﾀｰﾝ」/\" stacks \" e' resa « turni » nello "
    "stesso lotto. ⚠️ Le due righe hanno lo **stesso giapponese** e un inglese "
    "diverso — «turns » qui, « stacks » la': la resa viva segue il giapponese e "
    "il codice, che conta turni, e questa non serve. Non c'e' toppa da fare: non "
    "e' un difetto a schermo, e' testo morto."
)

MOTIVO_BLOCCO = (
    "Riga dentro un commento di **BLOCCO**: il tratto `/* JAMES CUSTOM */` di "
    "`command.hsp` che si chiude a `:273` con "
    "`********** ORIGINAL - ENDING **********/`. E' la versione di monte della "
    "scheda del bersaglio, che il mod ha rifatto piu' su: `:265` e `:271` sono "
    "le gemelle spente di `:160` e `:169`, che invece sono vive e rese nello "
    "stesso lotto («ID sprite: », «Sesso: … / Eta': … / Fede: …»). "
    "💡 Si riconoscono anche a occhio: le due spente scrivono i due punti a "
    "**larghezza intera** (`SpriteID：`), le vive a larghezza normale. "
    "Non c'e' toppa da fare: non e' un difetto a schermo, e' testo morto."
)

NUOVE = [
    ((115, 'turns '), MOTIVO_115),
    ((265, 'SpriteID： / ColorID： '), MOTIVO_BLOCCO),
    ((271, 'Sex: / Age: / Religion:'), MOTIVO_BLOCCO),
]

voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_command.jsonl', encoding='utf-8')
                  if l.strip())}

righe = []
for k, motivo in NUOVE:
    if k not in voci:
        raise SystemExit(f'chiave che non aggancia nessuna voce: {k}')
    v = voci[k]
    spenta_da = ('riga commentata col `;`' if k[0] == 115
                 else 'riga dentro un blocco /* ... */ spento dal mod')
    righe.append({
        'firma': v['firma'],
        'file': 'command.hsp',
        'en': v['en'],
        'rinviata_a': f'mai: {spenta_da}',
        'motivo': motivo,
    })

esistenti = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
firme = {json.loads(l)['firma'] for l in esistenti}
nuove = [r for r in righe if r['firma'] not in firme]
if not nuove:
    print('gia presenti, niente da fare')
else:
    # ⚠️ Si compone, si codifica in memoria e solo allora si apre il file: la
    # lezione della 39a, quando un errore di codifica a meta' di una `write()`
    # lascio' `toppe.jsonl` a zero byte.
    testo = ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in nuove)
    dati = testo.encode('utf-8')
    with io.open('rinviate.jsonl', 'ab') as f:
        f.write(dati)
    print(f'{len(nuove)} rinviate aggiunte (totale {len(esistenti) + len(nuove)})')
