# strumenti/menu_dialogo.py
"""Il tetto di una voce del menu del dialogo, misurato a schermo il 2026-08-17.

La finestra del dialogo aveva **due** tetti e ne era misurato uno solo. La rete
14 della 54a misura l'**altezza** — dodici righe di descrizione — e nel farlo ha
lasciato scoperta la **larghezza delle voci**, che e' un'altra geometria e un
altro riquadro. Il collaudo della 55a l'ha trovata rotta alla seconda schermata:

    [5500 biglietti] Carta del dio-di-carta-piegata-segretissimo <Kamikakushi>.

a schermo si fermava su «segretissimo», ventuno caratteri prima della fine.

## Da dove viene il numero

⚠️ **Non da un `sdim`.** `chatList` scrive in `listn(0, listmax)`, dichiarato
`sdim listn, 40, 2, 500` (`init.hsp:2428`), e a schermo se ne leggono una
sessantina: e' la terza volta in tre giorni che un `sdim` di questo progetto
sembra un tetto e non lo e'. Il tetto e' il **riquadro**, e si misura in pixel.

    chat.hsp:25232   ww = 600                        la finestra
    chat.hsp:25160   x = wx + 136                    dove comincia la voce
    chat.hsp:25177   cs_list listn(0,cnt), x + 30    il testo, 30 px piu' in la'
    module.hsp:129   pos arg2 + 4 ... : mes          e altri 4

Il testo parte a `wx + 170`. L'interno della pergamena finisce a `wx + 577`,
misurato sulla schermata del 2026-08-17 (finestra intera, 1920x1080, `wx = 660`,
ultimo pixel di pergamena a 1237). Restano **407 px**.

### ⚠️⚠️ Il passo del carattere e' 7, non 7,7 (corretto il 2026-08-18)

Per un giorno qui c'e' stato scritto **7,7**, e il tetto era 52 invece di 58.
Il numero veniva da sei voci misurate a schermo il 2026-08-17:

    47 caratteri -> 357 px    7,60      43 -> 331    7,70
    46           -> 350       7,61      42 -> 331    7,88
    47           -> 357       7,60      40 -> 308    7,70

⚠️ **Quelle sei misure sono giuste; sbagliato e' il conto che ci si e' fatto
sopra.** Non e' il rapporto che va preso, e' la PENDENZA. Fra la prima e
l'ultima ci sono 7 caratteri e 49 pixel: **7,00 esatti**. Il rapporto esce 7,7
perche' ogni misura porta dentro anche un **pezzo fisso** che non dipende dalla
lunghezza, e dividendolo per il numero di caratteri lo si spalma sui caratteri:
32 px spalmati su 47 fanno proprio 0,68.

💡 Il pezzo fisso ha un nome nel sorgente. `module.hsp:70`, dentro `cs_list`:

    locvar_cs_list_tx = limit(strlen(cs_list_arg1) * 7 + 32 + cs_list_arg5, 10, 480)

cioe' **il gioco stesso conta 7 px per carattere**, piu' 32 di contorno. Le sei
misure del 2026-08-17 non misuravano il testo: misuravano la **barra
evidenziata**, che e' il testo piu' quei 32.

✅ Confermato tre volte sulla schermata del lupo mannaro del 2026-08-18
(`event.hsp:521`, sfondo `bg_re9`, la voce inglese da 48 caratteri):

    l'avanzamento fra l'inizio di una parola e l'inizio della successiva vale
    7,00 px per carattere su tutti e 37 i caratteri misurabili
    (murdered a 965 = 847 + 17x7, someone a 1029 = 847 + 26x7, cold a 1106
    = 847 + 37x7)

    la barra evidenziata comincia a wx+60 = 843 e il sorgente la vuole larga
    48x7 + 32 = 368: prevista fino a 1210, misurata fino a 1210

    il bordo interno della pergamena cade a wx + dx - 12 = 1127, e la beige
    finisce a 1124-1126

⚠️ **E il 7,7 di `larghezze.py` resta giusto: e' un altro carattere.**
`*prompt_key` disegna con `font ..., 15 - en * 2` (`system.hsp:4259`), cioe' 13;
questa finestra e la pergamena con `font ..., 14 - en * 2`
(`chat.hsp:25149`, `event.hsp:4173`), cioe' **12**. Il rapporto torna: 13/12 =
1,083 contro 7,7/7 = 1,10. E il 7,7 di la' non e' un rapporto ma un **taglio
osservato** — 300 px che tagliavano a 33 caratteri.
💡 La lezione non e' sul numero: e' che questa rete aveva preso una costante da
un'altra dicendo «e' lo stesso carattere» senza verificarlo, e nessun test
poteva accorgersene perche' i test fissavano il numero, non la sua provenienza.

    407 / 7 = 58 caratteri

⚠️ **`cs_list` non taglia.** Fa `mes` (`module.hsp:130`), e la cornice e' gia'
stata disegnata (`chat.hsp:25256` prima di `:25177`): quel che sfora finisce
stampato **sopra** il bordo decorato. Non e' un troncamento pulito, e' un
pasticcio.

## Due geometrie che questa rete NON copre, e vanno sapute

⚠️⚠️ **Sopra le dieci voci il menu passa a due colonne e tronca a 24 caratteri
netti** (`chat.hsp:25166`):

    if ( keyrange > 10 & (cnt >= 10 | cnt < keyrange - 10) ) {
        listn(0, cnt) = strmid(listn(0, cnt), 0, 24)
    }

Quello si', e' un `strmid`. Ma `keyrange` e' il numero di voci **a tempo di
esecuzione**, che dipende dai rami percorsi: non si legge dal sorgente, e questa
rete non prova a indovinarlo. Il negozio delle carte si salva perche' impagina a
sette set piu' tre voci di servizio, dieci esatte.

💡 E la finestra larga (`evochat >= 2`, `ww = 1480`, testo a `wx + 100`) ha molto
piu' spazio: il tetto qui e' quello **stretto**, cioe' il conservativo. Una voce
che ci sta, ci sta in tutt'e due.

## ⚠️⚠️ Un `chatList` non e' sempre nella pergamena (corretto il 2026-08-18)

Per un giorno questa rete ha applicato **52 a tutte** le voci di menu del gioco,
e non era vero: `chatList` riempie una lista, ma **chi la disegna** e' il `gosub`
che viene dopo, e i posti sono piu' d'uno. Contate sul sorgente:

    chat_select        1240 righe   la pergamena del dialogo, tetto 58
    re_select           177         la finestra dell'evento, tetto 40-56
    talk_quest          148         non misurato
    com_txtadv_loop      46         non misurato
    altri                 9         non misurato

⚠️ **`*re_select` (`event.hsp:4119`) e' un'altra geometria**, e il suo tetto non
e' nemmeno una costante: dipende dal **BMP di sfondo** dell'evento.

    event.hsp:4153   dx = tx + 36                  tx = larghezza del bmp
    event.hsp:4195   cs_list q, wx + 60, ...       dove comincia la voce
    module.hsp:129   pos arg2 + 4 ... : mes        e altri 4

Il bordo interno destro sta a `dx - 12`, simmetrico ai `wx + 12` del `gcopy` di
`:4165`. Quindi `(tx + 36 - 12 - 64) / 7`, che sui bitmap veri va da **40**
(`bg_re15`, 280 px) a **56** (`bg_re20`, 392 px). Una voce da 45 caratteri col
tetto sbagliato passava e a schermo sfondava di nove.
✅ Misurato prima di correggere (`scratchpad/misura-re-select.py`): delle 32
voci gia' tradotte dentro `*re_select` non ne sforava nessuna. La correzione non
ripara un danno — **toglie un permesso** che nessuno aveva ancora usato.

⚠️ **E quel che non si sa misurare si CONTA, non si misura a occhio.** Per
`talk_quest` e `com_txtadv_loop` la geometria non e' stata letta: quelle voci
escono dal conto degli sfori ed entrano in un conto loro, che il referto stampa.
Applicare 58 «tanto per avere un numero» e' come il filtro furbo di
`custom_dmgpop.hsp` — non prova niente, e fa credere di aver guardato.

💡 **Il contenitore si trova guardando avanti fino al primo `gosub`, senza
limite di righe**, fermandosi su un'etichetta o su un `return`. Un limite di
sessanta righe lasciava 208 voci senza risposta: il negozio delle carte impagina
**253** righe di menu prima del suo `gosub *chat_select` (`tcg_custom.hsp:1968`
-> `:2221`). Se ci si ferma su un'etichetta, quella etichetta **e'** il
contenitore: sono i tre menu che si ridisegnano dentro il proprio ciclo.
"""
import json
import re
import struct
import sys
from pathlib import Path

