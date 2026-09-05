"""La rete dell'OPERANDO: il letterale che il codice CERCA, non quello che stampa.

⚠️⚠️ **Perche' esiste.** Tutte le reti del progetto guardano il testo che il
giocatore *legge*: `copertura` le `lang()`, `disegnate` e `salti` quel che
arriva a un comando che disegna. Nessuna guarda la **chiave**: il letterale che
`instr`, `sreplace`, `strmid` o `cnv_str` vanno a cercare **dentro** una
stringa. E la chiave non e' testo a schermo: e' quel che accende il codice.

⭐ La 142a ha trovato due volte, per caso, lo stesso difetto:

    command.hsp:4481   instr(inputlog, 0, "god inside")

La battuta che quella riga fa dire era italiana da sessioni; la parola che la
accendeva era inglese, e il giocatore italiano non poteva piu' accenderla.
`copertura` la contava — giustamente — ma nessuno sapeva **quante altre** ce ne
fossero. Questa rete risponde a quella domanda.

## Il metro: si guarda la BUILD, non il sorgente

⚠️⚠️ **A differenza di `copertura`, `disegnate` e `salti`, questa rete legge
`build/`.** E' la regola della 129a — «che cosa si misura per dire *risolta da
toppa*: la build, non l'elenco delle toppe» — e qui e' obbligatoria: quasi tutte
le chiavi che ci interessano stanno in righe che una toppa ha gia' riscritto.
Chiedere al sorgente vorrebbe dire riaprire fronti gia' chiusi, che e'
esattamente l'errore che la 142a ha fatto sul punto 12 della lista della 138a.
ⓘ Percio' la rete va rilanciata **dopo** i sei passi di `applica`, non prima.

## Che cosa e' un candidato

Un costrutto che cerca (`instr`, `strmid`) o sostituisce (`sreplace`,
`cnv_str`, `getstr`, `notefind`) con un letterale che:

- ha lettere latine (una chiave giapponese in un ramo `jp` e' al suo posto);
- **non e' un marcatore** — `%txt`, `{ev}`, `/neg/`, `\\n`, `:sound`. I
  marcatori sono la maggioranza assoluta e sono chiavi di formato dentro i file
  di dato: tradurli scollegherebbe il gioco dai suoi stessi file.

⚠️ **`copertura._PROSA` qui non serve, e sarebbe dannosa**: pretende due parole
latine, e l'operando di una sostituzione e' quasi sempre **una parola sola o un
frammento** — `"dragon"`, `"coffin "`, `" your"`, `", the "`. E' la ragione per
cui questa e' una rete a se' e non un ramo di `copertura`.

## Il pagliaio, che e' la domanda vera

⭐ Un letterale inglese cercato dentro `buff` — la riga di `autopick.txt` che il
giocatore scrive — **non e' un difetto**: quella chiave e' un'etichetta di
formato, e il file non e' nostro. Lo stesso letterale cercato dentro
`carddetailneff@tcg(...)` — il testo di una carta, che abbiamo tradotto — e' un
difetto certo. Quel che distingue i due casi non e' il letterale: e' **dentro
che cosa si cerca**.

Percio' la rete classifica per PAGLIAIO, e **segnala per difetto**: sta fuori
solo il pagliaio dichiarato qui sotto, uno per uno, col motivo. Un pagliaio
nuovo — una variabile che nessuno aveva mai visto — compare nel referto invece
di sparire in una regola generale.

## Uso

    python -m strumenti.operandi                # il censimento, per pagliaio
    python -m strumenti.operandi --righe        # con le righe
    python -m strumenti.operandi --pagliaio X   # un pagliaio solo
"""
import argparse
import re
from collections import defaultdict
from dataclasses import dataclass

from strumenti import percorsi
from strumenti.commenti import (colonna_commento_riga, righe_in_commento,
                                righe_in_ramo_spento)

