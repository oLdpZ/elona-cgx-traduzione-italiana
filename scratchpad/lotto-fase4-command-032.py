# -*- coding: utf-8 -*-
"""Lotto `command-032`: **la scheda dell'equipaggiamento** — le righe d'attacco
di `*show_weaponStat`, i cinque avvisi sul peso dell'arma e l'intestazione della
finestra `*com_wear`. Sedici rese e **una rinviata**.

⭐⭐⭐ **La resa di quattro etichette non l'ho scelta io: l'aveva già scelta
`buff.hsp:679`, e in questa stessa opposizione.** Le righe d'attacco sono una
colonna di quattro voci — 「武器」, 「格闘」, 「射撃」, 「命中」 — e le prime tre la rete 3
le dava già rese altrove, ma **in un altro mestiere**: `text.hsp:59` ha 武器 come
**categoria d'inventario** al plurale («armi»), `skill.hsp:161` ha 格闘 come **nome
di abilità** («Arti marziali»), `skill.hsp:387` ha 射撃 come nome dell'abilità di
tiro («Mira»).
✅ **A sciogliere il nodo è stato `buff.hsp:679`**, dove 「射撃力上昇/命中率上昇」 è già
reso «Tiro e **mira**»: lì i due termini compaiono **affiancati**, ed è la stessa
opposizione di questa colonna. Quindi 射撃 è «Tiro» e 命中 è «Mira», e la «Mira» di
`skill.hsp:387` è il nome dell'**abilità** Mira, non di questa colonna.
`skill.hsp:1277` conferma dall'altro lato: 命中率上昇 è «+mira».
💡 **La lezione**: quando la rete 3 accusa, la domanda non è «chi ha ragione fra
me e lei» ma «in che mestiere stava la resa che cita». Tre delle quattro rese di
questa colonna divergono da lei, e tutt'e tre perché il sito citato è un nome di
abilità o una categoria, non un'etichetta di riga.

⚠️⚠️ **E la colonna è larga sei caratteri, il che è la ragione per cui le rese
lunghe non erano scrivibili comunque.** `*com_skill_calcAttack` stampa `s(1)` a
`wx + 422` (`:12429`) e i dadi del danno a `wx + 460 + en * 8`, cioè `wx + 468`
nel ramo italiano (`:12452`): sono **46 px**, cioè 6,4 caratteri in Courier a
corpo 12. «Arti marziali» ne avrebbe fatti tredici, novantaquattro pixel, sopra
la colonna dei dadi. ⚠️ E upstream ci sfora già: «Unarmed» è di sette.
⚠️ Più stretta ancora l'etichetta di 「命中」: sta a `wx + 590` e la percentuale a
`wx + 625 - en * 8` = `wx + 617` (`:12444`), cioè **27 px**. «Mira» ne occupa 29:
due pixel di sconfinamento, un quarto di carattere, meno di quello che upstream
si permette con «Unarmed».

⭐⭐ **L'inglese appiattisce due scene in una, e stavolta la rete 11 non c'entra:
sono dinamiche, ma le funzioni coincidono.** `:12488` e `:12495` hanno lo
**stesso** inglese — «is too heavy for two-wield fighting style.» — e due
giapponesi diversi, perché il sorgente li raggiunge da due rami opposti:
`:12485` è `if ( attacknum == 1 )`, cioè l'arma della **mano principale** che
pesa 4 kg o più (「利手で扱うにも重すぎる」, «troppo pesante perfino per la mano
dominante»); `:12492` è l'`else`, cioè l'arma **secondaria** sopra i 1500
(「片手で扱うには重すぎる」, «troppo pesante per una mano sola»). Tutt'e due portano
`itemname` e nient'altro in tutt'e due le lingue, quindi la rete 11 **autorizza**
e l'italiano può rimettere la distinzione che l'inglese aveva buttato. È la
famiglia di `:15636` della 46ª.

⚠️⚠️ **E i cinque avvisi sul peso hanno un nodo che l'inglese non ha: il
GENERE.** «is too light» non concorda con niente, «troppo leggera» concorda con
`itemname(cw)`, che può essere «la spada» o «il martello». Non si può sapere a
scrittura. ✅ La manovra è quella di sempre e qui rende tutte e cinque: si passa
al **verbo**, che al presente non ha genere — «pesa troppo», «pesa troppo poco»,
«si impugna bene» — e l'accordo sparisce dal problema. ⚠️ Anche «per usarla a
cavallo» sarebbe stato un accordo nascosto dentro un pronome: la resa è «per
l'uso a cavallo».

⚠️⚠️ **`:12636` è rinviata, ed è la prima volta che una riga risulta morta in
TUTTI E QUATTRO i siti in cui è scritta.** È l'intestazione delle resistenze,
「火 冷 雷 闇 幻 毒 獄 音 神 沌 魔」 / «Fi Co Li Da Mi Po Nt So Nr Ch Ma», e compare a
`:12636`, `:12645`, `:14127` e `:14136`. Le prime e le terze stanno nel blocco
`ORIGINAL` spento; **le seconde e le quarte stanno nel blocco `ANNA CUSTOM`, che
è spento anche lui.**
💡 **E questo si vede solo leggendo il delimitatore**: `:12639` è
`/********** ANNA CUSTOM - BEGINNING ********** // Show skills on 'z' toggle`,
**senza la barra finale**, e a chiuderlo è `********** ANNA CUSTOM - ENDING
**********/` a `:12670`. Dove invece il blocco è vivo la riga si scrive
`/********** X - ENDING **********/` con la barra da tutt'e due i lati, come
`:12673` e `:14118`. La barra è l'unica differenza fra un blocco acceso e uno
spento, e non la guarda nessuno se non `commenti-blocco.py`.
✅ **A disegnare davvero le resistenze è MMAH**: `:12672` è
`display_show_resist showresist, ...`, una riga viva fra due marcatori
autochiusi. Le due versioni di monte sono state sostituite, non spente per
sbaglio. ⭐ **Quindi la rete 6 corretta nella 45ª ha fatto esattamente il lavoro
per cui era stata corretta**: boccia solo se sono spente tutte le occorrenze, e
qui lo sono.

⭐ Riscosso senza decidere: **«Mano\\*»** viene da `bodyn` (`text.hsp:136`, «Mano»),
che è la colonna in cui 「利手」 si sostituisce; e sta nei 42 px fra `wx + 46` e la
lettera di scelta a `wx + 88` (`:12698`, `:12709`).

💡 **Una misura che è avanzata**: la riga del peso di `:12674` è **destra**
(`display_note`, `module.hsp:4360`, `wx + ww - strlen * 7 - 140`), quindi su una
finestra da 690 il tetto è di **75 caratteri** — e l'inglese, con
«(Medium)» e un DV/PV a tre cifre, ci arriva. La resa italiana con « Mira:» e
« Danno:» ne fa 62, e il margine serve: 「(重いです)」 di `screen.hsp` non è ancora
tradotto e crescerà.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # *show_weaponStat / *com_skill_calcAttack — le righe d'attacco
    # ================================================================
    # ⚠️ Colonna da 46 px = 6,4 caratteri (:12429 contro :12452). Tutte e tre
    #    divergono dalla rete 3, e tutte e tre perche' il sito che cita e' un
    #    altro mestiere. Vedi il docstring.
    #
    # 武器: si concatena con p(1), quindi a schermo esce «Arma1», «Arma2».
    #    text.hsp:59 ha «armi» perche' li' e' la CATEGORIA d'inventario; qui
    #    etichetta una singola arma, e il plurale sarebbe sbagliato.
    (12402, 'Melee'): 'Arma',
    # 格闘: skill.hsp:161 ha «Arti marziali» perche' li' e' il NOME
    #    dell'abilita'; tredici caratteri in una colonna da sei.
    (12408, 'Unarmed'): 'Lotta',
    # ⭐ 射撃 e 命中 insieme: la coppia l'ha gia' decisa buff.hsp:679
    #    (「射撃力上昇/命中率上昇」 -> «Tiro e mira»), e skill.hsp:1277 conferma
    #    「命中率上昇」 -> «+mira».
    (12414, 'Dist'): 'Tiro',
    (12428, 'Hit'): 'Mira',

    # ================================================================
    # *show_weaponStat — i cinque avvisi sul peso dell'arma
    # ================================================================
    # ⚠️ Tutte e cinque al VERBO, non all'aggettivo: itemname(cw) puo' essere
    #    maschile o femminile e a scrittura non si sa. Vedi il docstring.
    (12478, ' fits well for two-hand fighting style.'):
        'itemname(cw) + " si impugna bene a due mani."',
    (12481, ' is too light for two-hand fighting style.'):
        'itemname(cw) + " pesa un po\' troppo poco per l\'uso a due mani."',
    # ⭐⭐ :12488 e :12495 hanno lo STESSO inglese e due giapponesi diversi.
    #    :12485 e' `if ( attacknum == 1 )`, cioe' l'arma della mano principale
    #    sopra i 4000; 「利手で扱うにも重すぎる」.
    (12488, ' is too heavy for two-wield fighting style.'):
        'itemname(cw) + " pesa troppo perfino per la mano dominante."',
    #    :12492 e' l'`else`, cioe' l'arma secondaria sopra i 1500;
    #    「片手で扱うには重すぎる」. La rete 11 autorizza: `itemname` di qua e di la'.
    (12495, ' is too heavy for two-wield fighting style.'):
        'itemname(cw) + " pesa troppo per una mano sola."',
    # ⚠️ «per usarla a cavallo» nasconderebbe un accordo dentro il pronome.
    (12505, ' is too heavy to use when riding.'):
        'itemname(cw) + " pesa troppo per l\'uso a cavallo."',

    # ================================================================
    # *com_wear — l'intestazione della finestra dell'equipaggiamento
    # ================================================================
    # ⚠️ text.hsp:59 ha 装備品 -> «equipaggiamento» minuscolo, perche' li' e'
    #    una voce di un elenco di categorie. Qui e' il TITOLO della finestra,
    #    e i titoli di questo file cominciano per maiuscola.
    (12618, 'Equipment'): 'Equipaggiamento',
    # 部位 e' la parte del corpo di bodyn (text.hsp:136), 名称 il nome
    #    dell'oggetto: la colonna li tiene tutt'e due.
    (12620, 'Category/Name'): 'Parte/Nome',
    (12622, 'Weight'): 'Peso',
    # ⚠️ La riga e' destra e il tetto e' 75 caratteri (module.hsp:4360, con
    #    ww = 690). L'inglese ci arriva; questa ne fa 62. Vedi il docstring.
    (12674, 'Equip weight: '): 'Peso equip.: ',
    (12674, ' Hit Bonus:'): ' Mira:',
    (12674, ' Damage Bonus:'): ' Danno:',
    # ⭐ Da bodyn (text.hsp:136, 手 -> «Mano»): 「利手」 prende il posto del nome
    #    della parte del corpo nella stessa colonna, larga 42 px.
    (12694, 'Hand*'): 'Mano*',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {(12636, 'Fi Co Li Da Mi Po Nt So Nr Ch Ma')}

USCITA = 'lavoro/fase4-command-032.jsonl'
DA, A = 12402, 12694
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
