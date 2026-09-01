# -*- coding: utf-8 -*-
"""121a - Lotto 059 di `db_item.hsp`: I LIBRI, e la categoria CHIUDE.

`FILTER_ITEM_BOOK`, righe da `:47220` a `:129580`: **23 righe** — 21
dell'indice 0 e 2 dell'indice 2 — su 23 oggetti. Con questo lotto
`FILTER_ITEM_BOOK` va a **0 da fare su 23 vive**, ed e' la **quattordicesima**
categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 059`: **+24 per 23 rese**. C'e'
una **gemella**, la prima da sei lotti: `:129580` (`ITEM_ID_RED_BOOK`) e
`:129651` (`ITEM_ID_BOOK`) hanno giapponese e inglese identici byte per byte —
due oggetti che si chiamano tutt'e due 本, «libro» — e una resa li copre
tutt'e due. ⓘ `:129651` **non e' nel lotto e non e' nel dossier**: la sua
esistenza la dice solo lo strumento, contando il sorgente (lezione della 116a).

### ⭐⭐⭐ QUATTRO DIARI CHE DEVONO RESTARE UGUALI, E UNO CHE DEVE RESTARE DIVERSO

Quattro righe aprono con la stessa formula, parola per parola:

    ◯がしたためたとされる日記。

    :56055  執事    -> il maggiordomo
    :71100  誰か    -> qualcuno
    :76935  姉      -> la sorella maggiore
    :89284  お嬢様  -> la signorina

La resa e' **«Un diario che si dice vergato da ◯.»** in tutte e quattro, e
cambia solo il nome. E tre di loro chiudono anche con la stessa seconda meta'
— 中には … が事細かに書かれているという — resa «Dentro, a quanto pare, … per
filo e per segno.» ⓘ したためる non e' 書く: e' il verbo formale del
*mettere per iscritto*, e «vergare» e' il suo pari in italiano.

⚠️⚠️ **E `:97200` NON e' della serie.** Il diario della sorella minore dice
妹が**書いた**日記 — il verbo comune — e la resa dice «Il diario che ha scritto
la sorella minore». A distinguerlo e' l'originale, e appiattirlo sui suoi
quattro fratelli sarebbe stato «migliorare» il testo cancellando una
differenza che l'autore ha scritto. ⭐ E' la lezione della 119a al rovescio:
li' l'inglese aveva ricopiato righe che dovevano differire, qui il rischio era
uniformare righe che l'inglese tiene distinte per caso e il giapponese per
scelta.

⭐ **I due diari segreti** — `:76791` la sorella cane maggiore, `:89356` la
sorella gatta minore — hanno la seconda meta' **identica byte per byte** in
giapponese. Le due rese cambiano «maggiore»/«minore» e nient'altro: i due
oggetti stanno uno accanto all'altro nell'inventario di chi li colleziona.

### ⭐⭐⭐ UN SEGMENTO CHE ESISTE SOLO IN INGLESE, E NON E' UNA RINVIATA

`:89358`, `description(2)` del diario segreto della sorella gatta.

    db_item.hsp:89352   description(2) = ""                       <- ramo jp
    db_item.hsp:89358   description(2) = "\\"Nyo reading!\\" ..."   <- ramo en

Il giapponese **non c'e'**: e' la stringa vuota, non una frase mancante.
⚠️ La tentazione e' trattarlo come `:129299`, la rinviata della 119a. **Non e'
lo stesso caso, e la differenza sta scritta nella rinviata stessa**: li' il
testo non ce l'aveva *nessuna delle due lingue* («la riga non ha testo in
nessuna delle due lingue»), e una resa avrebbe inventato. Qui l'inglese un
testo ce l'ha, e vale il precedente della 110a — *il giapponese vuoto e
l'inglese pieno: la riga si rende*.

⭐ E il bisticcio si puo' rendere perche' il gioco lo ha gia' reso altrove:
«Nyo reading!» e' il gatto che dice «no», e il tic della sorella gatta nel
dizionario e' **«miao»** in coda alla frase («E va bene, miao!», «Basta che tu
abbia capito, miao»). La resa e' «Vietato leggere, miao!».
ⓘ ⚠️ Altrove il progetto fa il contrario e **butta** il gatto inglese: le
battute di Mia («Nyobody knyows...») sono rese dal giapponese, che di gatto non
ha niente. Non e' incoerenza: e' che li' un giapponese c'era.

### ⭐⭐ CAIN NON ESISTE: SI CHIAMA CAIM

`:74101`, il diario del folle. Il giapponese dice 発狂したカイン, l'inglese
«a mad man named **Cain**» — e chi rende dall'inglese scrive Cain.

Il personaggio in gioco e' `<Caim> il riccone folle` (`<Caim> the mad rich`), e
il dizionario lo chiama **Caim** in tutte le sue voci. L'inglese di questa riga
e' l'unico posto dove compare la n.
⚠️ Nessuna rete lo vede: e' un nome plausibile, ed e' anche un nome vero.

### ⓘ Altri quattro punti dove il giapponese comanda

  - `:81064`, il libro di Bokonon: 真実であり、真っ赤な嘘である e' l'epigrafe
    dei *Libri di Bokonon* di Vonnegut, che in italiano suona «spudorate
    menzogne». ⚠️ L'inglese butta la seconda meta' e ci mette «granfalloon»,
    che il giapponese non nomina;
  - `:71100`, il diario di qualcuno: il giapponese dice **tre** cose (il nome
    non sta in copertina, non si sa di chi sia finche' non lo apri, e girano
    voci su un autore raro dopo una dozzina di letture); l'inglese ne tiene
    **una e mezza** e salta la seconda;
  - `:56201`: 開発主任 non e' «un capo progetto», e' `<Gavela> l'ingegnere
    capo`, un personaggio che il giocatore incontra;
  - `:86403`: レイチェル e' **Rachel**, ed e' una **donna** — «la scrittrice di
    favole Rachel», «una raccolta di fiabe che scaldano il cuore, firmata
    Rachel» — e i volumi sono quattro, come dice l'incarico di Renton.

### ⚠️⚠️ LA SPAZIATURA QUI NON E' UNIFORME IN NESSUNO DEI DUE PUNTI

Primo lotto della serie in cui `_forma.py` stampa due liste **diverse**:

    senza lo spazio prima del \\n : :47220  :57577  :71100  :93292
    senza lo spazio dopo il #    : :47220  :47222  :57577  :83697

⚠️⚠️ **E io ho letto «senza lo spazio prima del `\\n`» come «senza il `\\n`».**
Quattro rese sono uscite dal montaggio con la coda attaccata al punto finale, e
il segmento in meno. **`_preflight034.py` le ha prese tutte e quattro** —
«segmenti diversi: en 1, it 0» — prima del reimporta e prima della build.
⭐ E' il punto 3 del preflight, quello scritto nella 115a per un guasto
diverso, che qui ha pescato un errore di lettura di chi scrive le rese: la
riga di `_forma.py` dice due cose e io ne ho letta una.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :47220
    (47220, 'It is said to appear before those who are on the same wavelength. It is not cold, but when you hold it in your hand, you feel an unusual chill down your spine, as if your soul is being grabbed. The pages are all black and translucent, but strange characters appear when reflected in the light. Some believe that they are made of a material that is not of this world, and that they are not books at all, but windows into the abyss.\\n#~Irva Fantasy Encyclopedia~'):
        "Si dice che compaia davanti a chi ha la sua stessa lunghezza d'onda. Freddo non è, eppure a tenerlo in mano la schiena si gela in modo innaturale, e ti prende la sensazione che qualcuno ti stringa l'anima nel pugno. Le pagine sono tutte nere e semitrasparenti, ma alla luce vi affiorano caratteri strani. È fatto di una materia che non è di questo mondo, e c'è chi sostiene che in verità non sia un libro, ma una finestra che riflette l'Abisso.\\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :47222
    (47222, '\\"I was being used.\\" \\n# a Punched-in note'):
        "\\\"Io... ero solo uno strumento\\\" \\n#~Scarabocchio sul Foglietto Infilato Dentro~",

    # ---------------------------------------------------------- :50816
    (50816, 'Recording medium widely circulated in North Tyris. If anything, the volume tends to be more important than the content, you can sell them at shops to raise your fame. \\n# ~Big Book of Books~'):
        "Un supporto di registrazione che a Tyris del Nord circola parecchio. Semmai, più del contenuto tende a contare il volume. A darlo a un negozio, la fama dell'autore salirà. \\n# ~Il Libro dei Libri~",

    # ---------------------------------------------------------- :51150
    (51150, 'A book written by an angler to increase the number of his fishing buddies. He made good use of his waiting time for fishing to write the book. \\n# ~Big Book of Books~'):
        "Un libro che un pescatore ha scritto per farsi più compagni di pesca. Pare che a scriverlo abbia messo a frutto le attese fra un pesce e l'altro. \\n# ~Il Libro dei Libri~",

    # ---------------------------------------------------------- :51221
    (51221, 'A notebook prepared by a concerned father. He was worried about his child and slipped it into their luggage. The notebook was found beside the bulletin board, although it is unclear whether he dropped it, threw it away, or forgot about it. \\n# ~Big Book of Books~'):
        "Un taccuino che un padre aveva preparato. Pare che, in pensiero per il figlio, gliel'avesse infilato di nascosto nei bagagli. Se sia caduto, buttato o dimenticato non si sa: stava lì accanto alla bacheca. \\n# ~Il Libro dei Libri~",

    # ---------------------------------------------------------- :56055
    (56055, "A diary said to have been written by a butler. It is said that inside the diary are more detailed descriptions of the master's life than his own. \\n# ~Big Book of Children's Books~"):
        "Un diario che si dice vergato dal maggiordomo. Dentro, a quanto pare, la vita del padrone è raccontata per filo e per segno più della sua. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :56201
    (56201, 'Report written by the chief developer. They were going to start R&D with this as a starting point, but unfortunately, they did not get the budget. \\n# ~Big Book of Books~'):
        "Un rapporto scritto dall'ingegnere capo. Da qui voleva partire per aprire una ricerca, ma pare che il budget, purtroppo, non sia mai arrivato. \\n# ~Il Libro dei Libri~",

    # ---------------------------------------------------------- :57577
    (57577, "This is a photograph collection of sexy pictures of Lulwy. It is so excessive that the eye is involuntarily drawn to it regardless of one's tastes. The photographer published the book and continued to sell it until it was banned. They later proposed a second volume, but inadvertently offended Lulwy and became food for the sylphs.\\n#~Big Book of Adult Books~"):
        "Un album di foto in cui le immagini sexy di Lulwy sono stipate a non finire. Così spinte che l'occhio ci cade da solo, quali che siano i gusti. Lo pubblicò un fotografo che una volta era riuscito a metterla di buon umore, e si dice che abbia continuato a venderlo finché non fu proibito. Più tardi il fotografo propose un secondo volume, ma le guastò l'umore per sbadataggine e finì in pasto alle silfidi.\\n#~Il Libro dei Libri: le Riviste per Adulti~",

    # ---------------------------------------------------------- :62534
    (62534, 'Notebook of a researcher who was dissatisfied with his institute. It contains the activities of the people around him, along with his complaints. \\n# ~Big Book of Books~'):
        "Il taccuino di un ricercatore che non era contento dell'istituto per cui lavorava. Ci sono annotate le malefatte di chi gli stava intorno, e i lamenti che ne faceva. \\n# ~Il Libro dei Libri~",

    # ---------------------------------------------------------- :71100
    (71100, "A diary written by someone unknown. There is a rumor that an unusual author appears after reading a dozen or more.\\n# ~Big Book of Children's Books~"):
        "Un diario che si dice vergato da qualcuno. Di regola sulla copertina il nome non c'è, e finché non si guarda dentro non si sa di chi sia. Corre voce che, letta una dozzina abbondante di copie, salti fuori un autore raro.\\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :74101
    (74101, 'Diary written by a mad man named Cain. I think it describes the truth he learned at the end of his madness.... \\n# ~Big Book of Books~'):
        "Il diario che <Caim>, impazzito, ha scarabocchiato. Ci sta scritta la verità che in fondo alla sua follia ha conosciuto... o almeno così sembra. \\n# ~Il Libro dei Libri~",

    # ---------------------------------------------------------- :76791
    (76791, "A diary in which one's older sister's secrets are hidden. It is said that things which can never be said with words, are written in the diary, which has caused a stir among researchers. \\n# ~Big Book of Children's Books~"):
        "Un diario in cui la sorella maggiore ha nascosto i suoi segreti. Si dice contenga quelle cose lì che a voce non si dicono mai, e gli studiosi sono in agitazione. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :76935
    (76935, "A diary said to have been written by an older sister. It is said that her hardships and feelings are described in detail in it. \\n# ~Big Book of Children's Books~"):
        "Un diario che si dice vergato dalla sorella maggiore. Dentro, a quanto pare, le sue fatiche e i suoi sentimenti sono raccontati per filo e per segno. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :81064
    (81064, 'A religious book put up by a group of people who are said to be very eccentric. When you open its pages, you will know the truth of the world, and perhaps understand a granfalloon. \\n# ~Big Books of Historical Books~'):
        "Il libro sacro che innalza una congrega ritenuta stranissima. Aprendone le pagine saprai che quel che vi sta scritto è la verità, ed è una menzogna spudorata. \\n# ~Il Libro dei Libri: i Libri di Storia~",

    # ---------------------------------------------------------- :83697
    (83697, 'A precious book that is said to bring back lost beings. Ironically, there was a great war over this book in ancient times, and many lives were lost. \\n#~Big Book of Magical Books~'):
        "Un libro prezioso che si dice richiami indietro chi è andato perduto. Per ironia, nell'antichità intorno a questo libro ci fu una grande guerra, e si dice che molte vite andarono perdute. \\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :84233
    (84233, 'This is a book that describes the state of affairs in the town. However, since North Tyris respects freedom, it is said that this book, which describes the system, has become useless. \\n# ~Big Books of Historical Books~'):
        "Un libro in cui è scritto come vanno le cose in città. Siccome però a Tyris del Nord si tiene alla libertà, pare che questo libro, che descrive dei regolamenti, sia diventato un ingombro inutile. \\n# ~Il Libro dei Libri: i Libri di Storia~",

    # ---------------------------------------------------------- :86403
    (86403, "A collection of children's stories by Rachel, a writer of children's stories. The unique warmth of the text and illustrations is said to give readers something that touches their hearts. There are four volumes in total, but they are very hard to find. I am sure there are people in the world who would love to read them. \\n# ~Big Book of Children's Books~"):
        "La raccolta di fiabe che ha fatto Rachel, la scrittrice di favole. Si dice che la scrittura e le illustrazioni, con quel loro calore tutto particolare, diano a chi legge qualcosa che tocca il cuore. I volumi sono quattro in tutto, ma metterli insieme è impresa difficilissima. Al mondo ci sarà di sicuro qualcuno che muore dalla voglia di leggerli. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :89284
    (89284, "A diary said to have been written by a young lady. It is said that inside the diary are detailed descriptions of her glittering life and some of her lovely hobbies. \\n# ~Big Book of Children's Books~"):
        "Un diario che si dice vergato dalla signorina. Dentro, a quanto pare, la sua vita sfavillante e qualcuno dei suoi passatempi graziosi sono raccontati per filo e per segno. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :89356
    (89356, "A diary in which the secrets of a younger sister are hidden. It is said that such and such things that can never be said in words are written in it, and it has caused a stir among researchers. \\n# ~Big Book of Children's Books~"):
        "Un diario in cui la sorella minore ha nascosto i suoi segreti. Si dice contenga quelle cose lì che a voce non si dicono mai, e gli studiosi sono in agitazione. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :89358
    (89358, '\\"Nyo reading!\\" \\n# ~words on the cover~'):
        "\\\"Vietato leggere, miao!\\\" \\n# ~parole sulla copertina~",

# 2 voci, 0 ambigue

    # ---------------------------------------------------------- :93292
    (93292, "Books that can be read to train the skills described in them. In remote villages where there are no schools, these books are said to be a substitute for teachers.\\n# ~Big Book of Books: Teacher's Edition~"):
        "Un libro che, a leggerlo, allena l'abilità di cui parla. Si dice che nei villaggi di confine, dove una scuola non c'è, libri come questo facciano le veci del maestro.\\n# ~Il Libro dei Libri: i Manuali d'Insegnamento~",

    # ---------------------------------------------------------- :97200
    (97200, "A diary written by a younger sister. In it, she writes about her daily feelings, recent favorites, delicious food, etc. in two days' skips. \\n# ~Big Book of Children's Books~"):
        "Il diario che ha scritto la sorella minore. Dentro ci sono le cose che sente giorno per giorno, quel che le piace di questi tempi, i cibi che ha trovato buoni: e scrive saltando due giorni per volta. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :129580
    (129580, 'Recording medium widely circulated in North Tyris. Some of them contain important information, but most of them are just scraps of information that are not worth reading. \\n# ~Big Book of Books~'):
        "Un supporto di registrazione che a Tyris del Nord circola parecchio. Ce n'è qualcuno in cui sta scritto qualcosa d'importante, ma quasi tutti valgono sì e no quanto un appunto a margine. \\n# ~Il Libro dei Libri~",

# 21 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-059.jsonl'
RIGHE = {
    47220, 47222, 50816, 51150, 51221, 56055, 56201, 57577, 62534, 71100,
    74101, 76791, 76935, 81064, 83697, 84233, 86403, 89284, 89356, 89358,
    93292, 97200, 129580,
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