# ⭐⭐ I tre costrutti, e **dove sta la chiave in ognuno**. Guardare tutti i
# letterali della riga sarebbe un `grep`, non una rete: in
# `cnv_str fix_input_chat_arg1, "%", "per"` la chiave e' `"%"` — un simbolo — e
# `"per"` e' quel che ci si SCRIVE al posto. Contare anche il sostituto direbbe
# «chiave italiana» dove non c'e' nessuna chiave italiana, e il conto del fronte
# sarebbe gonfio della meta'.
#
#   instr(pagliaio, da, CHIAVE)                -> pagliaio 0, chiave 2
#   sreplace destinazione, pagliaio, CHIAVE, sostituto -> pagliaio 1, chiave 2
#   cnv_str pagliaio, CHIAVE, sostituto        -> pagliaio 0, chiave 1
#
# ⚠️ `strmid` sta fuori: prende posizione e lunghezza, **non ha mai un letterale
# come chiave**. Le sue righe finivano nel conto solo per l'`instr` annidato che
# ci sta dentro, e quello si vede da se'. ⚠️ `getstr` prende un carattere
# separatore come numero, e `notefind` nella build non esiste.
_COSTRUTTI = {
    "instr": (0, 2),
    "sreplace": (1, 2),
    "cnv_str": (0, 1),
}
_APERTURA = re.compile(r"\b(instr)\s*\(", re.IGNORECASE)
_COMANDO = re.compile(r"(?:^|:|\{)\s*(sreplace|cnv_str)\s+", re.IGNORECASE)

# un letterale HSP: le virgolette doppie non si annidano e non c'e' escape
_LETTERALE = re.compile(r'"([^"]*)"')

_GIAPPONESE = re.compile(r"[　-ヿ一-鿿！-ﾟ]")
_LATINO = re.compile(r"[A-Za-z]")

# ⚠️ I marcatori: chiavi di formato dentro i file di dato del gioco o del
# giocatore. Non sono testo e non si traducono mai.
_MARCATORE = re.compile(
    r"""^(?:
          \\[ntr]          # \n, \t, \r come coda della stringa
        | %\w*             # %txt, %HARVEST
        | \{\w+\}          # {ev}
        | /\w+/            # /neg/, /dragon/
        | :\w+             # :sound
        | _\w+_            # _tmp_
        | [A-Z]{2}         # JP, EN
        )$""",
    re.VERBOSE,
)


@dataclass(frozen=True)
class Dichiarazione:
    tipo: str      # vedi TIPI
    casi: int      # righe candidate misurate, non ereditate
    motivo: str


# ⭐ Quattro esiti, non due. «Chiave inglese» da sola non dice niente: quel che
# conta e' se il giocatore italiano perde qualcosa.
TIPI = {
    "esente":  "il pagliaio non e' testo nostro: un file di dato, un percorso, "
               "quel che il giocatore digita, la console di prova",
    "seguita": "e' testo nostro, e la chiave e' stata portata dietro: nella "
               "build cerca l'italiano (da sola o accanto all'inglese)",
    "inutile": "e' testo nostro, la chiave e' rimasta inglese, e non aggancia "
               "piu' niente — ma non c'e' niente da agganciare, perche' la "
               "resa italiana non ha la forma su cui la sostituzione lavorava",
    "fronte":  "e' testo nostro, la chiave e' rimasta indietro, e il giocatore "
               "italiano ci perde qualcosa. Lavoro aperto.",
}

