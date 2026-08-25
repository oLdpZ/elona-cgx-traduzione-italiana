# -*- coding: utf-8 -*-
"""97a - Il censimento del punto cieco della 74a: i menu scritti a mano.

⚠️ Il punto cieco non e' di traduzione, e' di **misura**: 128 righe
`listn(...) = lang(...)` in cinque file, di cui un centinaio gia' rese e **mai
passate sotto un tetto**. `larghezze.py` misura i menu dichiarati
(`s(cnt) = lang(...)` e `promptAdd`), `riquadri.py` le piastrelle,
`menu_dialogo.py` il dialogo: nessuno dei tre guarda una lista riempita a mano.

Questo modulo **raggruppa e misura**. Per ogni riga trova la routine che la
contiene (l'etichetta `*nome` che la precede), la finestra che la disegna
(il `display_window`, che porta la larghezza in px) e il punto dove le righe
della lista si posano (`pos wx + N, ... cnt ...` oppure `cs_list …, wx + N`).
Da li' il tetto in caratteri, col metro di `larghezze.py`: 7,7 px l'uno.

Il referto dice **tre** numeri, come `intestazioni_larghezze`: quante righe
sforano, quante sforavano gia' in inglese, e quante le ha introdotte
l'italiano. **Quello che deve restare a zero e' il terzo.**

⚠️ Le righe di una routine di cui non si trova la geometria si contano a
parte come «senza metro»: meglio non misurate che misurate male.

    python scratchpad/_97-listn.py [file.hsp ...]
"""
import io
import json
import os
import re
import sys

from strumenti.accenti import degrada

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'

FILE = sys.argv[1:] or ['command.hsp', 'chara.hsp', 'chat.hsp',
                        'event.hsp', 'help.hsp', 'net.hsp']

_LISTN = re.compile(r'^\s*listn\s*\([^)]*\)\s*=.*\blang\s*\(')
_ETICHETTA = re.compile(r'^\*(\w+)')
_FINESTRA = re.compile(r'^\s*display_window\s+(.+)$')
# ⚠️ `*com_charainfo` non chiama `display_window`: si scrive la geometria a mano
# (`command.hsp:10263`-`:10266`, `ww = 700`). Senza questa seconda forma la
# scheda del personaggio resta l'unico pannello non misurato del file.
_WW = re.compile(r'^\s*ww\s*=\s*(\d+)\s*$')
# ⚠️⚠️ **L'ancora e' una posizione DENTRO IL CICLO, non una qualunque.**
# Al primo giro bastava `pos wx + N`, e su `*com_charainfo` la prima che
# capitava era `pos wx + 4, wy + 4` (`command.hsp:10305`), che e' dove il
# pannello incolla lo **sfondo**: il tetto usciva 86 invece del vero, e la
# rete diceva verde misurando la cosa sbagliata. Le righe di una lista si
# posano sempre a passo di `cnt`, quindi la `y` deve nominarlo.
_POS = re.compile(r'^\s*pos\s+wx\s*\+\s*(\d+)\s*,.*\bcnt\b')
# e la seconda forma: `cs_list <voce>, wx + N, ...` (`command.hsp:11079`)
_CS_LIST = re.compile(r'^\s*cs_list\s+[^,]+,\s*wx\s*\+\s*(\d+)\s*,')
_PEZZO = re.compile(r'"((?:[^"\\]|\\.)*)"')

PIXEL_PER_CARATTERE = 7.7
MARGINE_DESTRO = 28
LARGHEZZA_NUMERO = 3

