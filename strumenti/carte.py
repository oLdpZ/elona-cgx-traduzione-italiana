"""`tcg_mod.hsp`: le descrizioni d'effetto delle carte, un meccanismo suo.

Le 835 descrizioni non sono firme `lang()`: sono **assegnazioni a un array**,

    effdesc@tcg(TCG_EFF_NONE) = "No Effect."

quindi `estrai.siti()` non le vede e il dizionario non le raggiunge. Come per
`scene2.hsp`, la strada e' una scansione propria, un dizionario proprio e un
`--applica` che riscrive l'albero di build.

⚠️ **Il dizionario sta in `dizionario/carte/effdesc.jsonl`, in sottocartella.**
`applica.py:772` fa `DIZIONARIO.glob("*.jsonl")` -- non ricorsivo -- e per
`scene2.hsp` ha dovuto mettere uno scarto cablato. Qui lo scarto non si puo'
fare: `dizionario/tcg_mod.hsp.jsonl` esiste gia' con otto voci `lang()` vere (i
colori delle carte) che `applica` deve continuare a vedere. La sottocartella e'
la stessa soluzione di `dizionario/dati/`.

⚠️⚠️ **L'ordine di build non cambia:** `applica` rigenera l'albero da
`sorgente/` e cancella ogni iniezione, quindi

    python -m strumenti.applica
    python -m strumenti.scene --applica
    python -m strumenti.carte --applica     <- qui
    python -m strumenti.compila --eseguibile

⚠️⚠️⚠️ **E cinque righe del codice cercano un letterale DENTRO il testo delle
carte** (`tcg_skill.hsp:618`, `:4960`, `:4972`, `:5003`, `tcg.hsp:1470`). La
piu' pesante e' `:618`, che copia un effetto solo se la carta e' marcata
`TCG_SKILL_TYPE_BATTLECRY` **e** la parola compare nel testo. Le due cose non
coincidono di monte, e l'invariante da sorvegliare non e' «la resa contiene la
parola»: e' che la **partizione resti 472 / 19**. Vedi `partizione_battlecry`.
"""
import argparse
import json
import re
from pathlib import Path

from strumenti import percorsi
from strumenti.accenti import degrada

FILE = "tcg_mod.hsp"

# ⚠️ Il numero atteso batte l'avviso, perche' non chiede a nessuno di
# ricordarsi (lezione delle «35 toppe» della 96a). Se il riconoscitore ne trova
# altri, il sorgente si e' mosso e il conto va rifatto, non aggiustato.
ATTESE = 835

# ⚠️ Due delle 835 hanno l'inglese VUOTO (`TCG_EFF_PROJETP1` e `P2`, i moduli
# del PRO-JET): non c'e' niente da tradurre, e non ci sara' mai. Il bersaglio
# delle rese e' quindi 833, non 835 -- un contatore che punta a un numero
# irraggiungibile e' un cancello che non chiude mai, e quelli si imparano a
# ignorare.
TRADUCIBILI = 833

# `tcg.hsp:1473`: `talk_conv carddetailneffbk@tcg, 65` manda a capo
# `"Effect: " + effdesc@tcg(...)`, non la sola descrizione.
COLONNA_SCHEDA = 65
PREFISSO = "Effetto: "

# Il prefisso che il gioco scrive **prima** della toppa 1230: serve per misurare
# l'inglese come l'eseguibile di monte lo disegna, non come lo disegnerebbe la
# build italiana.
PREFISSO_MONTE = "Effect: "

# ⚠️⚠️ **La larghezza NON era misurata da nessuno.** `talk_conv` non spezza mai
# dentro una parola: quando la coda non ha piu' spazi la appende **senza
# guardare la colonna** (difetto di monte, 23a sessione, `diario.py`). Cosi' una
# riga puo' uscire a 81 colonne pur avendo il rientro a 65.
#
# Il soffitto non e' scelto: e' **il massimo che l'inglese di monte gia'
# disegna**, cioe' l'unica larghezza di cui si sappia che il riquadro la regge.
# Sopra quella non si sa niente, e la scelta che non puo' far danno e' stare
# sotto. `test_la_larghezza_massima_e_quella_dell_inglese` lo ricalcola dal file
# a ogni giro, cosi' non puo' invecchiare in silenzio.
LARGHEZZA_MASSIMA = 77

