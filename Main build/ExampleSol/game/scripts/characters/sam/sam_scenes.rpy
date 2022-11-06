init python:
    def sam_grind_set_speed(label, is_revisit):
        renpy.call(label, is_revisit)
        
        return

label sam_scene_1_seq_1:
    $ display_multiple_characters([ (n, ""), (sa, "pose leaning face neutral") ])

    call process_character (sa, appearance="pose leaning face neutral", text="Ты готов к стриму со мной?")
    call prompt_menu_boldness_check ("Безусловно!", "Не совсем.", "sam_scene_1_seq_1", sa)

    return

label sam_scene_1_seq_1_refusal(text, insufficient_points):
    call process_character (sa, appearance="pose handsbehind face neutral", text="Я так взволнована!")
    call prompt_refusal_end (sa)
    return

label sam_scene_1_seq_1_sex(dream=False):
    call process_scene_beginning (sam_room, char_tuple_array=[ (n, "outfit clothesjacket"), (sa, "outfit clothes pose handface") ], dream=dream )

    call process_character (sa, appearance="pose handface face neutral", text="Если мы будем транслировать новые игры, это наверняка привлечет больше зрителей.")
    call process_character (n, appearance="pose handpocket face concerned", text="Как мы можем отделить себя от такой большой толпы конкурентов?")
    call process_character (sa, appearance="pose leaning face neutral", text="Ну, мы близнецы, например.")
    call process_character (n, appearance="pose handpocket face neutral", text="И это хорошо, но уже есть братские и сестринские каналы.")
    call process_character (n, appearance="pose behindhead face curious", text="Нам нужно что-то другое.")
    call process_character (n, appearance="pose behindhead face curious", text="Но что именно?")
    call process_character (sa, appearance="pose handface face curious", text="{i}Хмм{/i}...{p=1.0}Нуу...")
    call process_character (sa, appearance="pose handface face neutral", text="Мы могли бы попробовать этот новый тренд \"Кожа к Победе\".")
    call process_character (n, appearance="pose handpocket face concerned", text="Кожа к Победе?")
    call process_character (sa, appearance="pose handface face neutral", text="Да.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Снимаешь часть одежды, и чем больше кожи показываешь, тем больше зрителей.")
    call process_character (sa, appearance="pose handface face concerned", text="По крайней мере, так это должно работать.")
    call process_character (n, appearance="pose handfist face neutral", text="Ты хочешь попробовать это сделать?")
    call process_character (sa, appearance="pose leaning face neutral", text="Не понимаю, почему бы и нет.\nДавай попробуем...")


    call character_leave_dissolve (sa)
    $ renpy.pause(1)
    call process_character (sa, appearance="outfit underwear pose handsbehind face happy", text="Кожа к Победе!")

    call process_character (n, appearance="pose behindhead face neutral", text="Зачем так громко?")
    call process_character (sa, appearance="pose handface face neutral", text="Ты должен это кричать, когда снимаешь одежду.")
    call process_character (sa, appearance="pose handface face neutral", text="Это что-то вроде объявления.")

    call character_leave_dissolve (n)
    $ renpy.pause(1)
    call process_character (n, appearance="outfit underwear pose handsdown face happy", text="Кожа к победе!")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral", text="Вот так?")
    call process_character (sa, appearance="pose handface face happy", text="У тебя получилось!")
    call process_character (sa, appearance="pose leaning face neutral", text="Хорошо, позволь мне запустить стрим.")
    call static_still ("bg black")
    "Час спустя"
    call bust_art_background (sam_room)
    $ display_multiple_characters([ (n, "outfit underwear pose handsdown face neutral"), (sa, "outfit underwear pose handface face curious") ])
    call process_character (sa, appearance="outfit underwear pose handface face curious", text="Окей...Думаю, улучшение оружия здесь, в долине.")

    call process_character (n, appearance="pose behindhead face neutral", text="Я думал ты уже убежала туда.")
    call process_character (sa, appearance="pose handface face concerned", text="Я? Я думала, ты.")
    call process_character (sa, appearance="pose handface face curious")
    call process_character (n, appearance="pose behindhead face neutral")
    call process_character (sa, text="Я уверена, что нет.")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose leaning face neutral", text="Просто, чтобы все знали, мы не стримим каждую \"Безфутоболчную субботу\"!")
    call process_character (n, appearance="pose twohandfist face neutral", text="А также, мы не пользуемся руководствами на этом стриме!")
    call process_character (n, appearance="pose handfist face happy", text="Только нубы используют руководствам!")
    call process_character (n, appearance="pose handsdown face neutral")
    call process_character (sa, appearance="pose handsbehind face neutral", text="О, смотри! Человек-блинчик57 уже подписался!")
    call process_character (sa, appearance="pose handsbehind face happy", text="Спасибо, мистер Человек-блинчик57 ты вкусная еда на завтрак!")
    call process_character (sa, appearance="pose leaning face neutral", text="Ох! Крутящийся Ключ также подписался!")
    call process_character (n, appearance="pose behindhead face happy", text="Добро пожаловать!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Для тех из вас, кто только подключился, у нас активирован \"режим без штанов\"!")
    call process_character (n, appearance="pose twohandfist face happy")
    call process_character (sa, appearance="pose leaning face happy")
    $ temp_name = n.say_name + " и " + sa.say_name
    "[temp_name]" "Кожа к Победе!"
    call process_character (sa, appearance="pose handsbehind face neutral")
    call process_character (n, appearance="pose handfist face neutral", text="Смущатель только подписался и говорит")
    call process_character (n, text="\"Хотелось бы, чтобы каждый день был в режиме без штанов!\"")
    call process_character (n, text="Ну, что ж скоро это может стать реальностью, Смущатель!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Если мы получим 10 подписчиков на этом стриме, это гарантирует, что режим без штанов будет включен постоянно!")
    call process_character (n, appearance="pose twohandfist face happy")
    $ n.c(sa.say_name + " смотри!")
    call process_character (n, text="Мы только что получили еще 3 подписчика!")
    call process_character (sa, appearance="pose leaning face happy", text="Этот стрим идет удивительно!")
    call static_still_ctc ("bg sam_1_playing")

    call process_character (n, text="(Это была такая отличная идея!)")
    call process_character (n, text="(Мы легко достигнем 10 подписчиков за этот стрим!)")
    $ n.c("(" + sa.say_name + " \"Кожа к Победе\" было верным решением!)")
    $ renpy.pause(1)
    call static_still_ctc ("bg sam_1_sam_playing")
    call process_character (n, text="(Это странно)")
    call process_character (n, text="(Глядя на мою сестру, я чувствую себя еще счастливее)")
    call process_character (n, text="(Мне нравится видеть ее в нижнем белье)")
    $ renpy.pause(1)
    call process_character (n, text="(Я не могу дождаться, пока мы сделаем это снова!)")
    call static_still_ctc ("bg sam_1_nate_playing")
    call process_character (sa, text="(Этот стрим-только начало, я это чувствую!)")
    $ renpy.pause(1)
    call process_character (sa, text="(Я чувствую, что-то еще )")
    call process_character (sa, text="(Он чувствует себя хорошо)")
    $ sa.c( "(И, когда я смотрю на " + n.say_name + ")" )
    $ renpy.pause(1)
    call process_character (sa, text="(Мне всегда нравится быть рядом с моим братом, но это другое чувство)")
    $ renpy.pause(1)
    call process_character (sa, text="(Мы сделаем это снова очень скоро!)")

    python:
        if not dream:
            stats.add_stat("times_seen_panties", 1)
            stats.add_stat("times_seen_bra", 1)
            stats.add_stat("times_seen_in_underwear", 1)

    call process_end_of_scene ("sam_scene_1_seq_1", char=sa, dream=dream, force_no_boldness=True)

    return

label sam_scene_1_seq_2:
    $ display_multiple_characters([ (n, ""), (sa, "pose handsbehind face neutral") ])

    call process_character (sa, appearance="pose handsbehind face neutral", text="Давай еще стримить!")
    call prompt_menu_boldness_check ("Я готов к этому!", "Позволь мне кое-что сделать.", "sam_scene_1_seq_2", sa)

    return

label sam_scene_1_seq_2_refusal(text, insufficient_points):
    call process_character (sa, appearance="pose leaning face neutral", text="Дай мне знать, когда захочешь начать!")
    call prompt_refusal_end (sa)
    return

label sam_scene_1_seq_2_sex(dream=False):
    call process_scene_beginning (sam_room, char_tuple_array=[ (n, "outfit clothesjacket"), (sa, "outfit clothes pose leaning") ], dream=dream )

    call process_character (sa, text="Ладно, это еще один загруженный обзор!")
    call process_character (n, text="Как наш предыдущий обзор?")
    call process_character (sa, appearance="pose handface face happy", text="Всем понравилось! \nПочти 2,500 просмотров!")
    call process_character (n, appearance="pose twohandfist face happy", text="Круто! \nТы в видео написала ссылку на наш стрим?")
    call process_character (sa, appearance="pose handface face neutral", text="Ну конечно!")
    $ renpy.pause(1)
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (sa, appearance="pose handface face neutral", text="Кстати говоря...")

    call character_leave_dissolve (sa)
    $ renpy.pause(1)
    call process_character (sa, appearance="outfit underwear pose handsbehind face neutral", text="Время, чтобы запустить наш стрим снова! \nЯ вполне готова!")

    call character_leave_dissolve (n)
    $ renpy.pause(1)
    call process_character (n, appearance="outfit underwear pose handfist face happy", text="Готов как всегда!")

    call fade_to_black (1.5)

    "Немного позже..."
    call bust_art_background (sam_room)
    $ display_multiple_characters([ (n, "pose behindhead face neutral outfit underwear"), (sa, "outfit underwear pose handsbehind face neutral") ])

    call process_character (n, appearance="pose behindhead face neutral", text="Может, тебе стоит вернуться к этому боссу с лучшей экипировкой.")
    call process_character (sa, appearance="pose handface face angry", text="Нет! Я точно могу с ним разобраться! \nВ последний раз я добила его до половины здоровья!")
    call process_character (n, appearance="pose behindhead face neutral")
    $ renpy.pause(1)
    call process_character (n, appearance="pose handfist face neutral", text="Просто напоминаю всем.")
    call process_character (n, appearance="pose handfist face neutral", text="Не забудьте посмотреть наш новый канал [video_sharing_site], \"Твинстикс\"!")
    call process_character (sa, appearance="pose leaning face neutral", text="Мы публикуем обзоры игр, анимационных фильмов и шоу!")
    call process_character (sa, appearance="pose leaning face neutral", text="Наш последний обзор на \"Шериф Буги-вуги\".")
    $ sa.c(n.say_name + " очень понравилось.")
    call process_character (n, appearance="pose twohandfist face happy", text="Шоу просто великолепное! \nКрутая музыка и экшен!")
    call process_character (n, appearance="pose handsdown face neutral", text="Жаль, что серии короткие.")
    call process_character (sa, appearance="pose handface face neutral", text="Космическая Причуда говорит \"лучше, когда шоу непродолжительное и крутое.\"")
    call process_character (sa, appearance="pose handface face neutral", text="Я склонна согласиться с Причудой!")
    call process_character (sa, appearance="pose handface face neutral", text="Нет ничего хуже, чем шоу, которое длится слишком долго.")
    call process_character (n, appearance="pose behindhead face neutral", text="Да, как \"Зоркимон.\"")
    call process_character (sa, appearance="pose handsbehind face angry", text="{i}Угх{/i}, даже не напоминай.")
    call process_character (n, appearance="pose twohandfist face neutral", text="Еще раз спасибо всем, кто недавно подписался!")
    call process_character (sa, appearance="pose leaning face neutral", text="Благодаря вашим подводным лодкам, \"режим без штанов\" теперь активен на каждом будущем стриме!")
    call process_character (sa, appearance="pose leaning face happy", text="И еще один только что! \nДобро пожаловать, Неоновый Искатель, добро пожаловать!")
    call static_still_ctc ("bg sam_1_playing")
    call process_character (sa, text="Я уверена, что ещё больше людей присоединятся к нам в ближайшее время!")
    call process_character (n, text="Надеюсь, мы не застрянем на этом боссе!")
    call process_character (sa, text="Может мне просто нужна другая конфигурация оружия. {p=1.0}{i}Хмм{/i}...")
    call static_still_ctc ("bg sam_1_sam_playing")
    call process_character (n, text="(Моя сестра действительно сосредоточена на избиении этого босса)")
    call process_character (n, text="(Я бы давно сдался)")
    $ renpy.pause(2)
    call process_character (n, text="(Она симпатичная, когда она такая сосредоточенная)")

    if not dream or persistent.disable_dream_music:
        $ play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg sam_1_sam_playing_nip_slip")
    call process_character (n, text="(Э-это её...){p=1.0}{i}!!{/i}")
    call static_still_ctc ("bg sam_1_sam_playing_nip_zoom")
    call process_character (n, text="(Я вижу её грудь!)")
    $ renpy.pause(1)
    call process_character (n, text="(Она не замечает, что я вижу это со стороны)")
    call process_character (n, text="(Надеюсь, стрим не видит этого.)")
    call bust_art_background (sam_room)
    $ display_multiple_characters([ (n, "pose handsdown face concerned blush true"), (sa, "pose handface face happy") ])

    call process_character (sa, appearance="pose handface face happy", text="Да! \nЯ сделала!")
    call process_character (sa, appearance="pose handface face happy", text="Босс пал!")
    $ sa.c("Ты видел, как я сделала это " + n.say_name + "?")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="О-ох...{p=1.0}Д-да!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Ты сделала его!")
    call process_character (n, appearance="pose handsdown face neutral blush true", text="Какое оружие ты использовала?")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Я должна была понять это раньше,{p=1.0} у этого босса слабость к бронебойному!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Поэтому я поменяла свой посох на элементальный меч.")
    call process_character (n, appearance="pose handsdown face neutral blush false")
    call process_character (sa, appearance="pose leaning face neutral", text="И БАМ! \nОн быстро сдох!")
    call process_character (n, text="Круто!")
    call process_character (sa, text="Я поняла это до того, как чат написал!")
    call process_character (sa, text="Это довольно впечатляюще!")
    call process_character (n, text="Хочешь попробовать еще разок?")
    call process_character (sa, appearance="pose handface face neutral", text="У нас осталось немного времени.")
    call process_character (sa, appearance="pose handface face happy", text="Давай сделаем это!")
    call process_character (n, appearance="pose handfist face neutral", text="Не забудь забрать добычу с босса!")
    call process_character (sa, appearance="pose leaning face neutral", text="Ничего себе, почти забыла! \nЯ думала о том, насколько будет сложный следующий босс.")
    call process_character (sa, appearance="pose handface face neutral", text="Мне придется сильно сосредоточиться, чтобы победить его!")
    call process_character (n, appearance="pose behindhead face neutral", text="(Если это означает, что она будет наклоняться снова...)")
    call process_character (n, appearance="pose behindhead face neutral blush true", text="(Я не против)")

    python:
        if not dream:
            stats.add_stat("times_seen_panties", 1)
            stats.add_stat("times_seen_bra", 1)
            stats.add_stat("times_seen_in_underwear", 1)
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_flat_breasts", 1)

        sa.revistable_scenes.add("sam_scene_1_revisit")

    call process_end_of_scene ("sam_scene_1_seq_2", char=sa, dream=dream)

    return

label sam_scene_1_revisit:
    call process_character (n, appearance="pose twohandfist face neutral")
    call process_character (sa, appearance="pose handface face happy", text="Я только что заходила на [video_sharing_site]!")

    call process_scene_beginning ("bg sam_1_playing")

    call process_character (sa, text="Получила второе окончательное улучшение оружия для посоха!")
    call process_character (n, text="Этого должно быть достаточно, чтобы убить босса.")
    call process_character (sa, text="Мне еще нужно уклоняться от ракетных атак.")
    call process_character (n, text="Я могу стоять и лечить тебя.")
    call process_character (sa, text="Не такая уж плохая идея.")
    call process_character (sa, text="Я могу вызывать удар на себя, чтобы он держался от тебя подальше.")
    call process_character (n, text="Хорошо, я подготовлю своего персонажа.")
    call process_character (sa, text="Ладненько, надеюсь, что ты готов к этой эпической битве!")

    call static_still_ctc ("bg sam_1_sam_playing")
    call process_character (sa, text="Продолжай лечить меня!")
    call process_character (n, text="Мне приходится много бегать, чтобы добраться до тебя!")
    $ renpy.pause(1)
    call process_character (n, text="Хорошо, я нашел хорошее место.")
    call process_character (n, text="(Я нахожусь в безопасной зоне комнаты напротив босса)")
    call process_character (n, text="(Кроме того, я могу лечить [sa.say_name] легко отсюда)")
    call process_character (n, text="(Она яростно давит на кнопки)")
    call process_character (n, text="(С такой скоростью мне интересно, будет ли ее бюстгальтер...)")

    $ play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)
    call static_still_ctc ("bg sam_1_sam_playing_nip_slip")

    call process_character (n, text="(Это не заняло много времени!)")
    call process_character (n, text="(Я знаю, что должен следить за битвой)")
    call process_character (n, text="(Но я не могу не продолжать смотреть на нее)")
    call process_character (sa, text="[n.say_name], мне нужно полечиться!")
    window hide

    menu:
        "{i}Лечить персонажа [sa.say_name]{/i}":
            call add_points (sa, 1, tag="sam_scene_1_revisit_need_heals")
            call process_character (n, text="Супер исцеление готово!")
            call process_character (sa, text="Да! Здорово!")
            call process_character (sa, text="С этим боссом покончено!")
            call process_character (sa, text="Это происходит, когда ты работаешь в команде!")
        "{i}Продолжить пялиться{/i}":
            call add_boldness (1, tag="sam_scene_1_revisit_need_heals")
            call static_still_ctc ("bg sam_1_sam_playing_nip_zoom")
            call process_character (n, text="...")
            call process_character (sa, text="[n.say_name]!")
            call process_character (n, text="Ух ты!!")
            call process_character (sa, text="Ух ты!")
            call process_character (sa, text="Мне повезло, что у меня было лишнее зелье!")
            call process_character (n, text="Моя ошибка, я не уследил, где ты была.")
            call process_character (sa, text="Все нормально.")
            call process_character (sa, text="Этот босс уже в прошлом!")


    call bust_art_background (sam_room)
    $ display_multiple_characters([ (n, "pose handsdown face neutral outfit underwear"), (sa, "outfit underwear pose handface face happy") ])
    call process_character (sa, appearance="pose handface face happy", text="{i}Мм{/i}! О, да!")
    call process_character (sa, appearance="pose leaning face happy", text="Все это видели?")
    call process_character (sa, appearance="pose leaning face happy", text="Первый бой с этим злодеем и сразу победа!")
    call process_character (n, appearance="pose twohandfist face happy", text="Мы получили за это достижение!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Безусловно мы это сделали!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="И это не так просто сделать!")
    call process_character (sa, appearance="pose handface face neutral", text="Я думаю, что мы получим бонусы!")
    call process_character (n, appearance="pose handfist face neutral", text="Может быть, последнее обновление на посох!")
    call process_character (sa, appearance="pose handface face neutral", text="По крайней мере, дадут материалы для его изготовления.")
    call process_character (n, appearance="pose handsdown face neutral", text="Смотри, у нас появились новые подписчики после того боя!")
    call process_character (sa, appearance="pose leaning face neutral", text="Уничтожитель Корзин говорит,")
    call process_character (sa, appearance="pose leaning face neutral", text="\"Я сражался с этим боссом по крайней мере 8 раз, прежде чем победить его, и вы, ребята, просто разнесли его\"")
    call process_character (n, appearance="pose handsdown face neutral", text="Я думаю играть немного легче, когда вы играете в кооперативе.")
    call process_character (sa, appearance="pose handface face neutral", text="В этом есть смысл.")
    call process_character (sa, appearance="pose handface face neutral", text="Я практически заставила тебя лечить меня, и почти не использовала зелья.")
    call process_character (n, appearance="pose twohandfist face neutral", text="Похоже, наверху есть платформы с сундуками с сокровищами.")
    call process_character (sa, appearance="pose leaning face happy", text="Предоставь это мне!")

    call static_still_ctc ("bg sam_1_sam_playing_nip_slip")
    $ renpy.pause(1)
    call process_character (n, text="(Я надеюсь, что она надолго застрянет на платформах)")

    python:
        stats.add_stat("times_seen_panties", 1)
        stats.add_stat("times_seen_bra", 1)
        stats.add_stat("times_seen_in_underwear", 1)
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_flat_breasts", 1)

    call process_end_of_scene ("sam_scene_1_revisit", char=sa, force_no_boldness=True, reset_prompted_scene=False, force_not_replayable=True, revisit=True)
    return

label sam_scene_2_seq_1:
    $ display_multiple_characters([ (n, ""), (sa, "pose handface face neutral") ])

    call process_character (sa, text="У меня есть что добавить на наш канал!")
    call prompt_menu_boldness_check ("Здорово, что?", "Подожди, скажи мне позже, я вернусь через некоторое время.", "sam_scene_2_seq_1", sa)

    return

label sam_scene_2_seq_1_refusal(text, insufficient_points):
    if insufficient_points:
        call process_character (n, appearance="pose handpocket face neutral", text=text)
        call process_character (n, appearance="pose handpocket face curious", text="(Я не чувствую себя достаточно {b}уверенным{/b} для этого)")

    call process_character (sa, appearance="pose handsbehind face neutral", text="Окей!")
    call prompt_refusal_end (sa)
    return

label sam_scene_2_seq_1_sex(dream=False):
    call process_scene_beginning (sam_room, char_tuple_array=[ (n, "outfit clothesjacket pose handfist face happy"), (sa, "outfit clothes pose handsbehind") ], dream=dream )

    call process_character (n, appearance="pose handfist face happy", text="Похоже, что наш канал получает новых подписчиков каждый день!")
    call process_character (sa, appearance="pose handsbehind", text="У нас хорошо получается.")
    call process_character (sa, appearance="pose handface face concerned", text="Стабильный рост.")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (sa, appearance="pose handface face neutral", text="Зрителям очень понравился наш последний обзор,")
    call process_character (sa, appearance="pose handface face neutral", text="И им понравилось, благодаря твоим комментариям, как всегда.")
    call process_character (sa, appearance="pose handsbehind face neutral")
    call process_character (n, appearance="pose behindhead face neutral", text="Ну, ты делаешь много сложных вещей таких, как редактирование.")
    call process_character (n, appearance="pose behindhead face neutral", text="Это занимает много времени.")
    call process_character (n, appearance="pose behindhead face neutral", text="Без правок обзоры не смотрели бы так хорошо.")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (sa, appearance="pose leaning face happy", text="Также здорово делать это в нижнем белье.")
    call process_character (n, appearance="pose behindhead face neutral")
    $ renpy.pause(1)
    call process_character (n, appearance="pose behindhead face neutral", text="Да, мне нравится это делать.")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (sa, appearance="pose handface face neutral", text="Чувствую себя более сосредоточенной и комфортней, когда мы почти голые, ты знаешь?")
    $ renpy.pause(2)
    $ n.c(sa.say_name + ".")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Ага?")
    call process_character (n, appearance="pose behindhead face neutral", text="Мне...")
    $ renpy.pause(1)
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Мне нравится видеть тебя в нижнем белье.")
    call process_character (sa, appearance="pose handsbehind face embarrassed blush true", text="Да?")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Да.")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Мне нравится сидеть рядом с тобой во время обзора и, смотреть на тебя.")
    call process_character (sa, appearance="pose handsbehind face embarrassed blush true", text="И...")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose handsbehind face concerned blush true", text="Я чувствую то же самое.")
    call process_character (n, appearance="pose behindhead face embarrassed blush true")
    $ renpy.pause(1)
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Правда?")
    call process_character (sa, appearance="pose handface face concerned blush true", text="Я...")
    call process_character (sa, appearance="pose handface face concerned blush true", text="Я хочу...")
    call process_character (sa, appearance="pose handface face concerned blush true", text="Увидеть тебя в нижнем белье.")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose leaning face neutral blush true", text="Но мы не будем делать обзор.")
    call process_character (sa, appearance="pose leaning face neutral blush true", text="Мы просто сделаем это для удовольствия.")
    call process_character (sa, appearance="pose handsbehind face neutral")
    $ renpy.pause(1)
    call process_character (n, appearance="pose twohandfist face neutral blush true", text="Д-да, мне нравится эта идея.")
    $ renpy.pause(1)
    call process_character (n, appearance="pose handfist face neutral blush true", text="Хочешь сделать это прямо сейчас?")
    call process_character (sa, appearance="pose handface face neutral blush true")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose handface face neutral blush true", text="Да.")

    call fade_to_black (1)
    call bust_art_background (sam_room)
    $ display_multiple_characters([ (n, "outfit underwear pose handsdown face concerned blush true"), (sa, "outfit underwear pose handsbehind face concerned blush true") ])
    call process_character (n, appearance="outfit underwear pose handsdown face concerned blush true", text="...")
    call process_character (sa, appearance="outfit underwear pose handsbehind face concerned blush true", text="...")
    $ renpy.pause(1)
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Мне...мне нравится твоя кожа.")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Она выглядит очень нежной.")
    call process_character (sa, appearance="pose handface face embarrassed blush true")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose handface face embarrassed blush true", text="Твоя тоже выглядит нежной.")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="...")
    call process_character (sa, appearance="pose handface face embarrassed blush true", text="...")
    call process_character (sa, appearance="pose handface face concerned blush true")
    $ sa.c("Можешь обнять меня, " + n.say_name + "?")
    $ renpy.pause(1)
    call process_character (n, appearance="pose handfist face concerned blush true", text="Конечно.")

    call static_still_ctc ("bg sam_2_hug")
    $ renpy.pause(1)
    call process_character (n, text="Твоя кожа реально мягкая.")
    $ renpy.pause(1)
    call process_character (sa, text="Ты такая милая и теплая.")
    call process_character (sa, text="...")
    call bust_art_background (sam_room)
    $ display_multiple_characters([ (n, "outfit underwear pose behindhead face embarrassed blush true"), (sa, "outfit underwear pose handface face embarrassed blush true") ])
    call process_character (sa, appearance="outfit underwear pose handface face embarrassed blush true", text="Мне... мне понравилось это.")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Д-да, меня тоже.")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face concerned blush true", text="...")
    $ renpy.pause(1)
    call process_character (n, appearance="pose behindhead face neutral blush true", text="Хочешь посмотреть еще один эпизод \"Дробовика Джима\"?")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose leaning face neutral blush true", text="Конечно.")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose leaning face neutral blush true", text="Это было бы замечательно.")

    python:
        if not dream:
            stats.add_stat("times_seen_panties", 1)
            stats.add_stat("times_seen_bra", 1)
            stats.add_stat("times_seen_in_underwear", 1)

    call process_end_of_scene ("sam_scene_2_seq_1", char=sa, dream=dream)

    return

