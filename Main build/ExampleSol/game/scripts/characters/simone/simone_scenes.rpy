init python:
    def simone_vaginal_set_speed(label, is_revisit):
        renpy.call(label, is_revisit)
        
        return

image simone_vaginal_anim:
    "simone_vaginal_anim_0"
    pause 0.09
    "simone_vaginal_anim_1"
    pause 0.09
    "simone_vaginal_anim_2"
    pause 0.09
    "simone_vaginal_anim_3"
    pause 0.09
    "simone_vaginal_anim_4"
    pause 0.09
    "simone_vaginal_anim_5"
    pause 0.09
    "simone_vaginal_anim_6"
    pause 0.09
    repeat

screen simone_vaginal_speed_settings(is_revisit=False):
    vbox:
        xalign 0.97
        yalign 0.3
        spacing 20

        use main_menu_button(text="Медленно", action=Function(simone_vaginal_set_speed, "simone_vaginal_go_slow", is_revisit), enabled=main_animation_speed != simone_vaginal_slow_speed_multiplier)
        use main_menu_button(text="Нормально", action=Function(simone_vaginal_set_speed, "simone_vaginal_go_normal", is_revisit), enabled=main_animation_speed != 1.0)
        use main_menu_button(text="Быстро", action=Function(simone_vaginal_set_speed, "simone_vaginal_go_fast", is_revisit), enabled=main_animation_speed != simone_vaginal_fast_speed_multiplier)

label simone_scene_1_seq_1_sex(dream=False):
    call process_scene_beginning (bathroom, char_tuple_array=[ (n, "pose handpocket face flirty outfit clothesjacket_hard") ], dream=dream )

    python:
        fappable_targets = []
        fap_target = None
        if "sam_scene_2_seq_2" in scenes_completed:
            fappable_targets.append(sa)
        if "kira_scene_2_seq_2" in scenes_completed:
            fappable_targets.append(k)
        if "simone_scene_yoga_2" in scenes_completed:
            fappable_targets.append(si)
        if "julia_scene_nude" in scenes_completed:
            fappable_targets.append(julia)

        if len(fappable_targets) <= 0:
            fappable_targets.append(k)

        fap_target = random.choice(fappable_targets)

    if fap_target == sa:
        call process_character (n, text="(Мой член становится всё твёрже)")
        $ renpy.pause(1)
        call process_character (n, appearance="pose behindhead face flirty blush true", text="(Он затвердел...)")
        call process_character (n, appearance="pose behindhead face flirty blush true", text="(Когда я увидел голой [sa.say_name]...)")
    elif fap_target == si:
        call process_character (n, text="(Мой пенис никогда не был таким твердым...)")
        $ renpy.pause(1)
        call process_character (n, appearance="pose behindhead face flirty blush true", text="(Это началось после того, как я начал смотреть на мамины сиськи...)")
    elif fap_target == julia:
        call process_character (n, text="(Мой пенис супер твердый!)")
        call process_character (n, appearance="pose behindhead face flirty blush true", text="(Он был таким же твёрдым, когда...)")
        call process_character (n, appearance="pose behindhead face flirty blush true", text="(Я увидел [julia.say_name] голой в ванной...)")
    else:
        call process_character (n, text="(Мой пенис действительно твердый)")
        $ renpy.pause(1)
        call process_character (n, text="(Обычно через некоторое время он становится мягким)")
        call process_character (n, appearance="pose behindhead face flirty blush true", text="(Когда я увидел задницу [k.say_name]...)")
        call process_character (n, appearance="pose behindhead face flirty blush true", text="(Он встал)")

    $ renpy.pause(1)
    call process_character (n, appearance="pose twohandfist face flirty", text="(Ах, моему пенису мало места в штанах)")
    call process_character (n, appearance="pose twohandfist face flirty", text="(Мне нужно снять их, чтобы не давило так)")
    call static_still_ctc ("bg simone_1_grabs_dick")
    call process_character (n, text="(Так лучше)")

    if fap_target == sa:
        call process_character (n, text="(Я всё ещё думаю о [sa.say_name])")
    elif fap_target == si:
        call process_character (n, text="(Я всё ещё думаю о Маме)")
    elif fap_target == julia:
        call process_character (n, text="(Я всё ещё думаю о [julia.say_name])")
    else:
        call process_character (n, text="(Я всё ещё думаю о [k.say_name])")

    call process_character (n, text="{i}Ох{/i}...{p=1.0}(Приятно прикасаться к нему)")
    call process_character (n, text="(Может быть, я должен потрогать его, пока он не станет мягким)")

    call static_still_ctc ("bg simone_1_fapping")
    call process_character (n, text="{i}Ох! Ах!{/i}\n(Как же хорошо)")
    call process_character (n, text="{i}Ммм!{/i}")
    $ si.c(n.say_name + "!\nОбед стынет!")

    call bust_art_background (hallway)
    call process_character (si, appearance="outfit clothes pose armunder face curious")
    call process_character (n, text="{i}Ахх!{/i}")
    call process_character (si, appearance="pose armunder face curious", text="(Он должен быть в ванной)")
    call process_character (n, text="{i}Ах...{/i}{p=1.0}{i}Ыхх{/i}.", show_bust=False)
    call process_character (si, appearance="pose handsup face sad", text="(Ему больно?)")
    call process_character (n, text="{i}Ухх!{/i}", show_bust=False)
    call process_character (si, appearance="pose handsfront face curious", text="(Похоже, ему больно.){p=2.0}(Я должна убедиться, что он в порядке.)")
    call static_still_ctc ("bg simone_1_walks_in_a")
    call static_still_ctc ("bg simone_1_walks_in_b")
    call process_character (si, text="{i}!!!!{/i}")
    call process_character (n, text="МАМА!")
    $ si.c(n.say_name + " Мне так жаль!{p=0.5}Я хотела убедиться, что ты в порядке!")

    call static_still_ctc ("bg simone_1_what_is_my_life")

    $ si.c("Я-Я буду внизу с " + k.say_name + " и " + sa.say_name + ".{p=2.0}Не дай еде остыть.")
    call process_character (n, text="...")
    call process_character (si, text="(Я надеюсь, что он поймёт, как правильно...) {p=1.0}(мастурбировать)")
    $ renpy.pause(1)
    call process_character (si, text="(Может у него проблемы?)")
    $ renpy.pause(1)
    call process_character (si, text="(Он обязательно бы попробовал рано или поздно)")
    call process_character (si, text="(Должно быть, я его ужасно смутила, ворвавшись сюда.)")
    $ renpy.pause(1)
    call process_character (si, text="(Надеюсь, это было не слишком грубо)")

    call static_still_ctc ("bg simone_1_returns_to_fapping")
    call process_character (n, text="(Это чувство, будто я хочу писать!)")
    call process_character (n, text="(Но по-другому!)")
    call process_character (n, text="{i}Ахх, ахх!{/i}")
    call process_character (n, text="(Что-то выходит наружу!)")
    call static_still_ctc ("bg simone_1_cumming")
    call process_character (n, text="(Что это?)\n(Белое)")
    call process_character (n, text="(Вроде мой пенис становится мягче...)")

    call bust_art_background (bathroom)
    call process_character (n, appearance="pose handsdown face concerned outfit clothes", text="(Я не уверен, что случилось)")
    call process_character (n, appearance="pose handsdown face concerned", text="(Когда это белое вещество вышло...)")
    call process_character (n, appearance="pose handsdown face flirty", text="(Это было потрясающе)")
    $ renpy.pause(1)
    call process_character (n, appearance="pose behindhead face curious", text="...")

    $ renpy.pause(1)
    call process_character (n, appearance="pose handsdown face concerned", text="(Надо почистить тут всё и спуститься на ужин.)")

    python:
        if not dream:
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_fapped", 1)
            stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene ("simone_scene_1_seq_1", char=si, dream=dream, force_no_boldness=True)

    return

label simone_scene_1_revisit:
    python:
        fappable_targets = []
        fap_target = ""
        if "sam_scene_2_seq_2" in scenes_completed:
            fappable_targets.append(sa.say_name)

        if "kira_scene_2_seq_2" in scenes_completed:
            fappable_targets.append(k.say_name)

        if "simone_scene_yoga_2" in scenes_completed:
            fappable_targets.append("Mom")

        if "julia_scene_nude" in scenes_completed:
            fappable_targets.append(julia.say_name)

        if len(fappable_targets) == 0:
            fappable_targets.append(k.say_name)

        fap_target = random.choice(fappable_targets)


    call process_scene_beginning (bathroom, char_tuple_array=[ (n, "pose handpocket face flirty outfit clothesjacket") ])

    call process_character (n, appearance="pose handpocket face flirty outfit clothesjacket", text="(Это было очень круто в последний раз, когда я касался пениса)")
    $ renpy.pause(1)
    $ play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)
    call process_character (n, appearance="pose handpocket face flirty outfit clothesjacket", text="(Я думаю, что сделаю это снова)")
    call process_character (n, appearance="pose handpocket face flirty outfit clothesjacket", text="(На этот раз я запер дверь)")
    call static_still_ctc ("bg simone_1_grabs_dick")
    call process_character (n, text="{i}Ах{/i}...")
    $ renpy.pause(1)
    $ n.c( "(Как только я думаю о " + fap_target + ")" )
    call process_character (n, text="(Мой пенис становится твердым)")
    call static_still_ctc ("bg simone_1_fapping")
    call process_character (n, text="{i}Ахх! Охх!{/i}")
    call process_character (n, text="{i}Ммм!{/i}")

    if fap_target == sa.say_name:
        $ n.c("(Тело " + sa.say_name + "...)")
        $ renpy.pause(1)
        call process_character (n, text="(Ее влагалище выглядело так мило)")
        call process_character (n, text="(Я хочу увидеть её ещё раз)")
    elif fap_target == "Mom":
        call process_character (n, text="(Мамины сиськи...)")
        $ renpy.pause(1)
        call process_character (n, text="(Мне очень хотелось их потрогать)")
        call process_character (n, text="(Бьюсь об заклад, они такие мягкие)")
    elif fap_target == k.say_name:
        $ n.c("(Ох, и задница у " + k.say_name + "...)")
        $ renpy.pause(1)
        call process_character (n, text="(Мне нравится, какая она большая!)")
        call process_character (n, text="(Жаль, что я не могу смотреть на неё весь день!)")
    elif fap_target == julia.say_name:
        call process_character (n, text="(Тело [julia.say_name]...)")
        call process_character (n, text="(Хотел бы ближе к ней)")
        call process_character (n, text="(Бьюсь об заклад, её тело приятное и гладкое)")

    call process_character (n, text="{i}Аххх, Ох!{/i}")
    call process_character (n, text="(Я уже почти)")
    $ renpy.pause(1)
    call process_character (n, text="{i}Ммм!{/i}")
    call static_still_ctc ("bg simone_1_cumming")
    call process_character (n, text="(Эта штука снова вышла)")
    call process_character (n, text="(Чувствует себя потрясающе, когда это происходит!)")
    call bust_art_background (bathroom)
    call process_character (n, appearance="pose handsdown face flirty outfit underwear", text="{i}Фьюю...{/i}")
    call process_character (n, appearance="pose handsdown face flirty outfit underwear", text="(Это было ещё лучше, чем раньше!)")
    call process_character (n, appearance="pose handsdown face flirty outfit underwear", text="(И я думаю, что ещё больше белой штуки вышло)")
    $ renpy.pause(1)
    call process_character (n, appearance="pose behindhead face flirty outfit underwear", text="(Интересно, сколько раз я могу это делать)")
    call process_character (n, appearance="pose twohandfist face neutral outfit underwear", text="(Я надеюсь, что много!)")

    python:
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_fapped", 1)
        stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene ("simone_scene_1_revisit", force_no_boldness=True, force_not_replayable=True, revisit=True)

    return


label simone_scene_2:
    $ display_multiple_characters([ (n, ""), (si, "pose handsfront face neutral") ])

    call process_character (si, appearance="pose handsfront face neutral", text="[n.say_name], могу я с тобой поговорить?")
    call prompt_menu_boldness_check ("О чем ты хотела поговорить, Мама?", "Это не слишком срочно?", "simone_scene_2", si)

    return

label simone_scene_2_refusal(text, insufficient_points):
    if insufficient_points:
        call process_character (n, appearance="pose handpocket face neutral", text=text)
        call process_character (n, appearance="pose handpocket face curious", text="(Я не чувствую себя достаточно {b}уверенным{/b} для этого)")

    call process_character (si, appearance="pose armunder face neutral", text="Полагаю, это может подождать.")
    call prompt_refusal_end (si)

    return

label simone_scene_2_sex(dream=False):
    call process_scene_beginning (nate_room, char_tuple_array=[ (n, "outfit clothesjacket"), (si, "outfit clothes pose handsfront face neutral") ], dream=dream )
    call process_character (si, appearance="pose handsfront face neutral", text="Я хотела поговорить с тобой о том дне.")
    call process_character (si, appearance="pose handsfront face neutral", text="Когда ты была в туалете.")
    call process_character (n, appearance="pose handpocket face concerned", text="Ты имеешь в виду, когда увидела меня?")
    call process_character (si, appearance="pose handsfront face neutral", text="Да.")
    call process_character (n, appearance="pose handpocket face concerned blush true", text="...")
    call process_character (si, appearance="pose handsup face neutral", text="Я не хочу, чтобы ты расстраивался.")
    call process_character (si, appearance="pose handsup face neutral", text="Что ты делал, было совершенно нормально.")
    call process_character (n, appearance="pose handpocket face concerned blush true", text="Н-нормально?")
    call process_character (si, appearance="pose handsup face neutral", text="Конечно.")
    call process_character (si, appearance="pose handsup face neutral", text="Возможно, вы этого не знаете, но все молодые люди это делают.")
    call process_character (si, appearance="pose armunder face neutral", text="Это называется - мастурбация.")
    call process_character (n, appearance="pose handpocket face curious blush true", text="М-мастурбация?")

    if "kira_scene_2_seq_2" in scenes_completed:
        call process_character (n, appearance="pose handpocket face curious blush true", text="(Я думал, это называется дрочка?)")

    call process_character (si, appearance="pose handsup face neutral", text="Есть другие названия, чтобы описать это.")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="Это то, о чем ты хотела поговорить?")
    call process_character (si, appearance="pose handsup face neutral", text="Вроде.")
    call process_character (si, appearance="pose handsfront face neutral", text="Я просто хотела убедиться, что ты умеешь правильно мастурбировать.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Что ты имеешь в виду?")
    call process_character (si, appearance="pose handsfront face neutral", text="Когда я была в коридоре, ты издавал звуки, как будто тебе было больно.")
    call process_character (si, appearance="pose handsfront face neutral", text="И когда я тебя увидела...")
    call process_character (si, appearance="pose handsfront face neutral", text="Я беспокоился, что ты был груб со своими...")
    call process_character (si, appearance="pose armunder face neutral", text="Членом.")
    call process_character (n, appearance="pose twohandfist face embarrassed blush true", text="Мама!")
    call process_character (si, appearance="pose handsfront face curious", text="Как твоя мать, я должна всё знать, [n.say_name].")
    call process_character (si, appearance="pose handsfront face curious", text="Я знаю, что тебе стыдно об этом говорить.")
    call process_character (si, appearance="pose handsfront face curious", text="Но я не хочу, чтобы ты причинил себе вред.")
    call process_character (n, appearance="pose handpocket face concerned blush true", text="...")
    call process_character (n, appearance="pose handpocket face concerned blush true", text="Нуу...")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="Это был первый раз, когда я делал что-то подобное.")
    call process_character (si, appearance="pose handsup face neutral", text="Это веская причина узнать об этом побольше.")
    call process_character (si, appearance="pose handsup face neutral", text="Нужно быть осторожным, когда берешь и дёргаешь свой член.")
    call process_character (si, appearance="pose handsup face neutral", text="Особенно, когда он эрегированный, или как говорят \"стоит.\"")
    call process_character (n, appearance="pose behindhead face curious", text="...")
    call process_character (n, appearance="pose handpocket face curious", text="П-почему?")
    call process_character (si, appearance="pose armunder face neutral", text="Твой пенис - очень чувствительная часть тела.")
    call process_character (si, appearance="pose armunder face neutral", text="Если будешь груб, то рискуешь получить травму.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Звучит так, будто это больно.")
    call process_character (si, appearance="pose armunder face curious", text="Может быть больно.")
    call process_character (si, appearance="pose armunder face curious", text="И я не хотела, чтобы это случилось с тобой.")
    call process_character (si, appearance="pose handsup face neutral", text="Особенно, когда ты пытался почувствовать себя... хорошо.")
    call process_character (n, appearance="pose twohandfist face concerned", text="Я не хочу, чтобы это произошло!")
    call process_character (n, appearance="pose behindhead face curious", text="Итак, к-как это правильно делать...")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Мастурбировать?")
    call process_character (si, appearance="pose handsup face embarrassed", text="Нуу...")
    call process_character (si, appearance="pose handsup face neutral", text="Когда ты берёшь свой пенис, медленно двигай рукой вверх и вниз.")
    call process_character (si, appearance="pose handsup face neutral", text="Но не заходи слишком далеко.")
    call process_character (n, appearance="pose handpocket face concerned blush false")
    call process_character (si, appearance="pose handsfront face curious", text="Если станет больно, ты зашел слишком далеко.")
    call process_character (si, appearance="pose handsfront face curious", text="Как только найдешь комфортное расстояние, так и дрочи.")
    call process_character (si, appearance="pose armunder face neutral", text="Разве есть разница?")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Н-ну я думаю...")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Но как мне узнать правильное расстояние?")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Я не хочу, чтобы было больно.")
    call process_character (si, appearance="pose handsup face neutral", text="Я думаю, ты разберёшься, милый.")
    call process_character (si, appearance="pose handsup face neutral", text="Ты просто должен быть в курсе...")
    call process_character (n, appearance="pose twohandfist face concerned", text="Н-но я не очень много об этом знаю.")
    call process_character (n, appearance="pose twohandfist face concerned", text="Мам, ты знаешь об этом больше, чем я.")
    call process_character (n, appearance="pose twohandfist face concerned", text="Мне нужна твоя помощь!")
    call process_character (si, appearance="pose handsfront face neutral", text="Дорогой, ты научишься.")
    call process_character (si, appearance="pose handsfront face neutral", text="Ты узнаешь больше о том, как чувствовать себя хорошо очень быстро.")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Но что делать, если я не научусь!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Что если я поранюсь!")
    call process_character (si, appearance="pose handsup face neutral", text="(Он очень волновался по этому поводу)")
    call process_character (si, appearance="pose handsup face neutral", text="(Я надеялся, что этого не произойдет)")
    call process_character (si, appearance="pose handsup face neutral", text="...")
    call process_character (si, appearance="pose handsup face neutral", text="(Я не хочу, чтобы он боялся чего-то, что ему нравится)")
    call process_character (si, appearance="pose handsup face neutral", text="(Я должна найти способ успокоить его)")
    call process_character (si, appearance="pose handsup face neutral", text="...")
    call process_character (si, appearance="pose handsup face neutral", text="[n.say_name]...")
    call process_character (si, appearance="pose handsup face neutral", text="Я...")
    call process_character (si, appearance="pose handsup face neutral", text="Я могу присмотреть за тобой, если хочешь..")
    call process_character (n, appearance="pose twohandfist face embarrassed blush true", text="Ч-что?!")
    call process_character (si, appearance="pose handsfront face curious", text="Я знаю, что это странно.")
    call process_character (si, appearance="pose handsfront face curious", text="Но ты, кажется, обеспокоен этим...")
    call process_character (si, appearance="pose handsfront face curious", text="И единственный способ узнать, правильно ли ты мастурбируешь, это наблюдать за тобой.")
    call process_character (n, appearance="pose handpocket face embarrassed blush true", text="Н-но...")
    call process_character (si, appearance="pose handsup face neutral", text="Я твоя мать, [n.say_name].")
    call process_character (si, appearance="pose handsup face neutral", text="Я хочу, чтобы тебе было комфортно.")
    call process_character (si, appearance="pose handsup face neutral", text="И это то, что я могу предложить.")
    call process_character (n, appearance="pose behindhead face curious blush true", text="...")
    call process_character (si, appearance="pose handsfront face neutral", text="Давай...")
    call process_character (si, appearance="pose handsfront face neutral", text="Просто ложись на кровать..")
    call process_character (si, appearance="pose handsfront face curious", text="Это поможет тебе успокоиться.")
    call process_character (n, appearance="pose handpocket face concerned", text="...")
    call process_character (n, appearance="pose handpocket face concerned", text="О-окей.")

    $ quick_menu = False
    window hide
    $ clear_characters()
    show bg simone_2_bed
    show simone_2_nate_body clothed
    show simone_2_nate_face nervous
    show simone_2_simone worried
    with Dissolve(background_dissolve_speed)
    pause
    $ quick_menu = True


    call process_character (si, text="Так, не торопись.")
    call process_character (si, text="Сними штаны, когда будешь готов.")
    call process_character (n, text="Х-хорошо.")

    $ quick_menu = False
    window hide
    show simone_2_nate_face nervous_blush
    show simone_2_nate_body flaccid
    with Dissolve(background_dissolve_speed)
    pause
    $ quick_menu = True


    call process_character (si, text="...")
    call process_character (si, text="(Это первый раз за последнее время, когда я вижу его...)")
    call process_character (si, text="(Чтобы я видела его в таком состоянии.)")
    call process_character (si, text="Нуу...")
    call process_character (si, text="Твой пенис выглядит нормально, что хорошо.")
    call process_character (n, text="Д-да.")
    call process_character (si, text="[n.say_name]...")
    call process_character (si, text="Я знаю, что прошу о многом...")
    call process_character (si, text="Но мне нужно увидеть твой пенис, когда он эрегирован.")
    call process_character (n, text="!!!")
    call process_character (n, text="Н-но, я слишком нервничаю!")
    call process_character (si, text="Я знаю, милый. Это тяжело.")
    call process_character (si, text="Но подумай о чём-нибудь, что сделает твой пенис твердым.")
    call process_character (n, text="Я ... Я не могу сейчас ничего придумать.")
    call process_character (si, text="О чем ты думал перед тем, как пойти в туалет?")
    call process_character (n, text="Я... Я думал...")
    call process_character (n, text="Я думал о...")

    $ quick_menu = False
    window hide
    show simone_2_nate_face staring_blush
    with Dissolve(background_dissolve_speed)
    pause
    $ quick_menu = True


    call process_character (si, text="(Подожди...)")
    call process_character (si, text="(Он....)")

    $ quick_menu = False
    window hide
    show simone_2_simone shocked_blush
    with Dissolve(background_dissolve_speed)
    pause
    $ quick_menu = True

    call process_character (si, text="(Пялится на мою грудь?!)")
    call process_character (si, text="...")
    call process_character (si, text="(Это то, что он собирался сказать?)")
    call process_character (si, text="(Что он думал о моей груди в прошлый раз?)")
    call process_character (si, text="...")

    $ quick_menu = False
    window hide
    show simone_2_simone worried_blush
    with Dissolve(background_dissolve_speed)
    pause 1.0
    $ quick_menu = True

    call process_character (si, text="[n.say_name]...")
    call process_character (si, text="Ты думал о моей гр...")
    call process_character (sa, text="{b}Мам! Мам!{/b}")
    call process_character (sa, text="Где ты?")

    $ quick_menu = False
    window hide
    show simone_2_nate_face nervous_blush
    with Dissolve(background_dissolve_speed)
    pause 0.75
    $ quick_menu = True

    call process_character (si, text="(Нельзя чтобы [sa.say_name] ворвалась и увидела это!)")
    call process_character (si, text="(Кто знает, что она подумает!)")
    call process_character (si, text="Твоя сестра зовёт меня.")
    call process_character (si, text="Нам придется остановиться.")

    window hide
    hide simone_2_simone
    hide simone_2_nate_body
    hide simone_2_nate_face
    call bust_art_background (nate_room)
    with Dissolve(background_dissolve_speed)

    $ display_multiple_characters([ (n, "outfit clothes pose handsdown face concerned blush true"), (si, "pose armunder face embarrassed blush true") ])
    call process_character (n, appearance="pose handsdown face concerned blush true", text="Прости, Мам, я просто не смог этого сделать...")
    call process_character (si, appearance="pose armunder face embarrassed", text="Я... понимаю [n.say_name].")
    call process_character (si, appearance="pose armunder face embarrassed", text="Это нелегко, когда тебе некомфортно.")
    call process_character (si, appearance="pose armunder face embarrassed", text="Мы можем попробовать в другой раз.")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="Д-да.")
    call process_character (sa, text="Мааам!")
    call process_character (si, appearance="pose handsup face curious blush false", text="Я иду, [sa.say_name]!")
    call process_character (si, appearance="pose armunder face curious", text="Я загляну к тебе скоро, [n.say_name].")
    call process_character (si, appearance="pose armunder face curious", text="...")
    call process_character (si, appearance="pose handsfront face neutral", text="Если захочешь {w=1.0}помастурбировать.")
    call process_character (si, appearance="pose handsfront face neutral", text="Просто будь нежнее.")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="Х-хорошо.")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="Спасибо, Мам.")

    call process_new_location (bg=hallway)

    call process_character (si, appearance="outfit clothes pose handsup face concerned", text="(Я никогда не учила его ничему подобному)")
    call process_character (si, appearance="pose handsup face concerned", text="(Для него это в новинку.)")
    call process_character (si, appearance="pose handsup face concerned", text="...")
    call process_character (si, appearance="pose armunder face embarrassed", text="([n.say_name] смотрел на мою грудь)")
    call process_character (si, appearance="pose armunder face embarrassed", text="(Он действительно думал о ней, когда был в ванной?)")

    python:
        if not dream:
            stats.add_stat("times_had_penis_seen", 1)

    call process_end_of_scene ("simone_scene_2", char=si, dream=dream)

    return

label simone_scene_3:
    $ display_multiple_characters([ (n, ""), (si, "pose handsfront face neutral") ])

    call process_character (si, appearance="pose handsfront face neutral", text="[n.say_name]...")
    call process_character (si, appearance="pose handsfront face neutral", text="Ты готов попробовать то, что мы делали в прошлый раз?")
    call process_character (si, appearance="pose handsfront face neutral", text="Чтобы убедиться, что делаешь всё правильно.")
    call prompt_menu_boldness_check ("М-мы можем попробовать.", "Н-не сейчас.", "simone_scene_3", si)

    return

label simone_scene_3_refusal(text, insufficient_points):
    call process_character (n, appearance="pose behindhead face concerned blush true", text=text)
    if insufficient_points:
        call process_character (n, appearance="pose behindhead face concerned blush true", text="(Я не {b}уверен{/b}, чтобы попробовать это с Мамой)")

    call process_character (si, appearance="pose armunder face neutral", text="(Надеюсь, я не смутила его в прошлый раз.)")
    call prompt_refusal_end (si)

    return

