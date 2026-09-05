# strumenti/verifica.py
"""Regole di blocco sui lotti e sul dizionario. Vedi SPEC.md paragrafo 7."""
import argparse
import json
import re
from pathlib import Path

from strumenti import percorsi
from strumenti.accenti import (
    degrada,
    accenti_interni,
    doppi_byte_cp932,
    ha_apostrofo_scritto_a_mano,
    non_ascii_residuo,
    virgolette_non_protette,
)
from strumenti.articolo import GENERI
from strumenti.estrai import estrai_da_testo
from strumenti.funzioni import (
    _maschera_letterali,
    chiamate_di_contenuto,
    funzioni_di_contenuto,
    morfologia_residua,
)

# Due parole separate da spazio FUORI da una stringa: in un'espressione HSP non
# esiste (`name(cc) + " x"` mascherato non ne ha, `Ma viene subito` si').
_PROSA_NUDA = re.compile(r"\w\s+\w")

_RICHIESTI = ("tipo", "en", "en_grezzo")

# Il letterale che sta dentro una `cnvtalk(...)`. Serve due volte, per i due
# modi in cui una resa puo' finirci: da sola (statica, e allora la resa E'
# l'argomento) o dentro un'espressione (dinamica, e allora la chiamata si vede).
# La classe tiene conto degli escape di HSP, dove `\"` non chiude la stringa.
_LETTERALE = r'"((?:[^"\\]|\\.)*)"'
_CNVTALK_DENTRO = re.compile(r"cnvtalk\(\s*" + _LETTERALE + r"\s*\)")
_CNVTALK_INTERO = re.compile(r"^\s*cnvtalk\(\s*" + _LETTERALE + r"\s*\)\s*$", re.S)

# Un articolo (o un possessivo, che concorda uguale) subito prima di una
# funzione che cambia col sesso del GIOCATORE. Si guarda la forma grezza, dove
# la funzione compare per nome: `" + _onii(...`, con lo spazio della
# concatenazione.
#
# Sono due, e hanno lo stesso identico rischio: `_onii` (`text.hsp:111`)
# «Fratellone»/«Sorellona» e `_syujin` (`text.hsp:112`)
# «Padrone»/«Padroncina». Nessuna delle due porta l'articolo dentro — a
# differenza di `name()` — quindi la preposizione nuda regge e l'articolo no.
_APPELLATIVI_DEL_GIOCATORE = ("_onii", "_syujin")
_ARTICOLO_DAVANTI_AD_APPELLATIVO = re.compile(
    r"\b(il|lo|la|un|uno|una|del|dello|della|al|allo|alla|dal|dallo|dalla"
    r"|nel|nello|nella|sul|sullo|sulla|mio|mia|tuo|tua|nostro|nostra)"
    r'\s+"\s*\+\s*(' + "|".join(_APPELLATIVI_DEL_GIOCATORE) + r")\b"
)

# I quattro campi che `estrai` aggiunge alle sole voci dei nomi di
# `db_item.hsp`. Vanno insieme: `plurale` e `genere` sono i due dati che
# l'italiano non deduce, `array` e `oggetto` dicono a `applica.py` dove
# scrivere le righe gemelle. Una voce che ne porta uno li porta tutti, o e'
# stata ritoccata a mano.
_CAMPI_NOME = ("plurale", "genere", "array", "oggetto")

# ⚠️⚠️ **`oggetto` NON basta piu' a riconoscere un nome, e dalla 107a e' un
# campo condiviso.** Le descrizioni di `db_item.hsp` (`DBMODE_DESC`) portano
# l'`ITEM_ID` in `oggetto` — e' la chiave che lega la descrizione al nome
# italiano gia' reso dello stesso oggetto — ma **non portano `array`**, perche'
# non sono la testa di un composto e non hanno righe gemelle da scrivere.
# Riconoscere il nome da «uno qualunque dei quattro campi» faceva bocciare
# **tutte** le 2.580 descrizioni come «voce di nome incompleta»: il difetto e'
# nato nella 107a insieme al terzo tipo di sito e si e' visto nella 108a, il
# primo lotto di descrizioni, perche' prima non c'era niente da verificare.
# Il riconoscitore guarda i tre campi che **solo** un nome ha; `_CAMPI_NOME`
# resta di quattro, perche' un nome deve avere anche l'`oggetto`.
_CAMPI_SOLO_NOME = ("plurale", "genere", "array")


