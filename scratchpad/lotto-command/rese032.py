import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # *show_weaponStat / *com_skill_calcAttack — le righe d'attacco
    # ================================================================
    # ⚠️ Colonna da 46 px = 6,4 caratteri (:12429 contro :12452). Tutte e tre
    #    divergono dalla rete 3, e tutte e tre perche' il sito che cita e' un
    #    altro mestiere. Vedi il docstring.
    #
    # 武器: si concatena con p(1), quindi a schermo esce «Arma1», «Arma2».
    #    text.hsp:59 ha «armi» perche' li' e' la CATEGORIA d'inventario; qui
    #    etichetta una singola arma, e il plurale sarebbe sbagliato.
    (12402, 'Melee'): 'Arma',
    # 格闘: skill.hsp:161 ha «Arti marziali» perche' li' e' il NOME
    #    dell'abilita'; tredici caratteri in una colonna da sei.
    (12408, 'Unarmed'): 'Lotta',
    # ⭐ 射撃 e 命中 insieme: la coppia l'ha gia' decisa buff.hsp:679
    #    (「射撃力上昇/命中率上昇」 -> «Tiro e mira»), e skill.hsp:1277 conferma
    #    「命中率上昇」 -> «+mira».
    (12414, 'Dist'): 'Tiro',
    (12428, 'Hit'): 'Mira',

    # ================================================================
    # *show_weaponStat — i cinque avvisi sul peso dell'arma
    # ================================================================
    # ⚠️ Tutte e cinque al VERBO, non all'aggettivo: itemname(cw) puo' essere
    #    maschile o femminile e a scrittura non si sa. Vedi il docstring.
    (12478, ' fits well for two-hand fighting style.'):
        'itemname(cw) + " si impugna bene a due mani."',
    (12481, ' is too light for two-hand fighting style.'):
        'itemname(cw) + " pesa un po\' troppo poco per l\'uso a due mani."',
    # ⭐⭐ :12488 e :12495 hanno lo STESSO inglese e due giapponesi diversi.
    #    :12485 e' `if ( attacknum == 1 )`, cioe' l'arma della mano principale
    #    sopra i 4000; 「利手で扱うにも重すぎる」.
    (12488, ' is too heavy for two-wield fighting style.'):
        'itemname(cw) + " pesa troppo perfino per la mano dominante."',
    #    :12492 e' l'`else`, cioe' l'arma secondaria sopra i 1500;
    #    「片手で扱うには重すぎる」. La rete 11 autorizza: `itemname` di qua e di la'.
    (12495, ' is too heavy for two-wield fighting style.'):
        'itemname(cw) + " pesa troppo per una mano sola."',
    # ⚠️ «per usarla a cavallo» nasconderebbe un accordo dentro il pronome.
    (12505, ' is too heavy to use when riding.'):
        'itemname(cw) + " pesa troppo per l\'uso a cavallo."',

    # ================================================================
    # *com_wear — l'intestazione della finestra dell'equipaggiamento
    # ================================================================
    # ⚠️ text.hsp:59 ha 装備品 -> «equipaggiamento» minuscolo, perche' li' e'
    #    una voce di un elenco di categorie. Qui e' il TITOLO della finestra,
    #    e i titoli di questo file cominciano per maiuscola.
    (12618, 'Equipment'): 'Equipaggiamento',
    # 部位 e' la parte del corpo di bodyn (text.hsp:136), 名称 il nome
    #    dell'oggetto: la colonna li tiene tutt'e due.
    (12620, 'Category/Name'): 'Parte/Nome',
    (12622, 'Weight'): 'Peso',
    # ⚠️ La riga e' destra e il tetto e' 75 caratteri (module.hsp:4360, con
    #    ww = 690). L'inglese ci arriva; questa ne fa 62. Vedi il docstring.
    (12674, 'Equip weight: '): 'Peso equip.: ',
    (12674, ' Hit Bonus:'): ' Mira:',
    (12674, ' Damage Bonus:'): ' Danno:',
    # ⭐ Da bodyn (text.hsp:136, 手 -> «Mano»): 「利手」 prende il posto del nome
    #    della parte del corpo nella stessa colonna, larga 42 px.
    (12694, 'Hand*'): 'Mano*',
}
