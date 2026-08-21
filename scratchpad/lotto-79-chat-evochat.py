# -*- coding: utf-8 -*-
"""79a — `chat.hsp`, il sistema degli EVOCHAT, intero.

Non e' un parlante: e' un **sistema**, come le gilde della 78a. Sta in cinque
pezzi lontani fra loro e va preso tutto insieme, perche' il menu e la risposta
si leggono di seguito:

    18866-19235   le reazioni del compagno durante l'evochat (`buff` e `txt`)
    19242-19319   i cinque menu (evochat -1, 1, 11, 2, 3)
    19430-19437   i due ingressi dal menu principale     (gia' resi)
    19504-19506   l'ingresso oscuro                      (gia' reso)
    21362-21979   i venticinque `chatval` che li servono

⭐⭐⭐ **Il motivo per aprirlo adesso: e' il difetto della 78a GIRATO.** I tre
ingressi — «<evochat>», «<evochat in coppia>», «<evochat oscuro>» — sono
**gia' italiani** dalla 73a, e sotto c'e' un sottosistema tutto inglese. Nessuna
rete lo misura: `bilingui` guarda i gruppi di `chatList`, e un menu tutto
inglese non e' bilingue. Si vede solo chiedendo *dove porta* una voce resa.

⭐ **Il perimetro vero, col conto della 78a** (`scratchpad/perimetro-zona.py`):
109 firme non tradotte con almeno un'occorrenza nella zona, 110 occorrenze, e
**zero** con occorrenze fuori. E' il lotto piu' chiuso di `chat.hsp`: nessuna
firma condivisa da accendere altrove.

⭐⭐⭐ **Il lessico non si e' deciso: si e' ripreso.** Le dieci «route» non sono
dieci parole nuove — sono le dieci **scale di rapporto** di `text.hsp:33`-`43`
(`_impressiona1`-`7`, `_impressionb1`-`3`), gia' tradotte, che il gioco stampa
sulla finestra del dialogo (`chat.hsp:25620`) e nel messaggio di
`chara_func.hsp:1080`, «Il rapporto con X diventa <Y>...». Ogni `chatval`
scrive `CDATA_HEART_LOCK_RELATION` e sceglie la scala:

    119 -> -1  _impressiona1  Compagno / Legame di battaglia
    120 -> -2  _impressiona2  Amico / Confidente / Anima gemella
    121 -> -3  _impressiona3  Concorrente / Rivale / Nemesi
    122 -> -4  _impressiona4  Innamoramento / Passione / *Amore*
    123 -> -5  _impressiona5  Tutela / Successione / *Discepolato*
    124 -> -6  _impressiona6  Insegnamento / Magistero / Venerazione
    125 -> -7  _impressiona7  Famiglia / Affetto / Devozione
    126 -> -11 _impressionb1  Contratto / Sodalizio / Legame del destino
    127 -> -12 _impressionb2  Appartenenza / Sottomissione / Dipendenza
    128 -> -13 _impressionb3  Fedelta' / Obbedienza / Lealta'

Quindi il messaggio dice la parola che il giocatore rilegge subito dopo sotto
il ritratto. Stessa cosa per i due esiti dello scasso: `command.hsp:2502` e
`:2507` chiamano i due tratti «Nessun **cruccio**» e «**Passatempo pericoloso**»,
e le due righe di `:21732` e `:21750` dicono quelle parole.

⚠️⚠️ **`name(cc)` in `*chat_default` e' il GIOCATORE** (`cc = CHARA_PLAYER`, e lo
conferma `:22124`, dove `name(cc)` decapita il prigioniero). Monte lo usa per
tre righe che parlano del **compagno**: `:21732`, `:21750` e `:21867`. Il
giapponese dice `name(tc)` tutt'e tre le volte, e il codice gli da' ragione
(`cbitmod ..., tc`). E' la 77a, caso 1: si segue il codice. Le prime due sono
di oggi; la terza e' una resa vecchia, e va **corretta** — vedi
`scratchpad/correzione-79-monete-coppia.py`.

⚠️⚠️ **L'inglese ha perso dodici battute**, e le ha sostituite con due
segnaposto ripetuti: «name is staring at you with a happy expression» otto
volte (`:19053`, `:19080`, `:19103`, `:19107`, `:19110`, `:19158`, `:19162`,
`:19165`) e «name seems to be a little pounding» due (`:19049`, `:19056`).
Il giapponese ha otto battute diverse. **Deroga dichiarata**: si segue il
giapponese, come `:1744` e `:1866` nella 78a. Il nome resta perche' `verifica`
pretende le funzioni di contenuto dell'inglese, e perche' attribuisce la
battuta: la forma e' quella di `:8888`.

⚠️ **Il divieto di genere vale su tutt'e tre i soggetti, e qui tutti e tre sono
ignoti**: il compagno (qualunque creatura), il giocatore (le voci di menu le
dice lui: «Sono innamorato» ✗ -> «Ho perso la testa per te» ✓) e il compagno di
coppia. Nessun participio, nessun aggettivo che concordi con una persona.

⚠️ **`is(tc)`, `_s(cc)` e `his(cc)` a un argomento sono morfologia e si
tolgono.** `cnvtalk()` porta le virgolette da fuori, quindi la resa e' nuda.
"""
import io
import json
import sys

