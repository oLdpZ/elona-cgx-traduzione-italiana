# -*- coding: utf-8 -*-
"""Le sei stringhe di `CDATAN_NEWSEX` in `command.hsp:3639`-`:3654`: invariate.

⚠️ **Questa non e' una decisione nuova: e' l'applicazione di una decisione della
Fase 0**, scritta in `invariati.md` alla sezione «Valori di dato, non testo —
tradurli rompe i salvataggi» e datata 2026-08-07. Quella sezione nomina gia'
`command.hsp:3639-3654` fra i siti di rilettura, ma le sei voci di questo file
non erano mai state messe in dizionario: risultavano «non ancora tradotte» e
tornavano a galla a ogni sessione.

Il valore di `CDATAN_NEWSEX` fa quattro mestieri con **una firma sola**:

  - etichetta di menu (`command.hsp:4653`-`:4656`);
  - valore **salvato** nel personaggio (`:4678`-`:4690`, poi `:4707`);
  - chiave di **confronto** (`:3639`-`:3654`, `init.hsp:1813`-`:2008` dentro
    `he()`/`his()`/`him()`, `text.hsp:359`-`:375`);
  - testo stampato nudo (`:3640`-`:3655`, `:17834`, `init.hsp:2085`).

Siccome il dizionario e' indicizzato per contenuto, il confronto di `:3645` e la
stampa di `:3646` sono la **stessa voce**: non si separano traducendo. E un
salvataggio fatto con la build inglese contiene la stringa inglese, quindi
tradurla farebbe fallire ogni confronto in silenzio.
✅ Che sia cosi' lo dice upstream: `init.hsp:1816` confronta con «male?» **e**
«trans-male» insieme, cioe' tiene un ramo di compatibilita' per il nome vecchio.
⚠️ E `:4702` e' `locvar_newsex = "" + inputlog`: il giocatore puo' digitarselo.

`text.hsp:123` e `:124` hanno gia' `en='male' it='male'`, cioe' esattamente
questa forma. Qui si fa lo stesso per `command.hsp`.

💡 **`bisexual` e' nuovo in `invariati.md`, ed e' il gemello di
`hermaphorodite`**: `:3639` confronta con «bisexual» ma chi scrive il valore
(`chara.hsp:2790`, `command.hsp:4686`) scrive «hermaphrodite». Il ramo e' morto
nella build inglese, vivo in quella giapponese, dove 「両性具有」 sta da tutt'e due
le parti.

💡 **Perche' fuori dal lotto e non dentro**: la rete 7 del modello ferma una voce
che sta dentro un confronto e chiede di rinviarla, e ha ragione a fermarla —
quello che non sa e' che per questa famiglia esiste gia' una decisione piu'
specifica. Tenerla fuori dal lotto lascia la rete intatta e la decisione
rintracciabile.
"""
import io
import json

VOCI = ['bisexual', 'none', 'male', 'female', 'male?', 'female?']

da_fare = {(v['riga'], v['en']): v
           for v in (json.loads(l) for l in io.open('lavoro/_command.jsonl', encoding='utf-8') if l.strip())}

righe = []
for riga, en in ((3639, 'bisexual'), (3642, 'none'), (3645, 'male'),
                 (3648, 'female'), (3651, 'male?'), (3654, 'female?')):
    if (riga, en) not in da_fare:
        raise SystemExit(f'chiave che non aggancia nessuna voce: {(riga, en)}')
    v = dict(da_fare[(riga, en)])
    v['it'] = en          # invariato: la resa E' l'inglese, per scelta dichiarata
    righe.append(v)

with io.open('lavoro/invariati-command-newsex.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for v in righe:
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
for v in righe:
    print(f"{v['riga']}  en={v['en']!r}  ->  invariato")
print('scritto lavoro/invariati-command-newsex.jsonl')
