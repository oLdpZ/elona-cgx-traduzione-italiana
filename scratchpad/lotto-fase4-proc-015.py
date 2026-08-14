# -*- coding: utf-8 -*-
"""Lotto fase4-proc-015: il log delle azioni speciali (proc.hsp 12501-14499).

47 rese, nessuna rinviata. `proc.hsp` passa a 660 su 1.098 (60%).

⚠️ **La zona e' quasi tutta log di combattimento**, cioe' la roba che il
giocatore legge a ogni scontro: le mosse di barra delle armi (falce, spada,
pugnale, arco, balestra, pistola, fucile, lancia, bastone, scudo, pugni), i
cannoni, l'acido, il tornado magnetico, e le due coppie corpo/spirito.

⚠️⚠️ **La scoperta del lotto: la rete 4 e la rete 11 si contraddicono.** A
`:12837` e `:13298` il giapponese e' lo **stesso** —
`name(tc) + "は咄嗟に" + name(cc) + "の攻撃を防いだ！"` — ma l'inglese no:
`:13298` nomina tutt'e due i personaggi, `:12837` ne nomina **uno solo**
(`name(cc) + " bluntly prevented the attack!"`). La rete 11 pretende che la resa
porti esattamente le funzioni dell'inglese, quindi a `:12837` un nome solo; la
rete 4 pretende che due siti con lo stesso giapponese dicano le stesse parole, e
con un nome in meno non si puo'. **Le due reti non possono avere ragione
insieme, e la differenza non l'ho scelta io: la impone il sorgente.**
✅ La rete 4 adesso raggruppa per `(giapponese, funzioni di contenuto)` invece
che per il solo giapponese, e stampa un 💡 quando lo stesso giapponese ha due
firme diverse.

💡 **E a `:12837` la resa segue il giapponese, non l'inglese**, perche' puo':
`verifica` accetta ogni chiamata che compaia **in una delle due forme di monte**
(`verifica.py:384`), e `name(tc)` sta nel giapponese. L'inglese qui nomina il
personaggio **sbagliato** — dice che a parare e' `cc`, cioe' chi attacca —
ed e' l'ottavo errore di monte della serie, gemello di `:6200` della 35a.
⚠️ Il nono e' `:14021`: `name(tc)の前面がＮ極になった！` contro
`name(cc) + " became the N pole on the front!"`, e a dare ragione al giapponese
sono le due righe **sotto**, che fanno `cbitmod ... tc`.

💡 **La forma «X attacca, ma Y para» risolve tre siti in un colpo.** Il
giapponese dice «Y ha parato l'attacco **di X**», e il genitivo davanti a
`name()` non esiste (vedi il lotto 014). Girando la frase i due nomi diventano
tutt'e due **soggetti**, e la differenza fra i tre siti resta dove il sorgente
la mette: `:13298` a mani nude, `:12940` con l'arma, `:14282` con lo scudo.

⚠️ **Sei rese sono copie di decisioni gia' prese**: `:12514` («Il corpo e'
bloccato e non si muove!», `proc.hsp:9362`), `:13308` («esita», `action.hsp:288`
e `proc.hsp:8303`), `:13471` e `:13475` (i tappi di pozione, `action.hsp:6545` e
`:9928`), e la forma «Il ... colpisce X e» / «... X.» delle due coppie acido e
tornado, che e' quella di `action.hsp:15364`/`:15367` per il raggio di
particelle.

💡 **Il vocabolario di questa zona viene tutto da `skill.hsp`**, che i giocatori
leggono nel menu: ゲージ -> «barra» (e ゲージ技 -> «mossa di barra», da
`custom_tweaks.hsp:1256`), 超電磁トルネード -> «Tornado magnetico» (`:1816`),
臨界粒子砲 -> «Cannone a particelle» (`:1756`), 肉体復活 -> «Ripristina Corpo»
(`:619`), 精神復活 -> «Ripristina Spirito» (`:624`), 麻痺 -> «paralisi».

⚠️ **`:13389` e le due «In addition» sono i tre siti dove l'accordo rischiava.**
`name(tc) + " " + is(tc) + " paralyzed."` chiederebbe «paralizzato/paralizzata»:
la resa mette la **paralisi come soggetto** e il nome come complemento oggetto.
E `:14434`/`:14454` hanno `his(tc)` e basta, cioe' **zero** funzioni di
contenuto: la resa non puo' nominare nessuno, e dice «il corpo», «lo spirito».
⚠️ Sono anche due dinamiche senza nessuna funzione: vanno fra virgolette, o
scatta la rete 12 nata nel lotto 014.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- il passo dell'ombra
    # copiata da proc.hsp:9362, stesso giapponese
    (12514, 'It cannot move to while binded!'):
        'Il corpo è bloccato e non si muove!',
    (12528, 'you have not set a target.'):
        'Non hai scelto nessun bersaglio.',
    (12542, ' teleport in the shadow and bind .'):
        'name(cc) + " scivola nell\'ombra e immobilizza " '
        '+ cdatan(CDATAN_NAME, tc) + "."',

    # --- i cannoni. 砲弾発射 e' «Colpo di cannone» in skill.hsp:1680
    (12632, ' shot the special cannon.'):
        'name(cc) + " spara un proiettile speciale."',
    (12648, ' shot the nuclear artillery.'):
        'name(cc) + " spara un proiettile nucleare."',

    # --- l'arma lanciata, e la prima delle tre parate
    (12833, ' threw the weapon with a strong spin!'):
        'name(cc) + " scaglia l\'arma con una rotazione violenta!"',
    # ⚠️ un nome solo, ed e' quello del giapponese: l'inglese nomina cc, cioe'
    #    chi attacca, e a parare e' tc. Vedi la nota in cima.
    (12837, ' bluntly prevented the attack!'):
        'name(tc) + " para il colpo al volo!"',

    # --- la barra di potenza. ゲージ -> «barra», ゲージ技 -> «mossa di barra»
    (12886, ' put all of  strength into the next blow!'):
        'name(cc) + " concentra ogni forza nel prossimo colpo!"',
    (12890, ' decide not to put all of  strength into the next blow.'):
        'name(cc) + " stava concentrando le forze nel prossimo colpo, ma ci ripensa."',
    (12899, 'You decide to save your power gauge.'):
        'Decidi di risparmiare le mosse di barra.',
    (12904, 'You decide to use your power gauge aggressively.'):
        'Decidi di usare le mosse di barra senza risparmio.',

    # --- le mosse di barra, arma per arma
    (12933, ' mow  down!'):
        'name(cc) + " falcia " + name(tc) + " con un ampio colpo di falce!"',
    (12940, ' stop  attack with  weapon!'):
        'name(cc) + " attacca, ma " + name(tc) + " para al volo con l\'arma!"',
    (13004, ' slashed  in the blink of an eye!'):
        'name(cc) + " squarcia " + name(tc) + " in un lampo!"',
    (13086, ' hold  weapon overhead in a reverse grip and vigorously stab !'):
        'name(cc) + " impugna l\'arma al rovescio e trafigge " + name(tc) + " con violenza!"',
    (13156, ' drive a heavy slash into !'):
        'name(cc) + " colpisce " + name(tc) + " con un fendente pesantissimo!"',
    (13233, ' shoot a bundle of arrows into the sky!'):
        'name(cc) + " scaglia in cielo un fascio di frecce!"',
    (13239, 'Arrows rain down on  like a waterfall!'):
        '"Una cascata di frecce investe " + name(tc) + "!"',
    (13298, ' fend off  attack!'):
        'name(cc) + " attacca, ma " + name(tc) + " para al volo!"',
    # copiata da action.hsp:288 e proc.hsp:8303, stesso giapponese
    (13308, '  frightened.'):
        'name(tc) + " esita."',
    (13348, ' fire a bundle of bolts at  head!'):
        'name(cc) + " scaglia un fascio di frecce e colpisce " + name(tc) + " alla testa!"',
    # «paralizzato» concorderebbe con tc: la paralisi diventa soggetto
    (13389, '  paralyzed.'):
        '"La paralisi coglie " + name(tc) + "."',
    # copiata da action.hsp:6545
    (13471, 'Potion-charge Lv!!'):
        '"Carica-pozione Lv" + inv(INV_ITEM_LEVEL, cipk) + "!!"',
    # copiata da action.hsp:9928, stesso giapponese
    (13475, ' put potion plugs.[Remaining plug ]'):
        'name(cc) + " carica i tappi di pozione. [Tappi rimasti: " '
        '+ gdata(GDATA_FLAG_TOTAL_POTION_PLUGS) + "]"',
    (13508, ' brace for recoil and fire at !'):
        'name(cc) + " incassa il rinculo e fa fuoco contro " + name(tc) + "!"',
    (13579, ' fire a bullet at  with perfect accuracy!'):
        'name(cc) + " centra " + name(tc) + " con un colpo di precisione assoluta!"',
    # 臨界粒子砲 e' «Cannone a particelle», skill.hsp:1756
    (13652, ' fire a particle beam!'):
        'name(cc) + " scatena un torrente di particelle!"',

    # --- l'acido e il tornado magnetico: la forma e' quella di action.hsp:15364
    (13747, ' send out a blast of acidic wind!'):
        'name(cc) + " libera nel vento una raffica d\'acido!"',
    (13801, 'The acid hits  and'):
        '"L\'acido colpisce " + name(tc) + " e"',
    (13804, 'The acid hits .'):
        '"L\'acido colpisce " + name(tc) + "."',
    # 超電磁トルネード e' «Tornado magnetico», skill.hsp:1816
    (13945, ' gave off tornado of E-Mag energy!'):
        'name(cc) + " scatena un tornado magnetico!"',
    (13999, 'The E-Mag hits  and'):
        '"Il tornado colpisce " + name(tc) + " e"',
    (14002, 'The E-Mag hits .'):
        '"Il tornado colpisce " + name(tc) + "."',
    # ⚠️ l'inglese dice name(cc), il giapponese name(tc), e le due righe sotto
    #    (`cbitmod ... tc`) danno ragione al giapponese. Ｎ極状態 e' «Magnete-N»
    #    nella piastrella di stato (text.hsp:83).
    (14021, ' became the N pole on the front!'):
        'name(tc) + " prende la polarità N sul fronte!"',

    # --- le ultime mosse di barra
    (14055, ' drive a heroic blow into  with all  might!'):
        'name(cc) + " sferra un colpo tremendo e travolge " + name(tc) + "!"',
    (14123, ' aim at one point and pierce !'):
        'name(cc) + " prende la mira su un solo punto e trafigge " + name(tc) + "!"',
    (14200, ' hit  with a furious succession of attacks!'):
        'name(cc) + " investe " + name(tc) + " con una raffica di colpi!"',
    (14278, ' bash  with  shield.'):
        'name(cc) + " prende a scudate " + name(tc) + "."',
    (14282, ' fend off  attack with  shield!'):
        'name(cc) + " attacca, ma " + name(tc) + " para con lo scudo!"',
    (14343, ' unleash the utmost limit of  fighting spirit and pummel !'):
        'name(cc) + " porta la furia al limite e tempesta " + name(tc) + " di colpi!"',

    # --- corpo e spirito. I nomi vengono da skill.hsp:619 e :624.
    # 蝕まれた e' l'erosione di «Res+ erosione» (buff.hsp:919)
    (14427, ' body is damaged.'):
        'name(tc) + " ha il corpo corroso."',
    (14430, ' body is restored.'):
        'name(tc) + " ha il corpo ripristinato."',
    # ⚠️ zero funzioni di contenuto: his(tc) e' morfologia e sparisce, quindi la
    #    resa non puo' nominare nessuno. Ma resta una DINAMICA: virgolette.
    (14434, 'In addition,  body is enhanced.'):
        '"Inoltre il corpo ne esce rafforzato."',
    (14447, ' spirit is damaged.'):
        'name(tc) + " ha lo spirito corroso."',
    (14450, ' spirit is restored.'):
        'name(tc) + " ha lo spirito ripristinato."',
    (14454, 'In addition,  spirit is enhanced.'):
        '"Inoltre lo spirito ne esce rafforzato."',

    # --- il desiderio che non arriva
    (14492, 'The power of the Wish Goddess does not seem to reach here...'):
        'Nemmeno il potere della dea dei desideri arriva fin qui...',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-015.jsonl'
DA, A = 12501, 14499
# ⚠️ il SORGENTE pinnato, non la build: i numeri di riga del dizionario vengono
#    da li'. Vedi il lotto 014.
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\proc.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_proc.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]
voci = [v for v in zona if (v['riga'], v['en']) not in RINVIATE]

errori = []
for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items():
    if n > 1:
        errori.append(f'rete 0: la chiave {k} identifica {n} voci, non una')
indice = {(v['riga'], v['en']): v for v in voci}
for v in voci:
    if (v['riga'], v['en']) not in RESE:
        errori.append(f"rete 1: voce senza resa -> riga {v['riga']}  en={v['en']!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {(v['riga'], v['en']) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: nessuna voce del lotto deve stare su una riga spenta — commentata col
# `;` (lotto 006) o dentro un blocco `/* ... */` (lotto 014).
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
# ⚠️ `valn` solo se viene da un `itemname()`: vedi il lotto 014.
# ⚠️ «con» NON si fonde in italiano moderno e non entra qui: misurato nella 37a
#    passando la rete su tutto il dizionario, dove faceva cinque falsi positivi.
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[(v['riga'], v['en'])]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo, se no si salda alla coda del danno senza respiro (lotto 010).
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].rstrip().endswith(' and'):
        resa = RESE[(v['riga'], v['en'])].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome che dev'essere maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[(v['riga'], v['en'])]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore, non le reti).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[(v['riga'], v['en'])]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO della resa devono essere le stesse
# dell'inglese, nello stesso ordine (verifica.py:367). ⚠️ Solo le DINAMICHE.
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[(v['riga'], v['en'])])
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

# ⚠️ Il confronto fra due rese e' sui LETTERALI di testo, non sull'espressione:
# due siti che dicono le stesse parole su variabili diverse sono la STESSA resa
# (lotto 011 per la rete 4, lotto 014 per la rete 3).
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
    resa = RESE[(v['riga'], v['en'])]
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
# ⚠️⚠️ Raggruppata per (giapponese, FUNZIONI DI CONTENUTO) e non per il solo
# giapponese: nella 37a `:12837` e `:13298` hanno lo stesso giapponese e un
# inglese che nomina un numero diverso di personaggi (uno contro due). La rete 11
# pretende le funzioni dell'inglese, quindi le due rese NON possono dire le
# stesse parole — e la differenza la impone il sorgente, non la traduzione.
# Raggruppare per il solo giapponese faceva litigare le due reti.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v))].add(parole(RESE[(v['riga'], v['en'])]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[(v['riga'], v['en'])]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
