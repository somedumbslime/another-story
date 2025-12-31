init:

    $ pim1 = Character (u'Пионер 1', color = "#696969", what_color = "E2C778")
    #
    $ pim2 = Character (u'Пионер 2', color = "#a77338", what_color = "E2C778")
    #
    $ pim3 = Character (u'Пионер 3', color = "#a2df70", what_color = "E2C778")
    #
    $ pim4 = Character (u'Пионер 4', color = "#734f91", what_color = "E2C778")
    #
    $ pim5 = Character (u'Пионер 5', color = "#42ac80", what_color = "E2C778")
    # Серый
    $ pim6 = Character (u'Пионер 6', color = "#949eb8", what_color = "E2C778")
    #
    $ pim7 = Character (u'Пионер 7', color = "#f3f3f3", what_color = "E2C778")
    # Толик
    $ pim8 = Character (u'Пионер 8', color = "#b7be4f", what_color = "E2C778")
    # Русланчик
    $ pim9 = Character (u'Пионер 9', color = "#5259bd", what_color = "E2C778")
    # Богдан

    $ ot1 = Character (u'Отброс 1', color = "#c0c0c0", what_color = "E2C778")
    $ ot2 = Character (u'Отброс 2', color = "#c0c0c0", what_color = "E2C778")

    $ tl = Character (u'Толик', color = "#f3f3f3", what_color = "E2C778")
    $ bd = Character (u'Богдан', color = "#5259bd", what_color = "E2C778")
    $ rs = Character (u'Русланчик', color = "#b7be4f", what_color = "E2C778")
    $ sr = Character (u'Серый', color = "#42ac80", what_color = "E2C778")

    $ pv = Character (u'Повариха', color = "#5ccece", what_color = "E2C778")
    $ gr = Character (u'Гром', color = "#dd4c4c", what_color = "E2C778")
    $ tenb = Character (u'Тень', color = "#a3a3a3", what_color = "E2C778")


# Старший пионер-инструктор Филимонов
    $ muzhik = Character (u'Незнакомый мужик', color = "#b792e0", what_color = "E2C778")
    $ instr = Character (u'Инструктор', color = "#b792e0", what_color = "E2C778")

#-----------------------------
    # Пионерки
    $ pif1 = Character (u'Пионерка 1', color = "#e593d1", what_color = "E2C778")
    $ pif2 = Character (u'Пионерка 2', color = "#9f82a3", what_color = "E2C778")
    $ pif3 = Character (u'Пионерка 3', color = "#db7891", what_color = "E2C778")
    $ pif4 = Character (u'Пионерка 4', color = "#9b68dd", what_color = "E2C778")


