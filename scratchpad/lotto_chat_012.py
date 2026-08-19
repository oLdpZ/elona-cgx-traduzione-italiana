# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-012.jsonl: le schede dell'informatore su Tempio
Caos, Fortezza Meccanica, Valle degli Inferi e i pericoli di Remido
(chat.hsp:24384-:24407).

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib

RESE = {
    # ----------------------------------------- il boss del Tempio Caos: Exossil
    24384: "Exossil l'ala del caos, che domina il Tempio Caos, è di livello 60. "
           "Pare che scappi in volo tirando magie di caos e oscurità "
           "amplificate dall'equipaggiamento.",
    24385: "Ah, giusto. Un mago che l'ha sfidato prima si è preso una Nebbia di "
           "silenzio, non ha più potuto usare la magia e non ha combinato "
           "niente. E pare che tiri anche una maledizione che abbassa le "
           "resistenze, quindi anche se non pensi di usare la magia portati "
           "dietro bacchette o pergamene di luce sacra. Con un Velo sacro di "
           "livello alto si può anche prevenire.",
    24386: "È un non morto, è un dio e sta sospeso in aria, quindi con armi che "
           "portino gli incantamenti giusti per queste tre cose dovresti "
           "cavartela. Non pare avere resistenze particolarmente forti né "
           "particolarmente deboli.",
    # ------------------------------- il boss della Fortezza Meccanica: Metal Vesda
    24390: "Stando ai dati... ehi, non chiedermi come li ho avuti. Metal Vesda, "
           "il drago di fuoco meccanico schierato nella Fortezza Meccanica, è "
           "di livello 70.",
    24391: "L'arma principale è a pallettoni, quindi combattendo da lontano i "
           "danni calano. Pare che faccia anche attacchi a irradiazione di "
           "energia, ma anche quelli, con un po' di resistenza alla magia, non "
           "fanno paura.",
    24392: "Però sembra che monti un congegno di autodistruzione. Quando lo "
           "metti alle strette, prima bagnalo: così non può autodistruggersi.",
    24393: "È parecchio duro, quindi se intorno hai nemici d'intralcio conviene "
           "forse togliere prima quelli. Al fuoco pare che resista in modo "
           "anomalo, quindi meglio attaccarlo con altri elementi.",
    # ------------------------------ il boss della Valle degli Inferi: l'Anubis
    24397: "La Valle degli Inferi? L'Anubis che sta lì, il signore della morte, "
           "è di livello 80. E anche di recente pare che dei tombaroli ci "
           "abbiano rimesso le penne.",
    24398: "Ci sono andati corazzati d'armatura pesante, e sono stati quasi "
           "sterminati da un'arma molto perforante. La difesa non sembra "
           "servire granché. E chiude la distanza col teletrasporto, quindi "
           "dicono che sia difficile anche scappare.",
    24399: "Se vuoi affrontarlo, alza la schivata con la magia Piuma o con le "
           "pozioni di piuma, e abbattilo in fretta concentrando gli attacchi, "
           "se no è dura. Se non usi attacchi fisici, un'altra via è spargere "
           "una Nebbia d'oscurità.",
    24400: "Da quel che ho sentito, resiste all'oscurità e alla magia. È pur "
           "sempre un dio, quindi se hai un'arma che picchia forte sugli dèi "
           "dovrebbe funzionare.",
    # ----------------------------------------------- i pericoli di Remido (1)
    24404: "Quel che può fare da ostacolo è... sì, questo.",
    24405: "L'<Apparato di comunicazione mobile> di Yerles è di livello 100. "
           "Dicono che nelle Rovine di Remido ne abbiano messi in campo due. Se "
           "non ti riconosce come nemico non dovrebbe combattere, ma tanto per "
           "sapere.",
    24406: "Si dice che ferisca con manipolatori a distanza affilati, e che si "
           "difenda con scariche elettriche e armamenti di tiro di ogni sorta. "
           "Ha contromisure contro la magia dappertutto, quindi le magie "
           "d'elemento magia non fanno quasi niente.",
    24407: "In combattimento pare che non si avvicini troppo. Be', è ovvio: in "
           "origine è un apparato di comunicazione. Se ti tocca combatterlo, "
           "meglio prendere le distanze col teletrasporto e fare fuori prima "
           "gli altri nemici.",
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
    with io.open(radice / "lavoro" / "fase4-chat-012.jsonl", "wb") as f:
        f.write(dati)
    doppi = set("—–“”«»…・《》")
    guasti = [d["riga"] for d in voci if doppi & set(d["it"])]
    print("%d voci scritte | caratteri a due byte: %s" % (len(voci), guasti or "nessuno"))


if __name__ == "__main__":
    main()