# ⚠️ Il soffitto VERO del riquadro nessuno l'ha mai visto a schermo: `mes`
# disegna verbatim e `tcg.hsp:3503` fa scendere il corpo da 13 a 11 sopra le
# quattro righe, ma quante ne entri prima che il testo esca dal riquadro e'
# grafica. Finche' non c'e' una schermata questo e' una **soglia d'avviso**, non
# un rifiuto: un cancello che chiede l'impossibile viene disattivato, non
# rispettato (lezione della 134a sui `{txt}`).
SOFFITTO_AVVISO = 4

# ⭐ LA RETE NON E' QUELLA DI `scene.py`. Li' `GRAFIE` cerca **inglese rimasto
# dentro l'italiano**, e prende «Ylva» scritto in una resa. Qui il guaio tipico
# non ha inglese dentro: «Grido di guerra» e' italiano, ed e' sbagliato lo
# stesso. Quindi la rete guarda **l'inglese di monte** e pretende il traducente
# canonico nella resa -- che e' anche, per costruzione, cio' che tiene in piedi
# la partizione 472 / 19 di `tcg_skill.hsp:618`.

# Gli innesti: si controllano SOLO in testa, prima dei due punti. `Sacrifice`
# in testa e' «Sacrificio:», ma a meta' frase e' il verbo «sacrifica»: un
# cancello che lo cercasse ovunque direbbe rosso su una resa giusta, e chi
# traduce imparerebbe a non guardarlo (la lezione della 70a).
INNESTI = {
    "Battlecry": "Grido di battaglia",
    "BattleCry": "Grido di battaglia",
    "Begin Phase": "Fase iniziale",
    "BeginPhase": "Fase iniziale",
    "End Phase": "Fase finale",
    "EndPhase": "Fase finale",
    "Ongoing": "Continuo",
    "Deathrattle": "Rantolo di morte",
    "DeathRattle": "Rantolo di morte",
    "Deathblow": "Colpo di grazia",
    "Sacrifice": "Sacrificio",
    "After Combat": "Dopo lo scontro",
    "AfterCombat": "Dopo lo scontro",
    "OnKill": "All'uccisione",
    "On Kill": "All'uccisione",
    "In-Hand": "In mano",
    "In Hand": "In mano",
    "InHand": "In mano",
    "OnDraw": "Alla pesca",
    "On Draw": "Alla pesca",
}

# Le ventisei parole chiave gia' a schermo nelle toppe di `tcg.hsp` da fasi.
# Queste si controllano OVUNQUE: sono sostantivi, e una seconda resa sarebbe una
# seconda traduzione della stessa parola, in un gioco dove le due si vedono
# nella stessa schermata.
#
# ⚠️⚠️ La prima versione di questa tabella ne aveva SETTE, e il buco l'ha
# trovato la prova al contrario: «Ricarica» al posto di «Rigenerazione» passava
# indisturbata perche' `Regeneration` non c'era. Una tabella incompleta non
# sbaglia, tace -- ed e' peggio, perche' il verde si legge lo stesso.
#
# ⓘ L'esposizione e' misurata sulle 835, non stimata: 23 occorrenze in tutto, e
# le parole che sarebbero rischiose (`Reach`, `Rider`, `Critical`, `Flying`,
# `Armored`) qui non compaiono mai.
PAROLE_CHIAVE = {
    "Windfury": "Raffica",
    "Trample": "Travolgere",
    "Lifelink": "Legame vitale",
    "Deathtouch": "Tocco letale",
    "Deathword": "Condanna",
    "First Strike": "Anticipo",
    "Dual Strike": "Doppio colpo",
    "Double Strike": "Doppio colpo",
    "Critical": "Critico",
    "Barrier": "Barriera",
    "Evasion": "Schivata",
    "Vigilance": "Vigilanza",
    "Defender": "Difensore",
    "Reach": "Portata",
    "Intimidate": "Minaccia",
    "Flying": "Volo",
    "Armored": "Corazza",
    "Regeneration": "Rigenerazione",
    "Rider": "Cavaliere",
    "Ghost": "Fantasma",
    "Frozen": "Gelo",
    "Silenced": "Silenzio",
    "Confused": "Confusione",
    "Poisoned": "Veleno",
    "Bleeding": "Sangue",
    "Paralysed": "Paralisi",
    "Insane": "Follia",
    "Gravity": "Gravità",
    "Graveyard": "cimitero",
    # ⓘ `Haste` e `Immune` sono parole chiave di `tcg.hsp:1539` e
    # `:1549` che le 26 toppe NON avevano tradotto: le loro etichette
    # sono ancora inglesi, come tutte quelle dei bit, che sono della
    # Fase 6. Decise qui perche' compaiono nelle descrizioni: `Immune`
    # resta com'e' (le toppe scrivono gia' «Immune alla confusione»),
    # `Haste` diventa «Impeto», nel registro di Raffica e Anticipo.
    "Haste": "Impeto",
    "Immune": "Immune",
}

