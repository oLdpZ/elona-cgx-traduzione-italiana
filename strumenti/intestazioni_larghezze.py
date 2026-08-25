# strumenti/intestazioni_larghezze.py
"""RETE 20. Quanto puo' essere lunga un'intestazione di colonna prima di
sbattere in qualcosa.

`display_topic` (`module.hsp:4364`) disegna un'icona da 24 px, poi il testo
**26 px** piu' in la' con un `mes` che non taglia e non va a capo:

    #deffunc display_topic str testo, int x, int y, int
        font lang(cfg_font1, cfg_font2), 12 + sizefix - en * 2, 1
        pos x, y + 7      : gcopy 3, 120, 360, 24, 16      <- l'icona
        pos x + 26, y + 8 : mes testo                      <- il testo
        line x + 22, y + 21, x + strlen(testo) * 7 + 36, y + 21

Il testo comincia a `x + 26` e ogni carattere avanza di 7 px, quindi il tetto
di un'intestazione e' `(ostacolo - x - 26) / 7` caratteri, dove l'ostacolo e'
**la cosa piu' a sinistra fra quelle che le stanno a destra**.

## ⚠️⚠️⚠️ Il punto cieco che e' costato due difetti: l'ULTIMA della riga

Fino alla 68a questa rete guardava **solo** le coppie di intestazioni vicine, e
sull'ultima di ogni riga scriveva «il suo limite e' il bordo della finestra, che
sta altrove». Non lo guardava nessuno, e nella 68a il collaudo ne ha trovate due
rotte nella stessa finestra — la scheda del personaggio, che il giocatore apre
di continuo:

    command.hsp:10431  «Benedizioni e malocchi»  22 caratteri, tetto 18  TAGLIATA
    command.hsp:10429  «Tiri di combattimento»   21 caratteri, tetto 16  SOVRAPPOSTA

💡 E il limite **non era il bordo della finestra** in nessuno dei due casi. Era
il **ritratto** (`window2 wx + 557, wy + 23, 87, 120`, disegnato sessanta righe
dopo, quindi ci passa sopra) e una **`mes`** (`pos wx + 542, wy + 263` con
«Pot. magia»). Una cosa disegnata dopo copre quel che c'era prima, e il bordo
della finestra non la nomina.

Percio' adesso la rete cerca gli **ostacoli**: qualunque `window2`, `mes` o
immagine piazzata dentro la stessa etichetta HSP, la cui fascia verticale
incrocia quella dell'intestazione e la cui `x` le sta a destra.

## Il confine e' l'etichetta, non un numero di righe

Fra l'intestazione a `command.hsp:10429` e la `mes` che la limita a `:10733`
corrono trecento righe: nessuna finestra di righe scelta a occhio le tiene
insieme senza tenere insieme anche mezzo file. Il confine giusto ce l'ha il
linguaggio — `*com_charainfo_loop_WHILE1` — e dentro a un'etichetta HSP tutto
quel che si disegna finisce sulla stessa schermata.

## Il corpo e' 11, non 10

`sizefix` viene da `config.txt` (`fontSfix1. "1"`, `config.hsp:180`) e vale **1**
in inglese; `config.hsp:436` lo azzera solo nel ramo giapponese. Il corpo qui e'
`12 + 1 - 2 = 11`.

## ⚠️⚠️⚠️ E il passo a corpo 11 e' 7, MISURATO — non si deduce

La prima stesura di questa rete usava **6**, da `int(0,6 * 11)`, e si dichiarava
provata perche' con 6 l'inglese di monte non sforava da nessuna parte. **Era un
ragionamento circolare**: il passo era stato scelto proprio perche' faceva
tornare la prova. La regola della 63a — *il tetto vero lo tocca l'inglese* — e'
un **controllo**, non un modo di ricavare una costante.

Il numero vero e' a schermo, ed e' stato misurato tre volte su tre finestre
diverse: la scheda delle modalita' nella 65a (`chara.hsp:4193`, 72 caratteri in
503 px), e nella 68a le intestazioni di questa stessa finestra —
«Attributi base - Potenziale» da 27 caratteri copre 664→847 fra il primo glifo e
l'ultimo, cioe' 183 px su 26 intervalli: **7,038**.

## ⚠️ E con il passo giusto l'inglese di monte SFORA in tre posti

Non e' un difetto della rete: e' un difetto del gioco, piccolo e mai notato.
L'icona della colonna dopo viene disegnata **dopo** il testo di quella prima, e
gli copre la coda.

    command.hsp:4199   Message(Impress)             16 su 15   elenco avventurieri
    command.hsp:10410  Attributes(Org) - Potential  27 su 26   scheda personaggio
    command.hsp:2601   Name                          4 su  3   finestra dei talenti

Il secondo si vede **solo** nelle partite in modalita' speciale, perche' la
casella a `wx + 240` che gli sta accanto negli altri casi e' vuota. Sono le
colonne piu' strette del gioco, ed e' il motivo per cui la resa italiana di
`:10410` sta a 27 e non a 29: **non piu' lunga di monte**, che e' il metro del
progetto dove monte gia' sfora.

## ⚠️ Che cosa NON misura

- **Le chiamate con la `x` per espressione** (`wx + ww / 2`) o con il **testo in
  una variabile**: quelle le trova `intestazioni.py`, che e' un'altra rete.
- **Le intestazioni senza nessun ostacolo a destra dentro la loro etichetta.**
  Non sono «a posto»: sono **non misurate**, e il referto le conta a parte.
- **Le coppie a meno di 40 px**, che non sono colonne ma **rami alternativi** di
  un `if`: `command.hsp:7625` ne e' l'unico caso, «Level(Piety Cost)» a `wx+328`
  e «Level» a `wx+348`, in `if` e `else`.

⚠️ E si misura sulla forma **degradata**: `applica` scrive «Modalita'» dove il
dizionario dice «Modalità», e l'apostrofo e' un carattere in piu'.
"""
import collections
import io
import re
import sys

