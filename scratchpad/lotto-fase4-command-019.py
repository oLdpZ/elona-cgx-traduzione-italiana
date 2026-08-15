# -*- coding: utf-8 -*-
"""Lotto `command-019`: la coda della scheda dei talenti e il diario dei ranghi.
Chiude la zona 2000-2999.

⚠️⚠️ **Sette delle diciannove voci NON si vedranno mai in italiano, e la ragione
e' una forma nuova di riga spenta: il ramo della lingua.** `command.hsp:2954`
apre un `if ( jp ) { ... }` lungo settanta righe — le statistiche
dell'avventura, «最深攻略階層」, 「世界移動距離」, 「総睡眠時間」 — e dentro ci
sono sette `lang()` vere: `:2956` « level», `:2962` « Miles», `:2970` « Hours»,
`:2971` « Days», `:2976` « Guest», `:2982` « Plat», `:2986` « points». Il ramo
`else` (`:3022`) stampa le stesse statistiche **in inglese nudo**, dentro un
blocco `ANNA CUSTOM`, fuori da ogni `lang()`: «Your stats so far:», «@BL
Deepest Lvl : ». Chi gioca in italiano legge quelle, non queste.
✅ Rinviate tutte e sette, col motivo per esteso.
⚠️ **E' una famiglia nuova di riga morta**, la terza dopo il `;` e il
`/* ... */`: qui la riga e' viva, il file e' vivo, la `lang()` e' vera — e' il
**ramo** a non girare mai. La rete 6 non la vede, `commenti-blocco.py` nemmeno,
e nessun conteggio di «non tradotte» la distingue da lavoro utile.
💡 `else_jp.py` guardava lo stesso costrutto **dall'altro lato**: cercava
l'inglese nudo dentro l'`else`. Il rovescio — la `lang()` sprecata dentro il
ramo `jp` — non lo cercava nessuno.

⭐ **Il genitivo sassone di `:2640` si scioglie coi due punti.** Il sorgente
scrive `cnven(cdatan(CDATAN_NAME, tc)) + lang("の特性", "'s Trait")`: il nome
arriva **prima** e la resa puo' solo seguirlo, quindi «Tratti di X» non e'
scrivibile. ✅ «X: i tratti», che e' la strada dei due punti del `map-005` e la
stessa cosa che fa il giapponese col の.

⭐ **`:2637` e' l'unica riga della schermata che PUO' dare del tu**, e non e' una
svista: il sorgente la mette dentro `if ( tc == CHARA_PLAYER )` (`:2636`) e nel
ramo `else` scrive tutt'altra frase, quella di `:2640`. Dove la persona e'
garantita dal sorgente, il registro nominale non serve. ✅ Anche qui pero' la
resa resta impersonale — «Restano N talenti da prendere» — perche' non costa
niente e la riga e' piu' corta.

⚠️ **`:2543` e' una rete 10**: `his(tc, 1)` sceglie il possessivo sul genere del
possessore e restituisce un valore solo, quindi il nome che lo segue dev'essere
**maschile singolare**. «equipaggiamento» lo e'. ⚠️ `cnven` non e' morfologia
(`funzioni.py`) e resta.

⚠️ **La rete 3 ha parlato su 「仲間」, e la divergenza c'era gia'**: `text.hsp:32`
lo rende «Alleato» al singolare, `command.hsp:1270` «Alleati» al plurale. Non e'
una resa nuova ne' una scelta di questo lotto — sono due siti diversi, il titolo
di una finestra e l'etichetta di un tasto — e qui vince **quella del file**,
`:1270`, che e' la stessa lista di compagni a cui `z,x` fa passare. 💡 La rete 3
mostra solo la resa divergente, non quella che coincide: leggere il suo avviso
senza cercare le altre gemelle avrebbe fatto sembrare unica una resa che unica
non e'.

Copiate senza decidere niente: «Fama» (`command.hsp:10517`), «monete d'oro»
(`proc.hsp:7056` e altri sei siti), «Alleati» (`command.hsp:1270`, lo stesso
giapponese nello stesso file), «Conferma» per 「決定」 (`command.hsp:1319`).
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :2543 la riga degli incantesimi dell'equipaggiamento.
    #     ⚠️ rete 10: his(tc, 1) vuole un nome maschile singolare accanto, e
    #     «equipaggiamento» lo e'. `cnven` non e' morfologia e resta.
    (2543, ' equipment '): 'cnven(his(tc, 1)) + " equipaggiamento "',

    # --- :2589 il titolo della finestra e la riga dei tasti.
    (2589, 'Feats and Traits'): 'Talenti e tratti',
    # 「決定」 e' «Conferma» in command.hsp:1319.
    (2589, 'Enter [Gain Feat]  '):
        '"Conferma [prendi un talento]  " + strhint2 + strhint3',
    # ⭐ 「仲間」 e' gia' «Alleati» a command.hsp:1270, stesso file.
    (2589, 'Ally'): 'Alleati',

    # --- :2637-:2640 le due note in fondo, una per te e una per il compagno.
    (2637, 'You can acquire  feats'):
        '"Restano " + gdata(GDATA_TRAIT_POINT) + " talenti da prendere"',
    # ⭐ il genitivo sassone non e' scrivibile: il nome arriva prima. Due punti.
    (2640, "'s Trait"): ': i tratti',

    # --- :2738 il rifiuto.
    (2738, 'You already have maxed out the feat.'):
        'Questo talento è già al massimo.',

    # --- :2897-:2911 il diario dei ranghi. ⭐ «Fama» da command.hsp:10517,
    #     «monete d'oro» da proc.hsp:7056 e altri sei siti.
    (2897, 'Fame: '): 'Fama: ',
    (2902, 'Pay: About  gold pieces '):
        '"Paga: circa " + calcincome(cnt) + " monete d\'oro  "',
    (2905, '\\nDeadline: '): '\\nScadenza: ',
    # 「日以内」 e' «entro N giorni»: l'inglese dice «Days left», e la resa sta
    # in coda al numero.
    (2905, ' Days left'): ' giorni',
    # ⚠️ `cnvrank` la porta solo l'inglese, ed e' contenuto: resta.
    (2911, 'EX Arena Wins:  Highest Level:'):
        '"Arena EX: " + gdata(GDATA_EX_BATTLE_WIN) + " vittorie  livello massimo " + cnvrank(gdata(GDATA_EX_BATTLE_MAX_LVL))',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {
    # Le sette `lang()` dentro il ramo `if ( jp )` di :2954-:3021: il ramo
    # `else` stampa le stesse statistiche in inglese nudo, fuori da ogni
    # `lang()`. In italiano non si vedono mai.
    (2956, ' level'),
    (2962, ' Miles'),
    (2970, ' Hours'),
    (2971, ' Days'),
    (2976, ' Guest'),
    (2982, ' Plat'),
    (2986, ' points'),
}

USCITA = 'lavoro/fase4-command-019.jsonl'
DA, A = 2543, 2999
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
