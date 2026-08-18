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

## Le due strade per arrivare allo stesso riquadro

Fino al 2026-08-18 la rete guardava **solo `text.hsp`**, ed era un punto cieco
che la 57a, la 58a e la 59a avevano segnalato senza chiuderlo. Le strade sono
due, e la seconda e' la piu' grossa:

    text.hsp   #deffunc txtset* riempie s(cnt), il chiamante fa promptAdd s(cnt)
               e dichiara il riquadro poco sotto -> 75 menu, 412 voci
    altrove    una corsa di `promptAdd lang(...)` chiusa dallo stesso
               `gosub *prompt_key` -> 92 siti, 261 voci

⚠️ **Il metro sta in `*prompt_key`, non nel nome dei parametri.** `system.hsp`
legge `val` cosi': `sx = val - val(2) / 2` (`:4272`), `sy = val(1) - ...`
(`:4273`), `gfini val(2) - 17` (`:4275`). La larghezza e' il **terzo campo**,
comunque siano scritti i primi due — `promptx, prompty, 300` ma anche
`promptx, 240, 160` (chara.hsp) e `basex@tcg + 400, basey@tcg + 230, 300`
(tcg.hsp). Cercare `promptx, prompty, N` ne trova venti su novantadue.

⚠️ E la lingua allarga il riquadro **in tutt'e due i versi**: `450 - 50 * en`
lo stringe a 400, `180 + ( en * 50 )` lo allarga a 230. Chi legge il primo
numero e basta grida al difetto sul menu del voto, che invece ha margine.

⚠️ Per questo la ricerca parte dal `gosub *prompt_key` e cammina **all'indietro**:
ci sono `val =` a cinque campi che non dichiarano nessun riquadro
(`winposy(90), 12, 1, 0` e' un campo d'immissione, e il 12 sono cifre), e
partire da loro inventa menu che non esistono. I `#define` di `init.hsp:19`-`:33`
si saltano per lo stesso motivo: il `gosub` che portano dentro e' il corpo di
una macro, non un sito.

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
_CHIAMATA = re.compile(r"^\s*(\w+)\s+\w")
_INTERPOLAZIONE = re.compile(r'"\s*\+\s*[^+"]+?\s*\+\s*"')
_SOLO_ARITMETICA = re.compile(r"^[\d\s+\-*/()]+$")
_ADD = re.compile(r"\bpromptAdd\s+\S")
_PROMPT_KEY = re.compile(r"gosub\s+\*prompt_key\b")
_VAL = re.compile(r"^\s*val\s*=\s*(.+?)\s*$")

# quanto indietro si cerca il `val =` che dichiara il riquadro: i menu piu`
# lunghi (command.hsp:5952-:6172) ne occupano duecento
FINESTRA = 400


def budget(pixel: int) -> int:
    """Quanti caratteri entrano in un riquadro largo `pixel`."""
    return int((pixel - MARGINE) / PIXEL_PER_CARATTERE)


def campi(espressione: str) -> list[str]:
    """Spezza gli argomenti di un `val =` sulle virgole di primo livello.

    Serve perche' la larghezza e' il **terzo campo** e i primi due possono
    portarsi dentro delle virgole loro: `basex@tcg + 420, basey@tcg + 230, 200`
    ma anche `winposy(90)`.
    """
    fuori, corrente, profondita = [], "", 0
    for c in espressione:
        if c in "([":
            profondita += 1
        elif c in ")]":
            profondita -= 1
        if c == "," and profondita == 0:
            fuori.append(corrente)
            corrente = ""
        else:
            corrente += c
    fuori.append(corrente)
    return fuori


def larghezza_inglese(campo: str) -> int | None:
    """Il campo della larghezza valutato nella build inglese, cioe' `en = 1`.

    ⚠️ La lingua allarga il riquadro **in tutt'e due i versi**: `450 - 50 * en`
    lo stringe a 400, `180 + ( en * 50 )` lo allarga a 230. Chi leggesse il
    primo numero e basta griderebbe al difetto sul menu del voto, che invece
    ha margine.

    `None` quando il campo non e' un numero: sono i `val =` che non dichiarano
    un riquadro di menu — `winposy(90), 12, 1, 0` e' un campo d'immissione, e
    il 12 sono cifre, non pixel.
    """
    testo = re.sub(r"\ben\b", "1", campo).strip()
    if not _SOLO_ARITMETICA.match(testo):
        return None
    try:
        return int(eval(testo, {"__builtins__": {}}, {}))
    except Exception:
        return None


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


