# -*- coding: utf-8 -*-
"""Il rito del lupo mannaro, l'esecuzione, l'assassino e il banchetto.

`event.hsp:366`-`:673`, cioe' i quattro eventi casuali di citta' che stanno in
fila nello `switch`. Ventisette voci, e sono la prima apertura di `event.hsp`
(649 da fare).

⭐ **Il lotto nasce da una schermata di collaudo**, non da un elenco: la 59a ha
chiesto una finestra `*re_select` per misurarne il tetto, e quella che e'
arrivata era proprio questo evento, in corso nella partita di chi collauda.

## ⚠️ L'inglese di monte sbaglia l'evento, e stavolta e' dimostrabile

`:442` sta dentro `if ( wolf == 0 )`: non e' rimasto nessun lupo, il contatore
va a zero, suona `SOUNDLIST_COMPLETE1`, e la riga dopo (`:444`) dice che il rito
e' **fallito** e che vincono i cittadini. Il giapponese scrive 【人狼遊儀が失敗】,
«fallito». L'inglese scrive «in progress», che e' la riga di `:525` — quella del
rito che prosegue.
💡 La copia si vede anche dalla punteggiatura: `:525` chiude con `/200 > ` e
`:442` con `/200> `, senza lo spazio. Chi copia una riga si porta dietro tutto
tranne uno spazio.
✅ La resa segue il giapponese. E' la lezione della 58a in un file nuovo, e qui
non serve nemmeno un referto per vederla: basta leggere la riga di sotto.

## ⚠️ E appiattisce due volte

1. `:518` rende 狼の襲撃 — «l'attacco del lupo», che e' il nome dell'EVENTO — con
   «Werewolf», che e' il nome della CREATURA (`ai.hsp:117`, «il lupo mannaro»).
   E' l'appiattimento di `decisioni.md` §«L'inglese riscrive, e in cinque modi»:
   il giapponese distingue, l'inglese fonde. La resa segue il giapponese.
2. `:520` e `:654` sono due eventi diversi con due giapponesi diversi — l'uno ha
   l'ululato del lupo, l'altro il grido 「人殺し、人殺しだ！！」 — e in inglese
   diventano quasi la stessa frase, con le guardie che corrono in tutt'e due.
   Le rese tengono cio' che i due giapponesi non hanno in comune.

## ✅ E una volta l'inglese sfonda il riquadro, mentre il giapponese ci sta

`:521` e' la voce di menu che il collaudo ha visto uscire dalla pergamena:
48 caratteri contro un tetto di **40** (`bg_re9`, 280 px utili). E' rotta a
monte, per tutti. La resa italiana dice la stessa cosa in 34.
⚠️ Il tetto e' quello **corretto oggi** — 7 px per carattere, non 7,7. Col metro
vecchio sarebbe stato 36, e la resa da 34 sarebbe passata lo stesso: qui la
correzione non cambia l'esito, cambia il margine.

## I tre riquadri di questo lotto

    :415  bg_re7    360 px utili   tetto 51    l'esecuzione
    :519  bg_re9    280 px utili   tetto 40    il lupo mannaro
    :653  bg_re9    280 px utili   tetto 40    l'assassino
    :662  bg_re10   320 px utili   tetto 45    il banchetto
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :402 / :491 l'urlo di chi viene giustiziato e di chi viene sbranato.
    # ⚠️ rete 11: `name` e `cnvtalk` sono funzioni di contenuto e restano.
    # 💡 ぎゃぁーー e' un grido acuto di dolore: db_creature ha gia' «Aaahhh...»
    #    per あぁぁ (:50828), che e' un lamento. Qui serve l'altro.
    (402, ' screams, Ahhhhhhh!'):
        'name(tc) + " urla, " + cnvtalk("Aaargh!")',
    (491, ' screams, Ahhhhhhh!'):
        'name(p) + " urla, " + cnvtalk("Aaargh!")',

    # --- :407 il valore della citta'. Nessun termine fissato prima.
    (407, 'City property value was increased 5. (Total: )'):
        '"Il valore della città è salito di 5. (Totale: " + '
        'mdata(MDATA_CITY_PROPERTY_VALUE) + ")"',

    # --- :410 / :413 i due contatori. La forma «[X attuale: n]» viene da
    #     proc.hsp:4135; «ispirazione» da action.hsp:7814, «esperienza di
    #     viaggio» da main.hsp:8475.
    (410, ' You got inspired. [Currently:]'):
        '" Hai avuto un\'ispirazione. [Ispirazione attuale: " + '
        'gdata(GDATA_FLAG_MANUSCRIPT_IDEAS) + "]"',
    (413, ' You gained a good amount of travel experience. [Currently:]'):
        '" Hai guadagnato molta esperienza di viaggio. [Esperienza attuale: " + '
        'gdata(GDATA_TRAVEL_DISTANCE) + "]"',

    # --- :414-:417 l'esecuzione del sospetto (bg_re7, tetto 51).
    (414, 'Time of execution'):
        "L'ora dell'esecuzione",
    (416, 'From somewhere in the town, a faint painful shriek of execution could be heard.'):
        'Da qualche parte in città si è udito il grido soffocato del condannato.',
    # ⚠️ rete 13: lo stesso «Sorry for you.» sta anche a :655, e i due giapponesi
    #    sono diversi — 南無 in kanji qui, なむ… in kana e sospeso la'. La
    #    distinzione e' di registro e va tenuta: qui e' una preghiera detta
    #    intera, la' un borbottio.
    (417, 'Sorry for you.'):
        'Che riposi in pace.',

    # --- :442 ⚠️⚠️ IL GIAPPONESE, non l'inglese. Vedi il docstring.
    (442, '< Werewolf-RitualGame in progress: /200> '):
        '"< Rito del lupo mannaro fallito: " + '
        'mdata(MDATA_WEREWOLF_PROGRESS) + "/200 > "',
    (444, "The wolves' ritual failure was confirmed. It's a victory for the citizens."):
        'Il fallimento del rito dei lupi è confermato. Vincono i cittadini.',

    # --- :511-:525 l'attacco del lupo mannaro (bg_re9, tetto 40).
    (511, '[A werewolf has caused havoc. People should vote on whom they suspect it being.] '):
        '[Un lupo mannaro ha fatto una vittima. Gli elettori votino per mandare '
        'al patibolo chi sospettano.] ',
    # ⚠️ appiattimento: 狼の襲撃 e' l'evento, «Werewolf» e' la creatura.
    (518, 'Werewolf'):
        "L'attacco del lupo",
    (520, 'Suddenly, a painful shriek and the howling of a wolf rises from somewhere in the town. You see several guards hastily running by.'):
        "Da qualche parte in città si sono levati l'ululato di un lupo e un grido "
        'di dolore. Vedi delle guardie correre in fretta.',
    # ⚠️ rotta a monte: 48 caratteri in un riquadro da 40. La resa ne usa 34.
    (521, 'The werewolf had murdered someone in cold blood!'):
        'Il lupo ha ucciso a sangue freddo!',
    (525, '< Werewolf-RitualGame in progress: /200 > '):
        '"< Rito del lupo mannaro in corso: " + '
        'mdata(MDATA_WEREWOLF_PROGRESS) + "/200 > "',

    # --- :548 / :601 i due finali. 神狼 e' <Lupo Divino> sulla carta
    #     (db_card.hsp:231), 妖狐 «la volpe ammaliatrice» (ai.hsp:184), 九尾 «la
    #     volpe a nove code» (action.hsp:17620, 弟九尾).
    (548, "The sacrifice was made so that the total level was 200 or more, so a wolfgod descended. It's a victory for the wolves."):
        'I sacrifici hanno raggiunto il livello 200 e il lupo divino è sceso in '
        'terra. Vincono i lupi.',
    (601, "A fox that had been hiding out takes over Werewolf-RitualGame, so a foxgod descended. It's a victory for the fox."):
        'La volpe ammaliatrice che si era nascosta ha preso il controllo del rito '
        'e la volpe a nove code è scesa in terra. Vincono le volpi.',

    # --- :652-:655 l'assassino (bg_re9, tetto 40).
    (652, 'Murderer'):
        "L'assassino",
    # ⚠️ il grido 「人殺し、人殺しだ！！」 c'e' nel giapponese e non nell'inglese:
    #    e' l'unica cosa che distingue questa finestra da :520.
    (654, 'Suddenly, a painful shriek rises from somewhere in the town. You see several guards hastily run by.'):
        # ⚠️ le virgolette caporali non esistono in CP932 e `reimporta` le
        #    boccia. La citazione dentro una statica si scrive con lo escape
        #    dello HSP, come `action.hsp:3094`.
        'Da qualche parte in città si è levato un grido. Vedi delle guardie '
        "correre in fretta. \\\"All'assassino, all'assassino!!\\\"",
    (655, 'Sorry for you.'):
        "Pace all'anima sua...",

    # --- :661-:669 il banchetto misterioso (bg_re10, tetto 45).
    (661, 'Strange Feast'):
        'Un banchetto misterioso',
    (663, 'You come across a strange feast.'):
        'Ti trovi davanti un banchetto.',
    # ⚠️ rete 3: 食べる e' gia' «Mangia» in `text.hsp:135` — ma li' e' il titolo
    #    del comando d'inventario (`invtitle`, in fila con «Esamina» e «Lascia»),
    #    e qui e' una voce di menu di `*re_select`. E' il posto a decidere: lo
    #    stile delle voci di questo menu e' l'INFINITO, fissato dal lotto della
    #    58a sul minigioco delle orecchie («Raschiare con cura», «Far scoppiare
    #    il condotto», «Regolare la misura»). La coppia resta coerente con se'
    #    stessa e con le sue vicine.
    (664, '(Eat)'):
        '(Mangiare)',
    (665, '(Leave)'):
        '(Andarsene)',
    # ⚠️ rete 0: tre lang() sulla stessa riga :669, con inglesi diversi: la
    #    chiave corta basta.
    (669, 'It was tasty.'):
        'Era buono.',
    (669, 'Not bad at all.'):
        'Niente male.',
    (669, 'You smack your lips.'):
        'Ti sei leccato i baffi.',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-event-001.jsonl'
DA, A = 350, 700
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\event.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_event.jsonl', encoding='utf-8') if l.strip()]
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
# vive. `event.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
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
# `event.hsp:13` compone la lista degli oggetti sulla casella con
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
