﻿label act2_Semen_meet5():
    if $SAtt < -6:
        jump Semen_meet5_bad_bad
    else:
        scene SenG
        "Вы застает Семена и Галину Петровну, распивающих чаи на рабочем месте."
        show GalIdle
        show SemIdle at right
        mainChar "Добрый вечер, а что за чаепитие?"
        if $SAtt > 0:
            Semen "Да так, работы нет вот и время коротаем, а что?"
        else:
            Semen "Добрый, а какое тебе дело?"
        menu:
            "Можно к вам?":
                mainChar "Да так, интересно просто. Могу присоединиться?"
                jump Semen_meet5_good
            "Работы нет?":
                mainChar "Совсем что ли работы нет? А если у Генадия поинтересоваться? М?"
                jump Semen_meet5_bad

    return

label Semen_meet5_bad_bad():
    scene SenG
    show SemIdle
    "Вы застает Семена за ремонтом офисного компьютера"
    mainChar "Привет, а..."
    Semen "Пошел к черту."
    mainChar "Э-эм, а в чем.."
    Semen "Я неясно выразился?"
    mainChar "Ясно, ясно."
    $SAtt -= 20
    jump Semen_meet5_end
    return

label Semen_meet5_bad():
    Semen "Смотрите ка, крыса из ниоткуда выползла. Может в никуда и вернешься?"
    mainChar "Ну ну, сроки горят а вы здесь время зазря тратите? Я иду к Евгению Викторовичу."
    Semen "Ну крысеныш, тебе это еще аукнется."
    $SAtt -= 2
    jump Semen_meet5_end
    return

label Semen_meet5_good():
    if $SAtt < 0 and $GalAtt < 0:
       Galina "Нет, знаешь, мы тут так, по душам болтаем." 
       mainChar "Ладно, хорошо вам посидеть."
       jump Semen_meet5_end
    elif $SAtt > 0:
        Semen "Ну ладно, садись."

    elif $GalAtt > 0:
        Galina "Конечно! Тебе покрепче налить?"
    "Вы садитесь за стол, пригнав к нему соседний свободный стул"
    if $SAtt > $GalAtt:
        Semen "Ну как оно, жив еще?"
    else:
        Galina "Ну как оно, жив еще?"
    mainChar "Ну, типо того. Жизнь потихоньку налаживается, деньги хоть появились и слава богу."
    Galina "Ну это просто замечательно! Повезло тебе с коллективом."
    mainChar "Ладно. Галина Петровна, а как ваше ничего?"
    if $GalAtt >0:
        Galina "Просто замечательно!{w} Представляешь, недавно целая пачка пожертвований пришла от клуба собачников, и я даже задумалась свой мини приют открыть!{w} Остается лишь надеяться, что все и дальше будет так хорошо идти... еще чайку подлить?"
    else:
        Galina "Ну, ничего так, что сказать. Живу-доживаю себе. Еще чайку подлить?"
    menu:
        "Не":
            mainChar "Да нет, спасибо. Ну, а у тебя, Сема, как дела?"
            Semen "Нормально, жив еще и отлично."
        "Мне пора":
            mainChar "Ну, я уже думаю пойду. Хорошо посидели."
            jump Semen_meet5_end
    "Из своего кабинета выходит Евгений Викторович"
    show EVcalm
    EV "Так так так, это что тут еще за посиделки? На рабочем то месте?"
    mainChar "Да уже никаких, сматываем удочки."
    EV "Ну смотрите у меня."
    jump Semen_meet5_end
    return

label Semen_meet5_end():
    
    return