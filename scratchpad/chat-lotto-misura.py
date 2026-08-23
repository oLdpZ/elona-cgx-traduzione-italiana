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
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from importlib import import_module

chat_righe = import_module('chat_righe')
talk_conv = chat_righe.talk_conv

# ⭐ 89a: il conto dei bottoni adesso sta in `strumenti/`, perche' lo vuole
# anche `menu_dialogo` per la soglia delle due colonne. Una funzione sola, una
# fonte sola: se la si tiene in due posti, la prossima correzione ne ripara uno
# (68a, «se una rete conta, sta in strumenti/ e ha un test»).
sys.path.insert(0, str(Path(__file__).parent.parent))
from strumenti.menu_dialogo import opzioni_del_menu as opzioni

SORGENTE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp')
TETTO_MENU = 58


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