from strumenti import percorsi
from strumenti.accenti import degrada

# la geometria, letta dal sorgente
INIZIO_TESTO = 170       # wx+136 (chat.hsp:25160) + 30 (:25177) + 4 (module.hsp:129)
FINE_PERGAMENA = 577     # misurato a schermo il 2026-08-17
PIXEL_UTILI = FINE_PERGAMENA - INIZIO_TESTO

# ⚠️ corretto il 2026-08-18 da 7,7 a 7: vedi il docstring. Il 7,7 di
# larghezze.py e' il carattere da 13 di *prompt_key, non questo, che e' da 12.
PIXEL_PER_CARATTERE = 7

# cifre supposte per un prezzo interpolato. ⚠️ `larghezze.py` ne suppone tre; qui
# sono **quattro** perche' il set piu' caro del negozio costa 5500 biglietti, e
# su un tetto stretto un carattere e' la differenza fra dentro e fuori.
LARGHEZZA_NUMERO = 4

TETTO = int(PIXEL_UTILI / PIXEL_PER_CARATTERE)

# --- il SECONDO tetto della pergamena: le due colonne (chat.hsp:25166)
#
# ⚠️⚠️ **La pergamena ha due tetti, non uno.** Sopra le dieci voci il menu passa
# a due colonne (`x = wx + 136 + cnt / 10 * 216`, `chat.hsp:25164`) e il gioco
# **taglia con `strmid` a 24 caratteri**:
#
#     if ( keyrange > 10 & (cnt >= 10 | cnt < keyrange - 10) ) {
#         listn(0, cnt) = strmid(listn(0, cnt), 0, 24)
#
# Il conto torna con la geometria: la colonna e' larga 216 px, il testo comincia
# 34 px dentro (30 di `cs_list` piu' 4 di `module.hsp:129`), restano 182 px che
# a 7 px per carattere fanno 26 — e upstream taglia due caratteri prima.
#
# ⚠️ **Non e' un tetto che vale sempre**: dipende da QUANTE voci ha il menu di
# quel PNG, che dipende dal ruolo, dalla trama e dai compagni. Un negoziante ne
# mostra sette e sta in una colonna; un compagno ne supera dieci. Non e'
# decidibile dal sorgente, e per questo la regola qui non e' «≤ 24» ma:
#
#     ⭐ **se l'inglese di monte ci sta in 24, l'italiano ci deve stare.**
#
# Cosi' la rete non chiede di mutilare le voci che upstream stesso lascia
# tagliare, e ferma soltanto le nostre regressioni. 💡 E' la stessa forma di
# `fuori_misura_inglese`: il metro non e' l'inglese, ma l'inglese dice da dove
# viene il danno.
TETTO_DUE_COLONNE = 24

