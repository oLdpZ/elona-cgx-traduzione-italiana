# -*- coding: utf-8 -*-
"""52a, lotto `ai-tabelle`: le sei tabelle di testo di custom_ai.hsp, piu' il menu.

Le tabelle sono il SESTO punto cieco misurato oggi (`scratchpad/tabelle_en.py`):
73 voci che nessun conteggio vedeva, perche' stanno in un'assegnazione di array
e arrivano a schermo per indice, da righe che di letterali non ne hanno.

⚠️⚠️ **Una delle sette non si tocca, e il motivo e' misurato.** `AITextData(0, 6)`
sono le dodici classi, e `custom_ai.hsp:493` e `:508` le CONFRONTANO con
`cdatan(CDATAN_CLASS, …)`, che porta la chiave INGLESE: la scrivono come
letterale nudo `action.hsp:13670`-`:13703` e `command.hsp:4591`-`:4626`, e la
rileggono `chara.hsp:2875`-`:2962`, `ai.hsp:2546`, `calculation.hsp:888`, `:953`,
`:992`, `action.hsp:5704`, `:5723`, `chara_func.hsp:5010`. Tradurla lascerebbe
l'IA senza piu' nessuna classe da riconoscere. E' la lezione della 46a sulle
stringhe che il giocatore DIGITA, in forma nuova: **quel che serve a un confronto
non e' testo, e si guarda il sito.** Le classi restano inglesi e vanno in
`rinviate.jsonl`.
💡 Le tabelle 4 e 5 si confrontano anche loro (19 e 9 siti) ma sono numeri: non
c'e' niente da tradurre e non c'e' niente da rompere.

Il vocabolario e' quasi tutto **gia' deciso altrove**, e questo lotto lo va a
prendere invece di inventarlo:

    gli stati       le piastrelle dell'HUD, `text.hsp:69`-`:102`
    le qualita'     la serie di `text.hsp:106` (bad/common/great/miracle/godly)
    Gauge           «Barra», `action.hsp:11476`, `buff.hsp:530`, `:845`
    Buff            «Potenziamento», gia' reso per «Boost»
    Shift Core      «nucleo di transizione», `db_item.hsp:138463`
    Do Nothing      «Non fare nulla», `skill.hsp:1228`
    Blind           «Cecita'», `command.hsp:1848`
    MPoison         «mana avvelenato», `skill.hsp:1069`
    pet             «alleato», come in tutto `custom_tweaks.hsp`

Le colonne sono strette e il corpo e' 11 (`font …, 13 - en * 2`, con `en` = 1):
Chi 100 px, Condizione 125, Confronto 135, Valore 100, Azione 132.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\custom_ai.hsp")
FILE = "custom_ai.hsp"

# ⚠️ `splitlines()` e non `split("\n")`: il sorgente ha fine riga CRLF, e un
# `cerca` che si porta dietro il `\r` non aggancia niente — `applica` risponde
# «non esiste piu'» come se upstream avesse riscritto la riga.
TESTO = SORGENTE.read_bytes().decode("cp932").splitlines()


def riga(n: int) -> str:
    return TESTO[n - 1]


# (numero di riga, resa, motivo)
LOTTO = [
    (
        22,
        '\tAIStatusNames(0, 0) = "Terrore", "Atrofia", "Vincolo", "Sangue", "Cecita\'", '
        '"Plagio", "Tremore", "Confusione", "Stordimento", "Furia", "Gravita\'", '
        '"Follia", "Jujitsu", "Metallo", "Mana avvelenato", "Olio", "Paralisi", '
        '"Veleno", "Sonno", "Umidita\'", "Esitazione", "NULL"',
        "I ventuno stati che l'IA puo' controllare, e sono gli STESSI che l'HUD "
        "disegna nelle piastrelle: le rese vengono tutte da `text.hsp:69`-`:102` "
        "(«Terrore» :100, «Atrofia» :101, «Vincolo» :102, «Sangue» :87, «Plagio» "
        ":84, «Tremore» :86, «Confusione» :99, «Stordimento» :71, «Furia» :72, "
        "«Follia» :88, «Jujitsu» :79, «Metallo» :76, «Olio» :92, «Paralisi» :97, "
        "«Veleno» :69, «Sonno» :95, «Umidita'» :91, «Esitazione» :85). ⭐ Le tre "
        "che li' non c'erano stanno altrove e non sono state inventate: «Cecita'» "
        "da `command.hsp:1848` («Blind status»), «Gravita'» da `skill.hsp:789`, "
        "«Mana avvelenato» da `skill.hsp:1069` («Target MP-damage/MPoison»). "
        "⚠️ Vanno nella colonna «Valore», 100 px a corpo 11: la piu' lunga e' "
        "«Mana avvelenato» (15), sotto le 17 che ci stanno. `NULL` e' il "
        "sentinella di fine tabella e non si tocca: `:3145` lo confronta.",
    ),
    (
        24,
        '\tAITextData(0, 0) = "Non impostato", "Attacca (mischia)", "Attacca (a distanza)", '
        '"Allontanati", "Avvicinati", "E", "Non fare nulla", "Usa il nucleo", '
        '"Fa\' come vuoi", "NULL"',
        "Le azioni che l'alleato puo' eseguire. ⭐ Forma verbale in tutte, perche' "
        "«Do Nothing» era gia' reso «Non fare nulla» in `skill.hsp:1228` e sono "
        "istruzioni, non etichette. «Move (Away)»/«(Forward)» diventano "
        "«Allontanati»/«Avvicinati»: l'italiano ha il verbo che l'inglese deve "
        "fare con la parentesi, e sono piu' corte dell'originale. "
        "⚠️ «Usa il nucleo» e non «Usa il nucleo di transizione» (il nome pieno, "
        "`db_item.hsp:138463`): la colonna «Azione» e' 132 px a corpo 11, cioe' "
        "circa 23 caratteri, e il nome pieno ne fa 28. Nel menu delle azioni non "
        "c'e' nessun altro nucleo, quindi non si confonde con niente. "
        "«Attacca (a distanza)» fa 20 caratteri, la piu' lunga che ci sta.",
    ),
    (
        25,
        '\tAITextData(0, 1) = "Non impostato", "Se stesso", "Bersaglio", "Alleato", '
        '"Tu", "Nemico", "NULL"',
        "Su chi si valuta la condizione. Le rese vengono dal gioco: «Bersaglio» da "
        "`text.hsp:135`, «Alleato» da `text.hsp:32`, «Tu» da `text.hsp:1932` "
        "(«Player»). ⚠️ Colonna «Chi», 100 px a corpo 11: la piu' lunga e' "
        "«Non impostato» (13). 💡 «Self» e' l'alleato che sta eseguendo la "
        "tattica, non il giocatore — «Se stesso», non «Tu», che qui e' un'altra "
        "voce della stessa tabella e li distingue.",
    ),
    (
        26,
        '\tAITextData(0, 2) = "Non impostato", "HP", "MP", "Distanza", "Potenziamento", '
        '"Barra", "Classe", "Stato", "Probabilita\'", "Numero", "Qualita\'", "NULL"',
        "Che cosa si guarda. ⭐ «Barra» per «Gauge» e' gia' del progetto: "
        "`action.hsp:11476` rende «You need 100% power gauge» con «Serve la barra "
        "al 100%», e `buff.hsp:530` e `:845` dicono «Barra ferma» e «Barra cala». "
        "«Potenziamento» per «Buff» e' la resa gia' data a «Boost». «HP» e «MP» "
        "non si traducono, come in tutto il progetto. «Classe» da "
        "`command.hsp:10504`, «Stato» da `command.hsp:1197`. "
        "⚠️ Colonna «Condizione», 125 px: la piu' lunga e' «Potenziamento» (13).",
    ),
    (
        27,
        '\tAITextData(0, 3) = "Non impostato", "<", ">", "=", "!=", ">=", "<=", "NULL"',
        "I comparatori. C'e' una parola sola da tradurre — i sei segni sono segni "
        "in ogni lingua. ⚠️ Ci sta comodamente: la colonna «Confronto» e' la piu' "
        "larga delle cinque, 135 px.",
    ),
    (
        31,
        '\tAITextData(0, 7) = "Nessuna", "Scadente", "Comune", "Eccellente", '
        '"Eccezionale", "Celestiale", "Speciale", "NULL"',
        "Le qualita' degli oggetti, e sono la serie che `text.hsp:106` ha gia' "
        "fissato: bad→scadente, common→comune, great→eccellente, "
        "miracle→eccezionale, godly→celestiale, special→speciale. ⭐ La "
        "corrispondenza non e' parola per parola ed e' il punto: «Good» qui e' il "
        "gradino che il resto del gioco chiama «common», e «Unique» quello che "
        "chiama «special». Tradurli alla lettera («Buono», «Unico») avrebbe dato "
        "due nomi nuovi a due qualita' che il giocatore legge gia' cosi' "
        "nell'inventario. «Nessuna» da `init.hsp:371`. "
        "⚠️ Colonna «Valore», 100 px: la piu' lunga e' «Eccezionale» (11).",
    ),
    # ---- la schermata: intestazioni, voci e righe di aiuto ----
    (
        1088,
        '\ts = "Istruzioni tattiche", strhint3b',
        "Il titolo della finestra. ⚠️ L'inglese fa 21 caratteri, l'italiano 19.",
    ),
    (
        1090,
        '\tdisplay_topic "Chi", wx + 28, wy + 30',
        "L'intestazione della prima colonna. ⭐ «Chi» e non «Soggetto» o «Entita'»: "
        "la colonna e' 100 px e sotto ci vanno «Se stesso», «Bersaglio», "
        "«Alleato», «Tu», «Nemico» — che sono tutte risposte alla domanda «chi». "
        "L'inglese ne fa 6, l'italiano 3.",
    ),
    (
        1091,
        '\tdisplay_topic "Condizione", wx + 128, wy + 30',
        "Seconda colonna, 125 px. Dieci caratteri contro i nove dell'inglese: e' "
        "l'unica intestazione che cresce, ed e' di uno.",
    ),
    (
        1092,
        '\tdisplay_topic "Confronto", wx + 253, wy + 30',
        "Terza colonna, la piu' larga (135 px). Nove caratteri contro dieci.",
    ),
    (
        1093,
        '\tdisplay_topic "Valore", wx + 388, wy + 30',
        "Quarta colonna, 100 px. Sei caratteri contro cinque.",
    ),
    (
        1094,
        '\tdisplay_topic "Azione", wx + 488, wy + 30',
        "Quinta colonna, 132 px. Sei caratteri come l'inglese.",
    ),
    (
        1095,
        '\ts = "Istruisci il tuo alleato"',
        "La riga sotto il titolo. «pet» e' «alleato» in tutto il progetto — "
        "`custom_tweaks.hsp` dice «Gli alleati muoiono per sempre» e «gli alleati "
        "temporanei» — e «Teach» qui e' l'atto di dare istruzioni, non "
        "d'insegnare una magia (quello e' la voce di menu sotto).",
    ),
    (1097, '\tlistn(0, 0) = "Configura"', "Prima voce del menu."),
    (
        1098,
        '\tlistn(0, 1) = "Insegna una magia o un\'abilita\'."',
        "Seconda voce. Qui «Teach» e' davvero insegnare.",
    ),
    (1099, '\tlistn(0, 2) = "Esci"', "Terza voce."),
    (
        1140,
        '\t\ts = "Cambia l\'IA del tuo alleato."',
        "La riga d'aiuto della prima voce. «IA» e' deciso dalla 50a.",
    ),
    (
        1145,
        '\t\ts = "Insegna al tuo alleato una magia o un\'abilita\' nuova."',
        "La riga d'aiuto della seconda voce.",
    ),
    (1150, '\t\ts = "Esci dal menu."', "La riga d'aiuto della terza voce."),
]


def main() -> None:
    toppe, problemi = [], []
    for n, resa, motivo in LOTTO:
        cerca = riga(n)
        quante = TESTO.count(cerca)
        if quante == 0:
            problemi.append(f":{n} non esiste nel sorgente: {cerca!r}")
            continue
        if cerca == resa:
            problemi.append(f":{n} la resa e' identica all'inglese")
            continue
        for c in resa:
            if ord(c) > 0x7F:
                problemi.append(f":{n} carattere fuori ASCII in una toppa: {c!r} — "
                                "le toppe non passano da accenti.py")
        toppa = {"file": FILE, "cerca": cerca, "sostituisci": resa, "motivo": motivo}
        if quante > 1:
            # ⭐ La forma della 50a: la riga sta identica in piu' routine del
            # pannello dell'IA (lo stesso titolo, le stesse cinque intestazioni,
            # la stessa riga sotto il titolo), e la resa e' la stessa ovunque.
            # Senza questo `applica` si fermerebbe sull'ambiguita', giustamente.
            toppa["tutte"] = True
            toppa["motivo"] += (f" ⭐ `tutte`: la riga sta identica in {quante} punti "
                               "del pannello dell'IA, che sono le schermate dei sette "
                               "menu — stesso titolo, stesse intestazioni di colonna. "
                               "La resa e' la stessa in tutte.")
        toppe.append(toppa)

    if problemi:
        for p in problemi:
            print("⚠️ ", p)
        raise SystemExit("lotto non scritto")

    uscita = REPO / "lavoro" / "_toppe-ai-tabelle.jsonl"
    dati = "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in toppe).encode("utf-8")
    uscita.write_bytes(dati)
    print(f"{len(toppe)} toppe in {uscita}")

    esito = subprocess.run(
        [sys.executable, str(REPO / "scratchpad" / "aggiungi-toppe.py"), str(uscita)],
        cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    print(esito.stdout.strip() or esito.stderr.strip())


if __name__ == "__main__":
    main()