label sam_scene_2_seq_2:
    $ display_multiple_characters([ (n, ""), (sa, "pose handface face concerned blush true") ])

    call process_character (sa, text="[n.say_name]...")
    $ renpy.pause(1)
    call process_character (sa, text="Я хотела узнать, хочешь ли ты этого...")
    $ renpy.pause(1)
    call process_character (sa, text="Увидимся снова в нижнем белье.")

    call prompt_menu_boldness_check ("К-конечно.", "Я-я не знаю...", "sam_scene_2_seq_2", sa)

    return

label sam_scene_2_seq_2_refusal(text, insufficient_points):
    if insufficient_points:
        call process_character (n, appearance="pose handpocket face neutral", text=text)
        call process_character (n, appearance="pose handpocket face curious", text="(Я не чувствую себя достаточно {b}уверенным{/b} для этого)")

    call process_character (sa, appearance="pose handface face concerned blush true", text="Может, как-нибудь в другой раз?")
    call prompt_refusal_end (sa)

    return

label sam_scene_2_seq_2_sex(dream=False):
    call process_scene_beginning (sam_room, char_tuple_array=[ (n, "outfit underwear pose handsdown face concerned blush true"), (sa, "outfit underwear pose handsbehind face concerned blush true") ], dream=dream, force_bg_change=True)

    call process_character (n, text="...")
    call process_character (sa, text="...")
    call process_character (n, text="...")
    $ renpy.pause(1)
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Ты хотела обняться?")
    call process_character (sa, appearance="pose handface face concerned blush true", text="Д-да.")
    call static_still_ctc ("bg sam_2_hug")
    $ renpy.pause(1)
    call process_character (n, text="Твои волосы очень приятно пахнут.")
    $ renpy.pause(1)
    call process_character (sa, text="С-спасибо.")
    call process_character (sa, text="Ты тоже хорошо пахнешь.")
    $ renpy.pause(2)
    $ sa.c(n.say_name + "?")
    call process_character (n, text="Да?")
    call process_character (sa, text="Могу я...")
    $ renpy.pause(1)

    if not dream or persistent.disable_dream_music:
        $ play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)

    call process_character (sa, text="Снять твоё нижнее белье?")
    call process_character (n, text="Е-если ты этого хочешь...")
    $ renpy.pause(1)
    call process_character (sa, text="Ладно.")

    call static_still_ctc ("bg sam_2_pulls_down_nate_underwear")
    call fade_to_black (1)
    call process_character (sa, text="{i}!!!{/i}")
    call bust_art_background (sam_room)
    $ display_multiple_characters([ (n, "outfit nudesoft pose behindhead face curious blush true"), (sa, "outfit underwear pose handface face embarrassed blush true") ])

    call process_character (sa, appearance="pose handface face embarrassed blush true", text="{i}Ч-что это такое?{/i}")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Э-это...")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Мой пенис.")
    call process_character (sa, appearance="pose handface face concerned blush true", text="Твой п-пенис?")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face concerned blush false", text="Выглядит смешно...")
    $ renpy.pause(0.5)
    call process_character (sa, appearance="pose leaning face neutral blush true", text="Но, мне нравится.")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Похож на симпатичного червяка.")
    $ renpy.pause(2)
    call process_character (sa, appearance="pose handface face concerned blush false", text="Могу я...")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose handface face concerned blush true", text="Потрогать его?")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Конечно.")

    call static_still_ctc ("bg sam_2_pets_penis")

    call process_character (sa, text="Она такой мягкий.")
    call process_character (n, text="Да, он довольно мягкий.")
    $ renpy.pause(1)
    call process_character (n, text="(Он чувствует себя хорошо, когда она прикасается к нему)")
    call process_character (sa, text="Он шевелится!")
    call process_character (n, text="Это происходит, когда я двигаю телом.")
    $ sa.c("(Пенис " + n.say_name + " забавный)")
    $ renpy.pause(1)

    call process_character (n, text="Ничего страшного, если я...")
    $ renpy.pause(1)
    call process_character (n, text="Сниму твою тоже?")
    $ renpy.pause(1)
    call process_character (sa, text="Д-да, можешь.")

    call static_still_ctc ("bg sam_2_pulls_down_sam_underwear")

    call process_character (n, text="Это твоя...")
    call process_character (sa, text="Вагина?")
    call process_character (n, text="М-могу я...")
    $ renpy.pause(1)
    call process_character (n, text="Чувствуешь?")
    call process_character (sa, text="Конечно.")

    call static_still_ctc ("bg sam_2_almost_pet_puss")

    call process_character (sa, text="Б-будь осторожен.")



    "{b}ТУК-ТУК{/b}"

    $ si.c(sa.say_name + ", " + n.say_name + ", ужин готов!")
    call bust_art_background (sam_room)
    $ display_multiple_characters([ (n, "outfit nudesoft pose behindhead face embarrassed blush true"), (sa, "outfit bra_bottomless pose handface face embarrassed blush true") ])

    call process_character (sa, appearance="pose handface face embarrassed blush true", text="Ладно!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Мы заканчиваем!")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face concerned blush true", text="...")
    $ renpy.pause(1)
    call process_character (n, appearance="pose behindhead face neutral blush true", text="Пошли есть.")
    $ renpy.pause(1)
    call process_character (n, appearance="pose behindhead face neutral blush true", text="(Мне не удалось прикоснуться)")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose leaning face concerned blush true", text="Д-да, пошли.")
    call character_leave_dissolve (n)
    $ renpy.pause(1)
    call process_character (sa, appearance="pose handsbehind face concerned blush false", text="(Он не дотронулся до меня)")
    call process_character (sa, appearance="pose handsbehind face concerned blush false", text="(Я действительно этого хотела!)")
    call process_character (sa, appearance="pose handface face flirty blush true", text="(Я хочу снова потрогать его пенис)")

    python:
        sa.revistable_scenes.add("sam_scene_2_revisit")
        skip_jump = True
        if "sam_scene_2_seq_2" in scenes_completed or "simone_scene_1_seq_1" in scenes_completed:
            skip_jump = False

        if not dream:
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_had_incestual_situation", 1)
            stats.add_stat("times_seen_panties", 1)
            stats.add_stat("times_seen_bra", 1)
            stats.add_stat("times_seen_in_underwear", 1)

    call process_end_of_scene ("sam_scene_2_seq_2", char=sa, do_not_jump=skip_jump, dream=dream )

    if skip_jump:
        call simone_scene_1_seq_1_sex

    return

label sam_scene_2_revisit:
    call process_character (n, appearance="pose behindhead face curious blush true")
    call process_character (sa, appearance="pose handsbehind face concerned blush true", text="Если ты не возражаешь, конечно.")

    call process_scene_beginning (sam_room, char_tuple_array=[ (n, "outfit nudesoft pose handsdown face neutral blush true"), (sa, "outfit underwear pose handsbehind face neutral blush true") ], force_bg_change=True)

    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="Приятно было бы увидеть это снова.")
    call process_character (sa, appearance="pose handface face curious blush false", text="Но он ещё не твёрдый.")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Пока.")
    call process_character (sa, appearance="pose handface face concerned blush false", text="Я все еще не совсем понимаю.")
    call process_character (sa, appearance="pose handface face concerned blush false", text="Как это становится твёрдым?")

    menu:
        "Он становится твёрдым, когда касаюсь его.":
            call process_character (n, appearance="pose behindhead face curious blush true")
            call add_points (sa, 1, tag="sam_scene_2_revisit_how_get_hard")
            call process_character (sa, appearance="pose leaning face neutral blush false", text="Да ну?")
            call process_character (sa, appearance="pose handface face neutral blush true", text="Ну, мне было очень весело прикасаться к нему раньше.")
            call process_character (sa, appearance="pose leaning face happy blush true", text="Предоставь это мне!")

            call static_still_ctc ("bg sam_2_pets_penis")

            python:
                stats.add_stat("times_had_penis_touched", 1)

            call process_character (sa, text="Вот так?")
            call process_character (n, text="Ах, {w=0.5}да.")
            call process_character (sa, text="Я представляю, что это домашнее животное.")
            call process_character (sa, text="Ему нравится, когда его гладят по головке.")
            call process_character (sa, text="И ему нравится, когда ее трут под животом.")
            call process_character (n, text="...")
            call process_character (sa, text="Думаешь, ему это нравится?")
            call process_character (n, text="Ему действительно очень нравится.")
            call process_character (sa, text="Но он не становится твёрдым.")
            call process_character (sa, text="Если он действительно счастлив, то становится твёрдым, не так ли?")
            call process_character (n, text="Может, если я посмотрю на тебя там еще раз, это поможет.")
            call process_character (sa, text="Т-там?")
            call process_character (sa, text="Ты имеешь ввиду мою...")
            call process_character (sa, text="Ты думаешь, это поможет, если увидишь")
        "Если я увижу твою вагину, он станет твёрдым.":
            call add_boldness (1, tag="sam_scene_2_revisit_how_get_hard")
            call process_character (n, appearance="pose handsdown face concerned blush true")

            call process_character (sa, appearance="pose handsbehind face embarrassed blush true", text="Да?")
            call process_character (n, appearance="pose behindhead face neutral blush true", text="Да.")
            call process_character (n, appearance="pose behindhead face neutral blush true", text="Когда я смотрю на тебя, это очень помогает.")
            call process_character (sa, appearance="pose handsbehind face concerned blush true", text="...")
            $ renpy.pause(0.5)
            call process_character (sa, appearance="pose handsbehind face concerned blush true", text="Я хочу убедиться, что это правда.")

    call static_still_ctc ("bg sam_2_puss")
    call process_character (sa, text="...")
    call process_character (sa, text="Ну?")
    call process_character (sa, text="Помогает?")

    if "sam_scene_4" in scenes_completed:
        call process_character (n, text="(Я чувствую, что он встаёт)")
        call process_character (n, text="Кажется, это работает.")
        call process_character (n, text="Я думаю, если я коснусь её, и мы потрёмся, как раньше...")
        call process_character (n, text="Тогда пенис станет твердым.")
        call process_character (sa, text="Ты хочешь попробовать это сделать?")

        menu:
            "Определенно.":
                $ renpy.call("sam_scene_4_revisit")
            "С другой стороны...":
                call process_character (n, text="Я буду продолжать смотреть на тебя, как ты делала раньше со мной.")
    else:

        call process_character (n, text="(Я чувствую, что он встаёт)")
        call process_character (n, text="Кажется, это работает.")

    call static_still_ctc ("bg sam_2_almost_pet_puss")
    call process_character (n, text="Как думаешь, ты тоже почувствуешь себя также если я потрогаю?")

    if "sam_scene_4" in scenes_completed:
        call process_character (sa, text="Я бы хотела, чтобы ты потер.")
        call process_character (sa, text="Я буду счастлива, если ты это сделаешь.")

        call static_still_ctc ("bg sam_3_touch_eachother")
        call process_character (sa, text="Ах!")
        call process_character (n, text="Я правильно её тру?")
        call process_character (sa, text="Ммм...")
        $ renpy.pause(1)
        call process_character (sa, text="Продолжай тереть еще, {w=0.5}пожалуйста.")
    else:

        call process_character (sa, text="Я-я не знаю...")
        call process_character (n, text="(Теперь я могу посмотреть на неё ближе)")
        call process_character (sa, text="Ты очень близко!")
        call process_character (n, text="П-Прости.")
        call process_character (sa, text="Все нормально.")
        call process_character (sa, text="Я просто нервничаю из-за твоих прикосновений.")
        call process_character (n, text="Я понимаю.")
        call process_character (n, text="Я тоже нервничал, когда ты впервые захотела потрогать мой пенис.")

    call fade_to_black (1)
    call bust_art_background (sam_room)
    $ display_multiple_characters([ (n, "outfit nudehard pose handsdown face aroused blush true"), (sa, "outfit bra_bottomless pose handsbehind face concerned blush true") ])

    call process_character (n, appearance="pose handsdown face aroused blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face concerned blush true", text="...")
    $ renpy.pause(2)
    call process_character (sa, appearance="pose handface face curious blush true", text="...")
    $ renpy.pause(1)
    call process_character (sa, appearance="pose handface face neutral blush true", text="О, {w=0.5}мой {w=0.5}Бог!")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="Хм?")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="Твой пенис!")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="Такой твёрдый!")
    call process_character (n, appearance="pose behindhead face neutral blush true", text="О, да.")
    call process_character (n, appearance="pose behindhead face neutral blush true", text="Так и есть.")
    call process_character (sa, appearance="pose leaning face neutral blush true", text="Не может быть!")
    call process_character (sa, appearance="pose leaning face neutral blush true", text="Он больше, чем раньше!")
    call process_character (sa, appearance="pose leaning face neutral blush true", text="И он смотрит вверх!")
    call process_character (sa, appearance="pose handface face neutral blush true", text="Я даже не знаю, что и думать об этом.")
    call process_character (sa, appearance="pose handface face neutral blush true", text="Но ведь это так здорово!")
    call process_character (sa, appearance="pose handface face neutral blush true", text="Я имею в виду, что это круто, {w=0.5}я не ожидала этого !")
    call process_character (n, appearance="pose handsdown face neutral blush true", text="Я рад, что тебе понравилось.")

    if "sam_scene_4" in scenes_completed:
        call process_character (sa, appearance="pose leaning face neutral blush true", text="В следующий раз я снова увижу эту белую штуку!")
        call process_character (sa, appearance="pose leaning face neutral blush true", text="Вероятно, нам придется тереть друг в друга, как в тот раз, чтобы это произошло!")
    else:
        call process_character (sa, appearance="pose leaning face neutral blush true", text="[n.say_name], мы должны сделать это снова когда-нибудь!")
        call process_character (sa, appearance="pose leaning face neutral blush true", text="Я с радостью помогу тебе снова стать твёрдым!")

    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="...")

    python:
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_seen_vagina", 1)

    call process_end_of_scene ("sam_scene_2_revisit", char=sa, force_no_boldness=True, reset_prompted_scene=False, force_not_replayable=True, revisit=True)


    return



label sam_scene_3(dream=False):
    call sam_scene_3_sex (dream=dream)

    return

label sam_scene_3_sex(dream=False):
    call process_scene_beginning (sam_room, char_tuple_array=[ (n, "outfit clothesjacket"), (sa, "outfit underwear pose handsbehind face neutral") ], dream=dream)

    call process_character (sa, appearance="pose handsbehind face neutral", text="Эй, [n.say_name]!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Я начала соло стрим!")
    call process_character (sa, appearance="pose handsbehind face happy", text="Но если ты присоединишься, мы можем удвоить удовольствие!")
    call process_character (n, appearance="pose twohandfist face happy", text="Я присоединяюсь!")

    call character_leave_dissolve (n)
    $ renpy.pause(1)

    call process_character (n, appearance="outfit underwear pose handsdown face neutral")
    call process_character (sa, appearance="pose leaning face happy", text="Оотличноо!")
    call process_character (sa, appearance="pose handface face neutral", text="Ты знаешь, что мы получаем пожертвования, [n.say_name]?")
    call process_character (n, appearance="pose twohandfist face happy", text="Это потрясающе!")
    call process_character (sa, appearance="pose leaning face neutral", text="Но пожертвования надо отрабатывать!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Ранее я приняла вызов убить босса менее чем за 3 минуты...")
    call process_character (sa, appearance="pose handsbehind face happy", text="И я разбила его вдребезги!")
    call process_character (sa, appearance="pose handsbehind face happy", text="И вскоре после этого я получила пожертвование.")
    call process_character (n, appearance="pose handfist face neutral", text="Так каков наш последний вызов?")
    call process_character (sa, appearance="pose handface face curious", text="Давай, посмоооотрим...")
    call process_character (n, appearance="pose handsdown face neutral")
    call process_character (sa, appearance="pose handface face curious", text="...")
    call process_character (sa, appearance="pose handface face neutral", text="Ого!")
    call process_character (n, appearance="pose handsdown face neutral", text="Что?")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Двадцать пять баксов ждет нас!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Не может быть!")
    call process_character (sa, appearance="pose handsbehind face happy", text="Может!")
    call process_character (n, appearance="pose handfist face neutral", text="Что мы должны сделать, чтобы получить их?")
    call process_character (sa, appearance="pose leaning face neutral", text="На самом деле, тебе даже не нужно ничего делать!")
    call process_character (sa, appearance="pose leaning face neutral", text="Это специально для меня!")
    call process_character (n, appearance="pose handsdown face neutral", text="Что это?")
    call process_character (sa, appearance="pose leaning face neutral", text="Все, что мне нужно сделать...")

    call character_leave_dissolve (sa)
    $ renpy.pause(1)

    call process_character (sa, appearance="outfit topless pose handsbehind face neutral", text="Вот это!")
    call process_character (n, appearance="pose behindhead face embarrassed", text="Ты сняла свой топик на стриме?!")
    call process_character (n, appearance="pose behindhead face embarrassed", text="(Е-её, ее сиськи!)")
    call process_character (n, appearance="pose behindhead face embarrassed", text="(Я могу видеть их!)")
    call process_character (n, appearance="pose behindhead face embarrassed", text="(Но так много других людей...)")
    call process_character (n, appearance="pose behindhead face embarrassed", text="...")
    call process_character (n, appearance="pose behindhead face embarrassed", text="У нас ведь не будет неприятностей из-за этого?")
    call process_character (sa, appearance="pose handface face neutral", text="Неее...")
    call process_character (sa, appearance="pose handface face neutral", text="Я уверен, что все будет хорошо!")
    call process_character (n, appearance="pose behindhead face concerned", text="...")
    call process_character (n, appearance="pose behindhead face curious", text="Ох...")
    call process_character (n, appearance="pose behindhead face curious", text="Хорошо.")
    call process_character (n, appearance="pose behindhead face curious", text="(Мне трудно не смотреть на ее сиськи...)")
    call process_character (sa, appearance="pose handsbehind face happy", text="И вот оно!")
    call process_character (sa, appearance="pose handsbehind face happy", text="Двадцать пять баксов на подходе!")
    call process_character (sa, appearance="pose handface face neutral", text="И посмотри на это!")
    call process_character (sa, appearance="pose handface face neutral", text="Еще двадцать пять баксов ждут нас!")
    call process_character (sa, appearance="pose handface face happy", text="Ух ты!")
    call process_character (n, appearance="pose handsdown face neutral", text="Какая на этот раз просьба?")
    call process_character (sa, appearance="pose handface face curious", text="Там написано...")
    call process_character (sa, appearance="pose handface face curious", text="\"Женский анон здесь, и я хочу увидеть, как [n.say_name] снимет всю одежду!\"")
    call process_character (sa, appearance="pose leaning face neutral", text="Ну [n.say_name]?")
    call process_character (sa, appearance="pose leaning face neutral", text="Вот простой способ заработать $25!")
    call process_character (n, appearance="pose behindhead face concerned", text="Это действительно очень просто...")
    call process_character (sa, appearance="pose handsbehind face happy", text="Тогда чего же ты ждешь?")
    call process_character (n, appearance="pose behindhead face curious blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face neutral")

    call character_leave_dissolve (n)
    $ renpy.pause(1)

    call process_character (n, appearance="outfit nudesoft pose handsdown face curious blush true", text="...")
    call process_character (sa, appearance="pose handface face happy", text="Хаха!")
    call process_character (sa, appearance="pose handface face happy", text="[n.say_name], ты должен увидеть все эти смайлики с сердечком в чате от этой женщины анонима!")
    call process_character (sa, appearance="pose handface face happy", text="Это уморительно!")
    call process_character (n, appearance="pose handsdown face neutral blush true", text="Д-да?")
    call process_character (n, appearance="pose handsdown face neutral blush true", text="(Это просто нереально)")
    call process_character (n, appearance="pose handsdown face neutral blush true", text="(Сначала [sa.say_name] показывает сиськи...)")
    call process_character (n, appearance="pose handsdown face neutral blush true", text="(И это первый раз, когда я вижу их ясно...)")
    call process_character (n, appearance="pose handsdown face neutral blush true", text="(И теперь я полностью голый!)")
    show screen hud
    call process_character (n, appearance="pose handsdown face neutral blush true", text="Что насчет пожертвования?")
    $ inventory.add_money(25, tag = "sam_3_donation")
    call process_character (sa, appearance="pose handsbehind face neutral", text="А вот и оно!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Двадцать пять баков!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Это было быстро!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Так и было!")
    hide screen hud
    call process_character (n, appearance="pose handsdown face neutral blush false")
    call process_character (sa, appearance="pose handface face neutral", text="Что пишут в чате?")
    call process_character (sa, appearance="pose handface face curious", text="Хотят, чтобы я потрясла грудью?")
    call process_character (sa, appearance="pose handface face curious", text="...")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Ну, это одна из случайных просьб!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Этот чат такой сумасшедший!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Но конечно, я могу это сделать!")
    call process_character (sa, appearance="pose leaning face neutral", text="...")
    call process_character (sa, appearance="pose handsbehind face neutral", text="...")
    call process_character (sa, appearance="pose leaning face neutral", text="Вот так?")
    call process_character (n, appearance="face concerned", text="(Что она делает?)")
    call process_character (sa, appearance="pose leaning face neutral", text="Давай снова сделаю!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="...")
    call process_character (sa, appearance="pose leaning face neutral", text="...")
    call process_character (sa, appearance="pose handsbehind face neutral", text="...")
    call process_character (sa, appearance="pose leaning face neutral", text="...")

    call process_character (n, appearance="pose twohandfist face flirty", text="...")
    call process_character (n, appearance="pose twohandfist face flirty", text="(Мне нравится то, что она делает...)")
    call process_character (n, appearance="pose twohandfist face flirty", text="(Она выставляет свою грудь мне навстречу...)")
    call process_character (n, appearance="pose twohandfist face flirty", text="...")
    call process_character (n, appearance="pose twohandfist face flirty", text="(Ой-ой...)")

    call process_character (n, appearance="outfit nudehard pose twohandfist face flirty blush true", show_bust=False)
    $ refresh_character(n, force_transition = Dissolve(1.5))

    call process_character (n, appearance="outfit nudehard pose twohandfist face flirty blush true", text="...")
    call process_character (sa, appearance="pose handface face curious", text="О чем сейчас чат пишет?")
    call process_character (sa, appearance="pose handface face curious", text="...")
    call process_character (sa, appearance="pose handface face curious", text="[n.say_name] ты...")
    call process_character (sa, appearance="pose handface face neutral", text="Хаха! Вы правы!")
    call process_character (sa, appearance="pose leaning face neutral", text="[n.say_name], твой пенис твёрдый!")
    call process_character (n, appearance="pose handsdown face embarrassed blush true", text="Вот дерьмо...")
    call process_character (sa, appearance="pose handface face neutral", text="Нет, нет, [n.say_name]!")
    call process_character (sa, appearance="pose handface face neutral", text="Чату нравится это!")
    call process_character (sa, appearance="pose handface face neutral", text="Эта женщина анон только что кинула смайлик с носовым кровотечением!")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face happy", text="Ха-ха, вы правы чат!")
    call process_character (sa, appearance="pose handsbehind face happy", text="Он дергается и двигается!")
    call process_character (sa, appearance="pose handsbehind face happy", text="Наши подписчики и количество зрителей лезут и лезут!")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="Э-это здорово...")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="([sa.say_name] не возражает против этого вообще...)")

    python:
        sa.revistable_scenes.add("sam_scene_3_revisit")

        if not dream:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_flat_breasts", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)

    call process_end_of_scene ("sam_scene_3", char=sa, dream=dream, force_no_boldness=True)

    return

