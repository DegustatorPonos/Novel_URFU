init python:
    def edna_titfuck_set_speed(label, is_revisit, dream = False):
        renpy.call(label, is_revisit, dream = dream)
        
        return
    def edna_fucked_vaginally():
        if "finale_scene" in store.scenes_completed or store.edna_finale_vaginal_chosen:
            return True
        return False

image edna_titfuck_bikini_anim:
    "edna_titfuck_anim_0"
    pause 0.11
    "edna_titfuck_anim_1"
    pause 0.11
    "edna_titfuck_anim_2"
    pause 0.11
    "edna_titfuck_anim_3"
    pause 0.11
    "edna_titfuck_anim_4"
    pause 0.11
    "edna_titfuck_anim_5"
    pause 0.11
    "edna_titfuck_anim_6"
    pause 0.11
    "edna_titfuck_anim_7"
    pause 0.11
    "edna_titfuck_anim_8"
    pause 0.11
    repeat

image edna_titfuck_nude_anim:
    "edna_titfuck_nude_anim_0"
    pause 0.11
    "edna_titfuck_nude_anim_1"
    pause 0.11
    "edna_titfuck_nude_anim_2"
    pause 0.11
    "edna_titfuck_nude_anim_3"
    pause 0.11
    "edna_titfuck_nude_anim_4"
    pause 0.11
    "edna_titfuck_nude_anim_5"
    pause 0.11
    "edna_titfuck_nude_anim_6"
    pause 0.11
    "edna_titfuck_nude_anim_7"
    pause 0.11
    "edna_titfuck_nude_anim_8"
    pause 0.11
    repeat


label edna_scene_intro_2(dream=False):
    call edna_scene_intro_2_sex (dream)
    return

label edna_scene_intro_2_sex(dream=False):

    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Я хотел бы пойти посмотреть, что бабушка делает сегодня!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="У меня с собой пропуск, так что я смогу пройти!")

    call process_scene_beginning (bg="bg edna_house_daytime", char_tuple_array=[ (n, "outfit clothesjacket pose handpocket"), (edna, "outfit clothes pose handhip face happy blush false mouth red") ], dream=dream )

    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="[n.say_name]!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Какой приятный сюрприз!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Привет, Бабушка!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Я хотел увидеться с тобой.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Ты пришел сюда один?")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Да.")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Сюда было легко добраться.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Ты уже лучший навигатор, чем я.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Когда я впервые попала сюда, я потерялась у комплекса!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Так чем ты сегодня занималась бабушка?")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Я следовала своему обычному распорядку.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Я только что вернулась с прогулки по пляжу.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Сейчас я готовлю ужин в мультиварке на сегодня.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Ты когда-нибудь пользовался мультиваркой?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Не думаю, нет.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Я обожаю это.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Это один из самых простых способов приготовления.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Просто брось ингредиенты в мультиварку, а она сделает все остальное!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Я ленива, когда готовлю что-то для себя.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Так что чем проще приготовить еду, тем лучше.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Хочешь покажу, как пользоваться мультиваркой, [n.say_name]?")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Да!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Присаживайся у кухонного стола.")

    call fade_to_black (1)
    call process_scene_beginning (bg="bg edna_house_daytime", char_tuple_array=[ (n, "outfit clothesjacket pose behindhead face neutral blush false"), (edna, "outfit clothes pose fisthip face neutral blush false mouth red") ], dream=dream )

    call process_character (edna, appearance="pose fisthip face neutral blush false", text="И ты устанавливаешь температуру, вот и все!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="И это все?")
    call process_character (n, appearance="pose behindhead face happy blush false", text="Ух ты!")
    call process_character (n, appearance="pose behindhead face happy blush false", text="Это очень просто!")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Я говорила тебе.")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Через несколько часов ты почувствуешь фантастический аромат, и еда будет готова.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Так что мы просто подождем, а?")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Ну, нет причин сидеть и смотреть на часы.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Мы должны скоротать время, делая что-то вместе.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Любые идеи, что ты хочешь сделать, [n.say_name]?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Хм...")
    call process_character (edna, appearance="pose fisthip face curious blush false", text="Ты и [sa.say_name] еще играете в эти игры, правильно?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты имеешь в виду видеоигры, Бабушка?")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Да, точно!")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Я недавно читала в газете, что открылся новый большой игровой зал на прошлой неделе.")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Большой?!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Где?!")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="В торговом центре вниз по улице.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Я помню, видела его в последний раз, когда была там.")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Мы можем пойти туда, Бабушка?")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Пожалуйста?")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Знаешь, что я тебе скажу.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Я отведу тебя в зал игровых автоматов, если мы сходим в кино после.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Кинотеатр по соседству, и вышел новый фильм, который я умираю, как хочу увидеть.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Что это за фильм?")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Я думаю, тебе понравится, [n.say_name].")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Речь идет о двух путешественниках во времени, которые пытаются изменить ход истории.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Он получил хорошие отзывы.")
    call process_character (n, appearance="pose behindhead face happy blush false", text="О, я видел анонс этого фильма!")
    call process_character (n, appearance="pose behindhead face happy blush false", text="Вроде он называется Вихрь Времени?")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Точно!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Я действительно хочу его посмотреть!")
    call process_character (n, appearance="pose handfist face happy blush false", text="[k.say_name] сказала, что это было потрясающе!")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Следующий показ будет через два часа, так что давай побежали!")

    call fade_to_black (1)
    "{i}Позже...{/i}"
    call process_scene_beginning (bg="bg edna_house_evening", char_tuple_array=[ (n, "outfit clothesjacket pose handpocket"), (edna, "outfit clothes pose handclasp face neutral blush false mouth red") ], dream=dream )

    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="{i}Нюх-Нюх...{/i}")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Еда почти готова, я чувствую ее запах!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Этот фильм был просто сногсшибательный!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Рейтинг, который он получил от критиков, был определенно на высоте.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Это фильм, который я бы посмотрела только один раз.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Я хочу посмотреть его снова!")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Ты должен пойти с [sa.say_name] в следующий раз.")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false", text="Думаешь, ей понравится?")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Определенно!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Она любит научную фантастику!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Тогда не порть ей удовольствие!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Ты хочешь поесть здесь со мной, [n.say_name]?")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Здесь достаточно места для двоих!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Конечно, Бабушка!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Спасибо!")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Вообще-то, я сделала слишком много...")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Я положу остатки в контейнер, чтобы ты мог отнести их домой для всех.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Круто.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Я позвоню твоей маме и скажу, что ты ешь здесь.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="На самом деле, я думаю, что она должна забрать тебя.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Становится темно.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Все в порядке, Бабушка.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Я могу вернуться домой пешком.")
    call process_character (edna, appearance="outfit clothes pose handclasp face concerned blush false", text="Ты уверен?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Да, это не проблема.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Я хорошо вижу ночью.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Ах, у тебя сильные, молодые глаза!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Мне трудно видеть вещи в темноте.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Вот почему я не люблю поздно садиться за руль, это заставляет меня нервничать.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="На обратном пути к дому стоят уличные фонари.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Так что мне не нужно беспокоиться, что будет слишком темно.")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false", text="Мм, все же...")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false", text="Возьми один из моих фонариков, когда пойдёшь.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Лучше перестраховаться, чем потом сожалеть!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Спасибо, что позволила мне быть с тобой сегодня, Бабушка!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Не стесняйся болтаться здесь столько, сколько хочешь, [n.say_name]!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Я счастлива провести время со своим внуком!")

    call process_end_of_scene ("edna_scene_intro_2", char=edna, dream=dream)

    return

label edna_scene_minigame_intro(dream=False):
    call edna_scene_minigame_intro_sex (dream)
    return

label edna_scene_minigame_intro_sex(dream=dream):
    call process_scene_beginning (bg=edna_house, char_tuple_array=[ (n, "outfit clothesjacket pose behindhead face neutral blush false"), (edna, "outfit clothes pose handhip face neutral blush false mouth red") ], dream=dream )

    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Что это за теннисные мячики, Бабушка?")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Ах, ты заметил ведро, полное их?")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Я член теннисного клуба!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Ты?")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Я присоединилась к нему вскоре после переезда сюда.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Я никогда раньше не играла в теннис!")
    call process_character (edna, appearance="pose fisthip face curious blush false", text="Ты когда-нибудь играл в теннис, [n.say_name]?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Я?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Нет.")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Ты должен попробовать со мной!")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Корты пока что пустые.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Так что мы можем проводить там столько времени, сколько захотим.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Трудно ли играть?")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Это плёвое дело!")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Если такой неловкий человек, как я, может играть в теннис, то ты, конечно, сможешь!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Хм...")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Хорошо, я попробую!")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Как только попадёшь в ритм, ты почувствуешь себя профессионалом на корте!")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Или это то, как я хотела бы представить себя, ха-ха!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Хорошо у тебя получается, бабушка?")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Я выиграла пару турниров, проведенных с другими жителями кондоминиума.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Конечно, никто из нас не является экспертом, но со временем наши навыки выросли.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Интересно, будет ли у меня шанс победить тебя...")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Я могу не торопиться с тобой, если хочешь.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Или, если ты предпочитаешь более сложные задачи, я могу играть в своем обычном темпе.")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="{b}Я буду очень впечатлена, если ты меня выиграешь!{/b}")

    window hide
    menu:
        "Играть в мини-игру Тенис":
            call process_end_of_scene ("edna_scene_minigame_intro", char=edna, dream=dream, force_no_boldness=True, force_not_replayable=True, do_not_jump=True)
            call minigame_table_tennis (partner=edna)
        "Не играть":
            call process_end_of_scene ("edna_scene_minigame_intro", char=edna, dream=dream, force_no_boldness=True, force_not_replayable=True, do_not_jump=started_main_game)
            if started_main_game:
                $ edna.scene = ""
                $ edna_house.start()

    return

label edna_scene_nate_underwear(dream=False):
    call edna_scene_nate_underwear_sex (dream=dream)

    return

label edna_scene_nate_underwear_sex(dream=False):
    call process_scene_beginning (bg="bg nate_room_daytime", dream=dream )
    $ replace_position = True

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="...")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Эй [n.say_name], хочешь переночевать сегодня у бабушки?")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Я бы с удовольствием, да!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Бабушка знает, что мы придём?")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="О, да!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Я спросила маму, она позвонила бабушке и сказала, что хотела бы, чтобы мы пришли!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Хорошо, круто!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Нам взять что-нибудь?")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Я возьму свою консоль, чтобы мы могли играть в игры ночью!")
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="Или мы можем посмотреть фильм или два!")


    call process_new_location (bg="bg edna_house_daytime", dream=dream)
    $ sa.position = "right"
    $ display_multiple_characters([ (edna, "outfit clothes pose handhip face happy blush false mouth red"), (sa, "outfit clothes pose leaning face happy blush false") ])

    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Мы прибыли!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Вы рады остаться на ночь?")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Да, Бабушка!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="У тебя что-нибудь запланировано на день?")
    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="Хм, не совсем так...")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="У тебя есть идеи, что нам делать, бабушка?")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false", text="А у меня есть?")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false", text="Дай подумать...")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="О!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Что насчет зала игровых автоматов [n.say_name], в который мы ходили?")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Это о нём ты рассказывал мне, [n.say_name]?")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Где есть пятьдесят различных аркадных игр?!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Да, это именно тот самый!")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Я голосую ЗА!")
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="Я тоже голосую за то, чтобы пойти туда!")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Ты тоже любите аркадные автоматы, [sa.say_name]?")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Автоматы самые крутые вещи!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Нет ничего похожего на них.")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Ты не знаешь, там есть пинбол?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Да, я видел несколько пинбольных автоматов.")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="В пинбол так весело играть!")
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="У меня плохо получается, но я все равно весело провожу время!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Мы должны сыграть во все игры двух игроков!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Правильно, мы должны это сделать!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="[n.say_name] и я всегда играем в кооперативные игры в залах, Бабушка, и мы обычно делаем это очень хорошо!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Я думаю, это потому, что вы близнецы.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Вы находитесь в синхронизации друг с другом, когда играете!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Мы можем побыть там немного, бабушка?")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Вы хотели провести там большую часть дня?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face happy blush false", text="Я так думаю, да!")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Я пойду посмотрю фильм после того, как подброшу вас туда.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Так вы оба сможете повеселиться, а я проведу время в кино.")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Я одобряю этот план.")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Пошли!")

    call fade_to_black (1)
    "{i}Через несколько часов...{/i}"
    call process_new_location (bg="bg edna_house_evening", dream=dream)
    $ sa.position = "right"
    $ display_multiple_characters([ (edna, "outfit clothes pose handhip face happy blush false mouth red"), (sa, "outfit clothes pose handsbehind face neutral blush false") ])

    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Хотела бы я увидеть момент, когда ты выиграла джек-пот!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Это невероятно, что вы получили его только после нескольких попыток.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Игра требует быстрых рефлексов, но я знала, что могу получить его после того, как пойму закономерность.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Это так здорово, что вы можете использовать выигрыш, в качестве оплаты других видеоигр.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Некоторые из них вышли совсем недавно!")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Я знаю, я не могла в это поверить!")
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Я смогла выбрать одну игру, которая стоит пятьдесят баксов!")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Вы двое там были как бандиты.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Я надеюсь, что они позволят вам вернуться после того, сколько вы выиграли!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Ты хочешь сыграть в одну из новых игр, [sa.say_name]?")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Ммм не сейчас.")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Мы сегодня играли в кучу игр в аркадном зале.")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Я лучше фильм посмотрю!")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Хотите попкорна или чего-нибудь выпить?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Что у тебя есть выпить?")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Давай посмотрим...")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Есть вода, чай со льдом, немного сока...")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Ахх, думаю, что есть...{w=1.0}да, точно.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Я могу сделать немного газировки, если хочешь!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Я буду, пожалуйста!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="Я тоже!")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Какой фильм вы собираетесь смотреть?")
    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="Я тут подумала...")
    call process_character (sa, appearance="outfit clothes pose handface face curious blush false", text="...")
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Повелитель амулетов!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Это замечательный фильм!")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Но это надолго.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Когда посмотрите, сразу ложитесь спать.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Хорошо, Бабушка.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Я ложусь спать раньше, чем вы привыкли.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Так что я буду спать, когда вы будете ложиться.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="В кондоминиуме есть шумовой комендантский час, поэтому убедитесь, что ведёте себя тихо.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Поняла.")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Спасибо, Бабушка.")

    call process_new_location (bg="bg edna_house_evening", dream=dream)
    $ display_multiple_characters([ (n, "outfit underwear pose handsdown face neutral blush false"), (sa, "outfit underwear pose leaning face happy blush false") ])

    call process_character (sa, appearance="outfit underwear pose leaning face happy blush false", text="Этот фильм такой крутой!")
    call process_character (sa, appearance="outfit underwear pose leaning face happy blush false", text="Меня даже не волновало, сколько он продлится!")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="Я не скучал ни разу во время просмотра!")
    call process_character (sa, appearance="outfit underwear pose handface face neutral blush false", text="Черт возьми, уже поздно.")
    call process_character (sa, appearance="outfit underwear pose handface face neutral blush false", text="...")
    call process_character (sa, appearance="outfit underwear pose handface face neutral blush false", text="Я могу поспать сегодня на балконе.")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="На балконе?")
    call process_character (n, appearance="outfit underwear pose behindhead face neutral blush false", text="Почему так?")
    call process_character (sa, appearance="outfit underwear pose handsbehind face happy blush false", text="Потому что будет так круто смотреть на океан, когда я проснусь!")
    call process_character (n, appearance="outfit underwear pose behindhead face curious blush false", text="Разве там не будет ветрено?")
    call process_character (sa, appearance="outfit underwear pose handsbehind face neutral blush false", text="Сегодня тепло, так что мне не должно быть холодно.")
    call process_character (sa, appearance="outfit underwear pose leaning face neutral blush false", text="Я возьму одеяло на всякий случай!")

    call fade_to_black (1)

    "{i}Следующим утром...{/i}"
    call process_new_location (bg="bg edna_house_daytime", dream=dream)
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false mouth red", text="...{p}...")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="(Я думаю [sa.say_name] и [n.say_name] вчера вечером припозднились)")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="(Я даже не слышу, как они шевелятся...)")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face aroused blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Доброе позднее утро, [n.say_name]!")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face aroused blush false", text="{i}Зевок.{/i}..")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face aroused blush false", text="Утро.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Во сколько ты лег спать прошлой ночью?")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face aroused blush false", text="Было поздно...")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Твоя сестра еще не встала?")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face neutral blush false", text="{i}Зевок.{/i}..")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face neutral blush false", text="Нет.")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face neutral blush false", text="Она устала больше, чем я думаю.")
    call process_character (edna, appearance="outfit clothes pose fisthip face curious blush false", text="Почему так?")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face neutral blush false", text="Она хотела спать на балконе, поэтому схватила одеяло и попыталась лечь там.")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face neutral blush false", text="Но я думаю, она не могла уснуть и в конце концов пришла в спальню ко мне.")
    call process_character (edna, appearance="outfit clothes pose handclasp face concerned blush false", text="О, она, наверное, усталая.")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face neutral blush false", text="Она не хотела, но разбудила меня, когда вошла.")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face aroused blush false", text="Так вот почему я все еще немного уставший...")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Вымой лицо холодной водой, это должно тебя разбудить.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="...{p}...")
    call process_character (edna, appearance="outfit clothes pose handhip face curious blush false", text="([n.say_name] не заметил, что у него эрекция?)")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face aroused blush false", text="...{p}...")
    call process_character (edna, appearance="outfit clothes pose handhip face curious blush false", text="(Она у него с тех пор, как он вышел из спальни...)")
    call process_character (edna, appearance="outfit clothes pose handhip face curious blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="(Я думаю, что он уже знает об этом)")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="(Это часто с ним случается?)")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="(Может быть, поэтому он не замечает)")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face curious blush false", text="(Так странно, какой мой пенис был твердый, когда я встал)")

    if "sam_scene_2_seq_2" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Я не думаю, что [sa.say_name] трогала его или что-нибудь, пока я спал...)")
    else:
        call process_character (n, appearance="blush false", text="(Интересно, станет ли он мягче через некоторое время...)")

    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false", text="(Эрекция должна длиться так долго?)")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false", text="(Кажется необычным)")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear_hard pose twohandfist face concerned blush false", text="...")
    call process_character (n, appearance="outfit underwear_hard pose twohandfist face concerned blush false", text="Мне надо в туалет, Бабушка.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="(О, он должно быть заметил)")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="(Это заняло у него некоторое время...)")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="(Может также сделать вид, как будто я этого не видела)")

    call process_character (n, appearance="outfit underwear_hard pose handsdown face neutral blush false")

    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Я налью тебе апельсинового сока, когда ты выйдешь из ванной.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Я собиралась приготовить яйца и тосты для нас.")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face neutral blush false", text="Мило.")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face neutral blush false", text="Можно мне немного джема на тост тоже?")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="У меня есть виноградное варенье.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Это вкусно?")
    call process_character (n, appearance="outfit underwear_hard pose handfist face neutral blush false", text="По мне так неплохо.")

    if not dream:
        $ week.advance_to_next_day()

    python:
        edna.revistable_scenes.add("edna_scene_nate_underwear_revisit")
        if not dream:
            stats.add_stat("times_had_erection", 1)

    call process_end_of_scene ("edna_scene_nate_underwear", char=edna, dream=dream)

    return

label edna_scene_underwear(dream=False):
    call edna_scene_underwear_sex (dream=dream)

    return

label edna_scene_underwear_sex(dream=False):
    call process_scene_beginning (bg="bg edna_house_daytime", dream=dream )

    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Бабушка, это я [n.say_name]!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="...{p}...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Бабушка!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="(Может быть, ее нет дома?)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="(Дверь не заперта...)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="(О, хорошо, я думаю, я всегда могу вернуться позже)")
    call process_character (edna, appearance="outfit underwear pose handclasp face flirt blush false")
    pause 0.5
    call process_character (edna, appearance="outfit underwear pose handclasp face flirt blush false", text="{i}Зевок.{/i}..")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face embarrassed blush false", text="Б-бабуля?!")
    call process_character (edna, appearance="outfit underwear pose handclasp face flirt blush false", text="О, не так громко, [n.say_name].")
    call process_character (edna, appearance="outfit underwear pose handclasp face flirt blush false", text="...")
    call process_character (edna, appearance="outfit underwear pose handclasp face flirt blush false", text="Который сейчас час?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Ч-час дня.")
    call process_character (edna, appearance="outfit underwear pose handhip face embarrassed blush false", text="О, боже...")
    call process_character (edna, appearance="outfit underwear pose handhip face embarrassed blush false", text="Это правда?")
    call process_character (edna, appearance="outfit underwear pose handhip face embarrassed blush false", text="...")
    call process_character (edna, appearance="outfit underwear pose handclasp face neutral blush false", text="Прошлой ночью в доме отдыха была вечеринка.")
    call process_character (edna, appearance="outfit underwear pose handclasp face neutral blush false", text="Я никогда раньше не пробовала шампанское, но выпила несколько бокалов.")
    call process_character (edna, appearance="outfit underwear pose handclasp face sad blush false", text="И у меня раскалывалась голова.")
    call process_character (edna, appearance="outfit underwear pose fisthip face sad blush false", text="Я даже не хотела вставать с постели.")
    call process_character (edna, appearance="outfit underwear pose fisthip face sad blush false", text="Пропустила утреннюю прогулку.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Жаль, что ты плохо себя чувствуешь, бабушка.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Стало немного лучше?")
    call process_character (edna, appearance="outfit underwear pose handclasp face neutral blush false", text="Я уверена, что тошнота пройдет через некоторое время.")
    call process_character (edna, appearance="outfit underwear pose handclasp face neutral blush false", text="Мне нужно принять аспирин и перекусить.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="(Бабушка не понимает, что она в нижнем белье?)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="(Я не знаю, должен ли я что-то сказать или нет)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...")

    if stats.stat_value("times_seen_bra") > 0:
        call process_character (n, appearance="blush false", text="(Я никогда раньше не видел такого лифчика...)")
        call process_character (n, appearance="pose behindhead face embarrassed blush false", text="(Как он вообще держится?)")
        call process_character (n, appearance="pose behindhead face embarrassed blush false", text="...")
        call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="(Он соскользнет через некоторое время?!)")
        call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="(Если это произойдет, ее сиськи будут прямо передо мной)")
        call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="...")
    else:
        call process_character (n, appearance="blush false", text="(Как он держится?)")
        call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="(Соскользнет через некоторое время, не так ли?!)")
        call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="(Если это произойдет, ее сиськи будут прямо передо мной)")
        call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="...")

    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face concerned blush false")

    call process_character (edna, appearance="outfit underwear pose fisthip face curious blush false", text="(Почему [n.say_name] так долго смотрел на меня?)")
    call process_character (edna, appearance="outfit underwear pose fisthip face curious blush false", text="...")
    call process_character (edna, appearance="outfit underwear pose fisthip face curious blush false", text="(У него...)")
    call process_character (edna, appearance="outfit underwear pose handclasp face embarrassed blush false", text="(эрекция?)")
    call process_character (edna, appearance="outfit underwear pose handclasp face embarrassed blush false", text="(Почему сейчас?)")
    call process_character (edna, appearance="outfit underwear pose handclasp face neutral blush false", text="(Я могла понять, как она случилась утром)")
    call process_character (edna, appearance="outfit underwear pose handclasp face neutral blush false", text="...")
    call process_character (edna, appearance="outfit underwear pose handhip face curious blush false", text="(Они происходят случайно, без предупреждения для него?)")
    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face curious blush false", text="...")
    call process_character (edna, appearance="outfit underwear pose handhip face shock blush false", text="!!")
    call process_character (edna, appearance="outfit underwear pose handhip face shock blush false", text="(Я все еще в нижнем белье!)")
    call process_character (edna, appearance="outfit underwear pose handclasp face shock blush false", text="(Я даже не поняла, что не оделась должным образом!)")
    call process_character (edna, appearance="outfit underwear pose handclasp face shock blush false", text="[n.say_name]!")
    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face embarrassed blush false", text="Д-да?!")
    call process_character (edna, appearance="outfit underwear pose handclasp face embarrassed blush true", text="Мне так жаль!")
    call process_character (edna, appearance="outfit underwear pose handclasp face embarrassed blush true", text="Я не порядочный человек!")
    call process_character (edna, appearance="outfit underwear pose handclasp face embarrassed blush true", text="Мне нужно одеться!")

    call character_leave_dissolve (edna)
    pause 0.5

    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face curious blush false", text="(Я думаю, что она вообще не знала...)")
    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face curious blush false", text="...{p}...")

    pause 0.5
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false")
    pause 1.0

    call process_character (edna, appearance="outfit clothes pose handhip face embarrassed blush false", text="Я так смущена этим, [n.say_name]...")
    call process_character (edna, appearance="outfit clothes pose handhip face embarrassed blush false", text="Я чувствовала себя настолько слабой, что мой разум не мог соображать.")
    call process_character (edna, appearance="outfit clothes pose fisthip face concerned blush false", text="Я даже губы не накрасила...")
    call process_character (edna, appearance="outfit clothes pose fisthip face concerned blush false", text="Я, наверное, выглядела как старая ведьма в нижнем белье.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Старая ведьма?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Я не думал, что ты похожа на неё, Бабушка.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face embarrassed blush false", text="Я просто… {w=1.0}удивлен видеть тебя такой.")
    call process_character (edna, appearance="outfit clothes pose handhip face angry blush false", text="Я больше никогда не буду пить шампанское...")
    call process_character (edna, appearance="outfit clothes pose handhip face angry blush false", text="Оно совсем не сочетается с моей системой.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="{i}Вздох.{/i}..")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Я должна была знать, особенно в моем возрасте.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Во всяком случае, я думаю, что это хорошо, что ты снова пришёл ко мне, [n.say_name]!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Ты спешил куда-нибудь еще, или можешь остаться на обед?")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Ну, это будет поздний завтрак для меня!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Мне сегодня нечем заняться.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Так что да, я могу остаться на обед.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Тебе нравится тунец?")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="У меня есть немного, если хочешь.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="...{p}...")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="(Эрекция [n.say_name] спала...)")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="(Это длилось не очень долго)")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handhip face curious blush false", text="(У него была эрекция только когда я была в нижнем белье?)")
    call process_character (edna, appearance="outfit clothes pose handhip face curious blush false", text="(После того, как я надела свою одежду, у него больше не было)")
    call process_character (edna, appearance="outfit clothes pose handhip face curious blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handclasp face embarrassed blush false", text="(Может быть, он получил потому что...)")
    call process_character (edna, appearance="outfit clothes pose handclasp face embarrassed blush false", text="...{p}...")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="(Нет, я делаю поспешные выводы)")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="(Нет закономерности)")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="(Молодые люди получают случайные жесткие стояки все время!)")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="(Это всего лишь часть их развития)")


    $ replace_position = False
    python:
        edna.revistable_scenes.add("edna_scene_underwear_revisit")

        if not dream:
            stats.add_stat("times_seen_panties", 1)
            stats.add_stat("times_seen_bra", 1)
            stats.add_stat("times_had_erection", 1)

    call process_end_of_scene ("edna_scene_underwear", char=edna, dream=dream)

    return

label edna_scene_swimsuit(dream=False):
    call edna_scene_swimsuit_sex (dream=dream)

    return