# --- la geometria di *re_select, letta da event.hsp:4145-4195
CORNICE_RE_SELECT = 36   # dx = tx + 36            (event.hsp:4153)
INIZIO_VOCE_RE_SELECT = 64   # cs_list a wx+60 (:4195) + 4 (module.hsp:129)
MARGINE_RE_SELECT = 12   # il bordo interno, simmetrico al gcopy di :4165

# --- la geometria del pannello degli dei, letta da god.hsp:382-:462
LARGHEZZA_GOD = 650          # dx = 650                     (god.hsp:382)
INIZIO_VOCE_GOD = 84         # cs_list a wx+80 (:462) + 4   (module.hsp:129)
MARGINE_GOD = 12             # lo stesso bordo interno di *re_select

# --- la geometria dell'elenco delle leggi, letta da economy.hsp:494-:509
INIZIO_VOCE_LEGGI = 104      # cs_list a wx+100 (:509) + 4  (module.hsp:129)
FINE_VOCE_LEGGI = 439        # la striscia della riga: wx+74 + gfini 365 (:494)

# i quattro contenitori di cui la geometria e' stata letta. Tutto il resto si
# conta e non si misura: vedi il docstring.
PERGAMENA = "chat_select"
FINESTRA_EVENTO = "re_select"
PANNELLO_DEI = "god_select_WHILE1"
LEGGI_CITTA = "skip_rule"

# ⚠️ **I `gosub` che non disegnano un menu.** La regola «a disegnarla e' il
# `gosub` che segue» vale finche' il primo `gosub` dopo la voce e' quello che
# apre la finestra. In `*god_select` non lo e': fra i `chatList` (`god.hsp:345`-
# `:350`) e il ciclo che disegna davvero c'e' un `gosub *screen_drawStatus`
# (`:366`), che ridisegna l'HUD e non ha niente a che vedere col menu. Senza
# questa lista le tre voci del pannello degli dei risultavano dentro
# `*screen_drawStatus`, cioe' dentro un contenitore che non esiste — e la
# guardia le contava fra le «non misurate» per sempre.
# 💡 Si scarta per NOME e non per forma, perche' la forma non distingue: e' un
# `gosub *etichetta` come tutti gli altri.
# ⚠️ E `*talk_quest` (`text.hsp:11686`) e' il terzo caso, trovato nella 72a
# quando le 101 voci del menu comune sono entrate nel dizionario tutte insieme:
# non disegna, **costruisce le stringhe** della descrizione dell'incarico
# (`s(5)`, `s(6)`, la ricompensa in monete d'oro). Sta in mezzo alla catena di
# `chatList` di `*talk_main` (`chat.hsp:19799`), quindi la regola «a disegnarla
# e' il primo gosub che segue» ci finiva sopra per **tutte** le voci prima di
# quella riga. 💡 La forma non lo distingue: e' `gosub *etichetta` come gli
# altri, e la prova che non disegna e' che il suo corpo non ha nessun `cs_list`.
# ⚠️ E `*convert_word` (`text.hsp:6899`) e' il quarto caso, trovato nella 74a
# quando il menu del **sonno condiviso** (`event.hsp:2586`-`:2590`) e' entrato nel
# dizionario: non disegna, **scioglie i segnaposto** `{...}` dentro `buff` (1.266
# righe, e la prova e' sempre la stessa: nel suo corpo non c'e' nessun `cs_list`).
# In `event.hsp` lo chiamano dieci volte, sempre poco prima della finestra che
# disegna davvero — qui `gosub *re_select` a `:2605`.
NON_DISEGNANO = frozenset({"screen_drawStatus", "screen_draw", "screen_refreshFull",
                           "talk_quest", "quest_success", "convert_word"})

