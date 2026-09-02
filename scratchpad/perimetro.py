# -*- coding: utf-8 -*-
"""Quanto manca alla traduzione completa, contando anche quel che sta fuori
perimetro: le descrizioni degli oggetti e i quattro file di `data/`.

⚠️ **Ci sono due risposte diverse alla domanda «a che punto siamo», e finche'
non si dice quale si sta dando il numero inganna.**

⚠️⚠️⚠️ **124a: LA PERCENTUALE NON E' PIU' UN RAPPORTO FRA UN CONTO VERO E UNA
STIMA.** Fino a ieri il referto diceva **91%**, e sbagliava due volte nello
stesso senso: metteva al denominatore le 2.832 descrizioni **una seconda volta**
(stanno gia' dentro `rese['db_item.hsp']` dalla 107a), e divideva un numeratore
vero per un denominatore stimato per difetto. Corretta la prima, veniva
**101%** — che almeno lo diceva ad alta voce. Adesso quel che resta si **conta**,
con lo stesso `estrai` che scrive il dizionario, e la risposta e' una
sottrazione: **26.159 fatte, 167 da fare, 99,4%**.

⭐ E' la terza volta che questo referto sbaglia, e tutte e tre nello stesso modo:
la 98a ci aveva trovato le rese dei file dati contate solo al denominatore, la
107a le 2.452 stringhe vuote, la 124a le descrizioni contate due volte. Ogni
volta, lavoro che non esisteva messo al denominatore di «a che punto siamo».

I due numeri storici (per capire la forma del problema, non lo stato di oggi):

- **Dentro il perimetro** — quel che passa da `lang()`, piu' i nomi di
  `db_item.hsp` — la traduzione era al **47%** quando questo file fu scritto.
  E' la risposta a «quanto manca del lavoro impostato», ed e' quella che danno
  `verifica --dizionario` e `avanzamento.md`.
- **Contando tutto il testo che il giocatore legge** si scendeva al **35%**,
  perche' due blocchi grossi non erano mai stati contati da nessuna parte:

  1. **Le descrizioni degli oggetti**: `db_item.hsp` le scrive come
     `description(0..3) = "..."` dentro un `if ( jp ) { ... } else { ... }`,
     **non** dentro `lang()`. `estrai.py` cerca `lang()`, quindi non le vede:
     non sono tradotte **e non risultano fra quelle da fare**. Sono 10.568
     righe, 5.284 per lingua. E' il testo lungo del rapporto d'identificazione.
  2. **I quattro file di `data/`**: `book.txt` (i 33 libri), `talk.txt` (i
     dialoghi legati alle aree), `exhelp.txt`, `board.txt`. Non stanno nel
     sorgente: il gioco li carica con `noteload` a runtime (`item.hsp:112`,
     `text.hsp:9360`, `help.hsp:227`, `command.hsp:8371`). `SPEC.md` §6 li
     chiama «aggiuntivi» e non li ha mai aperti.

💡 **In caratteri pesano molto piu' che in firme.** Le 5.284 descrizioni e i
67.184 caratteri inglesi dei libri sono **prosa continua**, non righe di log:
sommati valgono probabilmente piu' di tutto quello che e' stato tradotto finora.
La contropartita e' che sono il lavoro **meno insidioso** del progetto — niente
`name()` da accordare, niente participi che concordano col giocatore, niente
reti da far scattare. Il costo e' in volume, non in analisi.

⚠️ **Il conteggio delle firme e' una STIMA**, e sbaglia per difetto del 2-4%:
conta gli argomenti inglesi distinti di ogni `lang()` con un analizzatore di
parentesi, mentre `estrai.py` ne trova qualcuno in piu' (le righe con piu'
`lang()`, le forme annidate). Tarato sui file chiusi: `item_data.hsp` 318 su 318
esatto, `db_creature.hsp` 3.507 contro 3.651 vere, `text.hsp` 1.706 contro
1.738, `action.hsp` 1.266 contro 1.286.

    python scratchpad/perimetro.py
"""
import glob
import io
import json
import os
import re

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
DATI = r'C:\Games\Elona\elonaplus2.31\data'
DIZIONARIO = 'dizionario'

