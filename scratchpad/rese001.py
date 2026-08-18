import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :433 il primo, e vale fuori da ogni struttura. 旅経験 e' «esperienza
    #     di viaggio» da main.hsp:8475, che e' la finestra di conferma di
    #     questa stessa voce: li' c'e' spazio per la frase intera, qui no.
    (433, 'Organize and share travelExp'): 'Ordina i punti di viaggio',

    # --- :443-:457 il negozio. Sette voci, e sono quelle che vivono nel
    #     riquadro largo 330: nessuna ne ha avuto bisogno.
    # 💡 仲間に…頼む e' «chiedere a un compagno», non «assumere uno sconosciuto».
    (443, 'Assign a shopkeeper'): 'Metti un compagno al negozio',
    # ⚠️ La lang() e' il solo «Extend»: il « (N GP)» sta FUORI, concatenato dopo
    #    (`:445`). Una resa lunga qui sfora il riquadro senza che il dizionario
    #    lo veda, perche' la rete misura la lang() e non la riga.
    (445, 'Extend'): 'Ingrandisci',
    (447, 'Change shop type'): 'Cambia tipo di negozio',
    # ⚠️ dinamica: `kunren` e' il costo, e vale 1000000 quando il negoziante non
    #    ha la trattativa — sette cifre. Con la resa corta ci stanno lo stesso.
    (450, 'Train shopkeeper for  bronze coins'):
        '"Addestra (" + kunren + " di bronzo)"',
    (454, 'Get shopkeeper feat'): 'Prendi il talento da negozio',
    # 💡 Porta al menu di text.hsp:1646, gia' reso «15 al giorno (Esp. Trattativa+)».
    (456, 'Limit sales per day'): 'Limita le vendite al giorno',
    # ⚠️ 未実装 / «Unimplemented»: la voce c'e' e non fa niente. Va detto, o
    #    chi gioca la prova ogni volta.
    (457, 'Hire part time worker (Unimplemented)'): 'Assumi un aiuto (non attivo)',

    # --- :460-:474 l'allevamento.
    (460, 'Assign a breeder'): 'Nomina un allevatore',
    # 💡 Il giapponese sposta 家畜・ブリーダー, tutt'e due; l'inglese dimentica
    #    gli allevatori.
    (461, 'Move a livestock'): 'Sposta bestiame e allevatori',
    # 💡 L'azione e' 餌を撒く, «spargere il mangime»; il consumo e' la nota fra
    #    parentesi, ed e' l'unica cosa che l'inglese tiene.
    (462, 'Consume livestock feed'): 'Spargi il mangime',
    (463, 'Consume disinfectant'): 'Disinfetta i locali',
    # ⚠️ Le due coppie: in giapponese cambia una parola sola (発動 / 解除), e in
    #    italiano cambia una lettera. Due voci opposte devono somigliarsi.
    #    Si perde コード, «codice»: «Attiva il codice antiriproduzione» fa 33.
    (465, 'Activate breeding-prevent code'): 'Blocca la riproduzione',
    (468, 'Cancel breeding-prevent code'): 'Sblocca la riproduzione',
    (471, 'Activate production-prevent code'): 'Blocca la produzione',
    (474, 'Cancel production-prevent code'): 'Sblocca la produzione',

    # --- :478-:481 il campo di prigionia. «rinchiudere» e «prigioniero» sono
    #     di command.hsp:1196-:1197 e adv.hsp:197; «Energia da Lavoro» di
    #     map.hsp:12281.
    (478, 'Contain a inmate'): 'Rinchiudi un prigioniero',
    (479, 'Move a inmate'): 'Sposta un prigioniero',
    # 💡 Porta al menu di text.hsp:2213, dove 強度N e' gia' «<Livello N>».
    (480, 'Change Toil-Lv'): 'Cambia il livello di lavoro',
    (481, 'Exchange Toil-Energy'): "Scambia l'Energia da Lavoro",

    # --- :484-:504 la casa.
    (484, 'Release ally'): 'Libera un compagno',
    (485, 'Move a stayer'): 'Sposta un ospite',
    (487, 'Design'): 'Ridecora la casa',
    # ⚠️ Il giapponese dice 家の情報, «informazioni»; l'inglese «Home rank». La
    #    schermata mostra il rango dentro le informazioni: si tiene la piu' larga.
    (489, 'Home rank'): 'Informazioni sulla casa',
    (490, 'Allies in your home'): 'Compagni in casa',
    (492, 'Recruit a servant'): 'Assumi un domestico',
    (499, 'Change door type'): 'Cambia tipo di porta',
    (500, 'Change tile group'): 'Cambia gruppo di piastrelle',
    (501, 'Change Map Icon'): "Cambia l'aspetto esterno",
    (504, 'Change Map Name'): 'Cambia nome alla struttura',
    # ⚠️ :507 e` scritta nella forma ESPANSA della macro — `promptl(0, promptmax)
    #    = lang(...)` invece di `promptAdd lang(...)` — ed e` la trentatreesima
    #    voce dello stesso riquadro. La rete 5 non la vedeva: e` stata questa
    #    riga a farlo scoprire, ed erano 37 righe in sette file.
    # 💡 お片付け e` mettere in ordine, non raccogliere il raccolto: «riordino»
    #    la tiene distinta da «Raccogli il prodotto» due voci piu` sotto.
    (507, 'Collecting function'): 'Funzione di riordino',

    # --- :514-:515 il campo.
    (514, 'Plant seeds'): 'Pianta dei semi',
    (515, 'Collect yield'): 'Raccogli il prodotto',
}
