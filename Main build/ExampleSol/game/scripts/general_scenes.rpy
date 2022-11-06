screen intro_title:
    add Solid("#000")
    vbox:
        xalign 0.5
        if not persistent.use_incestral_awakening_name:
            text "Insexual" size 360 xalign 0.5
        else:
            text "Incestral" size 360 xalign 0.5

        text "Awakening" size 360 xalign 0.5

label intro_0:
    $ renpy.set_return_stack([])
    $ renpy.block_rollback()
    $ renpy.scene('screens')
    $ started_main_game = True
    call clear_and_reset_characters

    if wholesome_mode:
        call intro_4

    call bust_art_background ("bg black")
    $ play_music("audio/music/Daily_Music_01.ogg", fadein = 2.0, fadeout = 1.0)
    "{i}Бип! Бип! Бип!{/i}"
    "{i}Ммм...\nЭэ-а...{p=1.0}Рад, что школа еще не началась.{/i}"
    "{i}Я еще немного полежу здесь в постели.{/i}"
    "{i}Начало лета было просто ураганным.{/i}"
    "{i}Такое чувство, что его и не было.{/i}"

    call bust_art_background ("bg family_portrait")
    "{i}Наш старый дом продали через пару недель.{/i}"
    "{i}Грузовики прибыли через несколько дней.{/i}"
    "{i}И вот мы уже живём в новом доме.{/i}"
    "{i}Все прошло на удивление гладко.{/i}"
    "{i}Но это только благодаря моей маме{/i}"

    $ process_character(si, "position right")
    "{i}Я не встречал человека лучше, чем моя мама.{/i}"
    call change_character_name (si, "Моя мама...")
    "{i}Её зовут [si.say_name].{/i}"
    "{i}Она защищала нас с самого детства.\n{/i}"
    "{i}И не важно еда ли это, которую мы едим; школа, которую мы посещаем. Моя мама всегда хочет лучшего для нас.{/i}"
    "{i}Я не видел, чтобы она занималась чем-то другим, кроме как заботилась о нас.{/i}"
    "{i}Иногда мне кажется, что она слишком мало уделяет себе времени.{/i}"
    "{i}Она пытается быть идеальной матерью для нас, но ей тоже нужна наша помощь.{/i}"
    "{i}Кстати, об идеальном...{/i}"

    $ clear_characters()
    $ process_character(k, "position right")
    call change_character_name (k, "Моя старшая сестра...")
    "{i}Моя старшая сестра [k.say_name].{/i}"
    "{i}И я имею в виду \"крупная\" сестра.{/i}"
    "{i}Она высокая.{/i}"
    "{i}Мама сказала, что она унаследовала гены амазонок от наших предков.{/i}"
    "{i}Эта высота ей определенно пригодилась...{/i}"
    "{i}Она выиграла практически все спортивные игры, в которых когда-либо играла.{/i}"
    "{i}Баскетбол, Хоккей, Бейсбол...{/i}"
    "{i}Она даже была квотербеком в своей предыдущей школе.{/i}"
    "{i}И выиграл 3 чемпионата!{/i}"
    "{i}Она пробовалась на Олимпиаду по легкой атлетике.{/i}"
    "{i}Мама была уверена, что она с лёгкостью возьмёт золотую медаль.{/i}"
    "{i}Но думаю, она бы не прошла квалификацию.{/i}"
    "{i}Она сказала, что ее грудь стала слишком большой и тормозит ее.{/i}"
    "{i}Сейчас она работает инструктором по фитнесу в местном тренажерном зале.{/i}"
    "{i}Я думаю, что она может поднять более тяжелые веса, чем большинство парней...{/i}"
    "{i}Она очень нахальна, но всегда выручает и дает советы.{/i}"
    "{i}Она вернула меня и мою сестру.{/i}"
    "{i}Ой!{/i}"

    $ clear_characters()
    $ process_character(sa, "position right")
    call change_character_name (sa, "Моя сестра-близнец,")
    "{i}Моя сестра-близнец, [sa.say_name].{/i}"
    "{i}Мы делаем всё вместе.{/i}"
    "{i}У нас почти все одинаковые интересы.\nвидео игры, аниме...{/i}"
    "{i}Недавно мы попытались создать учетную запись на [video_sharing_site].{/i}"
    "{i}Это место, где можно поделиться прикольным видео.{/i}"
    "{i}И наш план состоит в том, чтобы загружать на него обзоры аниме и видеоигр.{/i}"
    "{i}Я начну скоро писать обзоры.{/i}"
    "{i}[sa.say_name] думает, что прямая трансляция поможет собрать больше зрителей.{/i}"
    "{i}Она очень сильно интересуется высокими технологиями.{/i}"
    "{i}Она постоянно зависает в интернете.{/i}"
    "{i}Но это помогает и мне, потому что она рассказывает обо всем, что узнала.{/i}"

    $ clear_characters()
    $ process_character(n, "position right")
    "{i}Мы делаем все возможное, чтобы держаться на плаву.{/i}"
    "{i}Недавно мы переехали в новый дом.{/i}"
    "{i}И даже нераспаковали все вещи.{/i}"
    "{i}Когда я разберу все коробки я буду таким же сильным, как [k.say_name]...{/i}"
    "{i}Ну, может не таким.{/i}"
    "{i}Но я определенно становлюсь сильнее.{/i}"
    $ renpy.pause(1)
    "{i}Я здесь никого не знаю.{/i}"
    "{i}Кроме моей бабушки, которая живет в пляжном домике.{/i}"
    "{i}И моя тетя, которая недавно развелась.{/i}"
    "{i}Мне нравится разговаривать только с близкими.{/i}"
    "{i}Я слишком нервничаю, пытаясь поговорить с чужими людьми.{/i}"
    "{i}Я даже не захожу в магазины дальше по улице.{/i}"
    $ renpy.pause(1)
    "{i}Надеюсь, этот шаг нам поможет.{/i}"
    "{i}Мы все должны держаться вместе и быть счастливы, что мы есть друг у друга.{/i}"
    $ renpy.pause(1)

    call change_character_name (n, "Ага, а меня то звать,")

    python:
        last_name = renpy.input("[[Введите фамилию]", default = "Williams", length = 14)

    call update_last_names

    "{color=[n.color]}[n.say_name] [last_name]{/color}, пора вставать"
    $ stop_music(fadeout=3)
    $ quick_menu = False

    $ clear_characters()
    with Dissolve(0.5)
    show screen intro_title
    with Dissolve(1.0)

    $ renpy.pause(1.5)
    $ play_music("audio/music/Daily_Music_03.ogg", fadein = 2.0, fadeout = 1.0)
    call process_scene_beginning (nate_room, char_tuple_array=[ (n, "outfit underwear pose handsdown face neutral") ])
    $ renpy.scene('screens')
    $ quick_menu = True
    call process_character (n, appearance="outfit underwear pose handsdown face neutral", text="{i}Зевок...{/i}")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral", text="(Это был хороший сон)")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral", text="(Нужно уже привыкнуть к планировке комнаты)")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral", text="(Кажется, моя одежда в этом ящике.)")
    $ renpy.pause(1)
    call process_character (n, appearance="outfit underwear pose handsdown face concerned", text="(Нет)")
    call process_character (n, appearance="outfit underwear pose handsdown face concerned", text="(В этом?)")
    $ renpy.pause(1)
    call process_character (n, appearance="outfit underwear pose twohandfist face happy", text="(Да!)")
    call character_leave_dissolve (n)
    $ renpy.pause(1)
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="(Это здорово, проснуться позже, чем обычно).")
    $ renpy.pause(1)
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned", text="(Так странно не делить комнату с сестрой {color=[sa.color]}[sa.say_name]{/color})")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="(Я могу сходить к ней в комнату.)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral", text="(Или я могу увидеть{color=[k.color]}[k.say_name]{/color}, может она уже встала)")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy", text="(Бьюсь об заклад, {color=[si.color]}Мама{/color} готовит вкусный завтрак)")

    $ scenes_completed.add("intro_0")

    menu:
        "Пойду посмотреть, как там {color=[sa.color]}[sa.say_name]{/color}.":
            call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="Интересно, как у нее дела с настройкой компьютера.")
            call intro_1_chose_sam
        "Я посмотрю, что делает {color=[k.color]}[k.say_name]{/color}.":
            call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="Кажется, я слышу ее в коридоре.")
            call intro_1_chose_kira
        "Я очень голоден, я спущусь вниз и поприветствую {color=[si.color]}Маму{/color}.":
            call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="Я чувствую запах ее потрясающего омлета!")
            call intro_1_chose_simone

    return

