init python:
    def gloryhole_handjob_xray():
        store.gloryhole_handjob_xray_on = not store.gloryhole_handjob_xray_on
        
        if store.gloryhole_handjob_xray_on:
            renpy.show("bg gloryhole_handjob_stall_transparent", tag = "bg")
        else:
            renpy.show("bg gloryhole_handjob_stall_opaque", tag = "bg")
        
        return

    def gloryhole_blowjob_xray():
        store.gloryhole_blowjob_xray_on = not store.gloryhole_blowjob_xray_on
        
        if store.gloryhole_blowjob_xray_on:
            renpy.show("bg kacey_blowjob_throughwall_x-ray", tag = "bg")
        else:
            renpy.show("bg kacey_blowjob_throughwall", tag = "bg")
        
        return

screen gloryhole_handjob_xray:
    use main_menu_button(text="Рентген", action=Function(gloryhole_handjob_xray), xalign=0.010, yalign=0.5 )

screen gloryhole_blowjob_xray:
    use main_menu_button(text="Рентген", action=Function(gloryhole_blowjob_xray), xalign=0.03, yalign=0.05 )

label gloryhole_handjob_scene(dream=False):
    call gloryhole_handjob_scene_sex (dream=dream)

    return

label gloryhole_handjob_scene_sex(dream=False):
    $ renpy.scene('screens')
    if dream:
        show screen dream_blur

    $ no_bust_art = False
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="(Я впомнил, что рядом с нашим домом есть парк)")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy", text="(Было бы здорово сходить туда!)")

    if store.week.time != "night":
        $ store.week.time = "night"
        call process_character (n, appearance="outfit clothesjacket pose handfist face happy", text="(Я отправлюсь туда сегодня вечером!)")
    else:
        call process_character (n, appearance="outfit clothesjacket pose handfist face happy", text="(Думаю, я отправлюсь прямо сейчас!)")


    call process_scene_beginning (bg=park, char_tuple_array=[ (n, "outfit clothesjacket pose twohandfist face happy") ], dream=dream )

    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy", text="(Весь парк в моём распоряжении!)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="(Здесь тихо и спокойно)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="(Все, что я слышу, это стрёкот жучков)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="{i}Фуух{/i}...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral", text="(Этот парк довольно большой)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="(Но все дорожки хорошо освещены)")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral", text="(И с этими указателями очень легко найти дорогу обратно)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious", text="Мм?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious", text="(Похоже, впереди туалет)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious", text="...")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face concerned", text="(Теперь, когда я вижу его, я хочу...)")

    call fade_to_black (1.0, do_not_show_quick_menu=True)
    show bg public_bathroom_evening
    with Dissolve(0.5)
    $ no_bust_art = False
    pause 0.5
    $ quick_menu = True
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="(Эта туалет не так уж плох!)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious", text="(Хотя, похоже, что некоторые унитазы не работают)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy", text="(Кабинка в конце открыта!)")

    window hide
    $ quick_menu = False
    $ clear_characters()
    show bg black
    with Dissolve(0.5)
    pause 1.0
    call static_still_ctc ("bg gloryhole")

    call process_character (n, text="(Ах, как хорошо!)")
    call process_character (n, text="(Плохо было бы его не найти)")
    call process_character (n, text="...")
    call process_character (n, text="Что здесь делает эта дыра?")

    "{color=#FDDF7D}Женский Голос{/color}" "Ты хочешь узнать?"
    call process_character (n, text="...")
    call process_character (n, text="Кто это сказал?")
    "{color=#FDDF7D}Женский Голос{/color}" "Эй там!"
    "{color=#FDDF7D}Женский Голос{/color}" "Я в кабинке рядом с тобой."
    call process_character (n, text="Ух...")
    call process_character (n, text="Привет.")
    "{color=#FDDF7D}Женский Голос{/color}" "Я услышала твой милый голос."
    "{color=#FDDF7D}Женский Голос{/color}" "Ты новенький?"
    call process_character (n, text="...")
    call process_character (n, text="Даа...")
    call process_character (n, text="Я переехал сюда недавно.")
    "{color=#FDDF7D}Женский Голос{/color}" "Замечательно!"
    "{color=#FDDF7D}Женский Голос{/color}" "Ты осматривал парк?"
    call process_character (n, text="Э, да...")
    "{color=#FDDF7D}Женский Голос{/color}" "Это отличный парк."
    "{color=#FDDF7D}Женский Голос{/color}" "Но не так много людей ходят здесь ночью."
    call process_character (n, text="...")
    call process_character (n, text="Ты говоришь так, будто ты девушка.")
    "{color=#FDDF7D}Женский Голос{/color}" "Да, я девушка."
    call process_character (n, text="Но...")
    call process_character (n, text="Разве это не мужской туалет?")
    "{color=#FDDF7D}Женский Голос{/color}" "Этот?"
    "{color=#FDDF7D}Женский Голос{/color}" "Ууупс!"
    "{color=#FDDF7D}Женский Голос{/color}" "Должно быть, я неправильно поняла знак."
    call process_character (n, text="Ой...")
    call process_character (n, text="...{p}...")
    "{color=#FDDF7D}Женский Голос{/color}" "Так тебе была интересна эта дыра?"
    call process_character (n, text="Она необычная.")
    "{color=#FDDF7D}Женский Голос{/color}" "Знаешь, для чего она используется?"
    call process_character (n, text="Без понятия.")
    "{color=#FDDF7D}Женский Голос{/color}" "Не хочешь узнать?"
    "{color=#FDDF7D}Женский Голос{/color}" "О, ты такое упускаешь!"
    "{color=#FDDF7D}Женский Голос{/color}" "Ты должен попробовать!"
    call process_character (n, text="Попробовать?")
    call process_character (n, text="Как мне это попробовать?")
    "{color=#FDDF7D}Женский Голос{/color}" "Легко!"
    "{color=#FDDF7D}Женский Голос{/color}" "Просто вставь туда свой член!"
    call process_character (n, text="М-мой пенис?!")
    call process_character (n, text="...")
    call process_character (n, text="Что произойдет, если я это сделаю?")
    "{color=#FDDF7D}Женский Голос{/color}" "Нуу..."
    "{color=#FDDF7D}Женский Голос{/color}" "Что-то весёлое произойдёт!"
    call process_character (n, text="...")
    call process_character (n, text="Я не знаю.")
    "{color=#FDDF7D}Женский Голос{/color}" "Ты никогда не узнаешь, если не попробуешь..."
    call process_character (n, text="...{p}...")
    call process_character (n, text="(Немного странно делать это...)")
    call process_character (n, text="...")
    call process_character (n, text="Если мне не понравится, могу я вытащить свой пенис?")
    "{color=#FDDF7D}Женский Голос{/color}" "Конечно."
    "{color=#FDDF7D}Женский Голос{/color}" "(Я сомневаюсь, что ты захочешь)"
    call process_character (n, text="...{p}...")
    call process_character (n, text="Х-хорошо, я вставлю свой пенис.")

    call static_still_ctc ("bg gloryhole_sticks_dick_through")

    "{color=#FDDF7D}Женский Голос{/color}" "..."
    "{color=#FDDF7D}Женский Голос{/color}" "{i}Вздох!{/i}"
    call process_character (n, text="Ч-что?")
    "{color=#FDDF7D}Женский Голос{/color}" "У тебя такой милый пенис!"
    call process_character (n, text="ой...")
    call process_character (n, text="С-спасибо.")
    "{color=#FDDF7D}Женский Голос{/color}" "(Я нашла золотую жилу!)"
    "{color=#FDDF7D}Женский Голос{/color}" "(Это самый молодой пенис, который я видела!)"
    "{color=#FDDF7D}Женский Голос{/color}" "(Надеюсь, мне это не снится!)"

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg gloryhole_touches_dick")

    call process_character (n, text="А, ч-что ты делаешь?")
    "{color=#FDDF7D}Женский Голос{/color}" "(Выглядит совершенно нетронутым!)"
    "{color=#FDDF7D}Женский Голос{/color}" "(И такой гладкий)"
    "{color=#FDDF7D}Женский Голос{/color}" "..."
    "{color=#FDDF7D}Женский Голос{/color}" "(Он уже твердеет?)"
    "{color=#FDDF7D}Женский Голос{/color}" "(О, какой потенциал у этого парня...)"
    call process_character (n, text="Ах...")
    call process_character (n, text="(Такое чувство, что ее пальцы двигаются вдоль моего пениса!)")
    call process_character (n, text="(Я чувствую, как он становится...)")

    call static_still_ctc ("bg gloryhole_handjob")

    "{color=#FDDF7D}Женский Голос{/color}" "!!!"
    "{color=#FDDF7D}Женский Голос{/color}" "(Посмотрите на эту реакцию!)"
    "{color=#FDDF7D}Женский Голос{/color}" "(Он знает, что чувствует себя хорошо!)"
    "{color=#FDDF7D}Женский Голос{/color}" "Хорошо, хорошо..."
    call process_character (n, text="Ахх...")
    call process_character (n, text="М-мой пенис...")
    call process_character (n, text="Становится твёрдым.")
    "{color=#FDDF7D}Женский Голос{/color}" "Именно так."
    "{color=#FDDF7D}Женский Голос{/color}" "И так быстро!"
    "{color=#FDDF7D}Женский Голос{/color}" "Это значит, что тебе это нравится, не так ли?"
    call process_character (n, text="М-мне приятно...")
    "{color=#FDDF7D}Женский Голос{/color}" "(Ну, если он думает, что это приятно...)"
    "{color=#FDDF7D}Женский Голос{/color}" "(Что ты скажешь на это!)"

    call static_still_ctc ("bg gloryhole_handjob_stall_opaque")

    $ gloryhole_handjob_xray_on = False
    show screen gloryhole_handjob_xray

    "{color=#FDDF7D}Женский Голос{/color}" "Да-ха-ха!"
    call process_character (n, text="Ах, ах, ах!")
    call process_character (n, text="Над чем это ты смеешься?")
    "{color=#FDDF7D}Женский Голос{/color}" "Ха, ну я просто ..."
    "{color=#FDDF7D}Женский Голос{/color}" "Твой пенис прямо подпрыгивает!"
    "{color=#FDDF7D}Женский Голос{/color}" "..."
    "{color=#FDDF7D}Женский Голос{/color}" "(Сейчас парень получит дьявольскую дрочку)"
    "{color=#FDDF7D}Женский Голос{/color}" "(Но я ничего не могу с этим поделать!)"
    "{color=#FDDF7D}Женский Голос{/color}" "(Как часто я ещё смогу его петушка отшлёпать?)"
    call process_character (n, text="Ах! Ух...")
    call process_character (n, text="(Она ведет себя немного грубо!)")
    call process_character (n, text="(Но это тоже не плохо)")
    "{color=#FDDF7D}Женский Голос{/color}" "Как ты там?"
    call process_character (n, text="Ах, мм...")
    call process_character (n, text="Я, ах...")
    call process_character (n, text="Я ... Я думаю, что задержусь здесь еще немного.")
    "{color=#FDDF7D}Женский Голос{/color}" "(Попался!)"
    "{color=#FDDF7D}Женский Голос{/color}" "...{p}..."
    "{color=#FDDF7D}Женский Голос{/color}" "(Он всё ещё держится, я удивлена)"
    "{color=#FDDF7D}Женский Голос{/color}" "(Я была уверена, что сейчас он-)"
    call process_character (n, text="Ах, ох...")
    call process_character (n, text="Ахх...")
    call process_character (n, text="Аххх!")

    hide screen gloryhole_handjob_xray

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg gloryhole_handjob_cum")

    "{color=#FDDF7D}Женский Голос{/color}" "(Ой, поторопилась )"
    "{color=#FDDF7D}Женский Голос{/color}" "..."
    "{color=#FDDF7D}Женский Голос{/color}" "(Срань Господня!)"
    "{color=#FDDF7D}Женский Голос{/color}" "(Сколько я могу выжать из него?)"
    "{color=#FDDF7D}Женский Голос{/color}" "(Возьму всё до {w=0.5}последней {w=0.5}капли)"
    call process_character (n, text="Т-ты сжимаешь сильно!")
    "{color=#FDDF7D}Женский Голос{/color}" "Моя вина."
    "{color=#FDDF7D}Женский Голос{/color}" "Ты должен выжать из себя всё до последней капли."
    "{color=#FDDF7D}Женский Голос{/color}" "..."
    "{color=#FDDF7D}Женский Голос{/color}" "Итак..."
    "{color=#FDDF7D}Женский Голос{/color}" "Тебе понравилось?"
    call process_character (n, text="Д-да.")
    "{color=#FDDF7D}Женский Голос{/color}" "Эта дыра забавная, не так ли?"
    call process_character (n, text="Я и не знал, что все будет именно так.")
    call process_character (n, text="Но мне понравилось.")
    "{color=#FDDF7D}Женский Голос{/color}" "(Тут я согласна, вся рука обрызгана)"
    "{color=#FDDF7D}Женский Голос{/color}" "..."
    "{color=#FDDF7D}Женский Голос{/color}" "Ну..."
    "{color=#FDDF7D}Женский Голос{/color}" "Надеюсь увидеть тебя здесь снова."
    call process_character (n, text="Прямо здесь?")
    "{color=#FDDF7D}Женский Голос{/color}" "Почему нет?"
    "{color=#FDDF7D}Женский Голос{/color}" "Никто не беспокоит нас, и мы можем хорошо провести время вместе!"
    call process_character (n, text="Как я узнаю, что ты здесь?")
    "{color=#FDDF7D}Женский Голос{/color}" "Легко!"
    "{color=#FDDF7D}Женский Голос{/color}" "Просто назови мое имя, [gloryhole_girl.say_name]."
    call process_character (gloryhole_girl, text="...")
    call process_character (gloryhole_girl, text="Кстати об именах, а как тебя зовут?")

    call process_character (n, text="Ох...")
    call process_character (n, text="М-меня зовут, [n.say_name].")
    call process_character (gloryhole_girl, text="[n.say_name]...")
    call process_character (gloryhole_girl, text="Мне нравится имя.")
    call process_character (gloryhole_girl, text="Хорошо, [n.say_name].")
    call process_character (gloryhole_girl, text="Надеюсь увидеть тебя снова очень скоро!")
    call process_character (gloryhole_girl, text="В следующий раз у меня для тебя будет новый сюрприз...")

    python:
        gloryhole_girl.revistable_scenes.add("gloryhole_handjob_scene_revisit")

        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_received_handjob", 1)
            stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene ("gloryhole_handjob_scene", char=gloryhole_girl, dream=dream)

    return


