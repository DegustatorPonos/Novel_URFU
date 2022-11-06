label sam_convo_default:
    call process_conversation_beginning ([ (n, ""), (sa, "") ])

    call debug_message ("Default conversation when none others are available.")
    $ sa.c("Привет " + n.say_name + ".")

    call process_end_of_conversation ("sam_convo_default", sa, priority=False, default=True)

    return

label minigame_math_first_time_intro:
    call process_conversation_beginning ([ (n, ""), (sa, "pose handsbehind face neutral") ])

    call process_character (sa, appearance="pose handsbehind face neutral", text="Мама хочет, чтобы мы практиковались в математике.")

    call process_character (n, appearance="pose handpocket face concerned", text="(Вздыхает) {p=1.0}Я понял...")
    call process_character (n, appearance="pose handpocket face concerned", text="Кажется, ты не слишком беспокоишься об этом.")
    call process_character (sa, appearance="pose handface face happy", text="Это будет очень просто!")
    call process_character (n, appearance="pose behindhead face neutral", text="Хотел бы быть таким же самоуверенным.")
    call process_character (n, appearance="pose behindhead face neutral", text="Как это может быть легко?")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Подумай об этом, [n.say_name]!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Мы играем в эти RPG игры, которые показывают все виды чисел! Вроде урона, защиты, регена, удачи...")
    call process_character (n, appearance="pose handpocket face neutral", text="Да? И что?")
    call process_character (sa, appearance="pose leaning face neutral", text="Мы занимались математикой всё это время, играя в видеоигры!")
    call process_character (sa, appearance="pose leaning face neutral", text="Мы вычитаем, складываем, умножаем и даже делим.")
    call process_character (sa, appearance="pose leaning face neutral", text="У нас не должно быть проблем с этим!")
    call process_character (n, appearance="pose handpocket face curious", text="Думаю, стоит попробовать.")
    call process_character (n, appearance="pose handpocket face curious", text="Но могу ли я выбрать {b}сложность{/b} вопросов?")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Почему бы и нет.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="{i}Но было бы круто, если бы ты ответил на сложные математические вопросы.{/i}")
    $ renpy.pause(0.5)
    call process_character (sa, appearance="pose handsbehind face neutral", text="Дай мне знать, когда захочешь попробовать ответить на некоторые из них!")


    call process_end_of_conversation ("minigame_math_first_time_intro", sa, priority=False, considered_scene=True, override_scene_limit=True)

    return


label sam_convo_1:
    call process_conversation_beginning ([ (n, ""), (sa, "pose handsbehind") ])

    call process_character (sa, appearance="pose handsbehind face neutral", text="Я как раз собиралась опубликовать наш обзор Цельнометаллического чародея.")
    call process_character (n, appearance="pose handpocket face neutral", text="Уже почти закачалось на [video_sharing_site]?")
    call process_character (sa, appearance="pose leaning face neutral", text="О, да.")
    call process_character (sa, appearance="pose leaning face neutral", text="Я попыталась подражать некоторым техникам монтажа из каналов, которые нам нравятся.")
    call process_character (n, appearance="pose handpocket face neutral", text="Как у \"Канала Впечатлений.\"?")
    call process_character (sa, appearance="pose leaning face happy", text="Да вроде быстрых обзоров \"Возмущённого Йена\".")
    call process_character (n, appearance="pose handfist face happy", text="Мило.")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (sa, appearance="pose handface face neutral", text="Нам придется составить расписание.")
    call process_character (sa, appearance="pose handface face neutral", text="Мы не можем просто беспорядочно загружать новое видео здесь и там.")
    call process_character (n, appearance="pose handpocket face neutral", text="Правильно.")
    call process_character (sa, appearance="pose leaning face neutral", text="Я думаю, чтобы было больше просмотров, мы должны переключаться между обзорами игр и фильмов.")
    call process_character (n, appearance="pose handpocket face neutral", text="У тебя уже есть что-нибудь на примете?")
    call process_character (sa, appearance="pose handface face neutral", text="Ну, новая игра \"Твистер Душ\" отличный выбор.")
    call process_character (sa, appearance="pose handface face neutral", text="Нам придется сыграть в него еще не раз, прежде чем мы сможем дать ему надлежащий обзор.")

    call process_end_of_conversation ("sam_convo_1", sa, priority=False, default=False)


    return

