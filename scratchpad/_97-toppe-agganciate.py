# -*- coding: utf-8 -*-
"""97a - Quante toppe abbiano davvero agganciato: il numero atteso che mancava.

⚠️⚠️⚠️ **IL PUNTO 6 DELLA RIPRESA, APERTO DALLA 96a.** `applica` non si ferma
quando una toppa non aggancia: stampa la riga e continua. In un output di decine
di righe chi guarda la coda non la vede, ed e' cosi' che la 96a ha spedito nel
gioco un eseguibile senza la toppa del «(marcio)». La 97a ci e' ricascata dal
lato opposto — rendendo `map.hsp:1396`, che era l'ancora della toppa di
migrazione della 42a — e li' `applica` e' pure **uscito con 1**, ma
`compila --eseguibile` ha prodotto lo stesso il suo eseguibile dal solito albero
incompleto. Il codice d'uscita non basta: i due comandi non sono incatenati
apposta.

Quel che serviva era **un numero con un valore atteso**, e la 96a lo aveva
scritto: «il conto (`item_func.hsp: 35 toppe`) era l'unico segnale, e nessuno lo
confronta con niente». Questo modulo e' quel confronto, e lo fa **sull'albero di
build**, cioe' sul risultato e non sull'intenzione: per ogni toppa guarda se il
testo che doveva mettere ci sia.

    aggancia    il `sostituisci` della toppa e' nel file costruito
    ⚠️ MANCA    non c'e': la toppa e' saltata, e il difetto che riparava e' tornato

⚠️ Il valore atteso e' **1023 su 1023**. Un solo «MANCA» vuol dire che la build
in `C:\Games\Elona\_traduzione\build` e' incompleta, e con lei l'eseguibile che
sta nel gioco.

⚠️ Legge la **build**, quindi su una macchina senza albero costruito non dice
«manca una toppa»: muore di file non trovato. Come `strumenti.gronde`.

    python scratchpad/_97-toppe-agganciate.py
"""
import io
import json
import os
import sys

# ⚠️ Il primo argomento serve alla **prova al contrario**: puntando la guardia sul
# sorgente pinnato, dove nessuna toppa e' stata applicata, deve dire rosso su
# quasi tutte. Una guardia che non si e' mai vista dire rosso non e' una
# guardia, e' una riga di output.
BUILD = sys.argv[1] if len(sys.argv) > 1 else r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'


def righe_di(t, campo):
    """Il `cerca`/`sostituisci` di una toppa, che puo' essere una riga o un elenco."""
    c = t.get(campo)
    if isinstance(c, list):
        return '\n'.join(c)
    return c or ''


toppe = [json.loads(l) for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]

testo_di = {}
for t in toppe:
    nome = t.get('file')
    if nome in testo_di:
        continue
    percorso = os.path.join(BUILD, nome)
    if not os.path.exists(percorso):
        print(f'⚠️ {nome} non c\'e\' nella build: l\'albero non e\' costruito')
        sys.exit(1)
    testo_di[nome] = io.open(percorso, encoding='cp932', errors='replace').read()

agganciate = mancanti = 0
per_file = {}
for t in toppe:
    nome = t.get('file')
    messo = righe_di(t, 'sostituisci')
    per_file.setdefault(nome, [0, 0])
    # ⚠️⚠️ Le dodici toppe dichiarate `prima` girano **sull'albero ancora
    # inglese**, e il dizionario poi riscrive le `lang()` che il loro
    # `sostituisci` si porta dentro: cercarlo alla lettera nella build da' dieci
    # falsi allarmi su dieci (`command.hsp` sette, `blend`, `economy`,
    # `map_user`, `config` uno per uno). Su quelle si guarda l'altra meta' del
    # fatto: che la riga di partenza **non ci sia piu'**.
    # ⚠️ E' una prova piu' debole — il dizionario da solo puo' far sparire una
    # riga, ed e' esattamente cosi' che la 97a ha rotto la toppa di `map.hsp` —
    # ma per le `prima` non c'e' di meglio, e sono dodici su 1023.
    if t.get('prima'):
        cercato = righe_di(t, 'cerca')
        ok = bool(cercato) and cercato not in testo_di[nome]
    else:
        ok = bool(messo) and messo in testo_di[nome]

    if ok:
        agganciate += 1
        per_file[nome][0] += 1
    else:
        mancanti += 1
        per_file[nome][1] += 1
        print(f'⚠️ MANCA  {nome}: {messo.splitlines()[0][:100] if messo else "(vuoto)"}')
        print(f'          motivo: {(t.get("motivo") or "")[:140]}…')

print()
for nome in sorted(per_file):
    ok, ko = per_file[nome]
    marca = f'   ⚠️ {ko} MANCANTI' if ko else ''
    print(f'{nome:<28} {ok:4d} agganciate{marca}')

print(f'\ntoppe: {len(toppe)}   agganciate: {agganciate}   ⚠️ mancanti: {mancanti}   (atteso: 0)')
sys.exit(1 if mancanti else 0)