# ⚠️ `Split` -> «Sdoppia» e' una parola chiave di `tcg.hsp`, e NON sta qui
# apposta: tutte e cinque le sue occorrenze in `tcg_mod.hsp` sono il verbo
# inglese comune -- «Deal 4 Damage Split Among Enemies», cioe' «ripartiti fra i
# nemici» -- e non la parola chiave. Un cancello su di essa direbbe rosso su
# cinque rese giuste. La ragione sta qui perche' la prossima persona che vede la
# tabella mancare di una parola chiave si chieda perche', invece di aggiungerla.
FUORI_DAL_CANCELLO = {
    "Split": "le 5 occorrenze sono il verbo inglese, non la parola chiave",
    "EXPLODING!": "e' il messaggio che lampeggia sulla carta che esplode "
                  "(«ESPLODE!»), non una parola chiave: in una descrizione "
                  "d'effetto non compare mai",
    "S [Surrender]": "e' la voce di menu della resa («S [Arrenditi]»), non una "
                     "parola chiave",
}

GRAFIE = {**INNESTI, **PAROLE_CHIAVE}

# ⚠️⚠️ I DUE REFUSI DI MONTE SI RIPRODUCONO, NON SI RIPARANO.
# `tcg_skill.hsp:618` esclude dalla copia le carte la cui descrizione non porta
# la parola esatta. Queste due la sbagliano di monte -- `Batllecry`, `BattleCry`
# -- e oggi NON vengono copiate. Scriverle in italiano corretto le accenderebbe:
# un cambio di comportamento nascosto dentro una traduzione. Le loro rese sono
# esentate dal cancello delle grafie e devono restare fuori dalla partizione.
REFUSI_DI_MONTE = {
    "TCG_EFF_CARAVAN": "riproduce il refuso «Batllecry» di monte",
    "TCG_EFF_NAPLUS": "riproduce la maiuscola di «BattleCry» di monte",
}

# La parola che `tcg_skill.hsp:618` cerca dentro la descrizione.
PAROLA_COPIA = "Battlecry"
PARTIZIONE_ATTESA = (472, 19)

_DESCRIZIONE = re.compile(
    r'^(\s*effdesc@tcg\(([A-Za-z_][A-Za-z0-9_]*)\)\s*=\s*")(.*)("\s*)$')
# Le battute che le carte dicono, nello stesso file. Otto stanno dentro
# `cnvtalk(...)` e una e' nuda; la nona -- `TCG_EFF_LITTLESISTER` -- ha una
# concatenazione dentro l'involucro e NON si riconosce apposta: va guardata a
# mano, e resta dichiarata invece di sparire dal censimento.
BATTUTE_ATTESE = 8

_BATTUTA = re.compile(
    r'^(\s*efftalk@tcg\(([A-Za-z_][A-Za-z0-9_]*)\)\s*=\s*'
    r'(?:cnvtalk\()?")((?:[^"\\]|\\.)*)("\)?\s*)$')

_MARCATURA = re.compile(
    r'^\s*effref@tcg\(TCG_SKILL_REF,\s*([A-Za-z_][A-Za-z0-9_]*)\)\s*=\s*(.*)$')


