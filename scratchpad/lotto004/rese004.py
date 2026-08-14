import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- l'acido sull'equipaggiamento. ⚠️ genitivo: 「name の itemname は…」.
    #     Il dativo riflessivo, come a :6399 e :6411.
    (4200, '  is damaged by acid.'):
        'name(item_acid_arg1) + " si vede rovinare " + itemname(locvar_item_acid_ci, , 1) + " dall\'acido."',
    (4213, '  is melted by acid.'):
        'name(item_acid_arg1) + " si vede sciogliere " + itemname(locvar_item_acid_ci, , 1) + " dall\'acido."',
    # qui il possesso si attacca in coda: la forma di proc.hsp, vista a schermo
    (4223, '  is immune to acid.'):
        'name(item_acid_arg1) + " porta addosso " + itemname(locvar_item_acid_ci, , 1) + ", che l\'acido non intacca."',

    # --- il fuoco. ⚠️ itemname() puo' essere PLURALE: l'elemento diventa
    #     soggetto cosi' il verbo resta singolare qualunque cosa arrivi.
    (4274, ' on the ground get perfectly broiled.'):
        '"Il fuoco arrostisce a puntino " + itemname(locvar_item_acid_ci, inv(INV_ITEM_NUM, locvar_item_acid_ci)) + " per terra."',
    (4280, '  get perfectly broiled.'):
        '"Il fuoco arrostisce a puntino " + itemname(locvar_item_acid_ci, inv(INV_ITEM_NUM, locvar_item_acid_ci), 1) + " che " + name(item_fire_arg1) + " porta addosso."',
    (4316, ' protects  stuff from fire.'):
        'itemname(locvar_item_fire_ti, 1) + " protegge dal fuoco quello che " + name(item_fire_arg1) + " porta addosso."',
    (4324, ' turns to dust.'):
        'itemname(locvar_item_fire_ti, 1) + " si riduce in cenere."',
    (4337, ' exploded.'):
        '"Il fuoco fa esplodere " + itemname(locvar_item_acid_ci, locvar_item_acid_p) + "."',
    # ⚠️ :4369 e' RINVIATA: riga commentata nel sorgente. La resa esisteva gia'
    #    comunque (proc.hsp:6481, text.hsp:13). Vedi il docstring.
    (4387, '  equip turn to dust.'):
        '"Il fuoco riduce in cenere " + itemname(locvar_item_acid_ci, locvar_item_acid_p) + " che " + name(item_fire_arg1) + " indossa."',
    (4397, '  turn to dust.'):
        '"Il fuoco riduce in cenere " + itemname(locvar_item_acid_ci, locvar_item_acid_p, 1) + " che " + name(item_fire_arg1) + " porta addosso."',
    (4404, ' on the ground turn to dust.'):
        '"Il fuoco riduce in cenere " + itemname(locvar_item_acid_ci, locvar_item_acid_p) + " per terra."',

    # --- il gelo.
    (4506, ' protects  stuff from cold.'):
        'itemname(locvar_item_fire_ti, 1) + " protegge dal gelo quello che " + name(item_cold_arg1) + " porta addosso."',
    (4511, ' is broken to pieces.'):
        '"Il gelo manda in frantumi " + itemname(locvar_item_fire_ti, 1) + "."',
    # ⚠️ :4520 e' RINVIATA a toppa: il prefisso possessivo lo costruisce :4491,
    #    dentro una lang() che estrai.py non vede. Vedi il docstring.

    # --- txteledmg: i tre gradini di ogni danno elementale.
    #     0 = ferito, 1 = ucciso da chi attacca (CODA), 2 = morto.
    (4761, ' melt.'):
        '"L\'acido scioglie " + name(txteledmg_arg3) + "."',
    (4768, ' get a cut.'):
        'name(txteledmg_arg3) + " riporta un taglio."',
    # coda senza soggetto, come «uccide sul colpo.» di :6843.
    # ⚠️ niente clitico: «lo fa a listarelle» concorderebbe col personaggio
    (4772, 'cut  into thin strips.'):
        '"taglia a listarelle."',
    (4775, '  cut into thin strips.'):
        'name(txteledmg_arg3) + " finisce a listarelle."',
    (4782, ' was beaten with chestnuts.'):
        '"Le castagne colpiscono " + name(txteledmg_arg3) + "."',
    # ⚠️ il giapponese e' una coda, ma l'inglese ci ha rimesso un name():
    #    la rete 11 pretende che ci sia
    (4786, '  gouged to death with chestnuts.'):
        '"Le castagne crivellano " + name(txteledmg_arg3) + " a morte."',
    (4789, '  gouged by chestnuts and died.'):
        'name(txteledmg_arg3) + " non regge ai colpi delle castagne e muore."',
    (4796, ' received a shock to the brain.'):
        'name(txteledmg_arg3) + " prende una scossa al cervello."',
    # ⚠️ «il cervello di X» fonderebbe: il -ne enclitico della 37ª. E il name()
    #    che l'inglese dichiara e' quello di CHI ATTACCA (arg2)
    (4800, ' burst  brain.'):
        'name(txteledmg_arg2) + " ne fa scoppiare il cervello."',
    (4803, ' die from brain rupture.'):
        'name(txteledmg_arg3) + " muore con il cervello in pezzi."',
    # ⚠️ genitivo: «la testa di X»
    (4810, ' head was hit with tofu.'):
        '"Un angolo di tofu centra " + name(txteledmg_arg3) + " in testa."',
    (4814, ' crush  head with tofu.'):
        'name(txteledmg_arg2) + " colpisce " + name(txteledmg_arg3) + " alla testa con un angolo di tofu."',
    (4817, ' die from being hit in the head with tofu.'):
        'name(txteledmg_arg3) + " muore per un angolo di tofu in testa."',
    (4823, 'change  into a doll.'):
        '"trasforma " + name(txteledmg_arg3) + " in una bambola."',
    (4826, ' change into a doll.'):
        'name(txteledmg_arg3) + " perde ogni libertà e diventa una bambola."',
    # coda: il possesso resta implicito, come fa il giapponese
    (4832, 'burst the body of .'):
        '"fa crollare il corpo dall\'interno."',
    (4835, ' burst and die.'):
        'name(txteledmg_arg3) + " non regge e il corpo crolla."',
    (4841, '  wounded.'):
        '"Il colpo ferisce " + name(txteledmg_arg3) + "."',
    # copiata da chara_func.hsp:6843, stesso giapponese 「殺した。」
    (4845, 'kill .'):
        '"uccide sul colpo."',
    (4848, '  killed.'):
        'name(txteledmg_arg3) + " muore."',
}
