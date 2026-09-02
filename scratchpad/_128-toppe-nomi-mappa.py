# -*- coding: utf-8 -*-
"""Il secondo lotto della 128a: tre confronti che la traduzione aveva gia' rotto.

⚠️⚠️⚠️ **NON E' UNA RESA NUOVA: E' UNA RINVIATA LA CUI CONDIZIONE E' MATURATA
SENZA CHE NESSUNO TORNASSE A GUARDARE.**

`rinviate.jsonl` porta tre voci di `proc.hsp` con la stessa forma, scritte nella
27a e nella 60a, e tutt'e tre dicono la stessa cosa:

    «Non e' testo, e' un operando di confronto fra due file. map_rand.hsp:1287
     ASSEGNA il nome della mappa e proc.hsp:1123 lo CONFRONTA con lo stesso
     letterale. Tradurre solo il confronto lo fa fallire per sempre, in
     silenzio. Va tradotta INSIEME a map_rand.hsp: **non prima**.»

Il rinvio era giusto. Solo che **l'altra meta' e' stata fatta**, in una sessione
qualunque, e nessuno e' tornato a chiudere il rinvio. Nella build di oggi:

    map_rand.hsp:1287   mdatan(MDATAN_NAME) = lang("パーティー場", "Sala feste")
    map.hsp:4092        mdatan(0)           = lang("商船内部",   "Nave mercantile")
    map.hsp:4104        mdatan(0)           = lang("海賊船内部", "Nave pirata")
    map.hsp:8296        mdatan(MDATAN_NAME) = lang("海賊船内部", "Nave pirata")

    proc.hsp:1123       if ( mdatan(MDATAN_NAME) == lang(…, "Party Room") )
    proc.hsp:5584/:5685 if ( mdatan(0) == lang(…, "Merchant ship") | … )

⚠️⚠️ **Quindi i tre rami sono morti nella build italiana, oggi**, ed e'
esattamente il difetto che il rinvio voleva evitare — arrivato dalla parte
opposta:

  - `proc.hsp:1123` — ballare nella **sala delle feste** dura 41 turni invece
    di 4 (`CDATA_ACTION_PERIOD`). Oggi ne dura 4.
  - `proc.hsp:5584` e `:5685` — scavando **dentro una nave** il bottino deve
    diventare spazzatura, schegge e legname invece di minerali e polvere di
    stelle. Oggi la nave frutta come un sotterraneo.

💡 **La forma della riparazione non si inventa: e' quella della migrazione di
«Your Home»** (toppa di `map.hsp:1396`). La `lang()` **resta rinviata** — e'
quel che rende stabile la stringa cercata dalla toppa, ed e' la regola della
rete 7 sui confronti contro un valore serializzato — e il letterale italiano si
aggiunge **fuori** da `lang()`, con un `|`, perche' non e' testo da leggere: e'
il valore memorizzato. Cosi' il confronto accetta tutt'e due, e un salvataggio
scritto prima della traduzione continua a funzionare.

ⓘ `mdatan` e' serializzato (`module.hsp:4598` noteadd, `:4601` noteget), quindi
la doppia via non e' prudenza a vuoto: e' la stessa ragione della 42a.
"""
import io
import json

BASE = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
righe = io.open(BASE + r'\proc.hsp', encoding='cp932').read().split('\n')

RINVIO = (
    "⚠️⚠️⚠️ RINVIATA CON CONDIZIONE, E LA CONDIZIONE E' MATURATA: la voce di "
    "`rinviate.jsonl` diceva «va tradotta INSIEME a chi assegna il nome della "
    "mappa, non prima», e chi assegna e' stato tradotto in una sessione "
    "qualunque senza che nessuno tornasse a chiudere il rinvio. Il ramo e' "
    "quindi MORTO nella build italiana. "
    "💡 La forma e' quella della migrazione di «Your Home» (toppa di "
    "map.hsp:1396): la `lang()` resta rinviata — e' quel che rende stabile la "
    "stringa cercata, regola della rete 7 sui confronti contro un valore "
    "serializzato — e il letterale italiano si aggiunge FUORI da lang(), "
    "perche' non e' testo da leggere ma il valore memorizzato. Il confronto "
    "accetta tutt'e due, quindi un salvataggio scritto prima della traduzione "
    "continua a funzionare (`mdatan` e' serializzato: module.hsp:4598/:4601). "
)