from strumenti import percorsi

CORPO = 11       # module.hsp:4365, `12 + sizefix - en * 2` con sizefix = 1
PASSO = 7        # misurato a schermo nella 65a e nella 68a. Vedi il docstring.
ICONA = 26       # module.hsp:4370, `pos x + 26` -- il testo parte dopo l'icona
GAP_MINIMO = 40  # sotto questo, le due chiamate sono rami alternativi, non colonne

# La fascia verticale che il testo dell'intestazione occupa, relativa alla `y`
# della chiamata: `pos x + 26, y + 8` piu' l'altezza del carattere a corpo 11.
# ⚠️ L'inchiostro e' alto **12** px, misurato nella 68a (righe 456-467 per una
# chiamata con `y` 448). Con 15 la fascia arrivava a toccare la riga di valori
# sotto -- `chat.hsp:25513` ha un `mes` a `wy + 245`, tre px dentro -- e la rete
# inventava tre colonne dal tetto zero.
ALTO, BASSO = 8, 20

ALTEZZA_MES = 16  # una riga di testo, qualunque corpo fra 10 e 14

# I due siti dove l'inglese di monte sfora gia' di suo: il perimetro del progetto
# li' non e' il tetto, e' «non piu' lungo di monte».
DI_MONTE = {("command.hsp", 4199), ("command.hsp", 10410)}

ETICHETTA = re.compile(r"^\*\w+")
LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')
NUDO = re.compile(r'^"((?:[^"\\]|\\.)*)"$')

# ⚠️ La `x` puo' portare un termine `en`: `pos wx + 564 - en * 22` e' la `mes`
# che limita «Tiri di combattimento», e con la regex senza `en` la rete non la
# vedeva -- cioe' non vedeva il secondo dei due difetti che l'hanno fatta
# riscrivere. Nella build inglese `en` vale 1.
_X = r"wx \+ (\d+)(?:\s*([-+])\s*en \* (\d+))?"
_Y = r"wy \+ (\d+)"