ZONE = [(18866, 19235), (19242, 19319), (19430, 19437), (19504, 19506),
        (21362, 21979)]
ESTRAZIONE = 'scratchpad/_79-chat-tutte.jsonl'
DIZIONARIO = 'dizionario/chat.hsp.jsonl'
USCITA = 'lavoro/fase4-chat-evochat.jsonl'

RESE = {
    # ---- le reazioni del compagno, evochat == -1 (lo scasso del cuore) ----
    (18869, '( seems to open up to you...)'):
        '"(" + name(tc) + " sta per aprirti il cuore...)"',
    (18872, 'What are you gonna do to me?'):
        'Che cosa hai intenzione di farmi?',
    (18877, '( envisions a future relationship...)'):
        '"(" + name(tc) + " immagina già come sarà, fra voi due...)"',
    (18880, 'Once again, I look forward to adventuring with you!'):
        'Di nuovo insieme: conto su di te!',
    # 心を閉ざしている, non «embarrassed»: e' lo stato di SCASSO FALLITO (hyouzyou 6)
    (18885, '( seems to be embarrassed.)'):
        '"(" + name(tc) + " chiude il cuore a chiave...)"',
    (18888, "Don't step into my heart so easily!"):
        'Non entrarmi nel cuore con tanta leggerezza!',
    # hyouzyou 5: e' l'esito di «Voglio esserti d'aiuto» -> «Nessun cruccio»
    (18893, '( get rids of the worries and eases...)'):
        '"(" + name(tc) + " si lascia alle spalle i crucci, e quasi non ci crede...)"',
    (18896, "It's strange, why would I worry about that."):
        'Che strano: e pensare che me ne facevo un cruccio.',
    (18901, '(  staring at you in a dangerous smile.)'):
        '"(" + name(tc) + " ti fissa con un sorriso pericoloso.)"',
    (18904, 'Ahh...You will take responsibility, right?'):
        'Ah... la responsabilità te la prendi tu, vero?',

    # ---- le reazioni, evochat == 1 (l'evochat normale) ----
    (18919, '( seems to be a bit nervous.)'):
        '"(" + name(tc) + " sembra un po\' in tensione.)"',
    (18922, "It's just the two of us..."):
        'Qui non ci disturba nessuno...',
    # 反応に困っている: non sa come reagire
    (18933, '( seems to be embarrassed.)'):
        '"(" + name(tc) + " non sa che pesci pigliare...)"',
    (18936, 'P...Please quit the joke in a place like this!'):
        'S-smettila di scherzare, non qui!',
    (18947, '(  pleased.)'):
        '"(" + name(tc) + " si illumina!)"',
    (18950, 'This kind of thing is really nice...'):
        'Queste cose mi fanno davvero piacere...',
    (18962, '(  staring at you with a happy expression.)'):
        '"(" + name(tc) + " ti fissa con un\'espressione felice.)"',
    (18965, '... I am very happy now.'):
        'cdatan(CDATAN_NAME, CHARA_PLAYER) + "... adesso sono davvero felice."',

    # ---- le reazioni, evochat == 11 (l'evochat oscuro) ----
    (18975, "Stop...you're trying to be rough with me, aren't you?"):
        'Basta... vuoi essere brutale con me, vero?',
    (18978, "Yes...I won't defy you..."):
        'Sì... non mi opporrò a te...',
    (18983, '( looks grimaced with pain.)'):
        '"(" + name(tc) + " storce il viso dal dolore.)"',
    (18986, "It...It doesn't hurt at all..."):
        'N-non fa mica male...',
    (18989, 'Ugh...!'):
        'Ngh...!',
    (18996, '( is surprised and confused.)'):
        '"(" + name(tc) + " sgrana gli occhi, senza capire.)"',
    (18999, 'Mugh...!? Mmmmhhm!!'):
        'Mmgh...!? Mmmh mmh!!',
    (19002, "It, it's delicious...?"):
        'M-ma è... buono?',
    (19009, 'What...do you mean all of a sudden?'):
        'Ih... e questo da dove salta fuori?',
    (19012, "...It's kind of creepy."):
        '...Mi vengono i brividi.',
    (19015, "...I wouldn't mind doing more of the same."):
        "...Non mi dispiacerebbe ancora un po'.",
    (19022, 'Hyahahahaaa!! Ahyaaaaa!?'):
        'Aaah, ahahahaha! Ahi, ahiahiahiaaah!!',
    (19025, 'Whe! hiii! Haaa...!'):
        'Ih! Iiih! Ihihih, iiiih!!',
    (19028, 'Ahahahaaa! Ooh..! A..Ahyaaaa!!'):
        'Ahahaha, ah!? Ah, aaah!! A... ahahahah...!!!',

    # ---- le reazioni ai gesti, evochat == 2 ----
    # ⚠️ deroga: l'inglese qui e' un segnaposto ripetuto, il giapponese no
    (19049, ' seems to be a little pounding.'):
        'name(tc) + " si abbandona all\'abbraccio..."',
    (19053, '  staring at you with a happy expression.'):
        'name(tc) + " ride: \\"Quanta voglia di coccole!\\""',
    (19056, ' seems to be a little pounding.'):
        'name(tc) + " ha il cuore che batte forte..."',
    (19076, ' seems to be a little relaxed.'):
        'name(tc) + " sembra rilassarsi."',
    (19080, '  staring at you with a happy expression.'):
        'name(tc) + " ridacchia: \\"Eh eh...\\""',
    (19083, ' gently strokes you.'):
        'name(tc) + " ti restituisce la carezza."',
    (19103, '  staring at you with a happy expression.'):
        'name(tc) + " è in estasi..."',
    (19107, '  staring at you with a happy expression.'):
        'name(tc) + " sorride: \\"Non c\'è bisogno di tanta foga...\\""',
    (19110, '  staring at you with a happy expression.'):
        'name(tc) + " ti guarda: \\"Ti basta un bacio?\\""',
    (19130, '  taken aback.'):
        'name(tc) + " resta di sasso."',
    (19135, '???'): '???',
    (19138, 'What!?'): 'Cosa!?',
    (19158, '  staring at you with a happy expression.'):
        'name(tc) + " ti guarda con aria birichina."',
    (19162, '  staring at you with a happy expression.'):
        'name(tc) + " ti ferma: \\"Un attimo, calma!\\""',
    (19165, '  staring at you with a happy expression.'):
        'name(tc) + " sospira: \\"E dai...\\""',

    # ---- la scena, evochat == 3 ----
    (19181, ' begin to take  clothes off.'):
        'name(tc) + " comincia a spogliarsi."',
    (19184, 'You calmed yourself.'):
        'Riprendi fiato.',
    (19189, ' begin to take your clothes off.'):
        'name(tc) + " comincia a spogliarti."',
    (19208, 'You are awesome!'): 'Che meraviglia!',
    (19208, 'Oh my god....'): 'È... è troppo!',
    (19208, 'Okay, okay, you win!'): 'N-non ce la faccio più...',
    # ⚠️ due firme diverse con lo stesso inglese «Holy...!»: la chiave (riga, en)
    # non le distingue, e il giapponese si'. Vedi PER_FIRMA.
    (19223, 'Yes!'): 'Sì!',
    (19223, 'Ohhh'): 'Ahhh',
    (19223, '*gasp*'): '*sussulto*',
    (19223, '*rumble*'): '*fremito*',
    (19223, 'Come on!'): 'Su, dai!',

    # ---- il menu dello SCASSO DEL CUORE (evochat == -1) ----
    # ⚠️ le dice il GIOCATORE: niente participi, il suo genere non si sa
    (19250, "[% Unlock] Let's fight together as allies."):
        '"[Scasso " + ulp1 + "%] Combattiamo insieme, da compagni d\'arme."',
    (19251, "[% Unlock] Let's just be friends."):
        '"[Scasso " + ulp1 + "%] Diventiamo amici."',
    (19252, '[% Unlock] I want to compete with you.'):
        '"[Scasso " + ulp1 + "%] Voglio misurarmi con te."',
    (19253, "[% Unlock] I'm in love with you."):
        '"[Scasso " + ulp2 + "%] Ho perso la testa per te."',
    (19254, '[% Unlock] I want you to teach me various things.'):
        '"[Scasso " + ulp2 + "%] Voglio imparare da te."',
    (19255, '[% Unlock] I want to teach you various things.'):
        '"[Scasso " + ulp3 + "%] Voglio guidarti io."',
    (19256, '[% Unlock] I think of you as an important family member.'):
        '"[Scasso " + ulp3 + "%] Per me sei famiglia."',
    (19257, '[% Unlock] I want to form a contract with you.'):
        '"[Scasso " + ulpb1 + "%] Voglio un contratto con te."',
    (19258, '[% Unlock] You are my pet!'):
        '"[Scasso " + ulpb2 + "%] Tu mi appartieni!"',
    (19259, '[% Unlock] I want you to pledge allegiance to me.'):
        '"[Scasso " + ulpb3 + "%] Voglio che mi giuri fedeltà."',
    (19261, '[% Unlock] <I want to be your help...>'):
        '"[Scasso " + ulpb2 + "%] <Voglio esserti d\'aiuto>"',
    (19264, '[% Unlock] <Show me your real self...>'):
        '"[Scasso " + ulpb3 + "%] <Mostrami come sei davvero>"',
    (19267, '<Return>'): '<Indietro>',

    # ---- il menu dell'evochat (evochat == 1) ----
    (19271, '<Be kind>'): '<Trattare con dolcezza>',
    (19272, '<To embarrass>'): '<Mettere in imbarazzo>',
    # ⚠️ tetto 24 a due colonne: «monete d'oro» non ci sta, e l'inglese si'
    (19274, '<Pass 100,000gold>'): '<Dare 100.000 oro>',
    # 152/153 del menu principale dicono gia' «divertirci»
    (19276, "<<Interest in a little tail t'night>>"): '<<Divertirci in modo speciale>>',
    (19278, '<Heart unlock>'): '<Scasso del cuore>',
    (19281, '<Let them Evochat>'): '<Evochat fra loro due>',
    (19284, '<<Get excited>>'): '<<Perdere il controllo>>',
    (19287, '<End evochat>'): "<Chiudere l'evochat>",

    # ---- il menu dell'evochat oscuro (evochat == 11) ----
    (19291, '<Whipping>'): '<Frustare>',
    (19292, '<Stick a candy in>'): '<Caramella in bocca>',
    (19293, '<Give lots of love>'): '<Coccolare a lungo>',
    (19294, '<<Violence>>(Unimplemented)'): '<<Violenza>> (non implementato)',
    (19295, '<Dark tickling recording>'): '<Solletico oscuro con riprese>',
    (19297, '<<Torture anyway>>(Unimplemented)'): '<<Torturare comunque>> (non implementato)',
    (19300, '<End evochat>'): "<Chiudere l'evochat>",

    # ---- il menu dei gesti (evochat == 2) ----
    (19306, '(Various things)'): "(Un po' di tutto)",
    (19308, '<<Hug>>'): '<<Abbracciare>>',
    (19309, '<<Pat>>'): '<<Accarezzare>>',
    (19310, '<<Kiss>>'): '<<Baciare>>',
    (19311, '<<>>'): '"<<" + iroiro + ">>"',
    (19313, '<Return>'): '<Riprendersi>',

    # ---- il menu della scena (evochat == 3) ----
    (19316, '<Gently>'): '<Con dolcezza>',
    (19317, '<Violently>'): '<Con foga>',
    (19318, '<Small break>'): '<Pausa>',

    # ---- le dieci VIE, con le parole delle scale di text.hsp ----
    (21562, "You've entered the Comrade route!"):
        'Il rapporto prende la via del Compagno!',
    (21579, "You've entered the Friend route!"):
        "Il rapporto prende la via dell'Amico!",
    (21596, "You've entered the Rival route!"):
        'Il rapporto prende la via del Rivale!',
    (21613, "You've entered the Affection route!"):
        "Il rapporto prende la via dell'Innamoramento!",
    (21630, "You've entered the Student route!"):
        'Il rapporto prende la via della Tutela!',
    (21647, "You've entered the Master route!"):
        "Il rapporto prende la via dell'Insegnamento!",
    (21664, "You've entered the Family route!"):
        'Il rapporto prende la via della Famiglia!',
    (21681, "You've entered the Contract route!"):
        'Il rapporto prende la via del Contratto!',
    (21698, "You've entered the Owner route!"):
        "Il rapporto prende la via dell'Appartenenza!",
    (21715, "You've entered the Loyalty route!"):
        'Il rapporto prende la via della Lealtà!',

    # ---- i due esiti dello scasso, con le parole di command.hsp:2502 e :2507 ----
    # ⚠️ name(cc) e' il giocatore: il soggetto giusto e' tc, e lo dice il giapponese
    (21732, ' got rid of troubles and felt lighter.'):
        'name(tc) + " si libera dei crucci e ha il cuore più leggero."',
    (21750, ' has awakened to a dangerous hobby...'):
        'name(tc) + " ha scoperto un passatempo pericoloso..."',

    # ---- il potere di scasso ----
    (21964, 'Your unlock power is .'):
        '"Il vostro potere di scasso è " + ulp + "."',
}

