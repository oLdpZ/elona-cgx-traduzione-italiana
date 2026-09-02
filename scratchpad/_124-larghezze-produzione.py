# -*- coding: utf-8 -*-
"""124a - Il cancello di larghezza del pannello della PRODUZIONE.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_124-larghezze-produzione.py

⚠️⚠️⚠️ **PERCHE' ESISTE, ED E' UN PANNELLO CHE NESSUNO AVEVA MAI MISURATO.** La
123a ha misurato il pannello dei *materiali posseduti* (`*com_material`,
`material.hsp:429`-`:470`). Questo e' l'**altro** — `*com_product`, la finestra
che si apre col kit e in cui si fabbrica — e ha **tre** colonne, non due, con
**due font diversi nella stessa finestra**:

    :220  display_window ..., 640, 448          la finestra
    :235  gfini 540, 18   da pos wx+70          la riga: wx+70 .. wx+610
    :299  font ..., 14 - en * 2, 0              font **12** per l'elenco
    :306  cs_list cnven(s), wx + 86             la colonna del NOME
    :307  pos wx + 308  : mes s(1)              la colonna «Crea [nome]»

    :252  font ..., 13 - en * 2, 0              font **11** per il dettaglio
    :273  pos wx + 37,  wy + 288                la riga dell'abilita' richiesta
    :288  pos wx + 37 + cnt \\ 3 * 192           i materiali, TRE colonne da 192

⭐ **I due metri sono gia' pagati e non si ritarano**: 7,7 px/carattere a font
12 (`larghezze.py`, i menu) e 6,9 px/carattere a font 11 (il corpo impaginato
del pannello degli oggetti, 112a). ⚠️ Confonderli allenta un cancello in
silenzio — e' la lezione della 112a, e qui i due font stanno a venti righe di
distanza dentro la stessa schermata.

⚠️⚠️ **LA COLONNA DEI MATERIALI E' LA PIU' STRETTA DI TUTTO IL PROGETTO**: 192 px
a font 11 fanno **27** caratteri, e dentro ci sta `nome + " x " + quanti +
"(" + posseduti + ")"`. Il budget della 123a era 27 per `nome + " x N"`; qui
la coda e' piu' lunga di quella, sullo **stesso** insieme di nomi.

⭐ **E il modello si legge sull'inglese di monte**, che per queste tre colonne
sta dentro: se una colonna italiana sfora e quella inglese no, e' il nostro
lavoro a non starci, non il modello a essere sbagliato.

⚠️ Si legge la **BUILD**, non il sorgente: i nomi degli oggetti non passano da
`lang()` (`db_item.hsp:137225`, dentro un `else` del ramo `jp`) e in italiano
li scrive `applica`. Su una macchina senza albero costruito questo strumento
muore di file non trovato, come `gronde` e `_97-toppe-agganciate`.
"""
import io
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
sys.path.insert(0, RADICE)

from strumenti import percorsi  # noqa: E402

SORGENTE = percorsi.SORGENTE_HSP
BUILD = percorsi.BUILD_HSP

PX_FONT12 = 7.7     # larghezze.py, misurato sui menu
PX_FONT11 = 6.9     # 112a, il corpo impaginato del pannello degli oggetti

PX_NOME = 308 - 86          # 222  colonna del nome, font 12
PX_CREA = 610 - 308         # 302  colonna «Crea [nome]», font 12
PX_ABILITA = 610 - 37       # 573  la riga dell'abilita', font 11

BUDGET_NOME = int(PX_NOME / PX_FONT12)              # 28
BUDGET_CREA = int(PX_CREA / PX_FONT12)              # 39
BUDGET_ABILITA = int(PX_ABILITA / PX_FONT11)        # 83

# ⚠️⚠️ IL PASSO DELLE COLONNE DEI MATERIALI SI LEGGE, NON SI SCRIVE QUI. Monte
# ne mette **tre da 192 px** (`material.hsp:288`) e la build italiana **due da
# 288**, per la toppa della 124a: un numero fisso qui misurerebbe la geometria
# di un albero sull'altro, che e' il modo di allentare un cancello senza
# accorgersene (112a). Si prende dalla riga che disegna, in ciascun albero.
RE_COLONNE = re.compile(
    r'^\s*pos wx \+ 37 \+ cnt \\ (\d+) \* (\d+), wy \+ 334 \+ cnt / \d+ \* 16')

# ⚠️⚠️ IL CONTATORE FA PARTE DELLA STRINGA, e qui ce ne sono DUE: quanti ne
# chiede la ricetta e quanti se ne posseggono. `mat()` non ha nessun tetto in
# tutto il sorgente (123a), quindi i posseduti si contano a CINQUE cifre; i
# richiesti li dice la ricetta e si leggono uno per uno.
CIFRE_POSSEDUTI = 5

# ⚠️ La riga dell'abilita' e' `"Abilita' richiesta: " + nome + " " + livello +
#   "(" + posseduto + ")"` (`material.hsp:253`-`:266`): due numeri a tre cifre.
CODA_ABILITA = len(' 100(100)')