# Le sezioni di `invariati.md` che portano una tabella, classificate per
# prefisso del titolo. Non c'e' un default: una sezione con valori che non
# compare qui alza `ValueError`.
#
# Il motivo e' un difetto vero, trovato il 2026-08-07. Prima si leggeva "la
# tabella fino al primo `##`", e quando la sezione dei valori di dato fu
# inserita in mezzo eredito' l'esclusione **in silenzio**: le otto stringhe di
# `CDATAN_NEWSEX`, che devono restare inglesi per non rompere i salvataggi,
# non arrivavano a `controlla_voce`. Un lotto che le lasciava inglesi -- cioe'
# che faceva esattamente cio' che `invariati.md` prescrive -- inciampava nella
# regola "traduzione identica all'inglese", e `controlla_lotto` rifiutava il
# lotto **intero**. L'unico modo di far passare il lotto era tradurle: il
# controllo spingeva verso la trappola che il cancello della Fase 0 doveva
# impedire.
#
# Spostare il confine avrebbe corretto il sintomo: il prossimo che aggiunge una
# sezione avrebbe rifatto il buco. Quello che non deve piu' essere possibile e'
# il silenzio.
_SEZIONI_INVARIANTI = ("Valori di dato", "Versi senza contenuto linguistico",
                       "Chiavi e nomi di file", "Nomi coniati del potioman",
                       "Termini coniati dentro una DESCRIZIONE",
                       # 138a: le sei battute della nuvoletta del gioco di
                       # carte che restano identiche. Quattro sono
                       # punteggiatura e due sono versi -- lo stesso criterio
                       # della sezione dei versi, su un meccanismo diverso
                       # (`dizionario/carte/dialoghi.jsonl`, campo `invariata`).
                       "Le sei battute della nuvoletta",
                       # 138a: `Dv:`, ` Pv:`, `Sp` e la citazione di Ken il
                       # guerriero. Il glossario le aveva gia' decise; stanno
                       # fuori da `lang()`, quindi non le raggiungeva nessun
                       # dizionario e non le dichiarava nessuna riga.
                       "Le sigle nude che il glossario",
                       # 139a: `Lv`, `,Tab ` e la «d» dei dadi. Stessa specie
                       # della sezione qui sopra -- letterali nudi che
                       # `disegnate.py` ha ripresentato come lavoro da fare --
                       # ma qui la decisione non era gia' scritta nel
                       # glossario: si prende adesso, e il criterio di `Lv` e'
                       # il giapponese (レベル la parola, `Lv` la sigla).
                       "Le sigle e i segni nudi",
                       # 141a: `Trap`, l'unica delle quindici sigle del
                       # pannello dell'equipaggiamento che non si tocca --
                       # abbrevia «trappole» con le stesse quattro lettere di
                       # `trap`. Le altre quattordici sono toppe di
                       # `genera_toppe_tag_equip.py`. La rete che le ha
                       # ripresentate e' la terza, `strumenti/salti.py`.
                       "Le sigle del pannello dell'equipaggiamento")
_SEZIONI_NON_INVARIANTI = ("Da decidere", "Nomi di creatura")

# ⚠️ La terza categoria, nata nella 132a. Le due liste qui sopra rispondono
# alla domanda «questi valori restano inglesi per scelta?», e per farlo danno
# per scontato che la prima colonna della tabella **sia** una stringa del
# gioco. Per qualche sezione non lo e': la sezione dell'articolo mancante,
# scritta dalla 131a, ha per prima colonna degli identificativi del sorgente
# (`ITEM_ID_JUICE`), che nel dizionario non compaiono e non possono ne'
# restare inglesi ne' essere candidati a niente.
#
# Prima non c'era modo di dirlo, e il costo si e' visto in apertura della
# 132a: `pytest` **16 rossi**, tutti da quella sezione, lasciati dal commit
# dei documenti della 131a. Le due scelte disponibili erano tutt'e due false —
# invariante avrebbe messo `ITEM_ID_JUICE` fra le stringhe che restano
# inglesi, non invariante l'avrebbe messo fra i candidati da tradurre.
#
# La proprieta' che questa lista NON deve rompere e' l'unica che conta qui: il
# silenzio. Una sezione nuova continua ad alzare `ValueError` finche' qualcuno
# non la classifica a mano, e le tre categorie sono tre affermazioni diverse,
# tutte esplicite.
_SEZIONI_SENZA_VALORI = ("Quattro oggetti che restano senza articolo",)


def _classifica_sezione(titolo: str) -> str:
    """Da che parte sta una sezione: `invariante`, `candidato` o `senza-valori`.

    Nessun default: o e' scritto, o si rompe.
    """
    for prefisso in _SEZIONI_INVARIANTI:
        if titolo.startswith(prefisso):
            return "invariante"
    for prefisso in _SEZIONI_NON_INVARIANTI:
        if titolo.startswith(prefisso):
            return "candidato"
    for prefisso in _SEZIONI_SENZA_VALORI:
        if titolo.startswith(prefisso):
            return "senza-valori"
    raise ValueError(
        f"invariati.md: la sezione {titolo!r} porta dei valori ma non e'"
        " classificata. Aggiungi il suo prefisso a _SEZIONI_INVARIANTI (i suoi"
        " valori restano inglesi per scelta), a _SEZIONI_NON_INVARIANTI"
        " (sono candidati, e verifica.py deve continuare a segnalarli) oppure"
        " a _SEZIONI_SENZA_VALORI (la prima colonna non e' una stringa del"
        " gioco: sono identificativi, nomi di costante, riferimenti)."
    )


