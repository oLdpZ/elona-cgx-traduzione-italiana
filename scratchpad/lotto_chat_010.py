# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-010.jsonl: le prime quattro schede dell'informatore
sui boss (chat.hsp:24328-:24353) — la Torre Rovente, il Castello Antico, la
grotta dei morti, i pericoli di Lesimas.

⚠️ A :24330 l'inglese di monte SCAMBIA i due nomi: dice «focus your attacks on
Corgon first while using teleportation to keep Quruiza at bay», ma il giapponese
dice l'opposto — テレポートでコルゴンを翻弄しつつ、先にクルイツゥアを集中攻撃 —
ed e' l'unico dei due che sta in piedi, perche' la riga prima ha appena spiegato
che Corgon e' il piu' duro e il piu' lento. Decide il giapponese.

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib

RESE = {
    # ------------------------------------------------------- la Torre Rovente
    24328: "La Torre Rovente è nelle mani di una coppia di sposi. Stando a chi "
           "li ha sfidati prima di te, la moglie, Quruiza dall'occhio finto, è "
           "di livello 24, e il marito, Corgon il drago d'acciaio, di livello "
           "16.",
    24329: "Pare che Quruiza scappi in giro tirando magie di gelo e oscurità. "
           "Ecco: per venire a capo della Torre Rovente non basta la resistenza "
           "al fuoco, ci vuole anche un po' di resistenza al gelo e "
           "all'oscurità.",
    24330: "Corgon è un drago, quindi è molto più duro della moglie, ma a "
           "quanto pare si limita ad avvicinarsi e a menare, e si muove piano. "
           "Meglio tenere Corgon a bada col teletrasporto e concentrare prima "
           "gli attacchi su Quruiza, no?",
    24331: "Il corpo a corpo sarà difficile, quindi con un attacco a distanza "
           "potente le cose filano più lisce. Vivono nella Torre Rovente, "
           "quindi al fuoco resistono tutti e due in modo esagerato; ma Corgon "
           "regge bene anche il fulmine e la magia.",
    # ----------------------------------------------------- il Castello Antico
    24335: "Stando alle mie informazioni, Wynan, il signore del Castello "
           "Antico, è di livello 25. Ha un'arma potente d'oltretomba, ma per lo "
           "più scappa in giro tirando magie di gelo e oscurità. Se vuoi "
           "sfidarlo, meglio avere un po' di resistenza a oltretomba, gelo e "
           "oscurità.",
    24336: "Lui in sé si difende male, e pare che resista solo all'oltretomba; "
           "ma i pezzi degli scacchi che si porta dietro ti tagliano la strada. "
           "Se non fai fuori il <Re>, continua a chiamare nemici e finisci per "
           "consumarti.",
    24337: "Se lo trasformi in un altro mostro con una bacchetta di mutamento "
           "di creatura o una pozione di mutazione, basta un turno. Se non "
           "passa, allora fuori il <Re> in fretta, concentrando gli attacchi.",
    # ---------------------------------------------------- la grotta dei morti
    24341: "Vai alla grotta dei morti? Che sprezzo del pericolo. Stando a uno "
           "che è tornato scappando, Issizzle l'aberrazione oscura è di livello "
           "28.",
    24342: "Pare che si teletrasporti in continuazione tirando magie di gelo e "
           "oscurità. La magia gli viene amplificata dall'equipaggiamento, e "
           "diceva che la potenza è fuori misura. Se non alzi bene la "
           "resistenza al gelo e all'oscurità rischi di morire sul colpo. Se "
           "non basta, prova anche con le pozioni di resistenza.",
    24343: "Lo sfidante diceva anche di aver risposto con oscurità, oltretomba "
           "e nervi, e che non gli facevano quasi niente. Se avessi un'arma che "
           "picchia forte sugli dèi e sui non morti sarebbe un'altra storia, ma "
           "inutile chiedere quel che non c'è.",
    # ------------------------------------------------------ i pericoli di Lesimas
    24347: "Gira voce che una squadra di assassini di Zanan stia invadendo "
           "Lesimas. Sono di livello 25, ma cancellano la propria presenza e si "
           "mimetizzano otticamente: una squadra invisibile.",
    24348: "Se scendi in Lesimas ti assaltano di sicuro. Si avvicinano in un "
           "attimo con un passo speciale, quindi tenerli a distanza sarà "
           "difficile.",
    24349: "Sono gente da paura, ma con la magia o la pergamena di Percezione "
           "oggetti si capisce dove sono, e se li bagni con la magia dell'acqua "
           "o con una pozione l'invisibilità salta. Se hai un equipaggiamento "
           "che fa vedere le cose invisibili, meglio di così non si può.",
    24350: "Pare che la squadra si divida in più gruppi, quindi anche dopo "
           "averne battuto uno non abbassare la guardia. ...E poi: se fra loro "
           "c'è una donna con una maschera bianca, sta' in guardia. Qui fra "
           "noi: pare che ci sia in mezzo un'assassina fuori di testa, raccolta "
           "dalla casa imperiale di Zanan.",
    24351: "Alsapia la maschera bianca è di livello 35. Non è invisibile, ma "
           "dicono che schivi gli attacchi normali come se ballasse, e che "
           "chiuda la partita con contraccolpi tremendi. Se le voci sono vere "
           "contrattacca perfino alle frecce e ai proiettili: una donna "
           "spaventosa.",
    24352: "Se ti tocca combatterla, attaccala con quel che non si può "
           "schivare: magie e abilità. Un'altra via è metterle addosso lo stato "
           "di \\\"costrizione\\\", così gli attacchi normali non li schiva più.",
    24353: "Se non riesci a costringerla, ai compagni che attaccano di forza "
           "conviene ordinare la difesa. Come si ordina? Con la bandiera di "
           "comando tutti insieme, oppure uno per uno con l'abilità Ordini "
           "tattici. Ah, giusto: la squadra di assassini, Alsapia compresa, non "
           "pare avere resistenze di elemento particolari.",
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
    with io.open(radice / "lavoro" / "fase4-chat-010.jsonl", "wb") as f:
        f.write(dati)
    print("%d voci scritte" % len(voci))
    doppi = set("—–“”«»…・《》")
    for d in voci:
        if doppi & set(d["it"]):
            print("  ⚠️ caratteri a due byte in %d" % d["riga"])
    print("caratteri a due byte: nessuno" if not any(doppi & set(d["it"]) for d in voci) else "")


if __name__ == "__main__":
    main()