RE_RECIPE = re.compile(r'^\s*if \( matid == (ITEM_ID_\w+) \)')
RE_MATVAL = re.compile(r'^\s*matval = (SKILL_NORMAL_\w+),')
RE_MATNEED = re.compile(r'^\s*matneed = (.+)$')
RE_NOME_ITEM = re.compile(
    r'^\s*ioriginalnameref\((ITEM_ID_\w+)\) = "(.*)"\s*$')
RE_MATNAME = re.compile(
    r'^\s*matname\((MATERIAL_\w+)\) = lang\("(?:.*?)", "(.*)"\)\s*$')
# le quattro abilita' del pannello, rese nel lotto di oggi
RE_SKILLNAME = {
    'SKILL_NORMAL_ALCHEMY': 255,
    'SKILL_NORMAL_CARPENTRY': 258,
    'SKILL_NORMAL_JEWELER': 261,
    'SKILL_NORMAL_TAILORING': 264,
}


def righe(cartella, nome):
    percorso = os.path.join(cartella, nome)
    return io.open(percorso, encoding='cp932', errors='replace').read().split('\n')


def ricette(db_item):
    """matid -> (abilita', [(materiale, quanti), ...]), dal blocco *recipe_ref."""
    dentro = False
    fuori = {}
    corrente = None
    for riga in db_item:
        if riga.startswith('*recipe_ref'):
            dentro = True
            continue
        if not dentro:
            continue
        if riga.startswith('*') and not riga.startswith('*recipe_ref'):
            break
        m = RE_RECIPE.match(riga)
        if m:
            corrente = m.group(1)
            fuori[corrente] = [None, []]
            continue
        if corrente is None:
            continue
        m = RE_MATVAL.match(riga)
        if m:
            fuori[corrente][0] = m.group(1)
            continue
        m = RE_MATNEED.match(riga)
        if m:
            pezzi = [p.strip() for p in m.group(1).split(',')]
            if pezzi[0] == '-1':
                continue
            coppie = []
            for i in range(0, len(pezzi) - 1, 2):
                if not pezzi[i].startswith('MATERIAL_'):
                    break
                coppie.append((pezzi[i], int(pezzi[i + 1])))
            fuori[corrente][1] = coppie
    return fuori


def nomi_oggetto(db_item):
    """ITEM_ID -> nome disegnato. L'ultimo vince: il ramo `else` segue il `jp`."""
    fuori = {}
    for riga in db_item:
        m = RE_NOME_ITEM.match(riga)
        if m:
            fuori[m.group(1)] = m.group(2)
    return fuori


def nomi_materiale(material_data):
    fuori = {}
    for riga in material_data:
        m = RE_MATNAME.match(riga)
        if m:
            fuori[m.group(1)] = m.group(2)
    return fuori


def nomi_abilita(material):
    """Le quattro rese di `material.hsp`, prese dalla riga che le scrive."""
    fuori = {}
    for costante, _ in RE_SKILLNAME.items():
        pass
    testo = '\n'.join(material)
    for costante in RE_SKILLNAME:
        # `if ( matval == SKILL_NORMAL_X ) {` e la riga dopo e' `s += lang(...)`
        m = re.search(r'matval == %s \) \{\s*\n\s*s \+= lang\("(?:.*?)", "(.*?)"\)'
                      % costante, testo)
        fuori[costante] = m.group(1) if m else '?'
    return fuori