label sam_scene_3_revisit:
    call process_character (n, appearance="pose twohandfist face neutral")
    call process_character (sa, appearance="pose handface face happy", text="Я услышала вас!")

    call process_scene_beginning (sam_room, char_tuple_array=[ (n, "outfit underwear pose behindhead face neutral"), (sa, "outfit underwear pose handsbehind face neutral") ], force_bg_change=True)


    call process_character (n, appearance="pose behindhead face neutral", text="Хорошо, я сделал эту позу, как и просили!")
    call process_character (sa, appearance="pose leaning face neutral", text="А вот и оно!")
    call process_character (sa, appearance="pose leaning face neutral", text="Еще одно пожертвование на стриме Твинстикс!")
    call process_character (n, appearance="pose handfist face happy", text="Вы, ребята, потрясающие!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Так здорово на самом деле...")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Мы сможем направить эти пожертвования на новое стримерское оборудование!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Все возможно с помощью наших удивительных подписчиков!")
    call process_character (sa, appearance="pose handface face curious", text="Новый запрос...")
    call process_character (sa, appearance="pose handface face curious", text="...")
    call process_character (sa, appearance="pose handface face neutral", text="Ого...")
    call process_character (sa, appearance="pose handface face neutral", text="Пятьдесят долларов ждут, если мы сделаем это!")
    call process_character (n, appearance="pose handsdown face happy", text="Святые угодники!")
    call process_character (n, appearance="pose handsdown face happy", text="Пятьдесят баксов!?")
    call process_character (sa, appearance="pose leaning face neutral", text="Это не обычная просьба или пожертвование, это точно!")
    call process_character (sa, appearance="pose leaning face neutral", text="Мы должны сделать несколько вещей!")
    call process_character (n, appearance="pose handfist face neutral", text="Давай, говори!")
    call process_character (sa, appearance="pose handface face neutral", text="Сначала...")
    call process_character (sa, appearance="pose handface face neutral", text="Ты должен показать свой пенис!")
    call process_character (n, appearance="pose behindhead face neutral", text="Конечно, никаких проблем...")

    call character_leave_dissolve (n)
    $ renpy.pause(1)

    call process_character (n, appearance="outfit nudesoft pose handsdown face neutral", text="Готово!")
    call process_character (sa, appearance="pose handface face happy", text="Хорошо, хорошо!")
    call process_character (sa, appearance="pose handface face neutral", text="Теперь мне нужно снять лифчик...")

    call character_leave_dissolve (sa)
    $ renpy.pause(1)

    call process_character (sa, appearance="outfit topless pose handsbehind face neutral", text="Сделано!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Все хорошо?")
    call process_character (n, appearance="pose twohandfist face neutral", text="И это все?")
    call process_character (sa, appearance="pose leaning face neutral", text="Не совсем, не совсем!")
    call process_character (sa, appearance="pose leaning face neutral", text="Есть одна последняя часть!")
    call process_character (n, appearance="pose handsdown face neutral", text="...")
    call process_character (sa, appearance="pose handface face curious", text="Ты тоже..")
    call process_character (sa, appearance="pose handface face curious", text="...")
    call process_character (sa, appearance="pose handface face concerned blush true", text="С-сними моё нижнее белье.")
    call process_character (n, appearance="pose handsdown face curious blush true", text="...")
    call process_character (n, appearance="pose handsdown face curious blush true", text="И это все?")
    call process_character (sa, appearance="pose handface face neutral blush true", text="П-просьба выполнена, да!")
    call process_character (n, appearance="pose handsdown face curious blush true", text="...")

    call static_still_ctc ("bg sam_2_pulls_down_sam_underwear")

    call process_character (sa, text="И она выполнена!")
    call process_character (sa, text="...")
    call process_character (sa, text="(Мы делаем это в прямом эфире, и многие зрители увидят!)")
    call process_character (sa, text="(Я надеюсь, что [n.say_name] не возражает)")
    call process_character (sa, text="(Я...)")
    call process_character (sa, text="(Мне нравится делать это перед зрителями...)")

    call fade_to_black (1)
    call bust_art_background (sam_room)
    $ display_multiple_characters([ (n, "outfit nudehard pose handsdown face curious blush true"), (sa, "outfit nude pose handsbehind face neutral blush false") ])

    call process_character (sa, appearance="pose handsbehind face neutral", text="И вы получили это!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Теперь мы оба голые!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="...")
    call process_character (sa, appearance="pose leaning face neutral", text="И смотри!")
    call process_character (sa, appearance="pose leaning face neutral", text="В качестве бонуса, у [n.say_name] пенис твёрдый!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Это бонус.")
    call process_character (sa, appearance="pose handface face neutral", text="Ох, ох!")
    call process_character (sa, appearance="pose handface face neutral", text="Вот наше пожертвование!")
    call process_character (n, appearance="pose behindhead face curious blush true")
    call process_character (sa, appearance="pose handface face neutral", text="И с ним есть послание!")
    call process_character (sa, appearance="pose leaning face neutral", text="\"Спасибо за выполнение моей просьбы...\"")
    call process_character (sa, appearance="pose leaning face neutral", text="\"И бонус, за бонусный стояк.\"")
    call process_character (sa, appearance="pose handsbehind face happy", text="Мило!")
    call process_character (sa, appearance="pose handsbehind face happy", text="[n.say_name], мы получили пять долларов дополнительно к пятидесяти!")
    call process_character (sa, appearance="pose handsbehind face curious", text="За то, что называется\"стояк.\"")
    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="pose handsdown face curious", text="Ты спрашивали в чате, что это значит?")
    call process_character (sa, appearance="pose handface face curious", text="Хм...")
    call process_character (sa, appearance="pose handface face curious", text="...")
    call process_character (sa, appearance="pose handface face neutral", text="Ооох...")
    call process_character (sa, appearance="pose handface face happy", text="Ха-ха, понятно!")
    call process_character (n, appearance="pose behindhead face neutral", text="Что?")
    call process_character (sa, appearance="pose leaning face neutral", text="Стояк, это когда твой пенис становится твердым!")
    call process_character (sa, appearance="pose handface face neutral", text="Наверное, потому что он стоит?")
    call process_character (sa, appearance="pose handface face happy", text="Кого волнует, это весело!")
    call process_character (n, appearance="pose behindhead face curious", text="(Итак, мой пенис...)")
    call process_character (n, appearance="pose behindhead face curious", text="(Стояк?)")

    python:
        store.heard_of_boner = True
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_seen_vagina", 1)

    call process_end_of_scene ("sam_scene_3_revisit", char=sa, force_no_boldness=True, reset_prompted_scene=False, force_not_replayable=True, revisit=True)


    return

label sam_scene_4:
    $ display_multiple_characters([ (n, ""), (sa, "pose handface face curious") ])

    call process_character (sa, text="Привет, [n.say_name]...")
    call process_character (sa, text="Я кое-что хочу узнать о твоем пенисе.")
    call process_character (sa, appearance="pose handface face neutral", text="Могу я спросить тебя об этом?")

    call prompt_menu_boldness_check ("О чем ты хотела спросить?", "Н-ну, не прямо сейчас.", "sam_scene_4", sa)

    return

label sam_scene_4_refusal(text, insufficient_points):
    if insufficient_points:
        call process_character (n, appearance="pose handpocket face neutral", text=text)
        call process_character (n, appearance="pose handpocket face curious", text="(Я не чувствую себя достаточно {b}уверенным{/b} для этого)")

    call process_character (sa, appearance="pose handsbehind face neutral", text="Не проблема.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Тем временем, я провела несколько интернет-исследований!")
    call prompt_refusal_end (sa)

    return

label sam_scene_4_sex(dream=False):
    $ renpy.start_predict("sam_grind_anim")
    call process_scene_beginning (sam_room, char_tuple_array=[ (n, "outfit clothesjacket pose handpocket face curious"), (sa, "outfit clothes pose handface face curious") ], dream=dream, force_bg_change=True)

    call process_character (sa, appearance="pose handface face curious", text="Мне было интересно узнать об этом...")
    call process_character (sa, appearance="pose handface face concerned", text="Каково это, когда я прикасаюсь к твоему пенису?")
    call process_character (n, appearance="pose handpocket face embarrassed", text="!!!")
    call process_character (n, appearance="pose handpocket face embarrassed", text="...")
    call process_character (n, appearance="pose behindhead face embarrassed", text="Ну...")
    call process_character (sa, appearance="pose handface face curious", text="Потому что он иногда двигается.")
    call process_character (sa, appearance="pose handface face curious", text="Особенно, когда я прикасаюсь к нему.")
    call process_character (sa, appearance="pose handface face curious", text="Это должно так происходить?")
    call process_character (n, appearance="pose behindhead face curious", text="Я думаю, да.")
    call process_character (n, appearance="pose behindhead face curious", text="Это как бы происходит без моего ведома.")
    call process_character (n, appearance="pose behindhead face curious", text="Меня немного покалывает, когда ты его трогаешь.")
    call process_character (sa, appearance="pose handface face concerned", text="Покалывает?")
    call process_character (n, appearance="pose handpocket face neutral", text="Да, но не такое сильное покалывание.")
    call process_character (n, appearance="pose behindhead face neutral", text="Это вроде щекотки по всему телу.")
    call process_character (n, appearance="pose handpocket face neutral", text="Чувствуется по-другому.")
    call process_character (n, appearance="pose handpocket face neutral", text="Это здорово.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Правда?")
    call process_character (n, appearance="pose handpocket face neutral", text="Да.")
    call process_character (sa, appearance="pose handsbehind face concerned", text="[n.say_name]?")
    call process_character (sa, appearance="pose handsbehind face concerned", text="...")
    call process_character (sa, appearance="pose handsbehind face concerned", text="Можешь {w=1.0}прикоснуться ко мне?")
    call process_character (n, appearance="pose handpocket face concerned blush true", text="...")
    call process_character (sa, appearance="pose handface face concerned blush true", text="Я хочу испытать это чувство \"покалывания\".")
    call process_character (n, appearance="pose behindhead face curious blush true", text="...")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Конечно, я могу это сделать.")
    call process_character (sa, appearance="pose leaning face happy blush true", text="Правда?")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Да!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Я в восторге от этого!")
    call process_character (sa, appearance="pose handface face neutral", text="Эй, я знаю!")

    call character_leave_dissolve (sa)
    $ renpy.pause(1)

    call process_character (sa, appearance="outfit nude pose handface face neutral", text="Мы можем касаться друг друга одновременно!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Ты так быстро разделась!")

    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face embarrassed blush true", show_bust=False)
    $ refresh_character(n, force_transition = Dissolve(1.0))
    pause 0.5

    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="(У меня даже не было времени среагировать!)")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Ну, мы не можем делать это в одежде!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Так что давай приступим к делу!")

    call character_leave_dissolve (n)
    $ renpy.pause(1)

    call process_character (n, appearance="outfit nudehard pose behindhead face curious blush true", text="В-вот.")
    call process_character (sa, appearance="pose leaning face neutral", text="Ты уже твёрдый там?")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="Он встаёт даже, когда я просто думаю об этом...")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="Как я буду прикасаться к тебе.")
    call process_character (sa, appearance="pose handface face concerned blush true", text="...")
    call process_character (sa, appearance="pose handface face concerned blush true", text="Значит, у тебя твердеет, когда ты думаешь обо мне?")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face concerned blush true", text="Я готова, если ты готов...")



    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Resort Loop2.ogg", fadeout=1.0, fadein = 1.0)

    call fade_to_black_fade_to_static_ctc ("bg sam_3_touch_eachother", 1.0)

    call process_character (sa, text="Б-будь осторожен...")
    call process_character (n, text="Буду.")
    call process_character (n, text="...")
    call process_character (n, text="(Я действительно чувствую ее...)")
    call process_character (sa, text="Мм!")
    call process_character (n, text="Ты в порядке?")
    call process_character (sa, text="Все так, как ты и сказал!")
    call process_character (n, text="Ты чувствуешь покалывание?")
    call process_character (sa, text="Ахх!")
    call process_character (sa, text="Д-да.")
    call process_character (sa, text="...")
    call process_character (sa, text="(Пенис у [n.say_name] тёплый)")
    call process_character (sa, text="(И он становится жестким...)")
    call process_character (n, text="Ах...")
    call process_character (n, text="(Мне нравится, как она прикасается ко мне)")
    call process_character (n, text="(Я чувствую тепло от нее)")
    call process_character (sa, text="...")
    call process_character (sa, text="(Я так близко к нему)")
    call process_character (sa, text="(Его тело почти касается моего)")
    call process_character (sa, text="...")
    call process_character (n, text="([sa.say_name] очень тихая)")
    call process_character (n, text="...")
    call process_character (n, text="(Надеюсь, ей это нравится...)")
    call process_character (sa, text="(Я чувствую, что мы должны...)")
    call process_character (sa, text="[n.say_name]?")
    call process_character (n, text="Хм?")
    pause 1.0
    call process_character (sa, text="Мы можем поцеловаться в губы?")
    call process_character (n, text="Я никогда так раньше не целовалась.")
    call process_character (sa, text="Я тоже...")
    call process_character (n, text="(Я-я думаю, я буду стараться изо всех сил)")
    call process_character (n, text="(Я попытаюсь подражать тому, как это делают другие люди...)")

    call static_still_ctc ("bg sam_3_kiss")

    call process_character (sa, text="(Мы сейчас целуемся!)")
    call process_character (sa, text="(Мне так понравилось!)")
    call process_character (n, text="(Ее губы мягкие и немного влажные)")
    call process_character (n, text="(И она так сильно краснеет!)")
    call process_character (n, text="...")
    call process_character (n, text="(Я хочу почувствовать ее тело)")

    call static_still_ctc ("bg sam_3_going_to_bed")
    call process_character (sa, text="Т-ты толкаешь меня.")
    call process_character (n, text="Я хотел полапать тебя.")
    call process_character (n, text="Ты такая мягкая и теплая...")
    call process_character (sa, text="Кровать находится позади нас...")
    call process_character (sa, text="Если мы сделаем еще несколько шагов, то...")
    call process_character (n, text="Мм...")
    call process_character (n, text="Мне нравится, что наша кожа касается во много местах)")
    call process_character (sa, text="[n.say_name], я собираюсь упасть на...")

    window hide
    call fade_to_black (1.0)

    call process_character (sa, text="Ого!")
    call process_character (n, text="Уф!")

    call static_still_ctc ("bg sam_3_grind")

    call process_character (n, text="П-прости...")
    call process_character (n, text="Я не обратил внимания.")
    call process_character (sa, text="Это, нормально.")
    call process_character (sa, text="Ах...")
    $ sa.c( n.say_name[0] + "-" + n.say_name + ", смотри, где твой член..." )
    call process_character (n, text="Он... напротив твоей...")
    call process_character (n, text="(Это отличается от того, когда [sa.say_name] коснулась моего пениса руками)")
    call process_character (n, text="Ах...")
    call process_character (n, text="(Он чувствует себя более чувствительным)")

    $ sam_grind_had_slow_speed_message = False
    $ sam_grind_had_normal_speed_message = False
    $ sam_grind_had_fast_speed_message = False

    window hide
    $ play_sex_sounds = True
    $ set_main_animation_speed(1.0)
    show anim_nothing_image as main_animation at main_animation_transform(IA_Animation_Sam_Grind_Info(), xalign = 0.5, yalign = 0.5)
    with Dissolve(1.35)
    show bg white
    $ renpy.pause(1.75)

    call process_character (sa, text="Ч-что ты делаешь?")
    call process_character (n, text="Я только начал двигаться.")
    call process_character (n, text="Я не могу остановиться по какой-то причине...")
    call process_character (sa, text="Вообще-то, это действительно здорово!")
    call process_character (sa, text="Я хочу, чтобы ты продолжал!")
    call process_character (n, text="П-правда?")
    call process_character (n, text="Все в порядке!")
    call process_character (n, text="Ах!")
    call process_character (n, text="(Меня как-то покалывает!)")
    call process_character (n, text="(Очень сильно в области пениса!)")
    call process_character (sa, text="(Я никогда не чувствовала ничего подобного)")
    call process_character (sa, text="(Оно должно быть из-за того, что [n.say_name] трёт свой пенис об меня)")
    call process_character (sa, text="Ахх!")

    window hide
    $ quick_menu = False
    show screen sam_grind_speed_settings(is_revisit = False)
    $ renpy.pause(3.0)
    $ renpy.suspend_rollback(True)

    jump sam_scene_4_segment_2

label sam_scene_4_segment_2:
    show screen sam_grind_speed_settings(is_revisit = False)
    call screen progress_button_screen("Кончить!")

    hide screen sam_grind_speed_settings
    $ set_main_animation_speed(sam_grind_fast_speed_multiplier)

    call process_character (n, text="Ах, ах.")
    call process_character (n, text="(Это чувство в...)")
    call process_character (n, text="(Такое же, когда я делал это в ванной комнате, я...)")
    call process_character (n, text="Ах, [sa.say_name]...")
    call process_character (n, text="[sa.say_name], я думаю, что-то случилось...")
    call process_character (sa, text="Ах, ах...")
    call process_character (sa, text="Что ты имеешь в виду?")

    window hide
    $ set_main_animation_speed(sam_grind_fastest_speed_multiplier)
    $ renpy.pause(1.5)
    window hide
    hide main_animation
    with Dissolve(1.5)
    $ play_sex_sounds = False

    window hide
    show bg sam_3_cum
    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
    with Dissolve(2)

    $ play_sex_sounds = True
    $ renpy.pause()

    "[sa.say_name] & [n.say_name]" "Аххх!!"
    call process_character (sa, text="...{p}...")
    call process_character (sa, text="Это было потрясающе, [n.say_name]!")
    call process_character (n, text="Да, это так.")
    call process_character (sa, text="...")
    call process_character (sa, text="Что это за белое вещество?")
    call process_character (n, text="Оно выходит из моего пениса, когда меня сильно покалывает.")
    call process_character (sa, text="Ты знаешь, что это?")
    call process_character (n, text="Она, вроде, не плохая.")
    call process_character (n, text="Это какая-то белая, липкая слизь.")

    call static_still_ctc ("bg sam_3_plays_with_cum")

    call process_character (sa, text="Похоже, она попала на кровать.")
    call process_character (sa, text="И на мои ноги.")
    call process_character (n, text="Д-да.")
    call process_character (n, text="Она всё марает.")
    call process_character (sa, text="...")
    call process_character (sa, text="Мне нужно узнать больше об этих вещах.")
    call process_character (sa, text="Я спрошу об этом в интернете.")
    call process_character (n, text="Думаешь, это поможет?")
    call process_character (sa, text="Интернет никогда не подводил меня, чтобы помочь узнать что-то новое!")
    call process_character (sa, text="И эту тайну стоит разгадать!")
    call process_character (sa, text="(Хм, пахнет забавно)")
    call process_character (n, text="Я думаю, мы должны это убрать.")
    call process_character (sa, text="Просто дай мне еще несколько минут с этой хренью.")
    call process_character (sa, text="(Это настолько здорово!)")
    call process_character (sa, text="(Я не могу поверить, что это вещество вышло из пениса моего брата!)")
    call process_character (sa, text="(Ха-ха, я могу сделать так много классных форм)")
    call process_character (sa, text="...")
    call process_character (sa, text="(Интересно, хотели бы зрители увидеть это...)")

    python:
        sa.revistable_scenes.add("sam_scene_4_revisit")

        if not dream:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_flat_breasts", 1)
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_had_incestual_situation", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_kissed_on_lips", 1)

    $ renpy.stop_predict("sam_grind_anim")
    call process_end_of_scene ("sam_scene_4", char=sa, dream=dream )

    return

image sam_grind_anim:
    "sam_grind_anim_0"
    pause 0.08
    "sam_grind_anim_1"
    pause 0.08
    "sam_grind_anim_2"
    pause 0.08
    "sam_grind_anim_3"
    pause 0.08
    "sam_grind_anim_4"
    pause 0.08
    "sam_grind_anim_5"
    pause 0.08
    "sam_grind_anim_6"
    pause 0.08
    "sam_grind_anim_7"
    pause 0.08
    "sam_grind_anim_8"
    pause 0.08
    "sam_grind_anim_9"
    pause 0.08
    "sam_grind_anim_10"
    pause 0.08
    repeat

label sam_grind_go_slow(is_revisit):
    call sam_grind_set_speed (sam_grind_slow_speed_multiplier)

    if not sam_grind_had_slow_speed_message:
        if is_revisit:
            call process_character (sa, text="Я чувствую, как твоя кожа двигается туда-сюда...")

    window hide
    with None
    $ sam_grind_had_slow_speed_message = True

    if is_revisit:
        $ renpy.call("sam_scene_4_revisit_segment_2")
    else:
        $ renpy.call("sam_scene_4_segment_2")

    return

