# -*- coding: utf-8 -*-
"""Lotto `command-011`: i 28 pensieri di `*com_knowOther`, seconda meta' — e
`*com_knowOther` e' chiuso.

Segue il `command-010` nella stessa cascata di `if`, e prende i blocchi che
parlano di quando il compagno **sta male**: stamina a terra, vita sotto un
quarto, e le tredici condizioni (cecita', ubriachezza, immobilizzazione,
paralisi, ira, confusione, ottundimento, lavaggio del cervello, veleno,
malattia, paura, soffocamento, sonno, follia).

⭐ **E l'ultima riga vince su tutte: `:1783` e' `if ( tc == CHARA_PLAYER )`.**
Quando il bersaglio della telepatia sei tu, il gioco butta via qualunque
pensiero avesse scelto e stampa 「自分の心を覗くのは奇妙な感じだ」. Una battuta
sola, e sta in fondo alla cascata proprio per sovrascrivere le altre
ventisette.

⭐⭐ **Due pensieri dipendono dal MASOCHISMO del compagno, non dalla sua vita.**
Con la vita sotto un quarto il blocco tira `rnd(3)`, ma poi `:1721` e `:1724`
guardano `CDATA_MASTER_SERVANT2`: sopra +5 esce 「痛い痛い嫌だ死にたくない」 —
il panico — e sotto -5 esce 「なんだかゾクゾクする」, cioe' che la cosa gli
**piace**. Le due rese vanno tenute lontane l'una dall'altra come le tiene il
sorgente: «Ahi ahi no non voglio morire» contro «Che brivido...».

⭐ **`:1750` e' in KATAKANA, e il katakana qui e' la voce.** 「命令ヲ実行スル」 e'
「命令を実行する」 scritto tutto in katakana, che in giapponese e' la lingua dei
robot e delle cose senza volonta': la condizione e' il **lavaggio del
cervello**. L'inglese lo appiattisce in «Trying to execute the order». ✅ In
italiano il maiuscolo fa lo stesso mestiere: «ESEGUO L'ORDINE».

⚠️ **Un errore di monte**: `:1703` 「なんかどうでもよくなってきた」 e' «comincia a
non importarmi piu' niente» — l'apatia della stanchezza — e l'inglese scrive
«It keeps getting more difficult...», che parla di fatica invece che di
disinteresse.

💡 `:1732` 「なんだか愉快♪」 tiene la **crome**, che l'inglese butta via
(«Somewhat funny»): e' l'ubriachezza, e la nota dice il tono meglio
dell'aggettivo. `guardie.py` la lascia passare apposta — e' l'unica eccezione
alla regola sulla doppia larghezza.

Tetto 52 caratteri (`:1784`); la resa piu' lunga ne fa 39. Zero copie da
`dossier.py`.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1700-:1709 la stamina a terra, `rnd(4)`.
    (1700, 'Want to rest'):
        'Voglio riposare',
    # ⚠️ errore di monte: il giapponese e' l'apatia, non la fatica
    (1703, 'It keeps getting more difficult...'):
        'Comincia a non importarmi più niente',
    (1706, 'Do I really need to work this hard?'):
        'Devo per forza sforzarmi ancora?',
    (1709, 'Well, that was unpleasant'):
        'Ecco perché non volevo',

    # --- :1713-:1725 la vita sotto un quarto. ⚠️ le ultime due non dipendono
    #     dal `rnd(3)` ma da `CDATA_MASTER_SERVANT2`: il panico e il piacere.
    (1713, 'I may die'):
        'Potrei morire',
    (1716, 'I can not afford to fall down yet'):
        'Non posso cadere adesso',
    (1719, 'I am not going to die here'):
        'Non è qui che voglio morire',
    (1722, 'I do not want to die...'):
        'Ahi ahi no non voglio morire',
    (1725, 'I am excited'):
        'Che brivido...',

    # --- :1729-:1780 le tredici condizioni, una riga per condizione.
    (1729, 'Anxious that can not see anything'):
        'Non vedo niente, che angoscia',
    # 💡 la croma la porta il giapponese, e l'inglese la butta via
    (1732, 'Somewhat funny'):
        'Che allegria♪',
    (1735, 'Wants to escape by some means'):
        'Devo trovare il modo di scappare!',
    (1738, 'Regret that can not move'):
        'Non riesco a muovermi, che frustrazione',
    (1741, 'Can not stop anger'):
        'La rabbia non passa!',
    (1744, 'Scattered in head'):
        'Mi gira tutto in testa',
    (1747, 'Misty on head'):
        'Ho come una nebbia in testa',
    # ⭐ il katakana e' la voce di chi non decide piu': il maiuscolo fa lo stesso
    (1750, 'Trying to execute the order'):
        "ESEGUO L'ORDINE",
    (1753, 'In a bad mood'):
        'Mi sento male',
    (1756, 'Painful a poor physical condition'):
        'Sto poco bene, che fatica',
    # ⚠️ il giapponese la dice due volte, ed e' il panico: si tiene
    (1759, 'Have to run away'):
        'Devo scappare devo scappare',
    (1762, 'Painful that can not breathe'):
        'Non respiro! Che agonia...',
    (1765, 'Playing with the sheep in dream'):
        'Nel sogno gioco con le pecore',
    (1768, 'Obsession'):
        'Un pensiero fisso non mi lascia',
    (1771, 'Scared with fear'):
        'Il terrore mi confonde tutto',
    (1774, 'Suffering from trauma.'):
        'Un vecchio trauma mi tormenta',
    # ⚠️ 「あなたに殺される」: l'allucinazione e' che a ucciderlo sia TU
    (1777, 'Looking at the hallucination killed by you'):
        'Ti vedo uccidermi, e non è vero',
    (1780, 'Suffers from a suicide impulse.'):
        'Resisto alla voglia di farla finita',

    # --- :1784 quando il bersaglio sei tu: sovrascrive tutte le altre.
    (1784, "It's a strange feeling looking into one's own heart."):
        'Guardarsi dentro fa un effetto strano',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-011.jsonl'
DA, A = 1699, 1784
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
