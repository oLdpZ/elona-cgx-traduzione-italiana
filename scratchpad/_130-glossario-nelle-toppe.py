# -*- coding: utf-8 -*-
"""Il glossario, misurato dove non lo misurava nessuno: dentro le toppe.

## Che cosa mancava

`glossario.md` si apre dicendo «**Vincolante**: un termine tradotto qui si riusa
ovunque», e sono 1.008 righe. Nessuno strumento del progetto lo legge: la
ricerca `grep -rn "glossario.md" --include=*.py` trova solo teste di lotto,
cioe' prosa scritta da chi traduceva a mano. Il glossario e' vincolante **per
chi se lo ricorda**.

Sul dizionario la dimenticanza ha un argine: ogni resa passa da un lotto, e la
testa del lotto cita il glossario. Le **toppe** no. Una toppa si scrive dentro
una sessione, in mezzo al codice, e l'italiano che porta non passa da nessun
lotto: sono 910 toppe con testo, ed e' l'italiano su cui il glossario non ha mai
avuto voce.

## Il criterio, e perche' non e' «cerca la parola»

Per ogni toppa si guarda l'inglese che **toglie** e l'italiano che **mette**
(la definizione di `_126-referti-toppe.py`, invariata apposta). Se nell'inglese
c'e' un termine del glossario e nell'italiano non c'e' nessuna delle sue rese,
la toppa e' da leggere.

⚠️⚠️ **Il confronto e' sullo stem, non sulla parola.** «Livello» compare come
«livelli», «Resistenza» come «resistente»: cercare la forma di dizionario nella
prosa italiana da' divergenze dove non ce ne sono. Si cerca il prefisso senza
l'ultima vocale, sul testo con gli accenti degradati.

⚠️⚠️ **E un termine con piu' rese non e' una divergenza.** `glossario.md` da'
`Body` tre volte — Torso, Corpo, corpo — perche' la resa dipende dal posto. Le
righe con lo stesso inglese si sommano: **basta che ci sia una** delle rese.

⚠️ Restano fuori i termini di **una lettera o due** e quelli che il glossario
rende **con se stessi** (Mana, Karma: sono in `invariati.md`, e cercarli
significa cercare l'inglese dentro l'italiano, che e' un altro referto).

## ⚠️⚠️⚠️ La regola che rende questo un filtro: il termine dev'essere MAIUSCOLO

La prima stesura non guardava come il termine e' scritto, e su 163 voci
giudicate ne bocciava **87**. Piu' della meta': non un filtro, l'elenco completo
con un passaggio in piu'. La causa sta tutta nel conto dei termini che
bocciavano (`_130-perche-il-filtro-passa.py`):

    will 35   items 8   skill 7   change 5   attack 3   report 2 ...

**`will` trentacinque volte, ed e' il futuro inglese.** «You **will** die
alone» non parla dell'attributo Volonta'. Lo stesso per `change`, `attack`,
`bow` («**Bow** down before me»), `body` («wash your **body**»): sono parole
comuni che il glossario nomina perche' **altrove** sono etichette.

⭐ La discriminante non e' la lunghezza del testo, e' la **maiuscola**. Un
termine di glossario e' un termine d'interfaccia; quando l'inglese lo scrive
maiuscolo **in mezzo a una frase** lo sta usando come termine, non come parola.
Misurate una accanto all'altra:

    restrizione                     contenevano  giudicate  divergenze
    nessuna                                 163        163          87
    solo inglese <= 40 caratteri             68         68          15
    solo termine maiuscolo                  163         46           6   <-
    maiuscolo + inglese <= 40                68         33           5

⚠️ Si sceglie la terza e non la quarta **anche se boccia una voce di piu'**: la
quarta lascia fuori meta' delle toppe **prima di guardarle**, per la lunghezza,
che col glossario non c'entra niente. La terza le apre tutte e 163 e ne trova 46
in cui un termine e' usato **come termine**. Un filtro si sceglie sul rapporto,
non sul totale.

## ⚠️⚠️ Questa taratura vale per le TOPPE, e sul dizionario NO

`--dizionario` gira la stessa rete sulle 26.326 rese: **1.239 giudicate, 458
divergenze**, cioe' il 37%. Non e' un difetto della rete, e' una differenza fra
i due insiemi: le toppe sono quasi tutte **etichette**, le rese sono quasi tutte
**prosa**, e in prosa una resa cambia parola per ritmo — `Darkness` -> «buio»
dove il glossario dice «oscurita'», ed e' giusto cosi'. Il numero e' stampato
qui perche' nessuno l'aveva mai preso, **non** perche' sia un cancello.

⚠️ «In mezzo a una frase» e' parte della regola: a inizio frase la maiuscola e'
della punteggiatura, non del termine.

## Il numero che conta

Accanto alle divergenze sta **quante toppe hanno davvero avuto un termine da
giudicare**: senza quel secondo numero uno zero non distingue «nessuna
divergenza» da «nessun caso».

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-glossario-nelle-toppe.py
    ... --dizionario   la stessa rete sulle 26.326 rese, il numero mai preso
"""
import io
import json
import re
import sys

from strumenti import percorsi
from strumenti.accenti import degrada

