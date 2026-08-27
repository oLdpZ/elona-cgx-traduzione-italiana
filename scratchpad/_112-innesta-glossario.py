# -*- coding: utf-8 -*-
"""112a - Innesta in `glossario.md` la sezione generata, senza passare dalla shell.

⚠️ Un `cat >> glossario.md` con dentro duecento righe di Markdown e' morto due
volte in questo progetto (110a) con un errore che parla della **sintassi della
shell** e non dice se abbia scritto meta' documento. Qui il testo non tocca mai
la riga di comando: si legge da un file e si scrive con Python, e la marca si
verifica prima.

Idempotente: se la sezione c'e' gia', la sostituisce invece di aggiungerne una
seconda.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_112-innesta-glossario.py
"""
from pathlib import Path

from strumenti.percorsi import PROGETTO

SEZIONE = Path(__file__).resolve().parent / 'lotti-112' / 'sezione-glossario.md'
GLOSSARIO = PROGETTO / 'glossario.md'
MARCA = '## Le righe-fonte delle descrizioni di `db_item.hsp` — 112ª'


def main():
    nuova = SEZIONE.read_text(encoding='utf-8').rstrip('\n') + '\n'
    assert nuova.startswith(MARCA), 'la sezione generata non comincia con la marca'
    base = GLOSSARIO.read_text(encoding='utf-8')

    quante = base.count(MARCA)
    assert quante <= 1, f'la marca compare {quante} volte: fermarsi e guardare'

    if quante == 1:
        inizio = base.index(MARCA)
        # la sezione finisce al prossimo titolo di pari livello, o a fine file
        dopo = base.find('\n## ', inizio + len(MARCA))
        fine = len(base) if dopo == -1 else dopo + 1
        fuori = base[:inizio] + nuova + base[fine:]
        verbo = 'sostituita'
    else:
        fuori = base.rstrip('\n') + '\n\n' + nuova
        verbo = 'aggiunta'

    GLOSSARIO.write_text(fuori, encoding='utf-8')
    print(f'sezione {verbo} in glossario.md: '
          f'{len(base.splitlines())} -> {len(fuori.splitlines())} righe')
    assert fuori.count(MARCA) == 1, 'la marca deve comparire una volta sola'


if __name__ == '__main__':
    main()
