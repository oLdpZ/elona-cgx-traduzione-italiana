# -*- coding: utf-8 -*-
"""Lotto `command-016`: le 23 voci finali della zona — le quattro carte, le
reazioni alla frase insegnata, e la notte con chi hai sposato.

Chiude 6000-6999. Dentro ci sono tre cose che non c'entrano niente fra loro e
stanno vicine solo perche' il menu del compagno le raccoglie tutte.

⭐ **I quattro nomi di carta erano gia' decisi, e con l'articolo dentro.**
`db_creature.hsp` rende 「スペード・ウォリアー」 «il guerriero di picche»
(`:38006`), 「クラブフェザー」 «la piuma di fiori» (`:37943`), 「ダイヤアイズ」
«gli occhi di quadri» (`:37880`) e 「ハート・ウィッチ」 «la strega di cuori»
(`:37816`). ⚠️ La rete 3 non li avrebbe pescati — qui il giapponese e' la frase
intera, non il nome — ma `dossier.py` per l'inglese si'.
💡 E «is treated as» non puo' diventare «e' trattato come», che concorderebbe
con la creatura: **«conta come»**, che e' anche la lingua vera dei giochi di
carte.

⭐ **«Il tuo diario e' stato aggiornato.» sta in CINQUE file**, e questo e' il
sesto: `action.hsp:8282`, `chara_func.hsp:3964`, `map.hsp:1197`,
`proc.hsp:4228`, `text.hsp:4`. Copiata parola per parola.

⚠️ **Un errore di monte che ribalta il senso**: `:6901` 「まんざらでもないようだ」
vuol dire «non gli dispiace affatto», cioe' **gli fa piacere**, e l'inglese
scrive «doesn't seem to be very happy about that». La resa segue il giapponese —
«non sembra dispiacersene affatto» — che e' anche la forma senza participio.

⚠️ **Tutta la scena finale ha il giapponese PARLATO e l'inglese DESCRITTO**, e
qui vince l'inglese. `:6939` e' 「「まだ眠くない〜」」, una battuta fra virgolette;
`:6947` e' 「「いやん、あなたったら…」」 e l'inglese lo riduce a «\\*blush\\*»;
`:6998` e' 「「はい…喜んで」」 e diventa «X blushed and nodded!». ✅ Non e' un
appiattimento da disfare: e' che **le battute giapponesi sono costruite con le
funzioni del tono** — `_yo(3)`, `_ga(3)`, `_ore(3)`, `_kure(3)` — che l'inglese
non ha e l'italiano nemmeno. Se rendessi le battute, dovrei inventare un
registro che il gioco non sa scegliere. La descrizione lo evita.

⭐ **E 「ジュア様」 e' «Jure», non «Jua».** L'inglese scrive «Lady Jua», ma il
progetto rende ジュア «Jure» in quattro file — `db_creature.hsp:72943`,
`:72961`, `:100613`, `action.hsp:14058` — che e' il nome canonico della dea
della guarigione. Il 様 cade, come cade gia' in `db_creature.hsp:72943`.

Tetto 61 caratteri (`:6863`). Una copia di giapponese e tre di inglese.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :6790-:6811 le quattro carte. ⭐ i nomi vengono da db_creature.hsp,
    #     articolo compreso. ⚠️ «e' trattato come» concorderebbe con la creatura.
    (6790, ' is treated as a spade warrior.'):
        'cdatan(CDATAN_NAME, tc) + " conta come il guerriero di picche."',
    (6797, ' is treated as a club feather.'):
        'cdatan(CDATAN_NAME, tc) + " conta come la piuma di fiori."',
    (6804, ' is treated as a diamond eyes.'):
        'cdatan(CDATAN_NAME, tc) + " conta come gli occhi di quadri."',
    (6811, ' is treated as a heart witch.'):
        'cdatan(CDATAN_NAME, tc) + " conta come la strega di cuori."',

    # --- :6825 l'icona tolta. ⚠️ rete 8: «da » + name() darebbe «da il putit»,
    #     quindi il nome passa a soggetto e il verbo e' un composto con AVERE.
    (6825, 'You deleted the item mark on .'):
        'name(tc) + " ha perso l\'icona."',

    # --- :6863-:6921 le reazioni alla frase insegnata.
    #     ⚠️ `him(tc)` e `his(tc)` sono morfologia e spariscono.
    (6863, ' becomes very curious about what you were wanting to tell ...'):
        'cdatan(CDATAN_NAME, tc) + " si domanda con ansia che cosa volevi dire..."',
    # ⭐ copiata: la stessa riga sta in cinque file
    (6869, 'Your journal has been updated.'):
        'Il tuo diario è stato aggiornato.',
    (6880, ' looks happy.'):
        'cdatan(CDATAN_NAME, tc) + " ha un\'aria felice."',
    (6883, ' seemed to think it was an exaggerated joke.'):
        'cdatan(CDATAN_NAME, tc) + " sembra averla presa per una battuta esagerata."',
    (6889, " is looking at you like you're some kind of creep."):
        'cdatan(CDATAN_NAME, tc) + " ti guarda come si guarda un tipo losco."',
    # ⚠️ errore di monte: 「まんざらでもない」 e' «non gli dispiace affatto»,
    #    cioe' il contrario di quel che dice l'inglese
    (6901, " doesn't seem to be very happy about that."):
        'cdatan(CDATAN_NAME, tc) + " non sembra dispiacersene affatto."',
    (6915, " couldn't believe  ears..."):
        'cdatan(CDATAN_NAME, tc) + " non crede alle proprie orecchie..."',
    (6918, ' gives you a look of pity.'):
        'cdatan(CDATAN_NAME, tc) + " ti guarda con pietà."',
    # ⚠️ 「やれやれ」 e' il sospiro di chi la scampa, non il sollievo del corpo
    (6921, ' shrugged  shoulders in relief.'):
        'cdatan(CDATAN_NAME, tc) + " alza le spalle con un sospiro."',

    # --- :6934-:6947 la notte con chi hai sposato, e i tre rifiuti del gioco.
    (6934, "You can't make a gene in this game mode."):
        'In questa modalità non si possono lasciare geni.',
    (6939, " isn't sleepy yet."):
        'cdatan(CDATAN_NAME, tc) + " non ha ancora sonno."',
    (6944, 'It seems that  wants to get out of here.'):
        '"Sembra che " + cdatan(CDATAN_NAME, tc) + " voglia andarsene da qui."',
    (6947, '*blush*'):
        '*arrossisce*',

    # --- :6955-:6978 le guardie di Jure. ⭐ 「ジュア」 e' «Jure» in quattro file.
    (6955, ': \\"Stop this at once! Lady Jua says she doesn\'t want to!\\"'):
        'cdatan(CDATAN_NAME, cnt) + ": \\"Smettila subito! Jure ha detto di no!\\""',
    (6978, ': \\"I won\'t forgive you for that.\\"'):
        'cdatan(CDATAN_NAME, cnt) + ": \\"Questo non te lo perdono!\\""',

    # --- :6987-:6998 le due risposte no e quella si'. Lo spazio in coda delle
    #     prime due e' dell'inglese.
    (6987, '... gently refuses your proposal. '):
        '"..." + cdatan(CDATAN_NAME, tc) + " rifiuta con garbo. "',
    (6993, '... sadly refuses your proposal. '):
        '"..." + cdatan(CDATAN_NAME, tc) + " rifiuta con dispiacere. "',
    (6998, '... blushed and nodded!'):
        '"..." + cdatan(CDATAN_NAME, tc) + " arrossisce e annuisce!"',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-016.jsonl'
DA, A = 6790, 6998
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
