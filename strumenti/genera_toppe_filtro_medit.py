# strumenti/genera_toppe_filtro_medit.py
"""Le 26 categorie del filtro oggetti nell'editor di mappe.

`map_func.hsp:2517` monta in una stringa sola le voci della casella a discesa
che filtra gli oggetti nell'editor di mappe, separate da `\\n`:

    meidtfilterlistn = "All items\\nFurniture\\nJunk\\nFood\\n..."

e la riga dopo mette in fila le costanti `FILTER_*` corrispondenti, una per
voce. Le due liste si leggono per posizione, quindi **il numero di voci non si
puo' cambiare**: il cancello lo verifica.

## Che cosa e' questo schermo, e perche' si traduce

⚠️ **L'editor di mappe non e' una schermata del gioco.** `main.hsp:186` ci
entra solo con `if ( dirinfo(4) == "medit" )`, cioe' se l'eseguibile si
**chiama** `medit`: chi gioca con `cgx-test.exe` non ci arriva mai.

⭐ Si traduce lo stesso perche' il progetto **l'ha gia' tradotto**: delle
tredici stringhe di prosa di `map_func.hsp`, dodici sono italiane nella build
da sessioni — «I dati non salvati andranno persi. Vuoi creare una mappa
nuova?», «Salva mappa con nome...», «Costa automatica». Questa era la
tredicesima, ed era l'ultimo fronte dichiarato del progetto.

## Le parole non si decidono qui

⚠️ La dichiarazione di `copertura.py` diceva che tradurre queste 26 voci
«**fisserebbe** i nomi italiani delle categorie, che il progetto non ha». Il
progetto ce li ha, e li usa il giocatore: sono le categorie dell'**autopick**
(`custom_autopick.hsp:366-:555`), decise e nel dizionario — `helm` → «elmo»,
`ore` → «minerale`, `cargo` → «merce da commercio». Questo generatore le legge
di li', e alza `KeyError` sulla voce che nessuno ha deciso.

⚠️ Tre non sono un rinvio e sono l'unica decisione nuova, segnata in `NUOVE`.

## Il tetto

⚠️ **Qui non vale la matematica in pixel del progetto**: la casella e' un
controllo nativo di Windows (`combox`), non testo disegnato da `mes`, e il
carattere e' quello dell'interfaccia di sistema. L'unica misura che il sorgente
dichiara e' la larghezza dell'oggetto:

    map_func.hsp:2533   objsize 100, 25    la casella e' larga 100 px

A ~7,5 px per carattere fanno **una tredicina di caratteri**, ed e' una stima,
non una misura come quelle delle linguette. Il cancello sta a 13 per tenere le
voci corte; chi sfora non rompe niente, si vede tagliato nella casella chiusa —
e in uno strumento che il giocatore non apre mai il prezzo di sbagliare e'
cosmetico. L'ancora inglese e' «All items», 9 caratteri.
"""
from __future__ import annotations

import json
import re

from strumenti import accenti, percorsi

TETTO = 13

RIGA_VOCI = 2517
RIGA_COSTANTI = 2518
RIGA_LARGHEZZA = 2533

# ⭐ Voce inglese -> voce del dizionario di `custom_autopick.hsp` da cui
#    prendere la parola. Le categorie dell'autopick sono quelle che il
#    GIOCATORE legge e filtra: se l'editor ne usasse altre, il progetto
#    avrebbe due vocabolari per la stessa cosa.
DALL_AUTOPICK = {
    "Furniture": "furniture",
    "Junk": "junk",
    "Food": "food",
    "Ore": "ore",
    "Tool": "tool",
    "Well": "well",
    "Tree": "tree",
    "Potion": "potion",
    "Scroll": "scroll",
    "Book": "book",
    "Spellbook": "spellbook",
    "Staff": "rod",          # FILTER_ITEM_ROD: l'inglese dell'editor dice
                             # «Staff», la costante dice `ROD`, e la costante
                             # ha ragione — sono le bacchette.
    "Range": "ranged weapon",
    "Ammo": "ammo",
    "Helm": "helm",
    "Armor": "armor",
    "Glove": "glove",
    "Boots": "boot",
    "Cloak": "cloak",
    "Girdle": "belt",        # FILTER_GIRDLE: l'autopick la chiama `belt`.
    "Shield": "shield",
    "Amulet": "necklace",    # FILTER_ACCESSORY_AMULET: l'autopick la chiama
                             # `necklace`, ed e' la stessa fessura.
    "Ring": "ring",
}