# ⚠️⚠️ Come in `copertura`, `disegnate` e `salti`: o un pagliaio e' dichiarato,
# o il cancello si accende. **Il conto e' misurato e il cancello lo legge; il
# motivo accanto e' prosa, e nessun cancello legge la prosa** — la lezione della
# 140a, dove quattro motivi su sette dicevano una cosa falsa.
DICHIARATI: dict[str, Dichiarazione] = {

    # ---- esenti: il pagliaio non e' testo nostro -------------------------
    "chat.hsp:evact": Dichiarazione(
        "esente", 187,
        "L'azione di un evento di CNPC: `gohos`, `turnAlly`, `emofire`, le "
        "venti icone d'emozione. Il giocatore le scrive nel file del suo "
        "personaggio (`%txt_ucnpc_ev_b` … `_e`), e sono parole chiave del "
        "formato. Tradurle scollegherebbe ogni CNPC gia' scritto."),
    "system.hsp:buff": Dichiarazione(
        "esente", 38,
        "La console di prova (`del`, `freemove`, `resetmap`, `fixmap`, "
        "`removequest`): comandi che si digitano, non testo che si legge."),
    "custom_lib.hsp:ReturnString": Dichiarazione(
        "esente", 4,
        "`%syujin%` e `%onii%`: i due segnaposto che la libreria sostituisce "
        "col nome del padrone e con la parola per «fratello». Marcatori con la "
        "percentuale, come i `%…` di `text.hsp`."),
    "custom_lib.hsp:Tempstring": Dichiarazione(
        "esente", 4, "Le sequenze `\\n` e `\\t` dentro la libreria di lettura "
        "dei file: separatori, non parole."),
    "custom_lib.hsp:TempString": Dichiarazione(
        "esente", 2, "Come `Tempstring` qui sopra — nella stessa libreria "
        "convivono i due nomi, e sono due variabili diverse."),
    "item_func.hsp:locvar_itemowner_s": Dichiarazione(
        "esente", 2,
        "⭐ `sreplace … \"user\", getcnpcnamebychecksum(...)` mette il nome del "
        "CNPC al posto del segnaposto. **Misurato**: il nome della creatura "
        "`CREATURE_ID_USER` e' `lang(\"user\", \"user\")` "
        "(`db_creature.hsp:97539` e `:97573`) — inglese in tutt'e due i rami, "
        "che e' quel che questa riga si aspetta. La chiave aggancia ancora."),
    "module.hsp:fix_input_chat2_arg1": Dichiarazione(
        "esente", 2,
        "`fucking` -> `nyoro~n` e `fuck` -> `nyou talk funny`: la censura "
        "scherzosa di monte sulle parolacce **inglesi** digitate in chat. Non "
        "c'e' un italiano da agganciare senza inventare una lista di "
        "parolacce nostra, che sarebbe una decisione nuova e non una resa."),
    "net.hsp:netbuf": Dichiarazione(
        "esente", 2, "`<!--START-->` e la riga vuota: delimitatori della "
        "risposta del server degli aggiornamenti."),
    "scene.hsp:s": Dichiarazione(
        "esente", 2, "`{chat_` e `{actor_`: i segnaposto delle scene."),
    "system.hsp:txtbuff": Dichiarazione(
        "esente", 2, "`%Elona Custom Item` e `%Elona Custom Npc`: "
        "l'intestazione che dichiara di che tipo e' il file dell'utente."),
    "tcg_custom.hsp:cardrefsex": Dichiarazione(
        "esente", 2,
        "`Male` -> `male` e `Female` -> `female` sulla carta della `@`: il "
        "valore arriva da `zisyousex`, cioe' dal sesso che il giocatore ha "
        "**digitato** lui, e la sostituzione serve solo a portarlo minuscolo."),
    "tcg_custom.hsp:cdatan": Dichiarazione(
        "esente", 2,
        "`Alhaz` e `Eleusis` dentro il NOME di un `CREATURE_ID_USER`: il nome "
        "di un CNPC lo scrive il giocatore nel suo file, e i due mazzi "
        "preparati stanno li' per chi usa quei due personaggi."),
    "command.hsp:description": Dichiarazione(
        "esente", 1, "La sequenza `\\n` dentro la descrizione: e' l'a capo."),
    "command.hsp:s": Dichiarazione(
        "esente", 1,
        "`ElonaPlus Custom-GX ` tolto dal titolo della finestra "
        "(`command.hsp:413`). ⓘ E' la stessa riga che resta dichiarata in "
        "`copertura` per `command.hsp`, ed e' un nome proprio."),
    "config.hsp:s": Dichiarazione(
        "esente", 1, "`key_set.` e' la chiave del file di configurazione."),
    "custom_itemlist.hsp:FileLoadString_1": Dichiarazione(
        "esente", 1, "`.ID` e' un campo del file della lista oggetti."),
    "help.hsp:netbuf": Dichiarazione(
        "esente", 1, "`<!--START-->`, come in `net.hsp`."),
    "help.hsp:s": Dichiarazione(
        "esente", 1, "`&quot;` e' l'entita' HTML della pagina scaricata."),
    "main.hsp:s": Dichiarazione(
        "esente", 1, "`&quot;`, come in `help.hsp`."),
    "map_func.hsp:fmapfile": Dichiarazione(
        "esente", 1, "`map\\` e' un pezzo di percorso."),
    "sound.hsp:musicfile": Dichiarazione(
        "esente", 1, "`.mp3` e' un'estensione."),
    "system.hsp:e": Dichiarazione(
        "esente", 1, "`<eof>` chiude il file."),
    "system.hsp:useritemtxt": Dichiarazione(
        "esente", 1, "`nodescription` e' il valore che il file dell'utente "
        "scrive quando la descrizione non c'e'."),

    # ---- seguite: la chiave e' venuta dietro alla resa -------------------
    "module.hsp:fix_wish_arg1": Dichiarazione(
        "seguita", 24,
        "⭐ I dodici prefissi inglesi di `fix_wish` (`card of `, `figure `, "
        "`golden doll`, `flesh doll`) piu' le **dodici forme italiane** che la "
        "toppa 772 ha aggiunto nella 138a (`carta di `, `statuetta `, "
        "`bambola dorata`, `bambola di carne`). E' il punto 12 della lista "
        "della 138a, chiuso; la 142a l'ha riaperto per sbaglio e ci ha perso "
        "una toppa, perche' aveva guardato il sorgente invece della build."),
    "command.hsp:inputlog": Dichiarazione(
        "seguita", 4,
        "Le due battute del desiderio (`god inside` / `dio dentro`, "
        "`man inside` / `persona dentro`), decise nella 142a leggendo la "
        "chiave dalla **risposta**. L'italiano sta in `or` accanto "
        "all'inglese: chi conosce il gioco di monte deve poter scrivere "
        "ancora «god inside»."),
    "chara_func.hsp:ndeathcause": Dichiarazione(
        "seguita", 2,
        "Le due cause di morte dello sbudellatore: la chiave cercata e' gia' "
        "quella italiana («perse la vita contro lo sbudellatore»)."),
    "tcg_skill.hsp:effdesc@tcg": Dichiarazione(
        "seguita", 2,
        "`Grido di battaglia` cercato **in `or`** con `Battlecry` dentro la "
        "descrizione dell'effetto: la forma giusta, e la stessa scelta delle "
        "battute del desiderio."),
    "tcg.hsp:rtvaln2": Dichiarazione(
        "seguita", 1,
        "`Tratti:  ` — l'etichetta che la 138a ha portato da `Bits:` a "
        "`Tratti:`, e la ricomposizione della scheda l'ha seguita."),
    "tcg.hsp:carddetailneffbk@tcg": Dichiarazione(
        "seguita", 1, "`Tratti:  `, come `rtvaln2`."),
    "tcg.hsp:bits@tcg": Dichiarazione(
        "seguita", 1, "`Tratti:  `, come `rtvaln2`."),
    "tcg.hsp:s@tcg": Dichiarazione(
        "seguita", 1, "`Effetto: `, la gemella di `Tratti:  `."),

    # ---- inutili: non aggancia piu' niente, e va bene cosi' --------------
    "command.hsp:listn": Dichiarazione(
        "inutile", 4,
        "⭐ La pagina dei tratti di un compagno: per un PNG il codice cambia "
        "` your` -> `il suo` e `You` -> `lui`, e in italiano non aggancia "
        "piu'. **Misurato, e non serve che agganci**: le descrizioni italiane "
        "degli incantamenti sono impersonali — «Aumenta Forza di 3.», «Riduce "
        "Volonta' di 2.» (`item_data.hsp:*item_encdetail`) — e vanno bene "
        "identiche per la `@` e per il compagno. L'inglese aveva bisogno di "
        "quel giro perche' scrive «You gain…». ⚠️ Chi un giorno rendesse una "
        "di quelle descrizioni alla seconda persona riaprirebbe il fronte, e "
        "questa rete non lo direbbe: legge la chiave, non il pagliaio."),

    # ---- fronte: lavoro aperto -------------------------------------------
    "command.hsp:cdatan": Dichiarazione(
        "seguita", 10,
        "⭐ Le cinque battute della professione «alchimista», CHIUSE nella "
        "143a: dieci righe candidate perche' ogni riga porta adesso due "
        "chiavi, l'inglese e l'italiana. Erano "
        "`instr(cdatan(CDATAN_FAKE_CLASS, CHARA_PLAYER), 0, \"lchemist\")` — "
        "il troncone senza la `a` iniziale, per pigliare anche `Alchemist`. "
        "La professione finta la **digita il giocatore** col desiderio "
        "(`action.hsp:13705`), e in italiano scrivera' «alchimista»: la "
        "chiave e' stata affiancata da `lchimista` — il troncone senza la prima "
        "lettera, come l'inglese — sull'esempio delle dodici classi e delle "
        "due battute del desiderio."),
    "action.hsp:cdatan": Dichiarazione(
        "seguita", 2,
        "⭐ La sesta battuta dell'«alchimista», la castagna: stessa chiave "
        "`lchemist`, stessa cura, chiusa nella 143a con `command.hsp:cdatan`."),
    "tcg_skill.hsp:carddetailneff@tcg": Dichiarazione(
        "seguita", 12,
        "⭐⭐ Il difetto preesistente di «ragon» — punto 9 della lista della "
        "138a — CHIUSO nella 143a, e questa rete e' lo strumento che l'ha "
        "misurato. `instr` cerca dentro il TESTO della carta, che adesso e' "
        "italiano, e in `db_card.hsp` «ragon» compariva ancora 4 volte, tutte "
        "«dragonewt»: l'effetto della cacciatrice di draghi agganciava per "
        "testo quei quattro e nient'altro. ⚠️ **E la decisione di glossario "
        "che il punto 9 diceva mancante c'era gia'**: `dragon` -> «drago», "
        "glossario riga 278, dalla 96a. Non serviva decidere: serviva portare "
        "la chiave dietro alla decisione, e sono le tre forme «drago», "
        "«Drago», «draghi» — non il troncone «rago», che avrebbe pigliato "
        "«mandragora» e «aragosta» e ucciso carte che non dovevano morire."),
    "custom_dmgpop.hsp:s@DP": Dichiarazione(
        "seguita", 4,
        "⭐⭐ Il fumetto del danno scrive il nome di un PNG su due righe sopra "
        "la testa, e per spezzarlo cercava ` the ` («Arnord the mercenary»). "
        "**Misurato**: nella build un ` the ` di giuntura non esiste piu', "
        "perche' il contratto dei nomi §4 dice che l'articolo lo porta il "
        "nome, e la composizione italiana e' `randomname() + \" \" + "
        "cdatan(CDATAN_NAME, rc)` in 152 siti di `db_creature.hsp` — «Arnord "
        "il mercenario». Il fumetto non spezzava piu' niente. Chiuso nella "
        "143a: `:238` prova la giuntura italiana, cioe' l'ARTICOLO, e prende "
        "quello che viene prima nella stringa. ⚠️ `:225` — il `the ` di testa "
        "dell'alias — resta com'e' **apposta**: l'inglese butta via il suo "
        "articolo perche' «the mercenary» da solo non si scrive, e l'italiano "
        "lo tiene perche' «il mercenario» si'. ⓘ E' il punto 7 della lista "
        "della 138a per la parte che riguarda il fumetto; la pezza «the The» "
        "di `tcg_custom.hsp:4566` era gia' chiusa, e nella build quella riga "
        "dice `randomname() + \", \" + random_title()`."),
}


