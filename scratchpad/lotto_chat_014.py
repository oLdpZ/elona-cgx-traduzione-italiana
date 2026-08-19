# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-014.jsonl: le ultime quattro schede
dell'informatore — Aikage e gli spiriti del caos, il drago a nove teste al largo
di Valm, le armi biologiche di Zanan, il demone di Mayroon
(chat.hsp:24443-:24469).

Con questo lotto il PNG e' chiuso: chat.hsp:24236-:24469, il menu e sedici
schede.

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib

RESE = {
    # ---------------------------- i pericoli della Culla del Caos: Aikage
    24443: "Pare che ci sia un piano dove un ninja dal volto di demone si è "
           "accampato insieme a un grosso esercito di spiriti del caos. Se è "
           "Aikage, il ninja dalla maschera demoniaca, allora è di livello 155.",
    24444: "Dicono che sia bravo negli attacchi ravvicinati mordi-e-fuggi e "
           "negli indebolimenti. Con un Velo sacro o con le bacchette di luce "
           "sacra a scopo preventivo si sta tranquilli.",
    24445: "Se lo colpisci a metà si sdoppia, ma tanto vale continuare a "
           "picchiare e stenderlo. E poi, pare che abbia alta la resistenza al "
           "suono.",
    24446: "Gli spiriti del caos sono tanti, quindi meglio non affrontarli tutti "
           "insieme. O ti teletrasporti in un angolo della stanza e resisti lì, "
           "o spargi una cortina di fumo e sfondi da una parte. Con un modo per "
           "recuperare gli MP e la resistenza al caos alzata, secondo me non ci "
           "sono problemi.",
    # ------------------------------- il boss delle Acque di Valm: il nove teste
    24450: "Al largo di Valm ci sono delle isolette, e da lì pare che alcuni "
           "isolani siano scappati. A sentire le loro testimonianze, la "
           "situazione somiglia parecchio al \\\"mito del drago a nove teste\\\".",
    24451: "Il drago a nove teste sarà sul livello 160. C'è chi riferisce che a "
           "intervalli irregolari emetta onde mentali che alzano il grado di "
           "follia. Se non ti porti dietro qualche corno di unicorno resti "
           "bloccato.",
    24452: "Conviene abbatterlo in fretta, ma con le resistenze al suono e "
           "mentale basse la cosa ti si ritorce contro. Ci sono anche mostri a "
           "mucchi, quindi se ignorarli e puntare dritto al drago si possa fare "
           "dipende dalla tua potenza d'attacco e da quanti corni di unicorno "
           "hai. Dovrebbe resistere all'elemento magia, quindi attaccalo con "
           "altro.",
    24453: "Se la follia ti divora, mettiti a mollo con calma alle terme e "
           "curati. In Tyris del Sud sono famose quelle di Arcbelc, della "
           "Locanda del Fumo e della Pipa, e di Ruoza.",
    # --------------------------------------- le armi biologiche di Zanan
    24457: "Ce ne sono di tanti tipi, quindi a dire soltanto \\\"arma "
           "biologica\\\" non si capisce quale, vorrei dire; ma... ah, no. È "
           "quel posto dove hanno provato a usare le Meshera e hanno scatenato "
           "un disastro biologico?",
    24458: "Su quel posto da sempre si sentivano solo voci nere, e alla fine "
           "pare che sia crollato. Dicono anche che ultimamente esagerassero "
           "ancora di più, per nascondere la fuga di un soggetto compatibile "
           "prezioso.",
    24459: "Ah, i soggetti da esperimento sono di livello 150. Dicono che non "
           "abbiano capacità di movimento, quindi eliminandoli uno per uno non "
           "si fa fatica.",
    24460: "Anche la rigenerazione è riprodotta male e pare che dipenda dalla "
           "magia, quindi se non riesci a sfondare basta metterli in silenzio. "
           "Se ti ci metti, meglio avere un po' di resistenza all'oltretomba e "
           "un po' di difesa.",
    24461: "Ci saranno anche gli impiegati che non hanno fatto in tempo a "
           "scappare, trasformati in mostri; ma a differenza dei soggetti da "
           "esperimento non sono stati messi a punto per il combattimento, "
           "quindi non sono granché.",
    24462: "Però ci dovrebbe essere un congegno che sparge gas nervino per "
           "sedare le rivolte. Se è in funzione, ci vorrà anche una discreta "
           "resistenza ai nervi.",
    # ------------------------------------------- il demone: Lazasye
    24466: "Le informazioni arrivano da un avventuriero che era nella spedizione "
           "precedente. Lazasye il demone della distruzione è di livello 160. "
           "Pare che piombi addosso in un attimo e scateni attacchi ad area di "
           "gelo e oltretomba.",
    24467: "E poi, dicono che consumi una gran quantità di MP per tirare un "
           "attacco ad area potentissimo. Raccontava che quelli con la "
           "resistenza alla magia bassa sono stati spazzati via senza lasciare "
           "traccia, e con loro il terreno.",
    24468: "Uno che si è preso una cosa del genere è tornato a nuoto: gli "
           "avventurieri sono gente dura. Pare che dopo il colpo anche Lazasye "
           "fosse parecchio consumato, quindi non ne tirerà più di quattro, no? "
           "Puoi anche svuotargli gli MP, ma forse la partita si chiude prima.",
    24469: "Si porta dietro spiriti del caos, e pare che Lazasye ne evochi anche "
           "altri. Per sicurezza tieni pronto un modo per recuperare MP.",
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
    with io.open(radice / "lavoro" / "fase4-chat-014.jsonl", "wb") as f:
        f.write(dati)
    doppi = set("—–“”«»…・《》")
    guasti = [d["riga"] for d in voci if doppi & set(d["it"])]
    print("%d voci scritte | caratteri a due byte: %s" % (len(voci), guasti or "nessuno"))


if __name__ == "__main__":
    main()
