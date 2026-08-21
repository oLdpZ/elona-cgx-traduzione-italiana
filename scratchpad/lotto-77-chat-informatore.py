# -*- coding: utf-8 -*-
"""77a — `chat.hsp`, l'informatore: la lista, il messaggio e il compleanno.

Tre `chatval` dello stesso parlante, tutt'e tre voci di menu gia' rese dalla
73a: 18 («Avventurieri (100 oro)», `:20525`), 105 («Messaggio (2000 oro)»,
`:22961`) e 82 («[Dire il compleanno]», `:19576` -> `:22972`).

⚠️⚠️ **Il compleanno e' una schermata a tre finestre**, e le due domande stanno
in mezzo a un `prompt_word`: si conferma (`:22974`), si batte il mese
(`:22981`), si batte il giorno (`:22995`), si rilegge la data (`:23010`) e si
conferma di nuovo (`:23011`). Vanno tradotte tutte insieme o la sequenza esce
meta' e meta'.

⚠️ **`:22974` non puo' dire «sicuro?»**: e' rivolto al giocatore e l'aggettivo
si accorda. «Poi non si potra' piu' cambiare, va bene?» non accorda niente — e'
la regola (1) della 75a.

⚠️ **`:23011` regge perche' il passato prossimo e' con AVERE**: «Ho sbagliato»
sta in piedi per tutt'e due i sessi, come `:23892` nella 76a.

💡 **La data si scrive all'italiana**: monte stampa 「M月D日」 e «M / D», noi
«il D/M». L'ordine si puo' cambiare perche' l'espressione la scriviamo intera, e
le funzioni di contenuto restano le stesse due `gdata()` — la rete 11 confronta
l'insieme, non la posizione (40a).

💡 **E `:23010` si riprende la domanda che l'inglese ha buttato via**: il
giapponese chiude con 「間違いない**か**」 e sotto ci sono due bottoni, «Ho
sbagliato» e «Si'». Quel che ha solo il giapponese e' permesso.

⚠️ 「やめる」 resta **«Annulla»** (`:22975`), come nelle altre cinque volte in
`chat.hsp`, e 「間違いない」 «Si'» come a `:2630`, `:6276` e `:22025`: due
schermate che mostrano la stessa scelta dicono le stesse parole (73a).

💡 **Deroga dichiarata, due volte: «avventuriero» al maschile generico**
(`:20531`, `:22966`). Non e' un referente di sesso ignoto ma una **categoria**
nominata prima che la scelta esista — l'elenco degli avventurieri si apre dopo —
e in italiano la categoria si dice al maschile. Il divieto della 75a vale su chi
parla, su chi ascolta e sull'oggetto: qui non c'e' ancora nessuno.

    python scratchpad/lotto-77-chat-informatore.py
"""
import io
import json
import sys

USCITA = 'lavoro/77-chat-informatore.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((20525, 20535), (22961, 22971), (22972, 23035))

MESE = 'gdata(GDATA_FLAG_INFORMER_BIRTHDAY_MONTH)'
GIORNO = 'gdata(GDATA_FLAG_INFORMER_BIRTHDAY_DAY)'

RESE = {
    # --- 18: la lista degli avventurieri
    (20531, 'If you select an adventurer, you can see the details.'):
        'Se scegli un avventuriero, ne vedi la scheda.',

    # --- 105: il messaggio agli altri avventurieri
    (22966, 'Which adventurer should I tell?'):
        'A quale avventuriero devo riferirlo?',

    # --- 82: il compleanno
    (22974, "It can't be changed later. OK?"):
        'Poi non si potrà più cambiare, va bene?',
    (22975, 'Wait...'): 'Annulla',
    (22976, 'OK!'): 'Te lo dico',
    (22981, 'Which month?'): 'Che mese?',
    (22995, 'And which day?'): 'E che giorno?',
    (23010, 'Your birthday is  / .'):
        '"Il tuo compleanno è il " + ' + GIORNO + ' + "/" + ' + MESE
        + ' + ". Giusto?"',
    (23011, 'I made a mistake.'): 'Ho sbagliato',
    (23012, 'Yes.'): 'Sì',
    (23017, "I see! I'll also tell everyone!"):
        'Ottimo! Lo dirò anche a tutti gli altri!',
    (23032, 'I already know it. Your birthday is  / .'):
        '"Lo so già: il tuo compleanno è il " + ' + GIORNO + ' + "/" + ' + MESE
        + ' + "."',
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
