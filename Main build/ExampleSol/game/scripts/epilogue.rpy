label epilogue:

    $ renpy.scene('screens')
    $ stop_music(fadeout=1)
    call fade_to_black (2)
    $ replace_position = True

    "{i}Несколько недель спустя...{/i}"

    $ play_music("audio/music/Daily_Music_01.ogg", fadeout=1)
    call process_scene_beginning (bg="bg nate_room_daytime")

    call process_character (n, appearance="outfit nudesoft pose handsdown face aroused blush false", text="{i}Зевает.{/i}..")
    call process_character (n, appearance="outfit nudesoft pose handsdown face aroused blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose handsdown face concerned blush false", text="(Ну, это свершилось...)")
    call process_character (n, appearance="outfit nudesoft pose handsdown face concerned blush false", text="(Еще один летний день, и снова в школу...)")
    call process_character (n, appearance="outfit nudesoft pose handsdown face concerned blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face happy blush false", text="(Боже, это лето было эпическим!)")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face happy blush false", text="(Я думал, что начало было сумасшедшим со всеми переездами и разборами вещей)")
    call process_character (n, appearance="outfit nudesoft pose handsdown face happy blush false", text="(Но это было только начало!)")

    if finale_scene_completed_with_julia_sam:
        call process_character (sa, text="[n.say_name], ты не спишь?")
        call process_character (n, appearance="pose handsdown face neutral blush false", text="Только что встал!")
        call process_character (sa, appearance="outfit nude pose handsbehind face neutral blush false", text="Спускайся вниз!")
        call process_character (sa, appearance="outfit nude pose handsbehind face neutral blush false", text="Мама, Бабушка и все остальные здесь, чтобы сделать групповое фото!")
        call process_character (n, appearance="pose twohandfist face neutral blush false", text="Ах да, мы собирались сделать это сегодня!")
        call process_character (sa, appearance="outfit nude pose handface face neutral blush false", text="И не забудь о нашей секс-вечеринке после этого!")
        call process_character (sa, appearance="outfit nude pose handface face happy blush false", text="Тема дня поза раком!")
        call process_character (n, appearance="pose handfist face happy blush false", text="Да, мне нравится эта поза!")
        call process_character (sa, appearance="outfit nude pose leaning face happy blush false", text="Мне тоже!")
    else:

        call process_character (k, text="Брат, ты все еще спишь или как?")
        call process_character (n, appearance="pose handsdown face neutral blush false", text="Только что встал!")
        call process_character (k, appearance="outfit nude pose armcross face neutral blush false", text="Давай, тормоз!")
        call process_character (k, appearance="outfit nude pose armcross face neutral blush false", text="Все ждут от тебя групповое фото!")
        call process_character (n, appearance="pose twohandfist face neutral blush false", text="Ах да, мы собирались сделать это сегодня!")
        call process_character (k, appearance="outfit nude pose handhip face neutral blush false", text="Да, а потом мы будем играть в бутылочку, а ты будешь бутылкой!")
        call process_character (n, appearance="pose behindhead face neutral blush false", text="Да?")
        call process_character (k, appearance="outfit nude pose armsup face happy blush false", text="Ну да, после того, как я предложу это!")
        call process_character (k, appearance="outfit nude pose armsup face happy blush false", text="Так что давай, двигай свой член и яйца вниз!")

    call process_scene_beginning (bg="bg hallway_daytime")

    call process_character (n, appearance="outfit nudesoft pose handsdown face neutral blush false", text="(Хорошо, что я продолжаю работать над улучшением моей сексуальной способности)")
    call process_character (n, appearance="outfit nudesoft pose handsdown face happy blush false", text="(В среднем, я могу трахаться три раза в день!)")
    call process_character (n, appearance="outfit nudesoft pose behindhead face neutral blush false", text="(Думаю, если мне повезет, я смогу пять или шесть раз в день)")

    if finale_scene_completed_with_julia_sam:
        call process_character (n, appearance="pose handsdown face neutral blush false", text="(Утром обычно Мама или [sa.say_name] будят меня минетом или мастурбацией)")
        call process_character (n, appearance="pose handsdown face neutral blush false", text="(Также иногда [k.say_name] приходит, чтобы разбудить меня и пососать мой член, идя на кухню)")

        call process_new_location ("bg kitchen_daytime")

        call process_character (n, appearance="outfit nudesoft pose behindhead face neutral blush false", text="(После этого все зависит только от того, чья очередь трахаться)")
        call process_character (n, appearance="pose behindhead face neutral blush false", text="(Тетя [janet.say_name] и [julia.say_name] любят приходить по выходным, и они объединяют усилия)")
        call process_character (n, appearance="pose behindhead face neutral blush false", text="([gloryhole_girl.say_name] снимает квартиру всего в паре кварталов отсюда, и я навещаю ее ночью)")
        call process_character (n, appearance="pose twohandfist face happy blush false", text="(Иногда [sa.say_name] присоединяется, и мы проводим несколько потрясающих игровых сессий!)")
    else:

        call process_character (n, appearance="pose handsdown face neutral blush false", text="(По утрам меня обычно будит Мама, делая мне минет или мастурбируя)")
        call process_character (n, appearance="pose handsdown face neutral blush false", text="(Также иногда [k.say_name] приходит, чтобы разбудить меня и пососать мой член, идя на кухню)")

        call process_new_location ("bg kitchen_daytime")

        call process_character (n, appearance="outfit nudesoft pose behindhead face neutral blush false", text="(После этого все зависит только от того, чья очередь трахаться)")
        call process_character (n, appearance="pose behindhead face neutral blush false", text="(Тетя [janet.say_name] обычно остается на выходные, и мы устраиваем групповушку с ней, Мамой и [k.say_name]!)")
        call process_character (n, appearance="pose behindhead face neutral blush false", text="([gloryhole_girl.say_name] снимает квартиру всего в паре кварталов отсюда, и я навещаю ее ночью)")
        call process_character (n, appearance="pose twohandfist face happy blush false", text="(Мы проводим несколько потрясающих игровых сессий!)")

    call process_character (n, appearance="pose twohandfist face happy blush false", text="(Мне нравится лежать на [gloryhole_girl.say_name] и засунуть член в ее задницу или киску, пока мы играем!)")

    call process_new_location ("bg living_room_daytime")

    call process_character (n, appearance="outfit nudesoft pose handsdown face neutral blush false", text="([vicky.say_name] наняла Маму в качестве секретаря для своего бизнеса)")
    call process_character (n, appearance="pose handsdown face happy blush false", text="(Когда они в офисе, то ходят топлесс, поэтому я могу играть с их сиськами весь день!)")
    call process_character (n, appearance="pose handfist face neutral blush false", text="(А пятницы зарезервированы для Бабушки)")
    call process_character (n, appearance="pose handfist face happy blush false", text="(Мы трахаемся в течение нескольких часов подряд, это потрясающе!)")

    call process_character (si, appearance="outfit nude pose handsup face neutral blush false", text="Вот ты где, милый!")
    call process_character (n, appearance="outfit nudesoft pose behindhead face neutral blush false", text="Прости, что заставил всех ждать, Мама.")

    call process_character (si, appearance="outfit nude pose handsup face happy blush false", text="Нам бы пришлось ждать в любом случае, из-за [janet.say_name]!")

    call process_character (n, appearance="outfit nudesoft pose handsdown face neutral blush false")


    call process_character (n, appearance="outfit nudesoft pose handsdown face neutral blush false")


    call process_character (janet, appearance="outfit nude pose handchest face neutral blush false", text="Я настраиваю освещение для этой фотографии.")
    call process_character (janet, appearance="outfit nude pose handchest face happy blush false", text="Нет ничего хуже, чем размытое изображение от вспышки камеры!")
    call process_character (janet, appearance="outfit nude pose handhips face neutral blush false", text="Лучше использовать естественный свет с небольшим рассеиванием.")
    call process_character (si, appearance="outfit nude pose armunder face happy blush false", text="Я ничего не понимаю, когда дело доходит до этого!")
    call process_character (si, appearance="outfit nude pose armunder face happy blush false", text="Я просто знаю, что нужно нажать кнопку на камере, и тогда вылетит птичка!")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Может ли камера сделать меня моложе лет на двадцать?")
    call process_character (k, appearance="outfit nude pose handhip face neutral blush false", text="С этим могут помочь программы редактирования фотографий, Бабушка.")

    if finale_scene_completed_with_julia_sam:
        call process_character (sa, appearance="outfit nude pose leaning face neutral blush false", text="Хорошо, я устанавливаю таймер для камеры, Тетя [janet.say_name]!")
        call process_character (sa, appearance="outfit nude pose leaning face neutral blush false", text="Установить на тридцать секунд?")
        call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="Наверное, лучше установить его на минуту.")
        call process_character (julia, appearance="outfit nude pose armcross face neutral blush false", text="Кто знает, сколько времени у нас уйдет на то, чтобы занять свои позиции.")

        gloryhole_girl.c "Камера достаточно далеко, чтобы заснять нас всех?"
        vicky.c "Если нам придется теснее прижиматься, так тому и быть."

        call process_character (k, appearance="pose armsup face neutral blush false", text="Мы можем закончить тем, что наши сиськи будут прижаты друг к другу.")
        call process_character (k, appearance="pose armsup face happy blush false", text="[n.say_name] одобрил бы!")
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (sa, appearance="outfit nude pose handface face embarrassed blush false", text="Ой, я уже нажала на кнопку!")
        call process_character (sa, appearance="outfit nude pose handface face embarrassed blush false", text="Фотоаппарат ведет обратный отсчет!")
        call process_character (si, appearance="pose handsfront face embarrassed blush false", text="О Господи, давайте занимать места!")
        call process_character (si, appearance="pose handsfront face embarrassed blush false", text="Скорей, скорей!")


        $ no_bust_art = True
        $ clear_characters()
        show bg photo_epilogue_background
        show family_milf_layer:
            Null()
        show nate_layer:
            Null()
        show julia_sam_layer:
            Null()
        show nonrelated_layer:
            Null()
        with Dissolve(0.5)






        call process_character (si, appearance="blush false", text="Ладно, давайте посмотрим...")
        call process_character (si, appearance="blush false", text="Мам, встань вон там.")
        call process_character (si, appearance="blush false", text="[janet.say_name], ты хочешь быть рядом с Мамой?")
        call process_character (janet, appearance="blush false", text="Конечно!")
        call process_character (si, appearance="blush false", text="А я буду стоять напротив тебя.")
        call process_character (si, appearance="blush false", text="[k.say_name], ты самая высокая, поэтому ты должна быть сзади.")
        call process_character (k, appearance="blush false", text="Буду рядом с тобой, Мама.")

        $ play_music("audio/music/Smooth 01.ogg", fadeout=1)

        $ quick_menu = False
        window hide
        show bg photo_epilogue_ednajanetkirasimone_np as family_milf_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True

        call process_character (janet, appearance="blush false", text="Ты можешь проверить, находимся ли мы в кадре [julia.say_name]?")
        call process_character (julia, appearance="blush false", text="...")
        call process_character (julia, appearance="blush false", text="Да, все нормально.")
        call process_character (si, appearance="blush false", text="Теперь что касается тебя, [n.say_name], можешь ли ты...")
        call process_character (si, appearance="blush false", text="[n.say_name], прекрати ласкать [sa.say_name].")
        call process_character (si, appearance="blush false", text="Ты нужен нам здесь.")
        call process_character (n, appearance="blush false", text="О, да!")
        call process_character (si, appearance="blush false", text="Почему бы тебе не пойти...")
        call process_character (si, appearance="blush false", text="...")
        call process_character (k, appearance="blush false", text="[n.say_name], может быть прямо посередине.")
        call process_character (k, appearance="blush false", text="Он будет окружен сиськами!")
        call process_character (si, appearance="blush false", text="Да, идеально!")
        call process_character (si, appearance="blush false", text="Встань прямо перед [janet.say_name] и мной, милый.")

        $ quick_menu = False
        window hide
        show bg photo_epilogue_nate_np as nate_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True

        call process_character (n, appearance="blush false", text="Вот так?")
        call process_character (k, appearance="blush false", text="Бабушка, ты выглядишь такой стойкой!")
        call process_character (edna, appearance="blush false", text="Я, как правило, лучше смотрюсь на фотографиях, где моя улыбка подавлена.")
        call process_character (si, appearance="blush false", text="Хорошо, [sa.say_name] и [julia.say_name]...")
        call process_character (si, appearance="blush false", text="Было бы хорошо, если бы наши дочери были перед нами [janet.say_name], что ты думаешь?")
        call process_character (janet, appearance="blush false", text="Мне это нравится!")
        call process_character (edna, appearance="blush false", text="Почему бы [sa.say_name] и [julia.say_name] не прижаться к [n.say_name], возможно, они могут обнять его.")
        call process_character (edna, appearance="blush false", text="Это было бы очень мило.")
        call process_character (si, appearance="blush false", text="Звучит очаровательно!")

        $ quick_menu = False
        window hide
        show bg photo_epilogue_samjulia_np as julia_sam_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True

        call process_character (janet, appearance="blush false", text="Это редкость, чтобы [julia.say_name] была на переднем плане снимка.")
        call process_character (janet, appearance="blush false", text="Это может быть наш единственный шанс!")
        call process_character (julia, appearance="blush false", text="Эй, я не избегаю фотоаппаратов так сильно.")
        call process_character (julia, appearance="blush false", text="Хорошо, но...")
        call process_character (edna, appearance="blush false", text="Я тоже не люблю фотоаппараты, [julia.say_name], но это особый случай!")
        call process_character (si, appearance="blush false", text="Очень особенный случай!")
        call process_character (si, appearance="blush false", text="Я люблю фотографии всей семьи!")
        call process_character (janet, appearance="blush false", text="Обязательно улыбайтесь!")

        $ quick_menu = False
        window hide
        pause 0.5
        show camera:
            Solid("#ffffff", xsize = 1920, ysize = 1080)
            alpha 0.0
            linear .25 alpha 1.0
            pause .25
            linear .25 alpha 0.0

        pause 2
        window show
        $ quick_menu = True

        call process_character (gloryhole_girl, appearance="", text="...")
        call process_character (gloryhole_girl, appearance="", text="Снимок вышел отличным, ребята!")
        call process_character (vicky, appearance="", text="Я согласна, вы получились очень красиво на экране камеры.")
        call process_character (si, appearance="blush false", text="Теперь надо сфотографироваться с вами двумя!")
        call process_character (si, appearance="blush false", text="Вы проводите так много времени с [n.say_name] и нами, так что вы тоже практически семья!")
        call process_character (k, appearance="blush false", text="Мы одна большая, счастливая, ебучая семья!")
        call process_character (k, appearance="blush false", text="Акцент на ебучая!")
        call process_character (sa, appearance="blush false", text="Нажми кнопку на камере, [gloryhole_girl.say_name]!")
        call process_character (gloryhole_girl, appearance="", text="...")
        call process_character (gloryhole_girl, appearance="", text="Она мигает!")

        $ quick_menu = False
        window hide
        show bg photo_epilogue_kaceyvicky_np as nonrelated_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True

        call process_character (k, appearance="blush false", text="Мы действительно сбились в кучу!")
        call process_character (vicky, appearance="", text="Думаю, все будет хорошо.")
        call process_character (vicky, appearance="", text="Не то, чтобы мы будем распространять это фото.")
        call process_character (si, appearance="blush false", text="Ха-ха, нет, абсолютно нет!")
        call process_character (si, appearance="blush false", text="Это частное фото, только для нас!")
        call process_character (k, appearance="blush false", text="Эй, если бы это было где-то опубликовано, мы могли бы просто сказать, что мы семья нудистов.")
        call process_character (si, appearance="blush false", text="[k.say_name]...")
        call process_character (sa, appearance="blush false", text="Я сделаю снимок фоновым изображением на своем компьютере!")
        call process_character (gloryhole_girl, appearance="", text="Я могла бы сделать то же самое, [sa.say_name]!")
        call process_character (vicky, appearance="", text="Я думаю, мы должны периодически делать такие фотографии.")
        call process_character (vicky, appearance="", text="Было бы интересно посмотреть, насколько изменимся.")
        call process_character (edna, appearance="blush false", text="Ты имеешь в виду, как мы стареем, ха-ха!")
        call process_character (vicky, appearance="", text="Надеюсь, я буду стареть так же грациозно, как и ты, [edna.say_name].")
        call process_character (julia, appearance="blush false", text="Еще одно фото, и все будет хорошо?")
        call process_character (si, appearance="blush false", text="До тех пор, пока никто не чихнет или не закроет глаза в неподходящее время!")
        call process_character (k, appearance="blush false", text="Или решит бесконтрольно трясти сиськами!")
        call process_character (sa, appearance="blush false", text="Ха-ха!")
        call process_character (gloryhole_girl, appearance="", text="Эй [k.say_name], хочешь устроить битву сисек после этого?")
        call process_character (k, appearance="blush false", text="Ты в деле!")
        call process_character (k, appearance="blush false", text="И давайте сделаем это, пока член [n.say_name] будет между нами!")
        call process_character (n, appearance="blush false", text="Черт возьми, да!")
        call process_character (sa, appearance="blush false", text="Так, я снимаю!")
        call process_character (si, appearance="blush false", text="Постарайтесь сдерживать свое волнение еще немного!")
        call process_character (si, appearance="blush false", text="Как только фотография будет сделана, все вы можете сойти с ума!")
        call process_character (k, appearance="blush false", text="Все говорим \"Сперма\"!")

        "Все" "Сперма!"

        $ quick_menu = False
        window hide
        pause 0.5
        show camera:
            Solid("#ffffff", xsize = 1920, ysize = 1080)
            alpha 0.0
            linear .25 alpha 1.0
            pause .25
            linear .25 alpha 0.0

        pause 2
        window show
        $ quick_menu = True

        call process_character (n, appearance="blush false", text="(Это лето будет трудно превзойти)")
        call process_character (n, appearance="blush false", text="(Придется целый год ждать следующего)")
        call process_character (n, appearance="blush false", text="(Надеюсь, оно будет так же хорошо, или даже лучше!)")
        call process_character (n, appearance="blush false", text="(Но сначала мне нужно снова пройти школу...)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Может быть, все будет не так уж плохо .)")
        call process_character (n, appearance="blush false", text="(Там я и [sa.say_name] может быть познакомимся с крутыми одноклассниками, чтобы тусоваться)")
        call process_character (n, appearance="blush false", text="(Интересно, какими будут учительницы в школе...)")
        call process_character (n, appearance="blush false", text="(Надеюсь, у одной из них большие сиськи!)")
        call process_character (k, appearance="blush false", text="Йоу, [n.say_name]!")
        call process_character (k, appearance="blush false", text="Давай приготовим твой член к этой разборке сисек!")
        call process_character (gloryhole_girl, appearance="", text="Я могу вылизать его своим языком для тебя!")
        call process_character (n, appearance="blush false", text="Хорошо, давайте начнем!")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(По крайней мере, я знаю, что мне будет весело после школы!)")
    else:

        call process_character (janet, appearance="pose handhips face neutral blush false", text="Так, таймер камеры установлен на тридцать секунд.")
        call process_character (janet, appearance="pose handhips face curious blush false", text="Вообще-то, давай на шестьдесят.")
        call process_character (janet, appearance="pose handhips face neutral blush false", text="Мы, скорее всего, будем меняться местами, чтобы сделать хороший портрет.")
        call process_character (gloryhole_girl, appearance="", text="Камера достаточно далеко, чтобы заснять нас всех?")
        call process_character (vicky, appearance="", text="Если нам придется теснее прижиматься, так тому и быть.")
        call process_character (k, appearance="pose armsup face neutral blush false", text="Мы можем закончить тем, что наши сиськи будут прижаты друг к другу.")
        call process_character (k, appearance="pose armsup face happy blush false", text="[n.say_name] одобрил бы!")
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (janet, appearance="pose handface face happy blush false", text="Хорошо, фотоаппарат отсчитывает время!")
        call process_character (si, appearance="pose handsfront face embarrassed blush false", text="О Господи, давайте занимать места!")
        call process_character (si, appearance="pose handsfront face embarrassed blush false", text="Скорей, скорей!")

        $ no_bust_art = True
        $ clear_characters()
        show bg photo_epilogue_background
        show family_milf_layer:
            Null()
        show nate_layer:
            Null()
        show julia_sam_layer:
            Null()
        show nonrelated_layer:
            Null()
        with Dissolve(0.5)

        call process_character (si, appearance="blush false", text="Ладно, давайте посмотрим...")
        call process_character (si, appearance="blush false", text="Мам, встань вон там.")
        call process_character (si, appearance="blush false", text="[janet.say_name], ты хочешь быть рядом с Мамой?")
        call process_character (janet, appearance="blush false", text="Конечно!")
        call process_character (si, appearance="blush false", text="А я буду стоять напротив тебя.")
        call process_character (si, appearance="blush false", text="[k.say_name], ты самая высокая, поэтому ты должна быть сзади.")
        call process_character (k, appearance="blush false", text="Буду рядом с тобой, Мама.")

        $ play_music("audio/music/Smooth 01.ogg", fadeout=1)

        $ quick_menu = False
        window hide
        show bg photo_epilogue_ednajanetkirasimone_np as family_milf_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True

        call process_character (janet, appearance="blush false", text="Можешь проверить, все ли мы в кадре [vicky.say_name]?")
        call process_character (vicky, appearance="", text="...")
        call process_character (vicky, appearance="", text="Вы молодцы!")
        call process_character (si, appearance="blush false", text="Теперь что касается тебя, [n.say_name], можешь ли ты...")
        call process_character (si, appearance="blush false", text="[n.say_name], хватит тянуть [gloryhole_girl.say_name] за соски.")
        call process_character (si, appearance="blush false", text="Ты нужен нам здесь.")
        call process_character (n, appearance="blush false", text="О, да!")
        call process_character (si, appearance="blush false", text="Почему бы тебе не пойти...")
        call process_character (si, appearance="blush false", text="...")
        call process_character (k, appearance="blush false", text="[n.say_name], может быть прямо посередине.")
        call process_character (k, appearance="blush false", text="Он будет окружен сиськами!")
        call process_character (si, appearance="blush false", text="Да, идеально!")
        call process_character (si, appearance="blush false", text="Встань прямо перед [janet.say_name] и мной, милый.")

        $ quick_menu = False
        window hide
        show bg photo_epilogue_nate_np as nate_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True

        call process_character (n, appearance="blush false", text="Вот так?")
        call process_character (k, appearance="blush false", text="Бабушка, ты выглядишь такой стойкой!")
        call process_character (edna, appearance="blush false", text="Я, как правило, лучше смотрюсь на фотографиях, где моя улыбка подавлена.")
        call process_character (janet, appearance="blush false", text="Это редкий подвиг для всех нас, встать перед камерой!")
        call process_character (edna, appearance="blush false", text="Это особый случай.")
        call process_character (si, appearance="blush false", text="Очень особенный случай!")
        call process_character (si, appearance="blush false", text="Обожаю семейные фотографии!")
        call process_character (janet, appearance="blush false", text="Обязательно улыбайтесь!")

        $ quick_menu = False
        window hide
        pause 0.5
        show camera:
            Solid("#ffffff", xsize = 1920, ysize = 1080)
            alpha 0.0
            linear .25 alpha 1.0
            pause .25
            linear .25 alpha 0.0

        pause 2
        window show
        $ quick_menu = True

        call process_character (gloryhole_girl, appearance="", text="...")
        call process_character (gloryhole_girl, appearance="", text="Снимок вышел отличным, ребята!")
        call process_character (vicky, appearance="", text="Я согласна, вы получились очень красиво на экране камеры.")
        call process_character (si, appearance="blush false", text="Теперь надо сфотографироваться с вами двумя!")
        call process_character (si, appearance="blush false", text="Вы проводите так много времени с [n.say_name] и нами, так что вы тоже практически семья!")
        call process_character (k, appearance="blush false", text="Мы одна большая, счастливая, ебучая семья!")
        call process_character (k, appearance="blush false", text="Акцент на ебучая!")
        call process_character (janet, appearance="blush false", text="Можешь ли ты нажать кнопку на камере, [gloryhole_girl.say_name]?")
        call process_character (gloryhole_girl, appearance="", text="...")
        call process_character (gloryhole_girl, appearance="", text="Она мигает!")

        $ quick_menu = False
        window hide
        show bg photo_epilogue_kaceyvicky_np as nonrelated_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True

        call process_character (k, appearance="blush false", text="Мы действительно сбились в кучу!")
        call process_character (vicky, appearance="", text="Думаю, все будет хорошо.")
        call process_character (vicky, appearance="", text="Не то, чтобы мы будем распространять это фото.")
        call process_character (si, appearance="blush false", text="Ха-ха, нет, абсолютно нет!")
        call process_character (si, appearance="blush false", text="Это частное фото, только для нас!")
        call process_character (k, appearance="blush false", text="Эй, если бы это было где-то опубликовано, мы могли бы просто сказать, что мы семья нудистов.")
        call process_character (si, appearance="blush false", text="[k.say_name]...")
        call process_character (gloryhole_girl, appearance="", text="Я могла бы сделать это изображение фоном рабочего стола на моем компьютере!")
        call process_character (vicky, appearance="", text="Я думаю, мы должны периодически делать такие фотографии.")
        call process_character (vicky, appearance="", text="Было бы интересно посмотреть, насколько мы изменимся.")
        call process_character (edna, appearance="blush false", text="Ты имеешь в виду, как мы состаримся, ха-ха!")
        call process_character (vicky, appearance="", text="Надеюсь, я буду стареть так же грациозно, как и ты, [edna.say_name].")
        call process_character (janet, appearance="blush false", text="Еще одно фото, и все будет хорошо!")
        call process_character (si, appearance="blush false", text="До тех пор, пока никто не чихнет или не закроет глаза в неподходящее время!")
        call process_character (k, appearance="blush false", text="Или решит бесконтрольно трясти сиськами!")
        call process_character (gloryhole_girl, appearance="", text="Ха-ха!")
        call process_character (gloryhole_girl, appearance="", text="Эй [k.say_name], хочешь устроить битву сисек после этого?")
        call process_character (k, appearance="blush false", text="Ты в деле!")
        call process_character (k, appearance="blush false", text="И давайте сделаем это, пока член [n.say_name] будет между нами!")
        call process_character (n, appearance="blush false", text="Черт возьми, да!")
        call process_character (si, appearance="blush false", text="Постарайтесь сдерживать свое волнение еще немного!")
        call process_character (si, appearance="blush false", text="Как только фотография будет сделана, все вы можете сойти с ума!")
        call process_character (k, appearance="blush false", text="Все говорим \"Сперма\"!")

        "Все" "Сперма!"

        $ quick_menu = False
        window hide
        pause 0.5
        show camera:
            Solid("#ffffff", xsize = 1920, ysize = 1080)
            alpha 0.0
            linear .25 alpha 1.0
            pause .25
            linear .25 alpha 0.0

        pause 2
        window show
        $ quick_menu = True


        call process_character (n, appearance="blush false", text="(Это лето будет трудно превзойти)")
        call process_character (n, appearance="blush false", text="(Придется целый год ждать следующего)")
        call process_character (n, appearance="blush false", text="(Надеюсь, оно будет так же хорошо, или даже лучше!)")
        call process_character (n, appearance="blush false", text="(Но сначала мне нужно снова пройти школу...)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Может быть, все будет не так уж плохо .)")
        call process_character (n, appearance="blush false", text="(Там я и [sa.say_name] может быть познакомимся с крутыми одноклассниками, чтобы тусоваться)")
        call process_character (n, appearance="blush false", text="(Интересно, какими будут учительницы в школе)")
        call process_character (n, appearance="blush false", text="(Надеюсь, у одной из них большие сиськи!)")
        call process_character (k, appearance="blush false", text="Йоу, [n.say_name]!")
        call process_character (k, appearance="blush false", text="Давай приготовим твой член к этой разборке сисек!")
        call process_character (gloryhole_girl, appearance="", text="Я могу вылизать его своим языком для тебя!")
        call process_character (n, appearance="blush false", text="Хорошо, давайте начнем!")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(По крайней мере, я знаю, что мне будет весело после школы!)")


    menu:
        "{i}Все забеременели от меня!{/i}":
            jump epilogue_pregnancy
        "{i}Это было лучшее лето в моей жизни!{/i}":
            jump epilogue_end

    return