_LANG = re.compile(r'lang\s*\(')
_DESCRIZIONE = re.compile(r'^\s*description\(\d+\)\s*=')
_APRE_JP = re.compile(r'^if\s*\(\s*jp\s*\)')


def _salta_stringa(testo: str, i: int) -> int:
    """L'indice dopo la stringa che comincia in `i` (dove testo[i] == '"')."""
    i += 1
    while i < len(testo) and testo[i] != '"':
        i += 1
    return i + 1


def firme_lang(testo: str) -> set:
    """Gli argomenti INGLESI distinti di ogni `lang()`: approssima la firma."""
    fuori = set()
    for trovato in _LANG.finditer(testo):
        i = trovato.end()
        livello, j = 1, i
        while j < len(testo) and livello > 0:
            if testo[j] == '"':
                j = _salta_stringa(testo, j)
                continue
            if testo[j] == '(':
                livello += 1
            elif testo[j] == ')':
                livello -= 1
            j += 1
        argomenti = testo[i:j - 1]
        # la virgola di primo livello separa il giapponese dall'inglese
        livello, taglio, k = 0, -1, 0
        while k < len(argomenti):
            c = argomenti[k]
            if c == '"':
                k = _salta_stringa(argomenti, k)
                continue
            if c == '(':
                livello += 1
            elif c == ')':
                livello -= 1
            elif c == ',' and livello == 0:
                taglio = k
                break
            k += 1
        if taglio > 0:
            fuori.add(argomenti[taglio + 1:].strip())
    return fuori


def descrizioni_oggetto() -> tuple[int, int]:
    """(righe del ramo inglese, descrizioni VIVE) di `db_item.hsp`.

    ⚠️⚠️ **Dalla 107a non si contano piu' a mano.** Fino a ieri questo modulo
    aveva un automa suo, che rendeva **5.284** — cioe' tutte le righe, comprese
    le **2.452 che sono la stringa vuota**. Non era una stima per difetto come
    quella delle firme `lang()`: era il 46% di lavoro che non esiste, messo al
    denominatore di «a che punto siamo». Adesso il riconoscitore vero sta in
    `estrai.descrizioni_per_riga` (vedi `strumenti/tests/test_descrizioni.py`) e
    le vuote le scarta `siti()`, come per i nomi.
    """
    from strumenti.estrai import descrizioni_per_riga, spezza_righe
    testo = io.open(os.path.join(SORGENTE, 'db_item.hsp'), encoding='cp932').read()
    righe, _, _ = spezza_righe(testo)
    trovate = descrizioni_per_riga(righe)
    vive = sum(1 for dati in trovate.values() if dati[1] != '""')
    return len(trovate), vive


def file_esterni() -> dict:
    """Righe e caratteri della sezione EN dei quattro file di `data/`."""
    # `book.txt` marca le sezioni `%<n>,EN`, `talk.txt` `%AREA,<n>,EN`
    marca = re.compile(r'^%[A-Za-z]*,?\d*,?(JP|EN)\s*(/.*)?$')
    fuori = {}
    for nome in ('book.txt', 'talk.txt', 'exhelp.txt', 'board.txt'):
        percorso = os.path.join(DATI, nome)
        if not os.path.exists(percorso):
            continue
        sezione, righe, caratteri = None, 0, 0
        for riga in io.open(percorso, encoding='cp932', errors='replace').read().split('\n'):
            s = riga.strip()
            trovata = marca.match(s)
            if trovata:
                sezione = trovata.group(1)
                continue
            if s.startswith('%'):
                sezione = None
                continue
            if sezione == 'EN' and s:
                righe += 1
                caratteri += len(riga)
        fuori[nome] = (righe, caratteri)
    return fuori


def _file_senza(rese: dict) -> list:
    """I file .hsp che portano `lang()` e non hanno un dizionario."""
    fuori = []
    for percorso in sorted(glob.glob(os.path.join(SORGENTE, '*.hsp'))):
        nome = os.path.basename(percorso)
        if nome in rese:
            continue
        if firme_lang(io.open(percorso, encoding='cp932', errors='replace').read()):
            fuori.append(nome)
    return fuori