label edna_scene_swimsuit_sex(dream=False):
    call process_scene_beginning (bg="bg kitchen_daytime", dream=dream )
    $ sa.position = "right"
    $ k.position = "right"
    $ replace_position = True
    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (si, "outfit clothes pose handsfront face neutral blush false") ])

    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Бабушка разговаривает по телефону.")

    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Привет, Бабушка!")
    call process_character (sa, appearance="outfit clothes pose handsbehind face neutral blush false", text="Передай привет от меня тоже бабушке!")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Она передает привет в ответ.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Так это правда, что так хорошо на пляже, мама?")
    call process_character (si, appearance="pose armunder face neutral blush false", text="...{p}...")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Хорошо, сейчас спрошу.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Бабушка хотела узнать, не хотели бы мы присоединиться к ней сегодня на пляже.")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Я бы хотел отправиться туда!")
    call process_character (sa, appearance="pose leaning face happy blush false", text="Я тоже!")

    if "sam_scene_swimsuit" in scenes_completed:
        call process_character (sa, appearance="pose leaning face happy blush false", text="И на этот раз я не забуду взять свой купальник!")
        call process_character (si, appearance="pose armunder face neutral blush false", text="Дай его мне, чтобы я могла упаковать его в пляжную сумку.")
        call process_character (sa, appearance="pose handface face happy blush false", text="Не надо!")
        call process_character (sa, appearance="pose handface face neutral blush false", text="Сейчас я надену его и одену поверх него свою одежду!")
        call process_character (si, appearance="pose armunder face neutral blush false", text="Ах, это хорошая стратегия, [sa.say_name].")
        call process_character (si, appearance="pose armunder face happy blush false", text="Теперь ты ничего не забудешь!")
    else:
        call process_character (sa, appearance="pose handface face concerned blush false", text="У меня все еще нет купальника.")
        call process_character (si, appearance="pose armunder face neutral blush false", text="Все в порядке, просто надень что-нибудь легкое.")
        call process_character (sa, appearance="pose handsbehind face neutral blush false", text="Могу ли я использовать мое нижнее белье, чтобы пойти в океан?!")
        call process_character (si, appearance="pose handsup face concerned blush false", text="Абсолютно нет.")
        call process_character (si, appearance="pose handsup face concerned blush false", text="Я не хочу, чтобы ты испортила свой лифчик.")
        call process_character (sa, appearance="pose handface face concerned blush false", text="Ох, как не везёт...")
        call process_character (sa, appearance="pose handface face concerned blush false", text="...")
        call process_character (sa, appearance="pose handface face neutral blush false", text="Что если я надену футболку и шорты для плавания?")
        call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
        call process_character (si, appearance="pose handsfront face neutral blush false", text="Это сойдёт.")
        call process_character (si, appearance="pose handsfront face curious blush false", text="Но дай мне подумать.")

    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Мы должны спросить, может [k.say_name] тоже хочет пойти.")
    call process_character (k, appearance="outfit clothes pose armcross face neutral blush false", text="Куда пошли?")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Бабушка говорит, что сегодня идеальный пляжный день.")
    call process_character (si, appearance="pose handsup face concerned blush false", text="Она пригласила нас.")
    call process_character (si, appearance="pose handsup face concerned blush false", text="Ты хочешь пойти?")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="Тебе вообще нужно спрашивать меня, Мама?")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="Любое приглашение на пляж является автоматическим да от меня!")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Тогда почему бы вам всем не надеть купальники и не подготовиться.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Я сделаю бутерброды, и там мы их съедим.")
    call process_character (si, appearance="pose armunder face curious blush false", text="Не забудьте взять с собой сменную одежду, если вы идете в океан.")
    call process_character (si, appearance="pose armunder face curious blush false", text="Вы замёрзнете, если будете в мокром купальнике весь день!")

    call process_new_location ("bg beach_daytime", dream=dream)

    if "sam_scene_swimsuit" in scenes_completed:
        $ sa.outfit = "bikini"
    else:
        $ sa.outfit = "clothes"

    if "simone_scene_swimsuit" in scenes_completed:
        $ si.outfit = "swimsuit"
    else:
        $ si.outfit = "yoga"

    python hide:
        for char in character_list():
            char.position = "right"

    $ replace_position = True
    $ edna.position = "left"

    call process_character (sa, appearance="pose handsbehind face happy blush false", text="Даа, мы здесь!")
    call process_character (n, appearance="outfit swimsuit pose behindhead face embarrassed blush false", text="Ой, ох, ах...{w=0.5} песок горячий!")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Вот почему ты должен носить сандалии, бро.")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Или просто должны терпеть это!")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Как только мы установим зонтик, тень охладит песок.")
    call process_character (n, appearance="outfit swimsuit pose behindhead face neutral blush false", text="Где бабушка?")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Она сказала нам приготовится перед кондоминиумом, и что она присоединится к нам.")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="О, волны там очень большие!")
    call process_character (sa, appearance="pose leaning face neutral blush false", text="Должна...{w=0.5}нырнуть...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Держись! Прежде чем это сделаешь...")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Тебе нужно намазаться солнцезащитным кремом.")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Но я буду часто находиться в воде.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Ты все еще можешь обжечься, пока ты там.")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="И я знаю, как ты ненавидишь солнечные ожоги.")
    call process_character (sa, appearance="pose handsbehind face angry blush false", text="Я ненавижу их, но я хочу войти в океан!")
    call process_character (si, appearance="pose handsup face neutral blush false", text="И будь терпеливой.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="Покрой каждый дюйм себя, это водостойкий солнцезащитный крем.")
    call process_character (si, appearance="pose handsup face neutral blush false", text="То же самое касается и тебя, [n.say_name].")
    call process_character (n, appearance="outfit swimsuit pose behindhead face curious blush false", text="Солнцезащитный крем всегда такой жирный и противный.")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="Ты выживешь, бро.")
    call process_character (k, appearance="outfit bikini pose armcross face neutral blush false", text="Мне не нужно так сильно загорать из-за того, что я уже загорела.")
    call process_character (sa, appearance="pose leaning face curious blush false", text="Там есть люди, играющие в волейбол?")
    call process_character (k, appearance="outfit bikini pose armsup face shocked blush false", text="Что? Где?")
    call process_character (sa, appearance="pose handface face curious blush false", text="Я вижу белую сетку и прыгающий мяч.")
    call process_character (n, appearance="outfit swimsuit pose behindhead face neutral blush false", text="О, да, я тоже это вижу.")
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="Хороший глаз, сестренка!")
    call process_character (k, appearance="outfit bikini pose handhip face happy blush false", text="Я знаю, куда направляюсь!")
    call process_character (si, appearance="pose armunder face neutral blush false", text="Ты собираешься поиграть в волейбол с этими людьми?")
    call process_character (k, appearance="outfit bikini pose armsup face neutral blush false", text="Играть?")
    call process_character (k, appearance="outfit bikini pose armsup face happy blush false", text="Я собираюсь выиграть!")

    call character_leave_dissolve (k)
    pause 1.0

    call process_character (si, appearance="pose armunder face happy blush false", text="Бьюсь об заклад, мы услышим ее крики отсюда!")
    call process_character (si, appearance="pose armunder face happy blush false", text="...")
    call process_character (si, appearance="pose handsfront face neutral blush false", text="[sa.say_name], ты видишь какие-либо признаки бабушки?")
    call process_character (sa, appearance="pose handface face curious blush false", text="Хм...")
    call process_character (sa, appearance="pose handface face curious blush false", text="...")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Мне кажется, я ее вижу!")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Она носит эту большую черную шляпу!")
    call process_character (edna, appearance="", text="Эй, ребята!")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face happy blush false", text="Эй, Бабушка!")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face happy blush false", text="Мы только что приехали сюда.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false hat sunhat mouth red")
    call process_character (edna, text="Я как раз собиралась идти к вам.")
    call process_character (edna, text="Затем я увидела, что [k.say_name] пробежала мимо с ее ярко-зеленым бикини!")
    call process_character (si, appearance="pose armunder face shocked blush false", text="М-мама!")
    call process_character (si, appearance="pose armunder face shocked blush false", text="Что это на тебе надето?!")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="А ты как думаешь?")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Я купила его на распродаже!")
    call process_character (si, appearance="pose handsup face embarrassed blush false", text="...")
    call process_character (si, appearance="pose handsup face embarrassed blush false", text="Это так откровенно...")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Я уже получила много комплиментов.")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Несколько молодых людей уже подошли ко мне.")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Это было очень лестно.")
    call process_character (si, appearance="pose armunder face embarrassed blush false", text="Надеюсь, это не главная причина, по которой ты носишь что-то подобное...")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Что, если это так?")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Есть причина, почему этого не должно быть?")
    call process_character (si, appearance="pose handsfront face embarrassed blush false", text="Нет.")
    call process_character (si, appearance="pose handsfront face embarrassed blush false", text="Все именно так...")

    if si.outfit == "swimsuit":
        call process_character (edna, appearance="pose handhip face neutral blush false", text="А что насчет твоего купальник?")
        call process_character (edna, appearance="pose handhip face neutral blush false", text="Разве он не слишком мал для твоего бюста?")
        call process_character (si, appearance="pose armunder face curious blush false", text="[n.say_name] купил мне этот купальник, и он не знал точного размера, который мне подойдет...")
        call process_character (edna, appearance="pose handclasp face happy blush false", text="Ну разве это не мило с твоей стороны!")
        call process_character (edna, appearance="pose handclasp face happy blush false", text="Ты купил маме ее собственный купальник?")
        call process_character (n, appearance="pose handfist face neutral blush false", text="Ага!")
        call process_character (edna, appearance="pose handhip face happy blush false", text="Ну, даже если он немного маленький, я думаю ты хорошо смотришься в нём дочка!")
        call process_character (si, appearance="pose handsfront face neutral blush false", text="...")
        call process_character (si, appearance="pose handsfront face neutral blush false", text="Спасибо, Мам.")
    else:
        call process_character (edna, appearance="pose handhip face curious blush false", text="У тебя нет собственного костюма, [si.say_name]?")
        call process_character (si, appearance="pose handsup face neutral blush false", text="Мне не очень нравится носить купальник.")
        call process_character (si, appearance="pose handsup face neutral blush false", text="Так что вместо этого я надела костюм для йоги.")
        call process_character (si, appearance="pose handsup face neutral blush false", text="Мне совсем не жарко, что очень приятно.")

    call process_character (edna, appearance="pose handhip face neutral blush false")
    call process_character (sa, appearance="pose handface face neutral blush false", text="Мам, что-то не так с бабушкиным купальником?")
    call process_character (si, appearance="pose armunder face embarrassed blush false", text="...")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Я думаю, твоя мама просто чувствует, что я слишком стара, чтобы носить что-то вроде этого, вот и все.")
    call process_character (si, appearance="pose armunder face embarrassed blush false", text="Э-это еще не все...")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Все в порядке, дорогая.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="В конце концов, я твоя мать.")
    call process_character (edna, appearance="pose handhip face happy blush false", text="А родители всегда смущают своих детей!")
    call process_character (si, appearance="pose handsup face embarrassed blush false", text="(Ты можешь сказать это снова...)")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="[n.say_name], ты молодой человек...")
    call process_character (edna, appearance="pose handclasp face curious blush false", text="Что ты думаешь о том, во что я одета?")
    call process_character (n, appearance="outfit swimsuit pose behindhead face curious blush false", text="Ты спрашиваешь меня об этом?")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Конечно!")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Я бы хотела узнать твое мнение о моем бикини!")

    menu:
        "Я думаю, что он выглядит хорошо.":
            call process_character (edna, appearance="pose handhip face neutral blush false", text="[n.say_name] считает, что мне он подходит [si.say_name].")
            call process_character (si, appearance="pose armunder face neutral blush false", text="...")
            call process_character (sa, appearance="pose leaning face neutral blush false", text="Мне кажется тоже, бабушка!")
            call process_character (edna, appearance="pose handhip face happy blush false", text="Значит, двое из трех внуков согласны!")
            call process_character (edna, appearance="pose handhip face happy blush false", text="Я готова поспорить, что [k.say_name] согласится с ними!")
        "Она выглядит хорошо, Бабушка.":
            call process_character (edna, appearance="pose handhip face neutral blush false", text="Тебе нравится этот цвет?")
            call process_character (edna, appearance="pose handhip face neutral blush false", text="Я думаю, это очень хорошо дополняет мою шляпу.")
        "Я не могу перестать смотреть на него!":
            call add_boldness (1, tag="edna_scene_swimsuit_cant_stop_looking")
            call process_character (si, appearance="pose armunder face embarrassed blush false", text="[n.say_name], не смотри так на свою бабушку...")
            call process_character (edna, appearance="pose handhip face neutral blush false", text="Твоя мать права, это невежливо.")
            call process_character (n, appearance="pose handsdown face concerned blush false", text="...")
            call process_character (edna, appearance="pose handhip face happy blush false", text="Ты должен делать короткие взгляды, чтобы никто не заметил...")
            call process_character (si, appearance="pose handsup face shocked blush false", text="Не говори такие вещи, мама!")
            call process_character (edna, appearance="pose handclasp face happy blush false", text="Я просто шучу, [si.say_name]!")

    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="(Я вижу гораздо больше бабушкиных сисек, чем, когда она была в нижнем белье)")
    call process_character (n, appearance="pose behindhead face curious blush false", text="(Ее сиськи подпрыгивают, когда она двигается даже...)")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit swimsuit_hard pose twohandfist face curious blush false", text="(У меня опять встает!)")
    call process_character (n, appearance="outfit swimsuit_hard pose twohandfist face curious blush false", text="(Надеюсь, бабушка этого не увидит!)")

    call process_character (edna, appearance="pose handclasp face neutral blush false")


    call process_character (si, appearance="pose handsfront face neutral blush false", text="Готовы ли вы поплавать [sa.say_name] и [n.say_name]?")
    call process_character (si, appearance="pose handsfront face happy blush false", text="Покажи бабушке и мне, как ты умеешь кататься на волнах!")
    call process_character (sa, appearance="pose handface face happy blush false", text="Ты увидишь, насколько я хороший мастер!")
    call process_character (sa, appearance="pose handface face happy blush false", text="Несмотря на то, что я давно этого не делала, я помню технику бодисёрфа, как свои пять пальцев!")
    call process_character (n, appearance="outfit swimsuit_hard pose handfist face neutral blush false", text="Я тоже это прекрасно знаю!")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Удачи вам!")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Не пытайтесь взять волну, есть думаете, что вы не сможете справиться.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Ты свалишься кубарем, если поймаешь волну неправильно!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Это случалось со мной несколько раз в прошлом.")


    call character_leave_dissolve (n)
    pause 0.5

    call process_character (edna, appearance="pose fisthip face neutral blush false", text="...")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="(У [n.say_name] снова эрекция)")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="(Он смотрел на меня прямо перед тем, как это произошло)")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="(Затем он отвернулся...)")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="...{p}...")
    call process_character (edna, appearance="pose fisthip face curious blush false", text="(Я была причиной его эрекции?)")
    call process_character (edna, appearance="pose fisthip face curious blush false", text="...")


    $ replace_position = False

    python:
        edna.revistable_scenes.add("edna_scene_swimsuit_revisit")
        if not dream:
            stats.add_stat("times_had_erection", 1)

    call process_end_of_scene ("edna_scene_swimsuit", char=edna, dream=dream)

    return

label edna_scene_nate_naked(dream=False):
    call edna_scene_nate_naked_sex (dream=dream)

    return

label edna_scene_nate_naked_sex(dream=False):
    call process_scene_beginning (bg="bg kitchen_daytime", dream=dream )

    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false")

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Привет, Мам.")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Привет, [n.say_name]!")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Куда собрался?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Я подумываю пойти сегодня к бабушке домой.")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Да?")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="У меня к тебе просьба.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Хм?")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Бабушке очень нравится этот омолаживающий лосьон для кожи, который продается только в интернете.")
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Я заказала бутылку для нее на днях, и она только что пришла по почте!")
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Ты можешь отнести ей?")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Конечно, Мама!")
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Спасибо, [n.say_name], это сэкономит мне поездку!")
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Она будет очень рада получить еще одну бутылку.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Я отправлюсь туда прямо сейчас.")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Я позвоню бабушке и скажу, что ты придёшь!")


    call process_new_location ("bg edna_house_daytime", dream=dream)

    call process_character (edna, appearance="outfit clothes face neutral pose fisthip mouth red blush false", text="...{p}...")
    "{i}Тук-Тук-Тук{/i}"
    call process_character (edna, appearance="blush false", text="(О, это должно быть [n.say_name]!)")
    call process_character (edna, appearance="blush false", text="Сейчас буду, [n.say_name]!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Привет, Бабушка!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Я принес лосьон, что тебе нравится!")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Я ценю это [n.say_name]!")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Эта штука действительно работает.")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Никакой другой продукт не сравнится!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Что именно такое антивозрастной крем?")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Он помогает сохранить мою кожу увлажненной и предотвратить будущие морщины.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Твоя кожа высыхает, бабушка?")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Так и есть.")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Такое случается, когда стареешь!")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Кожа не производит много масла, поэтому она высыхает и трескается.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="И прежде чем ты это узнаешь, станешь городом морщин!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Так всегда происходит?")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="У тебя все еще молодая кожа, так что не о чем беспокоиться.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Но для меня это совсем другая история!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Хм...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Иногда моя кожа высыхает и чешется.")
    call process_character (edna, appearance="pose fisthip face curious blush false", text="Неужели?")
    call process_character (edna, appearance="pose fisthip face curious blush false", text="Что случилось с твоей матерью, когда она была моложе.")
    call process_character (edna, appearance="pose fisthip face curious blush false", text="Твоя кожа, вероятно, чувствительна к Солнцу.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Что-то вроде этого лосьона поможет?")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Так и есть!")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Даже если он разрекламировано как анти-возраст, лосьон больше для общего назначения!")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Хочешь, я натру тебя немного?")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Конечно!")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Я должна втереть его на бОльшую часть твоего тела, так что вся ваша кожа будет лечится.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Тебе нужно снять рубашку и штаны, чтобы я смогла втереть.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Ты собираешься растирать его по мне?")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Я очень опытна в такого рода вещах, [n.say_name].")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Я была массажистом в течение многих лет.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Окей.")

    call character_leave_dissolve (n)
    pause 0.5


    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false")

    call process_character (edna, appearance="pose handhip face neutral blush false", text="Я положу несколько полотенец на пол, чтобы было удобно.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Сначала ложись на живот, чтобы я могла заняться твоей спиной.")

    call fade_to_black (1)

    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...{p}...")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Этот лосьон на вес золота для меня.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Я узнала об этом от друга около года назад.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Он быстро раскупается, поэтому я попросила [si.say_name] купить несколько бутылок.")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="Он скользкий.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Ха, ты не привык к лосьонам, которыми я пользуюсь?")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Есть много людей, которым не нравится ощущение лосьона, это так смешно.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Они не будут использовать его просто потому, что он чувствует себя странно, хотя это может быть полезно.")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="Я надеюсь, что это хорошо работает.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Так и будет, клянусь тебе.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Хорошо, перевернись.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Позволь мне поработать спереди.")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...{p}...")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Плюс этого лосьона - тебе не нужно применять много.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Просто тонкий слой.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Но нужно втирать его.")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="...")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="([n.say_name], кажется, нервничает)")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="(Он, вероятно, не ожидал, что его бабушка будет тереть его руками по всему телу)")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="...")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="(Я понимаю, что ему это нравится)")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="(Возможно, поэтому он нервничает с самого начала?)")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="...")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="(Я почти закончила в любом случае)")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="(Просто нужно нанести лосьон на бедра)")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="(Бабушка втирает лосьон мне в ногу...)")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="(Ее руки приближаются к моему пенису...)")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="(Я могу видеть ее рубашку!)")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="(Ух-ох!)")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="...")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Не вставай ещё, [n.say_name].")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="{cps=40}Есть еще несколько пятен на ноге, которые я-{/cps}{w=0.75}{nw}")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="!!")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="[n.say_name]!")

    call process_new_location ("bg edna_house_daytime", dream=dream)

    $ display_multiple_characters([ (n, "outfit underwear_hard pose handsdown face curious blush true"), (edna, "outfit clothes pose handclasp face shock mouth red blush false") ])

    call process_character (n, appearance="outfit underwear_hard pose handsdown face curious blush true", text="...")
    call process_character (edna, appearance="pose handclasp face shock mouth red blush false", text="У тебя опять эрекция?!")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face concerned blush true", text="О-опять эрекция?")
    call process_character (edna, appearance="pose handclasp face embarrassed blush false", text="Да!")
    call process_character (edna, appearance="pose handhip face embarrassed blush false", text="Это уже четвертый раз, когда это происходит!")
    call process_character (edna, appearance="pose handhip face embarrassed blush false", text="У тебя впервые была одна, когда ты спал с [sa.say_name]...")
    call process_character (edna, appearance="pose handhip face embarrassed blush false", text="Потом у тебя была эрекция, когда я проснулась поздно...")
    call process_character (edna, appearance="pose handhip face embarrassed blush false", text="И совсем недавно, когда все были на пляже!")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face embarrassed blush true", text="!")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face embarrassed blush true", text="(Она замечала все это время?!)")
    call process_character (edna, appearance="pose handhip face embarrassed blush false", text="...")
    call process_character (edna, appearance="pose fisthip face concerned blush false", text="У тебя проблемы там, [n.say_name]?")
    call process_character (edna, appearance="pose fisthip face concerned blush false", text="Что-то не так с твоим пенисом?")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face curious blush true", text="Я так не думаю...")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Кажется ненормальным, что это происходит так часто.")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face concerned blush false", text="Н-ненормально?")
    call process_character (edna, appearance="pose handhip face curious blush false", text="Когда это началось, ты знаешь?")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face curious blush false", text="Н-нуу...")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face curious blush false", text="Примерно в начале лета.")
    call process_character (edna, appearance="pose handclasp face concerned blush false", text="Ты рассказал об этом своей маме?")

    if "simone_scene_2" in scenes_completed:
        call process_character (n, appearance="pose behindhead face concerned blush false", text="Она говорила со мной об этом, да.")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="Но она сказала, что это нормально...")
        call process_character (edna, appearance="pose fisthip face neutral blush false", text="Ну, такого рода вещи случаются, да.")
        call process_character (edna, appearance="pose fisthip face neutral blush false", text="Но я не знаю, буду ли я считать это нормальным.")
    else:
        call process_character (n, appearance="pose behindhead face concerned blush false", text="Н-нет.")
        call process_character (edna, appearance="pose fisthip face neutral blush false", text="Тебе было стыдно что-нибудь сказать?")

    call process_character (n, appearance="outfit underwear_hard pose handsdown face concerned blush false", text="...")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Мне нужно взглянуть, [n.say_name].")
    call process_character (n, appearance="outfit underwear_hard pose handsdown face embarrassed blush true", text="Ааа?")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Я хочу посмотреть, нет ли покраснения или видимых признаков, что что-то не так.")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face embarrassed blush true", text="...")
    call process_character (edna, appearance="pose fisthip face concerned blush false", text="Я не могу игнорировать потенциальную проблему со здоровьем моего внука!")
    call process_character (edna, appearance="pose fisthip face concerned blush false", text="Особенно в такой чувствительной зоне!")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Мне нужно только увидеть его на мгновение, [n.say_name].")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Пожалуйста, дай мне взглянуть.")
    call process_character (n, appearance="outfit underwear_hard pose behindhead face concerned blush true", text="...{p}...")

    call character_leave_dissolve (n)
    pause 0.5


    call process_character (n, appearance="outfit nudehard pose behindhead face concerned blush true")

    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Давайте посмотрим, что здесь происходит...")

    call process_character (edna, appearance="pose fisthip face neutral blush false position edna_special")
    call process_character (n, appearance="outfit nudehard pose behindhead face embarrassed blush true", text="Б-бабуля?!")
    call process_character (n, appearance="outfit nudehard pose behindhead face embarrassed blush true", text="Тебе обязательно быть так близко?")
    call process_character (edna, appearance="pose handclasp face curious blush false", text="Да, [n.say_name].")
    call process_character (edna, appearance="pose handclasp face curious blush false", text="Я ищу что-нибудь необычное.")
    call process_character (n, appearance="outfit nudehard pose behindhead face embarrassed blush true", text="...")
    call process_character (edna, appearance="pose handclasp face curious blush false", text="Хм...")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="У тебя крайняя плоть покрывает большую часть головки, но ничего необычного.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="...")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Твои яички выглядят нормально.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Нет покраснения или признаков раздражения.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="...")
    call process_character (n, appearance="outfit nudehard pose handsdown face concerned blush false", text="Так мой пенис в порядке?")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Я не вижу в этом ничего плохого.")
    call process_character (n, appearance="outfit nudehard pose handsdown face embarrassed blush false", text="{i}Фух.{/i}.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Он выглядит настолько здоровым, насколько может быть пенис...")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="...")
    call process_character (edna, appearance="pose handclasp face curious blush false", text="(Я удивлена, что у него все еще эрекция)")
    call process_character (edna, appearance="pose handclasp face curious blush false", text="(Я бы подумала, что смущение от этого сделало бы его вялым)")
    call process_character (edna, appearance="pose handclasp face curious blush false", text="(Но он не смягчился даже немного!)")
    call process_character (edna, appearance="pose handclasp face curious blush false", text="...")
    call process_character (edna, appearance="pose handclasp face curious blush false", text="(Единственная причина, по которой он все ещё твёрдый - это если...)")
    call process_character (edna, appearance="pose handclasp face embarrassed blush false", text="!")
    call process_character (edna, appearance="pose handclasp face embarrassed blush false", text="(Я возбуждаю [n.say_name]!)")
    call process_character (edna, appearance="pose handclasp face embarrassed blush false", text="(Моя интуиция была права!)")
    call process_character (edna, appearance="pose handclasp face embarrassed blush false", text="...{p}...")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="(Я думаю, вот почему [n.say_name] посещает \nменя так часто)")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="(Может быть, он надеется, что однажды увидит меня, выходящей из душа...)")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="...")
    call process_character (edna, appearance="pose handhip face happy blush false", text="(Он фантазирует обо мне?)")
    call process_character (edna, appearance="pose handhip face happy blush false", text="(Я его первая девушка-мечты?)")
    call process_character (edna, appearance="pose handhip face happy blush false", text="(Это было бы так мило, если бы я была!)")
    call process_character (edna, appearance="pose handhip face happy blush false", text="...")
    call process_character (edna, appearance="pose handhip face happy blush false", text="(Я не чувствую, что это неправильно для [n.say_name] думать обо мне)")
    call process_character (edna, appearance="pose handhip face happy blush false", text="...{p}...")
    call process_character (edna, appearance="pose handhip face happy blush false", text="(Было бы неправильно для меня думать о нем?)")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="(Бабушка сказала, что мой пенис в порядке...)")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="(Почему она все еще смотрит на нее?)")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="(Так тайна была разгадана)")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="([n.say_name] имеет сексуальное влечение ко мне, его бабушке)")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="...")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="(Я хотела, чтобы молодой человек испытывал чувства ко мне, но думала, что это была несбыточная мечта в моем возрасте...)")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="(А теперь вот мой внук, превращающий мою давнюю мечту в реальность...)")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="...{p}...")
    call process_character (edna, appearance="pose handhip face flirt blush false", text="(Жаль, что я не могу вспомнить, какой на ощупь молодой член)")
    call process_character (edna, appearance="pose handhip face flirt blush false", text="(Есть идеальный прямо передо мной...)")
    call process_character (edna, appearance="pose handhip face flirt blush false", text="...")
    call process_character (edna, appearance="pose handhip face flirt blush false", text="{cps=40}(Это так заманчиво-){/cps}{w=0.75}{nw}")
    call process_character (edna, appearance="pose handhip face embarrassed blush false", text="(Нет, нет!)")
    call process_character (edna, appearance="pose handhip face embarrassed blush false", text="(Я должна остановить себя!)")
    call process_character (edna, appearance="pose handclasp face embarrassed blush false position left")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="(Бабушка очень быстро встала...)")
    call process_character (edna, appearance="pose handclasp face embarrassed blush false", text="...")
    call process_character (edna, appearance="pose handclasp face embarrassed blush false", text="(Это было неосторожно с моей стороны!)")
    call process_character (edna, appearance="pose handclasp face embarrassed blush false", text="(Я не могу поверить, что почти прикоснулся к нему!)")
    call process_character (n, appearance="outfit nudehard pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit nudehard pose behindhead face concerned blush false", text="Можно я снова надену свою одежду, Бабушка?")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="О-ох, извини, [n.say_name].")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Да, конечно.")

    call character_leave_dissolve (n)
    pause 0.5


    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false")

    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Прости, если я заставила тебя волноваться, [n.say_name].")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Я слишком чувствительна к проблемам со здоровьем.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="В моей возрастной группе нельзя игнорировать эти проблемы.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Все в порядке, бабушка.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Лучше быть в безопасности, чем потом сожалеть, верно?")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Вот именно!")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Кстати, как сейчас себя чувствует твоя кожа?")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Я знаю, что мы немного отвлеклись от применения лосьона.")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Моя кожа чувствует себя хорошо и гладко!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="И я совсем не чувствую зуда!")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Если тебе понравилось использовать его, то купи бутылку для себя.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Они делают бутылки больших размеров.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Круто.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="...")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Я только что вспомнила, что мне нужно уехать по делам.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Так что тебе лучше вернуться домой.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Хорошо, Бабушка.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Я могу прийти снова?")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Непременно!")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Это всегда хороший день, когда мой внук приходит!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Для меня тоже, когда я вижу тебя бабушка!")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="(Мхм, что я знаю, это правда для тебя)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Пока, бабушка, люблю тебя!")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Я тоже тебя люблю, [n.say_name]!")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Скоро увидимся!")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (edna, appearance="pose handclasp face neutral blush false", text="...{p}...")
    call process_character (edna, appearance="pose handhip face embarrassed blush false", text="(Что на меня нашло?)")
    call process_character (edna, appearance="pose handhip face embarrassed blush false", text="(Внезапно меня разбудили мысли о члене [n.say_name]!)")
    call process_character (edna, appearance="pose handhip face embarrassed blush false", text="...")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="(Я не знала, что в моем теле осталось столько сексуального желания!)")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="...")
    call process_character (edna, appearance="pose handclasp face curious blush false", text="(Как я должна справиться с этой ситуацией с [n.say_name]?)")
    call process_character (edna, appearance="pose handclasp face curious blush false", text="...{p}...")
    call process_character (edna, appearance="pose handhip face happy blush false", text="(Тайная интрижка с моим внуком действительно звучит захватывающе!)")
    call process_character (edna, appearance="pose handhip face happy blush false", text="...")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="(Хотя придётся держать его в тени)")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="...")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="(Это будет нелегко)")


    python:
        edna.revistable_scenes.add("edna_scene_nate_naked_revisit")

        if not dream:
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)

    call process_end_of_scene ("edna_scene_nate_naked", char=edna, dream=dream)

    return

label edna_scene_topless(dream=False):
    call edna_scene_topless_sex (dream=dream)

    return

