# -*- coding: utf-8 -*-
"""Lotto fase4-db_card-001: i **1.141 nomi delle carte**, e apre `db_card.hsp`.

⭐⭐⭐ **`db_card.hsp` e' il NONO punto cieco** (vedi
`scratchpad/db_card_nomi.py`). Il nome che il giocatore legge sulla carta non
viene da `db_creature.hsp`: `tcg_custom.hsp:4537` legge `cardrefn` da
`dbs_card`, che `:4514` riempie chiamando `db_card` — un file di 15.075 righe,
**2.324 `lang()`**, senza nessun file di dizionario e mai nominato da
`verifica --dizionario`.

Il lotto prende **solo i nomi** (`cardrefn`). I 1.144 testi di ambientazione
(`cardrefskill`, 257.399 caratteri) restano fuori e risulteranno «non ancora
tradotte»: sono il lavoro di un'altra volta.

⭐⭐ **Le rese non si inventano: si prendono dal dizionario, e la chiave e'
`(jp, en)`.** Col solo inglese 29 nomi risultavano ambigui; col giapponese
accanto ne restano **tre**. Il giapponese e' quello che distingue «rabbit»
ウサギ («coniglio») da 野うさぎ («coniglio selvatico»), «salamander» 沙羅曼蛇
(«salamandra d'oriente») da メガサラマンダー («salamandra»), «staff»
カジノスタッフ («addetto del casinò») da 杖 («bastone»). Non e' una comodita':
scegliere col solo inglese avrebbe dato a due creature diverse lo stesso nome.

⭐⭐⭐ **L'articolo RESTA, e la decisione e' stata capovolta da una misura.**
Il primo disegno lo toglieva: sulla carta il nome e' un'etichetta in testa a una
riga di dati (`tcg.hsp:1492`-`:1509`), e «la zanzara gigante  No.1142
Rare:Common» ha un articolo che non regge niente. Poi il lotto e' stato
generato e `reimporta` l'ha **rifiutato**:

    52 voci — traduzione identica all'inglese

Togliendo l'articolo, «lo yeek» diventa «yeek», «il troll» «troll», «la medusa»
«medusa»: **52 rese perfettamente italiane diventano indistinguibili
dall'inglese**, e passare il lotto vorrebbe dire scrivere 52 righe motivate in
`invariati.md` per nomi che non sono affatto invariati. L'articolo non era
decorazione: era **quel che rende italiana la resa**, ed e' esattamente il
motivo per cui `contratto-nomi.md` §4 lo mette dentro il nome.

⚠️ E l'argomento che aveva convinto a toglierlo non regge al controllo: il
numerale del negozio («1 zanzara gigante») sta in `tcg_custom.hsp`, dentro un
elenco `[Contains]` che e' **prosa scritta a mano** e non interpola `cardrefn`.
L'unico sito che il nome lo interpola davvero e' la voce di menu di
`tcg_custom.hsp:1917` — «Card of » + `carddailyt@tcg` — e quella si riscrive
«Carta: » + nome, dove l'articolo sta **meglio**, non peggio.

✅ Misurato: 881 rese su 1.121 cominciano con un articolo, tutte minuscole, e
una sola e' plurale — «gli occhi di quadri», che e' giusta.

⭐ **La larghezza non e' un vincolo, ed e' stato misurato prima**
(`scratchpad/db_card_riga_aiuto.py`): la riga d'aiuto sta su 680 px a font 10,
cioe' 136 caratteri, e la piu' lunga di oggi ne fa **93**. Il nome italiano piu'
lungo supera il piu' lungo inglese di 12 caratteri: ci sta con 43 di margine.
⚠️ Il primo conto diceva il contrario — 137 caratteri, fuori misura — perche'
prendeva come `skillname()` il piu' lungo `it` di `dizionario/skill.hsp.jsonl`,
59 caratteri, che e' una **descrizione** e non un nome di mossa. Il tetto vero
sta nel `sdim` di `skill.hsp:3` (`sdim skillname, 16, MAX_SKILL`): **quindici**.
E' la stessa lezione del lotto `tcg_mod-001`.

⚠️ **Due nomi si risolvono solo col giapponese, perche' l'inglese di monte non
coincide**, e vanno detti a chiare lettere invece di lasciarli risolvere in
silenzio:

    db_card:257    "<Kamikakushi> the hiden ShikiOrigami"    (hiden: refuso)
    db_creature    "<Kamikakushi> the hidden ShikiOrigami"
    db_card:2714   "<Nagarew> the oblivion beast"
    db_creature    "<Nagarew> the oblivion rude beast"       (rude in meno)

Stessa creatura, stesso giapponese, due inglesi. La resa segue il giapponese.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata
from pathlib import Path

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\db_card.hsp'
ESTRAZIONE = 'lavoro/_db_card.jsonl'
USCITA = 'lavoro/fase4-db_card-001.jsonl'

# I file che tengono i NOMI delle creature. Una resa che viene da qui e' il nome
# della creatura; una che viene da altrove ha solo lo stesso (jp, en) per
# combinazione — e va guardata, non presa.
FILE_DEI_NOMI = ('db_creature', 'action', 'custom_enemyevolution')

ARTICOLI = ('il ', 'lo ', 'la ', 'i ', 'gli ', 'le ', "l'", "gl'")

# ---------------------------------------------------------------- rese a mano
#
# Quindici in tutto: tre che il giapponese non scioglie, e le dodici carte che
# nessun altro file nomina.
RESE_A_MANO = {
    # --- i tre che restano ambigui anche con (jp, en): lo stesso giapponese sta
    # in due file, e uno dei due non e' un nome di creatura.
    # 先生: db_creature «l'insegnante» contro text.hsp «Insegnamento», che e' la
    # SKILL «Teaching». La carta e' una persona.
    (6744, 'teacher'): "l'insegnante",
    # バグ: db_creature «il bug» contro item_data «baco», che e' un modificatore
    # di qualita' degli oggetti. La carta e' la creatura di prova.
    (10202, 'bug'): 'il bug',
    # 観光客: db_creature «il turista» contro init.hsp «Turista», che e' una voce
    # di menu con la maiuscola: la' e' un'etichetta, qui una persona.
    (13883, 'tourist'): 'il turista',

    # --- lo spazio in coda, che l'ha trovato `reimporta`.
    # ⚠️ `db_card.hsp:10085` scrive `lang("『犬のおまわりさん』", "<Dog cop> ")` — con
    # **uno spazio in coda** che la resa di `db_creature` non ha. `verifica`
    # pretende che uno spazio finale si conservi, perche' di norma e' la giuntura
    # col pezzo che segue; qui e' solo una sbavatura di monte, ma conservarlo
    # costa un carattere e togliere la rete costerebbe una garanzia. Lo spazio
    # resta.
    (10085, '<Dog cop> '): '<Cane poliziotto> ',

    # --- le OTTO TERRE, `cardreftype = 30`: `tcg.hsp:1499` gli attacca in coda
    # « <Land>». Sono la famiglia delle terre base, come in Magic, e vanno
    # scritte insieme o non si riconoscono come famiglia — tutte minuscole e di
    # una parola dove si puo'.
    # ⚠️ **E sono la sola deroga dichiarata all'articolo**, insieme alle due
    # magie: l'articolo lo porta il nome perche' un nome di **creatura** entra
    # nelle frasi del gioco («hai ucciso lo yeek»), mentre una terra e' un tipo
    # di terreno che non entra in nessuna frase — compare solo qui, con « <Land>»
    # appiccicato dietro. «la montagna <Land>» direbbe una cosa che «montagna
    # <Land>» dice meglio.
    # ⚠️ **Quattro su otto le avrebbe risolte il dizionario, e tutte e quattro
    # MALE**: «Mare» da `text.hsp`, «Pianura», «Foresta» e «Distesa innevata» da
    # `map.hsp`, cioe' i nomi delle **regioni** della mappa del mondo, scritti
    # con la maiuscola perche' la' sono toponimi. Le ha trovate il referto delle
    # rese prese da un file che non tiene nomi di creatura: senza quello, quattro
    # carte su otto sarebbero uscite con la maiuscola in mezzo a una famiglia
    # minuscola.
    (14882, 'forest'): 'foresta',
    (14893, 'mountain'): 'montagna',
    (14904, 'sea'): 'mare',
    (14915, 'island'): 'isola',
    (14926, 'swamp'): 'palude',
    # 枯地 e' «terra secca»; l'inglese ha scelto «dead land» e il dominio e' nero.
    (14937, 'dead land'): 'terra morta',
    (14948, 'plain'): 'pianura',
    # 💡 «distesa innevata» e' due parole dove le altre sette ne hanno una, ma e'
    # la stessa che il giocatore legge sulla mappa del mondo (`map.hsp`): meglio
    # ripetere quella che inventare «nevi» per far quadrare la famiglia.
    (14959, 'snow field'): 'distesa innevata',

    # --- le due carte MAGIA, `cardreftype = 20` (« <Spell>» in coda).
    (15058, 'homing pigeon'): 'piccione viaggiatore',
    # 帰還 e' il ritorno di Elona, e `skill.hsp:564` lo rende gia' «Ritorno».
    (15069, 'return'): 'Ritorno',
}
RESE_A_MANO = {k: unicodedata.normalize('NFC', v) for k, v in RESE_A_MANO.items()}

RINVIATE = set()

# ------------------------------------------------------------------ il lotto
sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')
RIGA_NOME = re.compile(r'^\s*cardrefn\s*=\s*lang\(')
righe_di_nome = {n for n, r in enumerate(sorgente, 1) if RIGA_NOME.match(r)}

tutte = [json.loads(l) for l in io.open(ESTRAZIONE, encoding='utf-8') if l.strip()]
zona = [v for v in tutte if v['riga'] in righe_di_nome]

AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

# ------------------------------------------------- le rese, dal dizionario
per_coppia = collections.defaultdict(list)
per_jp = collections.defaultdict(list)
tutto_il_dizionario = collections.defaultdict(set)
for p in sorted(glob.glob('dizionario/*.jsonl')):
    nomefile = Path(p).name.replace('.hsp.jsonl', '')
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if not d.get('it'):
            continue
        per_coppia[(d['jp'], d['en'].strip().lower())].append((nomefile, d['riga'], d['it']))
        per_jp[d['jp']].append((nomefile, d['riga'], d['en'], d['it']))
        tutto_il_dizionario[d['jp']].add((nomefile, d['riga'], d['it']))


def senza_articolo(resa: str) -> str:
    for a in ARTICOLI:
        if resa.lower().startswith(a):
            return resa[len(a):]
    return resa


def preferisci(rese: list) -> list:
    """Le rese che vengono da un file di NOMI, se ce ne sono."""
    dai_nomi = [r for r in rese if r[0] in FILE_DEI_NOMI]
    return dai_nomi or rese


RESE = {}
da_fuori, per_solo_jp, senza_resa = [], [], []
for v in voci:
    k = chiave(v)
    corta = (v['riga'], v['en'])
    if corta in RESE_A_MANO:
        RESE[k] = RESE_A_MANO[corta]
        continue
    rese = preferisci(per_coppia.get((v['jp'], v['en'].strip().lower()), []))
    if rese:
        distinte = {r[2] for r in rese}
        if len(distinte) > 1:
            senza_resa.append((v['riga'], v['en'], f'ambigua: {sorted(distinte)}'))
            continue
        RESE[k] = distinte.pop()
        if rese[0][0] not in FILE_DEI_NOMI:
            da_fuori.append((v['riga'], v['en'], rese[0][0], RESE[k]))
        continue
    # ripiego: lo stesso giapponese con un inglese diverso di monte
    rese = preferisci([(f, r, it) for f, r, en, it in per_jp.get(v['jp'], [])])
    if rese:
        distinte = {r[2] for r in rese}
        if len(distinte) > 1:
            senza_resa.append((v['riga'], v['en'], f'ambigua per solo jp: {sorted(distinte)}'))
            continue
        RESE[k] = distinte.pop()
        inglesi = {en for f, r, en, it in per_jp[v['jp']] if f in FILE_DEI_NOMI} or \
                  {en for f, r, en, it in per_jp[v['jp']]}
        per_solo_jp.append((v['riga'], v['en'], sorted(inglesi), RESE[k]))
        continue
    senza_resa.append((v['riga'], v['en'], 'nessuna resa nel dizionario'))

RESE = {k: unicodedata.normalize('NFC', r) for k, r in RESE.items()}

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'va data con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE_A_MANO:
    if k not in {(v['riga'], v['en']) for v in zona}:
        errori.append(f'rete 2: resa a mano che non aggancia nessuna voce -> {k}')
for riga, en, perche in senza_resa:
    errori.append(f'rete 1-bis: :{riga} {en!r} — {perche}')

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# rete 6: righe spente, col `;` o dentro un blocco di commento.
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)

from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    return sorgente[riga - 1].lstrip().startswith(';') or riga in SPENTE


for v in voci:
    _righe = [r for r in _righe_per_firma.get(v['firma'], [v['riga']]) if r in righe_di_nome]
    _righe = _righe or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        errori.append(f"rete 6: riga {v['riga']} e' spenta in tutte le sue occorrenze, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"💡 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

# rete 7: una voce dentro un CONFRONTO non e' testo.
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome.
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
for v in voci:
    for _, nome in FONDONO.findall(RESE[chiave(v)]):
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde davanti a {nome}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») chiude col connettivo.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        if not TESTA.search(RESE[chiave(v)].rstrip()):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non finisce con ' e'")

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo.
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo nudo")

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
            errori.append(f"rete 11: riga {v['riga']} — attese {attese}, trovate {trovate}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


# rete 3: lo stesso giapponese reso in modo diverso altrove nel dizionario.
#
# 💡 Adesso che l'articolo resta, le rese di questo lotto sono **le stesse
# stringhe** del dizionario e la rete 3 tace su tutte le automatiche: quel che
# stampa riguarda solo le tredici scritte a mano e i pochi giapponesi che
# portano piu' di un significato. Il conto `solo_articolo` resta per le tredici.
solo_articolo = 0
for v in voci:
    resa = RESE[chiave(v)]
    for nomefile, riga, it in tutto_il_dizionario.get(v['jp'], ()):
        if it == resa:
            continue
        if senza_articolo(it) == resa:
            solo_articolo += 1
            continue
        if parole(it) == parole(resa):
            continue
        print(f"⚠️ rete 3: :{v['riga']} jp={v['jp']!r}\n"
              f"      qui                 {resa!r}\n"
              f"      {nomefile}:{riga}  {it!r}")
print(f'💡 rete 3: {solo_articolo} rese differiscono dal dizionario **solo per '
      f'l\'articolo** in testa, che e\' la scelta di questo lotto')

# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
per_jp_lotto = collections.defaultdict(set)
inglesi_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp_lotto[(v['jp'], v['en'], ())].add(parole(RESE[chiave(v)]))
    inglesi_per_jp[v['jp']].add(v['en'])
for (jp, en, firma), rese in per_jp_lotto.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} / {en!r} reso in {len(rese)} modi: {rese}')
for jp, inglesi in sorted(inglesi_per_jp.items()):
    if len(inglesi) > 1:
        print(f'💡 rete 4: il giapponese {jp!r} sta per {len(inglesi)} inglesi diversi '
              f'{sorted(inglesi)}: la resa segue l\'inglese, ma guarda che sia voluto')

# rete 13: stesso inglese, giapponese diverso.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

# ------------------------------------------------------------------- referti
if per_solo_jp:
    print(f'\n⚠️ {len(per_solo_jp)} nomi risolti col SOLO giapponese: '
          f'l\'inglese di monte non coincide, e va letto')
    for riga, en, inglesi, resa in per_solo_jp:
        print(f'    :{riga:6d}  db_card {en!r}\n'
              f'              altrove {inglesi}  → {resa!r}')
if da_fuori:
    print(f'\n⚠️ {len(da_fuori)} rese prese da un file che NON tiene nomi di creatura: '
          f'la coincidenza di (jp, en) va guardata')
    for riga, en, nomefile, resa in da_fuori:
        print(f'    :{riga:6d}  {en:40s} [{nomefile}] → {resa!r}')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'\n{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate); '
      f'{len(RESE_A_MANO)} rese scritte a mano')
