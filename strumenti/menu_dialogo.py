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

Sei voci dello stesso menu, misurate a schermo lo stesso giorno:

    47 caratteri -> 357 px    7,60      43 -> 331    7,70
    46           -> 350       7,61      42 -> 331    7,88
    47           -> 357       7,60      40 -> 308    7,70

cioe' **7,7 px per carattere** — lo stesso valore che `larghezze.py` aveva
misurato il 2026-08-10 su un menu diverso, che e' lo stesso carattere. La
settima voce, quella lunga, si e' fermata esattamente sul bordo.

    407 / 7,7 = 52 caratteri

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

    chat_select        1240 righe   la pergamena del dialogo, tetto 52
    re_select           177         la finestra dell'evento, tetto 36-50
    talk_quest          148         non misurato
    com_txtadv_loop      46         non misurato
    altri                 9         non misurato

⚠️ **`*re_select` (`event.hsp:4119`) e' un'altra geometria**, e il suo tetto non
e' nemmeno una costante: dipende dal **BMP di sfondo** dell'evento.

    event.hsp:4153   dx = tx + 36                  tx = larghezza del bmp
    event.hsp:4195   cs_list q, wx + 60, ...       dove comincia la voce
    module.hsp:129   pos arg2 + 4 ... : mes        e altri 4

Il bordo interno destro sta a `dx - 12`, simmetrico ai `wx + 12` del `gcopy` di
`:4165`. Quindi `(tx + 36 - 12 - 64) / 7,7`, che sui bitmap veri va da **36**
(`bg_re15`, 280 px) a **50** (`bg_re20`, 392 px). Una voce da 45 caratteri col
tetto sbagliato passava e a schermo sfondava di nove.
✅ Misurato prima di correggere (`scratchpad/misura-re-select.py`): delle 32
voci gia' tradotte dentro `*re_select` non ne sforava nessuna. La correzione non
ripara un danno — **toglie un permesso** che nessuno aveva ancora usato.

⚠️ **E quel che non si sa misurare si CONTA, non si misura a occhio.** Per
`talk_quest` e `com_txtadv_loop` la geometria non e' stata letta: quelle voci
escono dal conto degli sfori ed entrano in un conto loro, che il referto stampa.
Applicare 52 «tanto per avere un numero» e' come il filtro furbo di
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

# misurato su sei voci il 2026-08-17; lo stesso di larghezze.py, che e' lo
# stesso carattere misurato il 2026-08-10 su un altro menu
PIXEL_PER_CARATTERE = 7.7

# cifre supposte per un prezzo interpolato. ⚠️ `larghezze.py` ne suppone tre; qui
# sono **quattro** perche' il set piu' caro del negozio costa 5500 biglietti, e
# su un tetto da 52 un carattere e' la differenza fra dentro e fuori.
LARGHEZZA_NUMERO = 4

TETTO = int(PIXEL_UTILI / PIXEL_PER_CARATTERE)

# --- la geometria di *re_select, letta da event.hsp:4145-4195
CORNICE_RE_SELECT = 36   # dx = tx + 36            (event.hsp:4153)
INIZIO_VOCE_RE_SELECT = 64   # cs_list a wx+60 (:4195) + 4 (module.hsp:129)
MARGINE_RE_SELECT = 12   # il bordo interno, simmetrico al gcopy di :4165

# i due contenitori di cui la geometria e' stata letta. Tutto il resto si conta
# e non si misura: vedi il docstring.
PERGAMENA = "chat_select"
FINESTRA_EVENTO = "re_select"

_VOCE = re.compile(r"\bchatList\b")
_GOSUB = re.compile(r"\bgosub\s+\*(\w+)")
_ETICHETTA = re.compile(r"^\*(\w+)")
_SFONDO = re.compile(r'^\s*file\s*=\s*"([^"]+)"')
_INTERPOLAZIONE = re.compile(r'"\s*\+\s*[^+"]+?\s*\+\s*"')
_GIUNTURA = re.compile(r'"\s*\+\s*"')


def reso(espressione: str) -> str:
    """La forma che arriva a schermo, a partire da come sta scritta nel sorgente.

    Una voce dinamica e' un'espressione HSP: si tengono i pezzi letterali e ogni
    valore interpolato vale `LARGHEZZA_NUMERO` cifre.

    ⚠️ Le virgolette interne stanno nel dizionario **come le scrive HSP**
    (`\\"Miao?\\"`): la barra rovesciata non si vede a schermo e non si conta,
    o ogni battuta fra virgolette risulterebbe due caratteri piu' lunga del vero.
    """
    testo = _INTERPOLAZIONE.sub("9" * LARGHEZZA_NUMERO, espressione)
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


def contenitore_di_menu(sorgente: Path | None = None) -> dict[str, dict[int, tuple[str, str]]]:
    """file .hsp -> riga -> (chi disegna il menu, bmp di sfondo).

    ⚠️ **Il `chatList` riempie la lista; a disegnarla e' il `gosub` che segue.**
    Si guarda avanti fino al primo `gosub *X` **senza limite di righe** — il
    negozio delle carte ne impagina 253 prima del suo — e ci si ferma su
    un'etichetta (che allora e' il contenitore: sono i menu che si ridisegnano
    dentro il proprio ciclo) o su un `return`.

    Lo sfondo si cerca all'indietro: e' l'ultimo `file = "bg_reNN"` prima della
    voce, e serve solo dentro `*re_select`, dove il tetto dipende dal bitmap.
    """
    sorgente = sorgente or percorsi.SORGENTE_HSP
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
    return 1 if sfori else 0


if __name__ == "__main__":
    sys.exit(main())
