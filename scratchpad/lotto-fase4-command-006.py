# -*- coding: utf-8 -*-
"""Lotto `command-006`: i 45 pregi di `*setHistory3`, la TESTA della terza frase
del «Background».

⭐⭐ **Questa riga e' meta' di una frase, e l'altra meta' e' `*setHistory4`.**
`chara.hsp:3322`-`:3330` disegna `ohanasi3` e `ohanasi4` su due righe
consecutive, e in giapponese la prima finisce in 「〜が、」 — la congiuntiva
avversativa — mentre la seconda chiude il periodo col punto:

    温厚で慈悲深いが、          ->  Mitezza e generosità, ma
    熱中すると周りが見えなくなる。 ->  la passione fa perdere di vista tutto il resto.

⚠️⚠️ **E le due meta' si tirano a sorte SEPARATAMENTE**: `ohanasi3` e `ohanasi4`
sono due `rnd(45) + 1` indipendenti (`chara.hsp:3261`-`:3262`), quindi ognuno dei
45 pregi deve saldarsi a ognuno dei 43 difetti — 1.935 frasi possibili. La resa
non puo' concordare la testa con la coda in niente: ne' genere, ne' numero, ne'
soggetto. ✅ Il nominale lo garantisce per costruzione, ed e' il motivo per cui
questa riga il registro nominale lo pretende invece di limitarsi a preferirlo.

✅ **Ogni testa finisce in «, ma»**, che e' il posto in cui il giapponese mette
「が、」. L'inglese fa il contrario e mette «Though» in **testa** — «Though you
are gentle and merciful,» — che in italiano vorrebbe «Per quanto mite e
generoso,», cioe' due aggettivi accordati col giocatore. La congiunzione in coda
e' la stessa manovra della rete 9, applicata a una avversativa invece che a
una copulativa.

💡 **I pregi sono AGGETTIVI in inglese e SOSTANTIVI in italiano**, ed e' la
tabella di `guida-stile.md` («Starving» -> «Inedia») usata quarantacinque volte:
«Though you are calm and collected» -> «Sangue freddo e buon giudizio».
⚠️ Dove il pregio nomina per forza la persona, torna il nome di genere fisso:
`:9837` «strong leadership» -> «Una **guida** forte per gli altri».

Tetto 57 caratteri (`:9831`), misurato con `scratchpad/misura-background.py`;
la resa piu' lunga ne fa 47. Zero copie da `dossier.py`.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :9735-:9867 i quarantacinque pregi. Ognuno chiude in «, ma» perche' la
    #     riga dopo e' un difetto tirato a sorte a parte: vedi il docstring.
    (9735, 'Though you are gentle and merciful,'):
        'Mitezza e generosità, ma',
    (9738, 'Though you are a genius,'):
        'Un cervello geniale, ma',
    (9741, 'Though you are friends with everyone,'):
        'Amicizia con tutti, ma',
    (9744, 'Though you are always polite,'):
        'Buone maniere e precisione, ma',
    (9747, 'Though you know many things,'):
        'Un sapere vasto, ma',
    (9750, 'Though you have a keen eye,'):
        'Occhio acuto, ma',
    (9753, 'Though you are calm and collected,'):
        'Sangue freddo e buon giudizio, ma',
    # ⚠️ 「ムードメーカー」 e' chi tira su gli altri, non chi fa festa
    (9756, 'Though you are the life of the party,'):
        'Allegria che contagia gli altri, ma',
    (9759, 'Though you are ordinary,'):
        'Una normalità di fondo, ma',
    (9762, 'Though you are bold and daring,'):
        'Ambizione e voglia di sfide, ma',
    (9765, 'Though you never give up,'):
        'Mai una resa, ma',
    (9768, 'Though you are always strict with yourself,'):
        'Serietà e severità con se stessi, ma',
    (9771, 'Though you are passionate,'):
        'Un carattere schietto e caldo, ma',
    (9774, 'Though highly proactive,'):
        "Una gran capacità di agire, ma",
    (9777, 'Though bold and courageous,'):
        'Audacia e fegato, ma',
    (9780, 'Though good at supporting others,'):
        'Un gran talento nel dare una mano, ma',
    (9783, 'Though enduring hardships,'):
        'Tempra da resistere alle sventure, ma',
    (9786, 'Though curious and sociable,'):
        'Curiosità e simpatia, ma',
    (9789, 'Though have an excellent memory,'):
        'Una memoria formidabile, ma',
    (9792, 'Though adapt to different environments,'):
        'Adattamento rapido a ogni ambiente, ma',
    (9795, 'Though have extraordinary imagination,'):
        "Un'inventiva fuori dal comune, ma",
    (9798, "Though doesn't leave people in trouble alone,"):
        'Mai un occhio chiuso su chi è nei guai, ma',
    (9801, 'Though remains confident even in times of crisis,'):
        'Portamento saldo anche nei momenti neri, ma',
    (9804, 'Though have a strong sense of responsibility,'):
        'Un senso di responsabilità come nessuno, ma',
    (9807, 'Though have the ability to bring everyone together,'):
        'Il polso per tenere insieme tutti, ma',
    (9810, 'Though have virtue and is loved by everyone,'):
        "Virtù, e l'affetto di tutti, ma",
    (9813, 'Though have strong loyalty and kindness,'):
        'Lealtà e cuore, ma',
    (9816, 'Though think flexibly according to the situation,'):
        'Pensiero elastico secondo il momento, ma',
    (9819, 'Though always easygoing,'):
        'Una leggerezza costante, ma',
    (9822, 'Though have a strong resolve,'):
        'Una determinazione nascosta, ma',
    (9825, 'Though have no ulterior motives and are straightforward,'):
        'Nessun doppio fine, tutto alla luce del sole, ma',
    (9828, 'Though good at gathering information,'):
        'Un fiuto per le notizie, ma',
    (9831, 'Though never get depressed even when worst things happen,'):
        'Nessuno scoramento, per male che vada, ma',
    (9834, 'Though good at identifying the good points of others,'):
        'Un occhio per i pregi degli altri, ma',
    # ⚠️ «leader» ha un genere addosso: «guida» e' il nome di genere fisso
    (9837, 'Though possesses strong leadership,'):
        'Una guida forte per gli altri, ma',
    (9840, "Though doesn't sweat the small stuff,"):
        'Nessun pensiero per le piccolezze, ma',
    (9843, 'Though good at taking care of others,'):
        'Alla fine, cura per gli altri, ma',
    # ⚠️ 「格下相手にも」: la guardia non cala nemmeno contro i piu' deboli
    (9846, 'Though never let guard down,'):
        'Mai la guardia bassa, nemmeno coi deboli, ma',
    (9849, 'Though show true worth in times of crisis,'):
        'Il vero valore esce nei guai, ma',
    (9852, 'Though kind and tolerant,'):
        'Dolcezza e larghezza di vedute, ma',
    (9855, 'Though good at paying attention to small details,'):
        'Attenzioni minute per chiunque, ma',
    (9858, 'Though work hard for others,'):
        'Ogni sforzo, se è per qualcuno, ma',
    (9861, 'Though have the ability to see the big picture,'):
        'Uno sguardo che abbraccia tutto, ma',
    (9864, 'Though value bonds with others,'):
        'I legami con gli altri contano, ma',
    (9867, 'Though have the strength to not rely on anyone,'):
        'La forza di non dipendere da nessuno, ma',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-006.jsonl'
DA, A = 9733, 9870
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
