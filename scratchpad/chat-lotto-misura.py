# -*- coding: utf-8 -*-
"""Misura un lotto di `chat.hsp` nella finestra del dialogo.

Riusa il simulatore di `talk_conv` di `chat_righe.py` (54a), che replica il ramo
inglese di `init.hsp:1326` — e NON e' un `textwrap`: taglia sugli spazi, quindi
una parola piu' lunga della riga sfonda invece di spezzarsi.

Tre misure, ognuna col suo tetto letto nel sorgente:

  MENU   voce di `chatList`  -> tetto 58 caratteri (`chat_select`, 407 px / 7)
  BUFF   battuta + N bottoni -> (324 - N*19 - 43) // 19 righe
  PIU    `chatMore`, 1 bottone -> 13 righe

E per ogni battuta confronta le righe dell'italiano con quelle dell'inglese: la
regola prudente della 73a e' che l'italiano non ne faccia di piu'.

    python scratchpad/chat-lotto-misura.py lavoro/75-chat-lavoro.jsonl
"""
import collections
import io
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from importlib import import_module

chat_righe = import_module('chat_righe')
talk_conv = chat_righe.talk_conv

SORGENTE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp')
TETTO_MENU = 58


GUARDIA = re.compile(r'^if\s*\((.*?)==\s*([^)]*?)\s*\)\s*\{?$')


def opzioni(src: list, riga: int) -> int:
    """Quanti bottoni ha la finestra in cui esce la battuta di questa riga.

    ⚠️ 87a: **le `chatList` dentro guardie che si escludono a vicenda non si
    sommano.** Il seminario ne e' la prova: i quattro docenti hanno sedici
    `chatList` in fila, quattro per ognuno dei quattro incontri, e ogni gruppo
    sta dentro un `if ( gdata(STARTING_GDATA_FLAG + 329) == N ) {` con N che
    cambia. A schermo i bottoni sono **quattro**, non sedici, e con sedici il
    tetto viene negativo: qualunque battuta risulta fuori misura.

    La regola: si raggruppano le `chatList` per la guardia che le contiene, e
    per ogni SINISTRA di `==` si prende il gruppo piu' numeroso invece della
    somma — due `if` che confrontano la stessa cosa con costanti diverse non
    possono essere veri insieme. I gruppi con sinistre diverse, e le `chatList`
    fuori da ogni guardia, si sommano lo stesso: li' l'esclusione non si sa.

    💡 Prima della correzione il numero era sbagliato anche quando non lo
    sembrava: nel lotto di Ajetalio la passeggiata all'indietro si fermava su
    una riga **commentata** (`// chatList 4`), contava 12 invece di 16, e il
    tetto tornava positivo per caso.
    """
    libere = 0
    gruppi = collections.defaultdict(list)   # sinistra di `==` -> conti
    corrente = 0
    dentro = False
    i = riga - 2
    while i >= 0 and riga - i < 60:
        s = src[i].strip()
        if s.startswith('chatList') or s.startswith('chatlist'):
            if dentro:
                corrente += 1
            else:
                libere += 1
        elif s.startswith('}'):
            dentro = True
            corrente = 0
        elif s.startswith('if ('):
            m = GUARDIA.match(s)
            if dentro:
                gruppi[m.group(1).strip() if m else s].append(corrente)
                dentro = False
                corrente = 0
        elif s.startswith('else') or s == '':
            pass
        else:
            break
        i -= 1
    n = libere + sum(max(c) for c in gruppi.values())
    return max(n, 1)


def testo_reso(v: dict) -> str:
    """Il testo che finisce a schermo: una statica e' nuda, una dinamica e' una
    espressione e i pezzi fra virgolette sono il solo testo che si legge."""
    it = v['it']
    if v['tipo'] == 'statica':
        return it.replace('\\"', '"').replace("\\'", "'")
    fuori = []
    dentro = False
    pezzo = ''
    i = 0
    while i < len(it):
        c = it[i]
        if c == '\\' and i + 1 < len(it):
            pezzo += it[i + 1]
            i += 2
            continue
        if c == '"':
            if dentro:
                fuori.append(pezzo)
                pezzo = ''
            dentro = not dentro
        elif dentro:
            pezzo += c
        i += 1
    return ''.join(fuori)


def main() -> int:
    lotto = sys.argv[1]
    src = io.open(SORGENTE, encoding='cp932', errors='replace').read().split('\n')
    fuori = 0
    peggiorate = 0
    for l in io.open(lotto, encoding='utf-8'):
        v = json.loads(l)
        r = v['riga']
        s = src[r - 1].strip()
        it = testo_reso(v)
        en = v['en'] if v['tipo'] == 'statica' else v['en']
        if s.startswith('chatList') or s.startswith('chatlist'):
            if len(it) > TETTO_MENU:
                fuori += 1
                print('MENU  %6d  %3d car > 58   %s' % (r, len(it), it))
            continue
        if s.startswith('txt'):
            continue
        n = 1 if s.startswith('chatMore') else opzioni(src, r)
        tetto = (324 - n * 19 - 43) // 19
        rit = len(talk_conv(it))
        ren = len(talk_conv(en))
        marchio = ''
        if rit > tetto:
            fuori += 1
            marchio = '  *** FUORI: tetto %d' % tetto
        elif rit > ren:
            peggiorate += 1
            marchio = '  (una riga in piu\' dell\'inglese: %d contro %d)' % (rit, ren)
        if marchio:
            print('%-5s %6d  %d bottoni, %2d righe%s' % (
                'PIU' if s.startswith('chatMore') else 'BUFF', r, n, rit, marchio))
    print()
    print('fuori misura: %d ; peggiorate rispetto all\'inglese: %d' % (fuori, peggiorate))
    return 1 if fuori else 0


if __name__ == '__main__':
    sys.exit(main())