label sam_grind_go_normal(is_revisit):
    call sam_grind_set_speed (1.0)

    if not sam_grind_had_normal_speed_message:
        if is_revisit:
            call process_character (sa, text="Ты знаешь, как долго ты сможешь это делать?")
            call process_character (n, text="Я не {w=0.5}ах, знаю.")

    window hide
    with None
    $ sam_grind_had_normal_speed_message = True

    if is_revisit:
        $ renpy.call("sam_scene_4_revisit_segment_2")
    else:
        $ renpy.call("sam_scene_4_segment_2")

    return

label sam_grind_go_fast(is_revisit):
    call sam_grind_set_speed (sam_grind_fast_speed_multiplier)

    if not sam_grind_had_fast_speed_message:
        if is_revisit:
            call process_character (sa, text="Ах, ахх, ах!")
            call process_character (sa, text="Это не кажется слишком быстрым?")
            call process_character (n, text="Ах...")
            call process_character (n, text="Я думаю, все в порядке.")

    window hide
    with None
    $ sam_grind_had_fast_speed_message = True

    if is_revisit:
        $ renpy.call("sam_scene_4_revisit_segment_2")
    else:
        $ renpy.call("sam_scene_4_segment_2")

    return

label sam_grind_set_speed(speed):
    hide screen sam_grind_speed_settings
    $ set_main_animation_speed(speed)

    return

screen sam_grind_speed_settings(is_revisit=True):
    vbox:
        xalign 0.97
        yalign 0.3
        spacing 20

        use main_menu_button(text="Медленно", action=Function(sam_grind_set_speed, "sam_grind_go_slow", is_revisit), enabled=main_animation_speed != sam_grind_slow_speed_multiplier)
        use main_menu_button(text="Нормально", action=Function(sam_grind_set_speed, "sam_grind_go_normal", is_revisit), enabled=main_animation_speed != 1.0)
        use main_menu_button(text="Быстро", action=Function(sam_grind_set_speed, "sam_grind_go_fast", is_revisit), enabled=main_animation_speed != sam_grind_fast_speed_multiplier)

screen sam_dream_speed_settings:
    hbox:
        xalign 0.3
        yalign 0.1
        spacing 20

        vbox:
            spacing 20

            use main_menu_button(text="Минет", action=Jump("sam_dream_go_blowjob"), enabled=sam_scene_dream_position != "blowjob")
            use main_menu_button(text="Вагин. секс", action=Jump("sam_dream_go_vaginal"), enabled=sam_scene_dream_position != "vaginal")
            use main_menu_button(text="Анал. секс", action=Jump("sam_dream_go_anal"), enabled=sam_scene_dream_position != "anal")

        vbox:
            spacing 20

            use main_menu_button(text="Медленно", action=Jump("sam_dream_go_slow"), enabled=main_animation_speed != sam_dream_slow_speed_multiplier)
            use main_menu_button(text="Нормально", action=Jump("sam_dream_go_normal"), enabled=main_animation_speed != 1.0)
            use main_menu_button(text="Быстро", action=Jump("sam_dream_go_fast"), enabled=main_animation_speed != sam_dream_fast_speed_multiplier)


label sam_scene_4_revisit:
    $ renpy.start_predict("sam_grind_anim")

    call process_character (n, appearance="pose behindhead face curious blush true")
    call process_character (sa, appearance="pose handsbehind face concerned blush true", text="Если ты не возражаешь, да.")

    python hide:
        play_music("audio/music/Resort Loop2.ogg", fadeout=1.0, fadein = 1.0)

    call fade_to_black_fade_to_static_ctc ("bg sam_3_touch_eachother", 1.0)

    call process_character (sa, text="Мне нравится, как ты прикасаешься.")
    call process_character (n, text="Да?")
    call process_character (sa, text="Мм!")
    call process_character (n, text="Чувствую немного влажным.")
    call process_character (sa, text="Д-да?")
    call process_character (sa, text="Раньше там не было мокро.")
    call process_character (n, text="Она промокла после того, как я начал её трогать.")
    call process_character (sa, text="Э-это интересно...")
    call process_character (sa, text="Мне придется больше читать об этом в интернете.")
    call process_character (sa, text="...")
    call process_character (sa, text="Тебе нравится моя рука на твоем пенисе?")
    call process_character (n, text="([sa.say_name] дергает мой пенис по-другому)")
    call process_character (n, text="(Она крепче сжимает его)")
    call process_character (n, text="Мне...мне нравится.")
    call process_character (sa, text="...")
    call process_character (sa, text="Тебе нравилось, когда мы целовались раньше?")

    window hide
    menu:
        "Э-это было забавно...":
            call process_character (sa, text="Почему бы нам не поцеловаться снова?")
            call static_still_ctc ("bg sam_3_kiss")
        "Я хочу поцеловать тебя снова!":
            call add_boldness (1, tag="sam_scene_4_revisit_kiss_you")
            call static_still_ctc ("bg sam_3_kiss")
            call process_character (sa, text="!")
            call process_character (sa, text="(Он сразу начал целовать меня!)")

    call process_character (n, text="(Я слышу звуки наших поцелуев)")
    call process_character (sa, text="(Я думаю, что чувствую язык [n.say_name]!)")
    call process_character (sa, text="(Он скользкий)")

    call static_still_ctc ("bg sam_3_going_to_bed")

    call process_character (n, text="Мммф…")
    call process_character (n, text="В прошлый раз мы были на кровати.")
    call process_character (sa, text="Мммф…")
    call process_character (sa, text="Да...")
    call process_character (sa, text="Я лежала на спине.,")
    call process_character (sa, text="А потом ты подобрался ближе...")


    call static_still_ctc ("bg sam_3_kiss_on_bed")
    call static_still_ctc ("bg sam_3_grind")

    call process_character (n, text="Вот как мы это сделали.")
    call process_character (sa, text="Это немного щекотно...")
    call process_character (sa, text="Когда твой пенис щиплет задевает мою...")
    call process_character (n, text="([sa.say_name] прав)")
    call process_character (n, text="(Это щекочет и заставляет меня дрожать)")
    call process_character (n, text="(Но эта дрожь не от холода)")
    call process_character (n, text="...")
    call process_character (n, text="(Это расслабляет...)")

    $ sam_grind_had_slow_speed_message = False
    $ sam_grind_had_normal_speed_message = False
    $ sam_grind_had_fast_speed_message = False

    window hide
    $ play_sex_sounds = True
    $ set_main_animation_speed(1.0)
    show anim_nothing_image as main_animation at main_animation_transform(IA_Animation_Sam_Grind_Info(), xalign = 0.5, yalign = 0.5)
    with Dissolve(1.35)
    show bg white
    $ renpy.pause(1.75)

    call process_character (sa, text="Ах...")
    call process_character (sa, text="Ты легко скользишь по мне.")
    call process_character (n, text="Я думаю, что ты становишься мокрой там.")
    call process_character (n, text="Мне не нужно много двигаться, чтобы скользить туда-сюда.")
    call process_character (sa, text="Так это помогает?")
    call process_character (n, text="Д-да, именно так.")
    call process_character (sa, text="...")
    call process_character (sa, text="(Когда я чувствую себя так...)")
    call process_character (sa, text="(Я не хочу говорить)")
    call process_character (sa, text="(Интересно, [n.say_name] чувствует то же самое?)")
    call process_character (sa, text="(М-мой ум только думает о том, насколько хорошо от трения...)")

    window hide
    $ quick_menu = False
    show screen sam_grind_speed_settings
    $ renpy.pause(3.0)
    $ renpy.suspend_rollback(True)

    jump sam_scene_4_revisit_segment_2

    return

label sam_scene_4_revisit_segment_2:
    show screen sam_grind_speed_settings

    if "sam_scene_blowjob_revisit" in scenes_completed and 1 == 2:
        call screen progress_button_screen("Дальше")

        call process_character (sa, text="Е...Если ты хочешь...")
        call process_character (sa, text="Я бы не прочь снова у тебя пососать.")
        call process_character (sa, text="Может, это будет по-другому на вкус.")
        hide screen sam_grind_speed_settings

        menu:
            "Мы можем это сделать.":
                $ renpy.stop_predict("sam_grind_anim")
                jump sam_scene_blowjob_revisit
            "Мне нравится делать это с тобой.":
                call process_character (sa, text="Мне тоже это нравится...")
    else:
        call screen progress_button_screen("Кончить!")

    $ renpy.suspend_rollback(False)
    hide screen sam_grind_speed_settings
    with None

    call process_character (n, text="(Я думаю, что я смогу продержаться дольше)")
    call process_character (n, text="(Но я приближаюсь к тому, когда выходит белое вещество)")
    call process_character (n, text="(Как [sa.say_name] назвала её?)")
    call process_character (n, text="(\"Кончина?\")")
    call process_character (n, text="Ах, ах...")
    call process_character (sa, text="(Он снова делает это лицо...)")
    call process_character (sa, text="(Я думаю, что это то же самое лицо перед тем...)")
    $ sa.c( n.say_name[0] + "-" + n.say_name + "?" )
    call process_character (sa, text="Ты готовишься...")
    call process_character (sa, text="Стрелять спермой?")
    call process_character (n, text="Ах, ах, ах...")
    call process_character (n, text="Я-я готов...")
    call process_character (n, text="Я собираюсь...")

    $ set_main_animation_speed(sam_grind_fast_speed_multiplier)

    call process_character (sa, text="Хах, ах, ах!")
    call process_character (sa, text="(Такое же чувство...)")
    call process_character (sa, text="(Это должно быть то же самое, что [n.say_name] чувствовал раньше...)")
    call process_character (sa, text="Ах, ах!")
    call process_character (sa, text="(Перед его...)")

    window hide
    $ set_main_animation_speed(sam_grind_fastest_speed_multiplier)
    $ renpy.pause(1.5)
    window hide
    hide main_animation
    with Dissolve(1.5)
    $ play_sex_sounds = False

    window hide
    show bg sam_3_cum
    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
    with Dissolve(2)

    $ play_sex_sounds = True
    $ renpy.pause()

    "[sa.say_name] & [n.say_name]" "Аххх!!"
    call process_character (sa, text="...")
    call process_character (n, text="...")
    call process_character (sa, text="Я чувствовала покалывание по всему телу.")
    call process_character (n, text="Я тоже это почувствовал...")
    call process_character (n, text="И оно исходило из пениса.")

    call static_still_ctc ("bg sam_3_plays_with_cum")

    call process_character (sa, text="На мне больше, чем раньше.")
    call process_character (n, text="Может, чем больше мы этим занимаемся...")
    call process_character (n, text="Тем больше этого выходит наружу?")
    call process_character (sa, text="Хм, возможно.")
    call process_character (n, text="Я думаю, что мы должны провести стрим, как только мы помоемся.")
    call process_character (sa, text="Хороший план!")
    call process_character (sa, text="...")
    call process_character (sa, text="(Это напомнило мне...)")
    call process_character (sa, text="(Я должна сфотографировать, как [n.say_name] кончил на меня)")
    call process_character (sa, text="(Может быть, чат подумает, что это круто...)")


    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_had_incestual_situation", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_ejaculated", 1)

    $ renpy.stop_predict("sam_grind_anim")

    call process_end_of_scene ("sam_scene_4_revisit", char=sa, force_no_boldness=True, reset_prompted_scene=False, force_not_replayable=True, revisit=True)


    return

label sam_scene_swimsuit(after_buy_label=False, dream=False):
    call sam_scene_swimsuit_sex (dream=dream)

    return

label sam_scene_swimsuit_sex(dream=False):
    call process_scene_beginning (bg="bg nate_room_daytime", dream=dream)
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="(Хорошо, купальник куплен)")
    call process_character (n, appearance="pose twohandfist face neutral", text="(Я надеюсь [sa.say_name] понравится!)")

    call process_scene_beginning (bg="bg sam_room_daytime", char_tuple_array=[ (n, "outfit clothesjacket pose handpocket face neutral"), (sa, "outfit clothes pose handsbehind face neutral") ], dream=dream, force_bg_change=True)

    call process_character (n, appearance="pose handpocket face neutral", text="Привет.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Привет, [n.say_name], что случилось?")
    call process_character (n, appearance="pose behindhead face neutral", text="У меня… есть кое-что для тебя.")
    call process_character (sa, appearance="pose handface face neutral", text="Правда?")
    call process_character (sa, appearance="pose handface face neutral", text="Что ты для меня приготовил?")
    call process_character (n, appearance="pose behindhead face neutral", text="Вот.")
    call process_character (n, appearance="pose behindhead face neutral", text="Новый купальник.")
    call process_character (sa, appearance="pose leaning face neutral", text="Оу, спасибо, [n.say_name]!")
    call add_points (sa, 2, tag="sam_scene_swimsuit_nice_color")
    call process_character (sa, appearance="pose leaning face neutral", text="Оох, какой приятный цвет!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Так тебе нравится?")
    call process_character (sa, appearance="pose handface face happy", text="Да, да!")
    call process_character (sa, appearance="pose handface face neutral", text="И идеальное время тоже!")
    call process_character (sa, appearance="pose handface face neutral", text="Я искала свой старый купальник, и не смогла его найти!")
    call process_character (sa, appearance="pose leaning face happy", text="Так что теперь я могу наслаждаться бассейном, наконец!")
    call process_character (n, appearance="pose handfist face neutral", text="Я надеюсь, что это правильный размер.")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Что ж, давай узнаем прямо сейчас!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Надевай свои плавки и жди меня у бассейна!")

    call process_scene_beginning (bg="bg backyard_daytime", char_tuple_array=[ (n, "outfit swimsuit pose handsdown face neutral")])

    call process_character (n, appearance="pose handsdown face neutral", text="(Сегодняшний день идеально подходит для бассейна)")
    call process_character (n, appearance="pose handsdown face neutral", text="...")
    call process_character (n, appearance="pose handsdown face neutral", text="([sa.say_name] уже пришла)")
    call process_character (sa, appearance="outfit bikini pose handsbehind face neutral", text="И вуаля!")
    call process_character (sa, appearance="pose handsbehind face neutral", text="Идеально подходит!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Мило!")
    call process_character (sa, appearance="pose handface face neutral", text="Мне нравится!")
    call process_character (sa, appearance="pose handface face neutral", text="И такой изящный пушистик к нему.")
    call process_character (n, appearance="pose behindhead face neutral", text="Я прочитал в интернете, что это \"бахрома\".")
    call process_character (sa, appearance="pose leaning face happy", text="Ну, как бы это ни называлось, это изящно!")
    call process_character (n, appearance="pose handsdown face neutral")
    call process_character (sa, appearance="pose handface face neutral", text="Хорошо, время для веселья в бассейне!")
    call process_character (sa, appearance="pose handface face curious", text="Хм, что бы сделать в первую очередь.")
    call process_character (n, appearance="pose behindhead face neutral", text="Разве ты не говорила, что хочешь переплыть из одного конца бассейна в другой, без единого вдоха?")
    call process_character (sa, appearance="pose handface face neutral", text="О, да, я вспомнила!")
    call process_character (sa, appearance="pose handface face happy", text="Спасибо, что напомнил!")
    call process_character (n, appearance="pose handsdown face neutral")
    call process_character (sa, appearance="pose handsbehind face curious", text="Мне еще предстоит дойти до этого.")
    call process_character (sa, appearance="pose handsbehind face curious", text="Я просто знаю секретный метод...")
    call process_character (sa, appearance="pose leaning face angry", text="Ладно, в бассейн!")
    call process_character (sa, appearance="pose leaning face angry", text="Ты можешь победить меня только в своей H2O!")
    call process_character (n, appearance="pose behindhead face curious", text="(У нее напряженный взгляд на лице...)")


    python:
        sa.revistable_scenes.add("sam_scene_swimsuit_revisit")

        if not dream:
            stats.add_stat("times_seen_bikini", 1)

    call process_end_of_scene ("sam_scene_swimsuit", char=sa, dream=dream, reset_prompted_scene=False )

    return

label sam_scene_vaginal:
    $ display_multiple_characters([ (n, ""), (sa, "") ])

    call process_character (sa, appearance="", text="[n.say_name]!")
    call process_character (sa, appearance="", text="Чувак, мне дали доступ к раннему доступу к игре Дьявол Может Смеяться 2!")
    call process_character (sa, appearance="", text="Если мы будем транслировать игру, мы будем одним из немногих людей, играющих в нее!")
    call process_character (sa, appearance="", text="Мы получим множество зрителей наверняка!")
    call process_character (sa, appearance="", text="Давай начнём прямо сейчас!")

    call prompt_menu_boldness_check ("Этот стрим будет эпическим!", "Я устал сегодня немного.", "sam_scene_vaginal", sa)

    return

label sam_scene_vaginal_refusal(text, insufficient_points):
    if insufficient_points:
        call process_character (n, appearance="pose behindhead face neutral", text=text)
        call process_character (n, appearance="pose behindhead face concerned", text="(Я-я не знаю, готов ли я к стриму голым перед большим количеством людей...)")
        call process_character (n, appearance="pose behindhead face curious", text="(Что делать, если [sa.say_name] хочет попробовать что-то новое со мной?)")
    else:
        call process_character (n, appearance="pose behindhead face neutral")

    call process_character (sa, appearance="pose leaning face neutral", text="Ну, ты там оторвись по полной!")
    call process_character (sa, appearance="pose leaning face neutral", text="Такая возможность не так часто случается!")
    call prompt_refusal_end (sa)
    return

label sam_scene_vaginal_sex(dream=False):
    call process_scene_beginning (bg="bg sam_room_evening", char_tuple_array=[ (n, "outfit nudesoft pose handsdown"), (sa, "outfit nude pose leaning face happy") ], dream=dream )

    call process_character (sa, appearance="pose leaning face happy blush false", text="Спасибо всем за то, что пришли на наш стрим!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Мы покажем ранний доступ к Дьявол Может Смеяться 2 в следующий раз!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Мне нравится!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Управление намного лучше, чем в первой!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="И частота кадров супер гладкая, без задержек!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Делает боевой геймплей более увлекательным!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="В любом случае, скоро мы увидимся снова!")

    call process_character (sa, appearance="pose leaning face happy blush false")
    call process_character (n, appearance="pose handfist face happy blush false")
    "[sa.say_name] & [n.say_name]" "\"Твинстикс отключены!\""
    call process_character (n, appearance="pose handsdown face neutral blush false")

    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Святые угодники, что за стрим!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Это было безумие!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="У нас была тысяча человек онлайн!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Это более чем вдвое больше, чем обычно приходят!")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Люди любят видеть игры с ранним доступом.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Это потому, что они могут узнать, хорошо это или нет!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Я хотела бы знать, прежде чем делать предзаказ!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Они также любят видеть нас и как мы ведём стрим.")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Определенно.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Похоже, все ждут нас без одежды все время.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Я слышала, что некоторые люди пытаются подражать нашим голым стримам.")
    call process_character (sa, appearance="pose handface face happy blush false", text="Но они не могут соответствовать оригиналу!")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Я чувствую, что мы должны отдохнуть после долгого стрима.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Хочешь посмотреть фильм или послушать музыку?")
    call process_character (sa, appearance="pose handface face curious blush false", text="...")
    call process_character (sa, appearance="pose handface face curious blush false", text="Вообще-то, я тут подумала...")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Хм?")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Ну...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Я хотела сделать что-то другое, чтобы отпраздновать этот эпический стрим!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Да ну?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Что ты хотела попробовать?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Это было то, что я видела в интернете.")
    call process_character (sa, appearance="pose handsbehind face concerned blush false", text="Это...")
    call process_character (sa, appearance="pose handsbehind face concerned blush false", text="...")
    call process_character (sa, appearance="pose handface face concerned blush true", text="Там показывали пенис, входящий во влагалище.")
    call process_character (n, appearance="pose behindhead face curious blush true", text="О-ох...")
    call process_character (n, appearance="pose behindhead face curious blush true", text="...")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Да?")
    call process_character (sa, appearance="pose handsbehind face concerned blush true", text="Фактически...")
    call process_character (sa, appearance="pose handsbehind face concerned blush true", text="В названии видео сказано \"засунул член в тугую киску\" или что-то в этом роде...")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="...")
    call process_character (sa, appearance="pose handface face concerned blush true", text="...")
    call process_character (sa, appearance="pose handface face concerned blush true", text="Я...")
    call process_character (sa, appearance="pose handface face concerned blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="Я хочу, чтобы мы это сделали!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="{i}Глык!{/i}")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Ты уверена?")
    call process_character (sa, appearance="pose handface face neutral blush true", text="Я знаю, мы никогда не делали этого раньше...")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="Но это выглядело супер просто!")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="...")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="Ладно.")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Но ты можешь мне сказать, что делать?")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="Конечно!")
    call process_character (sa, appearance="pose leaning face neutral blush true", text="Поверь мне, это пустяк!")
    call process_character (n, appearance="pose handsdown face curious blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="Вот, смотри.")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="Я просто повторю то, что видела.")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="Сначала нужно лечь на спину...")

    if not dream or persistent.disable_dream_music:
        $ play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg sam_vaginal_spread")

    call process_character (n, appearance="", text="...")
    call process_character (sa, appearance="", text="А-ах...")
    call process_character (sa, appearance="", text="Девушка в видео раздвигала свою киску пальцами вот так.")
    call process_character (sa, appearance="", text="Мне нравится это чувство.")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Итак, {w=0.5}что мне делать?")
    call process_character (sa, appearance="", text="Ты должен лечь на меня сверху.")
    call process_character (n, appearance="", text="Л-лечь на тебя сверху?")
    call process_character (sa, appearance="", text="Когда ты будешь лежать на мне...")
    call process_character (sa, appearance="", text="Ты засунешь свой член мне в киску.")

    call static_still_ctc ("bg sam_vaginal_dick_out")

    call process_character (n, appearance="", text="Вот так?")
    call process_character (sa, appearance="", text="Я чувствую, как он начинает входить...")
    call process_character (n, appearance="", text="Д-да, ах...")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Тебе нужно протолкнуть его до конца.")
    call process_character (sa, appearance="", text="Надави на меня своим телом...")

    call static_still_ctc ("bg sam_vaginal_dick_in_eyes_closed")

    call process_character (sa, appearance="", text="Аааах!")
    call process_character (sa, appearance="", text="([n.say_name] во мне!)")
    call process_character (n, appearance="", text="(Она теплая!)")
    call process_character (sa, appearance="", text="Ммм, а-ах.")
    call process_character (sa, appearance="", text="...")

    call static_still_ctc ("bg sam_vaginal_dick_in")

    call process_character (sa, appearance="", text="Ты можешь немного  подвигаться?")
    call process_character (n, appearance="", text="П-подвигаться?")
    call process_character (sa, appearance="", text="Мы не должны стоять на месте, как сейчас.")
    call process_character (sa, appearance="", text="Ты должен подниматься и опускаться.")

    call static_still_ctc ("bg sam_vaginal_dick_out")

    call process_character (n, text="...")

    call static_still_ctc ("bg sam_vaginal_dick_in_eyes_closed")

    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="Ахх!")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="...")

    call static_still_ctc ("bg sam_vaginal_dick_in")

    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="С-сделай это снова.")

    call static_still_ctc ("bg sam_vaginal_dick_out")

    call process_character (n, appearance="pose handsbehind face neutral blush true", text="...")

    call static_still_ctc ("bg sam_vaginal_dick_in")

    call process_character (n, appearance="pose handsbehind face neutral blush true", text="О, это действительно приятно.")
    call process_character (n, appearance="pose handsbehind face neutral blush true", text="(М-мой член скользкий после входа в [sa.say_name]...)")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="(К-каждый раз, когда он это делает...)")

    call static_still_ctc ("bg sam_vaginal_dick_out")

    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="...{p}...")

    call static_still_ctc ("bg sam_vaginal_dick_in")

    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="Ах...")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="(Я чувствую прилив возбуждения)")

    call static_still_ctc ("bg sam_vaginal_dick_out")

    call process_character (n, appearance="pose handsbehind face neutral blush true", text="(Кожа на моем пенисе двигается, когда я...)")
    call process_character (n, appearance="pose handsbehind face neutral blush true", text="...")

    call static_still_ctc ("bg sam_vaginal_dick_in")

    call process_character (n, appearance="pose handsbehind face neutral blush true", text="(Толчок внутрь)")
    call process_character (n, appearance="pose handsbehind face neutral blush true", text="{i}Вздох, Вздох{/i}")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="...")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="([n.say_name] дышит тяжело, как собака)")
    call process_character (sa, appearance="pose handsbehind face neutral blush true", text="(О-он толкает сильнее каждый раз...)")

    call static_still_ctc ("bg sam_vaginal_xray")

    call process_character (n, appearance="pose handsbehind face neutral blush true", text="{i}Вздох{/i}")
    $ n.c(sa.say_name[0] + "-" + sa.say_name + "...")
    call process_character (n, appearance="pose handsbehind face neutral blush true", text="Внутри тебя становится теснее.")
    call process_character (sa, appearance="", text="Ммм, я тоже это чувствую!")
    call process_character (n, appearance="", text="Я-я должен продолжать?")
    call process_character (sa, appearance="", text="Я-я думаю, тебе следует...")
    call process_character (sa, appearance="", text="Я чувствую себя прекрасно.")
    call process_character (n, appearance="", text="Я-я тоже, ах!")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Интересно, каково это будет, если [n.say_name]...)")
    call process_character (sa, appearance="", text="(Кончит?)")
    call process_character (n, appearance="", text="Ах, ох...")
    call process_character (n, appearance="", text="(Если я продолжу, сперма войдет в [sa.say_name]...)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Ты хочешь, чтобы я {w=1.0}кончил, пока мы это делаем?")
    call process_character (sa, appearance="", text="Ах, ах!")
    call process_character (sa, appearance="", text="Только если ты этого хочешь...")
    call process_character (n, appearance="", text="Д-да, давай попробуем.")
    call process_character (sa, appearance="", text="Я хочу посмотреть, смогу ли я сказать, когда это произойдет.")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Это не займет много времени...)")
    call process_character (n, appearance="", text="(Мой член горит!)")
    call process_character (sa, appearance="", text="(Нижняя половина меня дрожит)")
    call process_character (sa, appearance="", text="(Я не могу это контролировать...)")
    call process_character (n, appearance="", text="Ох!")
    call process_character (n, appearance="", text="(Э-это определенно то время...)")
    call process_character (n, appearance="", text="(Толчок проходит через мой пенис)")
    call process_character (n, appearance="", text="Ургх!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
    call static_still_ctc ("bg sam_vaginal_xray_cum")

    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Он спустил внутрь...)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Это забавное...)")
    call process_character (sa, appearance="", text="(Н-но приятное чувство)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Интересно, сколько в ней...)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Т-ты почувствовала это?")
    call process_character (sa, appearance="", text="Д-да.")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Ты не знаешь, оно выйдет наружу?")
    call process_character (sa, appearance="", text="Я-я не знаю...")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Может быть, когда ты вытащишь, часть выйдет?")
    call process_character (n, appearance="", text="Хм, ты думаешь?")
    call process_character (n, appearance="", text="...")

    call static_still_ctc ("bg sam_vaginal_spread_cum")

    call process_character (n, appearance="", text="Я вижу часть выходит!")
    call process_character (n, appearance="", text="Часть спермы выходит!")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Ну, [n.say_name]...")
    call process_character (sa, appearance="", text="М-мы потрахались.")
    call process_character (n, appearance="", text="Э-это и есть трахаться?")
    call process_character (n, appearance="", text="...")
    call process_character (sa, appearance="", text="Думаю, это был один из способов трахаться, да.")
    call process_character (n, appearance="", text="Ты имеешь в виду, есть другие способы?")
    call process_character (sa, appearance="", text="Из того, что я видела...")
    call process_character (sa, appearance="", text="Их гораздо больше.")

    python:
        if not dream:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_flat_breasts", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_incestual_situation", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_vaginal_sex", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_given_vaginal_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

        sa.revistable_scenes.add("sam_scene_vaginal_revisit")

    call process_end_of_scene ("sam_scene_vaginal", char=sa, dream=dream)

    return


