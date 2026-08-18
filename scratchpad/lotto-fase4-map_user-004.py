# -*- coding: utf-8 -*-
"""Il resto di `map_user.hsp`: i codici dell'allevamento, il negozio, i ranghi.

`map_user.hsp:1025`-`:2775`, cinquantadue voci, e con queste **il file e'
chiuso** per il referto del dizionario: 204 `lang()`, 203 rese e una rinviata
con toppa (`:730`, lotto 003).

## ⚠️ Due volte l'inglese di monte non regge, e decide il sito

1. **`:1510` sbaglia la reazione.** `shopval == 0` vuol dire che il giocatore ha
   **annullato** il menu dei talenti del negoziante. Il giapponese gli fa fare
   una ずっこけ — la caduta comica della delusione — e l'inglese scrive
   «smiled». Dopo un annullamento un sorriso non vuol dire niente: la resa
   segue il giapponese, «ci resta male».
2. **`:1164` ha il giapponese di un'altra riga.** 「護衛対象は放せない」 e'
   identico a `:937`, che sta all'**allevamento** e parla di lasciar libero un
   compagno; qui si e' nel **campo di prigionia** e si rinchiude. L'inglese
   distingue («release» contro «contain»), il giapponese no: e' il caso
   dell'inglese che **sa di piu'**, e si segue lui. ⚠️ La rete 3 lo segnala, ed
   e' giusto che lo segnali.

## Il vocabolario, e da dove viene

    YacaPoint          invariato, da action.hsp:1277 e db_item.hsp:135931
    punti fama         名声値, da action.hsp:1207 — stessa riga, si copia
    chip da casino'    カジノチップ, da text.hsp:2197
    monete di bronzo   ブロンズ硬貨, dal lotto 001
    Energia da Lavoro  労働エナジー, da map.hsp:12281
    accresce il potenziale   潜在能力を伸ばす, da ai.hsp:1893
    vendite            営業実績, il contatore reso «[Vendite: N]» a :407
    Arredi / Cimeli    家具 / 家宝, dalla finestra del valore (lotto 003)
    map0..map3         nomi di file, non parole: restano

💡 **`:1611` e' l'unica volta che l'inglese e' piu' oscuro del giapponese senza
sbagliare**: 片開き e' la porta a **un battente solo**, e l'inglese scrive «EW
type», che non dice niente a nessuno. La resa segue il giapponese.

## ⚠️ Tre righe sono pezzi di un'altra riga

`:2308` e `:2310` non sono frasi: sono i due addendi con cui `:2308`-`:2311`
compone `s`, che poi entra dentro `:2315`. Lo spazio in testa e' quel che li
attacca al numero che li precede, e va tenuto.

## ⚠️ E il riquadro dei talenti del negoziante e' uno dei larghi

`:1501` dichiara `val = promptx, prompty, 280 + (en * 140), 0`, cioe' **420 px
in inglese** contro 280 in giapponese: e' uno dei cinque riquadri che la lingua
**allarga** invece di stringere, e la rete 5 lo sa leggere solo dalla 60a.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1025-:1108 l'allevamento: disinfezione, codici, funzione di riordino.
    (1025, 'You need a disinfectant.'): 'Non hai il disinfettante.',
    # ⚠️ Il giapponese non nomina nessuno («ho disinfettato i locali»), l'inglese
    #    nomina due cose: la rete 11 pretende le funzioni dell'inglese.
    (1036, ' sprinkled .'):
        'name(CHARA_PLAYER) + " disinfetta i locali con " + itemname(ci, 1) + "."',
    (1073, 'Breeding will be prevented in this area.'):
        'In questo allevamento non ci saranno nascite.',
    (1082, 'Production will be prevented in this area.'):
        'In questo allevamento non ci sarà produzione.',
    (1091, 'Breeding is no longer prevented in this area.'):
        'Le nascite tornano regolari.',
    (1100, 'Production is no longer prevented in this area.'):
        'La produzione torna regolare.',
    (1108, 'This is a function to collect all the dropped items at your feet.'):
        'È la funzione che raccoglie ai tuoi piedi tutti gli oggetti a terra.',

    # --- :1150-:1253 il campo di prigionia.
    (1150, 'You cannot contain more than 30 in this camp.'):
        'Qui puoi rinchiuderne al massimo 30.',
    # ⚠️ Stesso giapponese di :937 («放せない», lasciar libero) ma inglese
    #    diverso: li' si libera all'allevamento, qui si rinchiude nel campo.
    #    E' l'inglese che sa di piu', e si segue lui.
    (1164, 'You can not contain escort target in this camp.'):
        'Non puoi rinchiudere chi devi scortare.',
    (1173, ' stay at this camp.'):
        '"Hai rinchiuso " + cdatan(CDATAN_NAME, c) + "."',
    # 💡 Stesso giapponese di command.hsp:7098.
    (1177, ' changed to original cloth.'):
        'cdatan(CDATAN_NAME, c) + " riprende l\'aspetto di prima."',
    (1250, "You don't have enough Toil-Energy..."):
        'Non hai abbastanza Energia da Lavoro...',
    # 💡 Stesso giapponese di map.hsp:9914 e text.hsp:3.
    (1253, 'Something is put on the ground.'): 'Qualcosa viene posato per terra.',

    # --- :1376-:1487 il negozio: premi, ingrandimento, tipo, addestramento.
    # 💡 «chip da casino'» viene da text.hsp:2197.
    (1376, 'You get 10 Casino chips.'): 'Hai ricevuto 10 chip da casinò.',
    (1385, "You don't have enough money..."): 'Non hai abbastanza soldi...',
    (1392, 'You extend your shop! You can display a total of  items now!'):
        '"Hai ingrandito il negozio! Adesso puoi esporre " + mdata(MDATA_MAX_INV)'
        ' + " oggetti!"',
    (1400, 'This Shop will be changeable again at .'):
        '"Il prossimo cambio sarà possibile il "'
        ' + cnvdate(adata(ADATA_SHOP_TYPE_CHANGE_COOLDOWN, gdata(GDATA_AREA)), 1) + "."',
    (1437, 'Shop type changed: .'): '"Tipo di negozio cambiato: " + shops + "."',
    # ⚠️ `his(sc)` a un argomento e' morfologia e se ne va. «accresce il
    #    potenziale» viene da ai.hsp:1893, la stessa cosa fatta al trainer.
    (1455, ' calls a trainer and develops  potential!'):
        'cdatan(CDATAN_NAME, sc) + " chiama un allenatore e accresce il potenziale!"',
    (1459, "You don't have enough bronze coins..."):
        'Non hai abbastanza monete di bronzo...',
    # 💡 «vendite» e' il contatore di :407, «[Vendite: N]».
    (1469, '120 sales exp is needed...'): 'Servono almeno 120 vendite...',
    (1476, '360 sales exp is needed...'): 'Servono almeno 360 vendite...',
    (1482, " can't earn any more feats."):
        'cdatan(CDATAN_NAME, sc) + " non può ottenerne altri."',
    (1487, ' has earned enough sales exp to learn a new feat! Which is...'):
        'cdatan(CDATAN_NAME, sc) + " ha venduto abbastanza da prendere un talento! Ed è..."',
    # ⚠️ Qui l'inglese sbaglia la reazione. `shopval == 0` vuol dire che il
    #    giocatore ha annullato il menu: il giapponese fa fare al negoziante una
    #    ずっこけ, la caduta comica della delusione, e l'inglese scrive «smiled».
    #    Decide il sito: dopo un annullamento un sorriso non vuol dire niente.
    (1510, ' smiled.'): 'cdatan(CDATAN_NAME, sc) + " ci resta male."',
    (1531, ' already has that feat.'):
        'cdatan(CDATAN_NAME, sc) + " ha già quel talento."',
    (1542, ' got a new feat.'):
        'cdatan(CDATAN_NAME, sc) + " ha preso un talento nuovo."',

    # --- :1599-:1669 le porte, le piastrelle, l'aspetto esterno.
    (1599, 'You changed door to Japan type.'):
        'Adesso le porte sono in stile giapponese.',
    (1603, 'You changed door to normal type.'): 'Adesso le porte sono normali.',
    (1607, 'You changed door to SF type.'): 'Adesso le porte sono meccaniche.',
    # 💡 片開き e' la porta a un battente solo; l'inglese scrive «EW type», che
    #    non dice niente a nessuno.
    (1611, 'You changed door to EW type.'):
        'Adesso le porte hanno un battente solo.',
    (1614, 'You have to enter the map again to apply the changes.'):
        'Per applicare del tutto le modifiche bisogna rientrare nella mappa.',
    # 💡 map0..map3 sono nomi di file, non parole: restano.
    (1637, 'You changed tile group to map0.'):
        'Gruppo di piastrelle cambiato in map0.',
    (1641, 'You changed tile group to map1.'):
        'Gruppo di piastrelle cambiato in map1.',
    (1645, 'You changed tile group to map2.'):
        'Gruppo di piastrelle cambiato in map2.',
    (1649, 'You changed tile group to map3.'):
        'Gruppo di piastrelle cambiato in map3.',
    (1661, 'Input the number of map_ . (1-33) / If input 0, undo.'):
        "Che numero ha l'immagine? (da 1 a 33; con 0 si torna a quella di prima.)",
    (1669, 'You put back the original graphic.'):
        "Hai rimesso l'aspetto di prima.",

    # --- :1792-:1980 gli ospiti, i domestici, il banco vuoto.
    (1792, 'You already have too many guests in your home.'):
        'La casa è già piena di gente.',
    (1877, 'Who do you want to hire?'): 'Chi vuoi assumere?',
    (1892, 'You hire .'): '"Hai accolto in casa " + cdatan(CDATAN_NAME, tc) + "."',
    (1980, "[Shop] Your shop doesn't have a shopkeeper."):
        '[Negozio] Il negozio non ha nessuno al banco.',

    # --- :2182-:2417 il rendiconto del negozio.
    # 💡 Stesso giapponese di action.hsp:1207 e main.hsp:6912.
    (2182, 'You gain  fame.'):
        '"Hai guadagnato " + bookfame + " punti fama."',
    (2300, "[Shop] customers visited your shop but  couldn't sell any item."):
        '"[Negozio]" + customer + " clienti sono passati, ma "'
        ' + cdatan(CDATAN_NAME, worker) + " non ha venduto niente."',
    # ⚠️ :2308 e :2310 sono i pezzi con cui `s` si compone a :2308-:2311, e
    #    finiscono dentro :2315: lo spazio in testa e' quel che li attacca al
    #    numero che li precede.
    (2308, ' gold pieces'): " monete d'oro",
    (2310, ' and  items'): '" e " + income(1) + " oggetti"',
    (2315, '[Shop] customers visited your shop and  sold  items.  put  in the'
           ' shop strong box. You got  YacaPoints.'):
        '"[Negozio]" + customer + " clienti sono passati e "'
        ' + cdatan(CDATAN_NAME, worker) + " ha venduto " + sold + " oggetti. "'
        ' + cdatan(CDATAN_NAME, worker) + " ha messo " + s + " nella cassaforte."'
        ' + " Hai guadagnato " + yaca + " YacaPoint."',
    (2417, '[Shop] imported and sold some goods for the shop, earning  gold and'
           ' put them in the shop strong box. You got  yaca points.'):
        '"[Negozio]" + cdatan(CDATAN_NAME, worker) + " ha comprato e rivenduto'
        ' merce per conto suo, guadagnando " + dokuzi + " monete d\'oro, e le ha'
        ' messe nella cassaforte. Hai guadagnato " + yaca + " YacaPoint."',

    # --- :2594-:2775 i rendiconti di rango, che escono a fine mese.
    (2594, 'Museum Rank:-> Your museum is now known as <>.'):
        '"Rango del museo: " + cnvrank(rankorg / 100) + " -> "'
        ' + cnvrank(rankcur / 100) + " Adesso il tuo museo è <" + ranktitle(3) + ">."',
    (2692, 'Unique Level:-> '):
        '"Livello unico: " + rankorg + " -> " + gdata(STARTING_GDATA_FLAG + 365) + " "',
    (2693, '/ Next stage: '): '"/ Prossima tappa: " + nokori + " "',
    (2775, 'Furniture Value: Heirloom Value: Home Rank:-> Your home is now known as <>.'):
        '"Arredi: " + gdata(GDATA_HOME_FURNITURE) / 100 + " Cimeli: "'
        ' + gdata(GDATA_HOME_VALUE) / 100 + " Rango della casa: "'
        ' + cnvrank(rankorg / 100) + " -> " + cnvrank(rankcur / 100)'
        ' + " Adesso la tua casa è <" + ranktitle(4) + ">."',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-map_user-004.jsonl'
DA, A = 1000, 3328
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\map_user.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_map_user.jsonl', encoding='utf-8') if l.strip()]
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
# vive. `event.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
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
# `event.hsp:13` compone la lista degli oggetti sulla casella con
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
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
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