label sam_convo_2:
    call process_conversation_beginning ([ (n, ""), (sa, "pose handface") ])

    call process_character (sa, appearance="pose handface face neutral", text="Одно скажу о нашем новом доме:")
    call process_character (sa, appearance="pose handface face happy", text="У него сумасшедший быстрый интернет!")
    call process_character (n, appearance="pose handpocket face neutral", text="Да ну?")
    call process_character (sa, appearance="pose leaning face happy", text="Я могу загружать видео на [video_sharing_site] намного быстрее, чем раньше.")
    call process_character (n, appearance="pose handpocket face curious", text="Загружать?")
    call process_character (sa, appearance="pose handsbehind face neutral", text="О, это когда вы берете файл со своего компьютера и помещаете его на веб-сайт, например, [video_sharing_site].")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Так что другие люди могут увидеть его!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Между тем загрузка, пока ты...")
    call process_character (n, appearance="pose behindhead face neutral", text="Можно ли получить файл на компьютере с [video_sharing_site]?")
    call process_character (sa, appearance="pose handsbehind face happy", text="Да, конечно!")
    call process_character (sa, appearance="pose handsbehind face happy", text="Мы также можем транслировать в ФуллХД.")
    call process_character (sa, appearance="pose handsbehind face happy", text="Таким образом, люди могут смотреть игру и нас чётко и без задержек.")

    call process_end_of_conversation ("sam_convo_2", sa, priority=False, default=False)

    return

label sam_convo_3:
    call process_conversation_beginning ([ (n, ""), (sa, "pose handface face concerned") ])
    call process_character (sa, appearance="pose handface face concerned", text="Я не жду начала учёбы.")
    call process_character (n, appearance="pose behindhead face neutral", text="Да, приятно расслабиться и отвлечься от учебы.")
    call process_character (sa, appearance="pose handface face concerned", text="Дело не столько в этом.")
    call process_character (sa, appearance="pose handface face curious", text="Я имею в виду, что она раздражает, не пойми меня неправильно.")
    call process_character (sa, appearance="pose handface face concerned", text="Я хочу уделить, как можно больше времени [video_sharing_site] каналу.")
    call process_character (n, appearance="pose handfist face neutral", text="Ах, да.")
    call process_character (n, appearance="pose handfist face neutral", text="Ну, мы всё сможем, если будем делать вместе.")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Похоже, {p=1.0}я уже знаю, чем хочу заниматься в будущем.")
    call process_character (sa, appearance="pose handsbehind face happy", text="И это быть успешным на [video_sharing_site].")
    call process_character (n, appearance="pose handpocket face neutral", text="Это было бы замечательно.")
    call process_character (n, appearance="pose behindhead face neutral", text="Может быть, мы сможем распространить информацию о нашем канале в школе.")
    call process_character (sa, appearance="pose handface face curious", text="Точно.")
    call process_character (sa, appearance="pose handface face curious", text="Да...")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose leaning face neutral", text="На самом деле, это отличная идея!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Да?")
    call process_character (sa, appearance="pose leaning face happy", text="Если они распространят информацию в интернете, мы получим много подписчиков!")


    call process_end_of_conversation ("sam_convo_3", sa, priority=False, default=False)

    return

