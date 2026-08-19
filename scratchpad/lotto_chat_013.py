# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-013.jsonl: le ultime schede dell'informatore —
il Passo di Montagna e gli uomini antichi, il boss di Remido, e la rivelazione
su chi gli passa le notizie (chat.hsp:24421-:24439).

⚠️ Le code di :24434 e :24435 ripetono parola per parola quelle di :24378 e
:24379 (la barra di potenza, i pomodori marci): sono stringhe diverse per il
dizionario, ma la stessa frase per chi legge, e vanno rese IDENTICHE.

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib

RESE = {
    # --------------------------- il Passo di Montagna e gli uomini antichi
    24421: "Nel Passo di Montagna non c'è nessun boss. Ma lo sai che cosa c'è in "
           "fondo a quella strada di montagna? Non ti stupire: pare che ci sia "
           "un insediamento di uomini dell'era della civiltà biochimica.",
    24422: "È una montagna dove da tempo immemorabile il vento d'etere si leva a "
           "chiazze, quindi non mi pare poi strano che siano sopravvissuti "
           "degli uomini antichi, quelli che alla Meshera non si sono adattati.",
    24423: "Si sono trovati anche documenti che dicono che all'epoca si studiava "
           "una forma di vita artificiale capace di generare il vento d'etere. "
           "...Eppure, fino a poco fa, restava una bella teoria che conoscevano "
           "in pochi.",
    24424: "In verità, qui fra noi... c'è andato a controllare uno pieno di "
           "curiosità e senza paura di morire. Dopo aver portato le "
           "testimonianze che confermavano la teoria, è morto per le "
           "complicazioni della malattia dell'etere.",
    24425: "Nella piazza in fondo all'insediamento pare ci fosse anche una forma "
           "di vita artificiale di livello 120. Oltre agli attacchi d'elemento "
           "magia, pare che se ti fissa la malattia dell'etere avanzi. Da come "
           "me l'hanno raccontata, non ha resistenze forti né deboli.",
    24426: "Anche sugli uomini antichi la magia moderna dovrebbe funzionare, "
           "quindi con la magia Incognito o con un set da travestimento si "
           "evita di far chiasso.",
    24427: "Sia gli uomini antichi sia la forma di vita artificiale sono fonti "
           "d'informazione preziose, quindi, per quel che mi riguarda, se puoi "
           "evitare di ammazzarli mi faresti un piacere.",
    # ----------------------------------------------------- il boss di Remido
    24431: "Il piano più profondo di Remido è un impianto di ricerca antico. Lì "
           "dorme il capo delle Meshera. Livello 120. O 130?",
    24432: "Pare che non si sposti da dove sta, e che dalle cellule che ha "
           "assorbito replichi mostri di ogni sorta. Se lo chiudi in un muro e "
           "gli togli lo spazio per tirarli fuori, lo puoi bloccare.",
    24433: "C'è anche chi dice che si rigeneri molto, ma dalle caratteristiche "
           "non mi pare così alta. ...Le due fonti non concordano: che ce ne "
           "siano di due tipi?",
    24434: "Be', se comincia a curarsi basta fargli più danno di quanto ne "
           "recupera. La via solida è portare la barra di potenza oltre il 100% "
           "e scaricargliela addosso tutti insieme coi compagni, con <Forza "
           "liberata> o con <Attacco combinato>. I compagni fuori dall'ordine "
           "di Assalto tengono da parte la barra, quindi regola i tempi.",
    24435: "Se li fai infuriare tirandogli addosso pomodori marci, natto o "
           "yogurt, il danno raddoppia; ma raddoppia anche quello che prendono, "
           "quindi va visto quanto regge la tua squadra.",
    24436: "Rigenerarsi non credo che lo faccia con la magia. Se è così, non ci "
           "si può fare niente né finendogli gli MP né con la Nebbia di "
           "silenzio.",
    24437: "Poi pare che convenga alzare la resistenza all'oltretomba. ...Su "
           "quest'altro appunto c'è scritto che ha attacchi fisici e di suono "
           "potenti? Be', meglio avere alti anche PV, DV e resistenza al suono. "
           "Lui non pare avere resistenze forti né deboli.",
    # ---------------------------------------------- da dove vengono le notizie
    24438: "Eh? Vuoi sapere da dove mi arrivano queste informazioni?",
    24439: "...C'è una tale che chiamano il demonio delle informazioni, una "
           "specie di informatrice coi fiocchi. Stavolta ho comprato da lei, "
           "quindi è roba sicura. Ma anch'io ho il mio orgoglio, e a quella "
           "donna preferisco ricorrere il meno possibile.",
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
    with io.open(radice / "lavoro" / "fase4-chat-013.jsonl", "wb") as f:
        f.write(dati)
    doppi = set("—–“”«»…・《》")
    guasti = [d["riga"] for d in voci if doppi & set(d["it"])]
    print("%d voci scritte | caratteri a due byte: %s" % (len(voci), guasti or "nessuno"))


if __name__ == "__main__":
    main()