# --- lo sfondo letto a mano, quando la ricerca all'indietro non lo trova
#
# ⚠️⚠️ **Il registro esiste per NON allargare la finestra all'indietro**, che
# sarebbe la correzione ovvia e darebbe la risposta sbagliata in silenzio.
# `event.hsp:3633`-`:3638` mette le due voci in due rami dello stesso `if`, e
# `:3512`-`:3519` sceglie il bitmap con **la stessa guardia**, 116 righe piu' su:
#
#     3512  if ( gdata(GDATA_AREA) == AREA_OCEAN ) { file = "bg_re25" }   tetto 33
#     3516  else                                   { file = "bg_re13" }   tetto 45
#     3633  if ( gdata(GDATA_AREA) == AREA_OCEAN ) { chatList ...mare... }
#     3636  else                                   { chatList ...strada... }
#
# Tornando indietro dalla voce del **mare** il primo `file =` che si incontra e'
# quello dell'altro ramo: la rete misurerebbe la voce stretta col riquadro largo
# e direbbe «dentro» per costruzione. 💡 E' la trappola gia' scritta nel test di
# questa rete — un tetto scelto senza seguire il ramo produce permessi, non
# difetti — quindi il ramo lo si legge **a mano**, una volta, e lo si scrive qui.
#
# ⚠️ Quel che si registra e' il BITMAP, non il tetto: il numero continua a
# ricavarlo la rete con la sua formula. L'unica cosa che una persona aggiunge e'
# il fatto che dal sorgente non si deduce, cioe' **quale ramo**.
# ⚠️ E si indicizza per SITO, non per firma: e' la lezione della 68a, dove un
# rinvio scritto guardando una riga ha tenuto ferma anche la sua gemella altrove.
SFONDO_A_MANO: dict[tuple[str, int], str] = {
    # il sonno condiviso: `s = "Force Sleep Sharing"` e `file = "bg_re16"` stanno
    # a `event.hsp:2543`-`:2544`, senza rami di mezzo — 42 righe sopra la prima
    # voce, cioe' due righe oltre la finestra della ricerca automatica.
    ("event.hsp", 2586): "bg_re16",
    ("event.hsp", 2587): "bg_re16",
    ("event.hsp", 2588): "bg_re16",
    ("event.hsp", 2589): "bg_re16",
    ("event.hsp", 2590): "bg_re16",
    # gli eventi di viaggio: il ramo del mare e quello della strada, vedi sopra
    ("event.hsp", 3634): "bg_re25",
    ("event.hsp", 3637): "bg_re13",
}

# ⚠️⚠️ **HSP non distingue maiuscole e minuscole, e monte scrive in due modi.**
# Nel sorgente pinnato ci sono 1.626 `chatList` e **31 `chatlist`** (16 in
# `chat.hsp`, 15 in `event.hsp`), che il gioco disegna esattamente uguali. Fino
# alla 74a questa rete cercava la sola forma con la L grande: quelle 31 righe non
# erano «dentro il tetto», erano **fuori dal perimetro** — e tredici delle
# quindici di `event.hsp` sono i menu degli eventi di mare, cioe' il lotto che si
# stava per aprire quando e' saltato fuori.
# 💡 E' la lezione della 66a in una forma nuova: una rete puo' misurare la cosa
# giusta e non arrivarci. Qui non l'ha trovata un referto — nessun referto poteva
# — l'ha trovata la lettura del codice prima di tradurre.
# ⚠️ `chatMore` resta escluso: il suo primo argomento e' il corpo del messaggio,
# non una voce di lista (vedi `righe_di_menu`). Nel sorgente si scrive in un modo
# solo, ma il riconoscimento e' comunque per parola intera.
_VOCE = re.compile(r"(?i)\bchatlist\b")
_GOSUB = re.compile(r"\bgosub\s+\*(\w+)")
_ETICHETTA = re.compile(r"^\*(\w+)")
_SFONDO = re.compile(r'^\s*file\s*=\s*"([^"]+)"')
# ⚠️⚠️ **Un valore interpolato puo' contenere a sua volta un `+`, e la prima
# stesura non lo prevedeva** (76a). `chat.hsp:24715` interpola
# `limit(cdata(CDATA_LEVEL, CHARA_PLAYER) / 2 + 5, 6, 130)`: con `[^+"]` il
# pezzo non veniva riconosciuto come interpolazione, `reso()` restituiva
# l'espressione **intera** — virgolette, nome della funzione e argomenti — e la
# voce risultava lunga 84 caratteri invece di 24. Da fuori si vedeva solo una
# voce «fuori misura» che si salvava per «gia' rotta in inglese», perche'
# l'inglese ha la stessa forma e sbagliava allo stesso modo: un difetto della
# rete travestito da difetto di monte. Il `"` resta escluso — un'interpolazione
# che contiene una stringa non si sa dove finisca — ma il `+` no.
_INTERPOLAZIONE = re.compile(r'"\s*\+\s*[^"]+?\s*\+\s*"')
_GIUNTURA = re.compile(r'"\s*\+\s*"')

