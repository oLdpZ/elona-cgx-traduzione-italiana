# strumenti/genera_toppe_tag_equip.py
"""Le 15 sigle delle abilita' nel pannello dell'equipaggiamento.

`item_func.hsp:2592-:2651` (`*equipinfo_mmah`, ramo `showresist == 3`) disegna
in fila i potenziamenti dell'oggetto equipaggiato, uno per abilita':

    locvar_equipinfo_s = skillname(locvar_colorres_i)   :2601
    if ( strlen(locvar_equipinfo_s) > 4 ) {             :2605
        ... quindici `if` che sostituiscono una sigla   :2612-:2626
        if ( strlen(locvar_equipinfo_s) > 4 ) {
            locvar_equipinfo_s = strmid(..., 0, 4)      :2629  ⚠️ TAGLIO SECCO
        }
    }
    locvar_equipinfo_s = locvar_equipinfo_s + ":" + ... :2645
    mes locvar_equipinfo_s                              :2650

⚠️⚠️ **Il nome dell'abilita' arriva qui gia' in italiano** — `skillname()` e'
tradotto dal dizionario — **e le quindici sigle no**: un giocatore italiano che
guarda un anello leggeva `Lett`? No: leggeva **`Read`**, `Hv-A`, `2Hnd`. Le
sigle sono scritte a mano nel ramo `else` di `if ( jp )`, cioe' fuori da
`lang()`, e nessuna rete del progetto le vedeva.

## Perche' nessuno le contava

`copertura._PROSA` pretende due parole alfabetiche: `2Hnd` non ne ha nemmeno
una. `disegnate.py` parte da chi disegna e segue la variabile, ma `s` — qui
`locvar_equipinfo_s` — riceve il valore **dentro un `if` a graffe sulla stessa
riga**, e la sua `_ASSEGNAZIONE` e' ancorata a inizio riga. Le ha trovate
`strumenti/salti.py` (141a), ed erano il fronte piu' grosso dei sette che ha
aperto.

## Il tetto: 4 caratteri, e non e' una stima

⭐ Non e' geometria e non e' una misura in pixel: e' un **taglio nel codice**.
`item_func.hsp:2629` fa `strmid(locvar_equipinfo_s, 0, 4)` su tutto quel che
resta piu' lungo di quattro. Una sigla di cinque caratteri non sborda dal
pannello: viene **tagliata**, e il giocatore legge un troncone.

⚠️ E l'altro verso vale allo stesso modo: `locvar_equipinfo_x += strlen(s) * 8`
(`:2651`) fa avanzare la fila **in proporzione alla lunghezza**. Sigle di
esattamente quattro caratteri, come le inglesi, lasciano la geometria della
riga identica a com'era.

## Da dove vengono le sigle

⭐ **Nessuna e' inventata: ognuna abbrevia il nome italiano dell'abilita'** che
il giocatore legge nella lista delle abilita' e nelle descrizioni. Il rinvio e'
un cancello, non un commento: `problemi()` rilegge `dizionario/skill.hsp.jsonl`
e si accende se il nome da cui una sigla e' stata ricavata non c'e' piu'. Se
`Greater Evasion` smettesse di essere «Intuito», `Intu` andrebbe ridecisa e non
indovinata — e' la stessa regola con cui la 140a ha legato le etichette di F1
alla barra dei comandi.

⚠️ **Lo schema segue quello inglese**, perche' la fila e' la stessa e il
giocatore la legge di colpo: nome di **una parola** -> le prime quattro lettere
(`Lettura` -> `Lett`, come `Mining` -> `Mine`); nome di **due parole** ->
iniziale, trattino, due lettere (`Sollevamento pesi` -> `S-Pe`, come
`Weight Lifting` -> `Wt-L`).

⚠️ Gli accenti si degradano qui, come in ogni generatore di toppe: una toppa
scrive dritta nel file CP932 e non passa piu' da `accenti.degrada`. Nessuna
delle quindici ne ha, e il cancello sull'ASCII lo verifica lo stesso.
"""
from __future__ import annotations

import json
import re

from strumenti import accenti, percorsi

TETTO = 4

# La riga del sorgente che impone il tetto, e quella che fa avanzare la fila.
GEOMETRIA = [
    ("item_func.hsp", 2629,
     "locvar_equipinfo_s = strmid(locvar_equipinfo_s, 0, 4)",
     "il taglio secco a quattro caratteri"),
    ("item_func.hsp", 2651,
     "locvar_equipinfo_x += strlen(locvar_equipinfo_s) * 8",
     "l'avanzamento della fila, in proporzione alla lunghezza"),
]

