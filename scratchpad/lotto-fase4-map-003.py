# -*- coding: utf-8 -*-
"""Lotto fase4-map-003: i sotterranei, il Sigillo Eterno, i famigli e la Chiesa
della Sorella Maggiore (map.hsp, righe 4210-9000).

52 rese, zero rinviate. `map.hsp` passa da 107 a **159 su 260**.

⭐⭐ **Due nomi importanti erano gia' decisi altrove, e le mie prime scelte li
avrebbero spaccati tutti e due.**
- 「神の間」 l'avevo scritto «Sala del Dio», guardando il giapponese
  («la stanza del dio»). ✅ Ma `text.hsp` lo rende gia' **«il Sigillo Eterno»**
  in due righe di trama — «Devo puntare al Sigillo Eterno, in fondo alla grande
  fortezza del caos» — seguendo l'inglese «The Eternal Seal». Le tre righe di
  qui (`:4496`, `:4510`, `:4540`) sono **lo stesso posto** in tre stati.
- 「冥宮」 l'avevo scritto «Palazzo dei Morti». ✅ Ma `db_creature.hsp` rende
  gia' 冥宮の悪鬼 «il demone del **palazzo infero**», e i sei piani di
  `:6524`-`:7011` sono quel palazzo.
💡 **E' la lezione del `Bolt` della 35a in forma nuova**: una scelta presa una
volta in un file, che torna a chiedere il conto in un altro mesi dopo. La
differenza e' che stavolta i due termini non erano in `glossario.md` — stavano
solo in dizionario, e a trovarli e' stata una ricerca per sottostringa
giapponese. ⚠️ **E' esattamente lo strumento che la 40a aveva chiesto**
(`termini.py`, punto 5 delle cinque cose): qui e' servito due volte in un lotto
solo, e l'ho fatto a mano.

⭐ **La Chiesa della Sorella Maggiore era attesa dalla 39a.** `:8809` e'
「姉の教会」, e il culto delle sorelle maggiori e' la materia per cui quella
sessione aveva messo 姉波動 «Onda Sororale» in `glossario.md` **prima di
servire**, dicendo che il grosso stava in `chat.hsp`. Il primo posto dove il
termine tocca terra e' invece questo. ✅ «Chiesa della Sorella Maggiore», che e'
anche il registro che `text.hsp` usa gia' («La sorella maggiore, a Ludus, mi ha
chiesto…»).

⚠️⚠️ **La rete 13 grida quattro volte, ed e' il record di `map.hsp`.** Con le
due dei lotti `001` e `002` fanno **sei appiattimenti di toponimi in un file
solo**, e a questo punto non e' piu' un caso: l'inglese di `map.hsp` e' stato
scritto guardando la funzione, non il posto.
- **«Hall» sta per cinque piani diversi**: 15階大広間 (lotto `002`), poi
  20階, 25階, 30階 e un 大広間 senza numero. ✅ «Salone del piano 20/25/30» e
  «Salone»;
- **«The Eternal Seal» sta per tre stati**: 神の間<復元>, 神の間<崩壊> e
  神の間 nudo. ✅ «<ricomposto>», «<in rovina>», e il nome nudo. Il codice
  conferma: sono tre mappe distinte;
- **«Underground passage» sta per due posti**, e uno dei due giapponesi e' un
  **segnaposto di sviluppo**: `:5839` dice 「仮」, cioe' «provvisorio». ⚠️ Qui il
  giapponese non aiuta e l'inglese si', che e' il rovescio di tutto il resto del
  lotto. ✅ «Cunicolo» per il segnaposto e «Passaggio sotterraneo» per 地下通路,
  cosi' restano due;
- **«basement» sta per una cantina e per un covo di demoni**: 地下室 contro
  悪魔の巣. ✅ «Cantina» e «Nido del demonio».

⚠️ **E tre volte l'inglese non appiattisce: butta via.** Non e' la rete 13,
perche' l'inglese non ripete niente — dice solo un'altra cosa.
- `:7901` chiama «The Mine» quello che il giapponese chiama エウダーナ駐屯地,
  il **presidio di Eulderna**. E «The Mine» era gia' preso da スライムの坑道 del
  lotto `002`, quindi l'inglese ha due miniere e il giapponese nessuna delle due;
- `:8408` chiama «Deep-Sea Castle» il 九頭竜の城, il **castello del drago a nove
  teste**: il mostro che ci sta dentro sparisce dal nome;
- `:5972` chiama «Eulderna city» quello che il giapponese chiama 王宮近隣,
  «nei pressi del palazzo reale».
💡 In tutti e tre ho seguito il giapponese, che e' la regola del progetto dal
Gioco delle Ombre della 39a.

💡 **«Albedrion» invece si perde, e l'ho verificato prima.** `:7303` e' l'unica
riga di **tutto il codice** che contiene quella parola — `grep` su 72 file ne
trova una sola — quindi non c'e' nessuna continuita' da rispettare e il nome
inglese non e' mai ripreso da nessuna parte. ✅ Vince il giapponese:
「眠れる神艦・上層」, «Nave divina dormiente - ponte alto».
⚠️ Se un giorno saltasse fuori che «Albedrion» e' il nome della nave in una riga
di `chat.hsp` non ancora estratta, questa e' la resa da rivedere per prima.

💡 **I tre 使い魔 non sono schiavi.** L'inglese scrive «magic shop slave»,
«general shop slave», «furniture shop slave»; 使い魔 e' il **famiglio**, la
creatura evocata che serve un mago. ✅ «il famiglio della bottega magica», «il
famiglio della merceria» — e i due nomi di bottega vengono tali e quali da
`text.hsp:420` e `:440`, dove erano gia' decisi.

⚠️ **`:6552` e' reso IDENTICO all'inglese, ed e' un invariato nuovo.**
「？？？？」 diventa «????»: e' il nome di un personaggio che il gioco tiene
nascosto, e quattro punti interrogativi si scrivono uguali in ogni lingua.
Dichiarato in `invariati.md`. ⚠️ Il giapponese usa i punti interrogativi **a
larghezza intera** e l'inglese quelli ASCII: la resa segue l'inglese, perche' e'
il ramo che sostituisce.

💡 **I sei suffissi di citta' seguono il lotto `002` senza pensarci**: «di
Eirel», «di Melkawn», «di Kurualm», «di Valm», «di Arcbelc», «di Ludus» — tutti
e sei i nomi erano gia' fissati da `text.hsp`, e nessuno prende l'articolo.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :4267 la sala dei seguaci. 眷属 e' «seguaci» in skill.hsp, non «evil»
    (4267, 'Hall of evil'):
        'Sala dei Seguaci',

    # --- :4373-:4465 gli altri quattro «Hall». Col :4158 del lotto 002 sono
    #     CINQUE piani diversi sotto lo stesso inglese.
    (4373, 'Hall'):
        'Salone del piano 20',
    (4389, 'Hall'):
        'Salone del piano 25',
    (4411, 'Hall'):
        'Salone del piano 30',
    (4465, 'Hall'):
        'Salone',

    # --- :4496-:4540 il Sigillo Eterno nei suoi tre stati.
    # ⭐⭐ «Sigillo Eterno» non e' una scelta: text.hsp lo rende gia' cosi' in
    #     due righe di trama, e 神の間 e' lo stesso posto
    (4496, 'The Eternal Seal'):
        'Sigillo Eterno <ricomposto>',
    (4510, 'The Eternal Seal'):
        'Sigillo Eterno <in rovina>',
    (4540, 'The Eternal Seal'):
        'Sigillo Eterno',

    # --- :4932-:5032 quattro negozianti e un gatto.
    (4932, "the traveler's food vendor"):
        'il venditore di viveri',
    (4942, 'the interior goods vendor'):
        'il venditore di soprammobili',
    (4951, 'the trader'):
        'il mercante',
    (4961, 'the bakery clerk'):
        "l'aiutante della panetteria",
    (5032, 'white cat'):
        'il gatto bianco',

    # --- :5466-:5478 tre suffissi con sncnv(): la bottega, non il mestiere.
    # ⭐ «Arena delle Bestie» viene da text.hsp:2803
    (5466, 'the barten'):
        'sncnv(cdatan(CDATAN_NAME, rc)) + "del caffè"',
    (5472, 'of arena'):
        'sncnv(cdatan(CDATAN_NAME, rc)) + "dell\'arena"',
    (5478, 'of pet arena'):
        'sncnv(cdatan(CDATAN_NAME, rc)) + "dell\'arena delle bestie"',

    # --- :5839 e :8596 i due «Underground passage».
    # ⚠️ :5839 in giapponese e' 「仮」, un SEGNAPOSTO di sviluppo: qui il
    #    giapponese non aiuta e l'inglese si', che e' il rovescio del lotto
    (5839, 'Underground passage'):
        'Cunicolo',

    (5850, 'Concert hall'):
        'Sala dei concerti',

    # --- :5882-:5900 i tre famigli. 使い魔 e' il FAMIGLIO, non uno schiavo.
    # ⭐ i nomi di bottega vengono da text.hsp:420 e :440
    (5882, 'magic shop slave'):
        'il famiglio della bottega magica',
    (5891, 'general shop slave'):
        'il famiglio della merceria',
    (5900, 'furniture shop slave'):
        'il famiglio del negozio di mobili',

    # --- :5972 l'inglese dice «Eulderna city», il giapponese «presso il palazzo»
    (5972, 'Eulderna city'):
        'Presso il palazzo reale',

    # --- :6524-:7011 i sei piani del Palazzo Infero.
    # ⭐⭐ «palazzo infero» viene da db_creature.hsp, che rende 冥宮の悪鬼
    #     «il demone del palazzo infero»
    (6524, 'LabyrinDeath 1F'):
        'Palazzo Infero - ingresso',
    (6621, 'LabyrinDeath 2F'):
        'Palazzo Infero - livello 2',
    (6718, 'LabyrinDeath 3F'):
        'Palazzo Infero - livello 3',
    (6817, 'LabyrinDeath 4F'):
        'Palazzo Infero - livello 4',
    (6914, 'LabyrinDeath 5F'):
        'Palazzo Infero - livello 5',
    (7011, 'LabyrinDeath 6F'):
        'Palazzo Infero - livello 6',

    # --- :6552 il nome che il gioco tiene nascosto. INVARIATO, dichiarato.
    # ⚠️ il giapponese usa i punti a larghezza intera, l'inglese quelli ASCII:
    #    la resa segue l'inglese, che e' il ramo che sostituisce
    (6552, '????'):
        '????',

    # --- :6590 悪鬼 e' «demone», come in db_creature.hsp
    (6590, 'Area of Curse'):
        'Palmo del Demone',

    (7213, 'Oasis in tower'):
        'Oasi turistica',
    # 💡 «Albedrion» compare una sola volta in TUTTO il codice: nessuna
    #    continuita' da rispettare, vince il giapponese
    (7303, 'Albedrion'):
        'Nave divina dormiente - ponte alto',
    (7362, 'Work area'):
        'Zona di lavoro',
    (7490, 'Ruined city'):
        'Città morta',

    # --- i sei suffissi di citta'. Tutti e sei i nomi erano gia' in text.hsp.
    (7865, ' of Eirel'):
        'cdatan(CDATAN_NAME, rc) + " di Eirel"',
    (8085, ' of Melkawn'):
        'cdatan(CDATAN_NAME, rc) + " di Melkawn"',
    (8236, ' of Kurualm'):
        'cdatan(CDATAN_NAME, rc) + " di Kurualm"',
    (8361, ' of Valm'):
        'cdatan(CDATAN_NAME, rc) + " di Valm"',
    (8671, ' of Arcbelc'):
        'cdatan(CDATAN_NAME, rc) + " di Arcbelc"',
    (8758, ' of Ludus'):
        'cdatan(CDATAN_NAME, rc) + " di Ludus"',

    # --- :7901 l'inglese dice «The Mine», il giapponese «presidio di Eulderna».
    # ⚠️ e «The Mine» era gia' preso da スライムの坑道 nel lotto 002
    (7901, 'The Mine'):
        'Presidio di Eulderna',

    (8004, 'Hill of mushroom'):
        'Collina dei funghi',
    (8017, 'Near the ruins'):
        'Presso le rovine di Suginoko',
    (8133, 'Gambling hall'):
        'Bisca clandestina',
    (8142, 'loser'):
        'il perdente',
    (8306, 'Ninja House'):
        'Casa dei ninja',
    # ⚠️ l'inglese butta via il drago: 九頭竜 e' «a nove teste»
    (8408, 'Deep-Sea Castle'):
        'Castello del Drago a Nove Teste',
    (8443, 'Island in madness'):
        'Arcipelago della Follia',
    (8596, 'Underground passage'):
        'Passaggio sotterraneo',

    # --- :8797 e :8911 i due «basement»: una cantina e un covo di demoni.
    (8797, 'basement'):
        'Cantina',
    (8911, 'basement'):
        'Nido del demonio',

    # --- :8809 la chiesa attesa dalla 39a, quando 姉波動 fini' in glossario.md
    # ⭐ «sorella maggiore» e' il registro che text.hsp usa gia' per 姉
    (8809, 'the Church of Older Sister'):
        'Chiesa della Sorella Maggiore',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-map-003.jsonl'
DA, A = 4210, 9000
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\map.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_map.jsonl', encoding='utf-8') if l.strip()]
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
