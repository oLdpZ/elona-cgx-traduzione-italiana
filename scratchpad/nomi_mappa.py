# -*- coding: utf-8 -*-
"""Il nome della mappa nella barra in basso, e il tetto che nessuna rete guarda.

Il **tredicesimo punto cieco**, trovato col collaudo della 62a guardando il
piede della schermata del pannello degli dei: la barra diceva «La Terra della
T». Non e' un difetto della resa: e' `screen.hsp:153`, che taglia con `strmid`.

    if ( strlen(mdatan(MDATAN_NAME)) > 16 - (maplevel() != "") * 4 ) {
        mes cnven(strmid(mdatan(MDATAN_NAME), 0, 16 - (maplevel() != "") * 4))
    }

Cioe':

- **16 caratteri** per una mappa senza numero di piano (citta', campi, i posti
  fissi come la Terra della Tregua);
- **12** per una che il piano ce l'ha (`maplevel()` non vuoto: Lesimas, i nefia
  generati, le stanze di missione, la propria casa sotto il primo piano).

Il taglio e' netto, senza puntini: il nome si interrompe a meta' parola. E si
legge **a ogni schermata del gioco**, sempre, in ogni mappa.

⚠️ **Non e' `larghezze.py`**, che misura le voci dei menu di `*prompt_key`; non
e' `riquadri.py`, che misura le piastrelle di stato dell'HUD accanto a questa
barra; non e' `linguette.py`. Nessuna delle tre guarda `mdatan`.

⚠️ **E il tetto e' in caratteri, non in pixel.** Lo spazio fisico e' di 90 px
(`screen.hsp:152` scrive il nome a `inf_raderw + 24`, `:160` il piano a
`inf_raderw + 114`), che a 6 px per carattere — Courier New a corpo 10, cioe'
`12 + sizefix - en * 2` — sono 15 caratteri: il `strmid` a 16 e' gia' un
capello oltre lo spazio. Allargarlo con una toppa non si puo'.

## Da dove vengono i nomi

`map.hsp:1331` e `:1406` riempiono `mdatan(MDATAN_NAME)` con `mapname()`
(`text.hsp:2734`), che e' l'elenco dei posti fissi; altrove il nome viene
assegnato dritto — le mappe generate (`map_rand.hsp`) e alcune stanze speciali.
Questo referto guarda tutt'e due le forme.

## Struttura e da fare

Come `nudi_en.py`, sono due misure diverse:

- **struttura**: quanti nomi ci sono, e quanti gia' l'inglese di monte ne taglia
  (upstream ha scritto lui il tetto: se lo sfora, il tetto e' finto);
- **da fare**: quanti ne taglia l'italiano della build.

⚠️ La misura si prende sul **nome**, non sulla riga: una riga di `mapname` porta
spesso anche la descrizione della mappa del mondo, che il tetto non riguarda.
E' la lezione della 61a — misurare la cosa e non una cosa vicina.
"""
import io
import os
import re
import sys

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'

TETTO = 16
TETTO_CON_PIANO = 12

# `s = lang("...", "...")` dentro *mapname*: il PRIMO lang() e' il nome, il
# secondo (quando c'e') e' la descrizione della mappa del mondo.
_ASSEGNA_S = re.compile(r'^\s*s\s*=\s*(.+)$')
_ASSEGNA_MDATAN = re.compile(r'^\s*mdatan\(\s*(?:MDATAN_NAME|0)\s*\)\s*=\s*(.+)$')
_LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')
_NUDO = re.compile(r'^"((?:[^"\\]|\\.)*)"\s*$')


def leggi(percorso):
    with io.open(percorso, encoding='cp932', errors='replace') as f:
        return f.read().split('\n')


def blocco_mapname(righe):
    """Le righe di `#defcfunc mapname`, con il loro numero (1-based)."""
    dentro = False
    for n, riga in enumerate(righe, 1):
        if riga.startswith('#defcfunc mapname '):
            dentro = True
            continue
        if dentro and re.match(r'^#(defcfunc|deffunc|module|global)', riga):
            break
        if dentro:
            yield n, riga


