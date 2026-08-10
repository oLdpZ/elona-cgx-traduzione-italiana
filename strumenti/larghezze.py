# strumenti/larghezze.py
"""Il tetto di un menu, misurato dove il sorgente lo dichiara.

`guida-stile.md` dice da sempre che **la larghezza e' per campo, non per file**,
ma non diceva come si misura un campo, e per i menu il metro esisteva ed era
sotto gli occhi: e' il terzo argomento che il chiamante passa a `*prompt_key`.

    txtsettamer 18
    repeat 18
        promptAdd s(cnt), key_select(cnt)
    loop
    val = promptx, prompty, 300, 1        <- 300 pixel, e il riquadro taglia

⚠️ **Il riquadro taglia, non manda a capo e non restringe il carattere.** Visto
a schermo il 2026-08-10 sul menu della frusta da domatore: otto frasi diverse
finivano allo stesso identico pixel — «…vaga lonta», «…gira qui i», «…resta
immo», «…stermina le lu» — mentre le corte si fermavano prima con il loro
margine. Otto stringhe diverse che finiscono nello stesso punto sono un taglio.

## La conversione da pixel a caratteri

Due misure a schermo, lo stesso giorno:

    300px -> 33 caratteri  (menu della frusta, dove il taglio si vedeva)
    500px -> ~59           (libro dell'abisso in inglese, con il suo margine)

da cui `caratteri = (larghezza - MARGINE) / PIXEL_PER_CARATTERE`, con 46 e 7,7.
Il margine non e' cosmetico: se ne va nella colonna della lettera di scelta
(`a)`, `b)`, …) che il riquadro disegna a sinistra di ogni voce.

Il numero e' una **misura**, non una costante del motore, e vale finche' non si
tocca il carattere. Se un giorno una voce dentro il tetto uscisse tagliata, il
posto dove correggere e' qui, e i due test che fissano i punti misurati devono
fallire prima del resto.

## Che cosa e' una voce di menu, e che cosa no

Solo le assegnazioni a `s(cnt)`. Dentro gli stessi `#deffunc` ci sono anche dei
`txt lang(...)` — le domande del quiz, per esempio `text.hsp:1310` — che sono
messaggi e non hanno nessun tetto: contarli fa gridare al difetto dove non c'e'.
E' la solita lezione: [[il-posto-decide-quando-arriva-il-dato]].

## L'inglese non e' il tetto

⚠️ In dieci menu su venti **sfora anche l'inglese**: `txtsettamer` ha una voce
inglese da 46 caratteri in un riquadro da 32, tagliata da sempre a monte. Chi
prendesse la stringa inglese come budget — come dice `guida-stile.md` per i
campi misurati a schermo — erediterebbe il difetto. Per i menu il tetto e' il
riquadro, e si controlla anche quando l'inglese lo sfora.

## Il numero dentro una dinamica

Una voce dinamica interpola un valore che a scrittura non si conosce. Si misura
sostituendo `LARGHEZZA_NUMERO` cifre: tre bastano per i valori che compaiono
qui (percentuali, costi, livelli). Dove il valore puo' essere piu' largo — il
`kane` di `txtsetclementia` arriva a sei cifre — la voce ha comunque margine di
avanzo, ma la stima resta una stima e va detto.
"""
import argparse
import json
import re
import sys
from pathlib import Path

from strumenti import percorsi
from strumenti.accenti import degrada

FILE = "text.hsp"

# misurati a schermo il 2026-08-10; vedi il docstring
PIXEL_PER_CARATTERE = 7.7
MARGINE = 46

# cifre supposte per un valore interpolato dentro una voce dinamica
LARGHEZZA_NUMERO = 3

_DEFFUNC = re.compile(r"^#deffunc\s+(\w+)")
_VOCE = re.compile(r"^\s*s\(\s*cnt\s*\)\s*=\s*lang\(")
_CHIAMATA = re.compile(r"^\s*(txt(?:set|select)\w+)\s+\w")
_PROMPT = re.compile(
    r"val\s*=\s*promptx\s*,\s*prompty\s*,\s*(\d+)(?:\s*-\s*(\d+)\s*\*\s*en)?"
)
_INTERPOLAZIONE = re.compile(r'"\s*\+\s*[^+"]+?\s*\+\s*"')


def budget(pixel: int) -> int:
    """Quanti caratteri entrano in un riquadro largo `pixel`."""
    return int((pixel - MARGINE) / PIXEL_PER_CARATTERE)


def _righe(percorso: Path) -> list[str]:
    return percorso.read_bytes().decode("cp932", "replace").split("\n")


def menu_per_riga(percorso: Path | None = None) -> dict[int, str]:
    """riga (1-based) di una voce di menu -> nome del `#deffunc` che la contiene.

    Le righe che non sono `s(cnt) = lang(...)` non entrano: chi le cerca se le
    trova assenti, invece che misurate per sbaglio.
    """
    percorso = percorso or (percorsi.SORGENTE_HSP / FILE)
    fuori: dict[int, str] = {}
    corrente = None
    for i, riga in enumerate(_righe(percorso), start=1):
        m = _DEFFUNC.match(riga)
        if m:
            corrente = m.group(1)
        elif corrente and _VOCE.match(riga):
            fuori[i] = corrente
    return fuori


