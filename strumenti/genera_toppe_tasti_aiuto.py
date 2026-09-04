# strumenti/genera_toppe_tasti_aiuto.py
"""Le 38 etichette dei tasti nella schermata di aiuto (F1).

`help.hsp:387-:440` riempie l'array `s` con sette righe fatte cosi':

    s = "アイテムを取る(get)", key_get, "アイテムを置く(drop)", key_drop, ...

cioe' una descrizione giapponese con **il nome inglese del comando fra
parentesi**, alternata alla lettera del tasto. `*convertHelp` (`help.hsp:284`)
in inglese butta via il giapponese e tiene **solo quel che sta fra le
parentesi**, passandolo per `cnven`:

    s(cnt) = cnven(strmid(s(cnt), instr(s(cnt), 0, "(") + 1, ...))

⚠️⚠️ **Quindi l'etichetta che il giocatore inglese legge sta dentro le
parentesi, e le trentotto erano rimaste inglesi.** La schermata di aiuto e' il
posto dove si va per imparare i comandi, e diceva «Get», «Quaff», «Zap».

## Perche' nessuno le contava

E' lo stesso punto cieco della riga di stato dell'editor di mazzo, e per gli
stessi due motivi. `copertura._PROSA` pretende due parole alfabetiche e ne
vedeva **una sola** su 38 — «Wide apply» — perche' tutte le altre sono una
parola dentro una stringa giapponese. `disegnate.py` non ne vedeva nessuna: il
valore finisce in `s(cnt)`, viene riscritto da `*convertHelp` in un altro
sottoprogramma e disegnato da `mes s(cnt * 2)` venti righe piu' giu'. E' il
**secondo salto**, e questo e' il suo secondo conto: 8 stringhe nell'editor di
mazzo, 38 qui.

## Il tetto, misurato e non stimato

    help.hsp:393   pos x + 38 + cnt / 6 * 290, ...     l'etichetta parte a 38
    help.hsp:396   pos x + 248 + cnt / 6 * 290, ...    il tasto sta a 248
    help.hsp:392   font ..., 13 - en * 2               corpo 11 (en == 1)

`Courier New` monospaziato fa 6,6 px a corpo 11, e fra l'etichetta e il tasto
ci sono 210 px:

    (248 - 38) / 6,6 = 31,8  ->  TETTO 31 CARATTERI

Le colonne distano 290 px, quindi 31 caratteri non invadono nemmeno la colonna
accanto. La resa piu' lunga ne fa 10.

## Da dove vengono le parole

⭐ **Ventidue delle trentotto non si decidono qui.** La barra dei comandi in
cima a questo stesso file (`help.hsp:16-:58`) e' gia' tradotta dal dizionario, e
il generatore legge di li': `Pick Up` -> «Raccogli», `Zap` -> «Agita»,
`W Skill` -> «Ab. ampia». Se la schermata di aiuto chiamasse un comando con una
parola e la barra con un'altra, il giocatore imparerebbe il nome sbagliato.

Le sedici che il dizionario non copre sono l'unica decisione nuova, e sono
segnate una per una in `NUOVE`.

⚠️ **Gli accenti si degradano qui.** Queste sono toppe, non voci di dizionario:
scrivono direttamente nel file CP932, dove la vocale accentata non esiste, e
nessuno le fa passare da `accenti.degrada` per conto suo. Lo fa questo file, su
tutt'e due le tabelle: cosi' `NUOVE` puo' portare l'italiano giusto e la build
riceve «Abilita'». ⚠️ E `degrada` conosce **le sole vocali accentate**: un
trattino lungo o una virgoletta a caporale passerebbero, e per quelli c'e' il
cancello sull'ASCII.
"""
from __future__ import annotations

import json
import re

from strumenti import accenti, percorsi

TETTO = 31

