# -*- coding: utf-8 -*-
"""108a - Lotto 001 di `db_item.hsp`: il RAPPORTO DI IDENTIFICAZIONE dei cibi.

`FILTER_ITEM_FOOD`, `description(3)`: **133 righe del sorgente, 56 firme**. E' il
lotto piu' economico del file, ed e' quello da cui si comincia perche' fissa la
**formula** del rapporto di identificazione, che poi si ripete su tutte le
2.580 firme rimaste.

⚠️⚠️ **E' IL PRIMO LOTTO CHE NON E' UN INTERVALLO DI RIGHE.** Le descrizioni di
una categoria sono sparse per settantacinquemila righe (42.785 -> 117.602),
quindi la zona si dichiara con `RIGHE = {...}`, emesso da
`_107-chiavi-item.py --solo-righe` e non scritto a mano. Il contratto del lotto
— «ogni voce della zona e' resa, ogni resa aggancia una voce» — e' identico, e
lo controllano le stesse reti 1 e 2.

⚠️⚠️ **IL TETTO E' SECCO: 69 CARATTERI, E SI MISURA DEGRADATO.** L'indice 3 non
passa da nessun impaginatore: `command.hsp:16275` fa
`cnven(trimdesc(description(3), 1))`, tronca al primo `#` e mette la riga in
`listn`. Non va a capo, non si taglia: **sfora e basta**. E «perche'» occupa 7
caratteri dove «perché» ne occupa 6, quindi il numero che conta e' quello dopo
`accenti.degrada()`. La rete e' `scratchpad/_107-descrizioni-item.py`.

### La formula, e perche' e' una formula

Il giapponese scrive **la stessa frase** su tutta la categoria — 「満腹度を回復
することができる食物。調理することができる。」 — e cambia solo quando cambia il
fatto. Non e' prosa: e' un referto. L'italiano tiene la forma del referto:

    Un cibo che sazia.                      il caso base
    ... e che si può cucinare.              quando il giapponese lo dice
    Un cibo di mare / Una verdura /         quando l'INGLESE riempie la casella
    Un frutto / Frutti a guscio / Un uovo   della categoria, che e' parte del referto

⭐ **Dove l'inglese, invece di riempire la casella, si mette a raccontare, si
torna alla formula.** Sette righe: il tonno «carnivoro», il salmone «dalle
abitudini di deposizione uniche», il pesce sciabola «che somiglia a un'anguilla»,
la farina «da forno», la pasta «che verrebbe meglio cotta», il cadavere «che si
puo' cucinare in piatti di carne». Il giapponese di tutte e sette e' la formula
generica, e un referto che dice cose diverse per il tonno e per la sardina ha
smesso di essere un referto. E' la regola di `decisioni.md`, «Quando l'inglese
aggiunge un fatto»: si segue il giapponese e si tace l'aggiunta.

### ⭐⭐ Tre difetti di monte che l'italiano ripara gratis

1. **`:115655`, la razione — l'inglese dice il CONTRARIO del giapponese.**
   「調理することができる。」 e' «si puo' cucinare»; l'inglese scrive «it cannot
   be cooked». In gioco la razione **si cucina**. Non e' un'aggiunta: e' una
   negazione.
2. **`:80490`, il mochi — l'inglese ha perso una frase intera.**
   「のどに詰まることがある。」, «certe volte va di traverso», che sulla gemella
   `:80553` (il kagami mochi) l'inglese ce l'ha, in maiuscolo: «CHOKE WARNING».
   I due giapponesi sono identici e adesso lo sono anche i due italiani.
3. **`:113943`, il filoncino — l'inglese ha perso 「調理することができる。」**,
   che il giapponese ha e che le altre righe della stessa forma dicono.

ⓘ **`:60517`, le tre bottiglie del condimento**: il giapponese dice solo
「調味料だ。使用することができる（使い捨て）。」. L'inglese aggiunge che qualcuno
lo versa sul bestiame prima della macellazione — vero in gioco, ma non e' quel
che il referto dice, e nei 69 caratteri non ci starebbe insieme al resto.

ⓘ **`:74301`, il pranzo del ringiovanimento**: «ti riporta all'infanzia» e non
«ti fa tornare bambino», perche' il genere del giocatore non si conosce
(`guida-stile.md`).

ⓘ **I termini gia' fissati altrove, e qui si ubbidisce:** 「エーテル病」 → «la
malattia dell'etere» (`command.hsp:2336` e altre otto), 「狂気度」 → «Follia»
(`command.hsp:10517`), 「運勢」 → «fortuna» (`skill.hsp:64`), 「マナ」 → mana
(`invariati.md:50`), e i nomi d'attributo dal glossario — apprendimento,
carisma, destrezza, percezione, magia, volonta', forza, costituzione.
`alraunia`, `spenseweed`, `mareilon`, `morgia`, `stomafillia` e `curaria` sono
in `invariati.md` e qui non compaiono: il nome dell'oggetto sta altrove, il
referto dice solo che cosa fa.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :42785 la mesugaki
    (42785, 'It is seafood that can be cooked and eaten.'):
        "Un cibo di mare che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :52111 la pianta acquatica
    (52111, 'It is vegetable that can be cooked and eaten.'):
        "Una verdura che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :52246 l'anguilla giardiniera
    # ⚠️ stesso inglese di :42785, giapponese diverso solo per due tabulazioni:
    #    e' la stessa cosa e si scrive uguale.
    (52246, 'It is seafood that can be cooked and eaten.'):
        "Un cibo di mare che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :55077 il cristallo curativo
    (55077, 'It is a precious food used to cure ether disease.'):
        "Un cibo prezioso che guarisce la malattia dell'etere.",

    # ---------------------------------------------------------- :55547 la gomma masticata
    (55547, 'It is food that barely restores satiety.'):
        "Un cibo che sazia appena appena.",

    # ---------------------------------------------------------- :55610 la gomma da masticare
    (55610, 'It is food that can slightly restore satiety.'):
        "Un cibo che sazia poco.",

    # ---------------------------------------------------------- :56403 la pastura
    (56403, '(Single-use) tool type food for feeding fishes placed on the ground.'):
        "Un cibo da dare ai pesci posati per terra (usa e getta).",

    # ---------------------------------------------------------- :56874 l'hamburger
    (56874, 'It is food that can restore satiety.'):
        "Un cibo che sazia.",

    # ---------------------------------------------------------- :56937 l'osiruko, l'ozouni
    (56937, 'It is food that can restore satiety. CHOKE WARNING.'):
        "Un cibo che sazia. Certe volte va di traverso.",

    # ---------------------------------------------------------- :57191 il pesce essiccato
    (57191, 'It is a dried out fish that can restore satiety.'):
        "Un pesce essiccato che sazia.",

    # ---------------------------------------------------------- :57254 la verdura essiccata
    (57254, 'It is a dried out vegetable that can restore satiety.'):
        "Una verdura essiccata che sazia.",

    # ---------------------------------------------------------- :57317 la frutta secca
    (57317, 'It is a dried out fruit that can restore satiety.'):
        "Un frutto essiccato che sazia.",

    # ---------------------------------------------------------- :58592 il tofu fritto e i suoi
    (58592, 'It is food that can restore satiety.'):
        "Un cibo che sazia.",

    # ---------------------------------------------------------- :60517 le tre bottiglie del condimento
    # ⚠️ il giapponese dice solo 「調味料だ。使用することができる（使い捨て）。」.
    #    L'inglese aggiunge il bestiame prima della macellazione: si tace, per la
    #    regola della 57a e della 91a (decisioni.md, «Quando l'inglese aggiunge un fatto»).
    (60517, '(Single-use) Seasoning. Some pour these on livestocks before slaughter.'):
        "Un condimento. Si può usare (usa e getta).",

    # ---------------------------------------------------------- :65530 la lanterna di zucca
    (65530, 'It is food that can restore satiety, illuminates surroundings brightly.'):
        "Un cibo che sazia e che di notte illumina un po' i dintorni.",

    # ---------------------------------------------------------- :67324 il pranzo dell'abisso
    (67324, 'It is a bento blessed by abyssal powers, it restores your stamina.'):
        "Un pranzo protetto dall'acqua. Ridà anche vigore.",

    # ---------------------------------------------------------- :67795 romias
    (67795, 'It is food that can restore satiety. Are you sure you want to eat it?'):
        "Un cibo che sazia. Vuoi davvero mangiarlo?",

    # ---------------------------------------------------------- :67860 il caco
    (67860, 'It is fruit that can be cooked and eaten.'):
        "Un frutto che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :67923 la ghianda dorata
    (67923, 'These are nuts that can be eaten, but it cannot cooked.'):
        "Frutti a guscio che si mangiano, ma non si possono cucinare.",

    # ---------------------------------------------------------- :67986 la ghianda, la castagna
    (67986, 'These are nuts that can be cooked and eaten.'):
        "Frutti a guscio che si possono cucinare e mangiare.",

    # ---------------------------------------------------------- :68653 la crimberry
    (68653, 'It is food that can restore satiety. Contains harmful substances.'):
        "Un cibo che sazia. Contiene sostanze nocive.",

    # ---------------------------------------------------------- :74167 la carne proibita
    (74167, "One thing for sure, it's edible."):
        "Tutto sommato è un cibo.",

    # ---------------------------------------------------------- :74301 il pranzo del ringiovanimento
    # ⚠️ «bambino» vorrebbe il genere del giocatore, che non si conosce
    #    (guida-stile.md): si rende il fatto, non la persona.
    (74301, 'It is food that turns you into a child.'):
        "Un cibo che ti riporta all'infanzia.",

    # ---------------------------------------------------------- :74364 il pranzo dell'invecchiamento
    (74364, 'It is food that makes you old.'):
        "Un cibo che ti fa invecchiare.",

    # ---------------------------------------------------------- :76722 la polpetta di riso
    (76722, 'It is food that can restore satiety instantly.'):
        "Un cibo che sazia in un attimo.",

    # ---------------------------------------------------------- :78118 il putitoro
    (78118, 'It is food that can restore satiety. Has beauty benefits.'):
        "Un cibo che sazia. Fa bene anche alla bellezza.",

    # ---------------------------------------------------------- :80490 il mochi
    # ⭐ L'INGLESE HA PERSO LA SECONDA FRASE. Il giapponese e' identico a quello
    #    di :56937 — 「のどに詰まることがある。」 — e la gemella :80553 (il kagami
    #    mochi) l'inglese ce l'ha, «CHOKE WARNING». Qui l'italiano la rimette,
    #    e la resa e' la stessa delle altre tre.
    (80490, 'It is food that can restore satiety.'):
        "Un cibo che sazia. Certe volte va di traverso.",

    # ---------------------------------------------------------- :81672 il biscotto della fortuna
    (81672, 'It is food that can restore satiety, and it will tell you your fortune.'):
        "Un cibo che sazia. Dopo averlo mangiato, predice la sorte.",

    # ---------------------------------------------------------- :84103 la coda di coniglio
    (84103, 'It is food that brings luck when eaten.'):
        "Un cibo che alza la fortuna.",

    # ---------------------------------------------------------- :86469 il pranzo della sorella
    # ⚠️ il giapponese dice solo 「狂気度が減少する食物だ。」: la sazieta' la
    #    aggiunge l'inglese. 狂気度 e' «Follia» da command.hsp:10517.
    (86469, 'It is food that can restore satiety and lower insanity.'):
        "Un cibo che abbassa la follia.",

    # ---------------------------------------------------------- :86803 il frutto magico
    (86803, 'It is a fruit increase mana when eaten.'):
        "Un cibo che alza il mana.",

    # ---------------------------------------------------------- :87256 il formaggio dell'eroe
    (87256, 'It is food that can increase your life energy.'):
        "Un cibo che alza la vita.",

    # ---------------------------------------------------------- :88278 la mela della felicità
    (88278, "It is a magical fruit that increase one's luck greatly."):
        "Un cibo che alza molto la fortuna.",

    # ---------------------------------------------------------- :92588 l'uovo
    (92588, 'It is an egg that can be cooked and eaten.'):
        "Un uovo che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :92720 la carne secca
    (92720, 'It is a dried out meat that can restore satiety.'):
        "Della carne secca che sazia.",

    # ---------------------------------------------------------- :93893 il seme magico
    (93893, '(Single-use) edible seed that can be planted to grow magical plants.'):
        "Un seme che diventa un albero magico. Si usa (usa e getta).",

    # ---------------------------------------------------------- :93960 il seme di gemma
    (93960, '(Single-use) edible seed that can be planted to grow gems.'):
        "Un seme che diventa un albero di gemme. Si usa (usa e getta).",

    # ---------------------------------------------------------- :102524 la stomafillia
    (102524, 'It is a type of herb that can greatly restore satiety.'):
        "Un'erba che sazia molto.",

    # ---------------------------------------------------------- :102587 l'alraunia
    (102587, 'It is a type of herb that is good for your learning and charisma..'):
        "Un'erba che alza apprendimento e carisma.",

    # ---------------------------------------------------------- :102650 la curaria
    (102650, 'It is a type of herb that is good for your overall abilities.'):
        "Un'erba che alza un po' tutti gli attributi base.",

    # ---------------------------------------------------------- :102713 la spenseweed
    (102713, 'It is a type of herb that is good for your dexterity and perception.'):
        "Un'erba che alza destrezza e percezione.",

    # ---------------------------------------------------------- :102776 il mareilon
    (102776, 'It is a type of herb that is good for your magic and willpower..'):
        "Un'erba che alza magia e volontà.",

    # ---------------------------------------------------------- :102839 la morgia
    (102839, 'It is a type of herb that is good for your strength and constitution.'):
        "Un'erba che alza forza e costituzione.",

    # ---------------------------------------------------------- :102906 il seme di artefatto
    (102906, '(Single-use) edible seed that can be planted to grow artifacts.'):
        "Un seme che diventa un albero di artefatti. Si usa (usa e getta).",

    # ---------------------------------------------------------- :102973 il seme ignoto
    (102973, '(Single-use) edible seed that can be planted to grow a mysterious plant.'):
        "Un seme che diventa un albero misterioso. Si usa (usa e getta).",

    # ---------------------------------------------------------- :103040 il seme di erba
    (103040, '(Single-use) edible seed that can be planted to grow magical herbs.'):
        "Un seme che diventa un albero di erbe. Si usa (usa e getta).",

    # ---------------------------------------------------------- :103107 il seme di frutto
    (103107, '(Single-use) edible seed that can be planted to grow fruits.'):
        "Un seme che diventa un albero da frutto. Si usa (usa e getta).",

    # ---------------------------------------------------------- :103174 il seme di ortaggio
    (103174, '(Single-use) edible seed that can be planted to grow vegetables.'):
        "Un seme che diventa un albero di ortaggi. Si usa (usa e getta).",

    # ---------------------------------------------------------- :107676 il pesce sciabola
    # ⚠️ il giapponese e' la formula generica; l'anguilla la nomina solo l'inglese.
    (107676, 'It is seafood that looks something like an Eel.'):
        "Un cibo di mare che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :107749 il tonno
    (107749, 'It is a carnivorous fish that can be cooked and eaten.'):
        "Un cibo di mare che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :107895 il salmone
    (107895, 'It is a fish with unique spawning habits.'):
        "Un cibo di mare che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :113815 il sacco di farina
    (113815, 'It is flour used for baking.'):
        "Un cibo che sazia e che si può cucinare.",

    # ---------------------------------------------------------- :113880 la pasta fresca
    (113880, 'It is food that would taste better cooked.'):
        "Un cibo che sazia e che si può cucinare.",

    # ---------------------------------------------------------- :113943 il filoncino
    # ⭐ l'inglese ha perso 「調理することができる。」, che il giapponese ha.
    (113943, 'It is food that can restore satiety.'):
        "Un cibo che sazia e che si può cucinare.",

    # ---------------------------------------------------------- :115655 la razione
    # ⭐⭐ QUI L'INGLESE DICE IL CONTRARIO DEL GIAPPONESE: 「調理することができる。」
    #    e' «si puo' cucinare», e l'inglese scrive «it cannot be cooked».
    (115655, 'It is food that restores satiety, it cannot be cooked.'):
        "Un cibo che sazia e che si può cucinare.",

    # ---------------------------------------------------------- :117602 il cadavere
    (117602, 'It is food that restores satiety, it can be cooked into meat dishes.'):
        "Un cibo che sazia e che si può cucinare.",
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-001.jsonl'
RIGHE = {
    42785, 52111, 52246, 55077, 55547, 55610, 56403, 56874, 56937, 57191,
    57254, 57317, 58592, 60517, 65530, 67324, 67795, 67860, 67923, 67986,
    68653, 74167, 74301, 74364, 76722, 78118, 80490, 81672, 84103, 86469,
    86803, 87256, 88278, 92588, 92720, 93893, 93960, 102524, 102587, 102650,
    102713, 102776, 102839, 102906, 102973, 103040, 103107, 103174, 107676, 107749,
    107895, 113815, 113880, 113943, 115655, 117602,
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