# costante dell'abilita' -> (riga, sigla inglese, nome italiano da cui la sigla
# viene, sigla italiana). ⚠️ Il **nome italiano** non e' un commento: e' il
# rinvio che `problemi()` rilegge nel dizionario.
SIGLE: dict[str, tuple[int, str, str, str]] = {
    # una parola -> le prime quattro lettere, come `Mining` -> `Mine`
    "SKILL_NORMAL_LITERACY":       (2612, "Read", "Lettura", "Lett"),
    "SKILL_NORMAL_MINING":         (2614, "Mine", "Scavo", "Scav"),
    "SKILL_NORMAL_SHIELD":         (2618, "Shld", "Scudo", "Scud"),
    "SKILL_NORMAL_HEAVY_ARMOR":    (2619, "Hv-A", "Corazza", "Cora"),
    "SKILL_NORMAL_MEDIUM_ARMOR":   (2620, "Md-A", "Maglia", "Magl"),
    "SKILL_NORMAL_LIGHT_ARMOR":    (2621, "Li-A", "Farsetto", "Fars"),
    "SKILL_NORMAL_GREATER_EVASION": (2625, "G-Ev", "Intuito", "Intu"),
    # ⭐ «trappole» e' italiano quanto `trap`: la sigla regge in tutt'e due le
    #    lingue, e cambiarla non aggiungerebbe niente al giocatore.
    "SKILL_NORMAL_DISARM_TRAP":    (2623, "Trap", "Disarmo trappole", "Trap"),
    # due parole -> iniziale, trattino, due lettere, come `Wt-L`
    "SKILL_NORMAL_WEIGHT_LIFTING": (2613, "Wt-L", "Sollevamento pesi", "S-Pe"),
    "SKILL_NORMAL_MAGIC_CAPACITY": (2615, "M-Cp", "Capacita' magica", "C-Mg"),
    "SKILL_NORMAL_DUAL_WIELD":     (2616, "D-Wd", "Doppia arma", "D-Ar"),
    "SKILL_NORMAL_MAGIC_DEVICE":   (2622, "M-Dv", "Dispositivi magici", "D-Mg"),
    "SKILL_NORMAL_EYE_OF_MIND":    (2624, "EoMn", "Occhio della mente", "O-Me"),
    # ⭐ `2Hnd` conta il numero e non la lettera, e in italiano regge uguale:
    #    «Due mani» -> `2Man`. E' l'unica delle quindici che copia la FORMA
    #    della sigla inglese invece dello schema.
    "SKILL_NORMAL_TWO_HAND":       (2617, "2Hnd", "Due mani", "2Man"),
    # ⚠️ «Controllo magia» darebbe `C-Ma`, che accanto a `C-Mg` («Capacita'
    #    magica») si legge male in una fila di quattro caratteri: due sigle che
    #    si distinguono per una lettera in fondo, sulla stessa riga, sono due
    #    sigle che il giocatore confonde. Si tiene `Ctrl`, che e' la parola
    #    intera abbreviata e non somiglia a nient'altro.
    "SKILL_NORMAL_CONTROL_MAGIC":  (2626, "Ct-M", "Controllo magia", "Ctrl"),
}

GENERATA = "tag-equip"

_MODELLO = re.compile(
    r'^\t+if \( locvar_colorres_i == (\w+) \) \{ locvar_equipinfo_s = "([^"]*)" \}$')
_NOME_ABILITA = re.compile(
    r'skillname\((\w+)\)\s*=\s*lang\(.*?,\s*"([^"]*)"\)')


class MonteMosso(Exception):
    """Il sorgente pinnato non ha piu' la forma su cui questo file si regge."""


def _righe_file(nome: str) -> list[str]:
    testo = (percorsi.SORGENTE_HSP / nome).read_bytes().decode("cp932")
    return [r.rstrip("\r") for r in testo.split("\n")]


def _controlla_geometria() -> None:
    for nome, numero, atteso, che_cosa in GEOMETRIA:
        riga = _righe_file(nome)[numero - 1]
        if riga.strip() != atteso:
            raise MonteMosso(
                "%s:%d dichiarava %s con %r e ora dice %r. Il tetto di %d "
                "caratteri veniva da li': va rifatta la misura."
                % (nome, numero, che_cosa, atteso, riga.strip(), TETTO))


