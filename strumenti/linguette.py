# strumenti/linguette.py
"""Il tetto delle linguette di `drawmenu`, misurato a schermo il 2026-08-17.

Sono le quattro file di schede in cima alle finestre grandi — `Chara / Wear /
Feat / Material` sulla scheda del personaggio, `Spell / Skill / Wide Skill`,
`Log / Journal / Chat`, `Chart / City / Law` — e nessuna rete le guardava:
`larghezze.py` misura i menu di `*prompt_key`, `riquadri.py` le piastrelle
dell'HUD, `menu_dialogo.py` le voci di `chatList`, `diario.py` il diario. Queste
non passano da nessuno dei quattro.

## Da dove viene il numero

Misurato sulla schermata della scheda del personaggio, finestra intera
1920x1080, `windoww - 260 = 1660`:

    Chara     1691-1724   34 px / 5 car = 6,80    centro 1707,5  (atteso 1706)
    Wear      1742-1770   29 px / 4 car = 7,25    centro 1756    (atteso 1756)
    Feat      1792-1820   29 px / 4 car = 7,25    centro 1806    (atteso 1806)
    Material  1832-1886   55 px / 8 car = 6,90    centro 1859    (atteso 1856)

⚠️ **Il gioco stima il proprio carattere piu' stretto di quel che e'.**
`module.hsp:5184` centra il testo con `46 - strlen(s(cnt)) * 3`, cioe' suppone
**6** px per carattere; il carattere vero ne misura **7**. Il testo esce percio'
spostato a destra rispetto al centro dell'icona (di 3,5 px su «Material», e si
vede nella misura qui sopra) e cresce verso destra piu' di quanto il centraggio
compensi.

Con il passo di 50 px fra le celle (`module.hsp:5176`), il testo della linguetta
`i` finisce a `46 + 4*L(i)` e quello della `i+1` comincia a `96 - 3*L(i+1)`.
Le due non si toccano se

    4 * L(i) + 3 * L(i+1) <= 50

⭐ **La formula la prova l'inglese**: `Skill`(5) + `Wide Skill`(10) fa
`20 + 30 = 50`, cioe' tocca il limite **esatto**. Nessun'altra coppia inglese ci
arriva e nessuna lo supera — il che sarebbe una coincidenza notevole se il conto
fosse sbagliato.

E per l'ultima linguetta della fila vale il bordo destro della barra `window2`,
misurato a 1897:

    L(ultima) <= 10       e `Wide Skill` e' 10 esatti

⚠️ **Il tetto NON e' «50 / 7 = 7 caratteri»**, che sarebbe la lettura ingenua.
Una linguetta lunga sta benissimo se la sua vicina di destra e' corta, ed e'
esattamente il caso di `Wide Skill`. Il vincolo e' sulla **coppia**, non sulla
voce: e' la stessa forma del tetto di `riquadri.py` (una colonna) vista da
un'altra parte, ma qui il vicino conta.

💡 E il tetto e' asimmetrico, che e' la cosa meno ovvia di tutte: la penalita' e'
**4** sulla linguetta di sinistra e **3** su quella di destra, perche' il
centraggio sbagliato spinge tutto verso destra. Scambiare due rese fra vicine
puo' far passare una coppia che sforava.
"""
import json
import sys
from pathlib import Path

from strumenti import percorsi
from strumenti.accenti import degrada
from strumenti.estrai import siti

# la geometria, letta dal sorgente
PASSO = 50            # module.hsp:5176, `cnt * 50`
CENTRAGGIO = 3        # module.hsp:5184, `46 - strlen * 3`: quel che il gioco suppone
SCOSTAMENTO = 46      # module.hsp:5184, il centro della cella

# misurato a schermo il 2026-08-17 su quattro etichette: da 6,80 a 7,25
PIXEL_PER_CARATTERE = 7

# Il testo della linguetta `i` finisce a `46 + 4*L(i)` e quello della `i+1`
# comincia a `50 + 46 - 3*L(i+1)`: il tetto e' la differenza fra i due
# scostamenti, cioe' **il passo stesso**. Lo `SCOSTAMENTO` si semplifica perche'
# e' lo stesso in tutte e due le celle — e vale la pena scriverlo cosi' invece
# che «50», perche' se un domani il passo cambia il tetto lo segue da solo.
TETTO_COPPIA = PASSO
# bordo destro della barra `window2`, misurato a 1897 sulla stessa schermata
TETTO_ULTIMA = 10

FILE = "module.hsp"


