# -*- coding: utf-8 -*-
"""125a - Le 24 firme di `net.hsp`.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_125-rese-net.py

`net.hsp` sono le funzioni in rete di monte: la chat verso il server, l'urna del
**voto per l'esecuzione** dei lupi mannari (`*com_vote_new`, locale) e quella del
**voto per l'epiteto** (`*com_vote`, che parla col CGI di nifty.com), piu' le due
finestre del caricamento file e del browser interno.

⚠️⚠️⚠️ **`:375` E' UN DIFETTO DI MONTE, ED E' LA FORMA DELLA 119a: L'INGLESE HA
RICOPIATO UNA RIGA NELL'ALTRA.** Tre righe portano lo stesso inglese —
«You need to wait before submitting a new vote.» — ma i giapponesi sono due:

    :375  現在、処刑投票は行われていない。      «adesso non si vota»
    :565  まだ投票権が復活していない。          «non hai ancora riavuto il voto»
    :717  まだ投票権が復活していない。          (stessa firma di :565)

⭐ **E il codice da' ragione al giapponese, non all'inglese**: `:373` entra in
quel ramo con `mdata(MDATA_WEREWOLF_STAGE) == 0`, cioe' *nessuna votazione in
corso*, mentre `:563` e `:715` guardano `gdata(GDATA_NEXT_VOTE)`, cioe' *il tuo
diritto di voto*. Sono due cose diverse e l'inglese le dice uguali. Reso dal
giapponese, e le due firme restano distinte.

⚠️ **`:749` e `:751`: l'inglese ripete una frase, il giapponese la mette una
volta sola.** La finestra del caricamento ha due scritte, in alto (`pos 140,25`)
e in basso (`pos 120,180`); l'inglese scrive l'istruzione in tutt'e due, il
giapponese mette l'uscita in alto e l'istruzione in basso. Si segue il
giapponese: due scritte diverse invece della stessa due volte.

⚠️ **Quattro voci restano identiche all'inglese e sono dichiarate in
`invariati.md`**, sezione «Versi senza contenuto linguistico»: sono una
spaziatura e due parentesi, cioe' cornice. Senza la dichiarazione `verifica`
rifiuterebbe il lotto intero per «traduzione identica all'inglese», e l'unico
modo di farlo passare sarebbe inventare qualcosa.

    :367   lang("", " ")     lo spazio fra epiteto e nome nel messaggio inviato
    :534   lang(" ", "(")    la parentesi che apre il conto dei voti
    :534   lang("票", ")")   quella che lo chiude

⭐ **`:367` — « says, » invece si rende.** E' testo, non cornice: la riga e'
`net_send "chat" + AKA + lang("", " ") + NOME + lang("", " says, ") + inputlog`,
cioe' il messaggio che il giocatore manda al server. Il giapponese non ha niente
li' perche' incornicia col 「」 di `:360`; ogni lingua ci mette la sua congiunzione,
e l'italiano mette « dice, ». ⓘ E' l'unica riga del progetto misurata finora che
esce **verso** un server invece di entrare a schermo.

⚠️ **異名 e' «epiteto» qui**, perche' e' il nome della funzione e le sue tre
sorelle lo dicono gia' cosi': `action.hsp:2238` «Vota per l'epiteto»,
`chara.hsp:3187` «Scelta dell'epiteto», `chara.hsp:3196` «Epiteti».
⚠️⚠️ **E la stessa parola e' resa «alias» in due righe** — `command.hsp:4566` e
`command.hsp:10504` — che sono la **stessa funzione**. Misurato, non deciso:
`:10504` e' l'etichetta della scheda e ha un budget di larghezza, quindi il
cambio va misurato prima di farlo. In prosa 異名 e' «soprannome» otto volte su
otto, e quello e' un caso diverso e va bene com'e'.
"""
import io
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
DENTRO = os.path.join(QUI, '_125-net.jsonl')
FUORI = os.path.join(RADICE, 'lavoro', 'fase6-net-001.jsonl')

# La chiave e' (riga, inglese): quattro righe di questo file portano DUE firme
# ciascuna, perche' una `lang()` per parte sta nella stessa istruzione.
RESE = {
    # --- la chat verso il server
    (42, 'You need an internet connection.'): 'Non c\'è connessione a internet.',
    (49, 'Failed to send a message.'): 'Invio non riuscito.',
    (345, 'You think you should wait a little more.'):
        'Ti sembra meglio aspettare ancora un po\'.',
    # cornice: lo spazio fra epiteto e nome. Dichiarato in invariati.md.
    (367, ' '): ' ',
    (367, ' says, '): ' dice, ',

    # --- l'urna del voto per l'esecuzione (*com_vote_new)
    # ⚠️ l'inglese qui e' ricopiato da :565 e dice un'altra cosa: si segue il
    #    giapponese, che il codice conferma (:373, WEREWOLF_STAGE == 0).
    (375, 'You need to wait before submitting a new vote.'):
        'Al momento non c\'è nessuna votazione per l\'esecuzione.',
    (465, "You can't vote until ."):
        '"Non hai ancora riavuto il diritto di voto (fino a "'
        ' + cnvdate(gdata(GDATA_NEXT_VOTE), 1) + ")"',
    (473, 'Who do you want to vote for?'): 'Per quale candidato vuoi votare?',
    (485, 'Voting Box'): 'Urna',
    # la barra dei tasti: forma gia' in uso in command.hsp:10347 e sorelle
    (485, 'Enter [Vote] '): 'Invio [Vota] ',
    (493, 'Name'): 'Nome',
    (493, 'Vote'): 'Voti',
    # cornice: le due parentesi intorno al conto dei voti. In invariati.md.
    (534, '('): '(',
    (534, ')'): ')',
    (565, 'You need to wait before submitting a new vote.'):
        'Non hai ancora riavuto il diritto di voto.',
    (572, 'You vote.'): 'Hai votato.',

    # --- l'urna del voto per l'epiteto (*com_vote)
    (604, 'Submit your alias.'): 'Registra il tuo epiteto',
    (646, 'Choice'): 'Scelta',
    (646, 'Vote'): 'Voti',
    (721, 'I like !'):
        'cnvtalk("Mi piace " + listn(0, cs + pagesize * page) + "!")',

    # --- la finestra del caricamento e quella del browser
    # ⚠️ l'inglese ripete l'istruzione in tutt'e due le scritte; il giapponese
    #    mette l'uscita in alto e l'istruzione in basso, e si segue quello.
    (749, 'Select a file and press the upload button.\\nPress the Esc key to return.'):
        'Premi Esc per chiudere.',
    (751, 'Select a file and press the upload button.'):
        'Premi il pulsante Sfoglia, scegli un file nella cartella elona/user'
        '\\ne caricalo.',
    (781, 'Slow loading? Try exiting your internet browser or restart the game.'):
        'Ti viene da pensare che forse conviene chiudere il browser, o '
        'riavviare il gioco.',
    (825, 'Press the Esc key to return.'): 'Premi Esc per chiudere.',
}


def main():
    voci = [json.loads(l) for l in io.open(DENTRO, encoding='utf-8')]
    assert len(voci) == len(RESE), (len(voci), len(RESE))
    for v in voci:
        chiave = (v['riga'], v['en'])
        assert chiave in RESE, chiave
        v['it'] = RESE[chiave]
    with io.open(FUORI, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%d rese in %s' % (len(voci), FUORI))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