def leggi(percorso: Path | None = None) -> list[str]:
    """Le righe del file, senza terminatore. `'\\r\\n'.join(...)` le ricompone."""
    percorso = percorso or (percorsi.SORGENTE_HSP / FILE)
    return percorso.read_bytes().decode("cp932").split("\r\n")


def scrivi(righe: list[str], percorso: Path) -> None:
    percorso.write_bytes("\r\n".join(righe).encode("cp932"))


def voci(righe: list[str]) -> list[dict]:
    """Le assegnazioni a `effdesc@tcg`, una per riga, chiave = la costante.

    ⚠️ Il riconoscitore accetta **solo** la forma esatta. `sdim effdesc@tcg, 30,
    3000` dichiara l'array e non assegna niente; una concatenazione con `+` non
    e' un letterale e va guardata a mano, non indovinata.
    """
    fuori = []
    for numero, riga in enumerate(righe, 1):
        trovato = _DESCRIZIONE.match(riga)
        if trovato is None:
            continue
        fuori.append({"costante": trovato.group(2), "riga": numero,
                      "en": trovato.group(3)})
    return fuori


def battute(righe: list[str]) -> list[dict]:
    """Le battute delle carte: `efftalk@tcg(COSTANTE) = "..."`, nude o dentro
    `cnvtalk(...)`.

    ⚠️ Una concatenazione non e' un letterale e non si riconosce: meglio una
    riga in meno tradotta che una riga sbagliata iniettata.
    """
    fuori = []
    for numero, riga in enumerate(righe, 1):
        trovato = _BATTUTA.match(riga)
        if trovato is None:
            continue
        fuori.append({"costante": trovato.group(2), "riga": numero,
                      "en": trovato.group(3)})
    return fuori


def applica_battute_a_righe(righe: list[str],
                            dizionario: dict) -> tuple[list[str], int]:
    """Inietta le battute, conservando l'involucro `cnvtalk(...)` dov'e'."""
    per_riga = {v["costante"]: v for v in battute(righe)}
    fuori = list(righe)
    fatte = 0
    for costante, voce in dizionario.items():
        monte = per_riga.get(costante)
        if monte is None:
            raise ValueError(
                "%s: la battuta %s non esiste piu' nel sorgente. La voce va"
                " rifatta, non riagganciata." % (FILE, costante))
        reso = voce.get("it")
        if not reso:
            continue
        if monte["en"] != voce.get("en"):
            raise ValueError(
                "%s riga %d (%s): il monte non e' piu' quello su cui la resa fu"
                " scritta. La voce va rifatta, non riagganciata."
                % (FILE, monte["riga"], costante))
        indice = monte["riga"] - 1
        pezzi = _BATTUTA.match(fuori[indice])
        fuori[indice] = pezzi.group(1) + degrada(reso) + pezzi.group(4)
        fatte += 1
    return fuori, fatte


def carica_battute(percorso: Path | None = None) -> dict:
    percorso = percorso or (percorsi.DIZIONARIO / "carte" / "efftalk.jsonl")
    if not percorso.exists():
        return {}
    fuori = {}
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        if not riga.strip():
            continue
        voce = json.loads(riga)
        fuori[voce["costante"]] = voce
    return fuori


def carica_dizionario(percorso: Path | None = None) -> dict:
    percorso = percorso or (percorsi.DIZIONARIO / "carte" / "effdesc.jsonl")
    if not percorso.exists():
        return {}
    fuori = {}
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        if not riga.strip():
            continue
        voce = json.loads(riga)
        fuori[voce["costante"]] = voce
    return fuori


def applica_a_righe(righe: list[str], dizionario: dict) -> tuple[list[str], int]:
    """Inietta le rese. Dizionario vuoto -> le righe tornano identiche.

    Ogni descrizione sta su **una riga sola**, quindi qui non serve il giro
    all'indietro di `scene.applica_a_righe`: nessun indice si sposta.
    """
    per_riga = {v["costante"]: v for v in voci(righe)}
    fuori = list(righe)
    fatte = 0
    for costante, voce in dizionario.items():
        monte = per_riga.get(costante)
        if monte is None:
            raise ValueError(
                "%s: la costante %s non esiste piu' nel sorgente. La voce va"
                " rifatta, non riagganciata." % (FILE, costante))
        reso = voce.get("it")
        if not reso:
            continue
        if monte["en"] != voce.get("en"):
            raise ValueError(
                "%s riga %d (%s): il monte non e' piu' quello su cui la resa fu"
                " scritta. La voce va rifatta, non riagganciata."
                % (FILE, monte["riga"], costante))
        indice = monte["riga"] - 1
        pezzi = _DESCRIZIONE.match(fuori[indice])
        fuori[indice] = pezzi.group(1) + degrada(reso) + pezzi.group(4)
        fatte += 1
    return fuori, fatte