label intro_1_chose_sam:
    call process_scene_beginning (sam_room, char_tuple_array=[ (n, ""), (sa, "") ])

    call process_character (n, appearance="pose handpocket face neutral", text="Привет.")
    call process_character (sa, appearance="pose leaning face neutral")
    $ sa.c_full("Ой, привет [n.say_name]!")
    call process_character (n, appearance="pose handpocket face neutral", text="Просто хотел узнать, как ты.")
    call process_character (sa, appearance="pose handface face neutral", text="Спасибо, что проведал меня.")
    call process_character (sa, appearance="pose handface face neutral", text="Мы жили в одной комнате всю жизнь, а теперь у каждого своя.")
    call process_character (sa, appearance="pose handface face neutral", text="По крайней мере, мы рядом друг с другом.")
    call process_character (n, appearance="pose handpocket face neutral", text="Это точно.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Я вчера допоздна настраивала компьютер.")
    call process_character (n, appearance="pose handpocket face neutral", text="Да?")
    call process_character (n, appearance="pose handfist face neutral", text="Мы уже можем стримить?")
    call process_character (sa, appearance="pose handface face happy", text="Почти!")
    call process_character (sa, appearance="pose handface face happy", text="Никак не найду время увеличить количество фолловеров.")
    call process_character (sa, appearance="pose leaning face neutral", text="Но завтра уже можно будет стримить")
    call process_character (sa, appearance="pose handface face neutral", text="Присоединишься ко мне?")

    menu:
        "Да, конечно.":
            $ sa.add_points(1, tag = "intro_1_chose_sam_join_streaming")
            call process_character (sa, appearance="pose leaning face happy", text="О, да!\nНаш стрим канал заживёт!")
        "Может быть, посмотрим.":
            call process_character (n, appearance="pose handpocket face neutral")
            call process_character (sa, appearance="pose handsbehind face neutral", text="Ну, надеюсь, ты подойдёшь, когда будет возможность.")

    call process_character (sa, appearance="pose handface face neutral", text="Мама, наверное, ждет нас внизу.")
    call process_character (sa, appearance="pose handface face neutral", text="Надеюсь, она готовит омлет!")
    call process_character (sa, appearance="pose handface face happy", text="Давай быстрее, а то [k.say_name] всё сожрет!!")

    $ scenes_completed.add("intro_1_chose_sam")
    call intro_2
    return

label intro_1_chose_kira:
    call process_scene_beginning (hallway, char_tuple_array=[ (n, ""), (k, "pose armcross") ])

    call process_character (k, appearance="pose armcross face neutral")
    $ k.c_full("Хай, бро.")
    call process_character (n, appearance="pose handpocket face neutral", text="Привет [k.say_name].")
    call process_character (k, appearance="pose armcross face neutral", text="Болит тело после вчерашнего переноса коробок?")
    call process_character (n, appearance="pose handpocket face neutral", text="Да не особо.\nНо я очень устала вчера.")
    call process_character (k, appearance="pose handhip face neutral", text="Держу пари.")
    call process_character (k, appearance="pose handhip face happy", text="Ты слишком сильно волнуешься за меня!")
    call process_character (n, appearance="pose handpocket face neutral", text="Эй, ванная свободна?")
    call process_character (k, appearance="pose armcross face neutral", text="Только что оттуда после пробежки.")
    call process_character (n, appearance="pose handpocket face curious", text="Последний раз, когда я был в душе после тебя, сток был забит.")
    call process_character (k, appearance="pose armcross face happy", text="Ах да, хаха.\nНу, на этот раз не должно быть.")
    call process_character (k, appearance="pose armcross face neutral")
    call process_character (n, appearance="pose handpocket face curious", text="Это было похоже на твои волосы в сливе.\nТы же не лысеешь?")
    call process_character (k, appearance="pose handhip face neutral", text="Нет, это были не волосы не с головы.\nЯ брилась.")
    call process_character (n, appearance="pose behindhead face curious")
    $ renpy.pause(1)
    call process_character (n, appearance="pose behindhead face curious", text="Что брила?")
    call process_character (k, appearance="pose armsup face neutral", text="Просто очищала взлётную полосу.")
    call process_character (n, appearance="pose handpocket face curious")
    $ renpy.pause(1)
    call process_character (n, appearance="pose handpocket face curious", text="{i}?{/i}")
    call process_character (k, appearance="pose armsup face neutral", text="(Чешет голову)")
    $ renpy.pause(1)
    call process_character (k, appearance="pose armsup face neutral", text="Эй!")
    call process_character (k, appearance="pose handhip face neutral")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (k, appearance="pose handhip face neutral", text="Завтра я буду выполнять зарядку.")
    call process_character (k, appearance="pose handhip face neutral", text="И мне нужна будет твоя помощь.")
    call process_character (k, appearance="pose handhip face neutral", text="Придёшь?")

    menu:
        "Конечно!":
            $ k.add_points(1, tag = "intro_1_chose_kira_you_down")
            call process_character (n, appearance="pose twohandfist face neutral")
            call process_character (k, appearance="pose armsup face happy", text="Мило!")
        "А зачем?":
            call process_character (n, appearance="pose handpocket face curious")
            call process_character (k, appearance="pose handhip face concerned", text="{i}Эхх{/i}\nПросто приходи завтра, и я объясню.")

    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (k, appearance="pose armcross face neutral", text="Я чувствую сильный запах маминого омлета.")
    call process_character (k, appearance="pose armcross face neutral", text="Должно быть, она опробовала новый рецепт, что я ей дала.")
    call process_character (k, appearance="pose handhip face neutral", text="Увидимся внизу!")

    $ scenes_completed.add("intro_1_chose_kira")
    call intro_2

    return

label intro_1_chose_simone:
    call process_scene_beginning (kitchen, char_tuple_array=[ (n, ""), (si, "") ])

    call process_character (n, appearance="pose handpocket face neutral", text="Привет, Мам!")
    call process_character (si, appearance="pose handsfront face neutral")
    $ si.c_full("Доброе утро, [n.say_name]!\nЯ только что закончила готовить.")
    call process_character (n, appearance="pose twohandfist face happy", text="Круто.")
    call process_character (si, appearance="pose handsfront face neutral", text="Кто успел, тот и съел!")
    call process_character (si, appearance="pose armunder face happy", text="И похоже, ты первый в очереди!")
    call process_character (n, appearance="pose handpocket face neutral", text="Что у нас на завтрак?")
    call process_character (si, appearance="pose handsup face neutral", text="Омлет со свежим шпинатом и помидорами.")
    call process_character (si, appearance="pose handsup face neutral", text="Немного ржаного хлеба из пекарни,")
    call process_character (si, appearance="pose handsup face neutral", text="молока и апельсинового сока.")
    call process_character (si, appearance="pose handsup face happy", text="Выбирай сам!")

    menu:
        "Спасибо, Мама!":
            call process_character (si, appearance="pose handsfront face neutral", text="Всегда пожалуйста!")
        "Хочешь, я потом помогу помыть посуду?":
            $ si.add_points(1, tag = "intro_1_chose_simon_take_pick")
            call process_character (si, appearance="pose armunder face neutral", text="Это так мило [n.say_name]! Спасибо!")

    $ scenes_completed.add("intro_1_chose_simone")
    call intro_2

    return

