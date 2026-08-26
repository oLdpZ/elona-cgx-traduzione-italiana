import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :44034 l'atto dell'accampamento
    (44034, '(Single-use) Readable deed used to build a labor camp.'):
        "Un atto: letto, fa nascere un accampamento.",

    # ---------------------------------------------------------- :44303 la pergamena del raccolto
    (44303, 'It is a scroll that when read, causes gold coins to fall from the sky.'):
        "Una pergamena che fa piovere monete d'oro dal cielo.",

    # ---------------------------------------------------------- :44374 la pergamena del richiamo
    (44374, 'It is a scroll that when read, pulls three enemies to you.'):
        "Una pergamena che tira a sé fino a tre nemici.",

    # ---------------------------------------------------------- :45063 i sei atti dei mezzi di mare
    # ⚠️ il giapponese non nomina il mezzo — dice «un mezzo per la mappa del
    #    mare» — perché il nome dell'oggetto lo dice già. Sei firme, un solo
    #    giapponese, e l'inglese ci mette il nome: qui vince il giapponese.
    (45063, 'Certificate of ownership of a land raft. Can be read more than once.'):
        "Un atto per un mezzo di mare. Si può rileggere sempre.",

    (45134, 'Certificate of ownership of a fishing ship. Can be read more than once.'):
        "Un atto per un mezzo di mare. Si può rileggere sempre.",

    (45205, 'Certificate of ownership of a pirate ship. Can be read more than once.'):
        "Un atto per un mezzo di mare. Si può rileggere sempre.",

    (45276, 'Certificate of ownership of a cruise ship. Can be read more than once.'):
        "Un atto per un mezzo di mare. Si può rileggere sempre.",

    (45347, 'Certificate of ownership of a warship. Can be read more than once.'):
        "Un atto per un mezzo di mare. Si può rileggere sempre.",

    (45418, 'Certificate of ownership of a submarine. Can be read more than once.'):
        "Un atto per un mezzo di mare. Si può rileggere sempre.",

    # ---------------------------------------------------------- :51362 i quattro atti dei mezzi di terra
    (51362, 'Certificate of ownership of a battleship. Can be read more than once.'):
        "Un atto per un mezzo da viaggio. Si può rileggere sempre.",

    (51433, 'Certificate of ownership of a locomotive. Can be read more than once.'):
        "Un atto per un mezzo da viaggio. Si può rileggere sempre.",

    (51504, 'Certificate of ownership of a truck. Can be read more than once.'):
        "Un atto per un mezzo da viaggio. Si può rileggere sempre.",

    (51575, 'Certificate of ownership of a carriage. Can be read more than once.'):
        "Un atto per un mezzo da viaggio. Si può rileggere sempre.",

    # ---------------------------------------------------------- :52520 la pergamena della stregoneria
    # ⚠️ il «5» lo dice solo l'inglese; il giapponese dice スペルボーナス e basta.
    (52520, 'It is a scroll that when read, grants 5 spell bonus points.'):
        "Una pergamena che dà punti bonus per gli incantesimi.",

    # ---------------------------------------------------------- :55214 l'atto del trasferimento
    (55214, '(Single-use) Readable deed used to move a building, except your home.'):
        "Un atto: letto, sposta un edificio che non sia la casa.",

    # ---------------------------------------------------------- :58399 i due certificati fiscali
    (58399, 'Certificate that allows tax to be paid in advance. Pay them at tax boxes.'):
        "Paga le tasse in anticipo. Si mette nella cassetta delle tasse.",

    # ---------------------------------------------------------- :70200 l'atto dell'allevamento abbandonato
    (70200, '(Single-use) Readable deed used to build a giant ranch.'):
        "Un atto: letto, fa nascere un allevamento di mostri.",

    # ---------------------------------------------------------- :71031 l'atto del trasloco
    (71031, '(Single-use) Readable deed used to move your home.'):
        "Un atto: letto, permette di traslocare.",

    # ---------------------------------------------------------- :81402 la licenza dell'esploratore del vuoto
    # ⚠️ il giapponese non dice DOVE sta il Vuoto: lo aggiunge l'inglese.
    (81402, 'Certificate that allow one to explore the Void at South-West North Tyris.'):
        "Un atto: letto, dà il permesso di entrare nel Vuoto.",

    # ---------------------------------------------------------- :81743 la pergamena del nome
    # ⚠️ il giapponese scrive 「☆のついた武器防具」, ma ☆ e ★ sono a DOPPIA
    #    LARGHEZZA in CP932 e `guardie` li boccia: nessuna resa del progetto ne
    #    contiene uno (0 su 23.469). Si scrive quel che la stella significa, e
    #    lo dice l'inglese: le due qualità che marca, `_quality` 4 e 5.
    (81743, 'It is a scroll that when read, renames a miracle or godly equipment.'):
        "Cambia il nome a un'arma o armatura eccezionale o celestiale.",

    # ---------------------------------------------------------- :83414 l'atto del sotterraneo
    (83414, '(Single-use) Readable deed used to build a dungeon.'):
        "Un atto: letto, fa nascere un sotterraneo.",

    # ---------------------------------------------------------- :83629 la pergamena della contingenza
    (83629, 'It is a scroll that when read, allow you to sometimes cheat Death.'):
        "A volte azzera il colpo che sarebbe mortale.",

    # ---------------------------------------------------------- :88349 la pergamena della fuga
    (88349, 'It is a scroll that when read, opens a rift to escape after a few turns.'):
        "Porta fuori dal sotterraneo dopo qualche turno. Rileggerla annulla.",

    # ---------------------------------------------------------- :88744 la pergamena volante
    (88744, 'It is a scroll that when read, reduce weight of 1 item in your backpack.'):
        "Alleggerisce un oggetto dello zaino.",

    # ---------------------------------------------------------- :89493 la mappa del tesoro
    (89493, "(Re-usable) readable map from sources unknown that lead's to treasure."):
        "Una mappa con su un tesoro nascosto da qualche parte.",

    # ---------------------------------------------------------- :89887 la fattura
    (89887, 'It is a piece of paper with the amount of tax to be collected.'):
        "Un foglio con su quante tasse si devono pagare.",

    # ---------------------------------------------------------- :92657 l'atto dell'allevamento
    (92657, '(Single-use) Readable deed used to build a ranch.'):
        "Un atto: letto, fa nascere un allevamento.",

    # ---------------------------------------------------------- :94249 la pergamena della pioggia curativa
    (94249, 'It is a scroll that when read, restore health of the surrounding allies.'):
        "Cura i compagni qui attorno.",

    # ---------------------------------------------------------- :94673 l'atto del magazzino
    (94673, '(Single-use) Readable deed used to build a warehouse.'):
        "Un atto: letto, fa nascere un magazzino.",

    # ---------------------------------------------------------- :94742 l'atto del campo
    (94742, '(Single-use) Readable deed used to build a farm.'):
        "Un atto: letto, fa nascere un campo.",

    # ---------------------------------------------------------- :95993 l'atto del negozio
    (95993, '(Single-use) Readable deed used to build a shop.'):
        "Un atto: letto, fa nascere un negozio.",

    # ---------------------------------------------------------- :96063 l'atto del museo
    (96063, '(Single-use) Readable deed used to build a museum.'):
        "Un atto: letto, fa nascere un museo.",

    # ---------------------------------------------------------- :96500 la pergamena della ricarica
    (96500, 'It is a scroll that when read, restore charges of certain items.'):
        "Ridà cariche a certi oggetti.",

    # ---------------------------------------------------------- :96785 l'atto dell'eredità
    (96785, "It is a deed of heirship. It grants you power to open the heir's trunk"):
        "Un atto: letto, apre la borsa dei ricordi.",

    # ---------------------------------------------------------- :96918 potenziamento armatura, superiore
    (96918, 'It is a scroll that when read, enhances your equipment, potent.'):
        "Potenzia un'armatura. È più forte del solito.",

    # ---------------------------------------------------------- :96989 potenziamento armatura
    (96989, 'It is a scroll that when read, enhances your equipment.'):
        "Una pergamena che potenzia un'armatura.",

    # ---------------------------------------------------------- :97060 potenziamento arma, superiore
    (97060, 'It is a scroll that when read, enhances your weapon, potent.'):
        "Potenzia un'arma. È più forte del solito.",

    # ---------------------------------------------------------- :97131 potenziamento arma
    (97131, 'It is a scroll that when read, enhances your weapon.'):
        "Una pergamena che potenzia un'arma.",

    # ---------------------------------------------------------- :97399 materiale superiore
    (97399, 'It is a scroll that when read, remodel a item with rare materials.'):
        "Cambia il materiale di un oggetto. È più forte del solito.",

    # ---------------------------------------------------------- :97470 cambio di materiale
    (97470, 'It is a scroll that when read, remodel a item with a different material.'):
        "Una pergamena che cambia il materiale di un oggetto.",

    # ---------------------------------------------------------- :97541 materiale inferiore
    (97541, 'It is a scroll that when read, remodel a item with commonplace materials.'):
        "Cambia il materiale di un oggetto. Di solito in peggio.",

    # ---------------------------------------------------------- :99028 la pergamena dell'alleato
    (99028, 'It is a scroll that when read, summons a friendly character to join you.'):
        "Chiama una creatura amichevole che si unisce a te.",

    # ---------------------------------------------------------- :102253 la pergamena della fede
    (102253, 'It is a scroll that when read, deepens your faith.'):
        "Una pergamena che fa crescere la Fede.",

    # ---------------------------------------------------------- :102324 la pergamena della crescita
    (102324, 'It is a scroll that when read, raises your skill potential.'):
        "Alza il potenziale di un'abilità.",

    # ---------------------------------------------------------- :103579 la pergamena della scoperta
    (103579, 'It is a scroll that when read, detects and marks nearby objects.'):
        "Una pergamena che scopre le cose qui attorno.",

    # ---------------------------------------------------------- :104449 la pergamena della conoscenza
    (104449, 'It is a scroll that when read, enhances reading capabilities temporarily.'):
        "Per un po', rende più facile leggere i libri.",

    # ---------------------------------------------------------- :104666 la pergamena dei materiali
    (104666, 'It is a scroll that when read, grants you miscellaneous materials.'):
        "Una pergamena che fa ottenere dei materiali.",

    # ---------------------------------------------------------- :105016 la pergamena del mana
    (105016, 'It is a scroll that when read, restores your MP.'):
        "Una pergamena che ridà MP.",

    # ---------------------------------------------------------- :105087 la pioggia santa
    (105087, 'It is a scroll that when read, removes all curses cast on you.'):
        "Toglie di dosso tutte le maledizioni.",

    # ---------------------------------------------------------- :105158 la luce santa
    (105158, 'It is a scroll that when read, removes 1 curses cast on you.'):
        "Toglie di dosso una maledizione.",

    # ---------------------------------------------------------- :105455 il velo santo
    (105455, 'It is a scroll that when read, dispels curses temporarily.'):
        "Per un po', dà resistenza alle maledizioni.",

    # ---------------------------------------------------------- :106984 dissolvi maledizione
    (106984, 'It is a scroll that when read, removes curses from equipments. Potent.'):
        "Toglie la maledizione a un oggetto. È più forte del solito.",

    # ---------------------------------------------------------- :107055 identificazione superiore
    (107055, 'It is a scroll that when read, identifies unknown items. Potent.'):
        "Identifica gli oggetti ignoti. È più forte del solito.",

    # ---------------------------------------------------------- :108330 l'atto della casa
    (108330, '(Single-use) Readable deed used to build your own house.'):
        "Un atto: letto, fa nascere una casa.",

    # ---------------------------------------------------------- :111924 la pergamena della maledizione
    (111924, 'It is a scroll that when read, curses an item in your possession.'):
        "Una pergamena che maledice un oggetto.",

    # ---------------------------------------------------------- :114862 teletrasporto breve
    (114862, 'It is a scroll that when read, teleports you for a short distance.'):
        "Una pergamena che teletrasporta poco lontano.",

    # ---------------------------------------------------------- :114933 la pergamena del prodigio
    (114933, 'It is a scroll that when read, grants you magical knowledge.'):
        "Una pergamena che dà conoscenza magica.",

    # ---------------------------------------------------------- :115004 la pergamena del talento
    (115004, 'It is a scroll that when read, grants you profession skills.'):
        "Dà un'abilità che non si ha ancora.",

    # ---------------------------------------------------------- :115075 la mappa magica
    (115075, 'It is a scroll that when read, reveal undiscovered regions nearby.'):
        "Svela le parti del sotterraneo non ancora esplorate.",

    # ---------------------------------------------------------- :115456 la pergamena del ritorno
    (115456, 'It is a scroll that when read, teleports you to specified location.'):
        "Fra qualche turno porta in un luogo scelto. Rileggerla annulla.",

    # ---------------------------------------------------------- :117259 togli maledizione
    (117259, 'It is a scroll that when read, removes curses from your equipment.'):
        "Una pergamena che toglie la maledizione a un oggetto.",

    # ---------------------------------------------------------- :130104 la pergamena dell'incognito
    (130104, 'It is a scroll that when read, reset memories of hostile situations.'):
        "Azzera le ostilità, tranne quelle dei mostri.",

    # ---------------------------------------------------------- :130175 il teletrasporto
    (130175, 'It is a scroll that when read, teleports you for a distance.'):
        "Una pergamena che teletrasporta a caso.",

    # ---------------------------------------------------------- :130246 la pergamena dell'oracolo
    (130246, 'It is a scroll that when read, reveal locations of powerful artifacts.'):
        "Dice dove sono finiti gli artefatti già apparsi.",

    # ---------------------------------------------------------- :130317 l'identificazione
    (130317, 'It is a scroll that when read, identifies unknown items.'):
        "Una pergamena che identifica gli oggetti che si portano.",
}
