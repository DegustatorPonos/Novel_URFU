init python:
    def julia_vaginal_xray(xray_off_image, xray_on_image):
        store.julia_vaginal_xray_on = not store.julia_vaginal_xray_on
        bg_name = ""
        
        if store.julia_vaginal_xray_on:
            bg_name = xray_on_image
        else:
            bg_name = xray_off_image
        
        if persistent.sfw_mode:
            renpy.show_screen("sfw_mode_background_display", bg_name)
        else:
            renpy.show(bg_name, tag = "bg")
        
        return

screen julia_vaginal_xray(xray_off_image, xray_on_image, xalign=0.0, yalign=0.0):
    use main_menu_button(text="Рентген", action=Function(julia_vaginal_xray, xray_off_image, xray_on_image), xalign=xalign, yalign=yalign )

label julia_scene_underwear(dream=False):
    call julia_scene_underwear_sex (dream=dream)

    return

label julia_scene_underwear_sex(dream=False):
    call process_scene_beginning (bg="bg nate_room_evening", dream=dream )

    call process_character (n, appearance="outfit underwear pose behindhead face aroused blush false", text="{i}Уфф{/i}...")
    call process_character (n, appearance="outfit underwear pose behindhead face aroused blush false", text="(Отлично сходил в душ)")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="(Не знаю сколько ещё [julia.say_name] будет здесь жить)")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="(Но горячей воды на всех не хватает)")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="(Думаю я буду посмотрю смешные видео, прежде чем я-)")

    "{i}Тук-Тук-Тук{/i}"

    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="pose handsdown face curious blush false", text="Хмм?")
    call process_character (n, appearance="pose handsdown face curious blush false", text="Войдите?")
    call process_character (julia, appearance="outfit underwear pose handface face neutral blush false", text="Привет.")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="...")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="П-привет, [julia.say_name].")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="(Во что она сейчас одета?)")
    call process_character (julia, appearance="outfit underwear pose handup face neutral blush false", text="У тебя есть запасные подушки?")
    call process_character (julia, appearance="outfit underwear pose handface face neutral blush false", text="Мне нравится держать голову поднятой, когда я ... ..")
    call process_character (julia, appearance="outfit underwear pose handface face neutral blush false", text="...")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="(Я вижу насквозь её блузку)")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="(И её нижнее бельё очень маленькое...)")
    call process_character (julia, appearance="outfit underwear pose armcross face curious blush false", text="...")
    call process_character (julia, appearance="outfit underwear pose armcross face curious blush false", text="На что уставился, [n.say_name]?")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="О-ой!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Да, ничего...")
    call process_character (julia, appearance="outfit underwear pose armcross face neutral blush false", text="...")
    call process_character (julia, appearance="outfit underwear pose armcross face neutral blush false", text="Ну, что...")
    call process_character (julia, appearance="outfit underwear pose armcross face neutral blush false", text="...")
    call process_character (julia, appearance="outfit underwear pose handface face neutral blush false", text="Так у тебя есть запасная подушка или нет?")
    call process_character (n, appearance="pose handsdown face curious blush true", text="Д-Да, у меня есть одна.")
    call process_character (julia, appearance="outfit underwear pose handup face neutral blush false", text="...")
    call process_character (n, appearance="pose handsdown face curious blush true", text="Вот, держи.")

    call character_leave_dissolve (julia)
    pause 0.5

    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="(Должно быть, она увидела, что я пялился на неё)")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="(Я даже не понял, что так долго смотрел...)")

    call process_new_location (bg="bg hallway_evening", dream=dream )

    call process_character (julia, appearance="outfit underwear pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="(Он так пристально смотрел на моё нижнее бельё...)")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="(Не мог отвести взгляда от трусиков)")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="...")
    call process_character (julia, appearance="pose handup face curious blush false", text="(Как будто он никогда раньше не видел девушку в нижнем белье...)")
    call process_character (julia, appearance="pose handup face curious blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="(У него видимо не было опыта с противоположным полом)")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="(Не удивлюсь, если он весь день играет в видеоигры и мастурбирует...)")

    python:
        julia.revistable_scenes.add("julia_scene_underwear")

        if not dream:
            stats.add_stat("times_seen_panties", 1)
            stats.add_stat("times_seen_bra", 1)

    call process_end_of_scene ("julia_scene_underwear", char=julia, dream=dream)

    return

label julia_scene_topless(dream=False):
    call julia_scene_topless_sex (dream=dream)

    return

label julia_scene_topless_sex(dream=False):
    call process_scene_beginning (bg="bg backyard_daytime", dream=dream )

    call process_character (sa, appearance="position right", show_bust=False)
    call process_character (julia, appearance="position right", show_bust=False)
    call process_character (k, appearance="position right", show_bust=False)

    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Рада, что ты пришла сюда, [julia.say_name]!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Разве солнце не красивое?", replace=True)
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Ну пока я в основном в тени ...", replace=True)
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Привет, [sa.say_name]...", replace=True)
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="Хочешь, чтобы я сделала бомбочку?", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="О, да!", replace=True)
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="[julia.say_name]!", replace=True)
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Ты должна это увидеть!", replace=True)
    call process_character (julia, appearance="pose handup face neutral blush false", text="Мм...", replace=True)
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="Дай мне обратный отсчет [sa.say_name]!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Три...", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Два...", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Один...", replace=True)
    call process_character (julia, appearance="pose handface face curious blush false", text="К чему обратный отсчет?", replace=True)
    call process_character (julia, appearance="pose handface face curious blush false", text="{cps=40}Я занята чтением моей-{/cps}{w=0.75}{nw}", replace=True)
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="Бомбочка!!", replace=True)

    call character_leave_dissolve (k)
    $ renpy.pause(0.5)

    "{i}ВСПЛЕСК!{/i}"

    call process_character (julia, appearance="pose armcross face embarrassed blush false", text="Ахх!", replace=True)
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Оох!", replace=True)
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Я и не думала, что ты так близко к [julia.say_name]!", replace=True)
    call process_character (sa, appearance="pose leaning face happy blush false", text="Все брызги от бомбочки попали на тебя!", replace=True)
    call process_character (julia, appearance="pose armcross face neutral blush false", text="...", replace=True)
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Даа...", replace=True)

    call process_character (k, appearance="blush false", text="Немного воды никогда никому не повредит, [julia.say_name]!", show_bust=False)
    call process_character (k, appearance="blush false", text="Ты будешь жить!", show_bust=False)

    call process_character (sa, appearance="pose handface face neutral blush false", text="Давая я повешу твою футболку сохнуть на сушилку!", replace=True)
    call process_character (sa, appearance="pose handface face happy blush false", text="На этоё жаре она почти мгновенно высохнет!", replace=True)
    call process_character (julia, appearance="pose handup face curious blush false", text="А что я надену?", replace=True)
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Просто иди в мою комнату и бери запасную.", replace=True)
    call process_character (sa, appearance="pose leaning face neutral blush false", text="У нас с тобой почти один размер, поэтому мои футболки должны подойти!", replace=True)
    call process_character (julia, appearance="pose armcross face neutral blush false", text="...", replace=True)
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Хорошо...", replace=True)

    call process_new_location (bg="bg nate_room_daytime", dream=dream )
    $ reset_all_characters()

    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="(Хорошо, еще один обзор готов!)")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="([sa.say_name] это должно понравиться)")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="(Похоже, она вошла в свою комнату...)")

    call process_new_location (bg="bg sam_room_daytime", dream=dream )

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Background Groove.ogg", fadein = 1.0)

    call process_character (julia, appearance="outfit topless pose handface face curious blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handface face curious blush false", text="(Все эти рубашки настолько яркие...)")
    call process_character (julia, appearance="outfit topless pose handface face neutral blush false", text="(Отстой)")
    call process_character (julia, appearance="outfit topless pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose armcross face neutral blush false", text="{cps=40}(Даже нет ни темно-фиолетовой ни темно-синей,){/cps}{w=0.75}{nw}")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="[sa.say_name]!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="{cps=40}Ты должна взглянуть на этот обзор, я только что его на-{/cps}{w=0.75}{nw}")
    call process_character (julia, appearance="outfit topless pose armcross face angry blush true", text="Какого черта!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="[julia.say_name[0]]-[julia.say_name]?!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Почему ты в комнает [sa.say_name] без верха...")
    call process_character (julia, appearance="outfit topless pose handface face angry blush true", text="Убирайся отсюда, прямо сейчас!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Ахх!")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (julia, appearance="outfit topless pose handface face angry blush true", text="...")
    call process_character (julia, appearance="outfit topless pose handup face embarrassed blush true", text="(Он просто открыл дверь!)")
    call process_character (julia, appearance="outfit topless pose handup face embarrassed blush true", text="...")
    call process_character (julia, appearance="outfit topless pose armcross face angry blush true", text="(Кто, черт возьми, так делает?)")
    call process_character (julia, appearance="outfit topless pose armcross face angry blush true", text="(Его никто не учил уважать неприкосновенность частной жизни?!)")
    call process_character (julia, appearance="outfit topless pose armcross face angry blush true", text="...{p}...")
    call process_character (julia, appearance="outfit topless pose handface face neutral blush false", text="(Интересно, знал ли он, что я здесь...)")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(Не похоже, что он это знал, основываясь на его реакции)")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose armcross face angry blush false", text="(Надеюсь, он будет более осторожен, чтобы не врываться в чью-то комнату!)")

    call process_new_location (bg="bg hallway_daytime", dream=dream )

    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="...")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="([julia.say_name] была в бешенстве!)")
    call process_character (n, appearance="pose behindhead face curious blush false", text="(Но что она делала в комнате [sa.say_name]?)")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="(И почему была без верха?!)")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="...{p}...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="(Надеюсь, она понимает, что это был несчастный случай...)")

    python:
        julia.revistable_scenes.add("julia_scene_topless")

        if not dream:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_flat_breasts", 1)

    call process_end_of_scene ("julia_scene_topless", char=julia, dream=dream)

    return

label julia_scene_bottomless(dream=False):
    call julia_scene_bottomless_sex (dream=dream)

    return