# Le sette righe che riempiono `s` con «descrizione(comando)», e la riga
# `pos`/`font` da cui il tetto viene.
RIGHE = (387, 388, 408, 409, 429, 430, 440)
GEOMETRIA = [
    ("help.hsp", 393, "pos x + 38 + cnt / 6 * 290, y + 58 + cnt \\ 6 * 14",
     "dove parte l'etichetta"),
    ("help.hsp", 396, "pos x + 248 + cnt / 6 * 290, y + 57 + cnt \\ 6 * 14",
     "dove sta il tasto"),
    ("help.hsp", 392, "font lang(cfg_font1, cfg_font2), 13 - en * 2, 0",
     "il corpo"),
]

# ⭐ Comando inglese -> voce del dizionario di `help.hsp` da cui prendere la
#    parola. Non e' una traduzione: e' un rinvio, e serve perche' la schermata
#    di aiuto e la barra dei comandi dicano la stessa parola.
DAL_DIZIONARIO = {
    "get": "Pick Up",
    "drop": "Drop",
    "examine": "Examine",
    "itemstack": "Stack",
    "eat": "Eat",
    "read": "Read",
    "zap": "Zap",
    "tool": "Tool",
    "throw": "Throw",
    "ammo": "Ammo",
    "wear,wield": "Wear",
    "fire": "Fire",
    "apply": "Skill",
    "Wide apply": "W Skill",
    "bash": "Bash",
    "dig": "Dig",
    "interact": "Interact",
    "chara": "Chara",
    "journal": "Journal",
    "help": "Help",
    "log": "Log",
    "pray": "Pray",
}

# ⚠️ Le sedici che il dizionario non copre: l'unica decisione nuova di questo
#    file, presa il 2026-09-05.
NUOVE = {
    # 飲む: bere una pozione. La barra dei comandi non ha questa voce.
    "quaff": "Bevi",
    # 魔法を唱える. «Lancia» e' gia' `throw`, e due comandi non possono
    # chiamarsi uguale in una schermata che serve a distinguerli: si tiene
    # «Magia», la parola con cui la barra rende `Spell` («Magie»).
    "cast": "Magia",
    # 調合: `text.hsp:137` rende `blend` «sintesi».
    "blend": "Sintesi",
    # 周囲を調べる: `txtadv.hsp:438` rende `search` «Esplora».
    "search": "Esplora",
    "go down": "Scendi",
    "go up": "Sali",
    "wait": "Attendi",
    # 鍵を開ける: `text.hsp:135` rende `open` «Apri».
    "open": "Apri",
    # ターゲットを指定: la barra dei comandi non ha questa voce; `text.hsp:135`
    # rende `target` «Bersaglio», ed e' lo stesso menu di `open` e `offer`.
    "target": "Bersaglio",
    # マテリアル表示: `material.hsp` rende `material` «Materie».
    "material": "Materie",
    "feat": "Tratti",
    "save": "Salva",
    "close": "Chiudi",
    "give": "Dai",
    "offer": "Offri",
    "hi jump": "Salto alto",
}

_LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')
_COMANDO = re.compile(r"^(.*)\(([^()]+)\)$")

GENERATA = "tasti-aiuto"


class MonteMosso(Exception):
    """Il sorgente pinnato non ha piu' la forma su cui questo file si regge."""


def _righe_file(nome: str) -> list[str]:
    testo = (percorsi.SORGENTE_HSP / nome).read_bytes().decode("cp932")
    return [r.rstrip("\r") for r in testo.split("\n")]


def dal_dizionario() -> dict[str, str]:
    """Le rese gia' decise della barra dei comandi, lette invece che riscritte."""
    percorso = percorsi.PROGETTO / "dizionario" / "help.hsp.jsonl"
    per_inglese: dict[str, str] = {}
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        voce = json.loads(riga)
        if voce.get("it") and voce["riga"] < 80:
            per_inglese.setdefault(voce["en"], voce["it"])
    fuori = {}
    for comando, voce in DAL_DIZIONARIO.items():
        if voce not in per_inglese:
            raise KeyError(
                "il comando %r rinviava alla voce %r della barra dei comandi, "
                "e nel dizionario di help.hsp quella voce non c'e' piu'. Il "
                "rinvio esiste perche' le due schermate dicano la stessa "
                "parola: se la voce se n'e' andata, la parola va ridecisa, "
                "non indovinata." % (comando, voce))
        fuori[comando] = accenti.degrada(per_inglese[voce])
    return fuori


