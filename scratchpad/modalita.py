# -*- coding: utf-8 -*-
"""Le descrizioni delle modalita' nella creazione del personaggio.

`chara.hsp:4191`-`:4315` disegna la scheda di ognuna delle sei modalita' —
Essential, Loss, Overdose, Natural, Abnormal, Purge — una riga per volta:

    s = lang("…", "…")
    pos wx + 165, wy + 66 + n * 15
    mes s

Il `mes` non taglia e non va a capo. La finestra e' larga **680**
(`chara.hsp:4170`), quindi da `wx + 165` restano **515 px**, e il carattere
qui e' `13 - en * 2` = **11**, cioe' 7 px.

    515 / 7 = 73 caratteri

⭐ Come per la rete 16 e per le targhe, la formula la prova l'inglese: la riga
di monte piu' lunga ne ha 73 esatti (o giu' di li' — il referto lo stampa), e
nessuna la passa.

⚠️ Non e' il tetto delle targhe: li' il carattere e' 14 e il passo 8. Due
finestre vicine, due metri diversi.
"""
import io
import os
import re
import sys

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'

LARGHEZZA = 680         # chara.hsp:4170
INIZIO = 165            # chara.hsp:4193, `pos wx + 165`
PASSO = 7               # font 13 - en*2 = 11
TETTO = (LARGHEZZA - INIZIO) // PASSO       # 73

_LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')
_RIGA = re.compile(r'^\s*s\s*=\s*lang\(')
_POS = re.compile(r'^\s*pos\s+wx\s*\+\s*165\s*,')


def leggi(percorso):
    with io.open(percorso, encoding='cp932', errors='replace') as f:
        return f.read().split('\n')


def raccogli(radice):
    """[(riga, testo)] per ogni `s = lang(..)` seguita da `pos wx + 165`.

    ⚠️ Si risale dall'uso: e' il `pos wx + 165` a dire che quella riga finisce
    nella colonna stretta della scheda, non la forma dell'assegnazione.
    """
    righe = leggi(os.path.join(radice, 'chara.hsp'))
    fuori = []
    for n, riga in enumerate(righe):
        if not _RIGA.match(riga):
            continue
        if n + 1 < len(righe) and _POS.match(righe[n + 1]):
            coppie = _LANG.findall(riga)
            if coppie:
                fuori.append((n + 1, coppie[0][1]))
    return fuori


def main(argv):
    en = dict(raccogli(SORGENTE))
    it = dict(raccogli(BUILD))
    print('LE SCHEDE DELLE MODALITA` (chara.hsp:4191)')
    print(f'tetto: ({LARGHEZZA} - {INIZIO}) / {PASSO} = {TETTO} caratteri')
    print()
    for etichetta, quale in (("l'inglese di monte", en), ('la build', it)):
        fuori = [r for r, t in quale.items() if len(t) > TETTO]
        piu_lungo = max((len(t) for t in quale.values()), default=0)
        print(f'    {etichetta:<20} {len(quale):>3} righe   '
              f'fuori {len(fuori):>2}   la piu\' lunga {piu_lungo}')
    print()
    nostre = [(len(t), r, t, en[r]) for r, t in it.items()
              if r in en and len(en[r]) <= TETTO < len(t)]
    print(f"=== DOVE L'INGLESE CI STA E NOI NO: {len(nostre)} ===")
    for quanto, r, testo, monte in sorted(nostre, reverse=True):
        print(f'  {quanto:3d}/{TETTO}  chara.hsp:{r}')
        print(f'      it  {testo}')
        print(f'      en  {monte}')

    if '--tutte' in argv:
        print()
        for r, t in sorted(it.items()):
            print(f'  {r:>5}  {len(t):>3}  {t}')
    return 1 if nostre else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
