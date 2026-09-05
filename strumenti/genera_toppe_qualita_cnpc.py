# strumenti/genera_toppe_qualita_cnpc.py
"""Le sei qualita' del CNPC evocato, e la giuntura che le sposta.

`command.hsp:7715-:7724` (`*com_userNpcExisting_loop`) monta in `s` la qualita'
del *Custom NPC* che il giocatore evoca, ci appende il nome, e infila il tutto
nel ramo inglese di una `lang()`:

    s = ""                                                        :7715
    if ( userdata(5, knowCNPC) == 1 ) { s += "Bad " }             :7716
    ... altre cinque ...                                          :7717-:7721
    s += userdatan(3, knowCNPC)                                   :7722
    txt lang("別世界の何かを召喚した！",
             "A " + s + " is summoned from another world!")        :7724

⚠️⚠️ **E la resa italiana buttava via `s`.** Il dizionario rendeva quella riga
con «Qualcosa di un altro mondo e' stato evocato!»: il giocatore inglese legge
**chi** e' arrivato e con che qualita', quello italiano no. E' la specie della
131a — «l'articolo era calcolato, salvato e buttato una riga dopo» — e la
ripresa la elencava fra le reti che mancavano.

⭐ **La misura, spaccata.** Delle 2.891 rese dinamiche del progetto, 832
perdono un operando; 822 lo perdono **giustamente**, perche' e' l'accordo del
verbo inglese (`_s`, `is`, `was`, `his`, `your`) o l'ordinale (`cnvrank`, che
in giapponese restituisce gia' il numero nudo, `init.hsp:149`). Le perdite
vere sono **una**: questa.

## Perche' nessuna rete le vedeva: il terzo punto cieco

`copertura._PROSA` pretende due parole alfabetiche e `Bad ` ne ha una.
`disegnate` e `salti` prendevano il **primo** simbolo dopo il comando che
disegna: qui il primo simbolo e' `lang`, e `s` sta **dentro** l'argomento,
concatenato. E' la terza ancora dopo quella della graffa e quella del nome
generico, ed e' tolta in `salti._disegnate_sulla_riga` dalla stessa sessione.

## La giuntura: perche' non basta tradurre sei parole

⚠️ In inglese la qualita' sta **davanti** al nome («a Legendary Fulano»), e in
italiano un aggettivo davanti a un nome proprio non regge. La cura e' quella
della 82a — l'**apposizione** — e vuole che il nome venga prima:

    "Fulano, da leggenda"

quindi la toppa non tocca solo le sei parole: sposta anche la giuntura di
`:7722`, da `s += userdatan(…)` a `s = userdatan(…) + s`. ⭐ E per questo le
sei rese portano la virgola in testa invece dello spazio in coda: cosi' un
CNPC **senza** qualita' esce «Fulano» e non «Fulano, », che e' il difetto che
la giuntura spostata avrebbe introdotto da sola.

## Gli aggettivi sono INVARIABILI IN GENERE, e non e' una preferenza

⚠️⚠️ `s` finisce attaccato al nome di una creatura di cui **nessuno conosce il
sesso**: i CNPC li scrive il giocatore. `guida-stile.md` («l'etichetta si legge
dove esce») e `contratto-nomi.md` §3 dicono la stessa cosa, e l'hanno imparata
a schermo sulle sei qualita' dell'oggetto: *un aggettivo che esce attaccato a
un nome di genere ignoto va invariabile*. Percio' «da leggenda» e non
«leggendario», «celebre» e non «famoso».

⭐ E due delle sei non si decidono qui: «scadente» e «comune» sono gia' le
parole con cui `text.hsp:106` rende le qualita' dell'oggetto, e il generatore
le rilegge dal dizionario invece di riscriverle.
"""
from __future__ import annotations

import json
import re

from strumenti import accenti, percorsi

