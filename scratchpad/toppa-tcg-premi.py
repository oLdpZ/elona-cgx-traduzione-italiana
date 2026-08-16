# -*- coding: utf-8 -*-
"""52a, lotto `tcg-premi`: i premi e i duelli mortali, e il nome del gioco.

Chiude `tcg_custom.hsp` (15 righe) e scioglie una delle tre incoerenze che la
51a aveva lasciato aperte: il gioco di carte si chiamava «Gioco delle Tenebre»
in `command.hsp:6166` e «Gioco delle Ombre» in `chara_func.hsp:7002` e `:7004`.

⭐ **Vince «Gioco delle Ombre», e non per maggioranza**: e' il termine italiano
ufficiale di Yu-Gi-Oh! per «Shadow Game», e il mod cita quella serie
apertamente — `:1587` sigilla l'avversario **dentro una carta** e `:1556` dice
che chi scappa ci lascia **l'anima danneggiata**. Il riferimento e' il contenuto
della scena, non un'eco lontana. Cambia una voce sola (il dizionario di
`command.hsp` piu' la toppa gemella del pannello dei ritocchi).

⚠️ **«amur-cage» non era mai stato reso**, ed e' il posto dove finisce chi
perde: `chara_func.hsp:7002` e `:7004` l'avevano AGGIRATO riscrivendo la frase
(«X perde il Gioco delle Ombre contro Y») invece di nominare la gabbia. Qui non
si puo' aggirare, perche' la gabbia e' il soggetto della frase.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\tcg_custom.hsp")
FILE = "tcg_custom.hsp"
TESTO = SORGENTE.read_bytes().decode("cp932").splitlines()

VECCHIO_NOME, NUOVO_NOME = "Gioco delle Tenebre", "Gioco delle Ombre"

LOTTO = [
    (1550,
     "Time passed, but your opponent seems to have reverted back to the moment before the duel, a strange phenomenon in the Moongate world, as if the duel had never occurred.",
     "Il tempo e' passato, ma il tuo avversario sembra tornato all'istante prima del duello: uno strano fenomeno del mondo del cancello lunare, come se il duello non fosse mai avvenuto.",
     "⭐ «cancello lunare» e' il nome che il progetto usa gia' (il ritocco del "
     "bottino nelle mappe da cancello lunare, `custom_tweaks.hsp:1290`). ⚠️ I due "
     "punti al posto della virgola davanti a «uno strano fenomeno»: in inglese "
     "l'apposizione regge con la virgola, in italiano no."),
    (1556, "You escaped from the lethal game, but your soul is severedly damaged in the process!",
     "Sei scappato dalla partita mortale, ma ne esci con l'anima gravemente ferita!",
     "⭐ «partita mortale» e non «gioco mortale»: e' la singola partita, non il "
     "gioco in se'. ⚠️ «severedly» e' un refuso di monte per «severely», e non "
     "si ricalca. «ne esci con l'anima ferita» evita il passivo inglese, che in "
     "italiano suonerebbe da referto medico."),
    (1568, " consecutive lethal game victory!", " vittorie di fila in partite mortali!",
     "⚠️ L'inglese dice «victory» al singolare anche quando il numero e' due o "
     "piu': e' un refuso di monte. L'italiano mette il plurale, che con un "
     "contatore davanti e' l'unica forma che regge."),
    (1587, "Your opponent is sealed into a card!", "Il tuo avversario viene sigillato dentro una carta!",
     "⭐ La riga che decide il nome del gioco: e' la citazione di Yu-Gi-Oh!, e "
     "«sigillato» e' il verbo di quella serie."),
    (1608, "You are sent to the amur-cage!", "Finisci nella gabbia di Amur!",
     "⚠️ La prima resa di «amur-cage» del progetto: `chara_func.hsp:7002` e "
     "`:7004` l'avevano aggirata riscrivendo la frase, qui la gabbia e' il "
     "soggetto e va nominata. ⭐ «Finisci» e non «Sei mandato»: l'italiano non "
     "ha bisogno del passivo, e la seconda persona e' quella che il resto della "
     "scena usa."),
    (1611, "Also, your socks were stolen!", "E ti hanno pure rubato i calzini!",
     "«calzini» e' del dizionario (`db_item.hsp:134939`). ⭐ «pure» tiene il tono "
     "sconsolato di «Also,», che tradotto «Inoltre,» diventerebbe un verbale."),
    (1633, " consecutive wins!", " vittorie di fila!", "Il gemello non mortale di `:1568`."),
    (1637, "You get ", "Ricevi ", "I biglietti: il resto della riga tiene la variabile."),
    (1637.1, " music tickets!", " biglietti per il concerto!",
     "«music ticket» e' «biglietto per il concerto» dal dizionario "
     "(`db_item.hsp:142700`): il nome pieno, perche' e' l'oggetto che finisce "
     "nell'inventario con quel nome."),
    (1651, " wins against Unique NPCs!", " vittorie contro PNG unici!",
     "«PNG» e' la sigla che il progetto usa gia' in tutto `custom_tweaks.hsp`."),
    (1654, "You get a Card Pack!", "Ricevi un pacchetto di carte!",
     "«pacchetto di carte» dal dizionario (`db_item.hsp:141802`)."),
    (1662, "Your socks were stolen!", "Ti hanno rubato i calzini!",
     "Il gemello di `:1611` senza «Also»."),
    (1707, "You got an ultra rare card!", "Hai preso una carta ultra rara!",
     "⭐ Le quattro rarita' concordano al femminile con «carta», che in inglese "
     "non e' un problema perche' l'aggettivo non si accorda."),
    (1722, "You got a super rare card!", "Hai preso una carta super rara!", "Come sopra."),
    (1733, "You got an uncommon card!", "Hai preso una carta non comune!",
     "⭐ «non comune» e non «insolita»: e' il gradino di rarita' dei giochi di "
     "carte, e «comune» e' gia' la resa di `common` nelle qualita' "
     "(`text.hsp:106`)."),
    (1737, "You got a rare card!", "Hai preso una carta rara!", "Come sopra."),
]


def main() -> None:
    toppe, problemi, viste = [], [], {}
    for chiave, vecchio, nuovo, motivo in LOTTO:
        n = int(chiave)
        cerca = TESTO[n - 1]
        if vecchio not in cerca:
            problemi.append(f":{n} non contiene {vecchio!r}")
            continue
        # due pezzi della stessa riga (`:1637`): il secondo lavora sul primo
        base = viste.get(cerca, cerca)
        resa = base.replace(vecchio, nuovo, 1)
        for c in resa:
            if ord(c) > 0x7F:
                problemi.append(f":{n} carattere fuori ASCII: {c!r}")
        viste[cerca] = resa

    for cerca, resa in viste.items():
        quante = TESTO.count(cerca)
        motivi = [m for k, v, nu, m in LOTTO if TESTO[int(k) - 1] == cerca]
        toppa = {"file": FILE, "cerca": cerca, "sostituisci": resa,
                 "motivo": " ".join(motivi)}
        if quante > 1:
            toppa["tutte"] = True
            toppa["motivo"] += f" ⭐ `tutte`: la riga sta identica in {quante} punti."
        toppe.append(toppa)

    if problemi:
        for p in problemi:
            print("⚠️ ", p)
        raise SystemExit("lotto non scritto")

    # --- l'incoerenza del nome: la voce di dizionario e la toppa gemella
    diz = REPO / "dizionario" / "command.hsp.jsonl"
    righe, cambiate = [], 0
    for r in diz.read_text(encoding="utf-8").splitlines():
        v = json.loads(r)
        if v.get("it") and VECCHIO_NOME in v["it"]:
            v["it"] = v["it"].replace(VECCHIO_NOME, NUOVO_NOME)
            cambiate += 1
        righe.append(json.dumps(v, ensure_ascii=False))
    diz.write_bytes(("\n".join(righe) + "\n").encode("utf-8"))
    print(f"dizionario di command.hsp: {cambiate} voce/i col nuovo nome")

    tp = REPO / "toppe.jsonl"
    righe, cambiate_t = [], 0
    for r in tp.read_text(encoding="utf-8").splitlines():
        v = json.loads(r)
        s = v.get("sostituisci")
        if isinstance(s, str) and VECCHIO_NOME in s:
            v["sostituisci"] = s.replace(VECCHIO_NOME, NUOVO_NOME)
            v["motivo"] = v.get("motivo", "") + (
                " ⚠️ Il nome del gioco e' cambiato nella 52a: «Gioco delle Tenebre» "
                "-> «Gioco delle Ombre», che e' il termine italiano di Yu-Gi-Oh! per "
                "«Shadow Game» ed era gia' la resa di `chara_func.hsp:7002` e "
                "`:7004`. Il mod cita quella serie apertamente: "
                "`tcg_custom.hsp:1587` sigilla l'avversario dentro una carta.")
            cambiate_t += 1
        righe.append(json.dumps(v, ensure_ascii=False))
    tp.write_bytes(("\n".join(righe) + "\n").encode("utf-8"))
    print(f"toppe: {cambiate_t} col nuovo nome")

    print(f"{len(toppe)} toppe per {FILE}")
    uscita = REPO / "lavoro" / "_toppe-tcg-premi.jsonl"
    dati = "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in toppe).encode("utf-8")
    uscita.write_bytes(dati)

    esito = subprocess.run(
        [sys.executable, str(REPO / "scratchpad" / "aggiungi-toppe.py"), str(uscita)],
        cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    print(esito.stdout.strip() or esito.stderr.strip())


if __name__ == "__main__":
    main()
