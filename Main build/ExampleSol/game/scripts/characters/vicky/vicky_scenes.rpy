init python:
    def vicky_titfuck_sideview_xray():
        if store.vicky_titfuck_xray_style == "normal":
            store.vicky_titfuck_xray_style = "xray"
        else:
            store.vicky_titfuck_xray_style = "normal"
        
        if store.vicky_titfuck_xray_style == "xray":
            renpy.show("bg vicky_titfuck_sideview_xray", tag = "bg")
        else:
            renpy.show("bg vicky_titfuck_sideview", tag = "bg")
        
        return

    def vicky_titfuck_special_button(image, style):
        store.vicky_titfuck_xray_style = style
        renpy.show(image, tag = "bg")
        
        return

screen vicky_titfuck_mash_xray:
    vbox:
        spacing 30
        xalign 0.025
        yalign 0.025

        use main_menu_button(text="Нормально", enabled=vicky_titfuck_xray_style != "normal", action=Function(vicky_titfuck_special_button, "bg vicky_titfuck_nocum", "normal") )
        use main_menu_button(text="Рентген", enabled=vicky_titfuck_xray_style != "xray", action=Function(vicky_titfuck_special_button, "bg vicky_titfuck_nocum_xray", "xray") )
        use main_menu_button(text="Рентген 2", enabled=vicky_titfuck_xray_style != "penisonly", action=Function(vicky_titfuck_special_button, "bg vicky_titfuck_nocum_penisonly", "penisonly") )

screen vicky_titfuck_mash_cum_xray:
    vbox:
        spacing 30
        xalign 0.025
        yalign 0.025

        use main_menu_button(text="Нормально", enabled=vicky_titfuck_xray_style != "normal", action=Function(vicky_titfuck_special_button, "bg vicky_titfuck_cum", "normal") )
        use main_menu_button(text="Рентген", enabled=vicky_titfuck_xray_style != "xray", action=Function(vicky_titfuck_special_button, "bg vicky_titfuck_cum_xray", "xray") )
        use main_menu_button(text="Рентген 2", enabled=vicky_titfuck_xray_style != "penisonly", action=Function(vicky_titfuck_special_button, "bg vicky_titfuck_cum_penisonly", "penisonly") )

screen vicky_titfuck_sideview_xray:
    use main_menu_button(text="Рентген", action=Function(vicky_titfuck_sideview_xray), xalign=0.03, yalign=0.05 )

label vicky_pre_intro:
    $ nate_room.decide_and_play_daily_music_queue()
    call process_scene_beginning (bg=nate_room)

    call process_character (n, appearance="outfit clothes pose handsdown face aroused blush false", text="{i}Зевок.{/i}..")
    call process_character (n, appearance="outfit clothes pose handsdown face aroused blush false", text="...{p}...")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="(Интересно, кто-нибудь уже смотрел мой обзор, который я сделал вчера...)")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="...{p}...")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="(Эй!)")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="(Это очень хорошо!)")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="(Им делятся и обсуждают тоже!)")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="...")
    call process_character (n, appearance="outfit clothes pose handfist face neutral blush false", text="{b}{i}(Если отзывы продолжат смотреть...){/i}{/b}")
    call process_character (n, appearance="outfit clothes pose handfist face happy blush false", text="{b}{i}(То возможно, я получу предложение о партнерстве с ReflexViz.HD!){/i}{/b}")

    $ reset_all_characters()
    if started_main_game:
        $ had_vicky_pre_intro_scene = True
        call day_reset_locations_chars
        call day_start_after_location_reset
    else:
        jump debug_menu

    return

label vicky_intro:
    $ nate_room.decide_and_play_daily_music_queue()
    call process_scene_beginning (bg=nate_room)

    call process_character (n, appearance="outfit clothes pose behindhead face aroused blush false", text="(Похоже, я проснулся немного раньше...)")
    call process_character (n, appearance="outfit clothes pose behindhead face aroused blush false", text="...")
    call process_character (n, appearance="outfit clothes pose behindhead face happy blush false", text="(О! Я должен проверить, как последний обзор поживает!)")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="...{p}...")
    call process_character (n, appearance="outfit clothes pose handfist face happy blush false", text="(Все в порядке!)")
    call process_character (n, appearance="outfit clothes pose handfist face happy blush false", text="(Он зашёл лучше, чем предыдущий!)")
    call process_character (n, appearance="outfit clothes pose handfist face happy blush false", text="...")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="(Хм?)")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="(Я получил личное сообщение...)")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="{i}Задыхается!{/i}")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="(Это от ReflexViz.HD!)")
    call process_character (n, appearance="outfit clothes pose behindhead face neutral blush false", text="(Что там говорится...)")
    call process_character (n, appearance="outfit clothes pose behindhead face neutral blush false", text="...")

    "\"Привет, меня зовут [vicky.say_name] Харди, и я работаю в качестве местного филиала ReflexViz.HD.\""
    "\"Вашими обзорами часто делились на нашем сайте, и я хотела бы обсудить с вами возможность создания партнерской программы.\""

    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="(О боже мой, о боже мой!)")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="(Вот оно!)")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="(Что еще в нем говорится...)")

    "\"Я хотела бы поговорить с вами в следующий раз, когда вы будете доступны.\""
    "\"Вы можете связаться со мной через чат, используя ссылку, которую я предоставила.\""
    "\"С нетерпением жду вашего ответа.\""

    call process_character (n, appearance="outfit clothes pose handfist face happy blush false", text="(Не может быть!)")
    call process_character (n, appearance="outfit clothes pose handfist face happy blush false", text="(Это грандиозно!)")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="(Получение партнерского предложения в такой ранний срок - отличный знак!)")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="(Я не хочу упустить эту возможность!)")
    call process_character (n, appearance="outfit clothes pose handfist face happy blush false", text="(Я напишу им в чат прямо сейчас!)")


    call process_new_location (bg=nate_room, force_bg_change=True)

    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="(Подключаюсь...)")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothes pose twohandfist face neutral blush false", text="(Хорошо, я вошёл!)")
    call process_character (n, appearance="outfit clothes pose twohandfist face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="(Я думаю, что я должен напечатать что-то, чтобы увидеть, здесь ли [vicky.say_name]...)")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="\"Привет.\"")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="\"Я нажал на ссылку, чтобы присоединиться к приватному чату.\"")
    call process_character (vicky, appearance="", text="\"Здравствуйте!\"")
    call process_character (vicky, appearance="", text="\"Как ты себя чувствуешь сегодня?\"")
    call process_character (n, appearance="outfit clothes pose handsdown face happy blush false", text="(Да, она здесь!)")
    call process_character (n, appearance="outfit clothes pose handsdown face happy blush false", text="\"У меня все хорошо!\"")
    call process_character (vicky, appearance="", text="\"Это здорово слышать!\"")
    call process_character (vicky, appearance="", text="\"Вы владелец канала \"Твинстикс?\"")
    call process_character (n, appearance="outfit clothes pose handfist face happy blush false", text="\"Да!\"")
    call process_character (n, appearance="outfit clothes pose handfist face happy blush false", text="\"Он принадлежит мне и моей сестре.\"")
    call process_character (vicky, appearance="", text="\"Вы принимаете решения на канале?\"")
    call process_character (n, appearance="outfit clothes pose behindhead face neutral blush false", text="\"Уум...\"")
    call process_character (n, appearance="outfit clothes pose behindhead face neutral blush false", text="\"Я думаю, что да.\"")
    call process_character (vicky, appearance="", text="\"Хорошо, замечательно!\"")
    call process_character (vicky, appearance="", text="\"Я просто хотела убедиться, что вы один из создателей.\"")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="\"Попался.\"")
    call process_character (vicky, appearance="", text="\"Я не знаю вашего имени.\"")
    call process_character (vicky, appearance="", text="\"Не могли бы вы дать его мне для моего досье?\"")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="\"Меня зовут [n.say_name] [last_name].\"")
    call process_character (vicky, appearance="", text="\"Спасибо.\"")
    call process_character (vicky, appearance="", text="\"Ну, мистер [last_name], я предполагаю, что вы заинтересованы в партнерстве с ReflexViz.HD?\"")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="\"Конечно\"")
    call process_character (vicky, appearance="", text="\"Отлично!\"")
    call process_character (n, appearance="outfit clothes pose handfist face neutral blush false", text="\"Итак, как мне стать партнером?\"")
    call process_character (vicky, appearance="", text="\"Я рада, что вы спросили!\"")
    call process_character (vicky, appearance="", text="\"Для того, чтобы стать нашим партнером, вы должны подписать договор.\"")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="\"Хорошо!\"")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="\"Вы можете отправить его мне по электронной почте?\"")
    call process_character (vicky, appearance="", text="\"На самом деле этот контракт должен быть подписан лично.\"")
    call process_character (vicky, appearance="", text="\"Мне нужно иметь юридическую подпись, подтверждающую партнерство.\"")
    call process_character (n, appearance="outfit clothes pose behindhead face concerned blush false", text="\"О...\"")
    call process_character (n, appearance="outfit clothes pose behindhead face concerned blush false", text="\"Как я смогу это сделать?\"")
    call process_character (vicky, appearance="", text="\"Не беспокойтесь!\"")
    call process_character (vicky, appearance="", text="\"Я близко нахожусь к вашей месту проживания!\"")
    call process_character (vicky, appearance="", text="\"ReflexViz разместил сотрудников, таких как я, повсюду, поэтому встреча требует минимум передвижений!\"")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="\"Где именно вы находитесь?\"")
    call process_character (vicky, appearance="", text="\"Я могу отправить вам инструкции по электронной почте.\"")
    call process_character (vicky, appearance="", text="\"У меня офис в моей квартире.\"")
    call process_character (n, appearance="outfit clothes pose twohandfist face neutral blush false", text="\"Потрясающе!\"")
    call process_character (n, appearance="outfit clothes pose twohandfist face neutral blush false", text="\"Когда мы можем встретиться?\"")
    call process_character (vicky, appearance="", text="\"Когда вам удобно!\"")
    call process_character (vicky, appearance="", text="\"Просто дайте мне знать заранее, и я впишу вас в своё расписание!\"")
    call process_character (n, appearance="outfit clothes pose handsdown face happy blush false", text="\"Я не могу дождаться!\"")
    call process_character (vicky, appearance="", text="\"Я только что отправила инструкции.\"")
    call process_character (vicky, appearance="", text="\"Я с нетерпением жду встречи с вами мистер [last_name]!\"")
    call process_character (n, appearance="outfit clothes pose handsdown face happy blush false", text="\"Я то же!\"")

    "{i}Чат Отключен.{/i}"

    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="(Это так замечательно!)")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="(Я отправлюсь туда, как только смогу!)")

    "{i}Теперь вы можете ездить на квартиру [vicky.say_name].{/i}"

    $ reset_all_characters()
    if started_main_game:
        $ had_vicky_intro_scene = True
        call day_reset_locations_chars
        call day_start_after_location_reset
    else:
        jump debug_menu

    return

label vicky_tease_scene(dream=False):
    call vicky_tease_scene_sex (dream=dream)

    return

label vicky_tease_scene_sex(dream=False):
    if store.week.time == "night":
        call process_scene_beginning (bg="bg apartment_building_night", char_tuple_array=[], dream=dream)
    else:
        call process_scene_beginning (bg="bg apartment_building_day", char_tuple_array=[], dream=dream)

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="(Вот это место!)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="(Стоп..)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="(Этот дом огромный!)")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="(Её квартира на верхнем этаже!)")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="(Было бы здорово проверить вид!)")

    call process_new_location (bg="bg apartment_hallway", dream=dream)

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="(Хорошо, я на правильном этаже)")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="(Теперь просто нужно найти правильную дверь...)")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face happy blush false", text="(Мне кажется!)")

    call fade_to_black (1)

    call process_character (n, appearance="pose behindhead face happy blush false", text="...")
    call process_character (n, appearance="pose behindhead face happy blush false", text="(Она должна быть здесь...)")

    "{i}Тук-Тук{/i}"

    call process_character (vicky, appearance="", text="Кто это?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face happy blush false", text="Это [n.say_name] [last_name].")
    call process_character (vicky, appearance="", text="Ох, мистер [last_name]!")
    call process_character (vicky, appearance="", text="Заходите же!")

    if store.week.time == "night":
        call process_new_location (bg="bg apartment_evening", dream=dream)
    else:
        call process_new_location (bg="bg apartment_daytime", dream=dream)


    call process_character (n, appearance="outfit clothesjacket")

    call process_character (vicky, appearance="", text="Ты легко нашёл мою квартиру?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Мне пришлось воспользоваться лифтом пару раз, но я нашел её!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Это большое здание!")
    call process_character (vicky, appearance="", text="Я знаю, здесь сложно ориентироваться!")
    call process_character (vicky, appearance="", text="Прошу прощения, что не встретила у двери.")
    call process_character (vicky, appearance="", text="Сейчас я заканчиваю бумажную работу.")
    call process_character (n, appearance="pose handpocket face happy blush false", text="У вас очень хорошая квартира!")
    call process_character (vicky, appearance="", text="Спасибо!")
    call process_character (vicky, appearance="", text="Она сочетается с моим стилем жизни.")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Пожалуйста, приходите ко мне в офис, и мы обсудим соглашение!")

    call static_still_ctc ("bg vicky_sit_smile")

    call process_character (vicky, appearance="", text="Устраивайтесь поудобнее.")
    call process_character (vicky, appearance="", text="{cps=40}Офис немного маленький, но-{/cps}{w=0.75}{nw}")
    call process_character (vicky, appearance="", text="...")

    call static_still_ctc ("bg vicky_sit_neutral")

    call process_character (vicky, appearance="", text="...")
    call process_character (n, appearance="blush false", text="Что-то не так?")
    call process_character (vicky, appearance="", text="Я...")
    call process_character (vicky, appearance="", text="Я просто удивлена, насколько ты молод.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Это будет проблемой?")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Ох, вовсе нет, [last_name]!")
    call process_character (n, appearance="blush false", text="Мистер [last_name]?")
    call process_character (vicky, appearance="", text="Как вы предпочитаете, чтобы вас называли?")
    call process_character (n, appearance="blush false", text="Просто [n.say_name] меня устраивает.")
    call process_character (vicky, appearance="", text="Ну тогда, [n.say_name]...")
    call process_character (vicky, appearance="", text="Давай обсудим твой партнерский контракт.")
    call process_character (n, appearance="blush false", text="Окей!")
    call process_character (vicky, appearance="", text="Я знаю, ты взволнован обсуждением этого!")
    call process_character (vicky, appearance="", text="И хорошая новость, вам не придется ничего менять.")
    call process_character (vicky, appearance="", text="Вы можете продолжать писать и делать обзоры, как и ранее!")
    call process_character (n, appearance="blush false", text="Круто!")

    call static_still_ctc ("bg vicky_sit_neutral")

    call process_character (vicky, appearance="", text="Важно помнить, что нужно соблюдать квоту.")
    call process_character (n, appearance="blush false", text="Квота?")
    call process_character (vicky, appearance="", text="Да.")
    call process_character (vicky, appearance="", text="Для того, чтобы сохранить партнерство с ReflexViz, требуется от Вас поддерживать постоянный поток контента для вашего канала.")
    call process_character (n, appearance="blush false", text="Сколько контента нужно?")

    call static_still_ctc ("bg vicky_sit_turn")

    call process_character (vicky, appearance="", text="Ну, основываясь на предыдущих партнерских отношениях...")
    call process_character (vicky, appearance="", text="Я бы сказала, что вам нужно будет делать по крайней мере два обзора каждую неделю.")
    call process_character (n, appearance="blush false", text="Две обзора в неделю?")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я знаю, такое правило.")
    call process_character (vicky, appearance="", text="Но оно того стоит.")
    call process_character (n, appearance="blush false", text="Что?")
    call process_character (vicky, appearance="", text="Вы получите более высокую долю дохода.")
    call process_character (vicky, appearance="", text="Позвольте мне объяснить...")

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Когда вы не являетесь партнером, вы получаете только половину дохода, а ReflexViz получает вторую половину.")
    call process_character (vicky, appearance="", text="Но если вы станете партнером, вы сможете сохранить восемьдесят пять процентов своего дохода!")
    call process_character (vicky, appearance="", text="ReflexViz увеличивает сумму, которую вы зарабатываете, потому что вы всегда добавляете новый контент.")
    call process_character (vicky, appearance="", text="Это в свою очередь увеличивает количество просмотров, и увеличивает их доход.")
    call process_character (vicky, appearance="", text="Так что это беспроигрышный вариант для вас, создателя контента, и ReflexViz!")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="В этом есть смысл?")
    call process_character (n, appearance="blush false", text="Хм...")
    call process_character (n, appearance="blush false", text="Вроде как...")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Может быть трудно переубедить Вас, но я здесь, чтобы помочь!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я не уверен, смогу ли я идти в ногу с такой квотой...")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я понимаю.")
    call process_character (vicky, appearance="", text="Для вас получить такой успешный канал так рано впечатляет!")
    call process_character (vicky, appearance="", text="Тем не менее, это большое давление для кого-то молодого.")
    call process_character (n, appearance="blush false", text="Да...")
    call process_character (vicky, appearance="", text="Вам нужно время, чтобы все обдумать?")
    call process_character (n, appearance="blush false", text="Я не хочу пропустить такое!")
    call process_character (vicky, appearance="", text="Не торопитесь.")
    call process_character (vicky, appearance="", text="Я могу позволить вам всё обдумать.")
    call process_character (n, appearance="blush false", text="...{p}...")

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="(Для парнишки это слишком тяжёлая ноша)")
    call process_character (vicky, appearance="", text="(Тем не менее, он нашел выгодную нишу)")
    call process_character (vicky, appearance="", text="(Мне было бы трудно пройти мимо такого, если бы я была в его ситуации!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я хотел бы это партнерство!)")
    call process_character (n, appearance="blush false", text="(Но было бы очень трудно делать два обзора в неделю!)")
    call process_character (n, appearance="blush false", text="(Будет трудно даже сделать один, когда школа начинается!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(И эта дама такая милая)")
    call process_character (n, appearance="blush false", text="(Она действительно хочет помочь мне добиться успеха!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Она очень красивая...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="(Если он пойдет на это, у меня потенциально будет огромный клиент для моего портфолио!)")
    call process_character (vicky, appearance="", text="(Не говоря уже о том, что я получу постоянную комиссию и бонус!)")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="([n.say_name] тщательно обдумывает это)")
    call process_character (vicky, appearance="", text="(Он смотрит прямо на меня)")
    call process_character (vicky, appearance="", text="...")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="(Погоди...)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Он...)")
    call process_character (vicky, appearance="", text="(Пялится на мое декольте?)")
    call process_character (n, appearance="blush false", text="(Уууу...)")
    call process_character (n, appearance="blush false", text="(Ее сиськи огромны!)")

    if "simone_scene_yoga_2" in scenes_completed:
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Они даже больше, чем сиськи мамы?)")

    call process_character (vicky, appearance="", text="...")

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="(Хорошо, что он не в должности специалиста)")
    call process_character (vicky, appearance="", text="(Его поймали бы с поличным)")
    call process_character (vicky, appearance="", text="(Отдел кадров пришёл бы в восторг от него!)")
    call process_character (vicky, appearance="", text="...")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="(Хотя он всего лишь ребенок)")
    call process_character (vicky, appearance="", text="(Грудь высокий приоритет для него сейчас)")
    call process_character (vicky, appearance="", text="...{p}...")
    call process_character (vicky, appearance="", text="(Интересно...)")
    call process_character (n, appearance="blush false", text="...")

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я могу дополнить это соглашение.")
    call process_character (n, appearance="blush false", text="Что дополнить?")
    call process_character (vicky, appearance="", text="Считайте это бонусом к Вашему контракту.")
    call process_character (n, appearance="blush false", text="Бонус?")
    call process_character (n, appearance="blush false", text="Какой бонус?")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я понимаю, что у Вас уйдёт много времени, чтобы выполнять эту квоту.")
    call process_character (vicky, appearance="", text="Но, если вы подпишите его...")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="То получите от меня личное вознаграждение.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я не понимаю, что Вы имеете в виду.")
    call process_character (vicky, appearance="", text="...")

    call static_still_ctc ("bg vicky_sit_tease")

    call process_character (n, appearance="blush false", text="!!")
    call process_character (vicky, appearance="", text="Ты понимаешь, о чем я сейчас говорю?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Вы имеете ввиду...")
    call process_character (n, appearance="blush false", text="Вы покажете мне свои сиськи?")
    call process_character (vicky, appearance="", text="Немного больше, чем Вы думает, [n.say_name].")
    call process_character (vicky, appearance="", text="Вы будете получать больше, если вы работаете больше.")
    call process_character (n, appearance="blush false", text="Так Вы хотите сказать…")
    call process_character (vicky, appearance="", text="Я говорю, что Вы получите больше бонусов, если вы достигнете квоты.")
    call process_character (n, appearance="blush false", text="Что может быть ещё лучше?")

    call static_still_ctc ("bg vicky_sit_smile")

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Я Вам покажу.")
    call process_character (n, appearance="blush false", text="...")

    call fade_to_black (1)

    call process_character (vicky, appearance="", text="...")
    call process_character (n, appearance="blush false", text="Зачем Вы повернули свой стул ко мне?")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Почувствуй это.")
    call process_character (n, appearance="blush false", text="Ч-Что?!")
    call process_character (vicky, appearance="", text="У вас есть мое разрешение.")
    call process_character (n, appearance="blush false", text="...")

    call static_still_ctc ("bg vicky_fondle_clothed_transparent")

    call process_character (n, appearance="blush false", text="О-оох!")
    call process_character (vicky, appearance="", text="Это пример бонуса, который вы можете получить, [n.say_name].")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я даже не могу обнять их своими руками!)")
    call process_character (n, appearance="blush false", text="(Ее сиськи хлюпают между пальцами!)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Возможно, это не самый этичный метод...)")
    call process_character (vicky, appearance="", text="(Но, похоже, он получает результаты!)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Его ласки тоже не так уж плохи)")
    call process_character (vicky, appearance="", text="(Смею сказать...)")
    call process_character (vicky, appearance="", text="(Он может сделать мои соски твёрдыми, если продолжит!)")
    call process_character (vicky, appearance="", text="(Я не могу позволить ему получить пирог и съесть его)")
    call process_character (vicky, appearance="", text="{i}Гмм{/i}...")
    call process_character (vicky, appearance="", text="Нам нужно доработать контракт, [n.say_name].")
    call process_character (n, appearance="blush false", text="Ах, простите!")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Значит, условия устраивают?")
    call process_character (n, appearance="blush false", text="Д-Да!")
    call process_character (vicky, appearance="", text="Я счастлива это слышать!")
    call process_character (vicky, appearance="", text="Все, что тебе осталось - подписать здесь...")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (vicky, appearance="", text="Отлично!")
    call process_character (vicky, appearance="", text="Я подпишу прямо внизу...")
    call process_character (vicky, appearance="", text="И на этом всё, [n.say_name]!")
    call process_character (vicky, appearance="", text="Ваш канал, \"Твинстикс\", официально сотрудничает с ReflexViz.HD!")
    call process_character (n, appearance="blush false", text="[sa.say_name] с ума сойдёт, когда узнает!")

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="На вашем аккаунте появится специальная эмблема с указанием партнерства.")
    call process_character (n, appearance="blush false", text="Я пойду домой и расскажу [sa.say_name] все об этом!")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Не уходите пока!")
    call process_character (vicky, appearance="", text="Позвольте мне сделать ксерокопию этого соглашения для отчета.")
    call process_character (n, appearance="blush false", text="А, понятно!")
    call process_character (n, appearance="blush false", text="Спасибо!")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я надеюсь, что вы заработаете эти бонусы!")
    call process_character (n, appearance="blush false", text="Я-я определенно буду стараться!")
    call process_character (vicky, appearance="", text="Спасибо за продуктивную встречу, мистер [last_name]!")
    call process_character (vicky, appearance="", text="Наслаждайтесь остатком дня!")

    if not dream:
        $ minigame_typing_money_earned_since_last_vicky_meeting = 0
        $ minigame_typing_times_succeeded_since_last_vicky_meeting = 0

    python:
        vicky.revistable_scenes.add("vicky_tease_scene_revisit")
        if not dream:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_big_breasts", 1)

    call process_end_of_scene ("vicky_tease_scene", char=vicky, dream=dream)

    return

