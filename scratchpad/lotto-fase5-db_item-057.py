# -*- coding: utf-8 -*-
"""120a - Lotto 057 di `db_item.hsp`: I CONTENITORI, e la categoria CHIUDE.

`FILTER_CONTAINER`, righe da `:57125` a `:115260`: **25 righe** — 22
dell'indice 0 e 3 dell'indice 2 — su 22 oggetti. Con questo lotto
`FILTER_CONTAINER` va a **0 da fare su 25 vive**, ed e' la **dodicesima**
categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 057`: **+25** per 25 rese,
nessuna gemella. ⓘ `_gia-reso.py 057`: 0 su 25. `_code.py 057`: 0 righe senza
resa in tabella.

### ⓘ QUI SERIE NON CE NE SONO, E A DIRLO E' STATO UNO STRUMENTO

`_120-serie-bacchette.py 057` — lo strumento nato per il lotto delle bacchette
— ha risposto in un secondo: **25 righe, 24 aperture distinte, nessuna coppia
col giapponese identico**. Vale la pena scriverlo perche' e' il **valore
atteso** di quello strumento: un lotto normale non ha serie, e saperlo in un
secondo evita di cercarle a mano per venti minuti.

⭐ L'unica coppia e' `:103233` / `:103295`, le due sfere del tesoro: stessa
frase, e cambia il nome della speranza che ci sta dentro — 「欲望」 la **brama**
nella sfera rara, 「期待」 l'**attesa** in quella normale. Le due rese cambiano
quella parola e nient'altro.

### ⚠️⚠️ OTTO CODE SU VENTICINQUE LE AVEVO SCRITTE A MEMORIA, E OTTO ERANO SBAGLIATE

Scrivendo le rese ho ricostruito i titoli-fonte **a senso** dal giapponese,
invece di copiarli dall'uscita di `_code.py`. Tutti e otto erano plausibili e
tutti e otto diversi da quelli in tabella:

    «Alla Faccia della Chiusura! Box Mania, Numero Primo»
                              -> «Chiudeteci Pure! Box Mania, Numero Uno»
    «Manuale dei Giochi: Edizione per Tutte le Età»
                              -> «Grande Compendio dei Giochi: Per Tutte le Età»
    «Cose Belle da Ricevere in Regalo» -> «Regali che Fa Piacere Ricevere»
    «Libro da Donare a Chi Sta per Morire» -> «Libro in Dono a Chi Sta Morendo»
    «I Cinquanta Articoli Più Amati dai Carcerati»
                              -> «I 50 Prodotti Preferiti dai Detenuti»
    … e altre tre.

⚠️ **Il preflight non le prende**: guarda la spaziatura e la struttura, non il
testo del titolo. A prenderle sarebbe stato `_112-corpo-descrizioni`, il cui
«titoli resi in PIU' modi» sarebbe salito da 7 a **15** — ma solo *dopo* il
reimporta, cioe' dopo aver messo nel dizionario quindici titoli doppi.

⭐ **`_code.py` esiste esattamente per non farlo, e io non l'ho letto.** La
regola non e' «stare piu' attento»: e' che i titoli si **copiano** dall'uscita
dello strumento, come le righe si copiano dal template. Un titolo somiglia
abbastanza al giusto da non insospettire chi lo rilegge.

### ⓘ Tre punti dove l'inglese e il giapponese non dicono la stessa cosa

  - `:57127`, la lettera nella busta misteriosa. はく製 nel dizionario e' la
    **statuetta** — l'oggetto che il giocatore raccoglie ed espone — e ユニーク
    sono le creature **uniche** del gioco: la lettera ringrazia per una
    collezione di statuette di personaggi unici aperta al pubblico. L'inglese
    scrive «fossils», che non e' ne' l'una ne' l'altra cosa;
  - `:78658`, il pacchetto di carte. Il giapponese dice **una** cosa (le carte
    dentro non mostrano l'immagine finche' non le metti nel mazzo); l'inglese
    ci **aggiunge** «Pack of 5 collectible cards», che nell'indice 0 non c'e'.
    Il conto delle cinque sta nell'indice 3, gia' reso: dirlo due volte lo
    farebbe leggere due volte nello stesso pannello;
  - `:115260`, le parole del guardiano della gilda dei ladri. マスター e' **il
    maestro** della gilda, un personaggio del gioco; l'inglese scrive «a
    gentleman» e la battuta perde la persona — la prima volta che il guardiano
    si e' stupito e' stato per il **proprio capo**.
  - ⓘ E `:107114`: il giapponese dice che la magia della borsa mette addosso
    不安, **inquietudine**; l'inglese dice «guilty», colpa. Sono due cose
    diverse, e la resa segue il giapponese.

### ⓘ Un nome che l'inglese perde e che la tabella aveva gia' recuperato

`:112196`, il portafoglio: chi parla e' ならずもののオネスト, «**Onest** il
farabutto», e il nome **e'** la battuta — uno che si chiama Onesto e raccoglie
portafogli altrui. L'inglese lo cancella e ci mette un punto interrogativo
(«words of the honest? rogue»). La tabella dei titoli lo aveva gia' ripescato
in una sessione passata, e la resa ci si appoggia.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :57125
    (57125, 'Envelope made of thick brown paper. The sender is not written, but a letter is attached. \\n# ~Gifts that I am Happy to Receive~'):
        "Una busta fatta di carta marrone e spessa. Chi la manda non c'è scritto, ma insieme c'è una lettera. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :57127
    (57127, '\\"Thank you for generously opening up your unique collection of fossils to the public. They are things that we would not be able to see if we lived in a straight life, and they excite me every day. Keep up the good work in collecting these unique finds!\\" \\n# ~words of an Fossil Enthusiast~'):
        "\\\"La ringrazio d'aver aperto al pubblico, con tanta generosità, le sue statuette uniche. Sono tutte cose che una vita per bene non permetterebbe di vedere, e mi emozionano un giorno sì e l'altro pure. Continui così a raccogliere statuette uniche!\\\" \\n# ~Lettera di un Fissato di Tassidermia~",

    # ---------------------------------------------------------- :78658
    (78658, 'Pack of 5 collectible cards. The contained cards have no images, but can be putted into your deck.\\n# ~Heated Duelists~'):
        "Le carte che ci sono dentro non mostrano l'immagine finché non le metti nel mazzo.\\n# ~Duellanti Ardenti~",

    # ---------------------------------------------------------- :80736
    (80736, 'In some regions, it is customary to give gifts to acquaintances at the beginning of the year. The gifts are filled with good things for those who are close to the recipient, but on the other hand, for those who are not so close to the recipient, a prank is sometimes played on the recipient. It is said that some people become a good person on all sides just for this reason. \\n# ~Gifts that I am Happy to Receive~'):
        "In certe zone c'è l'usanza di farne dono ai conoscenti all'inizio dell'anno. A chi si è amici ci si mette dentro roba buona in proporzione; a chi lo si è meno, invece, capita che ci si nasconda uno scherzo. Si dice che ci sia chi, solo per questo, si mette a fare il gentile con tutti. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :81260
    (81260, 'Cat in a box. Whether the cat inside is alive or dead will not be known until the box is opened. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una scatola dentro cui è stato messo un gatto. Se il gatto lì dentro sia vivo o morto, non lo si saprà finché non si prova ad aprirla. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :81941
    (81941, '\\"A great experience for a handful of lucky people! Please bring your lockpicks to the challenge.\\" \\n# ~note written on the back of the box~'):
        "\\\"Un'esperienza sublime per una manciata di fortunati! Chiunque voglia tentare, si presenti col grimaldello\\\" \\n# ~Avvertenza Scritta sul Retro della Scatola~",

    # ---------------------------------------------------------- :88147
    (88147, 'A mechanical box that allows food to be stored without spoiling. Extremely useful item, but only holds four kinds of food, so beware if you are going on a picnic with a lot of people. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una scatola a ingranaggi, che conserva il cibo senza farlo marcire. È comodissima, ma ci stanno solo quattro qualità di cibo: attenzione, quando si va a far merenda in molti. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :89821
    (89821, 'Special box for payment of designated taxes. Visit the Palmia Embassy to pay tax once a month. \\n# ~Censored! Box Mania, First Issue~'):
        "Una scatola apposita, per versare le tasse dovute. Una volta al mese conviene fare un salto all'ambasciata di Palmia. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # ---------------------------------------------------------- :90832
    (90832, 'Huge, sturdy fetters made of metal. It does not seem to be affected by pushing or pulling, but the joints seem to be a little loose. \\n# ~Top 50 Most Popular Products Among Prisoners~'):
        "Un ceppo di metallo, enorme e saldo. A spingerlo o a tirarlo pare non muoversi di un dito, eppure a guardarlo bene la giuntura sembra un po' allentata. \\n# ~I 50 Prodotti Preferiti dai Detenuti~",

    # ---------------------------------------------------------- :92186
    (92186, 'A work of wisdom that can store foodstuffs semi-permanently. However, there is a secret to this furniture. No matter how many units you own, their doors can only lead to the same space! \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un frutto dell'ingegno, che conserva gli ingredienti quasi per sempre. C'è però un segreto in questo mobile: per quanti se ne posseggano, oltre lo sportello si arriva sempre e solo allo stesso spazio! \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :93420
    (93420, "A special safe that takes care of all the store's sales. For security purposes, the system is such that it can never be opened outside of the store. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~"):
        "Una cassaforte apposita, che raccoglie tutto l'incasso del negozio. Contro i furti, è congegnata in modo da non aprirsi mai fuori dal negozio. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :93422
    (93422, 'A safe is essential to running a store. This is where all sales proceeds are stored. \\"If you lose it by accident, don\'t worry. Everything is available at the Palmia Embassy, the keystone of the economy.\\" \\n# ~Tyris Armor Compendium, page of advertisements~'):
        "Una cassaforte indispensabile per mandare avanti un negozio. Qui dentro finisce tutto l'incasso. \\\"Se un incidente ve la fa perdere, state tranquilli: all'ambasciata di Palmia, cardine dell'economia, si trova tutto\\\" \\n# ~Grande Compendio delle Armi di Tyris: le Reclame~",

    # ---------------------------------------------------------- :93483
    (93483, 'A special box for the delivery of designated items. It is said that a little effort is made at the slot to prevent wrong everything from being dumped. \\n# ~Censored! Box Mania, First Issue~'):
        "Una scatola apposita, per consegnare la merce richiesta. Pare che la fessura abbia qualche accorgimento, perché non ci si butti dentro di tutto. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # ---------------------------------------------------------- :94381
    (94381, 'A box to receive the earned salary twice a month. Even if the box is lost due to unforeseen circumstances, the salary will be properly transferred. But remember that Palmia officials are inflexible, you need to buy another box from them. \\n# ~Censored! Box Mania, First Issue~'):
        "Una scatola per ritirare la paga, due volte al mese. Anche se un imprevisto la fa perdere, la paga viene versata lo stesso; conviene però ricordarsi che i funzionari di Palmia non fanno sconti a nessuno. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # ---------------------------------------------------------- :96844
    (96844, 'An old briefcase. Inside the briefcase are items left behind by those who left the continent in the midst of their ambitions. To receive them, one must follow the proper procedures. \\n# ~Book for the Dying Ones~'):
        "Una borsa vecchiotta. Dentro ci stanno le cose lasciate da chi se n'è andato dal continente a metà del cammino. Per averle bisogna passare per la trafila dovuta. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :103233
    (103233, "Sphere containing some item. Inside it is filled with hope in the name of 'desire'. \\n# ~Game Tricks, All Ages Version~"):
        "Una sfera in cui è stato riposto un oggetto qualunque. Dentro ci sta stipata una speranza che porta il nome di \\\"brama\\\". \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :103295
    (103295, "Sphere containing some item. Inside it is filled with hope in the name of 'expectation'. \\n# ~Game Tricks, All Ages Version~"):
        "Una sfera in cui è stato riposto un oggetto qualunque. Dentro ci sta stipata una speranza che porta il nome di \\\"attesa\\\". \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :104725
    (104725, 'A black box that pops out materials when opened. A wide variety of items pop out all at once, but no one knows how they fit into this box. \\n# ~Censored! Box Mania, First Issue~'):
        "Una scatola nera da cui, ad aprirla, saltano fuori i materiali. Ne esce di tutto in una volta sola, e si dice che come ci stiano dentro non lo sappia nessuno. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # ---------------------------------------------------------- :107114
    (107114, 'A briefcase filled with the best goods that a peddler has worked tirelessly to collect. For security purposes, the bag is said to be enchanted with a spell that makes people feel extremely guilty if anyone other than the registered owner opens it. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~'):
        "Una borsa piena dei pezzi pregiati che un mercante ambulante ha raccolto con la propria fatica. Contro i furti, si dice porti addosso una magia che a chi la apre, e non sia l'intestatario, mette dentro un'inquietudine fortissima. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :112196
    (112196, '\\"Oh, I found a wallet here. Good, I was worried it might be lost. You say I look familiar? That\'s right, \'cause I have a lot of wallets.\\" \\n# ~words of the honest? rogue~'):
        "\\\"Oh, un portafoglio qui. Meno male, ero in pena perché credevo d'averlo perso. Dici che somiglia a quello che hai perso tu l'altro giorno? Ma certo che sì: è perché di portafogli io ne ho tanti\\\" \\n# ~Parole di <Onest> il farabutto~",

    # ---------------------------------------------------------- :112258
    (112258, '\\"This bag belongs to me. No, I used to have it. No, I remember I had it, no, I wanted to buy it - no, wait. Oh yes, I remember, it was a bag that some old gentleman put there. In other words, it belonged to me.\\" \\n# ~words of <Gleed> the thief~'):
        "\\\"Questa borsa è mia. Anzi no, ce l'avevo tempo fa. Anzi, mi ricordo d'averla avuta; anzi, la volevo comprare... anzi, aspetta. Ah, ecco, mi è tornato: era la borsa che aveva posato lì un vecchio signore. E dunque è mia\\\" \\n# ~Parole di <Gleed> il topo d'appartamento~",

    # ---------------------------------------------------------- :115134
    (115134, '\\"Is there hope inside, or is it despair? I guess the only thing I know is that for those who keep it, it\'s all despair.\\" \\n# ~words of <Marks> the great thief~'):
        "\\\"Dentro c'è la speranza, oppure la disperazione? L'unica cosa che si può sapere è che per chi la tiene chiusa lì non sarà altro che disperazione\\\" \\n# ~Parole di <Marks>, ladro senza pari~",

    # ---------------------------------------------------------- :115196
    (115196, 'A box containing items that are said to be mainly kept in Nephia. The boxes are made to be very heavy so that adventurers who cannot unlock them will not be able to rob them by brute force. \\n# ~Censored! Box Mania, First Issue~'):
        "Una scatola che custodisce oggetti, e che si dice stia soprattutto nelle Nefia. È fatta pesantissima, perché l'avventuriero che non riesce ad aprirla non se la porti via a forza. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # ---------------------------------------------------------- :115258
    (115258, 'A shining treasure box decorated with jewelry. Despite its appearance, it is surprisingly lightweight, and some customers seem to buy it as a glamorous accessory box. \\n# ~Censored! Box Mania, First Issue~'):
        "Un baule splendente, ornato di gioielli. Contro le apparenze è insolitamente leggero, e con quel rivestimento sfavillante pare che ci siano clienti che lo comprano per tenerci le cianfrusaglie. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

# 22 voci, 0 ambigue

    # ---------------------------------------------------------- :115260
    (115260, '\\"I\'ve been here all my life, sifting through the stolen goods, and I\'ve been surprised twice in the past. The first time was by a gentleman who brought me a golden statue of a giant god. The second time was to a man like you who brought not the contents of the treasure, but its bejeweled exterior.\\" \\n# ~words of <Abyss> the thief watchman~'):
        "\\\"Io sto qui da sempre a stimare la refurtiva, e in tutto questo tempo mi sarò stupito sì e no due volte. La prima per il maestro, che mi portò una statua d'oro di un gigante. La seconda per uno come te, che della refurtiva mi ha portato non il dentro, ma il fuori\\\" \\n# ~Parole di <Abyss> il guardiano della Gilda dei Ladri~",

# 3 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-057.jsonl'
RIGHE = {
    57125, 57127, 78658, 80736, 81260, 81941, 88147, 89821, 90832, 92186,
    93420, 93422, 93483, 94381, 96844, 103233, 103295, 104725, 107114, 112196,
    112258, 115134, 115196, 115258, 115260,
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
