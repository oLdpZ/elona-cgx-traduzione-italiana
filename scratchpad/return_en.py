# -*- coding: utf-8 -*-
"""Il debito della 50a: i `return "…"` dentro un `#defcfunc`, che nessuno vede.

`nudi_en.py` cerca le righe che **disegnano** (`mes`, `bmes`, `txt`, `noteadd`…)
e quelle che **compongono** una variabile che verra' disegnata (`s = `,
`listn(0, …) = `, `buff += `). Un `return "…"` dentro un `#defcfunc` non e' ne'
l'una ne' l'altra, e il testo che restituisce finisce a schermo lo stesso — e'
cosi' che il suffisso di stato del pannello dei ritocchi (« (Currently: Off)»)
e' rimasto invisibile fino alla 50a.

    python scratchpad/return_en.py            # solo quel che resta da fare
    python scratchpad/return_en.py --tutte    # anche le classi gia' chiuse

## ⚠️ Perche' la regola NON poteva essere sulla forma del letterale

La 50a aveva lasciato il debito scrivendo: «serve una regola di forma che
distingua». Provata, **non esiste**:

    text.hsp   `return "vernis"`   chiave di mappa      NON e' testo
    init.hsp   `return "st"`       suffisso ordinale    E' testo

Tutt'e due sono un token minuscolo, senza spazi, senza punteggiatura. Nessuna
regola che guardi **il letterale** puo' separarli, e inventarne una avrebbe
ripetuto per la quinta volta l'errore di `_PERCORSO`: un filtro che sembra
giusto sul totale e sbaglia sulla riga vera.

## ✅ La regola vera: si guarda dove va a finire il valore

Un `#defcfunc` non e' un letterale, e' una **funzione**: quel che conta non e'
come e' fatto quel che restituisce, ma **chi lo chiama e che cosa ci fa**. Se
anche una sola chiamata sta su una riga che disegna o che compone (le stesse due
famiglie di `nudi_en.py`), allora quel che la funzione restituisce arriva a
schermo. E' la stessa regola per cui la 50a ha deciso «Bandits Killed»
guardando chi assegna il campo, e per cui `triage_nudi` guarda il prefisso
`dbg_` invece del nome: **si guarda il sito, non la parola**.

## Le quattro classi

**chiave** — nessuna chiamata disegna o compone: il valore e' un identificativo.
Ci finisce `text.hsp:2615 mapfile` (35 `return`: «vernis», «kapul»,
«fighterguild»), che e' esattamente il caso che la 50a aveva indicato a mano.

**morfologia** — la funzione e' nell'elenco che `strumenti/funzioni.py` gia'
tiene: `MORFOLOGIA_INGLESE` (`_s`, `is`, `was`, `have`, `does`, `its`,
`yourself`…) e i `PRONOMI_PER_SITO` (`he`, `his`, `him`) chiamati **senza** il
secondo argomento. Sono la grammatica inglese, e la resa italiana **li toglie
dal sito** invece di tradurli: i loro `return` non sono lavoro, sono la cosa che
la traduzione fa sparire. ⚠️ Sono **44 `return` su 121**, cioe' piu' di un
terzo del totale che la 50a aveva contato.

**toccata** — la classe piu' importante e quella che mancava. La funzione arriva
a schermo, **ma dentro il suo blocco build e sorgente gia' differiscono**:
qualcuno ci ha lavorato. Contarla fra le cose da fare sarebbe un falso
positivo, e non guardarla sarebbe peggio.

**testo** — quel che resta: arriva a schermo e nessuno l'ha toccata.

## ⚠️⚠️ Il caso che la 50a indicava era gia' chiuso

La 50a scriveva: «il caso su cui provarla e' `init.hsp:155`-`:168`: i suffissi
ordinali `"st"`/`"nd"`/`"rd"`/`"th"`». **Erano gia' risolti**, da
`scratchpad/toppa-init-cnvrank.py`: la toppa fa diventare `if ( jp )` un
`if ( jp | en )`, cosi' il ramo italiano restituisce il numero nudo e quei
quattro `return` non li raggiunge piu' nessuno. Le quattro righe stanno ancora
li' nella build, identiche al sorgente, e **un conteggio ingenuo le chiamerebbe
«da fare» per sempre**. Le trova la classe `toccata`.

💡 E' la stessa lezione della 50a al contrario: li' un rinvio dipendeva da un
fatto e ha aspettato in ordine; qui un debito dipendeva da un ricordo, e il
ricordo era vecchio di una sessione. **Prima di contare, si guarda la build.**
"""
import glob
import importlib.util
import io
import os
import re
import sys

