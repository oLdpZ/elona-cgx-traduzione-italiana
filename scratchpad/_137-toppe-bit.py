"""Lotto A della Fase 6: la riga dei tratti nella scheda di ogni carta.

Trentuno etichette di bit piu' `"Bits:  "`, che `copertura._PROSA` non puo'
vedere perche' pretende due parole. Sono letterali nudi dentro il codice, quindi
sono **toppe**, come le altre 103 di `tcg.hsp`.

⚠️⚠️ `"Bits:  "` la SCRIVE un sito solo (`:1522`) e la CERCANO tre
(`:1470`, `:4625`, `:4630`). Tradurre solo la scrittura fa sparire la riga dei
tratti dalla scheda di ogni carta che ne abbia: e' la trappola della 136a, dove
un operando non censito ha spento la copia di 195 carte. Qui i quattro siti si
scrivono insieme, e una prova pretende che restino quattro.

⚠️ Gli accenti si scrivono gia' degradati: nessuna delle 1.230 toppe del
progetto ne porta uno vero, perche' l'albero di build e' CP932 e «à» non
c'e' dentro.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strumenti import percorsi  # noqa: E402

FILE = "tcg.hsp"

# Il glossario e' quello della 136a (`carte.PAROLE_CHIAVE`), che l'aveva ricavato
# dalle toppe gia' a schermo invece di deciderlo a tavolino. Qui si aggiungono le
# due che li' non c'erano, e le due grafie col trattino che il sorgente usa.
#
# ⚠️ `Immune` e `Kamikaze` NON stanno qui: in italiano si scrivono uguali, e una
# toppa con `cerca` identico a `sostituisci` `applica` la rifiuta -- giustamente,
# perche' e' una toppa muta, cioe' una che nessuno accorgerebbe se smettesse di
# agganciare. Restano invariate **per decisione**, non per dimenticanza:
# `carte.PAROLE_CHIAVE` le porta gia' tutt'e due con la stessa forma.
INVARIATE = ("Immune ", "Kamikaze ")

ETICHETTE = {
    "Regeneration ": "Rigenerazione ",
    "Armored ":      "Corazza ",
    "Flying ":       "Volo ",
    "Intimidate ":   "Minaccia ",
    "Reach ":        "Portata ",
    "Lifelink ":     "Legame vitale ",
    "Haste ":        "Impeto ",
    "Trample ":      "Travolgere ",
    "First-Strike ": "Anticipo ",
    "Dual-Strike ":  "Doppio colpo ",
    "Deathtouch ":   "Tocco letale ",
    "Critical ":     "Critico ",
    "Windfury ":     "Raffica ",
    "Windfury(1) ":  "Raffica(1) ",
    "Vigilance ":    "Vigilanza ",
    "Defender ":     "Difensore ",
    "Splits ":       "Scissione ",
    "Rider ":        "Cavaliere ",
    "Barrier ":      "Barriera ",
    "Evasion ":      "Schivata ",
    "Deathword ":    "Condanna ",
    "Gravity ":      "Gravita' ",
    "Bleeding ":     "Sangue ",
    "Poisoned ":     "Veleno ",
    "Paralysed ":    "Paralisi ",
    "Silenced ":     "Silenzio ",
    "Frozen ":       "Gelo ",
    "Insane ":       "Follia ",
    "Confused ":     "Confusione ",
}

# ⚠️ I DUE SPAZI SONO PORTANTI: chi la cerca la cerca esatta.
BITS_EN = "Bits:  "
BITS_IT = "Tratti:  "

MOTIVO_ETICHETTA = (
    "La riga dei tratti nella scheda della carta (`tcg.hsp:1522-1605`), che il "
    "giocatore legge premendo `c`. ⚠️ `copertura._PROSA` pretende DUE parole e "
    "queste ne hanno una: erano a schermo in inglese e nessun conto le vedeva. "
    "Il traducente e' quello che il progetto usa gia' nelle descrizioni "
    "d'effetto (`carte.PAROLE_CHIAVE`, glossario della 136a), non una scelta "
    "nuova."
)

MOTIVO_BITS = (
    "⚠️⚠️ `\"Bits:  \"` (DUE spazi, portanti) la scrive `tcg.hsp:1522` e la "
    "CERCANO `:1470`, `:4625` e `:4630`. Tradotta solo dove si scrive, la riga "
    "dei tratti sparisce dalla scheda di ogni carta che ne abbia: e' la "
    "trappola della 136a, dove un operando non censito aveva spento la copia di "
    "195 carte. I quattro siti stanno o cadono insieme, e "
    "`test_i_quattro_siti_di_tratti_sono_concordi` lo pretende."
)

MOTIVO_EFFETTO = (
    "L'operando dimenticato dalla toppa 1230: quella ha reso `\"Effect: \"` in "
    "`\"Effetto: \"` alla riga 1473, ma `:4628` toglie ancora il prefisso "
    "INGLESE dal testo che finisce in `TCG_card_list.txt`. Non e' una riga a "
    "schermo -- e' l'export della lista carte -- ma e' un comportamento che la "
    "traduzione ha cambiato senza dirlo."
)


def _riga_unica(righe: list[str], ago: str) -> tuple[int, str]:
    """La riga che contiene `ago`, e **una sola**.

    Un `cerca` che aggancia in due posti e' una toppa che ne riscrive uno a
    caso: meglio fermarsi che indovinare.
    """
    # ⚠️ Il primo giro divideva il file su `\r\n`, che li' non c'e': usciva UNA
    # riga sola lunga tutto il file, e questo controllo diceva «unica» perche'
    # la divisione era fallita. Trentasei toppe con l'intero sorgente dentro
    # `cerca`. Un controllo di unicita' su un elenco di uno non prova niente:
    # la sua premessa va provata separatamente.
    if len(righe) < 1000:
        raise SystemExit("il file e' stato diviso in %d righe: la divisione e'"
                         " fallita, e ogni controllo qui sotto sarebbe cieco"
                         % len(righe))
    trovate = [(n, r) for n, r in enumerate(righe, 1) if ago in r]
    if len(trovate) != 1:
        raise SystemExit("«%s»: %d righe, ne serviva 1 -> %s"
                         % (ago, len(trovate), [n for n, _ in trovate]))
    return trovate[0]


def main() -> int:
    percorso = percorsi.SORGENTE_HSP / FILE
    righe = percorso.read_text(encoding="cp932").splitlines()

    nuove = []
    for inglese, italiano in ETICHETTE.items():
        ago = 's@tcg += "%s"' % inglese
        _, riga = _riga_unica(righe, ago)
        nuove.append({"file": FILE, "cerca": riga,
                      "sostituisci": riga.replace('"%s"' % inglese,
                                                  '"%s"' % italiano),
                      "motivo": MOTIVO_ETICHETTA})

    for ago in ['s@tcg += "%s"' % BITS_EN,
                'instr(carddetailneffbk@tcg, 0, "%s")' % BITS_EN,
                'instr(rtvaln2, 0, "%s")' % BITS_EN,
                'sreplace bits@tcg, bits@tcg, "%s", ""' % BITS_EN]:
        _, riga = _riga_unica(righe, ago)
        nuove.append({"file": FILE, "cerca": riga,
                      "sostituisci": riga.replace('"%s"' % BITS_EN,
                                                  '"%s"' % BITS_IT),
                      "motivo": MOTIVO_BITS})

    _, riga = _riga_unica(righe, 'sreplace s@tcg, s@tcg, "Effect: ", ""')
    nuove.append({"file": FILE, "cerca": riga,
                  "sostituisci": riga.replace('"Effect: "', '"Effetto: "'),
                  "motivo": MOTIVO_EFFETTO})

    bersaglio = percorsi.PROGETTO / "toppe.jsonl"
    esistenti = {json.loads(r)["cerca"] if isinstance(json.loads(r)["cerca"], str)
                 else tuple(json.loads(r)["cerca"])
                 for r in bersaglio.read_text(encoding="utf-8").splitlines()
                 if r.strip()}
    da_scrivere = [t for t in nuove if t["cerca"] not in esistenti]
    if not da_scrivere:
        print("niente da aggiungere: le %d toppe ci sono gia'" % len(nuove))
        return 0

    with bersaglio.open("a", encoding="utf-8") as scrittura:
        for toppa in da_scrivere:
            scrittura.write(json.dumps(toppa, ensure_ascii=False) + "\n")
    print("toppe aggiunte: %d   (ne erano gia' presenti %d)"
          % (len(da_scrivere), len(nuove) - len(da_scrivere)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