# ⚠️⚠️ **E un valore interpolato puo' stare in TESTA o in CODA, non solo in
# mezzo** (76a). `_INTERPOLAZIONE` cerca un valore **fra due letterali**, quindi
# non vedeva ne' `cdatan(CDATAN_NAME, tc) + " lascia..."` ne'
# `"Catalogo A: Lv. " + limit(...)`: in quei due casi `reso()` restituiva il
# codice insieme al testo e la voce risultava lunga il triplo del vero. Le due
# regex chiedono un `+` prima della virgoletta (in testa) o dopo (in coda), che
# e' quel che distingue un'espressione da una **statica**: `\\"Miao?\\"` e
# `citta'` non hanno nessun `+` e restano intatte.
_TESTA = re.compile(r'^[^"]+?\s*\+\s*"')
_CODA = re.compile(r'"\s*\+\s*[^"]+$')


def reso(espressione: str) -> str:
    """La forma che arriva a schermo, a partire da come sta scritta nel sorgente.

    Una voce dinamica e' un'espressione HSP: si tengono i pezzi letterali e ogni
    valore interpolato vale `LARGHEZZA_NUMERO` cifre.

    ⚠️ Le virgolette interne stanno nel dizionario **come le scrive HSP**
    (`\\"Miao?\\"`): la barra rovesciata non si vede a schermo e non si conta,
    o ogni battuta fra virgolette risulterebbe due caratteri piu' lunga del vero.
    """
    cifre = "9" * LARGHEZZA_NUMERO
    testo = _TESTA.sub('"' + cifre, espressione)
    testo = _CODA.sub(cifre + '"', testo)
    testo = _INTERPOLAZIONE.sub(cifre, testo)
    testo = _GIUNTURA.sub("", testo).strip()
    if testo.startswith('"') and testo.endswith('"'):
        testo = testo[1:-1]
    testo = testo.replace('\\"', '"')
    return degrada(testo)


def righe_di_menu(sorgente: Path | None = None) -> dict[str, set[int]]:
    """file .hsp -> righe (1-based) che disegnano una riga di menu.

    ⚠️ **Si legge dal sorgente pinnato, non dal `contesto` della voce.** La prima
    versione di questa rete guardava `contesto`, e vedeva 31 voci su 150: quel
    campo lo riempie `estrai.py` **solo per le dinamiche**, e le voci di menu
    sono quasi tutte statiche (`chatList 1, lang("引き受ける", "Sure thing.")`).
    Una guardia vale solo dove guarda, ed e' la stessa trappola in cui era caduto
    `larghezze.py` cercando i menu per convenzione di nome.

    ⚠️ **`chatMore` non e' una voce di menu**: il suo primo argomento e' il corpo
    del messaggio — quello che misura la rete 14 — e la riga di lista che la
    macro genera e' il bottone «More», che non porta testo scelto da noi. Per
    questo il riconoscimento e' su `chatList` con il confine di parola.
    """
    sorgente = sorgente or percorsi.SORGENTE_HSP
    fuori: dict[str, set[int]] = {}
    for percorso in sorted(sorgente.glob("*.hsp")):
        righe = percorso.read_bytes().decode("cp932", "replace").split("\n")
        trovate = {i for i, riga in enumerate(righe, start=1) if _VOCE.search(riga)}
        if trovate:
            fuori[percorso.name] = trovate
    return fuori


