# -*- coding: utf-8 -*-
"""80a — `chat.hsp`, il sistema di LEOLD (`:16645`-`:18001`) intero.

Leold e' il fabbro-scienziato che vende **AP**: aggiunge slot d'equipaggiamento,
alza velocità e Vita, insegna talenti e tecniche, risveglia i compagni. Dentro
la stessa zona ci sta anche `*com_change_gamemode`, il pannello che cambia
modalità di bilanciamento (che Leold non c'entra: e' la donna dagli occhi
strani, ma il codice lo tiene li').

⭐ **Zona CHIUSA**, misurata prima di cominciare con `scratchpad/perimetro-zona.py`:
90 firme da fare, 110 occorrenze, **zero** con occorrenze fuori. Quindi
`bilingui` deve dare zero al primo giro, come gli evochat della 79a.

Le famiglie, in ordine di riga:

    16645-16907   gli ARTI: uno slot d'equipaggiamento nuovo, pagato in Vita
    16909-17232   il cambio di MODALITA' (Essential/Loss/Overdose/...)
    17233-17252   i tre rifiuti: già al massimo, AP insufficienti, bonus pieni
    17253-17539   l'ESITO comune: che cosa il compagno ha imparato o scordato
    17541-17797   il RISVEGLIO del giocatore: talenti e tecniche
    17798-18001   il RISVEGLIO del compagno: 13 poteri e 10 regolazioni

⭐⭐⭐ **IL LESSICO NON SI E' DECISO: STA TUTTO IN UN PANNELLO GIA' TRADOTTO.**
Ogni voce di questi menu vende un `CHARA_BIT_AWAKE_*` o un `SKILL_SPACT_*`, e
tutti e due hanno già un nome italiano stampato altrove. La strada e' il `grep`
sul nome della **variabile** (79a), non sulla stringa:

  * i **risvegli** — `command.hsp:2355`-`:2452`, il pannello dei talenti, venti
    righe `listn(0, listmax) = lang(...)` già rese: «Il fascino stordisce chi
    attacca in mischia», «L'orgoglio cresce col pericolo», «La forza nascosta
    cresce col pericolo», «La barriera annulla i danni», «Insulto appreso»,
    «Accumulo di mana appreso», «Salto dimensionale appreso», «Cura tattica
    appresa», «Attacco tattico appreso», «Arti marziali tattiche apprese»,
    «Maledizione tattica appresa», «Carica appresa», «Provocazione appresa»,
    «Tiro zero appreso», «Lancio tattico appreso», «Soffio variabile appreso»,
    «Tempesta variabile appresa», «Preferenza per la mischia / per il tiro /
    per le magie a freccia». I menu qui dicono **quei** nomi.
  * le **tecniche** — `skill.hsp`: «Attacchi continui» (`:1264`), «Provocazione»
    (`:1188`), «Guardia metallica» (`:1456`), «Sincronia delle anime» (`:1152`),
    «Carica» (`:1212`).
  * il **talento** e' «talento» (`command.hsp:2113`, `:2589`, `:2637`), non
    «fiata»; lo **skill bonus** e' «bonus di abilità» (`action.hsp:9321`);
    «INIT» sulla scheda e' «Iniz.» (`command.hsp:10504`); la statistica e' «Vita».
  * «Hai imparato una nuova capacità: X.» era già reso in tre file per altre
    `SKILL_SPACT_*` (`chara.hsp:16`, `map.hsp:9853`, `chat.hsp:17222`): le
    cinque di qui hanno firma diversa solo perche' cambia la costante.

⚠️⚠️⚠️ **L'INGLESE DI MONTE SBAGLIA UN PREZZO, E IL GIUDICE E' IL CODICE** (79a).
`:17864` etichetta 可変放射 «Variable Breath (**300**AP)», ma il giapponese dice
消費AP**400** e `:17925` fa `leoap = 400`. Chi legge l'inglese mette da parte 300
AP e si sente rispondere che non bastano. La resa dice **400**. Controllati tutti
e ventisei i prezzi dei due menu: e' l'unico che diverge.

⚠️⚠️ **E l'inglese sbaglia anche DUE NOMI DI PARTE DEL CORPO, sempre contro se
stesso.** `:16741` offre «Chest» e `:16743` «Finger», ma gli slot che concede
sono `EQUIP_SLOT_BODY` e `EQUIP_SLOT_RING`, e `bodyn()` (`text.hsp:136`) li
chiama «Body» e «Ring»: il menu inglese nomina una cosa che il messaggio di
conferma chiama in un altro modo. Il giapponese e' coerente (胴体/胴体, 指/指).
⚠️ **Non e' materia di questo lotto** — quelle nove voci sono già tradotte da
una sessione vecchia, e in italiano dicono «Torso», «Dito», «Braccio»,
«Schiena», «Fianchi» mentre `bodyn()` dice «Torso», «Anello», «Arto», «Dorso»,
«Vita». Quattro su nove non combaciano. Va in `decisioni.md`: la correzione
ovvia («il menu dica le parole di `bodyn()`», 76a) inciampa su «Vita», che nella
stessa riga e' già il nome della statistica — «Vita (Vita -12)».

⚠️⚠️ **IL MENU DEI TREDICI POTERI HA IL TETTO DURO A 24** (`chat.hsp:25166`:
sopra le dieci voci due colonne e `strmid(..., 0, 24)`). Lo stile del progetto
per i costi e' «(100 AP)» (`:17704`-`:17716`, già in build), ma li' non ci sta:
«Accumulo di mana (600 AP)» fa 25. Nel solo menu a tredici il costo si stringe a
«AP600». ⭐ E' la regola della 73a: *due schermate che mostrano la stessa scelta
devono dire le stesse PAROLE, non sono tenute a dirle con la stessa LUNGHEZZA*
— i nomi restano identici, cambia la notazione del prezzo. Una sola voce non
entra lo stesso, «Maledizione tattica AP500» (25): si accorcia il qualificatore
condiviso, non il nome (72a).

⚠️ **Il divieto di genere morde in cinque punti**: la donna del pannello dice
«benvenuto» (vocativo, 77a) e «sei caduto» (participio, 75a); il compagno «si e'
risvegliato»; il giocatore «non poter più essere te stesso» e «Attento!». Le
vie d'uscita usate: presente al posto del passato prossimo, accordo su una parola
nostra («la stessa persona»), imperativo, e la relativa senza nome.

⚠️ `:16679` e `:16904` passano da `cnvtalk`: le virgolette le mette il codice
(74a), la resa non le porta. `:16788` invece le ha scritte a mano nell'inglese e
le tiene; li' `he(r1)` e' morfologia a un argomento e si toglie (75a), e quel
che resta e' un impersonale — che e' anche quel che dice il giapponese.
"""
import io
import json
import sys