# ⚠️ Le tre che un rinvio non copre: l'unica decisione nuova, 2026-09-05.
NUOVE = {
    # FILTER_NOTHING: nessun filtro. L'autopick non ha una voce «tutto».
    "All items": "Tutti",
    # FILTER_CARGO_TRADE. L'autopick dice «merce da commercio», 18 caratteri:
    # nella casella non ci sta, e qui la parola da sola non e' ambigua.
    "Trade": "Merce",
    # FILTER_WEAPON. L'autopick distingue «arma da mischia» da «arma da tiro»,
    # e qui la voce accanto e' gia' «Arma da tiro»: la contrapposizione tiene
    # anche con la parola nuda, e «arma da mischia» sono 15 caratteri.
    "Weapon": "Arma",
}

_LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')

GENERATA = "filtro-medit"


class MonteMosso(Exception):
    """Il sorgente pinnato non ha piu' la forma su cui questo file si regge."""


def _righe() -> list[str]:
    testo = (percorsi.SORGENTE_HSP / "map_func.hsp").read_bytes().decode("cp932")
    return [r.rstrip("\r") for r in testo.split("\n")]


def riga_sorgente() -> str:
    riga = _righe()[RIGA_VOCI - 1]
    if "meidtfilterlistn = " not in riga:
        raise MonteMosso(
            "map_func.hsp:%d doveva montare `meidtfilterlistn` e dice %r."
            % (RIGA_VOCI, riga.strip()[:60]))
    return riga


def voci() -> list[str]:
    """Le 26 voci inglesi, nell'ordine in cui la casella le mostra."""
    letterali = _LETTERALE.findall(riga_sorgente())
    if len(letterali) != 1:
        raise MonteMosso(
            "map_func.hsp:%d doveva portare un letterale solo e ne porta %d."
            % (RIGA_VOCI, len(letterali)))
    return letterali[0].split("\\n")


def costanti() -> list[str]:
    riga = _righe()[RIGA_COSTANTI - 1]
    if "meditfilterlist = " not in riga:
        raise MonteMosso(
            "map_func.hsp:%d doveva portare le costanti `FILTER_*` e dice %r."
            % (RIGA_COSTANTI, riga.strip()[:60]))
    return [p.strip() for p in riga.split("=", 1)[1].split(",")]


def dall_autopick() -> dict[str, str]:
    """Le categorie gia' decise, lette dal dizionario invece che riscritte."""
    percorso = percorsi.PROGETTO / "dizionario" / "custom_autopick.hsp.jsonl"
    per_inglese: dict[str, str] = {}
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        voce = json.loads(riga)
        if voce.get("it") and 360 <= voce["riga"] <= 560:
            per_inglese.setdefault(voce["en"], voce["it"])
    fuori = {}
    for etichetta, chiave in DALL_AUTOPICK.items():
        if chiave not in per_inglese:
            raise KeyError(
                "la voce %r rinviava alla categoria %r dell'autopick, e nel "
                "dizionario quella categoria non c'e' piu'. Il rinvio esiste "
                "perche' l'editor e il filtro del giocatore usino la stessa "
                "parola: se se n'e' andata, va ridecisa, non indovinata."
                % (etichetta, chiave))
        parola = accenti.degrada(per_inglese[chiave])
        fuori[etichetta] = parola[:1].upper() + parola[1:]
    return fuori


def rese() -> dict[str, str]:
    fuori = dict(dall_autopick())
    doppi = set(fuori) & set(NUOVE)
    if doppi:
        raise KeyError(
            "%r stanno sia in DALL_AUTOPICK sia in NUOVE: una parola con due "
            "sorgenti cambia a seconda di chi la legge." % sorted(doppi))
    fuori.update({k: accenti.degrada(v) for k, v in NUOVE.items()})
    return fuori


def _controlla_geometria() -> None:
    riga = _righe()[RIGA_LARGHEZZA - 1]
    if riga.strip() != "objsize 100, 25":
        raise MonteMosso(
            "map_func.hsp:%d dichiarava la larghezza della casella con "
            "`objsize 100, 25` e ora dice %r. Il tetto di %d caratteri veniva "
            "da li'." % (RIGA_LARGHEZZA, riga.strip(), TETTO))


def problemi() -> list[str]:
    guai = []
    elenco = voci()
    if len(elenco) != len(costanti()):
        guai.append(
            "le voci sono %d e le costanti `FILTER_*` %d: le due liste si "
            "leggono per posizione, e una voce in piu' o in meno sposterebbe "
            "tutti i filtri di uno." % (len(elenco), len(costanti())))
    try:
        tabella = rese()
    except KeyError as errore:
        return guai + [str(errore)]
    for etichetta in elenco:
        if etichetta not in tabella:
            guai.append(
                "la voce %r del filtro non ha una parola italiana: o il monte "
                "ha aggiunto una categoria, o la tabella e' incompleta."
                % etichetta)
    for etichetta in sorted(set(tabella) - set(elenco)):
        guai.append(
            "%r ha una resa e nel filtro non compare piu': una riga di "
            "tabella che non serve invecchia in silenzio." % etichetta)
    for etichetta, italiano in tabella.items():
        if len(italiano) > TETTO:
            guai.append("%r -> %r: %d caratteri, e nella casella da 100 px ne "
                        "stanno una tredicina"
                        % (etichetta, italiano, len(italiano)))
        if not italiano.isascii():
            guai.append("%r -> %r: non e' ASCII, e la build e' CP932"
                        % (etichetta, italiano))
        if "\\n" in italiano or "\n" in italiano:
            guai.append("%r -> %r: il `\\n` separa le voci, e una voce che ne "
                        "porta uno ne diventerebbe due"
                        % (etichetta, italiano))
    return guai


