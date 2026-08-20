# strumenti/dati_verifica.py
"""Le reti di un lotto di file dati.

Ogni rete nasce da un sito, non da una prudenza generica:

    segnaposto    `text.hsp:11922 *talktxt_conv` sostituisce **solo i nomi che
                  conosce** — ne conosce trentatre' — e uno che non conosce
                  resta a schermo fra graffe. Dei trentatre', dodici sono
                  contenuto e ventuno sono conversioni grammaticali giapponesi
                  che in italiano non devono comparire mai.
    due punti     `text.hsp:11656` spacca la riga al **primo** due punti:
                  davanti il titolo dell'incarico, dietro il corpo.
    titolo largo  `command.hsp:3357` disegna il titolo a `wx + 100`
                  (`module.hsp:129`: `arg2 + 4 + arg5`) con `font ..., 14 - en*2`,
                  cioe' corpo 12, cioe' **7 px per carattere** — la costante che
                  il progetto ha misurato tre volte per la pergamena del
                  dialogo. La scadenza gli sta davanti a `wx + 344`
                  (`command.hsp:3360`). Restano 244 px: **34 caratteri**.
    struttura     `dati.py` rifiuta a-capo e percento, ma il lotto va fermato
                  prima: qui l'errore si legge col blocco accanto.
    doppi byte    la regola di ogni lotto (`accenti.doppi_byte_cp932`).
    identica      una resa uguale all'inglese e' quasi sempre una dimenticanza.

⚠️ Il tetto si misura sulla forma **degradata**: «perché» sta in 6 caratteri nel
dizionario e in **7** a schermo, perche' l'apostrofo e' un carattere in piu'
(64a).
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
import re

from strumenti import accenti

# I dodici nomi di **contenuto** che `talktxt_conv` sostituisce: quelli che
# hanno senso anche in italiano.
NOMI_CONTENUTO = frozenset({
    "client", "map", "ref", "you", "me", "reward", "objective",
    "deadline", "n", "player", "aka", "npc",
})

# I ventuno di **conversione giapponese**: rendono una desinenza o un registro
# che l'italiano non ha. Se compaiono in una resa e' una svista di copiatura.
NOMI_GIAPPONESI = frozenset({
    "ある", "う", "か", "が", "かな", "だ", "よ", "た", "だな", "だろ",
    "たのむ", "る", "のだ", "な", "くれ", "しろ", "見るな", "ごめん",
    "onii", "syujin", "sex",
})

NOMI_NOTI = NOMI_CONTENUTO | NOMI_GIAPPONESI

# command.hsp:3357 -> il testo a wx+100, la scadenza a wx+344, 7 px per carattere
TETTO_TITOLO = (344 - 100) // 7            # 34

_SEGNAPOSTO = re.compile(r"\{([^}]*)\}")


@dataclass
class Problema:
    genere: str
    blocco: str
    riga: int
    dettaglio: str

    def __str__(self) -> str:
        return f"  {self.genere:13s} {self.blocco},{self.riga}  {self.dettaglio}"


def segnaposto(testo: str) -> Counter:
    return Counter(_SEGNAPOSTO.findall(testo))


def righe_a_capo(testo: str, tetto: int) -> list[str]:
    """Rifa' quel che fa `talk_conv` nel ramo non giapponese (`init.hsp:1326`).

    Spezza **sulle spaziature**, e conta ogni parola insieme allo spazio che la
    segue. L'ultimo pezzo — quello dopo l'ultima spaziatura — viene appeso
    **senza controllo**, quindi puo' sforare.

    ⚠️ E se una parola con lo spazio dietro e' piu' lunga del tetto, il ciclo
    esterno non consuma niente e va avanti a mandare a capo fino alle sue mille
    iterazioni: mille righe vuote, e poi il testo. E' un difetto di monte, non
    una scelta; qui si riproduce perche' una rete che *corregge* il motore non
    misura il motore.
    """
    resto = testo
    uscita = ""
    p = 0
    for _ in range(1000):
        lunghezza = 0
        for _ in range(1000):
            p = resto.find(" ") + 1
            if p == 0:
                break
            if lunghezza + p > tetto:
                uscita += "\n"
                break
            uscita += resto[:p]
            lunghezza += p
            resto = resto[p:]
        if p == 0:
            break
    return (uscita + resto).split("\n")


def _titolo(testo: str) -> str | None:
    posizione = testo.find(":")
    return None if posizione == -1 else testo[:posizione]


def righe_del_corpo(testo: str, tetto: int) -> int:
    """Quante righe prende il corpo (quel che sta dopo il primo due punti).

    I segnaposto si lasciano com'e' invece di espanderli: l'inglese e la resa ne
    hanno lo **stesso insieme** — e' una delle reti — quindi a tempo
    d'esecuzione crescono tutt'e due della stessa quantita', e il confronto
    resta onesto senza dover indovinare che oggetto uscira'.
    """
    posizione = testo.find(":")
    corpo = testo if posizione == -1 else testo[posizione + 1:]
    return len(righe_a_capo(corpo, tetto))


def controlla(voci: list[dict], invariati: set[str] | None = None,
              tetto_a_capo: int | None = None) -> list[Problema]:
    """I problemi delle rese italiane di un lotto. Le voci non tradotte si saltano.

    Con `tetto_a_capo` accende anche la rete dell'**altezza**: nessuna resa puo'
    prendere piu' righe della piu' lunga fra quelle inglesi dello stesso lotto.

    ⚠️ Il tetto non viene da una misura dello schermo — l'altezza della riga di
    `mes` a corpo 11 non e' mai stata misurata — ma dal **corpo**: quel che
    upstream ci fa stare, ci sta. E' un tetto piu' debole di quello vero e piu'
    forte di nessun tetto, e va dichiarato per quel che e'.
    """
    invariati = invariati or set()
    problemi: list[Problema] = []

    massimo_monte = None
    if tetto_a_capo is not None and voci:
        massimo_monte = max(righe_del_corpo(v["en"], tetto_a_capo) for v in voci)

    def segnala(voce, genere, dettaglio):
        problemi.append(Problema(genere, voce["blocco"], voce["riga"], dettaglio))

    for voce in voci:
        resa = voce["it"]
        if not resa:
            continue                       # non tradotta: da fare, non rotta

        # -------------------------------------------------------- struttura
        if "\n" in resa or "\r" in resa:
            segnala(voce, "struttura", "la resa contiene un a-capo: spaccherebbe il blocco")
            continue
        if resa.lstrip().startswith("%"):
            segnala(voce, "struttura", "la resa comincia per '%': verrebbe letta come intestazione")
            continue

        # ------------------------------------------------------- segnaposto
        nell_inglese = segnaposto(voce["en"])
        nella_resa = segnaposto(resa)
        if nella_resa != nell_inglese:
            persi = nell_inglese - nella_resa
            aggiunti = nella_resa - nell_inglese
            pezzi = []
            if persi:
                pezzi.append("persi " + " ".join(f"{{{n}}}x{c}" for n, c in sorted(persi.items())))
            if aggiunti:
                pezzi.append("aggiunti " + " ".join(f"{{{n}}}x{c}" for n, c in sorted(aggiunti.items())))
            segnala(voce, "segnaposto", "; ".join(pezzi))
        else:
            ignoti = [n for n in nella_resa if n not in NOMI_CONTENUTO]
            if ignoti:
                giapponesi = [n for n in ignoti if n in NOMI_GIAPPONESI]
                fuori = [n for n in ignoti if n not in NOMI_NOTI]
                if giapponesi:
                    segnala(voce, "segnaposto",
                            "conversioni giapponesi nella resa: "
                            + " ".join(f"{{{n}}}" for n in giapponesi))
                if fuori:
                    segnala(voce, "segnaposto",
                            "talktxt_conv non li conosce, resterebbero fra graffe: "
                            + " ".join(f"{{{n}}}" for n in fuori))

        # -------------------------------------------------------- due punti
        titolo = _titolo(resa)
        if titolo is None:
            segnala(voce, "due punti", "nessun due punti: il gioco non trova il titolo")
        elif not titolo.strip():
            segnala(voce, "due punti", "il titolo davanti ai due punti e' vuoto")
        else:
            largo = len(accenti.degrada(titolo))
            if largo > TETTO_TITOLO:
                segnala(voce, "titolo largo",
                        f"{largo} caratteri, tetto {TETTO_TITOLO}: {titolo!r}")

        # ------------------------------------------------------- doppi byte
        # ⚠️ Si guarda la forma DEGRADATA, come fa `verifica.py` per gli .hsp:
        # nel lotto va l'accento vero («perché»), e la degradazione ad apostrofo
        # la fa l'applicazione. Controllare la resa grezza segnalerebbe ogni «è».
        # Quel che resta dopo la degradazione e' un problema vero.
        #
        # ⚠️ E servono TUTT'E DUE i controlli: la differenza si e' vista
        # scrivendo il test, perche' «—» (U+2014) CP932 non lo codifica affatto
        # — lo prende `non_ascii_residuo` — mentre quello a due byte e' «―»
        # (U+2015). Con un controllo solo passava proprio il trattino lungo che
        # si infila da se' scrivendo prosa italiana (67a).
        a_schermo = accenti.degrada(resa)
        if accenti.ha_apostrofo_scritto_a_mano(resa):
            segnala(voce, "apostrofo",
                    "apostrofo scritto a mano: nel lotto va l'accento vero, "
                    "la degradazione la fa l'applicazione")
        residui = accenti.doppi_byte_cp932(a_schermo)
        if residui:
            segnala(voce, "doppi byte", "".join(residui))
        fuori_cp932 = accenti.non_ascii_residuo(a_schermo)
        if fuori_cp932:
            segnala(voce, "fuori cp932", "".join(fuori_cp932))

        # --------------------------------------------------------- identica
        if resa == voce["en"] and resa not in invariati:
            segnala(voce, "identica", "la resa e' l'inglese")

        # ---------------------------------------------------------- altezza
        if massimo_monte is not None:
            quante = righe_del_corpo(accenti.degrada(resa), tetto_a_capo)
            if quante > massimo_monte:
                segnala(voce, "altezza",
                        f"{quante} righe a capo, il piu' lungo di monte ne prende {massimo_monte}")

    return problemi


def segnaposto_ignoti_di_monte(voci: list[dict]) -> list[Problema]:
    """I segnaposto che l'INGLESE usa e `talktxt_conv` non conosce.

    Non e' un problema nostro: e' un difetto di monte che il giocatore inglese
    vede gia' (in `talk.txt` ce ne sono sei, tutti `{nptc}` per `{npc}`). Si
    stampa perche' una resa italiana non deve copiarlo.
    """
    fuori = []
    for voce in voci:
        ignoti = [n for n in segnaposto(voce["en"]) if n not in NOMI_NOTI]
        if ignoti:
            fuori.append(Problema("monte", voce["blocco"], voce["riga"],
                                  "l'inglese usa " + " ".join(f"{{{n}}}" for n in ignoti)))
    return fuori


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Controlla un lotto di file dati.")
    analizzatore.add_argument("lotto", help="percorso del lotto JSONL")
    analizzatore.add_argument("--tetto", type=int, default=70,
                              help="larghezza a cui il gioco manda a capo il corpo "
                                   "(board.txt: talk_conv buff, 70 in command.hsp:3367)")
    argomenti = analizzatore.parse_args()

    voci = [json.loads(r) for r in Path(argomenti.lotto).read_text(encoding="utf-8").splitlines() if r.strip()]
    tradotte = [v for v in voci if v["it"]]

    for problema in segnaposto_ignoti_di_monte(voci):
        print(problema)

    problemi = controlla(voci, tetto_a_capo=argomenti.tetto)
    for problema in problemi:
        print(problema)

    print(f"\n{len(tradotte)} / {len(voci)} tradotte, {len(problemi)} problemi")
    if problemi:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