_QUI = os.path.dirname(os.path.abspath(__file__))
_RADICE = os.path.dirname(_QUI)
if _RADICE not in sys.path:
    sys.path.insert(0, _RADICE)

_spec = importlib.util.spec_from_file_location('nudi_en', os.path.join(_QUI, 'nudi_en.py'))
nudi = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(nudi)

from strumenti.funzioni import MORFOLOGIA_INGLESE, PRONOMI_PER_SITO  # noqa: E402

SORGENTE = nudi.SORGENTE
BUILD = nudi.BUILD

# ⚠️ Le due righe che arrivano a schermo e che si LASCIANO, col motivo scritto.
#    Non e' una lista di comodo: senza, il referto le riproporrebbe a ogni
#    sessione e chi legge dovrebbe rifare la stessa indagine da capo.
DECISE = {
    ('init.hsp', 171): (
        "`cnvtalk` mette il parlato fra virgolette dritte, e in italiano ci resta. "
        "Misurato: «» NON stanno in CP932, e le uniche virgolette alte che ci stanno "
        "(“”, 0x81 0x67) sono a DOPPIA larghezza, che `scratchpad/guardie.py` "
        "vieta — la stessa regola per cui l'ordinale «5°» non si puo' scrivere "
        "(vedi `toppa-init-cnvrank.py`). Le virgolette dritte sono l'unica forma "
        "scrivibile e sono italiano corretto: non e' un ripiego, e' l'unica strada."
    ),
    ('init.hsp', 1875): (
        "`his2` restituisce «your» per il giocatore e `name()` per chiunque altro, "
        "quindi NON e' morfologia: `strumenti/funzioni.py` lo tratta da contenuto, e ha "
        "ragione. ⭐ La forma della soluzione c'e' gia': `proc.hsp:11481` e' stato "
        "chiuso con una toppa che toglie `his2(tc) + your2(tc)` e mette `name(tc)`, "
        "cioe' nomina il personaggio invece di dire «il suo». ⚠️ Restano due siti, "
        "`item.hsp:4291` e `:4294`, e `item.hsp` non e' ancora nel perimetro: sono "
        "righe `lang()`, quindi lavoro da dizionario, non da toppa. **Si sblocca il "
        "giorno in cui `item.hsp` entra nel perimetro**, e allora seguira' la forma di "
        "proc.hsp:11481. Il quarto sito, `mock.hsp:29`, e' una schermata di prova."
    ),
}

_LETTERALE = re.compile(r'"([^"]*)"')
_DEFCFUNC = re.compile(r'^#(?:defcfunc|deffunc)\s+(?:local\s+)?(\w+)')
# Un blocco di funzione finisce dove ne comincia un altro, o a un'etichetta.
_FINE_BLOCCO = re.compile(r'^(?:#(?:def|module|global|const|enum|uselib|func|cfunc)|\*\w)')


def _blocchi(righe: list[str]) -> list[tuple[str, int, int]]:
    """(nome, inizio, fine) di ogni `#defcfunc`/`#deffunc`, indici 0-based.

    ⚠️ Un blocco si chiude **anche** quando ne comincia un altro, non solo a
    un'etichetta. Alla prima scrittura questo caso mancava e ogni funzione di
    `init.hsp` risultava contenere tutti i 57 `return` del file: se n'e' accorto
    il referto, che dava lo stesso elenco a `netload` e a `xy2pic`.
    """
    fuori = []
    corrente = None
    for i, riga in enumerate(righe):
        s = riga.strip()
        m = _DEFCFUNC.match(s)
        if (m or _FINE_BLOCCO.match(s)) and corrente is not None:
            fuori.append((corrente[0], corrente[1], i))
            corrente = None
        if m:
            corrente = (m.group(1), i)
    if corrente is not None:
        fuori.append((corrente[0], corrente[1], len(righe)))
    return fuori


