# -*- coding: utf-8 -*-
"""116a - Le righe del corpo la cui coda GIAPPONESE e quella INGLESE non sono
lo stesso libro.

`_115-fonti-storpiate.py` trova le righe con la coda giapponese e **nessuna**
coda inglese (3 righe). Questa e' l'altra meta' della domanda: le righe che
hanno **tutt'e due** le code, ma che indicano **fonti diverse** — cioe' dove
l'inglese non ha appiattito una distinzione, l'ha **sostituita**.

Nata su `:70398` (la castagna), dove il giapponese e' la battuta di
『ナプラス』 l'alchimista spaventato e l'inglese e' il testo generico del
rapporto di identificazione. Il difetto non si vede da nessun cancello:
`_code.py` cerca prima la coda giapponese in tabella, non la trova, e **ripiega
sull'inglese**, cosi' il referto «righe senza resa in tabella» resta a 0.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_116-code-discordi.py

⚠️ E' un REFERTO, non un cancello: il valore atteso non e' zero, e ogni riga va
letta.
"""
import importlib.util
import io
import json
import sys

LAVORO = 'lavoro/_107-daitem.jsonl'
TABELLA = 'scratchpad/lotti-112/titoli_fonte.py'


def tabelle():
    spec = importlib.util.spec_from_file_location('titoli_fonte', TABELLA)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.TITOLI_JP, modulo.TITOLI_EN


def coda(testo):
    for pezzo in reversed((testo or '').split('\\n')):
        if pezzo.startswith('#'):
            return pezzo[1:].strip()
    return None


def main():
    jp_it, en_it = tabelle()
    discordi = []
    solo_jp = 0
    solo_en = 0
    tutt_e_due = 0
    for linea in io.open(LAVORO, encoding='utf-8'):
        if not linea.strip():
            continue
        v = json.loads(linea)
        cjp = coda(v.get('jp'))
        cen = coda(v.get('en'))
        if cjp and not cen:
            solo_jp += 1
            continue
        if cen and not cjp:
            solo_en += 1
            continue
        if not cjp and not cen:
            continue
        tutt_e_due += 1
        # la tabella traduce il giapponese: se il titolo italiano che nasce dal
        # giapponese e quello che nasce dall'inglese sono diversi, le due code
        # non parlano dello stesso libro.
        da_jp = jp_it.get(cjp)
        da_en = en_it.get(cen)
        if da_jp is not None and da_en is not None and da_jp != da_en:
            discordi.append((v['riga'], cjp, cen, da_jp, da_en))
        elif da_jp is None and da_en is not None:
            discordi.append((v['riga'], cjp, cen, '(non in tabella)', da_en))

    print('righe con tutt\'e due le code : %d' % tutt_e_due)
    print('righe con la sola coda jp    : %d   (le trova _115-fonti-storpiate)' % solo_jp)
    print('righe con la sola coda en    : %d' % solo_en)
    print()
    print('=== LE CODE DISCORDI: %d' % len(discordi))
    for riga, cjp, cen, da_jp, da_en in discordi:
        print('   :%d' % riga)
        print('      jp  %s   ->  %s' % (cjp, da_jp))
        print('      en  %s   ->  %s' % (cen, da_en))
    print()
    print('ⓘ referto, non cancello: ogni riga va letta.')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