label gloryhole_handjob_scene_revisit():
    call process_scene_beginning (bg="bg gloryhole_sticks_dick_through" )

    call process_character (gloryhole_girl, text="А ты не теряешь время!")
    call process_character (gloryhole_girl, text="Вот как мне это нравится!")
    call process_character (gloryhole_girl, text="(Его член такой пленительный)")
    call process_character (gloryhole_girl, text="(Он с нетерпением ждет меня)")

    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg gloryhole_touches_dick")

    call process_character (n, text="Ахх!")
    call process_character (gloryhole_girl, text="Моя ошибка, мои руки немного холодные.")
    call process_character (gloryhole_girl, text="Скоро они разогреются.")
    call process_character (n, text="(Это холодное прикосновение было приятно...)")
    call process_character (n, text="(Меня даже в дрожь бросило)")
    call process_character (gloryhole_girl, text="Ах да, твой член тёпленький!")
    call process_character (gloryhole_girl, text="Идеально подходит для девушки, чтобы согреть её пальцы!")
    call process_character (gloryhole_girl, text="...")
    call process_character (gloryhole_girl, text="Дай мне согреться!")

    call static_still_ctc ("bg gloryhole_handjob_stall_opaque")

    $ gloryhole_handjob_xray_on = False
    show screen gloryhole_handjob_xray

    call process_character (gloryhole_girl, text="Ммм...")
    call process_character (gloryhole_girl, text="(Мне нравится звук, который издаёт его член, когда я дрочу ему)")
    call process_character (gloryhole_girl, text="(Я слышу эхо в кабинке)")
    call process_character (n, text="{i}Вздох{/i}...")
    call process_character (n, text="(То, как она сжимает и двигает рукой...)")

    if "simone_scene_1_seq_1" in scenes_completed or stats.stat_value('times_fapped') > 0:
        call process_character (n, text="(Э-это намного сильнее, чем, когда я хватал свой пенис)")

    if "gloryhole_handjob_scene_revisit" not in scenes_completed:
        call process_character (n, text="Ах, ох!")
        call process_character (gloryhole_girl, text="...")
        call process_character (gloryhole_girl, text="Ты когда-нибудь дрочил раньше?")
        call process_character (n, text="Д-дрочил?")
        call process_character (gloryhole_girl, text="Ну ты знаешь, делать то, что делаю я, но в одиночку?")

        if "simone_scene_1_seq_1" in scenes_completed or stats.stat_value('times_fapped') > 0:
            call process_character (n, text="Я-я делал это раньше.")
            call process_character (gloryhole_girl, text="Как это может сравниться с этим?")
            menu:
                "Э-это лучше.":
                    call process_character (gloryhole_girl, text="Я надеюсь на это.")
                    call process_character (gloryhole_girl, text="Не стоило бы и делать, если бы это было не так, верно?")
                "Ты делаешь это лучше, чем я!":
                    call add_boldness (1, tag="gloryhole_handjob_scene_revisit_do_it_way_better")
                    call process_character (gloryhole_girl, text="Приятно слышать!")
                    call process_character (gloryhole_girl, text="Будет трудно вернуться к работе в одиночку, не так ли?")
        else:
            call add_boldness (2, tag="gloryhole_handjob_scene_revisit_never_done_it_before")
            call process_character (n, text="Я никогда не делал ничего подобного раньше.")
            call process_character (gloryhole_girl, text="Ты хочешь сказать, что даже не трогал себя раньше?")
            call process_character (gloryhole_girl, text="(Это джек-пот!)")
            call process_character (gloryhole_girl, text="(Подрочить член, прежде чем его владелец сам сделает это!)")
            call process_character (gloryhole_girl, text="(Сколько девушек могут претендовать на это?!)")
            call process_character (gloryhole_girl, text="(Я могу, вот кто...)")

    call process_character (n, text="Аах, ах...")
    call process_character (gloryhole_girl, text="Не кончай пока что!")
    call process_character (gloryhole_girl, text="Мне нужно еще немного времени.")
    call process_character (gloryhole_girl, text="...")
    call process_character (gloryhole_girl, text="(Хорошо, больше, чем немного)")
    call process_character (gloryhole_girl, text="Чем дольше ты держишься, тем больше удовольствие!")
    call process_character (n, text="Д-да...")
    call process_character (n, text="Ахх…")
    call process_character (n, text="Я старюсь...")
    call process_character (gloryhole_girl, text="Продолжай стараться!")
    call process_character (gloryhole_girl, text="...")
    call process_character (gloryhole_girl, text="(Нельзя мучить ребенка слишком долго)")
    call process_character (gloryhole_girl, text="(Когда ты готов кончить, ты кончаешь)")
    call process_character (n, text="Ах, ах...")
    call process_character (n, text="Ахх, Ахх...")
    call process_character (gloryhole_girl, text="Ты чувствуешь, что тебе нужно выпустить?")
    call process_character (gloryhole_girl, text="{cps=40}Готов ли ты кон- {/cps}{w=0.75}{nw}")

    hide screen gloryhole_handjob_xray

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg gloryhole_handjob_cum")

    call process_character (n, text="Хах, ах! Ах!")
    call process_character (gloryhole_girl, text="Ууу, я почти пропустила это!")
    call process_character (gloryhole_girl, text="(Он должен быть вполне здоров, чтобы столько кончить!)")
    call process_character (n, text="{i}Вздох, вздох{/i}...")
    call process_character (gloryhole_girl, text="Чувствуешь себя без сил?")
    call process_character (n, text="Д-да.")
    call process_character (gloryhole_girl, text="Ну, мы же не хотим, чтобы ты упал в унитаз от усталости.")
    call process_character (gloryhole_girl, text="Ты должен идти домой.")
    call process_character (n, text="Ага.")
    call process_character (gloryhole_girl, text="Рада буду снова тебя видеть, [n.say_name].")
    call process_character (gloryhole_girl, text="Если тебе когда-нибудь понадобится облегчение, ты знаешь, где меня найти.")
    call process_character (n, text="С-Спасибо, [gloryhole_girl.say_name].")
    call process_character (gloryhole_girl, text="Не забудь засунуть свой член обратно в штаны!")
    call process_character (gloryhole_girl, text="Ты же не хочешь, чтобы он хлопал на ветру!")

    python:
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_received_handjob", 1)
        stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene ("gloryhole_handjob_scene_revisit", char=gloryhole_girl, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label gloryhole_scene_blowjob(dream=False):
    call gloryhole_scene_blowjob_sex (dream=dream)
    return

label gloryhole_scene_blowjob_sex(dream=False):
    call process_scene_beginning (bg="bg gloryhole", dream=dream )
    $ no_bust_art = True

    call process_character (gloryhole_girl, appearance="", text="Ты как всегда вовремя, [n.say_name]!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Ага...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Мне нравится следовать расписанию.")
    call process_character (gloryhole_girl, appearance="", text="Это хорошее качество, знаешь!")
    call process_character (gloryhole_girl, appearance="", text="Рациональное использование времени не такое простое дело.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Моя семья довольно организованна.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Особенно моя мама.")
    call process_character (gloryhole_girl, appearance="", text="Кстати о семье.")
    call process_character (gloryhole_girl, appearance="", text="Ты единственный ребенок?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Нет.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Я живу со своими двумя сестрами и моей мамой.")
    call process_character (gloryhole_girl, appearance="", text="О, вау, единственный мальчик в доме, да?")
    call process_character (gloryhole_girl, appearance="", text="Каково это?")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Я никогда над этим не задумывался.")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Я играю в видеоигры с моей сестрой-близнецом.")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="И моя старшая сестра любит тренироваться со мной на беговой дорожке.")
    call process_character (gloryhole_girl, appearance="", text="Значит, ты хорошо ладишь со своими сестрами?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="О, да!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="С ними весело проводить время.")
    call process_character (gloryhole_girl, appearance="", text="Замечательно!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Что на счёт тебя?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="У тебя есть братья или сестры?")
    call process_character (gloryhole_girl, appearance="", text="Нет, я была единственным ребёнком.")
    call process_character (gloryhole_girl, appearance="", text="Не было братьев или сестер для компании.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Я не знаю, что бы я сделал, если бы у меня не было сестер.")
    call process_character (gloryhole_girl, appearance="", text="Было бы здорово иметь младшего брата!")
    call process_character (gloryhole_girl, appearance="", text="Я бы делала с ним все, что делаю с тобой.")

    if "kira_scene_3" in scenes_completed:
        call process_character (n, appearance="pose behindhead face neutral blush false", text="На самом деле, моя старшая сестра делает такие вещи со мной.")
        call process_character (gloryhole_girl, appearance="", text="Да?")
        call process_character (gloryhole_girl, appearance="", text="Она самая лучшая сестра!")
        call process_character (gloryhole_girl, appearance="", text="Ты так не думаешь?")
        call process_character (n, appearance="pose handpocket face neutral blush false", text="Это очень весело...")
        call process_character (gloryhole_girl, appearance="", text="Она не собирается съезжать или что-нибудь подобное?")
        call process_character (n, appearance="pose handfist face neutral blush false", text="О нет, она живёт дома с моей мамой и сестрой!")
        call process_character (gloryhole_girl, appearance="", text="Приятно слышать!")
        call process_character (gloryhole_girl, appearance="", text="Так что у тебя будет достаточно времени, чтобы насладиться ею!")
    elif "sam_scene_2_seq_2" not in scenes_completed:
        call process_character (n, appearance="blush false", text="Мои сестры не делают со мной такого рода вещи.")
        call process_character (gloryhole_girl, appearance="", text="О, не повезло.")
        call process_character (gloryhole_girl, appearance="", text="Если бы я была твоей сестрой, я бы веселилась с тобой каждый день!")

    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ты наслаждался солнцем сегодня?")
    call process_character (gloryhole_girl, appearance="", text="Ты знаешь, да!")
    call process_character (gloryhole_girl, appearance="", text="Это был прекрасный день!")
    call process_character (n, appearance="blush false", text="Определенно!")
    call process_character (n, appearance="blush false", text="Я сходи в бассейн пораньше.")
    call process_character (gloryhole_girl, appearance="", text="Я пыталась добраться до пляжа, но он был закрыт!")
    call process_character (gloryhole_girl, appearance="", text="Поэтому вместо этого я гуляла по парку.")
    call process_character (gloryhole_girl, appearance="", text="Дул легкий ветерок.")
    call process_character (gloryhole_girl, appearance="", text="Плюс было тихо.")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="Но знаешь, что случилось?")
    call process_character (n, appearance="blush false", text="Что?")
    call process_character (gloryhole_girl, appearance="", text="Я забыла взять с собой воды.")
    call process_character (gloryhole_girl, appearance="", text="Так что я умираю от жажды!")
    call process_character (n, appearance="blush false", text="Ты могла выпить воды из фонтанчика.")
    call process_character (gloryhole_girl, appearance="", text="Вода это, конечно, хорошо, но...")
    call process_character (gloryhole_girl, appearance="", text="Я знаю кое-что, что лучше воды.")
    call process_character (n, appearance="blush false", text="Да?")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg kacey_blowjob_mouth_nocum")

    call process_character (gloryhole_girl, appearance="", text="Твоя сперма утолит мою жажду!")
    call process_character (n, appearance="blush false", text="М-моя сперма?")
    call process_character (gloryhole_girl, appearance="", text="Этот белая, липкая штука, которая выходит из твоего члена, да.")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (gloryhole_girl, appearance="", text="Почему бы тебе не вставить свой член в отверстие?")
    call process_character (n, appearance="blush false", text="Где твой рот?")
    call process_character (gloryhole_girl, appearance="", text="Точно.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="О-окей.")
    call process_character (gloryhole_girl, appearance="", text="Тебе понравится, я обещаю!")
    call process_character (gloryhole_girl, appearance="", text="Это принесет пользу обоим из нас!")

    call fade_to_black (1)

    if stats.stat_value('times_received_blowjob') > 0:
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Думаю, я знаю, что [gloryhole_girl.say_name] хочет сделать...)")
        call process_character (n, appearance="blush false", text="...")

        if "kira_scene_tip_blowjob" in scenes_completed or "kira_scene_stealth_bj" in scenes_completed:
            call process_character (n, appearance="blush false", text="([k.say_name] сосала у меня раньше...)")
        elif "simone_scene_blowjob" in scenes_completed:
            call process_character (n, appearance="blush false", text="(Мама сосала у меня раньше...)")
        elif "sam_scene_blowjob" in scenes_completed:
            call process_character (n, appearance="blush false", text="([sa.say_name] сосала у меня раньше...)")
        elif "julia_scene_blowjob" in scenes_completed:
            call process_character (n, appearance="blush false", text="([julia.say_name] сосала у меня раньше...)")
        else:
            pass
    else:
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Она действительно хочет, чтобы я вставил свой член в ее рот?)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Интересно, каково это ...)")


    $ gloryhole_blowjob_xray_on = False
    call static_still_ctc ("bg kacey_blowjob_throughwall")
    show screen gloryhole_blowjob_xray

    call process_character (n, appearance="blush false", text="Охх!")
    call process_character (gloryhole_girl, appearance="", text="Мм, ах!")
    call process_character (gloryhole_girl, appearance="", text="Твой член жаждет этого!")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(У него свежий вкус!)")
    call process_character (gloryhole_girl, appearance="", text="(Как много крайней плоти!)")
    call process_character (gloryhole_girl, appearance="", text="Ммф...")
    call process_character (gloryhole_girl, appearance="", text="(Это замечательный, неиспорченный член!)")
    call process_character (gloryhole_girl, appearance="", text="(И он весь мой)")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="([gloryhole_girl.say_name] взяла мой член в рот?)")
    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (n, appearance="blush false", text="(Похоже, она на самом деле это делает!)")
    call process_character (gloryhole_girl, appearance="", text="Ммм...")
    call process_character (gloryhole_girl, appearance="", text="Как же чертовски хорошо.")
    call process_character (n, appearance="blush false", text="Что хорошо?")
    call process_character (gloryhole_girl, appearance="", text="Твой гребаный член.")
    call process_character (gloryhole_girl, appearance="", text="И твоё предсемя...")
    call process_character (gloryhole_girl, appearance="", text="Это мощно!")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="Ты сосёшь сильнее!")
    call process_character (gloryhole_girl, appearance="", text="(Я не могу контролировать себя)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Я просто хочу сосать его член всё сильнее и сильнее...)")
    call process_character (n, appearance="blush false", text="Ахх, ах, ах!")
    call process_character (n, appearance="blush false", text="Как долго ты будешь это делать, [gloryhole_girl.say_name]?")
    call process_character (gloryhole_girl, appearance="", text="Ммф...")
    call process_character (gloryhole_girl, appearance="", text="Пока не возьму всё!")
    call process_character (n, appearance="blush false", text="Я-я не знаю, как долго я, ах,{w=0.5} смогу держаться!")
    call process_character (gloryhole_girl, appearance="", text="Это то, что мы хотим.")
    call process_character (gloryhole_girl, appearance="", text="Когда ты достигнешь предела...")
    call process_character (gloryhole_girl, appearance="", text="Ты забьёшь мой рот горячей спермой.")
    call process_character (gloryhole_girl, appearance="", text="Ты хочешь это сделать, да, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Ахх...")
    call process_character (n, appearance="blush false", text="Д-да.")
    call process_character (gloryhole_girl, appearance="", text="Я так и думала.")

    if "kira_scene_stealth_bj" in scenes_completed:
        call process_character (gloryhole_girl, appearance="", text="...")
        call process_character (gloryhole_girl, appearance="", text="Скажи мне, [n.say_name]...")
        call process_character (gloryhole_girl, appearance="", text="Твоя сестра глотала?")
        call process_character (n, appearance="blush false", text="Глотала?")
        call process_character (gloryhole_girl, appearance="", text="Ну ты знаешь...")
        call process_character (gloryhole_girl, appearance="", text="Проглатывала ли она твою сперму?")
        call process_character (n, appearance="blush false", text="Ох...")
        call process_character (n, appearance="blush false", text="Да, она проглатывала.")
        call process_character (gloryhole_girl, appearance="", text="Ты, должно быть, ужасно хороший брат, чтобы заслужить это!")
        call process_character (n, appearance="blush false", text="...")
        call process_character (gloryhole_girl, appearance="", text="Я тоже проглатываю у хороших парней.")

    hide screen gloryhole_blowjob_xray
    call static_still_ctc ("bg kacey_blowjob_nocumshot")

    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="[gloryhole_girl.say_name[0]]-[gloryhole_girl.say_name]...")
    call process_character (n, appearance="blush false", text="Я-я кончаю!")
    call process_character (gloryhole_girl, appearance="", text="Выстреливай, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Ммм!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg kacey_blowjob_cumshot")

    call process_character (gloryhole_girl, appearance="", text="!!")
    call process_character (gloryhole_girl, appearance="", text="(Он будто взорвался спермой в мой рот!)")
    call process_character (n, appearance="blush false", text="Аах, ах...")
    call process_character (gloryhole_girl, appearance="", text="(Она капает с моего подбородка!)")
    call process_character (n, appearance="", text="{i}Вздох.{/i}..")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Ты в порядке, [gloryhole_girl.say_name]?")

    call static_still_ctc ("bg kacey_blowjob_mouth_cum")

    call process_character (gloryhole_girl, appearance="", text="{i}Угх!{/i}")
    call process_character (gloryhole_girl, appearance="", text="{i}Чавк!{/i}")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="Лучше, чем в порядке!")
    call process_character (gloryhole_girl, appearance="", text="Это было довольно освежающе, [n.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Спасибо!")
    call process_character (n, appearance="blush false", text="В-всегда пожалуйста.")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="Ну, уже поздно.")
    call process_character (gloryhole_girl, appearance="", text="Я не хочу, чтобы твоя семья беспокоилась о тебе.")
    call process_character (n, appearance="blush false", text="Да, я должен вернуться домой.")
    call process_character (gloryhole_girl, appearance="", text="Что ты думаешь?")
    call process_character (gloryhole_girl, appearance="", text="Это весело, когда твой член сосут, не так ли?")
    call process_character (n, appearance="blush false", text="Конечно!")
    call process_character (gloryhole_girl, appearance="", text="Если ты захочешь опустошить свои яйца, не проходи мимо.")
    call process_character (gloryhole_girl, appearance="", text="Не трать впустую носки или салфетки!")
    call process_character (n, appearance="blush false", text="Хорошо, я зайду, когда смогу!")
    call process_character (n, appearance="blush false", text="Пока, [gloryhole_girl.say_name]!")

    python:
        gloryhole_girl.revistable_scenes.add("gloryhole_scene_blowjob_revisit")

        if not dream:
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_cummed_in_mouth", 1)
            stats.add_stat("times_received_blowjob", 1)

    call process_end_of_scene ("gloryhole_scene_blowjob", char=gloryhole_girl, dream=dream)

    return