label edna_scene_topless_sex(dream=False):
    call process_scene_beginning (bg="bg edna_house_daytime", dream=dream )
    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (edna, "outfit clothes pose handhip face neutral blush false mouth red") ])

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Привет, Бабушка!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Я, как раз, думала о том, собираешься ли ты посетить меня сегодня, [n.say_name]!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="И вуаля, ты здесь!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Вовремя, да?")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Лучше и быть не могло.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Я хотела поговорить с тобой.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Речь идет о чем-то очень важном.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Да ну?")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Почему бы нам не прогуляться по пляжу вместе?")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Это хорошо быть вне дома весь день!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Хорошо, что я взял с собой плавки!")

    call process_new_location ("bg beach_daytime", dream=dream)
    $ display_multiple_characters([ (n, "outfit swimsuit pose handsdown face neutral blush false"), (edna, "outfit swimsuit pose handhip face neutral blush false mouth red hat sunhat") ])

    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false", text="(Похоже, я смогу поговорить об этом, чтобы никто не услышал нас)")
    call process_character (edna, appearance="outfit swimsuit pose handhip face embarrassed blush false", text="(Я думаю, что я немного сумасшедшая, чтобы думать об этом...)")
    call process_character (n, appearance="outfit swimsuit pose behindhead face neutral blush false", text="О чем важном ты хотела поговорить, Бабушка?")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Прежде чем я что-то скажу, я хочу, чтобы ты знал, что это конфиденциально между нами.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Только наши уши должны слышать то, о чем мы говорим.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Хорошо, конечно, Бабушка!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false", text="{i}Уфф,{/i} хорошо...")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false", text="Я думала о том, чего мне не хватало в моей жизни, когда я стала старше.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false", text="И есть один аспект, который я хотела бы вернуть.")
    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false", text="Почему он пропал?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false", text="Потому что долгое время я думала, что когда ты достигаешь определенного возраста, ты должен отказаться от этого.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false", text="Это было бы похоже...{w=1.0}если ты почувствовал, что должен отказаться от видеоигр после достижения определенного возраста.")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face concerned blush false", text="Отказаться от видеоигр?!")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face concerned blush false", text="Я бы никогда этого не сделал!")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face concerned blush false", text="Не до тех пор, пока я жив!")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false", text="Это именно то, что я чувствую по поводу того, от чего я отказалась много лет назад.")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false", text="Теперь я понимаю, что для этого не было причин.")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false", text="Мой возраст не должен диктовать, что я могу, а что нет.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false", text="Я выгляжу старше, но не чувствую себя старше.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false", text="Я все еще хочу участвовать в вещах, которые делают люди вдвое моложе меня.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false", text="Разве это имеет смысл?")
    call process_character (n, appearance="outfit swimsuit pose handfist face neutral blush false", text="В этом есть смысл, Бабушка, да!")
    call process_character (n, appearance="outfit swimsuit pose handfist face neutral blush false", text="Ты не хочешь пропустить интересные вещи из-за возраста!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false", text="Это мой проницательный внук!")
    call process_character (n, appearance="outfit swimsuit pose behindhead face neutral blush false", text="Что именно ты хотела вернуть?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false", text="Я хочу чувствовать больше возбуждения и разжечь свою сексуальность.")

    if stats.stat_value("times_had_sex") > 0 or stats.stat_value('times_received_blowjob') > 0:
        call process_character (n, appearance="pose behindhead face curious blush false", text="В-возбуждения?")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Ты имеешь в виду, как я себя чувствую, когда мой пенис становится твердым?")
        call process_character (edna, appearance="pose fisthip face neutral blush false", text="Тебе нравится это чувство, не так ли?")
    else:

        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Что ты имеешь в виду?")
        call process_character (edna, appearance="pose handclasp face embarrassed blush false", text="(Да Боже мой, он не понимает!)")
        call process_character (edna, appearance="pose handclasp face embarrassed blush false", text="(Мне нужно сказать более понятно...)")
        call process_character (edna, appearance="pose handclasp face embarrassed blush false", text="...")
        call process_character (edna, appearance="pose fisthip face neutral blush false", text="[n.say_name], ты знаешь, как ты получал эрекции в последнее время?")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="Д-да.")
        call process_character (edna, appearance="pose fisthip face neutral blush false", text="Тебе нравится это чувство?")

    call process_character (n, appearance="outfit swimsuit pose handsdown face curious blush false", text="Мне приятно...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face curious blush false", text="Ты знаешь, почему они появляются возле меня?")

    if stats.stat_value("times_had_sex") > 0 or stats.stat_value('times_received_blowjob') > 0:
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Д-да, понимаю...")
        call process_character (edna, appearance="pose handhip face neutral blush false", text="Все в порядке, ты можешь сказать мне.")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="Это потому, что мне нравится смотреть на тебя, бабушка.")
        call process_character (edna, appearance="pose handclasp face neutral blush false", text="Тебе нравится смотреть на некоторые части меня?")
    else:
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Я... я думаю, что да.")
        call process_character (edna, appearance="pose handhip face neutral blush false", text="Все в порядке, ты можешь сказать мне.")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="Это случается, когда я смотрю на некоторые твои части, Бабушка.")
        call process_character (edna, appearance="pose handclasp face neutral blush false", text="На что бы ты хотел посмотреть?")

    call process_character (n, appearance="outfit swimsuit pose handsdown face curious blush false", text="...{p}...")
    call process_character (n, appearance="outfit swimsuit pose handsdown face curious blush false", text="Г-грудь.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false", text="(Он был очень честен)")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false", text="Когда видишь меня в купальнике...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false", text="Тебе нравится, потому что ты видишь много моей груди?")
    call process_character (n, appearance="outfit swimsuit pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit swimsuit pose behindhead face concerned blush false", text="Ммм...")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false", text="Ну, я хочу сказать тебе, [n.say_name]...")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face flirt blush false", text="Мне понравилось смотреть на твой пенис на днях.")
    call process_character (n, appearance="outfit swimsuit pose handsdown face curious blush false", text="Да?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face flirt blush false", text="Это взволновало меня так же, как ты возбуждаешься, глядя на мою грудь.")
    call process_character (n, appearance="outfit swimsuit pose handsdown face concerned blush false", text="Так...")
    call process_character (n, appearance="outfit swimsuit pose handsdown face concerned blush false", text="Тебе тоже нравится на меня смотреть, бабушка?")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false", text="Вот почему я чувствую, что мы можем помочь друг другу.")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false", text="Мы вместе осуществим наши возбуждения.")
    call process_character (n, appearance="outfit swimsuit pose behindhead face concerned blush false", text="Как именно мы это сделаем?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face flirt blush false", text="Я тебе покажу...")

    call character_leave_dissolve (edna)
    pause 0.5

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadein = 1.0)

    call process_character (edna, appearance="outfit topless_swimsuit pose handclasp face flirt blush false")

    call process_character (n, appearance="outfit swimsuit pose twohandfist face embarrassed blush true", text="!!")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face embarrassed blush true", text="Б-бабушка!")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face embarrassed blush true", text="Т-ты сняла...")
    call process_character (edna, appearance="outfit topless_swimsuit pose handclasp face happy blush false", text="Ты ведь хотел их увидеть, не так ли?")
    call process_character (edna, appearance="outfit topless_swimsuit pose handclasp face happy blush false", text="Теперь они больше не остаются в твоём воображении.")
    call process_character (n, appearance="outfit swimsuit_hard pose behindhead face embarrassed blush true", text="(Я не могу поверить, что вижу сиськи моей бабушки!)")
    call process_character (n, appearance="outfit swimsuit_hard pose behindhead face embarrassed blush true", text="(Они даже больше, чем я думал!)")
    call process_character (edna, appearance="outfit topless_swimsuit pose fisthip face flirt blush false", text="(Он смотрит прямо на мою грудь)")
    call process_character (edna, appearance="outfit topless_swimsuit pose fisthip face flirt blush false", text="(И его член твердый!)")
    call process_character (edna, appearance="outfit topless_swimsuit pose fisthip face flirt blush false", text="(Это меня возбуждает!)")
    call process_character (edna, appearance="outfit topless_swimsuit pose fisthip face flirt blush false", text="...")
    call process_character (edna, appearance="outfit topless_swimsuit pose handhip face flirt blush false", text="Теперь покажи мне свою часть, [n.say_name].")
    call process_character (n, appearance="outfit swimsuit_hard pose handsdown face curious blush true", text="...{p}...")
    call process_character (n, appearance="outfit swimsuit_hard pose handsdown face curious blush false", text="Надеюсь, нас никто не увидит...)")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (n, appearance="outfit nudehard pose behindhead face curious blush true", text="...")
    call process_character (edna, appearance="outfit topless_swimsuit pose handclasp face flirt blush true", text="О, да!")
    call process_character (edna, appearance="outfit topless_swimsuit pose handclasp face flirt blush true", text="Ты понимаешь, о чем я говорю, [n.say_name]?")
    call process_character (edna, appearance="outfit topless_swimsuit pose handclasp face flirt blush true", text="Мы потакаем своим желаниям!")
    call process_character (n, appearance="outfit nudehard pose handsdown face embarrassed blush true", text="...")
    call process_character (n, appearance="outfit nudehard pose handsdown face embarrassed blush true", text="Кажется, я понимаю...")
    call process_character (edna, appearance="outfit topless_swimsuit pose handhip face happy blush true", text="Ты надеялся, что моя грудь будет выглядеть именно так?")
    call process_character (n, appearance="outfit nudehard pose twohandfist face flirt blush true", text="Она на самом деле намного лучше, чем я думал!")
    call process_character (edna, appearance="outfit topless_swimsuit pose handhip face happy blush true", text="...")
    call process_character (edna, appearance="outfit topless_swimsuit pose handhip face happy blush true", text="(Его член выглядит готовым к действию!)")
    call process_character (edna, appearance="outfit topless_swimsuit pose handhip face happy blush true", text="(Хотела бы я прочитать, что у [n.say_name] на уме)")
    call process_character (edna, appearance="outfit topless_swimsuit pose handclasp face flirt blush true", text="(Он думает, что он может сделать с моей грудью?)")
    call process_character (edna, appearance="outfit topless_swimsuit pose handclasp face flirt blush true", text="(Хочет ли он играть с ними или пойти еще дальше...)")
    call process_character (n, appearance="outfit nudehard pose twohandfist face embarrassed blush true", text="Кажется, я кого-то вижу!")
    call process_character (edna, appearance="outfit topless_swimsuit pose handclasp face shock blush true", text="Ох, быстро!")

    $ clear_characters()
    with Dissolve(0.25)
    pause 1.0

    $ display_multiple_characters([ (n, "outfit swimsuit_hard pose behindhead face curious blush false"), (edna, "outfit swimsuit pose fisthip face neutral blush false mouth red hat sunhat") ])

    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="Это было близко.")
    call process_character (n, appearance="outfit swimsuit_hard pose behindhead face curious blush false", text="Да...")
    call process_character (n, appearance="outfit swimsuit_hard pose behindhead face curious blush false", text="Не думаю, что они нас видели.")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false", text="Это то, чего мне не хватало в моей жизни...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face flirt blush false", text="Это чувство страсти и желания.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face flirt blush false", text="Оно слишком долго было в бутылке, и мне нужно его выпустить.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face flirt blush false", text="Но мне понадобится твоя помощь, [n.say_name]...")
    call process_character (n, appearance="outfit swimsuit_hard pose handsdown face concerned blush false", text="Моя помощь?")
    call process_character (n, appearance="outfit swimsuit_hard pose handsdown face concerned blush false", text="...")
    call process_character (n, appearance="outfit swimsuit_hard pose handsdown face curious blush false", text="Думаешь, я справлюсь, бабушка?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false", text="Ты уже показал, что можешь, [n.say_name]!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false", text="Возбуждение, которое я почувствовала мгновение назад, было электризующим!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false", text="И я хочу этого еще больше!")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false", text="Хотя… моя квартира лучше подойдет нам в будущем.")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face flirt blush false", text="Там должно быть для нас более конфиденциальности...")


    python:
        edna.revistable_scenes.add("edna_scene_topless_revisit")

        if not dream:
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_big_breasts", 1)
            stats.add_stat("times_had_erection", 1)

    call process_end_of_scene ("edna_scene_topless", char=edna, dream=dream)

    return

label edna_scene_bottomless(dream=False):
    call edna_scene_bottomless_sex (dream=dream)

    return

label edna_scene_bottomless_sex(dream=False):
    call process_scene_beginning (bg=edna_house, dream=dream )

    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Ты дома, Бабушка?")
    call process_character (edna, appearance="", text="Я в ванной комнате, [n.say_name]!")
    call process_character (edna, appearance="", text="Просто красила ногти!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="...")

    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false mouth red")

    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Хорошо выглядишь сегодня, Бабушка!")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Так я не всегда хорошо выгляжу?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="О-ох, я не это имел в виду...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Ты хорошо выглядишь каждый день, Бабушка!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Ха-ха, я просто шучу!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Я знала, что ты имеешь в виду.")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Спасибо тебе.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Как ты думаешь, моя помада и ногти делают меня более привлекательной?")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Я думаю, что они делают, да!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Если мой внук так говорит, значит это правда!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="[k.say_name] и [sa.say_name] не носят макияж, как ты.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Все по-разному относятся к макияжу.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Про [k.say_name] это понятно из-за ее легкой атлетики.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Любой макияж будет бежать сразу от пота!")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="И твоя сестра [sa.say_name] возможно, еще не совсем поняла значение макияжа.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Я думаю, что она в конце концов поймёт.")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Она ухаживает за своими великолепными золотыми волосами, так что твоя сестра-близнец заботится о том, как она выглядит!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Я до сих пор не знаю, как она справляется с таким количеством волос.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Я бы не смог этого сделать.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Когда станешь старше, ты будешь заботиться гораздо больше о том, сколько волос у тебя на голове.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Или то, что от них осталось, ха-ха!")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="К счастью, мои волосы сохранили свою первоначальную толщину.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Я могу жить со смесью серого в обмен.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Интересно, когда мои волосы поседеют...")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Чем больше ты думаешь об этом, тем больше вероятность, что это произойдет раньше!")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Вот почему ты не думаешь так много о том, сколько тебе лет.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Другие люди останавливаются на этом, и, конечно же, они стареют быстрее.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Вот во, что я верю.")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Бьюсь об заклад, именно поэтому ты до сих пор так хорошо выглядишь, Бабушка!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Я думаю, что ты прав!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Я знаю, что ты очень наблюдателен, [n.say_name], и мне было просто любопытно...")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false", text="Как много ты знаешь о женской анатомии?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Женская анатомия?")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false", text="Ты знаешь о груди, или сиськах, как ты их называешь, не так ли?")
    call process_character (edna, appearance="outfit clothes pose fisthip face curious blush false", text="Но знаешь ли ты о чем-то еще?")

    if stats.stat_value('times_seen_vagina') > 0 or stats.stat_value('times_had_vaginal_sex') > 0:
        call process_character (n, appearance="pose handpocket face curious blush false", text="...")
        call process_character (n, appearance="pose handpocket face curious blush false", text="Ну, я знаю кое-что о другой части.")
        call process_character (edna, appearance="pose fisthip face neutral blush false", text="Вагина?")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="Да.")
        call process_character (edna, appearance="pose handhip face curious blush false", text="Ты когда-нибудь видел её лично?")
        call process_character (n, appearance="pose handpocket face curious blush false", text="...")
        call process_character (n, appearance="pose handpocket face curious blush false", text="Да...")
        call process_character (edna, appearance="pose handhip face happy blush false", text="О, боже...")
        call process_character (edna, appearance="pose handhip face happy blush false", text="Похоже, мой внук не так невинен, как я думала.")
        call process_character (n, appearance="pose handpocket face concerned blush false", text="...")
        call process_character (n, appearance="pose handpocket face concerned blush false", text="Почему ты спрашиваешь, Бабушка?")
        call process_character (edna, appearance="pose handclasp face flirt blush false", text="Мне было интересно, хочешь ли ты взглянуть на мою.")
        call process_character (n, appearance="pose behindhead face embarrassed blush false", text="Т-твою, Бабушка?")
        call process_character (edna, appearance="pose handclasp face flirt blush false", text="Не понимаю, почему бы и нет.")
        call process_character (edna, appearance="pose handclasp face flirt blush false", text="В конце концов, я имела честь увидеть твой пенис.")
        call process_character (edna, appearance="pose handhip face flirt blush false", text="Так что тебе должно быть позволено увидеть каждую частичку меня...")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
    else:
        call process_character (n, appearance="pose handpocket face curious blush false", text="...")
        call process_character (n, appearance="pose handpocket face curious blush false", text="Я не уверен.")
        call process_character (edna, appearance="pose fisthip face neutral blush false", text="Ты знаешь, что такое влагалище?")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="Вроде того.")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="Но я никогда его не видел.")
        call process_character (edna, appearance="pose handhip face curious blush false", text="О, разве нет?")
        call process_character (edna, appearance="pose handhip face curious blush false", text="Даже в образовательных целях?")
        call process_character (n, appearance="pose handpocket face curious blush false", text="Мне так не кажется.")
        call process_character (edna, appearance="pose handhip face neutral blush false", text="Понятно.")
        call process_character (edna, appearance="pose handhip face neutral blush false", text="Я все равно не ожидала, что ты знаешь об этой части женского тела.")
        call process_character (edna, appearance="pose handhip face neutral blush false", text="...{p}...")
        call process_character (edna, appearance="pose handclasp face flirt blush false", text="Ты бы хотел увидеть?")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="Прямо сейчас?")
        call process_character (edna, appearance="pose handclasp face flirt blush false", text="Прямо сейчас, да.")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
        call process_character (n, appearance="pose behindhead face embarrassed blush false", text="Ты покажешь мне, Бабушка?")
        call process_character (edna, appearance="pose fisthip face flirt blush false", text="Не понимаю, почему бы и нет.")
        call process_character (edna, appearance="pose fisthip face flirt blush false", text="В конце концов, я имела честь увидеть твой пенис.")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="...")

    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Вы готовы к представлению?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Д-да.")
    call process_character (edna, appearance="outfit clothes pose handclasp face flirt blush false", text="(Я не могу вспомнить последний раз, когда я показывала мою киску!)")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="(Единственный раз, когда я могу вспомнить, когда это случайно произошло, поправляя мой купальник на пляже...)")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="(Но специально для кого-то другого?)")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="(Давно это было!)")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Хорошо, давай начнём!")

    call character_leave_dissolve (edna)
    pause 0.5

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Suave Standpipe.ogg", fadein = 1.0)

    call process_character (edna, appearance="outfit underwear_bottomless pose fisthip face happy blush false", text="Та-да!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face embarrassed blush false", text="(Она действительно показывает!)")
    call process_character (edna, appearance="outfit underwear_bottomless pose fisthip face flirt blush false", text="(Его глаза говорят мне все, что мне нужно знать...)")
    call process_character (edna, appearance="outfit underwear_bottomless pose fisthip face flirt blush false", text="(Он в восторге от моей киски даже издалека)")
    call process_character (edna, appearance="outfit underwear_bottomless pose fisthip face flirt blush false", text="...")
    call process_character (edna, appearance="outfit underwear_bottomless pose handhip face curious blush false", text="(Почему он должен быть далеко?)")
    call process_character (edna, appearance="outfit underwear_bottomless pose handhip face flirt blush false", text="Подойди ближе, [n.say_name].")
    call process_character (edna, appearance="outfit underwear_bottomless pose handhip face flirt blush false", text="Ты должен увидеть это вблизи...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Можно?")
    call process_character (edna, appearance="outfit underwear_bottomless pose handclasp face happy blush false", text="У тебя есть мое полное разрешение.")

    $ clear_characters()
    with Dissolve(0.5)

    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face concerned blush false position nate_edna_pussy_level_nate"), (edna, "outfit underwear_bottomless pose handhip face flirt blush false position nate_edna_pussy_level_edna") ])
    with Dissolve(0.5)

    call process_character (edna, appearance="outfit underwear_bottomless pose handhip face flirt blush false", text="Теперь гораздо лучший обзор.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush true", text="Д-да...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush true", text="Я вижу.")
    call process_character (edna, appearance="outfit underwear_bottomless pose handhip face flirt blush false", text="...")
    call process_character (edna, appearance="outfit underwear_bottomless pose handhip face flirt blush false", text="(Я возбуждаюсь, просто наблюдая, как [n.say_name] смотрит на мою киску!)")
    call process_character (edna, appearance="outfit underwear_bottomless pose handhip face flirt blush false", text="(У меня есть желание засунуть его лицо в мою промежность!)")
    call process_character (edna, appearance="outfit underwear_bottomless pose handhip face flirt blush false", text="...")
    call process_character (edna, appearance="outfit underwear_bottomless pose handclasp face neutral blush false", text="(Но я не хочу забегать вперед)")
    call process_character (edna, appearance="outfit underwear_bottomless pose handclasp face neutral blush false", text="(Если ему не понравится, я потеряю дружбу с ним)")
    call process_character (edna, appearance="outfit underwear_bottomless pose handclasp face neutral blush false", text="...")
    call process_character (edna, appearance="outfit underwear_bottomless pose fisthip face embarrassed blush false", text="(Неужели я хотела бы зарыть лицо моего внука в своей киске?)")
    call process_character (edna, appearance="outfit underwear_bottomless pose fisthip face embarrassed blush false", text="(Это те мысли, которые я получаю, когда я возбуждена!)")
    call process_character (edna, appearance="outfit underwear_bottomless pose fisthip face neutral blush false", text="(Нет пределов, даже с моим внуком!)")
    call process_character (edna, appearance="outfit underwear_bottomless pose fisthip face neutral blush false", text="...")
    call process_character (edna, appearance="outfit underwear_bottomless pose handhip face flirt blush false", text="(Нет сомнений, что я соблазняю сына своей дочери...)")
    call process_character (edna, appearance="outfit underwear_bottomless pose handhip face flirt blush false", text="(Это порочно для бабушки делать что-то подобное!)")
    call process_character (edna, appearance="outfit underwear_bottomless pose handhip face flirt blush false", text="(Но [n.say_name] не отступает)")
    call process_character (edna, appearance="outfit underwear_bottomless pose handhip face flirt blush false", text="(И я становлюсь все более и более возбужденной...)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush true", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush true", text="У тебя здесь много волос, бабушка.")
    call process_character (edna, appearance="outfit underwear_bottomless pose handclasp face neutral blush false", text="Да.")
    call process_character (edna, appearance="outfit underwear_bottomless pose handclasp face neutral blush false", text="Я там почти не бреюсь.")
    call process_character (edna, appearance="outfit underwear_bottomless pose handclasp face happy blush false", text="У меня почти нет волос на теле, кроме моей киски!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face aroused blush true", text="Мне нравятся все эти волосы.")
    call process_character (edna, appearance="outfit underwear_bottomless pose fisthip face neutral blush false", text="Я думаю, что все женщины должны иметь хотя бы немного волос.")
    call process_character (edna, appearance="outfit underwear_bottomless pose fisthip face neutral blush false", text="Я никогда не была поклонником эпиляции.")
    call process_character (edna, appearance="outfit underwear_bottomless pose fisthip face happy blush false", text="Наверное, я просто старомодна!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face aroused blush true", text="...{p}...")

    $ clear_characters()
    with Dissolve(0.5)

    $ display_multiple_characters([ (n, "outfit clothesjacket_hard pose handpocket face aroused blush true position right"), (edna, "outfit underwear_bottomless pose handclasp face curious blush false position left") ])



    call process_character (edna, appearance="outfit underwear_bottomless pose handclasp face curious blush false", text="О, ты закончил смотреть?")
    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face aroused blush true", text="Да...")
    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face aroused blush true", text="Спасибо, что показала мне свою вагину, Бабушка.")
    call process_character (edna, appearance="outfit underwear_bottomless pose handclasp face flirt blush false", text="Всегда пожалуйста, [n.say_name].")
    call process_character (edna, appearance="outfit underwear_bottomless pose handclasp face flirt blush false", text="(У него жесточайший стояк)")
    call process_character (edna, appearance="outfit underwear_bottomless pose handclasp face flirt blush false", text="(Посмотрите, какой он твёрдый...)")
    call process_character (edna, appearance="outfit underwear_bottomless pose handclasp face flirt blush false", text="...")
    call process_character (edna, appearance="outfit underwear_bottomless pose fisthip face happy blush false", text="Если ты когда-нибудь захочешь еще раз взглянуть, все, что тебе нужно сделать, это спросить!")
    call process_character (n, appearance="outfit clothesjacket_hard pose twohandfist face aroused blush true", text="...")
    call process_character (n, appearance="outfit clothesjacket_hard pose twohandfist face aroused blush true", text="Мне придется потереть пенис, когда я вернусь домой...)")


    python:
        edna.revistable_scenes.add("edna_scene_bottomless_revisit")

        if not dream:
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_had_erection", 1)

    call process_end_of_scene ("edna_scene_bottomless", char=edna, dream=dream)

    return

label edna_scene_naked(dream=False):
    call edna_scene_naked_sex (dream=dream)

    return

label edna_scene_naked_sex(dream=False):
    call process_scene_beginning (bg="bg edna_house_daytime", dream=dream )
    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (edna, "outfit clothes pose handclasp face neutral blush false mouth red") ])

    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false")

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Привет, Бабушка.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Ты собираешься уходить?")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Извини, [n.say_name], но да.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Я вызвалась курировать большую продажу выпечки в общественном центре.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Ням, распродажа выпечки!")
    call process_character (edna, appearance="outfit clothes pose handhip face concerned blush false", text="Это будет тяжело для меня, потому что другой человек, который собирался помочь, заболел и не может этого сделать.")
    call process_character (edna, appearance="outfit clothes pose handhip face concerned blush false", text="Так что это будет две работы в одной.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Это звучит жестко, Бабушка.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="С тобой все будет в порядке?")
    call process_character (edna, appearance="outfit clothes pose handclasp face concerned blush false", text="Я знаю, что буду уставшей к тому времени, как все закончится.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Эй, я могу с этим помочь?")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Ах ты, [n.say_name]?!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Ты поможешь мне выбраться из серьезной передряги.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Что ты хочешь, чтобы я сделал?")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Ты можешь собирать платежи от людей, которые покупают вещи на распродаже.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Все стоит один доллар, так что просто помни об этом.")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Понял!")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Давайте пошли!")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="Нам нужно все подготовить заранее.")

    call fade_to_black (1)
    call process_new_location ("bg edna_house_daytime", dream=dream)
    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (edna, "outfit clothes pose handclasp face happy blush false mouth red") ])

    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Я не ожидала, что будет столько человек!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Я знаю!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Это было безумие!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Мы буквально продали каждую вещь.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="[n.say_name], я не знаю, как бы я выжила без тебя!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Жаль, что ничего не осталось...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Я хотел купить что-нибудь.")
    call process_character (edna, appearance="outfit clothes pose handclasp face concerned blush false", text="Ай...")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Я всегда могу испечь тебе партию печенья, если хочешь!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Правда?!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Спасибо, Бабушка!")
    call process_character (edna, appearance="outfit clothes pose handhip face curious blush false", text="Ты хочешь кусочки шоколада в них тоже?")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Да, это мое любимое блюдо!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Это меньшее, что я могу для тебя сделать, [n.say_name].")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Ты не обязан был помогать.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Я не думал, что это справедливо, что тебе пришлось делать всю эту работу в одиночку.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face happy blush false", text="Кроме того, я думал, что это было весело собирать платежи от всех!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Хаха!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Некоторые из жителей кондоминиума думали, что это было очень мило, что мой внук помогал мне.")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="Они сказали, что ты был очень вежлив.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Что будет со всеми деньгами, поступившими с продажи?")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Пойдут на местный благотворительный фонд.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Каждый месяц продажи идут на разные.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Это очень популярно, как ты видел.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false", text="Люди получают вкусные угощения, и это идет на благое дело.")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Так что это беспроигрышный вариант!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false", text="Так и есть!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Как ты думаешь, ты можешь приготовить это печенье прямо сейчас, бабушка?")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Не удивительно, что ты хочешь их после того, как продал кучу!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="Я начну готовить.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false", text="...{p}...")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false", text="Думаю, я также назначу особую награду за это печенье.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Особая награда?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face happy blush false", text="Мне нравится, как это звучит!")
    call process_character (edna, appearance="outfit clothes pose handclasp face flirt blush false", text="Думаю, тебе очень понравится...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="(Интересно, что это может быть!)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="(Может быть, бабушка добавит еще один ингредиент в печенье!)")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="(Да, это должно быть так!)")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="(Может быть, это кусочки арахисового масла?)")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="(Белые шоколадные чипсы также были бы потрясающими!)")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false", text="(Я не думаю, что [n.say_name] понял, что я имела в виду под специальной наградой...)")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false", text="(Но думаю, что он получит подсказку через мгновение)")

    call character_leave_dissolve (edna)
    pause 0.5

    call process_character (edna, appearance="outfit underwear pose handhip face neutral blush false")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="А?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Почему ты сняла одежду, Бабушка?")
    call process_character (edna, appearance="outfit underwear pose handhip face flirt blush false", text="Это твоя особая награда, [n.say_name].")
    call process_character (edna, appearance="outfit underwear pose handhip face flirt blush false", text="Личный стриптиз.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Стриптиз?")
    call process_character (edna, appearance="outfit underwear pose fisthip face flirt blush false", text="Какую часть я сниму первой, [n.say_name]?")
    call process_character (edna, appearance="outfit underwear pose fisthip face flirt blush false", text="Мой лифчик или трусики?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="У меня есть право выбора?")
    call process_character (edna, appearance="outfit underwear pose fisthip face happy blush false", text="Это не зря называется личным стриптизом!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...")

    $ edna_scene_naked_bra_off_first = False
    menu:
        "Сними лифчик первым, Бабушка.":
            call process_character (edna, appearance="pose handclasp face happy blush false", text="Хотела бы я, чтобы для этого играла музыка!")
            call process_character (edna, appearance="pose handclasp face happy blush false", text="Хороший стриптиз нуждается в саундтреке, на мой взгляд.")
            call process_character (n, appearance="pose handpocket face neutral blush false", text="Я не против, если не будет музыки.")
            call process_character (edna, appearance="pose handhip face happy blush false", text="Тогда мне этого достаточно!")
            call process_character (edna, appearance="pose handhip face happy blush false", text="...")
            call process_character (edna, appearance="pose handhip face flirt blush false", text="Хорошо, ты готов к большому раскрытию?")
            call process_character (edna, appearance="pose handhip face flirt blush false", text="Раз...")
            call process_character (edna, appearance="pose handhip face flirt blush false", text="Два...")

            call character_leave_dissolve (edna)
            pause 0.5

            python hide:
                if not dream or persistent.disable_dream_music:
                    play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

            call process_character (edna, appearance="outfit topless_underwear pose fisthip face happy blush false", text="Вуаля!")
            $ edna_scene_naked_bra_off_first = True
        "Сними трусики первыми, Бабушка.":
            call process_character (edna, appearance="pose handclasp face happy blush false", text="Хотела бы я, чтобы для этого играла музыка!")
            call process_character (edna, appearance="pose handclasp face happy blush false", text="Хороший стриптиз нуждается в саундтреке, на мой взгляд.")
            call process_character (n, appearance="pose handpocket face neutral blush false", text="Я не против, если не будет музыки.")
            call process_character (edna, appearance="pose handhip face happy blush false", text="Тогда мне этого достаточно!")
            call process_character (edna, appearance="pose handhip face happy blush false", text="...")
            call process_character (edna, appearance="pose handhip face flirt blush false", text="Хорошо, ты готов к большому раскрытию?")
            call process_character (edna, appearance="pose handhip face flirt blush false", text="Раз...")
            call process_character (edna, appearance="pose handhip face flirt blush false", text="Два...")

            call character_leave_dissolve (edna)
            pause 0.5

            python hide:
                if not dream or persistent.disable_dream_music:
                    play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

            call process_character (edna, appearance="outfit underwear_bottomless pose fisthip face happy blush false", text="Вуаля!")
            $ edna_scene_naked_bra_off_first = False

    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Мне понравилось это, Бабушка!")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Шоу еще не закончилось!")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Теперь мы на втором акте!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="(Это будет первый раз, когда бабушка полностью обнажится...)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="(Я надеялся, что это произойдет!)")
    call process_character (edna, appearance="pose handclasp face flirt blush false", text="...")
    call process_character (edna, appearance="pose handclasp face flirt blush false", text="(Это так порочно!)")
    call process_character (edna, appearance="pose handclasp face flirt blush false", text="(Я не думаю, что когда-нибудь смогу сделать это для кого-то другого, кроме [n.say_name])")
    call process_character (edna, appearance="pose handclasp face flirt blush false", text="...")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="(Он считает меня привлекательной, и он не осуждает мой возраст)")
    call process_character (edna, appearance="pose handhip face happy blush false", text="(Женщина не может просить лучшего мужчину, чем этот!)")
    call process_character (edna, appearance="pose handhip face happy blush false", text="...")

    if edna_scene_naked_bra_off_first:
        call process_character (edna, appearance="pose fisthip face flirt blush false", text="Я медленно сниму трусики, [n.say_name]...")
        call process_character (edna, appearance="pose fisthip face flirt blush false", text="Это наполняет тебя предвкушением?")
        call process_character (n, appearance="outfit clothesjacket_hard pose twohandfist face neutral blush false", text="Д-да!")
        call process_character (edna, appearance="pose handhip face flirt blush false", text="Почти...")
        call process_character (edna, appearance="pose handhip face flirt blush false", text="Иии...")
    else:
        call process_character (edna, appearance="pose fisthip face flirt blush false", text="Защелка бюстгальтера была расстёгнута, [n.say_name].")
        call process_character (edna, appearance="pose fisthip face flirt blush false", text="Все, что мне осталось сделать, это позволить ему упасть...")
        call process_character (n, appearance="outfit clothesjacket_hard pose twohandfist face neutral blush false", text="...")

    call character_leave_dissolve (edna)
    pause 0.5

    call process_character (edna, appearance="outfit nude pose fisthip face happy blush false", text="Теперь у тебя есть полный вид!")
    call process_character (n, appearance="outfit clothesjacket_hard pose twohandfist face happy blush false", text="За стриптизом было весело наблюдать, Бабушка!")
    call process_character (edna, appearance="outfit nude pose handclasp face flirt blush false", text="Ты ожидал такой особой награды?")
    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face happy blush false", text="Вовсе нет!")
    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face happy blush false", text="Я бы никогда не догадался!")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false", text="Приятно удивить внука!")
    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face neutral blush false", text="Привет, Бабушка...")
    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face neutral blush false", text="Ты собираешься печь печенье голышом?")
    call process_character (edna, appearance="outfit nude pose fisthip face neutral blush false", text="Я думала о том же самом, [n.say_name]!")
    call process_character (edna, appearance="outfit nude pose fisthip face neutral blush false", text="Это отличная идея, согласен?")
    call process_character (n, appearance="outfit clothesjacket_hard pose handfist face happy blush false", text="Определенно!")
    call process_character (edna, appearance="outfit nude pose fisthip face flirt blush false", text="(Его хер твёрд как камень, я могу сказать!)")
    call process_character (edna, appearance="outfit nude pose fisthip face flirt blush false", text="(Я не знаю, как он сопротивляется желанию дрочить прямо здесь!)")
    call process_character (edna, appearance="outfit nude pose fisthip face flirt blush false", text="...")
    call process_character (edna, appearance="outfit nude pose handhip face happy blush false", text="(Однажды я собираюсь принять окончательный шанс с ним)")
    call process_character (edna, appearance="outfit nude pose handhip face happy blush false", text="(Не так долго осталось)")
    call process_character (edna, appearance="outfit nude pose handhip face happy blush false", text="...")
    call process_character (edna, appearance="outfit nude pose fisthip face flirt blush false", text="(Я, наконец, могу получить свой шанс на его член...)")
    call process_character (edna, appearance="outfit nude pose fisthip face flirt blush false", text="...")
    call process_character (edna, appearance="outfit nude pose fisthip face neutral blush false", text="Ты должен стоять позади меня, когда я кладу печенье в духовку, [n.say_name].")
    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face neutral blush false", text="Почему бабушка?")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false", text="Я должна наклониться, чтобы положить печенье....")
    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face curious blush false", text="Н-наклониться?")

    call fade_to_black (1)
    call process_new_location ("bg edna_house_daytime", dream=dream)

    $ display_multiple_characters([ (n, "outfit clothesjacket pose twohandfist face happy blush false"), (edna, "outfit nude pose handhip face neutral blush false mouth red") ])

    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Аах, это печенье хорошее, Бабушка!")
    call process_character (edna, appearance="outfit nude pose handhip face happy blush false", text="Ничто не сравнится со свежеиспеченным печеньем!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Ты сказал это!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Спасибо, что сделала их, Бабушка!")
    call process_character (edna, appearance="outfit nude pose fisthip face neutral blush false", text="...")
    call process_character (edna, appearance="outfit nude pose fisthip face neutral blush false", text="(Представьте, что все эти люди на этой продаже выпечки видят [n.say_name] и меня вместе)")
    call process_character (edna, appearance="outfit nude pose fisthip face happy blush false", text="(Они понятия не имеют, что на самом деле происходит между нами)")
    call process_character (edna, appearance="outfit nude pose fisthip face happy blush false", text="(Это так захватывающе!)")

    python:
        edna.revistable_scenes.add("edna_scene_naked_revisit")

        if not dream:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_big_breasts", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_seen_vagina", 1)

    call process_end_of_scene ("edna_scene_naked", char=edna, dream=dream)

    return