label sam_convo_4:
    call process_conversation_beginning ([ (n, ""), (sa, "pose handsbehind") ])
    call process_character (sa, appearance="pose handsbehind face neutral", text="Мама говорит, что мы оба похожи по фигуре.")
    call process_character (n, appearance="pose handpocket face neutral", text="Она действительно часто так говорит.")
    call process_character (sa, appearance="pose handsbehind face curious", text="Я никогда не думала об этом, но я думаю, это правда.")

    call process_character (n, appearance="pose handpocket face curious", text="У мамы и бабушки одинаковая фигура.")
    call process_character (sa, appearance="pose handface face neutral")
    $ sa.c("А тётушка и " + k.say_name + " очень похожи.")
    call process_character (n, appearance="pose behindhead face curious", text="Но раньше она была похожа на маму.")
    call process_character (sa, appearance="pose handface face neutral", text="Это правда.")
    call process_character (sa, appearance="pose handface face neutral")
    $ sa.c("Я думаю, что " + k.say_name + " вдохновила ее начать тренироваться, и она нарастила мускулы.")
    call process_character (n, appearance="pose handpocket face neutral", text="Мама говорит, что мы близнецы.")
    call process_character (n, appearance="pose handpocket face curious", text="Но разве близнецы не должны выглядеть одинаково?")
    call process_character (sa, appearance="pose handface face neutral", text="Ой! {p=1.0}Думаю, мама однажды ответила мне на этот вопрос.")
    call process_character (sa, appearance="pose leaning face neutral", text="Она сказала, что мы \"двуяйцевые\" близнецы, вроде так.")
    call process_character (n, appearance="pose behindhead face curious", text="Двуяйцевые близнецы?")
    call process_character (sa, appearance="pose handface face neutral", text="Да, думаю, двуяйцевые близнецы могут выглядеть совершенно по-разному.")
    call process_character (sa, appearance="pose handface face neutral", text="Но у нас одинаковый цвет глаз.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="И мы оба одного роста.")
    call process_character (n, appearance="pose handpocket face embarrassed", text="Эй! \nЯ немного выше.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Вполне справедливо.")
    call process_character (sa, appearance="pose leaning face happy", text="Но ненамного!")

    call process_end_of_conversation ("sam_convo_4", sa, priority=False, default=False)

    return

label sam_convo_5:
    call process_conversation_beginning ([ (n, ""), (sa, "pose handface face neutral") ])
    call process_character (sa, appearance="pose handface face neutral", text="Я не раз думала, а не поспать ли в твоей комнате.")
    call process_character (n, appearance="pose handpocket face neutral", text="Это еще почему?")
    call process_character (sa, appearance="pose handsbehind face concerned", text="Ну это просто… {p=1.0}Странно больше не делить одну комнату.")
    call process_character (n, appearance="pose handpocket face neutral", text="По крайней мере, мы рядом.")
    call process_character (sa, appearance="pose handface face concerned", text="Да… {p=1.0}Но я задумываюсь об этом.")
    call process_character (sa, appearance="pose handface face concerned", text="И я так привыкла, что ты всегда рядом со мной.")
    call process_character (n, appearance="pose behindhead face neutral", text="Иногда это действительно странно.")
    call process_character (sa, appearance="pose leaning face neutral", text="Я даже иногда переворачиваюсь, чтобы поболтать с тобой ночью.")
    call process_character (sa, appearance="pose leaning face neutral", text="Чтобы задать вопрос или ещё что.")
    call process_character (n, appearance="pose twohandfist face neutral", text="Да без проблем, приходи ко мне спать.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Спасибо!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Я так стараюсь привыкнуть к своей комнате.")
    call process_character (sa, appearance="pose leaning face happy", text="Но я рада, что могу приходить к тебе в любое время!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Для тебя тоже всегда открыта дверь!")
    call process_character (sa, appearance="pose handsbehind face happy", text="Я имею в виду, что ты можешь видеть меня, когда угодно. {p=1.0}И ночью тоже.")
    call process_character (n, appearance="pose behindhead face neutral", text="О, хорошо.")
    call process_character (n, appearance="pose behindhead face neutral", text="Звучит неплохо.")

    call process_end_of_conversation ("sam_convo_5", sa, priority=False, default=False)

    return


label sam_convo_6:
    call process_conversation_beginning ([ (n, ""), (sa, "pose leaning face happy") ])
    call process_character (sa, appearance="pose leaning face happy", text="Люди снова пересматривают наш первый стрим!")
    call process_character (n, appearance="pose twohandfist face happy", text="Да ну? Круто!")
    call process_character (sa, appearance="pose handface face neutral", text="Некоторые смотрят его снова и снова.")
    call process_character (sa, appearance="pose handface face neutral", text="Они указывают на мелочи, которые мы не заметили.")
    call process_character (n, appearance="pose handpocket face neutral", text="Не удивительно.")
    call process_character (n, appearance="pose behindhead face neutral", text="Мы тоже пересматриваем наших любимых стримеров.")
    call process_character (sa, appearance="pose handface face neutral", text="Ты знаешь, один парень, \"Каскад Дронов\", указал на что-то смешное.")
    call process_character (n, appearance="pose handpocket face neutral", text="На что?")
    call process_character (sa, appearance="pose leaning face neutral", text="Он сказал, что когда мы приближались к концу стрима, мы начали смотреть друг на друга.")
    call process_character (sa, appearance="pose leaning face happy", text="И каждый из нас был немного в отключке, я думаю, ха-ха.")

    menu:
        "Мы, наверное, устали.":
            call add_points (sa, 1, tag="sam_convo_6_zone_out")
        "Я не думаю, что я смотрел на тебя так долго.":
            call add_boldness (1, tag="sam_convo_6_zone_out")
            call process_character (n, appearance="pose handpocket face curious")
            call process_character (sa, appearance="pose leaning face concerned blush true", text="...")
            call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Эх, эм, в смысле, {p=0.5}Это было забавно!")
            call process_character (sa, appearance="pose leaning face concerned blush true", text="Ага...")
            $ renpy.pause(1)

    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Но это не помешало мне победить этого элементального босса!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Верно, ты избила этого босса прямо во время стрима!")
    call process_character (sa, appearance="pose handface face neutral", text="В следующем стриме мы сразимся с ледяным элементалем!")
    call process_character (sa, appearance="pose handface face happy", text="Но не раньше, чем я найду этот загадочный заколдованный посох!")

    call process_end_of_conversation ("sam_convo_6", sa, priority=True, default=False, considered_scene=True)

    return


label sam_convo_7:
    call process_conversation_beginning ([ (n, ""), (sa, "pose handface face curious") ])
    $ sa.c(n.say_name + "...")
    $ renpy.pause(2)
    call process_character (sa, appearance="pose handface face curious", text="Это странно, иметь пенис?")
    call process_character (n, appearance="pose behindhead face curious", text="Что ты имеешь в виду?")
    call process_character (sa, appearance="pose handface face curious", text="Ну… {p=1.0}Похоже, что он просто болтается у тебя между ног.")
    call process_character (sa, appearance="pose handface face curious", text="Разве он не будет качаться туда-сюда?")
    call process_character (n, appearance="pose behindhead face neutral", text="Я думаю, я никогда не думал об этом раньше.")
    call process_character (n, appearance="pose behindhead face neutral", text="Но он не болтается так сильно, когда я ношу нижнее белье.")
    call process_character (sa, appearance="pose handface face concerned", text="Ты не боишься, что сядешь на него и раздавишь?")
    call process_character (n, appearance="pose handpocket face neutral", text="Думаю, тебе просто нужно быть осторожным.")
    call process_character (sa, appearance="pose handface face curious", text="Твой пенис всегда мягкий и хлюпающий, как тогда?")
    call process_character (n, appearance="pose behindhead face embarrassed", text="Н-не всегда...")
    call process_character (sa, appearance="pose handface face neutral", text="Правда?")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose handface face neutral", text="Что происходит?")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Иногда он становится твёрдым.")
    call process_character (sa, appearance="pose handface face neutral", text="Ого...")
    $ renpy.pause(2)
    call process_character (sa, appearance="pose leaning face neutral", text="Становится таким твёрдым, что можно что-то им сломать?")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Я так не думаю...")
    call process_character (sa, appearance="pose handface face curious", text="Знаешь, почему он становится твёрдым?")
    call process_character (n, appearance="pose behindhead face neutral", text="Нуу...")
    $ renpy.pause(1)

    menu:
        "У-у меня встал, когда я увидел твою вагину.":
            call add_points_and_boldness (sa, 1, 1, tag="sam_convo_7_why_hard")
            call process_character (n, appearance="pose behindhead face curious blush true")
            call process_character (sa, appearance="pose handface face concerned blush true", text="...{p=1.0}...")
            $ renpy.pause(1)
            call process_character (sa, appearance="pose handface face curious blush false", text="Хм… интересно...")
        "Я не совсем уверен...":
            call process_character (n, appearance="pose behindhead face neutral blush true", text="Я думаю, это связано с тем, что мы обнимались в нижнем белье...")
            call process_character (sa, appearance="pose handface face curious blush false", text="Хм...{w=1.0}интересно...")
            call process_character (sa, appearance="pose leaning face neutral", text="Ну, я уверена, что мы сможем это выяснить!")


    call process_character (n, appearance="pose handpocket face neutral blush false")
    call process_character (sa, appearance="pose leaning face neutral", text="Но это супер круто, он может стать твёрдым!")
    call process_character (sa, appearance="pose handface face neutral", text="В смысле, если бы у меня был пенис...")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose handface face happy", text="Я хотела бы ходить вокруг и тыкать в людей им!")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Что?")


    call process_end_of_conversation ("sam_convo_7", sa, priority=True, default=False, considered_scene=True)

    return

