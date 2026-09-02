# -*- coding: utf-8 -*-
"""Cinque toppe della 126a portano nell'italiano il carattere `…`, che a
schermo non e' tre punti.

`…` (U+2026) esiste in CP932 — e' 0x81 0x63 — quindi
`test_nessuna_toppa_porta_testo_che_cp932_non_sa_scrivere` lo lascia passare:
quella rete chiede che il carattere sia SCRIVIBILE, non che sia leggibile. Ma
e' un carattere a **doppia larghezza**, e il ramo che la build italiana esegue
disegna col carattere latino di `config.txt` (`font2. "Courier New"`): i due
byte diventano due glifi latini a caso, esattamente come `invariati.md` spiega
per 《 》 e 【 】.

⚠️⚠️ **E il progetto lo sapeva gia'.** `scratchpad/guardie.py` ha `…` in cima
all'elenco `PROIBITI` dalla 33a — ma `guardie.py` legge i **JSONL di lotto**,
cioe' il dizionario. Le toppe non le guarda nessuno: e' la scoperta della 126a
(«le toppe erano l'unico italiano che nessuna rete avesse mai letto») che
colpisce di nuovo, nello stesso giorno in cui erano nati i due referti sulle
toppe — che pero' cercavano participi ed elisioni, non caratteri.

Le cinque righe sono tutte del lotto di `proc.hsp` della 126a, le battute delle
mosse speciali.

⚠️ **Non si tocca il `…` giapponese.** Cinque toppe a blocco portano nel
`cerca` e nel `sostituisci` anche il ramo `if ( jp )`, dove
「くやしい、でも…」 e 「疲れた…」 sono scritte giuste: li' il carattere e'
a doppia larghezza in una riga a doppia larghezza, ed e' quel che il giapponese
vuole. Il filtro guarda **riga per riga** e salta quelle che contengono kana o
kanji.
"""
import io
import json

GIAPPONESE = (('぀', 'ヿ'), ('一', '鿿'))


def ha_giapponese(riga: str) -> bool:
    return any(a <= c <= b for c in riga for a, b in GIAPPONESE)


def correggi(valore):
    """Sostituisce `…` con `...` nelle sole righe senza giapponese."""
    if isinstance(valore, list):
        return [correggi(r) for r in valore]
    if ha_giapponese(valore):
        return valore
    return valore.replace('…', '...')


toppe = [json.loads(r) for r in io.open('toppe.jsonl', encoding='utf-8') if r.strip()]

toccate = 0
for t in toppe:
    for chiave in ('cerca', 'sostituisci'):
        nuovo = correggi(t[chiave])
        if nuovo != t[chiave]:
            # ⚠️ `cerca` deve restare agganciato al SORGENTE: se una correzione
            #    finisse li' dentro, la toppa smetterebbe di trovare la riga.
            if chiave == 'cerca':
                raise SystemExit(
                    'una correzione tocca il `cerca` della toppa {!r}: il `cerca` '
                    'e\' il sorgente inglese e non si corregge.'.format(t['motivo'][:60]))
            t[chiave] = nuovo
            toccate += 1

if toccate != 5:
    raise SystemExit('attese 5 righe da correggere, toccate {}'.format(toccate))

restanti = [t for t in toppe
            for r in (t['sostituisci'] if isinstance(t['sostituisci'], list) else [t['sostituisci']])
            if '…' in r and not ha_giapponese(r)]
if restanti:
    raise SystemExit('ne restano {}'.format(len(restanti)))

# ⚠️ si compone e si valida PRIMA di aprire il file (regola della 39a)
dati = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in toppe).encode('utf-8')
with io.open('toppe.jsonl', 'wb') as f:
    f.write(dati)
print('{} sostituzioni in {} toppe riscritte'.format(toccate, len(toppe)))