def righe_a_capo(testo: str, colonna: int = COLONNA_SCHEDA) -> list[str]:
    """`talk_conv` nel ramo non giapponese (`init.hsp:1326-1367`).

    Si guarda il **prossimo spazio**: se la riga corrente piu' quella parola
    supera la colonna, si va a capo prima della parola. La coda senza spazi
    finisce tutta sull'ultima riga, lunga quanto viene -- ed e' l'unico modo in
    cui una riga puo' sforare in larghezza invece che in altezza.

    ⚠️⚠️ **E c'e' il blocco JAMES CUSTOM (`:1337-1352`), che la 136a aveva
    saltato:** se prima del prossimo spazio c'e' un ritorno a capo, `talk_conv`
    spezza **li'**. Nel sorgente HSP quell'a capo e' scritto `\\n`, due
    caratteri; nell'eseguibile e' un carattere solo, e il gioco ci va a capo
    davvero. Senza questo ramo il conto delle righe usciva **corto su 24 rese
    su 833**, e il massimo vero e' 4 righe, non 3.

    ⚠️ Il ciclo esterno e' limitato a 1000 giri come in HSP, e non e' pedanteria:
    quando il pezzo fino all'a capo e' **da solo** piu' largo della colonna, il
    ramo emette un a capo senza consumare niente e ci ricasca. Li' HSP esaurisce
    i giri e appende il resto grezzo; questa funzione fa lo stesso, perche' un
    simulatore che «corregge» il difetto misura un gioco che non esiste
    (la lezione di `diario.py`, 23a).
    """
    resto, fuori, corrente = testo, "", 0
    for _ in range(1000):
        corrente = 0
        for _ in range(1000):
            spazio = resto.find(" ")
            if spazio == -1:
                break
            parola = spazio + 1
            acapo = resto.find("\n")
            if acapo != -1 and acapo + 1 < parola:
                if corrente + acapo + 1 > colonna:
                    fuori += "\n"
                    break
                fuori += resto[:acapo + 1]
                resto = resto[acapo + 1:]
                break
            if corrente + parola > colonna:
                fuori += "\n"
                break
            fuori += resto[:parola]
            corrente += parola
            resto = resto[parola:]
        if resto.find(" ") == -1:
            break
    return (fuori + resto).split("\n")


def _disegnate(testo: str) -> list[str]:
    """Le righe come le vede il gioco: prefisso, accenti degradati, a capo.

    ⚠️ `degrada` prima di contare, non dopo: CP932 non contiene nessuna vocale
    accentata italiana e `Rarità` a schermo e' `Rarita'`, un carattere in piu'.
    Contare sulla resa e' ottimista proprio sulle rese piu' italiane.

    ⚠️ E `\\n` va sciolto **prima** di contare: nel file HSP sono due caratteri,
    nell'eseguibile e' un ritorno a capo, e `righe_a_capo` ci spezza la riga solo
    se lo vede per quello che e'.
    """
    return righe_a_capo(degrada(PREFISSO + testo).replace("\\n", "\n"))


def _teste(testo: str) -> list[str]:
    """Le teste di frase: quel che sta prima dei due punti, per ogni riga.

    L'a capo dentro una descrizione e' scritto `\\n` nel sorgente HSP, cioe'
    due caratteri veri, non un ritorno a capo.
    """
    fuori = []
    for pezzo in testo.split("\\n"):
        taglio = pezzo.find(":")
        if taglio != -1:
            fuori.append(pezzo[:taglio])
    return fuori


