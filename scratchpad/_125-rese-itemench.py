# -*- coding: utf-8 -*-
"""125a - Le 26 firme di `custom_itemenchantment.hsp`.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_125-rese-itemench.py

⭐⭐⭐ **DICIASSETTE DELLE 26 ERANO GIA' DECISE**, e le ha trovate
`scratchpad/_125-sorelle-itemench.py` (la regola della 113a applicata al lotto
intero, come nella 124a): il giapponese di questo file e' **ricopiato identico**
da `chat.hsp:11290`-`:11661`, cioe' dal fabbro di monte. Diciassette firme hanno
la sorella gia' resa, quattro ne hanno una somigliante, cinque sono sole.

⚠️⚠️⚠️ **E LE DUE VERSIONI SONO TUTT'E DUE VIVE.** Non e' codice morto
sostituito: `chat.hsp:23306` manda a `*extrachat_diet_artifact_fusion` (questo
file) sulla voce di menu `chatval == 114514`, e `chat.hsp:11287` tiene la
fusione originale su `chatval == 1`. Stesso fabbro, due voci di menu vicine. Se
le due rese divergessero, il giocatore leggerebbe lo stesso discorso due volte,
detto in due modi: le diciassette si **copiano**, non si riscrivono.

⚠️⚠️⚠️ **IN QUESTO FILE LA FONTE SCRITTA E' L'INGLESE, NON IL GIAPPONESE.** E'
il rovescio del solito, e la regola della 109a lo prevede: «si segue la fonte
piu' affidabile, e si guarda quale fonte e' stata **copiata** e quale e' stata
**scritta**». Qui Custom-GX ha ricopiato il giapponese di monte parola per
parola e ha **riscritto l'inglese**, che dice cose che il giapponese non dice.
Ne seguono due trattamenti diversi, e la differenza non e' di gusto:

  - dove il giapponese e' una **frase di monte** e l'inglese la riscrive, vale
    la resa gia' decisa (le diciassette);
  - dove il giapponese e' un **moncone** lasciato li' (むむむ。 = «Mmm.»,
    すまんのう。 = «Mi dispiace.», どうだろう = «che ne dici») e l'inglese porta
    il contenuto vero del mod, si rende dall'**inglese**. Sono `:115`, `:267`,
    `:274` e `:276`: senza questo, il giocatore italiano leggerebbe «Mmm.» dove
    l'inglese gli dice **quanto oro costa** e **quale pozione serve**.

⭐⭐ **E IL PREFISSO DEL PUNTEGGIO SI TIENE.** Tre righe (`:67`, `:108`, `:267`)
hanno in inglese un'intestazione che il giapponese non ha:

    "The item's hill folk rating is: " + p + "/" + p(1) + "..."

`p` e' la potenza degli incantamenti dell'oggetto e `p(1)` il limite del fabbro,
tutt'e due calcolati da `*extrachat_get_thalia_score` (`:18`-`:52`): e' il
**numero concreto** della scala di cui il discorso d'apertura (`:58`) parla in
astratto, ed e' l'unico posto dove il giocatore lo legge. Tacerlo lascerebbe
l'italiano piu' povero dell'inglese su un fatto che il codice calcola apposta.
⚠️ Si dice con le parole gia' in gioco — «la scala di Thalia», da `:58` — e non
con «hill folk»: サリム e' **Thalia** in dodici rese su dodici, ed e' l'inglese
di Custom-GX ad aver cambiato nome alla scala, non il giapponese.
ⓘ La prova che il prefisso e' voluto e non un incidente: `:290` ha lo **stesso
giapponese** di `:67` e l'inglese **senza** prefisso, perche' li' il punteggio
e' gia' stato mostrato a `:267`. Due firme, due rese.

⚠️⚠️ **`:88` E' IL CASO OPPOSTO, E ERA GIA' DECISO.** La voce di menu dice in
inglese «Sorry.» dove il giapponese dice エンチャントひとつ消去 e il codice
(`chatval == 2`, `:94`-`:106`) cancella davvero un incantamento. Non e' una
divergenza di Custom-GX: `chat.hsp:11347` ha lo stesso «Sorry.» di monte, ed e'
gia' reso **«Cancellare un incanto»**. L'inglese qui non abbrevia, sbaglia.

⚠️ **`:301` non copia la sorella.** 「足りないんよ」 e' reso «Non bastano!» in
`action.hsp:14356` e `command.hsp:7784`, ma li' si parla di punti di Yacatect e
di platino; qui l'inglese dice «gold» e il codice controlla
`cdata(CDATA_GOLD, CHARA_PLAYER)`. E' oro, e la resa lo dice.

⚠️⚠️ **LE VOCI DI MENU SONO CORTE PERCHE' IL RIQUADRO E' STRETTO**, 58 caratteri
(`strumenti/menu_dialogo.py`). `:88` dice «Cancellare un **incanto**» dove la
prosa dice «incantamento», ed e' la scelta gia' fatta in `chat.hsp:11347`; e
`:276` — che nella parentesi porta `cnvitemname()`, fino a **38 caratteri** —
si riduce al **verbo solo**, «Potenziare? (…)», simmetrico alle due voci di
toppa `:278` e `:280`. La misura sta in
`scratchpad/_125-larghezze-menu-incanti.py`, e le prime stesure sforavano:
⚠️ `menu_dialogo` non se ne sarebbe accorto, perche' `reso()` conta una
chiamata di funzione come lunga zero.

⚠️ **`cnvitemname()` restituisce il nome NUDO, senza articolo** (`init.hsp:179`,
e nella build il « of » e' gia' « di »): «pozione di evoluzione», «pozione di
mutazione», «pergamena di acquisizione di attributi». Tutt'e tre **femminili**,
e sono le uniche possibili — `p_item1` e' una delle due pozioni (a
`ITEM_ID_DUMMY` la voce di menu non compare, `:275`) e `p_item2` e' la pozione
di evoluzione o la pergamena. Per questo `:297` e `:313` possono scrivere «una»
in chiaro senza chiamare `articolo.py`, che qui non arriverebbe.

ⓘ Le tre righe **inglesi nude** di questo file (`:256`, `:278`, `:280`) non
stanno in questo lotto perche' non passano da nessuna `lang()`: le fa
`_125-toppa-itemench.py`.
"""
import io
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
DENTRO = os.path.join(QUI, '_124-itemench.jsonl')
FUORI = os.path.join(RADICE, 'lavoro', 'fase6-itemench-001.jsonl')

