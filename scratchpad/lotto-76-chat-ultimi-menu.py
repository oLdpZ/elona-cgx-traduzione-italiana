# -*- coding: utf-8 -*-
"""76a — `chat.hsp`, gli ultimi cinque menu a meta', piu' quelli che tirano.

    :5682-:5696   i briganti e i pirati            «(Attaccare da lontano)» / 4 no
    :19327-:19340 il pasto insieme                 «Ritirare i materiali» / 4 no
    :24094-:24100 la scuola di magia               «Annulla» / 6 no
    :24715-:24724 il catalogo degli schiavi        «Annulla» / 4 no
    :24954-:24961 imparare o allenare una capacita' «Annulla» / 2 no

⚠️⚠️ **E l'ultimo ne ha tirati dentro altri due, sempre per la firma.**
「習得する」/«Teach me the skill.» e 「訓練する」/«Train me.» stanno tutt'e due
anche a `:390` e `:396`, dentro la schermata dell'**allenatore amico** (quella a
«prezzo d'amico»), che oggi e' tutta inglese: tradurle solo per `:24954` avrebbe
aperto quella. Quindi entrano anche `:388`, `:394` e `:399`. E la schermata di
`:24943` porta con se' il suo `buff` e il bottone 「訓練する」 di `:24945`, che
`blocchi_menu` considera un menu a parte perche' dista sedici righe dal
successivo — **il raggruppamento per distanza e' il limite noto della rete**.

⚠️⚠️ **`:19327` e `:19334` sono righe COMMENTATE** (`// chatList 84, ...`): la
variante lunga delle due voci vive, con la coda `[Total EXP 200%, Satiety
increase halved]`. La prima stesura le aveva tradotte «tanto non costa niente»,
e **e' costato**: una voce tradotta entra in `voci_di_menu()`, quindi la loro
coda da 74 caratteri e' finita nel registro delle voci rotte a monte e la mia
resa da 61 in quello delle voci fuori misura — due numeri veri su una riga che
non disegna niente. Vanno in `rinviate.jsonl`, come le tre del blocco `ORIGINAL`
spento di `command.hsp`. 💡 *Tradurre codice morto non e' gratis: lo fa entrare
nelle misure.*

⚠️ **Tre tetti stretti da `tagliate_a_due_colonne`**, tutti nel catalogo:
l'inglese e' «Catalog A (Level < 9999)», 24 caratteri contati con `reso()`, che
vale quattro cifre per ogni valore interpolato. «Catalogo A (max Lv. 9999)» ne
fa 25, e la parentesi si toglie: «Catalogo A: max Lv. 9999», 24 esatti. `Lv.` e'
la forma che il progetto usa gia' (`text.hsp:10851`, «[Lv. 80] H Sister»).

⚠️⚠️ **E i due del catalogo hanno fatto trovare un difetto nella rete**, non nel
lotto: `menu_dialogo._INTERPOLAZIONE` non ammetteva un `+` dentro il valore
interpolato, e `limit(... / 2 + 5, 6, 130)` non veniva riconosciuto — `reso()`
restituiva l'espressione intera e la voce risultava lunga **84** caratteri
invece di 24. Si vedeva solo come «gia' rotta in inglese», perche' l'inglese ha
la stessa forma e sbagliava allo stesso modo. Corretto, con due test.

⚠️ **Il genere, due volte.** (1) `:5698` chiama il giocatore «traveler»: in
italiano «viandante» va bene per chiunque — ed e' la parola con cui
`name(CHARA_PLAYER)` lo chiama gia' — mentre «fortunato» no, e diventa «Hai
proprio una bella fortuna». (2) `:394` non puo' dire «la tua " + skillname()»,
perche' l'articolo si accorderebbe col nome della capacita': si dice «allenarti
in " + skillname()», dove la preposizione non porta articolo.

⭐ `:24943` e `:24949` rimettono la domanda che l'inglese ha buttato via
(「…けどいい」): «Va bene?». E' quel che il progetto fa gia' a `chat.hsp:23750`.

    python scratchpad/lotto-76-chat-ultimi-menu.py
"""
import io
import json
import sys

USCITA = 'lavoro/76-chat-ultimi-menu.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
# ⚠️ le due righe vive sono prese una per una: :19327 e :19334 sono commentate
# e rinviate, e una zona che le contenesse le ripescherebbe
ZONE = ((388, 399), (5682, 5701), (19328, 19328), (19335, 19335), (24094, 24101),
        (24713, 24722), (24943, 24958))