label sam_convo_8:
    call process_conversation_beginning ([ (n, ""), (sa, "pose handface face neutral") ])
    call process_character (sa, appearance="pose handface face neutral", text="Мы должны добавить кнопку пожертвования на нашем стриме.")
    call process_character (n, appearance="pose behindhead face neutral", text="Для чего?")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Для покупки разных вещей!")
    call process_character (sa, appearance="pose handsbehind face happy", text="Много блестящих, новых вещей!")
    call process_character (n, appearance="pose handpocket face neutral", text="Значит, мы сможем что-то купить?")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Не просто какие-то вещи!")
    call process_character (sa, appearance="pose leaning face neutral", text="Новые видеоигры, консоли, современные компьютеры.")
    call process_character (sa, appearance="pose leaning face neutral", text="Черт, если мы получим достаточно пожертвований...")
    call process_character (sa, appearance="pose leaning face neutral", text="Нам больше никогда не придется просить маму купить нам что-нибудь!")
    call process_character (n, appearance="pose handfist face neutral", text="Ей бы это понравилось.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Ммм...")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Мама бы нами гордилась.")
    call process_character (sa, appearance="pose leaning face neutral", text="Самостоятельно зарабатывая деньги!")
    call process_character (n, appearance="pose behindhead face curious", text="Думаешь, люди действительно пожертвуют нам?")
    call process_character (sa, appearance="pose handface face neutral", text="Почему бы и нет?")
    call process_character (sa, appearance="pose handface face neutral", text="Один подписчик может дать нам только доллар...")
    call process_character (sa, appearance="pose handface face happy", text="Но представьте, если бы сто или тысяча подписчиков дали нам по доллару!")
    call process_character (n, appearance="pose handpocket face happy", text="Уоу...")
    call process_character (sa, appearance="pose handsbehind face happy", text="Не плохо, да?")
    call process_character (n, appearance="pose twohandfist face happy", text="Я скажу вот, что!")
    call process_character (n, appearance="pose twohandfist face happy", text="Мы должны поставить кнопку пожертвования прямо сейчас!")
    call process_character (sa, appearance="pose leaning face neutral", text="Я уже опередила тебя!")
    call process_character (sa, appearance="pose leaning face neutral", text="Я открываю счет для пожертвований прямо сейчас.")
    call process_character (sa, appearance="pose leaning face neutral", text="Все, что нам нужно сделать сейчас, это добавить кнопку,")
    call process_character (sa, appearance="pose leaning face happy", text="И зрители могут пожертвовать, сколько их душе угодно!")

    call process_end_of_conversation ("sam_convo_8", sa, priority=False, default=False)

    return

