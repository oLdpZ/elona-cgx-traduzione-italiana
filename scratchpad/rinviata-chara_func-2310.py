# -*- coding: utf-8 -*-
"""Registra `chara_func.hsp:2310` fra le rinviate: riga dentro un blocco spento.

⚠️ **La forma della scrittura non e' un dettaglio.** Nella 39ª uno script ha
troncato `toppe.jsonl` a ZERO byte perche' apriva il file in scrittura e
componeva il testo dentro `write()`: un `UnicodeEncodeError` a meta' e' arrivato
**dopo** che l'apertura aveva gia' troncato il file. Qui si compone, si codifica
in memoria, e **solo allora** si apre.
"""
import io
import json

PERCORSO = 'rinviate.jsonl'

VOCE = {
    'firma': 'a443144e74cb6ab219c57961aeee674fdb5544a1',
    'file': 'chara_func.hsp',
    'en': 'name(addbuff_charid) + " " + bufftxt(0, addbuff_buffid) + '
          '_s(addbuff_charid) + bufftxt(1, addbuff_buffid)',
    'rinviata_a': 'mai: riga dentro un blocco /* ... */ spento dal mod',
    'motivo':
        "chara_func.hsp:2310. La riga sta dentro un commento di BLOCCO — "
        "`/********** ORIGINAL - BEGINNING **********` a `:2308`, chiuso da "
        "`********** ORIGINAL - ENDING **********/` a `:2312` — cioe' la riga con "
        "cui monte annunciava l'arrivo di un buff (`name + bufftxt(0) + _s + "
        "bufftxt(1)`) prima che il mod la sostituisse. Il giocatore non la "
        "leggera' mai. E' la seconda voce del progetto in questa classe dopo "
        "`proc.hsp:11796` della 37ª, quella per cui la rete 6 e' stata allargata "
        "dai commenti `;` ai blocchi `/* ... */`. ⚠️ Trovata leggendo il "
        "`dossier.py`, che stampa due righe di contesto sopra e sotto la voce e "
        "quindi mostra il `BEGINNING`; `commenti-blocco.py` lo conferma, "
        "mettendo `:2310` fra le 46 righe spente di `chara_func.hsp`. ✅ Non "
        "c'e' toppa da fare: non e' un difetto a schermo, e' testo morto, e "
        "`misura-blocchi-spenti.py` resta a 7 proprio perche' il lotto 002 non "
        "l'ha tradotta.",
}


def riscrivi(percorso: str, righe: list) -> None:
    """Compone, codifica in memoria, e solo allora apre. Vedi il docstring."""
    testo = ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in righe)
    dati = testo.encode('utf-8')
    with io.open(percorso, 'wb') as f:
        f.write(dati)


righe = [json.loads(l) for l in io.open(PERCORSO, encoding='utf-8') if l.strip()]
if any(r.get('firma') == VOCE['firma'] for r in righe):
    raise SystemExit('la voce c\'e\' gia\': niente da fare')
righe.append(VOCE)
riscrivi(PERCORSO, righe)
print(f'{PERCORSO}: {len(righe)} rinviate')
