# -*- coding: utf-8 -*-
"""Lotto `command-013`: le 36 voci del menu che si apre su un compagno, piu' una
rinviata.

E' il menu che compare puntando un alleato, una bestia del ranch, un
prigioniero o un sacco da pugni: dai un nome, insegna a parlare, cambia
l'aspetto, sciogli la coppia, e — se e' bestiame — **scuoia**. Trentasette
`promptAdd` in un `if` a testa, tutti dentro `*com_chara`.

⭐⭐ **E qui il budget non e' una stima: e' il modello di `larghezze.py`
applicato a mano.** `command.hsp:6172` fa `val = promptx, prompty, 275, 1`
prima di `gosub *prompt_key`, quindi il riquadro e' largo **275 px** e
`larghezze.budget(275)` da' **29 caratteri**. E' la stessa formula che misura i
75 menu di `text.hsp` — solo che `larghezze.py:68` legge un file solo e questo
non lo vede. ⚠️ Se un giorno la guardia imparasse a leggere piu' file, questo
lotto e' gia' dentro il tetto: la resa piu' lunga ne fa 28.
💡 L'inglese piu' lungo ne fa 27, quindi le due misure — il modello e
`tetto-en.py` — dicono la stessa cosa. E' la prima zona della sessione in cui
si possono confrontare.

⚠️ **DUE righe sono commentate, e la seconda l'ha trovata la rete 6.** `:6148`
e' `; promptAdd lang("カスタムＡＩ", "Custom AI"), "null", 998` — la voce «Custom
AI» esiste nel sorgente ma non nel menu — e l'avevo vista leggendo. `:6070`
«Item mark adjust» no: sta dentro un `if` spento a tre righe (`:6069`-`:6071`,
`;` su tutt'e tre) in mezzo a quattro comandi vivi, e a occhio si perde.
✅ Sono le **prime due rinviate della sessione**, dopo nove lotti che non ne
avevano avuto bisogno. 💡 E il conto dice la cosa piu' utile: **una l'ho vista
io e una l'ha vista la guardia**, che e' esattamente il motivo per cui la
guardia esiste.

⚠️ Delle quattro voci «Item mark», quindi, ne restano tre: si mette l'icona, la
si sposta, la si toglie. **Regolarla non si puo'**, e il menu non lo offre.

⚠️ **Due inglesi stanno per due giapponesi diversi, e sono due comandi
diversi.** «Release» e' 「縄を解く」 a `:6110` — il sacco da pugni, che e'
*legato con una corda* — e 「檻から解き放つ」 a `:6116`, il prigioniero *in
gabbia*: «Slega» e «Libera dalla gabbia». «Information» e' 「能力の開示」 a
`:6144`, che apre la scheda delle capacita' di un alleato, e 「情報」 a `:6147`,
che e' il dump di sviluppo dietro `if ( develop | gdata(GDATA_WIZARD) )`:
«Mostra le capacita'» e «Informazioni».

💡 **Due nomi non possono avere un genere**, e la strada e' l'aggettivo
invariabile: 「大事な仲間に指定」 non e' «segna come prezioso» — che
concorderebbe col compagno — ma «Metti fra gli **indispensabili**», col suo
contrario «Togli dagli indispensabili».

⭐ **「闇のゲーム!」 ha un nome italiano gia' fatto e non e' «Play TCG (Lethal)».**
E' la citazione di *Yu-Gi-Oh!*, che in italiano e' il **«Gioco delle Tenebre»**;
e 「決闘!」 e' «Duello!», non «Play TCG!». L'inglese spiega la meccanica, il
giapponese fa la citazione — e qui vince il giapponese, che e' anche piu' corto.

Tetto 29 caratteri. Zero copie di giapponese, una di inglese.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :6002 lo zombie del negromante.
    (6002, 'Return to the coffin'):
        'Rimetti nella bara',

    # --- :6009-:6019 il bestiame del ranch. 「皮を剥ぐ」 e' scuoiare, e in
    #     italiano c'e' il verbo apposta.
    (6009, 'Bring Out'):
        'Porta fuori',
    (6013, 'Take out bone'):
        'Estrai un osso',
    (6014, 'Take out heart'):
        'Estrai il cuore',
    (6015, 'Take out eye'):
        'Cava un occhio',
    # ⚠️ 「体液」 sono i fluidi, non il sangue
    (6016, 'Take out blood'):
        'Spremi i fluidi',
    (6017, 'Take out skin'):
        'Scuoia',
    (6019, 'Name'):
        'Dai un nome',

    # --- :6026-:6047 quel che si comanda a un alleato.
    # ⚠️ 「言葉を教える」 e' una frase per volta: :6631 chiede «quale frase?»
    (6026, 'Teach Words'):
        'Insegna una frase',
    (6027, 'Change Tone'):
        'Cambia parlata',
    (6031, 'Shut up'):
        'Fai tacere',
    (6034, 'You can speak now'):
        'Lascia parlare',
    # ⚠️ «prezioso» concorderebbe col compagno: «indispensabile» e' invariabile
    (6038, 'Designate as precious ally'):
        'Metti fra gli indispensabili',
    (6041, 'Cancel precious ally status'):
        'Togli dagli indispensabili',
    (6044, "Don't pick up items"):
        'Non raccogliere oggetti',
    (6047, 'Pick up items freely'):
        'Raccogli pure gli oggetti',
    (6053, 'Wait at the town'):
        'Fai aspettare in città',

    # --- :6062-:6076 l'aspetto. 「アイテム画像」 e' l'icona che si appiccica
    #     addosso al compagno, non un oggetto.
    (6062, 'Appearance'):
        'Cambia i vestiti',
    (6065, 'Shape change'):
        'Cambia aspetto',
    # ⚠️ 「立ち姿」 e' il ritratto a figura intera, non una posa
    (6067, 'Change Tachi-e'):
        'Cambia il ritratto',
    (6068, 'Item mark set'):
        "Assegna un'icona",
    # ⚠️ :6070 «Item mark adjust» e' commentata: rinviata, non resa
    (6073, 'Item mark move'):
        "Sposta l'icona",
    (6076, 'Item mark delete'):
        "Togli l'icona",

    # --- :6094-:6098 la coppia da tag-team.
    (6094, 'Tag organization'):
        'Forma una coppia',
    (6098, 'Tag dissolution'):
        'Sciogli la coppia',

    # --- :6110, :6116 due «Release» che sono due cose diverse.
    (6110, 'Release'):
        'Slega',
    (6116, 'Release'):
        'Libera dalla gabbia',

    # --- :6125-:6138 i casi speciali.
    (6125, 'Return home'):
        'Rimanda a casa',
    (6132, 'Ask for chocolate'):
        'Chiedi del cioccolato',
    (6138, 'Offer yourself as a gift'):
        'Offriti in regalo',

    # --- :6144, :6147 due «Information», e la seconda e' da sviluppo.
    (6144, 'Information'):
        'Mostra le capacità',
    (6147, 'Information'):
        'Informazioni',

    (6155, 'Collect materials'):
        'Raccogli i materiali',

    # --- :6163-:6166 il gioco di carte. ⭐ il giapponese cita Yu-Gi-Oh!, e la
    #     citazione in italiano esiste gia'.
    (6163, 'Play TCG!'):
        'Duello!',
    (6166, 'Play TCG (Lethal)!'):
        'Gioco delle Tenebre!',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {
    (6070, 'Item mark adjust'),
    (6148, 'Custom AI'),
}

USCITA = 'lavoro/fase4-command-013.jsonl'
DA, A = 6002, 6166
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
