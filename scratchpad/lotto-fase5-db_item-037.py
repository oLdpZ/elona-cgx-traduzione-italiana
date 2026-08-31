# -*- coding: utf-8 -*-
"""115a - Lotto 037 di `db_item.hsp`: GLI ATTREZZI, la coda. LA CATEGORIA SI CHIUDE.

`FILTER_ITEM_TOOL`, righe 90.000 in su: **25 righe** su 21 oggetti — 21
dell'indice 0, nessuna dell'indice 1 e 4 dell'indice 2. Con questo lotto
`FILTER_ITEM_TOOL` passa a **0 da fare su 204 vive**: e' la seconda categoria
chiusa del corpo dopo `FILTER_FURNITURE` (114a), e ci sono voluti cinque lotti,
dal 033 al 037.

⚠️ **La zona non e' un intervallo stretto**: le ultime 25 righe stanno sparse
fra `:90137` e `:122679`, e per prenderle tutte si passa `90000 200000`. Il
numero che `_corpo.py` stampa prima di scrivere e' l'unico modo di saperlo.

### ⭐⭐ TRE FAMIGLIE, E UNA E' UNA FRASE RIPETUTA QUATTRO VOLTE

  - **i quattro attrezzi di mestiere** (`:104791` gemme, `:120505`
    falegnameria, `:120571` cucito, `:122679` alchimia) hanno il giapponese
    identico a meno del mestiere, **seconda frase compresa**:
    当然ながら技術が無ければ扱うことはできない, «va da se' che senza l'abilita'
    non si puo' adoperare». Quattro rese uguali tranne il mestiere;
  - **le due coperte** (`:92934` gelo, `:92998` fuoco) sono la stessa frase con
    l'elemento cambiato, e la stessa chiusa «tutto ha un limite»;
  - **i due dischi** (`:92389` immagini, `:94601` musica) chiudono con la stessa
    frase sulla tecnica dimenticata.

⚠️ **E i due dischi non hanno la stessa spaziatura.** `:92389` mette lo spazio
prima del `\\n`, `:94601` no — due righe gemelle in tutto il resto. Il
preflight l'ha visto; leggendo il dossier non si vedeva.

### ⚠️⚠️ IL TITOLO-FONTE SBAGLIATO DELL'INGLESE ALZA IL CANCELLO A 5

`:102458` (il sacco a pelo) ha per fonte giapponese
～今日から君も冒険者・旅用マニュアル～, il manuale di viaggio. L'inglese ci
mette `~ Great Encyclopedia of North Tyris Furnitures~`, che e' la fonte di
`:88021` (il letto orientale, lotto 036) e di `:92252` (il salvadanaio, qui).

Il cancello «titoli resi in piu' modi» chiava sull'**inglese**, quindi dopo
questo lotto passa da **4 a 5**, e il quinto e'
`~ Great Encyclopedia of North Tyris Furnitures~` -> Enciclopedia dei Mobili /
Manuale di Viaggio. **Annunciato prima di misurarlo**, come il terzo nel 034 e
a differenza del quarto nel 035, che e' arrivato senza preavviso.

ⓘ I cinque sono adesso tutti e cinque appiattimenti o errori **dell'inglese**:
Gavela/Icolle, le Cianfrusaglie, Irva/Aimwell, Extra Issue, e questo. Nessuno e'
una nostra divergenza. Un **6** va guardato.

### ⓘ E l'inglese sbaglia ancora la fonte due volte, senza che nessun cancello lo veda

`:116603` (la corda robusta) porta ～巻かれる為の長いもの～ e l'inglese ci
mette di nuovo `~Battles, Dragons, Swords and Magic~`, come per la frusta e il
guinzaglio del 036. Tre righe, stesso errore di monte, stessa resa nostra:
il cancello non si accende perche' l'inglese e' lo stesso e la resa e' la
stessa. Si vede solo dal giapponese.

### ⭐ LA REGOLA DEL MESTIERE, dove il giapponese cambia parola e l'italiano deve seguirlo

Il giapponese dei quattro attrezzi non dice sempre «attrezzo»: dice ツール
(`:104791`), 道具 (`:120505`), セット (`:120571`), キット (`:122679`). Le rese
seguono — «l'attrezzo di base», «l'attrezzo di base», «il set di base», «il kit
di base» — perche' e' l'unica differenza che il giapponese si e' preso la briga
di fare in quattro righe altrimenti identiche.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :90137
    (90137, 'A board with various drawings detailed on it. It is an excellent tool to use on buildings you own to rearrange your home without wasting muscle power. \\n# ~Supporting Roles on the Streets~'):
        "Una tavola con sopra disegnati per esteso vari progetti. Usata in un edificio di tua proprietà, cambia la disposizione della casa senza sprecare forza nelle braccia: un bell'arnese. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :91909
    (91909, 'People have always lived with fire. With fire we got heat to warm the space, and with fire we got light to illuminate the night. Now you are holding the spark of civilization! \\n# ~an Adventurer is You! Guide for Travels~'):
        "In ogni tempo l'uomo è stato insieme al fuoco. Dal fuoco il calore che scalda lo spazio, dal fuoco la luce che rischiara la notte. E ora la scintilla della civiltà è nelle tue mani! \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :91911
    (91911, '\\"Just by clutching it in one hand, your Nefia life will become much more adventurous. You should definitely try this excellent light-up tool.\\" \\n# ~notice of good store of Vernis~'):
        "\\\"Basta stringerla in una mano e la tua vita nelle Nefia diventa molto più da avventuriero. Prova anche tu questo ottimo arnese per far luce!\\\" \\n# ~Reclame Affissa al Bazar di Vernis~",

    # ---------------------------------------------------------- :92252
    (92252, 'A box that allows you to put a certain amount of money in it every time you use it and keep it. The fact that it gets a little heavier each time it is used is surely due to the happiness of storing it. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una cassetta dove a ogni uso si mette dentro una certa somma e la si tiene da parte. Che a ogni uso si faccia un po' più pesante sarà di sicuro merito della felicità di mettere da parte. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :92389
    (92389, 'Disks containing videos. The use of these disks can bring back past memories in the form of videos, but unfortunately all other techniques have been forgotten today except for their use. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un disco con dentro delle immagini. Usandolo si richiamano in forma di filmato le memorie del passato, ma purtroppo oggi, di tutta quella tecnica, non è rimasto che il modo di usarlo. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :92934
    (92934, 'Blankets developed against icy blades of wind. Although it completely prevents freezing damage to the potion, overconfidence is not advised, as there are limits to what can be achieved. \\n# ~Palmian Winter Fashion~'):
        "Una coperta messa a punto contro le lame di ghiaccio che sferzano. Impedisce del tutto che il gelo rovini le pozioni, ma tutto ha un limite e fidarsi troppo è vietato. \\n# ~Palmia: Collezione Autunno-Inverno~",

    # ---------------------------------------------------------- :92998
    (92998, 'Blankets developed against an approaching flame. It completely prevents the destruction of items due to combustion, but it has its limitations and one should not be overconfident. \\n# ~Palmian Summer Fashion~'):
        "Una coperta messa a punto contro le fiamme che avanzano. Impedisce del tutto che gli oggetti, bruciando, si riducano in carbone, ma tutto ha un limite e fidarsi troppo è vietato. \\n# ~Palmia: Collezione Primavera-Estate~",

    # ---------------------------------------------------------- :93358
    (93358, 'An indispensable machine for buying and selling money and goods. For security purposes, the system allows only one person registered to use it. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~'):
        "Una macchina indispensabile quando si comprano e si vendono denaro e merci. Per sicurezza il sistema la rende usabile a una sola persona, quella registrata. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :93360
    (93360, 'This machine is essential in assigning personnel. It is here that you can change the assignment of your fellow workers. \\"If you lose it by accident, don\'t worry. Everything is available at the Palmia Embassy, the keystone of the economy.\\" \\n# ~Tyris Armor Compendium, page of advertisements~'):
        "Una macchina indispensabile per assegnare la gente. Qui si cambia l'incarico dei compagni. \\\"Se per un caso sfortunato la perdete, state tranquilli: all'ambasciata di Palmia, cardine dell'economia, si trova tutto.\\\" \\n# ~Grande Compendio delle Armi di Tyris: le Reclame~",

    # ---------------------------------------------------------- :93823
    (93823, 'A simple shelter that can be set up in an emergency. After the crisis has passed, it can be picked up and reused. \\n# ~Daily Necessities for the Home~'):
        "Un rifugio semplice che si può montare in caso di bisogno. Passato il pericolo lo si raccoglie e si riusa: un arnese buono a tutto. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :94601
    (94601, 'A disc containing music. These discs play a specific enclosed song when used, but unfortunately, the technology to do anything but play them is lost to the present day.\\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un disco con dentro della musica. Usandolo suona il brano che ci hanno chiuso, ma purtroppo oggi, di tutta quella tecnica, non è rimasto che il modo di usarlo.\\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :99091
    (99091, "Medical equipment that, when used, determines a person's physical condition. Everyone may have played doctor when they were a child, but sensible adventurers should never use it for anything nefarious. \\n# ~an Adventurer is You! Guide for Travels~"):
        "Un arnese da medico che, a usarlo, dice sul momento come sta il corpo. Da bambini tutti avranno giocato al dottore, ma un avventuriero di buon senso non lo adoperi mai per fini poco puliti. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :102458
    (102458, 'A simple bedding mainly intended for sleeping outdoors. When you are sleepy, you can get temporary peace of mind by being completely enclosed in this bedding, cut off from the outside world. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Un giaciglio semplice, pensato soprattutto per dormire all'aperto. Quando hai sonno ti ci infili tutto e resti chiuso fuori dal mondo: per un poco è pace. \\n#~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :104791
    (104791, 'Basic tool necessary for jewelry processing. Naturally, it cannot be handled without skill. \\n# ~Daily Necessities for the Home~'):
        "L'attrezzo di base che serve per lavorare le gemme. Va da sé che senza l'abilità non si può adoperare. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :108457
    (108457, 'Tool needed to catch fish. On holidays, the docks of Port Kapul are said to be filled with anglers, or even tourists, who are struggling alone, clutching their gear in their hands, dreaming of catching a big fish. \\n# ~Daily Necessities for the Home~'):
        "L'arnese che serve per pescare. Nei giorni di festa, sulla banchina di Port Kapul, si dice che parecchi pescatori, anzi turisti, se lo stringano in mano sognando di tirare su un pesce grosso, e combattano da soli la loro battaglia. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :108459
    (108459, '\\"To catch fish, the bait is the most important. The rest is easy, just swing the rod, wait, and profit. And yes, of course, if you don\'t have the skill, you\'d be just waiting and waiting.\\" \\n# ~words of a fisherman proud of his catch~'):
        "\\\"Per pescare conta l'esca, certo, ma più di tutto conta questo. Il resto è facile: butti la lenza e stai fermo ad aspettare. Ah, e va da sé: se l'abilità non ce l'hai, aspetti e basta.\\\" \\n# ~Parole di un Pescatore Fiero della Sua Preda~",

    # ---------------------------------------------------------- :114077
    (114077, 'Small cooking set that can do a whole range of cooking. However, its only advantage is its light weight, so if you want to become a professional, we recommend you buy more expensive cooking equipment. \\n# ~Supporting Roles in Kitchen~'):
        "Un piccolo set da cucina con cui, solo a usarlo, si prepara un po' di tutto. Detto questo, il suo unico pregio è quanto pesa poco: se punti a diventare un professionista, meglio comprare attrezzi da cucina più cari. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :114141
    (114141, 'It is not only a cooking utensil, but also serves as a lightsource, and even produces the gentle sound of flames just by placing it on the table. However, from the standpoint of a cooking utensil, it is a little underpowered, and is often used as interior decoration. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Non serve solo da attrezzo da cucina: fa anche luce, e basta posarlo perché aggiunga il suono gentile della fiamma. Tre cose in una. Come attrezzo da cucina però è un po' debole, e finisce che lo si tiene per arredo. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :116346
    (116346, 'This revolutionary cooking utensil allows you to throw ingredients into it and cook a dish just by using it. However, as one might expect, it is difficult to make complicated dishes since the ingredients are simply thrown into the cooker. \\n# ~Supporting Roles in Kitchen~'):
        "Un attrezzo da cucina che cambia tutto: ci butti dentro gli ingredienti, lo usi, e il piatto è fatto. Però, come c'era da aspettarsi, siccome li butti dentro e basta, i piatti complicati vengono male. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :116603
    (116603, 'A strong rope that will not come undone no matter how hard it is pulled. It is a tool to be used for objects, so it is not suitable for attaching to people. \\n# ~Battles, Dragons, Swords and Magic~'):
        "Una corda forte che, per quanto la si tiri, non si sfilaccia. È un arnese da usare sulle cose, quindi per legarci una persona pare che non vada bene. \\n# ~Cose Lunghe Fatte per Essere Avvolte~",

    # ---------------------------------------------------------- :116605
    (116605, '\\"I said, \'Hey, hey, hey, what are you mad about?\' I answered as I was asked. I don\'t think I deserve your thanks or your abuse. And I didn\'t just say, \'Use it.\' I said, \'It\'s one of the many options you have to try.\'\\" \\n# ~<Lomias> the messenger from Vindale~'):
        "\\\"Ehi, ehi, che cos'è che ti fa arrabbiare? Io ho risposto a quel che mi è stato chiesto. Semmai mi si dovrebbe ringraziare; prendermi a male parole mi pare fuori luogo. E poi io non ho detto di usarla: ho detto che provare è una delle tante scelte che hai.\\\" \\n# ~Parole di <Lomias> il messaggero di Vindale~",

# 4 voci, 0 ambigue

    # ---------------------------------------------------------- :120505
    (120505, 'Basic tool necessary for carpentry. Naturally, it cannot be handled without skill. \\n# ~Daily Necessities for the Home~'):
        "L'attrezzo di base che serve per i lavori di falegname. Va da sé che senza l'abilità non si può adoperare. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :120571
    (120571, 'Basic tool necessary for tailoring. Naturally, it cannot be handled without skill. \\n# ~Daily Necessities for the Home~'):
        "Il set di base che serve per cucire. Va da sé che senza l'abilità non si può adoperare. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :121829
    (121829, 'A complete set of tools necessary for painting. If you have an artistic mind, it would be a good idea to use it. If you have a good mind for painting, you should try it. \\n# ~Gifts that I am Happy to Receive~'):
        "Un insieme con tutti gli arnesi che servono per dipingere. Se hai mano per il disegno, provalo. Sempre che tu ce l'abbia, la mano. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :122679
    (122679, 'This is the basic kit required to perform alchemy. Naturally, it cannot be handled without skill. \\n# ~Arcane Almanac~'):
        "Il kit di base che serve a fare alchimia. Va da sé che senza l'abilità non si può adoperare. \\n# ~Compendio Completo degli Oggetti Magici~",

# 21 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-037.jsonl'
RIGHE = {
    90137, 91909, 91911, 92252, 92389, 92934, 92998, 93358, 93360, 93823,
    94601, 99091, 102458, 104791, 108457, 108459, 114077, 114141, 116346, 116603,
    116605, 120505, 120571, 121829, 122679,
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
