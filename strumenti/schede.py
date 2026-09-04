"""Le schede di carta scritte a mano dentro il codice (lotto C della Fase 6).

`tcg_skill.hsp` e `tcg.hsp` assegnano a `carddetailneff@tcg(...)` **schede
intere gia' composte**, invece di lasciarle costruire a `card_ref`:

    carddetailneff@tcg(cextra@tcg) = "Cure Crystal  No.???   overpriced heal
        potion  Rare:None\\n[Command Card]\\nEffect: Heal Player 2 Damage."

⚠️⚠️ **NON C'E' UNA CHIAVE COME NELLA FASE 5.** Li' ogni descrizione stava in
`effdesc@tcg(COSTANTE)` e la costante era la chiave. Qui l'indice e' una
**variabile** (`cextra@tcg`, `aeft@tcg`, `tcggen_arg1`, `cnt`), e non dice
niente. E non puo' essere `file:riga`, che la Fase 4 ha imparato a proprie
spese: la riga si sposta sotto una resa. Resta il **letterale inglese**, che su
questi due file e' distinto -- ed e' la stessa `firma` che il dizionario
generale usa da sempre, applicata a letterali che non stanno dentro `lang()`.

⚠️⚠️ **E QUESTE SCHEDE NON PASSANO DA `talk_conv`.** `card_ref` manda a capo il
sapore a 95/100 colonne e l'effetto a 65; qui `cardhelp` riceve la stringa
gia' fatta e `mes` la disegna **verbatim**. Quindi ogni riga separata da `\\n`
esce lunga quanto viene, e la larghezza non la limita nessuno: il cancello la
misura, e il tetto e' il massimo che l'inglese di monte gia' disegna.

⭐ **Il vocabolario della scheda e' gia' italiano nel ramo dinamico**, deciso da
fasi precedenti dentro `lang()` (`tcg.hsp:1495-1610`) e dal lotto B:

    "  No."    -> "  N."          "Effect: "        -> "Effetto: "
    "  Rare:"  -> "  Rarita':"    "[Command Card] " -> "[Carta comando] "

Se le 76 non lo seguono, meta' gioco dice `Rare:` e meta' `Rarita':` -- e non lo
noterebbe nessun cancello che guardi solo la resa in se'. Per questo il
vocabolario e' un **rifiuto**, non un avviso.
"""
import argparse
import json
import re
from pathlib import Path

from strumenti import percorsi
from strumenti.accenti import degrada

FILE = ("tcg_skill.hsp", "tcg.hsp")

# ⚠️ Il numero atteso batte l'avviso, perche' non chiede a nessuno di
# ricordarsi (lezione delle «35 toppe» della 96a). Se il riconoscitore ne trova
# altre, il sorgente si e' mosso e il conto va rifatto, non aggiustato.
# ⭐ 72, non le 76 che il censimento della 135a dava per `tcg_skill.hsp`. Il
# conto e' stato RIFATTO, non aggiustato: `scratchpad/_137-schede-riconcilia.py`
# fa vedere che le sette di differenza sono le GIUNTURE qui sotto piu' una
# traccia di debug (`"tcg draw: c"`, `tcg.hsp:2105`, che nomina
# `carddetailneff@tcg` dentro un `proctcg` ma non ci assegna niente).
#   72 riconosciute + 7 dichiarate = 79, che e' quel che il censimento vede.
ATTESE = 72

_ASSEGNAZIONE = re.compile(r"carddetailneff@tcg\([^)]*\)\s*\+?=\s*(.*)$")
_LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')

# Un letterale piu' corto di questo non e' una scheda: e' `""` (un azzeramento)
# oppure un pezzo di giuntura come `"ace of "`. Quelli si dichiarano, non si
# riconoscono per sbaglio.
MINIMO = 4

# ⚠️ I pezzi di giuntura del gioco del poker (`tcg_skill.hsp:6230-6245`) e i due
# prefissi concatenati: sono testo, ma NON sono schede, e si rendono a mano nel
# lotto E. Restano dichiarati invece di sparire dal censimento.
GIUNTURE = {
    "ace of ": "tcg_skill.hsp:6230, prefisso del gioco del poker",
    " of ": "tcg_skill.hsp:6234, giuntura del gioco del poker",
    "jack of ": "tcg_skill.hsp:6237",
    "queen of ": "tcg_skill.hsp:6241",
    "king of ": "tcg_skill.hsp:6245",
    "High Potion of ": "tcg_skill.hsp:931, prefisso di un nome generato",
    "socks of ": "tcg_skill.hsp:4246, prefisso di un nome generato",
    "\\nEffect: ": "tcg_skill.hsp:2003, la SECONDA ricomposizione della scheda",
}