label sam_scene_vaginal_revisit:
    $ no_bust_art = False
    if "sam_scene_vaginal_revisit" not in scenes_completed:
        call process_character (n, appearance="pose twohandfist face neutral")
        call process_character (sa, appearance="pose handface face neutral", text="Да!")
        call process_character (n, appearance="pose handpocket face neutral")
        call process_character (sa, appearance="pose handface face neutral", text="Позволь мне убедиться, что стрим готов к работе.")
        call process_character (sa, appearance="pose leaning face neutral", text="Наши зрители получат такой сюрприз!")

        call sam_scene_vaginal_revisit_on_stream
    else:
        call process_character (n, appearance="pose behindhead face neutral")
        call process_character (sa, appearance="pose handface face neutral", text="Не понимаю, почему бы и нет!")

        call sam_scene_vaginal_revisit_off_stream


    return

label sam_scene_vaginal_revisit_on_stream:
    $ play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)
    call process_scene_beginning ("bg sam_vaginal_dick_out")

    call process_character (sa, appearance="", text="Добро пожаловать всем!")
    call process_character (sa, appearance="", text="Приятно видеть всех вас!")
    call process_character (n, appearance="", text="Ты видишь, кто подключился?")
    call process_character (n, appearance="", text="Я не могу смотреть на экран.")
    call process_character (sa, appearance="", text="Я могу видеть чат отсюда.")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Хаха!")
    call process_character (sa, appearance="", text="[n.say_name], я вижу твою задницу в видео-превью!")

    call static_still_ctc ("bg sam_vaginal_dick_in")

    call process_character (sa, appearance="", text="А, ха...")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="О, эти комментарии чата!")
    call process_character (n, appearance="", text="Что они говорят?")
    call process_character (sa, appearance="", text="Есть пара подписчиков, которые продолжают говорить: \"Вот это Задница.\"")
    call process_character (sa, appearance="", text="Я думаю, они имеют в виду твою задницу, [n.say_name]!")

    call static_still_ctc ("bg sam_vaginal_dick_out")

    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Извините, я не могу видеть всех в чате. Ах...")
    call process_character (n, appearance="", text="В такой позе трудно что-то увидеть.")
    call process_character (sa, appearance="", text="Я вижу много новичков, которые только подошли!")

    call static_still_ctc ("bg sam_vaginal_dick_in_eyes_closed")

    call process_character (sa, appearance="", text="Для тех, кто задается вопросом, ах, {w=0.5}мы будем транслировать еще немного Демон Может Смеяться 2 позже!")
    call process_character (sa, appearance="", text="Мы просто думали, что вам понравится наше специальное начало!")
    call process_character (n, appearance="", text="Ах, ах!")

    call static_still_ctc ("bg sam_vaginal_dick_in")

    call process_character (sa, appearance="", text="ТрикМик3 говорит...")
    call process_character (sa, appearance="", text="\"Сегодня я сорвал хороший орех! Спасибо!\"")
    call process_character (sa, appearance="", text="Это потрясающе, рада, что мы помогли Вам сорвать орех, ТрикМик3!")

    call static_still_ctc ("bg sam_vaginal_dick_out")

    call process_character (sa, appearance="", text="...{p}...")
    call process_character (sa, appearance="", text="Это отличное предложение МуувОвер!")
    call process_character (n, appearance="", text="Какое?")
    call process_character (sa, appearance="", text="Он сказал, что у нас должен быть счетчик, который отслеживает, сколько зрителей \"рвут орехи\" во время стрима!")
    call process_character (sa, appearance="", text="Интересно, что они имеют ввиду?")

    call static_still_ctc ("bg sam_vaginal_dick_in_eyes_closed")

    call process_character (n, appearance="", text="Ах, ах.")
    call process_character (n, appearance="", text="В чате были какие-нибудь хорошие названия?")
    call process_character (sa, appearance="", text="...")

    call static_still_ctc ("bg sam_vaginal_dick_in")

    call process_character (sa, appearance="", text="Хм, ахх...")
    call process_character (sa, appearance="", text="Н-еще нет.")
    call process_character (sa, appearance="", text="...")

    menu:
        "Как насчёт \"Ореховая пирушка?\"":
            call process_character (sa, appearance="", text="Да, думаю, это очевидный выбор.")
            call process_character (sa, appearance="", text="Иногда самые очевидные названия-самые лучшие!")
        "Как насчёт \"Щелкунчик?\"":
            call add_points (sa, 1, tag="sam_scene_vaginal_revisit_nutcracker")
            call process_character (sa, appearance="", text="Хаха!")
            call process_character (sa, appearance="", text="Щелкунчик?")
            call process_character (sa, appearance="", text="Вы, ребята, слышали, что [n.say_name] сказал?")
            call process_character (sa, appearance="", text="...")
            call process_character (sa, appearance="", text="Чату, конечно, понравилось это название, [n.say_name]!")
            call process_character (sa, appearance="", text="Думаю, ты выбрал бесспорного победителя!")

    call static_still_ctc ("bg sam_vaginal_xray")

    call process_character (sa, appearance="", text="Аахх...")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Да, он определенно чат выбирает это название.")
    call process_character (n, appearance="", text="Что это?")
    call process_character (sa, appearance="", text="Ахх...")
    call process_character (sa, appearance="", text="Ты слишком далеко залезаешь в меня своим членом.")
    call process_character (sa, appearance="", text="Они называют это \"по самые шары\".")
    call process_character (sa, appearance="", text="...")
    call process_character (n, appearance="", text="Ах, ах...")
    call process_character (sa, appearance="", text="[n.say_name], они хотят, чтобы ты двигался быстрее!")
    call process_character (n, appearance="", text="Если ты просишь...")
    call process_character (n, appearance="", text="Я-я буду продолжать столько, сколько смогу!")
    call process_character (sa, appearance="", text="Продолжай в том же духе! Продолжай!")
    call process_character (sa, appearance="", text="Мы почти установили новый рекорд для зрителей!")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Чем быстрее я толкаю, тем скорее я...")
    call process_character (sa, appearance="", text="У меня тоже такое чувство возникает.")
    call process_character (sa, appearance="", text="Но если мы можем просто подождать...")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", xalign = 0.97, yalign = 0.97)

    call process_character (n, appearance="", text="Хмм, ах!")
    call process_character (n, appearance="", text="[sa.say_name[0]]-[sa.say_name]...")
    call process_character (sa, appearance="", text="Ааах, ах!")
    call process_character (sa, appearance="", text="В-всем приготовься!")
    call process_character (n, appearance="", text="Я не могу удержаться...")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
    call static_still_ctc ("bg sam_vaginal_xray_cum")

    "[n.say_name] & [sa.say_name]" "Ооох!"

    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="И вот оно!")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Отдайте должное [n.say_name], он держался!")
    call process_character (n, appearance="", text="...")
    call process_character (sa, appearance="", text="[n.say_name] может долго гораздо...")
    call process_character (sa, appearance="", text="Он оторвался, как и все мы!")
    call process_character (n, appearance="", text="Но в следующий раз я продержусь дольше!")
    call process_character (sa, appearance="", text="Да...")
    call process_character (sa, appearance="", text="И чат просит тебя двигаться быстрее, ха-ха!")
    call process_character (n, appearance="", text="...")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Чат спрашивает, ты \"наполнил меня.\"")

    call static_still_ctc ("bg sam_vaginal_spread_cum")

    call process_character (sa, appearance="", text="Я бы сказала!")
    call process_character (sa, appearance="", text="Если присмотреться, то можно увидеть, как часть капает...")
    call process_character (n, appearance="", text="Мне казалось, что я выстрелил хорошее количество.")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Хорошо...")
    call process_character (sa, appearance="", text="Дайте [n.say_name] и мне пять секунд, чтобы помыться и выпить немного воды.")
    call process_character (sa, appearance="", text="А когда вернемся, перейдем к играм!")

    call sam_scene_vaginal_revisit_end

    return

label sam_scene_vaginal_revisit_off_stream:
    $ play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)
    call process_scene_beginning ("bg sam_vaginal_dick_out")

    call process_character (sa, appearance="", text="Ты знаешь...")
    call process_character (sa, appearance="", text="Это вроде как мило, что мы делаем это вне стрима.")
    call process_character (sa, appearance="", text="Мы можем просто наслаждаться этим чувством.")
    call process_character (sa, appearance="", text="И не должны идти в ногу с чатом.")
    call process_character (n, appearance="", text="Д-Да...")
    call static_still_ctc ("bg sam_vaginal_dick_in_eyes_closed")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Интересно, как часто другие люди это делают)")
    call process_character (sa, appearance="", text="(Кажется, невозможно устоять перед желанием делать это каждый день!)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Я предпочитаю это видеоиграм!)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Ну, это точно равно видеоиграм)")
    call static_still_ctc ("bg sam_vaginal_dick_out")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Мой член входит так легко!)")
    call static_still_ctc ("bg sam_vaginal_dick_in_eyes_closed")
    call process_character (n, appearance="", text="(Я чувствую, как мой пенис скользит в киске [sa.say_name])")
    call process_character (n, appearance="", text="...")

    call static_still_ctc ("bg sam_vaginal_xray")

    call process_character (sa, appearance="", text="Ммм!")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Мне действительно нравится, когда он двигается медленно)")
    call process_character (sa, appearance="", text="(Он дотрагивается до каждой точки внутри моей киски...)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", xalign = 0.97, yalign = 0.97)

    call process_character (n, appearance="", text="{i}Вздох, Вздох{/i}")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
    call static_still_ctc ("bg sam_vaginal_xray_cum")

    call process_character (n, appearance="", text="Хрм!")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Он прямо взорвался во мне!)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Это должно быть хорошо для него)")
    call process_character (sa, appearance="", text="(Это было потрясающе для меня!)")
    call process_character (sa, appearance="", text="...{p}...")
    call process_character (sa, appearance="", text="(Я бы делала это в любое время)")
    call process_character (sa, appearance="", text="(Во время и после стрима...)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Пока мы хорошо проводим время, для меня это не имеет значения)")

    call sam_scene_vaginal_revisit_end
    return

label sam_scene_vaginal_revisit_end:
    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_incestual_situation", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_vaginal_sex", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_given_vaginal_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("sam_scene_vaginal_revisit", char=sa, force_no_boldness=True, reset_prompted_scene=False, force_not_replayable=True, revisit=True)
    return

label sam_scene_blowjob(dream=False):
    call sam_scene_blowjob_sex (dream=dream)

    return

label sam_scene_blowjob_sex(dream=False):
    call process_scene_beginning (bg="bg nate_room_daytime", dream=dream )


    $ sam_scene_blowjob_character = ""
    if "kira_scene_tip_blowjob" in scenes_completed:
        $ sam_scene_blowjob_character = k.say_name
    elif "simone_scene_blowjob" in scenes_completed:
        $ sam_scene_blowjob_character = "Mom"
    elif "julia_scene_blowjob" in scenes_completed:
        $ sam_scene_blowjob_character = julia.say_name
    elif "vicky_scene_blowjob" in scenes_completed:
        $ sam_scene_blowjob_character = vicky.say_name
    elif "gloryhole_scene_blowjob" in scenes_completed:
        $ sam_scene_blowjob_character = gloryhole_girl.say_name
    elif "janet_scene_blowjob" in scenes_completed:
        $ sam_scene_blowjob_character = janet.say_name


    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Хм...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="(Интересно, как я должен начать свой день...)")
    call process_character (n, appearance="pose handfist face neutral blush false", text="(Я мог бы прыгнуть прямо в бассейн)")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="(Или, может быть, проверить, какие новые видеоигры были выпущены!)")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="...")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="(Или я бы мог...)")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face aroused blush false", text="(Потрогать мой пенис немного)")
    call process_character (n, appearance="pose behindhead face aroused blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face aroused blush false", text="(Да...)")
    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face aroused blush false", text="(Это кажется хорошей идеей...)")
    call character_leave_dissolve (n)
    pause 0.5

    call process_character (n, appearance="outfit nudehard pose handsdown face aroused blush true", text="...")
    call process_character (n, appearance="outfit nudehard pose handsdown face aroused blush true", text="{cps=40}(Я просто буду касаться его в течение нескольких минут и-){/cps}{w=0.75}{nw}")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false")
    call process_character (n, appearance="outfit nudehard pose handsdown face aroused blush true")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Эй, [n.say_name]!")
    call process_character (n, appearance="pose twohandfist face embarrassed blush true", text="Ах!")
    call process_character (sa, appearance="pose handface face happy blush false", text="Ха-ха, я напугала тебя?")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Я не ожидал, что ты будешь здесь!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Ну, тебе нужно освежить память!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ты сказал, что я могу прийти в любое время в твою комнату.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Поэтому я воспользовалась возможностью, чтобы зайти!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="К тому же, ты всегда оставляешь дверь незапертой.")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="{i}Задыхается{/i}...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Ты собирался поиграть со своим пенисом?")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Нуу...")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Я тут подумал об этом...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ох, ох!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Можно мне с ним поиграть?")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Пожалуйста?")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="Ты хочешь поиграть с ним?")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Да!")
    call character_leave_dissolve (sa)
    pause 0.5

    call process_character (sa, appearance="outfit nude pose handface face neutral blush false", text="Я готова немного повеселиться!")
    call process_character (n, appearance="pose handsdown face curious blush true", text="...")
    call process_character (n, appearance="pose handsdown face curious blush true", text="Что ты планировал сделать?")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Посмотрим.")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Но сначала мне нужно подойти очень близко...")
    call fade_to_black (1)
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Эй!")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Твое лицо прямо напротив моего...")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg sam_bj_lick")

    call process_character (n, appearance="pose handsbehind face flirty blush false", text="...{p}...")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="[sa.say_name[0]]-[sa.say_name]...")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Почему ты лижешь мой пенис?")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Я не знаю...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Я дотронулась до него, и он потерла, как раньше...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="И подумала, почему бы не попробовать лизнуть его?")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="...")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="(Это кажется случайностью)")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Ах!")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Хм?")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Тебе нравится, когда я его облизываю?")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Фактически...")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Д-Да.")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Он чувствует себя хорошо.")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Правда?")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="(Может быть, я нашла что-то...)")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Ты что, хочешь продолжать его облизывать?")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Думаешь, мне стоит попробовать что-то другое?")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Тебе решать, ах...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Хм...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="(Эта кожа на кончике его члена)")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="(Она выглядит эластичной)")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="(Интересно, если бы я могла...)")
    call static_still_ctc ("bg sam_bj_foreskin_play")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Хаах!")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Т-ты дергаешь за кожу!")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Ты чувствуешь себя плохо?")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="{i}Вздох{/i}")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Н-Нет...")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Нисколько.")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Должна ли я продолжать тянуть её?")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Д-Да.")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="(Его пенис действительно твердый, но кожа мягкая и податливая на моих губах)")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="...")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="(Я надеюсь, что она не натянет её слишком далеко...)")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="(Но она осторожна)")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="([n.say_name] очень нравится то, что я делаю!)")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Хм...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="(Есть ли что-нибудь еще, что я могу попробовать своим ртом?)")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="(Теперь, когда я думаю об этом...)")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="(Его пенис выглядит так, как будто он может войти в мой...)")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Эй [n.say_name]...")
    call process_character (n, appearance="pose handsbehind face flirty blush false", text="Да?")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Я просто подумала об этом, но…")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face flirty blush false", text="Думаешь, мне стоит засунуть твой член себе в рот?")

    if sam_scene_blowjob_character:
        call process_character (n, appearance="", text="Я-я думаю, тебе стоит, да.")
        call process_character (n, appearance="", text="(Интересно, будет ли это похоже на то, когда [sam_scene_blowjob_character] это делала)")
    else:
        call process_character (n, appearance="", text="В-возможно.")
        call process_character (n, appearance="", text="Если тебе захочется попробовать.")


    call process_character (sa, appearance="", text="Окей!")
    call process_character (sa, appearance="", text="Я собираюсь пойти на это!")
    call static_still_ctc ("bg sam_bj_suck")
    call process_character (n, appearance="", text="!!")
    call process_character (n, appearance="", text="(Она засунула его себе в рот!)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Я не думаю, что могу вместить все это...)")
    call process_character (sa, appearance="", text="(Его член рядом с задней частью моего горла!)")

    if sam_scene_blowjob_character:
        call process_character (n, appearance="", text="(Она очень ласковая)")
        call process_character (n, appearance="", text="(Это намного отличается от того, когда [sam_scene_blowjob_character] делала это со мной)")
    else:
        call process_character (n, appearance="", text="Ах...")
        call process_character (n, appearance="", text="(Мой член движется в ее рту!)")

    call process_character (sa, appearance="", text="Ммм...")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Хм?")
    call process_character (sa, appearance="", text="(Он продолжает биться о верх моего рта!)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Я тоже чувствую, как он пульсирует)")
    call process_character (n, appearance="", text="Ахх...")
    call process_character (n, appearance="", text="(Может ли она вместить больше во рту?)")
    call process_character (sa, appearance="", text="Ммф!")
    call process_character (sa, appearance="", text="(Интересно, что произойдет, если я зажму губы...)")
    call process_character (n, appearance="", text="Хаах!")
    call process_character (sa, appearance="", text="Что-то тебе не понравилось?")
    call process_character (n, appearance="", text="Я на самом деле чувствовал себя великолепно!")
    call process_character (n, appearance="", text="Ты можешь сделать это еще немного?")
    call process_character (sa, appearance="", text="Конечно!")
    call process_character (n, appearance="", text="Ах, ах...")

    if sam_scene_blowjob_character:
        call process_character (n, appearance="", text="(Это начинает немного напоминать то, что [sam_scene_blowjob_character] делала со мной)")

    call process_character (sa, appearance="", text="Мм, мм...")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="[n.say_name]...")
    call process_character (n, appearance="", text="Д-да?")
    call process_character (sa, appearance="", text="Если я буду продолжать делать это...")
    call process_character (sa, appearance="", text="Сперма выйдет?")
    call process_character (n, appearance="", text="Вообще-то, я как раз собирался тебе сказать.")
    call process_character (sa, appearance="", text="Ну...")
    call process_character (sa, appearance="", text="Я могу что-нибудь сделать, чтобы это случилось раньше?")

    if sam_scene_blowjob_character:
        call process_character (n, appearance="", text="Может, попробуешь двигать головой туда-сюда.")
        call process_character (n, appearance="", text="Держи губы вокруг моего пениса, пока делаешь это.")
        call process_character (sa, appearance="", text="Хм, да!")
        call process_character (sa, appearance="", text="Посмотри, что из этого получится!")
    else:
        call process_character (n, appearance="", text="Я-я не знаю.")
        call process_character (n, appearance="", text="Ты о чем-то задумалась?")
        call process_character (sa, appearance="", text="Думаю, я попробую потянуть за твой член, пока мои губы вокруг него.")

    call process_character (n, appearance="", text="{i}Вздох{/i}, {i}Вздох{/i}...")
    call process_character (sa, appearance="", text="Ммф...")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Это работает?")
    call process_character (n, appearance="", text="Это...")
    call process_character (n, appearance="", text="Я-я...")
    call process_character (sa, appearance="", text="Что, [n.say_name]?")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="{cps=40}это помогает тебе с-{/cps}{w=0.75}{nw}")
    call static_still_ctc ("bg sam_bj_cum")
    call process_character (sa, appearance="", text="!!!")
    call process_character (sa, appearance="", text="(Это на моем лице!)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Я думаю [sa.say_name] не ожидала этого)")
    call process_character (sa, appearance="", text="(Есть ещё!)")
    call process_character (n, appearance="", text="...{p}...")
    call process_character (n, appearance="", text="(Я надеюсь, что это не испугало ее)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Прости, [sa.say_name].")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Простить за что?")
    call process_character (n, appearance="", text="Я должен был сказать тебе, что это выйдет...")
    call process_character (sa, appearance="", text="Ох...")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Все нормально.")
    call process_character (n, appearance="", text="Ты, кажется, была поражена этим.")
    call process_character (sa, appearance="", text="Ну...")
    call process_character (sa, appearance="", text="Я ожидала, что это произойдет.")
    call process_character (sa, appearance="", text="Я просто не знала точно, когда.")
    call process_character (sa, appearance="", text="Это сумасшествие видеть, как белая штука вырвалась из твоего члена!")
    call process_character (n, appearance="", text="Я думаю, много вышло, потому что мы делали это.")
    call process_character (sa, appearance="", text="Да? Правда?")
    call process_character (sa, appearance="", text="Потрясающе!")
    call process_character (sa, appearance="", text="Я надеялась, что делаю правильно.")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Я многому научилась из этого!")
    call process_character (sa, appearance="", text="Теперь у меня есть еще несколько способов развлечься с твоим пенисом!")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Мне нравится пробовать что-то новое.")
    call process_character (sa, appearance="", text="Я могу сказать, ха-ха!")
    call process_character (sa, appearance="", text="Ты корчил смешные рожицы, пока я это делала!")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Его сперма похожа на липкий лосьон)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Это делает мое лицо теплым)")


    python:
        sa.revistable_scenes.add("sam_scene_blowjob_revisit")

        if not dream:
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_foreskin_played_with", 1)
            stats.add_stat("times_given_facial", 1)
            stats.add_stat("times_received_blowjob", 1)
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_had_penis_seen", 1)

    call process_end_of_scene ("sam_scene_blowjob", char=sa, dream=dream )

    return