def toppe() -> list[dict]:
    _controlla_geometria()
    tabella = rese()
    riga = riga_sorgente()
    nuova = _LETTERALE.sub(
        lambda t: '"%s"' % "\\n".join(tabella[v] for v in t.group(1).split("\\n")),
        riga)
    if nuova == riga:
        return []
    return [{
        "file": "map_func.hsp",
        "cerca": riga,
        "sostituisci": nuova,
        "motivo": (
            "Le 26 voci del filtro oggetti nell'editor di mappe "
            "(map_func.hsp:%d), montate in una stringa sola separate da `\\n` "
            "e lette per posizione insieme alle costanti `FILTER_*` della riga "
            "dopo — quindi il NUMERO di voci non si tocca, e un cancello lo "
            "verifica. ⚠️ L'editor di mappe non e' una schermata del gioco: "
            "`main.hsp:186` ci entra solo `if ( dirinfo(4) == \"medit\" )`, "
            "cioe' se l'eseguibile si CHIAMA `medit`. Si traduce lo stesso "
            "perche' delle 13 stringhe di prosa del file 12 sono italiane "
            "nella build da sessioni, e questa era la tredicesima. ⭐ Le "
            "parole non si decidono qui: 23 su 26 le legge dalle categorie "
            "dell'AUTOPICK (`custom_autopick.hsp:366-:555`), che sono quelle "
            "che il giocatore filtra davvero — la dichiarazione di "
            "`copertura.py` diceva che tradurle «fisserebbe i nomi italiani "
            "delle categorie, che il progetto non ha», e il progetto ce li ha. "
            "⚠️ Il tetto qui e' una STIMA e non una misura: la casella e' un "
            "`combox`, un controllo nativo di Windows, e l'unico numero "
            "dichiarato e' `objsize 100, 25` (:2533) — una tredicina di "
            "caratteri. Chi sfora si vede tagliato nella casella chiusa, in "
            "uno strumento che il giocatore non apre. "
            "Generata da `strumenti/genera_toppe_filtro_medit.py`."
            % RIGA_VOCI),
        "generata": GENERATA,
    }]


def scrivi() -> int:
    mie = toppe()
    righe = _righe()
    for toppa in mie:
        if righe.count(toppa["cerca"]) != 1:
            raise SystemExit("la riga da cercare non e' unica")
    percorso = percorsi.PROGETTO / "toppe.jsonl"
    esistenti = [json.loads(r) for r in
                 percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    altre = [t for t in esistenti if t.get("generata") != GENERATA]
    with percorso.open("w", encoding="utf-8", newline="\n") as f:
        for toppa in altre + mie:
            f.write(json.dumps(toppa, ensure_ascii=False) + "\n")
    print("  toppe a mano o d'altri generatori: %d, generate qui: %d "
          "(ne sostituiscono %d)"
          % (len(altre), len(mie), len(esistenti) - len(altre)))
    return len(mie)


def main() -> None:
    import argparse
    analizzatore = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizzatore.add_argument("--scrivi", action="store_true",
                              help="riscrive le toppe generate in toppe.jsonl")
    argomenti = analizzatore.parse_args()

    _controlla_geometria()
    guai = problemi()
    print("  voci del filtro       : %d" % len(voci()))
    print("  costanti FILTER_*     : %d" % len(costanti()))
    if not guai:
        tabella = rese()
        print("  lette dall'autopick   : %d" % len(DALL_AUTOPICK))
        print("  decise qui            : %d" % len(NUOVE))
        piu_lunga = max(tabella.values(), key=len)
        print("  la piu' lunga         : %r, %d caratteri (tetto %d)"
              % (piu_lunga, len(piu_lunga), TETTO))
    for guaio in guai:
        print("  ⚠️", guaio)
    if argomenti.scrivi and not guai:
        scrivi()
    print("\n  " + ("genera_toppe_filtro_medit: 26 voci, 26 costanti, nessuna "
                    "fuori misura" if not guai
                    else "genera_toppe_filtro_medit: %d guai" % len(guai)))
    raise SystemExit(1 if guai else 0)


if __name__ == "__main__":
    main()
