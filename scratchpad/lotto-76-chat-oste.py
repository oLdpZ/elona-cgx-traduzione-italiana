# -*- coding: utf-8 -*-
"""76a — `chat.hsp`, l'oste: pasto, bevanda, piatto e bevanda speciali, kiseru.

`chatval` 13 (da mangiare), 83 (piatto speciale, 1 bronzo), 93 (da bere),
112 (bevanda speciale, 1 bronzo), 86 (il kiseru). Sono cinque voci del menu di
`*chat_default` gia' tradotte dalla 73a — «Ordinare da mangiare», «Piatto
speciale (1 bronzo)», «Ordinare da bere», «Bevanda speciale (1 bronzo)»,
«Vorrei un kiseru» — e finora il giocatore le sceglieva in italiano e riceveva
inglese.

⭐⭐ **DEROGA DICHIARATA a `:19984`: l'inglese appiattisce due gradini di una
scala, il giapponese no.** Le tre esclamazioni del **piatto speciale** sono
「すごく美味しい！」「これは凄くいける！」「とてもいい味だ！」 — tutt'e tre col
superlativo — ma l'inglese ci ha messo esattamente le stesse tre frasi del cibo
normale, gia' rese in `event.hsp:779` e `item.hsp:3359` («Questo si' che si
mangia!», «Che bel sapore!», «Delizioso!»/«Che bonta'!»). Renderle uguali
farebbe dire la stessa cosa al pasto da poche monete e al piatto pagato con un
**bronzo**, che nella stessa taverna e' la scelta accanto. Quindi il piatto
speciale prende forme piu' forti. E' la deroga (2) della 74a (la colazione), e
il progetto l'ha gia' fatta da se': lo stesso «Delicious!» e' «Che bonta'!» a
`item.hsp:3304` e «Delizioso!» a `:3359`, perche' li' il giapponese differisce.

⚠️ **`:19990` e `:20093` sono quasi gemelle di `command.hsp:4294`** — stesso
giapponese 「冷やかし」+`_ka(1)`, stesso inglese «You kidding?», gia' reso «Mi
stai prendendo in giro?». Stesse parole. (Le due qui hanno firme diverse fra
loro solo per uno **spazio in coda** nell'inglese di `:20093`.)

⚠️ **`:20442` e' quasi gemella di `event.hsp:933`**: stesso giapponese
「いらない」, inglese diverso («I'll pass.» contro «I don't need it.»), gia' reso
«Non mi serve!». Si dicono le stesse parole.

⭐ **`:20042` rimette quel che l'inglese ha buttato via** (regola della 72a: quel
che ha solo il giapponese e' PERMESSO). 「…お待たせした。本日のスペシャルメニュー
だ。」 dice *che cosa* sta servendo; l'inglese e' un «Here you are...» nudo,
identico a quello del pasto normale a `:19936`. La resa tiene la giuntura.

⚠️ **Il genere non si tocca in tre punti.** (1) `:20451` l'oste da' del
mascalzone **al giocatore**: «canaglia» e' un nome femminile che vale per
chiunque, quindi non accorda (regola (1) della 75a, il nome predicativo).
(2) `:20037` il **parlante** e' l'oste, che puo' essere uomo o donna: «felice»
e' un aggettivo in -e, invariabile. (3) `:20084` e `:19984` reagiscono a un
piatto o a una bevanda che nessun `itemname()` nomina: le rese girano su nomi
nostri («che roba», «che squisitezza», «che sapore»), non su aggettivi.

💡 `:20087` riusa il verbo con cui il progetto ha gia' reso 染み渡る in
`action.hsp:8359` («Mi si diffonde fin dentro al cervello!»).

    python scratchpad/lotto-76-chat-oste.py
"""
import io
import json
import sys

USCITA = 'lavoro/76-chat-oste.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((19923, 20095), (20435, 20456))

RESE = {
    # --- 13: ordinare da mangiare
    (19929, "You don't seem that hungry."): 'Non mi sembra che tu abbia fame.',
    (19936, 'Here you are.'): 'Ecco qua.',

    # --- 83: il piatto speciale (1 bronzo) — vedi la deroga nella docstring
    (19984, 'Delicious!'): 'Che squisitezza!',
    (19984, 'Gee what a good taste!'): 'Questa sì che è cucina!',
    (19984, 'It tasted pretty good!'): 'Che sapore meraviglioso!',
    (19990, 'You kidding?'): 'Mi stai prendendo in giro?',

    # --- 93: ordinare da bere
    (20000, "You don't seem that thirsty."): 'Non mi sembra che tu abbia sete.',

    # --- 112: la bevanda speciale (1 bronzo)
    (20037, "I'm happy to be able to serve you. Please wait for a moment."):
        'Sono felice di poterti servire. Solo un momento.',
    (20040, 'Drink all at once'): "Bere tutto d'un fiato",
    (20041, 'Taste slowly'): 'Assaporare con calma',
    (20042, 'Here you are...'): 'Ecco qua... la specialità del giorno.',
    (20084, 'Delicious...!!!'): 'Aaah... che roba!!!',
    (20087, 'It feels like my thirsty heart and throat are moisturized...'):
        'Mi si diffonde nel cuore e nella gola riarsi...',
    # ⚠️ lo spazio in coda e' quello dell'inglese: `verifica` lo pretende
    (20093, 'You kidding? '): 'Mi stai prendendo in giro? ',

    # --- 86: il kiseru
    (20438, 'Our kiseru is special made. Price is  gold.'):
        '"Il nostro kiseru è fatto su misura. Costa " + value + " monete d\'oro."',
    (20440, 'I want it...'): 'Lo voglio...',
    (20442, "I'll pass."): 'Non mi serve',
    (20451, "Quite the bad egg, aren't you?"): 'Anche tu sei una bella canaglia, eh?',
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
