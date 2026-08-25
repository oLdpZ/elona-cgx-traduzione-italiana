# -*- coding: utf-8 -*-
"""Toglie dal dizionario `command.hsp:17515`, che sta dietro un `//`.

E' l'unica voce **gia' tradotta** che il referto del commento `//` ha trovato
(`scratchpad/_100-commento-barre.py`, 1 su 9): lavoro speso su testo che il
giocatore non legge. ⚠️ Si toglie solo perche' la **firma vive li' e basta** —
la lezione della 45a e' che `estrai --da-tradurre` ancora una voce alla prima
occorrenza, e una firma spenta in un punto puo' vivere in un altro. Qui no:
`estrai` la trova a `:17515` e in nessun altro posto.
"""
import io
import json

FIRMA = "7b82abe9b863246a63176239bb98443c8fe7c4b4"
MOTIVO = (
    "La riga e' spenta da un commento di riga `//` — `// \\ttxt lang(\"デバッグ"
    "モードでは無効だ。\", \"This function is disabled in wizard mode.\")` — e la "
    "firma non vive in nessun altro punto del sorgente. E' la QUINTA famiglia di "
    "riga morta, trovata nella 100a: HSP3 ha due commenti di riga, `;` e `//`, e il "
    "progetto ne guardava uno solo. Questa resa e' l'unica gia' scritta fra le nove "
    "righe che il referto ha trovato, cioe' l'unico lavoro davvero sprecato: era in "
    "dizionario dalla sessione che ha chiuso `command.hsp`, e nessuna rete poteva "
    "dirlo. Tolta dal dizionario perche' resti misurabile lo zero: se un giorno il "
    "referto torna a dire «gia' rese: 1», e' un lotto nuovo che ha sbagliato, non "
    "questa."
)

voci = [json.loads(r) for r in io.open('dizionario/command.hsp.jsonl', encoding='utf-8')
        if r.strip()]
uscita = [v for v in voci if v['firma'] != FIRMA]
tolte = [v for v in voci if v['firma'] == FIRMA]
if len(tolte) != 1:
    raise SystemExit(f'attesa una voce con quella firma, trovate {len(tolte)}')

with io.open('dizionario/command.hsp.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for v in uscita:
        f.write(json.dumps(v, ensure_ascii=False) + '\n')

esistenti = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
firme = {json.loads(l)['firma'] for l in esistenti}
if FIRMA in firme:
    print('rinvio gia presente')
else:
    with io.open('rinviate.jsonl', 'a', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps({
            'firma': FIRMA,
            'file': 'command.hsp',
            'en': tolte[0]['en'],
            'rinviata_a': 'mai: riga spenta da un commento di riga `//`',
            'motivo': MOTIVO,
        }, ensure_ascii=False) + '\n')
    print(f'rinvio aggiunto (totale {len(esistenti) + 1})')
print(f"dizionario command.hsp: {len(voci)} -> {len(uscita)} voci")
