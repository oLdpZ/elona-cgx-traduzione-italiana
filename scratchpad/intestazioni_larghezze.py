# -*- coding: utf-8 -*-
"""Quanto puo' essere lunga un'intestazione di colonna prima di toccare la dopo.

RETE 20. `display_topic` (`module.hsp:4364`) disegna un'icona da 24 px, poi il
testo **26 px** piu' in la', poi una riga di sottolineatura:

    #deffunc display_topic str testo, int x, int y, int
        font lang(cfg_font1, cfg_font2), 12 + sizefix - en * 2, 1
        pos x, y + 7      : gcopy 3, 120, 360, 24, 16      <- l'icona
        pos x + 26, y + 8 : mes testo                      <- il testo
        line x + 22, y + 21, x + strlen(testo) * 7 + 36, y + 21

Il `mes` non taglia e non va a capo. Due intestazioni sulla stessa riga non si
toccano se

    x + 26 + strlen * PASSO  <=  x della intestazione successiva

cioe' il tetto della colonna e' `(x_dopo - x - 26) / PASSO` caratteri.

## ⚠️⚠️ Il passo e' 6, e i due modi di sbagliarlo

**Non e' il 7 della riga `line`.** Quel `strlen * 7 + 36` e' il modello che il
gioco ha della **sottolineatura**, che per disegno sporge oltre il testo: preso
per larghezza del testo fa un tetto troppo stretto, e infatti l'inglese di monte
lo sfonda in tre posti.

**E non e' il corpo 10.** `sizefix` viene da `config.txt` (`fontSfix1. "1"`,
`config.hsp:180`) e vale **1** in inglese — `config.hsp:436` lo azzera solo nel
ramo giapponese. Quindi il corpo qui e' `12 + 1 - 2 = 11`, non 10.
⚠️ `toppa-command-combat-rolls.py` (47a) scrive «`sizefix` assente da
`config.txt` e quindi 0»: e' sbagliato: `config.txt` ce l'ha. Arriva allo stesso
6 px per un'altra strada, quindi la toppa regge, ma la ragione scritta no.

Il passo giusto lo da' la regola di `riquadri.py`: **`Courier New` e'
monospaziato e avanza sei decimi del corpo**, troncati. Lo confermano i due passi
che il gioco stesso si scrive nel sorgente, agli altri due corpi che usa:

    corpo 14  ->  int(0,6 * 14) = 8    screen.hsp:2255, `strlen(s) * 8 + 45`
    corpo 12  ->  int(0,6 * 12) = 7    module.hsp:70,   `strlen(...) * 7 + 32`
    corpo 11  ->  int(0,6 * 11) = 6    <- display_topic

e il 7 del corpo 12 e' anche **misurato a schermo** tre volte nella 64a
(`menu_dialogo.py`).

## ⭐ Provato sull'inglese di monte, come vuole la 61a

Con il passo 6 l'inglese **sta dentro dappertutto**: 0 coppie fuori misura su 34.
E ci sta *per un pelo* dove ci si aspetta che lo faccia — la coppia piu' stretta
del gioco e' `command.hsp:4199`, «Message(Impress)», 16 caratteri in una colonna
da 17: e' la prova della 63a, upstream scrive dentro la finestra che ha disegnato
e il suo massimo tocca il tetto.

Col passo 7 le coppie fuori sarebbero **tre**, e sono le tre piu' strette del
gioco: il segno che il metro misurava una cosa vicina invece della cosa.

## ⚠️ Che cosa NON misura

- **L'ultima intestazione di ogni riga.** Il suo limite e' il bordo della
  finestra, che sta in un `display_window` altrove, spesso in un'altra procedura.
- **Le chiamate con la `x` per espressione** (`wx + ww / 2`) o con il **testo in
  una variabile**: quelle le trova `intestazioni.py`, che e' un'altra rete.
- **Le coppie a meno di 40 px**, che non sono colonne ma **rami alternativi** di
  un `if`: `command.hsp:7625` ne e' l'unico caso, «Level(Piety Cost)» a `wx+328`
  e «Level» a `wx+348`, in `if` e `else`.

⚠️ E si misura sulla forma **degradata**: `applica` scrive «Modalita'» dove il
dizionario dice «Modalità», e l'apostrofo e' un carattere in piu'.
"""
import collections
import io
import os
import re
import sys

SORGENTE = r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx"
BUILD = r"C:\Games\Elona\_traduzione\build\2.05-custom-gx"