label edna_scene_handjob:
    $ replace_position = True
    call process_scene_beginning (bg="bg kitchen_daytime" )
    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (k, "outfit clothes pose armsup face neutral blush false") ])
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Слышал хорошие новости, бро?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Какие новости?")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Ты же знаешь, что у нас есть джакузи со сломанным насосом?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="О да, я помню.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="С тех пор оно было под брезентом.")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="Ну ремонтник сегодня приезжал!")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="И я всё оплатила!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Ты имеешь в виду, что джакузи теперь работает?!")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="О да, бро!")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="Пузырьки и всё такое!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Это будет потрясающе!")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Я попробую сегодня вечером, когда будет прохладно.")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Ты знал, что в него встроены подводные лампочки?")
    call process_character (k, appearance="outfit clothes pose armsup face happy blush false", text="Мы провели отличную сделку, получив роскошную горячую ванну с домом!")

    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false")


    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false")

    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Мама!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Ты слышала про джакузи?!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Теперь оно работает!")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Да, я знаю!")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="[k.say_name] была очень рада рассказать мне!")

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false")


    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false")

    call process_character (si, appearance="outfit clothes pose armunder face curious blush false", text="Хотя механик запросил намного больше, чем я ожидала.")
    call process_character (si, appearance="outfit clothes pose armunder face curious blush false", text="Ты потратила всё, что заработала за лето, [k.say_name]?")

    $ k.position = "right"

    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Нет, все в порядке, Мам.")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Я работаю сверхурочно в фитнес-центре, и это покроет расходы.")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="Кроме того, я получаю деньги, когда предоставляю личные тренировки для клиентов!")
    call process_character (si, appearance="outfit clothes pose armunder face embarrassed blush false", text="Надеюсь, наш счет за электричество не взлетит до небес теперь, когда это джакузи работает.")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Тебе не придется беспокоиться об этом, Мама!")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="Оказывается, эта гидромассажная ванна работает от солнечной энергии!")
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="Насколько это круто звучит?!")
    call process_character (si, appearance="outfit clothes pose handsup face shocked blush false", text="Я даже и не знаю, [k.say_name]!")
    call process_character (si, appearance="outfit clothes pose handsup face shocked blush false", text="Это невероятно!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Солнечная?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Ты имеешь в виду, что он нагревается солнцем?")
    call process_character (si, appearance="outfit clothes pose handsfront face happy blush false", text="Ты хорошо информирован, [n.say_name]!")
    call process_character (si, appearance="outfit clothes pose handsfront face happy blush false", text="Это именно то, что оно делает!")
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Таким образом, счет за электричество вряд ли должен изменитсья.")

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false")


    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false")

    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Надеюсь на это.")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="С кондиционером и всей электроникой, используемой в доме, счет может стать большим!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Ты собираешься туда пойти, мама?")
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Я могу попробовать в когда-нибудь, милый.")
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Было бы неплохо окунуть в него ноги после работы в саду!")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Знаешь, кто бы сошел с ума из-за этого?")
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Бабушка.")
    call process_character (si, appearance="outfit clothes pose handsfront face happy blush false", text="Ох, неужели!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Мы должны спросить, не хочет ли она зайти!")
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Почему бы тебе не позвонить ей, [n.say_name]?")
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Я уверена, она хотела бы наконец увидеть наш новый дом!")

    call fade_to_black (1)


    call process_new_location ("bg backyard_daytime")

    $ display_multiple_characters([ (edna, "outfit clothes pose handclasp face happy blush false mouth red position left"), (si, "outfit clothes pose handsfront face neutral blush false position right") ])

    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Ваш дом прекрасен, [si.say_name].")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Мне нравится этот просторный задний двор!")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Спасибо, Мам!")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Здорово, что есть так много комната.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false mouth red", text="И на вершине всего этого ваш собственный бассейн!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false mouth red", text="Это как миниатюрный курорт!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="[sa.say_name] и я бываем там часто, бабушка!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="Я уверена, что да!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="У вас есть мгновенный доступ прямо из кухни!")

    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Наш задний двор, безусловно, полезен!")
    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Кто-нибудь всегда здесь есть днем.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="И я вижу этот чудесный сад неподалеку!")
    call process_character (si, appearance="outfit clothes pose armunder face happy blush false", text="Это битва за выживание, но я, кажется, выигрываю!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Мама делает много еды из овощей из сада для нас.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false mouth red", text="Звучит вкусно иметь свежий виноград!")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Кстати говоря, я собираюсь приготовить обед для всех нас.")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Это будет томатный бульон с овощным супом!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Звучит вкусно!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="Я полностью согласна.")

    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Мне нужно начать готовить его.")
    call process_character (si, appearance="outfit clothes pose armunder face neutral blush false", text="Мам, джакузи разогрелось, если ты хочешь им воспользоваться.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false mouth red", text="Не возражаешь, если я попробую?")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false mouth red", text="У меня немного болит тело после утренней прогулки, так что это пойдет на пользу моим суставам.")

    call character_leave_dissolve (si)
    pause 0.5

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false")

    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="Мне нравится, как у тебя и твоей сестры [sa.say_name] комнаты размещены.")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="Спальня [sa.say_name] выглядит как миниатюрная киностудия!")
    call process_character (edna, appearance="outfit clothes pose fisthip face curious blush false mouth red", text="Почему у нее камера и все это высокотехнологичное оборудование?")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Это для нашей онлайн-трансляции!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="[sa.say_name] и я играем в новейшие видеоигры, и люди в интернете могут смотреть на нас, пока мы играем!")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false mouth red", text="...")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false mouth red", text="Я совершенно запуталась.")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false mouth red", text="Кто те люди, которые могут наблюдать за тобой?")
    call process_character (edna, appearance="outfit clothes pose handclasp face curious blush false mouth red", text="Где они находятся?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="О, они могут быть откуда угодно!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Когда кто-то заходит на наш канал на ReflexViz.HD, они увидят [sa.say_name] и меня вживую!")
    call process_character (edna, appearance="outfit clothes pose handhip face curious blush false mouth red", text="...")
    call process_character (edna, appearance="outfit clothes pose handhip face curious blush false mouth red", text="Я стараюсь понять, что ты говоришь.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false mouth red", text="Значит, у тебя есть собственный телеканал?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Ммм...{w=1.0} примерно так.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Легко настроить свой собственный канал, но реальная проблема становится, когда набирается много подписчиков и зрителей!")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false mouth red", text="Поразительно...")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false mouth red", text="А я-то думала, что нужен бюджет в миллион долларов, чтобы сделать такое.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Теперь каждый может сделать это из собственного дома!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Ты даже можешь создать свой собственный канал, Бабушка!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="[sa.say_name] и я могли бы помочь настроить его!")
    call process_character (edna, appearance="outfit clothes pose fisthip face embarrassed blush false mouth red", text="Я откажусь от предложения.")
    call process_character (edna, appearance="outfit clothes pose fisthip face embarrassed blush false mouth red", text="Мне нравится держать моё лицо подальше от  камер.")
    call process_character (edna, appearance="outfit clothes pose handclasp face embarrassed blush false mouth red", text="Эти ужасные штуки делают тебя старше на десять лет!")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false mouth red", text="У меня нет...{w=0.5}как это называется?")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false mouth red", text="Онлайн штуки?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Ты имеешь в виду интернет, Бабушка?")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false mouth red", text="Да, это его.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false mouth red", text="У меня нет интернета в моей квартире, и я не очень заинтересована в его получении.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Ох.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="В этом случае да, ты не сможешь ничего транслировать.")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="Я оставлю это для тебя и твоей сестры!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Я готова наслаждаться вашей гидромассажной ванной, [n.say_name]!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Ты ведь присоединишься ко мне, верно?")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Я еще не был в нем, так что да!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="Ты должен посидеть рядом со мной.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Сидеть рядом с тобой?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Почему?")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false mouth red", text="Я просто хочу быть рядом со своим внуком.")
    call process_character (edna, appearance="outfit clothes pose handhip face flirt blush false mouth red", text="Мы можем быть очень близки...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...")

    $ replace_position = False
    call prompt_menu_boldness_check ("Конечно, я сяду рядом с тобой, Бабушка...", "Д-думаю, в этот раз я просто посижу на другой стороне...", "edna_scene_handjob", edna)

    return

label edna_scene_handjob_refusal(text, insufficient_points):
    if insufficient_points:
        call process_character (n, appearance="pose behindhead face curious blush true", text="Думаю, в этот раз я просто посижу на другой стороне...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="(Я знаю, что у меня была бы эрекция, если бы я сидел так близко к бабушке...)")
        call process_character (n, appearance="pose behindhead face curious blush false", text="(Ее сиськи были бы прямо у меня перед носом!)")

    call process_character (edna, appearance="pose handclasp face sad blush false", text="Ох, [n.say_name]?")
    call process_character (edna, appearance="pose handclasp face sad blush false", text="Мне здесь будет одиноко...")

    if edna in nate_room.characters:
        $ nate_room.characters.remove(edna)
        $ edna_house.characters.append(edna)
        $ edna.scene = ""
        $ edna.prompted_sceen = "edna_scene_handjob"
        $ nate_room.start()

    return

label edna_scene_handjob_sex(dream=False):
    call process_scene_beginning ("bg edna_hottub", dream=dream )
    pause
    $ no_bust_art = True
    call process_character (edna, appearance="blush false", text="О, теперь это очень мило!")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (edna, appearance="blush false", text="Тебе это нравится, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Сначала было немного жарковато...")
    call process_character (n, appearance="blush false", text="Но теперь так здорово, бабушка.")
    call process_character (edna, appearance="blush false", text="Это потому, что вода горячее, чем температура твоего тела.")
    call process_character (edna, appearance="blush false", text="Твое тело должно привыкнуть к этому.")
    call process_character (n, appearance="blush false", text="У тебя есть горячие ванны, где ты живёшь, Бабушка?")
    call process_character (edna, appearance="blush false", text="Знаешь, единственное, чего у них нет, это джакузи.")
    call process_character (edna, appearance="blush false", text="Я не могла поверить, когда спросила.")
    call process_character (n, appearance="blush false", text="Никаких гидромассажных ванн вообще?")
    call process_character (edna, appearance="blush false", text="До меня дошли слухи, что на базе отдыха строители неправильно рассчитали какие-то размеры.")
    call process_character (edna, appearance="blush false", text="В результате им пришлось отклонить горячие ванны.")
    call process_character (edna, appearance="blush false", text="Многие жители пытаются подтолкнуть руководство к реконструкции, чтобы на этот раз их включили.")
    call process_character (n, appearance="blush false", text="Жаль, что у тебя нет джакузи там.")
    call process_character (edna, appearance="blush false", text="Мне не нужно беспокоиться об этом сейчас, когда у меня есть своё собственное!")
    call process_character (n, appearance="blush false", text="Да!")
    call process_character (n, appearance="blush false", text="Ты можешь тусоваться со всеми нами, Бабушка!")
    call process_character (edna, appearance="blush false", text="Единственное, что могло бы сделать это лучше, если бы оно было закрыто.")
    call process_character (n, appearance="blush false", text="Почему так?")
    call process_character (edna, appearance="blush false", text="Тогда можно будет использовать его круглый год.")
    call process_character (edna, appearance="blush false", text="Зимой здесь может идти снег, но эта гидромассажная ванна была бы защищена от внешних воздействий.")
    call process_character (n, appearance="blush false", text="Это было бы супер круто!")
    call process_character (n, appearance="blush false", text="Снежинки падали, и мы наблюдали за ними, пока они нагревались в воде!")
    call process_character (edna, appearance="blush false", text="Разве это не красиво?")
    call process_character (edna, appearance="blush false", text="Может, ты спросишь свою маму об этом.")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (edna, appearance="blush false", text="Жара расслабляет, не так ли?")
    call process_character (n, appearance="blush false", text="Да...")
    call process_character (edna, appearance="blush false", text="Гидромассажная ванна отлично подходит для снятия напряжения.")
    call process_character (edna, appearance="blush false", text="Все боли уходят, когда я нахожусь в ней.")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (edna, appearance="blush false", text="Чувствуешь ли ты какое-либо напряжение, [n.say_name]?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Мне так не кажется...")
    call process_character (edna, appearance="blush false", text="Нет областей на теле, которые находятся в дискомфорте?")
    call process_character (n, appearance="blush false", text="Да вроде нет, Бабушка.")
    call process_character (edna, appearance="blush false", text="...{p}...")

    call static_still_ctc ("bg edna_legtouch_soft")

    call process_character (edna, appearance="blush false", text="Ты уверен, что нет ничего, чему может понадобиться...{w=1.0}внимание?")
    call process_character (n, appearance="blush false", text="Бабушка, твоя рука на моей ноге.")
    call process_character (edna, appearance="blush false", text="Я проверяю, есть ли у тебя здесь какие-нибудь проблемы.")
    call process_character (edna, appearance="blush false", text="В конце концов, ты очень активен в твоём возрасте.")
    call process_character (edna, appearance="blush false", text="Я не хочу, чтобы у тебя было растяжение мышц или шишки.")
    call process_character (n, appearance="blush false", text="{i}Угх.{/i}..")
    call process_character (n, appearance="blush false", text="(Бабушка держит руку так близко к моему пенису...)")
    call process_character (n, appearance="blush false", text="(В последний раз она держала руку так близко, когда втирала лосьон)")
    call process_character (n, appearance="blush false", text="(Она помнит, что произошло, когда она это сделала?)")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Ноги [n.say_name] ёрзают)")
    call process_character (edna, appearance="blush false", text="(У меня есть сильное подозрение, почему...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(О нет, я не могу остановить это!)")
    call process_character (n, appearance="blush false", text="(Я чувствую, что он становится все твёрже!)")

    call static_still_ctc ("bg edna_legtouch_hard")

    call process_character (edna, appearance="blush false", text="Ой...")
    call process_character (edna, appearance="blush false", text="Я чувствую напряжение.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Да, это очень заметно, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Он просто вспыхнул.")
    call process_character (n, appearance="blush false", text="Что ты имеешь в виду, Бабушка?")
    call process_character (n, appearance="blush false", text="Что вспыхнуло?")
    call process_character (edna, appearance="blush false", text="Это требует немедленного внимания.")
    call process_character (edna, appearance="blush false", text="Неразумно оставлять всё так.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Т-ты имеешь в виду мой...")

    if not dream or persistent.disable_dream_music:
        $ play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

    call static_still_ctc ("bg edna_underwater_jerk")

    call process_character (edna, appearance="blush false", text="Позволь мне дать тебе облегчение...")
    call process_character (n, appearance="blush false", text="Ха, ах!")
    call process_character (edna, appearance="blush false", text="{i}Тсс{/i}, просто откинься и расслабляйся.")
    call process_character (edna, appearance="blush false", text="Бабушка позаботится о тебе.")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Я, безусловно, позабочусь о тебе, [n.say_name]...)")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Милый и твёрдый в моей руке)")
    call process_character (edna, appearance="blush false", text="(И пульсирует тоже)")
    call process_character (edna, appearance="blush false", text="(Таким хером любая бабушка будет гордиться...)")
    call process_character (n, appearance="blush false", text="Хмм!")
    call process_character (n, appearance="blush false", text="(Разве бабушка не знает, что мы делаем это в открытую?!)")
    call process_character (n, appearance="blush false", text="(Что делать, если [k.say_name] или [sa.say_name] решат присоединиться?!)")
    call process_character (n, appearance="blush false", text="(Нас обязательно поймают!)")
    call process_character (n, appearance="blush false", text="Ох...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Но...{w=1.0}я не хочу, чтобы бабушка сейчас останавливалась)")
    call process_character (n, appearance="blush false", text="(Я просто должен молчать)")
    call process_character (n, appearance="blush false", text="(Пока я здесь, и никто не придёт, мы должны быть в порядке...)")
    call process_character (si, appearance="blush false", text="Вы только посмотрите на этих двоих!")
    call process_character (n, appearance="blush false", text="!!")
    call process_character (n, appearance="blush false", text="(М-мама!)")

    call static_still_ctc ("bg edna_simonetalk")

    call process_character (si, appearance="blush false", text="[n.say_name] решил пойти с тобой, Мама?")
    call process_character (si, appearance="blush false", text="Прекрасная температура!")
    call process_character (edna, appearance="blush false", text="Да, он был очень рад провести время со своей бабушкой в джакузи!")

    show bg edna_simonehappy
    with Dissolve(0.5)

    call process_character (si, appearance="blush false", text="Это восхитительно, [n.say_name] сидит прямо рядом с тобой, мама!")
    call process_character (si, appearance="blush false", text="Тебе нравится быть рядом с бабушкой, а [n.say_name]?")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (edna, appearance="blush false", text="Думаю, он немного смущен, дорогая.")
    call process_character (edna, appearance="blush false", text="Мальчику трудно признать, что он любит зависать с бабушкой.")

    show bg edna_simonehappy_ednahappy
    with Dissolve(0.5)

    call process_character (edna, appearance="blush false", text="Но мы отлично проводим время вместе!")
    call process_character (edna, appearance="blush false", text="Мы говорим обо всяких вещах.")

    show bg edna_underwater_jerk
    with Dissolve(0.5)

    call process_character (si, appearance="blush false", text="Это замечательно!")
    call process_character (si, appearance="blush false", text="О чем вы болтаете, [n.say_name]?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Бабушка до сих пор не перестала тереть мой член!)")
    call process_character (n, appearance="blush false", text="(Разве она не беспокоится, что Мама увидит?!)")
    call process_character (edna, appearance="blush false", text="[n.say_name] рассказывал мне всё об этих стримерских вещах, которые его сестра и он делают вместе.")
    call process_character (si, appearance="blush false", text="О, ты не поверишь, как им нравится это, Мама!")
    call process_character (si, appearance="blush false", text="Люди могут смотреть, как они играют в видеоигры со всей страны.")
    call process_character (si, appearance="blush false", text="Я даже не могу понять, как это работает!")
    call process_character (edna, appearance="blush false", text="Когда я увидела комнату твоей дочери [sa.say_name], я подумала, что она больше похожа на высокотехнологичную студию!")
    call process_character (edna, appearance="blush false", text="Дети учатся технологиям так быстро!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Бабушка даже не беспокоится о том, что Мама рядом)")
    call process_character (n, appearance="blush false", text="(Она просто разговаривает, как обычно...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я думаю, что это хорошо, что бабушка говорит большую часть времени)")
    call process_character (n, appearance="blush false", text="(Мне трудно сохранять спокойствие...)")

    show bg edna_simonetalk_aroused
    with Dissolve(0.5)

    call process_character (si, appearance="blush false", text="Я хотела, чтобы вы оба знали, что суп почти готов.")
    call process_character (si, appearance="blush false", text="Есть ли что-нибудь, что бы ты предпочла?")

    show bg edna_simonetalk_ednahappy_aroused
    with Dissolve(0.5)

    call process_character (edna, appearance="blush false", text="Я возьму все, что ты мне дашь, дочка.")
    call process_character (edna, appearance="blush false", text="Я всегда заинтригована, когда мне не нужно готовить для себя!")
    call process_character (si, appearance="blush false", text="А как насчет тебя, [n.say_name]?")
    call process_character (si, appearance="blush false", text="Тебе что-нибудь нужно?")

    show bg edna_simonetalk_aroused
    with Dissolve(0.5)

    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (n, appearance="blush false", text="Я...{w=1.0}я не уверен...")
    call process_character (si, appearance="blush false", text="Может...{w=1.0}фруктов?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Есть...{w=1.0}красный картофель.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Я также могу разогреть несколько булочек.")
    call process_character (n, appearance="blush false", text="Ах!")
    call process_character (si, appearance="blush false", text="Ты хочешь их, [n.say_name]?")
    call process_character (si, appearance="blush false", text="Булочки?")
    call process_character (n, appearance="blush false", text="Д-да, пожалуйста.")

    show bg edna_simonetalk_ednahappy_aroused
    with Dissolve(0.5)

    call process_character (edna, appearance="blush false", text="Булочки это здорово!")
    call process_character (edna, appearance="blush false", text="Я тоже возьму немного.")

    show bg edna_simonehappy_ednahappy_aroused
    with Dissolve(0.5)

    call process_character (si, appearance="blush false", text="Прекрасно!")
    call process_character (si, appearance="blush false", text="Я разогрею несколько штук.")

    show bg edna_simonetalk_aroused
    with Dissolve(0.5)

    call process_character (si, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Твоё лицо выглядит немного красным, [n.say_name].")
    call process_character (n, appearance="blush false", text="...")
    call process_character (si, appearance="blush false", text="Не перегревайся в джакузи, ладно?")
    call process_character (si, appearance="blush false", text="Ты можешь остаться здесь еще на несколько минут.")
    call process_character (si, appearance="blush false", text="Мама, ты можешь убедиться, что [n.say_name] не останется надолго?")
    call process_character (edna, appearance="blush false", text="Конечно.")
    call process_character (edna, appearance="blush false", text="Я и сама собиралась скоро выбираться.")
    call process_character (si, appearance="blush false", text="Ладно, мне нужно вернуться и довести суп до кипения.")
    call process_character (si, appearance="blush false", text="Я позову, когда все будет готово.")

    show bg edna_nosimone_aroused
    with Dissolve(0.5)

    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (edna, appearance="blush false", text="Похоже, у нас есть немного больше времени, [n.say_name].")
    call process_character (edna, appearance="blush false", text="...")

    call static_still_ctc ("bg edna_jerkblur_nocum")

    call process_character (n, appearance="blush false", text="Б-бабушка!")
    call process_character (n, appearance="blush false", text="(Она даже не пытается скрыть, что она делает!)")
    call process_character (n, appearance="blush false", text="(Если мама вернется обратно...)")
    call process_character (edna, appearance="blush false", text="Я не ожидала, что ты продержишься так долго, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Это делает меня очень счастливой.")
    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (edna, appearance="blush false", text="Ты должно быть часто ласкаешь себя.")
    call process_character (edna, appearance="blush false", text="Ты гладишь свой член почти каждый день?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Д-да...")
    call process_character (edna, appearance="blush false", text="И все это время тебе приходилось справляться только с собой?")

    $ amount = girls_sexually_played_with_amount()
    if dream:
        $ amount = amount - 1

    if amount > 0:
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Не все время...")
        call process_character (edna, appearance="blush false", text="Мой внук признает, что у него отношения с другой девушкой?")
        call process_character (n, appearance="blush false", text="...")
        call process_character (edna, appearance="blush false", text="А, понятно...{w=1.0}это отношения, о которых никто не должен знать.")
        call process_character (n, appearance="blush false", text="...")
        call process_character (edna, appearance="blush false", text="Секрет останется в безопасности с бабушкой!")
        call process_character (edna, appearance="blush false", text="Любому было бы трудно заставить меня рассказать личную информацию.")
        call process_character (n, appearance="blush false", text="Спасибо, Бабушка.")
        call process_character (edna, appearance="blush false", text="И то, что происходит в джакузи, остаётся в джакузи.")
        call process_character (edna, appearance="blush false", text="Ты понимаешь, о чем я говорю?")
        call process_character (n, appearance="blush false", text="Д-да, Бабушка.")
    else:
        call process_character (n, appearance="blush false", text="Я-я...")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Я обычно трогаю свой пенис в ванной...")
        call process_character (edna, appearance="blush false", text="Но что делать, если в ванной комнате кто-то есть, [n.say_name]?")
        call process_character (edna, appearance="blush false", text="Куда ты пойдёшь?")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Может быть в мою спальню.")
        call process_character (edna, appearance="blush false", text="Или...{w=1.0}ты всегда можешь попросить бабушку о помощи.")
        call process_character (n, appearance="blush false", text="Ты сделаешь что-то подобное для меня, Бабушка?")
        call process_character (edna, appearance="blush false", text="Почему бы мне этого не сделать, [n.say_name]?")
        call process_character (edna, appearance="blush false", text="Если у моего внука есть сильное желание, я хочу помочь ему.")
        call process_character (edna, appearance="blush false", text="Это также самое веселое время, что у меня было с членами за последние годы!")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="С-спасибо, Бабушка...")

    call static_still_ctc ("bg edna_jerkblur_eyesclosed_nocum")

    call process_character (edna, appearance="blush false", text="Ты хочешь снять напряжение, [n.say_name]?")
    call process_character (edna, appearance="blush false", text="Ты все ближе и ближе...")
    call process_character (n, appearance="blush false", text="Ах, ах...")
    call process_character (edna, appearance="blush false", text="Подумай обо всех изгибах и как я трогаю твой хер.")
    call process_character (edna, appearance="blush false", text="И как мои пальцы обвиваются вокруг твоего члена.")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (edna, appearance="blush false", text="Сейчас есть только один вариант действий, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Это кульминация моего мастурбирования.")
    call process_character (edna, appearance="blush false", text="Я знаю, тебе не терпится это сделать...")
    call process_character (n, appearance="blush false", text="Хаа...{w=1.0}Аах!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg edna_jerkblur_eyesclosed_cum")

    call process_character (edna, appearance="blush false", text="О, вот ты и...")
    call process_character (edna, appearance="blush false", text="Это то, чего мы хотим.")
    call process_character (edna, appearance="blush false", text="Отпусти напряжение.")
    call process_character (n, appearance="blush false", text="{i}Глык!{/i}")

    window hide
    show bg edna_jerk_aftercum
    with Dissolve(0.5)
    pause

    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Посмотрите на всю сперму!)")
    call process_character (edna, appearance="blush false", text="(Это вытекает в воду)")
    call process_character (edna, appearance="blush false", text="(Шары [n.say_name], должно быть, работают на максимальной мощности!)")
    call process_character (n, appearance="blush false", text="Хаа, ах...")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Все прошло даже лучше, чем я ожидала!)")
    call process_character (edna, appearance="blush false", text="(Я не была уверена, как [n.say_name] отреагирует на меня, делая этот смелый шаг)")
    call process_character (edna, appearance="blush false", text="(Он был совершен в тот момент, когда я взяла его член!)")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Если мой внук наслаждался моей мастурбацией настолько...)")
    call process_character (edna, appearance="blush false", text="(Тогда я думаю, что ему понравятся и другие вещи...)")
    call process_character (si, appearance="blush false", text="Ужин почти готов!")
    call process_character (si, appearance="blush false", text="Заходите и высушитесь!")
    call process_character (si, appearance="blush false", text="Я подготовлю тарелки к тому времени, как вы оденетесь!")
    call process_character (edna, appearance="blush false", text="Звучит хорошо, дочка!")
    call process_character (edna, appearance="blush false", text="Мы выходим прямо сейчас!")

    show bg edna_jerk_aftercum_smile
    with Dissolve(0.5)

    call process_character (n, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Небольшой перекус звучит хорошо, [n.say_name]?")
    call process_character (edna, appearance="blush false", text="Особенно после этого...")
    call process_character (n, appearance="blush false", text="{i}Вздох...{/i}")
    call process_character (n, appearance="blush false", text="Да, я проголодался.")
    call process_character (edna, appearance="blush false", text="Моему внуку нужно хорошо питаться!")
    call process_character (edna, appearance="blush false", text="Давай вернем твой пенис обратно в плавки.")
    call process_character (edna, appearance="blush false", text="Я буду осторожна с ним...")


    python:
        edna.revistable_scenes.add("edna_scene_handjob_revisit")

        if not dream:
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_received_handjob", 1)

    call process_end_of_scene ("edna_scene_handjob", char=edna, dream=dream)

    return

label edna_scene_handjob_revisit:
    $ no_bust_art = False

    if "edna_scene_handjob_revisit" in scenes_completed:
        call edna_scene_handjob_revisit_2nd_time
    else:
        call edna_scene_handjob_revisit_1st_time

    return

label edna_scene_handjob_revisit_1st_time:
    call process_character (n, appearance="pose handfist face neutral blush false")
    call process_character (edna, appearance="pose fisthip face happy blush false mouth red", text="Ха-ха, постарайся быть более сдержанным в следующий раз, [n.say_name]!")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Что, если кто-то услышал тебя?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Сдержанным, Бабушка?")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Типа, Ах...{w=1.0} выбирай слова более тщательно.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Ох...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Тогда как мне следует спросить?")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Что-то вроде...")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="\"Мы можем пойти в джакузи вместе, бабушка?\"")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Это было бы идеально.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Но откуда тебе знать, что я на самом деле имею в виду?")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Не беспокойся об этом, [n.say_name].")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Я точно знаю, что ты имеешь в виду...")
    call process_character (edna, appearance="pose handclasp face flirt blush false", text="Я могу читать между строк, как говорится.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Это классно, Бабушка!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Жаль, что я не могу этого понять.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Когда-нибудь.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Всё это приходит со временем и опытом.")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="У меня много и того и другого!")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="...")
    call process_character (edna, appearance="pose handclasp face flirt blush false", text="Теперь о приглашении в джакузи...")

    call fade_to_black (1)


    call static_still_ctc ("bg edna_hottub")

    call process_character (edna, appearance="blush false", text="Похоже, все остальные сегодня вышли из дома.")
    call process_character (edna, appearance="blush false", text="Это чистое совпадение или стратегическое планирование, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Моя Мама была дома, прежде чем я ушел.")
    call process_character (n, appearance="blush false", text="Она, должно быть, делала некоторые поручения.")
    call process_character (edna, appearance="blush false", text="Это дает нам дополнительное время вместе.")
    call process_character (edna, appearance="blush false", text="Это именно то, чего мы хотим...")

    call static_still_ctc ("bg edna_legtouch_hard")

    call process_character (edna, appearance="blush false", text="Уже твердый, [n.say_name]?")
    call process_character (edna, appearance="blush false", text="Эрекция приходит легко к тебе.")
    call process_character (n, appearance="blush false", text="Я знаю, что ты будешь делать, Бабушка.")
    call process_character (n, appearance="blush false", text="Я задумалась об этом и.....")
    call process_character (edna, appearance="blush false", text="Твоя мама сказала, что у тебя богатое воображение.")
    call process_character (edna, appearance="blush false", text="Ты подумал о том, что чувствовал раньше?")
    call process_character (n, appearance="blush false", text="Д-да, я вроде как это сделал.")

    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg edna_underwater_jerk")

    call process_character (edna, appearance="blush false", text="Ты чувствуешь это?")
    call process_character (n, appearance="blush false", text="Ох...")
    call process_character (edna, appearance="blush false", text="Большая разница по сравнению с мечтами в твоей голове, да?")
    call process_character (n, appearance="blush false", text="Сильно отличаются...")
    call process_character (edna, appearance="blush false", text="Кусочек вечной мудрости для тебя, [n.say_name]...")
    call process_character (edna, appearance="blush false", text="Всегда выбирай реальные вещи, если можешь.")
    call process_character (edna, appearance="blush false", text="Фантазия не то же самое.")
    call process_character (edna, appearance="blush false", text="Поверь мне, я знаю.")
    call process_character (n, appearance="blush false", text="Окей.")
    call process_character (n, appearance="blush false", text="Я постараюсь делать все по-настоящему, насколько смогу.")
    call process_character (edna, appearance="blush false", text="Ты уже на шаг опережаешь всех, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Технически, такого рода вещи должны произойти позже в будущем для тебя.")
    call process_character (edna, appearance="blush false", text="К счастью, у тебя есть бабушка, которая не всегда играет по правилам!")
    call process_character (n, appearance="blush false", text="Ты не следуешь правилам, Бабушка?")
    call process_character (edna, appearance="blush false", text="Для некоторых вещей, я бы сказала, что это правда.")
    call process_character (n, appearance="blush false", text="Ах...")
    call process_character (n, appearance="blush false", text="Какими вещами?")

    call static_still_ctc ("bg edna_nosimone_aroused")

    call process_character (edna, appearance="blush false", text="С тем же успехом я могу убрать с дороги самое очевидное...")
    call process_character (edna, appearance="blush false", text="Бабушки обычно не должны делать такие вещи со своими внуками.")
    call process_character (edna, appearance="blush false", text="Я определенно нарушила это правило...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Но мне нравится то, что ты делаешь со мной, Бабушка.")

    show bg edna_nosimone_ednahappy_aroused
    with Dissolve(0.5)

    call process_character (edna, appearance="blush false", text="И вот почему меня не волнует нарушение нескольких правил!")
    call process_character (edna, appearance="blush false", text="Если это делает всех счастливыми, то кого это волнует!")
    call process_character (edna, appearance="blush false", text="Разве это не правильное мышление?")
    call process_character (edna, appearance="blush false", text="Убедись, что ты и другие счастливы, верно?")
    call process_character (n, appearance="blush false", text="Я согласен с этим...")
    call process_character (n, appearance="blush false", text="Хаах...")
    call process_character (edna, appearance="blush false", text="Ты остаёшься позитивным, [n.say_name], и это делает других позитивными.")
    call process_character (edna, appearance="blush false", text="Это визитная карточка хорошего парня...")

    call static_still_ctc ("bg edna_jerkblur_nocum")

    call process_character (edna, appearance="blush false", text="И ты знаешь...")
    call process_character (edna, appearance="blush false", text="Хорошие мальчики получают вознаграждение, [n.say_name].")
    call process_character (n, appearance="blush false", text="Ммм, ахх...")
    call process_character (edna, appearance="blush false", text="И это совокупно.")
    call process_character (edna, appearance="blush false", text="Ты знаешь, что означает совокупность?")
    call process_character (n, appearance="blush false", text="Ха-а...")
    call process_character (n, appearance="blush false", text="Я не могу вспомнить.")
    call process_character (edna, appearance="blush false", text="Это значит, чем больше ты будешь хорошим мальчиком, тем больше наград получишь.")
    call process_character (edna, appearance="blush false", text="И я, твоя бабушка, этому золотому правилу, всегда следую.")

    show bg edna_jerkblur_eyesclosed_nocum
    with Dissolve(0.5)

    call process_character (n, appearance="blush false", text="(Она движется быстрее!)")
    call process_character (edna, appearance="blush false", text="Я люблю вознаграждать тебя, [n.say_name].")
    call process_character (n, appearance="blush false", text="Ах, ах, ах!")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Разве моя грудь не мягкая?")
    call process_character (edna, appearance="blush false", text="Ты чувствуешь, как они давят на тебя?")
    call process_character (n, appearance="blush false", text="О-ох, да...")
    call process_character (n, appearance="blush false", text="Одна хлюпает по руке!")
    call process_character (edna, appearance="blush false", text="Ты думаешь о том, что бы ты сделал с моей грудью, если бы у тебя был шанс?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ммм, да, Бабушка...")
    call process_character (edna, appearance="blush false", text="Я уверена, что ты хочешь сделать множество вещей с моей грудью.")
    call process_character (edna, appearance="blush false", text="Я заметила, что ты любишь смотреть на неё при каждом удобном случае.")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (edna, appearance="blush false", text="Я здесь, чтобы сказать тебе, [n.say_name]...")
    call process_character (edna, appearance="blush false", text="Есть большая вероятность, что у тебя будет шанс.")
    call process_character (n, appearance="blush false", text="Д-действительно, Бабушка?")
    call process_character (edna, appearance="blush false", text="Это то, чего ты можешь с нетерпением ждать...")
    call process_character (n, appearance="blush false", text="Хррм!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg edna_jerkblur_eyesclosed_cum")

    call process_character (edna, appearance="blush false", text="Это было неожиданно!")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Бьюсь об заклад, он подумал о моей груди как раз перед тем, как он эякулировал)")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Я могу только представить, сколько бы он брызнул, если бы моя грудь была обернута вокруг его члена...)")

    call static_still_ctc ("bg edna_jerk_aftercum_smile")

    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (edna, appearance="blush false", text="Это мой внук!")
    call process_character (edna, appearance="blush false", text="Всегда впечатляющее количество спермы во время оргазма!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Что мы будем делать с спермой в джакузи?")
    call process_character (edna, appearance="blush false", text="Фильтр позаботится об этом.")
    call process_character (edna, appearance="blush false", text="Тем не менее, он может засориться, если мы сделаем эту процедуру много раз!")

    call edna_scene_handjob_revisit_end

    return