def rese() -> dict[str, str]:
    """Comando inglese -> etichetta italiana, per tutti e trentotto."""
    fuori = dict(dal_dizionario())
    doppi = set(fuori) & set(NUOVE)
    if doppi:
        raise KeyError(
            "%r stanno sia in DAL_DIZIONARIO sia in NUOVE: una parola con due "
            "sorgenti e' una parola che cambia a seconda di chi la legge."
            % sorted(doppi))
    fuori.update({k: accenti.degrada(v) for k, v in NUOVE.items()})
    return fuori


def comandi_sorgente() -> list[tuple[int, str, str]]:
    """(numero, letterale intero, comando fra parentesi) delle sette righe."""
    righe = _righe_file("help.hsp")
    fuori = []
    for numero in RIGHE:
        riga = righe[numero - 1]
        if not re.match(r"^\t\ts(\(\d+\))? = ", riga):
            raise MonteMosso(
                "help.hsp:%d doveva riempire l'array `s` e dice %r: il blocco "
                "dei tasti si e' mosso, e i numeri di riga qui vanno rifatti "
                "guardando." % (numero, riga.strip()[:60]))
        for pezzo in _LETTERALE.findall(riga):
            trovato = _COMANDO.match(pezzo)
            if trovato:
                fuori.append((numero, pezzo, trovato.group(2)))
    return fuori


def _controlla_geometria() -> None:
    for nome, numero, atteso, che_cosa in GEOMETRIA:
        riga = _righe_file(nome)[numero - 1]
        if riga.strip() != atteso:
            raise MonteMosso(
                "%s:%d dichiarava %s con %r e ora dice %r. Il tetto di %d "
                "caratteri veniva da li': va rifatta la misura."
                % (nome, numero, che_cosa, atteso, riga.strip(), TETTO))


def problemi() -> list[str]:
    """Vuoto = nessuna resa manca, sfora o e' impossibile da scrivere."""
    guai = []
    try:
        tabella = rese()
    except KeyError as errore:
        return [str(errore)]
    for numero, _pezzo, comando in comandi_sorgente():
        if comando not in tabella:
            guai.append(
                "help.hsp:%d chiama il comando %r e nessuno gli ha dato una "
                "parola italiana: o il monte ha aggiunto un tasto, o la "
                "tabella e' incompleta." % (numero, comando))
    usati = {c for _n, _p, c in comandi_sorgente()}
    for comando in sorted(set(tabella) - usati):
        guai.append(
            "%r ha una resa e nella schermata di aiuto non compare piu': una "
            "riga di tabella che non serve a niente invecchia in silenzio."
            % comando)
    for comando, italiano in tabella.items():
        if len(italiano) > TETTO:
            guai.append("%r -> %r: %d caratteri, il tetto e' %d e oltre "
                        "quello l'etichetta finisce sotto il tasto"
                        % (comando, italiano, len(italiano), TETTO))
        if not italiano.isascii():
            guai.append(
                "%r -> %r: non e' ASCII. Queste sono toppe, non voci di "
                "dizionario: scrivono nel file CP932 e nessuno le degrada "
                "piu'. Va scritto con l'apostrofo." % (comando, italiano))
        if "(" in italiano or ")" in italiano:
            guai.append(
                "%r -> %r: `*convertHelp` taglia sulla PRIMA parentesi, e una "
                "parentesi dentro la resa gli farebbe tagliare il pezzo "
                "sbagliato." % (comando, italiano))
    return guai


