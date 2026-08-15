# -*- coding: utf-8 -*-
"""Lotto `command-042`: **la bacheca, l'elenco dei PNG, le prenotazioni e il
jukebox**. Ventotto rese, da `:3120` a `:3845`, più sei voci tenute fuori. Con
questo la zona 3000-3999 si chiude, ed è la terza della sessione.

⚠️⚠️⚠️ **Le sei fuori sono il nodo `CDATAN_NEWSEX` che la 46ª aveva segnalato —
e la lezione della sessione è che NON era da decidere: era già deciso dalla Fase
0, e io stavo per deciderlo una seconda volta in un altro modo.**
`invariati.md` ha dal **2026-08-07** una sezione intera intitolata «Valori di
dato, non testo — tradurli rompe i salvataggi», che nomina per riga proprio
`command.hsp:3639-3654` e dichiara invariate `male`, `female`, `none`,
`hermaphrodite`, `male?`, `female?`, `trans-male`, `trans-female`. E
`text.hsp:123` ha già in dizionario `en='male'` con `it='male'`.
❌ La prima stesura di questo lotto le **rinviava**, con tanto di motivo scritto.
Il motivo era giusto e la mossa sbagliata: una rinviata resta aperta per sempre e
ritorna a galla a ogni sessione, mentre queste sei sono **chiuse da nove mesi** —
mancava solo la riga in dizionario. Le mette
`scratchpad/invariati-command-newsex.py`, fuori dal lotto perché la rete 7 le
ferma (sono confronti) e ha ragione a fermarle: quel che non sa è che per questa
famiglia c'è una decisione più specifica.
💡 **La lezione è più larga del caso**: prima di scrivere il motivo di un rinvio,
si cerca il valore in `invariati.md`. Il motivo che stavo per scrivere era una
riscoperta, non una scoperta.

⚠️ Perché la famiglia non si traduca, comunque, vale la pena riassumerlo: il
valore di `CDATAN_NEWSEX` fa **quattro mestieri con una firma sola** — etichetta
di menu (`:4653`-`:4656`), valore **salvato** (`:4678`-`:4690`, `:4707`), chiave
di confronto (qui, in `init.hsp:1813`-`:2008` dentro `he()`/`his()`/`him()`, e in
`text.hsp:359`-`:375`) e testo stampato nudo (`:3640`-`:3655`, `:17834`,
`init.hsp:2085`). Un salvataggio inglese contiene la stringa inglese.
✅ E che sia così lo dice upstream: `init.hsp:1816` confronta con «male?» **e**
«trans-male», cioè tiene un ramo di compatibilità per il nome vecchio.

💡 **Una cosa nuova però c'era, ed è finita in `invariati.md`: `bisexual`.**
`:3639` confronta `CDATAN_NEWSEX` con «bisexual», ma chi il valore lo **scrive**
— `chara.hsp:2790` e `command.hsp:4686` — scrive «hermaphrodite». Il ramo è
**morto nella build inglese**, e con lui la riga di stampa `:3640`; in giapponese
la stringa è 「両性具有」 da tutt'e due le parti e funziona. È il gemello esatto di
`hermaphorodite`, che sta in quella lista dal 2026-08-07 per la stessa ragione.

⭐⭐ **Sette rese su ventotto sono state riscosse, non decise.** 「情報」 è
«Informazioni» (`:6147`), e la rete 3 lo pretende; 「 gold」 è « oro»
(`text.hsp:193`), stesso giapponese; ガードブレイク è **«Rottura guardia»**
(`skill.hsp:957` e `:1789`); 依頼 è «Incarico» (`text.hsp:11875`) e 依頼人
«cliente» (`:11877`); 掲示板 è «bacheca» (`db_item.hsp:151223`); 予約 è «Prenota»
(`text.hsp:135`); ジャーナル è «diario» in cinque file.

⭐ **`:3643` invece si traduce, e la rete 7 lo conferma da sola.** 「性別不明」 /
«unknown» non è mai una chiave: `:4656` la usa come **etichetta** di menu, ma la
scelta 5 scrive `lang("なし", "none")`, non «unknown». Ed è già resa
«sconosciuto» in `init.hsp:2082`, dove `gendername()` la restituisce: si ricopia.
💡 Provata la rete 7 riga per riga sulle sette: confronto a `:3639`, `:3642`,
`:3645`, `:3648`, `:3651`, `:3654`; **passa** a `:3643`. Esattamente il taglio
giusto.

💡 **Quattro rese sono invariati, e sono dichiarati in `invariati.md`, non fatti
passare.** `$` e `$ x ` (`:3392`, `:3397`) sono il simbolo della ricompensa in
bacheca, dove il giapponese usa 「★」: l'inglese ha scelto un altro segno e
l'italiano non ne ha un terzo. `(` e `)` (`:3634`) sono punteggiatura.
⚠️ **E la parentesi non è pigrizia, è misura**: la riga dell'età vive in **19**
caratteri, fra `wx + 372` e la colonna dei valori a `wx + 512`, e
«Lv.100 female?(999)» ne fa esattamente 19. « anni)» ne costerebbe cinque.

💡 **Le altre larghezze, col corpo giusto del lotto 041.** Le intestazioni passano
da `display_topic`, corpo 11 e 26 px d'icona: «Informazioni» ha 17 caratteri fra
`wx + 350` e `wx + 490`, «Assunzione (paga)» ne ha 21 fra `wx + 490` e il bordo,
«Stato» ne ha 12. Le righe girano invece a corpo 12 (`:3589`, `14 - en * 2`),
7,2 px: quella di `allyctrl == 4` — «Hp:100%» più «/contrasto/» (`:1356`, già
spedita) più « Rottura guardia:100%» — fa **39 caratteri su 44**, contro i 33
dell'inglese.
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
    # Il diario (:3120)
    # ⭐ 「ジャーナル」 e' «diario» in action.hsp:8282, chara_func.hsp:3964,
    #    command.hsp:6869, map.hsp:1197, proc.hsp:4228 e text.hsp:4.
    # ================================================================
    (3120, 'Journal'):
        'Diario',

    # ================================================================
    # La bacheca degli incarichi (:3290-:3425)
    # ⭐ 依頼 e' «Incarico» (text.hsp:11875), 依頼人 «cliente» (:11877),
    #    掲示板 «bacheca» (db_item.hsp:151223).
    # ================================================================
    (3290, 'It seems there are no new notices.'):
        'Non sembra ci siano incarichi nuovi in bacheca.',
    (3320, 'Notice Board'):
        'Incarichi in bacheca',
    # 💡 Due invariati: sono simboli, e il passo della colonna e' 13 px (:3391).
    (3392, '$'):
        '$',
    (3397, '$ x '):
        '$ x ',
    (3425, 'Do you want to meet the client?'):
        'Vuoi incontrare il cliente?',

    # ================================================================
    # L'elenco dei PNG e dei candidati (:3543-:3677)
    # ⭐ NPC e' «PNG» (:7615). Intestazioni a corpo 11 (display_topic) piu' 26 px
    #    d'icona: «Informazioni» ha 17 caratteri, la terza colonna ne ha 21.
    # ================================================================
    (3543, 'NPC List'):
        'Elenco dei PNG',
    (3546, 'Chara List'):
        'Elenco dei candidati',
    (3550, 'Wage'):
        'Paga',
    (3553, 'Init. Cost(Wage)'):
        'Assunzione (paga)',
    # ⭐ ガードブレイク e' «Rottura guardia» in skill.hsp:957 e :1789.
    (3559, 'GuardBreak'):
        'Rottura guardia',
    # ⭐ 出血 come stato e' «Sanguinamento» (:1888).
    (3562, 'Bleeding Lv'):
        'Sanguinamento',
    (3565, 'Name'):
        'Nome',
    (3568, 'Name'):
        'Nome',
    # ⭐ Stesso giapponese di :6147, gia' reso «Informazioni»: la rete 3 lo
    #    pretende, e i 17 caratteri di colonna ci stanno.
    (3570, 'Info'):
        'Informazioni',
    # 💡 Riga a corpo 12: «Hp:100%» + «/contrasto/» (:1356) + questa fa 39
    #    caratteri sui 44 fra wx+372 e il bordo. L'inglese ne fa 33.
    (3627, ' GuardBreak:%'):
        '" Rottura guardia:" + cdata(CDATA_GUARD_BREAK, i) + "%"',
    # ⚠️ Due invariati, e non per pigrizia: la riga dell'eta' vive in 19
    #    caratteri fra wx+372 e wx+512, e «Lv.100 female?(999)» ne fa gia' 19.
    #    « anni)» ne costerebbe cinque che non ci sono.
    (3634, '('):
        '(',
    (3634, ')'):
        ')',
    # ⭐ Non e' mai una chiave: :4656 la usa come etichetta, ma la scelta 5
    #    scrive lang("なし", "none"). Ed e' gia' resa «sconosciuto» in
    #    init.hsp:2082, dove gendername() la restituisce.
    (3643, 'unknown'):
        'sconosciuto',
    # ⭐ Stesso giapponese di text.hsp:193 (« gold» -> « oro»): si ricopia, e lo
    #    spazio davanti serve, perche' :3677 concatena senza.
    (3677, 'gp'):
        ' oro',

    # ================================================================
    # Le prenotazioni in libreria (:3739-:3807)
    # ⭐ 予約 e' «Prenota» in text.hsp:135 e «prenotare» in :13924.
    # ================================================================
    (3739, 'Reserve List'):
        'Prenotazioni',
    (3741, 'Name'):
        'Nome',
    (3742, 'Status'):
        'Stato',
    # 💡 L'inglese mette un trattino, il giapponese dice 「入荷なし」/「入荷予定」:
    #    la colonna ha 18 caratteri e la distinzione ci sta per intero.
    (3777, '-'):
        'Non prenotato',
    (3781, 'Reserved'):
        'Prenotato',
    (3807, 'Ah, that book is unavailable.'):
        'Ah, quel libro non si trova.',

    # ================================================================
    # Il jukebox (:3843-:3845)
    # 💡 L'inglese dice «Name», il giapponese 「タイトル」: e' il titolo di un brano.
    # ================================================================
    (3843, 'Playlist'):
        'Elenco dei brani',
    (3845, 'Name'):
        'Titolo',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {
    # ⚠️ Non sono rinviate nel senso solito: sono le sei stringhe di
    #    CDATAN_NEWSEX, che `invariati.md` dichiara invariate dal 2026-08-07 e
    #    che entrano in dizionario con
    #    `scratchpad/invariati-command-newsex.py`. Stanno fuori dal LOTTO
    #    perche' la rete 7 le ferma — sono confronti — e ha ragione a fermarle:
    #    quel che non sa e' che per questa famiglia c'e' una decisione piu'
    #    specifica. Vedi il docstring.
    (3639, 'bisexual'),
    (3642, 'none'),
    (3645, 'male'),
    (3648, 'female'),
    (3651, 'male?'),
    (3654, 'female?'),
}

USCITA = 'lavoro/fase4-command-042.jsonl'
DA, A = 3000, 3999
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
