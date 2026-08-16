# -*- coding: utf-8 -*-
"""I letterali inglesi che non passano da NESSUNA `lang()`.

Il **quinto punto cieco**, trovato col collaudo della 49ª guardando il piede
dell'inventario: `command.hsp:14175` fa `s = "" + listmax + " items"` e
`module.hsp:4141` fa `s = "Page." + (page + 1) + ...`. Nessuna delle due sta
dentro una `lang()`, quindi:

- `estrai.py` non le vede (il perimetro e' definito dalle `lang()`);
- `verifica --dizionario` non le conta fra le «non ancora tradotte»;
- nessun lotto puo' raggiungerle: **si toccano solo con una toppa**.

E si leggono a ogni singola apertura d'inventario.

⚠️ **Non e' `blocchi_en.py` e non e' `else_jp.py`.** Quelli cercano letterali
nudi dentro un ramo di lingua (`if ( en )`, `if ( jp ) … else`), cioe' frasi
che *una* lingua ha e l'altra no. Qui il ramo non c'e' proprio: la riga e'
la stessa per giapponese e inglese, ed e' scritta in inglese per tutti.

⚠️ **E non e' `cnv_str_en.py`.** Li' la chiave inglese e' un *input* che la
resa italiana spegne; qui il letterale e' *uscita*, e si legge a schermo.

Come `blocchi_en.py`, struttura e lingua sono due misure diverse:

- **struttura**: quante righe cosi' fatte ci sono nel **sorgente pinnato**
  (li' non c'e' italiano, quindi ogni letterale con lettere latine e' inglese);
- **da fare**: quelle che nella **build** sono ancora **identiche al sorgente**,
  cioe' che nessuna toppa ha ancora toccato.
"""
import glob
import io
import os
import re
import sys

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'

# Le righe che portano testo sullo schermo: o lo disegnano, o compongono la
# variabile che verra' disegnata.
# ⚠️ `\b` e' a larghezza zero e non si puo' quantificare: il confine va messo
#    solo sui verbi nudi, e `listn(0,` sta come alternativa a se'.
_DISEGNA = re.compile(
    r'^((mes|bmes|txt|txtef|txtmore|noteadd|display_topic|display_note|'
    r'display_window|chatList|chatMore|promptAdd|cs_list)\b|listn\(\s*0\s*,)'
)
_COMPONE = re.compile(
    r'^(s|s\(\d+\)|s\d|buff|buff\(\d+\)|listn\(\s*0\s*,[^)]*\)|valn|strhint\w*|'
    r'locvar_\w*_s\d*|refstr|cardrefskill)\s*(\+?=)\s'
)
# ⚠️ **`listn(0, …)` e `listn(1, …)` non sono la stessa cosa.** La prima e' la
#    colonna che il giocatore legge, la seconda e' la CHIAVE del dato:
#    `db_race.hsp:315` fa `listn(1, listmax) = "kobolt"`, che e' un
#    identificativo di razza e non si traduce. Il censimento del 2026-08-10
#    (`decisioni.md`) le escludeva gia' a mano insieme a `filter_item`,
#    `rffilter_item` e `filter_creature`; qui la distinzione e' nella forma,
#    cosi' non dipende da chi si ricorda di quella pagina.

_LETTERALE = re.compile(r'"([^"]*)"')
# Due lettere di fila almeno una volta: scarta "%", " ", "/", "1", "s" ...
_PAROLA = re.compile(r'[A-Za-z]{2,}')