label edna_scene_handjob_revisit_2nd_time:
    python hide:
        play_music("audio/music/Sensual Loop.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg edna_underwater_jerk")

    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="([n.say_name] уже снимает плавки, прежде чем я положила руку на его член!)")
    call process_character (edna, appearance="blush false", text="(Он даже сделал это, пока его мать была рядом...)")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Он гораздо меньше беспокоится об этом, чем раньше)")
    call process_character (edna, appearance="blush false", text="(Это обнадеживает!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я надеюсь, что Мама не возражает против того, что Бабушка часто навещает нас)")
    call process_character (n, appearance="blush false", text="(Она хотела проводить больше времени с бабушкой, но я не знаю, часто ли она это имела в виду!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Мама, похоже, не знает, что мы с бабушкой делаем)")
    call process_character (n, appearance="blush false", text="(Я не думаю, что она смогла сказать...)")

    show bg edna_simonehappy_aroused
    with Dissolve(0.5)

    call process_character (si, appearance="blush false", text="Ты уверена, что не планируешь переехать к нам, Мама?")
    call process_character (si, appearance="blush false", text="Хаха, ты так часто здесь бываешь!")
    call process_character (edna, appearance="blush false", text="Мне нравится вас навещать.")
    call process_character (edna, appearance="blush false", text="И ваш дом очень гостеприимный!")
    call process_character (edna, appearance="blush false", text="Здесь такая приятная атмосфера.")

    show bg edna_simonetalk_aroused
    with Dissolve(0.5)

    call process_character (si, appearance="blush false", text="У него есть такое чувство, да!")
    call process_character (si, appearance="blush false", text="Это, конечно, требует много времени, хотя.")
    call process_character (si, appearance="blush false", text="Уборка первого этажа занимает почти целый день.")
    call process_character (edna, appearance="blush false", text="Вся эта тяжелая работа делает дом сногсшибательным внутри!")
    call process_character (edna, appearance="blush false", text="Но лично я бы не стала торопиться.")
    call process_character (edna, appearance="blush false", text="Последнее, что ты захочешь, это растянуть или напрягать что-то.")
    call process_character (edna, appearance="blush false", text="Тогда ты не сможешь сделать никакой уборки!")
    call process_character (si, appearance="blush false", text="Кто-нибудь из вас хочет что-нибудь выпить?")

    show bg edna_simonetalk_ednahappy_aroused
    with Dissolve(0.5)

    call process_character (edna, appearance="blush false", text="Мне холодный чай, пожалуйста!")
    call process_character (edna, appearance="blush false", text="Несладкий с лимоном, если есть.")
    call process_character (si, appearance="blush false", text="Ты хотел бы чай со льдом, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Конечно...")

    show bg edna_simonetalk_aroused
    with Dissolve(0.5)

    call process_character (edna, appearance="blush false", text="Я бы его подсластила.")
    call process_character (edna, appearance="blush false", text="Ты же сладкоежка, [n.say_name].")
    call process_character (si, appearance="blush false", text="Ты права, Мама!")
    call process_character (si, appearance="blush false", text="[n.say_name] любит сладкие напитки!")
    call process_character (si, appearance="blush false", text="По крайней мере, это лучше, чем содовая!")

    show bg edna_nosimone_aroused
    with Dissolve(0.5)

    call process_character (edna, appearance="blush false", text="...{p}...")

    call static_still_ctc ("bg edna_jerkblur_nocum")

    call process_character (n, appearance="blush false", text="Ахх...")
    call process_character (edna, appearance="blush false", text="Мне пришлось попросить твою маму зайти в дом ненадолго.")
    call process_character (edna, appearance="blush false", text="Эта поза обеспечивает лучшее сцепление...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (edna, appearance="blush false", text="Я знаю, что я поглаживаю тебе быстрее, чем обычно...")
    call process_character (edna, appearance="blush false", text="Но если ты не кончишь в ближайшее время, нас могут прервать, и я не смогу закончить.")
    call process_character (edna, appearance="blush false", text="Было бы ужасно, если бы у тебя были синие яйца.")
    call process_character (n, appearance="blush false", text="Ах...")
    call process_character (n, appearance="blush false", text="Я не хочу, чтобы это произошло.")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", yalign = 0.1)
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg edna_jerkblur_eyesclosed_cum")

    call process_character (edna, appearance="blush false", text="Ммм, вот!")
    call process_character (edna, appearance="blush false", text="Теперь я знаю, что ты полностью удовлетворён.")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Часть спермы плавает на поверхности...)")
    call process_character (edna, appearance="blush false", text="(Я надеюсь, что [si.say_name] не заметит!)")
    call process_character (edna, appearance="blush false", text="(Хотя она, вероятно, не поймет, что это. К тому времени она растворится)")

    call edna_scene_handjob_revisit_end

    return

label edna_scene_handjob_revisit_end:

    python:
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_received_handjob", 1)

    call process_end_of_scene ("edna_scene_handjob_revisit", char=edna, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label edna_scene_titfuck(dream=False):
    call edna_scene_titfuck_sex (dream=dream)
    return

label edna_scene_titfuck_sex(dream=False):
    $ renpy.start_predict("edna_titfuck_bikini_anim")
    call process_scene_beginning (bg="bg edna_house_daytime", dream=dream )

    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Я пришёл, Бабушка!")
    call process_character (edna, text="Привет [n.say_name]!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Где ты?")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Я была на балконе.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Ты там уже был?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Нет, не видел.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Он идеально подходит для двух человек!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Часто я выхожу туда, чтобы почитать книгу или расслабиться.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Там может быть жарко, поэтому тебе нужно убедиться, что ты хорошо защищен от солнца.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Мне понадобится много солнцезащитного крема?")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="О да, это жизненно важно.")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="На самом деле, я почти забыла нанести его, когда вышла туда.")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="У меня есть этот раствор на масляной основе, который охлаждает кожу и блокирует ультрафиолетовые лучи.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Никогда не слышал о таком солнцезащитном креме.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Это что-то вроде фирменного блюда.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Я могу найти его только в местной аптеке.")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face embarrassed blush false mouth red", text="Ты не поверишь, как дорого стоит маленькая бутылка!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face neutral blush false mouth red", text="Но он хорошо выполняет свою работу.")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Я хочу пойти туда с тобой, бабушка!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face happy blush false", text="Это должен быть такой сладкий вид на пляж с балкона!")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Да.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Так здорово видеть всех внизу.")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face happy blush false mouth red", text="Хотела бы я иметь бинокль, чтобы шпионить за людьми, ха-ха!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Звучит весело!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Я хочу сделать это!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="(Балкон - довольно уединенное место)")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="(Никто не сможет увидеть нас там...)")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face flirt blush false mouth red", text="(Я чувствую захватывающую возможность с моим внуком)")
    call process_character (edna, appearance="outfit swimsuit pose handhip face flirt blush false mouth red", text="([n.say_name] правильно...{w=1.0}это будет весело...)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Мне переодеть плавки прямо сейчас, чтобы присоединиться к тебе, бабушка?")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="О, разумеется!")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="Однако прежде чем ты это сделаешь, я хотела бы задать тебе небольшой вопрос.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Да?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Ты можешь помочь мне с нанесением масла?")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Я всегда пропускаю определенные места и сгораю на солнце!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Ты хочешь, чтобы я помог с этим?")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="У тебя будет гораздо больше шансов охватить все укромные места.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="В каких местах ты хочешь, чтобы я смазал тебя маслом?")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="Есть только одно место, где мне больше всего нужна помощь...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Область вокруг груди.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Вокруг груди?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face embarrassed blush true", text="Это значит, что я буду тереться о тебя...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="У меня нет проблем с этим, [n.say_name].")
    call process_character (edna, appearance="outfit swimsuit pose handhip face flirt blush false mouth red", text="Я позволю тебе работать в этой области столько, сколько тебе нужно.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face flirt blush false mouth red", text="В конце концов, цель - защитить мою грудь от солнца.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush true", text="...{p}...")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face happy blush false mouth red", text="(Он немного смущен)")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face happy blush false mouth red", text="(Как мило)")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face happy blush false mouth red", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="(Однако он не отклонил запрос...)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush true", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush true", text="(Я буду трогать бабушкины сиськи, если сделаю это!)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush true", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush true", text="(Я действительно хотел знать, какие они на ощупь...)")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush true", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="(Он не может перестать пялиться на мою грудь...)")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="([n.say_name] не хочет упустить возможность!)")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="...")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="(Я немного поколеблю его решение)")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="Я всегда могу нанести масло сама, [n.say_name].")
    call process_character (edna, appearance="outfit swimsuit pose fisthip face neutral blush false mouth red", text="Ничего страшного.")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face embarrassed blush false", text="Н-нет, я хочу сделать это, бабушка!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="О, хорошо!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="Я благодарна тебе за помощь, [n.say_name]!")
    call process_character (edna, appearance="outfit swimsuit pose handclasp face happy blush false mouth red", text="(Прошло как по маслу)")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face neutral blush false mouth red", text="В любом случае, я собираюсь вернуться на балкон.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Я буду ждать тебя там!")

    call fade_to_black (1)

    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="...{p}...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Вау, здесь так светло!")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Это потому, что солнечный свет отражается от балкона.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Именно поэтому здесь может быть жарко.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Самое приятное, что мы можем просто зайти внутрь и остыть.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="У тебя есть крем для загара, бабушка?")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Конечно!")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Я держу его рядом все время.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="...")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Вот, держи.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Абсолютно новый флакон!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Как ты хочешь, чтобы я нанёс его на тебя?")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Можешь делать это так, как хочешь, [n.say_name].")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Обильно намажь маслом мою грудь.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Ты поймёшь, что моя кожа защищена, когда она выглядит блестящей.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Отлично.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="И не пропусти нижнюю часть.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Нижнюю часть?")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Под грудью.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Это место я часто пропускаю.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Протри, как можно больше там.")
    call process_character (edna, appearance="outfit swimsuit pose handhip face happy blush false mouth red", text="Я прилягу, пока ты будешь работать.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...{p}...")

    call static_still_ctc ("bg edna_titrub")

    call process_character (edna, appearance="blush false", text="Оох!")
    call process_character (edna, appearance="blush false", text="Я уже чувствую, как масло охлаждает мою кожу!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Бабушка просто позволяет мне трогать ее сиськи, как я хочу!)")
    call process_character (n, appearance="blush false", text="(Я могу сжимать их руками и все такое!)")
    call process_character (edna, appearance="blush false", text="(Я никогда не видела глаза [n.say_name] настолько широко открытыми раньше)")
    call process_character (edna, appearance="blush false", text="(Он использует все шансы, чтобы ласкать мою грудь)")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Ммм...")
    call process_character (edna, appearance="blush false", text="Хорошая работа по размазыванию масла, [n.say_name].")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Кажется, я почти закончил, Бабушка.")
    call process_character (edna, appearance="blush false", text="Там есть что ещё покрыть, не так ли?")
    call process_character (edna, appearance="blush false", text="Но ты очень тщательный [n.say_name], гораздо больше, чем я.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Ты хочешь убедиться, что бабушкина грудь защищена, не так ли?")
    call process_character (n, appearance="blush false", text="{i}Глык.{/i}..")
    call process_character (edna, appearance="blush false", text="...{p}...")
    call process_character (edna, appearance="blush false", text="Ты хочешь сделать с ними непослушные вещи, [n.say_name]?")
    call process_character (edna, appearance="blush false", text="Я могу сказать по тому, как ты ведешь себя.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Скажи мне, о чем ты фантазируешь с моей грудью.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Тебе не нужно притворяться.")
    call process_character (edna, appearance="blush false", text="Скажи мне откровенно, о чем ты думаешь.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я-я думаю о многих вещах...")
    call process_character (edna, appearance="blush false", text="Да ладно тебе.")
    call process_character (edna, appearance="blush false", text="Будь более конкретен.")
    call process_character (edna, appearance="blush false", text="Какие мысли проносятся в твоей голове?")
    call process_character (n, appearance="blush false", text="Эээ, ну...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я...{w=1.0}ум...")
    call process_character (edna, appearance="blush false", text="(Хм, трудно получить от него ответ)")
    call process_character (edna, appearance="blush false", text="(Возможно, разговор успокоит его нервы...)")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Хочешь узнать, о чём я мечтала пока ты работал над моей грудью, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Т-ты фантазировала, Бабушка?")
    call process_character (edna, appearance="blush false", text="Эй, может я и старушка, но у меня тоже есть желания.")
    call process_character (n, appearance="blush false", text="О чём ты думаешь, Бабушка?")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Я очень хочу, чтобы ты пососал мои соски.")
    call process_character (edna, appearance="blush false", text="Одно упоминание об этом меня возбуждает.")
    call process_character (n, appearance="blush false", text="Это так?")
    call process_character (edna, appearance="blush false", text="Это то, что ты хотел бы, [n.say_name]?")
    call process_character (edna, appearance="blush false", text="Хочешь пососать мои сиськи?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Вообще-то...")
    call process_character (n, appearance="blush false", text="Это одна из вещей, о которых я думал...")
    call process_character (edna, appearance="blush false", text="Тогда почему бы тебе не попробовать, [n.say_name]?")
    call process_character (edna, appearance="blush false", text="Дай мне почувствовать твой рот на моей груди...")
    call process_character (n, appearance="blush false", text="...")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadein = 1.0)

    call static_still_ctc ("bg edna_titsuck")

    call process_character (edna, appearance="blush false", text="{i}Ухх.{/i}..")
    call process_character (n, appearance="blush false", text="Ммм...")
    call process_character (edna, appearance="blush false", text="(Да!)")
    call process_character (edna, appearance="blush false", text="(Его язык такой теплый...)")
    call process_character (edna, appearance="blush false", text="(И мой сосок растягивается у него во рту!)")
    call process_character (edna, appearance="blush false", text="Ох!")
    call process_character (edna, appearance="blush false", text="(Они становятся такими твердыми!)")
    call process_character (n, appearance="blush false", text="Ммф, Ммф.")
    call process_character (n, appearance="blush false", text="(Так бабушка хотела, чтобы я это сделал?)")
    call process_character (n, appearance="blush false", text="(Интересно, так ли она себе это представляла...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я надеюсь, что это так хорошо, как она себе представляла)")
    call process_character (n, appearance="blush false", text="(Я знаю, что это для меня!)")
    call process_character (edna, appearance="blush false", text="Аах, [n.say_name]...")
    call process_character (edna, appearance="blush false", text="То как ты тянешь мои соски, оргазмично!")
    call process_character (edna, appearance="blush false", text="Ты когда-нибудь делал это раньше?")

    $ titsuck_amount = scenes_had_titsucking_amount()
    if "edna_scene_titfuck" in scenes_completed:
        $ titsuck_amount = titsuck_amount - 1

    if titsuck_amount >= 1:
        call process_character (n, appearance="blush false", text="Мм...{w=1.0}да, Бабушка.")
        call process_character (edna, appearance="blush false", text="Надеюсь, девушка, с которой ты это сделал, похвалила тебя после.")
        call process_character (edna, appearance="blush false", text="Ты одарён в этом, [n.say_name].")
        call process_character (edna, appearance="blush false", text="Я не знала никого, кто мог бы возбудить мои соски так сильно!")
    else:
        call process_character (n, appearance="blush false", text="Мм...{w=1.0}нет, Бабушка.")
        call process_character (n, appearance="blush false", text="Это в первый раз.")
        call process_character (edna, appearance="blush false", text="Тогда ты должно быть одарён, [n.say_name].")
        call process_character (edna, appearance="blush false", text="Я не знала никого, кто мог бы возбудить мои соски так сильно!")

    call static_still_ctc ("bg edna_titsuck_pull")

    call process_character (edna, appearance="blush false", text="Хммм!")
    call process_character (edna, appearance="blush false", text="([n.say_name] так энергичен с моей грудью)")
    call process_character (edna, appearance="blush false", text="(Моим сиськам никогда не уделяли так много внимания!)")
    call process_character (edna, appearance="blush false", text="(Им нравится темп моего внука!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(У меня весь рот забит бабушкиной грудью!)")
    call process_character (n, appearance="blush false", text="(Она немного сладкая на вкус...)")
    call process_character (edna, appearance="blush false", text="Ооо, ох!")
    call process_character (edna, appearance="blush false", text="Не слишком...{w=0.5}ах...{w=0.5} увлекайся, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Они могут не выглядеть так, но моя грудь такая же старая, как я!")
    call process_character (n, appearance="blush false", text="Прости, Бабушка...")
    call process_character (n, appearance="blush false", text="Я буду с ними помягче.")
    call process_character (edna, appearance="blush false", text="Я знаю, что бывает трудно сдержать возбуждение.")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Кстати о возбуждении...")
    call process_character (edna, appearance="blush false", text="Твой пенис должен быть твердым как камень.")
    call process_character (n, appearance="blush false", text="О-ох, да...")
    call process_character (n, appearance="blush false", text="Он очень твёрд.")
    call process_character (edna, appearance="blush false", text="Почему бы нам не дать твоему члену что-нибудь, чтобы насладиться?")
    call process_character (edna, appearance="blush false", text="Я знаю, что для этого нужно.")
    call process_character (edna, appearance="blush false", text="Это прекрасный комплимент нашей прелюдии...")
    call process_character (edna, appearance="blush false", text="Знаешь ли ты, что это такое [n.say_name]?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Это касается твоих сисек?")
    call process_character (edna, appearance="blush false", text="Ты на правильном пути!")

    call static_still_ctc ("bg edna_beforetitfuck")

    call process_character (edna, appearance="blush false", text="Как насчет того, чтобы ты скользнул своим членом в мою огромную грудь, [n.say_name]?")
    call process_character (edna, appearance="blush false", text="В конце концов, именно поэтому ты сейчас так возбуждён.")
    call process_character (n, appearance="blush false", text="В-вау...")
    call process_character (n, appearance="blush false", text="Я могу, Бабушка?")
    call process_character (edna, appearance="blush false", text="Ммм.")
    call process_character (edna, appearance="blush false", text="Посмотри, какое большое у меня декольте, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Твой пенис потеряется там.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я... я не против этого.")
    call process_character (edna, appearance="blush false", text="Хаха!")
    call process_character (edna, appearance="blush false", text="Мой бесстрашный внук!")

    if "vicky_tease_scene" in scenes_completed or "kira_scene_6" in scenes_completed or "gloryhole_scene_stall" in scenes_completed or "simone_scene_undressing" in scenes_completed:
        call process_character (n, appearance="blush false", text="У тебя самые большие сиськи, которые я когда-либо видел, Бабушка!")
        call process_character (edna, appearance="blush false", text="Самые большие?")
        call process_character (edna, appearance="blush false", text="Честное слово, ты должен узнать, каковы грудастые дамы!")
        call process_character (edna, appearance="blush false", text="Но я знаю, что они и в подмётки мне не годятся, намного большее удовольствия ты будешь иметь с моим!")
    else:
        call process_character (n, appearance="blush false", text="Твои сиськи такие массивные, Бабушка!")
        call process_character (edna, appearance="blush false", text="Вряд ли ты найдёшь больше, чем эти [n.say_name]!")
        call process_character (edna, appearance="blush false", text="И лучше всего, ты можешь использовать их!")
        call process_character (edna, appearance="blush false", text="Это идеальное преимущество, иметь такую Бабушку!")

    call process_character (n, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Я ожидала, что твой член выпал уже.")
    call process_character (edna, appearance="blush false", text="Особенно с такой палаткой в плавках!")
    call process_character (n, appearance="blush false", text="Я-я был в отключке, глядя на твои сиськи.")
    call process_character (edna, appearance="blush false", text="Ах, тогда это можно понять.")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (edna, appearance="blush false", text="Это великолепное зрелище, если я сама так говорю!")
    call process_character (edna, appearance="blush false", text="Твой член такой пылкий и нетерпеливый!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Как ты отреагируешь, когда твой член окажется между моих сисек?")
    call process_character (edna, appearance="blush false", text="Мне бы очень хотелось это выяснить!")
    call process_character (n, appearance="blush false", text="Я могу это сделать, Бабушка?")
    call process_character (edna, appearance="blush false", text="Непременно, пожалуйста!")

    call static_still_ctc ("bg edna_bikini_titfuck_nocum_surprise")

    call process_character (n, appearance="blush false", text="Хаах...")
    call process_character (n, appearance="blush false", text="(Ее сиськи окружили мой член!)")
    call process_character (edna, appearance="blush false", text="Твой член проскользнул без усилий, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Это почти элегантно, как это произошло.")
    call process_character (n, appearance="blush false", text="Т-такая мягкая...")
    call process_character (edna, appearance="blush false", text="Ощущение груди на члене никогда не состарится, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Вот почему ты всегда будешь возвращаться, чтобы сделать это снова и снова.")
    call process_character (n, appearance="blush false", text="Аах...")

    call static_still_ctc ("bg edna_bikini_titfuck_nocum_smile")

    call process_character (edna, appearance="blush false", text="Зажать твой член между моих грудей - это только половина удовольствия...")
    call process_character (edna, appearance="blush false", text="Давай, трахни мои сиськи, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Засунь и скользи своим членом по моей груди!")


    $ edna_titfuck_had_slow_speed_message = False
    $ edna_titfuck_had_normal_speed_message = False
    $ edna_titfuck_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    $ set_main_animation_speed(1.0)
    show anim_nothing_image as main_animation at main_animation_transform(IA_Animation_Edna_Titfuck_Bikini_Info())
    with Dissolve(1.15)
    show bg white

    pause 
    $ quick_menu = True

    call process_character (n, appearance="blush false", text="Ах, ох!")
    call process_character (n, appearance="blush false", text="Мм, ха!")
    call process_character (edna, appearance="blush false", text="Держись за мои сиськи, чтобы не упасть!")
    call process_character (edna, appearance="blush false", text="Да...{w=0.5}так хорошо, [n.say_name].")
    call process_character (edna, appearance="blush false", text="И надави бедрами.")
    call process_character (n, appearance="blush false", text="Ха-ах!")
    call process_character (n, appearance="blush false", text="(Я не знаю, где мой пенис в ее сиськах!)")
    call process_character (n, appearance="blush false", text="(Он входит, и я даже не могу его увидеть!)")
    call process_character (n, appearance="blush false", text="Хрм!")
    call process_character (n, appearance="blush false", text="(Но это не имеет значения!)")
    call process_character (n, appearance="blush false", text="(Это так совершенно потрясающе!)")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Мне все равно, что говорят другие...)")
    call process_character (edna, appearance="blush false", text="(Это правильный способ заботы о внуке!)")
    call process_character (edna, appearance="blush false", text="(Я - бабушка нового поколения!)")
    call process_character (edna, appearance="blush false", text="(Я могу бы быть пионером тренда для бабушек во всем мире!)")
    call process_character (edna, appearance="blush false", text="Мм...")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Опять же, я могла бы быть так далеко впереди своего времени, другие люди не приняли бы меня)")
    call process_character (edna, appearance="blush false", text="(Сейчас я чувствую удовлетворение, зная одно...)")
    call process_character (edna, appearance="blush false", text="(Я бабушка, которая предлагает сиськотрах внуку!)")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (n, appearance="blush false", text="Аах, да...")
    call process_character (edna, appearance="blush false", text="Эй, [n.say_name]...")
    call process_character (edna, appearance="blush false", text="Почему бы тебе не попробовать трахать мои сиськи в другом темпе?")
    call process_character (n, appearance="blush false", text="Ты имеешь в виду, что я должен изменить свою скорость?")
    call process_character (edna, appearance="blush false", text="Ты можешь полюбить медленное или быстрое движение.")
    call process_character (edna, appearance="blush false", text="Никогда не узнаешь, пока не попробуешь!")
    call process_character (n, appearance="blush false", text="Л-ладно.")
    call process_character (n, appearance="blush false", text="Я попробую!")

    window hide
    $ quick_menu = False
    show screen edna_titfuck_speed_settings(False)
    $ renpy.pause(3.0)
    $ renpy.suspend_rollback(True)

    call edna_scene_titfuck_phase_2 (dream=dream)

    return

label edna_titfuck_set_speed(speed):
    hide screen edna_titfuck_speed_settings
    $ set_main_animation_speed(speed)

    return

screen edna_titfuck_speed_settings(is_revisit=False, dream=False):
    vbox:
        xalign 0.97
        yalign 0.3
        spacing 20

        use main_menu_button(text="Медленно", action=Function(edna_titfuck_set_speed, "edna_titfuck_go_slow", is_revisit, dream), enabled=main_animation_speed != edna_titfuck_slow_speed_multiplier)
        use main_menu_button(text="Нормально", action=Function(edna_titfuck_set_speed, "edna_titfuck_go_normal", is_revisit, dream), enabled=main_animation_speed != 1.0)
        use main_menu_button(text="Быстро", action=Function(edna_titfuck_set_speed, "edna_titfuck_go_fast", is_revisit, dream), enabled=main_animation_speed != edna_titfuck_fast_speed_multiplier)


label edna_titfuck_go_slow(is_revisit, dream=False, skip_dialog=False):
    call edna_titfuck_set_speed (edna_titfuck_slow_speed_multiplier)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                call process_character (edna, appearance="blush false", text="Считаешь ли ты, как долго останешься на определенной скорости [n.say_name]?")
                call process_character (edna, appearance="blush false", text="Это похоже на то, что ты бы сделал!")
            else:
                call process_character (edna, appearance="blush false", text="Ах, почувствуй океанский бриз, [n.say_name]...")
                call process_character (edna, appearance="blush false", text="Это делает мои соски тверже!")
        else:
            if random.randint(0,1) == 0:
                call process_character (n, appearance="blush false", text="О, так хорошо, Бабушка!")
                call process_character (edna, appearance="blush false", text="Твой член движется неуклонно с такой скоростью.")
                call process_character (edna, appearance="blush false", text="Я чувствую, как твоя крайняя плоть ходит туда-сюда!")
            else:
                call process_character (n, appearance="blush false", text="Как тебе, Бабушка?")
                call process_character (edna, appearance="blush false", text="Мне это нравится, [n.say_name]!")
                call process_character (edna, appearance="blush false", text="Теперь, когда ты притормозил, ты можешь чувствовать себя лучше.")

        window hide
        with None
        $ edna_titfuck_had_slow_speed_message = True

    if is_revisit:
        $ renpy.call("edna_scene_titfuck_revisit_phase_2")
    else:
        $ renpy.call("edna_scene_titfuck_phase_2", dream = dream)

    return