label epilogue_pregnancy:
    $ epilogue_pregnancy_completed = True
    hide family_milf_layer
    hide nate_layer
    hide julia_sam_layer
    hide nonrelated_layer
    $ stop_music(fadeout=1)
    call fade_to_black (2)

    "{i}Несколько месяцев спустя...{/i}"

    window hide
    pause 1

    $ play_music("audio/music/Daily_Music_03.ogg", fadeout=1)

    window show
    call process_character (n, appearance="blush false", text="(Да, начало весенних каникул!)")
    call process_character (n, appearance="blush false", text="(Как я рад, что они настали!)")
    call process_character (n, appearance="blush false", text="(Еще не достаточно тепло, чтобы воспользоваться бассейном, вот облом)")
    call process_character (n, appearance="blush false", text="(Ну ладно)")
    call process_character (n, appearance="blush false", text="(Есть еще много других вещей, которые я могу сделать, чтобы занять себя...)")


    call static_still_ctc ("bg kira_epilogue_01")

    call process_character (n, appearance="blush false", text="Эй, что случилось, [k.say_name]?")
    call process_character (k, appearance="blush false", text="Хех, тебе меня не одурачить, [n.say_name].")
    call process_character (n, appearance="blush false", text="Что ты имеешь в виду?")
    call process_character (k, appearance="blush false", text="Ты не будешь ко мне подлизываться, если не хочешь чего-то определенного.")
    call process_character (n, appearance="blush false", text="Ну, сейчас дома только ты.")
    call process_character (n, appearance="blush false", text="Я подумал, что мы могли бы провести некоторое время вместе.")
    call process_character (k, appearance="blush false", text="Ты сейчас очень повседневно к этому относишься, не так ли?")
    call process_character (n, appearance="blush false", text="Только потому, что я учился у мастера повседневного секса.")
    call process_character (k, appearance="blush false", text="Ха, ты чертовски прав!")

    call process_character (n, appearance="blush false", text="{i}Я рад, что все осталось таким же, каким было летом.{/i}")
    call process_character (n, appearance="blush false", text="{i}Каждый день я сыт по горло многочисленными трахами.{/i}")
    call process_character (n, appearance="blush false", text="{i}Для меня стало второй натурой доставать член всякий раз, когда я возбужден.{/i}")
    call process_character (n, appearance="blush false", text="{i}Если тетя [janet.say_name], Бабушка, или кто-нибудь приходит в гости, мы трахаемся прямо в дверях в качестве приветствия.{/i}")
    call process_character (n, appearance="blush false", text="{i}А семейные сборища во время праздников всегда превращаются в оргию.{/i}")
    call process_character (n, appearance="blush false", text="{i}Становится очень грязно.{/i}")

    $ play_music("audio/music/Funking the Streets.ogg", fadeout=1)

    call static_still_ctc ("bg kira_epilogue_02")

    call process_character (k, appearance="blush false", text="Ах да, [n.say_name], соси мои сиськи!")
    call process_character (n, appearance="blush false", text="Ммф...")
    call process_character (n, appearance="blush false", text="Твоя киска уже мокрая.")
    call process_character (k, appearance="blush false", text="Ну с двумя пальцами в киске этого не трудно добиться!")
    call process_character (n, appearance="blush false", text="Может быть, тогда я смогу вместить три или четыре!")
    call process_character (k, appearance="blush false", text="Оох, черт!")

    call process_character (n, appearance="blush false", text="{i}Несмотря на то, насколько большим стал ее живот, [k.say_name] по-прежнему работает каждый день.{/i}")
    call process_character (n, appearance="blush false", text="{i}Некоторые упражнения сейчас для нее невозможны, но бег трусцой и тяжелая атлетика все еще обычное дело.{/i}")
    call process_character (n, appearance="blush false", text="{i}[k.say_name] всегда шутит, что я виноват в этом, но все это просто шутки.{/i}")
    call process_character (n, appearance="blush false", text="{i}И к счастью, мы все еще можем трахаться, так чтобы мозги сносило!{/i}")

    call static_still_ctc ("bg kira_epilogue_03")

    call process_character (k, appearance="blush false", text="Засунь туда свой член, [n.say_name], да!")
    call process_character (n, appearance="blush false", text="Ах, ах!")
    call process_character (n, appearance="blush false", text="Я продвигаюсь так далеко, как могу!")
    call process_character (k, appearance="blush false", text="Жестче, [n.say_name], жестче!")
    call process_character (n, appearance="blush false", text="Хе-хе, вот где все началось для нас.")
    call process_character (n, appearance="blush false", text="Я сидел на том диване, а ты наклонялась, делая приседания.")
    call process_character (k, appearance="blush false", text="Срань господня, кажется, это было сто лет назад!")
    call process_character (k, appearance="blush false", text="Да, я помню тот день.")
    call process_character (k, appearance="blush false", text="Когда я увидела, как ты украдкой заглядываешь на мою задницу, я была удивлена.")
    call process_character (k, appearance="blush false", text="Честно говоря, тогда я не думала, что ты такой уж извращенец.")
    call process_character (n, appearance="blush false", text="Я не знала, что ты такой извращенец!")
    call process_character (n, appearance="blush false", text="Ты вошла в мою комнату и заставила меня пялиться на твою задницу!")
    call process_character (k, appearance="blush false", text="Эй, разберись в фактах!")
    call process_character (k, appearance="blush false", text="Я пришла, чтобы одолжить твой ноутбук.")
    call process_character (k, appearance="blush false", text="Затем ты начал пялиться на мои стринги, пока я пыталась достать адаптер питания твоего ноутбука!")
    call process_character (n, appearance="blush false", text="Оох, да!")
    call process_character (n, appearance="blush false", text="Эй, я не мог перестать смотреть на твою задницу!")
    call process_character (k, appearance="blush false", text="Ты все еще не можешь!")
    call process_character (k, appearance="blush false", text="То же самое касается и моих сисек!")

    call process_character (n, appearance="blush false", text="{i}Я запомнил все чувствительные места [k.say_name].{/i}")
    call process_character (n, appearance="blush false", text="{i}Для нее сейчас не редкость множественные оргазмы.{/i}")

    call static_still_ctc ("bg kira_epilogue_04a")

    call process_character (n, appearance="blush false", text="{i}За последние несколько месяцев я многому научился, но знаю, что еще многому могу научиться.{/i}")

    call process_character (k, appearance="blush false", text="Да, просверли мою киску своим членом, [n.say_name]!")
    call process_character (n, appearance="blush false", text="С радостью!")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (n, appearance="blush false", text="...")


    if finale_scene_completed_with_julia_sam:
        call process_character (sa, appearance="blush false", text="Мы дооома!")
        call process_character (si, appearance="blush false", text="Ничего себе, сколько всего мы купили в продуктовом магазине!")
        call process_character (si, appearance="blush false", text="Такое чувство, что мы выкупили весь магазин!")
        call process_character (sa, appearance="blush false", text="Мы почти поместили все сумки в багажник машины!")
        call process_character (si, appearance="blush false", text="[sa.say_name], можешь позвать [k.say_name] и [n.say_name].")
        call process_character (si, appearance="blush false", text="Нам нужно, чтобы они помогли принести всю эту еду.")
        call process_character (sa, appearance="blush false", text="[n.say_name], [k.say_name]!")
        call process_character (sa, appearance="blush false", text="Мы нуждаемся в вас, чтобы помочь...")
        call process_character (sa, appearance="blush false", text="Ооу, блин!")
        call process_character (sa, appearance="blush false", text="Вы трахаетесь без меня?!")
        call process_character (si, appearance="blush false", text="Что такое, дорогая?")
        call process_character (sa, appearance="blush false", text="[k.say_name] и [n.say_name] сцепились в гостиной.")
        call process_character (si, appearance="blush false", text="Ты не могла подождать, пока мы не вернемся, [k.say_name]?")
        call process_character (k, appearance="blush false", text="Эй, не вини меня!")
        call process_character (k, appearance="blush false", text="[n.say_name] был тот, кто начал это!")
        call process_character (si, appearance="blush false", text="Ммм, вот как?")
        call process_character (k, appearance="blush false", text="Я серьезно!")
        call process_character (k, appearance="blush false", text="Ах...")
        call process_character (n, appearance="blush false", text="Это правда, Мама.")
        call process_character (n, appearance="blush false", text="Я был очень, очень возбужден.")
        call process_character (k, appearance="blush false", text="Ты бы видела, что он сделал, Мама.")
        call process_character (k, appearance="blush false", text="Он буквально залез мне в штаны и начал меня лапать!")
        call process_character (sa, appearance="blush false", text="Ха-ха, круто!")
        call process_character (sa, appearance="blush false", text="[n.say_name] делает это и со мной!")
        call process_character (sa, appearance="blush false", text="Он также проводит скрытную атаку, когда тянет вниз мои штаны и пихает член в мою задницу!")
        call process_character (sa, appearance="blush false", text="Но я ему мщу, понимаешь [n.say_name]?")
        call process_character (n, appearance="blush false", text="Да.")
        call process_character (n, appearance="blush false", text="Я всегда попадаюсь на твои внезапные и быстрые ласки.")
        call process_character (sa, appearance="blush false", text="Уловка и ярость, так я это называю!")
        call process_character (si, appearance="blush false", text="Ох уж, вы и ваши сумасшедшие сексуальные игры!")
        call process_character (k, appearance="blush false", text="Повторяю, я не была зачинщиком нашего трахфеста!")
        call process_character (k, appearance="blush false", text="В данном случае я невиновна!")
        call process_character (si, appearance="blush false", text="Ну, после того, как вы закончите, заберите продукты из машины и принесите их.")
        call process_character (si, appearance="blush false", text="Многие из них скоропортящиеся, так что не задерживайтесь!")
        call process_character (n, appearance="blush false", text="Мы почти закончили.")
        call process_character (n, appearance="blush false", text="Вообще-то, я как раз собирался сказать [k.say_name], что я...")
        call process_character (n, appearance="blush false", text="Ох!")
        call process_character (n, appearance="blush false", text="Вот так!")
        call process_character (n, appearance="blush false", text="Пора расколоть орех!")

        if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

        call static_still_ctc ("bg kira_epilogue_04b")

        call process_character (n, appearance="blush false", text="Гааах!")
        call process_character (n, appearance="blush false", text="Мм-Мм!")
        call process_character (sa, appearance="blush false", text="Ох, он взрывается!")
        call process_character (n, appearance="blush false", text="Вууу...")
        call process_character (n, appearance="blush false", text="Мне нужен был этот трах!")
        call process_character (k, appearance="blush false", text="Ты говоришь это каждый день!")
        call process_character (sa, appearance="blush false", text="Да, конечно!")
        call process_character (n, appearance="blush false", text="Я просто говорю честно.")
        call process_character (k, appearance="blush false", text="Честно говоря, мне это тоже было нужно.")
        call process_character (k, appearance="blush false", text="Мой день становился немного скучным.")
        call process_character (sa, appearance="blush false", text="Я хочу потрахаться позже, [n.say_name]!")
        call process_character (sa, appearance="blush false", text="Я следующая!")

        call static_still_ctc ("bg kira_epilogue_04c")

        call process_character (sa, appearance="blush false", text="Вуууа!")
        call process_character (sa, appearance="blush false", text="Мам, ты должна увидеть, сколько спермы [n.say_name] закачивает в киску [k.say_name]!")
        call process_character (si, appearance="blush false", text="Я уверена, что много.")
        call process_character (sa, appearance="blush false", text="Это еще мягко сказано!")
        call process_character (sa, appearance="blush false", text="Киска [k.say_name] даже не может сдержать все!")
        call process_character (si, appearance="blush false", text="Постарайтесь, чтобы сперма не попала на ковер, я пару часов чистила его вчера!")
        call process_character (k, appearance="blush false", text="С учетом того, сколько спермы [n.say_name] летает по нашему дому, чистые ковры кажутся проигранной битвой.")
        call process_character (sa, appearance="blush false", text="[n.say_name] на днях кончил так, что попал в стену?")
        call process_character (si, appearance="blush false", text="Как это могло случиться?")
        call process_character (k, appearance="blush false", text="Он должен был кончить мне в рот, но я недооценила угол.")
        call process_character (k, appearance="blush false", text="Его сперма пальнула и просвистела над моей головой!")
        call process_character (si, appearance="blush false", text="Надеюсь, ты прибралась.")
        call process_character (k, appearance="blush false", text="[sa.say_name] и я, конечно, прибрались!")
        call process_character (k, appearance="blush false", text="Мы вылизали языком!")
        call process_character (sa, appearance="blush false", text="Я ни за что не позволю, что ореховое масло [n.say_name] пропало впустую!")
    else:

        call process_character (si, appearance="blush false", text="Я дома!")
        call process_character (si, appearance="blush false", text="Ничего себе, сколько всего купила в продуктовом магазине!")
        call process_character (si, appearance="blush false", text="Такое чувство, что я выкупила весь магазин!")
        call process_character (n, appearance="blush false", text="Привет Мама, ах, ах...")
        call process_character (si, appearance="blush false", text="Привет милый.")
        call process_character (si, appearance="blush false", text="[k.say_name] в гостиной с тобой?")
        call process_character (k, appearance="blush false", text="Да, конечно...{w=1.0}!")
        call process_character (si, appearance="blush false", text="Помогите мне все принести.")
        call process_character (si, appearance="blush false", text="Машина до краев забита мешками с едой!")
        call process_character (n, appearance="blush false", text="Можешь дать нам, ах...{w=1.0}несколько минут?")
        call process_character (si, appearance="blush false", text="Что вы...{w=1.0}ох, конечно.")
        call process_character (si, appearance="blush false", text="Я должна была догадаться, что вы двое это сделаете.")
        call process_character (si, appearance="blush false", text="Ты не могла подождать, пока я не вернусь, [k.say_name]?")
        call process_character (k, appearance="blush false", text="Эй, не вини меня!")
        call process_character (k, appearance="blush false", text="[n.say_name] был тот, кто начал это!")
        call process_character (si, appearance="blush false", text="Ммм, вот как?")
        call process_character (k, appearance="blush false", text="Я серьезно!")
        call process_character (k, appearance="blush false", text="Ах...")
        call process_character (n, appearance="blush false", text="Это правда, Мама.")
        call process_character (n, appearance="blush false", text="Я был очень, очень возбужден.")
        call process_character (k, appearance="blush false", text="[n.say_name] буквально стягивает с меня штаны, и начинает ласкать пальцами меня!")
        call process_character (si, appearance="blush false", text="О да, я знаю, о чем ты говоришь.")
        call process_character (si, appearance="blush false", text="[n.say_name] любит делать это, когда я пытаюсь приготовить ужин.")
        call process_character (n, appearance="blush false", text="Или я хватаю тебя за сиськи!")
        call process_character (k, appearance="blush false", text="Ты так жонглируешь маминой грудью, что можешь стать придворным шутом!")
        call process_character (si, appearance="blush false", text="Ха-ха!")
        call process_character (si, appearance="blush false", text="[n.say_name] любит заниматься своими маленькими сексуальными играми с нами!")
        call process_character (k, appearance="blush false", text="Повторяю, я не была зачинщиком нашего трахфеста!")
        call process_character (k, appearance="blush false", text="В данном случае я невиновна!")
        call process_character (si, appearance="blush false", text="Ну после того как вы закончите, пожалуйста, заберите продукты из машины.")
        call process_character (si, appearance="blush false", text="Многие из них скоропортящиеся, так что не задерживайтесь!")
        call process_character (n, appearance="blush false", text="Мы почти закончили.")
        call process_character (n, appearance="blush false", text="Вообще-то, я как раз собирался сказать [k.say_name], что я...")
        call process_character (n, appearance="blush false", text="Ох!")
        call process_character (n, appearance="blush false", text="Вот так!")
        call process_character (n, appearance="blush false", text="Пора расколоть орех!")

        if persistent.enable_sex_sounds:
            $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

        call static_still_ctc ("bg kira_epilogue_04b")

        call process_character (n, appearance="blush false", text="Гааах!")
        call process_character (n, appearance="blush false", text="Мм-Мм!")
        call process_character (si, appearance="blush false", text="Я слышу, как [n.say_name] пыхтит.")
        call process_character (si, appearance="blush false", text="Ты только что кончил, милая?")
        call process_character (n, appearance="blush false", text="Ооох, да.")
        call process_character (n, appearance="blush false", text="Мне нужен был этот трах.")
        call process_character (k, appearance="blush false", text="Ты говоришь это каждый день!")
        call process_character (n, appearance="blush false", text="Я просто говорю честно.")
        call process_character (k, appearance="blush false", text="Честно говоря, мне это тоже было нужно.")
        call process_character (k, appearance="blush false", text="Мой день становился немного скучным.")

        call static_still_ctc ("bg kira_epilogue_04c")

        call process_character (k, appearance="blush false", text="Чееерт!")
        call process_character (k, appearance="blush false", text="Мам, ты должна увидеть, сколько спермы [n.say_name] закачивает в мою киску!")
        call process_character (si, appearance="blush false", text="Я уверена, что много.")
        call process_character (k, appearance="blush false", text="Моя киска даже не может вместить все!")
        call process_character (k, appearance="blush false", text="Она начинает вытекать!")
        call process_character (si, appearance="blush false", text="Постарайтесь, чтобы сперма не попала на ковер, я пару часов чистила его вчера!")
        call process_character (k, appearance="blush false", text="С учетом того, сколько спермы [n.say_name] летает по нашему дому, чистые ковры кажутся проигранной битвой.")
        call process_character (k, appearance="blush false", text="Только на днях, [n.say_name] выстрелил так, что попал в стену.")
        call process_character (si, appearance="blush false", text="Как это могло случиться?")
        call process_character (k, appearance="blush false", text="Он должен был кончить мне в рот, но я недооценила угол.")
        call process_character (k, appearance="blush false", text="Его сперма пальнула и просвистела над моей головой!")
        call process_character (si, appearance="blush false", text="Надеюсь, ты прибралась.")
        call process_character (k, appearance="blush false", text="Я сделала это...{w=1.0}моим языком!")
        call process_character (n, appearance="blush false", text="[k.say_name] убедилась, что моя сперма не пропала зря!")
        call process_character (si, appearance="blush false", text="Постарайся, чтобы член [n.say_name] был ближе ко рту в следующий раз, [k.say_name].")

    call fade_to_black (1)
    call process_character (n, appearance="blush false", text="{i}Да, это просто еще один обычный день.{/i}")
    call process_character (n, appearance="blush false", text="{i}Хотя, по большинству стандартов, мои дни далеки от обычных.{/i}")
    call process_character (n, appearance="blush false", text="{i}Мне очень повезло, что в моей жизни столько замечательных девушек.{/i}")

    $ no_bust_art = True
    $ clear_characters()
    show bg photo_epilogue_background
    show family_milf_layer:
        Null()
    show nate_layer:
        Null()
    show julia_sam_layer:
        Null()
    show nonrelated_layer:
        Null()
    with Dissolve(0.5)

    call process_character (n, appearance="blush false", text="{i}Теперь, когда я думаю об этом, все мы сильно изменились с прошлого лета!{/i}")
    call process_character (n, appearance="blush false", text="{i}Смогу ли я вспомнить все...{/i}")

    $ play_music("audio/music/Resort Loop2.ogg", fadeout=1)

    $ quick_menu = False
    window hide
    show bg photo_epilogue_ednajanetkirasimone_p as family_milf_layer
    with Dissolve(0.5)
    pause
    window show
    $ quick_menu = True

    call process_character (n, appearance="blush false", text="{i}[k.say_name] согласилась на предложение [vicky.say_name] сниматься в порно видео со мной, но она все еще работает неполный рабочий день в фитнес-центре.{/i}")
    call process_character (n, appearance="blush false", text="{i}Она говорит, что хочет, чтобы однажды я встретился со всеми ее коллегами.{/i}")
    call process_character (n, appearance="blush false", text="{i}По-видимому, все они по какой-то причине хотят меня видеть...{/i}")
    call process_character (n, appearance="blush false", text="{i}...{/i}")
    call process_character (n, appearance="blush false", text="{i}Мама начала блог о садоводстве с помощью [sa.say_name], и он набирает популярность.{/i}")
    call process_character (n, appearance="blush false", text="{i}Она также получила повышение зарплаты от [vicky.say_name] из-за постоянного увеличения доходов Эмпориума!{/i}")
    call process_character (n, appearance="blush false", text="{i}...{/i}")
    call process_character (n, appearance="blush false", text="{i}Тетя [janet.say_name] предоставляет частные уроки йоги.{/i}")
    call process_character (n, appearance="blush false", text="{i}Она была удивлена, как много людей хотят сделать это обнаженными!{/i}")
    call process_character (n, appearance="blush false", text="{i}Иногда она зовет меня, когда думает, что мне понравится смотреть, как девушки занимаются йогой на улице.{/i}")
    call process_character (n, appearance="blush false", text="{i}...{/i}")
    call process_character (n, appearance="blush false", text="{i}Бабушка наслаждается новым казино в своем кондоминиуме.{/i}")
    call process_character (n, appearance="blush false", text="{i}Я слышал, что ей везет с автоматами!{/i}")
    call process_character (n, appearance="blush false", text="{i}Кроме того, она заручилась поддержкой жителей для строительства пляжного бассейна с гидромассажными ваннами.{/i}")
    call process_character (n, appearance="blush false", text="{i}Я не могу дождаться, когда оно завершится!{/i}")

    $ quick_menu = False
    window hide
    show bg photo_epilogue_kaceyvicky_p as nonrelated_layer
    with Dissolve(0.5)
    pause
    window show
    $ quick_menu = True

    call process_character (n, appearance="blush false", text="{i}[gloryhole_girl.say_name] подала заявку на должность помощника учителя в моей школе!{/i}")
    call process_character (n, appearance="blush false", text="{i}Когда мой учитель начальной школы отсутствует, [gloryhole_girl.say_name] заменяет его.{/i}")
    call process_character (n, appearance="blush false", text="{i}Это потрясающе иметь возможность видеть ее, и она хороший инструктор.{/i}")
    call process_character (n, appearance="blush false", text="{i}Я думаю, она учится, чтобы получить официальную степень преподавателя.{/i}")
    call process_character (n, appearance="blush false", text="{i}...{/i}")
    call process_character (n, appearance="blush false", text="{i}Бизнес [vicky.say_name] процветает!{/i}")
    call process_character (n, appearance="blush false", text="{i}Ее сайт уже входит в десятку лучших порно компаний!{/i}")
    call process_character (n, appearance="blush false", text="{i}Она планирует нанять больше актрис для работы со мной в ближайшее время.{/i}")
    call process_character (n, appearance="blush false", text="{i}Я не могу дождаться!{/i}")

    if finale_scene_completed_with_julia_sam:
        $ quick_menu = False
        window hide
        show bg photo_epilogue_nate_p as nate_layer
        show bg photo_epilogue_samjulia_p as julia_sam_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True

        call process_character (n, appearance="", text="{i}[julia.say_name] хочет написать и опубликовать свой первый фантастический роман!{/i}")
        call process_character (n, appearance="", text="{i}Она решила, что пришло время представить ее художественную работу, и я думаю, что это было отличное решение!{/i}")
        call process_character (n, appearance="", text="{i}Я даже помог ей назвать некоторых персонажей ее книги.{/i}")
        call process_character (n, appearance="", text="{i}Из того, что я прочитал, история чертовски удивительна!{/i}")
        call process_character (n, appearance="", text="...")
        call process_character (n, appearance="", text="{i}[sa.say_name] и я сделали Твинстикс одним из лучших каналов на ReflexViz.HD!{/i}")
        call process_character (n, appearance="", text="{i}Он вырос настолько, что теперь мы продаем мерч нашим поклонникам!{/i}")
        call process_character (n, appearance="", text="{i}У нас есть футболки, шляпы, брелки и даже мышеловки!{/i}")
        call process_character (n, appearance="", text="{i}Разработчики игр постоянно присылают нам игры по почте.{/i}")
        call process_character (n, appearance="", text="{i}Мы получаем ранний доступ ко всем последним играм, и это самое замечательное!{/i}")
    else:
        $ quick_menu = False
        window hide
        show bg photo_epilogue_nate_p as nate_layer
        with Dissolve(0.5)
        pause
        window show
        $ quick_menu = True

    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="{i}Так много произошло.{/i}")
    call process_character (n, appearance="blush false", text="{i}И мы не будем замедляться в ближайшее время!{/i}")
    call process_character (n, appearance="blush false", text="{i}Ах да, чуть не забыл...{/i}")
    call process_character (n, appearance="blush false", text="{i}Этим летом размер нашей семьи резко увеличится!{/i}")

    jump epilogue_end

    return

label epilogue_end:
    $ epilogue_completed = True

    window hide
    $ quick_menu = False
    with Dissolve(0.5)
    pause 0.5
    show epilogue_thanks as thanks
    with Dissolve(0.5)

    pause

    window hide
    $ quick_menu = False
    hide thanks
    show bg black as black
    with Dissolve(0.5)
    hide family_milf_layer
    hide nate_layer
    hide julia_sam_layer
    hide nonrelated_layer

    pause 0.5

    $ replace_position = False

    $ nate_room.start()

    return