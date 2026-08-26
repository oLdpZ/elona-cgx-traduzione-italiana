# -*- coding: utf-8 -*-
"""Quanto manca alla traduzione completa, contando anche quel che sta fuori
perimetro: le descrizioni degli oggetti e i quattro file di `data/`.

⚠️ **Ci sono due risposte diverse alla domanda «a che punto siamo», e finche'
non si dice quale si sta dando il numero inganna.**

- **Dentro il perimetro** — quel che passa da `lang()`, piu' i nomi di
  `db_item.hsp` — la traduzione e' a circa il **47%**. E' la risposta a «quanto
  manca del lavoro impostato», ed e' quella che danno `verifica --dizionario` e
  `avanzamento.md`.
- **Contando tutto il testo che il giocatore legge** si scende al **35%**,
  perche' due blocchi grossi non sono mai stati contati da nessuna parte:

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
    vive = sum(1 for _, en, _, _ in trovate.values() if en != '""')
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
    perimetro = dentro + nomi_oggetto + descrizioni
    totale = perimetro + righe_esterne

    print(f'firme rese                          : {fatte:>7}')
    print(f'firme lang() stimate nel sorgente   : {dentro:>7}')
    print(f'  di cui in file mai estratti       : {fuori_dizionario:>7}')
    print(f'nomi di db_item.hsp (senza lang())  : {nomi_oggetto:>7}')
    print(f'--- perimetro dichiarato            : {perimetro:>7}   '
          f'fatto {100 * fatte / perimetro:.0f}%')
    print()
    print(f'descrizioni di oggetto (ramo EN)    : {descrizioni:>7}   '
          f'vive su {righe_descrizione} righe (107a: ora nel perimetro)')
    for nome, (righe, caratteri) in esterni.items():
        quante = rese_dati.get(nome, 0)
        stato = '⭐ CHIUSO' if quante >= righe else f'{quante} rese'
        print(f'  data/{nome:<24}{righe:>7} righe EN, {caratteri:>6} caratteri   {stato}')
    print(f'--- TOTALE col testo fuori perimetro: {totale:>7}   '
          f'fatto {100 * (fatte + fatte_dati) / totale:.0f}%')
    print()
    print(f'⚠️ le {descrizioni} descrizioni e i {caratteri_esterni} caratteri esterni sono '
          'PROSA: in caratteri pesano molto piu\' che in firme.')
    print('⚠️ 107a: i due numeri si muovono in DIREZIONI OPPOSTE, e non e\' un errore.')
    print('   Il PERIMETRO scende (100% -> 90%) perche\' 2.832 stringhe vere ci sono')
    print('   entrate. Il TOTALE sale (86% -> 93%) perche\' ne sono uscite 2.452 che')
    print('   sono la stringa VUOTA: l\'86% di ieri aveva al denominatore mezzo file')
    print('   di lavoro che non esiste. Il salto non e\' progresso, e\' un conto giusto.')


if __name__ == '__main__':
    main()