def _valore_di_riga(riga: str) -> str | None:
    """La prima cella di una riga di tabella, se e' una riga di dati.

    Un valore fra apici inversi si prende **verbatim**, spazi compresi. Serve
    perche' una cella markdown si legge con `strip()`, e alcuni invariati hanno
    uno spazio che conta: `text.hsp:62` allinea le sigle delle statistiche con
    `lang("感覚", " PER")`, e la sigla italiana e' " PER" identica — una
    coincidenza legittima, non una traduzione dimenticata. Gli apici inversi
    sono gia' la convenzione del progetto per il codice dentro la prosa.
    """
    spoglia = riga.strip()
    if not spoglia.startswith("|"):
        return None
    celle = [cella.strip() for cella in spoglia.strip("|").split("|")]
    if len(celle) < 2 or not celle[0] or celle[0] == "valore":
        return None
    if set(celle[0]) <= {"-", ":"}:  # riga separatrice
        return None
    valore = celle[0]
    if len(valore) >= 2 and valore.startswith("`") and valore.endswith("`"):
        return valore[1:-1]
    return valore


def carica_invariati(percorso: Path | None = None) -> set[str]:
    """I valori che possono restare identici all'inglese senza che sia un difetto.

    Il file e' un'aggiunta, non un requisito: se manca, la regola si comporta
    come prima. Un progetto senza eccezioni e' un progetto senza il file.

    Si legge **sezione per sezione**. La tabella iniziale, prima di ogni
    titolo, sono gli invariati per scelta esplicita. Le sezioni successive
    valgono secondo `_classifica_sezione`: alcune elencano valori che devono
    restare inglesi (i valori di dato), altre elencano candidati non ancora
    accettati — e leggerle li renderebbe invariati di fatto, cioe' l'opposto
    di cio' che dichiarano — e altre ancora hanno per prima colonna qualcosa
    che non e' affatto una stringa del gioco (identificativi, nomi di
    costante), e allora non c'e' niente da raccogliere.

    Una sezione che porta valori senza essere classificata alza `ValueError`.
    Una sezione di sola prosa non e' una decisione da prendere, e si ignora.
    """
    percorso = percorso or (percorsi.PROGETTO / "invariati.md")
    if not percorso.exists():
        return set()

    # prima si raccoglie per sezione, poi si classifica: cosi' una sezione di
    # sola prosa non deve essere classificata, perche' non ha valori da dare
    titolo = ""  # la tabella iniziale, che non ha titolo
    per_sezione: dict[str, list[str]] = {titolo: []}
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        spoglia = riga.strip()
        # solo `##` e oltre aprono una sezione: `#` e' il titolo del
        # documento, e la tabella che lo segue e' la prima, senza sezione
        if spoglia.startswith("##"):
            titolo = spoglia.lstrip("#").strip()
            per_sezione.setdefault(titolo, [])
            continue
        valore = _valore_di_riga(spoglia)
        if valore is not None:
            per_sezione[titolo].append(valore)

    valori: set[str] = set()
    for titolo, trovati in per_sezione.items():
        if not trovati:
            continue
        if titolo == "" or _classifica_sezione(titolo) == "invariante":
            valori.update(trovati)
    return valori