label vicky_fondle_scene(dream=False):
    $ renpy.scene('screens')

    if minigame_typing_times_succeeded_since_last_vicky_meeting < 1:
        call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Хмм...")
        call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Я не думаю, что мне стоит встречаться с [vicky.say_name] пока что.")
        call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Я должен написать еще несколько обзоров.")
        $ vicky.prompted_scene = ''
        $ nate_room.start()
        return

    call vicky_fondle_scene_sex (dream=dream)

    return

label vicky_fondle_scene_sex(dream=False):
    $ renpy.scene('screens')
    if dream and not persistent.disable_dream_blur:
        show screen dream_blur

    call static_still_ctc ("bg vicky_sit_smile")

    call process_character (vicky, appearance="", text="Вы не разочаровали меня, [n.say_name]!")
    call process_character (vicky, appearance="", text="Вы с лёгкостью выполнили норму!")
    call process_character (n, appearance="blush false", text="Это не проблема!")
    call process_character (vicky, appearance="", text="Понятно!")
    call process_character (vicky, appearance="", text="Должно быть, Вы посвятили всё свободное время этому.")
    call process_character (vicky, appearance="", text="Надеюсь, Вы сможете продолжать в том же духе, как только начнется школа.")
    call process_character (n, appearance="blush false", text="Думаю, я смогу с этим справиться!")
    call process_character (n, appearance="blush false", text="Моя сестра [sa.say_name] может помогать мне тоже.")
    call process_character (vicky, appearance="", text="Кстати о твоей сестре, как она отреагировала на новости о партнерстве?")
    call process_character (n, appearance="blush false", text="Она сошла с ума!")
    call process_character (n, appearance="blush false", text="Она бегала по своей комнате и прыгала на кровати в волнении!")
    call process_character (vicky, appearance="", text="Ну вы заслуживаете этого!")
    call process_character (vicky, appearance="", text="Вы стабильно увеличиваете аудиторию.")
    call process_character (n, appearance="blush false", text="Это очень волнующе для нас!")
    call process_character (vicky, appearance="", text="Так что, я уверена, вы пришли ко мне по поводу бонуса.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Мне было любопытно, что это будет...")
    call process_character (vicky, appearance="", text="Как насчет моей груди, снова?")
    call process_character (vicky, appearance="", text="Это приемлемо?")
    call process_character (n, appearance="blush false", text="Д-Да!")

    call static_still_ctc ("bg vicky_fondle_clothed_transparent")

    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (vicky, appearance="", text="Вы можете трогать их в течение длительного периода.")
    call process_character (vicky, appearance="", text="Вы заслужили это право.")
    call process_character (n, appearance="blush false", text="М-мило...")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Вы раньше видели такую большую грудь?")

    if has_seen_big_breasts_other_than_vicky():
        call process_character (n, appearance="blush false", text="Вообще-то...")
        call process_character (n, appearance="blush false", text="Я видел большие сиськи раньше.")
        call process_character (vicky, appearance="", text="Такие же большие, как у меня?")
        call process_character (n, appearance="blush false", text="Д-Да.")
        call process_character (vicky, appearance="", text="Похоже, у вас есть небольшой опыт.")
        call process_character (vicky, appearance="", text="Вы разбираетесь в подобных вещах?")
        call process_character (n, appearance="blush false", text="Хм?")
    else:
        call process_character (n, appearance="blush false", text="Я никогда не видел таких больших сисек так близко.")
        call process_character (vicky, appearance="", text="Вам повезет, если вы снова увидите такую большую грудь.")

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Моя грудь плотно облегает эту блузку.")
    call process_character (vicky, appearance="", text="Не могли бы вы снять её для меня?")
    call process_character (n, appearance="blush false", text="Снять?")
    call process_character (vicky, appearance="", text="К концу дня им нужна передышка.")
    call process_character (vicky, appearance="", text="Будьте джентльменом и помогите мне, [n.say_name]?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я... я могу это сделать.")

    call static_still_ctc ("bg vicky_fondle_exposed_transparent")

    call process_character (vicky, appearance="", text="Ах...")
    call process_character (vicky, appearance="", text="Спасибо, [n.say_name].")
    call process_character (vicky, appearance="", text="Вы настоящий джентльмен!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(В-вау...)")
    call process_character (vicky, appearance="", text="Они тяжелые, не правда ли?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Д-Да...")
    call process_character (n, appearance="blush false", text="Они потрясающие!")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="([n.say_name] вполне опытен)")
    call process_character (vicky, appearance="", text="(Он держит мою грудь, как будто он делает осмотр)")
    call process_character (vicky, appearance="", text="(Не могу сказать, что удивлена)")
    call process_character (vicky, appearance="", text="(Все молодые мужчины мечтают об этом)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я не могу сказать, знает ли он, что он делает, или нет, но...)")
    call process_character (vicky, appearance="", text="(У него прекрасный способ двигать руками...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="([vicky.say_name] позволяет мне трогать ее сиськи столько, сколько я хочу!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Интересно, нравится ли ей это?)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Это действительно сюрприз...)")
    call process_character (vicky, appearance="", text="(Его ласки меня возбуждают!)")
    call process_character (vicky, appearance="", text="(Я должна сохранять самообладание...)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Если я продолжу ему позволять это делать, то моя юбку станет мокрой от...)")
    call process_character (vicky, appearance="", text="Мм!")
    call process_character (n, appearance="blush false", text="Вы что-то сказали, [vicky.say_name]?")
    call process_character (vicky, appearance="", text="М-Мой!")
    call process_character (vicky, appearance="", text="Посмотрите на время!")
    call process_character (vicky, appearance="", text="У меня назначена встреча через несколько минут.")
    call process_character (vicky, appearance="", text="Мы должны закончить нашу сессию на сегодня.")
    call process_character (n, appearance="blush false", text="Ладно...")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Отличная работа над вашими отзывами!")
    call process_character (vicky, appearance="", text="Так держать!")
    call process_character (n, appearance="blush false", text="С-спасибо!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я могу прийти снова?")
    call process_character (vicky, appearance="", text="Почему бы и нет.")
    call process_character (vicky, appearance="", text="Вообще-то, у меня есть предложение для Вас.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="Если превысите квоту обзоров...")

    call static_still_ctc ("bg vicky_sit_tease")

    call process_character (vicky, appearance="", text="Тогда Вы получите лучший бонус в следующий раз.")
    call process_character (vicky, appearance="", text="Как Вам такое предложение?")
    call process_character (n, appearance="blush false", text="Звучит неплохо!")
    call process_character (vicky, appearance="", text="Тогда до скорой встречи!")

    if not dream:
        $ minigame_typing_money_earned_since_last_vicky_meeting = 0
        $ minigame_typing_times_succeeded_since_last_vicky_meeting = 0

    python:
        vicky.revistable_scenes.add("vicky_fondle_scene_revisit")
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_big_breasts", 1)

    call process_end_of_scene ("vicky_fondle_scene", char=vicky, dream=dream)

    return

label vicky_titjob_scene(dream=False):
    call vicky_titjob_scene_sex (dream=dream)

    return

label vicky_titjob_scene_sex(dream=False):
    call process_scene_beginning (bg="bg nate_room_daytime", dream=dream)

    $ vicky_titfuck_xray_style = "normal"

    if has_fucked_everyone_in_home:
        $ n.outfit = "nudesoft"
    else:
        $ n.outfit = "underwear"

    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="Похоже, еще один отличный летний день!")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear pose behindhead face happy blush false", text="О!")
    call process_character (n, appearance="outfit underwear pose behindhead face happy blush false", text="Я получил сообщение от Вики!")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="\"[n.say_name], я хотела бы поговорить с Вами о вашем канале..\"")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="\"Я считаю, что это поможет увеличить количество ваших зрителей и подписчиков.\"")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="\"Пожалуйста, приходите ко мне как можно скорее.\"")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="Хм...")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="Интересно, о чем она хочет поговорить?")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="Если это поможет ускорить рост нашего канала, то было бы здорово!")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="Я должен навестить ее как можно скорее!")

    $ no_bust_art = False
    $ clear_characters()
    with Dissolve(0.5)
    window hide
    with Dissolve(0.5)

    call fade_to_black (0.5)
    pause 0.5
    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Приятно видеть тебя снова, [n.say_name].")
    call process_character (vicky, appearance="", text="Как поживаете?")
    call process_character (n, appearance="blush false", text="Очень хорошо!")
    call process_character (n, appearance="blush false", text="А вы?")
    call process_character (vicky, appearance="", text="Хорошо, спасибо.")
    call process_character (n, appearance="blush false", text="Вы хотели поговорить со мной о моем канале?")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Да, это так.")
    call process_character (vicky, appearance="", text="Я думаю, что ваш канал находится на перекрестке, [n.say_name].")
    call process_character (n, appearance="blush false", text="Перекрестке?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Это плохо?")
    call process_character (vicky, appearance="", text="Необязательно.")
    call process_character (vicky, appearance="", text="На самом деле это может быть очень хорошо, в зависимости от того, как к этому относиться.")
    call process_character (n, appearance="blush false", text="Что Вы имеете в виду?")

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Согласно аналитике канала, ваша аудитория быстро растет.")
    call process_character (vicky, appearance="", text="И я вижу тенденцию увеличения аудитории ваших зрителей.")
    call process_character (n, appearance="blush false", text="Что это?")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Большинству ваших подписчиков нравятся многие из тех же вещей, которые вы делаете.")
    call process_character (vicky, appearance="", text="Видеоигры, фильмы...")
    call process_character (vicky, appearance="", text="Но я заметила, что им также нравится другая категория.")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Порнография.")
    call process_character (n, appearance="blush false", text="Порнография?")

    if "sam_scene_vaginal_revisit" in scenes_completed:
        show bg vicky_sit_neutral
        with Dissolve(0.5)

        call process_character (vicky, appearance="", text="Ты не знаешь, что такое порно?")
        call process_character (n, appearance="blush false", text="Я, вроде как...")
        call process_character (vicky, appearance="blush false", text="Я думала, после того секс-стрима с твоей сестрой, ты много об этом узнал.")
        call process_character (n, appearance="blush false", text="Вы видели этот стрим?!")

        show bg vicky_sit_smile
        with Dissolve(0.5)

        call process_character (vicky, appearance="", text="В конце концов, я часть вашего партнерства.")
        call process_character (vicky, appearance="", text="Поэтому я слежу за всем, что вы делаете, чтобы увидеть тенденции.")
        call process_character (n, appearance="blush false", text="О-О, да...")
        call process_character (n, appearance="blush false", text="Правда.")

        show bg vicky_sit_neutral
        with Dissolve(0.5)

        call process_character (vicky, appearance="", text="Что ты и твоя сестра [sa.say_name] делали...")
        call process_character (vicky, appearance="", text="Это считается порнографией или порно.")
        call process_character (n, appearance="blush false", text="Это?")
        call process_character (vicky, appearance="", text="Порно - эротический акт с целью вызвать сексуальное возбуждение у зрителя.")

        show bg vicky_sit_smile
        with Dissolve(0.5)

        call process_character (vicky, appearance="", text="Это вроде того, когда ты вставлял свой пенис во влагалище сестры для удовольствия, пока идёт трансляция или запись…")
        call process_character (n, appearance="blush false", text="Э-это порно?")
        call process_character (vicky, appearance="", text="Правильно.")
        call process_character (vicky, appearance="", text="Что возвращает меня к тому, что я говорила о том, что ваш канал на перекрестке.")
    else:
        show bg vicky_sit_neutral
        with Dissolve(0.5)

        call process_character (vicky, appearance="", text="Ты не знаешь, что такое порно?")
        call process_character (n, appearance="blush false", text="Я, вроде как...")

        show bg vicky_sit_turn
        with Dissolve(0.5)

        call process_character (vicky, appearance="", text="Порно считается эротическим актом с целью вызвать сексуальное возбуждение у зрителя.")
        call process_character (vicky, appearance="", text="Например...")
        call process_character (vicky, appearance="", text="Скажем, есть видео, где женщина занимается оральным сексом с мужчиной в эротической манере...")
        call process_character (vicky, appearance="", text="Или, возможно, мужчина вставляет свой пенис во влагалище женщины исключительно для возбуждения.")

        show bg vicky_sit_neutral
        with Dissolve(0.5)

        call process_character (vicky, appearance="", text="Если что-то подобное распространяется для всеобщего обозрения, это считается порнографией.")
        call process_character (n, appearance="blush false", text="!")
        call process_character (n, appearance="blush false", text="Это порно?")

        show bg vicky_sit_smile
        with Dissolve(0.5)

        call process_character (vicky, appearance="", text="Похоже, ты знаком с сексуальной частью, основываясь на твоей реакции.")
        call process_character (n, appearance="blush false", text="...")
        call process_character (vicky, appearance="", text="Некоторые из видеоигр и шоу, которые ты рассматриваешь, содержат сексуальные темы, но не порнографию.")
        call process_character (vicky, appearance="", text="В качестве побочного эффекта многие из ваших зрителей в конечном итоге ищут порно на основе шоу и видеоигр, которые вы обозревали.")
        call process_character (n, appearance="blush false", text="О-Ох...")
        call process_character (n, appearance="blush false", text="Понятно.")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Так мои подписчики смотрят много порно?")
        call process_character (vicky, appearance="", text="Что возвращает меня к тому, что я говорила о том, что ваш канал на перекрестке.")


    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Как ты знаешь, очень важно создавать контент вокруг того, что нравится вашей аудитории.")
    call process_character (vicky, appearance="", text="Если ты можешь извлечь из этого выгоду, вам гарантирован успех.")
    call process_character (n, appearance="blush false", text="Имеет смысл.")

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Основываясь на этих данных, у меня есть предложение для вашего канала, которое я бы настоятельно рассмотрела...")
    call process_character (n, appearance="blush false", text="Да?")
    call process_character (n, appearance="blush false", text="Что это?")
    call process_character (vicky, appearance="", text="Помимо написания обычных отзывов, которыми ты занимаешься и сейчас...")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я рекомендую тебе также ознакомиться с порнографическими материалами.")
    call process_character (n, appearance="blush false", text="Вы хотите, чтобы я смотрел порно?")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Не все время конечно.")
    call process_character (vicky, appearance="", text="Но ты должен добавить порно обзоры в твоё расписание.")
    call process_character (vicky, appearance="", text="Таким образом, ты задействуешь главный интерес вашей аудитории!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Хм...")

    if "sam_scene_vaginal_revisit" in scenes_completed:
        call process_character (vicky, appearance="", text="Ты знаешь, сколько раз делились люди вашим секс-стримом с сестрой?")
        call process_character (n, appearance="blush false", text="Я-я еще не проверял...")

        show bg vicky_sit_smile
        with Dissolve(0.5)

        call process_character (vicky, appearance="", text="Тысячи раз им делились!")
        call process_character (n, appearance="blush false", text="Вау, так много?")
        call process_character (vicky, appearance="", text="Секс продаёт всё, [n.say_name]...")
        call process_character (vicky, appearance="", text="Это всегда было так.")
        call process_character (vicky, appearance="", text="Плюс аспект, что вы брат и сестра увеличивает привлекательность еще сильнее!")
        call process_character (n, appearance="blush false", text="Неужели?")
        call process_character (vicky, appearance="", text="Безусловно!")
        call process_character (vicky, appearance="", text="Люди всегда ищут что-то уникальное в порно.")
        call process_character (vicky, appearance="", text="Моя предыдущая работа доказала это.")
    else:

        show bg vicky_sit_smile
        with Dissolve(0.5)

        call process_character (vicky, appearance="", text="Секс продаёт всё, [n.say_name]...")
        call process_character (vicky, appearance="", text="Это всегда было так.")
        call process_character (vicky, appearance="", text="Моя предыдущая работа доказала это.")

    call process_character (n, appearance="blush false", text="Ваша предыдущая работа?")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Прежде чем я был нанята в качестве партнёра ReflexViz.HD, я была директором по маркетингу порнографической кинокомпании.")
    call process_character (n, appearance="blush false", text="Правда?")

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Моя роль заключалась в том, чтобы увеличить продажи фильмов для взрослых, поэтому мне пришлось многое узнать о спросе на рынке.")
    call process_character (vicky, appearance="", text="Это был изнурительный график.")
    call process_character (vicky, appearance="", text="В конце концов, постоянное давление продавать, продавать, продавать стало слишком стрессовым.")
    call process_character (vicky, appearance="", text="Поэтому я переключилась на такую карьеру, которая более спокойная и представительная.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Значит, Вы много знаете о порно?")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я понимаю состояние рынка.")
    call process_character (vicky, appearance="", text="Но я знаю немного о производственном процессе.")
    call process_character (vicky, appearance="", text="В конце концов, это была киностудия.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Вы когда-нибудь снимались в тех фильмах?")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Ахаха.")
    call process_character (vicky, appearance="", text="Я бы солгала, если бы сказал, что продюсеры не просили меня десятки раз сняться в одном из их фильмов.")
    call process_character (vicky, appearance="", text="Они были одержимы моими \"бидонами\", как они их называли, и надеялись, что однажды я соглашусь на съемку.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Но Вы никогда этого не делали?")

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Мне просто было не по себе заниматься этим с каким-то случайным человеком.")
    call process_character (vicky, appearance="", text="Я бы предпочла сначала узнать и полюбить человека, чтобы было с ним комфортно.")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Ты тоже так считаешь, [n.say_name]?")

    menu:
        "Да.":
            call add_boldness (0, tag="vicky_titjob_like_a_lot", force_no_popup=True)
            show bg vicky_sit_smile
            with Dissolve(0.5)

            call process_character (vicky, appearance="", text="Звучит неплохо.")
            call process_character (vicky, appearance="", text="Отношения важны как для профессиональной, так и для личной жизни.")
            call process_character (vicky, appearance="", text="Вот почему мы с тобой так хорошо работаем вместе.")
        "Вы мне нравитесь, Викки!":
            call add_boldness (1, tag="vicky_titjob_like_a_lot")
            show bg vicky_sit_smile
            with Dissolve(0.5)

            call process_character (vicky, appearance="", text="Ха, ты мне тоже нравишься, [n.say_name].")
            call process_character (vicky, appearance="", text="Вообще-то, ты мой любимый клиент.")
            call process_character (n, appearance="blush false", text="Я?")
            call process_character (vicky, appearance="", text="Ты однозначно самый младший...")
            call process_character (vicky, appearance="", text="Но держишься, как профессионал.")
            call process_character (vicky, appearance="", text="И с Вами приятно общаться.")
            call process_character (vicky, appearance="", text="Ты заставляешь меня чувствовать себя хорошо на моей работе.")

    call process_character (n, appearance="blush false", text="Здорово, что Вы помогаете мне, Вики!")
    call process_character (vicky, appearance="", text="Я чувствую, что мы вместе продолжим завоёвывать большой успех!")
    call process_character (vicky, appearance="", text="Вы знаете...")
    call process_character (vicky, appearance="", text="Если бы ты был одним из актеров в той студии, я бы подумала о съемках.")
    call process_character (n, appearance="blush false", text="Да?")
    call process_character (vicky, appearance="", text="Мы… {w=1.0}могли бы выполнить одну из сцен, которую они запланировали для меня, если хочешь.")
    call process_character (n, appearance="blush false", text="О-одну из сцен?")
    call process_character (vicky, appearance="", text="Да, я помню, как продюсеры рассказывали мне об этом.")
    call process_character (vicky, appearance="", text="Это включает в себя две большие штуки, которые тебе нравятся.")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (n, appearance="blush false", text="Д-думаю, я понимаю, что Вы имеете в виду...")

    call static_still_ctc ("bg vicky_sit_tease")

    call process_character (vicky, appearance="", text="Я знаю, ты справишься...")
    call process_character (n, appearance="blush false", text="Так как мы сделаем это?")
    call process_character (vicky, appearance="", text="Сначала я должна встать на колени.")
    call process_character (vicky, appearance="", text="И ты должен снять свои штаны.")
    call process_character (n, appearance="blush false", text="И мое нижнее белье тоже?")
    call process_character (vicky, appearance="", text="О, да.")
    call process_character (vicky, appearance="", text="Просто положи на стул.")

    call fade_to_black (1)

    call process_character (vicky, appearance="", text="...{p}...")
    call process_character (vicky, appearance="", text="([n.say_name] возводился уже)")
    call process_character (vicky, appearance="", text="(Его член такой чистый...)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Но выглядит готовым испачкаться!)")
    call process_character (n, appearance="blush false", text="Что Вы хотите, чтобы я сделал сейчас?")
    call process_character (vicky, appearance="", text="Видишь место между моими грудями, мое декольте?")
    call process_character (n, appearance="blush false", text="Д-Да...")
    call process_character (vicky, appearance="", text="Вот куда пойдет твой пенис.")
    call process_character (vicky, appearance="", text="Ты готов?")
    call process_character (n, appearance="blush false", text="...{p}...")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg vicky_titfuck_sideview")

    show screen vicky_titfuck_sideview_xray

    call process_character (n, appearance="blush false", text="Хаах!")
    call process_character (vicky, appearance="", text="Это было легко, не так ли?")
    call process_character (n, appearance="blush false", text="Мм, Мм!")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я чувствую, как его член трется между моими сиськами...)")
    call process_character (vicky, appearance="", text="(Бьюсь об заклад, что он чувствует себя удивительно)")
    call process_character (vicky, appearance="", text="(Возможно, как между двумя теплыми подушками)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(О боже мой!)")

    if "kira_scene_8" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Это очень напоминает мне, когда [k.say_name] делала это со мной!)")
        call process_character (n, appearance="blush false", text="(Это всегда так здорово!)")
    elif "simone_scene_titfuck" in scenes_completed or "sam_simone_threesome_scene" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Это так напоминает мне, когда мама делала это со мной!)")
        call process_character (n, appearance="blush false", text="(Это всегда так здорово!)")
    else:
        call process_character (n, appearance="", text="(Я никогда бы не подумал сделать это!)")
        call process_character (n, appearance="", text="(Я рад, что узнал, хотя бы!)")
        call process_character (n, appearance="", text="(Положить мой пенис между сиськами это здорово!)")


    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я думаю, что предыдущая рабочая среда сказалась на мне)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Когда я была там, я думала, что поведение офиса было настолько непрофессиональным)")
    call process_character (vicky, appearance="", text="(Женщины щупают друг друга, мужчины хватают за промежности секретарш...)")
    call process_character (vicky, appearance="", text="(И теперь я здесь, в моем личном кабинете, давая ребенку персональный сиськотрах!)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я стала более извращённой, чем они!)")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (vicky, appearance="", text="Ты устал?")
    call process_character (vicky, appearance="", text="Позволь помочь...")

    hide screen vicky_titfuck_mash_xray
    hide screen vicky_titfuck_mash_cum_xray
    hide screen vicky_titfuck_sideview_xray

    window hide

    if vicky_titfuck_xray_style == "normal":
        show bg vicky_titfuck_nocum
    else:
        show bg vicky_titfuck_nocum_xray

    with Dissolve(0.5)
    show screen vicky_titfuck_mash_xray
    pause

    call process_character (vicky, appearance="", text="Вот так-то!")
    call process_character (n, appearance="blush false", text="Хрм!")
    call process_character (vicky, appearance="", text="Я могу подталкивать свою грудь вот так...")
    call process_character (vicky, appearance="", text="Теперь твой член застрял на месте!")
    call process_character (n, appearance="blush false", text="Ах!")
    call process_character (vicky, appearance="", text="Это хорошо, не правда ли?")
    call process_character (n, appearance="blush false", text="Д-Да...{w=1.0}...")
    call process_character (vicky, appearance="", text="Хорошая идея, поддерживать грудь.")
    call process_character (vicky, appearance="", text="Теперь я могу легко двигать ими вокруг твоего члена.")
    call process_character (n, appearance="blush false", text="Ох, ах!")
    call process_character (vicky, appearance="", text="(Крайняя плоть [n.say_name] движется вперед и назад)")
    call process_character (vicky, appearance="", text="(Его возбуждение должно быть огромным!)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(У этого ребенка больше мужества, чем я когда-либо представляла...)")

    if "sam_scene_vaginal_revisit" in scenes_completed:
        call process_character (vicky, appearance="", text="(Хотя я должна была это понять, увидев стрим со его сестрой)")
        call process_character (vicky, appearance="", text="(Я никогда не смогу трахаться перед аудиторией, даже в интернете!)")
        call process_character (vicky, appearance="", text="(Назовите это догадкой, но я думаю, что [n.say_name] и его сестра будут первопроходцами...)")
    else:

        call process_character (vicky, appearance="", text="(Это пригодится ему)")
        call process_character (vicky, appearance="", text="...")
        call process_character (vicky, appearance="", text="(Назовите это догадкой, но я думаю, что [n.say_name] станет первопроходцем...)")

    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Она двигает своими сиськами взад и вперед по моему пенису...)")
    call process_character (n, appearance="blush false", text="(Это потрясающие ощущения!)")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ох, ох!")
    call process_character (vicky, appearance="", text="Ты двигаешься, [n.say_name].")
    call process_character (vicky, appearance="", text="Как ты себя чувствуешь?")
    call process_character (n, appearance="blush false", text="Ах, ааах...")
    call process_character (n, appearance="blush false", text="В Вики!")
    call process_character (n, appearance="blush false", text="Мне кажется, что я собираюсь...")


    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    hide screen vicky_titfuck_mash_xray
    hide screen vicky_titfuck_mash_cum_xray
    hide screen vicky_titfuck_sideview_xray

    window hide

    if vicky_titfuck_xray_style == "normal":
        show bg vicky_titfuck_cum
    elif vicky_titfuck_xray_style == "penisonly":
        show bg vicky_titfuck_cum_penisonly
    else:
        show bg vicky_titfuck_cum_xray

    with Dissolve(0.5)
    pause 0.75
    show screen vicky_titfuck_mash_cum_xray
    pause

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Я думаю, что знаю, что случилось, [n.say_name]...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="В моем декольте есть кое-что еще, кроме твоего пениса.")
    call process_character (vicky, appearance="", text="Я уверена.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Д-Да, скорее всего так и есть...")
    call process_character (vicky, appearance="", text="Ммм...")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Может, нам стоит взглянуть?")

    hide screen vicky_titfuck_mash_xray
    hide screen vicky_titfuck_mash_cum_xray
    hide screen vicky_titfuck_sideview_xray
    call static_still_ctc ("bg vicky_titfuck_aftercum")

    call process_character (vicky, appearance="", text="О, боже!")
    call process_character (vicky, appearance="", text="Я не ожидала, что там будет так много!")
    call process_character (n, appearance="blush false", text="Э-это очень много...")
    call process_character (vicky, appearance="", text="Глядя на это, я рада, что ты кончил в мое декольте.")
    call process_character (vicky, appearance="", text="Это был бы беспорядок, если бы мы сделали по-другому!")
    call process_character (n, appearance="blush false", text="Я так хорошо себя чувствовал, Вики.")
    call process_character (n, appearance="blush false", text="Прости, что так много вышло...")
    call process_character (vicky, appearance="", text="Не беспокойся, [n.say_name].")
    call process_character (vicky, appearance="", text="Я рада, что сперма не попала на мой деловой костюм!")
    call process_character (vicky, appearance="", text="Мне пришлось бы заплатить целое состояние, чтобы его почистить.")
    call process_character (vicky, appearance="", text="И мне бы пришлось объяснять эти белые пятна...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="Я думаю, что на этом наша встреча на сегодня завершается, [n.say_name].")
    call process_character (vicky, appearance="", text="Помни, что я говорила о вашем канале.")
    call process_character (n, appearance="blush false", text="О порно-обзорах?")
    call process_character (vicky, appearance="", text="Я бы занялся этим как можно скорее.")
    call process_character (vicky, appearance="", text="Вы легко получите несколько сотен новых подписчиков, если начнешь прямо сейчас!")
    call process_character (n, appearance="blush false", text="Да?")
    call process_character (vicky, appearance="", text="Оседлай гребень волны, [n.say_name], как говорится.")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Почему бы тебе не рассмотреть порно с большой грудью в качестве темы?")
    call process_character (vicky, appearance="", text="Это идеальная отправная точка для тебя!")
    call process_character (n, appearance="blush false", text="...")


    python:
        vicky.revistable_scenes.add("vicky_titjob_scene_revisit")

        if not dream:
            minigame_typing_money_earned_since_last_vicky_meeting = 0
            minigame_typing_times_succeeded_since_last_vicky_meeting = 0
            
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_big_breasts", 1)
            stats.add_stat("times_had_paizuri", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene ("vicky_titjob_scene", char=vicky, dream=dream)

    return

label vicky_titjob_scene_revisit:
    $ no_bust_art = False

    if "vicky_titjob_scene_revisit" in scenes_completed:
        call vicky_titjob_scene_revisit_2nd_time
    else:
        call vicky_titjob_scene_revisit_1st_time

    return

label vicky_titjob_scene_revisit_1st_time:
    $ vicky_titfuck_xray_style = "normal"

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Ты предан всему этому!")
    call process_character (vicky, appearance="", text="Но я думаю, это показывает, насколько тебе понравилось то, что я делала раньше!")

    $ play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)
    call static_still_ctc ("bg vicky_sit_tease")

    call process_character (vicky, appearance="", text="Хорошо, что я сегодня без лифчика...")

    call static_still_ctc ("bg vicky_titfuck_sideview")

    show screen vicky_titfuck_sideview_xray

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Это хороший отдых от напряженного дня, который у меня был.")
    call process_character (vicky, appearance="", text="Я надеялась, что ты зайдешь.")
    call process_character (n, appearance="blush false", text="Мм, да?")
    call process_character (vicky, appearance="", text="Это позволяет мне расслабиться, как бы странно это ни звучало.")
    call process_character (vicky, appearance="", text="Это позволяет мне очистить голову.")
    call process_character (n, appearance="blush false", text="Э-это хорошо.")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (vicky, appearance="", text="Никогда не знала, что будет столько бумажной работы!")
    call process_character (vicky, appearance="", text="Можно подумать, в такой компания, как ReflexViz.HD, не придется об этом беспокоиться.")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="К счастью, большинство документов хранятся на компьютере.")
    call process_character (n, appearance="blush false", text="Мм, Мм!")
    call process_character (vicky, appearance="", text="Надеюсь, в будущем тебе не придется делать слишком много бумажной работы.")
    call process_character (vicky, appearance="", text="Даже мне сложно все это организовать!")
    call process_character (n, appearance="blush false", text="Я-я надеюсь, что нет...")
    call process_character (n, appearance="blush false", text="Домашние задания достаточно тяжёлые!")
    call process_character (vicky, appearance="", text="Вот именно!")
    call process_character (vicky, appearance="", text="Я все время забываю, что ты еще в школе.")

    $ renpy.scene('screens')

    window hide

    if vicky_titfuck_xray_style == "normal":
        show bg vicky_titfuck_nocum
    else:
        show bg vicky_titfuck_nocum_xray

    with Dissolve(0.5)
    show screen vicky_titfuck_mash_xray
    pause

    call process_character (vicky, appearance="", text="Знаешь, иногда я могу жаловаться, что делаю всю эту работу.")
    call process_character (vicky, appearance="", text="Но я бы взяла это на себя в школе в любой день.")
    call process_character (n, appearance="blush false", text="Ты бы хотела?")
    call process_character (n, appearance="blush false", text="Оох!")
    call process_character (vicky, appearance="", text="Определенно.")
    call process_character (vicky, appearance="", text="В школе тебе предстоит заниматься сочинениями, тестами, школьными постановками...")
    call process_character (vicky, appearance="", text="Намного лучше, когда ты закончишь школу и занимаешься своим делом.")
    call process_character (n, appearance="blush false", text="Это будет просто замечательно.")
    call process_character (vicky, appearance="", text="Ты уже закладываешь основу для своего будущего!")
    call process_character (vicky, appearance="", text="Ты начал зарабатывать раньше, чем большинство людей!")
    call process_character (n, appearance="blush false", text="Ах!")
    call process_character (n, appearance="blush false", text="Я-я думаю, что вы правы.")
    call process_character (vicky, appearance="", text="Для меня школа пролетела быстро.")
    call process_character (vicky, appearance="", text="Ты закончишь её раньше, чем успеешь оглянуться!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Мне жаль, что мне придётся ходить в школу, а так я мог бы просто работать на своем канале с [sa.say_name]!)")
    call process_character (n, appearance="blush false", text="(Я мог бы писать обзоры весь день и делать такие вещи с Вики!)")
    call process_character (n, appearance="blush false", text="(Это было бы так здорово!)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Интересно, смогу ли я выбить стипендию для [n.say_name])")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(ReflexViz.HD предлагают их?)")
    call process_character (vicky, appearance="", text="(Они определенно должны!)")
    call process_character (vicky, appearance="", text="(Мне придется отправить записку высшему руководству и спросить их об этом)")
    call process_character (n, appearance="blush false", text="Ааах, ах, ах!")
    call process_character (vicky, appearance="", text="Если ты собираетесь кончить, просто продолжай делать то, что вы делаешь!")
    call process_character (vicky, appearance="", text="Я должна ходить по магазинам после работы, так что я хотела бы избежать пятен спермы на моем костюме!")
    call process_character (n, appearance="blush false", text="Хннг!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    $ renpy.scene('screens')

    window hide

    if vicky_titfuck_xray_style == "normal":
        show bg vicky_titfuck_cum
    elif vicky_titfuck_xray_style == "penisonly":
        show bg vicky_titfuck_cum_penisonly
    else:
        show bg vicky_titfuck_cum_xray

    with Dissolve(0.5)
    pause 0.75
    show screen vicky_titfuck_mash_cum_xray
    pause

    call process_character (vicky, appearance="", text="Сожми мои сиськи покрепче!")
    call process_character (vicky, appearance="", text="Я пытаюсь удержать сперму от капания на ковер!")
    call process_character (n, appearance="blush false", text="Ох...")
    call process_character (vicky, appearance="", text="Тебе удалось это?")
    call process_character (n, appearance="blush false", text="Я... я думаю, что да...")

    $ renpy.scene('screens')
    call static_still_ctc ("bg vicky_titfuck_aftercum")

    call process_character (vicky, appearance="", text="Похоже, что ты это сделал!")
    call process_character (vicky, appearance="", text="Некоторые капли даже попали на нижнюю часть моей груди!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="Можешь передать мне эти салфетки со стола?")
    call process_character (vicky, appearance="", text="Я не хочу двигаться слишком много, и заставить твою сперму соскользнуть.")


    call vicky_titjob_scene_revisit_end

    return

label vicky_titjob_scene_revisit_2nd_time:
    $ vicky_titfuck_xray_style = "normal"
    $ play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)
    $ no_bust_art = True
    $ renpy.scene('screens')

    window hide
    show bg vicky_titfuck_nocum
    with Dissolve(0.5)
    show screen vicky_titfuck_mash_xray
    pause

    call process_character (vicky, appearance="", text="Обзоры все еще идут хорошо?")
    call process_character (n, appearance="blush false", text="Да, именно так...")
    call process_character (vicky, appearance="", text="Это здорово.")
    call process_character (vicky, appearance="", text="Кажется, у тебя никогда не заканчивается материал для критики!")
    call process_character (n, appearance="blush false", text="Ну, есть много видеоигр, в которые я до сих пор не играл, которые вышли пару лет назад.")
    call process_character (vicky, appearance="", text="О, так у тебя есть значительное отставание?")
    call process_character (n, appearance="blush false", text="И-их много.")
    call process_character (n, appearance="blush false", text="Мм!")
    call process_character (n, appearance="blush false", text="Моя сестра помогает, играя в них тоже.")
    call process_character (n, appearance="blush false", text="Так мы сможем пройти их быстрее.")
    call process_character (vicky, appearance="", text="Очень умно.")
    call process_character (vicky, appearance="", text="Вы чередуетесь в играх.")
    call process_character (n, appearance="blush false", text="Д-Да.")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я удивлена, что его сестра и он не участвовали в турнирах по видеоиграм)")
    call process_character (vicky, appearance="", text="(Похоже, что они мастера в этом!)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я никогда не могла играть в видеоигры, даже когда была моложе)")
    call process_character (vicky, appearance="", text="(Игры так сильно изменились за эти годы...)")
    call process_character (vicky, appearance="", text="(По крайней мере, я знаю, как играть в пасьянс и покер!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я должна позволить [sa.say_name] поговорить с [vicky.say_name] какое-то время)")
    call process_character (n, appearance="blush false", text="(Она, вероятно, задаст гораздо больше технических вопросов, чем я!)")
    call process_character (n, appearance="blush false", text="([sa.say_name] любит все эти статистические штуки!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Бьюсь об заклад [sa.say_name] будет спрашивать о специальных значках и символах, которые мы могли бы получить для нашего канала...)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!")
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    $ renpy.scene('screens')

    window hide

    if vicky_titfuck_xray_style == "normal":
        show bg vicky_titfuck_cum
    elif vicky_titfuck_xray_style == "penisonly":
        show bg vicky_titfuck_cum_penisonly
    else:
        show bg vicky_titfuck_cum_xray

    with Dissolve(0.5)
    pause 0.75
    show screen vicky_titfuck_mash_cum_xray
    pause

    call process_character (n, appearance="blush false", text="Ах...")
    call process_character (vicky, appearance="", text="Я почти не была готова к этому!")
    call process_character (vicky, appearance="", text="Хорошо, что я смогла засунуть свою грудь тебе под член!")
    call process_character (n, appearance="blush false", text="{i}Фьюю.{/i}..")

    $ renpy.scene('screens')
    call static_still_ctc ("bg vicky_titfuck_aftercum")

    call process_character (vicky, appearance="", text="Учитывая, насколько здесь всё грязно...")
    call process_character (vicky, appearance="", text="Никто никогда не узнает, что мы делаем это в моем офисе!")
    call process_character (vicky, appearance="", text="Хотя я распыляю освежитель воздуха здесь после твоего ухода, на всякий случай...")


    call vicky_titjob_scene_revisit_end

    return

