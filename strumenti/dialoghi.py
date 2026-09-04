"""Le battute della nuvoletta del gioco di carte (lotto D della Fase 6).

⭐⭐ **Questo riconoscitore parte da CHI PARLA, non dalla forma della stringa.**
E' il primo pezzo della rete che la 137a lascia aperta: `copertura._PROSA`
pretende due parole alfabetiche, e cosi' non vede `"One!"`, `"AIEEE!!!"`,
`"Cheapskate."`, `"Rent-free!"`. Sono battute a schermo esattamente come le
altre, e il censimento del piano diceva **52** dove i siti veri sono **77**.
Il conto e' stato rifatto, non aggiustato.

## I due modi in cui una battuta arriva alla nuvoletta

    efllistaddchat "Totally not my fault.", c@tcg          <- letterale diretto
    efllistaddchat randomchat@tcg(rnd(3)), ac@tcg          <- da un array

`efllistaddchat` (`tcg.hsp:1362`) mette il testo in `efllisttalk@tcg`, e
`tcg.hsp:1211` lo disegna con `bmes`. `efllistaddchatplayer` (`:1357`) e' la
stessa cosa con l'ancora sul giocatore. Quando l'argomento e' un array, il
nome dell'array si segna e si vanno a leggere le sue **assegnazioni**, che
portano piu' letterali sulla stessa riga:

    randomchat@tcg = "I'm not good at card games, hehe.", "What would Bethel
        play...", "Your deck is ASS, seriously!", ...

⚠️⚠️ **Piu' letterali sulla stessa riga, e lo stesso letterale su piu' righe.**
`"H means HIGHLANDER!"` sta a `:1716` e a `:7187`, `"I tire of this stupid card
game."` a `:7254` e a `:7271`. La chiave e' il letterale — come nelle schede —
ma una voce ha una **lista di siti**, e `applica` li serve tutti. Una chiave
`file:riga` non si poteva usare (la riga si sposta sotto una resa, lezione
della Fase 4), e una resa scritta due volte sarebbe una resa che diverge.

## La larghezza: non c'e' riquadro, c'e' una posizione

`bmes` disegna la battuta su una riga sola, e l'ascissa la calcola
`tcg.hsp:1366`:

    elax@tcg = 36 - strlen(sprint@tcg) * ((16 - en * 2) / 2 / 2)

cioe' la nuvoletta e' **centrata sulla carta**, e piu' la stringa e' lunga piu'
scorre a sinistra. Non c'e' niente che la spezzi e niente che la fermi: il
soffitto e' il massimo che l'inglese di monte gia' disegna, come per le schede.

⚠️ **Un a capo nella resa dove l'inglese non ce l'ha e' un rifiuto:** `bmes`
lo onora, e una nuvoletta a due righe si sovrappone alla carta di sopra.
"""
import argparse
import json
import re
from pathlib import Path

from strumenti import percorsi
from strumenti.accenti import degrada
from strumenti.commenti import righe_in_commento

FILE = ("tcg.hsp", "tcg_skill.hsp", "tcg_custom.hsp", "tcg_mod.hsp")

# ⚠️ Il numero atteso batte l'avviso (lezione delle «35 toppe» della 96a): se
# il riconoscitore ne trova altri, il sorgente si e' mosso e il conto va
# rifatto, non aggiustato.
#   49 letterali diretti + 4 `imaritsuka@tcg` + 4 `manytiadialog@tcg`
#   + 20 `randomchat@tcg` = 77 siti.
ATTESE = 77

# ⚠️ `efftalk@tcg` e' un array di battute a tutti gli effetti, ed e' **gia'
# reso**: lo copre `carte.battute()`, chiave = la costante dell'effetto,
# dizionario `dizionario/carte/efftalk.jsonl`, otto voci dalla Fase 5.
# Riconoscerlo anche qui vorrebbe dire due meccanismi che scrivono la stessa
# riga, che e' il modo in cui una resa sparisce senza che nessuno lo veda.
ARRAY_ESENTI = {
    "efftalk@tcg": "reso da `carte.battute()` (dizionario/carte/efftalk.jsonl)",
}

