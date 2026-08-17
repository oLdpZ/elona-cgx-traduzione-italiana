# -*- coding: utf-8 -*-
"""Lotto fase4-main-010: il minigioco delle orecchie (main.hsp, 6035-6273).

Quarantaquattro rese. E' il rovescio esatto di quello che `action.hsp` ha gia'
chiuso: la' e' un compagno che pulisce le orecchie a chi gioca, qui e' chi gioca
a pulirle a un compagno. Stesse azioni, stessi esiti, **battute dell'altro
parlante**.

⭐⭐ **Dieci delle quarantaquattro non si traducono: si copiano.** Le cinque
frasi dell'esito (「粉末みみくそがとれた！」…「ひとつなぎのみみくそがとれた！」)
hanno il giapponese **identico** a `action.hsp:14622`-`:14650` e ci sono due
volte a testa, perche' upstream ha scritto due inglesi appena diversi per lo
stesso giapponese («Some powdered earwax…» al primo orecchio, «The powdered
earwax…» al secondo). Il giapponese non distingue niente e la resa nemmeno.
💡 E' la regola «cercare prima di scrivere» che rende dieci voci su
quarantaquattro: quasi un quarto del lotto era gia' deciso e nessuno lo
sapeva, perche' `main.hsp` non aveva un dizionario fino alla 57a.

💡 **Il vocabolario viene tutto da `action.hsp`** e non si ridecide qui:
`mimikaki` resta il nome dell'attrezzo (`:14584`), «timpano» (`:14584`),
«condotto uditivo» (`:14611`), «cerume», «l'altro orecchio» (`:14658`).
⚠️ Il **titolo** dell'evento e' l'altra cosa: l'inglese scrive «Mimikaki», che e'
l'attrezzo, ma 「耳掃除」 e' l'**attivita'**. In italiano l'attrezzo si chiama gia'
mimikaki e il titolo dice quel che si sta facendo: «Pulizia delle orecchie».

⚠️⚠️ **Il giapponese di queste battute porta i suffissi di parlata**
(`_da(3)`, `_na(3)`, `_kure(3)`, `_yo(3)`, `_ore(3)`, `_noka(3)`), che scelgono
il tono secondo il personaggio. L'inglese non li ha e le voci sono **statiche**:
la resa e' testo nudo e il tono va scelto una volta sola, neutro. Non si prova a
riprodurre il registro, che qui e' una funzione del sorgente e non una parola.

⚠️ **`:6111` dice «Piano, non strattonare!» e non «Non essere brusco».**
「乱暴にしないで」 e' rivolto a chi gioca, e «brusco» ne marcherebbe il genere. E'
la stessa disciplina di `:5194` nel lotto 008 — il destinatario, non il
parlante.

⚠️ **Niente `～` nella resa, nemmeno dove il giapponese lo usa.** 「耳がぁ～！！」
e 「～～～～～っ！！」 allungano il suono con un carattere a doppia larghezza che
il progetto proibisce: in italiano si allunga la vocale. Il `♪` invece resta —
e' l'unico a doppia larghezza ammesso, e distingue le tre battute contente
(`:6099`, `:6273`) dalle tre spaventate (`:6095`).

💡 **`:6074` e `:6189` sono lo stesso giapponese con due inglesi diversi**
(«Size expansion (large)» e «Size large expansion»): e' una svista di monte, non
una distinzione, e la resa e' la stessa. La rete 4 le lascia passare perche'
guarda anche l'inglese (57a), e sta bene cosi': qui la rete deve **permettere**,
non decidere.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

# Le cinque frasi dell'esito, copiate da action.hsp:14622-:14650. Ognuna vale
# per due righe — il primo orecchio e il secondo — che upstream ha scritto con
# due inglesi diversi e lo stesso giapponese.
POLVERE = 'È venuto via del cerume in polvere!'
PEZZETTI = 'Sono venuti via dei pezzetti di cerume!'
MEMBRANA = 'È venuta via una membrana di cerume!'
GRUMO = 'È venuto via un grumo di cerume!'
FILO = 'È venuto via un filo di cerume tutto attaccato!'

RESE = {
    # --- :6035 e :6046 i due incidenti: il timpano sfondato (SOUNDLIST_STAB +
    # dmghp su SKILL_RES_SOUND) e il condotto che sanguina (dmgcon BLEED).
    # ⚠️ Il `～` del giapponese non si copia: si allunga la vocale.
    (6035, '!!!???'):
        'Aaaaaaaaaah!!!!!??',
    (6035, 'Eeeeeeeeeek!'):
        "L'orecchio, il mio orecchio!!",
    (6046, 'What are you doing!?'):
        'Ahiii!?',
    (6046, 'No...No...!'):
        'Basta, non voglio più!',

    # --- :6052-:6086 il primo orecchio: titolo, testo e le dieci voci di menu.
    # ⚠️ Il titolo e' l'attivita', non l'attrezzo: vedi la lezione in cima.
    (6052, 'Mimikaki'):
        'Pulizia delle orecchie',
    # ⚠️ Dinamica: perde `his(tc)`, che e' morfologia, e resta espressione HSP.
    (6054, "It's hard to see inside  ear..."):
        '"Dentro l\'orecchio si vede poco..."',
    (6058, 'Put in carefully'):        'Infilare con cautela',
    (6061, 'Put in all the way'):      'Infilare fino in fondo',
    (6064, 'Carefully scrape'):        'Raschiare con cura',
    (6068, 'Size adjustment'):         'Regolare la misura',
    (6071, 'Size expansion'):          'Ingrossare',
    (6074, 'Size expansion (large)'):  'Ingrossare molto',
    (6077, 'Rupture ear canal'):       'Far scoppiare il condotto',
    (6080, 'Shove in'):                'Spingere dentro',
    (6083, 'Thrust in deeply'):        'Conficcare a fondo',
    (6086, 'Break through the eardrum'): 'Sfondare il timpano',

    # --- :6095-:6119 le battute di chi riceve, tre per esito.
    (6095, 'It is somehow strange feeling.'): 'Che sensazione strana...',
    (6095, 'A little scary.'):                'Fa un po\' paura...',
    (6095, 'Please be gentle...'):            'Fai piano, ti prego...',
    (6099, 'Oh…'):                            'Ngh...♪',
    (6099, 'It feels good...!'):              'Che bello...♪',
    (6099, 'That tickles!'):                  'Mi fai il solletico!♪',
    # 「痛っ！」 e' gia' «Ahi!» in ai.hsp:522, stesso giapponese: si copia.
    (6111, 'Ouch!'):                          'Ahi!',
    (6111, 'You are hurting my eardrum!'):    'Hai toccato il timpano!?',
    # ⚠️ Niente «brusco»: il genere e' di chi gioca.
    (6111, "Don't be rough!"):                'Piano, non strattonare!',
    (6119, 'Something has swelled!?'):        'Si sta gonfiando qualcosa!?',
    (6119, "It's too big for me..."):         'Per me è troppo grosso...',
    (6119, 'Calm down a little!'):            'Ehi, calmati un attimo!',

    # --- :6128-:6156 i cinque esiti del primo orecchio: copiati da action.hsp.
    (6128, 'Some powdered earwax has been removed!'):     POLVERE,
    (6135, 'Some pieces of earwax have been removed!'):   PEZZETTI,
    (6142, 'Some membranous earwax has been removed!'):   MEMBRANA,
    (6149, 'A clump of earwax has been removed!'):        GRUMO,
    (6156, 'A mass of collected earwax was removed!'):    FILO,

    # --- :6167-:6189 il secondo orecchio.
    (6167, 'Opposite ear'):
        "L'altro orecchio",
    (6169, "It's difficult to do the same thing with everything reversed..."):
        'È tutto specchiato e viene difficile...',
    # ⚠️ Stesso giapponese di :6074 con un inglese appena diverso: stessa resa.
    (6189, 'Size large expansion'):
        'Ingrossare molto',

    # --- :6239-:6267 gli stessi cinque esiti, secondo orecchio.
    (6239, 'The powdered earwax has been removed!'):      POLVERE,
    (6246, 'The debris of the earwax has been removed!'): PEZZETTI,
    (6253, 'The membranous earwax has been removed!'):    MEMBRANA,
    (6260, 'The lump of earwax has been removed!'):       GRUMO,
    (6267, 'All the earwax was connected and removed!'):  FILO,

    # --- :6273 la chiusa contenta. ⚠️ L'inglese «Is it over?» perde il senso:
    # 「こんなに出た？」 e' lo stupore per **quanto** ne e' uscito, non una domanda
    # sulla fine. Si segue il giapponese.
    (6273, 'Is it over?'):              'Ne è venuto fuori tutto questo?',
    (6273, 'It was comfortable!'):      'Che bella sensazione!',
    (6273, 'Please do more...!'):       'Rifacciamolo, eh?...',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-main-010.jsonl'
DA, A = 6000, 6280
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