def contenitore_di_menu(
    sorgente: Path | None = None,
    a_mano: dict[tuple[str, int], str] | None = None,
) -> dict[str, dict[int, tuple[str, str]]]:
    """file .hsp -> riga -> (chi disegna il menu, bmp di sfondo).

    ⚠️ **Il `chatList` riempie la lista; a disegnarla e' il `gosub` che segue.**
    Si guarda avanti fino al primo `gosub *X` **senza limite di righe** — il
    negozio delle carte ne impagina 253 prima del suo — e ci si ferma su
    un'etichetta (che allora e' il contenitore: sono i menu che si ridisegnano
    dentro il proprio ciclo) o su un `return`.

    Lo sfondo si cerca all'indietro: e' l'ultimo `file = "bg_reNN"` prima della
    voce, e serve solo dentro `*re_select`, dove il tetto dipende dal bitmap.
    ⚠️ La ricerca guarda **40 righe** e non di piu': vedi `SFONDO_A_MANO` per il
    motivo, che e' un ramo di `if` e non un limite di pazienza. Dove non trova
    niente vale il registro a mano, e **solo li'**: se un domani la ricerca
    automatica trovasse da sola una di quelle righe, il registro non la
    sovrascrive e `sfondi_a_mano_da_togliere()` lo dice.
    """
    sorgente = sorgente or percorsi.SORGENTE_HSP
    a_mano = SFONDO_A_MANO if a_mano is None else a_mano
    fuori: dict[str, dict[int, tuple[str, str]]] = {}
    for percorso in sorted(sorgente.glob("*.hsp")):
        righe = percorso.read_bytes().decode("cp932", "replace").split("\n")
        trovate: dict[int, tuple[str, str]] = {}
        for i, riga in enumerate(righe, start=1):
            if not _VOCE.search(riga):
                continue
            dove = "?"
            for j in range(i, len(righe)):
                gosub = _GOSUB.search(righe[j])
                if gosub:
                    if gosub.group(1) in NON_DISEGNANO:
                        continue
                    dove = gosub.group(1)
                    break
                etichetta = _ETICHETTA.match(righe[j])
                if etichetta:
                    dove = etichetta.group(1)
                    break
                if righe[j].strip() == "return":
                    break
            sfondo = "?"
            for j in range(i - 2, max(0, i - 40), -1):
                trovato = _SFONDO.match(righe[j])
                if trovato:
                    sfondo = trovato.group(1)
                    break
            if sfondo == "?":
                sfondo = a_mano.get((percorso.name, i), "?")
            trovate[i] = (dove, sfondo)
        if trovate:
            fuori[percorso.name] = trovate
    return fuori


def larghezza_sfondo(nome: str, grafica: Path | None = None) -> int | None:
    """La larghezza in pixel di `graphic/<nome>.bmp`, o None se non c'e'.

    Si legge dalla testa del BMP (i quattro byte a offset 18) invece di aprire
    l'immagine: nessuna dipendenza, e di quel file serve un numero solo.
    """
    grafica = grafica or (percorsi.GIOCO / "graphic")
    percorso = grafica / f"{nome}.bmp"
    if not percorso.exists():
        return None
    return struct.unpack("<i", percorso.read_bytes()[18:22])[0]


def tetto_di(contenitore: str, sfondo: str, grafica: Path | None = None) -> int | None:
    """Il tetto in caratteri di una voce, o None se la geometria non e' nota.

    ⚠️ **None non vuol dire «va bene»: vuol dire «non guardato».** Le voci con
    tetto ignoto escono dal conto degli sfori ed entrano in quello delle non
    misurate, che il referto stampa separatamente.
    """
    if contenitore == PERGAMENA:
        return TETTO
    if contenitore == FINESTRA_EVENTO:
        larghezza = larghezza_sfondo(sfondo, grafica)
        if larghezza is None:
            return None
        utili = larghezza + CORNICE_RE_SELECT - MARGINE_RE_SELECT - INIZIO_VOCE_RE_SELECT
        return int(utili / PIXEL_PER_CARATTERE)
    if contenitore == LEGGI_CITTA:
        # ⚠️ Qui il confine non e' il bordo della finestra (`ww = 480`) ma la
        #    **striscia** che il gioco disegna sotto le righe pari,
        #    `gfini 365, 18` a partire da wx+74 (`economy.hsp:494`-`:495`): e'
        #    quella a dire dove finisce la riga, e finisce 41 px prima del bordo.
        return (FINE_VOCE_LEGGI - INIZIO_VOCE_LEGGI) // PIXEL_PER_CARATTERE
    if contenitore == PANNELLO_DEI:
        # ⚠️ Qui il riquadro non dipende da un bitmap: `god.hsp:382` lo scrive
        #    a mano, `dx = 650`, ed e' lo stesso per tutti e nove gli dei.
        utili = LARGHEZZA_GOD - INIZIO_VOCE_GOD - MARGINE_GOD
        return int(utili / PIXEL_PER_CARATTERE)
    return None


def voci_di_menu(
    dizionario: Path | None = None,
    sorgente: Path | None = None,
) -> list[dict]:
    """Le voci del dizionario che il gioco disegna come riga di un menu.

    Ogni voce porta in piu' `_contenitore` e `_sfondo`, cioe' **in quale
    finestra** finisce: senza quelli il tetto non si sa scegliere.
    """
    dizionario = dizionario or percorsi.DIZIONARIO
    per_file = contenitore_di_menu(sorgente)
    fuori = []
    for percorso in sorted(dizionario.glob("*.jsonl")):
        righe = per_file.get(percorso.name.removesuffix(".jsonl"), {})
        if not righe:
            continue
        for linea in percorso.read_text(encoding="utf-8").splitlines():
            if not linea.strip():
                continue
            voce = json.loads(linea)
            if voce["riga"] in righe:
                voce["_contenitore"], voce["_sfondo"] = righe[voce["riga"]]
                fuori.append(voce)
    return fuori