# ⭐⭐ Il vocabolario che ALTRI meccanismi hanno gia' scritto in italiano, e
# che queste battute devono seguire. E' un **RIFIUTO**, non un avviso: e' la
# lezione del lotto C, dove una scheda scritta a mano che dicesse ancora
# `Rare:` avrebbe spaccato il gioco in due meta' che parlano lingue diverse.
#
# ⚠️⚠️ Il caso vero sono i sette **kamui**. `tcg_skill.hsp:7302-7308` li
# ANNUNCIA nella nuvoletta, e `effdesc@tcg(TCG_EFF_KAMUI1..7)` li DESCRIVE
# nella scheda della carta — con nomi inglesi diversi per la stessa cosa:
#
#     annuncio                          descrizione (resa in Fase 5)
#     <Sigh of the Creator Gods>        <Respiration of Creative Gods>
#     <Roar of the War Gods>            <Roar of Fighting Gods>
#     <Claws of the Beast Gods>         <Assault of Beast Gods>
#     <Sentence of the Judicial Gods>   <Referee of Judicial Gods>
#     <Grudge of the Abominable Gods>   <Grudge of Abominable Gods>   <- uguale
#     <Commandment of the Hell Gods>    <Commandment of Hell Gods>    <- uguale
#
# Due grafie di monte, un traducente solo — come `Dual-Strike`/`Double-Strike`
# nelle schede. La meta' che nomina gli dei DEVE dire quel che la scheda dice
# gia', o il giocatore vede annunciare un potere e descriverne un altro.
VOCABOLARIO = {
    "Creator Gods>": "dei creatori>",
    "War Gods>": "dei guerrieri>",
    "Beast Gods>": "dei bestiali>",
    "Judicial Gods>": "dei giudici>",
    "Abominable Gods>": "dei abominevoli>",
    "Hell Gods>": "dei infernali>",
    "Chaos Child": "Figlio del Caos",
    "Deck": "mazzo",
    "Hand": "mano",
    "Field": "campo",
}

_CHIAMATA = re.compile(r"\befllistaddchat(?:player)?\s+(.+)$")
_LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')
_ARRAY = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*@tcg)\s*\(")
_ARRAY_NUDO = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*@tcg)\s*,")


def leggi(nome: str, percorso: Path | None = None) -> list[str]:
    """Le righe del file, senza terminatore.

    ⚠️ La premessa si prova PRIMA del controllo: il generatore delle toppe
    divideva su `\\r\\n` un testo che non ne aveva, otteneva **una riga sola
    lunga tutto il file**, e il controllo «una riga sola deve agganciare»
    diceva «unica» proprio perche' la divisione era fallita.
    """
    percorso = percorso or (percorsi.SORGENTE_HSP / nome)
    righe = percorso.read_bytes().decode("cp932").split("\r\n")
    if len(righe) < 500:
        raise ValueError("%s: diviso in %d righe, la divisione e' fallita e"
                         " ogni conto qui sotto sarebbe cieco"
                         % (nome, len(righe)))
    return righe


def scrivi(righe: list[str], percorso: Path) -> None:
    percorso.write_bytes("\r\n".join(righe).encode("cp932"))


def _viva(riga: str) -> bool:
    """Una riga che il compilatore legge davvero.

    In HSP il commento e' `;` **oppure** `//`. E una direttiva `#deffunc` che
    *dichiara* `efllistaddchat` non e' una chiamata: il suo `str
    efllistadd_argstr` non e' una battuta.
    """
    spoglia = riga.lstrip()
    if spoglia.startswith(";") or spoglia.startswith("//"):
        return False
    return not spoglia.startswith("#")


def array_parlanti(testi: dict[str, list[str]],
                   morte: dict[str, set[int]] | None = None) -> dict[str, list[str]]:
    """I nomi degli array che qualcuno passa a `efllistaddchat`, coi siti.

    Gli esenti restano **fuori dal risultato ma dichiarati**: sparire dal
    censimento e essere coperti da un altro meccanismo non sono la stessa cosa.
    """
    morte = morte or {}
    fuori: dict[str, list[str]] = {}
    for nome, righe in testi.items():
        for numero, riga in enumerate(righe, 1):
            if numero in morte.get(nome, set()) or not _viva(riga):
                continue
            trovato = _CHIAMATA.search(riga)
            if trovato is None:
                continue
            coda = trovato.group(1).strip()
            if coda.startswith('"') or coda.startswith("cnvtalk("):
                continue
            nome_array = _ARRAY.match(coda) or _ARRAY_NUDO.match(coda)
            if nome_array is None or nome_array.group(1) in ARRAY_ESENTI:
                continue
            fuori.setdefault(nome_array.group(1), []).append(
                "%s:%d" % (nome, numero))
    return fuori