label vicky_titjob_scene_revisit_end:

    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_big_breasts", 1)
        stats.add_stat("times_had_paizuri", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene ("vicky_titjob_scene_revisit", char=vicky, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label vicky_scene_blowjob(dream=False):
    call vicky_scene_blowjob_sex (dream=dream)

    return

label vicky_scene_blowjob_sex(dream=False):
    call process_scene_beginning (bg="bg nate_room_daytime", dream=dream)
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="(Последнее видео получает огромное количество просмотров!)")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="([vicky.say_name] была абсолютно права насчет добавления порно обзоров на канал!)")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="(Она действительно знает свое дело!)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face happy blush false", text="(Что напоминает мне, что я должен нанести ей визит!)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face happy blush false", text="(Может быть, у нее будет еще одно предложение для канала!)")

    call fade_to_black (1)


    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Посмотрите-ка, кто пришел!")
    call process_character (vicky, appearance="", text="И ты широко улыбаешься!")
    call process_character (n, appearance="blush false", text="Твинстикс разрывается от подписчиков!")
    call process_character (vicky, appearance="", text="Я наблюдала за вашим ростом.")
    call process_character (vicky, appearance="", text="Ваш канал превзошел даже мои лучшие оценки!")
    call process_character (n, appearance="blush false", text="Если бы не Вы [vicky.say_name], у Твинстикс не было бы столько же подписчиков, сколько сейчас!")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я просто дала совет, что нужно улучшить и в каком направлении двигаться.")
    call process_character (vicky, appearance="", text="Это ты принял совет и превратил его в нечто.")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="И это именно ты сделал.")
    call process_character (vicky, appearance="", text="Ты загрузил больше отзывов, расширил свою трансляцию...")
    call process_character (vicky, appearance="", text="Вот что приводит к быстрому росту канала!")
    call process_character (n, appearance="blush false", text="Я никогда не ожидал, что это произойдет так быстро...")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Вот почему так важно планировать заранее.")
    call process_character (vicky, appearance="", text="Многие каналы не в состоянии извлечь выгоду из внезапного всплеска успеха.")
    call process_character (vicky, appearance="", text="Чтобы сохранить темп, нужно всегда думать о том, как улучшить свой канал.")
    call process_character (vicky, appearance="", text="Сохранение актуальности для вашей аудитории является фактором номер один для долгосрочного успеха.")
    call process_character (n, appearance="blush false", text="Это именно то, что я хочу сделать с Твинстикс!")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Тогда ваши шансы на успех намного больше, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Вы лучший эксперт в этом деле, [vicky.say_name]!")
    call process_character (n, appearance="blush false", text="Вы когда-нибудь думали о создании собственного канала?")
    call process_character (n, appearance="blush false", text="Бьюсь об заклад, он станет огромным!")

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Вообще-то, я думала о чем-то большем, чем просто канал.")
    call process_character (vicky, appearance="", text="До того, как ты пришел, я печатала планы для своего сайта.")
    call process_character (n, appearance="blush false", text="О, круто!")
    call process_character (n, appearance="blush false", text="Это на голову выше канала ReflexViz.HD точно!")
    call process_character (n, appearance="blush false", text="Какой контент Вы собирались разместить на своем сайте?")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Мне пришла в голову идея, посмотрев твой канал.")
    call process_character (vicky, appearance="", text="В частности, твои порно обзоры.")
    call process_character (n, appearance="blush false", text="Мои порно обзоры помогли?")
    call process_character (n, appearance="blush false", text="Как?")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я наслаждалась твоим юмором и анализом порно, которое ты смотрел.")
    call process_character (vicky, appearance="", text="Но я никогда не понимала, как мало существует высококачественного порно.")
    call process_character (n, appearance="blush false", text="Ты не думаешь, что порно там очень хорошее?")
    call process_character (vicky, appearance="", text="По моему мнению, большинство из них едва ли удовлетворительны.")
    call process_character (vicky, appearance="", text="Сейчас так мало творчества и нестандартного мышления в порнографии.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Это связано с вашим новым сайтом?")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Так и есть!")
    call process_character (vicky, appearance="", text="[n.say_name]...{w=1.0} мой план - стать порно-режиссером!")
    call process_character (n, appearance="blush false", text="П-порно режиссер?")
    call process_character (vicky, appearance="", text="Немного неожиданно, не правда ли?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Вы ведь раньше работали в порно-компании?")
    call process_character (n, appearance="blush false", text="Я думал, вам это не нравится...")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я застряла, выполняя задачи, которые никто не хотел делать, когда я была там.")
    call process_character (vicky, appearance="", text="Я вообще не была вовлечен в производственный процесс.")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Но сейчас я все напишу, спродюсирую и сама все направлю!")
    call process_character (n, appearance="blush false", text="Это звучит намного лучше для вас!")
    call process_character (n, appearance="blush false", text="Когда Вы собираетесь начать?")

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я уже заказала профессиональную видеокамеру.")
    call process_character (vicky, appearance="", text="Что касается студийного пространства, я могу использовать свою квартиру, чтобы сэкономить на стоимости.")
    call process_character (vicky, appearance="", text="И ещё нужно разработать сам сайт.")
    call process_character (vicky, appearance="", text="Это долгий процесс, но стоящий.")
    call process_character (n, appearance="blush false", text="Кто будет на видео, которое Вы сделаете?")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я рада, что ты спросил!")
    call process_character (vicky, appearance="", text="Я буду играть главную роль во всех из них!")
    call process_character (n, appearance="blush false", text="В-вы?!")
    call process_character (n, appearance="blush false", text="Серьезно?!")
    call process_character (n, appearance="blush false", text="Не могу дождаться, чтобы увидеть их!")
    call process_character (n, appearance="blush false", text="Многим другим людям тоже понравятся ваши видео!")
    call process_character (vicky, appearance="", text="Я уверена, что да.")
    call process_character (vicky, appearance="", text="Тяжелая работа всегда окупается!")
    call process_character (n, appearance="blush false", text="Если вам нужна помощь, дайте мне знать [vicky.say_name]!")
    call process_character (n, appearance="blush false", text="Я готов помочь вам, чем только смогу!")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Ты на самом деле существенная часть всего этого, [n.say_name].")
    call process_character (n, appearance="blush false", text="Я?")
    call process_character (vicky, appearance="", text="Я могу продюсировать порно в одиночку...")
    call process_character (vicky, appearance="", text="Но я не думаю, что фильм захватит такую большую аудиторию, как мне хотелось бы.")
    call process_character (vicky, appearance="", text="Поэтому для того, чтобы максимизировать зрительскую аудиторию и интерес...")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я бы хотела, чтобы ты была на сцене со мной.")
    call process_character (n, appearance="blush false", text="!!")
    call process_character (n, appearance="blush false", text="Вы хотите, чтобы я снимался с Вами в порно?!")
    call process_character (vicky, appearance="", text="На мой взгляд, нет никого лучше!")
    call process_character (vicky, appearance="", text="У нас с тобой уже есть отличная сексуальная химия!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Вы так думаете?")
    call process_character (vicky, appearance="", text="Я видела достаточно офисных дел, чтобы знать, куда движется наша траектория, [n.say_name].")
    call process_character (vicky, appearance="", text="Мы с тобой неизбежно закончим сексом.")
    call process_character (n, appearance="blush false", text="Да?")
    call process_character (vicky, appearance="", text="Так почему бы не воспользоваться этим?")
    call process_character (vicky, appearance="", text="Мы смешаем бизнес и удовольствие!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="Это отличная возможность для тебя, [n.say_name]!")
    call process_character (vicky, appearance="", text="Представь себе продвижение моего сайта на вашем канале?")
    call process_character (vicky, appearance="", text="А что, если я стану спонсором?")
    call process_character (vicky, appearance="", text="Я не вижу в этом ничего плохого!")
    call process_character (vicky, appearance="", text="Больше просмотров, больше подписчиков...")
    call process_character (vicky, appearance="", text="И дополнительный доход для тебя и твоей сестры!")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (n, appearance="blush false", text="Сколько видео мы могли бы сделать?")
    call process_character (vicky, appearance="", text="Столько, сколько захотим!")
    call process_character (n, appearance="blush false", text="...")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Ключ в том, чтобы сосредоточиться на том, чтобы порно было превосходного качества!")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Не думаю, что у нас будут проблемы с этим!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Но как мы узнаем, хорошо это или нет?")
    call process_character (vicky, appearance="", text="Легко!")
    call process_character (vicky, appearance="", text="Зрители дадут нам знать.")
    call process_character (vicky, appearance="", text="Как только мы видим, какие видео нравятся нашим зрителям, мы создаем больше видео, которые им нравятся.")
    call process_character (vicky, appearance="", text="И если они устанут от видео, мы вернемся к экспериментам, пока снова не зацепим аудиторию!")
    call process_character (vicky, appearance="", text="Фильмы никогда не будет застаиваться!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Думаю, я понимаю, о чем Вы говорите...")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я бы не волнуюсь, если мы не сделаем хоум-ран первые несколько раз.")
    call process_character (vicky, appearance="", text="Ты не станешь великим режиссером порно за одну ночь!")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="А пока мы должны просто наслаждаться.")
    call process_character (n, appearance="blush false", text="Звучит неплохо!")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="У тебя есть немного свободного времени сегодня, [n.say_name]?")
    call process_character (vicky, appearance="", text="Я подумала, что спрошу, вдруг тебе нужно быть где-то.")
    call process_character (n, appearance="blush false", text="Нет, сейчас у меня нет никаких планов.")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Отлично!")
    call process_character (vicky, appearance="", text="Я надеялась, что мы могли бы попрактиковаться в записи видео.")
    call process_character (n, appearance="blush false", text="Здесь?")
    call process_character (vicky, appearance="", text="Большая часть наших действий будет происходить здесь, так почему бы и нет?")
    call process_character (n, appearance="blush false", text="Но у нас нет камеры?")
    call process_character (vicky, appearance="", text="Мы можем использовать мой смартфон.")
    call process_character (vicky, appearance="", text="Всё будет в порядке.")
    call process_character (n, appearance="blush false", text="Что мы будем делать?")
    call process_character (vicky, appearance="", text="У меня есть кое-что на уме...")

    window hide
    show bg black
    with Dissolve(0.5)

    pause 1.0

    window show

    call process_character (vicky, appearance="", text="Хорошо, я поставлю телефон на запись...")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Там, это происходит!")
    call process_character (vicky, appearance="", text="Вот, возьми это.")
    call process_character (n, appearance="blush false", text="Почему я?")
    call process_character (vicky, appearance="", text="Я хочу, чтобы ты запечатлел это с твоей точки зрения.")
    call process_character (vicky, appearance="", text="Хотелось бы посмотреть, как это выглядит с твоей точки зрения!")
    call process_character (n, appearance="blush false", text="Я сижу в этом кресле?")
    call process_character (vicky, appearance="", text="А Вы...")
    call process_character (n, appearance="blush false", text="Вы встали на колени?")
    call process_character (vicky, appearance="", text="Ты уже догадываешься, что я буду делать?")
    call process_character (vicky, appearance="", text="Позволь мне расстегнуть твои штаны...")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Мм!")
    call process_character (vicky, appearance="", text="Ты уже готов!")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Summer Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg vicky_blowjob_foreskinpull")

    call process_character (vicky, appearance="", text="Как это выглядит?")
    call process_character (vicky, appearance="", text="Я в кадре?")
    call process_character (n, appearance="blush false", text="Ах, да!")
    call process_character (n, appearance="blush false", text="Я вижу Вас!")
    call process_character (vicky, appearance="", text="И твой член тоже на картинке?")
    call process_character (n, appearance="blush false", text="Да!")
    call process_character (vicky, appearance="", text="Прекрасно!")
    call process_character (n, appearance="blush false", text="В-вы тянете...")
    call process_character (vicky, appearance="", text="Чуть не забыла, что у тебя есть крайняя плоть.")
    call process_character (vicky, appearance="", text="Она чувствительная?")
    call process_character (n, appearance="blush false", text="Хаах!")
    call process_character (vicky, appearance="", text="Ох, да!")
    call process_character (vicky, appearance="", text="Ты же знаешь, что я собираюсь сделать это еще...")
    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (vicky, appearance="", text="Это пока хорошо!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="Интересно, чувствительны ли другие части твоих гениталий.")
    call process_character (vicky, appearance="", text="Как бы ты отреагировал на то, что на них положат рот и язык?")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (vicky, appearance="", text="Сначала я проверю внизу...")

    call static_still_ctc ("bg vicky_blowjob_ballsuck")

    call process_character (vicky, appearance="", text="Ммф!")
    call process_character (n, appearance="blush false", text="Ох, ах!")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Его яйца гладкие, никаких волос вообще!)")
    call process_character (vicky, appearance="", text="(Я могу поместить их в рот с легкостью!)")
    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (n, appearance="blush false", text="Мне действительно нравится это, [vicky.say_name]...")
    call process_character (vicky, appearance="", text="Я была бы шокирован, если бы ты не был.")
    call process_character (vicky, appearance="", text="Попробуй сделать хороший снимок моего рта с твоими яйцами!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я не ожидал, что это произойдет с [vicky.say_name]!)")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="(Но я уверен, что счастлив!)")
    call process_character (vicky, appearance="", text="Ммм...")
    call process_character (vicky, appearance="", text="Как продвигается видео?")
    call process_character (vicky, appearance="", text="Твои плечи или руки устают от поднятия телефона?")
    call process_character (n, appearance="blush false", text="У них сейчас все хорошо.")
    call process_character (vicky, appearance="", text="Спасибо за экспромт кинограф, кстати.")
    call process_character (vicky, appearance="", text="Это одна из самых важнейших обязанностей во время производства порно.")
    call process_character (n, appearance="blush false", text="Я получаю удовольствие, делая это!")
    call process_character (n, appearance="blush false", text="Ох, ох!")
    call process_character (vicky, appearance="", text="Тогда тебе будет очень весело, когда я начну делать тебе минет.")

    if stats.stat_value('times_received_blowjob') > 0:
        call process_character (n, appearance="blush false", text="Вы собираетесь сделать мне минет?")
        call process_character (vicky, appearance="", text="Я все еще хочу дать яйцам немного внимания...")
        call process_character (vicky, appearance="", text="Но да, я буду сосать твой член в ближайшее время.")
        call process_character (n, appearance="blush false", text="К-круто.")
        call process_character (vicky, appearance="", text="Ты знаком с минетом, [n.say_name]?")
        call process_character (vicky, appearance="", text="Ты знаешь, каково это должно быть?")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Да, понимаю.")
        call process_character (vicky, appearance="", text="Я посмотрю, смогу ли я оправдать или превзойти твои ожидания!")
    else:
        call process_character (n, appearance="blush false", text="М-минет?")
        call process_character (vicky, appearance="", text="У тебя правда никогда не было такого раньше?")
        call process_character (vicky, appearance="", text="Это будет твой первый раз?")
        call process_character (n, appearance="blush false", text="Д-Да.")
        call process_character (vicky, appearance="", text="Это видео только что стало намного ценнее!")
        call process_character (n, appearance="blush false", text="Почему?")
        call process_character (vicky, appearance="", text="Люди хотели бы видеть, как молодой человек получает свой первый минет!")
        call process_character (vicky, appearance="", text="Это буквально случается один раз в жизни, и это будет записано!")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Это здорово.")
        call process_character (n, appearance="blush false", text="Я не думала, что это настолько важно.")

    call process_character (vicky, appearance="", text="Не мог бы ты передать мне мой телефон, [n.say_name]?")
    call process_character (vicky, appearance="", text="У меня есть идея для камеры...")
    call process_character (n, appearance="blush false", text="...")

    call fade_to_black (1)

    call process_character (vicky, appearance="", text="Хорошо, мне нужно сделать это быстро, чтобы мы могли вернуться к этому...")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Я просто подопру телефон книгами на полу...")
    call process_character (vicky, appearance="", text="Выпрямить угол наклона...")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Мы готовы!")
    call process_character (vicky, appearance="", text="Я думаю, что эта перспектива должна выглядеть фантастически!")

    call static_still_ctc ("bg vicky_blowjob_nocum")

    call process_character (n, appearance="blush false", text="Ух ты!")
    call process_character (n, appearance="blush false", text="Ааагх!")
    call process_character (vicky, appearance="", text="Ммм...")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Это милый хер!)")
    call process_character (vicky, appearance="", text="(Я надеюсь, что это смотрится хорошо на камеру!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="([vicky.say_name] сосет так усердно!)")
    call process_character (n, appearance="blush false", text="(И она сжимает мой пенис рукой!)")
    call process_character (vicky, appearance="", text="Я знаю, что веду себя агрессивно, держа рот на твоем члене...")
    call process_character (vicky, appearance="", text="Но я хочу создать несколько хороших звуков.")
    call process_character (n, appearance="blush false", text="Звуков?")
    call process_character (vicky, appearance="", text="В порно, которое я хочу снять, будет много сексуальных звуков.")
    call process_character (vicky, appearance="", text="Это уникально и безошибочно.")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (n, appearance="blush false", text="Итак, звуки делают порно видео лучше?")
    call process_character (vicky, appearance="", text="Это может превратить среднюю сцену в отличную!")
    call process_character (vicky, appearance="", text="Запись звуков секса никогда не следует упускать из виду!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="Посмотрим, смогу ли я сделать что-нибудь с твоим членом...")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="{i}Шлёп, шлёп!{/i}")
    call process_character (n, appearance="blush false", text="Я... я слышал это!")
    call process_character (vicky, appearance="", text="{i}Хлёб!{/i}")
    call process_character (vicky, appearance="", text="{i}Хлоп!{/i}")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я надеюсь, что мой выбор стать порно режиссером является правильным...)")
    call process_character (vicky, appearance="", text="(Это самая большая авантюра за всю мою карьеру!)")
    call process_character (vicky, appearance="", text="(Я знала, что могу рискнуть, если [n.say_name] ступит на борт!)")
    call process_character (vicky, appearance="", text="(Теперь я просто должна построить бизнес с нуля...)")
    call process_character (vicky, appearance="", text="(Но я лучше всего работаю под давлением!)")
    call process_character (vicky, appearance="", text="(Это перезагружает мою мотивацию!)")
    call process_character (n, appearance="blush false", text="Оох!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я не думаю, что когда-нибудь догадался бы, что буду в порно!)")
    call process_character (n, appearance="blush false", text="(Не через миллион лет!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Интересно, что [sa.say_name] скажет по этому поводу...)")

    if "sam_scene_vaginal" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Она, вероятно, подумает, что это было потрясающе!)")
        call process_character (n, appearance="blush false", text="(Я имею в виду...{w=1.0}[vicky.say_name] сказала, что [sa.say_name] и я уже сделали своё порно...)")
        call process_character (n, appearance="blush false", text="(Интересно, если [sa.say_name] хотела бы быть в одном из видео тоже...)")
    else:
        call process_character (n, appearance="blush false", text="(Я думаю, что она будет в порядке с чем угодно, если это означает рост нашего канала!)")
        call process_character (n, appearance="blush false", text="(Может, ей сделать обзор на видео, которое я сделал!)")
        call process_character (n, appearance="blush false", text="(Интересно, предложит ли она идеи и для сцен...)")

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Даже если моя режиссерская карьера не увенчается успехом, у меня могут быть некоторые альтернативы...)")
    call process_character (vicky, appearance="", text="([n.say_name] будет в моей жизни, все это время)")
    call process_character (vicky, appearance="", text="(Возможно, если все начнется медленно, я могу стану гостевой звездой на канале [n.say_name] и его сестры)")
    call process_character (vicky, appearance="", text="(Я могла бы предложить встряхнуть мои бидоны на камеру для каждого нового подписчика!)")
    call process_character (vicky, appearance="", text="(Я уверена, что их зрительская аудитория будет рада!)")
    call process_character (n, appearance="blush false", text="Ннг...")
    call process_character (n, appearance="blush false", text="Мм! Мм!")
    call process_character (vicky, appearance="", text="Ты почти готов?")
    call process_character (vicky, appearance="", text="Скажи мне, чтобы я могла приготовила смартфон!")
    call process_character (n, appearance="blush false", text="Хрмм!")
    call process_character (vicky, appearance="", text="Хорошо, я должна убедиться, что сниму это!")
    call process_character (vicky, appearance="", text="Есть только один шанс, чтобы снять его в самый раз!")
    call process_character (n, appearance="blush false", text="Я не могу этого удержать...")
    call process_character (vicky, appearance="", text="(Он толкает мне в рот!)")
    call process_character (vicky, appearance="", text="Нет необходимости удерживать его!")
    call process_character (vicky, appearance="", text="Покажи свое лучшее оргазмирующее лицо на камеру!")
    call process_character (n, appearance="blush false", text="Гяаха!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg vicky_blowjob_cum")

    call process_character (vicky, appearance="", text="(Должна держать рот на его члене!)")
    call process_character (vicky, appearance="", text="(Я не хочу потерять свой груз!)")
    call process_character (n, appearance="blush false", text="Я готов!")
    call process_character (n, appearance="blush false", text="Хаах!")
    call process_character (vicky, appearance="", text="Ммм...{w=0.5}мм...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (vicky, appearance="", text="Всё?")
    call process_character (n, appearance="blush false", text="Да...")

    call static_still_ctc ("bg vicky_blowjob_aftercum_openmouth")

    call process_character (vicky, appearance="", text="Ты можешь закрыть мой рот?")
    call process_character (vicky, appearance="", text="Я сейчас сперму вылью..")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="А-аккуратно.")
    call process_character (vicky, appearance="", text="Нравится ли тебе играться со спермой?")
    call process_character (vicky, appearance="", text="Не думаю, что кому-то это не нравится!")
    call process_character (n, appearance="blush false", text="...")

    call static_still_ctc ("bg vicky_blowjob_aftercum_closemouth")

    call process_character (vicky, appearance="", text="{i}Глык.{/i}..")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="([n.say_name] на вкус чертовски хорош!)")
    call process_character (n, appearance="blush false", text="Ты глотаешь, [vicky.say_name]?")
    call process_character (vicky, appearance="", text="...")

    call static_still_ctc ("bg vicky_blowjob_aftercum_swallow")

    call process_character (vicky, appearance="", text="Ааах...")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Я помню тот обзор, что ты написал...")
    call process_character (vicky, appearance="", text="Ты сказал, что тебе нравится, когда девушка глотает.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Да, я действительно так сказал...")
    call process_character (vicky, appearance="", text="Мне было очень весело делать это, [n.say_name]!")
    call process_character (vicky, appearance="", text="Я могла бы привыкнуть делать это полный рабочий день.")
    call process_character (n, appearance="blush false", text="Я тоже!")
    call process_character (n, appearance="blush false", text="Я хочу делать это все больше и больше!")
    call process_character (vicky, appearance="", text="Мне нравится эта твердая приверженность, [n.say_name]!")
    call process_character (vicky, appearance="", text="Мой график становится более гибким.")
    call process_character (vicky, appearance="", text="Если тебе станет скучно и нечего будет делать, отправь мне сообщение!")
    call process_character (vicky, appearance="", text="Я прослежу, чтобы у нас был продуктивный день вместе!")

    python:
        vicky.revistable_scenes.add("vicky_scene_blowjob_revisit")

        if not dream:
            minigame_typing_money_earned_since_last_vicky_meeting = 0
            minigame_typing_times_succeeded_since_last_vicky_meeting = 0
            
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_cummed_in_mouth", 1)
            stats.add_stat("times_received_blowjob", 1)
            stats.add_stat("times_had_balls_sucked", 1)
            stats.add_stat("times_had_balls_played_with", 1)

    call process_end_of_scene ("vicky_scene_blowjob", char=vicky, dream=dream)

    return

