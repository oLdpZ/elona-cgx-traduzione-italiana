# -*- coding: utf-8 -*-
"""Aggiunge a rinviate.jsonl la voce di proc.hsp:4958, che sta su riga commentata."""
import io, json

MOTIVO = (
    "Riga COMMENTATA nel sorgente. `estrai.py` non salta i commenti HSP "
    "(scoperta 1 della 27ª: 28 voci su 27.813 stanno su righe che cominciano "
    "per `;`), e questa e' l'unica in tutto `proc.hsp` — misurato sull'intera "
    "estrazione, non dedotto. Il blocco `JAMES CUSTOM - MANUSCRIPT HINT` "
    "(`proc.hsp:4950-4962`) e' spento per intero: il contatore "
    "`GDATA_FLAG_MANUSCRIPT_IDEAS` non viene mai incrementato e il messaggio "
    "non esce mai. Renderla non farebbe danno, ma direbbe il falso a chi legge "
    "il conteggio delle non tradotte. ⚠️ E il giapponese qui non aiuta: "
    "「いいアイデアだ！」 e' «Ottima idea!» (gia' reso cosi' in "
    "`action.hsp:6648`), mentre l'inglese ci ha scritto una frase intera sul "
    "viaggio e sul libro — due testi diversi sotto la stessa `lang()`. "
    "Da riprendere se e quando il blocco venisse riacceso."
)

NUOVE = [(4958, 'While travelling, you accumulated some ideas for writing a book. ')]

voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_proc.jsonl', encoding='utf-8') if l.strip())}

righe = []
for k in NUOVE:
    if k not in voci:
        raise SystemExit(f'chiave che non aggancia nessuna voce: {k}')
    v = voci[k]
    righe.append({
        'firma': v['firma'],
        'file': 'proc.hsp',
        'en': v['en'],
        'rinviata_a': 'se il blocco MANUSCRIPT HINT viene riacceso',
        'motivo': MOTIVO,
    })

esistenti = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
firme = {json.loads(l)['firma'] for l in esistenti}
nuove = [r for r in righe if r['firma'] not in firme]
if not nuove:
    print('gia presenti, niente da fare')
else:
    with io.open('rinviate.jsonl', 'a', encoding='utf-8', newline='\n') as f:
        for r in nuove:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(f'{len(nuove)} rinviate aggiunte (totale {len(esistenti) + len(nuove)})')