label gloryhole_scene_blowjob_revisit:
    if "gloryhole_scene_blowjob_revisit" not in scenes_completed:
        call gloryhole_scene_blowjob_revisit_1st_time
    else:
        call gloryhole_scene_blowjob_revisit_2nd_time

    return

label gloryhole_scene_blowjob_revisit_1st_time:
    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg kacey_blowjob_mouth_nocum")

    call process_character (gloryhole_girl, appearance="", text="Вернулся за добавкой?")
    call process_character (n, appearance="blush false", text="Я-я, да...")
    call process_character (gloryhole_girl, appearance="", text="Мой рот готов к твоему члену!")
    call process_character (n, appearance="blush false", text="Я вытаскиваю его из штанов.")
    call process_character (gloryhole_girl, appearance="", text="Это уже твёрдый?")
    call process_character (n, appearance="blush false", text="Ээ, да.")
    call process_character (gloryhole_girl, appearance="", text="Ох!")
    call process_character (gloryhole_girl, appearance="", text="У меня слюнка уже потекла!")

    $ gloryhole_blowjob_xray_on = False
    call static_still_ctc ("bg kacey_blowjob_throughwall")
    show screen gloryhole_blowjob_xray

    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (n, appearance="blush false", text="Аaах!")
    call process_character (gloryhole_girl, appearance="", text="Ммм...")
    call process_character (gloryhole_girl, appearance="", text="(Его член становится скользки от моего языка)")
    call process_character (gloryhole_girl, appearance="", text="(Вкус его члена вызывает слюнотечение!)")
    call process_character (n, appearance="blush false", text="Ах, [gloryhole_girl.say_name]...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (gloryhole_girl, appearance="", text="Тебе нравится, когда твой член весь грязный и скользкий, [n.say_name]?")
    call process_character (gloryhole_girl, appearance="", text="А как насчет всех звуков, которые я издаю, когда я сосу твой член?")
    call process_character (gloryhole_girl, appearance="", text="Тебе нравится?")

    menu:
        "Твой рот издает все эти звуки?":
            call process_character (gloryhole_girl, appearance="", text="Конечно!")
            call process_character (gloryhole_girl, appearance="", text="Все эти причмокивающие звуки?")
            call process_character (gloryhole_girl, appearance="", text="Это мой рот и твой член работают вместе в полной гармонии!")
        "Сделай звуки громче!":
            call add_boldness (1, tag="gloryhole_scene_blowjob_revisit_1st_time_louder_sounds")
            call process_character (gloryhole_girl, appearance="", text="Ох!")
            call process_character (gloryhole_girl, appearance="", text="Говоришь, сделать погромче?")
            call process_character (gloryhole_girl, appearance="", text="Тогда я должна сосать еще усерднее!")
            call process_character (gloryhole_girl, appearance="", text="Но я уверена, что ты знаешь...")

    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (gloryhole_girl, appearance="", text="Думаю, нам с тобой очень хорошо вместе.")
    call process_character (gloryhole_girl, appearance="", text="Ты так не думаешь?")
    call process_character (n, appearance="blush false", text="Ч-что ты имеешь в виду?")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (gloryhole_girl, appearance="", text="Мы оба добры друг к другу, мы наслаждаемся обществом друг друга...")
    call process_character (gloryhole_girl, appearance="", text="И мы получаем некоторое сексуальное поощрение!")
    call process_character (n, appearance="blush false", text="Мне нравится тусоваться здесь с тобой, [gloryhole_girl.say_name].")
    call process_character (n, appearance="blush false", text="Т-ты очень веселая!")
    call process_character (gloryhole_girl, appearance="", text="О, это так мило, [n.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Мне тоже нравится быть здесь с тобой.")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(И мне нравится быть с твоим членом)")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="Ох!")
    call process_character (n, appearance="blush false", text="Т-так здорово, [gloryhole_girl.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Знаешь, что будет по-настоящему здорово?")

    hide screen gloryhole_blowjob_xray
    call static_still_ctc ("bg kacey_blowjob_nocumshot")

    call process_character (gloryhole_girl, appearance="", text="Наполни весь мой рот!")
    call process_character (n, appearance="blush false", text="Ах, ах, ах!")
    call process_character (n, appearance="blush false", text="Это действительно звучит хорошо!")
    call process_character (n, appearance="blush false", text="Я думаю, что я готов сделать это!")
    call process_character (gloryhole_girl, appearance="", text="Дай мне его!")
    call process_character (gloryhole_girl, appearance="", text="Я бы хотела попробовать еще немного твоего семени!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg kacey_blowjob_cumshot")

    call process_character (n, appearance="blush false", text="Аах!")
    call process_character (gloryhole_girl, appearance="", text="Держись, держись!")
    call process_character (n, appearance="blush false", text="Аах, оох...")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="У тебя яйца размером с грейпфрут!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Что заставляет тебя так говорить?")

    call static_still_ctc ("bg kacey_blowjob_mouth_cum")

    call process_character (gloryhole_girl, appearance="", text="Это была тонна спермы!")
    call process_character (gloryhole_girl, appearance="", text="{i}Хлёб!{/i}")
    call process_character (gloryhole_girl, appearance="", text="Но послушай, я не жалуюсь!")

    call gloryhole_scene_blowjob_revisit_end

    return