label julia_scene_bottomless_sex(dream=False):
    call process_scene_beginning (bg="bg bathroom_evening", dream=dream )

    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face happy blush false", text="(Хорошо принять душ поздно ночью)")
    call process_character (julia, appearance="outfit clothes pose handup face happy blush false", text="(Меня никто не побеспокоит, и я могу быть здесь дольше...)")
    call process_character (julia, appearance="outfit clothes pose handup face happy blush false", text="...")

    call character_leave_dissolve (julia)
    pause 0.5

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Background Groove.ogg", fadein = 1.0)

    call process_character (julia, appearance="outfit bottomless pose handface face neutral blush false", text="(Этот душ отлично подходит для мытья волос)")
    call process_character (julia, appearance="outfit bottomless pose handup face neutral blush false", text="(А где полотенце?)")
    call process_character (julia, appearance="outfit bottomless pose handup face neutral blush false", text="...{p}...")
    call process_character (julia, appearance="outfit bottomless pose armcross face angry blush false", text="(Издеваетесь, что ли?)")
    call process_character (julia, appearance="outfit bottomless pose armcross face angry blush false", text="(Нет полотенец?)")
    call process_character (julia, appearance="outfit bottomless pose armcross face angry blush false", text="...")
    call process_character (julia, appearance="outfit bottomless pose handface face neutral blush false", text="(Это означает, что мне нужно взять из сушилки)")
    call process_character (julia, appearance="outfit bottomless pose handface face neutral blush false", text="{i}Вздох{/i}...")

    call process_new_location (bg="bg hallway_evening", dream=dream )

    call process_character (n, appearance="outfit underwear pose handsdown face aroused blush false", text="{i}Зевок{/i}.")
    call process_character (n, appearance="outfit underwear pose handsdown face aroused blush false", text="...")
    call process_character (n, appearance="outfit underwear pose behindhead face concerned blush false", text="(Во рту супер сухо!)")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="(Я думаю, что картофель был немного соленым...)")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="(Хорошо, что у нас есть целый ящик с бутылками для воды здесь)")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="{cps=40}(Таким образом, мне не нужно идти на кухню, чтобы-){/cps}{w=0.75}{nw}")


    call process_character (julia, appearance="outfit bottomless pose handface face embarrassed blush true", text="!!")
    call process_character (julia, appearance="outfit bottomless pose handface face embarrassed blush true", text="Что ты делаешь?!")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="Я... я пришёл за водой.")
    call process_character (julia, appearance="outfit bottomless pose armcross face embarrassed blush true", text="Как раз, когда я вышла из ванной?!")
    call process_character (n, appearance="outfit underwear pose handsdown face concerned blush false", text="Почему?")
    call process_character (n, appearance="outfit underwear pose handsdown face concerned blush false", text="Плохо, что я вышел в то же время, что и...")
    call process_character (n, appearance="outfit underwear pose behindhead face embarrassed blush true", text="!!")
    call process_character (julia, appearance="outfit bottomless pose handface face angry blush true", text="Не смей смотреть!")
    call process_character (julia, appearance="outfit bottomless pose handface face angry blush true", text="Смотри на моё лицо!")
    call process_character (n, appearance="outfit underwear pose behindhead face concerned blush true", text="...")
    call process_character (julia, appearance="outfit bottomless pose handup face angry blush true", text="На самом деле, почему бы тебе не развернуться?")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush true", text="...")
    call process_character (julia, appearance="outfit bottomless pose armcross face angry blush true", text="Чтобы я видела твой затылок через две секунды...")
    call process_character (n, appearance="outfit underwear pose behindhead face embarrassed blush true", text="{i}Глык!{/i}")

    call process_character (n, appearance="pose handsdown face concerned blush false position right_mirror")

    call process_character (n, appearance="pose handsdown face concerned blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush true", text="...")
    call process_character (julia, appearance="pose handface face neutral blush true", text="Хорошо.")
    call process_character (julia, appearance="pose handface face neutral blush true", text="Теперь вернись в свою комнату и подожди десять минут.")
    call process_character (julia, appearance="pose armcross face angry blush true", text="И не раньше!")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="...")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (julia, appearance="pose armcross face neutral blush false", text="...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="([n.say_name] всё время не вовремя!)")
    call process_character (julia, appearance="pose handface face neutral blush false", text="(В первый раз он увидел мою грудь, в комнате [sa.say_name]...)")
    call process_character (julia, appearance="pose handface face embarrassed blush false", text="(Теперь он мельком увидел мою писю!)")
    call process_character (julia, appearance="pose handface face embarrassed blush false", text="...{p}...")
    call process_character (julia, appearance="pose armcross face curious blush false", text="(Если бы я не знала его так хорошо, я бы сказала, что он делал это специально...)")
    call process_character (julia, appearance="pose armcross face curious blush false", text="...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="(Я знаю, на что способны мальчики...)")
    call process_character (julia, appearance="pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="([n.say_name] не похож на тип, который будет делать это)")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="(Но никогда не знаешь...)")

    call process_new_location (bg="bg nate_room_evening", dream=dream )
    $ reset_all_characters()

    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="(Я забыл, что [julia.say_name] поздно ходит в душ)")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear pose twohandfist face concerned blush false", text="(Но это не моя вина, что я вышел в то же время, что и она!)")
    call process_character (n, appearance="outfit underwear pose twohandfist face embarrassed blush false", text="(И почему она ходит без штанов или нижнего белья?!)")
    call process_character (n, appearance="outfit underwear pose twohandfist face embarrassed blush false", text="...{p}...")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="(Надо просто не забыть принести побольше воды в следующий раз...)")


    python:
        julia.revistable_scenes.add("julia_scene_bottomless")

        if not dream:
            stats.add_stat("times_seen_vagina", 1)

    call process_end_of_scene ("julia_scene_bottomless", char=julia, dream=dream)

    return

label julia_scene_nude(dream=False):
    call julia_scene_nude_sex (dream=dream)

    return

label julia_scene_nude_sex(dream=False):
    call process_scene_beginning (bg="bg bathroom_evening", dream=dream )

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Background Groove.ogg", fadein = 1.0)

    call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="...")
    call process_character (julia, appearance="outfit nude pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="outfit nude pose handface face neutral blush false", text="(У меня останется этот размер на всю жизнь?)")
    call process_character (julia, appearance="outfit nude pose handup face neutral blush false", text="(Они просто не хотят расти...)")
    call process_character (julia, appearance="outfit nude pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="(Я думаю, это лучше, чем гигантские)")
    call process_character (julia, appearance="outfit nude pose handup face neutral blush false", text="(У тети [si.say_name] сиськи огромные!)")
    call process_character (julia, appearance="outfit nude pose handup face concerned blush false", text="(Если бы мои сиськи были такого размера!")

    call process_new_location (bg="bg hallway_evening", dream=dream )

    call process_character (n, appearance="outfit underwear pose twohandfist face concerned blush false", text="...")
    call process_character (n, appearance="outfit underwear pose twohandfist face concerned blush false", text="(мне нужно, как можно скорее, в туалет!)")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="(Но, [julia.say_name] в ванной)")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="(Может быть, она там ненадолго)")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear pose twohandfist face concerned blush false", text="(Я не знаю, как долго я смогу продержаться!)")
    call process_character (n, appearance="outfit underwear pose twohandfist face concerned blush false", text="...{p}...")
    call process_character (n, appearance="outfit underwear pose behindhead face concerned blush false", text="(Похоже, она в душе)")
    call process_character (n, appearance="outfit underwear pose behindhead face concerned blush false", text="(Чёрт, она не узнает, если я это сделаю быстро!)")
    call process_character (n, appearance="outfit underwear pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="(Дверь открыта...)")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="(Я могу пройти...)")
    call process_character (n, appearance="outfit underwear pose behindhead face embarrassed blush false", text="(Но если [julia.say_name] увидит меня, я покойник!)")
    call process_character (n, appearance="outfit underwear pose behindhead face embarrassed blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="(Я мог бы закрыть глаза...)")
    call process_character (n, appearance="outfit underwear pose handsdown face concerned blush false", text="(Но тогда я не увижу, куда писаю!)")
    call process_character (n, appearance="outfit underwear pose handsdown face concerned blush false", text="...{p}...")
    call process_character (n, appearance="outfit underwear pose twohandfist face concerned blush false", text="(Я просто войду так быстро, как только смогу...)")
    call process_character (n, appearance="outfit underwear pose twohandfist face embarrassed blush false", text="(Я должен рискнуть!)")

    call process_new_location (bg="bg bathroom_evening", dream=dream )

    call process_character (n, appearance="outfit underwear pose behindhead face concerned blush false", text="(Хорошо, я готов!)")
    call process_character (n, appearance="outfit underwear pose behindhead face concerned blush false", text="...")

    call fade_to_black (1)

    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Аах...)")
    call process_character (n, appearance="blush false", text="...")

    call process_new_location (bg="bg bathroom_evening", dream=dream )

    call process_character (n, appearance="outfit underwear pose twohandfist face embarrassed blush false", text="(Вода перестала бежать!)")
    call process_character (n, appearance="pose twohandfist face concerned blush false", text="(Надо выбираться отсюда!)")


    call process_character (n, appearance="pose twohandfist face concerned blush false position right_mirror")

    call process_character (n, appearance="pose twohandfist face concerned blush false", text="...")


    call process_character (julia, appearance="outfit nude pose armcross face angry blush true", text="[n.say_name]!!")

    call process_character (n, appearance="pose twohandfist face embarrassed blush false position right")

    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="Агх!")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="Мне очень нужно было в туалет, [julia.say_name]!")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="Я хотел спросить тебя, могу ли я воспользоваться ванной!")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="{cps=40} Но ты была в душе и - {/cps}{w=0.75}{nw}")
    call process_character (julia, appearance="pose handface face angry blush true", text="Извращенец!")
    call process_character (julia, appearance="pose handface face angry blush true", text="Ты делаешь это специально!")
    call process_character (n, appearance="pose twohandfist face embarrassed blush true", text="Что? Нет!")
    call process_character (n, appearance="pose twohandfist face embarrassed blush true", text="Клянусь, нет!")
    call process_character (julia, appearance="pose armcross face angry blush false", text="Ты думаешь, что я поверю тебе?!")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face embarrassed blush true", text="Пожалуйста, поверь мне, [julia.say_name]!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Это был несчастный случай!")

    call process_character (julia, appearance="pose handup face angry blush false", text="Несчастный случай?")
    call process_character (julia, appearance="pose handup face angry blush false", text="Тогда скажи мне...")
    call process_character (julia, appearance="pose armcross face angry blush false", text="Почему ваш пенис стоит?!")
    call process_character (julia, appearance="pose armcross face angry blush false", text="Я вижу выпуклость!")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face concerned blush true", text="...{p}...")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face curious blush true", text="{cps=40} Я даже не знаю, как так получилось- {/cps}{w=0.75}{nw}")
    call process_character (julia, appearance="pose handface face angry blush false", text="Я поймала тебя с поличным, [n.say_name].")
    call process_character (julia, appearance="pose handface face angry blush false", text="Я раскусила тебя!")
    call process_character (n, appearance="outfit underwear_hard pose twohandfist face embarrassed blush true", text="!")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (julia, appearance="pose armcross face neutral blush true", text="...{p}...")
    call process_character (julia, appearance="pose handface face embarrassed blush false", text="(Он больной извращенец!)")
    call process_character (julia, appearance="pose armcross face embarrassed blush false", text="(Он один из тех кретинов, которые тайно любят пялиться на задницы и сиськи)")
    call process_character (julia, appearance="pose armcross face embarrassed blush false", text="...{p}...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="(Ему это не сойдет с рук!)")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="(Я лично позабочусь об этом...)")




    python:
        julia.revistable_scenes.add("julia_scene_nude")
        skip_jump = True
        if "julia_scene_nude" in scenes_completed or "simone_scene_1_seq_1" in scenes_completed:
            skip_jump = False


        if not dream:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_flat_breasts", 1)
            stats.add_stat("times_seen_vagina", 1)

    call process_end_of_scene ("julia_scene_nude", char=julia, dream=dream, do_not_jump=skip_jump)

    if skip_jump:
        call fade_to_black (1)
        "{i}На следующее утро...{/i}"
        call process_new_location (bg=bathroom, dream=dream, force_bg_change=True )
        call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="...{p}...")
        call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="(Я едва мог спать прошлой ночью)")
        call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="...")
        call process_character (n, appearance="outfit clothesjacket pose twohandfist face concerned blush false", text="(Я так беспокоился о том, что [julia.say_name] собирается делать...)")
        call process_character (n, appearance="outfit clothesjacket pose twohandfist face concerned blush false", text="...")
        call process_character (n, appearance="outfit clothesjacket pose behindhead face embarrassed blush false", text="(Я все еще беспокоюсь...)")
        call process_character (n, appearance="outfit clothesjacket pose behindhead face embarrassed blush false", text="(Она собирается рассказать обо мне?)")
        call process_character (n, appearance="outfit clothesjacket pose twohandfist face concerned blush false", text="(Что, если она меня побьет?!)")
        call process_character (n, appearance="outfit clothesjacket pose twohandfist face concerned blush false", text="...")
        call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...{p}...")
        call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="(Я все время думаю о голой [julia.say_name]...)")
        call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
        call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face aroused blush false", text="...")
        jump simone_scene_1_seq_1_sex

    return

label julia_scene_post_nude:
    call process_scene_beginning (nate_room)

    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Эй, я иду в магазин.")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Тебе что-то нужно?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Хм?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Ой...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Нет, не надо.")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Ты кажешься более странным, чем обычно.")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Что случилось?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Я думаю, [julia.say_name] меня ненавидит.")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Ненавидит тебя?")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Почему ты так думаешь?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Прошлой ночью я...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Мне очень хотелось в туалет.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Но [julia.say_name] была в душе.")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="И ты вошёл, пока она все еще была в душе?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Д-да, как ты узнала?")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="Я слышала, что [julia.say_name] кричит на тебя.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Ой...")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Я знаю, ты не хотел мочиться в штаны...")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Но это был не самый умный шаг, чтобы пойти в ванную без приглашения.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Я знаю...")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Итак, что ты собираешься делать?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="{cps=40} Я просто оставлю в покое ее до конца лета и- {/cps}{w=0.75}{nw}")
    call process_character (k, appearance="outfit clothes pose armcross face concerned blush false", text="Нет, [n.say_name] прослушай...")
    call process_character (k, appearance="outfit clothes pose armcross face concerned blush false", text="Я знаю, что ты беспокоишься о том, что случилось, и тебе плохо.")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Но убегать каждый раз, когда ты её видишь, не заставит тебя чувствовать себя лучше.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Я просто извинюсь перед ней.")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Скажи, что тебе очень жаль, что ты это сделал.")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face concerned blush false", text="Но я не думаю, что это сработает!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face concerned blush false", text="Она думает, что я извращенец!")

    if "kira_scene_2_seq_2" in scenes_completed:
        call process_character (k, appearance="pose armsup face happy blush false", text="Ну, она не ошибается в этом, хе-хе...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (k, appearance="pose armcross face neutral blush false", text="Но разница в том, что она не хочет, чтобы ты видел её обнаженной.")
        call process_character (k, appearance="pose armcross face happy blush false", text="Лучше я буду трясти своей задницей, чтобы ты смотрел на ней!")
        call process_character (n, appearance="pose behindhead face curious blush true", text="...")
        call process_character (k, appearance="pose handhip face neutral blush false", text="Я просто честно скажу, что ты не собирался шпионить за ней.")
        call process_character (k, appearance="pose handhip face neutral blush false", text="Всё просто.")
    else:
        call process_character (k, appearance="pose handhip face neutral blush false", text="Потом я скажу, что ты не извращенец.")
        call process_character (k, appearance="pose handhip face neutral blush false", text="Всё просто.")

    call process_character (n, appearance="pose handpocket face curious blush false", text="Это не может быть так просто...")
    call process_character (k, appearance="pose armcross face neutral blush false", text="Если думаешь, что этого будет недостаточно, попробуй предложить ей помощь")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Или купи ей книгу, которую она любит, и вложи письмо с извинениями.")
    call process_character (k, appearance="pose handhip face neutral blush false", text="Мы все делаем ошибки.")
    call process_character (k, appearance="pose handhip face neutral blush false", text="[julia.say_name] знает это.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Может быть.")
    call process_character (k, appearance="pose armcross face neutral blush false", text="Поверь мне, [n.say_name], тебе станет лучше, если ты поговоришь с ней.")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Во всяком случае, я должна бежать.")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Но просто поговори с ней, хорошо?")
    call process_character (k, appearance="pose handhip face neutral blush false", text="Сейчас она внизу.")
    call process_character (k, appearance="pose handhip face happy blush false", text="Намёк, намёк.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Х-хорошо.")

    call character_leave_dissolve (k)
    pause 0.5

    call process_character (n, appearance="pose handpocket face curious blush false", text="...")

    call process_new_location (living_room)

    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false")

    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Привет, [julia.say_name].")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...{p}...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Я хотел извиниться за случившееся.")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face concerned blush false", text="Я не должен был уходить в ванную, пока ты принимала душ.")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face concerned blush false", text="Я должен был дождаться, когда ты закончишь, прежде чем заходить.")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Мне жаль, что я сделал это, и я обещаю, что больше не буду.")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="...{p}...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="И... Если хочешь, я могу сделать для тебя все.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Я могу купить новую книгу.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Или, может быть, если ты хочешь, чтобы я постирал твою одежду.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Я сделаю все, что хочешь.")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face concerned blush false", text="Я просто не хочу, чтобы ты злилась на меня!")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...{p}...")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Ты сказал, что сделаешь, что угодно для меня?")
    call process_character (n, appearance="outfit clothesjacket pose handfist face concerned blush false", text="Да!")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Похоже, ты хочешь принести извинения.")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Я ещё подумаю, что тебе сделать бы такого.")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Л-ладно, звучит отлично!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face curious blush false", text="(Надеюсь, что извинения сработали...)")

    call process_character (julia, appearance="pose handface face neutral blush false", text="(Похоже, [n.say_name] решил послужить мне)")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose handface face happy blush false", text="(Это будет интересно...)")

    call process_end_of_scene ("julia_scene_post_nude", char=julia, force_not_replayable=True, force_no_boldness=True)

    return

label julia_scene_footjob:
    $ display_multiple_characters([ (n, ""), (julia, "pose handup face neutral") ])
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="[n.say_name], я знаю, что ты можешь сделать для меня.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Д-да?")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="У тебя есть время обговорить это?")

    call prompt_menu_boldness_check ("К-конечно...", "Не думаю, что смогу прямо сейчас...", "julia_scene_footjob", julia)

    return

label julia_scene_footjob_refusal(text, insufficient_points):
    call process_character (n, appearance="pose behindhead face concerned", text=text)
    call process_character (n, appearance="pose behindhead face concerned", text="(О чём она собирается спросить?)")
    call process_character (n, appearance="pose behindhead face concerned", text="(Может быть, когда я буду чувствовать себя лучше, я спрошу, о чем она хотела поговорить...)")
    call process_character (julia, appearance="pose armcross face neutral", text="Ты не передумал?")
    call prompt_refusal_end (julia)
    return

