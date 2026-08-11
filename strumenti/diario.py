# strumenti/diario.py
"""Il tetto di una riga che passa da `talk_conv`, e il difetto che ci vive dentro.

`larghezze.py` misura i menu, dove il riquadro **taglia**. Qui si misura l'altra
famiglia: le stringhe che il gioco manda a capo da solo con `talk_conv`
(`init.hsp:1279`), cioe' il diario delle missioni, i messaggi lunghi, le schede.
Sono 139 siti nel solo `text.hsp`, tutti con `talk_conv s, 40 - en * 4`: nella
build inglese, dove `en` vale 1 (`config.hsp:439`), il tetto e' **36 caratteri**.

## Perche' serve un misuratore, se manda a capo da solo

Perche' l'ultima parola non passa dal controllo. Il ramo inglese di `talk_conv`
(`init.hsp:1326-1369`) accumula parola per parola cercando lo spazio successivo;
quando lo spazio non c'e' piu' — cioe' sull'**ultima parola** — esce dai due
cicli e fa `talk_conv_arg1 += msgtemp`, appendendo quel che resta **senza
guardare la larghezza**. Se l'ultima parola non ci sta nella riga aperta, sfora,
e il riquadro del diario la taglia.

⚠️ Misurato a schermo il 2026-08-11, prima riga del diario della trama:

    Forse a Lesimas, uno dei labirinti
    di Nefia a sud di Vernis, si trova qualco

La seconda riga e' di 44 caratteri contro 36, ed e' uscita mozza: `qualcosa.`
era l'ultima parola. E' un difetto **di monte**, non nostro — ma l'inglese lo
sfiora appena («…called Lesimas.», ultima parola corta) e l'italiano, che e' piu'
lungo del 20%, ci cade dentro di continuo.

## Che cosa si misura

Ogni riga che assegna un `lang()` a una variabile poi passata a `talk_conv`
dentro lo stesso blocco. La lunghezza si calcola sulla forma **degradata**, come
in `larghezze.py`: un accento vale due caratteri.

⚠️ Non tutti i `talk_conv` hanno un tetto calcolabile: `event.hsp` e `help.hsp`
lo derivano dalla dimensione della finestra (`(dx - 80) / (7 - en) - en * 4`).
Quei siti si saltano e si dichiarano, invece di indovinare un numero.
"""
import argparse
import json
import re
import sys
from pathlib import Path

from strumenti import percorsi
from strumenti.accenti import degrada

# nella build inglese; config.hsp:439
EN = 1

# cifre supposte per un valore interpolato, come in larghezze.py
LARGHEZZA_NUMERO = 3

_TALK_CONV = re.compile(r"^\s*talk_conv\s+(\w+)\s*,\s*(.+?)\s*$")
_CONFINE = re.compile(r"^(#deffunc|#defcfunc|\*\w)")
_DEFFUNC = re.compile(r"^#deffunc\s+(\w+)\s*(.*)$")
_PARAMETRO = re.compile(r"\b(?:str|int|var|double|array)\s+(\w+)")
_COPIA = re.compile(r"^\s*(\w+)\s*=\s*(\w+)\s*$")
_INTERPOLAZIONE = re.compile(r'"\s*\+\s*[^+"]+?\s*\+\s*"')
_SOLO_EN = re.compile(r"^[\d\s+\-*/()]*$")


def tetto(espressione: str) -> int | None:
    """I caratteri della riga, o `None` se il tetto dipende dalla finestra.

    Si valuta l'espressione con `en` = 1. Se dentro c'e' un identificatore che
    non sia `en` — `dx`, `ww` — il tetto non e' una costante del sorgente e non
    si indovina: si dichiara ignoto.
    """
    ridotta = espressione.replace("en", str(EN))
    if not _SOLO_EN.match(ridotta):
        return None
    try:
        return int(eval(ridotta, {"__builtins__": {}}, {}))  # noqa: S307
    except Exception:
        return None


def manda_a_capo(testo: str, larghezza: int) -> list[str]:
    """Le righe che produce il ramo inglese di `talk_conv` (`init.hsp:1326`).

    Riproduce l'algoritmo alla lettera, **compreso il difetto**: l'ultima parola
    si appende senza controllo di larghezza. Riprodurre il difetto e' il punto —
    un simulatore che lo corregge non troverebbe niente.
    """
    resto = testo
    fuori: list[str] = []
    riga = ""
    for _ in range(1000):
        lunghezza = 0
        riga = ""
        while True:
            spazio = resto.find(" ")
            p = spazio + 1 if spazio != -1 else 0
            if p == 0:
                break
            if lunghezza + p > larghezza:
                break
            riga += resto[:p]
            lunghezza += p
            resto = resto[p:]
        fuori.append(riga)
        if p == 0:
            break
    # `talk_conv_arg1 += msgtemp`: la coda entra senza passare dal controllo
    fuori[-1] += resto
    return fuori


def _testo(percorso: Path) -> list[str]:
    return percorso.read_bytes().decode("cp932", "replace").split("\n")