def problemi(voce: dict) -> list[str]:
    """Che cosa RIFIUTA una resa. Elenco vuoto = va bene.

    Qui dentro non c'e' il conto delle righe: quello e' un avviso, perche' il
    soffitto vero del riquadro nessuno l'ha visto.
    """
    reso = voce.get("it")
    if not reso:
        return []
    guai = []
    # ⚠️⚠️ La larghezza, che e' un RIFIUTO mentre l'altezza e' un avviso. Non
    # sono due pesi: dell'altezza nessuno sa il soffitto, della larghezza si sa
    # che il riquadro **taglia** -- l'ha mostrato uno screenshot della 23a, sulla
    # stessa `talk_conv`. E qui il tetto e' quello che l'inglese gia' disegna,
    # quindi e' un cancello che si puo' rispettare, non uno da disattivare.
    for numero, riga in enumerate(_disegnate(reso), 1):
        if len(riga) > LARGHEZZA_MASSIMA:
            guai.append("riga %d larga %d colonne: `talk_conv` non spezza dentro"
                        " una parola e la coda esce dal riquadro; l'inglese non"
                        " passa le %d"
                        % (numero, len(riga), LARGHEZZA_MASSIMA))
    # ⚠️⚠️ Il carattere che CP932 non sa scrivere. `degrada` toglie gli accenti,
    # non tutto: le caporali «» passavano indenni e scoppiavano dopo, dentro
    # `--applica`, a lotto gia' reimportato (133a, e di nuovo la 135a). Il
    # cancello va dove si scrive la resa, non dove si costruisce l'albero.
    try:
        degrada(reso).encode("cp932")
    except UnicodeEncodeError as errore:
        fuori = degrada(reso)[errore.start:errore.end]
        guai.append("il carattere %r non esiste in CP932: il gioco non puo'"
                    " scriverlo" % fuori)
    # ⚠️ I due refusi di monte sono esentati: le loro rese DEVONO restare fuori
    # dalla partizione, o si accendono due carte che oggi il gioco non copia.
    if voce.get("costante") in REFUSI_DI_MONTE:
        return guai
    inglese = voce.get("en") or ""
    teste = _teste(inglese)
    for chiave, italiano in INNESTI.items():
        if any(chiave in testa for testa in teste) and italiano not in reso:
            guai.append("l'inglese dichiara l'innesto «%s»: la resa deve"
                        " portare «%s»" % (chiave, italiano))
    for chiave, italiano in PAROLE_CHIAVE.items():
        if chiave in inglese and italiano not in reso:
            guai.append("«%s» il progetto lo scrive «%s» dalle toppe di"
                        " tcg.hsp: la resa non ce l'ha" % (chiave, italiano))
    return guai


def avvisi(voce: dict) -> list[str]:
    """Cio' che va **guardato**, non cio' che va rifiutato.

    L'italiano e' piu' lungo dell'inglese quasi sempre; se «una riga in piu'»
    fosse un rifiuto, il cancello direbbe rosso su una resa corretta e chi
    traduce imparerebbe a non guardarlo (la distinzione della 70a).
    """
    reso = voce.get("it")
    inglese = voce.get("en")
    if not reso or not isinstance(reso, str) or not isinstance(inglese, str):
        return []
    dopo = len(_disegnate(reso))
    prima = len(_disegnate(inglese))
    fuori = []
    if dopo > prima:
        fuori.append("%d righe contro le %d dell'inglese" % (dopo, prima))
    if dopo > SOFFITTO_AVVISO:
        fuori.append("%d righe, oltre le %d dell'inglese piu' lungo: il"
                     " riquadro non e' mai stato visto a schermo"
                     % (dopo, SOFFITTO_AVVISO))
    return fuori


def partizione_battlecry(righe: list[str],
                         parola: str = PAROLA_COPIA) -> tuple[list, list]:
    """Le carte marcate BATTLECRY, spaccate in «con la parola» e «senza».

    `tcg_skill.hsp:618` copia un effetto solo se **tutt'e due** le cose sono
    vere: la marcatura `TCG_SKILL_TYPE_BATTLECRY` in `effref@tcg` e la parola
    dentro `effdesc@tcg`. Le due stanno in due posti diversi dello stesso file e
    di monte non coincidono: 491 marcate, 19 senza la parola -- le carte degli
    dei, i sette `KAMUI`, e due refusi.

    ⚠️ L'italiano deve riprodurre questa partizione, non ripararla: accendere le
    due carte che oggi il gioco non copia sarebbe un cambio di comportamento
    nascosto dentro una traduzione.
    """
    testo = {v["costante"]: v["en"] for v in voci(righe)}
    marcate = []
    for riga in righe:
        trovato = _MARCATURA.match(riga)
        if trovato and "TCG_SKILL_TYPE_BATTLECRY" in trovato.group(2):
            marcate.append(trovato.group(1))
    con = [k for k in marcate if parola in testo.get(k, "")]
    senza = [k for k in marcate if parola not in testo.get(k, "")]
    return con, senza


