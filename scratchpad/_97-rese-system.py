# -*- coding: utf-8 -*-
"""97a - `system.hsp` per intero: 40 firme, e il file si chiude.

`system.hsp` non e' una schermata: e' **l'avvio**. Dentro ci stanno tre cose
diverse, e nessuna delle tre si vede giocando normalmente —

  1. l'**aggiornamento del salvataggio** da una versione vecchia (`:106`-`:906`),
     una catena di `if ( gdata(GDATA_VERSION) < N )` che si legge una volta sola
     nella vita di una partita;
  2. il **caricamento dei PNG e degli oggetti fatti dal giocatore**
     (`:1433`-`:2096`), con i suoi selettori di file;
  3. l'**esportazione** di mappe e squadre (`:2504`-`:3317`), cioe' le
     intestazioni dei file che i giocatori si scambiano.

⭐⭐⭐ LA COSA CHE DECIDE PIU' RIGHE DEL LOTTO: **QUI L'INGLESE E IL GIAPPONESE
DICONO COSE DIVERSE QUATTRO VOLTE, E NON VINCE SEMPRE LO STESSO.** Il testimone
si sceglie guardando **che cosa fa il codice**, non quale lingua di solito ha
ragione:

  - `:289` `lang("盗賊団フラグ抹消。", "Death bug is corrected.")` — il blocco fa
    `gdata(GDATA_QUEST) = QUEST_TYPE_NONE` quando l'incarico e' quello dei
    ladri. **Ha ragione il giapponese**; l'inglese parla di un baco della morte
    che li' non c'entra niente;
  - `:445` `lang("1.18fix以外のセーブデータは使えません。", "…please save not
    1.18fix version then retry.")` — il blocco e' `if ( GDATA_VERSION == 2220 )
    { dialog …; goto *exit_game }`, cioe' il salvataggio **e'** la 1.18fix e
    viene rifiutato. Il giapponese dice l'opposto («i salvataggi **diversi** da
    1.18fix non si possono usare»): **ha ragione l'inglese**. ⚠️ Ed e' un
    rovesciamento, non una sfumatura: i due fratelli `:436` e `:574`, con lo
    stesso identico blocco, in giapponese lo dicono giusto;
  - `:531` `lang("「おい、暗殺者が私の後ろにいるぞ」", cnvtalk("Hey, the assassins
    are killing me."))` — e' il cliente della scorta che avvisa. Il giapponese
    dice «ho un assassino alle spalle», l'inglese «mi stanno ammazzando», e il
    codice mette `p = DAMAGE_FROM_UNSEEN`: e' **un colpo da un nemico che non si
    vede**, cioe' esattamente il giapponese;
  - `:1959` e `:1976` — il giapponese chiede «da quale file creare il PNG?» e
    «quale immagine incorporare?», l'inglese si limita a «Choose the original
    file.» / «Choose the graphic file.». I due siti gemelli `:1856` e `:1873`
    fanno la domanda per intero in tutt'e due le lingue: si segue il giapponese,
    che e' anche l'unico che tiene le quattro righe parallele.

⚠️⚠️ LA SECONDA: `:1873` E `:1976` HANNO LO **STESSO GIAPPONESE**
(どの画像を埋め込む？) e due inglesi diversi. **Si rende uguale** — «Quale
immagine incorporare?» — perche' e' la stessa domanda, fatta una volta per
l'oggetto e una per il PNG. `:1997` invece ha un giapponese suo (…(jpg推奨)) e
prende la sua resa.

⚠️ **CORREZIONE.** Qui c'era scritto che `battute --divergenti` sarebbe salito da
13 a 14 rendendoli in due modi. **E' falso**: `strumenti/battute.py:79` e'
`FILE = "db_creature.hsp"`, e quello strumento non guarda nessun altro file. La
rete che vede questa famiglia su tutto il dizionario e'
`scratchpad/misura-rete4.py`, che separa i gruppi con lo **stesso** inglese da
quelli con inglese diverso — e questo sarebbe finito fra i secondi.

⭐ LA TERZA: L'INTESTAZIONE DEI FILE ESPORTATI E' TESTO, NON UNA CHIAVE — E
L'HO VERIFICATO. `:3271` scrive `[Made by][titolo]` in cima al file di una mappa
esportata, e la tentazione e' lasciarlo inglese per non rompere chi lo rilegge.
Chi lo rilegge e' `command.hsp:407`-`:416`, e prende le righe **per posizione**
(`noteget s, 0`), non cercando la targhetta: `[Made by]` si vede e non si
confronta. Si traduce.

⚠️ QUATTRO VOCI DI QUESTO FILE NON SONO RESE, E STANNO IN `invariati.md`:
`iknownnameref_en.` e `author_en.` (`:1441`, `:1442`) sono le **chiavi** che
`getnpctxt()` cerca dentro il file `.txt` del giocatore, come `EN` per
`book.txt`; `[` e `]` (`:3316`) sono la **cornice** attorno al nome della
squadra, come `< ` e ` >` di `god.hsp`. ⭐ E `lang("", " ")` di `:3317` era gia'
dichiarato dalla 39a per `strblank`: il confronto e' sul valore intero, quindi
lo copre.

LESSICO EREDITATO (non deciso qui):
  - «Hai imparato una nuova capacità: …»  `action.hsp:12012`, `chara.hsp:16`
    (⚠️ `ability` -> «capacità», non «abilità», che e' `Skill`: `glossario.md`)
  - «Il tuo diario è stato aggiornato.»   `action.hsp:8282` e due altri siti
  - punti bonus per gli incantesimi       `proc.hsp:11773`
  - geni                                  `action.hsp:8800`
  - PNG                                   `chara.hsp:4314`, `command.hsp:3543`

PERIMETRO: 40 firme su 40. Nessuna in un ramo `if ( jp )` (`lang-nel-ramo-jp.py`
resta 21 | 0), nessuna in un `if ( 0 )`. L'unica morta del file, `:777`, e' gia'
in `rinviate.jsonl` — ed e' viva e resa in `screen.hsp:6792`.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""
import io
import json
import sys

RESE = {
    # --- 1. l'aggiornamento del salvataggio, che si legge una volta sola
    (106, 'Updating your save data from Ver.'):
        '"Aggiorno il salvataggio della Ver." + gdata(GDATA_VERSION) + "."',
    (212, 'Please exit the current area and enter the world map once'):
        "Per aggiornare i dati delle proprietà, dopo l'avvio esci una volta sulla mappa del mondo.",
    (242, 'To update your game, please save your game in a town'):
        'Per aggiornare serve un salvataggio fatto in città con la versione precedente.',
    (245, 'The next updating process may take a while to complete.'):
        'Il passaggio che segue può richiedere un po\' di tempo.',
    (289, 'Death bug is corrected.'):
        "Azzerata la bandiera dell'incarico dei ladri.",
    (436, 'To update your game, please save not 1.1555 version then retry.'):
        "Il salvataggio della 1.1555 non si può aggiornare: ne serve uno di un'altra versione.",
    (445, 'To update your game, please save not 1.18fix version then retry.'):
        "Il salvataggio della 1.18fix non si può usare: ne serve uno di un'altra versione.",
    (513, 'To update your game, please save not 1.25 version then retry.'):
        "Il salvataggio della 1.25 non si può aggiornare: ne serve uno di un'altra versione.",
    (574, 'To update your game, please save not 1.38 version then retry.'):
        'Il salvataggio della 1.38 non si può aggiornare.',
    (531, 'Hey, the assassins are killing me.'):
        'Ehi, ho un assassino alle spalle!',
    (596, 'You have learned a new ability,'):
        '"Hai imparato una nuova capacità: " + skillname(SKILL_SPACT_GAUGE_RELEASE) + "."',
    (845, 'You have learned new ability,'):
        '"Hai imparato una nuova capacità: " + skillname(SKILL_SPACT_MAGNECOAT) + "."',
    (943, 'You have learned new ability,'):
        '"Hai imparato una nuova capacità: " + skillname(SKILL_SPACT_EYE_OF_ANE) + "."',
    (743, 'You gain spell bonus points.'):
        'Ottieni punti bonus per gli incantesimi.',
    (752, 'The graphic of the eye evolution character have been corrected.'):
        "Corretta l'immagine delle evoluzioni degli occhi.",
    (906, 'Your journal has been updated.'):
        'Il tuo diario è stato aggiornato.',
    (1013, 'This adventurer can not be revived...'):
        'Quell\'avventuriero non tornerà più...',
    (1064, 'It is a nosave penalty.'):
        'La partita precedente è stata chiusa a forza invece di uscire con Esc: penalità.',

    # --- 2. i PNG e gli oggetti fatti dal giocatore
    (1433, 'An item of the same name exists.'):
        'Un oggetto con lo stesso nome non viene caricato.',
    (1441, 'iknownnameref_en.'): 'iknownnameref_en.',
    (1442, 'author_en.'): 'author_en.',
    (1442, 'Player'): 'Giocatore',
    (1693, 'A npc of the same name exists.'):
        'Un PNG con lo stesso nome non viene caricato.',
    (1856, 'Use which file to create item?'): "Da quale file creare l'oggetto?",
    (1873, 'Embed which picture?'): 'Quale immagine incorporare?',
    (1959, 'Choose the original file.'): 'Da quale file creare il PNG?',
    (1976, 'Choose the graphic file.'): 'Quale immagine incorporare?',
    (1995, 'Embed portrait?'): 'Incorporare il ritratto?',
    (1997, 'Embed which picture?(.jpg recommended)'):
        'Quale immagine incorporare? (meglio .jpg)',
    (2084, 'A custom NPC has been successfully generated!'):
        'PNG personalizzato creato!',
    (2096, ''): 'name(rc) + " va su tutte le furie e ti attacca."',
    (2209, 'Save file:'):
        '"Salvataggio: " + file + " non esiste. Controlla la cartella: '
        'potrebbe essere un errore nello spostamento dei file."',
    (2259, 'Save file:'):
        '"Salvataggio: " + file + " non si è potuto leggere. '
        'Il file potrebbe essere danneggiato."',

    # --- 3. le intestazioni dei file esportati
    (2504, "'s Gene"): ' - i geni',   # ⚠️ trattino ASCII: CP932 cancella la lineetta lunga
    (3271, '[Made by]['): '[Fatto da][',
    (3271, ']'): ']',
    (3280, '[Made by]'): '[Fatto da]',
    (3316, '['): '[',
    (3316, 'p'): 'pg',
    (3317, ' '): ' ',
}

LOTTO = 'lavoro/97-system.jsonl'

voci = [json.loads(l) for l in io.open(LOTTO, encoding='utf-8') if l.strip()]


def chiave(v):
    trovate = [k for k in RESE if k[0] == v['riga'] and v['en'].startswith(k[1])]
    if len(trovate) != 1:
        # ⚠️ `:3271` porta `'[Made by]['` e `']'`, e `startswith('')` prende
        # tutto: si preferisce la chiave piu' lunga che aggancia davvero.
        esatte = [k for k in trovate if k[1] == v['en']]
        if len(esatte) == 1:
            return esatte[0]
        return None
    return trovate[0]


mancanti = [(v['riga'], v['en']) for v in voci if chiave(v) is None]
usate = {chiave(v) for v in voci if chiave(v)}
in_piu = [k for k in RESE if k not in usate]
if mancanti or in_piu:
    print('mancanti: %s' % mancanti)
    print("in piu' : %s" % in_piu)
    sys.exit(1)

with io.open(LOTTO, 'w', encoding='utf-8', newline='\n') as fh:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        fh.write(json.dumps(v, ensure_ascii=False) + '\n')
print('%d rese scritte in %s' % (len(voci), LOTTO))
