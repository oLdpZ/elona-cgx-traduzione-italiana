# strumenti/gronde.py
"""La gronda fra un'etichetta e il suo valore, dove il gioco disegna i due
a **due x fissi** invece di scriverli di seguito.

## Perche' e' una famiglia, e perche' nessuno la guardava

Le reti di larghezza del progetto misurano tutte lo stesso mestiere: **quanto
spazio ha una stringa prima del bordo del riquadro**. `larghezze`, `diario`,
`riquadri`, `menu_dialogo`, `linguette`, `intestazioni_larghezze` — sei reti,
un solo tipo di ostacolo, il contenitore.

Qui l'ostacolo e' un altro: non c'e' nessun bordo, c'e' **la stringa
successiva**, e non e' nemmeno la stringa successiva del testo — e' un `mes`
diverso, in un ciclo diverso, centocinquanta righe piu' in la' nel sorgente.
Il gioco disegna l'etichetta a un `pos` e il valore a un altro:

    command.hsp:10506   pos wx + 30 + cnt / 5 * 190      «Classe»
    command.hsp:10661   pos wx + 79 + cnt / 5 * 190      «Guerriero»

Fra i due c'e' una gronda, e la gronda e' un tetto: se l'etichetta italiana e'
piu' larga, il valore le finisce **sopra**. A schermo si legge
«ClasseGuerriero», e non e' un troncamento — e' sovrastampa.

⚠️⚠️ **E il difetto non si vede in inglese.** «Class» ha 5 caratteri, «Classe»
6; «Speed» 5, «Velocita'» 9; «Height» 6, «Altezza» 7. Il numero e' tarato sulla
parola inglese, e la parola italiana e' quasi sempre piu' lunga: e' esattamente
la forma di difetto che una build tradotta produce e una build inglese no.
Dichiarato nella 68a («Classe e Guerriero una sopra l'altra, Altezza157 cm,
Velocita70(70)»), rimasto scoperto per quattro sessioni perche' nessuna delle
sei reti guarda questa geometria.

## ⚠️ Si legge la BUILD, non il sorgente pinnato

Le altre reti leggono `sorgente/`, perche' misurano il testo che il dizionario
scrivera'. Questa misura la **geometria**, e la geometria del progetto la
cambiano le toppe: le due della 72a spostano i valori a `wx + 79` e `wx + 325`
proprio per aprire la gronda. Letta sul sorgente, questa rete direbbe per
sempre che «Classe» sfora.

⭐ E leggendo la build si guadagna una seconda cosa: **l'italiano e' gia' nella
fessura inglese della `lang()`**, quindi non serve nemmeno il dizionario. Quel
che la rete legge e' quel che il giocatore vede.

💡 **E la build e' anche l'unica che dice quale riga e' viva.** Nella colonna
del carico i valori hanno due `pos`: `wx + 86` e `wx + 102`. Il primo e' dentro
un blocco `ORIGINAL - BEGINNING` commentato, il secondo e' la modifica di monte
che lo ha sostituito. Chi prendesse il primo misurerebbe una gronda di 57 px
che non esiste — quella vera e' 73.

## Il passo del carattere

`command.hsp` disegna la scheda con `font ..., 12 + sizefix - en * 2`
(`:10492`). ⚠️ Ma il passo NON e' proporzionale al corpo: e' quello del glifo a
larghezza fissa, e sulle schermate del collaudo della 72a vale **7 px**, lo
stesso di `menu_dialogo` — «Classe» a 42 px, «Altezza» a 49, «Velocita'» a 63,
e tutte e tre sovrastampano come previsto. E' il numero che il gioco stesso usa
in `cs_list` (`module.hsp:70`).
"""
import re
import sys
from pathlib import Path

from strumenti import estrai
from strumenti import percorsi
from strumenti.accenti import degrada

PIXEL_PER_CARATTERE = 7

# lo spazio minimo fra la fine dell'etichetta e l'inizio del valore: un
# carattere. Sotto questo la scheda si legge «Altezza157 cm».
RESPIRO = 1


class Gronda:
    """Una coppia etichetta/valore disegnata a due `pos` fissi.

    `ancora_etichette` e `ancora_valori` sono il testo esatto delle due righe
    `pos` nella build: si **cercano** invece di puntare a un numero di riga,
    cosi' se upstream le riscrive la rete si ferma con un errore invece di
    misurare la riga sbagliata. `scarto` e' l'offset in piu' che il valore
    prende in build non giapponese (`en * ...`), che la riga `pos` porta come
    espressione e non come numero.
    """

    def __init__(self, nome, file, ancora_etichette, ancora_valori,
                 indici=None, scarto=0):
        self.nome = nome
        self.file = file
        self.ancora_etichette = ancora_etichette
        self.ancora_valori = ancora_valori
        self.indici = indici
        self.scarto = scarto


_PRIME_CINQUE = "pos wx + 30 + cnt / 5 * 190, wy + 47 + cnt \\ 5 * 15"
_LORO_VALORI = ("pos wx + 79 + cnt / 5 * 190 + en * ((cnt > 4) * 12), "
                "wy + 46 + cnt \\ 5 * 15")

