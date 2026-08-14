# -*- coding: utf-8 -*-
"""Lotto fase4-init-002: casa, negozio, comunita', gilda, e le cariche
cittadine (init.hsp, righe 359-390).

54 rese, ed e' il **secondo lotto piu' grosso del progetto** dopo le 68 del
`chara_func-003`. Chiude le quattro scale di rango che restavano e i due
elenchi piccoli che le seguono: i tre nomi di gilda che `guildname()` sceglie
(`:370`-`:381`) e le sei cariche di `popostname` (`:384`-`:390`).

⚠️⚠️ **L'inglese di monte ha sbagliato CONTINENTE, due volte.** `:359` gradino 0
e' 「イルヴァの楽園」 e `:360` gradino 0 e' 「イルヴァ最大の店」 — **Irva**, che e'
il mondo — e l'inglese scrive tutt'e due «Tyris», che e' **il continente** dove
sta il gioco. Non e' una semplificazione: e' un posto diverso, e il progetto ha
gia' i due nomi separati (`text.hsp:2917` «Irva Perduta», `proc.hsp:9996` «Tyris
del Nord»). ✅ Resi su Irva. Con questi la serie degli errori di monte passa da
quarantatre' a **quarantasei**: il terzo e' `:362` gradino 10, qui sotto.

⚠️⚠️ **E il terzo e' lo stesso errore del museo, ma peggio: l'inglese ha messo un
GRADINO dove andava il nome della categoria.** L'undicesima voce di ogni riga di
`rankn` non e' un rango, e' l'etichetta che `module.hsp:264` stampa in «Cambio di
rango (**Gilda** 5° → 4°)». Per le altre sette categorie l'inglese ci mette
l'etichetta giusta — `Arena`, `Pet Arena`, `Museum`, `Home`, `Shop`,
`Community` — e per la gilda ci mette **«Novice»**, che e' un grado. Il
giapponese dice 「ギルド」. ✅ «Gilda».

⚠️ **La scala della gilda e' l'unica dove l'inglese ha rifatto la classifica da
capo.** Il giapponese sale 見習い → メンバー候補 → 正式メンバー → ジャーニーマン →
エキスパート → アダプト → 重役候補 → 重役 → 右腕 → 次代マスター, cioe' una
carriera di bottega; l'inglese ci ha messo sopra `Master` e `Champion` sui due
gradini dei **重役**, che sono i dirigenti. ✅ Reso sul giapponese, con i termini
della bottega italiana: **apprendista → lavorante → maestro**, che e' la scala
vera dei mestieri. ⚠️ E `ranktitle(8)` finisce dentro una frase — `chat.hsp:5396`
fa 「ようこそ魔術士ギルドへ、」+ ranktitle(8) + 「の」+ nome — quindi ogni gradino
dev'essere un titolo che si puo' appiccicare a un nome: «Apprendista Tizio»
regge, «Della gilda» no.

💡 **I termini erano quasi tutti gia' fissati, e nessuno in una frase intera.**
ギルドマスター e' il «maestro della Gilda» (`db_creature.hsp:123766`), 見習い
l'«apprendista» (`db_creature.hsp:99431`), 乞食 l'«accattone»
(`db_creature.hsp:102544`), 徴税官 l'«esattore» (`db_item.hsp:144349`), マダム la
«dama» (`db_item.hsp:145456`), e i tre nomi di gilda stanno gia' per intero in
`db_creature.hsp:79873`-`:80071`. E' la sesta volta in due sessioni che il
lavoro sta nei **termini** e `dossier.py` non li vede.

⚠️ **Le sei cariche restano minuscole**, perche' minuscole sono in inglese
(`mayor`, `chief`, `priest`…) e perche' `podata` le stampa dentro una frase. Non
sono titoli come i ranghi.

💡 **Le quattro grida della rete 3 non sono divergenze.** Tre sono i nomi di
gilda, che in `db_creature.hsp:103737`-`:103915` compaiono dentro il nome di una
creatura — «il **membro della** Gilda dei Maghi» — mentre qui il nome della gilda
sta da solo: e' lo stesso termine in due cornici, non due decisioni. La quarta e'
「なし」, che a `text.hsp:49` e' il valore `none` di `CDATAN_NEWSEX` e **resta
inglese apposta** (vedi `invariati.md`, «Valori di dato»), mentre qui e' la
risposta di `guildname()` a chi non sta in nessuna gilda: due cose diverse con lo
stesso giapponese, e infatti hanno due inglesi diversi — `none` contro `None`.

💡 **Nessuna chiave ambigua in questa zona**: le quattro righe hanno undici
inglesi distinti ciascuna. La chiave lunga serviva solo al museo del lotto 001.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :359 la casa. ⚠️ il giapponese dice IRVA, non Tyris
    (359, 'Heaven of Tyris'):
        'Il paradiso di Irva',
    (359, 'Royal mansion'):
        'Villa da nababbi',
    (359, 'Celebrity mansion'):
        'Villa da primato',
    (359, 'Dream mansion'):
        'Casa da sogno',
    (359, 'Cozy mansion'):
        'Casa da rivista',
    (359, 'Attractive house'):
        'Casa che si fa notare',
    (359, 'Average house'):
        'Casa nella media',
    (359, 'Poor house'):
        "Casa un po' malandata",
    (359, "Peasant's shack"):
        'Casa nella miseria',
    # 乞食 e' l'«accattone» di db_creature.hsp:102544
    (359, "Beggar's shack"):
        'Tugurio da accattone',
    (359, 'Home'):
        'Casa',

    # --- :360 il negozio. ⚠️ anche qui il giapponese dice IRVA
    (360, "Tyris' greatest mall"):
        'Il negozio più grande di Irva',
    (360, 'Royal mall'):
        'Negozio da re',
    (360, 'Prosperous mall'):
        'Negozio che va a gonfie vele',
    (360, 'Celebrity shop'):
        'Negozio per gente famosa',
    (360, 'Prosperous shop'):
        'Negozio sempre pieno',
    # マダム e' la «dama» di db_item.hsp:145456
    (360, 'Popular shop'):
        'Negozio da dame',
    (360, 'Average shop'):
        'Negozio con clienti fissi',
    (360, 'Small shop'):
        'Bottega che si fa strada',
    (360, 'Souvenir shop'):
        'Bottega che non vende',
    (360, 'Unknown shop'):
        'Bottega senza nome',
    (360, 'Shop'):
        'Negozio',

    # --- :361 la comunita'.
    (361, 'Boss'):
        'Capo',
    (361, "King's advisor"):
        'Consigliere del re',
    (361, 'Elite consultant'):
        'Consulente scelto',
    (361, 'Famous consultant'):
        'Voce che conta',
    (361, 'Model voter'):
        'Elettore esemplare',
    (361, 'Nice voter'):
        'Elettore che piace alle dame',
    # ⚠️ il giapponese dice 名の知れた, «conosciuto»: l'inglese ci ha messo
    #    «Infamous», che e' il contrario
    (361, 'Infamous voter'):
        'Elettore conosciuto',
    (361, 'Average voter'):
        'Elettore qualunque',
    (361, 'Indifferent voter'):
        'Elettore disinteressato',
    (361, 'Almost voter'):
        'Elettore per un pelo',
    (361, 'Community'):
        'Comunità',

    # --- :362 la gilda, la sola scala che l'inglese ha rifatto da capo.
    (362, 'Future Guildmaster'):
        'Futuro maestro della gilda',
    (362, 'High Champion'):
        'Braccio destro del maestro',
    # ⚠️ 重役 e' il dirigente: l'inglese dice «Champion» e «Master»
    (362, 'Champion'):
        'Dirigente della gilda',
    (362, 'Master'):
        'Aspirante dirigente',
    (362, 'Adept'):
        'Adepto',
    (362, 'Expert'):
        'Esperto',
    (362, 'Journeyman'):
        'Lavorante',
    (362, 'Member'):
        'Membro effettivo',
    (362, 'Candidate'):
        'Aspirante membro',
    (362, 'Apprentice'):
        'Apprendista',
    # ⚠️ l'undicesima voce e' il NOME della categoria, non un grado: il
    #    giapponese dice 「ギルド」, l'inglese ci ha messo un rango
    (362, 'Novice'):
        'Gilda',

    # --- :371-:379 le tre gilde, come le dice gia' db_creature.hsp:79873.
    (371, 'None'):
        'Nessuna',
    (373, 'Mages Guild'):
        'Gilda dei Maghi',
    (376, 'Fighters Guild'):
        'Gilda dei Guerrieri',
    (379, 'Thieves Guild'):
        'Gilda dei Ladri',

    # --- :385-:390 le cariche cittadine, minuscole come in inglese.
    (385, 'mayor'):
        'sindaco',
    (386, 'chief'):
        'capovillaggio',
    (387, 'priest'):
        'sacerdote',
    (388, 'guard master'):
        'capo delle guardie',
    (389, 'tax master'):
        'esattore',
    (390, 'head architect'):
        'capomastro',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-init-002.jsonl'
DA, A = 359, 390
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
