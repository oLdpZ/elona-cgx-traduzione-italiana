# strumenti/genera_toppe_desideri.py
"""Le parole che il giocatore DIGITA: il desiderio e i due banchi del cambio classe.

Non e' traduzione, e' un comportamento del gioco. `command.hsp:4460` chiede
«Che cosa desideri?» e poi confronta quel che il giocatore ha scritto con una
lista chiusa di parole **giapponesi o inglesi**; lo stesso fanno i due banchi
che chiedono la nuova classe (`command.hsp:4581`, dal desiderio, e
`action.hsp:13659`, dalla pergamena). Un giocatore che legge un'interfaccia
italiana scrive italiano, e non aggancia niente: il desiderio fallisce **in
silenzio**, senza messaggio d'errore e senza che nessun cancello del progetto
se ne accorga, perche' tutti misurano il testo a schermo e questo non e' testo
a schermo.

⚠️⚠️ **Le alternative si AGGIUNGONO, non si traducono.** Il letterale a destra
di `==` non e' un'etichetta: la riga sotto scrive
`cdatan(CDATAN_CLASS, tc) = "warrior"`, che e' una **chiave** confrontata 77
volte in 13 file e passata tre volte a `*db_class` come indice di database.
Tradurre l'operando spegnerebbe il costo degli incantesimi del mago, il colpo
in piu' del guerriero e il riconoscimento dell'IA. Qui si tocca **solo** la
condizione, e solo per allungarla.

## I due tetti, misurati e non stimati

`*prompt_word` (`system.hsp:3885`) passa a `mesbox` come massimo numero di
caratteri `val(2) * (1 + en)` (`system.hsp:3985` e `:3989`). `val(2)` e' il
terzo numero della riga `val = ...` che precede la chiamata:

    command.hsp:4461   ..., winposy(90), 16, 0, 0   ->  16 * 2 = 32   il desiderio
    command.hsp:4582   ..., winposy(90), 12, 1, 0   ->  12 * 2 = 24   la classe
    action.hsp:13660   ..., winposy(90), 12, 1, 0   ->  12 * 2 = 24   la classe

Una parola piu' lunga del tetto **non si puo' nemmeno digitare**: la casella
smette di accettare caratteri. `_controlla_tetti_dichiarati` rilegge quei tre
numeri dal sorgente a ogni giro, cosi' se il monte stringe la casella il
cancello si accende invece di lasciare in giro una parola che nessuno riesce
a scrivere.

## Da dove vengono i nomi delle classi

⭐ **Le dodici classi non si decidono qui**: il nome italiano sta gia' in
`dizionario/db_class.hsp.jsonl`, che e' la stessa fonte da cui
`genera_toppe_filtri.py` prende le linguette del menu dei filtri. Leggerlo
invece di riscriverlo e' l'unico modo perche' la parola da digitare sia la
stessa che la scheda del personaggio mostra.

⚠️ **Il banco della classe non abbassa le maiuscole.** Il desiderio si', e su
una riga sola: `if ( en ) { inputlog = getpath(inputlog, 16) }`
(`command.hsp:4473`). I due banchi della classe no, e non si aggiunge la
normalizzazione: la riga dopo il confronto scrive
`cdatan(CDATAN_FAKE_CLASS, ...) = "" + inputlog`, cioe' il giocatore puo'
scriverci dentro **qualunque cosa** come falsa classe, e abbassarne le
maiuscole rovinerebbe quella liberta' per tutti. Si aggiungono percio' due
forme, «Guerriero» e «guerriero», e non una.

## Che cosa resta fuori, dichiarato

`SENZA_ITALIANO` elenca le righe della catena che una parola italiana non la
vogliono: i nomi propri degli otto dei (che in italiano si scrivono uguale),
la `q` della creatura quantistica, e i due confronti col vuoto. Una riga della
catena che non sta ne' qui ne' nelle tabelle fa alzare `KeyError`: e' il modo
di non lasciar passare in silenzio una parola nuova di monte.

⚠️ **Restano fuori anche i due `instr` scherzosi** di `:4481` e `:4485`
(「中の神」 / «god inside»), che hanno la forma della sottostringa e non del
confronto: vogliono una decisione sulla battuta, non una parola chiave.
"""
from __future__ import annotations

import json
import re

from strumenti import percorsi

# ⚠️ I tetti veri, non i numeri della finestra: sono `val(2) * (1 + en)`.
TETTO_DESIDERIO = 32
TETTO_CLASSE = 24