label sam_scene_blowjob_revisit:
    $ no_bust_art = False
    call process_character (n, appearance="pose behindhead face neutral blush false")
    if "sam_scene_blowjob_revisit" in scenes_completed:
        call process_character (sa, appearance="pose handface face happy blush false", text="Я думала, ты хочешь, чтобы я это сделала!")
        call sam_scene_blowjob_revisit_second_time
    else:
        call process_character (sa, appearance="pose handface face neutral blush false", text="Я надеялся, что ты спросишь меня об этом!")
        call process_character (sa, appearance="pose leaning face happy blush false", text="В этот раз я точно знаю, что делать!")
        call sam_scene_blowjob_revisit_first_time


    return

label sam_scene_blowjob_revisit_first_time:
    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg sam_bj_lick")
    call process_character (sa, appearance="", text="Ничего, если я снова его оближу?")
    call process_character (n, appearance="", text="Ты уже его облизываешь...")
    call process_character (sa, appearance="", text="А, точно...")
    call process_character (sa, appearance="", text="Тогда, {w=0.5} ничего, если я продолжу лизать?")
    call process_character (n, appearance="", text="Ну конечно!")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(У него есть некоторые вещи, выходящие из его пениса)")
    call process_character (sa, appearance="", text="(Но это не его сперма)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Интересно, что это такое...)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Имеет соленый вкус)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="([sa.say_name] выясняет, где мне будет лучше.)")
    call process_character (n, appearance="", text="(Её язык касается более чувствительных мест на этот раз!)")
    call process_character (sa, appearance="", text="Ммм.")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Мне любопытно, [n.say_name]...")
    call process_character (sa, appearance="", text="Что ты хочешь, чтобы я сделала с твоим членом дальше?")
    call process_character (n, appearance="", text="Ты хочешь, чтобы я выбрал?")
    call process_character (sa, appearance="", text="Почему нет?")
    call process_character (sa, appearance="", text="Я попрошу тебя решить, что тебе больше нравится.")

    menu:
        "Можешь потянуть мою кожу на пенисе?":
            call process_character (sa, appearance="", text="Это действительно интересно делать!")
            call static_still_ctc ("bg sam_bj_foreskin_play")
            call process_character (sa, appearance="", text="Кожа такая эластичная!")
            call process_character (n, appearance="", text="Аах!")
            call process_character (n, appearance="", text="Не тяни слишком далеко.")
            call process_character (sa, appearance="", text="Я не буду.")
            call process_character (n, appearance="", text="...")
            call process_character (n, appearance="", text="(Она такая нежная)")
            call process_character (n, appearance="", text="Ах, ах...")
            call process_character (n, appearance="", text="(Но она тянет в самый раз...)")
            call process_character (sa, appearance="", text="([n.say_name] по душе это, я могу сказать)")
            call process_character (sa, appearance="", text="...")
            call process_character (sa, appearance="", text="(Я определенно делаю лучше на этот раз!)")
            call process_character (sa, appearance="", text="...")
            call process_character (sa, appearance="", text="(Есть еще одна вещь, которую нужно сделать)")
            call process_character (sa, appearance="", text="[n.say_name]?")
            call process_character (n, appearance="", text="Хм?")
            call process_character (sa, appearance="", text="Давай я положу свой рот на твой член.")
            call process_character (n, appearance="", text="В-вперед!")
        "Положи в рот мой хер.":
            call add_boldness (1, tag="sam_scene_blowjob_revisit_mouth_around_dick")
            call process_character (sa, appearance="", text="Все в порядке!")
            call process_character (sa, appearance="", text="Я надеялась, что ты захочешь этого!")
            call process_character (sa, appearance="", text="Я посмотрю, как хорошо я смогу на этот раз.")

    call static_still_ctc ("bg sam_bj_suck")
    call process_character (n, appearance="", text="Ох!")
    call process_character (sa, appearance="", text="Ммм, Ммф...")
    call process_character (sa, appearance="", text="(Теперь это имеет больше смысла)")
    call process_character (sa, appearance="", text="(Это приятно для [n.say_name], когда я двигаю головой вперед и назад...)")
    call process_character (sa, appearance="", text="(Но он также любит, когда я сжимаю его член губами)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Ему нравится, как я отсасываю)")
    call process_character (n, appearance="", text="Э-это удивительно, [sa.say_name]!")
    call process_character (n, appearance="", text="{i}Вздох{/i}...")
    call process_character (n, appearance="", text="Думаю, я кончу очень скоро такими темпами.")
    call process_character (sa, appearance="", text="Хм...")
    call process_character (sa, appearance="", text="(Давай посмотрим, как скоро ты кончишь)")
    call process_character (n, appearance="", text="([sa.say_name] сосёт сильнее!)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Мне нравится заставлять моего брата чувствовать себя так)")
    call process_character (sa, appearance="", text="(И я никогда не понимала, как это легко!)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Интересно, если [n.say_name] хотел бы, чтобы я сделала это утром, когда мы только просыпаемся)")
    call process_character (sa, appearance="", text="(Или, может быть, мы могли бы сделать это прямо перед сном)")
    call process_character (n, appearance="", text="Ах, [sa.say_name]...")
    call process_character (n, appearance="", text="Э...это должно сейчас произойти...")
    call process_character (sa, appearance="", text="(Возможно, мы могли бы попробовать это в душе или даже бассейне!)")
    call process_character (sa, appearance="", text="{cps=40}(Я думаю, мы могли бы сделать это в любом месте, где мы чувствовали себя-){/cps}{w=0.75}{nw}")
    call process_character (n, appearance="", text="Хннг!")
    call static_still_ctc ("bg sam_bj_cum")
    call process_character (sa, appearance="", text="Ах!")
    call process_character (sa, appearance="", text="Она опять на меня попала!")
    call process_character (n, appearance="", text="Я сделал все возможное, чтобы предупредить тебя.")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Это была моя вина.")
    call process_character (sa, appearance="", text="Я не обратила внимания.")
    call process_character (n, appearance="", text="Ах, ах...")
    call process_character (n, appearance="", text="Кажется, осталось еще немного.")
    call process_character (sa, appearance="", text="Он просто стреляет из твоего члена!")
    call process_character (sa, appearance="", text="Интересно, как он это делает...")
    call process_character (n, appearance="", text="Я-я не знаю.")
    call process_character (sa, appearance="", text="Твоя сперма прилипает и к моему лицу!")
    call process_character (sa, appearance="", text="Думаю, на этот раз было еще больше.")
    call process_character (n, appearance="", text="Казалось, что это то же количество.")
    call process_character (sa, appearance="", text="У меня на лице много осталось.")
    call process_character (sa, appearance="", text="Но это ладно!")
    call process_character (sa, appearance="", text="Мне нравится это чувство.")

    call sam_scene_blowjob_revisit_end
    return

label sam_scene_blowjob_revisit_second_time:
    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg sam_bj_suck")
    call process_character (sa, appearance="", text="Мммф...")
    call process_character (sa, appearance="", text="(Я всё правильно делаю!)")
    call process_character (sa, appearance="", text="(Я знаю, что делаю это правильно, когда слышу шум от моего сосания!)")
    call process_character (n, appearance="", text="(Это здорово, что [sa.say_name] хочет делать это со мной)")
    call process_character (n, appearance="", text="(Это гораздо лучшая альтернатива, чтобы теребить мой пенис самостоятельно)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Надо совместить всё, что я узнала...)")
    call static_still_ctc ("bg sam_bj_foreskin_play")
    call process_character (n, appearance="", text="Ахх!")
    call process_character (sa, appearance="", text="(Да! Как насчёт...)")
    call process_character (sa, appearance="", text="([n.say_name], определенно нравится!)")
    call process_character (sa, appearance="", text="(Его глаза прищуриваются)")
    call process_character (sa, appearance="", text="(Вот когда я знаю, что он чувствует себя хорошо)")
    call static_still_ctc ("bg sam_bj_lick")
    call process_character (sa, appearance="", text="(Я буду лизать его член дальше)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="([n.say_name] наслаждается, когда я трогаю кончик его пениса)")
    call process_character (sa, appearance="", text="(Он должен быть чувствительным там)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Это так же хорошо, как и в первый раз)")
    call process_character (n, appearance="", text="(Невозможно не наслаждаться этим!)")
    call static_still_ctc ("bg sam_bj_suck")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Ах да...")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Я знаю, что ты скоро кончишь.")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Можешь сделаешь это на моё лице, если хочешь.")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!")
    $ quick_menu = True

    call static_still_ctc ("bg sam_bj_cum")
    call process_character (sa, appearance="", text="Он начинает стрелять!")
    call process_character (n, appearance="", text="Ах, это!")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Думаешь, у тебя когда-нибудь кончится сперма?")
    call process_character (n, appearance="", text="Я-я не знаю.")
    call process_character (n, appearance="", text="Этого еще не происходило.")
    call process_character (sa, appearance="", text="Я надеюсь, что ты этого не будет!")
    call process_character (sa, appearance="", text="Я хочу посмотреть, смогу ли я заставить тебя выстрелить дальше в следующий раз!")

    call sam_scene_blowjob_revisit_end
    return

label sam_scene_blowjob_revisit_end:

    python:
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_foreskin_played_with", 1)
        stats.add_stat("times_given_facial", 1)
        stats.add_stat("times_received_blowjob", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_had_penis_seen", 1)

    call process_end_of_scene ("sam_scene_blowjob_revisit", char=sa, force_no_boldness=True, reset_prompted_scene=False, force_not_replayable=True, revisit=True)
    return

label sam_scene_anal(dream=False):
    call sam_scene_anal_sex (dream=dream)

    return

label sam_scene_anal_sex(dream=False):

    $ sam_scene_anal_character = ""
    if "kira_scene_anal" in scenes_completed:
        $ sam_scene_anal_character = k.say_name
    elif "simone_scene_anal" in scenes_completed:
        $ sam_scene_anal_character = "Mom"

    call process_scene_beginning (bg=sam_room, dream=dream, char_tuple_array=[(sa, "outfit nude pose handface face neutral blush false"), (n, "outfit clothesjacket pose handpocket face neutral blush false")])

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Привет, [sa.say_name]...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Трансляция уже началась?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Привет!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="На самом деле, нет.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Тогда зачем ты раздеваешься?")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Знаешь, я так привыкла проводить стрим голышом...")
    call process_character (sa, appearance="pose handface face happy blush false", text="Я чувствую, что надевать одежду необязательно.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Думаю, в этом есть смысл.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Кроме того, ты можешь видеть меня голой чаще!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Я знаю, тебе это нравится!")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face concerned blush false", text="...")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Я вижу шишку у тебя в штанах!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="У тебя уже встал!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Ну?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Ты тоже собираешься раздеться?")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Давай немедленно!")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (n, appearance="outfit nudehard pose handsdown face neutral blush false")
    call process_character (sa, appearance="pose handsbehind face happy blush false")
    call process_character (sa, appearance="pose handface face neutral blush false", text="...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Ты уже выглядишь более комфортно!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Разве не здорово быть голым?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Это больше не кажется странным, это точно.")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Это здорово, когда жарко, и мы можем просто сорвать нашу одежду, чтобы остыть.")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="...")
    call process_character (sa, appearance="pose leaning face happy blush false", text="И так легче трахаться друг с другом!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Ты хотел трахаться прямо сейчас?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Я действительно этого хочу!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Но...")
    call process_character (n, appearance="pose handsdown face curious blush false", text="Но?")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Тут есть супер крутой шутер от первого лица, в который я хотела сыграть.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="И он только закачался.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Так что я хотела бы сыграть в него.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="О, хорошо.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ничего страшного.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Мы можем потрахаться позже.")
    call process_character (sa, appearance="pose handface face curious blush false", text="Хм...")
    call process_character (sa, appearance="pose handface face curious blush false", text="...")
    call process_character (sa, appearance="pose handface face concerned blush false", text="Проклятье, я разрываюсь.")
    call process_character (sa, appearance="pose handface face concerned blush false", text="...")
    call process_character (n, appearance="pose handsdown face neutral blush false")
    call process_character (sa, appearance="pose handface face concerned blush false")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Например, я хочу ожесточённо сыграть в эту новую игру.")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="...")
    call process_character (sa, appearance="pose handface face curious blush false", text="Но в то же время, я в настроении трахаться...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Я бы не стал об этом беспокоиться.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Давай просто сядем и начнем игру.")
    call process_character (sa, appearance="pose handface face curious blush false", text="Садись, садись...")
    call process_character (sa, appearance="pose handface face curious blush false", text="...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Вот и все, [n.say_name]!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="В чем дело?")
    call process_character (sa, appearance="pose leaning face happy blush false", text="У меня есть решение нашей дилеммы!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Решение?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Все, что нам нужно, это кресло!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Только один стул?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Один из нас будет сидеть на полу?")
    call process_character (sa, appearance="pose handface face happy blush false", text="Нет!")
    call process_character (sa, appearance="pose handface face happy blush false", text="Мы оба будем использовать этот кресло, хе-хе.")
    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="pose handsdown face curious blush false", text="(Что задумала [sa.say_name]?)")

    call fade_to_black (1)
    call bust_art_background (sam_room)

    call process_character (sa, appearance="pose handsbehind face neutral blush false")
    call process_character (n, appearance="pose handsdown face curious blush false")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Я принёс кресло.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Здорово!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Теперь садись на него первым.")

    call fade_to_black (1)

    call process_character (sa, appearance="pose leaning face happy blush false", text="Хорошо.")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Мне просто нужно вот так сесть...")
    call process_character (n, appearance="pose leaning face happy blush false", text="...")
    call process_character (n, appearance="pose leaning face happy blush false", text="О, понятно.")
    call process_character (n, appearance="pose leaning face happy blush false", text="Ты собираешься сидеть на мне?")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Да...")
    call process_character (sa, appearance="pose leaning face happy blush false", text="{cps=40}Я пытаюсь понять, где твой член-{/cps}{w=0.75}{nw}")
    call process_character (sa, appearance="pose leaning face happy blush false", text="...")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Просто {w=1.0}должна {w=1.0}попасть на верхушку...")
    call process_character (n, appearance="pose leaning face happy blush false", text="Уф!")
    call process_character (n, appearance="pose leaning face happy blush false", text="Эк!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Хватит двигаться!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Я пытаюсь забраться к тебе на колени.")
    call process_character (n, appearance="pose leaning face happy blush false", text="Я знаю, но это сложно.")
    call process_character (sa, appearance="pose leaning face happy blush false", text="...")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Дай мне попробовать подвинуться выше...")
    call process_character (n, appearance="pose leaning face happy blush false", text="Думаешь, эта поза сработает?")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Не могу сказать.")
    call process_character (sa, appearance="pose leaning face happy blush false", text="{cps=40}Позволь мне попробовать двигаться-{/cps}{w=0.75}{nw}")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg sam_anal")

    call process_character (n, appearance="pose leaning face happy blush false", text="Ох!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Хаах!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="...")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Куда делся твой член?")
    call process_character (n, appearance="pose leaning face happy blush false", text="Я чувствую, что очень туго!")
    call process_character (n, appearance="pose leaning face happy blush false", text="Он попала в твою киску?")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Я так не думаю.")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Такое чувство, что он вошёл в мою....")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Моя задница!")
    call process_character (n, appearance="pose leaning face happy blush false", text="Т-твоя задница?!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Думаю, это случилось, когда я поскользнулась.")
    call process_character (n, appearance="pose leaning face happy blush false", text="...{p}...")
    call process_character (n, appearance="pose leaning face happy blush false", text="Он не скользит так легко, как в киске.")
    call process_character (n, appearance="pose leaning face happy blush false", text="Я должен надавить сильнее, чтобы протолкнуть его.")
    call process_character (sa, appearance="pose leaning face happy blush false", text="...")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Хочешь узнать, каково это?")
    call process_character (n, appearance="pose leaning face happy blush false", text="...{p}...")
    call process_character (n, appearance="pose leaning face happy blush false", text="Вообще-то, мне нравится.")
    call process_character (n, appearance="pose leaning face happy blush false", text="(Я думаю, что попробую скользить, как я делал с киской [sa.say_name])")

    call static_still_ctc ("bg sam_anal_blur")

    call process_character (sa, appearance="pose leaning face happy blush false", text="Ах, ах!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="...")
    call process_character (sa, appearance="pose leaning face happy blush false", text="(Я никогда и не думала засунуть член [n.say_name] в мою задницу)")
    call process_character (sa, appearance="pose leaning face happy blush false", text="(Не могу поверить, что он может поместиться!)")

    if sam_scene_anal_character:
        call process_character (n, text="Ахх!")
        call process_character (n, text="(Я думал, что это будет похоже на то, когда [sam_scene_anal_character] делала это со мной)")
        call process_character (n, text="(Но оно чувствуется совсем по-другому с [sa.say_name]!)")
        call process_character (n, text="(Интересно, как далеко я могу зайти...)")
        call process_character (n, text="Ахх!")
    else:
        call process_character (n, text="(Я не ожидал такого!)")
        call process_character (n, text="...")
        call process_character (n, text="(Это намного лучше, чем я думал!)")
        call process_character (n, text="...")
        call process_character (n, text="(Интересно, как далеко я могу зайти...)")
        call process_character (n, text="Ахх!")

    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Ты наслаждаешься этим, [n.say_name].")
    call process_character (n, appearance="", text="Ммм...")
    call process_character (n, appearance="", text="Это не похоже ни на что, что мы делали раньше!")
    call process_character (sa, appearance="", text="{i}Вздох{/i}, {i}Вздох{/i}...")
    call process_character (sa, appearance="", text="Ты прав.")
    call process_character (sa, appearance="", text="Ах...")
    call process_character (sa, appearance="", text="Приятно наслаждаться чем-то новым вместе!")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Ты собираешься играть в свою игру?")
    call process_character (sa, appearance="", text="Я... я могу подождать.")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="На данный момент было бы трудно сосредоточиться на игре.")
    call process_character (n, appearance="", text="...{p}...")
    call process_character (n, appearance="", text="[sa.say_name[0]]-[sa.say_name]...")
    call process_character (n, appearance="", text="Я уже близко.")
    call process_character (sa, appearance="", text="Ты хочешь сказать, что хочешь кончить?")
    call process_character (n, appearance="", text="Ммм...")
    call process_character (n, appearance="", text="Я хочу продолжать, но.....")
    call process_character (n, appearance="", text="Слишком сложно сдерживаться.")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Ах...")
    call process_character (n, appearance="", text="Ах...")
    call process_character (sa, appearance="", text="Хорошо, я готова к этому!")

    call static_still_ctc ("bg sam_anal_cum_blur")

    call process_character (n, appearance="", text="Хаах!")
    call process_character (sa, appearance="", text="Ммм!")
    call process_character (sa, appearance="", text="(Я кончаю!)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="{i}Вздох...{/i}")

    call static_still_ctc ("bg sam_anal_cum")

    call process_character (sa, appearance="", text="Ты воткнул в меня свой член, когда кончил.")
    call process_character (n, appearance="", text="Я не мог остановиться.")
    call process_character (n, appearance="", text="Я даже не осознавал, что сделал это.")
    call process_character (sa, appearance="", text="Т-толчок заставил меня кончить.")
    call process_character (n, appearance="", text="Это так?")
    call process_character (sa, appearance="", text="Я почувствовала, что это случилось.")
    call process_character (sa, appearance="", text="А потом внезапно начала кончать.")
    call process_character (sa, appearance="", text="Все мое тело дрожало от этого.")
    call process_character (sa, appearance="", text="Это было такое приятное чувство.")
    call process_character (n, appearance="", text="Я рад, что тебе понравилось!")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Моя задница чувствует себя так странно прямо сейчас!")
    call process_character (sa, appearance="", text="Она, должно быть, наполнена твоей спермой.")
    call process_character (sa, appearance="", text="Мне кажется, что она капает из меня.")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Наверное, играть в видеоигры не очень получилось, да?")
    call process_character (sa, appearance="", text="Я не отказалась бы попробовать снова!")
    call process_character (sa, appearance="", text="В этот раз я не была к этому готова.")
    call process_character (sa, appearance="", text="Но нам просто нужно больше сеансов, чтобы привыкнуть.")
    call process_character (sa, appearance="", text="Я думаю, если делать это несколько раз в день, то поможет!")
    call process_character (n, appearance="", text="Несколько раз в день?")
    call process_character (sa, appearance="", text="Ладно, ладно...")
    call process_character (sa, appearance="", text="Один раз в день на данный момент, {w=1.0}, а затем мы будем стремиться к множеству раз в день!")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Даже один раз утомляет меня!)")

    python:
        sa.revistable_scenes.add("sam_scene_anal_revisit")

        if not dream:
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_seen_butt", 1)
            stats.add_stat("times_seen_butthole", 1)
            stats.add_stat("times_given_anal_sex", 1)
            stats.add_stat("times_given_anal_creampie", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("sam_scene_anal", char=sa, dream=dream )

    return

label sam_scene_anal_revisit:
    $ sam_scene_anal_character = ""
    if "kira_scene_anal" in scenes_completed:
        $ sam_scene_anal_character = k.say_name
    elif "simone_scene_anal" in scenes_completed:
        $ sam_scene_anal_character = "Mom"

    $ no_bust_art = False
    call process_character (n, appearance="pose twohandfist face neutral blush false")
    if "sam_scene_anal_revisit" in scenes_completed:
        call process_character (sa, appearance="pose handface face happy blush false", text="Жопотрах, ха-ха!")
        call process_character (sa, appearance="pose handface face happy blush false", text="Я смеюсь до колик, когда ты это говоришь!")
        call sam_scene_anal_revisit_second_time
    else:
        call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Готов попробовать еще раз?")
        call process_character (sa, appearance="pose leaning face happy blush false", text="Давай посмотрим, сможем ли мы сделать это нарочно на этот раз!")
        call sam_scene_anal_revisit_first_time

    return

label sam_scene_anal_revisit_first_time:
    call fade_to_black (1)

    call process_character (sa, appearance="", text="Я на позиции!")
    call process_character (sa, appearance="", text="Теперь мне просто нужно медленно опуститься.")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Он…он начинает входить!")

    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg sam_anal")

    call process_character (sa, appearance="", text="Вот так-то!")
    call process_character (n, appearance="", text="Ах, ах!")
    call process_character (n, appearance="", text="Все прошло очень легко!")
    call process_character (sa, appearance="", text="Да.")
    call process_character (sa, appearance="", text="На этот раз я был готова к этому...")

    call static_still_ctc ("bg sam_anal_blur")

    call process_character (sa, appearance="", text="{i}Вздох{/i}...")
    call process_character (sa, appearance="", text="([n.say_name] двигается по-разному...)")

    if "kira_scene_anal" in scenes_completed:
        call process_character (n, appearance="", text="...{p}...")
        call process_character (n, appearance="", text="Ты знаешь, как это называется, [sa.say_name]?")
        call process_character (sa, appearance="", text="...")
        call process_character (sa, appearance="", text="Понятия не имею, ахх!")
        call process_character (n, appearance="", text="Я думаю, что это называется...")
        call process_character (n, appearance="", text="\"Трахать зад.\"")
        call process_character (sa, appearance="", text="Это? Хаха!")
        call process_character (sa, appearance="", text="Знаешь, в этом есть смысл.")
    else:
        call process_character (sa, appearance="", text="...{p}...")
        call process_character (sa, appearance="", text="Знаешь, я только что поняла...")
        call process_character (n, appearance="", text="Что такое?")
        call process_character (sa, appearance="", text="Ты трахаешь меня, только в задницу.")
        call process_character (sa, appearance="", text="Так что это скорее \"жопотрах.\"")
        call process_character (n, appearance="", text="Хаха, ты права!")
        call process_character (sa, appearance="", text="Это никогда не было так смешно!")

    call process_character (n, appearance="", text="...{p}...")
    call process_character (n, appearance="", text="(Интересно, каково это для [sa.say_name])")
    call process_character (n, appearance="", text="(Опыт похож на мой?)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Это должно быть, по крайней мере, немного по-другому, так как она чувствует мой член в ней)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Член [n.say_name] такой твёрдый...)")
    call process_character (sa, appearance="", text="(Всё же он может сгибаться и двигаться в моей заднице)")
    call process_character (sa, appearance="", text="...{p}...")
    call process_character (sa, appearance="", text="(Всё равно было бы слишком сложно играть в видеоигры одновременно с этим)")
    call process_character (sa, appearance="", text="(Мой мозг может сосредоточиться только на этом прямо сейчас!)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Сначала я должна попробовать сыграть в простую игру)")
    call process_character (sa, appearance="", text="(Может так мне будет проще сосредоточиться...)")
    call process_character (n, appearance="", text="Ннг!")
    call process_character (n, appearance="", text="(Я не могу долго так её трахать!)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!")
    $ quick_menu = True

    call process_character (n, appearance="", text="Ммм, Ммм...")
    call process_character (sa, appearance="", text="([n.say_name] сжимает мое тело)")
    call process_character (sa, appearance="", text="(Я думаю, что он кончает)")
    call process_character (n, appearance="", text="Я продержался столько, сколько смог...")
    call process_character (n, appearance="", text="Сперма выходит наружу!")

    call static_still_ctc ("bg sam_anal_cum_blur")

    call process_character (n, appearance="", text="Ох!")
    call process_character (sa, appearance="", text="Аах!")
    call process_character (sa, appearance="", text="(Определенно выходит!)")
    call process_character (sa, appearance="", text="(Этот выстрел прямо в мою задницу!)")

    call static_still_ctc ("bg sam_anal_cum")

    call process_character (n, appearance="", text="Фьюю...")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Я должна была следить, насколько долго ты продержался.")
    call process_character (n, appearance="", text="Почему?")
    call process_character (sa, appearance="", text="Так я смогу сравнить и узнать, дольше ли мы это делаем!")
    call process_character (n, appearance="", text="Как долго, по-твоему, мы сможем?")
    call process_character (sa, appearance="", text="Хороший вопрос!")
    call process_character (sa, appearance="", text="Трудно сказать.")
    call process_character (sa, appearance="", text="Но я поняла...")
    call process_character (sa, appearance="", text="Если мы сможем увеличивать на несколько секунд каждый день...")
    call process_character (sa, appearance="", text="То мы будем трахаться больше часа!")
    call process_character (n, appearance="", text="Ч-час?!")
    call process_character (sa, appearance="", text="Оптимистично.")
    call process_character (sa, appearance="", text="А реально, я рассчитываю на тридцать пять минут.")
    call process_character (n, appearance="", text="...")

    call sam_scene_anal_revisit_end
    return

label sam_scene_anal_revisit_second_time:
    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg sam_anal_blur")

    call process_character (sa, appearance="", text="([n.say_name] уже двигается)")
    call process_character (n, appearance="", text="Ах, ах...")
    call process_character (n, appearance="", text="(Это поза оказалась более удобной, чем я ожидал!)")

    if "kira_scene_anal" in scenes_completed:
        call process_character (n, appearance="", text="([k.say_name] села на меня, когда я был на полу)")
        call process_character (n, appearance="", text="(Я не мог даже пошевелиться, когда она начала трахать меня!)")

    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="([sa.say_name], кажется, не возражает)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="([n.say_name] все лучше и лучше!)")
    call process_character (sa, appearance="", text="(Его шансы выглядят хорошо для увеличения времени!)")
    call process_character (sa, appearance="", text="Ахх! Ммм...")
    call process_character (sa, appearance="", text="(Я тоже должна улучшаться)")
    call process_character (sa, appearance="", text="...{p}...")
    call process_character (sa, appearance="", text="Эй [n.say_name]...")
    call process_character (sa, appearance="", text="Что если мы поменяемся местами?")
    call process_character (n, appearance="", text="Думаешь, стоит попробовать по-другому?")
    call process_character (sa, appearance="", text="Полностью зависит от тебя.")
    call process_character (sa, appearance="", text="Если захочешь потрахаться по-другому, дай мне знать.")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Я не могу решить, что мне нравится больше...)")
    call process_character (n, appearance="", text="(Трахать [sa.say_name] во влагалище круто!)")
    call process_character (n, appearance="", text="(Трахать попку [sa.say_name] приятно)")
    call process_character (n, appearance="", text="(И не надо забывать, что [sa.say_name] хорошо отсасывает!)")
    call process_character (n, appearance="", text="(В каждом из этих вариантов есть что-то хорошее...)")

    window hide
    menu:
        "Let's just keep fucking.":
            pass
        "I can switch to fucking your pussy.":
            if "sam_scene_vaginal_revisit" in scenes_completed:
                jump sam_scene_vaginal_revisit_off_stream
            else:
                jump sam_scene_vaginal_revisit_on_stream
        "Can you put my dick in your mouth?":
            if "sam_scene_blowjob_revisit" in scenes_completed:
                jump sam_scene_blowjob_revisit_second_time
            else:
                jump sam_scene_blowjob_revisit_first_time

    call process_character (sa, appearance="", text="Ладно.")
    call process_character (sa, appearance="", text="Постарайся продержаться как можно дольше.")
    call process_character (n, appearance="", text="Я постараюсь...")
    call process_character (n, appearance="", text="Но это будет непросто!")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="([n.say_name] трахает меня немного быстрее каждый раз, когда мы делаем это)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Я с чаще кончаю, когда он набирает скорость)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Если я кончу в то же время, что и [n.say_name], я знаю, что я смогу угнаться за ним!)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!")
    $ quick_menu = True


    call static_still_ctc ("bg sam_anal_cum_blur")

    call process_character (n, appearance="", text="{i}Вздох{/i}, {i}Вздох{/i}...")
    call process_character (n, appearance="", text="Гьяя!")
    call process_character (sa, appearance="", text="Ммм!")
    call process_character (sa, appearance="", text="...")

    call static_still_ctc ("bg sam_anal_cum")

    call process_character (n, appearance="", text="(Это было грязно)")
    call process_character (n, appearance="", text="(Я думаю, часть попала на кресло)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Мы добиваемся прогресса, [n.say_name]!")
    call process_character (sa, appearance="", text="Все еще есть способы увеличить время трахания!")
    call process_character (sa, appearance="", text="Каждая секунда на счету!")

    call sam_scene_anal_revisit_end
    return

