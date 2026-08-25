# -*- coding: utf-8 -*-
"""97a - `init.hsp:510`: riga commentata col `;`, ed e' l'«Original» soppiantato.

    507   /********** JAMES CUSTOM - ENDING **********/
    508   // Original:
    509   ; cdata(CDATA_PIC, getunid_charid) = COLOR_DEFAULT * COLOR_TINT_MULT + 1
    510   ; cdatan(CDATAN_NAME, getunid_charid) = lang("残りカス", "a garbage")

E' la **prima famiglia di riga morta** del progetto, quella della rete 6: il `;`
in testa. La riga sta sotto un `// Original:` e insieme alla sua compagna `:509`
e' il codice che il JAMES CUSTOM ha sostituito — dava il nome «a garbage» al PNG
il cui identificativo non si trova piu'.
"""
import io
import json

FILE = 'init.hsp'
RIGA, EN = 510, 'a garbage'

MOTIVO = (
    "La riga e' **commentata col `;`**, e non da sola: `init.hsp:509` e `:510` "
    "sono le due righe dell'«Original» che il tratto `JAMES CUSTOM` chiuso a "
    "`:507` ha sostituito, e `:508` lo dice per esteso (`// Original:`). Il "
    "codice vivo e' `:505`-`:506`, che al PNG senza identificativo cambia "
    "l'immagine invece del nome. "
    "⭐ E il nome che dava — «a garbage», 残りカス, «gli scarti» — non compare "
    "piu' da nessuna parte: era il segnaposto di un personaggio rotto, e adesso "
    "un personaggio rotto il nome se lo tiene. "
    "✅ Si sblocca solo se qualcuno riaccende quelle due righe."
)

voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_97-init.hsp-tutto.jsonl',
                                                 encoding='utf-8') if l.strip())}
if (RIGA, EN) not in voci:
    raise SystemExit(f'chiave che non aggancia nessuna voce: {(RIGA, EN)}')
v = voci[(RIGA, EN)]

esistenti = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
if any(json.loads(l)['firma'] == v['firma'] for l in esistenti):
    raise SystemExit('gia presente, niente da fare')

nuova = {
    'firma': v['firma'],
    'file': FILE,
    'en': v['en'],
    'rinviata_a': "mai: riga commentata col `;`, meta' dell'«Original» che il "
                  'JAMES CUSTOM ha sostituito',
    'motivo': MOTIVO,
}

# ⚠️ si compone e si codifica prima di toccare il file (la 39a)
dati = (json.dumps(nuova, ensure_ascii=False) + '\n').encode('utf-8')
with io.open('rinviate.jsonl', 'ab') as f:
    f.write(dati)
print(f'rinviata aggiunta (totale {len(esistenti) + 1})')
