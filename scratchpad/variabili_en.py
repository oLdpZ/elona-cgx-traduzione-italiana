# -*- coding: utf-8 -*-
"""Le variabili che si portano dentro l'inglese, e le `lang()` che le interpolano.

⚠️ **Il terzo punto cieco, dopo `blocchi_en.py` e `else_jp.py`.** Quei due
cercano i letterali inglesi nudi dentro `if ( en ) { ... }` e dentro
`if ( jp ) ... else`. Ma un letterale inglese puo' entrare in una frase per una
terza strada, che nessuno dei due vede: **un assegnamento incondizionato a una
variabile**, che poi una `lang()` interpola nel ramo inglese.

Il caso che l'ha imposta, `proc.hsp` (38ª sessione):

    16976: if ( studybuddy == "" ) { studybuddy = name(tc) }
    16980: else                     { studybuddy = "your friends" }
    16991: txt lang("あなたと仲間たちは読書会を始めた。",
                    "You started a reading party with " + studybuddy + ".")

Non c'e' nessun `if ( en )` e nessun `else` di `jp`: e' codice che gira in tutte
e due le lingue, e il letterale inglese arriva a schermo dentro la frase
tradotta. E' la stessa classe di `his2()` della 36ª e di `bufftxt(1)` della 28ª —
inglese che nessun dizionario raggiunge — ma travestita da variabile.

Il referto stampa, per ogni file:

  - **trappole**: le variabili assegnate a un letterale inglese nudo E
    interpolate dentro una `lang()`. Sono quelle su cui una resa sbaglierebbe.
  - il conteggio delle sole assegnazioni, per tenere le proporzioni.

**Il conto al 2026-08-15 (47ª): 60 variabili si portano dentro un inglese nudo,
e 4 arrivano dentro una `lang()`.** Tutte e quattro lette a mano e vere:

| dove | variabile | che cosa esce a schermo |
|---|---|---|
| `proc.hsp:16991` | `studybuddy` | «Cominci un circolo di lettura con **your friends**» — ✅ evitato nella 38ª rendendo sul giapponese |
| `proc.hsp:19178` | `performerpal` | il **gemello identico**, sull'ensemble: stessa struttura, stessa frase, stesso `"your friends"`. ⚠️ Sta nella zona `19000-19999`, ancora da tradurre: **chi ci arriva renda sul giapponese** |
| `economy.hsp:319` | `s1` | l'allineamento della città — «Neutral», «Law», «Chaos» — che compare in **tutt'e due** i rami di `lang()`: e' inglese anche nella build giapponese |
| ⭐ `command.hsp:7724` | `s` | il **rango** del custom NPC evocato — «Bad », «Common », «Skilled », «Professional », «Legendary », «Well-Known » — composto a pezzi da `:7716`-`:7721`. Trovato nella 47ª, **e solo perche' il referto e' stato corretto**: vedi qui sotto |

⚠️⚠️ **E il referto aveva un punto cieco suo, per nove sessioni.** Fino alla 47ª
`_ASSEGNA` prendeva solo `nome = "testo"`, e **non vedeva `nome += "testo"`**.
Non e' un dettaglio: la forma che accumula e' quella con cui si **compone una
frase inglese a pezzi**, cioe' il caso piu' grosso, non il piu' piccolo — sei
aggettivi in `command.hsp`, ognuno dentro un `if ( ... ) { ... }` su una riga
sola, che il referto non poteva agganciare nemmeno volendo.
💡 E' la stessa lezione di `cnv_str_en.py` nella 45ª, parola per parola: **un
referto che non ha mai trovato niente in una famiglia di file non e' una prova
che quella famiglia sia pulita** — puo' essere che non la guardi. Anche stavolta
il caso e' saltato fuori **leggendo il sorgente**, non rilanciando lo strumento.
✅ Il `+=` ha portato con se' un secondo lavoro: i **nomi di file** che
`system.hsp` compone a pezzi (`"krecipe.s1"`, `"spells.s1"`, `"customval.s1"`)
passavano perche' `.s1` non era nell'elenco delle estensioni scritto a mano.
Adesso c'e' `_ESTENSIONE`, che li prende tutti per forma invece che per nome.
Provato: scarta **56** letterali e sono tutti nomi di file (`.s1`, `.s2`,
`.ept`, `.eum`, `.pet`, `.pum`) o indirizzi web. Nessuna prosa.

⚠️ **Due limiti dichiarati, perche' il numero non e' una garanzia.**

1. Conta solo l'assegnamento **piu' vicino**. Se in un `if` il ramo inglese sta
   piu' lontano di un altro assegnamento, la trappola non si vede. Per
   `studybuddy` e `performerpal` funziona perche' il ramo col letterale e'
   l'`else`, cioe' l'ultimo. ⚠️ Un `+=` non azzera, quindi **non chiude la
   ricerca**: se aggiunge un letterale inglese la trappola c'e', se aggiunge
   altro si continua a guardare piu' su. Solo un `=` chiude la domanda.
2. Prende le forme `nome = "testo"` e `nome += "testo"` su una riga sola, la
   seconda anche dentro un `if ( ... ) { ... }`. Le liste
   (`s = "a", "b", "c"`) sono un'altra famiglia, gia' contata da
   `blocchi_en.py`.

⚠️ Legge il **`SORGENTE` pinnato**, non la build: vedi la nota della 37ª sui
numeri di riga.

    python scratchpad/variabili_en.py [file.hsp ...]
"""
import glob
import io
import os
import re
import sys

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'

