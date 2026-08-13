# -*- coding: utf-8 -*-
"""Genera le toppe sui blocchi `if ( en )` di proc.hsp.

⚠️ `applica` si ferma se una toppa non aggancia **o se aggancia due volte**.
Cinque di queste righe sono identiche a un'altra dello stesso file, quindi il
`cerca` non puo' essere la riga sola: qui il blocco si allarga **verso l'alto**
finche' non diventa unico, e il ramo giapponese sopra basta quasi sempre a
distinguerlo (le due scene hanno versi diversi).

Le righe si leggono dal **sorgente pinnato**: nessuna delle 23 contiene `lang()`,
quindi sono identiche nella build prima delle toppe, e leggerle da li' toglie
ogni dipendenza dall'ordine dei passaggi.
"""
import io, json, sys

from strumenti.accenti import degrada

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\proc.hsp'
righe = io.open(SORGENTE, encoding='cp932').read().split('\n')

# riga (1-based) -> la riga italiana che la sostituisce
NUOVE = {}

def _cnv(*battute):
    return 'txt ' + ', '.join(f'cnvtalk("{b}")' for b in battute)

def _cnv_nome(var, *battute):
    return 'txt ' + ', '.join(f'{var} + " " + cnvtalk("{b}")' for b in battute)

# --- i versi della scena, tutti dentro 「」 nel giapponese: tutti cnvtalk
NUOVE[3319] = _cnv('Iiih...', 'Che morbido...', 'Che umiliazione... eppure...',
                   'Hah... hah!', 'Uh uh uh...')
NUOVE[3487] = NUOVE[3319]
NUOVE[3574] = _cnv('Che morbido...', 'Che umiliazione... eppure...',
                   'Hah... hah!', 'Uh uh uh...')

# --- la frase che apre le virgolette e le chiude altrove (:3376, :3383, :3389).
#     ⚠️ Tutte invarianti: chi parla e chi ascolta hanno genere ignoto.
#     «Sei stato bravissimo» sbaglierebbe meta' delle partite.
_FINE = ['Che bello...', 'I-incredibile!', 'N-non ne posso più...',
         'C-che impeto...', 'H-ho perso su tutta la linea...']
_apre = 'txt ' + ', '.join(f'"\\"{b}"' for b in _FINE)
NUOVE[3372] = _apre
NUOVE[3533] = _apre
NUOVE[3617] = _apre

# --- onomatopee. ♪ e' l'unico carattere a due byte ammesso.
NUOVE[3822] = 'txt " *clang* ", " *♪* ", " *tonf* ", " *crac...* "'
NUOVE[3851] = 'txt " *zac* ", " *♪* ", " *tonf* ", " *scric* "'
NUOVE[4865] = 'txt " *ciaf* ", " *zac* ", " *plop* ", " *sciff* "'
NUOVE[4898] = NUOVE[4865]
NUOVE[4926] = 'txt " *sciaf* ", " *splash* ", " *plaf* ", " *sciab* "'

# --- le allucinazioni. ⚠️ Il giapponese usa il possessivo `name(cc)の`, e in
#     italiano «di» davanti a name() darebbe «di il cane»: le quattro frasi sono
#     state girate perche' name(cc) faccia da SOGGETTO.
NUOVE[9862] = (
    'txt name(tc) + " ha le allucinazioni: " + name(cc) + " ha il ventre squarciato e brulicante di vermi.", '
    'name(tc) + " ha le allucinazioni: " + name(cc) + " divora cadaveri.", '
    'name(tc) + " trema: " + name(cc) + " ha uno sguardo terribile.", '
    'name(tc) + " ha la nausea: " + name(cc) + " ha i tentacoli impigliati nelle viscere."'
)

# --- chi ti porta in groppa. ⚠️ Il giapponese distingue i due siti, l'inglese
#     li appiattisce sulle stesse quattro battute: qui tornano diversi.
NUOVE[10768] = _cnv_nome('name(gdata(GDATA_RIDER))',
                         'Fiuu.', 'Comoda la cavalcata?', 'Che fatica...',
                         'Risalimi in groppa quando vuoi♪')
NUOVE[10781] = _cnv_nome('name(gdata(GDATA_RIDER))',
                         'Ooop.', 'Che bella cavalcata!', 'Che fatica, eh?',
                         'Ci risalirei volentieri♪')

NUOVE[10847] = _cnv_nome('name(tc)',
                         'Ugh...', "Mettiti a dieta, va'...", 'Si parte!',
                         'Vacci piano, mi raccomando♪')
# ⚠️ Il giapponese di :10857 nomina il giocatore con titolo e nome, e l'inglese
#    li butta via. Vocativo, perche' `cdatan(CDATAN_NAME, ...)` porta dentro
#    l'articolo e una preposizione davanti darebbe «a il cane».
NUOVE[10860] = (
    'txt name(tc) + " " + cnvtalk(cdatan(CDATAN_AKA, CHARA_PLAYER) + ", " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ": in sella!"), '
    'name(tc) + " " + cnvtalk("Non peso troppo?"), '
    'name(tc) + " " + cnvtalk("Non scuoterti troppo, eh."), '
    'name(tc) + " " + cnvtalk("Andiamooo♪")'
)

