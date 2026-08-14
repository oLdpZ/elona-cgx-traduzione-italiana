# -*- coding: utf-8 -*-
"""Lotto fase4-ai-001: il sacco da pugni, il pubblico dell'arena, i compagni che
mangiano e bevono, la canzone rumena (ai.hsp, righe 79-1468).

48 rese, ed e' il **primo lotto di `ai.hsp`**, il file dell'intelligenza
artificiale: quel che gli alleati e i nemici fanno e dicono da soli, senza che il
giocatore lo chieda. E' testo di **log ad alta frequenza** — chi ti segue mangia,
beve, contratta col mercante, si medica — e per questo e' entrato prima di
`init.hsp`, che ha piu' firme (133 contro 94) ma si legge quasi tutto nella
scheda del personaggio.

⚠️⚠️ **L'inglese di monte ha rimescolato le battute in DUE punti, ed e' una
famiglia nuova.** Con `:406` qui sotto la serie degli errori di monte passa da
trentasei a **trentanove**. Non e' la famiglia del
«personaggio sbagliato» ne' quella della «riga ricopiata»: qui l'ordine dei
`lang()` sulla stessa riga e' giusto, ma le coppie giapponese-inglese **non si
corrispondono**.

- `:472` e' il blocco del **sacco da pugni** (`CHARA_BIT_SANDBAG`), e il
  giapponese lo dice: 「もっとぶって」 e' «picchiami ancora», la battuta del
  masochista che ti ha chiesto lui di essere preso a pugni. L'inglese ci mette
  «`Release me now.`», che e' la battuta del **prigioniero** di `:482` dieci
  righe piu' sotto, e sposta «`Hit me!`» sulla terza, dove il giapponese dice
  「何をする」, «ma che fai?». Due battute su tre finite sulla riga sbagliata;
- `:658` e' il **pubblico dell'arena**, e le ultime due sono scambiate:
  「頑張って！」 («forza!») porta «`Use your brain!`» e 「頭を使えよ」 («usa la
  testa») porta «`Good fighting.`».

✅ Rese tutte sul giapponese, che e' la regola del progetto dal lotto 019 della
38a — *si copia sul giapponese, mai sull'inglese*.

⚠️ **`:406` e' un «personaggio sbagliato» in piena regola**: il giapponese dice
`name(cc)` e l'inglese `name(tc)`, e il codice sta col giapponese — le tre righe
sopra (`snd`, `animeload 8, cc`) e le quattro sorelle `:381`-`:399` parlano tutte
di `cc`. ✅ La resa usa `name(cc)`, che `verifica` accetta perche' l'argomento
viene da **uno dei due rami di monte**, non per forza dall'inglese.

⭐ **Tre rese erano gia' decise altrove, e `dossier.py` ne ha pescata una per
giapponese intero**: `:865` («キットを使い…応急手当») e' parola per parola
`action.hsp:11146`, e la resa e' **copiata** — «ha usato il kit di pronto
soccorso». Le altre due sono termini, non frasi, e il dossier non le vede: la
ふかふかパン e' il **«pane soffice»** di `db_item.hsp:141763`, e la パートナー
della tag-team e' il **«compagno di coppia»** di `action.hsp:1024`-`:1889`. E' la
lezione del lotto 005 della 40a: il dossier prende le frasi intere e manca i
termini annegati.

⚠️ **`he(cc, 1)` e' contenuto e va conservato, e in italiano dice «lui»/«lei».**
`:381` e' l'unica voce del lotto che lo porta (`init.hsp:1819`-`:1838`, gia'
tradotto): il ramo con **due** argomenti passa da `lang()`, quello a un argomento
no. La resa se lo tiene dentro la frase — «non ricorda piu' perche' lui
combatte» — perche' la rete 11 lo pretende. ⚠️ E per chi si dichiara maschio o
femmina senza esserlo restituisce «lui?» / «lei?», col punto interrogativo
dentro: e' l'upstream, non la resa.

⚠️⚠️ **Due divergenze nuove e legittime — e la misura ha smentito la previsione,
che e' la cosa piu' utile del lotto.** Erano state annunciate come «`battute
--divergenti` passa da 13 a 15», e invece il referto e' rimasto **13**: quel
comando legge `dizionario/db_creature.hsp.jsonl` **e basta** (`battute.py:143`,
`percorsi.DIZIONARIO / f"{FILE}.jsonl"`), quindi un giapponese reso in due modi
in **due file diversi** non lo vede nessuno. L'unica cosa che l'ha visto e' la
**rete 3 dentro il lotto**, che pero' gira solo mentre si scrive un lotto nuovo e
non e' mai stata passata all'indietro su tutto il dizionario. 💡 E' esattamente
la situazione della rete 8 prima della 37a, quando `rete8_dizionario.py` trovo'
sei rese gia' entrate che stampavano «di il»: **e' il candidato naturale al
prossimo referto**, insieme al `termini.py` della 40a.

Le due divergenze sono lo stesso giapponese reso in due modi perche' i due siti
sono di **tipo** diverso:

- 「痛っ！」 qui e' una **statica** fra virgolette che il personaggio grida
  (`chatc@DP = cc`), «Ahi!»; ad `action.hsp:8778` e' una **dinamica** che
  descrive dal di fuori, «name(tc) + " si contorce dal dolore."»;
- 「いいぞ！」 qui e' il pubblico dell'**arena** che incita, «Cosi' si fa!»; a
  `proc.hsp:850` e' il pubblico di un **concerto**, «Bel pezzo!».

⭐ **La canzone rumena, e la scelta piu' discutibile del lotto.**
`:1452`-`:1468` sono *Dragostea din tei*, e il giapponese non la traduce: la
scrive in **soramimi**, cioe' in parole giapponesi vere che suonano come il
rumeno — 「飲ま飲まイェイ」, «bevi bevi yay», che in Giappone e' il modo in cui la
canzone e' conosciuta. L'inglese ha rinunciato e ha stampato il rumeno vero piu'
il ritornello famoso. ✅ La resa italiana fa quel che ha fatto il giapponese, cioe'
usa la forma con cui la canzone e' conosciuta **qui**: «Numa numa iei!!». E i due
gradini piu' assurdi (`:1456` e `:1460`) fanno il soramimi vero e proprio, cioe'
**parole italiane esistenti che suonano come il rumeno**: «Brie♪ sale♪ pece♪
dai♪» per «Vrei sa pleci dar», «Numera♪ numera♪ ehi!♪» e «Una mano♪ una mano♪
ehi!♪» per «nu ma nu ma iei». La scala dei tre gradini regge come in giapponese:
il primo e' la forma famosa, gli altri due sono sempre piu' scemi.
⚠️ **«Vrei sa pleci dar♪» resta invariato** e va dichiarato in `invariati.md`:
e' un verso in una terza lingua, ed e' il caso di «Ensemble!» e «*Kamikakushi*»
della 38a.

💡 **Le tre coppie di `rnd` sono una scala, non tre righe sparse.** `:1207` e
`:1252` («non resiste e si avvicina al cibo / all'acqua») sono la stessa frase
per i due bisogni, come le sei della sete e della fame di `calculation.hsp`: le
rese sono parallele apposta, cosi' la scala si sente.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- il bambino del caos che dimentica, e il nemico che implora pieta'.
    # ⚠️ l'inglese ha DUE name(): la rete 11 li pretende tutt'e due, e in
    #    italiano il nome si ripete come si ripete in inglese
    (79, ' was frightened and began to ask for forgiveness. Maybe you could talk to  now.'):
        '"La paura travolge " + name(cc) + ", che si mette a implorare pietà. '
        'Vuoi ascoltare " + name(cc) + "?"',
    # ⚠️ he(cc, 1) e' CONTENUTO (due argomenti, init.hsp:1819): dice «lui»/«lei»
    #    e va conservato dentro la frase
    (381, ' forgot the reason why   fighting.'):
        'name(cc) + " non ricorda più perché " + he(cc, 1) + " combatte."',
    (387, ' forgot how to walk.'):
        'name(cc) + " ha dimenticato come si cammina."',
    (393, ' forgot how to breathe.'):
        'name(cc) + " ha dimenticato come si respira."',
    (399, ' forgot  fighting instincts.'):
        'name(cc) + " ha dimenticato l\'istinto della lotta."',
    # ⚠️ personaggio sbagliato: l'inglese dice name(tc), il giapponese e il
    #    codice dicono cc (animeload 8, cc; le quattro sorelle qui sopra)
    (406, ' forgot everything and completely stopped moving....'):
        'name(cc) + " ha dimenticato ogni cosa e non si muove più..."',

    # --- il sacco da pugni (CHARA_BIT_SANDBAG). ⚠️ l'inglese ha rimescolato:
    #     «Release me now.» e' la battuta del prigioniero di :482
    (472, 'Release me now.'):
        'Colpiscimi ancora!',
    (472, "I won't forget this."):
        'Questa non te la perdono!',
    (472, 'Hit me!'):
        'Ma che fai?!',

    # --- il prigioniero in gabbia (CHARA_BIT_LOCKED_UP). ⚠️ la seconda ha lo
    #     stesso giapponese di :472: la rete 4 pretende la stessa resa
    (482, 'Release me now!'):
        'Fammi uscire di qui!',
    (482, "I won't forget this!"):
        'Questa non te la perdono!',
    (482, 'Where are you taking me?'):
        'Dove mi porti?',

    # --- chi si tira dietro al guinzaglio e non ci sta.
    # ⚠️ divergenza dichiarata: action.hsp:8778 ha lo stesso giapponese ma e'
    #    una dinamica che descrive da fuori, qui e' il grido del personaggio
    (522, 'Ouch!'):
        'Ahi!',
    (522, 'Stop it!'):
        'Smettila!',
    (528, ' untangle the leash.'):
        'name(cc) + " si libera dal guinzaglio."',

    # --- il pubblico dell'arena delle bestie.
    # ⚠️ divergenza dichiarata: proc.hsp:850 rende lo stesso giapponese «Bel
    #    pezzo!», ma li' e' il pubblico di un concerto
    (658, 'Come on!'):
        'Così si fa!',
    (658, 'More blood!'):
        'Dagliele!',
    (658, "Beat'em!"):
        'Fallo sanguinare!',
    # ⚠️ le due qui sotto sono scambiate di monte: 頑張って e' «forza!» e
    #    頭を使えよ e' «usa la testa». Rese sul giapponese
    (658, 'Use your brain!'):
        'Forza!',
    (658, 'Wooooo!'):
        'Uooooh!',
    (658, 'Go go!'):
        'Vai!',
    (658, 'Good fighting.'):
        'Usa la testa!',
    (658, 'Yeeee!'):
        'Iiiih!',
    # le due degli evocati, che guardano e basta
    (670, 'Come on!'):
        'Sembra divertente!',
    (670, 'More blood!'):
        'Forza tutti e due!',

    # --- il pronto soccorso. ⭐ copiata da action.hsp:11146, stesso giapponese
    (865, ' used a first aid kit.'):
        'name(cc) + " ha usato il kit di pronto soccorso."',

    # --- i compagni che mangiano e bevono.
    (1009, ' consults your expression and cautiously touches the food.'):
        'name(cc) + " ti scruta in faccia e prende il cibo con timore."',
    # ⚠️ genitivo: «lo zaino di X» non si scrive. Il possesso resta implicito
    (1100, ' searched  bag and find nothing to eat!'):
        'name(cc) + " fruga nello zaino e non trova niente da mangiare!"',
    (1129, ' searched  bag and find nothing to drink!'):
        'name(cc) + " fruga nello zaino e non trova niente da bere!"',
    # ふかふかパン e' il «pane soffice» di db_item.hsp:141763
    (1163, '  frightned by the puff puff bread at  feet.'):
        'name(cc) + " ha paura del pane soffice che ha ai piedi..."',
    # パートナー e' il «compagno di coppia» di action.hsp:1024
    (1191, ' silently watches  partner have a meal.'):
        'name(cc) + " guarda in silenzio il compagno di coppia che mangia..."',
    (1207, " couldn't endure and approached the food."):
        'name(cc) + " non resiste e si avvicina al cibo."',
    (1224, '  gazing at the food with a pained expression.'):
        'name(cc) + " fissa il cibo con occhi struggenti..."',
    (1241, ' salivates to moisten  throat, but remembers something and jumps up trembling.'):
        'name(cc) + " sta per bere, poi si ricorda di qualcosa e trasalisce."',
    (1252, " couldn't endure and approached the water."):
        'name(cc) + " non resiste e si avvicina all\'acqua."',
    # ⚠️ senza kit, ed e' un'altra frase: qui il codice cura hp, mp e sp da solo
    (1326, ' administered first aid.'):
        'name(cc) + " si medica alla meglio."',

    # --- Dragostea din tei, primo gradino: la forma con cui la canzone e'
    #     conosciuta in Italia. ⚠️ il verso rumeno resta invariato
    (1452, 'Vrei sa pleci dar♪'):
        'Vrei sa pleci dar♪',
    (1452, 'Numa numa yay!!'):
        'Numa numa iei!!',
    (1452, 'Numa numa numa yay!!'):
        'Numa numa numa iei!!',

    # --- secondo gradino: il soramimi, parole italiane vere che suonano come
    #     il rumeno, come fa il giapponese
    (1456, 'Vrei sa pleci dar♪'):
        'Brie♪ sale♪ pece♪ dai♪',
    (1456, 'Numa numa yay!!'):
        'Numera♪ numera♪ ehi!♪',
    (1456, 'Numa numa numa yay!!'):
        'Numera♪ numera♪ numera♪ ehi!♪',

    # --- terzo gradino, il piu' scemo dei tre
    (1460, 'Numa numa yay!!'):
        'Una mano♪ una mano♪ ehi!♪',
    (1460, 'Numa numa numa yay!!'):
        'Una mano♪ una mano♪ una mano♪ ehi!♪',

    # --- il fischiettio e il ritornello vero.
    (1465, ' *whistle-whistle* '):
        ' *fiuu-fiuu* ',
    (1468, 'Mai-Ya-Hi♪'):
        'Mai-a-hi♪',
    (1468, 'Mai-Ya-Hoo♪'):
        'Mai-a-hu♪',
    (1468, 'Mai-Ya-Ha Ma Mi A♪'):
        'Mai-a-ho♪',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-ai-001.jsonl'
DA, A = 0, 1499
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\ai.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_ai.jsonl', encoding='utf-8') if l.strip()]
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