# file -> (prima riga, ultima riga) della catena di confronti da guardare.
BLOCCHI = {
    "command.hsp": (4469, 4790),
    "action.hsp": (13664, 13704),
}

# Le righe `val = ...` che dichiarano la larghezza della casella, e il numero
# che ci si aspetta di leggerci come terzo campo.
TETTI_DICHIARATI = [
    ("command.hsp", 4461, 16, TETTO_DESIDERIO),
    ("command.hsp", 4582, 12, TETTO_CLASSE),
    ("action.hsp", 13660, 12, TETTO_CLASSE),
]

# Le parole della catena che non vogliono un'alternativa italiana, e perche'.
SENZA_ITALIANO = {
    "": "il confronto col vuoto: il giocatore ha annullato",
    " ": "il confronto con lo spazio: il giocatore ha annullato",
    "q": "il nome della creatura quantistica, una lettera sola",
    "Q": "il nome della creatura quantistica, una lettera sola",
    "ehekatl": "nome proprio di dio: in italiano si scrive uguale",
    "lulwy": "nome proprio di dio: in italiano si scrive uguale",
    "opatos": "nome proprio di dio: in italiano si scrive uguale",
    "kumiromi": "nome proprio di dio: in italiano si scrive uguale",
    "mani": "nome proprio di dio: in italiano si scrive uguale",
    "itzpalt": "nome proprio di dio: in italiano si scrive uguale",
    "yacatect": "nome proprio di dio: in italiano si scrive uguale",
    "jure": "nome proprio di dio: in italiano si scrive uguale",
}

# ⚠️ Le parole del desiderio SONO una decisione, e vanno scritte tutte in
#    minuscolo: `command.hsp:4473` abbassa le maiuscole di quel che il
#    giocatore scrive, quindi un'alternativa con la maiuscola sarebbe morta.
#    Nessun accento: CP932 non ha le vocali accentate e la casella non le
#    accetta, quindi «eta» e non «età».
# La chiave e' la parola INGLESE che identifica il ramo.
AGGIUNTE = {
    "youth": ["giovinezza", "eta", "bellezza", "ringiovanire"],
    "aka": ["epiteto", "titolo", "soprannome"],
    "class": ["classe", "professione", "mestiere"],
    "race": ["razza", "reincarnazione", "rinascita"],
    "sex": ["sesso", "genere"],
    "redemption": ["redenzione", "espiazione"],
    "death": ["morte"],
    "friend": ["amico", "amici", "alleato", "compagno"],
    "money": ["soldi", "denaro", "oro", "ricchezza", "fortuna"],
    "medal": ["medaglia", "medaglietta", "medagliette"],
    "platina": ["platino"],
    "anoinu": ["fischietto", "fischietto per cani", "quel cane"],
    "happy new year": ["buon anno", "felice anno nuovo"],
    "merry christmas": ["buon natale"],
    "chocolate": ["cioccolato", "cioccolatino", "cioccolata"],
    "secretchar": ["personaggio segreto"],
    "repatriation": ["rimpatrio", "rimpatriare"],
}

# Le dodici chiavi di classe, nell'ordine in cui il sorgente le confronta.
# ⚠️ Sono CHIAVI: compaiono qui solo come indice del dizionario, mai come
#    cosa da riscrivere.
CLASSI = ["warrior", "thief", "wizard", "farmer", "predator", "archer",
          "warmage", "tourist", "pianist", "gunner", "priest", "claymore"]

_CONFRONTO = re.compile(r'inputlog\s*==\s*"((?:[^"\\]|\\.)*)"')
_RIGA_IF = re.compile(r'^(\s*if \( )(.*)( \) \{)$')

GENERATA = "desideri"


class MonteMosso(Exception):
    """Il sorgente pinnato non ha piu' la forma su cui questo file si regge."""


def _righe(nome: str) -> list[str]:
    testo = (percorsi.SORGENTE_HSP / nome).read_bytes().decode("cp932")
    return [r.rstrip("\r") for r in testo.split("\n")]


def nomi_classi() -> dict[str, str]:
    """Chiave di classe -> nome italiano, letto da `db_class.hsp.jsonl`.

    Alza `KeyError` sulla chiave che il dizionario non copre: un generatore
    che tira a indovinare fa digitare al giocatore una parola che la scheda
    del personaggio non dice.
    """
    percorso = percorsi.PROGETTO / "dizionario" / "db_class.hsp.jsonl"
    per_inglese: dict[str, str] = {}
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        voce = json.loads(riga)
        if voce.get("it"):
            per_inglese.setdefault(voce["en"], voce["it"])
    fuori = {}
    for chiave in CLASSI:
        etichetta = chiave.capitalize()
        if etichetta not in per_inglese:
            raise KeyError(
                "la classe %r non ha un nome italiano in db_class.hsp.jsonl: "
                "senza quello il giocatore non sa che parola scrivere al "
                "banco del cambio classe." % chiave)
        fuori[chiave] = per_inglese[etichetta]
    return fuori


