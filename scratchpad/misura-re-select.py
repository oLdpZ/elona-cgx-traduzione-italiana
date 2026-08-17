# -*- coding: utf-8 -*-
"""Le voci di `chatList` non stanno tutte nella stessa finestra.

La rete 15 (`strumenti/menu_dialogo.py`) cerca `chatList` in **tutti** i .hsp e
applica un tetto solo, 52 caratteri, che e' la pergamena del dialogo di
`chat.hsp`. Ma un `chatList` puo' finire in due posti diversi:

    gosub *chat        chat.hsp        pergamena, testo a wx+170, fine a wx+577
    gosub *re_select   event.hsp:4119  finestra dell'evento, larga tx+36

dove `tx` e' la larghezza del **BMP di sfondo** (`file = "bg_re13"`), che cambia
da evento a evento. Questo referto dice, per ogni voce di menu del dizionario,
in quale delle due sta e quanto le resta davvero.

Non e' una guardia: e' una misura, da leggere prima di correggere la rete 15.
"""
import io
import json
import os
import re
import struct
from pathlib import Path

SORGENTE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx')
GRAFICA = Path(r'C:\Games\Elona\elonaplus2.31\graphic')

from strumenti.menu_dialogo import PIXEL_PER_CARATTERE, TETTO, reso

# --- la geometria di *re_select, letta da event.hsp:4145-4195
#   dx = tx + 36                       la finestra, tx = larghezza del bmp
#   cs_list q, wx + 60, ...            dove comincia la voce
#   module.hsp:129  pos arg2 + 4       e altri 4
#   il bordo interno destro sta a dx - 12, simmetrico ai wx + 12 del gcopy
INIZIO_VOCE = 60 + 4
MARGINE_DESTRO = 12


def larghezza_bmp(nome: str) -> int | None:
    percorso = GRAFICA / f'{nome}.bmp'
    if not percorso.exists():
        return None
    testa = percorso.read_bytes()[:26]
    return struct.unpack('<i', testa[18:22])[0]


def tetto_di(bmp: str) -> tuple[int, int] | None:
    tx = larghezza_bmp(bmp)
    if tx is None:
        return None
    dx = tx + 36
    utili = dx - MARGINE_DESTRO - INIZIO_VOCE
    return utili, int(utili / PIXEL_PER_CARATTERE)


# --- per ogni riga con chatList, si guarda in avanti fino al primo gosub: e'
#     quello che dice in quale finestra il menu viene disegnato. All'indietro si
#     cerca l'ultima assegnazione di `file`, cioe' lo sfondo.
#
# ⚠️ **Senza limite di righe, e ci si ferma su un'etichetta o su un `return`.**
# La prima versione guardava avanti sessanta righe e ne lasciava 208 senza
# risposta: il negozio delle carte impagina **253** righe di menu prima del suo
# `gosub *chat_select` (`tcg_custom.hsp:1968` -> `:2221`), e sessanta non
# bastavano nemmeno per `chat.hsp`. Col limite tolto restano tre casi soli, e
# non sono ignoti: sono menu che si ridisegnano **in loco** dentro il proprio
# ciclo (`*cm_stats_WHILE1`, `*com_tone_loop_pgchk`, `*com_config_loop`), e li'
# l'etichetta che li ferma E' il contenitore.
_CHATLIST = re.compile(r'\bchatList\b')
_GOSUB = re.compile(r'\bgosub\s+\*(\w+)')
_ETICHETTA = re.compile(r'^\*(\w+)')
_FILE = re.compile(r'^\s*file\s*=\s*"([^"]+)"')

contenitore: dict[tuple[str, int], tuple[str, str]] = {}
for percorso in sorted(SORGENTE.glob('*.hsp')):
    righe = percorso.read_bytes().decode('cp932', 'replace').split('\n')
    for i, riga in enumerate(righe, start=1):
        if not _CHATLIST.search(riga):
            continue
        dove = '?'
        for j in range(i, len(righe)):
            trovato = _GOSUB.search(righe[j])
            if trovato:
                dove = trovato.group(1)
                break
            etichetta = _ETICHETTA.match(righe[j])
            if etichetta:
                dove = etichetta.group(1)
                break
            if righe[j].strip() == 'return':
                break
        sfondo = '?'
        for j in range(i - 2, max(0, i - 40), -1):
            trovato = _FILE.match(righe[j])
            if trovato:
                sfondo = trovato.group(1)
                break
        contenitore[(percorso.name, i)] = (dove, sfondo)

voci = []
for percorso in sorted(Path('dizionario').glob('*.jsonl')):
    nome = percorso.name.removesuffix('.jsonl')
    for linea in io.open(percorso, encoding='utf-8'):
        if not linea.strip():
            continue
        voce = json.loads(linea)
        chiave = (nome, voce['riga'])
        if chiave in contenitore:
            voce['_dove'], voce['_sfondo'] = contenitore[chiave]
            voce['_file'] = nome
            voci.append(voce)

conto: dict[str, int] = {}
for chiave, (dove, _) in contenitore.items():
    conto[dove] = conto.get(dove, 0) + 1
print('righe di menu nel sorgente, per finestra:')
for dove, n in sorted(conto.items(), key=lambda x: -x[1]):
    print(f'    {dove:<20} {n:5d}')
print()

print(f'voci tradotte che la rete 15 misura: {len(voci)}')
print(f'tetto che applica a tutte: {TETTO} caratteri\n')

sfori = []
for voce in voci:
    if voce['_dove'] != 're_select':
        continue
    misura = tetto_di(voce['_sfondo'])
    if misura is None:
        print(f"⚠️ {voce['_file']}:{voce['riga']}  sfondo {voce['_sfondo']!r} non trovato")
        continue
    utili, tetto = misura
    for campo, chi in (('it', 'resa'), ('en_grezzo', 'inglese')):
        testo = reso(voce.get(campo) or '')
        if len(testo) > tetto:
            sfori.append((voce['_file'], voce['riga'], chi, len(testo), tetto,
                          voce['_sfondo'], testo))

per_sfondo: dict[str, int] = {}
for voce in voci:
    if voce['_dove'] == 're_select':
        per_sfondo[voce['_sfondo']] = per_sfondo.get(voce['_sfondo'], 0) + 1
print('voci tradotte dentro *re_select, per sfondo (tetto vero fra parentesi):')
for sfondo, n in sorted(per_sfondo.items()):
    misura = tetto_di(sfondo)
    detto = f'{misura[1]} caratteri, {misura[0]} px' if misura else 'sfondo non trovato'
    print(f'    {sfondo:<12} {n:4d} voci   ({detto})')
print()

if sfori:
    print('FUORI MISURA sul tetto vero di *re_select:')
    for file, riga, chi, n, tetto, sfondo, testo in sorted(sfori):
        print(f'  {file}:{riga}  {chi:<8} {n} > {tetto}  [{sfondo}]  {testo[:70]}')
else:
    print('nessuna voce gia\' tradotta sfora il tetto vero di *re_select')
