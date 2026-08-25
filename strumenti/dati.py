# strumenti/dati.py
"""Il formato a blocchi dei file di `elonaplus2.31\\data\\`.

Questo modulo e' **l'unico posto del progetto che sa com'e' fatto quel
formato**. Tutto il resto — l'estrazione del lotto, l'applicazione del
dizionario, le reti — lavora su `Documento` e `Blocco` senza guardare il testo.

Il formato, contato sul corpus (board.txt, book.txt, exhelp.txt, talk.txt):

    %COOK,GENERAL,EN            intestazione: chiave, poi la lingua
    A new recipe!:As in the...  le righe del blocco
    %END                        chiusura (talk.txt usa anche `%END%`)

Fuori dai blocchi il file puo' avere qualunque cosa — commenti, righe vuote, la
documentazione che monte ci ha scritto dentro — e va conservata com'e'.

⚠️ **Il round-trip si misura sui byte.** I file dati vogliono i CRLF, perche'
`noteinfo(0)` di HSP conta le righe sui CRLF e un file a LF soltanto per HSP e'
**una riga sola** (lezione della 65a: due CSV scritti a LF piantarono il gioco
alla creazione del personaggio). Per questo il documento tiene le righe **coi
loro fine-riga attaccati**: `"".join(righe)` ridà il testo di partenza qualunque
cosa ci fosse dentro, compreso un file che non finisce con un a-capo.

Chi legge un blocco vuole quasi sempre le sue righe **piene**, cioe' senza le
vuote: sono quelle che il gioco pesca (`text.hsp:11654` fa `rnd(noteinfo(0) - 1)
+ 1`, e una riga vuota pescata sarebbe un incarico vuoto).
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

CHIUSURA = "%END"

# ⚠️⚠️ **`autopick.txt` non e' come gli altri quattro, e in due modi.**
#
# 1. E' scritto in **UTF-8**, l'unico di `data\` a esserlo: i suoi 4.516 byte
#    non si decodificano in CP932 (`illegal multibyte sequence` al byte 3153) e
#    la sezione giapponese di monte, letta col font del gioco, e' gia' mojibake
#    per conto suo. Non e' una nostra scelta: e' il file che l'eseguibile legge.
# 2. **Non ha blocchi.** Niente `%CHIAVE,LINGUA` … `%END`: e' un file di
#    configurazione — commenti con `#` e regole di raccolta — che il gioco copia
#    nel salvataggio (`custom_autopick.hsp:41`) e che poi apre nell'editor di
#    testo del giocatore. Nessuna riga di questo file viene mai **disegnata**
#    dal gioco, e per questo qui gli accenti veri si possono tenere.
#
# ⚠️ La conseguenza che conta: `degrada()` esiste **perche' CP932 cancella le
# vocali accentate**, quindi si applica solo dove la codifica e' CP932.
CODIFICHE = {"autopick.txt": "utf-8"}
PIATTI = {"autopick.txt"}


def codifica(nome_file: str) -> str:
    return CODIFICHE.get(nome_file, "cp932")


def e_piatto(nome_file: str) -> bool:
    """Vero se il file non ha blocchi e va letto come un testo unico."""
    return nome_file in PIATTI


def leggi(percorso: Path | str, nome_file: str | None = None) -> str:
    """Il testo di un file dati, nella codifica che quel file ha davvero."""
    percorso = Path(percorso)
    return percorso.read_bytes().decode(codifica(nome_file or percorso.name))


def scrivi(percorso: Path | str, testo: str, nome_file: str | None = None) -> None:
    percorso = Path(percorso)
    percorso.write_bytes(testo.encode(codifica(nome_file or percorso.name)))


@dataclass
class Blocco:
    """Un blocco `%CHIAVE,LINGUA` … `%END` dentro un file dati."""

    chiave: str
    lingua: str
    intestazione: int          # indice della riga `%…`
    indici: list[int] = field(default_factory=list)   # le righe di contenuto
    chiusura: int | None = None                       # indice della riga `%END`
    _documento: "Documento | None" = field(default=None, repr=False, compare=False)

    def righe(self) -> list[str]:
        """Le righe di contenuto, senza il fine-riga, comprese le vuote."""
        assert self._documento is not None
        return [self._documento.riga(i) for i in self.indici]

    def righe_piene(self) -> list[str]:
        """Le righe che portano qualcosa: quelle che il gioco puo' pescare."""
        return [r for r in self.righe() if r.strip()]

    def indici_pieni(self) -> list[int]:
        """Gli indici delle righe piene, nell'ordine in cui stanno nel file."""
        assert self._documento is not None
        return [i for i in self.indici if self._documento.riga(i).strip()]


