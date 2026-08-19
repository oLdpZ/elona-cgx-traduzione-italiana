# -*- coding: utf-8 -*-
"""Le descrizioni di razza e classe nella creazione: quante righe entrano.

RETE 19. `chara.hsp:4569` compone la descrizione e la scrive sotto l'intestazione
«Descrizione»; a `wy + 166` comincia «Bonus attributi», che il testo non deve
raggiungere.

    talk_conv buff, 60 + en * 2      ; a capo automatico a 62 caratteri
    pos tx - 20, ty                  ; ty = wy + 62
    mes buff
    ...
    ty = wy + 166
    display_topic «Bonus attributi», tx, ty

Il passo di riga e' **15 px**, quindi lo spazio e' (166 - 62) / 15 = 6,9 righe:
la settima arriva a `wy + 152` e ci sta, l'**ottava** cade su `wy + 167` e si
sovrappone all'intestazione. Il tetto e' **7 righe**.

⚠️ Il conto delle righe non e' `len(testo) / 62`: `talk_conv` (`init.hsp:1279`,
ramo non giapponese) e' un a-capo **greedy sulle parole** -- accumula finche' la
parola dopo non ci sta piu' -- quindi una parola lunga in fondo alla riga la
chiude prima. Qui sotto la funzione e' rifatta com'e' scritta in HSP, incluso il
fatto che l'ultimo pezzo dopo l'ultimo spazio viene appeso **senza controllo**.

⭐ **Provato sulle schermate della 64a**, come vuole la 61a: la descrizione della
razza Juere si legge a schermo su **6** righe e quella della classe Warrior su
**7 piu' una**, ed e' proprio l'ottava -- «[Onslaught] Increased chance for an
additional melee attack.» -- che a schermo sta sopra «Bonus attributi». Il
simulatore deve dire gli stessi numeri; se non li dice, e' il simulatore a
essere sbagliato, non la geometria.

⚠️ **Upstream sfonda gia' di suo**: la regola per l'italiano non e' «7 righe» e
basta, e' «7 righe dove l'inglese ci sta, e comunque mai piu' righe
dell'inglese».
"""
import re
import sys
from pathlib import Path

SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx")
BUILD = Path(r"C:\Games\Elona\_traduzione\build\2.05-custom-gx")

LARGHEZZA = 62          # talk_conv buff, 60 + en * 2
TETTO = 7               # (166 - 62) / 15 = 6,9 -> la settima ci sta, l'ottava no

FILE = ("db_race.hsp", "db_class.hsp")

# `buff = lang("...", "...")` -- la descrizione lunga. `racename`/`classname`
# sono un'altra cosa e non passano di qui.
RIGA = re.compile(r'buff\s*=\s*lang\(\s*"(?:[^"\\]|\\.)*"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')


def talk_conv(testo, larghezza=LARGHEZZA):
    """Il ramo non giapponese di `talk_conv` (init.hsp:1326-1369), riga per riga.

    HSP lavora su `instr(msgtemp, 0, " ")`, cioe' la posizione del primo spazio:
    `p` e' quella posizione piu' uno, ovvero la lunghezza della parola **con** lo
    spazio che la chiude. Quando `len + p` passa la larghezza si va a capo. Il
    resto senza piu' spazi viene appeso in coda cosi' com'e'.
    """
    resto = testo
    righe = []
    corrente = ""
    while True:
        i = resto.find(" ")
        if i == -1:
            break
        p = i + 1
        if len(corrente) + p > larghezza:
            righe.append(corrente)
            corrente = ""
            continue
        corrente += resto[:p]
        resto = resto[p:]
    return righe + [corrente + resto]


def voci(albero):
    fuori = []
    for nome in FILE:
        testo = (albero / nome).read_text(encoding="cp932", errors="replace")
        for n, linea in enumerate(testo.splitlines(), 1):
            m = RIGA.search(linea)
            if m and m.group(1).strip():
                fuori.append((nome, n, m.group(1)))
    return fuori


def referto():
    print(f"a capo a {LARGHEZZA} caratteri, tetto {TETTO} righe")
    sorgente = {(f, n): t for f, n, t in voci(SORGENTE)}
    build = {(f, n): t for f, n, t in voci(BUILD)}

    for etichetta, v in (("inglese di monte", sorgente), ("build italiana", build)):
        conti = {k: len(talk_conv(t)) for k, t in v.items()}
        fuori = {k: r for k, r in conti.items() if r > TETTO}
        print(f"\n--- {etichetta}: {len(v)} descrizioni, {len(fuori)} oltre le {TETTO} righe")
        for k, r in sorted(fuori.items(), key=lambda x: -x[1])[:10]:
            print(f"   {r} righe  {k[0]}:{k[1]}  {v[k][:60]}...")

    # il perimetro: dove l'inglese sta e noi no, o dove facciamo piu' righe
    nostre, peggio = [], []
    for k, it in build.items():
        en = sorgente.get(k, "")
        r_it, r_en = len(talk_conv(it)), len(talk_conv(en))
        if r_it <= TETTO:
            continue
        (nostre if r_en <= TETTO else peggio if r_it > r_en else []).append((k, r_en, r_it))
    print(f"\n=== il perimetro: {len(nostre) + len(peggio)}")
    print(f"    l'inglese ci sta e noi no : {len(nostre)}")
    print(f"    piu' righe dell'inglese   : {len(peggio)}")
    for k, r_en, r_it in nostre + peggio:
        print(f"   {k[0]}:{k[1]}  en {r_en} righe -> it {r_it}")


def prova():
    """⭐ Il banco di prova: le due descrizioni lette a schermo nella 64a."""
    sorgente = {(f, n): t for f, n, t in voci(SORGENTE)}
    atteso = {"Juere": 6, "Warrior": 8}
    trovato = {}
    for (f, n), t in sorgente.items():
        if t.startswith("The Juere are a people wild and free"):
            trovato["Juere"] = len(talk_conv(t))
        if t.startswith("The Warrior."):
            trovato["Warrior"] = len(talk_conv(t))
    print("--- prova sulle schermate della 64a")
    ok = True
    for k, quante in atteso.items():
        v = trovato.get(k)
        segno = "ok  " if v == quante else "⚠️  "
        if v != quante:
            ok = False
        print(f"   {segno} {k:8s} atteso {quante} righe, il simulatore ne da' {v}")
    return ok


if __name__ == "__main__":
    buono = prova()
    print()
    referto()
    sys.exit(0 if buono else 1)