CHIAMA = re.compile(r"^\s*display_topic\s+(.+?),\s*" + _X + r",\s*" + _Y)
POS = re.compile(r"^\s*pos\s+" + _X + r",\s*" + _Y + r"\s*$")
FINESTRA = re.compile(r"^\s*window2\s+" + _X + r",\s*" + _Y + r",\s*(\d+),\s*(\d+)")
DISEGNA = re.compile(r"^\s*(mes|bmes)\b")
GZOOM = re.compile(r"^\s*gzoom\s+(\d+),\s*(\d+)")
GCOPY = re.compile(r"^\s*gcopy\s+.*,\s*(\d+),\s*(\d+)\s*$")
# righe che stanno fra un `pos` e il disegno vero senza spostare niente
NEUTRA = re.compile(r"^\s*(color|font|gmode|objcolor|;|//|$)")


def ascissa(base, segno, termine):
    """`wx + 564 - en * 22` vale 542: nella build inglese `en` e' 1."""
    x = int(base)
    if segno:
        x += int(termine) * (1 if segno == "+" else -1)
    return x


def testo_di(argomento):
    """L'inglese dell'intestazione, o None se non e' un letterale."""
    m = LANG.search(argomento)
    if m:
        return m.group(2)
    m = NUDO.match(argomento.strip())
    return m.group(1) if m else None


def blocchi(righe):
    """[(prima, ultima)] per ogni etichetta HSP: e' il confine di una schermata."""
    tagli = [n for n, r in enumerate(righe) if ETICHETTA.match(r)]
    if not tagli or tagli[0] != 0:
        tagli.insert(0, 0)
    tagli.append(len(righe))
    return [(tagli[i], tagli[i + 1]) for i in range(len(tagli) - 1)]


def ostacoli(righe, prima, ultima):
    """[(x, alto, basso)] di tutto cio' che viene disegnato dentro il blocco.

    Un `pos` da solo non disegna niente: conta solo se la riga che segue --
    saltate quelle che cambiano colore o carattere -- e' un `mes`, una `gzoom` o
    una `gcopy`. Cosi' un `pos` seguito da un `line` non inventa un ostacolo.
    """
    trovati = []
    for n in range(prima, ultima):
        f = FINESTRA.match(righe[n])
        if f:
            x = ascissa(f.group(1), f.group(2), f.group(3))
            y, h = int(f.group(4)), int(f.group(6))
            trovati.append((x, y, y + h))
            continue
        p = POS.match(righe[n])
        if not p:
            continue
        x = ascissa(p.group(1), p.group(2), p.group(3))
        y = int(p.group(4))
        for m in range(n + 1, min(n + 6, ultima)):
            if NEUTRA.match(righe[m]):
                continue
            if DISEGNA.match(righe[m]):
                trovati.append((x, y, y + ALTEZZA_MES))
            elif GZOOM.match(righe[m]):
                trovati.append((x, y, y + int(GZOOM.match(righe[m]).group(2))))
            elif GCOPY.match(righe[m]):
                trovati.append((x, y, y + int(GCOPY.match(righe[m]).group(2))))
            break
    return trovati


def leggi(cartella, nome):
    return io.open(cartella / nome, encoding="cp932",
                   errors="replace").read().split("\n")