# Спрайты --------------------

    # Толик
    image tl normal full = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((1920, 1080), (0, 0), 'mods/another_story/images/sprites/tl/tl.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((1920, 1080), (0, 0), 'mods/another_story/images/sprites/tl/tl.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((1920, 1080), (0, 0), 'mods/another_story/images/sprites/tl/tl.png'))



    # image tl normal full = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/normal/dv/dv_5_sport.png', (0, 0), 'mods/another_story/images/sprites/normal/dv/dv_5_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/normal/dv/dv_5_sport.png', (0, 0), 'mods/another_story/images/sprites/normal/dv/dv_5_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/normal/dv/dv_5_sport.png', (0, 0), 'mods/another_story/images/sprites/normal/dv/dv_5_angry.png'))


    # Серый

    image sr normal pioneer far = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((836, 1159), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body_far.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((836, 1159), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body_far.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((836, 1159), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body_far.png'))

    image sr normal pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png'))
    image sr evil_laugh pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_1_evil_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_1_evil_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_1_evil_laugh.png'))
    image sr happy pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_1_happy.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_1_happy.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_1_happy.png'))
    image sr laugh pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_1_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_1_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_1_laugh.png'))
    image sr smile pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_1_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_1_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_1_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_1_smile.png'))

    image sr normal2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_2_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_2_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_2_normal.png'))
    image sr serious pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_2_serious.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_2_serious.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_2_serious.png'))
    image sr surprise pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_2_surprise.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_2_surprise.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_2_surprise.png'))
    image sr angry pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_2_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_2_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_2_angry.png'))


    image sr angry2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_3_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_3_angry2.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_3_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_3_angry2.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_3_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_3_angry2.png'))
    image sr grin pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_3_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_3_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_3_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_3_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_3_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_3_grin.png'))
    image sr serious2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_3_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_3_serious2.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_3_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_3_serious2.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_3_body.png', (0, 0), 'mods/another_story/images/sprites/sr/ps_3_serious2.png'))

    image sr bottle pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_bottle.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_bottle.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_bottle.png'))
    image sr bottle_full pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_bottle_full.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_bottle_full.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sr/ps_2_bottle_full.png'))


    # Богдан

    image bd normal pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/1/bd_1_body.png', (0, 0), 'mods/another_story/images/sprites/bd/1/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/1/emo/normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/1/bd_1_body.png', (0, 0), 'mods/another_story/images/sprites/bd/1/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/1/emo/normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/1/bd_1_body.png', (0, 0), 'mods/another_story/images/sprites/bd/1/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/1/emo/normal.png'))
    image bd dumaet pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/1/bd_1_body.png', (0, 0), 'mods/another_story/images/sprites/bd/1/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/1/emo/dumaet.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/1/bd_1_body.png', (0, 0), 'mods/another_story/images/sprites/bd/1/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/1/emo/dumaet.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/1/bd_1_body.png', (0, 0), 'mods/another_story/images/sprites/bd/1/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/1/emo/dumaet.png'))

    image bd angry pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/angry.png'))
    image bd serious pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/hmur.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/hmur.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/hmur.png'))
    image bd scared pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/hmur.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/hmur.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/hmur.png'))
    image bd normal1 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/norm.png'))
    image bd pofig pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/pofig.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/pofig.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/pofig.png'))
    image bd radost pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/radost.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/radost.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/radost.png'))
    image bd radost_close pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/radost_close.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/radost_close.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/radost_close.png'))
    image bd smile pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/smile.png'))
    image bd grin pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/stestn.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/stestn.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/stestn.png'))
    image bd shocked pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/udiv.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/udiv.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/2/bd_2_body.png', (0, 0), 'mods/another_story/images/sprites/bd/2/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/2/emo/udiv.png'))

    image bd angry2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/angry.png'))
    image bd serious2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/hmur.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/hmur.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/hmur.png'))
    image bd scared2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/hmur.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/hmur.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/hmur.png'))
    image bd normal2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/norm.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/norm.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/norm.png'))
    image bd pofig2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/pofig.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/pofig.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/pofig.png'))
    image bd radost2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/radost.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/radost.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/radost.png'))
    image bd radost_close2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/radost_close.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/radost_close.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/radost_close.png'))
    image bd smile2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/smile.png'))
    image bd grin2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/stestn.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/stestn.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/stestn.png'))
    image bd shocked2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/udiv.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/udiv.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((675, 1077), (0, 0), 'mods/another_story/images/sprites/bd/3/bd_3_body.png', (0, 0), 'mods/another_story/images/sprites/bd/3/clothes/pioner.png', (0, 0), 'mods/another_story/images/sprites/bd/3/emo/udiv.png'))

    image bd scared droch = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/bd/bd_3_droch_ispug.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/bd/bd_3_droch_ispug.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/bd/bd_3_droch_ispug.png'))
    

    # Русланчик

    image rs normal pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/rs/ruslan_pioneer.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/rs/ruslan_pioneer.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/rs/ruslan_pioneer.png'))
    image rs bottle pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/rs/ruslan_bottle_full.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/rs/ruslan_bottle_full.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/rs/ruslan_bottle_full.png'))


    # Инструктор

    image instr normal pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((810, 1080), (0, 0), 'mods/another_story/images/sprites/instr/go2.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((810, 1080), (0, 0), 'mods/another_story/images/sprites/instr/go2.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((810, 1080), (0, 0), 'mods/another_story/images/sprites/instr/go2.png'))    
    image instr smile pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((810, 1080), (0, 0), 'mods/another_story/images/sprites/instr/go1.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((810, 1080), (0, 0), 'mods/another_story/images/sprites/instr/go1.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((810, 1080), (0, 0), 'mods/another_story/images/sprites/instr/go1.png'))


    # Гром

    image gr grin pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_1_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_grin.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_1_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_grin.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_1_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_grin.png'))
    image gr laugh pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_1_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_laugh2.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_1_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_laugh2.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_1_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_laugh2.png'))
    image gr normal pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_1_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_1_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_1_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_normal.png'))
    image gr scared pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_1_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_scared.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_1_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_scared.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_1_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_1_scared.png'))
    
    image gr angry pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_angry.png'))
    image gr guilty pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_guilty.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_guilty.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_guilty.png'))
    image gr laugh2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_laugh.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_laugh.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_laugh.png'))
    image gr rage pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_rage.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_rage.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_rage.png'))
    image gr shy pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_shy.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_shy.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_2_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_2_shy.png'))

    image gr happy pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_happy.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_happy.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_happy.png'))
    image gr shocked pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_shocked.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_shocked.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_shocked.png'))
    image gr smile pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_smile.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_smile.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_smile.png'))
    image gr smile2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_smile2.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_smile2.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_smile2.png'))
    image gr tender pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_tender.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_tender.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/gr/bo_3_body.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_pioneer.png', (0, 0), 'mods/another_story/images/sprites/gr/bo_3_tender.png'))


    # Отброс 1

    image ot1 angry pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot1/bydlo_angry_2kop.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot1/bydlo_angry_2kop.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot1/bydlo_angry_2kop.png'))
    image ot1 normal pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot1/bydlo_norm_2kop.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot1/bydlo_norm_2kop.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot1/bydlo_norm_2kop.png'))
    image ot1 scared pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot1/bydlo_scared_2kop.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot1/bydlo_scared_2kop.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot1/bydlo_scared_2kop.png'))
    image ot1 surprise pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot1/bydlo_surprise_2kop.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot1/bydlo_surprise_2kop.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot1/bydlo_surprise_2kop.png'))


    # Отброс 2

    image ot2 angry pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot2/gena_angry.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot2/gena_angry.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot2/gena_angry.png'))
    image ot2 angry2 pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot2/gena_angry2.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot2/gena_angry2.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot2/gena_angry2.png'))
    image ot2 normal pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot2/gena_normal.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot2/gena_normal.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ot2/gena_normal.png'))


    # Лысый

    image ls normal pioneer = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ls/Lysy.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ls/Lysy.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/ls/Lysy.png'))


    # Алиска сиськи

    image dv titka pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titka.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titka.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titka.png'))
    image dv titki pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki.png'))
    image dv titki_ruki pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_ruki.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_ruki.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_ruki.png'))
    image dv titki_leek1 pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_leek1.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_leek1.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_leek1.png'))
    image dv titki_leek2 pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_leek2.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_leek2.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_leek2.png'))
    image dv titki_leek3 pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_leek3.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_leek3.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_leek3.png'))
    image dv titki_leek4 pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_leek4.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_leek4.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/dv_2_titki_leek4.png'))
    image dv spina pioneer2 = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/Alisa_so_spiny.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/Alisa_so_spiny.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/dv/Alisa_so_spiny.png'))
    
    
    # Славя

    image sl book_lighter dress = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_book_lighter.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_book_lighter.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_book_lighter.png'))
    image sl book dress = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_book.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_book.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_book.png'))

    image sl underwear = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_underwear.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_underwear.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_underwear.png'))
    image sl underwear tits = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_underwear_tits.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_underwear_tits.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_underwear_tits.png'))
    image sl underwear serious = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_underwear_serious.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_underwear_serious.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_underwear_serious.png'))
    image sl shirt = ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_rub.png'), im.matrix.tint(0.94, 0.82, 1.0)), "persistent.sprite_time=='night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_rub.png'), im.matrix.tint(0.63, 0.78, 0.82)), True, im.Composite((900, 1080), (0, 0), 'mods/another_story/images/sprites/sl/sl_rub.png'))
    image sl shirt night = "mods/another_story/images/sprites/sl/sl_rub_night.png"




# Фоны -----------------------------

    image dhds_preview = "mods/another_story/images/cg/dhds_preview.png"

# label as_day_1:
    image lineyka_vse = "mods/another_story/images/cg/lineyka_vse.png"

    # наш домик
    image ext_dom_day = "mods/another_story/images/bg/ext_dom_day.jpg"
    image ext_dom_sunset = "mods/another_story/images/bg/ext_dom_sunset.jpg"
    image ext_dom_night = "mods/another_story/images/bg/ext_dom_night.jpg"
    image ext_dom_rain = "mods/another_story/images/bg/ext_dom_rain.jpg"

    image int_dom_day = "mods/another_story/images/bg/int_dom_day.jpg"
    image int_dom_sunset = "mods/another_story/images/bg/int_dom_sunset.jpg"
    image int_dom_night = "mods/another_story/images/bg/int_dom_night.jpg"
    image int_dom_night_lighton = "mods/another_story/images/bg/int_dom_night_lighton.jpg"
    image int_dom_night_windowlight = "mods/another_story/images/bg/int_dom_night_windowlight.jpg"

# label as_day_1_path_dininghall:

    image ext_dining_hall_back_day_7dl = "mods/another_story/images/bg/ext_dining_hall_back_day_7dl.jpg"
    image ext_dining_hall_backroad_day_7dl = "mods/another_story/images/bg/ext_dining_hall_backroad_day_7dl.jpg"
    image ext_dining_hall_backroad_night_7dl = "mods/another_story/images/bg/ext_dining_hall_backroad_night_7dl.jpg"




# label as_day_1_dininghall_morning:

    image int_dininghall_povariha = "mods/another_story/images/bg/int_dininghall_povariha.png"
    image int_dining_table_day = "mods/another_story/images/bg/int_dining_table_day.png"
    image int_dining_table_day_sr = "mods/another_story/images/bg/int_dining_table_day_sr.png"
    image int_dining_table_day_sr_bd = "mods/another_story/images/bg/int_dining_table_day_sr_bd.png"
    image int_dining_table_day_dv_razm = "mods/another_story/images/bg/int_dining_table_day_dv_razm.jpg"
    image int_dining_table_day_dv = "mods/another_story/images/bg/int_dining_table_day_dv.jpg"
    image int_dining_hall2 = "mods/another_story/images/bg/int_dining_hall2.jpg"
    image buterbrod_2kop = "mods/another_story/images/effects/buterbrod_2kop.png"
    image buterbrod_kus_2kop = "mods/another_story/images/effects/buterbrod_kus_2kop.png"

# label as_day_1_otkritie_smeni:

    image flag_sh = "mods/another_story/images/cg/flag_sh.png"
    image flag_bez = "mods/another_story/images/cg/flag_bez.png"
    image ext_square2_day_7dl = "mods/another_story/images/bg/ext_square2_day_7dl.jpg"

# label as_day_1_alisa_povela_buhat:

    image ext_forest_new_day = "mods/another_story/images/bg/ext_forest_new_day.jpg"
    image ext_lake_morning = "mods/another_story/images/bg/ext_lake_morning.png"
    # баня
    image ext_bathhouse_day = "mods/another_story/images/bg/ext_bathhouse_day.png"
    image ext_bathhouse_sunset = "mods/another_story/images/bg/ext_bathhouse_sunset.jpg"
    image ext_bathhouse_nolight_night = "mods/another_story/images/bg/ext_bathhouse_nolight_night.jpg"
    image int_banya = "mods/another_story/images/bg/int_banya.jpg"
    image int_banya_par = "mods/another_story/images/bg/int_banya_par.jpg"

    image int_banya_dv_vodka = "mods/another_story/images/bg/int_banya_dv_vodka.jpg"
    image int_banya_dv_drink = "mods/another_story/images/bg/int_banya_dv_drink.jpg"
    image glotok_vodki = "mods/another_story/images/effects/glotok_vodki.png"

    # drunk
    image int_banya_drunk1 = "mods/another_story/images/bg/drunk/int_banya_drunk1.jpg"
    image int_banya_drunk2 = "mods/another_story/images/bg/drunk/int_banya_drunk2.jpg"
    image int_banya_drunk3 = "mods/another_story/images/bg/drunk/int_banya_drunk3.jpg"
    image int_banya_drunk4 = "mods/another_story/images/bg/drunk/int_banya_drunk4.jpg"
    image int_banya_drunk5 = "mods/another_story/images/bg/drunk/int_banya_drunk5.jpg"
    image int_banya_drunk6 = "mods/another_story/images/bg/drunk/int_banya_drunk6.jpg"
    image int_banya_drunk7 = "mods/another_story/images/bg/drunk/int_banya_drunk7.jpg"

# label as_day_1_grom_club:

    image ext_vorota_drunk = "mods/another_story/images/bg/drunk/ext_vorota_drunk.jpg"
    image ext_club_drunk = "mods/another_story/images/bg/drunk/ext_club_drunk.jpg"
    image ext_club_drunk_dv = "mods/another_story/images/bg/drunk/ext_club_drunk_dv.jpg"
    image ext_club_drunk2 = "mods/another_story/images/bg/drunk/ext_club_drunk2.jpg"
    image int_club_drunk1 = "mods/another_story/images/bg/drunk/int_club_drunk1.jpg"
    image int_club_drunk2 = "mods/another_story/images/bg/drunk/int_club_drunk2.jpg"
   
    image int_club_narik = "mods/another_story/images/bg/int_club_narik.jpg"
    image int_club_day_vedro = "mods/another_story/images/bg/int_club_day_vedro.png"
    image int_club_day_vedro_ogurtsi = "mods/another_story/images/bg/int_club_day_vedro_ogurtsi.png"

    image samogov_v_ruke = "mods/another_story/images/effects/samogov_v_ruke.png"
    image braga_v_ruke = "mods/another_story/images/effects/braga_v_ruke.png"

    image int_club_vedro_drunk1 = "mods/another_story/images/bg/drunk/int_club_vedro_drunk1.jpg"
    image int_club_vedro_drunk2 = "mods/another_story/images/bg/drunk/int_club_vedro_drunk2.jpg"
    image int_club_vedro_drunk3 = "mods/another_story/images/bg/drunk/int_club_vedro_drunk3.jpg"
    image int_club_vedro_drunk4 = "mods/another_story/images/bg/drunk/int_club_vedro_drunk4.jpg"
    image int_club_vedro_drunk5 = "mods/another_story/images/bg/drunk/int_club_vedro_drunk5.jpg"

# label as_day_1_grom_club_podval:

    image skrimer1 = "mods/another_story/images/effects/skrimer/skrimer1.png"
    image skrimer2 = "mods/another_story/images/effects/skrimer/skrimer2.png"
    image skrimer3 = "mods/another_story/images/effects/skrimer/skrimer3.png"
    image skrimer4 = "mods/another_story/images/effects/skrimer/skrimer4.png"
    image skrimer5 = "mods/another_story/images/effects/skrimer/skrimer5.png"
    image skrimer6 = "mods/another_story/images/effects/skrimer/skrimer6.png"
    image skrimer7 = "mods/another_story/images/effects/skrimer/skrimer7.png"
    image skrimer8 = "mods/another_story/images/effects/skrimer/skrimer8.png"

    image int_club_sunset = "mods/another_story/images/bg/int_club_sunset.jpg"

# label as_day_1_nightmare:

    image ext_clubs_sunset = "mods/another_story/images/bg/ext_clubs_sunset_7dl.jpg"
    image ext_houses_night = "mods/another_story/images/bg/MRS_houses_night.jpg"
    image int_house_of_dv_night_no_light = "mods/another_story/images/bg/int_house_of_dv_night_no_light_7dl.jpg"

# label as_day_2_morning:


# label as_day_2_tualet:

    image ext_toilets_day = "mods/another_story/images/bg/ext_toilets_day.jpg"
    image int_toilets_day = "mods/another_story/images/bg/int_toilets_day.jpg"


# label as_day_2_alisa_tits:



# label as_day_2_revenge:

    image int_dining_table_day_podlivaet = "mods/another_story/images/bg/int_dining_table_day_podlivaet.jpg"
    image int_dining_table_day_mocha = "mods/another_story/images/bg/int_dining_table_day_mocha.jpg"
    image int_dining_table_day_pusto = "mods/another_story/images/bg/int_dining_table_day_pusto.jpg"


# label as_day_2_alisa_debt:

    image ext_backstage_alt_day_7dl = "mods/another_story/images/bg/ext_backstage_alt_day_7dl.jpg"


# label as_day_2_drochka:


# label as_day_2_beach:

    image ext_beach_day_draka1 = "mods/another_story/images/bg/beach_draka/ext_beach_day_draka1.jpg"
    image ext_beach_day_draka2 = "mods/another_story/images/bg/beach_draka/ext_beach_day_draka2.jpg"
    image ext_beach_day_draka3 = "mods/another_story/images/bg/beach_draka/ext_beach_day_draka3.jpg"
    image ext_beach_day_draka4 = "mods/another_story/images/bg/beach_draka/ext_beach_day_draka4.jpg"
    image ext_beach_day_draka5 = "mods/another_story/images/bg/beach_draka/ext_beach_day_draka5.jpg"
    image ext_beach_day_draka6 = "mods/another_story/images/bg/beach_draka/ext_beach_day_draka6.jpg"
    image ext_beach_day_draka7 = "mods/another_story/images/bg/beach_draka/ext_beach_day_draka7.jpg"
    image ext_beach_day_draka8 = "mods/another_story/images/bg/beach_draka/ext_beach_day_draka8.jpg"
    image ext_beach_day_draka9 = "mods/another_story/images/bg/beach_draka/ext_beach_day_draka9.jpg"
    image ext_beach_day_draka10 = "mods/another_story/images/bg/beach_draka/ext_beach_day_draka10.jpg"

# label as_day_2_mt_kover


# label as_day_2_old_house_alisa:

    image ext_old_building_day = "mods/another_story/images/bg/ext_old_building_day.jpg"
    image ext_old_building_day_rainy = "mods/another_story/images/bg/ext_old_building_day_rainy.jpg"
    image ext_old_building_night_moonlight = "mods/another_story/images/bg/ext_old_building_night_moonlight.jpg"

    image int_old_building_day = "mods/another_story/images/bg/int_old_building_day_7dl.jpg"
    image int_old_building_cab_day = "mods/another_story/images/bg/int_old_building_cab_day_7dl.jpg"

# label as_day_2_old_house_alisa_ero:

    image int_old_house_ero1 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero1.jpg"
    image int_old_house_ero2 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero2.jpg"
    image int_old_house_ero3 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero3.jpg"
    image int_old_house_ero4 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero4.jpg"
    image int_old_house_ero5 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero5.jpg"
    image int_old_house_ero6 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero6.jpg"
    image int_old_house_ero7 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero7.jpg"
    image int_old_house_ero8 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero8.jpg"
    image int_old_house_ero9 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero9.jpg"
    image int_old_house_ero10 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero10.jpg"
    image int_old_house_ero11 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero11.jpg"
    image int_old_house_ero12 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero12.jpg"
    image int_old_house_ero13 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero13.jpg"
    image int_old_house_ero14 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero14.jpg"
    image int_old_house_ero15 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero15.jpg"
    image int_old_house_ero16 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero16.jpg"
    image int_old_house_ero17 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero17.jpg"
    image int_old_house_ero18 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero18.jpg"
    image int_old_house_ero19 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero19.jpg"
    image int_old_house_ero20 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero20.jpg"
    image int_old_house_ero21 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero21.jpg"
    image int_old_house_ero22 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero22.jpg"
    image int_old_house_ero23 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero23.jpg"
    image int_old_house_ero24 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero24.jpg"
    image int_old_house_ero25 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero25.jpg"
    image int_old_house_ero26 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero26.jpg"
    image int_old_house_ero27 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero27.jpg"
    image int_old_house_ero28 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero28.jpg"
    image int_old_house_ero29 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero29.jpg"
    image int_old_house_ero30 = "mods/another_story/images/bg/old_house_dv/int_old_house_ero30.jpg"




# label as_day_2_mt_house:


# label as_day_2_bratki_zasada:

    image ext_forest_new_sunset = "mods/another_story/images/bg/ext_forest_new_sunset.jpg"
    image ext_forest_new_sunset_bratva = "mods/another_story/images/bg/ext_forest_new_sunset_bratva.jpg"
    image bd_les_scene = "mods/another_story/images/effects/bd_les_scene.png"
    


# label as_day_2_draka:

    image ext_forest_new_sunset_instr_izbit = "mods/another_story/images/bg/ext_forest_new_sunset_instr_izbit.jpg"

    image ext_backroad_night = "mods/another_story/images/bg/ext_backroad_night_7dl.jpg"
    image ext_backdoor_night = "mods/another_story/images/bg/ext_backdoor_night_7dl.jpg"

# label as_day_2_night_beach_sl:

    image ext_boathouse_night_book_fire = "mods/another_story/images/bg/ext_boathouse_night_book_fire.jpg"

# label as_day_1_sl_house:


# label as_day_2_sl_house_test:

    image ext_house_of_sl_night = "mods/another_story/images/bg/sl_house/ext_house_of_sl_night_7dl.jpg"
    image ext_house_of_sl_night2 = "mods/another_story/images/bg/sl_house/ext_house_of_sl_night2.jpg"
    image ext_house_of_sl_sunset = "mods/another_story/images/bg/sl_house/ext_house_of_sl_sunset.jpg"

    image int_house_of_sl_night = "mods/another_story/images/bg/sl_house/int_house_of_sl_night.jpg"
    image int_house_of_sl_light_night = "mods/another_story/images/bg/sl_house/int_house_of_sl_light_night.jpg"
    image int_house_of_sl_floor = "mods/another_story/images/bg/sl_house/int_house_of_sl_floor.jpg"

    image int_house_of_sl_1 = "mods/another_story/images/bg/sl_house/sl_house_scene/int_house_of_sl_1.jpg"



# label as_day_2_sl_house_sleep:

    image int_house_of_sl_floor_night = "mods/another_story/images/bg/sl_house/int_house_of_sl_floor_night.jpg"
    image mi_night = "mods/another_story/images/cg/mi_night.jpg"
    image mi_night_2 = "mods/another_story/images/cg/mi_night_2.jpg"
    image mi_night_3 = "mods/another_story/images/cg/mi_night_3.jpg"
    image sl_mi_bed = "mods/another_story/images/cg/sl_mi_bed.jpg"
    image int_house_of_sl_back_night = "mods/another_story/images/bg/sl_house/int_house_of_sl_back_night.jpg"
    image int_sl_mi_sleep = "mods/another_story/images/cg/int_sl_mi_sleep.png"
    image sl_mi_sleep_blue = "mods/another_story/images/cg/sl_mi_sleep_blue.jpg"

# ------------------------------

    image proda_budet = "mods/another_story/images/transitions/proda_budet.jpg"

# Еффекты ------------------------------

    image ruka2_2kop = "mods/another_story/images/effects/ruka2_2kop.png"




    #   ПЕРЕХОДЫ
    $ perehod_ebat = ImageDissolve("mods/another_story/images/transitions/f0079.jpg", 0.5, 100, reverse=False )
    $ perehod_ebat2 = ImageDissolve("mods/another_story/images/transitions/TS_0598.jpg", 1.0, 100, reverse=False )
    $ perehod_w = ImageDissolve("mods/another_story/images/transitions/perehod_w.jpg", 0.5, 100, reverse=True )



#   мызыка

    $ posledniu_geroy = "mods/another_story/audio/music/mainsoundtrack.MP3"
    $ pachka_cig = "mods/another_story/audio/music/dlyaphona.MP3"
    $ be_my_lover = "mods/another_story/audio/music/sexbemylover.MP3"
    $ posledniy_geroy_short = "mods/another_story/audio/music/mainsoundtrackbeznachala.MP3"
    $ sexsongrofl = "mods/another_story/audio/music/sexrofl.MP3"
    $ peremen = "mods/another_story/audio/music/clubmusic.MP3"

    $ epilog_music = "mods/another_story/audio/music/epilog_music.ogg"
    $ prologue_after_sex = "mods/another_story/audio/music/prologue_after_sex.ogg"

#   звуки

    $ shoroh = "mods/another_story/audio/sfx/shoroh.mp3"
    $ udarshag = "mods/another_story/audio/sfx/udarshag.mp3"
    $ tryapkavedro = "mods/another_story/audio/sfx/tryapkavedro.mp3"
    $ tryapkapol = "mods/another_story/audio/sfx/tryapkapol.mp3"
    $ public_toilet = "mods/another_story/audio/sfx/public_toilet.mp3"
    $ udar1 = "mods/another_story/audio/sfx/udar1.mp3"
    $ zvukseksa = "mods/another_story/audio/sfx/zvukseksa.mp3"