def voci_dirette(righe: list[str], nome: str,
                 morte: set[int] | None = None) -> list[dict]:
    """I letterali passati a mano a `efllistaddchat`."""
    morte = morte or set()
    fuori = []
    for numero, riga in enumerate(righe, 1):
        if numero in morte or not _viva(riga):
            continue
        trovato = _CHIAMATA.search(riga)
        if trovato is None:
            continue
        coda = trovato.group(1).strip()
        if not (coda.startswith('"') or coda.startswith("cnvtalk(")):
            continue
        for letterale in _LETTERALE.findall(coda):
            fuori.append({"file": nome, "riga": numero, "en": letterale,
                          "come": "diretta"})
    return fuori


def voci_da_array(righe: list[str], nome: str, nomi_array: list[str],
                  morte: set[int] | None = None) -> list[dict]:
    """I letterali assegnati a un array che qualcuno fa parlare."""
    morte = morte or set()
    fuori = []
    for nome_array in nomi_array:
        assegna = re.compile(r"^\s*%s\s*(?:\([^)]*\))?\s*\+?=\s*(.*)$"
                             % re.escape(nome_array))
        for numero, riga in enumerate(righe, 1):
            if numero in morte or not _viva(riga):
                continue
            trovato = assegna.match(riga)
            if trovato is None:
                continue
            for letterale in _LETTERALE.findall(trovato.group(1)):
                fuori.append({"file": nome, "riga": numero, "en": letterale,
                              "come": nome_array})
    return fuori


def _righe_morte() -> dict[str, set[int]]:
    return {nome: righe_in_commento(percorsi.SORGENTE_HSP / nome)
            for nome in FILE}


def tutte(testi: dict[str, list[str]] | None = None,
          morte: dict[str, set[int]] | None = None) -> list[dict]:
    """Tutti i siti di battuta, nell'ordine dei file e delle righe."""
    if testi is None:
        testi = {nome: leggi(nome) for nome in FILE}
        morte = _righe_morte()
    morte = morte or {}
    nomi_array = sorted(array_parlanti(testi, morte))
    fuori = []
    for nome, righe in testi.items():
        fuori += voci_dirette(righe, nome, morte.get(nome))
        fuori += voci_da_array(righe, nome, nomi_array, morte.get(nome))
    return fuori


def carica_dizionario(percorso: Path | None = None) -> dict:
    percorso = percorso or (percorsi.DIZIONARIO / "carte" / "dialoghi.jsonl")
    if not percorso.exists():
        return {}
    fuori = {}
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        if riga.strip():
            voce = json.loads(riga)
            fuori[voce["en"]] = voce
    return fuori


def decise(dizionario: dict) -> set[str]:
    """Le chiavi che hanno una resa **o** una ragione per restare inglesi."""
    return {chiave for chiave, voce in dizionario.items()
            if voce.get("it") or voce.get("invariata")}


LARGHEZZA_MASSIMA = 0    # riempita da `_misura_inglese()` al primo uso


def _misura_inglese(siti: list[dict] | None = None) -> int:
    """Il soffitto: la battuta piu' lunga che l'inglese di monte gia' disegna.

    Non e' un riquadro (non ce n'e' uno): e' il punto oltre il quale la
    nuvoletta scorre a sinistra piu' di quanto il gioco abbia mai fatto.
    """
    global LARGHEZZA_MASSIMA
    if not LARGHEZZA_MASSIMA:
        LARGHEZZA_MASSIMA = max(len(v["en"]) for v in (siti or tutte()))
    return LARGHEZZA_MASSIMA


