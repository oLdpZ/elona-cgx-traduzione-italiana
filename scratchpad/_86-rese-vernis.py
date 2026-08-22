# -*- coding: utf-8 -*-
"""Le rese di cinque blocchi chiusi di `*chat_unique` (chat.hsp :3316-:3463 e
:3794-:3970): 55 firme, nessuna con occorrenze fuori.

    :3316  RAPHAEL il donnaiolo — l'incarico della moglie             15
    :3423  AINC il cavaliere novizio — il capo degli yeek              7
    :3794  RENTON il mago tormentato — i libri di Rachel              12
    :3867  MARKS il ladro leggendario — l'invito della piramide        7
    :3905  NOEL la dinamitarda — la bomba atomica di Derphy           14

Registri:
  RAPHAEL  volgare e compiaciuto, da' del tu sbrigativo (お前さん)
  AINC     terrorizzato e cerimonioso: urla «Yeeek!» e poi si scusa (です/ます)
  RENTON   lento, dolente, parla della sorella morta; poi impazzisce
  MARKS    ladro elegante, cortese fino all'untuoso (です/ます, «ホホホッ»)
  NOEL     fredda e sensuale, il piacere della sofferenza altrui (あたし)

Lessico ereditato: «<Raphael> il donnaiolo», «<Ainc> il cavaliere novizio»,
«<Renton> il mago tormentato», «<Marks> il ladro leggendario», «<Noel> la
dinamitarda» (`db_card.hsp`, `db_creature.hsp`), «yeek» e «Derphy» e «Porto
Kapul» (glossario), «Lumiest» (`map.hsp:2734`), «Rachel» (`proc.hsp:6131`),
«bomba atomica» (`db_item.hsp:143543`), «Ehekatl» (`action.hsp:14108`, ed e'
femmina: «Mi hai chiamata?»).

⚠️ L'epiteto `cdatan(CDATAN_AKA, ...)` a :3880 non regge articolo: si usa
l'APPOSIZIONE, la regola della 84a.
"""

RESE = {}

# --- RAPHAEL il donnaiolo
RESE[3319] = "Se ti basta la mia"
# ⚠️ stesso giapponese di :3334 (「ふざけるな」) ma due inglesi diversi e due
# momenti diversi: qui e' il rifiuto alla proposta, li' e' il rifiuto durante
# la scelta. Due firme, due rese.
RESE[3320] = "Ma come ti permetti?"
RESE[3321] = ("Non sai chi sono? Sono Raphael, il più bel pezzo d'uomo di questa città, e forse "
              "di tutta Tyris del Nord. Le donne le prendo tutte quelle che voglio: potrei portarmi a "
              "letto perfino la principessa di Palmia. Solo che ultimamente il gioco della conquista "
              "mi ha stufato. A dirla tutta ne voglio una che mi serva e basta, senza fare storie. "
              "Che ne dici di lasciarmi una delle tue mogli? Ti ricompenso.")
RESE[3324] = "Bah, troppo bello per essere vero."
RESE[3328] = "Ottimo. Allora portami la tua bella mogliettina!"
RESE[3333] = "Mostrare la moglie"
RESE[3334] = "Lascia perdere"
RESE[3335] = "Vediamo, vediamo. Fammela esaminare, questa moglie!"
RESE[3338] = "Sbrigati, portamela."
RESE[3344] = "Non farmi penare."
RESE[3349] = "Una moglie voglio. Se non è una moglie non serve a niente!"
RESE[3365] = ('"Oh oh, e questa sarebbe tua moglie? " + cdatan(CDATAN_NAME, rc) + ", si chiama? '
              'Non fare la timida, vieni qui!"')
# ⚠️ deroga: l'inglese rovescia la battuta. 「いやん、おじさまったら♪」 e' la
# moglie che civetta con Raphael, non che si lamenta di essere lasciata li'.
RESE[3398] = "Uh, che modi, signore♪"
RESE[3401] = "M-ma tu... ghgh... tua mogl... ghgh... non è uman... ghgh"
RESE[3418] = ("Questa sì che è una gran moglie...! In fatto di donne mi sa che abbiamo lo stesso "
              "gusto. Se me ne porti un'altra così, ti do qualcosa di buono.")