def deffunc_che_mandano_a_capo(cartella: Path | None = None) -> dict[str, int]:
    """nome di `#deffunc` -> tetto, per quelli che passano il PROPRIO argomento.

    ⚠️ Il secondo modo di arrivare a `talk_conv`, e la prima versione di questo
    modulo non lo vedeva. `addnews2` (`text.hsp:12100`) manda a capo il suo
    parametro, e le stringhe gliele passano i chiamanti **gia' dentro la
    chiamata**: `addnews2 lang("…", "…")`. Cercando solo le assegnazioni locali
    restavano fuori tutte le notizie, cioe' la pagina di sinistra del diario —
    proprio quella che si vedeva nello screenshot del 2026-08-11.
    """
    cartella = cartella or percorsi.SORGENTE_HSP
    fuori: dict[str, int] = {}
    for percorso in sorted(cartella.glob("*.hsp")):
        righe = _testo(percorso)
        nome, parametri = None, set()
        for riga in righe:
            m = _DEFFUNC.match(riga)
            if m:
                nome, parametri = m.group(1), set(_PARAMETRO.findall(m.group(2)))
                continue
            # ⚠️ il parametro arriva a talk_conv per COPIA: addnews2 scrive
            # `locvar_addnews2_n = addnews2_arg1` e manda a capo la copia.
            # Cercare il nome del parametro e basta non trova niente.
            copia = _COPIA.match(riga)
            if copia and nome and copia.group(2) in parametri:
                parametri.add(copia.group(1))
                continue
            t = _TALK_CONV.match(riga)
            if t and nome and t.group(1) in parametri:
                largo = tetto(t.group(2))
                if largo is not None:
                    fuori[nome] = min(fuori.get(nome, largo), largo)
    return fuori


def siti(cartella: Path | None = None) -> dict[str, dict[int, int]]:
    """file -> {riga di un `lang()` misurabile: tetto in caratteri}.

    Due modi di finire dentro `talk_conv`, e servono entrambi:

    1. **assegnazione locale.** Per ogni `talk_conv VAR, ...` si risale fino al
       confine del blocco (`#deffunc` o etichetta) raccogliendo le assegnazioni
       di `VAR` che portano un `lang(`. E' la struttura del diario: un `if` per
       stato, ognuno con la sua riga, e un solo `talk_conv` in fondo.
    2. **argomento di chiamata.** Le righe che chiamano un `#deffunc` di
       `deffunc_che_mandano_a_capo` passandogli un `lang(` — vedi il perche' li'.
    """
    cartella = cartella or percorsi.SORGENTE_HSP
    inoltrano = deffunc_che_mandano_a_capo(cartella)
    chiamata = re.compile(r"^\s*(\w+)\s+.*\blang\(") if inoltrano else None
    fuori: dict[str, dict[int, int]] = {}
    for percorso in sorted(cartella.glob("*.hsp")):
        righe = _testo(percorso)
        trovate: dict[int, int] = {}

        def segna(riga_1based: int, largo: int) -> None:
            # piu' chiamanti sullo stesso testo: vince il piu' stretto
            trovate[riga_1based] = min(trovate.get(riga_1based, largo), largo)

        for i, riga in enumerate(righe):
            if chiamata:
                c = chiamata.match(riga)
                if c and c.group(1) in inoltrano:
                    segna(i + 1, inoltrano[c.group(1)])
            m = _TALK_CONV.match(riga)
            if not m:
                continue
            largo = tetto(m.group(2))
            if largo is None:
                continue
            assegna = re.compile(r"^\s*" + re.escape(m.group(1)) + r"\s*\+?=\s*.*\blang\(")
            for j in range(i - 1, -1, -1):
                if _CONFINE.match(righe[j]):
                    break
                if assegna.match(righe[j]):
                    segna(j + 1, largo)
        if trovate:
            fuori[percorso.name] = trovate
    return fuori


def reso(italiano: str) -> str:
    """La forma che finisce a schermo: interpolazioni stimate, accenti degradati."""
    testo = italiano
    if testo.lstrip().startswith('"') or '" + ' in testo:
        testo = _INTERPOLAZIONE.sub("9" * LARGHEZZA_NUMERO, testo).strip().strip('"')
    return degrada(testo).replace('\\"', '"')


def fuori_misura(
    dizionario: Path | None = None,
    sorgente: Path | None = None,
) -> list[tuple[str, int, int, int, str]]:
    """(file, riga, tetto, lunghezza della riga peggiore, testo) per ogni resa che sfora."""
    dizionario = dizionario or percorsi.DIZIONARIO
    per_file = siti(sorgente)
    fuori = []
    for nome, tetti in per_file.items():
        percorso = dizionario / (nome + ".jsonl")
        if not percorso.exists():
            continue
        for l in percorso.open(encoding="utf-8"):
            voce = json.loads(l)
            if voce["riga"] not in tetti or not voce.get("it"):
                continue
            largo = tetti[voce["riga"]]
            testo = reso(voce["it"])
            peggiore = max(len(r.rstrip()) for r in manda_a_capo(testo, largo))
            if peggiore > largo:
                fuori.append((nome, voce["riga"], largo, peggiore, testo))
    return sorted(fuori)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tutti", action="store_true", help="elenca tutti i siti misurati col loro tetto"
    )
    argomenti = parser.parse_args(argv)

    per_file = siti()
    misurati = sum(len(v) for v in per_file.values())
    if argomenti.tutti:
        for nome, tetti in per_file.items():
            for riga, largo in sorted(tetti.items()):
                print(f"{nome}:{riga}  tetto {largo}")

    fuori = fuori_misura()
    for nome, riga, largo, peggiore, testo in fuori:
        print(f"{nome}:{riga}  tetto {largo}, riga piu' lunga {peggiore}")
        for r in manda_a_capo(testo, largo):
            segno = "!" if len(r.rstrip()) > largo else " "
            print(f"   {segno} {r}")
    print(f"\nrighe fuori misura: {len(fuori)} su {misurati} siti misurati")
    return 1 if fuori else 0


if __name__ == "__main__":
    sys.exit(main())