def _prova_identita(righe: list[str]) -> None:
    rifatte, fatte = applica_a_righe(righe, {})
    if rifatte != righe or fatte != 0:
        raise SystemExit("identita' ROTTA: col dizionario vuoto il file cambia")
    print("identita'                : il file torna identico, 0 sostituzioni")


def referto() -> None:
    righe = leggi()
    tutte = voci(righe)
    diz = carica_dizionario()
    rese = [v for v in tutte if diz.get(v["costante"], {}).get("it")]
    print("%s: %d righe, %d descrizioni   (attese: %d)"
          % (FILE, len(righe) - 1, len(tutte), ATTESE))
    if len(tutte) != ATTESE:
        raise SystemExit(
            "il riconoscitore ne trova %d invece di %d: il sorgente si e'"
            " mosso, e il conto va rifatto, non aggiustato"
            % (len(tutte), ATTESE))
    traducibili = [v for v in tutte if v["en"].strip()]
    if len(traducibili) != TRADUCIBILI:
        raise SystemExit(
            "le descrizioni con inglese non vuoto sono %d invece di %d: il"
            " sorgente si e' mosso" % (len(traducibili), TRADUCIBILI))
    print("tradotte                 : %d su %d   (2 hanno l'inglese vuoto)"
          % (len(rese), TRADUCIBILI))
    dette = carica_battute()
    tutte_battute = battute(righe)
    if len(tutte_battute) != BATTUTE_ATTESE:
        raise SystemExit(
            "le battute riconosciute sono %d invece di %d: il sorgente si e'"
            " mosso" % (len(tutte_battute), BATTUTE_ATTESE))
    print("battute                  : %d su %d   (1 concatenata, esclusa)"
          % (sum(1 for v in tutte_battute if dette.get(v["costante"], {}).get("it")),
             BATTUTE_ATTESE))
    _prova_identita(righe)

    con, senza = partizione_battlecry(righe)
    print("partizione di monte      : %d con la parola, %d senza   (attesa: %d / %d)"
          % (len(con), len(senza), *PARTIZIONE_ATTESA))
    if (len(con), len(senza)) != PARTIZIONE_ATTESA:
        raise SystemExit(
            "la partizione di `tcg_skill.hsp:618` si e' mossa nel SORGENTE:"
            " il monte non e' piu' quello su cui la fase e' stata progettata")

    # ⚠️⚠️ IL CANCELLO CHE CONTA STA QUI, E MISURA LA BUILD.
    # La riga sopra legge il sorgente, che e' inglese e non cambia mai: da sola
    # e' un verde che non puo' diventare rosso, cioe' non e' un cancello. Quel
    # che si vuole sapere e' quante carte l'operando RAGGIUNGE davvero nel file
    # che finisce nell'eseguibile.
    #
    # ⓘ E' anche il modo in cui e' venuta fuori la regressione di meta' fase:
    # con la toppa che cercava la sola parola italiana, qui uscivano 277 su 472.
    build = percorsi.BUILD_HSP / FILE
    if build.exists():
        righe_build = leggi(build)
        raggiunte = set()
        for parola in (INNESTI[PAROLA_COPIA], PAROLA_COPIA):
            raggiunte |= set(partizione_battlecry(righe_build, parola=parola)[0])
        atteso = PARTIZIONE_ATTESA[0]
        print("raggiunte dall'operando  : %d su %d   (sulla BUILD)"
              % (len(raggiunte), atteso))
        if len(raggiunte) != atteso:
            print("  ⚠️ %d carte marcate BATTLECRY che l'operando NON raggiunge:"
                  " la loro copia e' spenta" % (atteso - len(raggiunte)))
            guasti_operando = 1
        else:
            guasti_operando = 0
    else:
        print("raggiunte dall'operando  : (nessun albero di build da misurare)")
        guasti_operando = 0

    guasti = 0
    for voce in tutte:
        piena = diz.get(voce["costante"])
        if piena is None:
            continue
        for guaio in problemi(piena):
            print("  %s (%s:%d): %s"
                  % (voce["costante"], FILE, voce["riga"], guaio))
            guasti += 1
    print("rese fuori misura        : %d   (atteso: 0)" % guasti)
    guasti += guasti_operando

    segnalate = 0
    for voce in tutte:
        piena = diz.get(voce["costante"])
        if piena is None:
            continue
        for nota in avvisi(piena):
            print("  ⓘ %s: %s" % (voce["costante"], nota))
            segnalate += 1
    print("rese da guardare         : %d   (avviso, non rifiuto)" % segnalate)
    if guasti:
        raise SystemExit(1)