label simone_scene_3_sex(dream=False):
    if si.outfit == "nude":
        call process_scene_beginning (nate_room, char_tuple_array=[ (n, "outfit clothes pose handsdown face concerned"), (si, "outfit clothes pose handsup face neutral") ], dream=dream )
    else:
        call process_scene_beginning (nate_room, char_tuple_array=[ (n, "outfit clothes pose handsdown face concerned"), (si, "pose handsup face neutral") ], dream=dream )

    call process_character (si, appearance="pose handsup face neutral", text="Просто помни, что я сказала.")
    call process_character (si, appearance="pose handsup face neutral", text="Будь осторожен, как сильно ты дёргаешь.")
    call process_character (n, appearance="pose handsdown face concerned", text="О-окей.")
    call process_character (si, appearance="pose armunder face neutral", text="Ты был более расслабленным, когда лежал.")
    call process_character (si, appearance="pose armunder face neutral", text="Я только что застелила простыни на твоей кровати.")
    call process_character (si, appearance="pose armunder face curious", text="Так что тебе должно быть удобно.")

    $ quick_menu = False
    window hide
    $ clear_characters()
    show bg simone_2_bed
    show simone_2_nate_body clothed
    show simone_2_nate_face nervous
    show simone_2_simone worried
    with Dissolve(background_dissolve_speed)
    pause
    $ quick_menu = True


    call process_character (si, text="Начнём, когда ты почувствуешь, что готов, милый.")
    call process_character (n, text="Х-хорошо.")

    $ quick_menu = False
    window hide
    show simone_2_nate_face nervous_blush
    show simone_2_nate_body flaccid
    with Dissolve(background_dissolve_speed)
    pause
    $ quick_menu = True


    call process_character (si, text="...")

    $ quick_menu = False
    window hide
    show simone_2_simone happy
    with Dissolve(background_dissolve_speed)
    pause
    $ quick_menu = True

    call process_character (si, text="(Я, наверное, предвзята, но...)")
    call process_character (si, text="(Пенис моего сына такой милый)")
    show simone_2_simone worried
    with Dissolve(background_dissolve_speed)
    call process_character (si, text="Ты все еще нервничаешь?")
    call process_character (n, text="Д-да.")
    call process_character (si, text="Как я говорила раньше...")
    call process_character (si, text="Подумай о чем-нибудь, что сделает твой пенис твердым.")
    call process_character (n, text="...")

    show simone_2_nate_face staring_blush
    with Dissolve(background_dissolve_speed)

    call process_character (n, text="...")
    call process_character (si, text="...")

    $ quick_menu = False
    window hide
    show simone_2_simone shocked_blush
    show simone_2_nate_face staring_blush
    with Dissolve(background_dissolve_speed)
    pause
    $ quick_menu = True

    call process_character (si, text="(Он опять пялится на мою грудь?)")
    call process_character (si, text="...")

    show simone_2_simone worried_blush
    with Dissolve(background_dissolve_speed)

    call process_character (si, text="(Нет никаких сомнений)")
    call process_character (si, text="...")
    call process_character (si, text="[n.say_name]?")

    show simone_2_nate_face nervous_blush
    with Dissolve(background_dissolve_speed)

    call process_character (n, text="Д-да?")
    call process_character (si, text="Ты смотришь на мою грудь?")
    call process_character (n, text="Я-я-я-...")
    call process_character (si, text="...")

    show simone_2_simone worried
    with Dissolve(background_dissolve_speed)


    call process_character (si, text="Не стоит расстраиваться.")
    call process_character (si, text="Я должна была догадаться.")
    call process_character (si, text="Думать о груди - обычное дело, когда пытаешься мастурбировать.")
    call process_character (n, text="...")
    call process_character (si, text="Несмотря на то, что я твоя мама...")
    call process_character (si, text="Ты просто сфокусируйся на моей груди для возбуждения.")
    call process_character (n, text="...{p}...")
    call process_character (n, text="М-мама?")
    call process_character (si, text="Да?")
    call process_character (n, text="М-могу я увидеть...")
    call process_character (n, text="твою грудь?")

    show simone_2_simone shocked_blush
    with Dissolve(background_dissolve_speed)

    call process_character (si, text="!!!")
    call process_character (si, text="Я...")
    call process_character (si, text="(Не могу поверить, что мой сын об этом спросил!)")
    call process_character (si, text="(Он хочет, чтобы его собственная мать, показала грудь!?)")
    call process_character (si, text="...{p}...")

    show simone_2_simone worried_blush
    with Dissolve(background_dissolve_speed)

    call process_character (si, text="(Я знаю, что это странно для него)")
    call process_character (si, text="(И он стесняется всей этой ситуации.)")
    call process_character (si, text="...")
    call process_character (si, text="Это...поможет тебе?")
    call process_character (si, text="Если ты увидишь...")
    call process_character (si, text="Мою грудь?")
    call process_character (n, text="Д-да.")
    call process_character (si, text="(Я не могу и представить, почему он находит мою грудь привлекательной)")
    call process_character (si, text="(Он намного старше, чем выглядит, я уверена)")
    call process_character (si, text="...")
    call process_character (si, text="(Я не могу заставить себя обнажить её всю)")
    call process_character (si, text="(Я предложу ему компромисс)")
    call process_character (si, text="Ты можешь смотреть на мою грудь, но в лифчике.")
    call process_character (si, text="Хорошо?")
    call process_character (n, text="О-окей.")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)

    $ quick_menu = False
    window hide
    hide simone_2_simone
    hide simone_2_nate_body
    hide simone_2_nate_face
    call static_still ("bg simone_2_removes_top")
    with Dissolve(background_dissolve_speed)
    pause

    call process_character (si, text="(Постарайся не думать слишком много об этом...)")

    call static_still_ctc ("bg simone_2_top_removed")

    call process_character (si, text="В-вот...")
    call process_character (n, text="(Уауу...)")
    call process_character (n, text="...")
    call process_character (n, text="М-мам?")
    call process_character (si, text="...")
    call process_character (si, text="Да?")
    call process_character (n, text="М-мой пенис становится твёрдым.")
    call process_character (si, text="...")
    call process_character (n, text="...")
    call process_character (n, text="Ничего, если я посмотрю на них спереди?")
    call process_character (si, text="...{p}...")
    call process_character (si, text="Все, что угодно, лишь бы помогло тебе...")
    call process_character (n, text="Могу я также посмотреть на них сверху вниз?")
    call process_character (si, text="...")
    call process_character (si, text="Для этого мне придется встать на колени.")
    call process_character (si, text="...")
    call process_character (si, text="Может я подушку под колени?")
    call process_character (si, text="Здесь жесткий пол.")
    call process_character (n, text="К-конечно...")

    call static_still_ctc ("bg simone_2_fapping_to_bra")

    call process_character (si, text="(Я действительно стараюсь изо всех сил...)")
    call process_character (n, text="(С-сиськи моей Мамы...)")
    call process_character (n, text="(Какие большие...)")
    call process_character (si, text="(Он так быстро двигает рукой!)")
    call process_character (si, text="...")
    call process_character (si, text="(Но не похоже, что он тянет слишком сильно)")
    call process_character (si, text="...")
    call process_character (si, text="(Ему так нравится смотреть на мою грудь?)")
    call process_character (si, text="...{p}...")
    call process_character (si, text="(Странно)")
    call process_character (si, text="...")
    call process_character (si, text="(Это не беспокоит меня так сильно, как я думала)")
    call process_character (si, text="(Видя, как мой сын мастурбирует на мою грудь...)")
    call process_character (si, text="...")
    call process_character (si, text="(У моего сына, кажется, очень здоровый, молодой пенис)")
    call process_character (si, text="...")
    call process_character (si, text="(И он выглядит очень твёрдым...)")
    call process_character (si, text="(О чём я только думаю?!)")
    call process_character (n, text="Ах! Ммм!")
    call process_character (n, text="(Бьюсь об заклад, они очень мягкие)")
    call process_character (si, text="(Я не должна так думать.)")
    call process_character (si, text="(Это всё для того, чтобы убедиться, что мой сын правильно мастурбирует)")
    call process_character (si, text="(Я просто наблюдаю за ним)")
    call process_character (si, text="...")
    call process_character (si, text="(Такой возбуждённый и чувствительный...)")
    call process_character (si, text="(В смысле!) {w=0.5}(Он здоровый!)")
    call process_character (n, text="(Я что-то чувствую!)")
    call process_character (n, text="(Интересно, если эта белая штука снова выйдет, то..)")
    call process_character (n, text="Ах, Ахххх...")
    call process_character (n, text="Аххххх!")
    call process_character (si, text="!!!")

    $ quick_menu = False
    window hide
    with None
    show bg white
    with Dissolve(1.0)
    pause 0.5
    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
    pause 1.5

    show bg simone_2_cums_on_breasts
    with Dissolve(2)
    $ renpy.pause()

    call process_character (si, text="...")
    call process_character (n, text="...")
    call process_character (n, text="М-мам?")
    call process_character (n, text="Ты в порядке?")
    call process_character (si, text="...")
    call process_character (n, text="Извини меня, Мама!")
    call process_character (si, text="Это...")
    call process_character (si, text="Это не твоя вина, [n.say_name].")
    call process_character (si, text="Я должна была ожидать, что это произойдет..")
    call process_character (n, text="Мне правда очень жаль, Мама!")
    call process_character (n, text="Я должен был сказать тебе, я почувствовал себя забавным.")
    call process_character (si, text="...")
    call process_character (si, text="(Как много он накончал)")
    call process_character (si, text="(Его сперма застряла в моем декольте)")
    call process_character (si, text="...")
    call process_character (si, text="Все в порядке, дорогой.")
    call process_character (si, text="Когда ты чувствуешь себя хорошо от мастурбации, то не следишь за собой и думаешь только о том, насколько хорошо это чувство.")
    call process_character (si, text="Но ты устроил настоящий беспорядок.")
    call process_character (n, text="Я могу помочь тебе прибраться.")

    call process_character (si, text="Нет, все в порядке.")
    call process_character (si, text="В любом случае, ты бы на меня попал.")
    call process_character (si, text="Я сейчас все здесь уберу.")
    call process_character (n, text="Мам...")
    call process_character (n, text="Я чувствую сонливость.")
    call process_character (si, text="Почему бы тебе не вздремнуть?")
    call process_character (si, text="Еще не время для еды.")
    call process_character (n, text="О-окей.")
    call process_character (si, text="Отдохни немного.")
    call process_character (si, text="Я позову тебя, когда обед будет готов.")
    call process_character (si, text="...")
    call process_character (si, text="(Я не должна была заходить так далеко.)")
    call process_character (si, text="(Но я не хотела, чтобы он поранился.)")

    call static_still_ctc ("bg simone_2_looks_at_cum")

    call process_character (si, text="(Он произвел много спермы)")
    call process_character (si, text="(Она густая и липкая)")
    call process_character (si, text="...")
    call process_character (si, text="(Я не должна больше беспокоиться об этом)")
    call process_character (si, text="(Я знаю, [n.say_name] будет в порядке)")
    call process_character (si, text="...")
    call process_character (si, text="(Но что, если он продолжит думать обо мне?)")


    python:
        if not dream:
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_fapped", 1)
            stats.add_stat("times_ejaculated", 1)

    $ si.revistable_scenes.add("simone_scene_3_revisit")

    call process_end_of_scene ("simone_scene_3", char=si, dream=dream)

    return

label simone_scene_3_revisit:
    if "simone_scene_3_revisit" not in scenes_completed:
        call simone_scene_3_revisit_first_time
    else:
        call simone_scene_3_revisit_second_time

    return

label simone_scene_3_revisit_first_time:
    call process_character (n, appearance="pose handpocket face concerned")
    call process_character (si, appearance="pose handsfront face embarrassed", text="...")
    call process_character (si, appearance="pose handsfront face embarrassed", text="Мне {w=0.5}проверить еще раз?")
    call process_character (n, appearance="pose handpocket face concerned", text="Пожалуйста?")
    call process_character (si, appearance="pose armunder face neutral", text="Ну...")
    call process_character (si, appearance="pose armunder face neutral", text="Ты так мило попросил.")
    call process_character (si, appearance="pose armunder face curious", text="Хорошо, я сделаю это для тебя.")

    $ quick_menu = False
    window hide
    $ clear_characters()
    show bg simone_2_bed
    show simone_2_nate_body clothed

    if "simone_scene_blowjob" not in scenes_completed:
        show simone_2_nate_face nervous
        show simone_2_simone worried
    else:
        show simone_2_nate_face expecting
        show simone_2_simone happy

    with Dissolve(background_dissolve_speed)
    pause
    $ quick_menu = True

    if "simone_scene_blowjob" not in scenes_completed:
        call process_character (si, text="Ты чувствуешь себя лучше, когда я здесь?")
        menu:
            "Д-да, это меня успокаивает.":
                call process_character (si, text="Ну, я не всегда могу быть рядом, когда ты...")
                call process_character (si, text="Возбуждён.")
                call process_character (si, text="Ты должен чувствовать себя более уверенным, чтобы делать это правильно без моего контроля.")
                call process_character (si, text="...")
            "Я...мне легче делать это, когда ты здесь.":
                show simone_2_simone worried_blush
                with Dissolve(background_dissolve_speed)
                call add_boldness (1, tag="simone_scene_3_feel_more_secure")
                call process_character (si, text="Понятно...")
                call process_character (si, text="(Что он имеет в виду под этим?)")
                call process_character (si, text="(Он меньше нервничает, когда я здесь?)")
                call process_character (si, text="(Или он имеет в виду, что ему легче, потому что он может смотреть на меня...)")
                show simone_2_simone worried
                with Dissolve(background_dissolve_speed)

    call process_character (si, text="Как только почувствуешь, что готов.")
    $ quick_menu = False
    window hide
    show simone_2_nate_body flaccid
    if "simone_scene_blowjob" not in scenes_completed:
        show simone_2_nate_face nervous_blush
    else:
        show simone_2_nate_face expecting_blush

    with Dissolve(background_dissolve_speed)
    pause 1.0
    $ quick_menu = True

    call process_character (n, text="...")
    call process_character (si, text="...")
    call process_character (n, text="Я...")
    call process_character (n, text="У меня возникли проблемы.")
    call process_character (si, text="Почему у тебя проблемы?")
    call process_character (n, text="Я думаю, это потому что...")
    call process_character (n, text="...")

    show simone_2_nate_face staring_blush
    with Dissolve(background_dissolve_speed)
    call process_character (n, text="...")

    if "simone_scene_blowjob" not in scenes_completed:
        show simone_2_simone shocked_blush
    else:
        pause 0.5
        show simone_2_simone happy_blush

    with Dissolve(background_dissolve_speed)


    call process_character (si, text="(Он снова на них смотрит!)")
    call process_character (si, text="...")

    if "simone_scene_blowjob" not in scenes_completed:
        show simone_2_simone worried_blush
        with Dissolve(background_dissolve_speed)

    call process_character (si, text="(Я должна была догадаться...)")
    call process_character (si, text="Это потому что тебе нужно снова увидеть меня в лифчике?")

    if "simone_scene_blowjob" not in scenes_completed:
        show simone_2_nate_face nervous_blush
        with Dissolve(background_dissolve_speed)
    else:
        show simone_2_nate_face expecting_blush
        with Dissolve(background_dissolve_speed)

    call process_character (n, text="...")
    call process_character (n, text="Д-да.")

    if "simone_scene_blowjob" not in scenes_completed:
        call process_character (si, text="...")
        call process_character (si, text="(Если я сделаю это для него...)")
        call process_character (si, text="(Будет ли он думать, что я просто помогу ему с этим, когда у него будет желание?)")
        call process_character (si, text="(Что, если мой сын начнет думать, что я просто материал для мастурбации?)")
        call process_character (si, text="...")
        call process_character (si, text="(Нет, я знаю, что мой сын не сделал бы этого)")
        call process_character (si, text="(Он попросил моей помощи, потому что я его мама)")
        call process_character (si, text="(Он доверяет мне больше, чем кому-либо)")

    call process_character (n, text="Э... это нормально, Мам?")

    if "simone_scene_blowjob" not in scenes_completed:
        call process_character (si, text="...")

    call process_character (si, text="Да, это нормально.")
    call process_character (si, text="Просто, дай мне минутку...")

    python hide:
        play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)

    $ quick_menu = False
    window hide
    hide simone_2_simone
    hide simone_2_nate_body
    hide simone_2_nate_face
    call static_still ("bg simone_2_removes_top")
    with Dissolve(background_dissolve_speed)
    pause

    call static_still_ctc ("bg simone_2_top_removed")

    call process_character (si, text="Хорошо.")

    call static_still_ctc ("bg simone_2_fapping_to_bra")

    call process_character (si, text="...")
    call process_character (si, text="(Он схватился за член так быстро!)")
    call process_character (n, text="(Я очень рад, что мама позволила мне увидеть ее сиськи снова)")
    call process_character (n, text="(Даже если они просто в лифчике)")
    call process_character (n, text="Ах...")
    call process_character (si, text="(Я не должна так смотреть на него)")
    call process_character (si, text="([n.say_name], кажется, все равно)")
    call process_character (si, text="(Но опять же, он зациклен на других вещах...)")

    if "simone_scene_blowjob" not in scenes_completed:
        call process_character (si, text="(У него нет проблем, которые я могу увидеть)")
        call process_character (si, text="(На самом деле у него получается)")
        call process_character (si, text="(Он крепко обхватил рукой свой стержень...)")
        call process_character (si, text="!!!")
        call process_character (si, text="(Я имею в виду, что он осторожен с этим!)")
    else:
        call simone_scene_3_revisit_blowjob_ask

    call process_character (n, text="Ах, ах...")
    call process_character (n, text="М-Мам?")
    call process_character (si, text="Мм?")
    call process_character (n, text="Ах, ахх...")
    call process_character (n, text="Я чувствую себя так же, как в прошлый раз.")
    call process_character (si, text="Ты имеешь в виду, когда ты испачкался?")
    call process_character (n, text="Д-да.")
    call process_character (si, text="Тогда...")

    if "simone_scene_blowjob" not in scenes_completed:
        call process_character (si, text="Когда ты почувствуешь, что это произойдет...")
        call process_character (si, text="Дай мне знать.")
        call process_character (n, text="Вообще-то...")
        call process_character (n, text="Мне понравилось, когда она попала на твои...")
        call process_character (n, text="Твои сиськи.")
        call process_character (si, text="!!!")
        call process_character (si, text="[n.say_name] [store.last_name]!")
        call process_character (n, text="{i}Глык{i}...")
        call process_character (si, text="Ты ведешь себя очень свежо.")
        call process_character (n, text="...")
        call process_character (si, text="...")
        call process_character (si, text="Ты ведь не специально сделал это раньше, правда?")
        call process_character (n, text="Я-я не специально, клянусь!")
        call process_character (n, text="Я не знал, куда выстрелит белая штука!")
        call process_character (n, text="Я не хочу, чтобы на тебе была белая штука, если ты будешь злиться на меня!")
        call process_character (si, text="...")
        call process_character (si, text="Мне жаль, если ты подумал, что я злюсь на тебя, [n.say_name].")
        call process_character (si, text="Я была просто удивлена, что ты хотел сделать что-то подобное.")
        call process_character (n, text="Мне правда очень жаль, Мама.")
        call process_character (si, text="...{p}...")
        call process_character (si, text="Если я позволю тебе сделать это...")
        call process_character (si, text="Ты должен сохранить это между нами, хорошо?")
        call process_character (si, text="Это самый большой секрет, который ты должен хранить.")
        call process_character (n, text="Я буду держать это в секрете.")
        call process_character (si, text="Я знаю, как мой сын, ты честен.")
        call process_character (si, text="Поэтому я поверю тебе на слово.")
        call process_character (si, text="...")
        call process_character (si, text="(Не могу поверить, что я собираюсь это сделать)")
        call process_character (si, text="(Может быть, это будет один раз)")
        call process_character (si, text="(Я строго с ним поговорила)")
        call process_character (si, text="(И он должен знать, что это редкое событие для него)")
    else:
        call simone_scene_3_revisit_second_time_cum_on_breasts_ask

    call process_character (n, text="(У-уже почти...)")
    call process_character (n, text="Ах!")
    call process_character (n, text="(Я чувствую это!)")
    call process_character (n, text="Ах, ах.")
    call process_character (si, text="(Я надеюсь, что он может контролировать, куда кончит...)")
    call process_character (n, text="(Я кончу на мою маму...)")

    $ quick_menu = False
    window hide
    with None
    show bg white
    with Dissolve(1.0)
    pause 0.5
    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
    pause 1.5

    show bg simone_2_cums_on_breasts
    with Dissolve(2)
    $ renpy.pause()

    call process_character (n, text="Ахххх!")
    call process_character (si, text="!!!")
    call process_character (si, text="(Я запуталась!)")
    call process_character (n, text="(Вся эта штука попала на ее сиськи!)")
    call process_character (si, text="(Она все еще капает)")
    call process_character (si, text="(Я никогда не видела столько спермы от одной эякуляции!)")
    call process_character (n, text="...")
    call process_character (n, text="Я старался изо всех сил быть осторожным, куда попаду, мама.")
    call process_character (n, text="П-прости.")
    call process_character (si, text="...")
    call process_character (si, text="Я знаю, что ты действительно пытался.")
    call process_character (si, text="По тебе было видно, что ты чувствуешь себя замечательно.")
    call process_character (n, text="Мне действительно хорошо.")
    call process_character (si, text="Ну, вот что важно.")
    call process_character (n, text="Мама...")
    call process_character (n, text="Это нормально чувствовать усталость после?")
    call process_character (si, text="Это нормально для многих людей, [n.say_name], да.")
    call process_character (n, text="Э-это хорошо.")
    call process_character (si, text="Если ты собираешься отдохнуть...")
    call process_character (si, text="Сначала я постелю сверху простыню.")
    call process_character (si, text="Здесь нужно немного почистить.")
    call process_character (n, text="Окей.")
    call process_character (n, text="Спасибо, Мам.")

    call static_still_ctc ("bg simone_2_looks_at_cum")

    call process_character (si, text="(У меня есть чувство, что с этого момента мне придётся стирать больше...)")

    python:
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_fapped", 1)
        stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene ("simone_scene_3_revisit", char=si, force_no_boldness=True, reset_prompted_scene=False, force_not_replayable=True, revisit=True)
    return

label simone_scene_3_revisit_blowjob_ask:
    call process_character (si, text="(У меня такой похотливый сын)")
    call process_character (si, text="(Хотя я не могу винить его за все это)")
    call process_character (si, text="(Я продолжила насыщать его возбуждение)")
    call process_character (si, text="...")
    call process_character (si, text="(Мне понравилось, когда он выстрелил её...)")
    call process_character (si, text="(Когда он закрыл мое лицо)")
    call process_character (si, text="(Я была так взволнована от этого)")
    call process_character (si, text="(Яблоко от яблони, я думаю...)")
    call process_character (si, text="(Он захочет чего-то большего)")
    call process_character (si, text="(Ты просто попросишь снять бюстгальтер, знаю, что я могу...)")
    call process_character (si, text="[n.say_name]?")
    call process_character (si, text="Тебе...")
    call process_character (si, text="Нужна дополнительная помощь от меня?")

    menu:
        "Д-Да Мам!":
            call simone_scene_blowjob_revisit (start_naked=True)
        "Д-думаю, что в я порядке.":
            call process_character (si, text="Все в порядке, дорогой.")

    return

label simone_scene_3_revisit_second_time:
    call process_character (n, appearance="pose handpocket face concerned")
    call process_character (si, appearance="pose handsfront face embarrassed", text="Ну, хорошо...")

    $ quick_menu = False
    window hide
    $ clear_characters()
    show bg simone_2_bed
    show simone_2_nate_body flaccid
    show simone_2_nate_face expecting_blush

    if "simone_scene_blowjob" not in scenes_completed:
        show simone_2_simone worried
    else:
        show simone_2_simone happy

    with Dissolve(background_dissolve_speed)
    pause
    $ quick_menu = True



    call process_character (si, text="...")
    call process_character (si, text="Полагаю, ты этого хочешь...")
    call process_character (si, text="Снять с меня рубашку?")

    $ quick_menu = False
    window hide
    pause 0.25
    show simone_2_nate_face staring_blush
    with Dissolve(background_dissolve_speed)
    pause 0.75
    show simone_2_nate_body fapping
    with Dissolve(1.25)

    if "simone_scene_blowjob" not in scenes_completed:
        show simone_2_simone worried_blush
    else:
        show simone_2_simone happy_blush
    with Dissolve(background_dissolve_speed)

    pause

    call process_character (n, text="Д-да.")

    python hide:
        play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)

    $ quick_menu = False
    window hide
    hide simone_2_simone
    hide simone_2_nate_body
    hide simone_2_nate_face
    call static_still ("bg simone_2_removes_top")
    with Dissolve(background_dissolve_speed)
    pause

    call static_still_ctc ("bg simone_2_top_removed")
    call static_still_ctc ("bg simone_2_fapping_to_bra")

    if "simone_scene_blowjob" not in scenes_completed:
        call process_character (si, text="(Я думаю, что это стало обыденно)")
        call process_character (si, text="(Я не знаю, будет ли это иметь положительное или отрицательное влияние на него)")
        call process_character (si, text="(Это не совсем нормально мастурбировать на грудь своей матери...)")
        call process_character (si, text="(Может быть, он найдёт что-то в интернете и будет возбуждаться на это)")
        call process_character (si, text="...")
        call process_character (si, text="(Но я не хочу, чтобы у него были неприятности...)")
        call process_character (si, text="(По крайней мере то, что он делает здесь...)")
        call process_character (si, text="(Это то, о чем я знаю)")
    else:
        call simone_scene_3_revisit_blowjob_ask

    call process_character (n, text="Ах, ах...")
    call process_character (n, text="М-Мам?")
    call process_character (si, text="Да [n.say_name]?")
    call process_character (n, text="Ах, ахх...")
    call process_character (n, text="У меня такое чувство, что...")
    call process_character (si, text="Ты уже почти?")
    call process_character (n, text="Ммм...")

    if "simone_scene_blowjob" not in scenes_completed:
        call simone_scene_3_revisit_second_time_cum_on_breasts_ask
        call process_character (si, text="Я полагаю ты захочешь, раз уж я позволила тебе раньше...")
    else:
        call process_character (si, text="Тогда, когда будешь готов...")
        call process_character (si, text="И не осторожничай.")
        call process_character (si, text="Просто чувствуй себя так хорошо, как можешь.")
        call process_character (si, text="Моя грудь ждет тебя.")

    call process_character (n, text="(Почти...)")
    call process_character (n, text="Ах!")
    call process_character (n, text="(Я чувствую это!)")
    call process_character (n, text="Ах, ах.")
    call process_character (si, text="...")

    $ quick_menu = False
    window hide
    with None
    show bg white
    with Dissolve(1.0)
    pause 0.5
    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
    pause 1.5

    show bg simone_2_cums_on_breasts
    with Dissolve(2)
    $ renpy.pause()

    call process_character (n, text="Ахххх!")
    call process_character (si, text="!!!")
    call process_character (n, text="Ах. Ах...")

    if "simone_scene_blowjob" not in scenes_completed:
        call process_character (si, text="(Как удаётся моему сыну производить столько спермы!?)")
        call process_character (si, text="(Она покрывает меня!)")
        call process_character (si, text="...")
        call process_character (si, text="(И она удивительно густая...)")
        call process_character (si, text="!")
        call process_character (si, text="(Ч-что означает, что он здоров! И это замечательно!)")
        call process_character (si, text="...")
        call process_character (si, text="Ты хорошо себя чувствуешь, [n.say_name]?")
        call process_character (n, text="Я-я...")
        call process_character (n, text="...")
        call process_character (n, text="Мама...")
        call process_character (si, text="Да?")
        call process_character (n, text="Мне нравится делать это с тобой.")
        call process_character (si, text="!!!")
        call process_character (si, text="[n.say_name]...")
        call process_character (si, text="Я говорила тебе...")
        call process_character (si, text="В конце концов, это должно быть сделано без меня.")
        call process_character (si, text="Ты не должен каждый раз нуждаться в моей помощи.")
        call process_character (n, text="...")
        call process_character (si, text="Тебе все равно понравится, не волнуйся.")
        call process_character (si, text="...{p}...")
        call process_character (si, text="(Надеюсь, он в это поверит...)")
    else:
        call process_character (si, text="(О, боже мой!)")
        call process_character (si, text="(Он всегда удивляет меня количеством, которое он выстреливает!)")
        call process_character (si, text="(И она вся густая)")
        call process_character (si, text="(А какой приятный аромат...)")
        call process_character (si, text="...")
        call process_character (si, text="Милый, ты выглядишь замученным.")
        call process_character (si, text="Ты вздремнёшь?")
        call process_character (n, text="{i}Зевок{/i}...")
        call process_character (n, text="Я думаю, да...")
        call process_character (si, text="Не забудь помыться перед сном, ладно?")
        call process_character (n, text="Окей.")


    python:
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_fapped", 1)
        stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene ("simone_scene_3_revisit", char=si, force_no_boldness=True, reset_prompted_scene=False, force_not_replayable=True, revisit=True)
    return

label simone_scene_3_revisit_second_time_cum_on_breasts_ask:
    call process_character (si, text="...")
    call process_character (si, text="(Я должна ждать, пока он спросит?)")
    call process_character (si, text="(Даже если бы он спросил, я бы действительно сказала нет?)")
    call process_character (si, text="[n.say_name]...")
    call process_character (si, text="Ты собирался спросить, можно ли {w=1.0}кончить мне на грудь?")
    call process_character (n, text="Я...я собирался это сделать...")
    call process_character (si, text="(Как только ты открываешь дверь, ты уже не сможешь ее закрыть)")
    call process_character (si, text="Не нужно больше спрашивать...")

    return

label simone_scene_yoga_1(dream=False):
    call simone_scene_yoga_1_sex (dream=dream)

    return