# Quello che ha lettere latine ma non e' testo per il giocatore.
# ⚠️ Il punto e' OBBLIGATORIO. Scritta `^\.?[a-z]{2,4}$` questa regola si mangia
#    ogni parola corta e minuscola, e la prima a sparire e' stata `" gp"`
#    (`command.hsp:14366`, l'oro dell'alleato), che si legge a schermo.
_ESTENSIONE = re.compile(r'^\.[a-z]{2,4}$|\.(bmp|png|jpg|wav|mid|ogg|txt|hsp|csv|ini|dll|as|ept|eum|pet|pum)\b', re.I)
_PERCORSO = re.compile(r'[\\/]')
# ⚠️⚠️ Ma la barra da sola non fa un percorso, e per una sessione questa regola
#    si e' mangiata una frase: `command.hsp:3095` e' `"@RE   Cats/Dogs Killed: "`,
#    dove la barra sta come congiunzione fra due parole. Trovata solo perche' la
#    50ª stava traducendo il diario riga per riga e quella mancava dall'elenco.
#    ✅ Un percorso e' un TOKEN — non ha spazi dentro: `graphic\book.bmp`,
#    `./user`. Una frase ce li ha. E' la stessa lezione di ` gp` e `Page.` scritta
#    per la terza volta: **un filtro si prova su una riga che si e' vista a
#    schermo**, non solo sul totale.
_SENZA_SPAZI = re.compile(r'^\S+$')
# I nomi passati come stringa e non letti da nessuno: le chiavi di `config.txt`
# (`"netWish."`, `"exAnime."`) e quelle dei file dei PNG (`"meleeElem."`).
# ⚠️ Sono in camelCase, quindi il corpo dev'essere `[A-Za-z]`: con `[a-z]`
#    passavano tutte per testo inglese.
# ⚠️⚠️ Ma l'INIZIALE dev'essere minuscola, o il filtro si mangia `"Page."`, che
#    e' testo vero e si legge in fondo a ogni inventario (`module.hsp:4141`).
#    Le chiavi partono sempre minuscole (`netWish.`, `meleeElem.`, `name.`).
_CHIAVE = re.compile(r'^[a-z_][A-Za-z0-9_]*\.$')
# I marcatori dei file di dialogo (`"%txtAggro"`): tag, non parole.
_TAG = re.compile(r'^%')
# Le funzioni che leggono un dato per chiave: il letterale e' la chiave.
_PER_CHIAVE = re.compile(r'\b(getnpctxt|getpath|cfgRead|getreq|noteget)\s*\(?')
# ⚠️ I codici colore di `noteadd` (`@BL`, `@RE`) sono marcatori, non parole:
#    vanno tolti prima di cercare la parola, o «@BL」+ giapponese» passa per
#    inglese.
_MARCATORE = re.compile(r'@[A-Z]{2}')
# Se il letterale ha un carattere giapponese, la riga sta nel ramo `jp`: e'
# un'altra classe, e la misura `else_jp.py`.
_CJK = re.compile(r'[　-ヿ㐀-鿿＀-￯]')


def _e_testo(letterale: str) -> bool:
    """Vero se il letterale e' testo INGLESE che il giocatore legge."""
    if _CJK.search(letterale):
        return False
    nudo = _MARCATORE.sub('', letterale).strip()
    if not _PAROLA.search(nudo):
        return False
    if _ESTENSIONE.search(nudo):
        return False
    if _PERCORSO.search(nudo) and _SENZA_SPAZI.match(nudo):
        return False
    if _CHIAVE.match(nudo) or _TAG.match(nudo):
        return False
    return True


def righe_nude(righe: list[str]) -> list[int]:
    """Gli indici (0-based) delle righe di uscita con letterali fuori da `lang()`."""
    trovati = []
    for i, riga in enumerate(righe):
        s = riga.strip()
        if not s or s.startswith('//') or s.startswith('#') or s.startswith('/*'):
            continue
        if 'lang(' in s:
            continue
        # `cnv_str` e' un'altra classe: la misura `cnv_str_en.py`.
        if s.startswith('cnv_str'):
            continue
        # Le letture per chiave: il letterale e' la chiave del dato, non testo.
        if _PER_CHIAVE.search(s):
            continue
        if not (_DISEGNA.match(s) or _COMPONE.match(s)):
            continue
        if any(_e_testo(m) for m in _LETTERALE.findall(s)):
            trovati.append(i)
    return trovati


def main(argv: list[str]) -> None:
    nomi = argv or sorted(os.path.basename(p) for p in glob.glob(SORGENTE + r'\*.hsp'))
    tot_struttura = tot_da_fare = 0
    for nome in nomi:
        sorg = io.open(os.path.join(SORGENTE, nome), encoding='cp932').read().split('\n')
        percorso_build = os.path.join(BUILD, nome)
        build = (io.open(percorso_build, encoding='cp932').read().split('\n')
                 if os.path.exists(percorso_build) else sorg)
        indici = righe_nude(sorg)
        if not indici:
            continue
        # ⚠️ Stessa cautela di `blocchi_en.py`: se la build ha piu' righe del
        #    sorgente l'allineamento per indice non vale, e la riga si cerca
        #    per contenuto in tutto il file.
        allineata = len(build) == len(sorg)
        if allineata:
            intatte = [i for i in indici if build[i] == sorg[i]]
        else:
            insieme = set(build)
            intatte = [i for i in indici if sorg[i] in insieme]
        tot_struttura += len(indici)
        tot_da_fare += len(intatte)
        stato = '' if allineata else "  (build piu' lunga: confronto per contenuto)"
        print(f'=== {nome}: {len(indici)} righe, {len(intatte)} ancora intatte{stato}')
        for i in intatte:
            print(f'  {i+1:6d} | {sorg[i].strip()[:120]}')
    print(f'--- struttura: {tot_struttura} righe | ancora da fare: {tot_da_fare}')


if __name__ == '__main__':
    main(sys.argv[1:])
