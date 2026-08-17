# -*- coding: utf-8 -*-
"""Lotto fase4-main-005: il finale di Lesimas — la scena del Figlio del Caos e
il quadro del cammino (main.hsp, righe 4006-4105).

Ventidue rese, ed e' il pezzo di prosa piu' importante di `main.hsp`: la scena
che si vede **una volta sola per partita**, quando si arriva in fondo a Lesimas
e Zeome e' morto. Undici righe di racconto, poi il quadro riassuntivo con lo
sfondo `g1.bmp`, poi la stessa cosa per Remido.

⭐ **Cinque nomi propri erano gia' tutti decisi, e nessuno e' stato scelto qui:**

  - «Zeome» sta cosi' in `text.hsp:669`, e `db_card.hsp:10397` lo chiama
    «<Zeome> il falso profeta»;
  - il 「盟約」 e' il **«Patto Eterno»** (`db_creature.hsp:46255`,
    `text.hsp:9695` «Parte terza - Il patto eterno»);
  - 「ノースティリス」 e' **«Tyris del Nord»** (`text.hsp:2737`);
  - 「レミード」 e' **«le Rovine di Remido»** (`text.hsp:2979`), e la resa tiene
    le rovine perche' e' cosi' che il gioco nomina il posto ovunque;
  - 「レシマス」 resta **«Lesimas»**.

⭐⭐ **「秘宝」 non e' «il codice», ed e' il giapponese a dirlo.** L'inglese scrive
`the codex`, che in italiano non vuol dire niente di preciso; il giapponese dice
「レシマスの秘宝」, e 「秘宝」 e' gia' reso **«tesoro segreto»** in
`db_item.hsp:143525`. La resa e' «il tesoro segreto di Lesimas», che dice quel
che l'oggetto e' e riusa una parola gia' fissata invece di coniarne una.

⚠️ **La scena e' tutta al «tu», e nessuna riga puo' portare un participio.**
Il giocatore non ha genere: `:4006` dice «prima o poi doveva succedere» e non
«saresti arrivato», `:4065` mette l'arrivo come **voce di registro** («Anno 517,
12/8: arrivo a Tyris del Nord») invece di «sei sbarcato», `:4067` conta le
creature in una colonna invece di dire «hai raggiunto». E' la stessa disciplina
del lotto 003 e dei figli della 52ª, applicata a un testo lungo.

⭐ **`:4065`-`:4073` e' un QUADRO, non un paragrafo, e la resa lo scrive come
tale.** Le sei righe stanno dentro `display_window 60, 70, 680, 488` e sono
stampate una per una con `mes`, separate da `mes ""`: e' un tabellone. Il
giapponese e' una frase sola spezzata in tre (「…到達し、」「…殺して、」「…叩き出して
いる。」), l'inglese ha gia' rotto la catena, e l'italiano la rompe fino in fondo —
ogni riga sta in piedi da sola, con i due punti al posto del verbo. ⚠️ Il `\\n` di
`:4067` va tenuto: l'inglese ce l'ha messo perche' la riga non ci stava, e la
resa italiana e' piu' lunga, non piu' corta.

⭐⭐ **`:4050` fa parlare la rete 3, e la divergenza la impone UPSTREAM.** La rete
avverte che 「*勝利*」 e' gia' reso «<Vittoria>» in `skill.hsp:1780`, ed e' vero —
ma quel sito e' `skillname(SKILL_SPACT_WIN)`, cioe' il nome di una **mossa**, e
li' **l'inglese scrive `<Win>`**, con le parentesi angolari, mentre qui scrive
`*Win*`, con gli asterischi. Lo stesso giapponese, due forme inglesi diverse
scelte apposta per due mestieri diversi: la resa segue il mestiere, `<Vittoria>`
per la mossa e `*Vittoria*` per il cartello.
💡 E' la regola della 47ª — «quando la rete 3 accusa, si guarda il mestiere del
sito che cita» — in una forma piu' facile del solito: qui a distinguere i due
mestieri non serve un ragionamento, basta guardare che cosa ha fatto l'inglese.
⚠️ Gli asterischi restano per la stessa ragione di `:3024` nel lotto 004, dove
`*Loss on points*` e' diventato `*Sconfitta ai punti*`.

💡 **`:4048` riordina i due `cdatan`, e puo' farlo.** L'inglese scrive
«Blessing to NAME, AKA!», il giapponese «AKA NAME に祝福あれ！»: la rete 11
confronta l'**insieme** delle funzioni di contenuto, non la loro posizione
(misurato nella 40ª), quindi l'ordine e' una scelta di stile. Qui si tiene
quello inglese, perche' in italiano «Benedizione su Ary, il viandante!» suona e
«Benedizione sul viandante Ary!» no.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :4006-:4013 il Figlio del Caos compare. ⚠️ Niente participi riferiti
    # al giocatore: «doveva succedere» e non «saresti arrivato».
    (4006, 'Your arrival here was inevitable... sooner or later.'):
        'Era già scritto... prima o poi doveva succedere.',
    (4007, 'Space within the room distorts, and an elegant young man appears before you.'):
        'Lo spazio della stanza si deforma, e davanti a te compare un giovane di bell\'aspetto.',
    (4008, "For us, it's merely one facet of a vast, complex system, but I believe you humans know it as 'fate'?"):
        'Per noi è solo una faccia di un sistema immenso e intricato; ma voi umani, '
        'se non sbaglio, lo chiamate destino.',
    (4011, 'You earnestly attempt to suppress the shaking in your legs, but it proves difficult.'):
        'Cerchi con tutte le forze di fermare il tremito alle gambe, ma non ci riesci.',
    (4012, "The shadow of the young man with an elegant face is not a man's shadow."):
        "L'ombra di quel giovane dal viso gentile non è l'ombra di un uomo.",
    (4013, 'From the depths of his innocent eyes, you feel immeasurable strength and darkness.'):
        'In fondo a quegli occhi innocenti senti una forza e un buio senza fondo.',

    # --- :4016-:4031 il dono del tesoro. 「盟約」 e' il «Patto Eterno»
    # (db_creature.hsp:46255), 「秘宝」 il «tesoro segreto» (db_item.hsp:143525).
    (4016, 'The young man gestures at the corpse of Zeome with an ironic smile.'):
        'Il giovane indica il cadavere di Zeome con un sorriso ironico.',
    (4017, 'In accordance with the oath of the Eternal League of Nefia, the item that was guarded by this pathetic old man is now yours.'):
        'In virtù del Patto Eterno di Nefia, quel che questo povero vecchio custodiva '
        'da adesso è tuo.',
    (4020, 'You cast a suspicious gaze at the gorgeously adorned book resting on the pedestal as the man begins to speak to it...'):
        'Guardi con diffidenza il libro riccamente ornato posato sul piedistallo, '
        "mentre l'uomo comincia a parlargli...",
    (4025, 'The young man laughs and leans against the wall, wearing a mischievous smile.'):
        'Il giovane ride e si appoggia al muro, con un sorriso malizioso.',
    (4031, "...An unknown amount of time passes. The man with the terrifying eyes vanished while you weren't looking. You shake off your uncertainty, slowly reaching your hand out to the book..."):
        "...Chissà quanto tempo è passato. L'uomo dagli occhi di ghiaccio è sparito "
        "senza che te ne accorgessi. Scacci l'inquietudine e allunghi piano la mano "
        'verso il libro...',

    # --- :4048-:4050 lo striscione della vittoria. L'ordine dei due `cdatan` e'
    # quello inglese: la rete 11 confronta l'insieme, non la posizione.
    # ⚠️ «Benedizione a te, X» e non «Benedizione su X»: la rete 8 vieta una
    # preposizione che si fonde attaccata a `cdatan`, e ha ragione in generale —
    # per un PNG quel nome porta l'articolo. Il pronome scioglie il nodo.
    (4048, "Blessing to , ! You've finally acquired the codex!"):
        '"Benedizione a te, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", " '
        '+ cdatan(CDATAN_AKA, CHARA_PLAYER) '
        '+ "! Hai finalmente in mano il tesoro segreto di Lesimas!"',
    # Gli asterischi restano, come per *Sconfitta ai punti* di :3024.
    (4050, '*Win*'):
        '*Vittoria*',

    # --- :4060-:4073 il quadro del cammino: un tabellone, non un paragrafo.
    # Sei `mes` separati da righe vuote, dentro display_window 60,70,680,488.
    (4060, 'Trace'):
        'Il cammino verso la vittoria',
    (4065, 'In the year , /, you arrived at North Tyris.'):
        '"Anno " + 517 + ", " + 12 + "/" + 8 + ": arrivo a Tyris del Nord."',
    # ⚠️ Il `\n` c'e' anche nell'inglese, e serve: la riga non ci sta.
    (4067, "You've killed  creatures and reached\\nmaximum of  level of dungeons."):
        '"Creature uccise: " + gdata(GDATA_KILLED) '
        '+ ".\\nLivello di sotterraneo più profondo: " '
        '+ cnvrank(gdata(GDATA_DEEPEST)) + "."',
    (4068, 'Your score is  points now.'):
        '"Punteggio attuale: " + calcscore() + " punti."',
    (4070, 'In the year , /, you conquered Lesimas.'):
        '"Anno " + gdata(GDATA_YEAR) + ", " + gdata(GDATA_DAY) + "/" '
        '+ gdata(GDATA_MONTH) + ": conquista di Lesimas."',
    (4071, 'Upon killing Zeome, you said, '):
        '"Uccidendo Zeome hai detto: " + cnvtalk("" + wincomment)',
    (4073, 'Your journey continues...'):
        'Il tuo viaggio non finisce qui...',

    (4092, 'Do you want to watch this event again?'):
        'Vuoi rivedere la scena?',
    # 「レミード」 e' «le Rovine di Remido» ovunque nel gioco (text.hsp:2979).
    (4105, 'Unbelievable! You conquered Remido!'):
        'Incredibile! Hai conquistato le Rovine di Remido!',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-main-005.jsonl'
DA, A = 4000, 4110
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