label simone_scene_yoga_1_sex(dream=False):
    call process_scene_beginning (bg=simone_room, char_tuple_array=[ (n, "outfit clothesjacket face curious"), (si, "outfit yoga pose handsfront face neutral") ], dream=dream )
    call process_character (n, appearance="pose handpocket face curious", text="(Мне нравится одежда Мамы...)")
    call process_character (n, appearance="pose handpocket face curious", text="...")

    call process_character (si, appearance="pose handsfront face neutral", text="О! [n.say_name], я и не знала, что ты здесь.")
    call process_character (n, appearance="pose handpocket face curious blush false")
    call process_character (si, appearance="pose handsfront face neutral", text="Я слишком увлеклась йогой.")
    call process_character (n, appearance="pose behindhead face curious", text="Йога?")
    call process_character (si, appearance="pose handsup face neutral", text="Это такие упражнения.")
    call process_character (si, appearance="pose handsup face neutral", text="Они способствуют гибкости тела и снятию стресса.")
    call process_character (n, appearance="pose handpocket face concerned", text="...")
    call process_character (n, appearance="pose handpocket face concerned", text="Мама, ты нервничаешь?")
    call process_character (si, appearance="pose armunder face neutral", text="Этот переезд нервы изрядно потрепал.")
    call process_character (si, appearance="pose armunder face neutral", text="Я думала, что это будет легко и быстро.")
    call process_character (si, appearance="pose handsfront face neutral", text="Но было так много подводных камней, к которым я не была готова.")
    call process_character (n, appearance="pose twohandfist face neutral", text="Я могу чем-нибудь помочь?")
    call process_character (si, appearance="pose handsup face happy", text="Ты такой милый, [n.say_name]!")
    call process_character (si, appearance="pose handsup face neutral", text="Я ценю твою помощь, но я в порядке.")
    call process_character (n, appearance="pose handpocket face neutral", text="Хорошо, Мама.")
    call process_character (si, appearance="pose handsfront face neutral", text="[k.say_name] дала несколько уроков по йоге.")
    call process_character (si, appearance="pose armunder face embarrassed", text="Некоторые из этих поз кажутся немного сложными.")
    call process_character (n, appearance="pose handfist face neutral", text="Ты сможешь, мама!")
    call process_character (n, appearance="pose handfist face neutral", text="Просто сконцентрируйся!")
    call process_character (si, appearance="pose armunder face happy", text="Я думаю, что мне нужно что-то большее, чем просто концентрация, чтобы выполнить все упражнения.")
    call process_character (si, appearance="pose armunder face happy", text="(У меня нет такого атлетического тела, как у твоей сестры.)")
    call process_character (si, appearance="pose handsfront face neutral", text="(Чем [k.say_name] думала, показывая такие упражнения?)")
    call process_character (si, appearance="pose handsfront face neutral", text="Если я не буду торопиться, все будет хорошо.")
    call process_character (n, appearance="pose handpocket face neutral", text="Хорошо!")
    call process_character (n, appearance="pose handpocket face neutral", text="...")
    call process_character (n, appearance="pose behindhead face curious", text="Мам?")
    call process_character (si, appearance="pose handsfront face neutral", text="Да, [n.say_name]?")
    call process_character (n, appearance="pose behindhead face curious", text="Могу я посмотреть, как ты занимаешься йогой?")
    call process_character (si, appearance="pose armunder face embarrassed", text="Смотреть, как я занимаюсь йогой?")
    call process_character (si, appearance="pose armunder face embarrassed", text="Я совсем не разбираюсь в этом.")
    call process_character (si, appearance="pose armunder face embarrassed", text="...")
    call process_character (si, appearance="pose armunder face embarrassed", text="Но если тебе интересно, то конечно.")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (si, appearance="pose handsup face happy", text="Но если я упаду на лицо, это не считается техникой йоги!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Ну так я могу посмотреть?")
    call process_character (n, appearance="pose twohandfist face neutral", text="Конечно!")
    call process_character (si, appearance="pose handsup face neutral", text="Но сделайте мне одолжение.")
    call process_character (n, appearance="pose handpocket face neutral", text="Какое?")
    call process_character (si, appearance="pose handsfront face neutral", text="Если я завернусь в крендель...")
    call process_character (si, appearance="pose armunder face happy", text="Ты развяжешь меня?")
    call process_character (n, appearance="pose handpocket face curious", text="...")
    call process_character (n, appearance="pose handpocket face curious", text="Да, само собой.")
    call process_character (si, appearance="pose handsfront face happy", text="Надеюсь, этого не случится...")
    call process_character (si, appearance="pose handsfront face happy", text="Твоя мать может только наклоняться!")


    call process_end_of_scene ("simone_scene_yoga_1", char=si, dream=dream, force_no_boldness=True)

    return

label simone_scene_yoga_2(dream=False):
    call simone_scene_yoga_2_sex (dream=dream)

    return

label simone_scene_yoga_2_sex(dream=False):
    call process_scene_beginning (bg=simone_room, char_tuple_array=[ (n, "outfit clothesjacket face neutral"), (si, "outfit yoga pose handsfront face neutral") ], dream=dream )
    call process_character (n, appearance="pose handpocket face neutral", text="Привет, Мам!")
    call process_character (n, appearance="pose handpocket face neutral", text="Хочешь еще позаниматься йогой?")
    call process_character (si, appearance="pose armunder face happy", text="\"Попробовать заниматься\" правильное слово!")
    call process_character (si, appearance="pose armunder face neutral", text="В прошлый раз я вывихнула спину.")
    call process_character (si, appearance="pose handsup face neutral", text="Я говорила [k.say_name], что нужно начинать с растяжки.")
    call process_character (si, appearance="pose handsup face happy", text="Теперь я не смогу крутить ногой за головой!")
    call process_character (n, appearance="pose behindhead face curious", text="Разве такое вообще возможно?")
    call process_character (si, appearance="pose armunder face happy", text="Я сказал то же самое!")
    call process_character (si, appearance="pose armunder face happy", text="Может быть, для ловкой гимнастки, но не для зрелой мамочки!")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (si, appearance="pose handsfront face neutral", text="Я делаю это для расслабления.")
    call process_character (n, appearance="pose handpocket face neutral", text="Круто.")
    call process_character (si, appearance="pose handsfront face happy", text="Ха-ха, что я делаю \"круто\"?")
    call process_character (n, appearance="pose behindhead face neutral", text="Нуу...")
    call process_character (n, appearance="pose behindhead face neutral", text="Ты делаешь то, что я не могу сделать.")
    call process_character (n, appearance="pose behindhead face neutral", text="Так что это довольно круто.")
    call process_character (si, appearance="pose armunder face neutral", text="О, я уверена, ты сможешь это сделать, милый.")
    call process_character (si, appearance="pose armunder face neutral", text="Йогой может заниматься любой.")
    call process_character (si, appearance="pose armunder face happy", text="Попробуй вместе со мной.")
    call process_character (n, appearance="pose handpocket face neutral", text="Ты думаешь, я смогу это сделать?")
    call process_character (si, appearance="pose handsup face neutral", text="Конечно!")
    call process_character (si, appearance="pose handsup face neutral", text="Почему бы тебе не попробовать вместе со мной?")
    call process_character (si, appearance="pose handsup face neutral", text="Я сниму твою куртку, чтобы ты был более гибким.")
    call process_character (n, appearance="pose handpocket face neutral", text="Хорошо.")

    call character_leave_dissolve (n)
    $ renpy.pause(1)

    call process_character (n, appearance="outfit clothes pose handsdown face neutral")
    call process_character (si, appearance="pose handsfront face neutral", text="Хорошо, как насчет \"позы дерева\" для начала?")
    call process_character (si, appearance="pose handsfront face happy", text="Надеюсь я не буду \"лесоматериалом!\"")

    call fade_to_black (0.5)
    $ quick_menu = False
    $ renpy.pause(0.5)
    call bust_art_background (simone_room)
    $ quick_menu = True

    $ display_multiple_characters([ (n, "pose handsdown face neutral"), (si, "pose handsup face neutral") ])
    call process_character (si, appearance="pose handsup face neutral", text="Как себя чувствуешь?")
    call process_character (n, appearance="pose twohandfist face neutral", text="Некоторые из этих растяжек были сложными!")
    call process_character (si, appearance="pose handsfront face neutral", text="Ты отлично справился с ними!")
    call process_character (si, appearance="pose handsfront face neutral", text="Не хочешь сделать перерыв на минутку?")
    call process_character (n, appearance="pose handsdown face neutral", text="Да.")
    call process_character (si, appearance="pose armunder face neutral", text="Я собираюсь сделать еще несколько.")
    call process_character (n, appearance="pose handsdown face neutral", text="(Мама была права)")
    call process_character (n, appearance="pose handsdown face neutral", text="(Это расслабляет)")
    call process_character (n, appearance="pose handsdown face neutral", text="(Но это утомило меня)")
    call process_character (n, appearance="pose handsdown face neutral", text="...")
    call process_character (n, appearance="pose handsdown face neutral", text="(Похоже Мама пытается сделать новую позу)")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)

    $ quick_menu = False
    window hide
    with None
    show mom_tits as mom_tits
    $ clear_characters()
    with Dissolve(1.0)
    pause 
    $ quick_menu = True

    call process_character (n, text="...")
    call process_character (n, text="(М-мамины сиськи трясутся в позе, которую она делает)")
    call process_character (n, text="...")
    call process_character (n, text="(М-мне нравится, как они выпирают из ее рубашки...)")
    call process_character (n, text="...")
    call process_character (n, text="(М-мама обычно не носит такие вещи)")
    call process_character (n, text="(Я никогда не замечал, какие они большие...)")
    call process_character (n, text="...")
    call process_character (n, text="(Ее сиськи двигаются...)")
    call process_character (n, text="(Они должны быть очень нежными и мягкими...)")
    call process_character (n, text="...")
    call process_character (n, text="(Я...)")
    call process_character (n, text="(Я чувствую что-то...)")

    window hide
    hide mom_tits
    with Dissolve(0.5)
    $ display_multiple_characters([ (n, "outfit clothes_hard pose twohandfist face concerned blush true"), (si, "pose handsup face neutral") ])

    call process_character (n, appearance="pose twohandfist face concerned blush true", text="(Ах...)")
    call process_character (n, appearance="pose twohandfist face concerned blush true", text="(Э-это мой пенис....)")
    call process_character (si, appearance="pose armunder face neutral", text="[n.say_name], что-то случилось?")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="Н-неет...")
    call process_character (si, appearance="pose armunder face curious", text="Ты весь покраснел")
    call process_character (si, appearance="pose armunder face neutral", text="Наверное, от всех тех растяжек, что ты сделал.")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="Д-даа...")
    call process_character (si, appearance="pose handsfront face neutral", text="Я как раз заканчиваю..")
    call process_character (si, appearance="pose handsfront face neutral", text="Почему бы тебе не отдохнуть до ужина?")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="О-окей, Мам.")
    call process_character (si, appearance="pose handsup face neutral", text="Хорошая работа по йоге, милый!")


    python:
        si.revistable_scenes.add("simone_scene_yoga_revisit")
        skip_jump = True

        if "simone_scene_yoga_2" in scenes_completed or "simone_scene_1_seq_1" in scenes_completed:
            skip_jump = False

    call process_end_of_scene ("simone_scene_yoga_2", char=si, do_not_jump=skip_jump, dream=dream )

    if skip_jump:
        call simone_scene_1_seq_1_sex

    return

label simone_scene_swimsuit(after_buy_label=False, dream=False):
    call simone_scene_swimsuit_sex (dream=dream)

    return

label simone_scene_swimsuit_sex(dream=False):
    call process_scene_beginning (bg="bg nate_room_daytime", dream=dream)
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text="(Я не видел, что мама ходит в бассейн с тех пор, как мы переехали...)")
    call process_character (n, appearance="pose handpocket face neutral", text="(Вероятно, потому, что у нее еще нет купальника)")
    call process_character (n, appearance="pose twohandfist face neutral", text="(Хорошо теперь она будет!)")

    call process_scene_beginning (bg="bg simone_room_daytime", char_tuple_array=[ (n, "outfit clothesjacket pose twohandfist face neutral"), (si, "outfit clothes pose handsfront face neutral") ], dream=dream, force_bg_change=True)

    call process_character (n, appearance="pose twohandfist face neutral", text="Мама, Мама!")
    call process_character (si, appearance="pose armunder face neutral", text="Ну, ты выглядишь взволнованным!")
    call process_character (si, appearance="pose armunder face neutral", text="В чем дело?")
    call process_character (n, appearance="pose twohandfist face neutral", text="Я купил тебе купальник!")
    call process_character (si, appearance="pose armunder face curious", text="Купальный костюм для меня?")
    call process_character (n, appearance="pose handpocket face neutral", text="Ну, я не видел, чтобы ты ходила в бассейн.")
    call process_character (n, appearance="pose twohandfist face neutral", text="И я подумал, может это потому что у тебя нет купальника!")
    call process_character (si, appearance="pose handsfront face neutral", text="Понятно...")
    call process_character (si, appearance="pose handsfront face neutral", text="Ну, это очень мило с твоей стороны, [n.say_name].")
    call process_character (si, appearance="pose armunder face neutral", text="Но я не думаю, что он мне понадобится.")
    call process_character (n, appearance="pose behindhead face concerned", text="А почему бы и нет?")
    call process_character (si, appearance="pose handsfront face neutral", text="Это трудно объяснить.")
    call process_character (si, appearance="pose handsfront face neutral", text="Но...")
    call process_character (si, appearance="pose armunder face neutral", text="Я бы слишком беспокоилась о том, как выгляжу.")
    call process_character (n, appearance="pose behindhead face curious", text="...")
    call process_character (n, appearance="pose behindhead face curious", text="Что ты имеешь в виду?")
    call process_character (si, appearance="pose handsfront face neutral", text="Ну...")
    call process_character (si, appearance="pose handsfront face neutral", text="Я уже не так молода, как раньше.")
    call process_character (si, appearance="pose handsfront face neutral", text="И мне просто неудобно носить купальник.")
    call process_character (n, appearance="pose handpocket face curious", text="Ох, я понимаю...")
    call process_character (n, appearance="pose handpocket face curious", text="...")
    pause 0.5
    call process_character (n, appearance="pose behindhead face concerned", text="Итак, {w=0.5}ты хочешь, чтобы я вернул его?")
    call process_character (si, appearance="pose handsup face neutral", text="...")
    call process_character (n, appearance="pose handpocket face concerned")
    call process_character (si, appearance="pose handsup face neutral", text="(Посмотрите на его лицо...)")
    call process_character (si, appearance="pose handsup face neutral", text="(Он действительно надеялся, что я буду счастлива с его подарком)")
    call process_character (si, appearance="pose handsup face neutral", text="...")
    call process_character (si, appearance="pose armunder face neutral", text="(Если я скажу ему вернуть его, он почувствует себя очень плохо)")
    call process_character (si, appearance="pose armunder face neutral", text="(Он подумает, что сделал что-то не так)")
    call process_character (si, appearance="pose armunder face neutral", text="Ну, милый...")
    call process_character (si, appearance="pose handsfront face neutral", text="Тебе не нужно его возвращать.")
    call process_character (si, appearance="pose handsfront face neutral", text="Фактически...")
    call process_character (si, appearance="pose handsfront face neutral", text="Я попробую его.")
    call process_character (n, appearance="pose twohandfist face happy", text="Правда?!")
    call process_character (si, appearance="pose handsup face happy", text="Подарок от сына - это нечто особенное.")
    call add_points (si, 2, tag="simone_scene_swimsuit_how_i_look")
    call process_character (si, appearance="pose handsup face happy", text="И меня это волнует больше, как я выгляжу!")
    call process_character (n, appearance="pose handfist face happy", text="Я так рада, что ты собираешься примерить его на маму!")
    call process_character (n, appearance="pose handfist face neutral", text="Я пытался купить что-то вроде купальника, который у тебя был раньше.")
    call process_character (si, appearance="pose armunder face neutral", text="(Тот, который у меня был раньше...)")
    call process_character (si, appearance="pose armunder face neutral", text="(Это было некоторое время назад...)")
    call process_character (si, appearance="pose handsfront face neutral", text="Просто дай мне время переодеться.")
    call process_character (si, appearance="pose handsfront face neutral", text="Я буду в бассейне через некоторое время.")

    call process_scene_beginning (bg="bg backyard_daytime", char_tuple_array=[ (n, "outfit swimsuit pose handfist face neutral")])

    call process_character (n, appearance="pose handfist face neutral", text="(Не могу дождаться, чтобы увидеть маму!)")
    call process_character (n, appearance="pose handfist face neutral", text="(Она, наконец-то, поплавает в бассейне!)")
    call process_character (si, appearance="outfit swimsuit pose handsfront face neutral")
    call process_character (n, appearance="pose handsdown face happy", text="Привет, Мам!")
    call process_character (n, appearance="pose handsdown face happy", text="Тебе нравится?")
    call process_character (si, appearance="pose handsfront face neutral", text="Ты ведь не шутил.")
    call process_character (si, appearance="pose handsfront face neutral", text="Ты купил почти такой же купальник для меня.")
    call process_character (si, appearance="pose handsfront face embarrassed", text="(Включая слишком малый размер...)")

    if "simone_scene_2" in scenes_completed:
        call process_character (n, appearance="pose twohandfist face neutral", text="(Её сиськи так хорошо видны!)")
        call process_character (n, appearance="pose twohandfist face neutral", text="(Я думаю, что вижу даже больше, чем, когда она показала мне их в бюстгальтере в моей комнате!)")
        call process_character (si, appearance="pose armunder face embarrassed", text="(Он довольно долго пялится...)")
        call process_character (si, appearance="pose armunder face embarrassed", text="(Я надеюсь, что он не купил это, чтобы смотреть на меня...)")
        call process_character (si, appearance="pose armunder face embarrassed", text="(Этот костюм едва может вместить мою грудь!)")
    else:
        call process_character (n, appearance="pose handsdown face neutral", text="(Это похоже на ее старый костюм)")
        call process_character (n, appearance="pose behindhead face curious", text="(Но ее сиськи теперь намного больше...)")

    call process_character (n, appearance="pose handfist face neutral", text="Ты собираешься поплавать, мама?")
    call process_character (si, appearance="pose armunder face neutral", text="Я пока повременю с этим.")
    call process_character (si, appearance="pose handsup face neutral", text="Я все еще привыкаю к этому костюму.")
    call process_character (si, appearance="pose handsup face neutral", text="Он немного...")
    call process_character (si, appearance="pose handsup face embarrassed", text="Плотно сидит.")
    call process_character (n, appearance="pose twohandfist face neutral", text="Ты можешь просто сидеть на солнце!")
    call process_character (n, appearance="pose twohandfist face neutral", text="[k.say_name] делает это все время.")
    call process_character (si, appearance="pose armunder face happy", text="Я бы поджарилась на этом солнце.")
    call process_character (si, appearance="pose armunder face happy", text="Через несколько часов я буду красной, как лобстер!")
    call process_character (n, appearance="pose handsdown face neutral")
    call process_character (si, appearance="pose handsfront face neutral", text="Думаю, я поставлю зонтик и посижу в тени.")
    call process_character (si, appearance="pose handsfront face neutral", text="Я могу почитать о садоводстве.")
    call process_character (n, appearance="pose twohandfist face neutral", text="Хорошо, Мам!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Я собираюсь прыгнуть в бассейн!")
    call process_character (si, appearance="pose handsup face curious", text="Не забудь нанести солнцезащитный крем!")
    call process_character (si, appearance="pose handsup face curious", text="Ты унаследовал мою чувствительную кожу.")

    python:
        si.revistable_scenes.add("simone_scene_swimsuit_revisit")

        if not dream:
            stats.add_stat("times_seen_bikini", 1)

    call process_end_of_scene ("simone_scene_swimsuit", char=si, dream=dream, reset_prompted_scene=False )

    return

label simone_scene_4(dream=False):
    call simone_scene_4_sex (dream=dream)

    return

label simone_scene_4_sex(dream=False):
    call process_scene_beginning (bg=simone_room, char_tuple_array=[ (n, "outfit clothesjacket pose behindhead face neutral") ], dream=dream )
    call process_character (n, appearance="pose behindhead face neutral", text="Мам?")
    call process_character (n, appearance="pose behindhead face neutral", text="Ты здесь?")
    call process_character (n, appearance="pose behindhead face neutral", text="{cps=40}Я хотел поговорить с тобой о-{/cps}{w=0.75}{nw}")

    call process_character (si, appearance="outfit underwear pose armunder face embarrassed blush true", text="Ах!")
    call process_character (n, appearance="pose twohandfist face embarrassed blush true", text="!!!")
    call process_character (si, appearance="pose armunder face embarrassed blush true", text="[n.say_name]!")
    call process_character (si, appearance="pose armunder face embarrassed blush true", text="Пожалуйста, стучи, прежде чем войти в мою комнату!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="М-мам!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Я ...я не знал, что ты только ...")
    call process_character (si, appearance="pose handsup face embarrassed blush true", text="[n.say_name], пожалуйста!")
    call process_character (si, appearance="pose handsup face embarrassed blush true", text="Уйди и закрой дверь!")
    call process_character (n, appearance="pose twohandfist face embarrassed blush true", text="И-извини!")


    call fade_to_black (1)
    call bust_art_background (hallway, dream=dream)

    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="(Я всё испортил)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="(Надеюсь, мама не злится на меня)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="...{p}...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="(Я хотел рассказать ей о том, что происходит, когда я ...)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="(Мастурбирую)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="(Каждый раз, когда я мастурбирую...)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face embarrassed blush true", text="(Я не могу не думать о ее сиськах)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face embarrassed blush true", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face embarrassed blush true", text="(Я знаю, что мама хочет, чтобы я думал о чем-то другом)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face embarrassed blush true", text="(Но каждый раз, когда я пытаюсь ...)")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face flirty blush false", text="...")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Dreamland.ogg", fadeout = 1.0)

    $ quick_menu = False
    window hide
    $ clear_characters()
    show bg white
    with Dissolve(1.0)
    $ renpy.pause(1.0)
    $ renpy.show_screen("dream_blur")

    show bg kitchen_daytime
    with Dissolve(1.0)

    call process_character (si, appearance="outfit underwear pose handsfront face neutral position right blush false", text="Доброе утро, сладкий!")
    call process_character (si, appearance="outfit underwear pose handsfront face neutral", text="Хорошо ли спалось?")
    call process_character (si, appearance="outfit underwear pose handsfront face neutral", text="...")
    call process_character (si, appearance="outfit underwear pose handsup face happy", text="Тебе нравится, что я надела только мое нижнее белье?")
    call process_character (si, appearance="outfit underwear pose handsup face happy", text="Я сделала это, потому что знаю, что тебе нравятся малютки!")
    call process_character (si, appearance="outfit underwear pose handsup face happy", text="...")
    call process_character (si, appearance="outfit underwear pose handsfront face neutral", text="Я сделал для тебя блинчики с черникой!")
    call process_character (si, appearance="outfit underwear pose handsfront face neutral", text="Я знаю, что они тебе нравятся!")
    call process_character (si, appearance="outfit underwear pose armunder face neutral", text="...")
    call process_character (si, appearance="outfit underwear pose armunder face neutral", text="Ты...")
    call process_character (si, appearance="outfit underwear pose armunder face neutral", text="Ты хочешь посмотреть на мои сиськи, пока ешь свои блины?")
    call process_character (si, appearance="outfit underwear pose handsup face happy", text="Это звучит весело!")
    call process_character (si, appearance="outfit underwear pose handsup face happy", text="Я буду сидеть рядом с тобой за столом.")
    call process_character (si, appearance="outfit underwear pose armunder face neutral", text="...")
    call process_character (si, appearance="outfit underwear pose armunder face neutral", text="О, я вижу...")
    call process_character (si, appearance="outfit underwear pose armunder face neutral", text="Так ты хочешь мастурбировать после завтрака?")
    call process_character (si, appearance="outfit underwear pose armunder face neutral", text="...")
    call process_character (si, appearance="outfit underwear pose armunder face neutral", text="Ты хочешь кончить на сиськи мамы за столом?")
    call process_character (si, appearance="outfit underwear pose handsup face happy", text="Это блестящая идея!")
    call process_character (si, appearance="outfit underwear pose handsup face happy", text="Ты знаешь, мне всегда нравится, когда ты кончаешь на мою грудь!")

    $ stop_music(fadeout = 1.0)

    $ quick_menu = False
    window hide
    $ clear_characters()
    show bg white
    with Dissolve(1.0)
    $ renpy.pause(1.0)

    if not dream:
        $ renpy.scene('screens')

    if store.week.time == "night":
        show bg hallway_evening
    else:
        show bg hallway_daytime

    with Dissolve(1.0)


    call process_character (n, appearance="outfit clothesjacket_hard pose twohandfist face flirty blush true", text="(Вот это да...)")
    call process_character (n, appearance="outfit clothesjacket_hard pose twohandfist face flirty blush true", text="(Я слишком много думал о них)")
    call process_character (n, appearance="outfit clothesjacket_hard pose twohandfist face flirty blush true", text="(Надо сходить в туалет сейчас...)")

    python:
        si.revistable_scenes.add("simone_scene_4_revisit")

        if not dream:
            stats.add_stat("times_seen_bikini", 1)
            stats.add_stat("times_seen_panties", 1)
            stats.add_stat("times_seen_bra", 1)

    call process_end_of_scene ("simone_scene_4", char=si, dream=dream, force_no_boldness=True)

    return

label simone_scene_undressing(dream=False):
    call simone_scene_undressing_sex (dream=dream)

    return

label simone_scene_undressing_sex(dream=False):
    call process_scene_beginning (bg="bg hallway_evening", char_tuple_array=[ (n, "outfit underwear pose handsdown face neutral") ], dream=dream )
    call process_character (n, appearance="pose handsdown face neutral", text="(Интересно, мама все еще не спит?)")
    call process_character (n, appearance="pose handsdown face neutral", text="...")
    call process_character (n, appearance="pose handsdown face curious", text="(Похоже, ее дверь открыта, и свет включен)")
    call process_character (n, appearance="pose handsdown face curious", text="...")
    call process_character (n, appearance="pose behindhead face curious", text="(На этот раз я не буду врываться к ней, как в прошлый раз)")
    call process_character (n, appearance="pose behindhead face curious", text="(Я должен убедиться, что все в порядке)")
    call process_character (n, appearance="pose handsdown face neutral", text="(Я просто посмотрю, что мама делает...)")
    call process_character (n, appearance="pose handsdown face neutral", text="...")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Summer Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg simone_undressing")

    call process_character (n, text="!!!")
    call process_character (n, text="(М-мама снимает одежду!)")
    call process_character (n, text="(Я-я вижу её сиськи!)")
    call process_character (n, text="...")
    call process_character (n, text="(Я ...я думаю, сейчас не подходящее время поговорить с ней)")
    call process_character (n, text="(Поскольку она голая)")
    call process_character (n, text="...{p}...")
    call process_character (n, text="(М-может быть, мама скоро наденет свою ночную рубашку)")
    call process_character (n, text="(Тогда я смогу поговорить с ней)")
    call process_character (n, text="...")
    call process_character (n, text="(Да...)")
    call process_character (n, text="(Я ...я подожду еще немного...)")
    call process_character (n, text="...")

    if "kira_scene_6" in scenes_completed:
        call process_character (n, text="(Мамины сиськи даже больше, чем у [k.say_name]!)")

    call process_character (si, text="(Что за день!!)")
    call process_character (si, text="(Я, должно быть, потратила половину на заднем дворе)")
    call process_character (si, text="(А после сходила по магазина и прибралась на кухне)")
    call process_character (si, text="(Определенно, завтра утром всё будет болеть)")

    call static_still_ctc ("bg simone_undressing_mirror")

    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Когда вы, девочки, стали такими большими?)")
    call process_character (si, appearance="", text="(Трудно справиться с домом и семьёй...)")
    call process_character (si, appearance="", text="(И вы двое не облегчаете мне жизнь, когда я наклоняюсь!)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Почему она трогает свои сиськи?)")
    call process_character (si, appearance="", text="...{p}...")
    call process_character (si, appearance="", text="(Я совсем не стройная)")
    call process_character (si, appearance="", text="(И моя энергия не та, что раньше)")
    call process_character (si, appearance="", text="(Йога, по крайней мере, помогает мне оставаться немного гибкой)")
    call process_character (si, appearance="", text="(Но я и не жду, что буду выглядеть, как [k.say_name]...)")
    call process_character (si, appearance="", text="(Даже при том, что она унаследовала мою грудь, она все еще выглядит и чувствует себя атлетом)")
    call process_character (si, appearance="", text="([k.say_name] может просто носить любые бикини и выглядеть невероятно)")
    call process_character (si, appearance="", text="(Хотел бы я, чтобы эта одежда не смущала меня!)")
    call process_character (si, appearance="", text="(Несколько лет назад я могла носить короткое трико и крошечные бикини)")
    call process_character (si, appearance="", text="(От этого уже не сбежать...)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Это просто сбивает меня с толку, когда [n.say_name] таращится на мою грудь)")
    call process_character (si, appearance="", text="(Я могла понять, была ли я моложе)")
    call process_character (si, appearance="", text="(Но я никогда не думала, что они будут смотреться сейчас...)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Девочки бесценны для моего сына)")
    call process_character (si, appearance="", text="([n.say_name] не сдерживается, когда он кончает)")
    call process_character (si, appearance="", text="(Он может легко покрыть верхнюю часть моей груди)")
    call process_character (si, appearance="", text="(А это не так легко сделать...)")
    call process_character (si, appearance="", text="...{p}...")
    call process_character (si, appearance="", text="(Интересно, насколько он хорош в...)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Он получает пользу от них)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я-я могла бы обучить его...)")
    call process_character (si, appearance="", text="!")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я имею в виду...)")
    call process_character (si, appearance="", text="(Это не неправильно для матери, чтобы заботиться о том, что ее сын столкнулся...)")
    call process_character (si, appearance="", text="(Я бы не хотела, чтобы кто-нибудь научил его плохому)")
    call process_character (si, appearance="", text="...")
    call process_character (n, appearance="", text="(М-мама уже некоторое время смотрит на себя)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Интересно, почему?)")
    call process_character (si, appearance="", text="(Я слишком много думаю об этом...)")
    call process_character (si, appearance="", text="(И я не стану моложе стоя перед этим зеркалом)")
    call process_character (si, appearance="", text="(Это просто напоминает мне, что мне приходится работать всё больше над замедлением процесса старения)")
    call process_character (si, appearance="", text="{i}Зевок{/i}...")
    call process_character (si, appearance="", text="(Пора с этим завязывать, а то я буду сонная завтра...)")

    call fade_to_black (1)

    call process_character (n, text="(Мама надела ночную рубашку)")
    call process_character (n, text="...")
    call process_character (n, text="(Похоже, она ложится в постель)")
    call process_character (n, text="...")
    call process_character (n, text="(Я должен просто позволить ей поспать)")

    call process_scene_beginning (bg="bg nate_room_evening")

    call process_character (n, appearance="outfit underwear_hard pose behindhead face curious", text="(Интересно, должен ли я сказать, что я был там ...)")
    call process_character (n, appearance="pose behindhead face concerned", text="(Но я не хотел ее пугать)")
    call process_character (n, appearance="pose behindhead face concerned", text="...")
    call process_character (n, appearance="pose twohandfist face happy", text="(Я не ожидал увидеть ее сиськи!)")
    call process_character (n, appearance="pose twohandfist face happy", text="(Это было круто!)")
    call process_character (n, appearance="pose twohandfist face happy", text="(И она поднимала их и касалась их...)")
    call process_character (n, appearance="pose handsdown face neutral", text="...")
    call process_character (n, appearance="pose behindhead face curious blush true", text="(Хотел бы я сделать это с ними ...)")
    call process_character (n, appearance="pose behindhead face curious blush true", text="...")
    call process_character (n, appearance="pose handsdown face flirty blush false", text="{i}Зевок{/i}...")
    call process_character (n, appearance="pose handsdown face flirty", text="(Я лёг спать позже обычного)")
    call process_character (n, appearance="pose handsdown face flirty", text="...")
    call process_character (n, appearance="pose handsdown face flirty", text="(Но оно того стоило)")

    python:
        si.revistable_scenes.add("simone_scene_undressing_revisit")

        if not dream:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_big_breasts", 1)

    call process_end_of_scene ("simone_scene_undressing", char=si, dream=dream)

    return

