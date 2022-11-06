init python:
    def sam_simone_threesome_scene_choose_sam(dream, revisit):
        store.sam_simone_threesome_scene_current_partner = sa
        renpy.call("sam_simone_threesome_scene_choose_sam", dream, revisit)
        return

    def sam_simone_threesome_scene_choose_simone(dream, revisit):
        store.sam_simone_threesome_scene_current_partner = si
        renpy.call("sam_simone_threesome_scene_choose_simone", dream, revisit)
        return

    def sam_simone_threesome_scene_continue(dream, revisit):
        if not revisit:
            renpy.call("sam_simone_threesome_scene_phase_3", dream)
        
        return

label kira_simone_threesome_scene(dream=False):
    call kira_simone_threesome_scene_sex (dream=dream)

    return

label kira_simone_threesome_scene_sex(dream=False):
    call process_scene_beginning (bg="bg hallway_evening", char_tuple_array=[], dream=dream)

    call process_character (k, appearance="outfit underwear pose armsup face neutral blush false", text="Фьюю...")
    call process_character (k, appearance="pose armsup face neutral blush false", text="(Какой долгий выдался денек!)")
    call process_character (k, appearance="pose armcross face neutral blush false", text="(Будет приятно принимать душ и завалиться спать)")
    call process_character (k, appearance="pose armcross face neutral blush false", text="...{p}...")
    call process_character (k, appearance="pose handhip face happy blush false", text="(Хо, хо!)")
    call process_character (k, appearance="pose handhip face happy blush false", text="(Что это такое?)")
    call process_character (k, appearance="pose armcross face neutral blush false", text="(Видимо, [n.say_name] оставил дверь открытой)")
    call process_character (k, appearance="pose armcross face happy blush false", text="(Это открытое приглашение!)")
    call process_character (k, appearance="pose armsup face happy blush false", text="(Мой день еще не совсем закончен...)")
    call process_character (n, text="Ах! Ммм...")
    call process_character (k, appearance="pose armcross face surprised blush false", text="(Что это было?)")
    call process_character (n, text="Ах, Ммм...")
    call process_character (k, appearance="pose handhip face neutral blush false", text="(Ох, это [n.say_name] похотливо стонет...)")
    call process_character (k, appearance="pose handhip face neutral blush false", text="...")
    call process_character (k, appearance="pose armcross face concerned blush false", text="(Только не говори мне, что он там дрочит...)")
    call process_character (k, appearance="pose handhip face happy blush false", text="(Я могла бы позаботиться об этом легко, бро!)")
    call process_character (k, appearance="pose armsup face neutral blush false", text="(Тебе действительно не хватает самоконтроля?)")
    call process_character (k, appearance="pose armsup face neutral blush false", text="...")
    call process_character (k, appearance="pose handhip face neutral blush false", text="(Может помочь ему закончить, если он хлопает своим мясом)")
    call process_character (k, appearance="pose armcross face happy blush false", text="(Я должна заглянуть и посмотреть, как он поживает...)")
    call process_character (k, appearance="pose armcross face happy blush false", text="(Бьюсь об заклад, это смешно!)")

    call static_still_ctc ("bg simone_blowjob_nude")

    call process_character (n, appearance="pose armcross face happy blush false", text="М-Мам...")
    call process_character (n, appearance="pose armcross face happy blush false", text="Э-это чувство, ах...")
    call process_character (n, appearance="pose armcross face happy blush false", text="Так хорошо!")
    call process_character (si, appearance="pose armcross face happy blush false", text="Мм, Ммф.")
    call process_character (k, appearance="pose armcross face happy blush false", text="!!!")
    call process_character (k, appearance="pose armcross face happy blush false", text="(Что {w=1.0}за {w=1.0}хрень?!)")
    call process_character (k, appearance="pose armcross face happy blush false", text="...")
    call process_character (k, appearance="pose armcross face happy blush false", text="(Святое дерьмо!)")
    call process_character (k, appearance="pose armcross face happy blush false", text="...")
    call process_character (k, appearance="pose armcross face happy blush false", text="(Мама сосет у [n.say_name]!)")
    call process_character (k, appearance="pose armcross face happy blush false", text="...")
    call process_character (k, appearance="pose armcross face happy blush false", text="(Я имею в виду, {w=0.5}она действительно сосёт ему!)")
    call process_character (k, appearance="pose armcross face happy blush false", text="...")

    window hide
    call bust_art_background (name="bg kira_room_evening")

    call process_character (k, appearance="pose armsup face surprised blush false", text="(Я не могу поверить в то, что я только что видела...)")
    call process_character (k, appearance="pose armsup face surprised blush false", text="...")
    call process_character (k, appearance="pose armcross face embarrassed blush false", text="([n.say_name] получает удовольствие от Мамы!)")
    call process_character (k, appearance="pose armcross face embarrassed blush false", text="(Нереально!)")
    call process_character (k, appearance="pose armcross face embarrassed blush false", text="...{p}...")
    call process_character (k, appearance="pose handhip face happy blush false", text="([n.say_name]!)")
    call process_character (k, appearance="pose handhip face happy blush false", text="(Какой же ты гребаный жеребец!)")
    call process_character (k, appearance="pose handhip face happy blush false", text="(Одного женского рта было недостаточно, чтобы удовлетворить тебя, а?)")
    call process_character (k, appearance="pose handhip face happy blush false", text="...")
    call process_character (k, appearance="pose armcross face neutral blush false", text="(Я немного удивлена, что это была мама...)")
    call process_character (k, appearance="pose armsup face happy blush false", text="(Я думаю, он хочет сохранить это в семье!)")
    call process_character (k, appearance="pose armsup face happy blush false", text="...")
    call process_character (k, appearance="pose armsup face curious blush false", text="(Подождите секунду...)")
    call process_character (k, appearance="pose armsup face curious blush false", text="...")
    call process_character (k, appearance="pose handhip face curious blush false", text="(Нет способа, почему [n.say_name] был способен соблазнить маму!)")
    call process_character (k, appearance="pose armcross face curious blush false", text="([n.say_name] может быть, завоевывает доверие, но он не так самоуверен!)")
    call process_character (k, appearance="pose armcross face curious blush false", text="(Только мама будет сосать ему, если...)")
    call process_character (k, appearance="pose armcross face curious blush false", text="...")
    call process_character (k, appearance="pose handhip face surprised blush false", text="(Ох {w=1.0}мой {w=1.0}чёртов...)")
    call process_character (k, appearance="pose armsup face surprised blush false", text="(Мама ухаживала за ним?!)")
    call process_character (k, appearance="pose armsup face happy blush false", text="(Черт возьми, а я думала, что я извращенка!)")
    call process_character (k, appearance="pose armsup face happy blush false", text="(Но опуститься до члена своего сына?)")
    call process_character (k, appearance="pose armcross face happy blush false", text="(Ах, как не стыдно, Мама!)")
    call process_character (k, appearance="pose armcross face happy blush false", text="...")
    call process_character (k, appearance="pose handhip face neutral blush false", text="(Я недооценила тебя, бро...)")
    call process_character (k, appearance="pose armcross face neutral blush false", text="(Ты держал это в секрете от меня долгое время)")
    call process_character (k, appearance="pose armsup face happy blush false", text="(Я поражена, что не поймала тебя раньше!)")
    call process_character (k, appearance="pose armsup face happy blush false", text="(Отличная работа, бро)")
    call process_character (k, appearance="pose armsup face happy blush false", text="...")
    call process_character (k, appearance="pose armcross face neutral blush false", text="(Какая потрясающая новость!)")
    call process_character (k, appearance="pose armcross face neutral blush false", text="...")
    call process_character (k, appearance="pose armcross face flirt blush false", text="(Завтра будет интересный день...)")

    call fade_to_black (1)

    call bust_art_background (name="bg simone_room_daytime")

    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (si, "outfit clothes pose armunder face happy blush") ])

    call process_character (si, appearance="pose armunder face happy blush false", text="{i}Зевок{/i}...")
    call process_character (si, appearance="pose armunder face happy blush false", text="О, Господи Боже мой.")
    call process_character (si, appearance="pose armunder face happy blush false", text="Я легла спать позже, чем хотела!")
    call process_character (n, appearance="pose behindhead face aroused blush false", text="{i}Зевок{/i}...")
    call process_character (si, appearance="pose handsup face happy blush false", text="Похоже, ты тоже!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Да...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Но ты хорошо провёл время прошлой ночью?")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Да, мама!")
    call process_character (si, appearance="pose armunder face happy blush false", text="Хорошо!")
    call process_character (n, appearance="pose handpocket face neutral blush false")
    call process_character (si, appearance="pose armunder face happy blush false")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Ты...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Нужна помощь сегодня утром?")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Ты хочешь, чтобы я тебе отсосала?")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Это было бы потрясающе, мама!")
    call process_character (si, appearance="pose handsup face happy blush false", text="Это должно быть быстро!")
    call process_character (si, appearance="pose handsup face happy blush false", text="У меня впереди напряженный день.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="{cps=40}Хочешь ли ты лечь на кровать для минета или-{/cps}{w=0.75}{nw}")

    call character_leave_dissolve (n)

    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false position right", text="Помогаешь [n.say_name] с его утренним стояком, Мама?")
    call process_character (si, appearance="pose armunder face surprised blush false")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose twohandfist face embarrassed blush false")
    pause 1
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armcross face neutral blush false")
    call process_character (si, appearance="pose armunder face surprised blush false", text="[k.say_name[0]]-[k.say_name]!")
    call process_character (si, appearance="pose armunder face surprised blush false", text="...")
    call process_character (si, appearance="pose handsup face surprised blush true", text="[n.say_name]!")
    call process_character (si, appearance="pose handsup face surprised blush true", text="Почему ты не запер дверь?!")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="{i}Угх{/i}...")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face neutral blush false", text="Эй, ты не можешь винить его.")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face happy blush false", text="Он был слишком занят моментом.")
    call process_character (si, appearance="pose armunder face embarrassed blush true", text="Я...")
    call process_character (si, appearance="pose armunder face embarrassed blush true", text="Я понятия не имею, о чем ты говоришь.")
    call process_character (si, appearance="pose handsfront face embarrassed blush true", text="[n.say_name] пожелал{w=1.0}, мне доброго утра.")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose behindhead face concerned blush true", text="...")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armsup face neutral blush false", text="Его доброе утро включает полировку хера?")
    call process_character (si, appearance="pose handsup face embarrassed blush false", text="...")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armcross face neutral blush false", text="И как называется этот эквивалент сна?")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armcross face happy blush false", text="Уложить и натянуть?")
    call process_character (si, appearance="pose armunder face embarrassed blush false", text="...{p}...")
    call process_character (si, appearance="pose handsfront face embarrassed blush false", text="Т-тебе должно быть это приснилось, [k.say_name].")
    call process_character (si, appearance="pose handsfront face embarrassed blush false", text="{cps=40}Я не была наверху прошлой ночью в спальне [n.say_name]-{/cps}{w=0.75}{nw}")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face curious blush false", text="Мам, у тебя все еще пятно спермы на свитере.")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face curious blush false", text="Просто признай это.")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face curious blush false", text="Ты отсасывала у [n.say_name].")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armcross face flirt blush false", text="Ты сосала, пока он не взорвался у тебя на лице.")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose handpocket face embarrassed blush true", text="...")
    call process_character (si, appearance="pose armunder face concerned blush true", text="...")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face neutral blush false", text="Нечего сказать, да?")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face neutral blush false", text="...")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face neutral blush false", text="Что насчет тебя, [n.say_name]?")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armsup face neutral blush false", text="Как тебе мамин язык?")
    call process_character (si, appearance="pose handsup face surprised blush false", text="[k.say_name]!!")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face flirt blush false", text="Было тепло и уютно?")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose behindhead face curious blush true", text="...")
    call process_character (si, appearance="pose handsfront face angry blush true", text="[k.say_name], немедленно убирайся из комнаты!")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armsup face neutral blush false", text="Почему?")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armsup face neutral blush false", text="Ты думаешь, что я забуду, что случилось?")
    call process_character (si, appearance="pose armunder face angry blush true", text="Ты не скажешь об этом ни одной душе, [k.say_name]!")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face neutral blush false", text="Как давно ты занимаешься этим, мама?")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face neutral blush false", text="Как давно ты тренируешь его член?")
    call process_character (si, appearance="pose handsup face angry blush true", text="[k.say_name]...")
    call process_character (si, appearance="pose handsup face angry blush true", text="У тебя будут большие неприятности, если продолжишь в том же духе...")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armcross face neutral blush false", text="Я не собираюсь никому говорить, мама.")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armcross face neutral blush false", text="На самом деле, у меня даже нет проблем с этим.")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose twohandfist face concerned blush true", text="М-Мама!")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose twohandfist face concerned blush true", text="У меня не будет проблем с [k.say_name]!")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose twohandfist face embarrassed blush true", text="Не надо ее наказывать!")
    call process_character (si, appearance="pose armunder face concerned blush true", text="...")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armsup face neutral blush false", text="Видишь?")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armsup face neutral blush false", text="[n.say_name] в порядке.")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose handfist face concerned blush true", text="[k.say_name] сосет мне, и это тоже не должно быть проблемой!")
    call process_character (si, appearance="pose handsup face surprised blush false", text="Ч-Ч-Что?!")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armsup face embarrassed blush false", text="...")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="...")
    call process_character (si, appearance="pose armunder face surprised blush false", text="[k.say_name]!")
    call process_character (si, appearance="pose armunder face surprised blush false", text="Ты занимаешься оральным сексом с [n.say_name]?!")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armsup face embarrassed blush true", text="...")
    call process_character (si, appearance="pose handsup face surprised blush false", text="Ты его старшая сестра!")
    call process_character (si, appearance="pose armunder face angry blush false", text="Как ты могла так им воспользоваться?!")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face curious blush false", text="Стой, стой!")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face curious blush false", text="Не пытайся провернуть это со мной!")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose armcross face curious blush false", text="Ты так же виновна, если не больше!")
    call process_character (si, appearance="pose handsup face concerned blush false", text="Я всегда делала так, чтобы [n.say_name] было комфортно со мной!")
    call process_character (si, appearance="pose handsup face angry blush false", text="Ты, наверное, заставляла его заниматься с тобой сексом!")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face angry blush false", text="Это не соответствует действительности!")
    call character_leave_dissolve (n)
    call process_character (k, appearance="pose handhip face angry blush false", text="Это был выбор [n.say_name], чтобы сделать это!")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose twohandfist face sad blush true", text="Хватит! {w=0.5} Стоп!")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose twohandfist face sad blush true", text="Я не хочу, чтобы вы дрались!")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose twohandfist face sad blush true", text="Это случилось из-за меня!")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose twohandfist face sad blush true", text="Это я во всем виноват!")

    call character_leave_dissolve (n)
    call process_character (si, appearance="pose handsup face embarrassed blush false")
    pause 0.5

    call process_character (k, appearance="pose armsup face sad blush false")
    call process_character (si, appearance="pose handsup face embarrassed blush false", text="[n.say_name], милый, подожди!")

    call process_character (k, appearance="pose armsup face sad blush false", text="...")
    call process_character (si, appearance="pose handsfront face concerned blush false", text="...")
    call process_character (k, appearance="pose armcross face concerned blush false", text="В этом нет ничего хорошего.")
    call process_character (si, appearance="pose handsfront face concerned blush false", text="[n.say_name] очень расстроен.")
    call process_character (si, appearance="pose armunder face sad blush false", text="Зачем ты вломилась?")
    call process_character (si, appearance="pose armunder face sad blush false", text="Теперь [n.say_name] будет плакать весь день.")
    call process_character (k, appearance="pose handhip face concerned blush false", text="Мам, ты правда думала, что сможешь хранить это в секрете вечно?")
    call process_character (si, appearance="pose handsfront face concerned blush false", text="...")
    call process_character (k, appearance="pose armcross face concerned blush false", text="В конце концов, ты бы тоже узнала обо мне.")
    call process_character (si, appearance="pose armunder face concerned blush false", text="...")
    call process_character (k, appearance="pose handhip face concerned blush false", text="Мы должны признать, что мы оба наслаждались [n.say_name].")
    call process_character (k, appearance="pose armcross face embarrassed blush false", text="Хотя после того, как [n.say_name] сбежал...")
    call process_character (k, appearance="pose armcross face embarrassed blush false", text="Я не знаю, захочет ли он что-нибудь сделать с нами...")
    call process_character (si, appearance="pose handsup face curious blush false", text="Я знаю...")
    call process_character (si, appearance="pose handsup face curious blush false", text="...")
    call process_character (si, appearance="pose handsup face curious blush false", text="Он думает, что виноват в нашей соре.")
    call process_character (k, appearance="pose handhip face concerned blush false", text="Мы должны оставить в стороне наши чувства по этому поводу.")
    call process_character (k, appearance="pose handhip face concerned blush false", text="[n.say_name] должен быть в центре.")
    call process_character (si, appearance="pose handsfront face curious blush false", text="Да, и это несправедливо по отношению к нему.")
    call process_character (si, appearance="pose handsfront face curious blush false", text="...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Нам обоим нужно поговорить с ним, прямо сейчас.")
    call process_character (k, appearance="pose armcross face neutral blush false", text="Согласна!")

    if "sam_simone_threesome_scene" in scenes_completed:
        call character_leave_dissolve (k)
        pause 0.5
        call process_character (si, appearance="pose handsup face neutral blush false", text="...{p}...")
        call process_character (si, appearance="pose handsup face embarrassed blush false", text="(Я не могу поверить, что это происходит!)")
        call process_character (si, appearance="pose handsup face embarrassed blush false", text="(Сначала я узнаю, что [sa.say_name] и [n.say_name] экспериментировали с сексом...)")
        call process_character (si, appearance="pose armunder face surprised blush false", text="(Но [k.say_name] тоже?!)")
        call process_character (si, appearance="pose armunder face surprised blush false", text="(Как такое могло произойти?!)")
        call process_character (si, appearance="pose armunder face surprised blush false", text="...{p}...")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="(Я не могу думать об этом сейчас)")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="([k.say_name] и мне нужно успокоить [n.say_name]...)")

    call fade_to_black (1)

    call bust_art_background (name="bg nate_room_daytime")

    call process_character (n, appearance="pose behindhead face sad blush true", text="(Это просто ужасно!)")
    call process_character (n, appearance="pose behindhead face sad blush true", text="(Теперь [k.say_name] и мама ненавидят друг друга!)")
    call process_character (n, appearance="pose twohandfist face sad blush false", text="(И я мог бы предотвратить это...)")
    call process_character (n, appearance="pose twohandfist face sad blush false", text="...")
    call process_character (n, appearance="pose behindhead face sad blush false", text="{cps=40}(Я не должен был пытаться-){/cps}{w=0.75}{nw}")

    call process_character (si, appearance="pose armunder face neutral blush false", text="Милый?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Мы можем с тобой поговорить?")
    call process_character (n, appearance="pose handpocket face sad blush false", text="М-Мам?")
    call process_character (n, appearance="pose handpocket face sad blush false", text="[k.say_name[0]]-[k.say_name]?")
    call character_leave_dissolve (si)
    call process_character (k, appearance="pose armcross face neutral blush false position left", text="Просто успокойся, [n.say_name].")
    call character_leave_dissolve (si)
    call process_character (k, appearance="pose armcross face neutral blush false", text="Все в порядке.")
    call process_character (n, appearance="pose twohandfist face sad blush false", text="Мама не выгонит тебя из дома?")
    call character_leave_dissolve (k)
    call process_character (si, appearance="pose handsup face neutral blush false", text="Конечно, нет, [n.say_name].")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Я бы никогда так не поступила.")
    call character_leave_dissolve (si)
    call process_character (k, appearance="pose armcross face concerned blush false", text="Прости, что расстроила тебя, брат.")
    call process_character (n, appearance="pose twohandfist face sad blush false", text="...{p}...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
    call character_leave_dissolve (k)
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Я тоже прошу прощения.")
    call process_character (si, appearance="pose armunder face curious blush false", text="Мы пережили много эмоций...")
    call process_character (si, appearance="pose armunder face curious blush false", text="И я не думала рационально, пока говорила.")
    call character_leave_dissolve (si)
    call process_character (k, appearance="pose handhip face concerned blush false", text="И теперь я это понимаю...")
    call process_character (k, appearance="pose handhip face concerned blush false", text="Я должна была поговорить об этом с Мамой наедине.")
    call process_character (n, appearance="pose handpocket face concerned blush false")
    call character_leave_dissolve (si)
    call process_character (k, appearance="pose handhip face concerned blush false")
    call character_leave_dissolve (k)
    call process_character (si, appearance="pose handsup face neutral blush false", text="Ты не сделал ничего плохого, [n.say_name].")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Не вини себя в этом.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Ты не заставлял нас ссориться.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Вы все еще сердитесь друг на друга?")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Нет, это не так.")
    call character_leave_dissolve (si)
    call process_character (k, appearance="pose armcross face neutral blush false", text="Мы все уладили, бро.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Так...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Что теперь будем делать со всем этим?")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Вы обе любите проводить со мной время.")
    call process_character (n, appearance="pose twohandfist face concerned blush false", text="Мне не придется выбирать, не так ли?")
    call character_leave_dissolve (si)
    call process_character (k, appearance="pose armcross face neutral blush false", text="...")
    call character_leave_dissolve (k)
    call process_character (si, appearance="pose armunder face neutral blush false", text="...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Выбирать между нами не нужно.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Было бы несправедливо и затруднительно возложить это бремя на тебя.")
    call character_leave_dissolve (si)
    call process_character (k, appearance="pose armsup face neutral blush false", text="Да.")
    call process_character (n, appearance="pose handpocket face concerned blush false")
    call character_leave_dissolve (si)
    call process_character (k, appearance="pose armsup face neutral blush false")
    call character_leave_dissolve (k)
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Гораздо важнее, чтобы мы наслаждались все вместе.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Ты понимаешь, что я имею в виду, правильно, [k.say_name]?")
    call character_leave_dissolve (si)
    call process_character (k, appearance="pose handhip face flirt blush false", text="О, да...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Я точно знаю, что ты имеешь в виду.")

    call static_still_ctc ("bg simonekira_3some_smile")

    call process_character (n, appearance="pose handhip face flirt blush false", text="Что вы собираетесь сделать?")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Есть только одна вещь, которую нужно сделать, [n.say_name]...")
    call process_character (n, appearance="pose handhip face flirt blush false", text="...{p}...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Мы действительно должны быть настолько очевидны с тобой?")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg simonekira_3some_titsquish")

    call process_character (n, appearance="pose handhip face flirt blush false", text="!!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Ты понимаешь, что происходит?")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Ммф!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Не нажимай слишком сильно, [k.say_name].")
    call process_character (si, appearance="pose handhip face flirt blush false", text="[n.say_name] требуется некоторое пространство для дыхания.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Поверь мне, [n.say_name] любит это.")
    call process_character (n, appearance="pose handhip face flirt blush false", text="М-Мам?")
    call process_character (n, appearance="pose handhip face flirt blush false", text="И тебя это устраивает?")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Да, если это устраивает и тебя, сладкий.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Ты в полном порядке, бро.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Я могу сказать.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Знаешь, как тебе повезло, что это случилось?")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Твоя мама и старшая сестра прижимаются сиськами к твоей голове.")
    call process_character (n, appearance="pose handhip face flirt blush false", text="...")
    call process_character (si, appearance="pose handhip face flirt blush false", text="[k.say_name] так сильно домогается?")
    call process_character (n, appearance="pose handhip face flirt blush false", text="...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Эй, я могу подомогаться до тебя...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Но я никогда не отказываю ему в том, чего он хочет!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Это значит быть хорошей сестрой!")

    call static_still_ctc ("bg simonekira_3some_pantson")

    call process_character (si, appearance="pose handhip face flirt blush false", text="...")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Ты хочешь снять с меня штаны, [n.say_name]?")
    call process_character (n, appearance="pose handhip face flirt blush false", text="...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Не говори, ты слишком нервный, бро!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Нервничать - это нормально, милый.")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Ты можешь не знать, что делать, когда с тобой две женщины.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Может быть...")

    call static_still_ctc ("bg simonekira_3some_pantsoff")

    call process_character (si, appearance="pose handhip face flirt blush false", text="Вот мы!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Без штанов.")
    call process_character (n, appearance="pose handhip face flirt blush false", text="...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="А вот это шокирующая новость...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="У тебя всё ещё не встал?!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Я могу помочь тебе с мастурбацией, милый, если хочешь.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Нет...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="[n.say_name] требует более пристального внимания...")

    call static_still_ctc ("bg simonekira_3some_liftbro")

    call process_character (n, appearance="pose handhip face flirt blush false", text="Что?!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Хорошо, уступаю тебе, Мама.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Не окажешь мне честь?")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Должна быть причина, почему [n.say_name] стонал так сильно прошлой ночью!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Покажи, на что ты способна!")

    call static_still_ctc ("bg simonekira_3some_nosaliva")

    call process_character (k, appearance="pose handhip face flirt blush false", text="[n.say_name], смотри!")
    call process_character (n, appearance="pose handhip face flirt blush false", text="...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Посмотри, как близко мамин рот к твоему члену.")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Д-да...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Чувствуешь горячий воздух из ее рта?")
    call process_character (si, appearance="pose handhip face flirt blush false", text="([k.say_name] очень любит прелюдии...)")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Ты так извиваешься, бро!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="О, ты тоже это заметила?")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Думаю, он наполовину червяк или типа того!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Это просто [n.say_name] так реагирует на волнение.")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Ты предвкушаешь минет, не так ли милый?")
    call process_character (n, appearance="pose handhip face flirt blush false", text="...")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Мне нравится, как ты это делаешь, мама.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Эй!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="А как насчет меня?")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Мне тоже нравится, как ты это делаешь, сестренка!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Тебе нравится, как мы обе это делаем, не так ли?")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Д-да!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="[n.say_name] просто хотел сказать, что ему нравится это чувство, [k.say_name].")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Он не имел в виду, что у меня лучше получается.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Ладно, хватит болтать.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Я хочу увидеть тебя в действии, мама.")

    call static_still_ctc ("bg simonekira_3some_blowjob")

    call process_character (si, appearance="pose handhip face flirt blush false", text="Ммм...")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Хаах!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Посмотри на себя Мама!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Mмф...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Это материнская любовь или что?")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Ах, ох...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Я вижу, чем ты занимаешься...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Ты много сосешь его кончик.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Идешь по самому чувствительному месту, да?")
    call process_character (si, appearance="pose handhip face flirt blush false", text="...")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Это может сократить время, как долго он может длиться.")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Но я предпочитаю доставлять сыну удовольствие.")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Ннг!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Вот какую штуку Мама делает!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Эй, [n.say_name]...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Кто ещё может сказать, что их мама отсасывает им вот так?")

    call static_still_ctc ("bg simonekira_3some_saliva")

    call process_character (si, appearance="pose handhip face flirt blush false", text="Мм, [n.say_name]...")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Не рассказывай об этом одноклассникам в школе!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Ха!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Мама, ему все равно никто не поверит!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Они не поверят, что ребенок настолько удачлив!")
    call process_character (n, appearance="pose handhip face flirt blush false", text="...")

    call static_still_ctc ("bg simonekira_3some_blowjobclose")

    call process_character (n, appearance="pose handhip face flirt blush false", text="Аах...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Как ты держишься, [n.say_name]?")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Твой голова-шар для боулинга плюхнулась назад!")
    call process_character (n, appearance="pose handhip face flirt blush false", text="...")
    call process_character (n, appearance="pose handhip face flirt blush false", text="М-мам…")
    call process_character (k, appearance="pose handhip face flirt blush false", text="...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="(Я не думаю, что мама собирается отпускать в ближайшее время...)")
    call process_character (k, appearance="pose handhip face flirt blush false", text="(Посмотри на эту технику!)")
    call process_character (k, appearance="pose handhip face flirt blush false", text="...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="(Как она научилась так сосать?)")
    call process_character (k, appearance="pose handhip face flirt blush false", text="...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="(Мне придется поговорить с ней об этом!)")
    call process_character (n, appearance="pose handhip face flirt blush false", text="[k.say_name[0]]-[k.say_name]...")
    call process_character (n, appearance="pose handhip face flirt blush false", text="С-скажи Маме, что я...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Ох?")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Про взрыв?")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Ммм...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Прикончи его, мамочка!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Дай ему несколько жестких отсосов, и он будет готов!")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Х-Ха?!")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Ах, ах, ах!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Хорошо, Мам!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="[n.say_name] сейчас в деле!")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Ах, хрмм!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Он свернулся калачиком!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="И...")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg simonekira_3some_cumshot")

    call process_character (k, appearance="pose handhip face flirt blush false", text="Вот оно!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="(Посмотрите на маму, принимающую эту порцию, как профессионал!)")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Ааах...")
    call process_character (n, appearance="pose handhip face flirt blush false", text="...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="После этого ты почувствуешь себя на 10 фунтов легче [n.say_name], хаха!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Твои набухшие яйца, должно быть, тянули тебя вниз!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="{i}Глык{/i}...")
    call process_character (si, appearance="pose handhip face flirt blush false", text="{i}Кашляет!{/i}")
    call process_character (k, appearance="pose handhip face flirt blush false", text="О, ты уже проглотила всё, Мама?")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Я надеялась, что ты покажешь мне добычу своих усилий!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="(Сперма [n.say_name] была густой!)")
    call process_character (si, appearance="pose handhip face flirt blush false", text="(Почти подавилась ей!)")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Сильная штука, не правда ли мама?")
    call process_character (si, appearance="pose handhip face flirt blush false", text="...")
    call process_character (si, appearance="pose handhip face flirt blush false", text="[n.say_name] очень здоровый!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Достаточно здоров для второго раунда?")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Оох...")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Потолок кружится.")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Я знаю, что ты хотела бы, [k.say_name]...")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Но как только [n.say_name] получает оргазм, он быстро выдыхается.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Да, это действительно так.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="После такого извержения брата нужно перезарядить.")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Я могу попробовать еще разок...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Хаха!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Ты так говоришь, но выглядишь опьянённым!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="У тебя был бурный день, дорогой.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Не говоря уже о бурной ночи!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Эх, эх?")
    call process_character (si, appearance="pose handhip face flirt blush false", text="...")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Да.")
    call process_character (n, appearance="pose handhip face flirt blush false", text="...")
    call process_character (n, appearance="pose handhip face flirt blush false", text="Мы сможем сделать это снова, верно?")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Не понимаю, почему бы и нет.")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Я отлично провела время с вами!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="...")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Как ты относишься к этому, [k.say_name]?")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Я чувствую, что ты становишься мертвым грузом, бро!")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Я кладу тебя на кровать.")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Но ты знаешь, где найти меня и маму...")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Я всегда готова надрать тебе яйца, {w=0.5}но в хорошем смысле!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="[k.say_name], хаха!")
    call process_character (si, appearance="pose handhip face flirt blush false", text="...")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Давай дадим [n.say_name] шанс отдохнуть.")
    call process_character (si, appearance="pose handhip face flirt blush false", text="Он даст нам знать, когда будет готов снова....")

    call add_replayable_scene ("kira_simone_threesome_scene", si)
    call add_replayable_scene ("kira_simone_threesome_scene", k)

    python:
        k.revistable_scenes.add("kira_simone_threesome_scene_revisit_kira")
        si.revistable_scenes.add("kira_simone_threesome_scene_revisit_simone")

        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_received_blowjob", 1)
            stats.add_stat("times_had_group_sex", 1)
            stats.add_stat("times_cummed_in_mouth", 1)

    call process_end_of_scene ("kira_simone_threesome_scene", dream=dream)

    return


label kira_simone_threesome_scene_revisit_kira:
    $ no_bust_art = False

    if "kira_simone_threesome_scene_revisit" in scenes_completed:
        call process_character (n, appearance="pose twohandfist face happy")
        call process_character (k, appearance="pose handhip face neutral", text="Тебе правда нравится, когда тебя несут на руках старшей сестры?")
        call process_character (k, appearance="pose handhip face happy", text="Мои сиськи хлюпают возле тебя, вот почему.")
        call process_character (k, appearance="pose armsup face happy", text="Мягкие сиськи сестры в сочетании с жесткий отсосом от мамы...")
    else:
        call process_character (n, appearance="pose twohandfist face happy")
        call process_character (k, appearance="pose armsup face happy", text="Хорошо, пойдем спросим у нее!")
        call process_character (k, appearance="pose armsup face happy", text="Я склонна думать, что она согласится.")

    call kira_simone_threesome_scene_revisit

    return

label kira_simone_threesome_scene_revisit_simone:
    $ no_bust_art = False

    if "kira_simone_threesome_scene_revisit" in scenes_completed:
        call process_character (n, appearance="pose twohandfist face happy")
        call process_character (si, appearance="pose armunder face happy", text="[k.say_name] собирается нарастить еще больше мышц, поднимая тебя так часто!")
        call process_character (si, appearance="pose handsup face neutral", text="Не забудь поблагодарить ее после того, как мы закончим!")
    else:
        call process_character (n, appearance="pose twohandfist face happy")
        call process_character (si, appearance="pose handsup face happy", text="Тебе бы этого хотелось, не так ли?")
        call process_character (si, appearance="pose handsup face happy", text="Позволь мне найти твою сестру!")

    call kira_simone_threesome_scene_revisit

    return

label kira_simone_threesome_scene_revisit_extended_content_choice:
    if "kira_scene_anal" and "simone_scene_vaginal" in scenes_completed:
        call process_character (k, appearance="blush false", text="Эй, бро...")
        call process_character (k, appearance="blush false", text="Ты хочешь, чтобы я занялась твоим членом?")
        call process_character (k, appearance="blush false", text="Мама получила всё веселье!")

        $ kira_suck_me_too_append = ""
        if not kira_simone_threesome_part_2_done:
            $ kira_suck_me_too_append = "(Новое!)"

        menu:
            "Да, я тоже хочу, чтобы ты меня отсосала, [k.say_name]. [kira_suck_me_too_append]":
                call process_character (si, appearance="blush false", text="Да, твоя сестра должна побыть с тобой.")
                call process_character (k, appearance="blush false", text="О, да!")
                call process_character (k, appearance="blush false", text="Твоя комната слишком мала для того, что я хочу сделать.")
                call process_character (k, appearance="blush false", text="Выходим в гостиную, проверив, чист ли горизонт.")
                jump kira_simone_threesome_extended_content_1st_time
            "Я хочу кончить в мамин рот.":
                call process_character (k, appearance="blush false", text="Хорошо, хорошо.")
                call process_character (k, appearance="blush false", text="Но в следующий раз я хочу показать маме, на что я способна!")

    return

label kira_simone_threesome_scene_revisit:
    $ scenes_completed.add("kira_simone_threesome_scene_revisit_simone")
    $ scenes_completed.add("kira_simone_threesome_scene_revisit_kira")

    if "kira_simone_threesome_scene_revisit" in scenes_completed:
        call kira_simone_threesome_scene_revisit_2nd_time
    else:
        call kira_simone_threesome_scene_revisit_1st_time

    return

label kira_simone_threesome_scene_revisit_1st_time:
    python hide:
        play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg simonekira_3some_titsquish")

    call process_character (k, appearance="", text="Не можешь удержаться от того, что мы снова вместе?")
    call process_character (k, appearance="", text="Тебе нравится, когда тебя обнимают?")
    call process_character (n, appearance="", text="Ммф...")
    call process_character (si, appearance="", text="Ты выглядишь комфортно там, [n.say_name].")
    call process_character (si, appearance="", text="Ты пытаешься вздремнуть у нас на груди?")
    call process_character (k, appearance="", text="Ты можешь сделать это позже, бро!")
    call process_character (k, appearance="", text="Положить голову на облако из сисек - это одно...")

    call static_still_ctc ("bg simonekira_3some_liftbro")

    call process_character (k, appearance="", text="Но я думаю, ты согласишься, что хороший отсос - это правильный выбор!")
    call process_character (n, appearance="", text="Мне нравится этот выбор!")
    call process_character (k, appearance="", text="Видишь?")
    call process_character (k, appearance="", text="...")
    call process_character (k, appearance="", text="Отсоси ему хорошенько, Мама!")

    call static_still_ctc ("bg simonekira_3some_nosaliva")

    call process_character (k, appearance="", text="Мама любит медленный подход!")
    call process_character (si, appearance="", text="Мне нравится втягивать его.")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Мой член начинает пульсировать!)")
    call process_character (k, appearance="", text="Я действую совершенно противоположно.")
    call process_character (k, appearance="", text="Как только я беру этот член, мой рот становится вакуумом.")
    call process_character (k, appearance="", text="Я шоком заставляю [n.say_name] получить эрекцию!")
    call process_character (si, appearance="", text="Не думаю, что важно, как это делается.")
    call process_character (si, appearance="", text="Главное, чтобы [n.say_name] наслаждался этим.")

    call static_still_ctc ("bg simonekira_3some_blowjob")

    call process_character (n, appearance="", text="Ах, да...")
    call process_character (k, appearance="", text="Ха, глаза [n.say_name] стали стеклянными.")
    call process_character (k, appearance="", text="Мне знаком этот взгляд.")
    call process_character (si, appearance="", text="Ммм...")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Это отличная, что мама и [k.say_name] ладят)")
    call process_character (n, appearance="", text="(Я думал, что они снова начнут сражаться за меня)")
    call process_character (n, appearance="", text="(Но они обе выглядят так, как будто им весело вместе!)")
    call process_character (k, appearance="", text="...")
    call process_character (k, appearance="", text="(Есть что-то удовлетворительное в том, что мама сосёт у [n.say_name]...)")
    call process_character (k, appearance="", text="(Может быть, это потому, что я обычно та, кто в этом положении)")
    call process_character (k, appearance="", text="...")
    call process_character (k, appearance="", text="(Я хочу показать маме, как я справляюсь с [n.say_name] когда-нибудь)")
    call process_character (k, appearance="", text="(Я думаю, что она будет впечатлена тем, что я могу сделать!)")

    call static_still_ctc ("bg simonekira_3some_blowjobclose")

    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="([k.say_name] в этот раз тихо себя ведёт)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я вижу, как ее соски упираются в рубашку)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Ей нравится смотреть на это!)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Она возбуждается, видя член [n.say_name]?)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Или она возбуждается, видя меня?)")
    call process_character (n, appearance="", text="{i}Вздох{/i}, {i}вздох{/i}...")
    call process_character (k, appearance="", text="...")
    call process_character (k, appearance="", text="(Вот чёрт, у мамы просто огромные буфера)")
    call process_character (k, appearance="", text="...")
    call process_character (k, appearance="", text="(Интересно, позволяла ли мама [n.say_name] кончить на ее забавные сумочки)")
    call process_character (k, appearance="", text="(Если бы я была на месте [n.say_name]...)")
    call process_character (k, appearance="", text="(Я бы жонглировала сиськами мамы, как будто завтра не наступит!)")
    call process_character (k, appearance="", text="...")
    call process_character (k, appearance="", text="(Ее сиськи, вероятно, раздавят хер [n.say_name], ха-ха!)")
    call process_character (k, appearance="", text="(Зная [n.say_name], он бы сказал, что это того стоило...)")
    call process_character (n, appearance="", text="Хаах...")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Интересно, как [sa.say_name] отреагирует на это?)")
    call process_character (n, appearance="", text="...")
    call process_character (n, appearance="", text="(Что, если она войдёт прямо сейчас?)")
    call process_character (n, appearance="", text="...")

    if "sam_scene_vaginal" in scenes_completed:
        call process_character (n, appearance="", text="(Теперь, когда я думаю об этом...)")
        call process_character (n, appearance="", text="...")
        call process_character (n, appearance="", text="(Она, вероятно, захочет присоединиться!)")
    else:
        call process_character (n, appearance="", text="(Она может взбеситься и задаться вопросом, что мы делаем)")
        call process_character (n, appearance="", text="(Надеюсь, она будет в порядке...)")

    call kira_simone_threesome_scene_revisit_extended_content_choice

    call process_character (n, appearance="", text="Ахх!")
    call process_character (n, appearance="", text="Ммм!")
    call process_character (k, appearance="", text="...")
    call process_character (k, appearance="", text="У [n.say_name] готов орех, Мама.")
    call process_character (si, appearance="", text="Это термин, который они используют сейчас, чтобы описать эякуляцию?")
    call process_character (k, appearance="", text="Это здорово, не правда ли?")
    call process_character (k, appearance="", text="Я пытаюсь давать [n.say_name], чтобы использовать его чаще.")
    call process_character (n, appearance="", text="М-Мам...")
    call process_character (n, appearance="", text="[k.say_name[0]]-[k.say_name]...")
    call process_character (k, appearance="", text="Скажи \"У меня готов орех\" [n.say_name]!")
    call process_character (k, appearance="", text="Я буду сжимать твои яйца, пока ты этого не сделаешь!")
    call process_character (si, appearance="", text="[k.say_name]!")
    call process_character (si, appearance="", text="Не будь такой злой!")
    call process_character (k, appearance="", text="Я пошутила, пошутила!")
    call process_character (k, appearance="", text="Но серьезно, просто прокричи это, [n.say_name].")
    call process_character (k, appearance="", text="Поверь мне, это помогает усилить оргазм.")
    call process_character (n, appearance="", text="...")
    call process_character (si, appearance="", text="Она просто дразнит тебя, милый.")
    call process_character (n, appearance="", text="Я-я...")
    call process_character (n, appearance="", text="Ах...")
    call process_character (si, appearance="", text="Ммм...")
    call process_character (n, appearance="", text="У меня готов орех!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg simonekira_3some_cumshot")

    call process_character (si, appearance="", text="Ммф!")
    call process_character (k, appearance="", text="Ты действительно сказал это!")
    call process_character (n, appearance="", text="Д-да...")
    call process_character (k, appearance="", text="Вот ты и кончил!")
    call process_character (k, appearance="", text="Разве оргазм не стал намного лучше?")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Часть спермы [n.say_name] вошла прямо мне в горло!)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="{i}Глык{/i}...")
    call process_character (k, appearance="", text="Ты справилась с этой порцией намного лучше, мама!")
    call process_character (si, appearance="", text="Хехе...")
    call process_character (si, appearance="", text="Спасибо [k.say_name].")

    call kira_simone_threesome_scene_revisit_end

    return

label kira_simone_threesome_scene_revisit_2nd_time:
    python hide:
        play_music("audio/music/Background Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg simonekira_3some_blowjob")

    call process_character (k, appearance="", text="Я надеюсь, что ты ценишь это, [n.say_name].")
    call process_character (k, appearance="", text="Мы с мамой готовы отложить все дела, чтобы твой член не бездельничал.")
    call process_character (si, appearance="", text="Мм...")
    call process_character (si, appearance="", text="Это показывает, как сильно мы заботимся о тебе, милый.")
    call process_character (n, appearance="", text="Ох, ах...")
    call process_character (n, appearance="", text="Спасибо, Мам.")
    call process_character (n, appearance="", text="С-спасибо, [k.say_name].")
    call process_character (n, appearance="", text="Я люблю вас.")
    call process_character (si, appearance="", text="Мы тоже тебя любим, милый.")
    call process_character (k, appearance="", text="Я жду от тебя непосредственно любви, бро.")
    call process_character (k, appearance="", text="Понимаешь, о чем я говорю?")
    call process_character (n, appearance="", text="Д-да...")

    call kira_simone_threesome_scene_revisit_extended_content_choice

    call static_still_ctc ("bg simonekira_3some_blowjobclose")

    call process_character (si, appearance="", text="([k.say_name] могла сказать нет этому...)")
    call process_character (si, appearance="", text="(Но я думаю, что она хочет отведать сексуальной активности с [n.say_name] насколько это возможно)")
    call process_character (si, appearance="", text="(Даже если она просто смотрит!)")
    call process_character (si, appearance="", text="...")
    call process_character (si, appearance="", text="(Я думаю, что она даже пропустила бы работу, если бы это означало, что она могла наслаждаться [n.say_name]!)")
    call process_character (k, appearance="", text="...")
    call process_character (k, appearance="", text="(Невероятно, как мама может вписать это в свой график)")
    call process_character (k, appearance="", text="(Ее тайм-менеджмент должен быть безупречным)")
    call process_character (k, appearance="", text="(Она должна задействовать каждую минуту каждого дня)")
    call process_character (k, appearance="", text="(Опять же, у меня тоже не так много свободного времени...)")
    call process_character (k, appearance="", text="(Вот почему это здорово быть вместе для этого!)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!")
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg simonekira_3some_cumshot")

    call process_character (n, appearance="", text="Аах!")
    call process_character (si, appearance="", text="Ммм...")
    call process_character (si, appearance="", text="...")
    call process_character (k, appearance="", text="Мама наслаждается протеином, который ты ей даешь, [n.say_name].")
    call process_character (k, appearance="", text="Ты поддерживаешь ее здоровье!")
    call process_character (si, appearance="", text="Ха...")
    call process_character (si, appearance="", text="Твоя сестра не ошибается насчет спермы, содержащей белки.")
    call process_character (si, appearance="", text="Но я не могу подтвердить, здорова ли она!")

    call kira_simone_threesome_scene_revisit_end

    return

label kira_simone_threesome_scene_revisit_end:

    python:
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_cummed_in_mouth", 1)
        stats.add_stat("times_received_blowjob", 1)
        stats.add_stat("times_had_group_sex", 1)

    call process_end_of_scene ("kira_simone_threesome_scene_revisit", reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return



label sam_simone_threesome_scene(dream=False):
    call sam_simone_threesome_scene_sex (dream=dream)

    return

label sam_simone_threesome_scene_sex(dream=False):
    call process_scene_beginning (bg="bg sam_room_daytime", char_tuple_array=[ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (sa, "outfit clothes pose leaning face neutral blush false") ], dream=dream)

    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Нам нужно сделать марафонский стрим, [n.say_name]!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Что такое марафонский стрим?")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Знаешь, как те супер длинные, которые идут целый день?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Как долго мы будем разговаривать?")
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="Я не понимаю, почему мы не можем снять двенадцатичасовой стрим!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face embarrassed blush false", text="Двенадцать часов?!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face embarrassed blush false", text="А как насчет того, чтобы поесть и сходить в туалет?")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Один из нас может остаться на стриме, в то время как другой может поесть и сделать небольшой перерыв.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="Так игровой стрим никогда не остановится!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Звучит очень напряженно...")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Нет, если мы хорошо отдохнём!")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Так что убери всё из своего расписания!")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Завтра будет напряженный день!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")

    call process_new_location ("bg sam_room_evening", dream=dream)

    call process_character (sa, appearance="outfit underwear pose handsbehind face neutral blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handsbehind face neutral blush false", text="(Наши фанаты получат такой кайф от этого стрима!)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face neutral blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="Хм...")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="(Интересно, должна ли я сосать член [n.say_name], пока он играет в одну из игр...)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face neutral blush false", text="(Может быть, я буду держать счетчик выстрелов спермы в течение дня!)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face happy blush false", text="(Я могу увидеть, сколько раз [n.say_name] выстрелит из его пистона, ха-ха!)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face happy blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handface face neutral blush false", text="(Ох!)")
    call process_character (sa, appearance="outfit underwear pose handface face neutral blush false", text="(Я совершенно забыла, какие игры мы будем играть завтра!)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face happy blush false", text="(Для долгого стрима, ты должен знать такого рода вещи!)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face happy blush false", text="(Я спрошу [n.say_name] прямо сейчас!)")

    call process_new_location ("bg nate_room_evening", dream=dream)

    call process_character (sa, appearance="outfit underwear pose leaning face neutral blush false", text="Эй, [n.say_name]!")
    call process_character (sa, appearance="outfit underwear pose leaning face neutral blush false", text="{cps=40}Я хотела-{/cps}{w=0.75}{nw}")
    call process_character (sa, appearance="outfit underwear pose leaning face concerned blush false", text="А?")
    call process_character (sa, appearance="outfit underwear pose leaning face concerned blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handface face concerned blush false", text="(Где [n.say_name]?)")
    call process_character (sa, appearance="outfit underwear pose handface face concerned blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="(Я знаю, что он был здесь секунду назад)")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="(Он ушёл в ванную комнату?)")

    call process_new_location ("bg hallway_evening", dream=dream)

    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="(Нет, его нет в ванной комнате)")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="Хм...")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handface face neutral blush false", text="(Бьюсь об заклад, он пошел, чтобы перекусить на кухне)")
    call process_character (sa, appearance="outfit underwear pose handface face happy blush false", text="(Я могла бы найти что-нибудь для себя!)")

    call process_new_location ("bg kitchen_evening", dream=dream)

    call process_character (sa, appearance="outfit underwear pose handsbehind face curious blush false", text="(Его здесь тоже нет)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face curious blush false", text="(Странно...)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face curious blush false", text="...")
    call process_character (n, text="М-Мама...")
    call process_character (sa, appearance="outfit underwear pose handface face neutral blush false", text="(Эй! Я только что слышала [n.say_name]!)")
    call process_character (n, text="Аах, Мам!")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="(Он должен быть в маминой спальне...)")
    call process_character (sa, appearance="outfit underwear pose handface face concerned blush false", text="(Я надеюсь, что [n.say_name] не заболел)")
    call process_character (sa, appearance="outfit underwear pose handface face concerned blush false", text="(Это было бы облом для завтрашнего стрима...)")
    call process_character (n, text="Оох!")
    call process_character (sa, appearance="outfit underwear pose handsbehind face concerned blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handsbehind face concerned blush false", text="(Я должна увидеть, как он себя чувствует)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face angry blush false", text="(Летние простуды - худшие, если ты их получишь!)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face angry blush false", text="(Они отстой!)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face angry blush false", text="...{p}...")

    call fade_to_black (0.5)
    show simone_vaginal_anim as bg
    with Dissolve(1.0)
    pause 1.0

    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (n, appearance="blush false", text="Мама! Мама!")
    call process_character (si, appearance="blush false", text="Тише, милый.")
    call process_character (si, appearance="blush false", text="Постарайся быть потише.")
    call process_character (si, appearance="blush false", text="Мы должны держать это в секрете, помнишь?")
    call process_character (sa, appearance="blush false", text="!!!")
    call process_character (n, appearance="blush false", text="Прости, Мам...")
    call process_character (n, appearance="blush false", text="Я постараюсь быть потише.")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="У тебя здорово получается, [n.say_name].")
    call process_character (si, appearance="blush false", text="Оох, да...")
    call process_character (n, appearance="blush false", text="Мы можем сделать это завтра?")
    call process_character (si, appearance="blush false", text="Мы уже делали это каждую ночь на этой неделе, милый!")
    call process_character (si, appearance="blush false", text="Ммм!")
    call process_character (si, appearance="blush false", text="Но...{w=1.0} у меня нет возражений...")
    call process_character (sa, appearance="blush false", text="...{p}...")
    call process_character (sa, appearance="blush false", text="([n.say_name]...)")
    call process_character (sa, appearance="blush false", text="(Он делает то же самое с мамой, что и со мной...)")
    call process_character (sa, appearance="blush false", text="...{p}...")
    call process_character (sa, appearance="blush false", text="(Похоже, ему очень весело)")
    call process_character (sa, appearance="blush false", text="...")

    window hide
    show bg black
    with Dissolve(0.5)
    call process_new_location ("bg sam_room_evening", dream=dream)

    call process_character (sa, appearance="outfit underwear pose handsbehind face concerned blush false", text="...{p}...")
    call process_character (sa, appearance="outfit underwear pose handface face concerned blush false", text="(Мама попросила [n.say_name] сделать это?)")
    call process_character (sa, appearance="outfit underwear pose handface face concerned blush false", text="(Или [n.say_name] рассказал маме о том, что мы делали?)")
    call process_character (sa, appearance="outfit underwear pose handface face concerned blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handsbehind face concerned blush false", text="(Почему я не знала об этом, [n.say_name]?)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face concerned blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="(Хотя я слышала, что мама сказала...)")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="(Она хотела сохранить это в тайне...)")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="...{p}...")
    call process_character (sa, appearance="outfit underwear pose handface face neutral blush false", text="(Конечно!)")
    call process_character (sa, appearance="outfit underwear pose handface face neutral blush false", text="(Теперь все это имеет смысл!)")
    call process_character (sa, appearance="outfit underwear pose handface face neutral blush false", text="(Мама сказала [n.say_name], чтобы держать это в секрете все время!)")
    call process_character (sa, appearance="outfit underwear pose leaning face happy blush false", text="(В противном случае, [n.say_name] сказал бы мне все об этом!)")
    call process_character (sa, appearance="outfit underwear pose leaning face happy blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="(Но почему мама не хочет, чтобы я знала об этом?)")
    call process_character (sa, appearance="outfit underwear pose handface face concerned blush false", text="(Может [n.say_name] попадёт в беду, если он скажет мне?)")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="(Есть ли что-то особенное в том, как она делает это с [n.say_name]?)")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="Хм...")
    call process_character (sa, appearance="outfit underwear pose handface face curious blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handface face angry blush false", text="(Черт возьми! Так много вопросов без ответов!)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face angry blush false", text="(Я ни за что не смогу спать, думая обо всем этом!)")
    call process_character (sa, appearance="outfit underwear pose handsbehind face curious blush false", text="(Этот марафонский завтрашний стрим придется отложить...)")

    call process_new_location ("bg nate_room_daytime", dream=dream)

    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="{i}Зевок.{/i}..")
    call process_character (n, appearance="outfit underwear pose handfist face neutral blush false", text="(Я прекрасно спал прошлой ночью!)")
    call process_character (n, appearance="outfit underwear pose handfist face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="(После того, как сделал все это с мамой...)")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="(У меня не было проблем со сном!)")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear pose twohandfist face happy blush false", text="(Точно!)")
    call process_character (n, appearance="outfit underwear pose twohandfist face happy blush false", text="(Марафонский стрим скоро начнется!)")
    call process_character (n, appearance="outfit underwear pose twohandfist face happy blush false", text="([sa.say_name] должно быть всё подготовила...)")

    call process_new_location ("bg sam_room_daytime", dream=dream)
    $ display_multiple_characters([ (n, "outfit clothesjacket pose handfist face neutral blush false"), (sa, "outfit clothes pose handface face neutral blush false") ])

    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Хорошо, я готов к марафону [sa.say_name]!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Я так ждала, когда ты встанешь!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Стрим еще не начался?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Вообще-то да...")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Стрима не будет сегодня.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Почему?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="ReflexViz.HD сайт не работает?")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Нет, дело не в этом.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Кое-что важное всплыло, и мне пришлось отменить это.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Ты не кажешься слишком расстроенной из-за необходимости отменить стрим...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Что в этом такого важного?")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Я узнала об одном секрете.")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Супер секрете!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Супер-секрет?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Это секрет между тобой и мамой...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...{p}...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Ты хорошо знаешь этот секрет!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Тот, про который мама сказала, чтобы никто не узнал?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face embarrassed blush true", text="!!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face embarrassed blush true", text="{i}Глык.{/i}..")
    call process_character (sa, appearance="pose handface face happy blush false", text="Ага, ты покраснел!")
    call process_character (sa, appearance="pose handface face happy blush false", text="Ты знаешь, о чем я говорю!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face embarrassed blush true", text="Так ты знаешь, чем мы с мамой занимались все это время?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Я искала тебя прошлой ночью.")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Тебя не было в комнате, поэтому я обошла весь дом...")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="А потом я услышала твой голос из маминой спальни.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush true", text="...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Я заглянула в дверь и увидела тебя на кровати, трахающим Маму!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush true", text="...{p}...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush true", text="Что ты собираешься делать теперь, когда ты знаешь?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Не волнуйся!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Твой секрет в безопасности, [n.say_name]!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face embarrassed blush false", text="{i}Фух.{/i}.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Но теперь, когда я это знаю...")
    call process_character (sa, appearance="pose handface face happy blush false", text="Я хочу тоже!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Хочешь?")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Я хочу быть частью этого!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Разве это не было бы удивительно, если бы ты, я и мама были вместе?!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Что… {w=1.0}звучит действительно потрясающе...")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Так что давай сделаем это!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Но… {w=1.0}как?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Как что?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Как мы заставим маму быть частью этого?")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Должно быть проще простого!")
    call process_character (sa, appearance="pose handface face happy blush false", text="Просто заставь маму снова заняться с тобой сексом, а я позабочусь об остальном!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Если ты так говоришь...")

    call process_new_location ("bg kitchen_daytime", dream=dream)

    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="...{p}...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Доброе утро, Мама!")
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Ты бодр и свеж!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Да...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="[sa.say_name] и я собирались сделать очень длинный стрим, но мы отменили.")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Я думаю, это было хорошее решение.")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Посмотри, как ясно и светло на улице сегодня!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="{i}Нюх-Нюх{/i}...")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Очень вкусно пахнет!")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Это сырный омлет, я приготовила остатки картошки и добавила их в него.")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="{i}Задыхается!{/i}")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Можно мне немного, пожалуйста?")
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Помоги себе сам!")

    call fade_to_black (1)
    call process_new_location ("bg kitchen_daytime", dream=dream)
    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (si, "outfit clothes pose handsfront face neutral blush false") ])

    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Ну и как?")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Это было восхитительно, Мама!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Мне очень понравилось, как он был заполнен кусками мягкой картошки!")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Я знала, что тебе понравится!")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Это довольно сытный завтрак.")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="...")
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Так что ты собираешься делать сегодня вместо стрима?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Ну я хотел спросить...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Мы могли бы повеселиться сегодня снова.")
    call process_character (si, appearance="outfit clothes pose armunder face curious blush false", text="Так рано утром, дорогой?")
    call process_character (si, appearance="outfit clothes pose armunder face curious blush false", text="Ты не хочешь сделать это позже?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Ну, мы могли бы...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Но я буду думать об этом весь день, пока мы не сделаем это.")
    call process_character (si, appearance="outfit clothes pose handsfront face happy blush false", text="Я надеюсь, ты не вырастешь избалованным, делая это так много!")
    call process_character (si, appearance="outfit clothes pose handsfront face flirt blush false", text="(Я знаю, что чувствую себя избалованным этим...)")
    call process_character (si, appearance="outfit clothes pose handsfront face flirt blush false", text="...")
    call process_character (si, appearance="outfit clothes pose handsup face flirt blush false", text="Хорошо, [n.say_name], мы можем.")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Да!")

    $ clear_characters()
    with Dissolve(0.5)
    pause 1.0

    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="([n.say_name] собирается в спальню мамы)")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="(Отлично!)")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="(Я не могу дождаться этого...)")
    call process_character (sa, appearance="pose handface face curious blush false", text="Нюх-Нюх...")
    call process_character (sa, appearance="pose handface face curious blush false", text="(Это...)")
    call process_character (sa, appearance="pose handface face neutral blush false", text="(Оох-хохо!)")
    call process_character (sa, appearance="pose handface face neutral blush false", text="(Это омлет с сыром и картофелем?!)")
    call process_character (sa, appearance="pose handface face happy blush false", text="(Хвать!)")

    call process_new_location ("bg simone_room_daytime", dream=dream)
    $ display_multiple_characters([ (n, "outfit nudehard pose handsdown face neutral blush false"), (si, "outfit nude pose armunder face neutral blush false") ])

    call process_character (si, appearance="outfit nude pose armunder face neutral blush false", text="Я не думаю, что я когда-либо трахалась так рано утром!")
    call process_character (n, appearance="outfit nudehard pose twohandfist face neutral blush false", text="Я тоже!")
    call process_character (si, appearance="outfit nude pose armunder face happy blush false", text="Это новый опыт для нас обоих!")
    call process_character (si, appearance="outfit nude pose armunder face happy blush false", text="...")
    call process_character (si, appearance="outfit nude pose handsfront face neutral blush false", text="Что-то конкретное хочешь, милый?")
    call process_character (n, appearance="outfit nudehard pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit nudehard pose handsdown face aroused blush false", text="...")

    $ clear_characters()
    with Dissolve(0.5)
    $ n.position = "nate_simone_tit_level_nate"
    $ si.position = "nate_simone_tit_level_simone"
    pause 0.25
    $ refresh_character(n, force_no_dissolve = True)
    $ refresh_character(si, force_no_dissolve = True)
    with Dissolve(0.5)
    pause 0.5

    if "simone_scene_titfuck" in scenes_completed:
        call process_character (si, appearance="pose handsfront face flirt blush false", text="А, понятно...")
        call process_character (si, appearance="pose armunder face flirt blush true", text="Ты снова хочешь пососать мою грудь?")
        call process_character (si, appearance="pose armunder face flirt blush true", text="Я знаю, что раньше тебе это очень нравилось.")
        call process_character (n, appearance="pose twohandfist face aroused blush true", text="...")
        call process_character (n, appearance="pose twohandfist face aroused blush true", text="Я снова хочу их пососать, Мама.")
        call process_character (si, appearance="pose armunder face flirt blush true", text="Хочешь, чтобы я тоже положила свою грудь на твой пенис?")
        call process_character (n, appearance="pose handfist face aroused blush true", text="Да...")
        call process_character (n, appearance="pose handfist face aroused blush true", text="Это лучшее, что ты делаешь, Мама!")
    else:
        call process_character (si, appearance="pose handsfront face flirt blush false", text="А, понятно...")
        call process_character (si, appearance="pose handsfront face flirt blush false", text="...")
        call process_character (si, appearance="pose armunder face flirt blush false", text="Ты действительно любишь мамину грудь, не так ли?")
        call process_character (n, appearance="pose handsdown face aroused blush true", text="...")
        call process_character (si, appearance="pose armunder face flirt blush true", text="Ты хочешь поиграть с ними?")
        call process_character (n, appearance="pose twohandfist face aroused blush true", text="...")
        call process_character (n, appearance="pose twohandfist face aroused blush true", text="Я...я хочу пососать их.")
        call process_character (n, appearance="pose twohandfist face aroused blush true", text="Я хочу сосать их, так что ты почувствуешь себя хорошо, Мама!")
        call process_character (si, appearance="pose armunder face flirt blush true", text="Я думаю, что ты отлично справишься с этим, [n.say_name]...")

    call static_still_ctc ("bg sam_simone_group_nate_suck")

    call process_character (n, appearance="blush false", text="Ммм...")
    call process_character (si, appearance="blush false", text="Ох...")
    call process_character (si, appearance="blush false", text="{i}Задыхается!{/i}")
    call process_character (si, appearance="blush false", text="Оох, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Тебе нравится, мама?")
    call process_character (si, appearance="blush false", text="Ты заставляешь маму возбудиться!")
    call process_character (si, appearance="blush false", text="(Мои соски не потеряли чувствительность!)")
    call process_character (si, appearance="blush false", text="([n.say_name] так хорошо использует свой язык!)")
    call process_character (si, appearance="blush false", text="(И он нежно сжимает мою грудь!)")
    call process_character (si, appearance="blush false", text="(Я могу испытать оргазм, если он продолжит...)")
    call process_character (sa, appearance="blush false", text="Вау, это выглядит потрясающе, [n.say_name]!")
    call process_character (si, appearance="blush false", text="!!!")

    call process_new_location ("bg simone_room_daytime", dream=dream)
    $ si.position = "left"
    $ n.position = "right"
    $ sa.position = "right"
    $ display_multiple_characters([ (sa, "outfit clothes pose handsbehind face neutral blush false"), (si, "outfit nude pose handsup face surprise blush false") ])

    call process_character (si, appearance="outfit naked pose handsup face surprise blush false", text="[sa.say_name]!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Привет, Мам!")
    call process_character (si, appearance="outfit naked pose handsup face surprise blush false", text="...{p}...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="[n.say_name] собирается сосать твои сиськи снова, мама?")
    call process_character (si, appearance="outfit naked pose armunder face embarrassed blush false", text="...{p}...")
    call process_character (si, appearance="outfit naked pose armunder face embarrassed blush false", text="(Что я могу сказать по этому поводу?!)")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Хаха, [n.say_name] твой член очень твёрд!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ты собираешься трахаться?")
    call process_character (si, appearance="outfit naked pose handsup face surprise blush false", text="[sa.say_name]!")
    call process_character (si, appearance="outfit naked pose armunder face surprise blush false", text="Это плохие слова!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Но разве это не правильный термин для того, что вы делаете с [n.say_name]?")
    call process_character (si, appearance="outfit naked pose handsfront face embarrassed blush false", text="...{p}...")
    call process_character (si, appearance="outfit naked pose handsfront face embarrassed blush false", text="Что ты имеешь в виду?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Знаешь...")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Например, когда вы лежите на кровати, и [n.say_name] вставляет свой член в киску!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Разве это не трахание?")
    call process_character (si, appearance="outfit naked pose handsup face surprise blush false", text="!!")
    call process_character (si, appearance="outfit naked pose handsup face surprise blush false", text="(Она должно быть услышала [n.say_name] прошлой ночью!)")
    call process_character (si, appearance="outfit naked pose handsup face surprise blush false", text="(Я знала, что он был слишком громким!)")
    call process_character (si, appearance="outfit naked pose handsup face surprise blush false", text="...")
    call process_character (si, appearance="outfit naked pose handsup face embarrassed blush false", text="(Но откуда она знает о том, что мы делаем?)")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Когда я делаю это, мне нравится говорить \"продолжай трахать меня!\"")
    call process_character (si, appearance="outfit naked pose armunder face surprise blush false", text="Когда ты это делаешь?!")
    call process_character (si, appearance="outfit naked pose armunder face surprise blush false", text="[sa.say_name]!")
    call process_character (si, appearance="outfit naked pose armunder face surprise blush false", text="У тебя был секс?!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Да!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Я постоянно этим занимаюсь!")
    call process_character (si, appearance="outfit naked pose handsup face surprise blush false", text="С каких пор?!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="С самого начала лета.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="[n.say_name] знает об этом.")
    call process_character (si, appearance="outfit naked pose handsup face surprise blush false", text="Ты?!")

    call character_leave_dissolve (sa)
    pause 0.25

    call process_character (n, appearance="outfit nudesoft pose behindhead face concerned blush false", text="...")

    call process_character (si, appearance="outfit naked pose armunder face angry blush false", text="Ты должен был сказать мне об этом сразу, [n.say_name]!")
    call process_character (si, appearance="outfit naked pose armunder face angry blush false", text="Какой-то извращенец занимается сексом с твоей сестрой, а ты мне не сказал?!")

    call character_leave_dissolve (n)
    pause 0.25

    call process_character (sa, appearance="pose handface face neutral blush false", text="О ничего такого, Мама!")
    call process_character (sa, appearance="pose handface face happy blush false", text="Я знаю этого человека целую вечность!")
    call process_character (si, appearance="outfit naked pose handsfront face embarrassed blush false", text="...{p}...")
    call process_character (si, appearance="outfit naked pose handsfront face embarrassed blush false", text="Что?")
    call process_character (si, appearance="outfit naked pose handsfront face embarrassed blush false", text="Что ты имеешь в виду?")
    call process_character (si, appearance="outfit naked pose handsfront face embarrassed blush false", text="[n.say_name], о чем она говорит?")

    call character_leave_dissolve (sa)
    pause 0.25

    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="...{p}...")
    call process_character (si, appearance="outfit naked pose handsup face surprise blush false", text="Даю слово...")
    call process_character (si, appearance="outfit naked pose handsup face surprise blush false", text="...")
    call process_character (si, appearance="outfit naked pose handsup face surprise blush false", text="Не говори мне...")
    call process_character (n, appearance="outfit nudesoft pose handsdown face curious blush false", text="...")

    call character_leave_dissolve (n)
    pause 0.25

    call process_character (sa, appearance="pose leaning face happy blush false", text="[n.say_name] - это тот человек, который трахает меня!")
    call process_character (si, appearance="outfit naked pose handsfront face embarrassed blush false", text="...{p}...")
    call process_character (si, appearance="outfit naked pose handsfront face embarrassed blush false", text="[n.say_name]...")
    call process_character (si, appearance="outfit naked pose handsfront face embarrassed blush false", text="Это правда?")

    call character_leave_dissolve (sa)
    pause 0.25

    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Д-Да, это действительно так.")
    call process_character (si, appearance="outfit naked pose armunder face embarrassed blush false", text="...{p}...")
    call process_character (n, appearance="outfit nudesoft pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose behindhead face concerned blush false", text="Мама, ты в порядке?")

    call character_leave_dissolve (n)
    pause 0.25

    call process_character (sa, appearance="pose handface face concerned blush false", text="...")
    call process_character (sa, appearance="pose handface face concerned blush false", text="(Я думала, что мама будет счастлива по этому поводу...)")
    call process_character (sa, appearance="pose handface face concerned blush false", text="...")

    if "kira_simone_threesome_scene" in scenes_completed:
        call process_character (si, appearance="pose armunder face embarrassed blush false", text="...")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="(Я должна была подумать, что это произойдет)")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="([n.say_name] уже узнавал все больше и больше о сексе от [k.say_name])")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="(И тогда я решила научить его большему...)")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="...")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="(Это был только вопрос времени, прежде чем он и [sa.say_name] будут...)")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="...")
        call process_character (si, appearance="pose armunder face embarrassed blush false", text="(Я бы никогда не подумала, что [sa.say_name] занимается этим)")
        call process_character (si, appearance="pose armunder face embarrassed blush false", text="(Она все еще выглядит так невинно...)")
    else:
        call process_character (si, appearance="pose armunder face embarrassed blush false", text="...")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="(Я должна была понять, что это произойдет)")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="(Заинтересованность в сексе у [n.say_name] только растет)")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="(И я способствовала этому...)")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="...")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="(Это был только вопрос времени, прежде чем он и [sa.say_name] будут...)")
        call process_character (si, appearance="pose handsfront face concerned blush false", text="...")
        call process_character (si, appearance="pose armunder face embarrassed blush false", text="(Я бы никогда не подумала, что [sa.say_name] занимается этим)")
        call process_character (si, appearance="pose armunder face embarrassed blush false", text="(Она все еще выглядит так невинно...)")

    call character_leave_dissolve (sa)
    pause 0.25

    call process_character (n, appearance="pose handsdown face concerned blush false", text="...")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="(Я никогда не видела маму такой тихой...)")

    call character_leave_dissolve (n)
    pause 0.25

    call process_character (sa, appearance="pose handface face concerned blush false", text="М-Мам?")
    call process_character (sa, appearance="pose handface face concerned blush false", text="Это… {w=1.0}неправильно, что я и [n.say_name] делаем?")
    call process_character (si, appearance="pose handsfront face curious blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face concerned blush false", text="Нам это очень нравилось.")
    call process_character (sa, appearance="pose handsbehind face concerned blush false", text="Это здорово, когда мы это делаем...")
    call process_character (si, appearance="pose handsfront face concerned blush false", text="...")
    call process_character (sa, appearance="pose handsbehind face concerned blush false", text="...{p}...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ты всегда говоришь нам, что мы должны делать вещи, которые заставляют нас чувствовать себя хорошо.")

    call character_leave_dissolve (sa)
    pause 0.25

    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Да!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="[sa.say_name] и я люблю проводить время вместе!")

    call character_leave_dissolve (n)
    pause 0.25

    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="[n.say_name] и я чувствую себя ближе, чем когда-либо до этого, Мама!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Мы думали, что секс показал, как сильно мы заботимся друг о друге...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="...{p}...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Вы правы.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Я не думала об этом раньше...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Я нахожу это чудесным, что вы так близки друг к другу.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="И вы нашли способ еще больше углубить эту связь.")

    call character_leave_dissolve (sa)
    pause 0.25

    call process_character (n, appearance="pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Эй, Мам...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="[sa.say_name] и мне было интересно...")

    call character_leave_dissolve (n)
    pause 0.25

    call process_character (sa, appearance="pose handface face neutral blush false", text="Мы можем быть вместе ради секса?")

    call character_leave_dissolve (sa)
    pause 0.25

    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Мы очень хотим, чтобы ты была с нами, Мама!")
    call process_character (si, appearance="pose armunder face neutral blush false", text="...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Я думаю...")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Resort Loop2.ogg", fadeout=1.0, fadein = 1.0)

    call process_character (si, appearance="pose armunder face flirt blush false", text="Это замечательная идея.")

    call character_leave_dissolve (n)
    pause 0.25

    call process_character (sa, appearance="pose leaning face happy blush false", text="Ура, Мама!")

    call character_leave_dissolve (sa)
    pause 0.25

    call process_character (n, appearance="pose handfist face happy blush false", text="Мама, ты просто потрясающая!")
    call process_character (si, appearance="pose handsup face happy blush false", text="Вы оба очень взволнованы этим!")
    call process_character (si, appearance="pose handsup face happy blush false", text="Это так мило!")
    call process_character (si, appearance="pose handsup face happy blush false", text="...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Поэтому мне стало любопытно...")
    call process_character (si, appearance="pose armunder face flirt blush false", text="Что бы вы хотели сделать в первую очередь?")

    call character_leave_dissolve (n)
    pause 0.25

    call process_character (sa, appearance="outfit nude pose handface face neutral blush false", text="Я знаю, как мы можем начать!")
    call process_character (sa, appearance="outfit nude pose handface face neutral blush false", text="[n.say_name]!")
    call process_character (sa, appearance="outfit nude pose handface face happy blush false", text="Пососи мамину грудь еще раз!")


    call static_still_ctc ("bg sam_simone_group_nate_suck")

    call process_character (n, appearance="blush false", text="Ммф!")
    call process_character (si, appearance="blush false", text="Аахх!")
    call process_character (si, appearance="blush false", text="Ты сосешь сильнее, [n.say_name]!")
    call process_character (si, appearance="blush false", text="Это потому, что ты так взволнован по поводу присоединения [sa.say_name]?")

    menu:
        "Смотри как я могу сосать Маму, [sa.say_name]!":
            call process_character (sa, appearance="blush false", text="Дай мне взглянуть...")
            call process_character (sa, appearance="blush false", text="...")
            call process_character (sa, appearance="blush false", text="Ух ты!")
            call process_character (sa, appearance="blush false", text="Так тебе нравится это чувство мама, когда [n.say_name] делает так?")
            call process_character (si, appearance="blush false", text="Да, милая.")
            call process_character (si, appearance="blush false", text="Очень.")
            call process_character (sa, appearance="blush false", text="Я должна запомнить, чтобы позволить тебе попробовать это на мне, [n.say_name].")
            call process_character (sa, appearance="blush false", text="Хотя моя грудь намного меньше, чем у мамы...")
            call process_character (si, appearance="blush false", text="Все в порядке, [sa.say_name].")
            call process_character (si, appearance="blush false", text="Если [n.say_name] будет сосать и лизать соски, ты будешь чувствовать то же удовольствие, что и я.")
            call process_character (si, appearance="blush false", text="Ах!")
            call process_character (sa, appearance="blush false", text="Ооох!")
            call process_character (sa, appearance="blush false", text="То насколько это хорошо, не имеет ничего общего с размером сисек?")
            call process_character (si, appearance="blush false", text="Вот именно.")
            call process_character (si, appearance="blush false", text="Ху! Мм!")
        "Попробуй это, [sa.say_name]!":
            $ did_sam_simone_ff = True
            call process_character (sa, appearance="blush false", text="О, я собираюсь кончить!")

            call static_still_ctc ("bg sam_simone_group_nate_sam_suck")

            call process_character (si, appearance="blush false", text="{i}Задыхается!{/i}")
            call process_character (sa, appearance="blush false", text="Ух ты!")
            call process_character (sa, appearance="blush false", text="[n.say_name], неудивительно, почему ты хотел это сделать!")
            call process_character (sa, appearance="blush false", text="Мамина грудь такая вкусная!")
            call process_character (sa, appearance="blush false", text="У неё немного сладковатый вкус...")
            call process_character (si, appearance="blush false", text="Ммм!")
            call process_character (si, appearance="blush false", text="(Последний раз, когда [n.say_name] и [sa.say_name] сосали мою грудь, они делали это, чтобы получить молоко...)")
            call process_character (si, appearance="blush false", text="(Теперь те же самые рты ублажают меня!)")
            call process_character (sa, appearance="blush false", text="Я всегда думала о маминых сиськах и о том, какие они были большие.")
            call process_character (sa, appearance="blush false", text="Я представляла, как сильно их сжимаю!")
            call process_character (sa, appearance="blush false", text="Как насчет тебя, [n.say_name]?")
            call process_character (n, appearance="blush false", text="Ммм...")
            call process_character (si, appearance="blush false", text="[n.say_name] регулярно мастурбирует на мою грудь.")
            call process_character (si, appearance="blush false", text="Он сказал мне, как сильно он их любит.")
            call process_character (sa, appearance="blush false", text="Так вот о чем он думает, когда сам играет со своим членом!")
            call process_character (sa, appearance="blush false", text="Ха-ха, теперь всё имеет смысл!")
            call process_character (si, appearance="blush false", text="Я случайно вошла к [n.say_name], когда он мастурбировал в первый раз.")
            call process_character (si, appearance="blush false", text="Ху! Мм!")
            call process_character (sa, appearance="blush false", text="Я бы с удовольствием посмотрела на ваши лица, когда это произошло!")
            call process_character (n, appearance="blush false", text="...")

    call process_character (sa, appearance="blush false", text="Мама! Мама!")
    call process_character (sa, appearance="blush false", text="Я думаю, ты должна попробовать что-то с [n.say_name]!")
    call process_character (si, appearance="blush false", text="Что я должна попробовать?")
    call process_character (sa, appearance="blush false", text="Что если ... ..")
    call process_character (sa, appearance="blush false", text="Ты положишь свои сиськи на пенис [n.say_name]!")

    if "simone_scene_titfuck" in scenes_completed:
        call process_character (n, appearance="blush false", text="Мм...")
        call process_character (si, appearance="blush false", text="[n.say_name] очень нравилось это раньше.")
        call process_character (sa, appearance="blush false", text="О, я хочу это увидеть, я хочу это увидеть!")
        call process_character (si, appearance="blush false", text="Твоя сестра, кажется, очень рада видеть, как я это делаю, [n.say_name].")
        call process_character (si, appearance="blush false", text="Ты хочешь, чтобы я потерла свои сиськи о твой член?")
        call process_character (n, appearance="blush false", text="Д-Да!")
        call process_character (si, appearance="blush false", text="[n.say_name] должен лежать на кровати для этого, [sa.say_name].")
        call process_character (sa, appearance="blush false", text="Я принесу подушки!")
    else:
        call process_character (n, appearance="blush false", text="Хм?!")
        call process_character (si, appearance="blush false", text="Ты знаешь, [n.say_name] на самом деле никогда не имел пенис между моими сиськами?")
        call process_character (sa, appearance="blush false", text="Ты не делала этого с [n.say_name]?!")
        call process_character (sa, appearance="blush false", text="Давай изменим это прямо сейчас!")
        call process_character (si, appearance="blush false", text="Твоя сестра, кажется, очень рада видеть, как я это делаю, [n.say_name].")
        call process_character (si, appearance="blush false", text="Ты хочешь, чтобы я потерла свои сиськи о твой член?")
        call process_character (n, appearance="blush false", text="Д-Да!")
        call process_character (si, appearance="blush false", text="[n.say_name] должен лежать на кровати для этого, [sa.say_name].")
        call process_character (sa, appearance="blush false", text="Я принесу подушки!")

    call fade_to_black (1)

    call process_character (sa, appearance="blush false", text="Не могу дождаться, чтобы увидеть это!")
    call process_character (si, appearance="blush false", text="Ложись прямо здесь, [n.say_name]...")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (si, appearance="blush false", text="Удобно?")
    call process_character (sa, appearance="blush false", text="Ему достаточно комфортно!")
    call process_character (sa, appearance="blush false", text="Положи свои сиськи ему на член!")
    call process_character (si, appearance="blush false", text="Ты готова милая?")

    call static_still_ctc ("bg sam_simone_group_titfuck_sam_watches")

    call process_character (n, appearance="blush false", text="Аах!")
    call process_character (sa, appearance="blush false", text="Посмотри на лицо [n.say_name], хаха!")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}Вздох.{/i}.")
    call process_character (si, appearance="blush false", text="Я уверена, что ты тоже корчишь рожи, когда чувствуешь себя хорошо, [sa.say_name].")
    call process_character (sa, appearance="blush false", text="Я уверена, что да...")
    call process_character (sa, appearance="blush false", text="Но у [n.say_name] самые смешные и лучшие!")
    call process_character (n, appearance="blush false", text="...")

    if stats.stat_value('times_had_paizuri') > 0:
        call process_character (n, appearance="blush false", text="(Мамины сиськи такие мягкие!)")
        call process_character (n, appearance="blush false", text="(Они, безусловно, самые мягкие, которые я чувствовал!)")
        call process_character (n, appearance="blush false", text="(Я думаю, что сиськи мамы могут быть лучшими в мире!)")
    else:
        call process_character (n, appearance="blush false", text="(Мамины сиськи так хлюпают!)")
        call process_character (n, appearance="blush false", text="(И они супер мягкие!)")
        call process_character (n, appearance="blush false", text="(Мой пенис обернут в них!)")
        call process_character (n, appearance="blush false", text="(Сиськи мамы - это все, на что я надеялся!)")

    call process_character (sa, appearance="blush false", text="Это так весело делать мама!")
    call process_character (sa, appearance="blush false", text="Я надеюсь, что у меня вырастут такие же массивные сиськи!")
    call process_character (si, appearance="blush false", text="Ха-ха, будь осторожна в своих желаниях...")
    call process_character (si, appearance="blush false", text="Они не совсем легкие!")
    call process_character (si, appearance="blush false", text="Что если ты не вырастешь высокой, и у тебя будет грудь размером с мою?")
    call process_character (sa, appearance="blush false", text="Хм...")
    call process_character (sa, appearance="blush false", text="Ну...{w=0.5} ладно, возможно, немного меньше...")
    call process_character (sa, appearance="blush false", text="Но я хочу, чтобы они были достаточно большими, чтобы [n.say_name] смог просунуть его пенис между моими сиськами тоже!")
    call process_character (n, appearance="blush false", text="Ха, Ахх!")
    call process_character (si, appearance="blush false", text="Мне любопытно, [sa.say_name]...")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="[n.say_name] когда-либо делал куннилингус тебе раньше?")

    "[n.say_name] & [sa.say_name]" "Куни-что?"
    call process_character (si, appearance="blush false", text="О, значит он тебе этого не делал!")
    call process_character (sa, appearance="blush false", text="Это ещё одно безумное слово!")
    call process_character (n, appearance="blush false", text="Что это значит, мама?")
    call process_character (si, appearance="blush false", text="Это означает, что ты будешь заниматься оральным сексом с [sa.say_name].")
    call process_character (si, appearance="blush false", text="Другими словами, ты будешь лизать ее киску..")
    call process_character (sa, appearance="blush false", text="{i}Задыхается!{/i}")
    call process_character (sa, appearance="blush false", text="Ты имеешь в виду минет для девушки?!")
    call process_character (si, appearance="blush false", text="Хаха, ну это не совсем то же самое...")
    call process_character (sa, appearance="blush false", text="[n.say_name]!")
    call process_character (sa, appearance="blush false", text="Я прошу тебя сделать кунни...")
    call process_character (sa, appearance="blush false", text="Каннил...")
    call process_character (sa, appearance="blush false", text="Ах, забыла это слово!")
    call process_character (sa, appearance="blush false", text="Ты можешь вылизать мою киску, [n.say_name]?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Твоя сестра была бы благодарна тебе за это, милый.")
    call process_character (si, appearance="blush false", text="Я знаю, что ты сможешь возбудить ее!")
    call process_character (sa, appearance="blush false", text="Да, да!")
    call process_character (sa, appearance="blush false", text="Как насчет этого, [n.say_name]?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Хорошо, я могу это сделать!")
    call process_character (n, appearance="blush false", text="Но ты все еще можешь тереться сиськами о мой член, Мама?")
    call process_character (si, appearance="blush false", text="Нет проблем, милый!")
    call process_character (sa, appearance="blush false", text="Как [n.say_name] сможет лизать мою киску?")
    call process_character (si, appearance="blush false", text="Я прошепчу тебе, [sa.say_name].")
    call process_character (sa, appearance="blush false", text="...{p}...")
    call process_character (sa, appearance="blush false", text="А? Нет!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (sa, appearance="blush false", text="Хорошо [n.say_name]!")
    call process_character (sa, appearance="blush false", text="Готов или нет, но вот я иду!")

    call static_still_ctc ("bg sam_simone_group_titfuck_sam_licked")

    call process_character (n, appearance="blush false", text="Ммф...")
    call process_character (n, appearance="blush false", text="Ммм...")
    call process_character (sa, appearance="blush false", text="{i}Задыхается.{/i}.")
    call process_character (sa, appearance="blush false", text="Ах, ах...")
    call process_character (si, appearance="blush false", text="Ну как, [sa.say_name]?")
    call process_character (sa, appearance="blush false", text="О-Ох…")
    call process_character (sa, appearance="blush false", text="Язык [n.say_name] идет вверх и вниз по моей киске.")
    call process_character (sa, appearance="blush false", text="Ан!")
    call process_character (sa, appearance="blush false", text="И он засовывает его внутрь!")
    call process_character (si, appearance="blush false", text="Похоже, вам обоим это очень нравится!")
    call process_character (n, appearance="blush false", text="...")

    if stats.stat_value('times_given_cunnilingus') > 0:
        call process_character (n, appearance="blush false", text="(Я никогда не слышал этого слова, которое мама сказала раньше...)")
        call process_character (n, appearance="blush false", text="(Но по крайней мере теперь я знаю, что это значит!)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Мне нравится чувствовать киску [sa.say_name])")
        call process_character (n, appearance="blush false", text="(Моему языку очень тепло...)")
    else:
        call process_character (n, appearance="blush false", text="(Я никогда раньше не лизал киску!)")
        call process_character (n, appearance="blush false", text="(Я всегда задавался вопросом, должен ли я попробовать...)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Очень мокро на моем языке)")
        call process_character (n, appearance="blush false", text="(И супер тепло)")
        call process_character (n, appearance="blush false", text="(Я даже не знаю, правильно ли я это делаю...)")
        call process_character (n, appearance="blush false", text="(Но [sa.say_name] сказала, что ей нравится!)")

    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="(Они так сосредоточены на сексе...)")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="([n.say_name] и [sa.say_name] - мои сын и дочь)")
    call process_character (sa, appearance="blush false", text="[n.say_name[0]]-[n.say_name]...")
    call process_character (sa, appearance="blush false", text="Ах...")
    call process_character (n, appearance="blush false", text="Ммм...")
    call process_character (si, appearance="blush false", text="Хочешь развернуться с членом своего брата?")
    call process_character (sa, appearance="blush false", text="Д-да, мама!")
    call process_character (si, appearance="blush false", text="Тогда закончи это.")
    call process_character (sa, appearance="blush false", text="Мне нравится моя поза.")
    call process_character (sa, appearance="blush false", text="Я буду сидеть на твоем члене, [n.say_name]!")

    call static_still_ctc ("bg sam_simone_group_titfuck_sam_rides")

    call process_character (si, appearance="blush false", text="Мм, да, дорогой...")
    call process_character (si, appearance="blush false", text="Играй с моей грудью сколько хочешь.")
    call process_character (sa, appearance="blush false", text="Ах, ах, ах!")
    call process_character (sa, appearance="blush false", text="Это позволяет меня подпрыгивать на твоём пенисе [n.say_name]!")
    call process_character (n, appearance="blush false", text="Мм! Мм!")
    call process_character (si, appearance="blush false", text="Ты делаешь большую работу, [sa.say_name]!")
    call process_character (si, appearance="blush false", text="[n.say_name] сжимает мою грудь каждый раз, когда ты прыгаешь на его члене.")
    call process_character (sa, appearance="blush false", text="Эта поза называется как-то, Мама?")
    call process_character (si, appearance="blush false", text="Это часто называют позой ковбойши.")
    call process_character (sa, appearance="blush false", text="Позой ковбойши?")
    call process_character (sa, appearance="blush false", text="Ахх...")
    call process_character (si, appearance="blush false", text="Да.")
    call process_character (si, appearance="blush false", text="Думаю, что [n.say_name] как седло на лошади, и ты едешь на нём.")
    call process_character (sa, appearance="blush false", text="Теперь я поняла!")
    call process_character (sa, appearance="blush false", text="Йииихааа [n.say_name]!")
    call process_character (n, appearance="blush false", text="Ммф!")
    call process_character (si, appearance="blush false", text="Ты полностью контролируешь ситуацию, делая это [sa.say_name].")
    call process_character (si, appearance="blush false", text="Ты контролируешь скорость и угол.")
    call process_character (sa, appearance="blush false", text="Зацени [n.say_name]!")
    call process_character (sa, appearance="blush false", text="Я могу ехать так быстро, как хочу!")
    call process_character (n, appearance="blush false", text="Ах, ах, ах!")
    call process_character (n, appearance="blush false", text="Мм, ахх!")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}.")
    call process_character (si, appearance="blush false", text="Будь осторожна, [sa.say_name].")
    call process_character (si, appearance="blush false", text="Если ты будешь ехать слишком быстро, то травмируешь [n.say_name].")
    call process_character (si, appearance="blush false", text="В конце концов, его пенис очень чувствителен.")
    call process_character (sa, appearance="blush false", text="Моя ошибка, Мама.")
    call process_character (sa, appearance="blush false", text="Обычно [n.say_name] выбирает двигаться быстрее или медленнее, когда трахаемся.")
    call process_character (sa, appearance="blush false", text="Я буду более осторожна, [n.say_name].")
    call process_character (n, appearance="blush false", text="Да всё нормально...")
    call process_character (n, appearance="blush false", text="Мне все еще нравится это.")
    call process_character (sa, appearance="blush false", text="Ах...")
    call process_character (sa, appearance="blush false", text="Почему бы тебе не попробовать эту позу, мама?")
    call process_character (sa, appearance="blush false", text="Это будет весело!")
    call process_character (si, appearance="blush false", text="Не думаю, что твоему брату будет весело.")
    call process_character (si, appearance="blush false", text="Бедный [n.say_name] будет хлюпать, как блин, если я сяду на него!")
    call process_character (si, appearance="blush false", text="У тебя правильный вес для ковбойши!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (sa, appearance="blush false", text="Хм...")
    call process_character (sa, appearance="blush false", text="Но тебе нужно трахаться с [n.say_name] тоже, Мама!")
    call process_character (sa, appearance="blush false", text="Твоя очередь!")
    call process_character (si, appearance="blush false", text="Это очень заботливо с твоей стороны, [sa.say_name].")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Я знаю способ, чтобы мы оба могли наслаждаться хером [n.say_name]...")
    call process_character (n, appearance="blush false", text="Да?")
    call process_character (sa, appearance="blush false", text="Расскажи нам, как Мама!")
    call process_character (si, appearance="blush false", text="Ложись рядом со мной, [sa.say_name].")
    call process_character (si, appearance="blush false", text="[n.say_name], ты иди к концу кровати...")

    call static_still_ctc ("bg sam_simone_group_sprawl")

    call process_character (si, appearance="blush false", text="Видишь, как мы это делаем?")
    call process_character (si, appearance="blush false", text="[n.say_name] может легко переключаться между нами.")
    call process_character (sa, appearance="blush false", text="Это отличная идея, мама!")
    call process_character (sa, appearance="blush false", text="Итак, хер [n.say_name] может быть в твоей киске минуту, а затем может переключиться на мою!")
    call process_character (n, appearance="blush false", text="В-Вау...")
    call process_character (si, appearance="blush false", text="Это зависит от тебя, милый.")
    call process_character (si, appearance="blush false", text="Ты хочешь трахнуть меня или свою сестру?")

    $ sam_simone_threesome_scene_current_partner = None

    menu:
        "Мама":
            $ sam_simone_threesome_scene_current_partner = si
            call process_character (n, appearance="blush false", text="Я хочу трахнуть тебя первой, Мама!")

            call static_still_ctc ("bg sam_simone_group_sprawl_fuck_simone")

            call process_character (n, appearance="blush false", text="Ннг!")
            call process_character (si, appearance="blush false", text="Молодец, малыш!")
            call process_character (si, appearance="blush false", text="{i}Задыхается!{/i}")
            call process_character (si, appearance="blush false", text="О да!")
            call process_character (sa, appearance="blush false", text="М-Мам...")
            call process_character (sa, appearance="blush false", text="Ты издаешь классные звуки, когда мы занимаемся сексом!")
        "[sa.say_name]":
            $ sam_simone_threesome_scene_current_partner = sa
            call process_character (n, appearance="blush false", text="Я хочу трахнуть тебя, [sa.say_name]!")
            call process_character (sa, appearance="blush false", text="Ты хочешь трахнуть меня?")
            call process_character (sa, appearance="blush false", text="Звучит хорошо!")

            call static_still_ctc ("bg sam_simone_group_sprawl_fuck_sam")

            call process_character (sa, appearance="blush false", text="Хьяа!")
            call process_character (sa, appearance="blush false", text="Ммм!")
            call process_character (si, appearance="blush false", text="У вас обоих есть много выносливости для этого!")

    call sam_simone_threesome_scene_phase_2 (dream=dream)

    return

screen sam_simone_threesome_scene_choose_partner(dream=False, revisit=False):
    vbox:
        xalign 0.02
        yalign 0.02
        spacing 30
        use main_menu_button(text="Мама", action=Function(sam_simone_threesome_scene_choose_simone, dream, revisit), enabled=sam_simone_threesome_scene_current_partner != si)
        use main_menu_button(text="[sa.say_name]", action=Function(sam_simone_threesome_scene_choose_sam, dream, revisit), enabled=sam_simone_threesome_scene_current_partner != sa)
        use main_menu_button(text="Продолжить", action=Function(sam_simone_threesome_scene_continue, dream, revisit))

label sam_simone_threesome_scene_choose_sam(dream=False, revisit=False):
    call static_still_ctc ("bg sam_simone_group_sprawl_fuck_sam")

    $ dice_roll = random.randint(1,4)

    if dice_roll == 1:
        call process_character (sa, appearance="blush false", text="Насколько отличается моя киска по сравнению с маминой?")
        call process_character (sa, appearance="blush false", text="Бьюсь об заклад, они обе потрясающие!")
    elif dice_roll == 2:
        call process_character (sa, appearance="blush false", text="Это правильно, [n.say_name]!")
        call process_character (sa, appearance="blush false", text="Мы все прекрасно себя чувствуем от этого!")
    elif dice_roll == 3:
        call process_character (sa, appearance="blush false", text="(Интересно, [n.say_name] будет стрелять спермой в одну из нас!)")
    else:
        call process_character (sa, appearance="blush false", text="Это должно стать нашим способом трахаться, когда мы сделаем это снова, мама!")

    if not revisit:
        call sam_simone_threesome_scene_phase_2 (dream=dream)
    return

label sam_simone_threesome_scene_choose_simone(dream=False, revisit=False):
    call static_still_ctc ("bg sam_simone_group_sprawl_fuck_simone")

    $ dice_roll = random.randint(1,4)

    if dice_roll == 1:
        call process_character (si, appearance="blush false", text="Ты знаешь, как раз подходящее время, чтобы переключиться, милая!")
    elif dice_roll == 2:
        call process_character (si, appearance="blush false", text="Эти простыни будут очень грязными после того, как мы закончим...")
    elif dice_roll == 3:
        call process_character (si, appearance="blush false", text="Тебе нравится, что мы обе доступны для тебя, не так ли, [n.say_name]?")
    else:
        call process_character (si, appearance="blush false", text="Трахни меня детка!")
        call process_character (si, appearance="blush false", text="Трахни меня и твою сестру!")


    if not revisit:
        call sam_simone_threesome_scene_phase_2 (dream=dream)
    return

label sam_simone_threesome_scene_phase_2(dream=False):
    window hide
    call screen sam_simone_threesome_scene_choose_partner(dream = dream, revisit = False)
    return

label sam_simone_threesome_scene_phase_3(dream=False):
    call process_character (n, appearance="blush false", text="Хррм!")
    call process_character (n, appearance="blush false", text="Ннг!")
    call process_character (si, appearance="blush false", text="[n.say_name] скоро будет эякулировать, [sa.say_name]...")
    call process_character (si, appearance="blush false", text="Он близок.")
    call process_character (sa, appearance="blush false", text="Итак, [n.say_name] кончит в одну из нас, Мама!")
    call process_character (si, appearance="blush false", text="Конечно.")
    call process_character (n, appearance="blush false", text="Я-я почти...")
    call process_character (sa, appearance="blush false", text="Так как насчет этого, [n.say_name]?")
    call process_character (sa, appearance="blush false", text="Какая киска наполнится твоими сливками?")
    call process_character (si, appearance="blush false", text="Ха-ха, ты называешь это сливками, милая?")
    call process_character (sa, appearance="blush false", text="Я называю сперму [n.say_name] многими вещами!")
    call process_character (si, appearance="blush false", text="Ну, [n.say_name]...")
    call process_character (si, appearance="blush false", text="[sa.say_name] с нетерпением ждет этого момента!")

    window hide
    menu:
        "Кончить в Маму":
            if sam_simone_threesome_scene_current_partner != si:
                call static_still_ctc ("bg sam_simone_group_sprawl_fuck_simone")
            call process_character (n, appearance="blush false", text="Хааа...")
            call process_character (n, appearance="blush false", text="Хррм!")
            call process_character (si, appearance="blush false", text="Вы почти у цели, [n.say_name]!")
            call process_character (n, appearance="blush false", text="Маааам!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg sam_simone_group_sprawl_cum_simone")

            call process_character (si, appearance="blush false", text="Это все, дорогой!")
            call process_character (si, appearance="blush false", text="Дай мне все!")
            call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
            call process_character (sa, appearance="blush false", text="Чувак, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Ты как будто наполняешь маму своим спермой!")
            call static_still_ctc ("bg sam_simone_group_sprawl_aftercum_simone")
        "Кончить в [sa.say_name]":

            if sam_simone_threesome_scene_current_partner != sa:
                call static_still_ctc ("bg sam_simone_group_sprawl_fuck_sam")
            call process_character (n, appearance="blush false", text="Хааа...")
            call process_character (n, appearance="blush false", text="Хррм!")
            call process_character (sa, appearance="blush false", text="Давай сюда!")
            call process_character (n, appearance="blush false", text="Аааах!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
            call static_still_ctc ("bg sam_simone_group_sprawl_cum_sam")

            call process_character (sa, appearance="blush false", text="Все это попало в меня, [n.say_name]!")
            call process_character (n, appearance="blush false", text="Ху! Ох!")
            call process_character (si, appearance="blush false", text="О-Ох мой...")
            call process_character (si, appearance="blush false", text="...")
            call process_character (si, appearance="blush false", text="[n.say_name] действительно уместил все в тебя.")
            call process_character (sa, appearance="blush false", text="Я всегда позволяю ему делать это в мою киску!")
            call process_character (si, appearance="blush false", text="Понятно...")
            call static_still_ctc ("bg sam_simone_group_sprawl_aftercum_sam")

    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}.")
    call process_character (sa, appearance="blush false", text="{i}Фьюю.{/i}.")
    call process_character (si, appearance="blush false", text="{i}Уфф.{/i}..")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Это было здорово!")
    call process_character (n, appearance="blush false", text="Я очень рада, что ты сделала это с нами, Мама!")
    call process_character (sa, appearance="blush false", text="Я тоже!")
    call process_character (sa, appearance="blush false", text="Ты самая лучшая Мама на свете!")
    call process_character (si, appearance="blush false", text="Мне нравится проводить время с вами обоими.")
    call process_character (si, appearance="blush false", text="Это заставляет нам чувствовать друг друга еще ближе!")
    call process_character (sa, appearance="blush false", text="Ты определенно права, Мама!")
    call process_character (n, appearance="blush false", text="Согласен!")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Вуу!")
    call process_character (si, appearance="blush false", text="Не могу поверить, что впереди еще целый день!")
    call process_character (si, appearance="blush false", text="Я уже вытерлась, ха-ха!")
    call process_character (n, appearance="blush false", text="Плавание в бассейне кажется отличным вариантом...")
    call process_character (sa, appearance="blush false", text="Я слышу это, [n.say_name]!")
    call process_character (si, appearance="blush false", text="Вы двое, наслаждайтесь этим!")
    call process_character (si, appearance="blush false", text="Моему саду нужен срочный уход!")

    call sam_simone_threesome_scene_end (dream=dream)
    return

label sam_simone_threesome_scene_end(dream=False):
    call add_replayable_scene ("sam_simone_threesome_scene", si)
    call add_replayable_scene ("sam_simone_threesome_scene", sa)

    python:
        sa.revistable_scenes.add("sam_simone_threesome_scene_revisit_sam")
        si.revistable_scenes.add("sam_simone_threesome_scene_revisit_simone")

        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_given_cunnilingus", 1)
            stats.add_stat("times_had_sex", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_given_vaginal_creampie", 1)
            stats.add_stat("times_had_vaginal_sex", 1)
            stats.add_stat("times_had_paizuri", 1)
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_seen_flat_breasts", 1)
            stats.add_stat("times_seen_big_breasts", 1)
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_had_group_sex", 1)

    call process_end_of_scene ("sam_simone_threesome_scene", dream=dream)

    return


label sam_simone_threesome_scene_revisit_sam:
    $ no_bust_art = False

    if "sam_simone_threesome_scene_revisit" not in scenes_completed:
        call process_character (n, appearance="pose twohandfist face happy blush false")
        call process_character (sa, appearance="pose handface face happy blush false", text="Да!")
        call process_character (sa, appearance="pose handface face happy blush false", text="Давайте спросим ее прямо сейчас!")
    else:
        pass

    call sam_simone_threesome_scene_revisit

    return

label sam_simone_threesome_scene_revisit_simone:
    $ no_bust_art = False

    if "sam_simone_threesome_scene_revisit" not in scenes_completed:
        call process_character (n, appearance="pose behindhead face neutral blush false")
        call process_character (si, appearance="pose handsup face neutral blush false", text="Конечно, милый!")
        call process_character (si, appearance="pose handsup face happy blush false", text="Я уверена, что она будет в восторге, чтобы сделать это снова!")
    else:
        pass

    call sam_simone_threesome_scene_revisit

    return

label sam_simone_threesome_scene_revisit:
    $ scenes_completed.add("sam_simone_threesome_scene_revisit_simone")
    $ scenes_completed.add("sam_simone_threesome_scene_revisit_sam")

    if "sam_simone_threesome_scene_revisit" in scenes_completed:
        call sam_simone_threesome_scene_revisit_2nd_time
    else:
        call sam_simone_threesome_scene_revisit_1st_time

    return

label sam_simone_threesome_scene_revisit_1st_time:
    python hide:
        play_music("audio/music/Resort Loop2.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg sam_simone_group_titfuck_sam_watches")

    call static_still_ctc ("bg sam_simone_group_titfuck_sam_watches")

    call process_character (sa, appearance="blush false", text="Иди, Мама!")
    call process_character (si, appearance="blush false", text="Разве ты не собираешься присоединиться к нам, [sa.say_name]?")
    call process_character (sa, appearance="blush false", text="Ой!")
    call process_character (sa, appearance="blush false", text="Но мне нравится смотреть, как твоя грудь накрывает член [n.say_name]!")
    call process_character (si, appearance="blush false", text="Ха-ха, понятно...")
    call process_character (n, appearance="blush false", text="Хрм!")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (sa, appearance="blush false", text="Как это вообще называется?")
    call process_character (si, appearance="blush false", text="Ты имеешь в виду, что я делаю с моей грудью на пенисе [n.say_name]?")
    call process_character (sa, appearance="blush false", text="Да, да!")
    call process_character (si, appearance="blush false", text="Это называется сиськотрах.")
    call process_character (si, appearance="blush false", text="Ничего сложного, ха-ха.")
    call process_character (sa, appearance="blush false", text="О, конечно!")
    call process_character (sa, appearance="blush false", text="Я должна была догадаться!")
    call process_character (n, appearance="blush false", text="Ах!")
    call process_character (sa, appearance="blush false", text="Твой член почти полностью поглотили мамины сиськи, [n.say_name]!")
    call process_character (sa, appearance="blush false", text="Как будто его проглотили!")
    call process_character (n, appearance="blush false", text="О!")
    call process_character (si, appearance="blush false", text="Подходи и присоединяйся к нам, [sa.say_name].")
    call process_character (si, appearance="blush false", text="Тебе понравилось лизать киску, верно?")
    call process_character (sa, appearance="blush false", text="Да!")

    call static_still_ctc ("bg sam_simone_group_titfuck_sam_licked")

    call process_character (sa, appearance="blush false", text="Аааха...")
    call process_character (si, appearance="blush false", text="[n.say_name] делает хорошую работу?")
    call process_character (sa, appearance="blush false", text="Д-да Мам...")
    call process_character (si, appearance="blush false", text="Твоя сестра похвалила твою способность делать куннилингус, [n.say_name].")
    call process_character (si, appearance="blush false", text="Это большая честь для меня!")
    call process_character (n, appearance="blush false", text="Ммф...")
    call process_character (sa, appearance="blush false", text="Уху...")
    call process_character (sa, appearance="blush false", text="Лижи прямо там, [n.say_name]!")
    call process_character (sa, appearance="blush false", text="Ахх!")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="([sa.say_name] выглядит довольной...)")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="(Возможно, мне придется спросить у [n.say_name], чтобы сделать это со мной когда-нибудь...)")
    call process_character (sa, appearance="blush false", text="...")
    call process_character (sa, appearance="blush false", text="([n.say_name] и я должны сделать это на стриме когда-нибудь...)")
    call process_character (sa, appearance="blush false", text="Ах!")
    call process_character (sa, appearance="blush false", text="(Но я могу потерять концентрацию через некоторое время)")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Я думаю, что хер [n.say_name] готов для тебя, [sa.say_name].")
    call process_character (si, appearance="blush false", text="Ты хочешь заняться этим делом?")
    call process_character (sa, appearance="blush false", text="Я-я хочу запрыгнуть на Маму!")

    call static_still_ctc ("bg sam_simone_group_titfuck_sam_rides")

    call process_character (sa, appearance="blush false", text="У тебя стало получаться!")
    call process_character (sa, appearance="blush false", text="Хер [n.say_name] движется вместе со мной!")
    call process_character (si, appearance="blush false", text="Твоя сестра удовлетворяет тебя, милый?")
    call process_character (n, appearance="blush false", text="Ааахх!")
    call process_character (n, appearance="blush false", text="П-продолжай, [sa.say_name]...")
    call process_character (sa, appearance="blush false", text="Вас поняла, [n.say_name]!")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="(Они любят получать удовольствие, даже занимаясь сексом)")
    call process_character (si, appearance="blush false", text="([sa.say_name] и [n.say_name] так заботятся об этом)")
    call process_character (n, appearance="blush false", text="...")

    if "kira_simone_threesome_scene" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Если только [k.say_name] сможет присоединиться к нам тоже...)")
        call process_character (n, appearance="blush false", text="(Интересно, что бы она попробовала со всеми нами здесь?)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Может быть, в один прекрасный день все мы сможем быть вместе!)")
    else:

        call process_character (n, appearance="blush false", text="(Было бы здорово, если бы Мама смогла быть гостем на стриме с [sa.say_name] и мной...)")
        call process_character (n, appearance="blush false", text="(Я не думаю, что она это сделает)")
        call process_character (n, appearance="blush false", text="(Она все еще хочет, чтобы это было секретом между нами)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Но, возможно, однажды она передумает...)")


    call process_character (sa, appearance="blush false", text="Как долго [n.say_name] трахается с тобой Сама, прежде чем он выстрелил спермой?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Со мной?")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Я не совсем уверена.")
    call process_character (si, appearance="blush false", text="Я знаю, что он способен продержаться дольше!")
    call process_character (si, appearance="blush false", text="Не так ли, [n.say_name]?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я так думаю.")
    call process_character (sa, appearance="blush false", text="Да ну?")
    call process_character (sa, appearance="blush false", text="Он смог продержаться со мной дольше!")
    call process_character (n, appearance="blush false", text="Я ... я уже близко подобрался...")
    call process_character (sa, appearance="blush false", text="Ох!")
    call process_character (sa, appearance="blush false", text="Пока не кончай, [n.say_name]!")
    call process_character (sa, appearance="blush false", text="Тебе все еще нужно трахнуть Маму!")
    call process_character (si, appearance="blush false", text="Только если ты хочешь этого, сладенький.")
    call process_character (sa, appearance="blush false", text="Ты должен продержаться немного дольше ради мамы [n.say_name]!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я могу продолжать в том же духе.")
    call process_character (si, appearance="blush false", text="Если ты чувствуешь желание кончить, не пытайся сдержать его.")

    $ sam_simone_threesome_scene_current_partner = si

    call static_still_ctc ("bg sam_simone_group_sprawl_fuck_simone")

    call process_character (sa, appearance="blush false", text="Отлично, [n.say_name]!")
    call process_character (sa, appearance="blush false", text="Теперь мама может наслаждаться!")
    call process_character (si, appearance="blush false", text="Д-Да, могу!")
    call process_character (si, appearance="blush false", text="Ох, ох!")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}.")
    call process_character (sa, appearance="blush false", text="Убедитесь, что мама много получит, [n.say_name]!")
    call process_character (si, appearance="blush false", text="Давай сильнее, дорогой!")
    call process_character (si, appearance="blush false", text="Ммм!")
    call process_character (sa, appearance="blush false", text="Посмотри, как сиськи мамы шлепаются, когда ты двигаешься быстрее, [n.say_name]!")
    call process_character (sa, appearance="blush false", text="Они такие упругие!")

    jump sam_simone_threesome_scene_revisit_1st_time_phase_2

    return

label sam_simone_threesome_scene_revisit_1st_time_phase_2:
    window hide
    call screen sam_simone_threesome_scene_revisit_choose_partner_first_time
    return

label sam_simone_threesome_scene_revisit_1st_time_phase_3:
    call process_character (n, appearance="blush false", text="Вы оба чувствуете себя так хорошо...")
    call process_character (n, appearance="blush false", text="Я готов кончить!")
    call process_character (sa, appearance="blush false", text="Твой выбор, чувак!")
    call process_character (si, appearance="blush false", text="Это зависит от тебя, милый!")

    window hide
    menu:
        "Кончить в Маму":
            if sam_simone_threesome_scene_current_partner != si:
                call static_still_ctc ("bg sam_simone_group_sprawl_fuck_simone")

            call process_character (si, appearance="blush false", text="Да детка, да!")
            call process_character (si, appearance="blush false", text="Кончи внутрь меня!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg sam_simone_group_sprawl_cum_simone")

            call process_character (n, appearance="blush false", text="Ннгх!")
            call process_character (si, appearance="blush false", text="Очень хорошо, дорогой!")
            call process_character (si, appearance="blush false", text="Выпускай столько, сколько хочешь!")
            call process_character (n, appearance="blush false", text="Ааах...")
            call process_character (n, appearance="blush false", text="...")

            call static_still_ctc ("bg sam_simone_group_sprawl_aftercum_simone")

            call process_character (sa, appearance="blush false", text="Это было эпично, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Ты взяла эту порцию, как босс, Мама!")
        "Кончить в [sa.say_name]":
            if sam_simone_threesome_scene_current_partner != sa:
                call static_still_ctc ("bg sam_simone_group_sprawl_fuck_sam")

            call process_character (sa, appearance="blush false", text="Ха, ах!")
            call process_character (sa, appearance="blush false", text="Сделай это, [n.say_name]!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg sam_simone_group_sprawl_cum_sam")

            call process_character (n, appearance="blush false", text="Ннгх!")
            call process_character (sa, appearance="blush false", text="Даааа, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Я чувствую, как ты брызгаешь в меня!")
            call process_character (n, appearance="blush false", text="Ааах..")
            call process_character (n, appearance="blush false", text="...")

            call static_still_ctc ("bg sam_simone_group_sprawl_aftercum_sam")

            call process_character (si, appearance="blush false", text="...")
            call process_character (si, appearance="blush false", text="(Из киски [sa.say_name] капает сперма...)")
            call process_character (si, appearance="blush false", text="...")
            call process_character (si, appearance="blush false", text="(Она знает о том, что происходит, когда...)")

    call sam_simone_threesome_scene_revisit_end
    return

label sam_simone_threesome_scene_revisit_2nd_time:
    python hide:
        play_music("audio/music/Resort Loop2.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg sam_simone_group_titfuck_sam_rides")

    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="(Интересно, как мы теперь справимся с семейными прогулками...)")
    call process_character (si, appearance="blush false", text="(Я надеюсь [n.say_name] или [sa.say_name] не попытаются потрахаться, пока мы на пикнике или что-нибудь!)")
    call process_character (si, appearance="blush false", text="(Что, если они попытаются схватить меня за грудь, пока мы в торговом центре?)")
    call process_character (si, appearance="blush false", text="(Мне придется установить с ними некоторые основные правила, чтобы это не вышло из-под контроля...)")
    call process_character (sa, appearance="blush false", text="...")
    call process_character (sa, appearance="blush false", text="(У нас должны быть специальные мероприятия на праздники!)")
    call process_character (sa, appearance="blush false", text="(Может быть, мы можем разодеться на Хэллоуин, и так трахнуться!)")
    call process_character (sa, appearance="blush false", text="(Или, может быть, можем у нас будет голый барбекю у бассейна!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я надеюсь, что у нас будет достаточно времени в течение учебного года, чтобы трахаться так!)")
    call process_character (n, appearance="blush false", text="(Я бы не возражал, если бы мама сказала, что мы должны вести себя хорошо в школе, чтобы мы могли сделать это еще!)")

    call static_still_ctc ("bg sam_simone_group_sprawl")

    menu:
        "Мама":
            $ sam_simone_threesome_scene_current_partner = si
            call static_still_ctc ("bg sam_simone_group_sprawl_fuck_simone")
            pass
        "[sa.say_name]":
            $ sam_simone_threesome_scene_current_partner = sa
            call static_still_ctc ("bg sam_simone_group_sprawl_fuck_sam")
            pass

    jump sam_simone_threesome_scene_revisit_2nd_time_phase_2
    return

label sam_simone_threesome_scene_revisit_2nd_time_phase_2:
    window hide
    call screen sam_simone_threesome_scene_revisit_choose_partner_second_time
    return

label sam_simone_threesome_scene_revisit_2nd_time_phase_3:
    menu:
        "Кончить в Маму":
            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg sam_simone_group_sprawl_cum_simone")

            call process_character (n, appearance="blush false", text="Хьяях!")
            call process_character (si, appearance="blush false", text="Постарайся говорить тише, милый.")
            call process_character (sa, appearance="blush false", text="Он ничего не может поделать с собой, Мама!")
            call process_character (sa, appearance="blush false", text="Наши киски слишком хорошие!")
        "Кончить в [sa.say_name]":

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg sam_simone_group_sprawl_cum_sam")

            call process_character (n, appearance="blush false", text="Ммм!")
            call process_character (sa, appearance="blush false", text="Динь!")
            call process_character (sa, appearance="blush false", text="Еще один выстрел в киску для меня!")

    call sam_simone_threesome_scene_revisit_end
    return

label sam_simone_threesome_scene_revisit_end:

    python:
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_given_cunnilingus", 1)
        stats.add_stat("times_had_sex", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_given_vaginal_creampie", 1)
        stats.add_stat("times_had_vaginal_sex", 1)
        stats.add_stat("times_had_paizuri", 1)
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_seen_flat_breasts", 1)
        stats.add_stat("times_seen_big_breasts", 1)
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_had_group_sex", 1)

    call process_end_of_scene ("sam_simone_threesome_scene_revisit", reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label sam_simone_threesome_scene_revisit_choose_sam_first_time:
    if sam_simone_threesome_scene_current_partner != sa:
        call static_still_ctc ("bg sam_simone_group_sprawl_fuck_sam")
    $ sam_simone_threesome_scene_current_partner = sa

    $ dice_roll = random.randint(1,2)

    if dice_roll == 1:
        call process_character (sa, appearance="blush false", text="Ты трахаешь меня снова, [n.say_name]?")
        call process_character (sa, appearance="blush false", text="Мило!")
    else:
        call process_character (sa, appearance="blush false", text="Это правильно, [n.say_name]!")
        call process_character (sa, appearance="blush false", text="Мы все прекрасно себя чувствуем от этого!")

    jump sam_simone_threesome_scene_revisit_1st_time_phase_2
    return

label sam_simone_threesome_scene_revisit_choose_simone_first_time:
    if sam_simone_threesome_scene_current_partner != si:
        call static_still_ctc ("bg sam_simone_group_sprawl_fuck_simone")
    $ sam_simone_threesome_scene_current_partner = si

    $ dice_roll = random.randint(1,2)

    if dice_roll == 1:
        call process_character (si, appearance="blush false", text="Дай мне больше, [n.say_name]!")
    else:
        call process_character (si, appearance="blush false", text="Трахни меня детка!")
        call process_character (si, appearance="blush false", text="Трахни меня и твою сестру!")

    jump sam_simone_threesome_scene_revisit_1st_time_phase_2

    return

screen sam_simone_threesome_scene_revisit_choose_partner_first_time:
    vbox:
        xalign 0.02
        yalign 0.02
        spacing 30
        use main_menu_button(text="Мама", action=Jump("sam_simone_threesome_scene_revisit_choose_simone_first_time"), enabled=sam_simone_threesome_scene_current_partner != si)
        use main_menu_button(text="[sa.say_name]", action=Jump("sam_simone_threesome_scene_revisit_choose_sam_first_time"), enabled=sam_simone_threesome_scene_current_partner != sa)
        use main_menu_button(text="Кончить!", action=Jump("sam_simone_threesome_scene_revisit_1st_time_phase_3"))

screen sam_simone_threesome_scene_revisit_choose_partner_second_time:
    vbox:
        xalign 0.02
        yalign 0.02
        spacing 30
        use main_menu_button(text="Мама", action=Jump("sam_simone_threesome_scene_revisit_choose_simone_second_time"), enabled=sam_simone_threesome_scene_current_partner != si)
        use main_menu_button(text="[sa.say_name]", action=Jump("sam_simone_threesome_scene_revisit_choose_sam_second_time"), enabled=sam_simone_threesome_scene_current_partner != sa)
        use main_menu_button(text="Кончить!", action=Jump("sam_simone_threesome_scene_revisit_2nd_time_phase_3"))

label sam_simone_threesome_scene_revisit_choose_sam_second_time:
    if sam_simone_threesome_scene_current_partner != sa:
        call static_still_ctc ("bg sam_simone_group_sprawl_fuck_sam")
    $ sam_simone_threesome_scene_current_partner = sa

    $ dice_roll = random.randint(1,3)

    if dice_roll == 1:
        call process_character (sa, appearance="blush false", text="Это должно быть частью нашей повседневной жизни!")
    elif dice_roll == 2:
        call process_character (sa, appearance="blush false", text="(Бьюсь об заклад, что [n.say_name] трахает маму тонну раз, когда я занята!)")
    else:
        call process_character (sa, appearance="blush false", text="Я должна следить за тем, сколько раз ты кончаешь в наши киски!")

    jump sam_simone_threesome_scene_revisit_2nd_time_phase_2
    return

label sam_simone_threesome_scene_revisit_choose_simone_second_time:
    if sam_simone_threesome_scene_current_partner != si:
        call static_still_ctc ("bg sam_simone_group_sprawl_fuck_simone")
    $ sam_simone_threesome_scene_current_partner = si

    $ dice_roll = random.randint(1,3)

    if dice_roll == 1:
        call process_character (si, appearance="blush false", text="Можешь ли ты помочь очистить дом со мной после, [n.say_name]?")
        call process_character (n, appearance="blush false", text="Конечно, Мама.")
    elif dice_roll == 2:
        call process_character (si, appearance="blush false", text="Думаю, я закажу пиццу сегодня вечером.")
        call process_character (si, appearance="blush false", text="Как вам?")
        call process_character (sa, appearance="blush false", text="Звучит хорошо, мама!")
        call process_character (n, appearance="blush false", text="Да!")
    else:
        call process_character (si, appearance="blush false", text="(Интересно, как часто [sa.say_name] и [n.say_name] заниматься сексом, когда меня нет рядом...)")

    jump sam_simone_threesome_scene_revisit_2nd_time_phase_2

    return

label sam_julia_threesome_scene(dream=False):
    call sam_julia_threesome_scene_sex (dream=dream)

    return

label sam_julia_threesome_scene_sex(dream=False):
    call process_scene_beginning (bg="bg sam_room_daytime", char_tuple_array=[], dream=dream)

    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (sa, "outfit clothes pose leaning face neutral blush false") ])


    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Хорошо [n.say_name]...")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Если у тебя есть какие-то планы, то отложи их в сторону!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Почему, что-то случилось?")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Ты разве не помнишь, какая сегодня вышла игра?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Я пытаюсь вспомнить...")
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="Это серия файтингов, которой ты одержим, и думаешь, что она величайшая?")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Ой, быть того не может!!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Ты говоришь, что сегодня вышла игра Мега Сокрушительные Приятели?!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="Ты очень долго ждал, когда она выйдет!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Как будто вечность!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Ты права [sa.say_name], сегодня не будет ничего, кроме этой игры!")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Там так много персонажей, которых можно разблокировать, это круто!")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Я хочу получить их всех в первый же день игры!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Держу пари, это будет тяжело.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Разработчики делают это специально трудным делом.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Кроме того, нет никаких руководств, потому что игра новая.")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Это то, что делает её лучше, [n.say_name]!")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Не имея руководства, мы лично откроем для себя все секреты и достижения!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Это отличная идея, да!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Я не хочу узнать про новых персонажей от других игроков!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Узнать самому намного лучше!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Бери контроллер, [n.say_name]!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Давайте драться друг с другом в течение нескольких раундов, чтобы привыкнуть к механике!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Я думаю, что они те же, что и в предыдущей игре.")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Да, но они всегда меняют разные штуки каждый раз, когда выпускают новую версию.")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Если мы изучим их вместе, нам будет легче разблокировать всех персонажей!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Это правда.")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Кроме того, я хочу показать тебе, насколько я стала лучше!")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Я тренировалась в предыдущей игре, когда тебя не было.")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Я уверена, что смогу победить тебя сейчас!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Ты, должно быть, много тренировалась, чтобы так говорить!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Я освоил движения нескольких персонажей.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Надеюсь, они не изменили их слишком сильно в новой версии.")
    call process_character (n, appearance="pose behindhead face happy blush false", text="Потому что я хочу дать тебе достойный вызов с моими лучшими героями!")

    call fade_to_black (1)


    call process_new_location ("bg sam_room_daytime", dream=dream)

    $ display_multiple_characters([ (sa, "outfit clothes pose handsbehind face neutral blush false"), (n, "outfit clothesjacket pose twohandfist face happy blush false") ])


    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Управление намного лучше в этой новой версии!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="И я не могу поверить, здесь есть новые этапы и музыка, которые они добавили!")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Неудивительно, что потребовалось так много времени, чтобы сделать это, они забили игру новыми фишками!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Это легко будет моя новая любимая игра в течение всего лета!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Возможно даже до конца года!")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Так что я больше подхожу для тебя сейчас, [n.say_name]?")
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="Мы идём ноздря в ноздрю с нашими победами друг над другом!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Ты значительно улучшилась.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="У меня было много практики!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Это то, что окупается в конце концов.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Сколько игр ты хотите сыграть?")
    call process_character (sa, appearance="pose handface face flirt blush false", text="Не знаю, как ты, но я начинаю возбуждаться.")
    call process_character (sa, appearance="pose handface face flirt blush false", text="Мы должны потрахаться после того, как закончим!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Да!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Я готов к этому!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Ты хочешь отсосать у меня или ты хочешь, чтобы я тебя трахнул?")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Почему бы нам не сделать и то, и другое!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Оба в раз?")
    call process_character (sa, appearance="pose handface face flirt blush false", text="Я сегодня очень возбуждена.")
    call process_character (sa, appearance="pose handface face flirt blush false", text="Так что на этот раз мы должны сделать что-то большее.")
    call process_character (sa, appearance="pose handface face flirt blush false", text="Я думаю, что это будет весело!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Интересно, смогу ли я продержаться так долго...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Это не похоже на то, что мы новички в этом уже, [n.say_name].")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Мы можем трахаться всё дольше и дольше!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Помнишь, как долго я сосала тебе на стриме?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Да...")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Я думаю, это было почти тридцать минут.")
    call process_character (sa, appearance="pose handface face happy blush false", text="Двадцать девять минут и сорок две секунды, если быть точным!")
    call process_character (sa, appearance="pose handface face happy blush false", text="И я знаю, что сосала довольно сильно в определенные моменты!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты много играла с крайней плотью на моем члене...")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Ага!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Когда мы только начали это делать, ты продержался всего несколько минут после минета.")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Теперь посмотри, как долго ты можешь продолжать!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="А ты все равно кончаешь много.")
    call process_character (sa, appearance="pose handface face embarrassed blush false", text="Я думаю, твоя сперма попала на один из запасных контроллеров…")
    call process_character (sa, appearance="pose handface face embarrassed blush false", text="Он все еще немного липкий.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Дело в том, что ты продлил время, которое тебе нужно, чтобы кончить!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Давай попробуем разблокировать еще одного персонажа, и тогда потрахаемся!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Звучит неплохо.")


    call fade_to_black (1)


    call process_new_location ("bg hallway_daytime", dream=dream)

    call process_character (julia, appearance="outfit clothes pose handface face curious blush false", text="...")
    call process_character (julia, appearance="pose handface face curious blush false", text="(Где [sa.say_name] и [n.say_name]?)")
    call process_character (julia, appearance="pose handface face curious blush false", text="(Я знаю, что они не уходили)")
    call process_character (julia, appearance="pose handface face curious blush false", text="...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="(Я думаю, что они играли в видеоигры весь день)")
    call process_character (julia, appearance="pose handup face neutral blush false", text="(Если глядеть на экран всё время, то будут болеть глаза)")
    call process_character (julia, appearance="pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="(Я хотела продолжить кампанию Парящих Королевств)")
    call process_character (julia, appearance="pose armcross face concerned blush false", text="(Не могу без них)")
    call process_character (julia, appearance="pose armcross face concerned blush false", text="(И я могу только планировать свои ходы наперед...)")
    call process_character (julia, appearance="pose armcross face concerned blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="(Я просто спрошу, хотят ли они играть или нет)")
    call process_character (julia, appearance="pose handface face neutral blush false", text="(Нам нужно сделать расписание игры, потому что эти задержки становятся раздражающими)")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...{p}...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="([n.say_name] не в своей комнате, поэтому он определенно с [sa.say_name] играет в видеоигры)")
    call process_character (julia, appearance="pose handup face curious blush false", text="(Я не слышу звука их телевизора...)")
    call process_character (julia, appearance="pose handup face curious blush false", text="(Они уже закончили?)")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="(Дверь слегка приоткрыта)")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="(Можно посмотреть, если они все еще находятся в игровой сессии...)")

    call fade_to_black (1)


    call static_still_ctc ("bg sam_bj_lick")

    call process_character (sa, appearance="blush false", text="Мне нравится, что, если я лизну кончик члена [n.say_name] пару раз, и тогда он сразу встаёт.")
    call process_character (n, appearance="blush false", text="Он всё еще очень чувствительный.")
    call process_character (julia, appearance="blush false", text="...{p}...")
    call process_character (sa, appearance="blush false", text="Хорошо, готова отсосать?")

    call static_still_ctc ("bg sam_bj_suck")

    call process_character (julia, appearance="blush false", text="...{p}...")
    call process_character (sa, appearance="blush false", text="Ммм...")
    call process_character (n, appearance="blush false", text="Ты так хороша в этом, [sa.say_name].")
    call process_character (sa, appearance="blush false", text="Ммф...")
    call process_character (sa, appearance="blush false", text="Как и в случае с видеоиграми, все сводится к большой практике...")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Практике?)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="([n.say_name] и [sa.say_name] делают это уже некоторое время?)")
    call process_character (julia, appearance="blush false", text="(Похоже, что да)")
    call process_character (julia, appearance="blush false", text="([sa.say_name] сосёт у [n.say_name] с большой уверенностью...)")
    call process_character (n, appearance="blush false", text="Ах...")
    call process_character (n, appearance="blush false", text="Когда мы начнем трахаться?")
    call process_character (sa, appearance="blush false", text="Мм...")
    call process_character (sa, appearance="blush false", text="В любое время, когда захочешь.")
    call process_character (n, appearance="blush false", text="Давай поменяемся сейчас местами.")

    call static_still_ctc ("bg sam_vaginal_dick_in")

    call process_character (julia, appearance="blush false", text="(Так это что-то большее, чем просто брать в рот)")
    call process_character (sa, appearance="blush false", text="Ха! Ахх!")
    call process_character (sa, appearance="blush false", text="Быстрее, [n.say_name], быстрее!")
    call process_character (sa, appearance="blush false", text="Оох!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Я думаю, что [n.say_name] получал только от меня киску...)")
    call process_character (julia, appearance="blush false", text="...{p}...")
    call process_character (julia, appearance="blush false", text="([sa.say_name] развлекается с [n.say_name])")
    call process_character (julia, appearance="blush false", text="(Но она хорошо справляется)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Я никогда бы не догадалась, что она любит члены)")
    call process_character (julia, appearance="blush false", text="(Она легко одурачила меня)")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}Вздох.{/i}..")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="([n.say_name] едва мог справиться с футджобом, когда я впервые делала...)")
    call process_character (julia, appearance="blush false", text="(Теперь он так быстро трахается, как будто это не имеет большого значения)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Он научился держаться дольше после моих тренировок)")
    call process_character (julia, appearance="blush false", text="(Я научила его, как дисциплинировать его член)")
    call process_character (julia, appearance="blush false", text="(И теперь он использует эту дисциплину, чтобы насладиться киской своей сестры)")
    call process_character (sa, appearance="blush false", text="Ммм!")
    call process_character (sa, appearance="blush false", text="Можешь продолжать, [n.say_name]?")
    call process_character (sa, appearance="blush false", text="Это самый долгий раз, что у нас был до сих пор!")
    call process_character (n, appearance="blush false", text="Хрм!")
    call process_character (n, appearance="blush false", text="Думаю, у меня получится...")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Похоже, что Парящие Королевства сегодня откладываются...)")

    call process_new_location (hallway, dream=dream)

    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...{p}...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="([n.say_name] скрывал это от меня)")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="(Он довольно смелый, чтобы трахать двух девушек в его же доме)")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="(Ему это сошло с рук...)")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="(Трахает свою Кузину, и трахает свою сестру...)")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="(Интересно, что еще он скрывает)")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="(Бьюсь об заклад. что [sa.say_name] не знает обо мне и [n.say_name])")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="(На самом деле, я уверена, что она не знает)")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="(Я думаю, что пришло время для меня, чтобы изменить это...)")

    call process_new_location ("bg sam_room_evening", dream=dream)

    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="...")
    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="(Какой будет следующий персонаж для Мега Парней?)")
    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="(Похоже, на экране выбора персонажа есть открытые слоты...)")

    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false position right")

    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Привет, [julia.say_name]!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Я не ожидала, что ты придешь сегодня!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="[n.say_name] и я играли в эту удивительную новую игру сегодня!")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="На самом деле мы собираемся сыграть еще немного после, [n.say_name] делает закуски внизу.")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Ты хочешь присоединиться к нам?")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Нет, спасибо, я откажусь.")
    call process_character (sa, appearance="outfit clothes pose handface face concerned blush false", text="О, правда?")
    call process_character (sa, appearance="outfit clothes pose handface face concerned blush false", text="Думаю, тебе понравится.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Это очень легко узнать!")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="На самом деле я хотела поговорить с тобой, пока [n.say_name] нет в комнате.")
    call process_character (julia, appearance="outfit clothes pose handface face neutral blush false", text="Я не хотела, чтобы он услышал.")
    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="Ты не хочешь, чтобы [n.say_name] услышал, что ты будешь говорить со мной?")
    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="...")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Ох, ох!")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Что-то о нём?")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Можно и так сказать.")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Это то, чего ты о нем не знаешь.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Существует не так много, чего я не знаю о [n.say_name].")
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="Так это должно быть супер секрет!")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Я узнала об этом только сегодня.")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Ух ты!")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Итак, это совершенно новая информация о [n.say_name]!")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Расскажи!")

    call process_new_location ("bg hallway_evening", dream=dream)

    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="(Это хорошая закуска!)")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="(Теперь я подпитался, чтобы играть еще!)")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="([sa.say_name] и я должны играть в новом режиме испытания)")
    call process_character (n, appearance="outfit clothes pose behindhead face neutral blush false", text="(Это звучит очень сложно, нужно победить каждого персонажа на одной жизни!)")
    call process_character (n, appearance="outfit clothes pose behindhead face happy blush false", text="(Но я уверен, что мы откроем нового персонажа, если мы завершим его!)")
    call process_character (n, appearance="outfit clothes pose handfist face neutral blush false", text="(Тогда есть сто проблем, которые нам нужно решить...)")
    call process_character (n, appearance="outfit clothes pose handfist face happy blush false", text="(Эта игра упакована содержанием!)")

    call process_new_location ("bg sam_room_evening", dream=dream)


    $ display_multiple_characters([ (n, "outfit clothes pose handsdown face neutral blush false"), (sa, "outfit clothes pose handface face curious blush false") ])

    $ replace_position = True

    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="Хорошо, я вернулся!")
    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="Привет, [julia.say_name]!")
    call process_character (n, appearance="outfit clothes pose handfist face neutral blush false", text="[sa.say_name] рассказала тебе о новой игре, в которую мы играем?")
    call process_character (n, appearance="outfit clothes pose handfist face happy blush false", text="Она быстро становится моим фаворитом!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face curious blush false", text="...")
    call process_character (n, appearance="outfit clothes pose behindhead face neutral blush false", text="Что у тебя с лицом, [sa.say_name]?")
    call process_character (n, appearance="outfit clothes pose behindhead face neutral blush false", text="Ты не смогла победить одно из трудных испытаний?")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Нет, дело не в этом.")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Я только что сообщила ей о наших эскападах этим летом, [n.say_name].")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="Эскападах?")
    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="...")
    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="[julia.say_name] действительно делала тебе минет, [n.say_name]?")
    call process_character (n, appearance="outfit clothes pose twohandfist face embarrassed blush false", text="Что?!")
    call process_character (n, appearance="outfit clothes pose twohandfist face embarrassed blush false", text="Ты рассказала [sa.say_name] об этом, [julia.say_name]?!")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="Вообще-то, я ей всё рассказала.")
    call process_character (julia, appearance="outfit clothes pose handup face neutral blush false", text="С того момента, как ты увидел меня голой, до того, как ты трахнул меня на полу своей спальни.")
    call process_character (n, appearance="outfit clothes pose behindhead face embarrassed blush true", text="...{p}...")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Почему это смущает тебя, [n.say_name]?")
    call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="Есть ли причина, по которой [sa.say_name] не должна знать об этом?")
    call process_character (n, appearance="outfit clothes pose handsdown face concerned blush true", text="...")
    call process_character (n, appearance="outfit clothes pose handsdown face concerned blush true", text="Ну, это просто...")
    call process_character (sa, appearance="pose handsbehind face curious blush false", text="Итак, ты и [julia.say_name] делали все это...")
    call process_character (sa, appearance="pose handsbehind face curious blush false", text="Большую часть лета...")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="(Интересно, что [sa.say_name] собирается сделать сейчас)")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="(Бьюсь об заклад, она откажет ему в сексе до конца лета...)")
    call process_character (sa, appearance="pose handface face curious blush false", text="...")
    call process_character (sa, appearance="pose handface face curious blush false", text="Ну [n.say_name], у меня только один вопрос...")
    call process_character (n, appearance="pose handsdown face concerned blush true", text="...")
    call process_character (sa, appearance="pose handface face happy blush false", text="Почему ты не пригласил меня посмотреть?!")
    call process_character (julia, appearance="pose armcross face curious blush false", text="А?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Ох...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Я просто...{w=1.0}не подумал…")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ну же, [n.say_name]!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Как можно забыть о чём-то подобном?")
    call process_character (julia, appearance="pose handface face curious blush false", text="Тебя не беспокоит, что [n.say_name] и я трахаемся?")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Единственное, что меня беспокоит, это то, как много я пропустила!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Типа, дрочки ногами?!")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Я бы никогда не подумала тереть твой член ногами, [n.say_name]!")
    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Ох, кстати, [julia.say_name] знает, что мы трахаемся тоже!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Я думаю, мы полностью не закрывали дверь сегодня, и она видела нас!")
    call process_character (n, appearance="pose handsdown face embarrassed blush false", text="...")
    call process_character (julia, appearance="pose armcross face curious blush false", text="...")
    call process_character (julia, appearance="pose armcross face curious blush false", text="(Ну, это неожиданно...)")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Ох, ох!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Теперь у меня есть более важный вопрос!")
    call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Хочешь знать, что это значит?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Что?")
    call process_character (sa, appearance="pose handface face happy blush false", text="Мы можем трахаться вместе?!")
    call process_character (julia, appearance="pose handface face concerned blush false", text="Мы?")
    call process_character (julia, appearance="pose handface face concerned blush false", text="Ты имеешь в виду всех нас троих?")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Черт возьми, да!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Ты и я, [julia.say_name], будем вместе на члене [n.say_name]!")


    if stats.stat_value('times_had_group_sex') > 0 or "kira_simone_threesome_scene" in scenes_completed or "sam_simone_threesome_scene" in scenes_completed:
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    else:
        call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="В-вместе?")

    call process_character (julia, appearance="pose armcross face curious blush false", text="...")
    call process_character (julia, appearance="pose armcross face curious blush false", text="Ты...{w=1.0}хочешь сделать что-нибудь подобное, [sa.say_name]?")

    if "sam_simone_threesome_scene" in scenes_completed:
        call process_character (sa, appearance="pose handface face happy blush false", text="Конечно, да!")
        call process_character (sa, appearance="pose handface face neutral blush false", text="[n.say_name] и я делали это раньше, и это супер весело!")
        call process_character (julia, appearance="pose handface face embarrassed blush false", text="(Что?)")
        call process_character (julia, appearance="pose handface face embarrassed blush false", text="(У них раньше были тройнички?)")
        call process_character (julia, appearance="pose handface face embarrassed blush false", text="(Что делают эти двое?)")
    else:
        call process_character (sa, appearance="pose handface face happy blush false", text="Думаю, это будет супер весело!")
        call process_character (sa, appearance="pose handface face happy blush false", text="Ну же!")


    call character_leave_dissolve (sa)
    pause 0.5

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call process_character (sa, appearance="outfit nude pose leaning face neutral blush false")
    pause 0.5


    call process_character (n, appearance="outfit clothes pose handsdown face concerned blush false")

    call process_character (sa, appearance="outfit nude pose leaning face neutral blush false", text="Мы можем вернуться к игре позже, [n.say_name]!")
    call process_character (sa, appearance="outfit nude pose leaning face happy blush false", text="Теперь это стало главным приоритетом!")
    call process_character (julia, appearance="outfit clothes pose handup face curious blush false", text="...{p}...")
    call process_character (julia, appearance="outfit clothes pose handup face happy blush false", text="(Я не могла предсказать этот результат)")
    call process_character (julia, appearance="outfit clothes pose handup face happy blush false", text="...")
    call process_character (julia, appearance="outfit clothes pose handup face happy blush false", text="(Похоже, мне придется показать [sa.say_name], что я знаю об ублажении [n.say_name]...)")

    call character_leave_dissolve (julia)
    pause 0.5

    call process_character (julia, appearance="outfit nude pose armcross face happy blush false")
    pause 0.5

    call process_character (julia, appearance="outfit nude pose armcross face happy blush false", text="Я подготовлю себя, [n.say_name]...")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="([sa.say_name] и [julia.say_name] смотрят на меня смешно...)")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="(Они приближаются...)")
    call process_character (sa, appearance="outfit nude pose handsbehind face happy blush false", text="Я сниму его штаны, ты снимешь его рубашку!")
    call process_character (n, appearance="outfit clothes pose behindhead face embarrassed blush false", text="А?")

    $ clear_characters()
    with Dissolve(0.25)

    pause 0.5

    call process_character (n, appearance="outfit nudehard pose handsdown face concerned blush false", show_bust=False)
    $ refresh_character(n, force_transition = Dissolve(0.25))

    pause 0.25

    call process_character (julia, appearance="outfit nude pose armcross face happy blush false position julia_sam_threesome_closer_julia", show_bust=False)
    call process_character (sa, appearance="outfit nude pose handsbehind face neutral blush false position julia_sam_threesome_closer_sam", show_bust=False)
    $ refresh_character(sa, force_no_dissolve = True)
    $ refresh_character(julia, force_no_dissolve = True)
    with Dissolve(0.25)


    call process_character (sa, appearance="outfit nude pose handsbehind face neutral blush false position julia_sam_threesome_closer_sam", text="Что мы сделаем в первую очередь?")
    call process_character (sa, appearance="outfit nude pose handsbehind face happy blush false", text="Я не могу принять решение!")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="...")
    call process_character (julia, appearance="outfit nude pose armcross face happy blush false position julia_sam_threesome_closer_julia", text="Я буду выбирать.")
    call process_character (julia, appearance="outfit nude pose armcross face happy blush false", text="[n.say_name], подойди к постели.")
    call process_character (n, appearance="outfit nudehard pose behindhead face curious blush false", text="...")
    call process_character (sa, appearance="outfit nude pose handface face neutral blush false", text="Мне нравится, к чему ты клонишь!")
    call process_character (sa, appearance="outfit nude pose handface face neutral blush false", text="Что бы это могло быть?")

    call fade_to_black (1)

    call process_character (n, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Ложись, [n.say_name].")
    call process_character (julia, appearance="blush false", text="[sa.say_name] и я возьмём управление на себя.")
    call process_character (sa, appearance="blush false", text="Мы покажем тебе силу двух, [n.say_name]!")
    call process_character (n, appearance="blush false", text="...")

    call static_still_ctc ("bg julia_sam_group_blowjob")

    call process_character (n, appearance="blush false", text="Ух ты!")
    call process_character (sa, appearance="blush false", text="Я с этой стороны, [julia.say_name]!")
    call process_character (julia, appearance="blush false", text="Я поняла.")
    call process_character (n, appearance="blush false", text="Ааах!")
    call process_character (sa, appearance="blush false", text="Как тебе, [n.say_name]?")
    call process_character (sa, appearance="blush false", text="Каково это?")

    call static_still_ctc ("bg julia_sam_group_blowjob_pre")

    call process_character (n, appearance="blush false", text="(Я чувствую губы [sa.say_name] на одной стороне моего члена, и [julia.say_name] на другой!)")
    call process_character (n, appearance="blush false", text="(Их рты обвиваются вокруг кончика!)")
    call process_character (n, appearance="blush false", text="Гннг!")
    call process_character (julia, appearance="blush false", text="Ты толкаешь мне за щеку, [sa.say_name].")
    call process_character (sa, appearance="blush false", text="Я хочу вложить больше члена [n.say_name] в рот!")
    call process_character (sa, appearance="blush false", text="Мне нужно подойти поближе.")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Я думала, что [sa.say_name] позволила мне сосать у [n.say_name], но сама...)")
    call process_character (julia, appearance="blush false", text="(Но она решила остаться на его члене)")
    call process_character (n, appearance="blush false", text="Ааахх!")
    call process_character (n, appearance="blush false", text="(Оба они сосут так по-разному!)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Как ты думаешь, одна из нас сосет лучше, чем другая, [n.say_name]?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я-я...")
    call process_character (sa, appearance="blush false", text="Черт возьми, что за вопрос!")
    call process_character (sa, appearance="blush false", text="Не думаю, что это имеет значение.")
    call process_character (sa, appearance="blush false", text="Важно то, что его член сходит с ума от этого!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я не могу выбрать.")
    call process_character (n, appearance="blush false", text="Здорово, что вы обе сосете у меня!")
    call process_character (julia, appearance="blush false", text="Количество предсемени, которую ты производишь, похоже, подтверждает это.")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (julia, appearance="blush false", text="Я видела, как долго ты можешь продержаться с [sa.say_name], [n.say_name].")
    call process_character (julia, appearance="blush false", text="Ты не должен кончать в этот момент!")
    call process_character (sa, appearance="blush false", text="Нет, у него еще есть способы продлить это!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (sa, appearance="blush false", text="Эй, я знаю, что мы можем сделать!")
    call process_character (sa, appearance="blush false", text="Я только что вспомнила это из видео, которое я видел.")
    call process_character (julia, appearance="blush false", text="Что?")
    call process_character (sa, appearance="blush false", text="Давайте тереться нашими киски по члену [n.say_name]!")
    call process_character (julia, appearance="blush false", text="Значит мы делаем это по одной?")
    call process_character (sa, appearance="blush false", text="Нет, нет!")
    call process_character (sa, appearance="blush false", text="Мы делаем это одновременно!")
    call process_character (n, appearance="blush false", text="Тереться своими кисками о мой член?")
    call process_character (julia, appearance="blush false", text="Звучит действительно интересно.")
    call process_character (sa, appearance="blush false", text="Не так ли?")
    call process_character (sa, appearance="blush false", text="Я говорю, что мы сделаем это!")

    call fade_to_black (1)

    call process_character (n, appearance="blush false", text="...")
    call process_character (sa, appearance="blush false", text="Ты можешь оставаться на месте, [n.say_name].")
    call process_character (sa, appearance="blush false", text="[julia.say_name] и мне просто нужно попасть в нужное место...")
    call process_character (julia, appearance="blush false", text="Ты уверена, что это возможно?")
    call process_character (sa, appearance="blush false", text="Конечно, я уверена!")
    call process_character (sa, appearance="blush false", text="Мне просто нужно обхватить тебя ногами, чтобы все получилось.")
    call process_character (sa, appearance="blush false", text="Поставь свои ноги сюда...")
    call process_character (sa, appearance="blush false", text="Ииии, я думаю, у нас получилось!")

    call static_still_ctc ("bg julia_sam_group_grind")

    call process_character (n, appearance="blush false", text="Ооох!")
    call process_character (n, appearance="blush false", text="{i}Уфф!{/i}")
    call process_character (sa, appearance="blush false", text="Да, это действительно работает!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Это довольно приятное чувство.")
    call process_character (julia, appearance="blush false", text="Я не думала, что это получится...")
    call process_character (sa, appearance="blush false", text="Я знаю, правильно?")
    call process_character (sa, appearance="blush false", text="Не похоже, что мы делаем что-то, но моя киска чувствует себя удивительно!")
    call process_character (julia, appearance="blush false", text="Ах...")
    call process_character (julia, appearance="blush false", text="И моя тоже.")
    call process_character (sa, appearance="blush false", text="Ха-ха, посмотри на [n.say_name]!")
    call process_character (sa, appearance="blush false", text="Он сидит сложа руки и принимает все это!")
    call process_character (n, appearance="blush false", text="Хмммм!")
    call process_character (n, appearance="blush false", text="(Мой член промокает от их трения!)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="([n.say_name] теперь является частью очень низкого процента мальчиков, которые участвуют в тройничке с двумя девушками...)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Он даже не знает, насколько ему повезло, что это произошло?)")
    call process_character (sa, appearance="blush false", text="Ах, да!")
    call process_character (sa, appearance="blush false", text="([julia.say_name] очень хороша в этом!)")
    call process_character (sa, appearance="blush false", text="(Бьюсь об заклад, она знает больше, чем я о сексе!)")
    call process_character (sa, appearance="blush false", text="(Я рада, что могу спросить ее об этом сейчас!)")
    call process_character (sa, appearance="blush false", text="([julia.say_name] получает огромный позитив!)")
    call process_character (n, appearance="blush false", text="Оох!")
    call process_character (n, appearance="blush false", text="([julia.say_name] и [sa.say_name] ладят лучше, чем я думал)")
    call process_character (n, appearance="blush false", text="(Я должен был понять, что нам всем понравилось бы сделать что-то подобное вместе!)")
    call process_character (julia, appearance="blush false", text="Ммм...")
    call process_character (julia, appearance="blush false", text="Я думаю, что пришло время [n.say_name] вставил нам, ты не думаешь, [sa.say_name]?")
    call process_character (sa, appearance="blush false", text="Вставил?")
    call process_character (sa, appearance="blush false", text="Ты имеешь ввиду...")
    call process_character (sa, appearance="blush false", text="Да, я думаю, что это справедливо!")
    call process_character (n, appearance="blush false", text="Хм?")
    call process_character (julia, appearance="blush false", text="Ты знаешь, чего мы хотим от тебя, [n.say_name].")
    call process_character (sa, appearance="blush false", text="Мы хотим, чтобы ты трахнул нас!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Ты должен быть в состоянии удовлетворить нас обеих.")
    call process_character (julia, appearance="blush false", text="Ты не можешь держать нас ждать слишком долго.")
    call process_character (sa, appearance="blush false", text="[julia.say_name] права!")
    call process_character (sa, appearance="blush false", text="Ты должен переключиться в любой момент!")

    call fade_to_black (1)

    call process_character (julia, appearance="blush false", text="Я займу позу по-собачьи.")
    call process_character (julia, appearance="blush false", text="Не нужно вдаваться в подробности.")
    call process_character (sa, appearance="blush false", text="Это хорошая идея, [julia.say_name]!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Эй, что ты...")

    call static_still_ctc ("bg julia_sam_group_stackup")

    call process_character (sa, appearance="blush false", text="Давай, [n.say_name]!")
    call process_character (sa, appearance="blush false", text="Теперь ты можете быстро переключаться между нами!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Она серьезно собирается сидеть на мне вот так?)")
    call process_character (julia, appearance="blush false", text="(Что я, лошадь?)")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="(Это ещё один сумасшедший способ трахаться...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Кто из вас хочет этого первым?")
    call process_character (sa, appearance="blush false", text="Это тебе решать, [n.say_name]!")
    call process_character (julia, appearance="blush false", text="Но убедись, что доберешься до нас обоих.")
    call process_character (n, appearance="blush false", text="У тебя получилось!")

    window hide
    menu:
        "Трахнуть [sa.say_name]":
            call static_still_ctc ("bg julia_sam_group_samfuck")

            call process_character (sa, appearance="blush false", text="Аахх!")
            call process_character (n, appearance="blush false", text="Твоя киска тугая, [sa.say_name]!")
            call process_character (sa, appearance="blush false", text="Вставь его быстрее, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Ох, ах!")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="([sa.say_name] крепко сжимает мои плечи)")
            call process_character (julia, appearance="blush false", text="([n.say_name] должно быть ей чертовски хорошо...)")
            call process_character (sa, appearance="blush false", text="{i}Уфф!{/i}")
            call process_character (sa, appearance="blush false", text="Да!")
            call process_character (n, appearance="blush false", text="Я достаточно быстро толкаю, [sa.say_name]?")
            call process_character (sa, appearance="blush false", text="Даа, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Мне нравится, когда ты так быстро двигаешься!")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="(Я могу чувствовать, что тело [sa.say_name] нагревается)")
            call process_character (julia, appearance="blush false", text="(И она тяжело дышит)")
            call process_character (n, appearance="blush false", text="Ах, ах!")
            call process_character (n, appearance="blush false", text="(Обычно я чувствую себя усталым после того, когда трахаюсь с [sa.say_name] и я уже сегодня...)")
            call process_character (n, appearance="blush false", text="(Но я чувствую себя энергичным и хочу продолжать!)")
            call process_character (n, appearance="blush false", text="(Я думаю, что трахаться сразу с [sa.say_name] и [julia.say_name] поднимает моё возбуждение!)")
            call process_character (julia, appearance="blush false", text="{i}Кхм.{/i}.")
            call process_character (julia, appearance="blush false", text="Можно уже меня?")
            call process_character (sa, appearance="blush false", text="О-ох...")
            call process_character (sa, appearance="blush false", text="Извини, [julia.say_name].")
            call process_character (sa, appearance="blush false", text="Я почти забыла, что ты прямо подо мной.")
            call process_character (sa, appearance="blush false", text="[n.say_name], [julia.say_name] нужно развернуться.")

            call static_still_ctc ("bg julia_sam_group_juliafuck")

            call process_character (n, appearance="blush false", text="Аах!")
            call process_character (n, appearance="blush false", text="Ты тоже узкая, [julia.say_name]!")
            call process_character (julia, appearance="blush false", text="Ооох...")
            call process_character (sa, appearance="blush false", text="Я думаю, ей это действительно нравится, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Ты должен нажать на ее киску еще немного!")
            call process_character (n, appearance="blush false", text="Х-хорошо!")
            call process_character (n, appearance="blush false", text="Ох, ах!")
            call process_character (julia, appearance="blush false", text="Хаа, чёрт!")
            call process_character (julia, appearance="blush false", text="Ммм!")
            call process_character (sa, appearance="blush false", text="Член [n.say_name] трётся внутри твоей киски?")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Д-да...")
            call process_character (sa, appearance="blush false", text="[n.say_name] двигайся быстрее в [julia.say_name]!")
            call process_character (sa, appearance="blush false", text="Я не могу описать, насколько это хорошо!")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Быстрее, [n.say_name].")

            call process_character (sa, appearance="blush false")

            call process_character (n, appearance="blush false", text="Мм, Мм!")
            call process_character (julia, appearance="blush false", text="{i}Вздох,{/i} {i}Вздох.{/i}.")
            call process_character (sa, appearance="blush false", text="...")
            call process_character (sa, appearance="blush false", text="(Это просто взрывная волна!)")
            call process_character (sa, appearance="blush false", text="(Я надеюсь, что [julia.say_name] захочет делать это до конца лета!)")
            call process_character (n, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="Я...я скоро кончу.")
            call process_character (sa, appearance="blush false", text="Ох, почти вовремя [julia.say_name]!")
            call process_character (sa, appearance="blush false", text="Ты хочешь быть той, кого заполнит [n.say_name] своей спермой?")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Для меня это не имеет значения...")
            call process_character (sa, appearance="blush false", text="Не имеет значения, да?")
            call process_character (sa, appearance="blush false", text="...")
            call process_character (sa, appearance="blush false", text="Как насчет того, что [n.say_name] выберет, в кого кончит?")
            call process_character (sa, appearance="blush false", text="[n.say_name], это все на тебя!")
        "Трахнуть [julia.say_name]":
            call static_still_ctc ("bg julia_sam_group_juliafuck")

            call process_character (n, appearance="blush false", text="Аах!")
            call process_character (n, appearance="blush false", text="Ты такая узкая, [julia.say_name]!")
            call process_character (julia, appearance="blush false", text="Ооох...")
            call process_character (sa, appearance="blush false", text="Я думаю, ей это действительно нравится, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Ты должен нажать на ее киску еще немного!")
            call process_character (n, appearance="blush false", text="Х-хорошо!")
            call process_character (n, appearance="blush false", text="Ох, ах!")
            call process_character (julia, appearance="blush false", text="Хаа, чёрт!")
            call process_character (julia, appearance="blush false", text="Ммм!")
            call process_character (sa, appearance="blush false", text="Вы чувствуете себя очень жарко [julia.say_name]!")
            call process_character (sa, appearance="blush false", text="Член [n.say_name] трётся внутри твоей киски?")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Д-да...")
            call process_character (sa, appearance="blush false", text="[n.say_name] двигайся быстрее в [julia.say_name]!")
            call process_character (sa, appearance="blush false", text="Я не могу описать, насколько это хорошо!")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Быстрее, [n.say_name].")
            call process_character (n, appearance="blush false", text="Мм, Мм!")
            call process_character (julia, appearance="blush false", text="{i}Вздох,{/i} {i}Вздох.{/i}.")
            call process_character (sa, appearance="blush false", text="...")
            call process_character (sa, appearance="blush false", text="([julia.say_name] отрывается!)")
            call process_character (sa, appearance="blush false", text="(Не могу дождаться своей очереди!)")
            call process_character (sa, appearance="blush false", text="(Он трахается быстрее, чем обычно!)")
            call process_character (julia, appearance="blush false", text="Хмммм!")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Я кончаю.")
            call process_character (sa, appearance="blush false", text="Может [n.say_name] трахнет уже меня, [julia.say_name]?")
            call process_character (julia, appearance="blush false", text="Д-давай вперед...")
            call process_character (sa, appearance="blush false", text="Да, спасибо!")

            call static_still_ctc ("bg julia_sam_group_samfuck")

            call process_character (sa, appearance="blush false", text="Аахх!")
            call process_character (sa, appearance="blush false", text="Вставь его быстрее, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Ох, ах!")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="([sa.say_name] крепко сжимает мои плечи)")
            call process_character (julia, appearance="blush false", text="([n.say_name] должно быть ей чертовски хорошо...)")
            call process_character (sa, appearance="blush false", text="{i}Уфф!{/i}")
            call process_character (sa, appearance="blush false", text="Да!")
            call process_character (n, appearance="blush false", text="Я достаточно быстро толкаю, [sa.say_name]?")
            call process_character (sa, appearance="blush false", text="Даа, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Мне нравится, когда ты так быстро двигаешься!")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="(Я могу чувствовать, что тело [sa.say_name] нагревается)")
            call process_character (julia, appearance="blush false", text="(И она тяжело дышит)")
            call process_character (n, appearance="blush false", text="Ах, ах!")
            call process_character (n, appearance="blush false", text="(Обычно я чувствую себя усталым после того, когда трахаюсь с [sa.say_name] и я уже сегодня...)")
            call process_character (n, appearance="blush false", text="(Но я чувствую себя энергичным и хочу продолжать!)")
            call process_character (n, appearance="blush false", text="(Я думаю, что трахаться сразу с [sa.say_name] и [julia.say_name] поднимает моё возбуждение!)")
            call process_character (n, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="Я...я скоро кончу.")
            call process_character (julia, appearance="blush false", text="И что?")
            call process_character (julia, appearance="blush false", text="В кого ты собираешься кончить?")
            call process_character (julia, appearance="blush false", text="У тебя есть предпочтения, [sa.say_name]?")
            call process_character (sa, appearance="blush false", text="Решай, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Он может выбирать!")
            call process_character (julia, appearance="blush false", text="Тогда ладно.")
            call process_character (julia, appearance="blush false", text="[n.say_name], похоже, вы тот, кто принимает решение.")

    window hide
    menu:
        "Кончить в [sa.say_name]":
            call static_still_ctc ("bg julia_sam_group_samfuck")

            call process_character (n, appearance="blush false", text="Я собираюсь кончить в тебя, [sa.say_name]!")
            call process_character (n, appearance="blush false", text="Будь готова к этому!")
            call process_character (sa, appearance="blush false", text="Ха, ах!")
            call process_character (sa, appearance="blush false", text="Я готова!")
            call process_character (sa, appearance="blush false", text="Я готова к этому, [n.say_name]!")
            call process_character (n, appearance="blush false", text="Аааах!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg julia_sam_group_samfuck_cum")

            call process_character (sa, appearance="blush false", text="Она течет прямо в меня!")
            call process_character (n, appearance="blush false", text="Хннг!")
            call process_character (julia, appearance="blush false", text="(Интересно, сколько спермы в киске [sa.say_name])")
            call process_character (sa, appearance="blush false", text="{i}Вздох,{/i} {i}Вздох.{/i}..")
            call process_character (n, appearance="blush false", text="Я не думал, что кончу так много снова...")
            call process_character (sa, appearance="blush false", text="Д-да...")
            call process_character (sa, appearance="blush false", text="Второй раз ты меня наполнил [n.say_name]!")

            call static_still_ctc ("bg julia_sam_group_stackup_samcum")

            call process_character (sa, appearance="blush false", text="Это было потрясающе весело!")
            call process_character (sa, appearance="blush false", text="Ты хорошо провела время, [julia.say_name]?")
            call process_character (julia, appearance="blush false", text="У меня никогда не было такого опыта, как этот.")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Однако это было хорошо.")
            call process_character (sa, appearance="blush false", text="В следующий раз будет еще лучше!")
            call process_character (sa, appearance="blush false", text="Я гарантирую это!")
            call process_character (n, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="Хочешь ли ты продолжить игру, [sa.say_name]?")
            call process_character (sa, appearance="blush false", text="Да!")
            call process_character (sa, appearance="blush false", text="Ты будешь смотреть [julia.say_name]?")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Конечно, я думаю, что могу.")
            call process_character (julia, appearance="blush false", text="Не возражаешь, если я прилягу на твою кровать, пока буду смотреть?")
            call process_character (sa, appearance="blush false", text="Ты устала от всего?")
            call process_character (sa, appearance="blush false", text="Это случается.")
        "Кончить в [julia.say_name]":
            call static_still_ctc ("bg julia_sam_group_juliafuck")

            call process_character (n, appearance="blush false", text="[julia.say_name]!")
            call process_character (n, appearance="blush false", text="Я собираюсь кончить в тебя!")
            call process_character (julia, appearance="blush false", text="Мм, Мм!")
            call process_character (julia, appearance="blush false", text="Я знаю, у тебя не будет проблем с этим...")
            call process_character (n, appearance="blush false", text="Аааах!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg julia_sam_group_juliafuck_cum")

            call process_character (julia, appearance="blush false", text="Аахх!")
            call process_character (n, appearance="blush false", text="Хннг!")
            call process_character (sa, appearance="blush false", text="[n.say_name] много выстрелил, не так ли?")
            call process_character (julia, appearance="blush false", text="Д-да...")
            call process_character (sa, appearance="blush false", text="Там обычно так много, что часть будет вытекать из киски!")
            call process_character (sa, appearance="blush false", text="Со мной такое постоянно случается!")

            call static_still_ctc ("bg julia_sam_group_stackup_juliacum")

            call process_character (n, appearance="blush false", text="{i}Фух.{/i}.")
            call process_character (sa, appearance="blush false", text="Да, я вижу!")
            call process_character (sa, appearance="blush false", text="Часть спермы [n.say_name] выходит из тебя, [julia.say_name]!")
            call process_character (julia, appearance="blush false", text="{i}Вздох.{/i}.")
            call process_character (sa, appearance="blush false", text="Ещё одна большая порция в один и тот же день, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Для тебя это первый раз?")
            call process_character (n, appearance="blush false", text="Я не знаю...")
            call process_character (n, appearance="blush false", text="Возможно.")
            call process_character (sa, appearance="blush false", text="Это было потрясающе весело!")
            call process_character (sa, appearance="blush false", text="Ты хорошо провела время, [julia.say_name]?")
            call process_character (julia, appearance="blush false", text="У меня никогда не было такого опыта, как этот.")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Однако это было хорошо.")
            call process_character (sa, appearance="blush false", text="В следующий раз будет еще лучше!")
            call process_character (sa, appearance="blush false", text="Я гарантирую это!")
            call process_character (n, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="Хочешь ли ты продолжить игру, [sa.say_name]?")
            call process_character (sa, appearance="blush false", text="Да!")
            call process_character (sa, appearance="blush false", text="Ты будешь смотреть [julia.say_name]?")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Конечно, я думаю, что могу.")
            call process_character (julia, appearance="blush false", text="Не возражаешь, если я прилягу на твою кровать, пока буду смотреть?")
            call process_character (sa, appearance="blush false", text="Ты устала от всего?")
            call process_character (sa, appearance="blush false", text="Я все понимаю!")
        "Кончить в обеих":
            call static_still_ctc ("bg julia_sam_group_samfuck")

            call process_character (n, appearance="blush false", text="Я хочу кончить в вас обеих!")
            call process_character (sa, appearance="blush false", text="В нас обеих, [n.say_name]?")
            call process_character (julia, appearance="blush false", text="Как ты собираешься это провернуть?")
            call process_character (n, appearance="blush false", text="Я не знаю, но хочу попробовать!")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Удачи.")
            call process_character (sa, appearance="blush false", text="Ах, ах!")
            call process_character (sa, appearance="blush false", text="Давай, [n.say_name]!")
            call process_character (n, appearance="blush false", text="Хаах...")
            call process_character (n, appearance="blush false", text="Ммм!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg julia_sam_group_samfuck_cum")

            call process_character (sa, appearance="blush false", text="Она течет прямо в меня!")
            call process_character (sa, appearance="blush false", text="Аххх!")
            call process_character (n, appearance="blush false", text="Хннг!")
            call process_character (sa, appearance="blush false", text="{i}Уфф!{/i}")
            call process_character (sa, appearance="blush false", text="Так много!")
            call process_character (julia, appearance="blush false", text="(Он начал кончать, прежде чем добрался до меня...)")
            call process_character (n, appearance="blush false", text="[julia.say_name]!")

            call static_still_ctc ("bg julia_sam_group_juliafuck_cum_samcum")

            call process_character (julia, appearance="blush false", text="Ааах, гах!")
            call process_character (julia, appearance="blush false", text="(Сколько спермы у [n.say_name]?)")
            call process_character (julia, appearance="blush false", text="(Моя киска наполняется!)")
            call process_character (n, appearance="blush false", text="Хууу!")
            call process_character (julia, appearance="blush false", text="{i}Вздох.{/i}.")
            call process_character (sa, appearance="blush false", text="{i}Фух.{/i}.")

            call static_still_ctc ("bg julia_sam_group_stackup_bothcum")

            call process_character (sa, appearance="blush false", text="Ты сделал это, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Ты действительно сделал это!")
            call process_character (sa, appearance="blush false", text="Ты кончил в нас обеих!")
            call process_character (julia, appearance="blush false", text="Я даже не знаю, что сказать...")
            call process_character (julia, appearance="blush false", text="Я думала, что это будет невозможно, [n.say_name].")
            call process_character (n, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="Я знал, что должен действовать быстро.")
            call process_character (n, appearance="blush false", text="И я думаю, я смог правильно рассчитать время.")
            call process_character (sa, appearance="blush false", text="Я не знаю, сколько спермы ты выстрелил, [n.say_name]...")
            call process_character (sa, appearance="blush false", text="Но это должно быть одна из самых больших порций!")
            call process_character (n, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="Может быть...")
            call process_character (julia, appearance="blush false", text="Учитывая, что с киски [sa.say_name] и моей капает сперма, это меня не удивляет.")
            call process_character (sa, appearance="blush false", text="Ну, это было потрясающе весело!")
            call process_character (sa, appearance="blush false", text="Ты хорошо провела время, [julia.say_name]?")
            call process_character (julia, appearance="blush false", text="У меня никогда не было такого опыта, как этот.")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Однако это было хорошо.")
            call process_character (sa, appearance="blush false", text="В следующий раз будет еще лучше!")
            call process_character (sa, appearance="blush false", text="Я гарантирую это!")
            call process_character (n, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="Хочешь ли ты продолжить игру, [sa.say_name]?")
            call process_character (sa, appearance="blush false", text="Да!")
            call process_character (sa, appearance="blush false", text="Ты будешь смотреть [julia.say_name]?")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Конечно, я думаю, что могу.")
            call process_character (julia, appearance="blush false", text="Не возражаешь, если я прилягу на твою кровать, пока буду смотреть?")
            call process_character (sa, appearance="blush false", text="Ты устала от всего?")
            call process_character (sa, appearance="blush false", text="Это случается.")

    call add_replayable_scene ("sam_julia_threesome_scene", julia)
    call add_replayable_scene ("sam_julia_threesome_scene", sa)

    python:
        sa.revistable_scenes.add("sam_julia_threesome_scene_revisit_sam")
        julia.revistable_scenes.add("sam_julia_threesome_scene_revisit_julia")

        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_sex", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_given_vaginal_creampie", 1)
            stats.add_stat("times_had_vaginal_sex", 1)
            stats.add_stat("times_had_paizuri", 1)
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_seen_flat_breasts", 1)
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_had_group_sex", 1)
            stats.add_stat("times_received_blowjob", 1)
            stats.add_stat("times_had_double_blowjob", 1)
            stats.add_stat("times_had_multi_blowjob", 1)

    call process_end_of_scene ("sam_julia_threesome_scene", dream=dream)

    return

label sam_julia_threesome_scene_revisit_sam:
    $ no_bust_art = False

    call process_character (n, appearance="pose twohandfist face happy")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Вообще-то, я спросила ее минуту назад.")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Она будет готова, когда мы будем готовы!")

    call sam_julia_threesome_scene_revisit

    return

label sam_julia_threesome_scene_revisit_julia:
    $ no_bust_art = False

    call process_character (n, appearance="pose handfist face neutral")
    call process_character (julia, appearance="pose handface face happy blush false", text="Если [sa.say_name] согласна, то я в игре.")
    call sam_julia_threesome_scene_revisit

    return

label sam_julia_threesome_scene_revisit:
    $ scenes_completed.add("sam_julia_threesome_scene_revisit_julia")
    $ scenes_completed.add("sam_julia_threesome_scene_revisit_sam")

    if "sam_julia_threesome_scene_revisit" in scenes_completed:
        call sam_julia_threesome_scene_revisit_2nd_time
    else:
        call sam_julia_threesome_scene_revisit_1st_time

    return

label sam_julia_threesome_scene_revisit_1st_time:
    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg julia_sam_group_grind")

    call process_character (julia, appearance="blush false", text="Ты когда-нибудь боялся, что тебя поймают?")
    call process_character (sa, appearance="blush false", text="Кто?")
    call process_character (julia, appearance="blush false", text="Твоя мама или твоя сестра.")

    if "sam_simone_threesome_scene" in scenes_completed and "sam_kira_threesome_scene" in scenes_completed:
        call process_character (sa, appearance="blush false", text="О, я совсем об этом не беспокоюсь!")
        call process_character (sa, appearance="blush false", text="Они знают, что [n.say_name] и я занимаемся сексом.")
        call process_character (julia, appearance="blush false", text="Да?")
        call process_character (sa, appearance="blush false", text="Да!")
        call process_character (sa, appearance="blush false", text="На самом деле, [n.say_name] и у меня был секс с [k.say_name] раньше, и с нашей мамой раньше!")
        call process_character (julia, appearance="blush false", text="Вы все трахаетесь друг с другом?!")

        if did_sam_simone_ff:
            call process_character (sa, appearance="blush false", text="Последний раз, когда [n.say_name] трахал маму, мы сосали ее сиськи!")
            call process_character (sa, appearance="blush false", text="Они огромные!")

        call process_character (sa, appearance="blush false", text="[n.say_name] трахает маму все время.")
        call process_character (sa, appearance="blush false", text="Практически каждый день!")
        call process_character (julia, appearance="blush false", text="...")
        call process_character (julia, appearance="blush false", text="(Черт, и я думала, что я безрассудная в сексе...)")

    elif "sam_simone_threesome_scene" in scenes_completed:
        call process_character (sa, appearance="blush false", text="О, я совсем об этом не беспокоюсь!")
        call process_character (sa, appearance="blush false", text="Наша мама знает, что [n.say_name] и я занимаюсь сексом.")
        call process_character (julia, appearance="blush false", text="Да?")
        call process_character (sa, appearance="blush false", text="Да!")
        call process_character (sa, appearance="blush false", text="На самом деле, [n.say_name] и у меня был секс с нашей мамой раньше!")
        call process_character (julia, appearance="blush false", text="Ты трахаешь свою маму, [n.say_name]?!")

        if did_sam_simone_ff:
            call process_character (sa, appearance="blush false", text="Последний раз, когда [n.say_name] трахал маму, мы сосали ее сиськи!")
            call process_character (sa, appearance="blush false", text="Они огромные!")
            call process_character (julia, appearance="blush false", text="...")

        call process_character (sa, appearance="blush false", text="Я слышу, как [n.say_name] трахает маму постоянно.")
        call process_character (sa, appearance="blush false", text="Практически каждый день!")
        call process_character (julia, appearance="blush false", text="...")
        call process_character (julia, appearance="blush false", text="(Черт, и я думала, что я безрассудная в сексе...)")

    elif "sam_kira_threesome_scene" in scenes_completed:
        call process_character (sa, appearance="blush false", text="О, я совсем об этом не беспокоюсь!")
        call process_character (sa, appearance="blush false", text="[k.say_name] знает, что [n.say_name] и я занимаемся сексом.")
        call process_character (julia, appearance="blush false", text="Да?")
        call process_character (sa, appearance="blush false", text="Да!")
        call process_character (sa, appearance="blush false", text="На самом деле, [n.say_name] и у меня был секс с [k.say_name] раньше!")
        call process_character (julia, appearance="blush false", text="Ты, трахаешь обеих сестёр, [n.say_name]?!")
        call process_character (sa, appearance="blush false", text="Я чувствую, как дрожит комната [k.say_name], когда [n.say_name] трахает ее.")
        call process_character (sa, appearance="blush false", text="Практически каждый день!")
        call process_character (julia, appearance="blush false", text="...")
        call process_character (julia, appearance="blush false", text="(Черт, и я думала, что я безрассудная в сексе...)")
    else:
        call process_character (sa, appearance="blush false", text="Если они узнают, у меня нет причин для беспокойства.")
        call process_character (sa, appearance="blush false", text="Наша мама очень хорошо разбирается в этих вещах.")
        call process_character (sa, appearance="blush false", text="[k.say_name] я думаю тоже.")
        call process_character (julia, appearance="blush false", text="...")
        call process_character (julia, appearance="blush false", text="(Черт, [sa.say_name] кажется уверена, что ее мама и старшая сестра будут поддерживать, что [n.say_name] её трахает...)")

    call process_character (sa, appearance="blush false", text="...")
    call process_character (sa, appearance="blush false", text="Я хотел снова занять эту позу.")
    call process_character (sa, appearance="blush false", text="В прошлый раз было весело!")
    call process_character (n, appearance="blush false", text="Хаах!")
    call process_character (julia, appearance="blush false", text="Как ты придумываешь все эти позы, [sa.say_name]?")
    call process_character (sa, appearance="blush false", text="Большое спасибо всему порно, что я смотрю.")
    call process_character (sa, appearance="blush false", text="Я запоминаю, что мне понравилось, а затем я пробую это с [n.say_name]!")
    call process_character (julia, appearance="blush false", text="Сколько порнухи ты смотришь?")
    call process_character (sa, appearance="blush false", text="Ой, я даже не знаю на данный момент.")
    call process_character (sa, appearance="blush false", text="По крайней мере, час или больше каждый день!")
    call process_character (n, appearance="blush false", text="Ох, ох!")
    call process_character (sa, appearance="blush false", text="Сколько секса у тебя было до [n.say_name]?")
    call process_character (julia, appearance="blush false", text="Я не знаю точное количество раз.")
    call process_character (julia, appearance="blush false", text="Я перебрала пару парней, так что секс должен был случиться.")
    call process_character (sa, appearance="blush false", text="У тебя уже были парни?")
    call process_character (sa, appearance="blush false", text="Я еще даже не думала об этом!")
    call process_character (julia, appearance="blush false", text="Это, как повезёт.")
    call process_character (julia, appearance="blush false", text="Я не тороплюсь с кем-то встречаться.")
    call process_character (julia, appearance="blush false", text="Честно говоря, тебе было бы лучше иметь [n.say_name] как парня.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (sa, appearance="blush false", text="Хм, я думаю, что сделаю это!")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Мы потерли наши киски о член [n.say_name] достаточно долго.")
    call process_character (julia, appearance="blush false", text="Давай заставим его трахнуть нас.")
    call process_character (sa, appearance="blush false", text="У меня нет возражений!")

    call static_still_ctc ("bg julia_sam_group_stackup")

    call process_character (sa, appearance="blush false", text="Как мы уложимся [n.say_name]?")
    call process_character (sa, appearance="blush false", text="Понял?")
    call process_character (julia, appearance="blush false", text="...")
    call process_character (julia, appearance="blush false", text="Ты серьезно только, что сказала это?")
    call process_character (sa, appearance="blush false", text="Это была прекрасная возможность для каламбура!")
    call process_character (julia, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (julia, appearance="blush false", text="За эту шутку ты должен трахнуть её второй.")
    call process_character (sa, appearance="blush false", text="Ну, [n.say_name] в конечном итоге решает это!")
    call process_character (sa, appearance="blush false", text="Кого ты выберешь первой, [n.say_name]?")

    $ sam_julia_threesome_scene_current_partner = julia
    window hide
    menu:
        "Выбрать [julia.say_name]":
            $ sam_julia_threesome_scene_current_partner = julia
            call static_still_ctc ("bg julia_sam_group_juliafuck")

            call process_character (julia, appearance="blush false", text="Ааа, да...")
            call process_character (n, appearance="blush false", text="Твоя киска сжимается на моем члене!")
            call process_character (julia, appearance="blush false", text="Мм...")
            call process_character (julia, appearance="blush false", text="Я знаю, что чувствую себя хорошо, [n.say_name].")
            call process_character (julia, appearance="blush false", text="Держи темп.")
            call process_character (sa, appearance="blush false", text="Не забывай обо мне, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Ты сказал, что моя киска напряжена, помнишь?")
        "Выбрать [sa.say_name]":
            $ sam_julia_threesome_scene_current_partner = sa
            call static_still_ctc ("bg julia_sam_group_samfuck")

            call process_character (sa, appearance="blush false", text="Ооох, вау!")
            call process_character (n, appearance="blush false", text="Мм, да!")
            call process_character (sa, appearance="blush false", text="Как-то чувствуется еще лучше, когда ты здесь, [julia.say_name]!")
            call process_character (sa, appearance="blush false", text="Я всё больше возбуждаюсь, когда ты смотришь на нас!")
            call process_character (sa, appearance="blush false", text="Ах, ахх!")
            call process_character (julia, appearance="blush false", text="Я хочу быть больше, чем просто зритель.")
            call process_character (julia, appearance="blush false", text="Моя киска также нуждается в твоём внимании, [n.say_name]!")


    jump sam_julia_threesome_scene_revisit_phase_2
    return

screen sam_julia_threesome_scene_choose_partner:
    vbox:
        xalign 0.98
        yalign 0.02
        spacing 30
        use main_menu_button(text="[julia.say_name]", action=Jump("sam_julia_threesome_scene_choose_julia"), enabled=sam_julia_threesome_scene_current_partner != julia)
        use main_menu_button(text="[sa.say_name]", action=Jump("sam_julia_threesome_scene_choose_sam"), enabled=sam_julia_threesome_scene_current_partner != sa)
        use main_menu_button(text="Продолжить", action=Jump("sam_julia_threesome_scene_revisit_phase_3"))


label sam_julia_threesome_scene_choose_julia:
    $ sam_julia_threesome_scene_current_partner = julia
    call static_still_ctc ("bg julia_sam_group_juliafuck")
    if "sam_julia_threesome_scene_revisit" not in scenes_completed:
        $ dice_roll = random.randint(1,3)

        if dice_roll == 1:
            call process_character (julia, appearance="blush false", text="{i}Вздох,{/i} {i}Вздох.{/i}..")
            call process_character (julia, appearance="blush false", text="Я только что получила второе дыхание!")
        elif dice_roll == 2:
            call process_character (julia, appearance="blush false", text="Хаа, ах!")
            call process_character (julia, appearance="blush false", text="(Я думаю, что он будет продолжать переключаться до тех пор, пока может держаться)")
            call process_character (julia, appearance="blush false", text="([n.say_name] хочет чувствовать обе наши киски!)")
        else:
            call process_character (julia, appearance="blush false", text="Ммм, Мм...")
            call process_character (julia, appearance="blush false", text="Ты нашёл правильное место, [n.say_name]...")
    else:

        $ dice_roll = random.randint(1,3)

        if dice_roll == 1:
            call process_character (julia, appearance="blush false", text="Да...{w=0.5} вот и всё...")
            call process_character (julia, appearance="blush false", text="Ахх!")
        elif dice_roll == 2:
            call process_character (julia, appearance="blush false", text="{i}Вздох.{/i}.")
            call process_character (julia, appearance="blush false", text="Я начинаю потеть.")
        else:
            call process_character (julia, appearance="blush false", text="Ох, ох...")
            call process_character (julia, appearance="blush false", text="Держись до конца, [n.say_name]!")

    jump sam_julia_threesome_scene_revisit_phase_2
    return

label sam_julia_threesome_scene_choose_sam:
    $ sam_julia_threesome_scene_current_partner = sa
    call static_still_ctc ("bg julia_sam_group_samfuck")
    if "sam_julia_threesome_scene_revisit" not in scenes_completed:
        $ dice_roll = random.randint(1,3)

        if dice_roll == 1:
            call process_character (sa, appearance="blush false", text="{i}Уфф!{/i}")
            call process_character (sa, appearance="blush false", text="Ты вставляешь так быстро, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Это меня удивило!")
        elif dice_roll == 2:
            call process_character (sa, appearance="blush false", text="Аааахх...")
            call process_character (sa, appearance="blush false", text="Знаешь ли ты, сколько раз ты переключался, [n.say_name]?")
            call process_character (sa, appearance="blush false", text="Я не могу сосредоточиться и сосчитать...")
        else:
            call process_character (sa, appearance="blush false", text="Ох, ох!")
            call process_character (sa, appearance="blush false", text="Трахай нас жёстче, [n.say_name]!")
    else:

        $ dice_roll = random.randint(1,3)

        if dice_roll == 1:
            call process_character (sa, appearance="blush false", text="Ммм!")
            call process_character (sa, appearance="blush false", text="Это лучше всего, [n.say_name]!")
        elif dice_roll == 2:
            call process_character (sa, appearance="blush false", text="Хаа!")
            call process_character (sa, appearance="blush false", text="Моя киска такая мокрая!")
        else:
            call process_character (sa, appearance="blush false", text="Продолжай, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="{i}Уфф!{/i}")

    jump sam_julia_threesome_scene_revisit_phase_2
    return

label sam_julia_threesome_scene_revisit_phase_2:
    window hide
    call screen sam_julia_threesome_scene_choose_partner
    return

label sam_julia_threesome_scene_revisit_phase_3:
    if "sam_julia_threesome_scene_revisit" not in scenes_completed:
        call process_character (sa, appearance="blush false", text="[n.say_name], когда ты собираешься кончить?")
        call process_character (n, appearance="blush false", text="Я не знаю...")
        call process_character (n, appearance="blush false", text="Очень скоро.")
        call process_character (sa, appearance="blush false", text="Давай ты закончишь по-другому!")
        call process_character (n, appearance="blush false", text="По-другому?")
        call process_character (sa, appearance="blush false", text="Да, да!")
        call process_character (sa, appearance="blush false", text="Я думаю, ты должен кончить нам в рот!")
        call process_character (n, appearance="blush false", text="Ты хочешь, чтобы я это сделал?")
        call process_character (julia, appearance="blush false", text="Мы сможем справиться, [n.say_name].")
        call process_character (sa, appearance="blush false", text="Конечно сможем!")
        call process_character (sa, appearance="blush false", text="И мы сделаем это одновременно!")

        call static_still_ctc ("bg julia_sam_group_blowjob_pre")

        call process_character (sa, appearance="blush false", text="Мммф...")
        call process_character (sa, appearance="blush false", text="Ты готова, [julia.say_name]?")
        call process_character (julia, appearance="blush false", text="Да.")
        call process_character (n, appearance="blush false", text="Хрм!")
        call process_character (sa, appearance="blush false", text="Ты на грани, [n.say_name]!")
        call process_character (julia, appearance="blush false", text="Он должен быть после всего, что он только что сделал.")
        call process_character (n, appearance="blush false", text="Ах...")
        call process_character (n, appearance="blush false", text="Т-ты права...")
        call process_character (sa, appearance="blush false", text="Приготовься к этому, [julia.say_name]!")
        call process_character (n, appearance="blush false", text="Я… {w=1.0}Я кончаю!")

        if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

        call static_still_ctc ("bg julia_sam_group_blowjob_cum")

        call process_character (sa, appearance="blush false", text="Посмотри, как он фонтанирует!")
        call process_character (julia, appearance="blush false", text="Ммм...")
        call process_character (n, appearance="blush false", text="Ннг!")
        call process_character (sa, appearance="blush false", text="Ой, часть выливается из моего рта!")
        call process_character (sa, appearance="blush false", text="Ты всё удержала, [julia.say_name]!")
        call process_character (n, appearance="blush false", text="Ооох...")
        call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
        call process_character (sa, appearance="blush false", text="Сколько ты получила, [julia.say_name]?")
        call process_character (sa, appearance="blush false", text="Много во рту!")
        call process_character (julia, appearance="blush false", text="У меня тоже хороший кусок.")
        call process_character (n, appearance="blush false", text="...{p}...")
        call process_character (n, appearance="blush false", text="Вы двое очень близки друг к другу.")
        call process_character (n, appearance="blush false", text="Если бы мой член не был между вами, вы бы целовались...")
        call process_character (julia, appearance="blush false", text="Это интересное наблюдение, [n.say_name].")
        call process_character (julia, appearance="blush false", text="...")
        call process_character (julia, appearance="blush false", text="Ты намекаешь, что хочешь, чтобы мы поцеловались?")
        call process_character (n, appearance="blush false", text="...")
        call process_character (sa, appearance="blush false", text="Ты хочешь, чтобы [julia.say_name] и я поцеловались, [n.say_name]?")
        call process_character (sa, appearance="blush false", text="Я сделаю это ради тебя!")

        menu:
            "Да! Устрой шоу!":
                $ did_sam_julia_ff = True
                call process_character (sa, appearance="blush false", text="О, я никогда раньше не целовала девушку!")
                call process_character (n, appearance="blush false", text="Я никогда не видел, чтобы две девушки целовались передо мной...")
                call process_character (julia, appearance="blush false", text="Не многие девушки сделали бы это ради парня.")
                call process_character (julia, appearance="blush false", text="Но ты исключение, [n.say_name].")
                call process_character (sa, appearance="blush false", text="Правда!")

                call static_still_ctc ("bg julia_sam_group_cumkiss_pre")

                call process_character (sa, appearance="blush false", text="Мм...")
                call process_character (n, appearance="blush false", text="(Уау...)")
                call process_character (n, appearance="blush false", text="...")
                call process_character (n, appearance="blush false", text="(На это стоит посмотреть!)")
                call process_character (n, appearance="blush false", text="(Это стоило того, чтобы попросить!)")
                call process_character (julia, appearance="blush false", text="Ммф...")
                call process_character (julia, appearance="blush false", text="Я чувствую сперму [n.say_name] во рту [sa.say_name]...")
                call process_character (sa, appearance="blush false", text="Надеюсь, ничего не выльется!")
                call process_character (julia, appearance="blush false", text="Держи свой рот на моем, и не будет.")
                call process_character (n, appearance="blush false", text="...")
                call process_character (julia, appearance="blush false", text="Тебе нравится смотреть на это, [n.say_name]?")
                call process_character (n, appearance="blush false", text="Я уверен, что да!")
                call process_character (n, appearance="blush false", text="...")
                call process_character (n, appearance="blush false", text="(Мой пенис твердый!)")
                call process_character (n, appearance="blush false", text="...")
                call process_character (n, appearance="blush false", text="(У меня такое чувство, что я должен кончить снова)")
                call process_character (n, appearance="blush false", text="(То, как они целуются, удивительно...)")
                call process_character (sa, appearance="blush false", text="[n.say_name], твой хер снова встал?")
                call process_character (sa, appearance="blush false", text="Не может быть!")
                call process_character (julia, appearance="blush false", text="Продолжай целовать меня [sa.say_name].")
                call process_character (julia, appearance="blush false", text="[n.say_name] полностью повернут на этом!")
                call process_character (sa, appearance="blush false", text="Мм, Ммф...")
                call process_character (n, appearance="blush false", text="Ах, ах!")
                call process_character (n, appearance="blush false", text="(Я не был уверен, что смогу кончить снова, но это произойдет!)")
                call process_character (n, appearance="blush false", text="Хнннг!")

                if persistent.enable_sex_sounds:
                    $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

                call static_still_ctc ("bg julia_sam_group_cumkiss_cum")

                call process_character (julia, appearance="blush false", text="(Так густо, как в последний раз!)")
                call process_character (sa, appearance="blush false", text="Оох!")

                call static_still_ctc ("bg julia_sam_group_cumkiss_aftercum")

                call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}Вздох.{/i}..")
                call process_character (julia, appearance="blush false", text="(Черт, [n.say_name] покрыл наши лица)")
                call process_character (sa, appearance="blush false", text="[julia.say_name], мы сделали так, что [n.say_name] кончил два раза в такой короткий срок!")
                call process_character (sa, appearance="blush false", text="Из нас получился отличный дуэт!")
                call process_character (julia, appearance="blush false", text="Хех...")
                call process_character (julia, appearance="blush false", text="Конечно.")
            "Может быть в следующий раз...":
                call process_character (julia, appearance="blush false", text="Тогда ладно.")
                call process_character (sa, appearance="blush false", text="Эй!")
                call process_character (sa, appearance="blush false", text="Почему бы нам не проглотить его сперму перед ним?")
                call process_character (julia, appearance="blush false", text="Я знаю, что он любит смотреть на это.")
                call process_character (n, appearance="blush false", text="...")
    else:
        menu:
            "Кончить в [julia.say_name]":
                if persistent.enable_sex_sounds:
                    $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

                call static_still_ctc ("bg julia_sam_group_juliafuck_cum")

                call process_character (n, appearance="blush false", text="Хннг!")
                call process_character (julia, appearance="blush false", text="Аах, чёрт!")
                call process_character (julia, appearance="blush false", text="Я возьму все это, [n.say_name]!")
                call process_character (sa, appearance="blush false", text="Мило, [julia.say_name]!")
                call process_character (sa, appearance="blush false", text="Ты наполнил до краев!")
            "Кончить в [sa.say_name]":
                if persistent.enable_sex_sounds:
                    $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

                call static_still_ctc ("bg julia_sam_group_samfuck_cum")

                call process_character (n, appearance="blush false", text="Хрмм!")
                call process_character (sa, appearance="blush false", text="У меня такое чувство!")
                call process_character (sa, appearance="blush false", text="Я заполнена, [n.say_name]!")
                call process_character (julia, appearance="blush false", text="...")
                call process_character (julia, appearance="blush false", text="Бьюсь об заклад, что часть будет капать на мою задницу.")

                if did_sam_julia_ff:
                    call process_character (sa, appearance="blush false", text="Э-это нормально...")
                    call process_character (sa, appearance="blush false", text="Я слижу её для тебя.")
            "Кончить в обеих":
                if persistent.enable_sex_sounds:
                    $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

                call static_still_ctc ("bg julia_sam_group_samfuck_cum")

                call process_character (n, appearance="blush false", text="Я собираюсь кончить в вас обеих снова!")
                call process_character (sa, appearance="blush false", text="Да!")
                call process_character (sa, appearance="blush false", text="Дай нам обеим!")

                call static_still_ctc ("bg julia_sam_group_juliafuck_cum_samcum")

                call process_character (n, appearance="blush false", text="Вот для тебя, [julia.say_name]!")
                call process_character (julia, appearance="blush false", text="Я чувствую, как я наполняюсь спермой...")
                call process_character (sa, appearance="blush false", text="Наполни ее до краев, [n.say_name]!")
            "Кончить на их лица, пока они целуются":
                $ did_sam_julia_ff = True
                call process_character (n, appearance="blush false", text="Можете поцеловать друг друга, пока я кончаю на ваши лицах?")

                call static_still_ctc ("bg julia_sam_group_kiss_pre")

                call process_character (sa, appearance="blush false", text="Ммм...")
                call process_character (julia, appearance="blush false", text="Покрой нас [n.say_name].")

                if persistent.enable_sex_sounds:
                    $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

                call static_still_ctc ("bg julia_sam_group_kiss_cum")

                call process_character (n, appearance="blush false", text="Ааах!")
                call process_character (sa, appearance="blush false", text="Там много, [julia.say_name]!")

                call static_still_ctc ("bg julia_sam_group_kiss_aftercum")

                call process_character (sa, appearance="blush false", text="...")
                call process_character (sa, appearance="blush false", text="Она теплая...")
                call process_character (julia, appearance="blush false", text="Давай я слижу её с твоего лица.")
            "Кончить им в рот":
                call static_still_ctc ("bg julia_sam_group_blowjob_pre")

                call process_character (julia, appearance="blush false", text="Вернемся к тому, с чего начали.")
                call process_character (sa, appearance="blush false", text="Это хорошо, чтобы закончить в наших ртах, [n.say_name]!")
                call process_character (sa, appearance="blush false", text="Я хочу этого!")

                if persistent.enable_sex_sounds:
                    $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

                call static_still_ctc ("bg julia_sam_group_blowjob_cum")

                call process_character (n, appearance="blush false", text="Оох!")
                call process_character (julia, appearance="blush false", text="Ммф...")
                call process_character (sa, appearance="blush false", text="...")
                call process_character (sa, appearance="blush false", text="{i}Глык!{/i}")
                call process_character (sa, appearance="blush false", text="Ах...")
                call process_character (sa, appearance="blush false", text="Разве его сперма на вкус не прекрасна, [julia.say_name]?")
                call process_character (julia, appearance="blush false", text="И нам есть что попробовать.")


    call sam_julia_threesome_scene_revisit_end
    return

label sam_julia_threesome_scene_revisit_2nd_time:
    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg julia_sam_group_blowjob_pre")

    call process_character (sa, appearance="blush false", text="Ты вернешься домой после окончания лета [julia.say_name]?")
    call process_character (julia, appearance="blush false", text="Да...")
    call process_character (julia, appearance="blush false", text="Будет скучно дома.")
    call process_character (julia, appearance="blush false", text="Я не знаю, что я буду делать, не в состоянии сосать хер [n.say_name].")
    call process_character (sa, appearance="blush false", text="Мы ни за что не позволим тебе так скучать!")
    call process_character (sa, appearance="blush false", text="Перейти от всего веселья, которое у нас сейчас, к нулю?")
    call process_character (sa, appearance="blush false", text="Я бы сошла с ума если бы это случилось со мной!")
    call process_character (julia, appearance="blush false", text="Я не с нетерпением жду этого.")
    call process_character (n, appearance="blush false", text="Почему бы нам не договориться, когда ты сможешь приезжать снова?")
    call process_character (n, appearance="blush false", text="Мы могли бы спланировать это заранее.")
    call process_character (sa, appearance="blush false", text="Отличная идея, [n.say_name]!")
    call process_character (sa, appearance="blush false", text="Мы могли бы планировать всё на год вперед, если бы хотели!")
    call process_character (sa, appearance="blush false", text="Я думаю, что [julia.say_name] должна посещать два раза в неделю, как минимум!")
    call process_character (julia, appearance="blush false", text="Так много всего нужно спланировать...")
    call process_character (sa, appearance="blush false", text="Но это стоит того, [julia.say_name]!")
    call process_character (sa, appearance="blush false", text="Не думаю, что это будет так сложно.")
    call process_character (sa, appearance="blush false", text="Мы можем настроить все на наших телефонах!")

    call static_still_ctc ("bg julia_sam_group_grind")

    call process_character (julia, appearance="blush false", text="Смотря на вас, я хочу, чтобы у меня был брат.")
    call process_character (julia, appearance="blush false", text="Я бы хотела трахаться с ним каждое утро перед школой.")
    call process_character (sa, appearance="blush false", text="Хаха!")
    call process_character (sa, appearance="blush false", text="[n.say_name], я знаю, что ты и я будем делать осенью!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (sa, appearance="blush false", text="Что если он все еще будет спать утром, а ты проснулась раньше него?")
    call process_character (julia, appearance="blush false", text="Это меня не остановит.")
    call process_character (julia, appearance="blush false", text="Я бы все равно отсосала бы ему или села на его член.")
    call process_character (julia, appearance="blush false", text="Он проснется, как только почувствует это.")
    call process_character (sa, appearance="blush false", text="Ха-ха, потрясающе!")
    call process_character (sa, appearance="blush false", text="Мне нравится ход твоих мыслей, [julia.say_name]!")

    $ sam_julia_threesome_scene_current_partner = None

    call static_still_ctc ("bg julia_sam_group_stackup")

    jump sam_julia_threesome_scene_revisit_phase_2

    return

label sam_julia_threesome_scene_revisit_end:

    python:
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_cummed_in_mouth", 1)
        stats.add_stat("times_received_blowjob", 1)
        stats.add_stat("times_had_group_sex", 1)

    call process_end_of_scene ("sam_julia_threesome_scene_revisit", reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label family_foursome_scene(dream=False):
    call family_foursome_scene_sex (dream=dream)

    return

label family_foursome_scene_sex(dream=False):
    call process_scene_beginning (bg="bg kitchen_daytime", char_tuple_array=[], dream=dream)

    call process_character (si, appearance="outfit clothes pose armunder face embarrassed blush false", text="...")
    call process_character (si, appearance="outfit clothes pose armunder face embarrassed blush false", text="(Что я буду делать в этой ситуации?)")
    call process_character (si, appearance="outfit clothes pose armunder face embarrassed blush false", text="...")
    call process_character (si, appearance="outfit clothes pose handsup face shocked blush false", text="(Как невозможна вероятность того, что [n.say_name] трахает [k.say_name], [sa.say_name], и меня?)")
    call process_character (si, appearance="outfit clothes pose handsup face shocked blush false", text="(И все это за короткий промежуток времени!)")
    call process_character (si, appearance="outfit clothes pose handsup face shocked blush false", text="...")
    call process_character (si, appearance="outfit clothes pose handsfront face curious blush false", text="(Секс может выйти из-под контроля в этот момент)")
    call process_character (si, appearance="outfit clothes pose handsfront face curious blush false", text="([n.say_name] и [sa.say_name] вероятно, уже думали, как будут трахаться в школе)")
    call process_character (si, appearance="outfit clothes pose handsfront face curious blush false", text="([k.say_name] конечно будет трахаться с [n.say_name] везде и всякий раз, когда она почувствует, что он готов)")
    call process_character (si, appearance="outfit clothes pose armunder face embarrassed blush false", text="(Просто совместное посещение ресторана вместе может стать проблемой!)")
    call process_character (si, appearance="outfit clothes pose armunder face embarrassed blush false", text="([n.say_name] уже щиплет мои соски через свитер всякий раз)")
    call process_character (si, appearance="outfit clothes pose armunder face embarrassed blush false", text="(Если он не делает этого, он подбрасывает мою грудь вверх и вниз руками...)")
    call process_character (si, appearance="outfit clothes pose armunder face embarrassed blush false", text="...")
    call process_character (si, appearance="outfit clothes pose handsup face curious blush false", text="(Но я знаю, что нужно держать такие вещи строго дома)")
    call process_character (si, appearance="outfit clothes pose handsup face curious blush false", text="([k.say_name] и [sa.say_name], я не уверена на их счёт)")
    call process_character (si, appearance="outfit clothes pose handsup face curious blush false", text="(Нам нужно прийти к взаимопониманию...)")

    $ replace_position = True
    call process_new_location ("bg living_room_daytime", dream=dream)
    $ sa.position = "right"
    $ si.position = "left"
    $ k.position = "right"
    $ display_multiple_characters([ (si, "outfit clothes pose handsfront face neutral blush false position left"), (k, "outfit clothes pose armcross face neutral blush false position right") ])

    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Что за семейное собрание, Мама?")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false position right", text="Да, почему нет [n.say_name]?")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Потому что нам нужно поговорить о нём, [sa.say_name].")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Многое изменилось за то короткое время, что мы живём в этом новом доме.")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Но не такое большое, как то, что мы делали с [n.say_name].")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Ты говоришь о том, как мы с ним трахаемся?")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Ты трахаешься с [n.say_name] тоже, [sa.say_name]?")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="Так точно, Сестрёнка!")
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="Ха, спасибо!")
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="...")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Подожди, ты трахаешься с [n.say_name], [k.say_name]?")
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="О, да!")
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="Я удивлена, что его яйца еще не отсохли без всей спермы, которую я высосала!")
    call process_character (si, appearance="outfit clothes pose handsfront face embarrassed blush false")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Я люблю ореховое масло [n.say_name]!")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="Ха-ха, ореховое масло!")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="Черт возьми, я запомню эти словечки!")
    call process_character (si, appearance="outfit clothes pose armunder face concerned blush false", text="[sa.say_name], [k.say_name] пожалуйста!")
    call process_character (si, appearance="outfit clothes pose armunder face concerned blush false", text="Я хочу серьезно поговорить об этом.")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Почему?")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Мы все знаем, что мы делаем с [n.say_name].")
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="И я не слышу, чтобы он жаловался!")
    call process_character (sa, appearance="outfit clothes pose handface face embarrassed blush false", text="Ты же не собираешься сказать нам остановиться, Мама?!")
    call process_character (sa, appearance="outfit clothes pose handface face embarrassed blush false", text="Я сделаю все, чтобы продолжать трахаться с [n.say_name]!")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Нет, я не собираюсь говорить тебе перестать трахаться с [n.say_name].")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Не волнуйся.")
    call process_character (sa, appearance="outfit clothes pose handface face concerned blush false", text="{i}Фух.{/i}..")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Но я не хочу, чтобы это было публично.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face concerned blush false", text="А?")
    call process_character (sa, appearance="outfit clothes pose handsbehind face concerned blush false", text="Что значит публично?")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Мама не хочет, чтобы [n.say_name] вторгался в наши киски в торговом центре или парке.")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Или в школе, или где-нибудь за порогом этого дома.")
    call process_character (sa, appearance="outfit clothes pose handface face embarrassed blush false", text="О, никакого секса в школе, Мама?")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="Пока она не узнает...")
    call process_character (si, appearance="outfit clothes pose armunder face angry blush false", text="[k.say_name]!")
    call process_character (si, appearance="outfit clothes pose armunder face angry blush false", text="Нет, никакого секса в школе.")
    call process_character (si, appearance="outfit clothes pose armunder face concerned blush false", text="Я не хочу, чтобы мне позвонили и сказали, что ты сосешь хер [n.say_name] во время учебы.")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Эх, непруха, [sa.say_name].")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Я все время трахалась в школе.")
    call process_character (si, appearance="outfit clothes pose handsup face embarrassed blush false", text="И это было достаточно сложно!")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Итаак... пока я трахаюсь с [n.say_name] здесь, дома, все в порядке?")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Ты можешь сделать это прямо у двери, когда вернешься домой, если хочешь.")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="А как насчет в бассейне, Мама?")

    if "kira_scene_pool_fuck" in scenes_completed:
        call process_character (si, appearance="pose armunder face neutral blush false", text="{i}Вздох.{/i}..")
        call process_character (si, appearance="pose armunder face neutral blush false", text="Я знаю, ты просто проигнорируешь меня, если я скажу тебе не делать этого...")
        call process_character (si, appearance="pose armunder face neutral blush false", text="Так что да, вы можете трахаться на заднем дворе, так как он огорожен.")
        call process_character (k, appearance="pose handhip face happy blush false", text="Это все, что мне нужно было услышать!")
        call process_character (si, appearance="pose handsup face neutral blush false", text="Но постарайся не шуметь.")
        call process_character (si, appearance="pose handsup face embarrassed blush false", text="На днях я слышала, как ты хлопаешь по заднице [n.say_name] из кухни!")
    else:
        call process_character (si, appearance="pose armunder face neutral blush false", text="{i}Вздох.{/i}..")
        call process_character (si, appearance="pose armunder face neutral blush false", text="Да, ты можешь трахаться на заднем дворе, так как он огорожен.")
        call process_character (si, appearance="pose armunder face neutral blush false", text="Но постарайтесь не шуметь.")
        call process_character (k, appearance="pose handhip face happy blush false", text="Это все, что мне нужно было услышать!")

    call process_character (si, appearance="outfit clothes pose handsfront face curious blush false", text="Итак, мы все согласны?")
    call process_character (si, appearance="outfit clothes pose handsfront face curious blush false", text="Секс с [n.say_name] ограничивается домом.")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Да, я могу сделать это, Мама!")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Меня устраивает.")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Отлично.")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Я рада это слышать!")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="...")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Мне тоже было интересно...")
    call process_character (si, appearance="outfit clothes pose armunder face curious blush false", text="Как часто вы двое трахаетесь с [n.say_name]?")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Каждый день!")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Да, так же.")
    call process_character (si, appearance="outfit clothes pose armunder face shocked blush false", text="Каждый день?")
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="Ну, иногда два раза в день, если первый был достаточно рано.")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Я просто трахаюсь с [n.say_name] всякий раз, когда возбуждена.")
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="Что и происходит большую часть времени.")
    call process_character (si, appearance="outfit clothes pose handsfront face curious blush false", text="Кажется, ему с этим очень трудно справиться...")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Мы можем разделить дни, Мама!")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Я могу трахаться с ним по понедельникам, средам и субботам!")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Нет, мне нужен [n.say_name] чаще.")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Как насчет того, чтобы установить ежедневное расписание?")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="Я ранняя пташка, поэтому я получаю утренние \"стояки\" [n.say_name].")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Ох, ох!")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Я выбираю время обеда и ранний вечер!")
    call process_character (si, appearance="outfit clothes pose handsup face curious blush false", text="Держитесь, вы двое.")
    call process_character (si, appearance="outfit clothes pose handsup face curious blush false", text="Это безумие.")
    call process_character (si, appearance="outfit clothes pose handsup face curious blush false", text="У [n.say_name] не будет времени на себя.")
    call process_character (si, appearance="outfit clothes pose handsup face curious blush false", text="Нам нужно придумать что-то получше.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Что, Мама?")
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Хм...")
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="У меня есть идея, что делать...")

    call process_new_location ("bg nate_room_daytime", dream=dream)


    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="{i}Зевает.{/i}..")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="(Это был хороший сон)")
    call process_character (n, appearance="outfit clothes pose behindhead face neutral blush false", text="(Я проголодался и хочу перекусить...)")
    call process_character (n, appearance="outfit clothes pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="(Я мог бы пойти за сыром и крекерами!)")
    call process_character (n, appearance="outfit clothes pose twohandfist face happy blush false", text="(Я надеюсь, что они есть на кухне!)")


    call process_new_location ("bg hallway_daytime", dream=dream)

    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="...")
    call process_character (sa, appearance="outfit nude pose handsbehind face neutral blush false", text="Привет, [n.say_name]!")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="Ох, доброе утро, [sa.say_name].")
    call process_character (sa, appearance="outfit nude pose handface face neutral blush false", text="Что делаешь?")
    call process_character (n, appearance="outfit clothes pose handfist face neutral blush false", text="Я иду на кухню, чтобы перекусить.")
    call process_character (sa, appearance="outfit nude pose handface face neutral blush false", text="Не возражаешь, если я пойду с тобой?")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="Конечно, но...")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="Ты голая.")
    call process_character (sa, appearance="outfit nude pose leaning face happy blush false", text="Не думаю, что это будет проблемой.")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="Если ты так говоришь.")


    call process_new_location ("bg living_room_daytime", dream=dream)

    $ sa.position = "left"
    $ si.position = "left"
    $ k.position = "left"
    $ display_multiple_characters([ (n, "outfit clothes pose handsdown face neutral blush false"), (k, "outfit nude pose handhip face neutral blush false") ])


    call process_character (k, appearance="outfit nude pose handhip face neutral blush false", text="Привет, бро, привет, сестрёнка.")
    call process_character (sa, appearance="outfit nude pose handsbehind face neutral blush false", text="Привет, [k.say_name]!")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="...")
    call process_character (k, appearance="outfit nude pose armcross face neutral blush false", text="Вы двое пойдёте в бассейн потом?")
    call process_character (sa, appearance="outfit nude pose handface face curious blush false", text="Хм, возможно...")
    call process_character (k, appearance="outfit nude pose armcross face happy blush false", text="Я думаю, тебе нужно будет остыть после всех этих... {w=0.5}действий, которые мы будем делать.")
    call process_character (sa, appearance="outfit nude pose handface face happy blush false", text="О, да, это правда!")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="(Ни одну из них, кажется, не заботит, что они голые прямо сейчас...)")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="(Они не боятся, что мама может их увидеть?)")
    call process_character (k, appearance="outfit nude pose handhip face neutral blush false", text="Куда ты собрался, бро?")
    call process_character (sa, appearance="outfit nude pose leaning face neutral blush false", text="[n.say_name] хочет взять вкусности на кухне.")
    call process_character (k, appearance="outfit nude pose handhip face neutral blush false", text="А, понятно.")
    call process_character (k, appearance="outfit nude pose armsup face neutral blush false", text="Зарядиться энергией!")
    call process_character (k, appearance="outfit nude pose armsup face happy blush false", text="Она тебе понадобится!")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="(Мне она понадобится?)")

    call process_new_location ("bg kitchen_daytime", dream=dream)

    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="(Так, посмотрим...)")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="Привет, Мам!")
    call process_character (si, text="Да, [n.say_name]?")
    call process_character (n, appearance="outfit clothes pose behindhead face neutral blush false", text="Ты не знаешь, у нас есть сыр или крекеры?")
    call process_character (si, appearance="outfit nude pose handsfront face neutral blush false", text="Я думаю, что есть.")
    call process_character (si, appearance="outfit nude pose handsfront face neutral blush false", text="Я посмотрю.")
    call process_character (n, appearance="outfit clothes pose twohandfist face embarrassed blush false", text="М-Мама?!")
    call process_character (si, appearance="outfit nude pose armunder face neutral blush false", text="Хм, что случилось, милый?")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="...{p}...")
    call process_character (si, appearance="outfit nude pose armunder face happy blush false", text="Вот держи!")
    call process_character (si, appearance="outfit nude pose handsup face happy blush false", text="Сыр чеддер и немного соленых крекеров!")
    call process_character (si, appearance="outfit nude pose handsup face neutral blush false", text="Хочешь что-нибудь выпить?")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="Э...")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="У нас есть сладкий чай?")
    call process_character (si, appearance="outfit nude pose handsfront face curious blush false", text="Я думаю, мы он закончился.")
    call process_character (si, appearance="outfit nude pose handsfront face neutral blush false", text="Как насчет виноградного сока?")
    call process_character (si, appearance="outfit nude pose handsfront face neutral blush false", text="Он должен хорошо сочетаться с сыром!")
    call process_character (n, appearance="outfit clothes pose handsdown face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothes pose handsdown face concerned blush false", text="Да, я бы с удовольствием.")
    call process_character (si, appearance="outfit nude pose handsup face neutral blush false", text="Давай я принесу тебе тарелку...")

    call character_leave_dissolve (si)

    call process_character (n, appearance="outfit clothes pose behindhead face concerned blush false", text="(Мама тоже раздета?)")
    call process_character (n, appearance="outfit clothes pose behindhead face concerned blush false", text="(Она тоже кажется безучастной...)")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="(Что происходит?)")
    call process_character (si, appearance="outfit nude pose armunder face happy blush false", text="Вот, держи.")
    call process_character (si, appearance="outfit nude pose armunder face happy blush false", text="Полная тарелка для тебя, чтобы пожевать!")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="Спасибо, Мам.")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="Но я не думаю, что смогу съесть все это...")
    call process_character (si, appearance="outfit nude pose handsup face neutral blush false", text="Ты должен принести еду в гостиную, чтобы поделиться с сёстрами.")
    call process_character (si, appearance="outfit nude pose handsup face neutral blush false", text="Я уверен, что они будут наслаждаться этим!")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="Хорошо.")

    call process_new_location ("bg living_room_daytime", dream=dream)
    $ sa.position = "left"
    $ si.position = "left"
    $ k.position = "left"
    $ display_multiple_characters([ (n, "outfit clothes pose handsdown face neutral blush false"), (sa, "outfit nude pose handface face happy blush false") ])

    call process_character (sa, appearance="outfit nude pose handface face happy blush false", text="Сыр ооочень вкусный!")
    call process_character (k, appearance="outfit nude pose handhip face neutral blush false", text="Я признаю, что он ничего.")
    call process_character (k, appearance="outfit nude pose handhip face neutral blush false", text="Простой, но удовлетворительный.")
    call process_character (si, appearance="outfit nude pose handsfront face neutral blush false", text="Вы все насладились едой?")
    call process_character (sa, appearance="outfit nude pose leaning face neutral blush false", text="Купи побольше этого, Мама!")
    call process_character (sa, appearance="outfit nude pose leaning face happy blush false", text="Сыр чеддер - мой любимый!")
    call process_character (si, appearance="outfit nude pose handsup face neutral blush false", text="Тебе это понравилось, [n.say_name]?")
    call process_character (n, appearance="outfit clothes pose handfist face neutral blush false", text="Да, это замечательно.")
    call process_character (n, appearance="outfit clothes pose handfist face neutral blush false", text="Я бы предпочел его другим закускам.")
    call process_character (si, appearance="outfit nude pose handsup face happy blush false", text="Я куплю его столько, сколько необходимо!")
    call process_character (n, appearance="outfit clothes pose handsdown face neutral blush false", text="...{p}...")
    call process_character (k, appearance="outfit nude pose armcross face neutral blush false", text="Ладно, хватит болтать.")
    call process_character (k, appearance="outfit nude pose armcross face neutral blush false", text="Давайте перейдем к делу и скажем [n.say_name], что мы будем делать здесь.")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="Хм?")
    call process_character (si, appearance="outfit nude pose armunder face neutral blush false", text="Ну, милый...")
    call process_character (si, appearance="outfit nude pose armunder face neutral blush false", text="Мы знаем, что этим летом ты многое узнал о себе.")
    call process_character (k, appearance="outfit nude pose armsup face happy blush false", text="Да, он обнаружил, что его член идеально вписывается в мою задницу!")
    call process_character (sa, appearance="outfit nude pose handface face happy blush false", text="И мою киску!")
    call process_character (n, appearance="outfit clothes pose behindhead face embarrassed blush false", text="...")
    call process_character (si, appearance="outfit nude pose handsup face neutral blush false", text="Что мы хотим сказать...")
    call process_character (si, appearance="outfit nude pose handsup face neutral blush false", text="Тебе не нужно беспокоиться о том, кого ты должен трахнуть.")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false")
    call process_character (si, appearance="outfit nude pose handsup face neutral blush false", text="Это твоё решение, кого ты предпочитаешь изо дня в день.")
    call process_character (k, appearance="outfit nude pose armsup face happy blush false", text="Подсказка-Подсказка, выбери меня...")
    call process_character (si, appearance="outfit nude pose handsup face concerned blush false", text="[k.say_name]...")
    call process_character (k, appearance="outfit nude pose handhip face neutral blush false", text="Я пошутила.")
    call process_character (n, appearance="outfit clothes pose handsdown face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothes pose handsdown face concerned blush false", text="Так ты не будешь ругаться с тем, с кем я захочу заняться сексом?")
    call process_character (sa, appearance="outfit nude pose handsbehind face neutral blush false", text="Ага!")
    call process_character (sa, appearance="outfit nude pose handsbehind face neutral blush false", text="Хотя, если ты можешь трахать каждую из нас одинаково, это было бы здорово!")
    call process_character (si, appearance="outfit nude pose handsfront face neutral blush false", text="Но мы понимаем, что это будет трудно для тебя.")
    call process_character (si, appearance="outfit nude pose handsfront face neutral blush false", text="Так что, если тебе нужен перерыв, мы поймем.")
    call process_character (si, appearance="outfit nude pose handsfront face neutral blush false", text="Тебе это кажется выполнимым?")
    call process_character (n, appearance="outfit clothes pose twohandfist face neutral blush false", text="Да!")
    call process_character (n, appearance="outfit clothes pose twohandfist face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothes pose behindhead face neutral blush false", text="Но у меня есть вопрос.")
    call process_character (si, appearance="outfit nude pose armunder face neutral blush false", text="Да?")
    call process_character (n, appearance="outfit clothes pose behindhead face neutral blush false", text="Почему вы все сейчас голые?")
    call process_character (k, appearance="outfit nude pose armcross face happy blush false", text="...")
    call process_character (sa, appearance="outfit nude pose handsbehind face happy blush false", text="...")
    call process_character (n, appearance="outfit clothes pose behindhead face curious blush false", text="...")
    call process_character (si, appearance="outfit nude pose armunder face flirt blush false", text="Мы хотели предложить тебе другой вариант.")
    call process_character (si, appearance="outfit nude pose armunder face flirt blush false", text="И тебе это может понравиться.")
    call process_character (k, appearance="outfit nude pose handhip face neutral blush false", text="Может понравится?")
    call process_character (k, appearance="outfit nude pose handhip face happy blush false", text="Я знаю, тебе понравится!")
    call process_character (sa, appearance="outfit nude pose leaning face happy blush false", text="Ты можешь трахнуть каждую из нас, всех за один раз!")
    call process_character (n, appearance="outfit clothes pose twohandfist face embarrassed blush false", text="К-каждую из вас?")
    call process_character (k, appearance="outfit nude pose armsup face neutral blush false", text="Ну, повеяло тройничком на тебя, [n.say_name].")
    call process_character (k, appearance="outfit nude pose armsup face happy blush false", text="Просто добавь еще одну девушку в уравнение!")
    call process_character (si, appearance="outfit nude pose handsup face neutral blush false", text="Не дави на него, [k.say_name].")
    call process_character (si, appearance="outfit nude pose handsup face neutral blush false", text="Это решение [n.say_name].")
    call process_character (sa, appearance="outfit nude pose handface face neutral blush false", text="Прими правильное решение, [n.say_name]!")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="...{p}...")
    call process_character (n, appearance="outfit clothes pose handsdown face curious blush false", text="(Маму, [k.say_name] и [sa.say_name] всех сразу?)")
    call process_character (n, appearance="outfit clothes_hard pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit clothes_hard pose behindhead face curious blush false", text="(Смогу ли я вообще справиться с этим?)")
    call process_character (n, appearance="outfit clothes_hard pose behindhead face curious blush false", text="...{p}...")
    call process_character (n, appearance="outfit clothes_hard pose twohandfist face happy blush false", text="(Я думаю, я воспользуюсь своим шансом!)")

    call character_leave_dissolve (n)
    call process_character (n, appearance="outfit nudehard pose handsdown face happy blush false")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call process_character (k, appearance="outfit nude pose armsup face happy blush false", text="Молодец, [n.say_name]!")
    call process_character (sa, appearance="outfit nude pose leaning face happy blush false", text="Уррра, [n.say_name]!")
    call process_character (si, appearance="outfit nude pose handsup face happy blush false", text="Буду считать, что это да!")
    call process_character (n, appearance="outfit nudehard pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit nudehard pose handsdown face neutral blush false", text="С чего мы должны начать?")
    call process_character (si, appearance="outfit nude pose armunder face neutral blush false", text="...")
    call process_character (si, appearance="outfit nude pose armunder face neutral blush false", text="[k.say_name], [sa.say_name]...")
    call process_character (si, appearance="outfit nude pose armunder face neutral blush false", text="Готовы ли вы дать минет [n.say_name]?")
    call process_character (k, appearance="outfit nude pose armcross face flirt blush false", text="Да.")
    call process_character (sa, appearance="outfit nude pose handsbehind face flirt blush false", text="Совершенно верно!")
    call process_character (si, appearance="outfit nude pose handsfront face flirt blush false", text="Тогда у нас есть отправная точка!")
    call process_character (si, appearance="outfit nude pose handsfront face flirt blush false", text="[n.say_name], кто отсосёт тебе в первую очередь?")
    window auto
    $ family_foursome_bj_available_choices = ["kira", "sam", "simone"]
    call family_foursome_bj_choice (1, dream=dream)


    return

label family_foursome_bj_choice(family_foursome_choice_time, dream=False):
    window auto
    menu:
        "[k.say_name]" if "kira" in family_foursome_bj_available_choices:
            call family_foursome_kira_bj (family_foursome_choice_time, dream=dream)
        "[sa.say_name]" if "sam" in family_foursome_bj_available_choices:
            call family_foursome_sam_bj (family_foursome_choice_time, dream=dream)
        "Мама" if "simone" in family_foursome_bj_available_choices:
            call family_foursome_simone_bj (family_foursome_choice_time, dream=dream)

    return

label family_foursome_phase_2(dream=False):
    call process_character (si, appearance="blush false", text="Ты доволен, [n.say_name]?")
    call process_character (si, appearance="blush false", text="Мы все хорошо поработали?")
    call process_character (n, appearance="blush false", text="О-ох, да...")
    call process_character (n, appearance="blush false", text="...")

    call process_character (k, appearance="blush false", text="Теперь, когда твой член весь вылизан, пришло время отплатить тебе тем же...")
    call process_character (k, appearance="blush false", text="Ложись на спину, бро... Я требую, чтобы твой член был направлен прямо вверх!")

    if kira_simone_threesome_part_2_done:
        call static_still_ctc ("bg foursome_kirafuck")

        call process_character (k, appearance="blush false", text="Мм, о да...")
        call process_character (k, appearance="blush false", text="Не возражаешь, если я сделаю это, Мама?")
        call process_character (si, appearance="blush false", text="Я думаю, ты уже приняла это решение, ха-ха!")
        call process_character (k, appearance="blush false", text="Лучше просить прощения, чем разрешения.")
        call process_character (n, appearance="blush false", text="Хах, ах, ах!")
        call process_character (k, appearance="blush false", text="Тебе понравилась эта позиция в последний раз, когда мы это делали, [n.say_name]!")
        call process_character (sa, appearance="blush false", text="Я чувствую, как дрожит пол от того, как [k.say_name] подпрыгивает вверх и вниз на члене [n.say_name]!")
        call process_character (si, appearance="blush false", text="Когда я впервые увидела твою старшую сестру, делающую это с твоим братом, я была уверен, что он будет раздавлен!")
        call process_character (si, appearance="blush false", text="Я ожидала, что мне придется счищать его с пола, ха-ха!")
        call process_character (k, appearance="blush false", text="[n.say_name] много тренируется со мной.")
        call process_character (k, appearance="blush false", text="Я могу надавить на него всем своим весом, а он принимает это как чемпион!")
        call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
        call process_character (sa, appearance="blush false", text="Я практиковалась с [n.say_name] тоже!")
        call process_character (sa, appearance="blush false", text="Мы оба теперь способны трахаться играя в видеоигры!")
        call process_character (sa, appearance="blush false", text="Я когда-то сосала ему, пока проходили Демон Может Смеяться!")
        call process_character (k, appearance="blush false", text="[n.say_name] это битва закалила его для секса, ха!")
        call process_character (k, appearance="blush false", text="И тебе нужно быть таким, бро!")
        call process_character (si, appearance="blush false", text="Похоже, вы двое давите на [n.say_name] до предела!")
        call process_character (k, appearance="blush false", text="Ты тоже, Мама, я видела, на что ты способна!")
        call process_character (si, appearance="blush false", text="Шшш, ха-ха!")
        call process_character (k, appearance="blush false", text="Почему бы тебе не попробовать, Мама?")
        call process_character (k, appearance="blush false", text="Присаживайся на хер [n.say_name]!")
        call process_character (si, appearance="blush false", text="Ох, можно?")
        call process_character (k, appearance="blush false", text="Я чувствую, как его член дергается в моем влагалище.")
        call process_character (k, appearance="blush false", text="[n.say_name] хочет, чтобы ты сидела на нем.")
        call process_character (n, appearance="blush false", text="Д-да... Мама...")
        call process_character (n, appearance="blush false", text="Я хочу этого, ах... {w=1.0}я хочу трахнуть тебя.")
        call process_character (k, appearance="blush false", text="Я же говорила.")
        call process_character (k, appearance="blush false", text="Бро вызывает свою Мамочку!")
        call process_character (sa, appearance="blush false", text="Хаха!")
        call process_character (sa, appearance="blush false", text="Давай, Мама, сделай это!")
        call process_character (sa, appearance="blush false", text="Чёрт, [n.say_name]!")
        call process_character (si, appearance="blush false", text="Думаю, теперь все внимание сосредоточено на мне!")

        call static_still_ctc ("bg foursome_simonefuck")

        call process_character (n, appearance="blush false", text="О, Мама!")
        call process_character (si, appearance="blush false", text="Ммм!")
        call process_character (si, appearance="blush false", text="Да, милый!")
        call process_character (k, appearance="blush false", text="Круто, [n.say_name]!")
        call process_character (k, appearance="blush false", text="Толкай свой член до упора!")
        call process_character (k, appearance="blush false", text="Пусть мама почувствует каждый твой дюйм!")
        call process_character (sa, appearance="blush false", text="Делай, как говорит [k.say_name], [n.say_name]!")
        call process_character (sa, appearance="blush false", text="Трахни Маму, как сумасшедший!")
        call process_character (n, appearance="blush false", text="Аах...")
        call process_character (n, appearance="blush false", text="Твоя задница такая мягкая, Мама.")
        call process_character (k, appearance="blush false", text="Она большая и круглая, как хорошо!")
        call process_character (k, appearance="blush false", text="И она прямо над тобой, ха-ха!")
        call process_character (si, appearance="blush false", text="Ты так хорошо справляешься с этим, [n.say_name]!")
        call process_character (si, appearance="blush false", text="Ты проделал такой долгий путь с тех пор, как я впервые увидела тебя мастурбирующим в ванной!")
        call process_character (k, appearance="blush false", text="Точно, мама видела твою первую дрочку!")
        call process_character (k, appearance="blush false", text="Хотела бы я быть там, чтобы увидеть выражение ваших лиц!")
        call process_character (sa, appearance="blush false", text="Это было еще до того, как я узнала, что такое сперма!")
        call process_character (sa, appearance="blush false", text="Теперь я не могу представить жизнь без неё!")
        call process_character (si, appearance="blush false", text="Оох, оох, да!")
        call process_character (si, appearance="blush false", text="[n.say_name] стал настоящим мужчиной в доме!")
        call process_character (k, appearance="blush false", text="Ха, ну ты можешь называть его так, если хочешь, Мама.")
        call process_character (k, appearance="blush false", text="А ещё он трахабельный младший брат для меня!")
        call process_character (sa, appearance="blush false", text="Я следующая, Мама, я следующая!")
        call process_character (si, appearance="blush false", text="Конечно, дорогая.")
        call process_character (si, appearance="blush false", text="Повеселись со своим братом.")
    else:
        call static_still_ctc ("bg foursome_kirafuck")

        call process_character (k, appearance="blush false", text="Мм, ах, чёрт...")
        call process_character (k, appearance="blush false", text="Не возражаешь, если я сделаю это, Мама?")
        call process_character (si, appearance="blush false", text="Я думаю, ты уже приняла это решение, ха-ха!")
        call process_character (k, appearance="blush false", text="Лучше просить прощения, чем разрешения.")
        call process_character (n, appearance="blush false", text="Хах, ах, ах!")
        call process_character (k, appearance="blush false", text="Тебе нравится, что ты можешь видеть мою киску на своём члене, [n.say_name]?")
        call process_character (k, appearance="blush false", text="Ты увидишь всё действие!")
        call process_character (sa, appearance="blush false", text="Я чувствую, как дрожит пол от того, как [k.say_name] подпрыгивает вверх и вниз на члене [n.say_name]!")
        call process_character (si, appearance="blush false", text="Я надеюсь, что [n.say_name] сможет справиться с этим.")
        call process_character (k, appearance="blush false", text="Для него это ничего не значит.")
        call process_character (k, appearance="blush false", text="Я тщательно подготовила тело [n.say_name] для такого рода вещей!")
        call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
        call process_character (sa, appearance="blush false", text="Это то, чем я тоже занимаюсь!")
        call process_character (sa, appearance="blush false", text="[n.say_name] теперь способен трахать меня, играя в видеоигры!")
        call process_character (sa, appearance="blush false", text="Помню, однажды я сосала у него целую сессию игры Демона может смеяться!")
        call process_character (k, appearance="blush false", text="[n.say_name] это битва закалила его для секса, ха!")
        call process_character (k, appearance="blush false", text="Да, ты должен быть закалён, бро!")
        call process_character (si, appearance="blush false", text="Похоже, вы двое давите на [n.say_name] до предела!")
        call process_character (k, appearance="blush false", text="Ты тоже это делаешь, Мама, от нас этого не утаишь!")
        call process_character (k, appearance="blush false", text="[n.say_name] трахает тебя так сильно, что падает в обморок на тебя, я видела это!")
        call process_character (si, appearance="blush false", text="{i}Шшш,{/i} хаха!")
        call process_character (k, appearance="blush false", text="Почему бы тебе не попробовать, Мама?")
        call process_character (k, appearance="blush false", text="Просто присядь на хер [n.say_name]!")
        call process_character (si, appearance="blush false", text="Ох, можно?")
        call process_character (si, appearance="blush false", text="Я не легкая, как перышко!")
        call process_character (k, appearance="blush false", text="У него не будет проблем с тобой, Мама.")
        call process_character (k, appearance="blush false", text="Я чувствую, как его член дергается в моем влагалище.")
        call process_character (k, appearance="blush false", text="[n.say_name] хочет, чтобы ты села на него.")
        call process_character (n, appearance="blush false", text="Д-да...Мама...")
        call process_character (n, appearance="blush false", text="Я хочу этого, ах... {w=1.0}я хочу трахнуть тебя.")
        call process_character (k, appearance="blush false", text="Я же говорила.")
        call process_character (k, appearance="blush false", text="Бро вызывает свою Мамочку!")
        call process_character (sa, appearance="blush false", text="Хаха!")
        call process_character (sa, appearance="blush false", text="Давай, мама, сделай это!")
        call process_character (sa, appearance="blush false", text="Чёрт, [n.say_name]!")
        call process_character (si, appearance="blush false", text="Думаю, теперь все внимание сосредоточено на мне!")

        call static_still_ctc ("bg foursome_simonefuck")

        call process_character (n, appearance="blush false", text="Оох, Мама!")
        call process_character (si, appearance="blush false", text="Ммм!")
        call process_character (si, appearance="blush false", text="Да, милый!")
        call process_character (k, appearance="blush false", text="Круто, [n.say_name]!")
        call process_character (k, appearance="blush false", text="Толкай свой член до упора!")
        call process_character (k, appearance="blush false", text="Пусть мама почувствует каждый твой дюйм!")
        call process_character (sa, appearance="blush false", text="Делай, как говорит [k.say_name], [n.say_name]!")
        call process_character (sa, appearance="blush false", text="Трахни Маму, как сумасшедший!")
        call process_character (n, appearance="blush false", text="Аах...")
        call process_character (n, appearance="blush false", text="Твоя задница такая мягкая, Мама.")
        call process_character (k, appearance="blush false", text="Она большая и круглая, как хорошо!")
        call process_character (k, appearance="blush false", text="И она прямо над тобой, ха-ха!")
        call process_character (si, appearance="blush false", text="Ты так хорошо справляешься с этим, [n.say_name]!")
        call process_character (si, appearance="blush false", text="Ты проделал такой долгий путь с тех пор, как я впервые увидела тебя мастурбирующим в ванной!")
        call process_character (k, appearance="blush false", text="Точно, мама видела твою первую дрочку!")
        call process_character (k, appearance="blush false", text="Хотела бы я быть там, чтобы увидеть выражение ваших лиц!")
        call process_character (sa, appearance="blush false", text="Это было еще до того, как я узнала, что такое сперма!")
        call process_character (sa, appearance="blush false", text="Теперь я не могу представить жизнь без неё!")
        call process_character (si, appearance="blush false", text="Оох, оох, да!")
        call process_character (si, appearance="blush false", text="[n.say_name] стал настоящим мужчиной в доме!")
        call process_character (k, appearance="blush false", text="Ха, ну ты можешь называть его так, если хочешь, Мама.")
        call process_character (k, appearance="blush false", text="А ещё он трахабельный младший брат для меня!")
        call process_character (sa, appearance="blush false", text="Я следующая, Мама, я следующая!")
        call process_character (si, appearance="blush false", text="Конечно, дорогая.")
        call process_character (si, appearance="blush false", text="Повеселись со своим братом.")

    call static_still_ctc ("bg foursome_samfuck")

    call process_character (sa, appearance="blush false", text="Хорошо [n.say_name], только ты и я!")
    call process_character (n, appearance="blush false", text="Ахх, ах!")
    call process_character (sa, appearance="blush false", text="Хахх, ох, ах!")
    call process_character (si, appearance="blush false", text="Независимо от того, что вы двое делаете, вы всегда выглядите так мило вместе!")
    call process_character (k, appearance="blush false", text="Внешность может обманывать, Мама.")
    call process_character (k, appearance="blush false", text="[sa.say_name] и [n.say_name] может быть и выглядят мило, но когда трахаются мозги у них улетают!")
    call process_character (sa, appearance="blush false", text="Просто подожди и увидишь!")
    call process_character (sa, appearance="blush false", text="[n.say_name] и я можем пойти на полную!")
    call process_character (n, appearance="blush false", text="{i}Вздох-вздох-вздох!{/i}")
    call process_character (sa, appearance="blush false", text="Ха-а-а!")
    call process_character (k, appearance="blush false", text="Ничего себе, ты не шутила.")
    call process_character (k, appearance="blush false", text="Это самый быстрый секс в позе ковбойши, который я видела!")
    call process_character (si, appearance="blush false", text="Я думаю, что потянула бы мышцу, если двигалась так быстро, ха-ха!")
    call process_character (sa, appearance="blush false", text="Мы постоянно совершенствуемся!")
    call process_character (sa, appearance="blush false", text="Теперь мы можем практиковаться где угодно в доме!")
    call process_character (n, appearance="blush false", text="Мы можем?")
    call process_character (si, appearance="blush false", text="Пока это в доме или на заднем дворе, то разрешено.")
    call process_character (k, appearance="blush false", text="Вы двое будете трахаться за обеденным столом, не так ли?")

    call process_character (sa, appearance="blush false", text="Знаешь... это не плохая идея!")
    call process_character (k, appearance="blush false", text="Когда мы собираемся устроить еженедельный вечер голых фильмов?")
    call process_character (si, appearance="blush false", text="Я не думаю, что мы будем обращать внимание на фильм, если мы сделаем это!")
    call process_character (sa, appearance="blush false", text="Может, в этом и смысл, хе-хе!")
    call process_character (k, appearance="blush false", text="[sa.say_name] получает его!")
    call process_character (si, appearance="blush false", text="Если вы все заинтересованы, то почему бы и нет?")
    call process_character (n, appearance="blush false", text="Вы все будете голые во время фильма?")
    call process_character (k, appearance="blush false", text="Эй, ты тоже!")
    call process_character (k, appearance="blush false", text="Мы все в этом замешаны!")
    call process_character (sa, appearance="blush false", text="Бьюсь об заклад пенис [n.say_name] будет стоять все время!")
    call process_character (k, appearance="blush false", text="Без сомнения!")
    call process_character (k, appearance="blush false", text="Я в восторге!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (sa, appearance="blush false", text="Хмм...")
    call process_character (sa, appearance="blush false", text="...")
    call process_character (sa, appearance="blush false", text="Я только что придумала одну идею!")

    call process_character (k, appearance="blush false", text="Говори.")
    call process_character (sa, appearance="blush false", text="Мы все должны трахаться с [n.say_name] вместе!")
    call process_character (si, appearance="blush false", text="Как нам это сделать, милая?")
    call process_character (sa, appearance="blush false", text="Ну...")
    call process_character (sa, appearance="blush false", text="Хмм...")
    call process_character (k, appearance="blush false", text="Как насчет того, что [n.say_name] будет трахать мою задницу!")
    call process_character (sa, appearance="blush false", text="Да!")
    call process_character (sa, appearance="blush false", text="Звучит неплохо!")
    call process_character (sa, appearance="blush false", text="И Мама...")
    call process_character (sa, appearance="blush false", text="Ты можешь хлюпать сиськами по лицу [n.say_name]!")
    call process_character (si, appearance="blush false", text="Но куда это тебя приведет?")
    call process_character (sa, appearance="blush false", text="И я бы...")
    call process_character (sa, appearance="blush false", text="...")
    call process_character (sa, appearance="blush false", text="Что бы ты хотел, чтобы я сделала, [n.say_name]?")
    call process_character (sa, appearance="blush false", text="Или у тебя есть другая идея?")

    window auto
    menu:
        "Ты могла бы лизать снизу киску [k.say_name]!":
            $ did_family_foursome_ff = True
            call process_character (sa, appearance="blush false", text="Я бы никогда не подумала об этом!")
            call process_character (sa, appearance="blush false", text="Так что пока ты трахаешь задницу [k.say_name], я буду лизать ее киску?")
            call process_character (k, appearance="blush false", text="Ха!")
            call process_character (k, appearance="blush false", text="Это звучит так безумно...")
            call process_character (k, appearance="blush false", text="Мне нравится!")
            call process_character (sa, appearance="blush false", text="Мне тоже!")
            call process_character (si, appearance="blush false", text="Хорошо, что [sa.say_name] и [n.say_name] придумали такую хитроумную идею!")
            call process_character (k, appearance="blush false", text="Моя задница готова к твоему члену, [n.say_name].")
            call process_character (sa, appearance="blush false", text="Мне любопытно посмотреть, какова киска [k.say_name] на вкус!")
            call process_character (si, appearance="blush false", text="Это должно быть возбуждающе!")

            call fade_to_black (1)


            call static_still_ctc ("bg foursome_groupfuck")

            call process_character (k, appearance="blush false", text="Это так!")
            call process_character (si, appearance="blush false", text="Как-то нам удалось это скоординировать!")
            call process_character (sa, appearance="blush false", text="Убедись, что не поскользнешься и не упадешь на меня!")
            call process_character (n, appearance="blush false", text="Аах!")
            call process_character (n, appearance="blush false", text="Все...так хорошо...")
            call process_character (k, appearance="blush false", text="Встань по центру, [n.say_name]!")
            call process_character (k, appearance="blush false", text="Теперь ты застрял, хе-хе...")
            call process_character (sa, appearance="blush false", text="Мм...")
            call process_character (sa, appearance="blush false", text="Ммм...")
            call process_character (k, appearance="blush false", text="Твои навыки вылизывания достойны восхищения для новичка [sa.say_name]!")
            call process_character (sa, appearance="blush false", text="Я просто копирую то, что [n.say_name] делал, когда был на твоей киске!")
            call process_character (k, appearance="blush false", text="Это была хорошая идея!")
            call process_character (k, appearance="blush false", text="Как ты там поживаешь, [n.say_name]?")
            call process_character (k, appearance="blush false", text="Тебя душат гигантские сиськи?")
            call process_character (si, appearance="blush false", text="Он продолжает тыкать лицом мне между грудей!")
            call process_character (k, appearance="blush false", text="Это называется моторная лодка, [n.say_name]!")
            call process_character (n, appearance="blush false", text="Хммрм!")
            call process_character (k, appearance="blush false", text="Что такое, [n.say_name]?")
            call process_character (k, appearance="blush false", text="Ты хочешь, чтобы я напрягла свою задницу еще больше?")
            call process_character (k, appearance="blush false", text="Получи!")
            call process_character (n, appearance="blush false", text="Мммм!")
            call process_character (si, appearance="blush false", text="Я не думаю, что ты когда-нибудь услышишь о такой семейной связи где-нибудь еще!")
            call process_character (k, appearance="blush false", text="Это эксклюзивно для нас, Мама!")
            call process_character (k, appearance="blush false", text="О, да!")
            call process_character (k, appearance="blush false", text="Вгоняй глубже [n.say_name], по самые шары!")
            call process_character (sa, appearance="blush false", text="Это отличная идея!")
            call process_character (sa, appearance="blush false", text="Никто не сможет превзойти это!")
            call process_character (k, appearance="blush false", text="Я бы не стала говорить это слишком рано, [sa.say_name]!")
            call process_character (k, appearance="blush false", text="Мы еще не достигли оргазма!")
            call process_character (sa, appearance="blush false", text="О, правда!")
            call process_character (sa, appearance="blush false", text="Нам нужны наши оргазмы!")
            call process_character (si, appearance="blush false", text="Как, по-твоему, мы должны это сделать?")
            call process_character (n, appearance="blush false", text="...{p}...")
            call process_character (n, appearance="blush false", text="Я знаю как.")
            call process_character (k, appearance="blush false", text="Я знала, что ты что-то замышляешь, бро!")
            call process_character (sa, appearance="blush false", text="О чем ты думаешь, [n.say_name]?")
            call process_character (sa, appearance="blush false", text="Скажи нам, скажи нам!")
            call process_character (n, appearance="blush false", text="Я думаю...")
            call process_character (n, appearance="blush false", text="Я должен кончить в каждую из вас.")
        "Ты можешь смотреть, как я трахаю задницу [k.say_name], [sa.say_name]!":
            call process_character (sa, appearance="blush false", text="О да!")
            call process_character (sa, appearance="blush false", text="[k.say_name] упоминала ранее, как хорошо твой член вписывается в ее задницу!")
            call process_character (sa, appearance="blush false", text="Я хотела бы на это посмотреть!")
            call process_character (k, appearance="blush false", text="Мы устроим для тебя настоящее шоу [sa.say_name]!")
            call process_character (k, appearance="blush false", text="Ну же, [n.say_name], мой анус готов!")
            call process_character (si, appearance="blush false", text="Это должно быть захватывающе!")

            call fade_to_black (1)


            call static_still_ctc ("bg foursome_groupfucknosam")

            call process_character (k, appearance="blush false", text="Это происходит!")
            call process_character (si, appearance="blush false", text="Это требует немного координации, чтобы получилось!")
            call process_character (n, appearance="blush false", text="Аах!")
            call process_character (n, appearance="blush false", text="Все...так хорошо...")
            call process_character (sa, appearance="blush false", text="Смотреть это намного веселее, чем я думала!")
            call process_character (sa, appearance="blush false", text="Я могу быть супер близко к действию и увидеть все детали!")
            call process_character (k, appearance="blush false", text="Ты кормишь свою внутреннюю вуайеристку, сестрёнка!")
            call process_character (k, appearance="blush false", text="...")
            call process_character (k, appearance="blush false", text="Как ты там поживаешь, [n.say_name]?")
            call process_character (k, appearance="blush false", text="Тебя душат гигантские сиськи?")
            call process_character (si, appearance="blush false", text="Он продолжает тыкать лицом мне между грудей!")
            call process_character (k, appearance="blush false", text="Это называется моторная лодка, [n.say_name]!")
            call process_character (n, appearance="blush false", text="Хммрм!")
            call process_character (k, appearance="blush false", text="Что такое, [n.say_name]?")
            call process_character (k, appearance="blush false", text="Ты хочешь, чтобы я напрягла свою задницу еще больше?")
            call process_character (k, appearance="blush false", text="Получи!")
            call process_character (n, appearance="blush false", text="Мммм!")
            call process_character (si, appearance="blush false", text="Я не думаю, что ты когда-нибудь услышишь о такой семейной связи где-нибудь еще!")
            call process_character (k, appearance="blush false", text="Это эксклюзивно для нас, Мама!")
            call process_character (k, appearance="blush false", text="О, да!")
            call process_character (k, appearance="blush false", text="Вгоняй глубже [n.say_name], по самые шары!")
            call process_character (sa, appearance="blush false", text="Это отличная идея!")
            call process_character (sa, appearance="blush false", text="Никто не сможет превзойти это!")
            call process_character (k, appearance="blush false", text="Я бы не стала говорить это слишком рано, [sa.say_name]!")
            call process_character (k, appearance="blush false", text="Мы еще не достигли оргазма!")
            call process_character (sa, appearance="blush false", text="О, правда!")
            call process_character (sa, appearance="blush false", text="Нам нужны наши оргазмы!")
            call process_character (si, appearance="blush false", text="Как, по-твоему, мы должны это сделать?")
            call process_character (n, appearance="blush false", text="...{p}...")
            call process_character (n, appearance="blush false", text="Я знаю как.")
            call process_character (k, appearance="blush false", text="Я знала, что ты что-то замышляешь, бро!")
            call process_character (sa, appearance="blush false", text="О чем ты думаешь, [n.say_name]?")
            call process_character (sa, appearance="blush false", text="Скажи нам, скажи нам!")
            call process_character (n, appearance="blush false", text="Я думаю...")
            call process_character (n, appearance="blush false", text="Я должен кончить в каждую из вас.")

    call process_character (sa, appearance="blush false", text="В каждую из нас [n.say_name]?")
    call process_character (k, appearance="blush false", text="Слушай, брат...")
    call process_character (k, appearance="blush false", text="Я впечатлена количеством спермы, хранящейся в этих шарах.")
    call process_character (k, appearance="blush false", text="Но наполнить нас всех за один присест?")
    call process_character (k, appearance="blush false", text="Даже по моим стандартам, это довольно сложная задача.")
    call process_character (si, appearance="blush false", text="Ты уверен, что хочешь попробовать это, милый?")
    call process_character (n, appearance="blush false", text="Да...")
    call process_character (n, appearance="blush false", text="Да, я хочу кончить в каждую из вас!")
    call process_character (sa, appearance="blush false", text="[n.say_name] действительно хочет этого...")
    call process_character (k, appearance="blush false", text="Бро полностью предан делу.")
    call process_character (si, appearance="blush false", text="Мы возьмем все, что ты можешь дать нам, [n.say_name]!")


    $ family_foursome_cum_available_choices = ["kira", "sam", "simone"]
    call family_foursome_cum_choice (dream=dream)


    call family_foursome_end (dream=dream)
    return

label family_foursome_cum_choice(dream=False):
    window auto
    menu:
        "[k.say_name]" if "kira" in family_foursome_cum_available_choices:
            call family_foursome_cum_kira (dream=dream)
        "[sa.say_name]" if "sam" in family_foursome_cum_available_choices:
            call family_foursome_cum_sam (dream=dream)
        "Мама" if "simone" in family_foursome_cum_available_choices:
            call family_foursome_cum_simone (dream=dream)

    return

label family_foursome_cum_simone(dream=False):
    $ family_foursome_cum_available_choices.remove("simone")
    call static_still_ctc ("bg simoneahego_internal_nocum")

    call process_character (si, appearance="blush false", text="О, мой сладкий!")
    call process_character (si, appearance="blush false", text="Продолжай в том же духе!")
    call process_character (n, appearance="blush false", text="Конечно, Мама!")
    call process_character (n, appearance="blush false", text="Я буду продолжать делать это, пока не кончу!")
    call process_character (si, appearance="blush false", text="Ты такой особенный у меня, [n.say_name].")
    call process_character (si, appearance="blush false", text="Мне нравится то, что мы делаем вместе!")
    call process_character (si, appearance="blush false", text="Сначала я не была уверена, что справлюсь с этим, но у нас случился первый секс....")
    call process_character (si, appearance="blush false", text="Я знала, что это лучшее решение, которое я приняла за долгое время!")
    call process_character (n, appearance="blush false", text="Я чувствую то же самое, Мама!")
    call process_character (n, appearance="blush false", text="Я так рад, что мы смогли трахаться все это лето!")
    call process_character (si, appearance="blush false", text="Я...{w=1.0}я хочу, чтобы ты оплодотворил меня, [n.say_name]!")
    call process_character (si, appearance="blush false", text="У меня никогда не было такого сильного желания!")
    call process_character (si, appearance="blush false", text="Ты чувствуешь то же самое, [n.say_name]?")
    call process_character (si, appearance="blush false", text="Ты хочешь, чтобы твоя Мамочка забеременела?")

    menu:
        "Да, конечно!":
            $ simone_impreg = True
            call process_character (si, appearance="blush false", text="Тогда давай кончим вместе, милый!")
            call process_character (si, appearance="blush false", text="Вылей всю свою сперму в мою киску!")
            call process_character (n, appearance="blush false", text="Я почти, Мама!")
            call process_character (n, appearance="blush false", text="Спермы будет очень много!")
            call process_character (si, appearance="blush false", text="Да, да!")
            call process_character (si, appearance="blush false", text="Я знаю, что у тебя сильная плодовитость!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg simoneahego_internal_cum_impreg")

            call process_character (n, appearance="blush false", text="Вот оно, Мамааа!")
            call process_character (si, appearance="blush false", text="Я чувствую это, детка!")
            call process_character (si, appearance="blush false", text="Продолжай так долго, как сможешь!")
            call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..вздох...")
            call process_character (si, appearance="blush false", text="Я так горжусь тобой, [n.say_name]!")
            call process_character (si, appearance="blush false", text="Это замечательно, что ты мой сын!")
            call process_character (n, appearance="blush false", text="Я так сильно люблю тебя, Мама...")
            call process_character (n, appearance="blush false", text="...")
        "Может быть позже.":
            call process_character (si, appearance="blush false", text="Конечно, милый.")
            call process_character (si, appearance="blush false", text="Ты не должен принимать это решение сейчас.")
            call process_character (si, appearance="blush false", text="Сначала все должно успокоиться в нашем новом доме!")
            call process_character (n, appearance="blush false", text="Я почти, Мама!")
            call process_character (n, appearance="blush false", text="Спермы будет очень много!")
            call process_character (si, appearance="blush false", text="Да!")
            call process_character (si, appearance="blush false", text="Влей всю свою сперму в мою киску!")
            call process_character (n, appearance="blush false", text="Вот оно, Мамааа!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg simoneahego_internal_cum")

            call process_character (si, appearance="blush false", text="Я чувствую это, детка!")
            call process_character (si, appearance="blush false", text="Продолжай так долго, как сможешь!")
            call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..вздох...")
            call process_character (n, appearance="blush false", text="Я всё.")
            call process_character (si, appearance="blush false", text="Я так горжусь тобой, [n.say_name]!")
            call process_character (si, appearance="blush false", text="Это так замечательно быть твоей мамой!")
            call process_character (n, appearance="blush false", text="И я рад, что ты моя Мама...Мама!")
            call process_character (n, appearance="blush false", text="Всегда здорово кончить в тебя.")


    if len(family_foursome_cum_available_choices) == 2:
        call process_character (si, appearance="blush false", text="[k.say_name] и [sa.say_name] выглядят нетерпеливыми, конфетка.")
        call process_character (si, appearance="blush false", text="Ты должен оказать им внимание, хорошо!")
    elif len(family_foursome_cum_available_choices) == 1:
        if family_foursome_cum_available_choices[0] == "kira":
            $ family_foursome_cum_last = k.say_name
        else:
            $ family_foursome_cum_last = sa.say_name

        call process_character (si, appearance="blush false", text="[family_foursome_cum_last] все еще остались, сладкий.")
        call process_character (si, appearance="blush false", text="Они терпеливо ждали!")
    else:
        call family_foursome_end (dream=dream)
        return

    call family_foursome_cum_choice (dream=dream)

    return

label family_foursome_cum_sam(dream=False):
    $ family_foursome_cum_available_choices.remove("sam")
    call static_still_ctc ("bg SamAhego_Internal_NoCum")

    call process_character (sa, appearance="blush false", text="Хаахх!")
    call process_character (n, appearance="blush false", text="Не могу дождаться, когда кончу в тебя, [sa.say_name]!")
    call process_character (sa, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (sa, appearance="blush false", text="Я недавно думала...")
    call process_character (sa, appearance="blush false", text="Может, если ты кончишь достаточно сильно, то я забеременею!")
    call process_character (sa, appearance="blush false", text="Мы, конечно, много трахаемся и это произойдёт в конце концов!")
    call process_character (sa, appearance="blush false", text="Представь, как это было бы здорово, [n.say_name]!")
    call process_character (sa, appearance="blush false", text="Что ты думаешь о том, чтобы сделать меня беременной?")

    menu:
        "Это было бы здорово.":
            $ sam_impreg = True
            call process_character (sa, appearance="blush false", text="Тогда давай сделаем это!")
            call process_character (sa, appearance="blush false", text="Если это сработает в этот раз, то отлично!")
            call process_character (sa, appearance="blush false", text="Если нет, мы будем делать это снова и снова, пока не добьемся успеха!")
            call process_character (sa, appearance="blush false", text="Это будет грандиозно!")
            call process_character (n, appearance="blush false", text="Ааах, ааах!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg samahego_internal_cum_impreg")

            call process_character (sa, appearance="blush false", text="{i}Уфф!{/i}")
            call process_character (sa, appearance="blush false", text="Потрясающееее!")
            call process_character (sa, appearance="blush false", text="Ты вливаешь так много спермы в киску!")
            call process_character (sa, appearance="blush false", text="Я думаю, что это должно сработать, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Я на сто процентов уверена, что забеременею!")
            call process_character (n, appearance="blush false", text="Хррм!")
            call process_character (n, appearance="blush false", text="Бьюсь об заклад, ты права, [sa.say_name].")
        "Мне нужно подумать об этом.":
            call process_character (sa, appearance="blush false", text="Да, хорошее замечание.")
            call process_character (sa, appearance="blush false", text="Мы должны все тщательно спланировать.")
            call process_character (sa, appearance="blush false", text="Но у нас это хорошо получается!")
            call process_character (sa, appearance="blush false", text="А сейчас мы просто потрахаемся, как обычно!")
            call process_character (n, appearance="blush false", text="Ааах, ааах!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg samahego_internal_cum")

            call process_character (sa, appearance="blush false", text="{i}Уфф!{/i}")
            call process_character (sa, appearance="blush false", text="Потрясающееее!")
            call process_character (sa, appearance="blush false", text="Ты вливаешь так много спермы в киску!")
            call process_character (sa, appearance="blush false", text="Думаешь, она прольется на пол, когда ты его вытащишь?")
            call process_character (sa, appearance="blush false", text="Я не удивлюсь, если это случится!")
            call process_character (n, appearance="blush false", text="Хррм!")
            call process_character (n, appearance="blush false", text="Вещи становятся грязными, когда мы трахаемся!")


    if len(family_foursome_cum_available_choices) == 2:
        call process_character (sa, appearance="blush false", text="Эй, не забудь про Маму и [k.say_name]!")
        call process_character (sa, appearance="blush false", text="Ты должен заполнить их киски спермой тоже!")
    elif len(family_foursome_cum_available_choices) == 1:
        if family_foursome_cum_available_choices[0] == "kira":
            $ family_foursome_cum_last = k.say_name
        else:
            $ family_foursome_cum_last = "Mom"

        call process_character (sa, appearance="blush false", text="Не забывай о [family_foursome_cum_last], [n.say_name]!")
        call process_character (sa, appearance="blush false", text="Тебе нужно заполнить ее киску спермой!")
    else:
        call family_foursome_end (dream=dream)
        return

    call family_foursome_cum_choice (dream=dream)

    return

label family_foursome_cum_kira(dream=False):
    $ family_foursome_cum_available_choices.remove("kira")
    call static_still_ctc ("bg kiraahego_internal_nocum")

    call process_character (k, appearance="blush false", text="Унф...")
    call process_character (k, appearance="blush false", text="Ты задеваешь мою точку G.")
    call process_character (k, appearance="blush false", text="Я знала, что это и был твой, ах, план.")
    call process_character (n, appearance="blush false", text="Ааах, да!")
    call process_character (n, appearance="blush false", text="Я, кончу в тебя, [k.say_name]!")
    call process_character (n, appearance="blush false", text="Это будет самый мощный оргазм, который я когда-либо делал!")
    call process_character (k, appearance="blush false", text="Сильные слова, бро.")
    call process_character (k, appearance="blush false", text="Надеюсь, ты сможешь это подтвердить.")
    call process_character (n, appearance="blush false", text="Да!")
    call process_character (n, appearance="blush false", text="Я знаю, что сделаю!")
    call process_character (k, appearance="blush false", text="Ммм, ах.")
    call process_character (k, appearance="blush false", text="Ты пытаешься... обрюхатить старшую сестру?")
    call process_character (k, appearance="blush false", text="Это твоя цель, бро?")
    call process_character (k, appearance="blush false", text="Посадить свое семя в утробу старшей сестры раньше всех?")


    menu:
        "Да!":
            $ kira_impreg = True
            call process_character (k, appearance="blush false", text="Ха, правда выходит наружу!")
            call process_character (k, appearance="blush false", text="Тогда пусть это и произойдет.")
            call process_character (k, appearance="blush false", text="Пусть твоя сперма достигнет места назначения!")
            call process_character (n, appearance="blush false", text="Хрмм...")
            call process_character (n, appearance="blush false", text="Га-ха!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg kiraahergo_internal_cum_impreg")

            call process_character (k, appearance="blush false", text="Ааах, чёрт!")
            call process_character (k, appearance="blush false", text="Прямое попадание, бро!")
            call process_character (n, appearance="blush false", text="Мм-Ммм!")
            call process_character (n, appearance="blush false", text="Ааах...")
        "Я просто хочу кончить в тебя.":
            call process_character (k, appearance="blush false", text="Конечно, конечно...")
            call process_character (k, appearance="blush false", text="Ну, тогда пусть это и произойдет!")
            call process_character (k, appearance="blush false", text="Кончи в мою киску!")
            call process_character (n, appearance="blush false", text="Хрмм...")
            call process_character (n, appearance="blush false", text="Га-ха!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg kiraahego_internal_cum")

            call process_character (k, appearance="blush false", text="Ааах, чёрт!")
            call process_character (k, appearance="blush false", text="Прямое попадание, бро!")
            call process_character (k, appearance="blush false", text="Я буду сливать сперму всю недели!")
            call process_character (n, appearance="blush false", text="Мм-Ммм!")
            call process_character (n, appearance="blush false", text="Ааах...")



    if len(family_foursome_cum_available_choices) == 2:
        call process_character (k, appearance="blush false", text="У тебя все еще есть еще две киски, которые нужно заполнить, [n.say_name]!")
        call process_character (k, appearance="blush false", text="Поторопись!")
    elif len(family_foursome_cum_available_choices) == 1:
        call process_character (k, appearance="blush false", text="У тебя все еще есть еще одна киска, которую нужно заполнить, [n.say_name]!")
        call process_character (k, appearance="blush false", text="Поторопись!")
    else:
        call family_foursome_end (dream=dream)
        return

    call family_foursome_cum_choice (dream=dream)

    return


label family_foursome_end(dream=False):
    call process_character (n, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="Чувак, запах здесь нереальный!")
    call process_character (sa, appearance="blush false", text="Там сперма повсюду тоже!")
    call process_character (si, appearance="blush false", text="Все в порядке, мы освежим комнату позже.")
    call process_character (n, appearance="blush false", text="Это...{w=1.0} было величайшей вещью.")
    call process_character (sa, appearance="blush false", text="Ты действительно сделал это, [n.say_name]!")
    call process_character (sa, appearance="blush false", text="Ты кончил во всех нас!")
    call process_character (k, appearance="blush false", text="Я уверена, что это будет не последний раз, когда ты сделаешь это, хе-хе.")
    call process_character (si, appearance="blush false", text="Я пропитана потом и другими телесными жидкостями!")
    call process_character (si, appearance="blush false", text="Я в душ!")
    call process_character (sa, appearance="blush false", text="[n.say_name], пойдем в бассейн!")
    call process_character (sa, appearance="blush false", text="Я хочу попробовать отсосать у тебя под водой!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="Я тоже пойду на улицу, позанимаюсь.")
    call process_character (k, appearance="blush false", text="Я позабочусь о том, чтобы было видно мою задницу из бассейна, [n.say_name].")
    call process_character (k, appearance="blush false", text="Эта процедура требует много наклонов!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Так вот как все будет дальше, да?)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Семья - это круто!)")

    $ replace_position = False
    call add_replayable_scene ("family_foursome_scene", si)
    call add_replayable_scene ("family_foursome_scene", k)
    call add_replayable_scene ("family_foursome_scene", sa)

    python:
        k.revistable_scenes.add("family_foursome_scene_revisit_kira")
        si.revistable_scenes.add("family_foursome_scene_revisit_simone")
        sa.revistable_scenes.add("family_foursome_scene_revisit_sam")

        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_received_blowjob", 1)
            stats.add_stat("times_had_group_sex", 1)
            stats.add_stat("times_cummed_in_mouth", 1)
            stats.add_stat("times_seen_butt", 1)
            stats.add_stat("times_seen_butthole", 1)
            stats.add_stat("times_given_anal_sex", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("family_foursome_scene", dream=dream)

    return

label family_foursome_sam_bj(family_foursome_choice_time, dream=False):
    $ family_foursome_bj_available_choices.remove("sam")

    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Дааа!")
    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Я собиралась попробовать новую технику на тебе, [n.say_name]!")

    call static_still_ctc ("bg sam_deepblowjob")

    call process_character (n, appearance="blush false", text="Аах, да, [sa.say_name]!")
    call process_character (k, appearance="blush false", text="Довольно хорошо, сестрёнка!")
    call process_character (k, appearance="blush false", text="У тебя только что взяли весь член в рот, [n.say_name]!")
    call process_character (si, appearance="blush false", text="Как ты научилась делать это, милая?")
    call process_character (sa, appearance="blush false", text="Ммф...смотрела много порно.")
    call process_character (k, appearance="blush false", text="Ты должно быть смотришь качественные фильмы!")
    call process_character (k, appearance="blush false", text="Пришли мне несколько видео, когда будет возможность.")
    call process_character (n, appearance="blush false", text="(Щека [sa.say_name] давит на мой член!)")
    call process_character (n, appearance="blush false", text="(Я чувствую, как кончик касается этой стороны ее рта!)")
    call process_character (k, appearance="blush false", text="Черт, [sa.say_name], ты скоро будешь профессионалкой в этом!")
    call process_character (k, appearance="blush false", text="К счастью, у тебя всегда есть готовый член для практики, правильно, [n.say_name]?")
    call process_character (n, appearance="blush false", text="П-правильно, ах...")
    call process_character (sa, appearance="blush false", text="Ммм...")
    call process_character (sa, appearance="blush false", text="Я в состоянии сосать хер [n.say_name] часто.")
    call process_character (sa, appearance="blush false", text="Обычно мы делаем это во время или после видеоигр.")
    call process_character (si, appearance="blush false", text="Почти все время, [sa.say_name]!")
    call process_character (sa, appearance="blush false", text="Ага!")
    call process_character (k, appearance="blush false", text="В таком случае, мы сможем проводить соревнования, кто лучший членосос!")
    call process_character (si, appearance="blush false", text="О боже...")
    call process_character (sa, appearance="blush false", text="Думаешь, мы сможем это сделать?")
    call process_character (k, appearance="blush false", text="Сестра против сестры, финальная битва!")
    call process_character (k, appearance="blush false", text="[n.say_name] будет судить наш стиль, силу сосания, и глотание спермы!")
    call process_character (k, appearance="blush false", text="Проигравший должен смотреть, как [n.say_name] трахает победителя!")
    call process_character (n, appearance="blush false", text="{i}Глык.{/i}..")
    call process_character (si, appearance="blush false", text="Не выходи из-под контроля с этой идеей, [k.say_name].")
    call process_character (si, appearance="blush false", text="В противном случае [n.say_name] будет получать минет, где бы он ни был в доме!")
    call process_character (k, appearance="blush false", text="И это плохо, потому что?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (sa, appearance="blush false", text="Ммф...")
    call process_character (sa, appearance="blush false", text="Ммм...")


    if family_foursome_choice_time == 1:
        call process_character (si, appearance="blush false", text="Не забудь дать [k.say_name] и мне попытку, [sa.say_name].")
        call process_character (sa, appearance="blush false", text="О, моя ошибка...")
        call process_character (sa, appearance="blush false", text="Ты можешь переключаться, когда захочешь, [n.say_name]!")

        call family_foursome_bj_choice (2, dream=dream)

    elif family_foursome_choice_time == 2:
        call process_character (si, appearance="blush false", text="Убедись, что все получат очередь, [sa.say_name].")
        call process_character (sa, appearance="blush false", text="О, моя ошибка...")
        call process_character (sa, appearance="blush false", text="Ты можешь переключаться, когда захочешь, [n.say_name]!")

        call family_foursome_bj_choice (3, dream=dream)
    elif family_foursome_choice_time == 3:
        call family_foursome_phase_2 (dream=dream)

    return

label family_foursome_simone_bj(family_foursome_choice_time, dream=False):
    $ family_foursome_bj_available_choices.remove("simone")

    if family_foursome_choice_time == 1:
        call process_character (k, appearance="pose handhip face neutral blush false", text="Конечно, сначала ты выбрала Маму.")
        call process_character (k, appearance="pose handhip face neutral blush false", text="Это подтверждает, что ты маменькин сыночек!")
        call process_character (k, appearance="pose handhip face happy blush false", text="Хотя я не удивлена, учитывая, что мама может сосать твой член как пылесос!")
        call process_character (si, appearance="pose armunder face flirt blush false", text="...")

    call process_character (si, appearance="pose armunder face flirt blush false", text="Ты готов, дорогой?")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Д-да, Мам...")

    call static_still_ctc ("bg simone_underblowjob_nude")

    call process_character (n, appearance="blush false", text="Ах, ах, ах!")
    call process_character (si, appearance="blush false", text="Хмм, Мм...")
    call process_character (sa, appearance="blush false", text="Посмотри на Маму!")
    call process_character (k, appearance="blush false", text="Да, это материнская любовь.")
    call process_character (k, appearance="blush false", text="И [n.say_name] знает это!")
    call process_character (si, appearance="blush false", text="Ммм, Ммм...")
    call process_character (si, appearance="blush false", text="Ох, [n.say_name]...")
    call process_character (k, appearance="blush false", text="Мама втягивается в это!")
    call process_character (k, appearance="blush false", text="Давай, Мама!")
    call process_character (sa, appearance="blush false", text="Соси, Мама, соси!")
    call process_character (n, appearance="blush false", text="Хаахх!")
    call process_character (n, appearance="blush false", text="(Мама сосет сильнее, чем обычно!)")
    call process_character (n, appearance="blush false", text="(Это потому, что [sa.say_name] и [k.say_name] подбадривают её?)")
    call process_character (n, appearance="blush false", text="{i}Уфф!{/i}")
    call process_character (n, appearance="blush false", text="(Продолжайте болеть, продолжайте восхищаться!)")
    call process_character (si, appearance="blush false", text="([n.say_name] держится за мою голову)")
    call process_character (si, appearance="blush false", text="(Он держит меня в позе, чтобы сосать его член!)")

    call static_still_ctc ("bg simone_underblowjob_nude_sloppy")

    call process_character (k, appearance="blush false", text="Эй, посмотри на это [sa.say_name]...")
    call process_character (k, appearance="blush false", text="Посмотри, как мама пускает слюни.")
    call process_character (sa, appearance="blush false", text="Некоторые из них попали на ее сиськи!")
    call process_character (k, appearance="blush false", text="Это то, что известно как мокрый минет.")
    call process_character (sa, appearance="blush false", text="Мокрый минет...поняла!")
    call process_character (sa, appearance="blush false", text="Мама также издает много звуков своим ртом.")
    call process_character (k, appearance="blush false", text="Это часть того, что делает хороший мокрый минет!")
    call process_character (si, appearance="blush false", text="Ммф...")
    call process_character (si, appearance="blush false", text="Вы двое развлекаетесь, комментируя?")
    call process_character (sa, appearance="blush false", text="Я люблю смотреть, как ты двигаешь головой, Мама!")


    if family_foursome_choice_time == 1:
        call process_character (si, appearance="blush false", text="Я хотела бы посмотреть, как вы оба подходите к своим минетам.")
        call process_character (si, appearance="blush false", text="Если хочешь, милый, я могу передать тебя к [k.say_name] или [sa.say_name] далее!")

        call family_foursome_bj_choice (2, dream=dream)

    elif family_foursome_choice_time == 2:
        call process_character (si, appearance="blush false", text="У тебя еще есть один минет [n.say_name].")
        call process_character (si, appearance="blush false", text="Дай мне знать, когда захочешь поменяться!")

        call family_foursome_bj_choice (3, dream=dream)
    elif family_foursome_choice_time == 3:
        call family_foursome_phase_2 (dream=dream)

    return

label family_foursome_kira_bj(family_foursome_choice_time, dream=False):
    $ family_foursome_bj_available_choices.remove("kira")
    if not kira_simone_threesome_part_2_done:
        call process_character (k, appearance="pose handhip face flirt blush false", text="Любой старомодный минет не годится для тебя, [n.say_name].")
        call process_character (k, appearance="pose handhip face happy blush false", text="Ты должен попробовать фишку [k.say_name]!")

        call static_still_ctc ("bg kirablowjob_69")

        call process_character (n, appearance="blush false", text="Ух ты!")
        call process_character (si, appearance="blush false", text="Ох, надо же, [k.say_name]!")
    else:

        call process_character (k, appearance="pose handhip face flirt blush false", text="Любой старомодный минет не годится для тебя, [n.say_name].")
        call process_character (k, appearance="pose handhip face happy blush false", text="Давай покажем [sa.say_name] нашу позу шестьдесят девять!")

        call static_still_ctc ("bg kirablowjob_69")

        call process_character (n, appearance="blush false", text="Ух ты!")
        call process_character (si, appearance="blush false", text="О да, я помню, как ты это делала, [k.say_name]!")

    call process_character (si, appearance="blush false", text="Не урони [n.say_name] на голову!")
    call process_character (k, appearance="blush false", text="Ммм ... всё в порядке.")
    call process_character (k, appearance="blush false", text="Кроме того, у [n.say_name] крепкая башка.")
    call process_character (k, appearance="blush false", text="Его голова сломает пол, если ударится!")
    call process_character (sa, appearance="blush false", text="Это самая крутая позиция!")
    call process_character (sa, appearance="blush false", text="Хотела бы я быть достаточно сильной, чтобы сделать это!")
    call process_character (k, appearance="blush false", text="Эй, если ты будешь работать над этим, сестрёнка, то сможешь поднять [n.say_name] тоже!")
    call process_character (k, appearance="blush false", text="Нет ничего более приятного, чем трясти твоим братом во время секса!")
    call process_character (sa, appearance="blush false", text="Ха-ха, держу пари!")
    call process_character (k, appearance="blush false", text="Эй, лижи мою киску, [n.say_name].")
    call process_character (k, appearance="blush false", text="Нырни туда своим языком!")
    call process_character (n, appearance="blush false", text="Ммф...")
    call process_character (k, appearance="blush false", text="Ах, да, вот так-то!")
    call process_character (k, appearance="blush false", text="Продолжай работать языком, бро!")
    call process_character (n, appearance="blush false", text="([k.say_name] прижимает меня плотно к своему телу!)")
    call process_character (n, appearance="blush false", text="(Мое лицо уткнулось ей в промежность!)")
    call process_character (si, appearance="blush false", text="Ты должна позволить [n.say_name] опуститься в конце концов, [k.say_name].")
    call process_character (si, appearance="blush false", text="У него закружится голова от прилива крови к голове.")

    if family_foursome_choice_time == 1:
        call process_character (sa, appearance="blush false", text="И я хочу уже отсосать [n.say_name]!")
        call process_character (k, appearance="blush false", text="Просто дай мне еще пару секунд побыть с ним.")
        call process_character (k, appearance="blush false", text="Скажи, когда захочешь переключиться на Маму или [sa.say_name], бро!")

        call family_foursome_bj_choice (2, dream=dream)

    elif family_foursome_choice_time == 2:
        call process_character (k, appearance="blush false", text="Просто дай мне еще пару секунд побыть с ним.")
        call process_character (k, appearance="blush false", text="[n.say_name] скажет мне, когда будет готов двигаться дальше!")

        call family_foursome_bj_choice (3, dream=dream)
    elif family_foursome_choice_time == 3:
        call process_character (k, appearance="blush false", text="Просто дай мне еще пару секунд побыть с ним.")
        call process_character (k, appearance="blush false", text="[n.say_name] скажет мне, когда будет готов двигаться дальше!")
        call process_character (k, appearance="blush false", text="...")

        call family_foursome_phase_2 (dream=dream)

    return


label family_foursome_scene_revisit_kira:
    $ no_bust_art = False

    call process_character (n, appearance="pose twohandfist face happy blush false")
    call process_character (k, appearance="pose handhip face happy blush false", text="Твой член снова нуждается во всех наших дырочках, а?")
    call process_character (k, appearance="pose handhip face happy blush false", text="Время для еще одного семейного сбора!")

    call family_foursome_scene_revisit

    return

label family_foursome_scene_revisit_sam:
    $ no_bust_art = False

    call process_character (n, appearance="pose twohandfist face happy blush false")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Отличная идея!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Ты иди за Мамой, а я позову [k.say_name]!")

    call family_foursome_scene_revisit

    return

label family_foursome_scene_revisit_simone:
    $ no_bust_art = False

    call process_character (n, appearance="pose handfist face happy blush false")
    call process_character (si, appearance="pose armunder face happy blush false", text="Уверена, твои сёстры будут рады!")
    call process_character (si, appearance="pose armunder face happy blush false", text="[k.say_name], [sa.say_name]!")
    call process_character (si, appearance="pose armunder face happy blush false", text="[n.say_name] хочет трахнуть всех нас снова!")

    call family_foursome_scene_revisit

    return

screen family_foursome_options(xalign=0.98):
    vbox:
        xalign xalign
        yalign 0.5
        spacing 30

        use main_menu_button(text="Трахнуть [k.say_name]", action=Jump("family_foursome_scene_revisit_kira_fuck"), text_size=44)
        use main_menu_button(text="Минет [k.say_name]", action=Jump("family_foursome_scene_revisit_kira_blowjob"), text_size=44)
        use main_menu_button(text="Трахнуть [sa.say_name]", action=Jump("family_foursome_scene_revisit_sam_fuck"), text_size=44)
        use main_menu_button(text="Минет [sa.say_name]", action=Jump("family_foursome_scene_revisit_sam_blowjob"), text_size=44)
        use main_menu_button(text="Трахнуть Маму", action=Jump("family_foursome_scene_revisit_simone_fuck"), text_size=44)
        use main_menu_button(text="Минет Мамы", action=Jump("family_foursome_scene_revisit_simone_blowjob"), text_size=44)
        use main_menu_button(text="Вчетвером", action=Jump("family_foursome_scene_revisit_foursome"), text_size=44)
        use main_menu_button(text="Тройничок", action=Jump("family_foursome_scene_revisit_threesome"), text_size=44)

        if family_foursome_revisit_current_mode == "fuck":
            if family_foursome_revisit_current_partner == k:
                use main_menu_button(text="Кончить", action=Jump("family_foursome_scene_revisit_kira_cum_no_impreg"), text_size=44)
                use main_menu_button(text="Оплодотворить", action=Jump("family_foursome_scene_revisit_kira_impreg"), text_size=44)
            elif family_foursome_revisit_current_partner == sa:
                use main_menu_button(text="Кончить", action=Jump("family_foursome_scene_revisit_sam_cum_no_impreg"), text_size=44)
                use main_menu_button(text="Оплодотворить", action=Jump("family_foursome_scene_revisit_sam_impreg"), text_size=44)
            else:
                use main_menu_button(text="Кончить", action=Jump("family_foursome_scene_revisit_simone_cum_no_impreg"), text_size=44)
                use main_menu_button(text="Оплодотворить", action=Jump("family_foursome_scene_revisit_simone_impreg"), text_size=44)

label family_foursome_scene_revisit_simone_impreg:
    $ simone_impreg = True
    call static_still_ctc ("bg simoneahego_internal_nocum")
    call process_character (si, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Аах!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
    call static_still_ctc ("bg simoneahego_internal_cum_impreg")
    jump family_foursome_scene_revisit_simone_cum
    return


label family_foursome_scene_revisit_simone_cum_no_impreg:
    call static_still_ctc ("bg simoneahego_internal_nocum")
    call process_character (si, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Аах!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
    call static_still_ctc ("bg simoneahego_internal_cum")

    jump family_foursome_scene_revisit_simone_cum
    return

label family_foursome_scene_revisit_simone_cum:
    call process_character (si, appearance="blush false", text="Ооох!")
    call process_character (si, appearance="blush false", text="Великолепно, конфетка!")

    jump family_foursome_scene_revisit_end

    return

label family_foursome_scene_revisit_sam_impreg:
    call static_still_ctc ("bg samahego_internal_nocum")

    call process_character (sa, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Оох!")

    $ sam_impreg = True
    call static_still_ctc ("bg samahego_internal_cum_impreg")
    jump family_foursome_scene_revisit_sam_cum
    return


label family_foursome_scene_revisit_sam_cum_no_impreg:
    call static_still_ctc ("bg samahego_internal_nocum")

    call process_character (sa, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Оох!")

    call static_still_ctc ("bg samahego_internal_cum")
    jump family_foursome_scene_revisit_sam_cum
    return

label family_foursome_scene_revisit_sam_cum:
    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call process_character (sa, appearance="blush false", text="Ммнф!")
    call process_character (sa, appearance="blush false", text="Я кончаю!")

    jump family_foursome_scene_revisit_end

    return

label family_foursome_scene_revisit_kira_impreg:
    call static_still_ctc ("bg kiraahego_internal_nocum")
    call process_character (k, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Хррм!")

    $ kira_impreg = True
    call static_still_ctc ("bg kiraahergo_internal_cum_impreg")
    jump family_foursome_scene_revisit_kira_cum
    return


label family_foursome_scene_revisit_kira_cum_no_impreg:
    call static_still_ctc ("bg kiraahego_internal_nocum")
    call process_character (k, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Хррм!")

    call static_still_ctc ("bg kiraahego_internal_cum")
    jump family_foursome_scene_revisit_kira_cum
    return

label family_foursome_scene_revisit_kira_cum:
    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call process_character (k, appearance="blush false", text="Ааах дааа...")
    call process_character (k, appearance="blush false", text="Мощно кончил, бро!")

    jump family_foursome_scene_revisit_end

    return

label family_foursome_scene_revisit_kira_blowjob:
    $ family_foursome_revisit_current_partner = k
    $ family_foursome_revisit_current_mode = "bj"
    call static_still_ctc ("bg kirablowjob_69")
    $ dice_roll = random.randint(1,3)
    if dice_roll == 1:
        call process_character (k, appearance="blush false", text="Держу пари, я могу пронести тебя по дому вот так, ха-ха!")
        call process_character (si, appearance="blush false", text="Это было бы зрелище!")
    elif dice_roll == 2:
        call process_character (k, appearance="blush false", text="Кому нужны гири, когда есть ты, бро?")
        call process_character (k, appearance="blush false", text="Теперь мне не нужно копить на набор гантелей!")
    else:
        call process_character (k, appearance="blush false", text="У тебя уже есть хорошие навыки лизания киски, [n.say_name]!")
        call process_character (k, appearance="blush false", text="Мне нужно просить тебя делать это чаще со мной!")

    window auto
    call screen family_foursome_options
    return

label family_foursome_scene_revisit_kira_fuck:
    $ family_foursome_revisit_current_partner = k
    $ family_foursome_revisit_current_mode = "fuck"
    call static_still_ctc ("bg foursome_kirafuck")
    $ dice_roll = random.randint(1,3)

    if dice_roll == 1:
        call process_character (k, appearance="blush false", text="Мы должны смотреть порно по телевизору, когда мы делаем это вместе.")
        call process_character (k, appearance="blush false", text="Тогда мы могли бы попробовать имитировать то, что порнозвезды могут сделать!")
    elif dice_roll == 2:
        call process_character (k, appearance="blush false", text="Если мы когда-нибудь замерзнем зимой, это нас согреет!")
    else:
        call process_character (k, appearance="blush false", text="Нет конца наших трахфестивалей!")
        call process_character (k, appearance="blush false", text="Так и должно быть!")

    window auto
    call screen family_foursome_options(xalign = 0.02)
    return

label family_foursome_scene_revisit_sam_blowjob:
    $ family_foursome_revisit_current_partner = sa
    $ family_foursome_revisit_current_mode = "bj"
    call static_still_ctc ("bg sam_deepblowjob")

    $ dice_roll = random.randint(1,3)
    if dice_roll == 1:
        call process_character (sa, appearance="blush false", text="Я могла бы собрать несколько порций твоей спермы и попытаться проглотить всё сразу!")
        call process_character (sa, appearance="blush false", text="Думаешь, я смогу это сделать, [n.say_name]?")
    elif dice_roll == 2:
        call process_character (sa, appearance="blush false", text="Думаешь, сперма годиться вместо еды?")
        call process_character (si, appearance="blush false", text="Сперма, милая?")
        call process_character (sa, appearance="blush false", text="Мне просто было любопытно.")
        call process_character (sa, appearance="blush false", text="На днях я видела видео, как девушка ела еду, покрытую спермой, и это выглядело вкусно!")
    else:
        call process_character (sa, appearance="blush false", text="Я освою глубокий заглот, [n.say_name]!")
        call process_character (sa, appearance="blush false", text="Однажды я засуну весь твой член себе в рот!")

    window auto
    call screen family_foursome_options
    return

label family_foursome_scene_revisit_sam_fuck:
    $ family_foursome_revisit_current_partner = sa
    $ family_foursome_revisit_current_mode = "fuck"
    call static_still_ctc ("bg foursome_samfuck")
    $ dice_roll = random.randint(1,3)

    if dice_roll == 1:
        call process_character (sa, appearance="blush false", text="Нам нужен надувной плот для бассейна, [n.say_name]!")
        call process_character (sa, appearance="blush false", text="Тогда мы могли бы трахаться, плавая в воде!")
    elif dice_roll == 2:
        call process_character (sa, appearance="blush false", text="(Представь, если бы мы могли стримить это?!)")
        call process_character (sa, appearance="blush false", text="(Количество наших подписчиков взлетит до небес!)")
        call process_character (sa, appearance="blush false", text="(Мама, вероятно, была бы против...)")
    else:
        call process_character (sa, appearance="blush false", text="Мы должны сделать специальные вещи на праздники!")
        call process_character (sa, appearance="blush false", text="Как на Хэллоуин мы могли бы одеваться и трахаться!")
        call process_character (si, appearance="blush false", text="Ха-ха, это возможно!")

    window auto
    call screen family_foursome_options(xalign = 0.98)
    return

label family_foursome_scene_revisit_simone_fuck:
    $ family_foursome_revisit_current_partner = si
    $ family_foursome_revisit_current_mode = "fuck"

    call static_still_ctc ("bg foursome_simonefuck")

    $ dice_roll = random.randint(1,3)
    if dice_roll == 1:
        call process_character (si, appearance="blush false", text="Никогда не думала, что мне понравится, когда другие будут смотреть, как я трахаюсь.")
        call process_character (si, appearance="blush false", text="Но это интересно видеть реакции [sa.say_name] и [k.say_name]!")
    elif dice_roll == 2:
        call process_character (si, appearance="blush false", text="Нам понадобится мягкое ковровое покрытие для гостиной.")
        call process_character (si, appearance="blush false", text="Это должно сделать секс комфортнее!")
        call process_character (k, appearance="blush false", text="Оно должно легко мыться тоже, Мама.")
    else:
        call process_character (si, appearance="blush false", text="Думаю, у каждого из нас должен быть под рукой халат.")
        call process_character (si, appearance="blush false", text="Никогда не знаешь, когда нам вдруг понадобится их надеть!")
    window auto
    call screen family_foursome_options(xalign = 0.4)
    return

label family_foursome_scene_revisit_simone_blowjob:
    $ family_foursome_revisit_current_partner = si
    $ family_foursome_revisit_current_mode = "bj"

    call static_still_ctc ("bg simone_underblowjob_nude")

    $ dice_roll = random.randint(1,3)
    if dice_roll == 1:
        call process_character (si, appearance="blush false", text="Ты хочешь, чтобы я отсосала у тебя сразу после того, как ты вернешься из школы?")
        call process_character (n, appearance="blush false", text="Наверное, Мама.")
        call process_character (si, appearance="blush false", text="Просто спусти штаны, когда войдешь, и я пойму, что к чему!")
    elif dice_roll == 2:
        call process_character (si, appearance="blush false", text="Мне нужно срочно купить вам новую одежду.")
        call process_character (si, appearance="blush false", text="Все больше и больше пятен появляется на нашем нижнем белье!")
    else:

        call process_character (si, appearance="blush false", text="Я думаю, что весь этот секс сделал мою грудь более упругой!")
        call process_character (si, appearance="blush false", text="Должно быть, вся эта активность действует так!")

    window auto
    call screen family_foursome_options(xalign = 0.02)
    return

label family_foursome_scene_revisit_threesome:
    $ family_foursome_revisit_current_partner = si
    $ family_foursome_revisit_current_mode = "threesome"

    call static_still_ctc ("bg foursome_groupfucknosam")

    call process_character (sa, appearance="blush false", text="Я очень хочу сфотографировать это!")
    call process_character (si, appearance="blush false", text="[sa.say_name], нет...")
    call process_character (si, appearance="blush false", text="Это только для наших глаз!")
    call process_character (k, appearance="blush false", text="Как бы мне не нравилось хвастаться своей задницей, я не думаю, что хочу, чтобы все смотрели на нее в интернете.")
    call process_character (sa, appearance="blush false", text="Что делать, если я обещаю не загружать его в интернет?")
    call process_character (k, appearance="blush false", text="Это все равно что пообещать больше никогда не играть в видеоигры...")

    window auto
    call screen family_foursome_options(xalign = 0.02)
    return

label family_foursome_scene_revisit_foursome:
    $ did_family_foursome_ff = True
    $ family_foursome_revisit_current_partner = si
    $ family_foursome_revisit_current_mode = "foursome"

    call static_still_ctc ("bg foursome_groupfuck")

    call process_character (k, appearance="blush false", text="Эй, [sa.say_name]...")
    call process_character (k, appearance="blush false", text="Если [n.say_name] кончает в мою задницу, ты должна вылизать её!")
    call process_character (sa, appearance="blush false", text="Хаха!")
    call process_character (sa, appearance="blush false", text="Только если [n.say_name] думает, что на это было бы здорово смотреть!")
    call process_character (si, appearance="blush false", text="Никогда не бывает скучно, когда мы вместе!")

    window auto
    call screen family_foursome_options(xalign = 0.02)
    return

label family_foursome_scene_revisit:
    $ play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)
    $ family_foursome_revisit_current_mode = None
    window auto
    call screen family_foursome_options(0.5)
    call family_foursome_scene_revisit_end
    return

label family_foursome_scene_revisit_end:
    python:
        scenes_completed.add("family_foursome_scene_revisit_kira")
        scenes_completed.add("family_foursome_scene_revisit_simone")
        scenes_completed.add("family_foursome_scene_revisit_sam")

    python:
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_received_blowjob", 1)
        stats.add_stat("times_had_group_sex", 1)
        stats.add_stat("times_cummed_in_mouth", 1)
        stats.add_stat("times_seen_butt", 1)
        stats.add_stat("times_seen_butthole", 1)
        stats.add_stat("times_given_anal_sex", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("family_foursome_scene_revisit", reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label kira_simone_threesome_extended_content:
    if not kira_simone_threesome_part_2_done:
        call kira_simone_threesome_extended_content_1st_time
    else:
        call kira_simone_threesome_extended_content_2nd_time
    return

label kira_simone_threesome_extended_content_1st_time:
    call fade_to_black (1)

    call process_character (si, appearance="blush false", text="Похоже, сейчас здесь никого нет.")
    call process_character (k, appearance="blush false", text="Перфекто!")
    call process_character (k, appearance="blush false", text="Теперь я могу показать тебе, что я могу сделать!")
    call process_character (k, appearance="blush false", text="Бросай эту одежду, [n.say_name]!")
    call process_character (k, appearance="blush false", text="Она просто помеха!")
    call process_character (si, appearance="blush false", text="Ты так быстро все сняла, [k.say_name]!")
    call process_character (k, appearance="blush false", text="Если ты думала, что это было впечатляюще, Мама, подожди, и ты увидишь это!")
    call process_character (n, appearance="blush false", text="Ух ты!")

    call static_still_ctc ("bg kirablowjob_69")

    call process_character (si, appearance="blush false", text="Ох, надо же, [k.say_name]!")
    call process_character (k, appearance="blush false", text="Вот именно!")
    call process_character (k, appearance="blush false", text="И вот мы в позе шестьдесят девять!")
    call process_character (n, appearance="blush false", text="Ха, ах!")
    call process_character (si, appearance="blush false", text="Держись за него крепче, [k.say_name]!")
    call process_character (k, appearance="blush false", text="О, да, я это сделаю!")
    call process_character (k, appearance="blush false", text="Ммф...")
    call process_character (n, appearance="blush false", text="(Я не ожидал, что [k.say_name] перевернёт меня, пока держит меня!)")
    call process_character (n, appearance="blush false", text="(Это было похоже на американские горки на секунду!)")
    call process_character (si, appearance="blush false", text="Все в порядке, дорогой?")
    call process_character (si, appearance="blush false", text="Скажите мне, если у тебя кружится голова.")
    call process_character (n, appearance="blush false", text="У меня все хорошо, Мама.")
    call process_character (k, appearance="blush false", text="Конечно, [n.say_name]!")
    call process_character (k, appearance="blush false", text="Ты будешь высосан!")
    call process_character (n, appearance="blush false", text="([k.say_name] не шутит!)")
    call process_character (n, appearance="blush false", text="(Она делает это так быстро!)")
    call process_character (k, appearance="blush false", text="Я беру твой хер, [n.say_name] так глубоко, что мой нос трогает твои яйца!")
    call process_character (k, appearance="blush false", text="Что ты думаешь об этом, Мама?")

    call process_character (si, appearance="blush false", text="(Моя дочь вполне глубокая глотка)")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="(Это...{w=1.0}возбуждает меня)")
    call process_character (si, appearance="blush false", text="(Мой сын и дочь делают это...)")
    call process_character (si, appearance="blush false", text="(Они выглядят так, как будто они полностью наслаждаются друг другом)")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="(Мне становится жарко в этом свитере...)")
    call process_character (k, appearance="blush false", text="Ммм... хм?")
    call process_character (k, appearance="blush false", text="Ты тоже раздеваешься, Мама?")
    call process_character (n, appearance="blush false", text="М-мама?")
    call process_character (si, appearance="blush false", text="Я не хотела быть лишней!")
    call process_character (si, appearance="blush false", text="Плюс я...{w=1.0}хотела попробовать вкус хера [n.say_name].")
    call process_character (k, appearance="blush false", text="Вау-хо, Мам!")
    call process_character (k, appearance="blush false", text="У тебя похотливый голос!")
    call process_character (k, appearance="blush false", text="Мне нравится эта сторона тебя!")
    call process_character (k, appearance="blush false", text="Эй, [n.say_name]!")
    call process_character (k, appearance="blush false", text="Тебе лучше быть готовым к Маме!")
    call process_character (k, appearance="blush false", text="У нее такой взгляд в глазах.")

    call process_character (n, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="Мамин рот хочет второй раунд с твоим членом!")
    call process_character (k, appearance="blush false", text="Удачи, [n.say_name]!")
    call process_character (n, appearance="blush false", text="У-удачи?")

    call static_still_ctc ("bg simone_underblowjob_clothed")

    call process_character (si, appearance="blush false", text="Ммф, Ммф, Ммн!")
    call process_character (n, appearance="blush false", text="Гааха!")
    call process_character (k, appearance="blush false", text="О да, Мам!")
    call process_character (k, appearance="blush false", text="Вот так!")
    call process_character (k, appearance="blush false", text="Поработай над этим членом!")
    call process_character (k, appearance="blush false", text="Ты так сильно хотела хер [n.say_name], что даже не полностью сняла свой верх!")
    call process_character (n, appearance="blush false", text="(Это не так, как мама обычно сосет!)")
    call process_character (n, appearance="blush false", text="(Она делает это так же сильно, как [k.say_name], может быть, еще сильнее!)")
    call process_character (k, appearance="blush false", text="Ха, посмотри на это, [n.say_name]!")
    call process_character (k, appearance="blush false", text="Ты не ожидал, что Мама будет так сосать!")
    call process_character (k, appearance="blush false", text="Это то, на что она действительно способна, бро!")
    call process_character (n, appearance="blush false", text="{i}Уфф!{/i}")
    call process_character (n, appearance="blush false", text="М-мама!")
    call process_character (si, appearance="blush false", text="{i}Хлёб, хлёб!{/i}")
    call process_character (k, appearance="blush false", text="Чем грязнее, тем лучше Мама!")

    call static_still_ctc ("bg simone_underblowjob_clothed_sloppy")

    call process_character (k, appearance="blush false", text="(Мама, должно быть, активировала свою внутреннюю шлюху или что-то еще!)")
    call process_character (k, appearance="blush false", text="(Она собирается оторваться с членом [n.say_name]!)")
    call process_character (k, appearance="blush false", text="(Слюна капает с ее подбородка на сиськи)")
    call process_character (k, appearance="blush false", text="(Мама - настоящая извращенка!)")
    call process_character (k, appearance="blush false", text="(И только посмотрите на размер ее дынек!)")
    call process_character (k, appearance="blush false", text="(Видя их в открытую, действительно многое понимаешь)")
    call process_character (k, appearance="blush false", text="(Они, вероятно, весят половину веса тела [n.say_name], ха-ха!)")
    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (k, appearance="blush false", text="Да, держись за ее голову, бро.")
    call process_character (k, appearance="blush false", text="Засунь мамино лицо себе в член.")
    call process_character (k, appearance="blush false", text="Зафиксируй её так!")
    call process_character (n, appearance="blush false", text="Мам, это нормально?")
    call process_character (si, appearance="blush false", text="Ммм...да детка.")
    call process_character (si, appearance="blush false", text="Засунь свой член мне в глотку.")
    call process_character (k, appearance="blush false", text="Сделай каждый момент с ней стоящим, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Да, да!")
    call process_character (n, appearance="blush false", text="Ах...{w=0.5}это кажется настолько невероятным!")
    call process_character (n, appearance="blush false", text="Я не думаю, что это может быть лучше.")
    call process_character (k, appearance="blush false", text="Ты не понимаешь?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="О, бро...")
    call process_character (k, appearance="blush false", text="Как же ты не прав...")
    call process_character (n, appearance="blush false", text="Д-да?")
    call process_character (k, appearance="blush false", text="Эй, Мам...")
    call process_character (k, appearance="blush false", text="Пусть каждый прокатится на члене [n.say_name].")
    call process_character (si, appearance="blush false", text="Ммм, это отличная идея, [k.say_name].")
    call process_character (k, appearance="blush false", text="Теперь ты узнаешь, что может быть лучше, [n.say_name].")
    call process_character (n, appearance="blush false", text="...")

    call fade_to_black (1)

    call process_character (k, appearance="blush false", text="Тебе лучше лечь на спину, бро...")
    call process_character (k, appearance="blush false", text="...")

    call static_still_ctc ("bg threesome_kirafuck_simonewatch")

    call process_character (k, appearance="blush false", text="Ммм да, это действительно хорошо!")
    call process_character (k, appearance="blush false", text="Тебе нравится, что ты можешь видеть мою киску на своём члене, [n.say_name]?")
    call process_character (k, appearance="blush false", text="Ты можешь увидеть всё действие!")
    call process_character (si, appearance="blush false", text="Я надеюсь, что [n.say_name] сможет справиться со всей силой, с которой ты давишь на него [k.say_name].")
    call process_character (k, appearance="blush false", text="Для него это ничего не значит.")
    call process_character (k, appearance="blush false", text="Я тщательно подготовила тело [n.say_name] для такого рода вещей!")
    call process_character (n, appearance="blush false", text="Ох, ох!")
    call process_character (si, appearance="blush false", text="Мой-мой-мой...")
    call process_character (si, appearance="blush false", text="Так это обычная процедура для вас двоих.")
    call process_character (k, appearance="blush false", text="Единственное, что я скажу о [n.say_name]...")
    call process_character (k, appearance="blush false", text="Он подходит для меня по всем параметрам, Мама!")
    call process_character (k, appearance="blush false", text="Если я попробую что-то новое, он сразу ухватится за это.")
    call process_character (k, appearance="blush false", text="Чтобы не отставать и иметь достаточно сил, чтобы удовлетворить меня?")
    call process_character (k, appearance="blush false", text="Бро не имеет себе равных в моих глазах!")
    call process_character (si, appearance="blush false", text="[k.say_name] дала тебе высокую оценку, [n.say_name]!")
    call process_character (si, appearance="blush false", text="Это нужно заслужить, чтобы получить такие слова от твоей сестры.")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}.. Д-Да.")
    call process_character (k, appearance="blush false", text="Плюс это похоже на лучшую версию секса по дружбе.")
    call process_character (k, appearance="blush false", text="Это секс по родству!")
    call process_character (si, appearance="blush false", text="Хаха, [k.say_name]!")
    call process_character (k, appearance="blush false", text="Эй, я все еще люблю его как своего глупого маленького бро.")
    call process_character (k, appearance="blush false", text="Разница лишь в том, что мы проводим время вместе немного иначе, чем большинство братьев и сестер...")
    call process_character (n, appearance="blush false", text="И мне это нравится.")
    call process_character (si, appearance="blush false", text="Хаха!")
    call process_character (k, appearance="blush false", text="У тебя и [n.say_name] также не типичные отношения матери и сына...")
    call process_character (k, appearance="blush false", text="Почему бы тебе не показать их мне, Мама?")
    call process_character (k, appearance="blush false", text="Покажи мне, как ты и [n.say_name] наслаждайтесь друг другом.")
    call process_character (si, appearance="blush false", text="Что бы ты хотела [k.say_name]?")
    call process_character (k, appearance="blush false", text="Я видела вас двоих раньше издалека...")
    call process_character (k, appearance="blush false", text="Вы трахаетесь так сильно, что [n.say_name] падает в обморок на тебе!")
    call process_character (si, appearance="blush false", text="[n.say_name] имеет тенденцию делать это со мной, да.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Но ты так хорошо отдыхаешь, когда это происходит, милый!")
    call process_character (k, appearance="blush false", text="У тебя не будет проблем с подсчетом овец сегодня вечером, бро!")

    call static_still_ctc ("bg threesome_simonefuck_kirawatch")

    call process_character (n, appearance="blush false", text="Ах...Мама, аах...")
    call process_character (si, appearance="blush false", text="Это хорошо для тебя, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (k, appearance="blush false", text="Оседлай этот хер, Мама!")
    call process_character (si, appearance="blush false", text="Да!")
    call process_character (si, appearance="blush false", text="Трахни Мамочку!")
    call process_character (n, appearance="blush false", text="Ха-ах!")
    call process_character (k, appearance="blush false", text="(Это как бы мой личный просмотр!)")
    call process_character (k, appearance="blush false", text="(У меня не будет проблем с тем, чтобы держать себя мокрой во время просмотра!)")
    call process_character (k, appearance="blush false", text="(Черт, мамина задница такая широкая!)")
    call process_character (k, appearance="blush false", text="(Хер [n.say_name] находится где-то там внизу, ха!)")
    call process_character (k, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="(Это объясняет, почему [n.say_name] любит щупать маму)")
    call process_character (k, appearance="blush false", text="(Я получаю такое удовольствие от того, как он это делает так небрежно)")
    call process_character (k, appearance="blush false", text="(Мама готовит ужин, и вдруг появляется [n.say_name] хватаясь за ее сиськи или задницу!)")
    call process_character (k, appearance="blush false", text="(Мне нравится, как он пытается найти ее сосок под всей ее одеждой)")
    call process_character (k, appearance="blush false", text="(Бро полон решимости получить несколько щипков)")
    call process_character (k, appearance="blush false", text="(Это приближается к вершине извращения!)")
    call process_character (k, appearance="blush false", text="(И за этим здорово наблюдать!)")
    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="([k.say_name] мастурбирует на то, как [n.say_name] и я трахаемся)")
    call process_character (si, appearance="blush false", text="(Это невероятно, насколько спокойной я стала к этому!)")
    call process_character (si, appearance="blush false", text="(Я сделала самый большой разворот на 180 градусов этим летом)")
    call process_character (si, appearance="blush false", text="([n.say_name] смог сломать стену, которую я построила для секса)")
    call process_character (si, appearance="blush false", text="(Не только это, он также попал под воздействие своей старшей сестры!)")
    call process_character (si, appearance="blush false", text="(У нас в доме происходит маленькая сексуальная революция!)")
    call process_character (k, appearance="blush false", text="Я готова вернуться в строй!")
    call process_character (k, appearance="blush false", text="Ты должен вставить в мою задницу немного, [n.say_name]!")
    call process_character (si, appearance="blush false", text="Ты много занималась аналом до этого, [k.say_name]?")
    call process_character (k, appearance="blush false", text="Я раньше много занимался аналом?")
    call process_character (k, appearance="blush false", text="Я сделала это достаточно раз, чтобы считаться анальным мастером!")
    call process_character (si, appearance="blush false", text="Хаха!")
    call process_character (si, appearance="blush false", text="Анальный мастер, [k.say_name]?")
    call process_character (si, appearance="blush false", text="Это была бы уникальная запись в резюме!")
    call process_character (k, appearance="blush false", text="[n.say_name] и я покажу тебе нашу команду по жопотраху!")

    call fade_to_black (1)

    call process_character (k, appearance="blush false", text="Хорошо, поднимаю задницу в воздух.")
    call process_character (k, appearance="blush false", text="Хер [n.say_name] стучится в мою заднюю дверь и...")
    call process_character (k, appearance="blush false", text="Дави-дави-дави!")

    call static_still_ctc ("bg foursome_groupfucknosam")

    call process_character (k, appearance="blush false", text="И он там!")
    call process_character (k, appearance="blush false", text="Ах да, он там!")
    call process_character (n, appearance="blush false", text="Ммф!")
    call process_character (k, appearance="blush false", text="Ха, как хорошо, Мама!")
    call process_character (k, appearance="blush false", text="Подавай классическую сиськодушилку!")
    call process_character (si, appearance="blush false", text="Я хотела показать вам своё грудное мастерство!")
    call process_character (n, appearance="blush false", text="Хм?")
    call process_character (k, appearance="blush false", text="Грудное мастерство, Мама?")
    call process_character (si, appearance="blush false", text="Я знаю, это прозвучало не так круто, когда я это сказала!")
    call process_character (k, appearance="blush false", text="Лицо [n.say_name] довольно глубоко в твоих сиськах, Мама!")
    call process_character (k, appearance="blush false", text="Я не думаю, что он хочет подниматься на воздух, ха-ха!")
    call process_character (n, appearance="blush false", text="Мм, Мм!")
    call process_character (k, appearance="blush false", text="Бьюсь об заклад [n.say_name] любит твои сиськи так же, как он любит мою задницу, не так ли Мама?")
    call process_character (si, appearance="blush false", text="Это точное сравнение!")
    call process_character (si, appearance="blush false", text="[n.say_name] будет смотреть на мою грудь так внимательно, что он даже не узнает, что я с ним разговариваю!")
    call process_character (k, appearance="blush false", text="Он постоянно терял счет моим упражнениям на корточках, потому что моя задница слишком отвлекала!")
    call process_character (k, appearance="blush false", text="Так это значит...{w=1.0}[n.say_name] - любитель задниц и сисек!")
    call process_character (si, appearance="blush false", text="Хаха!")
    call process_character (si, appearance="blush false", text="Он никогда не сможет выбрать одно из двух!")
    call process_character (si, appearance="blush false", text="Так как ему просто нравятся оба варианта!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ахх...")
    call process_character (n, appearance="blush false", text="Я очень близок к тому, чтобы кончить.")
    call process_character (k, appearance="blush false", text="Тогда давай дадим тебе место, что запустить этот снаряд!")
    call process_character (k, appearance="blush false", text="Моя киска подготовлена для мега нагрузки, бро!")
    call process_character (si, appearance="blush false", text="Я совершенно счастлива быть получателем также, [n.say_name].")
    call process_character (k, appearance="blush false", text="Мама тоже предлагает свою киску!")
    call process_character (k, appearance="blush false", text="Лучше сделай свой выбор быстро, прежде чем твой член сделает это за тебя!")

    menu:
        "Кончить в [k.say_name]":
            call static_still_ctc ("bg kiraahego_internal_nocum")

            call process_character (k, appearance="blush false", text="Давай вперёд, бро!")
            call process_character (n, appearance="blush false", text="Хаа, Ахх...")
            call process_character (n, appearance="blush false", text="Кончаю, кончаю!")
            call process_character (n, appearance="blush false", text="Гааах!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg kiraahego_internal_cum")

            call process_character (k, appearance="blush false", text="Оох, да...")
            call process_character (k, appearance="blush false", text="Кончай в мою киску, бро!")
            call process_character (n, appearance="blush false", text="Ннг, Ннг!")
            call process_character (k, appearance="blush false", text="Ммм...")
            call process_character (k, appearance="blush false", text="Ты всё сделал правильно в тот раз, [n.say_name].")
            call process_character (k, appearance="blush false", text="Не так много тебе нужно улучшить.")
            call process_character (k, appearance="blush false", text="Для этой позы в любом случае, хе-хе...")
            call process_character (n, appearance="blush false", text="{i}Фух.{/i}..")

            call process_character (k, appearance="blush false", text="В следующий раз я хочу увидеть, как ты опустошишь свои яйца в Маме.")
            call process_character (k, appearance="blush false", text="С ней нужно делиться орешками.")
            call process_character (si, appearance="blush false", text="Ха-ха, все эти термины и фразы ты придумываешь, [k.say_name]!")
        "Оплодотворить [k.say_name]":
            call static_still_ctc ("bg kiraahego_internal_nocum")

            call process_character (k, appearance="blush false", text="Давай вперёд, бро!")
            call process_character (n, appearance="blush false", text="Хаа, Ахх...")
            call process_character (k, appearance="blush false", text="(У меня мало сомнений, к чему приведут эти кремовые пироги...)")
            call process_character (k, appearance="blush false", text="(Не то чтобы я не знала раньше, но теперь я готова к результату)")
            call process_character (k, appearance="blush false", text="(Я принимаю твое семя, бро!)")
            call process_character (k, appearance="blush false", text="(Если ты хочешь оплодотворить мою матку, она открыта для сделки!)")
            call process_character (n, appearance="blush false", text="Кончаю, кончаю!")
            call process_character (n, appearance="blush false", text="Гааах!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg kiraahego_internal_cum")

            call process_character (k, appearance="blush false", text="Оох, да...")
            call process_character (k, appearance="blush false", text="Кончай в мою киску, бро!")
            call process_character (n, appearance="blush false", text="Ннг, Ннг!")
            call process_character (k, appearance="blush false", text="Ммм...")
            call process_character (k, appearance="blush false", text="Ты всё сделал правильно в тот раз, [n.say_name].")
            call process_character (k, appearance="blush false", text="Не так много тебе нужно улучшить.")
            call process_character (k, appearance="blush false", text="Для этой позы в любом случае, хе-хе...")
            call process_character (n, appearance="blush false", text="{i}Фух.{/i}..")

            call static_still_ctc ("bg KiraAhergo_Internal_Cum_Impreg")

            call process_character (k, appearance="blush false", text="В следующий раз я хочу увидеть, как ты опустошишь свои яйца в Маме.")
            call process_character (k, appearance="blush false", text="С ней нужно делиться орешками.")
            call process_character (si, appearance="blush false", text="Ха-ха, все эти термины и фразы ты придумываешь, [k.say_name]!")
        "Кончить в Маму":
            call static_still_ctc ("bg SimoneAhego_Internal_NoCum")
            call process_character (si, appearance="blush false", text="Ах да, ах да!")
            call process_character (si, appearance="blush false", text="Продолжай в том же духе, дорогой!")
            call process_character (n, appearance="blush false", text="Хаа, Ахх...")
            call process_character (n, appearance="blush false", text="(Мама раскачивается взад-вперед на мне)")
            call process_character (n, appearance="blush false", text="(Мой член трётся о ее киску еще сильнее!)")
            call process_character (n, appearance="blush false", text="(Я на грани взрыва!)")
            call process_character (si, appearance="blush false", text="(Глаза [n.say_name] плотно закрыты)")
            call process_character (si, appearance="blush false", text="(У него будет интенсивный оргазм)")
            call process_character (si, appearance="blush false", text="(Я знаю, что он будет после всех вещей, что [k.say_name] и я сделала с ним!)")
            call process_character (n, appearance="blush false", text="Мама, я сейчас кончу!")
            call process_character (n, appearance="blush false", text="Хууу!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg simoneahego_internal_cum")

            call process_character (si, appearance="blush false", text="Аах-хаа!")
            call process_character (si, appearance="blush false", text="Я кончаю тоже, сладкий!")
            call process_character (si, appearance="blush false", text="Я на грани!")
            call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
            call process_character (si, appearance="blush false", text="Я не вижу, чтобы сперма вытекала.")
            call process_character (si, appearance="blush false", text="Ты, должно быть, выстрелил глубоко в мою киску!")
            call process_character (si, appearance="blush false", text="...")

            call process_character (n, appearance="blush false", text="{i}Фух.{/i}..")
            call process_character (si, appearance="blush false", text="Я думаю, что [n.say_name] выдохся на данный момент, [k.say_name].")
            call process_character (k, appearance="blush false", text="Да, после того, как сильно он кончил.")
            call process_character (si, appearance="blush false", text="В следующий раз он должен кончить в тебя.")
            call process_character (k, appearance="blush false", text="Это справедливо - делиться!")
            call process_character (si, appearance="blush false", text="Хаха!")
        "Оплодотворить Маму":
            call static_still_ctc ("bg simoneahego_internal_nocum")

            call process_character (si, appearance="blush false", text="Ах да, ах да!")
            call process_character (si, appearance="blush false", text="Продолжай в том же духе дорогая!")
            call process_character (n, appearance="blush false", text="Хаа, Ахх...")
            call process_character (n, appearance="blush false", text="(Мама раскачивается взад-вперед на мне)")
            call process_character (n, appearance="blush false", text="(Мой член трётся о ее киску еще сильнее!)")
            call process_character (n, appearance="blush false", text="(Я на грани взрыва!)")
            call process_character (si, appearance="blush false", text="(Глаза [n.say_name] плотно закрыты)")
            call process_character (si, appearance="blush false", text="(У него будет интенсивный оргазм)")
            call process_character (si, appearance="blush false", text="(Я знаю, что он будет после всех вещей, что [k.say_name] и я сделала с ним!)")
            call process_character (n, appearance="blush false", text="Мама, я сейчас кончу!")
            call process_character (n, appearance="blush false", text="Хууу!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg simoneahego_internal_cum")

            call process_character (si, appearance="blush false", text="Аах-хаа!")
            call process_character (si, appearance="blush false", text="Я кончаю тоже, сладкий!")
            call process_character (si, appearance="blush false", text="Я на грани!")
            call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
            call process_character (si, appearance="blush false", text="Я не вижу, чтобы сперма вытекала.")
            call process_character (si, appearance="blush false", text="Ты, должно быть, выстрелил глубоко в мою киску!")
            call process_character (si, appearance="blush false", text="...")

            call static_still_ctc ("bg simoneahego_internal_cum_impreg")

            call process_character (si, appearance="blush false", text="(Существует очень высокая вероятность, что [n.say_name] может быть просто...оплодотворил меня)")
            call process_character (si, appearance="blush false", text="(Конечно, я позволяла ему свободно кончать в мою киску, поэтому шансы всегда были высоки!)")
            call process_character (si, appearance="blush false", text="(Я просто должна проверить себя в течение следующих нескольких дней...)")
            call process_character (si, appearance="blush false", text="(Хотя, если я беременна, я буду счастлива, что это была сперма [n.say_name], которая слилась с моей яйцеклеткой!)")
            call process_character (n, appearance="blush false", text="{i}Фух.{/i}..")
            call process_character (si, appearance="blush false", text="Я думаю, что [n.say_name] выдохся на данный момент, [k.say_name].")
            call process_character (k, appearance="blush false", text="Да, после того, как сильно он кончил.")
            call process_character (si, appearance="blush false", text="В следующий раз он должен кончить в тебя.")
            call process_character (k, appearance="blush false", text="Это справедливо - делиться!")
            call process_character (si, appearance="blush false", text="Хаха!")


    $ kira_simone_threesome_part_2_done = True
    call kira_simone_threesome_scene_revisit_end
    return

screen kira_simone_threesome_extended_content_2nd_time_options(xalign=0.98):
    vbox:
        xalign xalign
        yalign 0.5
        spacing 30

        use main_menu_button(text="Трахнуть [k.say_name]", action=Jump("kira_simone_threesome_extended_content_kira_fuck"), text_size=44)
        use main_menu_button(text="Минет [k.say_name]", action=Jump("kira_simone_threesome_extended_content_kira_blowjob"), text_size=44)
        use main_menu_button(text="Трахнуть Маму", action=Jump("kira_simone_threesome_extended_content_simone_fuck"), text_size=44)
        use main_menu_button(text="Минет Мамы", action=Jump("kira_simone_threesome_extended_content_simone_blowjob"), text_size=44)
        use main_menu_button(text="Тройничок", action=Jump("kira_simone_threesome_extended_content_threesome"), text_size=44)
        if kira_simone_threesome_part_2_positions_chosen >= 2:
            use main_menu_button(text="Кончить", action=Jump("kira_simone_threesome_extended_content_cum"), text_size=44)



label kira_simone_threesome_extended_content_2nd_time:
    $ kira_simone_threesome_part_2_positions_chosen = 0
    $ kira_simone_threesome_part_2_done = True
    call screen kira_simone_threesome_extended_content_2nd_time_options
    return

label kira_simone_threesome_extended_content_cum:
    call process_character (k, appearance="blush false", text="Готов взорваться, бро?")

    menu:
        "Кончить в [k.say_name]":
            call static_still_ctc ("bg kiraahego_internal_nocum")
            call process_character (k, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="Хррм!")
            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg kiraahego_internal_cum")

            call process_character (k, appearance="blush false", text="Ааах дааа...")
            call process_character (k, appearance="blush false", text="Мощно кончил, бро!")
        "Оплодотворить [k.say_name]":
            call static_still_ctc ("bg kiraahego_internal_nocum")
            call process_character (k, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="Хррм!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
            call static_still_ctc ("bg kiraahergo_internal_cum_impreg")

            call process_character (k, appearance="blush false", text="Ааах дааа...")
            call process_character (k, appearance="blush false", text="Мощно кончил, бро!")
        "Кончить в Маму":
            call static_still_ctc ("bg simoneahego_internal_nocum")

            call process_character (si, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="Аах!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg simoneahego_internal_cum")

            call process_character (si, appearance="blush false", text="Ооох!")
            call process_character (si, appearance="blush false", text="Великолепно, конфетка!")
        "Оплодотворить Маму":

            call static_still_ctc ("bg simoneahego_internal_nocum")

            call process_character (si, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="Аах!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            call static_still_ctc ("bg simoneahego_internal_cum_impreg")

            call process_character (si, appearance="blush false", text="Ооох!")
            call process_character (si, appearance="blush false", text="Великолепно, конфетка!")

    call kira_simone_threesome_scene_revisit_end
    return

label kira_simone_threesome_extended_content_simone_blowjob:
    $ kira_simone_threesome_part_2_positions_chosen = kira_simone_threesome_part_2_positions_chosen + 1

    call static_still_ctc ("bg simone_underblowjob_nude")

    $ dice_roll = random.randint(1,3)
    if dice_roll == 1:
        call process_character (si, appearance="blush false", text="Ты хочешь, чтобы я отсосала у тебя сразу после того, как ты вернешься из школы?")
        call process_character (n, appearance="blush false", text="Наверное, Мама.")
        call process_character (si, appearance="blush false", text="Просто спусти штаны, когда войдешь, и я пойму, что к чему!")
    elif dice_roll == 2:
        call process_character (si, appearance="blush false", text="Мне нужно срочно купить вам новую одежду.")
        call process_character (si, appearance="blush false", text="Все больше и больше пятен появляется на нашем нижнем белье!")
    else:

        call process_character (si, appearance="blush false", text="Я думаю, что весь этот секс сделал мою грудь более упругой!")
        call process_character (si, appearance="blush false", text="Должно быть, вся эта активность действует так!")

    call screen kira_simone_threesome_extended_content_2nd_time_options
    return

label kira_simone_threesome_extended_content_threesome:
    $ kira_simone_threesome_part_2_positions_chosen = kira_simone_threesome_part_2_positions_chosen + 1


    call static_still_ctc ("bg foursome_groupfucknosam")

    call process_character (k, appearance="blush false", text="Эй, [n.say_name]...")
    call process_character (k, appearance="blush false", text="Если ты кончишь в мою задницу, ты должен сказать Маме, чтобы вылизала её!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="[k.say_name], ты такая извращенка!")
    call process_character (k, appearance="blush false", text="Я считаю это комплиментом!")

    call screen kira_simone_threesome_extended_content_2nd_time_options
    return

label kira_simone_threesome_extended_content_simone_fuck:
    $ kira_simone_threesome_part_2_positions_chosen = kira_simone_threesome_part_2_positions_chosen + 1

    call static_still_ctc ("bg threesome_simonefuck_kirawatch")

    $ dice_roll = random.randint(1,3)
    if dice_roll == 1:
        call process_character (si, appearance="blush false", text="Никогда не думала, что мне понравится, когда другие будут смотреть, как я трахаюсь.")
        call process_character (si, appearance="blush false", text="Но это забавно видеть реакции [k.say_name]!")
    elif dice_roll == 2:
        call process_character (si, appearance="blush false", text="Нам понадобится мягкое ковровое покрытие для гостиной.")
        call process_character (si, appearance="blush false", text="Это должно сделать секс комфортнее!")
        call process_character (k, appearance="blush false", text="Оно должно легко мыться тоже, Мама.")
    else:
        call process_character (si, appearance="blush false", text="Думаю, у каждого из нас должен быть под рукой халат.")
        call process_character (si, appearance="blush false", text="Никогда не знаешь, когда нам вдруг понадобится их надеть!")


    call screen kira_simone_threesome_extended_content_2nd_time_options
    return

label kira_simone_threesome_extended_content_kira_fuck:
    $ kira_simone_threesome_part_2_positions_chosen = kira_simone_threesome_part_2_positions_chosen + 1

    call static_still_ctc ("bg threesome_kirafuck_simonewatch")

    $ dice_roll = random.randint(1,3)

    if dice_roll == 1:
        call process_character (k, appearance="blush false", text="Мы должны смотреть порно по телевизору, когда мы делаем это вместе.")
        call process_character (k, appearance="blush false", text="Тогда мы могли бы попробовать имитировать то, что порнозвезды могут сделать!")
    elif dice_roll == 2:
        call process_character (k, appearance="blush false", text="Если мы когда-нибудь замерзнем зимой, это нас согреет!")
    else:
        call process_character (k, appearance="blush false", text="Нет конца наших трахфестивалей!")
        call process_character (k, appearance="blush false", text="Так и должно быть!")


    call screen kira_simone_threesome_extended_content_2nd_time_options
    return

label kira_simone_threesome_extended_content_kira_blowjob:
    $ kira_simone_threesome_part_2_positions_chosen = kira_simone_threesome_part_2_positions_chosen + 1

    call static_still_ctc ("bg kirablowjob_69")

    $ dice_roll = random.randint(1,3)
    if dice_roll == 1:
        call process_character (k, appearance="blush false", text="Держу пари, я могу пронести тебя по дому вот так, ха-ха!")
        call process_character (si, appearance="blush false", text="Это было бы зрелище!")
    elif dice_roll == 2:
        call process_character (k, appearance="blush false", text="Кому нужны гири, когда есть ты, бро?")
        call process_character (k, appearance="blush false", text="Теперь мне не нужно копить на набор гантелей!")
    else:
        call process_character (k, appearance="blush false", text="У тебя уже есть хорошие навыки лизания киски, [n.say_name]!")
        call process_character (k, appearance="blush false", text="Мне нужно просить тебя делать это чаще со мной!")


    call screen kira_simone_threesome_extended_content_2nd_time_options
    return

label kira_simone_threesome_extended_content_phase_1:
    call screen kira_simone_threesome_extended_content_2nd_time_options
    return

label finale_scene(dream=False):
    call finale_scene_sex (dream=dream)

    return

label finale_scene_initialize:
    $ finale_julia_sam = "sam_scene_dream" in scenes_completed and "julia_scene_anal" in scenes_completed and "family_foursome_scene" in scenes_completed and "sam_simone_threesome_scene" in scenes_completed and "sam_julia_threesome_scene" in scenes_completed

    $ finale_chose_edna = False
    $ finale_chose_janet = False
    $ finale_chose_julia = False
    $ finale_chose_sam = False
    $ finale_chose_simone = False
    $ finale_chose_kira = False
    $ finale_chose_kacey = False
    $ finale_chose_vicky = False

    $ finale_cum_edna = False
    $ finale_cum_janet = False
    $ finale_cum_julia = False
    $ finale_cum_sam = False
    $ finale_cum_simone = False
    $ finale_cum_kira = False
    $ finale_cum_kacey = False
    $ finale_cum_vicky = False

    $ finale_kacey_arrived = False
    $ finale_vicky_arrived = False
    $ finale_fucked_amount = 0
    $ finale_cum_amount = 0

    if finale_julia_sam:
        $ finale_cum_amount_goal = 8
    else:
        $ finale_cum_amount_goal = 6

    return

label finale_scene_sex(dream=False):
    $ renpy.start_predict("edna_titfuck_nude_anim")

    call finale_scene_initialize

    if finale_julia_sam:
        $ finale_fucked_amount_goal = 8
    else:
        $ finale_fucked_amount_goal = 6

    call process_scene_beginning (bg="bg kira_room_evening", char_tuple_array=[], dream=dream)

    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="(Сегодняшний вечер идеально подходит для пробежки!)")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="(На улице становится прохладнее)")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="...")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="(Я должна попросить [n.say_name] присоединиться ко мне)")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="(Это даст ему изменение темпа от беговой дорожки)")

    call process_new_location (bg="bg nate_room_evening", dream=dream)

    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Эй [n.say_name]!")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="{cps=40}Ты хочешь пойти-{/cps}{w=0.75}{nw}")
    call process_character (k, appearance="outfit clothes pose handhip face curious blush false", text="...")
    call process_character (k, appearance="outfit clothes pose handhip face curious blush false", text="(Где он, черт возьми?)")
    call process_character (k, appearance="outfit clothes pose armcross face curious blush false", text="(Я знаю, что он не трахает маму, она внизу убирает кухню)")
    call process_character (k, appearance="outfit clothes pose armcross face curious blush false", text="(Я не видела его и в комнате [sa.say_name] тоже)")
    call process_character (k, appearance="outfit clothes pose armcross face curious blush false", text="...")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="(Я попробую позвонить ему)")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="(Если он не ответит, тогда я просто пойду одна)")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="...")

    "{i}Дзинь-Дзинь-Дзинь!{/i}"

    call process_character (k, appearance="outfit clothes pose handhip face curious blush false", text="...")

    "{i}Дзинь-Дзинь-Дзинь!{/i}"

    call process_character (k, appearance="outfit clothes pose armcross face curious blush false", text="(Что за...)")
    call process_character (k, appearance="outfit clothes pose armcross face curious blush false", text="(Серьезно [n.say_name]?)")
    call process_character (k, appearance="outfit clothes pose armcross face curious blush false", text="(Ты оставил телефон в своей комнате?)")
    call process_character (k, appearance="outfit clothes pose handhip face concerned blush false", text="{i}Вздох.{/i}..")
    call process_character (k, appearance="outfit clothes pose handhip face concerned blush false", text="(Мой брат иногда просто летает в облаках...)")
    call process_character (k, appearance="outfit clothes pose handhip face concerned blush false", text="(В один из таких дней он потеряет телефон или его украдут, это неизбежно)")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="(Бьюсь об заклад, у него даже нет пароля на телефоне)")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="...")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="(Да, знала это!)")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="(Я могу просто открыть его телефон без усилий!)")

    "{i}Дзинь!{/i}"

    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="(И, конечно же, входящие СМСки)")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="(Кто бы ни послал их, придется подождать ответа от моего брата)")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="...")
    call process_character (k, appearance="outfit clothes pose handhip face curious blush false", text="([gloryhole_girl.say_name]?)")
    call process_character (k, appearance="outfit clothes pose armcross face curious blush false", text="(Я никогда не слышала, чтобы [n.say_name] упоминал девушку по имени [gloryhole_girl.say_name]...)")
    call process_character (k, appearance="outfit clothes pose armcross face curious blush false", text="...")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="\"Я буду в парке через несколько минут [n.say_name]!\"")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="\"Не могу дождаться, когда мы повеселимся вместе! <3\"")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="(Хорошо, должно быть...)")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="([n.say_name] завел себе подружку!)")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="(Похоже, она тоже его любит)")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="(Бро, должно быть, хочет утаить это, встречаясь с ней в парке ночью)")
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="(Мне очень любопытно посмотреть, с какой девушкой [n.say_name] связался!)")
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="(Я знаю, куда пойду на пробежку!)")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="(Если [n.say_name] случайно заметил меня, я просто скажу, что это чистое совпадение, что я бегаю по тому же парку)")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="(Да, чистое совпадение...)")

    call fade_to_black (1)


    call process_new_location ("bg park_evening", dream=dream)

    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="...")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="(Хорошо, где он, где он...)")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="...")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="(А-ха!)")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="(Я вижу [n.say_name]!)")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="(Он рядом с одним из туалетов)")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="(Ты у меня под прицелом, бро!)")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="(Девушки не видно...{w=1.0} пока)")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="(Я уверена, что они встречаются возле туалетов, так как это очевидный ориентир)")
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="(Требуется дальнейшее расследование!)")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="...")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="([n.say_name] заходит)")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="(Пока он там, я буду присматривать за его девушкой...)")

    call fade_to_black (1)


    call process_new_location ("bg park_evening", dream=dream)

    call process_character (k, appearance="outfit clothes pose armcross face curious blush false", text="...")
    call process_character (k, appearance="outfit clothes pose armcross face curious blush false", text="(Сколько времени [n.say_name] собирается быть там?)")
    call process_character (k, appearance="outfit clothes pose armcross face curious blush false", text="(Он обделался или что?)")
    call process_character (k, appearance="outfit clothes pose handhip face concerned blush false", text="(И я никого не видела здесь с тех пор, как он вошел)")
    call process_character (k, appearance="outfit clothes pose handhip face concerned blush false", text="(Нет других сообщений от [gloryhole_girl.say_name], либо...)")
    call process_character (k, appearance="outfit clothes pose handhip face concerned blush false", text="...{p}...")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="(Наконец-то он появился!)")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="...")
    call process_character (k, appearance="outfit clothes pose armsup face curious blush false", text="(Почему [n.say_name] выглядят потными?)")
    call process_character (k, appearance="outfit clothes pose handhip face curious blush false", text="(Он сильно потеет, только когда он...)")
    call process_character (k, appearance="outfit clothes pose handhip face shocked blush false", text="!")
    call process_character (k, appearance="outfit clothes pose handhip face shocked blush false", text="(Стоп, стоп, какого хрена?!)")
    call process_character (k, appearance="outfit clothes pose armcross face shocked blush false", text="(Девушка только что вышла из того же туалета, что и [n.say_name]!)")
    call process_character (k, appearance="outfit clothes pose armcross face curious blush false", text="(И она с ним разговаривает...)")
    call process_character (k, appearance="outfit clothes pose armcross face curious blush false", text="...")
    call process_character (k, appearance="outfit clothes pose handhip face embarrassed blush false", text="(Может быть...{w=1.0}[gloryhole_girl.say_name]?)")
    call process_character (k, appearance="outfit clothes pose handhip face embarrassed blush false", text="(Она, кажется, тоже вся потная)")
    call process_character (k, appearance="outfit clothes pose handhip face shocked blush false", text="(Бро делал то, что, я думаю, он делал там с ней?)")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="...{p}...")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="(Они обнимаются)")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="([n.say_name] хватает ее задницу...{w=0.5}бро крутой)")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="(У меня нет сомнений, что это Кейси)")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="...")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="(Похоже, они расстаются)")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="...")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="(Мне нужно быстро заглянуть в туалет)")
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="(Если там было совершено какое-нибудь грязное дело, я узнаю довольно быстро...)")

    call fade_to_black (1)


    call process_new_location ("bg public_bathroom_evening", dream=dream)

    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="(Здесь сильный, знакомый запах)")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="(И это не обычный запах, связанный с туалетом)")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="(Но мне нужно больше доказательств...)")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="...{p}...")

    call static_still_ctc ("bg gloryhole")

    call process_character (k, appearance="blush false", text="(Ну, не может быть более очевидным, чем это...)")
    call process_character (k, appearance="blush false", text="(Дыра славы!)")
    call process_character (k, appearance="blush false", text="(Вау, посмотрите на пол прямо под ним!)")
    call process_character (k, appearance="blush false", text="(Это свежие пятна спермы)")
    call process_character (k, appearance="blush false", text="(Нити спермы все еще скользят по двери)")
    call process_character (k, appearance="blush false", text="(Это все, что мне нужно увидеть!)")
    call process_character (k, appearance="blush false", text="([n.say_name] трахает эту [gloryhole_girl.say_name]!)")
    call process_character (k, appearance="blush false", text="(И, судя по всему, это было не раз!)")
    call process_character (k, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="(Как им удалось встретиться друг с другом?)")
    call process_character (k, appearance="blush false", text="(И почему [n.say_name] все еще не пригласил ее к нам домой?)")
    call process_character (k, appearance="blush false", text="(Она похожа на девушку, которую я хочу узнать!)")
    call process_character (k, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="(Подожди секунду...{w=1.0} Телефон [n.say_name]...)")
    call process_character (k, appearance="blush false", text="([gloryhole_girl.say_name] подумает, что это [n.say_name] пишет ей)")
    call process_character (k, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="(Я думаю, я устрою встречу с этой [gloryhole_girl.say_name])")
    call process_character (k, appearance="blush false", text="(Тогда я смогу узнать больше обо всех сочных, липких деталях между ней и [n.say_name], хехе...)")

    call fade_to_black (1)


    call process_new_location ("bg kitchen_daytime", dream=dream)

    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face aroused blush false", text="{i}Зевает.{/i}..")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Долгая ночь была, а?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Угу.")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Ты не сможешь ложиться спать так поздно, скоро начнется школа.")
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="Если только ты не собираешься спать во время уроков!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Не могу поверить, что лето почти закончилось...")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Осталось еще немного времени.")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Ты просто должен извлечь максимум пользы из него!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Да, я должен...")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Лично я хочу провести еще несколько пляжных дней!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Я тоже!")
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="Почему бы нам не пойти туда сегодня?")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="Я жажду еще одного волейбольного матча!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Мы можем попросить Бабушку присоединиться к нам?")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Конечно.")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Сомневаюсь, что она откажется от приглашения на пляж.")

    call fade_to_black (1)


    call process_new_location ("bg beach_daytime", dream=dream)


    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false")


    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false")

    $ replace_position = True
    $ k.position = "right"

    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Я рада, что вы двое смогли сегодня добраться до пляжа!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Да, мы тоже!")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Скоро нам понадобятся куртки, если мы хотим быть здесь.")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Осень быстро приближается.")
    call process_character (n, appearance="outfit swimsuit pose handsdown face concerned blush false", text="И школа тоже...")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face curious blush false mouth red", text="Действительно, скоро снова в школу [n.say_name]?")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="Такое чувство, что лето только началось несколько дней назад!")

    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false")

    call process_character (k, appearance="outfit bikini pose armcross face concerned blush false", text="Хуже всего то, как долго ждать следующего лета.")
    call process_character (k, appearance="outfit bikini pose armcross face concerned blush false", text="Зима тянется слишком долго.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Я точно знаю, что ты чувствуешь [k.say_name]!")
    call process_character (edna, appearance="outfit swimsuit pose handhip face embarrassed blush false mouth red", text="Мои суставы не ценят холодную погоду!")
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="Ну, прежде чем эти холодные фронты начнут наступать, я сокрушу их на волейболе еще немного!")

    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red")

    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="[n.say_name], ты хочешь объединиться, чтобы мы могли доминировать?")
    call process_character (n, appearance="outfit swimsuit pose behindhead face neutral blush false", text="Хмм...")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Может ли [n.say_name] присоединиться к тебе немного позже [k.say_name]?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Я хочу поговорить с ним о том, что будет происходить в его новой школе и чему он будет учиться!")

    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false")


    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false")

    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Хорошо, Бабушка.")
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="Пока я жду, я помогу команде, которая нуждается в дополнительном игроке!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Сделай их, внучка!")

    call character_leave_dissolve (k)
    pause 0.5

    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false", text="...")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="Когда ты вернешься в школу, я не буду видеть тебя так часто.")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="Ты будешь занят учебой, сдачей тестов...")
    call process_character (n, appearance="outfit swimsuit pose behindhead face concerned blush false", text="И написанием текстов...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="[k.say_name] будет занята некоторое время.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face flirt blush false mouth red", text="Ты хочешь сходить в мою квартиру?")
    call process_character (edna, appearance="outfit swimsuit pose handhip face flirt blush false mouth red", text="Есть определенные вещи, которые мы можем сделать, пока мы там...")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face neutral blush false", text="Да, конечно, Бабушка...")

    call fade_to_black (1)


    call process_new_location ("bg beach_daytime", dream=dream)

    call process_character (k, appearance="outfit bikini pose armcross face angry blush false", text="Не думаю, что раньше играла с более дерьмовой командой!")
    call process_character (k, appearance="outfit bikini pose armcross face angry blush false", text="Они едва могли отбить мяч через сетку!")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="[n.say_name], ты и я бы размазали их по полу!")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Давай вернемся туда и покажем им, кто здесь хозяин...")
    call process_character (k, appearance="outfit bikini pose armsup face curious blush false", text="...")
    call process_character (k, appearance="outfit bikini pose handhip face curious blush false", text="(Куда [n.say_name] и Бабушка ушли?)")
    call process_character (k, appearance="outfit bikini pose handhip face curious blush false", text="(Их вещи все еще здесь)")
    call process_character (k, appearance="outfit bikini pose handhip face curious blush false", text="...")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="(Держу пари, они делают бутерброды в кондоминиуме)")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="(Мне нужно захватить несколько дополнительных бутылок с водой, поэтому я быстро вернусь туда)")

    call fade_to_black (1)


    call process_new_location ("bg edna_house_daytime", dream=dream)

    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="...")
    call process_character (k, appearance="outfit bikini pose handhip face curious blush false", text="(Черт, неужели я потеряла их?)")
    call process_character (k, appearance="outfit bikini pose handhip face curious blush false", text="(Нет, я не могла этого сделать.)")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="(Я бы заметила их в коридоре или вестибюле)")
    call process_character (k, appearance="outfit bikini pose armcross face curious blush false", text="(Нет бутербродов или чего-нибудь на кухне)")
    call process_character (k, appearance="outfit bikini pose armcross face curious blush false", text="(Зачем они тогда вернулись сюда?)")
    call process_character (k, appearance="outfit bikini pose handhip face curious blush false", text="([n.say_name] укусила медуза или еще что?)")
    call process_character (k, appearance="outfit bikini pose handhip face curious blush false", text="...")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="(Ох, вот они!)")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="(Они выходят на балкон)")
    call process_character (k, appearance="outfit bikini pose armsup face curious blush false", text="(Погоди...{w=1.0}они там голые?)")
    call process_character (k, appearance="outfit bikini pose armcross face curious blush false", text="{cps=40}(И почему бабушка стоит на коленях -){/cps}{w=0.75}{nw}")
    call process_character (k, appearance="outfit bikini pose armcross face shocked blush false", text="!!")

    $ set_main_animation_speed(1.0)
    $ edna_titfuck_had_slow_speed_message = False
    $ edna_titfuck_had_normal_speed_message = False
    $ edna_titfuck_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    show anim_nothing_image as main_animation at main_animation_transform(IA_Animation_Edna_Titfuck_Nude_Info())
    with Dissolve(1.15)
    show bg white


    pause 
    $ quick_menu = True
    $ no_bust_art = True

    call process_character (k, appearance="blush false", text="(Что за дерьмо?!)")
    call process_character (k, appearance="blush false", text="(У меня, что галлюцинации от теплового удара?!)")
    call process_character (k, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="(Это...{w=1.0}это реально)")
    call process_character (k, appearance="blush false", text="(Бабушка и [n.say_name] ...)")
    call process_character (k, appearance="blush false", text="(Бабушка...{w=1.0}и [n.say_name]!)")
    call process_character (k, appearance="blush false", text="(Даже представить себе такого не могу!)")
    call process_character (k, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="(Хотя...{w=1.0}Я помню, как бабушка в последнее время немного кокетничала с [n.say_name])")
    call process_character (k, appearance="blush false", text="(Но я думала, что она просто развлекается!)")
    call process_character (k, appearance="blush false", text="(Я не думала, что она хотела какого-то реального жесткого действия с членом бро!)")
    call process_character (k, appearance="blush false", text="(Я подумала, что в ее возрасте она уже прошла этот этап)")
    call process_character (k, appearance="blush false", text="(Я все неправильно поняла!)")

    window hide
    call edna_titfuck_set_speed (edna_titfuck_fastest_speed_multiplier)
    pause
    window auto

    call process_character (k, appearance="blush false", text="(А Бабуля круто проводит время!)")
    call process_character (k, appearance="blush false", text="(Она улыбалась все время, когда [n.say_name] держал его член между ее сиськами!)")
    call process_character (k, appearance="blush false", text="(И [n.say_name] не проявляет никаких признаков колебаний!)")
    call process_character (k, appearance="blush false", text="(Где этот нервный и неохотный брат, уставившийся на мою задницу!)")
    call process_character (k, appearance="blush false", text="(Теперь он - мамин удовлетворитель и бабушкин трахаль!)")
    call process_character (n, appearance="blush false", text="Ох, о да...")
    call process_character (n, appearance="blush false", text="Я кончаю, Бабушка!")
    call process_character (k, appearance="blush false", text="...")

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
    show bg edna_nude_titfuck_cumshot_surprise
    with Dissolve(1.5)

    pause
    $ quick_menu = True

    call process_character (n, appearance="blush false", text="Хнгаа!")
    call process_character (k, appearance="blush false", text="(Черт, какой мощный оргазм!)")

    call static_still_ctc ("bg edna_nude_titfuck_aftercum_smile")

    call process_character (k, appearance="blush false", text="([n.say_name] просто взорвал бабушкины сиськи спермой!)")
    call process_character (k, appearance="blush false", text="(Он извергался, как фонтан!)")
    call process_character (k, appearance="blush false", text="(И посмотрите на широкую улыбку Бабушки!)")
    call process_character (k, appearance="blush false", text="(Я не думаю, что видела, чтобы кто-нибудь показывал столько ликования по поводу траха...{w=0.5}кроме меня!)")
    call process_character (edna, appearance="blush false", text="Чувствуешь себя лучше, [n.say_name]?")
    call process_character (edna, appearance="blush false", text="Теперь ты будешь готов играть в волейбол со своей старшей сестрой!")
    call process_character (n, appearance="blush false", text="Да, я сделаю это, Бабушка!")
    call process_character (edna, appearance="blush false", text="Идем вниз к пляжу.")
    call process_character (edna, appearance="blush false", text="[k.say_name], вероятно, задается вопросом, где мы сейчас.")
    call process_character (k, appearance="blush false", text="(Черт, я должна выбраться отсюда!)")
    call process_character (k, appearance="blush false", text="(Я просто буду круто играть в течение оставшейся части дня)")

    call fade_to_black (1)


    $ renpy.stop_predict("edna_titfuck_nude_anim")
    call process_new_location (bg="bg edna_house_evening", dream=dream)

    $ k.position = "right"

    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false")

    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Это было самое долгое время, когда я была на пляже за один день!")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Но температура была слишком идеальной, чтобы тратить ее впустую!")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face happy blush false", text="Я думаю, что это был лучший пляжный день, Бабушка!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Я думаю, что это так!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Не было многолюдно, волны катились гладко...")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face happy blush false mouth red", text="И ты, и [k.say_name] остались непобежденными в волейболе!")
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="Благодаря моему верному удару я делаю мощные броски!")
    call process_character (n, appearance="outfit swimsuit pose behindhead face neutral blush false", text="Весь мои плавки в песке от игры.")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Из-за всех этих прыжков, которые я сделала, у меня тонна песка в заднице.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Сходи в душ, чтобы привести себя в порядок.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Если быть на пляже так долго, то начинаешь становиться немного грязным.")

    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Ты пойдешь первым, бро.")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Я поговорю с бабушкой, пока буду ждать.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Вот и славно [k.say_name].")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Не истрать всю горячую воду!")
    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false", text="Обещаю.")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="...")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="...{p}...")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="Я знаю, что ты видела меня на балконе с [n.say_name], [k.say_name].")
    call process_character (k, appearance="outfit bikini pose armcross face embarrassed blush false", text="!")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="Я краем глаза заметила твое ярко-зеленое бикини.")
    call process_character (k, appearance="outfit bikini pose armcross face embarrassed blush false", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Ты собиралась спросить меня об этом, я могу ответить.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Итак, я признаюсь тебе, что да, я занимаюсь сексом с [n.say_name].")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="...")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Ты на удивление хладнокровно рассказываешь мне об этом, Бабушка.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Ну, твоя реакция на это довольно сдержанная.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face curious blush false mouth red", text="Разве это не необычно?")
    call process_character (k, appearance="outfit bikini pose armcross face curious blush false", text="...")
    call process_character (k, appearance="outfit bikini pose armcross face curious blush false", text="Какое отношение к этому имеет моя реакция?")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="У тебя также был сексуальный опыт с [n.say_name].")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Это началось этим летом.")
    call process_character (k, appearance="outfit bikini pose armsup face embarrassed blush false", text="А?!")
    call process_character (k, appearance="outfit bikini pose armsup face embarrassed blush false", text="Как ты...")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Откуда я знаю?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="[n.say_name] любит говорить о тебе.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Он сказал мне, что ты даешь трахать сиськи дома.")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face curious blush false mouth red", text="И вы оба практикуете эти...{w=0.5}позиции Камасутры друг с другом?")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face happy blush false mouth red", text="Они вне моего диапазона гибкости!")
    call process_character (k, appearance="outfit bikini pose handhip face curious blush false", text="...")
    call process_character (k, appearance="outfit bikini pose handhip face curious blush false", text="Значит, [n.say_name] просто так разболтал все это тебе?")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Не сердись на [n.say_name], [k.say_name].")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Он говорит мне это только потому, что знает, что я поддерживаю его.")
    call process_character (k, appearance="outfit bikini pose armcross face embarrassed blush false", text="Ты поддерживаешь то, что [n.say_name] и я трахаемся, Бабушка?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Конечно!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Я думаю, что это круто!")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="Я...{w=1.0}не знала, что ты так увлечена этим.")

    if "family_foursome_scene" in scenes_completed or finale_julia_sam:
        call process_character (edna, appearance="pose handclasp face happy blush false", text="[n.say_name] не перестает говорить о групповушке, которую он имел с тобой, [sa.say_name] и [si.say_name] на днях!")
        call process_character (edna, appearance="pose handclasp face happy blush false", text="Хотела бы я на это посмотреть!")
    else:
        call process_character (edna, appearance="pose handclasp face happy blush false", text="[n.say_name] не перестает говорить о групповушке, которую он имел с тобой и [si.say_name] на днях!")
        call process_character (edna, appearance="pose handclasp face happy blush false", text="Хотела бы я на это посмотреть!")

    call process_character (k, appearance="outfit bikini pose armcross face happy blush false", text="Ты...{w=1.0} бабушка, нимфоманка?")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Хаха!")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="В какой-то момент это было бы очень точное слово, чтобы ассоциироваться со мной!")
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="Так теперь ты просто нимфо?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Очень смешно [k.say_name]!")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Нихрена себе, [n.say_name] обошел всех этим летом!")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Он эффективно использует свое свободное время!")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Вот почему я хотела быть с ним сегодня.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Школа будет сжимать его расписание.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Он уже занимает большую часть своего времени, вращаясь среди всех нас!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Один день со мной, на следующий день это может быть [si.say_name], затем [janet.say_name], а затем...")
    call process_character (k, appearance="outfit bikini pose armcross face shocked blush false", text="Подожди, что?")
    call process_character (k, appearance="outfit bikini pose armcross face shocked blush false", text="Тетя [janet.say_name]?!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face curious blush false mouth red", text="Ты не знала о [janet.say_name]?")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="Да, она также была активна с [n.say_name].")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="Я видела их пару раз, трахающихся на пляже.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Это очень умно, как они прячутся между креслами!")

    if finale_julia_sam:
        call process_character (k, appearance="pose armsup face embarrassed blush false", text="Он практически трахает всю семью!")
        call process_character (k, appearance="pose armsup face embarrassed blush false", text="Я не знаю, как [julia.say_name] еще не узнала об этом.")
        call process_character (edna, appearance="pose handclasp face neutral blush false", text="Мм...{w=1.0}нуу...")
        call process_character (k, appearance="pose armcross face shocked blush false", text="...")
        call process_character (k, appearance="pose armcross face shocked blush false", text="Ты издеваешься надо мной.")
        call process_character (edna, appearance="pose handclasp face neutral blush false", text="Он трахает [julia.say_name] тоже.")
    else:
        call process_character (k, appearance="pose armsup face embarrassed blush false", text="...")
        call process_character (k, appearance="pose armsup face embarrassed blush false", text="Ты издеваешься надо мной.")

    call process_character (k, appearance="outfit bikini pose handhip face embarrassed blush false", text="Как это вообще возможно для [n.say_name]?")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Я не знаю, но [n.say_name] справляется.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Я думаю, что это помогает, что все находятся в непосредственной близости.")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="Он тебе рассказывал о [gloryhole_girl.say_name]?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face curious blush false mouth red", text="[gloryhole_girl.say_name]?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="[gloryhole_girl.say_name]...{w=0.5}[gloryhole_girl.say_name]...")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="Угу.")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Бро устроил с ней большую интрижку в местном парке.")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Я узнала о его связи с ней совершенно случайно.")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="Я не знала об этом.")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="Так что [n.say_name] также имел сексуальные приключения вне семьи.")
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="У [n.say_name] буквально есть девушка на каждый день недели.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="У него нет ни секунды свободного времени!")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Для него это просто постоянный секс.")
    call process_character (k, appearance="outfit bikini pose armcross face happy blush false", text="Бро не просто сексуальный наркоман...он сексуальный маньяк!")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Я не знаю, сколько еще [n.say_name] сможет держать это в тайне.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Я чувствую, что каждая девушка в конечном итоге узнает все, что мы знаем в настоящее время.")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Я думаю ты права, Бабушка.")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Рано или поздно все это вырвется наружу.")
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="Так же, как то, что [n.say_name] сделал ранее сегодня, разрываясь на сиськи!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Хаха!")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="Ладно, я закончил с душем.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="...")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="Над чем вы смеялись?")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="О, мы просто смеялись над этим...")
    call process_character (k, appearance="outfit bikini pose armcross face happy blush false", text="Как я стукнула этого чувака по голове одним из своих ударов!")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face happy blush false mouth red", text="Да!")
    call process_character (n, appearance="outfit underwear pose twohandfist face happy blush false", text="О, да!")
    call process_character (n, appearance="outfit underwear pose twohandfist face happy blush false", text="Это было уморительно!")
    call process_character (n, appearance="outfit underwear pose twohandfist face happy blush false", text="Он развернулся после удара!")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="...")

    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Моя очередь принимать душ.")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="Бабушка, поговорим позже.")
    call process_character (k, appearance="outfit bikini pose armcross face happy blush false", text="Нам нужно многое наверстать...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Не могу дождаться [k.say_name]!")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Итак, [n.say_name]…")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Хочешь помочь мне приготовить еду на кухне?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="У меня есть рецепт сладких и кислых фрикаделек, которые я знаю, тебе понравятся!")
    call process_character (n, appearance="outfit underwear pose twohandfist face happy blush false", text="Звучит безумно хорошо, Бабушка!")
    call process_character (n, appearance="outfit underwear pose twohandfist face happy blush false", text="Да, я хочу помочь сделать их!")

    call fade_to_black (1)


    call process_new_location (bg="bg kira_room_daytime", dream=dream)

    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="...")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="(Вот как далеко ты зашел бро)")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="(Однажды ты втискиваешь свой член между моими ягодицами, желая узнать, каково это...)")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="(И затем, твой член входит в киску каждой девушки, которую ты встречаешь!)")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="(Довольно резкий скачок)")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="...")
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="(Ох, сколько потрахушек у него будет в школе!)")
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="(Это будет как маленькая армия!)")

    "{i}Дзинь!{/i}"

    call process_character (k, appearance="pose armcross face neutral blush false", text="(От кого эта СМСка?)")
    call process_character (k, appearance="pose armcross face neutral blush false", text="...")
    call process_character (k, appearance="pose armcross face neutral blush false", text="(Номер не знаком)")
    call process_character (k, appearance="pose handhip face neutral blush false", text="...")
    call process_character (k, appearance="pose handhip face curious blush false", text="([vicky.say_name]?)")
    call process_character (k, appearance="pose handhip face curious blush false", text="(Понятия не имею, кто это)")
    call process_character (k, appearance="pose armcross face embarrassed blush false", text="(Упс, она прислала мне кучу текста!)")
    call process_character (k, appearance="pose armcross face neutral blush false", text="(Давай посмотрим...)")
    call process_character (k, appearance="pose armcross face neutral blush false", text="\"Привет [k.say_name] [last_name].\"")
    call process_character (k, appearance="pose armcross face neutral blush false", text="Меня зовут [vicky.say_name], и я управляю компанией по производству видео для взрослых, Эмпорниум [vicky.say_name]\"")
    call process_character (k, appearance="pose armcross face happy blush false", text="(Эмпорниум...{w=1.0}умно)")
    call process_character (k, appearance="pose armcross face curious blush false", text="(Но почему со мной связывается такой человек?)")
    call process_character (k, appearance="pose armcross face curious blush false", text="...")
    call process_character (k, appearance="pose handhip face neutral blush false", text="\"О тебе рассказывал твой брат, [n.say_name] [last_name]\"")
    call process_character (k, appearance="pose handhip face shocked blush false", text="(Что?)")
    call process_character (k, appearance="pose handhip face shocked blush false", text="(Владелец порно компании знает [n.say_name]?)")
    call process_character (k, appearance="pose handhip face embarrassed blush false", text="(И он рассказывал обо мне?)")
    call process_character (k, appearance="pose armcross face embarrassed blush false", text="(Это должно быть шутка...)")
    call process_character (k, appearance="pose armcross face neutral blush false", text="...")
    call process_character (k, appearance="pose armcross face neutral blush false", text="\"Я бы очень хотела договориться о встрече с тобой\"")
    call process_character (k, appearance="pose armcross face neutral blush false", text="\"Для тебя есть отличная возможность, которую мы можем обсудить!\"")
    call process_character (k, appearance="pose armcross face neutral blush false", text="\"Если ты заинтересована, пожалуйста, ответь на эту СМС\"")
    call process_character (k, appearance="pose armcross face neutral blush false", text="\"Я с нетерпением жду ответа\"")
    call process_character (k, appearance="pose handhip face neutral blush false", text="...")
    call process_character (k, appearance="pose handhip face neutral blush false", text="(Отличная возможность?)")
    call process_character (k, appearance="pose handhip face embarrassed blush false", text="(В какую сумасшедшую схему попал [n.say_name]?)")
    call process_character (k, appearance="pose handhip face happy blush false", text="(И еще...{w=1.0}мое любопытство зашкаливает!)")
    call process_character (k, appearance="pose handhip face neutral blush false", text="(Я хочу знать, законна ли эта цыпочка или нет...)")
    call process_character (k, appearance="pose handhip face neutral blush false", text="...")
    call process_character (k, appearance="pose armsup face neutral blush false", text="\"Привет, Вики.\"")
    call process_character (k, appearance="pose armsup face neutral blush false", text="\"Где ты находишься и в какое время свободна?\"")

    call fade_to_black (1)

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (k, appearance="blush false", text="Ты [vicky.say_name], я полагаю?")
    call process_character (vicky, appearance="", text="А ты должны быть, [k.say_name]!")
    call process_character (vicky, appearance="", text="Я наконец-то познакомлюсь со старшей сестрой [n.say_name] во плоти!")
    call process_character (k, appearance="blush false", text="Да уж...{w=1.0}как мой младший брат познакомился с тобой?")
    call process_character (k, appearance="blush false", text="Не могу представить, что он случайно столкнулся с владельцем порно компании.")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Ранее я работал партнером в ReflexViz.HD.")
    call process_character (vicky, appearance="", text="Тебе известна эта компания?")
    call process_character (k, appearance="blush false", text="Это ведь сайт с онлайн-трансляциями, верно?")
    call process_character (k, appearance="blush false", text="[n.say_name] и [sa.say_name] не переставали говорить об этом в начале лета.")
    call process_character (k, appearance="blush false", text="Они делали шоу или что-то под названием Твинстикс.")
    call process_character (vicky, appearance="", text="Вот именно.")
    call process_character (vicky, appearance="", text="Я связалась с [n.say_name] после того, как он и его сестра [sa.say_name] начали собирать значительную аудиторию.")
    call process_character (vicky, appearance="", text="Их канал имел большой потенциал, и поэтому я встретилась с [n.say_name], чтобы помочь максимизировать его рост.")
    call process_character (k, appearance="blush false", text="Так что [n.say_name] и [sa.say_name] должно быть круты, чтобы связаться с кем-то вроде тебя.")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Они уже на пути к тому, чтобы стать одним из лучших каналов на ReflexViz.HD!")
    call process_character (k, appearance="blush false", text="Итак, когда же все эти порно штуки вступают в игру?")
    call process_character (vicky, appearance="", text="Я обнаружила, что у [n.say_name] довольно...{w=1.0}особый талант, когда дело доходит до взрослого контента.")
    call process_character (vicky, appearance="", text="Сразу после нашей первой встречи мне стало ясно, что [n.say_name] имел все задатки стать великой порнозвездой.")
    call process_character (k, appearance="blush false", text="Порнозвездой?!")
    call process_character (k, appearance="blush false", text="Мой маленький бро, [n.say_name], порнозвезда?")
    call process_character (k, appearance="blush false", text="Хахаха!")
    call process_character (vicky, appearance="", text="Я могу засвидетельствовать впечатляющие возможности [n.say_name].")
    call process_character (vicky, appearance="", text="Он никогда не подводит!")
    call process_character (k, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="Ты пытаешься мне сказать...{w=1.0} что ты и [n.say_name]...")
    call process_character (vicky, appearance="", text="Именно этот офис был местом нескольких наших...{w=1.0}сеансов.")
    call process_character (k, appearance="blush false", text="(Мне показалось, что я почувствовала слабый запах спермы здесь...)")
    call process_character (vicky, appearance="", text="Вскоре после этого я основала  Эмпорниум [vicky.say_name], [n.say_name] играет ключевую роль в производстве.")
    call process_character (k, appearance="blush false", text="Ключевая роль, да?")
    call process_character (vicky, appearance="", text="Ты уже видела наши видео?")
    call process_character (k, appearance="blush false", text="Ты и [n.say_name] записали все на видео?!")
    call process_character (vicky, appearance="", text="На данный момент их несколько.")
    call process_character (vicky, appearance="", text="Это эксклюзивный контент для сайта Эмпорниум [vicky.say_name].")

    show bg vicky_sit_turn
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Вот, позволь мне показать одно из наших недавних.")
    call process_character (k, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="Святое дерьмо, это [n.say_name]!")
    call process_character (k, appearance="blush false", text="А вот и ты!")
    call process_character (vicky, appearance="", text="Так и есть.")
    call process_character (k, appearance="blush false", text="Хорошая работа с камерой.")
    call process_character (k, appearance="blush false", text="Я вижу, ты позволила ему подняться к своему заднему проходу, хе-хе.")
    call process_character (k, appearance="blush false", text="Я одобряю.")
    call process_character (vicky, appearance="", text="Мы стараемся делать все возможное.")
    call process_character (k, appearance="blush false", text="([n.say_name] превратил потрахушки в профессию!)")
    call process_character (k, appearance="blush false", text="(Он буквально делает бабки, заставляя свой член делать работу!)")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Итак, что ты думаешь?")
    call process_character (k, appearance="blush false", text="Я думаю...{w=1.0}[n.say_name] - счастливый ублюдок.")
    call process_character (k, appearance="blush false", text="Хотела бы и я делать то же самое.")
    call process_character (vicky, appearance="", text="Тогда ты захочешь услышать мое предложение, [k.say_name].")
    call process_character (k, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="Продолжай.")
    call process_character (vicky, appearance="", text="Я бы хотела, чтобы ты была главной актрисой, которая работает с [n.say_name].")
    call process_character (vicky, appearance="", text="У вас была бы своя собственная серия!")
    call process_character (vicky, appearance="", text="И ты получишь семьдесят процентов от продаж и подписок.")
    call process_character (k, appearance="blush false", text="Хммм!")
    call process_character (k, appearance="blush false", text="Мне нравится, как это звучит!")
    call process_character (k, appearance="blush false", text="Если это станет успешным, мне больше не придется работать в фитнес-центре!")
    call process_character (vicky, appearance="", text="Я уверена, что это будет успешным.")
    call process_character (vicky, appearance="", text="Рынок созрел для такого рода контента.")

    show bg vicky_sit_neutral
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Но тебе не нужно торопиться с решением.")
    call process_character (vicky, appearance="", text="Я хочу убедиться, что ты уверена в этом.")
    call process_character (vicky, appearance="", text="Прежде чем ты уйдешь сегодня, я дам тебе некоторые документы и наброски того, что от тебя требуется.")
    call process_character (vicky, appearance="", text="Прочти внимательно и дай мне знать, что ты думаешь.")

    show bg vicky_sit_smile
    with Dissolve(0.5)

    call process_character (vicky, appearance="", text="Я открыта для изменений и переговоров, поэтому все, что ты читаешь, может измениться.")
    call process_character (k, appearance="blush false", text="Я не думаю, что это займет много времени, чтобы принять решение!")
    call process_character (vicky, appearance="", text="Это здорово слышать, что у тебя есть энтузиазм по поводу предложения!")
    call process_character (vicky, appearance="", text="Я рада, что ты смогла зайти и поговорить со мной сегодня!")
    call process_character (k, appearance="blush false", text="Спасибо, что хоть раз в жизни мне подарили такую возможность!")
    call process_character (vicky, appearance="", text="Не нужно меня благодарить.")
    call process_character (vicky, appearance="", text="Это был твой брат [n.say_name], он рассказал мне о тебе, в конце концов.")
    call process_character (vicky, appearance="", text="Это его ты должна благодарить.")
    call process_character (k, appearance="blush false", text="Поверь мне, я это сделаю...")
    call process_character (vicky, appearance="", text="У тебя есть моя контактная информация и визитка, так что звони, когда захочешь поговорить.")
    call process_character (k, appearance="blush false", text="Звучит отлично [vicky.say_name]!")

    call fade_to_black (1)


    call process_new_location (bg="bg backyard_daytime", dream=dream)

    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="...")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="(Представить не могу...{w=0.5}я стану порнозвездой с [n.say_name])")
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="(Мое любимое занятие трахаться теперь может быть карьерой!)")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="...")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="(Мне придется придумать хорошее имя для порнозвезды)")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="(Интересно, есть ли оно у [n.say_name]...)")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="...")
    call process_character (k, appearance="outfit bikini pose armcross face happy blush false", text="(Бро - единственный человек, кто думает своим членом и от этого получает выгоду!)")
    call process_character (k, appearance="outfit bikini pose armcross face happy blush false", text="(Теперь у него есть целый состав девушек, готовых на все ради него)")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="...")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="(Если бы все девушки [n.say_name] собрались бы в одном месте?)")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="(Это был бы хаос...{w=1.0}для [n.say_name]!)")
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="(Говоря о слишком хорошей вещи!)")
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="(Переживет ли его член и яйца такое испытание?)")
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="...")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="Хмм...")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="...")
    call process_character (k, appearance="outfit bikini pose armcross face happy blush false", text="Хехе...")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="(Учитывая, какое это лето было для [n.say_name], было бы уместно, если бы он ушел с огромным взрывом)")
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="(Спермы на всех нас...)")

    call fade_to_black (1)

    "{i}Несколько дней спустя...{/i}"

    call process_new_location (bg="bg nate_room_daytime", dream=dream)

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="(Скоро уже начнется учеба...)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="(Жаль, что я не могу путешествовать во времени и снова попасть в лето)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="{i}Эхх.{/i}..")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="(Ну, как сказала [k.say_name], мне нужно максимально использовать оставшиеся летние каникулы)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Хм?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="(Я слышу много людей снаружи у бассейна)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="(Мама пригласила компанию?)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="(Сегодня довольно тепло)")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="(Я думаю, что плавание в бассейне будет отличной идеей!)")


    call character_leave_dissolve (n)

    call process_character (n, appearance="outfit swimsuit pose twohandfist face happy blush false", text="(Я готов к пушечному ядру!)")

    call fade_to_black (1)


    call process_new_location (bg="bg backyard_daytime", dream=dream)

    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false", text="...")
    call process_character (si, appearance="outfit swimsuit pose armunder face happy blush false", text="Вот он где!")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Время пришло, бро!")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Все тебя так ждали.")
    call process_character (n, appearance="outfit swimsuit pose behindhead face neutral blush false", text="Что ты имеешь в виду?")

    if finale_julia_sam:
        call process_character (sa, appearance="outfit swimsuit pose leaning face neutral blush false", text="Просто посмотри, кто здесь [n.say_name]!")

    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Я люблю этот бассейн, [n.say_name]!")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Он идеально подходит для проведения такой вечеринки!")
    call process_character (n, appearance="outfit swimsuit pose handsdown face happy blush false", text="Тетя [janet.say_name]!")

    if finale_julia_sam:
        call process_character (julia, appearance="outfit clothes pose armcross face neutral blush false", text="У меня нет купальника, чтобы надеть его для плавания; не то, чтобы я бы хотела его надевать.")
        call process_character (julia, appearance="outfit clothes pose armcross face happy blush false", text="Но мне нравится погружать ноги в горячую ванну.")
        call process_character (n, appearance="pose handfist face neutral blush false", text="Привет [julia.say_name]!")
        call process_character (julia, appearance="outfit clothes pose handup face happy blush false", text="Привет.")

    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Угощайся закусками [n.say_name]!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Попробуй чипсы и соус!")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face happy blush false", text="Ты тоже здесь, Бабушка?!")
    call process_character (si, appearance="outfit swimsuit pose handsup face neutral blush false", text="Это все [k.say_name] спланировала!")
    call process_character (si, appearance="outfit swimsuit pose handsup face happy blush false", text="Она сказала, что мы должны собраться в конце лета, и я согласилась с этой идеей!")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Было нелегко работать по расписанию.")
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="Но я не собиралась сдаваться!")
    call process_character (n, appearance="outfit swimsuit pose handsdown face happy blush false", text="Я рад, что ты этого не сделала [k.say_name]!")
    call process_character (n, appearance="outfit swimsuit pose handsdown face happy blush false", text="Так здорово, что все здесь собрались!")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Ну, это еще не совсем все.")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Еще двое гостей не прибыли.")
    call process_character (n, appearance="outfit swimsuit pose behindhead face neutral blush false", text="Серьезно?")
    call process_character (n, appearance="outfit swimsuit pose behindhead face neutral blush false", text="Еще?")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Да...")
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="Твоя подружка по парку, [gloryhole_girl.say_name], и бизнес-партнер [vicky.say_name].")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face embarrassed blush false", text="[gloryhole_girl.say_name[0]]-[gloryhole_girl.say_name] и [vicky.say_name] придут?!")
    call process_character (si, appearance="outfit swimsuit pose handsfront face neutral blush false", text="Ты должен был рассказать нам о них раньше, милый!")
    call process_character (si, appearance="outfit swimsuit pose handsfront face neutral blush false", text="Они вроде обе милые девушки, основываясь на том, что [k.say_name] сказала мне.")
    call process_character (si, appearance="outfit swimsuit pose armunder face happy blush false", text="Я бы пригласила их на ужин!")
    call process_character (n, appearance="outfit swimsuit pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit swimsuit pose behindhead face curious blush false", text="К-как ты об этом узнала?..")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Внимание всем!")
    call process_character (k, appearance="outfit bikini pose handhip face neutral blush false", text="Внимание!")
    call process_character (n, appearance="outfit swimsuit pose handsdown face concerned blush false", text="...")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="Теперь, когда [n.say_name] наконец-то здесь...самое время рассказать ему, что это за вечеринка на самом деле.")
    call process_character (k, appearance="outfit bikini pose armcross face happy blush false", text="Каждый из вас должен точно знать, что я имею в виду, исходя из того, что обсуждалось ранее.")
    call process_character (n, appearance="outfit swimsuit pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit swimsuit pose behindhead face curious blush false", text="Что обсуждалось?")
    call process_character (n, appearance="outfit swimsuit pose behindhead face curious blush false", text="Не думаю, что ты говорила со мной об этом...")

    call character_leave_dissolve (k)
    pause 0.5

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Resort Loop2.ogg", fadeout=1.0, fadein = 1.0)

    call process_character (k, appearance="outfit nude pose armsup face happy blush false")
    pause 0.5

    call process_character (k, appearance="outfit nude pose armsup face happy blush false", text="...")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face embarrassed blush false", text="!!")

    call process_character (si, appearance="outfit swimsuit pose armunder face flirt blush false")
    pause 0.5
    call character_leave_dissolve (si)
    pause 0.5
    call process_character (si, appearance="outfit nude pose armunder face flirt blush false")
    pause 0.5

    call process_character (si, appearance="outfit nude pose armunder face flirt blush false", text="...")
    call process_character (n, appearance="outfit swimsuit pose handsdown face embarrassed blush true", text="(Х-Ха?!)")

    if finale_julia_sam:
        call process_character (sa, appearance="outfit swimsuit pose handface face happy blush false")
        pause 0.5
        call character_leave_dissolve (sa)
        pause 0.5
        call process_character (sa, appearance="outfit nude pose handface face happy blush false")
        pause 0.5

        call process_character (sa, appearance="outfit nude pose handface face happy blush false", text="О да, это начинается!")

        call process_character (julia, appearance="outfit clothes pose handup face aroused blush false")
        pause 0.5
        call character_leave_dissolve (julia)
        pause 0.5
        call process_character (julia, appearance="outfit nude pose handup face aroused blush false")
        pause 0.5
        call process_character (julia, appearance="outfit nude pose handup face aroused blush false", text="...")

    call process_character (janet, appearance="outfit swimsuit pose handface face neutral blush false")
    pause 0.5
    call character_leave_dissolve (janet)
    pause 0.5
    call process_character (janet, appearance="outfit nude pose handface face neutral blush false")
    pause 0.5

    call process_character (janet, appearance="outfit nude pose handface face neutral blush false", text="Твое лицо ярко-красное [n.say_name]!")
    call process_character (janet, appearance="outfit nude pose handface face happy blush false", text="Вокруг тебя слишком много милых девушек?")

    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red")
    pause 0.5
    call character_leave_dissolve (edna)
    pause 0.5
    call process_character (edna, appearance="outfit nude pose handhip face happy blush false mouth red")
    pause 0.5

    call process_character (edna, appearance="outfit nude pose handhip face happy blush false mouth red", text="Есть на что посмотреть, не правда ли [n.say_name]?")
    call process_character (n, appearance="outfit swimsuit pose behindhead face embarrassed blush true", text="(О-они все голые...)")
    call process_character (n, appearance="outfit swimsuit_hard pose behindhead face aroused blush true", text="...")
    call process_character (n, appearance="outfit swimsuit_hard pose twohandfist face aroused blush true", text="(Вся моя семья голая передо мной!)")
    call process_character (k, appearance="outfit nude pose handhip face flirt blush false", text="Ты еще не соединил все точки в своей голове?")
    call process_character (k, appearance="outfit nude pose handhip face flirt blush false", text="Твоя вторая голова уже все поняла!")
    call process_character (n, appearance="outfit swimsuit_hard pose handsdown face aroused blush true", text="...")
    call process_character (n, appearance="outfit swimsuit_hard pose handsdown face aroused blush true", text="(Что здесь происходит?)")
    call process_character (k, appearance="outfit nude pose armsup face happy blush false", text="Хватит пялиться на сиськи и задницы [n.say_name], и снимай одежду!")

    call process_character (n, appearance="outfit nudehard pose twohandfist face aroused blush true", show_bust=False)
    $ refresh_character(n, force_transition = Dissolve(1.0))
    call process_character (n, appearance="outfit nudehard pose twohandfist face aroused blush true", text="Ах!")

    call process_character (k, appearance="pose armcross face flirt blush false", text="Ну, кто хочет первой?")

    if finale_julia_sam:
        call process_character (sa, appearance="pose leaning face neutral blush false", text="Я, я, я!")
        call process_character (sa, appearance="pose leaning face neutral blush false", text="Я хочу быть первой!")

    call process_character (edna, appearance="pose handclasp face happy blush false", text="Учитывается ли старшинство в том, кто будет первой?")
    call process_character (si, appearance="pose handsup face happy blush false", text="А что если ты глава семьи?")
    call process_character (si, appearance="pose handsup face happy blush false", text="Хаха!")
    call process_character (janet, appearance="pose handface face happy blush false", text="Будем тянуть соломинки?")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="П-Подождите!")
    call process_character (n, appearance="pose behindhead face embarrassed blush true", text="У меня есть право голоса в этом?")
    call process_character (k, appearance="pose handhip face happy blush false", text="Хочешь выбрать сам, бро?")
    call process_character (k, appearance="pose handhip face flirt blush false", text="Я должна была догадаться, раз тебе так нравится.")

    call process_character (n, appearance="pose behindhead face curious blush true")

    call process_character (edna, appearance="pose handhip face neutral blush false", text="Меня это вполне устраивает.")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Пока я провожу время со своим внуком!")

    if finale_julia_sam:
        call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Так же!")


    call process_character (janet, appearance="pose handchest face neutral blush false", text="Кто бы это ни был!")

    if finale_julia_sam:
        call process_character (julia, appearance="pose handface face neutral blush false", text="Мне все равно, в любом случае.")

    call process_character (si, appearance="pose armunder face flirt blush false", text="Похоже, есть общее согласие, что ты сделаешь выбор, милый!")
    call process_character (k, appearance="pose armsup face flirt blush false", text="Ладно, бро, у тебя много вариантов.")
    call process_character (k, appearance="pose armsup face flirt blush false", text="Надеюсь, ты сможешь выбрать сам!")
    call process_character (n, appearance="pose handsdown face curious blush true", text="...")

    call finale_scene_choices (dream=dream)

    return

label finale_scene_choices(dream=False):

    if finale_fucked_amount >= finale_fucked_amount_goal:
        call finale_scene_end (dream=dream)
    elif finale_fucked_amount >= 1 and not finale_kacey_arrived:
        $ finale_kacey_arrived = True
        call process_character (k, appearance="blush false", text="...")
        call process_character (k, appearance="blush false", text="Ой, кто тут?")
        call process_character (gloryhole_girl, appearance="", text="Я сделала это!")
        call process_character (k, appearance="blush false", text="Привет, это [gloryhole_girl.say_name]!")
        call process_character (n, appearance="blush false", text="П-привет [gloryhole_girl.say_name]...")
        call process_character (gloryhole_girl, appearance="", text="Я немного заблудилась по дороге сюда, но, к счастью, я поняла это.")
        call process_character (gloryhole_girl, appearance="", text="Я много пропустила?")
        call process_character (k, appearance="blush false", text="Мы только начали!")
        call process_character (k, appearance="blush false", text="Снимай одежду и устраивайся поудобнее!")
        call process_character (si, appearance="blush false", text="Привет [gloryhole_girl.say_name], меня зовут [si.say_name].")
        call process_character (si, appearance="blush false", text="Я Мама [n.say_name]!")
        call process_character (gloryhole_girl, appearance="", text="Рада познакомиться Мама [n.say_name]!")
        call process_character (gloryhole_girl, appearance="", text="Ты очень красивая!")
        call process_character (si, appearance="blush false", text="Спасибо!")
        call process_character (si, appearance="blush false", text="Угощайся едой.")
        call process_character (gloryhole_girl, appearance="", text="Очень признательна!")
        call process_character (gloryhole_girl, appearance="", text="Есть порядок, кто будет следующей у [n.say_name]?")
        call process_character (janet, appearance="blush false", text="[n.say_name] сам выбирает.")
        call process_character (janet, appearance="blush false", text="Так что любая из нас может быть следующей!")
        call process_character (gloryhole_girl, appearance="", text="Ох, мне это нравится!")
        call process_character (gloryhole_girl, appearance="", text="Это делает вещи захватывающими!")
    elif finale_fucked_amount >= 2 and not finale_vicky_arrived:
        $ finale_vicky_arrived = True
        call process_character (k, appearance="blush false", text="...")
        call process_character (k, appearance="blush false", text="Приивет, это [vicky.say_name]!")
        call process_character (n, appearance="blush false", text="О-она здесь?")
        call process_character (vicky, appearance="", text="Всем привет.")
        call process_character (vicky, appearance="", text="Простите, что опоздала.")
        call process_character (vicky, appearance="", text="Пришлось позаботиться о технической проблеме на моем сайте.")
        call process_character (k, appearance="blush false", text="Рада, что ты смогла прийти [vicky.say_name].")
        call process_character (k, appearance="blush false", text="Итак, теперь мы все собрались!")
        call process_character (vicky, appearance="", text="Мне нужно познакомиться!")
        call process_character (vicky, appearance="", text="[n.say_name] рассказал мне так много о всех вас!")
        call process_character (si, appearance="blush false", text="Надеюсь, только хорошие вещи!")
        call process_character (vicky, appearance="", text="Вы, Мама [n.say_name]?")
        call process_character (si, appearance="blush false", text="Да, это так!")
        call process_character (si, appearance="blush false", text="[si.say_name]!")
        call process_character (vicky, appearance="", text="[vicky.say_name].")
        call process_character (vicky, appearance="", text="[n.say_name] очень похож на вас, вот что дало мне догадку!")
        call process_character (vicky, appearance="", text="Вы вырастили очень респектабельного молодого человека, [si.say_name].")
        call process_character (si, appearance="blush false", text="Это замечательно слышать от профессиональной бизнесвумен!")
        call process_character (vicky, appearance="", text="А кто остальные члены семьи здесь?")
        call process_character (janet, appearance="blush false", text="Я [janet.say_name], Тетя [n.say_name] и сестра [si.say_name].")
        call process_character (edna, appearance="blush false", text="Я его бабушка, [edna.say_name].")

        if finale_julia_sam:
            call process_character (julia, appearance="blush false", text="Кузина, [julia.say_name].")

        call process_character (vicky, appearance="", text="Поняла.")
        call process_character (vicky, appearance="", text="[k.say_name] я уже знаю...")

        if finale_julia_sam:
            call process_character (vicky, appearance="", text="И [sa.say_name]!")
            call process_character (sa, appearance="blush false", text="Да!")
            call process_character (sa, appearance="blush false", text="Вы знаете обо мне?")
            call process_character (vicky, appearance="", text="Конечно!")
            call process_character (vicky, appearance="", text="Ты другая половинка канала Твинстикс!")
            call process_character (vicky, appearance="", text="Я подписана на ваш канал.")
            call process_character (vicky, appearance="", text="Я смотрела много твоих прямых трансляций с [n.say_name].")
            call process_character (sa, appearance="blush false", text="{i}Ах!{/i}")
            call process_character (sa, appearance="blush false", text="Я встречаю лично моего первого подписчика!")

        call process_character (k, appearance="blush false", text="Уверена, тебе будет о чем поговорить со всеми, Вики.")
        call process_character (k, appearance="blush false", text="Но это может произойти позже.")
        call process_character (vicky, appearance="", text="Действительно.")
        call process_character (vicky, appearance="", text="[n.say_name] требует нашего пристального внимания прямо сейчас.")

    menu:
        "Бабушка" if not finale_chose_edna:
            if not finale_chose_edna:
                $ finale_fucked_amount += 1

            if edna_fucked_vaginally() in scenes_completed or finale_chose_edna:
                $ no_bust_art = False
                show bg backyard_daytime
                with Dissolve(0.5)
                call process_character (edna, appearance="pose handclasp face flirt blush false", text="Давай устроим шоу, [n.say_name]!")

                call static_still_ctc ("bg party_edna")

                call process_character (edna, appearance="blush false", text="Ооох...")
                call process_character (n, appearance="blush false", text="Так тепло.")
                call process_character (n, appearance="blush false", text="Можно я возьмусь за твои сиськи, Бабушка.")
                call process_character (edna, appearance="blush false", text="Сожми их, как тебе нравится [n.say_name], да!")
                call process_character (k, appearance="blush false", text="Знаете, что в этом действительно круто...")
                call process_character (k, appearance="blush false", text="[n.say_name] буквально трахнул три поколения нашей семьи!")
                call process_character (k, appearance="blush false", text="Это так сногсшибательно, когда думаешь об этом.")
                call process_character (n, appearance="blush false", text="Ммм, Мм!")
                call process_character (janet, appearance="blush false", text="[n.say_name] использовал другой подход к изучению нашего генеалогического древа")
                call process_character (k, appearance="blush false", text="Ха!")
                call process_character (k, appearance="blush false", text="Думаете, если [n.say_name] был бы путешественником во времени, он бы трахнул наших дальних родственников тоже?")
                call process_character (si, appearance="blush false", text="Хаха!")

                if finale_julia_sam:
                    call process_character (julia, appearance="blush false", text="Я бы не отпустила его в прошлом.")

                call process_character (edna, appearance="blush false", text="Я полагаю, это означает, что [n.say_name] может трахнуть меня в моей квартире, даже когда кто-либо из вас навещает меня!")
                call process_character (si, appearance="blush false", text="Ты можешь делать все, что захочешь, Мама!")
                call process_character (edna, appearance="blush false", text="Это здорово слышать, [si.say_name]!")
                call process_character (edna, appearance="blush false", text="Твой сын очень возбуждается у меня дома.")
                call process_character (edna, appearance="blush false", text="Он хватал меня за сиськи и за задницу весь день!")
                call process_character (si, appearance="blush false", text="В этом нет ничего удивительного.")
                call process_character (si, appearance="blush false", text="Он делает то же самое здесь, со мной!")


                if finale_julia_sam:
                    call process_character (sa, appearance="blush false", text="Если я приду к тебе, Бабушка, можем ли мы с [n.say_name] трахаться на кухне, пока делаем печенье?!")
                    call process_character (edna, appearance="blush false", text="Только если мы будем меняться!")
                    call process_character (sa, appearance="blush false", text="Нет проблем, Бабушка!")
                    call process_character (edna, appearance="blush false", text="Мы должны быть осторожны, когда [n.say_name] приходит, если тесто рядом!")

                call process_character (n, appearance="blush false", text="Аах, да, Бабушка...")
                call process_character (k, appearance="blush false", text="[n.say_name] конечно любит сиськи, не так ли?")
                call process_character (janet, appearance="blush false", text="Он мальчишка, ха-ха!")
                call process_character (janet, appearance="blush false", text="В нем заложена любовь к сиськам!")
                call process_character (edna, appearance="blush false", text="Мы все любим его член, хотя, так что это идет в обе стороны!")
            else:
                $ no_bust_art = False
                show bg backyard_daytime
                with Dissolve(0.5)
                call process_character (edna, appearance="pose handclasp face flirt blush false", text="Это будет особенный момент для [n.say_name] и меня.")
                call process_character (edna, appearance="pose handclasp face flirt blush false", text="У нас еще не было возможности...{w=0.5}пройти весь путь вместе.")
                call process_character (k, appearance="pose handhip face neutral blush false", text="Ты имеешь в виду, что это будет первый раз, когда хер [n.say_name] войдет в твою киску, Бабушка?")
                call process_character (k, appearance="pose handhip face happy blush false", text="И мы все станем свидетелями этого?!")
                call process_character (k, appearance="pose handhip face happy blush false", text="Я думаю, [n.say_name] сегодня не единственный, кому сегодня везет!")
                call process_character (k, appearance="pose handhip face happy blush false", text="Я собираюсь насладиться этим зрелищем!")
                call process_character (janet, appearance="pose handchest face neutral blush false", text="Тебе понравится, как [n.say_name] трахается, Мам.")
                call process_character (janet, appearance="pose handchest face flirt blush false", text="То, что [n.say_name] делает с этим хером, является чем-то особенным!")
                call process_character (n, appearance="pose handsdown face aroused blush true", text="...")
                call process_character (edna, appearance="pose handhip face flirt blush false", text="У нас нетерпеливая аудитория, [n.say_name].")
                call process_character (edna, appearance="pose handhip face flirt blush false", text="Давай начнем шоу для них!")

                call static_still_ctc ("bg party_edna")

                call process_character (edna, appearance="blush false", text="Ооох...")
                call process_character (edna, appearance="blush false", text="{i}Ах!{/i}")
                call process_character (edna, appearance="blush false", text="Это так круто!")
                call process_character (k, appearance="blush false", text="Хорошо, [n.say_name], скажи нам.")
                call process_character (k, appearance="blush false", text="Какова бабушкина киска сейчас на твоем члене?")
                call process_character (n, appearance="blush false", text="О-она мягкая и горячая!")
                call process_character (n, appearance="blush false", text="Хааа!")
                call process_character (n, appearance="blush false", text="И становится все теплее!")
                call process_character (k, appearance="blush false", text="Да, хватай бабушкины сиськи, [n.say_name].")
                call process_character (k, appearance="blush false", text="Держи их крепко!")
                call process_character (edna, appearance="blush false", text="Сожми их, делай, что тебе нравится [n.say_name], да!")
                call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
                call process_character (k, appearance="blush false", text="...")
                call process_character (k, appearance="blush false", text="Знаете, что в этом действительно круто...")
                call process_character (k, appearance="blush false", text="[n.say_name] буквально трахнул три поколения нашей семьи!")
                call process_character (k, appearance="blush false", text="Это так сногсшибательно, когда думаешь об этом.")
                call process_character (n, appearance="blush false", text="Ммм, Мм!")
                call process_character (janet, appearance="blush false", text="[n.say_name] использовал другой подход к изучению нашего генеалогического древа")
                call process_character (k, appearance="blush false", text="Ха!")
                call process_character (k, appearance="blush false", text="Думаете, если [n.say_name] был бы путешественником во времени, он бы трахнул наших дальних родственников тоже?")
                call process_character (si, appearance="blush false", text="Хаха!")

                if finale_julia_sam:
                    call process_character (julia, appearance="blush false", text="Я бы не отпустила его в прошлом.")

                call process_character (edna, appearance="blush false", text="Я полагаю, это означает, что [n.say_name] может трахнуть меня в моей квартире, даже когда кто-либо из вас навещает меня!")
                call process_character (si, appearance="blush false", text="Ты можешь делать все, что захочешь, Мама!")
                call process_character (edna, appearance="blush false", text="Это здорово слышать, [si.say_name]!")
                call process_character (edna, appearance="blush false", text="Твой сын очень возбуждается у меня дома.")
                call process_character (edna, appearance="blush false", text="Он хватал меня за сиськи и за задницу весь день!")
                call process_character (si, appearance="blush false", text="В этом нет ничего удивительного.")
                call process_character (si, appearance="blush false", text="Он делает то же самое здесь, со мной!")

                if finale_julia_sam:
                    call process_character (sa, appearance="blush false", text="Если я приду к тебе, Бабушка, можем ли мы с [n.say_name] трахаться на кухне, пока делаем печенье?!")
                    call process_character (edna, appearance="blush false", text="Только если мы будем меняться!")
                    call process_character (sa, appearance="blush false", text="Нет проблем, Бабушка!")
                    call process_character (edna, appearance="blush false", text="Мы должны быть осторожны, когда [n.say_name] приходит, если тесто рядом!")

                call process_character (n, appearance="blush false", text="Аах, да, Бабушка...")
                call process_character (k, appearance="blush false", text="[n.say_name] конечно любит сиськи, не так ли?")
                call process_character (janet, appearance="blush false", text="Он мальчишка, ха-ха!")
                call process_character (janet, appearance="blush false", text="В нем заложена любовь к сиськам!")
                call process_character (edna, appearance="blush false", text="Мы все любим его член, хотя, так что это идет в обе стороны!")

            $ finale_chose_edna = True
        "Тетя [janet.say_name]" if not finale_chose_janet:
            if not finale_chose_janet:
                $ finale_fucked_amount += 1

            $ finale_chose_janet = True

            $ no_bust_art = False
            show bg backyard_daytime
            with Dissolve(0.5)
            call process_character (janet, appearance="pose handchest face flirt blush false", text="Я уже бегу!")

            call static_still_ctc ("bg party_janet")

            call process_character (janet, appearance="blush false", text="Ммм, да...")
            call process_character (janet, appearance="blush false", text="Тебе нравится, когда я сверху?")
            call process_character (n, appearance="blush false", text="Аах, ах...")
            call process_character (n, appearance="blush false", text="Да, Тетя [janet.say_name].")
            call process_character (k, appearance="blush false", text="Это правда, что вы трахаетесь на пляже?")
            call process_character (janet, appearance="blush false", text="Да!")
            call process_character (janet, appearance="blush false", text="Это очень весело трахаться, когда ты так открыта!")
            call process_character (si, appearance="blush false", text="Пожалуйста, будь осторожна!")
            call process_character (si, appearance="blush false", text="Если тебя когда-нибудь поймают...")
            call process_character (janet, appearance="blush false", text="Мы будем в порядке, сестренка!")
            call process_character (janet, appearance="blush false", text="Мимо нас прошло много людей, и никто никогда не замечал.")
            call process_character (edna, appearance="blush false", text="За исключением того момента, когда я заметила тебя!")
            call process_character (janet, appearance="blush false", text="Это не считается, Мама!")
            call process_character (janet, appearance="blush false", text="[n.say_name] рассказал тебе, как и где мы трахаемся, так что у тебя была вся информация!")
            call process_character (edna, appearance="blush false", text="Это правда, ха-ха!")

            if finale_julia_sam:
                call process_character (julia, appearance="blush false", text="Я действительно думала, что [k.say_name] шутила, когда она сказала мне, что ты трахаешься с [n.say_name], Мам.")
                call process_character (julia, appearance="blush false", text="Теперь я знаю, что член [n.say_name] был в твоей киске.")
                call process_character (k, appearance="blush false", text="И в заднице, и во рту тоже.")
                call process_character (janet, appearance="blush false", text="Я слышала, у тебя был первый анальный опыт с [n.say_name], [julia.say_name]!")
                call process_character (janet, appearance="blush false", text="Если верить [n.say_name], ты стонала на весь дом!")
                call process_character (julia, appearance="blush false", text="Не разглашай таких подробностей, [n.say_name]!")
                call process_character (si, appearance="blush false", text="Ха-ха, все в порядке, [julia.say_name]!")
                call process_character (k, appearance="blush false", text="Да!")
                call process_character (k, appearance="blush false", text="Нет ничего плохого в том, чтобы быть фанатом траха в задницу!")
                call process_character (julia, appearance="blush false", text="...")

            call process_character (janet, appearance="blush false", text="[n.say_name] и я много медитируем голыми до и после того, как мы трахаемся!")
            call process_character (janet, appearance="blush false", text="Я думаю, все мы должны сделать это после того, как закончим!")
            call process_character (edna, appearance="blush false", text="Звучит весело!")
            call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
            call process_character (janet, appearance="blush false", text="Мы тоже часто ходим голые по дому!")
            call process_character (k, appearance="blush false", text="А вы, да?")
            call process_character (k, appearance="blush false", text="Тогда я должна как-нибудь приехать!")
            call process_character (k, appearance="blush false", text="Хотела бы я жить без одежды!")
            call process_character (janet, appearance="blush false", text="Это следующая лучшая вещь, когда ты у меня дома!")
        "[julia.say_name]" if finale_julia_sam and not finale_chose_julia:
            if not finale_chose_julia:
                $ finale_fucked_amount += 1

            $ finale_chose_julia = True

            $ no_bust_art = False
            show bg backyard_daytime
            with Dissolve(0.5)
            call process_character (julia, appearance="outfit nude pose armcross face aroused blush false", text="Я готова.")

            call static_still_ctc ("bg party_julia")

            call process_character (n, appearance="blush false", text="Ах, ах!")
            call process_character (n, appearance="blush false", text="Подпрыгивай вверх и вниз, вот так [julia.say_name]!")
            call process_character (julia, appearance="blush false", text="Так что я была права с самого начала [n.say_name]...{w=1.0}ты извращенец.")
            call process_character (julia, appearance="blush false", text="Я просто не понимала, насколько большой!")
            call process_character (k, appearance="blush false", text="Я поощряю извращения!")
            call process_character (k, appearance="blush false", text="Когда я поймала [n.say_name], глядящего на мою задницу, делая приседания, я дала ему именно то, что он хотел...")
            call process_character (k, appearance="blush false", text="Я буквально вошла в его комнату, стянула шорты и заставила его смотреть на мою задницу!")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (julia, appearance="blush false", text="Круто.")
            call process_character (julia, appearance="blush false", text="Так ты тоже извращенка, [k.say_name].")
            call process_character (edna, appearance="blush false", text="Все мы извращенцы в этой семье, [julia.say_name].")
            call process_character (edna, appearance="blush false", text="И это касается и тебя тоже!")
            call process_character (janet, appearance="blush false", text="Каждый раз, когда ты берешь в рот сперму и проглатываешь ее за один раз, ты попадаешь в категорию извращенцев, ха-ха!")
            call process_character (n, appearance="blush false", text="[julia.say_name] очень любит глотать мою сперму.")
            call process_character (n, appearance="blush false", text="Она открывает рот очень широко, когда я собираюсь стрелять своей спермой в ее рот.")
            call process_character (julia, appearance="blush false", text="...")
            call process_character (sa, appearance="blush false", text="Я могу подтвердить, что это совершенно верно!")
            call process_character (sa, appearance="blush false", text="[julia.say_name] готова выпить сперму с пола!")
            call process_character (si, appearance="blush false", text="Эякуляции [n.say_name] совсем не мизерные!")
            call process_character (si, appearance="blush false", text="Он выстреливает так много за один раз, что покрывает мои сиськи толстым слоем спермы!")
            call process_character (edna, appearance="blush false", text="Я чуть не подавилась его спермой после того, как он брызнул мне в рот.")
            call process_character (k, appearance="blush false", text="[julia.say_name]...{w=1.0}ты должна быть настоящим мусорным баком, чтобы проглотить всю сперму [n.say_name]!")
            call process_character (julia, appearance="blush false", text="Ладно, я поняла.")
            call process_character (julia, appearance="blush false", text="Я никогда не говорила, что я не извращенка.")
            call process_character (n, appearance="blush false", text="Ммм!")
            call process_character (n, appearance="blush false", text="Иду до самого конца, [julia.say_name]!")
            call process_character (n, appearance="blush false", text="Аах да!")
        "[k.say_name]" if not finale_chose_kira:
            if not finale_chose_kira:
                $ finale_fucked_amount += 1

            $ finale_chose_kira = True

            $ no_bust_art = False
            show bg backyard_daytime
            with Dissolve(0.5)
            call process_character (k, appearance="pose armsup face flirt blush false", text="Давай, бро!")

            call static_still_ctc ("bg party_kira")

            call process_character (k, appearance="blush false", text="Держись крепче!")
            call process_character (k, appearance="blush false", text="Не зря это называется кувалдой!")
            call process_character (n, appearance="blush false", text="Ха-ах!")
            call process_character (edna, appearance="blush false", text="Как называется эта поза?")
            call process_character (janet, appearance="blush false", text="Я думаю, что она сказала кувалда.")
            call process_character (edna, appearance="blush false", text="Кувалда, хаха!")
            call process_character (k, appearance="blush false", text="Я призываю всех практиковать Камасутру!")
            call process_character (janet, appearance="blush false", text="Кама-что?")
            call process_character (si, appearance="blush false", text="Камасутра!")
            call process_character (si, appearance="blush false", text="Там есть все эти сумасшедшие сексуальные позы, которые ты можешь сделать.")
            call process_character (si, appearance="blush false", text="Ты должна увидеть некоторые штуки, которые [k.say_name] и [n.say_name] делают друг с другом.")
            call process_character (si, appearance="blush false", text="Они делали шестьдесят девять стоя!")
            call process_character (edna, appearance="blush false", text="Если бы я попробовала такую позу, мои суставы защелкнулись бы, и я бы застряла в ней!")
            call process_character (si, appearance="blush false", text="Я не собираюсь даже пытаться сделать что-то подобное, что [k.say_name] делает.")
            call process_character (si, appearance="blush false", text="Я бы точно потянула мышцы!")
            call process_character (janet, appearance="blush false", text="Хмм...")
            call process_character (janet, appearance="blush false", text="Ты должна рассказать мне о некоторых из этих поз, [k.say_name].")
            call process_character (janet, appearance="blush false", text="Я думаю, я могла бы попробовать одну с [n.say_name] когда-нибудь!")

            if finale_julia_sam:
                call process_character (sa, appearance="blush false", text="Мне нужно выбрать несколько для меня и [n.say_name] и попытаться!")
                call process_character (sa, appearance="blush false", text="Может быть, ты поможешь нам выбрать, [k.say_name]!")

            call process_character (k, appearance="blush false", text="Камасутра набирает силу в семье [n.say_name]!")
            call process_character (k, appearance="blush false", text="Не забывай держать себя свободно и гибко!")
            call process_character (n, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="Хрм, ого-го!")
            call process_character (k, appearance="blush false", text="Бьюсь об заклад, это может работать и для анала, [n.say_name]!")
            call process_character (k, appearance="blush false", text="В другой раз, когда мы будем здесь, попробуем!")
        "Мама" if not finale_chose_simone:
            if not finale_chose_simone:
                $ finale_fucked_amount += 1

            $ finale_chose_simone = True

            $ no_bust_art = False
            show bg backyard_daytime
            with Dissolve(0.5)
            call process_character (si, appearance="pose handsup face flirt blush false", text="Я иду, милый!")

            call static_still_ctc ("bg party_simone")

            call process_character (n, appearance="blush false", text="Да, Мам, да!")
            call process_character (n, appearance="blush false", text="Ох!")
            call process_character (si, appearance="blush false", text="Да, детка!")
            call process_character (si, appearance="blush false", text="Трахни Мамочку на глазах у всех!")
            call process_character (si, appearance="blush false", text="Покажи им, как сильно ты любишь меня трахать!")
            call process_character (edna, appearance="blush false", text="Есть ли связь лучше, чем между матерью и сыном?")
            call process_character (k, appearance="blush false", text="Я не знаю, Бабушка, но я знаю, что хер [n.say_name] привязался к маминой киске!")
            call process_character (janet, appearance="blush false", text="Похоже, они много трахались вместе.")
            call process_character (k, appearance="blush false", text="Ох, ты даже не представляешь.")
            call process_character (k, appearance="blush false", text="Если [n.say_name] имеет проблемы с засыпанием ночью, мама придет...")
            call process_character (k, appearance="blush false", text="И она будет сосать его член, пока он не кончит в ее рот, а затем он заснет сразу после этого!")
            call process_character (k, appearance="blush false", text="Это как часовой механизм!")
            call process_character (edna, appearance="blush false", text="Это как более чувственная версия поцелуя на ночь!")

            if finale_julia_sam:
                call process_character (sa, appearance="blush false", text="Также [n.say_name] трахает сиськи Мамы все время!")
                call process_character (sa, appearance="blush false", text="Она всегда вынимает свои сиськи!")
                call process_character (janet, appearance="blush false", text="Моя сестра может многое предложить своими гигантскими дынями!")


            call process_character (si, appearance="blush false", text="Аах...")
            call process_character (si, appearance="blush false", text="[n.say_name] почти ничего не знал о сексе до начала лета!")
            call process_character (si, appearance="blush false", text="Его пенис становился твердым всякий раз, когда он смотрел на мою грудь.")
            call process_character (k, appearance="blush false", text="А остальное стало историей!")
            call process_character (janet, appearance="blush false", text="Ты открыла ему дверь, сестренка!")
            call process_character (janet, appearance="blush false", text="Это был правильный выбор, на мой взгляд!")
            call process_character (si, appearance="blush false", text="Хаах!")
            call process_character (si, appearance="blush false", text="Я ни капли не жалею об этом!")
            call process_character (n, appearance="blush false", text="Ахх, Маааам!")
            call process_character (edna, appearance="blush false", text="Если [n.say_name] будет трахать тебя все время, [si.say_name], в конечном у вас появится новый член семьи!")
        "[sa.say_name]" if finale_julia_sam and not finale_chose_sam:
            if not finale_chose_sam:
                $ finale_fucked_amount += 1

            $ finale_chose_sam = True

            $ no_bust_art = False
            show bg backyard_daytime
            with Dissolve(0.5)
            call process_character (k, appearance="pose armcross face flirt blush false", text="Давай, [sa.say_name]!")

            call static_still_ctc ("bg party_sam")

            call process_character (n, appearance="blush false", text="Хааах!")
            call process_character (sa, appearance="blush false", text="Аах, [n.say_name]!")
            call process_character (sa, appearance="blush false", text="Да, да!")
            call process_character (k, appearance="blush false", text="Обхвати его ногами вот так.")
            call process_character (k, appearance="blush false", text="Я буду поддерживать тебя немного, [sa.say_name].")
            call process_character (edna, appearance="blush false", text="Разве это не самое приятное - видеть всех своих детей вместе [si.say_name]?")
            call process_character (edna, appearance="blush false", text="Они выглядят так, будто знают, что делают!")
            call process_character (si, appearance="blush false", text="Можете ли вы поверить, что [sa.say_name] и [n.say_name] делают это во время игры в видеоигры?")
            call process_character (edna, appearance="blush false", text="Ох, неужели?")
            call process_character (edna, appearance="blush false", text="Хаха!")
            call process_character (janet, appearance="blush false", text="Это меня не удивляет.")
            call process_character (janet, appearance="blush false", text="Они настолько связаны с технологиями, что уже стали многозадачными!")
            call process_character (edna, appearance="blush false", text="Я никогда не смотрела на [n.say_name] со спины.")
            call process_character (edna, appearance="blush false", text="Посмотри, какие у него милые шары!")
            call process_character (k, appearance="blush false", text="Милый бро.")
            call process_character (k, appearance="blush false", text="Ты вкладываешь много силы в эти толчки!")
            call process_character (n, appearance="blush false", text="Ох...{w=1.0}ох...")
            call process_character (sa, appearance="blush false", text="Аах, ахх!")
        "Кейси" if finale_kacey_arrived and not finale_chose_kacey:
            if not finale_chose_kacey:
                $ finale_fucked_amount += 1

            $ finale_chose_kacey = True

            call process_character (gloryhole_girl, appearance="", text="Я готова, [n.say_name]!")
            call process_character (gloryhole_girl, appearance="", text="Моя киска мокрая с тех пор, как я здесь!")

            call static_still_ctc ("bg party_kacey")

            call process_character (n, appearance="blush false", text="Мм-мфф!")
            call process_character (gloryhole_girl, appearance="", text="Так приятно трахаться вне этого туалета, [n.say_name]!")
            call process_character (gloryhole_girl, appearance="", text="Я так рада, что мы больше не ограничены им!")
            call process_character (janet, appearance="blush false", text="Вы познакомились в туалете?")
            call process_character (gloryhole_girl, appearance="", text="Да, в местном парке!")
            call process_character (gloryhole_girl, appearance="", text="Это было наше место встречи в течение всего лета!")
            call process_character (edna, appearance="blush false", text="Как именно вы познакомились в туалете?")
            call process_character (edna, appearance="blush false", text="Ты перепутала знаки?")
            call process_character (k, appearance="blush false", text="[gloryhole_girl.say_name] упускает некоторые важные аспекты всей истории.")
            call process_character (k, appearance="blush false", text="Например, дыру славы.")
            call process_character (si, appearance="blush false", text="Дыра славы?!")
            call process_character (gloryhole_girl, appearance="", text="Ммм, хаах...")
            call process_character (gloryhole_girl, appearance="", text="Да, я проводила свое время в мужском туалете в дыре славы.")
            call process_character (gloryhole_girl, appearance="", text="Мне было...{w=1.0}любопытно, с кем я могу столкнуться.")
            call process_character (edna, appearance="blush false", text="Это...{w=1.0}очень авантюрно с твоей стороны.")
            call process_character (k, appearance="blush false", text="Стратегический выбор слов, Бабушка, ха-ха!")
            call process_character (gloryhole_girl, appearance="", text="С тех пор, как милый член [n.say_name] впервые проткнулся в дыру славы, я не хотела никого, кроме него!")
            call process_character (janet, appearance="blush false", text="Мы это видим.")
            call process_character (n, appearance="blush false", text="Ммм!")
            call process_character (k, appearance="blush false", text="В таком случае, [n.say_name] потеряет сознание из-за сисечного удушья!")
            call process_character (gloryhole_girl, appearance="", text="Неа.")
            call process_character (gloryhole_girl, appearance="", text="Я знаю, что [n.say_name] может справиться гораздо лучше!")
            call process_character (gloryhole_girl, appearance="", text="Вот почему он способен трахать всех нас!")
            call process_character (si, appearance="blush false", text="Ты, кажется, не против, что [n.say_name] трахается со всеми нами!")
            call process_character (gloryhole_girl, appearance="", text="Я совсем не против, потому что [n.say_name] всегда находит для меня время.")
            call process_character (gloryhole_girl, appearance="", text="До тех пор, пока это остается постоянным, он может трахать столько других девушек, сколько ему нравится!")
            call process_character (janet, appearance="blush false", text="Школа будет унылым временем для [n.say_name].")
            call process_character (janet, appearance="blush false", text="Удачи [si.say_name], это все, что я должна сказать.")
            call process_character (si, appearance="blush false", text="Я дала [n.say_name] явные инструкции не иметь никаких сексуальных контактов в школе.")
            call process_character (k, appearance="blush false", text="Держу пари, он не протянет и недели.")
            call process_character (edna, appearance="blush false", text="Я собиралась сказать несколько дней!")
            call process_character (k, appearance="blush false", text="Я так и хотела сказать...")
            call process_character (k, appearance="blush false", text="[n.say_name] трахнет своего учителя.")
            call process_character (k, appearance="blush false", text="Это должно произойти.")
            call process_character (si, appearance="blush false", text="О боже...{w=1.0}это последнее, что мне нужно.")
            call process_character (janet, appearance="blush false", text="Его учитель будет ставить ему сплошные пятерки за все \"дополнительные баллы\", которые он будет делать, ха-ха!")
            call process_character (gloryhole_girl, appearance="", text="Ах...")
            call process_character (gloryhole_girl, appearance="", text="Если тебе нужно, чтобы кто-то забирал его из школы каждый день, я буду добровольцем.")
            call process_character (si, appearance="blush false", text="Это очень щедро с твоей стороны, [gloryhole_girl.say_name]!")
            call process_character (si, appearance="blush false", text="Я обязательно запомню твое предложение!")
            call process_character (gloryhole_girl, appearance="", text="Если я заберу его, мне, вероятно, понадобится [n.say_name] для...{w=1.0}ты знаешь...")
            call process_character (k, appearance="blush false", text="Это же очевидно!")
        "Вики" if finale_vicky_arrived and not finale_chose_vicky:
            if not finale_chose_vicky:
                $ finale_fucked_amount += 1

            $ finale_chose_vicky = True

            call process_character (vicky, appearance="", text="Ты хочешь меня, [n.say_name]?")
            call process_character (vicky, appearance="", text="Я придумала идеальную позицию для нас с тобой!")

            call static_still_ctc ("bg party_vicky")

            call process_character (vicky, appearance="", text="Ммм, да...")
            call process_character (vicky, appearance="", text="...")
            call process_character (vicky, appearance="", text="Я надеялась однажды встретиться с твоей семьей, [n.say_name].")
            call process_character (vicky, appearance="", text="Тем не менее, я не ожидала встретить их в таких обстоятельствах!")
            call process_character (n, appearance="blush false", text="Аах, хаа...")
            call process_character (janet, appearance="blush false", text="Итак, ты и [n.say_name]...{w=1.0}работаете вместе?")
            call process_character (vicky, appearance="", text="Это правильно.")
            call process_character (vicky, appearance="", text="Мы установили деловые отношения в течение лета.")
            call process_character (edna, appearance="blush false", text="Похоже, это нечто большее, чем просто бизнес...")
            call process_character (si, appearance="blush false", text="О да.")
            call process_character (vicky, appearance="", text="Ох...")
            call process_character (vicky, appearance="", text="Могу заверить, что пока [n.say_name] и я выполняем внеклассные мероприятия вместе...")
            call process_character (vicky, appearance="", text="Мы всегда стремились к успеху с нашими усилиями, и каждый раз это было плодотворно.")
            call process_character (k, appearance="blush false", text="Да, ты еще не слышала всех подробностей, Мама, но [vicky.say_name] помогла [n.say_name] значительно расширить его канал!")

            if finale_julia_sam:
                call process_character (sa, appearance="blush false", text="Это потрясающе, Мама!")
                call process_character (sa, appearance="blush false", text="Канал [n.say_name] и мой, взлетел до небес с тех пор, как [n.say_name] поговорил с [vicky.say_name] об улучшениях, которые мы могли бы сделать!")

            call process_character (si, appearance="blush false", text="Серьезно?")
            call process_character (n, appearance="blush false", text="Да, Мам, ах...{w=1.0}[vicky.say_name] показала мне, насколько сильно канал Твинстикс может вырасти.")
            call process_character (n, appearance="blush false", text="Теперь [sa.say_name] и я получаю от этого доход!")
            call process_character (si, appearance="blush false", text="Это невероятно!")
            call process_character (si, appearance="blush false", text="То есть тебе буквально платят за видеоигры?")
            call process_character (vicky, appearance="", text="По сути, да.")
            call process_character (edna, appearance="blush false", text="Это впечатляет, [si.say_name].")
            call process_character (edna, appearance="blush false", text="Если он уже приносит доход вашей семье, кто знает, как далеко он зайдет в ближайшие несколько лет!")
            call process_character (vicky, appearance="", text="[n.say_name] и у меня есть много замечательных вещей, запланированных на будущее.")
            call process_character (vicky, appearance="", text="Мы всегда думаем наперед!")
            call process_character (si, appearance="blush false", text="Я так горжусь тобой, [n.say_name]!")
            call process_character (si, appearance="blush false", text="Я не могу дождаться, чтобы увидеть, над чем вы и [vicky.say_name] будете работать дальше!")
            call process_character (si, appearance="blush false", text="Надеюсь, у вас обоих все получится!")
            call process_character (k, appearance="blush false", text="О, я думаю, так и будет, Мама...")
            call process_character (vicky, appearance="", text="Твоя дочь [k.say_name] также хочет присоединиться к [n.say_name] и мне в нашем новом предприятии.")
            call process_character (vicky, appearance="", text="Мы думаем, она хорошо подойдет для этого.")
            call process_character (si, appearance="blush false", text="Это замечательно, [k.say_name]!")
            call process_character (k, appearance="blush false", text="Я расскажу тебе подробности позже, Мама.")
            call process_character (k, appearance="blush false", text="Все, что нужно знать прямо сейчас, это то, что [n.say_name] - идеальный кандидат для бизнеса [vicky.say_name] .")
            call process_character (si, appearance="blush false", text="...")
            call process_character (si, appearance="blush false", text="Кажется, я начинаю понимать, что это может быть...")
            call process_character (k, appearance="blush false", text="Хехе.")

    call finale_scene_choices (dream=dream)
    return

label finale_scene_end(dream=False):
    call process_character (k, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="Все уже потрахались?")
    call process_character (si, appearance="blush false", text="Дума., да!")
    call process_character (janet, appearance="blush false", text="Как ты держишься, [n.say_name]?")
    call process_character (janet, appearance="blush false", text="Ты должно быть готов взорваться!")
    call process_character (n, appearance="blush false", text="Я...я не знаю, как я держался так долго...")
    call process_character (edna, appearance="blush false", text="Я тоже!")
    call process_character (edna, appearance="blush false", text="Вам нужно снять напряжение с твоих шаров!")
    call process_character (gloryhole_girl, appearance="", text="Я могу помочь с этим [n.say_name].")
    call process_character (gloryhole_girl, appearance="", text="Ты знаешь, что я могу взять на себя весь твой груз.")

    if finale_julia_sam:
        call process_character (sa, appearance="blush false", text="Ох, но я хочу, чтобы меня забрызгал [n.say_name] своим ореховым маслом!")
        call process_character (julia, appearance="blush false", text="Ты не единственная, кто может принять всю сперму от [n.say_name], [gloryhole_girl.say_name].")
        call process_character (julia, appearance="blush false", text="Раньше у меня не было проблем с этим.")

    call process_character (janet, appearance="blush false", text="Я могу заглотить член [n.say_name], чтобы он кончил.")
    call process_character (janet, appearance="blush false", text="Я знаю, как контролировать рвотный рефлекс!")
    call process_character (si, appearance="blush false", text="Не хочешь покрыть мое лицо спермой, милый?")
    call process_character (k, appearance="blush false", text="Стойте, стойте!")
    call process_character (k, appearance="blush false", text="...")
    call process_character (k, appearance="blush false", text="Глупо спорить, кто должен принять сперму [n.say_name].")
    call process_character (k, appearance="blush false", text="Зачем одной девушке столько сливок, если мы можем поделиться?")
    call process_character (edna, appearance="blush false", text="Ты говоришь, что [n.say_name] должен кончить на всех нас?")
    call process_character (k, appearance="blush false", text="Он трахнул всех нас, правильно?")
    call process_character (k, appearance="blush false", text="Таким образом, у него не должно быть проблем с тем, чтобы дать нам всем сперму!")
    call process_character (n, appearance="blush false", text="...")

    call fade_to_black (1)

    call process_character (k, appearance="blush false", text="Соберитесь вокруг, как будто мы делаем фото.")
    call process_character (k, appearance="blush false", text="Прижмемся так близко, как можем!")

    if finale_julia_sam:
        call process_character (sa, appearance="blush false", text="Это должно быть весело!")
        call process_character (k, appearance="blush false", text="[sa.say_name] и [julia.say_name], вы идете вперед.")
        call process_character (k, appearance="blush false", text="Мам, ты хочешь пойти сюда?")

    call process_character (si, appearance="blush false", text="Ох, я понимаю, что ты делаешь, [k.say_name].")
    call process_character (si, appearance="blush false", text="Спеши, прежде чем [n.say_name] кончит!")
    call process_character (janet, appearance="blush false", text="Извини меня, я втискиваюсь сюда...")
    call process_character (k, appearance="blush false", text="Окей...{w=1.0}хорошо…")
    call process_character (k, appearance="blush false", text="Думаю, это все, на что мы способны!")


    if finale_julia_sam:
        call static_still_ctc ("bg party_Group_NoCum")
    else:
        call static_still_ctc ("bg party_Group_NoJS_NoCum")

    call process_character (k, appearance="blush false", text="Открой рот пошире, высунь язык и скажи \"аах!\"")


    if finale_julia_sam:
        call process_character (sa, appearance="blush false", text="Ааах!")
        call process_character (sa, appearance="blush false", text="Я хочу, чтобы все это было у меня во рту!")

    call process_character (gloryhole_girl, appearance="", text="Стреляй сюда, [n.say_name]!")
    call process_character (gloryhole_girl, appearance="", text="Дай мне попробовать твою сперму!")
    call process_character (edna, appearance="blush false", text="Не забывай про Бабулю, [n.say_name]!")

    if finale_julia_sam:
        call process_character (julia, appearance="blush false", text="Старайся не стрелять своей спермой мне в глаза, [n.say_name].")
        call process_character (julia, appearance="blush false", text="Целься чуть ниже, когда целишься в меня.")

    call process_character (si, appearance="blush false", text="Ты можешь замарать меня, как тебе нравится, милый!")
    call process_character (si, appearance="blush false", text="Я не возражаю!")
    call process_character (janet, appearance="blush false", text="Мы с тобой одинаково думаем об этом, сестренка!")
    call process_character (janet, appearance="blush false", text="Я возьму все, что ты мне дашь, [n.say_name]!")
    call process_character (vicky, appearance="", text="Я надеюсь, что у тебя будет достаточно, чтобы добраться до меня, [n.say_name]!")
    call process_character (vicky, appearance="", text="Желаю удачи!")
    call process_character (n, appearance="blush false", text="Ооох, чувак...")
    call process_character (n, appearance="blush false", text="Этот оргазм будет очень большим!")
    call process_character (k, appearance="blush false", text="Я еще больше расширяю рот!")
    call process_character (n, appearance="blush false", text="У меня никогда не было желания кончить так сильно, как сейчас!")
    call process_character (n, appearance="blush false", text="Ммггх...")
    call process_character (n, appearance="blush false", text="Мммх!")
    call process_character (n, appearance="blush false", text="Оооох!!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    show bg party_group_nate_cum2 as cum
    with Dissolve(0.5)
    pause

    if finale_julia_sam:
        call process_character (sa, appearance="blush false", text="Бьюсь об заклад, я получу больше спермы, чем ты, [julia.say_name]!")
        call process_character (julia, appearance="blush false", text="Хех, мы еще посмотрим.")

        hide cum
        show bg party_group_sam_cum as cum_sam
        show bg party_group_julia_cum as cum_julia
        with Dissolve(0.5)
        pause

        call process_character (k, appearance="blush false", text="Вы двое были прямо на линии огня! ")
        call process_character (k, appearance="blush false", text="Везет...")
        call process_character (sa, appearance="blush false", text="Ммм...")
        call process_character (sa, appearance="blush false", text="Вот почему я хотела быть впереди!")
        call process_character (n, appearance="blush false", text="Аах, аах...")
        call process_character (julia, appearance="blush false", text="Я думаю, что это было только начало.")
        call process_character (sa, appearance="blush false", text="Дай нам еще один взрыв, [n.say_name]!")
        call process_character (n, appearance="blush false", text="У-у тебя получилось!")
        call process_character (n, appearance="blush false", text="Еще один...{w=1.0}идет!")

        if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

        show bg party_group_nate_cum2 as cum
        with Dissolve(0.5)
        pause

        call process_character (k, appearance="blush false", text="Вот сюда, бро, вот сюда!")
        call process_character (gloryhole_girl, appearance="", text="Кончи на меня, [n.say_name]!")
        call process_character (gloryhole_girl, appearance="", text="Я хочу твою вкусную сперму!")

        hide cum
        show bg party_group_kacey_cum as cum_kacey
        show bg_party_group_kira_cum_juliasam as cum_kira
        with Dissolve(0.5)
        pause


        call process_character (gloryhole_girl, appearance="", text="Спасибо, [n.say_name], спасибо!")
        call process_character (k, appearance="blush false", text="Мне досталась большая часть!")
        call process_character (k, appearance="blush false", text="Я всегда могу пойти на большее!")
        call process_character (k, appearance="blush false", text="Я высосу все это!")
        call process_character (gloryhole_girl, appearance="", text="Я тоже могу!")
        call process_character (gloryhole_girl, appearance="", text="Не мог бы ты дать нам больше, [n.say_name]?")
        call process_character (n, appearance="blush false", text="Я...я думаю, что смогу.")
        call process_character (si, appearance="blush false", text="Кончи немного сюда, милый.")
        call process_character (si, appearance="blush false", text="Я бы хотела попробовать!")
        call process_character (vicky, appearance="", text="Ты же не хочешь, чтобы у твоей мамы пересохло во рту [n.say_name]?")
        call process_character (vicky, appearance="", text="Нам с ней нужно подкрепиться!")
        call process_character (si, appearance="blush false", text="Хаха!")
        call process_character (si, appearance="blush false", text="Да, это действительно так!")
        call process_character (n, appearance="blush false", text="Ладно!")
        call process_character (n, appearance="blush false", text="Я дам вам обеим!")
        call process_character (n, appearance="blush false", text="Приготовитесь!")

        if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
        show bg party_group_nate_cum1 as cum
        with Dissolve(0.5)
        pause

        call process_character (n, appearance="blush false", text="Гаах!")
        call process_character (vicky, appearance="", text="Вот оно!")
        call process_character (si, appearance="blush false", text="Это мой мальчик!")

        hide cum
        show bg party_group_vicky_cum as cum_vicky
        show bg party_group_simone_cum as cum_simone
        with Dissolve(0.5)
        pause

        call process_character (k, appearance="blush false", text="Еще один хороший выстрел, [n.say_name]!")

        call process_character (k, appearance="blush false", text="Она пронеслась мимо моего уха!")
        call process_character (vicky, appearance="", text="Это так здорово, сперма на моем лице!")
        call process_character (vicky, appearance="", text="И вкус как никогда хорош!")
        call process_character (si, appearance="blush false", text="Я знала, что семя моего сына что-то особенное!")
        call process_character (si, appearance="blush false", text="И я говорю это не только потому, что я твоя Мама!")
        call process_character (gloryhole_girl, appearance="", text="Твоя Мама права, [n.say_name]!")
        call process_character (gloryhole_girl, appearance="", text="Я могу глотать твою сперму весь день!")
        call process_character (k, appearance="blush false", text="Твоя сперма может быть любимой группой продуктов питания!")
        call process_character (sa, appearance="blush false", text="Я буду есть ее каждый день!")
        call process_character (julia, appearance="blush false", text="Если бы она была в шоколаде или арахисовом масле, я бы была рада.")
        call process_character (janet, appearance="blush false", text="[n.say_name], не забывай о нас!")
        call process_character (edna, appearance="blush false", text="Мы все еще ждем!")
        call process_character (n, appearance="blush false", text="Извини, Тетя [janet.say_name] и Бабушка.")
        call process_character (n, appearance="blush false", text="Надеюсь, я смогу кончить еще раз.")
        call process_character (janet, appearance="blush false", text="Ты должен, [n.say_name], ты должен!")
        call process_character (edna, appearance="blush false", text="Ты сможешь это сделать, [n.say_name]!")
        call process_character (edna, appearance="blush false", text="Это будет последний выстрел!")
        call process_character (k, appearance="blush false", text="Да, выпусти монстра из яиц!")
        call process_character (n, appearance="blush false", text="Ах...")
        call process_character (n, appearance="blush false", text="Да, у...{w=1.0}у меня получается!")
        call process_character (n, appearance="blush false", text="Я смогу еще раз кончить!")
        call process_character (janet, appearance="blush false", text="[n.say_name] сохранил лучшее для последнего выстрела!")
        call process_character (edna, appearance="blush false", text="Наше терпение будет вознаграждено!")
        call process_character (n, appearance="blush false", text="Ммм!")
        call process_character (n, appearance="blush false", text="Тетя [janet.say_name]...{w=1.0}Бабушка...")
        call process_character (n, appearance="blush false", text="Вот, для вас!")

        if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
        show bg party_group_nate_cum3 as cum
        with Dissolve(0.5)
        pause

        call process_character (janet, appearance="blush false", text="Не пропусти это, Мама!")
        call process_character (edna, appearance="blush false", text="Не пропущу, не пропущу!")

        hide cum
        show bg_party_group_janet_cum_juliasam as cum_janet
        show bg_party_group_edna_cum_juliasam as cum_edna
        with Dissolve(0.5)
        pause

        call process_character (janet, appearance="blush false", text="Оуу, да!")
        call process_character (janet, appearance="blush false", text="Хорошо и грязно!")
        call process_character (edna, appearance="blush false", text="Это стоило того, чтобы ждать!")
        call process_character (edna, appearance="blush false", text="Твоя сперма все еще густая, даже после всех твоих эякуляций!")
        call process_character (n, appearance="blush false", text="{i}Вздох…вздох...{/i}")
        call process_character (n, appearance="blush false", text="Это...вот и все.")
        call process_character (n, appearance="blush false", text="Не думаю, что у меня осталось и капли.")
        call process_character (sa, appearance="blush false", text="Это нормально, [n.say_name]!")
        call process_character (sa, appearance="blush false", text="Все цели поражены!")
        call process_character (k, appearance="blush false", text="Ага!")
        call process_character (k, appearance="blush false", text="Мы все покрыты твоим мужским молоком!")
        call process_character (k, appearance="blush false", text="Теперь мы все одно большое, белое, липкое месиво!")
    else:
        call process_character (k, appearance="blush false", text="Начинается!")
        call process_character (k, appearance="blush false", text="Вот сюда, бро, вот сюда!")
        call process_character (gloryhole_girl, appearance="", text="Кончи на меня, [n.say_name]!")
        call process_character (gloryhole_girl, appearance="", text="Я хочу твою вкусную сперму!")

        hide cum
        show bg party_group_kacey_cum as cum_kacey
        show bg party_group_kira_cum as cum_kira
        with Dissolve(0.5)
        pause

        call process_character (gloryhole_girl, appearance="", text="Спасибо, [n.say_name], спасибо!")
        call process_character (k, appearance="blush false", text="Мне досталась большая часть!")
        call process_character (k, appearance="blush false", text="Я всегда могу пойти на большее!")
        call process_character (k, appearance="blush false", text="Я высосу все это!")
        call process_character (gloryhole_girl, appearance="", text="Я тоже могу!")
        call process_character (gloryhole_girl, appearance="", text="Не мог бы ты дать нам больше, [n.say_name]?")
        call process_character (n, appearance="blush false", text="Я...я думаю, что смогу.")
        call process_character (si, appearance="blush false", text="Кончи немного сюда, милый.")
        call process_character (si, appearance="blush false", text="Я бы хотела попробовать!")
        call process_character (vicky, appearance="", text="Ты же не хочешь, чтобы у твоей мамы пересохло во рту [n.say_name]?")
        call process_character (vicky, appearance="", text="Нам с ней нужно подкрепиться!")
        call process_character (si, appearance="blush false", text="Хаха!")
        call process_character (si, appearance="blush false", text="Да, это действительно так!")
        call process_character (n, appearance="blush false", text="Ладно!")
        call process_character (n, appearance="blush false", text="Я дам вам обеим!")
        call process_character (n, appearance="blush false", text="Приготовитесь!")

        if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
        show bg party_group_nate_cum1 as cum
        with Dissolve(0.5)
        pause

        call process_character (n, appearance="blush false", text="Гаах!")
        call process_character (vicky, appearance="", text="Вот оно!")
        call process_character (si, appearance="blush false", text="Это мой мальчик!")

        hide cum
        show bg party_group_vicky_cum as cum_vicky
        show bg party_group_simone_cum as cum_simone
        with Dissolve(0.5)
        pause

        call process_character (k, appearance="blush false", text="Еще один хороший выстрел, [n.say_name]!")
        call process_character (k, appearance="blush false", text="Она пронеслась мимо моего уха!")
        call process_character (vicky, appearance="", text="Это так здорово, сперма на моем лице!")
        call process_character (vicky, appearance="", text="И вкус как никогда хорош!")
        call process_character (si, appearance="blush false", text="Я знала, что семя моего сына что-то особенное!")
        call process_character (si, appearance="blush false", text="И я говорю это не только потому, что я твоя Мама!")
        call process_character (gloryhole_girl, appearance="", text="Твоя Мама права, [n.say_name]!")
        call process_character (gloryhole_girl, appearance="", text="Я могу глотать твою сперму весь день!")
        call process_character (k, appearance="blush false", text="Твоя сперма может быть любимой группой продуктов питания!")
        call process_character (janet, appearance="blush false", text="[n.say_name], не забывай о нас!")
        call process_character (edna, appearance="blush false", text="Мы все еще ждем!")
        call process_character (n, appearance="blush false", text="Извини, Тетя [janet.say_name] и Бабушка.")
        call process_character (n, appearance="blush false", text="Надеюсь, я смогу кончить еще раз.")
        call process_character (janet, appearance="blush false", text="Ты должен, [n.say_name], ты должен!")
        call process_character (edna, appearance="blush false", text="Ты сможешь это сделать, [n.say_name]!")
        call process_character (edna, appearance="blush false", text="Это будет последний выстрел!")
        call process_character (k, appearance="blush false", text="Да, выпусти монстра из яиц!")
        call process_character (n, appearance="blush false", text="Ах...")
        call process_character (n, appearance="blush false", text="Да, у...{w=1.0}у меня получается!")
        call process_character (n, appearance="blush false", text="Я смогу еще раз кончить!")
        call process_character (janet, appearance="blush false", text="[n.say_name] сохранил лучшее для последнего выстрела!")
        call process_character (edna, appearance="blush false", text="Наше терпение будет вознаграждено!")
        call process_character (n, appearance="blush false", text="Ммм!")
        call process_character (n, appearance="blush false", text="Тетя [janet.say_name]...{w=1.0}Бабушка...")
        call process_character (n, appearance="blush false", text="Вот, для вас!")

        if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
        show bg party_group_nate_cum3 as cum
        with Dissolve(0.5)
        pause

        call process_character (janet, appearance="blush false", text="Не пропусти это, Мама!")
        call process_character (edna, appearance="blush false", text="Не пропущу, не пропущу!")

        hide cum
        show bg party_group_janet_cum as cum_janet
        show bg party_group_edna_cum as cum_edna
        with Dissolve(0.5)
        pause

        call process_character (janet, appearance="blush false", text="Оуу, да!")
        call process_character (janet, appearance="blush false", text="Хорошо и грязно!")
        call process_character (edna, appearance="blush false", text="Это стоило того, чтобы ждать!")
        call process_character (edna, appearance="blush false", text="Твоя сперма все еще густая, даже после всех твоих эякуляций!")
        call process_character (n, appearance="blush false", text="{i}Вздох...{w=1.0}вздох...{/i}")
        call process_character (n, appearance="blush false", text="Это...{w=1.0}вот и все.")
        call process_character (n, appearance="blush false", text="Не думаю, что у меня осталось и капли.")
        call process_character (k, appearance="blush false", text="Все в порядке, бро!")
        call process_character (k, appearance="blush false", text="Мы все покрыты твоим мужским молоком!")
        call process_character (k, appearance="blush false", text="Теперь мы все одно большое, белое, липкое месиво!")
        call process_character (n, appearance="blush false", text="...")

    call process_character (gloryhole_girl, appearance="", text="Это была отличная вечеринка!")
    call process_character (gloryhole_girl, appearance="", text="Спасибо за приглашение!")
    call process_character (vicky, appearance="", text="Да, благодарю вас!")
    call process_character (vicky, appearance="", text="Я счастлива, что смогла прийти вовремя!")
    call process_character (si, appearance="blush false", text="Всегда пожалуйста!")
    call process_character (si, appearance="blush false", text="Я надеюсь, что мы сможем сделать это снова!")


    if finale_julia_sam:
        call process_character (sa, appearance="blush false", text="Да!")
        call process_character (sa, appearance="blush false", text="Хотелось бы чаще приходить на такие вечеринки!")
        call process_character (julia, appearance="blush false", text="Обычно я не люблю вечеринки.")
        call process_character (julia, appearance="blush false", text="Но этот тип мне нравится.")

    call process_character (k, appearance="blush false", text="Ох, таких вечеринок наверняка будет больше.")
    call process_character (k, appearance="blush false", text="До тех пор, пока член [n.say_name] остается активным, мы будем видеть друг друга все чаще и больше!")
    call process_character (janet, appearance="blush false", text="Скоро станет слишком прохладно, чтобы устраивать вечеринки у бассейна.")
    call process_character (janet, appearance="blush false", text="Нам нужно переместиться внутрь.")
    call process_character (edna, appearance="blush false", text="Я была бы более чем готова провести вечеринку в своей квартире!")
    call process_character (si, appearance="blush false", text="Наш дом также доступен!")
    call process_character (vicky, appearance="", text="Просто свяжитесь со мной раньше времени, и я смогу сделать это без проблем.")
    call process_character (gloryhole_girl, appearance="", text="Не могу дождаться, когда эти вечеринки будут круглый год!")
    call process_character (gloryhole_girl, appearance="", text="Разве это не захватывающе, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Да, это действительно так!")
    call process_character (k, appearance="blush false", text="Мы во всем разберемся.")
    call process_character (k, appearance="blush false", text="Я умираю с голоду от всего этого.")
    call process_character (k, appearance="blush false", text="У нас есть еще чипсы?")

    if finale_julia_sam:
        call process_character (julia, appearance="blush false", text="Мне нужно что-нибудь сладкое.")
        call process_character (julia, appearance="blush false", text="Ты не знаешь, бабушка пекла печенье?")
        call process_character (sa, appearance="blush false", text="Я хочу сделать фруктовый коктейль!")


    call process_character (edna, appearance="blush false", text="Нам всем нужно перезарядить наши батареи после этого!")
    call process_character (vicky, appearance="", text="Жаль, что у меня нет купальника, чтобы пойти в бассейн.")
    call process_character (janet, appearance="blush false", text="Ах, иди голая!")
    call process_character (janet, appearance="blush false", text="Никто из нас не будет возражать!")
    call process_character (gloryhole_girl, appearance="", text="Как ты думаешь, ты хочешь трахнуть нас снова позже, [n.say_name]?")
    call process_character (n, appearance="blush false", text="...")

    call finale_scene_end_helper
    python:
        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_group_sex", 1)
            stats.add_stat("times_cummed_in_mouth", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("finale_scene", dream=dream)
    return

label finale_scene_end_helper:
    call fade_to_black (1)
    hide cum
    hide cum_kacey
    hide cum_janet
    hide cum_edna
    hide cum_kira
    hide cum_vicky
    hide cum_simone
    hide cum_sam
    hide cum_julia

    if finale_julia_sam:
        $ finale_scene_completed_with_julia_sam = True

    return

label finale_scene_revisit:
    call finale_scene_initialize

    $ finale_fucked_amount_goal = 3

    call process_character (n, appearance="pose twohandfist face happy blush false", text="(Я хочу устроить еще одну вечеринку в бассейне, как раньше!)")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="(Я собираюсь позвонить всем!)")

    call fade_to_black (1)

    call process_new_location ("bg backyard_daytime")

    python hide:
        play_music("audio/music/Resort Loop2.ogg", fadeout=1.0, fadein = 1.0)

    jump finale_scene_revisit_fuck_choices
    return

label finale_scene_revisit_end:
    call finale_scene_end_helper

    python:
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_group_sex", 1)
        stats.add_stat("times_cummed_in_mouth", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("finale_scene_revisit", reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label finale_scene_cum:


    menu:
        "Кончить на Бабушку" if not finale_cum_edna:
            if not finale_cum_edna:
                $ finale_cum_amount += 1

            $ finale_cum_edna = True

            call process_character (edna, appearance="blush false", text="Я люблю своего внука, и его сперму!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            show bg party_group_nate_cum2 as cum
            with Dissolve(0.5)
            pause

            hide cum
            if finale_julia_sam:
                show bg_party_group_edna_cum_juliasam as cum_edna
            else:
                show bg party_group_edna_cum as cum_edna
            with Dissolve(0.5)
            pause


        "Кончить на [janet.say_name]" if not finale_cum_janet:
            if not finale_cum_janet:
                $ finale_cum_amount += 1

            $ finale_cum_janet = True

            call process_character (janet, appearance="blush false", text="Дай своей любимой тете то, что она хочет!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            show bg party_group_nate_cum2 as cum
            with Dissolve(0.5)
            pause

            hide cum
            if finale_julia_sam:
                show bg_party_group_janet_cum_juliasam as cum_janet
            else:
                show bg party_group_janet_cum as cum_janet
            with Dissolve(0.5)
            pause


        "Кончить на [julia.say_name]" if finale_julia_sam and not finale_cum_julia:
            if not finale_cum_julia:
                $ finale_cum_amount += 1

            $ finale_cum_julia = True

            call process_character (julia, appearance="blush false", text="Мы извращенцы до мозга костей, [n.say_name]!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            show bg party_group_nate_cum3 as cum
            with Dissolve(0.5)
            pause

            hide cum
            show bg party_group_julia_cum as cum_julia
            with Dissolve(0.5)
            pause


        "Кончить на [k.say_name]" if not finale_cum_kira:
            if not finale_cum_kira:
                $ finale_cum_amount += 1

            $ finale_cum_kira = True

            call process_character (k, appearance="blush false", text="Сколько чуваков могут сказать, что они пристрастились ко всем цыпочкам в своей семье одновременно?")
            call process_character (k, appearance="blush false", text="Уверен, что это эксклюзивный клуб только с одним членом...{w=1.0}тобой!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            show bg party_group_nate_cum2 as cum
            with Dissolve(0.5)
            pause

            hide cum
            if finale_julia_sam:
                show bg_party_group_kira_cum_juliasam as cum_kira
            else:
                show bg party_group_kira_cum as cum_kira
            with Dissolve(0.5)
            pause

        "Кончить на Маму" if not finale_cum_simone:
            if not finale_cum_simone:
                $ finale_cum_amount += 1

            $ finale_cum_simone = True

            call process_character (si, appearance="blush false", text="Оох, Мм...")
            call process_character (si, appearance="blush false", text="Я так счастлива быть твоей матерью!")
            call process_character (si, appearance="blush false", text="Твоя сперма так дорога мне.")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            show bg party_group_nate_cum2 as cum
            with Dissolve(0.5)
            pause

            hide cum
            show bg party_group_simone_cum as cum_simone
            with Dissolve(0.5)
            pause

        "Кончить на [sa.say_name]" if finale_julia_sam and not finale_cum_sam:
            if not finale_cum_sam:
                $ finale_cum_amount += 1

            $ finale_cum_sam = True

            call process_character (sa, appearance="blush false", text="Разве это не было бы самой сумасшедшей вещью, сделать селфи этого, [n.say_name]?!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            show bg party_group_nate_cum2 as cum
            with Dissolve(0.5)
            pause

            hide cum
            show bg party_group_sam_cum as cum_sam
            with Dissolve(0.5)
            pause


        "Кончить на Кейси" if not finale_cum_kacey:
            if not finale_cum_kacey:
                $ finale_cum_amount += 1

            $ finale_cum_kacey = True

            call process_character (gloryhole_girl, appearance="", text="Я буду спермошлюхой только для тебя, [n.say_name]!")


            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            show bg party_group_nate_cum2 as cum
            with Dissolve(0.5)
            pause

            hide cum
            show bg party_group_kacey_cum as cum_kacey
            with Dissolve(0.5)
            pause


        "Кончить на Вики" if not finale_cum_vicky:
            if not finale_cum_vicky:
                $ finale_cum_amount += 1

            $ finale_cum_vicky = True

            call process_character (vicky, appearance="", text="Скоро мне придется добавить буккаке в качестве жанра в наши видео, [n.say_name]!")

            if persistent.enable_sex_sounds:
                $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

            show bg party_group_nate_cum2 as cum
            with Dissolve(0.5)
            pause

            hide cum
            show bg party_group_vicky_cum as cum_vicky
            with Dissolve(0.5)
            pause

    if finale_cum_amount >= finale_cum_amount_goal:
        jump finale_scene_revisit_end
    else:
        jump finale_scene_cum

    return

label finale_scene_revisit_fuck_choices:
    $ dice_roll = random.randint(1,2)
    menu:
        "Бабушка":
            if not finale_chose_edna:
                $ finale_fucked_amount += 1

            $ finale_chose_edna = True

            call static_still_ctc ("bg party_Edna")

            if dice_roll == 1:
                call process_character (edna, appearance="blush false", text="Хорошо, что ты из семьи с высокой жизненной силой!")
            else:
                call process_character (edna, appearance="blush false", text="Будешь ли ты приглашать на эти вечеринки других девушек?")
        "Тетя [janet.say_name]":

            if not finale_chose_janet:
                $ finale_fucked_amount += 1

            $ finale_chose_janet = True
            call static_still_ctc ("bg party_Janet")

            if dice_roll == 1:
                call process_character (janet, appearance="blush false", text="Тебе определенно понадобимся все мы на быстром наборе, [n.say_name]!")
            else:
                call process_character (janet, appearance="blush false", text="Мы все должны практиковать некоторые позы йоги, которые повышают наше либидо!")

        "[julia.say_name]" if finale_julia_sam:
            if not finale_chose_julia:
                $ finale_fucked_amount += 1
            call static_still_ctc ("bg party_julia")

            $ finale_chose_julia = True

            if dice_roll == 1:
                call process_character (julia, appearance="blush false", text="Если ты придешь ко мне домой в будущем, просто знай, что мы с мамой трахнем тебя.")
            else:
                call process_character (julia, appearance="blush false", text="Интересно, сможешь ли ты заняться аналом со всеми нами тоже.")
        "[k.say_name]":


            if not finale_chose_kira:
                $ finale_fucked_amount += 1
            call static_still_ctc ("bg party_kira")

            if dice_roll == 1:
                call process_character (k, appearance="blush false", text="Я могла бы начать делать дырки на шортах, [n.say_name].")
                call process_character (k, appearance="blush false", text="Тогда ты сможешь просто подойти и трахнуть меня, когда захочешь!")
            else:
                call process_character (k, appearance="blush false", text="Я хочу услышать все о том, что ты делаешь в школе, [n.say_name].")
                call process_character (k, appearance="blush false", text="Бьюсь об заклад, ты трахнешь как минимум пятерых девушек до зимних каникул!")

            $ finale_chose_kira = True
        "Мама":

            if not finale_chose_simone:
                $ finale_fucked_amount += 1
            call static_still_ctc ("bg party_simone")

            if dice_roll == 1:
                call process_character (si, appearance="blush false", text="Нам понадобится гораздо больше мебели, когда эта компания станет регулярной!")
            else:
                call process_character (si, appearance="blush false", text="Помни, ты всегда можешь сделать перерыв, милый.")
                call process_character (si, appearance="blush false", text="Не то, чтобы ты действительно хочешь делать это большую часть времени!")

            $ finale_chose_simone = True

        "[sa.say_name]" if finale_julia_sam:
            if not finale_chose_sam:
                $ finale_fucked_amount += 1
            call static_still_ctc ("bg party_sam")

            if dice_roll == 1:
                call process_character (sa, appearance="blush false", text="Я надеюсь, что мы встретим новых классных друзей в школе, [n.say_name].")
                call process_character (sa, appearance="blush false", text="Тогда мы могли бы пригласить их на эти вечеринки!")
            else:
                call process_character (sa, appearance="blush false", text="Это было бы эпично, если бы ты кончил во все наши киски!")
                call process_character (k, appearance="blush false", text="Точно!")

            $ finale_chose_sam = True
        "Кейси":


            if not finale_chose_kacey:
                $ finale_fucked_amount += 1
            call static_still_ctc ("bg party_kacey")

            if dice_roll == 1:
                call process_character (gloryhole_girl, appearance="", text="Я должна посмотреть, могу ли я подать заявление на должность учителя в твоей школе, [n.say_name].")
                call process_character (gloryhole_girl, appearance="", text="Тогда мы могли бы видеть друг друга еще больше!")
            else:
                call process_character (gloryhole_girl, appearance="", text="Ты должен зайти ко мне однажды, [n.say_name].")
                call process_character (gloryhole_girl, appearance="", text="Мы можем трахаться весь день и всю ночь там!")

            $ finale_chose_kacey = True
        "Вики":


            if not finale_chose_vicky:
                $ finale_fucked_amount += 1
            call static_still_ctc ("bg party_vicky")

            if dice_roll == 1:
                call process_character (vicky, appearance="", text="Вся твоя семья - идеальные кандидаты для сайта!")
                call process_character (vicky, appearance="", text="Я просто хочу посмотреть, смогу ли я убедить кого-нибудь из них сниматься...")
            else:
                call process_character (vicky, appearance="", text="Тебе стоит подумать о сексе с высокопоставленными женщинами-руководителями.")
                call process_character (vicky, appearance="", text="Мы могли бы выиграть несколько крупных сделок таким образом!")

            $ finale_chose_vicky = True
        "Кончить" if finale_fucked_amount >= 3:
            if finale_julia_sam:
                call static_still_ctc ("bg party_Group_NoCum")
            else:
                call static_still_ctc ("bg party_Group_NoJS_NoCum")
            jump finale_scene_cum

    jump finale_scene_revisit_fuck_choices

    return