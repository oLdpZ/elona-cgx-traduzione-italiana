# -*- coding: utf-8 -*-
"""112a - Il cancello della famiglia delle righe-fonte.

Controlla la tabella di `scratchpad/lotti-112/titoli_fonte.py` contro il
sorgente, e risponde a quattro domande che nessun'altra rete fa:

1. **la copertura**: ogni riga-fonte viva del corpo ha una resa? Le mancanti si
   stampano, che e' il modo di aggiungerle;
2. **il tetto**: la resa degradata sta entro 66 caratteri? A 67 la riga smette
   di essere una fonte e cade nell'impaginatore (`command.hsp:16758`);
3. **i caratteri che CP932 cancella**: `«` `»` `…` `“` `”` e la tilde larga
   `～` spariscono o sfigurano. ⚠️ La tilde giusta e' quella ASCII, e il
   sorgente ne ha due scritte larghe: copiate verbatim, fanno bocciare il lotto;
4. **l'apostrofo dentro la parola**: `degrada()` fa di «perche'» sette
   caratteri, e di «degli dei» con l'accento un `de'i` — l'apostrofo finisce
   dentro la parola e a schermo e' un refuso. La rete lo cerca.

⚠️ La copertura si misura sul **giapponese**, non sull'inglese: l'inglese
appiattisce libri diversi sotto lo stesso titolo (vedi `_112-dossier-fonti.py`).

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_112-verifica-fonti.py
    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_112-verifica-fonti.py --prova
"""
import argparse
import collections
import importlib.util
import re
import sys
from pathlib import Path

from strumenti.accenti import degrada

_qui = Path(__file__).resolve().parent


def _carica(nome, percorso):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


_112 = _carica('_112_corpo', _qui / '_112-corpo-descrizioni.py')
_dossier = _carica('_112_dossier', _qui / '_112-dossier-fonti.py')
_tabella = _carica('titoli_fonte', _qui / 'lotti-112' / 'titoli_fonte.py')

TETTO = _112.SOGLIA
PROIBITI = ('«', '»', '…', '“', '”', '～')
_APOSTROFO_DENTRO = re.compile(r"[A-Za-z]'[a-z]{1,2}\b(?<!\bl')")


def raccogli():
    """(jp, en, quante) per ogni riga-fonte viva del corpo."""
    fuori = collections.Counter()
    for riga, indice, jp, en in _dossier.coppie():
        t_en = _dossier.voluta_da(en)
        if not t_en:
            continue
        fuori[(_dossier.voluta_da(jp), t_en)] += 1
    return fuori


def resa_di(t_jp, t_en):
    if t_jp and t_jp in _tabella.TITOLI_JP:
        return _tabella.TITOLI_JP[t_jp], 'jp'
    if t_en in _tabella.TITOLI_EN:
        return _tabella.TITOLI_EN[t_en], 'en'
    return None, None