# Il vocabolario che il ramo dinamico scrive gia' in italiano. Chiave: quel che
# l'inglese di monte porta; valore: quel che la resa DEVE portare.
#
# ⭐ Gli innesti e le parole chiave si IMPORTANO da `carte.py` invece di
# ricopiarli: due copie della stessa tabella sono due tabelle, e la prima a
# restare indietro non lo dice a nessuno. Qui dentro restano solo le voci che
# `carte` non ha, perche' riguardano l'intestazione della scheda e non la
# descrizione d'effetto.
_INTESTAZIONE = {
    "No.???": "N.???",
    "Rare:": "Rarita':",
    "Effect:": "Effetto:",
    "Bits:": "Tratti:",
    "[Command Card]": "[Carta comando]",
    "[Illegal Card]": "[Carta illegale]",
    "[Cost at least 1": "[Costa almeno 1",
    "[Reusable]": "[Riutilizzabile]",
    "[Discard if not Played]": "[Scartata se non giocata]",
    # ⚠️ Il blocco delle etichette scrive «Dual-Strike», queste schede
    # «Double-Strike». Due grafie di monte, un traducente solo.
    "Double-Strike": "Doppio colpo",
}


VOCABOLARIO = _INTESTAZIONE

# Il soffitto della larghezza, ricalcolato dal file da una prova: e' il massimo
# che l'inglese di monte gia' disegna in queste stesse schede. Sopra quello non
# si sa niente, e la lettura che non puo' far danno e' stare sotto.
LARGHEZZA_MASSIMA = 0    # riempito da `_misura_inglese()` al primo uso


def leggi(nome: str, percorso: Path | None = None) -> list[str]:
    """Le righe del file, senza terminatore."""
    percorso = percorso or (percorsi.SORGENTE_HSP / nome)
    righe = percorso.read_bytes().decode("cp932").split("\r\n")
    if len(righe) < 500:
        raise ValueError("%s: diviso in %d righe, la divisione e' fallita e"
                         " ogni conto qui sotto sarebbe cieco"
                         % (nome, len(righe)))
    return righe


def scrivi(righe: list[str], percorso: Path) -> None:
    percorso.write_bytes("\r\n".join(righe).encode("cp932"))


def voci(righe: list[str], nome: str) -> list[dict]:
    """Le schede: i letterali assegnati a `carddetailneff@tcg(...)`.

    ⚠️ Le righe commentate si saltano: in HSP il commento e' `;` **oppure**
    `//`, e guardare solo il `;` e' il guasto che le rinviate chiamano «la
    quarta volta».
    """
    fuori = []
    for numero, riga in enumerate(righe, 1):
        spoglia = riga.lstrip()
        if spoglia.startswith(";") or spoglia.startswith("//"):
            continue
        trovato = _ASSEGNAZIONE.search(riga)
        if trovato is None:
            continue
        for letterale in _LETTERALE.findall(trovato.group(1)):
            if len(letterale) < MINIMO or letterale in GIUNTURE:
                continue
            fuori.append({"file": nome, "riga": numero, "en": letterale})
    return fuori


def tutte() -> list[dict]:
    return [v for nome in FILE for v in voci(leggi(nome), nome)]


def carica_dizionario(percorso: Path | None = None) -> dict:
    percorso = percorso or (percorsi.DIZIONARIO / "carte" / "schede.jsonl")
    if not percorso.exists():
        return {}
    fuori = {}
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        if riga.strip():
            voce = json.loads(riga)
            fuori[voce["en"]] = voce
    return fuori


def applica_a_righe(righe: list[str], nome: str,
                    dizionario: dict) -> tuple[list[str], int]:
    """Inietta le rese. Dizionario vuoto -> le righe tornano identiche.

    ⚠️ La sostituzione e' sul **letterale con le virgolette**, non sul testo
    nudo: `"of "` comparirebbe dentro mille altre parole, e una resa iniettata
    a meta' di un identificatore non la vedrebbe nessuno finche' il gioco non
    smette di partire.

    ⚠️⚠️ Si cammina sul **DIZIONARIO**, non sui letterali del file. La prima
    stesura faceva il contrario -- per ogni letterale trovato nel file cercava
    la resa -- e cosi' una voce il cui monte fosse cambiato non dava nessun
    errore: semplicemente non veniva trovata, e spariva in silenzio. Il
    `ValueError` che c'era per proteggere quel caso **non poteva accendersi
    mai**, ed e' peggio che non averlo, perche' sembra una rete. L'ha trovato
    la prova, non una rilettura.
    """
    per_letterale = {v["en"]: v for v in voci(righe, nome)}
    fuori = list(righe)
    fatte = 0
    for chiave, voce in dizionario.items():
        if voce.get("file") not in (None, nome):
            continue
        reso = voce.get("it")
        if not reso:
            continue
        monte = per_letterale.get(chiave)
        if monte is None:
            raise ValueError(
                "%s: il letterale su cui questa resa fu scritta non esiste"
                " piu'. La voce va rifatta, non riagganciata: %r"
                % (nome, chiave[:60]))
        indice = monte["riga"] - 1
        prima = fuori[indice]
        dopo = prima.replace('"%s"' % chiave, '"%s"' % degrada(reso), 1)
        if dopo == prima:
            raise ValueError("%s riga %d: la sostituzione non ha cambiato"
                             " niente" % (nome, monte["riga"]))
        fuori[indice] = dopo
        fatte += 1
    return fuori, fatte


