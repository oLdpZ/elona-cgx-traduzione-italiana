# -*- coding: utf-8 -*-
"""124a - Gli undici titoli di clan che nessun dizionario poteva raggiungere.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_124-toppa-random-title.py

⚠️⚠️⚠️ **PERCHE'.** `random_title(2)` (`etc.hsp:508`-`:525`) attacca un titolo di
clan al nome generato a caso, ed e' quel che `custom_nefiatypes.hsp:505` usa per
battezzare i servitori di Orphe nel Vuoto. Le due liste che lo compongono sono
**letterali inglesi nudi**: stanno dentro un `else` del ramo `jp` e non passano
da nessuna `lang()`, quindi non hanno firma, non hanno voce di dizionario e
nessun lotto puo' raggiungerle. E' il quinto punto cieco (`nudi_en.py`, 49a).

⭐ Sono **undici parole in due liste**, e senza di loro la resa di
`custom_nefiatypes.hsp:505` — che e' una cornice attorno a `randomname()` e
`random_title()` — non avrebbe niente di italiano da mostrare: il boss si
sarebbe chiamato «<Zaphyr>, Clan Gathering» in mezzo a un registro per il resto
tradotto.

⚠️ **Le due liste hanno due forme grammaticali, e in italiano ne resta una.**
Monte antepone nella prima («The army of Zaphyr») e **posticipa** nella seconda
(«Zaphyr Clan»); l'italiano non posticipa un sostantivo nudo a un nome proprio,
quindi anche la seconda diventa un prefisso. La varieta' si tiene cambiando le
parole, non la posizione: sono due liste distinte, come da monte.

⚠️ Niente articoli in testa («L'armata di...»): questo valore finisce in
`cdatan(CDATAN_NAME, rc)`, cioe' e' un NOME, e in questo progetto l'articolo dei
nomi lo porta il nome e non la frase (`contratto-nomi.md` §4). Un articolo
incollato qui uscirebbe due volte in ogni riga che il nome lo prende da sola.

⚠️ La toppa e' in **ASCII, commenti compresi** (123a).
"""
import io
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
TOPPE = os.path.join(RADICE, 'toppe.jsonl')

CERCA = [
    '\t\t\telse {',
    '\t\t\t\tlocvar_random_title_s2 = "Clan", "Party", "Band", "Gangs", '
    '"Gathering", "House", "Army"',
    '\t\t\t\tlocvar_randomname_s += " " + locvar_random_title_s2(rnd(7))',
    '\t\t\t}',
]
SOSTITUISCI = [
    '\t\t\telse {',
    '\t\t\t\t; TOPPA IT: in italiano un sostantivo nudo non segue un nome',
    '\t\t\t\t; proprio ("Zaphyr Clan"), quindi anche questa lista diventa un',
    '\t\t\t\t; prefisso come quella qui sopra. La varieta la tengono le',
    '\t\t\t\t; parole, non la posizione. Niente articoli: il valore finisce',
    '\t\t\t\t; in cdatan(CDATAN_NAME, rc), ed e un NOME.',
    '\t\t\t\tlocvar_random_title_s2 = "Clan ", "Congrega di ", "Banda di ", '
    '"Masnada di ", "Raduno di ", "Casata di ", "Armata di "',
    '\t\t\t\tlocvar_randomname_s = locvar_random_title_s2(rnd(7)) + '
    'locvar_randomname_s',
    '\t\t\t}',
]

CERCA2 = ['\t\t\t\tlocvar_random_title_s2 = "The army of ", "The party of ", '
          '"The house of ", "Clan "']
SOSTITUISCI2 = [
    '\t\t\t\t; TOPPA IT: gli stessi quattro titoli, gia prefissi in inglese.',
    '\t\t\t\tlocvar_random_title_s2 = "Armata di ", "Compagnia di ", '
    '"Casata di ", "Clan "',
]

MOTIVO_COMUNE = (
    "etc.hsp:508-:525, `random_title(2)`. Le due liste di titoli di clan sono "
    "LETTERALI INGLESI NUDI: stanno dentro un `else` del ramo `jp` e non "
    "passano da nessuna lang(), quindi non hanno firma, non hanno voce di "
    "dizionario e nessun lotto puo' raggiungerle (quinto punto cieco, "
    "nudi_en.py, 49a). Servono il nome dei servitori di Orphe nel Vuoto, che "
    "custom_nefiatypes.hsp:505 compone come "
    "\"<\" + randomname() + \">, \" + random_title(): senza questa toppa quel "
    "nome resta «<Zaphyr>, Clan Gathering» in mezzo a un registro tradotto. "
    "⚠️ Niente articoli in testa: il valore finisce in cdatan(CDATAN_NAME, rc), "
    "cioe' e' un NOME, e in questo progetto l'articolo dei nomi lo porta il "
    "nome e non la frase (contratto-nomi.md §4). "
)


def main():
    toppe = [
        {
            'file': 'etc.hsp',
            'motivo': MOTIVO_COMUNE + (
                "Questa e' la lista che monte POSTICIPA («Zaphyr Clan»): in "
                "italiano un sostantivo nudo non segue un nome proprio, "
                "quindi diventa un prefisso come l'altra, e la varieta' la "
                "tengono le parole invece della posizione."),
            'cerca': CERCA,
            'sostituisci': SOSTITUISCI,
        },
        {
            'file': 'etc.hsp',
            'motivo': MOTIVO_COMUNE + (
                "Questa e' la lista che monte antepone gia': cambiano solo le "
                "quattro parole."),
            'cerca': CERCA2,
            'sostituisci': SOSTITUISCI2,
        },
    ]
    for t in toppe:
        testo = ''.join(t['cerca'] + t['sostituisci'])
        assert all(ord(c) < 128 for c in testo), 'la toppa non e\' ASCII'
    with io.open(TOPPE, 'a', encoding='utf-8', newline='\n') as f:
        for t in toppe:
            f.write(json.dumps(t, ensure_ascii=False) + '\n')
    print('%d toppe aggiunte a %s' % (len(toppe), TOPPE))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
