# -*- coding: utf-8 -*-
"""Il nono lotto della 127a: due righe, e la prima e' un difetto mio di oggi.

    event.hsp:4560    la gemella esatta di command.hsp:15556, toppata stamattina
    module.hsp:2381   il contatore dei colpi incatenati, sulla mappa
"""
import io
import json

from strumenti.accenti import degrada

BASE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'

NUDO = ("LETTERALE INGLESE NUDO: non passa da nessuna lang(), quindi non ha firma "
        "ne' voce di dizionario e nessun lotto puo' raggiungerlo (quinto punto "
        "cieco, nudi_en.py, 49a). ")

LAVORO = [
    ('event.hsp', 4560, 'txt "HAI EVASO LE TASSE."',
     NUDO + "event.hsp:*event_income, la sfida «Tasse doppie ogni mese» che "
     "fallisce perche' le fatture non pagate si sono accumulate "
     "(`GDATA_BILL > 1`). ⚠️⚠️ E' LA GEMELLA ESATTA DI command.hsp:15556, "
     "toppata OGGI STESSO in questa sessione: stessa stringa, stessa sfida, "
     "stesso `TweakData(...) = (-1)`, due modi diversi di fallirla — pagare "
     "una fattura a zero, o lasciarne accumulare piu' d'una. ⚠️ E' la quarta "
     "famiglia toppata a meta' della 127a, e l'unica di cui la meta' mancante "
     "l'ho lasciata IO poche ore prima: il difetto non e' delle sessioni "
     "vecchie, e' della forma di lavoro. La cura e' cercare la stringa in "
     "tutto il sorgente prima di chiudere una toppa, non dopo. "
     "ⓘ «COMMITED» e' un refuso di monte, e la resa e' identica all'altra "
     "perche' la stringa e' identica."),
    ('module.hsp', 2381,
     'bmes " " + cdata(CDATA_CHAIN_ATTACK_COUNT, cell_draw_arg_c) + " colpi!", 235, 185, 35',
     NUDO + "module.hsp:*cell_draw_chara_detail_info, il contatore giallo che "
     "compare SULLA MAPPA sopra un personaggio quando incatena dieci colpi o "
     "piu'. ⚠️ Il progetto non ha un nome per questa meccanica: `CHAIN_ATTACK` "
     "non compare in nessuna `lang()`, e 連携 in dizionario vuol dire il "
     "coordinarsi dei compagni, che e' un'altra cosa. Non c'e' niente da "
     "riscuotere, quindi la resa e' una decisione: «colpi», che dice il "
     "numero e non chiede una parola che il gioco non ha mai insegnato. "
     "ⓘ Un carattere piu' dell'inglese («12Chain!» -> «12 colpi!»), su un "
     "glifo che galleggia sopra una casella e non dentro una colonna."),
]

toppe = []
for nome, n, nuova_grezza, motivo in LAVORO:
    righe = io.open(BASE + '\\' + nome, encoding='cp932').read().split('\n')
    originale = righe[n - 1]
    indent = originale[:len(originale) - len(originale.lstrip())]
    nuova = indent + degrada(nuova_grezza)
    for c in nuova:
        if c != '\u266a':
            assert len(c.encode('cp932')) == 1, (nome, n, c)
    assert nuova != originale
    quante = sum(1 for r in righe if r == originale)
    assert quante == 1, (nome, n, quante)
    toppe.append({'file': nome, 'cerca': originale, 'sostituisci': nuova,
                  'motivo': motivo})
    print('{:12s}{:6d}  {}'.format(nome, n, nuova.strip()[:70]))

dati = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in toppe).encode('utf-8')
with io.open('lavoro/toppe-127-gemelle.jsonl', 'wb') as f:
    f.write(dati)
print('{} toppe -> lavoro/toppe-127-gemelle.jsonl'.format(len(toppe)))
