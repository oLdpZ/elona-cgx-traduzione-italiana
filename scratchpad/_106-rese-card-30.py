# -*- coding: utf-8 -*-
"""106a - Lotto 30 di `db_card.hsp`, e con questo il file CHIUDE: le carte fra la
riga 14601 e la 15075 (21).

ⓘ **Nessuna carta di questo lotto ha l'inglese che finisce con uno spazio.**

ⓘ **Le voci da `:14878` in poi non sono carte di creature**: sono le tessere del
terreno (foresta, montagna, mare, isola, palude, terra morta, pianura, distesa
innevata) e le due carte di sistema (`draw2Card`, `return`). Non hanno prosa, e
`estrai` non le porta in questo lotto: il conteggio di 21 e' giusto.

⚠️ **UNA carta ha l'inglese ROTTO, e la resa viene dal giapponese.** `:14839`
apre con 異常な素早さで彷徨する鐘の魔物 — «un mostro campana che vaga con una
rapidità anomala» — e l'inglese ha **perso la prima frase** e comincia da
`The platinum-coloured ones`. ⓘ La frase c'e' invece nella gemella `:14852`, la
campana d'oro, e le due si scrivono uguali: e' da li' che si vede il buco.

⚠️ **`elite` non si puo' scrivere** (`:14605`): `degrada()` la porta a `e'lite`,
con l'apostrofo dentro la parola. E' la terza volta oggi, dopo «dèi» nel lotto 19
e «élite» nel lotto 23. Reso «il fior fiore».

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `ダルフィ` → **Derphy** (31 volte
nel dizionario), `ルミエスト` → **Lumiest**, `イルヴァ` → **Irva**, `ネフィア` →
**le Nefia**, `リトルシスター` → **<Little Sister>** e `ビッグダディ` →
**<Big Daddy>** (`invariati.md`, e sono le carte `:14748` e `:14761`),
`クイックリング` → **il quickling** (`db_card`), `プラチナ` → **il platino**,
`妖精` → **la fata**, `魔術士ギルド` / `盗賊ギルド` / `戦士ギルド` → **Gilda dei
Maghi / dei Ladri / dei Guerrieri**.

ⓘ **`:14735` cita `クレイモア` e resta Claymore.** Non e' lo spadone (che nel
progetto e' gia' «lo spadone», `db_card:4281`): e' il **soprannome** che le viene
dall'arma che porta, e la carta lo dice cosi'. La creatura si chiama gia' «la
mietitrice dagli occhi d'argento».
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :14605 il purosangue
    (14605, 'The best of the best horses, born after various breedings. Because of their outstanding quality, their name is often used as a synonym for the elite.'):
        "Il cavallo di razza fra i cavalli di razza, nato in fondo a un lungo lavoro di selezione. La qualità che ha è tanto fuori dal comune che spesso il suo nome si usa per dire il fior fiore di qualunque cosa.",

    # ---------------------------------------------------------- :14618 il mutante
    (14618, 'A strange creature created in ancient times by mixing the genes of several creatures. Its continuously active cells transform its body as it grows.'):
        "Una creatura strana, fabbricata nell'antichità mescolando i geni di parecchi esseri viventi. Le cellule restano sempre attive e, mentre cresce, gli deformano il corpo.",

    # ---------------------------------------------------------- :14631 <Icolle> il biochimico
    (14631, 'He is a reputed weirdo in the neighbourhood. But his brain is unquestionably genius, and although he specialises in biochemistry, he has managed to recreate and mass produce a genetic complex device that is a legacy of previous civilisations.'):
        "Nel vicinato ha fama di essere un tipo strano. Ma la sua testa è geniale, e non c'è da discutere: pur essendo specialista di biochimica è arrivato a riprodurre, e a produrre in serie, l'apparecchio che combina i geni, lascito della civiltà di prima.",

    # ---------------------------------------------------------- :14644 <Balzak> il custode
    (14644, 'A cleaner who is obsessed with keeping Lumiest looking beautiful. He is troubled by the fact that his title of cleaner is sometimes mistaken for that of an assassin. In his opinion, those who litter are worth less than the rubbish they litter.'):
        "Un netturbino che si consuma per tenere bello l'aspetto di Lumiest. Gli dispiace che il suo mestiere, il ripulitore, qualcuno lo scambi per quello del sicario. A sentir lui, chi butta i rifiuti per terra vale meno dei rifiuti che butta.",

    # ---------------------------------------------------------- :14657 <Revlus> il maestro della Gilda dei Maghi
    (14657, "A young and powerful man who governs the Mages' Guild. He spends his days deciphering grimoires. He is troubled by the recent discovery that the magic bookshop is being used by other guild members without his permission."):
        "Un giovane di valore, che governa la Gilda dei Maghi. Passa le giornate a decifrare i libri di magia. Di recente ha scoperto che la libreria magica se la usano senza permesso anche quelli delle altre gilde, e la cosa lo tormenta.",

    # ---------------------------------------------------------- :14670 <Lexus> il guardiano della Gilda dei Maghi
    (14670, "He works as a gatekeeper for the Mages' Guild and gives assignments to subscribers. He is sometimes teleported despite the fact that his equipment is not cursed and is questioned."):
        "Fa il guardiano della porta della Gilda dei Maghi e assegna le prove a chi si iscrive. Ogni tanto si ritrova teletrasportato pur non avendo addosso niente di maledetto, e la cosa lo lascia perplesso.",

    # ---------------------------------------------------------- :14683 <Sin> il maestro della Gilda dei Ladri
    (14683, "He is the head of the Thieves' Guild, which is still the darkest part of the criminal town of Derphy. His heart has been betrayed and betrayed again and again, and his mind has become closed to the darkness and he no longer trusts people."):
        "Il capo che tiene insieme la Gilda dei Ladri, che perfino a Derphy, città di criminali, resta il posto più oscuro. A furia di tradire ed essere tradito il suo cuore si è chiuso nel buio, e non riesce più a fidarsi di nessuno.",

    # ---------------------------------------------------------- :14696 <Abyss> il guardiano della Gilda dei Ladri
    (14696, "Keeper of the Thieves' Guild, who guards the staircase leading to the basement in Derphy's tavern. He intends to be on constant alert, but is often in the wrong place at the wrong time."):
        "Il guardiano della Gilda dei Ladri, che sorveglia la scala che dalla taverna di Derphy scende nel sotterraneo. Nelle sue intenzioni non abbassa mai la guardia, ma capita spesso che, senza accorgersene, si ritrovi da tutt'altra parte.",

    # ---------------------------------------------------------- :14709 <Fray> la maestra della Gilda dei Guerrieri
    (14709, 'A beautiful swordsman who is the head of the Warrior Guild. Many people join the guild for her, but she is unaware of this as she has no interest in anything other than wielding a sword.'):
        "Una bella spadaccina, che fa da capo alla Gilda dei Guerrieri. Non sono pochi quelli che si iscrivono alla gilda per lei, ma a parte menare la spada niente le interessa, e quindi non se n'è accorta.",

    # ---------------------------------------------------------- :14722 <Doria> il guardiano della Gilda dei Guerrieri
    (14722, 'He works as a gatekeeper for the Warrior Guild and gives assignments to subscribers. Frequent teleportation situations occur without his knowledge, and it has recently become difficult for him to return to his position each time.'):
        "Fa il guardiano della porta della Gilda dei Guerrieri e assegna le prove a chi si iscrive. Gli capita di continuo di ritrovarsi teletrasportato senza saperlo, e ultimamente tornare ogni volta al proprio posto ha cominciato a pesargli.",

    # ---------------------------------------------------------- :14735 la mietitrice dagli occhi d'argento
    (14735, 'Warriors who have been implanted with demons in order to defeat them, and who have acquired very good physical abilities. She is sometimes called Claymore because of the weapon she carries.'):
        "Una guerriera a cui, per battere il demoniaco, hanno innestato addosso il demoniaco, e che ne ha ricavato doti fisiche fuori dal comune. Dall'arma che porta le viene anche il soprannome di Claymore.",

    # ---------------------------------------------------------- :14748 <Big Daddy>
    (14748, 'He lives in hiding in Nefia, using his body as a shield to protect his Little Sister, who is hunted by those who seek his power. He has no mercy for those who threaten his little angels.'):
        "Vive nascosto nelle Nefia, e fa del proprio corpo uno scudo per proteggere la <Little Sister>, che chi cerca il potere insegue senza tregua. Con chi minaccia il suo piccolo angelo non usa nessuna pietà.",

    # ---------------------------------------------------------- :14761 <Little Sister>
    (14761, 'The energy he stores in his body is targeted by many forces. For this reason, she hides out in Nefia, protected by Big Daddy, with whom she has a symbiotic relationship.'):
        "L'energia che tiene accumulata in corpo è nel mirino di molte fazioni. Per questo se ne sta nascosta nelle Nefia, protetta dal <Big Daddy>, con cui vive in simbiosi.",

    # ---------------------------------------------------------- :14774 la scienziata misteriosa
    (14774, 'A female scientist who devotes her life to protecting Little Sisters. What she is trying to protect, what happened in her past and what on earth she is researching are all mysteries.'):
        "Una donna di scienza che dedica tutta la vita a proteggere le <Little Sister>. Con che cosa in testa le protegga, che cosa ci sia stato nel suo passato, che cosa diamine stia studiando: tutto è un mistero.",

    # ---------------------------------------------------------- :14787 <Misterioso Produttore>
    (14787, 'A mysterious man who travels to gather candidates to produce an idol that will make Irva go crazy. When he sees an attractive person, he has a bad habit of making a move on them, regardless of gender.'):
        "Un uomo misterioso che gira il mondo per raccogliere le candidate con cui produrre l'idolo che manderà in delirio Irva. Quando vede una persona attraente ha il brutto vizio di allungare le mani, uomo o donna che sia.",

    # ---------------------------------------------------------- :14800 l'ombra
    (14800, "A shadow of some creature that has awakened to its own consciousness and swallowed the original creature. In ancient times, it was believed to have been transformed by a fairy's mischief."):
        "L'ombra di un essere vivente qualunque che si è destata a una coscienza propria e ha inghiottito l'essere da cui veniva. Un tempo si credeva che a cambiarle forma fosse stato il dispetto di una fata.",

    # ---------------------------------------------------------- :14813 il quickling
    (14813, 'A type of gnome that lives in seclusion in unpopular places. They are very quick but very vulnerable. Overhunting is a concern, as their flesh can make the people who eat them very fast.'):
        "Una specie di piccolo essere che vive ritirato nei posti dove non passa nessuno. È svelto da non credere, ma anche fragilissimo. La sua carne rende svelto anche chi la mangia, e si teme che lo si cacci troppo.",

    # ---------------------------------------------------------- :14826 il quickling arciere
    (14826, 'Brave quicklings who take up their bows and stand up to defend their countrymen who are in danger of extinction. Many are shattered by their unusually fast hail of arrows.'):
        "Un quickling coraggioso, che ha preso l'arco e affronta il nemico per difendere i suoi, ormai sull'orlo dell'estinzione. Sono in tanti a finire ridotti in pezzi da quella grandinata di frecce di una rapidità anomala.",

    # ---------------------------------------------------------- :14839 la campana di platino
    (14839, 'The platinum-coloured ones have bodies made of platinum and have a habit of mistaking platinum coins for their friends and trying to protect them.'):
        "Un mostro campana che vaga con una rapidità anomala. Quelle color platino hanno il corpo fatto di platino, e hanno l'abitudine di scambiare le monete di platino per compagne e di provare a proteggerle.",

    # ---------------------------------------------------------- :14852 la campana d'oro
    (14852, 'A bell monster that wanders with abnormal speed. The golden ones love money. They disappear in the blink of an eye to protect their wealth.'):
        "Un mostro campana che vaga con una rapidità anomala. Quelle color oro vanno matte per il denaro. Per difendere il proprio patrimonio spariscono in un batter d'occhio.",

    # ---------------------------------------------------------- :14865 l'alieno
    (14865, 'An alien organism that lurks in wells and invades from the lifeline direction. Has acidic body fluids. The theory that they are merely sentinels of a higher invader is supported by recent observation data.'):
        "Un essere di un altro pianeta, che si annida nei pozzi e invade passando per le condutture. Ha liquidi corporei acidi. La teoria che sia soltanto l'avanguardia di un invasore ben più alto è, per i dati raccolti di recente, la più accreditata.",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-030.jsonl'
DA, A = 14601, 15075
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_card.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_102-dacard.jsonl', encoding='utf-8') if l.strip()]
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

# rete 6: righe spente, col `;` (lotto 006), col `//` (100a) o dentro un
# blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
# ⚠️ Lo strumento, non lo scratch: `strumenti/commenti.py` e' la stessa funzione
# di `scratchpad/commenti-blocco.py` ma con dei test, e dalla 100a sa anche del
# commento di riga `//`.
from strumenti import commenti as _cb
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    testo = sorgente[riga - 1]
    return (testo.lstrip().startswith(';')
            or _cb.lang_spenta_da_barre(testo)
            or riga in SPENTE)


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _testa = sorgente[_righe[0] - 1]
        if _testa.lstrip().startswith(';'):
            _come = "e' commentata nel sorgente"
        elif _cb.lang_spenta_da_barre(_testa):
            _come = "e' spenta da un commento `//`"
        else:
            _come = 'sta dentro un commento di BLOCCO'
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
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
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
