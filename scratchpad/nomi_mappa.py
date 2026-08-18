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


# ---- il tetto vero: 16, oppure 12 se la mappa mostra il numero di piano ----
#
# `maplevel()` (`text.hsp:2595`) non e' vuoto quando la mappa non e' una citta'
# **e** e' Lesimas, un nefia generato, una missione, o ha un `MDATA_TYPE` fra
# MAP_TYPE_DUNGEON_MIN e MAP_TYPE_DUNGEON_MAX. Il tipo lo dichiara la tavola
# delle aree in `map.hsp` (`adata(ADATA_TYPE, p) = MAP_TYPE_...`).
#
# ⚠️ **`MAP_TYPE_QUEST` non ci sta.** La condizione di `maplevel()` guarda
# l'*identificativo* `AREA_QUEST`, non il tipo, e il tipo QUEST vale 7: fuori
# dall'intervallo 20-27 dei sotterranei. Metterlo qui dava il piano all'Arena
# delle Bestie e alla Cupola delle Case, che non ce l'hanno.
#
# ⚠️ E il tipo vero e' `mdata(MDATA_TYPE)`, non `adata(ADATA_TYPE)`: `map.hsp:1387`
# copia il secondo nel primo, ma una manciata di mappe lo riscrive subito dopo
# (`:1407`, `:1443`, `:1854`, ...). Per quelle il tetto qui e' quello sbagliato.
_TIPI_COL_PIANO = {
    'MAP_TYPE_DUNGEON', 'MAP_TYPE_TOWER', 'MAP_TYPE_FOREST', 'MAP_TYPE_FORT',
    'MAP_TYPE_NEST', 'MAP_TYPE_CEMETERY', 'MAP_TYPE_MINE', 'MAP_TYPE_LAKE',
}
_SENZA_PIANO = {'AREA_NT_SOUTH_BORDER', 'AREA_ST_NORTH_BORDER', 'AREA_VALM'}
_AREA_P = re.compile(r'^\s*p\s*=\s*(AREA_\w+|areatestworld)\s*$')
_TIPO_P = re.compile(r'^\s*adata\(\s*ADATA_TYPE\s*,\s*p\s*\)\s*=\s*(\w+)')
_SE_AREA = re.compile(
    r'adata\(\s*ADATA_ID\s*,\s*mapname_mapid\s*\)\s*==\s*(AREA_\w+|areatestworld)')


def tipi_delle_aree(radice):
    """{ AREA_X: MAP_TYPE_Y } dalla tavola delle aree di map.hsp."""
    fuori, corrente = {}, None
    for riga in leggi(os.path.join(radice, 'map.hsp')):
        m = _AREA_P.match(riga)
        if m:
            corrente = m.group(1)
            continue
        if corrente:
            m = _TIPO_P.match(riga)
            if m:
                fuori[corrente] = m.group(1)
                corrente = None
    return fuori


def tetto_di(area, tipi):
    """16, oppure 12 se quella mappa mostra il numero di piano."""
    if not area or area in _SENZA_PIANO:
        return TETTO
    if area in ('AREA_LESIMAS', 'AREA_RANDOM_DUNGEON', 'AREA_QUEST'):
        return TETTO_CON_PIANO
    tipo = tipi.get(area)
    if tipo in _TIPI_COL_PIANO:
        return TETTO_CON_PIANO
    return TETTO


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
    """{ (file, giapponese): (riga, nome, area) } per ogni nome di mappa.

    `area` e' l'`AREA_...` che lo governa, e serve a sapere se quella mappa
    mostra il numero di piano: si conosce solo per i nomi di `mapname`, dove
    l'`if` che li racchiude la nomina. Per gli altri resta None, e il tetto
    va preso come «16, forse 12».
    """
    fuori = {}

    def aggiungi(nomefile, n, coda, area):
        esito = nome_di(coda)
        if not esito:
            return
        chiave, nome = esito
        if not nome.strip():        # `s = "", ""` in cima a mapname
            return
        k = (nomefile, chiave)
        while k in fuori:               # stesso giapponese due volte nel file
            k = (k[0], k[1] + '\x00')
        fuori[k] = (n, nome, area)

    area = None
    for n, riga in blocco_mapname(leggi(os.path.join(radice, 'text.hsp'))):
        m = _SE_AREA.search(riga)
        if m:
            area = m.group(1)
        m = _ASSEGNA_S.match(riga)
        if m:
            aggiungi('text.hsp', n, m.group(1), area)

    for nomefile in sorted(os.listdir(radice)):
        if not nomefile.endswith('.hsp'):
            continue
        for n, riga in enumerate(leggi(os.path.join(radice, nomefile)), 1):
            m = _ASSEGNA_MDATAN.match(riga)
            if m:
                aggiungi(nomefile, n, m.group(1), None)

    return fuori


def referto(etichetta, nomi, tipi):
    troppo = {k: v for k, v in nomi.items()
              if len(v[1]) > tetto_di(v[2], tipi)}
    print(f'--- {etichetta}: {len(nomi)} nomi di mappa')
    print(f'    oltre il proprio tetto (tagliati): {len(troppo)}')
    return troppo


def main(argv):
    tipi = tipi_delle_aree(SORGENTE)
    sorgente = raccogli(SORGENTE)
    build = raccogli(BUILD)

    orfani = [k for k in build if k not in sorgente]
    print('IL NOME DELLA MAPPA NELLA BARRA IN BASSO (screen.hsp:153)')
    print(f'tetto: {TETTO} caratteri, {TETTO_CON_PIANO} se la mappa ha il piano')
    if orfani:
        print(f'⚠️ {len(orfani)} nomi della build senza gemello nel sorgente: '
              f'{orfani[:3]}')
    print()
    referto("l'inglese di monte", sorgente, tipi)
    troppo_it = referto('la build italiana', build, tipi)
    print()

    # Il numero che conta: dove l'inglese di monte ci sta e noi no.
    nostre = []
    for k, (n, it, area) in build.items():
        t = tetto_di(area, tipi)
        en = sorgente.get(k, (0, '', None))[1]
        if en and len(en) <= t < len(it):
            nostre.append((len(it), t, k[0], n, it, en, area))
    print(f'=== DOVE L\'INGLESE CI STA E NOI NO: {len(nostre)} ===')
    print('   (il tetto e\' 16 tranne dove segnato; "?" = area non riconosciuta,')
    print('    cioe\' un nome assegnato fuori da mapname: potrebbe essere 12)')
    print()
    for lit, t, f, n, it, en, area in sorted(nostre, reverse=True):
        segno = f'{t}' if area else f'{t}?'
        print(f'  [{segno:>3}] {lit:3d}  {f}:{n:<6d} {it}')
        print(f'             a schermo "{it[:t]}"   en ({len(en)}): {en}')


if __name__ == '__main__':
    main(sys.argv[1:])