def _rese(righe: list[str], inizio: int, fine: int) -> list[tuple[int, str]]:
    """I `return` con testo inglese nudo dentro il blocco."""
    return [(i, righe[i].strip()) for i in range(inizio, fine)
            if righe[i].strip().startswith('return')
            and 'lang(' not in righe[i]
            and any(nudi._e_testo(x) for x in _LETTERALE.findall(righe[i]))]


def _carica(cartella: str) -> dict:
    return {os.path.basename(p): io.open(p, encoding='cp932').read().split('\n')
            for p in sorted(glob.glob(cartella + r'\*.hsp'))}


def _siti(sorgenti: dict, fun: str, definita_in: str, dentro: tuple[int, int]) -> list:
    """(file, riga1, classe, testo, argomenti) di ogni chiamata alla funzione."""
    chiamata = re.compile(r'\b' + re.escape(fun) + r'\s*\(')
    fuori = []
    for nome, righe in sorgenti.items():
        for i, riga in enumerate(righe):
            if nome == definita_in and dentro[0] <= i < dentro[1]:
                continue                       # il corpo della funzione stessa
            s = riga.strip()
            if s.startswith(('#', '//', ';')):
                continue
            m = chiamata.search(s)
            if not m:
                continue
            classe = ('disegna' if nudi._DISEGNA.match(s)
                      else 'compone' if nudi._COMPONE.match(s) else 'altro')
            # quanti argomenti: serve solo ai PRONOMI_PER_SITO
            resto = s[m.end() - 1:]
            livello, virgole = 0, 0
            for c in resto:
                if c == '(':
                    livello += 1
                elif c == ')':
                    livello -= 1
                    if livello == 0:
                        break
                elif c == ',' and livello == 1:
                    virgole += 1
            fuori.append((nome, i + 1, classe, s, virgole + 1))
    return fuori


def _inizio_in_build(b: list[str], fun: str) -> int | None:
    """Dove comincia lo stesso `#defcfunc` nella build, o None se non c'e'."""
    for i, riga in enumerate(b):
        m = _DEFCFUNC.match(riga.strip())
        if m and m.group(1) == fun:
            return i
    return None


def _riga_build(b: list[str], b_inizio: int, scarto: int) -> str | None:
    i = b_inizio + scarto
    return b[i] if 0 <= i < len(b) else None


def _classe(fun: str, siti: list) -> str:
    if fun in MORFOLOGIA_INGLESE:
        return 'morfologia'
    if fun in PRONOMI_PER_SITO:
        # ⚠️⚠️ `he`, `his` e `him` hanno DUE rami, e solo il primo e' contenuto.
        #    `init.hsp:1819`-`:1852` (build): dentro `if ( he_arg2 )` ogni
        #    `return` passa da `lang()` ed e' gia' reso — «lui», «lei», «il tuo»,
        #    «il suo»; sotto, il ramo a un argomento solo restituisce l'inglese
        #    nudo — «it», «you», «he», «she». E' esattamente la distinzione che
        #    `strumenti/funzioni.py` gia' descrive («con un secondo argomento
        #    passano da lang(), senza restano per sempre inglese nudo»).
        #    ✅ `_rese` scarta le righe con `lang(`, quindi quel che arriva qui
        #    e' **per costruzione** il solo ramo nudo: morfologia, sempre. La
        #    prima scrittura guardava invece se ESISTESSE un sito a due
        #    argomenti, e chiamava «da fare» 15 `return` che la resa italiana
        #    toglie dal sito.
        return 'morfologia'
    if not any(s[2] in ('disegna', 'compone') for s in siti):
        return 'chiave'
    return 'testo'


