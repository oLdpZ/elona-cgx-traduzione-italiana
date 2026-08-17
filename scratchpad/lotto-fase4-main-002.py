# -*- coding: utf-8 -*-
"""Lotto fase4-main-002: il rientro, la navigazione e il carretto
(main.hsp, righe 1702-1937).

Quattordici rese, e sono il seguito naturale del lotto 001: lo stesso `txt` del
registro, ma il tratto che governa il **Ritorno** e l'**imbarco**. Undici delle
quattordici escono solo quando il giocatore lancia Ritorno o sale su una nave —
cioe' a ogni viaggio, per tutta la partita.

⭐ **Il tratto e' costruito a coppie, e le coppie vanno rese a coppia.** Il
sorgente distingue sempre gli stessi due casi con la stessa variabile,
`gdata(GDATA_FLAG_SHIP_LAST_PORT)`: se vale 0 il giocatore sta **rientrando**,
se non vale 0 sta **salpando**. Le coppie sono quattro — `:1867`/`:1871`,
`:1889`/`:1893`, `:1915`/`:1919`, `:1928`/`:1932` — e in italiano si distinguono
con le stesse due parole ogni volta: «rientro» e «salpare». Renderle una per una
avrebbe prodotto otto frasi che non si assomigliano fra loro dove il codice le
tiene appaiate.

⭐ **Tre nomi propri erano gia' decisi, e con le parentesi angolari.**
`<Arasiel>`, `<Garziem>` e `<Amurdad>` stanno cosi' in `db_card.hsp` e in
`text.hsp` (gli incarichi di livello 150), e le parentesi non sono decorazione:
`init.hsp:1713` riconosce un nome proprio **dalla prima lettera**, e `<` e' quella
che glielo dice. Si ricopiano identici.
💡 `:1738` e' il caso in cui giapponese e inglese nominano **due persone
diverse**: 「ネヘルタード」 e `<Amurdad>`. Vince l'inglese, che e' il ramo da cui
la build parte e l'unico nome che il resto del gioco usa (venti rese in
`map.hsp` e `chara_func.hsp`).

⭐ **Due etichette dell'interfaccia hanno deciso due parole.**

  - `text.hsp:66` e' la barra di stato, e `Overweight` vi si chiama
    **«Sovraccarico»**. `:1898` e' la voce che annuncia proprio quello stato,
    e ripete la parola invece di inventarne una seconda.
  - `command.hsp:14176` e `action.hsp:1906` chiamano il carro del giocatore
    **«carretto»**, ed e' la parola di `:1928` e `:1932`. ⚠️ `map.hsp:1069` dice
    «carro» ed e' l'unica: due siti su tre dicono carretto, e la barra
    dell'inventario e' quella che si legge piu' spesso.

⚠️ **`:1915` ha lo stesso inglese di `calculation.hsp:1556`, e la resa e'
diversa apposta.** Li' l'inglese `"A dimensional door opens in front of you."`
sta per 「不思議な力が空間を歪めた！」 (*una forza strana ha distorto lo spazio*) ed
e' reso «Una forza strana distorce lo spazio!»; qui sta per 「あなたは次元の扉を
開けた。」 (*hai aperto la porta dimensionale*), ed e' l'arrivo del Ritorno, col
suono `SOUNDLIST_TELEPORT1`. I due giapponesi sono diversi, quindi le firme sono
diverse e la rete 3 non ha niente da dire: e' upstream che ha riciclato la
frase inglese su due eventi che non sono lo stesso.

💡 **Le virgolette di `:1898` si scrivono `\\"`**, come fa l'inglese di monte e
come fanno le altre 84 rese statiche che ne portano una. Le tipografiche `“ ”`
sono vietate: CP932 le codifica su due byte e la build inglese disegna un glifo
per byte.

⭐ **「時の管理者」 non era mai stato nominato**, e `:1937` e' il messaggio con cui
il Ritorno ti scarica in prigione invece che a casa (`gdata(GDATA_TELEPORT_AREA)
== AREA_JAIL`). «Custode del tempo» tiene insieme le due cose che 管理者 dice —
chi amministra e chi sorveglia — dove «amministratore» avrebbe fatto burocrazia
e «controllore» il bigliettaio.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1702-:1738 i tre incarichi di livello 150. I nomi stanno gia' cosi',
    # fra parentesi angolari, in db_card.hsp e in text.hsp.
    (1702, 'It seems that the mind of <Arasiel> has changed.'):
        'Pare che <Arasiel> abbia cambiato idea.',
    (1718, 'You have received a request for help from <Garziem>.'):
        'È arrivata una richiesta di aiuto da <Garziem>.',
    # Il giapponese dice 電波, un segnale radio: il messaggio arriva da lontano.
    (1738, 'You have received a rescue request from <Amurdad>.'):
        'È arrivata una chiamata di soccorso da <Amurdad>.',

    # --- :1867-:1893 le due coppie del rientro impedito. La variabile che le
    # separa e' GDATA_FLAG_SHIP_LAST_PORT: 0 = rientro, altro = imbarco.
    (1867, 'Strange power prevents you from returning.'):
        'Una forza misteriosa impedisce il rientro.',
    (1871, 'Strange power prevents you from sailing.'):
        'Una forza misteriosa impedisce di salpare.',
    (1889, 'One of your allies prevents you from returning.'):
        'Hai con te un alleato che adesso non può rientrare.',
    (1893, 'One of your allies prevents you from sailing.'):
        'Hai con te un alleato che adesso non può salpare.',

    # --- :1898 «Sovraccarico» e' il nome che text.hsp:66 da' a questo stato
    # nella barra: la voce ripete la parola invece di inventarne un'altra.
    (1898, 'Someone shouts, \\"Sorry, overweight.\\"'):
        'Da qualche parte si sente una voce: \\"Spiacente, sovraccarico.\\"',

    # --- :1910-:1919 il Ritorno che riesce.
    (1910, 'You commit a crime.'):
        'Hai infranto la legge.',
    # ⚠️ Stesso inglese di calculation.hsp:1556, ma altro giapponese e altro
    # evento: qui e' l'arrivo del Ritorno, con SOUNDLIST_TELEPORT1.
    (1915, 'A dimensional door opens in front of you.'):
        'Hai aperto una porta dimensionale.',
    (1919, 'Your ship has arrived.'):
        'La tua nave è arrivata.',

    # --- :1928-:1932 il carretto troppo pesante. «carretto» e' la parola della
    # barra dell'inventario (command.hsp:14176).
    (1928, 'Return failed because your cargo is too heavy.'):
        'Ma il carretto è troppo pesante: il rientro è fallito.',
    (1932, 'Sailing failed because your cargo is too heavy.'):
        "Ma il carretto è troppo pesante: l'imbarco è fallito.",

    # --- :1937 il Ritorno che ti scarica in prigione. 管理者 e' insieme chi
    # amministra e chi sorveglia: «custode» tiene le due cose.
    (1937, 'The capricious controller of time has changed your destination!'):
        'Il capriccioso custode del tempo ha stravolto la tua destinazione!',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-main-002.jsonl'
DA, A = 1641, 2000
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
