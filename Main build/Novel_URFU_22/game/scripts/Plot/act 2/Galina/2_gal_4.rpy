label act2_Gal_meet5:
    if GalBlueRoot:
        call act2_Gal_meet5_BlueRoot
        return
    "Вы заходите в кабинет к Галине Петровне, и застаете ее болтающей по телефону."
    scene GalBG
    show MCIdle at left
    show GalSmile:
        xalign 1.0
        xzoom -1.0
    show MCIdle at left
    Galina "Конечно Олечка я приеду, обязательно приеду!..{w} Да, да..."
    Galina "Хорошо, и Вадика, Вадика зови!..{w} Да, все да, давай пока!"
    mainChar "Здравствуйте Галина Петровна, что за радость?"
    show bg_bbg with fade
    "Вы даже не успеваете понять каким образом оказались в объятиях Галины Петровны."
    hide bg_bbg with fade
    Galina "Позвонила я!{w} Позвонила!{w} Ждут меня завтра к себе в гости в Качканаре!"
    mainChar "Во-оу, поздравляю получается!"    
    Galina "Ладно, у тебя что то срочное?{w} Я сейчас отпрошусь вещи собирать!.."
    $GalAtt = 1
    hide MCIdle
    hide GalSmile
    scene bg_bbg
    with fade
    "Вы решаете свои вопросы и расходитесь"

label act2_Gal_meet5_BlueRoot:
    if GalAtt > 0:
        "Вы заходите в кабинет к Галине Петровне, и застаете ее болтающей по телефону."
        scene GalBG
        show MCIdle at left
        show GalSmile:
            xalign 1.0
            xzoom -1.0
        show MCIdle at left
        Galina "Да да конечно!{w} Боже, спасибо вам большое!{w} Вы так много для них сделали!..{w} "
        Galina "Ага, хорошо... {w}Хорошо да, всего доброго, дай бог вам здоровья!"
        mainChar "Здравствуйте Галина Петровна, что за радость?"
        Galina "Представляешь - местный клуб собачников благотворительную акцию для моих бездомышей открыл!"
        menu:
            "Порадоваться":
                $GalAtt += 1
                mainChar "Во-оу, поздравляю получается!"
                Galina "Если все пройдет как надо, это ведь и на полноценное помещение для приюта можно надеяться!"
            "Посмеяться":
                $GalAtt -= 1
                mainChar "Хах, делать им больше видимо нечего..."
                if GalAtt < 0:
                    hide GalSmile
                    show GalScream:
                        xalign 1.0
                        xzoom -1.0
                    Galina "Нуждающимся они помогают, пользу в отличие от некоторых приносят."
                    hide GalScream
                    show GalSad:
                        xalign 1.0
                        xzoom -1.0

                else:
                    Galina "Если все пройдет как надо, это ведь и на полноценное помещение для приюта можно надеяться!"
        menu:
            "Порадоваться":
                $GalAtt += 1
                mainChar "Лишь бы все и вправду хорошо прошло!"
                hide GalSad
                hide GalSmile
                show GalSmile:
                    xalign 1.0
                    xzoom -1.0
                Galina "Боже а я то как надеюсь!"
                mainChar "У вас все получится, я в вас верю."
            "Усомниться":
                mainChar "Надеюсь что деньги хоть на животных пойдут, так ведь?"
                hide GalSad
                hide GalSmile
                show GalSad:
                    xalign 1.0
                    xzoom -1.0
                Galina "Это ты на что намекаешь?" with vpunch
                mainChar "Да так, ни на что..."
        Galina "Ладно, фух, ты зачем приходил то?"
        hide GalSad
        hide GalSmile
        hide MCIdle
        scene bg_bbg
        "Вы решаете свои вопросы и расходитесь"
    else:
        "Вы заходите в кабинет к Галине Петровне, и застаете ее за перебором купюр из конверта в конверт."
        scene GalBG
        show MCIdle at left
        show GalSad:
            xalign 1.0
            xzoom -1.0
        show MCIdle at left
        mainChar "Здравствуйте Гали..."
        "Галина Петровна чуть не соскочила со стула и крайне недовольно изменилась в лице" 
        hide GalSad
        show GalScream:
            xalign 1.0
            xzoom -1.0
        Galina "Тебя стучаться не учили?{w}  Убирайся!{w} Я занята!"
        mainChar "Но Галина Петровна..."
        Galina "Я не ясно выразилась?"
        Galina "Убирайся!" with vpunch
        hide GalScream
        hide MCIdle
        scene bg_bbg
        "Вы спешите покинуть кабинет, уворачиваясь от летящей вам в след кружки."
        $GalAtt = -10
        return
