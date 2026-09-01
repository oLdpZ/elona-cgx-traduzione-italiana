# -*- coding: utf-8 -*-
"""122a - Lotto 068 di `db_item.hsp`: LE CINTURE, e la categoria CHIUDE.

`FILTER_GIRDLE`, righe da `:61581` a `:126712`: **9 righe**, tutte dell'indice
0, su 9 oggetti. Con questo lotto `FILTER_GIRDLE` va a **0 da fare su 9 vive**,
ed e' la **ventitreesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 068`: **+9** per 9 rese,
nessuna gemella. ⓘ `_code.py 068`: 0 righe senza resa in tabella.
`_forma.py 068`: 9 su 9 con lo spazio prima del `\\n`.

### ⭐⭐ LA QUINTA RIGA DI SEI, E LA RETE ORA LE MOSTRA TUTTE INSIEME

`_122-sorelle-per-frase` trova cinque frasi con una sorella, **quattro gia'
rese**, e sono tutte lo stesso gruppo:

    :100849 (058)  盾    lo scudo      reso
    :101769 (060)  鎧    la corazza    reso
    :99872  (063)  兜    l'elmo        reso
    :101114 (066)  篭手  i guanti      reso
    :100392 (068)  腰当  la cintura    <- questo lotto
    :130450 (---)  靴    gli stivali   l'ultima che resta

⭐ La resa e' stata scritta **leggendo le quattro sorelle nell'uscita della
rete**, non ricordandole. Ieri sarebbe stato un giro di `_cerca.py` a mano, e
tre sessioni fa non sarebbe stato niente.

ⓘ E le due righe della famiglia si commentano a vicenda: l'elmo (`:99872`) dice
che pochi riescono a **coprire i difetti** del materiale, la cintura
(`:100392`) che qui ne hanno **spinto i pregi**, e per questo e' venuta piu'
leggera. Il giapponese le costruisce come una coppia.

### ⭐⭐ L'INGLESE BUTTA LA BATTUTA FINALE DELLE MUTANDE

`:64343`, 《鬼のパンツ》. Il giapponese chiude con **due** esortazioni:

    みんなで穿こう。投げたりしないで穿こう。
    «Mettiamocele tutti. E mettiamocele, invece di tirarle.»

La seconda e' una battuta su un gesto che nel gioco si fa davvero — le mutande
si possono lanciare — e l'inglese la sostituisce con «Put them on, yes, right
now!», che non dice niente. Resa dal giapponese, con tutt'e due le frasi.

⚠️ E nella stessa riga l'inglese aggiunge una parola che il giapponese non ha:
`:126712` dice 婦人, le **signore**, e l'inglese scrive «elderly women». Anche
questa e' resa dal giapponese. Sono due forme della stessa cosa — l'intermedio
che aggiunge e che toglie — e nessuna delle due si vede senza leggere l'originale.

### ⚠️⚠️ UNA DIVERGENZA DEL PROGETTO, TROVATA E NON TOCCATA

`:76049` dice 収穫の神. Nel dizionario quella parola e' gia' resa **due volte**,
tutt'e due al maschile: «il precedente **dio** del raccolto», «nata dal lato del
**dio** del raccolto». Ma 富の神 — nel lotto 066, la catena d'oro — e' reso «la
**dea** della ricchezza», e in gioco quella dea e' Yacatect, che parla al
femminile.

Se i due epiteti indicano la stessa divinita', il progetto le da' due generi.
⚠️ **Non l'ho deciso qui**: questa resa segue la forma gia' nel dizionario per
la parola che ha davanti (収穫の神 -> maschile), perche' cambiare genere a una
divinita' dentro un lotto del corpo e' esattamente il genere di modifica che
nessun conteggio segnala. Va decisa a parte, come la voce «vento di etere» del
lotto 067.
ⓘ Le due righe gia' rese parlano del dio del raccolto **precedente** e di una
divinita' *nata dal suo lato*, quindi e' possibile che non siano Yacatect: la
domanda va guardata, non risolta a occhio.

### ⓘ Le decisioni minori, e da dove vengono

  - ネイン -> «<Nein>», in gioco «<Nein> la strega volante», che parla al
    femminile; 魔石 «pietra magica»; 白虎 «la tigre bianca»; レシマス
    «Lesimas»; パルミア «Palmia»; エウダーナ «Eulderna» — tutti dal dizionario;
  - `:61581`: l'inglese apre con «Giant belt buckle **with an ego**», e
    quell'ego nel giapponese non c'e'. Reso dal giapponese;
  - 得意属性 -> «l'attributo in cui si è forti», e l'indice 3 dello stesso
    oggetto dice gia' «Cambia l'attributo di certe abilità»;
  - `:126712` usa 考案された dove la famiglia della testa, del collo e del
    polso usa 作られた: la resa dice «pensata» dove le altre dicono «fatta».
    La rete non le accosta perche' il verbo cambia, ed e' giusto cosi'.

### ⓘ Il preflight ha segnalato due parole lunghe, e non e' un difetto

`caratteristiche` (15) e `controindicazione` (17). Vale la misura del lotto 063.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :61581
    (61581, "Giant belt buckle with an ego. It emits a light that temporarily transforms one's signature attribute. It is studded with gemstones that resemble eyes, each of which represents a different attribute. Its main body is also in the shape of a giant eye, but it seems that this design was created by chance during the course of its creation. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una cintura con una fibbia enorme. Manda una luce che cambia per un po' l'attributo in cui si è forti. È cosparsa di gemme fatte a somiglianza di occhi, e ognuna governa un attributo diverso. Anche il corpo della fibbia ha la forma di un occhio gigante, ma pare sia venuto così per caso, mentre la costruivano senza pensarci troppo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :64276
    (64276, "This broom was given the ability to fly by Nein. Although it was originally intended to be ridden astride, it is safer to ride it sitting sideways because one's crotch might split open when it soars. It is capable of flying at the speed of sound due to its high specifications, but if it is actually used, the passenger will surely be swept off. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una scopa a cui <Nein> ha dato la facoltà di volare. All'inizio la si pensava da cavalcare a gambe larghe, ma siccome in salita improvvisa c'è il rischio di spaccarsi l'inguine conviene sedercisi sopra di traverso. Ha caratteristiche inutilmente spinte e arriva alla velocità del suono, ma a provarci davvero chi ci sta sopra viene sbalzato giù di sicuro. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :64343
    (64343, 'It was made by sewing tiger fur using magical threads extracted from the souls of mages. They are famous for their toughness and do not tear or stink even after 100 years of wear. Because they are easy to move in, they are used as sportswear, and there are even brand-name products made of white tiger fur. They are pants, but more like hot pants, so there is no need to be embarrassed when people see them. Put them on, yes, right now! \\n# ~Irva Fantasy Encyclopedia~'):
        "Fatte cucendo pelliccia di tigre con un filo magico estratto dall'anima dei maghi. Sono famose per la tenacia, e infatti a portarle cent'anni non si strappano e non prendono odore. Siccome lasciano muoversi bene si usano come abbigliamento sportivo, e ne esiste anche una versione di marca fatta con la pelliccia di tigre bianca. Mutande sì, ma nel senso di pantaloncini, quindi non c'è da vergognarsi se qualcuno le vede. Mettiamocele tutti. E mettiamocele, invece di tirarle. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :68112
    (68112, 'Belt studded with an imitation of the Lesimas Magic Stone. The original magic stone had the power to seal Lesimas, and a plan was proposed to apply it to create a defensive facility to protect Palmia. With the cooperation of adventurers from Eulderna, an imitation was produced, but the plan was abandoned because some of the strength could not be reproduced. Only a prototype of armor that temporarily covered only the bearer with a magical wall was produced. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una cintura cosparsa di imitazioni di pietre magiche. Le pietre magiche originali nascondevano una forza legata al sigillo di Lesimas, e da lì era nato il piano di costruire un impianto difensivo per proteggere Palmia. Con l'aiuto di un avventuriero venuto da Eulderna le imitazioni si riuscirono a produrre, ma una parte della forza non fu riproducibile e il piano si arenò. Di tutto rimase soltanto un prototipo: un'armatura che copre per un momento il solo portatore con un muro magico. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :76049
    (76049, 'Something the God of the Harvest uses to keep his precious objects from escaping. If you are not careful, it will wrap around you like a belt on its own. \\n# ~Irva Fantasy Encyclopedia~'):
        "Quello che il dio del raccolto adopera perché le cose a cui tiene non gli scappino. A distrarsi un attimo, si avvolge addosso da sé come una cintura. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :82342
    (82342, "Waistband made of ancient metals joined together in a scaly pattern. It is coated with a special red chemical that is said to protect the wearer's body and possessions. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una cintura fatta di metallo antico unito a scaglie. Ci è passata sopra una sostanza rossa particolare, e dicono che protegga il corpo di chi la indossa e le cose che porta con sé. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :100327
    (100327, 'A waist support with increased protection by layering. In addition to the increased weight, the overlapping parts collide with each other, which has the adverse effect of creating noise. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una cintura che alza la protezione sovrapponendo strato su strato. Oltre a pesare di più, ha la controindicazione che i pezzi sovrapposti sbattono l'uno contro l'altro e fanno rumore. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100392
    (100392, "A waist brace made of a combination of special materials to provide stronger protection. It is lighter than the usual one, perhaps as a result of the material's advantages. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Una cintura che, incrociando materiali speciali, ha ottenuto una protezione più solida. Forse perché ne hanno spinto i pregi, è venuta più leggera del solito. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :126712
    (126712, 'Protective gear designed to protect the lower half of the body while not impeding action. In cold weather, some elderly women wear these due to their lightweight material. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'armatura pensata per proteggere la parte bassa del corpo senza intralciare i movimenti. Pare che nella stagione fredda certe signore ne portino una fatta di materiale leggero. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 9 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-068.jsonl'
RIGHE = {
    61581, 64276, 64343, 68112, 76049, 82342, 100327, 100392, 126712,
}
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_item.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_107-daitem.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if v['riga'] in RIGHE]
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
