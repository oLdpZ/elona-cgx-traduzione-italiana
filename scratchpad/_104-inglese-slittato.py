# -*- coding: utf-8 -*-
"""104a - L'inglese di monte SLITTA di una carta, e a volte per NOVE carte.

`_103-inglese-ripetuto.py` cerca due prose inglesi **uguali**, e trova cosi' il
punto in cui monte ha scritto due volte lo stesso inglese. Ma quel punto e' solo
la **testa**: se l'inglese giusto della carta copiata finisce sulla successiva,
da li' in avanti tutto scivola di un posto, e dal secondo anello in poi ogni
inglese compare **una volta sola**. La rete della 103a li' tace.

⚠️⚠️ **E il difetto ha due forme, che si distinguono solo leggendo:**

- **il doppione isolato** — monte riscrive l'inglese della carta prima e
  l'inglese proprio di quella carta lo **perde**. La carta dopo e' a posto.
  Cosi' `:4125` (riparata dalla 103a) e `:9637`;
- **la catena** — l'inglese proprio non si perde, **spinge in avanti** quello di
  tutte le carte seguenti finche' monte non si riallinea buttandone uno.
  Cosi' `:6972`-`:7063`: **nove carte**, e il riallineamento avviene a `:7076`
  perdendo l'inglese di `:7063`.

⭐⭐ **Quindi la regola di lavoro, che e' il vero risultato di questa rete:**
quando `_103-inglese-ripetuto` segnala un doppione, il dossier delle **venti
carte successive** si legge a mano. Un doppione e' la testa di qualcosa, non un
caso singolo, e finche' non si guarda non si sa quale delle due forme sia.

⚠️⚠️ **I due segnali automatici qui sotto NON bastano, ed e' misurato.**
Puntati sul blocco `:6972`-`:7063`, dove il difetto c'e' di sicuro, accendono su
**cinque carte su nove** (`:6985`, `:6998`, `:7037`, `:7050` e `:4125` fuori
blocco) e tacciono su `:6972`, `:7011`, `:7024` e `:7063`. Il rapporto fra le
lunghezze e' troppo rumoroso su testi di due righe, e il nome della carta nella
prosa c'e' solo quando c'e'. Sono un aiuto alla lettura, **non un cancello**.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_104-inglese-slittato.py

⚠️ Referto da leggere: il valore atteso non e' zero, perche' il difetto sta nel
sorgente di monte e il sorgente non si tocca.
"""
import difflib
import re
import statistics
import sys

from strumenti.percorsi import SORGENTE_HSP

FILE = 'db_card.hsp'
_SKILL = re.compile(r'^\s*cardrefskill\s*=\s*lang\(')
_NOME = re.compile(r'^\s*cardrefn\s*=\s*lang\(')
_PEZZI = re.compile(r'"((?:[^"\\]|\\.)*)"')

# quanto simili devono essere due inglesi per contare come doppione
SIMILE = 0.90
# quante carte si guardano dopo una testa
FINESTRA = 20
# quanto meglio deve stare l'allineamento slittato per contare come segnale
MEGLIO = 2.0
# sotto questa lunghezza il rapporto fra le lunghezze e' rumore
CORTA = 40

VUOTE = {
    'the', 'of', 'a', 'an', 'and', 'in', 'to', 'his', 'her', 'its', 'it',
    'big', 'small', 'great', 'little', 'old', 'new', 'young', 'black', 'white',
    'red', 'blue', 'green', 'gold', 'golden', 'silver', 'dark', 'light',
    'king', 'queen', 'lord', 'god', 'goddess', 'type', 'man', 'men', 'one',
}


def parole(testo: str) -> set:
    return {p for p in re.findall(r"[a-z]+", testo.lower()) if len(p) > 3}