def _problemi_del_nome(voce: dict) -> list[str]:
    """Le regole che valgono sui due dati di un nome gia' tradotto: `plurale` e `genere`.

    Si chiama solo dopo che `it` e' stato riconosciuto pieno: un nome non
    ancora tradotto ha gia' il suo problema, e chiedergli anche il plurale
    sarebbe rumore.

    Perche' il plurale e' obbligatorio qui, mentre `applica_plurali` lo tratta
    come facoltativo: a valle un plurale che manca **non e' un errore**, il
    gioco ripiega sul singolare e lo stato intermedio resta leggibile. Ma il
    ripiego serve ai nomi **non ancora tradotti**, non a quelli tradotti male:
    su un nome tradotto senza plurale il gioco scriverebbe «2 spada lunga» per
    sempre, e nessuno lo saprebbe finche' non lo vedesse a schermo. E' il
    momento della traduzione il solo in cui qualcuno sta guardando quel nome.

    Il plurale finisce in una stringa letterale HSP come il singolare
    (`ioriginalnamerefplur(ITEM_ID_X) = "..."`), quindi eredita gli stessi tre
    controlli di carattere: virgoletta doppia, apostrofo scritto a mano,
    residuo non rappresentabile in CP932.
    """
    presenti = [nome for nome in _CAMPI_SOLO_NOME if nome in voce]
    if not presenti:
        return []  # non e' un nome: in `lang()` il plurale sta gia' nella stringa

    mancanti = [nome for nome in _CAMPI_NOME if nome not in voce]
    if mancanti:
        return [
            f"{_dove(voce)}: voce di nome incompleta, mancano: {', '.join(mancanti)}."
            " I quattro campi dei nomi viaggiano insieme: senza `array` e"
            " `oggetto` applica.py non sa dove scrivere le righe gemelle."
        ]

    plurale = voce["plurale"]
    if not plurale.strip():
        return [
            f"{_dove(voce)}: nome tradotto senza plurale. In italiano il plurale"
            " non si deduce (paio/paia, spada lunga/spade lunghe): e' un dato, e"
            " va scritto qui. Se coincide col singolare, riscrivilo uguale: la"
            " coincidenza si dichiara, non si indovina."
        ]

    problemi: list[str] = []
    if virgolette_non_protette(plurale):
        problemi.append(
            'il plurale non puo\' contenere una " nuda: applica.py lo scrive'
            ' in ioriginalnamerefplur(...) = "...", e la stringa HSP si'
            ' chiuderebbe in anticipo. Scrivila protetta, \\" — NON con le'
            " tipografiche “”, che CP932 scrive su due byte e la build"
            " inglese non sa disegnare"
        )
    if ha_apostrofo_scritto_a_mano(plurale):
        problemi.append(
            "apostrofo scritto a mano nel plurale: nel dizionario va l'accento"
            " vero, la degradazione la fa applica.py"
        )
    residui = non_ascii_residuo(degrada(plurale))
    if residui:
        problemi.append(f"caratteri del plurale che CP932 cancellerebbe: {residui}")
    doppi = doppi_byte_cp932(degrada(plurale))
    if doppi:
        problemi.append(
            f"caratteri del plurale che CP932 scrive su due byte: {doppi} — "
            "la build inglese ne disegna uno per byte"
        )

    # Il genere: stessa natura del plurale, stesso momento buono per scriverlo.
    # Non e' l'articolo — quello lo deriva `strumenti/articolo.py`, perche' la
    # scelta fra «un» e «uno» e' una regola meccanica sulla parola che segue.
    # Il numero fa parte del dato: «cianfrusaglie» e «attrezzi» esistono solo al
    # plurale, e su di loro l'articolo indeterminativo non c'e'.
    genere = voce["genere"]
    if genere not in GENERI:
        problemi.append(
            f"genere {genere!r} assente o non valido, attesi {', '.join(GENERI)}"
            " (m/f al singolare, mp/fp per i nomi che esistono solo al plurale)."
            " Serve all'articolo, che in italiano dipende dal genere del nome e"
            " non dalla lettera iniziale come in inglese: senza, il gioco ripiega"
            " sull'articolo inglese davanti a un nome italiano."
        )
    return problemi


def _dove(voce: dict) -> str:
    """`file:riga` per un messaggio d'errore che si possa seguire."""
    return f"{voce.get('file', '?')}:{voce.get('riga', '?')}"


