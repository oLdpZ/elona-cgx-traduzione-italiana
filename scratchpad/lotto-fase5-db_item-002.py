# -*- coding: utf-8 -*-
"""108a - Lotto 002 di `db_item.hsp`: il rapporto di identificazione delle POZIONI.

`FILTER_ITEM_POTION`, `description(3)`: **77 righe del sorgente, 65 firme**. La
formula e' quella fissata dal lotto 001 (`glossario.md`, sezione della 108a), e
qui prende la forma «**Una pozione che** …» / «**Una bevanda che** …» — la
casella della categoria la riempie il giapponese stesso, che alterna
ポーション, 飲み物, 液体 e 油.

⚠️ **Il tetto e' sempre secco: 69 caratteri degradati**, e questa categoria e'
la prima che lo tocca davvero. Sette righe compongono due fatti
(«alza X e Y, e resiste a Z e W»), e li' «Una pozione che» non ci sta: quelle
**aprono col verbo**. Non e' un'eccezione alla formula, e' la formula che cede
la testa quando il contenuto la riempie — l'inglese fa lo stesso, e infatti
110 righe dell'indice 3 sforano gia' in inglese.

### ⚠️ Quattro giapponesi uguali che l'inglese distingue

Il rovescio del lotto 001, dove l'inglese appiattiva. Qui e' il giapponese a
essere lo stesso e l'inglese a variare, e la resa dev'essere **una**:

    :44445 / :72144   様々な状態異常を引き起こすポーションだ。
                      en «a variety of undesired effects» / «many negative
                      status effects» — la stessa cosa detta in due modi
    :126010 / :126081 HPと状態異常を回復するポーションだ。
                      en «cures ALL status effects» solo sulla pozione di Jure:
                      le altre sei dicono «cures status effects»

⭐ Le due coppie passano dalla **rete 13**, che le stampa come referto: e'
esattamente il caso per cui esiste.

### ⚠️ Due righe dove il giapponese dice un'altra cosa, e vince lui

- **`:90772`, la bottiglia vuota.** L'inglese: «a potion bottle that is
  completely empty». Il giapponese: 「水を汲むことができる瓶だ。」, *una
  bottiglia in cui si puo' prendere l'acqua*. Il secondo dice a che serve, il
  primo descrive il nome dell'oggetto — e la bottiglia vuota, in gioco, si
  riempie al pozzo.
- **`:129442`, l'acqua sporca.** L'inglese dice che fa ammalare; il giapponese
  dice 「病気になる可能性のある」, *che **puo'** far ammalare*. La differenza e'
  fra una certezza e una probabilita', ed e' quella che il giocatore vuole.

ⓘ **`:63387`, i dolcetti della strega**: l'inglese apre con «It is **food**» ma
il giapponese dice 飲み物, *bevanda*, come tutta la sua famiglia. Si segue lui.

ⓘ **I termini gia' fissati altrove, e qui si ubbidisce:** 「友好度」 → «la
simpatia» (`chat.hsp:25511`, `:14284`, `:14335`), 「エーテル病」 → «la malattia
dell'etere», 「状態異常」 → «gli stati alterati» (`buff.hsp:430` li chiama
«stati»), 「潜在能力」 → «il potenziale» (`chara.hsp:4311`), 「恐怖」 →
«terrore», e `DV`, `PV`, `HP` sono **invariati** perche' il giapponese scrive le
stesse sigle (`invariati.md:79`, `:83`, `:84`).
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :43903 l'energetico
    (43903, 'It is a beverage that restores satiety.'):
        "Una bevanda che sazia.",

    # ---------------------------------------------------------- :44445 la pozione dell'agonia
    (44445, 'It is a potion that causes a variety of undesired effects.'):
        "Una pozione che provoca stati alterati di ogni genere.",

    # ---------------------------------------------------------- :44516 la pozione della calamità
    (44516, 'It is a potion that causes a variety of debuffs.'):
        "Una pozione che provoca indebolimenti di ogni genere.",

    # ---------------------------------------------------------- :44587 la pozione del fisico
    (44587, 'It is a potion that improves physical performance.'):
        "Una pozione che migliora le doti fisiche.",

    # ---------------------------------------------------------- :49649 l'idromele dorato
    (49649, 'It is a beverage that gives spirit-out-of-body experience.'):
        "Una bevanda che fa uscire dal corpo.",

    # ---------------------------------------------------------- :53775 il disinfettante
    (53775, 'It is a gallon of disinfectant.'):
        "Un prodotto per disinfettare.",

    # ---------------------------------------------------------- :55347 la cola, l'orzata, il succo
    (55347, 'It is a beverage that restores satiety.'):
        "Una bevanda che sazia.",

    # ---------------------------------------------------------- :56133 l'annullatore d'incontri
    (56133, '(Single-use) usable potion.'):
        "Un oggetto che si può anche bere. Si usa (usa e getta).",

    # ---------------------------------------------------------- :56474 l'urina, il vomito
    (56474, 'It is something that is (questionably) drinkable.'):
        "Un oggetto che si può bere.",

    # ---------------------------------------------------------- :58852 la pozione della saggezza
    (58852, 'It is a potion that boosts all sorts of abilities.'):
        "Una pozione che migliora attributi di ogni genere.",

    # ---------------------------------------------------------- :58923 la pozione della gemma
    # ⚠️ «Una pozione che» non ci sta nei 69: le quattro composte aprono col verbo.
    (58923, 'It is a potion that boosts CON & CHA and resists paralysis & blindness.'):
        "Alza costituzione e carisma, e resiste a paralisi e cecità.",

    # ---------------------------------------------------------- :59388 il tè verde, il tè nero
    (59388, 'It is a tea beverage with health benefits.'):
        "Un tè che ha effetti curativi.",

    # ---------------------------------------------------------- :61655 la benzina
    (61655, 'It is volatile oil that gives off an odor.'):
        "Un olio volatile che manda cattivo odore.",

    # ---------------------------------------------------------- :61726 l'olio essenziale
    (61726, 'It is some plant-based volatile oil.'):
        "Un olio volatile di origine vegetale.",

    # ---------------------------------------------------------- :63387 i dolcetti della strega
    (63387, 'It is food that fully restore satiety. Some faint due to its strong kick.'):
        "Una bevanda che sazia. Rimette in sesto, ma fa svenire.",

    # ---------------------------------------------------------- :65674 la pozione della piuma
    (65674, 'It is a potion that temporarily raises DV and floats you.'):
        "Alza il DV per un po' e fa fluttuare.",

    # ---------------------------------------------------------- :65745 la pozione della concentrazione
    (65745, 'It is a potion that boosts PER & WIL and helps resist sleep & confusion.'):
        "Alza percezione e volontà, e resiste a sonno e confusione.",

    # ---------------------------------------------------------- :68524 il caffè
    (68524, 'It is a potion that can trick mild sleepiness.'):
        "Una pozione che inganna un po' di sonnolenza.",

    # ---------------------------------------------------------- :70068 l'antisettico
    (70068, 'It is a potion that keeps food from rotting.'):
        "Mescolata a un cibo, gli impedisce di marcire.",

    # ---------------------------------------------------------- :72000 la pozione soma
    (72000, 'It is a potion that restores stamina and and relieves drowsiness.'):
        "Una pozione che toglie fatica e sonnolenza.",

    # ---------------------------------------------------------- :72073 la pozione nektar
    (72073, 'It is a potion that greatly restores HP.'):
        "Una pozione che ridà molti HP.",

    # ---------------------------------------------------------- :72144 la pozione del disastro
    # ⚠️ stesso giapponese di :44445, e quindi la stessa resa: l'inglese le
    #    distingue («undesired effects» / «negative status effects») e il
    #    giapponese no.
    (72144, 'It is a potion that causes many negative status effects.'):
        "Una pozione che provoca stati alterati di ogni genere.",

    # ---------------------------------------------------------- :72215 l'aqua sanctio
    (72215, 'It is a powerful offensive potion.'):
        "Una pozione d'attacco, e potente.",

    # ---------------------------------------------------------- :74435 l'acceleratore
    (74435, 'It is a potion that restores speed potential.'):
        "Una pozione che ridà potenziale alla velocità.",

    # ---------------------------------------------------------- :77637 la Vernis originale
    (77637, 'It is a special candy that restores all sorts of things.'):
        "Una caramella speciale che ridà un po' di tutto.",

    # ---------------------------------------------------------- :79506 la capsula blu
    (79506, 'It is a drinkable capsule that restores your stamina.'):
        "Una capsula che toglie la fatica. Si può bere.",

    # ---------------------------------------------------------- :79577 la gassosa
    (79577, 'It is a drink that can restore stamina.'):
        "Una bevanda che toglie la fatica.",

    # ---------------------------------------------------------- :81814 il liquido ignifugo
    (81814, 'It is a potion that protect items from fire when blended.'):
        "Mescolata a una cosa, la protegge dal fuoco.",

    # ---------------------------------------------------------- :83485 la pozione dell'evoluzione
    (83485, 'It is a potion that causes advantageous mutations.'):
        "Una pozione che porta mutazioni utili.",

    # ---------------------------------------------------------- :83838 la pozione della discesa
    (83838, 'It is a potion that induces level-lowering effect.'):
        "Una pozione che abbassa il livello.",

    # ---------------------------------------------------------- :84370 la soluzione salina
    (84370, "It is a potion that's just salty."):
        "Una pozione che è soltanto salata.",

    # ---------------------------------------------------------- :89152 il sangue di Ermes
    (89152, 'It is a potion that permanently increases speed.'):
        "Una pozione che alza la velocità per sempre.",

    # ---------------------------------------------------------- :89564 il filtro d'amore
    # ⓘ 友好度 è «la simpatia», già fissata da chat.hsp:25511 e :14284.
    (89564, 'It is a potion that increases impression. You can blend it in food.'):
        "Alza la simpatia. Si può mescolare al cibo.",

    # ---------------------------------------------------------- :90772 la bottiglia vuota
    # ⚠️ il giapponese non dice «vuota»: dice che ci si può prendere l'acqua.
    (90772, 'It is a potion bottle that is completely empty.'):
        "Una bottiglia in cui si può prendere l'acqua.",

    # ---------------------------------------------------------- :91659 la manciata di neve
    (91659, 'These are things that, can be used to build a snowman.'):
        "Se se ne raccoglie tanta, ci si fa un pupazzo di neve.",

    # ---------------------------------------------------------- :92326 la molotov
    (92326, 'It is a liquid that creates walls of flame.'):
        "Un liquido che fa nascere muri di fiamme.",

    # ---------------------------------------------------------- :92525 il latte
    (92525, 'It is a drink that fills your stomach.'):
        "Una bevanda che riempie la pancia.",

    # ---------------------------------------------------------- :93072 il liquido antiacido
    (93072, 'It is a potion that protect items from acid when blended.'):
        "Mescolata a una cosa, la protegge dagli acidi.",

    # ---------------------------------------------------------- :93557 la cura della corruzione
    (93557, 'It is a valuable potion that can cure Ether Disease.'):
        "Una pozione preziosa che guarisce la malattia dell'etere.",

    # ---------------------------------------------------------- :96198 la tintura
    (96198, "It is a potion that colors things it's mixed with."):
        "Mescolata a una cosa, la colora.",

    # ---------------------------------------------------------- :96429 l'acqua
    (96429, 'It is a potion with no particular effect.'):
        "Una pozione senza nessun effetto particolare.",

    # ---------------------------------------------------------- :102111 la cura della mutazione
    (102111, "It is a potion that removes some of your body's mutations."):
        "Una pozione che toglie qualcuna delle mutazioni addosso.",

    # ---------------------------------------------------------- :102182 la pozione della mutazione
    (102182, 'It is a potion that causes your body to mutate.'):
        "Una pozione che fa mutare il corpo.",

    # ---------------------------------------------------------- :102395 la pozione che indebolisce le resistenze
    (102395, 'It is a potion that temporarily lowers resistances.'):
        "Una pozione che abbassa le resistenze per un po'.",

    # ---------------------------------------------------------- :104865 l'acido solforico
    (104865, 'It is a chemical for dissolving bodies.'):
        "Un liquido che scioglie la carne.",

    # ---------------------------------------------------------- :105599 la pozione della debolezza
    (105599, 'It is a potion that temporarily lowers PV.'):
        "Una pozione che abbassa il PV per un po'.",

    # ---------------------------------------------------------- :105816 la pozione dell'eroe
    (105816, 'It is a potion that boosts STR & DEX and helps resist fear and confusion.'):
        "Alza forza e destrezza, e resiste a terrore e confusione.",

    # ---------------------------------------------------------- :106040 la pozione della lentezza
    (106040, 'It is a potion that temporarily slows you.'):
        "Una pozione che rallenta per un po'.",

    # ---------------------------------------------------------- :106111 la pozione della velocità
    (106111, 'It is a potion that temporarily speeds you up.'):
        "Una pozione che accelera per un po'.",

    # ---------------------------------------------------------- :106328 la pozione della resistenza
    (106328, 'It is a potion that temporarily confers resistance to all elements.'):
        "Dà per un po' resistenza agli elementi.",

    # ---------------------------------------------------------- :106472 il sangue di troll
    (106472, 'It is a potion that temporarily enhances natural regeneration.'):
        "Una pozione che alza per un po' la guarigione.",

    # ---------------------------------------------------------- :106616 la pozione del silenzio
    (106616, 'It is a potion that induces silence.'):
        "Una pozione che porta il silenzio.",

    # ---------------------------------------------------------- :106913 la pozione del difensore
    (106913, 'It is a potion that temporarily boosts PV and helps resist fear.'):
        "Alza il PV per un po' e resiste al terrore.",

    # ---------------------------------------------------------- :111995 la pozione del potenziale
    (111995, 'It is a potion that raises the potential of one attribute.'):
        "Alza il potenziale di uno degli attributi base.",

    # ---------------------------------------------------------- :112066 il ristoro dello spirito
    (112066, 'It is a potion that restores mental attributes.'):
        "Una pozione che ripara gli attributi mentali calati.",

    # ---------------------------------------------------------- :112137 il ristoro del corpo
    (112137, 'It is a potion that restores physical attributes.'):
        "Una pozione che ripara gli attributi fisici calati.",

    # ---------------------------------------------------------- :113679 il veleno
    (113679, 'It is poison. You can mix it in food.'):
        "Provoca l'avvelenamento. Si può mescolare al cibo.",

    # ---------------------------------------------------------- :114280 la birra, il whisky, la Crim ale
    (114280, 'It is a beverage that gets you drunk.'):
        "Una bevanda che ubriaca.",

    # ---------------------------------------------------------- :126010 la pozione di Jure
    # ⚠️ stesso giapponese di :126081, e l'inglese aggiunge «all» solo qui.
    (126010, 'It is a potion that restores HP and cures all status effects.'):
        "Una pozione che ridà HP e cura gli stati alterati.",

    # ---------------------------------------------------------- :126081 le altre sei pozioni di cura
    (126081, 'It is a potion that restores HP and cures status effects.'):
        "Una pozione che ridà HP e cura gli stati alterati.",

    # ---------------------------------------------------------- :129159 il sonnifero
    (129159, 'It is a potion that induces sleep.'):
        "Una pozione che fa addormentare.",

    # ---------------------------------------------------------- :129230 la pozione della paralisi
    (129230, 'It is a potion that induces paralysis.'):
        "Una pozione che paralizza.",

    # ---------------------------------------------------------- :129301 la pozione della confusione
    (129301, 'It is a potion that induces confusion.'):
        "Una pozione che confonde.",

    # ---------------------------------------------------------- :129372 la pozione della cecità
    (129372, 'It is a potion that induces blindness.'):
        "Una pozione che acceca.",

    # ---------------------------------------------------------- :129442 l'acqua sporca
    # ⚠️ il giapponese dice «può far ammalare», l'inglese lo dà per certo.
    (129442, 'It is a potion that induces sickness.'):
        "Una pozione che può far ammalare.",
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-002.jsonl'
RIGHE = {
    43903, 44445, 44516, 44587, 49649, 53775, 55347, 56133, 56474, 58852,
    58923, 59388, 61655, 61726, 63387, 65674, 65745, 68524, 70068, 72000,
    72073, 72144, 72215, 74435, 77637, 79506, 79577, 81814, 83485, 83838,
    84370, 89152, 89564, 90772, 91659, 92326, 92525, 93072, 93557, 96198,
    96429, 102111, 102182, 102395, 104865, 105599, 105816, 106040, 106111, 106328,
    106472, 106616, 106913, 111995, 112066, 112137, 113679, 114280, 126010, 126081,
    129159, 129230, 129301, 129372, 129442,
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
