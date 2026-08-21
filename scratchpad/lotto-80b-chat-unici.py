# -*- coding: utf-8 -*-
"""80a — `chat.hsp`, i PNG unici che chiudono la zona (`:16641`-`:16644`,
`:18002`-`:18601`).

Quel che restava dopo il lotto di Leold: il selettore delle pose, la madre
malata, e le tre scene di trama del finale — Enthumesis, Lankata, Jaldabaoth.
34 firme, 37 occorrenze, e la zona si chiude.

⚠️ **L'unica firma «sparsa» non lo era davvero.** `perimetro-zona.py` segnalava
`:18236` con un'occorrenza anche a `:15967`, fuori zona. Guardate, le due sono
lo **stesso codice duplicato**: stesso `map(...) = xy2pic(3, 8)`, stesso
`SOUNDLIST_ATK_FIRE`, stesso `DAMAGE_FROM_JALDABAOTH_SHIELDED`. E' la scena del
fuoco di Jaldabaoth scritta due volte. Tradurla vale in tutt'e due i siti.

⭐⭐ **QUI IL GENERE SI SA, E QUINDI SI USA.** E' l'altra faccia del divieto
(63a): non ci si accorda con un genere che non si conosce, ma questi personaggi
il codice li nomina per `CREATURE_ID`, quindi basta andarlo a leggere.

| chi | `db_creature.hsp` | come parla |
|---|---|---|
| Lankata | «<Lankata> il fulmine del cielo azzurro», donna | dice gia' «**Padre**, vi chiedo perdono...»: col padre e' il **voi** |
| Alfred | «<Alfred> il vento azzurro di Lothria», uomo | ex comandante dei cavalieri, forma di cortesia |
| Enthumesis | «<Enthumesis>» | dice gia' «**Pa... dre...**» e «Tante cose entrano dentro di me...» |
| Leold | «<Leold> il braccio nero» | brusco: «Mi prudono le mani.», «Andarci piano non fa per me.» |
| Jaldabaoth | «<Jaldabaoth> il Figlio del Caos» | sprezzante |
| Yayauhqui | «<Yayauhqui Tezcatlipoca>» | dio della guerra, tono solenne |

⭐ **E l'inglese aveva ragione dove il giapponese taceva.** `:18083` in
giapponese non nomina nessuno (「一度でいいから会いたいよ…」), l'inglese ci mette
«Father...». Non e' un'aggiunta arbitraria: Enthumesis dice «Pa... dre...» nella
sua riga di `db_creature.hsp`, gia' resa. Il personaggio conferma la scelta di
monte.

⚠️⚠️ **DEROGA DICHIARATA a `:18157`: l'inglese ha sbagliato la persona.** Il
giapponese e' 「ランカータ、なぜ貴方がここに？衛生兵なのに一人でここまで来たのですか？」 —
Alfred parla **a** sua figlia e le da' del 貴方. L'inglese scrive «The medic came
here on their own?», in terza persona, e la frase smette di essere rivolta a
lei. Si segue il giapponese: la seconda persona e' quel che il codice mette in
scena (le due battute intorno sono un dialogo padre-figlia).

⚠️ **Il divieto di genere morde solo dove il bersaglio e' il GIOCATORE**, e qui
capita quattro volte: «Unknown **adventurer**» e «You're in my way **Adventurer**»
sono vocativi (77a) e diventano il «voi» di cortesia che Lankata usa comunque;
«**Liar!**» detto dalla bambina diventa «Bugie!»; «Look out!» diventa
«Attenzione!» e non «Attento!». ⚠️ Invece «mi avete **salvata**» e «sono **salvo**»
restano accordati: sono Lankata e Alfred, e il loro sesso sta scritto.

⚠️ `:18064` e `:18076` nominano un OGGETTO, quindi dicono il nome che il
giocatore ha nello zaino (74a): `db_item.hsp:147525`-`:147527` compone «una
**pozione di cura della corruzione**», non «potion of cure corruption».

⚠️ `:16642` e' una dinamica il cui inglese e' tutto morfologia — `he(tc)` a un
argomento — e togliendolo non resta nessun soggetto. La via e' l'impersonale,
che e' anche quel che dice il giapponese (「あなたの言葉を聞いていない」). E siccome
resta una dinamica, la resa e' un'**espressione** e vuole le virgolette (69a).
"""
import io
import json
import sys

ZONE = [(16641, 16644), (18002, 18601)]
ESTRAZIONE = 'scratchpad/_80-chat-tutte.jsonl'
USCITA = 'lavoro/fase4-chat-unici.jsonl'