# ⚠️ I pannelli a colonne: qui il metro **si legge**, non si deduce, e ogni riga
# di questa tavola porta il sito da cui e' stata letta. Un pannello entra qui
# solo quando qualcuno e' andato a vedere quale `pos` disegna la voce della
# lista — non per far salire il conto delle misurate.
METRO_A_MANO = {
    # `*com_identify_loop` (`command.hsp:16868` e `:16877`): la finestra e' 600 px
    # e le voci si posano a `pos wx + 68, wy + 68 + cnt * 18`. Le altre due
    # ascisse che la rete vede nella routine — wx+15 e wx+40 — sono la barra di
    # scorrimento e il numero di pagina, non il testo. Letto nella 97a.
    ('command.hsp', '*com_identify'): (600, 68),

    # `*com_trait_loop` (`command.hsp:2596`, `:2680`-`:2691`): il pannello dei
    # talenti e' largo 730 px e ha DUE metri, scelti da `list(1, p)`:
    #   list(1, p) <  10000  ->  `pos wx + 30`, `x = 84`, e a `wx + 270` ci va la
    #                            colonna del grado: il nome sta in 186 px;
    #   list(1, p) >= 10000  ->  `pos wx + 45`, `x = 70`, e la colonna del grado
    #                            NON si disegna: la riga ha tutta la finestra.
    # ⭐ Le **settanta** righe `listn(...) = lang(...)` di questa routine stanno
    # tutte nel secondo caso — 41 con `99999` e 29 con `99998`, contate una per
    # una — e infatti non sono nomi di talento ma le frasi informative con la
    # targhetta davanti («[bit] Sei travestito», «[ETC] …», «[AWAKE] …»). I nomi
    # dei talenti veri stanno in `trait.hsp` e non passano di qui. Letto nella 97a.
    ('command.hsp', '*com_trait_loop'): (730, 70),
}


def campi(espressione):
    """Gli argomenti di un `display_window` spezzati sulle virgole di primo livello."""
    fuori, corrente, profondita = [], '', 0
    for c in espressione:
        if c == '(':
            profondita += 1
        elif c == ')':
            profondita -= 1
        if c == ',' and profondita == 0:
            fuori.append(corrente.strip())
            corrente = ''
        else:
            corrente += c
    fuori.append(corrente.strip())
    return fuori


def larghezza(espressione):
    """Il terzo campo di `display_window`, se e' un numero nudo."""
    c = campi(espressione)
    if len(c) < 4:
        return None
    return int(c[2]) if c[2].isdigit() else None


rese = {}
for nome in FILE:
    percorso = os.path.join('dizionario', nome + '.jsonl')
    if not os.path.exists(percorso):
        continue
    for l in io.open(percorso, encoding='utf-8'):
        if not l.strip():
            continue
        v = json.loads(l)
        if v.get('it'):
            rese.setdefault((nome, v['riga']), v)

def reso(it):
    """Il testo che finisce a schermo, dall'`it` del dizionario."""
    if not it.lstrip().startswith('"'):
        return degrada(it)
    pezzi = _PEZZO.findall(it)
    return degrada(''.join(pezzi)) + '#' * (LARGHEZZA_NUMERO * max(0, len(pezzi) - 1))


