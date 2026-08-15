# -*- coding: utf-8 -*-
"""Lotto fase4-map-005: la fine del mondo, la prigione e le folle del museo
(map.hsp, righe 13000-16000).

49 rese, e **chiude `map.hsp`**: 259 su 260, con la sola `:1396` rinviata
apposta. E' il **diciassettesimo file al 100%** del progetto, e il primo aperto
e chiuso **dentro la stessa sessione** — cinque lotti in una notte.

⭐⭐ **Le sedici battute delle folle del museo stanno su TRE righe sole, e la
chiave lunga non serve.** `:15399`, `:15404` e `:15440` sono tre `chatList`
lunghissime: sei voci sulla prima, sei sulla seconda, cinque sulla terza. La
chiave `(riga, en)` regge lo stesso perche' i sedici inglesi sono **tutti
diversi** — e' il caso che la 41a temeva quando ha inventato la chiave lunga, e
qui si vede il confine: **tante voci sulla stessa riga non bastano**, servono
due voci con lo **stesso inglese** sulla stessa riga.

⚠️⚠️ **Ma un giapponese si ripete fra due righe, e la resa dev'essere una
sola.** 「何だろう、これは」 sta a `:15399` e a `:15440`, e l'inglese lo scrive in
due modi — «What's this?» e «Oh what's this?» — perche' e' la stessa curiosita'
in due folle diverse. ✅ «Che cos'è questo?» tutt'e due le volte: lo impone la
rete 4, ed e' il rovescio della rete 13 che la 39a aveva gia' incontrato
(「パワーゲージが足りない。」 con due inglesi).
⚠️⚠️ **E il brusio ha corretto la 41a: gli spazi fanno parte della resa.**
「 *ざわざわ* 」 sta a `:15399` come «*noise*» e a `:15440` come « *murmur* », e
il primo giro aveva copiato gli spazi **dal sito** — senza la prima volta, con
la seconda — seguendo alla lettera la lezione di クスクス della 41a: «gli spazi
attorno li mette il sito, copiando il suo inglese».
✅ **La rete 4 ha fermato il lotto**, e ha ragione lei: lo stesso giapponese non
puo' avere due rese, e la spaziatura ne fa parte. Vince quella che
`db_creature.hsp:99492` aveva gia' scritto — « *brusio* », **con** gli spazi,
come il giapponese, che li porta in tutt'e due i siti.
💡 **Quindi la formula della 41a va stretta**: gli spazi li mette il **giapponese**,
non il sito inglese. Nel caso di クスクス le tre rese stavano in tre **file
diversi**, e la rete 4 non le ha mai messe a confronto; qui stanno nello stesso
lotto e il confronto scatta. La regola vera e' che la resa e' una sola, spazi
compresi, e a dirlo non e' stato un ragionamento ma una guardia.

⚠️ **L'inglese di questa zona sbaglia bersaglio quattro volte, e due sono
grosse.**
- `:14956` in giapponese e' un **grido**: 「奮い立て！ロスリアの理想のために命を
  賭けよ！」, «coraggio, giocatevi la vita per l'ideale di Lothria!». L'inglese ci
  mette **«Soldiers morale went up.»**, cioe' la *conseguenza* raccontata da
  fuori invece della battuta. ✅ Seguito il giapponese: e' una voce che si sente
  sul campo, non una riga di statistiche;
- `:15404` 「かわ、いー♪」 e' «cariiino♪» spezzato in due dalla virgola, e
  l'inglese scrive **«Scut!»**, che non vuol dire niente di simile;
- `:15404` 「今日はとことん見るぜ」 e' «oggi me li guardo tutti quanti» e l'inglese
  scrive «Absolutely amazing.»;
- `:15440` 「お買い物♪」 e' «che bello fare compere♪» e l'inglese scrive
  «I'm just watching», che dice il contrario.
💡 Sono quattro battute di folla, cioe' il posto dove un traduttore inglese si
sente piu' libero. Il progetto segue il giapponese, come dal Gioco delle Ombre
della 39a.

⭐ **La rete 13 chiude il file con la settima gridata**, e stavolta sono due
cose che si somigliano solo nella traduzione: `:14770` e' 「熱い！」, «che
caldo!», e `:14979` e' 「熱風が吹き抜けた！」, «una folata rovente ha spazzato
tutto!». L'inglese le appiattisce tutt'e due su «It's hot!».
💡 Con questa, `map.hsp` chiude con **sette** appiattimenti di toponimi e frasi
in un file solo. Non e' sciatteria isolata: e' il modo in cui quel file e' stato
tradotto in inglese.

💡 **Cinque nomi propri erano gia' fissati e non ho deciso niente**:
`<Karavika>`, `<Leiki>`, `Opatos`, `Mani`, `Ehekatl`. ⭐ E **ロスリア e'
«Lothria»**, che sta in `db_creature.hsp` («l'agente speciale di Lothria») e non
si sarebbe indovinato: la traslitterazione diretta darebbe «Rosria».
⚠️ 信者 e' «**fedele**», non «Fanatic»: l'inglese carica una parola che il
giapponese non carica, e i tre seguaci degli dei non sono fanatici.

💡 **Il modello della battuta attribuita c'era gia'**: `db_creature.hsp` scrive
`Ehekatl: \\"Mi hai chiamata? Mi hai chiamata?\\"` con le virgolette **con
l'escape**, ed e' la forma che `:15070` (`<Leiki>`) e `:15263` (il messaggero)
copiano.

💡 **Tre participi girati**, tutti sul giocatore: «Ti sei pentito» (`:15341`)
✅ «Hai espiato le tue colpe»; «Vorrei farmi impagliare anch'io…» (`:15399`), che
resta all'infinito apposta; e «Che bel…lezza♪» (`:15404`) invece di «te…nero»,
che avrebbe concordato con quel che sta in vetrina.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :14770 e :14979 ⚠️ rete 13: «It's hot!» per due cose diverse.
    (14770, "It's hot!"):
        'Che caldo!',
    (14979, "It's hot!"):
        'Una folata rovente ha spazzato tutto!',

    (14783, 'Something falls through the sky!'):
        'Qualcosa è caduto squarciando il cielo!',
    (14786, 'A rods from God is swung down!'):
        'Il bastone del dio si è abbattuto sulla terra!',

    # --- :14821 ⭐ copiata: proc.hsp:6481 e text.hsp:13 hanno la stessa riga
    (14821, ' guarded .'):
        'name(tc) + " protegge " + name(cdata(CDATA_TAGTEAM_PARTNER, tc)) + "."',

    (14836, 'Nerve gas was released!'):
        'Si è diffuso del gas nervino!',
    (14904, 'Rebel magicians were fueled by revenge.'):
        'I maghi nemici sono stati accesi dalla sete di vendetta.',

    # --- :14918 e :14936 i disturbatori di distorsione.
    (14918, 'Distortion jammers'):
        "L'interferenza spaziale del demonio è cominciata.",
    (14936, 'Distortion jammer was activated.'):
        '...Pare che il disturbatore D l\'abbia attenuata.',

    # --- :14956 ⚠️ il giapponese e' un GRIDO, l'inglese ne racconta l'effetto.
    # ⭐ ロスリア e' «Lothria», da db_creature.hsp: non si sarebbe indovinato
    (14956, 'Soldiers morale went up.'):
        "Coraggio! Giocatevi la vita per l'ideale di Lothria!",

    # --- :14992-:15022 le tre reazioni della Nefia.
    (14992, 'Nefia released an electrical discharge!'):
        'La Nefia ha emesso una scarica elettrica!',
    (15007, 'Nefia released deadly poison!'):
        'La Nefia ha sputato un veleno micidiale!',
    (15022, 'Nefia generated gravity!'):
        'La Nefia ha generato una stretta di gravità!',

    (15042, 'A horrifying call rings in your head...'):
        'Nella tua testa risuona un richiamo orribile...',
    # ⭐ «<Leiki>» e le virgolette con l'escape: forma gia' usata in db_creature
    (15070, 'Leiki says: \\"If you go any further your mind will break! I\'m getting you out!\\"'):
        '<Leiki>: \\"Oltre non si può, la mente si spezzerebbe! Ti tiro fuori io!\\"',
    (15086, 'Ether corrupts your body...'):
        "L'etere ti corrode il corpo...",

    # --- :15212-:15220 lo stalker. ⭐ «<Karavika>» era gia' fissato
    (15212, 'Stalker of Karavika'):
        'lo stalker di <Karavika>',
    (15220, '<Stalker of Karavika>'):
        '<Lo stalker di Karavika>',

    (15263, 'The messenger says: \\"The retreat of our army is over now. You don\'t need to '
            'fight them any more. Please leave at once!\\"'):
        'Il messaggero: \\"La ritirata del nostro esercito è completa! Non serve più '
        'combatterli. Andatevene subito!\\"',
    (15265, 'Suddenly, stairs appear.'):
        'Sono comparse delle scale.',

    # --- :15341-:15355 la prigione.
    # ⚠️ «ti sei pentito» concorderebbe
    (15341, 'You repent of your sin.'):
        'Hai espiato le tue colpe.',
    (15353, 'You hear footsteps coming towards your cell.'):
        'Senti i passi di una guardia avvicinarsi alla cella.',
    (15354, 'Hey punk, our boss says you can leave the jail now. Do not come back, okay?'):
        'Ehi, tu. Il capo dice che puoi uscire. Non tornare, chiaro?',
    (15355, 'A guard unenthusiastically unlocks your cell.'):
        'La guardia apre la porta della cella, svogliata.',

    # --- :15367-:15390 il rifugio.
    (15367, 'You eat stored food.'):
        'Mangi le scorte di cibo del rifugio.',
    (15375, 'You drink some beverages stored in the shelter.'):
        'Bevi le scorte di bevande del rifugio.',
    (15390, "You don't need to stay in the shelter any longer."):
        "Non c'è più bisogno di restare nel rifugio.",

    # --- :15399 la prima folla del museo: sei voci sulla stessa riga.
    # ⚠️⚠️ gli spazi fanno parte della resa, e a stabilirlo e' la RETE 4.
    #    Il primo giro scriveva «*brusio*» qui (copiando «*noise*», che spazi
    #    non ne ha) e « *brusio* » a :15440 (copiando « *murmur* »): la rete 4
    #    ha fermato il lotto, perche' lo stesso giapponese ' *ざわざわ* ' non
    #    puo' avere due rese. ✅ Vince quella di db_creature.hsp:99492, che ha
    #    gli spazi — come il giapponese, che li ha in tutt'e due i siti.
    (15399, '*noise*'):
        ' *brusio* ',
    (15399, 'Hmm. Not bad.'):
        'Hmm... niente male.',
    # ⚠️ stesso giapponese di :15440: la resa dev'essere UNA (rete 4)
    (15399, "What's this?"):
        'Che cos\'è questo?',
    (15399, 'Ohh...'):
        'Ohhh...',
    # ⚠️ «impagliato» concorderebbe: resta all'infinito
    (15399, 'I want to be stuffed...'):
        'Vorrei farmi impagliare anch\'io...',
    (15399, 'So this is the famous...'):
        'Allora è questo il posto di cui si parla...',

    # --- :15404 la seconda folla, quella disgustata.
    (15404, '*murmur*'):
        '*vocio*',
    (15404, 'Gross! Disgusting.'):
        'Che schifo! Fa senso.',
    (15404, 'Hey. Is it really dead?'):
        'Ehi, ehi, ma questo è morto davvero?',
    # ⚠️ l'inglese scrive «Scut!», che non vuol dire niente: il giapponese dice
    #    «cariiino♪». «te...nero» concorderebbe con quel che sta in vetrina
    (15404, 'Scut!'):
        'Che bel...lezza♪',
    # ⚠️ l'inglese scrive «Absolutely amazing.», il giapponese un'altra cosa
    (15404, 'Absolutely amazing.'):
        'Oggi me li guardo tutti quanti.',
    (15404, 'Can I touch?'):
        'Si può toccare?',

    # --- :15440 la terza folla, quella che compra.
    (15440, ' *murmur* '):
        ' *brusio* ',
    (15440, 'I want this! I want this!'):
        'Lo voglio! Lo voglio!',
    # ⚠️ stesso giapponese di :15399: stessa resa
    (15440, "Oh what's this?"):
        'Che cos\'è questo?',
    # ⚠️ l'inglese dice il contrario del giapponese
    (15440, "I'm just watching"):
        'Che bello fare compere♪',
    (15440, 'My wallet is empty...'):
        'Non mi bastano i soldi...',

    # --- :15502 e :15713 i due venditori ambulanti.
    # 💡 la bottega, non il mestiere; i due giapponesi differiscono per un 屋
    #    che ha tutta l'aria di un refuso di monte
    (15502, 'the street vendor'):
        'sncnv(cdatan(CDATAN_NAME, rc)) + "della bancarella"',
    (15713, 'the street vendor'):
        'sncnv(cdatan(CDATAN_NAME, rc)) + "della bancarella"',

    # --- :15622-:15627 i tre seguaci.
    # ⚠️ 信者 e' «fedele»: l'inglese carica «Fanatic», il giapponese no
    (15622, 'Opatos Fanatic'):
        'il fedele di Opatos',
    (15624, 'Mani Fanatic'):
        'il fedele di Mani',
    (15627, 'Ehekatl Fanatic'):
        'il fedele di Ehekatl',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-map-005.jsonl'
DA, A = 13000, 16000
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
