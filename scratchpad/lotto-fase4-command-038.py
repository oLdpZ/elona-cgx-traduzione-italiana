# -*- coding: utf-8 -*-
"""Lotto `command-038`: **mangiare, bere, equipaggiare**. Tredici rese, da
`:14741` a `:14828`, ancora dentro `*com_inventory_loop`.

⭐⭐ **Il quartetto della sete era già scritto, e quello della fame no — e la
scoperta è che sono la stessa scena due volte.** `:14799` e `:14741` hanno la
stessa identica struttura: una `txt` con **tre** `lang()` di fila, che il gioco
sceglie a caso, per dire che non ci sta più niente nello stomaco. Le tre della
sete hanno lo **stesso giapponese** di `action.hsp:8274` — 「これ以上飲めない…。」,
「膀胱がやぶける…」, 「まだ喉は渇いていない。」 — quindi non si riscrivono: si
**ricopiano**, e la rete 3 deve tacere. Le tre della fame non hanno precedente, e
sono state scritte **sulla forma delle tre della sete**, una per una:

    Non riesci a mangiare altro.      Non riesci a bere altro.
    La pancia sta per scoppiarti...   La vescica sta per scoppiarti...
    Non hai ancora fame.              Non hai ancora sete.

💡 È il caso in cui «cercare prima di scrivere» non serve a riusare una resa, ma
a **riusare un registro**: tre frasi nuove che suonano come tre già spedite.

⚠️ **E la terza coppia è un inglese solo su due giapponesi diversi**, che la
rete 13 segnalerà: `:14741` e `:14799` dicono tutt'e due «Your stomach can't
digest any more.», ma il giapponese di `:14741` è 「まだ腹は減っていない。」 (non hai
fame) e quello di `:14799` è 「まだ喉は渇いていない。」 (non hai sete). Upstream ha
copiaincollato la riga della fame dentro il ramo della sete; l'italiano no.

⭐ **Tre rese riscosse senza decidere.** `:14758` ha lo stesso giapponese di
`:12795` ed è ricopiata parola per parola; «equipaggiare» è già il verbo di
questo stesso schermo (`:13924`, «Che cosa vuoi equipaggiare?», e `:17020`);
l'icona di `:14828` è la stessa di `:6068`-`:6076` e la resa è il **gemello
speculare** di `:6825`, che dice «name(tc) + " ha perso l'icona."».

⚠️⚠️ **Quattro rese su tredici hanno dovuto schivare un accordo di genere**, e
tutte per lo stesso motivo: il soggetto è chi gioca, di cui non si sa il sesso,
oppure è l'oggetto, di cui non si sa il genere.
- `:14752` «È troppo pesante da equipaggiare» e non «troppo pesante per essere
  equipaggiato»: `pesante` è invariabile, il participio no.
- `:14778` «qualcosa veglia su di te» e non «ti senti protetto».
- `:14772` «ti prende un brivido» e non «resti raggelato».
- `:14775` «hai mosso un passo» e non «sei più vicino».
💡 Non è prudenza: sono le tre righe che il gioco stampa quando equipaggi un
oggetto **maledetto, votato alla rovina o benedetto**, e le vede chiunque.

💡 **`:14775` è l'unica resa che tiene tutt'e due gli originali.** Il giapponese
è 「破滅への道を歩み始めた。」, «ha cominciato a percorrere la via della rovina»;
l'inglese è «You are now one step closer to doom.», che conta i passi. «Hai mosso
un passo sulla via della rovina» dice le due cose insieme, e «rovina» è la parola
che `skill.hsp:1576` usa già per 「破滅の歌」, il «Canto di rovina».
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
    # Le tre della fame (:14741) — scritte sulla forma delle tre della sete
    # ================================================================
    (14741, 'You are too full to eat.'):
        'Non riesci a mangiare altro.',
    # ⚠️ 「腹がさける」 e' la pancia che si spacca, come 「膀胱がやぶける」 e' la vescica.
    (14741, 'You are too bloated to eat any more.'):
        'La pancia sta per scoppiarti...',
    # 💡 Stesso inglese di :14799 su un giapponese diverso (腹 contro 喉): upstream
    #    ha copiato la riga della fame dentro il ramo della sete. La rete 13 lo
    #    dira'.
    (14741, "Your stomach can't digest any more."):
        'Non hai ancora fame.',

    # ================================================================
    # Equipaggiare (:14752-:14778)
    # ================================================================
    # ⚠️ «pesante» e' invariabile, «equipaggiato» no: il genere dell'oggetto non
    #    si conosce a scrittura. Stessa forma di action.hsp:63.
    (14752, "It's too heavy to equip."):
        'È troppo pesante da equipaggiare.',
    # ⭐ Stesso giapponese di :12795, ricopiata parola per parola.
    # ⚠️ `is(cc)` e' morfologia e sparisce: resta il solo `name`.
    (14758, "  confused and can't change their equipment."):
        'name(cc) + " ha la mente annebbiata e non riesce a cambiare equipaggiamento."',
    # ⭐ «equipaggiare» e' il verbo di questo stesso schermo: :13924 chiede «Che
    #    cosa vuoi equipaggiare?» e :17020 dice «Devi equipaggiare frecce».
    #    Il gemello :12804 fa «Ti togli " + itemname(ci) + "."».
    (14769, 'You equip .'):
        '"Equipaggi " + itemname(ci) + "."',

    # ⚠️ Le tre righe del ramo maledetto / votato alla rovina / benedetto: le
    #    vede chiunque equipaggi, e il sesso di chi gioca non si conosce. Nessun
    #    participio riferito al giocatore.
    # ⭐ chara_func.hsp:2714 dice gia' «sente un brivido di freddo» per 寒気.
    (14772, 'You suddenly feel a chill and shudder.'):
        "D'improvviso ti prende un brivido di freddo.",
    # 💡 Il giapponese conta il cammino, l'inglese conta i passi: la resa tiene
    #    tutt'e due. 「破滅」 e' «rovina» in skill.hsp:1576 («Canto di rovina»).
    (14775, 'You are now one step closer to doom.'):
        'Hai mosso un passo sulla via della rovina.',
    # ⚠️ 見守る e' vegliare, non spiare: e' il ramo BENEDETTO.
    (14778, 'You feel as someone is watching you intently.'):
        'Hai la sensazione che qualcosa vegli su di te.',

    # ================================================================
    # Le tre della sete (:14799) — stesso giapponese di action.hsp:8274,
    # ricopiate parola per parola tutt'e tre.
    # ================================================================
    (14799, 'Your are too full to drink.'):
        'Non riesci a bere altro.',
    (14799, 'You are too bloated to drink any more.'):
        'La vescica sta per scoppiarti...',
    (14799, "Your stomach can't digest any more."):
        'Non hai ancora sete.',

    # ================================================================
    # Il marchio d'immagine (:14828)
    # ================================================================
    # ⭐ 「アイテム画像」 e' «icona» in :6068, :6073 e :6076, e questa resa e' il
    #    gemello speculare di :6825, «name(tc) + " ha perso l\'icona."».
    (14828, 'You attached an item mark to .'):
        'name(tc) + " ha ricevuto un\'icona."',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-038.jsonl'
DA, A = 14718, 14840
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
