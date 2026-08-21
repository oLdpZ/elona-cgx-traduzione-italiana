# -*- coding: utf-8 -*-
"""77a — `chat.hsp`, il nome della casa (`chatval` 45, `:22496`).

La voce «Un nome per la casa» (`:19617`, resa dalla 73a) fa comporre a un PNG il
nome della tua casa: `random_title()` tira un epiteto e il codice ci **appende**
uno degli undici suffissi di `:22498`.

⭐⭐⭐ **In italiano il suffisso non puo' stare in coda, e la soluzione non e'
una resa: e' l'ORDINE.** L'epiteto italiano e' gia' un sintagma intero —
«fragore della dipendenza», «luce della maga», «spettro d'argento» (64a) — e
«fragore della dipendenza casa» non e' italiano. Il giapponese, che dice
「<epiteto>の家」, ha la **stessa struttura dell'italiano**: «casa DI <epiteto>».
Quindi la toppa gira la concatenazione nel solo ramo inglese

    mdatan(MDATAN_NAME) = lang(mdatan + s(rnd(10)), s(rnd(10)) + " " + mdatan)

e gli undici suffissi diventano **prefissi che finiscono in «di»**: «Casa di
fragore della dipendenza». ⚠️ E «di» e' la sola preposizione che regge: qualunque
articolo — «Casa DEL fragore», «Casa DELLA luce» — si accorderebbe col primo
nome dell'epiteto, che cambia a ogni tiro. E' la 64a applicata alla
preposizione: *esiste una costruzione italiana che non chiede accordo?*

⚠️ **La riga e' toppabile perche' il dizionario non la riscrive**: la sua unica
`lang("", " ")` non viene estratta (giapponese vuoto), quindi sorgente pinnato e
build coincidono ed e' quel che `test_toppe` pretende (53a).

⚠️⚠️ **Gli undici suffissi seguono il GIAPPONESE.** Monte non li ha tradotti,
li ha **riscritti**: 城 (*castello*) e' diventato «Shack», ハウス (*house*)
«Hideout», ドーム (*cupola*) «Shed». Escono a sorte, quindi a schermo l'ordine
non si vede, ma la colonna che si legge accanto alla resa nel dizionario e' il
giapponese (57a, caso 2).

💡 **E l'undicesimo non esce mai**: `s` ha undici elementi e il tiro e'
`rnd(10)`, cioe' 0-9. 「ドーム」 e' codice morto di monte. Qui tradurlo non costa
niente — non e' una voce di menu e nessuna rete lo misura (al contrario delle due
righe commentate della 76a).

    python scratchpad/lotto-77-chat-casa.py
"""
import io
import json
import sys

USCITA = 'lavoro/77-chat-casa.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((22496, 22506),)

RESE = {
    # --- gli undici suffissi, che la toppa trasforma in prefissi
    (22498, 'Home'): 'Casa di',
    (22498, 'Mansion'): 'Residenza di',
    (22498, 'Shack'): 'Castello di',
    (22498, 'Nest'): 'Harem di',
    (22498, 'Base'): 'Covo di',
    (22498, 'Hideout'): 'Villa di',
    (22498, 'Dome'): 'Focolare di',
    (22498, 'Hut'): 'Tana di',
    (22498, 'Cabin'): 'Abitazione di',
    (22498, 'Hovel'): 'Rifugio di',
    (22498, 'Shed'): 'Cupola di',

    # --- e la battuta che annuncia il nome
    (22504, 'Hey, I\'ve come up with a good idea! \\"\\", doesn\'t it sound charming?'):
        ('"Ecco, mi è venuta un\'idea! D\'ora in poi questa casa si chiama'
         ' \\"" + mdatan(MDATAN_NAME) + "\\". Non suona bene?"'),
}


def main() -> int:
    voci = []
    for l in io.open(RESTANTE, encoding='utf-8'):
        v = json.loads(l)
        if any(a <= v['riga'] <= b for a, b in ZONE):
            voci.append(v)

    errori = []
    viste = set()
    for v in voci:
        k = (v['riga'], v['en'])
        if k not in RESE:
            errori.append('%d: voce senza resa | %r' % (v['riga'], v['en'][:80]))
            continue
        viste.add(k)
        v['it'] = RESE[k]
    for k in sorted(set(RESE) - viste):
        errori.append('%d: resa senza voce nel lotto | %r' % (k[0], k[1][:80]))
    if errori:
        for e in errori:
            print(e)
        return 1

    with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%s: %d voci' % (USCITA, len(voci)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