@dataclass
class Documento:
    """Un file dati: le sue righe (coi fine-riga) e i blocchi che contiene."""

    _righe: list[str]
    blocchi: list[Blocco]

    # ------------------------------------------------------------- lettura

    def riga(self, indice: int) -> str:
        """La riga `indice` senza il suo fine-riga."""
        return _spoglia(self._righe[indice])[0]

    def testo(self) -> str:
        return "".join(self._righe)

    def blocco(self, chiave: str, lingua: str) -> Blocco | None:
        for blocco in self.blocchi:
            if blocco.chiave == chiave and blocco.lingua == lingua:
                return blocco
        return None

    # ----------------------------------------------------------- scrittura

    def sostituisci(self, indice: int, nuovo: str) -> None:
        """Rimpiazza il contenuto della riga `indice`, tenendole il fine-riga.

        Rifiuta quel che spaccherebbe il formato: un a-capo dentro la resa
        creerebbe una riga in piu' dentro il blocco — e il gioco ne pesca una a
        caso, quindi mezzo incarico — e una resa che comincia per `%` verrebbe
        letta come una chiusura o una intestazione nuova.
        """
        if "\n" in nuovo or "\r" in nuovo:
            raise ValueError(
                f"riga {indice}: la resa contiene un a-capo, e spaccherebbe il blocco in due"
            )
        if nuovo.lstrip().startswith("%"):
            raise ValueError(
                f"riga {indice}: la resa comincia per '%', e verrebbe letta come intestazione o chiusura"
            )
        _, fine = _spoglia(self._righe[indice])
        self._righe[indice] = nuovo + fine


def _spoglia(riga: str) -> tuple[str, str]:
    """Divide una riga nel suo contenuto e nel suo fine-riga."""
    for fine in ("\r\n", "\n", "\r"):
        if riga.endswith(fine):
            return riga[: -len(fine)], fine
    return riga, ""


def _intestazione(contenuto: str) -> tuple[str, str] | None:
    """Da `%AREA,5,EN\\t\\t\\t/Vernis` a `("AREA,5", "EN")`.

    Restituisce None se la riga non e' una intestazione di blocco.

    ⚠️ I percento in testa si tolgono **tutti**: `talk.txt` ha un
    `%%SKILLTRAINER,JP` che e' un refuso di monte, e il gioco lo aggancia lo
    stesso perche' cerca `"%" + chiave + ",EN"` come sottostringa. Un parser che
    tenesse il percento in piu' inventerebbe una chiave che nessuno cerca.
    """
    if not contenuto.startswith("%") or contenuto.startswith(CHIUSURA):
        return None
    # il commento di servizio comincia con le tabulazioni: `%AREA,5,EN\t\t/Vernis`
    testa = contenuto.split("\t")[0].strip()
    campi = testa.lstrip("%").split(",")
    if len(campi) > 1 and campi[-1] in ("JP", "EN"):
        return ",".join(campi[:-1]), campi[-1]
    return ",".join(campi), ""


def analizza(testo: str) -> Documento:
    """Legge un file dati. `serializza(analizza(t)) == t`, sempre."""
    righe = testo.splitlines(keepends=True)
    documento = Documento(_righe=righe, blocchi=[])
    aperto: Blocco | None = None

    for indice, grezza in enumerate(righe):
        contenuto, _ = _spoglia(grezza)

        if contenuto.startswith(CHIUSURA):
            if aperto is not None:
                aperto.chiusura = indice
                aperto = None
            continue

        testa = _intestazione(contenuto)
        if testa is not None:
            # un blocco rimasto aperto si chiude d'ufficio qui: meglio che
            # inghiottire tutto il resto del file
            chiave, lingua = testa
            aperto = Blocco(chiave=chiave, lingua=lingua, intestazione=indice, _documento=documento)
            documento.blocchi.append(aperto)
            continue

        if aperto is not None:
            aperto.indici.append(indice)

    return documento


def analizza_piatto(testo: str) -> Documento:
    """Un file senza blocchi: tutto il file e' **un** blocco inglese implicito.

    Serve a `autopick.txt`, che di blocchi non ne ha. La chiave e' vuota e la
    lingua e' `EN`, cosi' tutto il resto della catena — l'estrazione, la firma,
    l'applicazione, la prova d'identita' — funziona senza sapere che questo file
    e' diverso.

    ⚠️ Le righe vuote restano fuori come nei file a blocchi (`righe_piene`), e
    la numerazione e' su quelle piene: una riga vuota aggiunta da monte non
    sposta la firma di tutte quelle che vengono dopo.
    """
    righe = testo.splitlines(keepends=True)
    documento = Documento(_righe=righe, blocchi=[])
    blocco = Blocco(chiave="", lingua="EN", intestazione=-1,
                    indici=list(range(len(righe))), _documento=documento)
    documento.blocchi.append(blocco)
    return documento


def analizza_file(nome_file: str, testo: str) -> Documento:
    """Il documento di un file dati, col lettore che quel file vuole."""
    return analizza_piatto(testo) if e_piatto(nome_file) else analizza(testo)


def serializza(documento: Documento) -> str:
    return documento.testo()