label vicky_scene_blowjob_revisit:
    $ no_bust_art = False

    if "vicky_scene_blowjob_revisit" in scenes_completed:
        call vicky_scene_blowjob_revisit_2nd_time
    else:
        call vicky_scene_blowjob_revisit_1st_time

    return

label vicky_scene_blowjob_revisit_1st_time:
    $ no_bust_art = True
    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Хочешь еще один раз?")
    call process_character (vicky, appearance="", text="Так же можно усовершенствовать мою фелляцию до начала видеопроизводства!")

    $ play_music("audio/music/Summer Groove.ogg", fadeout=1.0, fadein = 1.0)
    call static_still_ctc ("bg vicky_blowjob_foreskinpull")

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Тебе нравится, как я это делаю, не так ли?")
    call process_character (n, appearance="blush false", text="А-Ах...")
    call process_character (vicky, appearance="", text="Ты не можешь скрыть возбуждение на лице.")
    call process_character (vicky, appearance="", text="Предельно ясно, что тебе нравится, когда я дразню...")
    call process_character (n, appearance="blush false", text="Аах.")
    call process_character (vicky, appearance="", text="Тяну...")
    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (vicky, appearance="", text="И играюсь с твоей крайней плотью!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="Почему бы тебе не решить, что мне делать дальше, [n.say_name]?")
    call process_character (vicky, appearance="", text="Тебе понравилось, как я сосала яйца раньше?")
    call process_character (vicky, appearance="", text="Я могу сделать это снова, если хочешь...")
    call process_character (vicky, appearance="", text="Или ты предпочитаешь, чтобы я опустилась на твой член и дала тебе минет?")
    call process_character (n, appearance="blush false", text="...")

    $ vicky_bj_revisit_direction_choice = ""

    menu:
        "Я хочу, чтобы мне сосали яйца!":

            $ vicky_bj_revisit_direction_choice = "balls"
            call process_character (vicky, appearance="", text="Твои яйца выглядят красивыми и полными.")
            call process_character (vicky, appearance="", text="Они готовы к массажу языком...")
        "Я хочу, чтобы мне отсосали!":
            $ vicky_bj_revisit_direction_choice = "dick"
            call process_character (vicky, appearance="", text="У тебя член дергается!")
            call process_character (vicky, appearance="", text="Я думаю, он действительно хочет, чтобы мой рот поглотил его...")
        "Я хочу, чтобы мои яйца и член сосали!":
            $ vicky_bj_revisit_direction_choice = "both"
            call add_boldness (1, tag="vicky_blowjob_revisit_both")
            call process_character (vicky, appearance="", text="Ха, ты не хочешь пропустить этот эксперимент, да [n.say_name]?")
            call process_character (vicky, appearance="", text="Твои яйца выглядят красивыми и полными.")
            call process_character (vicky, appearance="", text="Я начну отсюда...")


    if vicky_bj_revisit_direction_choice == "both" or vicky_bj_revisit_direction_choice == "balls":
        call static_still_ctc ("bg vicky_blowjob_ballsuck")

        call process_character (n, appearance="blush false", text="Это так хорошо, [vicky.say_name]!")
        call process_character (vicky, appearance="", text="Рада, что ты так думаешь.")
        call process_character (vicky, appearance="", text="Я думаю, что есть вещи, которые я могла бы улучшить, однако.")
        call process_character (vicky, appearance="", text="Если я хочу стать лучшей звездой фильмов для взрослых, то должна приобрести определённые… {w=1.0}качества.")
        call process_character (n, appearance="blush false", text="Что вы подразумеваете под качествами?")
        call process_character (vicky, appearance="", text="Например, я хотела бы улучшить минет до такой степени, что это будет совершенно иначе, чем сейчас.")
        call process_character (n, appearance="blush false", text="Как бы это могло измениться?")
        call process_character (vicky, appearance="", text="Если я буду достаточно практиковаться, я смогу засунуть твой член и твои яйца мне в глотку!")
        call process_character (n, appearance="blush false", text="Н-ни за что!")
        call process_character (n, appearance="blush false", text="Это возможно?")
        call process_character (vicky, appearance="", text="Мне пришлось бы поработать над глубокой глоткой, чтобы иметь шанс на это.")
        call process_character (vicky, appearance="", text="Я просто посмотрю, на сколько я могу продвинуться...")


    call static_still_ctc ("bg vicky_blowjob_nocum")

    call process_character (n, appearance="blush false", text="Хрм!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="([vicky.say_name] продолжает сосать кончик моего члена!)")
    call process_character (n, appearance="blush false", text="(Она двигает головой так быстро!)")
    call process_character (vicky, appearance="", text="Мм, Мм...")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(У меня еще не было возможности посмотреть нашу первую запись)")
    call process_character (vicky, appearance="", text="(Я надеюсь, что я не похожа на шлюху в ней)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Хотя мне всё равно)")
    call process_character (vicky, appearance="", text="(Я с гордостью нацеплю любые ярлыки, которыми кто-то пытается повесить на меня)")
    call process_character (vicky, appearance="", text="(Особенно если сайт процветает...)")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="Я собираюсь кончить тебе в рот, [vicky.say_name]!")
    call process_character (n, appearance="blush false", text="Ннг!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg vicky_blowjob_cum")

    call process_character (vicky, appearance="", text="Хм?!")
    call process_character (vicky, appearance="", text="(Этого было недостаточно для предварительного предупреждения!)")
    call process_character (vicky, appearance="", text="(Мое горло почти полностью забилось спермой!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (vicky, appearance="", text="{i}Кашляет!{/i} {i}Кашляет!{/i}")
    call process_character (vicky, appearance="", text="Говори мне раньше, чем сейчас, [n.say_name]!")
    call process_character (vicky, appearance="", text="Я сосала так сильно, что когда ты кончил, я вдыхала твою сперму!")
    call process_character (n, appearance="blush false", text="М-моя ошибка...")
    call process_character (n, appearance="blush false", text="Я просто хотел кончить внезапно!")

    call static_still_ctc ("bg vicky_blowjob_aftercum_swallow")

    call process_character (vicky, appearance="", text="Тут даже не так много спермы, чтобы я могла играть с ней!")
    call process_character (vicky, appearance="", text="Большую часть уже проглотила.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я дам тебе знать раньше в следующий раз, [vicky.say_name].")
    call process_character (vicky, appearance="", text="Возможно, ты быстро кончил из-за того, как я сосала.")
    call process_character (vicky, appearance="", text="Это хороший способ проверить наши пределы.")
    call process_character (vicky, appearance="", text="Я лично думаю, что ты найдёшь способы продолжать немного дольше, прежде чем кончить.")
    call process_character (vicky, appearance="", text="Чем больше минетов я тебе сделаю, тем больше ты к этому привыкнешь!")


    $ heard_of_blowjob = True
    call vicky_scene_blowjob_revisit_end

    return

label vicky_scene_blowjob_revisit_2nd_time:
    $ no_bust_art = True
    $ play_music("audio/music/Summer Groove.ogg", fadeout=1.0, fadein = 1.0)
    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Мы начинаем устанавливать тенденцию с этим, [n.say_name]!")
    call process_character (vicky, appearance="", text="Давай работать в соответствии с графиком!")

    call static_still_ctc ("bg vicky_blowjob_ballsuck")

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я думаю, что [n.say_name] и я переопределяем, что значит быть в деловых отношениях...)")
    call process_character (vicky, appearance="", text="(Довольно увлекательно рвать шаблоны)")
    call process_character (vicky, appearance="", text="(Это делает нас аутсайдерами установленной системы)")
    call process_character (vicky, appearance="", text="(Я никогда не могла по-настоящему вписаться в традиционное деловое мышление)")
    call process_character (vicky, appearance="", text="(Я возьму неортодоксальный маршрут в любой день!)")

    call static_still_ctc ("bg vicky_blowjob_nocum")

    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Интересно, что мама скажет, если я уйду из школы, и сосредоточусь на канале и видео с [vicky.say_name]...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Ей, вероятно, это совсем не понравится)")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (n, appearance="blush false", text="(Может быть, я могу спросить о домашнем обучении!)")
    call process_character (n, appearance="blush false", text="([sa.say_name] и я отлично учимся вместе!)")
    call process_character (n, appearance="blush false", text="(И мы могли бы стримить сразу после того, как закончим!)")
    call process_character (n, appearance="blush false", text="(Это было бы прекрасно!)")
    call process_character (n, appearance="blush false", text="(Не говоря уже о том, что я мог бы работать с [vicky.say_name] чаще!)")
    call process_character (n, appearance="blush false", text="(Мне придется потратить некоторое время, чтобы подумать об этом, но это похоже на хороший план!)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", yalign = 0.1)
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg vicky_blowjob_cum")

    call process_character (n, appearance="blush false", text="Оох, кончаю!")
    call process_character (vicky, appearance="", text="Mмф...")
    call process_character (vicky, appearance="", text="Твоя сперма ворвалась мне в рот!")
    call process_character (vicky, appearance="", text="Я была готова на этот раз.")
    call process_character (vicky, appearance="", text="Я обращаю внимание на язык твоего тела.")
    call process_character (vicky, appearance="", text="Это помогает мне предвидеть твою эякуляцию.")


    call vicky_scene_blowjob_revisit_end

    return

