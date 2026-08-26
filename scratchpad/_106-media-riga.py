# -*- coding: utf-8 -*-
"""106a - quale carta e' passata sopra i 61 caratteri di riga media.

Nato perche' `_102-carta-conoscenza.py` e' passato da «1 su 1144» a «0 su 1144»
senza che nessuno avesse toccato la carta sospetta: un numero atteso che cambia
da solo e' un guasto finche' non si sa perche'.

💡 La risposta e' nella riga `testo = degrada(it) if it else en` di quello
strumento: il conto gira su **tutte** le 1144 carte, e per quelle non ancora
rese misura **l'inglese**. Quindi ogni lotto puo' spostare il numero senza che
nessuno tocchi la carta che stava sotto: basta che la sua resa italiana, piu'
lunga dell'inglese, passi sopra la soglia.
"""
import importlib.util
import io
import json
import pathlib
import sys

spec = importlib.util.spec_from_file_location(
    'ck', pathlib.Path(__file__).with_name('_102-carta-conoscenza.py'))
ck = importlib.util.module_from_spec(spec)
sys.argv = [sys.argv[0]]
spec.loader.exec_module(ck)


def media(testo: str):
    r, _ = ck.impagina(testo)
    piene = r[:-1] if len(r) > 1 else r
    return sum(len(x) for x in piene) / len(piene) if piene else None


voci = [json.loads(l) for l in io.open('dizionario/db_card.hsp.jsonl', encoding='utf-8')
        if l.strip()]
for v in voci:
    if not (9101 <= v['riga'] <= 11100):
        continue
    it, en = v.get('it') or '', v.get('en') or ''
    m_en, m_it = media(en), media(ck.degrada(it)) if it else None
    if m_en is not None and m_en < ck.GIRI_SU:
        print(f":{v['riga']}   inglese {m_en:5.1f}  ->  italiano "
              f"{m_it if m_it is None else round(m_it, 1)}   {en[:50]}...")
