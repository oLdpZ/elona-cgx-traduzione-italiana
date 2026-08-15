# -*- coding: utf-8 -*-
"""Lotto `command-024`: **dare un oggetto a un alleato**, e il bestiame che mangia.
Apre la zona 15000-15999, la piu' densa rimasta di `command.hsp` (79 firme).

⭐⭐ **Qui parla sempre qualcun altro, e non si sa mai chi**: ventisei rese su
trentasei sono battute di `tc` — l'alleato, il bestiame, il figlio — passate da
`cnvtalk`. Il genere del parlante non e' noto a chi scrive, quindi **nessuna
resa puo' contenere un participio o un aggettivo riferito a chi parla**. Le
manovre sono quelle di sempre: il nome al posto dell'aggettivo («Ho la pancia
piena!» e non «Sono pieno»), l'accordo spostato sulla cosa («Ma quanto e'
secco!», che concorda col mangime), il verbo al posto dello stato («Non ho piu'
fame!»).

⭐⭐ **E un errore di monte con la forma piu' pulita che si sia vista finora:
l'inglese di `:15188` e' l'array di `:15196` copiato addosso, senza guardare il
giapponese.** I quattro slot di `:15188` sono i quattro esiti della **borraccia
filtrante** (`:15169`-`:15186`) e il giapponese li dice tutti: `f = 2` e' la
borraccia vuota (`PARAM2 == 0`) e dice 「からっぽ！」, `f = 4` e' l'alleato che
**beve davvero** (`PARAM2 > 0`, `SOUNDLIST_DRINK1`, `THIRST += 2000`) e dice
「ありがとう！」, cioe' «grazie». L'inglese ci mette «No way.» e **«Never!»**,
che sono lo slot 2 e lo slot 4 dell'array del **rifiuto** otto righe piu' sotto.
In inglese, l'alleato beve e ti risponde «mai».
✅ La resa non deve scegliere: **la rete 3 decide da sola**, perche' 「ありがとう！」
e' gia' reso in `text.hsp:1994` come «Grazie!». Il giapponese e' l'identita'
della voce, e quando l'inglese sbaglia e' il giapponese a vincere.
💡 La lezione e' il gemello del punto 4 della 45a — «un referto puo' avere un
punto cieco suo» — dall'altro lato: qui a sbagliare non e' uno strumento, e'
**l'inglese di monte**, e a prenderlo e' stata una rete che guarda il
giapponese. Nessun conteggio di «non tradotte» lo avrebbe mai segnalato.

⚠️ **La rete 4 lega due righe che l'inglese distingue**: 「いらん」 sta in
`:15188` come «I don't want it.» e in `:15196` come «I don't need it.», stesso
giapponese e nessuna funzione di contenuto, quindi **una resa sola per tutt'e
due** — «Non mi serve!», che regge sia sull'alleato non assetato (`:15176`,
`THIRST > 10000`) sia sull'oggetto da buttare (`:15165`, `FILTER_JUNK`).
Stessa cosa per `:15101` e `:15115`, che hanno il **giapponese identico**
(name(tc) + 「に家畜の餌を食べさせた。」) e un inglese che a `:15101` dice «food for
livestock» e a `:15115` solo «food»: la resa e' una, e dice «mangime» — che vale
per tutt'e due, perche' **tutt'e due i rami pretendono `CHARA_BIT_LIVESTOCK`**.

⚠️ **Due dinamiche hanno dovuto girare la frase per la rete 8.** «You hand X to
Y» in italiano vuole «a » davanti a `name`, che si fonde con l'articolo: e'
diventata `name(tc) + " riceve " + itemname(ci, 1)`, cioe' il ricevente in testa.
Lo stesso per `:15101`, dove «dare da mangiare **a**» e' diventato «**nutrire**»,
che regge l'oggetto diretto. 💡 La rete 8 non chiede di accorciare: chiede di
scegliere un verbo che non abbia bisogno di quella preposizione.

⚠️ **`:15264` nomina un oggetto che l'inglese non nomina.** Il giapponese e'
`name(tc) + "は激怒して" + itemname(ci, 1) + "を叩き割った。"`, l'inglese
«throws it on the ground angrily» — un `itemname` in meno. La rete 11 pretende
l'insieme dell'**inglese**, quindi la resa non puo' nominare la pozione: dice
«il regalo», che e' un nome fisso e maschile e non ha bisogno di sapere che
oggetto sia.

⭐ Copiate senza decidere, tre su trentasei: «Non mi va.» (`action.hsp:9799`),
«Grazie!» (`text.hsp:1994`) e `name(tc) + " arrossisce."` (`action.hsp:10757`).
E due termini gia' fissati altrove: «pane soffice» (`db_item.hsp:141763`) e
«mangime per il bestiame» (`db_item.hsp:137486`).

💡 **Un invariato solo, ed e' un lamento**: «Nooooo!» per 「イヤぁぁあ！」. Le altre
tre del gruppo si scostano dall'inglese — «Nooo!», «No e no!», «Nooo!!!!!!» —
questa no, e in italiano si scrive identica. Va in `invariati.md`.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :15001 il bozzolo che schiude solo a febbraio.
    #     ⭐ parola per parola action.hsp:12728, stesso inglese.
    (15001, 'You have to wait until next February.'):
        'Bisogna aspettare il prossimo febbraio.',

    # --- :15007-:15027 il regalo di San Valentino rifiutato.
    #     Le prime due sono le due facce di un rnd(2) e devono restare diverse.
    #     ⭐ rete 3: 「いらん」 è già «Non mi va.» in action.hsp:9799.
    (15007, 'No way.'): 'Non se ne parla.',
    (15010, 'No way.'): 'Non mi va.',
    # 「盗んできたチョコレートなんて…」: l'inglese appiattisce, il giapponese dice
    # perché il regalo è rifiutato — è rubato (ITEM_BIT_STOLEN, :15026).
    (15027, 'No way.'): 'Cioccolatini rubati, poi...',

    # --- :15088 l'alleato già sazio (HUNGER >= 8000).
    #     ⚠️ «Sono pieno» accorderebbe col parlante: il nome al posto dell'aggettivo.
    (15088, "I'm full now!"): 'Adesso ho la pancia piena!',

    # --- :15101 e :15115 il bestiame che mangia. ⚠️ rete 4: stesso giapponese e
    #     stessa firma, quindi una resa sola. Tutt'e due i rami pretendono
    #     CHARA_BIT_LIVESTOCK, quindi «mangime» vale per l'uno e per l'altro.
    #     ⚠️ rete 8: «dare da mangiare a » + name si fonde. «Nutrire» regge
    #        l'oggetto diretto e la preposizione sparisce.
    (15101, 'You gave  food for livestock.'):
        '"Hai nutrito " + name(tc) + " con del mangime."',
    (15115, 'You gave  food.'):
        '"Hai nutrito " + name(tc) + " con del mangime."',

    # --- :15103 le cinque lagne sul mangime secco (パッサパサ).
    #     ⚠️ l'accordo cade sul mangime, mai su chi parla.
    (15103, 'This is hard!'): 'Che roba secca!',
    (15103, 'This dries your mouth!'): 'Mi si secca la bocca!',
    (15103, 'Ugh, this is so dry!'): 'Uff, ho la bocca tutta secca!',
    (15103, 'Ugh, this is hard!'): "Uff, ma quanto è secco!",
    (15103, 'Ugh, this is hard.'): 'Uff, che roba secca.',

    # --- :15108 il bestiame ingrassa.
    #     ⚠️ «è ingrassato» accorderebbe col soggetto: «mette su peso» non ha genere.
    (15108, ' grew fatter and now weighs kg.'):
        'name(tc) + " mette su peso: adesso pesa " + cdata(CDATA_WEIGHT, tc) + "kg."',

    # --- :15129-:15135 i due rifiuti del cibo.
    (15129, "I don't want it. I'm full."): 'No! Non ho più fame!',
    # 「ふかふかパン」: db_item.hsp:141763 fissa «pane soffice»
    (15135, "I-I don't want it! Get that puff puff bread away from me!!"):
        'N-no, non lo voglio! Basta con il pane soffice!!',

    # --- :15141 i quattro capricci del figlio appena nato.
    #     💡 «Nooooo!» si scrive identica all'inglese: va in invariati.md.
    (15141, 'Nooooo!'): 'Nooooo!',
    (15141, 'No!'): 'Nooo!',
    (15141, 'No! No!'): 'No e no!',
    (15141, 'No!!!!!!'): 'Nooo!!!!!!',

    # --- :15188 i quattro esiti della borraccia filtrante (:15169-:15186).
    #     ⚠️⚠️ l'inglese è l'array di :15196 copiato addosso: lo slot 2 è la
    #     borraccia vuota e lo slot 4 è l'alleato che beve e ringrazia. Si rende
    #     il GIAPPONESE. Vedi il docstring.
    (15188, 'Too heavy!'): 'Troppo pesante!',
    # 「からっぽ！」 = «vuota»: PARAM2 == 0. La borraccia filtrante è femminile
    # (db_item.hsp:135432).
    (15188, 'No way.'): "È vuota!",
    # ⚠️ rete 4: stesso 「いらん」 di :15196, una resa sola per tutt'e due.
    (15188, "I don't want it."): 'Non mi serve!',
    # ⭐ rete 3: 「ありがとう！」 è già «Grazie!» in text.hsp:1994. L'inglese dice
    #    «Never!», ed è lo slot sbagliato.
    (15188, 'Never!'): 'Grazie!',

    # --- :15196 i quattro rifiuti veri: troppo pesante, mobilio, cianfrusaglia,
    #     peso negativo.
    (15196, 'No way.'): 'Non posso!',
    (15196, "I don't need it."): 'Non mi serve!',
    (15196, 'Never!'): 'Mai!',

    # --- :15208-:15243 i rifiuti dell'oggetto da usare.
    (15208, "I don't want it. It's too creepy."):
        'Non lo voglio, non si sa nemmeno cosa sia!',
    # ⭐ stesso inglese di proc.hsp:11358, che è genderless per lo stesso motivo:
    #    l'oggetto maledetto può essere maschile o femminile.
    (15213, "It's cursed!"): 'Porta una maledizione!',
    (15230, 'Enough for me.'): 'Non riesco più a bere!',
    # 「おろす…」: l'alleata incinta a cui dai del veleno.
    (15243, 'Abortion...'): 'Meglio abortire...',

    # --- :15250-:15268 la consegna, l'anello di fidanzamento e la pozione d'amore.
    #     ⚠️ rete 8: «a » + name si fonde. Il ricevente va in testa, e la rete 11
    #        guarda l'insieme delle funzioni, non l'ordine (misura della 40a).
    (15250, 'You hand  to .'):
        'name(tc) + " riceve " + itemname(ci, 1) + "."',
    # ⭐ rete 3: parola per parola action.hsp:10757.
    (15253, ' blushes.'): 'name(tc) + " arrossisce."',
    # ⚠️ rete 11: il giapponese nomina l'oggetto con itemname, l'inglese no.
    #    La resa segue l'inglese e dice «il regalo», nome fisso e maschile.
    (15264, ' throws it on the ground angrily.'):
        'name(tc) + " va su tutte le furie e scaglia a terra il regalo."',
    # ⚠️ «pervertito» accorderebbe con chi ascolta, cioè col giocatore:
    #    l'accordo si sposta sull'atto.
    (15268, 'You scum!'): 'Sei il peggio!!',
    (15268, 'What are you trying to do!'): 'Che porcata!',
    (15268, 'Guards! Guards! Guards!'): 'Guardie! Guardie! Guardie!',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-024.jsonl'
DA, A = 15000, 15300
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