def _marcatore(letterale: str) -> bool:
    return bool(_MARCATORE.match(letterale.strip()))


def _chiave(letterale: str) -> bool:
    """Un letterale che vale come CHIAVE: ha lettere latine e non e' formato."""
    if not letterale.strip():
        return False
    if _GIAPPONESE.search(letterale):
        return False
    if not _LATINO.search(letterale):
        return False
    return not _marcatore(letterale)


def _radice(pagliaio: str) -> str:
    """`cdatan(CDATAN_NAME, tc)` -> `cdatan`. L'indice non cambia la specie."""
    return re.split(r"[(\[\s]", pagliaio.strip())[0]


def _righe_del_file(percorso):
    """Le righe VIVE del file, gia' potate del commento in coda.

    ⚠️⚠️ Le famiglie di riga morta di `commenti.py` non sono un dettaglio qui,
    e ne servono DUE:

    - `command.hsp:2554`-`:2555` — `cnv_str listn(0, cnt), " your", his(tc, 1)`
      — sta dentro un blocco `/* ORIGINAL - BEGINNING … ENDING */`, spento dal
      mod BLOODYSHADE che due righe sotto lo riscrive;
    - `item_func.hsp:2041`-`:2131` — il pluralizzatore inglese, `"coffins"`,
      `"ves"`, `"ies"` — sta dentro un `if ( 0 ) { … }` **che l'ha scritto il
      progetto** (`genera_toppe_nomi.py:359`), perche' il plurale italiano
      arriva da `ioriginalnamerefplur`.

    ⭐ Senza la seconda questa rete avrebbe aperto un fronte di quattro righe
    sul codice che il progetto stesso ha spento: e' la trappola di leggere la
    build, ed e' il motivo per cui `commenti.righe_in_ramo_spento` esiste.
    """
    testo = percorso.read_bytes().decode("cp932")
    morte = righe_in_commento(percorso) | righe_in_ramo_spento(percorso)
    for numero, riga in enumerate(testo.splitlines(), 1):
        if numero in morte:
            continue
        colonna = colonna_commento_riga(riga)
        if colonna is not None:
            riga = riga[:colonna]
        nudo = riga.strip()
        if nudo.startswith(";"):
            continue
        yield numero, nudo


