# -*- coding: utf-8 -*-
"""Lotto `command-033`: **togliere l'equipaggiamento e i gesti sulla mappa** —
i tre messaggi di `*com_wear`, la raccolta delle piante e della neve, la
demolizione di un edificio del mondo. Dodici rese, e con queste **la zona
12000-12999 è chiusa**.

⭐⭐⭐ **L'inglese butta via un avviso che protegge il salvataggio, e la resa se
lo riprende.** `:12955` in giapponese è
「本当にこの建物を撤去する？（注意！建物と中の物は完全に失われます）」 — «Demolire davvero
questo edificio? (Attenzione! L'edificio e quello che c'è dentro andranno persi
del tutto)» — e in inglese diventa **«Really remove this building?»**, cioè la
domanda senza la parte che conta. E quel che segue non è reversibile: `:12963`
fa `adata(ADATA_ID, area) = AREA_NONE`, `:12964` `removeworker area`, `:12967`
**salva** (`fmode = 13`, `*game_ctrlFile`). Chi risponde di sì al prompt inglese
non sa che sta perdendo il contenuto, e non può tornare indietro.
✅ È una **statica**: nessun contratto di funzioni, quindi la resa può seguire il
giapponese, come `:4764` nel lotto 030.
⭐ **E il registro non l'ho inventato: c'era già.** `map.hsp:1297` è la stessa
specie — una conferma distruttiva con l'avviso fra parentesi — ed è resa «Vuoi
reinizializzare questa mappa? (Attenzione: può avere conseguenze sulla partita.
…)». Duecentoventidue caratteri, già spediti: la forma «Vuoi …? (Attenzione: …)»
è quella di casa, e il registro del log regge frasi di questa lunghezza.

⭐⭐ **E `init.hsp:1704` decide la persona di tutto il lotto.** `name()` per il
giocatore non è «tu»: è **«il viandante»**, un sintagma di terza persona
maschile. Quindi una frase che interpola `name(cc)` va scritta in **terza**
(`:12795`, «il viandante ha la mente annebbiata…»), e regge identica sul
compagno; una frase che dice «You …» **senza** funzioni va in **seconda**, che è
quel che il progetto fa già da sempre — `action.hsp:3255`, «Usi anche il
passe-partout». Le due persone convivono nello stesso lotto perché a decidere
non è il gusto ma se c'è o no una funzione.

⚠️ **E a `:12795` gli helper da togliere sono due, non uno.** L'inglese è
`name(cc) + " " + is(cc) + " confused and can't change " + his(cc) + "
equipment."`: `is` e `his` a **un** argomento stanno tutt'e due in
`MORFOLOGIA_INGLESE` e se ne vanno. Resta `name`, e `name` soltanto, che è quel
che la rete 11 pretende.

⚠️ **`:12804` è il caso in cui l'inglese sbaglia e la resa non lo può
correggere.** «You unequip …» è in seconda persona, ma `*com_wear` si apre
**anche su un alleato** — lo dimostra `:12795`, che di `cc` fa il soggetto — e
allora non sei tu a toglierti niente. ⚠️ La correzione vorrebbe `name(cc)`, cioè
una funzione che l'inglese non ha: **è la rete 11, e non lascia scampo**. La resa
resta in seconda persona come l'inglese. È un difetto di monte che si eredita, e
va scritto qui perché al collaudo sembrerà un errore di traduzione.

⚠️ **Tre rese su dodici sono accordi evitati**, ed è sempre `itemname()` a
imporlo: «non si può togliere» invece di «non è togliibile», l'impersonale
invece del participio. `itemname(ci)` può essere «la spada» o «il martello».

⭐ Riscosso senza decidere: «Il tuo zaino è pieno.» (`text.hsp:14`, e il gemello
`command.hsp:15708`) e «Troppa stanchezza: il tentativo fallisce!»
(`proc.hsp:3467`). Due su dodici che la rete 3 ha nominato da sola.
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
    # *com_wear — togliere un pezzo di equipaggiamento (:12791-:12804)
    # ================================================================
    # ⚠️ Impersonale, non participio: itemname(ci) puo' essere «la spada» o
    #    «il martello», e «non e' togliibile» dovrebbe accordarsi.
    (12791, " can't be taken off."):
        'itemname(ci) + " non si può togliere."',
    # ⚠️ Gli helper da togliere sono DUE: `is(cc)` e `his(cc)` a un argomento,
    #    tutt'e due in MORFOLOGIA_INGLESE. Resta `name`, e la rete 11 pretende
    #    esattamente quello.
    # ⭐ Terza persona perche' c'e' `name()`: init.hsp:1704 rende
    #    name(CHARA_PLAYER) come «il viandante», non come «tu».
    (12795, "  confused and can't change  equipment."):
        'name(cc) + " ha la mente annebbiata e non riesce a cambiare '
        'equipaggiamento."',
    # ⚠️ Seconda persona come l'inglese, e l'inglese qui sbaglia: *com_wear si
    #    apre anche su un alleato. Correggerlo vorrebbe `name(cc)`, cioe' una
    #    funzione che l'inglese non ha: e' la rete 11. Vedi il docstring.
    (12804, 'You unequip .'):
        '"Ti togli " + itemname(ci) + "."',

    # ================================================================
    # I gesti sulla mappa (:12890-:12999)
    # ================================================================
    # 芽 e' il germoglio, 枯れた草 l'erba secca: il giapponese distingue le due
    #    piante, e l'inglese pure («young» / «dead»).
    (12890, 'You nip a young plant.'): 'Cogli il germoglio.',
    (12895, 'You nip a dead plant.'): "Cogli l'erba secca.",
    # ⭐ Gia' deciso: text.hsp:14 e command.hsp:15708.
    (12929, 'Your inventory is full.'): 'Il tuo zaino è pieno.',

    # ================================================================
    # La demolizione di un edificio del mondo (:12952-:12969)
    # ================================================================
    (12952, 'You can not remove the building until relocation.'):
        'Questo edificio non si può demolire finché non viene trasferito.',
    # ⭐⭐ L'inglese butta via l'avviso, e quel che segue non e' reversibile
    #    (:12963 azzera l'area, :12964 licenzia i lavoranti, :12967 SALVA).
    #    E' una statica: nessun contratto, la resa segue il giapponese.
    #    Il registro viene da map.hsp:1297. Vedi il docstring.
    (12955, 'Really remove this building?'):
        'Vuoi davvero demolire questo edificio? (Attenzione: l\'edificio e '
        'tutto quello che contiene andranno perduti per sempre.)',
    (12969, 'You remove the building.'): "Demolisci l'edificio.",

    # ================================================================
    # La neve e il gesto a vuoto (:12982-:12999)
    # ================================================================
    (12982, 'You rake up a handful of snow.'):
        'Raccogli una manciata di neve.',
    # ⭐ Gia' deciso: proc.hsp:3467.
    (12985, 'You are too exhausted!'):
        'Troppa stanchezza: il tentativo fallisce!',
    # 「あなたは空気をつかんだ。」 — la mano si chiude sul niente.
    (12999, 'You grasp at the air.'): 'Stringi solo aria.',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-033.jsonl'
DA, A = 12791, 12999
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
