# -*- coding: utf-8 -*-
"""Lotto `command-026`: **le tasse, le medagliette, le cose da non posare**.
Trenta rese, e con queste **la zona 15000-15999 e' chiusa**.

⭐⭐ **Otto rese su trenta non le ho decise io, ed e' il record del progetto per
un lotto solo.** Sei sono il coro della schermata dei traguardi — «Finalmente!»,
«Era il risultato naturale.», «Uooooooh!», «Hmpf.», «Stanotte non chiudo
occhio.», «Stai scherzando.» — che `text.hsp:477`-`:492` ha gia' reso perche' la
stessa lista serve a **ogni** traguardo del gioco: qui `:15564`-`:15569` la
riscrive tale e quale per la sfida delle tasse doppie. Le altre due sono «Non hai
abbastanza denaro...» (`proc.hsp:15584`) e «Mai!», che ho scritto io **due lotti
fa** (`:15196`, lotto 024). ⭐ La rete 3 le ha nominate tutte e otto da sola.

⭐⭐ **E qui l'italiano puo' rimettere quel che l'inglese ha buttato via.**
`:15636` e `:15645` hanno **lo stesso identico inglese** — «name swallows
itemname angrily» — e due giapponesi che non si somigliano per niente: a `:15636`
l'alleato «va su tutte le furie e ingoia» l'anello di fidanzamento, a `:15645`
«si ficca in bocca il cioccolatino in fretta e, masticando, risponde che non ha
nessun oggetto del genere». L'inglese ha appiattito una scenetta comica su una
frase di rabbia. ✅ La resa italiana puo' tenerle distinte **senza violare la
rete 11**, perche' quella confronta l'insieme delle funzioni di contenuto e
tutt'e due le righe hanno `name` piu' `itemname`, in inglese come in giapponese.
💡 E' il rovescio del caso di `:15188` nel lotto 024: la' l'inglese diceva la
cosa sbagliata e la rete 3 ha imposto il giapponese, qui l'inglese dice **meno**
e nessuna rete obbliga a niente — a decidere e' che le funzioni bastano.
⚠️ La rete 13 lo segnala, ed e' il suo mestiere: un inglese per due giapponesi.

⚠️⚠️ **Tre delle quattro battute di `:15615` non le vede nessuno, e non e' una
riga spenta.** L'array e' `s = "", 「やだ」, 「あげないよ」, 「だめ」, 「イヤ！」` e
l'indice arriva da `f`, che due righe sopra vale **`0` oppure `2`**:
`f = 0` a `:15610`, `f = 2` a `:15612` se l'oggetto e' un minerale, e `:15614`
entra solo `if ( f != 0 )`. Quindi il gioco stampa **sempre e solo lo slot 2**,
«Non si tocca!», e gli slot 1, 3 e 4 sono irraggiungibili.
⚠️ **Ma non sono testo morto nel senso della rete 6**: la riga e' viva, la
`lang()` gira, il valore finisce dentro `s`. A spegnerli e' l'**aritmetica di un
indice**, che nessuno strumento del progetto guarda — non `commenti-blocco.py`,
non `lang-nel-ramo-jp.py`, non la rete 6. ✅ Si traducono lo stesso, e per un
motivo pratico: basta che upstream aggiunga un `f = 3` da qualche parte perche'
tornino vivi, e allora sarebbero inglese in mezzo all'italiano.
💡 E' la **quarta famiglia** dopo il `;`, il `/* */` e il ramo della lingua — ma
la prima che non e' un fatto del testo: e' un fatto del **flusso**.

⚠️ **`:15627` nomina il soggetto in giapponese e non in inglese, ed e' statica.**
Il giapponese e' `name(tc) + "は洗脳されていて、装備を外さない！"`, l'inglese «It is
impossible to change the equipment by confusing» — nessuna funzione. La resa non
puo' nominare nessuno (la regola del contratto con la riga), quindi va
all'impersonale: «Sotto plagio non si cambia equipaggiamento!». 💡 «Plagio» e' il
termine che `buff.hsp:1362` ha gia' scelto per `brainwash`.

⭐ Altri termini riscossi: «Medagliette» e «Biglietti» (`command.hsp:14105`,
`:14108`), «Carretto» (`:14176`), «Scorciatoia» (`text.hsp:10`, `:121`), e la
coppia «posare»/«[Non posare]» del menu (`:14087`, `:14091`), che decide come si
dicono `no-drop` e `continuously drop` senza inventare niente.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :15508-:15562 le tasse e la sfida delle tasse doppie.
    # ⭐ rete 3: proc.hsp:15584 ha già lo stesso giapponese.
    (15508, "You don't have enough money."): 'Non hai abbastanza denaro...',
    (15524, "You don't have to pay your tax yet."):
        'Non è ancora ora di pagare le tasse.',
    (15549, 'You pay .'): '"Hai pagato " + itemname(ci) + "."',
    # il nome della sfida, che compare sulla schermata del traguardo
    (15560, 'Double Tax Each Month'): 'Tasse doppie ogni mese',
    (15562, 'Unbelievable! You paid your taxes for  month!'):
        '"Incredibile! Hai pagato le tasse per " '
        '+ (TweakData(TWEAK_CHALLENGE_DOUBLE_TAX_EACH_MONTH, TWEAK_CATEGORY_CHALLENGE) - 1) '
        '+ " mesi!"',

    # --- :15564-:15569 il coro del traguardo. ⭐ tutte e sei da text.hsp:477-:492,
    #     dove la stessa lista serve a OGNI traguardo del gioco.
    (15564, 'Finally!'): 'Finalmente!',
    (15565, 'Just the natural outcome.'): 'Era il risultato naturale.',
    (15566, 'Woooooo!'): 'Uooooooh!',
    (15567, 'Heh.'): 'Hmpf.',
    (15568, "I can't sleep tonight."): 'Stanotte non chiudo occhio.',
    (15569, "You're kidding."): 'Stai scherzando.',

    # --- :15615 l'alleato che non ridà il minerale.
    #     ⚠️ solo lo slot 2 è raggiungibile: f vale 0 o 2 (:15610, :15612).
    #        Gli altri tre si traducono lo stesso. Vedi il docstring.
    (15615, 'No!'): 'Non voglio!',
    (15615, "It's mine."): 'Non si tocca!',
    (15615, 'Get off!'): 'Giù le mani!',
    # ⭐ rete 3: 「イヤ！」 è già «Mai!» a :15196, lotto 024.
    (15615, 'Never.'): 'Mai!',

    # --- :15623-:15627 l'equipaggiamento che non si toglie.
    # ⚠️ «maledetto» accorderebbe col genere dell'oggetto; «non si può togliere»
    #    è impersonale e vale per la spada come per lo scudo.
    (15623, " is cursed and can't be taken off."):
        'itemname(ci) + " porta una maledizione e non si può togliere."',
    # ⚠️ il giapponese nomina tc, l'inglese no, e la voce è STATICA: la resa non
    #    può nominare nessuno. «Plagio» è il termine di buff.hsp:1362.
    (15627, 'It is impossible to change the equipment by confusing.'):
        'Sotto plagio non si cambia equipaggiamento!',

    # --- :15636 e :15645 lo stesso inglese per due scene diverse.
    #     ⭐ il giapponese le distingue e la rete 11 lo permette: name + itemname
    #        in tutt'e due. Vedi il docstring.
    (15636, ' swallows  angrily.'):
        'name(tc) + " va su tutte le furie e ingoia " + itemname(ci, 1) + "."',
    (15645, ' swallows  angrily.'):
        'name(tc) + " si ficca in bocca " + itemname(ci, 1) + " in fretta e, '
        'masticando, risponde che non ha nessun oggetto del genere."',

    # --- :15659-:15762 prendere, lanciare, le medagliette e i biglietti.
    (15659, 'You take .'): '"Hai preso " + itemname(ci, in) + "."',
    # 「そこには投げられない。」: qui si lancia, non si spara — action.hsp:10122 ha
    # lo stesso inglese per il tiro, e infatti dice «sparare».
    (15692, 'The location is blocked.'): 'Non si può lanciare lì.',
    # ⭐ stesso inglese di text.hsp:14 e :15
    (15708, 'Your inventory is full.'): 'Il tuo zaino è pieno.',
    # ⭐ «Medagliette» e «Biglietti» sono i termini del menu, :14105 e :14108
    (15727, "You don't have enough coins."): 'Non hai abbastanza medagliette...',
    (15734, 'You receive !'): '"Hai ricevuto " + itemname(ti, 1) + "!"',
    (15762, "You don't have enough tickets."): 'Non hai abbastanza biglietti...',

    # --- :15853-:15884 le cose da non posare e la posa in serie.
    #     ⭐ il menu dice «[Non posare]» e «[Posa in serie]» (:14087, :14091):
    #        le frasi usano lo stesso verbo, così il giocatore le riconosce.
    (15853, 'You set  as no-drop.'): '"Non poserai più " + itemname(ci) + "."',
    (15857, ' is no longer set as no-drop.'):
        'itemname(ci) + " si può posare di nuovo."',
    (15862, 'You can continuously drop items.'): 'Adesso puoi posare in serie.',
    (15884, 'Really leave these items?'):
        'Ci sono ancora oggetti: vuoi lasciarli?',

    # --- :15923 la scorciatoia. ⭐ «Carretto» da :14176, «Scorciatoia» da
    #     text.hsp:10 e :121.
    (15923, "You can't make a shortcut for cargo stuff."):
        'Le cose sul carretto non si possono assegnare a una scorciatoia.',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-026.jsonl'
DA, A = 15501, 15999
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\command.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_command.jsonl', encoding='utf-8') if l.strip()]
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
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v))].add(parole(RESE[chiave(v)]))
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
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