def _argomenti(testo: str, dentro_parentesi: bool) -> list[str]:
    """Spezza sulle virgole di primo livello: fuori dalle stringhe e dalle
    parentesi annidate. `instr(a, instr(b, 0, "x"), "y")` ha TRE argomenti, non
    cinque, e il terzo e' `"y"`.

    Con `dentro_parentesi` si ferma alla parentesi che chiude la chiamata; se no
    va fino a fine istruzione — la graffa che chiude un `if` a una riga sola.
    """
    argomenti, corrente = [], []
    profondita = 0
    in_stringa = False
    for carattere in testo:
        if carattere == '"':
            in_stringa = not in_stringa
        elif not in_stringa:
            if carattere in "([":
                profondita += 1
            elif carattere in ")]":
                if dentro_parentesi and profondita == 0:
                    break
                profondita -= 1
            elif carattere == "}" and profondita == 0:
                break
            elif carattere == "," and profondita == 0:
                argomenti.append("".join(corrente).strip())
                corrente = []
                continue
        corrente.append(carattere)
    argomenti.append("".join(corrente).strip())
    return argomenti


def _letterale_solo(argomento: str) -> str | None:
    """L'argomento e' UN letterale e basta? `"dragon"` si, `x + "a"` no."""
    nudo = argomento.strip()
    if len(nudo) < 2 or not nudo.startswith('"') or not nudo.endswith('"'):
        return None
    dentro = nudo[1:-1]
    return None if '"' in dentro else dentro