def sorgente() -> dict[str, tuple[int, str]]:
    """costante -> (riga, sigla inglese), letta dal sorgente pinnato."""
    fuori = {}
    for numero, riga in enumerate(_righe_file("item_func.hsp"), 1):
        if not (2605 <= numero <= 2632):
            continue
        trovato = _MODELLO.match(riga)
        if trovato:
            fuori[trovato.group(1)] = (numero, trovato.group(2))
    return fuori


def nomi_italiani() -> dict[str, str]:
    """costante dell'abilita' -> nome italiano, letto dal dizionario.

    ⚠️ E' il rinvio, non una copia: se il dizionario cambia il nome di
    un'abilita', la sigla che lo abbreviava va ridecisa.
    """
    righe = _righe_file("skill.hsp")
    per_costante = {}
    for numero, riga in enumerate(righe, 1):
        trovato = _NOME_ABILITA.search(riga)
        if trovato:
            per_costante[trovato.group(1)] = (numero, trovato.group(2))

    percorso = percorsi.PROGETTO / "dizionario" / "skill.hsp.jsonl"
    per_riga = {}
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        voce = json.loads(riga)
        if voce.get("it"):
            per_riga[(voce["riga"], voce["en"])] = voce["it"]

    fuori = {}
    for costante, (numero, inglese) in per_costante.items():
        italiano = per_riga.get((numero, inglese))
        if italiano:
            fuori[costante] = accenti.degrada(italiano)
    return fuori


def problemi() -> list[str]:
    """Vuoto = ogni sigla e' scrivibile, unica, e legata a un nome che c'e'."""
    guai = []
    try:
        _controlla_geometria()
    except MonteMosso as errore:
        return [str(errore)]

    from strumenti.verifica import carica_invariati

    nel_sorgente = sorgente()
    italiani = nomi_italiani()
    invarianti = set(carica_invariati())

    for costante in sorted(set(nel_sorgente) - set(SIGLE)):
        guai.append(
            "item_func.hsp:%d abbrevia %s e nessuno gli ha dato una sigla "
            "italiana: il monte ha aggiunto un'abilita' al pannello."
            % (nel_sorgente[costante][0], costante))
    for costante in sorted(set(SIGLE) - set(nel_sorgente)):
        guai.append(
            "%s ha una sigla italiana e nel pannello non compare piu': una "
            "riga di tabella che non serve invecchia in silenzio." % costante)

    for costante, (numero, inglese, nome, sigla) in sorted(SIGLE.items()):
        if costante in nel_sorgente:
            riga_vera, inglese_vero = nel_sorgente[costante]
            if riga_vera != numero or inglese_vero != inglese:
                guai.append(
                    "%s stava a item_func.hsp:%d con la sigla %r e ora sta a "
                    ":%d con %r. Il monte si e' mosso sotto la tabella."
                    % (costante, numero, inglese, riga_vera, inglese_vero))
        if sigla == inglese and sigla not in invarianti:
            guai.append(
                "%s: la sigla italiana %r coincide con l'inglese, quindi non "
                "genera nessuna toppa — e allora la decisione deve stare in "
                "`invariati.md`, o le reti continueranno a chiedere per sempre "
                "un lavoro gia' deciso. E' il motivo per cui quel file esiste."
                % (costante, sigla))
        if len(sigla) > TETTO:
            guai.append(
                "%s -> %r: %d caratteri, e item_func.hsp:2629 taglia a %d. "
                "Non sborderebbe dal pannello: verrebbe TAGLIATA, e il "
                "giocatore leggerebbe un troncone."
                % (costante, sigla, len(sigla), TETTO))
        if not sigla.isascii():
            guai.append(
                "%s -> %r: non e' ASCII. Queste sono toppe, non voci di "
                "dizionario: scrivono nel file CP932 e nessuno le degrada "
                "piu'." % (costante, sigla))
        atteso = italiani.get(costante)
        if atteso is None:
            guai.append(
                "%s: la sigla %r abbreviava %r e nel dizionario di skill.hsp "
                "quel nome non c'e' piu'. Il rinvio esiste perche' la sigla e "
                "la lista delle abilita' dicano la stessa parola: se il nome "
                "se n'e' andato, la sigla va ridecisa, non indovinata."
                % (costante, sigla, nome))
        elif atteso != nome:
            guai.append(
                "%s: la sigla %r era ricavata da %r e il dizionario adesso "
                "rende quell'abilita' %r. La sigla va ridecisa sul nome "
                "nuovo." % (costante, sigla, nome, atteso))

    doppie: dict[str, list[str]] = {}
    for costante, (_n, _e, _nome, sigla) in SIGLE.items():
        doppie.setdefault(sigla, []).append(costante)
    for sigla, costanti in sorted(doppie.items()):
        if len(costanti) > 1:
            guai.append(
                "la sigla %r sta su %d abilita' (%s): nella fila si leggono "
                "una accanto all'altra, e due uguali sono due che il "
                "giocatore non puo' distinguere"
                % (sigla, len(costanti), ", ".join(sorted(costanti))))
    return guai