def referto():
    coppie = raccogli()
    righe = sum(coppie.values())
    scoperte = collections.Counter()
    rese = {}
    for (t_jp, t_en), quante in coppie.items():
        it, _ = resa_di(t_jp, t_en)
        if it is None:
            scoperte[(t_jp, t_en)] += quante
        else:
            rese[(t_jp, t_en)] = it

    print(f'righe-fonte vive: {righe}   coppie jp/en distinte: {len(coppie)}')
    print(f'coperte dalla tabella: {len(rese)}   '
          f'⚠️ SCOPERTE: {len(scoperte)} ({sum(scoperte.values())} righe)')
    print()
    if scoperte:
        print('=== LE SCOPERTE, da aggiungere a `lotti-112/titoli_fonte.py`')
        for (t_jp, t_en), quante in scoperte.most_common():
            print(f'  {quante:>4}x')
            print(f'     jp  {t_jp if t_jp else "(muto)"}')
            print(f'     en  {t_en}')
        print()

    print('=== IL TETTO E I CARATTERI')
    lunghe = sporche = apostrofi = 0
    for (t_jp, t_en), it in sorted(rese.items(), key=lambda kv: -len(degrada(kv[1]))):
        degradata = degrada(it)
        guai = []
        if len(degradata) > TETTO:
            guai.append(f'OLTRE IL TETTO ({len(degradata)} > {TETTO})')
            lunghe += 1
        cattivi = [c for c in PROIBITI if c in it]
        if cattivi:
            guai.append('CARATTERI CHE CP932 CANCELLA: ' + ' '.join(cattivi))
            sporche += 1
        dentro = _APOSTROFO_DENTRO.findall(degradata)
        if dentro:
            guai.append('APOSTROFO DENTRO LA PAROLA: ' + ' '.join(dentro))
            apostrofi += 1
        if guai:
            print(f'  ⚠️ {it}')
            for g in guai:
                print(f'       {g}')
    print(f'  oltre il tetto           : {lunghe}   (atteso 0)')
    print(f'  caratteri cancellati     : {sporche}   (atteso 0)')
    print(f'  apostrofi dentro la parola: {apostrofi}   (atteso 0)')
    print()

    piu_lunga = max(rese.values(), key=lambda s: len(degrada(s)))
    print(f'=== LA RAGIONE DELLO ZERO, che senza ragione non e\' un risultato')
    print(f'  la resa piu\' lunga e\' di {len(degrada(piu_lunga))} caratteri '
          f'degradati, contro un tetto di {TETTO}:')
    print(f'    {piu_lunga}')
    print(f'  il margine che resta sulla peggiore e\' {TETTO - len(degrada(piu_lunga))}.')
    return 0 if not (scoperte or lunghe or sporche or apostrofi) else 1


def prova():
    """Le prove al contrario: ognuna dice DOVE si accende, non un segno di spunta."""
    print('=== 1. IL TETTO')
    base = '~Grande Enciclopedia dei Mobili di Tyris del Nord~'
    for aggiunti in range(0, 60):
        finto = base[:-1] + ('o' * aggiunti) + '~'
        if len(degrada(finto)) > TETTO:
            print(f'   -> si accende a {len(degrada(finto))} caratteri '
                  f'({aggiunti} aggiunti alla resa piu\' lunga vera)')
            break
    else:
        print('   -> NON si accende: la prova non prova niente')

    print()
    print('=== 2. I CARATTERI CHE CP932 CANCELLA')
    for c in PROIBITI:
        finto = f'~parole di {c}Norne{c}~'
        if any(p in finto for p in PROIBITI):
            print(f'   -> si accende su U+{ord(c):04X} ({c!r}), '
                  f'che a schermo sparisce o sfigura')
            break
    else:
        print('   -> NON si accende: la prova non prova niente')
    print('   ⓘ e il sorgente ne ha DUE scritti cosi\': `db_item.hsp:60514` e '
          '`:114277`,')
    print('     i due titoli con la tilde larga. Copiati verbatim, bocciano il lotto.')

    print()
    print('=== 3. L\'APOSTROFO DENTRO LA PAROLA')
    for parola in ('perche', 'perché', 'degli dèi', 'citta', 'città'):
        d = degrada(parola)
        trovato = _APOSTROFO_DENTRO.findall(d)
        if trovato:
            print(f'   -> si accende su {parola!r}, che degradato fa {d!r}')
            break
    else:
        print('   -> NON si accende: la prova non prova niente')
    print('   ⓘ LA RAGIONE: `degrada()` mette l\'apostrofo DOPO la vocale, quindi')
    print('     una parola tronca finale («citta\'») e\' giusta e una accentata')
    print('     in mezzo («de\'i») e\' un refuso. La rete cerca la seconda.')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--prova', action='store_true')
    args = ap.parse_args()
    if args.prova:
        prova()
        return 0
    return referto()


if __name__ == '__main__':
    sys.exit(main())