def candidati_di(nome: str, righe=None) -> list[dict]:
    """I candidati di un file: costrutto, pagliaio, chiave.

    ⚠️ Una riga puo' portarne piu' d'uno — `instr(s, 0, "a") | instr(s, 0, "b")`
    — e ognuno vale per se'.
    """
    if righe is None:
        righe = _righe_del_file(percorsi.BUILD_HSP / nome)
    trovati = []
    for numero, nudo in righe:
        occorrenze = [(m, True) for m in _APERTURA.finditer(nudo)]
        occorrenze += [(m, False) for m in _COMANDO.finditer(nudo)]
        for m, in_parentesi in sorted(occorrenze, key=lambda x: x[0].start()):
            costrutto = m.group(1).lower()
            posto_pagliaio, posto_chiave = _COSTRUTTI[costrutto]
            argomenti = _argomenti(nudo[m.end():], in_parentesi)
            if len(argomenti) <= posto_chiave:
                continue
            chiave = _letterale_solo(argomenti[posto_chiave])
            if chiave is None:
                # ⭐ La chiave costruita da un'espressione — quasi sempre una
                # `lang()`, a volte una concatenazione — non e' un candidato:
                # e' la FORMA GIUSTA, quella che il progetto usa per portarsi
                # dietro una chiave (le 75 parole del filtro automatico, i
                # marcatori di missione con `+ lang("JP", "EN")`). Si contano
                # in `chiavi_da_espressione()`, che e' il margine di questa
                # rete: dice quante ne stanno gia' a posto, invece di tacere.
                continue
            if not _chiave(chiave):
                continue
            pagliaio = argomenti[posto_pagliaio]
            trovati.append({
                "file": nome,
                "riga": numero,
                "costrutto": costrutto,
                "pagliaio": pagliaio,
                "radice": _radice(pagliaio),
                "chiavi": [chiave],
                "testo": nudo,
            })
    return trovati


