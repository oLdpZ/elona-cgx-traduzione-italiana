# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-015.jsonl: le schede dell'informatore sui quattro
demoni e sugli unimorti (chat.hsp:24473-:24512).

⚠️ A :24484 il giapponese dice レベル154 e l'inglese «level 153». Decide il
giapponese: 154.

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib

RESE = {
    # ---------------------------------- il demone di Eulderna: Inqtual
    24473: "Il demone che sta invadendo la capitale, Inqtual il demone della "
           "vendetta, è di livello 160. Sembra il tipo che si scatena con gli "
           "attacchi fisici. Rispondi con Scudo sacro e Piuma.",
    24474: "Pare che sia bravo anche nel lavaggio del cervello. Se tieni alta la "
           "volontà con la magia o con le pozioni di Concentrazione, il danno "
           "si attenua.",
    24475: "Visto che i maghi di corte non sono riusciti ad abbatterlo, deve "
           "avere un'alta resistenza alla magia. E pare che a volte alzi la "
           "barra di potenza dei ribelli soffiando sul loro desiderio di "
           "vendetta.",
    24476: "Quei ribelli sembrano fatti soprattutto di cavalieri evocatori e "
           "arcieri magici di Eulderna, ma ho sentito che il potere del demone "
           "li porta al livello 145, quindi non abbassare la guardia. Occhio "
           "soprattutto ai cavalieri evocatori: se li lasci fare, possono "
           "evocare mostri fastidiosi.",
    # ---------------------------------- il demone di Kikkasu: Roatonis
    24480: "Di quel fatto, l'unico sopravvissuto si è svegliato solo l'altro "
           "giorno. A parte lui, che era immune, sono morti tutti di malattia: "
           "e per noi è stata una fortuna.",
    24481: "Stando alla sua testimonianza, Roatonis il demone della pestilenza è "
           "di livello 160. Pare che lanci uno sguardo che fa avanzare la "
           "malattia dell'etere, quindi forse conviene portarsi dietro anche "
           "qualche cristallo curativo.",
    24482: "E poi pare che usi anche la Sentenza di morte, quindi si sta più "
           "tranquilli con un Velo sacro come prevenzione e con bacchette o "
           "pergamene di luce sacra per toglierla.",
    24483: "In giro per la città vagano non morti di ogni tipo, e dicono che "
           "siano tutti rinforzati fino al livello 140.",
    24484: "Accanto a Roatonis c'è anche una regina savant di livello 154, e "
           "insieme rinforzano gli zombi e ne assorbono le forze.",
    24485: "La regina savant ha alta la resistenza alla magia, ma è debolissima "
           "al fuoco. Meglio ridurre prima gli zombi, poi abbattere la regina "
           "savant, e per ultimo Roatonis.",
    24486: "Su Roatonis in sé non è che funzioni granché, ma con un attacco "
           "potente d'elemento fuoco le cose si fanno più facili.",
    # ------------------------- il demone che resta nella Culla: Egelveil
    24490: "I demoni comparsi qua e là sono stati spazzati via, ma secondo la "
           "tradizione ne resta ancora uno. Forse dorme nella Culla del Caos.",
    24491: "Egelveil il demone dei vincoli è di livello 180. Si dice che blocchi "
           "i movimenti con la costrizione e con le ragnatele.",
    24492: "Se la combatti, meglio cancellare le ragnatele con la magia "
           "dell'acqua o con una cortina di fumo, arrivarle addosso e chiudere "
           "in fretta. Nello stato di costrizione gli attacchi normali non si "
           "schivano nemmeno con un DV alto, quindi ne devi reggere parecchi. "
           "Conviene pensare anche a tagliare la linea di tiro con muri o "
           "cortine di fumo.",
    24493: "Fra lei e i suoi sottoposti attaccano con elementi di ogni sorta, ma "
           "conviene alzare soprattutto la resistenza al suono. Volendo, si può "
           "anche rialzarla con una pozione di resistenza.",
    # ----------------------------- la squadra speciale di Lothria: Lankata
    24497: "Sai che la squadra speciale di Lothria punta al Sigillo Eterno? I "
           "membri sono di livello 164, e chi li guida, Lankata il fulmine del "
           "cielo azzurro, è di livello 168.",
    24498: "Lankata e i soldati potenziati hanno alta la resistenza alla magia, "
           "quindi le magie d'elemento magia sono una cattiva idea. I soldati "
           "potenziati sono duri, perché si rigenerano anche, e verrebbe voglia "
           "di lasciarli per ultimi; ma sono bravi a tirarsi addosso il nemico "
           "col Richiamo d'ombra. Se tagli la linea di vista con la creazione "
           "di muri o con una cortina di fumo, non ti danno noia.",
    24499: "I membri regolari della squadra speciale hanno solo tiro e magia di "
           "cura, e non sono una vera minaccia. Secondo me conviene togliere "
           "prima i vecchi veterani, che caricano senza paura di morire. "
           "Comunque, visto che vanno soprattutto di attacco fisico normale, "
           "conviene puntare su PV e DV.",
    24500: "Ah, giusto. Stando alle informazioni, quelli riducono al minimo gli "
           "scontri per non consumarsi. Se sfondi a forza e tiri dritto, non è "
           "che si mettano a inseguirti.",
    24501: "E ancora una cosa. I dettagli non li so, ma pare che nella missione "
           "di Lankata rientri anche la ricerca di qualcuno. Se lo lasci in "
           "vita potrebbe succedere qualcosa, ma... be', anche abbatterlo non "
           "crea problemi.",
    # ------------------------------------------------- i quattro unimorti
    24505: "L'asso nella manica dei burattinai di Eulderna... sono i quattro "
           "unimorti. I burattinai sono spariti insieme alle armi non morte "
           "antiche che avevano catturato, ma ci sono avvistamenti nella Culla "
           "del Caos. Gli unimorti sono quattro: il re, la regina, il fante e "
           "il jolly, tutti di livello 175.",
    24506: "Il re è specializzato in potenza d'attacco fisico e rigenerazione. "
           "Ci vuole tempo per abbatterlo, ma se lo lasci scatenare i danni si "
           "allargano. Detto al contrario: se lo butti giù presto, respiri.",
    24507: "La regina è del tipo di retroguardia e non ha grande potenza "
           "d'attacco, ma si rigenera molto: meglio lasciarla per ultima.",
    24508: "Il fante va soprattutto di attacchi d'oltretomba ordinari, ma "
           "cancella anche tutti i potenziamenti, e quando lo metti alle "
           "strette spara a raffica attacchi magici ad area potentissimi. È "
           "quello da togliere per primo, concentrando la potenza di fuoco "
           "anche a costo di consumare la barra.",
    24509: "Il jolly è un tipo fastidioso: si teletrasporta, tira gelo, fulmine "
           "e Rallentamento, e fa anche cure ad area. A volerlo togliere per "
           "primo resiste e scappa, quindi tanto vale lasciarlo per dopo.",
    24510: "Nessuno dei quattro ha punti deboli particolari nelle resistenze. "
           "Reggono bene anche il fuoco, che di solito è il punto debole dei "
           "non morti. E per giunta il jolly pare avere alta anche la "
           "resistenza alla magia.",
    24511: "Se ti tocca combatterli sul serio, la lotta sarà dura. Forse "
           "conviene ritirarsi al piano di sopra ogni volta che ne abbatti uno.",
    24512: "Puoi anche scappare al piano di sotto e tirare dritto, ma allora è "
           "certo che ci rimettono quelli che vengono dopo. Se pensi di poterli "
           "trattenere, o se pensi che il male vada tagliato alla radice... "
           "decidi tu.",
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
    with io.open(radice / "lavoro" / "fase4-chat-015.jsonl", "wb") as f:
        f.write(dati)
    doppi = set("—–“”«»…・《》")
    guasti = [d["riga"] for d in voci if doppi & set(d["it"])]
    print("%d voci scritte | caratteri a due byte: %s" % (len(voci), guasti or "nessuno"))


if __name__ == "__main__":
    main()
