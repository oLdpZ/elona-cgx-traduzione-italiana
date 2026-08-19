# -*- coding: utf-8 -*-
"""Quanto puo' essere lunga un'intestazione di colonna prima di toccare la dopo.

RETE 20. `display_topic` (`module.hsp:4364`) disegna un'icona da 24 px, poi il
testo **26 px** piu' in la' con un `mes` che non taglia e non va a capo:

    #deffunc display_topic str testo, int x, int y, int
        font lang(cfg_font1, cfg_font2), 12 + sizefix - en * 2, 1
        pos x, y + 7      : gcopy 3, 120, 360, 24, 16      <- l'icona
        pos x + 26, y + 8 : mes testo                      <- il testo
        line x + 22, y + 21, x + strlen(testo) * 7 + 36, y + 21

Due intestazioni sulla stessa riga non si toccano se

    x + 26 + strlen * 7  <=  x della intestazione successiva

cioe' il tetto della colonna e' `(x_dopo - x - 26) / 7` caratteri.

## Il corpo e' 11, non 10

`sizefix` viene da `config.txt` (`fontSfix1. "1"`, `config.hsp:180`) e vale **1**
in inglese; `config.hsp:436` lo azzera solo nel ramo giapponese. Il corpo qui e'
`12 + 1 - 2 = 11`.
⚠️ `toppa-command-combat-rolls.py` (47a) scrive «`sizefix` assente da
`config.txt` e quindi 0»: `config.txt` ce l'ha. La toppa regge lo stesso (sposta
un'etichetta a sinistra, e col passo giusto ne servirebbe di piu', non di meno),
ma la ragione scritta no.

## ⚠️⚠️⚠️ E il passo a corpo 11 e' 7, MISURATO — non si deduce

La prima stesura di questa rete usava **6**, da `int(0,6 * 11)`, e si dichiarava
provata perche' con 6 l'inglese di monte non sforava da nessuna parte. **Era un
ragionamento circolare**: il passo era stato scelto proprio perche' faceva
tornare la prova. La regola della 63a — *il tetto vero lo tocca l'inglese* — e'
un **controllo**, non un modo di ricavare una costante: se il candidato si sceglie
guardando l'esito, il controllo non puo' piu' fallire.

Il numero vero e' a schermo. La 65a ha misurato la scheda delle modalita'
(`chara.hsp:4193`, stesso `Courier New` a corpo 11): la riga piu' lunga fa **72
caratteri in 503 px**, e l'ultimo carattere occupa una **cella da 7 px** di cui
due soli di inchiostro. Sette, non sei. Il rapporto sei decimi di `riquadri.py`
si **arrotonda**, non si tronca: `round(0,6 * 11) = 7`, `round(0,6 * 12) = 7`
(`module.hsp:70`, e misurato tre volte nella 64a), `round(0,6 * 14) = 8`
(`screen.hsp:2255`). Troncando, l'11 dava 6 e il 12 dava 7: due corpi vicini con
due passi diversi erano gia' il campanello.

## ⚠️ E con il passo giusto l'inglese di monte SFORA in due posti

Non e' un difetto della rete: e' un difetto del gioco, piccolo e mai notato.
L'icona della colonna dopo viene disegnata **dopo** il testo di quella prima, e
gli copre la coda.

    command.hsp:4199   Message(Impress)             16 su 15   elenco avventurieri
    command.hsp:10410  Attributes(Org) - Potential  27 su 26   scheda personaggio

Il secondo si vede **solo** nelle partite in modalita' speciale, perche' la
casella a `wx + 240` che gli sta accanto negli altri casi e' vuota. Sono le due
colonne piu' strette del gioco, ed e' il motivo per cui la resa italiana di
`:10410` sta a 27 e non a 29: **non piu' lunga di monte**, che e' il metro del
progetto dove monte gia' sfora.

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
PASSO = 7        # misurato a schermo nella 65a: round(0,6 * 11). Vedi il docstring.
ICONA = 26       # module.hsp:4370, `pos x + 26` -- il testo parte dopo l'icona
GAP_MINIMO = 40  # sotto questo, le due chiamate sono rami alternativi, non colonne
VICINE = 80      # due chiamate a piu' di 80 righe di distanza sono due finestre

# I due siti dove l'inglese di monte sfora gia' di suo: il perimetro del progetto
# li' non e' il tetto, e' «non piu' lungo di monte».
DI_MONTE = {("command.hsp", 4199), ("command.hsp", 10410)}

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


def indice(albero):
    return {(c[0], c[1]): c for c in coppie(chiamate(albero)[0])}


def referto(albero, etichetta):
    trovate, saltate = chiamate(albero)
    misurabili = coppie(trovate)
    sfora = [c for c in misurabili if len(c[5]) > tetto(c[3], c[4])]
    print(f"--- {etichetta}: {len(trovate)} display_topic con x e testo leggibili "
          f"({saltate} no), {len(misurabili)} in coppia, {len(sfora)} fuori misura")
    for nome, n, y, x, x2, t in sorted(sfora, key=lambda c: (c[0], c[1])):
        scusa = "  (sfora anche l'inglese)" if (nome, n) in DI_MONTE else ""
        print(f"   {nome}:{n}  wy+{y}  x {x} -> {x2}, tetto {tetto(x, x2)}, "
              f"lunghezza {len(t)}   {t!r}{scusa}")
    return sfora


def perimetro():
    """Le colonne senza scuse di monte: l'inglese ci sta e noi no, o siamo piu' lunghi."""
    monte, nostro = indice(SORGENTE), indice(BUILD)
    fuori = []
    for k, c in nostro.items():
        nome, n, y, x, x2, it = c
        en = monte.get(k, (None,) * 6)[5] or ""
        if len(it) <= tetto(x, x2):
            continue
        if len(en) <= tetto(x, x2) or len(it) > len(en):
            fuori.append((nome, n, x, x2, en, it))
    print(f"\n=== il perimetro: {len(fuori)} colonne")
    for nome, n, x, x2, en, it in fuori:
        print(f"   {nome}:{n}  tetto {tetto(x, x2)}   en {len(en):2d} {en!r}")
        print(f"{'':>{len(nome) + len(str(n)) + 4}}              it {len(it):2d} {it!r}")
    return fuori


def piu_strette(albero, quante=5):
    """Le colonne con meno margine, cioe' dove una resa lunga fa danno per prima."""
    trovate, _ = chiamate(albero)
    righe = [(tetto(x, x2) - len(t), tetto(x, x2), nome, n, x, x2, t)
             for nome, n, y, x, x2, t in coppie(trovate)]
    righe.sort()
    print(f"\n--- le {quante} colonne con meno margine")
    for margine, tt, nome, n, x, x2, t in righe[:quante]:
        print(f"   margine {margine:3d}   tetto {tt:3d}   {nome}:{n}  "
              f"x {x}->{x2}   {len(t):2d}  {t!r}")


def prova():
    """⭐ Il banco: l'inglese di monte sfora nei DUE siti noti e in nessun altro.

    Non e' «zero fuori misura»: con il passo misurato l'inglese sfora davvero in
    due colonne, e la rete deve dirlo. Se ne comparisse una terza, o ne sparisse
    una, e' cambiato il sorgente o e' sbagliata la rete.
    """
    sfora = referto(SORGENTE, "inglese di monte")
    trovato = {(c[0], c[1]) for c in sfora}
    ok = trovato == DI_MONTE
    print(f"   prova: attesi {sorted(DI_MONTE)}, trovati {sorted(trovato)} -> "
          f"{'ok' if ok else 'IL METRO NON REGGE'}")
    return ok


if __name__ == "__main__":
    buono = prova()
    piu_strette(SORGENTE)
    print()
    referto(BUILD, "build italiana")
    perimetro()
    sys.exit(0 if buono else 1)