# riga -> (inglese nel sorgente, italiano, perche')
QUALITA: dict[int, tuple[str, str, str]] = {
    7716: ("Bad ", ", scadente",
           "rinvio a `text.hsp:106`: e' la parola con cui il progetto rende "
           "gia' la qualita' piu' bassa di un oggetto"),
    7717: ("Common ", ", comune",
           "rinvio a `text.hsp:106`, come «scadente»"),
    7718: ("Skilled ", ", abile",
           "invariabile in genere per costruzione: «abile» vale per «Maria» "
           "come per «Fulano»"),
    7719: ("Professional ", ", professionista",
           "e' un sostantivo, quindi non concorda col nome che lo precede. "
           "⚠️ «esperto» concorderebbe, e il sesso di un CNPC non si sa"),
    7720: ("Legendary ", ", da leggenda",
           "⚠️ «leggendario» concorda («leggendaria»): la locuzione con «da» "
           "no, e dice la stessa cosa"),
    7721: ("Well-Known ", ", celebre",
           "⚠️ «famoso» concorda, «celebre» ha una forma sola per i due "
           "generi"),
}

# La giuntura: il nome viene PRIMA, e l'apposizione dopo (regola della 82a).
GIUNTURA = (7722,
            "s += userdatan(3, knowCNPC)",
            "s = userdatan(3, knowCNPC) + s")

# Le due parole che si rileggono invece di riscriverle.
# ⚠️ Le chiavi sono minuscole: `text.hsp:106` scrive `bad`/`common`, la
#    qualita' del CNPC `Bad `/`Common `. Sono la stessa parola in due grafie.
DAL_DIZIONARIO = {7716: "bad", 7717: "common"}

GENERATA = "qualita-cnpc"

_MODELLO = re.compile(
    r'^\t+if \( userdata\(5, knowCNPC\) == (\d) \) \{ s \+= "([^"]*)" \}$')


class MonteMosso(Exception):
    """Il sorgente pinnato non ha piu' la forma su cui questo file si regge."""


def _righe_file(nome: str) -> list[str]:
    testo = (percorsi.SORGENTE_HSP / nome).read_bytes().decode("cp932")
    return [r.rstrip("\r") for r in testo.split("\n")]


def sorgente() -> dict[int, str]:
    """riga -> qualita' inglese, letta dal sorgente pinnato."""
    righe = _righe_file("command.hsp")
    fuori = {}
    for numero in range(7710, 7724):
        trovato = _MODELLO.match(righe[numero - 1])
        if trovato:
            fuori[numero] = trovato.group(2)
    return fuori


def dal_dizionario() -> dict[int, str]:
    """Le due qualita' gia' decise per gli oggetti, rilette e non riscritte.

    ⚠️ Se `text.hsp` smettesse di rendere `Bad` con «scadente», la parola qui
    andrebbe ridecisa e non indovinata: e' lo stesso rinvio con cui la 140a ha
    legato le etichette di F1 alla barra dei comandi.
    """
    percorso = percorsi.PROGETTO / "dizionario" / "text.hsp.jsonl"
    per_inglese: dict[str, str] = {}
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        voce = json.loads(riga)
        if voce.get("it") and voce["riga"] == 106:
            per_inglese.setdefault(voce["en"], voce["it"])
    fuori = {}
    for numero, inglese in DAL_DIZIONARIO.items():
        if inglese not in per_inglese:
            raise KeyError(
                "la qualita' %r rinviava a text.hsp:106, dove il progetto "
                "rende le qualita' dell'oggetto, e li' quella voce non c'e' "
                "piu'. Il rinvio esiste perche' le due schermate dicano la "
                "stessa parola: se la voce se n'e' andata, la parola va "
                "ridecisa, non indovinata." % inglese)
        fuori[numero] = ", " + accenti.degrada(per_inglese[inglese]).lower()
    return fuori


def rese() -> dict[int, str]:
    fuori = {n: accenti.degrada(v[1]) for n, v in QUALITA.items()}
    fuori.update(dal_dizionario())
    return fuori


