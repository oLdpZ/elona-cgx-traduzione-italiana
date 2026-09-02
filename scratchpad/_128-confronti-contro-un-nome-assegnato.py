# -*- coding: utf-8 -*-
"""Il confronto che cerca una stringa che nessuno assegna piu'.

⚠️⚠️⚠️ **IL DIFETTO CHE QUESTO REFERTO GUARDA E' STATO TROVATO A MANO NELLA
128a, E CI SONO VOLUTE TRE SESSIONI PERCHE' NASCESSE.**

`rinviate.jsonl` portava tre voci di `proc.hsp` scritte nella 27a e nella 60a,
tutt'e tre con la stessa forma:

    «Non e' testo, e' un operando di confronto fra due file. map_rand.hsp:1287
     ASSEGNA il nome della mappa e proc.hsp:1123 lo CONFRONTA con lo stesso
     letterale. Tradurre solo il confronto lo fa fallire per sempre, in
     silenzio. Va tradotta INSIEME a map_rand.hsp: **non prima**.»

Il rinvio era giusto e la sua condizione era scritta. Solo che **l'altra meta'
e' stata tradotta**, in una sessione qualunque, e nessuno e' tornato a leggere
il rinvio: da quel giorno il confronto cercava «Party Room» mentre la mappa si
chiamava «Sala feste», e i tre rami erano morti. Un rinvio con una condizione e'
un debito che **nessuno rilegge**, e questo referto e' il promemoria che
rilegge al posto nostro.

## La regola, e perche' si tiene sul giapponese

Per ogni `X == lang(J, E)` nella build si cerca un `X = lang(J, A)` — stessa
**chiave giapponese**, che e' l'unica cosa che non cambia fra le due lingue. Se
`A != E`, cioe' l'assegnazione e' stata tradotta e il confronto no, allora la
riga del confronto **deve contenere anche il letterale `A`**, o il ramo e'
morto.

⭐ Il giapponese e' la chiave giusta e l'inglese no: e' la stessa lezione della
127a sulle famiglie sparse — «per `ai.hsp` l'inglese delle due gemelle era
diverso, a essere identico era il giapponese».

ⓘ La riparazione ammessa e' quella della migrazione di «Your Home» (toppa di
`map.hsp:1396`): il letterale italiano si aggiunge **fuori** da `lang()`, con un
`|`, e la `lang()` resta rinviata. Cosi' il confronto accetta tutt'e due e un
salvataggio scritto prima della traduzione continua a funzionare.

## ⚠️⚠️ IL NUMERO CHE CONTA NON E' IL TOTALE

Sei rami morti **ci sono gia' nel sorgente pinnato**, cioe' li ha scritti chi ha
tradotto in inglese e sono morti anche nel gioco inglese:

    command.hsp:3639   confronta «bisexual», ma tutti assegnano «hermaphrodite»
    text.hsp:359       confronta «hermaphorodite» — un REFUSO di monte
    init.hsp:1981      confronta lang("自称男性", "female?") — la coppia e' sbagliata,
                       il giapponese dice «male?» e l'inglese «female?»

Non si toccano: sono difetti di monte, e questo e' un progetto di traduzione.
Il referto li conta a parte, e il numero che fa da cancello e' **i rami morti
che la traduzione ha AGGIUNTO, atteso 0**.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_128-confronti-contro-un-nome-assegnato.py

        rami morti di monte (anche nel sorgente)  :  6
        rami morti AGGIUNTI dalla traduzione      :  0   <- il cancello

    ... --sorgente   guarda il sorgente pinnato invece della build. E' anche la
                     PROVA AL CONTRARIO: rimettendo `toppe.jsonl` senza le
                     quattro toppe della 128a e rifacendo la build, il cancello
                     passa da 0 a 4 e le nomina.
"""
import glob
import io
import os
import re
import sys

BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'

# lang("<jp>", "<en>") con letterali semplici: bastano, perche' un confronto
# contro una lang() con dentro una variabile non e' un nome di mappa.
_LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')
_CONFRONTO = re.compile(r'([A-Za-z_][A-Za-z0-9_]*\([^()]*\))\s*(?:==|!=)\s*lang\(')
_ASSEGNA = re.compile(r'^\s*([A-Za-z_][A-Za-z0-9_]*\([^()]*\))\s*=\s*lang\(')


def _albero(radice):
    fuori = {}
    for percorso in sorted(glob.glob(os.path.join(radice, '*.hsp'))):
        nome = os.path.basename(percorso)
        fuori[nome] = io.open(percorso, encoding='cp932', errors='replace').read().split('\n')
    return fuori


