# -*- coding: utf-8 -*-
"""77a — `chat.hsp`, l'ingaggio e il reclutamento (`chatval` 50 e 51).

`:23200` («Vorrei assumerti», `:19600`) e `:23244` («Unisciti a me!», `:19601`),
due voci di menu gia' rese dalla 73a. Il parlante e' un **avventuriero estratto
a caso**: il sesso non si sa mai.

⚠️⚠️ **Quindi nessuna resa puo' dire «compagno» in prima persona.** 「君の仲間
になれと？」 sarebbe «diventare tuo compagno?», che marca chi parla; l'inglese
gira gia' la frase («You are no match for me», «What made you think I'd want to
join you?») e l'italiano la gira allo stesso modo — «Non sei alla mia altezza»,
«Vuoi che mi unisca a te?». E' la regola (2) della 75a, il PARLANTE.

⚠️ **`:23236` mette il nome a complemento oggetto**: `name()` porta l'articolo
(`contratto-nomi.md` §4), quindi «Hai ingaggiato " + name(tc)» va bene e
qualunque preposizione davanti no.

⚠️ **Le tre voci del prezzo stanno nei 24 caratteri**: `menu_dialogo.reso()`
conta **quattro cifre** per ogni valore interpolato, quindi «Request 3 days.
(9999gp)» e' esattamente 24 e la resa deve starci. «3 giorni (9999 oro)» ne fa
19; «Ingaggia per 3 giorni» sforerebbe.

⚠️ 「やめる」 resta **«Annulla»**, la sesta volta in `chat.hsp`.

    python scratchpad/lotto-77-chat-ingaggio.py
"""
import io
import json
import sys

USCITA = 'lavoro/77-chat-ingaggio.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((23200, 23243), (23244, 23273))

RESE = {
    # --- 50: l'ingaggio a giornata
    (23201, 'If you pay me in advance, I will take the job.'):
        "Se mi paghi in anticipo, accetto l'incarico.",
    (23205, 'Request 3 days. (gp)'): '"3 giorni (" + hire3 + " oro)"',
    (23208, 'Request 7 days. (gp)'):
        '"7 giorni (" + calchireadv(tc) + " oro)"',
    (23211, 'Request 30 days. (gp)'): '"30 giorni (" + hire30 + " oro)"',
    (23213, 'Some other time.'): 'Annulla',
    (23236, 'You hired .'): '"Hai ingaggiato " + name(tc) + "."',

    # --- 51: il reclutamento
    (23246, 'Huh? You are no match for me.'): 'Eh? Non sei alla mia altezza.',
    (23250, 'Sure, I guess you and I can make a good team.'):
        'Ma sì, credo che insieme faremmo una bella squadra.',
    (23253, "It seems your party is already full. Come see me again when you're ready."):
        ('Sembra che il tuo gruppo sia al completo. Torna a cercarmi quando '
         'avrai fatto spazio.'),
    (23266, "Huh? What made you think I'd want to join you? I have no complaints about your capabilities.. but I don't know you well enough. Maybe hire me for some simple jobs first."):
        ('Eh? Vuoi che mi unisca a te? Sulle tue capacità non ho niente da dire... '
         'ma non ti conosco abbastanza. Prima ingaggiami per qualche lavoretto.'),
    (23270, "I-I don't feel like I want to... sorry."):
        'N-non me la sento... scusa.',
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