label sam_scene_anal_revisit_end:

    python:
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_seen_butt", 1)
        stats.add_stat("times_seen_butthole", 1)
        stats.add_stat("times_given_anal_sex", 1)
        stats.add_stat("times_given_anal_creampie", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("sam_scene_anal_revisit", char=sa, force_no_boldness=True, reset_prompted_scene=False, force_not_replayable=True, revisit=True)
    return

label sam_scene_swimsuit_revisit:
    if store.week.time == "night":
        call process_character (n, text="(Уже поздно)")
        call process_character (n, text="(Я спрошу [sa.say_name] пойдёт ли она завтра в бассейн)")
        $ sa.select()

        return

    if "sam_scene_swimsuit_revisit" not in scenes_completed:
        $ no_bust_art = False
        call process_character (n, appearance="pose handfist face neutral blush false")
        call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Да!")
        call process_character (sa, appearance="pose handface face happy blush false", text="Я надену купальник, который ты мне подарил!")

    if "sam_scene_vaginal" in scenes_completed:
        if "sam_scene_swimsuit_revisit_first_time_has_done_vaginal" in scenes_completed:
            call sam_scene_swimsuit_revisit_second_time_has_done_vaginal
        else:
            call sam_scene_swimsuit_revisit_first_time_has_done_vaginal
    elif "sam_scene_4" in scenes_completed:
        if "sam_scene_swimsuit_revisit_first_time_has_done_grinding" in scenes_completed:
            call sam_scene_swimsuit_revisit_second_time_has_done_grinding
        else:
            call sam_scene_swimsuit_revisit_first_time_has_done_grinding
    else:
        if "sam_scene_swimsuit_revisit" in scenes_completed:
            call sam_scene_swimsuit_revisit_second_time_normal
        else:
            call sam_scene_swimsuit_revisit_first_time_normal
    return

label sam_scene_swimsuit_revisit_first_time_has_done_vaginal:
    call process_scene_beginning (bg=backyard, char_tuple_array=[(sa, "outfit bikini pose leaning face neutral blush false"), (n, "outfit swimsuit pose handsdown face neutral blush false")])


    call process_character (sa, appearance="outfit bikini pose leaning face neutral blush false", text="Знаешь, что мне нравится слышать?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Звук от пузырьков после прыжка!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Этот шипучий звук классный.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Мне нравится хлопать рукой по воде и видеть, как она поднимается в воздух.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="О, да!")
    call process_character (sa, appearance="pose handface face happy blush false", text="[k.say_name] создает гейзеры, когда она это делает!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="[k.say_name] там сейчас?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Ммм, мама тоже.")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Так что придется создавать свои гейзеры!")

    call static_still_ctc ("bg sam_scene_swimsuit_jump_in")

    call process_character (sa, appearance="pose leaning face happy blush false", text="Джеронимо!")
    "{i}Плюх{/i}"
    call process_character (n, appearance="pose leaning face happy blush false", text="Отлично!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Посмотри на волну, которую я сделала этим прыжком!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Ты должен прыгнуть бомбочкой и сделать волну больше!")
    call process_character (n, appearance="pose leaning face happy blush false", text="Хорошо...")
    call process_character (n, appearance="pose leaning face happy blush false", text="На подходе!")
    "{i}Плюх{/i}"
    call process_character (sa, appearance="pose leaning face happy blush false", text="Ух ты!")
    call process_character (n, appearance="pose leaning face happy blush false", text="...")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Вода пошла прямо вверх!")
    call process_character (n, appearance="pose leaning face happy blush false", text="Мило!")

    call fade_to_black (1)

    call bust_art_background (backyard)
    call process_character (sa, appearance="outfit bikini pose handsbehind face neutral blush false")
    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false")

    call process_character (sa, appearance="outfit bikini pose handsbehind face neutral blush false", text="Что ты собираешься делать дальше?")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face happy blush false", text="Я думаю, что я сделаю вращение в воздухе!")
    call process_character (sa, appearance="pose handface face happy blush false", text="О, вот это хорошая шутка!")
    call process_character (sa, appearance="pose handface face curious blush false", text="Что можно бы попробовать...")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="...{p}...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="([sa.say_name] выглядит мило в этом купальнике)")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="(Он меньше, чем я думал)")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="outfit swimsuit_hard pose behindhead face aroused blush false", text="...")
    call process_character (sa, appearance="pose handface face curious blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Я могу сделать ниндзя удар...")
    call process_character (sa, appearance="pose handface face curious blush false", text="Или, может быть, салют...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Что думаешь, [n.say_name]?")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="[n.say_name]?")
    call process_character (n, appearance="pose handsdown face aroused blush false", text="...{p}...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Земля говорит с [n.say_name], отвечайте [n.say_name]...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="А, что?")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Ха-ха, ты действительно уставился в космос!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="О чем ты только думал?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Ну, я просто хотел сказать...")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="...")
    call process_character (sa, appearance="pose handface face flirty blush false", text="Ох!")
    call process_character (sa, appearance="pose handface face flirty blush false", text="Теперь я вижу!")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Мне было интересно, почему ты отключился...")
    call process_character (sa, appearance="pose leaning face happy blush false", text="А потом я увидела, как твой член выпирает из плавок!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Трудно спрятать его, когда это происходит.")
    call process_character (sa, appearance="pose handface face happy blush false", text="Послушай!")
    call process_character (sa, appearance="pose handface face happy blush false", text="...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Ох, чувак!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="У меня есть просто, {w=1.0}сумасшедшая идея!")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="Сумасшедшая?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Так что выслушай меня.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Что если...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Мы попробуем потрахаться...")
    call process_character (sa, appearance="pose handface face happy blush false", text="В бассейне!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Бассейне?")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Это немного безумно, правда?")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Но я думаю, что было бы здорово попробовать!")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Как мы...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты знаешь...")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Было бы желание, а способ найдётся, [n.say_name]!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Разве мы бы уплывём друг от друга?")
    call process_character (sa, appearance="pose handface face curious blush false", text="В этом есть смысл...")
    call process_character (n, appearance="pose handsdown face neutral blush false")
    call process_character (sa, appearance="pose handface face curious blush false")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Мы можем попробовать двигать руками и ногами, чтобы оставаться на одном месте.")
    call process_character (sa, appearance="pose handface face curious blush false", text="Мы бы, наверное, очень быстро устали.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Да, я не фанат такого подхода.")
    call process_character (sa, appearance="pose handface face curious blush false", text="Хм...")
    call process_character (sa, appearance="pose handface face curious blush false", text="...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Я знаю!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Лестница в бассейне!")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Как насчет этого?")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Я могу держаться на лестнице, так что я остаюсь на месте.")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Тогда ты просто встанешь в позу!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Думаю, стоит попробовать.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Я запрыгну прямо сейчас!")

    call fade_to_black (1)

    call process_character (sa, appearance="pose leaning face neutral blush false", text="...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Окей, я хорошо ухватилась за лестницу.")

    python hide:
        play_music("audio/music/Summer Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg sam_scene_swimsuit_fuck_nude" if sam_scene_swimsuit_revisit_nude else "bg sam_scene_swimsuit_fuck")

    call process_character (sa, appearance="pose leaning face neutral blush false", text="Держись за меня покрепче!")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Вот так?")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Д-Да...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="(Он сжимает мою грудь)")
    call process_character (n, appearance="pose leaning face neutral blush false", text="...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Посмотрим, сработает ли это.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ах...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Твой член упирается в мою задницу.")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Я пытаюсь прицелиться, чтобы он попал в тебя...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Спустись немного ниже.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Еще немного...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Ох...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Я думаю, что он вошёл внутрь!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ммм!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Это так!")

    call static_still_ctc ("bg sam_scene_swimsuit_fuck_nude_blur" if sam_scene_swimsuit_revisit_nude else "bg sam_scene_swimsuit_fuck_blur")

    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ах!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ах!")
    call process_character (n, appearance="pose leaning face neutral blush false", text="{i}Вздох{/i}, {i}Вздох{/i}...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Убедись, что мы не уплывем.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Я держусь.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ахх!")
    call process_character (n, appearance="pose leaning face neutral blush false", text="...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="(Киска [sa.say_name] горячее, чем вода)")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ах, ты плещешься водой...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Это от того, что я поднимаюсь и опускаюсь.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="([n.say_name] сжимает сильнее)")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ммм...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Как ты думаешь, что твоя сперма будет делать, когда она попадёт в воду?")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Ах, ах...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Я не уверен...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Но я думаю, мы выясним!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Т-ты двигаешься быстрее!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ах, ах!")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Ммм!")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Ааах...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Я кончаю!")

    call static_still_ctc ("bg sam_scene_swimsuit_cum_nude_blur" if sam_scene_swimsuit_revisit_nude else "bg sam_scene_swimsuit_cum_blur")

    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ох!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Внутри меня так тепло!")

    call static_still_ctc ("bg sam_scene_swimsuit_cum_nude" if sam_scene_swimsuit_revisit_nude else "bg sam_scene_swimsuit_cum")

    call process_character (n, appearance="pose leaning face neutral blush false", text="...{p}...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="{i}Фух{/i}...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Я полностью выбился из сил.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Мои руки немного болят от того, что держатся за поручни.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Мне действительно нужно было за что-нибудь держаться, пока ты трахалась!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="В противном случае мы дрейфовали бы в бассейне.")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Ты отлично держалась.")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Мне было легче проникнуть внутрь тебя.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="[n.say_name], смотри!")
    call process_character (n, appearance="pose leaning face neutral blush false", text="...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Сперма плавает под нами!")
    call process_character (n, appearance="pose leaning face neutral blush false", text="...")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Я думал, она опустится на дно.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Это маленькие кусочки, плавают вокруг нас!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Так изящно!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Жаль, что я не взяла свои очки.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Тогда бы я могла увидеть твою сперму под водой.")
    call process_character (n, appearance="pose leaning face neutral blush false", text="...")

    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_had_incestual_situation", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_vaginal_sex", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_given_vaginal_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    $ scenes_completed.add("sam_scene_swimsuit_revisit_first_time_has_done_vaginal")

    call sam_scene_swimsuit_revisit_end
    return

label sam_scene_swimsuit_revisit_second_time_has_done_vaginal:
    $ sam_scene_swimsuit_revisit_nude = False

    $ no_bust_art = False
    call process_character (n, appearance="pose twohandfist face neutral blush false")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Я мигом!")

    call static_still_ctc ("bg sam_scene_swimsuit_fuck_nude" if sam_scene_swimsuit_revisit_nude else "bg sam_scene_swimsuit_fuck")

    call process_character (sa, appearance="", text="Хорошо, я вцепилась в поручень.")
    call process_character (sa, appearance="", text="Жду тебя!")

    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg sam_scene_swimsuit_fuck_nude_blur" if sam_scene_swimsuit_revisit_nude else "bg sam_scene_swimsuit_fuck_blur")

    call process_character (sa, appearance="", text="Ах, ах, ах!")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="([n.say_name] дышит мне на шею)")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="(Я думаю, что он должен работать усерднее, чтобы сделать это)")
    call process_character (sa, appearance="", text="(Должно быть, поэтому он истощается быстрее)")
    call process_character (sa, appearance="", text="(Но это интересно делать это во время плавания)")
    call process_character (sa, appearance="", text="(Это как будто мы левитируем, пока мы трахаемся!)")
    call process_character (n, appearance="", text="{i}Вздох{/i}...")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Я думаю, мы должны попробовать это на пляже, когда пойдём туда...)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Может быть сложнее с волнами, смывающими нас)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Сначала мы должны привыкнуть к этому в бассейне)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Может быть, мы научимся в конечном итоге плавать, трахаясь!)")
    call process_character (sa, appearance="", text="Мм, ах...")
    call process_character (sa, appearance="", text="Эй, [n.say_name].")
    call process_character (n, appearance="", text="Да?")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Ты хочешь сделать это без наших купальников?")
    call process_character (sa, appearance="", text="Я думаю, это будет весело.")

    menu:
        "Let's get naked!":
            $ sam_scene_swimsuit_revisit_nude = True
            call process_character (sa, appearance="", text="Здесь...")
            call process_character (sa, appearance="", text="Дай мне свои плавки, и я положу их на край бассейна.")

            call fade_to_black (1.0)
            call static_still_ctc ("bg sam_scene_swimsuit_fuck_nude_blur" if sam_scene_swimsuit_revisit_nude else "bg sam_scene_swimsuit_fuck_blur")
        "Let's just keep fucking.":
            call process_character (sa, appearance="", text="Меня это устраивает.")
            call process_character (sa, appearance="", text="Ахх.")
            call process_character (sa, appearance="", text="С тем же успехом можно было оставить в колее.")

    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Это заставляет меня хотеть использовать бассейн чаще.")
    call process_character (n, appearance="", text="Каждый раз, когда я иду плавать, я думаю о том, чтобы мы это сделали.")
    call process_character (sa, appearance="", text="Я-я чувствую то же самое.")
    call process_character (sa, appearance="", text="Даже глядя на бассейн из дома, это напоминает мне.")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!")
    $ quick_menu = True

    call process_character (n, appearance="", text="Ах...")
    call process_character (n, appearance="", text="Я собираюсь кончить, [sa.say_name]!")

    call static_still_ctc ("bg sam_scene_swimsuit_cum_nude_blur" if sam_scene_swimsuit_revisit_nude else "bg sam_scene_swimsuit_cum_blur")

    call process_character (n, appearance="", text="Хаах!")
    call process_character (sa, appearance="", text="Смотри, как брызжет!")

    call static_still_ctc ("bg sam_scene_swimsuit_cum_nude" if sam_scene_swimsuit_revisit_nude else "bg sam_scene_swimsuit_cum")

    call process_character (n, appearance="", text="{i}Вздох...{/i}")
    call process_character (n, appearance="", text="...")
    call process_character (sa, appearance="", text="Я вижу, как твоя сперма плавает между моих ног.")
    call process_character (n, appearance="", text="Д-Да...")
    call process_character (sa, appearance="", text="...")
    call process_character (sa, appearance="", text="Ты хотел выбраться или поплавать еще немного?")
    call process_character (n, appearance="", text="На твоё усмотрение...")

    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_had_incestual_situation", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_vaginal_sex", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_given_vaginal_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)


    $ scenes_completed.add("sam_scene_swimsuit_revisit_second_time_has_done_vaginal")
    $ sam_scene_swimsuit_revisit_nude = False
    call sam_scene_swimsuit_revisit_end
    return

