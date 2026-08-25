"""Il SESTO punto cieco: le tabelle di stringhe inglesi nude.

    AITextData(0, 1) = "Not Set", "Self", "Target", "Ally", "Player", "Enemy", "NULL"

Una riga sola, sette parole che il giocatore legge in una colonna. `nudi_en.py`
cerca le righe che DISEGNANO (`mes`, `display_topic`, `cs_list`…) e quelle che
compongono una variabile che verra' disegnata: questa non e' ne' l'una ne'
l'altra. E' un'assegnazione di array, e il testo arriva a schermo molto piu'
tardi, per indice, da una riga che di letterali non ne ha nessuno
(`s = AITextData(CAIComparator(cnt, tc), 2)`).

Trovato nella 52a aprendo `custom_ai.hsp`: la schermata delle istruzioni tattiche
ha cinque colonne, e tradurne le intestazioni senza queste righe avrebbe lasciato
la tabella sotto in inglese — lo stesso difetto delle «due letterali per riga»
della 51a, in forma nuova.

⚠️ Come `triage_nudi.py`, questo NON scarta per euristica: elenca tutto e
classifica, perche' un filtro che si prova sul totale invece che su una riga
vista a schermo e' l'errore di `_PERCORSO`, gia' ripetuto cinque volte.

    numerica   ogni letterale e' un numero: sono valori, non testo ("10", "20")
    sigla      token corti senza spazi ne' minuscole di parola: "<", ">=", "NULL"
    jp         porta del giapponese: o e' la coppia (jp, en) scelta per indice
               di lingua, o e' il ramo giapponese di una guida. Fuori perimetro
    testo      tutto il resto: da guardare

⭐ **Atteso al 2026-08-16 (52a): testo 7 tabelle e 73 voci, tutte in
`custom_ai.hsp`, e delle sette 6 FATTE, 1 DECISA, 0 da fare** — piu' sigla 2/6,
numerica 2/22, jp 58/143. Il punto cieco e' circoscritto a un file solo — le
cinque colonne della schermata delle istruzioni tattiche piu' i 21 nomi di stato
di `AIStatusNames` — ed e' stato chiuso nella sessione stessa in cui e' nato.
⚠️ Se «testo» sale, un file nuovo ha una tabella; se scende senza che nessuno
abbia tradotto, il filtro si e' rotto. Se «DA FARE» sale sopra 0, o e' arrivata
una tabella nuova o `applica` non ha girato.
💡 «fatta» si misura confrontando la riga del SORGENTE con quella della BUILD:
una tabella non ha firma ne' voce di dizionario, quindi non c'e' nient'altro da
guardare — e per lo stesso motivo la tabella che non si tocca non poteva finire
in `rinviate.jsonl`, che indicizza per firma. Sta in `DECISE`, qui sotto.
💡 Le 58 «jp» sono quasi tutte i messaggi d'errore del runtime HSP (41 in
`init.hsp`, il resto altrove): il giocatore le legge solo se il gioco va in
errore, e sono di monte.

Uso:
    python scratchpad/tabelle_en.py            tutto il sorgente
    python scratchpad/tabelle_en.py custom_ai  un file solo
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti import percorsi  # noqa: E402

# `nome(indici) = "…"` con almeno una virgola e un altro letterale dopo.
# L'indice e' obbligatorio: senza, la riga e' una variabile semplice e la
# guarda gia' `variabili_en.py`.
ASSEGNA = re.compile(r'^\s*(\w+)\s*\(([^)]*)\)\s*=\s*(".*)$')
LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')
# ⚠️ `traitrefn(0) = lang("…", "…"), lang("…", "…")` ha la stessa forma ma NON e'
# un punto cieco: quei letterali hanno firma e stanno nel dizionario. Si tolgono
# prima di guardare, altrimenti il referto conta 159 tabelle invece di quelle
# vere — e un regex non basta, perche' dentro una `lang()` di `trait.hsp` ci
# sono parentesi annidate: `lang("…[魅力" + x + "]", "…")`. Si contano a mano.
def senza_lang(coda: str) -> str:
    """Toglie le chiamate `lang(...)` complete, parentesi annidate comprese."""
    fuori, i = [], 0
    while i < len(coda):
        m = re.compile(r"lang\s*\(").match(coda, i)
        if not m:
            if coda[i] == '"':  # una stringa puo' contenere parentesi: si salta intera
                fine = re.compile(r'"(?:[^"\\]|\\.)*"').match(coda, i)
                if fine:
                    fuori.append(fine.group(0))
                    i = fine.end()
                    continue
            fuori.append(coda[i])
            i += 1
            continue
        profondita, j = 1, m.end()
        while j < len(coda) and profondita:
            if coda[j] == '"':
                fine = re.compile(r'"(?:[^"\\]|\\.)*"').match(coda, j)
                j = fine.end() if fine else j + 1
                continue
            profondita += (coda[j] == "(") - (coda[j] == ")")
            j += 1
        i = j
    return "".join(fuori)


def concatenata(coda: str) -> bool:
    """C'e' un `+` fuori dalle stringhe? Allora e' una riga che COMPONE.

    ⚠️ Quelle non sono il punto cieco: `nudi_en.py` le vede gia', perche' il
    letterale sta accanto all'espressione che finisce a schermo
    (`listn(0, 2) = "Modify Comparator. (Current: " + AITextData(…) + ")"`).
    Il punto cieco e' la tabella PURA, dove i letterali sono solo separati da
    virgole e nessuno di loro tocca mai una riga che disegna.
    """
    fuori = re.sub(r'"(?:[^"\\]|\\.)*"', "", coda)
    return "+" in fuori


def classifica(valori: list[str]) -> str:
    vivi = [v for v in valori if v != "NULL"]
    if not vivi:
        return "sigla"
    # ⚠️ Una tabella che porta del giapponese non e' un letterale inglese nudo:
    # o e' la coppia (jp, en) scelta per indice di lingua — i 41 `ErrorMsg` del
    # runtime HSP in `init.hsp`, che il giocatore legge solo se il gioco va in
    # errore — o e' il ramo giapponese di una guida (`help.hsp`). Fuori dal
    # perimetro in tutt'e due i casi, ma si contano invece di sparire.
    if any(ord(c) > 0x7F for v in vivi for c in v):
        return "jp"
    if all(re.fullmatch(r"-?\d+(\.\d+)?%?", v) for v in vivi):
        return "numerica"
    if all(len(v) <= 3 or not re.search(r"[a-z]{2}", v) for v in vivi):
        return "sigla"
    return "testo"


def tabelle(testo: str) -> list[tuple[int, str, list[str], str]]:
    fuori = []
    for n, riga in enumerate(testo.split("\n"), 1):
        spoglia = riga.strip()
        if spoglia.startswith(";") or spoglia.startswith("//"):
            continue
        m = ASSEGNA.match(riga)
        if not m:
            continue
        coda = senza_lang(m.group(3))
        valori = LETTERALE.findall(coda)
        if len(valori) < 2 or concatenata(coda):
            continue
        fuori.append((n, m.group(1), valori, classifica(valori)))
    return fuori


# ⚠️ Le tabelle che NON si traducono, con il perche' misurato. Non sono lavoro
# che resta: sono lavoro che non si fa, e un referto che continuasse a contarle
# fra le «da fare» mentirebbe a ogni apertura.
DECISE = {
    ("custom_ai.hsp", 30): (
        "le dodici classi: `custom_ai.hsp:493` e `:508` le CONFRONTANO con "
        "`cdatan(CDATAN_CLASS, …)`, che porta la chiave inglese — la scrivono "
        "`action.hsp:13670`-`:13703` e `command.hsp:4591`-`:4626`, la rileggono "
        "`chara.hsp:2875`-`:2962`, `ai.hsp:2546`, `calculation.hsp:888`. "
        "Tradurla lascerebbe l'IA senza nessuna classe da riconoscere (52a)"
    ),
}


def main(argv: list[str]) -> None:
    solo = argv[0].replace(".hsp", "") if argv else None
    radice = percorsi.SORGENTE_HSP
    conta = {"testo": 0, "sigla": 0, "numerica": 0, "jp": 0}
    voci = {"testo": 0, "sigla": 0, "numerica": 0, "jp": 0}
    fatte = decise = da_fare = 0

    for percorso in sorted(radice.glob("*.hsp")):
        if solo and percorso.stem != solo:
            continue
        testo = percorso.read_bytes().decode("cp932", errors="replace")
        trovate = tabelle(testo)
        if not trovate:
            continue
        # La stessa tabella nella BUILD: se e' cambiata, e' gia' resa.
        #
        # ⚠️⚠️ **NON «la stessa RIGA»: la build la muoviamo noi.** Fino alla 98a
        # qui si confrontava `righe_build[n-1]` con `righe_src[n-1]`, cioe' lo
        # stesso indice nei due alberi. Regge finche' ogni toppa sostituisce una
        # riga con una riga — e per 1.023 toppe e' stato cosi'. Le toppe dei
        # **file dati** no: ne mettono sette al posto di una, e quella di
        # `book.txt` ha spostato in giu' di 6 tutto `command.hsp` sotto :8371.
        # Da li' in giu' il confronto avrebbe letto una riga per un'altra, che
        # quasi sempre e' diversa: ogni tabella sotto quel punto sarebbe stata
        # dichiarata **«fatta»** senza che nessuno l'avesse tradotta.
        # 💡 Oggi non e' successo per fortuna, non per costruzione: le sette
        # tabelle di testo stanno tutte in `custom_ai.hsp:22-31`, un file che
        # nessuna toppa dei file dati tocca. Un referto che dice la verita' per
        # dove capita di guardare non e' un referto che dice la verita'.
        #
        # L'appaiamento giusto e' per **nome della tabella e ordinale**: una
        # toppa sposta le righe, non ribattezza le tabelle ne' ne cambia
        # l'ordine. `AITextData` compare cinque volte in `custom_ai.hsp` ed e'
        # per questo che il nome da solo non basta.
        costruito = percorsi.BUILD_HSP / percorso.name
        def _per_nome(elenco):
            visti, uscita = {}, {}
            for voce in elenco:
                nome_tabella = voce[1]
                visti[nome_tabella] = visti.get(nome_tabella, -1) + 1
                uscita[(nome_tabella, visti[nome_tabella])] = voce
            return uscita
        mie = _per_nome(trovate)
        indice = {id(v): k for k, v in mie.items()}
        di_monte = _per_nome(tabelle(
            costruito.read_bytes().decode("cp932", errors="replace")
        )) if costruito.exists() else {}

        da_dire = [t for t in trovate if t[3] == "testo"]
        print(f"=== {percorso.name}: {len(trovate)} tabelle, {len(da_dire)} di testo")
        for tabella in trovate:
            n, nome, valori, classe = tabella
            conta[classe] += 1
            voci[classe] += len([v for v in valori if v != "NULL"])
            if classe != "testo":
                continue
            costruita = di_monte.get(indice[id(tabella)])
            stato = "da fare"
            if (percorso.name, n) in DECISE:
                stato, decise = "decisa", decise + 1
            elif costruita is not None and costruita[2] != valori:
                stato, fatte = "fatta", fatte + 1
            else:
                da_fare += 1
            mostra = ", ".join(valori[:14]) + (" …" if len(valori) > 14 else "")
            print(f"  {n:>6} | {nome:<16} {len(valori):>3} voci | {stato:<7} | {mostra[:120]}")
            if stato == "decisa":
                print(f"         ↳ {DECISE[(percorso.name, n)]}")
        print()

    print(f"--- di testo: {fatte} fatte, {decise} decise (non si toccano), "
          f"{da_fare} DA FARE")
    print(f"--- tabelle: testo {conta['testo']}, sigla {conta['sigla']}, "
          f"numerica {conta['numerica']}, jp {conta['jp']}")
    print(f"--- voci   : testo {voci['testo']}, sigla {voci['sigla']}, "
          f"numerica {voci['numerica']}, jp {voci['jp']}")


if __name__ == "__main__":
    main(sys.argv[1:])
