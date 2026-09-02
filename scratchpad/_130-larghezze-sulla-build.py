# -*- coding: utf-8 -*-
"""Il tetto dei menu misurato sulla BUILD, cioe' sull'esito e non sull'intenzione.

## Perche' non basta `strumenti/larghezze.py`

`larghezze.fuori_misura` scorre il **dizionario** e cerca `(file, riga)` nelle
mappe dei menu ricavate dal **sorgente pinnato**. Una toppa non ha una voce di
dizionario — non ha nemmeno un numero di riga: `toppe.jsonl` porta `file`,
`cerca`, `sostituisci`, `motivo`, e basta. Quindi l'italiano che entra nel gioco
per la strada delle toppe **non entra mai in quel ciclo**, in nessun caso.

⚠️⚠️ **E non si rimedia dando una riga alle toppe.** Il primo tentativo di
misurare questo fronte (`_130-quali-reti-vedono-le-toppe.py`) cercava le toppe
che cadono dentro un riquadro noto e rispondeva **0**: non perche' non ce ne
siano, ma perche' il campo `riga` non esiste e il ciclo saltava tutte e 1.172 le
voci. Lo zero era la spia rotta, non il dato — la lezione della 109a, arrivata
qui il giorno dopo che l'avevo scritta.

## Che cosa fa questo referto

Gira la stessa macchina di `strumenti/larghezze.py` — `menu_per_riga`,
`larghezze`, `_siti`, `budget`, `reso` — sopra `percorsi.BUILD_HSP`, e prende
l'italiano **dalla riga della build**, non dal dizionario. Nella build il
dizionario e' gia' applicato e le toppe pure: un metro solo, per tutt'e due le
strade, e nessun numero di riga da far combaciare fra due alberi che non hanno
lo stesso numero di righe (`map.hsp` nella build ne ha cinque piu' del sorgente).

Si misura **l'esito**: quel che il giocatore riceve.

## Le due differenze rispetto alla rete del sorgente, dichiarate

1. **`s(cnt) = ` senza `lang()`.** `menu_per_riga` pretende `s(cnt) = lang(`,
   perche' nel sorgente una voce senza `lang()` non ha resa da controllare. Nella
   build una toppa puo' aver **tolto** la `lang()` e lasciato il letterale nudo,
   ed e' esattamente la voce che serve guardare. Qui la forma nuda entra, e il
   referto stampa **quante voci aggiunge**: se un giorno quel numero salta, si
   vede.
2. **L'italiano si legge dall'espressione.** `lang(J, I)` si riduce a `I`, il
   letterale nudo vale se stesso, e il resto passa per `larghezze.reso`, che
   degrada gli accenti e da' `LARGHEZZA_NUMERO` cifre a ogni valore interpolato.

## Il numero che conta non e' «0 fuori misura»

Accanto allo zero sta **quante voci ha davvero giudicato** e **quante di quelle
vengono da una toppa**. Uno zero senza il secondo numero non distingue «nessuna
voce sfora» da «non ne ho misurata nessuna».

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-larghezze-sulla-build.py
    ... --elenco     tutte le voci misurate, menu per menu, col margine
"""
import io
import json
import re
import sys
from pathlib import Path

from strumenti import larghezze, percorsi

# `s(cnt) = <qualunque cosa>`, non solo `lang(`: vedi la differenza n. 1
_VOCE_LARGA = re.compile(r"^\s*s\(\s*cnt\s*\)\s*=\s*(.+?)\s*$")
_ADD_TESTA = re.compile(r"^\s*(?:promptAdd\s+|promptl\s*\(\s*0\s*,[^)]*\)\s*=\s*)(.+?)\s*$")
_DEFFUNC = re.compile(r"^#deffunc\s+(\w+)")


def _lang_a_italiano(espressione: str) -> str:
    """`lang("日本語", "italiano")` -> `"italiano"`, ovunque compaia.

    Si spezza a mano invece che con un'espressione regolare perche' il primo
    argomento puo' portarsi dentro virgole e virgolette scappate, e una regex
    che le ignori taglia la frase nel punto sbagliato — silenziosamente.
    """
    fuori = ""
    i = 0
    while i < len(espressione):
        if espressione.startswith("lang(", i) and (
                i == 0 or not (espressione[i - 1].isalnum() or espressione[i - 1] == "_")):
            j = i + len("lang(")
            profondita = 0
            dentro = False
            campi = [""]
            while j < len(espressione):
                c = espressione[j]
                if dentro:
                    campi[-1] += c
                    if c == "\\":
                        if j + 1 < len(espressione):
                            campi[-1] += espressione[j + 1]
                            j += 1
                    elif c == '"':
                        dentro = False
                elif c == '"':
                    dentro = True
                    campi[-1] += c
                elif c == "(":
                    profondita += 1
                    campi[-1] += c
                elif c == ")":
                    if profondita == 0:
                        break
                    profondita -= 1
                    campi[-1] += c
                elif c == "," and profondita == 0:
                    campi.append("")
                else:
                    campi[-1] += c
                j += 1
            if len(campi) >= 2:
                fuori += campi[1].strip()
                i = j + 1
                continue
        fuori += espressione[i]
        i += 1
    return fuori


