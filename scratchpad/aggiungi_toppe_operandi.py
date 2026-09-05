"""Le quattro toppe che chiudono due dei quattro fronti della rete dell'operando.

Si scrivono da qui e non a mano perche' le righe d'aggancio portano il
giapponese: copiarle a occhio vorrebbe dire ribatterle, e una barra rovescia o
un ideogramma sbagliato le renderebbe muta.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from strumenti import percorsi

TOPPE = percorsi.PROGETTO / "toppe.jsonl"


def riga(nome, numero):
    testo = (percorsi.SORGENTE_HSP / nome).read_bytes().decode("cp932")
    return testo.split("\n")[numero - 1].rstrip("\r")


def infila(originale, aggiunta, prima_di):
    """Aggiunge un pezzo prima dell'ultima chiusura della condizione."""
    posto = originale.rindex(prima_di)
    return originale[:posto] + aggiunta + originale[posto:]


MOTIVO_ALCHIMISTA = (
    "LA PROFESSIONE DELL'ALCHIMISTA (%s): la riga cerca il troncone "
    "\"lchemist\" dentro CDATAN_FAKE_CLASS, che e' la professione finta, e la "
    "professione finta la DIGITA il giocatore col desiderio "
    "(action.hsp:13705, `cdatan(CDATAN_FAKE_CLASS, tc) = \"\" + inputlog`). Un "
    "giocatore che legge un'interfaccia italiana scrive «alchimista», e la "
    "battuta non esce: e' lo stesso guasto muto delle due battute del "
    "desiderio della 142a e delle dodici classi. ⭐ Il troncone italiano e' "
    "\"lchimista\" e non \"alchimista\" per la stessa ragione per cui quello "
    "inglese e' \"lchemist\" e non \"alchemist\": salta la prima lettera, e "
    "cosi' piglia anche «Alchimista» con la maiuscola. ⚠️ La forma nuova si "
    "AGGIUNGE in or: chi gioca di monte deve poter scrivere ancora "
    "«alchemist». ⓘ Trovata da strumenti/operandi.py, che misura le chiavi "
    "delle sostituzioni."
)

MOTIVO_DRAGO = (
    "LA CACCIATRICE DI DRAGHI (tcg_skill.hsp:%s): l'effetto di Spipha uccide "
    "la carta se e' un drago, e lo riconosce in due modi — la razza "
    "(`== \"dragon\"`, chiave interna che resta inglese) oppure il TESTO della "
    "carta, cercandoci dentro \"ragon\". Il testo della carta adesso e' "
    "italiano. ⭐⭐ MISURATO su db_card.hsp della build: \"ragon\" ci compare "
    "ancora 4 volte, e sono tutte «dragonewt»; «drago» ci compare 60 volte, "
    "«Drago» 2 e «draghi» 28. Cioe' oggi l'effetto aggancia per testo soltanto "
    "i quattro dragonewt, e ogni altro drago si salva. ⚠️ La chiave italiana e' "
    "\"drago\" e non il troncone \"rago\": \"rago\" avrebbe pigliato anche "
    "«mandragora», «aragosta», «fragore» e «fragorosa», e un errore qui non e' "
    "una parola storta, e' una carta uccisa che non doveva morire. Le tre "
    "forme (\"drago\", \"Drago\", \"draghi\") coprono le 90 occorrenze vere. "
    "⚠️ «drago» e' la resa fissata dal glossario (riga 278), e questa toppa non "
    "decide niente di nuovo: porta la chiave dietro alla decisione. ⚠️ Le "
    "forme si AGGIUNGONO in or, e \"ragon\" resta per i dragonewt e per il "
    "gioco di monte. ⓘ Trovata da strumenti/operandi.py."
)


def main():
    nuove = []

    # --- l'alchimista: cinque righe gemelle in command.hsp, una in action ---
    originale = riga("command.hsp", 52)
    aggiunta = (' | instr(cdatan(CDATAN_FAKE_CLASS, CHARA_PLAYER), 0, '
                '"lchimista") != (-1)')
    nuove.append({
        "file": "command.hsp",
        "cerca": originale,
        "sostituisci": infila(originale, aggiunta, " ) {"),
        "tutte": True,
        "motivo": MOTIVO_ALCHIMISTA % ":52, :57, :62, :67, :72 — cinque righe "
                  "identiche, e vogliono tutte la stessa cura",
    })

    originale = riga("action.hsp", 123)
    aggiunta = ' | instr(cdatan(CDATAN_FAKE_CLASS, cc), 0, "lchimista") != (-1)'
    nuove.append({
        "file": "action.hsp",
        "cerca": originale,
        "sostituisci": infila(originale, aggiunta, " ) ) {"),
        "motivo": MOTIVO_ALCHIMISTA % "action.hsp:123, la castagna",
    })

    # --- la cacciatrice di draghi: due righe gemelle piu' una rientrata ---
    def con_draghi(originale):
        pezzo = ""
        for parola in ("drago", "Drago", "draghi"):
            pezzo += (' | instr(carddetailneff@tcg(spiphatarget@tcg), 0, "%s")'
                      ' != -1' % parola)
        return infila(originale, pezzo, " ) {")

    originale = riga("tcg_skill.hsp", 4960)
    assert originale == riga("tcg_skill.hsp", 4972), "le gemelle non sono gemelle"
    nuove.append({
        "file": "tcg_skill.hsp",
        "cerca": originale,
        "sostituisci": con_draghi(originale),
        "tutte": True,
        "motivo": MOTIVO_DRAGO % "4960 e :4972, due righe identiche",
    })

    originale = riga("tcg_skill.hsp", 5003)
    nuove.append({
        "file": "tcg_skill.hsp",
        "cerca": originale,
        "sostituisci": con_draghi(originale),
        "motivo": MOTIVO_DRAGO % "5003, la terza, che ha un rientro in piu' e "
                  "percio' e' una toppa sua",
    })

    esistenti = [json.loads(r) for r in
                 TOPPE.read_text(encoding="utf-8").splitlines() if r.strip()]
    # ⓘ `cerca` puo' essere una lista di righe: si normalizza a testo.
    gia = {(t["file"], json.dumps(t["cerca"], ensure_ascii=False))
           for t in esistenti}
    for toppa in nuove:
        if (toppa["file"],
                json.dumps(toppa["cerca"], ensure_ascii=False)) in gia:
            raise SystemExit("gia' presente: %s" % toppa["file"])
        print("+ %s" % toppa["file"])
        print("  - %s" % toppa["cerca"].strip()[:120])
        print("  + %s" % toppa["sostituisci"].strip()[:200])

    if "--scrivi" in sys.argv:
        with TOPPE.open("a", encoding="utf-8", newline="\n") as f:
            for toppa in nuove:
                f.write(json.dumps(toppa, ensure_ascii=False) + "\n")
        print("scritte %d toppe, ora sono %d"
              % (len(nuove), len(esistenti) + len(nuove)))


if __name__ == "__main__":
    main()