def _variabile(espressione):
    """`mdatan(MDATAN_NAME)` e `mdatan(0)` sono la stessa casella logica."""
    return espressione.split('(', 1)[0]


def _rami_morti(albero):
    """(chiave, descrizione) per ogni confronto che nessuno puo' piu' soddisfare.

    La chiave e' `(file, giapponese, inglese_confrontato, valore_assegnato)` e
    NON porta il numero di riga: le toppe fanno scivolare i numeri fra sorgente
    e build, e il confronto fra i due alberi si farebbe su una differenza finta.
    """
    assegnato = {}
    for nome, righe in albero.items():
        for riga in righe:
            m = _ASSEGNA.match(riga)
            if not m:
                continue
            l = _LANG.search(riga)
            if not l:
                continue
            assegnato.setdefault((_variabile(m.group(1)), l.group(1)), []).append(
                (nome, l.group(2)))

    morti = {}
    guardati = 0
    for nome in sorted(albero):
        for i, riga in enumerate(albero[nome]):
            for m in _CONFRONTO.finditer(riga):
                var = _variabile(m.group(1))
                l = _LANG.search(riga[m.end() - len('lang('):])
                if not l:
                    continue
                jp, en = l.group(1), l.group(2)
                guardati += 1
                for (dove, a) in assegnato.get((var, jp), []):
                    if a == en or '"' + a + '"' in riga:
                        continue
                    chiave = (nome, jp, en, a)
                    morti[chiave] = (
                        '{}:{}\n   confronta   {} == lang("{}", "{}")\n'
                        '   ma          {} assegna "{}"\n'
                        '   il ramo e\' MORTO: la riga non porta "{}"'
                        .format(nome, i + 1, var, jp, en, dove, a, a))
    return morti, guardati


def main(argv):
    if '--albero' in argv:
        # serve alla prova al contrario: un albero costruito a mano, per
        # controllare che il cancello si ACCENDA dove il difetto c'e' di sicuro
        radice = argv[argv.index('--albero') + 1]
        morti_albero, guardati = _rami_morti(_albero(radice))
        morti_monte, _ = _rami_morti(_albero(SORGENTE))
        aggiunti = {k: v for k, v in morti_albero.items() if k not in morti_monte}
        print('=== albero: {}  ({} confronti guardati)'.format(radice, guardati))
        for chiave in sorted(aggiunti):
            print('\n⚠️ ' + aggiunti[chiave])
        print('\n--- rami morti AGGIUNTI rispetto al sorgente: {}'.format(len(aggiunti)))
        return 1 if aggiunti else 0

    if '--sorgente' in argv:
        morti, guardati = _rami_morti(_albero(SORGENTE))
        print('=== sorgente pinnato: {} confronti guardati'.format(guardati))
        for chiave in sorted(morti):
            print('\n⚠️ ' + morti[chiave])
        print('\n--- rami morti nel sorgente: {}'.format(len(morti)))
        return 0

    morti_build, guardati = _rami_morti(_albero(BUILD))
    morti_monte, _ = _rami_morti(_albero(SORGENTE))

    di_monte = {k: v for k, v in morti_build.items() if k in morti_monte}
    aggiunti = {k: v for k, v in morti_build.items() if k not in morti_monte}

    print('=== confronti contro una lang() guardati nella build: {}'.format(guardati))

    if di_monte:
        print('\n=== DI MONTE — morti anche nel sorgente pinnato, NON si toccano')
        for chiave in sorted(di_monte):
            print('\nⓘ ' + di_monte[chiave])

    if aggiunti:
        print('\n=== ⚠️⚠️⚠️ AGGIUNTI DALLA TRADUZIONE — sono difetti nostri')
        for chiave in sorted(aggiunti):
            print('\n⚠️ ' + aggiunti[chiave])

    print('\n--- rami morti di monte (anche nel sorgente) : {:3d}'.format(len(di_monte)))
    print('--- rami morti AGGIUNTI dalla traduzione     : {:3d}   <- il cancello'
          .format(len(aggiunti)))
    if not aggiunti:
        print('\nⓘ Lo zero non e\' «non ci sono confronti»: ce ne sono {}, e i piu\' '
              'sono la\n  famiglia male/female di CDATAN_NEWSEX, dove assegnazione e '
              'confronto portano\n  la stessa stringa inglese perche\' quella famiglia '
              'e\' dichiarata invariante.\n  Vuol dire che ogni confronto accetta il '
              'valore che qualcuno gli assegna\n  davvero — le quattro toppe della '
              '128a sono li\' per questo.'.format(guardati))
    return 1 if aggiunti else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