ZONE = [(16645, 18001)]
ESTRAZIONE = 'scratchpad/_80-chat-tutte.jsonl'
USCITA = 'lavoro/fase4-chat-leold.jsonl'

RESE = {
    # ================= gli ARTI (*chat_unique_leold_limb) =================
    (16648, "A new equipment slot, is it? Ah, I just might be able to do it! Let's see. If I apply my previous biological hard point theory... Originally it was meant to strengthen a body part or add an additional part via an attachment similar to the power arm, but it had to be canceled for various reasons. We can use your own cells for the part, and then integrate it into your nervous system. Theoretically, we... Oops, sorry about that. I didn't mean to ramble on."):
        "Uno slot d'equipaggiamento nuovo, eh? Ah, forse ci riesco! Vediamo. Se applico la mia vecchia teoria dei punti d'aggancio biologici... All'inizio doveva rinforzare una parte del corpo, o aggiungerne una con un innesto come il braccio meccanico, ma fu sospesa per vari motivi. Prendiamo le cellule dal corpo e ci cresciamo sopra la parte nuova, poi la colleghiamo ai nervi. In teoria noi... Ops, scusa. Non volevo dilungarmi.",

    # menu a 3 voci, una colonna: nessun taglio a 24
    (16650, "Let's not."): 'Lascio perdere.',
    (16651, 'Try it on me.'): 'Lo provo io.',
    (16652, 'Try it on my companion.'): 'Lo prova un compagno.',
    (16653, 'So... Who is giving it a try?'): 'Allora... chi ci prova?',

    # ⚠️ cnvtalk: le virgolette le mette il codice, la resa NON le porta
    (16679, "There's nowhere else to attach any limbs."):
        "Non c'è più un posto dove attaccare niente.",

    (16747, 'The toll on your life will differ depending on the body part... so please choose wisely. We will start right away once you decide!'):
        'Il carico sulla Vita cambia a seconda della parte... pensaci bene. Appena scegli, si comincia!',

    # ⚠️ dinamica: le virgolette sono scritte a mano nell'inglese e restano;
    # he(r1) e' morfologia a un argomento e si toglie, e quel che resta e' un
    # impersonale — che e' anche quel che dice il giapponese
    (16788, '\\" can\'t endure another procedure! Stop, stop!\\"'):
        '"\\"Con una Vita così non si regge! Basta, si annulla!\\""',

    # ⚠️ cnvtalk: niente virgolette nella resa
    (16904, 'All done. There should be no chance of rejection.'):
        "Fatto. Non ci saranno problemi di rigetto.",

    # ================= il cambio di MODALITA' =================
    (16928, 'Balance Change(one-way) '): 'Cambio modalità (senza ritorno) ',
    (16932, 'You can see another universe in the back of her eyes...'):
        'In fondo alle sue pupille, che sembrano risucchiarti, si vede un altro universo...',
    # listn(0, 6): colonna larga 101 px (da wx+64 a wx+165), tetto 14 caratteri
    (16940, '*Cancel*'): '*Annulla*',
    (16967, 'Not selectable'): 'Non selezionabile',

    # ⚠️ «te stesso» porta il genere: l'accordo si sposta su «persona» (75a)
    (17110, 'You trembled with feeling you could not stay by yourself.'):
        'Senti di non essere più la stessa persona, e un brivido ti attraversa.',
    (17113, 'You distract your eyes...'): 'Distogli piano lo sguardo...',

    # ⚠️ «Benvenuto» e' un vocativo e si accorda (77a): la via d'uscita e' la
    # relativa senza nome
    (17204, 'Ahahahahaha! You really chose it... Welcome to the new universe.'):
        "Ahahahahah! L'hai scelto davvero... Che il nuovo universo ti accolga.",
    (17206, "But why stop here? You already chose to take the easy path, after all... Ufufu, will you fall even further? I think you will. I'm looking forward to seeing you again..."):
        "Ti faccio una profezia. Hai scelto la via comoda... e nemmeno questa ti basterà a lungo. Uh uh uh, da qui si scende ancora, sai? Non vedo l'ora di rivederti...",
    # ⚠️ «sei caduto» accorda: si passa all'ausiliare avere (75a)
    (17209, "Fufufu... You fell to the very limit... But someday, surely even this won't be enough for you. Until then, enjoy yourself to your heart's content..."):
        "Uh uh uh... Hai proprio toccato il fondo... Ma un giorno, di sicuro, nemmeno questo ti basterà. Fino ad allora il tempo è poco... abbandonati pure al piacere.",

    # ================= i tre rifiuti =================
    (17235, "Sorry, but I don't think I can train you any further right now."):
        'Scusa. Per come sono adesso, oltre di qui non riesco ad allenare.',
    (17240, "...I can't do that unless you save up more AP. You'll need to defeat enemies with high INI, regardless of their level, to gain AP."):
        "...Così non se ne fa niente: devi mettere da parte più AP. Gli AP arrivano battendo nemici con l'Iniz. molto sopra la tua, il livello non conta.",
    (17248, 'If there are 100 or more skill bonuses, I cannot give new. No matter how much skill bonus you accumulate, growth will be delayed if you do not use it.'):
        "Con cento o più bonus di abilità da parte non te ne posso dare altri. E accumularli senza spenderli non fa che rallentare la crescita.",

    # ================= l'ESITO comune (*chat_unique_leold_done) =================
    (17320, 'All done!'): 'Ecco fatto!',
    # ⚠️ cdatan(CDATAN_NAME, c) e' NUDO (niente articolo): il nome resta in testa
    # e nessuna preposizione gli va davanti (77a)
    (17407, ' forgot how to use that power.'):
        'cdatan(CDATAN_NAME, c) + " ha dimenticato come si usa quel potere."',
    (17413, "All done! Trying to learn the same thing again will make you forget it. Forgetting it won't cost AP, and will also refund the AP spent on it in the first place."):
        "Ecco fatto! Occhio però: se glielo fai imparare una seconda volta, se lo dimentica. Dimenticare non costa AP, e quelli spesi prima tornano indietro.",
    # ⚠️ «si e' risvegliato» accorda col compagno: presente
    (17417, ' awakened to a new power.'):
        'cdatan(CDATAN_NAME, c) + " si risveglia a un nuovo potere."',
    (17433, "'s preferred distance became ."):
        'cdatan(CDATAN_NAME, c) + " ha ora una distanza ideale di " + cdata(CDATA_AI_DISTANCE, c) + "."',
    (17447, "'s movement probability became ."):
        'cdatan(CDATAN_NAME, c) + " ha ora una probabilità di movimento di " + cdata(CDATA_AI_MOVE_FREQ, c) + "."',
    (17459, ' is now allowed to use spells.'):
        'cdatan(CDATAN_NAME, c) + " può di nuovo usare le magie."',
    (17463, ' is now forbidden from using spells.'):
        'cdatan(CDATAN_NAME, c) + " non può più usare le magie."',
    (17469, ' is now allowed to use special abilities.'):
        'cdatan(CDATAN_NAME, c) + " può di nuovo usare le tecniche."',
    (17473, ' is now forbidden from using special actions.'):
        'cdatan(CDATAN_NAME, c) + " non può più usare le tecniche."',
    (17483, "'s character quality was increased!"):
        'cdatan(CDATAN_NAME, c) + " sale di qualità!"',
    (17502, "Looks like you already have that feat. I'll return the AP to you."):
        "Quel talento ce l'hai già, a quanto pare. Ti restituisco gli AP.",
    (17522, "Looks like there's no more room for new feats. You'll have to select an existing one to turn it back into AP to make room for another."):
        "...Non c'è più spazio per altri talenti. Devi sceglierne uno che hai già e riconvertirlo in AP, così liberi un posto.",
    (17531, 'All done! It should be on your list of feats now.'):
        "Ecco fatto! Adesso lo trovi nell'elenco dei talenti.",
    (17532, ' acquired a new feat.'):
        'cdatan(CDATAN_NAME, c) + " ha preso un talento nuovo."',

    # ================= il RISVEGLIO del giocatore =================
    # menu a 5 voci, una colonna: tetto 58
    (17554, 'Increase speed by 30.(cost AP)'): '"Velocità +30 (" + spcost + " AP)"',
    (17555, 'Increase life by 10. (cost AP)'): '"Vita +10 (" + hpcost + " AP)"',
    (17556, 'Acquire feats.'): 'Prendere un talento',
    (17557, 'Learn special abilities.'): 'Imparare una tecnica',
    (17558, 'Gain 100 bonus points. (1500AP)'): "Cento bonus di abilità (1500 AP)",
    (17559, 'You have...  Awakening Points left. How do you want to use them?'):
        '"I punti che servono al risveglio... di AP te ne restano " + cdata(CDATA_AP_CURRENT, c) + ". Come li usi?"',

    # i quattro TALENTI: i nomi vengono dal pannello di command.hsp:2355-2372
    (17638, 'Charm (1500AP) [Dim enemies attacking at close range]'):
        'Fascino (1500 AP) [stordisce chi attacca in mischia]',
    (17639, 'Brave (1500AP) [Increase damage dealt as HP decreases]'):
        'Forza nascosta (1500 AP) [più danni a HP bassi]',
    (17640, 'Obstinate (1800AP) [Increase evasion, damage mitigation as HP decreases]'):
        'Orgoglio (1800 AP) [più schivata e riduzione a HP bassi]',
    (17641, 'Barrier (2000AP) [Negate attacks with equal amount of MP]'):
        'Barriera (2000 AP) [consuma MP pari al danno]',
    (17642, "Which feat would you like? If it's something you already know, the AP will be returned to you."):
        "Quale talento vuoi? Se ne scegli uno che hai già, lo togli e gli AP tornano indietro.",
    (17695, ' obtained a new power.'):
        'cdatan(CDATAN_NAME, c) + " ottiene un potere nuovo."',
    (17718, 'Which special action do you want to learn? Pick carefully, because once learned the AP cannot be refunded.'):
        "Quale tecnica vuoi imparare? Scegli bene: una volta imparata, gli AP non tornano più indietro.",
    (17747, "All done! You'll have to try it out for yourself to see how it works."):
        "Ecco fatto! Adesso provala sul serio, che si vede meglio l'effetto.",

    # le cinque capacità: la cornice era già resa in chara.hsp:16, map.hsp:9853
    # e chat.hsp:17222; qui cambia solo la costante, quindi cambia la firma
    (17754, 'You have learned a new ability, .'):
        '"Hai imparato una nuova capacità: " + skillname(SKILL_SPACT_CONTINUOUS_ATTACKS) + "."',
    (17763, 'You have learned a new ability, .'):
        '"Hai imparato una nuova capacità: " + skillname(SKILL_SPACT_PROVOKE) + "."',
    (17772, 'You have learned a new ability, .'):
        '"Hai imparato una nuova capacità: " + skillname(SKILL_SPACT_METAL_GUARD) + "."',
    (17781, 'You have learned a new ability, .'):
        '"Hai imparato una nuova capacità: " + skillname(SKILL_SPACT_SYNCHRO_HEARTS) + "."',
    (17790, 'You have learned a new ability, .'):
        '"Hai imparato una nuova capacità: " + skillname(SKILL_SPACT_CHARGE) + "."',

    # ================= il RISVEGLIO del compagno =================
    # menu a 6 voci, una colonna
    (17799, 'Increase speed.'): 'Alzare la velocità',
    (17800, 'Increase life.'): 'Alzare la Vita',
    (17802, 'Learn spells and special abilities.'): 'Imparare magie e tecniche',
    (17803, 'Change battle style/increase character quality.'):
        'Stile di combattimento e qualità',
    (17804, 'Convert AP into bonus points.'): "Prendere bonus di abilità",
    (17805, 'What form do you want your powers to take?'):
        'In che potere lo trasformo?',

    (17808, "Alright, I can raise an ally's life by 10 by consuming AP depending on initial life and bit. Who's it gonna be?"):
        "Bene. Consumo AP secondo la Vita e il Mana iniziali e le doti, e alzo la Vita di 10. A chi la alzo?",
    (17813, "100 bonus points will cost 500AP. Who's it gonna be?"):
        "Cento bonus di abilità costano 500 AP. Su chi lo faccio?",
    (17819, "Alright, I can raise an ally's speed by 30 by consuming AP depending on initial speed. Who's it gonna be?"):
        'Bene. Consumo AP secondo la velocità iniziale e alzo la velocità di 30. A chi la alzo?',
    (17828, 'Which feat do you want?'): 'Quale talento vuoi dargli?',

    # ⚠️⚠️ i TREDICI poteri: due colonne, taglio duro a 24 (chat.hsp:25166).
    # I nomi sono quelli di command.hsp:2377-2437; il costo si stringe ad «APn»
    # perche' «(100 AP)» non ci sta. Prezzi verificati su leoap, :17868-:17931.
    (17853, 'Insult (100AP)'): 'Insulto AP100',
    (17854, 'Crystal Spear (600AP)'): 'Accumulo di mana AP600',
    (17855, 'Dimensional Move (100AP)'): 'Salto dimensionale AP100',
    (17856, 'Provoke (200AP)'): 'Provocazione AP200',
    (17857, 'Charge (1000AP)'): 'Carica AP1000',
    (17858, 'Tactical Martial Arts (600AP)'): 'Arti marziali tattiche AP600',
    (17859, 'Tactical Attack (400AP)'): 'Attacco tattico AP400',
    (17860, 'Tactical Heal (500AP)'): 'Cura tattica AP500',
    # 25 caratteri per esteso: si accorcia il qualificatore condiviso, non il nome
    (17861, 'Tactical Curse (500AP)'): 'Maledizione tatt. AP500',
    (17862, 'Zero Shoot (500AP)'): 'Tiro zero AP500',
    (17863, 'Tactical Throw(500AP)'): 'Lancio tattico AP500',
    # ⚠️⚠️ l'inglese dice 300, il giapponese 400 e :17925 fa leoap = 400
    (17864, 'Variable Breath (300AP)'): 'Soffio variabile AP400',
    (17865, 'Variable Storm (800AP)'): 'Tempesta variabile AP800',
    (17866, 'Which spells and abilities do you want your ally to learn?'):
        'Quale magia o tecnica gli faccio imparare?',

    # menu a 10 voci: NON supera le dieci, quindi una colonna e tetto 58
    (17936, 'Increased frequency of melee attacks (30AP)'):
        'Preferenza per la mischia (30 AP)',
    (17937, 'Increased frequency of ranged attacks (30AP)'):
        'Preferenza per il tiro (30 AP)',
    (17938, 'Use dart spell instead of regular attack (200AP)'):
        'Preferenza per le magie a freccia (200 AP)',
    (17939, 'Preferred distance +1 (10AP)'): 'Distanza ideale +1 (10 AP)',
    (17940, 'Preferred distance -1 (10AP)'): 'Distanza ideale -1 (10 AP)',
    (17941, 'Movement probability +10% (5AP)'):
        "Probabilità di movimento +10% (5 AP)",
    (17942, 'Movement probability -10% (5AP)'):
        "Probabilità di movimento -10% (5 AP)",
    (17943, 'Allow/disallow spell usage (20AP)'):
        'Sigilla o libera le magie (20 AP)',
    (17944, 'Allow/disallow ability usage (20AP)'):
        'Sigilla o libera le tecniche (20 AP)',
    (17945, 'Increase character quality (1000AP)'):
        'Alza la qualità del personaggio (1000 AP)',
    # ⚠️ «Attento» accorda col giocatore: si gira in «Occhio» (75a)
    (17946, 'How do you want them to change? Careful now, AP spent on these will never get refunded even if you pick the same option again.'):
        "Che cosa gli cambio? Occhio: gli AP spesi qui non tornano mai indietro, nemmeno riscegliendo la stessa voce.",
}


def main() -> int:
    voci = []
    for l in io.open(ESTRAZIONE, encoding='utf-8'):
        v = json.loads(l)
        if not any(a <= v['riga'] <= b for a, b in ZONE):
            continue
        if (v['riga'], v['en']) in RESE:
            voci.append(v)

    errori = []
    viste = set()
    for v in voci:
        k = (v['riga'], v['en'])
        viste.add(k)
        v['it'] = RESE[k]
    for k in sorted(set(RESE) - viste):
        errori.append('%d: resa senza voce nel lotto | %r' % (k[0], k[1][:90]))
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