label gloryhole_scene_blowjob_revisit_2nd_time:
    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    $ gloryhole_blowjob_xray_on = False
    call static_still_ctc ("bg kacey_blowjob_throughwall")
    show screen gloryhole_blowjob_xray

    call process_character (gloryhole_girl, appearance="", text="Ммм, ахх...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я до сих пор не знаю, как [gloryhole_girl.say_name] выглядит...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Но она тоже не знает, как я выгляжу...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(За исключением моего...)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Мне нравится, как [n.say_name] просто предлагает свой член для меня)")
    call process_character (gloryhole_girl, appearance="", text="(Я более чем счастлива принять его...)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Просто надеюсь, что я не опустошаю его яйца слишком сильно)")
    call process_character (gloryhole_girl, appearance="", text="(Признаюсь, что я немного спермошлюха...)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Я буду продолжать пить сперму [n.say_name], пока не останется ничего, кроме пыли!)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!")
    $ quick_menu = True

    hide screen gloryhole_blowjob_xray

    call static_still_ctc ("bg kacey_blowjob_nocumshot")

    call process_character (n, appearance="blush false", text="Aaxx!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg kacey_blowjob_cumshot")

    call process_character (gloryhole_girl, appearance="", text="Ты золотая жила, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Ах, ах.")
    call process_character (n, appearance="blush false", text="Ох...")

    call static_still_ctc ("bg kacey_blowjob_mouth_cum")

    call process_character (gloryhole_girl, appearance="", text="Как вкусно!")
    call process_character (gloryhole_girl, appearance="", text="[n.say_name], продолжай приносить мне больше этих извержений!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Помогает ли это твоей жажде?")
    call process_character (gloryhole_girl, appearance="", text="Ах, да, [n.say_name]...")
    call process_character (gloryhole_girl, appearance="", text="Это определенно утоляет мою жажду...")
    call gloryhole_scene_blowjob_revisit_end

    return

label gloryhole_scene_blowjob_revisit_end:
    python:
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_cummed_in_mouth", 1)
        stats.add_stat("times_received_blowjob", 1)

    call process_end_of_scene ("gloryhole_scene_blowjob_revisit", char=gloryhole_girl, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label gloryhole_scene_vaginal(dream=False):
    call gloryhole_scene_vaginal_sex (dream=dream)
    return

label gloryhole_scene_vaginal_sex(dream=False):
    call process_scene_beginning (bg="bg gloryhole", dream=dream )
    $ no_bust_art = True
    $ heard_of_blowjob = True

    call process_character (gloryhole_girl, appearance="", text="О, это ты, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Ага!")
    call process_character (n, appearance="blush false", text="Я здесь!")
    call process_character (gloryhole_girl, appearance="", text="Я очень рада, что ты зашел!")
    call process_character (gloryhole_girl, appearance="", text="Особенно в мой день рождения!")
    call process_character (n, appearance="blush false", text="О, круто!")
    call process_character (n, appearance="blush false", text="С днем ​​рождения!")
    call process_character (gloryhole_girl, appearance="", text="Спасибо!")
    call process_character (n, appearance="blush false", text="У тебя была вечеринка или что-то еще?")

    call process_character (gloryhole_girl, appearance="", text="Ха, нет...")
    call process_character (gloryhole_girl, appearance="", text="Я даже не думала об этом.")
    call process_character (n, appearance="blush false", text="У тебя хотя бы был торт?")
    call process_character (gloryhole_girl, appearance="", text="На самом деле я не большой поклонник тортов.")
    call process_character (n, appearance="blush false", text="Да быть не может!")
    call process_character (n, appearance="blush false", text="Как можно не любить торт?")
    call process_character (gloryhole_girl, appearance="", text="Хаха, знаю, знаю...")

    call process_character (n, appearance="blush false", text="Как насчет подарков?")
    call process_character (n, appearance="blush false", text="Ты должна была получить хоть сколько-нибудь!")
    call process_character (gloryhole_girl, appearance="", text="Нет, у меня не было подарков ни от кого.")
    call process_character (n, appearance="blush false", text="Что?!")
    call process_character (n, appearance="blush false", text="Это ужасно!")
    call process_character (n, appearance="blush false", text="Ни вечеринки, ни торта, ни подарков!")
    call process_character (gloryhole_girl, appearance="", text="На самом деле это нормально для меня.")
    call process_character (gloryhole_girl, appearance="", text="Мои дни рождения обычно довольно незаметны.")
    call process_character (gloryhole_girl, appearance="", text="Вот почему я счастлива, что ты здесь, чтобы сделать его интересным!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Хотелось бы, чтобы у меня был для тебя подарок...")
    call process_character (gloryhole_girl, appearance="", text="Ах, не беспокойся об этом, [n.say_name].")
    call process_character (gloryhole_girl, appearance="", text="Но, эй...")
    call process_character (gloryhole_girl, appearance="", text="Я знаю что-то, что хотела бы на день рождения ...")
    call process_character (n, appearance="blush false", text="О, да?")
    call process_character (n, appearance="blush false", text="Я могу помочь?")
    call process_character (gloryhole_girl, appearance="", text="Ты точно сможешь!")
    call process_character (n, appearance="blush false", text="Хорошо!")
    call process_character (n, appearance="blush false", text="Что я должен сделать?")
    call process_character (gloryhole_girl, appearance="", text="Просто сделай то, что ты всегда делал.")
    call process_character (gloryhole_girl, appearance="", text="Сделай свой член твёрдым для меня.")
    call process_character (n, appearance="blush false", text="О-окей, конечно!")
    call process_character (gloryhole_girl, appearance="", text="И просуньте его, когда он будет красивым и твёрдым.")
    call process_character (n, appearance="blush false", text="...{p}...")

    call static_still_ctc ("bg kacey_vaginal_penis")

    call process_character (gloryhole_girl, appearance="", text="Ты сделал это в мгновение ока!")
    call process_character (gloryhole_girl, appearance="", text="(Я так рада, что он зашёл сегодня вечером!)")
    call process_character (gloryhole_girl, appearance="", text="(Я думала об этом весь день сегодня...)")
    call process_character (n, appearance="blush false", text="Так что ты хотела сделать на свой день рождения с моим членом?")
    call process_character (n, appearance="blush false", text="Это минет?")
    call process_character (gloryhole_girl, appearance="", text="Мой день рождения заслуживает чего-то более...{w=1.0} особенного, чем минет.")
    call process_character (gloryhole_girl, appearance="", text="Ты так не думаешь?")
    call process_character (n, appearance="blush false", text="Что-то особенное?")
    call process_character (gloryhole_girl, appearance="", text="Я думаю, ты должен познакомиться с определенной частью моего тела.")
    call process_character (gloryhole_girl, appearance="", text="Я так долго ждала встречи с твоим членом...")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg kacey_vaginal_tip")

    call process_character (gloryhole_girl, appearance="", text="Ты это чувствуешь?")
    call process_character (n, appearance="blush false", text="Я-я чувствую что-то...")
    call process_character (gloryhole_girl, appearance="", text="Ты чувствуешь что-то мокрое и теплое на кончике члена?")
    call process_character (n, appearance="blush false", text="Д-да.")
    call process_character (n, appearance="blush false", text="Э-это твои губы?")
    call process_character (gloryhole_girl, appearance="", text="Мм, ну...")
    call process_character (gloryhole_girl, appearance="", text="Можно сказать, что это мои губы...")
    call process_character (gloryhole_girl, appearance="", text="Мои губы киски.")
    call process_character (n, appearance="blush false", text="К-киски?")
    call process_character (gloryhole_girl, appearance="", text="Нет чувства, похожего на это, [n.say_name].")
    call process_character (gloryhole_girl, appearance="", text="Самая лучшая часть - это то, насколько легко впустить твой член в мою киску.")
    call process_character (gloryhole_girl, appearance="", text="Все, что я должна сделать, это немного откинуться назад и...")

    call static_still_ctc ("bg kacey_vaginal_nocum")

    call process_character (gloryhole_girl, appearance="", text="Мы в деле!")
    call process_character (gloryhole_girl, appearance="", text="Ах! Чёрт!")
    call process_character (gloryhole_girl, appearance="", text="Ох, мы в деле! Ах!")
    call process_character (n, appearance="blush false", text="Аах!")
    call process_character (n, appearance="blush false", text="Хм, ах...")
    call process_character (gloryhole_girl, appearance="", text="Не бойся размахивать бедрами!")
    call process_character (gloryhole_girl, appearance="", text="Пусть мои толчки, {w=0.5}ах, столкнуться с твоими!")
    call process_character (n, appearance="blush false", text="Мм! Мм!")

    if stats.stat_value("times_had_vaginal_sex") > 0:
        call process_character (gloryhole_girl, appearance="", text="Ох, ох!")
        call process_character (gloryhole_girl, appearance="", text="Ты сделал это раньше, не так ли?")
        call process_character (n, appearance="blush false", text="Ах, ах!")
        call process_character (gloryhole_girl, appearance="", text="Знаешь, трахать киску женщины это чертовски хорошо!")
        call process_character (gloryhole_girl, appearance="", text="Ах...")
        call process_character (gloryhole_girl, appearance="", text="Вот почему ты трахаешь меня с такой силой и энергией!")
        call process_character (n, appearance="blush false", text="Мм, ахх!")
        call process_character (gloryhole_girl, appearance="", text="Должно быть ты трахал хорошую киску раньше!")
        call process_character (gloryhole_girl, appearance="", text="Чёрт, ах!")
        call process_character (gloryhole_girl, appearance="", text="Респект тому, кто это был!")
    else:
        call process_character (gloryhole_girl, appearance="", text="Это ваш первый опыт с киской?")
        call process_character (n, appearance="blush false", text="Д-да.")
        call process_character (gloryhole_girl, appearance="", text="...")
        call process_character (gloryhole_girl, appearance="", text="(Вау, для девственника он долбит меня хорошо!)")
        call process_character (gloryhole_girl, appearance="", text="Я так понимаю, ты доволен этим опытом?")
        call process_character (n, appearance="blush false", text="Д-да, ах!")
        call process_character (gloryhole_girl, appearance="", text="Это значит он ещё вернётся сюда...")

    call process_character (n, appearance="blush false", text="Хмм!")
    call process_character (n, appearance="blush false", text="[gloryhole_girl.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Это лучший день рождения!")
    call process_character (gloryhole_girl, appearance="", text="Это лучше, чем любые подарки или пирожные!")
    call process_character (gloryhole_girl, appearance="", text="Э-это то, что я действительно хотела!")
    call process_character (gloryhole_girl, appearance="", text="Чтобы ты пронзил меня своим членом!")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Хотела бы я сделать это на следующий день рождения ...)")
    call process_character (gloryhole_girl, appearance="", text="Ах! Ох!")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="Но зачем останавливаться только на моем дне рождения?")
    call process_character (gloryhole_girl, appearance="", text="Каждый день - хороший день для этого!")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="Ты хочешь трахаться так каждый день, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="Е-если у меня будет время, чтобы зайти...")
    call process_character (n, appearance="blush false", text="Д-да я приду.")
    call process_character (gloryhole_girl, appearance="", text="Мм! Ах, ох!")
    call process_character (gloryhole_girl, appearance="", text="Если ты слишком занят, мы можем сделать это быстро!")
    call process_character (gloryhole_girl, appearance="", text="Или если, {w=0.5}ах, ты более свободен...")
    call process_character (gloryhole_girl, appearance="", text="Мы могли бы сделать это пару раз!")
    call process_character (n, appearance="blush false", text="Мм, Ммм!")
    call process_character (n, appearance="blush false", text="Я-я думаю, что это подходит мне...")
    call process_character (gloryhole_girl, appearance="", text="{i}Вздох!{/i} {i}Вздох!{/i}")
    call process_character (gloryhole_girl, appearance="", text="Да!{p}Да!")
    call process_character (gloryhole_girl, appearance="", text="Не останавливайся, не останавливайся!")
    call process_character (gloryhole_girl, appearance="", text="Чёрт!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Ну, сказала она, не останавливайся...)")
    call process_character (n, appearance="blush false", text="(Так что я думаю, это означает, что все в порядке, если я...)")
    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (n, appearance="blush false", text="Аах!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg kacey_vaginal_cum")

    call process_character (gloryhole_girl, appearance="", text="О, да!")
    call process_character (gloryhole_girl, appearance="", text="Накачай меня своим соком!")
    call process_character (gloryhole_girl, appearance="", text="(Он кончает на полную мощность!)")
    call process_character (n, appearance="blush false", text="Аах...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Уоу...")
    call process_character (gloryhole_girl, appearance="", text="Вау, ты прав [n.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Этот день рождения, я не скоро забуду!")
    call process_character (n, appearance="blush false", text="Д-да?")
    call process_character (gloryhole_girl, appearance="", text="Спасибо, что сделал это [n.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Ты сделал мой день точно!")
    call process_character (n, appearance="blush false", text="К-круто!")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="Уфф, парень!")
    call process_character (gloryhole_girl, appearance="", text="Уборщикам придётся брать сверхурочное время, чтобы очистить эту кабинку!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Кажется, мне пора уже идти домой.")
    call process_character (n, appearance="blush false", text="Становится поздно.")
    call process_character (gloryhole_girl, appearance="", text="Время летит, когда веселишься!")
    call process_character (gloryhole_girl, appearance="", text="Ещё раз спасибо, [n.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Заходи поскорее!")

    call fade_to_black (1)

    call process_character (n, appearance="blush false", text="Пока [gloryhole_girl.say_name], и с днём рождения!")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Не так много парней, которые так хороши)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Давай посмотрим ...)")

    call static_still_ctc ("bg kacey_vaginal_spread_cum")

    call process_character (gloryhole_girl, appearance="", text="(Обалдеть!)")
    call process_character (gloryhole_girl, appearance="", text="(Целый поток спермы!)")
    call process_character (gloryhole_girl, appearance="", text="...{p}...")
    call process_character (gloryhole_girl, appearance="", text="(Хорошо, что я приняла таблетку сегодня утром)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Погоди...)")
    call process_character (gloryhole_girl, appearance="", text="(Я приняла?)")

    python:
        gloryhole_girl.revistable_scenes.add("gloryhole_scene_vaginal_revisit")

        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_vaginal_sex", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_given_vaginal_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("gloryhole_scene_vaginal", char=gloryhole_girl, dream=dream)

    return

