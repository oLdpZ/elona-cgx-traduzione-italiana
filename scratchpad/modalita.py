# -*- coding: utf-8 -*-
"""Le descrizioni delle modalita' nella creazione del personaggio.

`chara.hsp:4191`-`:4315` disegna la scheda di ognuna delle sei modalita' —
Essential, Loss, Overdose, Natural, Abnormal, Purge — una riga per volta:

    s = lang("…", "…")
    pos wx + 165, wy + 66 + n * 15
    mes s

Il `mes` non taglia e non va a capo. La finestra e' larga **680**
(`chara.hsp:4170`), quindi da `wx + 165` restano **515 px** di carta, e il
carattere qui e' `13 - en * 2` = **11**, cioe' **7 px** per cella.

    515 / 7 = 73 caratteri

⚠️⚠️ **Ma il tetto vero e' 72, e lo dice lo schermo.** La 65a ha guardato
tutte e sei le schede e ha misurato la riga piu' lunga della build — «- Ricarica
con F2 per rigiocare la sorte. Salvataggio automatico spento.», **72 caratteri**
— che arriva a **500 px** di inchiostro su **503** disponibili. I 515 del conto
geometrico non tolgono il **bordo interno** della pergamena: contando la *cella*
invece dell'inchiostro (l'ultimo carattere e' un punto, due pixel di inchiostro
e sette di cella) la riga finisce **esattamente sul bordo**. Il 73esimo carattere
esce.

⚠️ **E l'inglese di monte ha una riga da 73**, che sarebbe la prima a sfondare:
non l'ha mai vista nessuno a schermo, e non e' un permesso ma un avviso. Qui la
regola della 63a — *l'inglese tocca il tetto* — non aiuta a ricavare il numero,
perche' upstream lo passa di uno.

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
PASSO = 7               # font 13 - en*2 = 11; 7 px per cella, misurati nella 65a
SPAZIO = 503            # px di carta veri, MISURATI a schermo nella 65a (non 515:
                        # il conto geometrico non toglie il bordo interno)
TETTO = 72              # 72 celle da 7 fanno 504 px e l'ultima e' un punto, due
                        # px di inchiostro: la riga finisce esattamente sul bordo

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
    print(f'tetto: {TETTO} caratteri ({SPAZIO} px misurati / {PASSO} per cella; il conto geometrico ne darebbe 73)')
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
