"""Il terreno di `scene2.hsp`, misurato prima di tradurne una riga.

`scene2.hsp` e' il ramo inglese delle scene di storia: `scene.hsp:31` e `:49`
fanno `noteload lang("scene1.hsp", "scene2.hsp")`, e `main.hsp:1`-`:2` li
impacchettano dentro l'eseguibile. E' un fronte che nessuno ha mai aperto --
sta fuori dal perimetro `lang()`, quindi tutti i conteggi del progetto lo
ignorano.

Il file ha **due** renderer, e sono diversi:

`{txt}`   scene.hsp:452-473. Ogni riga del sorgente si disegna **verbatim**,
          centrata: `x = windoww/2 - strlen(s)*4`, e sotto ci va una targa
          larga `dx = 80 + strlen(s)*8`. Nessun a capo automatico: chi
          traduce impagina a mano. Font `16 - en*2` = **14** in inglese.
          ⚠️ Il budget non e' una taratura, e' l'aritmetica del renderer:
          la targa sta dentro una finestra da 800 px finche'
          `80 + strlen*8 <= 800`, cioe' **90 caratteri**; il testo vero,
          a 7,7 px/carattere, tocca il bordo a 103.

`{chat_N}` scene.hsp:427-436 -> `*chat` -> `*chat_scene` -> `chatMore buff`.
          Il blocco e' **una riga sola**, e a mandarla a capo e' il gioco:
          `talk_conv buff, 56 - en*3` = **53** caratteri, spezzando **sugli
          spazi** (init.hsp:1329-1368). Le righe si disegnano a
          `wy + 43 + cnt*19` (chat.hsp:25721-25732) e le voci del menu
          partono da `wy + wh - 56 - keyrange*19` = `wy + 305` con una voce
          sola: **13 righe** ci stanno, la quattordicesima tocca il menu.
          ⚠️ Qui il vincolo non e' la larghezza, e' **l'altezza**.

`{actor_N}` scene.hsp:400-404. `"<Nome>,54"`: `csvsort` taglia sulla virgola,
          il nome finisce in `actor(0, rc)` e si disegna in cima al riquadro
          (chat.hsp:25603-25609), il numero e' il **ritratto** e non si tocca.

Il referto non chiede zero: chiede di sapere quanto e' largo il fronte e
dove sta il pericolo prima di aprirlo.
"""
import re
import sys
from collections import Counter
from pathlib import Path

SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx")

# scene.hsp:449 -- font 16-en*2, e il renderer stesso conta 8 px per carattere
# (`strlen*4` per centrare, `strlen*8` per la targa)
FINESTRA = 800
BUDGET_TARGA = (FINESTRA - 80) // 8          # 90
BUDGET_BORDO = int(FINESTRA / 7.7)           # 103, il testo vero

# init.hsp:1279 -- talk_conv buff, 56 - en*3
COLONNA_CHAT = 53
# chat.hsp:25728 vs :25161 -- (305 - 43) / 19
RIGHE_CHAT = 13

_MARCATORE = re.compile(r"^\{([A-Za-z0-9_]+)\}")


def leggi(nome):
    testo = (SORGENTE / nome).read_bytes().decode("cp932")
    return testo.split("\r\n")


def blocchi(righe):
    """(scena, tipo, argomento, righe di prosa) per ogni blocco del file."""
    scena = None
    tipo = None
    prosa = []
    for riga in righe:
        spoglia = riga.strip()
        trovato = _MARCATORE.match(spoglia)
        if trovato is None:
            if spoglia and not spoglia.startswith(";"):
                prosa.append(riga)
            continue
        if tipo is not None:
            yield scena, tipo, argomento, prosa
        marcatore = trovato.group(1)
        argomento = spoglia[trovato.end():].strip().strip('"')
        prosa = []
        if marcatore.isdigit():
            scena, tipo = marcatore, None
            continue
        tipo = marcatore
    if tipo is not None:
        yield scena, tipo, argomento, prosa


def a_capo_come_il_gioco(testo, colonna=COLONNA_CHAT):
    """`talk_conv` nel ramo non giapponese: spezza sugli spazi, mai dentro.

    init.hsp:1331-1363. Si guarda il **prossimo spazio**: se la riga corrente
    piu' quella parola supera la colonna, si va a capo prima della parola. La
    coda senza spazi finisce tutta sull'ultima riga, lunga quanto viene.
    """
    resto = testo
    righe = []
    corrente = ""
    while True:
        taglio = resto.find(" ")
        if taglio == -1:
            break
        parola = resto[:taglio + 1]
        if len(corrente) + len(parola) > colonna:
            righe.append(corrente)
            corrente = ""
        corrente += parola
        resto = resto[taglio + 1:]
    righe.append(corrente + resto)
    return righe