label julia_scene_footjob_sex(dream=False):
    call process_scene_beginning (nate_room, char_tuple_array=[ (n, "outfit clothesjacket pose handpocket face curious"), (julia, "outfit clothes pose handup face neutral") ], dream=dream )

    call process_character (julia, appearance="pose handup face neutral blush false", text="Хорошо, [n.say_name]...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Я долго думала о том, что ты сказал.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Что ты сделаешь все для меня в качестве извинения.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Д-да...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Кажется, тебе нравится быть извращенцем.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Но пока я рядом, это извращение будет регулироваться.")
    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Поэтому я думаю, что это будет...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Ты будешь моим сексуальным слугой на лето.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="К-какой слуга?")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Секс-слуга.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Каждый раз, когда я прошу тебя заняться сексом, ты будешь подчиняться.")
    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="В-в течение всего лета?")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Да, пока я здесь.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Если ты, конечно, не думаешь, что лучше, если я скажу твоей маме о том, что произошло в ванной...")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="Н-нет, все в порядке!")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Значит, ты согласился?")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Ты станешь моим личным секс-слугой?")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Д-да.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Скажи это громче, [n.say_name]!")
    call process_character (n, appearance="pose twohandfist face concerned blush false", text="Да!")
    call process_character (n, appearance="pose twohandfist face concerned blush false", text="Я буду твоим секс-слугой!")
    call process_character (julia, appearance="pose armcross face happy blush false", text="Это то, что мне нравится слышать.")
    call process_character (julia, appearance="pose armcross face happy blush false", text="...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Разденься.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Т-ты хочешь видеть меня голым?")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Верно.")
    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="pose handsdown face curious blush false", text="Х-хорошо.")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadein = 1.0)

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Как ты себя чувствуешь?")
    call process_character (n, appearance="outfit nudesoft pose handsdown face concerned blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Нервничаешь?")
    call process_character (n, appearance="outfit nudesoft pose behindhead face concerned blush false", text="Д-да...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Тебе неуютно, что я смотрю на твой пенис?")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Тебе понравилось смотреть на меня голой, не так ли?")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="У тебя привстал, когда ты увидел меня.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Не отрицай этого.")
    call process_character (n, appearance="outfit nudesoft pose behindhead face concerned blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Ты мастурбировал раньше?")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Это, когда ты трогаешь и трёшь свой член, чтобы почувствовать себя хорошо?")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Д-да, я делал это раньше...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Тебе нравится это чувство?")
    call process_character (n, appearance="outfit nudesoft pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose behindhead face concerned blush false", text="Ага...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Ну, я собираюсь тебе мастурбировать.")
    call process_character (n, appearance="outfit nudesoft pose handsdown face curious blush false", text="Т-ты?")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Моими ногами.")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Ногами?")
    call process_character (julia, appearance="pose handup face angry blush false", text="Без вопросов, [n.say_name]!")
    call process_character (julia, appearance="pose handup face angry blush false", text="Помни, ты мой послушный секс-слуга.")
    call process_character (n, appearance="outfit nudesoft pose behindhead face embarrassed blush false", text="...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="pose handface face happy blush false", text="(Это весело)")
    call process_character (julia, appearance="pose handface face happy blush false", text="(Гораздо веселее, чем я ожидала)")
    call process_character (julia, appearance="pose handface face happy blush false", text="...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Итак...")

    call character_leave_dissolve (julia)
    pause 0.5


    call process_character (julia, appearance="outfit topless pose handup face neutral blush false")

    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush true", text="!")
    call process_character (julia, appearance="outfit topless pose handface face neutral blush false", text="Какие-то проблемы, [n.say_name]?")
    call process_character (n, appearance="outfit nudesoft pose behindhead face embarrassed blush true", text="Т-ты тоже будешь голой?")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Я не хочу, чтобы моя одежда замаралась.")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush true", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Ложись на кровать.")

    call fade_to_black (1)

    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Позволь мне сесть позади тебя.")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Хм?")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="{cps=40} (Что она -) {/cps}{w=0.75}{nw}")

    call static_still_ctc ("bg julia_footjob_soft")

    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Ах!")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Хм...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Не очень-то и впечатляет.")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(Похоже, что-то происходит...)")

    call static_still_ctc ("bg julia_footjob_hardforeskin_noblur")

    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Вот это другое дело.")
    call process_character (n, text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(Он впечатляюще твёрд)")

    call static_still_ctc ("bg julia_footjob_hardforeskin_blur")

    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Ах, ах!")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(У него очень чувствительный член)")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(Хорошо...)")

    if "simone_scene_garden_handjob" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Обычно мама касается его руками...)")
        call process_character (n, appearance="blush false", text="Ха, ах!")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Но это так же хорошо!)")
    else:
        call process_character (n, appearance="blush false", text="Ха, ах!")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Трение очень приятное!)")


    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Ахх!")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(Я никогда не видела раньше пениса, как у него)")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(У него много кожи, покрывающей его головку)")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(Она кажется такой мягкой в моих пальцах ног)")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Тебе нравится это, [n.say_name]?")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Ах!")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Д-да.")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Ну, я только начала.")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Я собираюсь оттянуть твою кожу...")

    call static_still_ctc ("bg julia_footjob_hard_blur")

    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Ммм!")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(Я удивлена, что [n.say_name] согласился с этим)")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(Интересно, он понимал, что его ждёт, когда говорил, что сделает всё что угодно...)")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(У него член лучше, чем я думала)")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(А лето-то, возможно, и не будет скучным...)")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Ахх, ах, ах!")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="([n.say_name] довольно покорен)")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(Он позволяет мне играть со своим членом так, как я хочу)")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Ох, ах...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Ты уже скоро, [n.say_name]?")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Мм, ах!")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Я хочу видеть, как много ты кончишь!")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Ах, ах...")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Ммм!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg julia_footjobcum_hard_blur")

    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Aa!")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(Неплохо)")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="(Совсем неплохо...)")

    call static_still_ctc ("bg julia_footjobaftercum_hard_noblur")

    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Ну ну...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Я вижу, как много спермы.")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Я... я никогда бы не подумал, что ты сделаешь это...")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Г-где ты научилась так использовать свои ноги?")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="За последние годы я выучила несколько трюков.")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Т-ты покажешь еще некоторые из них?")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Возможно, в свое время.")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="Но сначала, почему бы тебе не почистить эти чулки?")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Твои чулки?")
    call process_character (julia, appearance="outfit topless pose handup face neutral blush false", text="И их нужно мыть руками...")

    python:
        julia.revistable_scenes.add("julia_scene_footjob_revisit")

        if not dream:
            stats.add_stat("times_received_footjob", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene ("julia_scene_footjob", char=julia, dream=dream)

    return

label julia_scene_footjob_revisit:
    if "julia_scene_footjob_revisit" not in scenes_completed:
        jump julia_scene_footjob_revisit_1st_time
    else:
        jump julia_scene_footjob_revisit_2nd_time

    return



label julia_scene_footjob_revisit_1st_time:
    $ no_bust_art = False
    $ display_multiple_characters([ (n, "pose behindhead face neutral"), (julia, "pose armcross face curious blush false") ])

    call process_character (julia, appearance="pose armcross face curious blush false", text="Что?")
    call process_character (n, appearance="pose handpocket face curious blush false")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Если хочешь, чтобы я это делала, ты должен попросить меня должным образом...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="\"[julia.say_name], ты сделаешь мне футджоб?\"")
    call process_character (n, appearance="pose behindhead face curious blush false", text="И-извини...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="[julia.say_name], ты сделаешь мне футджоб?")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Думаю, что я могу, конечно...")

    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadein = 1.0)

    call static_still_ctc ("bg julia_footjob_hardforeskin_blur")

    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ах, ах!")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (n, text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Т-тебе нравится это, [julia.say_name]?")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Я бы этого не делала, если бы не хотела.")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Я хочу тратить своё время на то, что мне нравится.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ахх...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Логично.")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Ну а мне, я надеюсь, не нужно спрашивать, нравится ли это тебе.")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="У тебя есть простой индикатор...")

    call static_still_ctc ("bg julia_footjob_hard_blur")

    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ах, Ммм!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="(Я не знал, что и ожидать от работы секс-слуги)")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="(Но если это так...)")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="(Думаю, мне это очень понравится!)")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="(Я этого не ожидал, но...)")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="([n.say_name], просто отличная игрушка в моих руках)")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="(Он даже захотел, чтобы я снова сделала это с ним)")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="(Я думаю [n.say_name] нравится это больше, чем кажется на первый взгляд...)")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ах.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ах, да...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Ты наслаждаешься этим больше, чем другие мальчики, с которыми я это делала.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты это делала с другими мальчиками?")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Ты думаешь я каким-то магическим образом узнала, как делать футджоб без практики, [n.say_name].")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ахх, ах!")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Я много практиковалась.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Гах, ах...")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg julia_footjobcum_hard_blur")

    call process_character (n, appearance="pose behindhead face neutral blush false", text="Хннг!")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Целый вулкан извергся из твоего члена.")

    call static_still_ctc ("bg julia_footjobaftercum_hard_noblur")

    call process_character (n, appearance="pose behindhead face neutral blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Ты не разочаровал меня своим оргазмом...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Но в следующий раз тебе нужно продержаться дольше!")

    jump julia_scene_footjob_revisit_end

    return

label julia_scene_footjob_revisit_2nd_time:
    $ no_bust_art = False
    $ display_multiple_characters([ (n, "pose behindhead neutral"), (julia, "pose armcross face happy blush false") ])

    call process_character (julia, appearance="pose armcross face happy blush false", text="Я в настроении для ещё одного раза, да...")

    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadein = 1.0)

    call static_still_ctc ("bg julia_footjob_hard_blur")

    call process_character (n, appearance="blush false", text="Ах...")
    call process_character (n, appearance="blush false", text="Ой...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Интересно, сколько парней было у [julia.say_name]?)")
    call process_character (n, appearance="blush false", text="(У меня никогда не было девушки!)")
    call process_character (n, appearance="blush false", text="...")

    if stats.stat_value("times_had_sex") > 0:
        call process_character (n, appearance="blush false", text="(Насколько я знаю, так или иначе...)")
        call process_character (n, appearance="blush false", text="...")

    call process_character (n, appearance="blush false", text="(Я рад, что [julia.say_name] больше не сердится на меня)")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="(Мне кажется, ей нравится возбуждать мой пенис!)")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="(Я скажу одно о [n.say_name]...)")
    call process_character (julia, appearance="pose handface face neutral blush false", text="(У него нет проблем поднять свой член для меня)")
    call process_character (julia, appearance="pose handface face neutral blush false", text="(Это замечательно)")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="(Некоторые из моих предыдущих бойфрендов были как обмякшая макаронина)")
    call process_character (julia, appearance="pose handface face neutral blush false", text="(Как освежает увидеть парня с активным членом)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", yalign = 0.2)
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg julia_footjobcum_hard_blur")

    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (n, appearance="blush false", text="...")

    call static_still_ctc ("bg julia_footjobaftercum_hard_noblur")

    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="(Я чувствую много спермы между моими пальцами...)")

    jump julia_scene_footjob_revisit_end
    return

label julia_scene_footjob_revisit_end:
    python:
        stats.add_stat("times_received_footjob", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene ("julia_scene_footjob_revisit", char=julia, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label julia_scene_blowjob(dream=False):
    call julia_scene_blowjob_sex (dream=dream)

    return

label julia_scene_blowjob_sex(dream=False):
    call process_scene_beginning (nate_room, char_tuple_array=[ (n, "outfit clothesjacket "), (julia, "outfit clothes pose handup face neutral blush false") ], dream=dream, force_bg_change=True )

    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="[n.say_name]...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Ох, [julia.say_name]!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Ты пришла, чтобы сделать мне еще один футджоб?")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Я думаю, мы оба знаем, что ты можешь справиться с большим, чем это [n.say_name].")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Большим чем это?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Что ты имеешь в виду?")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Я начала с футджоба, чтобы посмотреть, как ты справишься с этим.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="И я справился?")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Ты хорошо продержался.")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="И я не могу отрицать, что ты хорошо кончаешь.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face embarrassed blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Но теперь я собираюсь ввести себя погрубее.")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Если ты продолжишь оставаться моим сексуальным слугой, тебе нужно стать более агрессивным.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="А-агрессивным?")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Иначе говоря...")

    call fade_to_black (1)

    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="В-вау!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Уф!")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Сними одежду.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...{p}...")
    call process_character (julia, text="Теперь стой там, пока я работаю над тобой.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="(Работаешь надо мной?)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="(Что она имеет в виду?)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...")

    "{i}Вжик!{/i}"

    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="[julia.say_name[0]]-[julia.say_name]!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="{cps=40}Ч-то ты-{/cps}{w=0.75}{nw}")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

    call static_still_ctc ("bg julia_blowjob_table")

    call process_character (n, appearance="blush false", text="Aах!")
    call process_character (n, appearance="blush false", text="Вау!")
    call process_character (n, appearance="blush false", text="(Она положила весь мой член в рот!)")

    if stats.stat_value('times_received_blowjob') > 0:
        call process_character (n, appearance="blush false", text="(Мне никогда так не сосали!)")
        if "kira_scene_tip_blowjob" in scenes_completed:
            call process_character (n, appearance="blush false", text="(За исключением, может быть, [k.say_name]...)")
    else:
        call process_character (n, appearance="blush false", text="(Это действительно возбуждает меня!)")
        call process_character (n, appearance="blush false", text="(Так сильно!)")




    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="([n.say_name], не был готов к минету...)")
    call process_character (julia, appearance="blush false", text="(Но именно по этой причине я это и делаю)")
    call process_character (julia, appearance="blush false", text="(Он не соответствует моим стандартам пока)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Но он туда доберется...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="[julia.say_name[0]]-[julia.say_name]...")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="Т-ты не предупредила.")
    call process_character (julia, appearance="blush false", text="Не нужно.")
    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (n, appearance="blush false", text="Н-но как я должен быть более агрессивным от этого?")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Ты учишься на примере.")
    call process_character (n, appearance="blush false", text="А?")
    call process_character (n, appearance="blush false", text="Ах...")
    call process_character (julia, appearance="blush false", text="Когда дело доходит до меня и секса...")
    call process_character (julia, appearance="blush false", text="Я предпочитаю пропустить прелюдию.")
    call process_character (julia, appearance="blush false", text="Чем скорее удовольствие, тем лучше.")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (julia, appearance="blush false", text="Ты понимаешь это, я надеюсь?")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я-я понимаю.")
    call process_character (julia, appearance="blush false", text="Вот смотри, как я сразу начала сосать твой член.")
    call process_character (julia, appearance="blush false", text="Я просто схватила его и сунула себе в горло.")
    call process_character (n, appearance="blush false", text="Д-да...")
    call process_character (julia, appearance="blush false", text="Это тип агрессивного поведения, который я жду от тебя, [n.say_name].")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Теперь позволь мне закончить то, что я начала.")
    call process_character (n, appearance="blush false", text="А! Ах!")
    call process_character (julia, appearance="blush false", text="Мм, Ммф!")
    call process_character (n, appearance="blush false", text="(Ее губы давят и тянут мой пенис!)")
    call process_character (n, appearance="blush false", text="(Она не останавливается!)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Я ожидаю, что он будет готов кончить прямо...)")
    call process_character (n, appearance="blush false", text="Ах, ах!")

    call static_still_ctc ("bg julia_blowjob_nocum")

    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Я жду, [n.say_name]...")
    call process_character (julia, appearance="blush false", text="Где твоя сперма?")
    call process_character (n, appearance="blush false", text="Я... я сейчас...")
    call process_character (n, appearance="blush false", text="Ааа...")

    call static_still_ctc ("bg julia_blowjob_almostcum")
    call process_character (n, appearance="blush false", text="[julia.say_name[0]]-[julia.say_name]!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg julia_blowjob_cum")

    call process_character (n, appearance="blush false", text="Aa!")
    call process_character (julia, appearance="blush false", text="Вот оно!")
    call process_character (julia, appearance="blush false", text="Положись полностью на меня!")
    call process_character (n, appearance="blush false", text="Мм! Ах, ах...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")

    call static_still_ctc ("bg julia_blowjob_swallowcum")

    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="{i}Глык.{/i}..{p}{i}Глык.{/i}..")

    call static_still_ctc ("bg julia_blowjob_almostcum")

    call process_character (julia, appearance="blush false", text="Ааа...")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Я много лет оттачивала мой минет.")
    call process_character (julia, appearance="blush false", text="Я точно знала, когда ты собираешься кончить.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ты?")
    call process_character (n, appearance="blush false", text="Как?")
    call process_character (julia, appearance="blush false", text="Эти входит в привычку...")
    call process_character (julia, appearance="blush false", text="Но тебе надо ещё многое наверстать!")
    call process_character (julia, appearance="blush false", text="Я хочу, чтобы ты узнал, как можно больше до конца лета!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я... я сделаю все возможное.")
    call process_character (julia, appearance="blush false", text="Тебе придётся, если хочешь удовлетворить меня...")

    $ heard_of_blowjob = True


    python:
        julia.revistable_scenes.add("julia_scene_blowjob_revisit")

        if not dream:
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_cummed_in_mouth", 1)
            stats.add_stat("times_received_blowjob", 1)

    call process_end_of_scene ("julia_scene_blowjob", char=julia, dream=dream)

    return

label julia_scene_blowjob_revisit:
    if "julia_scene_blowjob_revisit" not in scenes_completed:
        jump julia_scene_blowjob_revisit_1st_time
    else:
        jump julia_scene_blowjob_revisit_2nd_time

    return



