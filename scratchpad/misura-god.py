# -*- coding: utf-8 -*-
"""Il pannello degli dei: quante righe scrive `gmes`, e dove finisce.

`god.hsp:448`-`:454` disegna la scheda di ogni dio con `gmes`, che **non e' un
`mes`**: e' il compositore di `module.hsp:4918`-`:5018`, che va a capo da solo e
interpreta i marcatori `<br>` e `<p>`. Nessuna delle reti di geometria lo
guarda: `larghezze` misura i menu di `*prompt_key`, `riquadri` le piastrelle
dell'HUD, `menu_dialogo` le voci di `chatList`, `linguette` le schede, e
`misura-config` le due colonne del pannello delle opzioni.

## Le regole, lette dal compositore

    locvar_gmes_size = 14                              module.hsp:4924
    gmesx += HIGHDPI_Y(size) / 2 * p                   :5014   -> 7 px per lettera
    if gmesx >= gmesx + gmesw: gmesy += size + 2       :5001   -> 16 px, e va a capo
    <br>  gmesy += 16                                  :4979
    <p>   gmesy += 24                                  :4975
    fine  gmesy += size + 4 = 18                       :5017

⚠️ **`gmes` ignora il `font` che il chiamante ha appena impostato**: `god.hsp:419`
chiede corpo 13, e `gmes` lo riscrive a 14 alla prima riga del corpo. Il passo e'
7, non 6.

⚠️ **Va a capo a META' PAROLA.** Il controllo e' su `gmesx >= lim`, carattere per
carattere: non c'e' nessuna nozione di parola. I `<br>` di upstream stanno li'
apposta, e una resa che li sposta o li perde spezza una parola a caso.

## Il perimetro verticale

    wy + 70                     dove comincia il corpo      god.hsp:449
    wy + dy - listmax*20 - 18   dove comincia il menu       god.hsp:462
    dy = 270, listmax = 2       -> il menu sta a wy + 212

Cioe' **142 px**, e upstream li usa tutti: la scheda di Mani finisce a 198.
Una riga in piu' sono 16 px e il testo finisce **sotto il menu**.

## ⚠️ Che cosa vuol dire «ci sta»

Non «la resa e' corta»: **la resa non aggiunge righe**. Le tre cose che le
aggiungono sono un `<br>` in piu', un `<p>` in piu', e un segmento piu' lungo di
84 caratteri (590 / 7), che va a capo da solo.
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from strumenti import accenti

PASSO = 7            # size / 2, con size = 14
ALTEZZA_RIGA = 16    # size + 2
ALTEZZA_BR = 16
ALTEZZA_P = 24
CODA = 18            # size + 4

DX = 650
GMESW = DX - 60      # god.hsp:450
INIZIO = 70          # god.hsp:449, relativo a wy
MENU = 270 - 2 * 20 - 18   # god.hsp:462 con dy = 270 e listmax = 2
LARGHEZZA_RIGA = GMESW // PASSO

_MARCATORE = re.compile(r'<(/?[a-z0-9]+)>')


def componi(testo: str) -> list[tuple[int, str]]:
    """Le righe come le disegna gmes: (y relativo all'inizio, testo).

    ⚠️ **L'ultima riga NON e' l'ultima posizione del cursore.** Ogni scheda
    finisce con un `<p>`, che sposta il cursore 24 px piu' giu' su una riga che
    poi resta **vuota**: misurare li' dava a Kumiromi wy+206 invece di wy+182,
    cioe' 24 px di sfondamento inventati. Si guarda l'ultima riga che ha del
    testo dentro.
    """
    y = 0
    x = 0
    righe = [[0, '']]
    for pezzo in re.split(r'(<[a-z0-9]+>)', testo):
        if not pezzo:
            continue
        if pezzo == '<br>':
            y += ALTEZZA_BR
            x = 0
            righe.append([y, ''])
            continue
        if pezzo == '<p>':
            y += ALTEZZA_P
            x = 0
            righe.append([y, ''])
            continue
        if _MARCATORE.fullmatch(pezzo):
            continue          # <emp1>, <def>, ... non spostano il cursore
        for carattere in pezzo:
            if x >= GMESW:
                y += ALTEZZA_RIGA
                x = 0
                righe.append([y, ''])
            righe[-1][1] += carattere
            x += PASSO
    return [(a, b) for a, b in righe]


def buff_dei(percorso: str, quale: str) -> dict:
    """Il `buff` di ogni dio, ricostruito dai `buff +=` di `*god_detail`.

    Si legge dal file `.hsp` (sorgente o build) invece che dal dizionario,
    perche' quel che conta e' il testo **composto**, e a comporlo sono piu'
    `lang()` di seguito.
    """
    righe = io.open(percorso, encoding='cp932').read().split('\n')
    dentro = False
    per_dio: dict[str, list[str]] = {}
    corrente = None
    for riga in righe:
        s = riga.strip()
        if s.startswith('*god_detail'):
            dentro = True
            continue
        if dentro and s == 'return':
            break
        if not dentro:
            continue
        trovato = re.search(r'== (GOD_[A-Z]+)', s)
        if trovato:
            corrente = trovato.group(1)
            per_dio.setdefault(corrente, [])
            continue
        if corrente and 'lang(' in s:
            argomenti = _secondo_argomento(s) if quale == 'en' else _primo_argomento(s)
            if argomenti is not None:
                per_dio[corrente].append(argomenti)
    return {dio: ''.join(pezzi) for dio, pezzi in per_dio.items() if pezzi}


def _letterali(s: str) -> list[str]:
    fuori = []
    i = s.find('lang(')
    if i < 0:
        return fuori
    i += 5
    while i < len(s):
        if s[i] == '"':
            j = i + 1
            pezzo = []
            while j < len(s):
                if s[j] == '\\':
                    pezzo.append(s[j:j + 2])
                    j += 2
                    continue
                if s[j] == '"':
                    break
                pezzo.append(s[j])
                j += 1
            fuori.append(''.join(pezzo))
            i = j + 1
            continue
        if s[i] == ')':
            break
        i += 1
    return fuori


def _primo_argomento(s: str) -> str | None:
    pezzi = _letterali(s)
    return pezzi[0] if pezzi else None


def _secondo_argomento(s: str) -> str | None:
    pezzi = _letterali(s)
    return pezzi[1] if len(pezzi) > 1 else None


def main(argv: list[str]) -> None:
    sorgente = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\god.hsp'
    build = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx\god.hsp'
    quale = argv[0] if argv else 'build'
    percorso = build if quale == 'build' and os.path.exists(build) else sorgente
    etichetta = 'build' if percorso == build else 'sorgente'
    schede = buff_dei(percorso, 'en')

    fuori = 0
    for dio, testo in schede.items():
        righe = componi(testo)
        piene = [(y, r) for y, r in righe if r.strip()]
        ultima = INIZIO + (piene[-1][0] if piene else 0)
        segno = '⚠️' if ultima + ALTEZZA_RIGA > MENU else '  '
        if ultima + ALTEZZA_RIGA > MENU:
            fuori += 1
        print(f'{segno} {dio:14} {len(piene):2} righe piene  ultima a wy+{ultima:3}  '
              f'(il menu comincia a wy+{MENU})')
        for y, r in righe:
            if not r.strip():
                continue
            marca = '!' if len(r) > LARGHEZZA_RIGA else ' '
            print(f'      {marca}{len(r):3} wy+{INIZIO + y:3} | {r[:95]}')
    print(f'\n--- {etichetta}: {len(schede)} schede, {fuori} che finiscono sotto il menu '
          f'(riga da {LARGHEZZA_RIGA} caratteri, {GMESW} px a {PASSO} px)')


if __name__ == '__main__':
    main(sys.argv[1:])
