# -*- coding: utf-8 -*-
"""Lotto fase4-proc-009: bere, i pozzi, le pergamene e le bacchette
(proc.hsp 6801-7700).

30 rese, zero rinviate.

⚠️ **`valn` e' un `itemname()`** — `proc.hsp:6950`, `:6965`, `:6970` fanno tutti
`valn = itemname(ci)` — quindi porta l'articolo italiano, e davanti gli vale il
divieto di `di`/`da`/`in`/`su` che la guida di stile scrive per `name()`. In
questa zona l'inglese ci mette una preposizione **quattro volte** («from», «in»),
e tutte e quattro le rese cambiano soggetto o verbo:

    en «name(cc) draws water from valn»  ->  «valn disseta name(cc)»
    en «name(cc) falls in valn!»         ->  «valn inghiotte name(cc)!»

E' la stessa scoperta del lotto 005 su `itemname()`, che qui si ripresenta
travestita da variabile: chi guarda solo il nome `valn` non ha modo di saperlo.

⚠️ A :6876 l'inglese non traduce il giapponese, e non ci somiglia nemmeno:
「意識が現実を離れ、幻覚に呑み込まれていく」 e' la coscienza che lascia la realta'
e sprofonda nelle allucinazioni; l'inglese scrive «regretted being born». La riga
scatta su `ITEM_BIT_HAZARD` e fa danno alla mente (`SKILL_RES_MIND`): il
giapponese ha ragione anche secondo il codice.

⚠️ Tre morfologiche diverse da togliere, oltre alle solite `_s()`: `he(cc)` a
:6997 (un argomento solo, quindi morfologia), `his(cc)` a :7394, `your(tc)` a
:7692. A :6997 e a :6994 il nome sta **fuori** da `lang()`, quindi la voce e'
solo la coda e non resta nessuna interpolazione: la resa e' una stringa nuda.

⚠️ «has dried up» a :7165 e :7170 non si puo' rendere con «si e' prosciugato»:
il soggetto e' un `itemname()`, di genere ignoto. «resta a secco» non concorda
con niente. Stesso motivo a :6951, dove «e' a secco» sostituisce «e' asciutto».

💡 Due termini erano gia' decisi e si copiano: 杖/魔杖 -> «bacchetta»
(`text.hsp:189` e `:9656`, piu' quattro voci di `skill.hsp`), «Zap» -> «Agita»
(`text.hsp:135`). E `<Mug of Ehekatl>` e' gia' `<Tazza di Ehekatl>`
(`db_item.hsp:138313`).
"""
import collections, glob, io, json, unicodedata

