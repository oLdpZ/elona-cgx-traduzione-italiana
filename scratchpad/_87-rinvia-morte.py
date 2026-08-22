# -*- coding: utf-8 -*-
"""Le quattro righe MORTE del blocco di Ajetalio: si rinviano, non si traducono.

`chat.hsp:13991` e' `// chatList 4, ...` — la voce di menu VECCHIA («Which
quests should I undertake?»), sostituita dalla viva di `:13992` («Are there
different types of Nefia?») che accende lo stesso `chatval == 4`. E
`:14036`-`:14038` sono i tre `chatMore` della risposta vecchia, commentati con
`;`: parlano di incarichi, mentre la risposta viva (`:14032`-`:14035`) parla
dei tipi di Nefia.

⚠️ Tradurle non e' gratis (76a, `chat.hsp:19327`): una voce tradotta entra in
`menu_dialogo.voci_di_menu()` e una battuta tradotta in `chat-lotto-misura`,
e quei numeri sarebbero veri su righe che non disegnano niente.

Nessuna delle quattro firme vive altrove nel file: si spengono da sole.
"""
import io
import json

RINVII = [
    ('d211c7133684408ebb6c82d471af0517329e9303', 13991,
     'Which quests should I undertake?',
     'la voce di menu vecchia'),
    ('b5df746cdc6768ac906e423b069ef18cb8fe011a', 14036,
     "At first, it's recommended to fulfill requests for items. Be sure to have the "
     "requested item handy. Once you have food and equipment and can travel between "
     "towns without difficulty, start doing delivery requests. If you fail, you'll "
     "lose karma, so check the deadline carefully.",
     'la prima battuta della risposta vecchia'),
    ('cbf33b308198ba3a6957e6b72201d8e605ec7d6d', 14037,
     'If you can handle wild animals, you can also do harvest requests. Picking crops '
     'is a good way to get stronger. If you score several times the quota you\'ll get '
     'more rewards and bronze coins, but at first it\'ll be difficult. If you\'re '
     'strong enough, you might want to take requests for killing monsters or escort '
     'requests for nearby towns.',
     'la seconda battuta della risposta vecchia'),
    ('c0863738813023b3d84292a8fc5fe05d3e31dc35', 14038,
     'Start doing party requests after getting your perform skill to at least about 5. '
     'If you perform near high-level people, you may be killed, so please be careful '
     'who you perform near to, both when practicing and during a request.',
     'la terza battuta della risposta vecchia'),
]

MOTIVO = (
    "`chat.hsp:%d` e' una riga **commentata** a monte (%s del blocco del docente "
    "Ajetalio, `*chat_unique_mizuki`): `:13991` e' `// chatList 4, ...`, "
    "`:14036`-`:14038` sono `; chatMore ...`. Monte ha cambiato la quarta voce del "
    "menu del secondo incontro — la voce viva `:13992` («Are there different types of "
    "Nefia?») accende lo stesso `chatval == 4`, e la risposta viva (`:14032`-`:14035`) "
    "parla dei tipi di Nefia — lasciando spenta la coppia domanda/risposta sugli "
    "incarichi. Non le disegna nessuno. ⚠️ **Tradurle non e' gratis** (76a, "
    "`chat.hsp:19327`): una voce tradotta entra in `menu_dialogo.voci_di_menu()` e una "
    "battuta tradotta in `chat-lotto-misura`, cioe' numeri veri su righe che non "
    "disegnano niente. Nessuna delle quattro firme vive altrove nel file. Si riaprono "
    "il giorno in cui monte togliesse il commento."
)


def main() -> int:
    righe_morte = {r for _, r, _, _ in RINVII}

    voci = [json.loads(l) for l in io.open('lavoro/_87-ajetalio.jsonl', encoding='utf-8')
            if l.strip()]
    tenute = [v for v in voci if v['riga'] not in righe_morte]
    with io.open('lavoro/_87-ajetalio.jsonl', 'w', encoding='utf-8', newline='\n') as fh:
        for v in tenute:
            fh.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('lotto: %d voci (erano %d)' % (len(tenute), len(voci)))

    gia = set()
    for l in io.open('rinviate.jsonl', encoding='utf-8'):
        if l.strip():
            gia.add(json.loads(l)['firma'])

    with io.open('rinviate.jsonl', 'a', encoding='utf-8', newline='\n') as fh:
        for firma, riga, en, che in RINVII:
            if firma in gia:
                print('gia rinviata: %d' % riga)
                continue
            fh.write(json.dumps({
                'firma': firma,
                'file': 'chat.hsp',
                'en': en,
                'rinviata_a': 'il giorno in cui monte togliesse il commento a chat.hsp:%d' % riga,
                'motivo': MOTIVO % (riga, che),
            }, ensure_ascii=False) + '\n')
            print('rinviata: %d' % riga)
    return 0


raise SystemExit(main())
