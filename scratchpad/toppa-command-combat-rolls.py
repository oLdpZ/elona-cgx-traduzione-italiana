# -*- coding: utf-8 -*-
"""Due etichette del riquadro «Combat Rolls» si saldano al valore: toppa sulla POSIZIONE.

⚠️⚠️ **E' la prima toppa del progetto che non cambia una parola: sposta una
coordinata.** Trovata al collaudo della 47a, non da una misura: a schermo si
legge «Mira64%» e «Pot. magia100%», tutt'e due senza spazio.

## Perche' succede, e perche' non e' colpa della resa

Il riquadro disegna l'etichetta e il valore a **due posizioni fisse**, e conta
sul fatto che l'etichetta ci stia in mezzo. Il carattere del ramo inglese e'
Courier New, monospaziato, e l'etichetta gira a corpo **10**
(`12 + sizefix - en * 2`, con `sizefix` assente da `config.txt` e quindi 0),
cioe' **6 px per carattere**. Il valore esce sempre a `wx + 625 - en * 8`, cioe'
a **617**.

    etichetta        parte a   larga   finisce a   spazio prima del valore
    Hit  (inglese)     590      18        608              9 px
    Mira (italiano)    590      24        614              3 px   <- saldata
    SpellPow (ingl.)   554      48        602             15 px
    Pot. magia (it.)   554      60        614              3 px   <- saldata

## La strada l'ha indicata upstream, tre righe piu' su

⭐ **Il sorgente compensa gia' esattamente cosi' quando l'inglese e' piu' largo
del giapponese**: `:10731` scrive `pos wx + 590 - en * 16` per «Evade» e `:10733`
`pos wx + 564 - en * 10` per «SpellPow». Il `- en * N` e' un idioma di casa, e
serve proprio a questo. Alla riga di 「命中」 (`:12427`) non c'e', perche' «Hit» e'
piu' **stretto** del giapponese e non serviva.
✅ Quindi la toppa non inventa niente: mette la compensazione dove l'italiano ne
ha bisogno e upstream non ne aveva. I valori sono scelti per **pareggiare lo
spazio dell'inglese**, non per esagerare:

    :12427   wx + 590            ->  wx + 590 - en * 6     «Mira» finisce a 608, 9 px
    :10733   wx + 564 - en * 10  ->  wx + 564 - en * 22    «Pot. magia» a 602, 15 px

⚠️ **A sinistra c'e' spazio.** Sulla riga d'attacco i dadi escono a
`wx + 460 + en * 8` = 468 e una stringa come «2d4+3 x2.9» ne occupa 72 (corpo
12), quindi finisce a 540: l'etichetta a 584 ha 44 px di margine. Sulla riga di
`SpellPow` l'unica cosa a sinistra e' il titolo del riquadro (`:10429`,
`wx + 400`), la cui sottolineatura arriva a 520: l'etichetta a 542 sta larga.

## Perche' una toppa e non una resa piu' corta

Per «Mira» l'alternativa era scendere a tre caratteri — «Mir», «Col» — cioe'
buttare via il termine che `buff.hsp:679` ha gia' deciso mettendo 「射撃力上昇」 e
「命中率上昇」 uno accanto all'altro («Tiro e mira»). Per «Pot. magia» sarebbe stato
riaprire la resa di un'altra sessione. ✅ La toppa non tocca nessuna parola.

⚠️ **E non viola la regola della 46a** («una toppa e una resa non stanno sulla
stessa riga»): le rese stanno a `:12428` e `:10734`, le toppe a `:12427` e
`:10733`. Righe diverse, nessun rinvio da fare.

💡 La toppa vale per tutt'e due le schermate che usano `*com_skill_calcAttack`:
la scheda del personaggio (`c`) e quella dell'equipaggiamento (`w`).
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\command.hsp'
NOME = 'command.hsp'

COMUNE = (
    "Il riquadro «Combat Rolls» disegna l'etichetta e il valore a due posizioni "
    "FISSE e conta sul fatto che l'etichetta ci stia in mezzo. Courier New a corpo "
    "10 (`12 + sizefix - en * 2`, sizefix assente da config.txt e quindi 0) fa 6 px "
    "per carattere, e il valore esce sempre a `wx + 625 - en * 8` = 617. "
    "⭐ La strada l'ha indicata upstream tre righe piu' su: `:10731` scrive "
    "`pos wx + 590 - en * 16` per «Evade» e `:10733` `pos wx + 564 - en * 10` per "
    "«SpellPow», cioe' compensa gia' cosi' quando l'inglese e' piu' largo del "
    "giapponese. La toppa mette la stessa compensazione dove serve all'italiano, "
    "con un valore scelto per PAREGGIARE lo spazio che si tiene l'inglese. "
    "⚠️ Non viola la regola della 46a: la resa sta sulla riga del `mes lang(...)`, "
    "la toppa su quella del `pos`. Righe diverse, nessun rinvio. "
    "⚠️ Trovata al COLLAUDO, non da una misura: a schermo si leggeva tutto attaccato."
)

TOPPE = [
    {
        'riga': 12427,
        'cerca': 'pos wx + 590,',
        'metti': 'pos wx + 590 - en * 6,',
        'motivo': (
            "command.hsp:12427, l'etichetta di 「命中」 nel riquadro «Combat Rolls» "
            "e nella scheda dell'equipaggiamento. «Hit» e' di tre caratteri e "
            "finisce a 608, nove pixel prima del valore; «Mira» e' di quattro, "
            "finisce a 614 e ne lascia tre, cioe' si salda: a schermo si legge "
            "«Mira64%». Spostata di sei pixel a sinistra torna a finire a 608, "
            "esattamente come l'inglese. "
            "💡 Accorciare la resa a tre caratteri avrebbe voluto dire buttare via "
            "«Mira», che buff.hsp:679 ha gia' deciso mettendo 「射撃力上昇」 e "
            "「命中率上昇」 uno accanto all'altro («Tiro e mira»). "
            "⚠️ A sinistra c'e' spazio: i dadi escono a wx+468 e una riga come "
            "«2d4+3 x2.9» finisce a 540. " + COMUNE
        ),
    },
    {
        'riga': 10733,
        'cerca': 'pos wx + 564 - en * 10,',
        'metti': 'pos wx + 564 - en * 22,',
        'motivo': (
            "command.hsp:10733, l'etichetta di 「魔法威力」 nel riquadro «Combat "
            "Rolls». «SpellPow» e' di otto caratteri e finisce a 602, quindici "
            "pixel prima del valore; «Pot. magia» e' di dieci, finisce a 614 e ne "
            "lascia tre: a schermo si legge «Pot. magia100%». Portata la "
            "compensazione da 10 a 22 pixel, l'etichetta finisce a 602 come "
            "l'inglese. "
            "⚠️ La resa non e' di questa sessione, e la toppa non la tocca: e' un "
            "difetto di POSIZIONE, non di parola. "
            "⚠️ A sinistra c'e' spazio: l'unica cosa su quella riga e' il titolo "
            "del riquadro (:10429, wx+400), la cui sottolineatura arriva a 520. "
            + COMUNE
        ),
    },
]

righe = io.open(SORGENTE, encoding='cp932').read().split('\n')
nuove = []

for t in TOPPE:
    originale = righe[t['riga'] - 1]
    if t['cerca'] not in originale:
        raise SystemExit(f"{NOME}:{t['riga']} non ha la forma attesa: {originale.strip()[:120]}")
    quante = sum(1 for r in righe if r == originale)
    if quante != 1:
        raise SystemExit(f"{NOME}:{t['riga']} compare {quante} volte, non una: toppa ambigua")
    nuova = originale.replace(t['cerca'], t['metti'])
    if nuova == originale:
        raise SystemExit(f"{NOME}:{t['riga']}: la toppa non cambierebbe niente")
    nuove.append({'file': NOME, 'cerca': originale, 'sostituisci': nuova,
                  'motivo': t['motivo'], '_riga': t['riga']})

esistenti = [l for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]


def _chiave(t: dict) -> tuple:
    cerca = t['cerca']
    return (t['file'], tuple(cerca) if isinstance(cerca, list) else cerca)


gia = {_chiave(json.loads(l)) for l in esistenti}
da_scrivere = [t for t in nuove if _chiave(t) not in gia]

if not da_scrivere:
    print('toppe gia presenti, niente da fare')
else:
    # ⚠️ Si compone, si codifica in memoria e solo allora si apre: vedi la 39a.
    dati = ''.join(
        json.dumps({k: v for k, v in t.items() if not k.startswith('_')},
                   ensure_ascii=False) + '\n'
        for t in da_scrivere
    ).encode('utf-8')
    with io.open('toppe.jsonl', 'ab') as f:
        f.write(dati)
    print(f'{len(da_scrivere)} toppe aggiunte (totale {len(esistenti) + len(da_scrivere)})')
    for t in da_scrivere:
        print(f"  :{t['_riga']}")
        print(f"    - {t['cerca'].strip()}")
        print(f"    + {t['sostituisci'].strip()}")