def controlla_voce(voce: dict, invariati: set[str] | None = None) -> list[str]:
    """Ritorna la lista dei problemi. Lista vuota significa voce pulita.

    L'accesso ai campi e' coerente e difensivo: un dizionario ritoccato a mano
    con un campo mancante produce un problema che nomina file e riga, non un
    `KeyError` nudo a meta' della validazione di un lotto.

    `invariati` sono i valori che possono restare identici all'inglese senza
    che sia un difetto. Il default `None` non legge il disco e non cambia il
    comportamento dei chiamanti esistenti: il file lo carica `controlla_lotto`
    una volta sola.
    """
    problemi: list[str] = []
    italiano = voce.get("it", "")

    mancanti = [nome for nome in _RICHIESTI if nome not in voce]
    if mancanti:
        problemi.append(f"{_dove(voce)}: campi mancanti nella voce: {', '.join(mancanti)}")
        return problemi

    tipo = voce["tipo"]
    if tipo not in ("statica", "dinamica"):
        problemi.append(f"{_dove(voce)}: tipo {tipo!r} non valido, attesi 'statica' o 'dinamica'")
        return problemi

    # Un invariato fatto di soli spazi non e' una traduzione vuota: `text.hsp:198`
    # e' `strblank = lang("", " ")`, uno spazio di RIEMPIMENTO. Senza questa
    # eccezione la regola scattava prima di quella sugli invariati, e quel valore
    # era irraggiungibile per costruzione — nessuna traduzione lo faceva passare,
    # nemmeno quella giusta. La regola resta per tutto il resto, dove una
    # traduzione vuota e' quasi sempre una riga dimenticata.
    if not italiano.strip() and italiano not in (invariati or set()):
        problemi.append("traduzione vuota")
        return problemi

    # per le dinamiche il termine di paragone e' l'espressione intera
    originale = voce["en_grezzo"] if tipo == "dinamica" else voce["en"]
    # il confronto e' sulla stringa intera: `Vernis` fra gli invariati zittisce
    # la voce che vale esattamente "Vernis", non una frase che lo contiene —
    # quella, se e' rimasta inglese, e' proprio cio' che la regola cerca
    if italiano == originale and italiano not in (invariati or set()):
        problemi.append("traduzione identica all'inglese")

    # i nomi di `db_item.hsp` portano due dati in piu' che arrivano fino al gioco
    problemi.extend(_problemi_del_nome(voce))

    if ha_apostrofo_scritto_a_mano(italiano):
        problemi.append(
            "apostrofo scritto a mano: nel dizionario va l'accento vero, "
            "la degradazione la fa applica.py"
        )

    # per le statiche applica.py avvolge l'italiano fra virgolette doppie
    # ("...") per farne una stringa letterale HSP: una " dentro il testo
    # chiude la stringa in anticipo e produce sorgente non compilabile.
    # Per le dinamiche invece l'italiano e' gia' un'espressione HSP intera
    # (es. name(tc) + " ha protetto " + name(x) + "."), dove le virgolette
    # doppie sono legittime e necessarie: la regola non si applica li'.
    if tipo != "dinamica" and virgolette_non_protette(italiano):
        problemi.append(
            'una statica non puo\' contenere una " nuda, perche\' romperebbe '
            "la stringa HSP generata da applica.py "
            '(lang("...", "...") si chiuderebbe in anticipo); '
            'scrivila protetta, \\" , come fa l\'inglese upstream '
            '(text.hsp:9879 scrive \\"Project LF\\"). '
            "⚠️ NON usare le tipografiche “”: CP932 le codifica, ma su DUE "
            "byte, e la build inglese disegna un glifo per byte — a schermo "
            "esce un carattere latino a caso. Vedi doppi_byte_cp932()"
        )

    # gli accenti veri (perche') si degradano regolarmente in fase di build:
    # non sono un residuo. Il residuo vero e' cio' che resta non rappresentabile
    # anche dopo la degradazione (es. un trattino lungo, virgolette tipografiche).
    residui = non_ascii_residuo(degrada(italiano))
    if residui:
        problemi.append(f"caratteri che CP932 cancellerebbe: {residui}")

    # ⚠️ L'accento in mezzo alla parola passa `degrada` senza rumore e diventa
    # illeggibile a schermo: «elite» -> «e'lite», «dei» -> «de'i». Non e' un
    # carattere che CP932 non sa scrivere — e' la degradazione stessa che
    # funziona solo sull'ultima lettera. Lezione della 41a, rete dalla 71a, che
    # l'ha trovata violata quindici volte nel dizionario.
    interni = accenti_interni(italiano)
    if interni:
        problemi.append(
            f"accento in mezzo alla parola: {interni} — la degradazione mette "
            "l'apostrofo dentro la parola («elite» diventa «e'lite», «dei» "
            "diventa «de'i») e a schermo non si legge. Si cambia parola, non "
            "si toglie l'accento"
        )

    # CP932 li codifica — e' proprio questo che li rendeva invisibili al
    # controllo di sopra — ma su due byte, e la build inglese disegna un glifo
    # per byte (init.hsp:1391, font Courier New). Misurato a schermo.
    doppi = doppi_byte_cp932(degrada(italiano))
    if doppi:
        problemi.append(
            f"caratteri che CP932 scrive su due byte: {doppi} — la build "
            "inglese ne disegna uno per byte e a schermo escono lettere "
            "latine a caso (「・」 e' uscito «E»). Usa ... per 「…」, "
            '\\" per 「“”」, <> per 「《》」'
        )

    # ⚠️ **La cifra dopo un ♪ non e' testo: e' il numero dell'icona, e sparisce.**
    # `msg_write` (`init.hsp:1372-1386`) cerca il ♪, legge il carattere subito
    # dopo come indice (`mark = int(strmid(msg, mp + 2, 1))`), disegna
    # `gcopy 3, 600 + mark * 24, ...` e poi togle dal testo il ♪ **e la cifra**
    # (`mp + 2 + (mark != 0)`, riga 1382). Upstream la usa di proposito —
    # `item.hsp:3954` scrive `"Wow♪1 Zaaaako♪1♪1♪1 "` — quindi non e' un difetto
    # di monte: e' una notazione. Ma una resa che si trovasse una cifra dopo la
    # nota per caso la perderebbe **in silenzio**, e nessun altro controllo lo
    # vede: il ♪ e' l'unico carattere a due byte ammesso, quindi passa
    # `doppi_byte_cp932` per costruzione.
    #
    # La regola: un `♪<cifra>` nell'italiano deve comparire **identico** in una
    # delle due forme di monte. Copiare l'icona che il sorgente sceglie e'
    # legittimo; inventarne una a partire dal testo no.
    icone = set(re.findall(r"♪[0-9]", italiano))
    if icone:
        monte = set(re.findall(r"♪[0-9]", voce.get("jp_grezzo", "") + voce["en_grezzo"]))
        inventate = sorted(icone - monte)
        if inventate:
            problemi.append(
                f"cifra dopo il ♪ che non viene da monte: {inventate}. In "
                "init.hsp:1376 la cifra dopo la nota e' il numero dell'icona, e "
                "riga 1382 la TOGLIE dal testo: quel carattere non arriva a "
                "schermo. Se e' testo, mettici uno spazio prima."
            )

    if tipo == "dinamica":
        # ⚠️⚠️ **Per una dinamica la resa e' un'ESPRESSIONE HSP, non del testo**,
        # e prosa nuda al posto di un'espressione produce sorgente che non
        # compila: `lang("...", Ma viene subito respinto fuori.)` muore con
        # «パラメーター式の記述が無効です». Nessun'altra guardia lo vedeva.
        #
        # Il buco si apre solo quando l'inglese della dinamica non ha NESSUNA
        # funzione di contenuto — perche' le sue chiamate sono tutte morfologia
        # (`"But " + he(tc) + " eject" + _s(tc) + " it out quickly."`,
        # `item.hsp:4597`). Li' il confronto delle interpolazioni trova due
        # elenchi vuoti e tace, e chi scrive la resa la tratta naturalmente come
        # una statica: e' proprio la voce in cui l'italiano non ha piu' niente
        # da interpolare. Trovato nella 69a, con l'errore del compilatore.
        #
        # La misura e' sulla forma, non sul contenuto: mascherati i letterali,
        # un'espressione HSP non ha mai due parole separate da uno spazio.
        if _PROSA_NUDA.search(_maschera_letterali(italiano)):
            problemi.append(
                "la resa di una dinamica dev'essere un'ESPRESSIONE HSP, non "
                "testo nudo: applica.py la scrive dentro lang(...) cosi' com'e', "
                "e il compilatore rifiuta la riga. Avvolgi il testo fra "
                'virgolette — \'"Ma viene subito respinto fuori."\' — anche '
                "quando non c'e' niente da concatenare."
            )

        # la morfologia inglese (_s, is, was, your, ... e he/his/him quando
        # chiamate con un solo argomento) non e' contenuto: non passa mai da
        # lang(), quindi non si localizzera' mai, e pretendere che l'italiano
        # la conservi tal quale e' il difetto che questa funzione correggeva.
        # Il confronto vero e' sulle sole chiamate di contenuto (nomi,
        # oggetti, dati... e he/his/him quando chiamate con due argomenti);
        # i pronomi non entrano nel confronto in nessuno dei due sensi.
        # ⭐ **E il metro non e' solo l'inglese: e' l'inglese PIU' il
        # giapponese.** Aggiunto nella 72a, su `screen.hsp:6759`:
        #
        #     JP  name(r1) + "はレベル" + cdata(CDATA_LEVEL, r1) + "になった！"
        #     EN  name(r1) + " have gained a level."
        #
        # cioe' il giapponese dice **a quale** livello si sale e l'inglese ha
        # buttato via il numero. Rimetterlo in italiano non e' inventare
        # un'interpolazione: quella chiamata sta gia' sulla stessa riga, nello
        # stesso ambito, ed e' valida per costruzione. La regola vecchia la
        # rifiutava, e cosi' obbligava la traduzione a ereditare ogni perdita
        # di monte.
        #
        # ⚠️ Le due liste restano diverse: quel che l'inglese ha e' **dovuto**
        # — toglierlo e' perdere un dato che il giocatore vede — mentre quel
        # che ha solo il giapponese e' **permesso**. Non e' una simmetria: una
        # resa non e' tenuta a recuperare tutto quello che l'inglese ha perso,
        # ma se lo recupera non e' un difetto.
        #
        # 💡 **E le due guardie di questa riga non erano d'accordo fra loro.**
        # Quella sugli argomenti, dieci righe piu' sotto, sottraeva gia'
        # l'unione dell'inglese e del giapponese — con un commento che spiega
        # perche' — mentre questa pretendeva l'uguaglianza col solo inglese.
        # Due misure della stessa cosa nella stessa funzione, una piu' larga
        # dell'altra: la piu' stretta vinceva sempre, e il commento della
        # piu' larga descriveva un comportamento che non c'era.
        attese = funzioni_di_contenuto(voce["en_grezzo"])
        permesse = funzioni_di_contenuto(voce.get("jp_grezzo") or "")
        trovate = funzioni_di_contenuto(italiano)
        mancanti = [f for f in attese if f not in trovate]
        inventate = [f for f in trovate if f not in attese and f not in permesse]
        if mancanti or inventate:
            problemi.append(
                f"interpolazioni non conservate: attese {attese}, trovate {trovate}"
                + (f", mancanti {mancanti}" if mancanti else "")
                + (f", inventate {inventate}" if inventate else ""))

        # ⚠️ i NOMI delle chiamate non bastano: `name(cc)` e `name(tc)` hanno lo
        # stesso nome e nominano due personaggi diversi. Ogni chiamata
        # dell'italiano deve comparire identica, argomenti compresi, in una
        # delle due forme di monte — l'inglese o il giapponese.
        #
        # L'unione delle due, e non il solo inglese, perche' i due rami di
        # `lang()` a volte scelgono soggetti diversi per lo stesso evento:
        # `action.hsp:1698` e' `name(cc) + " disturb" + ... + " sleep."` in
        # inglese e `name(tc) + "は睡眠を妨害された。"` in giapponese, e la resa
        # italiana segue il giapponese («si sveglia di soprassalto») perche'
        # l'inglese chiederebbe il possessivo che l'italiano omette. Pretendere
        # l'inglese avrebbe rifiutato una resa giusta.
        estranee = sorted(
            set(chiamate_di_contenuto(italiano))
            - set(chiamate_di_contenuto(voce["en_grezzo"]))
            - set(chiamate_di_contenuto(voce.get("jp_grezzo", "")))
        )
        if estranee:
            problemi.append(
                f"interpolazioni con argomenti che non vengono da monte: {estranee}. "
                "Il sorgente sceglie il personaggio (cc chi agisce, tc chi subisce): "
                "una resa che scambia i due nomina il personaggio sbagliato, e "
                "nessun'altra guardia lo vede."
            )

        # la morfologia inglese non si localizza mai: _s(tc) scrive "s" a
        # schermo anche dentro una frase italiana, e cosi' his(tc) senza
        # secondo argomento scrive "his" per sempre
        residue = morfologia_residua(italiano)
        if residue:
            problemi.append(
                f"morfologia inglese rimasta nella traduzione: {residue}. "
                "Sono desinenze e possessivi inglesi (\"s\", \"is\", \"'s\"): "
                "in italiano vanno tolti e la frase va riscritta."
            )

        # ⚠️ **Non portano l'articolo dentro, ma non ne vogliono uno davanti.**
        # `text.hsp:111` e' `_onii = lang("お兄", "Big bro"), lang("お姉", "Big
        # sis")` — «Fratellone» / «Sorellona» — e `text.hsp:112` e' `_syujin`,
        # «Padrone» / «Padroncina». Cambiano col sesso del GIOCATORE, quindi un
        # articolo davanti e' scritto una volta sola, concorda con uno dei due e
        # sbaglia meta' delle partite. A differenza di `name()`, che l'articolo
        # se lo porta dentro, qui la preposizione nuda regge: «a Fratellone»
        # si', «al mio Fratellone» no. `_onii` ha 36 siti di chiamata, 24 in
        # `db_creature.hsp`.
        articolo = _ARTICOLO_DAVANTI_AD_APPELLATIVO.search(italiano)
        if articolo:
            determinante, funzione = articolo.group(1), articolo.group(2)
            problemi.append(
                f"articolo davanti a {funzione}: {determinante!r}. {funzione} "
                "cambia col sesso del giocatore (Fratellone/Sorellona, "
                "Padrone/Padroncina), quindi un articolo davanti sbaglia genere "
                "meta' delle volte. La preposizione nuda regge: «a Fratellone», "
                "non «al Fratellone»."
            )

    # ⚠️ **Lo spazio in coda all'inglese e' una giuntura, non una svista.**
    # Quando la frase si compone di due pezzi il primo tiene lo spazio che li
    # separa: se la resa lo lascia cadere, le due meta' si saldano a schermo e
    # nessun'altra guardia lo vede, perche' entrambe le stringhe sono valide.
    #
    # ⚠️ **Solo per le statiche, e non e' un dettaglio.** Per una dinamica `en`
    # non e' la stringa intera: e' il testo dei letterali concatenati, e finisce
    # con uno spazio ogni volta che l'ultimo letterale precede una chiamata —
    # `name(tc) + " moans, " + cnvtalk("It stinks!")` da' `en = " moans, "`.
    # Li' lo spazio sta in MEZZO all'espressione, non in coda alla frase, e
    # pretenderlo alla fine della resa italiana rifiuterebbe ogni battuta con
    # una chiamata in fondo.
    # ⚠️⚠️ **Le virgolette del discorso diretto le mette `cnvtalk`, non la resa.**
    # `init.hsp:171` e' `return "\"" + s + "\" "`: quel che gli si passa esce
    # gia' fra virgolette. Una resa che se le porta dentro le **raddoppia** a
    # schermo, e nessuna guardia lo vedeva perche' le due stringhe — la nostra e
    # quella del codice — sono valide tutt'e due. E' la famiglia di difetti della
    # 72a, quelli che non stanno in una stringa ma **fra due**: qui il pezzo che
    # manca non lo mette una `pos`, lo mette una funzione.
    # ⭐ Trovata nella 74a con nove rese gia' spinte, otto della banca di
    # `action.hsp` e una di `db_creature.hsp` — e quest'ultima raccontava anche
    # una **narrazione** dentro le virgolette del parlato, cioe' un secondo modo
    # di sbagliare lo stesso sito: quel che entra in `cnvtalk` e' solo la battuta.
    for dentro in _CNVTALK_DENTRO.findall(voce.get("it") or ""):
        if '\\"' in dentro:
            problemi.append(
                "virgolette protette dentro cnvtalk: le mette gia' lui "
                '(init.hsp:171, `return "\\"" + s + "\\" "`), e a schermo '
                "verrebbero doppie. Dentro cnvtalk va la battuta nuda."
            )
    if _CNVTALK_INTERO.match(voce.get("en_grezzo") or "") and '\\"' in italiano:
        problemi.append(
            "virgolette protette in una resa che E' l'argomento di cnvtalk: "
            "le mette gia' lui (init.hsp:171), e a schermo verrebbero doppie. "
            "Qui va la battuta nuda, senza virgolette."
        )

    if tipo != "dinamica" and voce["en"].endswith(" ") and not italiano.endswith(" "):
        problemi.append(
            "l'inglese finisce con uno spazio e la traduzione no: quello "
            "spazio e' la giuntura con il pezzo che segue, e senza di lui le "
            "due meta' della frase si saldano."
        )

    return problemi