def problemi(voce: dict, tetto: int | None = None) -> list[str]:
    """Che cosa RIFIUTA una resa. Elenco vuoto = va bene."""
    reso = voce.get("it")
    if not reso:
        return []
    guai = []
    disegnata = degrada(reso)
    try:
        disegnata.encode("cp932")
    except UnicodeEncodeError as errore:
        guai.append("il carattere %r non esiste in CP932: il gioco non puo'"
                    " scriverlo" % disegnata[errore.start:errore.end])

    inglese = voce.get("en") or ""
    for monte, italiano in VOCABOLARIO.items():
        if monte in inglese and italiano not in disegnata:
            guai.append("il resto del gioco scrive «%s» dove questa dice"
                        " ancora «%s»: meta' gioco direbbe una cosa e meta'"
                        " l'altra" % (italiano, monte))

    if "\\n" in disegnata and "\\n" not in inglese:
        guai.append("la resa manda a capo dove l'inglese non lo fa: `bmes`"
                    " onora l'a capo e la nuvoletta finisce sulla carta di"
                    " sopra")

    tetto = tetto if tetto is not None else _misura_inglese()
    if len(disegnata) > tetto:
        guai.append("lunga %d caratteri: la nuvoletta e' centrata da"
                    " `36 - strlen * 3` (tcg.hsp:1366) e l'inglese di queste"
                    " battute non passa i %d" % (len(disegnata), tetto))
    return guai


def avvisi(voce: dict) -> list[str]:
    """Cio' che va **guardato**, non cio' che va rifiutato."""
    reso, inglese = voce.get("it"), voce.get("en")
    if not reso or not inglese:
        return []
    dopo, prima = len(degrada(reso)), len(inglese)
    if dopo > prima + 10:
        return ["%d caratteri contro %d: la nuvoletta scorre a sinistra di"
                " %d pixel piu' dell'inglese" % (dopo, prima, (dopo - prima) * 3)]
    return []


def applica_a_righe(righe: list[str], nome: str,
                    dizionario: dict) -> tuple[list[str], int]:
    """Inietta le rese. Dizionario vuoto -> le righe tornano identiche.

    ⚠️⚠️ Si cammina sul **DIZIONARIO**, non sui letterali del file, ed e' la
    lezione della 137a: al contrario, una voce il cui monte fosse cambiato non
    darebbe nessun errore — semplicemente non verrebbe trovata, e sparirebbe.

    ⚠️ E si servono **tutti** i siti di una chiave: `"H means HIGHLANDER!"` sta
    su due righe, e renderne una sola vorrebbe dire un gioco che dice due cose
    diverse nello stesso momento.
    """
    siti = voci_dirette(righe, nome) + voci_da_array(
        righe, nome, sorted(array_parlanti({nome: righe})))
    per_letterale: dict[str, list[dict]] = {}
    for sito in siti:
        per_letterale.setdefault(sito["en"], []).append(sito)

    fuori = list(righe)
    fatte = 0
    for chiave, voce in dizionario.items():
        reso = voce.get("it")
        if not reso:
            continue
        miei = per_letterale.get(chiave)
        if miei is None:
            if any(s.get("file") == nome for s in voce.get("siti", [])):
                raise ValueError(
                    "%s: il letterale su cui questa resa fu scritta non esiste"
                    " piu'. La voce va rifatta, non riagganciata: %r"
                    % (nome, chiave[:60]))
            continue
        for sito in miei:
            indice = sito["riga"] - 1
            prima = fuori[indice]
            dopo = prima.replace('"%s"' % chiave, '"%s"' % degrada(reso), 1)
            if dopo == prima:
                raise ValueError("%s riga %d: la sostituzione non ha cambiato"
                                 " niente" % (nome, sito["riga"]))
            fuori[indice] = dopo
            fatte += 1
    return fuori, fatte


def estrai(nome_lotto: str) -> Path:
    diz = carica_dizionario()
    fatte = decise(diz)
    lotto: dict[str, dict] = {}
    for sito in tutte():
        if sito["en"] in fatte:
            continue
        voce = lotto.setdefault(sito["en"], {"en": sito["en"], "it": "",
                                             "siti": []})
        voce["siti"].append({"file": sito["file"], "riga": sito["riga"],
                             "come": sito["come"]})
    bersaglio = percorsi.LAVORO_LOTTI / ("dialoghi-%s.jsonl" % nome_lotto)
    with bersaglio.open("w", encoding="utf-8") as scrittura:
        for chiave in lotto:
            scrittura.write(json.dumps(lotto[chiave], ensure_ascii=False) + "\n")
    return bersaglio