label simone_scene_masturbating(dream=False):
    if week.time == "night":
        call process_scene_beginning (hallway, dream=dream )
    else:
        call process_scene_beginning (bg="bg hallway_evening", dream=dream )

    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="(Хм?)")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="(Я слышу какие-то звуки)")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="(Похоже, что они идут из спальни мамы)")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="(Интересно, стоит ли мне посмотреть)")

    call prompt_menu_boldness_check ("(Надо убедиться, что она в порядке)", "(Эх, наверное, это ничего не значит)", "simone_scene_masturbating", si)

    return

label simone_scene_masturbating_refusal(text, insufficient_points):
    $ si.prompted_scene = "simone_scene_masturbating"
    if insufficient_points:
        call process_character (n, appearance="pose behindhead face neutral", text=text)
        call process_character (n, appearance="pose handsdown face curious", text="(Я не чувствую себя достаточно {b}уверенным{/b} для этого)")

    call day_advance_time (force_bg_change=True)

    return

label simone_scene_masturbating_sex(dream=False):
    if si.prompted_scene == "simone_scene_masturbating":
        call process_character (n, appearance="pose handpocket face neutral", text="(Я хочу убедиться, что она в порядке)")

    if not dream:
        $ week.time = "night"

    if current_background != "bg hallway_evening":
        call process_scene_beginning (bg="bg hallway_evening", dream=dream )


    if si.prompted_scene == "simone_scene_masturbating":
        call process_character (n, appearance="outfit underwear pose behindhead face curious", text="(Я снова слышу эти звуки)")
        call process_character (n, appearance="outfit underwear pose behindhead face curious", text="...")
        call process_character (n, appearance="outfit underwear pose behindhead face curious", text="(Я должен проверить, что происходит...)")


    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="(Звук определенно исходит из комнаты мамы)")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="(Её дверь открыта)")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="(И свет там горит)")
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="...")

    if not dream or persistent.disable_dream_music:
        $ play_music("audio/music/Summer Groove.ogg", fadeout=1.0, fadein = 1.0)
    call static_still_ctc ("bg simone_masturbation")

    call process_character (n, appearance="", text="!!!")
    call process_character (n, appearance="", text="(Ч-что делает Мама?!)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(О-она трогает себя между ног...)")
    call process_character (n, appearance="", text="(Прямо как я, когда я...)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Мама...)")
    call process_character (n, appearance="", text="(Мастурбирует?!)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Давненько я это делал)")
    call process_character (si, appearance="", text="(Я был так занят)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Мне кажется, я более чувствителен из-за того, как долго я ждал)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Я не знаю, должен ли я смотреть на это)")
    call process_character (n, appearance="", text="(Мама может рассердиться на меня)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Я никогда не видел, чтобы Мама делала что-то вроде этого)")
    call process_character (n, appearance="", text="...")

    call static_still_ctc ("bg simone_masturbation_grabbing_crotch")

    call process_character (n, appearance="", text="(Я...)")
    call process_character (n, appearance="", text="(Я не должен шпионить за Мамой)")
    call process_character (n, appearance="", text="(Но...)")
    call process_character (n, appearance="", text="(Мне нравится то, что она делает)")
    call process_character (n, appearance="", text="(Я {w=1.0}не могу отвести глаза)")
    call process_character (n, appearance="", text="...")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я думаю, [n.say_name] смотрит на мою грудь почти все время)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Он наслаждается моей зрелой фигурой)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Член [n.say_name]...)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Выглядел таким молодым и свежим)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(И он выстрелил так много спермы)")
    call process_character (si, appearance="", text="(Э-Этим трудно не впечатлиться)")

    call static_still_ctc ("bg simone_masturbation_fapping")

    call process_character (n, appearance="", text="(Это возможность увидеть...)")
    call process_character (n, appearance="", text="(Я-я могу увидеть её вагину)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(У неё волосы вокруг)")

    if "sam_scene_2_seq_2" in scenes_completed:
        call process_character (n, text="(У [sa.say_name] нет таких волос)")

    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Ах, я снова чувствую...)")
    call process_character (si, appearance="", text="(Пенис [n.say_name]...)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Член моего сына)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Если бы я могла научить его некоторым вещам)")
    call process_character (si, appearance="", text="(Я могла бы помочь ему)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Е-его первый опыт должен быть с его матерью...)")
    call process_character (si, appearance="", text="Ах.")

    call static_still_ctc ("bg simone_masturbation_fapping_fast")

    call process_character (n, appearance="", text="(М-мам)")
    call process_character (n, appearance="", text="(Хотел бы я потрогать твои сиськи)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Интересно, может ли она потрогать мой...)")
    call process_character (n, appearance="", text="(Мой пенис)")
    call process_character (n, appearance="", text="Мм, ах.")
    call process_character (n, appearance="", text="Охх....")


    call static_still_ctc ("bg simone_masturbation_about_to_cum")

    call process_character (n, appearance="", text="(Я... я чувствую, что собираюсь...)")
    call process_character (n, appearance="", text="...")

    call static_still_ctc ("bg simone_masturbation_cum")
    call process_character (n, appearance="", text="(Он извергается!)")
    call static_still ("bg simone_masturbation_after_cum")
    call process_character (n, appearance="", text="Ахх...")

    window hide
    call static_still ("bg simone_masturbation_after_cum")
    pause 0.5
    call static_still ("bg simone_masturbation_cum_notices")

    pause 1.0
    call process_character (n, appearance="", text="(Вот дерьмо, я слишком шумный!)")
    call process_character (n, appearance="", text="(Мама услышала, это точно!)")
    call process_character (n, appearance="", text="(Я должен уйти отсюда!)")

    window hide
    call static_still ("bg simone_room_evening")
    $ no_bust_art = False

    call process_character (si, appearance="outfit nightgown pose armunder face curious blush true", text="(Это звучало как будто [n.say_name] возле моей двери!)")
    call process_character (si, appearance="outfit nightgown pose armunder face curious blush true", text="[n.say_name], это ты?")
    call process_character (si, appearance="outfit nightgown pose armunder face curious blush true", text="...")
    call process_character (si, appearance="outfit nightgown pose armunder face curious blush true", text="[n.say_name]?")
    call process_character (si, appearance="outfit nightgown pose armunder face curious blush true", text="Ты там?")
    call process_character (si, appearance="outfit nightgown pose armunder face curious blush true", text="...")
    call process_character (si, appearance="pose handsup face curious blush true", text="(Я знаю, что слышал его голос)")
    call process_character (si, appearance="pose handsup face curious blush true", text="...")

    window hide
    call static_still ("bg hallway_evening")
    $ no_bust_art = False

    call process_character (si, appearance="outfit nightgown pose armunder face embarrassed blush true", text="...")
    call process_character (si, appearance="outfit nightgown pose armunder face embarrassed blush true", text="([n.say_name] видимо, был возле моей комнаты)")
    call process_character (si, appearance="outfit nightgown pose armunder face embarrassed blush true", text="(Как долго он там стоял?)")
    call process_character (si, appearance="outfit nightgown pose armunder face embarrassed blush true", text="...")
    call process_character (si, appearance="outfit nightgown pose armunder face embarrassed blush true", text="(Он видел, что я делаю?)")
    call process_character (si, appearance="outfit nightgown pose armunder face embarrassed blush true", text="(Он...)")
    call process_character (si, appearance="outfit nightgown pose armunder face embarrassed blush true", text="(Подглядывал?)")
    call process_character (si, appearance="outfit nightgown pose armunder face embarrassed blush true", text="...{p}...")

    call static_still_ctc ("bg simone_masturbation_cum_on_floor")

    call process_character (si, appearance="", text="(Это...)")
    call process_character (si, appearance="", text="(Сперма на полу?!)")
    call process_character (si, appearance="", text="(Значит я была права, что слышала голос [n.say_name])")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Это значит, [n.say_name] был здесь достаточно долго...)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Слава богу, я ничего не сказала вслух)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Мне нужно убрать здесь всё)")
    call process_character (si, appearance="", text="...")

    call fade_to_black (1)
    call static_still ("bg simone_room_evening")
    $ no_bust_art = False

    call process_character (si, appearance="pose handsfront face concerned blush true", text="(Я слишком увлеклась...)")
    call process_character (si, appearance="pose handsfront face concerned blush true", text="(Я должна быть более осторожной и запирать дверь)")
    call process_character (si, appearance="pose handsfront face concerned blush true", text="...")
    call process_character (si, appearance="pose handsup face concerned blush true", text="Эх...")
    call process_character (si, appearance="pose handsup face concerned blush true", text="(Как я буду говорить с [n.say_name] об этом?)")
    call process_character (si, appearance="pose handsup face concerned blush true", text="(Станет ли он говорить со мной?)")
    call process_character (si, appearance="pose handsup face concerned blush true", text="...")
    call process_character (si, appearance="pose handsup face concerned blush true", text="(Это будет сложно...)")

    python:
        si.revistable_scenes.add("simone_scene_masturbating_revisit")

        if not dream:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_big_breasts", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_fapped", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_seen_vagina", 1)

    call process_end_of_scene ("simone_scene_masturbating", char=si, dream=dream)

    return

label simone_scene_garden_handjob:
    $ display_multiple_characters([ (n, ""), (si, "pose handsup face neutral") ])

    call process_character (si, appearance="pose handsup face neutral blush false", text="Ох, [n.say_name], рад, что ты пришёл!")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Я надеялась, что ты мне поможешь.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Я не успеваю в уходе за садом.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="И мне нужна дополнительная пара рук, чтобы помочь с этим.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="У тебя есть время, чтобы помочь своей маме?")
    call prompt_menu_boldness_check ("Конечно! Я могу помочь!", "Мне нужно кое-что сделать на данный момент.", "simone_scene_garden_handjob", si)

    return

label simone_scene_garden_handjob_refusal(text, insufficient_points):
    if insufficient_points:
        call process_character (n, appearance="pose behindhead face neutral", text=text)
        call process_character (n, appearance="pose behindhead face curious", text="(Я слишком нервничаю рядом с мамой.)")
        call process_character (n, appearance="pose behindhead face curious", text="(Что если мой пенис затвердеет, когда я буду рядом с ней?)")

    call process_character (si, appearance="pose armunder face neutral", text="Ну, когда ты будешь свободен, я буду благодарна за помощь.")
    call prompt_refusal_end (si)

    return

label simone_scene_garden_handjob_sex(dream=False):
    call process_scene_beginning (bg="bg garden_daytime", char_tuple_array=[ (n, "outfit clothes pose handsdown"), (si, "outfit clothes pose handsup face happy blush false") ], dream=dream )

    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Огромное спасибо за помощь в саду, [n.say_name]!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Нет проблем, Мам!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Твой сад действительно растет!")
    call process_character (si, appearance="pose armunder face happy blush false", text="Я знаю!")
    call process_character (n, appearance="pose handsdown face neutral blush false")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Я даже удивляюсь, как всё хорошо идёт.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Надеюсь, урожай будет хорошим.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Я прочитала много справочников, прежде чем посадить все.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Чем еще я могу тебе помочь?")
    call process_character (si, appearance="pose handsup face curious blush false", text="Ну давай посмотрим...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Почему бы тебе не полить эти растения?")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Они выглядят высохшими.")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Я займусь этим!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="...")
    call process_character (n, appearance="pose handsdown face neutral blush false")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="(Я рада, что [n.say_name] хорошо проводит время в саду)")
    call process_character (si, appearance="pose armunder face neutral blush false", text="(Не многие молодые люди захотели бы тратить своё время, помогая своей матери)")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="(Мама много чего посадила в этом саду!)")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="(Я никогда не понимал, сколько труда она вкладывает в это)")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose handsdown face curious blush false", text="(Думаю, я буду продолжать поливать, пока мама не скажет прекратить)")
    call process_character (n, appearance="pose handsdown face curious blush false", text="...{p}...")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="(Мне кажется, или vамина одежда немного маловата?)")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="...")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="(Я-я могу видеть контуры ее сисек...)")
    call process_character (si, appearance="pose handsup face neutral blush false", text="(Какие овощи я должна выращивать дальше?)")

    call process_character (n, appearance="outfit clothes_hard pose handsdown face curious", show_bust=False)
    $ refresh_character(n, force_transition = Dissolve(1.0))

    call process_character (si, appearance="pose armunder face neutral blush false", text="(Интересно, если [n.say_name] будет есть морковку или...)")
    call process_character (si, appearance="pose armunder face neutral blush false", text="(Или...)")
    call process_character (si, appearance="pose armunder face neutral blush false", text="...")
    call process_character (si, appearance="pose armunder face embarrassed blush false", text="!")
    call process_character (si, appearance="pose armunder face embarrassed blush false", text="(Пенис [n.say_name] встал?!)")
    call process_character (si, appearance="pose armunder face embarrassed blush false", text="(Я вижу, как он выпирает из штанов!)")
    call process_character (si, appearance="pose handsup face embarrassed blush false", text="(О-он все время смотрел на меня....)")
    call process_character (n, appearance="pose handsdown face aroused blush false", text="...{p}...")
    call process_character (si, appearance="pose handsup face embarrassed blush false", text="...")
    call process_character (si, appearance="pose handsup face embarrassed blush false", text="(Он собирается просто там стоять с эрекцией?)")
    call process_character (si, appearance="pose handsup face embarrassed blush false", text="...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="[n.say_name]?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Д-да Мама?")
    call process_character (si, appearance="pose handsfront face curious blush false", text="Твой пенис сейчас твердый?")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="...")
    call process_character (si, appearance="pose armunder face curious blush false", text="Это ведь неудобно?")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="...")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="Я думаю, все в порядке..")
    call process_character (si, appearance="pose handsup face curious blush false", text="Ты не выглядишь нормально.")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Я-я могу просто подождать, пока он не станет мягким...")
    call process_character (si, appearance="pose handsfront face curious blush false", text="Но что делать пока он твёрдый?")
    call process_character (si, appearance="pose handsfront face curious blush false", text="Твой пенис будет изгибаться в штанах...")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="Тогда...")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="Ч-что мне следует делать?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="...{p}...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Нуу...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Я бы рекомендовала выпустить его из штанов.")
    call process_character (n, appearance="pose handsdown face embarrassed blush false", text="Выпустить?")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Чтобы не чувствовать себя стесненным в одежде.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Вероятно, будет лучше, если он будет наружу...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Ты можешь расстегнуть ширинку и вытащить его.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Как только оно размякнет ты сможешь положить его назад.")
    call process_character (n, appearance="pose handsdown face curious blush false", text="Т-ты права.")
    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="Думаешь, мой пенис в порядке, после долгого пребывания в штанах?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Я не знаю.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Я могу...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Проверить его для тебя...")

    if not dream or persistent.disable_dream_music:
        $ play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)
    call static_still_ctc ("bg simone_handjob")

    call process_character (n, appearance="pose armunder face flirt blush false", text="Ах, М-мам!")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Я...)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Я чувствую это)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Я просто хочу убедиться, что все в порядке.")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Ннгх, х-хорошо...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Да кого я обманываю?)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="([n.say_name] может и поверит мне, но если кто-нибудь еще узнает, что...)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Почему я все еще верю, что это ради его здоровья?)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Любой здравомыслящий человек назвал бы меня извращенцем)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Пожилая мама хватается за член своего маленького сына)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")

    call static_still_ctc ("bg simone_handjob_fast")

    call process_character (n, appearance="pose armunder face flirt blush false", text="Ах, Мама, ах!")
    call process_character (n, appearance="pose armunder face flirt blush false", text="(Мама двигает рукой по моему члену)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Его чувствительность должна быть очень высокой)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Я должна быть осторожна, чтобы не тянуть его крайнюю плоть слишком сильно)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Его пенис гладкий)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Давненько я не трогала их)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Но я никогда не чувствовала себя так хорошо, как сейчас.)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Интересно, хорошо ли я делаю свою работу...)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Как {w=1.0}ты себя чувствуешь, милый?")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Ах...")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Х-хорошо.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Ты...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Хочешь, чтобы я продолжила?")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Д-да...")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Ах, Мама...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Мне должно быть неловко, что это мой сын.)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(А еще...)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Мне нравится держать в руке его пульсирующий член)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Я могу попытаться думать, что это не член моего сына)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Но я знаю, что это [n.say_name])")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Я знаю, что у моего сына девственный член)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Я не могу сопротивляться этому!)")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Ахх.")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Мама...")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Это действительно здорово.")
    call process_character (n, appearance="pose armunder face flirt blush false", text="...")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Ах, Мама, Я...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Должно быть, он уже близко)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Он пульсирует всё чаще и чаще)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Интересно, сколько спермы он выстрелит?)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Я возбуждаюсь от этого)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(И он наслаждался каждым моим движением руки.)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Я снова чувствую себя молодой!)")

    call static_still_ctc ("bg simone_handjob_about_to_cum")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Мама!")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Я почти...{p}Я...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Просто расслабься, милый.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Ты будешь чувствовать себя прекрасно!")

    call static_still_ctc ("bg simone_handjob_cumming")

    call process_character (n, appearance="pose armunder face flirt blush false", text="Мааам!")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Так много!)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Невероятно!)")

    call static_still_ctc ("bg simone_handjob_after_cum")

    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(И я сделала это...)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Это...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Это было приятное чувство?")
    call process_character (n, appearance="pose armunder face flirt blush false", text="М-мама...")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Это было намного лучше, чем, когда я делаю это сам.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Я-я очень рада, что стало лучше.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="А твой пенис мне показался нормальным.")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Спасибо, что помогаешь мне Мама.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Всегда пожалуйста, дорогой.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Спасибо, что помог мне сегодня в саду.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Думаю, мы оба сделали так, чтобы сад выглядел как надо.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Мы будем вознаграждены за наше садоводство!")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Мы много вещей сделали.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Не знаю, как ты, но я готова лечь и отдохнуть.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Давайте зайдем внутрь и расслабимся перед ужином.")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Звучит неплохо.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="[n.say_name]?")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Да?")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Хочешь как-нибудь повторить?")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Но ты не должен никому рассказывать.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Если ты никому не скажешь, мы можем сделать это снова.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Это звучит хорошо?")
    call process_character (n, appearance="pose armunder face flirt blush false", text="{cps=40}Так что, если я никому не скажу-{/cps}{w=0.75}{nw}")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Даже своей сестре, [sa.say_name].")
    call process_character (n, appearance="pose armunder face flirt blush false", text="М-мы можем сделать это еще?")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Да, [n.say_name].")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Хорошо, Мама.")
    call process_character (n, appearance="pose armunder face flirt blush false", text="Я буду молчать!")

    python:
        si.revistable_scenes.add("simone_scene_garden_handjob_revisit")

        if not dream:
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_received_handjob", 1)

    call process_end_of_scene ("simone_scene_garden_handjob", char=si, dream=dream)

    return

label simone_scene_garden_handjob_revisit:

    if "simone_scene_garden_handjob_revisit" in scenes_completed:
        call process_character (si, appearance="pose handsup face happy", text="Ты, как всегда, в восторге от этого!")
        call simone_scene_garden_handjob_revisit_2nd_time
    else:
        call process_character (si, appearance="pose armunder face happy", text="Полагаю, ты не имеешь в виду садоводство!")
        call process_character (si, appearance="pose handsup face neutral", text="...")
        call process_character (si, appearance="pose handsup face neutral", text="Хорошо, давай выйдем на улицу.")
        call simone_scene_garden_handjob_revisit_1st_time

    return

label simone_scene_garden_handjob_revisit_1st_time:
    $ play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg simone_handjob")
    call process_character (si, appearance="", text="Приятно видеть, что ты чаще выходишь на улицу.")
    call process_character (si, appearance="", text="Тебе нужно отдохнуть от всех этих видеоигр.")
    call process_character (n, appearance="", text="Ах, {w=1.0}мне нравится теплая погода.")
    call process_character (si, appearance="", text="Ты как, [k.say_name].")
    call process_character (si, appearance="", text="Она тоже предпочитает жару.")
    call process_character (n, appearance="", text="...")
    call static_still_ctc ("bg simone_handjob_fast")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="([n.say_name] думает только об одном)")
    call process_character (si, appearance="", text="(Похоже у него узкий кругозор)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я не думаю, что ему все равно, если бы кто-то увидел нас)")
    call process_character (si, appearance="", text="(Но, если быть справедливой...)")
    call process_character (si, appearance="", text="(Если бы я была [n.say_name], мне бы это тоже понравилось)")
    call process_character (n, appearance="", text="Ха, мм...")
    call process_character (n, appearance="", text="(М-мама крутит рукой вокруг моего пениса)")
    call process_character (n, appearance="", text="(Я-я должен попробовать это сам когда-нибудь...)")
    call process_character (n, appearance="", text="Ах, ах...")
    call process_character (n, appearance="", text="(Это не будет так же хорошо, как это, хотя...)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я не думаю, что [n.say_name] даже знает, что именно я делаю)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Он мог бы больше узнать об этом)")
    call process_character (si, appearance="", text="Знаешь ли ты, как это называется, [n.say_name]?")

    if not heard_of_handjob:
        call process_character (n, appearance="", text="Как?")
        call process_character (n, appearance="", text="Ах...")
        call process_character (si, appearance="", text="То, что я делаю, называется дрочка.")

    call process_character (n, appearance="", text="Дрочка?")

    if not heard_of_handjob and "gloryhole_handjob_scene" in scenes_completed:
        call process_character (n, appearance="", text="(Т-так вот что [gloryhole_girl.say_name] делала с моим пенисом в туалете...)")

    $ heard_of_handjob = True
    call process_character (si, appearance="", text="Да.")
    call process_character (n, appearance="", text="Почему она так называется?")
    call process_character (si, appearance="", text="Я не совсем уверена...")
    call process_character (si, appearance="", text="Просто все так говорят.")
    call process_character (n, appearance="", text="...")
    call process_character (si, appearance="", text="Это всё ново для тебя, [n.say_name].")
    call process_character (si, appearance="", text="Ты узнаешь гораздо больше.")
    call process_character (si, appearance="", text="Например, есть много слов, используемых вместо слово пенис.")
    call process_character (n, appearance="", text="Да?")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Петушок, ещё одно слово.")
    call process_character (si, appearance="", text="О боже...")
    call process_character (si, appearance="", text="Петушок, ещё одно слово.")
    call process_character (si, appearance="", text="Хер.")
    call process_character (si, appearance="", text="Ты оценишь это по достоинству...")
    call process_character (si, appearance="", text="Сосиска.")
    call process_character (n, appearance="", text="Ха, ах...")
    call process_character (n, appearance="", text="Это действительно смешно.")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я должна была понять, что он может использовать эти термины возле [sa.say_name] или [k.say_name])")
    call process_character (si, appearance="", text="(Опять же, [k.say_name] иногда позволяет себе...)")
    call process_character (si, appearance="", text="(Он ещё научится... {w=1.0}таким уникальным словцам)")

    if "kira_scene_2_seq_2" in scenes_completed:
        call process_character (n, appearance="", text="(Я думаю, что я слышал некоторые из этих слов раньше...)")

    call process_character (n, appearance="", text="...")
    call process_character (si, appearance="", text="Например, я бы сказала, что у тебя твердый петушок.")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Было потрясающе сказать это!)")

    menu:
        "А что насчет белого вещества, которое выходит?":
            call process_character (si, appearance="", text="Ах, да, есть слова, описывающие это.")
            call process_character (si, appearance="", text="Конча часто используется.")
            call process_character (si, appearance="", text="И я думаю, что я слышала термин "малафья".")
            call process_character (si, appearance="", text="Твоя мать не в курсе, как описать эякулят!")
        "Есть слова для твоих сисек?":
            call add_boldness (1, tag="simone_scene_garden_handjob_revisit_1st_time_words_for_boobs")
            call process_character (si, appearance="", text="(Я должна была знать, что он хотел знать об этом...)")
            call process_character (si, appearance="", text="Я слышала много терминов за эти годы.")
            call process_character (si, appearance="", text="(Особенно, когда у тебя есть пара, как у меня)")
            call process_character (si, appearance="", text="Для начала...")
            call process_character (si, appearance="", text="Их можно назвать сиськи, буфера, дыньки, вымя...")
            call process_character (si, appearance="", text="Половина словаря может быть заполнена разными окологрудными словами!")

    call process_character (n, appearance="", text="Ах, ах...")
    call process_character (n, appearance="", text="Ничего, если я скажу несколько таких слов?")
    call process_character (si, appearance="", text="Ты можешь говорить их рядом со мной.")
    call process_character (si, appearance="", text="Но такие слова нельзя говорить незнакомым людям или публично.")
    call process_character (si, appearance="", text="Я не хочу, чтобы у тебя были проблемы из-за вульгарности.")
    call process_character (n, appearance="", text="Ладно.")
    call process_character (n, appearance="", text="Ах...")
    call static_still_ctc ("bg simone_handjob_about_to_cum")
    call process_character (n, appearance="", text="М-Мам...")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Я-я уже {w=1.0}вот-вот.")
    call process_character (si, appearance="", text="Как только будешь готов.")
    call process_character (n, appearance="", text="{i}Вздох, Вздох{/i}")
    call process_character (n, appearance="", text="...")
    call process_character (si, appearance="", text="(Он крепко сжимает мое плечо)")
    call static_still_ctc ("bg simone_handjob_cumming")
    call process_character (n, appearance="", text="Oox!")
    call process_character (si, appearance="", text="(Он выстрелил так далеко!)")
    call static_still_ctc ("bg simone_handjob_after_cum")
    call process_character (si, appearance="", text="Хорошая работа, [n.say_name]!")
    call process_character (si, appearance="", text="Эта сперма выглядит очень здоровой!")
    call process_character (si, appearance="", text="Вот почему ты должен продолжать есть фрукты и овощи.")
    call process_character (n, appearance="", text="Спасибо, мам.")
    call process_character (si, appearance="", text="(Эти цветы продолжают получать ливни спермы)")

    python:
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_received_handjob", 1)

    call process_end_of_scene ("simone_scene_garden_handjob_revisit", char=si, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)


    return