LETTERALE = re.compile(r'"(?:[^"\\]|\\.)*"')
RIGA = re.compile(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|")
# i pezzi di codice HSP che stanno dentro un letterale non sono prosa
CODICE = re.compile(r"\\[a-z]|%s\d|\bcnt\b")


def righe(valore) -> list:
    return list(valore) if isinstance(valore, list) else [valore]


def stem(parola: str) -> str:
    """La parte di una parola italiana che l'inflessione non tocca."""
    base = degrada(parola).lower()
    return base[:-1] if len(base) > 4 and base[-1] in "aeio" else base


def glossario() -> dict:
    """termine inglese (minuscolo) -> insieme degli stem delle sue rese."""
    fuori: dict = {}
    percorso = percorsi.PROGETTO / "glossario.md"
    for linea in io.open(percorso, encoding="utf-8"):
        m = RIGA.match(linea)
        if not m:
            continue
        en, it = m.group(1), m.group(2)
        if en in ("EN", "---") or set(en) <= set("-: "):
            continue
        # `Ally / Ally List`, `Resistance / Resist`: piu' termini in una riga
        for pezzo_en in en.split("/"):
            chiave = re.sub(r"\(.*?\)", "", pezzo_en).strip().lower()
            if len(chiave) < 3 or not re.match(r"^[a-z][a-z' -]*$", chiave):
                continue
            for pezzo_it in it.split("/"):
                reso = re.sub(r"\(.*?\)", "", pezzo_it).strip()
                reso = re.sub(r"[`*«».,]", "", reso).strip()
                if not reso or reso.lower() == chiave:
                    continue    # reso con se stesso: e' un invariato
                stems = tuple(stem(p) for p in reso.split() if len(p) > 2)
                if stems:
                    fuori.setdefault(chiave, set()).add(stems)
    return fuori


def usato_da_termine(termine: str, inglese: str) -> bool:
    """Il termine compare **maiuscolo e in mezzo a una frase**: e' un'etichetta.

    Vedi la testa del file: senza questa condizione `will` boccia trentacinque
    volte il futuro inglese, e il referto smette di essere un filtro.
    """
    for m in re.finditer(r"\b%s\b" % re.escape(termine), inglese, re.I):
        if not inglese[m.start()].isupper():
            continue
        prima = inglese[:m.start()].rstrip()
        if not prima or prima[-1] in ".!?":
            continue    # a inizio frase la maiuscola e' della punteggiatura
        return True
    return False


def coppie_delle_toppe():
    """(nome, inglese tolto, italiano messo) per ogni toppa con testo."""
    percorso = percorsi.PROGETTO / "toppe.jsonl"
    for linea in io.open(percorso, encoding="utf-8"):
        if not linea.strip():
            continue
        toppa = json.loads(linea)
        vecchi, nuovi = [], []
        letterali_nuovi = set()
        for r in righe(toppa["sostituisci"]):
            for x in LETTERALE.findall(r):
                letterali_nuovi.add(x)
                nuovi.append(x[1:-1])
        for r in righe(toppa["cerca"]):
            for x in LETTERALE.findall(r):
                if x not in letterali_nuovi:
                    vecchi.append(x[1:-1])
        aggiunti = [x[1:-1] for r in righe(toppa["sostituisci"])
                    for x in LETTERALE.findall(r)
                    if x not in {y for rr in righe(toppa["cerca"])
                                 for y in LETTERALE.findall(rr)}]
        if aggiunti:
            yield toppa["file"], " ".join(vecchi), " ".join(aggiunti)


def coppie_del_dizionario():
    for percorso in sorted(percorsi.DIZIONARIO.glob("*.jsonl")):
        nome = percorso.name[: -len(".jsonl")]
        for linea in io.open(percorso, encoding="utf-8"):
            if not linea.strip():
                continue
            voce = json.loads(linea)
            en, it = voce.get("en") or "", voce.get("it") or ""
            if en and it:
                yield "%s:%s" % (nome, voce["riga"]), en, it


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    sul_dizionario = "--dizionario" in argv
    termini = glossario()

    coppie = coppie_del_dizionario() if sul_dizionario else coppie_delle_toppe()
    giudicati = 0
    divergenze = []
    quante_volte: dict = {}
    for dove, inglese, italiano in coppie:
        if CODICE.search(italiano):
            pass    # il codice dentro il letterale non toglie la prosa intorno
        basso = inglese.lower()
        italiano_stem = degrada(italiano).lower()
        trovati = [t for t in termini if usato_da_termine(t, inglese)]
        if not trovati:
            continue
        giudicati += 1
        for termine in trovati:
            quante_volte[termine] = quante_volte.get(termine, 0) + 1
            va_bene = any(all(s in italiano_stem for s in stems)
                          for stems in termini[termine])
            if not va_bene:
                rese = sorted(" ".join(s) for s in termini[termine])
                divergenze.append((dove, termine, rese, inglese, italiano))

    for dove, termine, rese, inglese, italiano in divergenze:
        print("DIVERGENZA  %-22s «%s» -> %s" % (dove, termine, " | ".join(rese)))
        print("            en: %s" % inglese[:110])
        print("            it: %s" % italiano[:110])
    print()
    print("termini di glossario caricati        : %d" % len(termini))
    print("%-36s : %d" % ("voci con un termine da giudicare",
                          giudicati))
    print("divergenze                           : %d" % len(divergenze))
    if quante_volte:
        piu_visti = sorted(quante_volte.items(), key=lambda x: -x[1])[:8]
        print("i termini che hanno giudicato di piu': %s"
              % ", ".join("%s %d" % (t, n) for t, n in piu_visti))
    return 1 if divergenze else 0


if __name__ == "__main__":
    sys.exit(main())