def problemi() -> list[str]:
    """Vuoto = ogni qualita' ha la sua parola, invariabile e scrivibile."""
    guai = []
    nel_sorgente = sorgente()
    if set(nel_sorgente) != set(QUALITA):
        return ["command.hsp:7716-:7721 doveva portare sei qualita' e ne "
                "porta %d (righe %s): il monte si e' mosso sotto la tabella."
                % (len(nel_sorgente), sorted(nel_sorgente))]
    for numero, inglese in nel_sorgente.items():
        if inglese != QUALITA[numero][0]:
            guai.append(
                "command.hsp:%d portava %r e ora porta %r: il monte si e' "
                "mosso sotto la tabella."
                % (numero, QUALITA[numero][0], inglese))

    riga_giuntura = _righe_file("command.hsp")[GIUNTURA[0] - 1].strip()
    if riga_giuntura != GIUNTURA[1]:
        guai.append(
            "command.hsp:%d doveva appendere il nome con %r e dice %r. La "
            "resa italiana mette il nome PRIMA della qualita', e senza quella "
            "riga l'apposizione non si compone."
            % (GIUNTURA[0], GIUNTURA[1], riga_giuntura))

    try:
        tabella = rese()
    except KeyError as errore:
        return guai + [str(errore)]

    for numero, italiano in tabella.items():
        if not italiano.startswith(", "):
            guai.append(
                "command.hsp:%d -> %r: la resa deve cominciare con «, », "
                "perche' la giuntura mette il nome davanti e un CNPC senza "
                "qualita' deve uscire «Fulano» e non «Fulano, »."
                % (numero, italiano))
        if not italiano.isascii():
            guai.append(
                "command.hsp:%d -> %r: non e' ASCII. Queste sono toppe, non "
                "voci di dizionario: scrivono nel file CP932 e nessuno le "
                "degrada piu'." % (numero, italiano))
        # ⚠️ Il cancello del genere: una resa che finisce in `o` e' un
        #    aggettivo maschile, e qui il nome accanto e' di sesso ignoto.
        ultima = italiano.rstrip().rsplit(" ", 1)[-1]
        if ultima.endswith("o") and ultima not in ("professionista",):
            guai.append(
                "command.hsp:%d -> %r: %r finisce in «o», cioe' concorda al "
                "maschile, e `s` esce attaccato al nome di un CNPC di cui "
                "nessuno sa il sesso. Vedi `guida-stile.md`, «l'etichetta si "
                "legge dove esce»." % (numero, italiano, ultima))
    doppie = [v for v in tabella.values() if list(tabella.values()).count(v) > 1]
    if doppie:
        guai.append("due qualita' hanno la stessa parola (%s): il giocatore "
                    "non potrebbe distinguerle" % sorted(set(doppie)))
    return guai