label julia_scene_blowjob_revisit_1st_time:
    $ no_bust_art = False
    $ display_multiple_characters([ (n, "pose behindhead face neutral"), (julia, "pose handface face neutral blush false") ])

    call process_character (julia, appearance="pose handface face neutral blush false", text="Ну да, я могла бы пососать твой член, так как я делала это раньше...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Я думаю, что ты хочешь сказать «ты пососёшь мой член?»")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Просто поработай над своей грамматикой в ​​следующий раз, когда попросишь..")

    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

    call static_still_ctc ("bg julia_blowjob_table")

    call process_character (n, appearance="blush false", text="Ох, ох!")
    call process_character (julia, appearance="blush false", text="У тебя никогда не было минета, не так ли?")

    if "kira_scene_tip_blowjob" in scenes_completed or "simone_scene_blowjob" in scenes_completed or "sam_scene_blowjob" in scenes_completed or "gloryhole_scene_blowjob" in scenes_completed:
        call process_character (n, appearance="blush false", text="На самом деле, ах...")
        call process_character (n, appearance="blush false", text="Был.")
        call process_character (julia, appearance="blush false", text="Бред сивой кобылы.")
        call process_character (n, appearance="blush false", text="Ч-честно!")
        call process_character (julia, appearance="blush false", text="В любом случае, мне все равно.")
        call process_character (julia, appearance="blush false", text="Мои минеты превосходят все.")
    else:
        call process_character (n, appearance="blush false", text="Т-только ты, ах, {w=0.5} дала мне один.")
        call process_character (julia, appearance="blush false", text="Ты предпочтешь мой, потому что он лучше, чем любой другой.")

    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="[julia.say_name[0]]-[julia.say_name]?")
    call process_character (julia, appearance="blush false", text="Что?")
    call process_character (n, appearance="blush false", text="Мне кажется, что ты ведёшь себя иначе, когда мы делаем такие штуки.")
    call process_character (julia, appearance="blush false", text="Иначе?")
    call process_character (julia, appearance="blush false", text="Как?")
    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (n, appearance="blush false", text="О-обычно ты довольно спокойна дома.")
    call process_character (n, appearance="blush false", text="И ты много читаешь.")
    call process_character (n, appearance="blush false", text="Ах, ах...")
    call process_character (julia, appearance="blush false", text="Совершенно разные ситуации, [n.say_name].")
    call process_character (julia, appearance="blush false", text="В своей повседневной жизни, да, я остаюсь собой.")
    call process_character (julia, appearance="blush false", text="Я предпочитаю спокойную обстановку.")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Но секс приносит прилив энергии в мой день.")
    call process_character (julia, appearance="blush false", text="Кроме...")
    call process_character (julia, appearance="blush false", text="Немногие знают, что я делаю наедине.")
    call process_character (julia, appearance="blush false", text="Только мне должно быть позволено это знать.")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (n, appearance="blush false", text="Так ты, ах, {w=0.5}, не рассказываешь никому об этом?")
    call process_character (julia, appearance="blush false", text="Говорить о том, что я беру в рот у двоюродного брата - это не то, что я бы открыто обсуждала.")
    call process_character (julia, appearance="blush false", text="Даже, если бы ты не был моим родственником, я все равно держала бы рот на замке.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ах! Ммм!")
    call process_character (julia, appearance="blush false", text="Ты уже готов кончить, не так ли?")
    call process_character (julia, appearance="blush false", text="Сейчас я сделаю несколько глубоких заглотов!")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="Я... я больше не могу...")
    call process_character (julia, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (julia, appearance="blush false", text="По крайней мере, я знаю, что ты способен производить много слизи.")
    call process_character (julia, appearance="blush false", text="Очень хорошо...")

    call static_still_ctc ("bg julia_blowjob_nocum")

    call process_character (n, appearance="blush false", text="Ааа...")
    call process_character (julia, appearance="blush false", text="Поторопись, или я разолью твою сперму на пол.")
    call process_character (n, appearance="blush false", text="Мм!")
    call process_character (n, appearance="blush false", text="Аах!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg julia_blowjob_cum")

    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Эх, полная загрузка...)")
    call process_character (n, appearance="blush false", text="Ааа...")
    call process_character (n, appearance="blush false", text="{i}Уфф!{/i}")

    call static_still_ctc ("bg julia_blowjob_swallowcum")

    call process_character (julia, appearance="blush false", text="{i}Глык{/i}")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Этот кусочку нужно время, чтобы спуститься!)")
    call process_character (julia, appearance="blush false", text="{i}Глык{/i}")

    call static_still_ctc ("bg julia_blowjob_almostcum")

    call process_character (julia, appearance="blush false", text="Всё закончено, [n.say_name].")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="И как на вкус?")
    call process_character (julia, appearance="blush false", text="Твоя сперма на самом деле не так плоха.")
    call process_character (julia, appearance="blush false", text="У прошлых парней она мне не нравилась, я её выплёвывала.")
    call process_character (julia, appearance="blush false", text="Но твоя, я признаю...")
    call process_character (julia, appearance="blush false", text="Это лучшее, что я попробовала.")

    jump julia_scene_blowjob_revisit_end

    return

label julia_scene_blowjob_revisit_2nd_time:
    $ no_bust_art = False
    $ display_multiple_characters([ (n, "pose behindhead neutral"), (julia, "pose handup face neutral blush false") ])

    call process_character (julia, appearance="pose handup face neutral blush false", text="Я просто не устояла перед такой...")

    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

    call static_still_ctc ("bg julia_blowjob_table")

    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Не знаю, что я буду делать, как лето закончится)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Обычно мне становится скучно через некоторое время с одним парнем)")
    call process_character (julia, appearance="blush false", text="(Но [n.say_name]...)")
    call process_character (julia, appearance="blush false", text="(Он меня увлек надолго)")
    call process_character (n, appearance="blush false", text="Ах, ах...")
    call process_character (n, appearance="blush false", text="(Интересно, будет ли [julia.say_name] в том же классе, что и [sa.say_name], и ​​я...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Надеюсь, у меня не будет вставать, если она сядет рядом со мной в классе)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Может быть, если она даст мне минет утром, перед школой...)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!")
    $ quick_menu = True


    call static_still_ctc ("bg julia_blowjob_nocum")

    call process_character (julia, appearance="blush false", text="(Он дергается...)")
    call process_character (julia, appearance="blush false", text="(Это подсказывает мне)")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg julia_blowjob_cum")

    call process_character (n, appearance="blush false", text="Хннг!")
    call process_character (julia, appearance="blush false", text="([n.say_name] кончает, как два или три парня, клянусь...)")

    call static_still_ctc ("bg julia_blowjob_swallowcum")

    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Это много, но, по крайней мере, он спускает плавно)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Это так здорово, что [julia.say_name] проглатывает...)")

    jump julia_scene_blowjob_revisit_end
    return

label julia_scene_blowjob_revisit_end:
    python:
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_cummed_in_mouth", 1)
        stats.add_stat("times_received_blowjob", 1)

    call process_end_of_scene ("julia_scene_blowjob_revisit", char=julia, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return


label julia_scene_vaginal:
    call process_scene_beginning (bg=nate_room )
    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (julia, "outfit clothes pose handup face neutral blush false") ])

    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Ну [n.say_name], ты хорошо развиваешься как мой сексуальный слуга.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="С-спасибо.")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Но я кое-что поняла...")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Эти футджобы и минеты...")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Я та, кто прилагает усилия.")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Это слишком одностороннее движение.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Т-ты имеешь в виду...")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Пришло время обслужить меня, [n.say_name].")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Ты должен трахнуть меня.")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="!")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="Т-трахнуть тебя?")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="И ты не должен быть робким.")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Я ожидаю, что твой член окажется глубоко внутри моей киски.")
    call process_character (n, appearance="pose handpocket face embarrassed blush true", text="...")

    if stats.stat_value("times_had_vaginal_sex") > 0:
        call process_character (julia, appearance="pose armcross face curious blush false", text="Ты знаешь, о чем я говорю, верно?")
        call process_character (n, appearance="pose twohandfist face concerned blush true", text="Д-да!")
        call process_character (n, appearance="pose twohandfist face concerned blush true", text="Ты хочешь, чтобы мой пенис вошёл во влагалище.")
        call process_character (julia, appearance="pose armcross face neutral blush false", text="Ты, как минимум, понимаешь, что нужно делать...")
        call process_character (julia, appearance="pose armcross face neutral blush false", text="Но можешь ли ты сделать это более интересным?")
    else:
        call process_character (julia, appearance="pose armcross face curious blush false", text="Ты знаешь, о чем я говорю, верно?")
        call process_character (n, appearance="pose behindhead face curious blush true", text="...")
        call process_character (n, appearance="pose behindhead face curious blush true", text="Думаю, что да.")
        call process_character (julia, appearance="pose armcross face neutral blush false", text="{i}Вздох.{/i}..")
        call process_character (julia, appearance="pose handface face neutral blush false", text="Твой пенис входит в мое влагалище.")
        call process_character (julia, appearance="pose handface face neutral blush false", text="Просто, не так ли?")
        call process_character (n, appearance="pose behindhead face concerned blush true", text="...")
        call process_character (n, appearance="pose behindhead face concerned blush true", text="Д-да.")
        call process_character (julia, appearance="pose handface face neutral blush false", text="Ну а теперь...")
        call process_character (julia, appearance="pose handface face neutral blush false", text="Как ты сделаешь это более интересным?")


    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Ч-что ты имеешь в виду?")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Ты не можешь просто вставить свой член и закончить на сегодня.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Не со мной.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Я хочу эффективного удовольствия.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Поэтому тебе нужно найти хорошую позу.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Позу?")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Вам нужно обдумать это?")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Я надеялась, что ты уже разобрался...")

    call prompt_menu_boldness_check ("У-у меня есть кое-что на уме.", "М-мне нужно время, чтобы подумать об этом.", "julia_scene_vaginal", julia)

    return

label julia_scene_vaginal_refusal(text, insufficient_points):
    call process_character (n, appearance="pose behindhead face concerned", text=text)
    call process_character (n, appearance="pose behindhead face curious blush false", text="(Я понятия не имею, что такое позы в сексе, [julia.say_name])")
    call process_character (n, appearance="pose behindhead face curious blush false", text="(Я должен убедиться, что я придумал что-то хорошее!)")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Я надеюсь, что дополнительное ожидание того стоит.")

    call prompt_refusal_end (julia)
    return

