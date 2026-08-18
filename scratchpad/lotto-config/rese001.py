import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :580 il nome del pannello.
    (580, 'Option'): 'Opzioni',

    # --- :581 le nove sezioni. Riquadro da 370 e nessuna freccia: qui il tetto
    #     e' il bordo, non i 22 caratteri delle voci.
    (581, 'Game Setting'): 'Impostazioni di gioco',
    (581, 'Screen & Sound'): 'Schermo e audio',
    (581, 'Network Setting'): 'Impostazioni di rete',
    (581, 'Detailed Setting'): 'Impostazioni avanzate',
    (581, 'Game Pad'): 'Gamepad',
    (581, 'Message & Log'): 'Messaggi e registro',
    # ⚠️ Il giapponese scrive 言語(Language) apposta: chi ha sbagliato lingua non
    #    sa leggere l'etichetta, e la parola inglese e' il modo di ritrovarla.
    #    La resa tiene lo stesso servizio.
    (581, 'Language'): 'Lingua (Language)',
    (581, 'EX Setting 1'): 'Impostazioni extra 1',
    (581, 'EX Setting 2 (Display)'): 'Impostazioni extra 2 (schermo)',

    # --- :588 «Impostazioni di gioco», dodici voci. Tetto 22.
    (588, 'Extra Help'): 'Guida di Norne',
    (588, 'Neutral Npcs'): 'Ignora PNG neutrali',
    (588, 'Assign z key'): 'Assegna tasto z',
    (588, 'Assign x key'): 'Assegna tasto x',
    (588, 'Start Running After'): 'Passi prima di correre',
    (588, 'Walk Speed'): 'Velocità camminata',
    (588, 'Attack Interval'): 'Intervallo attacchi',
    # `cfg_record` accende la sezione « - Records of Adventure - » della scheda
    # (command.hsp:2951): livello piu' profondo, uccisioni, miglia, incarichi.
    (588, 'Record'): 'Mostra le statistiche',
    # La voce «Attacca» dentro il menu che si apre puntando qualcuno
    # (command.hsp:5954): si mostra sempre, solo sui non alleati, o mai.
    (588, 'Attack Select'): 'Opzione Attacca',
    (588, 'Block defecate generation'): 'Blocca lo sterco',
    (588, 'Gauge-Action Animation'): 'Animazione barra',
    # La domanda «vuoi mettere in ordine i punti di viaggio?» (main.hsp:8470).
    (588, 'TravelExp Confirmation'): 'Conferma riordino',

    # --- :594 «Schermo e audio», quattordici voci. Tetto 22.
    (594, 'Sound*'): 'Effetti sonori*',
    (594, 'Music*'): 'Musica*',
    (594, 'Screen Mode*'): 'Modo schermo*',
    (594, 'Screen Resolution*'): 'Risoluzione*',
    (594, 'High DPI Scaling*'): 'Scala DPI elevati*',
    (594, 'High DPI Smoothing*'): 'Smussatura DPI*',
    (594, 'Smooth Scroll'): 'Scorrimento fluido',
    (594, 'Always Center'): 'Centra sul giocatore',
    (594, 'Heartbeat Sound'): 'Battito cardiaco',
    (594, 'Attack Animation'): 'Animazione attacchi',
    (594, 'Weather Effect'): 'Effetti del tempo',
    # 光源の描写 e' il disegno delle sorgenti di luce, e i valori sono 高画質 /
    # 低画質: e' una scelta di qualita', non un interruttore.
    (594, 'Lighting'): 'Qualità delle luci',
    (594, 'Object Shadow'): 'Ombre degli oggetti',
    # I valori sono 原寸表示 / 縮小表示, cioe' due misure: PCC resta sigla.
    (594, 'PCC show'): 'Dimensione PCC',

    # --- :600 «Impostazioni di rete», tre voci. Tetto 22.
    (600, 'Use Network'): 'Usa la rete',
    (600, 'Constantly Connect'): 'Connessione periodica',
    (600, 'Filter Chat'): 'Filtra la chat',

    # --- :606 «Impostazioni avanzate», nove voci. Tetto 22.
    (606, 'Run Speed'): 'Velocità di corsa',
    (606, 'Auto Numlock'): 'Numlock automatico',
    (606, 'Title Water Effect'): 'Acqua nel titolo',
    (606, 'Screen Refresh'): 'Frequenza schermo',
    (606, 'Scroll When Run'): 'Scorrimento in corsa',
    (606, 'Auto Turn Speed'): 'Turno automatico',
    (606, 'Skip Random Events'): 'Eventi abbreviati',
    # ⚠️ `cfg_dhyouji` scrive «(37)» NEL REGISTRO (chara_func.hsp:6006). L'altra
    #    ダメージ表示, a :636, sono i numeri che volano sopra il bersaglio.
    (606, 'Damage show'): 'Danni nel registro',
    (606, 'Effect Speed'): 'Velocità effetti',

    # --- :612 «Gamepad», tredici voci. Tetto 22.
    #     La prima (ゲームパッド) ha la stessa firma di :581 e sta li'.
    (612, 'Enter/Ok'): 'Conferma',
    (612, 'Cancel'): 'Annulla',
    (612, 'Inventory'): 'Zaino',
    (612, 'Action'): 'Azione',
    (612, 'diagonal Move/(L)'): 'Diagonale (L)',
    (612, 'Pick/(R)'): 'Raccogli (R)',
    (612, 'Shoot/(R)'): 'Tiro (R)',
    (612, 'Target/(L)'): 'Bersaglio (L)',
    (612, 'Pause/Menu'): 'Menu di pausa',
    (612, 'Help'): 'Aiuto',
    (612, 'Chara-sheet'): 'Scheda',
    (612, 'Reload'): 'Ricarica',

    # --- :617/:618 «Messaggi e registro». ⚠️ Due delle sei voci sono nude e
    #     vogliono una toppa: vedi il docstring.
    (617, 'Message&Log'): 'Messaggi e registro',
    (618, 'Add time info'): 'Ora nel registro',
    # Il valore e' una percentuale (`cfg_msgtrans * 10 + " %"`, :929).
    (618, 'Transparency'): 'Trasparenza',
    (618, 'Disclaimer at startup'): "Avviso all'avvio",
    (618, 'Control Help*'): 'Guida ai comandi*',

    # --- :624 «Lingua». L'asterisco vuole il riavvio.
    (624, 'Language*'): 'Lingua*',

    # --- :630 «Impostazioni extra 1», cinque voci. Tetto 22.
    (630, 'Auto pickup & destroy'): 'Raccolta e distruzione',
    (630, 'Autopick sound'): 'Suono raccolta',
    (630, 'Autodestroy sound'): 'Suono distruzione',
    # MMAH e TCG sono sigle del mod e restano: nominano da dove viene la voce.
    (630, '(MMAH) Mouse Control'): '(MMAH) Mouse esteso',
    (630, '(TCG) Effect Speed'): '(TCG) Velocità',

    # --- :636 «Impostazioni extra 2 (schermo)», quattordici voci. Tetto 22.
    # ⚠️ Le tredici rientrate cominciano con DUE SPAZI normali, come l'inglese:
    #    il giapponese usa uno spazio a doppia larghezza (U+3000), che in CP932
    #    starebbe su due byte e la build inglese disegnerebbe due glifi.
    (636, 'Damage Popups'): 'Numeri di danno',
    (636, '  Hexes/Buffs'): '  Buff e malocchi',
    (636, '  Ailments'): '  Alterazioni',
    (636, '  Evade'): '  Schivate',
    (636, '  Chat'): '  Dialoghi',
    (636, '  Font Size'): '  Dim. carattere',
    (636, '  Font Shift'): '  Scarto carattere',
    # 表示速度 dice «velocita'», l'inglese «Duration»: e' il tempo che il numero
    # resta a schermo, e li' l'inglese e' quello giusto.
    (636, '  Display Duration'): '  Durata',
    (636, '  Show NPC Name'): '  Nomi dei PNG',
    (636, '  Show Pet HP gauge'): '  Barra HP bestie',
    (636, '  Show Damage Meter'): '  Misura danni',
    (636, '  Meter Duration Turns'): '  Turni misurati',
    (636, '  Extra UI Auto Hide'): '  Nascondi UI',
    (636, '  Multi-lined Name/Chat'): '  Nome/chat multiriga',

    # --- :681 l'intestazione della colonna, sopra l'elenco.
    (681, 'Menu'): 'Voce',
}
