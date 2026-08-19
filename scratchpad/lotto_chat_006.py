# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-chat-006.jsonl: il concilio di Mikraanesis
(chat.hsp:18094-:18111) — che cos'e' davvero la dea dell'oblio, i terminali che
divorano i ricordi, la rete akashica.

Legge le voci gia' estratte da lavoro/_chat.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib

RESE = {
    18094: "Mikraanesis, che cosa è mai successo?",
    18095: "Il nostro corpo principale sta trattenendo la dea dell'oblio. No... "
           "combattendo l'abbiamo capito: quella, a rigore, non è la dea che "
           "governa l'oblio.",
    18096: "È un essere concettuale, fatto per produrre il fenomeno dell'oblio "
           "su scala di mondo... un aspetto dell'oblio che ha preso corpo in "
           "forma di divinità. Finché in questo mondo esiste un ricordo "
           "qualsiasi, insieme a esso continua a esistere il concetto di "
           "oblio: per quante volte se ne distrugga la figura di dea, la "
           "radice non si può togliere.",
    18097: '"Se il corpo principale scendesse quaggiù nella sua forma '
           'completa, ogni esistenza di quel mondo sparirebbe del tutto, nel '
           'passato e nel futuro. " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", '
           'ce l\'hai anche tu, di sicuro: una storia di cui non ricordi più '
           'il contenuto, e nemmeno il titolo. Una persona che ha dimenticato '
           'perfino di aver dimenticato. Ecco, pensa alla stessa cosa su scala '
           'di mondo, anzi di universo."',
    18098: "Adesso stiamo attaccando il corpo principale prima che scenda, e lo "
           "teniamo fermo; ma le bestie, che ne sono i terminali, non siamo "
           "riusciti a contenerle. Se continuano a divorare ricordi e a "
           "moltiplicarsi, la forza del corpo principale crescerà, e alla fine "
           "ci travolgeranno.",
    18099: "Non è possibile... Allora Gaius Vis sta per sparire...? Non c'è "
           "proprio niente che si possa fare?!",
    18100: '"Una via c\'è. " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", non è una '
           'faccenda che riguarda altri. Se questo mondo diventa un mondo '
           'dimenticato del tutto, il turno dopo è di Irva. Forse non reggerà '
           'qualche secolo; forse nemmeno qualche decennio. Prima o poi, in '
           'tutto l\'universo, non resterà più nessuno che ricordi il '
           'paesaggio di Irva. Ecco perché voglio darti questo."',
    18102: "Ottieni la [rete akashica]!",
    18104: "Se nel tempo che resta riusciamo a incidere i ricordi negli "
           "osservatori di un altro mondo, la forza dell'avversario ne esce "
           "molto ridotta. Quello che ti ho appena dato è un meccanismo "
           "d'interferenza: serve a diffondere sui registri akashici, "
           "attraverso la luce astrale, la Gaius Vis che hai visto con i tuoi "
           "occhi. La pubblichi in rete, cresce il numero di chi ne conserva "
           "il ricordo, e l'oblio del mondo rallenta.",
    18105: '"Ma può usarlo un mortale che ha residenza nel mondo in cui lo usa, '
           'non un dio. E l\'effetto arriva solo a chi sta vicino al luogo del '
           'registro, cioè a chi vi è legato da vicino. Ecco perché serviva '
           'qualcuno come " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ": un '
           'mortale che non sia nato a Gaius Vis, che abbia girato in lungo e '
           'in largo, e che abbia la forza di aprirsi la strada in mezzo ai '
           'branchi di bestie dell\'oblio."',
    18106: "Capisco. Ah, e io non posso usarla, perché sono uno che è passato "
           "da Gaius Vis a Irva...",
    18107: "Anche a te, Norne, resta da fare. Con pazienza, a più gente che "
           "puoi, parla alle persone del mondo di là. Per quante volte la "
           "dimentichino, continua a raccontarla, questa storia di Gaius Vis: "
           "perché è il ricordo della gente la forza che tiene in piedi un "
           "mondo.",
    18108: "Ma io alla gente di Irva l'ho già raccontata più volte. Eppure le "
           "bestie non hanno smesso di avanzare...",
    18109: "Se ha reso poco, è perché finora mancava un tramite per la rete "
           "akashica. Sta' tranquillo: la tua fatica non andrà sprecata.",
    18110: '"...Bene, scusa la chiacchierata lunga, " + cdatan(CDATAN_NAME, '
           'CHARA_PLAYER) + ". Forse per te è stata un po\' ostica. E però '
           'ancora una cosa, un\'ultima: è un altro discorso."',
    18111: "Il vero risveglio del Caos si avvicina. Tornare al Sigillo Eterno e "
           "chiudere la partita: questo è il tuo destino.",
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
    with io.open(radice / "lavoro" / "fase4-chat-006.jsonl", "wb") as f:
        f.write(dati)
    print("%d voci scritte" % len(voci))
    for d in voci:
        print("  %d  %s" % (d["riga"], d["it"][:95]))


if __name__ == "__main__":
    main()
