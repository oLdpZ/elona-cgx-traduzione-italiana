# -*- coding: utf-8 -*-
"""Lotto fase4-main-011: la nascita e la lotteria (main.hsp, 6285-6431).

Sedici rese, due eventi con lo sfondo dipinto: il figlio che nasce da un
compagno, e la dea della ricchezza che porta la scatola dei biglietti.

⚠️⚠️⚠️ **«figlio di X» non si puo' scrivere, e la rete 8 ha ragione.**
`:6324` compone il nome del neonato come `cdatan(CDATAN_NAME, ccbk) + "の息子"`,
inglese `"son of " + cdatan(...)`. In italiano la forma naturale sarebbe «figlio
di » + nome, ma `contratto-nomi.md` §4 dice che **l'articolo lo porta il nome**:
`ccbk` e' la madre, cioe' un compagno **qualunque** rimasto incinta
(`CDATA_PREGNANCY_MALE_CHILD` a `:6310`), e il suo nome puo' benissimo essere «la
tigre bianca». «figlio di la tigre bianca» e' esattamente quel che la rete 8
esiste per fermare, e non e' un falso positivo.
✅ La strada e' quella che il progetto ha gia' preso **109 volte** per i costrutti
con `of`: il nome davanti, la specificazione dietro. Qui pero' l'apposizione
nuda («la tigre bianca il figlio») direbbe che la madre e' il figlio, quindi la
giuntura e' un **due punti**, che e' punteggiatura da etichetta e non chiede
nessun accordo: `{la tigre bianca: figlio}`, `{Anna: figlio}`.
💡 Il nome resta comunque **piu' informativo dell'inglese**, che sull'articolo
non ha il problema solo perche' in inglese l'articolo non c'e'.

⚠️⚠️ **Le due parentesi non si traducono, e il motivo e' che upstream ne usa
due paia diverse.** `:6325` avvolge il nome del neonato in `lang("《", "{")`, e
`module.hsp:264` rende gli **stessi due caratteri giapponesi** con `<` e `>`.
Non e' una contraddizione da sanare: in Elona `{ }` marca le creature **nate in
partita** e `< >` le uniche, ed e' l'inglese di monte a tenerli separati.
Uniformarli renderebbe un figlio indistinguibile da un boss. Dichiarati in
`invariati.md`, con il motivo.
💡 E' la stessa domanda di sempre — *quale delle due lingue di monte sa la cosa
che serve* — su un carattere invece che su una frase: il giapponese qui **non**
distingue, l'inglese si'.

⚠️ **Due titoli seguono il giapponese contro un inglese piu' povero.** `:6425` e'
「星の光」, *la luce delle stelle*, e l'inglese scrive «Result», che e' l'etichetta
di un tabellone; il testo sotto parla di biglietti che si fanno polvere di luce.
E `:6408`-`:6410` sono in giapponese tre **modi di scegliere** («scelgo pregando»,
«il primo che mi capita in mano», «frugo finche' uno non mi ispira»), mentre
l'inglese le ha riscritte come tre esclamazioni scollegate. Le voci di un menu
dicono che cosa si sta per fare: si segue il giapponese.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :7003 il carico perduto rientrando col carretto troppo pesante.
    (7003, 'You lost .'):
        '"Hai perso " + itemname(cnt) + "."',

    # --- :7028 EVENT_KILL_MOTHER: chi gioca ha ucciso la madre di <Pael>, e
    # <Pael> diventa ostile (`CDATA_RELATION = -3` subito sotto).
    # ⚠️ Il giapponese scrive 「パエル「…」」, cioe' NOMINA chi parla, e l'inglese
    # no. Qui l'inglese ha ragione: `:7027` fa `chatc@DP = tc`, che il nome lo
    # mostra gia'. E la voce sta dentro `cnvtalk()`, che le virgolette le mette
    # da se': un nome scritto qui finirebbe **dentro** le virgolette.
    (7028, 'M-mom...!!'):
        'Mammaaaa!!',

    # --- :7079-:7087 <Leold> riconosce chi gioca come Fattore Decisivo.
    (7079, 'You passed!'):
        'Hai passato la prova!',
    # ⚠️ 決戦因子 si fissa qui, e vale per venti righe. Vedi la lezione in cima.
    (7083, "You've shown you have suitable strength to be considered the Deciding "
           'Factor in a decisive battle.'):
        'Hai dimostrato la forza che si addice al Fattore Decisivo.',
    (7087, 'As you are now, you might even be able to defeat the God of Chaos... '
           "No, I'm certain you can!"):
        'Così forse puoi abbattere perfino il dio del caos... '
        'anzi, ci riuscirai di sicuro!',

    # --- :7102-:7136 Tezcatlipoca.
    (7102, "Let's fight as you wish!!"):
        'E va bene: combatteremo, come volevi!',
    # ⚠️ Non e' una battuta di chi gioca: dopo il menu delle tre risposte,
    # `:7137` suona SOUNDLIST_PUNISH1 e `:7141` toglie due quinti dei punti
    # vita **al giocatore**. La risposta e' un colpo.
    (7136, 'This is my reply!!'):
        'Ed ecco la mia risposta.',

    # --- :7173 la legge dei ninja. Qui il nome di chi parla ci sta, perche' la
    # voce non e' dentro `cnvtalk()` ma e' una stringa con le virgolette sue.
    # Il formato e' quello di `chara_func.hsp:1323`: `???: \"…\"`.
    (7173, '??? says: \\"If you truly wish to no longer be a ninja, then you must die. '
           'This is the law of ninjas.\\"'):
        '???: \\"Se vuoi davvero smettere di fare il ninja, non ti resta che morire. '
        'È la legge dei ninja.\\"',

    # --- :7201-:7229 gli otto dèi che entrano in casa. ⚠️⚠️ L'inglese di tutte e
    # otto e' RICICLATO dalle lodi di text.hsp:12370-:12391: vedi la lezione in
    # cima. Si segue il giapponese, che qui ha otto battute sue.
    (7201, 'Well done. After all, you might be useful than I thought.'):
        'Ecco dunque la dimora di un mortale. Ne prendo nota.',
    (7205, 'Oh my little puppet, you serve me well.'):
        'Scatenare una tempesta qua dentro sarebbe uno spasso... scherzo, eh.',
    (7209, 'Impressive. Your action shall be remembered.'):
        'Un paradiso... che parola nostalgica.',
    # Ehekatl e' la dea gatta, e たらばがに e' il granchio reale.
    (7213, "Wheeee! I'm so happy. I like you! I like you!"):
        "Miaaao! Granchio reale! Dov'è il granchio reale?",
    (7217, 'Muwahaha muwaha. Good. Good!'):
        'Muahahaha! Uahahaha! Permesso, entro!',
    (7221, "W-What? I-I'm not gonna praise you. I'm not!"):
        'P-permesso... ah! È più in ordine della mia stanza...',
    (7225, 'Good work... truly...'):
        'Quindi è qui che vivi... Posso... guardare in ogni angolo...?',
    (7229, 'Good job, just like that! Keep it up!'):
        "Oh, e l'ingresso non si paga? Che spreco...",

    # --- :7979-:7988 le quattro battute del peluche di Kumiromi.
    # ⚠️ Non le dice una persona: `:7973` chiede che chi gioca abbia
    # ITEM_ID_KUMIROMI_GURUMI, il pupazzo maledetto che «si muove quando nessuno
    # guarda» (db_item.hsp:57502), e `:7991` ammazza la bestia del campo con
    # 99999 punti. Le prime tre parlano dei parassiti; la quarta e' rivolta a chi
    # gioca, ed e' quella che fa paura.
    (7979, "A vermin... I can't... tolerate..."):
        'Bestie nocive... non vi perdono...',
    (7982, 'I... will have no mercy... for vermin...'):
        'Gli insetti cattivi... vanno uccisi...',
    (7985, 'I have to... get rid of it...'):
        'Presto... bisogna... sterminarli...',
    (7988, 'I always... watch over you...'):
        'Ti guarderò... sempre... eh?...',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-main-012.jsonl'
DA, A = 7000, 7999
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\main.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_main.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]

# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**. Vedi il
# lotto 007 per il perche' e per la chiave lunga `(riga, en, jp)`.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ Il controllo di rete 1 va PRIMA delle altre reti (lotto 007).
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` o dentro un blocco. ⚠️ Si guarda la FIRMA.
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    return sorgente[riga - 1].lstrip().startswith(';') or riga in SPENTE


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _come = ("e' commentata nel sorgente"
                 if sorgente[_righe[0] - 1].lstrip().startswith(';')
                 else 'sta dentro un commento di BLOCCO')
        errori.append(f"rete 6: riga {v['riga']} {_come}, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"\U0001f4a1 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

# rete 7: una voce dentro un CONFRONTO non e' testo.
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome.
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») chiude col connettivo.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare.
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo.
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
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
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
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

# rete 15-bis: le voci di menu di questo file stanno in `*re_select`, e il tetto
# e' quello dello sfondo. Adesso lo sa anche `strumenti/menu_dialogo.py`.
try:
    from strumenti.menu_dialogo import FINESTRA_EVENTO, reso, tetto_di
except ImportError:
    reso = None
if reso is not None:
    def sfondo_di(riga: int) -> str:
        for i in range(riga - 1, max(0, riga - 40), -1):
            trovato = re.match(r'^\s*file\s*=\s*"([^"]+)"', sorgente[i - 1])
            if trovato:
                return trovato.group(1)
        return '?'

    for v in voci:
        if 'chatList' not in sorgente[v['riga'] - 1]:
            continue
        sfondo = sfondo_di(v['riga'])
        tetto = tetto_di(FINESTRA_EVENTO, sfondo)
        testo = reso(RESE[chiave(v)])
        if tetto is None:
            print(f"⚠️ rete 15-bis: riga {v['riga']} — sfondo {sfondo!r} non trovato, "
                  f"NON misurata")
        elif len(testo) > tetto:
            errori.append(f"rete 15-bis: riga {v['riga']} {len(testo)} > {tetto} "
                          f"({sfondo}) -> {testo}")
        else:
            print(f"💡 rete 15-bis: riga {v['riga']} {len(testo):3d}/{tetto} "
                  f"({sfondo})  {testo}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione.
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
    resa = RESE[chiave(v)]
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


# rete 4: chiave `(giapponese, funzioni, inglese)` — corretta nella 57a.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: stesso inglese, giapponese diverso. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