def larghezze(cartella: Path | None = None) -> dict[str, int]:
    """nome del menu -> larghezza in pixel del riquadro, nella build inglese.

    Se piu' chiamanti costruiscono lo stesso menu si tiene **il piu' stretto**:
    una voce deve stare in tutti i posti in cui il menu compare.

    ⚠️ La larghezza puo' dipendere dalla lingua: `map_user.hsp:1228` scrive
    `450 - 50 * en`, cioe' 400 nella build inglese, che e' la nostra. Chi
    leggesse il primo numero e basta si darebbe 50 pixel che non ha.

    ⚠️ Il `val =` puo' stare molto piu' avanti della chiamata: i 35 menu del
    quiz sono costruiti in un `if` a testa e condividono un solo `prompt_key`
    cento righe piu' sotto (`chat.hsp:13055`). Per questo la ricerca non si
    ferma dopo poche righe, ma solo a un'etichetta o a un `#deffunc`.
    """
    cartella = cartella or percorsi.SORGENTE_HSP
    fuori: dict[str, int] = {}
    for percorso in sorted(cartella.glob("*.hsp")):
        righe = _righe(percorso)
        for i, riga in enumerate(righe):
            m = _CHIAMATA.match(riga)
            if not m:
                continue
            for j in range(i + 1, len(righe)):
                if righe[j].startswith(("#deffunc", "*")) or righe[j].lstrip().startswith("*"):
                    break
                p = _PROMPT.search(righe[j])
                if p:
                    px = int(p.group(1)) - (int(p.group(2)) if p.group(2) else 0)
                    nome = m.group(1)
                    fuori[nome] = min(fuori.get(nome, px), px)
                    break
    return fuori


def reso(italiano: str) -> str:
    """La forma che finisce nel sorgente, e quindi a schermo.

    Una dinamica e' un'espressione HSP: si tengono i pezzi letterali e ogni
    valore interpolato vale `LARGHEZZA_NUMERO` cifre. Gli accenti si degradano,
    e un accento degradato vale **due** caratteri.
    """
    testo = italiano
    if testo.lstrip().startswith('"') or '" + ' in testo:
        testo = _INTERPOLAZIONE.sub("9" * LARGHEZZA_NUMERO, testo).strip().strip('"')
    return degrada(testo)


def fuori_misura(
    dizionario: Path | None = None,
    sorgente: Path | None = None,
) -> list[tuple[str, int, int, int, int, str]]:
    """(menu, pixel, tetto, riga, lunghezza, testo) per ogni voce che sfora."""
    dizionario = dizionario or (percorsi.DIZIONARIO / (FILE + ".jsonl"))
    sorgente = sorgente or percorsi.SORGENTE_HSP
    per_riga = menu_per_riga(sorgente / FILE)
    px_per_menu = larghezze(sorgente)

    fuori = []
    for linea in dizionario.read_text(encoding="utf-8").splitlines():
        voce = json.loads(linea)
        nome = per_riga.get(voce["riga"])
        px = px_per_menu.get(nome)
        if px is None:
            continue
        testo = reso(voce.get("it") or "")
        tetto = budget(px)
        if len(testo) > tetto:
            fuori.append((nome, px, tetto, voce["riga"], len(testo), testo))
    return sorted(fuori)


def menu_senza_larghezza(sorgente: Path | None = None) -> set[str]:
    """I menu di cui non si e' trovato il chiamante: non sono misurati.

    Oggi e' vuoto, ed e' bene saperlo dal test: un menu che smette di essere
    trovato smette anche di essere controllato, in silenzio.
    """
    sorgente = sorgente or percorsi.SORGENTE_HSP
    return set(menu_per_riga(sorgente / FILE).values()) - set(larghezze(sorgente))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--tutti", action="store_true",
                   help="elenca ogni menu con il suo tetto, non solo chi sfora")
    args = p.parse_args(argv)

    px_per_menu = larghezze()
    if args.tutti:
        per_riga = menu_per_riga()
        quante: dict[str, int] = {}
        for nome in per_riga.values():
            quante[nome] = quante.get(nome, 0) + 1
        print("%-22s %6s %5s %6s" % ("menu", "pixel", "tetto", "voci"))
        for nome in sorted(px_per_menu):
            print("%-22s %6d %5d %6d"
                  % (nome, px_per_menu[nome], budget(px_per_menu[nome]), quante.get(nome, 0)))

    sfori = fuori_misura()
    if sfori:
        print()
        ultimo = None
        for nome, px, tetto, riga, n, testo in sfori:
            if nome != ultimo:
                print("\n%s  %dpx, tetto %d caratteri" % (nome, px, tetto))
                ultimo = nome
            print("   %6d  %3d  %s" % (riga, n, testo))
    print("\nvoci fuori misura: %d su %d menu misurati"
          % (len(sfori), len(px_per_menu)))

    senza = menu_senza_larghezza()
    if senza:
        print("menu non misurati (chiamante non trovato): %s" % ", ".join(sorted(senza)))
    return 1 if sfori else 0


if __name__ == "__main__":
    sys.exit(main())