def _controlla_tetti_dichiarati() -> None:
    """Rilegge dal sorgente i tre `val(2)` da cui i tetti derivano."""
    for nome, numero, atteso, tetto in TETTI_DICHIARATI:
        riga = _righe(nome)[numero - 1]
        pezzi = [p.strip() for p in riga.split(",")]
        if len(pezzi) < 3 or pezzi[2] != str(atteso):
            raise MonteMosso(
                "%s:%d doveva dichiarare una casella da %d (`val(2)`), e "
                "dice %r. Il tetto di %d caratteri veniva da li': va rifatta "
                "la misura, non aggiornato il numero a mano."
                % (nome, numero, atteso, riga.strip(), tetto))


def righe_bersaglio() -> list[tuple[str, int, str]]:
    """(file, numero, riga) di ogni confronto su `inputlog` nelle due catene."""
    fuori = []
    for nome, (da, a) in BLOCCHI.items():
        righe = _righe(nome)
        for numero in range(da, a + 1):
            riga = righe[numero - 1]
            if "inputlog ==" in riga:
                fuori.append((nome, numero, riga))
    return fuori


def alternative(riga: str, classi: dict[str, str]) -> tuple[list[str], int, str]:
    """Le parole da aggiungere alla riga, il suo tetto e il ramo che l'ha decisa.

    Torna `([], tetto, motivo)` per le righe dichiarate in `SENZA_ITALIANO`.
    """
    presenti = _CONFRONTO.findall(riga)
    if not presenti:
        raise MonteMosso("riga senza confronti su inputlog: %r" % riga)

    for chiave in presenti:
        if chiave in classi:
            nome = classi[chiave]
            volute = [nome, nome.lower()]
            return ([v for v in dict.fromkeys(volute) if v not in presenti],
                    TETTO_CLASSE, "la classe %r" % chiave)
    for chiave in presenti:
        if chiave in AGGIUNTE:
            return ([v for v in AGGIUNTE[chiave] if v not in presenti],
                    TETTO_DESIDERIO, "il desiderio %r" % chiave)

    # ⚠️ Dopo le due tabelle, mai prima: la dichiarazione vale per la riga che
    #    nessuna decisione reclama, e una riga reclamata da tutt'e due non deve
    #    poter sparire dietro il ramo giapponese, che in `SENZA_ITALIANO` non
    #    c'e' mai.
    for chiave in presenti:
        if chiave in SENZA_ITALIANO:
            return [], TETTO_DESIDERIO, SENZA_ITALIANO[chiave]

    raise KeyError(
        "la riga %r confronta %r e nessuna di quelle parole sta ne' in "
        "AGGIUNTE, ne' fra le classi, ne' in SENZA_ITALIANO. O il monte ha "
        "aggiunto un desiderio, o la tabella e' incompleta: in tutt'e due i "
        "casi la decisione e' di chi legge, non di questo file."
        % (riga.strip()[:70], presenti))


def problemi() -> list[str]:
    """Tutto quello che rende le parole scelte inservibili. Vuoto = a posto."""
    guai = []
    classi = nomi_classi()
    # ⚠️ La doppia si cerca DENTRO una catena, non fra le due: `command.hsp` e
    #    `action.hsp` sono due banchi diversi, e «Guerriero» deve valere in
    #    tutt'e due. Cercarla fra i file dichiarerebbe guasto proprio il lavoro
    #    fatto bene.
    viste: dict[tuple[str, str], str] = {}
    for nome, numero, riga in righe_bersaglio():
        try:
            nuove, tetto, _motivo = alternative(riga, classi)
        except KeyError as errore:
            guai.append(str(errore))
            continue
        for parola in nuove:
            dove = "%s:%d" % (nome, numero)
            if len(parola) > tetto:
                guai.append(
                    "%s: %r e' lunga %d e la casella ne accetta %d: il "
                    "giocatore non riuscirebbe a scriverla."
                    % (dove, parola, len(parola), tetto))
            if not parola.isascii():
                guai.append(
                    "%s: %r non e' ASCII, e la casella e' CP932: la vocale "
                    "accentata non si puo' digitare." % (dove, parola))
            # ⚠️ Un doppione fra rami diversi e' peggio di un doppione sulla
            #    stessa riga: la catena non ha `else`, quindi vincerebbe il
            #    primo ramo e il secondo resterebbe muto per sempre.
            if (nome, parola) in viste and viste[(nome, parola)] != dove:
                guai.append(
                    "%s: %r e' gia' la parola di %s, e la catena non ha "
                    "`else`: il secondo ramo non si accenderebbe mai."
                    % (dove, parola, viste[(nome, parola)]))
            viste[(nome, parola)] = dove
    return guai