label simone_scene_garden_handjob_revisit_2nd_time:
    $ play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)
    call static_still_ctc ("bg simone_handjob")
    call process_character (n, appearance="", text="...")
    call process_character (si, appearance="", text="(Твёрдый опять так быстро)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="Ну, я знаю, чего ты ожидаешь.")
    call static_still_ctc ("bg simone_handjob_fast")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Будет ещё чем заняться позже)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Это дает мне передышку...)")
    call process_character (si, appearance="", text="(Позволяет прийти в себя)")
    call process_character (n, appearance="", text="Ах...")

    $ n.c(random.choice(["(Интересно, что мы будем есть сегодня вечером)", "(Мне нужно увидеть, какие новые видеоигры скоро выйдут)", "(У мамы есть работа для меня по дому на сегодня?)"]))

    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Ещё один великолепный день!)")
    call process_character (n, appearance="", text="Ммм...")
    call process_character (si, appearance="", text="(Я уверена, что он хочет, чтобы делать это часами)")
    call process_character (si, appearance="", text="(Но у его члена другие планы...)")
    call static_still_ctc ("bg simone_handjob_about_to_cum")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Ах, М-Мама...")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Я ... я готов кончить.")
    call process_character (si, appearance="", text="Я буду двигать рукой быстрее, милый.")
    call process_character (si, appearance="", text="Ты придешь, когда понадобится.")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!")

    call static_still_ctc ("bg simone_handjob_cumming")
    call process_character (n, appearance="", text="Хмм! Ах!")
    call process_character (si, appearance="", text="Вот!")
    call process_character (si, appearance="", text="(Он, видимо, постоянно производит сперму)")
    call process_character (si, appearance="", text="(Его порции никогда не бывают маленькими!)")
    call static_still_ctc ("bg simone_handjob_after_cum")
    call process_character (si, appearance="", text="Эти цветы получают сюрприз от тебя.")

    python:
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_received_handjob", 1)

    call process_end_of_scene ("simone_scene_garden_handjob_revisit", char=si, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label simone_scene_bares_all(dream=False):
    call simone_scene_bares_all_sex (dream=dream)

    return

label simone_scene_bares_all_sex(dream=False):
    call process_scene_beginning (bg="bg simone_room_evening", char_tuple_array=[ (si, "outfit underwear pose handsfront face neutral") ], dream=dream )

    "{i}Тук-Тук-Тук{/i}."
    call process_character (n, appearance="", text="Мам?")
    call process_character (n, appearance="", text="Ничего, если мы войдем внутрь?")
    call process_character (si, appearance="outfit underwear pose handsfront face neutral blush false", text="Конечно, [n.say_name].")

    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="М-мама, мне очень жаль!")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="Я не знал, что ты была в нижнем белье!")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="{cps=40}Я думал, ты сказал, что можно зайти, так что я-{/cps}{w=0.75}{nw}")
    call process_character (si, appearance="pose handsup face curious blush false", text="[n.say_name], [n.say_name]...")
    call process_character (si, appearance="pose handsup face curious blush false", text="Успокойся.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Я сказала, что ты можешь войти.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Оох...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Ты не стесняешься?")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Нисколько.")
    call process_character (n, appearance="pose handsdown face curious blush false", text="Я просто помню, когда увидел тебя в нижнем белье, тебе это не понравилось.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Ну, кое-что изменилось с тех пор.")
    call process_character (si, appearance="pose armunder face happy blush false", text="На данный момент мы оба видели друг друга без одежды.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Я думаю, что да.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Вообще-то, я готовилась ко сну.")
    call process_character (n, appearance="pose handsdown face neutral blush false")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Мне просто нужно надеть ночную рубашку.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Ты ведь не будешь против, если я переоденусь?")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Я не буду возражать Маме.")

    if not dream or persistent.disable_dream_music:
        $ play_music("audio/music/Suave Standpipe.ogg", fadeout=1.0, fadein = 1.0)
    call character_leave_dissolve (si)
    $ renpy.pause(1)

    call process_character (si, appearance="outfit topless_underwear pose handsfront face neutral blush false")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="!!!")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="...")

    call character_leave_dissolve (si)
    $ renpy.pause(1)

    call process_character (si, appearance="outfit nude pose handsfront face neutral blush false")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="...{p}...")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="(М-мама стоит там без одежды!)")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="...")

    call process_character (n, appearance="outfit clothes_hard pose handsdown face concerned blush true", show_bust=False)
    $ refresh_character(n, force_transition = Dissolve(1.0))
    pause 1.0

    call process_character (n, appearance="outfit clothes_hard pose behindhead face curious blush true", text="(О-она, кажется, в порядке...)")
    call process_character (n, appearance="outfit clothes_hard pose behindhead face curious blush true", text="...")
    call process_character (n, appearance="pose handsdown face curious blush true", text="Т-ты...")
    call process_character (n, appearance="pose handsdown face curious blush true", text="Ты всегда раздеваешься перед тем, как надеть ночную рубашку?")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Это более удобно для моей груди.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Если носить их в лифчике весь день, то становится тесно через некоторое время.")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="...{p}...")
    call process_character (si, appearance="pose handsup face flirt blush true", text="(Он смотрит вверх и вниз по моему телу)")
    call process_character (n, appearance="pose behindhead face curious blush true")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="(Его глаза убегают прочь каждый раз, когда смотрит мне в глаза)")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="(Как мило...)")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush true", text="Тебе {w=1.0}нравится мое тело, [n.say_name]?")

    menu:
        "Т-ты выглядишь очень красиво.":
            call process_character (n, appearance="pose behindhead face curious blush true")
            call process_character (si, appearance="pose handsup face happy blush false", text="[n.say_name], это так мило с твоей стороны!")
            call process_character (si, appearance="pose handsup face happy blush false", text="Ты правда думаешь, что я красивая?")
            call process_character (n, appearance="pose handfist face neutral blush true", text="Да, Мама, да!")
            call process_character (n, appearance="pose handfist face neutral blush true", text="Я...")
            call process_character (n, appearance="pose behindhead face aroused blush true", text="Я думаю, ты отлично выглядишь голой.")
            call process_character (si, appearance="pose armunder face neutral blush false", text="Я польщена, милый!")
        "Мне нравится видеть тебя голой, Мама!":
            call add_boldness (1, tag="simone_scene_bares_all_loves_seeing_naked")
            call process_character (n, appearance="pose twohandfist face aroused blush true")
            call process_character (si, appearance="pose handsup face flirt blush true", text="Правда?")
            call process_character (n, appearance="pose handfist face aroused blush true", text="Да!")
            call process_character (n, appearance="pose handfist face aroused blush true", text="Мне нравится смотреть на твои сиськи и вагину!")
            call process_character (si, appearance="pose armunder face happy blush true", text="Хаха, [n.say_name]!")
            call process_character (si, appearance="pose armunder face happy blush true", text="Какой пикантный комментарий!")
            call process_character (n, appearance="pose behindhead face concerned blush true", text="П-прости мама.")
            call process_character (si, appearance="pose handsfront face neutral blush false", text="Все в порядке.")
            call process_character (si, appearance="pose handsfront face neutral blush false", text="Ты знаешь, что тебе нравится.")
            call process_character (si, appearance="pose armunder face flirt blush false", text="(И я получаю удовольствие, показывая, что тебе нравится...)")

    call process_character (si, appearance="pose handsup face neutral blush false", text="...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Может ли мама увидеть твоё тело, [n.say_name]?")
    call process_character (n, appearance="pose behindhead face curious blush true", text="М-моё тело?")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Я хочу посмотреть, как ты выглядишь.")
    call process_character (n, appearance="pose handsdown face curious blush true", text="...")
    call process_character (n, appearance="pose handfist face neutral blush true", text="Хорошо, Мам.")
    call process_character (n, appearance="pose handfist face neutral blush true", text="Я могу показать тебе...")

    call character_leave_dissolve (n)
    $ renpy.pause(1)

    call process_character (n, appearance="outfit nudehard pose handsdown face concerned blush true")

    call process_character (si, appearance="pose handsup face flirt blush true", text="Какой красивый молодой человек!")
    call process_character (si, appearance="pose handsup face flirt blush true", text="(И красивый член тоже)")
    call process_character (n, appearance="pose behindhead face neutral blush true", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush true", text="Я?")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Ты хорошо выглядишь как с одеждой, так и без!")
    call process_character (n, appearance="pose behindhead face neutral blush true", text="Д-да?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="И я говорю это не только потому, что я твоя мать.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Ты привлекательный...")

    call process_character (n, appearance="pose behindhead face neutral blush true", text="...")
    call process_character (n, appearance="pose twohandfist face aroused blush true", text="(Ах, не получается опустить пенис)")
    call process_character (n, appearance="pose twohandfist face aroused blush true", text="(Видя маму, я возбуждаюсь слишком сильно)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(Его член стал полностью твёрдый, увидев меня обнаженной)")
    call process_character (si, appearance="pose handsup face neutral blush false", text="(Я надеюсь, что он понимает, что я слишком устала, чтобы помочь сегодня)")
    call process_character (si, appearance="pose handsup face neutral blush false", text="...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="(Он, по крайней мере, наслаждается видом)")
    call process_character (si, appearance="pose handsup face neutral blush false", text="...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Я надеваю ночную рубашку, [n.say_name].")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Ты тоже можешь одеться.")

    call character_leave_dissolve (si)
    $ renpy.pause(1)

    call process_character (si, appearance="outfit nightgown pose handsfront face neutral blush false", text="...")

    call character_leave_dissolve (n)
    $ renpy.pause(1)

    call process_character (n, appearance="outfit clothes_hard pose handsdown face neutral blush false")

    call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="(Я компенсировала его эрекцию)")
    call process_character (si, appearance="pose handsup face neutral blush false", text="...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Похоже, мы оба довольны тем, как каждый из нас выглядит.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Я знаю, ты немного взволнован.")
    call process_character (n, appearance="pose behindhead face neutral blush true", text="Д-да...")
    call process_character (si, appearance="pose handsfront face curious blush false", text="Думаешь, ты будешь в порядке без моей помощи сегодня?")
    call process_character (n, appearance="pose handfist face neutral blush true", text="Со мной все будет в порядке...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Хорошо.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Я бы рекомендовала тебе мастурбировать перед сном.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Это поможет.")
    call process_character (n, appearance="pose handsdown face curious blush true", text="Хорошо, Мам.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Спокойной ночи, сладкий.")
    call process_character (n, appearance="pose handsdown face neutral blush true", text="Спокойной Ночи, Мама.")

    python:
        si.revistable_scenes.add("simone_scene_bares_all_revisit")

        if not dream:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_big_breasts", 1)
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_had_erection", 1)

    call process_end_of_scene ("simone_scene_bares_all", char=si, dream=dream)

    return

label simone_scene_bares_all_revisit:
    call process_character (n, appearance="pose behindhead face neutral blush false")
    call process_character (si, appearance="pose handsfront face happy blush false", text="Хорошо провести время, [n.say_name].")
    call process_character (si, appearance="pose handsfront face happy blush false", text="Я как раз собиралась раздеться.")

    call process_scene_beginning (bg=simone_room, char_tuple_array=[ (n, "outfit clothesjacket pose handpocket face neutral"), (si, "outfit underwear pose handsup face flirt blush false") ] )

    call process_character (si, appearance="pose handsup face flirt blush false", text="Я попрошу тебя выбрать, [n.say_name].")
    call process_character (si, appearance="pose handsup face flirt blush false", text="Хочешь, я сначала сниму лифчик или трусики?")

    menu:
        "Я хочу увидеть твои сиськи, Мама!":
            call process_character (n, appearance="pose twohandfist face neutral blush true")
            $ renpy.pause(0.5)

            call character_leave_dissolve (si)
            $ renpy.pause(1)

            call process_character (si, appearance="outfit topless_underwear pose handsfront face happy blush false", text="Вот они, только для тебя!")
            call process_character (n, appearance="outfit clothesjacket_hard pose twohandfist face flirt blush true", text="...{p}...")
            call process_character (si, appearance="pose armunder face flirt blush false", text="...")
            call process_character (si, appearance="pose armunder face neutral blush false", text="(Я надеюсь, что он немного более сдержан, глядя на грудь женщины)")
            call process_character (si, appearance="pose armunder face neutral blush false", text="(А то с таким взглядом его за километр будет видно)")
            call process_character (si, appearance="pose armunder face neutral blush false", text="...")
            call process_character (si, appearance="pose handsfront face neutral blush false", text="Теперь я сниму трусики.")
        "Я хочу увидеть твою вагину, мама!":
            call process_character (n, appearance="pose twohandfist face neutral blush true")
            $ renpy.pause(0.5)

            call character_leave_dissolve (si)
            $ renpy.pause(1)

            call process_character (si, appearance="outfit underwear_bottomless pose handsup face flirt blush false", text="Она также называется киска, пизда, или бобрятинка.")
            call process_character (n, appearance="pose behindhead face happy blush true", text="Бобрятинка?")
            call process_character (si, appearance="pose armunder face neutral blush false", text="Я знаю, это смешной термин.")
            call process_character (si, appearance="pose armunder face neutral blush false", text="Используется, когда у женщины много волос вокруг промежности.")
            call process_character (n, appearance="pose handpocket face neutral blush true", text="Как у тебя, Мам?")
            call process_character (si, appearance="pose handsup face happy blush false", text="Надеюсь, я там не слишком волосатая!")
            call process_character (n, appearance="outfit clothesjacket_hard pose twohandfist face flirt blush true", text="Мне нравится мама.")
            call process_character (si, appearance="pose armunder face flirt blush false", text="(Я думаю, ему просто нравится видеть меня голой)")
            call process_character (si, appearance="pose armunder face flirt blush false", text="...")
            call process_character (si, appearance="pose handsfront face neutral blush false", text="Позволь мне снять лифчик.")


    call character_leave_dissolve (si)
    $ renpy.pause(1)
    call process_character (si, appearance="outfit nude pose armunder face flirt blush false")
    $ renpy.pause(0.5)
    call process_character (n, appearance="pose behindhead face aroused blush true")
    $ renpy.pause(0.75)
    call process_character (si, appearance="pose armunder face flirt blush false", text="Тебе надо несколько минут, [n.say_name]?")
    call process_character (n, appearance="pose behindhead face aroused blush true", text="...{p}...")
    call process_character (n, appearance="pose handpocket face aroused blush true", text="Я бы хотел, чтобы ты все время была голой, мама.")
    call process_character (si, appearance="pose handsup face flirt blush true", text="[n.say_name]! Какой же ты непослушный!")
    call process_character (si, appearance="pose armunder face flirt blush true", text="Ты хочешь, чтобы твоя мама ходила голой все время?")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Э...это будет просто ходить так дома...")
    call process_character (si, appearance="pose handsup face happy blush true", text="Ха-ха, и это делает его более приемлемым?")
    call process_character (si, appearance="pose handsup face happy blush true", text="Какой шалун, [n.say_name]!")
    call process_character (n, appearance="pose handpocket face neutral blush true")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Ну, мне нужно кое-что сделать.")
    call process_character (si, appearance="pose handsfront face happy blush false", text="И желательно, чтобы я делала это в одежде!")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Но тебе понравилось?")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Ох да!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Мне действительно понравилось!")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Мне показалось, что это так.")
    call process_character (si, appearance="pose handsup face happy blush false", text="Твоя эрекция готова выстрелить в воздух!")
    call process_character (n, appearance="pose behindhead face curious blush true", text="...")


    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_big_breasts", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_had_erection", 1)

    call process_end_of_scene ("simone_scene_bares_all_revisit", char=si, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label simone_scene_blowjob(dream=False):
    call simone_scene_blowjob_sex (dream=dream)

    return

label simone_scene_blowjob_sex(dream=False):
    call process_scene_beginning (bg=kitchen, char_tuple_array=[ (n, "outfit clothesjacket pose handpocket face neutral"), (si, "outfit clothes pose armunder face surprised blush false") ], dream=dream )

    call process_character (si, appearance="outfit clothes pose armunder face surprised blush false", text="В доме такой беспорядок!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Ох, я не заметил.")
    call process_character (si, appearance="pose armunder face surprised blush false", text="Кухня грязная, ковер в гостиной грязный.")
    call process_character (si, appearance="pose handsup face curious blush false", text="Каждое помещение нуждается в тщательной уборке!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Мы можем прибраться в этой части дома сегодня?")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Я в состоянии сделать все это в течение нескольких дней.")
    call process_character (si, appearance="pose handsup face concerned blush false", text="Я не могу смириться с мыслью, что только часть дома была чистой.")
    call process_character (si, appearance="pose handsup face concerned blush false", text="Лучше заняться всем сразу.")
    call process_character (n, appearance="pose handpocket face neutral blush false")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="[n.say_name], ты сможешь справиться с уборкой наших комнат?")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Осталось несколько коробок, которые должны быть опустошены.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Я была бы признательна, если бы ты помог.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Похоже много работы предстоит сделать...")
    call process_character (si, appearance="pose handsfront face curious blush false", text="Это не похоже на ежедневную вещь, которую ты должен делать.")
    call process_character (si, appearance="pose handsfront face curious blush false", text="Мне станет лучше, если в доме будет чисто.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Хорошо, я могу поработать над этим.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Что мне нужно сделать в первую очередь?")
    call process_character (si, appearance="pose armunder face concerned blush false", text="Эти коробки уже стоят здесь вечность.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Сначала убери из них всё.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Затем пропылесось коридор наверху.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="И, наконец, пропылесось все наши спальни.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Я вымою душ и ванную, а затем кухню и гостиную.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Чем скорее мы приступим к работе, тем скорее все будет сделано.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="(Это займет некоторое время...)")

    call fade_to_black (1)
    call bust_art_background ("bg nate_room_evening", dream=dream)

    call process_character (n, appearance="outfit clothes pose behindhead face aroused blush false", text="{i}Фуу{/i}!")
    call process_character (n, appearance="pose behindhead face aroused blush false", text="(Я полностью уничтожен!)")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="(Было так много работы)")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="(Прошло столько времени)")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="...")
    call process_character (n, appearance="pose behindhead face aroused blush false", text="(Я думаю, что лечь отдохнуть, пока ужин готовится...)")
    call process_character (si, appearance="pose armunder face curious blush false", text="Ты выглядишь измученным, [n.say_name].")
    call process_character (n, appearance="pose handsdown face aroused blush false", text="Да, я только что закончил.")
    call process_character (si, appearance="pose handsup face happy blush false", text="Я должен сказать [n.say_name], ты проделал отличную работу!")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Да?")
    call process_character (si, appearance="pose armunder face happy blush false", text="Каждая спальня была убрана полностью, и больше никаких коробок!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Это здорово, что они пустые, наконец.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Все благодаря твоей сегодняшней тяжелой работе.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Ты собирался прилечь?")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Я, да.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Ужин еще готовится, так что у тебя будет время отдохнуть.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Хорошо.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="...{p}...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Я хотела наградить тебя, [n.say_name], за всю эту тяжелую работу.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Вознаградить меня?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Ты мне очень помогаешь в последнее время.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="И я хотела выразить свою признательность за это.")
    call process_character (n, appearance="pose handsdown face aroused blush false", text="{i}Зевок{/i}...")
    call process_character (n, appearance="pose handsdown face aroused blush false", text="Ты можешь дать мне награду после того, как я отдохну?")
    call process_character (si, appearance="pose handsup face flirt blush false", text="Фактически...")
    call process_character (si, appearance="pose handsup face flirt blush false", text="Я могу дать тебе эту награду, даже когда ты ляжешь.")
    call process_character (n, appearance="pose handsdown face curious blush false", text="Ты можешь?")
    call process_character (si, appearance="pose handsfront face flirt blush true", text="Я знаю, что тебе это понравится...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Что это?")
    call process_character (si, appearance="pose handsup face flirt blush true", text="Просто лежи на кровати и расслабься.")
    call process_character (si, appearance="pose handsup face flirt blush true", text="И я обязательно тебе покажу...")

    call fade_to_black (1)
    call process_character (n, text="...")
    call process_character (si, text="Твоя подушка удобная?")
    call process_character (n, text="Да.")
    call process_character (si, text="Хорошо.")
    call process_character (n, text="...")
    call process_character (n, text="!")
    call process_character (n, text="{cps=40}М-мама, что ты-{/cps}{w=0.75}{nw}")
    call process_character (si, text="Я немного приспускаю твои штаны.")
    call process_character (si, text="Так ты сможешь получить награду...")

    if not dream or persistent.disable_dream_music:
        $ play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)
    call static_still_ctc ("bg simone_blowjob_staring_clothed")

    call process_character (si, text="...")
    call process_character (si, text="(Уже встал)")
    call process_character (si, text="(Как будто он знал, что произойдет)")
    call process_character (si, text="...")
    call process_character (si, text="(У него такой красивый член)")
    call process_character (si, text="(Без пятен, без шершавости)")
    call process_character (n, text="Ты собираешься что-то сделать с моим пенисом, Мама?")
    call process_character (si, text="Да, детка, это так.")
    call process_character (si, text="Это называется Минет.")
    call process_character (n, text="Минет?")

    if heard_of_blowjob or "julia_scene_blowjob" in scenes_completed or "vicky_scene_blowjob" in scenes_completed or "gloryhole_scene_vaginal" in scenes_completed:
        call process_character (n, text="(Я слышал этот термин раньше...)")
    else:
        call process_character (n, text="Это что, еще одна форма мастурбации?")

    $ heard_of_blowjob = True
    call process_character (si, text="Вместо того, чтобы объяснять...")
    call process_character (si, text="Я просто хочу показать тебе.")




    call static_still_ctc ("bg simone_blowjob_foreskin_play_clothed")

    call process_character (n, text="М-Мама!")
    call process_character (n, text="...")


    if "kira_scene_tip_blowjob" in scenes_completed:
        call process_character (n, text="([k.say_name] давала мне один из них раньше...)")
    else:
        call process_character (n, text="(М-мама кладет свой язык на мой пенис!)")

    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Головка его теплая)")
    call process_character (si, appearance="", text="(Я могу просунуть мой язык под крайнюю плоть)")
    call process_character (n, appearance="", text="A-Ах, aхх...")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="Так начинается минет, [n.say_name].")
    call process_character (si, appearance="", text="Во-первых, я облизываю кончик твоего пениса, так как он наиболее чувствителен.")
    call process_character (si, appearance="", text="Ты должен почувствовать много удовольствия от этого.")
    call process_character (n, appearance="", text="Это чувство гораздо лучше, чем просто дрочка.")
    call process_character (si, appearance="", text="Это другое чувство, не так ли?")
    call process_character (n, appearance="", text="Намного, ах!")
    call process_character (si, appearance="", text="(Приятно знать, что я доставляю своему сыну удовольствие)")
    call process_character (si, appearance="", text="(Что-то, что может дать только мать...)")

    call static_still_ctc ("bg simone_blowjob_clothed")

    call process_character (n, appearance="", text="Ах, ах, Ммм!")
    call process_character (n, appearance="", text="(М-мама сосет его!)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я-я держу член [n.say_name] во рту)")
    call process_character (si, appearance="", text="(Его головка касается моего языка)")
    call process_character (si, appearance="", text="(Я чувствую, как сердце бьется через его член)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="([n.say_name], тяжело дышит)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я знаю еще несколько трюков...)")
    call process_character (n, appearance="", text="Мннх.")
    call process_character (n, appearance="", text="(Мама сосет так хорошо!)")
    call process_character (n, appearance="", text="{i}Вздох{/i}")
    call process_character (n, appearance="", text="(О-она двигает языком вокруг моего пениса)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="Это приемлемая награда?")
    call process_character (n, appearance="", text="Д-да.")
    call process_character (n, appearance="", text="Э-это потрясающе, Мам...")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Это вкус его предсемени?)")
    call process_character (si, appearance="", text="(Он бьёт меня, как волна)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я не ожидала, что он будет иметь такой великолепный вкус...)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="Награда не закончится, пока ты не кончишь, [n.say_name].")
    call process_character (n, appearance="", text="Ах, да...")
    call process_character (n, appearance="", text="Думаю, что я близко к тому времени.")
    call process_character (n, appearance="", text="Но куда мне все-таки кончать?")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="Ты...")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="Хочешь кончить на лицо мамочки?")
    call process_character (n, appearance="", text="Э... это нормально, Мама?")
    call process_character (si, appearance="", text="Если ты кончишь на моё лицо, это признак привязанности.")
    call process_character (si, appearance="", text="Это показывает, как сильно ты меня любишь.")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Я действительно люблю тебя, мама.")
    call process_character (n, appearance="", text="Можешь пососать еще немного?")
    call process_character (n, appearance="", text="Ах, ах...")
    call process_character (n, appearance="", text="Ещё чуть-чуть, Мама...")
    call process_character (n, appearance="", text="Д-да!")
    call process_character (n, appearance="", text="Ммм, ннгх!")

    call static_still_ctc ("bg simone_blowjob_cumming_clothed_skin_up")

    call process_character (si, appearance="", text="(Да!)")
    call process_character (si, appearance="", text="(Вот оно!)")



    call static_still_ctc ("bg simone_blowjob_facial_clothed_skin_up")

    call process_character (si, appearance="", text="(Она на мне...)")
    call process_character (si, appearance="", text="(Сперма моего сына стекает по моему лицу)")
    call process_character (si, appearance="", text="(Она теплая...)")
    call process_character (n, appearance="", text="М-Мам...")
    call process_character (n, appearance="", text="У тебя столько всего на лице.")
    call process_character (si, appearance="", text="Определённо!")
    call process_character (si, appearance="", text="И ты попал немного на себя, и на кровать.")
    call process_character (n, appearance="", text="Я не могу контролировать, куда она летит.")
    call process_character (si, appearance="", text="Ничего страшного, дорогой.")
    call process_character (si, appearance="", text="Я сниму простыню, чтобы ты не прилип во время отдыха.")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Мне очень нравятся минеты, мама.")
    call process_character (si, appearance="", text="Я же говорила, что это будет хитом!")
    call process_character (n, appearance="", text="Это единственный раз, когда я его получу?")
    call process_character (si, appearance="", text="Хочешь как-нибудь повторить?")
    call process_character (n, appearance="", text="Я хотел бы получить его, когда смогу!")
    call process_character (si, appearance="", text="Понятно...")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="Я могу сделать это для тебя, но ты можешь помочь мне, когда мне это нужно по дому?")
    call process_character (n, appearance="", text="Конечно, мама, могу!")
    call process_character (si, appearance="", text="Замечательно, [n.say_name]!")
    call process_character (si, appearance="", text="Ты такой замечательный сын.")
    call process_character (si, appearance="", text="И просто, чтобы ты знал...")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="Иногда я буду делать тебе минет, просто для удовольствия.")
    call process_character (n, appearance="", text="Ох, круто!")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="{i}Нюх-Нюх {/i}")
    call process_character (n, appearance="", text="Что это за запах?")
    call process_character (si, appearance="", text="Ох, макароны!")
    call process_character (si, appearance="", text="Должно быть почти готово.")
    call process_character (si, appearance="", text="Давай я возьму твою простыню и положу ее в стирку.")
    call process_character (si, appearance="", text="Я позову тебя, когда ужин будет на столе.")
    call process_character (n, appearance="", text="{i}Зевок{/i}")
    call process_character (n, appearance="", text="Хорошо, Мам.")

    python:
        si.revistable_scenes.add("simone_scene_blowjob_revisit")

        if not dream:
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_foreskin_played_with", 1)
            stats.add_stat("times_given_facial", 1)
            stats.add_stat("times_received_blowjob", 1)

    call process_end_of_scene ("simone_scene_blowjob", char=si, dream=dream)

    return