label intro_2:
    $ temp_variable = True
    python:
        if "intro_1_chose_simone" in scenes_completed:
            temp_variable = False

    if temp_variable:
        call process_scene_beginning (kitchen)
    else:
        call character_leave_dissolve (si)


    call process_character (n, appearance="position right", show_bust=False)
    call process_character (k, appearance="position right", show_bust=False)
    call process_character (sa, appearance="position right", show_bust=False)
    call process_character (si, appearance="position right", show_bust=False)

    call process_character (n, appearance="pose twohandfist face neutral", text="Завтрак такой вкусный!", replace=True)
    call process_character (si, appearance="pose handsfront face neutral", replace=True)

    python:
        if "intro_1_chose_simone" in scenes_completed:
            si.c("Рада, что понравилось!\n[k.say_name] дала рецепт.")
        else:
            si.c_full("Рада, что понравилось!\n[k.say_name] дала рецепт.")

    call process_character (k, appearance="pose armcross face neutral", replace=True)

    python:
        if "intro_1_chose_kira" in scenes_completed:
            k.c("Он очень питательный.")
        else:
            k.c_full("Он очень питательный.")

    call process_character (k, appearance="pose armsup face neutral", text="Вот, что мне нужно, чтобы быть в форме.", replace=True)
    call process_character (n, appearance="pose handpocket face curious", text="В форме чего?", replace=True)
    $ process_character_replace_utility(si, appearance = "pose armunder face happy", text = "Хаха! Это просто выражение [n.say_name]!", replace = True)

    call process_character (sa, appearance="pose leaning face neutral", replace=True)

    python:
        if "intro_1_chose_sam" in scenes_completed:
            sa.c("Мам!\nВ бассейн уже можно?")
        else:
            sa.c_full("Мам!\nВ бассейн уже можно?")

    call process_character (si, appearance="pose handsfront face neutral", text="Почти, милый.\nЯ вызвала сантехника, чтобы починил насос.", replace=True)
    call process_character (sa, appearance="pose handsbehind face happy", text="Урра!", replace=True)
    $ process_character_replace_utility(sa, appearance = "pose handsbehind face neutral", text = "[n.say_name], мы наконец-то узнаем, кто сможет проплыть от одного конца бассейна до другого, без единого вздоха!", replace = True)
    call process_character (n, appearance="pose behindhead face curious", text="Ну...", replace=True)
    $ process_character_replace_utility(k, appearance = "pose handhip face neutral", text = "Нужно работать над увеличением объёма легких [n.say_name]!", replace = True)
    call process_character (k, appearance="pose armcross face neutral", text="Ты же не хочешь, чтобы тебя побила девушка?", replace=True)
    call process_character (n, appearance="pose handpocket face concerned", text="О чём ты вообще?{p=1.0}Ты победила всех парней, с кем плавала.", replace=True)
    call process_character (k, appearance="pose handhip face happy", text="Я просто поддразниваю тебя.", replace=True)
    call process_character (k, appearance="pose armsup face neutral", text="Но серьезно, я не могу дождаться, когда этот бассейн заработает.", replace=True)
    call process_character (k, appearance="pose armsup face neutral", text="Климат здесь намного теплее.", replace=True)
    call process_character (si, appearance="pose handsup face neutral", text="Теперь, когда мы живем рядом с бабушкой, будем часто ходить на пляж!", replace=True)
    $ renpy.pause(1)
    call process_character (si, appearance="pose handsfront face neutral", text="Так какой план на сегодня?", replace=True)
    call process_character (k, appearance="pose handhip face concerned", text="Мне нужно идти на работу.", replace=True)
    call process_character (k, appearance="pose handhip face neutral", text="Я с нетерпением жду кардио тренировок!", replace=True)
    call process_character (sa, appearance="pose handface face curious", text="Так как бассейн еще не заработал...", replace=True)
    call process_character (sa, appearance="pose handface face neutral", text="Я буду играть в видеоигры", replace=True)
    $ process_character_replace_utility(si, appearance = "pose handsfront face neutral", text = "А ты что [n.say_name]?", replace = True)

    $ scenes_completed.add("intro_2")

    menu:
        "Я расслаблюсь на солнышке":
            call process_character (si, appearance="pose handsfront face neutral", text="Не забудь нанести солнцезащитный крем!", replace=True)
            call intro_3_chose_kira
        "Я буду играть в видеоигры с {color=[sa.color]}[sa.say_name]{/color}!":
            $ sa.add_points(1, tag = "intro_2_what_plan")
            call process_character (sa, appearance="pose leaning face happy", text="Отлично! Кооп!", replace=True)
            call intro_3_chose_sam
        "Я перенесу еще несколько ящиков с тобой {color=[si.color]}Мама{/color}.":
            $ si.add_points(2, tag = "intro_2_what_plan")
            call process_character (si, appearance="pose handsup face happy", text="Спасибо, [n.say_name]!", replace=True)
            call process_character (si, appearance="pose handsup face happy", text="Мне бы не помешала помощь!", replace=True)
            call intro_3_chose_simone

    return

label intro_3_chose_sam:
    call process_scene_beginning (sam_room, char_tuple_array=[ (n, ""), (sa, "") ])

    call process_character (sa, appearance="pose handface face neutral", text="Эта игра получила так много хороших отзывов.")
    call process_character (sa, appearance="pose handface face neutral", text="Я видел, как Игровой Гринч играл первый час.")
    call process_character (n, appearance="pose handpocket face neutral", text="\"Твистер Душ.\"")
    call process_character (sa, appearance="pose leaning face neutral", text="Да, это шмап.")
    call process_character (n, appearance="pose handpocket face curious", text="Шмап?")
    call process_character (sa, appearance="pose handface face neutral", text="О, это термин, который используют, чтобы описать эти стрелялки сверху вниз.")
    call process_character (sa, appearance="pose handface face neutral", text="\"Шут-эм-ап.\"")
    call process_character (sa, appearance="pose handface face happy", text="\"Шмап.\"")
    call process_character (n, appearance="pose handpocket face happy", text="О-о, понятно.")
    call process_character (n, appearance="pose handfist face happy", text="Так как же работает кооперативный режим?")
    call process_character (sa, appearance="pose handsbehind face neutral", text="О, это действительно круто")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Мы оба управляем одним кораблем.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Один человек контролирует движение корабля.\nДругой - оружие.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Поэтому мы должны координировать наши атаки.")
    call process_character (n, appearance="pose handpocket face happy", text="Звучит довольно круто.")
    call process_character (sa, appearance="pose leaning face neutral", text="Ты хочешь контролировать движение или оружие?")

    menu:
        "Я разберусь с движением.":
            call process_character (n, appearance="pose twohandfist face neutral")
            call process_character (sa, appearance="pose leaning face neutral", text="Я буду взрывать врагов своим лазерным оружием!")
        "Я разберусь с оружием.":
            call process_character (n, appearance="pose twohandfist face neutral")
            call process_character (sa, appearance="pose handface face curious", text="Время показать свои навыки уклонения!")
        "Выбирай ты.":
            call process_character (n, appearance="pose behindhead face neutral")
            $ sa.add_points(1, tag = "intro_3_chose_sam_controls")
            call process_character (sa, appearance="pose handsbehind face neutral blush true", text="Спасибо!")
            call process_character (sa, appearance="pose handsbehind face happy blush false", text="Хорошо, я выберу не глядя!")

    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (sa, appearance="pose leaning face neutral", text="Хорошо, почти готово.")
    call process_character (sa, appearance="pose leaning face neutral", text="Я думаю, что сейчас мы начнём с нормальной сложности.")
    call process_character (n, appearance="pose handpocket face neutral", text="Сколько достижений в этой игре?")
    call process_character (sa, appearance="pose handsbehind face neutral", text="О безумное количество!\nМожно разблокировать около 40 различных орудий.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Это безумие.")
    call process_character (n, appearance="pose twohandfist face happy", text="Ну, может уже начать разблокировывать их!")
    call process_character (sa, appearance="pose handface face neutral", text="Я знаю Эрика из Игрового Гринча нашел секретное оружие на первом уровне.")
    call process_character (sa, appearance="pose handface face curious", text="Кажется, я помню, где оно находится.{p=1.0}Мы должны взорвать камень, блокирующий пещеру.")
    call process_character (n, appearance="pose handpocket face neutral", text="Просто дай мне знать, когда увидишь.")
    call process_character (sa, appearance="pose leaning face neutral", text="У тебя получилось.")
    call process_character (sa, appearance="pose leaning face happy", text="И игра запущена!")

    $ scenes_completed.add("intro_3_chose_sam")
    call intro_4

    return

label intro_3_chose_simone:
    call process_scene_beginning (living_room, char_tuple_array=[ (n, ""), (si, "pose handsfront") ])

    call process_character (si, appearance="pose handsfront face neutral", text="Я очень ценю твою помощь [n.say_name].")
    call process_character (si, appearance="pose handsfront face neutral", text="Не перенапрягись.")
    call process_character (n, appearance="pose handpocket face neutral", text="Все в порядке, Мам.")
    call process_character (n, appearance="pose behindhead face neutral", text="Нам еще многое предстоит сделать.")
    call process_character (si, appearance="pose armunder face neutral", text="Я знаю.")
    call process_character (si, appearance="pose armunder face happy", text="Я и не представляла, сколько вещей мы упаковали.")
    call process_character (n, appearance="pose handpocket face curious", text="Интересно, сколько мы могли выбросить?")
    call process_character (si, appearance="pose handsfront face curious", text="Мне кажется, что мы выбросили итак много вещей из старого дома.")
    $ renpy.pause(1)
    call process_character (n, appearance="pose handpocket face concerned")

    menu:
        "Ты скучаешь по нашему старому дому, мам?":
            call process_character (si, appearance="pose handsup face flirty", text="Пока у меня есть ты и сестрички, не важно, где я нахожусь.")
        "Мам, как ты себя чувствуешь??":
            call process_character (si, appearance="pose handsfront face neutral", text="Спасибо [n.say_name], что спросил.")
            call process_character (si, appearance="pose handsfront face neutral", text="Я чувствую себя хорошо.")

    call process_character (si, appearance="pose handsup face neutral", text="Иногда мне тяжело.")
    call process_character (si, appearance="pose handsup face neutral", text="Легко увязнуть в мыслях обо всем, что произошло.")
    call process_character (si, appearance="pose armunder face happy", text="Но когда я вижу тебя или [sa.say_name] мне радостно на душе, я чувствую себя намного лучше!")
    call process_character (n, appearance="pose handpocket face neutral", text="Я просто хотел убедиться, что тебе есть с кем поговорить, если понадобится я всегда готов.")
    call process_character (si, appearance="pose handsfront face neutral", text="Ну, это очень мило с твоей стороны [n.say_name].")
    call process_character (si, appearance="pose handsup face flirty", text="Я очень счастлива, что у меня такой бескорыстный сын.\nИ есть поддержка семьи.")
    call process_character (n, appearance="pose behindhead face curious", text="Хотя, сегодня семья не особо помогает перетаскивать коробки.")
    call process_character (si, appearance="pose handsup face happy", text="Хаха, нуу...")
    call process_character (si, appearance="pose handsfront face neutral", text="Не похоже, что все эти коробки перетащим за один день.")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (si, appearance="pose handsfront face neutral", text="Мы просто продолжим потом.")
    call process_character (si, appearance="pose handsfront face neutral", text="Думаю, на сегодня достаточно.")
    call process_character (n, appearance="pose handfist face neutral", text="Мои руки хорошенько размялись.")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (si, appearance="pose handsup face neutral", text="Не хочешь чая со льдом?")
    call process_character (si, appearance="pose handsup face happy", text="С сахаром, конечно.")
    call process_character (n, appearance="pose twohandfist face neutral", text="Конечно!{p=1.0}Спасибо, Мам.")

    $ scenes_completed.add("intro_3_chose_simone")
    call intro_4

    return