TOPPE = [
    {
        'riga': 1123,
        'coda': ' | mdatan(MDATAN_NAME) == "Sala feste"',
        'motivo': (
            RINVIO +
            "proc.hsp:*act_perform (:1123). `map_rand.hsp:1287` assegna "
            "`mdatan(MDATAN_NAME) = lang(\"パーティー場\", \"Sala feste\")` — gia' "
            "italiano nella build — e questo confronto cercava ancora «Party "
            "Room». ⚠️ L'effetto a schermo non e' una parola: ballare nella "
            "sala delle feste deve durare **41 turni invece di 4** "
            "(`cdata(CDATA_ACTION_PERIOD, cc) = 41`), e oggi ne dura 4. "
            "ⓘ Il rinvio e' della 27a."
        ),
    },
    {
        'riga': 5584,
        'coda': ' | mdatan(0) == "Nave mercantile" | mdatan(0) == "Nave pirata"',
        'motivo': (
            RINVIO +
            "proc.hsp:5584, lo scavo (`*act_dig`). `map.hsp:4092` e `:4104` "
            "assegnano `mdatan(0)` = «Nave mercantile» / «Nave pirata» (e "
            "`:8296` la seconda), tutt'e tre gia' italiane nella build, e "
            "questo confronto cercava ancora l'inglese. ⚠️ L'effetto: dentro "
            "una nave il bottino dello scavo deve diventare **spazzatura, "
            "schegge di legno e legname** invece di zolfo, argilla, cristallo "
            "nero e polvere di stelle. Oggi la nave frutta come un "
            "sotterraneo. ⓘ Il rinvio e' della 60a. ⚠️ Le due condizioni "
            "aggiunte sono DUE perche' i nomi assegnati sono due, e vanno "
            "tutt'e due: la riga inglese ne confronta due, non uno."
        ),
    },
    {
        'riga': 5685,
        'coda': ' | mdatan(0) == "Nave mercantile" | mdatan(0) == "Nave pirata"',
        'motivo': (
            RINVIO +
            "proc.hsp:5685, la **gemella** di `:5584`: lo stesso blocco di "
            "scavo dentro il ramo che gira quando si scava con l'oggetto "
            "cercatore (`ITEM_ID_DOWSING_OPATOS`). ⚠️ Le due righe NON sono "
            "identiche — hanno indentazione diversa, tre tabulazioni contro "
            "sei — quindi sono due toppe e non una `tutte`: e' la trappola "
            "dell'indentazione della 127a. ⓘ Stesso effetto e stesso rinvio "
            "di `:5584`."
        ),
    },
]

# ---------------------------------------------------------------------------

fuori = []
for t in TOPPE:
    originale = righe[t['riga'] - 1]
    if '== lang(' not in originale or not originale.rstrip().endswith(') {'):
        raise SystemExit('proc.hsp:{}: non e\' il confronto atteso: {!r}'
                         .format(t['riga'], originale[:90]))
    quante = sum(1 for r in righe if r == originale)
    if quante != 1:
        raise SystemExit('proc.hsp:{}: la riga compare {} volte'
                         .format(t['riga'], quante))
    testa = originale.rstrip()
    if not testa.endswith(' ) {'):
        raise SystemExit('proc.hsp:{}: coda inattesa: {!r}'.format(t['riga'], testa[-10:]))
    nuova = testa[:-len(' ) {')] + t['coda'] + ' ) {'
    nuova.encode('cp932')
    for c in nuova:
        if c != '♪' and len(c.encode('cp932')) != 1 and not ('\u3000' <= c <= '\u9fff' or '\uff00' <= c <= '\uffef'):
            raise SystemExit('carattere a due byte inatteso {!r}'.format(c))
    fuori.append({'file': 'proc.hsp', 'cerca': originale, 'sostituisci': nuova,
                  'motivo': t['motivo']})
    print('{:6d}  {}'.format(t['riga'], nuova.strip()[:100]))

dati = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in fuori).encode('utf-8')
with io.open('lavoro/toppe-128-nomi-mappa.jsonl', 'wb') as f:
    f.write(dati)
print('{} toppe -> lavoro/toppe-128-nomi-mappa.jsonl'.format(len(fuori)))