def misure(cartella):
    """[(file, riga, y, x, limite, perche', testo)] per ogni intestazione misurabile.

    `limite` e' la `x` della cosa piu' vicina a destra; `perche'` dice se e'
    un'altra intestazione o un ostacolo disegnato dopo.
    """
    fatte, saltate, senza = [], 0, []
    for percorso in sorted(cartella.glob("*.hsp")):
        righe = leggi(cartella, percorso.name)
        for prima, ultima in blocchi(righe):
            teste, salti = [], 0
            for n in range(prima, ultima):
                m = CHIAMA.match(righe[n])
                if not m:
                    if re.match(r"^\s*display_topic\s", righe[n]):
                        salti += 1
                    continue
                t = testo_di(m.group(1))
                if t is None:
                    salti += 1
                    continue
                teste.append((n + 1, int(m.group(5)),
                              ascissa(m.group(2), m.group(3), m.group(4)), t))
            saltate += salti
            if not teste:
                continue
            muri = ostacoli(righe, prima, ultima)
            per_riga = collections.defaultdict(list)
            for riga, y, x, t in teste:
                per_riga[y].append((riga, x, t))
            for y, gruppo in per_riga.items():
                gruppo.sort(key=lambda v: v[1])
                for i, (riga, x, t) in enumerate(gruppo):
                    limite, perche = None, ""
                    if i + 1 < len(gruppo) and gruppo[i + 1][1] - x >= GAP_MINIMO:
                        limite, perche = gruppo[i + 1][1], "intestazione"
                    for mx, alto, basso in muri:
                        if mx <= x + ICONA:
                            continue
                        if basso <= y + ALTO or alto >= y + BASSO:
                            continue
                        if limite is None or mx < limite:
                            limite, perche = mx, "ostacolo"
                    if limite is None:
                        senza.append((percorso.name, riga, y, x, t))
                    else:
                        fatte.append((percorso.name, riga, y, x, limite, perche, t))
    return fatte, saltate, senza


def tetto(x, limite):
    return (limite - x - ICONA) // PASSO


def _scuse_per_ordinale():
    """`DI_MONTE` tradotto da coordinate del SORGENTE a ordinali.

    ⚠️ `DI_MONTE` sono righe del sorgente pinnato, e la scusa va stampata accanto
    ai siti della **build**, che non ha piu' gli stessi numeri di riga (vedi
    `_per_ordinale`). Prima della 98a il confronto era diretto, e la toppa di
    `book.txt` ha fatto sparire la scusa da `Attributi base - Potenziale`: il
    sito restava fuori misura — giusto — ma senza piu' dire che **sfora anche
    in inglese**, che e' la meta' che decide se e' un difetto nostro.
    """
    ordinali = _per_ordinale(misure(percorsi.SORGENTE_HSP)[0])
    return {chiave for chiave, c in ordinali.items() if (c[0], c[1]) in DI_MONTE}


def referto(cartella, etichetta):
    fatte, saltate, senza = misure(cartella)
    posizione = {id(c): chiave for chiave, c in _per_ordinale(fatte).items()}
    scuse = _scuse_per_ordinale()
    sfora = [c for c in fatte if len(c[6]) > tetto(c[3], c[4])]
    print("--- %s: %d intestazioni misurate (%d senza ostacolo a destra, "
          "%d con x o testo illeggibili), %d fuori misura"
          % (etichetta, len(fatte), len(senza), saltate, len(sfora)))
    for colonna in sorted(sfora):
        nome, riga, y, x, limite, perche, t = colonna
        scusa = "  (sfora anche l'inglese)" if posizione[id(colonna)] in scuse else ""
        print("   %s:%d  wy+%d  x %d -> %d (%s), tetto %d, lunghezza %d   %r%s"
              % (nome, riga, y, x, limite, perche, tetto(x, limite), len(t), t, scusa))
    return sfora


