# -*- coding: utf-8 -*-
"""La prova al contrario del referto sulle condizioni dei rinvii.

⚠️⚠️ **Una rete nuova che dice zero non ha ancora detto niente.** Il progetto
l'ha imparato due volte: nella 97a («una guardia va provata al contrario prima
di crederle») e nella 107a, dove la prova al contrario **c'era ed era spenta** —
il caso finto era costruito in modo che il difetto non potesse esserci.

Quindi qui non si costruisce un caso comodo: si prendono le **voci vere** di
`rinviate.jsonl` e si sposta di un passo la cosa che le tiene chiuse, una
famiglia per volta. Se il referto non se ne accorge, la famiglia non e' coperta.

E non si stampa un ✅: si stampa **dove** il cancello si e' acceso e **che cosa
ha detto**, perche' un esito booleano non distingue «ho trovato il guasto» da
«non l'ho cercato abbastanza».

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_129-prova-al-contrario-condizioni.py
"""
import copy
import importlib.util
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

_QUI = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    'condizioni_dei_rinvii', os.path.join(_QUI, '_129-condizioni-dei-rinvii.py'))
cd = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cd)


def _voce(rinvii, en, file=None):
    for voce in rinvii:
        if voce['en'] == en and (file is None or voce['file'] == file):
            return copy.deepcopy(voce)
    raise SystemExit('voce non trovata nelle voci vere: %r' % en)


def _voce_per_tipo(rinvii, tipo):
    for voce in rinvii:
        if (voce.get('condizione') or {}).get('tipo') == tipo:
            return copy.deepcopy(voce)
    raise SystemExit('nessuna voce vera di tipo %r' % tipo)


def casi(rinvii):
    """(famiglia, che cosa si sposta, voce guastata, esito atteso)."""
    fuori = []

    # 1. riga_morta — una firma le cui righe sono VIVE, dichiarata morta.
    #    ` liv.` e' quella che la 129a ha appena tolto dai rinvii proprio
    #    perche' la sua gemella a command.hsp:10710 e' viva: e' il difetto
    #    vero di oggi, rimesso dentro.
    fuori.append(('riga_morta', 'la firma di ` level`, viva a :10710, dichiarata morta',
                  _rinvio_level(), 'MATURATA'))

    # 2. risolta_da_toppa — un sito che la build lascia intatto.
    voce = _voce(rinvii, ' grown ')
    voce['condizione'] = {'tipo': 'risolta_da_toppa', 'siti': ['item_func.hsp:975']}
    fuori.append(('risolta_da_toppa', 'il sito spostato di una riga, dove nessuna toppa arriva',
                  voce, 'ROTTA'))

    # 3. attende_toppa — un sito che la build cambia davvero.
    voce = _voce(rinvii, ' grown ')
    voce['condizione'] = {'tipo': 'attende_toppa', 'siti': ['item_func.hsp:974']}
    fuori.append(('attende_toppa', 'la toppa c\'e\', ma il rinvio dice di aspettarla',
                  voce, 'MATURATA'))

    # 4. attende_resa — il sito atteso e' gia' reso nella build. E' la
    #    famiglia che ha ucciso i quattro rami della 128a: si rimette in piedi
    #    il rinvio com'era **prima** che qualcuno lo chiudesse.
    voce = _voce(rinvii, 'Party Room')
    voce['condizione'] = {'tipo': 'attende_resa', 'siti': ['map_rand.hsp:1287']}
    fuori.append(('attende_resa', 'il rinvio della sala delle feste com\'era prima della 128a',
                  voce, 'MATURATA'))

    # 5. attende_monte / morta_per_flusso — un sito dichiarato spento che e' vivo.
    voce = _voce(rinvii, "Let's have a meal together. [Total EXP 200%, Satiety increase halved]")
    voce['condizione'] = {'tipo': 'attende_monte', 'siti': ['chat.hsp:19326']}
    fuori.append(('attende_monte', 'il sito spostato di una riga, fuori dal commento',
                  voce, 'MATURATA'))

    voce = _voce(rinvii, 'St')
    voce['condizione'] = {'tipo': 'morta_per_flusso', 'siti': ['item_func.hsp:2474']}
    fuori.append(('morta_per_flusso', 'chi la stampa dichiarato sulla riga viva che la compone',
                  voce, 'MATURATA'))

    # 6. le due forme di voce che nessuno guarda.
    voce = _voce(rinvii, 'St')
    del voce['condizione']
    fuori.append(('(nessuna)', 'una voce senza il campo `condizione`', voce, 'SENZA-CONDIZIONE'))

    voce = _voce_per_tipo(rinvii, 'mai')
    voce['condizione'] = {'tipo': 'mai'}
    fuori.append(('mai', 'un `mai` senza la `nota` che dice perche\'', voce, 'SENZA-CONDIZIONE'))

    return fuori


def _rinvio_level():
    """Il rinvio di ` level` com'era stamattina, prima che la 129a lo togliesse.

    Non si inventa: si ricostruisce dalla firma vera del sito, cosi' che il caso
    finto cammini sullo stesso sorgente di quello vero.
    """
    from strumenti import estrai, percorsi
    testo = (percorsi.SORGENTE_HSP / 'command.hsp').read_text(encoding='cp932')
    for sito in estrai.siti(testo):
        if sito[0] == 10710 and sito[5] == ' level':
            return {'firma': sito[1], 'file': 'command.hsp', 'en': ' level',
                    'rinviata_a': 'mai: `lang()` dentro il ramo `if ( jp )`',
                    'motivo': 'ricostruito dalla prova al contrario',
                    'condizione': {'tipo': 'riga_morta'}}
    raise SystemExit('command.hsp:10710 non porta piu\' ` level`')


def main() -> int:
    rinvii = cd.carica_rinvii()
    sorgente = cd.Sorgente()
    toppe = cd.toppe_per_file()

    print('=== IL CANCELLO, PUNTATO DOVE IL DIFETTO C\'E\' DI SICURO')
    print()
    guasti = 0
    for famiglia, che_cosa, voce, atteso in casi(rinvii):
        esito, dettaglio = cd.valuta(voce, sorgente, toppe)
        segno = 'si accende' if esito == atteso else '⚠️ NON SI ACCENDE'
        if esito != atteso:
            guasti += 1
        print('  %-18s %s' % (famiglia, che_cosa))
        print('  %-18s %s -> %-17s %s' % ('', segno, esito, dettaglio))
        print()

    print('--- famiglie provate      : %4d' % len(casi(rinvii)))
    print('--- famiglie che NON si accendono : %4d   (atteso: 0)' % guasti)
    print()
    if guasti:
        print('⚠️⚠️ Una famiglia che non si accende non e\' una famiglia senza')
        print('  difetti: e\' una famiglia che il referto non guarda.')
        return 1

    print('ⓘ E il perche\' dello zero del referto, che senza questo non si legge:')
    print('  le sette famiglie sono coperte una per una, e ognuna e\' stata')
    print('  accesa su una voce **vera** spostata di un passo — non su un caso')
    print('  costruito apposta, che e\' il modo in cui la prova al contrario')
    print('  della 107a era rimasta spenta senza dirlo.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
