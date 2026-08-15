import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # Dare un nome a un alleato (:7460-:7471)
    # ================================================================
    # ⚠️ him(tc) e' morfologia e sparisce: niente funzioni di contenuto, quindi
    #    niente «chiamarlo». L'inglese finisce con uno spazio (e' un prompt).
    (7460, 'What do you want to call ? '): '"Che nome vuoi usare? "',
    (7466, 'You changed your mind.'): 'Hai cambiato idea.',
    (7471, 'You named  .'):
        '"D\'ora in poi si chiamerà " + cdatan(CDATAN_NAME, tc) + "."',

    # ================================================================
    # Il menu del tono di voce (:7493-:7563)
    # ================================================================
    (7493, 'Default Tone'): 'Tono predefinito',
    (7505, 'Tone of Voice'): 'Elenco dei toni',
    # ⚠️ Finestra da 500 px -> tetto 55 caratteri; strhint2 (14) piu' strhint3
    #    (20) ne mangiano 34, quindi qui ce ne stanno 21. Questa ne fa 20.
    # 💡 «Invio» e non «Conferma»: nella riga di aiuto il primo pezzo e' il
    #    TASTO, come «Cursore [Scegli]», «Shift,Esc [Chiudi]», «p [Ritratto]»,
    #    e text.hsp:117 rende gia' 「決定、」 con «Invio,».
    (7505, 'Enter [Change Tone] '): 'Invio [cambia tono] ',
    (7513, 'Title'): 'Titolo',
    # ⚠️ is(tc) e' morfologia: resta `name`, e la frase va in terza persona.
    (7563, '  somewhat different.'):
        'name(tc) + " parla in un modo un po\' diverso."',

    # ================================================================
    # L'evocazione dei PNG personalizzati (:7608-:7799)
    # ⭐ «Custom NPC» e' gia' «PNG personalizzato»: command.hsp:17535.
    # ================================================================
    # ⚠️ L'inglese dice «Check which CNPC?»; il giapponese chiede chi si
    #    desidera EVOCARE, che e' quel che succede davvero.
    (7608, 'Check which CNPC?'): 'Chi desideri evocare?',
    (7615, 'Custom NPC'): 'PNG personalizzati',
    # ⚠️⚠️ Qui il tetto lo sfora gia' l'inglese: coda da 46 caratteri
    #    (strhint2 14 + strhint3 20 + «* [Eq-Lvl] » 12, quest'ultimo fuori da
    #    ogni lang()), totale inglese 59 su 55. Questa resa e' di DUE caratteri
    #    piu' corta dell'inglese. Vedi il docstring.
    # ⚠️ E «[Details]» e' sbagliato: il giapponese dice 「召喚」, e il tasto evoca.
    (7615, 'Enter [Details] '): 'Invio [evoca] ',
    # ⚠️ Colonna stretta: display_topic a wx+328 su una finestra da 500.
    (7625, 'Level(Piety Cost)'): 'Liv. (devozione)',
    # ⭐ Espressione IDENTICA a un pezzo di action.hsp:12722, gia' reso
    #    «Devozione: ». Non c'era niente da scegliere.
    (7626, 'Piety: /'):
        '"Devozione: " + cdata(CDATA_PIETY, CHARA_PLAYER) + "/" + '
        'sdata(SKILL_NORMAL_FAITH, CHARA_PLAYER) * 100',
    (7628, 'Level'): 'Livello',
    # ⚠️⚠️ La trappola di variabili_en.py: `s` porta sei aggettivi inglesi nudi
    #    da :7716-:7721. La resa segue il giapponese, che non nomina niente —
    #    come la 38a per `studybuddy`. Vedi il docstring.
    (7724, 'A  is summoned from another world!'):
        '"Qualcosa di un altro mondo è stato evocato!"',
    (7755, 'You need to be more pious to let the being pass through the dimensional barrier.'):
        'Per farlo passare attraverso il muro dimensionale serve più devozione.',
    (7759, 'You need more experience to let the being pass through the dimensional barrier.'):
        'Per farlo passare attraverso il muro dimensionale serve più esperienza.',
    (7769, '[CNPC Summon] What do you want to do?'):
        '[Evoca PNG] Che cosa vuoi fare?',
    # ⭐ La rete 3 ha parlato e aveva ragione: 「足りないんよ」 e' gia' reso «Non
    #    bastano!» in action.hsp:14356, che e' il rifiuto di YACATECT quando i
    #    suoi punti non bastano (GDATA_FLAG_YACA_POINTS). Stessa frase, stessa
    #    scena — non si compra — e lo stesso dialetto in giapponese.
    (7784, 'Not enough!'): 'Non bastano!',
    (7799, 'A custom NPC has been successfully summoned from another world!'):
        'Un PNG personalizzato è arrivato da un altro mondo!',

    # ================================================================
    # La creatura che si agita (:7818-:7828)
    # ⚠️ Stesso giapponese, due inglesi: la rete 4 pretende una resa sola, e ha
    #    ragione — a distinguere i tre rami e' CDATA_RELATION, non il testo.
    # ================================================================
    (7818, ' is excited!'):
        'cdatan(CDATAN_NAME, rc) + " si infuria e ti salta addosso."',
    (7828, ' is confused and attacks you.'):
        'cdatan(CDATAN_NAME, rc) + " si infuria e ti salta addosso."',
}