label julia_scene_vaginal_sex(dream=False):
    $ julia_vaginal_xray_on = False

    $ renpy.scene('screens')

    if nate_room.background() != store.current_background:
        call process_scene_beginning (bg=nate_room, dream=dream )
    elif dream and not persistent.disable_dream_blur:
        show screen dream_blur

    $ display_multiple_characters([ (n, "outfit clothesjacket pose behindhead face curious blush false"), (julia, "outfit clothes pose armcross face neutral blush false") ])

    call process_character (julia, appearance="pose armcross face neutral blush false", text="Хорошо, [n.say_name]...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Что ты можешь предложить?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...{p}...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="(Надеюсь, это хорошая идея...)")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Это время на подготовку или что-то еще?")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Ой...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Я просто... {w=1.0} хотел убедиться, что ты готова.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Ты итак в центре внимания, [n.say_name].")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Я в ожидании разогрева.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Хорошо...")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (n, appearance="outfit nudehard pose handsdown face concerned blush false", text="Вот оно.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Предполагаю, ты хочешь, чтобы я была голой?")
    call process_character (n, appearance="outfit nudehard pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit nudehard pose behindhead face concerned blush false", text="Да.")

    call character_leave_dissolve (julia)
    pause 0.5

    call process_character (n, appearance="outfit nudehard pose handsdown face concerned blush false")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

    call process_character (julia, appearance="outfit nude pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit nude pose handup face neutral blush false", text="Итак, мы должны встать для этого?")
    call process_character (n, appearance="outfit nudehard pose behindhead face curious blush false", text="Я... мне нужно, чтобы ты...")
    call process_character (n, appearance="outfit nudehard pose behindhead face curious blush false", text="Прислонись к стене.")
    call process_character (julia, appearance="outfit nude pose handup face neutral blush false", text="Встала к стене, да?")
    call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="Надеюсь, ты не планируешь что-то скучное, типа гриндинга...")

    call fade_to_black (1)

    call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="Хорошо, я у стены.")
    call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="...{p}...")
    call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="Ой...")
    call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="...")
    call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="Ты пытаешься поднять меня?")
    call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="...")
    call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="{cps=40} Что ты собираешься сделать-{/cps}{w=0.75}{nw}")

    call static_still_ctc ("bg julia_fuck_lift")

    call process_character (julia, appearance="blush false", text="Oох!")
    call process_character (n, appearance="blush false", text="Ах. Мм, ах...")
    call process_character (julia, appearance="blush false", text="Да!")
    call process_character (julia, appearance="blush false", text="Прижми меня к стене, [n.say_name]!")
    call process_character (julia, appearance="blush false", text="Вставь свой член так далеко, насколько это возможно!")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}Вздох,{/i} {i}Вздох.{/i}..")
    call process_character (julia, appearance="blush false", text="(Это сторона [n.say_name], которую я ждала!)")
    call process_character (julia, appearance="blush false", text="(Я действительно не думала, что он способен...)")
    call process_character (julia, appearance="blush false", text="(Но он доказывает, что я неправа!)")
    call process_character (n, appearance="blush false", text="Ах, ахх!")
    call process_character (n, appearance="blush false", text="Это, ах...")
    call process_character (n, appearance="blush false", text="Ты этого хотела, [julia.say_name]?")
    call process_character (julia, appearance="blush false", text="Мм, ах...")
    call process_character (julia, appearance="blush false", text="Это что-то чего я не знала, но хотела!")
    call process_character (julia, appearance="blush false", text="И это, ах, {w=0.5} то, что я искала в тебе, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Тебе хорошо?")
    call process_character (julia, appearance="blush false", text="Ах...")
    call process_character (julia, appearance="blush false", text="Меньше разговоров, больше траха, [n.say_name]!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (julia, appearance="blush false", text="([n.say_name] неважно выглядит со стороны...)")
    call process_character (julia, appearance="blush false", text="(Но он страстный, когда его член стоит!)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="([n.say_name] дал мне приятный сюрприз)")
    call process_character (n, appearance="blush false", text="Ха, ах!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="У тебя есть другие трюки в рукаве, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Т-ты хочешь, чтобы я сделал что-то еще?")
    call process_character (julia, appearance="blush false", text="Ну я не знаю на, что ты ещё способен.")
    call process_character (julia, appearance="blush false", text="Ах...")
    call process_character (julia, appearance="blush false", text="Мне любопытно посмотреть, что ты выдумаешь на лету.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Теперь, когда она это упоминает...)")
    call process_character (n, appearance="blush false", text="(Я не думаю, что смогу удержать ее дольше)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Может быть, я смогу попробовать что-нибудь на полу)")

    call fade_to_black (1)

    call process_character (julia, appearance="blush false", text="Твои руки скользят...")
    call process_character (julia, appearance="blush false", text="Не бросай меня на голову!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Что он задумал?)")

    $ julia_vaginal_xray_on = False
    call static_still_ctc ("bg julia_fuck_tip")
    show screen julia_vaginal_xray("bg julia_fuck_tip", "bg julia_fuck_tip_xray", xalign = 0.01, yalign = 0.01)

    call process_character (julia, appearance="blush false", text="(Какого черта, что эта позиция ?!)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Как [n.say_name] додумался до этого?)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Хорошо, что я гибкая для этого...)")
    call process_character (n, appearance="blush false", text="В-всё в порядке, [julia.say_name]?")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Что за дебильная часть твоего разума придумала такое?")
    call process_character (n, appearance="blush false", text="Ч-что?")
    call process_character (julia, appearance="blush false", text="В этом нет никаких сомнений...")
    call process_character (julia, appearance="blush false", text="Ты настоящий извращенец, чтобы придумать эту позу для траха.")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (julia, appearance="blush false", text="Ну, что же ты ждёшь?")
    call process_character (n, appearance="blush false", text="Т-ты хочешь, чтобы я продолжал?")
    call process_character (julia, appearance="blush false", text="Почему ты думаешь, что не одобряю?")
    call process_character (n, appearance="blush false", text="Н-но ты сказала, что я извращенец...")
    call process_character (julia, appearance="blush false", text="Да.")
    call process_character (julia, appearance="blush false", text="И?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Если тебе не было очевидно, [n.say_name]...")
    call process_character (julia, appearance="blush false", text="Только извращенец позволил бы трахаться в этой позе.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Но я долго не протяну в такой позе.")
    call process_character (julia, appearance="blush false", text="Давай уже!")
    call process_character (n, appearance="blush false", text="Х-хорошо.")
    call process_character (n, appearance="blush false", text="Я начинаю...")

    hide screen julia_vaginal_xray
    call static_still_ctc ("bg julia_fuck__xray_nocum")

    call process_character (n, appearance="blush false", text="Ах! Ах!")
    call process_character (n, appearance="blush false", text="(Мой член вошёл легко!)")
    call process_character (julia, appearance="blush false", text="Мм. Ох!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Это намного лучше, чем я ожидала!)")
    call process_character (julia, appearance="blush false", text="(И хотя боковым зрением я вижу качающиеся пару шаров, прикрепленных к заднице)")
    call process_character (julia, appearance="blush false", text="Ах, ах!")
    call process_character (julia, appearance="blush false", text="(Но думаю, я могу это вытерпеть)")
    call process_character (n, appearance="blush false", text="Ах, Ахх!")
    call process_character (n, appearance="blush false", text="(Член чувствует себя всё лучше и лучше, и становится более твёрдым!)")
    call process_character (julia, appearance="blush false", text="Ах, Ммм...")
    call process_character (julia, appearance="blush false", text="([n.say_name] схватил мою задницу, чтобы получить крепкую хватку)")
    call process_character (julia, appearance="blush false", text="Трахай сильнее меня, [n.say_name]!")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (julia, appearance="blush false", text="Ах, если ты продолжишь в том же духе...")
    call process_character (julia, appearance="blush false", text="Ты дашь мне, ах...")
    call process_character (n, appearance="blush false", text="Что я тебе дам?")
    call process_character (julia, appearance="blush false", text="Просто продолжай втыкать свой член в меня.")
    call process_character (n, appearance="blush false", text="Мм! Ммм!")
    call process_character (julia, appearance="blush false", text="Ахх...")
    call process_character (julia, appearance="blush false", text="Хмммм!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Вот теперь замечательно...)")
    call process_character (julia, appearance="blush false", text="([n.say_name] дал мне оргазмом)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Я могу на самом деле устать, прежде чем он закончит)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Эй, [n.say_name]...")
    call process_character (n, appearance="blush false", text="Ах, Ох!")
    call process_character (julia, appearance="blush false", text="Готовы ли твои шары выстрелить?")
    call process_character (n, appearance="blush false", text="Ммм...")
    call process_character (n, appearance="blush false", text="Ах!")
    call process_character (julia, appearance="blush false", text="Хорошо.")
    call process_character (julia, appearance="blush false", text="Мое тело не привыкло так изгибаться.")
    call process_character (n, appearance="blush false", text="Oох!")
    call process_character (n, appearance="blush false", text="Я готов кончить, [julia.say_name]!")
    call process_character (n, appearance="blush false", text="Ах, аах...")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg julia_fuck__xray_cum")

    call process_character (n, appearance="blush false", text="Аах, [julia.say_name]!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Он кончил в мою киску?)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Я никому этого не позволяла...)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="([n.say_name] имел честь быть первым)")
    call process_character (julia, appearance="blush false", text="...{p}...")
    call process_character (julia, appearance="blush false", text="Ты закончил, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Я-я так думаю.")

    $ julia_vaginal_xray_on = False
    call static_still_ctc ("bg julia_fuck__aftercum_nate")
    show screen julia_vaginal_xray("bg julia_fuck__aftercum_nate", "bg julia_fuck__aftercum_nate_xray", xalign = 0.01, yalign = 0.01)

    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Как много спермы.")
    call process_character (julia, appearance="blush false", text="Часть из ней катится по моей груди.")
    call process_character (n, appearance="blush false", text="Д-да...")
    call process_character (julia, appearance="blush false", text="Вот, что я скажу, [n.say_name]...")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Мне это понравилось.")
    call process_character (n, appearance="blush false", text="Э-это то, на что ты надеялась?")
    call process_character (julia, appearance="blush false", text="На этот раз...")
    call process_character (julia, appearance="blush false", text="Да, это было так.")
    call process_character (n, appearance="blush false", text="Круто!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Теперь, пожалуйста, будь любезен отойди?")
    call process_character (julia, appearance="blush false", text="Мои ноги практически согнуты за моими ушами.")

    hide screen julia_vaginal_xray
    call static_still_ctc ("bg julia_fuck_aftercum")

    call process_character (n, appearance="blush false", text="Я собираюсь сбегать в душ, чтобы отмыться.")
    call process_character (julia, appearance="blush false", text="Ого, держи коней!")
    call process_character (julia, appearance="blush false", text="Сначала я в душ.")
    call process_character (n, appearance="blush false", text="Как так?")
    call process_character (julia, appearance="blush false", text="Я вся в сперме.")
    call process_character (julia, appearance="blush false", text="А тебе просто надо вытереть член салфеткой.")
    call process_character (julia, appearance="blush false", text="Держись подальше, пока я не выйду из ванной.")

    python:
        julia.revistable_scenes.add("julia_scene_vaginal_revisit")

        if not dream:
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_vaginal_sex", 1)
            stats.add_stat("times_given_vaginal_creampie", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("julia_scene_vaginal", char=julia, dream=dream)

    return

label julia_scene_vaginal_revisit:
    if "julia_scene_vaginal_revisit" not in scenes_completed:
        jump julia_scene_vaginal_revisit_1st_time
    else:
        jump julia_scene_vaginal_revisit_2nd_time

    return



label julia_scene_vaginal_revisit_1st_time:
    $ no_bust_art = False
    $ display_multiple_characters([ (n, "pose twohandfist face neutral"), (julia, "pose handface face happy blush false") ])

    call process_character (julia, appearance="outfit clothes pose handface face happy blush false", text="Если это будет похоже на прошлый раз, я всеми руками за.")

    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

    call static_still_ctc ("bg julia_fuck_lift")

    call process_character (julia, appearance="blush false", text="Ммм, ах!")
    call process_character (julia, appearance="blush false", text="Хорошо, [n.say_name]!")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (julia, appearance="blush false", text="Ты сильнее, чем я думала.")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Ты можешь закинуть меня на стену.")
    call process_character (n, appearance="blush false", text="Ах, ахх!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Надеюсь, мы не слишком сильно бьёмся о стену)")
    call process_character (julia, appearance="blush false", text="(Большинство людей знают на, что указывает ритмичные удары...)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Хотя я сомневаюсь, что [sa.say_name] поймёт, что происходит)")
    call process_character (julia, appearance="blush false", text="(Не похожа, что она сексуально активна)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Я не удивилась бы, если она никогда не мастурбировала)")
    call process_character (n, appearance="blush false", text="Ах! М-м...")
    call process_character (n, appearance="blush false", text="[julia.say_name[0]]-[julia.say_name]...")
    call process_character (n, appearance="blush false", text="Мои руки устали.")
    call process_character (julia, appearance="blush false", text="Тебе нужен перерыв?")
    call process_character (n, appearance="blush false", text="Д-да...")
    call process_character (n, appearance="blush false", text="Тем не менее, мы все еще можем трахаться.")
    call process_character (julia, appearance="blush false", text="Надеюсь, что так.")
    call process_character (julia, appearance="blush false", text="Я не близка к тому, чтобы кончить!")

    $ julia_vaginal_xray_on = False
    call static_still_ctc ("bg julia_fuck_tip")
    show screen julia_vaginal_xray("bg julia_fuck_tip", "bg julia_fuck_tip_xray", xalign = 0.01, yalign = 0.01)

    call process_character (n, appearance="blush false", text="Можем ли мы сделать это, снова?")
    call process_character (julia, appearance="blush false", text="Хорошо, я предположила, что ты собираешься повторить ту позицию.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Д-да.")
    call process_character (julia, appearance="blush false", text="Видишь?")
    call process_character (julia, appearance="blush false", text="Тебе нравится попадать точным выстрелом в мою киску.")

    hide screen julia_vaginal_xray
    call static_still_ctc ("bg julia_fuck__xray_nocum")

    call process_character (n, appearance="blush false", text="Ах, ах, ах!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Интересно, будет ли он пробовать эту позицию с другой девушкой)")
    call process_character (julia, appearance="blush false", text="(Если ему когда-нибудь удастся заполучить девушку...)")
    call process_character (julia, appearance="blush false", text="Ах...")
    call process_character (julia, appearance="blush false", text="(На самом деле...)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Он делает больше, чем я обычно позволяла)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Я даже не знаю, почему я позволяю ему)")
    call process_character (julia, appearance="blush false", text="Ммм!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Может быть, я даю ему больше свободы, потому что мы родственники...)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Хотя в этом контексте...)")
    call process_character (julia, appearance="blush false", text="(Это прозвучало так, как будто я та ещё извращенка)")
    call process_character (n, appearance="blush false", text="А! Ммм!")
    call process_character (n, appearance="blush false", text="Ч-что это за штука выходит из твоей вагины?")
    call process_character (julia, appearance="blush false", text="Штука?")
    call process_character (julia, appearance="blush false", text="Ты имеешь в виду, сок из киски?")
    call process_character (n, appearance="blush false", text="С-сок из киски?")
    call process_character (julia, appearance="blush false", text="Не веди себя так, ах, {w=1.0}странно.")
    call process_character (julia, appearance="blush false", text="Это происходит, когда девушка возбуждается.")
    call process_character (julia, appearance="blush false", text="У тебя тоже есть собственный сок, если ты не заметил.")
    call process_character (n, appearance="blush false", text="Эта штука скользкая.")
    call process_character (julia, appearance="blush false", text="Это, облегчает трахание, не так ли?")
    call process_character (n, appearance="blush false", text="О-о да, ах!")
    call process_character (n, appearance="blush false", text="Оно делает!")
    call process_character (julia, appearance="blush false", text="Теперь ты знаешь, что это хорошая штука.")
    call process_character (n, appearance="blush false", text="Ох, ах!")
    call process_character (julia, appearance="blush false", text="Ха, ммн!")
    call process_character (julia, appearance="blush false", text="Тебе нравится минеты и футджобы, [n.say_name]?")
    call process_character (n, appearance="blush false", text="П-почему ты спрашиваешь?")
    call process_character (julia, appearance="blush false", text="Я хочу знать, ты любишь давать или получать...")

    menu:
        "Мне нравится, когда ты делаешь мне минеты и футджобы.":
            call process_character (julia, appearance="blush false", text="Даже после всего этого, да?")
            call process_character (julia, appearance="blush false", text="Я мастер фелляции.")
        "Мне нравится трахать тебя.":
            call process_character (julia, appearance="blush false", text="Было бы странно, если бы ты не выбрал именно это.")
        "Могу ли я выбрать оба варианта?":
            call add_boldness (1, tag="kira_scene_1_revisit_strain_anything")
            call process_character (julia, appearance="blush false", text="Понятно...")
            call process_character (julia, appearance="blush false", text="Вы любишь возбуждать свой сексуальный аппетит разными методами.")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Я понимаю.")

    call process_character (n, appearance="blush false", text="Хмм!")
    call process_character (n, appearance="blush false", text="Аах...")
    call process_character (n, appearance="blush false", text="[julia.say_name[0]]-[julia.say_name]!")
    call process_character (julia, appearance="blush false", text="Что? Ой...")
    call process_character (julia, appearance="blush false", text="Ты собираешься кончить, не так ли?")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg julia_fuck__xray_cum")

    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (n, appearance="blush false", text="Aaах!")
    call process_character (julia, appearance="blush false", text="Ага.")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Оо, да...")
    call process_character (julia, appearance="blush false", text="Эй, не спотыкайся и не падай на меня!")
    call process_character (julia, appearance="blush false", text="Я заметила, что у тебя подкашиваются ноги после того, как кончишь.")

    $ julia_vaginal_xray_on = False
    call static_still_ctc ("bg julia_fuck__aftercum_nate")
    show screen julia_vaginal_xray("bg julia_fuck__aftercum_nate", "bg julia_fuck__aftercum_nate_xray", xalign = 0.01, yalign = 0.01)

    call process_character (n, appearance="blush false", text="{i}Фуух.{/i}..")
    call process_character (julia, appearance="blush false", text="Эта позиция может быть интересной, но...")
    call process_character (julia, appearance="blush false", text="Черт, всё в сперме.")
    call process_character (n, appearance="blush false", text="Д-да.")
    call process_character (julia, appearance="blush false", text="Скажи, пожалуйста, что ты моешь полы после этого?")
    call process_character (julia, appearance="blush false", text="Я не хочу трахаться на испачканном ковре.")
    call process_character (n, appearance="blush false", text="М-моя Мама обычно моет пол.")
    call process_character (julia, appearance="blush false", text="Ээ, [n.say_name]...")
    call process_character (julia, appearance="blush false", text="Вычисти свою сперму сам, прежде чем она высохнет и запачкает ковёр.")

    hide screen julia_vaginal_xray

    jump julia_scene_vaginal_revisit_end

    return

label julia_scene_vaginal_revisit_2nd_time:
    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

    call static_still_ctc ("bg julia_fuck__xray_nocum")

    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="Это чувство, {i}вздох,{/i}{w=0.5} такое приятное.")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="([n.say_name] имеет высокое либидо)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Откуда оно у него?)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Его сестра [k.say_name], выглядит так, будто у нее было много членов раньше...)")
    call process_character (julia, appearance="blush false", text="(Но его мама и [sa.say_name] выглядят так, как будто и не было никогда у них секса)")
    call process_character (julia, appearance="blush false", text="(Его сестра [sa.say_name] выглядит так, как будто даже не видела член и не касалась его)")
    call process_character (julia, appearance="blush false", text="Ах, ах!")
    call process_character (julia, appearance="blush false", text="(Я не могу себе представить, как можно не заниматься сексом или даже не интересоваться этим!)")
    call process_character (n, appearance="blush false", text="Мм! Мм!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Интересно, скажет ли [julia.say_name] Маме о том, что мы делаем...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Надеюсь, она этого не сделает)")
    call process_character (n, appearance="blush false", text="(И Мама расскажет тёте...)")
    call process_character (n, appearance="blush false", text="(Мы оба столкнемся с огромными неприятностями!)")
    call process_character (julia, appearance="blush false", text="Ах, ахх!")
    call process_character (julia, appearance="blush false", text="(Мне бы хотелось увидеть лицо моей мамы, если бы она узнала, что я трахаюсь с [n.say_name])")
    call process_character (julia, appearance="blush false", text="(Она конкретно взбесится!)")
    call process_character (julia, appearance="blush false", text="(И её будет волновать не то что я занимаюсь этим с двоюродным братом)")
    call process_character (julia, appearance="blush false", text="(А спросит, почему я трахаюсь с [n.say_name], а не с футболистом из школы...)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", xalign = 0.01, yalign = 0.01)
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )


    call static_still_ctc ("bg julia_fuck__xray_cum")

    call process_character (n, appearance="blush false", text="Oох!")
    call process_character (julia, appearance="blush false", text="Аaахх!")
    call process_character (julia, appearance="blush false", text="(Он нажал на мою точку G!)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Сразу голова пошла кругом!)")

    call static_still_ctc ("bg julia_fuck__aftercum_nate")

    call process_character (n, appearance="blush false", text="{i}Фуух!{/i}")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Ты стал лучше разбираться в этом, [n.say_name].")

    jump julia_scene_vaginal_revisit_end
    return

label julia_scene_vaginal_revisit_end:
    python:
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_vaginal_sex", 1)
        stats.add_stat("times_given_vaginal_creampie", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("julia_scene_vaginal_revisit", char=julia, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label julia_scene_post_vaginal:
    call julia_scene_post_vaginal_sex

    return

label julia_scene_post_vaginal_sex(dream=False):
    call process_scene_beginning (living_room, char_tuple_array=[ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (julia, "outfit clothes pose handface face neutral blush false") ])

    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="[n.say_name]...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="У тебя есть секунда?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Конечно, [julia.say_name]!")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Речь идет о нашем небольшом соглашении, относительно твоей роли сексуального слуги.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Ага...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Что насчет него?")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Ты свободен.")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Тебе больше не обязательно быть секс-слугой.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Да?")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Нет никакой необходимости.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Как так?")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Потому что мы все равно будем трахаться.")
    call process_character (julia, appearance="outfit clothes pose handup face curious blush false", text="Ты бы занялся сексом со мной, даже если я не заставила тебя, верно?")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Ага...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="В этом ты права.")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Кроме того, я полагаю, что через некоторое время ты откажешься служить мне.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Хм?")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Почему ты думаешь, что я это сделаю?")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Если бы я был на твоем месте, я бы не потерпел этого.")
    call process_character (julia, appearance="outfit clothes pose armcross face angry blush false", text="Я сказала бы человеку, что он пойдет на х.., если попытается сделать меня секс-слугой.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Это все, что я хотела тебе сказать.")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Тебе больше не нужно повиноваться.")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Если ты захочешь потрахаться, просто скажи мне.")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Кроме этого, можешь игнорировать меня на оставшуюся часть лета, если хочешь.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="...")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Игнорировать тебя?")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Зачем?")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Я знаю, что я не совместима с тобой и твоими интересами.")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="И ты не совместим с мной, ну кроме секса.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Я не думаю, что это правда...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Нам обоим нравится читать эти фэнтезийные книги!")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Но ты предпочтёшь фэнтези видеоигру, чем книгу.")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Ничего плохого в этом, это твой выбор.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="...{p}...")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Что ж...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Хотелось бы, чтобы ты и я могли действительно наслаждаться...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Да, сексом.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Нет, нет, я имею в виду...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Что-то иное, не только секс!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Несколько лет назад нам нравилось одно и то же, тебе, мне и [sa.say_name]!")
    call process_character (julia, appearance="outfit clothes pose handface face curious blush false", text="С тех пор многое изменилось...")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Ну... {w=1.0}, это просто означает, что мы должны вновь найти то, что нам понравится делать вместе!")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Я не знаю, почему ты в восторге от этого, но всё же.")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Если ты хочет уйти, уходи прямо сейчас.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Я придумаю что-нибудь, [julia.say_name]!")
    call process_character (n, appearance="pose handpocket face happy blush false", text="Я в этом уверен!")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Ммм...")


    call process_new_location (sam_room)


    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false")

    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="[sa.say_name]!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="У меня есть задание для нас!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Оох, задание?")
    call process_character (sa, appearance="pose handface face happy blush false", text="Мне нравится, как это звучит!")
    call process_character (sa, appearance="pose handface face happy blush false", text="В чем цель?")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Нам нужно выяснить, что [julia.say_name] понравится делать вместе с нами!")
    call process_character (sa, appearance="pose handface face concerned blush false", text="О, вау, это... {w=1.0} непростое задание...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Я знаю...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Это сложно, потому что [julia.say_name] не любит видеоигры...")

    if "simone_convo_15" in si.conversations_completed:
        call process_character (sa, appearance="pose handsbehind face curious blush false", text="Храмы и Гидры тоже не подойдут.")
        call process_character (sa, appearance="pose handsbehind face curious blush false", text="Помнишь тот раз, когда мы пытались сыграть на днях?")
        call process_character (sa, appearance="pose handface face concerned blush false", text="Ей не понравился сценарий, который я создала, ни персонажи!")
        call process_character (n, appearance="pose handpocket face curious blush false", text="Ага...")
        call process_character (n, appearance="pose handpocket face curious blush false", text="Это была непродолжительная кампания.")

    call process_character (sa, appearance="pose handface face curious blush false", text="Hmm...")

    call process_character (n, appearance="pose handpocket face neutral blush false")

    call process_character (sa, appearance="pose handface face curious blush false", text="...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Эй, я знаю!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Мы играли в настольные игры все время!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Может быть, ей понравится одна из них!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Ты уверена?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Даже мне это надоедает через некоторое время.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Они слишком просты.")
    call process_character (sa, appearance="pose leaning face concerned blush false", text="Хорошая точка зрения.")
    call process_character (sa, appearance="pose leaning face concerned blush false", text="...{p}...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ой!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="А что на счёт, этих более продвинутых настольных игр, которые сейчас нет?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Я думаю, мы видели, как их недавно рекламировали в Интернете...")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Думаю, я их помню!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Типа тех про научную фантастику?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Да!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Я думаю подойдет любая!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Некоторые из них основаны на видеоиграх, фильмах, книгах...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты сказала, что часть из них основаны на книгах?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Из того, что я увидела, они выглядели абсолютно безумными!")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="На самом деле сложные, и с глубоким сюжетом!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Да?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Хм...")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="pose handpocket face happy blush false", text="У меня есть идея, [sa.say_name]!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Кажется, я знаю, какую нужно выбрать!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Какая любимая книга [julia.say_name]?")
    call process_new_location (living_room)


    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...{p}...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Привет, [julia.say_name]!")
    call character_leave_dissolve (n)
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false position right", text="У нас есть сюрприз для тебя!")
    call process_character (julia, appearance="outfit clothes pose armcross face curious blush false", text="Хм?")
    call process_character (julia, appearance="outfit clothes pose armcross face curious blush false", text="Сюрприз?")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Вот смотри!")
    call process_character (julia, appearance="outfit clothes pose armcross face curious blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Это настольная игра...")
    call character_leave_dissolve (sa)
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Не просто настольная игра!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Посмотри на название!")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Написано, что она основана на...")
    call process_character (julia, appearance="outfit clothes pose handface face happy blush false", text="Рассказах о Парящих Королевствах?!")
    call character_leave_dissolve (n)
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="Ага!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="Игра проходит по всей трилогии!")
    call character_leave_dissolve (sa)
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="А супер круто то, что ты можешь выбрать альтернативные пути и полностью изменить ход истории!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Плюс, это совместная игра, поэтому мы будем заниматься этим вместе!")
    call process_character (julia, appearance="outfit clothes pose armcross face happy blush false", text="Здесь также говорится, что она написана оригинальным автором!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Эксклюзивно для этой специальной версии!")
    call process_character (julia, appearance="outfit clothes pose armcross face curious blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose armcross face curious blush false", text="Ты купил её для меня?")
    call character_leave_dissolve (n)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Этим летом мы провели мало времени вместе.")
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="И это просто глупо, так как мы в одном доме!")
    call character_leave_dissolve (sa)
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Мы решили, что ты захочешь сыграть в настольную игру, созданной по книге, которая тебе нравится!")
    call character_leave_dissolve (n)
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Её невозможно завершить за один присест!")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Мы можем играть на протяжении всего лета!")
    call process_character (julia, appearance="outfit clothes pose armcross face happy blush false", text="...")
    call character_leave_dissolve (sa)
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Хочешь сыграть прямо сейчас, [julia.say_name]?")
    call process_character (julia, appearance="outfit clothes pose handup face happy blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handup face happy blush false", text="Да, на самом деле.")
    call process_character (julia, appearance="outfit clothes pose handup face happy blush false", text="Это одна из моих любимых книг!")
    call process_character (julia, appearance="outfit clothes pose handup face happy blush false", text="Как тебе удалось найти что-то подобное?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Это было нелегко, это точно!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Их не очень много.")
    call character_leave_dissolve (n)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Хорошо, давай настроим!")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Думаю, что я выберу королевство льда!")
    call process_character (julia, appearance="outfit clothes pose armcross face happy blush false", text="Я - королевство камня.")
    call process_character (julia, appearance="outfit clothes pose armcross face happy blush false", text="Если здесь так же, как в рассказах, тут будут самые жестокие драконы.")

    call fade_to_black (1)

    "{i}Позже этим вечером...{/i}"

    call process_new_location ("bg living_room_evening")

    $ display_multiple_characters([ (n, "outfit clothesjacket pose behindhead face neutral blush false"), (julia, "outfit clothes pose handface face happy blush false") ])
    call process_character (si, appearance="", text="[sa.say_name], [julia.say_name], [n.say_name]!")
    call process_character (si, appearance="", text="Ужин готов!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Разве мы так долго играли?")
    call character_leave_dissolve (n)
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false position right", text="Эта игра, настолько захватывающая!")
    call process_character (julia, appearance="outfit clothes pose handface face happy blush false", text="Мне это очень понравилось.")
    call character_leave_dissolve (sa)
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Это потрясающе!")
    call character_leave_dissolve (n)
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Мы рады, что тебе понравилось, [julia.say_name]!")
    call process_character (julia, appearance="outfit clothes pose handface face happy blush false", text="Я никогда бы и не подумала, что существует такая игра до сегодняшнего дня.")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Интересно, есть ли другие.")
    call character_leave_dissolve (sa)
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="О да, есть много!")
    call character_leave_dissolve (n)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Мы должны показать тебе онлайн каталог!")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Я бы сказала, что на сегодня хватит.")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Согласна.")
    call process_character (julia, appearance="outfit clothes pose handup face happy blush false", text="Ещё многое предстоит сделать.")
    call character_leave_dissolve (sa)
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Оставим игру в гостиной.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Таким образом, нам больше не придется доставать её!")
    call character_leave_dissolve (n)
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Мама приготовила тушеное мясо сегодня вечером?")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Я так с нетерпением жду этого!")

    call fade_to_black (1)


    call process_new_location ("bg nate_room_evening")

    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="([julia.say_name] выглядела так, будто сегодня ей было очень весело)")
    call process_character (n, appearance="outfit underwear pose handfist face neutral blush false", text="(Нам всем было весело!)")
    call process_character (n, appearance="outfit underwear pose handfist face neutral blush false", text="...")
    call process_character (julia, appearance="outfit underwear pose handface face neutral blush false", text="Ничего, если я зайду, [n.say_name]?")
    call process_character (n, appearance="outfit underwear pose twohandfist face neutral blush false", text="Привет [julia.say_name]!")
    call process_character (n, appearance="outfit underwear pose twohandfist face happy blush false", text="Я просто думал о том, как здорово было бы найти эту игру раньше!")
    call process_character (julia, appearance="outfit underwear pose handup face happy blush false", text="Да, я тоже об этом думала.")
    call process_character (julia, appearance="outfit underwear pose handup face happy blush false", text="Я придумала новые стратегии, скорее бы продолжить.")

    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false")

    call process_character (julia, appearance="outfit underwear pose handup face happy blush false", text="...")
    call process_character (julia, appearance="outfit underwear pose armcross face neutral blush false", text="Слушай, [n.say_name]...")
    call process_character (julia, appearance="outfit underwear pose armcross face neutral blush false", text="...")
    call process_character (julia, appearance="outfit underwear pose armcross face happy blush false", text="Я... {w=1.0} хочу поблагодарить тебя за покупку этой настольной игры.")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="Пожалуйста!")
    call process_character (n, appearance="outfit underwear pose behindhead face happy blush false", text="Я надеялся, что тебе понравится!")
    call process_character (julia, appearance="outfit underwear pose handface face happy blush false", text="...")
    call process_character (julia, appearance="outfit underwear pose handface face happy blush false", text="Вот что делает тебя, [n.say_name] уникальным.")
    call process_character (julia, appearance="outfit underwear pose handface face happy blush false", text="Клянусь, ты когда-нибудь станешь филантропом или кем-то похожим.")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="Филантроп?")
    call process_character (julia, appearance="outfit underwear pose handface face happy blush false", text="Ты в основном просто хочешь, чтобы все были счастливы и чувствовали себя хорошо.")
    call process_character (julia, appearance="outfit underwear pose armcross face happy blush false", text="Ты даже преуспел со мной, когда я не думала, что ты мог бы.")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="Рад слышать это!")
    call process_character (julia, appearance="outfit underwear pose armcross face happy blush false", text="...")
    call process_character (julia, appearance="outfit underwear pose handup face happy blush false", text="Теперь имеет смысл, почему ты так трахаешь меня...")
    call process_character (julia, appearance="outfit underwear pose handup face happy blush false", text="Ты знаешь, мне это нравится, поэтому ты хочешь сделать это ещё лучше.")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="...")
    call process_character (julia, appearance="outfit underwear pose handface face happy blush false", text="Или это потому, что тебе это нравится?")
    call process_character (n, appearance="outfit underwear pose twohandfist face embarrassed blush false", text="Я... И то, и другое!")
    call process_character (julia, appearance="outfit underwear pose handface face happy blush false", text="Хех, я была прав.")
    call process_character (julia, appearance="outfit underwear pose handface face happy blush false", text="Ты действительно хочешь, чтобы мне это понравилось.")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="...")
    call process_character (julia, appearance="outfit underwear pose armcross face neutral blush false", text="Я уверена, что ты хочешь спать.")
    call process_character (julia, appearance="outfit underwear pose armcross face neutral blush false", text="Я тоже.")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="Ага...")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="Моему мозгу нужен отдых после изучения всех правил в этой игре.")
    call process_character (julia, appearance="outfit underwear pose handup face happy blush false", text="Если у тебя будет свободное время, когда ты встанешь, можно будет немного пообщаться.")
    call process_character (n, appearance="outfit underwear pose handfist face neutral blush false", text="Круто, я запомню это!")
    call process_character (n, appearance="outfit underwear pose handfist face neutral blush false", text="Спокойной ночи, [julia.say_name]!")



    call process_end_of_scene ("julia_scene_post_vaginal", char=julia, dream=dream, force_no_boldness=True, force_not_replayable=True)

    return

