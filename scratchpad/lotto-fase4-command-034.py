# -*- coding: utf-8 -*-
"""Lotto `command-034`: **il congedo degli otto dèi, i cioccolatini di San
Valentino e la gabbia**. Sedici rese, e sono l'apertura della zona 7000-7999.

⭐⭐⭐ **Otto rese su sedici non le ho decise io: sono gli stessi otto dèi del
lotto 028, che dicono addio invece di salutare.** `:7015`-`:7050` è il congedo di
Itzpalt, Yacatect, Jure, Lulwy, Ehekatl, Opatos, Kumiromi e Mani; `:4490`-`:4547`
era il loro arrivo, reso nella 46ª. Stessi personaggi, stesso registro, e il
registro **si riscuote**:

| dio | arrivo (46ª) | congedo (qui) |
|---|---|---|
| Lulwy | «Che sfacciataggine, convocarmi così.» | «Per stavolta ti lascio andare, gattino.» |
| Opatos | «Muahahahah! Eccomi qua!» | «Muahahahahahah! Addio.» |
| Kumiromi | «Mi hai chiamato... che gioia...» | «Non dimenticare... veglierò sempre su di te...» |
| Mani | «Hai fatto bene a chiamarmi. Ti concedo il diritto di adorarmi.» | «Per l'ultima volta, guarda di che cosa è capace questo trasferitore spaziale!» |
| Itzpalt | «Imprimilo nella tua anima: anche questo è destino tessuto dall'Elemento.» | «È tempo che io torni al mondo cui appartengo.» |
| Yacatect | «Se mi chiami, arrivo subito! Allora? C'è un affare da fare?» | «E allora ciao, eh!» |
| Jure | «N-non è mica che volessi venire, sai! Per niente!» | «N-non è mica che mi senta sola, sai! Per niente!» |
| Ehekatl | «Miaomiaomiaaa!» | «Torno a casa! A casa!» |

⭐⭐ **E l'eco di Jure non è una mia trovata: è nel giapponese.** L'arrivo è
「べ、別に来たくて来たわけじゃないんだからね！」 e il congedo
「ベ、別に寂しくなんかないんだから！」 — **la stessa costruzione**, balbettio compreso.
La resa italiana la ripete perché la ripete l'originale, non per simmetria.

⚠️⚠️ **E per abbinare dio e battuta ho dovuto capire una cosa che a occhio si
legge al contrario: in `*wish` il `txt` PRECEDE il suo `characreate`.** A
`:4490` c'è «Miaomiaomiaaa!» e a `:4493` `characreate CREATURE_ID_EHEKATL`; a
`:4497` la battuta arrogante e a `:4500` `LULWY`. Chi leggesse la battuta come
appartenente alla creatura creata **sopra** attribuirebbe ogni voce al dio
sbagliato, e lo sbaglio sarebbe invisibile: otto battute plausibili, tutte
sulla bocca di qualcun altro.
✅ Il controllo che lo dimostra è `:4547`, 「きゅー♪」: se la battuta appartenesse al
`characreate` precedente sarebbe di **Jure**, mentre `:4550` crea la
`QUANTUM_CREATURE` — ed è la forma di vita quantistica a fare «Quu», come la 46ª
aveva già scritto a proposito delle divergenze volute.
💡 Qui non serviva, perché `:7015`-`:7050` hanno un `if ( cdata(CDATA_ID, tc) ==
CREATURE_ID_… )` esplicito sopra ciascuna. Ma serviva per leggere il lotto 028,
cioè per sapere **da chi** si riscuote.

⚠️ **Cinque voci su `:7072` sono la stessa riga**, perché `txt` sceglie a caso
fra i suoi argomenti (`init.hsp:44`, `txtc = rnd(txtc)`): sono cinque varianti
della scena dei cioccolatini. Due sono `cnvtalk` (statiche) e tre sono
descrizioni con `name(tc)`.
⚠️ **E l'inglese di monte ci ha perso uno spazio**: `:7072` scrive
`name(tc) + "fidgeted a bit before…"` senza spazio dopo la funzione, quindi in
inglese si legge «Annafidgeted a bit». La resa italiana ce lo rimette — non è una
toppa, è che la resa **è** il letterale e lo spazio ci sta dentro.

⚠️ **Tre accordi evitati, e tutti per lo stesso motivo**: chi parla o di chi si
parla può essere di qualunque genere. `:7098` è «riprende l'aspetto di prima» e
non «è tornato»; `:7072` è «Davvero ti va bene, da una persona come me?» e non
«da uno come me»; `:7056` è «Hai rimandato a casa …» e non «… è tornato a casa».

⚠️ `:7094` porta **`name` due volte** in inglese, e la rete 11 conta le
occorrenze: la resa ne ha due anche lei. 「連行対象」 è chi va consegnato a
qualcuno, da cui «non è più da consegnare».
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
    # Il congedo degli otto dèi (:7015-:7050)
    # ⭐ Registro riscosso dal lotto 028 (:4490-:4547), l'arrivo degli stessi.
    #    Vedi la tabella nel docstring.
    # ================================================================
    # ITZPALT — solenne, 「我が」. Come :4526, «anche questo è destino tessuto
    #    dall'Elemento».
    (7015, 'Then I shall return to the world where I belong.'):
        'È tempo che io torni al mondo cui appartengo.',
    # YACATECT — il Kansai di 「ほなさいならー！」, cioè la popolana. Come :4533,
    #    «Se mi chiami, arrivo subito!».
    (7020, 'See ya!'): 'E allora ciao, eh!',
    # ⭐ JURE — il giapponese RIPETE la costruzione dell'arrivo,
    #    「べ、別に…んだからね！」 / 「ベ、別に…んだから！」, e la resa la ripete con lui.
    #    :4540 era «N-non è mica che volessi venire, sai! Per niente!».
    (7025, "I-I'm not lonely at all!"):
        'N-non è mica che mi senta sola, sai! Per niente!',
    # LULWY — arrogante, e chiama il giocatore 「子猫ちゃん」. Come :4497,
    #    «Che sfacciataggine, convocarmi così.».
    (7030, "I'll let you off the hook this time, kitty."):
        'Per stavolta ti lascio andare, gattino.',
    # EHEKATL — la gatta bambina che raddoppia le parole. Come :4490,
    #    «Miaomiaomiaaa!».
    (7035, "I'm going home! Home!"): 'Torno a casa! A casa!',
    # OPATOS — la risata. Come :4504, «Muahahahah! Eccomi qua!».
    (7040, 'Muwahahahahahahahahaha! Farewell.'):
        'Muahahahahahah! Addio.',
    # KUMIROMI — i puntini. Come :4511, «Mi hai chiamato... che gioia...».
    (7045, 'Do not forget... I will always be watching over you...'):
        'Non dimenticare... veglierò sempre su di te...',
    # MANI — il dio della macchina, altezzoso. Come :4518, «Ti concedo il
    #    diritto di adorarmi.». 「空間転移装置」 non ha un termine gia' deciso.
    (7050, 'Allow me to demonstrate one last time what this spatial shifter can do!'):
        "Per l'ultima volta, guarda di che cosa è capace questo trasferitore "
        'spaziale!',
    # ⚠️ Non «… è tornato a casa»: tc puo' essere di qualunque genere.
    (7056, 'You ask  to return to heaven.'):
        '"Hai rimandato a casa " + name(tc) + "."',

    # ================================================================
    # I cioccolatini di San Valentino (:7072)
    # ⚠️ Cinque varianti della stessa scena: `txt` ne sceglie una a caso.
    # ================================================================
    (7072, 'Please take it. These are my true feelings.'):
        'Tieni... sono i miei veri sentimenti.',
    # ⚠️ L'inglese di monte ha perso lo spazio dopo name(tc): «Annafidgeted».
    #    La resa e' il letterale, quindi lo spazio ce lo rimette.
    (7072, 'fidgeted a bit before taking out a package from  pocket.'):
        'name(tc) + " tentenna un po\', poi tira fuori un pacchetto dalla tasca."',
    (7072, ' hastily takes out some chocolate and shoves it in your face, blushing.'):
        'name(tc) + " arrossisce, tira fuori in fretta un cioccolatino e te lo '
        'mette sotto il naso."',
    (7072, ' smiles and shows you the chocolate  hid behind  back.'):
        'name(tc) + " sorride e mostra il cioccolatino che teneva nascosto '
        'dietro la schiena."',
    # ⚠️ «da una persona come me» e non «da uno come me»: chi parla puo' essere
    #    di qualunque genere.
    (7072, 'Are you really okay with someone like me...?'):
        '...Davvero ti va bene, da una persona come me?',

    # ================================================================
    # La gabbia (:7094-:7098)
    # ================================================================
    # ⚠️ L'inglese porta `name` DUE volte e la rete 11 conta le occorrenze.
    #    「連行対象」 e' chi va consegnato a qualcuno.
    (7094, 'You let  out of the cage.  is now free...'):
        '"Fai uscire " + name(tc) + " dalla gabbia. Ormai " + name(tc) + '
        '" non è più da consegnare."',
    # ⚠️ «riprende» e non «è tornato»: nessun accordo da indovinare.
    (7098, ' changed to their original shape.'):
        'cdatan(CDATAN_NAME, tc) + " riprende l\'aspetto di prima."',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-034.jsonl'
DA, A = 7015, 7098
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