def toppe() -> list[dict]:
    _controlla_geometria()
    righe = _righe_file("item_func.hsp")
    fuori = []
    for costante, (numero, inglese, nome, sigla) in sorted(
            SIGLE.items(), key=lambda v: v[1][0]):
        # ⚠️ Una sigla che coincide con l'inglese non si toppa: la toppa
        # sarebbe una riga uguale a se stessa, e `applica` la conterebbe come
        # una sostituzione che non sostituisce niente. La decisione sta in
        # `invariati.md`, che e' il posto dove il progetto scrive «resta
        # cosi', e questo e' il perche'».
        if sigla == inglese:
            continue
        riga = righe[numero - 1]
        nuova = riga.replace('"%s"' % inglese, '"%s"' % sigla)
        if nuova == riga:
            raise MonteMosso(
                "item_func.hsp:%d doveva portare la sigla %r e dice %r"
                % (numero, inglese, riga.strip()[:70]))
        fuori.append({
            "file": "item_func.hsp",
            "cerca": riga,
            "sostituisci": nuova,
            "motivo": (
                "La sigla di %s nel pannello dell'equipaggiamento "
                "(item_func.hsp:%d, `*equipinfo_mmah`, ramo `showresist == "
                "3`). ⚠️⚠️ Il nome dell'abilita' arriva qui GIA' IN ITALIANO — "
                "`skillname()` (:2601) e' tradotto dal dizionario — e le "
                "quindici sigle no: stanno nel ramo `else` di `if ( jp )`, "
                "fuori da `lang()`, e un giocatore italiano leggeva %r. "
                "⚠️ Non le contava nessuna rete: `_PROSA` pretende due parole "
                "alfabetiche e `2Hnd` non ne ha nemmeno una, e `disegnate` ha "
                "l'assegnazione ancorata a inizio riga mentre qui sta dentro "
                "un `if` a graffe. Le ha trovate `strumenti/salti.py` (141a). "
                "⭐ Tetto %d caratteri, e non e' una stima: item_func.hsp:2629 "
                "fa `strmid(s, 0, 4)`, cioe' una sigla piu' lunga non sborda "
                "— viene TAGLIATA. E :2651 fa avanzare la fila con "
                "`strlen(s) * 8`, quindi quattro caratteri lasciano la "
                "geometria identica all'inglese. ⭐ La sigla %r abbrevia "
                "«%s», il nome che il dizionario da' a quell'abilita' nella "
                "lista delle abilita': il rinvio e' un cancello, non un "
                "commento. Generata da "
                "`strumenti/genera_toppe_tag_equip.py`."
                % (costante, numero, inglese, TETTO, sigla, nome)),
            "generata": GENERATA,
        })
    return fuori


def scrivi() -> int:
    mie = toppe()
    righe = _righe_file("item_func.hsp")
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

    guai = problemi()
    print("  sigle nel pannello : %d nel sorgente, %d in tabella"
          % (len(sorgente()), len(SIGLE)))
    if not guai:
        print("  tetto              : %d caratteri, tagliati da "
              "item_func.hsp:2629" % TETTO)
        print("  righe toppate      : %d" % len(toppe()))
        print()
        for costante, (numero, inglese, nome, sigla) in sorted(
                SIGLE.items(), key=lambda v: v[1][0]):
            print("  %5d  %-4s -> %-4s   %s"
                  % (numero, inglese, sigla, nome))
    for guaio in guai:
        print("  ⚠️", guaio)
    if argomenti.scrivi and not guai:
        print()
        scrivi()
    print("\n  " + ("genera_toppe_tag_equip: ogni abilita' del pannello ha la "
                    "sua sigla italiana, e nessuna verrebbe tagliata"
                    if not guai
                    else "genera_toppe_tag_equip: %d guai" % len(guai)))
    raise SystemExit(1 if guai else 0)


if __name__ == "__main__":
    main()