GRONDE = [
    Gronda("scheda: Nome, Alias, Razza, Sesso, Classe", "command.hsp",
           _PRIME_CINQUE, _LORO_VALORI, indici=range(0, 5)),
    Gronda("scheda: Eta', Altezza, Peso, Iniz., AP", "command.hsp",
           _PRIME_CINQUE, _LORO_VALORI, indici=range(5, 10), scarto=12),
    Gronda("scheda: Livello, Prossimo, Fede, Gilda, Crescita", "command.hsp",
           "pos wx + 355, wy + 46 + cnt * 15",
           "pos wx + 418 + en * 5, wy + 45 + cnt * 15", scarto=5),
    Gronda("scheda: Vita, Mana, Follia, Velocita', Fama, Karma", "command.hsp",
           "pos wx + 255, wy + 151 + cnt * 15",
           "pos wx + 325, wy + 151 + cnt * 15"),
    Gronda("scheda: Carico, Limite, Peso eq., Turni, Tempo", "command.hsp",
           "pos wx + 29, wy + 290 + cnt * 15",
           "pos wx + 102, wy + 289 + cnt * 15"),
]

_POS_X = re.compile(r"pos wx \+ (\d+)")
_ASSEGNA = re.compile(r"\s*s = ")


def _righe(file: str, build: Path | None = None) -> list[str]:
    radice = build or percorsi.BUILD_HSP
    return (radice / file).read_bytes().decode("cp932").splitlines()


def _trova(righe: list[str], ancora: str, file: str) -> int:
    trovate = [i for i, r in enumerate(righe) if r.strip() == ancora]
    if len(trovate) != 1:
        raise LookupError(
            "%s: la riga %r si trova %d volte, non una. La geometria e' "
            "cambiata: la gronda va rimisurata sulla nuova, non indovinata."
            % (file, ancora, len(trovate)))
    return trovate[0]


def etichette_di(righe: list[str], riga_pos: int) -> list[str]:
    """Le etichette italiane del `s = lang(...), lang(...)` che precede il `pos`.

    ⚠️ Si risale al **primo** `s = ` sopra il `pos`, che e' l'idioma della
    scheda: si riempie l'array, poi lo si disegna in un `repeat`. Un `if/else`
    che assegna `s` due volte (`:10495` e `:10498`) lascia sopra il `pos` il
    ramo piu' vicino, e i due rami hanno le stesse etichette nelle stesse
    caselle: fra un ramo e l'altro cambia **quante** caselle sono piene, non
    che cosa c'e' scritto.
    """
    for i in range(riga_pos - 1, max(riga_pos - 12, -1), -1):
        testo = righe[i]
        if _ASSEGNA.match(testo):
            trovate = []
            for apertura in estrai.avvii(testo):
                argomenti = estrai.argomenti_di(testo, apertura)
                if argomenti and len(argomenti) == 2:
                    grezzo = argomenti[1].strip()
                    if grezzo.startswith('"') and grezzo.endswith('"'):
                        trovate.append(grezzo[1:-1])
            return trovate
    raise LookupError("nessun 's = ' nelle dodici righe sopra la %d"
                      % (riga_pos + 1))


def misura(gronda: Gronda, build: Path | None = None) -> dict:
    righe = _righe(gronda.file, build)
    i_et = _trova(righe, gronda.ancora_etichette, gronda.file)
    i_val = _trova(righe, gronda.ancora_valori, gronda.file)
    x_et = int(_POS_X.search(righe[i_et].strip()).group(1))
    x_val = int(_POS_X.search(righe[i_val].strip()).group(1)) + gronda.scarto
    etichette = etichette_di(righe, i_et)
    if gronda.indici is not None:
        etichette = [e for n, e in enumerate(etichette) if n in gronda.indici]
    return {
        "nome": gronda.nome,
        "file": gronda.file,
        "riga_etichette": i_et + 1,
        "riga_valori": i_val + 1,
        "gronda": x_val - x_et,
        "etichette": [degrada(e) for e in etichette if e],
    }


def larghezza(etichetta: str) -> int:
    return (len(etichetta) + RESPIRO) * PIXEL_PER_CARATTERE


def fuori_misura(build: Path | None = None) -> list[tuple]:
    """(file, riga, nome, etichetta, larghezza_px, gronda_px) per ogni
    etichetta che non lascia passare il suo valore."""
    fuori = []
    for gronda in GRONDE:
        m = misura(gronda, build)
        for etichetta in m["etichette"]:
            if larghezza(etichetta) > m["gronda"]:
                fuori.append((m["file"], m["riga_etichette"], m["nome"],
                              etichetta, larghezza(etichetta), m["gronda"]))
    return fuori


def main(argv: list[str] | None = None) -> int:
    for gronda in GRONDE:
        m = misura(gronda)
        piu_lunga = max(m["etichette"], key=len, default="")
        usati = larghezza(piu_lunga)
        print("  %-52s gronda %3d px   la piu' lunga: %-14s %3d px  %s"
              % (m["nome"], m["gronda"], "<%s>" % piu_lunga, usati,
                 "SFORA" if usati > m["gronda"] else "ok"))
    sfori = fuori_misura()
    if sfori:
        print()
        for file, riga, nome, etichetta, usati, gronda in sfori:
            print("  %s:%d  <%s> %d px in una gronda da %d  (%s)"
                  % (file, riga, etichetta, usati, gronda, nome))
    print("\netichette che sovrastampano il valore: %d su %d gronde misurate"
          % (len(sfori), len(GRONDE)))
    return 1 if sfori else 0


if __name__ == "__main__":
    sys.exit(main())