label gloryhole_scene_vaginal_revisit:
    if "gloryhole_scene_vaginal_revisit" not in scenes_completed:
        call gloryhole_scene_vaginal_revisit_1st_time
    else:
        call gloryhole_scene_vaginal_revisit_2nd_time

    return


label gloryhole_scene_vaginal_revisit_1st_time:
    python hide:
        play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg kacey_vaginal_penis")

    call process_character (gloryhole_girl, appearance="", text="Он выглядит, как счастливый петушок!")
    call process_character (gloryhole_girl, appearance="", text="Я очень рада тебя видеть.")
    call process_character (gloryhole_girl, appearance="", text="Или более конкретно...")

    call static_still_ctc ("bg kacey_vaginal_tip")

    call process_character (gloryhole_girl, appearance="", text="Рада показать свою киску!")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="Ты готов к еще одному раунду против моей киски, [n.say_name]?")

    menu:
        "Я готов!":
            call process_character (gloryhole_girl, appearance="", text="Конечно!")
        "Я собираюсь зайти так далеко, как смогу!":
            call add_boldness (1, tag="gloryhole_vaginal_scene_revisit_go_in_far")
            call process_character (gloryhole_girl, appearance="", text="Не могу с этим поспорить!")
            call process_character (gloryhole_girl, appearance="", text="Ты знаешь, что мне нравится, [n.say_name]!")

    call static_still_ctc ("bg kacey_vaginal_nocum")

    call process_character (gloryhole_girl, appearance="", text="Да! Ах да!")
    call process_character (gloryhole_girl, appearance="", text="Я уже могу сказать, что ты делаешь это по-разному!")
    call process_character (n, appearance="blush false", text="Ах...")
    call process_character (n, appearance="blush false", text="П-Правда?")
    call process_character (gloryhole_girl, appearance="", text="Ты пытался понять меня в первый раз.")
    call process_character (gloryhole_girl, appearance="", text="Но сейчас...")
    call process_character (gloryhole_girl, appearance="", text="Пытаешься меня сломать!")
    call process_character (gloryhole_girl, appearance="", text="Aах!")
    call process_character (n, appearance="blush false", text="Ах, ахх!")
    call process_character (n, appearance="blush false", text="В этот раз я стараюсь двигаться быстрее.")
    call process_character (gloryhole_girl, appearance="", text="Ты делаешь правильный выбор!")
    call process_character (gloryhole_girl, appearance="", text="Никаких вопросов по этому поводу!")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (n, appearance="blush false", text="Я-я становлюсь более возбужденным таким образом!")
    call process_character (gloryhole_girl, appearance="", text="Ты не шутишь об этом!")
    call process_character (gloryhole_girl, appearance="", text="Удовольствие распространяется по всему телу!")
    call process_character (gloryhole_girl, appearance="", text="(Только его второй трах, а он так резко улучшился!)")
    call process_character (gloryhole_girl, appearance="", text="(Он гений секса!)")
    call process_character (n, appearance="blush false", text="Аах!")
    call process_character (n, appearance="blush false", text="Ах, ах!")

    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Я не думаю, что [n.say_name] осознает его...{w=1.0} талант)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Никто и не подумает, что этот обычный ребенок, ах, {w=0.5} может отлупить вас своим членом!)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(По крайней мере, он кажется обычным)")
    call process_character (gloryhole_girl, appearance="", text="(Я действительно не знаю, как он выглядит...)")
    call process_character (gloryhole_girl, appearance="", text="(Пока)")
    call process_character (n, appearance="blush false", text="[gloryhole_girl.say_name[0]] - [gloryhole_girl.say_name]!")
    call process_character (n, appearance="blush false", text="Я-Я собираюсь кончить очень скоро!")
    call process_character (gloryhole_girl, appearance="", text="Я могу понять, почему!")
    call process_character (gloryhole_girl, appearance="", text="Ты не замедлялся, ах {w=0.5}с тех пор, как начал!")
    call process_character (gloryhole_girl, appearance="", text="Ни одни яйца юноши не могут продержаться так долго.")
    call process_character (n, appearance="blush false", text="Хмм!")
    call process_character (n, appearance="blush false", text="Aaах!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg kacey_vaginal_cum")

    call process_character (gloryhole_girl, appearance="", text="Oох!")
    call process_character (gloryhole_girl, appearance="", text="(Чувствую удары его спермы всей киской!)")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")

    call static_still_ctc ("bg kacey_vaginal_tip_cum")

    call process_character (gloryhole_girl, appearance="", text="Это незабываемое семяизвержение, наверняка!")
    call process_character (gloryhole_girl, appearance="", text="Твоя сперма продолжает сочиться из моей пизды!")

    call gloryhole_scene_vaginal_revisit_end

    return

label gloryhole_scene_vaginal_revisit_2nd_time:
    python hide:
        play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg kacey_vaginal_tip")

    call process_character (gloryhole_girl, appearance="", text="Твой член оживает, когда моя киска рядом, [n.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Я никогда не видела, чтобы член становился твердым с такой легкостью!")

    call static_still_ctc ("bg kacey_vaginal_nocum")

    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="([n.say_name] должно быть, из семьи порнозвезд или что-то еще...)")
    call process_character (gloryhole_girl, appearance="", text="(Или его предки были теми ещё кобелями)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Его либидо выше среднего)")
    call process_character (gloryhole_girl, appearance="", text="(Он, вероятно, смог бы сразу трех женщин за раз!)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Но это означало бы, что мне придется с кем-то делиться его членом)")
    call process_character (gloryhole_girl, appearance="", text="(Нет, спасибо!)")
    call process_character (gloryhole_girl, appearance="", text="(Мне нужен его стержень столько, сколько я могу!)")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="(Интересно, придется ли нам в конечном итоге отправиться в другое место)")
    call process_character (n, appearance="blush false", text="(Зимой здесь будет холодно!)")
    call process_character (n, appearance="blush false", text="(И я не думаю, что в этом туалете есть отопление...)")
    call process_character (gloryhole_girl, appearance="", text="Ах!")
    call process_character (gloryhole_girl, appearance="", text="Да, [n.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Продолжай трахать меня!")
    call process_character (gloryhole_girl, appearance="", text="Трахни меня, пока не будешь готов кончить!")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!")
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )


    call static_still_ctc ("bg kacey_vaginal_cum")

    call process_character (gloryhole_girl, appearance="", text="Ты предпочитаешь кончать внутрь, не так ли?")
    call process_character (gloryhole_girl, appearance="", text="Или ты не успеваешь вытащить его? Хаха!")
    call process_character (gloryhole_girl, appearance="", text="По крайней мере, твоя сперма используется надлежащим образом!")

    call gloryhole_scene_vaginal_revisit_end

    return

label gloryhole_scene_vaginal_revisit_end:
    python:
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_vaginal_sex", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_given_vaginal_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("gloryhole_scene_vaginal_revisit", char=gloryhole_girl, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label gloryhole_scene_anal(dream=False):
    call gloryhole_scene_anal_sex (dream=dream)
    return