# `nome = "testo"` — un assegnamento semplice, non un confronto (`==`, `!=`) e
# non un elemento d'array indicizzato da una stringa. Il letterale deve stare in
# coda: `s = "a", "b", "c"` (le liste di `screen.hsp`) e' un'altra famiglia, gia'
# contata da blocchi_en.py.
_ASSEGNA = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*"([^"]*)"\s*$')

# ⚠️⚠️ **E la forma che ACCUMULA, che questo referto non vedeva fino alla 47ª.**
# `nome += "testo"` non azzera la variabile: ci aggiunge un pezzo. E' la forma
# con cui si compone una frase inglese a pezzi, cioe' il caso piu' grosso, non
# il piu' piccolo: `command.hsp:7716`-`:7721` accumula **sei** aggettivi
# (`"Bad "`, `"Common "`, `"Skilled "`, `"Professional "`, `"Legendary "`,
# `"Well-Known "`) e li porta dentro la `lang()` di `:7724`.
# ⚠️ E ci arriva scritta **dentro un `if ( ... ) { ... }` su una riga sola**,
# quindi il prefisso va ammesso: senza, la riga non si aggancia comunque.
_ACCUMULA = re.compile(
    r'^(?:.*\{\s*)?([A-Za-z_][A-Za-z0-9_]*)\s*\+=\s*"([^"]*)"\s*\}?\s*$')

# Almeno due lettere ASCII e uno spazio o tre lettere di fila: esclude i
# separatori (`" "`, `","`), le sigle e le chiavi di dati di una lettera.
_PAROLA = re.compile(r'[A-Za-z]{3}')

# un nome di file: punto piu' da una a quattro lettere o cifre, in coda
_ESTENSIONE = re.compile(r'\.[A-Za-z0-9]{1,4}$')


def e_inglese(testo: str) -> bool:
    """Un letterale che a schermo si leggerebbe come una parola inglese."""
    if not _PAROLA.search(testo):
        return False
    # i nomi di file, le chiavi e i percorsi non sono testo
    if any(x in testo for x in ('.bmp', '.wav', '.txt', '.ax', '\\', '/', '%')):
        return False
    # ⚠️ **E l'elenco delle estensioni scritto a mano non bastava.** Con la forma
    # `+=` vista dalla 47ª sono comparsi i pezzi di nome di file che `system.hsp`
    # compone a `:2194`-`:2229` — `"krecipe.s1"`, `"spells.s1"`,
    # `"customval.s1"` — che passavano perche' `.s1` non era in elenco. Un
    # letterale che finisce con un punto e da una a quattro lettere o cifre e' un
    # **nome di file**, non una frase: nessuna prosa inglese finisce cosi'.
    if _ESTENSIONE.search(testo):
        return False
    return True


_QUALSIASI_ASSEGNA = re.compile(r'^([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+?)\s*$')
_ETICHETTA = re.compile(r'^\*[A-Za-z_]')
# ⚠️ **In HSP si scrive in una variabile anche senza `=`.** `noteget s, p + 2`
# mette nel `s` la riga letta dal buffer, e la prima stesura di questo referto
# non lo vedeva: cercando all'indietro l'assegnamento di `s` a `main.hsp:4468`
# passava sopra il `noteget` di `:4460` e arrivava fino al `s = "no entry"` di
# `:4449`, denunciando una trappola che non c'e' — quel `s` porta un punteggio,
# non l'inglese. Un comando con la variabile come **primo argomento** conta come
# scrittura e ferma la ricerca.
_COMANDO_SCRIVE = re.compile(r'^[A-Za-z_][A-Za-z0-9_]*\s+([A-Za-z_][A-Za-z0-9_]*)\s*,')
# la variabile interpolata in un'espressione, non dentro il testo di una stringa
_INTERPOLA = r'\+\s*{}\s*(\+|\))'


