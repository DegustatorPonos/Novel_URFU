label act1part3_alex():
    scene bg_bbg
    "Вы идёте в другой конец комнаты к столу, за который уже садится Александр."
    with dissolve
    scene bg_workplace_alex
    show AlIdle
    mainChar "Так вот, насчёт поручения…"
    Alex "Дада, помню. {w}Вообще, зря пришёл. {w}У меня всё норм."
    Alex "А чё вообще ему приспичило ко мне кодера позвать?"
    menu:
        "А чё, повежливее нельзя?":
            hide AlIdle
            show AlAngry
            Alex "А чё, поспокойнее нельзя?"
            $AlexAtt -= 2
            hide AlAngry
            show AlIdle
        "Самому бы знать":
            hide AlIdle
            show AlHappy
            Alex "Хех, он как всегда…"
            $AlexAtt += 2
            hide AlHappy
            show AlIdle
    Alex "Ну, в любом случае мы типа коллеги с тобой. {w}Или нет?"
    mainChar "Ну типа того."
    if knowAboutVerse:
        Alex "Ты же вроде с Сёмой болтал, он тебе про мои поэмы рассказал?"
        mainChar "Да, не очень лестно, кстати."
        Alexl "НУ это он просто не понимает. {w}Некультурный, что с него взять"
    else:
        Alex "Так вот, я вообще писатель! {w}И вполне себе ничего такой!"
        mainChar "Вы не об этом с тем парнем?"
        Alex "Ну типа да, но..."
        Alex "Ну..."
        Alex "Короче да!"
    hide AlIdle
    show AlHappy
    Alex "Так это, хочешь тоже почитать?"
    Alex "Я на почту скину"
    menu:
        "Исходя из отзыва того парня. Нет.":
            hide AlHappy
            show AlAngry
            $AlexAtt -= 2
            Alex "Блин, вот обидно было. {w}Ты вообще его не понял. {w}Короче отправлю на почту тебе, сам почитаешь и сам оценишь!"
            hide AlAngry
            show AlIdle
        "Ты же всё равно отправишь, да?":
            $AlexAtt -= 1
            Alex "Да!"
            Alex "Ты же не против?"
            menu:
                "Да нет…":
                    $AlexAtt += 1
                    Alex "Замечательно!"
                "От моего ответа же ничего не зависит?":
                    $AlexAtt -= 1
                    Alex " Может быть."
        
        "Слушай, звучит заманчиво.":
            $AlexAtt += 2
            Alex "Ну хоть кому-то они нравятся"
            mainChar "Но я их ещё не видел…"
    Alex "Тебе понравится, обещаю!"
    mainChar "Уж надеюсь…"
    hide AlHappy
    show AlIdle
    Alex "Ну ладно, нормально поболтали вроде, но мне мне типа работать надо"
    if knowAboutVerse:
        Alex "Ты кстати насчёт зп уже говорил?"
        mainChar "В смысле?"
        Alex "Ну там у нас чёт с банками муть, поговори об этом с Галей."
        Alex "Она там сидит, напротив отдела разработки."
        mainChar "Ладно, спасибо, сейчас зайду."
        Alex "Давай!"
        "Вы выходите из отдела разработки в сторону бухгалтерии."
        jump act1part4
    else:
        Alex "Зайди к Сёме, думаю он тебе тоже много чё расскажет."
        Alex "Ну, давай."
        mainChar "Давай…"
        "Вы направляетесь к месту в офисе, откуда вы ушли"
        $knowAboutVerse = True
        jump act1part3_sema
    return