def toppe() -> list[dict]:
    tabella = rese()
    righe = _righe_file("command.hsp")
    fuori = []
    for numero in sorted(tabella):
        riga = righe[numero - 1]
        inglese = QUALITA[numero][0]
        nuova = riga.replace('"%s"' % inglese, '"%s"' % tabella[numero])
        if nuova == riga:
            raise MonteMosso("command.hsp:%d doveva portare %r e dice %r"
                             % (numero, inglese, riga.strip()[:70]))
        fuori.append({
            "file": "command.hsp",
            "cerca": riga,
            "sostituisci": nuova,
            "motivo": (
                "La qualita' %r del CNPC evocato (command.hsp:%d, "
                "`*com_userNpcExisting_loop`). ⚠️⚠️ La resa italiana della "
                "riga che la disegna — `:7724` — **buttava via `s`**: diceva "
                "«Qualcosa di un altro mondo e' stato evocato!», e il "
                "giocatore inglese leggeva chi era arrivato e con che "
                "qualita'. Delle 832 rese dinamiche che perdono un operando "
                "questa e' l'unica perdita vera: le altre perdono l'accordo "
                "del verbo inglese o l'ordinale, che l'italiano non ha. "
                "⚠️ Non la contava nessuna rete: `_PROSA` pretende due parole "
                "alfabetiche, e `disegnate` e `salti` prendevano il PRIMO "
                "simbolo dopo il comando — qui e' `lang`, e `s` sta dentro "
                "l'argomento, concatenato. E' il TERZO punto cieco, tolto "
                "nella stessa 141a. ⭐ %s. ⚠️ La parola e' invariabile in "
                "genere perche' esce attaccata al nome di un CNPC, che lo "
                "scrive il giocatore e di cui nessuno sa il sesso "
                "(`guida-stile.md`, «l'etichetta si legge dove esce»). "
                "⚠️ La virgola in testa non e' un vezzo: la giuntura di "
                "`:7722` mette il nome DAVANTI, e senza la virgola qui un "
                "CNPC senza qualita' uscirebbe «Fulano, ». Generata da "
                "`strumenti/genera_toppe_qualita_cnpc.py`."
                % (inglese, numero, QUALITA[numero][2])),
            "generata": GENERATA,
        })

    numero, vecchia, nuova = GIUNTURA
    riga = righe[numero - 1]
    fuori.append({
        "file": "command.hsp",
        "cerca": riga,
        "sostituisci": riga.replace(vecchia, nuova),
        "motivo": (
            "La giuntura fra la qualita' e il nome del CNPC evocato "
            "(command.hsp:%d). ⚠️⚠️ **Non e' una resa: e' un ordine.** In "
            "inglese la qualita' sta davanti al nome («a Legendary Fulano»), "
            "e in italiano un aggettivo davanti a un nome proprio non regge: "
            "la forma che tiene e' l'**apposizione** — «Fulano, da leggenda» "
            "— ed e' la stessa regola con cui la 82a ha sciolto epiteto e "
            "nome in `chat.hsp:16472`. ⭐ Le sei rese portano percio' la "
            "virgola in testa invece dello spazio in coda, e un CNPC senza "
            "qualita' esce «Fulano» e non «Fulano, ». Generata da "
            "`strumenti/genera_toppe_qualita_cnpc.py`." % numero),
        "generata": GENERATA,
    })
    return fuori


def scrivi() -> int:
    mie = toppe()
    righe = _righe_file("command.hsp")
    for toppa in mie:
        quante = righe.count(toppa["cerca"])
        if quante != 1:
            raise SystemExit("la riga da cercare compare %d volte, non una: %r"
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
    analizzatore.add_argument("--scrivi", action="store_true")
    argomenti = analizzatore.parse_args()

    guai = problemi()
    print("  qualita' nel sorgente : %d" % len(sorgente()))
    if not guai:
        tabella = rese()
        print("  lette dal dizionario  : %d" % len(DAL_DIZIONARIO))
        print("  decise qui            : %d" % (len(tabella) - len(DAL_DIZIONARIO)))
        print("  righe toppate         : %d (sei rese piu' la giuntura)"
              % len(toppe()))
        print()
        for numero in sorted(tabella):
            print("  %5d  %-15s -> %r" % (numero, QUALITA[numero][0],
                                          tabella[numero]))
        print("  %5d  la giuntura     -> %r" % (GIUNTURA[0], GIUNTURA[2]))
    for guaio in guai:
        print("  ⚠️", guaio)
    if argomenti.scrivi and not guai:
        print()
        scrivi()
    print("\n  " + ("genera_toppe_qualita_cnpc: ogni qualita' ha la sua "
                    "parola, e nessuna concorda col nome accanto"
                    if not guai
                    else "genera_toppe_qualita_cnpc: %d guai" % len(guai)))
    raise SystemExit(1 if guai else 0)


if __name__ == "__main__":
    main()
