# strumenti/gemelle.py
"""Il dizionario e' per file, e una firma resa in un file non arriva all'altro.

## Che cosa fa davvero

Il dizionario vive in `dizionario/<file>.jsonl` e `applica.py` cerca la firma
**nel file che sta costruendo**. Una stringa identica in due file va quindi
tradotta due volte, e niente lo dice: `verifica --dizionario` conta le righe da
fare file per file senza accorgersi che di alcune la resa **esiste gia'**.

Trovato nella 72a dal collaudo, nel registro dei messaggi:

    You displace Tomdecker il cittadino.
    Ti scambi di posto con Chur il cane.

Stesso evento, due righe, la stessa firma `70e253be`: `action.hsp:1929` resa,
`chat.hsp:22587` no.

## Le tre classi, che non hanno lo stesso rischio

- **gemella** — la firma combacia. La firma include giapponese, inglese **e**
  l'espressione (vedi `estrai.firma`), quindi la resa e' valida *per
  costruzione*: e' esattamente la chiave che `applica` andra' a cercare, con le
  stesse variabili. Quel che resta da decidere e' il **registro**, e quello
  dipende dal sito. ✅ E' l'unica classe che finisce nel lotto pre-riempito.
- **divergente** — la firma e' gia' resa in **due modi** in due file diversi:
  «il cane» e «Cane», «un sotterraneo» e «sotterraneo». Quasi sempre e'
  legittimo — l'articolo dipende da come la frase incornicia la stringa — e la
  rete non sceglie: mette i candidati nel lotto e lascia `it` vuoto.
- **quasi gemella** — combacia solo il **giapponese**. ⚠️⚠️ Non si travasa:
  `chara_func.hsp:4369` e `map.hsp:14821` hanno lo stesso giapponese e la resa
  dell'altro porta `name(cdata(CDATA_TAGTEAM_PARTNER, tc))`, cioe' le
  **variabili dell'altro sito**. E' l'errore che il docstring di
  `estrai.firma()` descrive: una chiave troppo debole scrive codice sbagliato
  in silenzio. Sono un elenco **da leggere**.

⚠️ Il giapponese **vuoto** non fa quasi gemella. Una dinamica di sola
morfologia (`lang(name(cc), "The " + name(cc))`) non ha letterali giapponesi, e
il vuoto combacerebbe con qualunque altro vuoto.

## Perche' non e' una verifica d'apertura

I suoi numeri **scendono** man mano che si traduce: non e' una guardia con un
valore atteso, e' un elenco di lavoro. I conti vanno nella ripresa.
"""
import argparse
import json
from collections import defaultdict
from pathlib import Path

from strumenti import percorsi
from strumenti.verifica import estrai_da_testo

GEMELLA = "gemella"
DIVERGENTE = "divergente"
QUASI = "quasi"

# I file dove una `lang()` non e' un'etichetta da leggere ma una **chiave da
# confrontare**: travasarci una resa cambia il comportamento del gioco, non il
# testo a schermo. `lotto()` si rifiuta di generarli senza `--forza`.
FILE_DELICATI = {
    "custom_autopick.hsp":
        "78 delle sue 90 `lang()` sono confronti dentro `instr` contro"
        " `autopick.txt`, che scrive **il giocatore**: tradurne una cambia una"
        " chiave, non un'etichetta. E la gemella di 'armor' e' «Armatura» di"
        " db_race.hsp, cioe' maiuscola e registro di un'altra schermata.",
}


def indice(rese: list[dict]) -> dict[str, dict[str, list[dict]]]:
    """Da tutte le voci **tradotte** dei dizionari, i due modi di cercarle.

    `per_firma` e' la chiave forte (giapponese + inglese + espressione),
    `per_jp` quella debole. Il giapponese vuoto non entra in `per_jp`: e' il
    caso delle dinamiche di sola morfologia, dove combacerebbe con tutte.
    """
    per_firma: dict[str, list[dict]] = defaultdict(list)
    per_jp: dict[str, list[dict]] = defaultdict(list)
    for voce in rese:
        magra = {
            "file": voce["file"], "riga": voce["riga"],
            "it": voce["it"], "en": voce.get("en", ""),
        }
        per_firma[voce["firma"]].append(magra)
        if voce.get("jp"):
            per_jp[voce["jp"]].append(magra)
    return {"per_firma": per_firma, "per_jp": per_jp}


def confronta(nome_file: str, voci: list[dict], tradotte: set[str],
              ind: dict[str, dict[str, list[dict]]]) -> list[dict]:
    """Le righe di `nome_file` non ancora rese di cui esiste una resa altrove.

    `voci` e' l'estrazione del sorgente, `tradotte` l'insieme delle firme che il
    dizionario di questo file copre gia'. Una firma vale una riga sola: due
    occorrenze dello stesso sito sono una resa sola da scrivere.
    """
    righe: list[dict] = []
    viste: set[str] = set()
    for voce in voci:
        firma = voce["firma"]
        if firma in tradotte or firma in viste:
            continue
        viste.add(firma)

        rese = [r for r in ind["per_firma"].get(firma, []) if r["file"] != nome_file]
        if rese:
            distinte = {r["it"] for r in rese}
            classe = GEMELLA if len(distinte) == 1 else DIVERGENTE
            invariata = classe == GEMELLA and all(r["it"] == r["en"] for r in rese)
        else:
            rese = [r for r in ind["per_jp"].get(voce["jp"], []) if r["file"] != nome_file]
            if not rese:
                continue
            classe = QUASI
            invariata = False

        righe.append({
            "firma": firma, "file": nome_file, "riga": voce["riga"],
            "jp": voce["jp"], "en": voce["en"], "tipo": voce["tipo"],
            "classe": classe, "invariata": invariata, "rese": rese, "voce": voce,
        })
    return righe