label sam_convo_9:
    call process_conversation_beginning ([ (n, ""), (sa, "pose leaning face neutral") ])
    call process_character (sa, appearance="pose leaning face neutral", text="Я не могу дождаться, чтобы пойти на пляж снова!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Я тоже!")
    call process_character (sa, appearance="pose handface face neutral", text="Я читала в интернете, что волны здесь могут быть огромными!")
    call process_character (sa, appearance="pose handface face neutral", text="Как будто они поднимаются выше головы!")
    call process_character (n, appearance="pose behindhead face neutral", text="Это безумие.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Я бы с удовольствием прокатилась под ними, или даже на ней!")
    call process_character (n, appearance="pose handpocket face embarrassed", text="Последний раз, когда я пытался прокатиться на большой волне, я был полностью изничтожен.")
    call process_character (sa, appearance="pose handface face happy", text="Это было так смешно!")
    call process_character (sa, appearance="pose handface face happy", text="Ты пытался плыть вверх по волне, и она подбросила тебя!")
    call process_character (n, appearance="pose behindhead face embarrassed", text="Я даже ничего не мог видеть.")
    call process_character (sa, appearance="pose leaning face neutral", text="[k.say_name] вытащила тебя.")
    call process_character (sa, appearance="pose leaning face neutral", text="Мама побежала на берег, чтобы убедиться, что ты в порядке.")
    call process_character (n, appearance="pose handpocket face curious blush true", text="Я выучил урок, пытаясь оседлать огромную волну.")
    call process_character (n, appearance="pose handpocket face curious blush true", text="Не знаю, смогу ли я сделать это снова.")
    call process_character (sa, appearance="pose leaning face neutral", text="Нельзя сдаваться после одной попытки!")
    call process_character (n, appearance="pose handpocket face curious blush false")
    call process_character (sa, appearance="pose leaning face neutral", text="Просто нужно продолжать совершенствоваться!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Прямо, как мы улучшаем наш навык в видеоиграх.")
    call process_character (n, appearance="pose handpocket face neutral", text="Да, ты совершенно права.")
    call process_character (sa, appearance="pose handface face curious", text="Понять бы ещё, как предотвратить попадание песка под мой купальник...")

    call process_end_of_conversation ("sam_convo_9", sa, priority=False, default=False)

    return