label gloryhole_scene_anal_sex(dream=False):
    $ renpy.scene('screens')
    if dream:
        show screen dream_blur

    call fade_to_black (1)

    call process_character (n, appearance="blush false", text="Привет [gloryhole_girl.say_name].")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (n, appearance="blush false", text="[gloryhole_girl.say_name]?")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (n, appearance="blush false", text="(Может быть, ее здесь нет)")
    call process_character (n, appearance="blush false", text="(Надо проверить дырку...)")

    call static_still_ctc ("bg kacey_anal_gloryhole")

    call process_character (n, appearance="blush false", text="!!")
    call process_character (n, appearance="blush false", text="(Это анус?!)")
    call process_character (gloryhole_girl, appearance="", text="Я тебя удивила, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Оох!")
    call process_character (n, appearance="blush false", text="Это ты, [gloryhole_girl.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Ха-ха, а ты думал кто?")
    call process_character (n, appearance="blush false", text="Ты не ответила, поэтому я не был уверен...")
    call process_character (gloryhole_girl, appearance="", text="Ты подумал, что это какая-то другая попка, на которую ты смотрел?")
    call process_character (gloryhole_girl, appearance="", text="Хаха!")
    call process_character (n, appearance="blush false", text="Теперь, когда ты так говоришь...")
    call process_character (n, appearance="blush false", text="Мне было глупо думать, что это кто-то другой.")
    call process_character (gloryhole_girl, appearance="", text="Ты бунтарь, [n.say_name]!")
    call process_character (n, appearance="blush false", text="...")

    if "kira_scene_2_seq_2" in scenes_completed:
        call process_character (n, appearance="blush false", text="Т-твоя задница выглядит точно также, как у моей старшей сестры.")
        call process_character (gloryhole_girl, appearance="", text="Правда?")
        call process_character (gloryhole_girl, appearance="", text="Ты, должно быть, некоторое время наблюдал за ней.")
        call process_character (n, appearance="blush false", text="Оох да!")
        call process_character (n, appearance="blush false", text="Мне очень нравится попка моей сестры!")
        call process_character (gloryhole_girl, appearance="", text="Она позволила тебе перейти на следующую базу?")
        call process_character (gloryhole_girl, appearance="", text="Ты выбил хоумран?")
        call process_character (n, appearance="blush false", text="Хоумран?")
        call process_character (gloryhole_girl, appearance="", text="Твой член вошёл в ее задницу?")

        if "kira_scene_anal" in scenes_completed:
            call process_character (n, appearance="blush false", text="Да!")
            call process_character (n, appearance="blush false", text="Это было что-то!")
            call process_character (gloryhole_girl, appearance="", text="Ну тогда ты знаешь, что делать!")
            call process_character (gloryhole_girl, appearance="", text="Цель для твоего петушка прямо здесь!")
        else:
            call process_character (n, appearance="blush false", text="Н-нет.")
            call process_character (gloryhole_girl, appearance="", text="Ну, тогда я на шаг впереди твоей сестры!")
            call process_character (gloryhole_girl, appearance="", text="Моя задница готова к твоему члену!")
            call process_character (gloryhole_girl, appearance="", text="Просто вставь!")
    else:
        call process_character (gloryhole_girl, appearance="", text="Ты готов начать?")
        call process_character (n, appearance="blush false", text="В твою задницу?")
        call process_character (gloryhole_girl, appearance="", text="Тебе нужно исследовать все мои отверстия, [n.say_name]!")
        call process_character (gloryhole_girl, appearance="", text="Ты залил мое горло своей спермой.")
        call process_character (gloryhole_girl, appearance="", text="Потом ты забил мою киску")
        call process_character (gloryhole_girl, appearance="", text="А теперь, ты можешь рассверлить мой анус!")
        call process_character (gloryhole_girl, appearance="", text="Не плохо звучит?")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Х-хорошо!")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg kacey_anal_insert")

    call process_character (gloryhole_girl, appearance="", text="Oох!")
    call process_character (n, appearance="blush false", text="Я... я не думал, что это будет так!")
    call process_character (gloryhole_girl, appearance="", text="Почти что!")
    call process_character (gloryhole_girl, appearance="", text="Моя попка, ах, {w=1.0}такая чувствительная!")
    call process_character (n, appearance="blush false", text="Должен ли я быть более осторожным?")
    call process_character (gloryhole_girl, appearance="", text="Тебе решать.")
    call process_character (gloryhole_girl, appearance="", text="Самому...")
    call process_character (gloryhole_girl, appearance="", text="Я хочу, чтобы ты ввёл свой член прямо сейчас!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я-я могу это сделать, если хочешь.")
    call process_character (gloryhole_girl, appearance="", text="Пожалуйста!")

    call static_still_ctc ("bg kacey_anal_fuck_clothed_nocum")

    call process_character (gloryhole_girl, appearance="", text="Aaах!")
    call process_character (gloryhole_girl, appearance="", text="Да, Да!")
    call process_character (gloryhole_girl, appearance="", text="(Какой толчок наслаждения!)")
    call process_character (gloryhole_girl, appearance="", text="(Кажется, я кончила от шока от такого удовольствия!)")
    call process_character (n, appearance="blush false", text="Мм, Мм!")
    call process_character (gloryhole_girl, appearance="", text="Можешь помедленнее, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Д-да, ах!")
    call process_character (n, appearance="blush false", text="Сейчас.")
    call process_character (gloryhole_girl, appearance="", text="Я слышала, что легче заниматься анальным сексом, когда у мужчины есть крайняя плоть на члене, как у тебя.")
    call process_character (gloryhole_girl, appearance="", text="Ох!")
    call process_character (gloryhole_girl, appearance="", text="Я не знаю, правда ли это или нет...")
    call process_character (gloryhole_girl, appearance="", text="Но я знаю, что это чертовски хорошо!")
    call process_character (n, appearance="blush false", text="Аах! {i}Вздох.{/i}..")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Мои соски так же твёрдые, как скала!)")
    call process_character (gloryhole_girl, appearance="", text="(Я чувствую, будто они могут протереть дырку в моей рубашке!)")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (n, appearance="blush false", text="[gloryhole_girl.say_name[0]]-[gloryhole_girl.say_name]?")
    call process_character (n, appearance="blush false", text="Как далеко мой пенис входит в твою задницу?")
    call process_character (gloryhole_girl, appearance="", text="Достаточно далеко, чтобы держать мою киску влажной, [n.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Ах, ты отлично справляешься!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ты когда-нибудь делала это раньше, [gloryhole_girl.say_name]?")
    call process_character (gloryhole_girl, appearance="", text="Я-я практиковалась с некоторыми, ах,{w=0.5} некоторыми фаллоимитаторами раньше.")
    call process_character (gloryhole_girl, appearance="", text="Но это первый раз, когда я получаю настоящее мясцо в задницу!")
    call process_character (gloryhole_girl, appearance="", text="И это ни с чем не сравнится!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Она сказала, фаллоимитаторы?)")
    call process_character (gloryhole_girl, appearance="", text="Я также пробовала некоторые большие размеры!")
    call process_character (gloryhole_girl, appearance="", text="Ох, ах, ах!")
    call process_character (gloryhole_girl, appearance="", text="Твой член намного превосходит их!")
    call process_character (gloryhole_girl, appearance="", text="Ах, чёрт!")
    call process_character (n, appearance="blush false", text="Ох, ах!")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Не знаю, смогу ли я вернуться к фаллоимитаторам после этого...)")
    call process_character (gloryhole_girl, appearance="", text="(Черт, я не знаю, как смогу наслаждаться другим членом!)")
    call process_character (gloryhole_girl, appearance="", text="(И он еще даже не набрался опыта!)")
    call process_character (gloryhole_girl, appearance="", text="Ах, оох...")
    call process_character (gloryhole_girl, appearance="", text="(Он быстро научится, если сможет трахать меня постоянно!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я почти уже...")
    call process_character (gloryhole_girl, appearance="", text="Кончай мне в зад, [n.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Дай мне анальный кремовый пирог!")
    call process_character (n, appearance="blush false", text="Я не думаю, что раньше слышал этот термин.")
    call process_character (gloryhole_girl, appearance="", text="Я думаю, ты догадаешься!")
    call process_character (gloryhole_girl, appearance="", text="Просто дай, как можно больше, спермы в мой анус!")

    call static_still_ctc ("bg kacey_anal_internal_nocum")

    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (n, appearance="blush false", text="Оно выходит!")
    call process_character (n, appearance="blush false", text="Хннг!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg kacey_anal_internal_cum")

    call process_character (gloryhole_girl, appearance="", text="Aах!")
    call process_character (gloryhole_girl, appearance="", text="Твоя сперма...")
    call process_character (gloryhole_girl, appearance="", text="Такая горячая!")
    call process_character (n, appearance="blush false", text="Аах, ах!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")

    call static_still_ctc ("bg kacey_anal_fuck_clothed_cum")

    call process_character (gloryhole_girl, appearance="", text="Я чувствую, что ты все еще держишься!")
    call process_character (gloryhole_girl, appearance="", text="Даже после того, как кончил, он не может остановиться.")
    call process_character (n, appearance="blush false", text="Д-да...")
    call process_character (gloryhole_girl, appearance="", text="Когда будешь выходить из меня, делай это медленно.")
    call process_character (gloryhole_girl, appearance="", text="Если вы достанешь член слишком быстро, то сперма вырвется!")
    call process_character (n, appearance="blush false", text="О-окей.")
    call process_character (n, appearance="blush false", text="Буду помедленнее...")

    call static_still_ctc ("bg kacey_anal_gloryhole_cum")

    call process_character (gloryhole_girl, appearance="", text="Ухху!")
    call process_character (gloryhole_girl, appearance="", text="Сегодня мой анус прошёл через все базы!")
    call process_character (gloryhole_girl, appearance="", text="Ты видишь, как выбегает сперма?")
    call process_character (n, appearance="blush false", text="Д-да.")
    call process_character (gloryhole_girl, appearance="", text="Забавная у меня будет походка после этого.")
    call process_character (gloryhole_girl, appearance="", text="Но это небольшая цена, чтобы заплатить за то, насколько мне хорошо!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (gloryhole_girl, appearance="", text="Чувак, я вся вспотела!")
    call process_character (gloryhole_girl, appearance="", text="Хотелось бы, чтобы в этих туалетах были душевые!")
    call process_character (n, appearance="blush false", text="Я тоже вспотел.")
    call process_character (gloryhole_girl, appearance="", text="В будущем надо будет снимать нашу одежду.")
    call process_character (gloryhole_girl, appearance="", text="И сохраним всё в сухости.")
    call process_character (n, appearance="blush false", text="Д-да.")
    call process_character (gloryhole_girl, appearance="", text="Плюс мы не замёрзнем по дороге домой.")
    call process_character (gloryhole_girl, appearance="", text="Я ненавижу это липкое чувство от потной, холодной одежды.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ты придёшь ещё?")
    call process_character (gloryhole_girl, appearance="", text="Да.")
    call process_character (gloryhole_girl, appearance="", text="Мне нужно отдохнуть после всего этого!")
    call process_character (gloryhole_girl, appearance="", text="Ты заставил меня запыхаться от этого траха!")

    python:
        gloryhole_girl.revistable_scenes.add("gloryhole_scene_anal_revisit")

        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_seen_butt", 1)
            stats.add_stat("times_seen_butthole", 1)
            stats.add_stat("times_given_anal_sex", 1)
            stats.add_stat("times_given_anal_creampie", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("gloryhole_scene_anal", char=gloryhole_girl, dream=dream)

    return

label gloryhole_scene_anal_revisit:
    $ renpy.scene('screens')

    if "gloryhole_scene_anal_revisit" not in scenes_completed:
        call gloryhole_scene_anal_revisit_1st_time
    else:
        call gloryhole_scene_anal_revisit_2nd_time

    return


label gloryhole_scene_anal_revisit_1st_time:
    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg kacey_anal_gloryhole")

    call process_character (gloryhole_girl, appearance="", text="Вставь его, [n.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Я готов!")

    call static_still_ctc ("bg kacey_anal_insert")

    call process_character (gloryhole_girl, appearance="", text="Уже почти получилось...")
    call process_character (n, appearance="blush false", text="Я чувствую твои ягодицы своим членом...")
    call process_character (gloryhole_girl, appearance="", text="Это говорит тебе, что ты очень близко!")
    call process_character (gloryhole_girl, appearance="", text="Твой член прижат прямо к моей дырке.")
    call process_character (gloryhole_girl, appearance="", text="Почему бы тебе не сделать хороший толчок?")
    call process_character (n, appearance="blush false", text="Ладно.")
    call process_character (gloryhole_girl, appearance="", text="Подожди, прежде чем ты это сделаешь...")
    call process_character (n, appearance="blush false", text="Что случилось?")
    call process_character (gloryhole_girl, appearance="", text="Я не хочу, чтобы моя одежда снова промокла от пота.")
    call process_character (gloryhole_girl, appearance="", text="Дай мне всего секунду...")

    call fade_to_black (1)

    call process_character (n, appearance="blush false", text="...")
    call process_character (gloryhole_girl, appearance="", text="...{p}...")
    call process_character (gloryhole_girl, appearance="", text="Ладно...")

    call static_still_ctc ("bg kacey_anal_insert_naked")

    call process_character (gloryhole_girl, appearance="", text="Теперь все хорошо!")
    call process_character (gloryhole_girl, appearance="", text="Засунь в меня свой член!")

    call static_still_ctc ("bg kacey_anal_fuck_naked_nocum")

    call process_character (gloryhole_girl, appearance="", text="Aах!")
    call process_character (gloryhole_girl, appearance="", text="Он проскользнул прямо внутрь!")
    call process_character (gloryhole_girl, appearance="", text="Хорошая работа, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Ох, ох!")
    call process_character (n, appearance="blush false", text="Она тугая!")
    call process_character (gloryhole_girl, appearance="", text="Очень приятно это слышать!")
    call process_character (gloryhole_girl, appearance="", text="Я надеялась, что ты не будешь свободно ходить в моей заднице.")
    call process_character (gloryhole_girl, appearance="", text="Ах, ах!")
    call process_character (gloryhole_girl, appearance="", text="Он, конечно, не потерял чувствительность!")
    call process_character (n, appearance="blush false", text="Ахх, ах!")
    call process_character (gloryhole_girl, appearance="", text="Черт, ах!")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="На данный момент ты трахнул все мои дырочки, [n.say_name].")
    call process_character (gloryhole_girl, appearance="", text="Есть ли у тебя любимая?")
    call process_character (n, appearance="blush false", text="Любимая?")
    call process_character (gloryhole_girl, appearance="", text="У каждого есть любимая дырка, чтобы трахаться.")
    call process_character (gloryhole_girl, appearance="", text="Так скажи мне...")
    call process_character (gloryhole_girl, appearance="", text="Это мой рот, киска или попка?")

    menu:
        "Т-твой рот очень даже не плох...":
            call process_character (gloryhole_girl, appearance="", text="Ах, тебе должно быть понравилось движения языка.")
            call process_character (gloryhole_girl, appearance="", text="Фелляция может быть моей фишкой!")
        "Мне нравится трахать твою киску.":
            call process_character (gloryhole_girl, appearance="", text="Ожидаемый выбор.")
            call process_character (gloryhole_girl, appearance="", text="Нет ничего лучше теплой киски на твоем члене!")
        "Твоя задница - моя любимая дырка!":
            call process_character (gloryhole_girl, appearance="", text="Ха-ха, в этом есть смысл...")
            call process_character (gloryhole_girl, appearance="", text="Учитывая, куда ты опять меня трахаешь!")
        "Я не могу решить, мне все они нравятся!":
            call add_boldness (1, tag="gloryhole_anal_scene_revisit_like_all")
            call process_character (gloryhole_girl, appearance="", text="Ох, конечно!")
            call process_character (gloryhole_girl, appearance="", text="Я поняла!")
            call process_character (gloryhole_girl, appearance="", text="Ты хочешь всё самое лучшее!")

    call process_character (n, appearance="blush false", text="Много людей делают это, [gloryhole_girl.say_name]?")
    call process_character (gloryhole_girl, appearance="", text="Что, анал?")
    call process_character (n, appearance="blush false", text="Ах...")
    call process_character (n, appearance="blush false", text="Д-да.")
    call process_character (gloryhole_girl, appearance="", text="Я бы сказала, что много людей делают это, да.")
    call process_character (gloryhole_girl, appearance="", text="Его просто нужно распробовать")
    call process_character (n, appearance="blush false", text="Попробовать?")
    call process_character (gloryhole_girl, appearance="", text="Не каждая девушка хочет член в своей заднице.")
    call process_character (gloryhole_girl, appearance="", text="Ах, ах, ах!")
    call process_character (gloryhole_girl, appearance="", text="Почему они этого не делают, я никогда не пойму!")
    call process_character (gloryhole_girl, appearance="", text="Это фантастический способ оторваться!")
    call process_character (n, appearance="blush false", text="Аах! Ах!")
    call process_character (n, appearance="blush false", text="Аах!")
    call process_character (gloryhole_girl, appearance="", text="Похоже, ты готов сам оторваться!")
    call process_character (gloryhole_girl, appearance="", text="Наполни меня своей спермой!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg kacey_anal_internal_cum")

    call process_character (n, appearance="blush false", text="Ннг!")
    call process_character (gloryhole_girl, appearance="", text="Aaах!")
    call process_character (gloryhole_girl, appearance="", text="Всё внутрь!")

    call static_still_ctc ("bg kacey_anal_fuck_naked_cum")

    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (gloryhole_girl, appearance="", text="Вуу!")
    call process_character (gloryhole_girl, appearance="", text="Меня трясет после оргазма!")
    call process_character (gloryhole_girl, appearance="", text="Это случается с тобой иногда, когда ты кончаешь?")
    call process_character (n, appearance="blush false", text="Я-я не знаю.")
    call process_character (n, appearance="blush false", text="Мне просто очень нравится ощущение, когда я кончаю.")
    call process_character (gloryhole_girl, appearance="", text="Часть твоего семени капает на пол.")
    call process_character (gloryhole_girl, appearance="", text="Бьюсь об заклад, оно будет капать из моей задницы, пока я иду домой!")

    call gloryhole_scene_anal_revisit_end

    return

label gloryhole_scene_anal_revisit_2nd_time:
    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg kacey_anal_insert_naked")

    call process_character (gloryhole_girl, appearance="", text="Твой член выглядит тверже обычного.")
    call process_character (gloryhole_girl, appearance="", text="Интересно, я могу сказать...")

    call static_still_ctc ("bg kacey_anal_fuck_naked_nocum")

    call process_character (gloryhole_girl, appearance="", text="Ах, черт!")
    call process_character (gloryhole_girl, appearance="", text="Я не могу сказать, что твой член твёрже, чем раньше...")
    call process_character (gloryhole_girl, appearance="", text="Но я чертовски уверена, что знаю, как это хорошо!")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Это самое лучшее совокупление, которое у меня было за долгое время!)")
    call process_character (gloryhole_girl, appearance="", text="([n.say_name] превращает меня в сексуального наркомана!)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Я знаю, что наличие зависимости не всегда хорошо, но...)")
    call process_character (gloryhole_girl, appearance="", text="(Когда я чувствую себя так хорошо, это просто не может быть плохим!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я буду трахать [gloryhole_girl.say_name] насколько я смогу до конца лета)")
    call process_character (n, appearance="blush false", text="(После того, как школа начнётся, это будет труднее сделать)")
    call process_character (n, appearance="blush false", text="(Уф, у меня, вероятно, будет много домашней работы)")
    call process_character (n, appearance="blush false", text="(Может быть, [gloryhole_girl.say_name] и я сможем сделать это по выходным!)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", xalign = 0.65, yalign = 0.05)
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )


    call static_still_ctc ("bg kacey_anal_fuck_naked_cum")

    call process_character (gloryhole_girl, appearance="", text="Ммм! Да!")
    call process_character (gloryhole_girl, appearance="", text="[n.say_name], как много спермы!")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="Я должна вести учет количества оргазмов, которые мы получили!")
    call process_character (gloryhole_girl, appearance="", text="Интересно, сможем ли мы установить рекорд!")

    call gloryhole_scene_anal_revisit_end

    return

