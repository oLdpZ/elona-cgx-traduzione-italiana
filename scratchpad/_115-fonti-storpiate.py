# -*- coding: utf-8 -*-
"""115a - Le righe-fonte in cui la tilde di monte non e' una tilde.

Nato su `db_item.hsp:46207`, dove la coda giapponese e' `#?ティリス園芸図鑑?`
con **due punti interrogativi ASCII** (U+003F) al posto della tilde larga
（U+FF5E) che le altre quaranta occorrenze dello stesso libro portano. Non e' un
artefatto della nostra estrazione: sta cosi' nel sorgente pinnato.

Conta quante righe-fonte del corpo sono scritte cosi', e con quale carattere.
E' un **referto**: dice quanto e' grande la famiglia, non se qualcosa e' rotto.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_115-fonti-storpiate.py
"""
import collections
import io
import json
import sys

LAVORO = 'lavoro/_107-daitem.jsonl'
ACAPO = '\\n'
TILDE_LARGA = '～'
TILDE_ONDA = '〜'
TILDE_ASCII = '~'
RAPPORTO = '鑑定報告書'


def coda(testo):
    pezzi = (testo or '').split(ACAPO)
    for pezzo in reversed(pezzi):
        if pezzo.startswith('#'):
            return pezzo
    return None


def apertura(c):
    """Il carattere che apre il titolo, dopo il `#` e l'eventuale spazio."""
    resto = c[1:].lstrip(' ')
    return resto[0] if resto else ''


def main():
    conta = collections.Counter()
    storpiate = []
    senza_coda_en = []
    rapporti = 0
    for r in io.open(LAVORO, encoding='utf-8'):
        d = json.loads(r)
        c_jp = coda(d.get('jp'))
        c_en = coda(d.get('en'))
        if c_jp:
            a = apertura(c_jp)
            conta[a] += 1
            if a not in (TILDE_LARGA, TILDE_ONDA, TILDE_ASCII):
                storpiate.append((d['riga'], c_jp[:30], c_en))
        if c_jp and not c_en:
            # ⚠️ il jsonl NON porta il campo `indice` (vale None per tutti):
            #    l'indice 3 si riconosce dalla coda, che e' il rapporto di
            #    identificazione. Senza questo taglio il conto vale 1.131 e
            #    non vuol dire niente — sono quasi tutti rapporti, il cui
            #    inglese una coda non ce l'ha mai.
            if RAPPORTO in c_jp:
                rapporti += 1
            else:
                senza_coda_en.append((d['riga'], c_jp[:30]))

    print('=== IL CARATTERE CHE APRE IL TITOLO, nelle code GIAPPONESI del corpo')
    for c, n in conta.most_common():
        print('   U+%04X  %r  %d' % (ord(c), c, n) if c else '   (vuoto)  %d' % n)

    print()
    print('=== LE CODE STORPIATE: %d' % len(storpiate))
    for riga, c_jp, c_en in storpiate:
        print('   :%d  jp %r' % (riga, c_jp))
        print('        en %s' % (repr(c_en) if c_en else 'NESSUNA CODA'))

    print()
    print('=== LE RIGHE DEL CORPO CON LA CODA IN GIAPPONESE E NON IN INGLESE: %d'
          % len(senza_coda_en))
    print('   ⓘ esclusi %d rapporti di identificazione, il cui inglese una coda'
          % rapporti)
    print('     non ce l\'ha mai: contarli dentro fa 1.131 e non dice niente.')
    print('   ⓘ `_112-verifica-fonti` non le vede: la copertura la misura solo')
    print('     dove la coda inglese c\'e\' (`if not t_en: continue`).')
    for riga, c_jp in senza_coda_en[:20]:
        print('   :%d  %r' % (riga, c_jp))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