label sam_convo_10:
    call process_conversation_beginning ([ (n, ""), (sa, "pose leaning face neutral") ])
    $ n.reset_appearance()
    call process_character (sa, appearance="pose leaning face neutral", text="Ух ты!")
    call process_character (sa, appearance="pose leaning face neutral", text="Ты не поверишь, что я узнала в интернете.")
    call process_character (n, appearance="pose handpocket face neutral", text="Что?")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Я пыталась выяснить, что за липкое вещество вышло из тебя на днях.")
    call process_character (n, appearance="pose handpocket face neutral", text="И?")
    call process_character (sa, appearance="pose handsbehind face neutral", text="По-видимому, это называется \"эякулят.\"")

    if heard_of_ejaculate or "simone_convo_6" in si.conversations_completed:
        call process_character (n, appearance="pose behindhead face neutral", text="Думаю, я слышал об этом раньше.")
    else:
        call process_character (n, appearance="pose behindhead face neutral", text="Хм...")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Но, это просто \"технический\" термин.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Для этого есть множества других слов.")
    call process_character (n, appearance="pose handpocket face neutral", text="Каких?")
    call process_character (sa, appearance="pose handsbehind face curious", text="Я думаю, некоторые из них были...")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Сперма, {w=0.25}конча, {w=0.25}глазунья, {w=0.25}крем, {w=0.25}витамин, {w=0.25}ореховое масло, {w=0.25}малафья, {w=0.25}детский крем...")
    call process_character (n, appearance="pose handpocket face curious", text="...")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Что?")
    call process_character (n, appearance="pose handpocket face curious", text="(Ореховое масло?)")
    call process_character (n, appearance="pose handpocket face curious", text="Как долго ты изучала это?")
    call process_character (sa, appearance="pose handface face neutral", text="Я не уверена, но думаю, что заснула за столом.")
    call process_character (n, appearance="pose behindhead face neutral", text="Что-нибудь еще нашла?")
    call process_character (sa, appearance="pose leaning face happy", text="О, да!")
    call process_character (sa, appearance="pose leaning face happy", text="Я поняла, что это было за чувство \"покалывания\".")
    call process_character (n, appearance="pose twohandfist face neutral", text="И?")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Мы чувствовали себя возбужденными, или \"заведёнными.\"")

    if not heard_of_horny:
        call process_character (n, appearance="pose handpocket face curious", text="Заведёнными?")

    call process_character (n, appearance="pose behindhead face neutral", text="Чувак, эти термины странные!")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (sa, appearance="pose handface face neutral", text="Я знаю!")
    call process_character (sa, appearance="pose handface face neutral", text="Сначала я подумала, а что мы заводим.")
    call process_character (sa, appearance="pose handface face neutral", text="Но эти слова просто называются...")
    call process_character (sa, appearance="pose handface face curious", text="Эвфе- {w=1.0} Эвфемизмы, вроде как?")
    call process_character (n, appearance="pose behindhead face curious", text="Что вафамизмы?")
    call process_character (n, appearance="pose behindhead face curious", text="Теперь я действительно запутался...")
    call process_character (sa, appearance="pose leaning face neutral", text="Ах, мы освоим их!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Там просто сумасшедшее количество материалов в интернете об этом!")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Я ничего об этом не знала!")
    call process_character (sa, appearance="pose handface face curious", text="Теперь, когда я думаю об этом...")
    call process_character (sa, appearance="pose handface face curious", text="Я слышала, как [k.say_name] говорила, что некоторые из этих слов...")
    call process_character (sa, appearance="pose handface face neutral", text="Подожди секунду!")
    call process_character (sa, appearance="pose handface face neutral", text="Ну конечно!")
    call process_character (sa, appearance="pose handface face neutral", text="Я должна поспрашивать [k.say_name] подробнее об этом!")

    menu:
        "Ты не собираешься рассказать ей о том, что мы сделали с тобой?":
            call process_character (n, appearance="pose handpocket face concerned")
            call process_character (sa, appearance="pose leaning face neutral", text="Ха-ха, нет...")
            call process_character (sa, appearance="pose leaning face neutral", text="Это только между нами...")
            call process_character (sa, appearance="pose handsbehind face neutral", text="Знаешь, что?")
            call process_character (sa, appearance="pose handsbehind face neutral", text="Мы должны просто разобраться с этим!")
        "Я думаю, что мы можем узнать больше об этом сами!":
            call add_points (sa, 1, tag="sam_convo_10_ask_kira")
            call process_character (n, appearance="pose handfist face neutral")
            call process_character (sa, appearance="pose handface face neutral", text="Знаешь, что?")
            call process_character (sa, appearance="pose handface face neutral", text="Ты прав!")
            call process_character (sa, appearance="pose handface face neutral", text="Мы должны выяснить это сами!")


    call process_character (sa, appearance="pose leaning face neutral", text="Нет необходимости спрашивать у [k.say_name] или мамы.")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (sa, appearance="pose leaning face neutral", text="Мы сделаем это сами.")
    call process_character (sa, appearance="pose leaning face neutral", text="Мы можем узнать больше о {w=0.5}малафье.")
    call process_character (sa, appearance="pose handface face neutral", text="Нет, подожди!")
    call process_character (sa, appearance="pose handface face neutral", text="Глазунья, {w=0.5}мне нравится этот термин!")
    call process_character (sa, appearance="pose handface face neutral", text="На самом деле, ореховое масло тоже приличное!")
    call process_character (n, appearance="pose handpocket face curious", text="...")








    call process_end_of_conversation ("sam_convo_10", sa, priority=True, default=False, considered_scene=True)

    return

