# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-item-005.jsonl e le due toppe di his2().

`item.hsp:4258`-`:4324`. Quinto lotto: quel che il cibo incantato fa alle
abilita', piu' i due messaggi della gravidanza (la «Fase 2»).

⚠️⚠️ **DUE DELLE NOVE RIGHE NON SONO TRADUCIBILI DAL DIZIONARIO**, ed e' la
TERZA volta che questa famiglia si presenta dopo `proc.hsp:11481` (36a) e
`proc.hsp:24107` (39a). `:4291` e `:4294` compongono

    his2(cc) + your2(cc) + " " + skillname(enc) + " develops."

e `his2()` (`init.hsp:1881`) **non ha nessun `lang()`**: restituisce il
letterale nudo `"your"` per il giocatore e `name(EntityID)` per chiunque altro.
Non e' morfologia — porta il nome — quindi `funzioni.py` la classifica come
contenuto e `verifica` pretende che resti nella resa; ma il ramo del giocatore,
che e' il caso normale, stampera' `your` in inglese per sempre. E l'italiano non
ha uno slot dove «your» e «il putit» leggano tutt'e due.

La strada e' quella gia' battuta: **rinvio piu' toppa**, che riporta la riga
alla forma del ramo giapponese — `skillname(enc) + "が発達した。"`, cioe' senza
possessore. ⚠️ Le toppe girano **dopo** il dizionario e non passano da
`degrada`, quindi il loro testo si scrive gia' con l'apostrofo.

⭐ E il confronto che si legge da solo: `:4269` e `:4272` dicono le stesse due
parole inglesi — «develops» e «deteriorates» — ma **senza** `his2()`, e infatti
si traducono dal dizionario come tutte le altre. La differenza fra una riga
traducibile e una da toppare non sta nel testo: sta nelle funzioni che porta.

⭐ `:4258` copiata da `action.hsp:6012` e `proc.hsp:12060`, stesso giapponese.

