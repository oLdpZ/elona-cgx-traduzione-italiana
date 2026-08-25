# -*- coding: utf-8 -*-
"""97a - Le ultime dodici firme del perimetro `lang()` fuori da `db_card.hsp`.

Dodici voci in tre file, e **nessuna delle tre e' una decisione nuova**: undici
sono valori di dato gia' dichiarati in `invariati.md` da quattro sessioni, e la
dodicesima e' una resa gia' scritta altrove.

⭐⭐⭐ GLI UNDICI OPERANDI DI `CDATAN_NEWSEX`. `invariati.md`, sezione «Valori di
dato, non testo», li elenca tutti dalla 47a: `male`, `female`, `none`,
`hermaphrodite`, `male?`, `female?`, `trans-male`, `trans-female`. Tradurli
rompe i salvataggi — il confronto col valore italiano fallisce e il gioco
sbaglia il genere di ogni personaggio gia' creato — e a schermo ci arrivano per
**toppa**, non per resa. Quel che mancava non era la decisione: erano i siti.
`command.hsp:3651`, `item.hsp:4139`, `text.hsp:371` erano gia' entrati; questi
undici — `init.hsp:1813`-`:1822`, `:1973`, `chara.hsp:2790`, `:3631`-`:3633`,
`:4390` — no, e tenevano tre file «aperti» senza avere niente da fare.

⚠️⚠️ **E ADESSO `misura-rete4.py` SALE DA 806 A 812, PER COSTRUZIONE** — nella
colonna «inglese diverso», che e' quella legittima; i gruppi con lo **stesso**
inglese, che sono quelli senza scusa, restano **149**. Sono due giapponesi resi
in piu' modi, e nessuno dei due e' un errore nostro:

    自称男性  ->  'male?'   (`init.hsp:1816`, `command.hsp:3651`, `text.hsp:371`)
              ->  'trans-male'  (`init.hsp:1816`, il secondo operando della riga)
              ->  'female?' (`init.hsp:1973`)   <- ⚠️ e questo e' un baco di monte
    自称女性  ->  'female?' e 'trans-female'

Il giapponese ha **una** parola dove l'inglese ne ha **due** (il valore vecchio e
quello nuovo del campo), e i due valori devono restare distinti perche' un
salvataggio puo' contenere l'uno o l'altro. Renderli uguali per far tacere la
rete significherebbe fondere due valori di dato: il rimedio sarebbe peggiore.

⚠️⚠️ E **`battute --divergenti` resta 13**, che al primo giro mi ha sorpreso:
avevo scritto qui che sarebbe salito a 15. `strumenti/battute.py:79` e'
`FILE = "db_creature.hsp"` — quello strumento guarda **un file solo**, e di
`init.hsp` non sa niente. ⭐ E' la stessa cosa che la 96a aveva gia' scoperto sui
due `(Empty)`, scritta nella sua ripresa, e che io ho riscritto sbagliata **tre
volte** in questa sessione prima di misurarla. Il conto da guardare per questa
famiglia e' `misura-rete4.py`, non `--divergenti`.

⚠️ `init.hsp:1973` merita una riga a parte: `his()` confronta `NEWSEX` con
`lang("自称男性", "female?")` e restituisce 彼女？の / «her?». **Il giapponese
sbaglia** — dovrebbe dire 自称女性, come fa il gemello `:1822` — e l'inglese ha
ragione. Rendendo `it` = `en` la build italiana si comporta come quella inglese,
cioe' **giusta**: e' il quinto rovesciamento di questa sessione dopo i quattro
di `system.hsp`, e come quelli si e' deciso guardando che cosa fa il codice.

⭐⭐ `map.hsp:1396` NON E' UN INVARIANTE: E' UN DIFETTO VIVO CHE SI CHIUDE.

    1396   if ( mdatan(MDATAN_NAME) == "" | mdatan(MDATAN_NAME) == lang("ノースティリス", "North Tyris") ) {
    1397       mdatan(MDATAN_NAME) = lang("わが家", "Your Home")

Qui l'operando **non** viene dal salvataggio come `CDATAN_NEWSEX`: `map.hsp:1401`
lo riscrive a ogni caricamento con `mapname(gdata(GDATA_AREA))`, e per la mappa
del mondo `mapname()` finisce in `text.hsp:2737`, che e' **gia' reso** «Tyris del
Nord». Quindi oggi, nella build italiana, il confronto non riesce mai e la casa
del giocatore si chiama «Tyris del Nord» invece che «Casa mia». Rendere `:1396`
con la stessa resa di `text.hsp:2737` lo ripara. ⚠️ E la resa dev'essere
**identica** a quella, non una nuova: qui la coerenza non e' stile, e' il
funzionamento.
"""
import io
import json
import sys

RESE = {
    # --- init.hsp: gli operandi di he()/his()/him()
    ('init.hsp', 1813, 'male'): 'male',
    ('init.hsp', 1813, 'none'): 'none',
    ('init.hsp', 1816, 'male?'): 'male?',
    ('init.hsp', 1816, 'trans-male'): 'trans-male',
    ('init.hsp', 1819, 'female'): 'female',
    ('init.hsp', 1819, 'hermaphrodite'): 'hermaphrodite',
    ('init.hsp', 1822, 'female?'): 'female?',
    ('init.hsp', 1822, 'trans-female'): 'trans-female',
    ('init.hsp', 1973, 'female?'): 'female?',

    # --- chara.hsp: i valori scritti e il menu della creazione
    ('chara.hsp', 2790, 'hermaphrodite'): 'hermaphrodite',
    ('chara.hsp', 3631, 'male?'): 'male?',
    ('chara.hsp', 3632, 'female?'): 'female?',
    ('chara.hsp', 4390, 'none'): 'none',

    # --- map.hsp: il difetto vivo
    ('map.hsp', 1396, 'North Tyris'): 'Tyris del Nord',
}

LOTTI = {
    'init.hsp': 'lavoro/97-init.jsonl',
    'chara.hsp': 'lavoro/97-chara.jsonl',
    'map.hsp': 'lavoro/97-map.jsonl',
}

usate = set()
for nome, lotto in LOTTI.items():
    voci = [json.loads(l) for l in io.open(lotto, encoding='utf-8') if l.strip()]

    def chiave(v):
        trovate = [k for k in RESE
                   if k[0] == nome and k[1] == v['riga'] and k[2] == v['en']]
        return trovate[0] if len(trovate) == 1 else None

    mancanti = [(v['riga'], v['en']) for v in voci if chiave(v) is None]
    if mancanti:
        print(f'{nome} — mancanti: {mancanti}')
        sys.exit(1)
    usate |= {chiave(v) for v in voci}

    with io.open(lotto, 'w', encoding='utf-8', newline='\n') as fh:
        for v in voci:
            v['it'] = RESE[chiave(v)]
            fh.write(json.dumps(v, ensure_ascii=False) + '\n')
    print(f'{len(voci)} rese scritte in {lotto}')

in_piu = [k for k in RESE if k not in usate]
if in_piu:
    print("in piu' : %s" % in_piu)
    sys.exit(1)