def censimento() -> list[dict]:
    """Una riga per pagliaio E PER FILE, coi casi ordinati per numero.

    ⚠️ La chiave e' la coppia, non il solo nome della variabile: `s` in
    `custom_autopick.hsp` sono le 75 parole chiave del filtro automatico, che
    l'utente scrive nel suo file e che il progetto ha deciso di tradurre; `s` in
    `command.hsp` e' la versione del gioco dentro il titolo della finestra. Lo
    stesso nome, due specie diverse, e una dichiarazione sola direbbe il falso
    su una delle due.
    """
    per_coppia = defaultdict(list)
    for percorso in sorted(percorsi.BUILD_HSP.glob("*.hsp")):
        for caso in candidati_di(percorso.name, _righe_del_file(percorso)):
            per_coppia[(caso["file"], caso["radice"])].append(caso)
    righe = []
    for (nome_file, radice), casi in per_coppia.items():
        righe.append({
            "chiave": "%s:%s" % (nome_file, radice),
            "file": nome_file,
            "pagliaio": radice,
            "casi": sorted(casi, key=lambda c: c["riga"]),
            "quanti": len(casi),
        })
    return sorted(righe, key=lambda r: (-r["quanti"], r["chiave"]))


def chiavi_da_espressione() -> dict[str, int]:
    """Quante chiavi passano da una `lang()`, e quante da un'altra espressione.

    ⚠️ **E' il margine, e senza non si capisce il conto del fronte.** Il grosso
    delle chiavi che il progetto ha gia' sistemato non compare fra i candidati,
    perche' non e' piu' un letterale: `instr(s, 0, lang("すべての", " ogni "))`
    sono le 75 parole del filtro automatico, ed e' esattamente la forma che si
    vuole. Un referto che dicesse solo «12 righe nel fronte» lascerebbe credere
    che il resto non esista.
    """
    conti = {"lang": 0, "altra espressione": 0}
    for percorso in sorted(percorsi.BUILD_HSP.glob("*.hsp")):
        for numero, nudo in _righe_del_file(percorso):
            occorrenze = [(m, True) for m in _APERTURA.finditer(nudo)]
            occorrenze += [(m, False) for m in _COMANDO.finditer(nudo)]
            for m, in_parentesi in occorrenze:
                _, posto_chiave = _COSTRUTTI[m.group(1).lower()]
                argomenti = _argomenti(nudo[m.end():], in_parentesi)
                if len(argomenti) <= posto_chiave:
                    continue
                argomento = argomenti[posto_chiave]
                if _letterale_solo(argomento) is not None or '"' not in argomento:
                    continue
                conti["lang" if "lang(" in argomento else "altra espressione"] += 1
    return conti