label vicky_scene_blowjob_revisit_end:

    python:
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_cummed_in_mouth", 1)
        stats.add_stat("times_received_blowjob", 1)
        stats.add_stat("times_had_balls_sucked", 1)
        stats.add_stat("times_had_balls_played_with", 1)

    call process_end_of_scene ("vicky_scene_blowjob_revisit", char=vicky, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label vicky_scene_vaginal(dream=False):
    call vicky_scene_vaginal_sex (dream=dream)

    return

label vicky_scene_vaginal_sex(dream=False):
    $ renpy.scene('screens')
    window hide
    show bg black
    with Dissolve(0.5)
    pause 0.5

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="...{p}...")
    call process_character (vicky, appearance="", text="(Разработка веб-сайта намного сложнее, чем я думала)")
    call process_character (vicky, appearance="", text="(Эти готовые макеты - не то, что я ищу...)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я, возможно, просто должна научиться создавать их сама)")
    call process_character (vicky, appearance="", text="(Это, вероятно, займет много времени)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я могла бы нанять кого-нибудь, чтобы сделать работу за меня...)")
    call process_character (vicky, appearance="", text="(Что может влететь в копеечку...)")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="{i}Вздох.{/i}..")
    call process_character (vicky, appearance="", text="(С этими планированиями и проектированиями я перенапрягаюсь)")
    call process_character (vicky, appearance="", text="(Мне нужно расслабиться...)")
    call process_character (vicky, appearance="", text="...")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="(Я чувствую себя возбужденной с самого утра)")
    call process_character (vicky, appearance="", text="(И становится только хуже)")
    call process_character (vicky, appearance="", text="...{p}...")
    call process_character (vicky, appearance="", text="(Я думаю, что должна позвонить [n.say_name]...)")

    $ store.current_background = ""
    call process_new_location (bg=nate_room)

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="...{p}...")

    "{i}Дзинь!{/i}"

    call process_character (n, appearance="pose behindhead face neutral blush false", text="(Похоже, я получил сообщение...)")
    call process_character (n, appearance="pose behindhead face happy blush false", text="(Это от [vicky.say_name]!)")
    call process_character (vicky, appearance="", text="\"Было бы здорово, если ты зайдёшь ко мне сегодня.\"")
    call process_character (vicky, appearance="", text="\"Мы отлично проведем время!\"")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="(Мы отлично проведем время...)")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="pose handpocket face happy blush false", text="(Я надеюсь, мы отпразднуем важное достижение на канале!)")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="(Я бы не хотел пропустить это!)")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="(Я должен сообщить ей, что я готов заскочить)")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="\"Круто!\"")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="\"Я скоро буду!\"")

    call fade_to_black (1)

    $ no_bust_art = True

    "{i}Немного позже...{/i}"

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Ну, ты быстро пришёл!")
    call process_character (vicky, appearance="", text="Должно быть, мое текстовое сообщение пришло в правильное время!")
    call process_character (n, appearance="blush false", text="Вы прислали, как раз вовремя!")
    call process_character (n, appearance="blush false", text="Я болтался в своей комнате.")
    call process_character (vicky, appearance="", text="Хотел поиграть в видеоигры, я полагаю?")
    call process_character (n, appearance="blush false", text="Я думал об этом, да.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Вы сказали, что мы отлично проведем время, если я приду!")
    call process_character (n, appearance="blush false", text="Мы отметим важное достижение на канале Твинстикс?")
    call process_character (n, appearance="blush false", text="Или мы собираемся снять порно видео?")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я знаю, что обычно всякий раз, когда я прошу тебя приехать, это связано с работой так или иначе.")
    call process_character (vicky, appearance="", text="Мы с тобой в последнее время работаем не покладая рук.")
    call process_character (n, appearance="blush false", text="Точно!")
    call process_character (n, appearance="blush false", text="У меня никогда не было такого занятого лета!")
    call process_character (vicky, appearance="", text="Я могу сказать то же самое.")
    call process_character (vicky, appearance="", text="Я работала допоздна несколько ночей.")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Вот почему я думаю, что мы заслужили перерыв на этот раз.")
    call process_character (n, appearance="blush false", text="Да?")
    call process_character (vicky, appearance="", text="Никто не работает так усердно, как мы [n.say_name].")
    call process_character (vicky, appearance="", text="Мы работаем больше средней нагрузки, потому что хотим добиться успеха.")
    call process_character (vicky, appearance="", text="Но даже нам нужно время от времени расслабляться.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Мне нравится, как это звучит.")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Разум и тело нуждаются в отдыхе.")
    call process_character (vicky, appearance="", text="Вредно для здоровья всегда быть в рабочем режиме.")
    call process_character (vicky, appearance="", text="Подумай о том, как много времени мы находимся в моем офисе!")
    call process_character (n, appearance="blush false", text="Мы здесь практически все время...")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Вот именно!")
    call process_character (vicky, appearance="", text="Так что давай все изменим!")
    call process_character (n, appearance="blush false", text="Как?")
    call process_character (vicky, appearance="", text="Пойдем в мою спальню.")
    call process_character (vicky, appearance="", text="Мне там легко расслабиться и устроиться поудобнее.")
    call process_character (n, appearance="blush false", text="Я никогда не видел вашу спальню.")
    call process_character (vicky, appearance="", text="Тем больше причин туда ехать!")

    window hide
    show bg black
    with Dissolve(0.5)
    pause 0.5

    call process_character (vicky, appearance="", text="...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="Вот она!")
    call process_character (n, appearance="blush false", text="Очень мило, [vicky.say_name]!")
    call process_character (n, appearance="blush false", text="Я расслабляюсь здесь!")
    call process_character (vicky, appearance="", text="Понимаешь, что я имею ввиду?")
    call process_character (vicky, appearance="", text="Мне нужна была спальня, которая могла бы помочь мне быстро заснуть после долгих ночей работы.")
    call process_character (n, appearance="blush false", text="Мне тоже нравится вид!")
    call process_character (n, appearance="blush false", text="Я забыл, как высоко Вы живёте!")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Почему бы тебе не опробовать мою кровать?")
    call process_character (vicky, appearance="", text="У неё матрас с эффектом памяти.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="О, это действительно здорово!")
    call process_character (n, appearance="blush false", text="Очень удобно!")
    call process_character (vicky, appearance="", text="Они дорогие, но стоят того, если хочешь спать спокойно.")
    call process_character (n, appearance="blush false", text="Я должен спросить мою маму, может она купит мне такой!")
    call process_character (vicky, appearance="", text="Со скоростью, с которой развивается ваш канал [n.say_name], ты сможешь купить его из своего кармана!")
    call process_character (n, appearance="blush false", text="Эй, я, наверное, мог бы да!")
    call process_character (vicky, appearance="", text="...{p}...")
    call process_character (vicky, appearance="", text="(Я чувствую, как твердеют мои соски...)")
    call process_character (vicky, appearance="", text="(И я начинаю мокнуть...)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(На этой кровати я не занималась ещё сексом)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я думала, что так и останется, пока не появился [n.say_name]...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Кровать Вики намного лучше, чем моя)")
    call process_character (n, appearance="blush false", text="(Это заставляет меня закрыть глаза на некоторое время...)")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (n, appearance="blush false", text="{i}Уфф!{/i}")
    call process_character (n, appearance="blush false", text="(Что-то тяжелое лежит на мне...)")
    call process_character (vicky, appearance="", text="Эта кровать сделана для двоих.")
    call process_character (n, appearance="blush false", text="Почему Вы сидите на мне, Вики?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ты снимаешь с меня штаны?")
    call process_character (vicky, appearance="", text="Они тебе больше не понадобятся.")
    call process_character (n, appearance="blush false", text="...")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg vicky_onbed_clothed_soft")

    call process_character (vicky, appearance="", text="Очень мило.")
    call process_character (vicky, appearance="", text="Теперь мы все трахаться!")
    call process_character (n, appearance="blush false", text="Т-трахаться?")
    call process_character (vicky, appearance="", text="Ммм, я буду сидеть на твоем члене!")
    call process_character (vicky, appearance="", text="Мне было интересно, как ты будешь чувствовать себя в моей киске, и я готова это узнать!")

    if stats.stat_value("times_had_vaginal_sex") > 0:
        call process_character (n, appearance="blush false", text="Это должно быть очень приятно...")
        call process_character (vicky, appearance="", text="Ах, ты говоришь, что уже ублажал женщину своим членом?")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Я просто знаю, что мне это очень понравилось раньше.")
    else:
        call process_character (n, appearance="blush false", text="Это то, что Вы называете трахаться?")
        call process_character (vicky, appearance="", text="Это нормально, если ты не знаешь, как это делать правильно, [n.say_name].")
        call process_character (vicky, appearance="", text="Ты быстро схватываешь на лету!")

    if "sam_scene_vaginal" in scenes_completed:
        call process_character (vicky, appearance="", text="Твой член понравился твоей сестре [sa.say_name]?")
        call process_character (n, appearance="blush false", text="...")
        call process_character (vicky, appearance="", text="Я помню, выражение её лица, когда ты колотил ее киску.")
        call process_character (vicky, appearance="", text="Она наслаждалась каждым моментом!")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="[sa.say_name] никогда не испытывала ничего подобного раньше.")
        call process_character (vicky, appearance="", text="Она помогла мне предвкусить твой член!")
        call process_character (vicky, appearance="", text="Я надеюсь, что это больше, чем просто реклама!")



    call static_still_ctc ("bg_vicky_onbed_clothed_hard")

    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="Ты чувствуешь, как мои трусики трутся о твой член?")
    call process_character (vicky, appearance="", text="Каково это, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Ох...")
    call process_character (vicky, appearance="", text="Ммм, это хорошее чувство!")
    call process_character (vicky, appearance="", text="Это гарантированно успокоит наши нервы!")
    call process_character (vicky, appearance="", text="Я уже чувствую облегчение от сегодняшнего стресса!")
    call process_character (n, appearance="blush false", text="Очень приятно это слышать.")
    call process_character (vicky, appearance="", text="Не беспокойся о написании нового обзора, или вашего следующего стрима...")
    call process_character (vicky, appearance="", text="Просто наслаждайся моментом и очисти голову.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="Только подумай о том, как моя киска опустится на твой член...")

    call static_still_ctc ("bg vicky_onbed_clothed_pen")

    call process_character (vicky, appearance="", text="Да, да!")
    call process_character (vicky, appearance="", text="Твой член хотел быть в моей киске!")
    call process_character (n, appearance="blush false", text="Ах, [vicky.say_name]!")
    call process_character (n, appearance="blush false", text="Вы такая теплая [vicky.say_name]!")
    call process_character (vicky, appearance="", text="Это только начало, [n.say_name]!")
    call process_character (vicky, appearance="", text="Мы оба будем горячими и потными, когда всё закончится!")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (vicky, appearance="", text="Это… {w=1.0}это так хорошо!")
    call process_character (vicky, appearance="", text="Оох!")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Мне нужно скорректировать свою позу...")
    call process_character (vicky, appearance="", text="Тогда я смогу больше двигаться!")

    call static_still_ctc ("bg vicky_vaginal_clothed")

    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (vicky, appearance="", text="Теперь я могу ездить на твоём хере как следует, [n.say_name]!")
    call process_character (vicky, appearance="", text="Так у меня будет больше баланса!")
    call process_character (n, appearance="blush false", text="Я понимаю, что Вы имеете в виду!")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Невероятно думать о событиях, приведших к этому...)")
    call process_character (vicky, appearance="", text="(Сначала я действительно думала, что [n.say_name] просто похотливый ребенок, одержимый большими сиськами)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Ну, он определенно одержим большими сиськами… {w=1.0}но я не думала, что он будет кем-то большим)")
    call process_character (vicky, appearance="", text="(Я думала, что он пощупает меня, и это сможет мотивировать его развивать скромный канал)")
    call process_character (vicky, appearance="", text="(Но он продолжает делать замечательную работу со своим каналом)")
    call process_character (vicky, appearance="", text="(И он делает со мной удивительные вещи...)")
    call process_character (n, appearance="blush false", text="Ахх, {i}вздох.{/i}..")
    call process_character (vicky, appearance="", text="(Он умный, интуитивный и уже имеет отличное деловое чутье)")
    call process_character (vicky, appearance="", text="(Но у него также есть эта очаровательная невинность)")
    call process_character (vicky, appearance="", text="(И черт возьми, он замечательно трахается!)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я не думала, что кто-то может поспевать моему образу жизни, но [n.say_name] держится в седле)")
    call process_character (vicky, appearance="", text="(Он заставляет меня задуматься, должна ли я оставаться одинокой или нет...)")
    call process_character (n, appearance="blush false", text="Хаа!")
    call process_character (n, appearance="blush false", text="Хрм!")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я думаю, что [n.say_name] - один на миллион, нет...{w=0.5} один на миллиард!")
    call process_character (vicky, appearance="", text="(Я никогда не встречу кого-то, кто любит сексуальное удовольствие так же, как он!)")
    call process_character (vicky, appearance="", text="...{p}...")
    call process_character (vicky, appearance="", text="Как у тебя дела, [n.say_name]?")
    call process_character (n, appearance="blush false", text="У меня все отлично получается.")
    call process_character (vicky, appearance="", text="Я бы не попробовала эту позу, если бы мы не были на кровати.")
    call process_character (n, appearance="blush false", text="Ах, почему?")
    call process_character (vicky, appearance="", text="Ну, во-первых, я придаю тебе намного больше веса.")
    call process_character (vicky, appearance="", text="На мягкой кровати, нет проблем потому что матрас поглощает удар.")
    call process_character (vicky, appearance="", text="Если бы мы были на твердом полу...")
    call process_character (vicky, appearance="", text="Я бы выбила из тебя весь дух прямо сейчас!")
    call process_character (n, appearance="blush false", text="Не думаю, что мне бы это понравилось...")
    call process_character (vicky, appearance="", text="Нет, определенно нет.")
    call process_character (vicky, appearance="", text="Аах, да...")
    call process_character (n, appearance="blush false", text="Мм!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Как продвигается ваш сайт?")
    call process_character (vicky, appearance="", text="Спасибо, что спросил.")
    call process_character (vicky, appearance="", text="Все идет, но медленнее, чем хотелось бы.")
    call process_character (n, appearance="blush false", text="Почему?")
    call process_character (vicky, appearance="", text="Думаю, я слишком много смотрю на картину в целом, и это заставляет меня упираться в стену.")
    call process_character (vicky, appearance="", text="Лучше превратить большой проект в маленькие сегменты.")
    call process_character (vicky, appearance="", text="Вот как мне нужно подойти к этому сайту.")
    call process_character (n, appearance="blush false", text="Я занимаюсь обзорами аналогичным образом.")
    call process_character (n, appearance="blush false", text="Я разделил их на более мелкие разделы, и стало намного легче писать!")
    call process_character (vicky, appearance="", text="Это очень хороший образ мышления.")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Ах, да, да!")
    call process_character (vicky, appearance="", text="Ха-ха, послушай!")
    call process_character (vicky, appearance="", text="Мы должны трахаться, а говорим об управлении проектами!")
    call process_character (vicky, appearance="", text="Но ты знаешь...")
    call process_character (vicky, appearance="", text="Секс заставил меня пересмотреть свой метод работы.")
    call process_character (vicky, appearance="", text="Я чувствую, что теперь я могу гораздо эффективнее справиться с этим сайтом!")
    call process_character (n, appearance="blush false", text="Это потрясающе, [vicky.say_name]!")
    call process_character (n, appearance="blush false", text="Вы всегда во всем разбираетесь!")
    call process_character (vicky, appearance="", text="Я могу быстрее находить решения, когда ты рядом, [n.say_name].")
    call process_character (vicky, appearance="", text="У тебя просто аура мотивации.")
    call process_character (n, appearance="blush false", text="Моя аура чего?")
    call process_character (vicky, appearance="", text="Мы можем поговорить об этом позже...")
    call process_character (vicky, appearance="", text="То, что я хочу сделать прямо сейчас, это заставить нас испытать двойной оргазм.")
    call process_character (n, appearance="blush false", text="Двойной оргазм?")
    call process_character (vicky, appearance="", text="То есть мы оба кончим одновременно.")
    call process_character (n, appearance="blush false", text="Ох, здорово.")
    call process_character (n, appearance="blush false", text="Мы попытаемся сделать это, пока трахаемся сейчас?")
    call process_character (vicky, appearance="", text="Мы должны сделать что-то более мощное, чтобы вызвать двойной оргазм.")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Думаю, я знаю, что мы можем попробовать.")
    call process_character (n, appearance="blush false", text="Что Вы придумали?")
    call process_character (vicky, appearance="", text="Позволь мне...")

    call fade_to_black (1)

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Хорошо, я лягу снизу...")
    call process_character (vicky, appearance="", text="А ты продолжаешь в том же духе...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="Хорошо, теперь ты должен отодвинуть свои ноги назад...")
    call process_character (n, appearance="blush false", text="Уоу!")
    call process_character (n, appearance="blush false", text="Я должен отогнуть их так далеко?")
    call process_character (vicky, appearance="", text="Это будет стоить того, [n.say_name]!")

    call static_still_ctc ("bg vicky_matingpress_clothed")

    call process_character (n, appearance="blush false", text="Аааахх!")
    call process_character (vicky, appearance="", text="Оох! Это работает!")
    call process_character (vicky, appearance="", text="Это работает фантастически, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="М-мои ноги практически над моей головой!")
    call process_character (vicky, appearance="", text="Но чувствуешь ли ты экстаз от этого?!")
    call process_character (vicky, appearance="", text="То, как твой член помещается в моей киске, {i}задыхается!{/i}")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я никогда не знал, что мои ноги могут согнуться так далеко!)")
    call process_character (n, appearance="blush false", text="(Я надеюсь, что они не застрянут!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Это правда, что говорит [vicky.say_name], хотя...)")
    call process_character (n, appearance="blush false", text="Ааах!")
    call process_character (n, appearance="blush false", text="(Мой член чувствует супер сильное ощущение от этого!)")
    call process_character (n, appearance="blush false", text="(Это похоже на то, что мой пенис горит, но это не больно)")
    call process_character (n, appearance="blush false", text="(Вместо этого он просто чувствует себя потрясающе!)")
    call process_character (n, appearance="blush false", text="Хрм!")
    call process_character (vicky, appearance="", text="Ммм!")
    call process_character (vicky, appearance="", text="(Хер [n.say_name] тыкается на мою точку G каждые несколько секунд!)")
    call process_character (vicky, appearance="", text="{i}Задыхается!{/i}")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я считаю, что моя сексуальная выносливость выше среднего, но...)")
    call process_character (vicky, appearance="", text="(Это проверка моих пределов!)")
    call process_character (vicky, appearance="", text="(Я не могу себе представить, что [n.say_name] чувствует)")
    call process_character (vicky, appearance="", text="(Это неизбежно, он кончит)")
    call process_character (n, appearance="blush false", text="Хаа, аах...")
    call process_character (n, appearance="blush false", text="[vicky.say_name]...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я не могу продолжать двигаться.")
    call process_character (n, appearance="blush false", text="Я готов взорваться!")
    call process_character (vicky, appearance="", text="Я разделяю те же чувства!")
    call process_character (vicky, appearance="", text="Мы оба доведены до крайности!")
    call process_character (n, appearance="blush false", text="Мм, Ммм!")
    call process_character (vicky, appearance="", text="Я кончаю, [n.say_name]!")
    call process_character (vicky, appearance="", text="Давай смешаем наши телесные жидкости!")
    "[n.say_name] & Vicky" "Ааах!!"

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg vicky_matingpress_clothed_cum")

    call process_character (n, appearance="blush false", text="Ннг, Ннг!")
    call process_character (vicky, appearance="", text="(О, черт, какой оргазм!)")
    call process_character (vicky, appearance="", text="(Что в сочетании с эякуляцией [n.say_name]...)")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")

    call static_still_ctc ("bg vicky_matingpress_clothed_cum_impreg")

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Разве эта поза не стоила того, [n.say_name]?")
    call process_character (vicky, appearance="", text="Ты должно быть хорошо себя чувствуешь, зайдя сегодня?")
    call process_character (n, appearance="blush false", text="Мм...")
    call process_character (n, appearance="blush false", text="Ммм...")
    call process_character (vicky, appearance="", text="Нам обоим это было нужно.")
    call process_character (vicky, appearance="", text="Такой оргазм избавляет от беспокойства.")
    call process_character (vicky, appearance="", text="Я чувствую, что могу сосредоточиться гораздо больше, чем мог!")
    call process_character (vicky, appearance="", text="Ты чувствуешь то же самое, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Хм?")
    call process_character (n, appearance="blush false", text="Да...")
    call process_character (n, appearance="blush false", text="Я чувствую, что я сосредоточен… {w=1.0}тоже...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Хрр...")
    call process_character (vicky, appearance="", text="(Он вырубился прямо сейчас...)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="{i}Зевок.{/i}..")
    call process_character (vicky, appearance="", text="(Я могла бы использовать дремоту...)")

    python:
        vicky.revistable_scenes.add("vicky_scene_vaginal_revisit")

        if not dream:
            minigame_typing_money_earned_since_last_vicky_meeting = 0
            minigame_typing_times_succeeded_since_last_vicky_meeting = 0
            
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_vaginal_sex", 1)
            stats.add_stat("times_given_vaginal_creampie", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("vicky_scene_vaginal", char=vicky, dream=dream)

    return

label vicky_scene_vaginal_revisit:
    $ no_bust_art = False

    if "vicky_scene_vaginal_revisit" in scenes_completed:
        call vicky_scene_vaginal_revisit_2nd_time
    else:
        call vicky_scene_vaginal_revisit_1st_time

    return

label vicky_scene_vaginal_revisit_1st_time:
    $ no_bust_art = True

    show bg vicky_sit_smile
    with Dissolve(0.5)
    call process_character (vicky, appearance="", text="Ты выбрал идеальное время, чтобы зайти, [n.say_name]!")
    call process_character (vicky, appearance="", text="Я только что закончила всю работу.")
    call process_character (vicky, appearance="", text="Так что я могу немного повеселиться...")

    $ play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)
    call static_still_ctc ("bg_vicky_onbed_clothed_hard")

    call process_character (vicky, appearance="", text="Я просто подумала...")
    call process_character (vicky, appearance="", text="Нам правда нужна наша одежда для этого?")
    call process_character (vicky, appearance="", text="В прошлый раз это было в основном потому, что я просто не хотела откладывать.")
    call process_character (vicky, appearance="", text="Но оглядываясь назад, отсутствие одежды кажется идеальным вариантом.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я нормально к этому отношусь.")
    call process_character (vicky, appearance="", text="Тебе, наверное, интересно, как сильно мои сиськи будут покачиваться, когда мы будем трахаться!")
    call process_character (vicky, appearance="", text="Я права?")

    menu:
        "Мне просто нравится смотреть на Ваши сиськи.":
            call process_character (vicky, appearance="", text="Ты получишь отличный вид на них, как ляжешь.")
            call process_character (vicky, appearance="", text="Есть много преимуществ для тебя в этой позе, не так ли?")
        "Мне немного любопытно...":
            call process_character (vicky, appearance="", text="Немного любопытно?")
            call process_character (vicky, appearance="", text="Ха, я не думаю, что немного.")
            call process_character (vicky, appearance="", text="Бьюсь об заклад, ты уже давно задаёшься вопросом...")
        "Я надеюсь, что они будут высоко подпрыгивать!":
            call process_character (vicky, appearance="", text="Я не знаю, как будут подпрыгивать, но…")
            call process_character (vicky, appearance="", text="Я посмотрю, могу ли я заставить их прыгать, пока трахаю тебя!")

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Вообще-то, я должна быть осторожна, расстегивая блузку.")
    call process_character (vicky, appearance="", text="Если я не буду, пуговицы послетают от веса моих сисек, выталкивая их!")
    call process_character (vicky, appearance="", text="...")

    call static_still_ctc ("bg vicky_onbed_naked_hard")

    call process_character (n, appearance="blush false", text="До сих пор не могу поверить, какие у вас огромные сиськи [vicky.say_name]!")
    call process_character (vicky, appearance="", text="Ты можешь поблагодарить женщин из со стороны моего отца.")
    call process_character (vicky, appearance="", text="Средний размер чашечек у них, G.")
    call process_character (n, appearance="blush false", text="Чашечки G?")
    call process_character (n, appearance="blush false", text="Большие?")
    call process_character (vicky, appearance="", text="Они больше, чем твоя голова, [n.say_name].")

    if "simone_scene_undressing" in scenes_completed:
        call process_character (n, appearance="blush false", text="Такие же большие, как сиськи моей мамы!")
        call process_character (vicky, appearance="", text="Так твоя мать хорошо обеспечена?")
        call process_character (n, appearance="blush false", text="Да!")
        call process_character (n, appearance="blush false", text="Они были большими столько, сколько я помню!")
        call process_character (vicky, appearance="", text="Большая грудь создает приятные воспоминания...")
    else:
        call process_character (n, appearance="blush false", text="Не может быть!")
        call process_character (vicky, appearance="", text="Это правда.")
        call process_character (vicky, appearance="", text="Однако, насколько я знаю, у меня самые большие в семье.")
        call process_character (n, appearance="blush false", text="Так у вас самая большая грудь из всех?")
        call process_character (vicky, appearance="", text="Мои родственники пялятся на мою грудь во время семейных торжеств и встреч.")
        call process_character (vicky, appearance="", text="И они все сходят с ума, если я ношу топ с низким вырезом.")


    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="Но давай не будем отвлекаться.")
    call process_character (vicky, appearance="", text="Твой член и моя киска должны слиться!")

    call static_still_ctc ("bg vicky_onbed_naked_pen")

    call process_character (n, appearance="blush false", text="Хааа!")
    call process_character (vicky, appearance="", text="Я не думаю, что нам нужно начинать медленно.")
    call process_character (vicky, appearance="", text="Мы можем ускорить темп гораздо раньше!")
    call process_character (vicky, appearance="", text="Тебе нравится, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Мм!")
    call process_character (n, appearance="blush false", text="Звучит неплохо.")
    call process_character (vicky, appearance="", text="Позволь мне скорректировать...")

    call static_still_ctc ("bg vicky_vaginal_nude")

    call process_character (n, appearance="blush false", text="Такое же чувство, как и раньше!")
    call process_character (vicky, appearance="", text="Ты прав!")
    call process_character (vicky, appearance="", text="Ох! Ах...")
    call process_character (vicky, appearance="", text="(Моей киске становится жарко)")
    call process_character (vicky, appearance="", text="Ммм! {i}Задыхается!{/i}")
    call process_character (vicky, appearance="", text="(Её чувствительность взлетела до небес!)")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (n, appearance="blush false", text="(Мой член...)")
    call process_character (n, appearance="blush false", text="(Это похоже на то, что он тает в киске [vicky.say_name]!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я слышу, как ее сиськи шлепаются, когда она отскакивает от меня)")
    call process_character (n, appearance="blush false", text="(Это заставляет меня снова захотеть трахнуть их...)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Мои сиськи выглядят так, как будто у них есть собственный разум!)")
    call process_character (vicky, appearance="", text="(Они сходят с ума, когда я занимаюсь сексом)")
    call process_character (vicky, appearance="", text="([n.say_name] загипнотизирован ими, ха-ха!)")
    call process_character (n, appearance="blush false", text="Эм, Мммм...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Вы хотите сделать то, что делали раньше [vicky.say_name]?")
    call process_character (vicky, appearance="", text="То, что я делала раньше?")
    call process_character (n, appearance="blush false", text="{cps=40}Ну, знаете, оттолкнуть мои ноги назад и-{/cps}{w=0.75}{nw}")
    call process_character (vicky, appearance="", text="Ох, это!")
    call process_character (vicky, appearance="", text="Да!")
    call process_character (vicky, appearance="", text="Я хочу сделать это снова!")
    call process_character (vicky, appearance="", text="Я удивлена, что ты упомянул об этом!")
    call process_character (vicky, appearance="", text="Я думала, тебе неудобно.")
    call process_character (n, appearance="blush false", text="Нет, все не так уж плохо.")
    call process_character (n, appearance="blush false", text="Это того стоит, как здорово!")
    call process_character (vicky, appearance="", text="Мне нравится, как эта поза сближает нас.")
    call process_character (vicky, appearance="", text="Мы прям сверху друг на друге, когда трахаемся так!")

    call static_still_ctc ("bg vicky_matingpress_nude")

    call process_character (n, appearance="blush false", text="Ах, хаа!")
    call process_character (vicky, appearance="", text="Да, это правильное место!")
    call process_character (vicky, appearance="", text="О, черт!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="Я до сих пор не могу смириться с тем, как я все это придумала.")
    call process_character (vicky, appearance="", text="Это уже моя любимая поза!")
    call process_character (n, appearance="blush false", text="Это одна из моих любимых тоже!")
    call process_character (vicky, appearance="", text="Это может стать нашей фирменной секс позой для нашего порно видео!")
    call process_character (vicky, appearance="", text="Я не видела порно, в котором делают такую позу.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я не помню, чтобы видел порно, в котором делают такую позу.")
    call process_character (vicky, appearance="", text="Тогда мы должны снять короткое видео, демонстрирующее этот способ трахаться!")
    call process_character (vicky, appearance="", text="Думаю, если бы мы выложили его в сеть, оно бы распространилось как лесной пожар!")
    call process_character (n, appearance="blush false", text="Вы думаете, это сработает?")
    call process_character (vicky, appearance="", text="Без сомнения.")
    call process_character (vicky, appearance="", text="Это будет еще лучше, если мы захватим хорошие ракурсы.")
    call process_character (vicky, appearance="", text="Можешь себе представить, как выглядит эта поза сзади?")
    call process_character (vicky, appearance="", text="Нужно будет записать это в следующий раз для нас!")
    call process_character (n, appearance="blush false", text="Ххмн!")
    call process_character (n, appearance="blush false", text="Я кончу через пару секунд, [vicky.say_name]!")
    call process_character (vicky, appearance="", text="Это напомнило мне, что мне нужно будет больше снимать твои оргазмы!")
    call process_character (vicky, appearance="", text="Каждый кадр семяизвержения будет стоящий!")
    call process_character (n, appearance="blush false", text="Нннг!")
    call process_character (n, appearance="blush false", text="[vicky.say_name]!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg vicky_matingpress_nude_cum")

    call process_character (vicky, appearance="", text="Ааах, Мммм!")
    call process_character (vicky, appearance="", text="(Я чувствую сперму [n.say_name] глубоко внутри меня)")
    call process_character (n, appearance="blush false", text="Ещё чуть-чуть!")
    call process_character (n, appearance="blush false", text="Хаа! Хаа!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (n, appearance="blush false", text="Э-это всё.")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Сперма будет стекать из моей киски в течение нескольких часов после этого...)")
    call process_character (vicky, appearance="", text="([n.say_name] выстрелил сперму, как из пушки!)")

    call vicky_scene_vaginal_revisit_end

    return

label vicky_scene_vaginal_revisit_2nd_time:
    $ no_bust_art = True
    $ play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg vicky_vaginal_nude")

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я все время забываю взять презервативы, когда я хожу за покупками)")
    call process_character (vicky, appearance="", text="(Если мы собираемся продолжать так трахаться, есть шанс забеременеть от [n.say_name]...)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я всегда ненавидела презервативы)")
    call process_character (vicky, appearance="", text="(Это искусственный барьер, который отнимает много удовольствия)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Мне нужно будет принять на утро таблетки, так проще)")
    call process_character (vicky, appearance="", text="(Мне нужно запастись ими побольше и поскорее!)")
    call process_character (vicky, appearance="", text="(Я думаю, что у меня есть старая упаковка, лежащая где-то)")
    call process_character (vicky, appearance="", text="(Не уверена, что срок годности истек...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="([vicky.say_name] придумала, как будут платить за видео, которые мы сделаем?)")
    call process_character (n, appearance="blush false", text="(Интересно, какой был бы лучший способ продать наши видео...)")
    call process_character (n, appearance="blush false", text="(Мы могли бы продавать их индивидуально...)")
    call process_character (n, appearance="blush false", text="(Но нам, вероятно, придется продавать их по низкой цене)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Подписка была бы лучше!)")
    call process_character (n, appearance="blush false", text="(Люди получат доступ к каждому видео за ежемесячную плату!)")
    call process_character (n, appearance="blush false", text="(Это то, что я хотел бы, если посетил веб-сайт!)")
    call process_character (n, appearance="blush false", text="(Хотя...)")
    call process_character (n, appearance="blush false", text="(Что делает видео совершенно бесплатным для всех)")
    call process_character (n, appearance="blush false", text="(Мы могли бы собирать пожертвования, как делаем сейчас для Твинстикс!)")
    call process_character (n, appearance="blush false", text="(Этот метод работал отлично до сих пор!)")
    call process_character (n, appearance="blush false", text="(Я должен поговорить с [vicky.say_name] об этом в следующий раз)")

    call static_still_ctc ("bg vicky_matingpress_nude")

    call process_character (vicky, appearance="", text="Ах, Мм...")
    call process_character (vicky, appearance="", text="Я думала о разных местах, где мы могли бы снимать наши видео.")
    call process_character (vicky, appearance="", text="Кроме моей квартиры.")
    call process_character (n, appearance="blush false", text="У вас есть какие-нибудь планы?")
    call process_character (n, appearance="blush false", text="Оох!")
    call process_character (vicky, appearance="", text="Ну, первое, что приходит в голову...")
    call process_character (vicky, appearance="", text="Пляж, парк...")
    call process_character (vicky, appearance="", text="Моя машина.")
    call process_character (n, appearance="blush false", text="Мы будем трахаться в вашей машине?")
    call process_character (vicky, appearance="", text="Если это то, что ты хочешь сделать.")
    call process_character (n, appearance="blush false", text="А если кто-нибудь увидит нас в этих местах?")
    call process_character (vicky, appearance="", text="Не увидит, если мы выберем удалённое место или спрячемся.")
    call process_character (vicky, appearance="", text="Мы могли бы также арендовать лодку на день и повеселиться в море.")
    call process_character (n, appearance="blush false", text="О, это было бы чертовски круто!")
    call process_character (n, appearance="blush false", text="Наша собственная лодка!")
    call process_character (vicky, appearance="", text="Я спрошу об этом, когда у меня будет возможность.")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", xalign = 0.1, yalign = 0.1)
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg vicky_matingpress_nude_cum")

    call process_character (n, appearance="blush false", text="Хннг!")
    call process_character (n, appearance="blush false", text="Хррм!")
    call process_character (vicky, appearance="", text="О, да!")
    call process_character (vicky, appearance="", text="Аах!")
    call process_character (n, appearance="blush false", text="...")

    call static_still_ctc ("bg vicky_matingpress_nude_cum_impreg")

    call process_character (vicky, appearance="", text="(Я знаю, что недавно стирала простыни...)")
    call process_character (vicky, appearance="", text="(Мне нужно купить простыню чёрного цвета, чтобы знать, что она чиста)")
    call process_character (vicky, appearance="", text="(Скорее всего, есть несколько засохших пятен)")

    call vicky_scene_vaginal_revisit_end

    return

label vicky_scene_vaginal_revisit_end:

    python:
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_vaginal_sex", 1)
        stats.add_stat("times_given_vaginal_creampie", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("vicky_scene_vaginal_revisit", char=vicky, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label vicky_scene_anal(dream=False):
    call vicky_scene_anal_sex (dream=dream)

    return

label vicky_scene_anal_sex(dream=False):
    call process_scene_beginning (bg="bg nate_room_daytime", dream=dream)
    call process_character (n, appearance="outfit underwear pose handsdown face aroused blush false", text="...{p}...")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="(Хм?)")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="(Письмо в такую рань?)")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="(Единственный человек, которого это делает...)")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="([vicky.say_name], я так и думал!)")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="\"[n.say_name] у меня фантастические новости!\"")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="\"Мой сайт уже написан и почти готов к запуску!\"")
    call process_character (n, appearance="outfit underwear pose twohandfist face happy blush false", text="(Она наконец-то сделала свой сайт!)")
    call process_character (n, appearance="outfit underwear pose twohandfist face happy blush false", text="([vicky.say_name] работает над этим уже долгое время)")
    call process_character (n, appearance="outfit underwear pose twohandfist face happy blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="(Похоже, она отправила мне еще несколько сообщений...)")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="\"Я хочу, чтобы ты и я записали приветственное сообщение для сайта\"")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="\"Я хочу заинтриговать посетителей, и приветственное сообщение - идеальный способ привлечь интерес!\"")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="\"Если бы ты зашёл ко мне поскорее, это было бы здорово.\"")
    call process_character (n, appearance="outfit underwear pose behindhead face happy blush false", text="(Это хорошая идея, записать видео, которое представляет то, что есть на веб-сайте!)")
    call process_character (n, appearance="outfit underwear pose behindhead face happy blush false", text="([sa.say_name] и я должны сделать то же самое для нашего канала на ReflexViz!)")
    call process_character (n, appearance="outfit underwear pose handfist face neutral blush false", text="(Держу пари, что мы могли бы набить еще подписчиков, сделав это!)")
    call process_character (n, appearance="outfit underwear pose handfist face neutral blush false", text="...")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="(Надо написать [vicky.say_name], что я звйду к ней в офис сегодня!)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="\"Привет [vicky.say_name], круто слышать о веб-сайте!\"")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="\"Я могу приехать сегодня, если хочешь.\"")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="(И отослать!)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="...{p}...")
    "{i}Дзинь!{/i}"
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="(Вау, быстрый ответ...)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="\"Отлично!\"")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="\"Я прямо сейчас настраиваю камеру для записи.\"")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="\"Все будет готово к тому времени, как ты будешь здесь!\"")

    call fade_to_black (1)
    $ no_bust_art = True

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я с нетерпением ждала этого дня, [n.say_name].")
    call process_character (vicky, appearance="", text="Создание этого веб-сайта большой шагом вперед.")
    call process_character (n, appearance="blush false", text="Ты смогла сделать все это сама!")
    call process_character (n, appearance="blush false", text="Я даже не знал, что такое веб-дизайн.")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Это не так уж плохо, если у тебя есть время, чтобы изучить его.")
    call process_character (vicky, appearance="", text="К счастью, поскольку я работаю в основном дома, мне удалось собрать множество ресурсов по дизайну и управлению сайтом.")
    call process_character (vicky, appearance="", text="Это постоянный вызов - поддержка растущего веб-сайта, такого как мой, но мне нравится, что всегда есть способ сделать улучшения.")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Выигрыш для хорошо разработанного веб-сайта огромен.")
    call process_character (vicky, appearance="", text="Дать посетителям всё в одном портале с высококачественной порнографией - хорошая приманка.")

    if "sam_scene_vaginal_revisit" in scenes_completed:
        call process_character (n, appearance="blush false", text="Моей сестре [sa.say_name] очень понравится!")
        call process_character (vicky, appearance="", text="Я уверена, что да!")
        call process_character (vicky, appearance="", text="Ей не придётся тратить время в поисках нового, потому что все это будет прямо здесь!")
    else:
        call process_character (n, appearance="blush false", text="Я уверен, что людям это очень понравится!")
        call process_character (vicky, appearance="", text="Я тоже так думаю!")
        call process_character (vicky, appearance="", text="Им не нужно будет тратить время, пытаясь найти нужное видео, потому что все это будет прямо здесь!")

    call process_character (n, appearance="blush false", text="Я не могу дождаться записи этого приветственного сообщения для сайта!")
    call process_character (n, appearance="blush false", text="Ты собираешься разместить его везде?")
    call process_character (vicky, appearance="", text="Да, он будет распространен на всех основных платформах социальных сетей.")
    call process_character (vicky, appearance="", text="Все, что нам требуется, - чуточку заинтересовать людей, и это будет, как лавина!")
    call process_character (n, appearance="blush false", text="Где мы будем записывать видео?")
    call process_character (vicky, appearance="", text="Прямо здесь, в офисе.")
    call process_character (vicky, appearance="", text="У меня уже все камеры на месте!")
    call process_character (n, appearance="blush false", text="Их больше одной?")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Надо необходимо для видео.")
    call process_character (vicky, appearance="", text="Всё должно быть на профессиональном уровне.")
    call process_character (vicky, appearance="", text="Наличие одного угла обзора делает видео безвкусным.")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Очень важно, чтобы тот, кто смотрит видео, не пропустил ни одного действия!")
    call process_character (n, appearance="blush false", text="Действия?")
    call process_character (n, appearance="blush false", text="Но я думал, мы просто представим сайт и поговорим об этом.")
    call process_character (vicky, appearance="", text="О, да.")
    call process_character (vicky, appearance="", text="Но мы должны держать их внимание на протяжении всего видео.")

    call static_still_ctc ("bg vicky_sit_tease")

    call process_character (vicky, appearance="", text="И учитывая тематику нашего сайта...")
    call process_character (vicky, appearance="", text="Я думаю, что наш курс действий очевиден.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Мы будем трахаться и говорить о сайте одновременно?")
    call process_character (vicky, appearance="", text="Я буду вести большую часть разговоров.")
    call process_character (vicky, appearance="", text="Но не стесняйся, если захочешь вмешаться.")
    call process_character (vicky, appearance="", text="В твоём случае, впрочем, действия будут говорить громче, чем слова, хе-хе...")

    if "sam_scene_vaginal_revisit" in scenes_completed:
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Хорошо, что я привык трахаться с [sa.say_name] в то время как другие люди смотрят на нас онлайн...)")
        call process_character (n, appearance="blush false", text="(Это по сути то же самое)")
    else:
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Так много людей смогут посмотреть это видео онлайн)")
        call process_character (n, appearance="blush false", text="(Надеюсь, я не буду слишком нервничать во время записи...)")

    call process_character (vicky, appearance="", text="Всё готово, можем начинать?")
    call process_character (vicky, appearance="", text="Нам придется сделать это с первого дубля, но я всегда могу подредактировать любые ошибки.")
    call process_character (vicky, appearance="", text="Или, может быть, это сделает видео более аутентичным, если сохраним их...")
    call process_character (n, appearance="blush false", text="Да, я готов приступить к записи!")
    call process_character (vicky, appearance="", text="Позволь мне убедиться, что все камеры записывают!")

    call fade_to_black (1)

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Эта камера настроена...")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Эта тоже...")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Ладно, камеры работают!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Почему ты убираешь всё со стола, [vicky.say_name]?")
    call process_character (vicky, appearance="", text="Чтобы освободить место для нас.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Это значит...")
    call process_character (vicky, appearance="", text="Пришло время показать твою штуку, [n.say_name]!")
    call process_character (vicky, appearance="", text="Я наклонилась и приготовилась к твоему члену!")
    call process_character (n, appearance="blush false", text="Но я не могу дотянуться...")
    call process_character (n, appearance="blush false", text="Ты выше меня.")
    call process_character (vicky, appearance="", text="Подкати мой стул ко мне, чтобы ты мог подтянуться!")
    call process_character (n, appearance="blush false", text="О, да!")
    call process_character (n, appearance="blush false", text="Хорошая идея.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Вот, теперь ты на идеальной высоте!")
    call process_character (n, appearance="blush false", text="Вообще-то, я слишком высоко.")
    call process_character (n, appearance="blush false", text="Мне придется наклониться, чтобы трахнуть твою киску.")
    call process_character (n, appearance="blush false", text="Я должен опустить стул или...")
    call process_character (vicky, appearance="", text="А как насчет моей задницы?")
    call process_character (vicky, appearance="", text="Ты на нужной высоте для неё?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Да...{w=1.0} мой пенис смотрит прямо на неё.")
    call process_character (vicky, appearance="", text="Тогда я думаю, что это то, куда ты должен войти!")

    call static_still_ctc ("bg vicky_anal_probe")

    if stats.stat_value("times_given_anal_sex") > 0:
        call process_character (n, appearance="blush false", text="Действительно, я могу?")
        call process_character (vicky, appearance="", text="Моя задница полностью твоя.")
        call process_character (vicky, appearance="", text="Если только ты не чувствуешь, что тебе это не понравится...")
        call process_character (n, appearance="blush false", text="Нет, я бы с удовольствием!")
        call process_character (n, appearance="blush false", text="У меня не было возможности трахнуть тебя в задницу, [vicky.say_name]!")
        call process_character (vicky, appearance="", text="В твоём голосе слышится возбуждение от того, насколько твердым было это решение!")
        call process_character (vicky, appearance="", text="Теперь я заинтригована!")
        call process_character (vicky, appearance="", text="Устрой шоу моей заднице, [n.say_name]!")
    else:
        call process_character (n, appearance="blush false", text="Д-да?")
        call process_character (vicky, appearance="", text="Моя задница полностью твоя.")
        call process_character (vicky, appearance="", text="Если только ты не чувствуешь, что тебе это не понравится...")
        call process_character (n, appearance="blush false", text="Я никогда не трахался так раньше...")
        call process_character (vicky, appearance="", text="Ну, а теперь ты можешь попробовать!")
        call process_character (vicky, appearance="", text="По-моему, ты хорошо проведешь время.")
        call process_character (vicky, appearance="", text="Это может быть немного туго, но ощущения...")
        call process_character (vicky, appearance="", text="Ты поймёшь, когда надавишь!")


    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Хорошо, я готов!")
    call process_character (vicky, appearance="", text="Убедись, что ты сможете вставить его полностью!")
    call process_character (vicky, appearance="", text="Оседлай меня, если это поможет!")
    call process_character (n, appearance="blush false", text="Ах...")
    call process_character (n, appearance="blush false", text="Он проскользнул в твою задницу, [vicky.say_name]!")

    call static_still_ctc ("bg vicky_anal_behind")

    call process_character (vicky, appearance="", text="О, да, [n.say_name]!")
    call process_character (vicky, appearance="", text="Моя задница принимает весь твой член!")
    call process_character (vicky, appearance="", text="Начинай толкать свое тело!")
    call process_character (n, appearance="blush false", text="Вот так!")
    call process_character (n, appearance="blush false", text="Мм, Мм!")
    call process_character (n, appearance="blush false", text="Хорошо, [vicky.say_name]?")
    call process_character (vicky, appearance="", text="Да!")
    call process_character (vicky, appearance="", text="Это то, что я хочу, [n.say_name]!")
    call process_character (vicky, appearance="", text="Засунь в меня свой член!")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Теперь мне интересно, могу ли я сохранить самообладание для моей речи!)")
    call process_character (vicky, appearance="", text="([n.say_name] не собирается прекращать стучать в мою задницу в ближайшее время...)")
    call process_character (vicky, appearance="", text="(И я не хочу, чтобы он останавливался!)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я не думаю, что смогу следовать моему отрепетированному сценарию)")
    call process_character (vicky, appearance="", text="(Я просто сниму экспромтом и сделаю все, что смогу!)")

    call static_still_ctc ("bg vicky_anal_shirt")

    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (n, appearance="blush false", text="Ху, ах...")
    call process_character (vicky, appearance="", text="Я собираюсь начать приветственное сообщение, [n.say_name].")
    call process_character (n, appearance="blush false", text="П-понял.")
    call process_character (vicky, appearance="", text="{i}Кхм.{/i}..")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Привет всем и добро пожаловать на...{w=0.5}ах, Эмпорниум [vicky.say_name]!")
    call process_character (n, appearance="blush false", text="Мне нравится!")
    call process_character (n, appearance="blush false", text="Эмпорниум!")
    call process_character (vicky, appearance="", text="Хаха, [n.say_name] {i}тсс!{/i}")
    call process_character (vicky, appearance="", text="Пока придержи свои откровенные комментарии.")
    call process_character (vicky, appearance="", text="Я дам тебе знать, когда ты сможешь говорить.")
    call process_character (n, appearance="blush false", text="А, точно!")
    call process_character (n, appearance="blush false", text="Прости, [vicky.say_name]!")
    call process_character (n, appearance="blush false", text="Почему бы тебе не начать сначала?")
    call process_character (n, appearance="blush false", text="Я буду вести себя тихо.")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Привет, и добро пожаловать на мой сайт, Эмпорниум [vicky.say_name]!")
    call process_character (vicky, appearance="", text="Тебе очень повезло, что у тебя есть...{w=1.0}ой, молчу!")
    call process_character (vicky, appearance="", text="Я создаю обширную видеотеку, содержащую только самый лучший контент для взрослых для вашего удовольствия!")
    call process_character (n, appearance="blush false", text="([vicky.say_name] делает большую работу по продвижению сайта!)")
    call process_character (vicky, appearance="", text="Кроме того, вы сможете увидеть у меня, [vicky.say_name], и оригинальный контент, который я буду производить исключительно для Эмпорниума!")
    call process_character (vicky, appearance="", text="Ах...{w=1.0} в качестве специального превью вы смотрите одно из моих видео прямо сейчас!")
    call process_character (vicky, appearance="", text="Молодой человек, который отработает меня сзади, очень талантлив, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Хрм, ах...")
    call process_character (vicky, appearance="", text="Вместе, [n.say_name] и я будем поставлять вид порно, который вы захотите посмотреть!")
    call process_character (vicky, appearance="", text="Первые зарегистрированные получат специальную скидку на пожизненное членство!")
    call process_character (vicky, appearance="", text="[n.say_name], ты хочешь что-нибудь сказать?")

    call static_still_ctc ("bg vicky_anal_shirtpull")

    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (n, appearance="blush false", text="Я люблю трахать [vicky.say_name]!")
    call process_character (vicky, appearance="", text="[n.say_name], конечно...")
    call process_character (vicky, appearance="", text="Это и многое другое на Эмпорниум [vicky.say_name]!")
    call process_character (vicky, appearance="", text="Ммм!")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="И снято!")
    call process_character (n, appearance="blush false", text="С посланием покончено?")
    call process_character (vicky, appearance="", text="Все уже сделано!")
    call process_character (vicky, appearance="", text="Был ли толк в моём разговоре?")
    call process_character (n, appearance="blush false", text="Я думаю, ты отлично справился!")
    call process_character (vicky, appearance="", text="Это обнадеживает!")
    call process_character (vicky, appearance="", text="Трудно сосредоточиться, когда твою...{w=0.5}ах, задницу пялят!")
    call process_character (n, appearance="blush false", text="Д-да...{w=1.0}я едва могу сосредоточиться.")
    call process_character (n, appearance="blush false", text="Вот почему я не могла придумать, что сказать.")
    call process_character (vicky, appearance="", text="Все в порядке.")
    call process_character (vicky, appearance="", text="Это будет мощное приветственное видео сообщение для запуска с сайта!")
    call process_character (n, appearance="blush false", text="М-мы должны перестать трахаться после того, как ты все рассказала?")
    call process_character (vicky, appearance="", text="Нет!")
    call process_character (vicky, appearance="", text="Я никогда не брошу дело, не доделав его!")
    call process_character (vicky, appearance="", text="Мы пройдем весь путь до кульминации!")
    call process_character (vicky, appearance="", text="Сделаем ещё несколько крутых вставок и дополнительных кадров!")
    call process_character (n, appearance="blush false", text="(Да!)")
    call process_character (n, appearance="blush false", text="(Мы будем продолжать!)")

    call static_still_ctc ("bg vicky_anal_fuck")

    call process_character (vicky, appearance="", text="Ох, ох!")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="([n.say_name] втягивается в это!)")
    call process_character (vicky, appearance="", text="(Он очень рад, что мы продолжаем!)")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Его бедра бьются о мою задницу)")
    call process_character (vicky, appearance="", text="Да, ах!")
    call process_character (vicky, appearance="", text="(Мой стол весь трясётся!)")
    call process_character (n, appearance="blush false", text="Ммф...")
    call process_character (n, appearance="blush false", text="(Я не могу помочь, но трахаю [vicky.say_name] так быстро, как могу!)")
    call process_character (n, appearance="blush false", text="(Ее попка сжимает мой член!)")
    call process_character (n, appearance="blush false", text="(Так сильно сдавливает!)")
    call process_character (vicky, appearance="", text="Ах да, [n.say_name]...")
    call process_character (vicky, appearance="", text="Мы будем снимать отличные видео вместе.")
    call process_character (vicky, appearance="", text="Эмпорниум [vicky.say_name] будет иметь огромный успех, я уверена!")
    call process_character (vicky, appearance="", text="Мы достигнем такого уровня качества, с которым не сможет соперничать ни один конкурент.")
    call process_character (vicky, appearance="", text="Перед тобой светлое деловое будущее, [n.say_name].")
    call process_character (vicky, appearance="", text="Ты трахаешься и зарабатываешь деньги...")
    call process_character (vicky, appearance="", text="Это идеальная работа для тебя, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Это действительно звучит идеально...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я не могу дождаться, чтобы сделать больше этого, [vicky.say_name].")
    call process_character (vicky, appearance="", text="Нам есть над чем поработать.")
    call process_character (vicky, appearance="", text="Мы будем заниматься этим долгое время.")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (n, appearance="blush false", text="Я хочу попробовать все!")
    call process_character (n, appearance="blush false", text="До тех пор, пока тебе нравится!")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Он позволяет сексу диктовать большинство своих мыслей прямо сейчас...)")
    call process_character (vicky, appearance="", text="(Но я не сомневаюсь, что он искренен)")
    call process_character (n, appearance="blush false", text="Хаах!")
    call process_character (n, appearance="blush false", text="Я собираюсь кончить, [vicky.say_name], я кончаю!")
    call process_character (vicky, appearance="", text="Это будут хорошие кадры, [n.say_name]!")
    call process_character (vicky, appearance="", text="Центр внимания находится под тобой!")
    call process_character (n, appearance="blush false", text="Хррм!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg vicky_anal_behind_cum")

    call process_character (vicky, appearance="", text="Ооох!")
    call process_character (vicky, appearance="", text="(У меня пальцы скручиваются!)")
    call process_character (vicky, appearance="", text="(И мои ноги трясутся!)")
    call process_character (n, appearance="blush false", text="Ух, ух!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Только ты можешь довести меня до такого оргазма, [n.say_name].")
    call process_character (vicky, appearance="", text="Я не знаю, как ты это делаешь, но ты действительно можешь дать это женщине.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я тоже не уверен, что знаю...")
    call process_character (vicky, appearance="", text="Важен только конечный результат.")
    call process_character (n, appearance="blush false", text="Что с видео, получилось?")
    call process_character (vicky, appearance="", text="Мы не смогли бы сделать его лучше.")
    call process_character (vicky, appearance="", text="Я уверена, что это будет хоум-ран для сайта!")
    call process_character (vicky, appearance="", text="Видео нуждается в небольшом редактировании и полировке, и после этого оно будет завершено!")
    call process_character (n, appearance="blush false", text="Круто!")
    call process_character (n, appearance="blush false", text="Можешь прислать мне, когда закончишь?")
    call process_character (vicky, appearance="", text="Я буду более чем счастлива!")
    call process_character (vicky, appearance="", text="Я не могу дождаться, чтобы увидеть, как мы смотримся на камере со всех ракурсов!")

    python:
        vicky.revistable_scenes.add("vicky_scene_anal_revisit")

        if not dream:
            minigame_typing_money_earned_since_last_vicky_meeting = 0
            minigame_typing_times_succeeded_since_last_vicky_meeting = 0
            
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_seen_butt", 1)
            stats.add_stat("times_seen_butthole", 1)
            stats.add_stat("times_given_anal_sex", 1)
            stats.add_stat("times_given_anal_creampie", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("vicky_scene_anal", char=vicky, dream=dream)

    return

label vicky_scene_anal_revisit:
    $ no_bust_art = False

    if "vicky_scene_anal_revisit" in scenes_completed:
        call vicky_scene_anal_revisit_2nd_time
    else:
        call vicky_scene_anal_revisit_1st_time

    return

label vicky_scene_anal_revisit_1st_time:
    $ no_bust_art = True

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Ха-ха, и это сразу после того, как я разобралась и вычистила всё здесь!")
    call process_character (vicky, appearance="", text="Мне нужно купить реквизиторский стол для нас!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я помогу вернуть всё на свои места.")
    call process_character (vicky, appearance="", text="Это не имеет большого значения, но спасибо за предложение помочь!")
    call process_character (vicky, appearance="", text="В конце концов мне все равно придется часто чистить свой стол.")
    call process_character (vicky, appearance="", text="Там куча всякого рода заметок, бумаг и прочего хлама.")
    call process_character (n, appearance="blush false", text="Понятно.")
    call process_character (n, appearance="blush false", text="Моя мама заставляет меня убираться дома.")
    call process_character (vicky, appearance="", text="Хорошо, что она учит тебя быть аккуратным и организованным.")
    call process_character (vicky, appearance="", text="Это может показаться скучным и трудным, но сэкономит массу времени, чтобы иметь упорядоченный стол.")
    call process_character (vicky, appearance="", text="В любом случае...")

    $ play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg vicky_sit_tease")

    call process_character (vicky, appearance="", text="Давай вернемся к тому, что мы будем делать...")

    call static_still_ctc ("bg vicky_anal_probe")

    call process_character (vicky, appearance="", text="Ты помнишь каждую мелочь, не так ли?")
    call process_character (n, appearance="blush false", text="Хм?")
    call process_character (vicky, appearance="", text="Надо подготовиться, как и в первый раз, когда трахнул меня в задницу!")
    call process_character (n, appearance="blush false", text="А, ну да...")
    call process_character (n, appearance="blush false", text="У меня довольно хорошая память, ну так мне говорит моя семья.")
    call process_character (vicky, appearance="", text="Моя не самая лучшая, так что я должна быть великолепна в планировании.")
    call process_character (vicky, appearance="", text="Когда ты управляешь бизнесом, ты не можешь просто плыть по течению.")
    call process_character (vicky, appearance="", text="Если ты это сделаешь, это будет означать катастрофу.")

    call static_still_ctc ("bg vicky_anal_behind")

    call process_character (n, appearance="blush false", text="Аах, оох...")
    call process_character (n, appearance="blush false", text="Это было потрясающе, когда мой член впервые вошёл в твою задницу, [vicky.say_name].")
    call process_character (vicky, appearance="", text="Ммм, у тебя есть эта теплая дрожь по всему телу?")
    call process_character (vicky, appearance="", text="Вот что со мной происходит.")
    call process_character (n, appearance="blush false", text="Это похоже на теплую дрожь, да!")
    call process_character (n, appearance="blush false", text="И становится все теплее и теплее!")
    call process_character (vicky, appearance="", text="Тепло наших тел увеличивает температуру в офисе на несколько градусов к тому времени, как заканчиваем!")

    call static_still_ctc ("bg vicky_anal_shirt")

    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (vicky, appearance="", text="Я собрала кадры из нашего приветственного послания.")
    call process_character (vicky, appearance="", text="Есть много хороших!")
    call process_character (n, appearance="blush false", text="Это займет какое-то время?")
    call process_character (vicky, appearance="", text="Может быть...")
    call process_character (vicky, appearance="", text="Но я хочу выбрать только лучшие фрагменты для видео.")
    call process_character (vicky, appearance="", text="Я могу собрать сокращенную версию, а затем более длинную, более полную версию.")
    call process_character (vicky, appearance="", text="Лучше дразнить людей быстрыми фрагментами полной версии.")
    call process_character (n, appearance="blush false", text="Каким будет наше следующее видео?")
    call process_character (vicky, appearance="", text="Я обязательно повторю все это с тобой в другой раз.")
    call process_character (vicky, appearance="", text="Я подготовила таблицу с подробным расписанием.")
    call process_character (vicky, appearance="", text="Ты будешь занятым парнем, [n.say_name]!")
    call process_character (n, appearance="blush false", text="А, когда я вернусь в школу?")
    call process_character (vicky, appearance="", text="Я уже учла.")
    call process_character (vicky, appearance="", text="Это не нарушит твой образовательный процесс.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Будут ли выходные?")
    call process_character (n, appearance="blush false", text="Мне нравится в свободное время играть в видеоигры.")
    call process_character (vicky, appearance="", text="Ха, конечно!")
    call process_character (vicky, appearance="", text="Мы со всем этим разберемся.")
    call process_character (vicky, appearance="", text="Помни, что мы полностью контролируем, когда и как мы работаем, [n.say_name]!")
    call process_character (vicky, appearance="", text="В этом-то и вся прелесть!")

    call static_still_ctc ("bg vicky_anal_shirtpull")

    call process_character (n, appearance="blush false", text="Мне это очень нравится.")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="Эй, мне было любопытно, [n.say_name]...")
    call process_character (vicky, appearance="", text="Ты случайно не знаешь девушек, которые могут захотеть сняться в некоторых видео?")
    call process_character (n, appearance="blush false", text="Знаю ли я кого-нибудь?")
    call process_character (vicky, appearance="", text="Если не скажешь, это нормально.")
    call process_character (vicky, appearance="", text="Сейчас я ищу любых потенциальных женщин, которые хотят работать с вами на видео.")

    call static_still_ctc ("bg vicky_anal_fuck")

    call process_character (n, appearance="blush false", text="Р-работать со мной?")
    call process_character (n, appearance="blush false", text="Но, а что насчет тебя?")
    call process_character (vicky, appearance="", text="Ох, я все равно буду много работать с тобой, [n.say_name], хаха!")
    call process_character (vicky, appearance="", text="Но для некоторых видео я хотела бы быть за камерой, и иметь немного больше контроля над композицией.")
    call process_character (vicky, appearance="", text="Как я уже сказала, если ты не знаешь, это не имеет большого значения.")
    call process_character (vicky, appearance="", text="Это значит больше экранного времени для нас с тобой!")
    call process_character (n, appearance="blush false", text="...")

    $ fucked_amount = girls_fucked_amount() - 1
    if fucked_amount >= 3:
        call process_character (n, appearance="blush false", text="Я знаю нескольких девушек, которые могут быть заинтересованы...")
        call process_character (vicky, appearance="", text="Правда?")
        call process_character (vicky, appearance="", text="Несколько девочек, [n.say_name]?")
        call process_character (n, appearance="blush false", text="...")
        call process_character (vicky, appearance="", text="Вообще-то, я не должна так удивляться.")
        call process_character (vicky, appearance="", text="У тебя есть определенный шарм, который притягивает женщин.")
        call process_character (n, appearance="blush false", text="Ты так думаешь?")
        call process_character (vicky, appearance="", text="Я бы сказала, что ты магнит для цыпочек!")
        call process_character (vicky, appearance="", text="Который идеально подходит для нас, чтобы привлечь новых талантов для работы на сайте!")
    elif fucked_amount >= 2:
        call process_character (n, appearance="blush false", text="Я знаю пару девушек, которые могут быть заинтересованы...")
        call process_character (vicky, appearance="", text="Парочка?")
        call process_character (vicky, appearance="", text="Надеюсь, ты не устраиваешь двойные свидания, ха-ха!")
        call process_character (n, appearance="blush false", text="...")
        call process_character (vicky, appearance="", text="Я просто прикалываюсь.")
        call process_character (vicky, appearance="", text="Это здорово!")
        call process_character (vicky, appearance="", text="Спроси их обеих, готовы ли они встать перед камерой.")
        call process_character (vicky, appearance="", text="Скажи им, что хорошо залатят!")
    elif fucked_amount == 1:
        call process_character (n, appearance="blush false", text="Я знаю одну девушку...")
        call process_character (vicky, appearance="", text="Одна, вполне приемлемо!")
        call process_character (vicky, appearance="", text="У меня было предчувствие, что ты знаешь больше девушек, чем только меня.")
        call process_character (n, appearance="blush false", text="...")
        call process_character (vicky, appearance="", text="Я бы очень хотела с ней поговорить!")
        call process_character (vicky, appearance="", text="Если ты думаешь, что ей будет удобно перед камерой, попроси ее связаться со мной!")
        call process_character (vicky, appearance="", text="Напомни мне дать тебе пару визиток перед уходом.")
    else:
        call process_character (n, appearance="blush false", text="Я не знаю девушек, которые бы заинтересовались.")
        call process_character (n, appearance="blush false", text="Прости, [vicky.say_name].")
        call process_character (vicky, appearance="", text="Не нужно извиняться, [n.say_name]!")
        call process_character (vicky, appearance="", text="Ты и я более чем способны сделать большинство видео вместе!")
        call process_character (vicky, appearance="", text="Есть также много способов для нас, чтобы получить некоторых дополнительных женщин.")
        call process_character (vicky, appearance="", text="Я знаю, что мы получим много предложений, если я опубликую твою фотографию и скажу, что ты будешь работать с ними!")
        call process_character (n, appearance="blush false", text="...")
        call process_character (vicky, appearance="", text="Многие женщины найдут тебя милым, [n.say_name], и это заинтересует их больше.")

    if "sam_scene_vaginal_revisit" in scenes_completed:
        call process_character (vicky, appearance="", text="[sa.say_name] одна из девушек, [n.say_name]?")
        call process_character (n, appearance="blush false", text="Да, это так.")
        call process_character (vicky, appearance="", text="Тогда я точно знаю, что она это сделает!")
        call process_character (vicky, appearance="", text="Она имеет больше опыта, чем я!")
    elif fucked_amount == 1 and "sam_scene_vaginal" in scenes_completed:
        call process_character (vicky, appearance="", text="Подожди, [sa.say_name] это девушка, о которой ты говоришь, [n.say_name]?")
        call process_character (n, appearance="blush false", text="Да, это так.")
        call process_character (vicky, appearance="", text="Тогда я точно знаю, что она это сделает!")
        call process_character (vicky, appearance="", text="Она имеет больше опыта, чем я!")

    call process_character (n, appearance="blush false", text="Ах!")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (n, appearance="blush false", text="Я собираюсь кончить, [vicky.say_name]!")
    call process_character (vicky, appearance="", text="Мы были так увлечены обсуждением, что я почти забыла, что ты трахал мою задницу все это время!")
    call process_character (n, appearance="blush false", text="Хуу!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg vicky_anal_behind_cum")

    call process_character (vicky, appearance="", text="Это хорошая горячая сперма, [n.say_name]!")
    call process_character (vicky, appearance="", text="Ах, да...")
    call process_character (n, appearance="blush false", text="{i}Фью.{/i}..")
    call process_character (vicky, appearance="", text="Не останавливайся, пока что, [n.say_name]!")
    call process_character (vicky, appearance="", text="Трахай мою задницу!")
    call process_character (n, appearance="blush false", text="Даже после того, как я кончил в неё?")
    call process_character (vicky, appearance="", text="Я хочу твой член еще один раз!")

    call vicky_scene_anal_revisit_end

    return

