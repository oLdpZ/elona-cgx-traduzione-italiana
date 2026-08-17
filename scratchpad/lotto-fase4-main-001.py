# -*- coding: utf-8 -*-
"""Lotto fase4-main-001: il registro del mondo — meteo, vento d'etere, ciclo del
giorno (main.hsp, righe 1174-1635).

⭐ **`main.hsp` e' l'ultimo dei «mezzi fatti» della 55ª, ed e' l'undicesimo file
senza dizionario**: 384 `lang()` che nessun referto nominava, perche'
`verifica --dizionario` elenca solo i file che hanno un `dizionario/*.jsonl`.
Aprirlo anche per una voce sola lo fa entrare nel conteggio. Questa e' la
formula che la 54ª aveva scritto e la 56ª ha applicato in serie su altri quattro.

Trentaquattro rese, e la zona non e' scelta a caso: sono i messaggi che il
giocatore legge **piu' spesso di qualunque altro**, perche' escono da soli col
passare delle ore — «comincia a piovere», «spunta l'alba», «il tuo diario e'
stato aggiornato».

⚠️⚠️ **L'inglese di `:1307` e' sbagliato, e la resa italiana lo corregge.**
Il giapponese e' 「雪は止んだ。」 (*la neve e' cessata*) e il ramo che la contiene e'
`if ( p == WEATHER_SNOW )` (`:1304`); l'inglese ci ha copiato sopra
`"It stops raining."`, la stessa stringa che sta gia' a `:1274` per la pioggia.
Sono due voci con **firma diversa** — la firma e' sul contenuto, e il giapponese
differisce — quindi il dizionario le distingue senza bisogno di toppe. ⚠️ La
rete 13 lo dira' come referto: «un inglese solo per due giapponesi diversi». E'
esattamente il caso che quella rete esiste per far vedere.

⭐ **Quattro etichette gia' decise hanno deciso quattro rese**, e nessuna delle
quattro e' stata scelta qui:

  - `text.hsp:46` e' l'array `_weather`, cioe' i nomi del tempo nell'HUD:
    «Vento d'etere», «Neve», «Pioggia», «Temporale». Percio' `:1279`
    (RAIN -> HARD_RAIN) dice «diventa un temporale» e `:1286` (HARD_RAIN ->
    RAIN) dice «si attenua in pioggia»: il messaggio nomina lo stato in cui
    l'HUD sta passando, con la parola che l'HUD usa.
  - `text.hsp:60` sono le ore del giorno, e la sesta e' «Alba». `:1399` scatta
    a `if ( gdata(GDATA_HOUR) == 6 )`, cioe' **nell'ora che si chiama cosi'**:
    «Spunta l'alba» e l'orologio concordano.
  - `text.hsp:48` sono le cinque giornate bonus — «Giornata da allenamento»,
    «da battaglia», «da lavoro», «da esplorazione», «da studio» — e i cinque
    messaggi di `:1524`-`:1540` le annunciano. Portano lo **stesso sostantivo**,
    percio' chi legge il messaggio ritrova la parola nella barra.
  - ⭐⭐ La toppa di `custom_tweaks.hsp:1846` chiama la sfida **«Vento d'etere
    perenne»**, ed e' la voce del pannello dei ritocchi da cui la si accende.
    Percio' il titolo di `:1626` e l'etichetta `(Permanent Etherwind)` di
    `:1213`, `:1217` e `:1294` dicono tutte quella, e non una quinta variante.
    ⚠️ Quella riga non e' una `lang()`: e' un letterale **nudo**, e a trovarla
    e' stato `nudi_en`. Senza guardare anche li', il titolo qui sarebbe stato
    scelto a orecchio.

⭐ **Il blocco `:1626`-`:1635` ha un gemello gia' tradotto**, e non e' una
somiglianza: e' lo stesso codice con un'altra sfida dentro. `command.hsp:15560`
(«Tasse doppie ogni mese») ha la stessa forma riga per riga — `s`, `file`,
`buff`, `listmax`, sei `chatList`, `gosub *re_select` — e le sei battute sono
**le stesse identiche `lang()`**, gia' rese in `command.hsp` e in `text.hsp`.
Qui si ricopiano, e la rete 3 lo confermera' su tutte e sei.
💡 Da li' viene anche la forma del `buff` di `:1628`: «Incredibile! Hai pagato
le tasse per N mesi!» -> «Incredibile! Hai resistito al vento d'etere per N
giorni!». ⚠️ **«Sei sopravvissuto» non e' scrivibile**: e' un participio riferito
al giocatore, di cui non si conosce il genere (guida-stile, «Registro»).
«Hai resistito» prende l'ausiliare che non accorda, e per giunta combacia col
contatore del pannello, che la toppa rende «giorni di sopravvivenza».

⚠️ **`:1630`-`:1635` sono `chatList`, cioe' passano dalla RETE 15** (il tetto di
52 caratteri delle voci della finestra del dialogo, misurato nella 55ª). La piu'
lunga delle sei rese ne fa 27: nessuna ci si avvicina. Entrano comunque nel
denominatore di `menu_dialogo`, che passa da 50 a 56 voci misurate.

💡 **«Le Nefie», al plurale, e non «Le Nefia».** Il plurale l'ha gia' scelto il
pannello dei ritocchi — «Nefie casuali risvegliate», «tutte le Nefie casuali» —
mentre il singolare sta in `text.hsp:9935` («una Nefia casuale»). Le due voci di
`:1174` e `:1187` sono le due meta' della stessa cosa: `:1187` accende
`GDATA_FLAG_NEFIA_FEVER_ACTIVE` a 100 e `:1174` lo rimette a zero.

⚠️ **Le nove righe di `:874`-`:898` NON sono in questo lotto e non vanno
tradotte mai.** Sono la finestra dei comandi per principianti, chiusa dentro un
`if ( jp )`: in inglese non esiste, e tutte e nove portano lo stesso segnaposto
«Essential is normal mode.». Le conta `scratchpad/lang-nel-ramo-jp.py`, che
all'apertura di questa sessione ha trovato la sua prima voce **gia' tradotta**
in `item_func.hsp` e l'ha fatta rinviare.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1174-:1187 la febbre delle Nefie casuali, le due meta' della stessa
    # cosa: :1187 accende GDATA_FLAG_NEFIA_FEVER_ACTIVE, :1174 lo rimette a zero.
    # Il plurale «Nefie» lo ha gia' scelto il pannello dei ritocchi.
    (1174, 'Nefia got quiet.'):
        'Le Nefie si sono calmate.',
    (1187, 'Nefia have entered fever!'):
        'Le Nefie casuali sono entrate in fermento!',

    # --- :1213-:1229 il vento d'etere. L'etichetta fra parentesi e' il nome
    # della sfida, e lo dice gia' il pannello: «Vento d'etere perenne».
    (1213, '(Permanent Etherwind) Etherwind will start in a few days, brace yourselves.'):
        "(Vento d'etere perenne) Fra pochi giorni arriva il vento d'etere: preparati.",
    (1217, "(Permanent Etherwind) Etherwind starts to blow. There's no escape."):
        "(Vento d'etere perenne) Il vento d'etere comincia a soffiare. Non c'è scampo.",
    # «rifugio» e' la resa fissata di `shelter` (text.hsp:2827, db_item.hsp:145197).
    (1229, 'Etherwind starts to blow. You need to find a shelter!'):
        "Il vento d'etere comincia a soffiare. Devi trovare un rifugio!",

    # --- :1242-:1307 il meteo. Le parole sono quelle dell'HUD (text.hsp:46):
    # «Pioggia», «Temporale», «Neve».
    (1242, 'You draw a rain cloud.'):
        'Attiri a te una nube di pioggia.',
    (1249, 'It starts to snow.'):
        'Comincia a nevicare.',
    (1256, 'It starts to rain.'):
        'Comincia a piovere.',
    # Il ramo mette WEATHER_HARD_RAIN, che nell'HUD si chiama «Temporale».
    (1261, 'Suddenly, rain begins to pour down from the sky.'):
        "All'improvviso scoppia un temporale.",
    (1274, 'It stops raining.'):
        'Ha smesso di piovere.',
    (1279, 'The rain becomes heavier.'):
        'La pioggia diventa un temporale.',
    (1286, 'The rain becomes lighter.'):
        'Il temporale si attenua in pioggia.',
    (1294, '(Permanent Etherwind) The Etherwind is restless.'):
        "(Vento d'etere perenne) Il vento d'etere non si placa.",
    (1300, 'The Etherwind dissipates.'):
        "Il vento d'etere si è dissolto.",
    # ⚠️ Il giapponese e' 「雪は止んだ」 e il ramo e' `p == WEATHER_SNOW`: l'inglese
    # ha copiato qui la stringa della pioggia di :1274. La resa segue il codice.
    (1307, 'It stops raining.'):
        'Ha smesso di nevicare.',

    # --- :1365-:1462 il ciclo del giorno.
    # «pisolino» e' gia' la resa di `nap` (command.hsp:10068).
    (1365, 'You take a nap.'):
        'Fai un pisolino.',
    (1373, 'You endure your sleepiness.'):
        'Resisti al sonno.',
    # Scatta a `gdata(GDATA_HOUR) == 6`, cioe' nell'ora che text.hsp:60 chiama «Alba».
    (1399, 'Day breaks.'):
        "Spunta l'alba.",
    (1453, 'A day passes and a new day begins.'):
        'Il giorno finisce e ne comincia uno nuovo.',
    # Gia' reso identico in sei file: la rete 3 lo confermera'.
    (1462, 'Your journal has been updated.'):
        'Il tuo diario è stato aggiornato.',

    # --- :1524-:1540 le cinque giornate bonus. Il sostantivo e' quello con cui
    # text.hsp:48 nomina la giornata nella barra.
    (1524, "It's a perfect day for training today."):
        "Oggi è una giornata perfetta per l'allenamento.",
    (1528, "It's a perfect day for combat today."):
        'Oggi è una giornata perfetta per la battaglia.',
    (1532, "It's a perfect day for work today."):
        'Oggi è una giornata perfetta per il lavoro.',
    (1536, "It's a perfect day for exploring today."):
        "Oggi è una giornata perfetta per l'esplorazione.",
    (1540, "It's a perfect day for studying today."):
        'Oggi è una giornata perfetta per lo studio.',

    # --- :1589 il detective. Il nome della creatura e' «il detective»
    # (db_creature.hsp:70308) e «*Snif*» e' la resa gia' usata per lo sniffare
    # (db_creature.hsp:96610). `cnvtalk` e' contenuto e resta.
    (1589, 'A detective seems to have come.*Sniff*... I smell a case!!'):
        '"Pare che sia arrivato un detective." '
        '+ cnvtalk("*Snif*... qui sento odore di un caso!!")',

    # --- :1626-:1635 la finestra della sfida, gemella di command.hsp:15560.
    (1626, 'Permanent Etherwind'):
        "Vento d'etere perenne",
    # ⚠️ «Hai resistito» e non «Sei sopravvissuto»: il participio con `essere`
    # accorderebbe col genere del giocatore, che non si conosce.
    (1628, 'Unbelievable! You survived Etherwind for  days!'):
        '"Incredibile! Hai resistito al vento d\'etere per " '
        '+ (TweakData(TWEAK_CHALLENGE_ALWAYS_ETHERWIND, TWEAK_CATEGORY_CHALLENGE) - 1) '
        '+ " giorni!"',
    # Le sei battute sono le stesse `lang()` di command.hsp:15564-15569, gia'
    # rese li' e in text.hsp: si ricopiano.
    (1630, 'Finally!'):
        'Finalmente!',
    (1631, 'Just the natural outcome.'):
        'Era il risultato naturale.',
    (1632, 'Woooooo!'):
        'Uooooooh!',
    (1633, 'Heh.'):
        'Hmpf.',
    (1634, "I can't sleep tonight."):
        'Stanotte non chiudo occhio.',
    (1635, "You're kidding."):
        'Stai scherzando.',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-main-001.jsonl'
DA, A = 1160, 1640
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