label edna_titfuck_go_normal(is_revisit, dream=False, skip_dialog=False):
    call edna_titfuck_set_speed (1.0)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                call process_character (edna, appearance="blush false", text="Я думала о том, чтобы повесить занавеску на балконе.")
                call process_character (edna, appearance="blush false", text="Тогда у нас будет больше тени и дополнительное уединение!")
            else:
                call process_character (edna, appearance="blush false", text="Ты думал, что в самых смелых мечтах будешь трахать бабушкины сиськи?")
                call process_character (edna, appearance="blush false", text="Это больше не мечты!")
        else:
            if random.randint(0,1) == 0:
                call process_character (n, appearance="blush false", text="Это замечательно.")
                call process_character (edna, appearance="blush false", text="Я думаю, что ты нашёл отличное сладенькое местечко!")
            else:
                call process_character (n, appearance="blush false", text="Трудно решить, что лучше!")
                call process_character (edna, appearance="blush false", text="Я не думаю, что ты должен выбирать фаворитов, [n.say_name].")
                call process_character (edna, appearance="blush false", text="Ты можешь попробовать все способы!")

        window hide
        with None
        $ edna_titfuck_had_normal_speed_message = True

    if is_revisit:
        $ renpy.call("edna_scene_titfuck_revisit_phase_2")
    else:
        $ renpy.call("edna_scene_titfuck_phase_2", dream = dream)

    return

label edna_titfuck_go_fast(is_revisit, dream=False, skip_dialog=False):
    call edna_titfuck_set_speed (edna_titfuck_fast_speed_multiplier)

    if not skip_dialog:
        if is_revisit:
            if random.randint(0,1) == 0:
                call process_character (edna, appearance="blush false", text="О да, трахни мои сиськи.")
                call process_character (edna, appearance="blush false", text="Вот для чего они здесь, [n.say_name]!")
            else:
                call process_character (edna, appearance="blush false", text="Если бы у меня было немного больше места...")
                call process_character (edna, appearance="blush false", text="Я бы хотела попробовать это в джакузи у тебя дома!")
        else:
            if random.randint(0,1) == 0:
                call process_character (n, appearance="blush false", text="Я-я буду двигаться быстрее, Бабушка!")
                call process_character (edna, appearance="blush false", text="Ты не преувеличиваешь!")
                call process_character (edna, appearance="blush false", text="Твои бедра шлепают меня по груди!")
            else:
                call process_character (n, appearance="blush false", text="Надеюсь, это не слишком быстро, Бабушка!")
                call process_character (edna, appearance="blush false", text="Нет, [n.say_name]!")
                call process_character (edna, appearance="blush false", text="Ты двигайся так быстро, как хочешь!")
                call process_character (edna, appearance="blush false", text="Я хочу, чтобы ты насладился моими сиськами!")

        window hide
        with None
        $ edna_titfuck_had_fast_speed_message = True

    if is_revisit:
        $ renpy.call("edna_scene_titfuck_revisit_phase_2")
    else:
        $ renpy.call("edna_scene_titfuck_phase_2", dream = dream)

    return

label edna_scene_titfuck_phase_2(dream=dream):
    show screen edna_titfuck_speed_settings(False, True)
    call screen progress_button_screen("Продолжить")
    $ quick_menu = True
    hide screen edna_titfuck_speed_settings
    $ renpy.suspend_rollback(False)

    call edna_scene_titfuck_phase_3 (dream=dream)

    return

label edna_scene_titfuck_phase_3(dream=dream):
    call process_character (n, appearance="blush false", text="Оох, ахх...")
    call process_character (edna, appearance="blush false", text="Теперь не беспокойся о том, как будешь эякулировать, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Просто делай свое дело.")
    call process_character (n, appearance="blush false", text="Так что это не проблема, если...{w=1.0}я кончу на твои сиськи, Бабушка?")
    call process_character (edna, appearance="blush false", text="Вообще-то, это звучит забавно для меня!")
    call process_character (edna, appearance="blush false", text="Почему бы тебе не сделать это.")
    call process_character (n, appearance="blush false", text="Ты этого хочешь?")
    call process_character (edna, appearance="blush false", text="Конечно!")
    call process_character (edna, appearance="blush false", text="Может, закончим с того, с чего начали?")

    $ set_main_animation_speed(edna_titfuck_fastest_speed_multiplier)

    call process_character (n, appearance="blush false", text="Хррм...")
    call process_character (n, appearance="blush false", text="Ты...{w=0.5}ах...{w=0.5} так добра ко мне, Бабуля...")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (edna, appearance="blush false", text="Сожми мою грудь, пока не кончил!")
    call process_character (edna, appearance="blush false", text="Это должно дать твоему члену дополнительное сжатие!")
    call process_character (n, appearance="blush false", text="Хаах!")
    call process_character (n, appearance="blush false", text="Хнг!")

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
    show bg edna_bikini_titfuck_cumshot_surprise
    with Dissolve(1.5)

    pause
    $ quick_menu = True

    call process_character (edna, appearance="blush false", text="О, так хорошо, [n.say_name]!")
    call process_character (edna, appearance="blush false", text="Такая густая прекрасная сперма!")
    call process_character (n, appearance="blush false", text="Ух, ах, ох!")

    call static_still_ctc ("bg edna_bikini_titfuck_aftercum_surprise")

    call process_character (edna, appearance="blush false", text="(Насколько сильно он выстрелил?!)")
    call process_character (edna, appearance="blush false", text="(Он мог бы заполнить всю бутылку лосьона спермой!)")
    call process_character (n, appearance="blush false", text="Ах...")
    call process_character (n, appearance="blush false", text="{i}Фух.{/i}..")
    call process_character (edna, appearance="blush false", text="Все?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Д-да...")

    call static_still_ctc ("bg edna_bikini_titfuck_aftercum_smile")

    call process_character (edna, appearance="blush false", text="Помнишь, я говорила, что хорошие парни получают вознаграждение?")
    call process_character (edna, appearance="blush false", text="Я оправдала это заявление?")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (n, appearance="blush false", text="Ты точно сделал это, Бабушка.")
    call process_character (edna, appearance="blush false", text="И ты знаешь, как ты можешь стать особенным хорошим мальчиком?")
    call process_character (n, appearance="blush false", text="Как?")
    call process_character (edna, appearance="blush false", text="Не разглашай никаких подробностей о том, что мы делаем, когда ты приходишь сюда.")
    call process_character (edna, appearance="blush false", text="Если мама спросит, просто скажи, что ты хорошо провел время с бабушкой и что мы провели некоторое время на пляже.")
    call process_character (edna, appearance="blush false", text="Так ты будешь особенным хорошим мальчиком для бабушки?")
    call process_character (n, appearance="blush false", text="Я буду, Бабушка.")
    call process_character (edna, appearance="blush false", text="Чудесно.")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Ты хочешь печенья?")
    call process_character (edna, appearance="blush false", text="Давай сделаем, и мы можем принести их с собой на пляж!")
    call process_character (n, appearance="blush false", text="Можно к ним добавить кусочки шоколада?!")
    call process_character (edna, appearance="blush false", text="Только для такого особенного внука, как ты.")

    $ renpy.stop_predict("edna_titfuck_bikini_anim")
    python:
        edna.revistable_scenes.add("edna_scene_titfuck_revisit")
        if not dream:
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_big_breasts", 1)
            stats.add_stat("times_had_paizuri", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_penis_touched", 1)
            stats.add_stat("times_ejaculated", 1)

    call process_end_of_scene ("edna_scene_titfuck", char=edna, dream=dream)
    return

label edna_scene_titfuck_revisit:
    $ no_bust_art = False

    if "edna_scene_titfuck_revisit" in scenes_completed:
        call edna_scene_titfuck_revisit_2nd_time
    else:
        call edna_scene_titfuck_revisit_1st_time

    return

label edna_scene_titfuck_revisit_1st_time:
    $ renpy.start_predict("edna_titfuck_nude_anim")

    call process_character (edna, appearance="pose handhip face happy blush false mouth red", text="Ну, тебе не потребовалось много времени, чтобы спросить...")
    call process_character (edna, appearance="pose handhip face happy blush false mouth red", text="Ты проделал весь этот путь, чтобы поиграть с бабушкиной грудью?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Н-нет...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Это была не единственная причина.")
    call process_character (edna, appearance="pose handclasp face happy blush false mouth red", text="Ха-ха, все в порядке, [n.say_name]!")
    call process_character (edna, appearance="pose handclasp face happy blush false mouth red", text="Сегодня было немного скучно для меня.")
    call process_character (edna, appearance="pose handclasp face happy blush false mouth red", text="Но ты помогаешь оживить время!")

    call fade_to_black (1)

    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg edna_titrub")

    call process_character (edna, appearance="blush false", text="О, ты хотел бы сначала немного потереться?")
    call process_character (n, appearance="blush false", text="Я люблю трогать твои сиськи, Бабушка.")
    call process_character (n, appearance="blush false", text="То, как они подпрыгивают и покачиваются...")
    call process_character (edna, appearance="blush false", text="Ты бы хватал их все время, если бы мог?")
    call process_character (n, appearance="blush false", text="Еще бы!")
    call process_character (n, appearance="blush false", text="Я бы сжимал их, даже когда ты носишь рубашку!")
    call process_character (edna, appearance="blush false", text="Так что ты просто хочешь быть привязанным к ним, ха-ха!")
    call process_character (edna, appearance="blush false", text="Ты должен быть очень незаметным, если мы выйдем на улицу или на пляж, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Люди будут смотреть на нас смешно, если увидят мальчика, ласкающего пожилую женщину!")
    call process_character (n, appearance="blush false", text="Я буду осторожен, Бабушка.")
    call process_character (n, appearance="blush false", text="Но что насчет квартиры?")
    call process_character (edna, appearance="blush false", text="Это совсем другая история.")
    call process_character (edna, appearance="blush false", text="Если мы здесь, ты можешь схватить и прижать к своему сердцу!")
    call process_character (n, appearance="blush false", text="Все в порядке!")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Соси мой сосок, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Как в прошлый раз.")

    call static_still_ctc ("bg edna_titsuck")

    call process_character (edna, appearance="blush false", text="Мм, так мило...")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Знаешь, что у тебя очень мягкие губы, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Это хорошо?")
    call process_character (edna, appearance="blush false", text="Да для таких ситуаций!")
    call process_character (edna, appearance="blush false", text="Они бережно ласкают мои соски.")
    call process_character (edna, appearance="blush false", text="И ощущения феноменальные!")
    call process_character (edna, appearance="blush false", text="Оох!")
    call process_character (n, appearance="blush false", text="Ммф...")
    call process_character (n, appearance="blush false", text="Я не знал это, Бабушка.")
    call process_character (edna, appearance="blush false", text="По правде говоря, я всегда думала, что моя грудь не чувствительна.")
    call process_character (edna, appearance="blush false", text="Оказывается, у меня просто не было подходящего партнера, чтобы пробудить её!")
    call process_character (n, appearance="blush false", text="Значит, у меня все хорошо?")
    call process_character (edna, appearance="blush false", text="Позволь мне первой рассказать тебе...")
    call process_character (edna, appearance="blush false", text="Ты заработаешь много очков с женщинами, если сделаешь это с ними.")
    call process_character (n, appearance="blush false", text="Очки?")
    call process_character (edna, appearance="blush false", text="Скоро ты поймешь, что я имею в виду.")
    call process_character (edna, appearance="blush false", text="У меня много знаний на эту тему.")

    call static_still_ctc ("bg edna_titsuck_pull")

    call process_character (edna, appearance="blush false", text="{i}Ухх!{/i}")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (edna, appearance="blush false", text="Я знала, что в конце концов ты его увеличишь!")
    call process_character (edna, appearance="blush false", text="Хаа, да!")
    call process_character (edna, appearance="blush false", text="Можешь потянуть еще немного, если хочешь...")
    call process_character (n, appearance="blush false", text="Ммф!")
    call process_character (edna, appearance="blush false", text="Так хорошо, [n.say_name]!")
    call process_character (edna, appearance="blush false", text="(Его язык крутится вокруг моего соска!)")
    call process_character (edna, appearance="blush false", text="(Я становлюсь мокрой от этого...)")
    call process_character (n, appearance="blush false", text="(Я дергаю бабушку за сосок больше, чем раньше...)")
    call process_character (n, appearance="blush false", text="(Ей это действительно нравится!)")
    call process_character (edna, appearance="blush false", text="Ах...")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Хорошо, пришло время отплатить тебе тем же.")
    call process_character (edna, appearance="blush false", text="Сними эти шорты, [n.say_name].")
    call process_character (n, appearance="blush false", text="Я буду трахать твои сиськи, Бабушка?!")
    call process_character (edna, appearance="blush false", text="Да.")
    call process_character (edna, appearance="blush false", text="На этот раз, однако, я избавлюсь от этого надоедливого верха...")

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

    call process_character (n, appearance="blush false", text="Да, Бабушка!")
    call process_character (n, appearance="blush false", text="Это была хорошая идея - снять верх!")
    call process_character (edna, appearance="blush false", text="Не так ли?")
    call process_character (edna, appearance="blush false", text="Я знала, что ты одобришь.")
    call process_character (n, appearance="blush false", text="Теперь я могу потереть твои соски!")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Его энтузиазм никогда не иссякает)")
    call process_character (edna, appearance="blush false", text="(На самом деле, он увеличивается, в разгаре сиськотраха!)")
    call process_character (n, appearance="blush false", text="Бабушка...")
    call process_character (n, appearance="blush false", text="Я собираюсь изменить скорость всего за секунду.")
    call process_character (edna, appearance="blush false", text="Большая разница, когда ты так делаешь, не так ли?")
    call process_character (n, appearance="blush false", text="Да, это определенно так!")

    call edna_scene_titfuck_revisit_phase_2
    return

label edna_scene_titfuck_revisit_phase_2:
    $ quick_menu = False
    window hide
    show screen edna_titfuck_speed_settings(True, True)
    call screen progress_button_screen("Кончить!")
    $ renpy.scene('screens')
    hide screen edna_titfuck_speed_settings
    $ renpy.suspend_rollback(False)

    call edna_scene_titfuck_revisit_phase_3

    return

label edna_scene_titfuck_revisit_phase_3:
    if "edna_scene_titfuck_revisit" not in scenes_completed:
        $ quick_menu = True
        call edna_titfuck_set_speed (edna_titfuck_fastest_speed_multiplier)

        call process_character (n, appearance="blush false", text="Оох!")
        call process_character (n, appearance="blush false", text="Мм!")
        call process_character (edna, appearance="blush false", text="Буду ли я ожидать чего-то в ближайшее время, [n.say_name]?")
        call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}")
        call process_character (edna, appearance="blush false", text="Ворвись спермой, [n.say_name].")
        call process_character (edna, appearance="blush false", text="Обели мои сиськи своей спермой.")

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

        call process_character (n, appearance="blush false", text="Гааах!")
        call process_character (edna, appearance="blush false", text="(Он выстрелил довольно далеко!)")
        call process_character (edna, appearance="blush false", text="(Он попал мне на подбородок!)")

        call static_still_ctc ("bg edna_nude_titfuck_aftercum_smile")

        call process_character (edna, appearance="blush false", text="Ммм, замечательно, [n.say_name]...")
        call process_character (edna, appearance="blush false", text="Именно этого я и ожидала от внука.")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="В тот раз было много спермы.")
        call process_character (edna, appearance="blush false", text="Я бы рискнула предположить, что это был твой самое большое количество!")
        call process_character (edna, appearance="blush false", text="Но я знаю, что ты быстро улучшишь результат!")
    else:

        pause 0.1
        $ renpy.scene('screens')
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

        call process_character (n, appearance="blush false", text="Аах!")
        call process_character (edna, appearance="blush false", text="Ммм, так много кончил, [n.say_name]...")

        call static_still_ctc ("bg edna_nude_titfuck_aftercum_smile")

        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Спасибо, Бабушка.")
        call process_character (n, appearance="blush false", text="Твои сиськи всегда так хороши.")
        call process_character (edna, appearance="blush false", text="Не стоит благодарности.")
        call process_character (edna, appearance="blush false", text="...")
        call process_character (edna, appearance="blush false", text="(Я не хочу, чтобы семя [n.say_name] пропало)")
        call process_character (edna, appearance="blush false", text="(Может быть, в следующий раз я прослежу, чтобы этого не произошло...)")

    call edna_scene_titfuck_revisit_end

    return

label edna_scene_titfuck_revisit_2nd_time:
    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    $ scene_anim = IA_Animation_Edna_Titfuck_Nude_Info()
    $ scene_anim.pause()
    $ no_bust_art = True

    $ edna_titfuck_had_slow_speed_message = False
    $ edna_titfuck_had_normal_speed_message = False
    $ edna_titfuck_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    $ set_main_animation_speed(1.0)
    show anim_nothing_image as main_animation at main_animation_transform(scene_anim)
    with Dissolve(1.15)
    show bg white

    pause 
    $ quick_menu = True

    call process_character (edna, appearance="blush false", text="В полной готовности, [n.say_name]?")
    call process_character (edna, appearance="blush false", text="Как хочешь начать?")

    menu:
        "Медленно":
            $ scene_anim.unpause()
            $ set_main_animation_speed(edna_titfuck_slow_speed_multiplier)
            call process_character (edna, appearance="blush false", text="Знаешь, это полезно для кровообращения.")
            call process_character (edna, appearance="blush false", text="Мой пульс уже растёт!")
            call edna_titfuck_go_slow (True, False, True)
        "Нормально":
            $ scene_anim.unpause()
            $ set_main_animation_speed(1.0)
            call process_character (edna, appearance="blush false", text="Так приятно видеть, что моя грудь не пропадет даром!")
            call process_character (edna, appearance="blush false", text="У них новая цель в жизни для моего внука!")
            call edna_titfuck_go_normal (True, False, True)
        "Быстро":
            $ scene_anim.unpause()
            $ set_main_animation_speed(edna_titfuck_fast_speed_multiplier)
            call process_character (edna, appearance="blush false", text="О боже...")
            call process_character (edna, appearance="blush false", text="С места в карьер!")
            call process_character (edna, appearance="blush false", text="Это та сторона тебя, которую я хотела бы видеть больше, [n.say_name]!")

            call add_boldness (1, tag="edna_titfuck_revisit_2nd_time_go_fast")
            call edna_titfuck_go_fast (True, False, True)
    return

label edna_scene_titfuck_revisit_end:
    $ scene_anim = None
    $ renpy.stop_predict("edna_titfuck_nude_anim")

    python:
        stats.add_stat("times_seen_breasts", 1)
        stats.add_stat("times_seen_big_breasts", 1)
        stats.add_stat("times_had_paizuri", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_penis_touched", 1)
        stats.add_stat("times_ejaculated", 1)



    call process_end_of_scene ("edna_scene_titfuck_revisit", char=edna, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label edna_scene_blowjob(dream=False):
    call edna_scene_blowjob_sex (dream=dream)
    return
label edna_scene_blowjob_sex(dream=False):
    call process_scene_beginning (bg="bg edna_house_daytime", char_tuple_array=[ (n, "outfit clothesjacket pose handpocket"), (edna, "outfit clothes pose handhip face happy blush false mouth red") ], dream=dream )

    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false mouth red", text="[n.say_name]!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false mouth red", text="Ты зашёл в нужный день!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Почему Бабушка?")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Сегодня ежегодная летняя пляжная вечеринка!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Все жители кондоминиума собираются на большой ужин у океана.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Мне было предложено принести мою высоко оцененную помадку и печенье.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Звучит интересно.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Какая там будет еда?")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false mouth red", text="Все, что только можно придумать!")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false mouth red", text="Будут мясо, фрукты, овощи, супы, чипсы...")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false mouth red", text="Это огромное разнообразие!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="От этого я уже проголодался.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Я умираю с голоду!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Давай пойдем и насытимся хорошей едой!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Звучит хорошо для меня, Бабушка!")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false mouth red", text="And don't be afraid to bring back extra portions to the condo.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false mouth red", text="Соседи говорят, что там всегда слишком много объедков, и мы не хотим тратить их впустую!")

    call fade_to_black (1)


    call process_new_location ("bg edna_house_evening", dream=dream)


    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false mouth red")

    call process_character (n, appearance="outfit clothesjacket pose handpocket face aroused blush false", text="Ничего себе, я так сыт...")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="Не удивительно!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="Ты съел почти две полные тарелки еды!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Все было так вкусно!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Я хотел попробовать всё!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Ты так наелся, что не захотел десерта.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Вот это было потрясающе!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Но мы принесли торт и пирог на потом.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Я не хотел пропустить это.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false mouth red", text="Я не знала, что у них был выбор вин в этом году.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false mouth red", text="Были некоторые напитки очень высокого качества, подаваемые.")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Также были и коктейли!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Клубнично-банановый был моим любимым.")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="Я видел, как ты нечаянно потягивал алкоголь!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Сначала я подумал, что с ним что-то не так.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Как будто клубника была кислой.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Хаха!")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Ты еще не совсем готов к такому напитку.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="И ты можешь никогда им не стать.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false mouth red", text="Твоей маме тоже никогда не нравился вкус алкоголя.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Это было слишком крепко.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false mouth red", text="Я предпочитаю более мягкие вещи, такие как красное вино.")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false mouth red", text="Это дает мне приятный, легкий кайф.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Кайф?")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false mouth red", text="Это расслабляет меня, вот что я имею в виду.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false mouth red", text="Я пила вино десятилетиями.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false mouth red", text="И теперь я слышу, что это помогает замедлить процесс старения!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false mouth red", text="Звучит неплохо для меня!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Это классно, Бабушка.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Я слышал, как люди говорили, как хорошо ты выглядишь для своего возраста.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false mouth red", text="Я знаю, люди часто говорят, что старение сводится к выбору образа жизни.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false mouth red", text="Но я думаю, что тебе повезло с твоей генетикой.")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="Возможно, это означает, что ты останешься молодым, в течение длительного времени, [n.say_name]!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Ты так думаешь?")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="Время, безусловно, покажет!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="...")
    call process_character (edna, appearance="outfit clothes pose handclasp face flirt blush false mouth red", text="...")
    call process_character (edna, appearance="outfit clothes pose handclasp face flirt blush false mouth red", text="Здорово, что мы можем проводить время вместе, [n.say_name].")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="И мне тоже, Бабушка.")
    call process_character (edna, appearance="outfit clothes pose handclasp face flirt blush false mouth red", text="У меня столько жизненного опыта.")
    call process_character (edna, appearance="outfit clothes pose handclasp face flirt blush false mouth red", text="Это значительно опередит тебя!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Ты очень помогла с этим уже бабушка, да!")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false mouth red", text="...{p}...")

    call display_multiple_characters ([ (edna, "pose handhip face happy blush false position edna_special2"), (n, "outfit clothesjacket pose handpocket face curious blush false position nate_more_right") ] )

    call process_character (edna, appearance="pose handhip face happy blush false position edna_special2", text="Позволь мне подойти немного ближе, [n.say_name].")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Я бы хотела оттянуться с тобой.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (edna, appearance="pose fisthip face flirt blush false", text="Знаешь...")
    call process_character (edna, appearance="pose fisthip face flirt blush false", text="Есть еще многое, чему ты можешь научиться у меня\n[n.say_name].")
    call process_character (edna, appearance="pose handhip face flirt blush false", text="Это преимущество более старой\nженщины.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Да...")
    call process_character (edna, appearance="pose handhip face happy blush false", text="...")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Мне было интересно, [n.say_name]...")
    call process_character (edna, appearance="pose handclasp face flirt blush false", text="Когда ты трахаешь мои сиськи, или когда я дрочу тебе...")
    call process_character (edna, appearance="pose handclasp face flirt blush false", text="Ты не возражаешь, что это делает твоя \nБабушка?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Нет, я совсем не против.")
    call process_character (edna, appearance="pose fisthip face flirt blush false", text="Так это совершенно нормально иметь сексуальные отношения\nс членами семьи?")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Да!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="У меня нет проблем с этим.")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Я думаю, что это здорово!")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Это замечательно, [n.say_name]!")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Согласен и поддерживаю тебя на сто процентов!")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="У тебя не должно быть с этим проблем.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Почему ты спрашиваешь, Бабушка?")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Ну...")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Некоторые скажут, что ты не должен, или это не нормально...")
    call process_character (edna, appearance="pose fisthip face curious blush false", text="Но зачем другим людям говорить тебе, что\nнормально?")
    call process_character (edna, appearance="pose fisthip face curious blush false", text="Я верю, что только ты можешь принять такое решение.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Я понимаю, о чем ты говоришь, Бабушка.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="И знаешь что?")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="...")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Если ты захочешь заняться сексом со своей сестрой [sa.say_name] или\n[k.say_name], или даже захочешь переспать с Мамой...")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Я говорю, действуй!")

    if "simone_scene_blowjob" in scenes_completed or "kira_scene_tip_blowjob" in scenes_completed or "sam_scene_vaginal" in scenes_completed:
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Так ты будешь в порядке, если я займусь сексом с одной из них?")
        call process_character (edna, appearance="pose handhip face happy blush false", text="Просто знай, я буду за то, что ты\nрешишь.")
        call process_character (edna, appearance="pose handhip face happy blush false", text="Это то, что бабушки должны делать в конце\nконцов.")
        call process_character (n, appearance="pose handpocket face concerned blush false", text="...")
        call process_character (n, appearance="pose handpocket face concerned blush false", text="Что если.....{w=1.0}я занимался сексом с одной из них\nуже бабушка...")
        call process_character (edna, appearance="pose handhip face neutral blush false", text="Тогда все, что я могу сказать...")
        call process_character (edna, appearance="pose handclasp face happy blush false", text="Если тебе нравится, продолжай трахаться!")
        call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    else:
        call process_character (n, appearance="pose behindhead face curious blush false", text="Думаешь, мне стоит, Бабушка?")
        call process_character (edna, appearance="pose handhip face neutral blush false", text="Это полностью зависит от тебя, [n.say_name].")
        call process_character (edna, appearance="pose handhip face neutral blush false", text="Просто знай, я буду  за то, что ты\nрешишь.")
        call process_character (edna, appearance="pose handhip face happy blush false", text="Это то, что бабушки должны делать в конце\nконцов.")
        call process_character (n, appearance="pose handpocket face curious blush false", text="...")

    call process_character (edna, appearance="pose handclasp face flirt blush false", text="Мм...")
    call process_character (edna, appearance="pose handclasp face flirt blush false", text="...")
    call process_character (edna, appearance="pose handhip face flirt blush false", text="Я не знаю, вино ли это, или о чем мы говорим, но ... ..")
    call process_character (edna, appearance="pose handhip face flirt blush false", text="Я сейчас действительно в настроении.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="В настроении для чего бабушка?")

    call character_leave_dissolve (edna)
    pause 0.5

    call process_character (edna, appearance="outfit nude")
    pause 0.5


    call process_character (edna, appearance="outfit naked pose fisthip face flirt blush false")


    call process_character (edna, appearance="outfit naked pose fisthip face flirt blush false")

    call process_character (n, appearance="pose behindhead face concerned blush true", text="О-Ох...")
    call process_character (edna, appearance="outfit naked pose fisthip face happy blush false", text="Я знала, что ты быстро соединишь точки.")
    call process_character (edna, appearance="outfit naked pose fisthip face happy blush false", text="Присоединяйтесь ко мне [n.say_name]...{w=1.0}раздевайся.")
    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face neutral blush false", text="Конечно, Бабушка.")

    call character_leave_dissolve (n)
    pause 0.5


    call process_character (n, appearance="outfit nudehard pose handsdown face neutral blush false")

    call process_character (edna, appearance="outfit naked pose handclasp face happy blush false", text="...")
    call process_character (edna, appearance="outfit naked pose handclasp face happy blush false", text="(Я не думала, что я буду возбуждаться\nна этом пляже)")
    call process_character (edna, appearance="outfit naked pose handclasp face flirt blush false", text="(Но на самом деле я поймала себя, пытаясь\nсхватить промежность [n.say_name])")
    call process_character (edna, appearance="outfit naked pose handclasp face flirt blush false", text="([n.say_name] сжимал мои\nгруди, но только тогда, когда никто не смотрел...)")
    call process_character (edna, appearance="outfit naked pose handclasp face flirt blush false", text="...{p}...")

    call process_character (edna, appearance="outfit naked pose handclasp face flirt blush false position edna_special3")

    if stats.stat_value('times_received_blowjob'):
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="(Бабушка думает о том, чтобы сосать мой пенис?)")
        call process_character (n, appearance="pose twohandfist face aroused blush true", text="(О боже мой!)")
        call process_character (n, appearance="pose twohandfist face aroused blush true", text="(Я был бы рад, если бы она это сделала!)")
    else:
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (n, appearance="pose behindhead face curious blush false", text="(Что бабушка думает сделать на этот раз?)")
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (n, appearance="pose handsdown face curious blush false", text="(Ее рот довольно близко к моему пенису...)")
        call process_character (n, appearance="pose handsdown face curious blush false", text="...")
        call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="(Она собирается сосать его?!)")
        call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="...{p}...")
        call process_character (n, appearance="pose behindhead face aroused blush true", text="(Что... {w=1.0}было бы здорово, если бы она это сделала...)")


    call process_character (edna, appearance="outfit naked pose fisthip face happy blush false", text="Посмотрите, как отреагировала эта часть твоего тела, [n.say_name].")
    call process_character (edna, appearance="outfit naked pose fisthip face happy blush false", text="Это та часть, которую я ожидала.")
    call process_character (n, appearance="outfit nudehard pose handsdown face aroused blush true", text="...")
    call process_character (edna, appearance="outfit naked pose handclasp face flirt blush false", text="Ох...{w=1.0}Я хочу попробовать твой член, [n.say_name].")
    call process_character (edna, appearance="outfit naked pose handclasp face flirt blush false", text="...")
    call process_character (edna, appearance="outfit naked pose handclasp face flirt blush false", text="Можешь прилечь для меня?")
    call process_character (edna, appearance="outfit naked pose handclasp face flirt blush false", text="Обещаю, оно того стоит...")

    call fade_to_black (1)

    call process_character (n, appearance="outfit nudehard pose handsdown face aroused blush true", text="...{p}...")
    call process_character (edna, appearance="outfit naked pose handclasp face flirt blush false", text="Спасибо тебе.")
    call process_character (edna, appearance="outfit naked pose handclasp face flirt blush false", text="Теперь я покажу тебе, что я могу сделать.")


    if not dream or persistent.disable_dream_music:
        $ play_music("audio/music/Sensual Groove.ogg", fadein = 1.0)

    call static_still_ctc ("bg edna_tipsuck")

    call process_character (n, appearance="blush false", text="Хаа!")
    call process_character (edna, appearance="blush false", text="Аах, Ммм...")
    call process_character (edna, appearance="blush false", text="Я сделаю его красивым и влажным.")
    call process_character (n, appearance="blush false", text="Да, Бабушка, да!")
    call process_character (edna, appearance="blush false", text="(Я поработаю над верхушкой...)")
    call process_character (n, appearance="blush false", text="Ох, ох!")
    call process_character (n, appearance="blush false", text="(Она делает этот маленький отсос на вершине моего пениса!)")
    call process_character (edna, appearance="blush false", text="Ммф...")
    call process_character (edna, appearance="blush false", text="(У него такой гладкий ствол!)")
    call process_character (edna, appearance="blush false", text="(Мои губы скользят по поверхности его члена с легкостью!)")
    call process_character (n, appearance="blush false", text="Ахх...")
    call process_character (n, appearance="blush false", text="Ты великолепна, Бабушка!")
    call process_character (edna, appearance="blush false", text="Есть много методов, которые мне еще предстоит раскрыть, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Я продемонстрирую некоторые из моих любимых.")
    call process_character (n, appearance="blush false", text="П-пожалуйста, сделай это, Бабушка.")
    call process_character (n, appearance="blush false", text="Ах!")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Это как-будто я старый мастер, а он - молодой ученик)")
    call process_character (edna, appearance="blush false", text="([n.say_name] многому научится...{w=1.0}но я думаю, что он готов к этому)")
    call process_character (edna, appearance="blush false", text="(Его член, конечно!)")
    call process_character (n, appearance="blush false", text="Ммм...")
    call process_character (edna, appearance="blush false", text="(Я надеюсь, что помада не будет слишком сильно видна на члене [n.say_name])")

    if "simone_scene_blowjob" in scenes_completed or "kira_scene_tip_blowjob" in scenes_completed or "sam_scene_vaginal" in scenes_completed:
        call process_character (edna, appearance="blush false", text="(Последнее, что мне нужно, это чтобы одна из его сестер или его мама увидели это и соединили точки...)")
        call process_character (edna, appearance="blush false", text="...")
        call process_character (edna, appearance="blush false", text="(Интересно, с кем [n.say_name] трахался из них?)")
        call process_character (edna, appearance="blush false", text="...")
        call process_character (edna, appearance="blush false", text="(Я уверена, что скоро узнаю)")
    else:
        call process_character (edna, appearance="blush false", text="(Если это так, я должна убедиться, что он тщательно моет его перед отъездом)")
        call process_character (edna, appearance="blush false", text="(Мне нужно, чтобы мои следы были убраны)")

    call process_character (n, appearance="blush false", text="Хаа!")
    call process_character (n, appearance="blush false", text="Продолжай сосать у меня, Бабушка!")
    call process_character (edna, appearance="blush false", text="Если это то, что ты хочешь, это то, что ты получишь, [n.say_name]!")

    call static_still_ctc ("bg edna_blowjob _nocum")

    call process_character (n, appearance="blush false", text="Ух ты! Ах!")
    call process_character (edna, appearance="blush false", text="Ммф, Ммм...")
    call process_character (edna, appearance="blush false", text="Как тебе это сосание, [n.say_name]?")
    call process_character (n, appearance="blush false", text="(Весь мой член сжимается ее ртом!)")
    call process_character (n, appearance="blush false", text="(Как она это делает?!)")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Член моего внука получает удовольствие от многих лет опыта)")
    call process_character (edna, appearance="blush false", text="(Смотри [n.say_name]...{w=1.0}вот почему тебе нужна пожилая женщина)")
    call process_character (edna, appearance="blush false", text="(Ты всегда будешь получать лучшее возбуждение каждый раз...)")
    call process_character (n, appearance="blush false", text="Га-хаа!")
    call process_character (edna, appearance="blush false", text="(Я получаю удовольствие от [n.say_name]...{w=1.0}[n.say_name] получает удовольствие от меня...)")
    call process_character (edna, appearance="blush false", text="(Мы имеем полную свободу вместе)")
    call process_character (edna, appearance="blush false", text="(Но мы должны проводить время вместе отдельно от семейных собраний)")
    call process_character (edna, appearance="blush false", text="([n.say_name] не сможет тянуться к моим сиськам, пока его мама и сестры за обеденным столом)")
    call process_character (edna, appearance="blush false", text="(Этому [n.say_name] придется научиться управлять...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Это безумие, я не знал об этой стороне бабушки до лета)")
    call process_character (n, appearance="blush false", text="(Жаль, что я не узнал об этом раньше!)")
    call process_character (n, appearance="blush false", text="(Кто знает что бы мы делали сейчас, если бы она начала сосать у меня в прошлом году!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Хотя, я был намного дальше от этого места больше года назад...)")
    call process_character (n, appearance="blush false", text="(И я не мог ходить сюда один до недавнего времени)")
    call process_character (n, appearance="blush false", text="(Это было лучшее решение, которое я когда-либо делал!)")

    call static_still_ctc ("bg edna_blowjob _foreskinplay")

    call process_character (edna, appearance="blush false", text="Ммм...")
    call process_character (edna, appearance="blush false", text="Есть много крайней плоти для меня, чтобы играться!")
    call process_character (n, appearance="blush false", text="Ах...")
    call process_character (n, appearance="blush false", text="В-Вау!")
    call process_character (edna, appearance="blush false", text="У тебя очень чувствительный член.")
    call process_character (edna, appearance="blush false", text="Больше, чем я предполагала.")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="([n.say_name] должно быть сходит с ума, когда не может облегчиться)")
    call process_character (edna, appearance="blush false", text="(Я удивлена, что у него раньше не было несчастного случая в штанах)")
    call process_character (edna, appearance="blush false", text="(Я думаю, он смог добраться сюда в самый последний момент)")
    call process_character (edna, appearance="blush false", text="(Чем быстрее мы доберемся до места действия, тем лучше!)")

    if stats.stat_value('times_cummed_in_mouth'):
        call process_character (n, appearance="blush false", text="Бабушка...")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Можно мне...{w=1.0}кончить тебе в рот?")
        call process_character (edna, appearance="blush false", text="Ах да, просьба каждого молодого человека...")
        call process_character (edna, appearance="blush false", text="Да, [n.say_name], ты можешь.")
        call process_character (edna, appearance="blush false", text="Посмотрим, сможешь ли ты наполнить мой рот...")

    call static_still_ctc ("bg edna_blowjob _nocum")

    call process_character (n, appearance="blush false", text="Ох, ох...")
    call process_character (n, appearance="blush false", text="Это круто, Бабушка...")
    call process_character (edna, appearance="blush false", text="Мм, мм...")
    call process_character (edna, appearance="blush false", text="(Это заставит [n.say_name] кончить, гарантировано...)")
    call process_character (edna, appearance="blush false", text="(Я двигаюсь быстрее, его член имеет мало шансов)")
    call process_character (edna, appearance="blush false", text="(И так начинается обратный отсчет...)")
    call process_character (n, appearance="blush false", text="{i}Ухх.{/i}..")
    call process_character (n, appearance="blush false", text="Хии, аах...")
    call process_character (n, appearance="blush false", text="(Мои яйца сейчас взорвутся!)")
    call process_character (n, appearance="blush false", text="(И мой член горячий!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я почти, Бабушка!")
    call process_character (n, appearance="blush false", text="Я это чувствую!")
    call process_character (edna, appearance="blush false", text="Вот что я хотела услышать, [n.say_name]...")
    call process_character (n, appearance="blush false", text="Ох...")
    call process_character (n, appearance="blush false", text="Ааах, да!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg edna_blowjob _natetongue_cum")

    call process_character (n, appearance="blush false", text="Гаах!")
    call process_character (edna, appearance="blush false", text="Ммглбл!")
    call process_character (edna, appearance="blush false", text="(Такая густая!)")
    call process_character (edna, appearance="blush false", text="(Я никак не могу удержать всё это!)")
    call process_character (n, appearance="blush false", text="Ха, ха...")
    call process_character (edna, appearance="blush false", text="([n.say_name] так много выстрелил!)")
    call process_character (edna, appearance="blush false", text="(Сперма на моем подбородке, моих губах, его члене...)")
    call process_character (edna, appearance="blush false", text="(Я должна была ожидать такого извержения!)")
    call process_character (n, appearance="blush false", text="Ух, ах...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я думаю, что это всё, Бабушка.")

    call static_still_ctc ("bg edna_blowjob _foreskinplay_cum")

    call process_character (edna, appearance="blush false", text="Я действительно не была готова к твоему оргазму, [n.say_name]...")
    call process_character (edna, appearance="blush false", text="В результате я превратила твой член в неряшливое месиво.")
    call process_character (n, appearance="blush false", text="Не беспокойся, Бабушка.")
    call process_character (n, appearance="blush false", text="Нам просто нужно полотенце, чтобы вытереть все это.")
    call process_character (edna, appearance="blush false", text="В этом нет необходимости.")
    call process_character (n, appearance="blush false", text="Да?")
    call process_character (edna, appearance="blush false", text="Кому нужно полотенце, если я могу просто использовать свой рот, чтобы высосать все это?")
    call process_character (edna, appearance="blush false", text="{i}Хлёёб!{/i}")
    call process_character (edna, appearance="blush false", text="Твой член скоро будет безупречно чистым, [n.say_name]!")
    call process_character (edna, appearance="blush false", text="Ммм...")
    call process_character (edna, appearance="blush false", text="(Кажется, я нашла свой десерт)")
    call process_character (edna, appearance="blush false", text="(Так вкусно...)")

    python:
        edna.revistable_scenes.add("edna_scene_blowjob_revisit")

        if not dream:
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_had_foreskin_played_with", 1)
            stats.add_stat("times_given_facial", 1)
            stats.add_stat("times_received_blowjob", 1)
            stats.add_stat("times_cummed_in_mouth", 1)

    call process_end_of_scene ("edna_scene_blowjob", char=edna, dream=dream)

    return

