# -*- coding: utf-8 -*-
"""52a, lotto `tcg-carte`: le parole chiave sulle carte del gioco di carte.

⚠️ **Il tetto qui e' la CARTA, non la finestra**: `gcopy 7, 0, 0, 72, 96` la
disegna 72x96 px, e le parole chiave si impilano dal basso (`pos x@tcg, y@tcg +
72 - 7 * p@tcg`, sette px per riga) a corpo **9** — `font …, 10 + en - en * 2`
con `en` = 1. Col metro del progetto (6,6 px a corpo 13, cioe' 4,57 a corpo 9)
ci stanno **quindici caratteri**, e l'inglese piu' lungo — «Regeneration» — ne
fa dodici.

⭐ **Otto delle trentadue sono STATI che il gioco ha gia' nominato altrove**, e
sono le stesse rese appena messe nel pannello dell'IA: «Confusione», «Veleno»,
«Follia», «Paralisi», «Sangue», «Gravita'» vengono dalle piastrelle dell'HUD
(`text.hsp:69`-`:102`). Un nome di stato che cambia da una schermata all'altra e'
un difetto anche quando tutt'e due le rese sono buone.

⚠️ **Le altre ventiquattro sono parole chiave di un gioco di carte**, cioe' un
vocabolario che il progetto non aveva mai toccato. Dove l'italiano dei giochi di
carte ha gia' un nome affermato lo si usa («Vigilanza», «Travolgere», «Legame
vitale»); dove quel nome non ci sta in 72 px si sceglie l'immagine invece della
lettera, ed e' dichiarato voce per voce.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\tcg.hsp")
FILE = "tcg.hsp"
TESTO = SORGENTE.read_bytes().decode("cp932").splitlines()

DAGLI_STATI = ("Lo stesso stato che l'HUD disegna nelle piastrelle "
               "(`text.hsp:69`-`:102`) e che il pannello dell'IA usa da oggi: "
               "un nome di stato non puo' cambiare da una schermata all'altra.")

LOTTO = [
    # --- gli stati, gia' decisi altrove
    (887, "Silenzio", "«Silenced» e' l'unico degli otto che le piastrelle non "
                      "portano: il silenzio qui e' la carta che non puo' usare le "
                      "sue capacita'. Sostantivo come gli altri sette."),
    (891, "Confusione", DAGLI_STATI + " `text.hsp:99`."),
    (895, "Veleno", DAGLI_STATI + " `text.hsp:69`."),
    (990, "Gravita'", DAGLI_STATI + " `skill.hsp:789`."),
    (994, "Sangue", DAGLI_STATI + " `text.hsp:87`."),
    (1006, "Paralisi", DAGLI_STATI + " `text.hsp:97`."),
    (1022, "Follia", DAGLI_STATI + " `text.hsp:88`."),
    # --- le parole chiave del gioco di carte
    (909, "Rigenerazione", "13 caratteri, i piu' lunghi del lotto: 59 px sui 72 "
                           "della carta. L'inglese ne fa 12."),
    (913, "Corazza", "«Armored» e' la carta che para: il sostantivo dice la cosa "
                     "senza il participio, che in italiano avrebbe voluto un "
                     "genere («Corazzato» o «Corazzata»?) che la carta non ha."),
    (917, "Volo", "La parola dei giochi di carte, e la piu' corta di tutte."),
    (921, "Minaccia", "«Intimidate» e' la carta che non puo' essere bloccata dai "
                      "deboli. ⭐ «Minaccia» e non «Intimidazione» (13): dice la "
                      "stessa cosa in otto caratteri ed e' la parola che i giochi "
                      "di carte usano in italiano per questo effetto."),
    (925, "Portata", "«Reach»: colpisce chi vola. E' il nome italiano affermato."),
    (929, "Legame vitale", "«Lifelink»: il danno inflitto cura. Nome italiano "
                           "affermato, 13 caratteri, 59 px."),
    (933, "Travolgere", "«Trample»: il danno in eccesso passa oltre. Nome "
                        "italiano affermato."),
    (937, "Anticipo", "«First Strike»: colpisce per primo. ⚠️ Il nome italiano "
                      "affermato e' «Attacco improvviso», che fa 18 caratteri e "
                      "sfonda la carta di venti px. «Anticipo» (8) tiene "
                      "l'immagine — colpire prima — e ci sta; «Colpo primo» "
                      "sarebbe stato ambiguo con «Doppio colpo» qui sotto."),
    (941, "Doppio colpo", "«Dual Strike»: colpisce due volte."),
    (945, "Tocco letale", "«Deathtouch»: qualunque danno uccide. Il nome italiano "
                          "affermato e' «Tocco micidiale» (15, al limite esatto "
                          "dei 72 px): «letale» dice la stessa cosa con tre "
                          "caratteri di margine."),
    (949, "Critico", "«Critical»."),
    (953, "Raffica", "«Windfury»: attacca due volte in un turno. ⚠️ «Furia del "
                     "vento» fa 15 caratteri e arriva esatto sui 72 px, senza "
                     "margine per il bordo che `bmes` disegna intorno alle "
                     "lettere. «Raffica» dice il colpo ripetuto e ne fa sette."),
    (957, "Vigilanza", "«Vigilance»: attacca senza abbassare la guardia. Nome "
                       "italiano affermato."),
    (961, "Difensore", "«Defender»: non puo' attaccare."),
    (965, "Sdoppia", "«Split». ⭐ Il verbo lo dice gia' il gioco: `chara_func.hsp"
                     ":8751` annuncia «si sdoppia!». «Sdoppiamento» (12) ci "
                     "stava, ma le altre parole chiave d'azione sono verbi "
                     "(«Travolgere»), e questa e' quel che la carta FA."),
    # ⚠️ `:969` «Immune» NON c'e', ed e' voluto: in italiano si scrive uguale, e
    # una toppa che sostituisce una parola con se stessa e' rumore che ogni
    # sessione futura dovrebbe rileggere per capire che non fa niente. Il conteggio
    # dei nudi continuera' a contarla fra le «da fare»: non e' una dimenticanza,
    # e' la stessa scelta di «Abnormal» e «HP» della 51a.
    (973, "Cavaliere", "«Rider»: la carta che cavalca. ⭐ «Cavalcatore» (11) e' "
                       "piu' letterale ma non e' parola d'uso; «Cavaliere» e' "
                       "quel che il giocatore si aspetta di leggere."),
    (977, "Barriera", "«Barrier»."),
    (981, "Schivata", "«Evasion». ⭐ «Schivata» e non «Elusione»: e' la parola che "
                      "il progetto usa gia' per schivare un colpo."),
    (986, "Condanna", "«Deathword»: la parola che uccide. ⚠️ Tradurlo alla "
                      "lettera («Parola di morte», 15) arrivava esatto al bordo. "
                      "«Condanna» tiene la sentenza che la parola pronuncia."),
    (998, "Veleno", DAGLI_STATI + " ⚠️ Seconda occorrenza, sulla carta in campo "
                    "invece che in mano: la riga e' identica, quindi una toppa "
                    "sola con `tutte` le prende tutt'e due."),
    (1002, "ESPLODE!", "«EXPLODING!»: le maiuscole e il punto esclamativo sono "
                       "dell'inglese e restano, perche' sono il tono."),
    (1014, "Gelo", "«Frozen»: la carta congelata non agisce. Sostantivo breve "
                   "come gli altri stati."),
    (1018, "Fantasma", "«Ghost»."),
    # --- le tre righe d'aiuto, che stanno FUORI dalla carta
    (1089, "F [Mazzo]", "⚠️ Queste tre non stanno sulla carta ma accanto al "
                        "tavolo (`pos holderix@tcg(0) + …`), e sono le uniche del "
                        "lotto col tasto in testa. Il tasto NON si traduce — e' "
                        "quello che si preme — e «View» sparisce, perche' la "
                        "parentesi quadra da sola dice gia' che si guarda."),
    (1092, "G [Cimitero]", "Le carte scartate. ⭐ «Cimitero» e' il nome che i "
                           "giochi di carte usano in italiano, e «Grave» qui e' "
                           "quello, non una tomba."),
    (1095, "S [Arrenditi]", "13 caratteri come l'inglese. Imperativo perche' e' "
                            "un comando che il giocatore da'."),
]


def main() -> None:
    toppe, problemi = [], []
    for n, parola, motivo in LOTTO:
        cerca = TESTO[n - 1]
        # la resa cambia SOLO il letterale: il resto della riga (i tre colori,
        # l'indentazione) si tiene identico, altrimenti la toppa e' un'altra riga
        inizio = cerca.index('"')
        fine = cerca.index('"', inizio + 1)
        resa = cerca[:inizio + 1] + parola + cerca[fine:]
        quante = TESTO.count(cerca)
        if quante == 0 or cerca == resa:
            problemi.append(f":{n} non aggancia niente")
            continue
        for c in resa:
            if ord(c) > 0x7F:
                problemi.append(f":{n} carattere fuori ASCII: {c!r}")
        if len(parola) > 15 and n < 1089:
            problemi.append(f":{n} «{parola}» fa {len(parola)} caratteri: "
                            "sfonda i 72 px della carta")
        toppa = {"file": FILE, "cerca": cerca, "sostituisci": resa, "motivo": motivo}
        if quante > 1:
            toppa["tutte"] = True
            toppa["motivo"] += f" ⭐ `tutte`: la riga sta identica in {quante} punti."
        toppe.append(toppa)

    if problemi:
        for p in problemi:
            print("⚠️ ", p)
        raise SystemExit("lotto non scritto")

    larga = max(LOTTO, key=lambda v: len(v[1]))
    print(f"{len(toppe)} toppe | la piu' lunga: «{larga[1]}» "
          f"({len(larga[1])} caratteri, {round(len(larga[1]) * 4.57)} px sui 72)")

    uscita = REPO / "lavoro" / "_toppe-tcg-carte.jsonl"
    dati = "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in toppe).encode("utf-8")
    uscita.write_bytes(dati)

    esito = subprocess.run(
        [sys.executable, str(REPO / "scratchpad" / "aggiungi-toppe.py"), str(uscita)],
        cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    print(esito.stdout.strip() or esito.stderr.strip())


if __name__ == "__main__":
    main()
