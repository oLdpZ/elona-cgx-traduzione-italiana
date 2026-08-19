# -*- coding: utf-8 -*-
"""Il vocabolario italiano degli epiteti, e i due CSV che ne escono.

Il pezzo 1 del piano di `decisioni.md`, cominciato dalle **categorie concrete**
— armi, colori, pietre, elementi, tempo, animali, corpo, azioni — che sono 127
righe delle 365 e sono quelle che fanno gli epiteti piu' riconoscibili.

⭐ **Un vocabolario parziale non da' epiteti misti**: `random_title` salta le
celle vuote (`if rnlist(...) == "" -> continue`), quindi le righe non ancora
tradotte semplicemente non escono mai. Il gioco parla italiano da subito, con
meno varieta'.

## Le due forme, e perche'

    ndata-i.csv    forma NUDA, usata come testa       «lupo»
    ndata-i2.csv   forma PREPOSIZIONALE, modificatore «del lupo»

La toppa a `etc.hsp` ([[epiteti_toppe]]) monta sempre `testa + " " +
modificatore`, e siccome il modificatore porta dentro di se' la preposizione
**non c'e' nessun accordo di genere da fare**: e' la mossa che evita i «Fata
corrotto».

## La regola delle preposizioni

⭐ **Materiali ed elementi prendono «di» senza articolo** — «Spada di rame»,
«Lupo di fuoco», «Lama di ghiaccio» — perche' in italiano il materiale non si
determina. **Tutto il resto prende la preposizione articolata**: «del re»,
«della notte», «dell'alba». La differenza si sente: «Cavaliere del rame» suona
sbagliato dove «Cavaliere di rame» suona giusto.

⚠️ **I colori non funzionano come preposizionali diretti.** «Lupo del rosso» non
si puo' leggere: i colori diventano sostantivi di materia o di qualita' —
`red` → «scarlatto» (di scarlatto), `gold` → «oro» (d'oro), `white` →
«candore» (del candore). E' l'unico punto dove la resa si allontana dalla parola
inglese, e lo fa per restare leggibile.

⚠️ Gli accenti veri si scrivono qui e si degradano alla scrittura del CSV, come
fa `applica` col dizionario: il gioco legge CP932, che gli accenti non li ha.
"""
import csv
import io
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from strumenti.accenti import degrada

MONTE = Path(r"C:\Games\Elona\elonaplus2.31\data\ndata-e.csv")
USCITA = Path(r"C:\Games\Elona\elonaplus2.31\data")

