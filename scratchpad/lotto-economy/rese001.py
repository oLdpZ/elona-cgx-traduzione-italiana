import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :64-:116 il prospetto della citta'.
    (64, 'City Chart'): 'Prospetto cittadino',
    (74, "There's no information in this area."):
        'Di questo posto non ci sono informazioni.',
    (83, ' City Chart'):
        '"Prospetto di " + mapname(adata(ADATA_ID, gdata(GDATA_AREA)))',
    # il posto vuoto nell'elenco delle cariche
    (116, 'Empty'): 'Vacante',

    # --- :285-:303 il giudizio dei cittadini, dal peggiore al migliore.
    #     Sono etichette di stato, quindi sostantivi: guida-stile.md.
    (285, '<Tax-Thief>'): '<Ladro di tasse>',
    (288, 'Disappointment'): 'Delusione',
    (291, 'No Voice Raised'): 'Perplessità',
    (294, 'No Opinion'): 'Indifferenza',
    (297, 'No Complaints'): 'Nessuna lamentela',
    (300, 'Role Model'): 'Modello di gestione',
    (303, '<the Hope of >'):
        '"<Speranza di " + mdatan(MDATAN_NAME) + ">"',

    # --- :309-:312 i tre titoletti del pannello.
    (309, 'Town Information'): 'Quadro generale',
    (310, 'Town Finance'): 'Finanze',
    (312, 'Administrator'): 'Amministratore',

    # --- :319-:365 le dodici righe del prospetto. ⚠️ L'etichetta e' imbottita a
    #     VENTI caratteri e il numero comincia sempre alla stessa colonna: e' un
    #     allineamento a mano. Niente accenti nelle etichette, o la degradazione
    #     ne aggiunge uno e la colonna si sposta.
    (319, 'Security           ()  '):
        '"Sicurezza          (" + mdata(MDATA_CITY_PROPERTY_VALUE) + ") " + s1 + " "',
    (323, 'Population           '):
        '"Popolazione         " + mdata(MDATA_MODERATE_CROWD) + " "',
    # ⚠️ 「今までの死者N人」 e' «N morti fino a oggi»; l'inglese scrive
    #    «(dead N people)», che si legge come un aggettivo.
    (327, 'Water pollution      (dead  people) '):
        '"Acque inquinate     " + mdata(MDATA_CITY_WATER_POLLUTION) '
        '+ " (morti finora: " + mdata(MDATA_CITY_DEAD_PEOPLE) + ") "',
    (331, 'Ether concentration  '):
        '"Etere nell\'aria     " + taiki + " "',
    (335, 'Tax                 % '):
        '"Tassa sui consumi   " + mdata(MDATA_CITY_TAXES) + "% "',
    (339, 'Tourism revenue      cgp '):
        '"Entrate dal turismo " + mdata(MDATA_CITY_TOURISM_REVENUE) + " cgp "',
    (343, 'Maintenance costs    cgp '):
        '"Costi di gestione   " + mdata(MDATA_CITY_MAINTENANCE_COST) + " cgp "',
    (347, 'Budget              gp '):
        '"Bilancio            " + mdata(MDATA_CITY_BUDGET) + "gp "',
    (353, 'Complaint            '):
        '"Lamentele           " + mdata(MDATA_CITY_COMPLAINTS) + " "',
    # ⚠️ «Influenza» e non «Autorita'»: un'etichetta con l'accento si allunga di
    #    un carattere dopo la degradazione e sposta la colonna.
    (357, 'Authority            '):
        '"Influenza           " + mdata(MDATA_CITY_AUTHORITY) + " "',
    (361, 'Approval rate       % '):
        '"Gradimento          " + imp + "% "',
    (365, 'Evaluation           '):
        '"Giudizio            " + s2 + " "',

    # --- :440-:441 le due leggi. Tetto 47 caratteri: la striscia della riga,
    #     non il bordo della finestra.
    # ⚠️ L'inglese perde il segno di percentuale che il giapponese ha: a schermo
    #    esce «...is 15.», un numero senza unita'.
    (440, 'The consumption tax of this town is .'):
        '"Qui la tassa sui consumi è del " + mdata(MDATA_CITY_TAXES) + "%."',
    (441, 'Allow murder in this town.'): 'Qui è permesso uccidere.',

    # --- :468-:475 le due colonne delle leggi. «Nazionale» sta nei cento pixel
    #     fra le due icone (wx+185 e wx+285, :471 e :474): quattordici caratteri.
    (468, 'Law'): 'Leggi',
    (472, 'Global'): 'Nazionale',
    (475, 'Law of '): '"Legge di " + mapname(gdata(GDATA_AREA))',

    # --- :636-:752 la costruzione degli edifici.
    (636, "The city can't hold any more building."):
        'Questa città non può ospitare altri edifici.',
    # ⚠️ Lo stesso giapponese e' gia' reso «Qui non si può costruire.» in
    #    map_user.hsp:60, e la resa si allinea: 「その場所」 e' «li'» piu' che
    #    «qui», ma per lo stesso giapponese due rese diverse sono un difetto
    #    piu' grosso della sfumatura che si guadagna.
    (643, "You can't build here."): 'Qui non si può costruire.',
    (652, 'This location is too far from the town.'):
        'Quel posto è troppo lontano dal centro abitato.',
    (686, 'What do you want to build?'): 'Che cosa vuoi costruire?',
    (689, 'Building List'): 'Elenco degli edifici',
    (746, "Your city can't afford it..."): 'Il bilancio non basta...',
    (752, 'You have built a !'):
        '"Hai costruito: " + bdrefn(p) + "!"',

    # --- :778 il bilancio in fondo alla finestra di costruzione.
    (778, 'Budget:'): 'Bilancio:',
}
