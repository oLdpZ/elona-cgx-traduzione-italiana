# -*- coding: utf-8 -*-
"""97a - La larghezza del pannello «Conoscenza dell'oggetto» di `command.hsp`.

⚠️ **Nessuna guardia del progetto misura questo riquadro.** `larghezze.py`
guarda i menu di `text.hsp` e i siti di `*prompt_key`; `riquadri.py` le
piastrelle di stato e i `buffname`; `menu_dialogo.py` le voci del dialogo.
Il pannello che si apre esaminando un oggetto non e' nessuno dei tre — le sue
voci sono `listn(0, p)` scritte a mano una per una — ed e' il punto cieco della
74a visto da dentro (`RIPRESA-sessione.md`, punto 12: restano 100 righe
`listn(...) = lang(...)` in `command.hsp`).

IL METRO, LETTO DAL SORGENTE (`command.hsp:16866`-`:16877`):

    display_window (windoww - 600) / 2 + inf_screenx, winposy(408), 600, 408
    font lang(cfg_font1, cfg_font2), 14 - en * 2, 0
    pos wx + 68, wy + 68 + cnt * 18

Il riquadro e' largo **600 px**, il testo comincia a **wx + 68**, e il margine
destro si legge dal titolo (`display_topic … wx + 28`): sono **28 px**. Restano
**504 px**, e a `PIXEL_PER_CARATTERE = 7.7` — la misura a schermo della 34a, per
il font 12, che e' esattamente quello di qui (`14 - en * 2` con `en = 1`) — il
budget e' **65 caratteri**.

⚠️ Il referto NON dice «fuori misura, si accorci». Dice **due** numeri, come
`intestazioni_larghezze`: se sfora anche l'inglese, il traboccamento non
l'abbiamo introdotto noi e la riga era gia' cosi'. Quel che deve restare a zero
e' la **terza** colonna: le righe dove l'italiano sfora e l'inglese no.

    python scratchpad/_97-conoscenza-larghezza.py
"""
import io
import json
import re

from strumenti.accenti import degrada

PIXEL_PER_CARATTERE = 7.7
LARGHEZZA = 600
INSET_SINISTRO = 68
MARGINE_DESTRO = 28
BUDGET = int((LARGHEZZA - INSET_SINISTRO - MARGINE_DESTRO) / PIXEL_PER_CARATTERE)

# cifre supposte per un valore interpolato, come in `strumenti/larghezze.py`
LARGHEZZA_NUMERO = 3

# le righe del pannello: `:16054`-`:16420` piu' il titolo di `:16867`
DA, A = 16054, 16867

# ⚠️ Due voci non finiscono dove finisce la `lang()`: il sorgente ci appende una
# coda fuori da ogni dizionario, e chi misurasse la sola resa direbbe un numero
# piu' corto del vero.
CODE = {
    16349: ' [Lv:## Exp:###%]',        # `:16349`, la crescita dell'oggetto vivo
    16365: ' (#d## perfora ###%)',     # `:16365`, i dadi e la penetrazione
}

_PEZZO = re.compile(r'"((?:[^"\\]|\\.)*)"')


def reso(it: str) -> str:
    """Il testo che finisce a schermo, dall'`it` del dizionario.

    Una resa dinamica e' un'espressione HSP: si tengono i letterali e si conta
    ogni interpolazione come `LARGHEZZA_NUMERO` caratteri.
    """
    if not it.lstrip().startswith('"'):
        return degrada(it)
    pezzi = _PEZZO.findall(it)
    interpolazioni = max(0, len(pezzi) - 1)
    return degrada(''.join(pezzi)) + '#' * (LARGHEZZA_NUMERO * interpolazioni)


def inglese(en: str, tipo: str) -> str:
    # nell'estrazione l'inglese di una voce dinamica ha gia' i buchi al posto
    # dei valori: si riempiono con lo stesso metro dell'italiano
    if tipo != 'dinamica':
        return en
    return en + '#' * LARGHEZZA_NUMERO * en.count('  ')


voci = [json.loads(l) for l in io.open('dizionario/command.hsp.jsonl', encoding='utf-8')
        if l.strip()]
voci = [v for v in voci if DA <= v['riga'] <= A and v.get('it')]

sfora_it = sfora_en = solo_it = 0
print(f'budget: {BUDGET} caratteri  ({LARGHEZZA} px - {INSET_SINISTRO} - {MARGINE_DESTRO}, '
      f'a {PIXEL_PER_CARATTERE} px/carattere)\n')
for v in sorted(voci, key=lambda v: v['riga']):
    coda = CODE.get(v['riga'], '')
    testo = reso(v['it']) + coda
    en = inglese(v['en'], v['tipo']) + coda
    marca = ''
    if len(testo) > BUDGET:
        sfora_it += 1
        marca = '  <<< FUORI MISURA'
        if len(en) > BUDGET:
            sfora_en += 1
            marca += ' (sfora anche l\'inglese)'
        else:
            solo_it += 1
    print(f'{v["riga"]:6d}  it {len(testo):3d}  en {len(en):3d}  {testo!r}{marca}')

print(f'\nvoci misurate: {len(voci)}')
print(f'fuori misura: {sfora_it}   di cui gia\' fuori in inglese: {sfora_en}')
print(f'⚠️ introdotte dall\'italiano: {solo_it}   (atteso: 0)')
