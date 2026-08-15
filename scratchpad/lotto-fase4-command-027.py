# -*- coding: utf-8 -*-
"""Lotto `command-027`: **la bacheca degli avventurieri e la scelta del nome**.
Quindici rese e una rinviata, apre la zona 4000-4999 (76 firme, la più densa).

⚠️⚠️ **Tre voci di questo lotto non sono testo che si legge: sono parole che il
giocatore DIGITA.** `*wish_fix` (`:4325`-`:4337`) ripulisce quel che è stato
scritto nella finestra del desiderio, e `:4334`-`:4336` tolgono dalla stringa il
prefisso «item»/«skill» perché chi scrive «skill fishing» ottenga l'abilità.
✅ Vanno tradotte, perché il desiderio **si risolve in italiano**: `:4883` fa
`s = cnvitemname(cnt2)`, cioè confronta con il nome **tradotto** dell'oggetto, e
`:4332` mette tutto in minuscolo da tutt'e due le parti. Chi scrive «oggetto
spada» deve ritrovarsi con «spada».

⚠️⚠️ **E qui l'accento non si può scrivere, per una ragione che non è quella di
sempre.** Di solito l'accento si scrive vero nel dizionario e `accenti.py` lo
degrada in build: «abilità» diventerebbe «abilita'». Ma questa stringa non deve
**apparire**, deve **coincidere con quello che il giocatore batte sulla
tastiera** — e in CP932 la `à` non esiste, quindi nessuno può digitarla. Un
`del_str(inputlog, "abilita'")` non aggancerebbe mai niente.
✅ La resa è «abilita» **senza accento**, e non è un refuso: è l'unica forma che
il campo di input può contenere. 💡 È il rovescio esatto della regola degli
accenti: là l'apostrofo è come si scrive un accento che il carattere non ha, qui
l'accento non va scritto affatto perché la stringa non è testo da leggere.

⚠️⚠️ **Una rinviata, e la rete che la impone ha ragione in generale e torto qui.**
`:4335` e `:4336` sono la **stessa** `lang("スキル", …)` con due inglesi diversi —
«skill » con lo spazio e «skill» senza — e servono in quest'ordine: il primo
`del_str` porta via anche lo spazio, il secondo prende il caso senza. La rete 4
raggruppa per giapponese e pretende **una resa sola**, e in generale è quel che
deve fare (nel lotto 024 ha giustamente legato le due 「いらん」). Qui no: a
distinguerle non è il senso, è uno **spazio**, e il giapponese non ne ha bisogno
perché il ramo giapponese gli spazi li ha già tolti a `:4328`.
✅ Rinvio + toppa, la forma della 46ª: `:4336` prende la resa «abilita», `:4335`
esce dal dizionario e la toppa ci scrive «abilita ». ⚠️ **Senza, il taglio
lascerebbe uno spazio in testa**, e `:4887` fa il punteggio sui **prefissi** di
`inputlog`: con uno spazio davanti i prefissi diventano « », « s», « sp», e la
ricerca dell'oggetto si sfalda.

⚠️⚠️ **E la scoperta grossa di questo lotto è quello che NON si può tradurre.**
Da `:4481` a `:4780` il desiderio si risolve con una cinquantina di
`if ( inputlog == "lulwy" | inputlog == "ルルウィ" )`: gli dèi, le classi, le
razze, «money», «youth», «alias», «merry christmas». **Sono letterali nudi fuori
da `lang()`**, quindi il dizionario non li tocca — e la rete 7 ha ragione a
chiamarli operandi di confronto e non testo. La conseguenza però è che
**l'italiano può desiderare un oggetto o un'abilità in italiano, ma un dio, una
classe o una razza solo in inglese**. Non è un difetto della traduzione: è come
è fatto il gioco, e va scritto perché al collaudo non sembri un guasto.

⭐ Riscosso senza decidere: «Ignoto» per 不明 (`chara_func.hsp:172`,
`text.hsp:2969`). ⚠️ La rete 3 segnalerà anche `action.hsp:2608`, «classe
ignota»: lì il giapponese identico sta dentro una frase più lunga sulla classe,
qui è il nome di un luogo che la mappa non conosce. Restano due cose diverse.

💡 **Le larghezze di questa schermata non le misura nessuno strumento.**
`display_topic` (`module.hsp:4364`) scrive a `x + 26` con carattere in grassetto
da 10, e le tre colonne partono da `wx + 28`, `wx + 290` e `wx + 420` in una
finestra da 640. La colonna di mezzo ha quindi **104 pixel** e l'inglese
«Message(Impress)» ne prende già più di così — la sottolineatura di `:4372` è
lunga `strlen * 7 + 36` e sconfina nella colonna dopo. La regola qui è quella dei
siti non misurati: **mai più lunghi dell'inglese**. «Fama(amicizia)» sta in
quattordici, «Messaggio(amic.)» in sedici come l'inglese.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :4192-:4201 la bacheca degli avventurieri.
    #     ⚠️ display_topic non lo misura nessuno strumento: la colonna di mezzo
    #        ha 104 px e l'inglese ne prende già di più. Regola dei siti non
    #        misurati: mai più lunghi dell'inglese. Vedi il docstring.
    (4192, 'Adventurer Rank'): 'Rango degli avventurieri',
    (4194, 'Name and Rank'): 'Nome e rango',
    # 「名声(友好)」: 14 caratteri contro i 13 dell'inglese
    (4196, 'Fame(Impress)'): 'Fama(amicizia)',
    # 「伝言種類(友好)」: 16 caratteri esatti come l'inglese
    (4199, 'Message(Impress)'): 'Messaggio(amic.)',
    (4201, 'Location'): 'Luogo',

    # --- :4253-:4256 la colonna del luogo.
    # ⭐ rete 3: chara_func.hsp:172 e text.hsp:2969 dicono già «Ignoto».
    (4253, 'Unknown'): 'Ignoto',
    (4256, 'Hospital'): 'Ospedale',

    # --- :4294-:4312 l'avventuriero a cui si affida un messaggio.
    # 「冷やかしか」: l'inglese dice «You kidding?», il giapponese «vieni solo a
    # curiosare?». Restano tutt'e due un rifiuto seccato.
    (4294, ' You kidding?'): '" " + cnvtalk("Mi stai prendendo in giro?")',
    (4309, ' Well noted!'): '" " + cnvtalk("Ricevuto!")',
    (4312, " I'll make sure that your message is delivered!"):
        '" " + cnvtalk("Uso la mia rete di contatti: il messaggio arriverà di sicuro!")',

    # --- :4334-:4336 *wish_fix, che NON è testo da leggere: sono le parole che
    #     il giocatore digita nella finestra del desiderio.
    #     ⚠️⚠️ «abilita» è senza accento di proposito: in CP932 la à non esiste,
    #        quindi nessuno può batterla, e un del_str su «abilita'» non
    #        aggancerebbe mai niente. Vedi il docstring.
    #     ⚠️ :4335, la variante con lo spazio, è RINVIATA: la rete 4 pretende una
    #        resa sola per lo stesso giapponese. La scrive la toppa.
    (4334, 'item'): 'oggetto',
    (4336, 'skill'): 'abilita',

    # --- :4350-:4374 la scelta del nome d'arte.
    (4350, 'Alias Selection'): 'Scelta del nome',
    (4356, 'Alias List'): 'Nomi possibili',
    (4374, 'Reroll'): 'Pensane un altro',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {(4335, 'skill ')}

USCITA = 'lavoro/fase4-command-027.jsonl'
DA, A = 4000, 4400
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
