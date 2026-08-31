# -*- coding: utf-8 -*-
"""115a - Lotto 040 di `db_item.hsp`: GLI SCARTI, la coda. LA CATEGORIA SI CHIUDE.

`FILTER_JUNK`, righe 76.000 in su: **29 righe** su 27 oggetti — 26 dell'indice
0, nessuna dell'indice 1 e 3 dell'indice 2. Con questo lotto `FILTER_JUNK` passa
a **0 da fare su 124 vive**: e' la terza categoria chiusa del corpo dopo il
mobilio (114a) e gli attrezzi (115a), e ci sono voluti tre lotti, dal 038 al 040.

⚠️ Come per il 037, la coda di una categoria **non e' un intervallo stretto**:
le ultime 29 righe stanno sparse fra `:86735` e `:128235`.

### ⭐⭐ LE TRE OSSA SONO UNA FAMIGLIA, E IL GIAPPONESE LO DICE DUE VOLTE

`:116408` (animale), `:127669` (umane), `:127731` (di qualcosa) hanno la stessa
identica seconda frase — «di occasioni per usarle ce n'e' parecchie... ma ce
n'e' talmente tante che come valore non contano niente» — e cambia solo di chi
sono le ossa. Tre rese uguali tranne la prima riga.

ⓘ L'inglese qui e' fedele: traduce tre volte la stessa frase in tre modi
leggermente diversi, ma non aggiunge e non toglie niente.

### ⭐ IL NOME DELL'OGGETTO E' LUNGO 15 CARATTERI, E LO SI SCRIVE LO STESSO

`:91460` e' lo spaventapasseri di neve, e «spaventapasseri» misura **15**
caratteri: uno in piu' della finestra di rinculo. Il preflight lo segnala.

Si scrive lo stesso, per due ragioni misurabili: il contratto dei nomi (107a)
vuole che la prosa nomini l'oggetto col nome che il giocatore vede, e la parola
sta **all'inizio** della riga (caratteri 5-19), lontano dal confine dei 70 dove
l'impaginatore spezza. ⚠️ La prova non e' il ragionamento ma il cancello: se
`_107-descrizioni-item` avesse detto «parole spezzate introdotte: 1», la frase
andava riscritta. Ha detto 0.

ⓘ Nella riga gemella `:112817` (lo spaventapasseri normale) la parola **non
c'e'**, e non e' una svista: il giapponese li' dice 農地の守護者, «il guardiano
dei campi», e non usa il nome dell'oggetto. Si segue il giapponese.

### ⭐ LA QUINTA RIGA DEL CORPO SENZA GIAPPONESE

`:116915` — la battuta sul pezzo di minerale — ha il giapponese **vuoto** e un
inglese vero, come `:50410` (034), `:72552` (035), `:80994` e `:84969` (036).
Fanno **cinque su 694 rese del corpo**, e sono tutte e cinque righe di indice 2.

Il conto continua a comportarsi come previsto nel 036: cresce piano, una ogni
lotto o due, ed e' compatibile con l'ipotesi che siano aggiunte del CGX scritte
direttamente nel ramo inglese.

### ⓘ Il verso della battuta del cane

`:127733` e' 「う～、わんわん！わん！　…くぅん」, dove くぅん e' il guaito
sommesso del cane. L'italiano scrive «...mugolio» e non «...guaìto» per una
ragione di codifica, non di gusto: l'accento in mezzo alla parola `degrada()`
lo trasforma in apostrofo e la parola si spacca. E' la stessa lezione di «dei»
nel lotto 035, applicata **prima** invece che dopo il rifiuto.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :86735
    (86735, "A mysterious heart that continues to beat even now. It is said that just by possessing it, one can possess the hearts of one's enemies. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un cuore misterioso che ancora adesso continua a battere. Dicono che, solo a portarlo addosso, si fa proprio anche il cuore dei nemici. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :91460
    (91460, 'A fashionable scarecrow with a white hat on his head. It is said that this is the figure of a scarecrow that got tired of guarding the farmland and made a bold debut in the city. \\n# ~Totally Made-up Stories that are Mistaken for Lies, Volume 2~'):
        "Uno spaventapasseri elegante, con in testa un cappello bianco. Dicono che sia uno di quelli stanchi di fare la guardia ai campi, che si è deciso a esordire in città. \\n# ~Storie Inventate Scambiate per Bugie, Volume 2~",

    # ---------------------------------------------------------- :92451
    (92451, 'Brown substance spawned from living organisms. It has an abominable odor, but it is said that some people, perhaps caught up in madness, collect these things. \\n#~Thousands of pieces of Junk I love~'):
        "Un oggetto bruno partorito da un essere vivente. Ha anche un odore, ed è cosa da schifare; eppure pare che qualcuno, forse preso dalla follia, ne raccolga di una certa specie come se ne fosse posseduto. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :109208
    (109208, "Plain, unremarkable tree stump. It has a rugged, natural roughness that makes it ideal as a chair for the house! But don't fall for it, because although you can sit on it, it's really just a piece of junk. \\n#~Thousands of pieces of Junk I love~"):
        "Un ceppo d'albero senza niente di speciale. C'è chi te lo vende con l'astuzia dicendo che nel suo essere rozzo c'è l'asprezza della natura ed è perfetto da usare per sedia in casa; ma sederti ci puoi sedere, e per il resto è ciarpame: non cascarci. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :111063
    (111063, 'Miscellaneous goods consisting of cut flowers in a single package. Often used as a thoughtful gift. \\n# ~Gifts that I am Happy to Receive~'):
        "Un articolo fatto di fiori recisi messi insieme. Spesso si usa come dono che viene dal cuore. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :111065
    (111065, '\\"When you are as beautiful as I am, women will come to you, but when I want to approach a woman myself, I usually use this one. Women are weak against things, and the woman I love the most also says so.\\" \\n# ~words of <Raphael> the womanizer~'):
        "\\\"Quando sei bello come me sono le donne a venirti incontro; ma quando voglio essere io ad avvicinarmi, di solito uso questo. Le donne cedono alle cose, sai: me lo diceva anche la donna che amo di più.\\\" \\n# ~Parole di <Raphael> il donnaiolo~",

    # ---------------------------------------------------------- :112755
    (112755, "Tool used for cleaning. It has long been considered an abomination because it symbolizes a magician, but nowadays it is used exclusively as a plaything for children's sword fighting. \\n# ~Daily Necessities for the Home~"):
        "L'attrezzo che si usa per pulire. Dai tempi antichi la si è schifata perché è il simbolo dei maghi, ma oggi è ridotta a un gioco per le spade finte dei bambini. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :112817
    (112817, 'The guardian of the farmland, with its arms outstretched wide, threatening the vermin. Its legs are thrust into the ground, a sign of its will to engage in command without ever leaving the scene. \\n# ~Totally Made-up Stories that are Mistaken for Lies, Volume 2~'):
        "Il guardiano dei campi che, spalancate le braccia, mette paura alle bestie nocive. Che abbia i piedi piantati nel terreno sarà il segno della volontà di non lasciare mai il posto e di eseguire l'ordine. \\n# ~Storie Inventate Scambiate per Bugie, Volume 2~",

    # ---------------------------------------------------------- :112879
    (112879, 'Wood that has been prepared at a certain height and dried for use as fuel. Because it burns very well, it has a value in daily life, and is not expensive because it is a daily commodity. \\n#~Supporting Roles in Kitchen~'):
        "Legno tagliato a una certa altezza e fatto seccare per farne combustibile. Siccome brucia molto bene ha un suo valore nella vita di ogni giorno; ma essendo roba d'uso comune, caro non si può dire che sia. \\n#~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :116408
    (116408, 'Weathered animal bones. There are many opportunities to use the bones for spells and for refining water medicine, but they are in such oversupply that they are worth little more than a dime. \\n#~Thousands of pieces of Junk I love~'):
        "Ossa d'animale sbiancate dal tempo. Di occasioni per usarle ce n'è parecchie, dalla stregoneria al distillare pozioni, ma ce n'è talmente tante che come valore non contano niente. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :116470
    (116470, 'Dried and bundled grass. It has some elasticity and could be used for sleeping, but it would be best not to use it to rest, as the day would be consumed with the task of removing the straw from your clothes. \\n#~Thousands of pieces of Junk I love~'):
        "Erba fatta seccare e legata in fascio. Ha una certa elasticità e sembrerebbe buona per dormirci, ma poi la giornata se ne va a togliersi la paglia di dosso: meglio non riposarci sopra. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :116540
    (116540, 'Dried fish carcasses. They are worthless and inedible, but when given to children, they are said to hold them in their hands and play with them as if they were legendary creatures. \\n#~Cheap Gifts for Your Kids~'):
        "La carcassa secca di un pesce. Anche a metterla in acqua non si mangia di certo, e non vale niente; ma dandola a un bambino, dicono, se la tiene in mano e ci gioca muovendola come fosse una bestia leggendaria. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :116665
    (116665, 'A bowl with something inside, but it is not food, so you cannot eat it even if you are hungry. \\n# ~Daily Necessities for the Home~'):
        "Un recipiente fatto più largo e più basso di una scodella. Dentro c'è qualcosa, ma non è cibo, quindi anche se hai fame non lo puoi mangiare. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :116727
    (116727, 'An empty bowl with nothing inside. It can be used as a tableware, or put a plant in it for decoration. \\n# ~Supporting Roles in Kitchen~'):
        "Un recipiente vuoto, senza niente dentro. C'è chi lo usa per la tavola e chi ci mette una pianta per ornamento: ognuno a modo suo. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :116789
    (116789, 'Woven baskets made of grass vines. It has some holding power, but its coarse texture makes it impossible to use for activities such as fetching water. \\n# ~Supporting Roles in Kitchen~'):
        "Un cesto intrecciato con tralci di piante. Qualcosa la tiene, ma ha le maglie larghe, quindi per cose come attingere acqua non si può usare. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :116851
    (116851, "Empty bottles of various sizes. They are somewhat too small to hold water, but enough to catch a child's eye. \\n#~Cheap Gifts for Your Kids~"):
        "Bottiglie vuote di ogni misura. Per tenere l'acqua sono un po' troppo piccole, ma per attirare l'occhio di un bambino bastano e avanzano. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :116913
    (116913, 'Rock lumps containing a small amount of minerals. It has no monetary value due to its very low content, but it is said to have certain uses, such as being used in cooking and bathing when heated red-hot. \\n#~Thousands of pieces of Junk I love~'):
        "Un pezzo di roccia con dentro un poco di minerale. Ce n'è così poco che di valore in denaro non ne ha, ma pare che a scaldarlo fino al rosso qualche uso lo trovi, in cucina o al bagno. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :116915
    (116915, '\\"This ore piece is a real piece of trash.\\" \\n#~some Bearded Guy~'):
        "\\\"Questo pezzo di minerale è proprio un pezzo di spazzatura.\\\" \\n#~un tizio con la barba~",

    # ---------------------------------------------------------- :123419
    (123419, 'A basket with nothing in it. Most of them are disposable. \\n# ~Supporting Roles in Kitchen~'):
        "Un cesto senza niente dentro. Si usa soprattutto da contenitore quando si mangia all'aperto, e quasi tutti sono usa e getta. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :127669
    (127669, 'Weathered human bones. There are many opportunities to use the bones for spells, refining water medicine, and other purposes, however, there is an oversupply, so the value of the bones is a mere trifling sum. \\n#~Thousands of pieces of Junk I love~'):
        "Ossa umane sbiancate dal tempo. Di occasioni per usarle ce n'è parecchie, dalla stregoneria al distillare pozioni, ma ce n'è talmente tante che come valore non contano niente. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :127731
    (127731, 'Weathered bones. There are many opportunities to use the bones for spells, refining water medicine, and other purposes, however, there is an oversupply, so the value of the bones is a mere trifling sum. \\n#~Thousands of pieces of Junk I love~'):
        "Ossa di qualcosa, sbiancate dal tempo. Di occasioni per usarle ce n'è parecchie, dalla stregoneria al distillare pozioni, ma ce n'è talmente tante che come valore non contano niente. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :127733
    (127733, '\\"Woof! Woof! ..scut!\\" \\n#~Poppy the Puppy~'):
        "\\\"Uuuh, bau bau! Bau! ...mugolio.\\\" \\n#~Parole di <Poppy> il cagnolino~",

# 3 voci, 0 ambigue

    # ---------------------------------------------------------- :127793
    (127793, 'A sword broken in two from the middle. It has been exposed to the wind and rain and has spilled so much that it is no longer of any value, nevertheless, when given to children, they will try their best to imitate warriors, which is amusing. \\n#~Cheap Gifts for Your Kids~'):
        "Una spada spezzata in due a metà. Sbattuta da vento e pioggia, con la lama tutta sbeccata, non vale più un briciolo; eppure, a darla a un bambino, si mette a fare il guerriero con tutto se stesso, ed è divertente. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :127855
    (127855, 'Cloth that catches the wind and flutters in the wind. It is one of the most popular products among tourists as a memento of their trip because of the variety of colors and patterns, and each town has its own unique variant. \\n#~Cheap Gifts for Your Kids~'):
        "Un telo che prende il vento e sventola. I colori e i disegni sono tanti e ogni città ha i suoi, così è uno degli articoli che piacciono ai turisti come ricordo del viaggio. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :127917
    (127917, 'A simple light with an iron cage attached to the end of a pillar to hold a flame. The rugged construction gives a somewhat wild impression. In recent years, some restaurants have installed these lighting fixtures in their restaurants to achieve this effect. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Una lampada semplice: in cima a un palo, una gabbia di ferro dove si tiene la fiamma. La fattura rozza dà un'aria un po' selvatica. Da qualche anno, pare, certe trattorie la mettono nel locale proprio per quell'effetto. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :127979
    (127979, 'A tub with dirty clothes stuck in it. It is a wonder that anyone would want such a thing, but it is said to be irresistible to a certain type of cleaning enthusiast. \\n#~Thousands of pieces of Junk I love~'):
        "Una tinozza con dentro ficcati dei vestiti sporchi. C'è da stupirsi che qualcuno voglia una cosa simile, eppure pare che per certi patiti delle pulizie sia irresistibile. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :128041
    (128041, 'A jar that is broken and can no longer be used. Some artists see some potential in them and buy them half-heartedly, even though they have no value at all. \\n#~Thousands of pieces of Junk I love~'):
        "Un vaso rotto che non si può più usare. Non vale proprio niente, ma pare che qualche artista ci veda una possibilità e lo compri quasi per sfida. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :128103
    (128103, 'Withered grass curled up in a ball. It is very hard and cannot be used as a grass substitute, but when given to children, they play with it by kicking it around with all their hearts. \\n#~Cheap Gifts for Your Kids~'):
        "Erba secca appallottolata tutta insieme. È durissima e come foraggio non va, ma dandola a un bambino, dicono, si mette a prenderla a calci senza fermarsi mai. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :128235
    (128235, 'Pieces of crushed wood. Completely useless, but it would at least be interesting to a child. \\n#~Cheap Gifts for Your Kids~'):
        "Schegge di legno spaccato. Non servono proprio a niente, ma per incuriosire un bambino bastano. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

# 26 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-040.jsonl'
RIGHE = {
    86735, 91460, 92451, 109208, 111063, 111065, 112755, 112817, 112879, 116408,
    116470, 116540, 116665, 116727, 116789, 116851, 116913, 116915, 123419, 127669,
    127731, 127733, 127793, 127855, 127917, 127979, 128041, 128103, 128235,
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