def _termini(espressione: str) -> list:
    """Spezza un'espressione HSP sui `+` di primo livello, fuori dalle stringhe."""
    fuori, corrente, profondita, dentro = [], "", 0, False
    i = 0
    while i < len(espressione):
        c = espressione[i]
        if dentro:
            corrente += c
            if c == "\\" and i + 1 < len(espressione):
                corrente += espressione[i + 1]
                i += 1
            elif c == '"':
                dentro = False
        elif c == '"':
            dentro = True
            corrente += c
        elif c in "([":
            profondita += 1
            corrente += c
        elif c in ")]":
            profondita -= 1
            corrente += c
        elif c == "+" and profondita == 0:
            fuori.append(corrente)
            corrente = ""
        else:
            corrente += c
        i += 1
    fuori.append(corrente)
    return [t.strip() for t in fuori]


def _a_letterale(espressione: str) -> str:
    """L'espressione ridotta al solo testo, per darla a `larghezze.reso`.

    ⚠️⚠️ **Serve perche' `reso` da solo sbaglia quando il valore dinamico sta in
    TESTA.** La sua `_INTERPOLAZIONE` cerca `" + qualcosa + "`, cioe' un valore
    **fra due letterali**: in `mapname(i) + " " + cnvrank(...) + " liv."` il
    primo termine non e' preceduto da nessuna virgoletta, resta nel testo tale e
    quale, e `command.hsp:17441` risultava lungo **92 caratteri** — il codice,
    non la frase. Il difetto non si era mai visto perche' nella rete del
    sorgente il testo arriva dal campo `it` del dizionario, che e' sempre un
    letterale: e' un limite che **solo questa strada poteva incontrare**.

    Qui ogni termine di primo livello vale:
      - il suo contenuto, se e' un letterale;
      - i letterali che si porta dentro, se e' una chiamata che ne contiene
        (`cnven("ermafrodito")` disegna «Ermafrodito», non tre cifre);
      - `LARGHEZZA_NUMERO` cifre altrimenti, come fa `reso`.

    ⓘ La regola dei valori interpolati resta **quella di `reso`**, non una
    seconda: qui si normalizza l'espressione, non si rimisura.
    """
    pezzi = []
    for termine in _termini(espressione):
        if termine.startswith('"') and termine.endswith('"') and len(termine) >= 2:
            pezzi.append(termine[1:-1])
            continue
        dentro = larghezze._INTERPOLAZIONE.sub("", termine)
        letterali = re.findall(r'"((?:[^"\\]|\\.)*)"', termine)
        pezzi.append("".join(letterali) if letterali
                     else "9" * larghezze.LARGHEZZA_NUMERO)
    return "".join(pezzi)


def _italiano(espressione: str) -> str:
    """Il testo che il riquadro disegna, dall'espressione HSP della voce."""
    pezzi = larghezze.campi(espressione)
    # `promptAdd s, key_select(cnt)`: la voce e' il primo campo, il secondo e'
    # il tasto. Per `s(cnt) = ...` il campo e' uno solo e il taglio non fa nulla.
    return larghezze.reso(_a_letterale(_lang_a_italiano(pezzi[0]).strip()))