def estrai(nome: str) -> Path:
    """Un lotto di lavoro: le descrizioni non ancora rese, in ordine di riga."""
    righe = leggi()
    diz = carica_dizionario()
    lotto = [v for v in voci(righe) if not diz.get(v["costante"], {}).get("it")]
    bersaglio = percorsi.LAVORO_LOTTI / ("tcg-%s.jsonl" % nome)
    with bersaglio.open("w", encoding="utf-8") as scrittura:
        for voce in lotto:
            voce = dict(voce, it="")
            if voce["costante"] in REFUSI_DI_MONTE:
                voce["_nota"] = REFUSI_DI_MONTE[voce["costante"]]
            scrittura.write(json.dumps(voce, ensure_ascii=False) + "\n")
    return bersaglio


def reimporta(lotto: Path) -> int:
    """Le rese di un lotto entrano nel dizionario. Le vuote si saltano."""
    bersaglio = percorsi.DIZIONARIO / "carte" / "effdesc.jsonl"
    bersaglio.parent.mkdir(parents=True, exist_ok=True)
    diz = carica_dizionario(bersaglio)
    nuove = 0
    for riga in lotto.read_text(encoding="utf-8").splitlines():
        if not riga.strip():
            continue
        voce = json.loads(riga)
        if not voce.get("it"):
            continue
        guai = problemi(voce)
        if guai:
            raise SystemExit("%s: %s" % (voce["costante"], "; ".join(guai)))
        diz[voce["costante"]] = {"costante": voce["costante"],
                                 "riga": voce["riga"], "en": voce["en"],
                                 "it": voce["it"]}
        nuove += 1
    with bersaglio.open("w", encoding="utf-8") as scrittura:
        for costante in sorted(diz):
            scrittura.write(json.dumps(diz[costante], ensure_ascii=False) + "\n")
    return nuove


def main() -> None:
    analizzatore = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    analizzatore.add_argument("--estrai", metavar="NOME",
                              help="lotto JSONL con le descrizioni non rese")
    analizzatore.add_argument("--reimporta", metavar="LOTTO",
                              help="porta le rese di un lotto nel dizionario")
    analizzatore.add_argument("--applica", action="store_true",
                              help="riscrive build/tcg_mod.hsp col dizionario")
    analizzatore.add_argument("--referto", action="store_true",
                              help="il censimento e il cancello")
    argomenti = analizzatore.parse_args()

    if argomenti.estrai:
        percorso = estrai(argomenti.estrai)
        print("lotto scritto: %s" % percorso)
    elif argomenti.reimporta:
        quante = reimporta(Path(argomenti.reimporta))
        print("rese entrate nel dizionario: %d" % quante)
    elif argomenti.applica:
        origine = percorsi.SORGENTE_HSP / FILE
        bersaglio = percorsi.BUILD_HSP / FILE
        righe, fatte = applica_a_righe(leggi(origine), carica_dizionario())
        righe, dette = applica_battute_a_righe(righe, carica_battute())
        scrivi(righe, bersaglio)
        print("%s: %d descrizioni e %d battute iniettate"
              % (bersaglio, fatte, dette))
    else:
        referto()


if __name__ == "__main__":
    main()
