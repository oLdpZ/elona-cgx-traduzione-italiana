# -*- coding: utf-8 -*-
"""Lotto `command-036`: **dare un nome a un alleato, il menu del tono di voce e
l'evocazione dei PNG personalizzati**. Ventidue rese, e con queste **la zona
7000-7999 è chiusa**.

⭐⭐⭐ **La scoperta del lotto è una variabile che compone una frase inglese a
pezzi, e l'ha trovata il sorgente, non il referto.** `:7724` è
`txt lang("別世界の何かを召喚した！", "A " + s + " is summoned from another world!")`,
e quel `s` non è un nome: a `:7716`-`:7721` si carica **sei aggettivi inglesi
nudi** — `"Bad "`, `"Common "`, `"Skilled "`, `"Professional "`, `"Legendary "`,
`"Well-Known "` — uno per rango, ognuno dentro un `if ( … ) { … }` su una riga
sola, e solo a `:7722` ci aggiunge il nome vero.
⚠️⚠️ **E `variabili_en.py` non lo vedeva**, perché fino a stanotte prendeva solo
la forma `nome = "testo"` e non `nome += "testo"`. Corretto in questa sessione:
il conto passa da **66 variabili e 3 trappole** a **60 e 4**, e il quarto sito è
proprio questo. È il gemello esatto di `cnv_str_en.py` nella 45ª — **un referto
che non ha mai trovato niente in una famiglia non prova che la famiglia sia
pulita** — e anche stavolta il caso è saltato fuori leggendo il sorgente.
✅ **La resa segue il giapponese, che non nomina niente**: «Qualcosa di un altro
mondo è stato evocato!». È la stessa strada che la 38ª ha preso per `studybuddy`,
cioè il precedente di casa per questa famiglia di trappola. ⭐ Il rango si
potrebbe recuperare con **sei toppe** su `:7716`-`:7721` — e la regola della 46ª
non lo vieta, perché le toppe starebbero su righe diverse dalla resa — ma c'è un
nodo aperto: quegli aggettivi precedono un nome **che scrive il giocatore**, di
genere ignoto, e «Leggendario Anna» è sbagliato quanto l'inglese. Chi ci torna
deve prima decidere quello.

⭐⭐ **Due termini riscossi, e il secondo è la stessa espressione parola per
parola.** «Custom NPC» è già **«PNG personalizzato»** in `command.hsp:17535`; e
`:7626` — `"Piety: " + cdata(CDATA_PIETY, …) + "/" + sdata(SKILL_NORMAL_FAITH, …)
* 100` — è **identico carattere per carattere** a un pezzo di
`action.hsp:12722`, che lo rende già «**Devozione:** …». Non c'era niente da
scegliere.

⚠️⚠️ **E qui il tetto della riga di aiuto morde per la seconda volta, con una
differenza: stavolta lo sfora già l'inglese.** Tutt'e due le finestre sono da
**500 px**, quindi il tetto è (500 − 58 − 40) / 7,2 = **55 caratteri**. Ma la
riga non è solo la `lang()`: ci si sommano `strhint2` (**14** in italiano: due
tasti, una virgola e « [Pagina]  ») e `strhint3` (**20**, «Shift,Esc [Chiudi]  »),
e a `:7615` anche un `"* [Eq-Lvl] "` **fuori da qualunque `lang()`**.
- `:7505` — coda 34, quindi la `lang()` ha 21 caratteri. «Invio [cambia tono] »
  ne fa 20: totale **54**, dentro.
- `:7615` — coda **46**, quindi ne resterebbero 9. Impossibile. ⚠️ **Ma
  l'inglese è già a 59**, cioè quattro oltre il tetto, e a farlo sforare è
  proprio quel `"* [Eq-Lvl] "` che nessun dizionario raggiunge. La resa italiana
  è «Invio [evoca] », **due caratteri più corta dell'inglese**: il totale arriva
  a 60 solo perché `strhint2` e `strhint3` in italiano sono più lunghi, ed erano
  già spediti così.
⭐ **E `"* [Eq-Lvl] "` è il secondo membro della famiglia che la 46ª voleva
misurare con un `coda_en.py`** — un letterale inglese concatenato fuori dalla
parentesi di una `lang()`. Il primo era `:15489`, i «Guild Point». Questo, in
più, **è la causa dello sforamento**.

⚠️ **Tre volte l'inglese dice un'altra cosa, e tutt'e tre sono statiche senza
contratto, quindi la resa segue il giapponese**: `:7615` scrive «[Details]» dove
il giapponese ha 「召喚」, cioè **evoca** — ed è quel che il tasto fa davvero;
`:7608` scrive «Check which CNPC?» dove il giapponese chiede
「どの者を召喚したいと願うか？」, «chi desideri evocare?».

⭐⭐ **E su `:7784` la rete 3 ha parlato e aveva ragione, con un dettaglio che
non avrei trovato da solo.** 「足りないんよ」 — il rifiuto quando le monete di platino
non bastano — è già reso «Non bastano!» in `action.hsp:14356`, e lì la
condizione è `gdata(GDATA_FLAG_YACA_POINTS) < 100`: è **Yacatect**. Il dialetto
che si sente nel 「んよ」 non è un colore generico, è la sua voce, la stessa che il
lotto 028 ha reso popolana. Avevo scritto «Eh, non bastano.» prima di guardare;
la resa giusta esisteva già.

⚠️ **`:7818`, `:7823` e `:7828` sono la stessa riga giapponese sotto due inglesi
diversi, e la rete 4 pretende una resa sola — a ragione.**
「name(rc)は興奮して襲い掛かってきた。」 è identico in tutt'e tre i siti; l'inglese
distingue solo il terzo («is confused and attacks you» invece di «is excited!»).
I tre rami cambiano il valore di `CDATA_RELATION` (0, −1, −3), non il testo: è
l'autore giapponese ad aver scelto **una frase per tutti e tre**, e la rete 4
raggruppa per `(giapponese, funzioni di contenuto)`, che qui coincidono.
💡 È il rovescio del lotto 035, dove a distinguere era il giapponese e ad
appiattire l'inglese. Qui è l'inglese ad aggiungere una distinzione che
l'originale non fa, e non c'è nessuna rete che autorizzi a tenerla.

⚠️ Due accordi evitati: `:7460` è «Che nome vuoi usare?» e non «Come vuoi
chiamarlo?», perché `him(tc)` è morfologia e sparisce; `:7471` è «D'ora in poi si
chiamerà …», che vale per chiunque.
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
    # Dare un nome a un alleato (:7460-:7471)
    # ================================================================
    # ⚠️ him(tc) e' morfologia e sparisce: niente funzioni di contenuto, quindi
    #    niente «chiamarlo». L'inglese finisce con uno spazio (e' un prompt).
    (7460, 'What do you want to call ? '): '"Che nome vuoi usare? "',
    (7466, 'You changed your mind.'): 'Hai cambiato idea.',
    (7471, 'You named  .'):
        '"D\'ora in poi si chiamerà " + cdatan(CDATAN_NAME, tc) + "."',

    # ================================================================
    # Il menu del tono di voce (:7493-:7563)
    # ================================================================
    (7493, 'Default Tone'): 'Tono predefinito',
    (7505, 'Tone of Voice'): 'Elenco dei toni',
    # ⚠️ Finestra da 500 px -> tetto 55 caratteri; strhint2 (14) piu' strhint3
    #    (20) ne mangiano 34, quindi qui ce ne stanno 21. Questa ne fa 20.
    # 💡 «Invio» e non «Conferma»: nella riga di aiuto il primo pezzo e' il
    #    TASTO, come «Cursore [Scegli]», «Shift,Esc [Chiudi]», «p [Ritratto]»,
    #    e text.hsp:117 rende gia' 「決定、」 con «Invio,».
    (7505, 'Enter [Change Tone] '): 'Invio [cambia tono] ',
    (7513, 'Title'): 'Titolo',
    # ⚠️ is(tc) e' morfologia: resta `name`, e la frase va in terza persona.
    (7563, '  somewhat different.'):
        'name(tc) + " parla in un modo un po\' diverso."',

    # ================================================================
    # L'evocazione dei PNG personalizzati (:7608-:7799)
    # ⭐ «Custom NPC» e' gia' «PNG personalizzato»: command.hsp:17535.
    # ================================================================
    # ⚠️ L'inglese dice «Check which CNPC?»; il giapponese chiede chi si
    #    desidera EVOCARE, che e' quel che succede davvero.
    (7608, 'Check which CNPC?'): 'Chi desideri evocare?',
    (7615, 'Custom NPC'): 'PNG personalizzati',
    # ⚠️⚠️ Qui il tetto lo sfora gia' l'inglese: coda da 46 caratteri
    #    (strhint2 14 + strhint3 20 + «* [Eq-Lvl] » 12, quest'ultimo fuori da
    #    ogni lang()), totale inglese 59 su 55. Questa resa e' di DUE caratteri
    #    piu' corta dell'inglese. Vedi il docstring.
    # ⚠️ E «[Details]» e' sbagliato: il giapponese dice 「召喚」, e il tasto evoca.
    (7615, 'Enter [Details] '): 'Invio [evoca] ',
    # ⚠️ Colonna stretta: display_topic a wx+328 su una finestra da 500.
    (7625, 'Level(Piety Cost)'): 'Liv. (devozione)',
    # ⭐ Espressione IDENTICA a un pezzo di action.hsp:12722, gia' reso
    #    «Devozione: ». Non c'era niente da scegliere.
    (7626, 'Piety: /'):
        '"Devozione: " + cdata(CDATA_PIETY, CHARA_PLAYER) + "/" + '
        'sdata(SKILL_NORMAL_FAITH, CHARA_PLAYER) * 100',
    (7628, 'Level'): 'Livello',
    # ⚠️⚠️ La trappola di variabili_en.py: `s` porta sei aggettivi inglesi nudi
    #    da :7716-:7721. La resa segue il giapponese, che non nomina niente —
    #    come la 38a per `studybuddy`. Vedi il docstring.
    (7724, 'A  is summoned from another world!'):
        '"Qualcosa di un altro mondo è stato evocato!"',
    (7755, 'You need to be more pious to let the being pass through the dimensional barrier.'):
        'Per farlo passare attraverso il muro dimensionale serve più devozione.',
    (7759, 'You need more experience to let the being pass through the dimensional barrier.'):
        'Per farlo passare attraverso il muro dimensionale serve più esperienza.',
    (7769, '[CNPC Summon] What do you want to do?'):
        '[Evoca PNG] Che cosa vuoi fare?',
    # ⭐ La rete 3 ha parlato e aveva ragione: 「足りないんよ」 e' gia' reso «Non
    #    bastano!» in action.hsp:14356, che e' il rifiuto di YACATECT quando i
    #    suoi punti non bastano (GDATA_FLAG_YACA_POINTS). Stessa frase, stessa
    #    scena — non si compra — e lo stesso dialetto in giapponese.
    (7784, 'Not enough!'): 'Non bastano!',
    (7799, 'A custom NPC has been successfully summoned from another world!'):
        'Un PNG personalizzato è arrivato da un altro mondo!',

    # ================================================================
    # La creatura che si agita (:7818-:7828)
    # ⚠️ Stesso giapponese, due inglesi: la rete 4 pretende una resa sola, e ha
    #    ragione — a distinguere i tre rami e' CDATA_RELATION, non il testo.
    # ================================================================
    (7818, ' is excited!'):
        'cdatan(CDATAN_NAME, rc) + " si infuria e ti salta addosso."',
    (7828, ' is confused and attacks you.'):
        'cdatan(CDATAN_NAME, rc) + " si infuria e ti salta addosso."',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-036.jsonl'
DA, A = 7460, 7828
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
