import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :408-:413 gli edifici che si costruiscono in citta'.
    (408, 'Mine'):
        'Miniera',
    (409, 'Field'):
        'Campo',
    (410, 'Art Atelier'):
        "Bottega d'arte",
    (411, 'Temple'):
        'Tempio',
    # ⚠️ 盗賊 e' la stessa parola della «Gilda dei Ladri»: l'inglese ci ha messo
    #    un contrabbandiere
    (412, "Smuggler's Hideout"):
        'Covo dei ladri',
    (413, 'Light House'):
        'Faro',

    # --- :1573 il tempo che resta, in testa a ogni messaggio dell'incarico.
    (1573, '( min left) '):
        '"(restano " + (gdata(GDATA_TIME_LIMIT) + 1) + " min) "',

    # --- :1813-:1822 e :1973: i nove valori di CDATAN_NEWSEX sono RINVIATI,
    #     non resi. Stanno tutti dentro un confronto e la rete 7 li ferma; e
    #     sono scritti nel salvataggio, quindi tradurli lo romperebbe. Vedi
    #     `rinviate003.py` e `invariati.md`, sezione «Valori di dato».

    # --- :1959-:1974 i cinque possessivi di his(x, 1).
    # ⚠️ l'italiano accorda col POSSEDUTO, non col possessore: «il suo» copre
    #    tutti e quattro i generi, e il «?» segnerebbe un dubbio su una
    #    distinzione che l'italiano non fa. L'articolo ci vuole: i tre siti che
    #    la usano gia' dicono «succhi il suo sangue», «interrompe il suo daffare»
    (1959, 'your'):
        'il tuo',
    (1965, 'his'):
        'il suo',
    (1968, 'his?'):
        'il suo',
    (1971, 'her'):
        'il suo',
    (1974, 'her?'):
        'il suo',

    # --- :2082 il genere di chi non ne ha uno dichiarato.
    # ⭐ copiata da text.hsp:363, stessa firma: applica.py e' per file
    (2082, 'unknown'):
        'sconosciuto',

    # --- :2225-:2235 i separatori di data e orologio, che testo non sono.
    (2225, ' ', '年'):
        ' ',
    # la barra non e' ambigua: un solo giapponese, chiave corta
    (2225, '/'):
        '/',
    (2225, ' ', '日'):
        ' ',
    (2227, 'h'):
        'h',
    (2235, ':', '時間'):
        ':',
    (2235, ':', '分'):
        ':',
    # ✅ l'unico dei sette che cambia: l'italiano abbrevia in minuscolo
    (2235, ' Sec'):
        ' sec',

    # --- :2555-:2556 la testa del registro dei messaggi.
    (2555, '<Message Log>'):
        '<Registro dei messaggi>',
    (2556, 'Past 20 message lines are logged.'):
        'Qui compaiono le ultime 20 righe di messaggi.',

    # --- :2873 il paragrafo che il gioco scrive in error.txt quando muore.
    (2873, '\\n\\nPlease check and organize the information as to what kind of thing you were '
           'doing when the error occurred, if it is reproducible, screenshot showing the '
           'problem, comparison of the results from the vanilla version. In addition, if you '
           'can use the bug reporting template on the Elona board development thread, it would '
           'help identify the cause and will be saved for reference. There is little chance it '
           'will be solved if you provide very little information or just the error code.'):
        "\\n\\nControlla e metti in ordine le informazioni: che cosa stavi facendo quando è "
        "comparso l'errore, se il problema si ripete, uno screenshot che mostri la "
        "situazione, il confronto con la versione originale. Poi, se puoi, segnala il "
        "problema nel thread di sviluppo del forum di Elona seguendo il modello per le "
        "segnalazioni: aiuta a trovare la causa e resta agli atti. Se dai pochissime "
        "informazioni, o solo il codice d'errore, non c'è quasi speranza di venirne a capo.",
}