label act1part3_sema():
    scene bg_workplace_sema
    if knowAboutVerse:
        "Вы подходите к парню, сидящему за компьютером"
        show SeIdle
        mainChar "Вы Семён?"
        Semen "Ну да. {w}А что?"
        mainChar "Александр просил меня к Вам подойти."
        Semen "Зачем?"
        mainChar "Не знаю."
        Semen "Ну и вали тогда, отвлекаешь."
        "Вы стоите в неловкой тишине"
        "…"
        "Вы решаетесь прервать паузу"
        mainChar "Вы насчёт его.. творчества ругались?"
        Semen "Да.{w} Он и к тебе уже докопался?"
        mainChar "Да"
        Semen "Совет – не читай. {w}Пожалеешь."
        menu:
            "Всё настолько плохо?":
                $SAtt += 2
                Semen " Значит, ты ещё не читал. {w}Прочтёшь хотя бы один стих – поймёшь меня."
            "Ну не может всё быть настолько плохо!":
                $SAtt -= 2
                hide SeIdle
                show SeAngry
                Semen "Ты мне не веришь?"
                Semen "Посмотрим, что ты скажешь, когда он тебе будет ими спамить каждый вечер и требовать рецензий."
                hide SeAngry
                show SeIdle
        mainChar "Ну, выбора у меня всё равно не было, придётся читать."
        Semen "Сочувствую."
    else:
        show SeHappy
        Semen "А, ты же новый."
        Semen "Короче вот этот чувак – Саней звать – стихи пишет."
        Semen "Ну и как бы сказать…"
        Semen "Писать-то пишет, но вот качество оных его не заботит от слова совсем. {w}Вообще не советую читать, говнище то ещё."
        menu:
            "Всё настолько плохо?":
                $SAtt += 2
                Semen " Значит, ты ещё не читал. {w}Прочтёшь хотя бы один стих – поймёшь меня."
                hide SeHappy
                show SeIdle
            "Ну не может всё быть настолько плохо!":
                hide SeHappy
                show SeAngry
                $SAtt -= 2
                Semen "Ты мне не веришь?"
                Semen "Посмотрим, что ты скажешь, когда он тебе будет ими спамить каждый вечер и требовать рецензий."
                hide SeAngry
                show SeIdle
        $knowAboutVerse = True
        Semen "Вообще тебе бы к нему сходить, раз тебя Евгений Викторович попросил…"
        Semen "Но вот тебе совет – не соглашайся на чтение его стихов. {w}Вот не пожалеешь."
    Semen "Кстати, а ты кем устроился?"
    mainChar "Программистом."
    Semen "Ну и как пишется?"
    mainChar "Ну когда как…"
    Semen "Давай сразу договоримся. {w}Без тест-кейсов пушить даже не думай. {w}Пойдёт?"
    menu:
        "А давай договоримся – в мою работы ты лезть не будешь.":
            hide SeIdle
            show SeAngry
            $SAtt -= 2
            Semen "А я и не лезу, тесты – это работа моя."
            Semen "А ты сейчас пытаешься усложнять её для всех."
            menu:
                "А мне откуда было знать, что ты у нас тестировщик?":
                    Semen "А это на что-то бы повлияло?"
                "Блин, как-то неловко вышло, прости":
                    $SAtt += 1
                    Semen "Ладно, проехали."
            hide SeAngry
            show SeIdle
        "А их можно не ставить?":
            hide SeIdle
            show SeAngry
            $SAtt -= 1
            Semen "Прикинь, вообще да. {w}И мне бы очень хотелось, чтобы ты до этого не опускался."
            mainChar "Да без проблем, будем писать."
            Semen "Вот так бы сразу. {w}И со всеми."
            hide SeAngry
            show SeIdle
        "Да в принципе без проблем.":
            hide SeIdle
            show SeHappy
            $SAtt += 2
            Semen "Ну наконец, нормальный человек!"
            Semen "Сразу и хорошо!"
            Semen "Осталось понять, сколько твои слова стоят."
            hide SeHappy
            show SeIdle
    mainChar "А что, нынешний билд вообще признаки жизни подаёт?"
    Semen "Ну смотря что ты имеешь в виду под словами “признаки жизни”"
    Semen "Я бы сказал, что он бьётся в агонии, но никак не умрёт."
    mainChar "Жёстко."
    Semen "Зато честно."
    if knowAboutVerse:
        Semen "Ты, кстати, уже про карту поговорил?"
        mainChar "Про какую?"
        Semen "Значит нет."
        Semen "Короче, у нас договор со СтрахБанком и зарплату мы на их карты получаем. {w}Вот у тебя лично их карта?"
        mainChar "Нет…"
        Semen "Не удивлён. {w}Их услугами вообще на самом деле никто не пользуется."
        Semen "Но вот решила Галина, что с ними выгодно работать, так что приходится. {w} Зайди к ней, поговори об этом. {w}У неё офис прямо напротив выхода из отдела."
        Semen "Ну, давай, у меня работы навалом."
        mainChar "Давай."
        "Вы выходите из отдела разработки и заходите в бухгалтерию."
        jump act1part4
    else:
        Semen "Кстати, ты так прикольно Саню задинамил."
        Semen "Иди, поговори с ним, особенно раз тебя Евгений Викторович просил. {w}Только запомни – НА СТИХИ НЕ СОГЛАШАЙСЯ!"
        Semen "Ни при каких обстоятельствах. {w}Понял?"
        mainChar "Понял."
        Semen "Ну, давай, у меня работы навалом."
        mainChar "Давай."
        $knowAboutVerse = True
        jump act1part3_alex
    return