label intro_3_chose_kira:
    call process_scene_beginning (backyard, char_tuple_array=[ (n, "pose behindhead face happy outfit swimsuit") ])

    call process_character (n, appearance="pose behindhead face happy outfit swimsuit", text="{i}Ахх{/i}{p=1.0}Чувствую себя отлично!")
    call process_character (n, appearance="pose behindhead face embarrassed", text="(Лучше быть осторожным, чтобы не обжечься.){p=1.0}(В этом городе гораздо жарче на солнце)")
    call process_character (k, appearance="pose armcross face neutral", text="День ничегонеделания?")
    call process_character (n, appearance="pose handsdown face happy", text="Оу, привет!")
    call process_character (n, appearance="pose handsdown face happy", text="Ты только что вернулась с работы?")
    call process_character (k, appearance="pose handhip face neutral", text="Ну да...")
    call process_character (n, appearance="pose behindhead face concerned", text="Тяжелый день?")
    call process_character (k, appearance="pose armcross face neutral", text="Тяжело для людей, которых я тренирую!")
    call process_character (k, appearance="pose armcross face concerned", text="Некоторые даже не смогли выполнить 5 отжиманий!{p=1.0}И это было после того, как я их мотивировала!")
    call process_character (n, appearance="pose handsdown face neutral", text="Тебе здесь нравится?")
    call process_character (k, appearance="pose armsup face neutral", text="О, определенно!")
    call process_character (k, appearance="pose armsup face happy", text="Я занимаюсь спортом, и мне ещё платят за это!")
    call process_character (n, appearance="pose handsdown face neutral", text="Ты будешь загорать?")
    call process_character (k, appearance="pose handhip face neutral", text="Может быть.{p=1.0}В последнее время я часто бываю на солнце.")
    call process_character (k, appearance="pose handhip face neutral", text="При такой жаре очень легко загореть.")
    call process_character (n, appearance="pose twohandfist face neutral", text="Я же говорил!{p=1.0}Ты уже загорела!")
    call process_character (k, appearance="pose armsup face neutral", text="Я бронзовая богиня! Хехе.")
    $ k.add_points(1, tag = "intro_3_chose_kira_bronze")
    call process_character (k, appearance="pose handhip face curious", text="Парень по ремонту бассейнов еще не заходил?")
    call process_character (n, appearance="pose behindhead face neutral", text="Я еще никого не видел.")
    call process_character (k, appearance="pose armcross face concerned", text="{i}Эхх{/i}{p=1.0}Наверное, устал и забыл зайти.")
    call process_character (k, appearance="pose armcross face concerned", text="Я очень хочу, чтобы джакузи заработало.")
    call process_character (n, appearance="pose twohandfist face neutral", text="О, да!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Было бы неплохо использовать в прохладные ночи.")
    call process_character (k, appearance="pose handhip face neutral", text="Ну а пока...")
    call process_character (n, appearance="pose handsdown face neutral")
    call process_character (k, appearance="pose handhip face neutral", text="Я хотела купить новое бикини.")
    call process_character (k, appearance="pose handhip face neutral", text="Возможно, я найду в интернете.")
    call process_character (k, appearance="pose handhip face neutral", text="Обязательно зелёное.")

    menu:
        "Не могу дождаться, чтобы увидеть его!":
            $ k.add_points(1, tag = "intro_3_chose_kira_green_bikini")
            call process_character (n, appearance="pose handfist face happy")
            call process_character (k, appearance="pose armcross face flirty", text="(Спорим, не увидишь)")
        "Я думаю, желтый будет лучше смотреться.":
            call process_character (n, appearance="pose handsdown face neutral")
            call process_character (k, appearance="pose armcross face concerned", text="А...")
            call process_character (k, appearance="pose armcross face concerned", text="Желтый немного нейтрален для меня.")
            call process_character (k, appearance="pose armcross face concerned", text="Ну только, если он будет ярко-желтым.")

    call process_character (n, appearance="pose handsdown face neutral")
    call process_character (k, appearance="pose handhip face neutral", text="Думаю, ужин скоро будет готов.")
    call process_character (k, appearance="pose handhip face neutral", text="Увидимся внутри?")
    call process_character (n, text="Окей.")

    $ scenes_completed.add("intro_3_chose_kira")
    call intro_4

    return

label intro_4:
    $ stop_music(fadeout=3)
    $ week.time = "night"
    call process_scene_beginning (nate_room)

    $ temp_variable = "kira"
    python:
        if "intro_3_chose_sam" in scenes_completed:
            temp_variable = "sam"
        if "intro_3_chose_simone" in scenes_completed:
            temp_variable = "simone"

    if temp_variable == "kira":
        call process_character (n, appearance="pose behindhead face happy", text="{i}Ох!{/i}\nКакой спокойный денек выдался!")
    if temp_variable == "sam":
        call process_character (n, appearance="pose twohandfist face happy", text="Эта игра была очень веселой.")
        call process_character (n, appearance="pose handpocket face concerned", text="Но мы так и не смогли победить финального босса.")
    if temp_variable == "simone":
        call process_character (n, appearance="pose behindhead face flirty", text="{i}Фуу!{/i}\nВау, я устал от перетаскивания этих коробок!")

    call process_character (n, appearance="pose handpocket face neutral", text="Думаю, я еще не хочу спать.")
    call process_character (n, appearance="", text="Может, я смогу увидеть, что делают остальные.")

    call character_leave_dissolve (n)

    "Каждый день вы можете исследовать локации и взаимодействовать с персонажами."
    "Часть этого взаимодействия включает в себя мини-игры, которые являются основным методом построения отношений."
    "Есть также уникальные события, которые могут увеличить отношения с персонажем."
    "По мере роста ваших отношений будут доступны специальные сцены!"
    "Каждый уровень отношений открывает новую сцену."
    "Вы свободны выбирать, с кем вы хотите иметь отношения!"
    "Некоторые ситуации потребуют \"Смелости.\""
    "Смелость - важный атрибут отношений."
    "Смелость может быть увеличена с помощью определенных сцен и мини-игр."
    "Попробуйте открыть эти сцены и мини-игры!"
    "Повышая уровень смелости, вы сможете выполнять новые действия или исследовать новые локации."

    $ nate_room.decide_and_play_daily_music_queue()
    $ stats.current_zone = home

    call day_reset_locations_chars
    call navigation_menu

    return

