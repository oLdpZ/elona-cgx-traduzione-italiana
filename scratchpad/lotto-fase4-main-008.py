# -*- coding: utf-8 -*-
"""Lotto fase4-main-008: il Sigillo Eterno, i guardiani di Lesimas e i tre
incontri di strada (main.hsp, righe 5021-5496).

Undici rese. Il primo gruppo e' l'assalto finale al **Sigillo Eterno**: i
rinforzi che si teletrasportano dentro, la zanna della luce nascente che apre
il sigillo, la bestia che esce da <Enthumesis>. Il secondo sono i tre agguati
che scattano scendendo Lesimas — i sicari di Zanan a livello 20 e 25, i
cadaveri a livello 34. Il terzo sono tre righe sparse: il compleanno, l'urto
con Marka, la fine di un viaggio.

⭐⭐ **`:5393` e' il caso piu' netto di «l'inglese sbaglia» visto finora, ed e'
il codice a dirlo.** Il giapponese e' 「階段を下りた瞬間、あなたは銀髪の冒険者と
ぶつかった。」 — *appena sceso le scale hai urtato un avventuriero dai capelli
d'argento* — e l'inglese dice «So you are also of the same genus as the
others...», che non c'entra niente: e' una **battuta di dialogo** finita nella
riga della narrazione. Il codice sta col giapponese: `:5390` crea
`CREATURE_ID_MARKA_THE_SILVER_BEAR`, `:5391` e `:5392` suonano **due volte**
`SOUNDLIST_BASH1` (l'urto), e solo a `:5395`-`:5396` parte il dialogo vero. La
riga narra la collisione; la battuta viene dopo.
💡 Quarto modo in cui le due lingue di monte non concordano, dopo i tre della
57a: qui l'inglese non sbaglia una parola, ha proprio **la riga di un altro
posto**. La regola tiene lo stesso: decide il sito.

⚠️ **E Marka e' donna: «un'avventuriera».** Il giapponese non marca il genere e
l'italiano deve; ma qui non e' il caso di girarci intorno come si fa coi figli
di `event.hsp`, perche' il sesso **si sa** — e' `<Marka> l'orsa d'argento di
Mayroon` (`db_card.hsp:6380`), e `text.hsp:9816` dice gia' «muovere con lei».
La regola della 52a e' «non accordarsi con un genere che non si conosce», non
«non accordarsi mai».

⚠️⚠️ **`:5194` non puo' dire «un avventuriero», e li' il genere e' del
GIOCATORE.** 「《常闇の眼》を狙う冒険者だな？」 e' il sicario che si rivolge a chi
gioca, e in italiano «avventuriero» marcherebbe il maschile su una persona che
puo' essere donna. La resa toglie il sostantivo e tiene il senso: «A caccia
dell'<occhio delle tenebre eterne>, eh?». E' la stessa disciplina delle battute
dei figli, applicata al **destinatario** invece che al parlante.

⭐ **Il Libro della Verita' e' fissato qui, e prima non esisteva.** 「真実の書」
sta in tre punti del sorgente (`chat.hsp:7272`, `scene1.hsp:1217` e questo) e
in nessuna resa: il dizionario non lo aveva perche' `chat.hsp` e' quasi tutto
da fare. ⚠️ L'inglese di `:5181` dice altro — «You can not reach the bottom of
Lesimas» — cioe' **nomina il posto invece dell'oggetto**; il giapponese nomina
l'oggetto, ed e' quello che il giocatore va a prendere. Si segue il giapponese,
e la parola vale anche per `chat.hsp` quando ci si arrivera'.

💡 **I due nomi degli artefatti vengono da `text.hsp` e non si ridecidono qui**:
`:11633` ha gia' 来光の牙 = «zanna della luce nascente» e `:11585` 常闇の眼 =
«occhio delle tenebre eterne». Erano scritti fra parentesi quadre perche' li' il
giapponese le aveva; in mezzo a una frase vanno senza.

⚠️ **`:5496` evita il participio, e non e' pignoleria.** 「あなた達は目的地まで
辿り着いた」 e' plurale — tu e chi viaggia con te — e «siete arrivati» sarebbe un
participio che a una giocatrice sola suona sbagliato. «Siete a destinazione» dice
la stessa cosa senza chiedere il genere a nessuno.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :5021-:5101 l'assalto al Sigillo Eterno.
    # :5021 il teletrasporto dei rinforzi (`SOUNDLIST_TELEPORT1` a :5019, e a
    # :5030 arriva <Melugast Ao-i>): e' chi entra a dirlo, non il giocatore.
    (5021, 'Apparently that went well!'):
        "Pare che ce l'abbiamo fatta in tempo!",
    # :5054 lo stesso ingresso, ma a piedi: :5046-:5052 sono quattro passi.
    (5054, 'Is this the Eternal Seal!?'):
        'Allora questo è il Sigillo Eterno?!',
    # 来光の牙 = text.hsp:11633. Il nome sta gia' deciso, qui perde le quadre.
    (5080, 'The Origin of Light began to release astral light...'):
        'La zanna della luce nascente comincia a irradiare luce astrale...',
    (5083, 'The light emitted enveloped the Eternal Seal!!'):
        'La luce che ne sgorga avvolge il Sigillo Eterno!',
    # ⚠️ L'inglese si ferma a meta': 「獣の咆哮が辺りに響く…。」 non c'e'. Il
    # giapponese sa di piu' e la seconda frase e' quel che si sente davvero
    # (:5102-:5104 suonano SOUNDLIST_BEAST02 **tre volte**).
    (5101, 'Something splits <Enthumesis> body and breaks out!'):
        'Qualcosa schizza fuori dal ventre di <Enthumesis>! '
        "Il ruggito di una bestia risuona tutt'intorno...",

    # --- :5181-:5225 i tre agguati di Lesimas, a livello 20, 25 e 34.
    # ⚠️ L'inglese nomina il posto, il giapponese l'oggetto: 真実の書 e' quel che
    # si va a prendere in fondo, e la parola si fissa qui.
    (5181, 'You can not reach the bottom of Lesimas.'):
        'Chi si avvicina al Libro della Verità di Lesimas, muore.',
    # ⚠️ Niente «avventuriero»: la frase e' rivolta a chi gioca, e il genere non
    # si conosce. 常闇の眼 = text.hsp:11585.
    (5194, 'An adventurer seeking the <Origin of Vice>? You seek your own death?!'):
        "A caccia dell'<occhio delle tenebre eterne>, eh? E adesso muori!",
    (5225, 'The moment you set foot on this floor, a dozen corpses rise up and attack!'):
        "Appena metti piede sul piano, i cadaveri tutt'intorno si rialzano in massa!",

    # --- :5351-:5496 le tre righe sparse.
    # 「へぇ」 e' una sorpresa: chi parla se ne accorge in quel momento.
    (5351, 'Happy birthday!'):
        'Ma guarda, oggi compi gli anni? Auguri!',
    # ⚠️ L'inglese e' la battuta di un altro punto: vedi la lezione in cima.
    (5393, 'So you are also of the same genus as the others...'):
        "Appena scendi le scale, urti contro un'avventuriera dai capelli d'argento.",
    # ⚠️ Senza participio: 「あなた達」 e' plurale e il genere non si sa.
    (5496, 'You arrive at your destination...'):
        'Dopo un lungo cammino, siete a destinazione...',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-main-008.jsonl'
DA, A = 5000, 5600
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