label vicky_scene_anal_revisit_2nd_time:
    $ no_bust_art = True
    $ play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg vicky_anal_shirtpull")

    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Я должна просто принять это...)")
    call process_character (vicky, appearance="", text="(Когда рядом [n.say_name], я не могу не превращаться в сумасшедшую шлюху)")
    call process_character (vicky, appearance="", text="(В любое другое время, я была бы профессиональной деловой женщиной)")
    call process_character (vicky, appearance="", text="(Хорошо, что я могу разделить это поведение)")
    call process_character (vicky, appearance="", text="(Слава богу, у меня больше нет клиентов, приходящих в офис)")
    call process_character (vicky, appearance="", text="(На днях я заметила, что на поверхности моего стола было высохшее пятно спермы!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Интересно, сколько видео [vicky.say_name] и я в конечном итоге сделаем?)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я надеюсь, что сможем сделать некоторые крутые, поскольку наш бюджет растет!)")
    call process_character (n, appearance="blush false", text="(Было бы здорово, если будем использовать фэнтезийные тематические штуки!)")
    call process_character (n, appearance="blush false", text="([vicky.say_name] может быть волшебницей, а я могу быть ее учеником или кем-то еще!)")
    call process_character (n, appearance="blush false", text="(Ох, чувак, теперь, когда я думаю об этом, есть так много классных вещей, которые мы могли бы сделать!)")
    call process_character (n, appearance="blush false", text="(Это будет потрясающе!)")
    call process_character (vicky, appearance="", text="Кстати, [n.say_name]...")
    call process_character (vicky, appearance="", text="Если у тебя есть какие-либо идеи для видео, дай мне знать, чтобы я могла записать их.")
    call process_character (n, appearance="blush false", text="Вообще-то, я как раз думал о некоторых!")
    call process_character (vicky, appearance="", text="Отлично!")
    call process_character (vicky, appearance="", text="Если мы получим достаточно большой список, мы можем оценить лучшие концепции и поставить их на первое место!")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", yalign = 0.1)
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
    call process_character (vicky, appearance="", text="Сильнее [n.say_name], быстрее!")
    call process_character (vicky, appearance="", text="...")
    call process_character (vicky, appearance="", text="(Мои соски тверды как камень!)")
    call process_character (vicky, appearance="", text="(Клянусь, они могли бы проделать дырку в столе.)")

    call static_still_ctc ("bg vicky_anal_behind_cum")

    call process_character (n, appearance="blush false", text="Ннг!")
    call process_character (vicky, appearance="", text="{i}Ухх!{/i}")
    call process_character (vicky, appearance="", text="Кончи так глубоко, как сможешь, [n.say_name]!")

    call vicky_scene_anal_revisit_end

    return

label vicky_scene_anal_revisit_end:

    python:
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_seen_butt", 1)
        stats.add_stat("times_seen_butthole", 1)
        stats.add_stat("times_given_anal_sex", 1)
        stats.add_stat("times_given_anal_creampie", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)


    call process_end_of_scene ("vicky_scene_anal_revisit", char=vicky, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return