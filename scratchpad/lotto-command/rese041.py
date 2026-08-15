import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # L'oggetto che rotola ai piedi (:5015, :5096)
    # ⚠️ Stesso giapponese fra loro (rete 4) e con :4837 (rete 3): la resa e'
    #    gia' decisa e si ricopia. «from nowhere» e' un'aggiunta dell'inglese.
    # ================================================================
    (5015, ' appear.'):
        'itemname(ci) + " rotola fino ai tuoi piedi."',
    (5096, ' appear from nowhere.'):
        'itemname(ci) + " rotola fino ai tuoi piedi."',

    # ================================================================
    # Imparare e migliorare (:5068, :5072)
    # ⚠️ L'inglese non ha `name`: la resta resta in seconda persona, come lui.
    # ⭐ 「上達」 ha la sua forma in text.hsp:3205, «migliora in <abilita'>».
    # ================================================================
    (5068, 'You learn !'):
        '"Impari " + skillname(p) + "!"',
    (5072, 'Your  skill improves!'):
        '"Migliori in " + skillname(p) + "!"',

    # ================================================================
    # Le scorciatoie (:5201-:5241)
    # ⭐ 「ショートカット」 e' «Scorciatoia» in text.hsp:10 e :121.
    # 💡 Le due impossibilita' sono parallele nel sorgente e restano parallele.
    # ================================================================
    (5201, 'The key is unassigned.'):
        'Quel tasto non ha nessuna scorciatoia.',
    (5224, "You can't use this shortcut any more."):
        "Quell'azione non è più disponibile.",
    (5241, "You can't use that spell anymore."):
        'Quella magia non è più disponibile.',

    # ================================================================
    # Le direzioni (:5250, :5279, :5750, :5806)
    # ⭐ 「どの方向に…？」 e' «In che direzione vuoi …? » in proc.hsp:7607 e :7610.
    # ⚠️ Le prime tre finiscono con uno SPAZIO in inglese, e lo spazio resta:
    #    e' la giuntura col prompt (verifica.py:440).
    # ⭐ 体当たり e' «caricare»: action.hsp:1732 e :1740, «Carichi la porta».
    # ================================================================
    (5250, 'Which direction do you want to dig? '):
        'In che direzione vuoi scavare? ',
    (5279, 'Which direction do you want to bash? '):
        'In che direzione vuoi caricare? ',
    (5750, 'Which direction? '):
        'In che direzione? ',
    (5806, 'Choose the direction of the target.'):
        'In che direzione sta il bersaglio?',

    # ================================================================
    # Il menu delle capacita' (:5342-:5470) e quello ad area (:5552, :5673)
    # ⭐ 能力 e' «capacita'» in :6144 («Mostra le capacita'») e :7218; 広域 e'
    #    «in area» in skill.hsp:1913.
    # 💡 Corpo 11 (12 + sizefix - en * 2, con sizefix = 1): 6,6 px a carattere.
    #    display_topic spende 26 px per l'icona, quindi «Nome» ha 25 caratteri
    #    di spazio, «Costo» 11, «Effetto» 32.
    # ================================================================
    (5342, 'Skill'):
        'Capacità',
    (5344, 'Name'):
        'Nome',
    (5345, 'Cost'):
        'Costo',
    # ⭐ Stesso inglese di :10847, gia' reso «Effetto», e il giapponese qui dice
    #    proprio 「能力の効果」.
    (5346, 'Detail'):
        'Effetto',
    (5552, 'Wide Skill'):
        'Capacità ad area',

    # ⚠️ L'inglese dice «sealed», il giapponese 非表示: si NASCONDE, ed e' quel
    #    che fa il codice (`spact(p) = 2`). La riga di aiuto lo chiama gia'
    #    «[NASC.]» (text.hsp:122).
    (5457, 'Directly connected skills can not be sealed.'):
        "Le capacità legate a un'abilità non si possono nascondere.",
    # 💡 «Nascosta» concorda con «capacita'», non col nome che segue: sono tutte
    #    capacita', quindi l'accordo non dipende dalla voce.
    (5462, '[Hidden: ]'):
        '"[Nascosta: " + skillname(p) + "]"',
    (5470, '[Showing all skills]'):
        '[Mostrate tutte le capacità]',
    (5673, '[Showing all wide skills]'):
        '[Mostrate tutte le capacità ad area]',

    # ================================================================
    # Accorpare gli oggetti (:5725, :5730)
    # ⚠️ L'inglese dice «increasing», il giapponese 「低いほうにあわせて」: si
    #    allinea alla piu' BASSA. E' anche l'unica lettura che spiega il si'/no.
    # ================================================================
    (5725, 'Stack items of the same type and sort by increasing freshness and value?'):
        'Vuoi unire gli oggetti uguali, allineandoli alla freschezza e al valore più bassi?',
    # ⚠️ Onomatopea: spazio davanti e dietro come in inglese. Stessa forma di
    #    «*sbuffo*» e «*bau!*» della 27a.
    (5730, ' *rummage* '):
        ' *rovista* ',

    # ================================================================
    # I tentacoli e il menu di interazione (:5879, :5892)
    # ================================================================
    # ⚠️ rete 8: «su " + name» si fonderebbe con l'articolo. La frase gira sul
    #    complemento oggetto, che non vuole preposizione.
    (5879, 'Your tentacles attacked  against your will!'):
        '"I tuoi tentacoli si sono mossi da soli e hanno assalito " + name(tc) + "!"',
    # ⚠️⚠️ `him(tc)` a un argomento e' morfologia: funzioni di contenuto zero,
    #    quindi nessun nome, benche' il giapponese abbia `name(tc)`. Gemella di
    #    :14852. Voce dinamica -> espressione (rete 12).
    (5892, 'What action do you want to perform to ? '):
        '"Che cosa vuoi fare? "',
}