def controlla_lotto(voci: list[dict], invariati: set[str] | None = None) -> dict[str, list[str]]:
    """Mappa firma -> problemi, per le sole voci con almeno un problema.

    Gli invariati si caricano una volta sola qui, non a ogni voce: rileggere il
    file per ognuna delle 6.688 voci di un lotto sarebbe assurdo. I test lo
    passano gia' risolto per non toccare il disco.
    """
    invariati = carica_invariati() if invariati is None else invariati
    esito: dict[str, list[str]] = {}
    for voce in voci:
        problemi = controlla_voce(voce, invariati)
        if problemi:
            esito[voce.get("firma", _dove(voce))] = problemi
    return esito


def confronta_col_sorgente(nome_file: str) -> tuple[list[dict], int]:
    """Coda di ritraduzione per un file: SPEC 3.1.

    Ritorna le voci tradotte la cui firma **non esiste piu'** nel sorgente — la
    stringa e' cambiata o sparita a monte, e la traduzione va rifatta — e quante
    firme del sorgente non hanno ancora una traduzione.

    Sono due domande diverse e vanno lette insieme: un dizionario puo' essere
    completo e tutto da ritradurre.

    Una voce con `it` vuoto non e' orfana: non c'e' nessun lavoro da rifare, e
    contarla gonfierebbe il numero che decide se la catena si ferma.
    """
    percorso = percorsi.DIZIONARIO / f"{nome_file}.jsonl"
    voci = []
    if percorso.exists():
        voci = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    tradotte = {v["firma"]: v for v in voci if v.get("it")}

    # un .hsp puo' sparire a monte fra due versioni CGX: e' il caso che SPEC 3.1
    # contempla, e un read_bytes nudo lo trasformerebbe in un FileNotFoundError
    # a meta' scansione invece che in una coda da ritradurre
    sorgente = percorsi.SORGENTE_HSP / nome_file
    if sorgente.exists():
        nel_sorgente = {v["firma"] for v in estrai_da_testo(nome_file, sorgente.read_bytes().decode("cp932"))}
    else:
        nel_sorgente = set()

    orfane = [v for f, v in tradotte.items() if f not in nel_sorgente]
    non_tradotte = len(nel_sorgente - set(tradotte))
    return sorted(orfane, key=lambda v: v.get("riga", 0)), non_tradotte


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Verifica un lotto JSONL tradotto.")
    analizzatore.add_argument("lotto", nargs="?", help="percorso del lotto JSONL")
    analizzatore.add_argument(
        "--dizionario", action="store_true",
        help="confronta il dizionario col sorgente invece di validare un lotto")
    argomenti = analizzatore.parse_args()

    if argomenti.dizionario:
        totale_orfane = 0
        for percorso in sorted(percorsi.DIZIONARIO.glob("*.jsonl")):
            # ⚠️⚠️ `scene2.hsp` NON passa di qui, per la stessa ragione per cui
            # non passa dal ciclo di `applica.py` (chiusa nella 133a): le sue
            # voci non sono firme di `lang()` ma blocchi di scena, e
            # `confronta_col_sorgente` non trova nel sorgente NESSUNA delle sue
            # firme. Ogni resa nuova diventava cosi' una «da ritradurre», e il
            # numero cresceva col lavoro: 1.382 a fase finita, con
            # `--dizionario` che usciva con 1 senza che nessuno lo leggesse.
            # Il cancello di quel file e' `python -m strumenti.scene --referto`,
            # che lo legge per quello che e'. ⭐ Lo stesso guasto in due
            # strumenti diversi: quando si ripara un ciclo che scorre
            # `DIZIONARIO/*.jsonl`, si cercano gli altri cicli che fanno lo
            # stesso giro, invece di fermarsi al primo.
            if percorso.stem == "scene2.hsp":
                continue
            orfane, non_tradotte = confronta_col_sorgente(percorso.stem)
            totale_orfane += len(orfane)
            print(f"{percorso.stem}: {len(orfane)} da ritradurre, {non_tradotte} non ancora tradotte")
            for voce in orfane[:5]:
                print(f"    {voce['firma'][:10]} (riga {voce.get('riga', '?')}): {voce.get('en', '')[:60]!r}")
            if len(orfane) > 5:
                print(f"    ... e altre {len(orfane) - 5}")
        raise SystemExit(1 if totale_orfane else 0)

    if argomenti.lotto is None:
        analizzatore.error("serve il percorso di un lotto, oppure --dizionario")

    voci = [json.loads(riga) for riga in Path(argomenti.lotto).read_text(encoding="utf-8").splitlines() if riga.strip()]
    esito = controlla_lotto(voci)
    if not esito:
        print(f"{len(voci)} voci, nessun problema")
        return
    for chiave, problemi in esito.items():
        print(f"{chiave}: " + "; ".join(problemi))
    raise SystemExit(f"{len(esito)} voci con problemi su {len(voci)}")


if __name__ == "__main__":
    main()