def toppe() -> list[dict]:
    _controlla_geometria()
    tabella = rese()
    righe = _righe_file("help.hsp")
    fuori = []
    for numero in RIGHE:
        riga = righe[numero - 1]

        def sostituisci(trovato: re.Match) -> str:
            pezzo = trovato.group(1)
            comando = _COMANDO.match(pezzo)
            if not comando:
                return trovato.group(0)
            return '"%s(%s)"' % (comando.group(1), tabella[comando.group(2)])

        nuova = _LETTERALE.sub(sostituisci, riga)
        if nuova == riga:
            continue
        fuori.append({
            "file": "help.hsp",
            "cerca": riga,
            "sostituisci": nuova,
            "motivo": (
                "Le etichette dei tasti nella schermata di aiuto, riga %d di "
                "7 (help.hsp:%d). ⚠️⚠️ Quel che il giocatore inglese legge sta "
                "DENTRO le parentesi: `*convertHelp` (:284) butta via il "
                "giapponese e tiene solo `strmid` fra la prima `(` e la prima "
                "`)`, passandolo per `cnven`. Le 38 etichette erano rimaste "
                "inglesi nel posto dove si va a imparare i comandi. "
                "⚠️ Non le contava nessuna delle due reti: `copertura._PROSA` "
                "pretende due parole alfabetiche e ne vedeva UNA su 38 («Wide "
                "apply»), e `disegnate.py` nessuna, perche' il valore finisce "
                "in `s(cnt)`, lo riscrive un altro sottoprogramma e lo "
                "disegna `mes s(cnt * 2)` venti righe piu' giu' — e' il "
                "SECONDO SALTO. ⚠️ Tetto %d caratteri, misurato: etichetta a "
                "`x + 38` (:393), tasto a `x + 248` (:396), `Courier New` a "
                "corpo 11 (:392), 6,6 px per carattere; le colonne distano "
                "290, quindi 31 non invade la colonna accanto. ⭐ 22 parole su "
                "38 non si decidono qui: il generatore le legge dalla barra "
                "dei comandi di questo stesso file (help.hsp:16-:58, gia' nel "
                "dizionario), o la schermata di aiuto chiamerebbe un comando "
                "con una parola e la barra con un'altra. ⚠️ Gli accenti sono "
                "degradati qui dentro: una toppa scrive nel CP932 e non passa "
                "piu' da `accenti.degrada`. "
                "Generata da `strumenti/genera_toppe_tasti_aiuto.py`."
                % (len(fuori) + 1, numero, TETTO)),
            "generata": GENERATA,
        })
    return fuori


def scrivi() -> int:
    mie = toppe()
    righe = _righe_file("help.hsp")
    for toppa in mie:
        quante = righe.count(toppa["cerca"])
        if quante != 1:
            raise SystemExit(
                "la riga da cercare compare %d volte, non una: %r"
                % (quante, toppa["cerca"][:70]))
    percorso = percorsi.PROGETTO / "toppe.jsonl"
    esistenti = [json.loads(r) for r in
                 percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    altre = [t for t in esistenti if t.get("generata") != GENERATA]
    with percorso.open("w", encoding="utf-8", newline="\n") as f:
        for toppa in altre + mie:
            f.write(json.dumps(toppa, ensure_ascii=False) + "\n")
    print("  toppe a mano o d'altri generatori: %d, generate qui: %d "
          "(ne sostituiscono %d)"
          % (len(altre), len(mie), len(esistenti) - len(altre)))
    return len(mie)


def main() -> None:
    import argparse
    analizzatore = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizzatore.add_argument("--scrivi", action="store_true",
                              help="riscrive le toppe generate in toppe.jsonl")
    argomenti = analizzatore.parse_args()

    _controlla_geometria()
    guai = problemi()
    comandi = comandi_sorgente()
    print("  etichette nella schermata : %d su %d righe"
          % (len(comandi), len(RIGHE)))
    if not guai:
        tabella = rese()
        print("  lette dal dizionario      : %d" % len(DAL_DIZIONARIO))
        print("  decise qui                : %d" % len(NUOVE))
        piu_lunga = max(tabella.values(), key=len)
        print("  la piu' lunga             : %r, %d caratteri (tetto %d)"
              % (piu_lunga, len(piu_lunga), TETTO))
        print("  righe toppate             : %d" % len(toppe()))
    for guaio in guai:
        print("  ⚠️", guaio)
    if argomenti.scrivi and not guai:
        scrivi()
    print("\n  " + ("genera_toppe_tasti_aiuto: ogni tasto ha la sua parola, e "
                    "nessuna sfora" if not guai
                    else "genera_toppe_tasti_aiuto: %d guai" % len(guai)))
    raise SystemExit(1 if guai else 0)


if __name__ == "__main__":
    main()