def voci_della_build(cartella: Path | None = None):
    """(file, riga, sito, pixel, espressione) per ogni voce di menu della build.

    Le due strade di `strumenti/larghezze.py`, girate sull'albero della build.
    """
    cartella = cartella or percorsi.BUILD_HSP

    # strada 1: i `#deffunc txt*` di text.hsp, col riquadro dichiarato dal chiamante
    percorso_text = cartella / larghezze.FILE
    per_riga: dict[int, str] = {}
    strette: dict[int, str] = {}
    corrente = None
    for numero, riga in enumerate(percorso_text.read_bytes().decode("cp932", "replace").split("\n"), 1):
        m = _DEFFUNC.match(riga)
        if m:
            corrente = m.group(1)
            continue
        if not corrente:
            continue
        m = _VOCE_LARGA.match(riga)
        if m:
            per_riga[numero] = corrente
            if m.group(1).lstrip().startswith("lang("):
                strette[numero] = corrente
    px_per_menu = larghezze.larghezze(cartella, set(per_riga.values()))

    righe_text = percorso_text.read_bytes().decode("cp932", "replace").split("\n")
    for numero, sito in sorted(per_riga.items()):
        px = px_per_menu.get(sito)
        if px is None:
            continue
        m = _VOCE_LARGA.match(righe_text[numero - 1])
        yield larghezze.FILE, numero, sito, px, m.group(1), numero in strette

    # strada 2: le corse di `promptAdd` chiuse da `gosub *prompt_key`
    for nome, riga_pk, px, voci in larghezze._siti(cartella):
        if px is None:
            continue
        righe = (cartella / nome).read_bytes().decode("cp932", "replace").split("\n")
        for riga in voci:
            m = _ADD_TESTA.match(righe[riga - 1])
            if not m:
                continue
            yield nome, riga, "%s:%d" % (nome, riga_pk), px, m.group(1), True


def testo_delle_toppe() -> dict:
    """file -> insieme delle righe che una toppa scrive, ripulite dagli spazi.

    Serve solo per **attribuire** una voce alla strada da cui e' arrivata. Non
    e' un giudizio: una voce puo' sforare comunque sia entrata.
    """
    fuori: dict = {}
    percorso = percorsi.PROGETTO / "toppe.jsonl"
    for linea in io.open(percorso, encoding="utf-8"):
        if not linea.strip():
            continue
        toppa = json.loads(linea)
        valore = toppa["sostituisci"]
        righe = valore if isinstance(valore, list) else [valore]
        fuori.setdefault(toppa["file"], set()).update(r.strip() for r in righe if r.strip())
    return fuori


def main(argv: list[str] | None = None) -> int:
    elenco = "--elenco" in (argv if argv is not None else sys.argv[1:])
    da_toppa = testo_delle_toppe()

    misurate = 0
    nude = 0
    di_toppa = 0
    sfori = []
    margini = []
    for nome, riga, sito, px, espressione, era_lang in voci_della_build():
        testo = _italiano(espressione)
        if not testo:
            continue
        misurate += 1
        if not era_lang:
            nude += 1
        toppa = espressione.strip() in da_toppa.get(nome, ()) or \
            any(espressione.strip() in r for r in da_toppa.get(nome, ()))
        if toppa:
            di_toppa += 1
        tetto = larghezze.budget(px)
        margine = tetto - len(testo)
        margini.append((margine, nome, riga, sito, px, tetto, len(testo), testo, toppa))
        if margine < 0:
            sfori.append((sito, nome, riga, px, tetto, len(testo), testo, toppa))

    if elenco:
        for margine, nome, riga, sito, px, tetto, lung, testo, toppa in sorted(margini):
            print("%+4d  %-22s %-26s %4dpx tetto %2d  %s%s"
                  % (margine, "%s:%d" % (nome, riga), sito, px, tetto,
                     testo[:60], "   <- toppa" if toppa else ""))
        print()

    for sito, nome, riga, px, tetto, lung, testo, toppa in sorted(sfori):
        print("FUORI MISURA  %-22s %-26s %4dpx tetto %2d, ha %d%s"
              % ("%s:%d" % (nome, riga), sito, px, tetto, lung,
                 "   <- TOPPA" if toppa else ""))
        print("              %s" % testo)

    stretti = sorted(margini)[:5]
    print()
    print("voci di menu misurate nella build : %d" % misurate)
    print("  di cui senza `lang()` (nude)    : %d   ⓘ le vede solo questo referto"
          % nude)
    print("  di cui scritte da una toppa     : %d   ⓘ il fronte che nessuna rete leggeva"
          % di_toppa)
    print("voci fuori misura                 : %d" % len(sfori))
    print()
    print("i cinque margini piu' stretti (un cancello booleano non dice il margine):")
    for margine, nome, riga, sito, px, tetto, lung, testo, toppa in stretti:
        print("  %+4d  %-22s tetto %2d, ha %2d  %s%s"
              % (margine, "%s:%d" % (nome, riga), tetto, lung, testo[:48],
                 "   <- toppa" if toppa else ""))
    return 1 if sfori else 0


if __name__ == "__main__":
    sys.exit(main())