def menu_non_ancora_tradotti(sorgente: Path | None = None) -> int:
    """Quante righe di menu esistono nel sorgente, in tutto.

    Non e' un difetto: e' il denominatore. Serve a non scambiare «zero fuori
    misura» per «tutto controllato» quando il dizionario copre venti righe su
    millecinquecento.
    """
    return sum(len(r) for r in righe_di_menu(sorgente).values())


def _sfori(
    voci: list[dict],
    campo: str,
    grafica: Path | None = None,
) -> list[tuple[str, int, int, str]]:
    fuori = []
    for voce in voci:
        espressione = voce.get(campo) or ""
        if not espressione.strip():
            continue
        tetto = tetto_di(voce.get("_contenitore", PERGAMENA),
                         voce.get("_sfondo", "?"), grafica)
        if tetto is None:
            continue
        testo = reso(espressione)
        if len(testo) > tetto:
            fuori.append((voce["file"], voce["riga"], len(testo), testo))
    return sorted(fuori)


def non_misurate(
    dizionario: Path | None = None,
    sorgente: Path | None = None,
    grafica: Path | None = None,
) -> list[dict]:
    """Le voci di menu di cui non si sa il tetto, contenitore per contenitore.

    ⚠️ Il conto sta nel referto perche' **non sono a posto: sono non guardate**.
    Sommarle alle misurate direbbe «zero fuori misura» su voci che nessuno ha
    misurato, che e' esattamente il difetto che questa rete aveva prima.
    """
    return [v for v in voci_di_menu(dizionario, sorgente)
            if tetto_di(v.get("_contenitore", "?"), v.get("_sfondo", "?"), grafica) is None]


def sfondi_a_mano_da_togliere(
    sorgente: Path | None = None,
    grafica: Path | None = None,
    a_mano: dict[tuple[str, int], str] | None = None,
) -> list[tuple[str, int, str]]:
    """(file, riga, motivo) per ogni voce del registro a mano che non regge piu'.

    ⚠️ **Un registro a mano che nessuno ricontrolla e' un permesso nascosto**, ed
    e' esattamente la forma del difetto della 68a: un rinvio scritto guardando una
    riga che tiene ferma anche un'altra. Qui ogni voce deve continuare a valere
    per tutt'e quattro le ragioni per cui e' stata scritta, e il referto stampa
    quante ne sono in uso invece di lasciarle in silenzio nel codice.

    Le quattro:

    1. la riga e' ancora un `chatList` del sorgente pinnato;
    2. la ricerca automatica non la trova da sola — se la trovasse, il registro
       sarebbe di troppo e la riga andrebbe tolta (non tenuta «per sicurezza»:
       due risposte per lo stesso sito sono un modo di litigare in silenzio);
    3. il contenitore e' `*re_select`, l'unico dove il tetto dipende dal bitmap:
       altrove lo sfondo non lo guarda nessuno e scriverlo fa credere di aver
       misurato;
    4. il bitmap esiste davvero fra i `graphic/*.bmp` del gioco.
    """
    a_mano = SFONDO_A_MANO if a_mano is None else a_mano
    grezzo = contenitore_di_menu(sorgente, a_mano={})
    da_togliere = []
    for (nome, riga), bmp in sorted(a_mano.items()):
        trovate = grezzo.get(nome, {})
        if riga not in trovate:
            da_togliere.append((nome, riga, "non e' (piu') una riga di chatList"))
            continue
        dove, sfondo = trovate[riga]
        if sfondo != "?":
            da_togliere.append((nome, riga,
                                "la ricerca automatica trova gia' %s" % sfondo))
        elif dove != FINESTRA_EVENTO:
            da_togliere.append((nome, riga,
                                "il contenitore e' *%s, dove lo sfondo non si usa" % dove))
        elif larghezza_sfondo(bmp, grafica) is None:
            da_togliere.append((nome, riga, "il bitmap %s non esiste" % bmp))
    return da_togliere


def fuori_misura(
    dizionario: Path | None = None,
    sorgente: Path | None = None,
    grafica: Path | None = None,
) -> list[tuple[str, int, int, str]]:
    """(file, riga, lunghezza, testo) per ogni resa italiana che sfora."""
    return _sfori(voci_di_menu(dizionario, sorgente), "it", grafica)


def fuori_misura_inglese(
    dizionario: Path | None = None,
    sorgente: Path | None = None,
    grafica: Path | None = None,
) -> list[tuple[str, int, int, str]]:
    """Le stesse voci, misurate sull'inglese di monte.

    ⚠️ Serve a **distinguere una regressione nostra da un difetto ereditato**.
    `larghezze.py` ha gia' insegnato che in dieci menu su venti sfora anche
    l'inglese: chi prendesse la stringa inglese come budget erediterebbe il
    difetto. Il tetto e' il riquadro, e vale anche dove l'inglese lo sfora — ma
    sapere quali erano gia' rotte dice da dove viene il danno.
    """
    return _sfori(voci_di_menu(dizionario, sorgente), "en_grezzo", grafica)


