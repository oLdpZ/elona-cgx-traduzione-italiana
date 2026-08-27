# -*- coding: utf-8 -*-
"""112a - Genera la sezione di `glossario.md` per la famiglia delle righe-fonte.

⚠️ La tabella si GENERA dalla tabella eseguibile (`lotti-112/titoli_fonte.py`),
non si ricopia a mano: due copie divergono, e questa ha 234 righe. Il file
prodotto si innesta in `glossario.md` con `_112-innesta-glossario.py`.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_112-genera-glossario.py
"""
import collections
import importlib.util
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

USCITA = _qui / 'lotti-112' / 'sezione-glossario.md'


def main():
    per_jp = collections.Counter()
    per_en = collections.Counter()
    inglesi = collections.defaultdict(set)
    for riga, indice, jp, en in _dossier.coppie():
        t_en = _dossier.voluta_da(en)
        if not t_en:
            continue
        t_jp = _dossier.voluta_da(jp)
        if t_jp and t_jp in _tabella.TITOLI_JP:
            per_jp[t_jp] += 1
            inglesi[t_jp].add(t_en)
        elif t_en in _tabella.TITOLI_EN:
            per_en[t_en] += 1

    righe = []
    A = righe.append
    A('## Le righe-fonte delle descrizioni di `db_item.hsp` — 112ª')
    A('')
    A('1.509 descrizioni del **corpo** (indici 0-2) finiscono con una riga marcata')
    A('da `#`, che `command.hsp:16836`-`:16840` disegna a **destra**, in corsivo,')
    A('con un **trattino** davanti: è il titolo del libro da cui la notizia viene.')
    A('I titoli distinti sono **224**, e i venti più frequenti coprono il **74%**')
    A('delle righe — sono una famiglia chiusa sparsa su tutte le categorie, quindi')
    A('su tutti i lotti futuri. La tabella eseguibile sta in')
    A('`scratchpad/lotti-112/titoli_fonte.py`; il cancello è')
    A('`scratchpad/_112-verifica-fonti.py`.')
    A('')
    A('⚠️⚠️ **Il tetto è 66 caratteri degradati, e non è un tetto di larghezza:**')
    A('è la soglia che decide *di che tipo* è la riga (`:16758`). A 67 la fonte')
    A('smette di essere una fonte, cade nell\'impaginatore e viene disegnata a')
    A('sinistra come testo normale. Non rompe niente e non si vede in un conteggio.')
    A('La resa più lunga decisa qui ne misura 55.')
    A('')
    A('⚠️⚠️ **La chiave è il giapponese, non l\'inglese.** L\'inglese di monte')
    A('appiattisce: `~Vernis Ore Catalogue~` copre **tre** libri giapponesi diversi,')
    A('`~Irva Fantasy Encyclopedia~` ne copre due, `Lead Developer <Dr. Gavela>`')
    A('copre due persone, e `~Battles, Dragons, Swords and Magic~` traduce')
    A('「巻かれる為の長いもの」, *cose lunghe fatte per essere avvolte*, che non')
    A('c\'entra niente. Arbitra il giapponese, com\'è regola dalla 26ª.')
    A('')
    A('⚠️ **Due titoli il sorgente li scrive con la tilde larga** `～`')
    A('(`db_item.hsp:60514` e `:114277`), che sta fra i caratteri proibiti di')
    A('`guardie.py`: copiati verbatim fanno bocciare il lotto. La tilde giusta è')
    A('quella ASCII.')
    A('')
    A('⚠️ **Le divinità portano in giapponese un epiteto dentro `《》`** che')
    A('l\'inglese butta via — `《風のルルウィ》` è *Lulwy del vento*. Il progetto')
    A('aveva già reso quella forma come `<Lulwy>` (in `db_card.hsp`), e queste')
    A('righe le vanno dietro: l\'epiteto resta nel giapponese.')
    A('')
    A(f'### I titoli indicizzati per giapponese ({len(per_jp)})')
    A('')
    A('| jp | en | it | righe |')
    A('|---|---|---|---|')
    for t_jp, n in per_jp.most_common():
        it = _tabella.TITOLI_JP[t_jp]
        # ⚠️ piu' di un inglese sulla stessa riga vuol dire che l'inglese di
        # monte appiattisce o ha un refuso: si segna, perche' e' la cosa che
        # un lotto futuro rischia di riscrivere per imitazione
        varianti = sorted(inglesi[t_jp])
        marca = ' ⚠️' if len(varianti) > 1 else ''
        en = '<br>'.join(f'`{v}`' for v in varianti)
        A(f'| {t_jp} | {en}{marca} | `{it}` | {n} |')
    A('')
    A(f'### Le righe **mute**, dove l\'inglese è l\'unica fonte ({len(per_en)})')
    A('')
    A('Il ramo giapponese non ha questa riga: o è vuoto, o la mette in un altro')
    A('indice. ⓘ I quattro «rapporti di identificazione» il giapponese ce li ha,')
    A('ma nell\'**indice 3**, dove `trimdesc(desc, 1)` tronca al primo `#` e non')
    A('arrivano mai a schermo: la forma è `～鑑定報告書：＜食物＞カテゴリ～`.')
    A('')
    A('| en | it | righe |')
    A('|---|---|---|')
    for t_en, n in per_en.most_common():
        it = _tabella.TITOLI_EN[t_en]
        A(f'| `{t_en}` | `{it}` | {n} |')
    A('')

    USCITA.write_text('\n'.join(righe) + '\n', encoding='utf-8')
    print(f'scritto {USCITA} — {len(righe)} righe, '
          f'{len(per_jp)} titoli jp e {len(per_en)} muti')
    piu = max(list(_tabella.TITOLI_JP.values()) + list(_tabella.TITOLI_EN.values()),
              key=lambda s: len(degrada(s)))
    print(f'la resa piu\' lunga: {len(degrada(piu))} caratteri — {piu}')


if __name__ == '__main__':
    main()