def disegnate(testo: str) -> list[str]:
    """Le righe come `mes` le disegna: `\\n` sciolto, accenti degradati.

    Niente `talk_conv`: queste schede arrivano a `cardhelp` gia' composte.
    """
    return degrada(testo).replace("\\n", "\n").split("\n")


def _misura_inglese() -> int:
    """Il soffitto: la riga piu' larga che l'inglese di monte gia' disegna."""
    global LARGHEZZA_MASSIMA
    if not LARGHEZZA_MASSIMA:
        LARGHEZZA_MASSIMA = max(len(r) for v in tutte()
                                for r in disegnate(v["en"]))
    return LARGHEZZA_MASSIMA


def _effetto(scheda: str, marcatore: str) -> str:
    """La parte della scheda che sta dopo `Effect:` / `Effetto:`.

    E' l'unico pezzo confrontabile con una descrizione d'effetto della Fase 5:
    l'intestazione (nome, numero, sapore, rarita') non ha innesti e non va
    passata al cancello di `carte`, che li' non troverebbe niente da dire.
    """
    taglio = scheda.find(marcatore)
    if taglio == -1:
        return ""
    return scheda[taglio + len(marcatore):].strip()


def problemi(voce: dict) -> list[str]:
    """Che cosa RIFIUTA una resa. Elenco vuoto = va bene."""
    reso = voce.get("it")
    if not reso:
        return []
    guai = []
    try:
        degrada(reso).encode("cp932")
    except UnicodeEncodeError as errore:
        fuori = degrada(reso)[errore.start:errore.end]
        guai.append("il carattere %r non esiste in CP932: il gioco non puo'"
                    " scriverlo" % fuori)

    inglese = voce.get("en") or ""
    for monte, italiano in VOCABOLARIO.items():
        if monte in inglese and italiano not in degrada(reso):
            guai.append("la scheda dinamica scrive «%s» dove questa dice"
                        " ancora «%s»: meta' gioco direbbe una cosa e meta'"
                        " l'altra" % (italiano, monte))

    # ⭐ La parte d'effetto la giudica `carte.problemi`, non una regola nuova.
    # Li' dentro c'e' gia' la distinzione che serve: gli innesti si controllano
    # SOLO in testa, perche' «Sacrifice» in testa e' «Sacrificio:» ma a meta'
    # frase e' il verbo «sacrifica», e un cancello che lo cercasse ovunque
    # direbbe rosso su una resa giusta -- e chi traduce imparerebbe a non
    # guardarlo (la lezione della 70a). Riscriverla qui voleva dire riscriverla
    # peggio.
    from strumenti.carte import problemi as problemi_effetto

    effetto_en = _effetto(inglese, "Effect:")
    effetto_it = _effetto(degrada(reso), "Effetto:")
    if effetto_en and effetto_it:
        guai += problemi_effetto({"costante": "", "en": effetto_en,
                                  "it": effetto_it})

    tetto = _misura_inglese()
    for numero, riga in enumerate(disegnate(reso), 1):
        if len(riga) > tetto:
            guai.append("riga %d larga %d colonne: `mes` disegna verbatim e"
                        " qui non c'e' nessun `talk_conv`; l'inglese di queste"
                        " schede non passa le %d" % (numero, len(riga), tetto))
    return guai


def avvisi(voce: dict) -> list[str]:
    """Cio' che va **guardato**, non cio' che va rifiutato."""
    reso, inglese = voce.get("it"), voce.get("en")
    if not reso or not inglese:
        return []
    dopo, prima = len(disegnate(reso)), len(disegnate(inglese))
    if dopo > prima:
        return ["%d righe contro le %d dell'inglese" % (dopo, prima)]
    return []


def estrai(nome_lotto: str) -> Path:
    lotto = [v for v in tutte()
             if not carica_dizionario().get(v["en"], {}).get("it")]
    bersaglio = percorsi.LAVORO_LOTTI / ("schede-%s.jsonl" % nome_lotto)
    with bersaglio.open("w", encoding="utf-8") as scrittura:
        for voce in lotto:
            scrittura.write(json.dumps(dict(voce, it=""),
                                       ensure_ascii=False) + "\n")
    return bersaglio


