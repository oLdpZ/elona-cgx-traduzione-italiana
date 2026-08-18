import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :39-:153 leggere un atto, costruire, traslocare.
    (39, 'Property No.  has been registered. ()'):
        '"Registrata la proprietà n. " + inv(INV_ITEM_PARAM2, ci) + " ("'
        ' + adata(ADATA_ARENA_WIN, gdata(GDATA_AREA)) + ")"',
    (48, 'You must read it inside a building to register your property.'):
        'Per registrare la proprietà, va letto dentro la struttura.',
    # 💡 Stesso inglese di action.hsp:14742, gia' reso: si copia.
    (54, 'You can only use it in the world map.'):
        'Si usa sulla mappa del mondo.',
    (60, "You can't build it here."): 'Qui non si può costruire.',
    (72, "You can't build a building anymore."):
        'Non puoi costruire altri edifici.',
    (77, 'Really build it here? '): 'Vuoi davvero costruire qui? ',
    (80, 'Really move it here? '): 'Vuoi davvero spostarlo qui? ',
    # 💡 La nona copia della stessa riga: action.hsp:12012 e altre otto.
    (91, 'You have learned a new ability, .'):
        '"Hai imparato una nuova capacità: " + skillname(SKILL_SPACT_MARKING) + "."',
    (111, "You've built a new house!"): 'Hai costruito una casa nuova! ',
    (130, "You've moved your house!"): 'Trasloco completato! ',
    (153, 'Property relocation finished!'): 'Spostamento completato! ',

    # --- :178-:227 gli otto edifici, e la frase che li nomina.
    # ⚠️ L'articolo lo porta il nome (contratto-nomi.md §4): scrivere
    #    «un " + s + "» reggerebbe solo finche' tutti sono maschili.
    # ⚠️ Non sono i nomi propri di text.hsp:2806 («My Museum» contro «museum»):
    #    li' e' il nome della proprieta' sulla mappa, qui un nome comune.
    (178, 'museum'): 'un museo',
    (184, 'camp'): 'un campo di prigionia',
    (190, 'shop'): 'un negozio',
    (196, 'crop'): 'un campo',
    (202, 'storage'): 'un magazzino',
    (209, 'ranch'): 'un allevamento',
    (216, 'dungeon'): 'un sotterraneo',
    (223, 'discarded ranch'): 'un allevamento abbandonato',
    (227, "You've built a !"): '"Hai costruito " + s + "!"',

    # --- :286-:321 il pannello della struttura.
    # 💡 Il giapponese dice «questo non e' casa tua», l'inglese il contrario
    #    dalla stessa parte. Si segue il giapponese, che e' la colonna che si
    #    legge accanto alla resa.
    (286, 'You can only use it in your home.'): 'Questa non è casa tua.',
    (306, 'There are  items and  furniture in .(Max: ) '):
        'mapname(gdata(GDATA_AREA)) + " contiene " + p + " oggetti e " + p(1)'
        ' + " mobili (al massimo " + p(2) + ") "',
    # ⚠️ L'inglese perde il conto dei prigionieri, che il giapponese ha e che le
    #    venti righe di sopra esistono solo per calcolare. Si segue il codice.
    (321, 'Current Toil-Lv is , Toil-Energy is .'):
        '"I prigionieri sono " + pet + ", il livello di lavoro è "'
        ' + adata(ADATA_LABOR_CAMP_TOIL_LEVEL, gdata(GDATA_AREA))'
        ' + " e l\'Energia da Lavoro accumulata è "'
        ' + adata(ADATA_LABOR_CAMP_TOIL_ENERGY, gdata(GDATA_AREA)) + "."',

    # --- :325-:359 il negozio. I nomi vengono dagli epiteti di text.hsp:424+,
    #     che il progetto ha gia' fissato: «del bazar», «della drogheria»,
    #     «della bottega magica», «dell'armeria», «della locanda».
    (325, 'Goods shop'): 'bazar',
    (328, 'Food shop'): 'drogheria',
    (331, 'Magic shop'): 'bottega magica',
    (334, 'Blacksmith'): 'armeria',
    (337, 'Inn shop'): 'locanda',
    (340, 'Decorative arts shop'): 'negozio di arredi',
    (343, 'Junk shop'): 'rigattiere',
    (345, 'Shop type: .'): '"Tipo di negozio: " + shops + "."',
    (347, 'No sale restrictions.'): 'Nessun limite di vendita.',
    (350, 'Sales limited to 15 items.'): 'Vendita limitata a 15 pezzi al giorno.',
    (353, 'Sales limited to 5 items.'): 'Vendita limitata a 5 pezzi al giorno.',
    (356, 'Current shopkeeper is .'):
        '"Il negoziante è " + cdatan(CDATAN_NAME, getworker(gdata(GDATA_AREA))) + "."',
    (359, "You haven't assigned a shopkeeper yet."):
        "Al momento non c'è nessun negoziante.",

    # --- :365-:405 la scala dei potenziali, due volte.
    # ⭐ Le prime tre parole le detta text.hsp:107, la scala delle resistenze,
    #    gia' resa «Suprema / Enorme / Ottima»: qui concordano con
    #    «potenziale», che e' maschile. Le altre quattro sono nuove.
    (365, '[Trade potential : Supreme]'): '[Potenziale trattativa: Supremo]',
    (368, '[Trade potential : Amazing]'): '[Potenziale trattativa: Enorme]',
    (371, '[Trade potential: Superb]'): '[Potenziale trattativa: Ottimo]',
    (374, '[Trade potential: Great]'): '[Potenziale trattativa: Notevole]',
    (377, '[Trade potential: Good]'): '[Potenziale trattativa: Buono]',
    (380, '[Trade potential: Bad]'): '[Potenziale trattativa: Scarso]',
    (383, '[Trade potential: Hopeless]'): '[Potenziale trattativa: Nullo]',
    (387, '[Charisma potential : Supreme]'): '[Potenziale carisma: Supremo]',
    (390, '[Charisma potential : Amazing]'): '[Potenziale carisma: Enorme]',
    (393, '[Charisma potential: Superb]'): '[Potenziale carisma: Ottimo]',
    (396, '[Charisma potential: Great]'): '[Potenziale carisma: Notevole]',
    (399, '[Charisma potential: Good]'): '[Potenziale carisma: Buono]',
    (402, '[Charisma potential: Bad]'): '[Potenziale carisma: Scarso]',
    (405, '[Charisma potential: Hopeless]'): '[Potenziale carisma: Nullo]',
    # 営業実績 e' il venduto accumulato dal negoziante.
    (407, '[Sales exp: ]'):
        '"[Vendite: " + cdata(CDATA_SALES_EXP, sc) + "]"',

    # --- :412-:431 l'allevamento, la casa, e la domanda che apre il menu.
    (412, 'Current breeder is .'):
        '"L\'allevatore è " + cdatan(CDATAN_NAME, getworker(gdata(GDATA_AREA))) + "."',
    (415, "You haven't assigned a breeder yet."):
        "Al momento non c'è nessun allevatore.",
    (428, ' members are staying at your home. (Max: ).'):
        '"In casa ci sono " + p + " ospiti (al massimo "'
        ' + (gdata(GDATA_HOME_LEVEL) + 2) + ")."',
    # 💡 Da command.hsp:17531, «[Personalizzazione] Che cosa vuoi fare?».
    (431, 'What do you want to do?'): 'Che cosa vuoi fare?',
}
