# strumenti/riquadri.py
"""I due riquadri che non sono menu, e che nessuno misurava.

`larghezze.py` misura i menu, e li trova perche' passano tutti da
`*prompt_key` con un `val = promptx, prompty, <pixel>`. Questi due siti non ci
passano, quindi non erano ne' misurati ne' sospettati:

1. **Le piastrelle degli stati nell'HUD.** `screen.hsp` disegna ogni etichetta
   (`Veleno`, `Confusione`, `Marchio`) su una piastrella copiata da
   `gcopy ..., 416, 65 + en * N, 15`, col testo che parte a `sx + 6`. Nella
   build inglese sono **80** o **95** pixel.
2. **La colonna del menu tattiche del mod.** `custom_ai.hsp:3173` dispone le
   voci ogni **145** pixel, e con la condizione `Buff` ci elenca dentro
   **tutti** i `buffname` (`:3138`).

## Perche' si contano i caratteri, e non e' una stima

Il carattere della build inglese e' **`Courier New`** (`config.txt`, riga
`font2.`), che e' **monospaziato**: il passo e' `0,6 * corpo`, sempre. I due
corpi che servono qui sono quelli che il sorgente dichiara accanto ai due siti:
`13 - en * 2` = **11 px** per l'HUD (`screen.hsp:398`), `14 - en * 2` = **12
px** per il menu tattiche (`custom_ai.hsp:3169`).

    piastrella 80 px -> (80 - 6) / 6,6 = 11 caratteri
    piastrella 95 px -> (95 - 6) / 6,6 = 13 caratteri
    colonna   145 px ->  145      / 7,2 = 20 caratteri

⚠️ **La colonna non toglie il margine**, la piastrella si': il passo di 145 e'
la distanza fra due testi, che partono tutti e due allo stesso `+18`, mentre
sulla piastrella il testo parte a `+6` da un bordo che sta fermo.

## Le due ancore, che dicono cose diverse

Verificate a schermo il 2026-08-13, ed e' l'unico giorno in cui qualcuno le ha
guardate:

- «Marchio letale» e' 14 caratteri e usciva **«Marchio letal»**, cioe' 13: il
  conto cade dove cade il taglio;
- «Crescita della magia» e' 20 e **non** toccava la colonna dopo, mentre
  «Crescita della destre|Cambio di forma (A)» ci si sovrapponeva sopra.

⚠️ **I due riquadri si rompono in modo diverso.** La piastrella **taglia** al
bordo; la colonna **sconfina** sulla colonna accanto, perche' `cs_list` non
tronca. La seconda e' peggio: non perdi una lettera, rendi illeggibili due voci.

⚠️ **E l'inglese di upstream le rispetta**, al contrario dei `buffdesc` dove
46 su 63 sfondano da sempre: sulla colonna sono **0 su 71**, sulle piastrelle
2 su 61. Qui il tetto e' un vincolo vero, non un difetto ereditato.
Vedi `decisioni.md`, «Due tetti che nessuno aveva misurato».
"""
import json
import re
from pathlib import Path

from strumenti import percorsi
from strumenti.accenti import degrada

FILE_HUD = "screen.hsp"
FILE_STATI = "text.hsp"
FILE_TATTICHE = "custom_ai.hsp"
FILE_BUFF = "buff.hsp"

# `Courier New` e' monospaziato e il suo passo e' sei decimi del corpo
RAPPORTO_COURIER = 0.6

CORPO_HUD = 11        # screen.hsp:398, `13 - en * 2`
CORPO_TATTICHE = 12   # custom_ai.hsp:3169, `14 - en * 2`

INSET = 6             # il testo della piastrella parte a `sx + 6`
COLONNA_TATTICHE = 145

# la piastrella degli stati si riconosce dal 416: e' la riga della grafica
# nel foglio, e distingue queste `gcopy` da tutte le altre della schermata
_PIASTRELLA = re.compile(
    r"gcopy\s+\S+\s*,\s*[^,]+,\s*416\s*,\s*(\d+)\s*\+\s*en\s*\*\s*(\d+)")
_DISEGNO = re.compile(r"^\s*mes\s+(_con\w+)")
_ETICHETTA = re.compile(r"^\s*(_con\w+)\s*=")
_BUFFNAME = re.compile(r"^\s*buffname\(\s*(\w+)\s*\)\s*=")
_COLONNA = re.compile(r"cs_list.*?wx\s*\+\s*\d+\s*\+\s*\(\s*(\d+)\s*\*\s*\(\s*cnt")
_ELENCO_BUFF = re.compile(r"listn\(\s*0\s*,\s*\w+\s*\)\s*=\s*buffname\(")


def budget_piastrella(pixel: int) -> int:
    """Quanti caratteri entrano in una piastrella larga `pixel`."""
    return int((pixel - INSET) / (CORPO_HUD * RAPPORTO_COURIER))


