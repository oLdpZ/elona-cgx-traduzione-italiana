# -*- coding: utf-8 -*-
"""Lotto `command-014`: i 27 materiali che un compagno ti consegna, piu' la riga
che apre la consegna.

E' il comando «Raccogli i materiali» del lotto prima: ogni alleato porta quel
che ha raccolto in giro, e il gioco stampa una riga per tipo. Ventotto
dinamiche, tutte sulla stessa forma.

⚠️⚠️ **I nomi NON sono di questo file, e questa e' la trappola.** I 59 nomi
canonici stanno in `material_data.hsp:249`… — `matname(MATERIAL_PEBBLE) =
lang("石ころ", "Pebble")` — e quel file **non ha ancora un dizionario**. Qui
compaiono annegati dentro una frase: il giapponese di `:6289` e'
「マテリアル:**石ころ**を" + m1 + "個受け取った。」, che **contiene** 石ころ ma
non gli e' uguale.
⚠️ Quindi ne' `dossier.py` ne' la rete 3 li pescano: e' esattamente il caso
della 42a — un termine deciso in un file che torna a chiedere il conto in un
altro — e la risposta che quella sessione aveva gia' scritto e' **`glossario.md`**.
✅ I 27 nomi sono stati aggiunti li', in una tabella loro, col numero di riga di
`material_data.hsp` accanto. Chi apre quel file li trova gia' decisi.

⭐ **La forma non fa concordare niente col numero.** L'inglese scrive «You get 3
Pebble.», che e' sgrammaticato anche in inglese; l'italiano non puo' scrivere
«Ricevi 3 pietruzza» ne' indovinare il plurale di una variabile. ✅ Il
giapponese ha gia' la soluzione — 「石ころ**を3個**受け取った」, col contatore 個
che lascia il nome invariato — e in italiano il contatore e' la **parentesi**:
«Materiale ricevuto: pietruzza (3).» Il participio cade su «materiale», che un
genere ce l'ha suo.

⚠️ **Un nome diverge fra giapponese e inglese, e vince l'inglese.** 「風切石」 e'
«pietra che taglia il vento», ma la costante si chiama
`MATERIAL_ELEMENT_FRAGMENT` e l'inglese scrive «Element fragment» — e nel gioco
ci sono altre quattro «schegge» (etere, mithril, ferro, memoria, magia). Qui
**la coerenza batte il giapponese**, che e' la formula della 42a: «scheggia
elementale», per non lasciare un solo membro della famiglia fuori.
💡 E' l'unico dei ventisette in cui le due lingue non dicono la stessa cosa.

⭐ **Uno era gia' deciso**: 「魔法のインク」 e' «inchiostro magico» da
`action.hsp:12351`-`:12355`, le due righe che ti dicono quanto ne serve per una
pergamena.

⚠️ `:6248` porta `name(tc)` **come contenuto** e `he(tc)` come morfologia: il
primo resta, il secondo sparisce. «raccolti» concorda con «materiali», non col
compagno.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :6248 la riga che apre la consegna. ⚠️ `name(tc)` e' contenuto e resta,
    #     `he(tc)` e' morfologia e sparisce; «raccolti» concorda con «materiali».
    (6248, ' handed over the materials  has gathered during your adventures.'):
        'name(tc) + " ti consegna i materiali raccolti durante il viaggio."',

    # --- :6289-:6305 le pietre.
    (6289, 'You get  Pebble.'):
        '"Materiale ricevuto: pietruzza (" + m1 + ")."',
    (6293, 'You get  Fine stone.'):
        '"Materiale ricevuto: pietra pregiata (" + m2 + ")."',
    (6297, 'You get  Ether fragment.'):
        '"Materiale ricevuto: scheggia di etere (" + m3 + ")."',
    # ⚠️ 「風切石」 e' «pietra del vento», ma la costante e' ELEMENT_FRAGMENT e le
    #    schegge sono una famiglia: qui la coerenza batte il giapponese
    (6301, 'You get  Element fragment.'):
        '"Materiale ricevuto: scheggia elementale (" + m4 + ")."',
    (6305, 'You get  Chaos stone.'):
        '"Materiale ricevuto: pietra del caos (" + m5 + ")."',

    # --- :6349-:6365 l'acqua.
    (6349, 'You get  Waterdrop.'):
        '"Materiale ricevuto: goccia d\'acqua (" + m1 + ")."',
    (6353, 'You get  Hot water.'):
        '"Materiale ricevuto: acqua calda (" + m2 + ")."',
    (6357, 'You get  Snow.'):
        '"Materiale ricevuto: neve (" + m3 + ")."',
    (6361, "You get  Witch's tear."):
        '"Materiale ricevuto: lacrima di strega (" + m4 + ")."',
    (6365, "You get  Angel's tear."):
        '"Materiale ricevuto: lacrima d\'angelo (" + m5 + ")."',

    # --- :6407-:6423 il bosco.
    (6407, 'You get  Stick.'):
        '"Materiale ricevuto: bastone (" + m1 + ")."',
    (6411, 'You get  Branch.'):
        '"Materiale ricevuto: ramo (" + m2 + ")."',
    (6415, 'You get  Holy weed.'):
        '"Materiale ricevuto: erba sacra (" + m3 + ")."',
    (6419, 'You get  Shining weed.'):
        '"Materiale ricevuto: erba lucente (" + m4 + ")."',
    # ⚠️ nome proprio del canone Elona, con la sua storpiatura: non «Yggdrasil»
    (6423, 'You get  Sap of Yaggdrasil.'):
        '"Materiale ricevuto: linfa di Yaggdrasil (" + m5 + ")."',

    # --- :6465-:6481 la carne e la magia.
    (6465, 'You get  Human gene.'):
        '"Materiale ricevuto: gene umano (" + m1 + ")."',
    (6469, 'You get  Troll gene.'):
        '"Materiale ricevuto: gene di troll (" + m2 + ")."',
    (6473, "You get  Rabbit's tail."):
        '"Materiale ricevuto: coda di coniglio (" + m3 + ")."',
    (6477, "You get  Witch's eye."):
        '"Materiale ricevuto: occhio di strega (" + m4 + ")."',
    (6481, 'You get  Fairy dust.'):
        '"Materiale ricevuto: polvere di fata (" + m5 + ")."',

    # --- :6533-:6557 la bottega. ⚠️ 「わめく狂人」 e' un MATERIALE che si chiama
    #     cosi', non una persona.
    (6533, 'You get  Cloth.'):
        '"Materiale ricevuto: pezza di stoffa (" + m1 + ")."',
    (6537, 'You get  Paper.'):
        '"Materiale ricevuto: carta (" + m2 + ")."',
    (6541, 'You get  Yelling madman.'):
        '"Materiale ricevuto: pazzo urlante (" + m3 + ")."',
    # ⭐ copiata: action.hsp:12351 rende gia' 「魔法のインク」 «inchiostro magico»
    (6545, 'You get  Magic ink.'):
        '"Materiale ricevuto: inchiostro magico (" + m4 + ")."',
    (6549, 'You get  Magic mass.'):
        '"Materiale ricevuto: massa magica (" + m5 + ")."',
    (6553, 'You get  Generator.'):
        '"Materiale ricevuto: macchina generatrice (" + m6 + ")."',
    (6557, 'You get  Electricity.'):
        '"Materiale ricevuto: elettricità (" + m7 + ")."',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-014.jsonl'
DA, A = 6248, 6557
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
