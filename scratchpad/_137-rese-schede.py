"""Le rese del lotto C: le 72 schede di carta scritte a mano.

⚠️ La tabella e' indicizzata per **numero di riga del sorgente**, e l'inglese
non si ricopia mai a mano: lo script legge il lotto estratto e ci mette dentro
l'italiano. Ricopiare `en` vorrebbe dire riagganciare una voce a un monte che
non e' quello su cui la resa e' stata scritta, e `applica_a_righe` lo rifiuta --
ma solo dopo che il lavoro e' stato fatto due volte.

Il vocabolario e' quello del ramo dinamico e del lotto B:
    N.???   Rarita':   Effetto:   Tratti:   [Carta comando]
e gli innesti sono quelli di `carte.INNESTI`, cioe' il glossario della 136a.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strumenti import percorsi  # noqa: E402

A_CAPO = "\\n"

RESE = {
886: "Pozione di Evoluzione    N.???   o di Degenerazione?  Rarita':Nessuna"
     + A_CAPO + "[Carta comando]" + A_CAPO
     + "Effetto: evolvi una tua carta bersaglio in una da +1 di costo (max 9).",
931: "    N.???   birra molto forte  Rarita':Nessuna" + A_CAPO
     + "[Carta comando]" + A_CAPO + "Effetto: ottieni 1 mana extra.",
937: "Pane Sbuffo Sbuffo   N.???   pane sbuffoso  Rarita':Nessuna" + A_CAPO
     + "[Carta comando]" + A_CAPO
     + "Effetto: dai il Pane Sbuffo Sbuffo a 1 tua carta.",
944: "Cristallo di Cura  N.???   pozione di cura strapagata  Rarita':Nessuna"
     + A_CAPO + "[Carta comando]" + A_CAPO
     + "Effetto: cura 2 danni al giocatore.",
950: "Spada di Teschio   N.???   lama d'osso dozzinale  Rarita':Nessuna"
     + A_CAPO + "[Carta comando] " + A_CAPO
     + "Effetto: infliggi 2 danni alla carta bersaglio.",
956: "Palla Mostro   N.???   pokeball tarocca  Rarita':Nessuna" + A_CAPO
     + "[Carta comando] " + A_CAPO
     + "Effetto: rendi schiava la carta bersaglio con 1 di vita.",
962: "Magistus   N.???   e' solo una bomba  Rarita':Nessuna" + A_CAPO
     + "[Carta comando] " + A_CAPO + "Effetto: infliggi 1 danno a ogni carta.",
1003: "<Spadille>    N.???   e' solo una pala  Rarita':Nessuna" + A_CAPO
      + "[Costa almeno 1] [Riutilizzabile]" + A_CAPO
      + "Effetto: BONK sulla carta bersaglio, danni pari all'attacco.",
2739: "Bomba di Carta  N.???   carta  Rarita': Comune" + A_CAPO + "[Kamikaze]"
      + A_CAPO + "Effetto: Grido di battaglia: infliggi 3 danni a un nemico e"
      + " pesca 1 carta.",
2777: "Tofu Fritto  N.???   tofu fritto  Rarita':Nessuna" + A_CAPO
      + "Effetto: Grido di battaglia: dai il Tofu Fritto a 1 tua carta.",
2792: "Spaghetti  N.???   spaghett  Rarita': pasta" + A_CAPO
      + "Effetto: ti tremano le mani.",
3339: "Bambole Biscotto  N.???   golem magoguerriera  Rarita':Nessuna" + A_CAPO
      + "Effetto: nessuno.",
4066: "Carta-Risveglio QUICK   N.???   mazin arciere  Rarita':Nessuna" + A_CAPO
      + "[Carta comando]" + A_CAPO + "Effetto: rimanda Leold nella tua mano.",
4072: "Carta-Risveglio ARTS    N.???   mazin mago  Rarita':Nessuna" + A_CAPO
      + "[Carta comando]" + A_CAPO
      + "Effetto: infliggi 2 danni all'avversario.",
4078: "Carta-Risveglio BUSTER  N.???   mazin guerriero  Rarita':Nessuna"
      + A_CAPO + "[Carta comando]" + A_CAPO
      + "Effetto: infliggi 2 danni alla carta bersaglio.",
4085: "Carta-Risveglio EXTRA   N.???   mazin magoguerriero  Rarita':Nessuna"
      + A_CAPO + "[Carta comando] [Scartata se non giocata] " + A_CAPO
      + "Effetto: infliggi 1 danno a ogni carta.",
4246: "  N.???   calzini  Rarita':perche'?" + A_CAPO
      + "Effetto: tutti in campo prendono -1/-1, tranne <Kuroya> che prende"
      + " +1/+1." + A_CAPO
      + "          Se ce l'hai in mano quando vinci, ti prendi i calzini"
      + " avversari.",
4276: "Impatto di Ganesa  N.???   spirito primordiale  Rarita':Nessuna"
      + A_CAPO + "[Carta comando]" + A_CAPO
      + "Effetto: scatena un possente Impatto di Ganeshin!",
4305: "Fiamma di Suzaku  N.???   spirito di fiamma  Rarita':Nessuna" + A_CAPO
      + "[Carta comando]" + A_CAPO + "Effetto: fa risorgere Suzaku.",
4391: "Libro di Rachel N.1    Bella favola scritta da Rachel.  Rarita':Molta"
      + A_CAPO + "Effetto: Grido di battaglia: pesca 2 carte da 1 di costo."
      + A_CAPO + "        Se hai giocato tutt'e 4 i libri, Renton ha +6/+6"
      + " (ovunque sia).",
4397: "Libro di Rachel N.2    Bella favola scritta da Rachel.  Rarita':Molta"
      + A_CAPO + "Effetto: Grido di battaglia: ottieni +2 mana. Pesca 1 carta."
      + A_CAPO + "        Se hai giocato tutt'e 4 i libri, Renton ha +6/+6"
      + " (ovunque sia).",
4403: "Libro di Rachel N.3    Bella favola scritta da Rachel.  Rarita':Molta"
      + A_CAPO + "Effetto: Grido di battaglia: +1 di vita a ogni tua carta."
      + " Pesca 1 carta." + A_CAPO
      + "        Se hai giocato tutt'e 4 i libri, Renton ha +6/+6 (ovunque"
      + " sia).",
4409: "Libro di Rachel N.4    Bella favola scritta da Rachel.  Rarita':Molta"
      + A_CAPO + "Effetto: Grido di battaglia: indebolisci di 1 i nemici."
      + " Pesca 1 carta." + A_CAPO
      + "        Se hai giocato tutt'e 4 i libri, Renton ha +6/+6 (ovunque"
      + " sia).",
4467: "Tezcatl-Moyocoyani    Specchio d'ossidiana.  Rarita':Antica" + A_CAPO
      + "Effetto: trasforma le carte del tuo campo in immagini di"
      + " Tezcatlipoca.",
4475: "Ehecatlipoca-Nahuaque    Strana sfera fumosa.  Rarita':Antica" + A_CAPO
      + "Effetto: rendi 0/0 la carta nemica bersaglio.",
4483: "Monantzin-Yaotzin    Hmmmmm.  Rarita':Antica" + A_CAPO
      + "Effetto: al prossimo turno ottieni +4 mana.",
4491: "Tepeyollotl-Icnoacatzintli    Gemma pulsante.  Rarita':Antica" + A_CAPO
      + "Effetto: pesca Tezcatlipoca ovunque sia, e dagli +2/+2.",
4546: "Immagine di Tezcatlipoca    Cavolo!  Rarita':Non molta" + A_CAPO
      + "Effetto: nessuno.",
4715: "<Rito di Evocazione>    Carta dubbia.  Rarita':Nessuna" + A_CAPO
      + "Effetto: distruggi una carta della tua mano per tentare di evocare"
      + " TUWEN.",
4794: "<Rito di Evocazione RITORNA>    Carta dubbia.  Rarita':Nessuna"
      + A_CAPO + "Effetto: ruba +1/+1 dalle carte in campo per tentare di"
      + " evocare TUWEN.",
4867: "<Rito di Evocazione: Signore della Piramide>    Carta dubbia. "
      + " Rarita':Nessuna" + A_CAPO
      + "Effetto: distruggi la tua mano per evocare TUWEN.",
5400: "Valchiria N.???    Guerriera Roran  Rarita':Molta" + A_CAPO + "Effetto: ",
5409: "Bimbetta N.???    Guerriera Roran  Rarita':Molta" + A_CAPO + "Effetto: ",
5415: "Strega N.???    Guerriera Roran  Rarita':Molta" + A_CAPO + "Effetto: ",
5424: "Principessa Bianca N.???    Magoguerriera Roran  Rarita':Molta" + A_CAPO
      + "Effetto: ",
5434: "Signorina Vampira N.???    Magoguerriera Roran  Rarita':Molta" + A_CAPO
      + "Tratti:  Legame vitale Rigenerazione" + A_CAPO + "Effetto: ",
5446: "Sorella Gatta? N.???    Ladra Roran  Rarita':Molta" + A_CAPO
      + "Tratti:  Anticipo Impeto" + A_CAPO + "Effetto: ",
5453: "Sorella Yandere N.???    Ladra Roran  Rarita':Molta" + A_CAPO
      + "Effetto: ",
5462: "Sorella Maggiore Piccola N.???    Arciera Roran  Rarita':Molta" + A_CAPO
      + "Tratti:  Anticipo" + A_CAPO + "Effetto: ",
5468: "Sorella Maggiore Estiva N.???    Arciera Roran  Rarita':Molta" + A_CAPO
      + "Effetto:",
5478: "Gwen la Guerriera Innocente N.???    Roran  Rarita':Molta" + A_CAPO
      + "Effetto: ogni volta che Gwen viene uccisa torna nella tua mano con"
      + " +2/+2.",
5850: "Stacy  N.???   zombi guerriera  Rarita':Nessuna" + A_CAPO
      + "Tratti: Difensore Rigenerazione" + A_CAPO + "Effetto: nessuno.",
5857: "Baroque  N.???   zombi ladra  Rarita':Nessuna" + A_CAPO
      + "Tratti: Raffica" + A_CAPO
      + "Effetto: Grido di battaglia: infliggi 2 danni a 2 nemici a caso.",
5863: "Thanatos  N.???   zombi spadona  Rarita':Nessuna" + A_CAPO
      + "Tratti: Doppio colpo" + A_CAPO
      + "Effetto: Grido di battaglia: infliggi 3 danni a un nemico a caso.",
5867: "Romanesque  N.???   zombi sacerdotessa  Rarita':Nessuna" + A_CAPO
      + "Effetto: si evolve in Regina Zombi quando uccide qualcosa.",
5913: "Spirito del Budino Super  N.???   spirito ladro  Rarita':Nessuna"
      + A_CAPO
      + "Effetto: Grido di battaglia: raddoppia i valori di questa carta.",
6018: "<Lily> la mamma di Pael  N.222   mutante guerriera  Rarita':Nessuna"
      + A_CAPO + "Effetto: la malattia di Lily e' guarita, ma un po' troppo"
      + " tardi.",
6061: "<Lily> la mamma di Pael  N.222   roran guerriera  Rarita':Nessuna"
      + A_CAPO + "Effetto: la malattia di Lily e' guarita! Ottieni 3 carte!"
      + " Grazie!",
6175: "cucciolo d'orso  N.???   orsetto piccolissimo  Rarita':Nessuna" + A_CAPO
      + "Effetto: se e' nel cimitero, tutti gli orsi hanno +1 di attacco.",
6192: "Maga Nera Ragazza (Bianca) N.???    Guerriera Roran  Rarita':Molta"
      + A_CAPO + "Effetto: ",
6370: "Infetto da Meshera  N.???   turista meshera  Rarita':Nessuna" + A_CAPO
      + "Effetto: Grido di battaglia: trasforma 1 carta del tuo mazzo in un"
      + " Meshera.",
7533: ".338 La Puta Magnum   N.???   proiettile dubbio  Rarita':Nessuna"
      + A_CAPO + "[Carta comando]" + A_CAPO
      + "Effetto: trasforma un nemico in una prostituta 1/1.",
7541: "12/70 SuperFormance-RatShot   N.???   proiettile dubbio "
      + " Rarita':Nessuna" + A_CAPO + "[Carta comando]" + A_CAPO
      + "Effetto: infliggi 1 danno e Sangue a ogni nemico non corazzato.",
7547: ".50 BMG   N.???   proiettile dubbio  Rarita':Nessuna" + A_CAPO
      + "[Carta comando]" + A_CAPO + "Effetto: evoca 1 Maga Nera Ragazza.",
7555: "7.62x15mm TT Subsonico Lentissimo   N.???   proiettile dubbio "
      + " Rarita':Nessuna" + A_CAPO + "[Carta comando]" + A_CAPO
      + "Effetto: infligge 0 danni, incredibile.",
7561: "7.62x51mm M62 Tracist   N.???   proiettile dubbio "
      + " Rarita':Nessuna" + A_CAPO + "[Carta comando]" + A_CAPO
      + "Effetto: infligge 5 danni e ci mette sopra un segnalino.",
7569: "7.62x39mm Fumble-Mind-Jujitsu  N.???   proiettile dubbio "
      + " Rarita':Nessuna" + A_CAPO + "[Carta comando]" + A_CAPO
      + "Effetto: infliggi Follia a una carta in campo a caso, 10 volte.",
7575: "5.56x45mm Magoguerriero Eulderna   N.???   proiettile dubbio "
      + " Rarita':Nessuna" + A_CAPO + "[Carta comando]" + A_CAPO
      + "Effetto: infliggi 5 danni divisi fra i nemici.",
7581: "9x39 SupaPulya-4   N.???   proiettile dubbio  Rarita':Nessuna"
      + A_CAPO + "[Carta comando]" + A_CAPO
      + "Effetto: infliggi 1 danno alla carta bersaglio, 4 volte.",
7587: "7.62x51mm Ultra Chiassoso  N.???   proiettile dubbio "
      + " Rarita':Nessuna" + A_CAPO + "[Carta comando]" + A_CAPO
      + "Effetto: Silenzio e 3 danni a un nemico.",
7593: "20/70 Fleischesser  N.???   proiettile dubbio  Rarita':Nessuna"
      + A_CAPO + "[Carta comando]" + A_CAPO
      + "Effetto: infliggi 2 danni e Sangue a 3 nemici a caso.",
7601: ".300 Backout   N.???   proiettile dubbio  Rarita':Nessuna"
      + A_CAPO + "[Carta comando]" + A_CAPO
      + "Effetto: rimanda in mano la carta bersaglio avversaria.",
7620: "Modulo Sterminio: Grido di battaglia: 3 danni a un nemico,"
      + " pesca 1 carta.",
7630: "Modulo Testa Extra: ottieni il tratto Corazza.",
7635: "Modulo Autoriparazione: Rantolo di morte: torna nel mazzo con +2/+2.",
7646: "Modulo Doppio Guaio: Grido di battaglia: evoca una copia di questa"
      + " carta.",
7656: "Modulo Braccia Potenti: ottieni il tratto Travolgere.",
7665: "Modulo Pendolare Veloce: ottieni i tratti Vigilanza e Impeto.",
7674: "Modulo Azione Possente: infliggi 5 danni a chi la controlla.",
7685: "Costume da Bagno Pericoloso: le tue carte hanno +1 di attacco.",
2038: "Sei rimasto senza carte!!!",
# ⚠️ Monte e' TRONCATO a meta' parola: «Otherwise, it's just a ston». Non e'
# un refuso che porta comportamento -- niente cerca dentro questa scheda --
# quindi la resa e' la frase intera. La scelta sta in `decisioni.md`.
2639: "Fossile Misterioso N.???    Turista Dinosauro  Rarita':Antica" + A_CAPO
      + "Effetto: devi dissotterrarlo in qualche modo per usarlo." + A_CAPO
      + "        Se no, e' solo un sasso.",
}


def main() -> int:
    lotto = percorsi.LAVORO_LOTTI / "schede-137.jsonl"
    voci = [json.loads(r) for r in lotto.read_text(encoding="utf-8").splitlines()
            if r.strip()]
    per_riga = {v["riga"]: v for v in voci}

    senza_resa = [v["riga"] for v in voci if v["riga"] not in RESE]
    if senza_resa:
        raise SystemExit("schede senza resa: %s" % senza_resa)
    inventate = [r for r in RESE if r not in per_riga]
    if inventate:
        raise SystemExit("rese per righe che non esistono nel lotto: %s"
                         % inventate)

    with lotto.open("w", encoding="utf-8") as scrittura:
        for voce in voci:
            voce["it"] = RESE[voce["riga"]]
            scrittura.write(json.dumps(voce, ensure_ascii=False) + "\n")
    print("lotto riempito: %d rese su %d schede" % (len(RESE), len(voci)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