def carte():
    """(riga, nome_en, jp, en) di ogni carta, nell'ordine del file."""
    righe = (SORGENTE_HSP / FILE).read_bytes().decode('cp932', 'replace').split('\n')
    fuori = []
    aperta = None
    for i, testo in enumerate(righe, 1):
        if testo.lstrip().startswith(';'):
            continue
        if _SKILL.match(testo):
            pezzi = _PEZZI.findall(testo)
            if len(pezzi) >= 2:
                aperta = (i, pezzi[0], pezzi[-1])
        elif _NOME.match(testo) and aperta is not None:
            pezzi = _PEZZI.findall(testo)
            if len(pezzi) >= 2:
                riga, jp, en = aperta
                fuori.append((riga, pezzi[-1], jp, en))
            aperta = None
    return fuori


def teste(elenco) -> list:
    """le carte il cui inglese ripete quello di una carta precedente"""
    fuori = []
    for k in range(1, len(elenco)):
        mio = elenco[k][3].strip()
        if len(mio) < CORTA:
            continue
        for j in range(max(0, k - 3), k):
            suo = elenco[j][3].strip()
            if len(suo) < CORTA:
                continue
            if difflib.SequenceMatcher(None, mio, suo).ratio() >= SIMILE:
                fuori.append((k, j))
                break
    return fuori


def main() -> None:
    elenco = carte()
    rapporti = [len(en) / len(jp) for _, _, jp, en in elenco if len(jp) >= CORTA]
    tipico = statistics.median(rapporti)
    print(f'--- {len(elenco)} carte lette da {FILE}')
    print(f'--- rapporto tipico inglese/giapponese: {tipico:.2f}\n')

    def segnali(k) -> list:
        riga, nome, jp, en = elenco[k]
        _, nome_prima, jp_prima, _ = elenco[k - 1]
        fuori = []
        mie = parole(nome) - VUOTE
        sue = parole(nome_prima) - VUOTE
        dentro = parole(en)
        if mie and sue and not (mie & dentro) and (sue & dentro):
            fuori.append(f'nomina «{nome_prima}» e non se stessa')
        if len(jp) >= CORTA and len(jp_prima) >= CORTA:
            mio = abs(len(en) / len(jp) - tipico)
            slittato = abs(len(en) / len(jp_prima) - tipico)
            if slittato > 0 and mio > slittato * MEGLIO:
                fuori.append(f'lunghezza: sta al giapponese di :{elenco[k-1][0]} '
                             f'{mio / max(slittato, 1e-9):.1f} volte meglio')
        return fuori

    trovate = teste(elenco)
    for k, j in trovate:
        print(f'⚠️⚠️ TESTA a :{elenco[k][0]} «{elenco[k][1]}» — '
              f'ripete l\'inglese di :{elenco[j][0]} «{elenco[j][1]}»')
        print(f'     le {FINESTRA} carte successive, coi due segnali deboli '
              f'(⚠️ vanno LETTE, i segnali non bastano):')
        for m in range(k, min(k + FINESTRA, len(elenco))):
            s = segnali(m)
            marchio = '  ⚠️' if s else '    '
            print(f'{marchio} :{elenco[m][0]:<6} {elenco[m][1][:44]:<44}'
                  + ('   ' + ' | '.join(s) if s else ''))
        print()

    print(f'teste trovate: {len(trovate)}   (atteso al 2026-08-26: 2)')
    print('⚠️ referto da leggere, non una guardia: il difetto e\' di monte.')
    print('💡 :9637 e\' un DOPPIONE ISOLATO — verificato leggendo :9650, che e\' '
          'a posto. :6972 e\' la testa di una CATENA di NOVE, da :6972 a :7063, '
          'che si riallinea a :7076 perdendo l\'inglese di :7063.')
    print('⚠️⚠️ E QUESTA RETE NON LE TROVA TUTTE: la terza testa, :4125, qui non '
          'compare, perche\' il suo inglese non e\' una COPIA di :4112 ma una '
          'traduzione DIVERSA dello stesso giapponese (somiglianza 0,30). '
          'Quella la trova `_103-inglese-ripetuto.py`, che confronta le parole '
          'e non la stringa. ⭐ Le due reti si leggono INSIEME: nessuna delle '
          'due vede quello che vede l\'altra.')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