label julia_pre_arrival:
    call process_scene_beginning (bg="bg kitchen_daytime")
    $ nate_room.decide_and_play_daily_music_queue()

    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false position right", text="Скоро у нас будут гости!", replace=True)
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false position right", text="Да?", replace=True)
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Кто?", replace=True)
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Это твоя кузина, [julia.say_name].", replace=True)
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Мы давно ее не видели.", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="О, боже!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Она взрывная, с ней круто тусоваться!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Надо припасти побольше водяных шаров.", replace=True)
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="И объединиться против [n.say_name]!", replace=True)
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...", replace=True)
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Когда она приедет?", replace=True)
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Завтра.", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Так скоро?", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="Мило!", replace=True)
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Да, твоя тетя имеет тенденцию планировать всё на лету...", replace=True)
    call process_character (si, appearance="outfit clothes pose handsup face concerned blush false", text="И она только сказала мне, что [julia.say_name] приедет утром.", replace=True)
    call process_character (si, appearance="outfit clothes pose handsup face concerned blush false", text="...", replace=True)
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="К счастью, у нас есть место для нее!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Она может остаться в моей комнате!", replace=True)
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Я не знаю, захочет ли она спать на полу, дорогая!", replace=True)
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Диван в гостиной удобный.", replace=True)
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Она может там переночевать.", replace=True)
    call process_character (k, appearance="pose armsup face neutral blush false position right", text="Кто останется на ночь?", replace=True)
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Наша кузина [julia.say_name], заскочит утром!", replace=True)
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Правда?", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Я не могу дождаться, чтобы сделать всё, что мы делали в прошлый раз!", replace=True)
    call process_character (k, appearance="pose handhip face neutral blush false", text="Это было давно [sa.say_name].", replace=True)
    call process_character (k, appearance="pose handhip face neutral blush false", text="Может она изменилась.", replace=True)
    call process_character (k, appearance="pose handhip face neutral blush false", text="Последнее, что я слышала, она пыталась стать писателем.", replace=True)
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="О, она писательница?", replace=True)
    call process_character (k, appearance="pose handhip face neutral blush false", text="Я думаю, она делает это просто для удовольствия.", replace=True)
    call process_character (k, appearance="pose handhip face neutral blush false", text="Я читала кое-что из её работ в интернете.", replace=True)
    call process_character (k, appearance="pose armcross face neutral blush false", text="И это не так уж и плохо.", replace=True)
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Рада за неё!", replace=True)
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Она использует свой творческий потенциал.", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Может, мы с ней сможем написать рассказ вместе!", replace=True)
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Спроси ее, когда она приедет, милая.", replace=True)
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Как долго она здесь пробудет?", replace=True)
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Она будет здесь всё лето!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="{i}Вздох{/i}...", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Всё лето?!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="Да!", replace=True)
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Я думала, ты будешь рада это услышать!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Мы столько всего можем сделать!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Я хочу узнать, в какие видеоигры она захочет поиграть!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="У нас может быть игровой марафон на всё лето!", replace=True)
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Может быть, она захочет проверить бассейн, пока будет здесь.", replace=True)
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="[julia.say_name] будет более чем рада всему!", replace=True)
    call process_character (k, appearance="pose armcross face neutral blush false", text="Ты и [sa.say_name] можете показать ваши стриминговые вещички.", replace=True)
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="О, да!", replace=True)
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Думаю, ей бы это очень понравилось!", replace=True)
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Это может быть круто, да.", replace=True)
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Почему бы тебе не поговорить об этом с сёстрой?", replace=True)
    call process_character (si, appearance="outfit clothes pose handsfront face happy blush false", text="Я уверен, она будет рада этому!", replace=True)
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="[julia.say_name] будет специальным гостем нашего стрима!", replace=True)
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Я пойду расскажу прямо сейчас!!", replace=True)

    call character_leave_dissolve (n)
    pause 0.5

    $ display_multiple_characters([ (si, "pose handsfront face neutral blush false position right"), (k, "pose armcross face neutral blush false position left") ])

    call process_character (k, appearance="pose armcross face neutral blush false", text="...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
    call process_character (k, appearance="pose handhip face neutral blush false", text="Она будет всё лето здесь?")
    call process_character (k, appearance="pose handhip face neutral blush false", text="Уоу.")
    call process_character (si, appearance="pose handsup face happy blush false", text="Будет куча забот, это точно!")
    call process_character (k, appearance="pose handhip face happy blush false", text="Хорошо, что наш дом достаточно большой, чтобы разместить гостя для длительного пребывания.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Будет приятно увидеть, как [julia.say_name] изменилась.")
    call process_character (k, appearance="pose armcross face neutral blush false", text="Мы увидим ее очень скоро.")

    $ reset_all_characters()
    if started_main_game:
        $ had_julia_pre_arrival_scene = True
        show screen hud
        $ advance_time_return_location.start(force_music_change = True, morning_wake_lines = False)
    else:
        jump debug_menu

    return

label julia_arrival:
    $ nate_room.decide_and_play_daily_music_queue()
    call process_scene_beginning (bg="bg hallway_daytime")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="(Интересно, [julia.say_name] уже прибыла...)")
    call process_character (si, text="[n.say_name]!")
    call process_character (si, text="Спускайся!")

    call process_new_location (bg=living_room)

    call process_character (si, appearance="pose handsup face neutral blush false position right", text="[julia.say_name] здесь!")
    call character_leave_dissolve (si)
    pause 0.5

    call process_character (julia, appearance="pose handface face neutral blush false", show_bust=False)
    $ refresh_character(julia, force_transition = Dissolve(0.75))
    pause 0.75

    call process_character (n, appearance="pose handpocket face happy blush false position right", text="Привет [julia.say_name]!")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Привет.")
    call character_leave_dissolve (n)
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Вот диван, на котором ты будешь спать, пока ты здесь, [julia.say_name].")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Я приготовила подушки и одеяла.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Вообще-то, мне пора уходить.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="[n.say_name], почему бы тебе не показать [julia.say_name] дом?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Покажи ей всё здесь.")
    call character_leave_dissolve (si)
    call process_character (n, appearance="pose handfist face neutral blush false", text="Хорошо, Мам!")
    call character_leave_dissolve (n)
    call process_character (si, appearance="pose handsup face happy blush false", text="Увидимся позже!")

    $ clear_characters()

    $ display_multiple_characters([ (julia, "pose handface face neutral blush false"), (n, "pose handpocket face neutral blush false position right") ])

    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Хорошо, позволь мне устроить тебе экскурсию!")
    call process_character (julia, appearance="pose handup face neutral blush false", text="...")

    call process_new_location (bg=kitchen, char_tuple_array=[ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (julia, "outfit clothes pose handup face neutral blush false")] )

    call process_character (n, appearance="pose handpocket face neutral blush false", text="Итак, это кухня!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="В шкафчиках полно закусок.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="...")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Моя мама выращивает и хранит для нас много овощей.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Лично я больше люблю фрукты.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Я храню мои любимые хлопья повыше.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Если [k.say_name] она найдёт их и съест.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Разве она не может сама купить себе хлопья?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Это хороший вопрос...")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Ну, мы часто покупаем хлопья.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Так что всегда есть пара коробок.")

    call process_new_location (bg=backyard, char_tuple_array=[(julia, "pose handface face neutral blush false"), (n, "pose twohandfist face neutral blush false")] )

    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Теперь это...")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Это лучшая часть дома на мой взгляд!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="У нас есть большой бассейн, можно плавать все время.")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="При условии, что снаружи достаточно тепло.")
    call process_character (n, appearance="pose handfist face happy blush false", text="Так что мы можем быть здесь весь день!")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Я быстро сгораю на Солнце.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="У нас под рукой много солнцезащитного крема.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Моя мама всегда говорит мне нанести его.")
    call process_character (n, appearance="pose behindhead face happy blush false", text="Я еще ни разу не обжегся!")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Ладно, пошли внутрь, и я покажу остальную часть дома.")


    call process_new_location (bg=hallway, char_tuple_array=[(julia, "pose armcross face neutral blush false"), (n, "pose handpocket face neutral blush false")] )

    call process_character (n, appearance="pose handpocket face neutral blush false", text="Здесь, наверху, живу я, [sa.say_name] и...")
    call character_leave_dissolve (n)
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false position right", text="Привет [n.say_name].")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Ой, привет [julia.say_name]!")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Ты только что приехала?")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Да.")
    call process_character (k, appearance="pose handhip face neutral blush false", text="[n.say_name] показать тебе окрестности, как я понимаю?")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose handfist face neutral blush false", text="Ага!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Я провожу для нее экскурсию по дому.")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armcross face neutral blush false", text="Что думаешь, [julia.say_name]?")
    call process_character (julia, appearance="pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Здесь мило.")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Тебе стоит проверить нашу ванную, когда будет возможность.")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Там всякие примочки, и прочее!")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Ага!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Мне нравится их использовать.")

    if "simone_scene_1_seq_1" in scenes_completed:
        call character_leave_dissolve (n)
        call process_character (k, appearance="blush false", text="[n.say_name] любит проводить там много времени.")
        call process_character (k, appearance="pose armcross face happy blush false", text="Поэтому нам нужно много бумаги.")
        call character_leave_dissolve (k)
        call process_character (n, appearance="pose behindhead face embarrassed blush false", text="...")

    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armsup face neutral blush false", text="Пускай, [n.say_name] закончит показ дома.")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Мне нужно прибраться после кардиотренировки.")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose handpocket face neutral blush false", text="[k.say_name] делает много упражнений.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Вот почему она в очень хорошей форме.")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armsup face happy blush false", text="Эти мышцы сами себя не сделают!")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="...")
    call process_character (k, appearance="pose handhip face neutral blush false", text="В любом случае, я поговорю с вами позже.")
    call process_character (k, appearance="pose handhip face neutral blush false", text="Увидимся.")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose handfist face neutral blush false", text="Хорошо, в мою комнату!")
    call process_character (julia, appearance="pose handup face neutral blush false", text="...")

    call process_new_location (bg=nate_room, char_tuple_array=[(julia, "pose handface face neutral blush false"), (n, "pose handfist face happy blush false")] )

    call process_character (julia, appearance="pose handface face neutral blush false")
    call process_character (n, appearance="pose handfist face happy blush false", text="А вот и она!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="До этого, [sa.say_name] и я делили одну комнату.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Да, я помню.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Честно говоря, я часто тусуюсь в комнате [sa.say_name].")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Все видеоигры находятся там.")
    call process_character (n, appearance="pose behindhead face happy blush false", text="О!")
    call process_character (n, appearance="pose behindhead face happy blush false", text="Кстати говоря!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="[sa.say_name] и у меня есть наш собственный стрим канал!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Мы также делаем обзоры видеоигр и шоу.")
    call process_character (julia, appearance="pose handface face happy blush false", text="Это круто.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Мы думали, что ты могла бы присоединиться к нам в качестве гостя на нашем следующем стриме!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="[sa.say_name] и я покажу нашу коллекцию игр...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="{cps=40}И мы нашли несколько отличных вариантов, во что можно-{/cps}{w=0.75}{nw}")

    call process_character (julia, appearance="pose armcross face neutral blush false", text="Я не очень люблю видеоигры.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Ой...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="И я бы не хотела появляться в стримах.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Всё хорошо.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="{cps=40}Вы всегда можете смотреть нас, пока ты здесь, чтобы увидеть, как это-{/cps}{w=0.75}{nw}")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Я поняла.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Спасибо, что показал мне дом.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Да без проблем!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Так чем бы ты хотела заняться?")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="[sa.say_name] и у меня целый день свободен!")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Вообще-то, я собиралась спуститься вниз и почитать немного.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Ой...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Хорошо.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты будешь читать комиксы?")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Нет, я читаю роман.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Да ну?")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Мы могли бы по очереди читать!")
    call process_character (julia, appearance="pose handface face curious blush false", text="Думаю, это займет много времени.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Не может быть так плохо.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Сколько страниц в романе?")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Шестьсот страниц.")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="Шестьсот страниц?!")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Да.")
    call process_character (n, appearance="pose handpocket face embarrassed blush false", text="Это бы заняло у меня целую вечность, чтобы прочитать!")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Всё не так уж и плохо.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Я, вероятно, закончу его через пару дней.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...{p}...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="В любом случае, я буду внизу.")
    call process_character (n, appearance="pose twohandfist face concerned blush false", text="Подожди!")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Ты не хочешь поздороваться с [sa.say_name]?")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Она в своей комнате.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Я не хочу беспокоить её.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="{cps=40}О, всё в порядке, она ждала-{/cps}{w=0.75}{nw}")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Я увижу её скоро.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Ты можешь сказать ей, что я в гостиной..")

    call character_leave_dissolve (julia)
    pause 0.5

    call process_character (n, appearance="pose handpocket face concerned blush false", text="...{p}...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="(Думаю, я должен сказать [sa.say_name], что [julia.say_name] не присоединится к нам...)")

    call process_new_location (bg=sam_room, char_tuple_array=[(sa, "outfit clothes pose handface face embarrassed blush false"), (n, "pose behindhead face concerned blush false")] )

    call process_character (n, appearance="pose behindhead face concerned blush false")

    call process_character (sa, appearance="outfit clothes pose handface face embarrassed blush false", text="Она не придёт на стрим?!")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Нет.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Она сказала, что не любит видеоигры.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face concerned blush false", text="Блин, и у нас все было распланировано!")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Да, это очень плохо.")

    call process_character (sa, appearance="pose handface face concerned blush false", text="...{p}...")
    call process_character (sa, appearance="pose handface face concerned blush false", text="Значит, она совсем не увлекается видеоиграми?")
    call process_character (sa, appearance="pose handface face concerned blush false", text="Что ей больше всего нравится?")
    call process_character (sa, appearance="pose handface face concerned blush false", text="Это она тебе рассказала?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Она сказала мне, что собирается почитать книгу.")

    call process_character (sa, appearance="outfit clothes pose handface face angry blush false", text="Читать книгу?!")
    call process_character (sa, appearance="outfit clothes pose handface face angry blush false", text="Ухх!")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Думаю, сейчас она не такая, какой мы её помним.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face angry blush false", text="Вот, что я скажу!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face angry blush false", text="С каких пор ей нравится читать книги?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Она тоже одевается по-другому.")
    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="...")
    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="По-другому?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ну, сходи посмотри сама.")
    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="...")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Похоже, нужно больше веселья, записать в её расписание!")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="И я как раз тот, кто это сделает!")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="(Удачи...)")

    $ reset_all_characters()
    if started_main_game:
        $ had_julia_arrived_scene = True
        call day_reset_locations_chars
        call day_start_after_location_reset
    else:
        jump debug_menu

    return