# --- ⚠️ Qui l'inglese ha UNA battuta e il giapponese TRE: arbitra il giapponese.
NUOVE[21986] = ('txt name(tc) + " si contorce in silenzio!", '
                'cnvtalk("N-non guardarmi così!"), "*patapum♪*"')
NUOVE[22027] = ('txt name(tc) + " resta impassibile!", '
                'name(tc) + " guarda " + name(cc) + " con la faccia seria..."')
NUOVE[22489] = (
    'txt name(tc) + " si contorce dalle risate!", '
    'name(tc) + " cerca disperatamente di tenere occhi e bocca chiusi!", '
    'name(tc) + " si dimena con violenza!", '
    'name(tc) + " ride fra lacrime e sudore!"'
)
NUOVE[22497] = _cnv_nome('name(tc)',
                         'Hi! Hiii!', 'Ahahahah!!', 'Hahahahaha!', 'Nghiiii!?',
                         'Gaaah...! Haaa!', 'I... hi-hihiii...!', 'Cuuh... nnh!!',
                         'Basta! Bas...!')
NUOVE[22506] = _cnv_nome('name(tc)',
                         'Bastaaa... deeeh!', 'Hyahahahaha!!!',
                         '...Cof! Cof!! Uuuh... ueegh!', 'I... hiiii!!!',
                         'A-ahahah...!', 'A-hyaaaa AAAAAH!!?', 'Nhiiiih...!!!',
                         'Ghiiiiaaaaah!!')
# ⚠️ «Starò attento» concorderebbe con chi parla: «Ci farò attenzione» no.
#    ＯＫ resta: e' prestito in tutte e due le lingue.
NUOVE[26818] = _cnv_nome('name(tc)',
                         'Ricevuto!', 'Ci farò attenzione', 'Ah, ecco...', 'OK')
NUOVE[26886] = _cnv_nome('cdatan(CDATAN_NAME, tc)',
                         'Non darmi ordini!',
                         "Stavo giusto per farlo, e adesso mi è passata la voglia.")

MOTIVO = (
    "Blocco `if ( en )` con letterali **nudi** fuori da `lang()`: estrai.py non li "
    "vede, quindi il dizionario non li raggiunge e restano inglesi anche a file "
    "«tradotto». Sono 23 righe in proc.hsp (scratchpad/blocchi_en.py le elenca), e "
    "sono la stessa classe della scoperta 1 della 28ª su bufftxt. ⚠️ Il giapponese "
    "arbitra il contenuto: dove l'inglese ha meno battute del ramo jp (:21986 una "
    "contro tre, :22027 una contro due, :22489 due contro quattro) la resa segue il "
    "giapponese, e dove l'inglese appiattisce due scene diverse sulle stesse battute "
    "(:10768/:10781, :10847/:10860) le due tornano distinte."
)


def _codificabile(c: str) -> bool:
    try:
        c.encode('cp932')
        return True
    except UnicodeEncodeError:
        return False


def blocco_unico(n: int) -> list[str]:
    """Il blocco piu' corto che finisce alla riga n ed e' unico nel file."""
    for altezza in range(1, 25):
        blocco = righe[n - altezza:n]
        quanti = sum(1 for i in range(len(righe) - len(blocco) + 1)
                     if righe[i:i + len(blocco)] == blocco)
        if quanti == 1:
            return blocco
    raise SystemExit(f'riga {n}: nessun blocco unico entro 24 righe')


toppe = []
for n in sorted(NUOVE):
    originale = righe[n - 1]
    indent = originale[:len(originale) - len(originale.lstrip())]
    # ⚠️ `applica` degrada gli accenti SOLO per le voci di dizionario: le toppe
    #    le scrive grezze, e `nuovo.encode("cp932")` e' strict, quindi un accento
    #    farebbe fallire la catena. Si degrada qui.
    nuova = indent + degrada(NUOVE[n])
    residuo = [c for c in nuova if c != '♪' and not _codificabile(c)]
    if residuo:
        raise SystemExit(f'riga {n}: caratteri che CP932 non sa scrivere: {residuo}')
    if nuova == originale:
        raise SystemExit(f'riga {n}: la toppa non cambierebbe niente')
    cerca = blocco_unico(n)
    sostituisci = cerca[:-1] + [nuova]
    toppe.append({
        'file': 'proc.hsp',
        'cerca': cerca if len(cerca) > 1 else cerca[0],
        'sostituisci': sostituisci if len(sostituisci) > 1 else sostituisci[0],
        'motivo': f'proc.hsp:{n}. {MOTIVO}',
    })
    print(f'{n:6d}  blocco di {len(cerca)} riga/e')

with io.open('lavoro/toppe-proc-en.jsonl', 'w', encoding='utf-8', newline='\n') as f:
    for t in toppe:
        f.write(json.dumps(t, ensure_ascii=False) + '\n')
print(f'{len(toppe)} toppe -> lavoro/toppe-proc-en.jsonl')
