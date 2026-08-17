# -*- coding: utf-8 -*-
"""Lotto fase4-main-004: il turno del giocatore — carico, opzioni, uscita, e la
fine di Lesimas (main.hsp, righe 2625-3999).

Quindici rese sparse, tenute insieme dal fatto che escono tutte dal **giro del
turno**: il carico che schiaccia, la raccolta automatica che si accende e si
spegne, l'ora di gioco che passa, la domanda dell'arena, il tasto della guida,
e in fondo le due righe della vittoria finale.

⚠️⚠️ **`:3130` e' il caso in cui l'italiano non ha il trucco dell'inglese, e la
frase si riscrive invece di storpiarla.** L'inglese fa
`" hour" + _s3(hour_played)`, cioe' aggiunge la `s` **solo se le ore sono piu'
di una**: `_s3` sta in `MORFOLOGIA_INGLESE` e `verifica` pretende che sparisca.
Tolta, «da " + hour_played + " ore» direbbe «da 1 ore» alla prima ora, e non c'e'
nessuna funzione italiana da mettere al suo posto — aggiungerne una e' proprio
quel che la rete 11 vieta.
✅ La via d'uscita e' la stessa che il progetto usa gia' per i materiali
(`command.hsp:6357`, «Materiale ricevuto: neve (3)»): si mette il numero
**dietro i due punti**, dove singolare e plurale non si pongono. «Ore di gioco
su ElonaPlus: 1.» e «...: 12.» sono tutt'e due giuste.
💡 E' la stessa famiglia dell'accordo evitato invece che scelto, come le battute
dei figli della 52ª e i cuccioli del lotto 003: **quando la morfologia non c'e',
si cambia la forma della frase, non si accetta la forma sbagliata.**

⭐ **Due etichette dell'interfaccia decidono le due righe della raccolta
automatica.** `action.hsp:1067` la chiama «[Raccolta automatica]» nel menu che la
accende, `screen.hsp:1004` «Raccolta» nell'HUD dove non c'e' spazio: `:3343` e
`:3347` sono i due messaggi che annunciano il passaggio, e usano il nome per
esteso perche' li' lo spazio c'e'.

⭐ **`:3024` tiene gli asterischi**, come le altre 137 rese `*...*` del progetto:
`*ぷちゅ*` -> `*sciac*`, `*必殺セミファイナル！*` -> `*COLPO SEMI-FINALE!*`. Non
sono decorazione tipografica, sono il modo in cui Elona scrive un cartello. ⚠️ Il
gemello `*Win*` (`main.hsp:4050`) non e' in questo lotto e restera' in tinta.

💡 **`:3937`-`:3964` sono lo scherzo dell'uscita**, e vanno lette in fila: il
gioco reagisce riga per riga mentre si scrive la parola per uscire (`key == "Q"`,
poi `"y"`, poi `"sc"`), e alla fine evoca dieci `CREATURE_ID_AT_SIGN` — le
chiocciole che sono il giocatore nei roguelike di una volta. Le tre rese salgono
di tono come l'inglese: «Come...», «Non dirai sul serio...», «Aaaaahh!!».

💡 **`:3999` non traduce il giapponese, e va bene cosi'.** 「お前がここに辿り着く
ことは」台座から、何かの声が聞こえる。 comincia a meta' frase, con la parentesi di
chiusura di una battuta che il testo non ha mai aperto — e' un residuo di
upstream. L'inglese ha tenuto solo la seconda meta', che e' quella che ha senso,
e la resa segue l'inglese.

⭐ **«Lesimas» resta «Lesimas»**, come nelle undici rese che gia' lo nominano
(`text.hsp:2770`, `map.hsp:4112` «Fondo di Lesimas», `db_item.hsp:135481`).
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :2625 il carico. «zaino» e' la parola gia' fissata (ai.hsp:1100,
    # command.hsp:12929, item_func.hsp:587).
    (2625, 'Your backpack is squashing you!'):
        'Lo zaino ti sta schiacciando!',
    # Stesso giapponese e stesso inglese di chara_func.hsp:1380: si ricopia.
    (2641, 'Time starts to run again.'):
        'Il tempo riprende a scorrere.',

    # --- :3024-:3031 l'arena degli alleati. Gli asterischi sono il cartello,
    # e restano: sono la forma di altre 137 rese del progetto.
    (3024, '*Loss on points*'):
        '*Sconfitta ai punti*',
    (3031, 'Do you want to give up the game?'):
        "Vuoi abbandonare l'incontro?",

    (3089, 'You change your equipment.'):
        'Hai cambiato equipaggiamento.',

    # --- :3130 ⚠️ `_s3` e' morfologia inglese e va tolta; senza, «da 1 ore»
    # sarebbe sbagliato e aggiungere una funzione italiana e' vietato dalla
    # rete 11. Il numero va dietro i due punti, dove il plurale non si pone.
    # ⚠️ Lo spazio finale c'e' anche nell'inglese e serve a chi concatena.
    (3130, 'You have been playing ElonaPlus for  hour. '):
        '"Ore di gioco su ElonaPlus: " + hour_played + ". "',
    # Stesso giapponese di otto rese in cinque file: si ricopia la formula.
    (3147, 'You have learned new ability, .'):
        '"Hai imparato una nuova capacità: " '
        '+ skillname(SKILL_SPACT_CLEMENTIA) + "."',

    # --- :3343-:3347 la raccolta automatica. Il nome per esteso e' quello del
    # menu che la accende (action.hsp:1067).
    (3343, 'Autopickup is now disabled.'):
        'La raccolta automatica è disattivata.',
    (3347, 'Autopickup is now enabled.'):
        'La raccolta automatica è attivata.',

    (3924, 'Hit ? key to display help.'):
        "Premi ? per vedere l'elenco dei comandi.",

    # --- :3937-:3964 lo scherzo dell'uscita, da leggere in fila: il gioco
    # reagisce mentre si digita, e alla fine evoca dieci chiocciole.
    (3937, 'What...'):
        'Come...',
    (3946, 'No... no...'):
        'Non dirai sul serio...',
    (3964, 'Ahhhhh!!'):
        'Aaaaahh!!',

    # --- :3986-:3999 la fine di Lesimas.
    (3986, 'Unbelievable! You conquered Lesimas!'):
        'Incredibile! Hai conquistato Lesimas!',
    (3999, 'From the pedestal, you can hear a voice.'):
        'Dal piedistallo si sente una voce.',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-main-004.jsonl'
DA, A = 2401, 3999
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
