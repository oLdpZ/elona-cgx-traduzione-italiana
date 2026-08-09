# strumenti/creature.py
"""La classe che il sorgente dichiara per ogni stringa di `db_creature.hsp`.

Il file mescola due corpora che non pongono la stessa domanda:

    return lang("吸血妊婦『ママラリア』", "<Momalaria> the bloodsucker")
    cdatan(CDATAN_NAME, rc) = lang("ビッグモスキート", "big mosquito")   ← nome
    txt lang("「ガウッ」", "*gulp*")                                     ← voce

I **nomi** sono dati che finiscono nel salvataggio e che la rinomina
dell'evoluzione taglia per prefisso o per suffisso (`action.hsp:18640`): hanno
genere, plurale, e due proprieta' da rispettare che nessun occhio verifica su
mille voci. La **voce** e' prosa fra virgolette, e non ha nessuno di quei
vincoli.

Un lotto e' una classe, e una classe pone la stessa domanda: mescolarli
significherebbe tradurre mille nomi col metodo della prosa.

⚠️ **La classe la dichiara il sito, non il contenuto.** Lo stesso nome compare
due volte — una come `return`, una come assegnazione a `cdatan` — e sono la
stessa firma: e' voluto, ed e' la ragione per cui la classe si legge dalla
riga e non dalla stringa. La stessa lezione di `categorie.py` per `db_item.hsp`.

La rete e' `nessuna_firma_in_due_classi()`: oggi le due classi sono disgiunte,
e se un domani una stringa comparisse come nome **e** come voce il criterio
tornerebbe a essere un occhio in silenzio. Meglio saperlo dal test.
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path

from strumenti import percorsi

FILE = "db_creature.hsp"

# le tre forme, misurate sul sorgente pinnato: 1.297 assegnazioni a cdatan,
# 1.144 `return` dentro *db_creature2, 1.565 `txt`. Non ce ne sono altre.
_NOME = re.compile(r"^\s*(return lang\(|cdatan\(CDATAN_NAME,\s*\w+\)\s*=\s*lang\()")
_VOCE = re.compile(r"^\s*txt\s+lang\(")
_LANG = re.compile(r'lang\("((?:[^"\\]|\\.)*)", "((?:[^"\\]|\\.)*)"\)')


def classi_da_testo(testo: str) -> dict[tuple[str, str], str]:
    """(giapponese, inglese) -> 'nome' | 'voce'.

    Le righe che non sono ne' l'una ne' l'altra forma non entrano nella mappa:
    chi le chiede se le trova assenti, invece che classificate per sbaglio.
    """
    fuori: dict[tuple[str, str], str] = {}
    for riga in testo.split("\n"):
        if _NOME.match(riga):
            classe = "nome"
        elif _VOCE.match(riga):
            classe = "voce"
        else:
            continue
        for jp, en in _LANG.findall(riga):
            fuori.setdefault((jp, en), classe)
    return fuori


def classi(percorso: Path | None = None) -> dict[tuple[str, str], str]:
    percorso = percorso or (percorsi.SORGENTE_HSP / FILE)
    return classi_da_testo(percorso.read_bytes().decode("cp932"))


def nessuna_firma_in_due_classi(percorso: Path | None = None) -> set[tuple[str, str]]:
    """Le coppie che compaiono sia come nome sia come voce. Oggi: nessuna.

    `classi_da_testo` tiene la prima classe vista, quindi da sola non lo direbbe:
    qui si guarda davvero riga per riga.
    """
    percorso = percorso or (percorsi.SORGENTE_HSP / FILE)
    testo = percorso.read_bytes().decode("cp932")
    viste: dict[tuple[str, str], set[str]] = collections.defaultdict(set)
    for riga in testo.split("\n"):
        if _NOME.match(riga):
            classe = "nome"
        elif _VOCE.match(riga):
            classe = "voce"
        else:
            continue
        for coppia in _LANG.findall(riga):
            viste[coppia].add(classe)
    return {k for k, v in viste.items() if len(v) > 1}


# --- il campo che la rinomina puo' vedere -----------------------------------

_BLOCCO = re.compile(r"if\s*\(\s*dbid\s*==\s*(CREATURE_ID_[A-Z_0-9]+)\s*\)")
_NOME_ASSEGNATO = re.compile(r'cdatan\(CDATAN_NAME,\s*rc\)\s*=\s*lang\("[^"]*", "([^"]*)"\)')
_CANCELLO = re.compile(r"cdata\(CDATA_ID,\s*tc\)\s*==\s*(CREATURE_ID_[A-Z_0-9]+)")
_EVMODE = re.compile(r"^\s*evmode = (\d+)")
_RAMO = re.compile(r"^\s*if \( evmode == (\d+) \)")
_EV = re.compile(r'^\s*(evold|evname) = lang\("[^"]*", "([^"]*)"\)')


def nomi_per_creatura(percorso: Path | None = None) -> dict[str, str]:
    """CREATURE_ID -> nome inglese, letto da `db_creature.hsp`."""
    percorso = percorso or (percorsi.SORGENTE_HSP / FILE)
    fuori, blocco = {}, None
    for riga in percorso.read_bytes().decode("cp932").split("\r\n"):
        m = _BLOCCO.search(riga)
        if m:
            blocco = m.group(1)
        m = _NOME_ASSEGNATO.search(riga)
        if m and blocco:
            fuori.setdefault(blocco, m.group(1))
    return fuori


def evoluzioni(percorso: Path | None = None) -> dict[int, dict]:
    """evmode -> {'creature': {CREATURE_ID…}, 'coppie': [(evold, evname)…]}.

    ⚠️ **Il campo della rinomina non sono tutti i nomi: sono quelli che possono
    entrare in quel ramo.** L'idoneita' la decide `cdata(CDATA_ID, tc)`, quindi
    un `evold` non incontrera' mai un nome che non sta dietro al suo cancello.

    Serve saperlo, perche' senza il cancello il confronto e' pieno di agganci
    per caso: `imp` e' prefisso di `impure eye` e `zombie` di `zombie girl`, e
    una guardia che li pretendesse conservati in italiano chiederebbe che
    «occhio impuro» cominci per «folletto». Il taglio non ha un controllo di
    confine di parola, ma il cancello lo rende innocuo.
    """
    percorso = percorso or (percorsi.SORGENTE_HSP / "action.hsp")
    righe = percorso.read_bytes().decode("cp932").split("\r\n")

    cancelli: dict[int, set[str]] = collections.defaultdict(set)
    visti: list[tuple[int, str]] = []
    for i, riga in enumerate(righe):
        for m in _CANCELLO.finditer(riga):
            visti.append((i, m.group(1)))
        m = _EVMODE.match(riga)
        if m:
            n = int(m.group(1))
            cancelli[n].update(cid for j, cid in visti if 0 <= i - j <= 8)

    coppie: dict[int, list[tuple[str, str]]] = collections.defaultdict(list)
    ramo, evname = None, None
    for riga in righe:
        m = _RAMO.match(riga)
        if m:
            ramo, evname = int(m.group(1)), None
        m = _EV.match(riga)
        if m and ramo is not None:
            if m.group(1) == "evname":
                evname = m.group(2)
            elif evname is not None:
                coppie[ramo].append((m.group(2), evname))

    return {
        n: {"creature": cancelli[n], "coppie": coppie[n]}
        for n in sorted(set(cancelli) & set(coppie))
    }


def nomi_visibili(evmode: int, mappa: dict | None = None, nomi: dict | None = None) -> set[str]:
    """I nomi inglesi che il taglio di `evmode` puo' davvero incontrare.

    Sono i nomi delle creature dietro al suo cancello, **piu'** gli `evname`
    dei rami che condividono una di quelle creature: un'evoluzione incatenata
    vede il nome che le ha lasciato lo stadio prima. `evmode 5` ha il cancello
    su `DOG` e `HOUND` e cerca `Silver Fang`, che nessun cane si chiama alla
    nascita.
    """
    mappa = mappa if mappa is not None else evoluzioni()
    nomi = nomi if nomi is not None else nomi_per_creatura()
    creature = mappa[evmode]["creature"]
    fuori = {nomi[c] for c in creature if c in nomi}
    for altro in mappa.values():
        if altro["creature"] & creature:
            fuori.update(nuovo for _, nuovo in altro["coppie"])
    return fuori


# --- il nucleo atomico -------------------------------------------------------

AZIONI = "action.hsp"


def nucleo_atomico(mappa: dict | None = None, nomi: dict | None = None) -> set[str]:
    """Le stringhe inglesi che **non si possono tradurre separatamente**.

    Sono l'unione di due insiemi che il taglio della rinomina mette a confronto:
    gli `evold`/`evname` di `action.hsp` da una parte, e dall'altra i nomi di
    creatura che quel taglio puo' incontrare (`nomi_visibili`). Un `evold`
    italiano che incontra un nome ancora inglese non aggancia, e l'evoluzione
    smette di rinominare **in silenzio**: e' la ragione per cui il lotto entra
    in dizionario tutto insieme o niente.

    ⚠️ **Le stringhe sono 378, le firme 380.** Due inglesi portano due
    giapponesi diversi — `rabbit` (野うさぎ contro ウサギ) e `wild horse`
    (野生馬 contro サラブレッド, che vuol dire *purosangue*) — e la firma e'
    contenuto, quindi sono voci di dizionario distinte che **devono ricevere la
    stessa resa**. Il confronto a runtime e' fra stringhe, non fra firme: due
    rese diverse per lo stesso inglese rompono l'aggancio. Lo guarda
    `test_lo_stesso_inglese_non_riceve_due_rese`.
    """
    mappa = mappa if mappa is not None else evoluzioni()
    nomi = nomi if nomi is not None else nomi_per_creatura()
    fuori = {s for d in mappa.values() for coppia in d["coppie"] for s in coppia}
    for evmode in mappa:
        fuori |= nomi_visibili(evmode, mappa, nomi)
    return fuori


def _unici_per_firma(voci: list[dict]) -> list[dict]:
    viste, fuori = set(), []
    for voce in voci:
        if voce["firma"] not in viste:
            viste.add(voce["firma"])
            fuori.append(voce)
    return fuori


def lotto_nucleo() -> list[dict]:
    """Il lotto del nucleo: le voci dei due file, una per firma, in ordine di file.

    Da `db_creature.hsp` entrano le sole stringhe di classe **nome**: il
    filtro sull'inglese da solo prenderebbe una voce che dicesse la stessa cosa
    fra virgolette, e un nome tradotto col metodo della prosa e' proprio cio'
    che `classi()` esiste per impedire.

    Da `action.hsp` entra tutto cio' che sta nel nucleo, senza filtro di classe:
    li' non c'e' una classificazione da fare, e un `evold` e' un `evold`.
    """
    from strumenti.estrai import estrai_da_file

    bersaglio = nucleo_atomico()
    mappa = classi()
    creature = _unici_per_firma([
        v for v in estrai_da_file(percorsi.SORGENTE_HSP / FILE)
        if v["en"] in bersaglio and mappa.get((v["jp"], v["en"])) == "nome"
    ])
    azioni = _unici_per_firma([
        v for v in estrai_da_file(percorsi.SORGENTE_HSP / AZIONI)
        if v["en"] in bersaglio
    ])
    return creature + azioni


def _scrivi(voci: list[dict], uscita: str) -> None:
    percorso = Path(uscita)
    percorso.parent.mkdir(parents=True, exist_ok=True)
    with percorso.open("w", encoding="utf-8", newline="\n") as f:
        for voce in voci:
            f.write(json.dumps(voce, ensure_ascii=False) + "\n")
    print("scritto", uscita)


def main() -> None:
    sys.stdout = __import__("io").TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    p = argparse.ArgumentParser(description=f"Classi delle stringhe di {FILE}.")
    p.add_argument("--classe", choices=("nome", "voce"), help="elenca le voci di una classe")
    p.add_argument("--nucleo", action="store_true",
                   help="il nucleo atomico: nomi e stringhe di evoluzione, dai due file")
    p.add_argument("--uscita", help="scrive come lotto JSONL cio' che si e' chiesto")
    a = p.parse_args()

    mappa = classi()
    conto = collections.Counter(mappa.values())
    for k, v in sorted(conto.items()):
        print(f"{k:8} {v:5} firme")
    doppie = nessuna_firma_in_due_classi()
    print(f"firme in due classi: {len(doppie)}")

    if a.classe:
        from strumenti.estrai import estrai_da_file
        voci = [v for v in estrai_da_file(percorsi.SORGENTE_HSP / FILE)
                if mappa.get((v["jp"], v["en"])) == a.classe]
        unici = _unici_per_firma(voci)
        print(f"{a.classe}: {len(unici)} firme, {len(voci)} occorrenze")
        if a.uscita:
            _scrivi(unici, a.uscita)

    if a.nucleo:
        voci = lotto_nucleo()
        per_file = collections.Counter(v["file"] for v in voci)
        print(f"nucleo: {len(nucleo_atomico())} stringhe, {len({v['firma'] for v in voci})} firme")
        for nome_file, quante in sorted(per_file.items()):
            print(f"  {nome_file:18} {quante:4} voci")
        if a.uscita:
            _scrivi(voci, a.uscita)


if __name__ == "__main__":
    main()