# Il prefisso del punteggio, identico nelle tre righe che ce l'hanno in inglese.
PUNTEGGIO = ('"Sulla scala di Thalia quest\'oggetto sta a " + p + " su " '
             '+ p(1) + "...     "')

RESE = {
    # ------------------------------------------------------------------ :58
    # La fusione, discorso d'apertura. Identica a chat.hsp:11290, che la rende
    # cosi'; cambia solo la variabile del limite (li' gdata(GDATA_THALIA_LIMIT),
    # qui blacksmithlimit, che :12-:15 ricava da quella stessa).
    # ⚠️ L'inglese di Custom-GX butta la clausola del nucleo di Nefia; il
    # giapponese la tiene e il CODICE le da' ragione (:122, il ramo
    # `!= ITEM_ID_CORE_OF_NEFIA` e' quello che chiede la pergamena).
    ('custom_itemenchantment.hsp', 58):
        '"Oh, mi tieni compagnia mentre faccio pratica? E allora, qual è '
        'l\'equipaggiamento da incantare? Se ne ha già addosso di forti può '
        'darsi che resista alla magia e non ci si riesca. Vediamo... a stare a '
        'quella scala di potenza che dice Thalia, per adesso il limite è " '
        '+ blacksmithlimit + " per gli artefatti unici, " + kiseki + " per '
        'quelli eccezionali e " + kiseki2 + " per quelli celestiali. E se non '
        'fondi un nucleo di Nefia, ci vuole anche una pergamena di '
        'acquisizione di attributi."',

    # ------------------------------------------------------------------ :67
    # Il rifiuto, con il punteggio in testa. La frase e' chat.hsp:11325.
    ('custom_itemenchantment.hsp', 67):
        PUNTEGGIO + ' + "Ah! Questo non si può proprio fare. Gli incantamenti '
        'che ha addosso respingono tutto!"',

    # ------------------------------------------------- :85-:89, il menu pieno
    ('custom_itemenchantment.hsp', 85): 'Mmm.',                # chat.hsp:11344
    ('custom_itemenchantment.hsp', 86): 'Torno un\'altra volta',  # :11345
    ('custom_itemenchantment.hsp', 87): 'Nessun problema',        # :11346
    # ⚠️ l'inglese dice «Sorry.», il giapponese e il codice dicono che questa
    #    voce cancella un incantamento. Gia' deciso in chat.hsp:11347.
    ('custom_itemenchantment.hsp', 88): 'Cancellare un incanto',
    ('custom_itemenchantment.hsp', 89):
        'Gli incantamenti sono già quindici, tutti pieni. Se lo fondo così '
        'com\'è ci monta soltanto roba dello stesso tipo: per te va bene?',

    # ------------------------------------------------- :96-:105, la cancellazione
    ('custom_itemenchantment.hsp', 96):
        'Cancellarlo, dici? Mmm, con questo incantamento... non si può proprio '
        'fare. Mi dispiace.',
    ('custom_itemenchantment.hsp', 99):
        'Cancellarlo, dici? Mmm, con questo qualcosa si può fare: gli raschio '
        'via il legame...',
    ('custom_itemenchantment.hsp', 105):
        'itemname(cibk) + " perde un incantamento."',

    # ----------------------------------------------------------------- :108
    # La seconda domanda, di nuovo col punteggio in testa. Frase: chat.hsp:11367.
    ('custom_itemenchantment.hsp', 108):
        PUNTEGGIO + ' + "E allora, la forza di quale oggetto devo incastrare '
        'nell\'artefatto?"',

    # ----------------------------------------------------------------- :115
    # ⭐ Giapponese moncone (すまんのう。 = «Mi dispiace.»), inglese scritto: si
    #    rende dall'inglese tenendoci dentro le scuse del giapponese.
    #    Il ramo e' quello del nucleo di Nefia e della lacrima divina (:114,
    #    :118), che il fabbro non sa lavorare.
    #    「丘の民」 sono «gli abitanti della collina» in nove rese su nove.
    ('custom_itemenchantment.hsp', 115):
        'Un oggetto così non l\'ho mai visto in vita mia, non saprei da che '
        'parte prenderlo. Mi dispiace. Semmai portalo a qualcuno degli '
        'abitanti della collina.',

    ('custom_itemenchantment.hsp', 126):
        'Mmm, vediamo... ma un momento, non ce l\'hai una pergamena di '
        'acquisizione di attributi.',                          # chat.hsp:11377
    ('custom_itemenchantment.hsp', 175):
        '...Fusione degli incantamenti completata! È stata una bella pratica.',
                                                               # chat.hsp:11661

    # ----------------------------------------------------------------- :240
    # L'apertura della disincantazione. Nessuna sorella. Chi parla e' una donna
    # (ね, かしら), a differenza del fabbro (じゃ, のう).
    ('custom_itemenchantment.hsp', 240):
        'Ah, sembra che tu abbia qualcosa per gli incantamenti, no? E allora, '
        'su quale oggetto devo concentrarmi?',

    ('custom_itemenchantment.hsp', 266): 'Torno un\'altra volta',  # :11345

    # ----------------------------------------------------------------- :267
    # ⭐ Giapponese moncone (una domanda secca), inglese scritto: porta la
    #    regola dell'intera funzione, cioe' quale pozione serve per cosa.
    ('custom_itemenchantment.hsp', 267):
        PUNTEGGIO + ' + "Quale incantamento devo correggere? Per potenziarne '
        'uno normale ci vuole una pozione di mutazione; per potenziarne uno '
        'speciale, o per cancellarlo, una pozione di evoluzione."',

    # ----------------------------------------------------------------- :274
    # ⭐ Stesso caso: il giapponese dice «むむむ。» e l'inglese dice il PREZZO.
    #    Il moncone non si butta, diventa l'attacco della frase.
    #    `s` e' il nome dell'incantamento, che :272 prende da *item_encdetail.
    ('custom_itemenchantment.hsp', 274):
        '"Mmm, " + s + "... Per potenziare un incantamento normale ci vuole '
        'una pozione di mutazione, per uno speciale una pozione di evoluzione. '
        'Se invece lo vuoi cancellare, serve una pozione di evoluzione. Ah, e '
        'mi servono anche " + p_gold + " monete d\'oro per gli altri '
        'materiali."',

    # ----------------------------------------------------------------- :276
    # Voce di menu: deve dire che cosa fa. Il giapponese どうだろう («che ne
    # dici») non lo dice, l'inglese si'.
    # ⚠️ L'etichetta e' il verbo solo, e non «Potenziare l'incanto?»: dentro la
    #    parentesi ci va cnvitemname(), che per la pergamena di acquisizione di
    #    attributi vale 38 caratteri su un tetto di 58. Le tre voci di questa
    #    finestra (:276 qui, :278 e :280 di toppa) restano cosi' simmetriche
    #    fra loro e coi tre messaggi finali. Che cosa si potenzia lo dice :274,
    #    due righe sopra. Misurate da _125-larghezze-menu-incanti.py.
    ('custom_itemenchantment.hsp', 276):
        '"Potenziare? (" + cnvitemname(p_item1) + ")"',

    # ----------------------------------------------------------------- :290
    # Stesso giapponese di :67 e stessa frase, ma SENZA il punteggio: qui e'
    # gia' stato mostrato a :267. Due firme, e la differenza e' voluta.
    ('custom_itemenchantment.hsp', 290):
        'Ah! Questo non si può proprio fare. Gli incantamenti che ha addosso '
        'respingono tutto!',

    # ------------------------------------------------------------ :297, :313
    # La forma e' quella di :126, con il nome dell'oggetto al posto della
    # pergamena. «una» in chiaro: i tre nomi possibili sono tutti femminili.
    ('custom_itemenchantment.hsp', 297):
        '"Mmm, vediamo... ma un momento, non ce l\'hai una " '
        '+ cnvitemname(p_item1) + "."',
    ('custom_itemenchantment.hsp', 313):
        '"Mmm, vediamo... ma un momento, non ce l\'hai una " '
        '+ cnvitemname(p_item2) + "."',

    # ----------------------------------------------------------------- :301
    # ⚠️ NON e' la sorella «Non bastano!»: quelle due parlano di punti e di
    #    platino, qui il codice controlla l'oro (:300).
    ('custom_itemenchantment.hsp', 301): 'L\'oro non basta!',

    # --------------------------------------------- :308, :325, :327, la chiusa
    # Stessa famiglia di :175, che e' gia' resa: cambia solo il nome
    # dell'operazione. 改造 potenzia, 消去 cancella, 弱める indebolisce — e il
    # codice lo conferma (:307 encadd, :323 encremove, :324 il confronto
    # `p_rem == val(1)` che distingue cancellare da indebolire).
    ('custom_itemenchantment.hsp', 308):
        '...Potenziamento dell\'incantamento completato! È stata una bella '
        'pratica.',
    ('custom_itemenchantment.hsp', 325):
        '...Cancellazione dell\'incantamento completata! È stata una bella '
        'pratica.',
    ('custom_itemenchantment.hsp', 327):
        '...Indebolimento dell\'incantamento completato! È stata una bella '
        'pratica.',
}


def main():
    voci = [json.loads(l) for l in io.open(DENTRO, encoding='utf-8')]
    assert len(voci) == len(RESE), (len(voci), len(RESE))
    for v in voci:
        chiave = (v['file'], v['riga'])
        assert chiave in RESE, chiave
        v['it'] = RESE[chiave]
    with io.open(FUORI, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%d rese in %s' % (len(voci), FUORI))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