label julia_scene_anal:
    call julia_scene_anal_sex

    return

label julia_scene_anal_sex(dream=False):
    call process_scene_beginning (hallway, char_tuple_array=[ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (julia, "outfit clothes pose handface face neutral blush false") ], dream=dream)

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Привет, [julia.say_name].")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Что задумала?")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...{p}...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Ты о чём-то думаешь?")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Ага...")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Новый сюжет?")
    call process_character (julia, appearance="outfit clothes pose armcross face happy blush false", text="Хорошая догадка...")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Но это не так.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Это не так?")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Это... {w=1.0} не то, что мы можем обсудить здесь.")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Я могу рассказать тебе в твоей комнате.")
    call process_character (julia, appearance="outfit clothes pose handup face curious blush false", text="То есть, если ты действительно хочешь это знать.")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Мне слишком любопытно!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Да, я хочу знать!")

    call process_new_location (nate_room, dream=dream)


    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false")

    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Убедись, что дверь закрыта.")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Понял!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Теперь ты можешь мне сказать?")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Я все время занималась сексом этим летом.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Да?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Готов поклясться, что много.")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Это еще мягко сказано...")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Когда я сложила все разы, я пересчитала еще несколько раз.")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Потому что я действительно не могла в это поверить.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="И сколько?")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Это не так важно, как то, какие выводы я сделала.")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="[n.say_name]...")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="За лето ты трахал меня больше, чем за всю мою жизнь раньше!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Это... {w=0.5} много?")
    call process_character (julia, appearance="outfit clothes pose armcross face curious blush false", text="\"Это много?\"")
    call process_character (julia, appearance="outfit clothes pose armcross face curious blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Позволь мне сказать, это так...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Весь секс, который у меня был за последние пару лет, ты сравнял в то время, пока я была здесь.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Уоооу...")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Ага...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Мне нравится, как много мы это делаем!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Здорово!")
    call process_character (julia, appearance="outfit clothes pose handface face happy blush false", text="Ох, согласна.")
    call process_character (julia, appearance="outfit clothes pose handface face happy blush false", text="Я указываю на моё неподдельное удивление в результате совершенного нами подвига.")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Ты думаешь, что есть награды за такие вещи?")
    call process_character (julia, appearance="outfit clothes pose armcross face happy blush false", text="Ха, я в этом сомневаюсь.")
    call process_character (julia, appearance="outfit clothes pose armcross face happy blush false", text="Зачем нам нужна награда?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Ну, я не знаю...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Просто чтобы показать, насколько мы впечатляющие!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Представь, были ли медали или даже короны!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Нас можно было назвать королем и королевой траха!")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Королева траха, да?")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face happy blush false", text="Титул, который я бы не хотела получить...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Я думаю, что для секса нет наград или достижений.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face happy blush false", text="Мне всё равно нравится это делать!")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Пока мы говорим на эту тему, [n.say_name]...")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Есть тип секса, который я никогда раньше не пробовала.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Какой?")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Я никогда не позволяла кому-либо делать это со мной.")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Я не была достаточно уверена в них.")
    call process_character (julia, appearance="outfit clothes pose armcross face concerned blush false", text="Плюс я... {w=1.0} нервничала из-за этого.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Какого рода секс?")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Анальный.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Вместо того, чтобы совать член в мою киску, суй его в мой анус.")
    call process_character (julia, appearance="outfit clothes pose handface face curious blush false", text="Ты когда-нибудь слышал об этом?")

    $ heard_of_anal = True

    if stats.stat_value("times_given_anal_sex") > 0:
        call process_character (n, appearance="pose twohandfist face neutral blush false", text="О да, да!")
        call process_character (n, appearance="pose twohandfist face neutral blush false", text="Я слышал об этом раньше.")
        call process_character (julia, appearance="pose armcross face curious blush false", text="Это звучало слишком самоуверенно.")
        call process_character (julia, appearance="pose armcross face curious blush false", text="Ты уверен, что слышал об этом?")
        call process_character (n, appearance="pose handpocket face curious blush false", text="...")
        call process_character (julia, appearance="pose armcross face neutral blush false", text="Я слышал, что это туже, чем трахать киску.")
    else:
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Нет, я никогда не слышал об анале...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="Так это ничем не отличается от того, как вставлять мой пенис в твою киску?")
        call process_character (julia, appearance="pose armcross face neutral blush false", text="Есть одно важное отличие от того, что ты мне сказал...")
        call process_character (julia, appearance="pose armcross face neutral blush false", text="Это гораздо туже.")
        call process_character (n, appearance="pose handpocket face curious blush false", text="Туже?")
        call process_character (julia, appearance="pose handup face neutral blush false", text="Это значит, что тебе придется проталкивать свой член в мою задницу сильнее, чем во влагалище.")
        call process_character (n, appearance="pose handpocket face concerned blush false", text="О-ох...")

    call process_character (julia, appearance="pose handface face neutral blush false", text="Так или иначе...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Итак, ты никогда этого не делал раньше?")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Нет, но...")
    call process_character (julia, appearance="pose handface face happy blush false", text="Я думаю, что пойму, как это делать.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Как я уже говорила...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="У нас с тобой быстро накопилась сексуальная связь.")
    call process_character (julia, appearance="pose handup face aroused blush false", text="Я чувствую себя все более и более комфортно с тобой, когда мы трахаемся.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Ты помогла мне стать более уверенным, когда трахаю тебя, [julia.say_name]!")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Это правда.")
    call process_character (julia, appearance="pose handface face happy blush false", text="Сначала ты был неотёсанным чурбаном.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="...")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Я не могу отрицать этого...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="...")
    call process_character (julia, appearance="pose armcross face embarrassed blush false", text="Неловко это говорить, но...")

    call process_character (n, appearance="pose handpocket face neutral blush false")

    call process_character (julia, appearance="pose armcross face embarrassed blush false", text="...")
    call process_character (julia, appearance="pose armcross face embarrassed blush false", text="Я достигла точки, когда... {w=1.0} Я верю в твою сексуальные способности [n.say_name].")
    call process_character (julia, appearance="pose handface face embarrassed blush false", text="Поэтому я хочу, чтобы ты был первым... {w=1.0} попробуй это со мной.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Ты говоришь...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Ты хочешь заниматься со мной анальным сексом?")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Я не думаю, что смогу положиться на кого-либо еще так же, как и на тебя.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Фактически, мой анальный опыт, скорее всего, будет исключительно для тебя.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Похоже, ты долго ждала, чтобы попробовать!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Начнём прямо сейчас!")
    call process_character (julia, appearance="pose armcross face curious blush false", text="Прямо сейчас?")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (n, appearance="outfit nudehard pose handfist face neutral blush false")
    pause 0.5

    call process_character (n, appearance="outfit nudehard pose handfist face neutral blush false", text="Конечно, почему бы и нет?")
    call process_character (n, appearance="outfit nudehard pose handfist face happy blush false", text="Сейчас самое подходящее время, не так ли?")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="([n.say_name] взял на себя ответственность?]")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face aroused blush false", text="(Это довольно сексуально...)")
    call process_character (julia, appearance="outfit clothes pose handface face aroused blush false", text="(И это заставляет меня захотеть попробовать...)")

    call character_leave_dissolve (julia)
    pause 0.5

    call process_character (julia, appearance="outfit nude pose handface face happy blush false")
    pause 0.5

    call process_character (julia, appearance="outfit nude pose handface face happy blush false", text="Хорошо, ты замотивировал меня!")
    call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="Я собираюсь попробовать свой первый анал, но не переусердствуй!")
    call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="Я хочу, чтобы ты следовал моим указаниям, хорошо?")
    call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="Для меня это неизвестная территория.")
    call process_character (n, appearance="outfit nudehard pose twohandfist face neutral blush false", text="Я понимаю.")
    call process_character (n, appearance="outfit nudehard pose twohandfist face neutral blush false", text="Я последую твоим руководствам!")
    call process_character (julia, appearance="outfit nude pose handface face curious blush false", text="Твой пол чист?")
    call process_character (n, appearance="outfit nudehard pose handfist face neutral blush false", text="Пропылесосил сегодня утром!")
    call process_character (julia, appearance="outfit nude pose handface face neutral blush false", text="Хорошо.")
    call process_character (julia, appearance="outfit nude pose handface face neutral blush false", text="Первый шаг - встать в правильное положение.")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Suave Standpipe.ogg", fadein = 1.0)

    call static_still_ctc ("bg julia_anal_onfloor")

    call process_character (julia, appearance="blush false", text="Вот лучший способ попробовать анал в первый раз... {w=0.5} Я думаю.")
    call process_character (n, appearance="blush false", text="Думаешь?")

    if stats.stat_value("times_given_anal_sex") > 0:
        call process_character (julia, appearance="blush false", text="Какой?")
        call process_character (julia, appearance="blush false", text="У тебя есть лучший способ?")
        call process_character (n, appearance="blush false", text="Что ж...")
        call process_character (n, appearance="blush false", text="Я просто знаю, что есть другие способы...")
        call process_character (julia, appearance="blush false", text="Эта поза, которая мне очень нравится, поэтому мы придерживаемся этого.")
    else:
        call process_character (julia, appearance="blush false", text="Ты знаешь так же мало, как я.")
        call process_character (julia, appearance="blush false", text="Мы должны с чего-то начать.")
        call process_character (n, appearance="blush false", text="Верно подмечено...")
        call process_character (julia, appearance="blush false", text="Эта поза, которую я придумал, поэтому мы придерживаемся ее.")

    call process_character (julia, appearance="blush false", text="Одна вещь [n.say_name]...")
    call process_character (julia, appearance="blush false", text="Не вводи свой член быстро!")
    call process_character (n, appearance="blush false", text="Должен ли я быть осторожным?")
    call process_character (julia, appearance="blush false", text="Да, я бы предпочла.")
    call process_character (julia, appearance="blush false", text="Я понятия не имею, как это будет выглядеть.")
    call process_character (n, appearance="blush false", text="Хорошо.")
    call process_character (julia, appearance="blush false", text="Хорошо, встань близко ко мне.")
    call process_character (julia, appearance="blush false", text="Если мы будем ждать слишком долго, ты обмякнешь, и это будет почти невозможно.")
    call process_character (n, appearance="blush false", text="...")

    call static_still_ctc ("bg julia_anal_butthole")

    call process_character (n, appearance="blush false", text="Хорошо, я настолько близко, что ближе некуда.")
    call process_character (julia, appearance="blush false", text="Хорошо.")
    call process_character (julia, appearance="blush false", text="Удостоверься, что твой член стоит.")
    call process_character (julia, appearance="blush false", text="Выровняй его с моим анусом.")

    call static_still_ctc ("bg julia_anal_butthole_dicktouch")

    call process_character (julia, appearance="blush false", text="Я чувствую, как он меня касается!")
    call process_character (julia, appearance="blush false", text="Не дави слишком сильно!")
    call process_character (n, appearance="blush false", text="Я не буду.")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(На что это будет похоже?)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я засуну, когда ты скажешь мне, [julia.say_name].")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Вводи, но медленно!")

    call static_still_ctc ("bg julia_anal_butthole_pushin")

    call process_character (julia, appearance="blush false", text="Ой! Oох!")
    call process_character (julia, appearance="blush false", text="A!")
    call process_character (n, appearance="blush false", text="Хмм!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Это очень туго!")
    call process_character (julia, appearance="blush false", text="Уже?")
    call process_character (julia, appearance="blush false", text="...{p}...")
    call process_character (julia, appearance="blush false", text="Продолжай пытаться!")
    call process_character (n, appearance="blush false", text="Ты уверена?")
    call process_character (julia, appearance="blush false", text="Мы зашли уже слишком далеко, [n.say_name]!")
    call process_character (julia, appearance="blush false", text="Если я остановлюсь сейчас, я никогда не захочу повторить это снова!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я думаю, мне придется немного подтолкнуть...")
    call process_character (julia, appearance="blush false", text="Сильнее, чем сейчас?")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Сделай это... {w=1.0} сделай то, что нужно!")
    call process_character (n, appearance="blush false", text="Ммм!")

    if "sam_scene_anal" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Это напоминает мне, когда я трахал [sa.say_name] в задницу!)")
        call process_character (n, appearance="blush false", text="(Хотя [sa.say_name] как-то упала на мой член, так что он быстро вошёл...)")
        call process_character (n, appearance="blush false", text="(Это намного сложнее, когда вводишь медленно!)")
    elif "kira_scene_anal" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Я и не знал, что это может быть так туго заниматься аналом!)")
        call process_character (n, appearance="blush false", text="(Когда я делал это с [k.say_name], я вставил его без проблем!)")
    elif "simone_scene_anal" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Я и не знал, что это может быть так туго заниматься аналом!)")
        call process_character (n, appearance="blush false", text="(Когда я делал это с Мамой, я вставил его без проблем!)")
    elif "gloryhole_scene_anal" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Я и не знал, что это может быть так туго заниматься аналом!)")
        call process_character (n, appearance="blush false", text="(Когда я делал это с [gloryhole_girl.say_name], я вставил его без проблем!)")
    else:
        call process_character (n, appearance="blush false", text="([julia.say_name] была прав!)")
        call process_character (n, appearance="blush false", text="(Это гораздо труднее, чем попасть в киску!)")
        call process_character (n, appearance="blush false", text="(Смогу ли я это сделать?)")

    call process_character (julia, appearance="blush false", text="Aах!")
    call process_character (julia, appearance="blush false", text="Продолжай толкать, продолжай толкать!")
    call process_character (julia, appearance="blush false", text="{cps=40}В конце концов, он должен войти-{/cps}{w=0.75}{nw}")

    call static_still_ctc ("bg julia_anal_butthole_allin")

    call process_character (julia, appearance="blush false", text="Аах!")
    call process_character (n, appearance="blush false", text="Oох!")
    call process_character (n, appearance="blush false", text="Я заметил!")
    call process_character (n, appearance="blush false", text="Наконец-то он вошел!")
    call process_character (julia, appearance="blush false", text="Нихрена себе...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ты в порядке, [julia.say_name]?")
    call process_character (n, appearance="blush false", text="Должен ли я вытащить его обратно?")
    call process_character (julia, appearance="blush false", text="(Моя задница, кажется, в шоке!)")
    call process_character (julia, appearance="blush false", text="(Даже моя киска это ощущает!)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="[julia.say_name]?")
    call process_character (n, appearance="blush false", text="Тебе нравится?")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Трахай меня.")
    call process_character (n, appearance="blush false", text="Серьёзно?")
    call process_character (julia, appearance="blush false", text="Трахни меня, [n.say_name]!")
    call process_character (n, appearance="blush false", text="П-понял!")

    call static_still_ctc ("bg julia_anal_fuck")

    call process_character (julia, appearance="blush false", text="Ooох!")
    call process_character (julia, appearance="blush false", text="Чёёёрт!")
    call process_character (n, appearance="blush false", text="Ууау!")
    call process_character (n, appearance="blush false", text="Это совсем по-другому, [julia.say_name]!")
    call process_character (julia, appearance="blush false", text="Да, да!")
    call process_character (julia, appearance="blush false", text="Сложнее, тяжелее!")
    call process_character (julia, appearance="blush false", text="Вставь его глубже!")
    call process_character (n, appearance="blush false", text="Глубже?")
    call process_character (julia, appearance="blush false", text="Засунь весь свой член в мою задницу!")
    call process_character (julia, appearance="blush false", text="Всё до последнего дюйма!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Что случилось с [julia.say_name]?)")
    call process_character (n, appearance="blush false", text="(Обычно она не такая, когда мы трахаемся...)")
    call process_character (julia, appearance="blush false", text="Мм, да!")
    call process_character (julia, appearance="blush false", text="Держи мою задницу раскрытой, [n.say_name]!")
    call process_character (julia, appearance="blush false", text="Растяни её во всю ширину своего члена!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Как будто анал полностью изменил её поведение...)")
    call process_character (n, appearance="blush false", text="Ахх...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Она должно быть чувствует себя очень хорошо, раз так сильно изменилась)")
    call process_character (julia, appearance="blush false", text="Аaах!")
    call process_character (julia, appearance="blush false", text="Быстрее, {i}вздох.{/i}..{w=0.5}быстрее, [n.say_name]!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Я полностью потеряла контроль над собой!)")
    call process_character (julia, appearance="blush false", text="(Я вся теку от удовольствия!)")
    call process_character (julia, appearance="blush false", text="Ммм!")
    call process_character (julia, appearance="blush false", text="(Это лучше любого траха, который я получала раньше!)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Возможно, так как это мой первый анал, то я не была готова к такой стимуляции...)")
    call process_character (julia, appearance="blush false", text="Чёрт, чёрт!")
    call process_character (julia, appearance="blush false", text="(Это не может быть реальной причиной...)")
    call process_character (julia, appearance="blush false", text="(Нет, я думаю, что там самая чувствительная область моего тела!)")
    call process_character (julia, appearance="blush false", text="(Я никогда получала оргазм более одного раза во время траха...)")
    call process_character (julia, appearance="blush false", text="(У меня только что был третий!)")
    call process_character (n, appearance="blush false", text="[julia.say_name]...")
    call process_character (n, appearance="blush false", text="Что мне делать, когда я буду кончать?")
    call process_character (julia, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (julia, appearance="blush false", text="Мм, Мм!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ты хочешь, чтобы я кончил в твою задницу?")
    call process_character (julia, appearance="blush false", text="Ох, это так чертовски хорошо!")
    call process_character (julia, appearance="blush false", text="Да!")
    call process_character (julia, appearance="blush false", text="Круто!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я даже не думаю, что она меня слышит...)")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (n, appearance="blush false", text="(Я знаю, что скоро кончу!)")
    call process_character (n, appearance="blush false", text="(Мы не останавливались на секунду!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Кончи в меня, [n.say_name]!")
    call process_character (julia, appearance="blush false", text="Я знаю, что у тебя много спермы в этих шарах!")
    call process_character (julia, appearance="blush false", text="Я хочу, чтобы всё влилось в мою задницу!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я дам тебе это, [julia.say_name]!")
    call process_character (n, appearance="blush false", text="Я дам все!")
    call process_character (n, appearance="blush false", text="Аaaах!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg julia_anal_fuck_cuminside")

    call process_character (julia, appearance="blush false", text="{i}Задыхается!{/i}")
    call process_character (julia, appearance="blush false", text="Сделай кремовый пирог моей заднице!")
    call process_character (n, appearance="blush false", text="Мм!{p}Мм!")
    call process_character (julia, appearance="blush false", text="Я... я не могу удержать все это!")
    call process_character (julia, appearance="blush false", text="Я не могу!")
    call process_character (julia, appearance="blush false", text="Вытаскивай, [n.say_name]!")

    call static_still_ctc ("bg julia_anal_fuck_cum")

    call process_character (n, appearance="blush false", text="(Часть спермы осталась на моём члене!)")
    call process_character (n, appearance="blush false", text="([julia.say_name] сказала мне вытащить, прежде чем я полностью кончу!)")
    call process_character (julia, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (julia, appearance="blush false", text="Моя задница не может справиться с таким количество!")
    call process_character (julia, appearance="blush false", text="Я должна была знать!")
    call process_character (julia, appearance="blush false", text="Ооох...")

    call static_still_ctc ("bg julia_anal_aftercum")

    call process_character (julia, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Эй, [julia.say_name]?")
    call process_character (n, appearance="blush false", text="[julia.say_name]?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Мы не переусердствовали, не так ли?)")
    call process_character (julia, appearance="blush false", text="Я...")
    call process_character (julia, appearance="blush false", text="Я в порядке.")
    call process_character (julia, appearance="blush false", text="Просто дай мне несколько минут.")
    call process_character (julia, appearance="blush false", text="{i}Уфф.{/i}..")
    call process_character (n, appearance="blush false", text="Я никогда раньше тебя не видел тебя такой!")
    call process_character (n, appearance="blush false", text="Ты говорила какие-то сумасшедшие вещи!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Я не ожидала, что анал будет чувствоваться так...")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Н-но, возможно, это была просто случайность!")
    call process_character (n, appearance="blush false", text="Хм, может быть...")
    call process_character (n, appearance="blush false", text="Ты думаешь, нам стоит повторить?")
    call process_character (julia, appearance="blush false", text="Да!")
    call process_character (julia, appearance="blush false", text="Мы должны сделать это снова!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Я... я имею в виду, мы должны снова заняться анальным сексом, чтобы убедиться случайность ли то, что ты почувствовала!")
    call process_character (julia, appearance="blush false", text="Может быть, попробуем еще несколько раз, чтобы быть уверенными!")
    call process_character (n, appearance="blush false", text="Ох, э-э...")
    call process_character (n, appearance="blush false", text="Конечно!")
    call process_character (n, appearance="blush false", text="Я не возражаю!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Можешь принести мне полотенце?")
    call process_character (julia, appearance="blush false", text="Сперма бежит по моей ноге...")

    python:
        julia.revistable_scenes.add("julia_scene_anal_revisit")

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

    call process_end_of_scene ("julia_scene_anal", char=julia, dream=dream)

    return

label julia_scene_anal_revisit:
    if "julia_scene_anal_revisit" not in scenes_completed:
        jump julia_scene_anal_revisit_1st_time
    else:
        jump julia_scene_anal_revisit_2nd_time

    return



label julia_scene_anal_revisit_1st_time:
    $ no_bust_art = False
    $ display_multiple_characters([ (n, "pose twohandfist face neutral"), (julia, "pose handface face flirty blush false") ])

    call process_character (julia, appearance="blush false", text="Я собиралась спросить тебя об этом.")
    call process_character (julia, appearance="blush false", text="Я хочу убедиться, как оно будет во второй раз.")

    python hide:
        play_music("audio/music/Suave Standpipe.ogg", fadein = 1.0)

    call static_still_ctc ("bg julia_anal_onfloor")

    call process_character (julia, appearance="blush false", text="Как раньше, правильно?")
    call process_character (n, appearance="blush false", text="Как тогда, да.")
    call process_character (julia, appearance="blush false", text="Я не готова попробовать какую-то сложную позу для анального секса.")
    call process_character (julia, appearance="blush false", text="Это даст то, чего мы оба хотим.")

    call static_still_ctc ("bg julia_anal_butthole_dicktouch")

    call process_character (n, appearance="blush false", text="Должен ли я войти медленно, как раньше?")
    call process_character (julia, appearance="blush false", text="Да.")
    call process_character (julia, appearance="blush false", text="Но толкай сильнее, чем в первый раз.")
    call process_character (julia, appearance="blush false", text="Я хочу прямо сейчас!")

    call static_still_ctc ("bg julia_anal_butthole_pushin")

    call process_character (n, appearance="blush false", text="Вот так?")
    call process_character (julia, appearance="blush false", text="Мм, ах...")
    call process_character (julia, appearance="blush false", text="Еще чуть-чуть...")
    call process_character (n, appearance="blush false", text="Он медленно движется!")
    call process_character (julia, appearance="blush false", text="В любой момент...")

    call static_still_ctc ("bg julia_anal_butthole_allin")

    call process_character (julia, appearance="blush false", text="Ох, он вошел!")
    call process_character (julia, appearance="blush false", text="(Моя задница уже пульсирует!)")
    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (n, appearance="blush false", text="На этот раз член вошёл немного быстрее...")
    call static_still_ctc ("bg julia_anal_fuck")

    call process_character (n, appearance="blush false", text="Хуу!")
    call process_character (n, appearance="blush false", text="Я думаю, она чувствует себя потрясающе!")
    call process_character (julia, appearance="blush false", text="Охренеть!")
    call process_character (julia, appearance="blush false", text="Ах, черт!")
    call process_character (julia, appearance="blush false", text="Продолжай ускоряться!")
    call process_character (n, appearance="blush false", text="Не проблема!")
    call process_character (n, appearance="blush false", text="Мое тело хочет двигаться быстрее!")
    call process_character (julia, appearance="blush false", text="Ммм, ой, аах!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Я чувствую себя такой первобытной во время этого!)")
    call process_character (julia, appearance="blush false", text="(Это сырой всплеск похоти в моей душе!)")
    call process_character (julia, appearance="blush false", text="{i}Задыхается!{/i}")
    call process_character (julia, appearance="blush false", text="(Трахай, [n.say_name], меня глубже!)")
    call process_character (n, appearance="blush false", text="...")

    if "sam_scene_anal" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Я должен спросить, захочет ли [sa.say_name] принять такую позу)")
        call process_character (n, appearance="blush false", text="(Бьюсь об заклад, эта поза понравится так же, как и [julia.say_name]!)")
        call process_character (n, appearance="blush false", text="([sa.say_name], вероятно, захочет сфотографировать, как я сую член в ей задницу, чтобы она могла это увидеть...)")
    elif "kira_scene_anal" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Эта поза немного напоминает мне, когда [k.say_name] позволяла мне трахать её между ягодиц...)")
        call process_character (n, appearance="blush false", text="(Но когда мы занимались аналом, она просто сидела на мне!)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Было весело, когда она вставала и опускалась на мой пенис, хотя...)")
    elif "simone_scene_anal" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Мы с Мамой занимались сексом в такой же позе)")
        call process_character (n, appearance="blush false", text="(Я помню, мама позволяла мне опираться на нее)")
        call process_character (n, appearance="blush false", text="(Я думаю, [julia.say_name] разозлится, если я попробую это...)")
        call process_character (n, appearance="blush false", text="(Она, вероятно, упадет на землю из моего веса)")

    call process_character (julia, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (julia, appearance="blush false", text="[n.say_name]...")
    call process_character (julia, appearance="blush false", text="После лета ты будешь заходить ко мне домой.")
    call process_character (julia, appearance="blush false", text="Ах, оох!")
    call process_character (julia, appearance="blush false", text="Запланируй, по крайней мере, раз в неделю!")

    if "janet_scene_blowjob" in scenes_completed:
        call process_character (julia, appearance="blush false", text="Это не должно быть проблемой, поскольку ты уже много раз ездил ко мне домой!")
        call process_character (n, appearance="blush false", text="Школа может это затруднить...")
        call process_character (julia, appearance="blush false", text="Ты должен что-нибудь придумать, [n.say_name]!")
        call process_character (julia, appearance="blush false", text="Мм!")
        call process_character (julia, appearance="blush false", text="Нам нужно трахаться в осенью, зимой и после!")
    else:
        call process_character (n, appearance="blush false", text="Надеюсь, я смогу придумать...")
        call process_character (julia, appearance="blush false", text="Ты должен что-нибудь придумать, [n.say_name]!")
        call process_character (julia, appearance="blush false", text="Мм!")
        call process_character (julia, appearance="blush false", text="Нам нужно трахаться в осенью, зимой и после!")

    call process_character (n, appearance="blush false", text="Может быть, одну неделю ты будешь приходить ко мне, а на следующую я.")
    call process_character (julia, appearance="blush false", text="Значит, будем чередоваться?")
    call process_character (julia, appearance="blush false", text="Ахх!")
    call process_character (julia, appearance="blush false", text="Д-да, это может сработать.")
    call process_character (n, appearance="blush false", text="Ох, ох!")
    call process_character (n, appearance="blush false", text="(Анус [julia.say_name] сильно сжимает мой член!)")
    call process_character (julia, appearance="blush false", text="(Член [n.say_name] такой величины, с которой я могу справиться!)")
    call process_character (julia, appearance="blush false", text="(Его член занимает все пространство в моей заднице!)")
    call process_character (julia, appearance="blush false", text="Аах!")
    call process_character (n, appearance="blush false", text="Позволь мне снова кончить в твою задницу, [julia.say_name]!")
    call process_character (julia, appearance="blush false", text="Аах, Мм!")
    call process_character (n, appearance="blush false", text="Я действительно хочу это!")
    call process_character (julia, appearance="blush false", text="Я не останавливаю тебя!")
    call process_character (julia, appearance="blush false", text="Д-делай, что тебе нравится, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Я собираюсь засунуть член до самого основания!")
    call process_character (n, appearance="blush false", text="Начинаю!")
    call process_character (n, appearance="blush false", text="Хннг!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg julia_anal_fuck_cuminside")

    call process_character (julia, appearance="blush false", text="Хьяяя!")
    call process_character (julia, appearance="blush false", text="Слишком много!{p}Слишком много!")

    call static_still_ctc ("bg julia_anal_fuck_cum")

    call process_character (n, appearance="blush false", text="Я кончил больше, чем думал!")
    call process_character (julia, appearance="blush false", text="Хорошо, что ты, {i}вздох,{/i} {w=0.5}вытащил!")
    call process_character (julia, appearance="blush false", text="Моя задница была готова взорваться!")

    call static_still_ctc ("bg julia_anal_aftercum")

    call process_character (n, appearance="blush false", text="сперма прямо выстреливает из твоей задницы!")
    call process_character (julia, appearance="blush false", text="Я... я знаю!")
    call process_character (julia, appearance="blush false", text="Я пытаюсь вытолкнуть её!")
    call process_character (julia, appearance="blush false", text="Твоя сперма настолько густая, что это сложно сделать!")
    call process_character (n, appearance="blush false", text="Может быть, мне тогда не стоило кончать в твою задницу...")
    call process_character (julia, appearance="blush false", text="Нет!")
    call process_character (julia, appearance="blush false", text="Продолжай делать это!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Я не хочу упустить то чувство, когда горячая сперма льется в мою задницу!")
    call process_character (julia, appearance="blush false", text="Это просто компромисс, с которым я должна жить дальше!")

    jump julia_scene_anal_revisit_end

    return

label julia_scene_anal_revisit_2nd_time:
    python hide:
        play_music("audio/music/Suave Standpipe.ogg", fadein = 1.0)

    call static_still_ctc ("bg julia_anal_fuck")

    call process_character (julia, appearance="blush false", text="Ммм, да!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Теперь я контролирую себя, когда делаю это...)")
    call process_character (julia, appearance="blush false", text="Трахни!")
    call process_character (julia, appearance="blush false", text="Еб..ть, трахни меня, [n.say_name]!")
    call process_character (julia, appearance="blush false", text="(Может быть, не так сильно контролирую, как я думала!)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Я звучу как грязная шлюха, когда я это делаю!)")
    call process_character (julia, appearance="blush false", text="(Клянусь, если [n.say_name] расскажет кому-то, как я веду себя во время анала...)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Надо просто попросить его, чтобы он дал клятву молчания об этом)")
    call process_character (julia, appearance="blush false", text="(И если он нарушит её, то я не буду больше трахаться с ним!)")
    call process_character (julia, appearance="blush false", text="(Есть вероятность, что [n.say_name] оговорится!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я надеюсь, что [sa.say_name] надевает наушники в своей комнате)")
    call process_character (n, appearance="blush false", text="([julia.say_name] слишком громкая во время этого...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Если бы мы были на моей кровати, то она бы сильно ударялась об стену)")
    call process_character (julia, appearance="", text="...")
    call process_character (julia, appearance="", text="([n.say_name] трахнул все мои дырки)")
    call process_character (julia, appearance="", text="(Я не давала в рот, в киску и в задницу никому, кроме моего кузена)")
    call process_character (julia, appearance="", text="(Немного странно думать об этом)")
    call process_character (julia, appearance="", text="(Но пока не появился кто-то лучше, и я сомневаюсь, что это произойдет...)")
    call process_character (julia, appearance="", text="(Я смирилась с тем, что я трахаюсь с кровным родственником!)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", xalign = 0.5, yalign = 0.1)
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg julia_anal_fuck_cuminside")

    call process_character (n, appearance="blush false", text="Ааах...")
    call process_character (julia, appearance="blush false", text="Ммммм!")
    call process_character (julia, appearance="blush false", text="(Я получаю оргазм каждый раз, когда это происходит!)")

    call static_still_ctc ("bg julia_anal_fuck_cum")

    call process_character (n, appearance="blush false", text="{i}Фьюю.{/i}..")
    call process_character (julia, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (julia, appearance="blush false", text="Мне надо отдохнуть на твоей кровати после этого, [n.say_name]!")

    jump julia_scene_anal_revisit_end
    return

label julia_scene_anal_revisit_end:
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

    call process_end_of_scene ("julia_scene_anal_revisit", char=julia, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return