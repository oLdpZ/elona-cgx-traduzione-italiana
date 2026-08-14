# -*- coding: utf-8 -*-
"""Le righe di un .hsp che stanno dentro un commento di blocco `/* ... */`.

⚠️ Nata nella 37a: `proc.hsp:11796` e' dentro un blocco
`/********** ORIGINAL - BEGINNING **********  ...  ********** ORIGINAL - ENDING **********/`
— codice di monte spento dal mod — e la **rete 6 non lo vedeva**, perche' guarda
solo le righe che cominciano per `;`. Una voce dentro un blocco spento e' testo
che il giocatore non leggera' mai: va rinviata, non tradotta.

    python scratchpad/commenti-blocco.py proc.hsp            # tutte
    python scratchpad/commenti-blocco.py proc.hsp 11500 12500  # solo una zona
"""
import io
import sys

# ⚠️ Si legge il SORGENTE pinnato, non la build: i numeri di riga del dizionario
# vengono da lì, e una toppa che aggiunge una riga sposta tutto quello che segue
# nella build. Misurato nella 37a: `text.hsp` ha **una riga in più** nella build
# (12.528 contro 12.527), e la misura fatta sulla build accusava due voci giuste.
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'


def righe_in_commento(percorso: str) -> set:
    """I numeri di riga (1-based) coperti da un commento di blocco.

    ⚠️ I delimitatori si cercano fuori dalle stringhe e fuori dai commenti di
    riga (`;`), se no un `/*` scritto dentro un letterale spegnerebbe meta' file.
    """
    testo = io.open(percorso, encoding='cp932').read().split('\n')
    dentro = False
    fuori = set()
    for n, riga in enumerate(testo, 1):
        i = 0
        in_stringa = False
        apre_qui = False
        while i < len(riga):
            due = riga[i:i + 2]
            if dentro:
                if due == '*/':
                    dentro = False
                    i += 2
                    continue
                i += 1
                continue
            if riga[i] == '"':
                in_stringa = not in_stringa
            elif not in_stringa and riga[i] == ';':
                break
            elif not in_stringa and due == '/*':
                dentro = True
                apre_qui = True
                i += 2
                continue
            i += 1
        if dentro or apre_qui:
            fuori.add(n)
    return fuori


if __name__ == '__main__':
    nome = sys.argv[1]
    spente = righe_in_commento(f'{SORGENTE}\\{nome}')
    if len(sys.argv) > 3:
        da, a = int(sys.argv[2]), int(sys.argv[3])
        zona = sorted(n for n in spente if da <= n <= a)
        print(f'{nome}: {len(zona)} righe spente fra {da} e {a}')
        print(zona)
    else:
        print(f'{nome}: {len(spente)} righe dentro un commento di blocco')