def _da_fare_davvero(rese: dict) -> int:
    """Le firme che restano, contate col riconoscitore VERO, non con la stima.

    ⚠️ `firme_lang()` qui sopra approssima (sbaglia per difetto del 2-4%) e
    conta anche le `lang()` che non portano nessun letterale — il carattere,
    un valore gia' reso altrove. `estrai` no: e' lo stesso codice che scrive il
    dizionario, quindi «fatte + da fare» sono due numeri della stessa specie.
    """
    from strumenti.estrai import estrai_da_testo
    firme = set()
    for nome in _file_senza(rese):
        testo = io.open(os.path.join(SORGENTE, nome), encoding='cp932',
                        errors='replace').read()
        for voce in estrai_da_testo(nome, testo):
            firme.add(voce['firma'])
    return len(firme)


def main() -> None:
    rese = {}
    for percorso in sorted(glob.glob(os.path.join(DIZIONARIO, '*.jsonl'))):
        nome = os.path.basename(percorso).replace('.jsonl', '')
        rese[nome] = sum(1 for l in io.open(percorso, encoding='utf-8')
                         if l.strip() and json.loads(l).get('it'))
    fatte = sum(rese.values())

    dentro = fuori_dizionario = 0
    for percorso in sorted(glob.glob(os.path.join(SORGENTE, '*.hsp'))):
        nome = os.path.basename(percorso)
        quante = len(firme_lang(io.open(percorso, encoding='cp932').read()))
        if not quante:
            continue
        dentro += quante
        if nome not in rese:
            fuori_dizionario += quante

    # ⚠️⚠️ LE RESE DEI FILE DATI STANNO IN UN'ALTRA CARTELLA, E FINO ALLA 98a
    # ERANO SOLO AL DENOMINATORE. `dizionario/dati/*.jsonl` non lo prendeva la
    # glob qui sopra, quindi le 779 righe gia' rese di `board.txt`, `talk.txt` ed
    # `exhelp.txt` pesavano nel totale come lavoro DA FARE. Il referto diceva 70%
    # con tre file su quattro finiti: uno zero uniforme e' una domanda posta al
    # posto sbagliato, e questo era il suo gemello al numeratore.
    rese_dati = {}
    for percorso in sorted(glob.glob(os.path.join(DIZIONARIO, 'dati', '*.jsonl'))):
        nome = os.path.basename(percorso).replace('.jsonl', '')
        rese_dati[nome] = sum(1 for l in io.open(percorso, encoding='utf-8')
                              if l.strip() and json.loads(l).get('it'))
    fatte_dati = sum(rese_dati.values())

    nomi_oggetto = rese.get('db_item.hsp', 0)   # non passa da lang()
    righe_descrizione, descrizioni = descrizioni_oggetto()
    esterni = file_esterni()
    righe_esterne = sum(r for r, _ in esterni.values())
    caratteri_esterni = sum(c for _, c in esterni.values())

    # ⭐ Dalla 107a le descrizioni sono DENTRO il perimetro: `estrai.siti()` le
    # vede, `verifica` le conta, la prova d'identita' le attraversa. Il numero
    # sotto quindi **scende**, ed e' il primo calo onesto del progetto: prima
    # 2.832 stringhe che il giocatore legge stavano fuori dal denominatore.
    # ⚠️⚠️⚠️ **124a: QUI LE DESCRIZIONI SI CONTAVANO DUE VOLTE, E IL REFERTO
    # DICEVA 91% DOVE SIAMO AL 99%.** `nomi_oggetto` non e' un conto del
    # sorgente: e' `rese['db_item.hsp']`, cioe' **tutte** le voci del dizionario
    # di quel file — e dalla 107a le descrizioni stanno **dentro** quel
    # dizionario (2.831 rese su 4.407 voci; le altre 1.576 sono i nomi).
    # Sommare `descrizioni` accanto le metteva al denominatore una seconda
    # volta, mentre al numeratore stavano una volta sola: 2.832 di lavoro
    # inesistente, cioe' il 10% del progetto.
    # ⭐ E' lo stesso guasto della 98a («le rese dei file dati stavano solo al
    # denominatore») e della 107a («le 2.452 stringhe vuote stavano al
    # denominatore»), alla terza ripetizione: ogni volta che questo referto ha
    # sbagliato, ha sbagliato mettendo al denominatore lavoro che non c'era.
    # ⓘ Trovato perche' l'utente ha chiesto «siamo quasi alla fine?» e i due
    # modi di rispondere non tornavano: il referto diceva che mancava il 9%
    # (2.563 firme) e `verifica --dizionario` diceva che ogni file col
    # dizionario e' chiuso e che fuori ne restano **174**.
    perimetro = dentro + nomi_oggetto
    totale = perimetro + righe_esterne

    print(f'firme rese                          : {fatte:>7}')
    print(f'firme lang() stimate nel sorgente   : {dentro:>7}')
    print(f'  di cui in file mai estratti       : {fuori_dizionario:>7}')
    print(f'nomi di db_item.hsp (senza lang())  : {nomi_oggetto:>7}')
    print(f'--- perimetro STIMATO               : {perimetro:>7}   '
          f'(la stima sbaglia per difetto del 2-4%: vedi in testa)')
    print()
    # ⚠️⚠️⚠️ **124a: LA PERCENTUALE NON SI RICAVA PIU' DA QUESTA STIMA.** Il
    # numeratore e' un conto VERO (le voci di dizionario con `it`) e il
    # denominatore era una STIMA per difetto: il rapporto dei due non e' una
    # percentuale, e' un'illusione ottica — con la stima corretta della doppia
    # contatura veniva **101%**, che almeno lo dice ad alta voce.
    # ⭐ Il conto onesto e' una sottrazione, non un rapporto: quel che resta si
    # CONTA, con lo stesso riconoscitore che scrive il dizionario
    # (`estrai --da-tradurre` sui file che un dizionario non ce l'hanno), e il
    # denominatore diventa «fatte + da fare».
    da_fare = _da_fare_davvero(rese)
    print(f'firme ancora DA FARE, contate con estrai: {da_fare:>4}   '
          f'({", ".join(_file_senza(rese)) or "nessun file"})')
    print(f'--- fatto: {fatte} su {fatte + da_fare}   '
          f'= {100 * fatte / (fatte + da_fare):.1f}%')
    print()
    print(f'  di cui descrizioni di oggetto     : {descrizioni:>7}   '
          f'vive su {righe_descrizione} righe — GIA\' DENTRO la riga qui sopra,')
    print(f'{"":38}   non si sommano di nuovo (vedi il commento, 124a)')
    print()
    for nome, (righe, caratteri) in esterni.items():
        quante = rese_dati.get(nome, 0)
        stato = '⭐ CHIUSO' if quante >= righe else f'{quante} rese'
        print(f'  data/{nome:<24}{righe:>7} righe EN, {caratteri:>6} caratteri   {stato}')
    print(f'--- TOTALE coi file dati: {fatte + fatte_dati} su '
          f'{fatte + fatte_dati + da_fare}   '
          f'= {100 * (fatte + fatte_dati) / (fatte + fatte_dati + da_fare):.1f}%')
    print()
    print(f'⚠️ le {descrizioni} descrizioni e i {caratteri_esterni} caratteri esterni sono '
          'PROSA: in caratteri pesano molto piu\' che in firme.')
    print('⚠️⚠️ E QUESTO 99% E\' IL PERIMETRO, NON IL PROGETTO. Dice che le stringhe')
    print('   che qualcuno ha chiesto sono rese; NON dice che siano state viste a')
    print('   schermo (il debito di collaudo sta in RIPRESA-sessione.md), ne\' che')
    print('   non esistano fronti che nessuno ha ancora chiesto — la 123a ne ha')
    print('   trovato uno da 355 firme quando il referto diceva «TOTALE da fare 0».')


if __name__ == '__main__':
    main()
