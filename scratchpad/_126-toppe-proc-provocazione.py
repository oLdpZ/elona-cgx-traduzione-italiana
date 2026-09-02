# -*- coding: utf-8 -*-
"""Le toppe di `proc.hsp`: provocazione, insulto, <Clementia> e il colpo di Hokuto.

Sono le **15 righe nude vive** che `_126-nudi-nel-ramo-jp.py` conta in questo
file: le battute che i personaggi si dicono addosso quando usano una mossa
speciale. Non passano da nessuna `lang()`, quindi non hanno firma, non hanno
voce di dizionario e nessun lotto puo' raggiungerle. Una toppa per riga, e il
`cerca` e' la riga intera del sorgente pinnato: tutte e quindici sono uniche nel
file, controllato prima di scrivere.

## ⭐⭐⭐ L'inglese della PROVOCAZIONE e' l'inglese dell'INSULTO, e il codice lo smentisce

`:19733` e `:19736` stanno sotto `SKILL_SPACT_PROVOKE` (`:19712`), la mossa che
`:19715` annuncia come «provokes the enemy» — 挑発, il richiamo con cui si tira
addosso l'aggro. Il giapponese di `:19724` e `:19727` e' esattamente quello:
«vieni avanti», «prova a prendermi», «giochiamo?», «sei pronto?».

⚠️⚠️ **L'inglese di quelle due righe e' invece un elenco di insulti — ed e' lo
stesso identico elenco che sta sotto `SKILL_SPACT_INSULT` a `:26024` e `:26027`.**
Sette stringhe su sette ricopiate parola per parola da un'altra mossa. Il
giapponese delle due mosse non si somiglia per niente: 挑発 chiama, 罵倒 offende.
E' il difetto della 119a — «la riga gemella per costruzione» — alla scala di un
pool intero: ogni riga presa da sola e' a posto, e il guasto esiste solo nel
confronto.

⭐ **Quindi la provocazione si rende dal giapponese**, che e' l'originale e
l'unica delle due fonti che dice la cosa giusta per la mossa che la stampa. La
struttura non si tocca: il ramo `else` ha gia' lo stesso spacco sul sesso di chi
parla (`cdata(CDATA_SEX, cc) == 0`) che ha il ramo giapponese, quindi la riga
maschile prende `:19724` e quella femminile `:19727`.

⚠️ **L'insulto invece si rende dall'inglese, e non e' un'incoerenza.** A
`:26024` la mossa e' 罵倒 e l'inglese sono insulti: fa quel che deve, e non c'e'
niente da correggere. Il giapponese di li' e' piu' ricco (nove battute maschili,
diciassette femminili in due pool) e **spacca sul sesso di chi parla mentre
l'inglese tira a sorte**: se un giorno si vuole quel pool, vuole una toppa a
blocco che cambia l'`if`, ed e' una decisione, non una resa. Misurata, non presa.

## Le altre fonti lette

- `<Clementia>` resta latino (`invariati.md:414`), e `:20759` e' un gioco di
  parole sul nome della mossa: 「許してクレメンティア」 e' «perdonami» +
  «Clementia». L'italiano ce l'ha in casa e lo tiene: «Clemenza… Clementia!».
- 土下座 e' gia' reso **prostrazione** in cinque voci di dizionario, e `:20821`
  usa quella parola invece del prestito «dogeza» che scrive l'inglese.
- `:20651` ⚠️ **l'inglese ha buttato la battuta.** Il giapponese e'
  「ちょっとジャンプしてみろよ」 — *fai un saltello*, per sentire se tintinnano
  altre monete — e l'inglese ci ha messo «Hey, that's all you've got?!», che
  dice la stessa cosa della battuta dopo. Delle due inglesi ne resta una sola,
  e la prima si rende dal giapponese.
- `:20596`, `:20661`, `:20677` portano `_kure(3)`, `_dana(3)`, `_na(3)`, `_ore(3)`:
  sono i suffissi del **linguaggio di ruolo** giapponese, che scelgono la
  desinenza in base al sesso di chi parla. L'italiano non ha quel meccanismo e
  la resa e' neutra.

## ⚠️⚠️⚠️ Il colpo di Hokuto, e il participio che resta apposta

`:14386-14392` e' uno `switch` su `TWEAK_MISC_HOKUTO_NO_KEN_MODE`, cioe' una
**scelta del giocatore fra tre forme della stessa battuta**: `case 1` il
giapponese 「お前はもう死んでいる。」, `case 2` la battuta nella lingua del
gioco, `default` la **traslitterazione** «Omae wa mou shindeiru.».

- si topa **solo il `case 2`**, ed e' la battuta storica del doppiaggio italiano
  di Ken il guerriero: «Tu sei gia' morto.»;
- il `default` **non si tocca**: la traslitterazione e' il senso di quell'opzione,
  e tradurla la cancellerebbe. Va in `invariati.md`;
- ⚠️ «morto» e' un participio riferito a chi non ha genere noto, e
  `guida-stile.md` lo vieta. **Qui l'eccezione e' voluta e dichiarata**: la riga
  non descrive un personaggio, e' una **citazione**, e in italiano quella
  citazione ha una forma sola. Una versione neutra sarebbe corretta e non
  sarebbe piu' la battuta, cioe' toglierebbe l'unica cosa per cui quell'opzione
  esiste.

## Le rese e gli accenti

⚠️⚠️ **Le toppe non passano da `degrada()`.** Il dizionario tiene l'accento vero
e `applica` lo degrada scrivendo la build; una toppa invece finisce nel file
**com'e' scritta**. Per questo qui si scrive gia' «e'», «piu'», «cosi'», e nelle
1.048 toppe che c'erano prima di queste le vocali accentate sono **zero**.
ⓘ La rete c'e' gia' ed e' `test_nessuna_toppa_porta_testo_che_cp932_non_sa_scrivere`:
il codec CP932 di Python su «è» **solleva**, non degrada in silenzio. Il
controllo qui dentro non aggiunge una rete, sposta solo l'errore da dopo
`pytest` a prima della scrittura del file.

⚠️ Si compone tutto in memoria e si scrive alla fine: regola della 39a.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
NOME = 'proc.hsp'
USCITA = 'scratchpad/_126-toppe-proc.jsonl'

_QUINTO_CIECO = (
    "LETTERALE INGLESE NUDO: non passa da nessuna lang(), quindi non ha firma "
    "ne' voce di dizionario e nessun lotto puo' raggiungerlo (quinto punto "
    "cieco, nudi_en.py, 49a; triage_nudi.py, 125a). "
)

# (riga, [(letterale inglese, resa)] oppure None, riga intera nuova, motivo)
CASI = [
    (14389,
     [('"You are already dead."', '"Tu sei gia\' morto."')],
     None,
     _QUINTO_CIECO +
     "proc.hsp:14380, il colpo che uccide con TWEAK_MISC_HOKUTO_NO_KEN_MODE "
     "acceso. Lo switch di :14384 offre TRE forme della stessa battuta e le "
     "sceglie il giocatore: case 1 il giapponese, case 2 la battuta nella "
     "lingua del gioco, default la traslitterazione «Omae wa mou shindeiru.». "
     "Si topa solo il case 2, ed e' la battuta del doppiaggio italiano di Ken "
     "il guerriero; il default resta in traslitterazione perche' e' il senso "
     "di quell'opzione (dichiarato in invariati.md). "
     "⚠️ «morto» e' un participio riferito a chi non ha genere noto e "
     "guida-stile.md lo vieta: qui l'eccezione e' voluta, perche' la riga non "
     "descrive un personaggio ma **cita** una frase che in italiano ha una "
     "forma sola. Renderla neutra la cancellerebbe."),

    (19733, None,
     '\t\t\t\t\ttxt cnvtalk("Vieni avanti, e giocati la vita."), '
     'cnvtalk("Ti demoliro\' da cima a fondo."), '
     'cnvtalk("Prova a prendermi."), '
     'cnvtalk("Giochiamo un po\'?"), '
     'cnvtalk("Hai deciso di morire?"), '
     'cnvtalk("Non sforzarti: il finale non cambia."), '
     'cnvtalk("Datti meno arie.")',
     _QUINTO_CIECO +
     "proc.hsp:19712, SKILL_SPACT_PROVOKE — la provocazione (挑発), che :19715 "
     "annuncia come «provokes the enemy» e che serve a tirarsi addosso l'aggro. "
     "Chi parla e' maschio (cdata(CDATA_SEX, cc) == 0). "
     "⚠️⚠️ RESA DAL GIAPPONESE DI :19724, NON DALL'INGLESE: le sette stringhe "
     "inglesi di questa riga sono ricopiate parola per parola dal pool "
     "dell'INSULTO (:26024 e :26027), che e' un'altra mossa, e per la "
     "provocazione dicono la cosa sbagliata. Il giapponese chiama a se' — «vieni "
     "avanti», «prova a prendermi», «giochiamo?» — ed e' quello che la mossa fa. "
     "E' il difetto della 119a (la riga gemella per costruzione) alla scala di un "
     "pool intero: ogni riga presa da sola e' a posto, e il guasto esiste solo "
     "nel confronto fra le due mosse."),

    (19736, None,
     '\t\t\t\t\ttxt cnvtalk("Hai voglia di giocare con me?"), '
     'cnvtalk("Avanti, fatti sotto."), '
     'cnvtalk("Sono quiii\u2026 non mi trovi?"), '
     'cnvtalk("Su, vieni qui."), '
     'cnvtalk("Ti dispiace morire in fretta?"), '
     'cnvtalk("Vuoi che ti tenga compagnia?"), '
     'cnvtalk("Che delusioneee\u2026"), '
     'cnvtalk("Ma stai facendo sul serio?")',
     _QUINTO_CIECO +
     "La stessa provocazione di :19733 detta da una femmina (il ramo else di "
     "cdata(CDATA_SEX, cc) == 0). "
     "⚠️⚠️ RESA DAL GIAPPONESE DI :19727 per lo stesso motivo: l'inglese qui e' "
     "l'altra meta' del pool degli insulti di :26024. Il giapponese e' stuzzicante "
     "e sfottente — «sono quiii?», «ti dispiace morire in fretta?», «che "
     "delusione» — cioe' esattamente il richiamo. Le battute giapponesi sono OTTO "
     "contro le sette inglesi, e si tengono tutte: `txt` prende quante voci gli "
     "si danno e ne sorteggia una."),

    (20599,
     [('"I\'ll give you all I have, please don\'t kill me....!"',
       '"Ti do i soldi, ma lasciami vivere!"'),
      ('"You can take all my money, so please forgive me..."',
       '"E-e\' il denaro che vuoi, vero?!"')],
     None,
     _QUINTO_CIECO +
     "proc.hsp:20592, la mossa <Clementia> (命乞い, il chiedere la vita): chi la "
     "usa paga e implora. Il giapponese e' :20596. "
     "⚠️ La seconda battuta si rende dal giapponese: 「か、カネが欲しいんだな！？」 "
     "e' «e-e' i soldi che vuoi, vero?!», mentre l'inglese ci ha rimesso una "
     "seconda variante di «prendi tutto», cioe' ha ripetuto la prima. "
     "ⓘ `_kure(3)` e `_dana(3)` sono i suffissi del linguaggio di ruolo "
     "giapponese, che scelgono la desinenza sul sesso di chi parla: l'italiano "
     "non ha quel meccanismo e la resa e' neutra."),

    (20651,
     [('"Hey, that\'s all you\'ve got?!"', '"Dai, fai un saltello."'),
      ('"You definitely have more money!"', '"Altri ne hai di sicuro."')],
     None,
     _QUINTO_CIECO +
     "Chi ha incassato non si accontenta (aggro == 0 dopo il pagamento di "
     "<Clementia>). "
     "⚠️⚠️ L'INGLESE HA BUTTATO LA BATTUTA: il giapponese di :20648 e' "
     "「ちょっとジャンプしてみろよ」, «fai un saltello» — per sentire se "
     "tintinnano altre monete addosso — e l'inglese l'ha sostituita con «Hey, "
     "that's all you've got?!», che dice la stessa cosa della seconda. Delle due "
     "inglesi ne restava una sola: la prima si rende dal giapponese."),

    (20664,
     [('"Yes! Money! it\'s money..."', '"Questo si\' che e\' un affare."'),
      ('"You can go now!"', '"Puoi andare."')],
     None,
     _QUINTO_CIECO +
     "Chi ha incassato smette di attaccare (CDATA_AI_AGGRO sotto zero). Il "
     "giapponese di :20661 e' 「こりゃ儲けたな」, «bell'affare»: l'inglese «Yes! "
     "Money! it's money...» e' una riscrittura piu' scema, e la resa segue "
     "l'originale."),

    (20680,
     [('"I\'ll do anything, please don\'t kill me....!"',
       '"F-faro\' qualunque cosa, ma non uccidermi!"'),
      ('"You can do whatever you want, so please forgive me..."',
       '"Del mio corpo fanne quel che vuoi, ma lasciami andare\u2026"')],
     None,
     _QUINTO_CIECO +
     "La seconda forma di <Clementia> (rtval == 2), quella in cui si offre il "
     "corpo. Giapponese a :20677, e la seconda battuta lo dice esplicitamente "
     "(「俺の身体は好きにしていいから、見逃して…」): l'inglese la sfuma in un "
     "generico «whatever you want», e la resa tiene l'originale."),

    (20729,
     [('"I\'m not interested..."', '"Non mi interessa."'),
      ('"Gross!"', '"Che schifo!"')],
     None,
     _QUINTO_CIECO +
     "L'offerta di :20680 respinta (aggro == 0). Giapponese a :20726: "
     "「興味ないよ」, 「キモッ」 — secco e sprezzante, e l'italiano lo tiene "
     "corto com'e'."),

    (20744,
     [('"I\'ll make a mess of you!"', '"Ti riduco uno straccio."'),
      ('"Guhehe..."', '"Gu-eheh\u2026"')],
     None,
     _QUINTO_CIECO +
     "L'offerta di :20680 accettata. Giapponese a :20741: "
     "「滅茶苦茶にしてやるよ」 e' «ti faccio a pezzi / ti riduco uno straccio», e "
     "「ぐへへ…」 e' la risata sudicia, che in italiano si scrive e non si "
     "traduce."),

    (20759,
     [('"Forgive me...!"', '"Clemenza\u2026 Clementia!"'),
      ('"Please! Spare me!"', '"Chiedo scusa! Perdono!"')],
     None,
     _QUINTO_CIECO +
     "La terza forma di <Clementia> (rtval == 3). "
     "⭐ IL GIAPPONESE E' UN GIOCO DI PAROLE E L'INGLESE L'HA PERSO: "
     "「許してクレメンティア」 e' «perdonami» incollato al nome della mossa, "
     "<Clementia>. L'italiano ce l'ha in casa — clemenza / Clementia — e lo "
     "tiene. ⓘ Il nome resta latino: invariati.md:414, «il latino resta latino "
     "come in aqua sanctio»."),

    (20808,
     [('"No good..."', '"Non basta."'),
      ('"Do it on a hot iron plate!"', '"Rifallo su una piastra rovente!"')],
     None,
     _QUINTO_CIECO +
     "La prostrazione di :20759 respinta. Giapponese a :20805: 「駄目だ」 e "
     "「焼けた鉄板の上でやれ」 — «rifallo sulla piastra rovente», che e' la "
     "crudelta' della battuta e l'inglese la traduce bene."),

    (20821,
     [('"That was a magnificent dogeza..."', '"Che magnifica prostrazione\u2026"'),
      ('"Don\'t ever disobey me again!"', '"Non azzardarti a disobbedire di nuovo."')],
     None,
     _QUINTO_CIECO +
     "La prostrazione di :20759 accettata. Giapponese a :20818: "
     "「見事な土下座だ…」. ⚠️ Non «dogeza»: 土下座 e' gia' reso «prostrazione» / "
     "«prostrarsi» in cinque voci di dizionario (fra cui la mossa «Costringere a "
     "prostrarsi»), e il prestito che scrive l'inglese qui sarebbe l'unica "
     "occorrenza fuori posto."),

    (26024,
     [('"You suck!"', '"Fai schifo!"'),
      ('"You will die alone."', '"Morirai in solitudine."'),
      ('"Bow down before me."', '"Inchinati davanti a me."'),
      ('"Go jump off a bridge."', '"Vai a buttarti da un ponte."'),
      ('"Bang your head against the wall!"', '"Va\' a sbattere la testa al muro!"'),
      ('"Why do you sniff under your dog\'s tail?"',
       '"Perche\' annusi sotto la coda del tuo cane?"')],
     None,
     _QUINTO_CIECO +
     "proc.hsp:25998, SKILL_SPACT_INSULT — il ributtare addosso (罵倒), che "
     ":26002 annuncia come «insults». "
     "⚠️ QUI SI RENDE DALL'INGLESE, e non e' un'incoerenza con :19733: la' "
     "l'inglese era il pool di un'altra mossa, qui sono insulti sotto la mossa "
     "che offende, cioe' fanno quel che devono e non c'e' niente da correggere. "
     "ⓘ Il giapponese di :26010/:26014/:26017 e' piu' ricco e spacca sul sesso di "
     "chi parla dove l'inglese tira a sorte: prenderlo vuole una toppa a blocco "
     "che cambia l'`if`, ed e' una decisione aperta, non una resa. "
     "⚠️ Nessun aggettivo accordato su chi ascolta, che puo' essere il giocatore "
     "e non ha genere noto (guida-stile.md): «Fai schifo», non «Sei uno schifo»; "
     "«Morirai in solitudine», non «Morirai solo»."),

    (26027,
     [('"The world is against you because you are a unsavory decomposing virus."',
       '"Il mondo ti e\' contro, e come dargli torto: sei un virus in decomposizione."'),
      ('"You are no better than a immoral guzzling bureaucrat."',
       '"Non vali piu\' di un burocrate corrotto e ingordo."'),
      ('"You are so lowly."', '"Non sei che un verme."'),
      ('"Get off me."', '"Levati di torno."')],
     None,
     _QUINTO_CIECO +
     "L'altra meta' del pool di :26024 (il ramo else di rnd(2)). "
     "⚠️ «virus», «burocrate», «verme» sono sostantivi e non si accordano con "
     "chi ascolta: e' la strada che guida-stile.md indica dove l'inglese usa un "
     "aggettivo («you are so lowly» -> «non sei che un verme», non «sei cosi' "
     "meschino»)."),
]

ACCENTATE = 'àèéìòùÀÈÉÌÒÙ'

righe = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
nuove = []
for numero, coppie, intera, motivo in CASI:
    riga = righe[numero - 1]
    if righe.count(riga) != 1:
        raise SystemExit(f'{NOME}:{numero} compare {righe.count(riga)} volte: '
                         'il cerca va allargato a un blocco')
    if intera is not None:
        nuova = intera
        # ⚠️ La riga intera si riscrive a mano: l'indentazione e' l'unica cosa
        #    che non si puo' dedurre, e sbagliarla non fa fallire niente — HSP
        #    non se ne accorge, ma il file diventa illeggibile.
        vecchia_testa = riga[:len(riga) - len(riga.lstrip('\t'))]
        nuova_testa = nuova[:len(nuova) - len(nuova.lstrip('\t'))]
        if vecchia_testa != nuova_testa:
            raise SystemExit(f'{NOME}:{numero}: la riga nuova ha '
                             f'{len(nuova_testa)} tabulazioni invece di '
                             f'{len(vecchia_testa)}')
    else:
        nuova = riga
        for prima, dopo in coppie:
            if riga.count(prima) != 1:
                raise SystemExit(f'{NOME}:{numero} contiene {prima!r} '
                                 f'{riga.count(prima)} volte')
            nuova = nuova.replace(prima, dopo)
    if nuova == riga:
        raise SystemExit(f'{NOME}:{numero} non cambia')
    # ⚠️⚠️ Le toppe non passano da `degrada()`: una vocale accentata qui
    #    arriverebbe nella build come vocale nuda, in silenzio.
    fuori = [c for c in ACCENTATE if c in nuova]
    if fuori:
        raise SystemExit(f'{NOME}:{numero} porta {fuori}: le toppe si scrivono '
                         "gia' degradate (e', piu', cosi')")
    nuova.encode('cp932')
    nuove.append({'file': NOME, 'cerca': riga, 'sostituisci': nuova,
                  'motivo': motivo})

testo = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in nuove)
io.open(USCITA, 'w', encoding='utf-8', newline='\n').write(testo)
print(f'{len(nuove)} toppe in {USCITA}')