def toppe() -> list[dict]:
    """Una toppa per riga che cambia."""
    _controlla_tetti_dichiarati()
    classi = nomi_classi()
    fuori = []
    for nome, numero, riga in righe_bersaglio():
        nuove, tetto, motivo = alternative(riga, classi)
        if not nuove:
            continue
        trovato = _RIGA_IF.match(riga)
        if not trovato:
            raise MonteMosso(
                "%s:%d non ha piu' la forma `if ( ... ) {`: %r"
                % (nome, numero, riga))
        testa, condizione, coda = trovato.groups()
        aggiunta = "".join(' | inputlog == "%s"' % p for p in nuove)
        fuori.append({
            "file": nome,
            "cerca": riga,
            "sostituisci": testa + condizione + aggiunta + coda,
            "motivo": (
                "%s:%d, %s. Quel che il giocatore DIGITA, non quel che legge: "
                "la catena confronta l'input con una lista chiusa di parole "
                "giapponesi o inglesi, e chi gioca in italiano scrive italiano "
                "e il desiderio fallisce in silenzio. ⚠️⚠️ Le alternative si "
                "AGGIUNGONO: l'operando non e' un'etichetta, e la riga sotto "
                "scrive una CHIAVE che il gioco confronta 77 volte in 13 file "
                "e passa tre volte a *db_class come indice di database. "
                "⚠️ Tetto %d caratteri, non stimato: `*prompt_word` passa a "
                "`mesbox` un massimo di `val(2) * (1 + en)` "
                "(`system.hsp:3985`), e oltre quello la casella smette di "
                "accettare caratteri. ⭐ I nomi delle classi non si decidono "
                "qui: il generatore li legge da `db_class.hsp.jsonl`, la "
                "stessa fonte del menu dei filtri, o il giocatore dovrebbe "
                "digitare una parola diversa da quella che la sua scheda "
                "mostra. Generata da `strumenti/genera_toppe_desideri.py`."
                % (nome, numero, motivo, tetto)),
            "generata": GENERATA,
        })
    return fuori


def scrivi() -> int:
    """Riscrive le toppe generate dentro `toppe.jsonl`. Torna quante.

    Le generate del giro precedente si **sostituiscono**, come in
    `genera_toppe_filtri.py`: una parola ritoccata non deve lasciare in giro
    la sua versione vecchia.
    """
    mie = toppe()
    for toppa in mie:
        quante = _righe(toppa["file"]).count(toppa["cerca"])
        if quante != 1:
            raise SystemExit(
                "la riga da cercare compare %d volte in %s, non una: %r"
                % (quante, toppa["file"], toppa["cerca"][:70]))

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

    _controlla_tetti_dichiarati()
    guai = problemi()
    bersagli = righe_bersaglio()
    mie = toppe() if not guai else []
    dichiarate = len(bersagli) - len(mie)
    parole = sum(len(_CONFRONTO.findall(t["sostituisci"]))
                 - len(_CONFRONTO.findall(t["cerca"])) for t in mie)
    print("  righe della catena    : %d   (%s)"
          % (len(bersagli), ", ".join("%s %d" % (n, sum(1 for b in bersagli
                                                        if b[0] == n))
                                      for n in BLOCCHI)))
    print("  righe toppate         : %d" % len(mie))
    print("  righe dichiarate      : %d   (dei, «q», il vuoto)" % dichiarate)
    print("  parole aggiunte       : %d" % parole)
    print("  tetti                 : %d il desiderio, %d la classe"
          % (TETTO_DESIDERIO, TETTO_CLASSE))
    for guaio in guai:
        print("  ⚠️", guaio)
    if argomenti.scrivi and not guai:
        scrivi()
    print("\n  " + ("genera_toppe_desideri: nessuna parola e' fuori misura o "
                    "doppia" if not guai
                    else "genera_toppe_desideri: %d guai" % len(guai)))
    raise SystemExit(1 if guai else 0)


if __name__ == "__main__":
    main()