def nome_di(coda):
    """(chiave, nome) per l'assegnazione, o None.

    ⚠️ La chiave e' il **giapponese**, non il numero di riga: `applica` non
    conserva il conto delle righe (map.hsp ne ha cinque in piu' nella build,
    text.hsp una), quindi giungere sorgente e build per riga accoppia posti
    diversi. Il giapponese invece non lo tocca nessuno.
    """
    m = _LANG.search(coda)
    if m:
        return m.group(1), m.group(2)   # (giapponese, campo che la build
                                        #  rimpiazza con l'italiano)
    m = _NUDO.match(coda.strip())
    if m:
        return m.group(1), m.group(1)   # un nudo: chiave e nome coincidono
    return None


def raccogli(radice):
    """{ (file, giapponese): (riga, nome) } per ogni posto che scrive il nome."""
    fuori = {}

    def aggiungi(nomefile, n, coda):
        esito = nome_di(coda)
        if not esito:
            return
        chiave, nome = esito
        if not nome.strip():        # `s = "", ""` in cima a mapname
            return
        k = (nomefile, chiave)
        while k in fuori:               # stesso giapponese due volte nel file
            k = (k[0], k[1] + '\x00')
        fuori[k] = (n, nome)

    righe = leggi(os.path.join(radice, 'text.hsp'))
    for n, riga in blocco_mapname(righe):
        m = _ASSEGNA_S.match(riga)
        if m:
            aggiungi('text.hsp', n, m.group(1))

    for nomefile in sorted(os.listdir(radice)):
        if not nomefile.endswith('.hsp'):
            continue
        for n, riga in enumerate(leggi(os.path.join(radice, nomefile)), 1):
            m = _ASSEGNA_MDATAN.match(riga)
            if m:
                aggiungi(nomefile, n, m.group(1))

    return fuori


def referto(etichetta, nomi):
    troppo = {k: v for k, v in nomi.items() if len(v[1]) > TETTO}
    stretti = {k: v for k, v in nomi.items()
               if TETTO_CON_PIANO < len(v[1]) <= TETTO}
    print(f'--- {etichetta}: {len(nomi)} nomi di mappa')
    print(f'    oltre {TETTO} (tagliati sempre)        : {len(troppo)}')
    print(f'    fra {TETTO_CON_PIANO + 1} e {TETTO} '
          f'(tagliati se la mappa ha il piano): {len(stretti)}')
    return troppo, stretti


def main(argv):
    sorgente = raccogli(SORGENTE)
    build = raccogli(BUILD)

    orfani = [k for k in build if k not in sorgente]
    print('IL NOME DELLA MAPPA NELLA BARRA IN BASSO (screen.hsp:153)')
    print(f'tetto: {TETTO} caratteri, {TETTO_CON_PIANO} se la mappa ha il piano')
    if orfani:
        print(f'⚠️ {len(orfani)} nomi della build senza gemello nel sorgente: '
              f'{orfani[:3]}')
    print()
    troppo_en, stretti_en = referto("l'inglese di monte", sorgente)
    print()
    troppo_it, stretti_it = referto("la build italiana", build)
    print()

    if '--tutti' in argv:
        print("=== l'inglese di monte, oltre il tetto ===")
        for k, (n, v) in sorted(troppo_en.items(), key=lambda kv: -len(kv[1][1])):
            print(f'  {len(v):3d}  {k[0]}:{n:<6d} {v}')
        print()

    print('=== la build italiana, oltre il tetto ===')
    for k, (n, v) in sorted(troppo_it.items(), key=lambda kv: -len(kv[1][1])):
        en = sorgente.get(k, (0, ''))[1]
        stato = '' if len(en) > TETTO else '   <- l\'inglese ci stava'
        print(f'  {len(v):3d}  {k[0]}:{n:<6d} {v}')
        print(f'       a schermo: "{v[:TETTO]}"   (en {len(en):3d}: {en}){stato}')

    if '--stretti' in argv:
        print()
        print('=== la build italiana, fra 13 e 16 (solo se la mappa ha il piano) ===')
        for k, (n, v) in sorted(stretti_it.items(), key=lambda kv: -len(kv[1][1])):
            print(f'  {len(v):3d}  {k[0]}:{n:<6d} {v}')


if __name__ == '__main__':
    main(sys.argv[1:])
