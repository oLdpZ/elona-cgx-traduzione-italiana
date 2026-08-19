# -*- coding: utf-8 -*-
"""Lotto `chat-001`: **la grotta, il risveglio, e il primo discorso di Lomias**.

Diciotto rese fra `:18610` e `:18683`, cioe' la **scena d'apertura**: il primo
testo che legge chi comincia una partita nuova, e fino a oggi era tutto inglese.
`*chat_evOpening` e' la sequenza che parte quando il personaggio appena creato
apre gli occhi nella grotta, con Larnneire e Lomias che parlano sopra di lui.

⚠️ Il lotto della 65a ne chiedeva **una** (`:18646`, «You regain
consciousness.»). Aprendo il file si e' visto che quella riga sta in mezzo a
diciassette sorelle, tutte non tradotte e tutte della stessa scena: tradurne una
sola avrebbe messo una frase italiana dentro cinque minuti di inglese.

⭐ **I nomi propri sono riscossi, non decisi**: Vindale (`db_card.hsp:10579`,
«<Lomias> il messaggero di Vindale»), Elea e Larnneire (`db_card.hsp:10566`),
Ehekatl (`god.hsp:85`), putit (`action.hsp:16907`). Il glossario dichiara
invariati i nomi di popolo e di nazione del canone Elona.

⭐ **«Heretical Forest» diventa «Foresta Eretica»**, ed e' la prima volta che
compare in dizionario: il sorgente la nomina in altri cinque posti
(`chat.hsp:1600`, `:2378`, `:7273`, `:9500` e in `scene2.hsp`), tutti ancora da
aprire, e questa resa fa da capofila.

## ⚠️⚠️ Il genere del giocatore, cinque volte in dodici righe

`guida-stile.md` vieta participi e aggettivi riferiti al giocatore, e questa
scena e' il posto del gioco dove la regola morde di piu': Lomias e Larnneire
parlano **del** ferito per tutta la sequenza. Ogni volta si e' cambiata la
costruzione invece di scegliere un genere:

    the injured is about to wake up   ->  chi abbiamo curato sta riprendendo i sensi
    you're awake already?             ->  hai gia' ripreso conoscenza?
    You were badly wounded, passed out ->  Avevi ferite gravi e giacevi senza sensi
    the one injured before you         ->  qualcuno che e' ancora intontito
    you should be more thankful        ->  dovresti ringraziare piu' volentieri

💡 E una volta la costruzione inglese e' stata **lasciata cadere**, come nei
trascorsi: «nursing a lowly adventurer» diventa «l'attesa di una guarigione
qualunque». Il disprezzo di Lomias resta, il sostantivo che porta il genere no.
⚠️ Ed e' quel che dice il giapponese, che di «lowly adventurer» non ha traccia:
「君の回復を待つために」, «per aspettare la tua guarigione». L'inglese ci ha messo
del suo, e il suo e' proprio il pezzo che in italiano non si puo' scrivere.

## Il tetto

`chatMore` (`init.hsp:48`) mette il testo in `buff`, e la finestra del dialogo
lo manda a capo a **53** caratteri disegnandone al massimo **13** righe con una
sola opzione (`chat_righe.py`, la rete della 54a). La riga piu' lunga del lotto
e' la tirata di Lomias (`:18654`): in inglese ne fa 9, in italiano 10.
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
    # La grotta, prima che il giocatore apra gli occhi (:18610-:18630)
    # ⚠️ Il giocatore e' cieco (CDATA_CONDITION_BLIND = 100): sente e basta.
    # ================================================================
    (18610, "This cave... it's a good place to keep out of the rain. Lomias, check the inner chamber to be sure there is no danger lurking here."):
        'Questa grotta... ci ripara bene dalla pioggia. Lomias, va\' in fondo a controllare che non ci siano pericoli.',
    (18611, 'Okay. Wait here.'):
        "D'accordo. Aspetta qui.",
    # ⭐ Forma attiva, come tutte le righe di morte del progetto: chara_func.hsp
    #    :4848 rende «  killed.» con «name() + " muore."».
    (18616, 'Something is killed.'):
        'Qualcosa muore.',
    # dentro cnvtalk(), che ci mette le virgolette: qui va solo il verso.
    # ⭐ RISCOSSO dalla rete 3: lo stesso 「ぐわぁ」 e' gia' reso «Gwaah!» in
    #    db_creature.hsp:102524, dove pero' l'inglese scrive «Ahhhh!» e non
    #    «Uggghhh!». Due inglesi per un giapponese solo: si segue il giapponese,
    #    o `battute --divergenti` sale da 13 a 14 per una scelta senza motivo.
    (18618, 'Uggghhh!'):
        'Gwaah!',
    (18626, '...what was that sound? ...Lomias, are you alright?'):
        '...che cos\'\u00e8 stato? ...Lomias, tutto bene?',
    (18627, "It's nothing. Looks like this cave is long abandoned. It's a good place to stay."):
        'Niente di grave. Sembra che questa grotta sia abbandonata da tempo. Ci si pu\u00f2 fermare.',
    (18628, 'I see, that\'s convenient for us... wait Lomias, what are you carrying?... Argh! Putits!'):
        'Bene, allora ci fa comodo... aspetta, Lomias, che cosa ti porti dietro?... Aaah, dei putit!',
    (18629, "Don't worry. It appears these putits had been kept as pets by someone. They are kind of... cute."):
        "Non c'\u00e8 da preoccuparsi. A quanto pare qualcuno li teneva come animali da compagnia. Sono perfino... carini.",
    # ⚠️ «the injured» e' il giocatore: niente sostantivo che porti il genere.
    (18630, 'Huh, sounds like even you have a soft spot... Come here, the injured is about to wake up.'):
        'Ma guarda, hai un lato tenero anche tu... Vieni, chi abbiamo curato sta riprendendo i sensi.',

    # ================================================================
    # Il risveglio (:18641-:18646)
    # ================================================================
    (18641, 'It was... a dream...?'):
        'Era... un sogno...?',
    # ⚠️ Qui il gioco parla al giocatore e basta: il «tu» ci sta (guida-stile).
    (18646, 'You regain consciousness.'):
        'Riprendi conoscenza.',

    # ================================================================
    # Il discorso di Lomias (:18652-:18656)
    # ================================================================
    (18652, "...you...you're awake already? Remarkable. I was beginning to worry that nursing a lowly adventurer would bring our urgent travel to a halt."):
        '...hai... hai gi\u00e0 ripreso conoscenza? Notevole. Cominciavo a temere che'
        " l'attesa di una guarigione qualunque mandasse all'aria un viaggio che non ammette ritardi.",
    (18653, 'You were badly wounded, passed out on the bank of a river. It was fortunate that we found you before the dark mantle of night enveloped this whole valley, almost as if Ehekatl, the goddess of luck herself had her eyes upon you.'):
        'Avevi ferite gravi e giacevi senza sensi sulla riva di un fiume. \u00c8 stata una'
        ' fortuna che ti trovassimo prima che il manto scuro della notte coprisse tutta'
        " la valle: quasi che Ehekatl in persona, la dea della sorte, ti tenesse d\'occhio.",
    (18654, '...stop your curious eyes. Yes, we are children of Vindale, which they call the Heretical Forest. Though we Eleas, noble but blameless \\"heretics\\", aren\'t keen to spend idle time responding to every senseless question about our race, you should be more thankful for your fate. If it weren\'t for the lady Larnneire who cured your mortal wound, you wouldn\'t even be hearing my tirade. For the lady is no ordinary Elea and only she can...'):
        '...e smettila di guardarci a quel modo. S\u00ec, siamo figli di Vindale, quella che'
        ' chiamano la Foresta Eretica. Noi Elea, \\"eretici\\" nobili e senza colpa, non'
        ' abbiamo tempo da perdere con ogni domanda sciocca sulla nostra razza; ma tu'
        ' dovresti ringraziare pi\u00f9 volentieri la sorte che ti \u00e8 toccata. Se non fosse per'
        ' la nobile Larnneire, che ti ha guarito una ferita mortale, non saresti nemmeno'
        " qui ad ascoltare la mia tirata. Perch\u00e9 lei non \u00e8 un\'Elea qualunque, ed \u00e8 la sola"
        ' che possa...',
    (18655, 'You talk too much Lomias, even though the one injured before you is still dazed.'):
        'Parli troppo, Lomias. E hai davanti qualcuno che \u00e8 ancora intontito.',
    # dinamica: il nome del giocatore resta dov'e'
    (18656, "...yes, it's a bad habit of mine. Well, ..."):
        '"...hai ragione. \u00c8 un mio brutto vizio, lo so. ...Allora, "'
        ' + cdatan(CDATAN_NAME, CHARA_PLAYER) + "..."',

    # ================================================================
    # Fuori dalla scena: la scorta arrivata, e il messaggio ricordato
    # ================================================================
    # ⚠️ «We made it» sarebbe «Siamo arrivati», che concorda con chi parla piu'
    #    il giocatore: la forma senza participio non fa nessun accordo.
    (18662, 'We made it! Thank you!'):
        "Ce l'abbiamo fatta! Grazie!",
    (18683, ' recalled your message...'):
        'cdatan(CDATAN_AKA, tc) + " si ricorda del tuo messaggio..."',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-chat-001.jsonl'
DA, A = 18600, 18700
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_chat.jsonl', encoding='utf-8') if l.strip()]
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