def reimporta(lotto: Path) -> int:
    bersaglio = percorsi.DIZIONARIO / "carte" / "dialoghi.jsonl"
    bersaglio.parent.mkdir(parents=True, exist_ok=True)
    diz = carica_dizionario(bersaglio)
    tetto = _misura_inglese()
    nuove = 0
    for riga in lotto.read_text(encoding="utf-8").splitlines():
        if not riga.strip():
            continue
        voce = json.loads(riga)
        if not (voce.get("it") or voce.get("invariata")):
            continue
        guai = problemi(voce, tetto)
        if guai:
            raise SystemExit("%r: %s" % (voce["en"][:40], "; ".join(guai)))
        diz[voce["en"]] = {chiave: voce[chiave]
                           for chiave in ("en", "it", "invariata", "siti")
                           if voce.get(chiave)}
        nuove += 1
    with bersaglio.open("w", encoding="utf-8") as scrittura:
        for chiave in sorted(diz):
            scrittura.write(json.dumps(diz[chiave], ensure_ascii=False) + "\n")
    return nuove


def referto() -> None:
    siti = tutte()
    diz = carica_dizionario()
    print("siti di battuta          : %d   (attesi: %d)" % (len(siti), ATTESE))
    if len(siti) != ATTESE:
        raise SystemExit("il sorgente si e' mosso: il conto va rifatto, non"
                         " aggiustato")

    distinti = {v["en"] for v in siti}
    print("letterali distinti       : %d   (la chiave e' il letterale)"
          % len(distinti))
    print("array che parlano        : %s"
          % ", ".join(sorted(array_parlanti({n: leggi(n) for n in FILE},
                                            _righe_morte()))))
    print("array esenti             : %s"
          % ", ".join("%s (%s)" % (n, r) for n, r in ARRAY_ESENTI.items()))

    fatte = decise(diz)
    rese = {c for c in distinti if diz.get(c, {}).get("it")}
    invariate = {c for c in distinti if diz.get(c, {}).get("invariata")}
    print("decise                   : %d su %d   (%d rese, %d invariate)"
          % (len(distinti & fatte), len(distinti), len(rese), len(invariate)))

    for nome in FILE:
        righe = leggi(nome)
        rifatte, quante = applica_a_righe(righe, nome, {})
        if rifatte != righe or quante != 0:
            raise SystemExit("%s: col dizionario vuoto il file NON torna"
                             " identico" % nome)
    print("identita'                : i file tornano identici, 0 sostituzioni")
    print("soffitto di larghezza    : %d caratteri   (il massimo dell'inglese)"
          % _misura_inglese(siti))

    guasti = 0
    for chiave in sorted(distinti):
        for guaio in problemi(diz.get(chiave, {}), _misura_inglese(siti)):
            print("  %r: %s" % (chiave[:40], guaio))
            guasti += 1
    print("rese fuori misura        : %d   (atteso: 0)" % guasti)

    segnalate = 0
    for chiave in sorted(distinti):
        for nota in avvisi(diz.get(chiave, {})):
            print("  ⓘ %r: %s" % (chiave[:40], nota))
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
            # ⚠️⚠️ Dalla BUILD, non dal sorgente: qui dentro ci sono `tcg.hsp`
            # con 165 toppe e `tcg_mod.hsp` coi nomi delle fasi del turno.
            # Rifare il file da capo le butterebbe via — e' il difetto che la
            # 137a ha trovato in `carte --applica` e `scene --applica`, vivo
            # da una sessione intera senza che nessun conto lo dicesse.
            bersaglio = percorsi.BUILD_HSP / nome
            if not bersaglio.exists():
                raise SystemExit("albero di build assente: lancia prima"
                                 " `applica.py`")
            righe, fatte = applica_a_righe(leggi(nome, bersaglio), nome, diz)
            scrivi(righe, bersaglio)
            print("%s: %d battute iniettate" % (bersaglio, fatte))
    else:
        referto()


if __name__ == "__main__":
    main()