CORPO = 11       # module.hsp:4365, `12 + sizefix - en * 2` con sizefix = 1
PASSO = int(0.6 * CORPO)
ICONA = 26       # module.hsp:4370, `pos x + 26` -- il testo parte dopo l'icona
GAP_MINIMO = 40  # sotto questo, le due chiamate sono rami alternativi, non colonne
VICINE = 80      # due chiamate a piu' di 80 righe di distanza sono due finestre

CHIAMA = re.compile(r"^\s*display_topic\s+(.+?),\s*wx \+ (\d+),\s*wy \+ (\d+)")
LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')
NUDO = re.compile(r'^"((?:[^"\\]|\\.)*)"$')


def testo_di(argomento):
    """L'inglese dell'intestazione, o None se non e' un letterale."""
    m = LANG.search(argomento)
    if m:
        return m.group(2)
    m = NUDO.match(argomento.strip())
    return m.group(1) if m else None


def chiamate(albero):
    """[(file, riga, y, x, testo)] per ogni display_topic misurabile."""
    trovate, saltate = [], 0
    for nome in sorted(os.listdir(albero)):
        if not nome.endswith(".hsp"):
            continue
        testo = io.open(os.path.join(albero, nome), encoding="cp932",
                        errors="replace").read().split("\n")
        for n, riga in enumerate(testo, 1):
            m = CHIAMA.match(riga)
            if not m:
                if re.match(r"^\s*display_topic\s", riga):
                    saltate += 1
                continue
            t = testo_di(m.group(1))
            if t is None:
                saltate += 1
                continue
            trovate.append((nome, n, int(m.group(3)), int(m.group(2)), t))
    return trovate, saltate


def coppie(trovate):
    """Le coppie (sinistra, destra) sulla stessa riga della stessa finestra."""
    per_riga = collections.defaultdict(list)
    for nome, n, y, x, t in trovate:
        per_riga[(nome, y)].append((n, x, t))
    finestre = []
    for (nome, y), voci in per_riga.items():
        voci.sort()
        # una finestra per volta: chiamate lontane nel sorgente sono finestre diverse
        gruppo = []
        for v in voci:
            if gruppo and v[0] - gruppo[-1][0] > VICINE:
                finestre.append((nome, y, gruppo))
                gruppo = []
            gruppo.append(v)
        if gruppo:
            finestre.append((nome, y, gruppo))
    accoppiate = []
    for nome, y, gruppo in finestre:
        per_x = sorted(gruppo, key=lambda v: v[1])
        for (n, x, t), (_, x2, _t2) in zip(per_x, per_x[1:]):
            if x2 - x >= GAP_MINIMO:
                accoppiate.append((nome, n, y, x, x2, t))
    return accoppiate


def tetto(x, x2):
    return (x2 - x - ICONA) // PASSO


def referto(albero, etichetta):
    trovate, saltate = chiamate(albero)
    misurabili = coppie(trovate)
    sfora = [c for c in misurabili if len(c[5]) > tetto(c[3], c[4])]
    print(f"--- {etichetta}: {len(trovate)} display_topic con x e testo leggibili "
          f"({saltate} no), {len(misurabili)} in coppia, {len(sfora)} fuori misura")
    for nome, n, y, x, x2, t in sorted(sfora, key=lambda c: (c[0], c[1])):
        print(f"   {nome}:{n}  wy+{y}  x {x} -> {x2}, tetto {tetto(x, x2)}, "
              f"lunghezza {len(t)}   {t!r}")
    return sfora


def piu_strette(albero, quante=5):
    """Le colonne con meno margine, cioe' dove una resa lunga fa danno per prima."""
    trovate, _ = chiamate(albero)
    righe = [(tetto(x, x2) - len(t), tetto(x, x2), nome, n, x, x2, t)
             for nome, n, y, x, x2, t in coppie(albero and trovate)]
    righe.sort()
    print(f"\n--- le {quante} colonne con meno margine")
    for margine, tt, nome, n, x, x2, t in righe[:quante]:
        print(f"   margine {margine:3d}   tetto {tt:3d}   {nome}:{n}  "
              f"x {x}->{x2}   {len(t):2d}  {t!r}")


def prova():
    """⭐ Il banco: con il passo giusto l'inglese di monte non sfora da nessuna parte."""
    sfora = referto(SORGENTE, "inglese di monte")
    ok = not sfora
    print(f"   prova: atteso 0 fuori misura, trovati {len(sfora)} -> "
          f"{'ok' if ok else 'IL METRO NON REGGE'}")
    return ok


if __name__ == "__main__":
    buono = prova()
    piu_strette(SORGENTE)
    print()
    referto(BUILD, "build italiana")
    sys.exit(0 if buono else 1)