def problemi(righe: list[dict] | None = None) -> list[str]:
    """Le tre cose che accendono il cancello. Lista vuota = tutto dichiarato.

    ⚠️ E' lo stesso cancello di `copertura.problemi`, `disegnate.problemi` e
    `salti.problemi`, su un quarto metro. Un censimento senza cancello e' una
    misura che invecchia.
    """
    if righe is None:
        righe = censimento()
    per_nome = {r["chiave"]: r for r in righe}
    guai = []
    for riga in righe:
        nome = riga["chiave"]
        dichiarata = DICHIARATI.get(nome)
        if dichiarata is None:
            esempio = riga["casi"][0]
            guai.append(
                "%s: %d righe cercano un letterale latino dentro questo "
                "pagliaio, e non c'e' nessuna dichiarazione in operandi.py. "
                "Esempio: riga %d, %s"
                % (nome, riga["quanti"], esempio["riga"],
                   " ".join(repr(k) for k in esempio["chiavi"])))
        elif dichiarata.casi != riga["quanti"]:
            guai.append(
                "%s: dichiarate %d righe, nella build ne sono %d. Una toppa ha "
                "mosso il codice sotto la dichiarazione, oppure il conto era "
                "sbagliato." % (nome, dichiarata.casi, riga["quanti"]))
    for nome in DICHIARATI:
        if nome not in per_nome:
            guai.append(
                "%s: dichiarato in operandi.py ma nella build non ha piu' "
                "nessuna riga candidata. La dichiarazione va tolta." % nome)
    return guai


def _stampa(righe, con_righe, solo=None):
    for riga in righe:
        if solo and solo not in (riga["chiave"], riga["pagliaio"]):
            continue
        dichiarata = DICHIARATI.get(riga["chiave"])
        segno = {"esente": "  ", "seguita": "✅", "inutile": "➖",
                 "fronte": "⚠️", None: "❓"}[
            dichiarata.tipo if dichiarata else None]
        print("%s %-46s %4d" % (segno, riga["chiave"], riga["quanti"]))
        if not (con_righe or solo):
            continue
        for caso in riga["casi"]:
            print("     %s:%d  [%s]  %s"
                  % (caso["file"], caso["riga"], caso["costrutto"],
                     " ".join(repr(k) for k in caso["chiavi"])))
            if solo:
                print("        %s" % caso["testo"][:140])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--righe", action="store_true",
                    help="elenca le righe di ogni pagliaio")
    ap.add_argument("--pagliaio",
                    help="un pagliaio solo (`file.hsp:nome` o `nome`), con le "
                         "righe intere")
    args = ap.parse_args()

    righe = censimento()
    _stampa(righe, args.righe, args.pagliaio)
    totale = sum(r["quanti"] for r in righe)

    per_tipo = defaultdict(int)
    for riga in righe:
        dichiarata = DICHIARATI.get(riga["chiave"])
        per_tipo[dichiarata.tipo if dichiarata else "non dichiarato"] += \
            riga["quanti"]
    print()
    print("     esente %d   ✅ seguita %d   ➖ inutile %d   ⚠️ FRONTE %d"
          % (per_tipo["esente"], per_tipo["seguita"], per_tipo["inutile"],
             per_tipo["fronte"]))
    if per_tipo["non dichiarato"]:
        print("  ❓ non dichiarato %d" % per_tipo["non dichiarato"])
    print("  %d righe candidate, su %d pagliai" % (totale, len(righe)))

    espressione = chiavi_da_espressione()
    print()
    print("  ⓘ E il margine: altre %d chiavi non sono letterali perche' "
          "passano da una `lang()`" % espressione["lang"])
    print("    — la forma giusta, e la piu' comune — piu' %d costruite da "
          "un'altra espressione." % espressione["altra espressione"])

    guai = problemi(righe)
    if guai:
        print()
        for guaio in guai:
            print("  ❌ %s" % guaio)
        print()
        print("  operandi: %d pagliai senza dichiarazione o col conto mosso"
              % len(guai))
    else:
        print()
        print("  operandi: ogni pagliaio e' dichiarato, e ogni conto torna")


if __name__ == "__main__":
    main()
