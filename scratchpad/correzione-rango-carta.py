# -*- coding: utf-8 -*-
"""Correzione: il numero di una carta e' il suo «valore», non il suo «rango».

`command.hsp:6770` chiede 「変化後のランクは？」 subito dopo la voce di menu
【ランクチェンジ】 di `:5985`, e chiede un numero **da 1 a 13** (`:6772`) che
finisce in `CDATA_EVOLUTION_STAGE`: e' il valore della carta, non un grado.

Tre stringhe si rimandano l'una all'altra e finora due dicevano cose diverse:

  - `proc.hsp:20184` e' la frase che **insegna** la cosa, ed e' gia' spedita:
    «Dal menu d'interazione puoi cambiarne **seme e valore** a piacere.»
  - `command.hsp:5985` e' la voce di menu, resa nel lotto 040 «<Cambia valore>»;
  - `command.hsp:6770` e' il prompt che compare **un clic dopo**, e diceva
    «Quale rango?».

⚠️ E «rango» in questo stesso file e' gia' preso: `:4192` «Rango degli
avventurieri», `:4194` «Nome e rango», piu' i gradi di gilda di `text.hsp`. Due
concetti diversi con la stessa parola, a due righe di distanza.

Misurato prima di toccare: in `dizionario/command.hsp.jsonl` la riga 6770 ha una
voce sola, e nessun'altra resa del file contiene «rango» riferito a una carta.
"""
import io
import json

PERCORSO = 'dizionario/command.hsp.jsonl'
RIGA = 6770
PRIMA = 'Quale rango?'
DOPO = 'Quale valore?'

voci = [json.loads(l) for l in io.open(PERCORSO, encoding='utf-8') if l.strip()]
scelte = []
for v in voci:
    if v['riga'] == RIGA and v.get('it') == PRIMA:
        v['it'] = DOPO
        scelte.append(v)

if len(scelte) != 1:
    raise SystemExit(f'attesa 1 voce a command.hsp:{RIGA} con it={PRIMA!r}, '
                     f'trovate {len(scelte)}')

with io.open('lavoro/correzione-rango-carta.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for v in scelte:
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
for v in scelte:
    print(f"{v['riga']}  en={v['en']!r}  {PRIMA!r}  ->  it={v['it']!r}")
print('scritto lavoro/correzione-rango-carta.jsonl')