def main(argv: list[str]) -> None:
    tutte = '--tutte' in argv
    sorgenti = _carica(SORGENTE)
    build = _carica(BUILD)

    conta = {'testo': 0, 'decisa': 0, 'toccata': 0, 'morfologia': 0, 'chiave': 0}
    residuo = 0
    for nome, righe in sorgenti.items():
        b = build.get(nome, righe)
        for fun, inizio, fine in _blocchi(righe):
            rese = _rese(righe, inizio, fine)
            if not rese:
                continue
            siti = _siti(sorgenti, fun, nome, (inizio, fine))
            classe = _classe(fun, siti)
            # ⚠️ Il blocco della build NON sta agli stessi indici: `init.hsp` ha
            #    12 righe in piu' dopo l'applicazione. Si ritrova per nome e si
            #    confronta a partire dall'intestazione — che e' l'unico
            #    allineamento che regge. Alla prima scrittura il confronto era
            #    per indice e dava «0 intatti» su tutto, cioe' tutto gia' fatto.
            b_inizio = _inizio_in_build(b, fun)
            intatti = [(i, s) for i, s in rese
                       if b_inizio is None or _riga_build(b, b_inizio, i - inizio) == righe[i]]
            # ⚠️ «Toccata» si decide su TUTTO il blocco, non sui soli `return`:
            #    la toppa di `cnvrank` non tocca nessun `return`, cambia la
            #    guardia (`if ( jp )` -> `if ( jp | en )`) e cosi' spegne il ramo
            #    che li contiene. Guardando i soli `return` quei quattro
            #    risulterebbero da fare per sempre.
            if classe == 'testo' and b_inizio is not None and any(
                    _riga_build(b, b_inizio, i - inizio) != righe[i]
                    for i in range(inizio, fine)):
                classe = 'toccata'
            # ⚠️ Le decisioni si applicano PRIMA di contare: una riga decisa non
            #    e' lavoro, e lasciarla fra le «da fare» costringe la sessione
            #    dopo a rifare l'indagine che questa ha gia' fatto.
            decise = [(i, s) for i, s in rese if (nome, i + 1) in DECISE]
            if classe == 'testo' and len(decise) == len(rese):
                classe = 'decisa'
            conta[classe] += len(rese)
            if classe == 'toccata':
                residuo += len(intatti)
            if classe == 'decisa':
                print(f'=== [DECISA    ] {nome}:{inizio + 1} {fun} — {len(rese)} return')
                for i, s in rese:
                    print(f'  {i + 1:7d} | {s[:110]}')
                    print(f'          ↳ {DECISE[(nome, i + 1)][:300]}')
                continue
            if classe in ('morfologia', 'chiave') and not tutte:
                continue
            if classe == 'toccata' and not intatti and not tutte:
                print(f'=== [CHIUSA    ] {nome}:{inizio + 1} {fun} '
                      f'— {len(rese)} return, tutti gia\' resi')
                continue

            a_schermo = [s for s in siti if s[2] in ('disegna', 'compone')]
            print(f'=== [{classe.upper():10}] {nome}:{inizio + 1} {fun} '
                  f'— {len(rese)} return, {len(siti)} chiamate '
                  f'({len(a_schermo)} a schermo)')
            for f, r, c, s, _ in (a_schermo or siti)[:2]:
                print(f'    ↳ {c} in {f}:{r}  {s[:92]}')
            for i, s in (rese if classe != 'toccata' else intatti):
                print(f'  {i + 1:7d} | {s[:110]}')
    print('--- da fare   :', conta['testo'], 'return in funzioni che arrivano a schermo')
    print('--- decise    :', conta['decisa'], 'return che arrivano a schermo e si lasciano, col motivo')
    print('--- toccate   :', conta['toccata'], "return in funzioni gia' lavorate,",
          residuo, 'ancora identici al sorgente')
    print('--- morfologia:', conta['morfologia'], 'return che la resa italiana toglie dal sito')
    print('--- chiavi    :', conta['chiave'], 'return che nessuno disegna')
    print('--- totale    :', sum(conta.values()))


if __name__ == '__main__':
    main(sys.argv[1:])
