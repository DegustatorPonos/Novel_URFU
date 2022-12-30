define GalChoices = 0
define GalChoice = ["", "", ""]

label act2_Gal_meet3:
    "Вы заходите в бухгалтерию."
    scene GalBG
    show MCIdle at left
    "Вы видите дремлящую за столом Галину."
    menu:
        "Уйти":
            "Вы решаете не будить её."
            hide MCIdle
            scene bg_bbg
            return
        "Разбудить":
            mainChar "Добрый день, Галина Петровна!"
            
            if GalAtt < 0:
                show GalScream:
                    xalign 1.0
                    xzoom -1.0
                Galina "Етить твою за ногу!" with vpunch
                hide GalScream
                show GalIdle:
                    xalign 1.0
                    xzoom -1.0
                Galina "Что то срочное?"
            else:
                show GalIdle:
                    xalign 1.0
                    xzoom -1.0
                Galina "Ой, привет, [NameSpace], я тут прикорнула немного, чего хотел?"
            "Вы замечаете следы слез на лице Галины"
            menu:
                "Спросить, в чём дело":
                    if GalAtt < 0:
                        Galina "Какое тебе дело? Заняться нечем?"
                        menu:
                            "Уйти":
                                mainChar "Ладно, я к вам по делу..."
                                $GalAtt -= 2
                                return
                            "Спросить, в чём дело":
                                $galatt += 1
                                call Gal_3_1
                                return
                    else:
                        Galina "Ой да нормально все, все образумится."
                        call Gal_3_1
                        return
                "Проигнорировать это":
                    mainChar "Ладно, я к вам по делу..."
                    $GalAtt -= 2
                    return

label Gal_3_1:
    mainChar "Да ладно вам, не дело это просто так грустить."
    Galina "Предлагаешь в компании погрустить? {w}Садись тогда уж, сейчас чайку заварю."
    show bg_bbg
    "И вот вы сидите вдвоем за кружечками не в меру крепкого чая"
    hide bg_bbg
    hide GalIdle
    show GalSad:
        xalign 1.0
        xzoom -1.0
    Galina "...Ведь и показываешь и доказываешь что держишь у себя бедняжек, но ведь нет, принять не примем - места нет, помочь не поможем."
    Galina "Бумажки о том, что у меня приют нужной нет, и вот как жить то так?{w} Не фонд защиты животных, а какое то юридическое непотребство!"
    mainChar "Ну а как вы думали?{w} Помочь каждому животному нереально, а без бумажки где гарантии что деньги на нужды зверушек пойдут?"
    Galina "А куда еще деньги мне девать?{w} Я разве похожа на шарлатанку какую то?"
    menu:
        "А им откуда знать?":
            $GalAtt += 1
            mainChar "Ну смотрите..."
        "Ну вообще...":
            $GalAtt -= 1
            mainChar "Ну... если так посмотреть..."
            "Вы ловите неодобрительный взгляд Галины"
            if GalAtt < 0:
                call gal_3_ending_1
                return
    mainChar "Мы о вашей добросовестности из нашего знакомства знаем, а для них вы - случайная бабуля с кучей бездомышей."
    mainChar "Если помощи от приюта хотите тут по любому бумажку надо."
    Galina "Так ладно бумажку, это ведь и помещение отдельное нужно, квартирка-то моя не сойдет."
    mainChar "Это да, помещение другое нужно, но не думаю, что найти такое будет проблемой."
    mainChar "Найти то не проблема, а вот оплачивать все это дело..."
    mainChar "Ну... а вы не пробовали..."
    while GalChoices < 2:
        menu:
            "У родни попросить?[GalChoice[0]]":
                if len(GalChoice[0]) > 1:
                    call gal_3_2
                    return
                else:
                    Galina "Поругалась я с родней, не общаются они со мной больше.{w} Не нравится им мое занятие, что поделать."
                    mainChar "Оу, ну..."
                    $GalChoices += 1
                    $GalChoice[0] = " (Уже использовано)"
            "Кредит взять?[GalChoice[1]]":
                if len(GalChoice[1]) > 1:
                    call gal_3_2
                    return
                else:
                    Galina "Уже, нового не дадут, прошлые еще не отдала."
                    mainChar "Оу, ну..."
                    $GalChoices += 1
                    $GalChoice[1] = " (Уже использовано)"
            "Подрабатывать?[GalChoice[2]]":
                if len(GalChoice[2]) > 1:
                    call gal_3_2
                    return
                else:
                    Galina "Куда мне еще мотатьсяб на старость-то лет?"
                    mainChar "Оу, ну..."
                    $GalChoices += 1
                    $GalChoice[2] = " (Уже использовано)"
    call gal_3_2
    return


label gal_3_2:
    mainChar "Знаете, если все время искать оправдания, то вы так ничего не добьетесь."
    if GalChoices > 1:
        Galina "Ну, надо будет мне подумать еще, да..."
        "Наступила неловкая тишина, которую прервала открывающаяся дверь."
        show GenIdle
        with fade
        Gennadiy "Дня, это вы чем тут занимаетесь? {w} Работы мало?"
        Galina "А так мы тут это, по делам болтаем."
        Gennadiy "Ах вон оно как."
        Gennadiy "Не забудь после и ко мне по делам заглянуть, я к вам, Галина Петровна, позже тогда зайду."
        hide GenIdle
        with fade
        "Наступила неловкая тишина, которую прервала открывающаяся дверь."
        Galina "Нда-а, заболтались мы тут, что ты хотел?.."
        hide MCIdle
        hide GalSad
        scene bg_bbg
        "Вы решаете свои дела и расходитесь."
        $GalAtt += 2
        return
    else:
        hide GalSad
        show GalScream:
            xalign 1.0
            xzoom -1.0
        Galina "Это я то и оправдания ищу?" with vpunch
        Galina "Ну знаешь ли, я столько сил и времени ради них потратила, а тебе хватает совести меня так хаять!"
        call gal_3_ending_1
        return

label gal_3_ending_1:
    mainChar "Да я не это имел в виду..."
    "От последующей ругани Галины Петровны вас спасает внезапно открывшаяся дверь."
    show GenIdle
    with fade
    Gennadiy "Доброго дня, чего скандалите?"
    Galina "Не Ваше дело! Зачем пришел?"
    hide GalAngry
    hide GalSad
    hide GenIdle
    scene HallBG
    with fade
    "Вы решаете тихо покинуть кабинет, Геннадий и Галина остаются наедине."
    hide GalSad
    scene bg_bbg
    $GalAtt -= 2
    return  


