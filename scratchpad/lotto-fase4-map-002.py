# -*- coding: utf-8 -*-
"""Lotto fase4-map-002: i nomi delle mappe, i negozianti e i quattordici
Meshera che l'inglese chiamava tutti «tester» (map.hsp, righe 1858-4210).

64 rese, zero rinviate. E' il **secondo lotto piu' grosso del progetto** dopo le
68 del `chara_func-003`, e la percentuale di lavoro gia' deciso altrove e' alta:
diciannove voci avevano l'inglese gia' reso e sei il giapponese.

⭐⭐ **Il mestiere del negoziante non si traduce: si traduce la BOTTEGA, e la
regola c'era gia' in `text.hsp`.** L'inglese fa «Gilbert the baker» con
`sncnv()`, che prende la prima parola del nome (`text.hsp:417`:
`strmid(arg, 0, instr(arg, 0, " ")) + " "`). Il primo giro di questo lotto
scriveva «il tintore», «lo stalliere», «il ricettatore» — e sarebbe stato un
errore, perche' **meta' dei negozianti di Elona sono femmine**.
✅ `text.hsp:420`-`:460` aveva gia' risolto per undici mestieri, e la soluzione
e' il **giapponese**: 「パン屋の」 e' «**della panetteria**», 「宿屋の」 e'
«**della locanda**», 「武具店の」 e' «**dell'armeria**». Il nome del negozio ha
un genere fisso suo, e chi ci lavora resta senza genere.
💡 E' la strada del «nome di genere fisso» della 40a — «pelle», «corpo», «aria»,
«Balia delle bestie» — trovata pero' **gia' fatta**: bastava guardare la
famiglia `sn*` invece di inventare. Le sei nuove seguono: «della tintoria»,
«del negozio di souvenir», «della bottega dei ladri», «della bottega dei
grimori», «della stalla», «del banco ambulante».

⭐⭐ **E i quattordici «tester» sono la perdita d'informazione piu' grossa che il
progetto abbia contato.** `:1864`-`:1903` sono quattordici
`cdatan(CDATAN_NAME, rc) = lang("メシェーラ・<nome>", "tester")`: il giapponese
da' a ciascuno un **nome proprio** — キガツ, クトワ, タシハ, メシエ… — e
l'inglese scrive **quattordici volte la stessa parola**. Non e' un errore di
traduzione, e' un elenco buttato via.
✅ La strada era gia' battuta, e la batte `db_creature.hsp` sullo **stesso
mostro**: メシェーラ・ヴィム e' «il Meshera Vim» dove l'inglese diceva solo
«meshera delta», メシェーラ・アーギン e' «il Meshera Argin» per «meshera gamma»,
メシェーラ・ヘルグムト e' «il Meshera Hergmut» per «meshera beta». Il progetto
**restituisce il nome** ogni volta che l'inglese lo sostituisce con
un'etichetta, e qui lo fa altre quattordici volte.
⚠️ **Non e' «aggiungere quel che l'inglese non dice»**, che e' vietato dalla
41a: quel divieto riguarda le **funzioni di contenuto** — se l'inglese non ha
`name()`, la resa non puo' nominare il soggetto — e qui non c'e' nessuna
funzione, c'e' un letterale che dice una cosa in giapponese e un'altra in
inglese. Su quelli il progetto decide **sul giapponese** da sempre: il Gioco
delle Ombre contro «a card game», Irva contro Tyris.
💡 E il conto torna col vicino: `:4189`, `:4195` e `:4201` sono tre Meshera che
l'inglese **nomina** — «meshera Gilk», «meshera Hermana», «meshera Raimond». Tre
nominati e quattordici no, nello stesso file. Li' l'inglese si tiene, perche' un
nome c'e'.
⚠️ `cdatan(CDATAN_NAME)` e' scritto nel salvataggio, quindi i quattordici gia'
generati in una partita in corso restano «tester»: cambiano solo quelli nuovi.
E' il comportamento normale di tutto il bestiario, non un difetto di questo
lotto.

⭐ **La rete 13 grida di nuovo, e per la seconda volta nello stesso file.**
`:3619` e `:3622` hanno tutt'e due «moor», ma il giapponese distingue
メルカ大湿原 — la **grande** palude di Merca, un luogo con un nome — da 湿原, la
palude generica. ✅ «Grande palude di Merca» e «Palude». Nel lotto `001` era
toccato al valico (`:1121`/`:1137`); qui alla palude. **Due appiattimenti di
toponimi nello stesso file** dicono che l'inglese di `map.hsp` e' stato scritto
guardando la funzione, non il posto.

💡 **Nessun genitivo da girare, per una volta, e la ragione e' grammaticale.**
I sette suffissi di citta' — `cdatan(CDATAN_NAME, rc) + " of Derphy"` — in
italiano sono «di Derphy», «di Lumiest», «di Yowyn»: i **nomi propri di citta'
non prendono l'articolo**, quindi la preposizione non si fonde con niente e la
rete 8 non ha nulla da dire. E' il rovescio esatto del lotto `001`, dove
`mapname()` portava l'articolo dentro e sei righe su sei sono state girate.
⚠️ L'unico che non e' un nome nudo e' `:2593`, 「パルミア市街地の」: «del centro
di Palmia», dove l'articolo c'e' ma sta **dentro il letterale**, che e' fisso.

⚠️ **Un titolo che il gioco appiccica a un personaggio non puo' avere un
genere**, e `:2436` e' il caso della 41a in forma nuova: 「謎の奴隷商人」,
«mysterious slave trader». «Mercante» e «commerciante» hanno un genere;
✅ «**Il misterioso schiavista**» no — «schiavista» e' invariabile nella forma,
il gioco ci mette l'articolo maschile e va bene per chiunque. E' la strada di
«Balia delle bestie», ma con un nome che non ha proprio bisogno di scegliere.

⚠️ **La rete 3 grida quattro volte, e sono quattro «stesso giapponese, due
mestieri».** Non sono divergenze: sono lo stesso nome usato per due cose.
- 「盗賊ギルド」, 「魔術士ギルド」 e 「戦士ギルド」 sono il nome della **mappa**
  qui (`mdatan(MDATAN_NAME)`) e il nome della **creatura** in
  `db_creature.hsp:103826`/`:103737`/`:103915`, dove sono resi «il membro della
  Gilda dei Ladri». ⭐ **E a confermarlo e' l'inglese**, che li' scrive «thief
  guild **member**»: la distinzione che il giapponese non fa la fanno tutte e
  due le altre lingue. La mappa e' «Gilda dei Ladri», chi ci sta dentro e' «il
  membro della Gilda dei Ladri».
- 「ダルフィ」 e' «Derphy» a `text.hsp:747`, dove e' il nome della citta', ed e'
  il **prefisso** di un nome di persona a `:2447`, dove diventa il suffisso
  «di Derphy». Stessa parola, due posizioni nella frase.
💡 E' il caso di 日 del lotto `init-003` e di 「当然だ」 del `map-001`: la rete 3
guarda la stringa, e il mestiere lo decide il sito.

💡 **Quattro nomi copiati senza decidere niente**: «Gilda dei Ladri», «Gilda dei
Maghi» e «Gilda dei Guerrieri» erano gia' in dizionario, e «Covo dei ladri»
viene da `init.hsp:412` del lotto `init-003` — dove pero' l'inglese diceva
«Smuggler's Hideout» e qui dice «Robber's Hideout». Stesso posto, due inglesi.
⚠️ E «Porto Kapul» non e' una scelta: `text.hsp:2743` rende cosi' ポート・カプール,
e `:3271` deve dire lo stesso.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1858 e :3501 i due laboratori di armi biologiche.
    (1858, 'New Test Site'):
        'Nuovo laboratorio biologico',
    (3501, 'Test Site'):
        'Laboratorio biologico',

    # --- :1864-:1903 i QUATTORDICI Meshera che l'inglese chiama tutti «tester».
    # ⭐⭐ il giapponese da' a ognuno un nome proprio; db_creature.hsp fa gia'
    #     cosi' sugli stessi mostri («il Meshera Vim» per «meshera delta»)
    (1864, 'tester'):
        'il Meshera Kigatsu',
    (1867, 'tester'):
        'il Meshera Kutowa',
    (1870, 'tester'):
        'il Meshera Tashiha',
    (1873, 'tester'):
        'il Meshera Meshie',
    (1876, 'tester'):
        'il Meshera Ranisa',
    (1879, 'tester'):
        'il Meshera Retei',
    (1882, 'tester'):
        'il Meshera Tadake',
    (1885, 'tester'):
        'il Meshera Dotoma',
    (1888, 'tester'):
        'il Meshera Ranai',
    (1891, 'tester'):
        'il Meshera Gekitsu',
    (1894, 'tester'):
        'il Meshera Uhaka',
    (1897, 'tester'):
        'il Meshera Nashimu',
    (1900, 'tester'):
        'il Meshera Kotosa',
    (1903, 'tester'):
        'il Meshera Shiteku',

    # --- i sei negozianti nuovi.
    # ⭐⭐ si nomina la BOTTEGA, non il mestiere: «il tintore» darebbe un genere
    #     a chi puo' essere maschio o femmina. text.hsp:420-:460 lo fa gia' per
    #     undici mestieri («della panetteria», «della locanda», «dell'armeria»).
    (2102, 'the dye vendor'):
        'sncnv(cdatan(CDATAN_NAME, rc)) + "della tintoria"',
    (2106, 'the souvenir vendor'):
        'sncnv(cdatan(CDATAN_NAME, rc)) + "del negozio di souvenir"',
    (2504, 'the fence'):
        'sncnv(cdatan(CDATAN_NAME, rc)) + "della bottega dei ladri"',
    (2781, 'the spell writer'):
        'sncnv(cdatan(CDATAN_NAME, rc)) + "della bottega dei grimori"',
    (2964, 'the horse master'):
        'sncnv(cdatan(CDATAN_NAME, rc)) + "della stalla"',
    (3957, 'the wandering vendor'):
        'sncnv(cdatan(CDATAN_NAME, rc)) + "del banco ambulante"',

    # --- i sette suffissi di citta'.
    # 💡 nessun genitivo da girare: i nomi propri di citta' non prendono
    #    l'articolo, quindi «di» non si fonde e la rete 8 non ha niente da dire
    # ⚠️ «Porto Kapul» non e' una scelta: text.hsp:2743 rende cosi'
    (2447, ' of Derphy'):
        'cdatan(CDATAN_NAME, rc) + " di Derphy"',
    (2593, ' of Palmia city'):
        'cdatan(CDATAN_NAME, rc) + " del centro di Palmia"',
    (2734, ' of Lumiest'):
        'cdatan(CDATAN_NAME, rc) + " di Lumiest"',
    (2980, ' of Yowyn'):
        'cdatan(CDATAN_NAME, rc) + " di Yowyn"',
    (3137, ' of Noyel'):
        'cdatan(CDATAN_NAME, rc) + " di Noyel"',
    (3271, ' of Port Kapul'):
        'cdatan(CDATAN_NAME, rc) + " di Porto Kapul"',
    (3441, ' of Vernis'):
        'cdatan(CDATAN_NAME, rc) + " di Vernis"',

    # --- :2436 lo schiavista, e il genere che non deve esserci.
    # ⚠️ «mercante» e «commerciante» hanno un genere; «schiavista» no
    (2436, 'The slave master'):
        'Il misterioso schiavista',

    # --- le tre gilde. ⭐ tutte e tre gia' in dizionario, copiate
    (2481, 'Thieves Guild'):
        'Gilda dei Ladri',
    (2773, 'Mages Guild'):
        'Gilda dei Maghi',
    (3320, 'Fighters Guild'):
        'Gilda dei Guerrieri',

    # --- i luoghi costruiti.
    (2809, 'The Sewer'):
        'Fogne di Lumiest',
    (2867, 'Classroom'):
        'Aula',
    (3019, 'Cat Mansion'):
        'Villa dei gatti di Tam',
    (3032, 'Battle Field'):
        'Linea di difesa',
    (3181, 'Castle of Ice'):
        'Castello di Ghiaccio',
    (3353, 'Doom Ground'):
        'Campo di battaglia',
    (3477, 'The Mine'):
        'Miniera degli slime',
    # ⭐ copiata da init.hsp:412, dove pero' l'inglese diceva «Smuggler's Hideout»
    (3489, "Robber's Hideout"):
        'Covo dei ladri',
    (4112, 'The Depth'):
        'Fondo di Lesimas',
    (4158, 'Hall'):
        'Salone del piano 15',
    (4173, 'Ancient Research Facility'):
        'Antico centro di ricerca',

    # --- i dieci terreni della mappa del mondo.
    # ⭐ «Foresta» e «Mare» erano gia' rese altrove
    # ⚠️ rete 13: :3619 e :3622 hanno lo stesso inglese e due giapponesi
    #    diversi — la grande palude di Merca ha un nome, l'altra no
    (3528, 'Forest'):
        'Foresta',
    (3553, 'Sea'):
        'Mare',
    (3556, 'Grassland'):
        'Prateria',
    (3584, 'Wasteland'):
        'Landa desolata',
    (3597, 'Sand'):
        'Dune',
    (3619, 'moor'):
        'Grande palude di Merca',
    (3622, 'moor'):
        'Palude',
    (3639, 'Seabed'):
        'Fondale marino',
    (3746, 'Plain Field'):
        'Pianura',
    (3812, 'Snow Field'):
        'Distesa innevata',

    # --- le cinque acque costiere e le due navi.
    (4027, 'Kapul coastal'):
        'Acque di Kapul',
    (4039, 'Lumiest coastal'):
        'Acque di Lumiest',
    (4051, 'Kurualm coastal'):
        'Acque di Kurualm',
    (4063, 'Valm coastal'):
        'Acque di Valm',
    (4075, 'Devil coastal'):
        'Acque di Capo Diavolo',
    (4087, 'Merchant ship'):
        'Nave mercantile',
    (4099, 'Pirate ship'):
        'Nave pirata',

    # --- :4189-:4201 i tre Meshera che l'inglese NOMINA.
    # 💡 tre nominati e quattordici no, nello stesso file: qui l'inglese si tiene
    (4189, 'meshera Gilk'):
        'il Meshera Gilk',
    (4195, 'meshera Hermana'):
        'il Meshera Hermana',
    (4201, 'meshera Raimond'):
        'il Meshera Raimond',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-map-002.jsonl'
DA, A = 1858, 4210
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
