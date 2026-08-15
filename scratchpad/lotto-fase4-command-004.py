# -*- coding: utf-8 -*-
"""Lotto `command-004`: le 46 origini di `*setHistory1`, la prima riga del
«Background».

La schermata sta in `chara.hsp:3265`-`:3336` e la vede **ogni personaggio
nuovo**: cinque righe tirate a sorte — origine, perche' sei partito, un pregio,
un difetto, un vizio privato — disegnate una sotto l'altra con `mes` a
`pos wx + 75, wy + 200 + n * 15`. Questo lotto e' la prima delle cinque.

⚠️⚠️ **Il soggetto non e' solo il giocatore: e' anche un ALLEATO.**
`chat.hsp:8588`-`:8593` rilegge gli stessi cinque valori da
`cdata(CDATA_BACKGROUND_PART_*, c)` e li fa raccontare a Mizuki, dove `c` e'
il compagno scelto con `*com_ally`. Quindi il genere e' ignoto in tutt'e due i
casi, e non c'e' una `lang()` gemella che distingua: **e' la stessa riga**.

✅ **Il giapponese il soggetto non ce l'ha proprio** — 「奴隷だった過去を持つ。」,
「王族の一員だった。」 — ed e' l'inglese che ci mette «You». Le rese sono
**nominali**, che e' la forma del giapponese e l'unica senza accordo: la stessa
strada che `guida-stile.md` prescrive per le etichette di stato («Inedia» e non
«Affamato»).

💡 **Le tre manovre che tolgono il participio dal soggetto**, e tornano in tutte
e cinque le righe della schermata:
  - il **nome astratto** al posto dell'aggettivo: 「奴隷だった」 -> «Un passato di
    schiavitu'», 「囚われの身」 -> «Anni di prigionia»;
  - il participio **appeso a una cosa**, non alla persona: «Genitori perduti
    troppo presto», «Il paese natale, distrutto dai mostri» — l'accordo cade su
    `genitori` e su `paese`, che un genere ce l'hanno;
  - il **nome di genere fisso** per chi la persona la nomina per forza: «Cavia»,
    «una creatura maledetta», «Un'arma nata da una tecnologia proibita»,
    «Il clone», «Un frutto nascosto». E' la strada della 40a e della 41a («Balia
    delle bestie»), qui usata quarantasei volte di fila.

⚠️ **Il tetto e' 54 caratteri**, ed e' misurato: nessuna guardia guarda questa
finestra — come per la scheda del personaggio della 43a — ma la finestra e'
larga 360 px e upstream ci fa stare `:9579`, «You were actually being raised by
your parents' enemy.». Il metro possibile e' quello di `tetti_buffdesc.py`,
l'italiano **contro l'inglese di monte**: nessuna resa supera la piu' lunga
delle 46 inglesi. Lo misura `scratchpad/misura-background.py`.

💡 **Zero copie**: `dossier.py` non trova nemmeno un giapponese o un inglese
gia' reso altrove. E' la prima zona del progetto che non pesca niente — il
generatore del passato non parla la lingua di nessun'altra schermata.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :9456 il valore quando `ohanasi1 == 0`: la riga che si stampa al posto
    #     di tutte le altre quando il passato si tiene per se'. Il giapponese e'
    #     il sostantivo nudo 「内緒」.
    (9456, 'Secret'):
        'Segreto',

    # --- :9459-:9591 le quarantacinque origini, tirate a sorte da `rnd(45) + 1`.
    (9459, 'You had no family.'):
        'Nessuna famiglia, fin dalla nascita.',
    (9462, 'You grew up without any inconveniences.'):
        "Un'infanzia senza privazioni.",
    # ⚠️ «creato» concorderebbe: il participio passa al nome della cosa
    (9465, 'You were artificially created through an experiment.'):
        'Frutto artificiale di un esperimento.',
    # ⚠️ 「実験体にされていた」 e' il cavia, non l'esperimento: nome di genere fisso
    (9468, 'You were used for human experimentation.'):
        'Cavia in un centro di ricerca.',
    (9471, 'You have amnesia.'):
        'Amnesia: del passato nessun ricordo.',
    # ⚠️ «perduti» concorda con `genitori`, non con chi legge
    (9474, 'You lost your parents early.'):
        'Genitori perduti troppo presto.',
    (9477, 'You spent your days in peace.'):
        "Giorni sereni, uno dopo l'altro.",
    (9480, 'You have been abused since childhood.'):
        "Maltrattamenti fin dall'infanzia.",
    # ⚠️ il giapponese 「自分の出生を隠している」 e' attivo — le origini si NASCONDONO,
    #    non «furono tenute segrete». «tenute» concorda con `origini`.
    (9483, 'Your birth was kept secret.'):
        'Origini tenute nascoste.',
    (9486, 'You were a faithful servant.'):
        'Anni di servizio fedele.',
    (9489, 'You were raised by a different race.'):
        "Infanzia presso un'altra razza.",
    (9492, 'You were a slave.'):
        'Un passato di schiavitù.',
    (9495, 'You were poor but grew up well.'):
        'Povertà, ma una crescita robusta.',
    (9498, 'You had a normal life.'):
        'Famiglia normale, infanzia normale.',
    (9501, 'You were a member of a royal family.'):
        'Sangue reale in famiglia.',
    (9504, 'You were loved by everyone.'):
        "Un'infanzia circondata d'affetto.",
    (9507, 'You were bedridden with a disease for a long time.'):
        'Anni di malattia, a letto.',
    (9510, 'For some reason, you were asleep for a long time.'):
        'Un lunghissimo sonno, chissà perché.',
    # ⚠️ non «Vieni dal futuro»: la riga sta in colonna con le altre quarantaquattro,
    #    che sono tutte nominali. «Origine:» tiene la forma della lista.
    (9513, 'You actually come from the future.'):
        'Origine: il mondo del futuro.',
    (9516, 'You were a prisoner for a long time.'):
        'Anni di prigionia.',
    # ⭐ «criminale» e' invariabile in genere: qui il nome della persona si puo' dire
    (9519, 'You were a criminal.'):
        'Un passato da criminale.',
    (9522, 'For some reason, you destroyed your hometown.'):
        'Il proprio paese, distrutto per varie ragioni.',
    (9525, 'You lost your hometown in a war.'):
        'Il paese natale, perduto in guerra.',
    # ⚠️ «signore di provincia» ha un genere: si rende la CARICA, non chi la porta
    (9528, 'You were a local lord.'):
        'Un passato al comando di una provincia.',
    (9531, 'You were a powerful god.'):
        'Un passato di stirpe divina e potente.',
    # ⚠️ 「忌み子」 e' «figlio maledetto», che al femminile stona: «creatura» e' il
    #    nome di genere fisso che regge chiunque
    (9534, 'You were detested and abandoned as a child.'):
        "La nomea di creatura maledetta, e l'abbandono.",
    # --- :9537-:9549 i quattro 「家系」: la resa descrive la FAMIGLIA, che un genere
    #     ce l'ha, e non chi ne discende.
    (9537, 'You come from a family of adventurers.'):
        'Una famiglia di avventurieri da generazioni.',
    (9540, 'You come from a family of noble knights.'):
        'Una famiglia di cavalieri di nobile lignaggio.',
    (9543, 'You come from a prodigious family of mages.'):
        'Una famiglia di maghi di gran fama.',
    (9546, 'You were found and raised by thieves.'):
        "Un'infanzia in mano ai briganti.",
    (9549, 'Your family were impoverished warriors.'):
        'Una famiglia di guerrieri caduti in miseria.',
    # ⭐ «erede» e' invariabile in genere
    (9552, "You were raised as your family's heir."):
        "Un'educazione severa, da erede.",
    # ⭐ «militare» e' invariabile in genere; «ferita» concorda con se stessa
    (9555, 'You are a traumatized ex-soldier.'):
        "Un ex militare con una ferita nell'animo.",
    (9558, 'You are a minion of an evil organization.'):
        "Al soldo di un'organizzazione malvagia.",
    (9561, 'You are a clone of a certain person.'):
        'Il clone di una certa persona.',
    (9564, 'You are a weapon created with forbidden technology.'):
        "Un'arma nata da una tecnologia proibita.",
    (9567, 'You were discovered and rescued in ruins as a child.'):
        'Il ritrovamento fra le rovine, ancora in fasce.',
    (9570, 'You grew up in a village with horrific customs.'):
        'Infanzia in un villaggio dalle usanze atroci.',
    # ⚠️ «nato» concorderebbe: si nominano i due sangui, non chi li porta
    (9573, 'You were born between a monster and a human.'):
        'Sangue di mostro e sangue umano insieme.',
    # ⚠️ 「隠し子」 e' «figlio nascosto»: «frutto» e' la stessa manovra di :9465
    (9576, 'You are the illegitimate child of an affair.'):
        'Un frutto nascosto del tradimento.',
    (9579, "You were actually being raised by your parents' enemy."):
        'In casa del nemico dei genitori, senza saperlo.',
    (9582, 'You were isolated because of your hidden powers.'):
        "Un potere segreto, e per questo l'isolamento.",
    # --- :9585-:9591 le tre fini del paese natale: cambia la causa, non la forma.
    (9585, 'You lost your hometown in a great disaster.'):
        'Il paese natale, perduto in un cataclisma.',
    (9588, 'Your hometown was destroyed by monsters.'):
        'Il paese natale, distrutto dai mostri.',
    (9591, 'Your hometown was destroyed by an evil adventurer.'):
        'Il paese natale, distrutto da un pessimo avventuriero.',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-004.jsonl'
DA, A = 9454, 9594
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