# --- AINC il cavaliere novizio
RESE[3426] = "Yeeek!! Yeeeek! Ah... sei tu. Grazie di quella volta."
RESE[3430] = "Ci penso io"
RESE[3432] = ("Yeeek! No! Non avvicinarti! Yeeeek! Ah... ti chiedo scusa. Tu... a vederti sembri "
              "forte. Non è che mi dai una mano? Per diventare cavaliere devo superare una prova: "
              "abbattere il capo degli yeek. Per me è un compito troppo pesante... gli yeek... "
              "aaah... no, non ce la faccio... a ripensarci mi tremano le ginocchia. Ti prego, "
              "vai ad abbatterlo al posto mio.")
RESE[3435] = "Yeeeek!"
RESE[3439] = ("Mi salvi la vita. Una prova così io non la passo mai. La loro tana è nella grotta "
              "subito a ovest del villaggio. Conto su di te.")
RESE[3444] = "Yeeek! No! Non avvicinarti! Yeeeek! Ah... sei tu..."
RESE[3448] = ("Oh, il capo degli yeek l'hai abbattuto davvero. Adesso divento cavaliere sul serio. "
              "Grazie di cuore.")

# --- RENTON il mago tormentato
RESE[3797] = "Mi domando... la mia vita vale qualcosa?"
RESE[3801] = ("La fatica di chi ha talento e la fatica di chi non ne ha sono davvero la stessa cosa? "
              "Mia sorella era venuta a Lumiest per fare la pittrice. Amava le cose belle, ma di "
              "talento non ne aveva. Quando si accorse del proprio limite si ammalò nella mente e se "
              "la prese con tutti. Insultata, disprezzata, senza che nessuno la capisse, un giorno "
              "d'inverno si buttò nel lago e morì.")
RESE[3802] = ("Lo sapevo, io... che studiava pittura fino a rovinarsi la salute. Una passione fuori "
              "dal comune, e la fame di gloria. Ma poco dopo la sua morte arrivò in città un genio, "
              "e senza nessuna fatica ottenne tutto quello che lei aveva desiderato. Fama, "
              "felicità, ricchezza...")
RESE[3803] = ("Chi è baciato dalla sorte e chi no: è tutto un caso del destino... Non capisci bene "
              "dove voglio arrivare? Già, nemmeno io so spiegarlo. So solo che il senso della vita "
              "non lo trovo più. Tutto qui.")
RESE[3804] = ("...Mia sorella rileggeva sempre un libro illustrato di una scrittrice di fiabe, "
              "Rachel. Le sue cose le ho già fatte sparire tutte, ma quel libro vorrei leggerlo "
              "almeno una volta. Adesso forse riuscirei a capire un poco che cosa provava.")
# ⚠️ `_s3(p)` e' morfologia inglese e cade. La resa e' costruita per NON
# accordarsi col numero: `p` vale 1, 2 o 3, e «1 volumi» sarebbe sbagliato.
RESE[3825] = ('"Hai messo insieme " + p + " di quei volumi, per me? Ti ringrazio. Se ricordo bene la '
              'serie arriva al quarto. Se me li trovi tutti e quattro, in qualche modo ti '
              'ricompenserò."')
RESE[3841] = ("Oh... così questi sono i libri di Rachel. Era da tanto che non mi veniva voglia di "
              "leggere. Lascia che ci dia un'occhiata subito. ...Questi... questi sono! E "
              "questo! E... *Renton comincia a schiumare dalla bocca* ")
RESE[3843] = "... ..."
RESE[3844] = "... ... ..."
# ⚠️ deroga, ed e' la piu' grossa del lotto: l'inglese ha buttato via tutta la
# scena. 「ビーーー！バリリ！！…こんなモノ！…ビリビリビリビリ！」 e' Renton che
# STRACCIA i libri, e senza quella riga la battuta dopo (:3848) non ha causa.
# Lo spazio in coda e' la giuntura dell'inglese e si conserva.
# ⚠️ E costa tre righe contro una: e' il prezzo della deroga, non un difetto
# di misura — dentro il tetto ci sta.
RESE[3845] = ("Sbraaan! Strap!! Riiisc! Straaap!!! Roba come questa! Come questa! Come questa... "
              "strappa strappa strappa strappa! Ah... ah... hah... hah... ")
