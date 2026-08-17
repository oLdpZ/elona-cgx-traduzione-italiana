# -*- coding: utf-8 -*-
"""Lotto fase4-main-009: le due riunioni, i nove compagni che si rialzano e il
matrimonio (main.hsp, righe 5684-5943).

Trentotto rese, quattro gruppi. Le due schermate di **riunione** con lo sfondo
dipinto (chi ti seguiva di nascosto, e l'animale perduto nel naufragio), le
**nove coppie** del mostro abbattuto che chiede di unirsi, e il **matrimonio**.

⭐⭐⭐ **`:5684` e `:5686` sono due righe con l'inglese di un ALTRO evento, e
stavolta si vede a occhio nudo.** Il giapponese di `:5684` e' 「隠れていたもの」
(*chi si nascondeva*) e l'inglese dice «Reunion with your pet»; il giapponese di
`:5686` parla di 「背後の気配」 (*una presenza alle spalle*) e l'inglese racconta
il cane ritrovato entrando in citta' mineraria. Sono le righe di `:5737` e
`:5739`, **copiate**: la' il giapponese dice davvero 「ペットとの再会」 e 「懐かしい
鳴き声」. La prova sta nel menu che segue: sotto `:5686` le scelte sono *sorella,
signorina, fratello, maggiordomo* — persone — e sotto `:5739` sono *cane, gatto,
orso*. Un animale non e' un maggiordomo.
💡 E' il quinto modo in cui le due lingue non concordano, dopo i quattro gia'
visti: **l'inglese ha la riga giusta, ma dell'evento sbagliato**. Come al solito
decide il sito, e qui il sito e' il menu sotto.

⚠️⚠️ **E qui c'e' un tetto che nessuna rete misura bene.** Le tredici voci di
menu di questo lotto non stanno nella pergamena del dialogo: `main.hsp` fa
`gosub *re_select` (`event.hsp:4119`), che e' un'altra finestra — larga
`tx + 36` dove `tx` e' la larghezza del **BMP di sfondo**, col testo a `wx + 60`
invece che a `wx + 170`. `strumenti/menu_dialogo.py` cerca `chatList` in tutti i
file e applica **52** caratteri a tutte. Misurato con
`scratchpad/misura-re-select.py`: nel sorgente ci sono **177** righe di menu
dentro `*re_select`, e il tetto vero va da **36** (`bg_re15`) a **50**
(`bg_re20`) secondo lo sfondo. Qui sono `bg_re13` (360 px -> **41 caratteri**) e
`bg_re14` (380 -> **44**). Le rese piu' lunghe di questo lotto ne fanno 21.

💡 **La formula del mostro che si rialza non si inventa: e' gia' scritta.**
`chara_func.hsp:7915` rende 「なかまに　なりたそうに　こちらをみている」 con «si
rialza e ti guarda come se volesse unirsi a te», ed e' letteralmente la stessa
frase giapponese di queste nove. Si copia.
⚠️ **E i nove nomi vengono dal giapponese, non dal `CREATURE_ID`.** Il codice
crea `CREATURE_ID_PASCAL`, `_SUNRISE`, `_LITYOU`, ma il testo giapponese dice
「イヌ」「龍」「白虎」: nomi comuni, non nomi propri. La resa dice «il cane», «il
drago», «la tigre bianca» — e le parole sono quelle gia' fissate
(`action.hsp:16953`, `:16709`, `db_card.hsp:10553` per lo spazzino).
⚠️ Due dei nove sono **femminili in italiano** — la tigre bianca e la lumaca — e
il pronome cambia: «La accogli nel gruppo?» invece di «Lo accogli».

⚠️ **«You stabbed the monster in the coffin» e' un idiotismo storto.**
「トドメを刺した」 e' dare il colpo di grazia; l'inglese ci ha impastato «the final
nail in the coffin» e il risultato non vuol dire niente. La resa segue il
giapponese e la parola c'e' gia' tre volte in `db_creature.hsp` (`:62730`,
`:87139`, `:95886`): **colpo di grazia**.

⚠️⚠️ **Il matrimonio perde `his3` e cambia costruzione due volte, per lo stesso
motivo.** `:5934` e' l'annuncio che parte anche in rete (`net_send "marr"`):
l'inglese fa «X pledged his3 eternal love to name(marry)», e `his3` e'
morfologia che sparisce. Ma «amore eterno **a** name(marry)» lo fermerebbe la
rete 8 — la preposizione si fonderebbe con l'articolo del nome — quindi i due
sposi diventano soggetti insieme: «X e name(marry) si giurano amore eterno».
✅ Le funzioni di contenuto restano le stesse tre, e la rete 11 guarda
l'**insieme**, non l'ordine (40a).
⚠️ `:5941` evita per la seconda volta un participio: «tu e X siete uniti»
accorderebbe al maschile plurale una coppia che spesso non lo e'. «Un legame
saldo unisce te e X» dice la stessa cosa e non chiede il genere a nessuno.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

# La formula delle nove coppie, una volta sola: cambia solo il nome e il
# pronome. Scriverla nove volte a mano e' il modo di sbagliarne una.
def si_rialza(chi: str, pronome: str = 'Lo') -> str:
    return (f'{chi} che hai abbattuto si rialza e ti guarda come se volesse '
            f'unirsi a te. {pronome} accogli nel gruppo?')


def colpo_di_grazia(a_chi: str) -> str:
    return f'Hai dato il colpo di grazia {a_chi}.'


RESE = {
    # --- :5684-:5695 EVENT_SECRET_CHAR: chi ti seguiva di nascosto.
    # ⚠️ Inglese dell'evento sbagliato: vedi la lezione in cima. Si segue il
    # giapponese, che il menu qui sotto conferma (sono persone, non animali).
    (5684, 'Reunion with your pet'):
        'Chi si nascondeva',
    (5686, 'As you approach the mining town, you notice a familiar call and stop walking. '
           'Your old pet who got separated from you during the shipwreck is now running '
           'towards you joyfully! Your pet is...'):
        'Ti accorgi di una presenza alle spalle e ti fermi di colpo. '
        'Ti volti, ed ecco chi c\'era...',
    # Le otto scelte. I nomi sono quelli gia' fissati per le creature omonime:
    # action.hsp:17011, :17228, :16994, :17211, :18418, db_creature (fratello
    # minore), action.hsp:18435. Tetto vero 41 caratteri (bg_re13): la piu'
    # lunga ne fa 21.
    (5688, 'a sister!'):         'Una sorella minore!',
    (5689, 'a young lady!'):     'Una giovane dama!',
    (5690, 'an older sister!'):  'Una sorella maggiore!',
    (5691, 'a little girl!'):    'Una bambina!',
    (5692, 'a little boy!'):     'Un bambino!',
    (5693, 'a brother!'):        'Un fratello minore!',
    (5694, 'a butler!'):         'Un maggiordomo!',
    (5695, 'an older brother!'): 'Un fratello maggiore!',

    # --- :5737-:5743 l'evento vero dell'animale ritrovato, quello di cui
    # l'inglese qui sopra aveva rubato le righe.
    (5737, 'Reunion with your pet'):
        'Il ritorno del tuo animale',
    (5739, 'As you approach the mining town, you notice a familiar call and stop walking. '
           'Your old pet who got separated from you during the shipwreck is now running '
           'towards you joyfully! Your pet is...'):
        'Ti accorgi di un verso familiare e ti fermi di colpo. Ma guarda: il tuo '
        'animale, che era sparito nel naufragio, ti corre incontro tutto contento! '
        'Il tuo animale è...',
    (5741, 'a dog!'):  'Un cane!',
    (5742, 'a cat!'):  'Un gatto!',
    (5743, 'a bear!'): 'Un orso!',

    # --- :5780-:5919 le nove coppie del mostro che chiede di unirsi.
    # ⚠️ La stessa firma di 「少女だ！」 vale per :5691 e :5744: una voce sola.
    (5780, 'This monster seems to want to be friends. Do you want to befriend them?'):
        si_rialza("L'orco"),
    (5783, 'You stabbed the monster in the coffin.'):
        colpo_di_grazia("all'orco"),
    (5797, 'This monster seems to want to be friends. Do you want to befriend them?'):
        si_rialza('Lo scienziato'),
    (5800, 'You stabbed the monster in the coffin.'):
        colpo_di_grazia('allo scienziato'),
    (5814, 'This monster seems to want to be friends. Do you want to befriend them?'):
        si_rialza("L'angelo caduto"),
    (5817, 'You stabbed the monster in the coffin.'):
        colpo_di_grazia("all'angelo caduto"),
    (5831, 'This monster seems to want to be friends. Do you want to befriend them?'):
        si_rialza('Lo spazzino di sotterranei'),
    (5834, 'You stabbed the monster in the coffin.'):
        colpo_di_grazia('allo spazzino di sotterranei'),
    # ⚠️ Femminile: cambia anche il pronome.
    (5848, 'This monster seems to want to be friends. Do you want to befriend them?'):
        si_rialza('La tigre bianca', 'La'),
    (5851, 'You stabbed the monster in the coffin.'):
        colpo_di_grazia('alla tigre bianca'),
    (5865, 'This monster seems to want to be friends. Do you want to befriend them?'):
        si_rialza('Il cavaliere'),
    (5868, 'You stabbed the monster in the coffin.'):
        colpo_di_grazia('al cavaliere'),
    (5882, 'This monster seems to want to be friends. Do you want to befriend them?'):
        si_rialza('Il drago'),
    (5885, 'You stabbed the monster in the coffin.'):
        colpo_di_grazia('al drago'),
    # ⚠️ Femminile anche questa.
    (5899, 'This monster seems to want to be friends. Do you want to befriend them?'):
        si_rialza('La lumaca', 'La'),
    (5902, 'You stabbed the monster in the coffin.'):
        colpo_di_grazia('alla lumaca'),
    (5916, 'This monster seems to want to be friends. Do you want to befriend them?'):
        si_rialza('Il cane'),
    (5919, 'You stabbed the monster in the coffin.'):
        colpo_di_grazia('al cane'),
    # :5923 la dice il cane appena accolto (:5926 crea <Pascal>): 今後ともよろしく
    # e' la formula con cui si comincia un rapporto, non un ringraziamento.
    (5923, 'Thanks in advance.'):
        "Conto su di te, d'ora in poi...",

    # --- :5934-:5943 il matrimonio.
    # ⚠️ Perde `his3` (morfologia) e cambia costruzione per la rete 8: vedi la
    # lezione in cima. Le tre funzioni di contenuto restano tutt'e tre.
    (5934, '  pledged  eternal love to .'):
        'cdatan(CDATAN_AKA, CHARA_PLAYER) + " " + cdatan(CDATAN_NAME, CHARA_PLAYER) '
        '+ " e " + name(marry) + " si giurano amore eterno."',
    (5939, 'Marriage'):
        'Matrimonio',
    # ⚠️ Senza participio: «siete uniti» accorderebbe al maschile plurale.
    (5941, 'At last, you and  are united in marriage! After the wedding ceremony, '
           'you receive some gifts.'):
        '"Dopo un lungo fidanzamento un legame saldo unisce finalmente te e " '
        '+ name(marry) + "! Passate le nozze, ti arrivano alcuni doni."',
    # Il giapponese e' 「生涯をあなたに捧げる」, *ti dedico la mia vita*; l'inglese
    # dice il rovescio («senza di te la vita non ha senso»). Si segue il
    # giapponese, che e' la colonna che si legge accanto alla resa.
    (5943, 'Without you, life has no meaning.'):
        'Ti dedico la mia vita',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-main-009.jsonl'
DA, A = 5601, 5999
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

# rete 15-bis: le voci di menu di QUESTO file non stanno nella pergamena del
# dialogo ma in `*re_select`, e il tetto e' quello dello sfondo. Misurato in
# `scratchpad/misura-re-select.py`; qui si guarda solo il lotto.
try:
    from strumenti.menu_dialogo import PIXEL_PER_CARATTERE, reso
except ImportError:
    reso = None
if reso is not None:
    import struct
    from pathlib import Path

    GRAFICA = Path(r'C:\Games\Elona\elonaplus2.31\graphic')

    def sfondo_di(riga: int) -> str:
        for i in range(riga - 1, max(0, riga - 40), -1):
            trovato = re.match(r'^\s*file\s*=\s*"([^"]+)"', sorgente[i - 1])
            if trovato:
                return trovato.group(1)
        return '?'

    for v in voci:
        if 'chatList' not in sorgente[v['riga'] - 1]:
            continue
        bmp = GRAFICA / f'{sfondo_di(v["riga"])}.bmp'
        if not bmp.exists():
            print(f"⚠️ rete 15-bis: riga {v['riga']} — sfondo non trovato, non misurata")
            continue
        tx = struct.unpack('<i', bmp.read_bytes()[18:22])[0]
        tetto = int((tx + 36 - 12 - 64) / PIXEL_PER_CARATTERE)
        testo = reso(RESE[chiave(v)])
        stato = 'FUORI MISURA' if len(testo) > tetto else 'ok'
        if stato != 'ok':
            errori.append(f"rete 15-bis: riga {v['riga']} {len(testo)} > {tetto} "
                          f"({bmp.stem}) -> {testo}")
        else:
            print(f"💡 rete 15-bis: riga {v['riga']} {len(testo):3d}/{tetto} "
                  f"({bmp.stem})  {testo}")

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