def larghezze(cartella: Path | None = None, nomi: set[str] | None = None) -> dict[str, int]:
    """nome del menu -> larghezza in pixel del riquadro, nella build inglese.

    ⚠️ **I nomi si prendono da `menu_per_riga`, non da una convenzione.** La
    prima versione cercava le chiamate con `txt(set|select)\\w+`, e
    `txtplusbody` — il menu della parte del corpo da farsi crescere — non si
    chiama cosi': restava l'unico non misurato, e sembrava codice morto. Terzo
    esemplare di [[una-guardia-vale-solo-dove-guarda]], e stavolta la guardia
    ero io.

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
    if nomi is None:
        nomi = set(menu_per_riga(cartella / FILE).values())
    fuori: dict[str, int] = {}
    for percorso in sorted(cartella.glob("*.hsp")):
        righe = _righe(percorso)
        for i, riga in enumerate(righe):
            m = _CHIAMATA.match(riga)
            if not m or m.group(1) not in nomi:
                continue
            for j in range(i + 1, len(righe)):
                if righe[j].startswith(("#deffunc", "*")) or righe[j].lstrip().startswith("*"):
                    break
                v = _VAL.match(righe[j])
                if v:
                    pezzi = campi(v.group(1))
                    px = larghezza_inglese(pezzi[2]) if len(pezzi) >= 3 else None
                    if px is None:
                        continue
                    nome = m.group(1)
                    fuori[nome] = min(fuori.get(nome, px), px)
                    break
    return fuori


def _siti(cartella: Path):
    """(file, riga del `gosub *prompt_key`, pixel|None, righe delle voci).

    Un menu e' una corsa di `promptAdd` chiusa da `gosub *prompt_key`, e la
    larghezza sta nell'ultimo `val =` prima della chiusura. Si cammina
    all'indietro **dalla chiusura**, non in avanti dal `val =`: ci sono `val =`
    a cinque campi che non dichiarano nessun riquadro (`winposy(90), 12, 1, 0`
    e' un campo d'immissione), e partire da loro inventa menu che non esistono.

    ⚠️ I `#define` di `init.hsp:19`-`:33` portano dentro un `gosub *prompt_key`
    che non e' un sito: e' il corpo delle macro `promptYesNo`, `promptOk`,
    `promptTagTeam`, e il `%1=200` non e' una larghezza ma il valore di default
    di un parametro. Si saltano, continuazioni comprese.
    """
    for percorso in sorted(cartella.glob("*.hsp")):
        righe = _righe(percorso)
        confine = 0
        dentro_define = False
        for i, riga in enumerate(righe):
            if riga.startswith("#define"):
                dentro_define = True
            if dentro_define:
                if not riga.rstrip().endswith("\\"):
                    dentro_define = False
                confine = i + 1
                continue
            if not _PROMPT_KEY.search(riga):
                continue
            inizio = max(confine, i - FINESTRA)
            px = None
            for j in range(i - 1, inizio - 1, -1):
                m = _VAL.match(righe[j])
                if m:
                    pezzi = campi(m.group(1))
                    px = larghezza_inglese(pezzi[2]) if len(pezzi) >= 3 else None
                    break
            voci = [j + 1 for j in range(inizio, i)
                    if _ADD.search(righe[j]) and not righe[j].lstrip().startswith(";")]
            yield percorso.name, i + 1, px, voci
            confine = i + 1


def _diretti_con_sito(cartella: Path) -> dict[tuple[str, int], tuple[int, str]]:
    fuori: dict[tuple[str, int], tuple[int, str]] = {}
    for nome, riga_pk, px, voci in _siti(cartella):
        if px is None:
            continue
        for riga in voci:
            fuori[(nome, riga)] = (px, "%s:%d" % (nome, riga_pk))
    return fuori


def menu_diretti(cartella: Path | None = None) -> dict[tuple[str, int], int]:
    """(file, riga di una voce) -> larghezza in pixel del riquadro che la taglia.

    E' la seconda strada della rete, quella che non passa da `text.hsp`: 95
    siti contro 20, e 151 voci con `lang()` dentro. Le voci dei siti di cui non
    si e' trovata la larghezza **non entrano**: meglio non misurate che misurate
    col numero di qualcun altro — un sito che resta fuori lo dice il referto,
    un sito misurato male tace.
    """
    cartella = cartella or percorsi.SORGENTE_HSP
    return {chiave: px for chiave, (px, _) in _diretti_con_sito(cartella).items()}


def siti_senza_larghezza(cartella: Path | None = None) -> list[tuple[str, int]]:
    """I `gosub *prompt_key` di cui non si e' trovato il riquadro.

    Oggi e' vuoto, ed e' bene saperlo dal test: e' il fratello di
    `menu_senza_larghezza` per la seconda strada.
    """
    cartella = cartella or percorsi.SORGENTE_HSP
    return [(nome, riga) for nome, riga, px, _ in _siti(cartella) if px is None]


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
    """(sito, pixel, tetto, riga, lunghezza, testo) per ogni voce che sfora.

    Il **sito** e' il nome del `#deffunc` per i menu di `text.hsp` e
    `file.hsp:riga` del `gosub *prompt_key` per gli altri: sono due strade
    diverse per arrivare allo stesso riquadro, e vale la pena vedere da quale
    arriva una voce.

    ⚠️ `dizionario` e' la **cartella**, non piu' il solo `text.hsp.jsonl`: la
    rete leggeva un file solo, e una voce resa in un menu di `command.hsp` non
    aveva nessuno che la guardasse.
    """
    dizionario = dizionario or percorsi.DIZIONARIO
    sorgente = sorgente or percorsi.SORGENTE_HSP
    per_riga = menu_per_riga(sorgente / FILE)
    px_per_menu = larghezze(sorgente)
    diretti = _diretti_con_sito(sorgente)

    fuori = []
    for percorso in sorted(dizionario.glob("*.jsonl")):
        nome_file = percorso.name[: -len(".jsonl")]
        for linea in percorso.read_text(encoding="utf-8").splitlines():
            voce = json.loads(linea)
            riga = voce["riga"]
            if nome_file == FILE and riga in per_riga:
                sito = per_riga[riga]
                px = px_per_menu.get(sito)
            else:
                px, sito = diretti.get((nome_file, riga), (None, None))
            if px is None:
                continue
            testo = reso(voce.get("it") or "")
            tetto = budget(px)
            if len(testo) > tetto:
                fuori.append((sito, px, tetto, riga, len(testo), testo))
    return sorted(fuori)


def menu_senza_larghezza(sorgente: Path | None = None) -> set[str]:
    """I menu di cui non si e' trovato il chiamante: non sono misurati.

    Oggi e' vuoto, ed e' bene saperlo dal test: un menu che smette di essere
    trovato smette anche di essere controllato, in silenzio.
    """
    sorgente = sorgente or percorsi.SORGENTE_HSP
    nomi = set(menu_per_riga(sorgente / FILE).values())
    return nomi - set(larghezze(sorgente, nomi))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--tutti", action="store_true",
                   help="elenca ogni menu con il suo tetto, non solo chi sfora")
    args = p.parse_args(argv)

    px_per_menu = larghezze()
    diretti = _diretti_con_sito(percorsi.SORGENTE_HSP)
    if args.tutti:
        per_riga = menu_per_riga()
        quante: dict[str, int] = {}
        for nome in per_riga.values():
            quante[nome] = quante.get(nome, 0) + 1
        for _, sito in diretti.values():
            quante[sito] = quante.get(sito, 0) + 1
        larghezza_di = dict(px_per_menu)
        for px, sito in diretti.values():
            larghezza_di[sito] = px
        print("%-24s %6s %5s %6s" % ("menu", "pixel", "tetto", "voci"))
        for sito in sorted(larghezza_di):
            print("%-24s %6d %5d %6d"
                  % (sito, larghezza_di[sito], budget(larghezza_di[sito]),
                     quante.get(sito, 0)))

    sfori = fuori_misura()
    if sfori:
        print()
        ultimo = None
        for sito, px, tetto, riga, n, testo in sfori:
            if sito != ultimo:
                print("\n%s  %dpx, tetto %d caratteri" % (sito, px, tetto))
                ultimo = sito
            print("   %6d  %3d  %s" % (riga, n, testo))

    # ⚠️ Il denominatore sta nel referto apposta: «0 fuori misura» dice che
    # nessuna resa sfora, non che tutte le voci siano state controllate. Le
    # voci senza una resa non sono misurabili -- e sono la maggioranza.
    con_voci = {sito for _, sito in diretti.values()}
    print("\nvoci fuori misura: %d" % len(sfori))
    print("menu misurati: %d di text.hsp piu' %d siti di *prompt_key con voci proprie"
          % (len(px_per_menu), len(con_voci)))
    print("voci nel riquadro: %d di text.hsp piu' %d altrove"
          % (len(menu_per_riga()), len(diretti)))

    senza = menu_senza_larghezza()
    if senza:
        print("menu non misurati (chiamante non trovato): %s" % ", ".join(sorted(senza)))
    orfani = siti_senza_larghezza()
    if orfani:
        print("siti *prompt_key senza riquadro: %s"
              % ", ".join("%s:%d" % o for o in orfani))
    return 1 if sfori else 0


if __name__ == "__main__":
    sys.exit(main())