# le voci che (riga, en) non distingue: chiave la FIRMA
PER_FIRMA = {
    # 19208 「こ、心地よかったよ」 e 「さ、最高だ」, tutt'e due «Holy...!» in inglese
    'ce2b0e70': 'C-che sensazione...',
    '4ed72ab6': 'È... è il massimo!',
}


def main() -> int:
    # ⚠️ il lotto si ricostruisce dall'ESTRAZIONE e dalle chiavi di RESE, non da
    # «quel che il dizionario non ha ancora»: dopo la prima reimportazione quel
    # criterio svuota il lotto, e uno script di lotto che non si puo' rilanciare
    # non si puo' correggere. Le sette voci gia' rese della zona restano fuori
    # perche' semplicemente non hanno una chiave qui.
    voci = []
    for l in io.open(ESTRAZIONE, encoding='utf-8'):
        v = json.loads(l)
        if not any(a <= v['riga'] <= b for a, b in ZONE):
            continue
        if (v['riga'], v['en']) in RESE or v['firma'][:8] in PER_FIRMA:
            voci.append(v)

    errori = []
    viste = set()
    viste_f = set()
    for v in voci:
        corta = v['firma'][:8]
        if corta in PER_FIRMA:
            viste_f.add(corta)
            v['it'] = PER_FIRMA[corta]
            continue
        k = (v['riga'], v['en'])
        if k not in RESE:
            errori.append('%d: voce senza resa | %r' % (v['riga'], v['en'][:90]))
            continue
        viste.add(k)
        v['it'] = RESE[k]
    for k in sorted(set(RESE) - viste):
        errori.append('%d: resa senza voce nel lotto | %r' % (k[0], k[1][:90]))
    for k in sorted(set(PER_FIRMA) - viste_f):
        errori.append('%s: resa per firma senza voce nel lotto' % k)
    if errori:
        for e in errori:
            print(e)
        return 1

    with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%s: %d voci, %d firme' % (USCITA, len(voci), len({v['firma'] for v in voci})))
    return 0


if __name__ == '__main__':
    sys.exit(main())