def referto(nome="scene2.hsp"):
    righe = leggi(nome)
    tutti = list(blocchi(righe))
    conta = Counter(tipo for _, tipo, _, _ in tutti)
    prosa = sum(len(p) for _, _, _, p in tutti)
    print("== %s: %d righe, %d blocchi, %d righe di prosa"
          % (nome, len(righe), len(tutti), prosa))
    print("   " + ", ".join("%s %d" % (t, n) for t, n in conta.most_common(8)))

    print("\n-- {txt}: righe disegnate verbatim e centrate")
    righe_txt = [r for _, tipo, _, p in tutti if tipo == "txt" for r in p]
    lunghe = sorted(righe_txt, key=len, reverse=True)
    print("   %d righe in %d blocchi; la piu' lunga e' di %d caratteri"
          % (len(righe_txt), conta["txt"], len(lunghe[0])))
    oltre_targa = [r for r in righe_txt if len(r) > BUDGET_TARGA]
    oltre_bordo = [r for r in righe_txt if len(r) > BUDGET_BORDO]
    print("   oltre la targa (%d car.) : %d   <- gia' in inglese"
          % (BUDGET_TARGA, len(oltre_targa)))
    print("   oltre il bordo (%d car.): %d   <- gia' in inglese"
          % (BUDGET_BORDO, len(oltre_bordo)))
    print("   margine dell'inglese sulla targa: %d caratteri"
          % (BUDGET_TARGA - len(lunghe[0])))
    for r in lunghe[:3]:
        print("     %3d  %s" % (len(r), r.strip()))

    print("\n-- {chat_N}: il gioco manda a capo a %d, e nel riquadro ce ne"
          " stanno %d" % (COLONNA_CHAT, RIGHE_CHAT))
    chat = [(s, " ".join(x.strip() for x in p))
            for s, tipo, _, p in tutti if tipo and tipo.startswith("chat_") and p]
    misurati = sorted(((len(a_capo_come_il_gioco(t)), len(t), s, t)
                       for s, t in chat), reverse=True)
    istogramma = Counter(n for n, _, _, _ in misurati)
    print("   %d blocchi con testo; righe prodotte:" % len(misurati))
    for n in sorted(istogramma):
        print("     %2d righe : %3d blocchi%s"
              % (n, istogramma[n], "   <- sfora" if n > RIGHE_CHAT else ""))
    stretti = [m for m in misurati if m[0] >= RIGHE_CHAT - 2]
    print("   a due righe o meno dal fondo: %d" % len(stretti))
    for n, caratteri, scena, testo in misurati[:3]:
        print("     scena %-4s %2d righe, %4d caratteri: %s..."
              % (scena, n, caratteri, testo[:60]))

    print("\n-- {actor_N}: i nomi in cima al riquadro")
    attori = {}
    for _, tipo, arg, _ in tutti:
        if tipo and tipo.startswith("actor_"):
            nome_attore, _, ritratto = arg.rpartition(",")
            attori.setdefault(nome_attore or arg, set()).add(ritratto)
    print("   %d nomi distinti" % len(attori))
    senza_marca = [a for a in attori if not a.startswith("<")]
    print("   senza la marca <>: %d" % len(senza_marca))
    for a in sorted(attori, key=len, reverse=True)[:3]:
        print("     %2d car.  %s" % (len(a), a))
    return tutti


def divergenza():
    """Dove i due rami di lingua NON hanno gli stessi blocchi.

    Serve perche' `scene1.hsp` (giapponese) e `scene2.hsp` (inglese) sono due
    file paralleli ma non identici: 152 `{txt}` contro 147. Una scena che in
    inglese ha meno blocchi e' una scena che l'inglese ha gia' tagliato, e
    tradurre il taglio non lo rimette.
    """
    print("\n-- scene1.hsp (giapponese) contro scene2.hsp (inglese)")
    per_scena = {}
    for nome, colonna in (("scene1.hsp", 0), ("scene2.hsp", 1)):
        for scena, tipo, _, _ in blocchi(leggi(nome)):
            voce = per_scena.setdefault(scena, [Counter(), Counter()])
            voce[colonna][tipo] += 1
    diverse = []
    for scena, (jp, en) in per_scena.items():
        if jp != en:
            manca = {t: jp[t] - en[t] for t in set(jp) | set(en) if jp[t] != en[t]}
            diverse.append((scena, manca))
    print("   scene con struttura diversa: %d su %d" % (len(diverse), len(per_scena)))
    for scena, manca in diverse:
        print("     scena %-4s %s" % (scena, manca))


if __name__ == "__main__":
    referto()
    if "--divergenza" in sys.argv:
        divergenza()
