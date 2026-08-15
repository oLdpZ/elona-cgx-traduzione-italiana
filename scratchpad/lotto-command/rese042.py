import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # Il diario (:3120)
    # ⭐ 「ジャーナル」 e' «diario» in action.hsp:8282, chara_func.hsp:3964,
    #    command.hsp:6869, map.hsp:1197, proc.hsp:4228 e text.hsp:4.
    # ================================================================
    (3120, 'Journal'):
        'Diario',

    # ================================================================
    # La bacheca degli incarichi (:3290-:3425)
    # ⭐ 依頼 e' «Incarico» (text.hsp:11875), 依頼人 «cliente» (:11877),
    #    掲示板 «bacheca» (db_item.hsp:151223).
    # ================================================================
    (3290, 'It seems there are no new notices.'):
        'Non sembra ci siano incarichi nuovi in bacheca.',
    (3320, 'Notice Board'):
        'Incarichi in bacheca',
    # 💡 Due invariati: sono simboli, e il passo della colonna e' 13 px (:3391).
    (3392, '$'):
        '$',
    (3397, '$ x '):
        '$ x ',
    (3425, 'Do you want to meet the client?'):
        'Vuoi incontrare il cliente?',

    # ================================================================
    # L'elenco dei PNG e dei candidati (:3543-:3677)
    # ⭐ NPC e' «PNG» (:7615). Intestazioni a corpo 11 (display_topic) piu' 26 px
    #    d'icona: «Informazioni» ha 17 caratteri, la terza colonna ne ha 21.
    # ================================================================
    (3543, 'NPC List'):
        'Elenco dei PNG',
    (3546, 'Chara List'):
        'Elenco dei candidati',
    (3550, 'Wage'):
        'Paga',
    (3553, 'Init. Cost(Wage)'):
        'Assunzione (paga)',
    # ⭐ ガードブレイク e' «Rottura guardia» in skill.hsp:957 e :1789.
    (3559, 'GuardBreak'):
        'Rottura guardia',
    # ⭐ 出血 come stato e' «Sanguinamento» (:1888).
    (3562, 'Bleeding Lv'):
        'Sanguinamento',
    (3565, 'Name'):
        'Nome',
    (3568, 'Name'):
        'Nome',
    # ⭐ Stesso giapponese di :6147, gia' reso «Informazioni»: la rete 3 lo
    #    pretende, e i 17 caratteri di colonna ci stanno.
    (3570, 'Info'):
        'Informazioni',
    # 💡 Riga a corpo 12: «Hp:100%» + «/contrasto/» (:1356) + questa fa 39
    #    caratteri sui 44 fra wx+372 e il bordo. L'inglese ne fa 33.
    (3627, ' GuardBreak:%'):
        '" Rottura guardia:" + cdata(CDATA_GUARD_BREAK, i) + "%"',
    # ⚠️ Due invariati, e non per pigrizia: la riga dell'eta' vive in 19
    #    caratteri fra wx+372 e wx+512, e «Lv.100 female?(999)» ne fa gia' 19.
    #    « anni)» ne costerebbe cinque che non ci sono.
    (3634, '('):
        '(',
    (3634, ')'):
        ')',
    # ⭐ Non e' mai una chiave: :4656 la usa come etichetta, ma la scelta 5
    #    scrive lang("なし", "none"). Ed e' gia' resa «sconosciuto» in
    #    init.hsp:2082, dove gendername() la restituisce.
    (3643, 'unknown'):
        'sconosciuto',
    # ⭐ Stesso giapponese di text.hsp:193 (« gold» -> « oro»): si ricopia, e lo
    #    spazio davanti serve, perche' :3677 concatena senza.
    (3677, 'gp'):
        ' oro',

    # ================================================================
    # Le prenotazioni in libreria (:3739-:3807)
    # ⭐ 予約 e' «Prenota» in text.hsp:135 e «prenotare» in :13924.
    # ================================================================
    (3739, 'Reserve List'):
        'Prenotazioni',
    (3741, 'Name'):
        'Nome',
    (3742, 'Status'):
        'Stato',
    # 💡 L'inglese mette un trattino, il giapponese dice 「入荷なし」/「入荷予定」:
    #    la colonna ha 18 caratteri e la distinzione ci sta per intero.
    (3777, '-'):
        'Non prenotato',
    (3781, 'Reserved'):
        'Prenotato',
    (3807, 'Ah, that book is unavailable.'):
        'Ah, quel libro non si trova.',

    # ================================================================
    # Il jukebox (:3843-:3845)
    # 💡 L'inglese dice «Name», il giapponese 「タイトル」: e' il titolo di un brano.
    # ================================================================
    (3843, 'Playlist'):
        'Elenco dei brani',
    (3845, 'Name'):
        'Titolo',
}