label edna_scene_blowjob_revisit:
    $ no_bust_art = False

    if "edna_scene_blowjob_revisit" in scenes_completed:
        call edna_scene_blowjob_revisit_2nd_time
    else:
        call edna_scene_blowjob_revisit_1st_time

    return

label edna_scene_blowjob_revisit_1st_time:
    call process_character (edna, appearance="pose handclasp face happy blush false mouth red", text="Ты же не думал, что мой минет был один и всё, не так ли?")
    call process_character (edna, appearance="pose handclasp face happy blush false mouth red", text="Мы только начали!")

    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)
    call static_still_ctc ("bg edna_tipsuck")

    call process_character (n, appearance="blush false", text="Мм, Бабушка...")
    call process_character (n, appearance="blush false", text="Как ты научилась так хорошо сосать?")
    call process_character (edna, appearance="blush false", text="Я провела довольно много времени вокруг этой части тела.")
    call process_character (edna, appearance="blush false", text="На данный момент я знаю все способы угодить члену.")
    call process_character (edna, appearance="blush false", text="И с тех пор, как ты позволил мне свободно править...")
    call process_character (edna, appearance="blush false", text="Это позволяет мне персонализировать твоё удовольствие.")
    call process_character (n, appearance="blush false", text="Персонализировать?")
    call process_character (n, appearance="blush false", text="Ты хочешь сказать, что знаешь, что лучше всего работает на мне?")
    call process_character (edna, appearance="blush false", text="Ммф...")
    call process_character (edna, appearance="blush false", text="Например, я знаю, что у тебя чувствительность выше среднего.")
    call process_character (edna, appearance="blush false", text="Вот почему я так сосредоточена на головке.")
    call process_character (n, appearance="blush false", text="Оох, аах!")
    call process_character (edna, appearance="blush false", text="Видишь?")
    call process_character (edna, appearance="blush false", text="Каждый раз, когда я отсасываю, ты реагируешь.")
    call process_character (n, appearance="blush false", text="Т-ты права, я понимаю...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Бабушка, ультра эксперт в этом!)")

    $ edna_scene_blowjob_had_a_blowjob_from_someone_else = False
    $ edna_scene_blowjob_had_a_blowjob_outside_immediate_family = False
    $ edna_scene_blowjob_blowjob_outside_immediate_family_char = ""

    if "kira_scene_tip_blowjob" in scenes_completed:
        $ edna_scene_blowjob_had_a_blowjob_from_someone_else = True
        call process_character (n, appearance="blush false", text="([k.say_name] действительно хороша в этом тоже)")
        call process_character (n, appearance="blush false", text="(Она сосет супер жёстко!)")
        call process_character (n, appearance="blush false", text="(И она может засунуть весь мой член в рот!)")

    if "simone_scene_blowjob" in scenes_completed:
        $ edna_scene_blowjob_had_a_blowjob_from_someone_else = True
        call process_character (n, appearance="blush false", text="(Мама тоже делает потрясающую работу...)")
        call process_character (n, appearance="blush false", text="(Она любит сосать у меня медленно и осторожно)")
        call process_character (n, appearance="blush false", text="(Он чувствует себя безумно хорошо!)")

    if "sam_scene_blowjob" in scenes_completed:
        $ edna_scene_blowjob_had_a_blowjob_from_someone_else = True
        call process_character (n, appearance="blush false", text="(Мне нужно узнать, может ли [sa.say_name] научиться сосать у меня так...)")
        call process_character (n, appearance="blush false", text="(Она уже делает хорошую работу, но это вознесёт её минет на совершенно новый уровень!)")

    if "vicky_scene_blowjob" in scenes_completed:
        $ edna_scene_blowjob_had_a_blowjob_from_someone_else = True
        $ edna_scene_blowjob_had_a_blowjob_outside_immediate_family = True
        $ edna_scene_blowjob_blowjob_outside_immediate_family_char = "Vicky"

    if "gloryhole_scene_blowjob" in scenes_completed:
        $ edna_scene_blowjob_had_a_blowjob_from_someone_else = True
        $ edna_scene_blowjob_had_a_blowjob_outside_immediate_family = True
        $ edna_scene_blowjob_blowjob_outside_immediate_family_char = "Kacey"

    if "janet_scene_blowjob" in scenes_completed:
        $ edna_scene_blowjob_had_a_blowjob_from_someone_else = True
        $ edna_scene_blowjob_had_a_blowjob_outside_immediate_family = True
        $ edna_scene_blowjob_blowjob_outside_immediate_family_char = janet.say_name

    if "julia_scene_blowjob" in scenes_completed:
        $ edna_scene_blowjob_had_a_blowjob_from_someone_else = True
        $ edna_scene_blowjob_had_a_blowjob_outside_immediate_family = True
        $ edna_scene_blowjob_blowjob_outside_immediate_family_char = julia.say_name

    if edna_scene_blowjob_had_a_blowjob_outside_immediate_family:
        call process_character (n, appearance="blush false", text="(Удивительно, насколько по-другому Бабушка чувствуется по сравнению с кем-то вроде [edna_scene_blowjob_blowjob_outside_immediate_family_char].")
        call process_character (n, appearance="blush false", text="(Я уверен, что есть неограниченные способы наслаждаться тем, что мой член сосут!)")

    if not edna_scene_blowjob_had_a_blowjob_from_someone_else:
        call process_character (n, appearance="blush false", text="(Я не знаю, могу ли я сравнить это чувство с чем-либо еще, что я чувствовал раньше...)")
        call process_character (n, appearance="blush false", text="(Это то, что я хотел бы на свой день рождения или праздники!)")

    call static_still_ctc ("bg edna_blowjob _foreskinplay")

    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (n, appearance="blush false", text="Я как раз собирался попросить тебя сделать это, Бабушка!")
    call process_character (edna, appearance="blush false", text="Это моя интуиция, [n.say_name].")
    call process_character (edna, appearance="blush false", text="У меня было чувство, что ты хочешь поиграть со своей крайней плотью.")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(У [n.say_name] уже довольно грязный ум)")
    call process_character (edna, appearance="blush false", text="(Я бы солгала себе, если бы сказала, что я не способствовала этому, хе-хе...)")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Но я думаю [n.say_name] предрасположен быть таким образом)")
    call process_character (edna, appearance="blush false", text="(Он происходит из семьи, которая не стесняется сексуальных отклонений!)")
    call process_character (edna, appearance="blush false", text="(Хотя мы никогда не заходили так далеко, чтобы заниматься сексом с членами семьи...)")
    call process_character (edna, appearance="blush false", text="([n.say_name] разрушил этот барьер на части!)")
    call process_character (edna, appearance="blush false", text="(Я знаю [si.say_name] пыталась держать поведение в узде, пока он не стал старше)")
    call process_character (edna, appearance="blush false", text="(Но я знаю, что это не продлится долго)")
    call process_character (edna, appearance="blush false", text="(Все к лучшему, на мой взгляд!)")
    call process_character (edna, appearance="blush false", text="(Это просто означает, что [n.say_name] может проводить чертовски хорошо время!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я надеюсь, что как только начнется школа, бабушка сможет забрать меня по случаю)")
    call process_character (n, appearance="blush false", text="(Таким образом она могла сосать у меня в машине, как только я выйду!)")
    call process_character (n, appearance="blush false", text="(Приход к ней на выходные дни будет обязательным!)")
    call process_character (edna, appearance="blush false", text="Мне нужен...")
    call process_character (edna, appearance="blush false", text="Мне нужен этот член глубоко в горле!")

    call static_still_ctc ("bg edna_blowjob _nocum")

    call process_character (edna, appearance="blush false", text="Ммм, Мммм...")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (n, appearance="blush false", text="Потрясающе, Бабушка...")
    call process_character (edna, appearance="blush false", text="Ммм...")
    call process_character (edna, appearance="blush false", text="Прежде чем ты это узнаешь, [n.say_name]...")
    call process_character (edna, appearance="blush false", text="Ты хочешь вытащить свой член, как только входишь в мою дверь!")
    call process_character (n, appearance="blush false", text="Ах...")
    call process_character (n, appearance="blush false", text="Я думаю, что ты права...")
    call process_character (edna, appearance="blush false", text="Мы можем проводить больше времени вне нашей одежды, чем с ней!")
    call process_character (n, appearance="blush false", text="Мы можем сделать это, Бабушка?")
    call process_character (n, appearance="blush false", text="Мы можем быть голыми большую часть времени?")
    call process_character (edna, appearance="blush false", text="Хм...")
    call process_character (edna, appearance="blush false", text="Посмотрим, что я смогу сделать.")
    call process_character (edna, appearance="blush false", text="По крайней мере, я могу раздеться, пока здесь только ты и я!")
    call process_character (n, appearance="blush false", text="Да!")
    call process_character (n, appearance="blush false", text="Я бы хотел видеть тебя голой все больше и больше времени, Бабушка!")
    call process_character (edna, appearance="blush false", text="О, я знаю, что ты хочешь, ха-ха.")
    call process_character (edna, appearance="blush false", text="И я бы хотела увидеть твой член, размахивающий в моей квартире!")

    call static_still_ctc ("bg edna_blowjob _natetongue_nocum")

    call process_character (n, appearance="blush false", text="Я готов кончить, Бабушка!")
    call process_character (n, appearance="blush false", text="Это будет все в рот!")
    call process_character (edna, appearance="blush false", text="Именно так, как я хочу, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Ммф...")
    call process_character (n, appearance="blush false", text="Хррм, гах...")
    call process_character (n, appearance="blush false", text="Вот!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg edna_blowjob _natetongue_cum")

    call process_character (n, appearance="blush false", text="{i}Ухх!{/i}")
    call process_character (edna, appearance="blush false", text="(Ох!)")
    call process_character (edna, appearance="blush false", text="(Я чуть не подавилась!)")
    call process_character (edna, appearance="blush false", text="(Часть попало мне прямо в горло!)")
    call process_character (edna, appearance="blush false", text="(Рада, что у меня рвотный рефлекс...)")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (n, appearance="blush false", text="...")

    call static_still_ctc ("bg edna_blowjob _foreskinplay_cum")

    call process_character (edna, appearance="blush false", text="Там еще много спермы здесь для меня, чтобы наслаждаться!")
    call process_character (edna, appearance="blush false", text="Она густая, [n.say_name].")
    call process_character (n, appearance="blush false", text="И это хорошо, да?")
    call process_character (edna, appearance="blush false", text="Это, безусловно, самое лучшее.")
    call process_character (edna, appearance="blush false", text="Я могу пропустить обед после того, как выпью все это!")

    call edna_scene_blowjob_revisit_end

    return

label edna_scene_blowjob_revisit_2nd_time:
    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg edna_tipsuck")

    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Я рада, что они укрепили эти стены кондоминиума бетоном и изоляцией)")
    call process_character (edna, appearance="blush false", text="(Когда я сосу хер [n.say_name] он создает гораздо больше шума, чем я думала)")
    call process_character (edna, appearance="blush false", text="(До сих пор я не получила никаких жалоб на шум, что хорошо)")
    call process_character (edna, appearance="blush false", text="(Я хочу иметь возможность наслаждаться членом моего внука!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Мне нужно попросить бабушку как-нибудь приехать ко мне домой!)")
    call process_character (n, appearance="blush false", text="(Было бы здорово, если бы она осталась на несколько ночей!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Как мы можем координировать что-то подобное, пока она там?)")
    call process_character (n, appearance="blush false", text="(Может быть сложно...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Бабушка умна, она что-нибудь придумает!)")

    call static_still_ctc ("bg edna_blowjob _nocum")

    call process_character (edna, appearance="blush false", text="Ммф...")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Я действительно хочу, чтобы [si.say_name] осталась в этом новом доме)")
    call process_character (edna, appearance="blush false", text="(Даже если мне придется платить часть ипотеки)")
    call process_character (edna, appearance="blush false", text="(Без неё, [k.say_name] и [sa.say_name] нахождение рядом со мной будет печально для меня)")
    call process_character (edna, appearance="blush false", text="(Но если [n.say_name] не сможет остаться?)")
    call process_character (edna, appearance="blush false", text="(Я бы точно сошла с ума!)")
    call process_character (edna, appearance="blush false", text="(Я слишком зависима от него сейчас)")
    call process_character (edna, appearance="blush false", text="(И я уверена, что он чувствует то же самое ко мне)")
    call process_character (n, appearance="blush false", text="Оох...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я хотел бы съесть часть десертов после этого)")
    call process_character (n, appearance="blush false", text="(Я должен спросить, есть ли у бабушки ингредиенты, чтобы испечь торт!)")
    call process_character (n, appearance="blush false", text="(Может быть, мы можем сделать пончики с корицей!)")
    call process_character (n, appearance="blush false", text="(Хотя я не могу испортить аппетит)")
    call process_character (n, appearance="blush false", text="(Маме не понравится, если я не поужинаю...)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", xalign = 0.05, yalign = 0.05)
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg edna_blowjob _natetongue_cum")

    call process_character (n, appearance="blush false", text="Аагх!")
    call process_character (edna, appearance="blush false", text="{i}Ухх,{/i} {i}ухх.{/i}..")
    call process_character (edna, appearance="blush false", text="(В тот раз у меня во рту намного больше спермы!)")
    call process_character (edna, appearance="blush false", text="(Сперма накапливается на задней части моего языка...)")

    call edna_scene_blowjob_revisit_end

    return