label edna_pre_arrival_scene:
    call process_scene_beginning (bg="bg kitchen_daytime")
    $ nate_room.decide_and_play_daily_music_queue()

    $ sa.position = "right"
    $ k.position = "right"
    $ julia.position = "right"


    $ display_multiple_characters([ (si, "outfit clothes pose handsfront face neutral blush false"), (n, "outfit clothesjacket pose handpocket face aroused blush false") ])

    call process_character (n, appearance="outfit clothesjacket pose handpocket face aroused blush false", text="{i}Зевает.{/i}..")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Доброе утро соня!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Доброе Утро, Мама.")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Вы с сестрой вчера сидели допоздна?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Хе-хе, да...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Мы играли в новую видеоигру.")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Вы двое теряете чувство времени, когда сосредоточены на новой игре!")

    $ replace_position = True
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="{i}Зевает.{/i}..")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Твой брат только что сказал мне, что у вас была очень активная ночь.")

    if "sam_simone_threesome_scene" in scenes_completed:
        call process_character (si, appearance="pose armunder face curious blush false", text="Вы вдвоем не просто играли в видеоигры прошлой ночью?")
        call process_character (si, appearance="pose armunder face curious blush false", text="Мне показалось, что я слышала шум из твоей комнаты, кроме телевизора...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Ну...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Я бы сказал, что мы играли в видеоигры больше, чем трахались...")
        call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Да...{w=1.0} мы сделали несколько быстрых разов между играми!")
        call process_character (sa, appearance="pose handsbehind face happy blush false", text="Я думаю, что это называется короткий трах!")
    elif "sam_scene_vaginal" in scenes_completed:
        call process_character (sa, appearance="pose handface face concerned blush false", text="A-активная ночь?")
        call process_character (si, appearance="pose armunder face happy blush false", text="Вы оба были поглощены своей видеоигрой!")
        call process_character (sa, appearance="pose handsbehind face happy blush false", text="О-ох, да!")
        call process_character (sa, appearance="pose handsbehind face happy blush false", text="Точно!")
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (si, appearance="pose handsfront face neutral blush false", text="Ты не хотела, чтобы я знала, что ты опять сидишь допоздна?")
        call process_character (sa, appearance="pose handface face concerned blush false", text="(Сначала я подумала, что [n.say_name] рассказал маме о том, что мы...)")
        call process_character (si, appearance="pose handsup face neutral blush false", text="Я знаю, когда вы поздно ложитесь.")
        call process_character (si, appearance="pose handsup face neutral blush false", text="Я слышу, как ты топаешь по коридору, когда ложишься спать!")
        call process_character (sa, appearance="pose handface face curious blush false", text="(Я надеюсь, что она не слышит нас, когда мы трахаемся.)")
        call process_character (sa, appearance="pose handface face curious blush false", text="([n.say_name] и я могу быть довольно шумным...)")
    else:
        call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Да мы играли допоздна!")
        call process_character (sa, appearance="pose handsbehind face happy blush false", text="[n.say_name] и я пытались завершить уровень, который сводил нас с ума!")
        call process_character (n, appearance="pose twohandfist face neutral blush false", text="Этот уровень был таким тяжелым!")
        call process_character (n, appearance="pose twohandfist face neutral blush false", text="Нам пришлось перезапускать его тонну раз!")
        call process_character (sa, appearance="pose handface face angry blush false", text="Я не хотела сдаваться, знала, что его можно победить!")
        call process_character (n, appearance="pose behindhead face neutral blush false", text="Когда наконец закончили, мы оба легли спать.")
        call process_character (sa, appearance="pose leaning face happy blush false", text="Я чуть не уснула на полу!")

    call process_character (si, appearance="pose handsfront face neutral blush false", text="Не забудь хорошенько отдохнуть сегодня.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Завтра у нас напряженный день!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Что?")
    call process_character (sa, appearance="outfit clothes pose handface face embarrassed blush false", text="Мы встанем рано утром?")
    call process_character (sa, appearance="outfit clothes pose handface face embarrassed blush false", text="Обычно мне это не нравится...")
    call process_character (si, appearance="pose handsup face happy blush false", text="Мы наконец-то навестим бабушку!")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Да?!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Бабушка!")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Ей прямо не терпится увидеть нас.")
    call process_character (si, appearance="pose armunder face happy blush false", text="Особенно вас двоих!")
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="Бабушка самая лучшая!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Я надеюсь, что мы сможем сделать помадку, пока мы там!")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Или много печенья!")
    call process_character (si, appearance="pose handsup face happy blush false", text="Хаха, увидим.")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Я слышала громкие, радостные голоса, пока была наверху.")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Почему [n.say_name] и [sa.say_name] так взволнованы?")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Завтра мы увидимся с бабушкой!")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Ох, это правда, Мама?")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Она очень хочет увидеть нас этим летом.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Завтра ты не работаешь, так ведь [k.say_name]?")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="Так случилось, что завтра у меня выходной, так что я свободна!")
    call process_character (si, appearance="pose handsfront face happy blush false", text="Прекрасно!")
    call process_character (si, appearance="pose handsup face happy blush false", text="Бабуля будет рада, что мы все можем прийти!")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Я хотел бы увидеть, как выглядит ее отремонтированная квартира!")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Кажется, она очень довольна ей.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Бабушка прекрасно прижились в местном обществе.")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Мы можем сходит на пляж, пока мы будем там?")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Надеюсь, волны большие!")
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="Если это так, то я точно туда пойду!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Я тоже!")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Я третья!")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Хотя мне нужно купить доску для катания на волнах.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Здорово, что теперь нам не нужно далеко ездить в гости к бабушке.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Мы будем чаще видеться.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Так мы сможем видеться с ней чаще?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Безусловно!")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Вы сможете видеться с ней гораздо чаще!")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Вы говорите о бабушке?")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Да, мы все планировали встретиться с ней завтра!")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Не хочешь пойти с нами?")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Моя мама заберет меня завтра на прием к врачу, так что я не смогу пойти.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="О, это плохо, [julia.say_name].")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Ты собираешься зайти в другой раз?")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Я уверена, что зайду, так как моя мама ходит к ней все время.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Мы уже видели ее отремонтированную квартиру.")
    call process_character (julia, appearance="pose handup face happy blush false", text="Выглядит хорошо.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Хорошо, я рада, что завтра ты не останешься дома одна.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Я была бы обеспокоена.")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Нам нужно спланировать день, где мы все сможем встретиться.")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Было бы весело всей семье потусоваться.")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Надеюсь, что это произойдет этим летом!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Да!")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Это потребует определенного согласования, но мы должны добиться этого.")
    call process_character (si, appearance="pose handsup face happy blush false", text="Но завтра мы проведем время с бабушкой!")

    $ replace_position = False
    $ reset_all_characters()
    if started_main_game:
        $ had_edna_pre_arrival_scene = True
        show screen hud
        $ advance_time_return_location.start(force_music_change = True, morning_wake_lines = False)
    else:
        jump debug_menu

    return