label simone_scene_blowjob_revisit(start_naked=False):
    call process_character (n, appearance="pose behindhead face neutral blush false")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Конечно, милый.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="(Не могу отказаться от члена моего сына, нуждающегося в помощи)")

    if si.outfit == "nude":
        $ start_naked = True

    if not start_naked:
        call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Позволь мне закончить кое-что.")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="Я очень скоро буду...")
        call static_still_ctc ("bg simone_blowjob_staring_clothed_smiling")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="Извините, что заставила тебя ждать.")
        call process_character (n, appearance="pose handsfront face flirt blush false", text="Это было не долго, мама, не волнуйся.")
    else:
        call fade_to_black_fade_to_static_ctc ("bg simone_blowjob_staring_nude_smiling", 1)


    if "simone_scene_blowjob_revisit" not in scenes_completed and not start_naked:
        call process_character (si, appearance="pose handsfront face flirt blush false", text="...")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="Я просто подумала, [n.say_name]...")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="Как бы ты себя чувствовал, если бы мы разделись для этого?")
        call process_character (n, appearance="pose handsfront face flirt blush false", text="Да! Мы должны это сделать!")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="Подумай об этом дважды!")

        call fade_to_black_fade_to_static_ctc ("bg simone_blowjob_staring_nude_smiling", 1)

        call process_character (n, appearance="pose handsfront face flirt blush false", text="Ах!")
        call process_character (n, appearance="pose handsfront face flirt blush false", text="(Я чувствую, как мамины сиськи трогают мою кожу)")
        call process_character (n, appearance="pose handsfront face flirt blush false", text="(Они очень мягкие)")
        call process_character (n, appearance="pose handsfront face flirt blush false", text="(И ее сиськи вокруг моего члена)")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="(Наша одежда на полу, я на [n.say_name]...)")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="(Мы всего в одном шаге от этого...)")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="...")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="(Только вперёд...)")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="...")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="(Я уверена, что он мечтал об этом)")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="(Моя грудь лежит на нем)")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="(И его член под ними)")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="...")
    else:
        if not start_naked:
            call fade_to_black_fade_to_static_ctc ("bg simone_blowjob_staring_nude_smiling", 1)


    call static_still_ctc ("bg simone_blowjob_foreskin_play_nude")

    call process_character (si, appearance="pose handsfront face flirt blush false", text="{i}Ммф {/i}")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="(Он часто извивается, когда я это делаю)")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="(Движение моего языка должно оживить его)")
    call process_character (n, appearance="pose handsfront face flirt blush false", text="(Это очень чувствительная область, которую мама лижет!)")
    call process_character (n, appearance="pose handsfront face flirt blush false", text="(Она всегда начинает с неё!)")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="(Я уже эксперт по ублажению [n.say_name])")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="(Я могла бы просто лизать его кончик и заставить кончить его)")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="...")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="(Но зачем останавливаться на достигнутом?)")

    call static_still_ctc ("bg simone_blowjob_nude")

    call process_character (n, appearance="pose handsfront face flirt blush false", text="О, боже...")
    call process_character (n, appearance="pose handsfront face flirt blush false", text="(Как хорошо...)")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="(Я сосу так сильно, чтобы сжимаю его член)")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="(Что может сократить наше время...)")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="(Но даже если будет быстро, это сладко для него)")
    call process_character (n, appearance="pose handsfront face flirt blush false", text="...")
    call process_character (n, appearance="pose handsfront face flirt blush false", text="(Пытаюсь держаться)")
    call process_character (n, appearance="pose handsfront face flirt blush false", text="(Мне нравится это чувство, и я хочу продолжать!)")
    call process_character (n, appearance="pose handsfront face flirt blush false", text="(Мама сосет меня правильно...)")
    call process_character (n, appearance="pose handsfront face flirt blush false", text="Ах, ах.")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!")
    $ quick_menu = True

    call process_character (si, appearance="pose handsfront face flirt blush false", text="(Он толкает бедрами)")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="(Это означает только одно...)")
    call process_character (n, appearance="pose handsfront face flirt blush false", text="(Это, это...)")
    call process_character (n, appearance="pose handsfront face flirt blush false", text="(Это бесполезно, я не могу остановить его!)")

    call static_still_ctc ("bg simone_blowjob_cumming_nude_skin_up")

    call process_character (n, appearance="pose handsfront face flirt blush false", text="Аах! Хрнг...")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="(Вот оно!)")

    call static_still_ctc ("bg simone_blowjob_facial_nude_skin_up")

    call process_character (si, appearance="pose handsfront face flirt blush false", text="Ты пытался продержаться еще немного?")
    call process_character (n, appearance="pose handsfront face flirt blush false", text="Д-да...")
    call process_character (n, appearance="pose handsfront face flirt blush false", text="У меня ничего не получилось.")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="Мне нравится, что ты хочешь продлить удовольствие!")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="Трудно остановить оргазм, когда он на подходе.")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="Ты научишься держаться дольше, не беспокойся, милый!")

    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_big_breasts", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_foreskin_played_with", 1)
        stats.add_stat("times_given_facial", 1)
        stats.add_stat("times_received_blowjob", 1)

    call process_end_of_scene ("simone_scene_blowjob_revisit", char=si, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label simone_scene_vaginal(dream=False):
    $ no_bust_art = False
    $ display_multiple_characters([ (n, "pose handpocket face neutral"), (si, "pose handsfront face happy blush false") ])

    call process_character (si, appearance="pose handsfront face happy blush false", text="Привет [n.say_name]!")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Что привело тебя в мою спальню?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Ничего особенного.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Я просто хотел пожелать тебе спокойной ночи.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Это очень мило с твоей стороны!")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Ты скоро ложишься спать?")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Не ложись слишком поздно!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Я не буду мама.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="...{p}...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="[n.say_name]...")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Да, Мам?")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="Ты...")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="Хочешь провести ночь со мной?")

    call prompt_menu_boldness_check ("Да, мне бы этого очень хотелось!", "Я не знаю, смогу ли я сегодня...", "simone_scene_vaginal", si)

    return

label simone_scene_vaginal_refusal(text, insufficient_points):
    call process_character (n, appearance="pose behindhead face neutral blush false", text=text)
    if insufficient_points:
        call process_character (n, appearance="pose behindhead face curious", text="...")
        call process_character (n, appearance="pose behindhead face curious", text="(Мама хочет, чтобы я провел с ней ночь?!)")
        call process_character (n, appearance="pose behindhead face curious", text="(Бьюсь об заклад, она хочет что-то сделать со мной!)")
        call process_character (n, appearance="pose behindhead face curious", text="(Я должен быть более готов к этому!)")

    call process_character (si, appearance="pose armunder face neutral", text="Это прекрасно, дорогой.")
    call process_character (si, appearance="pose armunder face neutral", text="Дай мне знать, когда ты будешь свободен ночью...")

    call prompt_refusal_end (si)
    return

label simone_scene_vaginal_sex(dream=False):
    $ renpy.start_predict("simone_vaginal_anim")

    call process_scene_beginning (bg="bg simone_room_evening", char_tuple_array=[ (n, "outfit underwear pose handsdown face neutral"), (si, "outfit nightgown pose handsfront face neutral") ], dream=dream, force_bg_change=True )

    call process_character (si, appearance="pose handsfront face neutral blush false", text="Прошло много времени с тех пор, как ты спал со мной.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Хм?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Что ты имеешь в виду?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Разве ты не помнишь?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Когда тебе приснится страшный сон...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Ты забежал в мою комнату, желая спать со мной.")
    call process_character (si, appearance="pose handsup face happy blush false", text="Это было очень мило!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Ох, да...")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Теперь я это припоминаю.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Ты был единственным, кто приходил ко мне, когда боялся.")
    call process_character (n, appearance="pose handsdown face neutral blush false")
    call process_character (si, appearance="pose armunder face neutral blush false")
    call process_character (si, appearance="pose handsfront face happy blush false", text="Твоя сестра [k.say_name] всегда спала, как бревно!")
    call process_character (si, appearance="pose armunder face neutral blush false", text="И [sa.say_name] так много играет в видеоигры...")
    call process_character (si, appearance="pose armunder face happy blush false", text="Я не думаю, что сны для нее настолько волнительны!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты говоришь, что мое воображение действительно сильное или что?")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="У тебя живое воображение, да.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="И это хорошо, [n.say_name]!")
    call process_character (si, appearance="pose handsup face happy blush false", text="Вот почему ты такой творческий и умный!")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Спасибо, Мам.")
    call process_character (si, appearance="pose handsup face neutral blush false")
    call process_character (n, appearance="pose handsdown face neutral blush false")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Ты помогаешь мне многому научиться!")
    call process_character (si, appearance="pose armunder face happy blush false", text="Это не только моя заслуга!")
    call process_character (si, appearance="pose armunder face neutral blush false", text="У тебя очень хорошая память!")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="...")
    call process_character (si, appearance="pose handsup face flirt blush false", text="...{p}...")
    call process_character (si, appearance="pose handsup face flirt blush false", text="Тебе нравится, чем я занимаюсь в последнее время?")
    call process_character (si, appearance="pose handsup face flirt blush false", text="В кровати и в саду?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты имеешь в виду, когда ты сосешь мой член и все такое?")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Да, это просто замечательно!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Я с нетерпением жду этого каждый раз!")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="Ну, [n.say_name]...")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="У Мамы есть большая просьба.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Да ну?")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Какая?")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Я доставлял тебе много удовольствия, и я рада, что тебе это нравится.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="И сейчас...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Я хочу, чтобы ты доставил мне удовольствие.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Доставить тебе удовольствие, мама?")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="Ты тоже будешь чувствовать себя хорошо, [n.say_name].")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="Мы будем наслаждаться этим вместе.")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Так ты и я получим удовольствие?")
    call process_character (si, appearance="pose handsup face flirt blush false", text="Да.")
    call process_character (si, appearance="pose handsup face flirt blush false", text="...")
    call process_character (si, appearance="pose handsup face flirt blush false", text="Хочешь сделать это, милый?")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Да!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Конечно, да!")
    call process_character (si, appearance="pose armunder face happy blush false", text="Ты всегда в восторге от таких вещей!")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Что мы будем делать?")
    call process_character (n, appearance="pose handfist face happy blush false", text="Как мы оба можем чувствовать себя хорошо?")

    call character_leave_dissolve (si)
    pause 0.5

    call process_character (si, appearance="outfit nude pose handsfront face neutral blush false", text="Я помогу тебе пройти через это.")
    call process_character (si, appearance="outfit nude pose handsfront face neutral blush false", text="...")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="Ты засунешь свой член мне в киску.")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="Я-я!")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="Правда, Мама?!")
    call process_character (si, appearance="pose handsup face neutral blush false", text="{i}Шшш{/i}, милый.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Не так громко.")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face concerned blush false", text="Извини.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Но да, ты это сделаешь.")
    call process_character (si, appearance="pose handsup face flirt blush false", text="Тебе было интересно, каково это.")
    call process_character (si, appearance="pose handsup face flirt blush false", text="Мне самой тоже любопытно.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="(Я хотел сделать это с тех пор, как увидел маму в то время на ее кровати)")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="(Я никогда не думал, что мама позволит мне сделать это с ней!)")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="(Я в таком восторге!)")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="([n.say_name] не может сдержать своего волнения по этому поводу)")
    call process_character (si, appearance="pose handsfront face happy blush false", text="(Я видела, как его член растет, когда я сказала ему, что мы сделаем!)")
    call process_character (si, appearance="pose handsfront face happy blush false", text="...")
    call process_character (si, appearance="pose armunder face happy blush false", text="(Это восхитительно, как он не может контролировать себя)")
    call process_character (si, appearance="pose handsup face neutral blush false", text="(Если он видит мою грудь, он получает стояк)")
    call process_character (si, appearance="pose handsup face neutral blush false", text="(Если он видит мою задницу, он получает стояк)")
    call process_character (si, appearance="pose handsup face happy blush false", text="(У него постоянно будет эрекция такими темпами!)")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты хочешь, чтобы я снял нижнее белье?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Мы же не можем сделать это в твоей одежде?")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (n, appearance="outfit nudehard pose behindhead face neutral blush false")

    call process_character (si, appearance="pose handsfront face neutral blush false", text="Теперь встань передо мной...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Я откинусь здесь, у подножия кровати.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="И я просто хочу, чтобы ты подошел ко мне.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Я буду держаться за твой пенис, когда ты подойдешь ближе...")

    call fade_to_black (1)

    call process_character (si, appearance="pose armunder face flirt blush false", text="Теперь двигай бедрами.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Толкай туда-сюда в мою киску...")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Suave Standpipe.ogg", fadein = 1.0)

    $ simone_vaginal_had_slow_speed_message = False
    $ simone_vaginal_had_normal_speed_message = False
    $ simone_vaginal_had_fast_speed_message = False

    $ renpy.scene('characters')
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    $ set_main_animation_speed(1.0)
    show anim_nothing_image as main_animation at main_animation_transform(IA_Animation_Simone_Vaginal_Info())
    with Dissolve(1.15)
    show bg white
    $ renpy.pause(1.50)
    $ quick_menu = True

    call process_character (si, appearance="", text="О...")
    call process_character (si, appearance="", text="Oox!")
    call process_character (si, appearance="", text="Да!")
    call process_character (si, appearance="", text="Вот так, [n.say_name]!")
    call process_character (si, appearance="", text="Да!")
    call process_character (n, appearance="", text="Ты такая теплая мама!")
    call process_character (si, appearance="", text="Аах!")
    call process_character (si, appearance="", text="Продолжай, [n.say_name]...")
    call process_character (si, appearance="", text="Продолжай трахать меня!")
    call process_character (si, appearance="", text="Ой, бля!")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Я никогда не слышал, чтобы мама так говорила...)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Я правильно делаю, мама?")
    call process_character (si, appearance="", text="Ты делаете больше, чем правильно, [n.say_name]...")
    call process_character (si, appearance="", text="Ты идеален!")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Это было так давно, когда хер был во мне!)")
    call process_character (si, appearance="", text="([n.say_name] удовлетворяет меня лучше, чем я надеялась!)")
    call process_character (n, appearance="", text="Ах, {w=0.5}ах, {w=0.5}ах!")
    call process_character (n, appearance="", text="(Это самое лучшее!)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Интересно, если я попробую двигаться немного...)")
    call process_character (si, appearance="", text="О...")
    call process_character (si, appearance="", text="{cps=40}Ахх, о мой-{/cps}{w=0.75}{nw}")
    call process_character (si, appearance="", text="Твой член прямо здесь!")
    call process_character (n, appearance="", text="Где мама?")
    call process_character (si, appearance="", text="Это моё чувствительное место!")
    call process_character (si, appearance="", text="О, боже!")
    call process_character (si, appearance="", text="Засунь свой член внутрь меня!")
    call process_character (si, appearance="", text="Я хочу чувствовать больше!")
    call process_character (n, appearance="", text="Мне следует двигаться быстрее?")
    call process_character (si, appearance="", text="Будь так быстр, как ты можешь, милый!")

    $ set_main_animation_speed(simone_vaginal_fast_speed_multiplier)

    call process_character (si, appearance="", text="Ох, да детка!")
    call process_character (si, appearance="", text="(У него столько страсти!)")
    call process_character (si, appearance="", text="(И у него есть какая-то сила в его толчках!)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Тело мамы чувствуется податливым и мягким)")
    call process_character (n, appearance="", text="Ахх!")
    call process_character (n, appearance="", text="(И ее сиськи покачиваются)")
    call process_character (si, appearance="", text="[n.say_name]!")
    call process_character (si, appearance="", text="Ты невероятен в этом!")
    call process_character (n, appearance="", text="Я... Я?")
    call process_character (si, appearance="", text="Я не чувствовала себя так хорошо много лет, милый!")
    call process_character (si, appearance="", text="Ты угождаешь мамочке!")
    call process_character (si, appearance="", text="Мм!")
    call process_character (n, appearance="", text="Ты делаешь то же самое для меня, Мама!")
    call process_character (n, appearance="", text="Ах, ах!")
    call process_character (n, appearance="", text="Ты была права, что мне это понравится!")
    call process_character (si, appearance="", text="{i}Вздох{/i}...")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="Почему бы тебе не выбрать, как быстро мы будем двигаться дальше, [n.say_name]?")
    call process_character (n, appearance="", text="Ты хочешь, чтобы я выбрал, Мама?")
    call process_character (si, appearance="", text="Ты выглядишь более чем способным, милый.")
    call process_character (si, appearance="", text="Я верю, что ты справишься.")
    call process_character (si, appearance="", text="Двигайся так, как ты хочешь!")

    menu:
        "Низкая скорость":
            $ set_main_animation_speed(simone_vaginal_slow_speed_multiplier)
            call process_character (si, text="Ты должно быть устал после всех этих колебаний.")
            call process_character (si, text="Это требует много выносливости!")
            call process_character (si, text="Давай немного успокоимся.")
        "Нормальная скорость":
            $ set_main_animation_speed(1.0)
            call process_character (si, text="У тебя прирожденный талант, милый!")
            call process_character (si, text="Ах...")
            call process_character (si, text="Ты справляешься с этим, как опытный!")
        "Быстрая скорость":
            $ set_main_animation_speed(simone_vaginal_fast_speed_multiplier)
            call process_character (si, text="Ты хочешь продолжать быстро?")
            call process_character (si, text="Уверена, тебе нравится это чувство.")
            call process_character (si, text="Но не напрягайся!")

    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Что я должен делать, когда…")
    call process_character (si, appearance="", text="О...")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="Ну...")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Должна ли я позволить ему кончить в меня?)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я на самом деле не думала об этом до сих пор)")
    call process_character (si, appearance="", text="...")
    call process_character (n, appearance="", text="М-мама, ах...")
    call process_character (n, appearance="", text="Я уже почти, мама.")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Я-я должен продолжать?")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="Да милый.")
    call process_character (si, appearance="", text="Просто продолжай.")

    $ set_main_animation_speed(simone_vaginal_fast_speed_multiplier)

    call process_character (n, appearance="", text="Ах, ах!")
    call process_character (n, appearance="", text="(Я думаю, я выстрелю в мамину киску)")
    call process_character (si, appearance="", text="Ох, ох! Ах!")
    call process_character (si, appearance="", text="Да! Да!")
    call process_character (si, appearance="", text="Наполни меня, милый!")
    call process_character (si, appearance="", text="Ох, бля!")
    call process_character (n, appearance="", text="Ммм!")
    call process_character (n, appearance="", text="Ах, Мама!")
    call process_character (n, appearance="", text="Мааама!")

    $ quick_menu = False
    window hide
    hide main_animation
    with Dissolve(1.5)
    $ play_sex_sounds = False

    pause 0.5

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    $ quick_menu = False
    window hide
    show bg simone_vaginal_cum
    with Dissolve(1.5)
    $ quick_menu = True

    "[si.say_name] and [n.say_name]" "Aaах!!"
    call process_character (si, appearance="", text="...")
    call process_character (n, appearance="", text="...")
    call process_character (si, appearance="", text="{i}Вздох{/i}, {i}вздох{/i}...")
    call process_character (n, appearance="", text="{i}Уфф...{/i}")
    call process_character (n, appearance="", text="...")
    call process_character (si, appearance="", text="Ох, милый!")
    call process_character (si, appearance="", text="Какой ты наделал беспорядок!")
    call process_character (n, appearance="", text="...")
    call process_character (si, appearance="", text="Но, не беспокойся!")
    call process_character (si, appearance="", text="Все можно отстирать.")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Я весь вспотел, Мама.")
    call process_character (si, appearance="", text="Я тоже, малыш.")
    call process_character (si, appearance="", text="Мы выпустили много энергии!")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Можно я положу голову на тебя, Мама?")
    call process_character (n, appearance="", text="Я устал...")
    call process_character (si, appearance="", text="Я знаю.")
    call process_character (si, appearance="", text="Давай, отдохни.")
    call process_character (si, appearance="", text="{cps=40}Но после, ты должен помыться-{/cps}{w=0.75}{nw}")
    call process_character (n, appearance="", text="Хрр...")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Сразу же уснул!)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(И не в самом идеальном положении...)")
    call process_character (si, appearance="", text="(Его член все еще во мне!)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Надеюсь, я не переусердствовал им)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Но он мирно отдыхает)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я сомневаюсь, что он собирается вернуться в свою спальню сегодня вечером...)")

    $ renpy.stop_predict("simone_vaginal_anim")

    if not dream:
        $ week.time = "night"

    python:
        si.revistable_scenes.add("simone_scene_vaginal_revisit")

        if not dream:
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_vaginal_sex", 1)
            stats.add_stat("times_given_vaginal_creampie", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("simone_scene_vaginal", char=si, dream=dream)

    return

label simone_vaginal_set_speed(speed):
    hide screen simone_vaginal_speed_settings
    $ set_main_animation_speed(speed)

    return


label simone_vaginal_go_slow(is_revisit):
    call simone_vaginal_set_speed (simone_vaginal_slow_speed_multiplier)

    if not simone_vaginal_had_slow_speed_message:
        if is_revisit:
            call process_character (si, text="Ах, это очень хорошо, [n.say_name]!")
            call process_character (si, text="Как будто время замедляется.")
            call process_character (si, text="Это, ох...")
            call process_character (si, text="Это расслабляет.")
            call process_character (si, text="Ты так не думаешь?")
        else:
            pass

    window hide
    with None
    $ simone_vaginal_had_slow_speed_message = True

    if is_revisit:
        $ renpy.call("simone_scene_vaginal_revisit_segment_2")
    else:
        $ renpy.call("simone_scene_vaginal_segment_2")

    return

label simone_vaginal_go_normal(is_revisit):
    call simone_vaginal_set_speed (1.0)

    if not simone_vaginal_had_normal_speed_message:
        if is_revisit:
            call process_character (si, text="Мм, oox!")
            call process_character (si, text="Мне нравится, когда ты его включаешь!")
        else:
            pass

    window hide
    with None
    $ simone_vaginal_had_normal_speed_message = True

    if is_revisit:
        $ renpy.call("simone_scene_vaginal_revisit_segment_2")
    else:
        $ renpy.call("simone_scene_vaginal_segment_2")

    return

label simone_vaginal_go_fast(is_revisit):
    call simone_vaginal_set_speed (simone_vaginal_fast_speed_multiplier)

    if not simone_vaginal_had_fast_speed_message:
        if is_revisit:
            call process_character (si, text="Ах, ах, мм!")
            call process_character (si, text="Сначала я думала, что не смогу справиться с тобой так быстро...")
            call process_character (si, text="Но это заставляет меня чувствовать себя энергичной!")
        else:
            pass

    window hide
    with None
    $ simone_vaginal_had_fast_speed_message = True

    if is_revisit:
        $ renpy.call("simone_scene_vaginal_revisit_segment_2")
    else:
        $ renpy.call("simone_scene_vaginal_segment_2")

    return

label simone_scene_vaginal_revisit:
    $ renpy.start_predict("simone_vaginal_anim")
    $ no_bust_art = False

    if "simone_scene_vaginal_revisit" in scenes_completed:
        call simone_scene_vaginal_revisit_2nd_time
    else:
        call simone_scene_vaginal_revisit_1st_time

    return

label simone_scene_vaginal_revisit_1st_time:
    $ no_bust_art = False
    call process_character (si, appearance="pose armunder face happy blush false", text="Это не очень скрыто, [n.say_name]!")
    call process_character (si, appearance="pose armunder face happy blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Если ты готов к этому, то я готова для тебя...")

    if store.stats.current_location != simone_room:
        call process_character (si, appearance="pose handsup face neutral blush false", text="Приходи ко мне в комнату сегодня вечером.")


    python hide:
        play_music("audio/music/Suave Standpipe.ogg", fadein = 1.0)

    $ simone_vaginal_had_slow_speed_message = False
    $ simone_vaginal_had_normal_speed_message = False
    $ simone_vaginal_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    $ set_main_animation_speed(1.0)
    show anim_nothing_image as main_animation at main_animation_transform(IA_Animation_Simone_Vaginal_Info())
    with Dissolve(1.15)
    show bg white
    $ renpy.pause(1.50)
    $ quick_menu = True

    call process_character (si, appearance="", text="Вот и все!")
    call process_character (si, appearance="", text="Это идеальное движение, милый!")
    call process_character (si, appearance="", text="(Он делает лучше, чем раньше!)")
    call process_character (n, appearance="", text="Мм!")
    call process_character (n, appearance="", text="Я копирую, как мы делали это в прошлый раз!")
    call process_character (si, appearance="", text="(Он такой умный)")
    call process_character (si, appearance="", text="(Он даже помнит, где мое чувствительное место!)")
    call process_character (si, appearance="", text="Oox!")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(За короткий промежуток времени, [n.say_name] стал опытным в этом)")
    call process_character (si, appearance="", text="(Я не должна ожидать ничего меньшего от моего сына)")
    call process_character (n, appearance="", text="Ах, ах...")
    call process_character (n, appearance="", text="(Это лучший способ показать маме, как сильно я ее люблю!)")
    call process_character (n, appearance="", text="(Она чувствует себя хорошо, и все это из-за моего тела!)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Мама, ты потрясающая!)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="([n.say_name], смотрит на меня так...)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я знаю, когда он трахает меня, он делает это с большим количеством эмоций)")
    call process_character (si, appearance="", text="(Он хочет показать мне, как сильно он любит свою маму...)")
    call process_character (si, appearance="", text="(И это то, что делает наш секс особенным!)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Маме нравится, когда я ускоряюсь и замедляюсь)")
    call process_character (n, appearance="", text="(Интересно, как она хотела бы в следующий раз?)")

    window hide
    $ quick_menu = False
    show screen simone_vaginal_speed_settings(True)
    $ renpy.pause(3.0)
    $ renpy.suspend_rollback(True)

    call simone_scene_vaginal_revisit_segment_2

    return

label simone_scene_vaginal_revisit_2nd_time:
    call process_character (si, appearance="pose handsup face happy blush false", text="Я только что постирала простыни!")
    call process_character (si, appearance="pose handsup face happy blush false", text="...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Это нормально.")
    call process_character (si, appearance="pose armunder face neutral blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Кончил прямо на них...")

    python hide:
        play_music("audio/music/Suave Standpipe.ogg", fadein = 1.0)

    $ simone_vaginal_had_slow_speed_message = False
    $ simone_vaginal_had_normal_speed_message = False
    $ simone_vaginal_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    $ set_main_animation_speed(1.0)
    show anim_nothing_image as main_animation at main_animation_transform(IA_Animation_Simone_Vaginal_Info())
    with Dissolve(1.15)
    show bg white
    $ renpy.pause(1.50)
    $ quick_menu = True

    call process_character (si, appearance="", text="([n.say_name] по-прежнему возвращается снова и снова)")
    call process_character (si, appearance="", text="...{p}...")
    call process_character (si, appearance="", text="(Обычно сын будет смущен признать, что его мама привлекательна)")
    call process_character (si, appearance="", text="(Но не мой, [n.say_name]!)")
    call process_character (si, appearance="", text="(Он объявил бы об этом всему миру, если бы мог!)")
    call process_character (si, appearance="", text="...{p}...")
    call process_character (si, appearance="", text="(Уровень энергии [n.say_name] должно быть передаётся мне)")
    call process_character (si, appearance="", text="(Я гораздо более активна в течение дня, чем раньше)")
    call process_character (si, appearance="", text="(Не правы те, кто говорит, что дети изнашивают вас!)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Несмотря на то, что мама больше меня...)")
    call process_character (n, appearance="", text="(Я могу заставить ее двигаться, когда в неё втыкаю)")
    call process_character (n, appearance="", text="...{p}...")
    call process_character (n, appearance="", text="(Интересно, делают ли другие мамы такие вещи?)")
    call process_character (n, appearance="", text="(Я не думаю, что они делают)")
    call process_character (n, appearance="", text="(Я никогда не слышал об этом)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Это должно означать, что мы делаем что-то уникальное вместе!)")
    call process_character (n, appearance="", text="(Я знал, что моя мама не будет такой же, как другие мамы!)")
    call process_character (n, appearance="", text="(Вот почему она самая лучшая!)")

    window hide
    $ quick_menu = False
    show screen simone_vaginal_speed_settings(True)
    $ renpy.pause(3.0)
    $ renpy.suspend_rollback(True)

    call simone_scene_vaginal_revisit_segment_2

    return

label simone_scene_vaginal_revisit_segment_2:
    show screen simone_vaginal_speed_settings(True)
    call screen progress_button_screen("Кончить!")
    $ quick_menu = True
    hide screen simone_vaginal_speed_settings
    $ renpy.suspend_rollback(False)

    if "simone_scene_vaginal_revisit" in scenes_completed:
        call simone_scene_vaginal_revisit_segment_2_2nd_time
    else:
        call simone_scene_vaginal_revisit_segment_2_1st_time

    return

label simone_scene_vaginal_revisit_segment_2_1st_time:
    call process_character (n, appearance="", text="Я приближаюсь к концу, мама!")
    call process_character (n, appearance="", text="Ахх!")
    call process_character (si, appearance="", text="Я почувствовала, что ты почти готов!")
    call process_character (si, appearance="", text="Продолжай толкать, детка!")

    $ quick_menu = False
    window hide
    hide main_animation
    with Dissolve(1.5)
    $ play_sex_sounds = False

    pause 0.5

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    $ quick_menu = False
    window hide
    show bg simone_vaginal_cum
    with Dissolve(1.5)
    $ quick_menu = True

    call process_character (n, appearance="", text="Ннг!")
    call process_character (n, appearance="", text="Это выходит наружу, мама!")
    call process_character (si, appearance="", text="Это точно, милый!")
    call process_character (si, appearance="", text="(Его сперма течет в меня!)")
    call process_character (n, appearance="", text="Ооох, ахх...")
    call process_character (n, appearance="", text="...")
    call process_character (si, appearance="", text="Чувствуешь облегчение?")
    call process_character (n, appearance="", text="{i}Вздох{/i}...")
    call process_character (n, appearance="", text="Д-да...")
    call process_character (si, appearance="", text="Тебе нужно прилечь ненадолго?")
    call process_character (n, appearance="", text="Возможно.")
    call process_character (si, appearance="", text="Ты можешь отдохнуть на моей кровати.")
    call process_character (si, appearance="", text="Я думаю, что это более удобно, чем потерять сознание на мне!")

    call simone_scene_vaginal_revisit_end

    return

label simone_scene_vaginal_revisit_segment_2_2nd_time:
    $ quick_menu = False
    window hide
    hide main_animation
    with Dissolve(1.5)
    $ play_sex_sounds = False

    pause 0.5

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    $ quick_menu = False
    window hide
    show bg simone_vaginal_cum
    with Dissolve(1.5)
    $ quick_menu = True

    call process_character (n, appearance="", text="Ааах, Мам!")
    call process_character (si, appearance="", text="Это была большая порция, [n.say_name]!")
    call process_character (si, appearance="", text="Молодец!")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Его яйца должны работать сверхурочно, чтобы создать столько спермы!)")

    call simone_scene_vaginal_revisit_end

    return


