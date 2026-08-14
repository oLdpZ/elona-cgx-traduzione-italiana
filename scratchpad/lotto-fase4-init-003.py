# -*- coding: utf-8 -*-
"""Lotto fase4-init-003: gli edifici, il genere, i possessivi, l'orologio, il
log e il messaggio d'errore (init.hsp, righe 408-2873).

32 rese **+1 rinviata**, e **chiude `init.hsp`**. E' il lotto piu' vario del
progetto: ci sono sei nomi di edificio, nove valori che **non si traducono**,
cinque possessivi, sette separatori di data e un paragrafo di prosa.

⚠️⚠️ **I nove valori di `CDATAN_NEWSEX` restano inglesi, e la decisione non e'
di questo lotto: e' della Fase 0.** `male`, `female`, `none`, `hermaphrodite`,
`male?`, `female?`, `trans-male`, `trans-female` sono **scritti nel salvataggio**
(`chara.hsp:2790`, `:4390`, `item.hsp:4118`-`:4175`) e **riletti come operandi di
confronto** in cinque file (`init.hsp`, `text.hsp`, `command.hsp`, `item.hsp`,
`action.hsp`). Tradurli farebbe fallire ogni confronto su un salvataggio
esistente, e il gioco sbaglierebbe il genere di ogni personaggio gia' creato.
`invariati.md` lo dichiara dal 2026-08-07, sezione «Valori di dato».

⭐⭐ **Ma il modo di lasciarli inglesi e' cambiato, e a deciderlo e' stata la rete
7.** Il primo giro di questo lotto li aveva messi in dizionario **identici
all'inglese**, che e' il meccanismo che `invariati.md` descrive e che
`db_creature.hsp` usa per `Qy@` e `HAPPY END!!`. La rete 7 li ha fermati tutti e
nove — «riga 1813 e' un confronto, non un testo: va rinviata» — ed **ha ragione
lei**: quel testo `invariati.md` e' del 2026-08-07 e la rete 7 e' nata nel lotto
`007`, dopo. ✅ Sono **rinviati**, che e' piu' forte che renderli identici: la
resa identica passa comunque da `applica.py`, la rinviata non tocca il sito
nemmeno per riscriverci sopra la stessa stringa. Ed e' la convenzione che il
progetto usa gia' per dire «guardato, e si lascia stare» — le quattro di
`chara_func.hsp`, le sette di `proc.hsp`.
💡 **E l'asimmetria con `text.hsp` e' giusta, non un'incoerenza**: `text.hsp:123`
ha la **stessa firma** di `init.hsp:1813` e la tiene in dizionario resa
identica, perche' li' il sito e' un **assegnamento a `strmale`**, cioe' testo che
si stampa; qui e' un operando di `==`. La rete 7 guarda il sito, non la stringa.
💡 A schermo `male` e `female` arrivano lo stesso tradotti, per **sei toppe** su
`text.hsp`, che separano le righe di display dagli operandi.

⭐⭐ **E qui salta fuori un errore di monte NEL GIAPPONESE, che e' rarissimo.**
`his()` a `:1973` confronta `lang("自称男性", "female?")` — cioe' il ramo che
restituisce 「彼女？の」, «di lei?», controlla se il personaggio si dichiara
**maschio**. Le due funzioni sorelle non sbagliano: `he()` a `:1830` e `him()` a
`:2011` scrivono tutt'e due 自称女**性**. E' un refuso, ed e' nel giapponese,
mentre i quarantasei errori di monte contati finora erano quasi tutti
nell'inglese. 💡 **Ed e' innocuo per un pelo**: il secondo operando della stessa
riga e' `lang("自称女性", "trans-female")`, il cui ramo giapponese e' proprio
自称女性, quindi il caso viene preso lo stesso — un byte piu' in la' della riga.
Con questo la serie passa da quarantasei a **quarantasette**.

⭐⭐ **Il punto interrogativo di `his()` non si traduce, e quello di `he()` si:
e' la stessa marca, e in italiano vale in un caso e non nell'altro.** Upstream
distingue `his` da `his?` e `her` da `her?` per dire che il genere e'
**dichiarato** dal personaggio e non accertato. In italiano il possessivo
concorda col **posseduto**, non col possessore: «il suo» copre maschio, femmina e
chiunque altro, quindi tutt'e quattro i valori diventano **«il suo»** e il «?»
segnerebbe un dubbio su una distinzione che l'italiano **non fa**. ✅ Le cinque
rese sono «il tuo» per `your` e «il suo» per gli altri quattro.
⚠️ **Invece `he()` il «?» se lo tiene** — «lui?», «lei?», gia' in dizionario dal
lotto di Fase 1 — perche' li' il pronome soggetto in italiano il genere **lo
distingue davvero**, e il dubbio ha qualcosa su cui cadere.
💡 **E l'articolo ci vuole**: i tre siti che gia' usano `his(x, 1)` sono scritti
per riceverlo — `proc.hsp:8849` «succhi **il suo** sangue», `:9605` e `:9612`
«interrompe **il suo** daffare» — e ognuno ha accanto un nome **maschile
singolare**, che e' quel che la rete 10 pretende dal 2026-08-11.

⚠️ **`:510` e' RINVIATA, e l'ha vista la rete 6: la riga e' spenta.**
`; cdatan(CDATAN_NAME, ...) = lang("残りカス", "a garbage")` sta dentro il blocco
`// Original:` che il mod di James ha commentato — il nome che il gioco dava a un
personaggio andato perso. Tradurla sarebbe lavoro su testo morto, che
`misura-blocchi-spenti.py` conta gia' sette volte nel dizionario.

⚠️ **I sette separatori di data e orologio non sono testo, e sei su sette
restano.** `:2225` compone la data come `anno + " " + mese + "/" + giorno + " "`,
`:2227` aggiunge `ora + "h"`, `:2235` fa `ore + ":" + minuti + ":" + secondi +
" Sec"`. La barra, i due punti e la «h» l'italiano li scrive uguali; lo spazio
era **gia' dichiarato** in `invariati.md` da `text.hsp:198` (`strblank`).
✅ L'unica che cambia e' l'ultima: « Sec» diventa « sec», perche' l'italiano
abbrevia i secondi in minuscolo.
⚠️ **E qui sono le altre due chiavi ambigue del file**: lo spazio sta per 年 e
per 日, i due punti per 時間 e per 分. Chiave lunga `(riga, en, jp)` per tutt'e
quattro.

💡 **`:2082` era gia' tradotto, in un altro file, e serviva lo stesso.**
`text.hsp:363` rende 「性別不明」 «sconosciuto» ed e' la **stessa firma**; ma
`applica.py:618` cicla su `dizionario/<file>.jsonl` e applica ogni dizionario al
**suo** file soltanto. La firma e' globale, il dizionario no: la stessa voce va
scritta una volta per ogni `.hsp` che la contiene. ✅ Copiata identica.

💡 **E il file si chiude con 10 voci fuori dizionario, tutte volute**: le nove
del genere e la riga spenta di `:510`. `verifica --dizionario`
dira' «10 non ancora tradotte» per sempre, come dice «4» per `chara_func.hsp` e
«7» per `proc.hsp`.

⚠️ **Una grida della rete 3 che non e' una divergenza**: 日 e' « » qui, dove e' il
suffisso del giorno in una data, e «g» a `text.hsp:11695`, dove e' l'unita' di
misura in una scadenza («3g»). Stesso kanji, due mestieri.

💡 **Gli edifici, e un ladro diventato contrabbandiere.** `:412` e'
「盗賊の隠れ家」, e 盗賊 e' la stessa parola della «Gilda dei Ladri» del lotto 002:
l'inglese ci ha messo `Smuggler's`, che e' un altro mestiere. ✅ «Covo dei ladri».
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :408-:413 gli edifici che si costruiscono in citta'.
    (408, 'Mine'):
        'Miniera',
    (409, 'Field'):
        'Campo',
    (410, 'Art Atelier'):
        "Bottega d'arte",
    (411, 'Temple'):
        'Tempio',
    # ⚠️ 盗賊 e' la stessa parola della «Gilda dei Ladri»: l'inglese ci ha messo
    #    un contrabbandiere
    (412, "Smuggler's Hideout"):
        'Covo dei ladri',
    (413, 'Light House'):
        'Faro',

    # --- :1573 il tempo che resta, in testa a ogni messaggio dell'incarico.
    (1573, '( min left) '):
        '"(restano " + (gdata(GDATA_TIME_LIMIT) + 1) + " min) "',

    # --- :1813-:1822 e :1973: i nove valori di CDATAN_NEWSEX sono RINVIATI,
    #     non resi. Stanno tutti dentro un confronto e la rete 7 li ferma; e
    #     sono scritti nel salvataggio, quindi tradurli lo romperebbe. Vedi
    #     `rinviate003.py` e `invariati.md`, sezione «Valori di dato».

    # --- :1959-:1974 i cinque possessivi di his(x, 1).
    # ⚠️ l'italiano accorda col POSSEDUTO, non col possessore: «il suo» copre
    #    tutti e quattro i generi, e il «?» segnerebbe un dubbio su una
    #    distinzione che l'italiano non fa. L'articolo ci vuole: i tre siti che
    #    la usano gia' dicono «succhi il suo sangue», «interrompe il suo daffare»
    (1959, 'your'):
        'il tuo',
    (1965, 'his'):
        'il suo',
    (1968, 'his?'):
        'il suo',
    (1971, 'her'):
        'il suo',
    (1974, 'her?'):
        'il suo',

    # --- :2082 il genere di chi non ne ha uno dichiarato.
    # ⭐ copiata da text.hsp:363, stessa firma: applica.py e' per file
    (2082, 'unknown'):
        'sconosciuto',

    # --- :2225-:2235 i separatori di data e orologio, che testo non sono.
    (2225, ' ', '年'):
        ' ',
    # la barra non e' ambigua: un solo giapponese, chiave corta
    (2225, '/'):
        '/',
    (2225, ' ', '日'):
        ' ',
    (2227, 'h'):
        'h',
    (2235, ':', '時間'):
        ':',
    (2235, ':', '分'):
        ':',
    # ✅ l'unico dei sette che cambia: l'italiano abbrevia in minuscolo
    (2235, ' Sec'):
        ' sec',

    # --- :2555-:2556 la testa del registro dei messaggi.
    (2555, '<Message Log>'):
        '<Registro dei messaggi>',
    (2556, 'Past 20 message lines are logged.'):
        'Qui compaiono le ultime 20 righe di messaggi.',

    # --- :2873 il paragrafo che il gioco scrive in error.txt quando muore.
    (2873, '\\n\\nPlease check and organize the information as to what kind of thing you were '
           'doing when the error occurred, if it is reproducible, screenshot showing the '
           'problem, comparison of the results from the vanilla version. In addition, if you '
           'can use the bug reporting template on the Elona board development thread, it would '
           'help identify the cause and will be saved for reference. There is little chance it '
           'will be solved if you provide very little information or just the error code.'):
        "\\n\\nControlla e metti in ordine le informazioni: che cosa stavi facendo quando è "
        "comparso l'errore, se il problema si ripete, uno screenshot che mostri la "
        "situazione, il confronto con la versione originale. Poi, se puoi, segnala il "
        "problema nel thread di sviluppo del forum di Elona seguendo il modello per le "
        "segnalazioni: aiuta a trovare la causa e resta agli atti. Se dai pochissime "
        "informazioni, o solo il codice d'errore, non c'è quasi speranza di venirne a capo.",
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {
    (510, 'a garbage'),
    (1813, 'male'),
    (1813, 'none'),
    (1816, 'male?'),
    (1816, 'trans-male'),
    (1819, 'female'),
    (1819, 'hermaphrodite'),
    (1822, 'female?'),
    (1822, 'trans-female'),
    (1973, 'female?'),
}

USCITA = 'lavoro/fase4-init-003.jsonl'
DA, A = 391, 9999
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\init.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_init.jsonl', encoding='utf-8') if l.strip()]
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
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)
for v in voci:
    if sorgente[v['riga'] - 1].lstrip().startswith(';'):
        errori.append(f"rete 6: riga {v['riga']} e' commentata nel sorgente, va rinviata")
    elif v['riga'] in SPENTE:
        errori.append(f"rete 6: riga {v['riga']} sta dentro un commento di BLOCCO, va rinviata")

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
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].rstrip().endswith(' and'):
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
