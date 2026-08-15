# -*- coding: utf-8 -*-
"""Aggiunge a rinviate.jsonl le due voci commentate del menu di `*com_chara`."""
import io
import json

MOTIVO_6070 = (
    "La riga e' commentata col `;`, e con lei le due che la circondano: "
    "`command.hsp:6069`-`:6071` sono `; if ( cdata(CDATA_MARK_ITEM_PIC, tc) > 0 "
    "{`, `; \tpromptAdd lang(\"アイテム画像の調整\", \"Item mark adjust\"), \"null\", "
    "26` e `; }`. Il comando che regolava l'icona appiccicata al compagno e' "
    "stato spento dal mod, mentre i tre fratelli restano vivi e sono resi: "
    "`:6068` «Assegna un'icona», `:6073` «Sposta l'icona», `:6076` «Togli "
    "l'icona». ⚠️ **L'ha trovata la rete 6, non l'occhio**: tre righe spente in "
    "mezzo a quattro vive, con lo stesso rientro delle altre, e leggendo il "
    "sorgente per scrivere il lotto non l'avevo vista."
)

MOTIVO_6148 = (
    "La riga e' commentata col `;`: `command.hsp:6148` e' "
    "`; promptAdd lang(\"カスタムＡＩ\", \"Custom AI\"), \"null\", 998`, dentro il "
    "ramo `if ( develop | gdata(GDATA_WIZARD) )` che gia' da solo mostra le sue "
    "voci ai soli sviluppatori. La voce sorella `:6147` «Informazioni» resta "
    "viva ed e' resa. Il giocatore non leggera' mai «Custom AI»: non e' "
    "nascosta dietro una condizione, e' proprio fuori dal programma."
)

NUOVE = [
    (6070, 'Item mark adjust', MOTIVO_6070),
    (6148, 'Custom AI', MOTIVO_6148),
]

voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_command.jsonl', encoding='utf-8')
                  if l.strip())}

righe = []
for riga, en, motivo in NUOVE:
    if (riga, en) not in voci:
        raise SystemExit(f'chiave che non aggancia nessuna voce: {(riga, en)}')
    v = voci[(riga, en)]
    righe.append({
        'firma': v['firma'],
        'file': 'command.hsp',
        'en': v['en'],
        'rinviata_a': 'mai: riga commentata col `;` nel sorgente',
        'motivo': motivo,
    })

esistenti = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
firme = {json.loads(l)['firma'] for l in esistenti}
nuove = [r for r in righe if r['firma'] not in firme]
if not nuove:
    print('gia presenti, niente da fare')
else:
    # ⚠️ si compone e si codifica prima di toccare il file (la 39a)
    dati = ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in nuove).encode('utf-8')
    with io.open('rinviate.jsonl', 'ab') as f:
        f.write(dati)
    print(f'{len(nuove)} rinviate aggiunte (totale {len(esistenti) + len(nuove)})')