# indice di riga -> ((nuda, preposizionale) per la colonna 0, idem per la 1)
# None dove la cella di monte e' vuota o non si traduce.
VOC = {
    # --- 王, la regalita' ------------------------------------------------
    0: (("principe", "del principe"), ("duca", "del duca")),
    1: (("regina", "della regina"), ("sovrano", "del sovrano")),
    2: (("principessa", "della principessa"), ("duchessa", "della duchessa")),
    3: (("regno", "del regno"), ("nazione", "della nazione")),
    4: (("impero", "dell'impero"), None),
    # --- 具, le armi ----------------------------------------------------
    5: (("spada", "della spada"), ("claymore", "della claymore")),
    6: (("ascia", "dell'ascia"), ("alabarda", "dell'alabarda")),
    7: (("lancia", "della lancia"), ("tridente", "del tridente")),
    8: (("arco", "dell'arco"), ("arco lungo", "dell'arco lungo")),
    9: (("freccia", "della freccia"), None),
    10: (("martello", "del martello"), ("mazza", "della mazza")),
    11: (("pugnale", "del pugnale"), ("stocco", "dello stocco")),
    12: (("scudo", "dello scudo"), ("riparo", "del riparo")),
    13: (("fucile", "del fucile"), ("proiettile", "del proiettile")),
    14: (("filo", "del filo"), ("lama", "della lama")),
    # --- 時, il tempo ---------------------------------------------------
    54: (("eternità", "dell'eternità"), ("immortalità", "dell'immortalità")),
    55: (("ora", "dell'ora"), ("tempo", "del tempo")),
    56: (("passato", "del passato"), ("antichità", "dell'antichità")),
    57: (("futuro", "del futuro"), ("avvenire", "dell'avvenire")),
    58: (("ieri", "di ieri"), ("domani", "di domani")),
    59: (("aldilà", "dell'aldilà"), ("karma", "del karma")),
    60: (("crepuscolo", "del crepuscolo"), ("sera", "della sera")),
    61: (("mattino", "del mattino"), ("alba", "dell'alba")),
    62: (("notte", "della notte"), ("aurora", "dell'aurora")),
    63: (("mezzogiorno", "del mezzogiorno"), ("giorno", "del giorno")),
    64: (("mezzanotte", "della mezzanotte"), None),
    # --- 獣 -------------------------------------------------------------
    65: (("pecora", "della pecora"), ("ariete", "dell'ariete")),
    66: (("toro", "del toro"), ("toro da lotta", "del toro da lotta")),
    # --- 情, i sentimenti -----------------------------------------------
    67: (("amore", "dell'amore"), ("affetto", "dell'affetto")),
    68: (("passione", "della passione"), None),
    69: (("amicizia", "dell'amicizia"), ("fiducia", "della fiducia")),
    70: (("coraggio", "del coraggio"), ("ardimento", "dell'ardimento")),
    # --- 色, i colori: sostantivi di materia o di qualita' ---------------
    71: (("scarlatto", "di scarlatto"), ("rosa", "di rosa")),
    72: (("azzurro", "d'azzurro"), None),
    73: (("candore", "del candore"), ("neve", "di neve")),
    74: (("ambra", "d'ambra"), None),
    75: (("porpora", "di porpora"), None),
    76: (("nero", "del nero"), None),
    77: (("oro", "d'oro"), ("denaro", "del denaro")),
    78: (("argento", "d'argento"), None),
    79: (("raggio", "del raggio"), ("luce", "della luce")),
    80: (("oscurità", "dell'oscurità"), ("buio", "del buio")),
    81: (("arcobaleno", "dell'arcobaleno"), None),
    # --- 神 -------------------------------------------------------------
    82: (("dio", "del dio"), ("dea", "della dea")),
    83: (("pontefice", "del pontefice"), None),
    84: (("re", "del re"), ("monarca", "del monarca")),
    # --- 世界 -----------------------------------------------------------
    194: (("Ade", "dell'Ade"), ("oltretomba", "dell'oltretomba")),
    # --- 星, il cielo ---------------------------------------------------
    195: (("cometa", "della cometa"), None),
    196: (("luna", "della luna"), ("plenilunio", "del plenilunio")),
    197: (("sole", "del sole"), ("splendore", "dello splendore")),
    198: (("stella", "della stella"), ("astro", "dell'astro")),
    # --- 石, pietre e metalli: «di» senza articolo -----------------------
    199: (("pietra", "di pietra"), None),
    200: (("diamante", "di diamante"), None),
    201: (("zaffiro", "di zaffiro"), None),
    202: (("rubino", "di rubino"), None),
    203: (("perla", "di perla"), None),
    204: (("acciaio", "d'acciaio"), ("ferro", "di ferro")),
    205: (("rame", "di rame"), ("bronzo", "di bronzo")),
    206: (("platino", "di platino"), None),
    207: (("cristallo", "di cristallo"), None),
    # --- 属, gli elementi: «di» senza articolo ---------------------------
    208: (("ghiaccio", "di ghiaccio"), ("gelo", "di gelo")),
    209: (("acqua", "d'acqua"), None),
    210: (("fuoco", "di fuoco"), ("vampa", "di vampa")),
    211: (("terra", "di terra"), None),
    212: (("tuono", "di tuono"), ("fulmine", "di fulmine")),
    213: (("fiamma", "di fiamma"), None),
    214: (("sabbia", "di sabbia"), ("rena", "di rena")),
    215: (("cielo", "di cielo"), None),
    216: (("aria", "d'aria"), ("paradiso", "del paradiso")),
    # --- 属性, gli attributi ---------------------------------------------
    217: (("divinità", "della divinità"), None),
    218: (("benedizione", "della benedizione"), None),
    219: (("comando", "del comando"), None),
    220: (("maledizione", "della maledizione"), None),
    221: (("caos", "del caos"), None),
    222: (("ordine", "dell'ordine"), ("sistema", "del sistema")),
    223: (("equilibrio", "dell'equilibrio"), None),
    224: (("neutralità", "della neutralità"), None),
    225: (("ombra", "dell'ombra"), ("penombra", "della penombra")),
    226: (("nube", "della nube"), None),
    # --- 族 -------------------------------------------------------------
    227: (("spirito", "dello spirito"), None),
    228: (("fata", "della fata"), None),
    229: (("neve", "di neve"), ("nevicata", "della nevicata")),
    230: (("famiglia", "della famiglia"), ("clan", "del clan")),
    # --- 体, il corpo ---------------------------------------------------
    231: (("dito", "del dito"), ("pollice", "del pollice")),
    232: (("braccio", "del braccio"), None),
    233: (("piede", "del piede"), ("gamba", "della gamba")),
    234: (("cervello", "del cervello"), None),
    235: (("occhio", "dell'occhio"), ("occhi", "degli occhi")),
    # --- 動, le azioni --------------------------------------------------
    236: (("danza", "della danza"), None),
    237: (("sorriso", "del sorriso"), None),
    238: (("volo", "del volo"), None),
    239: (("salto", "del salto"), ("balzo", "del balzo")),
    240: (("stasi", "della stasi"), None),
    241: (("grido", "del grido"), ("urlo", "dell'urlo")),
    242: (("voce", "della voce"), None),
    243: (("distruzione", "della distruzione"), ("demolizione", "della demolizione")),
    244: (("sfacelo", "dello sfacelo"), ("caduta", "della caduta")),
    245: (("lamento", "del lamento"), ("gemito", "del gemito")),
    246: (("sfida", "della sfida"), ("rivolta", "della rivolta")),
    247: (("cimento", "del cimento"), None),
    248: (("ascesa", "dell'ascesa"), None),
    249: (("rinascita", "della rinascita"), ("risveglio", "del risveglio")),
    250: (("domatore", "del domatore"), ("addestratore", "dell'addestratore")),
    251: (("armonia", "dell'armonia"), None),
    252: (("suono", "del suono"), ("fragore", "del fragore")),
    253: (("risonanza", "della risonanza"), ("consonanza", "della consonanza")),
    254: (("controllo", "del controllo"), ("dominio", "del dominio")),
    # --- 動物, gli animali ----------------------------------------------
    255: (("leopardo", "del leopardo"), ("pantera", "della pantera")),
    256: (("falco", "del falco"), None),
    257: (("scorpione", "dello scorpione"), None),
    258: (("serpe", "della serpe"), ("serpente", "del serpente")),
    259: (("volpe", "della volpe"), None),
    # --- 普 -------------------------------------------------------------
    260: (("raccolto", "del raccolto"), ("mietitore", "del mietitore")),
    261: (("orizzonte", "dell'orizzonte"), None),
    262: (("scossa", "della scossa"), ("terremoto", "del terremoto")),
    263: (("virtù", "della virtù"), ("rettitudine", "della rettitudine")),
    264: (("meraviglia", "della meraviglia"), ("mistero", "del mistero")),
    265: (("distacco", "del distacco"), ("solitudine", "della solitudine")),
    266: (("legge", "della legge"), ("regola", "della regola")),
    # --- 物, le cose ----------------------------------------------------
    267: (("carro", "del carro"), None),
    268: (("droga", "della droga"), ("filtro", "del filtro")),
    269: (("chiave", "della chiave"), ("serratura", "della serratura")),
    270: (("corpo", "del corpo"), ("carne", "della carne")),
    271: (("mente", "della mente"), ("anima", "dell'anima")),
    272: (("osso", "dell'osso"), ("torre", "della torre")),
    273: (("torre", "della torre"), ("pagoda", "della pagoda")),
    274: (("fortezza", "della fortezza"), ("forte", "del forte")),
}