label edna_arrival_scene:
    $ replace_position = True
    call process_scene_beginning (bg="bg edna_house_daytime")
    $ edna_house.decide_and_play_daily_music_queue()

    python hide:
        for char in character_list():
            char.position = "right"

    $ display_multiple_characters([ (edna, "outfit clothes pose handclasp face happy blush false position left mouth red"), (n, "outfit clothesjacket pose twohandfist face happy blush false") ])
    window show
    "Женщина" "Вы здесь!"

    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Бабушка!")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Мы рады быть здесь, бабушка!")
    call change_character_name (edna, prompt="Имя Бабушки")

    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Вы двое очаровательны, как всегда!")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Привет, Бабушка.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="[k.say_name]!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Ты выглядишь готовой выиграть международный спортивный чемпионат!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Ты уже вступила в какие-нибудь спортивные ассоциации?")
    call process_character (k, appearance="pose armsup face happy blush false", text="Пока нет, но я подумываю об этом!")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Привет, Мам.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Вы, наконец, переехали на новое место [si.say_name]?")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Да!")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Были груды коробок, которые мы должны были разобрать, но мы сделали это!")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Когда ты стареешь, как я, ты все меньше и меньше хочешь иметь дело со всем этим.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Вот почему жить в квартире так здорово.")
    call process_character (k, appearance="pose armcross face neutral blush false", text="Это место выглядит великолепно, бабушка!")
    call process_character (k, appearance="pose armcross face neutral blush false", text="Квартира чувствуется совершенно по-новому!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Так и есть.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Это стоило немалых денег, но, думаю, стоило каждого цента.")
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Ты уже привыкла к пенсионной жизни, Мама?")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Может, я и на пенсии, но я остаюсь активной.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Вот почему мне нравится здешняя община.")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Каждый день что-то происходит.")
    call process_character (k, appearance="pose handhip face neutral blush false", text="Хорошо, что ты остаешься активной, Бабушка.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Да, это действительно важно.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Я не собираюсь становиться старым изворотливым пердуном!")
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Ха-Ха, Мама!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Бабушка! Бабушка!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Ты собираешься сделать немного своей помадки?")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Мы можем с этим помочь!")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="[n.say_name] и [sa.say_name] всегда с нетерпением ждут твоих угощений, Мама!")
    call process_character (edna, appearance="outfit clothes pose handhip face concerned blush false", text="Мне жаль вас двоих, но у меня не было возможности купить шоколад, чтобы приготовить помадку...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Ох...")
    call process_character (sa, appearance="pose handface face concerned blush false", text="Без помадки?")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Но я купила мороженое и шоколадный сироп!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Чтобы мы могли сделать молочные коктейли!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="{i}Вздох!{/i}")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Ты сказала молочные коктейли?!")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="О боже, ты сказала волшебное слово, Мама, ха-ха!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Две порции шоколада мне!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Мне нравится моя супер густой с дополнительным мороженым!")
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Вы двое будете бегать всю ночь с таким количеством шоколада в вас!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Они все это сожгут дотла.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Особенно, если они пойдут на пляж.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Мы можем пойти туда в ближайшее время?")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Я хочу пойти поплавать!")

    if "simone_scene_swimsuit" in scenes_completed and "sam_scene_swimsuit" not in scenes_completed:
        call process_character (si, appearance="pose armunder face curious blush false", text="Но тебе нужен новый купальный костюм, не так ли [sa.say_name]?")
        call process_character (sa, appearance="blush false", text="Точно, всё правильно...")
        call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты принесла мой купальник, Мама?")
        call process_character (si, appearance="pose armunder face happy blush false", text="Ты знаешь, твой и мой лежали у двери, и я забыла взять их, когда мы уходили!")
        call process_character (si, appearance="pose handsup face neutral blush false", text="Мы купим [sa.say_name] новый купальник, и я обязательно принесу их все в следующий раз!")
        call process_character (edna, appearance="pose handclasp face neutral blush false", text="Мы все еще можем сходить туда.")
        call process_character (edna, appearance="pose handclasp face neutral blush false", text="Просто оставь свои туфли и носки здесь и закатай штаны!")
    elif "simone_scene_swimsuit" not in scenes_completed and "sam_scene_swimsuit" in scenes_completed:
        call process_character (si, appearance="pose armunder face curious blush false", text="Ты не забыла взять свой купальник?")
        call process_character (sa, appearance="pose handface face concerned blush false", text="Ох...")
        call process_character (sa, appearance="pose handface face concerned blush false", text="Я думала, ты его возьмёшь, Мама.")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Я тоже об этом подумала...")
        call process_character (si, appearance="pose handsfront face neutral blush false", text="Я просила взять ваши купальники, но вы, возможно, не слышали меня снизу.")
        call process_character (edna, appearance="pose handclasp face neutral blush false", text="Мы все еще можем сходить туда.")
        call process_character (edna, appearance="pose handclasp face neutral blush false", text="Просто оставь свои туфли и носки здесь и закатай штаны!")
    else:
        call process_character (si, appearance="pose armunder face curious blush false", text="Тебе нужен новый купальный костюм, не так ли [sa.say_name]?")
        call process_character (sa, appearance="pose handsbehind face concerned blush false", text="Точно, всё правильно...")
        call process_character (si, appearance="pose armunder face curious blush false", text="[n.say_name], ты не забыл взять свои плавки?")
        call process_character (n, appearance="pose behindhead face curious blush false", text="О...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Я думал, ты взяла их, Мама.")
        call process_character (si, appearance="pose handsfront face neutral blush false", text="Я просила взять с собой, но ты, возможно, не слышал меня снизу.")
        call process_character (edna, appearance="pose handclasp face neutral blush false", text="Мы все еще можем сходить туда.")
        call process_character (edna, appearance="pose handclasp face neutral blush false", text="Просто оставь свои туфли и носки здесь и закатай штаны!")


    call process_character (k, appearance="pose armsup face happy blush false", text="Я подготовилась и взяла свой купальник!")
    call process_character (si, appearance="pose handsup face happy blush false", text="В этом нет ничего удивительного!")
    call process_character (si, appearance="pose handsup face neutral blush false", text="[k.say_name] любит наш бассейн на заднем дворе.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Она загорает там все время.")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Это объясняет, почему ты такая загорелая [k.say_name]!")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Я сама хотела бы больше выходить на солнце.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Но мне нужно защищать голову шляпой.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Мои волосы больше не защищают меня от солнца.")
    call process_character (k, appearance="pose handhip face neutral blush false", text="Твоя прическа все еще выглядит очень мило, Бабушка.")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Спасибо [k.say_name].")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Хотела бы я, чтобы было чуть меньше седого!")
    call process_character (edna, appearance="pose handhip face happy blush false", text="По крайней мере, я все еще могу его стильно уложить их.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Вода в океане теплая, Бабушка?")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="А волны большие?")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Я не проверяла сегодня, так почему бы нам самим не посмотреть?")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Давайте направимся туда.")
    call process_character (k, appearance="pose armcross face happy blush false", text="Звучит хорошо!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Да, я готова отправляться в путь!")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Там может быть немного жарковато.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Мне нужно оставаться в тени.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Достаньте из холодильника воду, чтобы не допустить обезвоживание.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="О! Пока не забыла...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Что случилось, Бабушка?")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Каждому из вас понадобится пропуск, если вы собираетесь посещать пляж чаще.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="В противном случае мне придется звонить в офис кондоминиума и регистрировать вас в качестве гостей каждый раз, когда вы захотите его посетить.")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Это сделает его легкодоступным для любого из вас, чтобы приходить и уходить, как вам заблагорассудится!")
    call process_character (sa, appearance="pose handface face concerned blush false", text="Это займет много времени?")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Это очень быстро, [sa.say_name]!")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Пляж будет сразу, как только это будет сделано.")

    call process_new_location ("bg beach_daytime")

    python hide:
        for char in character_list():
            char.position = "right"
            char.outfit = "clothes"


    pause 0.25
    $ display_multiple_characters([ (edna, "outfit clothes pose handhip face neutral blush false position left hat sunhat mouth red"), (k, "outfit bikini pose armsup face happy blush false") ])
    pause 0.25

    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="О, боже!")
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="Это просто потрясающе, что ты живёшь рядом с пляжем, Бабушка!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Я хожу сюда каждое утро прогуляться.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Запах океанского бриза - отличный способ начать день.")
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="Держу пари!")
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="На этом все, меня купили!")
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="Я собираюсь накопить денег и купить здесь дом!")
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Это может быть немного сложно, [k.say_name]!")
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Тебе должно быть пятьдесят пять лет или старше!")
    call process_character (k, appearance="outfit bikini pose armcross face embarrassed blush false", text="Черт, правда?!")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Я могу понять ограничение.")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Много пожилых людей хотят иметь мирный и тихий дом.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="И они не хотят, чтобы рядом дети сходили с ума.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Ночные вечеринки и громкая музыка - это всё не здесь.")
    call process_character (k, appearance="outfit bikini pose handhip face concerned blush false", text="Да...{w=1.0}это имеет смысл.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Но я знаю, как мои внуки себя ведут!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Если кто-то из вас хочет остаться на несколько ночей!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="У меня есть свободная спальня и раскладной диван, если нужно.")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Вы слышите [sa.say_name], [n.say_name], и [k.say_name]?")
    call process_character (n, appearance="outfit clothes pose handfist face happy blush false", text="Чтобы мы можем остаться, если захотим?")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Это было бы замечательно!")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Что ты должен сказать Бабушке?")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="Спасибо, Бабушка!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Огромное спасибо!")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Да, спасибо, Бабушка.")
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="Я обязательно воспользуюсь этим предложением!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Всегда пожалуйста!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Итак, как насчет воды?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Я могу только замочить ноги, но это приятно!")

    if "janet_scene_minigame_intro" in scenes_completed or "janet_scene_naked" in scenes_completed:
        call process_character (n, appearance="pose handsdown face neutral blush false", text="Я плавал здесь раньше с тётей [janet.say_name], и вода действительно теплая!")
        call process_character (edna, appearance="pose fisthip face neutral blush false", text="Да, это любимый пляж [janet.say_name].")
        call process_character (edna, appearance="pose fisthip face neutral blush false", text="Иногда я вижу, как она плавает взад и вперед в океане.")
        call process_character (edna, appearance="pose fisthip face curious blush false", text="Мне кажется, я видела вас, [n.say_name].")
        call process_character (n, appearance="pose handfist face happy blush false", text="Тетя [janet.say_name] и я играем в догонялки в океане иногда, так это наверное был я!")
        call process_character (edna, appearance="pose handhip face happy blush false", text="Ах, это тебя я тогда видела!")
    else:
        call process_character (n, appearance="pose behindhead face neutral blush false", text="Хотел бы я взять свои плавки, чтобы поплавать.")
        call process_character (n, appearance="pose behindhead face happy blush false", text="Вода кажется очень теплой!")
        call process_character (edna, appearance="pose handclasp face neutral blush false", text="Этим летом солнце сильно нагрело воду.")
        call process_character (edna, appearance="pose handclasp face neutral blush false", text="Пока нет дождя, температура должна оставаться такой некоторое время.")

    call process_character (sa, appearance="pose handface face happy blush false", text="Надеюсь, волны будут большими, когда мы будем здесь в следующий раз!")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="О, я уверена, что они будут.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Ветер сгладил волны сегодня..")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Но я слышала, что в ближайшие дни все изменится.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Тогда вы должны увидеть большие волны.")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Не могу дождаться!")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Эй, здесь есть волейбольные сетки, которые мы можем установить?")
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Ох, кому что...")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Я думаю, что есть, да!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Спроси у будки спасателей.")
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="Кто-нибудь будет?")
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="Как насчет меня и [sa.say_name] против [n.say_name] и Мамы?")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="...")
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Думаю, я откажусь от предложения!")
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="У меня нет подходящего наряда.")
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="И даже если бы и знала, я не очень хороша в волейболе!")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="Как насчет тебя, Бабушка?")
    call process_character (edna, appearance="outfit clothes pose handhip face embarrassed blush false", text="Это слишком интенсивный вид спорта для меня!")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Хорошо, тогда в таком случае...")
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="Мне придется довольствоваться матчем с гандикапом!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="Гандикап матч?")
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="Ты и [sa.say_name] против меня!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Это звучит весело [n.say_name]!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Мы можем победить [k.say_name] вместе!")
    call process_character (k, appearance="outfit bikini pose armcross face happy blush false", text="Я хотела бы попробовать!")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="...")
    call process_character (si, appearance="outfit clothes pose handsup face curious blush false", text="[k.say_name], постарайся сильно не бить, хорошо?")
    call process_character (si, appearance="outfit clothes pose handsup face curious blush false", text="Это будет плохо, если [n.say_name] или [sa.say_name] получат удар в лицо.")
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="Ааа, это просто укрепляет силу духа!")
    call process_character (si, appearance="outfit clothes pose handsup face concerned blush false", text="[k.say_name]...")
    call process_character (n, appearance="outfit clothes pose handsdown face concerned blush false", text="{i}Вздох.{/i}.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Я хочу снять это на видео!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="[n.say_name], у тебя есть один из этих супер телефонов?")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="Ты имеешь в виду смартфон, Бабушка?")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Да!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Можешь показать мне, как снимать видео?")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Я ненавижу его, как сложна эта новая технология!")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="Конечно.")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="{cps=40}Первое, что ты делаешь, это запускаешь приложению здесь, а затем ты-{/cps}{w=0.75}{nw}")
    call process_character (edna, appearance="outfit clothes pose handclasp face shock blush false", text="Ты показываешь слишком быстро!")
    call process_character (edna, appearance="outfit clothes pose handclasp face shock blush false", text="Что за кнопку ты нажал?")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="...")

    call process_new_location ("bg edna_house_daytime")

    python hide:
        for char in character_list():
            char.position = "right"
            char.outfit = "clothes"


    pause 0.25
    $ display_multiple_characters([ (edna, "outfit clothes pose handclasp face neutral blush false position left mouth red"), (si, "outfit clothes pose handsup face neutral blush false") ])
    pause 0.25

    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Вы отлично провели время на пляже, не так ли?")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Я уверена, что да!")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="Я могу остаться там на весь день!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Я определенно хочу вернуться снова!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Кажется, нас всех привлекает пляж.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Думаю, это у нас семейное!")
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Какой волейбольный матч [k.say_name], [sa.say_name], и [n.say_name]!")
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Голова кружилась, пока я смотрела на это!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Вы все держались хорошо.")
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="Мне понравился вызов!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ты делала какие-то эпические прыжки, чтобы достать мяч [k.say_name]!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Но [n.say_name] и я набрали несколько очков!")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Признаюсь, ты застала меня врасплох несколько раз.")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="Но я не собиралась позволить тебе победить!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Да...{w=1.0}Я могу сказать, что ты хотела выиграть, когда била по мячу.")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Я направляла его подальше от [n.say_name].")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="Он всё бегал, пока я это делала, ха-ха!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Вы планировали остаться на ужин?")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="В кондоминиуме работает отличный ресторан.")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Спасибо за предложение, Мама, но нам пора возвращаться.")
    call process_character (sa, appearance="pose handface face concerned blush false", text="Уже?")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Помнишь, что Бабушка говорила раньше?")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Ты можешь приходить сюда в любое время.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Нет недостатка вещей, что можно сделать, когда ты с Бабушкой!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="В следующий раз я обязательно приготовлю помадку, чтобы ты взял домой.")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Даа!")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Пока, Бабушка!")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Это здорово, что у тебя все хорошо!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Мы отлично провели время, Бабушка!")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Молочные коктейли были очень вкусными!")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Спасибо Мама, я поговорю с тобой позже!")

    $ replace_position = False
    $ reset_all_characters()
    if started_main_game:
        $ had_edna_intro_scene = True
        call day_reset_locations_chars
        call day_start_after_location_reset
    else:
        jump debug_menu

    return