label sam_convo_11:
    call process_conversation_beginning ([(n, "pose handpocket face neutral blush false"), (sa, "pose leaning face neutral blush false")])
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Куда ты ходил прошлой ночью?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="О, я ходил парк посмотреть.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="О, классно!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Много деревьев для лазания?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Не знаю, но там много деревьев.")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Я надеюсь, что есть и для лазания!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="У нас было дерево, на которое мы взбирались в нашем старом доме!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Было весело лазать!")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Я качался с ветки на ветку вверх по дереву.")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Мама так перепугалась из-за этого!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Да, она боялась, что мы упадем.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Мы опытные альпинисты!")
    call process_character (sa, appearance="pose handface face happy blush false", text="Мы никогда не упали бы!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Кажется, я слышал, что там есть большие скалы...")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="{i}Задыхается{/i}...")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Ты шутишь?")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Где этот парк был всю мою жизнь?!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Похоже, ты действительно хочешь туда пойти.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Пойти туда?")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Я хочу там жить!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Был бы wi-fi в парке...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="У меня не было проблем с сигналом.")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Ну, тогда, надо подумать о стриме на ходу!")

    call process_end_of_conversation ("sam_convo_11", sa, priority=False, default=False)


    return


label sam_convo_12:
    call process_conversation_beginning ([(sa, " pose handface face neutral blush false"), (n, " pose handpocket face neutral blush false")])
    call process_character (sa, appearance="pose handface face neutral blush false", text="Ух ты!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Я понятия не имела, насколько успешным был этот стрим!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Ты видела что-то о нашем канале?")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Да!")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Мы были в сотне лучших стримов, когда были в прямом эфире в ту ночь!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Не может быть!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Ты имеешь в виду из всех стримов?!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Да, но это ещё не всё.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Разработчики Демон Может Смеяться 2 увидели наш стрим...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="И они дали нам бесплатную копию расширенной версии игры!")
    call process_character (n, appearance="pose handfist face happy blush false", text="С ценником в восемьдесят долларов!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Сами разработчики нас видели?")
    call process_character (n, appearance="pose handfist face happy blush false", text="Какая честь!")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Мы получаем игровую добычу, [n.say_name], игровой хабар!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Я поражен, как быстро это происходит.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Не так давно у нас было всего несколько подписчиков.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Наш канал нажимает на нужную струну у людей!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="На самом деле...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Я могу проверить статистику нашего канала.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Для чего?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Я могу узнать, когда на стриме было больше всего зрителей.")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Так мы узнаем, что привлекает и удерживает нашу аудиторию!")
    call process_character (sa, appearance="pose handface face curious blush false", text="Хм, посмотрим, посмотрим...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Бьюсь об заклад, это было, когда ты сражалась с этим летучим монстром!")
    call process_character (sa, appearance="pose handface face angry blush false", text="Ах! Этот босс был таким простым!")
    call process_character (n, appearance="pose handpocket face neutral blush false")
    call process_character (sa, appearance="pose handface face angry blush false", text="Я была готова бросить свой контроллер!")
    call process_character (sa, appearance="pose handface face angry blush false", text="...")
    call process_character (sa, appearance="pose handface face curious blush false", text="В любом случае, кажется, я вижу...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Ага!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Вот огромный всплеск зрителей!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Это было к концу стрима.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ха, я думаю, мы должны были продолжать трансляцию, чтобы увидеть, получим ли больше.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Я должна посмотреть, что случилось, когда мы получили все эти просмотры...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="...")
    call process_character (sa, appearance="pose handface face embarrassed blush false", text="...")
    call process_character (sa, appearance="pose handface face embarrassed blush false", text="Э-э, [n.say_name]?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Что?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Когда это произошло?")
    call process_character (sa, appearance="pose handsbehind face embarrassed blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face embarrassed blush true", text="Стрим всё ещё шел, когда мы...")
    call process_character (sa, appearance="pose handsbehind face embarrassed blush true", text="Когда ты...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Что я вообще делал?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Надеюсь, я не чешу свою задницу или что-то вроде того.")
    call process_character (sa, appearance="pose handsbehind face concerned blush true", text="Конец стрима...")
    call process_character (sa, appearance="pose handsbehind face concerned blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face concerned blush true", text="Он шёл, когда мы трахались.")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Ч-Что?!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Я думал, ты закончила стрим до этого!")
    call process_character (sa, appearance="pose handface face embarrassed blush true", text="Я знаю, что закончила! Я нажала на кнопку, чтобы остановить стрим!")
    call process_character (sa, appearance="pose handface face embarrassed blush true", text="Щелчок должно быть не сработал...")
    call process_character (n, appearance="pose handpocket face concerned blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face concerned blush true", text="...")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Итак...")
    call process_character (n, appearance="pose behindhead face curious blush true", text="У нас было больше зрителей, когда мы трахались?")
    call process_character (sa, appearance="pose handface face concerned blush true", text="Больше, чем когда мы играли...")
    call process_character (sa, appearance="pose handface face concerned blush true", text="...")

    menu:
        "Я не думаю, что это плохо.":
            call process_character (n, appearance="pose behindhead face neutral blush false")
            call process_character (sa, appearance="pose handsbehind face concerned blush true", text="...")
            call process_character (n, appearance="pose behindhead face neutral blush false", text="Я имею в виду, они часто видели нас голыми, верно?")
            call process_character (n, appearance="pose behindhead face neutral blush false", text="Может быть, они надеялись, что это в конечном итоге произойдет.")
            call process_character (sa, appearance="pose handface face neutral blush false", text="Хм...")
            call process_character (sa, appearance="pose handface face neutral blush false", text="Знаешь, я никогда не думала об этом в таком ключе.")
            call process_character (sa, appearance="pose leaning face neutral blush false", text="И ты совершенно прав!")
            call process_character (sa, appearance="pose leaning face neutral blush false", text="Я думаю, они ожидали, что мы дадим им что-то новое и интересное!")
            call process_character (n, appearance="pose twohandfist face neutral blush false", text="Вот именно!")
        "Тогда мы должны трахаться на стриме!":
            call add_boldness (1, tag="sam_convo_12_fuck_on_stream")
            call process_character (n, appearance="pose handfist face neutral blush false")
            call process_character (sa, appearance="pose handsbehind face concerned blush false", text="Ты так думаешь?")
            call process_character (n, appearance="pose behindhead face neutral blush false", text="Ну, ты сама это видела...")
            call process_character (n, appearance="pose behindhead face neutral blush false", text="Мы получаем больше зрителей, когда они видят, что мы делаем такие вещи.")
            call process_character (sa, appearance="pose handface face neutral blush false", text="В твоих словах есть смысл...")
            call process_character (n, appearance="pose twohandfist face neutral blush false", text="Я имею в виду, представьте, сколько хабара и пожертвований мы получили бы, если бы они увидели нас играющими и трахающимися!")
            call process_character (sa, appearance="pose handface face curious blush false", text="Я помню кто-то в чате сказал что-то вроде \"секс всё продаст.\"")
            call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Так что, если мы объединим лучшее из обоих миров, игры и секс...")
            call process_character (n, appearance="pose handfist face happy blush false", text="Мы можем войти в десятку лучших стримеров!")

    call process_character (n, appearance="pose handpocket face neutral blush false")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Значит, мы договорились!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Мы знаем, что делать для нашей аудитории!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Мы должны все спланировать.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Может быть, как ты сказали раньше, принять предложения из чата.")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Спланировать? На наших стримах?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="{i}Фьють!{/i}")
    call process_character (n, appearance="pose handpocket face neutral blush false")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Я не ожидала, что им понравится, [n.say_name]!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Все, что нам нужно сделать, это обеспечить две ключевые вещи для их просмотра...")
    call process_character (sa, appearance="pose handface face happy blush false", text="Некоторые удовлетворяющие игровые комментарии, {w=1.0}и некоторые удовлетворяющие трахи!")


    call process_end_of_conversation ("sam_convo_12", sa, priority=True, default=False, considered_scene=True)

    return