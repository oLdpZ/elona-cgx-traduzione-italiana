# -*- coding: utf-8 -*-
"""Le toppe delle righe miste: un nudo inglese accanto a una `lang()`.

Le trova `scratchpad/nudi_accanto_a_lang.py`, il dodicesimo punto cieco (61a).
Tutte e nove portano anche una `lang()` sulla stessa riga, quindi vanno
dichiarate **`prima`**: girano sull'albero appena copiato, il loro `cerca` resta
la riga del sorgente pinnato e le `lang()` arrivano intatte al dizionario.
`applica.carica_toppe` verifica che nessuna di loro tocchi il contenuto di una
`lang()` — se lo facesse, quel sito diventerebbe orfano.

⚠️ Si compone tutto in memoria e si scrive alla fine: regola della 39a.

## Le rese, e da dove vengono

    Pag.        «Page.», gia' toppato tre volte in module.hsp
    oro         « gp» e « GP», gia' toppati in command.hsp e screen.hsp
    HP          maiuscolo: 15 volte nel dizionario, «PS» zero
    Lv          resta: 51 volte nel dizionario — solo «Exp» diventa «Esp»
    Esp         da text.hsp:1646, «Esp. Trattativa+»

⚠️ **«Incapacitated» non diventa un participio.** L'etichetta sta sopra una
creatura di cui non si conosce il genere, e `guida-stile.md` vieta il participio
riferito a chi non ha genere noto: «Fuori combattimento» non ne ha bisogno.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'

# file, riga, [(nudo inglese, resa)], motivo
CASI = [
    ('blend.hsp', 404, [('"Page."', '"Pag."')],
     "Il numero di pagina della finestra delle ricette. «Page.» e' gia' stato reso "
     "«Pag.» tre volte in module.hsp: questa e' la quarta occorrenza, e nessuno la "
     "vedeva perche' sta accanto a una lang()."),
    ('command.hsp', 135, [('"Tranquilizer taking effect: "', '"Tranquillante: "')],
     "L'etichetta che il gioco scrive sopra la creatura puntata quando il "
     "tranquillante e' attivo (CDATA_INCAPACITATED > 0). E' un bmes sulla mappa, "
     "senza riquadro: non ha tetto. Il conteggio dei turni accanto lo rende gia' la "
     "lang() della stessa riga."),
    ('command.hsp', 142, [('"Incapacitated: "', '"Fuori combattimento: "')],
     "La stessa etichetta col valore negativo, cioe' la creatura che non puo' agire. "
     "⚠️ Non «Incapacitato»: e' un participio, e sopra la testa di una creatura di "
     "cui non si conosce il genere guida-stile.md lo vieta. «Fuori combattimento» "
     "dice la stessa cosa e non ha genere."),
    ('command.hsp', 1379, [('"(Hp: "', '"(HP: "')],
     "La percentuale di salute nell'elenco degli alleati in attesa. Il progetto "
     "scrive HP maiuscolo (15 volte nel dizionario, «PS» zero): qui upstream aveva "
     "scritto «Hp»."),
    ('command.hsp', 7615, [('"* [Eq-Lvl] "', '"* [Liv-eq] "')],
     "Il suggerimento in fondo all'elenco dei PNG personalizzati: dice che il tasto "
     "mostra il livello dell'equipaggiamento. Un carattere piu' corto dell'inglese, "
     "quindi la riga dei suggerimenti non si allarga."),
    ('command.hsp', 16349, [('" Exp:"', '" Esp:"')],
     "L'arma vivente nell'elenco degli oggetti: «It is alive. [Lv:3 Exp:40%]». «Lv» "
     "resta — il progetto lo scrive cosi' 51 volte — e cambia solo «Exp», che in "
     "italiano e' «Esp» (text.hsp:1646)."),
    ('command.hsp', 17849, [('" gold  \\n"', '" oro  \\n"')],
     "La paga di un impiegato nella scheda del negozio. I due spazi prima del ritorno "
     "a capo allineano la colonna sotto e restano dove sono; cambia solo la parola, "
     "«gold» -> «oro», come nelle altre sette toppe che l'hanno gia' resa."),
    ('economy.hsp', 778, [('"k gp"', '"k oro"')],
     "Il bilancio della citta', scritto in migliaia. La «k» e' il moltiplicatore e "
     "resta; «gp» diventa «oro» come ovunque."),
    ('map_user.hsp', 445, [('" GP)"', '" oro)"')],
     "Il prezzo dell'ampliamento del negozio, nel menu di casa: «Ingrandisci (12000 "
     "GP)». ⚠️ E' la riga che la 60a ha lasciato aperta al punto 2 — larghezze.py "
     "misura la lang() e non la riga intera, quindi il prezzo non lo conta nessuno. "
     "La resa non allunga: « GP)» ha 4 caratteri, « oro)» ne ha 5, e il riquadro e' "
     "da 36 contro i 23 che la riga usa al massimo."),
]

nuove = []
for nome, numero, coppie, motivo in CASI:
    righe = io.open(f'{SORGENTE}\\{nome}', encoding='cp932').read().split('\n')
    riga = righe[numero - 1]
    if righe.count(riga) != 1:
        raise SystemExit(f'{nome}:{numero} compare {righe.count(riga)} volte: '
                         'il cerca va allargato a un blocco')
    nuova = riga
    for prima, dopo in coppie:
        if riga.count(prima) != 1:
            raise SystemExit(f'{nome}:{numero} contiene {prima!r} {riga.count(prima)} volte')
        nuova = nuova.replace(prima, dopo)
    if nuova == riga:
        raise SystemExit(f'{nome}:{numero} non cambia')
    nuove.append({'file': nome, 'cerca': riga, 'sostituisci': nuova,
                  'motivo': motivo, 'prima': True})

testo = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in nuove)
io.open('scratchpad/_toppe-nudi-accanto.jsonl', 'w', encoding='utf-8', newline='\n').write(testo)
print(f'{len(nuove)} toppe in scratchpad/_toppe-nudi-accanto.jsonl')