def _assegnamento_piu_vicino(righe: list[str], var: str, riga: int):
    """(numero di riga, valore) dell'ultimo assegnamento di `var` prima di `riga`.

    ⚠️ **La ricerca si ferma alla `*etichetta` che apre la routine.** Senza
    questo limite la misura e' inutile: `s` e' la variabile di comodo di tutto
    il sorgente, e il primo taglio di questo referto accoppiava un `s = "Have"`
    di `chara_func.hsp:11043` con una `lang()` di `:7724` che sta in un'altra
    routine e parla d'altro. E' la stessa lezione che la rete 8 aveva imparato
    nella 37ª per `valn`: conta **l'assegnamento piu' vicino**, non un
    assegnamento qualsiasi nello stesso file.
    """
    for i in range(riga - 1, 0, -1):
        s = righe[i - 1].strip()
        if _ETICHETTA.match(s):
            return None, None
        if 'lang(' in s:
            continue
        # ⚠️ Un `+=` NON azzera: se aggiunge un letterale inglese la trappola c'e'
        # comunque, e se aggiunge altro la ricerca deve **proseguire** — un `+=`
        # piu' su puo' averci gia' messo l'inglese. Solo un `=` chiude la
        # domanda, ed e' per questo che i due casi non si possono trattare
        # uguale.
        accumula = _ACCUMULA.match(s)
        if accumula and accumula.group(1) == var:
            if e_inglese(accumula.group(2)):
                return i, accumula.group(2)
            continue
        if re.match(rf'^(?:.*\{{\s*)?{re.escape(var)}\s*\+=', s):
            continue
        scrive = _COMANDO_SCRIVE.match(s)
        if scrive and scrive.group(1) == var:
            return i, None
        trovato = _QUALSIASI_ASSEGNA.match(s)
        if trovato and trovato.group(1) == var:
            return i, trovato.group(2)
    return None, None


def analizza(righe: list[str]) -> tuple[dict, dict]:
    """(assegnamenti, trappole).

    `assegnamenti`: variabile -> righe dove prende un letterale inglese nudo.
    `trappole`: variabile -> [(riga della lang(), riga dell'assegnamento)], per
    le sole `lang()` il cui assegnamento **piu' vicino** e' uno di quelli.
    """
    assegnamenti: dict[str, list[int]] = {}
    for i, riga in enumerate(righe):
        s = riga.strip()
        if 'lang(' in s:
            continue
        trovato = _ASSEGNA.match(s) or _ACCUMULA.match(s)
        if trovato and e_inglese(trovato.group(2)):
            assegnamenti.setdefault(trovato.group(1), []).append(i + 1)

    trappole: dict[str, list[tuple[int, int]]] = {}
    for i, riga in enumerate(righe):
        if 'lang(' not in riga:
            continue
        for nome in assegnamenti:
            if not re.search(_INTERPOLA.format(re.escape(nome)), riga):
                continue
            dove, _ = _assegnamento_piu_vicino(righe, nome, i + 1)
            if dove in assegnamenti[nome]:
                trappole.setdefault(nome, []).append((i + 1, dove))
    return assegnamenti, trappole


def main(argv: list[str]) -> None:
    nomi = argv or sorted(os.path.basename(p) for p in glob.glob(SORGENTE + r'\*.hsp'))
    tot_var = tot_trappole = tot_siti = 0
    for nome in nomi:
        righe = io.open(os.path.join(SORGENTE, nome), encoding='cp932').read().split('\n')
        assegnamenti, trappole = analizza(righe)
        if not assegnamenti:
            continue
        tot_var += len(assegnamenti)
        if not trappole:
            continue
        tot_trappole += len(trappole)
        print(f'=== {nome}: {len(assegnamenti)} variabili con un inglese nudo, '
              f'⚠️ {len(trappole)} arrivano dentro una lang()')
        for var, siti in sorted(trappole.items()):
            tot_siti += len(siti)
            print(f'  ⚠️ {var}')
            for sito, dove in siti:
                print(f'       {dove:6d} | {righe[dove - 1].strip()[:110]}')
                print(f'       {sito:6d} > {righe[sito - 1].strip()[:110]}')
    print(f'--- variabili con un inglese nudo: {tot_var} | '
          f'⚠️ trappole (interpolate in una lang()): {tot_trappole} in {tot_siti} siti')


if __name__ == '__main__':
    main(sys.argv[1:])