RESE = {
    # ---- *chat_unique_SWEND1: chi non ti ascolta piu' ----
    (16642, '( ignores you...)'): '"(...non ti sta ascoltando)"',

    # ---- *evochat_portrait: il selettore delle pose ----
    (18004, '(Currently using face)'):
        '"(Posa attuale: face" + cdata(CDATA_FACE, tc) + ")"',
    (18007, '(Current: No Tachi-e)'): 'Al momento non hai scelto nessuna posa.',
    # menu a 3 voci: le voci concordano con «posa», che e' parola nostra
    (18009, '>>>'): 'Successiva >>>',
    (18010, '<<<'): '<<< Precedente',
    (18011, 'Cancel'): 'Annulla',

    # ---- *sqMother_1: la bambina e la madre malata ----
    # il nome dell'oggetto e' quello dello zaino (db_item.hsp:147525)
    (18064, '(Hand her a potion of cure corruption.)'):
        '(Darle una pozione di cura della corruzione)',
    # ⚠️ «Bugiardo!» accorderebbe col giocatore
    (18072, 'Liar!'): 'Bugie!',
    (18076, 'You give her a potion.'):
        'Le dai una pozione di cura della corruzione.',
    (18078, 'R-Really? Mommy, mommy!  gave us a cure! Are you gonna be okay now?'):
        '"D-davvero? Mamma, mamma! " + cdatan(CDATAN_NAME, CHARA_PLAYER) + " ci ha portato la medicina! Adesso guarisci, vero?"',

    # ---- *chat_unique_enthumesis ----
    (18082, 'Sophia told me about the condition of this thing that she predicted based on reading its cumulative emissions... but it seems to be much weaker than that.'):
        "Sophia mi aveva detto in che stato doveva essere, contando quanto ha emesso finora... ma sembra molto più debole di così.",
    (18083, "Father... How I long to see him, even if it's only once... What is it I must do to see him? If I absorb the knowledge of these people, will I find out?"):
        'Padre... Vorrei vederlo, anche una volta sola... Che cosa devo fare per vederlo? Se prendo dentro di me il sapere di questa gente, lo capirò?',
    (18084, "Don't make the mistake of showing mercy. Let's finish this."):
        'Avere pietà adesso è pericoloso. Finiamola qui.',

    # ---- *chat_unique_lankata: la figlia, il padre e il reattore ----
    (18138, 'Finally we meet, father!'): 'Finalmente vi ho trovato...! Padre!',
    (18139, "Heh... I'm dying but I can hear my daughter's voice somehow. Oh, my vision... is already... getting... blurry."):
        'Eh eh... in punto di morte... sentire la voce di mia figlia... Ormai gli occhi... si stanno... annebbiando.',
    # ⚠️ vocativo: «Avventuriero» accorderebbe col giocatore. Lankata da' del voi
    (18140, "You're in my way Adventurer, make way please."):
        'Voi che cercate avventura, fatemi largo un momento.',
    (18141, "The new pain killer has been administered. However, I wonder if it's effective..."):
        'Somministrato il nuovo analgesico... speriamo che faccia effetto.',
    (18143, "In this state the body will break down before the medicine manages to take effect... For now let's remove the dimensional reactor. Please endure, father!"):
        'Di questo passo il corpo cede prima che il farmaco giri tutto... Estraggo subito il reattore dimensionale, qui e ora. Resistete, Padre!',
    # ⚠️ Alfred e' uomo e il codice lo dice: «salvo» si accorda, ed e' giusto
    (18155, "I-I'm saved?"): 'Io... sono salvo?',
    (18156, "Oh, I'm so glad, father!"):
        'Padre...! Che sollievo, che sollievo davvero...',
    # ⚠️⚠️ DEROGA: l'inglese passa alla terza persona, il giapponese da' del voi
    # a Lankata ed e' un dialogo padre-figlia. Si segue il giapponese.
    (18157, 'Why are you here Lankata? The medic came here on their own?'):
        "Lankata, perché siete qui? Siete un'infermiera da campo: siete venuta fin quassù da sola?",
    (18158, "We'll talk about that later. Let's escape first."):
        'Ne parliamo dopo. Su, andiamo via di qui.',
    (18159, "Uh-oh, we can't go that way."): 'Ah, no. Di lì non si passa. Un momento.',
    # ⚠️ «mi avete salvata» accorda con Lankata, che e' donna: si puo'
    (18160, "Unknown adventurer... if it hadn't been for you, I probably wouldn't have made it. You may be thinking that you've just brushed off a few embers, but in the end, you've saved the day. I thank you."):
        'Voi di cui non so il nome... se non aveste ripulito la strada, non sarei arrivata in tempo. Per voi sarà stato solo scacciare qualche favilla, ma alla fine mi avete salvata. Vi ringrazio.',
    (18162, ' opens a dimensional door.'):
        'name(tc) + " apre una porta dimensionale."',

    # ---- *chat_unique_jaldabaoth: il fuoco ----
    (18169, 'I tire of this.'): 'Che noia.',
    (18171, 'The air in the room suddenly became tense, and a fireball of blazing heat appeared.'):
        "L'aria della stanza si fa di colpo tesa, e compare una sfera di fuoco incandescente.",
    # ⚠️ «Attento!» accorderebbe col giocatore
    (18174, 'What the...!? Look out! !'):
        '"Ma...!? Attenzione! " + cdatan(CDATAN_NAME, CHARA_PLAYER) + "!"',
    (18177, 'I am finished with your games... All of you shall turn to ash.'):
        'Il gioco è finito... diventerete cenere.',
    (18182, 'A horrific wave of fire envelops the area!'):
        "Un'ondata di fuoco spaventosa avvolge ogni cosa!",
    (18184, 'You try your hardest to suppress the shaking in your legs, but it proves difficult...'):
        'Cerchi con tutte le forze di frenare il tremito delle gambe, ma è dura...',
    # name() si porta l'articolo dentro: nessuna preposizione davanti (72a)
    (18236, ' shielded you and turned to ashes.'):
        'name(cnt) + " ti fa scudo e diventa cenere."',
    (18279, '...After what felt like an eternity, you stagger to your feet, with half of your body turned into ash...'):
        '...Chissà quanto tempo è passato. Ti rialzi barcollando, col corpo per metà ridotto in cenere...',
    (18467, "You can hear someone's voice..."): 'Si sente una voce...',
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
