# -*- coding: utf-8 -*-
"""I trascorsi del personaggio, in DUE finestre con due metri diversi.

RETE 17. Le cinque righe dei trascorsi vengono da cinque blocchi di
`command.hsp` (`*setHistory1..5`), una `lang()` per ogni valore di `ohanasi<n>`,
e si leggono in **due** posti che non si somigliano.

## SITO A — la creazione del personaggio (`chara.hsp:3305`)

La finestra e' larga **360** px e le righe le scrive un `mes`, che non taglia e
non va a capo: passata la larghezza il testo esce dal bordo destro della
pergamena, sul marmo nudo.

    display_window (windoww - 360) / 2 + inf_screenx, ..., 360, 352
    pos wx + 75, wy + 200 + i * 15
    mes s

Il carattere e' quello lasciato dal giro precedente del ciclo — `font ..., 15 -
en * 2, 1`, cioe' **13** in inglese — e avanza **7 px** per carattere, misurato
sulla schermata della 64a: la riga da 46 caratteri va da x=858 a x=1176, 318 px.

    tetto = (360 - 75 - CORNICE) / 7 = 38 caratteri

## SITO B — la scheda del personaggio (`command.hsp:10539` e altri quattro)

Qui il testo passa da `talk_conv s, 32`, che **manda a capo**, e l'avanzo viene
disegnato **7 px** sotto la prima riga dove il passo fra una voce e l'altra e'
**15**: la seconda riga finisce *sopra* la voce successiva.

    talk_conv s, 32
    s(1) = "" ...
    split s, "\\n", s
    pos wx + 220 - en * 15, wy + 290
    mes s
    if ( strlen(s(1)) >= 1 ) {
        pos wx + 220 - en * 15, wy + 290 + 0 * 15 + 7     <- +7 su un passo di 15
        mes s(1) + " " + s(2) + " " + s(3) + " " + s(4)
    }

Il vincolo qui **non e' una larghezza in pixel** — la finestra e' larga 700 e il
testo comincia a `wx + 205` con il carattere a corpo 10, quindi di spazio ce
n'e' da vendere — **e' un conteggio di righe: deve venirne UNA**.

## ⚠️⚠️ E il sito B non si misura con `len()`

`talk_conv` (`init.hsp:1326`, ramo non giapponese) e' un a-capo **greedy sulle
parole**, e l'ultimo pezzo dopo l'ultimo spazio viene appeso **senza controllo**.
Quindi va a capo se e solo se

    somma di (len(parola) + 1) su tutte le parole TRANNE L'ULTIMA  >  32

e **la lunghezza totale non c'entra**. Misurato con `len() > 32` il perimetro
sembrava di **24** righe (65a); con il compositore vero e' di **7** — e tre
delle sette hanno l'inglese di monte **piu' lungo del nostro**, che pero' sta in
una riga sola perche' finisce con una parola lunga:

    en 45  Though have a strong sense of responsibility,   -> 1 riga
    it 44  Un senso di responsabilita' come nessuno, ma     -> 2 righe

💡 La leva per riparare una riga non e' accorciarla: e' **portare a 32 il pezzo
che sta prima dell'ultima parola**.

Il compositore non e' rifatto qui: e' quello di `descrizioni_cm.py` (RETE 19),
provato a schermo sulle descrizioni della 64a (Juere 6 righe, Warrior 8). Una
grammatica sola, in un posto solo.

## Il vincolo e' il sito piu' stretto dei due, ed e' B

⚠️ Provato prima sull'inglese di monte, come vuole la 61a. Qui l'inglese **non
tocca** nessuno dei due tetti: li sfonda tutt'e due, e di parecchio (97 righe su
226 oltre i 38 caratteri del sito A, 82 su 226 che vanno a capo nel sito B). La
finestra e' dimensionata sul **giapponese** — dove `talk_conv` conta i byte, e
32 byte fanno 16 caratteri — e upstream ci ha messo dentro un inglese che non ci
sta. Il perimetro del progetto e' percio' la coda **senza scuse di monte**: le
righe dove l'inglese sta dentro e noi no, e quelle dove sforiamo piu' di lui.
"""
import re
import sys
from pathlib import Path

from descrizioni_cm import talk_conv

SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx")
BUILD = Path(r"C:\Games\Elona\_traduzione\build\2.05-custom-gx")

# --- sito A: la creazione
LARGHEZZA = 360
SINISTRA = 75
CORNICE = 15
PASSO = 7
TETTO_CREAZIONE = (LARGHEZZA - SINISTRA - CORNICE) // PASSO
TETTO = TETTO_CREAZIONE   # il nome vecchio, che correzione-trascorsi.py della 64a usa ancora

# --- sito B: la scheda
A_CAPO = 32           # command.hsp:10540 e gli altri quattro, `talk_conv s, 32`
TETTO_RIGHE = 1       # l'avanzo cade a +7 px su un passo di 15

