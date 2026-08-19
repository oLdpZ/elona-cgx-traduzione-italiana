# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-003.jsonl: *chat_unique_yayauhqui, cioe' la scena
in cui Jaldabaoth si rivela (chat.hsp:18474-:18560).

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
Gli accenti sono quelli veri: la degradazione ad apostrofo la fa applica.py.
"""
import io
import json
import pathlib

RESE = {
    18483: "Sei tutto parole! Distruggere il Sigillo Eterno ti ha portato via "
           "tanto tempo che non sei riuscito ad assorbire il potere divino del "
           "Figlio del Caos!",
    18484: "Ti sbagli su qualcosa, Tezcatlipoca. E guarda come ti hanno "
           "ridotto: che pena.",
    18485: "Cosa...?",
    18492: "Ghah... Maledetto... Scappa, Tezcatlipoca...!",
    18495: "Sia la luce.",
    18516: "Il mio nome è Jaldabaoth. Io sono un dio geloso. Non serve nessun "
           "altro dio oltre a me. E anche quel misero involucro, ormai, ha "
           "finito il suo compito.",
    18519: "Jaldabaoth...? Involucro...?",
    18520: "Questa... cosa mi possedeva, e da sempre controllava i miei "
           "pensieri. E per ingannare l'occhio degli dèi ha ordito ogni sorta "
           "di trama.",
    18521: "Non è possibile... Proprio oggi, proprio adesso: si è servito di "
           "Orphe come copertura, per distruggere il Sigillo Eterno con un "
           "corpo mortale!",
    18524: "Il mio vero corpo era tornato nel ventre di Enthumesis, la madre "
           "indegna, per sottrarle il potere divino; ma prosciugarla fino in "
           "fondo richiedeva un tempo immenso. E nell'attesa mi sono preso "
           "gioco del mondo, e ho cercato di gettare le fondamenta del Caos.",
    18525: "Irregolare, le tue mosse mi hanno intralciato e non ho potuto "
           "portarlo a termine. Ma ora che ho in mano questa potenza "
           "schiacciante, è un dettaglio da nulla...",
    18528: "Basta così... Orphe! Tu ritirati al piano di sopra!",
    18529: "Ngh... perdonatemi...!",
    18534: "Fuggite pure dove volete. Cambierà soltanto l'ordine in cui "
           "sparirete.",
    18535: "Bene... La mente ricorda, ma il corpo ha dimenticato i movimenti... "
           "Ecco dunque il potere della dea dell'oblio. Così il corpo a corpo "
           "mi è precluso: che seccatura.",
    18536: "E anche la mia riserva di potere divino si è ridotta parecchio... "
           "eppure, eppure. Basta e avanza per incenerire il mondo e i suoi "
           "dèi fragili! Inghiottirò la luce, creerò il mondo del Caos, e sarò "
           "io il Creatore... regnerò come dio unico!",
    18539: "Dio falso, stolto e arrogante... lo sai da dove viene quella forza?",
    18540: "Il potere divino degli dèi, in origine, è il desiderio dei mortali. "
           "È anima, ed è luce astrale che affiora dai corridoi di Arkasha. Tu "
           "che la calpesti non potrai mai avere in mano la luce vera!",
    18543: "E allora?",
    18546: '"Io sono Tezcatlipoca, il dio della guerra, e gli altri dèi mi '
           'hanno affidato la loro forza. Anche se questo corpo perisce, non '
           'ti lascerò fare a modo tuo! Andiamo, " + cdatan(CDATAN_NAME, '
           'CHARA_PLAYER) + "! Qui si decide tutto!"',
    18549: "Continua pure a blaterare. Per un poco starò al gioco. Sono curioso "
           "di vedere fin dove reggete.",
    18553: "Il mondo comincia a ruotare attorno a Jaldabaoth...",
}


def main():
    radice = pathlib.Path(__file__).resolve().parent.parent
    voci = []
    with io.open(radice / "lavoro" / "_chat.jsonl", encoding="utf-8") as f:
        for riga in f:
            d = json.loads(riga)
            if d["riga"] in RESE:
                d["it"] = RESE[d["riga"]]
                voci.append(d)
    mancanti = set(RESE) - {d["riga"] for d in voci}
    if mancanti:
        raise SystemExit("righe non trovate nel lotto: %s" % sorted(mancanti))
    voci.sort(key=lambda d: (d["riga"], d["occorrenza"]))
    dati = "".join(json.dumps(d, ensure_ascii=False) + "\n" for d in voci).encode("utf-8")
    with io.open(radice / "lavoro" / "fase4-chat-003.jsonl", "wb") as f:
        f.write(dati)
    print("%d voci scritte" % len(voci))
    for d in voci:
        print("  %d  %s" % (d["riga"], d["it"]))


if __name__ == "__main__":
    main()
