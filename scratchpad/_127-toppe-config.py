# -*- coding: utf-8 -*-
"""Il quarto lotto della 127a: le righe nude di `config.hsp`.

Nove vive, e si dividono in tre:

    :777 :780 :875 :887 :906 :972   il valore « wait» in sei righe del menu
    :950                            i due nomi delle lingue
    :47  :1515                      chiavi di `config.txt`, non testo -> invariati

⚠️ Le sei righe del `wait` NON sono identiche fra loro (cambia la variabile),
quindi ognuna ha il suo `cerca` di una riga sola.
"""
import io
import json

from strumenti.accenti import degrada

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\config.hsp'
righe = io.open(SORGENTE, encoding='cp932').read().split('\n')

NUOVE = {}
MOTIVI = {}

NUDO = (
    "LETTERALE INGLESE NUDO: non passa da nessuna lang(), quindi non ha firma "
    "ne' voce di dizionario e nessun lotto puo' raggiungerlo (quinto punto "
    "cieco, nudi_en.py, 49a). "
)

# --- il valore « wait» nella colonna dei valori del menu opzioni ------------

_ATTESA = (
    "config.hsp:*com_config_loop_WHILE1, la colonna dei VALORI del menu delle "
    "opzioni: sei righe che stampano un ritardo, e sono le uniche sei di "
    "quella colonna rimaste inglesi — tutte le vicine passano da `lang()` e "
    "sono italiane da sessioni (:768 «Mai», :772 «Dopo N passi», :783 «In "
    "parte», :944 «MAIUSCOLO»). ⭐⭐ IL TETTO SI LEGGE, NON SI EREDITA: il "
    "valore si stampa a `pos wx + 250` (:747) e la colonna successiva comincia "
    "a `wx + 358` (:743), cioe' 108 px; il carattere e' a corpo 12 "
    "(`14 - en * 2`, :716), cioe' 7 px, e il tetto e' 15 CARATTERI. «20 di "
    "attesa» ne fa dodici. ⓘ Il giapponese qui non aiuta: la riga non ha ramo, "
    "e la build giapponese stampa «wait» come l'inglese. "
)

_WAIT = {
    777: ('cfg_walkwait', 'la velocita\' della camminata (voce «Velocita\' camminata», '
                          'sottomenu «Impostazioni di gioco»)'),
    780: ('cfg_attackwait', 'l\'intervallo fra un attacco e l\'altro (voce «Intervallo attacchi»)'),
    875: ('cfg_runwait', 'la velocita\' della corsa (voce «Velocita\' di corsa», '
                         'sottomenu «Impostazioni avanzate»)'),
    887: ('cfg_scrsync', 'la frequenza di aggiornamento dello schermo (voce «Frequenza schermo»)'),
    906: ('cfg_animewait', 'la durata delle animazioni'),
    972: ('cfg_tcganimewait', 'la durata delle animazioni del gioco di carte '
                              '(voce «(TCG) Velocita\'»)'),
}

for _n, (_var, _che) in _WAIT.items():
    NUOVE[_n] = 'mes "" + {} + " di attesa"'.format(_var)
    MOTIVI[_n] = (
        NUDO + _ATTESA + "Qui il valore e' {}, ed e' {}.".format(_var, _che)
    )

# --- i due nomi delle lingue ------------------------------------------------

NUOVE[950] = 's = "Giapponese", "Italiano"'
MOTIVI[950] = (
    NUDO +
    "config.hsp:*com_config_loop_WHILE1, sottomenu 7 («Lingua (Language)», "
    ":623): i due valori fra cui `cfg_language` sceglie. ⚠️⚠️ «English» "
    "DIVENTA «Italiano», NON «Inglese», e non e' una svista: in questa build "
    "il ramo `en` **e' la traduzione italiana** — e' li' che vivono le 26.326 "
    "firme del dizionario, le 1.120 toppe e i file dati `_it.txt`. Chi sceglie "
    "quella voce ottiene l'italiano, e chiamarla «Inglese» direbbe al "
    "giocatore una cosa falsa su quel che sta per succedere. L'altra resta "
    "«Giapponese», perche' quella voce il giapponese lo da' davvero. "
    "ⓘ Il valore scritto in `config.txt` e' l'INDICE (`cfg_language`, :1515 e "
    "sorelle), non la stringa: cambiare l'etichetta non tocca il salvataggio "
    "ne' la lettura. ⓘ Tetto 15 caratteri (vedi le sei righe del ritardo qui "
    "accanto): «Giapponese» ne fa dieci. ⚠️ La voce di riga porta un `*` "
    "(«Lingua*»), cioe' vuole il riavvio: non e' cambiato niente."
)

# ---------------------------------------------------------------------------


def _codificabile(c: str) -> bool:
    try:
        c.encode('cp932')
        return True
    except UnicodeEncodeError:
        return False


def blocco_unico(n: int) -> list:
    for altezza in range(1, 25):
        blocco = righe[n - altezza:n]
        quanti = sum(1 for i in range(len(righe) - len(blocco) + 1)
                     if righe[i:i + len(blocco)] == blocco)
        if quanti == 1:
            return blocco
    raise SystemExit('riga {}: nessun blocco unico entro 24 righe'.format(n))


toppe = []
for n in sorted(NUOVE):
    originale = righe[n - 1]
    indent = originale[:len(originale) - len(originale.lstrip())]
    nuova = indent + degrada(NUOVE[n])
    residuo = [c for c in nuova if not _codificabile(c)]
    if residuo:
        raise SystemExit('riga {}: caratteri che CP932 non sa scrivere: {}'.format(n, residuo))
    if nuova == originale:
        raise SystemExit('riga {}: la toppa non cambierebbe niente'.format(n))
    cerca = blocco_unico(n)
    sostituisci = cerca[:-1] + [nuova]
    toppe.append({
        'file': 'config.hsp',
        'cerca': cerca if len(cerca) > 1 else cerca[0],
        'sostituisci': sostituisci if len(sostituisci) > 1 else sostituisci[0],
        'motivo': MOTIVI[n],
    })
    print('{:6d}  blocco di {} riga/e   {}'.format(n, len(cerca), nuova.strip()[:70]))

dati = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in toppe).encode('utf-8')
with io.open('lavoro/toppe-127-config.jsonl', 'wb') as f:
    f.write(dati)
print('{} toppe -> lavoro/toppe-127-config.jsonl'.format(len(toppe)))