def budget_colonna(pixel: int = COLONNA_TATTICHE) -> int:
    """Quanti caratteri entrano in una colonna del menu tattiche."""
    return int(pixel / (CORPO_TATTICHE * RAPPORTO_COURIER))


def _righe(percorso: Path) -> list[str]:
    return percorso.read_bytes().decode("cp932", "replace").split("\n")


def _cartella(cartella: Path | None) -> Path:
    return cartella or percorsi.SORGENTE_HSP


def _disegni(cartella: Path | None = None) -> dict[str, int | None]:
    """etichetta di stato -> pixel della sua piastrella, `None` se non ne ha.

    ⚠️ Se la stessa etichetta e' disegnata in piu' punti si tiene **la
    piastrella piu' stretta**: la resa deve starci in tutti i posti in cui
    compare, non nel piu' comodo.

    ⚠️ **La piastrella e' quella disegnata subito prima, e «subito» non si
    misura in righe.** Una prima versione risaliva di sei righe e prendeva la
    prima `gcopy` che trovava: un'etichetta priva della propria si sarebbe
    presa in silenzio quella dell'etichetta precedente, cioe' un tetto che non
    e' il suo. Risalendo ci si ferma alla prima delle due cose che si
    incontrano — la `gcopy` e' sua solo se arriva **prima** di un'altra `mes`.
    """
    righe = _righe(_cartella(cartella) / FILE_HUD)
    trovate: dict[str, int | None] = {}
    for i, riga in enumerate(righe):
        m = _DISEGNO.match(riga)
        if not m:
            continue
        px = None
        for j in range(i - 1, -1, -1):
            if _DISEGNO.match(righe[j]):
                break
            g = _PIASTRELLA.search(righe[j])
            if g:
                px = int(g.group(1)) + int(g.group(2))
                break
        nome = m.group(1)
        if px is None:
            trovate.setdefault(nome, None)
        elif trovate.get(nome) is None:
            trovate[nome] = px
        else:
            trovate[nome] = min(trovate[nome], px)
    return trovate


def piastrelle(cartella: Path | None = None) -> dict[str, int]:
    """etichetta di stato -> pixel della sua piastrella, nella build inglese.

    ⚠️ `65 + en * 15` sono **80** pixel da noi, non 65: chi leggesse il primo
    numero si darebbe una piastrella che non ha.
    """
    return {n: px for n, px in _disegni(cartella).items() if px is not None}


def etichette_senza_piastrella(cartella: Path | None = None) -> set[str]:
    """Le etichette disegnate senza una `gcopy` sopra: non sono misurabili.

    Oggi e' vuoto, ed e' bene saperlo da un test: un'etichetta che smette di
    trovare la sua piastrella smette anche di essere controllata, in silenzio.
    """
    return {n for n, px in _disegni(cartella).items() if px is None}


def _stati_per_riga(cartella: Path | None = None) -> dict[int, tuple[str, int]]:
    """riga di `text.hsp` -> (etichetta, pixel della piastrella).

    ⚠️ Le etichette stanno in **array**: una riga sola porta fino a undici voci
    di dizionario, e `occorrenza` e' 0 per tutte. Quello che le accomuna, ed e'
    l'unica cosa che conta qui, e' la piastrella su cui finiscono.
    """
    misurate = piastrelle(cartella)
    fuori: dict[int, tuple[str, int]] = {}
    for i, riga in enumerate(_righe(_cartella(cartella) / FILE_STATI), start=1):
        m = _ETICHETTA.match(riga)
        if m and m.group(1) in misurate:
            fuori[i] = (m.group(1), misurate[m.group(1)])
    return fuori


def piastrella_per_riga(cartella: Path | None = None) -> dict[int, int]:
    """riga di `text.hsp` -> pixel della piastrella su cui finisce."""
    return {r: px for r, (_, px) in _stati_per_riga(cartella).items()}


def _buffname_per_riga(cartella: Path | None = None) -> dict[int, str]:
    righe = _righe(_cartella(cartella) / FILE_BUFF)
    return {i: m.group(1)
            for i, riga in enumerate(righe, start=1)
            if (m := _BUFFNAME.match(riga))}


def righe_buffname(cartella: Path | None = None) -> set[int]:
    """Le righe di `buff.hsp` che assegnano un `buffname`.

    ⚠️ I `bufftxt` **non** entrano: sono pezzi di frase, non voci d'elenco, e
    misurarli farebbe gridare al difetto su righe che nessuna colonna tocca.
    """
    return set(_buffname_per_riga(cartella))


