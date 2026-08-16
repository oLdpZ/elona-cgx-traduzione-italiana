# -*- coding: utf-8 -*-
"""Lotto fase4-tcg-002: l'editor del mazzo, e **chiude `tcg.hsp`**
(tcg.hsp, righe 2781-9999).

28 firme su 64 chiavi — le 34 chiavi in piu' sono «Elenco» e «Mazzo», le due
schede della colonna, riscritte in **diciassette** righe (`:3544`-`:3632`), una
per ogni tipo di filtro.

⭐⭐ **Questo lotto non sarebbe stato scrivibile ieri.** Contiene tre coppie che
la rete 4 vecchia avrebbe bocciato, perche' raggruppava per **giapponese** e
pretendeva una resa sola:

    :2781 / :2786 / :2791   「また今度ね」   «Maybe next time.» / «To the
                            Amur-cage you go!» / «Noooooooooooooo!»
    :4432 / :4433           「降参する」     «Surrender» / «No»
    :4424 / :4433           「いいえ」       la stessa firma in due menu

Sono tre punti dove chi ha scritto il mod ha riusato il primo argomento di
`lang()` senza toccarlo. La rete corretta oggi raggruppa per
`(giapponese, inglese, firma)` e li lascia passare dicendolo in un 💡.

⚠️ **`:2786` e `:2791` sono i bottoni di fine partita, e dicono cose opposte**:
il primo esce quando **vinci** — l'avversario finisce nella gabbia di Amur — il
secondo quando **perdi**. Il giapponese, identico, non lo distingue.
⭐ «gabbia di Amur» viene dalla 52ª, che l'aveva resa per la prima volta in
tutto il progetto a `tcg_custom.hsp:1608`.
⚠️ **«Noooooooooooooo!» resta identica**, e va detto perche' non e' una
dimenticanza: e' un urlo, si scrive uguale nelle due lingue. Stessa scelta di
«Mana», «Immune» e «Abnormal».

⭐⭐ **«F8 [Spec]» e' sbagliato anche in inglese, e la resa lo corregge.** F8 e'
il tasto virtuale 119 (`:3942`) e apre `*DeckExportImportMenu`, cioe' il menu di
esportazione e importazione che la 52ª ha gia' tradotto («Esporta il mazzo»,
«Importa il mazzo»…). «Spec» non vuol dire niente: la riga d'aiuto dice
**«F8 [File]»**. E' la stessa disciplina di «(Ora: ERRORE)» della 52ª — si
guarda il sito, non la parola — applicata a una riga d'aiuto invece che a uno
stato.

⚠️ **Due refusi di monte non ricalcati.** `:4065` dice «You can only put **2**
copy» mentre il giapponese dice 1枚, cioe' una; e tutte e quattro dicono «copy»
al singolare con un numero davanti. La resa segue l'**inglese**, che e' la
lingua di monte, e mette il plurale italiano dove ci vuole. ⚠️ `:4077` e'
l'altro verso: il giapponese dice «la stessa carta», l'inglese «lo stesso
seme» — e sono le carte da poker del negozio, quindi l'inglese ha ragione.

💡 **«Con che nome salvare?» non e' stata scelta: era gia' li'.** `:4553` ha lo
stesso giapponese 「どのファイル名で保存する？」 di `command.hsp:17552`, e
`gia_rese.py` l'ha trovata prima che scrivessi qualcosa. Lo stesso per
「キャンセル」 → «Annulla» (`command.hsp:17318`).

💡 **Il tetto delle due schede della colonna e' nel `sdim`.** `:3543` dichiara
`sdim cfname@tcg, 16, 10`: **quindici caratteri** per scheda. «Elenco» ne fa 6 e
«Mazzo» 5, e le nove schede di dominio che stanno nello stesso array arrivano da
`domname@tcg`, che e' un'altra riga.

💡 I tetti dei menu, col metro di `larghezze.py` — `(pixel − 46) / 7,7` — perche'
`*prompt_key@` e' l'etichetta del modulo principale, cioe' proprio `*prompt_key`:

    :3972  200px -> 20 caratteri   «Azzera il mazzo» (15)   «Annulla» (7)
    :4118  240px -> 25             «Salva ed esci» (13)     «Esci senza salvare» (18)
    :4425  200px -> 20             «Chiudi il turno» (15)   «No» (2)
    :4434  200px -> 20             «Arrenditi» (9)          «No» (2)

⭐ «Arrenditi» non e' una scelta nuova: e' quella che la 52ª ha gia' messo nella
barra in fondo al tavolo, `:1095` «S [Arrenditi]».
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

# Le due schede della colonna, riscritte in diciassette righe (una per ogni
# tipo di filtro): stessa firma, stessa resa, e il tetto e' il `sdim` di :3543.
_SCHEDE = {}
for _r in (3544, 3552, 3557, 3562, 3567, 3572, 3577, 3582, 3587,
           3592, 3597, 3602, 3607, 3612, 3617, 3622, 3627, 3632):
    _SCHEDE[(_r, 'List')] = 'Elenco'
    _SCHEDE[(_r, 'Deck')] = 'Mazzo'

RESE = {
    # --- :2781-:2828 i bottoni di fine partita e il saluto d'uscita.
    (2781, 'Maybe next time.'):
        'Sarà per la prossima volta.',
    # ⚠️ Vinci: e' l'AVVERSARIO che ci finisce.
    (2786, 'To the Amur-cage you go!'):
        'Dritto nella gabbia di Amur!',
    # ⚠️ Perdi. Urlo: identico nelle due lingue.
    (2791, 'Noooooooooooooo!'):
        'Noooooooooooooo!',
    (2801, 'Maybe next time.'):
        'Sarà per la prossima volta.',
    (2828, 'Game Over! Press Enter to leave.'):
        'Partita finita! Premi Invio per uscire.',

    # --- :3366 la riga d'aiuto in fondo all'editor. ⭐ «F8 [File]» e non
    #     «[Spec]»: il tasto apre il menu d'importazione (:3942).
    (3366, ',[Filter] , [Type]  [Sort]  [Info] Enter [Select] Cancel [Exit] F8 [Spec]'):
        '"" + key_next + "," + key_prev + "[Filtro] " + key_fire + "," + key_get'
        ' + " [Tipo] " + key_search + " [Ordine] " + key_charainfo'
        ' + " [Info] Invio [Scegli] Esc [Esci] F8 [File]"',

    # --- :3970-:3971 il menu del tasto di azzeramento. 200px -> 20 caratteri.
    (3970, 'Reset Your Deck'):
        'Azzera il mazzo',
    (3971, 'Cancel'):
        'Annulla',

    # --- :4059-:4077 le quattro regole sulle copie.
    # ⚠️ «copy» al singolare con un numero davanti e' un refuso di monte, e
    #    l'italiano mette il plurale. Vedi il docstring anche per il «2».
    (4059, 'You can only put 1 copy of the same Legendary Card in your deck.'):
        'Di una stessa carta leggendaria puoi metterne una sola nel mazzo.',
    (4065, 'You can only put 2 copy of the same Neutral Card in your deck.'):
        'Di una stessa carta neutrale puoi metterne solo due nel mazzo.',
    (4071, 'You can only put 4 copy of the same Card in your deck.'):
        'Di una stessa carta puoi metterne solo quattro nel mazzo.',
    (4077, 'You can only put 13 copy of the same suit Card in your deck.'):
        'Di uno stesso seme puoi mettere solo tredici carte nel mazzo.',

    # --- :4116-:4117 l'uscita dall'editor. 240px -> 25 caratteri.
    (4116, 'Save & Exit'):
        'Salva ed esci',
    (4117, 'Just Exit'):
        'Esci senza salvare',

    # --- :4193 la stessa firma di :1173, gia' resa nel lotto 001.
    (4193, 'Choose Randomly.'):
        'Scegli a caso.',

    # --- :4283-:4310 le azioni possibili sulla carta sotto il cursore.
    # ⚠️ Il `\n` in coda e' del sito: le righe si impilano.
    (4283, 'UP: Put the card.\\n'):
        'SU: gioca la carta.\\n',
    (4289, 'Down: Sacrifice the card.\\n'):
        'GIÙ: sacrifica la carta.\\n',
    (4298, 'UP: Declare an attack.\\n'):
        'SU: dichiara un attacco.\\n',
    (4305, 'UP: Block.\\n'):
        'SU: blocca.\\n',
    (4310, 'ENTER: Use the skill.\\n'):
        "INVIO: usa l'abilità.\\n",
    (4323, 'There is no action available.'):
        'Non ci sono azioni possibili.',

    # --- :4423-:4433 i due menu di conferma. 200px -> 20 caratteri.
    (4423, 'End Turn'):
        'Chiudi il turno',
    (4424, 'No'):
        'No',
    # ⭐ «Arrenditi» e' gia' la resa della barra in fondo al tavolo (:1095).
    (4432, 'Surrender'):
        'Arrenditi',
    (4433, 'No'):
        'No',

    # --- :4541-:4574 il menu dei file del mazzo.
    (4541, '[Deck] What do you want to do?'):
        '[Mazzo] Che cosa vuoi fare?',
    # ⭐ gia' resa a command.hsp:17552, stesso giapponese.
    (4553, 'Enter file name.'):
        'Con che nome salvare?',
    (4574, 'Choose the Deck file.'):
        'Da che file costruire il mazzo?',
}

RESE.update(_SCHEDE)
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-tcg-002.jsonl'
DA, A = 2781, 9999
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\tcg.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_tcg.jsonl', encoding='utf-8') if l.strip()]
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
#
# ⚠️⚠️ **CORRETTA nella 53ª, ed e' la quinta rete che si corregge** dopo la 8,
# la 4 (per le firme di contenuto), la 9 e la 6. Il raggruppamento era per
# giapponese soltanto, e dava per scontato che uno stesso primo argomento di
# `lang()` volesse dire uno stesso messaggio. Nei file del gioco di carte non e'
# vero: chi ha scritto il mod **riusa il giapponese senza toccarlo** e cambia
# solo l'inglese.
#
#     tcg.hsp:2238  lang("これ以上は場に出せない。", "Your field is full.")
#     tcg.hsp:2264  lang("これ以上は場に出せない。", "Your opponent's field is full.")
#     tcg.hsp:2565  lang("また今度ね", "Maybe next time.")
#     tcg.hsp:2786  lang("また今度ね", "To the Amur-cage you go!")
#     tcg.hsp:4432  lang("降参する", "Surrender")   e  :4433  lang("降参する", "No")
#
# Misurato prima di toccarla: **9 giapponesi su 123** dell'estrazione `tcg`
# portano piu' di un inglese, cioe' il 7%. La rete vecchia le bocciava tutte, e
# la resa che pretendeva — «Il tuo campo e' pieno» anche per il campo
# dell'avversario — sarebbe stata **sbagliata a schermo**.
#
# ✅ La regola giusta e' quella che il progetto applica da sempre: si sostituisce
# il SECONDO argomento, quindi la lingua di monte della resa e' l'INGLESE. Due
# voci con lo stesso giapponese e lo stesso inglese devono coincidere — e quelle
# la rete continua a bocciarle. Due voci con lo stesso giapponese e un inglese
# diverso sono una distinzione di monte, e vanno **lette**, non impedite.
#
# 💡 Cosi' la rete 4 diventa simmetrica alla rete 13, che e' la stessa domanda
# vista dall'altro lato — «stesso inglese, giapponesi diversi» — ed e' un
# referto da sempre. Non c'era motivo perche' una fosse un errore duro e l'altra
# no.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
inglesi_per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], v['en'], firma_di(v))].add(parole(RESE[chiave(v)]))
    inglesi_per_jp[v['jp']].add(v['en'])
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, en, firma), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} / {en!r} con firma {firma} '
                         f'reso in {len(rese)} modi: {rese}')
for jp, inglesi in sorted(inglesi_per_jp.items()):
    if len(inglesi) > 1:
        print(f'💡 rete 4: il giapponese {jp!r} sta per {len(inglesi)} inglesi diversi '
              f'{sorted(inglesi)}: la resa segue l\'inglese, ma guarda che sia voluto')
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