label gloryhole_scene_anal_revisit_end:
    python:
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_seen_butt", 1)
        stats.add_stat("times_seen_butthole", 1)
        stats.add_stat("times_given_anal_sex", 1)
        stats.add_stat("times_given_anal_creampie", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("gloryhole_scene_anal_revisit", char=gloryhole_girl, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label gloryhole_scene_stall(dream=False):
    call gloryhole_scene_stall_sex (dream=dream)
    return

label gloryhole_scene_stall_sex(dream=False):
    $ renpy.scene('screens')
    if dream and not persistent.disable_dream_blur:
        show screen dream_blur

    call static_still_ctc ("bg gloryhole")

    call process_character (gloryhole_girl, appearance="", text="Привет, [n.say_name].")
    call process_character (gloryhole_girl, appearance="", text="Как прошел твой вечер?")
    call process_character (n, appearance="blush false", text="Хорошо.")
    call process_character (n, appearance="blush false", text="А твой?")
    call process_character (gloryhole_girl, appearance="", text="День напряженный, но вечер был нормальный.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="Разве не странно, что мы так разговариваем?")
    call process_character (n, appearance="blush false", text="Хм?")
    call process_character (gloryhole_girl, appearance="", text="Что мы общаемся через эту дыру.")
    call process_character (gloryhole_girl, appearance="", text="Не пойми меня неправильно, то, что мы делаем с ней, здорово.")
    call process_character (gloryhole_girl, appearance="", text="Только...")
    call process_character (gloryhole_girl, appearance="", text="Я действительно хочу узнать, как ты выглядишь, [n.say_name].")
    call process_character (gloryhole_girl, appearance="", text="Кто этот молодой человек с прекрасным членом?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Так ты хочешь меня увидеть?")
    call process_character (gloryhole_girl, appearance="", text="Уверен, тебе тоже было интересно, как я выгляжу.")
    call process_character (n, appearance="blush false", text="Вообще-то...")
    call process_character (n, appearance="blush false", text="Да.")
    call process_character (gloryhole_girl, appearance="", text="{i}Клик{/i}")
    call process_character (gloryhole_girl, appearance="", text="Вот, моя кабинка открыта.")
    call process_character (n, appearance="blush false", text="Ты хочешь, чтобы я зашёл прямо сейчас?")
    call process_character (gloryhole_girl, appearance="", text="Абсолютно!")
    call process_character (gloryhole_girl, appearance="", text="Но у меня есть одно условие.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (gloryhole_girl, appearance="", text="Ты должен быть голым.")
    call process_character (gloryhole_girl, appearance="", text="Без одежды вообще.")
    call process_character (n, appearance="blush false", text="Без одежды?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Х-хорошо.")
    call process_character (gloryhole_girl, appearance="", text="Мы уже видели наши самые личные места друг у друга.")
    call process_character (gloryhole_girl, appearance="", text="С таким же успехом можно показать всё, да?")
    call process_character (n, appearance="blush false", text="Т-ты тоже собираешься раздеться?")
    call process_character (gloryhole_girl, appearance="", text="Уже.")
    call process_character (gloryhole_girl, appearance="", text="Повесь одежду на дверь, чтобы он не валялась на полу.")
    call process_character (n, appearance="blush false", text="Хорошо.")

    call fade_to_black (1)

    call process_character (n, appearance="blush false", text="...")
    call process_character (gloryhole_girl, appearance="", text="Ты идёшь?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я открываю дверь...")
    call process_character (gloryhole_girl, appearance="", text="...{p}...")
    call process_character (gloryhole_girl, appearance="", text="О, боже!")
    call process_character (gloryhole_girl, appearance="", text="Ты такой милашка!")
    call process_character (n, appearance="blush false", text="У-у тебя ноги раздвинуты!")
    call process_character (gloryhole_girl, appearance="", text="Что по-твоему, мы собирались здесь делать?")
    call process_character (gloryhole_girl, appearance="", text="Подойди ближе!")
    call process_character (gloryhole_girl, appearance="", text="Давай толкать наши тела вместе!")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg kacey_stall_fuck")

    call process_character (gloryhole_girl, appearance="", text="А ты меньше, чем я думала!")
    call process_character (gloryhole_girl, appearance="", text="Ох, ах, ах!")
    call process_character (gloryhole_girl, appearance="", text="Это еще более впечатляет, учитывая, как хорошо ты трахаешься!")
    call process_character (n, appearance="blush false", text="Ах, ахх!")
    call process_character (gloryhole_girl, appearance="", text="И мне нравятся твои голубые глаза!")
    call process_character (n, appearance="blush false", text="У-у моей сестры такие же глаза, как у меня.")
    call process_character (gloryhole_girl, appearance="", text="Твои короткие волосы подчеркивают черты лица.")
    call process_character (n, appearance="blush false", text="Ох!")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (n, appearance="blush false", text="Мне нравится быть так близко!")
    call process_character (gloryhole_girl, appearance="", text="Ах, ох чёрт!")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Я думала, что [n.say_name] младше, но...)")
    call process_character (gloryhole_girl, appearance="", text="(Я практически могу сойти за его маму!)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="([gloryhole_girl.say_name] похожа телом на [k.say_name]...)")
    call process_character (n, appearance="blush false", text="(Хотя [k.say_name] более мускулистая...)")
    call process_character (n, appearance="blush false", text="Ахх! Ммм!")
    call process_character (n, appearance="blush false", text="(Её сиськи такие мягкие)")
    call process_character (n, appearance="blush false", text="(Они вертятся, как желе!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я и не знал, что у тебя большие сиськи.")
    call process_character (gloryhole_girl, appearance="", text="Ох, это правда!")
    call process_character (gloryhole_girl, appearance="", text="Ты же никогда раньше не видел мои сиськи!")
    call process_character (n, appearance="blush false", text="Н-нет...")
    call process_character (gloryhole_girl, appearance="", text="Ты неравнодушен к большим сиськам?")
    call process_character (gloryhole_girl, appearance="", text="Большинство молодых мужчин такие.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Мне они действительно нравятся.")
    call process_character (gloryhole_girl, appearance="", text="Почему бы тебе не пососать их?")
    call process_character (n, appearance="blush false", text="Пососать их?")
    call process_character (gloryhole_girl, appearance="", text="Уверена, они понравятся тебе!")
    call process_character (gloryhole_girl, appearance="", text="Они прямо здесь для тебя!")
    call process_character (n, appearance="blush false", text="...")

    call static_still_ctc ("bg kacey_stall_titsuck")

    call process_character (gloryhole_girl, appearance="", text="Вот так!")
    call process_character (gloryhole_girl, appearance="", text="Oох!")
    call process_character (gloryhole_girl, appearance="", text="Ты тянешь меня за сосок губами!")
    call process_character (gloryhole_girl, appearance="", text="Да, да!")
    call process_character (n, appearance="blush false", text="{i}Ммф{/i}...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Соски [gloryhole_girl.say_name] довольно вкусные!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я не могу сравнить этот вкус ни с чем...)")
    call process_character (gloryhole_girl, appearance="", text="{i}Вздох.{/i}..")
    call process_character (gloryhole_girl, appearance="", text="(Это такое приятное чувство!)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="([n.say_name] превращает меня в сексуального наркомана!)")
    call process_character (gloryhole_girl, appearance="", text="(Я и не думала, что секс может достичь такого уровня!)")
    call process_character (gloryhole_girl, appearance="", text="(Раньше я считала, что порно даст мне больше удовольствия...)")
    call process_character (gloryhole_girl, appearance="", text="(Но, [n.say_name] на уровень выше!)")
    call process_character (n, appearance="blush false", text="Ммм...")
    call process_character (gloryhole_girl, appearance="", text="Я...")
    call process_character (gloryhole_girl, appearance="", text="Я хочу, чтобы ты взял меня сзади, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Хм?")
    call process_character (gloryhole_girl, appearance="", text="Сейчас не будет никакой стены, ограничивающей тебя.")
    call process_character (gloryhole_girl, appearance="", text="Так что можешь трахать меня с полной силой!")
    call process_character (n, appearance="blush false", text="...")

    call static_still_ctc ("bg kacey_stall_fuck_nocum")

    call process_character (gloryhole_girl, appearance="", text="Да!")
    call process_character (gloryhole_girl, appearance="", text="Вот так, [n.say_name]!")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}Вздох.{/i}..")
    call process_character (gloryhole_girl, appearance="", text="([n.say_name] вцепился в меня, как магнит!)")
    call process_character (gloryhole_girl, appearance="", text="(Он, похоже, не сбирается останавливаться в ближайшее время...)")
    call process_character (gloryhole_girl, appearance="", text="Ммм!")
    call process_character (gloryhole_girl, appearance="", text="(В этом преимущество молодости!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Попка [gloryhole_girl.say_name] подпрыгивает, когда я заталкиваю свой член в...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Это круто, что она так делает)")
    call process_character (gloryhole_girl, appearance="", text="Э-эй, [n.say_name]...")
    call process_character (gloryhole_girl, appearance="", text="Ты должен вставлять его на уровень выше!")
    call process_character (n, appearance="blush false", text="Что я должен сделать?")
    call process_character (gloryhole_girl, appearance="", text="Трахни меня как отбойный молоток!")
    call process_character (gloryhole_girl, appearance="", text="Заставь мою грудь качаться!")

    call static_still_ctc ("bg kacey_stall_fuckahego_blur_nocum")

    call process_character (n, appearance="blush false", text="Аах! Хррм!")
    call process_character (gloryhole_girl, appearance="", text="Твоооою мать!")
    call process_character (gloryhole_girl, appearance="", text="Аах, ах!")
    call process_character (gloryhole_girl, appearance="", text="(У меня сердце колотится!)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Можно ли испытывать оргазм каждые пару секунд?)")
    call process_character (gloryhole_girl, appearance="", text="(Потому что это то, что я делаю!)")
    call process_character (gloryhole_girl, appearance="", text="Оох...")
    call process_character (gloryhole_girl, appearance="", text="Т-ты делаешь девушку счастливой, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Я?")
    call process_character (gloryhole_girl, appearance="", text="Оох, да...")
    call process_character (n, appearance="blush false", text="Ахх...")
    call process_character (n, appearance="blush false", text="Хррм!")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Я знаю, это риск не сказать [n.say_name], чтобы он не кончал в меня...)")
    call process_character (gloryhole_girl, appearance="", text="(Но логическая часть моего мозга отключилась!)")
    call process_character (gloryhole_girl, appearance="", text="(Я просто хочу, чтобы он продолжал!)")
    call process_character (n, appearance="blush false", text="[gloryhole_girl.say_name[0]]-[gloryhole_girl.say_name]!")
    call process_character (n, appearance="blush false", text="Хннг!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg kacey_stall_fuck_blur_cum")

    call process_character (gloryhole_girl, appearance="", text="Oох!!")
    call process_character (gloryhole_girl, appearance="", text="(Он так глубоко кончил в меня, по полной!)")

    call static_still_ctc ("bg kacey_stall_fuck_blur_cum_impreg")

    call process_character (n, appearance="blush false", text="Мм!{p}Мм!")
    call process_character (gloryhole_girl, appearance="", text="(Есть не так много парней, которые могут продолжать после того, как они кончают...)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="([n.say_name] уникален, это точно)")

    call static_still_ctc ("bg kacey_stall_fuck_cum_impreg")

    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="Ты без сил, [n.say_name]?")
    call process_character (gloryhole_girl, appearance="", text="Могу себе представить, после всего, что ты сделал!")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..{p}{i}Вздох.{/i}..")
    call process_character (gloryhole_girl, appearance="", text="Не думаю, что ты сможешь дойти до дома в таком состоянии.")
    call process_character (gloryhole_girl, appearance="", text="Почему бы тебе не полежать у меня на коленях?")
    call process_character (gloryhole_girl, appearance="", text="Можешь потереться о мои сиськи, пока отдыхаешь.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Отлично звучит.")
    call process_character (gloryhole_girl, appearance="", text="Я уверена, что лаская мои сиськи к тебе вернутся силы в кратчайшие сроки!")

    python:
        gloryhole_girl.revistable_scenes.add("gloryhole_scene_stall_revisit")

        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_vaginal_sex", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_given_vaginal_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("gloryhole_scene_stall", char=gloryhole_girl, dream=dream)

    return

label gloryhole_scene_stall_revisit:
    $ renpy.scene('screens')

    if "gloryhole_scene_stall_revisit" not in scenes_completed:
        call gloryhole_scene_stall_revisit_1st_time
    else:
        call gloryhole_scene_stall_revisit_2nd_time

    return


label gloryhole_scene_stall_revisit_1st_time:
    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg kacey_stall_fuck")

    call process_character (gloryhole_girl, appearance="", text="Приятно видеть тебя снова лицом к лицу, [n.say_name]!")
    call process_character (n, appearance="blush false", text="М-мне тоже!")
    call process_character (gloryhole_girl, appearance="", text="Сегодня на улице сыро!")
    call process_character (gloryhole_girl, appearance="", text="Я принесла пару бутылок с водой.")
    call process_character (n, appearance="blush false", text="Это было хорошей идеей.")
    call process_character (n, appearance="blush false", text="Я уже вся вспотела!")
    call process_character (gloryhole_girl, appearance="", text="Да, сиденье унитаза холодное!")
    call process_character (gloryhole_girl, appearance="", text="Я должна принести полотенце, чтобы подложить его.")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (gloryhole_girl, appearance="", text="Ах...")
    call process_character (gloryhole_girl, appearance="", text="Я хотела спросить тебя, [n.say_name]...")
    call process_character (n, appearance="blush false", text="Хм?")
    call process_character (gloryhole_girl, appearance="", text="Что ты делаешь ради удовольствия?")
    call process_character (gloryhole_girl, appearance="", text="У тебя есть какие-нибудь хобби?")
    call process_character (n, appearance="blush false", text="Хобби?")
    call process_character (gloryhole_girl, appearance="", text="Даже нам нужен перерыв от траха!")
    call process_character (gloryhole_girl, appearance="", text="Должно быть что-то, что ты делаешь дома для развлечения!")

    menu:
        "Я играю в видеоигры.":
            pass
        "Я плаваю в бассейне.":
            call process_character (gloryhole_girl, appearance="", text="Правильно, ты мне уже говорил об этом!")
            call process_character (gloryhole_girl, appearance="", text="Должно быть, приятно иметь свой собственный бассейн, в который ты можешь прыгать, когда угодно!")
            call process_character (n, appearance="blush false", text="Это здорово, да!")
            call process_character (gloryhole_girl, appearance="", text="А когда становится холоднее на улице?")
            call process_character (gloryhole_girl, appearance="", text="Должно быть что-то еще, что ты любишь делать в помещении!")
            call process_character (n, appearance="blush false", text="В основном я играю в видеоигры.")
        "Я играюсь со своим членом.":
            call add_boldness (1, tag="gloryhole_scene_stall_play_penis")

            call process_character (gloryhole_girl, appearance="", text="Значит, когда ты не трахаешься, ты мастурбируешь?")
            call process_character (gloryhole_girl, appearance="", text="Хаха!")
            call process_character (gloryhole_girl, appearance="", text="Ты возбуждён все время?")
            call process_character (n, appearance="blush false", text="...")
            call process_character (gloryhole_girl, appearance="", text="Поверь мне, я все понимаю.")
            call process_character (gloryhole_girl, appearance="", text="Дома я тоже много мастурбирую...")
            call process_character (gloryhole_girl, appearance="", text="...")
            call process_character (gloryhole_girl, appearance="", text="Но должно быть что-то еще, что тебе нравится, кроме этого!")
            call process_character (n, appearance="blush false", text="Ну, я играю во многие видеоигры.")

    call process_character (gloryhole_girl, appearance="", text="Не может быть!")
    call process_character (gloryhole_girl, appearance="", text="Ты?")
    call process_character (n, appearance="blush false", text="Да.")
    call process_character (n, appearance="blush false", text="Я много общаюсь со своей сестрой.")
    call process_character (gloryhole_girl, appearance="", text="Я тоже играю в видеоигры!")
    call process_character (n, appearance="blush false", text="Ты?")
    call process_character (gloryhole_girl, appearance="", text="Я была долгое время игроком!")
    call process_character (gloryhole_girl, appearance="", text="Я помню, как купила игровую Game Station G.")
    call process_character (gloryhole_girl, appearance="", text="Это была отличная консоль!")
    call process_character (n, appearance="blush false", text="У тебя была одна из этих консолей?!")
    call process_character (gloryhole_girl, appearance="", text="Это было давно, не так ли?")
    call process_character (n, appearance="blush false", text="Я думаю, что я даже не родился, когда она вышла!")
    call process_character (gloryhole_girl, appearance="", text="Мы должны увидеться, чтобы сыграть онлайн когда-нибудь!")
    call process_character (n, appearance="blush false", text="Д-да!")
    call process_character (n, appearance="blush false", text="Это было бы замечательно!")
    call process_character (gloryhole_girl, appearance="", text="Кстати о веселье...")
    call process_character (gloryhole_girl, appearance="", text="Хочешь снова попробовать мои сиськи?")

    call static_still_ctc ("bg kacey_stall_titsuck")

    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (gloryhole_girl, appearance="", text="Ох, да!")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Его, должно быть, много кормили грудью, когда он был маленьким)")
    call process_character (gloryhole_girl, appearance="", text="(Как еще он мог полюбить сосать сиську?)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(У его мамы должно быть несколько больших...)")
    call process_character (n, appearance="blush false", text="Ммф.")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Он сжимает их)")
    call process_character (gloryhole_girl, appearance="", text="(Его рука едва помещается вокруг одной груди, ха-ха!)")
    call process_character (gloryhole_girl, appearance="", text="(Он любит покачивать ими, когда он двигает рукой)")
    call process_character (gloryhole_girl, appearance="", text="(Это всё для тебя парень...)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="Эй, [n.say_name]...")
    call process_character (gloryhole_girl, appearance="", text="Заходи в меня сзади!")

    call static_still_ctc ("bg kacey_stall_fuckahego_blur_nocum")

    call process_character (n, appearance="blush false", text="Хах, ах!")
    call process_character (gloryhole_girl, appearance="", text="О черт!")
    call process_character (gloryhole_girl, appearance="", text="Прямо туда, [n.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Пройди весь путь!")
    call process_character (gloryhole_girl, appearance="", text="Oox!")
    call process_character (n, appearance="blush false", text="А когда я соберусь кончать?")
    call process_character (gloryhole_girl, appearance="", text="Ты про что?")
    call process_character (n, appearance="blush false", text="Ты хочешь, чтобы я кончил внутрь тебя?")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="Нет необходимости беспокоиться об этом больше...")
    call process_character (n, appearance="blush false", text="Что ты имеешь в виду?")
    call process_character (gloryhole_girl, appearance="", text="Ах, ничего, [n.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Просто ворвался в мою киску!")
    call process_character (n, appearance="blush false", text="Ох, ладно.")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Я знаю, что в конце концов мне придется проверить...)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Ах, не нужно беспокоиться об этом прямо сейчас!)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(По крайней мере, я знаю, что это здоровая сперма льётся в меня!)")
    call process_character (n, appearance="blush false", text="О...")
    call process_character (n, appearance="blush false", text="О-она выходит наружу!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg kacey_stall_fuck_blur_cum")

    call process_character (n, appearance="blush false", text="Хннг!")
    call process_character (gloryhole_girl, appearance="", text="Аах!")
    call process_character (n, appearance="blush false", text="Мм! Ах...")

    call static_still_ctc ("bg kacey_stall_fuck_cum")

    call process_character (gloryhole_girl, appearance="", text="{i}Вздох.{/i}..")
    call process_character (gloryhole_girl, appearance="", text="Со всей спермой, которую ты производишь, [n.say_name]...")
    call process_character (gloryhole_girl, appearance="", text="Ты когда-нибудь думал о том, чтобы получить несколько долларов, пожертвовав в банк спермы?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Что?")
    call process_character (gloryhole_girl, appearance="", text="Хех, забудь.")

    call gloryhole_scene_stall_revisit_end

    return