RESE[3847] = 'Ehekatl: \\"Miaao?\\"'
RESE[3848] = ("...Un disegno così lo può fare solo un genio. La fatica non basta. Mia sorella... per "
              "quanto si sforzasse, non ci sarebbe mai arrivata. Se una dea della fortuna esiste "
              "davvero, io la odierò. ...Scusami, ecco il compenso. Adesso lasciami solo per un po'.")

# --- MARKS il ladro leggendario
RESE[3870] = "Eh. Non preoccuparti, in casa tua non ci entro."
RESE[3874] = "Ti dispiacerebbe non rivolgermi la parola con tanta confidenza?"
RESE[3880] = ('"Ah, ma tu sei " + cdatan(CDATAN_AKA, CHARA_PLAYER) + " in persona, la celebrità '
              'di cui parlano tutti. Capiti a proposito. La piramide a nord di Porto Kapul, la '
              'conosci? Sta lì da quando Nefia era un deserto senza un filo d\'erba, e si dice '
              'che dentro dorma un tesoro antico. Ma l\'ingresso è protetto da una magia bizzarra e nessuno '
              'riesce a metterci mano. Anzi... nessuno ci riusciva."')
RESE[3882] = "Comprare"
RESE[3885] = ("A me, sai, è arrivata una lettera curiosa. Il mittente è Tsen, il signore della "
              "piramide, e dentro c'è scritto che mi concede il diritto di sfidarla. ...Ma non sono "
              "tanto sciocco da infilarmi da solo in una trappola pericolosa. Questa sfida te la "
              "cedo. Non gratis, s'intende: che ne dici di 20.000 monete d'oro?")
RESE[3888] = "Eh. Quando avrai il denaro, l'affare è sempre aperto."
RESE[3899] = "Ho ho ho. Affare fatto. E allora l'invito è tuo."

# --- NOEL la dinamitarda
RESE[3909] = "Sei ancora in circolazione, eh. Ammazzagente."
RESE[3912] = "Guarda un po' chi si vede. ...Ammazzadei."
# ⚠️ due giapponesi diversi, un inglese solo (lo stesso di :3968): il
# giapponese qui dice che ASPETTA il fiore rosso a Palmia, li' ordina di
# farlo sbocciare. Due firme, due rese, e a deciderle e' il giapponese.
RESE[3916] = "Aspetto che su Palmia sbocci un fiore rosso rosso."
RESE[3930] = ("Lo sento già: la sofferenza di tanta gente... il dolore... Ne hai uccisi tanti, vero? "
              "Bambini piccoli... donne... vecchi... neonati appena venuti al mondo... Stanotte ho "
              "il corpo in fiamme, non riuscirò a dormire. Grazie. Prendi il tuo compenso.")
RESE[3934] = ("Uhm. Hai la faccia di chi è cresciuto nella bambagia e non sa come gira il mondo "
              "qui. Torna con un po' di scuola di vita, e t'insegno tante cose.")
RESE[3939] = ("Senti, tu non sei di questa città, vero? Si sente dall'odore, chi viene da fuori. Il "
              "mondo di fuori a me ha insegnato una cosa sola: chi non ha forza viene usato, preso "
              "in giro e alla fine mangiato. In questa città c'è tanta gente che non riesce a "
              "strappare neanche un po' di pietà. Non ti incuriosisce sapere come campano?")
RESE[3940] = "Certo"
RESE[3942] = ("Noi viviamo succhiando il sangue degli altri. Qui l'odio, l'invidia, l'ostinazione e "
              "la cattiveria diventano forza. Derphy è la città dove i deboli che fuori vengono "
              "schifati e disprezzati si sentono riconoscere per la prima volta quello che sanno "
              "fare. Allora, non ti va di venire anche tu da questa parte?")
RESE[3945] = "Vattene da un'altra parte, gallina."
RESE[3950] = ("Ecco, anche tu eri dei nostri. Al posto del banchetto di benvenuto ti do una notizia "
              "ghiotta. A me, sai, immaginare tanta gente che soffre mi eccita da morire. Nella "
              "locanda di Palmia c'è una stanza con un peluche. In quel peluche mettici una bomba. "
              "Se mi riempi di sangue quella città tutta compunta, ti do un premio.")
RESE[3953] = "Comprare"
RESE[3956] = "Senti, la vuoi una bomba atomica? 12.000 monete d'oro."
RESE[3959] = "Ah, va bene."
RESE[3968] = "Su, falla sbocciare, la tua rosa rosso sangue."
