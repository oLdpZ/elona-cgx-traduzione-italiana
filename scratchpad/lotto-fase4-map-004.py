# -*- coding: utf-8 -*-
"""Lotto fase4-map-004: i sussurri di Amurdad, gli incarichi e il tempo che
passa (map.hsp, righe 9000-13000).

51 rese, zero rinviate. `map.hsp` passa da 159 a **210 su 260**.

⭐⭐ **I tredici sussurri di Amurdad non sono testo da tradurre: sono un enigma
storpiato apposta, e la storpiatura va RIFATTA in italiano.**
`:10511`-`:10547` sono i suggerimenti che 「永遠のネヘルタード」 sussurra dentro
il Labirinto: dicono **quale scala prendere** — il dito, il colore, l'angolo — e
tutt'e due le lingue li scrivono **mangiati**, con le lettere che cadono.
`「みぎの…どに……」` e' 「右の**かど**に」, «nell'angolo destro», con due sillabe
sparite; l'inglese fa lo stesso con `«...ig...t co....r...»`, cioe'
`[r]ig[h]t co[rne]r`.
✅ **Tradurre la frase intera e' l'unico modo di sbagliare.** Se la resa dicesse
«nell'angolo destro» per intero, l'enigma non sarebbe piu' un enigma: il gioco
regalerebbe in italiano una risposta che in giapponese e in inglese si paga.
Quindi la resa italiana **rimangia le stesse parole** — «...ang...o de..ro...» —
tenendo in piedi quel che il giocatore deve poter riconoscere (pollice, indice,
medio, anulare, mignolo; blu, rosse; destro, sinistro) e mangiando il resto.
💡 Le tre righe che il giapponese scrive **intere** — `:10511` (il tasto Shift),
`:10541` (l'indice), `:10544` (il blu) — restano intere anche in italiano: sono
le conferme finali, e l'enigma e' costruito perche' arrivino chiare.

⭐ **E il modello della riga c'era gia'.** `chara_func.hsp` rende
`ネヘルタード「もう駄目…残念…」` come **`"<Amurdad>: " + cnvtalk(...)`**: il nome
si tiene inglese fra parentesi angolari — e' dichiarato cosi' in cinque righe di
`text.hsp` e in `db_creature.hsp` — e la battuta passa da `cnvtalk()`.
⚠️ **`cnvtalk` e' una funzione di CONTENUTO**, non di morfologia
(`funzioni.py:68`, `MORFOLOGIA_INGLESE` non la elenca): va conservata in tutte e
tredici le rese o la rete 11 le boccia.
⚠️ E il giapponese chiama il personaggio **ネヘルタード**, «Nehertard», mentre
l'inglese lo chiama **Amurdad**: due nomi diversi per lo stesso essere. Qui vince
l'inglese, perche' e' quel che il progetto ha gia' scritto in sei righe.

⚠️⚠️ **La rete 13 grida altre due volte, e una e' grossa.**
- `:10529` e `:10532` sono tutt'e due `«Bl.. sta...»`, ma il giapponese li
  mangia in due punti diversi — 「あお…階だ…」 contro 「あおの…いだ…」. ✅ Rese
  con due storpiature diverse, che e' la cosa giusta per un enigma: **due indizi
  identici non aiuterebbero due volte**;
- `:10847` e `:10873` sono tutt'e due «Detect the abnormal material. ... Erase
  operation is complete.», ma solo **uno dei due giapponesi dice quello**.
  `:10847` e' 「異常な物質を感知。番消去プログラムの号を作動…。」, e l'inglese lo
  rende bene; `:10873` e' 「進化プログラムの再構成を完了…。», «riconfigurazione
  del programma di evoluzione completata», che con la cancellazione di un
  materiale anomalo **non c'entra niente**. ⚠️ Non e' un appiattimento: e' la
  riga di sopra **ricopiata sulla riga di sotto**, ed e' la famiglia degli
  errori di monte. La serie passa da quarantasette a **quarantotto**.

⚠️ **E una grida della rete 3 mi ha corretto.** `:9914` e' 「何かが足元に転がっ
てきた。」, «qualcosa e' rotolato fino ai tuoi piedi», e l'avevo reso cosi'. Ma
`text.hsp:3` ha la **stessa identica firma giapponese** ed e' gia' reso
«Qualcosa viene posato per terra.» — piu' lasco, ma **gia' scritto**.
✅ Ha ragione la rete: una resa migliore in un file solo e' esattamente il
difetto che `battute --divergenti` esiste per trovare, e la 41a lo aveva gia'
segnato come punto cieco (quello strumento legge **solo** `db_creature`, quindi
una divergenza fra `map` e `text` non la vedrebbe **nessuno**). Copiata quella.
💡 Se un giorno si vuole la resa piu' letterale, si cambiano **tutt'e due
insieme**, e questa e' la riga a cui tornare.

⚠️ **Sei participi girati, e stavolta sono tutti sul giocatore.** «Sei
ripartito» (`:9175`), «Sei sceso dal carro» (`:11416`), «Hai rimesso piede»
(`:9165`): il primo e il secondo concordano col personaggio.
✅ Presente indicativo dove basta — «Scendi dal carro, a Yowyn.», «Rimetti piede
sul suolo fresco di Tyris del Nord.» — e giro di frase dove no: «Sono passati
tre anni, **e l'avventura ricomincia**.»

💡 **Il genitivo davanti a `mapname()` torna, e si risolve in due modi nuovi.**
- `:9095` «The location of X has been changed» ✅ «X **si è spostata**: da x…:y…
  a x…:y…» — il nome in testa, come nel lotto `001`;
- `:11988` «since you left X» ✅ «da quando **hai lasciato** X» — e qui non serve
  nessun giro, perche' «lasciare» regge l'**oggetto diretto**. E' la stessa
  scoperta di `:1061` del lotto `001`, e ormai e' la prima cosa da provare.

💡 **Il soggetto della camminata e' composto in tre pezzi, e l'italiano lo
regge con un gerundio.** `:12117`, `:12121` e `:12124` costruiscono `s` —
«Hai», «Tu e X avete», «Tu e i tuoi compagni avete» — e `:12128` ci attacca
«walked about N miles **and have gained** experience». ⚠️ Il secondo verbo
concorderebbe col soggetto scelto, che qui cambia. ✅ «…camminato per circa N
miglia, **guadagnando** esperienza»: il gerundio non ha ne' numero ne' persona,
e regge tutti e tre i soggetti.
⚠️ Grida della rete 3 su 「あなた」, reso «il viandante» altrove: li' e' un nome,
qui e' l'inizio di una frase verbale. Stesso pronome, due mestieri.

💡 **Tre copie pescate dal dossier** e messe tali e quali: `:9557` («si ricorda
del tuo messaggio…»), `:9853` e `:9858` («Hai imparato una nuova capacità: »).
⭐ E due nomi che erano gia' decisi: 『カルラ』 e' **«<Carla>»** e 『ミロス』 e'
**«<Milos>»**, col «Mondo Dimenticato» che `db_creature.hsp` aveva gia' scritto.
Qui si aggiunge il gemello: 忘れられ**ない**世界, il mondo che **non** si
dimentica, contro 忘れられ**た**世界. Una sillaba di differenza in giapponese,
due personaggi diversi nel gioco.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :9095 lo spostamento di una mappa sul mondo.
    # ⚠️ mapname() porta l'articolo dentro: il nome va in testa, senza «di»
    (9095, 'The location of  has been changed from x:y to x:y.'):
        '"" + mapname(p) + " si è spostata: da x" + adata(ADATA_X, p) + ":y" '
        '+ adata(ADATA_Y, p) + " a x" + x + ":y" + y + "."',

    # --- :9165-:9175 i tre anni che passano fra un atto e l'altro.
    # ⚠️ «sei ripartito» concorderebbe: girata sull'avventura
    (9165, '  Three years have passed. You set foot onto the cool soil of North Tyris once more.'):
        '  Sono passati tre anni. Rimetti piede sul suolo fresco di Tyris del Nord.',
    (9175, '  Three years have passed. You set out on adventure once more.'):
        "  Sono passati tre anni, e l'avventura ricomincia.",

    # --- :9557 ⭐ copiata dal dossier
    (9557, ' recalled your message...'):
        'cdatan(CDATAN_AKA, rc) + " si ricorda del tuo messaggio..."',

    (9600, 'Map loading failed.'):
        'Caricamento della mappa fallito.',

    # --- :9853-:9858 ⭐ copiate: la stessa riga e' gia' resa altrove
    (9853, 'You have learned a new ability, .'):
        '"Hai imparato una nuova capacità: " + skillname(SKILL_SPACT_WIN) + "."',
    (9858, 'You have learned a new ability, .'):
        '"Hai imparato una nuova capacità: " + skillname(SKILL_SPACT_PURGE) + "."',

    # --- :9914 ⭐ copiata da text.hsp:3, che ha la STESSA firma giapponese.
    # ⚠️ il primo giro diceva «Qualcosa rotola fino ai tuoi piedi.», piu' vicino
    #    a 転がってきた; ma la rete 3 ha ragione lei, e una resa migliore in un
    #    file solo e' esattamente il difetto che «battute --divergenti» cerca.
    #    Se si vuole la resa piu' letterale, si cambiano tutt'e due insieme.
    (9914, 'Something is put on the ground.'):
        'Qualcosa viene posato per terra.',

    (10460, ' You heard a growl of Big Daddy...'):
        ' Senti il ringhio di Big Daddy...',

    # --- :10511-:10547 I TREDICI SUSSURRI DI AMURDAD.
    # ⭐⭐ sono un enigma storpiato apposta: dicono quale scala prendere, e le
    #     lettere cadono in tutt'e due le lingue. Tradurre la frase intera
    #     regalerebbe in italiano una risposta che altrove si paga.
    # ⚠️ cnvtalk e' CONTENUTO (funzioni.py:68 non la elenca fra le morfologiche)
    # ⭐ «<Amurdad>» fra parentesi angolari: forma gia' fissata in text.hsp,
    #    db_creature.hsp e chara_func.hsp, che usa proprio «<Amurdad>: » + cnvtalk
    (10511, "Amurdad whispers, There's no time to spare...so run by Shift key..."):
        '"<Amurdad> sussurra: " + cnvtalk("Non c\'è tempo... corri col tasto Shift...")',
    # 「右のかどに」 = nell'angolo destro
    (10514, 'Amurdad whispers, ...ig...t co....r...'):
        '"<Amurdad> sussurra: " + cnvtalk("...ang...o de..ro...")',
    # 「ひだりのかどに」 = nell'angolo sinistro
    (10517, 'Amurdad whispers, ..ef.. c..r..er..'):
        '"<Amurdad> sussurra: " + cnvtalk("..ang..o si..st.o..")',
    (10520, 'Amurdad whispers, Go thumb stairs...again and again...'):
        '"<Amurdad> sussurra: " + cnvtalk("Vai alle scale del pollice... e ancora... e ancora...")',
    # 「なかゆびの階段」 = le scale del dito medio
    (10523, 'Amurdad whispers, ...dle.. fin...'):
        '"<Amurdad> sussurra: " + cnvtalk("...d..o m..io...")',
    # 「こゆびの階段だ」 = le scale del mignolo
    (10526, 'Amurdad whispers, ...ittl.. fin...'):
        '"<Amurdad> sussurra: " + cnvtalk("...mi...lo...")',
    # ⚠️ :10529 e :10532 hanno lo STESSO inglese e due giapponesi mangiati in
    #    punti diversi: due indizi identici non aiuterebbero due volte
    (10529, 'Amurdad whispers, Bl.. sta...'):
        '"<Amurdad> sussurra: " + cnvtalk("..a.e b.u...")',
    (10532, 'Amurdad whispers, Bl.. sta...'):
        '"<Amurdad> sussurra: " + cnvtalk("b.u... la sc..a...")',
    (10535, 'Amurdad whispers, R..d st..irs...'):
        '"<Amurdad> sussurra: " + cnvtalk("sc..e r..se...")',
    # 「くすりゆびの階段」 = le scale dell'anulare
    (10538, 'Amurdad whispers, Ri..g fi...ger st...irs...'):
        '"<Amurdad> sussurra: " + cnvtalk("an..a.e... sc..e...")',
    # 💡 le tre che il giapponese scrive INTERE restano intere: sono le conferme
    (10541, 'Amurdad whispers, Index finger stairs...'):
        '"<Amurdad> sussurra: " + cnvtalk("Le scale dell\'indice...")',
    (10544, 'Amurdad whispers, Blue stairs...'):
        '"<Amurdad> sussurra: " + cnvtalk("Le scale blu...")',
    (10547, "Amurdad whispers, There's the child...on the shore on this side..."):
        '"<Amurdad> sussurra: " + cnvtalk("Dovrebbe essere ancora... sulla riva di qua...")',

    (10557, 'Something has been crawled from the stairs!'):
        'Qualcosa è strisciato fuori dalle scale!',
    (10618, '<the pirate captain>'):
        '<il capitano dei pirati>',
    # --- :10657 la bottega, non il mestiere: qui la bottega e' la nave
    (10657, 'on the ship'):
        'sncnv(cdatan(CDATAN_NAME, rc)) + "della nave"',

    # --- :10847 e :10873 ⚠️ stesso inglese per due giapponesi SENZA NIENTE in
    #     comune: non e' un appiattimento, e' la riga sbagliata incollata
    (10847, 'Detect the abnormal material. ... Erase operation is complete.'):
        'Materiale anomalo rilevato. ... Cancellazione completata.',
    (10873, 'Detect the abnormal material. ... Erase operation is complete.'):
        'Riconfigurazione del programma di evoluzione completata...',

    # --- :10898-:10907 i quattro piani con una proprieta' strana.
    (10898, 'The floor seems to be charged.'):
        'Questo piano sembra sotto carica elettrica.',
    (10901, 'Passage of time is unstable on this floor.'):
        'Su questo piano lo scorrere del tempo è instabile.',
    (10904, 'Poison seems to fill this floor.'):
        'Questo piano sembra saturo di veleno.',
    (10907, 'Gravity is strong on this floor.'):
        'Su questo piano la gravità è forte.',

    # --- :11212-:11224 le due coppie di gemelli dei due mondi.
    # ⭐ «<Carla>», «<Milos>» e «Mondo Dimenticato» erano gia' in db_creature
    # 💡 忘れられない世界 (che NON si dimentica) contro 忘れられた世界
    (11212, '<Karura> the unforgettable singularity'):
        '<Carla> del Mondo Indimenticabile',
    (11213, '<Karura> hail flom Erusia'):
        '<Carla> del Mondo Dimenticato',
    (11223, '<Miros> the unforgettable singularity'):
        '<Milos> del Mondo Indimenticabile',
    (11224, '<Miros> hail flom Erusia'):
        '<Milos> del Mondo Dimenticato',

    # ⚠️ «sei sceso» concorderebbe
    (11416, '  You disembark from the wagon in Yowyn.'):
        '  Scendi dal carro, a Yowyn.',
    (11747, '...The basement is larger than you thought.'):
        '...La cantina di questa villa è più grande di quanto sembrasse.',
    (11763, 'This place is pretty dull. The dungeon master is no longer sighted here.'):
        'Non si avverte più nessuna tensione. Il padrone del sotterraneo non si fa più vedere.',

    # --- :11988 ⭐ «lasciare» regge l'oggetto diretto: niente giro di frase
    (11988, ' days and  hours have passed since you left .'):
        '"Sono passati " + p / 24 + " giorni e " + p \\ 24 + " ore da quando hai lasciato " '
        '+ mapname(gdata(GDATA_LAST_TOWN)) + "."',

    # --- :12117-:12128 il soggetto della camminata, composto in tre pezzi.
    # ⚠️ «and have gained» concorderebbe col soggetto, che qui cambia: gerundio
    (12117, "You've"):
        'Hai',
    (12121, 'You and  have'):
        '"Tu e " + name(locvar_map_begin_friendtc) + " avete"',
    (12124, 'You and your friends have'):
        'Tu e i tuoi compagni avete',
    (12128, ' walked about  miles and have gained experience.'):
        's + " camminato per circa " + gdata(GDATA_TRAVEL_DISTANCE) '
        '+ " miglia, guadagnando esperienza."',

    (12208, 'The students seem to have improved a bit through training.'):
        "Gli allievi sembrano cresciuti un po' con l'allenamento.",

    # --- :12215-:12231 le istruzioni dei quattro incarichi.
    (12215, 'You have to warm up the party within  minutes. Your target score is  points.'):
        '"Devi scaldare la festa entro " + gdata(GDATA_TIME_LIMIT) + " minuti. Il punteggio '
        'da raggiungere è " + qdata(QDATA_PARAM1, gdata(GDATA_QUEST_REF)) + " punti."',
    (12223, 'To complete the quest, you have to harvest  worth farm products and put them '
            'into the delivery chest within  minutes.'):
        '"Per completare l\'incarico devi raccogliere " '
        '+ cnvweight(qdata(QDATA_PARAM1, gdata(GDATA_QUEST_REF))) + " di prodotti agricoli '
        'e metterli nella cassa delle consegne entro " + gdata(GDATA_TIME_LIMIT) + " minuti."',
    (12227, 'To complete the quest, you have to remove  traps within  turns.'):
        '"Per completare l\'incarico devi disinnescare " '
        '+ qdata(QDATA_PARAM1, gdata(GDATA_QUEST_REF)) + " trappole entro " '
        '+ gdata(GDATA_TIME_LIMIT) + " turni."',
    (12231, 'You have to slay  within  minutes.'):
        '"Devi abbattere " '
        '+ refchara(qdata(QDATA_PARAM1, gdata(GDATA_QUEST_REF)), DBSPEC_CHARA_NAME_ORG, 1) '
        '+ " entro " + gdata(GDATA_TIME_LIMIT) + " minuti."',

    # --- :12281-:12303 il campo di lavoro.
    (12281, ' seems to have endured the fatigue with Toil-Energy.'):
        'cdatan(CDATAN_NAME, cnt) + " sembra aver retto alla fatica con l\'Energia da Lavoro."',
    (12303, 'It seems that  Toil-Energy has been produced. Current Toil-Energy is .'):
        '"Pare che l\'Energia da Lavoro prodotta stavolta sia " + work + ". Adesso è a " '
        '+ adata(ADATA_LABOR_CAMP_TOIL_ENERGY, gdata(GDATA_AREA)) + "."',

    (12944, ' A sudden diastrophism hits the continent.'):
        ' Un forte sconvolgimento tettonico ha colpito il continente.',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-map-004.jsonl'
DA, A = 9000, 13000
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\map.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_map.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]

# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006) o dentro un blocco (lotto 014).
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)
for v in voci:
    if sorgente[v['riga'] - 1].lstrip().startswith(';'):
        errori.append(f"rete 6: riga {v['riga']} e' commentata nel sorgente, va rinviata")
    elif v['riga'] in SPENTE:
        errori.append(f"rete 6: riga {v['riga']} sta dentro un commento di BLOCCO, va rinviata")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].rstrip().endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
        if attese != trovate:
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[chiave(v)]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v))].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
