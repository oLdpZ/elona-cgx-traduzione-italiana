# -*- coding: utf-8 -*-
"""Lotto fase4-proc-026: i tre sguardi, la voce, le pozioni, lo zaino e il menu
delle tattiche (proc.hsp 26000-26999).

34 rese, nessuna rinviata. ⭐ **Con questo `proc.hsp` e' CHIUSO**: 1.091 firme
su 1.098, e le 7 che restano sono tutte rinviate apposta. E' il settimo file
del progetto a chiudersi, dopo `db_item`, `item_data`, `skill`, `action`,
`text`, `db_creature`, `buff` e `chips`.

⭐ **E' anche il lotto con la percentuale di copie piu' alta del file: dodici su
trentaquattro hanno il giapponese gia' reso altrove**, e otto vengono da un
posto solo — `action.hsp:15232`-`:15313`, il **menu delle tattiche**, che
`proc.hsp:26858`-`:26986` ristampa parola per parola. E' l'X-Frame del lotto
018 in grande: il mod scrive la stessa sequenza da due punti, e la seconda volta
non si ridecide niente. 💡 `dossier.py` le ha pescate tutte e dodici senza che
servisse cercarle.

⚠️⚠️ **Un inglese solo per TRE giapponesi diversi, ed e' il record del
progetto.** `:26080`, `:26120` e `:26158` hanno tutt'e tre
«`name(cc) + " gaze" + _s(cc) + " " + name(tc) + "."`», e sono **tre azioni
speciali diverse**: `SKILL_SPACT_EYE_OF_MANA` (「魔力を込めて睨み付けた」, e il
codice fa `dmgcon CONDITION_MPOISON`), `..._EYE_OF_ILLUSION` (「幻影を見せた」,
danno `SKILL_RES_MIND`) e `..._EYE_OF_STIFFEN` (「妖しい眼光を放った」, danno
`SKILL_RES_NERVE` piu' `CONDITION_BIND`). L'inglese ha appiattito tre effetti in
una riga sola; il giapponese e il codice li distinguono, e la resa li segue. La
rete 13 e' nata nella 37ª su una coppia: qui trova una terna.

⚠️ **`:26940` e' una STATICA il cui giapponese interpola un nome.**
`lang(cdatan(CDATAN_NAME, tc) + "は矢弾を装備していない。", "You need to equip
ammo.")`: il ramo giapponese nomina il personaggio, quello inglese no, e
`estrai.py` classifica sul ramo che la resa sostituisce. Quindi la resa e'
**testo nudo** — «Devi equipaggiare le munizioni.» — e **non** puo' portare il
nome, anche se il gemello `action.hsp:15268` ce l'ha, perche' li' l'inglese era
dinamico. Stessa riga, due tipi diversi, due rese diverse: la decide il tipo,
non il senso.

💡 **`:26948` e' la stessa cosa portata all'estremo**: il giapponese dice
「name は <tipo> に切り替えた。」, l'inglese dice **«Current Ammo Type»** e
basta. Il tipo di munizione che `:26945` prepara in `s` — «Normali» /
«Illimitate» — nel ramo inglese **non compare da nessuna parte**: e' upstream
che butta via l'informazione, e la resa italiana non puo' rimetterla.

⚠️ **Sette rese girate per non far fondere una preposizione con `name()` o
`itemname()`**, e una di queste ne aveva **due nella stessa frase**: `:26347`,
«la voce **di** X risuona nel cuore **di** Y», risolta con i due nomi
soggetti — «X fa risuonare la voce, e Y la sente nel cuore!». Piu' «il corpo
di» (`:26166`), «l'occhio di» (`:26228`), «lo zaino di» (`:26598`, col **-ne
enclitico** della 37ª) e «il tanfo da » + `itemname()` (`:26637`, con l'oggetto
che diventa soggetto della seconda meta').

💡 **`:26301` e' un finto messaggio di sistema, e va lasciato rotto**:
「[システム]原因不明のエラーによりglobaltcda…」 e' un glitch di trama, troncato
a meta' apposta. Reso troncato uguale.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- l'insulto e i tre sguardi. 罵倒 e' «Insulto» in skill.hsp:1052
    (26002, ' insult .'):
        'name(cc) + " copre d\'insulti " + name(tc) + "."',
    # ⚠️ i tre sguardi hanno lo STESSO inglese e tre giapponesi diversi:
    #    Occhio del mana, Occhio dell'illusione, Occhio dell'irrigidimento
    (26080, ' gaze .'):
        'name(cc) + " fissa " + name(tc) + " con lo sguardo carico di magia."',
    (26120, ' gaze .'):
        'name(cc) + " avvolge " + name(tc) + " in un\'illusione."',
    (26158, ' gaze .'):
        'name(cc) + " trafigge " + name(tc) + " con un\'occhiata sinistra."',
    # «Il corpo di » + name() fonde, e «irrigidito» concorderebbe con tc
    (26166, 'Body of   stiff like a stone.'):
        'name(tc) + " ha il corpo rigido come la pietra."',
    # «l'occhio di » + name() fonde: il nome resta soggetto
    (26228, "'s eye shot a dazzling light."):
        'name(cc) + " sprigiona dagli occhi una luce accecante!"',

    # --- Maile e l'errore di sistema.
    (26296, "Hmmm. I guess I can't exert my full power without your consent."):
        'Ngh... Senza il tuo consenso non riesco a esprimere tutta la mia forza.',
    # finto messaggio di sistema, troncato apposta: si tiene tronco
    (26301, '[System]By unknown error, globalda...'):
        '[Sistema]Errore di origine ignota in globalda...',

    # --- la voce e il lampo.
    # «la voce di » e «il cuore di » fondono tutt'e due: i due nomi diventano
    # soggetti, come le parate del lotto 015
    (26347, 'The voice of  echoes in the mind of !'):
        'name(cc) + " fa risuonare la voce, e " + name(tc) + " la sente nel cuore!"',
    # copiata da proc.hsp:2354
    (26393, ' became too tired to fight and quietly went away.'):
        'name(tc) + " si stanca di combattere e se ne va in silenzio."',
    (26437, ' slammed the dazzling light to !'):
        'name(cc) + " scaglia contro " + name(tc) + " un lampo accecante!"',

    # --- le pozioni.
    # «assonnato» concorderebbe con tc
    (26471, ' drowsiness fades away.'):
        'name(tc) + " ha meno sonno."',
    # copiata da action.hsp:10575 e proc.hsp:15141
    (26563, '  surrounded by flames.'):
        'name(tc) + " prende fuoco."',
    # 状態異常 sono gli «stati» di buff.hsp:430
    (26573, '*Munch munch*... *Gulp*! Wow! All status conditions were cured!'):
        '*Sgranocchia*... *gulp*! Incredibile! Tutti gli stati alterati sono spariti!',

    # --- il saccheggio dello zaino.
    # «lo zaino di » + name() fonde: il -ne enclitico della 37ª
    (26598, ' loot  backpack.'):
        'name(cc) + " punta " + name(tc) + " e ne rovista lo zaino."',
    # his(tc) a un argomento e' morfologia: sparisce
    (26631, ' protect  food.'):
        'name(tc) + " difende le sue provviste."',
    # «da » + itemname() fonde: l'oggetto diventa soggetto della seconda meta'
    (26637, ' notice unusual odor from  and step back.'):
        'name(cc) + " ritira la mano: " + itemname(ci, 1) + " manda un tanfo strano."',
    (26644, ' eat !'):
        'name(cc) + " si mangia " + itemname(ci, 1) + "!"',

    # --- la tasca quadridimensionale (skill.hsp:774).
    (26696, 'You summon a 4-dimensional pocket.'):
        'Evochi la tasca quadridimensionale.',
    (26699, 'The mirror led to the 4th dimension.'):
        'Lo specchio si è aperto sulla quarta dimensione.',

    # --- l'istruzione individuale.
    (26784, 'Who will you lead?'):
        'Chi vuoi istruire?',
    # copiata da action.hsp:9947
    (26791, 'Out of range.'):
        'È fuori portata.',
    (26801, "It's too late to lead."):
        'Ormai è troppo tardi.',
    (26806, 'There seems to be no need for leading.'):
        'Non sembra avere bisogno di istruzioni.',

    # --- il menu delle tattiche, tutto copiato da action.hsp:15232-15313.
    (26858, 'Which instruction should I give my allies?'):
        'Che ordini do ai compagni?',
    (26910, ' switched to offensive mode!'):
        'name(tc) + " passa in assetto d\'assalto!"',
    (26914, ' switched to defensive mode!'):
        'name(tc) + " passa in assetto difensivo!"',
    (26918, ' switched to intercept mode!'):
        'name(tc) + " passa in assetto d\'intercettazione!"',
    (26922, ' switched to talking mode!'):
        'name(tc) + " passa in assetto di trattativa!"',
    # ⚠️ STATICA: il giapponese interpola cdatan(), l'inglese no, e la resa
    #    sostituisce il ramo inglese. Niente nome, come vuole il tipo
    (26940, 'You need to equip ammo.'):
        'Devi equipaggiare le munizioni.',
    (26945, 'Normal'):
        'Normali',
    (26945, 'Unlimited'):
        'Illimitate',
    (26948, 'Current Ammo Type'):
        'Tipo di munizione attuale',
    (26986, " isn't capable of using that ammo."):
        'itemname(ci) + " non regge quel tipo di munizione."',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-026.jsonl'
DA, A = 26000, 26999
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
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
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
