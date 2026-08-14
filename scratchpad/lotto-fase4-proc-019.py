# -*- coding: utf-8 -*-
"""Lotto fase4-proc-019: le azioni speciali di fine file — plagio, ipnosi,
scansione dati, trasfusione, ensemble, pesca dimensionale, origami
(proc.hsp 18000-19999).

38 rese, nessuna rinviata. `proc.hsp` passa a 838 su 1.098 (76%).

⚠️⚠️ **Quattro righe dove l'inglese nomina il PERSONAGGIO SBAGLIATO**, e ogni
volta il giapponese e il codice dicono la stessa cosa contro di lui. La serie
degli errori di monte sale da quindici a **diciannove**, ed e' la famiglia gia'
vista alla 35ª (`:6200`, `name(tc)` per `name(cc)`) e alla 37ª (`:14021`, «dice
`cc` dove il `cbitmod` sotto fa `tc`).

| riga | l'inglese dice | il giapponese e il codice dicono |
|---|---|---|
| `:18280` | `name(tc)` | `name(CHARA_PLAYER)`, e la riga sopra scrive in `cdata(cnt, CHARA_PLAYER)`: e' **il giocatore** che si toglie l'equipaggiamento |
| `:18309` | `name(tc)` | `name(cc)`: in `SKILL_SPACT_LOVE_CRAFTING` chi mostra la follia e' **chi agisce**, e i bersagli arrivano nel `repeat` sotto |
| `:18429` | `name(tc)` | `name(cc)`: identico, in `SKILL_SPACT_MIASMA_OF_HELL` |
| `:18744` | `name(tc)` | `name(0)`, e le due righe sopra toccano solo `cdata(..., CHARA_PLAYER)`: la modalita' di lancio e' **sempre** del giocatore |

⚠️ **E `:18280` mostra il limite della rete 11 meglio di qualunque esempio
finora.** La rete pretende che le funzioni di contenuto della resa coincidano
con quelle dell'**inglese**, e l'inglese qui ha **un** `name()` mentre il
giapponese ne ha **due** (il giocatore e chi dà l'ordine). Quindi la resa non
puo' nominarli tutt'e due, anche sapendo che il giapponese ha ragione: nomina
il giocatore — il soggetto, quello che il codice conferma — e l'ordine resta
implicito («obbedendo all'ordine»). E' la stessa forma di `:10312` della 36ª,
ma rovesciata: li' l'inglese aveva **meno** contenuto per scelta, qui per
errore.

⚠️ **`:19178` e' la trappola `performerpal`, trovata stamattina e schivata.**
`proc.hsp:19167` fa `performerpal = "your friends"` fuori da `lang()` e `:19178`
lo interpola: reso sul giapponese, che non lo usa. E' il gemello esatto di
`studybuddy` (`:16980`/`:16991`) del lotto 017 — stessa struttura, stessa frase,
stesso letterale. Vedi `scratchpad/variabili_en.py`.

⚠️ **Sette rese girano la frase per non far concordare un participio**, e cinque
di queste avrebbero anche fatto scattare la rete 8. Il caso piu' stretto e'
`:19102`, la trasfusione: l'inglese dice «from X to Y» e in italiano tutt'e due
le preposizioni si fondono con l'articolo che `name()` porta dentro. La resa
mette **i tre nomi come soggetti** — «X trasfonde il sangue: lo cede Y e lo
riceve Z» — che e' la stessa strada del genitivo della 37ª, applicata a due
complementi invece che a uno.

💡 **Tredici nomi vengono da `skill.hsp` e `buff.hsp`, nessuno e' inventato**:
Ipnosi collettiva, Onda psichica, Canto di rovina, Miasma infernale,
Provocazione, Scansione dati, Trasfusione diretta, Ensemble, Pesca dimensionale,
spiriti delle carte, Plagio, costrizione, supergravità.

💡 **Tre rese sono copie e tre no, e la differenza la fa il giapponese.**
`:19867` copia `action.hsp:12040` («Non se ne possono soggiogare più di
quindici.»), stesso giapponese. Ma `:19303` e `:19307` hanno lo **stesso inglese**
di `proc.hsp:5332` e `:5063` e un giapponese **diverso**: «A waste of time...» sta
per 「釣れる獲物がいないようだ…。」 (qui non c'e' pesce) e per un'altra frase
altrove, e 「亜空釣り」 e' la **Pesca dimensionale** (`skill.hsp:1608`), non la
pesca normale. Copiare sull'inglese avrebbe perso tutt'e due le distinzioni.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- Fiamma di Megiddo. 祝福を焼き尽くす: brucia le benedizioni.
    (18061, ' released a wave of dispelling flames.'):
        'name(cc) + " libera un\'onda che incenerisce le benedizioni."',
    # «bloccato» concorderebbe con tc: la costrizione diventa soggetto.
    # 束縛 -> «costrizione» (action.hsp:9515, la riga che la scioglie)
    (18115, '  bound.'):
        '"La costrizione avvolge " + name(tc) + "."',
    (18189, "You'll not escape..."):
        'Ehehe... ahahahahah! Non ti lascio scappare...',
    # Ipnosi collettiva (skill.hsp:1796)
    (18223, ' spread hypnotism extensively!'):
        'name(cc) + " diffonde l\'ipnosi tutt\'intorno!"',
    # ⚠️ l'inglese dice name(tc), il giapponese e il codice dicono
    #    CHARA_PLAYER. E la rete 11 concede UN name(): nomina il soggetto.
    (18280, '  brainwashed into removing  equipment.'):
        'name(CHARA_PLAYER) + " si toglie l\'equipaggiamento, obbedendo all\'ordine."',
    # ⚠️ «di name(cc)» si fonderebbe: il nome diventa soggetto.
    #    洗脳 -> «lavaggio del cervello» (skill.hsp:1797)
    (18289, "You resist 's brainwashing."):
        'name(cc) + " prova a lavarti il cervello, ma resisti."',
    (18296, " resists 's brainwashing."):
        'name(cc) + " prova a lavare il cervello, ma " + name(tc) + " resiste."',
    # ⚠️ reso su name(cc): l'inglese dice tc, ma chi agisce e' cc
    (18309, ' showed off glimpses of a horrifying madness...how blasphemous!'):
        'name(cc) + " lascia intravedere la follia che nasconde... che bestemmia!"',
    # Onda psichica (skill.hsp:1544)
    (18353, '  emitted intense spiritual wave!'):
        'name(cc) + " libera un\'onda psichica violentissima!"',
    # Canto di rovina (skill.hsp:1576)
    (18390, ' sang doom loudly.'):
        'name(cc) + " intona a gran voce il canto di rovina."',
    # ⚠️ reso su name(cc), come sopra. Miasma infernale (buff.hsp:187)
    (18429, ' emanated miasma of hell.'):
        'name(cc) + " libera il miasma infernale."',
    (18469, ' emanated blades of wind.'):
        'name(cc) + " libera lame di vento."',
    (18545, ' aim at nearby enemies.'):
        'name(cc) + " prende di mira i nemici intorno."',
    # ⚠️ reso su name(0): le due righe sopra toccano solo CHARA_PLAYER
    (18744, ' switched the casting mode.'):
        'name(0) + " cambia modalità di lancio."',
    (18752, ' noticed  was being analyzed and changed  behavior.'):
        'name(tc) + " capisce di essere sotto analisi e cambia movenze."',
    # ⚠️ «a name(sctc)» e «da name(sctc)» si fondono: il secondo nome diventa
    #    soggetto di una relativa. Scansione dati (buff.hsp:267)
    (18782, ' took over the data scan from .'):
        'name(tc) + " eredita la scansione dati che " + name(sctc) + " aveva cominciato."',
    (18846, "Flames began to burst out all over 's body."):
        'name(tc) + " erutta fiammate da ogni giuntura."',

    # --- Chiama o ferma un alleato (skill.hsp:1205).
    (19030, 'You order  to wait in town.'):
        '"Hai lasciato " + cdatan(CDATAN_NAME, rc) + " ad aspettare in città."',
    # il giapponese dice 呼び出せない (non si può richiamare), non «invitare»
    (19056, "Your party is already full. You can't invite someone anymore."):
        'Hai già il massimo di compagni: non puoi richiamarne altri.',
    (19060, 'You can not use it in Abnormal mode...'):
        'In questa modalità non si può usare...',
    # ⚠️ il nome sta FUORI da lang(): `cnven(cdatan(...)) + lang(...)`. La resa
    #    e' la coda della frase e comincia con lo spazio, come l'inglese.
    (19066, '  appeared out of nowhere.'):
        '" appare dal nulla."',

    # --- Trasfusione diretta (skill.hsp:1284).
    (19081, 'Choose a blood transfusion source.'):
        'Prima devi scegliere da chi prendere il sangue.',
    (19093, 'Choose a blood transfusion destination.'):
        'Adesso scegli a chi darlo.',
    # ⚠️ «da name(rc)» e «a name(tc)» si fondono tutt'e due: i tre nomi
    #    diventano soggetti.
    (19102, ' transfused blood from  to .'):
        'name(cc) + " trasfonde il sangue: lo cede " + name(rc) + " e lo riceve " + name(tc) + "."',

    # --- Ensemble (skill.hsp:1172).
    (19135, 'Ensemble!'):
        'Ensemble!',
    # ⚠️ reso sul giapponese: `performerpal` porta «your friends» in inglese
    #    nudo (:19167). E' il gemello di studybuddy del lotto 017.
    (19178, 'You started the ensemble with .'):
        '"Tu e i tuoi compagni cominciate l\'ensemble."',
    # famiglia di action.hsp:8536, stesso giapponese su un'altra variabile
    (19212, '  ready!'):
        'name(cc) + " si prepara a combattere!"',
    (19256, 'If you attack any more, the opponent will die...'):
        'Ancora un colpo e ci scappa il morto...',

    # --- Pesca dimensionale (skill.hsp:1608). ⚠️ Stesso inglese di
    #     proc.hsp:5332 e :5063, giapponese diverso: non si copia.
    (19303, 'A waste of time...'):
        'Non sembra esserci niente da pescare...',
    (19307, 'You start fishing.'):
        'Cominci la pesca dimensionale.',

    (19453, ' swung down the mass of super gravity.'):
        'name(cc) + " abbatte una massa di supergravità."',
    (19518, 'An expanse of ocean and fog spreads out.'):
        'Con la nebbia, tutt\'intorno si apre il mare.',
    # ヴァモス・カンタール e' spagnolo anche in giapponese: resta com\'e'
    (19582, 'This is my song!'):
        'Vamos, cantar!',

    # --- Provocazione (skill.hsp:1188).
    (19715, ' provokes the enemy.'):
        'name(cc) + " lancia una provocazione."',
    (19779, ' fell for the provocation.'):
        'name(tc) + " abbocca alla provocazione!"',

    # --- ShikiOrigami e le carte.
    # copiata da action.hsp:12040, stesso giapponese
    (19867, 'You can not control more than 15 origami.'):
        'Non se ne possono soggiogare più di quindici.',
    (19870, 'Which spellbook to use?'):
        'Quale grimorio consumare?',
    # カード精霊 -> «spiriti delle carte» (skill.hsp:1489)
    (19996, 'Requires 5 card spirits.'):
        'Servono 5 spiriti delle carte.',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-019.jsonl'
DA, A = 18000, 19999
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