totale = totale_rese = misurate = senza_metro = gia_fuori = introdotte = 0
for nome in FILE:
    righe = io.open(os.path.join(SORGENTE, nome), encoding='cp932',
                    errors='replace').read().splitlines()

    # per ogni riga: l'etichetta che la precede
    etichetta_di, corrente = {}, '(fuori da ogni etichetta)'
    for n, r in enumerate(righe, 1):
        m = _ETICHETTA.match(r)
        if m:
            corrente = '*' + m.group(1)
        etichetta_di[n] = corrente

    # per ogni etichetta: la finestra e l'inizio del testo, se li dichiara
    finestra_di, inset_di = {}, {}
    for n, r in enumerate(righe, 1):
        m = _FINESTRA.match(r)
        if m and finestra_di.get(etichetta_di[n]) is None:
            finestra_di[etichetta_di[n]] = larghezza(m.group(1))
        m = _WW.match(r)
        if m and finestra_di.get(etichetta_di[n]) is None:
            finestra_di[etichetta_di[n]] = int(m.group(1))
        # ⚠️⚠️ Si raccolgono **tutte** le ascisse del ciclo, non la prima.
        # `*com_charainfo` ne ha quattro (88, 282, 305, 420): e' un pannello a
        # colonne, e prendere la prima che capita da' un tetto inventato che
        # sembra una misura. Quando ce n'e' piu' d'una il metro non si indovina.
        m = _POS.match(r) or _CS_LIST.match(r)
        if m:
            inset_di.setdefault(etichetta_di[n], set()).add(int(m.group(1)))

    # ⚠️ **Chi riempie la lista e chi la disegna quasi mai sono la stessa
    # etichetta**: `*com_identify` riempie `listn(0, p)` e il `display_window` sta
    # in `*com_identify_loop`, venti righe piu' giu'. Al primo giro questo modulo
    # diceva «finestra NON dichiarata» su cinque routine su sette, e la finestra
    # c'era tutte e cinque le volte. La convenzione del sorgente e' meccanica:
    # l'etichetta che disegna porta lo **stesso nome piu' un suffisso**
    # (`_loop`, `_loop_pgchk`, `_WHILE1`), quindi si eredita per prefisso.
    def eredita(mappa, etichetta):
        if mappa.get(etichetta) is not None:
            return mappa[etichetta]
        parenti = sorted((e for e in mappa
                          if e.startswith(etichetta) and mappa[e] is not None),
                         key=len)
        return mappa[parenti[0]] if parenti else None

    def ascisse(etichetta):
        """Tutte le ascisse del ciclo della routine e delle sue etichette figlie."""
        insieme = set()
        for e, valori in inset_di.items():
            if e == etichetta or e.startswith(etichetta):
                insieme |= valori
        return insieme

    trovate = [n for n, r in enumerate(righe, 1) if _LISTN.search(r)]
    if not trovate:
        continue
    per_etichetta = {}
    for n in trovate:
        per_etichetta.setdefault(etichetta_di[n], []).append(n)

    print(f'=== {nome}: {len(trovate)} righe `listn(...) = lang(...)` '
          f'in {len(per_etichetta)} routine')
    for etichetta in sorted(per_etichetta, key=lambda e: per_etichetta[e][0]):
        ns = per_etichetta[etichetta]
        fatte = sum(1 for n in ns if (nome, n) in rese)
        w = eredita(finestra_di, etichetta)
        x = sorted(ascisse(etichetta))
        tetto = None
        if (nome, etichetta) in METRO_A_MANO:
            w, inset = METRO_A_MANO[(nome, etichetta)]
            tetto = int((w - inset - MARGINE_DESTRO) / PIXEL_PER_CARATTERE)
            geometria = f'{w} px, testo a wx+{inset}  ->  tetto {tetto}   (letto a mano)'
        elif w and len(x) == 1:
            tetto = int((w - x[0] - MARGINE_DESTRO) / PIXEL_PER_CARATTERE)
            geometria = f'{w} px, testo a wx+{x[0]}  ->  tetto {tetto}'
        elif w and len(x) > 1:
            geometria = (f'{w} px, ⚠️ {len(x)} colonne (wx+' + ', wx+'.join(map(str, x))
                         + '): il metro si decide a mano')
            senza_metro += len(ns)
        elif w:
            geometria = f'{w} px, inizio del testo NON trovato'
            senza_metro += len(ns)
        else:
            geometria = '⚠️ finestra NON dichiarata in questa routine'
            senza_metro += len(ns)
        print(f'  {etichetta:<28} {len(ns):3d} righe, {fatte:3d} rese   {geometria}')
        totale += len(ns)
        totale_rese += fatte
        if tetto is None:
            continue
        for n in ns:
            v = rese.get((nome, n))
            if v is None:
                continue
            misurate += 1
            testo = reso(v['it'])
            en = v['en'] + '#' * LARGHEZZA_NUMERO * (v['tipo'] == 'dinamica')
            if len(testo) <= tetto:
                continue
            if len(en) > tetto:
                gia_fuori += 1
                nota = "(sfora anche l'inglese)"
            else:
                introdotte += 1
                nota = '⚠️ INTRODOTTO DALL\'ITALIANO'
            print(f'      :{n}  it {len(testo)} / tetto {tetto}  {testo!r}  {nota}')
    print()

print(f'--- {totale} righe in tutto, {totale_rese} gia\' rese')
print(f'--- {misurate} misurate, {senza_metro} senza metro (routine senza geometria)')
print(f'fuori misura: {gia_fuori + introdotte}   di cui gia\' fuori in inglese: {gia_fuori}')
print(f'⚠️ introdotte dall\'italiano: {introdotte}   (atteso: 0)')
