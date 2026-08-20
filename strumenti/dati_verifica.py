# strumenti/dati_verifica.py
"""Le reti di un lotto di file dati.

Ogni rete nasce da un sito, non da una prudenza generica:

    segnaposto    l'espansore del file sostituisce **solo i nomi che conosce**,
                  e uno che non conosce resta a schermo fra graffe. Una parte di
                  quei nomi sono conversioni grammaticali giapponesi, che in
                  italiano non devono comparire mai.
    due punti     per `board.txt`, `text.hsp:11656` spacca la riga al **primo**
                  due punti: davanti il titolo dell'incarico, dietro il corpo.
                  In `talk.txt` non c'e' nessun due punti e la regola non vale.
    titolo largo  vedi `TETTO_TITOLO` qui sotto: il tetto lo fissa la prima cosa
                  disegnata alla destra del titolo, che non e' la prima che si
                  incontra leggendo il sorgente.
    struttura     `dati.py` rifiuta a-capo e percento, ma il lotto va fermato
                  prima: qui l'errore si legge col blocco accanto.
    cp932         doppi byte **e** caratteri non codificabili, sulla forma
                  degradata.
    identica      una resa uguale all'inglese e' quasi sempre una dimenticanza.
    altezza       nessuna resa prende piu' righe a capo della piu' lunga fra le
                  inglesi dello stesso lotto.

⚠️ I tetti si misurano sulla forma **degradata**: «perché» sta in 6 caratteri nel
lotto e in **7** a schermo, perche' l'apostrofo e' un carattere in piu' (64a).
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from strumenti import accenti

# ⚠️⚠️ OGNI FILE DATI HA IL SUO ESPANSORE, E NON CONOSCONO GLI STESSI NOMI.
#
#     board.txt  ->  *talktxt_conv  (text.hsp:11922)   33 nomi
#     talk.txt   ->  *convert_word  (text.hsp:6900)    46 nomi
#
# Nella 70a la rete e' stata girata su `talk.txt` col profilo di `board.txt` e ha
# «trovato» sei `{nptc}` inesistenti: `convert_word` conosce benissimo `nptc`,
# insieme a `npcc` e a diciannove codici di espressione e di suono. E' la domanda
# «finito per quale referto?» nella forma «misurato con quale rete?» — e una rete
# giusta puntata sul file sbagliato non tace: **mente**.
#
# Il **contenuto** e' quel che ha senso anche in italiano; le **conversioni
# giapponesi** rendono desinenze e registri che l'italiano non ha; i
# **controlli** sono direttive di faccia e di suono, che si conservano com'e'
# (lo impone gia' il confronto sull'insieme dei segnaposto).

_GIAPPONESI = frozenset({
    "ある", "う", "か", "が", "かな", "だ", "よ", "た", "だな", "だろ",
    "たのむ", "る", "のだ", "な", "くれ", "しろ", "見るな", "ごめん",
    "onii", "syujin", "sex",
})


class Espansore:
    def __init__(self, nome, contenuto, controlli=()):
        self.nome = nome
        self.contenuto = frozenset(contenuto)
        self.controlli = frozenset(controlli)
        self.giapponesi = _GIAPPONESI
        self.noti = self.contenuto | self.controlli | self.giapponesi

    def ammessi(self) -> frozenset:
        """Quel che una resa italiana puo' portare: contenuto e controlli."""
        return self.contenuto | self.controlli


TALKTXT_CONV = Espansore(
    "talktxt_conv",
    ("client", "map", "ref", "you", "me", "reward", "objective",
     "deadline", "n", "player", "aka", "npc"),
)

CONVERT_WORD = Espansore(
    "convert_word",
    ("ref", "you", "player", "aka", "npc", "nptc", "npcc", "me"),
    ("Basic", "Embarrassment", "Fun", "Happy", "Angry", "Question",
     "seChangePage", "seMelee1", "seMelee2", "seMiss", "seCursor1", "seFire",
     "seKill", "seKill2", "seMore", "seGetGold", "sePayGold", "seEquip", "seGet"),
)