def _per_ordinale(colonne):
    """Le colonne indicizzate per (file, quantesima nel file), non per riga.

    ⚠️⚠️ **PERCHE' NON PER RIGA: LA BUILD LA MUOVIAMO NOI.** Fino alla 98a questa
    funzione appaiava sorgente e build con la chiave `(file, riga)`. Regge finche'
    ogni toppa sostituisce una riga con una riga — e per 1.023 toppe e' stato
    cosi'. Le toppe dei **file dati** no: mettono sette righe al posto di una (il
    ramo `exist` piu' il ripiego), e quella di `book.txt` su `command.hsp:8371`
    ha spostato in giu' di **6** tutto quel che segue.

    ⚠️ Il guasto non e' stato un test rosso: e' stato un **verdetto cambiato**.
    `monte.get(("command.hsp", 10416))` non trovava niente, l'inglese risultava
    la stringa vuota, e il perimetro accusava `Attributi base - Potenziale` di
    sforare dove l'inglese sta — quando quella colonna sfora da sempre in
    tutt'e due le lingue. Una rete che tace quando dovrebbe parlare si nota; una
    che parla di un sito innocente perche' ha guardato la coordinata sbagliata
    si crede.

    L'ordinale invece regge: una toppa sposta le righe, non aggiunge siti di
    disegno. E se un giorno ne aggiungesse uno, il conto per file cambia e
    `perimetro()` se ne accorge, invece di appaiare a caso.
    """
    per_file = collections.defaultdict(list)
    for colonna in colonne:
        per_file[colonna[0]].append(colonna)
    return {(nome, i): c for nome, gruppo in per_file.items()
            for i, c in enumerate(gruppo)}


def perimetro():
    """Le colonne senza scuse di monte: l'inglese ci sta e noi no, o siamo piu' lunghi."""
    monte = _per_ordinale(misure(percorsi.SORGENTE_HSP)[0])
    nostro = _per_ordinale(misure(percorsi.BUILD_HSP)[0])

    # ⚠️ Se un file ha un numero di siti diverso fra sorgente e build, l'ordinale
    # non appaia piu' niente e va detto, non nascosto: e' l'unico modo in cui
    # questa chiave puo' rompersi.
    conta = lambda d: collections.Counter(nome for nome, _ in d)
    discordi = {n for n, q in conta(nostro).items() if conta(monte).get(n) != q}
    if discordi:
        print("\n⚠️ SITI IN NUMERO DIVERSO fra sorgente e build, il confronto "
              "non e' appaiabile: " + ", ".join(sorted(discordi)))

    fuori = []
    for k, c in sorted(nostro.items()):
        nome, riga, _y, x, limite, perche, it = c
        en = monte.get(k, (None,) * 7)[6] or ""
        if len(it) <= tetto(x, limite):
            continue
        if len(en) <= tetto(x, limite) or len(it) > len(en):
            fuori.append((nome, riga, x, limite, perche, en, it))
    print("\n=== il perimetro: %d colonne" % len(fuori))
    for nome, riga, x, limite, perche, en, it in fuori:
        print("   %s:%d  tetto %d (%s)   en %2d %r" % (nome, riga, tetto(x, limite), perche, len(en), en))
        print("   %s  it %2d %r" % (" " * (len(nome) + len(str(riga)) + 14), len(it), it))
    return fuori


def prova():
    """⭐ Il banco: l'inglese di monte sfora nei siti noti e in nessun altro.

    Non e' «zero fuori misura»: con il passo misurato l'inglese sfora davvero in
    qualche colonna, e la rete deve dirlo. Se ne comparisse una nuova, o ne
    sparisse una, e' cambiato il sorgente o e' sbagliata la rete.
    """
    sfora = referto(percorsi.SORGENTE_HSP, "inglese di monte")
    trovato = {(c[0], c[1]) for c in sfora}
    ok = trovato == DI_MONTE
    print("   prova: attesi %s, trovati %s -> %s"
          % (sorted(DI_MONTE), sorted(trovato), "ok" if ok else "IL METRO NON REGGE"))
    return ok


def main(argv: list[str] | None = None) -> int:
    buono = prova()
    print()
    fuori = referto(percorsi.BUILD_HSP, "build italiana")
    perimetro()
    return 0 if buono and not fuori else 1


if __name__ == "__main__":
    sys.exit(main())