label simone_scene_vaginal_revisit_end:
    $ renpy.stop_predict("simone_vaginal_anim")

    python:
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_vaginal_sex", 1)
        stats.add_stat("times_given_vaginal_creampie", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("simone_scene_vaginal_revisit", char=si, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label simone_scene_anal:
    $ no_bust_art = False
    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral"), (si, "outfit nightgown pose handsfront face neutral") ])

    call process_character (si, appearance="outfit nightgown pose handsfront face neutral blush false", text="[n.say_name], у меня есть вопрос.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Какой, Мама?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Что-то заинтриговало меня.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Хм?")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Я просто хотела узнать...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Если бы ты мог трахнуть меня так, как хочешь, как бы ты это сделал?")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="!")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="Я-я...")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="Не надо смущаться.")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="Я действительно хочу знать.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")

    call prompt_menu_boldness_check ("Ну, у меня есть кое-что на уме....", "М-мне нужно подумать об этом...", "simone_scene_anal", si)

    return

label simone_scene_anal_refusal(text, insufficient_points):
    if insufficient_points:
        call process_character (n, appearance="pose behindhead face neutral", text=text)
        call process_character (n, appearance="pose behindhead face curious blush false", text="(Я даже не думал, что мама спросит меня об этом!)")
        call process_character (n, appearance="pose behindhead face curious blush false", text="(Мне нужно убедиться, что я трахаю ее так, как ей понравится...)")

    call process_character (si, appearance="pose armunder face neutral", text="Нет необходимости принимать решение сейчас.")
    call process_character (si, appearance="pose armunder face neutral", text="Не торопись, дорогой.")
    call prompt_refusal_end (si)

    return

label simone_scene_anal_sex(dream=False):
    call process_scene_beginning (bg=simone_room, char_tuple_array=[ (n, "outfit clothesjacket pose behindhead face neutral"), (si, "outfit nightgown pose armunder face flirt") ])

    call process_character (si, appearance="pose armunder face flirt blush false", text="Так ты знаешь, как бы ты хотел меня трахнуть?")
    call process_character (n, appearance="pose handfist face neutral blush false", text="У меня... у меня есть идея...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Но я хочу убедиться, что тебе понравится.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Я думаю, все, что ты придумаешь, будет здорово, милый!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Х-Хорошо...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="...")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Ты будешь лежать на полу...")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="И я бы трахнул тебя сзади!")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Ох...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Это называется по-собачьи.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="По-собачьи?")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Это очень похоже на то, что ты описываешь.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Я буду стоять на четвереньках.")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Потом ты подходишь ко мне, и мы начинаем трахаться.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Это похоже на то, что тебе нравится мама?")
    call process_character (si, appearance="pose handsup face happy blush false", text="Я думаю, что это отличный выбор, [n.say_name]!")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Это весело и эротично!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Круто!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Здорово, что ты много знаешь об этом, Мама!")
    call process_character (si, appearance="pose armunder face happy blush false", text="Ха-ха, нуу...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Может в это трудно поверить...")
    call process_character (n, appearance="pose handpocket face neutral blush false")
    call process_character (si, appearance="pose armunder face neutral blush false")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Но когда я была моложе, я была довольно {w=1.0}безрассудна.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Безрассудна?")
    call process_character (si, appearance="pose handsfront face happy blush false", text="Скажем так, есть причина, по которой у тебя есть аппетит к сексу!")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Ты преследуешь меня во многих смыслах.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="...")
    call process_character (si, appearance="pose handsup face happy blush false", text="И это включает, сильное желание секса!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Оох, я понял, Мама!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="В этом есть смысл!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Я бы никогда не догадался, что ты такая!")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Я притормозила через некоторое время.")
    call process_character (si, appearance="pose armunder face happy blush false", text="Но я трахалась постоянно!")
    call process_character (si, appearance="pose armunder face neutral blush false", text="В какой-то момент я знала почти все возможные позы!")
    call process_character (n, appearance="pose behindhead face happy blush false", text="Круто!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Значит, ты много чего сделала...")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="По-собачьи?")
    call process_character (si, appearance="pose handsup face happy blush false", text="Хаха, о, да!")
    call process_character (si, appearance="pose handsup face happy blush false", text="Это классика, точно!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Потрясающе!")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Можешь сделать мне одолжение, милый?")
    call process_character (n, appearance="pose handpocket face neutral blush false")
    call process_character (si, appearance="pose handsfront face neutral blush false")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Можешь взять подушку с кровати?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Чтобы я могла положить его под колени, пока мы на полу.")
    call process_character (si, appearance="pose armunder face happy blush false", text="У меня будет всё болеть, если я лягу на жёсткую поверхность!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="...{p}...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Хорошо, я принесу подушку!")
    call process_character (si, appearance="pose handsfront face happy blush false", text="Спасибо!")

    $ clear_characters()
    with Dissolve(0.5)
    pause 1.0
    $ display_multiple_characters([ (n, "outfit nudehard pose handfist face neutral"), (si, "outfit nude pose handsfront face flirt") ])

    call process_character (si, appearance="outfit nude pose handsfront face flirt blush false", text="Позволь мне встать на четвереньки.")
    call process_character (si, appearance="outfit nude pose handsup face flirt blush false", text="И тогда ты знаешь, что делать, милый...")

    call fade_to_black (1)

    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="О!")
    call process_character (si, appearance="", text="Я чувствую, как ты трёшься об меня!")
    call process_character (n, appearance="", text="Д-да...")
    call process_character (si, appearance="", text="...{p}...")
    call process_character (si, appearance="", text="{cps=40}Двигайся прямо вперед и вставь его в мою-{/cps}{w=0.75}{nw}")
    call process_character (si, appearance="", text="Аах!")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

    call static_still_ctc ("bg simone_doggy")

    call process_character (n, appearance="", text="Ах! Ах!")
    call process_character (n, appearance="", text="Мама, да!")
    call process_character (si, appearance="", text="Ох, дорогой!")
    call process_character (si, appearance="", text="{cps=40}Т-ты вставил свой член прямо в-{/cps}{w=0.75}{nw}")
    call process_character (si, appearance="", text="Ах!")
    call process_character (si, appearance="", text="Ты засунул его мне в задницу!")
    call process_character (n, appearance="", text="Мм, ах! Ах!")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Уже слишком поздно)")
    call process_character (si, appearance="", text="([n.say_name] ухватился за меня)")
    call process_character (si, appearance="", text="(Он будет продолжать накачивать меня, пока не закончит)")
    call process_character (si, appearance="", text="Ах, ах...")

    call static_still_ctc ("bg simone_doggy_blur")

    call process_character (n, appearance="", text="Ахх!")
    call process_character (n, appearance="", text="(Даже если это не мамина киска...)")
    call process_character (n, appearance="", text="(Она по-прежнему чувствует себя очень хорошо!)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Я не обратил внимания на то, куда идет мой член...)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Надеюсь, мама не возражает)")
    call process_character (n, appearance="", text="Ах, ах!")
    call process_character (n, appearance="", text="(Я наслаждаюсь этим слишком сильно, чтобы остановиться!)")

    call static_still_ctc ("bg simone_behind_nocum")

    if "kira_simone_threesome_scene" in scenes_completed:
        call process_character (si, appearance="", text="Ммм, ах...")
        call process_character (si, appearance="", text="(У меня такое чувство, что это не первый раз, когда [n.say_name] трахает девушку в жопу)")
        call process_character (si, appearance="", text="(С тех пор, как [k.say_name] ходит только в нижнем белье...)")
        call process_character (si, appearance="", text="(Меня бы не удивило, если бы она соблазнила [n.say_name]...)")
    else:
        call process_character (si, appearance="", text="Ах, да...")
        call process_character (si, appearance="", text="(Моя киска мокрая)")
        call process_character (si, appearance="", text="Ммм!")
        call process_character (si, appearance="", text="(Моя задница более чувствительна, чем я помню!)")

    call process_character (n, appearance="", text="Мама, ах...")
    call process_character (n, appearance="", text="Я правильно делаю по-собачьи?")
    call process_character (si, appearance="", text="Ах, да...")
    call process_character (si, appearance="", text="Это немного отличается от обычного...")
    call process_character (si, appearance="", text="Ах! Ах!")
    call process_character (si, appearance="", text="Но если ты чувствуешь себя так же хорошо, как и я...")
    call process_character (si, appearance="pose new face message blush false", text="Тебе не нужно ничего менять!")
    call process_character (n, appearance="pose new face message blush false", text="Ладно...")
    call process_character (n, appearance="pose new face message blush false", text="Ах...")
    call process_character (si, appearance="pose new face message blush false", text="...")
    call process_character (si, appearance="pose new face message blush false", text="Возьми столько времени, ах, {w=0.5} сколько тебе нужно.")
    call process_character (si, appearance="pose new face message blush false", text="...")
    call process_character (si, appearance="pose new face message blush false", text="Можешь двигаться быстрее, если хочешь.")

    call static_still_ctc ("bg simone_behind_ballflop_blur")

    call process_character (n, appearance="pose new face message blush false", text="Ах, ахх, ах, ах!")
    call process_character (n, appearance="pose new face message blush false", text="Мааам!")
    call process_character (si, appearance="pose new face message blush false", text="О, да!")
    call process_character (si, appearance="pose new face message blush false", text="Ах да!")
    call process_character (si, appearance="pose new face message blush false", text="(Он ведет себя немного грубо...)")
    call process_character (si, appearance="pose new face message blush false", text="...")
    call process_character (si, appearance="pose new face message blush false", text="([n.say_name] не знает, что я раньше любила погрубее)")
    call process_character (si, appearance="pose new face message blush false", text="Oox!")
    call process_character (si, appearance="pose new face message blush false", text="...")
    call process_character (si, appearance="pose new face message blush false", text="(Это меня возбуждает!)")
    call process_character (n, appearance="pose new face message blush false", text="...")
    call process_character (n, appearance="pose new face message blush false", text="(Мама издает больше шума, чем быстрее я двигаюсь)")
    call process_character (n, appearance="pose new face message blush false", text="...")
    call process_character (n, appearance="pose new face message blush false", text="(Но если я буду продолжать так быстро...)")
    call process_character (n, appearance="pose new face message blush false", text="О!")
    call process_character (n, appearance="pose new face message blush false", text="Хнг! Аах!")
    call process_character (n, appearance="pose new face message blush false", text="(Я собираюсь кончить!)")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg simone_behind_cum")

    call process_character (si, appearance="pose new face message blush false", text="Aaах!")
    call process_character (si, appearance="pose new face message blush false", text="Да детка!")
    call process_character (si, appearance="pose new face message blush false", text="Наполни мою задницу!")
    call process_character (n, appearance="pose new face message blush false", text="Ух! Ух!")
    call process_character (n, appearance="pose new face message blush false", text="...")
    call process_character (n, appearance="pose new face message blush false", text="Ах...")
    call process_character (si, appearance="pose new face message blush false", text="...")
    call process_character (si, appearance="pose new face message blush false", text="{i}Уфф...{/i}")
    call process_character (si, appearance="pose new face message blush false", text="...")
    call process_character (si, appearance="pose new face message blush false", text="Ты заставил мамочку кончить.")
    call process_character (n, appearance="pose new face message blush false", text="{i}Вздох{/i}, {i}вздох{/i}...")
    call process_character (si, appearance="pose new face message blush false", text="Ох, будь осторожен, дорогой...")
    call process_character (si, appearance="pose new face message blush false", text="Ты становишься мертвым грузом после оргазма!")
    call process_character (si, appearance="pose new face message blush false", text="Постарайся не так сильно опираться на спину.")
    call process_character (n, appearance="pose new face message blush false", text="П-Прости Мама.")
    call process_character (n, appearance="pose new face message blush false", text="Сейчас встану ради тебя.")
    call process_character (n, appearance="pose new face message blush false", text="...")

    call static_still_ctc ("bg simone_behind_cumaftermath")

    call process_character (si, appearance="pose new face message blush false", text="{i}Фьюю{/i}...")
    call process_character (si, appearance="pose new face message blush false", text="...")
    call process_character (si, appearance="pose new face message blush false", text="Из моей задницы течет сперма?")
    call process_character (n, appearance="pose new face message blush false", text="Д-да...")
    call process_character (n, appearance="pose new face message blush false", text="Очень много.")
    call process_character (si, appearance="pose new face message blush false", text="Я так и думала...")
    call process_character (si, appearance="pose new face message blush false", text="...")
    call process_character (si, appearance="pose new face message blush false", text="Я вся в отключке от тебя, милый!")
    call process_character (n, appearance="pose new face message blush false", text="...")
    call process_character (si, appearance="pose new face message blush false", text="Ох...")
    call process_character (si, appearance="pose new face message blush false", text="Уфф...")
    call process_character (si, appearance="pose new face message blush false", text="...")
    call process_character (si, appearance="pose new face message blush false", text="Уоу...")
    call process_character (n, appearance="pose new face message blush false", text="Что случилось, мама?")
    call process_character (si, appearance="pose new face message blush false", text="Похоже, мне понадобится твоя помощь!")
    call process_character (si, appearance="pose new face message blush false", text="Я немного перенапряглась после всего этого...")
    call process_character (si, appearance="pose new face message blush false", text="...")
    call process_character (si, appearance="pose new face message blush false", text="Спасибо подушке, а то было бы хуже!")

    python:
        si.revistable_scenes.add("simone_scene_anal_revisit")

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

    call process_end_of_scene ("simone_scene_anal", char=si, dream=dream)

    return

label simone_scene_anal_revisit:
    if "simone_scene_anal_revisit" in scenes_completed:
        call simone_scene_anal_revisit_2nd_time
    else:
        call simone_scene_anal_revisit_1st_time

    return

label simone_scene_anal_revisit_1st_time:
    $ no_bust_art = False
    $ display_multiple_characters([ (n, "pose twohandfist face neutral"), (si, "pose handsup face happy") ])

    call process_character (si, appearance="pose handsup face happy blush false", text="Тебе это очень понравилось, не так ли?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Мне тоже это понравилось...")

    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

    call static_still_ctc ("bg simone_doggy")

    call process_character (si, appearance="", text="Давай изо всех сил, милый!")
    call process_character (n, appearance="", text="Д-да?")
    call process_character (si, appearance="", text="Я полностью готова к этому!")
    call process_character (si, appearance="", text="...")

    call static_still_ctc ("bg simone_doggy_blur")

    call process_character (n, appearance="", text="Ах, ах!")
    call process_character (n, appearance="", text="О да!")
    call process_character (si, appearance="", text="Ммм!")
    call process_character (si, appearance="", text="Вот так, малыш!")
    call process_character (n, appearance="", text="Ахх, ах!")
    call process_character (n, appearance="", text="(Мама позволяет мне делать все движения)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Я думаю, ей это нравится!)")

    call static_still_ctc ("bg simone_behind_nocum")

    call process_character (si, appearance="", text="Ох, ох!")
    call process_character (si, appearance="", text="Да, да!")
    call process_character (si, appearance="", text="(Мой сын стал настоящим мужчиной в доме!)")
    call process_character (si, appearance="", text="(Он единственный, кто мне нужен, чтобы удовлетворить меня!)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Другие матери хотели бы, чтобы их сыновья могли быть такими идеальными!)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Я никогда не понимал, насколько большой была задница мамы...)")
    call process_character (n, appearance="", text="(Он в два раза шире моего тела!)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Ее задница сотрясается, когда мое тело касается его)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Мне нравится, как она это делает...)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", yalign = 0.95)
    $ quick_menu = True


    call static_still_ctc ("bg simone_behind_ballflop_blur")

    call process_character (si, appearance="", text="Ох, ох!")
    call process_character (si, appearance="", text="[n.say_name]!")
    call process_character (si, appearance="", text="Да, [n.say_name]!")
    call process_character (si, appearance="", text="(Он врезается в меня!)")
    call process_character (si, appearance="", text="(Он получает второе, третье и четвертое дыхание!)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Это все, что юношеская энергия!)")
    call process_character (n, appearance="", text="Мааам!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg simone_behind_cum")

    call process_character (n, appearance="", text="Аaax!")
    call process_character (n, appearance="", text="Ах, ах...")
    call process_character (si, appearance="", text="Давай, малыш!")
    call process_character (n, appearance="", text="...{p}...")
    call process_character (si, appearance="", text="Не останавливайся, милый!")
    call process_character (si, appearance="", text="Продолжай трахать меня!")
    call process_character (n, appearance="", text="Н-но я уже кончил...")
    call process_character (si, appearance="", text="Все нормально!")
    call process_character (si, appearance="", text="Если всё еще стоит, просто продолжай!")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="Мне кажется, мой член становится мягче.")
    call process_character (si, appearance="", text="Да, малыш?")
    call process_character (si, appearance="", text="Ну, ты ничего не можешь с этим поделать.")

    call static_still_ctc ("bg simone_behind_cumaftermath")

    call process_character (si, appearance="", text="Трудно оставаться в вертикальном положении после такого оргазма.")
    call process_character (si, appearance="", text="Твой пенис говорит тебе, что он устал.")
    call process_character (n, appearance="", text="Д-да...")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="Тебе было хорошо во время нашего траха?")
    call process_character (n, appearance="", text="О да, мам!")
    call process_character (n, appearance="", text="Мне нравится, что ты разрешаешь мне двигаться так быстро, как я хочу!")
    call process_character (si, appearance="", text="Ну, ты мой особенный мальчик!")
    call process_character (si, appearance="", text="Ты можешь трахать мамочку сколько хочешь!")

    call simone_scene_anal_revisit_end
    return

label simone_scene_anal_revisit_2nd_time:
    $ no_bust_art = False
    $ display_multiple_characters([ (n, "pose twohandfist face happy"), (si, "pose armunder face happy") ])

    call process_character (si, appearance="pose armunder face happy blush false", text="Это одна из твоих любимых поз?")
    call process_character (si, appearance="pose armunder face happy blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Я не виню тебя...")

    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

    call static_still_ctc ("bg simone_doggy_blur")

    call process_character (si, appearance="", text="Хах, ах!")
    call process_character (si, appearance="", text="(Сексуальное влечение [n.say_name] начинает превосходить моё...)")
    call process_character (si, appearance="", text="...")

    if "kira_simone_threesome_scene" in scenes_completed:
        call process_character (si, appearance="", text="(Я понимаю, почему у него нет проблем с [k.say_name] и мной)")
        call process_character (si, appearance="", text="...")
        call process_character (si, appearance="", text="(Мы удовлетворяем его желания...)")
        call process_character (si, appearance="", text="(И теперь он пробудил свою похоть!)")
    else:
        call process_character (si, appearance="", text="(Одно можно сказать наверняка...)")
        call process_character (si, appearance="", text="(Я быстро сжигаю калории таким образом!)")
        call process_character (si, appearance="", text="...")
        call process_character (si, appearance="", text="(Если я собираюсь идти в ногу с [n.say_name]...)")
        call process_character (si, appearance="", text="(Мне придется делать еще несколько кардио-тренировок с [k.say_name]!)")

    call process_character (n, appearance="", text="Ах, Ахх!")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Мама сказала, что знает много поз...)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Интересно, сколько их существует?)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Минет считается сексуальной позицией?)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Маме придется рассказать о них подробнее)")
    call process_character (n, appearance="", text="(Я хочу сделать их все!)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", yalign = 0.95)
    $ quick_menu = True


    call static_still_ctc ("bg simone_behind_ballflop_blur")

    call process_character (si, appearance="", text="{i}Вздох{/i}, {i}Вздох{/i}, {i}Вздох{/i}...")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Он уже несколько раз накачал в меня...)")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg simone_behind_cum")

    call process_character (n, appearance="", text="Ннгх!")
    call process_character (n, appearance="", text="Ах...")
    call process_character (si, appearance="", text="(Он залил много спермы в мою задницу!)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я буду ходить немного странно после этого траха...)")

    call simone_scene_anal_revisit_end
    return

