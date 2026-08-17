# -*- coding: utf-8 -*-
"""Lotto fase4-main-007: gli esiti degli incarichi e le battute degli dèi
(main.hsp, righe 4520-4712).

Sedici rese, due gruppi. Il primo e' il verdetto che chiude ogni incarico a
tempo — festa, consegna, campo minato, caccia — cioe' la riga che il giocatore
legge **ogni volta** che ne finisce uno. Il secondo sono le sette battute che
gli dèi dicono prima di scatenare il Ragnarok (`ANIMATION_RAGNA`), una per
divinita'.

⭐⭐ **`:4549` e `:4562` sono lo stesso inglese per due incarichi diversi, e la
rete 13 ha ragione a segnalarlo.** Upstream ha scritto `"You complete the
task!"` due volte, ma il giapponese distingue: 「無事に納入を終えた！」 e' la
**consegna** (`QUEST_TYPE_HARVEST`, si portano le merci) e 「無事に撤去を終えた！」
e' la **rimozione** (`QUEST_TYPE_MINEFIELD`, si tolgono le mine). Lo stesso vale
per la coppia dei fallimenti, `:4554` e `:4567`.
✅ L'italiano tiene la distinzione, e le parole non sono scelte qui:
«consegna» viene da `command.hsp:15499` («Hai consegnato...», « Consegnato »),
che e' la riga di quello stesso incarico. Per il campo minato «bonifica» e' il
termine italiano proprio del togliere le mine.
💡 E' il rovescio del caso di `:4050` nel lotto 005: li' upstream distingueva
dove il giapponese non lo faceva, qui appiattisce dove il giapponese distingue.
Sono le due facce della stessa domanda — **quale delle due lingue di monte sa la
cosa che serve** — e la risposta si trova sempre guardando il codice intorno,
qui `gdata(GDATA_QUEST)`.

⚠️ **`:4712` perde `he(cc)`, che e' morfologia.** L'inglese chiude con «...the
dust from whence " + he(cc) + " came!», cioe' col pronome che l'italiano
dovrebbe accordare con un genere che non conosce. `he` con **un** argomento sta
in `MORFOLOGIA_INGLESE` e `verifica` pretende che sparisca. La resa segue allora
il giapponese, che quel pronome non ce l'ha: 「今こそ、あるべき姿へと還るのだ！」,
«e' ora di tornare alla forma che ti spetta». ⚠️ E non si mette «questo sciocco
torni alla polvere da cui e' **venuto**»: sarebbe lo stesso participio, entrato
dalla finestra.

⚠️ **`:4572` non dice «non sei riuscito».** 「討伐に失敗した…」 e' impersonale in
giapponese e lo diventa in italiano — «La caccia e' fallita...» — perche' il
participio con `essere` accorderebbe col genere del giocatore. Stessa ragione di
`:4353` nel lotto 006, dove «Sei sottoterra» ha preso il posto di «sei stato
sepolto».

💡 **Le sette battute degli dèi vanno lette come sette voci diverse**, e il
sorgente dice di chi sono: `EVENT_GOD_INSIDE_LULWY` a `:4619`, poi Ehekatl,
Opatos, Kumiromi, Mani, Jure e Itzpalt. Quella di Ehekatl e' un verso di gatto
(「みみゃぁ」 / «MEWWWWWW»), quella di Jure una battuta sulla stupidita' che non si
cura — e' la dea che guarisce — e quella di Itzpalt un'invocazione ai tre
elementi. Tradurle tutte con lo stesso tono le avrebbe appiattite.

⚠️ **`:4616` e' una citazione**, e resta tale: la Sorellina che scivola dalla
spalla del Papa'-Bombola e grida «Mr. Bubbles!» viene da *BioShock*, dove in
italiano quel nome **non e' stato tradotto**. Le due creature hanno gia' il loro
nome nel gioco; qui si tiene la citazione come la tiene l'inglese.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :4520-:4541 la festa a tempo.
    (4520, 'Your final score is  points!'):
        '"Il punteggio finale è " '
        '+ qdata(QDATA_PARAM2, gdata(GDATA_QUEST_REF)) + " punti!"',
    (4536, 'People had a hell of a good time!'):
        'La festa è stata un successone!',
    (4541, 'The party turned out to be a big flop...'):
        'La festa è finita in un mezzo disastro...',

    # --- :4549-:4554 la consegna (QUEST_TYPE_HARVEST). «consegna» viene da
    # command.hsp:15499, che e' la riga di questo stesso incarico.
    (4549, 'You complete the task!'):
        'Consegna completata!',
    (4554, 'You fail to fulfill your task...'):
        'La consegna non è arrivata in tempo...',

    # --- :4562-:4567 il campo minato (QUEST_TYPE_MINEFIELD). ⚠️ Stesso inglese
    # delle due qui sopra, giapponese diverso: 撤去 e' la rimozione delle mine.
    (4562, 'You complete the task!'):
        'Bonifica completata!',
    (4567, 'You fail to fulfill your task...'):
        'La bonifica non è finita in tempo...',

    # --- :4572 la caccia (QUEST_TYPE_CONQUER). ⚠️ Impersonale come il
    # giapponese: «non sei riuscito» porterebbe un participio col genere.
    (4572, 'You failed to slay the target...'):
        'La caccia è fallita...',

    # --- :4616 la citazione da BioShock. I due nomi stanno gia' cosi', fra
    # parentesi angolari, e «Mr Bubbles» si scrive senza il punto
    # (db_creature.hsp:124283, :124289, :124385).
    (4616, 'The Little Sister slips from the Big Daddy\'s shoulder. \\"Mr. Bubbles!\\"'):
        '<Little Sister> scivola dalla spalla di <Big Daddy>. \\"Mr Bubbles!\\"',

    # --- :4622-:4712 le sette battute degli dèi prima del Ragnarok, una per
    # divinita': Lulwy, Ehekatl, Opatos, Kumiromi, Mani, Jure, Itzpalt.
    (4622, 'Fool... Prepare to die!!!'):
        'Che sciocchezza... preparati a morire!!!',
    # Ehekatl e' la dea gatta: e' un verso, non una frase.
    (4652, 'memememw...MEMEMEM...MEWWWWWW!'):
        'mimimi... MIMIMI... MIAAAAAO!',
    (4664, '...Muwahahaha...wahahahaha!'):
        '...Muahahaha... uahahahahah!',
    (4676, "I absolutely... can't forgive...!!!"):
        'Non ti perdono... mai e poi mai...!!!',
    (4688, 'Come, let us bring this farce to a close!!!'):
        'Su, facciamo calare il sipario!!!',
    # Jure e' la dea che guarisce, e la battuta e' sua: la stupidita' non si cura.
    (4700, "I-if you won't die, then my only choice is to heal your foolishness!!!"):
        'S-se proprio non vuoi morire, allora ti curo io la stupidità!!!',
    # ⚠️ `he(cc)` con un argomento e' morfologia e sparisce: la chiusa segue il
    # giapponese, 「今こそ、あるべき姿へと還るのだ！」, che quel pronome non ce l'ha.
    # ⚠️⚠️ Ma la voce resta DINAMICA, perche' e' il ramo inglese a dirlo: la resa
    # va scritta come espressione HSP, fra virgolette, anche se di funzioni non
    # ne resta nessuna. Senza, `applica.py` la scriverebbe come codice (37ª).
    (4712, 'Roaring flames! Biting cold! Savage lightning! Return this fool to the dust from whence  came!'):
        '"Fiamme, turbinate! Gelo, avvolgi! Folgore, guizza! '
        'È ora di tornare alla forma che ti spetta!"',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-main-007.jsonl'
DA, A = 4421, 4720
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\main.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_main.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]

# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
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

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006) o dentro un blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
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
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `command.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
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


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
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
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