def file_di_linguette(sorgente: Path | None = None) -> dict[int, list[tuple[str, str]]]:
    """riga -> [(firma, inglese), ...] nell'ordine in cui `drawmenu` le disegna.

    ⚠️ Si leggono dal **corpo di `drawmenu`**, non da una lista scritta a mano:
    una quinta fila aggiunta da un aggiornamento CGX deve entrare nel referto da
    sola, invece di restare fuori in silenzio come ci e' restato per intero
    questo pezzo di schermo fino alla 56a.

    Il font della fila lo sceglie `module.hsp:5168` una volta per tutte, quindi
    non c'e' da distinguere: tutte le linguette hanno lo stesso corpo.
    """
    sorgente = sorgente or percorsi.SORGENTE_HSP
    testo = (sorgente / FILE).read_bytes().decode("cp932")
    righe = testo.splitlines()

    dentro = False
    nostre: set[int] = set()
    for numero, riga in enumerate(righe, start=1):
        spoglia = riga.strip()
        if spoglia.startswith("#deffunc"):
            dentro = spoglia.startswith("#deffunc drawmenu")
            continue
        if dentro and spoglia.startswith("s = lang("):
            nostre.add(numero)

    per_riga: dict[int, list[tuple[str, str]]] = {}
    for sito in siti(testo):
        numero, chiave, grezzo = sito[0], sito[1], sito[6]
        if numero in nostre:
            per_riga.setdefault(numero, []).append((chiave, grezzo.strip().strip('"')))
    return per_riga


def _dizionario(percorso: Path | None = None) -> dict[str, dict]:
    percorso = (percorso or percorsi.DIZIONARIO) / (FILE + ".jsonl")
    if not percorso.exists():
        return {}
    return {
        v["firma"]: v
        for v in (json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines() if r.strip())
    }


def rese(dizionario: Path | None = None,
         sorgente: Path | None = None) -> dict[int, list[tuple[str, str]]]:
    """riga -> [(inglese, quel che arriva a schermo), ...].

    Una linguetta non ancora tradotta si misura **sull'inglese**: e' quel che il
    giocatore vede adesso, e il referto non deve dire «zero fuori misura» per una
    fila che nessuno ha ancora toccato.
    """
    voci = _dizionario(dizionario)
    fuori: dict[int, list[tuple[str, str]]] = {}
    for numero, elenco in file_di_linguette(sorgente).items():
        fila = []
        for chiave, inglese in elenco:
            voce = voci.get(chiave)
            italiano = (voce or {}).get("it") or ""
            fila.append((inglese, degrada(italiano) if italiano else inglese))
        fuori[numero] = fila
    return fuori


def costo(sinistra: str, destra: str) -> int:
    """Quanto occupa la coppia, nella misura in cui il tetto la conta."""
    return (PIXEL_PER_CARATTERE - CENTRAGGIO) * len(sinistra) + CENTRAGGIO * len(destra)


def fuori_misura(dizionario: Path | None = None,
                 sorgente: Path | None = None) -> list[tuple[int, str, str, int]]:
    """(riga, sinistra, destra, costo) per ogni coppia che si sovrappone.

    L'ultima della fila compare con `destra` vuota: li' il vicino e' il bordo.
    """
    guasti = []
    for numero, fila in sorted(rese(dizionario, sorgente).items()):
        testi = [t for _, t in fila]
        for prima, dopo in zip(testi, testi[1:]):
            quanto = costo(prima, dopo)
            if quanto > TETTO_COPPIA:
                guasti.append((numero, prima, dopo, quanto))
        if testi and len(testi[-1]) > TETTO_ULTIMA:
            guasti.append((numero, testi[-1], "", len(testi[-1])))
    return guasti


def main(argv: list[str] | None = None) -> int:
    tutte = rese()
    quante = sum(len(f) for f in tutte.values())
    guasti = fuori_misura()

    print("linguette: %d in %d file di `drawmenu`" % (quante, len(tutte)))
    print("tetto: 4*L(i) + 3*L(i+1) <= %d fra vicine; L <= %d per l'ultima"
          % (TETTO_COPPIA, TETTO_ULTIMA))
    for numero, fila in sorted(tutte.items()):
        testi = [t for _, t in fila]
        coppie = " ".join(
            "%d" % costo(a, b) for a, b in zip(testi, testi[1:]))
        print("  %s:%-6d %-42s  coppie: %s"
              % (FILE, numero, " | ".join(testi), coppie))
    for numero, sinistra, destra, quanto in guasti:
        if destra:
            print("  FUORI %s:%d  %r + %r = %d" % (FILE, numero, sinistra, destra, quanto))
        else:
            print("  FUORI %s:%d  %r e' l'ultima e fa %d caratteri"
                  % (FILE, numero, sinistra, quanto))
    print("\ncoppie fuori misura: %d" % len(guasti))
    return 1 if guasti else 0


if __name__ == "__main__":
    sys.exit(main())