⚠️ I quattro giapponesi delle abilita' sono tutti diversi e l'inglese ne fonde
due coppie, quindi le rese si tengono distinte:
参考になる «c'e' da imparare» / 発達した «si sviluppa» / 回復した «si ristabilisce»
contro よくわからなくなった / 衰えた / 消耗した.
"""
import io
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from strumenti import accenti

# (riga, inglese) -> italiano.  Per le dinamiche l'italiano e' l'espressione HSP intera.
RESE = {
    (4258, " stop time."):                           # …は時を止めた。  <- action.hsp:6012
        'name(cc) + " ferma il tempo."',
    (4269, " develops."):                            # …の参考になる！
        'skillname(enc) + " fa un passo avanti!"',
    (4272, " deteriorates."):                        # …がよくわからなくなった。
        'skillname(enc) + " fa un passo indietro."',
    (4301, " is restored."):                         # …が回復した。
        'skillname(enc) + " si ristabilisce."',
    (4304, " is exhausted."):                        # …が消耗した。
        'skillname(enc) + " si logora."',
    (4319, "[Phase 2 progress  %]"):                 # [フェイズ2進捗率：…％]
        '"[Fase 2, avanzamento " + sintyoku + " %]"',
    (4324, "[HAPPY BIRTHDAY!!] Phase 2 completed."):  # [HAPPY BIRTHDAY！！]　フェイズ2が完了した。
        "[HAPPY BIRTHDAY!!] La Fase 2 è completa.",
}

# firma -> (motivo breve), per rinviate.jsonl
RINVIATE = {
    "8c1985d82be531ee1c856f0714c363328a9ea962": 4291,
    "e16d5cd8fb6dbf11ec3e9fabd0e7dad359bdf32f": 4294,
}

MOTIVO = (
    "item.hsp:{riga}. **Non e' una resa mancante: e' una riga che il dizionario non puo' "
    "aggiustare**, ed e' la terza della famiglia dopo proc.hsp:11481 (36a) e proc.hsp:24107 "
    "(39a). L'inglese e' `his2(cc) + your2(cc) + \" \" + skillname(enc) + \" {verbo}.\"`, e "
    "`his2()` (`init.hsp:1881`) **non ha nessun `lang()`**: restituisce il letterale nudo "
    "`\"your\"` per il giocatore e `name(EntityID)` per chiunque altro. Non e' morfologia — "
    "porta il nome, ed e' per questo che `funzioni.py` la classifica come contenuto e "
    "`verifica` pretende che resti nella resa — ma il ramo del giocatore, che e' il caso "
    "normale, stampera' **`your` in inglese per sempre**, qualunque cosa scriva il dizionario. "
    "⚠️ E l'italiano non ha uno slot dove «your» e «il putit» leggano tutt'e due: `his2()` "
    "restituisce un possessivo in un caso e un nome proprio nell'altro. 💡 La strada e' la "
    "toppa, che riporta la riga alla forma del ramo giapponese (`skillname(enc) + \"が{jp}\"`, "
    "cioe' senza possessore). ⭐ E la prova che il difetto sta nelle FUNZIONI e non nel testo: "
    "`item.hsp:{gemella}` dice la stessa parola inglese senza `his2()` e si traduce dal "
    "dizionario. Fatta nella 69a insieme al rinvio."
)

TOPPE = [
    {
        "riga": 4291,
        "cerca": '\t\t\t\t\ttxt lang(skillname(enc) + "が発達した。", his2(cc) + your2(cc) + " " + skillname(enc) + " develops.")',
        "sostituisci": '\t\t\t\t\ttxt lang(skillname(enc) + "が発達した。", skillname(enc) + " si sviluppa.")',
        "verbo": "develops",
        "jp": "発達した。",
        "gemella": 4269,
    },
    {
        "riga": 4294,
        "cerca": '\t\t\t\t\ttxt lang(skillname(enc) + "が衰えた。", his2(cc) + your2(cc) + " " + skillname(enc) + " deteriorates.")',
        "sostituisci": '\t\t\t\t\ttxt lang(skillname(enc) + "が衰えた。", skillname(enc) + " si indebolisce.")',
        "verbo": "deteriorates",
        "jp": "衰えた。",
        "gemella": 4272,
    },
]

USCITA = "fase4-item-005.jsonl"
RADICE = pathlib.Path(__file__).resolve().parent.parent
SORGENTE = pathlib.Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\item.hsp")


def main():
    voci = []
    with io.open(RADICE / "lavoro" / "_item.jsonl", encoding="utf-8") as f:
        for riga in f:
            d = json.loads(riga)
            chiave = (d["riga"], d["en"])
            if chiave in RESE:
                d["it"] = RESE[chiave]
                voci.append(d)

    mancanti = set(RESE) - {(d["riga"], d["en"]) for d in voci}
    if mancanti:
        raise SystemExit("chiavi non trovate nel lotto: %s" % sorted(mancanti))

    voci.sort(key=lambda d: (d["riga"], d["occorrenza"]))
    dati = "".join(json.dumps(d, ensure_ascii=False) + "\n" for d in voci).encode("utf-8")
    with io.open(RADICE / "lavoro" / USCITA, "wb") as f:
        f.write(dati)

    # ⚠️ Il `cerca` di una toppa e' fatto di righe INTERE del sorgente PINNATO e va
    # letto con .splitlines(), o il \r del CRLF resta in coda e non aggancia niente
    # (lezione della 53a). Qui lo si prova contro il sorgente prima di scrivere.
    righe = SORGENTE.read_bytes().decode("cp932").splitlines()
    for t in TOPPE:
        vera = righe[t["riga"] - 1]
        if vera != t["cerca"]:
            raise SystemExit("toppa :%d - il `cerca` non e' la riga del sorgente:\n  %r\n  %r"
                             % (t["riga"], t["cerca"], vera))
        if righe.count(t["cerca"]) != 1:
            raise SystemExit("toppa :%d - il `cerca` aggancia %d righe, non una"
                             % (t["riga"], righe.count(t["cerca"])))

    nuove = [{"file": "item.hsp", "cerca": t["cerca"], "sostituisci": t["sostituisci"],
              "motivo": MOTIVO.format(riga=t["riga"], verbo=t["verbo"], jp=t["jp"],
                                      gemella=t["gemella"])}
             for t in TOPPE]
    with io.open(RADICE / "lavoro" / "toppe-item-his2.jsonl", "w",
                 encoding="utf-8", newline="\n") as f:
        for t in nuove:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")

    rinvii = [{"firma": firma, "file": "item.hsp",
               "en": next(t for t in TOPPE if t["riga"] == riga)["verbo"],
               "rinviata_a": "nessuna fase: risolta da toppa (item.hsp:%d, applicata nella 69a)" % riga,
               "motivo": MOTIVO.format(riga=riga,
                                       verbo=next(t for t in TOPPE if t["riga"] == riga)["verbo"],
                                       jp=next(t for t in TOPPE if t["riga"] == riga)["jp"],
                                       gemella=next(t for t in TOPPE if t["riga"] == riga)["gemella"])}
              for firma, riga in RINVIATE.items()]
    with io.open(RADICE / "lavoro" / "rinviate-item-his2.jsonl", "w",
                 encoding="utf-8", newline="\n") as f:
        for r in rinvii:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    guasti = {it: sorted(accenti.doppi_byte_cp932(it)) for it in RESE.values()
              if accenti.doppi_byte_cp932(it)}
    testo_toppe = "".join(t["sostituisci"] for t in TOPPE)
    if accenti.doppi_byte_cp932(testo_toppe.replace("が発達した。", "").replace("が衰えた。", "")):
        raise SystemExit("caratteri a due byte nel testo italiano delle toppe")
    print("%d voci scritte in lavoro/%s" % (len(voci), USCITA))
    print("caratteri a due byte: %s" % (guasti or "nessuno"))
    print("2 toppe provate contro il sorgente pinnato: agganciano una riga sola ciascuna")
    for d in voci:
        print("   :%-6d %s" % (d["riga"], d["it"]))
    for t in TOPPE:
        print("   :%-6d TOPPA -> %s" % (t["riga"], t["sostituisci"].strip()))


if __name__ == "__main__":
    main()