# Il profilo di un file: chi lo legge, se la riga e' `titolo:corpo`, e a che
# larghezza il gioco la manda a capo.
#
#     board.txt   talk_conv buff, 70            command.hsp:3367
#     talk.txt    talk_conv buff, 56 - en * 3   chat.hsp:25226, cioe' 53
PROFILI = {
    "board.txt": {"espansore": TALKTXT_CONV, "titolo": True, "tetto_capo": 70},
    "talk.txt": {"espansore": CONVERT_WORD, "titolo": False, "tetto_capo": 53},
}

PROFILO_IGNOTO = {"espansore": TALKTXT_CONV, "titolo": True, "tetto_capo": None}


def profilo(nome_file: str | None) -> dict:
    return PROFILI.get(nome_file, PROFILO_IGNOTO)


def _profilo_del_lotto(voci: list[dict]) -> dict:
    nomi = {v.get("file") for v in voci}
    return profilo(nomi.pop() if len(nomi) == 1 else None)


# ⚠️⚠️ L'OSTACOLO NON E' IL `pos` CHE VIENE DOPO NEL SORGENTE.
#
# `command.hsp:3357` disegna il titolo di un incarico a `wx + 96`, e
# `module.hsp:129` lo scrive altri `4 + arg5` piu' in la': testo a **wx + 100**.
# Leggendo il sorgente in ordine il primo `pos` successivo e' la scadenza a
# `wx + 344` (`:3360`), e per mezza sessione qui c'e' stato scritto 34. Ma
# quaranta righe piu' giu' `:3391` disegna le **stellette del livello** a
# `wx + 270`, cioe' PIU' A SINISTRA, e **dopo** il titolo: quel che sfora ci
# finisce sotto.
#
# E' la lezione della 68a (`intestazioni_larghezze`) presa in pieno una seconda
# volta: *una cosa disegnata dopo copre quel che c'era prima, e l'ordine di
# lettura del sorgente non dice qual e' la piu' a sinistra*. A trovarlo e' stato
# il collaudo della 70a, misurando i pixel della bacheca di Yowyn:
#
#     testo del titolo   781 = wx + 100   (wx = 681)
#     stellette          951 = wx + 270   <- l'ostacolo
#     scadenza          1027 ~ wx + 344
#     nome del cliente  1073 = wx + 392
#
# e «Si fa festa!», dodici caratteri, finiva a 865 = 781 + 12 x 7: i 7 px per
# carattere confermati sulla schermata stessa.
TETTO_TITOLO = (270 - 100) // 7            # 24

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


def righe_del_corpo(testo: str, tetto: int, col_titolo: bool = True) -> int:
    """Quante righe prende il corpo, cioe' quel che il giocatore legge.

    Dove la riga e' `titolo:corpo` il titolo si toglie, perche' e' disegnato
    altrove; dove non lo e', il corpo e' tutta la riga.

    I segnaposto si lasciano com'e' invece di espanderli: l'inglese e la resa ne
    hanno lo **stesso insieme** — e' una delle reti — quindi a tempo
    d'esecuzione crescono tutt'e due della stessa quantita', e il confronto
    resta onesto senza dover indovinare che oggetto uscira'.
    """
    posizione = testo.find(":") if col_titolo else -1
    corpo = testo if posizione == -1 else testo[posizione + 1:]
    return len(righe_a_capo(corpo, tetto))