RESE = {
    # --- :388 l'allenatore amico (tirato dentro dalle firme di :24954 e :24945)
    (388, 'I can teach you the art of  for a friendly price of  platinum pieces. Do you want me to train you?'):
        ('"Posso insegnarti " + skillname(csskill) + " a prezzo d\'amico, "'
         ' + calclearncost(csskill, cc, 1) + " monete di platino. Che ne dici?"'),
    (390, 'Teach me the skill.'): 'Imparare',
    (394, 'I can train your  skill for a friendly price of  platinum pieces. Do you want me to train you?'):
        ('"Posso allenarti in " + skillname(csskill) + " a prezzo d\'amico, "'
         ' + calctraincost(csskill, cc, 1) + " monete di platino. Che ne dici?"'),
    (396, 'Train me.'): 'Allenare',
    (399, "I think I'll pass."): 'Lascio perdere',

    # --- :5682 i briganti di terra e i pirati di mare
    (5682, 'Try me.'): 'Fatti sotto',
    (5687, '(Ram your ship and get in) (success rate:%)'):
        '"(Sperona e sali) (" + seikou + "%)"',
    (5694, '(Run away)'): '(Fuggire)',
    (5696, 'I surrender.'): 'Mi arrendo',
    (5698, 'Halt, halt, traveler. You\'re a quite fortunate one. Before you is the renowned band of legendary brigands \\"\\" that the mere mention of its name is enough to silence a naughty child. Yet we will spare your life for only a toll of  gold pieces and your cargos. Quite fortunate indeed.'):
        ('"Alt, alt, viandante. Hai proprio una bella fortuna. Davanti a te c\'è la '
         'banda di briganti \\"" + gdatan(GDATAN_TEAM2) + "\\", quella che a nominarla '
         'zittisce i bambini capricciosi. E ti lasciamo la vita per un pedaggio da '
         'niente: il carico e " + cdata(CDATA_GOLD, CHARA_PLAYER) / 5 + " monete d\'oro. '
         'Una vera fortuna."'),
    (5701, 'Don\'t resist! We will sink your ship if you try to run. Before you is the renowned band of legendary pirates \\"\\" that the mere mention of its name is enough to silence a naughty child. Yet we will spare your life for only a toll of  gold pices and your cargos. Quite fortunate indeed.'):
        ('"Non opporre resistenza! Se scappi ti affondiamo. Davanti a te c\'è la banda '
         'di pirati \\"" + gdatan(GDATAN_TEAM2) + "\\", quella che a nominarla zittisce '
         'i bambini capricciosi. E ti lasciamo la vita per un pedaggio da niente: il '
         'carico e " + cdata(CDATA_GOLD, CHARA_PLAYER) / 5 + " monete d\'oro. Una vera '
         'fortuna."'),

    # --- :19328 il pasto insieme (le due righe VIVE; le commentate sono rinviate)
    (19328, "Let's have a meal together."): 'Mangiare insieme',
    (19335, 'Have a meal with your tag partner.'): 'Far mangiare la coppia',

    # --- :24094 la scuola di magia
    (24095, 'Sorcerer Training (Attack Magic)'): "Corso da stregone (magie d'attacco)",
    (24096, 'Warlock Training (High Lvl Atk Magic)'): 'Corso da mago nero (attacco superiore)',
    (24097, 'Enchanter Training (Buffing Magic)'): 'Corso da incantatore (potenziamenti)',
    (24098, 'Healer Training (Healing Magic)'): 'Corso da guaritore (magie curative)',
    (24099, 'Shaman Training (Special Magic)'): 'Corso da sciamano (magie speciali)',
    (24100, 'Mage Training (Exploration Magic)'): 'Corso da mago (magie di esplorazione)',
    (24101, 'Which magic practice are you going to do?'): 'Quale corso vuoi seguire?',

    # --- :24713 il catalogo degli schiavi
    (24713, "Okay. Let me check the stable... How about  for  gold pieces. I'd say it's quite a bargain!"):
        ('"D\'accordo, vediamo nella stalla... " + cnven(cdatan(CDATAN_NAME, MAX_CHARA_NC))'
         ' + " per " + calcslavevalue(MAX_CHARA_NC) + " monete d\'oro: un affare, direi!"'),
    # ⚠️ senza parentesi: «Catalogo A (max Lv. 9999)» e' 25 e l'inglese sta in 24
    (24715, 'Catalog A (Level < )'):
        '"Catalogo A: max Lv. " + limit(cdata(CDATA_LEVEL, CHARA_PLAYER) / 2 + 5, 6, 130)',
    (24718, 'Catalog B (Level < )'):
        '"Catalogo B: max Lv. " + limit(cdata(CDATA_LEVEL, CHARA_PLAYER) / 4 + 5, 6, 50)',
    (24720, 'Catalog C (Level < 5)'): 'Catalogo C: max Lv. 5',
    (24722, "I'll pay."): 'Comprare',

    # --- :24943 imparare o allenare una capacita'
    (24943, 'Training  will cost you  platinum pieces.'):
        ('"Allenare " + skillname(csskill) + " ti costa " + calctraincost(csskill, cc)'
         ' + " monete di platino. Va bene?"'),
    (24949, 'Learning  will cost you  platinum pieces.'):
        ('"Imparare " + skillname(csskill) + " ti costa " + calclearncost(csskill, cc)'
         ' + " monete di platino. Va bene?"'),
    (24954, 'Teach me the skill in exchange for a skill ticket.'):
        "Imparare con un biglietto d'abilità",
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
