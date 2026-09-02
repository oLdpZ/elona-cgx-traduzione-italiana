# -*- coding: utf-8 -*-
"""Scrive il campo `condizione` sulle 114 voci di `rinviate.jsonl`.

Si lancia una volta sola: dopo, il campo sta nel file e chi aggiunge un rinvio
lo scrive a mano. Le assegnazioni qui sotto sono **per indice**, cioe' lette una
per una: non c'e' una regola che deduca il tipo dalla prosa di `rinviata_a`,
perche' dedurlo dalla prosa e' esattamente cio' che non ha funzionato.

⚠️ Il controllo che l'assegnazione sia giusta **non e' in questo file**: e'
`_129-condizioni-dei-rinvii.py`, che va a misurare la condizione dichiarata. Una
voce marcata `riga_morta` la cui riga e' viva esce come MATURATA, e cosi' si
scopre di averla classificata male.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strumenti import percorsi  # noqa: E402

# indice (1-based, l'ordine del file) -> condizione
CONDIZIONI = {}


def _assegna(indici, tipo, siti=None, nota=None):
    for indice in indici:
        condizione = {'tipo': tipo}
        if siti:
            condizione['siti'] = list(siti)
        if nota:
            condizione['nota'] = nota
        CONDIZIONI[indice] = condizione


# --- riga spenta nel sorgente: una delle cinque famiglie note ---------------
_assegna([4, 5, 6, 7], 'riga_morta')                    # db_creature, commentate
_assegna([8], 'riga_morta')                             # blocco MANUSCRIPT HINT
_assegna([12, 15], 'riga_morta')                        # /* */ spento dal mod
_assegna([16], 'riga_morta')
_assegna([18, 19, 20, 21, 22, 23], 'riga_morta')        # `;` e /* */
_assegna(range(24, 34), 'riga_morta')                   # ramo if ( jp )
_assegna([34, 35, 36], 'riga_morta')                    # blocco ORIGINAL spento
_assegna([40, 41], 'riga_morta')
_assegna([58], 'riga_morta')                            # ramo if ( jp )
_assegna(range(59, 69), 'riga_morta')                   # if ( 0 ) e ramo jp
_assegna([80], 'riga_morta')                            # commento di blocco
_assegna(range(86, 95), 'riga_morta')                   # ramo `& jp`
_assegna([103], 'riga_morta')
_assegna([105, 106], 'riga_morta')
_assegna(range(108, 113), 'riga_morta')                 # `//` e `;`
_assegna([113], 'riga_morta')

# --- la riga e' viva, e' morto chi la stampa -------------------------------
# item_func.hsp:2474 compone le sigle in `s(cnt)`; il `mes s(cnt)` che le
# scriverebbe e' commentato a :2485-:2491, mentre la fila gemella delle
# resistenze (:2465) si stampa davvero con un `mes` vivo a :2470 ed e' tradotta.
_assegna(range(44, 58), 'morta_per_flusso',
         siti=['item_func.hsp:2485', 'item_func.hsp:2491'])

# --- gia' chiusa da una toppa: se la toppa sparisce, il rinvio riapre ------
_assegna([1, 2], 'risolta_da_toppa')
_assegna([3, 9, 10], 'risolta_da_toppa',
         nota='la condizione ERA `attende_resa` e nella 128a e\' maturata: chi '
              'assegna il nome della mappa e\' stato reso e il confronto era '
              'morto. Chiusa con una toppa per sito, che accetta i due nomi.')
_assegna([11, 13, 14, 17], 'risolta_da_toppa')
_assegna([37], 'risolta_da_toppa', siti=['command.hsp:15489'])
_assegna([38], 'risolta_da_toppa', siti=['command.hsp:4335'])
_assegna([39], 'risolta_da_toppa')
_assegna([42, 43], 'risolta_da_toppa')
_assegna([69, 70, 71, 72, 73], 'risolta_da_toppa')
_assegna([95, 96, 97, 98], 'risolta_da_toppa')
_assegna([107], 'risolta_da_toppa')

# --- aspetta una toppa che ancora non esiste -------------------------------
_assegna([81, 82, 83, 84], 'attende_toppa')             # succo/latte/mix
_assegna([85], 'attende_toppa',
         nota='dipende da `_weight()`, fra i 35 modificatori di qualita\' di '
              '`contratto-nomi.md` §6: si fa nello stesso lotto di quelli.')
_assegna([99, 100, 101, 102], 'attende_toppa')
_assegna([104], 'attende_toppa',
         nota='il segno che resta a schermo e\' il letterale nudo `"Have"` di '
              'command.hsp:11069, e la toppa e\' quella.')

# --- aspetta che monte cambi il sorgente pinnato ---------------------------
_assegna([74], 'attende_monte', siti=['chat.hsp:19327'])
_assegna([75], 'attende_monte', siti=['chat.hsp:19334'])
_assegna([76], 'attende_monte', siti=['chat.hsp:13991'])
_assegna([77], 'attende_monte', siti=['chat.hsp:14036'])
_assegna([78], 'attende_monte', siti=['chat.hsp:14037'])
_assegna([79], 'attende_monte', siti=['chat.hsp:14038'])

# --- nessuna condizione, e si dice perche' ---------------------------------
_assegna([114], 'mai',
         nota="la riga non ha testo in nessuna delle due lingue: sono tabulazioni "
              "e a capo. Non c'e' niente che possa maturare.")


def main() -> int:
    percorso = percorsi.PROGETTO / 'rinviate.jsonl'
    righe = [r for r in percorso.read_text(encoding='utf-8').splitlines() if r.strip()]
    if len(righe) != 114:
        print('⚠️ il file ha %d voci, non 114: le assegnazioni sono per indice '
              'e vanno rilette prima di riscrivere.' % len(righe))
        return 1

    mancanti = [i for i in range(1, 115) if i not in CONDIZIONI]
    if mancanti:
        print('⚠️ indici senza condizione: %s' % mancanti)
        return 1

    fuori = []
    for indice, riga in enumerate(righe, start=1):
        voce = json.loads(riga)
        voce['condizione'] = CONDIZIONI[indice]
        fuori.append(json.dumps(voce, ensure_ascii=False))
    percorso.write_text('\n'.join(fuori) + '\n', encoding='utf-8')
    print('scritte %d condizioni in %s' % (len(fuori), percorso.name))
    return 0


if __name__ == '__main__':
    sys.exit(main())
