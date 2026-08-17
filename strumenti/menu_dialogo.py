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
"""
import json
import re
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

_VOCE = re.compile(r"\bchatList\b")
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


def voci_di_menu(
    dizionario: Path | None = None,
    sorgente: Path | None = None,
) -> list[dict]:
    """Le voci del dizionario che il gioco disegna come riga di un menu."""
    dizionario = dizionario or percorsi.DIZIONARIO
    per_file = righe_di_menu(sorgente)
    fuori = []
    for percorso in sorted(dizionario.glob("*.jsonl")):
        righe = per_file.get(percorso.name.removesuffix(".jsonl"), set())
        if not righe:
            continue
        for linea in percorso.read_text(encoding="utf-8").splitlines():
            if not linea.strip():
                continue
            voce = json.loads(linea)
            if voce["riga"] in righe:
                fuori.append(voce)
    return fuori


def menu_non_ancora_tradotti(sorgente: Path | None = None) -> int:
    """Quante righe di menu esistono nel sorgente, in tutto.

    Non e' un difetto: e' il denominatore. Serve a non scambiare «zero fuori
    misura» per «tutto controllato» quando il dizionario copre venti righe su
    millecinquecento.
    """
    return sum(len(r) for r in righe_di_menu(sorgente).values())


def _sfori(voci: list[dict], campo: str) -> list[tuple[str, int, int, str]]:
    fuori = []
    for voce in voci:
        espressione = voce.get(campo) or ""
        if not espressione.strip():
            continue
        testo = reso(espressione)
        if len(testo) > TETTO:
            fuori.append((voce["file"], voce["riga"], len(testo), testo))
    return sorted(fuori)


def fuori_misura(
    dizionario: Path | None = None,
    sorgente: Path | None = None,
) -> list[tuple[str, int, int, str]]:
    """(file, riga, lunghezza, testo) per ogni resa italiana che sfora."""
    return _sfori(voci_di_menu(dizionario, sorgente), "it")


def fuori_misura_inglese(
    dizionario: Path | None = None,
    sorgente: Path | None = None,
) -> list[tuple[str, int, int, str]]:
    """Le stesse voci, misurate sull'inglese di monte.

    ⚠️ Serve a **distinguere una regressione nostra da un difetto ereditato**.
    `larghezze.py` ha gia' insegnato che in dieci menu su venti sfora anche
    l'inglese: chi prendesse la stringa inglese come budget erediterebbe il
    difetto. Il tetto e' il riquadro, e vale anche dove l'inglese lo sfora — ma
    sapere quali erano gia' rotte dice da dove viene il danno.
    """
    return _sfori(voci_di_menu(dizionario, sorgente), "en_grezzo")


def main(argv: list[str] | None = None) -> int:
    voci = voci_di_menu()
    sfori = fuori_misura()
    monte = {(f, r) for f, r, _, _ in fuori_misura_inglese()}

    print("voci di menu tradotte: %d su %d righe di menu nel sorgente"
          % (len(voci), menu_non_ancora_tradotti()))
    print("tetto: %d caratteri (%d px / %s)"
          % (TETTO, PIXEL_UTILI, str(PIXEL_PER_CARATTERE).replace(".", ",")))
    for file, riga, n, testo in sfori:
        gia = "gia' rotta in inglese" if (file, riga) in monte else "REGRESSIONE NOSTRA"
        print("  %-18s %6d  %3d  %-22s %s" % (file, riga, n, gia, testo[:90]))
    print("\nvoci fuori misura: %d su %d" % (len(sfori), len(voci)))
    if monte:
        print("(rotte anche in inglese, per confronto: %d)" % len(monte))
    return 1 if sfori else 0


if __name__ == "__main__":
    sys.exit(main())