# Quante righe di distanza possono avere due voci dello stesso menu. Il menu dei
# materiali di `chat.hsp:2637` mette tre righe di `if` fra una voce e l'altra;
# oltre questa distanza sono due menu diversi.
_DISTANZA_MENU = 6


def blocchi_menu(testo: str) -> list[list[int]]:
    """I numeri di riga delle `chatList`, raggruppati per menu.

    Un menu e' quel che il giocatore vede **in una schermata sola**: le voci
    stanno una sotto l'altra e si leggono insieme.
    """
    blocchi: list[list[int]] = []
    corrente: list[int] = []
    ultima = -_DISTANZA_MENU * 2
    for numero, riga in enumerate(testo.splitlines(), start=1):
        if "chatList" in riga and "lang(" in riga:
            if corrente and numero - ultima > _DISTANZA_MENU:
                blocchi.append(corrente)
                corrente = []
            corrente.append(numero)
            ultima = numero
    if corrente:
        blocchi.append(corrente)
    return blocchi


def annota_menu(righe: list[dict], testo: str, tradotte: set[str]) -> list[dict]:
    """Aggiunge a ogni riga il menu in cui sta, e quanto di quel menu copre.

    ⚠️⚠️ **Una gemella dentro un menu non e' gratis.** Le voci di `chatList` che
    stanno una sotto l'altra sono una schermata sola: tradurne tre su dodici
    porta il menu da inglese e coerente a meta' italiano e incoerente. E' la
    trappola della 64a (`db_race.hsp`, la chiave e l'etichetta) in un'altra
    forma. Misurato in `chat.hsp`: **82 delle 194 gemelle stanno dentro un menu,
    e nessuno dei 18 menu toccati sarebbe completo.**

    ⚠️ E il registro non e' salvo nemmeno per la gemella: `claw` resa in
    `text.hsp` e' «graffia», che e' il verbo del messaggio di combattimento. In
    un menu che chiede *quale stile impari* ci vuole un sostantivo.
    """
    voci_per_riga: dict[int, list[dict]] = defaultdict(list)
    for riga in righe:
        voci_per_riga[riga["riga"]].append(riga)

    tutte = estrai_da_testo(righe[0]["file"], testo) if righe else []
    per_riga: dict[int, list[dict]] = defaultdict(list)
    for voce in tutte:
        per_riga[voce["riga"]].append(voce)

    dentro: dict[int, dict] = {}
    for blocco in blocchi_menu(testo):
        voci_blocco = [v for n in blocco for v in per_riga.get(n, [])]
        # solo le righe che finiranno nel lotto: una quasi gemella non si
        # travasa, quindi nel menu resta un buco come tutte le altre
        firme_qui = {r["firma"] for n in blocco for r in voci_per_riga.get(n, [])
                     if r["classe"] != QUASI}
        if not firme_qui:
            continue
        mancanti = [
            v for v in voci_blocco
            if v["firma"] not in firme_qui and v["firma"] not in tradotte
        ]
        scheda = {
            "da": blocco[0], "a": blocco[-1], "voci": len(voci_blocco),
            "coperte": len(firme_qui), "mancanti": len(mancanti),
        }
        for numero in blocco:
            dentro[numero] = scheda

    for riga in righe:
        riga["menu"] = dentro.get(riga["riga"])
    return righe


def lotto(righe: list[dict], forza: bool = False) -> list[dict]:
    """Il lotto pre-riempito: gemelle e divergenti, mai le quasi gemelle.

    Le voci sono estrazioni normali — stessi campi di `estrai` — cosi' passano
    da `verifica` e `reimporta` come tutte le altre. La provenienza va in un
    campo con l'underscore davanti, che e' annotazione: la catena lo tollera e
    nessuno strumento lo legge, come `_chiave` in `skill.hsp`.
    """
    delicati = sorted({r["file"] for r in righe if r["file"] in FILE_DELICATI})
    if delicati and not forza:
        raise ValueError(
            f"{', '.join(delicati)}: {' '.join(FILE_DELICATI[d] for d in delicati)}"
            " Serve --forza, e serve leggerle una per una.")

    voci: list[dict] = []
    for riga in righe:
        if riga["classe"] == QUASI:
            continue
        voce = dict(riga["voce"])
        if riga["classe"] == GEMELLA:
            voce["it"] = riga["rese"][0]["it"]
            voce["_gemella"] = f"{riga['rese'][0]['file']}:{riga['rese'][0]['riga']}"
        else:
            voce["it"] = ""
            voce["_gemelle"] = [f"{r['file']}:{r['riga']} {r['it']}" for r in riga["rese"]]
        menu = riga.get("menu")
        if menu:
            voce["_menu"] = (f"{menu['da']}-{menu['a']}: {menu['coperte']} di {menu['voci']},"
                             f" ne mancano {menu['mancanti']}")
        voci.append(voce)
    return voci