label gloryhole_scene_stall_revisit_2nd_time:
    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg kacey_stall_titsuck")

    call process_character (gloryhole_girl, appearance="", text="...{p}...")
    call process_character (gloryhole_girl, appearance="", text="(Интересно, насколько чаще будет хотеть [n.say_name] секса, когда он станет старше?)")
    call process_character (gloryhole_girl, appearance="", text="(Что, если он потребует секса через час?)")
    call process_character (gloryhole_girl, appearance="", text="(Это было бы что-то!)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Хотя, я могла бы полностью справиться с этим)")

    call static_still_ctc ("bg kacey_stall_fuckahego_blur_nocum")

    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох,{/i} {i}вздох.{/i}..")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Мне нужен был бы импульс энергии, чтобы справиться с дополнительным трахом!)")
    call process_character (gloryhole_girl, appearance="", text="(Возможно, я могла бы сделать супер сок...)")
    call process_character (gloryhole_girl, appearance="", text="(Возможно, придется пожертвовать поздними ночными играми, чтобы больше отдохнуть...)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Но в настоящее время у меня нет проблем с членом [n.say_name]!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я все еще не могу поверить, [gloryhole_girl.say_name] играла в игры всё это время!)")
    call process_character (n, appearance="blush false", text="(Я уверен, что она эксперт в некоторых из этих старых платформеров и РПГ!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Было бы здорово посмотреть ее коллекцию игр в один прекрасный день...)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", yalign = 0.1)
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg kacey_stall_fuck_blur_cum")

    call process_character (gloryhole_girl, appearance="", text="(Еще одна большая порция спермы!)")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Я даже не знаю, как моя киска может удержать все это!)")

    call static_still_ctc ("bg kacey_stall_fuck_cum")

    call process_character (n, appearance="blush false", text="{i}Фьюю.{/i}..")
    call process_character (gloryhole_girl, appearance="", text="...")
    call process_character (gloryhole_girl, appearance="", text="(Не нужно беспокоиться о возрождении человечества, если есть кто-то вроде [n.say_name] рядом...)")

    call gloryhole_scene_stall_revisit_end

    return

label gloryhole_scene_stall_revisit_end:
    python:
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_vaginal_sex", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_given_vaginal_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("gloryhole_scene_stall_revisit", char=gloryhole_girl, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return