label edna_scene_blowjob_revisit_end:

    python:
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_had_foreskin_played_with", 1)
        stats.add_stat("times_given_facial", 1)
        stats.add_stat("times_received_blowjob", 1)

    call process_end_of_scene ("edna_scene_blowjob_revisit", char=edna, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label edna_scene_vaginal_anal_phase_2(dream=False):
    menu:
        "Вагинальный секс":
            if not edna_finale_vaginal_chosen_this_time:
                $ edna_finale_positions_chosen += 1
            $ edna_finale_vaginal_chosen_this_time = True

            if not dream:
                $ stats.add_stat("times_had_vaginal_sex", 1)

            call static_still_ctc ("bg edna_vag_anal_vagfuck")

            call process_character (edna, appearance="blush false", text="Уф!")
            call process_character (edna, appearance="blush false", text="Ты прямо на мне, [n.say_name]!")
            call process_character (edna, appearance="blush false", text="Ух, ох...")
            call process_character (n, appearance="blush false", text="Я очень хотел трахнуть твою киску, бабушка! ")
            call process_character (n, appearance="blush false", text="Ха, ах!")
            call process_character (n, appearance="blush false", text="Но я знал, что тебе удобнее лежа.")
            call process_character (n, appearance="blush false", text="Так что я подумал, что могу трахнуть тебя вот так, и тебе не придется вставать!")
            call process_character (edna, appearance="blush false", text="Ммм!")
            call process_character (edna, appearance="blush false", text="Ох-ах!")
            call process_character (edna, appearance="blush false", text="Ладно, можешь продолжать меня так трахать.")
            call process_character (edna, appearance="blush false", text="Но постарайся не давить на меня, ах...{w=1.0}всем своим весом.")
            call process_character (edna, appearance="blush false", text="Я уже не молодая пташка, да и ты не легкий!")
            call process_character (n, appearance="blush false", text="Я буду держать себя в руках.")
            call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")

            if not edna_fucked_vaginally():
                call process_character (edna, appearance="blush false", text="Каково это, быть во мне в первый раз?")
            else:
                call process_character (edna, appearance="blush false", text="Каково это, быть внутри меня [n.say_name]?")

            call process_character (n, appearance="blush false", text="Оо боже!")
            call process_character (n, appearance="blush false", text="Это лучше всего, Бабушка!")
            call process_character (n, appearance="blush false", text="Так жарко и влажно!")
            call process_character (n, appearance="blush false", text="Но также уютно моему члену!")
            call process_character (edna, appearance="blush false", text="Моя киска хорошо сохранилась за эти годы.")
            call process_character (edna, appearance="blush false", text="И все это для тебя сейчас, и в будущем!")
            call process_character (n, appearance="blush false", text="Ах, ах...я буду трахать тебя столько, сколько смогу, Бабушка!")
            call process_character (n, appearance="blush false", text="Я точно знаю, что буду!")
            call process_character (edna, appearance="blush false", text="Это работает в обе стороны, [n.say_name].")
            call process_character (edna, appearance="blush false", text="Я хочу трахнуть тебя так сильно, как только смогу!")
        "Анальный секс":
            if not edna_finale_anal_chosen_this_time:
                $ edna_finale_positions_chosen += 1
            $ edna_finale_anal_chosen_this_time = True
            call static_still_ctc ("bg edna_vag_anal_anal_noblur")

            call process_character (edna, appearance="blush false", text="Аах, хочешь попробовать мою попку, [n.say_name]?")
            call process_character (n, appearance="blush false", text="Д-Да, Бабушка.")
            call process_character (edna, appearance="blush false", text="Сначала нужно делать это медленно.")
            call process_character (edna, appearance="blush false", text="Ха-ах!")
            call process_character (edna, appearance="blush false", text="Не пытайся ее таранить.")
            call process_character (edna, appearance="blush false", text="Помедленнее.")
            call process_character (n, appearance="blush false", text="Ммм...")
            call process_character (n, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="Х-Хорошо, мой член полностью вошел!")
            call process_character (edna, appearance="blush false", text="{cps=40}Хорошо, вы можешь начать, когда ты-{/cps}{w=0.75}{nw}")

            call static_still_ctc ("bg edna_vag_anal_anal_blur_ahego")

            call process_character (edna, appearance="blush false", text="Ах!")
            call process_character (n, appearance="blush false", text="Ого-го!")
            call process_character (n, appearance="blush false", text="Аау да, Бабушка!")
            call process_character (n, appearance="blush false", text="Она такая тугая!")
            call process_character (edna, appearance="blush false", text="Да, да, это так!")
            call process_character (edna, appearance="blush false", text="О боже...{w=1.0}черт!")
            call process_character (edna, appearance="blush false", text="...")
            call process_character (edna, appearance="blush false", text="(Я пытаюсь вспомнить последний раз, когда у меня был анальный секс!)")
            call process_character (edna, appearance="blush false", text="(Я не помню, чтобы моя задница была такой чувствительной!)")
            call process_character (edna, appearance="blush false", text="(Всякий раз, когда [n.say_name] толкает член, он толкает все мое тело!)")
            call process_character (edna, appearance="blush false", text="(О, какое чувство!)")
            call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
            call process_character (n, appearance="blush false", text="Тебе нравится, когда твою задницу трахают, Бабушка?")
            call process_character (edna, appearance="blush false", text="Гораздо больше, чем я думала [n.say_name]!")
            call process_character (edna, appearance="blush false", text="На самом деле, ты можешь двигаться немного быстрее, если хочешь.")
            call process_character (n, appearance="blush false", text="Нет проблем, Бабушка!")
            call process_character (edna, appearance="blush false", text="Ха-ах-аах!")
            call process_character (edna, appearance="blush false", text="Трахни меня в зад, [n.say_name]!")
            call process_character (edna, appearance="blush false", text="Забей хорошенько!")
        "Анилингус":
            if not edna_finale_analingus_chosen_this_time:
                $ edna_finale_positions_chosen += 1
            $ edna_finale_analingus_chosen_this_time = True

            if not dream:
                $ stats.add_stat("times_given_analingus", 1)
            call static_still_ctc ("bg edna_vag_anal_analingus")

            call process_character (edna, appearance="blush false", text="Ох, ох!")
            call process_character (n, appearance="blush false", text="Ммм...")
            call process_character (edna, appearance="blush false", text="Я не ожидала такого ощущения!")
            call process_character (edna, appearance="blush false", text="Аа-ха!")
            call process_character (n, appearance="blush false", text="Я все делаю правильно, Бабушка?")
            call process_character (edna, appearance="blush false", text="Для меня, конечно!")
            call process_character (edna, appearance="blush false", text="{i}Ах!{/i}")
            call process_character (edna, appearance="blush false", text="Засунь свой язык дальше, [n.say_name]!")
            call process_character (edna, appearance="blush false", text="Глубже!")
            call process_character (n, appearance="blush false", text="Вот так?")
            call process_character (edna, appearance="blush false", text="У тебя получилось, ах!")
            call process_character (edna, appearance="blush false", text="Угости мою киску тоже!")
            call process_character (edna, appearance="blush false", text="Да!")
            call process_character (n, appearance="blush false", text="(Анилингус намного веселее, чем я думал!)")
            call process_character (n, appearance="blush false", text="(Просто облизывая бабушкину задницу, она возбуждается от этого)")
            call process_character (n, appearance="blush false", text="(Должно быть, поэтому бабушка так весело сосет мой член!)")
            call process_character (n, appearance="blush false", text="(Интересно, смогу ли я заставить ее кончить, сделав это...)")
            call process_character (n, appearance="blush false", text="...")
            call process_character (n, appearance="blush false", text="(Мои пальцы стали мокрыми от ее киски)")
            call process_character (edna, appearance="blush false", text="Мм, ох да, [n.say_name].")
            call process_character (edna, appearance="blush false", text="Продолжай столько, сколько захочешь.")
            call process_character (edna, appearance="blush false", text="...")
            call process_character (edna, appearance="blush false", text="(Мои пальцы ног продолжают скручиваться от возбуждения, которое я чувствую)")
            call process_character (edna, appearance="blush false", text="(Мой первый опыт лизания задницы очень положительный!)")
            call process_character (edna, appearance="blush false", text="(И из всех людей, с которыми я была, оказалось, что мой внук тот, кто готов попробовать)")
            call process_character (edna, appearance="blush false", text="(Опять же, [n.say_name] кажется, готов сделать что угодно, когда дело доходит до секса!)")
            call process_character (edna, appearance="blush false", text="(Он само определение кобеля!)")
        "Кончить" if edna_finale_positions_chosen >= 2:
            call edna_scene_vaginal_anal_end (dream=dream)

    call edna_scene_vaginal_anal_phase_2 (dream=dream)

    return

label edna_scene_vaginal_anal_end(dream=False):

    call static_still_ctc ("bg edna_vag_anal_anal_blur_ahego")

    call process_character (edna, appearance="blush false", text="Ты думал о том, чтобы войти в мою задницу, [n.say_name]?")
    call process_character (edna, appearance="blush false", text="Похоже, ты действительно хочешь это сделать.")
    call process_character (n, appearance="blush false", text="О-Ох, да, я...")
    call process_character (n, appearance="blush false", text="Я думаю, это случится, Бабушка!")
    call process_character (edna, appearance="blush false", text="Я думаю, нет такого возраста у людей, когда не хочешь чтобы сперма выстрелила в твой зад!")
    call process_character (edna, appearance="blush false", text="Я рада, что мой внук получает привилегию сделать это!")
    call process_character (n, appearance="blush false", text="Ох...{w=1.0}Ооох!")
    call process_character (n, appearance="blush false", text="Я сейчас кончу, Бабушка!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg edna_vag_anal_anal_blur_ahego_cum")

    call process_character (edna, appearance="blush false", text="Ммм!")
    call process_character (edna, appearance="blush false", text="{i}Ах!{/i}")
    call process_character (edna, appearance="blush false", text="(Он засовывает свой член в то время как кончает!)")
    call process_character (edna, appearance="blush false", text="(Это заставляет меня кончать!)")
    call process_character (n, appearance="blush false", text="Ух, ухх!")
    call process_character (n, appearance="blush false", text="Да, Бабушка, да!")
    call process_character (edna, appearance="blush false", text="Ты ждал, чтобы выстрелить побольше спермы, не так ли?")

    call static_still_ctc ("bg edna_vag_anal_nocumass_nate")

    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Ух ты!")
    call process_character (edna, appearance="blush false", text="Это был счастливый конец массажа!")
    call process_character (n, appearance="blush false", text="Счастливый конец?")
    call process_character (edna, appearance="blush false", text="Ах да, ты еще не знаком с этой фразой.")
    call process_character (n, appearance="blush false", text="...")

    call static_still_ctc ("bg edna_vag_anal_nocumass")

    call process_character (n, appearance="blush false", text="Ох-ох!")
    call process_character (n, appearance="blush false", text="Ах!")

    call static_still_ctc ("bg edna_vag_anal_cumass")

    call process_character (edna, appearance="blush false", text="У тебя еще не кончилась сперма!")
    call process_character (edna, appearance="blush false", text="Теперь она не только в моей заднице, но и на ней!")
    call process_character (n, appearance="blush false", text="Когда я вынул, у меня было желание кончить снова.")
    call process_character (edna, appearance="blush false", text="Моя задница, скорее всего, сжала твою головку на выходе.")
    call process_character (edna, appearance="blush false", text="Это то, что, вероятно, вызвало твой вторичный оргазм.")
    call process_character (n, appearance="blush false", text="Что бы это ни было, Бабушка, мне это нравилось!")
    call process_character (edna, appearance="blush false", text="Ну, я бы сказала, что ты максимально использовал эту награду, [n.say_name]!")
    call process_character (edna, appearance="blush false", text="Это те награды, которые ты хотел бы видеть чаще?")
    call process_character (n, appearance="blush false", text="Да, Бабушка!")
    call process_character (edna, appearance="blush false", text="Тогда как насчет этого...")
    call process_character (edna, appearance="blush false", text="Всякий раз, когда ты массируешь меня, как сегодня, то также можешь и трахнуть меня!")
    call process_character (edna, appearance="blush false", text="Я редко отказываюсь от массажа, так что у тебя много возможностей.")
    call process_character (n, appearance="blush false", text="Даааа!")
    call process_character (n, appearance="blush false", text="Когда в следующий раз я смогу прийти к тебе на массаж, Бабушка?")
    call process_character (edna, appearance="blush false", text="Ха-ха, когда захочешь [n.say_name], когда захочешь!")

    python:
        edna.revistable_scenes.add("edna_scene_vaginal_anal_revisit")

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

    call process_end_of_scene ("edna_scene_vaginal_anal", char=edna, dream=dream)
    return

label edna_scene_vaginal_anal(dream=False):
    call edna_scene_vaginal_anal_sex (dream=dream)
    return

label edna_scene_vaginal_anal_sex(dream=False):
    call process_scene_beginning (bg="bg edna_house_daytime", char_tuple_array=[ (n, "outfit clothesjacket pose handpocket face neutral blush false"), (edna, "outfit clothes pose handhip face neutral blush false mouth red") ], dream=dream )

    $ edna_finale_positions_chosen = 0
    $ edna_finale_vaginal_chosen_this_time = False
    $ edna_finale_anal_chosen_this_time = False
    $ edna_finale_analingus_chosen_this_time = False

    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false mouth red", text="Рада, что ты зашел, [n.say_name].")
    call process_character (edna, appearance="outfit clothes pose handhip face neutral blush false mouth red", text="Ай, ай...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face concerned blush false", text="Что-то случилось, Бабушка?")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false mouth red", text="У меня сегодня немного болят суставы.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false mouth red", text="Я была занята выполнением различных поручений.")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false mouth red", text="Иногда мое тело говорит мне, что я сделала слишком многое за один день.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false mouth red", text="Ничего необычного для человека моего возраста!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Я могу чем-нибудь помочь, Бабушка?")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="Как заботливо с твоей стороны, [n.say_name]!")
    call process_character (edna, appearance="outfit clothes pose fisthip face happy blush false mouth red", text="Знаешь...")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Мне бы не повредил массаж.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Ты хочешь этого, Бабушка?")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Да, это было бы здорово.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Особенно массаж поясницы.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Хммм...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Я никогда раньше не делал массаж.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Я имею в виду...{w=1.0}я тер твои сиськи, но не знаю, считается ли это.")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false mouth red", text="Это не совсем то же самое, но я не думаю, что тебе будет трудно научиться!")
    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false mouth red", text="Я могу помочь научить тебя основам.")

    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false")


    call process_character (edna, appearance="outfit clothes pose fisthip face neutral blush false mouth red", text="В молодости я постоянно делала массаж.")
    call process_character (edna, appearance="outfit clothes pose handhip face happy blush false mouth red", text="Так что я знаю, как сделать его хорошо!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Хорошо, Бабушка, покажи мне, что я должен сделать!")
    call process_character (edna, appearance="outfit clothes pose handclasp face neutral blush false mouth red", text="Во-первых, рекомендуется, чтобы массируемая область была полностью открыта.")
    call process_character (edna, appearance="outfit clothes pose handclasp face happy blush false mouth red", text="Чтобы было проще, почему бы мне просто не снять все?")

    call character_leave_dissolve (edna)
    pause 0.5

    call process_character (edna, appearance="outfit nude")
    pause 0.5


    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red")

    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Большинство людей получают массаж голыми?")
    call process_character (edna, appearance="outfit nude pose handhip face neutral blush false mouth red", text="Не всегда, это зависит от ситуации.")
    call process_character (edna, appearance="outfit nude pose handhip face neutral blush false mouth red", text="Если массаж требует, что получатель будет обнажен, то обычно их интимные области укрыты.")
    call process_character (edna, appearance="outfit nude pose handhip face flirt blush false mouth red", text="Но для нас в этом нет необходимости...")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Звучит хорошо для меня, Бабушка!")
    call process_character (edna, appearance="outfit nude pose fisthip face happy blush false mouth red", text="Хаха!")
    call process_character (edna, appearance="outfit nude pose fisthip face happy blush false mouth red", text="Я знала, что ты скажешь нечто подобное!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="А что насчет меня, я должен что-нибудь надеть?")
    call process_character (edna, appearance="outfit nude pose handclasp face neutral blush false mouth red", text="Полностью зависит от тебя.")
    call process_character (edna, appearance="outfit nude pose handclasp face flirt blush false mouth red", text="Лично мне нравится видеть тебя с меньшим...")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face neutral blush false", text="Я более чем доволен этим, Бабушка!")

    call character_leave_dissolve (n)
    pause 0.5


    call process_character (edna, appearance="outfit nude pose handclasp face neutral blush false mouth red")


    call process_character (edna, appearance="outfit nude pose handclasp face neutral blush false mouth red")

    call process_character (n, appearance="outfit underwear pose handsdown face neutral blush false", text="И что теперь?")
    call process_character (edna, appearance="outfit nude pose handhip face neutral blush false mouth red", text="Затем мне нужно будет устроиться поудобнее, так как я буду лежать на животе.")
    call process_character (edna, appearance="outfit nude pose handhip face neutral blush false mouth red", text="Подушки и большого полотенца должно хватить.")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="Я могу пойти и взять их!")
    call process_character (edna, appearance="outfit nude pose handclasp face neutral blush false mouth red", text="Возьми пляжное полотенце из сушилки.")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Оно мягкое и пушистое!")

    call fade_to_black (1)

    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="...")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Ах, как хорошо, просто прилечь.")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="И станет еще лучше, как только ты начнешь массировать, [n.say_name]!")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="Надеюсь, я смогу сделать это правильно, Бабушка.")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Не волнуйся.")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Это не так сложно, как ты думаешь.")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="...")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Ох, я только что вспомнила кое-что.")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="Что?")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="В ванной есть немного масла для тела.")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Я купила его некоторое время назад, но у меня не было возможности использовать его.")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Это отлично подходит для массажа и имеет приятный аромат.")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Почему бы тебе не взять его?")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Думаю, тебе понравится.")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="Где именно?")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Он в шкафу под раковиной в ванной.")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Он справа.")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="Хорошо, сейчас вернусь!")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="...")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="(Интересно, станет ли это больше, чем просто массаж, как планировалось)")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="(Основываясь на нашем послужном списке, я сомневаюсь!)")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="...")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="(Кто из нас будет искушен первым?)")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="(Будет интересно посмотреть, как долго [n.say_name] сможет проявлять сдержанность)")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="(Тем более, что у него будет полный обзор моей задницы и киски...)")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="...")
    call process_character (n, appearance="outfit underwear pose handfist face happy blush false", text="У меня есть все необходимое!")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Отлично, [n.say_name]!")
    call process_character (edna, appearance="outfit nude pose handclasp face happy blush false mouth red", text="Неси его сюда.")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Suave Standpipe.ogg", fadein = 1.0)

    call static_still_ctc ("bg edna_vag_anal_laying")

    call process_character (edna, appearance="blush false", text="Налей немного масла на руки и втирай мне в поясницу.")
    call process_character (edna, appearance="blush false", text="Затем нажми на область ладонями руки.")
    call process_character (n, appearance="blush false", text="Понял.")
    call process_character (edna, appearance="blush false", text="Используй свой вес в своих интересах.")
    call process_character (edna, appearance="blush false", text="Не вкладывай всю силу, это быстро утомит тебя.")
    call process_character (edna, appearance="blush false", text="Массажист должен так же расслабляться, как и массажируемый!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Угу...")
    call process_character (edna, appearance="blush false", text="Тебе нужно, чтобы я объяснила это снова, [n.say_name]?")
    call process_character (n, appearance="blush false", text="...{p}…")
    call process_character (n, appearance="blush false", text="(Бабушкин зад огромен!)")

    if "kira_scene_anal" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Я думаю, что он может быть больше, чем у [k.say_name]...)")
        call process_character (n, appearance="blush false", text="(Я не думал, что какая-то задница может быть больше!)")
        call process_character (n, appearance="blush false", text="(Я хотел бы иметь возможность почувствовать его!)")
        call process_character (n, appearance="blush false", text="(Может быть, бабушка хочет и массаж попки?)")
    elif "simone_scene_anal" in scenes_completed:
        call process_character (n, appearance="blush false", text="(Она очень похожа на мамину задницу)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Возможно, однажды я смогу сравнить их бок о бок)")
        call process_character (n, appearance="blush false", text="(Это было бы потрясающе!)")
    else:
        call process_character (n, appearance="blush false", text="(Она выглядит такой гладкой...)")
        call process_character (n, appearance="blush false", text="(Я хотел бы иметь возможность почувствовать его!)")
        call process_character (n, appearance="blush false", text="(Может быть, бабушка хочет и массаж попки?)")

    call process_character (edna, appearance="blush false", text="(Ну...{w=1.0}это было быстро)")
    call process_character (edna, appearance="blush false", text="([n.say_name] смотрит на мою задницу, как магнит на металл)")
    call process_character (edna, appearance="blush false", text="(Он еще даже не открыл бутылку.)")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Теперь ты готов, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Ох, ух...")
    call process_character (n, appearance="blush false", text="Да, Бабушка.")
    call process_character (edna, appearance="blush false", text="Я надеюсь, что ты дашь отличный массаж, [n.say_name].")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Я вознагражу тебя, если ты это сделаешь.")
    call process_character (n, appearance="blush false", text="Оох, бабушкина награда?")
    call process_character (edna, appearance="blush false", text="Вот в чем дело.")
    call process_character (edna, appearance="blush false", text="Если ты сможешь помочь моей спине почувствовать себя лучше и облегчить боль...")
    call process_character (edna, appearance="blush false", text="Ты можешь делать со мной все, что захочешь.")
    call process_character (edna, appearance="blush false", text="И я имею в виду, что угодно.")
    call process_character (n, appearance="blush false", text="Д-да?")
    call process_character (edna, appearance="blush false", text="Уверена, ты уже знаешь, что хочешь со мной сделать...")
    call process_character (edna, appearance="blush false", text="Все, что от тебя требуется, это сделать мне первоклассный массаж.")
    call process_character (n, appearance="blush false", text="Я сделаю тебе самый лучший массаж, Бабушка!")
    call process_character (n, appearance="blush false", text="Ты будешь чувствовать себя удивительно после этого!")
    call process_character (edna, appearance="blush false", text="Мне нравится, как это звучит!")
    call process_character (edna, appearance="blush false", text="Я не могу ждать, [n.say_name]!")

    call fade_to_black (1)

    call process_character (n, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Ммм...")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Сосредоточься на этом месте больше.")
    call process_character (n, appearance="blush false", text="На нем!")
    call process_character (edna, appearance="blush false", text="Аах, это замечательно.")
    call process_character (edna, appearance="blush false", text="Работай в этой области немного усерднее.")
    call process_character (edna, appearance="blush false", text="Ты можешь использовать локоть.")
    call process_character (n, appearance="blush false", text="Понял тебя.")
    call process_character (edna, appearance="blush false", text="Ох, это похоже на рай!")
    call process_character (edna, appearance="blush false", text="Мне становится намного лучше!")
    call process_character (n, appearance="blush false", text="Хочешь, чтобы я сделал это со всей твоей спиной, Бабушка?")
    call process_character (edna, appearance="blush false", text="Ох, ты сможешь?!")
    call process_character (edna, appearance="blush false", text="Я бы никогда не отказалась от такого предложения!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Должен убедиться, что этот массаж идеален!)")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="(Удивительно, как маленький стимул может иметь большое значение)")
    call process_character (edna, appearance="blush false", text="(Даже если [n.say_name] просто сделал хорошую работу, я бы все равно дала ему награду)")
    call process_character (edna, appearance="blush false", text="(Но он вкладывает душу и сердце в этот массаж)")
    call process_character (edna, appearance="blush false", text="(Я на самом деле предпочту [n.say_name], чем пойти в какой-нибудь профессиональный спа-центр)")
    call process_character (edna, appearance="blush false", text="(Это дешевле, и есть хороший шанс на счастливый конец...)")
    call process_character (edna, appearance="blush false", text="...")




    call static_still_ctc ("bg edna_vag_anal_laying_nonate")

    call process_character (n, appearance="blush false", text="Как я, Бабушка?")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Я чувствую себя такой расслабленной...")
    call process_character (edna, appearance="blush false", text="Я могу заснуть прямо здесь!")
    call process_character (n, appearance="blush false", text="Твоя спина чувствует себя лучше?")
    call process_character (edna, appearance="blush false", text="Да!")
    call process_character (edna, appearance="blush false", text="Спасибо, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Пожалуйста, Бабушка.")
    call process_character (edna, appearance="blush false", text="Я и не представляла, сколько у меня узлов!")
    call process_character (edna, appearance="blush false", text="Неудивительно, почему я чувствовала себя такой одеревеневшей.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Значит ли это, что я могу...")
    call process_character (edna, appearance="blush false", text="Конечно!")
    call process_character (edna, appearance="blush false", text="Твоя награда вполне заслуженна, [n.say_name].")
    call process_character (edna, appearance="blush false", text="Надеюсь, ты получишь от этого максимум.")
    call process_character (edna, appearance="blush false", text="(Я очень на это надеюсь...)")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (edna, appearance="blush false", text="Задумывался ли ты о том, что хотел бы сделать в первую очередь?")
    call process_character (n, appearance="blush false", text="Я не знаю, это трудное решение!")
    call process_character (edna, appearance="blush false", text="Почему бы тебе не подумать об этом немного?")
    call process_character (edna, appearance="blush false", text="Таким образом, ты можешь сузить свой выбор!")
    call process_character (n, appearance="blush false", text="Хм, я попробую это сделать.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Что бы я хотел сделать больше всего?)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Было бы здорово сделать то, что я никогда не пробовал с бабушкой раньше!)")

    if "finale_scene" in store.scenes_completed:
        call process_character (n, appearance="blush false", text="(Хотя, это было фантастически, трахнуть ее киску на вечеринке у бассейна)")
        call process_character (n, appearance="blush false", text="(Я не хотел, чтобы бабушка перестала подпрыгивать на моем члене!)")
        call process_character (n, appearance="blush false", text="(Просто думая об этом, мой член становится супер твердым!)")
        call process_character (n, appearance="blush false", text="(Трахать ее киску - это лучший выбор!)")
    else:
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Я еще не трахал бабушкину киску...)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Просто думая об этом, мой член становится твердым!)")
        call process_character (n, appearance="blush false", text="(Это определенно лучший выбор!)")

    call process_character (n, appearance="blush false", text="...")

    if stats.stat_value("times_given_anal_sex") > 0:
        call process_character (n, appearance="blush false", text="(Может, я попробую засунуть свой член ей в задницу?)")
        call process_character (n, appearance="blush false", text="(Я знаю, что буду чувствовать себя так хорошо!)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Хотя понравится ли это Бабушке?)")
        call process_character (n, appearance="blush false", text="(Я не знаю, делала ли она это раньше...)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Но это действительно заманчиво попробовать и посмотреть, что получится!)")
        call process_character (n, appearance="blush false", text="(В конце концов, бабушка сказала, что я могу сделать с ней все, что угодно...)")
    else:
        call process_character (n, appearance="blush false", text="(Может, я попробую засунуть свой член ей в задницу?)")
        call process_character (n, appearance="blush false", text="(Кажется, у меня получилось бы, если бы я протолкнул его...)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Хотя понравится ли это Бабушке?)")
        call process_character (n, appearance="blush false", text="(Я не знаю, можно ли засунуть туда свой член или нет...)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Но это действительно заманчиво попробовать, и посмотреть, что произойдет!)")
        call process_character (n, appearance="blush false", text="(В конце концов, бабушка сказала, что я могу сделать с ней все, что угодно...)")

    call process_character (n, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Ты все еще не можешь решить, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Я...{w=1.0}почти.")
    call process_character (edna, appearance="blush false", text="Не возражаешь, если я внесу предложение?")
    call process_character (edna, appearance="blush false", text="Возможно, ты не подумал об этом.")
    call process_character (n, appearance="blush false", text="Конечно, Бабушка!")
    call process_character (edna, appearance="blush false", text="Ты когда-нибудь слышал о анилингусе?")
    call process_character (n, appearance="blush false", text="Анилингус?")

    if stats.stat_value("times_given_anal_sex") > 0:
        call process_character (n, appearance="blush false", text="Похоже, это связано с твоей задницей, но я не уверен.")
        call process_character (edna, appearance="blush false", text="Ты совершенно прав!")
        call process_character (edna, appearance="blush false", text="Анилингус является формой орального секса, [n.say_name].")
    else:
        call process_character (n, appearance="blush false", text="Понятия не имею, что означает это слово.")
        call process_character (edna, appearance="blush false", text="Анилингус является формой орального секса, [n.say_name].")

    call process_character (n, appearance="blush false", text="Орального?")
    call process_character (n, appearance="blush false", text="Ты имеешь в виду, это связано с твоим ртом?")
    call process_character (edna, appearance="blush false", text="Когда я сосу твой член, это считается оральным сексом.")
    call process_character (edna, appearance="blush false", text="Я использую свой язык и рот, чтобы доставить удовольствие твоему члену.")
    call process_character (edna, appearance="blush false", text="Анилингус, это когда ты ублажаешь мой анус языком.")
    call process_character (n, appearance="blush false", text="Да?")
    call process_character (n, appearance="blush false", text="Я могу сделать это с тобой, Бабушка?")
    call process_character (edna, appearance="blush false", text="Если тебе это нравится, то да!")
    call process_character (edna, appearance="blush false", text="Лично мне никогда раньше никто не лизал задницу.")
    call process_character (edna, appearance="blush false", text="Меня всегда интересовало это.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Это интересный вариант, представленный Бабушкой)")
    call process_character (n, appearance="blush false", text="(Итак, у меня есть три надежных варианта, которые я могу сделать)")
    call process_character (n, appearance="blush false", text="(Я мог бы трахнуть ее киску, ее задницу или попробовать анилингус!)")
    call process_character (n, appearance="blush false", text="(Но с какой из них выбрать в первую очередь?)")
    call process_character (n, appearance="blush false", text="(Хмм...)")

    call edna_scene_vaginal_anal_phase_2 (dream=dream)

    return

label edna_scene_vaginal_anal_revisit:
    $ no_bust_art = False

    if "edna_scene_vaginal_anal_revisit" in scenes_completed:
        call edna_scene_vaginal_anal_revisit_2nd_time
    else:
        call edna_scene_vaginal_anal_revisit_1st_time

    return

label edna_scene_vaginal_anal_revisit_1st_time:

    call process_character (n, appearance="pose twohandfist face happy blush false")

    call process_character (edna, appearance="pose handhip face happy blush false mouth red", text="Хочешь получить еще одну награду?")
    call process_character (edna, appearance="pose handhip face happy blush false mouth red", text="Я положу полотенце на пол!")

    python hide:
        play_music("audio/music/Suave Standpipe.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg edna_vag_anal_laying_nonate")

    call process_character (edna, appearance="blush false", text="Ты когда-нибудь делал массаж своей маме или сестрам, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Нет.")
    call process_character (edna, appearance="blush false", text="Ты должен попробовать!")
    call process_character (edna, appearance="blush false", text="У тебя хорошо получается!")
    call process_character (n, appearance="blush false", text="Спасибо!")
    call process_character (edna, appearance="blush false", text="Некоторые здравые советы для тебя, [n.say_name]...")
    call process_character (edna, appearance="blush false", text="Быстрый путь к сердцу женщины может быть достигнут с помощью массажа.")
    call process_character (n, appearance="blush false", text="Да?")
    call process_character (edna, appearance="blush false", text="Представь себе, если бы твоя мама только что пришла после напряженного утра, работая в саду.")
    call process_character (edna, appearance="blush false", text="Затем ты предлагаешь ей массаж плеч или ног.")
    call process_character (edna, appearance="blush false", text="Она будет в восторге!")
    call process_character (n, appearance="blush false", text="Хмм...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ты думаешь, если я сделаю маме массаж, это может привести к.....")
    call process_character (edna, appearance="blush false", text="Награде вроде моей?")
    call process_character (edna, appearance="blush false", text="Кто знает.")
    call process_character (edna, appearance="blush false", text="Твоя мама очень щедрый человек.")
    call process_character (edna, appearance="blush false", text="Я уверена, она покажет ее...{w=1.0}благодарность тебе.")
    call process_character (n, appearance="blush false", text="Интересно, а [k.say_name] тоже хочет массаж...")
    call process_character (edna, appearance="blush false", text="Я бы не стала задаваться вопросом, я бы просто попробовала и посмотрела, что произойдет!")
    call process_character (edna, appearance="blush false", text="Ты удивишься.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="Кстати, о сюрпризах...")
    call process_character (edna, appearance="blush false", text="Как ты собираешься начать со мной, [n.say_name]?")
    call process_character (edna, appearance="blush false", text="Ты хочешь снова войти в мою киску?")
    call process_character (edna, appearance="blush false", text="Может, ты хочешь сделать мне лизание языком?")
    call process_character (edna, appearance="blush false", text="Или, может быть, ты предпочтешь свой член в моей заднице!")

    jump edna_scene_vaginal_anal_revisit_1st_time_phase_2

    return

label edna_scene_vaginal_anal_revisit_1st_time_phase_2:
    menu:
        "Вагинальный секс":
            $ stats.add_stat("times_had_vaginal_sex", 1)
            call static_still_ctc ("bg edna_vag_anal_vagfuck")

            call process_character (edna, appearance="blush false", text="Я думаю, ты получаешь удовольствие, оседлав меня вот так.")
            call process_character (n, appearance="blush false", text="Я-я вроде как, да...")
            call process_character (n, appearance="blush false", text="Так мой член входит в твою киску.")
            call process_character (edna, appearance="blush false", text="Ах, я должна была догадаться.")
            call process_character (edna, appearance="blush false", text="Ты хочешь только самые возбуждающие позы для твоего члена.")
            call process_character (edna, appearance="blush false", text="Аа-аах...")
            call process_character (edna, appearance="blush false", text="...")
            call process_character (edna, appearance="blush false", text="Но я бы солгала, если бы сказала, что я не такая.")
            call process_character (n, appearance="blush false", text="Так это все еще нормально для меня быть на тебе, Бабушка?")
            call process_character (edna, appearance="blush false", text="О, я просто дразню тебя, [n.say_name].")
            call process_character (edna, appearance="blush false", text="У меня нет проблем с тем, что ты сверху.")
            call process_character (edna, appearance="blush false", text="Это полотенце обеспечивает достаточную прокладку.")
        "Анальный секс":
            call static_still_ctc ("bg edna_vag_anal_anal_noblur")

            call process_character (edna, appearance="blush false", text="Хорошо [n.say_name], я знаю, что ты любишь двигаться быстро во время этого.")
            call process_character (edna, appearance="blush false", text="Прокати меня!")

            call static_still_ctc ("bg edna_vag_anal_anal_blur_ahego")

            call process_character (edna, appearance="blush false", text="Хаа-ах!")
            call process_character (edna, appearance="blush false", text="...")
            call process_character (edna, appearance="blush false", text="(Я, должно быть, самый дикий пожилой человек в этом кондоминиуме!)")
            call process_character (edna, appearance="blush false", text="(Никто не посмеет попробовать анальный секс в этом возрасте!)")
            call process_character (edna, appearance="blush false", text="(Никто...{w=1.0}кроме меня!)")
            call process_character (edna, appearance="blush false", text="(Последнее, что я хочу, чтобы мой возраст был помехой)")
            call process_character (edna, appearance="blush false", text="(С помощью [n.say_name], я позабочусь о том, чтобы этого никогда не произошло!)")
        "Анилингус":
            $ stats.add_stat("times_given_analingus", 1)
            call static_still_ctc ("bg edna_vag_anal_analingus")

            call process_character (edna, appearance="blush false", text="Ммм, ах...")
            call process_character (edna, appearance="blush false", text="Мне нравится твоя техника, [n.say_name].")
            call process_character (edna, appearance="blush false", text="Ты переключаешься между лизанием и вонзанием языка!")
            call process_character (n, appearance="blush false", text="Твой язык часто так делает, когда ты сосешь, Бабушка.")
            call process_character (n, appearance="blush false", text="Я решил, что должен попытаться сделать то же самое.")
            call process_character (edna, appearance="blush false", text="Ты адаптировал то, что видел, очень мило.")
            call process_character (edna, appearance="blush false", text="Такие вещи лучше всего изучать на опыте.")
            call process_character (edna, appearance="blush false", text="Трудно научить, как правильно делать минет или вылизать задницу.")
            call process_character (edna, appearance="blush false", text="На мой взгляд, твой лучший учитель - это ты сам.")
        "Кончить":

            jump edna_scene_vaginal_anal_revisit_1st_time_phase_3

    jump edna_scene_vaginal_anal_revisit_1st_time_phase_2

    return

label edna_scene_vaginal_anal_revisit_1st_time_phase_3:
    call static_still_ctc ("bg edna_vag_anal_anal_blur_ahego")

    call process_character (edna, appearance="blush false", text="Ты снова взорвешься в моей заднице, [n.say_name]?")
    call process_character (edna, appearance="blush false", text="Продолжай, пока не сделаешь этого!")
    call process_character (n, appearance="blush false", text="Д-Да!")
    call process_character (n, appearance="blush false", text="Да, Бабушка!")
    call process_character (edna, appearance="blush false", text="Охх, хаа!")
    call process_character (edna, appearance="blush false", text="Ммм, так хорошо...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Вот оно, Бабушка!")
    call process_character (n, appearance="blush false", text="Я не могу сдерживаться!")
    call process_character (edna, appearance="blush false", text="Тогда не надо, [n.say_name], выплесни все!")
    call process_character (n, appearance="blush false", text="Хннг!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg edna_vag_anal_anal_blur_ahego_cum")

    call process_character (edna, appearance="blush false", text="Вот, так.")
    call process_character (edna, appearance="blush false", text="Пусть твои яйца почувствуют облегчение.")
    call process_character (n, appearance="blush false", text="Мм-Мм-Мм!")

    call static_still_ctc ("bg edna_vag_anal_cumass_nate")

    call process_character (n, appearance="blush false", text="{i}Уфф.{/i}..")
    call process_character (n, appearance="blush false", text="...")
    call process_character (edna, appearance="blush false", text="У меня все хорошо, как у бабушки, [n.say_name]!")
    call process_character (edna, appearance="blush false", text="Я не отстаю от тебя и твоего сексуального влечения!")


    jump edna_scene_vaginal_anal_revisit_end

    return

label edna_scene_vaginal_anal_revisit_2nd_time_phase_2:
    menu:
        "Вагинальный секс":
            $ stats.add_stat("times_had_vaginal_sex", 1)

            if random.randint(0,1) == 0:
                call static_still_ctc ("bg edna_vag_anal_vagfuck")

                call process_character (edna, appearance="blush false", text="(Интересно, видел ли кто-нибудь [n.say_name] и меня раньше, но они не сообщают о нас, потому что им нравится смотреть)")
                call process_character (edna, appearance="blush false", text="(Это было бы так забавно!)")
            else:
                call static_still_ctc ("bg edna_vag_anal_vagfuck")

                call process_character (edna, appearance="blush false", text="Однажды я хотела бы сменить эту позу.")
                call process_character (edna, appearance="blush false", text="Я очень люблю быть сверху, [n.say_name].")
        "Анальный секс":

            if random.randint(0,1) == 0:
                call static_still_ctc ("bg edna_vag_anal_anal_blur")

                call process_character (edna, appearance="blush false", text="Если бы я была на несколько десятилетий моложе, [n.say_name], ты не поверишь, что мы могли бы сделать вместе.")
                call process_character (edna, appearance="blush false", text="Мы могли бы продолжать в течение нескольких часов!")
            else:
                call static_still_ctc ("bg edna_vag_anal_anal_blur")

                call process_character (edna, appearance="blush false", text="Ты думаешь, мы сможем заниматься сексом целый день, [n.say_name]?")
                call process_character (edna, appearance="blush false", text="У меня было желание попробовать!")
        "Анилингус":
            $ stats.add_stat("times_given_analingus", 1)

            if random.randint(0,1) == 0:
                call static_still_ctc ("bg edna_vag_anal_analingus")

                call process_character (edna, appearance="blush false", text="Держу пари, ты великолепно лижешь киску, [n.say_name].")
                call process_character (edna, appearance="blush false", text="Может, однажды ты попробуешь...")
            else:
                call static_still_ctc ("bg edna_vag_anal_analingus")

                call process_character (edna, appearance="blush false", text="Здесь длинный язык имеет большие преимущества!")
        "Кончить":

            jump edna_scene_vaginal_anal_revisit_2nd_time_phase_3

    jump edna_scene_vaginal_anal_revisit_2nd_time_phase_2

    return

label edna_scene_vaginal_anal_revisit_2nd_time_phase_3:
    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg edna_vag_anal_anal_blur_cum")

    call process_character (n, appearance="blush false", text="Гааах, черт!")

    call static_still_ctc ("bg edna_vag_anal_anal_aftercum")

    call process_character (edna, appearance="blush false", text="Мммм...")
    call process_character (edna, appearance="blush false", text="Есть не так много вещей, что лучше, чем это.")
    call process_character (n, appearance="blush false", text="Я хочу кончить тебе в задницу, Бабушка!")

    call static_still_ctc ("bg edna_vag_anal_nocumass")

    call process_character (n, appearance="blush false", text="Аахх!")
    call process_character (n, appearance="blush false", text="Я кончаю на обе твои ягодицы, Бабушка!")
    call process_character (n, appearance="blush false", text="Ммм, да!")

    call static_still_ctc ("bg edna_vag_anal_cumass")

    call process_character (edna, appearance="blush false", text="Ты получаешь слишком много удовольствия, забрызгивая мою задницу спермой!")

    jump edna_scene_vaginal_anal_revisit_end

    return

label edna_scene_vaginal_anal_revisit_2nd_time:
    python hide:
        play_music("audio/music/Suave Standpipe.ogg", fadeout=1.0, fadein = 1.0)
    call static_still_ctc ("bg edna_vag_anal_laying_nonate")

    jump edna_scene_vaginal_anal_revisit_2nd_time_phase_2

    return

label edna_scene_vaginal_anal_revisit_end:

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

    call process_end_of_scene ("edna_scene_vaginal_anal_revisit", char=edna, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return