def reimporta(lotto: Path) -> int:
    bersaglio = percorsi.DIZIONARIO / "carte" / "schede.jsonl"
    bersaglio.parent.mkdir(parents=True, exist_ok=True)
    diz = carica_dizionario(bersaglio)
    nuove = 0
    for riga in lotto.read_text(encoding="utf-8").splitlines():
        if not riga.strip():
            continue
        voce = json.loads(riga)
        if not voce.get("it"):
            continue
        guai = problemi(voce)
        if guai:
            raise SystemExit("%s:%d: %s"
                             % (voce["file"], voce["riga"], "; ".join(guai)))
        diz[voce["en"]] = {"file": voce["file"], "riga": voce["riga"],
                           "en": voce["en"], "it": voce["it"]}
        nuove += 1
    with bersaglio.open("w", encoding="utf-8") as scrittura:
        for chiave in sorted(diz):
            scrittura.write(json.dumps(diz[chiave], ensure_ascii=False) + "\n")
    return nuove


def referto() -> None:
    schede = tutte()
    diz = carica_dizionario()
    print("schede trovate           : %d   (attese: %d)" % (len(schede), ATTESE))
    if len(schede) != ATTESE:
        raise SystemExit("il sorgente si e' mosso: il conto va rifatto, non"
                         " aggiustato")

    distinte = {v["en"] for v in schede}
    print("letterali distinti       : %d   (la chiave e' il letterale)"
          % len(distinte))
    if len(distinte) != len(schede):
        raise SystemExit("due schede portano lo stesso letterale: la chiave non"
                         " basta piu'")

    rese = [v for v in schede if diz.get(v["en"], {}).get("it")]
    print("tradotte                 : %d su %d" % (len(rese), len(schede)))
    print("giunture dichiarate      : %d   (non sono schede)" % len(GIUNTURE))
    print("soffitto di larghezza    : %d colonne   (il massimo dell'inglese)"
          % _misura_inglese())

    for nome in FILE:
        righe = leggi(nome)
        rifatte, fatte = applica_a_righe(righe, nome, {})
        if rifatte != righe or fatte != 0:
            raise SystemExit("%s: col dizionario vuoto il file NON torna"
                             " identico" % nome)
    print("identita'                : i file tornano identici, 0 sostituzioni")

    guasti = 0
    for voce in schede:
        piena = diz.get(voce["en"])
        if piena is None:
            continue
        for guaio in problemi(dict(piena, file=voce["file"], riga=voce["riga"])):
            print("  %s:%d: %s" % (voce["file"], voce["riga"], guaio))
            guasti += 1
    print("rese fuori misura        : %d   (atteso: 0)" % guasti)

    segnalate = 0
    for voce in schede:
        piena = diz.get(voce["en"])
        if piena is None:
            continue
        for nota in avvisi(piena):
            print("  ⓘ %s:%d: %s" % (voce["file"], voce["riga"], nota))
            segnalate += 1
    print("rese da guardare         : %d   (avviso, non rifiuto)" % segnalate)
    if guasti:
        raise SystemExit(1)


def main() -> None:
    analizzatore = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizzatore.add_argument("--estrai", metavar="NOME")
    analizzatore.add_argument("--reimporta", metavar="LOTTO")
    analizzatore.add_argument("--applica", action="store_true")
    analizzatore.add_argument("--referto", action="store_true")
    argomenti = analizzatore.parse_args()

    if argomenti.estrai:
        print("lotto scritto: %s" % estrai(argomenti.estrai))
    elif argomenti.reimporta:
        print("rese entrate nel dizionario: %d"
              % reimporta(Path(argomenti.reimporta)))
    elif argomenti.applica:
        diz = carica_dizionario()
        for nome in FILE:
            # ⚠️⚠️ Dalla BUILD, non dal sorgente: `tcg.hsp` ha **165 toppe**, e
            # rifare il file da capo qui le butterebbe via tutte -- comprese le
            # 34 del lotto A e le 28 del lotto B scritte oggi. E' lo stesso
            # difetto che `carte.py` aveva su `tcg_mod.hsp`, dove costava una
            # toppa sola e non se n'era accorto nessuno per un anno di
            # sessioni.
            bersaglio = percorsi.BUILD_HSP / nome
            if not bersaglio.exists():
                raise SystemExit("albero di build assente: lancia prima"
                                 " `applica.py`")
            righe, fatte = applica_a_righe(leggi(nome, bersaglio), nome, diz)
            scrivi(righe, bersaglio)
            print("%s: %d schede iniettate" % (bersaglio, fatte))
    else:
        referto()


if __name__ == "__main__":
    main()