def misura(cartella, etichetta):
    db_item = righe(cartella, 'db_item.hsp')
    rec = ricette(db_item)
    oggetti = nomi_oggetto(db_item)
    materiali = nomi_materiale(righe(cartella, 'material_data.hsp'))
    abilita = nomi_abilita(righe(cartella, 'material.hsp'))
    prefisso = righe(cartella, 'material.hsp')
    testo = '\n'.join(prefisso)
    m = re.search(r'lang\("必要スキル: ", "(.*?)"\)', testo)
    if m is None:
        m = re.search(r's = lang\("(?:.*?)", "(Skill needed: |.*?)"\)', testo)
    etichetta_abilita = m.group(1) if m else 'Skill needed: '
    m = re.search(r'lang\("アイテム\[" \+ s \+ "\]", "(.*?)\[" \+ s \+ "\]"\)', testo)
    verbo = m.group(1) if m else 'Make '

    colonne, passo = None, None
    for riga in prefisso:
        m = RE_COLONNE.match(riga)
        if m:
            colonne, passo = int(m.group(1)), int(m.group(2))
            break
    assert passo, 'la riga che incolonna i materiali non si trova'
    budget_materiale = int(passo / PX_FONT11)

    fuori = []
    print()
    print('  === %s' % etichetta)
    print('    ricette lette: %d   materiali nominati: %d   oggetti: %d'
          % (len(rec), len(materiali), len(oggetti)))
    print('    materiali incolonnati: %d colonne da %d px  ->  %d caratteri'
          % (colonne, passo, budget_materiale))
    print('    etichetta abilita\': %r    verbo della colonna: %r'
          % (etichetta_abilita, verbo))

    # --- 1. la colonna del NOME, font 12
    lunghi = []
    for matid in rec:
        nome = oggetti.get(matid)
        if nome is None:
            continue
        if len(nome) > BUDGET_NOME:
            lunghi.append((len(nome), matid, nome))
    print('    NOME        budget %2d: %d fuori su %d'
          % (BUDGET_NOME, len(lunghi), len(rec)))
    for n, matid, nome in sorted(lunghi, reverse=True):
        print('       %3d  %-40s %s' % (n, nome, matid))
    fuori += lunghi

    # --- 2. la colonna «Crea [nome]», font 12
    lunghi = []
    for matid in rec:
        nome = oggetti.get(matid)
        if nome is None:
            continue
        riga = '%s[%s]' % (verbo, nome)
        if len(riga) > BUDGET_CREA:
            lunghi.append((len(riga), matid, riga))
    print('    CREA[...]   budget %2d: %d fuori su %d'
          % (BUDGET_CREA, len(lunghi), len(rec)))
    for n, matid, riga in sorted(lunghi, reverse=True):
        print('       %3d  %-40s %s' % (n, riga, matid))
    fuori += lunghi

    # --- 3. i materiali richiesti, font 11, la colonna piu' stretta
    lunghi = []
    viste = set()
    for matid, (_, coppie) in rec.items():
        for materiale, quanti in coppie:
            nome = materiali.get(materiale)
            if nome is None:
                continue
            riga = '%s x %d(%s)' % (nome, quanti, '9' * CIFRE_POSSEDUTI)
            chiave = (materiale, quanti)
            if chiave in viste:
                continue
            viste.add(chiave)
            if len(riga) > budget_materiale:
                lunghi.append((len(riga), materiale, riga))
    print('    MATERIALE   budget %2d: %d fuori su %d combinazioni'
          % (budget_materiale, len(lunghi), len(viste)))
    for n, materiale, riga in sorted(lunghi, reverse=True):
        print('       %3d  %-40s %s' % (n, riga, materiale))
    fuori += lunghi

    # --- 4. la riga dell'abilita' richiesta, font 11
    lunghi = []
    for costante, nome in sorted(abilita.items()):
        riga = etichetta_abilita + nome + '%s' % ('X' * CODA_ABILITA)
        if len(riga) > BUDGET_ABILITA:
            lunghi.append((len(riga), costante, riga))
    print('    ABILITA\'    budget %2d: %d fuori su %d   (%s)'
          % (BUDGET_ABILITA, len(lunghi), len(abilita),
             ', '.join(sorted(abilita.values()))))
    for n, costante, riga in sorted(lunghi, reverse=True):
        print('       %3d  %s' % (n, riga))
    fuori += lunghi
    return fuori, materiali, rec, budget_materiale


def main():
    print()
    print('  metri: %.1f px/carattere a font 12, %.1f a font 11'
          % (PX_FONT12, PX_FONT11))
    print('  posseduti contati a %d cifre (mat() non ha tetto, 123a)'
          % CIFRE_POSSEDUTI)

    fuori_en, _, _, budget_en = misura(SORGENTE, 'inglese di monte')
    fuori_it, materiali, rec, budget_it = misura(BUILD, 'build italiana  (atteso 0)')

    # ⚠️⚠️ Prova al contrario: NON una stringa finta, che si accende sempre e
    # non dimostra niente. Si rimisurano le STESSE rese italiane contro il
    # passo di **monte** (tre colonne da 192 px): se il cancello e' vivo, li'
    # deve accendersi — ed e' esattamente il difetto che la toppa della 124a ha
    # chiuso. Si stampa dove si accende e di quanto, non un ✅.
    print()
    budget_stretto = int(192 / PX_FONT11)
    combinazioni = {(m, q)
                    for _, coppie in rec.values() for m, q in coppie}
    righe_it = sorted(
        (len('%s x %d(%s)' % (materiali[m], q, '9' * CIFRE_POSSEDUTI)),
         '%s x %d(%s)' % (materiali[m], q, '9' * CIFRE_POSSEDUTI))
        for m, q in combinazioni if m in materiali)
    accese = [r for r in righe_it if r[0] > budget_stretto]
    print('  prova al contrario: le stesse %d combinazioni italiane, rimisurate'
          % len(righe_it))
    print('    contro il passo di MONTE (3 colonne da 192 px = %d caratteri):'
          % budget_stretto)
    if accese:
        print('    il cancello SI ACCENDE su %d, la peggiore a %d — «%s».'
              % (len(accese), accese[-1][0], accese[-1][1]))
        print('    E\' il difetto che la toppa della 124a ha chiuso allargando')
        print('    la colonna da %d a %d caratteri: lo zero qui sopra ha una'
              % (budget_stretto, budget_it))
        print('    ragione, non e\' che non l\'ho cercato.')
    else:
        print('    ⚠️ NON si accende: il cancello e\' tarato troppo largo.')
    print()
    return 1 if fuori_it or not accese else 0


if __name__ == '__main__':
    sys.exit(main())