def rese_del_dizionario() -> list[dict]:
    """Tutte le voci tradotte, da tutti i file di `dizionario/`."""
    rese: list[dict] = []
    for percorso in sorted(percorsi.DIZIONARIO.glob("*.jsonl")):
        for r in percorso.read_text(encoding="utf-8").splitlines():
            if r.strip():
                voce = json.loads(r)
                if voce.get("it"):
                    rese.append(voce)
    return rese


def tradotte_di(nome_file: str) -> set[str]:
    percorso = percorsi.DIZIONARIO / f"{nome_file}.jsonl"
    if not percorso.exists():
        return set()
    return {
        json.loads(r)["firma"]
        for r in percorso.read_text(encoding="utf-8").splitlines()
        if r.strip() and json.loads(r).get("it")
    }


def scandaglia(ind: dict, solo: str | None = None) -> dict[str, list[dict]]:
    """Passa tutto il sorgente e restituisce le righe per file, saltando i file puliti."""
    esito: dict[str, list[dict]] = {}
    for sorgente in sorted(percorsi.SORGENTE_HSP.glob("*.hsp")):
        if solo and sorgente.name != solo:
            continue
        testo = sorgente.read_bytes().decode("cp932")
        voci = estrai_da_testo(sorgente.name, testo)
        tradotte = tradotte_di(sorgente.name)
        righe = confronta(sorgente.name, voci, tradotte, ind)
        if righe:
            esito[sorgente.name] = annota_menu(righe, testo, tradotte)
    return esito


def main() -> None:
    analizzatore = argparse.ArgumentParser(
        description="Le rese che esistono gia' in un altro file di dizionario.")
    analizzatore.add_argument(
        "--lotto", metavar="FILE.hsp",
        help="scrive lavoro/_gemelle-<file>.jsonl con `it` pre-riempito")
    analizzatore.add_argument(
        "--forza", action="store_true",
        help="genera il lotto anche per un file delicato (leggilo riga per riga)")
    argomenti = analizzatore.parse_args()

    ind = indice(rese_del_dizionario())
    per_file = scandaglia(ind, solo=argomenti.lotto)

    if argomenti.lotto:
        righe = per_file.get(argomenti.lotto, [])
        voci = lotto(righe, forza=argomenti.forza)
        if not voci:
            print(f"{argomenti.lotto}: nessuna gemella da scrivere.")
            return
        destinazione = percorsi.LAVORO_LOTTI / f"_gemelle-{argomenti.lotto}.jsonl"
        destinazione.parent.mkdir(parents=True, exist_ok=True)
        destinazione.write_text(
            "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in voci), encoding="utf-8")
        gemelle = sum(1 for v in voci if v.get("_gemella"))
        print(f"{destinazione}: {len(voci)} voci — {gemelle} pre-riempite,"
              f" {len(voci) - gemelle} divergenti da scegliere a mano")
        return

    for classe, titolo in (
        (GEMELLA, "GEMELLE — la firma combacia, la resa e' valida per costruzione"),
        (DIVERGENTE, "DIVERGENTI — gia' resa in piu' modi: sceglie chi legge"),
        (QUASI, "QUASI GEMELLE — solo il giapponese combacia: da leggere, mai da travasare"),
    ):
        print(f"\n=== {titolo}")
        totale = 0
        for nome, righe in sorted(per_file.items(),
                                  key=lambda v: -sum(r["classe"] == classe for r in v[1])):
            conto = sum(1 for r in righe if r["classe"] == classe)
            if not conto:
                continue
            totale += conto
            gratis = sum(1 for r in righe if r["classe"] == classe and r["invariata"])
            avviso = "  ⚠️ delicato" if nome in FILE_DELICATI else ""
            in_piu = f"  ({gratis} identiche all'inglese)" if gratis else ""
            print(f"  {nome:26} {conto:5}{in_piu}{avviso}")
        print(f"  TOTALE {totale}")

    # ⚠️ Il numero che decide che cosa si puo' travasare davvero: una gemella
    # dentro un menu non si scrive da sola, si scrive col menu.
    dentro = [r for righe in per_file.values() for r in righe
              if r["classe"] != QUASI and r.get("menu")]
    if dentro:
        menu = {(r["file"], r["menu"]["da"]): r["menu"] for r in dentro}
        interi = sum(1 for m in menu.values() if not m["mancanti"])
        print(f"\n=== ⚠️ dentro un menu: {len(dentro)} gemelle in {len(menu)} menu,"
              f" di cui {interi} si chiuderebbero interi")
        print(f"    voci sorelle da scrivere per chiudere gli altri:"
              f" {sum(m['mancanti'] for m in menu.values())}")


if __name__ == "__main__":
    main()
