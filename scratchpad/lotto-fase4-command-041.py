# -*- coding: utf-8 -*-
"""Lotto `command-041`: **le capacità, le direzioni e il resto della zona
5000-5999**. Ventiquattro rese, da `:5015` a `:5892`. Con questo la zona si
chiude.

⭐⭐⭐ **La scoperta di questo lotto è che `sizefix` NON è zero, e questo corregge
un numero che la 47ª aveva scritto come corretto.** La 47ª, dopo il collaudo,
aveva stabilito che `12 + sizefix - en * 2` valesse **10** «con `sizefix` assente
da `config.txt` e quindi 0». Ma `sizefix` in `config.txt` c'è, dieci righe sotto
il `font2. "Courier New"` che quella stessa sessione aveva letto:

    config.txt:84   fontSfix1.  "1"     fixes font size
    config.hsp:180  cfgRead "fontSfix1.", sizefix = int(rtvaln)
    config.hsp:436  sizefix = 0     <- solo nel ramo GIAPPONESE

Il ramo inglese (`config.hsp:439`) non lo azzera: `sizefix` resta **1**, e il
corpo è **11**, cioè **6,6 px** a carattere. Non 10 e non 6.
✅ **Nessuna resa già spedita ne esce sbagliata**: l'unico tetto che la 47ª aveva
ricavato dal corpo 10 è quello di 「命中」, 27 px, che fa 4 caratteri tanto a 6 px
quanto a 6,6 — e «Mira» ne fa 4.
⚠️ **Ma cambia il tetto della riga di aiuto di `display_window`**, che la 47ª
calcolava a 7,2 px: la formula giusta è `(larghezza − 58 − 40) / 6,6`, cioè
**42** caratteri per una finestra da 380 e non 39, **76** per una da 600 e non
69. La stessa correzione vale per `display_topic` (`module.hsp:4365`) e
`display_note` (`:4359`), che usano tutt'e tre quella riga di `font`.
💡 E la decisione della 47ª su `:11849` **resta giusta lo stesso**: la resa ovvia
faceva 44 caratteri, che sfora anche i 42 veri.

⭐ **E la riga di aiuto di questa finestra è il primo caso misurato in cui
l'italiano ci sta per tre caratteri.** `:5342` compone `s(1)` con quattro pezzi
già spediti — `strhint2` «[Pagina]», `strhint3` «Shift,Esc [Chiudi]»,
`strhint7` «0~9 [Scorciatoia]», `strhint8` «* [NASC.] / [MOSTRA]» — più i due
tasti di `key_pageup`/`key_pagedown`: **73 caratteri su 76**. L'inglese ne usa
65. Chi allungasse una di quelle quattro stringhe di quattro caratteri farebbe
sparire l'ultima parola da questo menu e da ogni altro che le concatena.

⚠️⚠️ **`:5015` e `:5096` hanno lo STESSO giapponese, la stessa firma di funzioni
e una resa già decisa altrove**: 「足元に<item>が転がってきた。」 è `:4837`, «itemname(ci)
+ " rotola fino ai tuoi piedi."». La rete 4 pretende che le due siano uguali fra
loro e la rete 3 che siano uguali a `:4837`: si ricopia, e l'inglese
«from nowhere» di `:5096` — che il giapponese non dice — si perde come si è
perso in giapponese.

⚠️ **`:5892` è la rete 11 nella forma stretta, la seconda in due lotti.**
L'inglese è `"What action do you want to perform to " + him(tc) + "? "`, e `him`
a un argomento è morfologia: funzioni di contenuto **zero**, mentre il giapponese
ha `name(tc)`. La resa non nomina nessuno — «Che cosa vuoi fare? » — ed è
un'espressione perché la voce è dinamica. Gemella di `:14852` nel lotto 039.

⭐ **Sei rese riscosse senza decidere.** 「どの方向に…？」 è «In che direzione vuoi
…? » in `proc.hsp:7607` e `:7610`; 体当たり è «caricare» in `action.hsp:1732` e
`:1740` («Carichi la porta»); ショートカット è «Scorciatoia» in `text.hsp:10` e
`:121`; 能力 è «capacità» in `:6144` e `:7218`; 広域 è «in area» in
`skill.hsp:1913`; e 「上達」 ha la sua forma in `text.hsp:3205`, «migliora in
<abilità>», che `:5072` ripete in seconda persona.

⚠️ **Due volte l'inglese dice una cosa che il giapponese non dice, e vince il
giapponese.** `:5457` parla di «sealed» dove 非表示 vuol dire **nascondere** — ed
è quel che fa il codice, `spact(p) = 2` — e la riga di aiuto lo chiama già
«[NASC.]». `:5725` dice «sort by **increasing** freshness and value» dove il
giapponese dice 「低いほうにあわせて」, cioè si allinea alla **più bassa**: è anche
l'unica lettura che spiega perché il gioco lo chieda con un sì/no.

💡 **Le tre etichette a colonna di `:5344`-`:5346` hanno margine largo**, adesso
che il corpo è noto: «Nome» ha 25 caratteri di spazio (da `wx + 28` a `wx + 220`,
meno i 26 px che `display_topic` spende per la sua icona), «Costo» ne ha 11,
«Effetto» 32. Le stesse tre etichette servono anche il menu delle capacità ad
area (`:5554`-`:5556`), che sono seconde occorrenze della stessa firma.
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
    # L'oggetto che rotola ai piedi (:5015, :5096)
    # ⚠️ Stesso giapponese fra loro (rete 4) e con :4837 (rete 3): la resa e'
    #    gia' decisa e si ricopia. «from nowhere» e' un'aggiunta dell'inglese.
    # ================================================================
    (5015, ' appear.'):
        'itemname(ci) + " rotola fino ai tuoi piedi."',
    (5096, ' appear from nowhere.'):
        'itemname(ci) + " rotola fino ai tuoi piedi."',

    # ================================================================
    # Imparare e migliorare (:5068, :5072)
    # ⚠️ L'inglese non ha `name`: la resta resta in seconda persona, come lui.
    # ⭐ 「上達」 ha la sua forma in text.hsp:3205, «migliora in <abilita'>».
    # ================================================================
    (5068, 'You learn !'):
        '"Impari " + skillname(p) + "!"',
    (5072, 'Your  skill improves!'):
        '"Migliori in " + skillname(p) + "!"',

    # ================================================================
    # Le scorciatoie (:5201-:5241)
    # ⭐ 「ショートカット」 e' «Scorciatoia» in text.hsp:10 e :121.
    # 💡 Le due impossibilita' sono parallele nel sorgente e restano parallele.
    # ================================================================
    (5201, 'The key is unassigned.'):
        'Quel tasto non ha nessuna scorciatoia.',
    (5224, "You can't use this shortcut any more."):
        "Quell'azione non è più disponibile.",
    (5241, "You can't use that spell anymore."):
        'Quella magia non è più disponibile.',

    # ================================================================
    # Le direzioni (:5250, :5279, :5750, :5806)
    # ⭐ 「どの方向に…？」 e' «In che direzione vuoi …? » in proc.hsp:7607 e :7610.
    # ⚠️ Le prime tre finiscono con uno SPAZIO in inglese, e lo spazio resta:
    #    e' la giuntura col prompt (verifica.py:440).
    # ⭐ 体当たり e' «caricare»: action.hsp:1732 e :1740, «Carichi la porta».
    # ================================================================
    (5250, 'Which direction do you want to dig? '):
        'In che direzione vuoi scavare? ',
    (5279, 'Which direction do you want to bash? '):
        'In che direzione vuoi caricare? ',
    (5750, 'Which direction? '):
        'In che direzione? ',
    (5806, 'Choose the direction of the target.'):
        'In che direzione sta il bersaglio?',

    # ================================================================
    # Il menu delle capacita' (:5342-:5470) e quello ad area (:5552, :5673)
    # ⭐ 能力 e' «capacita'» in :6144 («Mostra le capacita'») e :7218; 広域 e'
    #    «in area» in skill.hsp:1913.
    # 💡 Corpo 11 (12 + sizefix - en * 2, con sizefix = 1): 6,6 px a carattere.
    #    display_topic spende 26 px per l'icona, quindi «Nome» ha 25 caratteri
    #    di spazio, «Costo» 11, «Effetto» 32.
    # ================================================================
    (5342, 'Skill'):
        'Capacità',
    (5344, 'Name'):
        'Nome',
    (5345, 'Cost'):
        'Costo',
    # ⭐ Stesso inglese di :10847, gia' reso «Effetto», e il giapponese qui dice
    #    proprio 「能力の効果」.
    (5346, 'Detail'):
        'Effetto',
    (5552, 'Wide Skill'):
        'Capacità ad area',

    # ⚠️ L'inglese dice «sealed», il giapponese 非表示: si NASCONDE, ed e' quel
    #    che fa il codice (`spact(p) = 2`). La riga di aiuto lo chiama gia'
    #    «[NASC.]» (text.hsp:122).
    (5457, 'Directly connected skills can not be sealed.'):
        "Le capacità legate a un'abilità non si possono nascondere.",
    # 💡 «Nascosta» concorda con «capacita'», non col nome che segue: sono tutte
    #    capacita', quindi l'accordo non dipende dalla voce.
    (5462, '[Hidden: ]'):
        '"[Nascosta: " + skillname(p) + "]"',
    (5470, '[Showing all skills]'):
        '[Mostrate tutte le capacità]',
    (5673, '[Showing all wide skills]'):
        '[Mostrate tutte le capacità ad area]',

    # ================================================================
    # Accorpare gli oggetti (:5725, :5730)
    # ⚠️ L'inglese dice «increasing», il giapponese 「低いほうにあわせて」: si
    #    allinea alla piu' BASSA. E' anche l'unica lettura che spiega il si'/no.
    # ================================================================
    (5725, 'Stack items of the same type and sort by increasing freshness and value?'):
        'Vuoi unire gli oggetti uguali, allineandoli alla freschezza e al valore più bassi?',
    # ⚠️ Onomatopea: spazio davanti e dietro come in inglese. Stessa forma di
    #    «*sbuffo*» e «*bau!*» della 27a.
    (5730, ' *rummage* '):
        ' *rovista* ',

    # ================================================================
    # I tentacoli e il menu di interazione (:5879, :5892)
    # ================================================================
    # ⚠️ rete 8: «su " + name» si fonderebbe con l'articolo. La frase gira sul
    #    complemento oggetto, che non vuole preposizione.
    (5879, 'Your tentacles attacked  against your will!'):
        '"I tuoi tentacoli si sono mossi da soli e hanno assalito " + name(tc) + "!"',
    # ⚠️⚠️ `him(tc)` a un argomento e' morfologia: funzioni di contenuto zero,
    #    quindi nessun nome, benche' il giapponese abbia `name(tc)`. Gemella di
    #    :14852. Voce dinamica -> espressione (rete 12).
    (5892, 'What action do you want to perform to ? '):
        '"Che cosa vuoi fare? "',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-041.jsonl'
DA, A = 5000, 5899
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