label sam_scene_swimsuit_revisit_first_time_has_done_grinding:
    call process_scene_beginning (bg=backyard, char_tuple_array=[(sa, "outfit bikini pose handsbehind face happy blush false"), (n, "outfit swimsuit pose handsdown face neutral blush false")])

    call process_character (sa, appearance="outfit bikini pose handsbehind face happy blush false", text="Похоже, бассейн полностью наш!")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Практически всегда он в нашем распоряжении.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Да, но, [k.say_name] и мама сейчас не дома.")
    call process_character (sa, appearance="pose handface face happy blush false", text="Значит, остались только ты, я и бассейн!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Разве мама не любит присматривать за нами, когда мы здесь?")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Она сказала, что доверяет нам.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="И ей нравится, что мы плаваем вместе, для безопасности.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Как будто мы что-то делаем по-другому, когда ее нет рядом.")
    call process_character (sa, appearance="pose handface face curious blush false", text="...{p}...")
    call process_character (sa, appearance="pose handface face curious blush false", text="Хм...")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Ты о чем-то думаешь?")
    call process_character (sa, appearance="pose handface face curious blush false", text="...")
    call process_character (sa, appearance="pose handface face curious blush false", text="Я просто подумала...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Каково это-плавать в бассейне голышом!")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Г-голыми?")
    call process_character (sa, appearance="pose handface face curious blush false", text="Интересно, каково это плавать в бассейне голой.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="{cps=40}я не думаю, что это будет выглядеть иначе-{/cps}{w=0.75}{nw}")

    call character_leave_dissolve (sa)
    pause 0.5

    call process_character (sa, appearance="outfit nude pose handsbehind face neutral blush false", text="Мне слишком любопытно!")
    call process_character (sa, appearance="outfit nude pose handsbehind face neutral blush false", text="Я должна знать!")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="Что если мама придет домой и увидит тебя?")
    call process_character (sa, appearance="pose handface face happy blush false", text="Ну, тогда присмотри за мной!")
    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Знаешь, а здесь ничего!")

    call static_still_ctc ("bg sam_scene_swimsuit_jump_in_nude")

    call process_character (sa, appearance="pose leaning face neutral blush false", text="Яхуу!")
    "{i}Плюх{/i}"
    call process_character (sa, appearance="pose leaning face neutral blush false", text="...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="О, это такое приятное чувство!")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Да?")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Я хотела бы плавать так все время!")
    call process_character (n, appearance="pose leaning face neutral blush false", text="Чувствуешь себя по-другому?")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Да, я бы так сказала!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Это освежает!")

    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_seen_vagina", 1)

    $ scenes_completed.add("sam_scene_swimsuit_revisit_first_time_has_done_grinding")
    call sam_scene_swimsuit_revisit_end
    return

label sam_scene_swimsuit_revisit_second_time_has_done_grinding:
    $ no_bust_art = False
    call process_character (n, appearance="pose behindhead face neutral blush false")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Сегодня идеальная погода для купания!")

    call static_still_ctc ("bg sam_scene_swimsuit_jump_in_nude")

    call process_character (sa, appearance="", text="На этот раз ты присоединишься ко мне, [n.say_name]?")

    menu:
        "Heck yeah!":
            call add_boldness (1, tag="sam_scene_swimsuit_revisit_second_time_has_done_grinding_yea")
            call process_character (sa, appearance="", text="Это [n.say_name], которого я знаю!")
            call process_character (sa, appearance="", text="Тебе понравится, поверь мне!")
            call process_character (sa, appearance="", text="Ветерок поддувает очень приятый, когда прыгаешь в воду!")
            call process_character (sa, appearance="", text="Сними эти шорты и сделай решительный шаг!")
        "I'll just watch.":
            call process_character (sa, appearance="", text="На этот раз не получится?")
            call process_character (sa, appearance="", text="Если ты можешь раздеться на стриме [n.say_name], ты определенно можешь сделать и это!")

    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_seen_vagina", 1)

    $ scenes_completed.add("sam_scene_swimsuit_revisit_second_time_has_done_grinding")

    call sam_scene_swimsuit_revisit_end
    return

label sam_scene_swimsuit_revisit_first_time_normal:
    call process_scene_beginning (bg=backyard, char_tuple_array=[(sa, "outfit bikini pose handsbehind face neutral blush false"), (n, "outfit swimsuit pose handsdown face neutral blush false")])


    call process_character (sa, appearance="outfit bikini pose handsbehind face neutral blush false", text="Ах, это замечательный день!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Хорошая идея быть здесь.")
    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false", text="Да.")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Итак, каков твой план проникновения?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Мое что?")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Как ты собираешься войти в бассейн?")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Ох.")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Я буду заниматься этим делом...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Как я всегда это делаю?")
    call process_character (sa, appearance="pose handface face happy blush false", text="Ха-ха, это скучно, [n.say_name]!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Первый раз, когда ты входишь в бассейн в жаркий день, он должен быть более творческими!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Как войти в бассейн творчески?")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Существует множество способов!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Один из моих любимых стоять на краю...")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Закрыть глаза и упасть в воду спиной!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Это как, ты знаешь, что прыгаешь в бассейн...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Но ты не знаешь, когда ты ударишься о воду!")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Ты много думала об этом.")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Ох, вовсе нет!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Есть только одна цель, {w=1.0}, попасть в этот бассейн!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Фактически...")
    call process_character (sa, appearance="pose handface face happy blush false", text="Я собираюсь прыгнуть сейчас же!")

    call static_still_ctc ("bg sam_scene_swimsuit_jump_in")

    call process_character (sa, appearance="pose handface face happy blush false", text="Уууу!")
    call process_character (sa, appearance="pose handface face happy blush false", text="(Она как будто зависла в воздухе!)")
    call process_character (n, appearance="pose handface face happy blush false", text="(Она прыгнула очень далеко!)")
    "{i}Плюх{/i}"
    call process_character (sa, appearance="pose handface face happy blush false", text="...")
    call process_character (sa, appearance="pose handface face happy blush false", text="Ты видел площадь этого всплеска?")
    call process_character (sa, appearance="pose handface face happy blush false", text="Она была огромной!")
    call process_character (n, appearance="pose handface face happy blush false", text="Брызги даже до меня достали!")
    call process_character (sa, appearance="pose handface face happy blush false", text="Попробуй побить этот взрыв воды, [n.say_name]!")
    call process_character (sa, appearance="pose handface face happy blush false", text="Смотри, не утрать решимость.")
    call process_character (sa, appearance="pose handface face happy blush false", text="Просто вложи как можно больше энергии в свой прыжок и прыгай!")


    $ scenes_completed.add("sam_scene_swimsuit_revisit_first_time_normal")

    call sam_scene_swimsuit_revisit_end

    return

label sam_scene_swimsuit_revisit_second_time_normal:
    $ no_bust_art = False
    call process_character (n, appearance="pose twohandfist face neutral blush false")
    call process_character (sa, appearance="pose handface face happy blush false", text="Наперегонки со мной!")

    call static_still_ctc ("bg sam_scene_swimsuit_jump_in")

    call process_character (sa, appearance="", text="Я бегу так быстро, как могу...")
    call process_character (sa, appearance="", text="Прыгай!")
    call process_character (sa, appearance="", text="Попробуй, [n.say_name]!")
    call process_character (sa, appearance="", text="Ты полетишь, когда сделаешь это!")

    $ scenes_completed.add("sam_scene_swimsuit_revisit_second_time_normal")
    call sam_scene_swimsuit_revisit_end

    return

label sam_scene_swimsuit_revisit_end:

    call process_end_of_scene ("sam_scene_swimsuit_revisit", char=sa, force_no_boldness=True, reset_prompted_scene=False, force_not_replayable=True, revisit=True)
    return

image sam_dream_anim:
    "sam_dream_anim_0"
    pause 0.17
    "sam_dream_anim_1"
    pause 0.17
    "sam_dream_anim_2"
    pause 0.09
    "sam_dream_anim_3"
    pause 0.17
    "sam_dream_anim_4"
    pause 0.17
    "sam_dream_anim_5"
    pause 0.09
    repeat

label sam_dream_go_slow:
    $ main_animation_speed = sam_dream_slow_speed_multiplier
    jump sam_dream_switch_position_speed_dialog
    return

label sam_dream_go_normal:
    $ main_animation_speed = 1.0
    jump sam_dream_switch_position_speed_dialog
    return

label sam_dream_go_fast:
    $ main_animation_speed = sam_dream_fast_speed_multiplier
    jump sam_dream_switch_position_speed_dialog
    return

label sam_dream_go_blowjob:
    $ sam_scene_dream_position = "blowjob"
    jump sam_dream_switch_position_speed_dialog
    return

label sam_dream_go_vaginal:
    $ sam_scene_dream_position = "vaginal"
    jump sam_dream_switch_position_speed_dialog
    return

label sam_dream_go_anal:
    $ sam_scene_dream_position = "anal"
    jump sam_dream_switch_position_speed_dialog
    return

label sam_dream_switch_position_speed_dialog:
    hide screen sam_dream_speed_settings
    if sam_scene_dream_position == "blowjob":
        if main_animation_speed == sam_dream_slow_speed_multiplier:
            call process_character (n, text="Время замедляется, когда я это делаю!")
            call process_character (n, text="Это круто, как мы синхронны!")
        elif main_animation_speed == 1.0:
            call process_character (n, text="Ахх, и обратно отсасывать.")
            call process_character (n, text="Я должен сказать [sa.say_name] об этом сне!")
        else:
            call process_character (n, text="Я никогда не видел, чтобы [sa.say_name] сосала мне так в реальной жизни!")
            call process_character (n, text="Она сосала, как девушка на видео!")

    elif sam_scene_dream_position == "vaginal":
        if main_animation_speed == sam_dream_slow_speed_multiplier:
            call process_character (n, text="Интересно, что вызывает такой сон?")
            call process_character (n, text="Я надеюсь, что он мне ещё приснится!")
        elif main_animation_speed == 1.0:
            call process_character (n, text="Я никогда не был под ней раньше!")
            call process_character (n, text="Мы должны попробовать эту позу по-настоящему!")
        else:
            call process_character (n, text="Несмотря на то, что это сон, я всё ещё чувствую себя хорошо!")
            call process_character (n, text="Это практически то же самое!")
    else:
        if main_animation_speed == sam_dream_slow_speed_multiplier:
            call process_character (n, text="Они не говорят много, но это имеет смысл...")
            call process_character (n, text="Я могу управлять сном, как захочу!")
        elif main_animation_speed == 1.0:
            call process_character (n, text="Мой пенис больше во сне?")
            call process_character (n, text="Это почти похоже на...")
        else:
            call process_character (n, text="М-мой член скользит и так легко!")
            call process_character (n, text="Я могу двигаться так быстро, как хочу!")

    jump sam_scene_dream_segment_2
    return

label sam_scene_dream(dream=False):
    call sam_scene_dream_sex (dream=dream)
    return

label sam_scene_dream_sex(dream=False):
    $ renpy.start_predict("sam_dream_anim")
    call process_scene_beginning (bg="bg sam_room_evening", char_tuple_array=[ (n, ""), (sa, "outfit clothes pose handsbehind face neutral blush false") ], dream=dream, force_bg_change=True)

    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="[n.say_name]! [n.say_name]!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Что, что?")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Взгляни на это видео, которое я только что нашел!")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Эта девушка трахается с тремя чуваками!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Нет!")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Вот именно!")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="И все они заняли свои позы!")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Один трахает ее задницу, другой трахает ее киску...")
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="А другой засунул свой член ей в рот!")
    call process_character (n, appearance="pose handpocket face happy blush false", text="Это видео просто безумие!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Это безумие, верно?")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Но смотри, что происходит в конце!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Они остановились.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Теперь девушка становится на колени.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="Продолжай смотреть!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Она открывает свой рот и.....")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Ох-хохо!")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Безумие, не правда ли?")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Весь ее рот наполнен спермой!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="И она...")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="Она все проглотила?!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="Я смотрела эту часть снова и снова!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="В смысле, как она вообще это сделала?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Понятия не имею!")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Представь, если бы тебя было трое, [n.say_name]?")

    call process_character (n, appearance="pose handpocket face neutral blush false")

    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="Тогда мы сможем осуществить это!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ха, как если бы у меня были клоны или что?")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Или, если бы ты мог наложить заклинание зеркального изображения, как в некоторых играх, которые мы играем.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Но да!")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Просто представь себе всё, что мы могли бы попробовать!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Мы даже не выяснили, что мы можем сделать с одним мной.")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Хаха!")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Хорошая мысль!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Хотя об этом интересно подумать...")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Верно?")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Придумывать это очень весело!")
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="Я постоянно придумываю разные сценарии!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="pose handpocket face aroused blush false", text="{i}Зевок.{/i}..")
    call process_character (n, appearance="pose handpocket face aroused blush false", text="Да, было бы забавно наблюдать за этим.")
    call process_character (n, appearance="pose handpocket face aroused blush false", text="Но сейчас я хочу лечь спать.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Да, я тоже.")

    call process_character (n, appearance="pose handpocket face neutral blush false")

    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Мне нужно скачать это видео очень быстро.")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Я хочу поделиться им с чатом в следующий раз, когда мы будем стримить!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Звучит неплохо.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Спокойной ночи [sa.say_name]!")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Спокойной ночи [n.say_name]!")

    call process_scene_beginning (bg="bg nate_room_evening", dream=dream)

    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="(Я не знаю, как [sa.say_name] нашла эти видео...)")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="(Оно действительно что-то)")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="(Я все еще думаю о том, что она показала мне...)")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="...{p}...")
    call process_character (n, appearance="outfit underwear pose behindhead face aroused blush false", text="{i}Зевок.{/i}..")
    call process_character (n, appearance="outfit underwear pose handsdown face aroused blush false", text="(Я едва могу держать глаза открытыми!)")
    call process_character (n, appearance="outfit underwear pose handsdown face aroused blush false", text="(Время встретиться лицом к лицу с подушкой...)")

    call fade_to_black (1)

    call process_character (n, appearance="outfit underwear pose handsdown face aroused blush false", text="...{p}...")
    call process_character (n, appearance="outfit underwear pose handsdown face aroused blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face aroused blush false", text="Хрр...")

    show screen dream_blur
    show bg sam_dream_background
    with Dissolve(0.5)

    $ no_bust_art = False

    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...{p}...")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="(Снова здесь...)")

    call process_character (nate2, appearance="outfit underwear pose handsdown face neutral blush false position nate2_special")
    pause 0.5


    call process_character (n, appearance="outfit underwear pose handsdown face concerned blush false", text="(А?)")
    call process_character (n, appearance="outfit underwear pose handsdown face concerned blush false", text="(Это я?)")

    call process_character (nate3, appearance="outfit underwear pose handsdown face neutral blush false position nate3_special")
    pause 0.5

    call process_character (n, appearance="outfit underwear pose behindhead face embarrassed blush false", text="(Еще один?!)")


    call process_character (n, appearance="outfit underwear pose behindhead face embarrassed blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="(Подождите секунду...)")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face happy blush false", text="(Мне это снится!)")
    call process_character (n, appearance="outfit underwear pose handsdown face happy blush false", text="...")
    call process_character (n, appearance="outfit underwear pose twohandfist face happy blush false", text="(Если это мой сон, значит, я могу делать в ней все, что захочу!)")
    call process_character (n, appearance="outfit underwear pose handpocket face curious blush false", text="(Но как я могу это проверить?)")
    call process_character (n, appearance="outfit underwear pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handpocket face happy blush false", text="(Я думаю, что знаю, как это сделать...)")

    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="...")

    call process_character (nate2, appearance="outfit underwear pose behindhead face neutral blush false")
    call process_character (nate3, appearance="outfit underwear pose behindhead face neutral blush false")
    pause 0.5

    call process_character (n, appearance="outfit underwear pose handfist face neutral blush false", text="...")

    call process_character (nate2, appearance="outfit underwear pose handfist face neutral blush false")
    call process_character (nate3, appearance="outfit underwear pose handfist face neutral blush false")
    pause 0.5


    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="(Круто!)")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="(Если я думаю о чем-то, чтобы сделать, они делают!)")

    if not dream or persistent.disable_dream_music:
        $ play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call process_character (sa, appearance="outfit naked handsbehind naked face neutral blush false position sam_dream_special", text="Привет, [n.say_name]!")
    call process_character (sa, appearance="outfit naked handsbehind naked face neutral blush false", text="Я хочу сделать что-то!")

    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="Хм...")
    call process_character (n, appearance="outfit underwear pose behindhead face happy blush false", text="Я знаю, что мы можем сделать!")
    call process_character (n, appearance="outfit underwear pose behindhead face happy blush false", text="Помнишь то видео с девушкой?")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Да!")

    python hide:
        char_layer = character_layer()

        for clone_char in [n, nate2, nate3]:
            base_tag = clone_char.base_tag()
            face_tag = clone_char.face_tag()
            blush_tag = clone_char.blush_tag()
            
            renpy.hide(base_tag, char_layer)
            renpy.hide(face_tag, char_layer)
            renpy.hide(blush_tag, char_layer)

        renpy.with_statement(character_leave_dissolve_speed)

    pause 0.5

    call process_character (n, appearance="outfit nudehard pose twohandfist face happy blush false")
    call process_character (nate3, appearance="outfit nudehard pose handfist face neutral blush false position nate3_special")
    call process_character (nate2, appearance="outfit nudehard pose handfist face neutral blush false position nate2_special")
    call process_character (n, appearance="outfit nudehard pose twohandfist face happy blush false", text="Давай сделаем это!")

    call process_character (sa, appearance="pose leaning face happy blush false", text="Есть!")

    $ clear_characters()

    window hide
    $ play_sex_sounds = True
    $ set_main_animation_speed(1.0)
    show anim_nothing_image as main_animation at main_animation_transform(IA_Animation_Sam_Dream_Info(), xalign = 0.5, yalign = 0.5)
    with Dissolve(1.35)

    if not persistent.sfw_mode:
        show bg sam_dream_nonates
    else:
        show bg black

    $ renpy.pause(1.75)

    $ sam_scene_dream_position = "blowjob"
    $ no_bust_art = True

    call process_character (n, appearance="blush false", text="(Дааа!)")
    call process_character (n, appearance="blush false", text="(Это сработало!)")
    call process_character (n, appearance="blush false", text="(Я представил себе то же самое, что было в видео, и теперь это происходит!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="([sa.say_name] сосёт меня прямо сейчас...)")
    call process_character (n, appearance="blush false", text="(Бьюсь об заклад, я мог бы попробовать здесь каждую позу, чтобы узнать, как это чувствуется!)")
    call process_character (n, appearance="blush false", text="(Это самый крутой сон!)")

    window hide
    $ quick_menu = False
    show screen sam_dream_speed_settings
    $ renpy.pause(3.0)
    $ renpy.suspend_rollback(True)

    jump sam_scene_dream_segment_2

label sam_scene_dream_segment_2:
    window hide
    show screen sam_dream_speed_settings
    call screen progress_button_screen("Кончить!", yalign = 0.95)

    hide screen sam_dream_speed_settings
    $ set_main_animation_speed(sam_dream_fast_speed_multiplier)

    window hide
    $ set_main_animation_speed(sam_dream_fastest_speed_multiplier)
    $ renpy.pause(1.5)
    window hide
    hide main_animation
    with Dissolve(1.5)
    $ play_sex_sounds = False
    pause

    call process_character (sa, appearance="blush false", text="Ты собираешься кончить, [n.say_name]?")
    call process_character (sa, appearance="blush false", text="Кончи на меня!")

    call static_still_ctc ("bg sam_dream_nate1_appear")


    call static_still_ctc ("bg sam_dream_nate2_appear")


    call static_still_ctc ("bg sam_dream_nate3_appear")

    call process_character (n, appearance="blush false", text="Ах, я собираюсь сделать это, [sa.say_name]!")
    call process_character (n, appearance="blush false", text="Я собираюсь кончить!")
    call process_character (sa, appearance="blush false", text="Я готова!")
    call process_character (sa, appearance="blush false", text="Дерзай же!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg sam_dream_cumshot_nate1")

    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (sa, appearance="blush false", text="Есть один!")
    call process_character (sa, appearance="blush false", text="Да!")

    call static_still_ctc ("bg sam_dream_aftercum_nate1")

    call process_character (sa, appearance="blush false", text="Кто следующий?")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg sam_dream_cumshot_nate2")

    call process_character (n, appearance="blush false", text="Охх!")
    call process_character (sa, appearance="blush false", text="Они везде!")

    call static_still_ctc ("bg sam_dream_aftercum_nate2")

    call process_character (sa, appearance="blush false", text="Хорошо, последний!")
    call process_character (sa, appearance="blush false", text="Давай!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg sam_dream_cumshot_nate3")

    call process_character (n, appearance="blush false", text="Ааах!")
    call process_character (sa, appearance="blush false", text="Засунь его мне в рот!")
    call process_character (n, appearance="blush false", text="Ах, ах!")

    call static_still_ctc ("bg sam_dream_aftercum_nate3")

    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Уоу, лицо [sa.say_name] полностью покрыто!)")
    call process_character (sa, appearance="blush false", text="{i}Бульк{/i}...")
    call process_character (n, appearance="blush false", text="С-собираешься ли ты проглотить, [sa.say_name]?")
    call process_character (sa, appearance="blush false", text="...")

    call static_still_ctc ("bg sam_dream_cumshot_swallow")

    call process_character (sa, appearance="blush false", text="{i}Глык.{/i}..{p}{i}Глык{/i}...")
    call process_character (n, appearance="blush false", text="(Она действительно это делает!)")
    call process_character (n, appearance="blush false", text="([sa.say_name] проглатывает всё!)")

    call static_still_ctc ("bg sam_dream_cumshot_allgone")

    call process_character (n, appearance="blush false", text="Не могу поверить, что ты это сделала [sa.say_name]!")
    call process_character (n, appearance="blush false", text="Это было эпично!")
    call process_character (sa, appearance="blush false", text="...{p}...")

    call fade_to_black (1)

    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (n, appearance="blush false", text="...")

    call process_scene_beginning (bg="bg nate_room_daytime", dream=dream)
    $ nate_room.decide_and_play_daily_music_queue()

    call process_character (n, appearance="outfit underwear_hard pose handsdown face aroused blush false", text="{i}Зевок.{/i}..")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face aroused blush false", text="...")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face happy blush false", text="(Вау, этот сон был безумным!)")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face happy blush false", text="(У меня никогда не было такого раньше!)")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face happy blush false", text="...")
    call process_character (n, appearance="outfit underwear_hard pose twohandfist face neutral blush false", text="(Это было потрясающе, как я смог сделать всё это!)")
    call process_character (n, appearance="outfit underwear_hard pose twohandfist face neutral blush false", text="(Я должен сказать [sa.say_name] об этом, когда она встанет!)")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face neutral blush false", text="(Она получит удовольствие от этого...)")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face embarrassed blush false", text="(Сперма на моем нижнем белье?!)")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face embarrassed blush false", text="...{p}...")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face curious blush false", text="(Так вот почему он чувствовал себя так хорошо во сне...)")


    call process_scene_beginning (bg="bg sam_room_daytime", dream=dream)

    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (sa, "outfit clothes pose handsbehind face neutral blush false") ])

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Я должен рассказать тебе о сне, который мне приснился прошлой ночью...")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Был ли он хорошим?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="О, да!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="Детали, детали!")

    call fade_to_black (1)

    "{i}Я рассказал свой сон целиком [sa.say_name]...{/i}"

    call process_scene_beginning (bg="bg sam_room_daytime", dream=dream)

    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (sa, "outfit clothes pose handface face neutral blush false") ])

    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Блин!")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Тебе так повезло, [n.say_name]!")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Надеюсь, у меня тоже будет такой сон!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Это было очень весело.")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="И это было приятно!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Хотя, я кончил в трусы...")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Эх, небольшая цена, чтобы заплатить за то, как здорово это было!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Я серьезно хочу такой сон!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Да?")

    call process_character (sa, appearance="pose handface face neutral blush false", text="Я даже не знаю, с чего мне начать, если бы нас было по трое!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Что, если мы все будем сосать ртом твой член?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Или, может быть, может быть...")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Мы все по очереди будем сидеть на твоем члене!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Так много возможностей!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Я хочу попробовать все!")
    call process_character (sa, appearance="pose handface face happy blush false", text="Я использую все преимущества, если получу сон, подобный твоему, [n.say_name]!")


    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...")

    $ renpy.stop_predict("sam_dream_anim")


    call process_end_of_scene ("sam_scene_dream", char=sa, dream=dream )

    return