def tagliate_a_due_colonne(
    dizionario: Path | None = None,
    sorgente: Path | None = None,
) -> list[tuple[str, int, int, int, str]]:
    """(file, riga, len_en, len_it, testo) per le voci che PEGGIORANO a due colonne.

    Solo la pergamena: gli altri tre contenitori non hanno la seconda colonna.
    Una voce ci finisce se l'inglese di monte sta nei 24 caratteri e l'italiano
    no — cioe' se a due colonne il giocatore leggerebbe tagliata una voce che in
    inglese leggeva intera. Vedi `TETTO_DUE_COLONNE`.
    """
    peggiorate = []
    for voce in voci_di_menu(dizionario, sorgente):
        if voce.get("_contenitore") != PERGAMENA:
            continue
        it = reso(voce.get("it") or "")
        en = reso(voce.get("en_grezzo") or "")
        if not it or not en:
            continue
        if len(en) <= TETTO_DUE_COLONNE < len(it):
            peggiorate.append((voce["file"], voce["riga"], len(en), len(it), it))
    return sorted(peggiorate)


def main(argv: list[str] | None = None) -> int:
    voci = voci_di_menu()
    sfori = fuori_misura()
    monte = {(f, r) for f, r, _, _ in fuori_misura_inglese()}
    scoperte = non_misurate()

    righe_per_contenitore: dict[str, int] = {}
    for per_riga in contenitore_di_menu().values():
        for dove, _ in per_riga.values():
            righe_per_contenitore[dove] = righe_per_contenitore.get(dove, 0) + 1

    print("voci di menu tradotte: %d su %d righe di menu nel sorgente"
          % (len(voci), menu_non_ancora_tradotti()))
    print("righe di menu nel sorgente, per finestra:")
    for dove, quante in sorted(righe_per_contenitore.items(), key=lambda x: -x[1]):
        if dove == PERGAMENA:
            come = "tetto %d caratteri (%d px / %s)" % (
                TETTO, PIXEL_UTILI, str(PIXEL_PER_CARATTERE).replace(".", ","))
        elif dove == FINESTRA_EVENTO:
            come = "tetto secondo il bmp di sfondo"
        else:
            come = "GEOMETRIA NON LETTA"
        print("    %-22s %5d   %s" % (dove, quante, come))

    # dentro *re_select il tetto cambia per sfondo: si stampano, o «zero fuori
    # misura» non direbbe contro che cosa
    per_sfondo: dict[str, int] = {}
    for voce in voci:
        if voce.get("_contenitore") == FINESTRA_EVENTO:
            per_sfondo[voce["_sfondo"]] = per_sfondo.get(voce["_sfondo"], 0) + 1
    if per_sfondo:
        print("\nvoci tradotte dentro *%s, per sfondo:" % FINESTRA_EVENTO)
        for sfondo, quante in sorted(per_sfondo.items()):
            tetto = tetto_di(FINESTRA_EVENTO, sfondo)
            print("    %-12s %4d voci   tetto %s"
                  % (sfondo, quante, tetto if tetto is not None else "SFONDO NON TROVATO"))

    # il registro a mano si dichiara: e' l'unico punto della rete dove il numero
    # non viene dal sorgente, e un elenco che non si stampa non lo ricontrolla
    # nessuno. Vedi SFONDO_A_MANO.
    stantii = sfondi_a_mano_da_togliere()
    print("\nsfondi letti a mano (il ramo non si deduce): %d siti, %d da togliere"
          % (len(SFONDO_A_MANO), len(stantii)))
    for nome, riga, motivo in stantii:
        print("  ⚠️ %-18s %6d  %s" % (nome, riga, motivo))

    if sfori:
        print()
    for file, riga, n, testo in sfori:
        gia = "gia' rotta in inglese" if (file, riga) in monte else "REGRESSIONE NOSTRA"
        print("  %-18s %6d  %3d  %-22s %s" % (file, riga, n, gia, testo[:90]))
    print("\nvoci fuori misura: %d su %d misurate" % (len(sfori), len(voci) - len(scoperte)))
    if monte:
        print("(rotte anche in inglese, per confronto: %d)" % len(monte))
    if scoperte:
        dove = sorted({v["_contenitore"] for v in scoperte})
        print("voci NON misurate (geometria non letta): %d, in %s"
              % (len(scoperte), ", ".join("*" + d for d in dove)))

    # il secondo tetto della pergamena, quello che dipende da quante voci ha il
    # menu di quel PNG: vedi TETTO_DUE_COLONNE
    peggiorate = tagliate_a_due_colonne()
    if peggiorate:
        print()
        for file, riga, len_en, len_it, testo in peggiorate:
            print("  %-18s %6d  en %2d -> it %2d  %s"
                  % (file, riga, len_en, len_it, testo[:70]))
    print("a due colonne (tetto %d): %d rese peggiorate rispetto all'inglese"
          % (TETTO_DUE_COLONNE, len(peggiorate)))
    return 1 if sfori or peggiorate else 0


if __name__ == "__main__":
    sys.exit(main())
