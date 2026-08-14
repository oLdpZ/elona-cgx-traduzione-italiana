# -*- coding: utf-8 -*-
"""Lotto fase4-proc-016: fuga e ritorno, veleni, maledizioni, terreni, artefatti
(proc.hsp 14500-15499).

49 rese, nessuna rinviata. `proc.hsp` passa a 709 su 1.098 (65%).

⚠️ **Zona a rischio d'accordo come poche**: undici rese descrivono qualcosa che
**succede a** `tc`, e l'inglese le scrive tutte col participio («is hit by
poison», «was showered by acid», «is dominated»). In italiano il participio
concorderebbe col personaggio, che puo' essere «il putit» o «la strega». La
strada, presa undici volte, e' **rovesciare la frase**: il veleno, l'inchiostro,
il torpore, l'acido diventano **soggetto**, e il nome resta complemento oggetto —
«Il veleno investe X», «Il torpore prende X».

⚠️ **`:14521` e `:14573` hanno lo stesso inglese e due giapponesi diversi**, e a
sbagliare e' l'inglese: dice «The air around you gradually loses power» in
tutt'e due, mentre il giapponese distingue 「脱出を中止した」 (la **fuga**, il
`SKILL_SPELL_ESCAPE`) da 「帰還を中止した」 (il **ritorno**, il
`SKILL_SPELL_RETURN`). Sono due incantesimi diversi, con due pergamene diverse
(`db_item.hsp:144021` «fuga», `:149602` «ritorno»), e l'inglese li appiattisce
su una frase che per giunta non dice quello che dicono: e' il decimo errore di
monte della serie. Rese sul giapponese.

⚠️ **`:14673` e' l'undicesimo**: il giapponese dice 「ひどい頭痛におそわれた」 —
un mal di testa — e l'inglese «A foul stench floods his nostrils», un tanfo.
L'effetto e' `CONDITION_CONFUSE` e il codice non arbitra fra i due; il
giapponese e' la lingua d'origine, e vince.

💡 **Sette rese sono copie**: `:14856` («Non si puo' usare in quest'area.»,
`action.hsp:10848`), `:14931` («In questo luogo non ha effetto.»,
`action.hsp:8552`), `:15141` («prende fuoco», `action.hsp:10575`), `:15454` (la
trasformazione dei materiali, `action.hsp:12474`), `:14562` che rifa' il
parallelo di `proc.hsp:6291`, e i nomi di creatura di `action.hsp` per le quattro
sorelle e il maggiordomo.

⚠️ **`:14931` porta anche una divergenza vecchia che NON si tocca.** Lo stesso
giapponese 「この場所では効果がない。」 e' reso «Qui non funziona.» a
`action.hsp:196` e «In questo luogo non ha effetto.» a `:8552`. Non e' una
decisione presa due volte: e' **l'inglese** che li distingue («This doesn't work
in this area» contro «The effect doesn't work in this area»), e `:196` sta accanto
a `:179`, che ha un giapponese diverso e la stessa resa breve. Qui la voce ha
l'inglese di `:8552`, e prende la resa di `:8552`.

⚠️ **`valn` a `:14755` e `:14766` viene da `itemname(i, 1, 1)`** (riga 14752),
non da `skillname` come nel lotto 014: e' un nome di oggetto, e la rete 8 ha
ragione a non volerci una preposizione davanti. Le due rese girano la frase e
mettono l'oggetto come soggetto — «X, che Y porta addosso, brilla di luce nera».

💡 **La battuta di `:14894` e' Vonnegut, e il gioco la cita due volte.** E'
l'ultima riga di *Ghiaccio-nove* — «Live by the foma that make you brave and kind
and healthy and happy» — e la creatura che la porta, `wrang-wrang`, in
`db_creature.hsp:85936` e' gia' «il guardiano del **karass**», l'altra parola
bokononista. Resa coi nomi al posto degli aggettivi («ti danno coraggio,
gentilezza, salute e felicita'») perche' «coraggioso» concorderebbe col
giocatore, che puo' essere donna.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- fuga e ritorno. 脱出 -> «fuga» (db_item:144021), 帰還 -> «ritorno»
    #     (:149602). ⚠️ L'inglese confonde i due: vedi la nota in cima.
    (14521, 'The air around you gradually loses power.'):
        'Hai annullato la fuga.',
    (14527, 'Returning while taking a quest is forbidden. Are you sure you want to return?'):
        'Fuggire mentre hai un incarico in corso è vietato dalla legge. Fuggire lo stesso?',
    (14533, 'The air around you becomes charged.'):
        'L\'aria intorno comincia a vibrare.',
    # reso sul giapponese: l'inglese parla del signore del sotterraneo, il
    # giapponese della missione di questo piano, ed e' quello che si perde
    (14537, 'The lord of the dungeon might disappear if you escape now.'):
        'Uscendo adesso, la missione di questo piano non si potrà più completare...',
    # il parallelo di proc.hsp:6291, che dice la stessa cosa per la fuga
    (14562, 'It seems that you cannot return from this floor.'):
        'Da questo piano sembra impossibile tornare indietro.',
    (14567, "There's no place to return to."):
        'Non c\'è nessun posto dove tornare.',
    (14573, 'The air around you gradually loses power.'):
        'Hai annullato il ritorno.',

    # --- il mana. ⚠️ «pieno» era falso in tutt'e due i siti: vedi
    #     scratchpad/correzione-mana.py
    (14597, ' mana is restored.'):
        'name(tc) + " recupera mana."',
    (14607, ' absorb mana from the air.'):
        'name(tc) + " assorbe il mana dall\'aria."',

    # --- i cinque malanni. Il participio inglese concorderebbe con tc: la
    #     sostanza diventa soggetto e il nome complemento oggetto.
    (14647, '  hit by poison!'):
        '"Il veleno investe " + name(tc) + "!"',
    (14665, 'Ink squirts into  face!'):
        '"Uno schizzo d\'inchiostro colpisce " + name(tc) + " in faccia!"',
    # reso sul giapponese: 頭痛 e' il mal di testa, non il tanfo dell'inglese
    (14673, 'A foul stench floods  nostrils!'):
        '"Un mal di testa tremendo assale " + name(tc) + "!"',
    (14681, ' get numbness!'):
        '"Il torpore prende " + name(tc) + "!"',
    (14689, 'Strange sweet liquid splashes onto !'):
        '"Uno strano liquido dolciastro inzuppa " + name(tc) + "!"',

    # --- la maledizione
    (14703, ' point  and mutter a curse.'):
        'name(cc) + " punta il dito contro " + name(tc) + " e mormora una maledizione."',
    (14716, 'Your prayer nullifies the curse.'):
        'La tua preghiera annulla la maledizione.',
    # ⚠️ qui valn = itemname(i, 1, 1), un nome di oggetto: niente preposizione
    #    davanti. La frase gira e l'oggetto diventa soggetto.
    (14755, '  resisted the curse.'):
        '"La maledizione non intacca " + valn + ", che " + name(tc) + " porta addosso."',
    (14766, '  glows black.'):
        'valn + ", che " + name(tc) + " porta addosso, brilla di luce nera."',

    # --- i diari che chiamano qualcuno. I nomi di creatura vengono da
    #     action.hsp: 妹猫 «la sorella gatta minore», 姉犬 «la sorella cane
    #     maggiore», 嬢 «la giovane dama», 執事 «il maggiordomo».
    (14820, 'The owner of the diary appears.'):
        'Il padrone del diario si presenta.',
    # copiata da action.hsp:10848, stesso giapponese
    (14856, "You can't use it in this area."):
        'Non si può usare in quest\'area.',
    (14870, 'How...! You suddenly get a younger cat sister!'):
        'Ma guarda: avevi una sorella gatta minore, persa da tempo e senza legami di sangue!',
    (14874, 'How...! You suddenly get a younger sister!'):
        'Ma guarda: avevi una sorella minore, persa da tempo e senza legami di sangue!',
    (14878, 'A young lady falls from the sky.'):
        'Una giovane dama cade dal cielo!',
    (14882, 'A butler falls from the sky.'):
        'Un maggiordomo cade dal cielo!',
    (14886, 'How...! You suddenly get an older sister!'):
        'Ma guarda: avevi una sorella maggiore, persa da tempo e senza legami di sangue!',
    (14890, 'How...! You suddenly get an older dog sister!'):
        'Ma guarda: avevi una sorella cane maggiore, persa da tempo e senza legami di sangue!',
    # ⚠️ Vonnegut, *Ghiaccio-nove*. «coraggioso» concorderebbe col giocatore:
    #    i nomi no. `karass` e' gia' in db_creature.hsp:85936.
    (14894, 'Live by the foma that make you brave and kind and healthy and happy.'):
        'Vivi secondo i foma che ti danno coraggio, gentilezza, salute e felicità.',

    # --- il dominio
    # copiata da action.hsp:8552, stesso giapponese e stesso inglese
    (14931, "The effect doesn't work in this area."):
        'In questo luogo non ha effetto.',
    (14946, ' never obeys.'):
        'name(tc) + " non si unisce a te."',
    (14984, "'s movement was dominated."):
        'name(tc) + " perde il controllo del corpo."',

    # --- i terreni. 蜘蛛の巣 -> «ragnatela», 霧 -> «nebbia», エーテル -> «etere»
    (15021, 'The air is wrapped in a dense smoke.'):
        'Un fumo nero copre la zona.',
    (15027, 'The ground is covered with thick webbing.'):
        'Le ragnatele coprono il terreno.',
    (15030, 'The air is wrapped in a dense fog.'):
        'Una fitta nebbia di tenebra copre la zona.',
    (15034, 'The air is wrapped in dazzling light.'):
        'Una nebbia di luce abbagliante copre la zona.',
    (15038, 'Acid puddles are generated.'):
        'Si formano pozze d\'acido.',
    (15042, 'Walls of fire come out from the ground.'):
        'Dal terreno si levano colonne di fuoco.',
    (15046, 'Ether mist spreads.'):
        'Si spande una nebbia di etere.',
    (15135, '  showered by a large amount of acid.'):
        '"Una gran quantità d\'acido investe " + name(cnt) + "."',
    # copiata da action.hsp:10575, stesso giapponese
    (15141, '  surrounded by flames.'):
        'name(cnt) + " prende fuoco."',

    # --- gli artefatti e i materiali
    (15167, 'What do you want to name this artifact?'):
        'Che nome vuoi dare a questo artefatto?',
    (15178, "It's now called ."):
        '"Adesso si chiama " + listn(0, p) + "."',
    (15198, 'This item has no room for improvement.'):
        'Quell\'oggetto non si può migliorare oltre.',
    # «diventato» concorderebbe con l'oggetto, che qui non e' nominato
    (15245, 'It becomes .'):
        '"Adesso è " + itemname(ci, 1) + "."',
    (15285, 'More magic power is needed to reconstruct an artifact.'):
        'Non c\'è potere magico a sufficienza per rigenerare un artefatto.',
    (15289, '  is reconstructed.'):
        'name(cc) + " vede " + itemname(ci, 1, 1) + " rigenerarsi."',
    # copiata da action.hsp:12474, stesso giapponese e stesso inglese
    (15454, '  transforms into .'):
        'name(cc) + " trasforma " + s + " e ne esce " + itemname(ci, 1) + "."',

    # --- l'eredita'. «riconosciuto» concorderebbe col giocatore.
    (15482, 'You claim the right of succession. (+)'):
        '"Hai ottenuto il diritto di eredità (+" + p + ")"',
    (15483, 'You can now inherit  items.'):
        '"Adesso puoi ereditare " + gdata(GDATA_HEIR_DEED) + " oggetti."',
    (15489, 'You need to read it while you are in the local map.'):
        'Va letto fuori dalla mappa del mondo.',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-016.jsonl'
DA, A = 14500, 15499
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\proc.hsp'

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

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006) o dentro un blocco (lotto 014).
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)
for v in voci:
    if sorgente[v['riga'] - 1].lstrip().startswith(';'):
        errori.append(f"rete 6: riga {v['riga']} e' commentata nel sorgente, va rinviata")
    elif v['riga'] in SPENTE:
        errori.append(f"rete 6: riga {v['riga']} sta dentro un commento di BLOCCO, va rinviata")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[(v['riga'], v['en'])]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].rstrip().endswith(' and'):
        resa = RESE[(v['riga'], v['en'])].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[(v['riga'], v['en'])]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[(v['riga'], v['en'])]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[(v['riga'], v['en'])])
        if attese != trovate:
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


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
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v))].add(parole(RESE[(v['riga'], v['en'])]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`, dove «The air around you
# gradually loses power» sta per 「脱出を中止した」 e per 「帰還を中止した」, cioe'
# per due incantesimi diversi. Referto da leggere, non errore: due giapponesi
# possono anche dire davvero la stessa cosa.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[(v['riga'], v['en'])]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
