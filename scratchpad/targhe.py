# -*- coding: utf-8 -*-
"""La targa dei messaggi di `screen_drawMsg2`, e il suo tetto di 89 caratteri.

`screen.hsp:2255` disegna una targa larga quanto il testo — `sx = strlen(s) * 8
+ 45` — e la **tappa a 760**:

    sx = strlen(s) * 8 + 45
    if ( sx > 760 ) { sx = 760 }
    ...
    pos msgx + 18, msgy + 4
    mes s

Il `mes` non taglia e non va a capo: passata la tappa, la targa smette di
crescere e il testo le esce da destra, su fondo nudo. Il tetto e' quindi

    strlen * 8 + 45 <= 760   ->   strlen <= 89

⭐ **La formula la prova l'inglese**, come per la rete 16: la frase piu' lunga
di monte che passa di qui — «Tell me one of your notable skills. The ones with
a mark overlap with your class or race.» (`chara.hsp:3921`) — ne ha **89
esatti**, cioe' tocca il limite e non lo passa. Sarebbe una coincidenza
notevole se il conto fosse sbagliato.

⚠️ **Il carattere qui e' piu' grande che altrove**: `font …, 16 - en * 2` fa
**14**, non 12, e infatti il codice conta 8 px per carattere invece di 7. Chi
riusasse il passo da 7 delle altre reti sbaglierebbe di un ottavo.

## Perche' e' il quattordicesimo punto cieco

Nessuna delle reti di geometria passa di qui: `larghezze` guarda i menu di
`*prompt_key`, `riquadri` le piastrelle dell'HUD, `menu_dialogo` le voci di
`chatList`, `diario` il diario, `linguette` le schede, `misura-trait` la
finestra dei talenti. La targa di `screen_drawMsg2` la disegna **tutta la
creazione del personaggio** — ventun chiamate in `chara.hsp` — piu'
`custom_ai.hsp`, `custom_tweaks.hsp`, `main.hsp` e `system.hsp`: 54 siti.

Trovato nella 63a traducendo `chara.hsp`, non da un referto.
"""
import io
import os
import re
import sys

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'

PASSO = 8               # screen.hsp:2262, `strlen(s) * 8`
CORNICE = 45            # screen.hsp:2262, il `+ 45`
TAPPO = 760             # screen.hsp:2263
TETTO = (TAPPO - CORNICE) // PASSO      # 89

_LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')
_ASSEGNA = re.compile(r'^\s*s\s*=\s*(.+)$')
_CHIAMA = re.compile(r'^\s*gosub\s+\*screen_drawMsg2\s*$')


def leggi(percorso):
    with io.open(percorso, encoding='cp932', errors='replace') as f:
        return f.read().split('\n')


def raccogli(radice):
    """[(file, riga, testo)] per ogni `s = …` che finisce in una targa.

    ⚠️ Si risale dall'**uso**, non dalla forma: solo le `s = …` seguite entro
    poche righe da `gosub *screen_drawMsg2` disegnano una targa. Cercare tutte
    le `s = "…"` del sorgente misurerebbe una cosa vicina invece della cosa.
    """
    fuori = []
    for nome in sorted(os.listdir(radice)):
        if not nome.endswith('.hsp'):
            continue
        righe = leggi(os.path.join(radice, nome))
        for n, riga in enumerate(righe):
            if not _CHIAMA.match(riga):
                continue
            for k in range(n - 1, max(n - 6, -1), -1):
                m = _ASSEGNA.match(righe[k])
                if not m:
                    continue
                coppie = _LANG.findall(m.group(1))
                if coppie:
                    fuori.append((nome, k + 1, coppie[0][1]))
                break
    return fuori


def main(argv):
    en = {(f, r): t for f, r, t in raccogli(SORGENTE)}
    it = {(f, r): t for f, r, t in raccogli(BUILD)}
    print('LA TARGA DI screen_drawMsg2')
    print(f'tetto: strlen * {PASSO} + {CORNICE} <= {TAPPO}, cioe\' '
          f'{TETTO} caratteri')
    print()
    for etichetta, quale in (("l'inglese di monte", en), ('la build', it)):
        fuori = [k for k, t in quale.items() if len(t) > TETTO]
        piu_lungo = max((len(t) for t in quale.values()), default=0)
        print(f'    {etichetta:<20} {len(quale):>3} targhe   '
              f'fuori {len(fuori):>2}   la piu\' lunga {piu_lungo}')
    print()

    nostre = []
    for chiave, testo in it.items():
        monte = en.get(chiave)
        if monte is None:
            continue
        if len(monte) <= TETTO < len(testo):
            nostre.append((len(testo), chiave, testo, monte))
    print(f"=== DOVE L'INGLESE CI STA E NOI NO: {len(nostre)} ===")
    for quanto, (f, r), testo, monte in sorted(nostre, reverse=True):
        print(f'  {quanto:3d}/{TETTO}  {f}:{r}')
        print(f'      it  {testo}')
        print(f'      en  {monte}')

    if '--tutte' in argv:
        print()
        print('=== tutte le targhe, per lunghezza ===')
        for chiave, testo in sorted(it.items(), key=lambda kv: -len(kv[1])):
            print(f'  {len(testo):3d}  {chiave[0]}:{chiave[1]}  {testo[:70]}')
    return 1 if nostre else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