def controlla(voci: list[dict], invariati: set[str] | None = None,
              tetto_a_capo: int | None = None,
              espansore: Espansore | None = None,
              titolo: bool | None = None) -> list[Problema]:
    """I problemi delle rese italiane di un lotto. Le voci non tradotte si saltano.

    `espansore` e `titolo` vengono dal **profilo** del file (vedi `PROFILI`):
    chi lo legge, e se la riga e' `titolo:corpo`. Se non li si passa si prendono
    dal campo `file` delle voci — cosi' chi chiama non deve saperlo, ma chi
    vuole imporli puo'.

    Con `tetto_a_capo` accende anche la rete dell'**altezza**: nessuna resa puo'
    prendere piu' righe della piu' lunga fra quelle inglesi dello stesso lotto.

    ⚠️ Quel tetto non viene da una misura dello schermo — l'altezza di una riga
    di `mes` a corpo 11 non e' mai stata misurata in questo progetto — ma dal
    **corpus**: quel che upstream ci fa stare, ci sta. E' un tetto piu' debole
    di quello vero e piu' forte di nessun tetto, e va dichiarato per quel che e'.
    """
    invariati = invariati or set()
    problemi: list[Problema] = []

    if espansore is None or titolo is None:
        suo = _profilo_del_lotto(voci)
        if espansore is None:
            espansore = suo["espansore"]
        if titolo is None:
            titolo = suo["titolo"]

    massimo_monte = None
    if tetto_a_capo is not None and voci:
        massimo_monte = max(righe_del_corpo(v["en"], tetto_a_capo, titolo) for v in voci)

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
            ignoti = [n for n in nella_resa if n not in espansore.ammessi()]
            if ignoti:
                giapponesi = [n for n in ignoti if n in espansore.giapponesi]
                fuori = [n for n in ignoti if n not in espansore.noti]
                if giapponesi:
                    segnala(voce, "segnaposto",
                            "conversioni giapponesi nella resa: "
                            + " ".join(f"{{{n}}}" for n in giapponesi))
                if fuori:
                    segnala(voce, "segnaposto",
                            f"{espansore.nome} non li conosce, resterebbero fra graffe: "
                            + " ".join(f"{{{n}}}" for n in fuori))

        # -------------------------------------------------------- due punti
        if titolo:
            testa = _titolo(resa)
            if testa is None:
                segnala(voce, "due punti", "nessun due punti: il gioco non trova il titolo")
            elif not testa.strip():
                segnala(voce, "due punti", "il titolo davanti ai due punti e' vuoto")
            else:
                largo = len(accenti.degrada(testa))
                if largo > TETTO_TITOLO:
                    segnala(voce, "titolo largo",
                            f"{largo} caratteri, tetto {TETTO_TITOLO}: {testa!r}")

        # ------------------------------------------------------------ cp932
        # ⚠️ Si guarda la forma DEGRADATA, come fa `verifica.py` per gli .hsp:
        # nel lotto va l'accento vero («perché»), e la degradazione ad apostrofo
        # la fa l'applicazione. Controllare la resa grezza segnalerebbe ogni «è».
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
            quante = righe_del_corpo(accenti.degrada(resa), tetto_a_capo, titolo)
            if quante > massimo_monte:
                segnala(voce, "altezza",
                        f"{quante} righe a capo, il piu' lungo di monte ne prende {massimo_monte}")

    return problemi


def segnaposto_ignoti_di_monte(voci: list[dict],
                               espansore: Espansore | None = None) -> list[Problema]:
    """I segnaposto che l'INGLESE usa e il suo espansore non conosce.

    Non sarebbe un problema nostro ma di monte: il giocatore inglese li vedrebbe
    gia' fra graffe. ⚠️ Va chiamata con l'espansore **giusto**: nella 70a,
    girata su `talk.txt` col profilo di `board.txt`, ha «trovato» sei `{nptc}`
    che `convert_word` conosce benissimo.
    """
    if espansore is None:
        espansore = _profilo_del_lotto(voci)["espansore"]
    fuori = []
    for voce in voci:
        ignoti = [n for n in segnaposto(voce["en"]) if n not in espansore.noti]
        if ignoti:
            fuori.append(Problema("monte", voce["blocco"], voce["riga"],
                                  "l'inglese usa " + " ".join(f"{{{n}}}" for n in ignoti)))
    return fuori


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Controlla un lotto di file dati.")
    analizzatore.add_argument("lotto", help="percorso del lotto JSONL")
    analizzatore.add_argument("--tetto", type=int, default=None,
                              help="larghezza a cui il gioco manda a capo "
                                   "(default: quella del profilo del file)")
    argomenti = analizzatore.parse_args()

    voci = [json.loads(r) for r in
            Path(argomenti.lotto).read_text(encoding="utf-8").splitlines() if r.strip()]
    tradotte = [v for v in voci if v["it"]]
    suo = _profilo_del_lotto(voci)
    tetto = argomenti.tetto if argomenti.tetto is not None else suo["tetto_capo"]

    for problema in segnaposto_ignoti_di_monte(voci):
        print(problema)

    problemi = controlla(voci, tetto_a_capo=tetto)
    for problema in problemi:
        print(problema)

    print(f"\n{len(tradotte)} / {len(voci)} tradotte, {len(problemi)} problemi "
          f"(espansore {suo['espansore'].nome}, a capo a {tetto})")
    if problemi:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
