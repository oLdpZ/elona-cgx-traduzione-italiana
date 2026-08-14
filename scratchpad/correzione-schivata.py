# -*- coding: utf-8 -*-
"""Le quattro rese che dicono «X schiva Y» dove Y non e' l'attacco, e' chi attacca.

⚠️ **Trovata a schermo nel collaudo della 39ª**, e in uno schermo solo compariva
**cinque volte**: «`Il viandante schiva Kefry.`» E' `action.hsp:5616`, il ramo
della schivata quando a schivare sei tu o un tuo alleato.

💡 **Il difetto e' dell'inglese di monte, e il giapponese lo smentisce.** Il
sorgente e' `lang(aln(tc) + name(cc) + "の攻撃を避けた。", name(tc) + " evade" +
_s(tc) + " " + name(cc) + ".")`: il giapponese dice 「name(cc) **の攻撃を**
避けた」, cioe' «ha schivato **l'attacco di** cc», e l'inglese butta via
「攻撃」 lasciando il nome nudo come complemento oggetto. In inglese «X evades Y»
regge lo stesso; in italiano «schiva Kefry» vuol dire un'altra cosa.

⚠️ **E la strada del genitivo era chiusa in partenza**: «l'attacco **di** » +
`name()` fa fondere l'articolo che `name()` porta dentro — «l'attacco di il
putit» — ed e' esattamente la rete 8.

✅ **La forma e' quella della 37ª**: «**X attacca, ma Y para**», che fa dei due
nomi due soggetti e non chiede nessuna preposizione. Li' aveva risolto le tre
parate del lotto 015; qui risolve le schivate **e la parata due righe sopra**,
che aveva la stessa forma storta («X respinge con lo scudo Y») e che nessuno
aveva guardato perche' il collaudo non c'era arrivato.

💡 **I due rami restanti dello stesso blocco erano gia' giusti** e non si
toccano: `:5601` («X urta contro lo scudo.») e `:5619` («X manca Y.») nominano
un personaggio solo o lo nominano nel ruolo giusto, perche' li' l'inglese di
monte aveva scelto il soggetto opposto.

⚠️ **Lo script compone e valida tutto in memoria prima di aprire un file in
scrittura.** Nella stessa sessione uno script scritto in fretta ha troncato
`toppe.jsonl` a zero byte fallendo dentro `write()`, e a salvarlo e' stato solo
`git checkout`.
"""
import io
import json
import sys

CORREZIONI = {
    'dizionario/action.hsp.jsonl': {
        # la parata: stessa forma storta della schivata, due righe sopra
        5598: (
            'name(tc) + " respinge con lo scudo " + name(cc) + "."',
            'name(cc) + " attacca, ma " + name(tc) + " para con lo scudo."',
        ),
        # la schivata, vista a schermo cinque volte in uno schermo solo
        5616: (
            'name(tc) + " schiva " + name(cc) + "."',
            'name(cc) + " attacca, ma " + name(tc) + " schiva."',
        ),
        # la schivata magistrale, ramo alleato...
        5640: (
            'name(tc) + " schiva con maestria " + name(cc) + "."',
            'name(cc) + " attacca, ma " + name(tc) + " schiva con maestria."',
        ),
        # ...e ramo nemico, che ha lo stesso inglese e quindi la stessa resa
        5644: (
            'name(tc) + " schiva con maestria " + name(cc) + "."',
            'name(cc) + " attacca, ma " + name(tc) + " schiva con maestria."',
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
# ⚠️ `verifica --dizionario` NON le guarda: una correzione scritta a mano nel
#    dizionario non incontra nessun'altra guardia.
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
