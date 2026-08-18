import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :751 la guida di Norne. ⚠️ Questa firma serve anche :783, :981-:994,
    #     :1006, :1010 e :1015: la resa deve reggere in tutti e sei i posti.
    (751, "Don't show"): 'No',
    (751, 'Show'): 'Sì',

    # --- :755 i PNG neutrali. 「しない」 vuol dire «non ignorare», cioe'
    #     attaccare: il giapponese nega la voce, l'inglese dice l'atto.
    (755, 'Attack'): 'Attacca',
    (755, 'Ignore'): 'Ignora',

    # --- :759 il tasto z.
    (759, 'Quick menu'): 'Menu rapido',
    (759, 'Zap'): 'Agita',
    (759, "Don't assign"): 'Nessuno',

    # --- :763 il tasto x.
    (763, 'Quick Inv'): 'Zaino rapido',
    (763, 'Identify'): 'Identifica',

    # --- :767 i passi prima di correre: 「走らない」 e' il valore 20, cioe' mai.
    (768, "Don't run"): 'Mai',
    # ⚠️ Dinamica: il numero e' `cfg_startrun + 1` e arriva a 20 — «Dopo 20
    #    passi» sta in 13 caratteri. L'inglese scrive «After 3 steps».
    (772, 'After  steps'): '"Dopo " + (cfg_startrun + 1) + " passi"',

    # --- :783 le statistiche della scheda. Il primo valore e' la firma di :751.
    (783, 'Show'): 'In parte',
    (783, 'Show Max'): 'Tutte',

    # --- :787 la voce «Attacca» nel menu di chi si punta.
    (787, 'Show'): 'Sempre',
    (787, 'Neutral'): 'Non alleati',
    (787, "Don't show"): 'Mai',

    # --- :791 lo sterco.
    (791, 'No Block'): 'No',
    (791, 'Block'): 'Sì',

    # --- :795 l'animazione delle mosse di barra. ⚠️ Il primo valore (全表示 /
    #     «Show») ha la stessa firma di :787 e sta li': «Sempre» deve reggere
    #     tutt'e due i posti, e per questo qui il secondo e' «Mai» e non «No».
    (795, "Don't show"): 'Mai',

    # --- :799 la domanda sul riordino dei punti di viaggio.
    (799, 'Confirm'): 'Chiedi',
    (799, "Don't Use"): 'Non chiedere',

    # --- :805 e :809 i driver audio. I nomi restano: sono quelli che si
    #     scrivono in config.txt, e MCI accanto a loro non e' nemmeno in lang().
    (805, 'None'): 'Nessuno',
    (805, 'Direct sound'): 'Direct sound',
    (809, 'Direct music'): 'Direct music',

    # --- :813 il modo schermo.
    (813, 'Window mode'): 'Finestra',
    (813, 'Full screen'): 'Schermo intero',

    # --- :823 la coppia generica しない/する. ⚠️ Serve dieci righe: :823, :827,
    #     :831, :861, :865, :869, :878, :890, :898, :902.
    (823, 'No'): 'No',
    (823, 'Yes'): 'Sì',

    # --- :835 il battito cardiaco.
    (835, "Don't play"): 'No',
    (835, 'Play'): 'Sì',

    # --- :839 l'animazione degli attacchi.
    (839, 'No'): 'Nessuna',
    (839, 'Only PC'): 'Solo tu',
    (839, 'Only Ally'): 'Solo alleati',
    (839, 'All'): 'Tutti',

    # --- :843 gli effetti del tempo.
    (843, 'No animation'): 'Nessuna',
    (843, 'Always'): 'Sempre',

    # --- :847 la qualita' delle luci.
    (847, 'High'): 'Alta',
    (847, 'Low'): 'Bassa',

    # --- :851 le ombre degli oggetti: il giapponese mette la ragione fra
    #     parentesi, e la resa la tiene.
    (851, 'No(Fast)'): 'No (veloce)',
    (851, 'Yes(Slow)'): 'Sì (lento)',

    # --- :855 la dimensione del PCC.
    (855, 'Full-size'): 'Originale',
    (855, 'Reduced'): 'Ridotta',

    # --- :882 l'acqua nel titolo.
    (882, 'No'): 'No',
    (882, 'Yes'): 'Sì',

    # --- :894 il turno automatico. 「省略」 e' «si salta», non «piu' veloce di
    #     tutte»: la resa dice il fatto e tiene la scala.
    (894, 'Normal'): 'Normale',
    (894, 'High'): 'Veloce',
    (894, 'Highest'): 'Immediato',

    # --- :902 il danno nel registro, terzo valore. 吊るし e' il gancio a cui si
    #     appende una creatura (CHARA_BIT_SANDBAG), non il sacco da boxe.
    (902, 'Sandbag'): 'Solo al gancio',

    # --- :911 il gamepad.
    (911, "Don't use"): 'No',
    (911, 'Use'): 'Sì',

    # --- :916 e :919 i tasti del gamepad. ⚠️ «Tasto » porta lo spazio perche'
    #     il numero si attacca subito dopo: `mes lang(...) + list(1, cnt)`.
    (916, 'Unassigned'): 'Non assegnato',
    (919, 'Button'): 'Tasto ',

    # --- :925 la coppia 非表示/表示. Serve :925, :932, :936, :940.
    (925, 'No'): 'No',
    (925, 'Yes'): 'Sì',

    # --- :944 i cinque modi di scrivere i nomi degli oggetti. Qui l'inglese sa
    #     di piu': il giapponese dice 「表示」 cinque volte.
    (944, 'Capitalize'): 'Iniziali',
    (944, 'Uppercase'): 'MAIUSCOLO',
    (944, 'Lowercase'): 'minuscolo',
    (944, 'Spongebob'): 'Spongebob',
    (944, 'Schizophrenic'): 'Schizofrenico',

    # --- :956 la raccolta automatica.
    (956, 'Disable'): 'No',
    (956, 'Enable'): 'Sì',

    # --- :960 la coppia なし/あり dei suoni. Serve :960, :964, :968.
    (960, 'Off'): 'No',
    (960, 'On'): 'Sì',

    # --- :977 i numeri di danno.
    (977, 'Off'): 'No',
    (977, 'On'): 'Sì',

    # --- :1006 i nomi dei PNG. «Tutti in citta'» ha 15 caratteri esatti dopo la
    #     degradazione, cioe' il tetto: l'inglese qui ne ha 16 e sfora.
    (1006, 'Show in Town'): 'In città',
    (1006, 'Show All in Town'): 'Tutti in città',
    (1006, 'Show All'): 'Tutti',

    # --- :1010 la barra HP. Il gioco distingue le bestie del giocatore dagli
    #     alleati in genere: `cfg_showPetHealth` vale 1 per le prime, 2 per tutti.
    (1010, 'Show pet'): 'Bestie',
    (1010, 'Show allies'): 'Alleati',

    # --- :1017 e :1021 i due suffissi numerici: il numero sta davanti.
    (1017, ' rows'): ' righe',
    (1021, ' turns'): ' turni',

    # --- :1038 e :1046 le due note in fondo al pannello, carattere piu' piccolo
    #     e 54 caratteri per riga.
    (1038, 'Items marked with * require a restart to apply changes.'):
        'Le voci con * si applicano dopo il riavvio del gioco.',
    # ⚠️ Tre righe come il giapponese, non due come l'inglese: la terza dice a
    #    che cosa servono i suffissi (L) e (R), che altrimenti non si spiegano.
    (1046, 'To assign a button, move the cursor to\\nan item and press the button.'):
        'Per assegnare un tasto, scegli la voce e premi\\n'
        'il tasto sul gamepad. Le voci con (L) e (R)\\n'
        'servono a cambiare linguetta nei menu.',
}