def colonna_dal_sorgente(cartella: Path | None = None) -> int:
    """Il passo della colonna, letto da `custom_ai.hsp` invece che ricordato.

    ⚠️ **Gli elenchi a colonne di quel file sono quattro**, e tre hanno un
    passo diverso: 150 pixel su quindici righe (`:1263`, `:1337`, `:1821`),
    contro i 145 su ventidue del menu dei potenziamenti (`:3174`). Una guardia
    che prendesse la prima `cs_list` misurerebbe un menu che non e' quello che
    sta controllando, e il verdetto sarebbe giusto per sbaglio: 150 / 7,2 fa
    comunque 20. Quindi si parte da dove i `buffname` vengono elencati
    (`:3138`) e si scende fino alla `cs_list` che li disegna.

    💡 Gli altri tre elencano azioni e **nomi di incantesimo**, che sono
    tradotti anche loro: sono un tetto da guardare, non un tetto guardato.
    Vedi `RIPRESA-sessione.md`, «Domande aperte».
    """
    righe = _righe(_cartella(cartella) / FILE_TATTICHE)
    for i, riga in enumerate(righe):
        if not _ELENCO_BUFF.search(riga):
            continue
        for successiva in righe[i:]:
            m = _COLONNA.search(successiva)
            if m:
                return int(m.group(1))
    raise LookupError(
        "nessuna `cs_list` a colonne dopo l'elenco dei buffname in " + FILE_TATTICHE)


def _voci(dizionario: Path, nome: str) -> list[dict]:
    percorso = dizionario / (nome + ".jsonl")
    return [json.loads(l) for l in percorso.read_text(encoding="utf-8").splitlines() if l.strip()]


def _testo(voce: dict, lingua: str) -> str:
    if lingua == "en":
        return voce.get("en") or ""
    return degrada(voce.get("it") or "")


def fuori_misura_stati(
    dizionario: Path | None = None,
    sorgente: Path | None = None,
    lingua: str = "it",
) -> list[tuple[str, int, int, int, int, str]]:
    """(etichetta, pixel, tetto, riga, lunghezza, testo) per ogni resa che sfora."""
    dizionario = dizionario or percorsi.DIZIONARIO
    per_riga = _stati_per_riga(sorgente)

    fuori = []
    for voce in _voci(dizionario, FILE_STATI):
        dati = per_riga.get(voce["riga"])
        if dati is None:
            continue
        nome, px = dati
        testo = _testo(voce, lingua)
        if not testo:
            continue
        tetto = budget_piastrella(px)
        if len(testo) > tetto:
            fuori.append((nome, px, tetto, voce["riga"], len(testo), testo))
    return sorted(fuori)


def fuori_misura_tattiche(
    dizionario: Path | None = None,
    sorgente: Path | None = None,
    lingua: str = "it",
) -> list[tuple[str, int, int, int, str]]:
    """(buffname, tetto, riga, lunghezza, testo) per ogni resa che sfora."""
    dizionario = dizionario or percorsi.DIZIONARIO
    per_riga = _buffname_per_riga(sorgente)
    tetto = budget_colonna(colonna_dal_sorgente(sorgente))

    fuori = []
    for voce in _voci(dizionario, FILE_BUFF):
        nome = per_riga.get(voce["riga"])
        if nome is None:
            continue
        testo = _testo(voce, lingua)
        if not testo:
            continue
        if len(testo) > tetto:
            fuori.append((nome, tetto, voce["riga"], len(testo), testo))
    return sorted(fuori)


def _referto() -> int:
    stati = fuori_misura_stati()
    tattiche = fuori_misura_tattiche()
    piastrelle_misurate = piastrelle()
    voci_stati = len(_voci(percorsi.DIZIONARIO, FILE_STATI))

    for nome, px, tetto, riga, lung, testo in stati:
        print("%-16s %3dpx tetto %2d  %s:%d  %2d caratteri  %s"
              % (nome, px, tetto, FILE_STATI, riga, lung, testo))
    print("\netichette di stato fuori misura: %d su %d piastrelle misurate"
          % (len(stati), len(piastrelle_misurate)))

    for nome, tetto, riga, lung, testo in tattiche:
        print("%-24s tetto %2d  %s:%d  %2d caratteri  %s"
              % (nome, tetto, FILE_BUFF, riga, lung, testo))
    print("buffname fuori misura: %d su %d, colonna da %d px, tetto %d caratteri"
          % (len(tattiche), len(righe_buffname()), colonna_dal_sorgente(),
             budget_colonna(colonna_dal_sorgente())))

    senza = etichette_senza_piastrella()
    if senza:
        print("\n⚠️ etichette disegnate senza piastrella: " + ", ".join(sorted(senza)))
    if voci_stati and not piastrelle_misurate:
        print("⚠️ nessuna piastrella trovata: la guardia non sta guardando niente")
    return 1 if (stati or tattiche) else 0


if __name__ == "__main__":
    raise SystemExit(_referto())