BLOCCHI = [
    ("setHistory1", 9454, 9595),
    ("setHistory2", 9595, 9733),
    ("setHistory3", 9733, 9871),
    ("setHistory4", 9871, 10009),
    ("setHistory5", 10009, 10145),
]

LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')


def righe(albero):
    testo = (albero / "command.hsp").read_text(encoding="cp932", errors="replace")
    linee = testo.splitlines()
    fuori = []
    for nome, da, a in BLOCCHI:
        for n in range(da, min(a, len(linee))):
            m = LANG.search(linee[n - 1])
            if m:
                fuori.append((nome, n, m.group(2)))
    return fuori


def coda(testo):
    """Il pezzo che sta PRIMA dell'ultima parola, spazi compresi.

    E' il numero che decide l'a-capo del sito B: se sta dentro `A_CAPO`, la riga
    e' una sola, per quanto lunga sia l'ultima parola.
    """
    i = testo.rfind(" ")
    return 0 if i == -1 else i + 1


def perimetro(sorgente, build, sfora, misura):
    """Le righe senza scuse di monte: l'inglese ci sta e noi no, o facciamo peggio."""
    nostre, peggio = [], []
    for k, it in build.items():
        en = sorgente.get(k, "")
        if not sfora(it):
            continue
        if not sfora(en):
            nostre.append((k, en, it))
        elif misura(it) > misura(en):
            peggio.append((k, en, it))
    return nostre, peggio


def referto():
    sorgente = {(b, n): t for b, n, t in righe(SORGENTE)}
    build = {(b, n): t for b, n, t in righe(BUILD)}

    print(f"--- SITO A, la creazione: mes senza a capo, tetto "
          f"({LARGHEZZA} - {SINISTRA} - {CORNICE}) / {PASSO} = {TETTO_CREAZIONE} caratteri")
    for etichetta, voci in (("inglese di monte", sorgente), ("build italiana", build)):
        fuori = [k for k, t in voci.items() if len(t) > TETTO_CREAZIONE]
        media = sum(len(t) for t in voci.values()) / len(voci)
        print(f"    {etichetta:18s} {len(voci)} righe, {len(fuori):3d} fuori misura, "
              f"lunghezza media {media:.1f}")

    print(f"\n--- SITO B, la scheda: talk_conv a {A_CAPO}, "
          f"deve venirne {TETTO_RIGHE} riga sola")
    for etichetta, voci in (("inglese di monte", sorgente), ("build italiana", build)):
        fuori = [k for k, t in voci.items() if len(talk_conv(t, A_CAPO)) > TETTO_RIGHE]
        media = sum(coda(t) for t in voci.values()) / len(voci)
        print(f"    {etichetta:18s} {len(voci)} righe, {len(fuori):3d} vanno a capo, "
              f"coda media {media:.1f}")

    gruppi = (
        ("SITO A", lambda t: len(t) > TETTO_CREAZIONE, len),
        ("SITO B", lambda t: len(talk_conv(t, A_CAPO)) > TETTO_RIGHE,
         lambda t: len(talk_conv(t, A_CAPO))),
    )
    totale = 0
    for etichetta, sfora, misura in gruppi:
        nostre, peggio = perimetro(sorgente, build, sfora, misura)
        totale += len(nostre) + len(peggio)
        print(f"\n=== il perimetro del {etichetta}: {len(nostre) + len(peggio)} righe")
        print(f"    l'inglese sta dentro e noi no : {len(nostre)}")
        print(f"    sforiamo piu' dell'inglese    : {len(peggio)}")
        for nome, gruppo in (("nostre", nostre), ("peggio", peggio)):
            for (b, n), en, it in sorted(gruppo, key=lambda v: -coda(v[2])):
                print(f"   [{nome}] coda {coda(it):3d} (en {coda(en):3d})  {b}:{n}")
                print(f"            it {len(it):3d}  {it}")
                print(f"            en {len(en):3d}  {en}")
    return totale


def prova():
    """⭐ Il banco di prova, sull'inglese di monte, come vuole la 61a.

    Le tre righe che dimostrano che il metro giusto e' la **coda** e non la
    lunghezza: la piu' lunga delle tre sta in una riga, la piu' corta no.
    """
    casi = [
        ("Though have a strong sense of responsibility,", 1),   # 45 caratteri, coda 30
        ("You were artificially created through an experiment.", 2),  # 52, coda 41
        ("Though don't like to be bound by anything,", 2),      # 42, coda 33
    ]
    print("--- prova del compositore sull'inglese di monte")
    ok = True
    for testo, atteso in casi:
        quante = len(talk_conv(testo, A_CAPO))
        segno = "ok  " if quante == atteso else "!!  "
        if quante != atteso:
            ok = False
        print(f"   {segno} {len(testo):3d} caratteri, coda {coda(testo):3d} -> "
              f"{quante} righe (atteso {atteso})   {testo}")
    return ok


if __name__ == "__main__":
    buono = prova()
    print()
    referto()
    sys.exit(0 if buono else 1)
