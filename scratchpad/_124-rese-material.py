# -*- coding: utf-8 -*-
"""124a - Le 17 rese di `material.hsp`, il pannello della produzione.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_124-rese-material.py

Scrive `lavoro/fase6-material-001.jsonl` a partire dal lotto estratto in
`scratchpad/_124-material.jsonl`.

⚠️ Il file era fra gli **undici senza dizionario** della 123a: nessun contatore
per-file lo mostrava, e `_97-quanto-resta` non lo elencava nemmeno come riga.

⚠️⚠️ **DUE RIGHE VANNO PENSATE INSIEME.** `:160` compone la frase e `:162` la
stampa aggiungendo il resto: sono l'unica coppia del lotto, e l'inglese le
chiude tutt'e due con un punto («N X was consumed.» + « (12 remaining.)»).
In italiano la prima resta **senza punteggiatura finale** e la seconda chiude
la frase, perche' `locvar_matgetmain_s` non e' mai stampata da sola.

⭐ La forma del contatore e' **la parentesi**, gia' decisa in `glossario.md` e
gia' in gioco sulla riga gemella `:120` (la toppa della 123a): «Materiale
ricevuto: pietruzza (3)». Qui il verbo cambia — l'inglese dice «consumed», il
giapponese 失った — e i due soli chiamanti di `matdelmain` spendono davvero il
materiale (l'inchiostro magico di `action.hsp:12358`, la gettone della macchina
di `command.hsp:17478`): «Materiale consumato».

⭐ I quattro nomi di abilita' NON si decidono qui: sono quelli di `skill.hsp`,
gia' resi — Alchimia, Falegnameria, Oreficeria, Sartoria — e li conferma
`action.hsp:7230`-`:7272` («Ottiene bonus in ...»).

⚠️ ` x ` resta identico all'inglese e va dichiarato in `invariati.md`.
"""
import io
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
DENTRO = os.path.join(QUI, '_124-material.jsonl')
FUORI = os.path.join(RADICE, 'lavoro', 'fase6-material-001.jsonl')

# riga -> resa. Per le dinamiche la resa e' l'ESPRESSIONE HSP intera, che
# sostituisce `en_grezzo`; per le statiche e' il testo nudo.
RESE = {
    160: '"Materiale consumato: " + matname(matdelmain_arg1)'
         ' + " (" + locvar_matgetmain_n + ")"',
    162: 'locvar_matgetmain_s + ", ne restano " + mat(matdelmain_arg1) + ". "',
    219: 'Produzione',
    221: 'Prodotto',
    222: 'Descrizione',
    223: 'Requisiti',
    224: 'Materiali necessari',
    253: 'Abilità richiesta: ',
    255: 'Alchimia',
    258: 'Falegnameria',
    261: 'Oreficeria',
    264: 'Sartoria',
    281: ' x ',
    298: '"Crea [" + s + "]"',
    340: 'Non hai i requisiti per fabbricare l\'oggetto.',
    369: '"Hai fabbricato " + itemname(ci, 1) + "."',
    433: 'Nome',
}


def main():
    voci = [json.loads(l) for l in io.open(DENTRO, encoding='utf-8')]
    assert len(voci) == len(RESE), (len(voci), len(RESE))
    for v in voci:
        assert v['riga'] in RESE, v['riga']
        v['it'] = RESE[v['riga']]
    with io.open(FUORI, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%d rese in %s' % (len(voci), FUORI))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