def griglia_di_monte():
    with io.open(MONTE, encoding="cp932", errors="replace", newline="") as f:
        return [r for r in csv.reader(f)]


def costruisci():
    monte = griglia_di_monte()
    nude, prep = [], []
    for n, riga in enumerate(monte):
        categoria = riga[14] if len(riga) > 14 else ""
        celle_n = [""] * 14
        celle_p = [""] * 14
        voce = VOC.get(n)
        if voce:
            for colonna, coppia in enumerate(voce):
                if coppia:
                    celle_n[colonna] = degrada(coppia[0])
                    celle_p[colonna] = degrada(coppia[1])
        nude.append(celle_n + [categoria])
        prep.append(celle_p + [categoria])
    return nude, prep


def scrivi(righe, nome):
    testo = "".join(",".join(r) + "\n" for r in righe)
    percorso = USCITA / nome
    io.open(percorso, "w", encoding="cp932", errors="strict", newline="").write(testo)
    return percorso


def main():
    nude, prep = costruisci()
    piene = sum(1 for r in nude if any(c for c in r[:14]))
    parole = sum(1 for r in nude for c in r[:14] if c)
    for righe, nome in ((nude, "ndata-i.csv"), (prep, "ndata-i2.csv")):
        p = scrivi(righe, nome)
        print(f"scritto {p}  ({len(righe)} righe)")
    print(f"righe tradotte: {piene} su {len(nude)}  |  parole: {parole}")


if __name__ == "__main__":
    main()