RESE = {
    # --- bere una pozione
    (6864, ' drink .'):
        'name(tc) + " beve " + itemname(ci, 1) + "."',
    # ⚠️ il giapponese e l'inglese dicono due cose diverse, e il codice
    #    (SKILL_RES_MIND, ITEM_BIT_HAZARD) da' ragione al giapponese.
    (6876, ' regretted being born.'):
        'name(tc) + " perde il contatto con la realtà e sprofonda nelle allucinazioni..."',

    # --- i quattro gradini del bisogno (mod). ⚠️ Niente aggettivi: «irrequieto»
    #     concorderebbe con name().
    (6926, ' is extremely restless and fidgety...'):
        'name(tc) + " si agita senza sosta..."',
    (6929, ' is squirming and writhing in discomfort...'):
        'name(tc) + " si contorce dal disagio..."',
    (6932, ' is desperately holding back urine, trying not to go...'):
        'name(tc) + " si trattiene a fatica dal fare pipì..."',
    (6935, ' is trembling slightly, barely managing to endure the urge to urinate...'):
        'name(tc) + " trema appena e resiste allo stimolo..."',

    # --- i pozzi e le fontane. ⚠️ valn = itemname(ci): porta l'articolo.
    # 💡 COPIATA da action.hsp:6427, stesso giapponese. La mia era «è a secco»:
    #    stessa soluzione allo stesso problema (niente participio che concordi
    #    con valn), parole diverse. Vince quella gia' decisa.
    (6951, ' is dry.'):
        'valn + " non ha più acqua."',
    # «from valn» -> valn diventa il soggetto
    (6966, ' draw water from .'):
        'valn + " disseta " + name(cc) + "."',
    (6971, ' draw water from  by Mug of Ehekatl.'):
        'valn + " disseta " + name(cc) + ", che attinge con la <Tazza di Ehekatl>."',
    # «falls in valn» -> valn diventa il soggetto
    (6988, ' falls in !'):
        'valn + " inghiotte " + name(cc) + "!"',
    # ⚠️ il nome sta fuori da lang() (`txt name(cc) + lang(...)`): questa e' solo
    #    la coda. ごぼぼぼ e' il gorgoglio di chi affoga.
    (6994, ' yells, Huuruulp!?'):
        '" urla, " + cnvtalk("Glu-glu-gluu!?")',
    # ⚠️ `he(cc)` con UN argomento e' morfologia e va tolta; il giapponese non ha
    #    soggetto, quindi non resta nessuna interpolazione.
    (6997, 'Soon  floats up to the surface.'):
        '"Ma torna subito a galla."',
    (7002, " couldn't breathe."):
        'name(cc) + " non riesce più a respirare."',
    (7056, ' find some gold pieces in water.'):
        'name(cc) + " trova delle monete d\'oro nell\'acqua."',
    (7082, ' swallow something bad.'):
        'name(cc) + " ingoia qualcosa che non doveva."',
    (7093, 'Something comes out from the well!'):
        'Dal pozzo salta fuori qualcosa!',
    # ⚠️ il giapponese e' una battuta: la fortuna e' arrivata... o cosi' e'
    #    sembrato. L'inglese tiene solo la prima meta'.
    (7120, 'You feel as a stroke of good fortune passed by.'):
        "Ti sembra che una fortuna sfacciata ti sia passata accanto... ma era solo un'impressione.",
    # ⚠️ «prosciugato» concorderebbe con itemname(ci): «a secco» non concorda.
    (7165, ' has completely dried up.'):
        'itemname(ci) + " resta completamente a secco."',
    (7170, ' has dried up.'):
        'itemname(ci) + " resta a secco."',

    # --- le pergamene e le bacchette
    # «barcolla» e' gia' la resa di ふらり in action.hsp:1842
    (7190, ' stagger.'):
        'name(cc) + " barcolla."',
    (7197, ' read .'):
        'name(cc) + " legge " + itemname(ci, 1) + "."',
    # «Zap» e' «Agita» da text.hsp:135, e il giapponese dice 振った, «ha agitato»
    (7232, ' zap .'):
        'name(cc) + " agita " + itemname(ci, 1) + "."',
    # ⚠️ «replica OF itemname» -> «di » + articolo: l'oggetto diventa diretto
    (7274, ' duplicated replica of .'):
        'name(cc) + " duplica per un istante " + itemname(ci) + "."',
    # 杖 e' «bacchetta» da text.hsp:189 e :9656
    (7335, ' fail to use the power of the rod.'):
        'name(cc) + " non riesce a usare la bacchetta."',
    # ⚠️ `his(cc)` con un argomento e' morfologia e va tolta
    (7394, ' shake  head.'):
        'name(cc) + " scuote la testa."',

    # --- le domande dell'interfaccia: qui il gioco parla a te e basta
    (7488, 'Which direction?'):
        'In che direzione?',
    (7590, "It's out of range."):
        'È fuori portata.',
    (7607, 'Which direction do you want to cast the spell? '):
        'In che direzione vuoi lanciare? ',
    (7610, 'Which direction do you want to zap the wand? '):
        'In che direzione vuoi agitare la bacchetta? ',

    # ⚠️ `your(tc)` e' morfologia e va tolta
    (7692, ' aging process slows down.'):
        'name(tc) + " invecchia più lentamente."',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-009.jsonl'
DA, A = 6801, 7700

tutte = [json.loads(l) for l in io.open('lavoro/_proc.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]
voci = [v for v in zona if (v['riga'], v['en']) not in RINVIATE]

errori = []
for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items():
    if n > 1:
        errori.append(f'rete 0: la chiave {k} identifica {n} voci, non una')
indice = {(v['riga'], v['en']): v for v in voci}
for v in voci:
    if (v['riga'], v['en']) not in RESE:
        errori.append(f"rete 1: voce senza resa -> riga {v['riga']}  en={v['en']!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {(v['riga'], v['en']) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# rete 6: nessuna voce del lotto deve stare su una riga commentata (lotto 006).
sorgente = io.open(r'C:\Games\Elona\_traduzione\build\2.05-custom-gx\proc.hsp',
                   encoding='cp932').read().split('\n')
for v in voci:
    if sorgente[v['riga'] - 1].lstrip().startswith(';'):
        errori.append(f"rete 6: riga {v['riga']} e' commentata nel sorgente, va rinviata")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8, nuova qui: nessuna preposizione che si fonde con l'articolo davanti a
# una variabile che porta un nome. `name()` e `itemname()` le controlla gia' la
# guida di stile a occhio, ma `valn` e' un itemname() sotto falso nome e non lo
# direbbe nessuno guardando la riga.
import re
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
for v in voci:
    resa = RESE[(v['riga'], v['en'])]
    if FONDONO.search(resa):
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a un nome -> {resa}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti 0-2, 6, 7 e 8')

gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[(v['riga'], v['en'])]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it != resa:
            print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
                  f"      qui      {resa!r}\n"
                  f"      {nome}:{riga}  {it!r}")

per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[v['jp']].add(RESE[(v['riga'], v['en'])])
for jp, rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} reso in {len(rese)} modi: {rese}')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[(v['riga'], v['en'])]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