label simone_scene_anal_revisit_end:
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

    call process_end_of_scene ("simone_scene_anal_revisit", char=si, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label simone_scene_titfuck:
    call simone_scene_titfuck_sex
    return

label simone_scene_titfuck_sex(dream=False):
    call process_scene_beginning (bg=simone_room, char_tuple_array=[ (n, "outfit clothesjacket"), (si, "outfit yoga") ], dream=dream)



    call process_character (si, appearance="outfit yoga pose handsfront face neutral blush false")

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Привет, Мам.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Ты только что занималась йогой?")
    call process_character (si, appearance="outfit yoga pose handsfront face neutral blush false", text="Да.")
    call process_character (si, appearance="outfit yoga pose handsup face happy blush false", text="На этот раз я почти смогла коснуться ног!")
    call process_character (si, appearance="outfit yoga pose handsup face happy blush false", text="Я чувствовала гордость за себя!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Хорошая Мама!")
    call process_character (si, appearance="outfit yoga pose armunder face neutral blush false", text="Хотя не думаю, что когда-нибудь смогу дотянуться до пальцев ног.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Почему так?")
    call process_character (si, appearance="outfit yoga pose armunder face neutral blush false", text="Моя грудь не позволяет мне наклониться так далеко.")
    call process_character (si, appearance="outfit yoga pose armunder face neutral blush false", text="Они как блокада!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="О...")
    call process_character (si, appearance="outfit yoga pose handsfront face neutral blush false", text="Я никогда не думала, что они станут такими большими.")
    call process_character (si, appearance="outfit yoga pose handsfront face neutral blush false", text="Иногда мне хочется, чтобы они были меньше...")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face concerned blush false", text="Н-нет!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face concerned blush false", text="Не надо меньше, Мама!")
    call process_character (si, appearance="outfit yoga pose armunder face curious blush false", text="Мм?")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face concerned blush false", text="Твоя великолепная грудь должна быть огромной!")
    call process_character (si, appearance="outfit yoga pose armunder face happy blush false", text="Хаха, [n.say_name]!")
    call process_character (si, appearance="outfit yoga pose armunder face happy blush false", text="У тебя есть твердое мнение об этом!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...")
    call process_character (si, appearance="outfit yoga pose handsup face neutral blush false", text="Мне всегда было интересно, почему ты так любишь мою грудь.")
    call process_character (si, appearance="outfit yoga pose handsup face neutral blush false", text="Держу пари, это потому, что я тебя постоянно кормила грудью..")
    call process_character (si, appearance="outfit yoga pose handsup face happy blush false", text="Это создало теплые воспоминания о них!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (si, appearance="outfit yoga pose armunder face neutral blush false", text="Не возражаешь, если я переоденусь, [n.say_name]?")
    call process_character (si, appearance="outfit yoga pose armunder face neutral blush false", text="Этот костюм йоги должен быть брошен в прачечную.")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Иди, Мама!")

    call character_leave_dissolve (si)
    pause 0.5
    call process_character (si, appearance="outfit nude")
    pause 0.5

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="...")
    call process_character (si, appearance="outfit naked pose handsfront face neutral blush false", text="Удивительно, как ты можешь обуздать всех нас.")
    call process_character (si, appearance="outfit naked pose handsfront face happy blush false", text="Не так давно тебе было стыдно видеть меня в нижнем белье!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="О, да...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Я это помню.")
    call process_character (si, appearance="outfit naked pose handsfront face neutral blush false", text="Ты проделал долгий путь!")

    if "sam_simone_threesome_scene" in scenes_completed and "kira_simone_threesome_scene" in scenes_completed:
        call process_character (si, appearance="pose armunder face neutral blush false", text="До начала лета ты почти ничего не знал о сексе.")
        call process_character (si, appearance="pose armunder face flirt blush false", text="Теперь ты трахаешь обеих сестер и меня!")
        call process_character (si, appearance="pose armunder face flirt blush false", text="Как ты планируешь свой день, если каждая из нас хочет быть с тобой?")
        call process_character (n, appearance="pose handpocket face neutral blush false", text="...")
        call process_character (n, appearance="pose handpocket face neutral blush false", text="Думаю, я просто решаю по ходу дела.")
        call process_character (si, appearance="pose handsup face neutral blush false", text="Убедись, что ты даёшь пенису отдохнуть хоть какое-то время.")
        call process_character (si, appearance="pose handsup face neutral blush false", text="Ты не должен перенапрягаться.")
        call process_character (n, appearance="pose handfist face neutral blush false", text="До сих пор у меня не было никаких проблем.")
        call process_character (si, appearance="pose handsup face happy blush false", text="Приятно слышать, дорогой.")
        call process_character (si, appearance="pose handsup face happy blush false", text="Ты невероятен, как ты можешь противостоять целой семье из девушек!")
    elif "kira_simone_threesome_scene" in scenes_completed:
        call process_character (si, appearance="pose armunder face neutral blush false", text="До начала лета ты почти ничего не знал о сексе.")
        call process_character (si, appearance="pose armunder face flirt blush false", text="Теперь ты трахаешь и меня, и свою сестру [k.say_name]!")
        call process_character (si, appearance="pose armunder face flirt blush false", text="Мне легко узнать, когда ты с [k.say_name].")
        call process_character (n, appearance="pose handpocket face curious blush false", text="Правда?")
        call process_character (n, appearance="pose handpocket face curious blush false", text="Как ты это узнаешь?")
        call process_character (si, appearance="pose handsfront face neutral blush false", text="Если я не нахожу тебя в твоей комнате, и громкий стук будет исходить из комнаты твоей сестры...")
        call process_character (si, appearance="pose handsfront face happy blush false", text="Вот откуда мне это известно!")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Это довольно громко?")
        call process_character (si, appearance="pose armunder face neutral blush false", text="Прежде чем я поняла, что происходит, я думала [k.say_name] просто делал тяжелую тренировку, и ты помогал ей.")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Ну...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Мы с этого и начали.")
        call process_character (si, appearance="pose armunder face flirt blush false", text="Ох...")
        call process_character (si, appearance="pose armunder face flirt blush false", text="Так вот как ты с сестрой впервые начали...")
        call process_character (n, appearance="pose handpocket face curious blush false", text="...")
        call process_character (si, appearance="pose handsup face happy blush false", text="Я надеюсь [k.say_name] не бросает тебя, как тряпичную куклу!")
    elif "sam_simone_threesome_scene" in scenes_completed:
        call process_character (si, appearance="pose armunder face neutral blush false", text="До начала лета ты почти ничего не знал о сексе.")
        call process_character (si, appearance="pose armunder face flirt blush false", text="Теперь ты трахаете меня, и [sa.say_name]!")
        call process_character (si, appearance="pose armunder face flirt blush false", text="Я до сих пор не могу поверить, что [sa.say_name] это нравится...")
        call process_character (n, appearance="pose handfist face neutral blush false", text="Ей это очень нравится.")
        call process_character (n, appearance="pose handfist face neutral blush false", text="Она ищет в интернете видео для новых идей.")
        call process_character (si, appearance="pose handsup face happy blush false", text="Это определенно твоя сестра!")
        call process_character (si, appearance="pose handsup face neutral blush false", text="Ее мозг всегда о чем-то думает.")
        call process_character (si, appearance="pose handsup face neutral blush false", text="Я никогда не думала, что секс будет одной из ее лучших дел!")
    else:
        call process_character (si, appearance="pose armunder face neutral blush false", text="До начала лета ты почти ничего не знал о сексе.")
        call process_character (si, appearance="pose armunder face flirt blush false", text="Теперь ты знаешь больше, чем большинство!")
        call process_character (n, appearance="pose handfist face neutral blush false", text="Ты помогла мне узнать много всего, Мама!")
        call process_character (si, appearance="pose handsup face happy blush false", text="Я уверена, что да!")
        call process_character (si, appearance="pose handsup face happy blush false", text="Гораздо больше, чем я думала!")
        call process_character (si, appearance="pose handsup face happy blush false", text="Не каждый день ты учишься сексу у своей матери!")
        call process_character (n, appearance="pose twohandfist face happy blush false", text="Я думаю, все мамы должны это делать!")
        call process_character (si, appearance="pose armunder face happy blush false", text="Хаха!")
        call process_character (si, appearance="pose armunder face happy blush false", text="Надеюсь, ты не будешь рекламировать это своим одноклассникам!")


    call process_character (n, appearance="pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face aroused blush false", text="...")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="...")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="[n.say_name]...")
    call process_character (si, appearance="pose handsfront face flirt blush false", text="Думаю, твой пенис хочет со мной поздороваться...")
    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face aroused blush false", text="Ну да..")
    call process_character (si, appearance="pose handsup face flirt blush false", text="Тогда выпустите его наружу...")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (n, appearance="outfit nudehard")
    pause 0.5

    call process_character (n, appearance="outfit nudehard pose handsdown face aroused blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="(У [n.say_name] знакомый взгляд ...)")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Он пялился на меня так, когда он смотрел...)")

    $ clear_characters()
    with Dissolve(0.5)
    $ n.position = "nate_simone_tit_level_nate"
    $ si.position = "nate_simone_tit_level_simone"
    pause 0.25
    $ refresh_character(n, force_no_dissolve = True)
    $ refresh_character(si, force_no_dissolve = True)
    with Dissolve(0.5)
    pause 0.5

    if "sam_simone_threesome_scene" in scenes_completed:
        call process_character (n, appearance="pose handsdown face aroused blush false", text="...")
        call process_character (si, appearance="pose handsfront face flirt blush true", text="Моя грудь снова соблазняет тебя, [n.say_name]?")
        call process_character (n, appearance="pose behindhead face aroused blush false", text="Д-да...")
        call process_character (si, appearance="pose handsup face flirt blush true", text="[sa.say_name] на этот раз.")
        call process_character (si, appearance="pose handsup face flirt blush true", text="Ты можешь наслаждаться моей грудью дольше.")
        call process_character (si, appearance="pose handsup face flirt blush true", text="Это то, что тебе нравится, милая?")
        call process_character (n, appearance="pose twohandfist face flirt blush false", text="Вот это, Мама!")
        call process_character (si, appearance="pose armunder face flirt blush true", text="Всё время в твоем распоряжении.")
        call process_character (si, appearance="pose armunder face flirt blush true", text="Мамины груди здесь для тебя!")
    else:
        call process_character (n, appearance="pose handsdown face aroused blush false", text="...")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="Ох, смотри-ка...")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="...")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="Ты действительно любишь мамину грудь, не так ли?")
        call process_character (n, appearance="pose handsdown face aroused blush false", text="Угу...")
        call process_character (si, appearance="pose handsup face flirt blush false", text="Тебе всегда нравилось смотреть на них.")
        call process_character (si, appearance="pose handsup face flirt blush false", text="Когда я помогала тебе мастурбировать, ты думал о моих сиськах.")
        call process_character (n, appearance="pose behindhead face flirt blush true", text="...")
        call process_character (si, appearance="pose armunder face flirt blush true", text="Я предлагаю их тебе, [n.say_name].")
        call process_character (si, appearance="pose armunder face flirt blush true", text="Ты можешь наслаждаться ими, как пожелаешь.")
        call process_character (n, appearance="pose handfist face aroused blush true", text="Могу?")
        call process_character (si, appearance="pose armunder face flirt blush true", text="Это то, о чем ты давно мечтал.")
        call process_character (si, appearance="pose armunder face flirt blush true", text="Мамины груди...")
        call process_character (n, appearance="pose twohandfist face aroused blush true", text="...{p}...")
        call process_character (n, appearance="pose twohandfist face aroused blush true", text="Я… Я хочу сосать их.")
        call process_character (n, appearance="pose twohandfist face aroused blush true", text="...")
        call process_character (n, appearance="pose twohandfist face aroused blush true", text="Я хочу сосать их, чтобы ты чувствовала себя хорошо, мама!")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Resort Loop2.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg simone_suck")

    call process_character (si, appearance="blush false", text="Оох, [n.say_name]!")
    call process_character (si, appearance="blush false", text="(Его рот вцепился в мою грудь!)")
    call process_character (n, appearance="blush false", text="Ммм...")
    call process_character (n, appearance="blush false", text="(Сиськи мамы больше, чем моя голова!)")
    call process_character (n, appearance="blush false", text="(Я должен использовать обе руки, чтобы поднять одну из них!)")

    if "sam_simone_threesome_scene" in scenes_completed:
        call process_character (si, appearance="blush false", text="Аа-ха!")
        call process_character (si, appearance="blush false", text="(Он ласкает мою грудь с тем же волнением, как тогда, когда [sa.say_name] была с нами!)")
        call process_character (si, appearance="blush false", text="О!")
        call process_character (si, appearance="blush false", text="(И у него так хорошо получается!)")
        call process_character (si, appearance="blush false", text="(Его рот касается с нежностью и силой моего соска!)")
        call process_character (si, appearance="blush false", text="(Он...)")
        call process_character (si, appearance="blush false", text="(Он делает меня мокрой!)")
    else:
        call process_character (si, appearance="blush false", text="Аа-ха!")
        call process_character (si, appearance="blush false", text="(Он вспахал мою грудь своим лицом!)")
        call process_character (si, appearance="blush false", text="([n.say_name] гораздо более напористый!)")
        call process_character (si, appearance="blush false", text="...")
        call process_character (si, appearance="blush false", text="(я...)")
        call process_character (si, appearance="blush false", text="(Мне нравится эта сторона [n.say_name]!)")
        call process_character (si, appearance="blush false", text="(Он позволяет своей страсти взять верх!)")
        call process_character (si, appearance="blush false", text="О!")
        call process_character (si, appearance="blush false", text="([n.say_name] долго ждал, чтобы сделать это с моей грудью...)")
        call process_character (si, appearance="blush false", text="(Я считаю, что это то, что делает его таким похотливым!)")

    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Мама...")
    call process_character (n, appearance="blush false", text="У тебя большие соски.")
    call process_character (si, appearance="blush false", text="Нравится ли тебе они?")
    call process_character (n, appearance="blush false", text="Они торчат.")
    call process_character (n, appearance="blush false", text="Я хочу продолжить сосать их...")
    call process_character (si, appearance="blush false", text="Ммм!")
    call process_character (si, appearance="blush false", text="Мои соски торчат, потому что они возбуждены.")
    call process_character (si, appearance="blush false", text="Ты возбуждаешь меня.")
    call process_character (n, appearance="blush false", text="Тогда это значит, что ты чувствуешь себя хорошо, мама!")
    call process_character (n, appearance="blush false", text="Так что я сделаю это еще раз!")
    call process_character (si, appearance="blush false", text="Милый!")
    call process_character (si, appearance="blush false", text="Ох, oox!")
    call process_character (n, appearance="blush false", text="Ммм...")
    call process_character (si, appearance="blush false", text="Я так возбуждена, [n.say_name]!")
    call process_character (si, appearance="blush false", text="Дай мне потрогать твой член!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Окей...")
    call process_character (si, appearance="blush false", text="Ты все еще можешь повеселиться с маминой грудью.")
    call process_character (si, appearance="blush false", text="Тебе просто нужно полежать у меня на коленях.")
    call process_character (si, appearance="blush false", text="Давайте попробуем вот это....")

    call static_still_ctc ("bg simone_jerksuck")

    call process_character (n, appearance="blush false", text="Ммф!")
    call process_character (si, appearance="blush false", text="Теперь я могу помассировать твой член.")
    call process_character (si, appearance="blush false", text="Тебе нравится, как я это делаю, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Мм!")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Я никогда не знала, что отношения матери и сына могут быть настолько интимными...")
    call process_character (si, appearance="blush false", text="Я думал, что было бы неприемлемо заходить так далеко...")
    call process_character (si, appearance="blush false", text="Но теперь, я бы не хотела, чтобы это было по-другому.")
    call process_character (n, appearance="blush false", text="И я, Мама!")
    call process_character (si, appearance="blush false", text="Я воспитывала тебя так, что никогда и не думала, что это случится.")
    call process_character (si, appearance="blush false", text="И теперь я чувствую, что ты тоже меня воспитываешь!")
    call process_character (n, appearance="blush false", text="Я буду продолжать делать это для тебя мама!")
    call process_character (si, appearance="blush false", text="Я знаю, милый.")
    call process_character (si, appearance="blush false", text="Ты идеальный сын.")

    if "sam_simone_threesome_scene" in scenes_completed:
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Привет, Мам...")
        call process_character (si, appearance="blush false", text="Да?")
        call process_character (n, appearance="blush false", text="Можешь положить свои сиськи на мой пенис?")
        call process_character (si, appearance="blush false", text="Мне было интересно, когда ты это спросишь.")
        call process_character (si, appearance="blush false", text="Ты хочешь, чтобы я сделала это так же, как и раньше?")
        call process_character (n, appearance="blush false", text="Да!")
        call process_character (n, appearance="blush false", text="Пожалуйста, Мама!")
        call process_character (si, appearance="blush false", text="Ты попросил так вежливо, [n.say_name]!")
        call process_character (si, appearance="blush false", text="Вот почему я знаю, что ты действительно этого хочешь.")
        call process_character (si, appearance="blush false", text="Просто стой здесь.")
        call process_character (si, appearance="blush false", text="Я спущусь к твоим ногам, чтобы правильно позиционировать себя...")
    else:
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Привет, Мам...")
        call process_character (si, appearance="blush false", text="Да?")
        call process_character (n, appearance="blush false", text="Как ты думаешь, я смогу...")
        call process_character (n, appearance="blush false", text="Положить мой член между грудей?")
        call process_character (si, appearance="blush false", text="Ох, ты хотел бы сделать это?")
        call process_character (n, appearance="blush false", text="Да, Мама!")
        call process_character (n, appearance="blush false", text="Пожалуйста!")
        call process_character (si, appearance="blush false", text="Ты попросил так вежливо, [n.say_name]!")
        call process_character (si, appearance="blush false", text="Так ты хочешь сиськотрах?")
        call process_character (n, appearance="blush false", text="Так это называется?")
        call process_character (si, appearance="blush false", text="Легко запомнить, не так ли?")
        call process_character (n, appearance="blush false", text="Затем...")
        call process_character (n, appearance="blush false", text="Пожалуйста, отсиськотрахай меня, мама.")
        call process_character (n, appearance="blush false", text="Я действительно люблю сиськотрах!")
        call process_character (si, appearance="blush false", text="Очень хорошо, [n.say_name].")
        call process_character (si, appearance="blush false", text="Тебе не нужно двигаться или что-то еще.")
        call process_character (si, appearance="blush false", text="Лёжа на самом деле идеальная установка.")
        call process_character (si, appearance="blush false", text="Мне просто нужно передвинуться сюда...")

    call static_still_ctc ("bg simone_titfuck_nocum")

    call process_character (n, appearance="blush false", text="Мааам!")
    call process_character (si, appearance="blush false", text="Ты чувствуешь мягкость моих грудей на твоём члене?")
    call process_character (n, appearance="blush false", text="Д-да!")
    call process_character (n, appearance="blush false", text="Ммм!")

    if "kira_simone_threesome_scene" in scenes_completed:
        call process_character (n, appearance="blush false", text="Это так же, как когда [k.say_name] делала это.")
        call process_character (si, appearance="blush false", text="[k.say_name] делала тебе сиськотрах, а?")
        call process_character (n, appearance="blush false", text="Д-да...")
        call process_character (si, appearance="blush false", text="Тебя соблазнила ее грудь?")
        call process_character (n, appearance="blush false", text="Они были действительно большими...")
        call process_character (n, appearance="blush false", text="Но не такими большими, как у тебя, мама!")
        call process_character (si, appearance="blush false", text="Ха-ха, нет необходимости сравнивать грудь твоей сестры с моей.")
        call process_character (si, appearance="blush false", text="Это не соревнование.")
        call process_character (n, appearance="blush false", text="...")
        call process_character (si, appearance="blush false", text="Я знаю, что это совершенно противоположное мышление твоей старшей сестры.")
        call process_character (si, appearance="blush false", text="Она, наверное, думает, что ее секс затмевает мой.")
        call process_character (si, appearance="blush false", text="Но меня это не волнует.")
        call process_character (n, appearance="blush false", text="Да?")
        call process_character (si, appearance="blush false", text="Ты и я веселимся вместе, это самое главное, дорогой.")
        call process_character (n, appearance="blush false", text="Ах, ах!")
        call process_character (n, appearance="blush false", text="Ты права, мама!")
    else:
        call process_character (si, appearance="blush false", text="...")
        call process_character (si, appearance="blush false", text="([n.say_name] любит такие вещи)")
        call process_character (si, appearance="blush false", text="(Интересно, он оценивает это выше, чем свою любимую видеоигру)")
        call process_character (n, appearance="blush false", text="Ахх, Мам!")
        call process_character (n, appearance="blush false", text="Хаа!")
        call process_character (si, appearance="blush false", text="([n.say_name] находит это еще более захватывающим, потому что он знает, что это его мать делает это?)")
        call process_character (si, appearance="blush false", text="(Меня бы это не удивило...)")
        call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
        call process_character (si, appearance="blush false", text="(Если он найдёт подружку, и она даст ему сиськотрах, он может разочароваться, ха-ха!)")
        call process_character (si, appearance="blush false", text="(Нет причин для [n.say_name] думать о девушке)")
        call process_character (si, appearance="blush false", text="(У него есть все, что ему нужно дома...)")
        call process_character (n, appearance="blush false", text="Оох, ох!")

    if "sam_simone_threesome_scene" in scenes_completed:
        call process_character (si, appearance="blush false", text="[sa.say_name] получила заряд смотря, как мы делаем это.")
        call process_character (n, appearance="blush false", text="Ей очень понравилось, да.")
        call process_character (si, appearance="blush false", text="Ты рассказал ей обо всем, что мы сделали?")
        call process_character (n, appearance="blush false", text="Нет, Мама.")
        call process_character (si, appearance="blush false", text="...")
        call process_character (si, appearance="blush false", text="На данный момент, я думаю, что ты должен ей рассказать.")
        call process_character (n, appearance="blush false", text="Так для тебя это больше не имеет значения?")
        call process_character (si, appearance="blush false", text="[sa.say_name], похоже, знает столько же о сексе, сколько и ты сейчас.")
        call process_character (si, appearance="blush false", text="И [sa.say_name] знает, что мы, по крайней мере, делаем некоторые вещи вместе.")
        call process_character (si, appearance="blush false", text="Просто пообещай мне, что будешь вести переговоры внутри семьи, хорошо?")
        call process_character (n, appearance="blush false", text="Хорошо, Мам.")
        call process_character (si, appearance="blush false", text="(Не уверен, что [sa.say_name] будет следовать этому правилу...)")

    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="М-Мам...")
    call process_character (n, appearance="blush false", text="Хотел бы я делать это вечно!")
    call process_character (si, appearance="blush false", text="Я уверена, что ты хочешь, милый!")
    call process_character (n, appearance="blush false", text="Но...")
    call process_character (si, appearance="blush false", text="Я знаю, что ты собираешься сказать...")
    call process_character (si, appearance="blush false", text="Ты чувствуешь желание кончить.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Я помогу тебе закончить, милый.")
    call process_character (si, appearance="blush false", text="Дай мне еще немного пошевелить грудью.")
    call process_character (n, appearance="blush false", text="Ааах, Хррм!")
    call process_character (si, appearance="blush false", text="Вот так?")
    call process_character (n, appearance="blush false", text="Д-Да!")
    call process_character (n, appearance="blush false", text="Да, Мама!")
    call process_character (n, appearance="blush false", text="Продолжай делать это!")
    call process_character (si, appearance="blush false", text="Я буду, малыш!")
    call process_character (si, appearance="blush false", text="Я буду двигать ими столько, сколько мне нужно, пока ты...")
    call process_character (n, appearance="blush false", text="Ммм...")
    call process_character (n, appearance="blush false", text="Ооох...")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg simone_titfuck_cum")

    call process_character (n, appearance="blush false", text="Хннг!!")
    call process_character (si, appearance="blush false", text="Ох, [n.say_name]!")
    call process_character (si, appearance="blush false", text="Твоя сперма вылетела из моей груди!")
    call process_character (n, appearance="blush false", text="Гьях!")
    call process_character (si, appearance="blush false", text="Моя грудь не может держать все это внутри!")

    call static_still_ctc ("bg simone_titfuck_aftercum")

    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (si, appearance="blush false", text="Оно повсюду, не так ли милый?")
    call process_character (si, appearance="blush false", text="Оно на мне, на тебе...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я даже не осознавал этого.")
    call process_character (si, appearance="blush false", text="Для тебя это был ценный опыт, не так ли?")
    call process_character (si, appearance="blush false", text="Мечта сбылась.")
    call process_character (n, appearance="blush false", text="Это...{w=1.0}было лучше, чем любая мечта, Мама.")
    call process_character (si, appearance="blush false", text="Теперь ты знаешь, что можешь получить крутые вещи.")
    call process_character (si, appearance="blush false", text="Просто скажи мне, когда у тебя будет захочешь мою грудь.")
    call process_character (si, appearance="blush false", text="Я здесь, чтобы поддержать тебя.")
    call process_character (n, appearance="blush false", text="Спасибо, Мам.")
    call process_character (n, appearance="blush false", text="Люблю тебя.")
    call process_character (si, appearance="blush false", text="Я тоже тебя люблю, дорогой.")
    call process_character (si, appearance="blush false", text="А теперь приведем тебя в порядок!")
    call process_character (si, appearance="blush false", text="Есть свежее мыло, которое можно использовать в душе.")

    python:
        si.revistable_scenes.add("simone_scene_titfuck_revisit")

        if not dream:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_big_breasts", 1)
            stats.add_stat("times_had_paizuri", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene ("simone_scene_titfuck", char=si, dream=dream)

    return

label simone_scene_titfuck_revisit:
    if "simone_scene_titfuck_revisit" in scenes_completed:
        call simone_scene_titfuck_revisit_2nd_time
    else:
        call simone_scene_titfuck_revisit_1st_time

    return

label simone_scene_titfuck_revisit_1st_time:
    $ no_bust_art = False
    $ display_multiple_characters([ (n, "pose twohandfist face neutral"), (si, "pose handsup face happy") ])

    call process_character (si, appearance="pose handsup face happy blush false", text="Я знала, что ты это спросишь!")
    call process_character (si, appearance="pose handsup face happy blush false", text="У тебя было такое выражение лица!")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Я буду в своей спальне через минуту...")

    $ play_music("audio/music/Resort Loop2.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg simone_suck")

    call process_character (si, appearance="blush false", text="Ах, [n.say_name]...")
    call process_character (si, appearance="blush false", text="Ты знаете, как доставить удовольствие женщине!")
    call process_character (n, appearance="blush false", text="Ммм...")
    call process_character (si, appearance="blush false", text="Даже я не могу стимулировать свою грудь так хорошо, как ты.")
    call process_character (si, appearance="blush false", text="Это что-то, как ты сосешь мои соски!")
    call process_character (si, appearance="blush false", text="{i}Задыхается!{/i}")
    call process_character (n, appearance="blush false", text="Я делаю все возможное, чтобы скопировать то, что я сделал раньше, когда тебе понравилось мама!")
    call process_character (n, appearance="blush false", text="Я помню, как мои руки держали твои сиськи - вот так...")
    call process_character (si, appearance="blush false", text="Oox!")
    call process_character (si, appearance="blush false", text="Да, это так!")
    call process_character (si, appearance="blush false", text="Именно так!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Это здорово, мама чувствует удовольствие от этого)")
    call process_character (n, appearance="blush false", text="(Я вспомнил, когда первый раз сосал ее сиськи!)")
    call process_character (n, appearance="blush false", text="(Похоже, это был идеальный способ!)")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Что тебе так нравится в моей груди, [n.say_name]?")
    call process_character (si, appearance="blush false", text="Есть что-то конкретное, что тебе в них нравится?")

    menu:
        "Мне нравится, какие они огромные!":
            call process_character (si, appearance="blush false", text="Ты говорил мне раньше, почему они тебе так нравятся.")
            call process_character (si, appearance="blush false", text="Я думаю, это подтверждает, что ваша позиция последовательна!")
            call process_character (si, appearance="blush false", text="Уверен, ты заметил, что они тоже имеют большой вес.")
            call process_character (si, appearance="blush false", text="Ты не поверите, насколько они были тяжелыми, когда я кормила грудью тебя, и [sa.say_name]!")
        "Мне нравятся твои соски!":
            call process_character (si, appearance="blush false", text="Мне самой нравится форма моих сосков.")
            call process_character (si, appearance="blush false", text="Так что это делает меня еще счастливее слышать, что ты тоже их любишь!")
        "Мне всё в них нравится!":
            call process_character (si, appearance="blush false", text="Хаха!")
            call process_character (si, appearance="blush false", text="Это не совсем конкретно, [n.say_name]!")
            call process_character (n, appearance="blush false", text="Я просто люблю каждую часть мамы!")
            call process_character (n, appearance="blush false", text="По размеру, по форме...")
            call process_character (n, appearance="blush false", text="И соски тоже!")
            call process_character (si, appearance="blush false", text="Теперь понятно.")
            call process_character (si, appearance="blush false", text="Так что все эти аспекты в сочетании делают мою грудь такой привлекательной для тебя!")
            call process_character (n, appearance="blush false", text="Именно, Мама!")

    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Думаю, пришло время твоему члену потереться о мою руку.")
    call process_character (si, appearance="blush false", text="Ты хочешь, чтобы я сделала это [n.say_name]?")
    call process_character (n, appearance="blush false", text="Да!")

    call static_still_ctc ("bg simone_jerksuck")

    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Я только что подумала, [n.say_name]...")
    call process_character (si, appearance="blush false", text="Ты понимаешь, как тебе действительно повезло?")
    call process_character (n, appearance="blush false", text="Мм?")
    call process_character (si, appearance="blush false", text="У тебя есть мать, которая готовит для тебя, чистит твою одежду, делает удобным дом, чтобы жить...")
    call process_character (si, appearance="blush false", text="И заниматься с тобой сексом!")
    call process_character (si, appearance="blush false", text="Я бы сказала, что я полноценная мать, не так ли, милый?")
    call process_character (n, appearance="blush false", text="Уверен, что да!")
    call process_character (n, appearance="blush false", text="Ты самая лучшая Мама на свете!")
    call process_character (si, appearance="blush false", text="Я рада, что ты так думаешь!")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="(Я надеюсь, что в этом году будет не так много родительских собраний...)")
    call process_character (si, appearance="blush false", text="(Я бы не хотела, чтобы [n.say_name] выпалил, что я даю ему минет за хорошие оценки или что-то в этом роде!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Как ты думаешь, ты можешь сиськотрахнуть меня сейчас, мама?")
    call process_character (si, appearance="blush false", text="Это то, чего ты с нетерпением ждал!")
    call process_character (si, appearance="blush false", text="Да! Я могу сделать сиськотрах, милый!")

    call static_still_ctc ("bg simone_titfuck_nocum")

    call process_character (n, appearance="blush false", text="А-Ах, да!")
    call process_character (n, appearance="blush false", text="Такая хорошая мама!")
    call process_character (si, appearance="blush false", text="Верь или нет, я не так много раз делала сиськотрах в моей жизни.")
    call process_character (n, appearance="blush false", text="Да?")
    call process_character (si, appearance="blush false", text="Нет.")
    call process_character (si, appearance="blush false", text="Так ты тот, на кого я полагаюсь, чтобы рассказать мне, как я с этим справляюсь!")
    call process_character (n, appearance="blush false", text="Ху!")
    call process_character (n, appearance="blush false", text="У тебя отлично получается, мама!")
    call process_character (n, appearance="blush false", text="В этом нет никаких сомнений!")
    call process_character (si, appearance="blush false", text="Я поняла, что тебе нравится, когда я прижимаю свою грудь к твоему члену.")
    call process_character (n, appearance="blush false", text="Как бы ты это ни делала, мама, для меня это потрясающе!")
    call process_character (si, appearance="blush false", text="...")

    if "kira_simone_threesome_scene" in scenes_completed:
        call process_character (si, appearance="blush false", text="(Я не могу представить, как [n.say_name] отреагирует, если [k.say_name] и я отсиськтотрахаем тебя)")
        call process_character (si, appearance="blush false", text="([n.say_name] будет в состоянии справиться с этим?)")
        call process_character (si, appearance="blush false", text="(О чем я вообще говорю?)")
        call process_character (si, appearance="blush false", text="([n.say_name] набросится на такую возможность мгновенно!)")
        call process_character (si, appearance="blush false", text="(Наличие двух больших грудей, нажимающих на его член, заставит его вспыхнуть!)")
    else:

        call process_character (si, appearance="blush false", text="([n.say_name], похоже, не возражает, насколько тяжела моя грудь на его члене...)")
        call process_character (si, appearance="blush false", text="(Бьюсь об заклад, это делает его еще более возбужденным!)")

    call process_character (si, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Это всё, мама...")
    call process_character (n, appearance="blush false", text="Ещё немного...")
    call process_character (si, appearance="blush false", text="Вероятно, ты снова замараешься, [n.say_name].")
    call process_character (n, appearance="blush false", text="Э-это нормально...")
    call process_character (n, appearance="blush false", text="Оно того стоит!")
    call process_character (n, appearance="blush false", text="Ах, aaах!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg simone_titfuck_cum")

    call process_character (n, appearance="blush false", text="Я сейчас кончу!")
    call process_character (si, appearance="blush false", text="Смотри, как далеко стреляет!")
    call process_character (n, appearance="blush false", text="Ннг!")

    call static_still_ctc ("bg simone_titfuck_aftercum")

    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (si, appearance="blush false", text="Ты выпустил много спермы этим летом.")
    call process_character (si, appearance="blush false", text="И ты не показываешь никаких признаков уменьшения!")
    call process_character (si, appearance="blush false", text="Это хороший знак, что твоё тело в отличной форме!")

    call simone_scene_titfuck_revisit_end
    return

label simone_scene_titfuck_revisit_2nd_time:
    $ no_bust_art = False
    $ display_multiple_characters([ (n, "pose twohandfist face happy"), (si, "pose handsup face happy") ])
    call process_character (si, appearance="pose handsup face happy blush false", text="Очень хорошо, милый!")

    $ play_music("audio/music/Resort Loop2.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg simone_jerksuck")

    call process_character (n, appearance="blush false", text="Ммф...")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="(Меня бы не удивило, если [n.say_name] начинает просить об этом перед сном)")
    call process_character (si, appearance="blush false", text="(Он выглядит довольно расслабленным после того, как он эякулирует)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Мама поняла, как именно обращаться с моим членом)")
    call process_character (n, appearance="blush false", text="(Она раньше делала это хорошо...)")
    call process_character (n, appearance="blush false", text="(Но теперь она крутится и тянет, и я чувствую себя безумно хорошо!)")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="(Я рада, что его член производит много предсемени)")
    call process_character (si, appearance="blush false", text="(Это делает более гладким сиськотрах для него!)")
    call process_character (si, appearance="blush false", text="(Его крайняя плоть помогает облегчить скольжение)")

    call static_still_ctc ("bg simone_titfuck_nocum")

    call process_character (n, appearance="blush false", text="Мм!")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="(Я надеюсь [n.say_name] останется сосредоточенным в классе)")
    call process_character (si, appearance="blush false", text="(Весь этот секс может заставить его мечтать об этом)")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="(Я надеюсь, что так не будет)")
    call process_character (si, appearance="blush false", text="(Пока учитель делает предметы интересными, он должен быть в порядке)")
    call process_character (si, appearance="blush false", text="(Последнее, что нам нужно, это чтобы его привели к директору из-за мастурбации во время занятий...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Как мамины сиськи стали такими большими?)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я, кажется, помню, что она сказала, что это связано с моим рождением и [sa.say_name])")
    call process_character (n, appearance="blush false", text="(Она сказала, что они стали большими после этого...)")
    call process_character (n, appearance="blush false", text="(И я думаю, что она сказала, что это связано с генетикой...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Означает ли это, что они станут еще больше, если у меня будет маленький брат или сестра?)")
    call process_character (n, appearance="blush false", text="(Хм...)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", xalign = 0.1, yalign = 0.1)
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg simone_titfuck_cum")

    call process_character (n, appearance="blush false", text="Мааам!")
    call process_character (si, appearance="blush false", text="Очень хорошо, дорогой!")
    call process_character (si, appearance="blush false", text="Убедись, что ты выпустил всё!")

    call static_still_ctc ("bg simone_titfuck_aftercum")

    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}Вздох.{/i}..")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="(Его сперма такая свежая)")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="(У меня соблазн лизнуть его...)")

    call simone_scene_titfuck_revisit_end
    return

label simone_scene_titfuck_revisit_end:
    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_big_breasts", 1)
        stats.add_stat("times_had_paizuri", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene ("simone_scene_titfuck_revisit", char=si, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return