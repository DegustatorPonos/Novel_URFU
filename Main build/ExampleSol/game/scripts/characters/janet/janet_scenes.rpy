init python:
    def janet_anal_set_speed(label, is_revisit, dream = False):
        renpy.call(label, is_revisit, dream = dream)
        
        return

image janet_anal_anim:
    "janet_anal_anim_0"
    pause 0.11
    "janet_anal_anim_1"
    pause 0.11
    "janet_anal_anim_2"
    pause 0.11
    "janet_anal_anim_3"
    pause 0.11
    "janet_anal_anim_4"
    pause 0.11
    "janet_anal_anim_5"
    pause 0.09
    "janet_anal_anim_6"
    pause 0.09
    "janet_anal_anim_7"
    pause 0.04
    repeat

label janet_bust_art_test:
    $ nate_room.decide_and_play_daily_music_queue()
    $ quick_menu = False
    window hide
    call process_scene_beginning (bg=nate_room, char_tuple_array=[ (n, "outfit underwear face aroused blush true"), (janet, "face neutral position janet_special") ])
    $ quick_menu = False
    window hide
    pause

    call process_character (janet, text=";)")
    return

label janet_intro:
    $ nate_room.decide_and_play_daily_music_queue()
    call process_scene_beginning (bg=nate_room, char_tuple_array=[ (n, ""), (si, "outfit clothes pose handsup face happy blush false") ])

    call process_character (si, appearance="outfit clothes pose handsup face happy blush false", text="Сегодня так хорошо!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Да!")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Тебе нужно выйти на улицу.")
    call process_character (n, appearance="pose handpocket face neutral blush false")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Лето не будет длиться вечно!")
    call process_character (si, appearance="outfit clothes pose handsfront face neutral blush false", text="Надо брать из каждого дня максимум.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Это правда.")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Ты должен попросить свою сестру тоже выйти.")
    call process_character (si, appearance="outfit clothes pose handsup face neutral blush false", text="Ей нужно отдохнуть от всех этих видеоигр.")

    "{i}Тук-тук-тук{/i}"

    call process_character (si, appearance="outfit clothes pose armunder face curious blush false", text="(Кто это?)")
    "{color=[janet.color]}Женский голос{/color}" "Привет, привет!"

    $ clear_characters()
    python hide:
        for char in character_list():
            char.position = "right"

    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", replace=True)
    "{color=[janet.color]}Woman{/color}" "Эй!"
    "{color=[janet.color]}Woman{/color}" "Как дела?"

    call change_character_name (janet, prompt="Имя Тёти")
    call process_character (si, appearance="pose handsup face shocked blush false", text="[janet.say_name]?!", replace=True)
    call process_character (si, appearance="pose handsup face shocked blush false", text="Я не знала, что ты придёшь!")
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Сейчас легче лёгкого прийтик вам, теперь, когда вы так близко!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Я подумала, почему бы не поздороваться со всеми!")
    call process_character (janet, appearance="outfit clothes pose handface face happy blush false", text="{i}Вздох...{/i}", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face happy blush false", text="Это ты, [n.say_name]?", replace=True)
    call process_character (n, appearance="pose handfist face happy blush false", text="Привет тётя, [janet.say_name]!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Ты выглядишь выше, чем раньше!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Но ты все равно такой тощий!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Кости да кожа!", replace=True)
    call process_character (n, appearance="pose handpocket face curious blush false", text="...", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Но это лучше, чем лишний вес!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Легко накопить, но трудно потерять!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face happy blush false", text="Для нашей семьи это особенно актуально!", replace=True)
    call process_character (si, appearance="pose handsfront face concerned blush false", text="...", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Итак, где твои сёстры, [n.say_name]?", replace=True)
    call process_character (n, appearance="pose behindhead face neutral blush false", text="[sa.say_name] наверху.", replace=True)
    call process_character (n, appearance="pose behindhead face neutral blush false", text="А [k.say_name] вышла на пробежку.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Ах да, твоя старшая сестра остается приверженной своим упражнениям!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Я втянула ее во всю эту тренировочную рутину.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Она родилась, чтобы быть спортсменом!", replace=True)
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="...", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="А вот и она!", replace=True)
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="Не может быть!", replace=True)
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="Тётя [janet.say_name]!", replace=True)
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="Когда ты сюда приехала?", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Чуть раньше тебя.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Какая красотка!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face happy blush false", text="Только посмотри на себя!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face happy blush false", text="Какая мускулистая!", replace=True)
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Я добавила тяжелую атлетику в свой полк.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Ты выглядишь так, будто можешь поднять [n.say_name] одной рукой!", replace=True)
    call process_character (n, appearance="pose behindhead face curious blush false", text="...", replace=True)
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="Хаха!", replace=True)
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="Я уверена, что я смогу!", replace=True)
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Вообще-то, он работал со мной.", replace=True)
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Ходим на беговую дорожку и бегаем друг за другом.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Тебе нужно попотеть, чтобы догнать свою сестру, [n.say_name]!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="{i}Зевает...{/i}", replace=True)
    call process_character (si, appearance="pose handsup face neutral blush false", text="Доброе утро солнышко!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face curious blush false", text="Утро?", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face curious blush false", text="Уже почти одиннадцать тридцать!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="Тётя [janet.say_name]!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Эй, малышка!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Надеюсь, ты не слишком поздно ложишься!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="Хе-хе, я теряю счет времени, когда играю онлайн ночью.", replace=True)
    call process_character (si, appearance="pose armunder face neutral blush false", text="Не испорти режим сна, хорошо?", replace=True)
    call process_character (si, appearance="pose armunder face neutral blush false", text="Ты будешь смертельно уставшей, когда школа начнётся!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Ваша мама права.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="У [julia.say_name] такая же проблема.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Она не спит допоздна, а потом мне приходится вытаскивать ее утром из постели.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Где она кстати?", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face neutral blush false", text="Она только что приняла душ.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Да, она будет там вечно.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Я просто хотела узнать, как у нее дела.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face curious blush false", text="Она вела себя хорошо?", replace=True)
    call process_character (si, appearance="pose handsup face happy blush false", text="О [julia.say_name] была превосходна!", replace=True)
    call process_character (si, appearance="pose handsup face happy blush false", text="Она умеет читать!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Да, это так.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Несколько лет назад я купила ей книгу с драконом на обложке и все.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face happy blush false", text="Редко проходит день, чтобы она читала!", replace=True)
    call process_character (n, appearance="pose handpocket face neutral blush false", text="[sa.say_name] и я спросили, хочет ли она играть в видеоигры, но ей это не интересно.", replace=True)
    call process_character (n, appearance="pose handpocket face curious blush false", text="Сначала мы думали, что сделали что-то не так...", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Просто она такая, какая есть.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Она не даже смотрит на такие вещи.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Она хочет сама за себя решать, что ей делать.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Это она попросила остаться здесь на лето.", replace=True)
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Да?", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Я думаю, что [julia.say_name] понемногу сходит с ума дома.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Он слишком большой для нас.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="Он отлично подходит для проведения вечеринок и встреч!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Но большую часть времени многие комнаты остаются неиспользованными.", replace=True)
    call process_character (si, appearance="pose armunder face neutral blush false", text="У вас прекрасный дом.", replace=True)
    call process_character (si, appearance="pose armunder face neutral blush false", text="Но я предпочитаю дом поменьше.", replace=True)
    call process_character (si, appearance="pose armunder face happy blush false", text="Дешевле и меньше чистки!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Вы, ребята, можете зайти к нам в любое время!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Было бы здорово иметь компанию!", replace=True)
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Звучит здорово.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Мы могли бы отправиться на пляж рядом с домом бабушки.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Мне нравится туда ходить!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handface face happy blush false", text="О, пляж!", replace=True)
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Да!", replace=True)
    call process_character (si, appearance="pose handsup face neutral blush false", text="Мы собирались пойти на пляж этим летом.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Температура воды сейчас идеальная.", replace=True)
    call process_character (si, appearance="pose armunder face happy blush false", text="Я знаю [sa.say_name] и [n.say_name] очень хотят покататься на волнах!", replace=True)
    call process_character (sa, appearance="outfit clothes pose leaning face happy blush false", text="Да, да, да!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Ах да, я катаюсь по волнам.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Я могу показать [sa.say_name] и [n.say_name] как поймать большие волны!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="...", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="В любом случае, мне нужно уехать по делам.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handface face happy blush false", text="Но было здорово всех увидеть!", replace=True)
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Было приятно увидеть тебя тётя [janet.say_name]!", replace=True)
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Мы скоро снова с вами увидимся!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Просто позвони мне, когда захочешь зайти.", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="Если хотите, то заходите, не стесняйтесь!", replace=True)
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="Увидимся позже!", replace=True)
    call process_character (si, appearance="pose handsfront face neutral blush false", text="...", replace=True)
    call process_character (si, appearance="pose handsfront face neutral blush false", text="{i}Фух...{/i}", replace=True)
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Тетя [janet.say_name] конечно, имеет много энергии.", replace=True)
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Надеюсь, я смогу оставаться такой же живой, когда буду в ее возрасте!", replace=True)
    call process_character (si, appearance="pose armunder face concerned blush false", text="Только не становись такой импульсивной, как она...", replace=True)
    call process_character (k, appearance="outfit clothes pose armcross face happy blush false", text="Она как всегда врывалась без предупреждения?", replace=True)
    call process_character (si, appearance="pose handsup face shocked blush false", text="Она постучала в дверь, а потом просто вошла!", replace=True)
    call process_character (si, appearance="pose handsup face shocked blush false", text="Я и не знала, что она придет!", replace=True)
    call process_character (k, appearance="outfit clothes pose handhip face neutral blush false", text="Просто так ей нравится мама!", replace=True)
    call process_character (k, appearance="outfit clothes pose handhip face happy blush false", text="Прийтииз ниоткуда, да и ещё в неловкое время!", replace=True)
    call process_character (si, appearance="pose armunder face neutral blush false", text="Да, но раньше она не могла этого сделать, так как мы жили далеко.", replace=True)
    call process_character (si, appearance="pose armunder face embarrassed blush false", text="Но теперь мы так близко...", replace=True)
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Я бы не слишком беспокоилась об этом, мама.", replace=True)
    call process_character (k, appearance="outfit clothes pose armsup face neutral blush false", text="Похоже, она хочет, чтобы мы её навещали, чем наоборот.", replace=True)
    call process_character (sa, appearance="outfit clothes pose leaning face neutral blush false", text="Я так сильно хочу пойти на пляж!", replace=True)
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Я знаю, милая!", replace=True)
    call process_character (si, appearance="pose handsfront face neutral blush false", text="Я надеюсь, что скоро мы все сможем пойти вместе.", replace=True)
    call process_character (si, appearance="pose handsfront face happy blush false", text="Но вы можете пойти с тетей [janet.say_name] если так не терпится!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="Ура!", replace=True)
    call process_character (sa, appearance="outfit clothes pose handsbehind face happy blush false", text="Бьюсь об заклад, она мастер-сёрфингист!", replace=True)
    call process_character (si, appearance="pose handsfront face neutral blush false", text="То же самое касается и тебя, [n.say_name].", replace=True)
    call process_character (si, appearance="pose armunder face curious blush false", text="Хотя иногда она может быть бестактной....{w=1.0} Ей нравится видеть вас, ребята .", replace=True)
    call process_character (si, appearance="pose armunder face happy blush false", text="Но если ты хочешь быть как она, будь готова просыпаться с петухами!", replace=True)
    call process_character (si, appearance="pose armunder face happy blush false", text="Она - истинное определение ранней пташки!", replace=True)
    call process_character (n, appearance="pose handfist face happy blush false", text="Было бы здорово видеть ее почаще!", replace=True)

    $ reset_all_characters()
    if started_main_game:
        $ had_janet_intro_scene = True
        $ reset_all_characters()
        call day_reset_locations_chars
        call day_start_after_location_reset
    else:
        jump debug_menu

    return

label janet_scene_intro_2(dream=False):
    call janet_scene_intro_2_sex (dream)
    return

label janet_scene_intro_2_sex(dream=False):
    if week.time == "day":
        call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="(Думаю, сегодня я буду тусить с тетей [janet.say_name]!)")
    else:
        call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="(Думаю, вечером затусить с тетей [janet.say_name]!)")

    call process_scene_beginning (bg=janet_house, char_tuple_array=[ (n, "outfit clothesjacket pose handpocket"), (janet, "outfit clothes pose handhips face happy") ], dream=dream )

    call process_character (janet, appearance="outfit clothes pose handhip face happy blush false", text="Я так рада, что ты смог зайти [n.say_name]!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Я тоже!")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Я правильно тебя сорентировала?")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Да!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Маршрут синхронизировался с моим телефоном и привел меня сюда!")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Эти смартфоны удивительны.")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Я могу все на нем сделать!")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Я знаю, что люди моего возраста обычно пугаются этой технологии...")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Но я честно не знаю, что бы я делала без этой штуки!")
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Он дорог мне больше, чем кошелек!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Мне и [sa.say_name] тоже нравится пользоваться ими.")
    call process_character (n, appearance="pose handpocket face happy blush false", text="В телефонах тонны игр!!")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Как дела у тебя и [sa.say_name]?")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Наверное, хотите, чтобы лето продолжалось вечно?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Это было бы здорово, да...")
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="Я чувствовала то же самое, когда ходила в школу!")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Я вообще-то прогуливала занятия, чтобы пораньше поиграть на улице.")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Да ладно!")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Только не смей так делать!")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Твоя мама с ума сойдёт!")
    call process_character (janet, appearance="outfit clothes pose handface face happy blush false", text="А что будет, если она узнает, что это я тебе дала идею, ха-ха!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Она заставляет делать домашнюю работу, если я пропускаю занятия.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Поэтому я не хожу на занятия, только если болею или еще что-нибудь.")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Молодец.")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Чем раньше отучишься, тем раньше отдохнёшь!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="О! Говоря о веселье!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Мы можем пойти на пляж сегодня?")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Знаешь, я знала, что ты собираешься спросить меня...")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="И я с удовольствием тебя возьму!")
    call process_character (janet, appearance="outfit clothes pose handface face angry blush false", text="Но, к сожалению...")

    call process_character (n, appearance="pose handpocket face concerned blush false")

    call process_character (n, appearance="pose handpocket face concerned blush false", text="...")
    call process_character (janet, appearance="outfit clothes pose handface face angry blush false", text="...")
    call process_character (janet, appearance="outfit clothes pose handface face angry blush false", text="Ух! Тот случай просто бесит меня!")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Что случилось?")
    call process_character (janet, appearance="outfit clothes pose handhips face angry blush false", text="Пришла я на пляж вчера утром, как обычно...")
    call process_character (janet, appearance="outfit clothes pose handchest face shock blush false", text="Внезапно эта старушка подошла ко мне!")
    call process_character (janet, appearance="outfit clothes pose handchest face shock blush false", text="И она говорит мне убираться к черту с ее пляжа!")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
    call process_character (janet, appearance="outfit clothes pose handhips face angry blush false", text="Я сказала ей, что один из членов моей семьи владеет недвижимостью на этом пляже.")
    call process_character (janet, appearance="outfit clothes pose handhips face angry blush false", text="Но она продолжала кричать и требовать, чтобы я ушла!")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Она не поверила тебе?")
    call process_character (janet, appearance="outfit clothes pose handchest face angry blush false", text="Я хотела сказать ей, что не надо толочь воду в ступе!")
    call process_character (janet, appearance="outfit clothes pose handchest face angry blush false", text="Терпеть не могу людей, которые думают, что владеют пляжем!")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="...")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Значит, мы не можем пойти?")
    call process_character (janet, appearance="outfit clothes pose handface face angry blush false", text="О, не волнуйся!")
    call process_character (janet, appearance="outfit clothes pose handface face angry blush false", text="Я быстро со всем разберусь с помощью твоей бабушки!")
    call process_character (janet, appearance="outfit clothes pose handhips face angry blush false", text="Я не хочу, чтобы нас преследовала какая-то капризная сучка!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (janet, appearance="outfit clothes pose handface face embarrassed blush false", text="...")
    call process_character (janet, appearance="outfit clothes pose handface face embarrassed blush false", text="Прости, я не должна так говорить рядом с тобой.")
    call process_character (janet, appearance="outfit clothes pose handface face embarrassed blush false", text="Это просто раздражало меня!")
    call process_character (janet, appearance="outfit clothes pose handface face embarrassed blush false", text="Никогда не было проблем, а теперь меня гонят с пляжа!")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Да, это слишком плохо.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Я так ждал этого.")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Я обещаю, как только все будет улажено, я дам тебе знать!")
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Мой племянник заслуживает насладиться пляжем, черт возьми!")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Угощайся закусками, если хочешь!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Ладно, круто.")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="И я с удовольствием пообщаюсь с тобой!")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Обычно у нас нет шанса остаться один на один.")
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Я бы хотела наверстать упущенное!")



    call process_end_of_scene ("janet_scene_intro_2", char=janet, dream=dream, force_no_boldness=True, force_not_replayable=True)

    return

label janet_scene_minigame_intro(dream=False):
    call janet_scene_minigame_intro_sex (dream)
    return

label janet_scene_minigame_intro_sex(dream=dream):
    $ display_multiple_characters([ (n, ""), (janet, "pose handhips face happy blush false") ])

    call process_character (janet, appearance="pose handhips face happy blush false", text="Сегодня твой счастливый день, [n.say_name]!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Почему так?")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Помнишь, я сказал, что разберусь с ситуацией на пляже?")
    call process_character (janet, appearance="pose handface face happy blush false", text="Всё было решено!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="{i}Ухх!{/i}")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Значит, мы можем пойти?!")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Я уже упаковала в свою машину пляжное снаряжение!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Я рада, что мама сказала мне взять плавки на всякий случай!")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="День еще только начался, так что мы получим много солнца!")
    call process_character (janet, appearance="pose handchest face happy blush false", text="Поехали!")

    call fade_to_black (0.5)
    "{i}Немного позже...{/i}"

    call bust_art_background (name="bg beach_daytime", dream=False)

    call process_character (n, appearance="outfit swimsuit pose handsdown face happy blush false", text="(Это место действительно хорошее!)")
    call process_character (n, appearance="outfit swimsuit pose handsdown face happy blush false", text="(Мама, [sa.say_name], и [k.say_name] хотели бы этого!)")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Разве здесь не замечательно?")
    call process_character (n, appearance="outfit swimsuit pose handfist face happy blush false", text="Это точно!")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Это все благодаря твоей бабушке!")
    call process_character (n, appearance="outfit swimsuit pose handsdown face happy blush false")
    call process_character (janet, appearance="outfit swimsuit pose handface face neutral blush false", text="Я говорила с ней по телефону о том, как меня выгнали с пляжа на днях.")
    call process_character (janet, appearance="outfit swimsuit pose handface face neutral blush false", text="Все, что она сделала, это сделала несколько звонков в офис...")
    call process_character (janet, appearance="outfit swimsuit pose handface face happy blush false", text="И теперь у нас есть специальные пропуска, чтобы получить доступ к пляжу, когда нам нравится!")
    call process_character (n, appearance="outfit swimsuit pose handsdown face happy blush false", text="Это так здорово!")
    call process_character (n, appearance="outfit swimsuit pose handsdown face happy blush false", text="[k.say_name], [sa.say_name] и моя мама тоже могут прийти сюда?")
    call process_character (janet, appearance="pose handchest face happy blush false", text="О, конечно!")
    call process_character (janet, appearance="pose handchest face happy blush false", text="Ты можешь рассказать им всё об этом месте, чтобы они захотели приехать!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Конечно!")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Этот океан кристально чист!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Здесь бывают большие волны?")
    call process_character (janet, appearance="pose handhips face happy blush false", text="Они могут стать очень большими, да!")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Сегодня ветер тихий, поэтому океан спокойный.")
    call process_character (n, appearance="pose handfist face happy blush false", text="Я хочу войти в него!")
    call process_character (janet, appearance="pose handchest face happy blush false", text="Я тоже!")
    call process_character (janet, appearance="pose handchest face happy blush false", text="Ты хорошо умеешь плавать?")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="У меня стало получаться гораздо лучше!")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="[sa.say_name] и я много плаваем в бассейне дома.")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Ты когда-нибудь плавал в океане?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Не думаю, нет.")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Это сложнее, чем в бассейне.")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Соленая вода плотнее пресной, так что ты будешь тратить больше энергии.")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Плюс приливное течение толкает тебя.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Насколько это сложнее?")
    call process_character (janet, appearance="pose handhips face happy blush false", text="Ты заметишь, как только начнёшь плыть на перегонки со мной!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Как далеко мы можем заплыть?")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Я использую пальмы и зонтики вдоль пляжа в качестве ориентира.")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Я не уплыву далеко, пока я с тобой.")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Может, пару сотен футов?")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Ты хорошо плаваешь?")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Ну, я плавала в океане еще до твоего рождения.")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Так что для меня это не проблема.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Я не думаю, что смогу победить тебя...")
    call process_character (janet, appearance="pose handhips face happy blush false", text="Не сдавайся, пока не начал, [n.say_name]!")
    call process_character (janet, appearance="pose handhips face happy blush false", text="Ты удивишься самому себе!")
    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Я всегда могу замедлиться, если потребуется.")

    call process_character (n, appearance="pose handsdown face neutral blush false")

    call process_character (janet, appearance="pose handchest face happy blush false", text="Ну же!")
    call process_character (janet, appearance="pose handchest face happy blush false", text="Эта мерцающая вода заманчивая!")

    window hide
    menu:
        "Играть в мини-игру Гонки":
            call process_end_of_scene ("janet_scene_minigame_intro", char=janet, dream=dream, force_no_boldness=True, force_not_replayable=True, do_not_jump=True)
            call minigame_racing (partner=janet)
        "Не играть":
            call process_end_of_scene ("janet_scene_minigame_intro", char=janet, dream=dream, force_no_boldness=True, force_not_replayable=True, do_not_jump=started_main_game)
            if started_main_game:
                $ janet.scene = ""
                $ janet_house.start()

    return

label janet_scene_underwear(dream=False):
    call janet_scene_underwear_sex (dream)
    return

label janet_scene_underwear_sex(dream=False):
    call process_scene_beginning (bg="bg janet_house_daytime", char_tuple_array=[ (n, "outfit clothesjacket pose handpocket"), (janet, "outfit clothes pose handhips face neutral blush false") ], dream=dream )

    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Готов снова сходить на пляж?")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Будь уверена!")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Думаю, сегодня волны будут большие!")
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="Мы сможем проплыть на них всю дорогу до берега!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Круто!")

    call fade_to_black (0.5)
    "{i}Позднее в этот же день...{/i}"

    call bust_art_background (name="bg janet_house_daytime", dream=False)
    $ display_multiple_characters([ (n, "outfit swimsuit pose handsdown face neutral blush false"), (janet, "outfit swimsuit pose handhips face happy blush false") ])

    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false")

    call process_character (janet, appearance="outfit swimsuit pose handhips face happy blush false", text="Это были мощные волны!")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face neutral blush false", text="Да!")
    call process_character (n, appearance="outfit swimsuit pose behindhead face embarrassed blush false", text="Я думал, что волны уничтожат меня...")
    call process_character (janet, appearance="outfit swimsuit pose handface face happy blush false", text="О да, держу пари, ха-ха!")
    call process_character (janet, appearance="outfit swimsuit pose handface face neutral blush false", text="Некоторые волны обманчивы.")

    call process_character (n, appearance="outfit swimsuit pose behindhead face neutral blush false")

    call process_character (janet, appearance="outfit swimsuit pose handface face neutral blush false", text="Как только они ударяются о песчаную отмель, они растут и растут...")
    call process_character (janet, appearance="outfit swimsuit pose handface face neutral blush false", text="Пока они не окажутся над твоей головой!")
    call process_character (n, appearance="outfit swimsuit pose handsdown face happy blush false", text="Ты отлично прокатился по каждой волне!")
    call process_character (janet, appearance="outfit swimsuit pose handchest face neutral blush false", text="Ты, возможно, заметил, что я не пыталась поймать каждую волну.")
    call process_character (janet, appearance="outfit swimsuit pose handchest face neutral blush false", text="Я ищу определенные волны, которые могу преодолеть.")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face neutral blush false", text="А как узнать, какие волны действительно хорошие!")
    call process_character (janet, appearance="outfit swimsuit pose handhip face neutral blush false", text="Это одна из тех вещей, которые просто приходят с опытом.")
    call process_character (janet, appearance="outfit swimsuit pose handhip face neutral blush false", text="Нужно научиться понимать тип волны.")
    call process_character (janet, appearance="outfit swimsuit pose handhip face happy blush false", text="Это не займет много времени!")
    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false", text="Круто.")
    call process_character (janet, appearance="outfit swimsuit pose handchest face concerned blush false", text="Бррр!")
    call process_character (janet, appearance="outfit swimsuit pose handchest face concerned blush false", text="Это настоящая проблема, когда на пляже нет кабинок для переодевания...")
    call process_character (janet, appearance="outfit swimsuit pose handchest face concerned blush false", text="Ты должен идти в плавках всю дорогу домой!")
    call process_character (n, appearance="outfit swimsuit pose behindhead face concerned blush false", text="Да, я довольно-таки замёрз.")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Позволь мне быстренько заскочить в душ, а потом ты сможешь зайти.")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Я быстро.")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Выходи на солнце, если нужно согреться!")

    $ character_leave_dissolve(janet)
    pause 0.5

    call process_character (n, appearance="pose handsdown face neutral blush false", text="...{p}...")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="(Было очень весело на пляже)")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="(Но в плавках холодно!)")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="(Мои яйца на того половина размера, которого они должны быть!)")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="...")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="(Я думаю, выйти на солнце, как тетя [janet.say_name] предложила...)")

    call fade_to_black (0.5)
    call bust_art_background (name="bg janet_house_daytime", dream=False)

    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false", text="(В тепле хорошо)")
    call process_character (n, appearance="outfit swimsuit pose handsdown face concerned blush false", text="(Но под кондиционером очень холодно!)")
    call process_character (n, appearance="outfit swimsuit pose handsdown face concerned blush false", text="...")

    call process_character (janet, text="Я уже выхожу!")
    call process_character (janet, text="Я уверена, что ты замерз!")

    call process_character (janet, appearance="outfit underwear pose handface face neutral blush false", text="Очень приятно принимать горячий душ!")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="...{p}...")
    call process_character (janet, appearance="outfit underwear pose handchest face curious blush false", text="...")
    call process_character (janet, appearance="outfit underwear pose handchest face curious blush false", text="Ты в порядке, [n.say_name]?")
    call process_character (n, appearance="pose behindhead face curious blush true", text="...")
    call process_character (n, appearance="pose behindhead face curious blush true", text="(Я вижу нижнюю часть ее сисек, торчащую из ее рубашки...")
    call process_character (janet, appearance="outfit underwear pose handchest face concerned blush false", text="(О...)")
    call process_character (janet, appearance="outfit underwear pose handchest face concerned blush false", text="(Я вижу, что произошло...)")
    call process_character (janet, appearance="outfit underwear pose handface face concerned blush false", text="(Я должна была надеть шорты или футболку)")
    call process_character (janet, appearance="outfit underwear pose handface face concerned blush false", text="(Это видимо неудобно для него)")
    call process_character (n, appearance="pose handsdown face curious blush true", text="...")
    call process_character (janet, appearance="outfit underwear pose handchest face neutral blush false", text="Странно видеть свою тетю такой, не так ли?")
    call process_character (janet, appearance="outfit underwear pose handchest face concerned blush false", text="Я быстро выбежала из душа, чтобы ты мог войти быстрее!")
    call process_character (janet, appearance="outfit underwear pose handchest face concerned blush false", text="Так что я успела надеть только нижнее белье.")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="О-ох...")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="Всё в порядке.")
    call process_character (janet, appearance="outfit underwear pose handface face curious blush false", text="Ты уверен?")
    call process_character (janet, appearance="outfit underwear pose handface face curious blush false", text="Я заметила, как ты застыл на месте, когда увидел меня.")
    call process_character (n, appearance="pose handsdown face curious blush true", text="...")
    call process_character (n, appearance="pose handsdown face curious blush true", text="Со мной все в порядке.")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Я пойду...{w=1.0}прими душ.")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (janet, appearance="outfit underwear pose handhips face concerned blush false", text="...")
    call process_character (janet, appearance="outfit underwear pose handhips face concerned blush false", text="(Ему ещё не совсем комфортно возле меня)")
    call process_character (janet, appearance="outfit underwear pose handhips face concerned blush false", text="...")
    call process_character (janet, appearance="outfit underwear pose handface face curious blush false", text="(Он выглядел потрясённым)")
    call process_character (janet, appearance="outfit underwear pose handface face curious blush false", text="...")
    call process_character (janet, appearance="outfit underwear pose handface face curious blush false", text="(Если подумать об этом...)")
    call process_character (janet, appearance="outfit underwear pose handface face neutral blush false", text="(Он изучал моё тело некоторое время...)")

    python:
        janet.revistable_scenes.add("janet_scene_underwear_revisit")
        if not dream:
            stats.add_stat("times_seen_panties", 1)
            stats.add_stat("times_seen_bra", 1)

    call process_end_of_scene ("janet_scene_underwear", char=janet, dream=dream)

    return

label janet_scene_topless(dream=False):
    call janet_scene_topless_sex (dream)
    return

label janet_scene_topless_sex(dream=False):
    call process_scene_beginning (bg=janet_house, char_tuple_array=[ (n, "outfit clothesjacket pose handpocket"), (janet, "outfit clothes pose handchest face happy blush false") ], dream=dream )
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="Ах, ты как раз вовремя, [n.say_name]!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Для чего?")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Мне нужна твоя помощь кое в чем.")

    if "janet_convo_3" in janet.conversations_completed:
        call process_character (janet, appearance="pose handhips face neutral blush false", text="Помнишь, я говорила тебе, что занимаюсь фотографией?")
        call process_character (n, appearance="pose handpocket face neutral blush false", text="Да.")
        call process_character (janet, appearance="pose handhips face neutral blush false", text="Ты научишь меня?")
        call process_character (n, appearance="pose handfist face happy blush false", text="Конечно!")
        call process_character (janet, appearance="pose handchest face happy blush false", text="Отлично!")
        call process_character (janet, appearance="pose handchest face happy blush false", text="Я настроила камеру, так что тебе просто нужно нажимать кнопку спуска затвора.")
    else:
        call process_character (janet, appearance="pose handhips face neutral blush false", text="Ты умеешь пользоваться цифровой камерой?")
        call process_character (n, appearance="pose handfist face neutral blush false", text="Я в основном использую свой телефон для фотографий, но да, думаю, что да.")
        call process_character (janet, appearance="pose handhips face neutral blush false", text="Я установил все параметры на моей камере, так что вам просто нужно нажать кнопку спуска затвора.")

    call process_character (n, appearance="pose behindhead face neutral blush false", text="Что я буду фотографировать?")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Вообще-то, ты будешь меня фотографировать.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Тебя тётя [janet.say_name]?")
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="Звучит просто, не так ли?")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Так и есть!")
    call process_character (n, appearance="pose twohandfist face curious blush false", text="Но разве ты не могла сделать это сама?")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Было бы слишком много возни с настройкой и надо каждый раз вставать в позу.")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Когда ты будешь снимать, мне не о чем будет беспокоиться.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Позу?")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Ага.")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="А потом выберу, какие из фотографий мне понравятся больше.")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Довольно обыденная работа в деле фотографа.")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="О, есть еще один аспект...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Хм?")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Я буду без верха.")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="Б-без верха?!")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Да.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Тебе обязательно нужно сниматься так?")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Почему?")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Твоя мама никогда бы не хотела, чтобы ты узнал об этом, пока не станешь намного старше, но...")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Я была моделью долгое время.")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Обнаженной моделью.")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="О-обнаженной моделью?!")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Именно так я узнала много о фотографии и заинтересовалась ею.")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Однажды ко мне подошли для фотосессии...")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Но им нужно было, чтобы модель была голой.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="...")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Ни одна модель не захотела сниматься голой, а оплата показалась мне хорошей, и я согласилась.")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Съемка была легкой, и я думала, что это одноразовая сделка.")
    call process_character (janet, appearance="pose handface face happy blush false", text="После неё, мне звонили из разных агентств и журналов!")
    call process_character (janet, appearance="pose handface face happy blush false", text="Я даже попала на обложку однажды!")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Ты была на обложке журнала?")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Твоя мама хотела, чтобы ты держался подальше от этого.")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Но ты ведь видел голых девушек раньше, верно?")

    $ janet_scene_topless_girls_seen_nude = 0
    python hide:
        if "kira_scene_6" in scenes_completed:
            store.janet_scene_topless_girls_seen_nude += 1
        if "simone_scene_undressing" in scenes_completed:
            store.janet_scene_topless_girls_seen_nude += 1
        if "julia_scene_topless" in scenes_completed:
            store.janet_scene_topless_girls_seen_nude += 1
        if "sam_scene_2_seq_2" in scenes_completed:
            store.janet_scene_topless_girls_seen_nude += 1
        if "gloryhole_scene_stall" in scenes_completed:
            store.janet_scene_topless_girls_seen_nude += 1
        if "vicky_fondle_scene" in scenes_completed:
            store.janet_scene_topless_girls_seen_nude += 1
        if "edna_scene_topless" in scenes_completed:
            store.janet_scene_topless_girls_seen_nude += 1

    if janet_scene_topless_girls_seen_nude >= 3:
        call process_character (n, appearance="pose behindhead face curious blush false", text="Вообще-то, я видел много голых девушек...")
        call process_character (janet, appearance="pose handface face shock blush false", text="Да?!")
        call process_character (janet, appearance="pose handface face shock blush false", text="...")
        call process_character (janet, appearance="pose handface face shock blush false", text="(Означает ли это, что у него уже был...)")
        call process_character (janet, appearance="pose handface face shock blush false", text="...{p}...")
        call process_character (janet, appearance="pose handchest face curious blush false", text="Тогда в чем проблема увидеть меня голой?")
        call process_character (janet, appearance="pose handchest face neutral blush false", text="Это потому, что я твоя тетя, не так ли?")
        call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    elif janet_scene_topless_girls_seen_nude > 1 or (stats.stat_value("times_seen_breasts") > 0 and stats.stat_value("times_seen_vagina") > 0):
        call process_character (n, appearance="pose behindhead face curious blush false", text="Я-я, да...")
        call process_character (janet, appearance="pose handchest face happy blush false", text="А, я понимаю...")
        call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
        call process_character (janet, appearance="pose handface face neutral blush false", text="Ты не уверен, потому что я твоя тетя?")
        call process_character (janet, appearance="pose handface face happy blush false", text="Я видела, как ты отреагировал, когда увидел меня в нижнем белье.")
        call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    else:
        call process_character (n, appearance="pose handpocket face concerned blush false", text="Н-Нет...")
        call process_character (janet, appearance="pose handchest face curious blush false", text="Правда?")
        call process_character (janet, appearance="pose handchest face curious blush false", text="Даже в журнале, по телевизору или на компьютере?")
        call process_character (n, appearance="pose behindhead face curious blush false", text="...")
        call process_character (janet, appearance="pose handface face embarrassed blush false", text="(Чёрт...)")
        call process_character (janet, appearance="pose handface face embarrassed blush false", text="(Это объясняет, почему он так нервничал, когда видел меня в нижнем белье...)")

    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Я не виню тебя, если ты думаешь, что это странно.")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Для меня это тоже странно.")
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="Я попросила племянника сфотографировать меня частично обнаженной!")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="...{p}...")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Я прошу тебя, потому что у меня очень мало времени.")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Компании срочно нужны были снимки моделей, потому что они потеряли фотографии.")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Они знают, что я надежная старая модель.")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="...")
    call process_character (janet, appearance="outfit clothes pose handchest face embarrassed blush false", text="Странно говорить, что я модель \"постарше\"...")
    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (janet, appearance="outfit clothes pose handface face concerned blush false", text="Это причина, почему ты не хочешь меня фотографировать?")
    call process_character (janet, appearance="outfit clothes pose handface face concerned blush false", text="Думаешь, я выгляжу старой?")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="Н-Нет!")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="Это вообще не причина!")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="Я думаю, что ты очень красивая тетя [janet.say_name]!")
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="О!")
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="Какое облегчение!")
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="У меня даже проявилось минутное беспокойство!")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="...")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Я не хочу давить на тебя.")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Я всегда могу сделать это сама, но это займет немного больше времени.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="...")
    call process_character (n, appearance="pose handfist face concerned blush false", text="Я...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Я хочу помочь тебе тетя [janet.say_name].")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Я справлюсь.")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Ты уверен?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Да, я в этом уверен.")
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="[n.say_name], спасибо!")
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="Это сэкономит мне столько времени!")

    call character_leave_dissolve (janet)
    pause 0.5

    call process_character (janet, text="...{p}...")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Background Groove.ogg", fadein = 1.0)

    call process_character (janet, appearance="outfit topless pose handhips face neutral blush false")
    pause 0.5

    call process_character (n, appearance="pose behindhead face curious blush true", text="...")
    call process_character (janet, appearance="outfit topless pose handhips face neutral blush false", text="Ладно, камера включена?")
    call process_character (janet, appearance="outfit topless pose handhips face curious blush false", text="Ты видишь меня на экране фотоаппарата?")
    call process_character (n, appearance="pose handpocket face curious blush true", text="Д-Да...")
    call process_character (janet, appearance="outfit topless pose handhips face happy blush false", text="Отлично!")
    call process_character (janet, appearance="outfit topless pose handchest face neutral blush false", text="Просто фотографируй каждый раз, когда я позирую, хорошо?")
    call process_character (janet, appearance="outfit topless pose handchest face neutral blush false", text="Держи меня в кадре, это всё, о чем нужно беспокоиться.")
    call process_character (n, appearance="pose handfist face neutral blush true", text="Ладно.")
    call process_character (janet, appearance="outfit topless pose handface face happy blush false", text="Начинай снимать!")

    "{i}Клик{/i}"

    call process_character (janet, appearance="outfit topless pose handhips face flirt blush false")

    "{i}Клик-Клик{/i}"

    call process_character (janet, appearance="outfit topless pose handchest face flirt blush false")

    "{i}Клик...{/i}"

    call fade_to_black (0.5)
    call bust_art_background (name=janet_house, dream=False)

    $ display_multiple_characters([ (n, "outfit clothesjacket_hard pose handpocket face neutral blush false"), (janet, "outfit clothes pose handhips face neutral blush false") ])

    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Этого должно быть достаточно!")
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="[n.say_name], ты мой спаситель!")
    call process_character (n, appearance="outfit clothesjacket_hard pose twohandfist face neutral blush false", text="Всегда пожалуйста, тетя [janet.say_name].")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Это было не слишком плохо?")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Видеть свою тетю топлесс?")
    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face neutral blush false", text="Нет, это было не плохо...")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="...")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="(У него небольшой стояк)")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="(Я думаю, что мой племянник поклонник...)")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="...")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Хочешь сегодня органическую пиццу?")
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="Я угощаю за то, что помог мне выбраться из передряги!")
    call process_character (n, appearance="outfit clothesjacket_hard pose twohandfist face happy blush false", text="Я люблю пиццу, да!")
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Я закажу её прямо сейчас!")

    python:
        janet.revistable_scenes.add("janet_scene_topless_revisit")
        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_seen_breasts", 1)

    call process_end_of_scene ("janet_scene_topless", char=janet, dream=dream)

    return

label janet_scene_bottomless(dream=False):
    call janet_scene_bottomless_sex (dream)
    return

label janet_scene_bottomless_sex(dream=False):
    call process_scene_beginning (bg=janet_house, char_tuple_array=[ (n, "outfit clothesjacket pose handpocket"), (janet, "outfit clothes pose handchest face happy blush false") ], dream=dream )

    call process_character (janet, appearance="pose handchest face happy blush false", text="Компания была очень впечатлена этими фотографиями [n.say_name]!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Да?")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Они думают, что ракурсы были отличными, и с нетерпением ждут, чтобы увидеть больше!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Что?")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Это очень важно, когда компания хвалит твои фотографии.")
    call process_character (janet, appearance="pose handface face happy blush false", text="У тебя есть талант, [n.say_name]!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Думаешь?")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Это дар.")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Было бы жалко тратить его впустую.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Так ты говоришь о...")
    call process_character (janet, appearance="pose handhips face happy blush false", text="Я думаю, что мы должны сделать больше фотосессий!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Еще?")
    call process_character (janet, appearance="pose handchest face happy blush false", text="Да, прямо сейчас!")
    call process_character (janet, appearance="pose handchest face happy blush false", text="Это для компании, делающих эпиляцию в зоне бикини.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Что они хотят увидеть?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Ты будешь в бикини?")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Хорошая догадка!")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Но нет.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Что же тогда?")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Им нужны примеры полностью бритых зон бикини.")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Это для того, чтобы женщины могли видеть, как может выглядеть конечный результат.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Зоны бикини?")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Я не понимаю, что ты имеешь в виду.")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Я имею в виду, что ты будешь фотографировать мою тазовую область.")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Промежность.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face embarrassed blush false", text="П-промежность?!")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Женщины там постоянно делают эпиляцию.")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Она должна быть крупным планом или в режиме макросъемки, как они это называют.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face embarrassed blush false", text="{i}Сглатывает{/i}.")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face embarrassed blush false", text="Крупным планом?")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Ты нервничаешь, потому что возбудишься во время съёмки?")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face embarrassed blush true", text="Уух?!")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Я понимаю, что могу вызвать такую реакцию, [n.say_name].")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Я ничего не имею против, если это произойдет.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush true", text="...")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Я привлекательна для тебя, даже если я твоя тетя.")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Ты сам сказал, что считаешь меня очень красивой.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush true", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush true", text="Т-ты...")
    call process_character (janet, appearance="pose handhips face happy blush false", text="Тогда я могу быть спокойна, [n.say_name]!")
    call process_character (janet, appearance="pose handhips face happy blush false", text="Я хочу, чтобы ты повеселился и наслаждался этим!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Правда?")
    call process_character (janet, appearance="pose handhip face neutral blush false", text="На самом деле, ты должен получать за это деньги.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Да?")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Технически, ты работаешь на меня, помогаешь завершить фотосессию.")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Поэтому ты должен получить некоторую компенсацию за свои усилия.")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Как насчет пятнадцати долларов?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Мне заплатят за это?")
    call process_character (janet, appearance="pose handhips face happy blush false", text="Ну конечно!")
    call process_character (janet, appearance="pose handhips face happy blush false", text="В конце концов, эти фотографии - часть бизнеса.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Я получу пятнадцать долларов?")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Становится еще лучше, когда в дело вступают наличные, да?")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Д-да, это действительно так!")
    call process_character (n, appearance="outfit clothesjacket pose handfist face neutral blush false", text="Давай фотографироваться!")

    call character_leave_dissolve (janet)
    pause 0.5

    call process_character (janet, text="...{p}...")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadein = 1.0)

    call process_character (janet, appearance="outfit bottomless pose handhips face neutral blush false")
    pause 0.5


    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false")

    call process_character (janet, appearance="outfit bottomless pose handhips face neutral blush false", text="Давай я поставлю камеру на штатив.")
    call process_character (janet, appearance="outfit bottomless pose handhips face neutral blush false", text="Им, наверное, нужны снимки с низкого ракурса.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Низкий ракурс?")
    call process_character (janet, appearance="outfit bottomless pose handchest face neutral blush false", text="К счастью, я недавно сделала эпиляцию.")
    call process_character (janet, appearance="outfit bottomless pose handchest face neutral blush false", text="Значит, щетины нет.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="(Щетина?)")
    call process_character (janet, appearance="outfit bottomless pose handface face neutral blush false", text="Хорошо, объектив должен быть в правильном фокусе...")
    call process_character (janet, appearance="outfit bottomless pose handface face curious blush false", text="Как это выглядит на экране?")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Я ... я могу видеть твою...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Я могу увидеть...")
    call process_character (janet, appearance="outfit bottomless pose handchest face neutral blush false", text="Я понимаю, к чему ты клонишь!")
    call process_character (janet, appearance="outfit bottomless pose handchest face neutral blush false", text="Нажми кнопку, чтобы сделать несколько снимков!")

    "{i}Клик-Клик{/i}{p}{i}Клик-Клик{/i}"

    call fade_to_black (0.5)
    call bust_art_background (name=janet_house, dream=False)

    $ display_multiple_characters([ (n, "outfit clothesjacket_hard pose handpocket face neutral blush false"), (janet, "outfit clothes pose handhips face neutral blush false") ])

    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Эти фото будут просто отличными!")

    show screen hud

    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Вот тебе, [n.say_name], за твой труд!")

    $ inventory.add_money(15, tag = "janet_bottomless")
    "{b}Получено $15!{/b}"

    call process_character (n, appearance="outfit clothesjacket_hard pose handfist face neutral blush false", text="Спасибо тетя [janet.say_name]!")

    hide screen hud

    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Спасибо [n.say_name] для помог с этим!")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Я знаю, что эта тема немного взрослая для тебя.")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Но ты справляешься с этим довольно хорошо!")
    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face neutral blush false", text="С-Спасибо.")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Это был продуктивный день [n.say_name]!")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Я думаю, ты заслуживаешь хорошо отдохнуть после этого.")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Почему бы тебе не отправиться домой?")
    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face neutral blush false", text="Д-Да.")
    call process_character (n, appearance="outfit clothesjacket_hard pose handpocket face neutral blush false", text="Звучит неплохо.")
    call process_character (janet, appearance="outfit clothes pose handface face neutral blush false", text="Если твоя мама спросит о деньгах, скажи ей, что это был ранний подарок на день рождения!")

    python:
        janet.revistable_scenes.add("janet_scene_bottomless_revisit")
        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_seen_vagina", 1)

    call process_end_of_scene ("janet_scene_bottomless", char=janet, dream=dream)

    return

label janet_scene_naked(dream=False):
    call janet_scene_naked_sex (dream)
    return

label janet_scene_naked_sex(dream=False):
    call process_scene_beginning (bg=janet_house, char_tuple_array=[ (n, "outfit clothesjacket pose handpocket"), (janet, "outfit clothes pose handhips face neutral blush false") ], dream=dream )

    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Ты когда-нибудь был у океана ночью?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Когда были фейерверки, я был там раньше.")
    call process_character (janet, appearance="outfit clothes pose handchest face neutral blush false", text="Я говорю о том, чтобы плавать ночью в океане.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="О, плавание?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Нет, я никогда этого не делал.")
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="О ты должен испытать это хотя бы раз!")
    call process_character (janet, appearance="outfit clothes pose handchest face happy blush false", text="Это трудно описать словами.")
    call process_character (janet, appearance="outfit clothes pose handhips face happy blush false", text="Вот почему ты просто должен сходить!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Да, конечно!")
    call process_character (janet, appearance="outfit clothes pose handhips face neutral blush false", text="Я приготовлю ужин, а потом мы пойдем гулять!")

    call process_new_location (bg="bg beach_evening", char_tuple_array=[ (n, "outfit swimsuit pose handsdown face neutral blush false"), (janet, "outfit swimsuit pose handhips face neutral blush false") ], dream=dream)

    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false", text="Мы здесь одни?")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Похоже на то!")
    call process_character (janet, appearance="outfit swimsuit pose handchest face neutral blush false", text="Это другая крутая часть плавания ночью.")
    call process_character (janet, appearance="outfit swimsuit pose handchest face neutral blush false", text="Когда никого нет рядом, атмосфера сильно отличается..")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face happy blush false", text="Отражение на воде выглядит так здорово!")
    call process_character (janet, appearance="outfit swimsuit pose handchest face neutral blush false", text="Я знаю, разве это не прекрасно?")
    call process_character (janet, appearance="outfit swimsuit pose handchest face neutral blush false", text="Луна отражается от океана.")
    call process_character (n, appearance="outfit swimsuit pose handfist face happy blush false", text="Пойдем!")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Подожди, дай я прикреплю фонарик на тебя.")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Так мы сможем увидеть друг друга в воде.")

    call fade_to_black (0.5)
    "{i}Бульк-Бульк{/i}"

    call process_character (n, appearance="outfit swimsuit pose handfist face happy blush false", text="Вода теплая!")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Она нагрелась от солнца!")

    "{i}Бульк-Бульк{/i}"

    call process_character (n, appearance="blush false", text="Ты права, тетя [janet.say_name]!")
    call process_character (n, appearance="blush false", text="Это не похоже ни на что, что я делал раньше!")
    call process_character (janet, appearance="blush false", text="Я же говорила!")
    call process_character (janet, appearance="blush false", text="Это как укромный рай ночью!")
    call process_character (n, appearance="blush false", text="Да, как секретное место, о котором знаем только мы!")
    call process_character (janet, appearance="blush false", text="Эй!")
    call process_character (janet, appearance="blush false", text="Наперегонки до берега?")
    call process_character (n, appearance="blush false", text="Окей!")
    call process_character (n, appearance="blush false", text="Вперед!")
    call process_character (janet, appearance="blush false", text="Нет, ха-ха!")
    call process_character (janet, appearance="blush false", text="У тебя есть преимущество!")

    call process_new_location (bg="bg beach_evening", dream=dream)

    call process_character (n, appearance="outfit swimsuit pose twohandfist face neutral blush false", text="Я обыграл тетю [janet.say_name]!")

    call process_character (janet, text="Я пыталась плыть так быстро, как могла.")
    call process_character (janet, text="Но я никак не могла тебя догнать!")

    call process_character (n, appearance="outfit swimsuit pose handfist face happy blush false", text="Я поймал несколько волн, чтобы добраться быстрее!")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Loop.ogg", fadein = 1.0)

    call process_character (janet, appearance="outfit nude pose handhips face neutral blush false")
    pause 1.0

    call process_character (n, appearance="pose handfist face embarrassed blush false", text="...")
    call process_character (n, appearance="pose handfist face embarrassed blush false", text="Т-тётя [janet.say_name]?!")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="Где твой купальник?!")
    call process_character (janet, appearance="pose handface face neutral blush false", text="О, он меня здесь.")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Я сняла его, когда купалась.")
    call process_character (n, appearance="pose handsdown face embarrassed blush false", text="С-сняла его?!")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Я просто хотела искупаться нагишом.")
    call process_character (janet, appearance="pose handchest face happy blush false", text="Никто не увидит меня в любом случае, кроме тебя!")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="...{p}...")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Боишься, что тебя поймают?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Н-Нет...")
    call process_character (janet, appearance="pose handface face happy blush false", text="Ты все еще не привык видеть свою тетю голой?")
    call process_character (n, appearance="outfit swimsuit_hard pose handsdown face curious blush false", text="...")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Просто представь, что я неизвестная девушка.")
    call process_character (janet, appearance="pose handhips face happy blush false", text="Ты всегда можешь прикрыть глаза, если хочешь!")
    call process_character (n, appearance="outfit swimsuit_hard pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit swimsuit_hard pose behindhead face concerned blush false", text="Почему я должен это делать?")
    call process_character (janet, appearance="pose handface face flirt blush false", text="Это был риторический вопрос, [n.say_name]?")
    call process_character (n, appearance="outfit swimsuit_hard pose behindhead face curious blush true", text="...{p}...")
    call process_character (janet, appearance="pose handface face embarrassed blush false", text="Вуу! Ветерок дует, становится холодновато!")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Давай вернемся назад.")
    call process_character (janet, appearance="pose handchest face happy blush false", text="Я могу пойти выпить горячего чая!")

    python:
        janet.revistable_scenes.add("janet_scene_naked_revisit")
        if not dream:
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_seen_breasts", 1)
            stats.add_stat("times_seen_vagina", 1)

    call process_end_of_scene ("janet_scene_naked", char=janet, dream=dream)

    return

label janet_scene_blowjob(dream=False):
    $ display_multiple_characters([ (n, ""), (janet, "pose handhips face neutral blush false") ])

    call process_character (janet, appearance="pose handhips face neutral blush false", text="Эй [n.say_name]...")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Хочешь еще одну фотосессию?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ох?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Я сделаю ещё фотографии тети [janet.say_name]?")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Вообще-то, это я буду фотографировать.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Ты?")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Да.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Тогда что ты будешь фотографировать?")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Вообще-то, я хотела тебя сфотографировать.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Меня?")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Почему?")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Я никогда не фотографировала мужчин.")
    call process_character (janet, appearance="pose handhips face happy blush false", text="И я подумала, что мой племянник будет идеальным способом заполнить пробел!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Нужно ли мне делать что-то особенное?")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Ничего особенного.")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Однако...")
    call process_character (janet, appearance="pose handface face neutral blush false", text="В какой-то момент тебе придется раздеться.")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="Р-раздеться?!")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Важно для изучения фотографирования тела, чтобы субъект был голым.")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Я много раз снималась для изучения фигур.")

    call process_character (n, appearance="pose handpocket face concerned blush false")

    call process_character (janet, appearance="pose handchest face neutral blush false", text="Но никогда с молодым мужчиной в качестве модели.")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Они обычно слишком нервничают!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="(Я буду голым перед тетей [janet.say_name]?)")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Думаешь, у тебя получится?")
    call process_character (janet, appearance="pose handface face happy blush false", text="Я буду рада, если ты согласишься!")

    call prompt_menu_boldness_check ("Д-да, Я могу тебе помочь.", "Я-я не знаю, смогу ли я сделать это прямо сейчас...", "janet_scene_blowjob", janet)
    return

label janet_scene_blowjob_refusal(text, insufficient_points):
    if insufficient_points:
        call process_character (n, appearance="pose behindhead face concerned", text=text)
        call process_character (n, appearance="pose handpocket face curious", text="(Я не чувствую себя достаточно {b}уверенным{/b} для этого)")
        call process_character (n, appearance="pose handpocket face curious", text="(Я буду так нервничать, будучи голым перед моей тетей, пока она фотографирует...)")
        call process_character (n, appearance="pose handpocket face curious blush true", text="(Что, если она будет фотографировать мой пенис в увеличении?)")

    call process_character (janet, appearance="pose handhips face sad blush false", text="Черт.")
    call process_character (janet, appearance="pose handhips face sad blush false", text="Я с нетерпением жду нашей встречи.")
    call process_character (janet, appearance="pose handface face concerned blush false", text="Я надеюсь, что ты передумаешь, [n.say_name]!")

    call prompt_refusal_end (janet)
    return

label janet_scene_blowjob_sex(dream=False):
    call process_scene_beginning (bg=janet_house, char_tuple_array=[ (n, "outfit clothesjacket pose handpocket"), (janet, "outfit clothes pose handchest face happy blush false") ], dream=dream )

    call process_character (janet, appearance="pose handchest face happy blush false", text="Это будет просто бомба, [n.say_name]!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Я надеюсь, что так...")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Можешь раздеться до нижнего белья?")

    call character_leave_dissolve (n)
    pause 0.5
    call process_character (n, appearance="outfit underwear pose handsdown face curious blush false", text="...")

    call process_character (janet, appearance="pose handhips face happy blush false", text="Отлично!")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Позволь мне сделать несколько предварительных снимков...")

    "{i}Клик{/i}{p}{i}Клик{/i}{p}{i}Клик{/i}"

    call process_character (janet, appearance="pose handchest face neutral blush false", text="Да, они выходят хорошими.")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Уровень экспозиции там, где я хочу.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Ну, я думаю, мы можем двигаться дальше...")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Сними свое нижнее белье.")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="...")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="Х-хорошо.")

    call character_leave_dissolve (n)
    pause 0.5
    call process_character (n, appearance="outfit nudesoft pose handsdown face concerned blush false")
    pause 0.25

    call process_character (janet, appearance="pose handchest face neutral blush false", text="Мм...")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Ммм...")

    "{i}Клик-Клик{/i}"
    "{i}Клик{/i}"

    call process_character (janet, appearance="pose handchest face flirt blush false", text="Мило, мило...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Что мило?")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Смотрю на тебя сейчас...")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Я поняла, что недооценила твою худобу.")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="У тебя действительно красивое тело.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="У меня...{w=1.0}приятное тело?")
    call process_character (janet, appearance="pose handface face happy blush false", text="Очень фотогеничное!")

    "{i}Клик{/i}"
    "{i}Клик-Клик{/i}"

    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="pose handsdown face curious blush false", text="(Она часто направляет фотоаппарат вниз...)")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="...")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="(Его пенис имеет замечательный вид)")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="(Хорошая форма и гладкость...)")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="...")
    call process_character (janet, appearance="pose handface face neutral blush false", text="(Я хотела бы увидеть, как он выглядит, когда...)")
    call process_character (janet, appearance="pose handface face neutral blush false", text="...")
    call process_character (janet, appearance="pose handface face neutral blush false", text="У меня есть особая просьба к тебе, [n.say_name].")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Да?")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Не мог бы ты...")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Сделать свой пенис твёрдым?")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="!")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="Ты хочешь, чтобы мой пенис был твердым?")
    call process_character (janet, appearance="pose handchest face flirt blush false", text="Да, с удовольствием посмотрю.")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="...")
    call process_character (janet, appearance="pose handchest face embarrassed blush false", text="Я хотела бы увидеть его, чтобы сфотографировать.")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Это важно для исследования фигур.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Я не знаю, сможет ли он встать в этой ситуации...")
    call process_character (janet, appearance="pose handface face curious blush false", text="Хм...")
    call process_character (janet, appearance="pose handface face curious blush false", text="...")
    call process_character (janet, appearance="pose handface face flirt blush false", text="Как насчет такого варианта?")

    call character_leave_dissolve (janet)
    pause 0.5
    call process_character (janet, appearance="outfit underwear pose handhip face neutral blush false", text="Это поможет?")

    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face aroused blush false", text="...")
    call process_character (janet, appearance="outfit underwear pose handhip face happy blush false", text="(О, что-то происходит!)")

    call process_character (n, appearance="outfit nudehard pose twohandfist face flirty blush true", show_bust=False)
    $ refresh_character(n, force_transition = Dissolve(1.5))

    call process_character (janet, appearance="outfit underwear pose handface face neutral blush false", text="Ты!")
    call process_character (janet, appearance="outfit underwear pose handface face neutral blush false", text="Я подумала, что это сработает!")
    call process_character (n, appearance="outfit nudehard pose handsdown face concerned blush false", text="...")

    "{i}Клик{/i}"
    "{i}Клик-Клик{/i}"

    call process_character (janet, appearance="outfit underwear pose handchest face neutral blush false", text="Твой пенис красивый, [n.say_name].")
    call process_character (n, appearance="outfit nudehard pose behindhead face curious blush false", text="Ты так думаешь?")
    call process_character (janet, appearance="outfit underwear pose handchest face happy blush false", text="Это один из лучших, которые я видела!")
    call process_character (n, appearance="outfit nudehard pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="outfit nudehard pose behindhead face curious blush false", text="Э-это хорошо...")
    call process_character (janet, appearance="outfit underwear pose handface face neutral blush false", text="...{p}...")
    call process_character (janet, appearance="outfit underwear pose handface face neutral blush false", text="Я должна признаться, [n.say_name].")
    call process_character (n, appearance="outfit nudehard pose handsdown face neutral blush false", text="В чем?")
    call process_character (janet, appearance="outfit underwear pose handhips face neutral blush false", text="Покаты проводил со мной все лето...")
    call process_character (janet, appearance="outfit underwear pose handhips face neutral blush false", text="Я никогда не думала, сколько у нас общих интересов.")
    call process_character (janet, appearance="outfit underwear pose handhips face neutral blush false", text="Кроме того, ты помог мне, когда я в этом нуждалась.")
    call process_character (janet, appearance="outfit underwear pose handchest face neutral blush false", text="Но ты также находишь время, чтобы расслабиться на пляже со мной.")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="...")
    call process_character (janet, appearance="outfit underwear pose handface face neutral blush false", text="Ты первый парень, с которым мне действительно нравится проводить время.")
    call process_character (janet, appearance="outfit underwear pose handface face neutral blush false", text="Несмотря на то, что ты молод, у тебя лучшие качества, чем у большинства мужчин.")
    call process_character (janet, appearance="outfit underwear pose handface face flirt blush false", text="Я действительно чувствую...")
    call process_character (janet, appearance="outfit underwear pose handface face flirt blush false", text="Меня влечёт к тебе, [n.say_name].")
    call process_character (n, appearance="outfit nudehard pose behindhead face concerned blush false", text="В-влечёт ко мне?")


    call character_leave_dissolve (janet)
    pause 0.5
    call process_character (janet, appearance="outfit underwear pose handface face flirt blush false position janet_special", show_bust=False)
    $ refresh_character(janet, force_transition = Dissolve(1.0))
    pause 0.5

    call process_character (n, appearance="outfit nudehard pose behindhead face embarrassed blush false", text="Т-тётя [janet.say_name]?!")
    call process_character (n, appearance="outfit nudehard pose behindhead face embarrassed blush false", text="Ты очень близко!")
    call process_character (janet, appearance="outfit underwear pose handhips face flirt blush false", text="Ты идеально подходишь мне, [n.say_name]...")
    call process_character (janet, appearance="outfit underwear pose handhips face flirt blush false", text="...{p}...")
    call process_character (janet, appearance="outfit underwear pose handhips face flirt blush false", text="(Я так сильно хочу попробовать его член...)")
    call process_character (janet, appearance="outfit underwear pose handhips face flirt blush false", text="...")
    call process_character (janet, appearance="outfit underwear pose handface face embarrassed blush false", text="(Но он же мой племянник!)")
    call process_character (janet, appearance="outfit underwear pose handface face embarrassed blush false", text="(Это должно быть неправильно думать об этом...)")
    call process_character (janet, appearance="outfit underwear pose handface face embarrassed blush false", text="...")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="(Тем не менее, все говорит мне, что это правильно...)")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="(Я хочу сделать вот что...)")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Тетя [janet.say_name]?")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Ты в порядке?")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Suave Standpipe.ogg", fadein = 1.0)

    call static_still_ctc ("bg janet_tip_lick")

    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Т-тетя [janet.say_name]!")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Ах, твой член такой свежий на вкус!")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Я думал, мы будем фотографировать?")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Мы решили отдохнуть от этого.")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Это хорошая точка зрения, согласись?")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Ох...")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Д-Да...")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Читаешь мои мысли.")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="...")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Мне нравится твоя крайняя плоть!")

    call static_still_ctc ("bg janet_foreskin_pull")

    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Мммм!")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Это уникальное ощущение.")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Аах!")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="У тебя очень чувствительная крайняя плоть.")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="У меня было предчувствие, что так и будет.")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="...")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="(Это напоминает мне о прошлом!)")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="(У моего первого парня была крайнюю плоть на его члене)")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="(Н у него не было столько, сколько у [n.say_name])")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Мм!")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Ты наслаждаешься таким опытом, [n.say_name]?")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Я наслаждаюсь им, ах!")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="У тебя когда-нибудь был подобный опыт?")

    if stats.stat_value('times_received_blowjob') > 0:
        call process_character (n, appearance="blush false", text="Я… Да.")
        call process_character (janet, appearance="blush false", text="Правда?")
        call process_character (janet, appearance="blush false", text="Уже был опыт под животом?")
        call process_character (janet, appearance="blush false", text="Ты должно быть дурачишь меня...")
    else:
        call process_character (n, appearance="blush false", text="Я-Я не делал ничего подобного раньше...")
        call process_character (janet, appearance="blush false", text="Меня это не удивляет.")
        call process_character (janet, appearance="blush false", text="Я и не ожидала, что ты много об этом знаешь.")
        call process_character (janet, appearance="blush false", text="Но узнаешь, хотя...")

    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="{i}Вздох.{/i}.")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Нн!")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Хочешь узнать, что я могу сделать своим ртом?")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Ч-Что?")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Я могу заставить твой член исчезнуть, засунув мне в глотку.")

    if "vicky_scene_blowjob" in scenes_completed or "simone_scene_blowjob" in scenes_completed or "julia_scene_blowjob" in scenes_completed or "gloryhole_scene_blowjob" in scenes_completed or "kira_scene_stealth_bj" in scenes_completed:
        call process_character (n, appearance="blush false", text="Мне кажется, это делали со мной раньше...")
        call process_character (janet, appearance="blush false", text="Мм, я так не думаю.")
        call process_character (janet, appearance="blush false", text="Не так, как я.")
        call process_character (n, appearance="blush false", text="И в чём разница?")
        call process_character (janet, appearance="blush false", text="Скажи мне через минуту...")
    else:
        call process_character (n, appearance="blush false", text="Т-ты можешь?")
        call process_character (janet, appearance="blush false", text="Я пробовала это давно...")
        call process_character (janet, appearance="blush false", text="Но я уверена, что у меня все получится.")
        call process_character (n, appearance="blush false", text="На что это будет похоже?")
        call process_character (janet, appearance="blush false", text="Ты узнаешь об этом прямо сейчас...")

    call static_still_ctc ("bg janet_deepthroat")

    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Аах!")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Ммф!")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Мм! Мм!")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Ха, ах!")

    if "vicky_scene_blowjob" in scenes_completed or "simone_scene_blowjob" in scenes_completed or "julia_scene_blowjob" in scenes_completed or "gloryhole_scene_blowjob" in scenes_completed or "kira_scene_stealth_bj" in scenes_completed:
        call process_character (n, appearance="blush false", text="([janet.say_name[0]]-[janet.say_name] была права!)")
        call process_character (n, appearance="blush false", text="(Это намного отличается от того, что я было раньше!)")
        call process_character (n, appearance="blush false", text="(Ее лицо прямо напротив меня!)")
    else:
        call process_character (n, appearance="blush false", text="([janet.say_name] не шутила!)")
        call process_character (n, appearance="blush false", text="(Весь мой пенис у нее во рту!)")
        call process_character (n, appearance="blush false", text="(И ее лицо прижимается ко мне!)")


    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="...")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="(У меня все еще могу это!)")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="(Я даже могу обернуть свой язык вокруг его шаров!)")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Ммм...")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="([n.say_name] проникся этом!)")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="(Он хватается за мою голову и пытается удержать меня на своем члене!)")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="{i}Вздох,{/i} {i}вздох.{/i}")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Чувствую себя...{w=0.5}так...{w=0.5}хорошо…")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Ммф...")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Есть много способов, которыми я могу заставить тебя чувствовать себя хорошо [n.say_name].")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Ты заслуживаешь ублажения!")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Э-это здорово, что ты делаешь, тетя [janet.say_name]!")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="...")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="(Это влечение к моему племяннику сильнее, чем любые другие отношения, которые у меня были)")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="(Я пока не могу полностью это понять...)")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="...")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="(Но не важно думать об этом прямо сейчас...)")
    call process_character (n, appearance="outfit nudehard pose handsdown face curious blush false", text="Ох, ох!")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Я не хочу, чтобы тебе пришлось стоять все время.")
    call process_character (janet, appearance="outfit underwear pose handchest face flirt blush false", text="Почему бы тебе не присесть?")

    call static_still_ctc ("bg janet_blowjob_tip_panties_natearouse")

    call process_character (janet, appearance="blush false", text="Здесь!")
    call process_character (janet, appearance="blush false", text="Теперь ты можешь расслабиться.")
    call process_character (n, appearance="blush false", text="Ммм!")
    call process_character (n, appearance="blush false", text="Ч-что ты делаешь?")
    call process_character (janet, appearance="blush false", text="Ох?")
    call process_character (janet, appearance="blush false", text="Ты имеешь в виду, как я натираю твои яйца?")
    call process_character (n, appearance="blush false", text="Д-Да...")
    call process_character (janet, appearance="blush false", text="Я не хочу их игнорировать!")
    call process_character (janet, appearance="blush false", text="Им тоже нужно внимание.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Это похоже массаж яиц)")

    call static_still_ctc ("bg janet_blowjob_panties_nateorgasm_nocum")

    call process_character (n, appearance="blush false", text="Хмм!")
    call process_character (janet, appearance="blush false", text="Я буду продолжать, пока ты не финишируешь.")
    call process_character (n, appearance="blush false", text="Пока я не финиширую?")
    call process_character (janet, appearance="blush false", text="Это будет, когда ты кончишь.")
    call process_character (janet, appearance="blush false", text="Я не собираюсь чтобы яйца у племянника стали голубые!")
    call process_character (n, appearance="blush false", text="А, я…")
    call process_character (janet, appearance="blush false", text="Твои яйца пульсируют в моей руке!")
    call process_character (n, appearance="blush false", text="Ахх, ооох...")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg janet_blowjob_panties_NateOrgasm_cum")

    call process_character (n, appearance="blush false", text="Гьяях!")
    call process_character (janet, appearance="blush false", text="Мм...")
    call process_character (janet, appearance="blush false", text="Мм!")
    call process_character (janet, appearance="blush false", text="(Его сперма...)")
    call process_character (janet, appearance="blush false", text="(Он имеет мощный вкус!)")

    call static_still_ctc ("bg janet_blowjob_panties_NateOrgasm_aftercum")

    call process_character (n, appearance="blush false", text="Ааах...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="{i}Фьюю.{/i}.")
    call process_character (janet, appearance="blush false", text="Ох...")

    call static_still_ctc ("bg janet_blowjob_tip_panties_NateAroused_cum")

    call process_character (janet, appearance="blush false", text="Жаль, что я не смогла сфотографировать твой оргазм [n.say_name].")
    call process_character (janet, appearance="blush false", text="Может быть, когда-нибудь я засниму одну из твоих эякуляций.")
    call process_character (janet, appearance="blush false", text="Это будет непросто сделать.")
    call process_character (janet, appearance="blush false", text="Я должна предвидеть это.")
    call process_character (n, appearance="blush false", text="Д-Да...")
    call process_character (janet, appearance="blush false", text="Теперь, [n.say_name]...")
    call process_character (janet, appearance="blush false", text="Я не хочу, чтобы твоя мама узнала об этом.")
    call process_character (janet, appearance="blush false", text="Ты ведь не рассказал ей о наших фотосессиях?")
    call process_character (n, appearance="blush false", text="Нисколько.")
    call process_character (janet, appearance="blush false", text="Пожалуйста, сделай все возможное, чтобы так и оставалось.")
    call process_character (janet, appearance="blush false", text="Если она когда-нибудь узнает...")
    call process_character (janet, appearance="blush false", text="Она больше не позволит тебе сюда приходить.")
    call process_character (n, appearance="blush false", text="Нет!")
    call process_character (n, appearance="blush false", text="Я не хочу, чтобы это случилось, тетя [janet.say_name]!")
    call process_character (janet, appearance="blush false", text="Я тоже!")
    call process_character (janet, appearance="blush false", text="Просто держи язык за зубами, и все будет хорошо.")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="Я хочу посмотреть фильм.")
    call process_character (janet, appearance="blush false", text="Есть предложения?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Дай мне подумать об этом...")

    python:
        janet.revistable_scenes.add("janet_scene_blowjob_revisit")
        if not dream:
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_ejaculated", 1)
            stats.add_stat("times_cummed_in_mouth", 1)
            stats.add_stat("times_received_blowjob", 1)

    call process_end_of_scene ("janet_scene_blowjob", char=janet, dream=dream)

    return

label janet_scene_blowjob_revisit:
    $ no_bust_art = False

    if "janet_scene_blowjob_revisit" in scenes_completed:
        call janet_scene_blowjob_revisit_2nd_time
    else:
        call janet_scene_blowjob_revisit_1st_time

    return

label janet_scene_blowjob_revisit_1st_time:
    call process_scene_beginning (bg=janet_house, char_tuple_array=[ (janet, "pose handface face curious blush false"), (n, "pose handpocket face neutral") ] )

    call process_character (janet, appearance="pose handface face curious blush false", text="Вроде он назывался фелляция, или минет, [n.say_name]?")

    if heard_of_blowjob:
        call process_character (n, appearance="pose behindhead face curious blush false", text="О да, я забыл...")
        call process_character (janet, appearance="pose handface face neutral blush false", text="Я знаю, что ты имел в виду.")
    else:
        call process_character (n, appearance="pose handpocket face curious blush false", text="Это?")
        call process_character (n, appearance="pose handpocket face curious blush false", text="Я ничего такого не знал.")
        call process_character (janet, appearance="pose handface face neutral blush false", text="Проще свести все к одному слову.")

    $ heard_of_blowjob = True


    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="...")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Я знаю, когда в последний раз я была в нижнем белье.")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Но тебе бы понравилось, если бы я сделала это без одежды?")

    menu:
        "Мне бы этого очень хотелось!":
            call process_character (n, appearance="pose handfist face happy blush false")
            call process_character (janet, appearance="pose handchest face flirt blush false", text="Тебе понравится, для большей стимуляции!")

            call character_leave_dissolve (janet)
            pause 0.5

            python hide:
                play_music("audio/music/Suave Standpipe.ogg", fadeout=1.0, fadein = 1.0)

            call process_character (janet, appearance="outfit nude")
            pause 1.5
        "Мы должны сфотографироваться голыми вместе!":

            call add_boldness (1, tag="janet_scene_blowjob_revisit_take_photos")

            call process_character (n, appearance="pose twohandfist face happy blush false")
            call process_character (janet, appearance="pose handchest face happy blush false", text="Честное слово, [n.say_name]!")
            call process_character (janet, appearance="pose handface face neutral blush false", text="Я не согласна с этой идеей...")
            call process_character (janet, appearance="pose handface face flirt blush false", text="Но эти фотографии должны попасть в мою частную коллекцию!")

            call character_leave_dissolve (janet)
            pause 0.5

            python hide:
                play_music("audio/music/Suave Standpipe.ogg", fadeout=1.0, fadein = 1.0)

            call process_character (janet, appearance="outfit nude")
            pause 1.5

    call static_still_ctc ("bg janet_tip_lick")

    call process_character (janet, appearance="pose handhips face flirt blush false", text="Твой член так быстро реагирует, [n.say_name]!")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Только легкое касание и он отвечает!")
    call process_character (n, appearance="blush false", text="Я ... Я чувствую там внизу...")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Так и положено!")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Знаешь, на этой части тела тысячи нервных окончаний.")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Вот почему ты чувствуешь это так сильно!")
    call process_character (n, appearance="blush false", text="В этом есть какой-то смысл.")

    call static_still_ctc ("bg janet_nude_foreskin_pull")

    call process_character (janet, appearance="blush false", text="И когда я этим занимаюсь...")
    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (janet, appearance="blush false", text="Смотри!")
    call process_character (janet, appearance="blush false", text="Уже выходит твоё предсемя.")
    call process_character (janet, appearance="blush false", text="Это верный знак, что сигналы удовольствия доходят!")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}.")
    call process_character (n, appearance="blush false", text="И он стаёт ещё больше, когда ты сосешь у меня?")
    call process_character (janet, appearance="blush false", text="Да!")

    call static_still_ctc ("bg janet_nude_deepthroat")

    call process_character (n, appearance="blush false", text="Аах!")
    call process_character (n, appearance="blush false", text="Да!")
    call process_character (janet, appearance="blush false", text="Мм. Ммм. Мм.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Как она это делает?)")
    call process_character (n, appearance="blush false", text="(Я удивлен, что она не задыхается!)")
    call process_character (janet, appearance="blush false", text="(Я даже не могу вспомнить, как я обнаружила эту способность)")
    call process_character (janet, appearance="blush false", text="(Я думаю, что впервые узнала, когда осмелилась засунуть банан в горло)")
    call process_character (janet, appearance="blush false", text="(Ха, когда я оглядываюсь на это сейчас...)")
    call process_character (janet, appearance="blush false", text="(Я понятия не имела, что это может быть сексуальным)")
    call process_character (n, appearance="blush false", text="Ох, ах!")
    call process_character (janet, appearance="blush false", text="Ах...")
    call process_character (janet, appearance="blush false", text="Я хотела бы продолжать делать заглот, [n.say_name].")
    call process_character (janet, appearance="blush false", text="Тем не менее, если ты кончишь в середине, то это не будет весело для меня.")
    call process_character (janet, appearance="blush false", text="Поэтому нам нужно немного изменить наши позиции...")

    call static_still_ctc ("bg janet_blowjob_tip_nude_NateArouse")

    call process_character (janet, appearance="blush false", text="Теперь я могу продолжить...")
    call process_character (n, appearance="blush false", text="Ммм, ахх...")
    call process_character (n, appearance="blush false", text="Пожалуйста, потри мои яйца, тетя [janet.say_name]!")
    call process_character (janet, appearance="blush false", text="Я же говорила, что стоит обратить на них внимание!")
    call process_character (janet, appearance="blush false", text="Они обильно вознаградят тебя!")
    call process_character (janet, appearance="blush false", text="(И в них есть много спермы в резерве...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Это круто, как мы можем сделать это прямо в гостиной)")
    call process_character (n, appearance="blush false", text="(Надеюсь, никто не планирует прийти, пока мы это делаем...)")
    call process_character (janet, appearance="blush false", text="(Его яйца полные...)")
    call process_character (janet, appearance="blush false", text="(Может быть, даже больше, чем раньше!)")
    call process_character (janet, appearance="blush false", text="(Может быть, все эти ласки переключили производство спермы на повышенные обороты!)")

    call static_still_ctc ("bg janet_blowjob_nude_NateArouse")

    call process_character (n, appearance="blush false", text="Ах!")
    call process_character (n, appearance="blush false", text="(Сосёт и натирает мои яйца...)")
    call process_character (n, appearance="blush false", text="(Это удваивает мое возбуждение!)")
    call process_character (n, appearance="blush false", text="Т-тетя [janet.say_name]...")
    call process_character (n, appearance="blush false", text="Ха! Ах!")
    call process_character (n, appearance="blush false", text="Я кончаю, я кончаю!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg janet_blowjob_nude_NateOrgasm_cum")

    call process_character (n, appearance="blush false", text="Хффмм! Ааоох!")
    call process_character (janet, appearance="blush false", text="(Он толкает нижнюю часть своего тела!)")
    call process_character (janet, appearance="blush false", text="(Это, должно быть, был хороший оргазм)")

    call static_still_ctc ("bg janet_blowjob_tip_nude_NateAroused_cum")

    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (janet, appearance="blush false", text="Ты так кричал во время семяизвержения!")
    call process_character (janet, appearance="blush false", text="Хорошо, что окна были закрыты!")
    call process_character (n, appearance="blush false", text="Мне просто нужно было закричать.")
    call process_character (n, appearance="blush false", text="То, как ты терлась и сосала, было...")
    call process_character (janet, appearance="blush false", text="Я нанесла двойной удар!")

    call janet_scene_blowjob_revisit_end

    return

label janet_scene_blowjob_revisit_2nd_time:
    python hide:
        play_music("audio/music/Suave Standpipe.ogg", fadeout=1.0, fadein = 1.0)

    call process_scene_beginning (bg="bg janet_nude_foreskin_pull")
    $ no_bust_art = True
    pause

    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Он знаком со позой бура)")
    call process_character (janet, appearance="blush false", text="(Это не заняло много времени...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Тете [janet.say_name] очень нравится кожа на моем пенисе)")
    call process_character (n, appearance="blush false", text="(Она хочет играть с ней каждый раз, когда мы делаем это...)")
    call process_character (janet, appearance="blush false", text="Ммм...")
    call process_character (janet, appearance="blush false", text="(Мой племянник всегда готов получить минет)")
    call process_character (janet, appearance="blush false", text="(Без сомнения, я ему нравлюсь...)")

    call static_still_ctc ("bg janet_nude_deepthroat")

    call process_character (janet, appearance="blush false", text="Ммф!")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Интересно, знает ли он о том, как моя дикая сестра и я вернулись в тот день...)")
    call process_character (janet, appearance="blush false", text="(Будет ли это иметь для него значение?)")
    call process_character (janet, appearance="blush false", text="([n.say_name] нравится жить одним моментом)")
    call process_character (janet, appearance="blush false", text="(Еще одна причина, почему он так обращается со мной!)")
    call process_character (n, appearance="blush false", text="Ох...")
    call process_character (n, appearance="blush false", text="(Прежде чем я начал посещать свою тетю этим летом...)")
    call process_character (n, appearance="blush false", text="(Я никогда не замечал, насколько она была красива)")
    call process_character (n, appearance="blush false", text="(Интересно, почему я никогда не замечал этого до недавнего времени?)")
    call process_character (n, appearance="blush false", text="Ахх!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Может быть, это было потому, что я увидел ее полностью обнаженной...)")

    call static_still_ctc ("bg janet_blowjob_tip_nude_NateArouse")

    call process_character (janet, appearance="blush false", text="([julia.say_name] в конце концов вернется сюда в конце лета)")
    call process_character (janet, appearance="blush false", text="(Как мне с этим справиться?)")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Мне придется планировать эти вещи с [n.say_name] более умно, я думаю)")
    call process_character (janet, appearance="blush false", text="(Особенно с тем, насколько подозрительной может быть моя дочь...)")

    call static_still_ctc ("bg janet_blowjob_nude_NateArouse")

    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я надеюсь, что в этом году в школе не будет слишком много экзаменов)")
    call process_character (n, appearance="blush false", text="(Я хотел бы посещать тетю [janet.say_name] часто!)")
    call process_character (n, appearance="blush false", text="Мм!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Возможно, я смогу учиться с [julia.say_name] и ночевать здесь...)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", xalign = 0.5, yalign = 0.1)
    $ quick_menu = True

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg janet_blowjob_nude_NateOrgasm_cum")

    call process_character (n, appearance="blush false", text="Ахххх!")
    call process_character (janet, appearance="blush false", text="...")

    call static_still_ctc ("bg janet_blowjob_nude_NateOrgasm_aftercum")

    call process_character (janet, appearance="blush false", text="(Я ещё не видела, чтобы он мало кончал...)")
    call process_character (janet, appearance="blush false", text="(И не думаю, что увижу в ближайшее время!)")

    call janet_scene_blowjob_revisit_end

    return

label janet_scene_blowjob_revisit_end:

    python:
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_ejaculated", 1)
        stats.add_stat("times_cummed_in_mouth", 1)
        stats.add_stat("times_received_blowjob", 1)

    call process_end_of_scene ("janet_scene_blowjob_revisit", char=janet, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label janet_scene_vaginal(dream=False):
    call process_scene_beginning (bg="bg janet_house_daytime", dream=dream )
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="Тетя [janet.say_name], это я [n.say_name]!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face happy blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Тетя [janet.say_name]?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Хм...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="...")
    call process_character (janet, appearance="outfit nude pose handhips face happy blush false", text="Я слышу тебя, [n.say_name]!")
    call process_character (janet, appearance="outfit nude pose handhips face neutral blush false", text="Я медитировала на заднем дворе.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face concerned blush false", text="Ты была голой снаружи?")
    call process_character (janet, appearance="outfit nude pose handface face neutral blush false", text="Да, с самого утра.")
    call process_character (janet, appearance="outfit nude pose handface face happy blush false", text="Я почти забыла, что была голой!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Так ты сегодня вообще не одевалась?")
    call process_character (janet, appearance="outfit nude pose handface face happy blush false", text="Точно!")
    call process_character (janet, appearance="outfit nude pose handchest face neutral blush false", text="У меня просто было внезапное желание не одеваться, когда я проснулась.")
    call process_character (janet, appearance="outfit nude pose handchest face neutral blush false", text="Я нахожу это очень расслабляющим.")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Да?")
    call process_character (janet, appearance="outfit nude pose handhips face neutral blush false", text="Я часто не носила одежду, когда была моложе.")
    call process_character (janet, appearance="outfit nude pose handhips face neutral blush false", text="Твоя мама кричала на меня, но я чувствовала себя комфортно.")
    call process_character (janet, appearance="outfit nude pose handhips face neutral blush false", text="Какое-то время я даже думала о присоединении к нудистской колонии!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Нудистская колония?")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious blush false", text="Ты имеешь в виду...{w=1.0}вокруг одни голые люди?")
    call process_character (janet, appearance="outfit nude pose handhips face happy blush false", text="В основном да!")
    call process_character (janet, appearance="outfit nude pose handhips face happy blush false", text="Ты живёшь своей повседневной жизни, без одежды!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Да...")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face curious blush false", text="Интересно.")
    call process_character (janet, appearance="outfit nude pose handface face neutral blush false", text="Почему бы тебе не попробовать, [n.say_name]?")
    call process_character (janet, appearance="outfit nude pose handface face neutral blush false", text="Я думаю, тебе это очень понравится!")
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral blush false", text="Мне?")
    call process_character (janet, appearance="outfit nude pose handface face happy blush false", text="Да!")
    call process_character (janet, appearance="outfit nude pose handface face happy blush false", text="Сегодня мы проведем такой день вместе!")
    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="...")

    call prompt_menu_boldness_check ("Все в порядке! Я готов к этому!", "М-может быть, в другой раз...", "janet_scene_vaginal", janet)
    return

label janet_scene_vaginal_refusal(text, insufficient_points):
    if insufficient_points:
        call process_character (n, appearance="pose behindhead face curious", text=text)
        call process_character (n, appearance="pose handpocket face curious", text="(Было бы странно ходить голым весь день)")
        call process_character (n, appearance="pose handpocket face curious blush true", text="(Мой член будет постоянно шлепаться?)")
    else:
        call process_character (n, appearance="pose behindhead face curious")

    call process_character (janet, appearance="pose handhips face concerned blush false", text="О, тебе не нравится, [n.say_name].")
    call process_character (janet, appearance="pose handhips face concerned blush false", text="Ты нервничаешь, что кто-то может увидеть?")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Мой задний двор очень уединенный!")

    call prompt_refusal_end (janet)
    return

label janet_scene_vaginal_sex(dream=False):
    if current_background != "bg janet_house_daytime":
        call process_scene_beginning (bg="bg janet_house_daytime", dream=dream )

    $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket"), (janet, "outfit nude pose handchest face happy blush false") ])

    call process_character (janet, appearance="outfit nude pose handchest face happy blush false", text="Вот, это племянник, которого я знаю!")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (n, appearance="outfit nudesoft")
    pause 0.5

    call process_character (n, appearance="outfit nudesoft pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose handsdown face neutral blush false", text="Так что же нам теперь делать?")
    call process_character (janet, appearance="outfit nude pose handface face neutral blush false", text="Мы делаем...{w=1.0}всё, что обычно делаем.")
    call process_character (n, appearance="outfit nudesoft pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose behindhead face curious blush false", text="Единственная разница в том, что мы голые?")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Правильно!")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Хотя, я уверен, мы можем сделать несколько особенных вещей, хе-хе...")
    call process_character (n, appearance="outfit nudesoft pose behindhead face neutral blush false", text="Я...{w=1.0}хочу выйти на улицу вот так.")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Это замечательный опыт!")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Я чувствую себя единой с природой и моим окружением, когда я голая.")
    call process_character (janet, appearance="pose handface face happy blush false", text="Я могу показать тебе, как медитировать, если хочешь!")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face happy blush false", text="Конечно!")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face happy blush false", text="Звучит весело!")

    call fade_to_black (1)

    "{i}Немного позже...{/i}"

    call process_new_location ("bg janet_house_daytime", dream=dream)

    $ display_multiple_characters([ (n, "outfit nudesoft pose handsdown face neutral blush false"), (janet, "outfit nude pose handchest face neutral blush false") ])
    call process_character (janet, appearance="outfit nude pose handchest face neutral blush false", text="Ты выглядишь расслабленным, [n.say_name]!")
    call process_character (janet, appearance="outfit nude pose handchest face neutral blush false", text="Я думаю ты отлично помедитировал.")
    call process_character (n, appearance="pose handfist face happy blush false", text="Да!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Я и не знал, как это легко медитировать!")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Разве это не замечательно?")
    call process_character (janet, appearance="pose handhips face happy blush false", text="Я чувствовал, что могу прикоснуться к ветру и услышать шелест листьев на ветру.")
    call process_character (n, appearance="pose handsdown face neutral blush false", text="Ты делаешь это каждый день, тетя [janet.say_name]?")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Я стараюсь!")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Что хорошего в медитации, так это то, что можно извлечь из нее пользу в любое время суток!")
    call process_character (n, appearance="pose behindhead face aroused blush false", text="Я почти заснул, пока я это делал.")
    call process_character (n, appearance="pose behindhead face aroused blush false", text="{i}Зевок.{/i}.")
    call process_character (janet, appearance="pose handchest face happy blush false", text="Ха, такое может случиться!")
    call process_character (janet, appearance="pose handchest face happy blush false", text="На самом деле, я иногда делаю это прямо перед сном, чтобы уснуть.")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Почему бы тебе не вздремнуть немного?")
    call process_character (n, appearance="pose handsdown face aroused blush false", text="{i}Зевок.{/i}.")
    call process_character (n, appearance="pose handsdown face aroused blush false", text="Это не плохая идея.")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Ты можешь отдохнуть прямо на этом диване.")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Это супер удобно!")
    call process_character (n, appearance="pose behindhead face aroused blush false", text="Звучит неплохо.")
    call process_character (n, appearance="pose behindhead face aroused blush false", text="Спасибо, тетя [janet.say_name]...")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Я буду в другой комнате, если понадоблюсь.")

    call fade_to_black (1)
    "{i}Ещё чуть позже...{/i}"
    $ no_bust_art = True

    call process_character (janet, appearance="outfit nude pose handface face curious blush false", text="...")
    call process_character (janet, appearance="outfit nude pose handface face curious blush false", text="([n.say_name] все еще спит?)")
    call process_character (n, text="{i}Хрр...{/i}")

    call process_character (janet, appearance="pose handface face happy blush false", text="(Да, ха-ха!)")
    call process_character (janet, appearance="pose handface face happy blush false", text="(Эта медитация действительно расслабила его)")
    call process_character (n, text="{i}Хрр...{/i}")
    call process_character (n, text="Мм, Ммф...")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="(Интересно, что ему снится?)")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="...{p}...")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="(О...)")
    call process_character (janet, appearance="pose handchest face happy blush false", text="(О!)")
    call process_character (janet, appearance="pose handchest face happy blush false", text="(Посмотрите на эту эрекцию!)")
    call process_character (janet, appearance="pose handchest face happy blush false", text="...")
    call process_character (janet, appearance="pose handface face flirt blush false", text="Хм...")
    call process_character (janet, appearance="pose handface face flirt blush false", text="(Грязная мысль пришла мне в голову)")
    call process_character (janet, appearance="pose handface face flirt blush false", text="...")
    call process_character (janet, appearance="pose handface face flirt blush false", text="(Я могла бы попробовать это...)")
    call process_character (janet, appearance="pose handface face flirt blush false", text="...")
    call process_character (janet, appearance="pose handchest face flirt blush false", text="([n.say_name] в идеальном положении!)")
    call process_character (janet, appearance="pose handchest face flirt blush false", text="...")
    call process_character (janet, appearance="pose handface face embarrassed blush false", text="(Нет пути назад, если я пойду на это!)")
    call process_character (janet, appearance="pose handface face embarrassed blush false", text="(Минет моему племяннику - это одно, но это...)")
    call process_character (janet, appearance="pose handface face embarrassed blush false", text="...{p}...")
    call process_character (janet, appearance="pose handchest face flirt blush false", text="(Его член продолжает дергаться)")
    call process_character (janet, appearance="pose handchest face flirt blush false", text="(Это сигнал мне к действию...)")
    call process_character (janet, appearance="pose handchest face flirt blush false", text="...")
    call process_character (janet, appearance="pose handface face flirt blush true", text="([n.say_name], слишком большой для твоей тети!)")

    call process_character (n, text="Хрр...")
    call process_character (n, text="...")
    call process_character (n, text="Ммм...")
    call process_character (n, text="...")
    call process_character (n, text="Х-хм?")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadein = 1.0)
    call static_still_ctc ("bg janet_vaginal_sideview")

    call process_character (janet, appearance="pose handface face flirt blush true", text="Я разбудила тебя [n.say_name]?")
    call process_character (n, appearance="blush false", text="!!")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Ох...")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Ты не против, если я немного покатаюсь на тебе?")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Я видела, что твой член твердый...")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Мне просто нужно было попробовать!")
    call process_character (n, appearance="blush false", text="Ммм! Ах!")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Тебе это нравится?")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Ты остаешься милым и твёрдым!")
    call process_character (n, appearance="blush false", text="Мне нравится, как ты прыгаешь вверх и вниз на мне, тетя [janet.say_name]!")
    call process_character (n, appearance="blush false", text="Я чувствую себя очень хорошо!")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Вот почему это называется скачками, хе-хе...")
    call process_character (janet, appearance="pose handface face flirt blush true", text="{i}Вздох!{/i}")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Твой член скользит во мне!")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Да, да!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Тетя [janet.say_name] прижала свои сиськи ко мне!!)")
    call process_character (janet, appearance="pose handface face flirt blush true", text="...")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Тебе нравится, как мои сиськи хлюпают по твоему телу [n.say_name]?")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Это заставляет их оттопыриваться и выглядеть больше, не так ли?")
    call process_character (n, appearance="blush false", text="Д-да.")
    call process_character (n, appearance="blush false", text="Они мягкие...")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Всё от природы, [n.say_name]!")
    call process_character (janet, appearance="pose handface face flirt blush true", text="И я знаю, как ими пользоваться!")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}.")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Мм, ах, ах...")
    call process_character (janet, appearance="pose handface face flirt blush true", text="...")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Это твой первый раз, когда ты трахаешься?")
    call process_character (janet, appearance="pose handface face flirt blush true", text="Кажется, ты знаешь, как это делать...")

    if stats.stat_value("times_had_vaginal_sex") > 0:
        call process_character (n, appearance="blush false", text="Я делал такое раньше...")
        call process_character (janet, appearance="blush false", text="Значит, ты уже был на всех базах?")
        call process_character (n, appearance="blush false", text="...")
        call process_character (janet, appearance="blush false", text="Даже если какая-нибудь девушка добралась до тебя раньше...")
        call process_character (janet, appearance="blush false", text="Бьюсь об заклад, она не смогла дать тебе полноценный опыт!")
        call process_character (n, appearance="blush false", text="Полноценный опыт?")
        call process_character (n, appearance="blush false", text="Эмм...")
        call process_character (janet, appearance="blush false", text="Просто подожди и увидишь!")
        call process_character (n, appearance="blush false", text="...")
    else:
        call process_character (n, appearance="blush false", text="Я никогда не делал ничего подобного!")
        call process_character (janet, appearance="blush false", text="Вот это сюрприз!")
        call process_character (janet, appearance="blush false", text="Большинство первых трахов никогда не длятся так долго!")
        call process_character (n, appearance="blush false", text="Что они?")
        call process_character (n, appearance="blush false", text="Мм!")
        call process_character (janet, appearance="blush false", text="Когда мужчина занимается сексом в первый раз, происходит одно из двух...")
        call process_character (janet, appearance="blush false", text="Либо он не может поднять его, потому что слишком нервничает...")
        call process_character (janet, appearance="blush false", text="Или он делает несколько толчков и кончает.")
        call process_character (janet, appearance="blush false", text="Говоря по опыту, так обычно бывает с девственниками.")
        call process_character (n, appearance="blush false", text="Итак, эм...")
        call process_character (n, appearance="blush false", text="Я не обычный девственник?")
        call process_character (janet, appearance="blush false", text="У тебя всё ещё твердый член, ха-ха!")
        call process_character (janet, appearance="blush false", text="И ты до сих пор не кончил.")
        call process_character (janet, appearance="blush false", text="Вот почему я изначально подумала, что ты был на всех базах неоднократно!")
        call process_character (n, appearance="blush false", text="...")
        call process_character (janet, appearance="blush false", text="(Итак, [n.say_name] теряет девственность со своей тетей...)")
        call process_character (janet, appearance="blush false", text="...")
        call process_character (janet, appearance="blush false", text="(Либо он никогда никому об этом не расскажет...) \n (Или он будет всем хвастаться!)")
        call process_character (n, appearance="blush false", text="Ах, ах!")

    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="Хочешь, чтобы я показала тебе, на что я действительно способна, [n.say_name]?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Что ты имеешь в виду, тетя [janet.say_name]?")
    call process_character (janet, appearance="blush false", text="Тебе любопытно?")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Д-Да.")

    call static_still_ctc ("bg janet_vaginal_behind_down")

    call process_character (janet, appearance="blush false", text="Возьми меня за руку.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Вот так?")
    call process_character (janet, appearance="blush false", text="Хорошо.")
    call process_character (janet, appearance="blush false", text="Теперь держись!")
    call process_character (n, appearance="blush false", text="{cps=40}Держаться за чт-{/cps}{w=0.75}{nw}")

    call static_still_ctc ("bg janet_vaginal_behind_up")

    call process_character (janet, appearance="blush false", text="За это!")

    call static_still_ctc ("bg janet_vaginal_behind_down")

    call process_character (n, appearance="blush false", text="Аах!")

    show bg janet_vaginal_behind_up
    with Dissolve(0.5)

    call process_character (janet, appearance="blush false", text="Ох, чёрт!")

    show bg janet_vaginal_behind_down
    with Dissolve(0.5)

    call process_character (janet, appearance="blush false", text="Ммм!")
    call process_character (n, appearance="blush false", text="Т-тетя [janet.say_name]!")
    call process_character (janet, appearance="blush false", text="Вот так я скачу на члене!")

    show bg janet_vaginal_behind_up
    with Dissolve(0.5)

    if stats.stat_value("times_had_vaginal_sex") > 0:
        call process_character (n, appearance="blush false", text="(Тпру...)")
        call process_character (n, appearance="blush false", text="(Тетя [janet.say_name] прямо падает на меня!)")
        call process_character (n, appearance="blush false", text="(Когда она это делает, я чувствую себя удивительно!)")

        show bg janet_vaginal_behind_down
        with Dissolve(0.5)

        call process_character (n, appearance="blush false", text="Мм!")
        call process_character (n, appearance="blush false", text="(Мой член становится все теплее и теплее!)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Я не был уверен, чего ожидать от тети [janet.say_name] сидящей на мне...)")
        call process_character (n, appearance="blush false", text="(Это не так, как я обычно делал раньше...)")

        show bg janet_vaginal_behind_up
        with Dissolve(0.5)

        call process_character (n, appearance="blush false", text="(Но это довольно мило!)")
    else:
        call process_character (n, appearance="blush false", text="(Тпру...)")
        call process_character (n, appearance="blush false", text="(Тетя [janet.say_name] прямо падает на меня!)")
        call process_character (n, appearance="blush false", text="(Когда она это делает, я чувствую себя удивительно!)")

        show bg janet_vaginal_behind_down
        with Dissolve(0.5)

        call process_character (n, appearance="blush false", text="Мм!")
        call process_character (n, appearance="blush false", text="(Мой член становится все теплее и теплее!)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Я не был уверен, чего ожидать от тети [janet.say_name] сидящей на мне...)")
        call process_character (n, appearance="blush false", text="(Но это довольно мило!)")

        show bg janet_vaginal_behind_up
        with Dissolve(0.5)

    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="Давай продолжим, [n.say_name]!")

    show bg janet_vaginal_behind_down
    with Dissolve(0.5)

    call process_character (janet, appearance="blush false", text="{i}Задыхается!{/i}")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="Я почувствовала оргазм...{w=1.0}только что...")
    call process_character (n, appearance="blush false", text="Ммм, хрм!")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Надеюсь, этот диван выдержит...)")
    call process_character (janet, appearance="blush false", text="(Я слышу, как он скрипит каждый раз, когда я подпрыгиваю на члене [n.say_name])")
    call process_character (janet, appearance="blush false", text="(Последнее, что мне нужно, это заплатить за ремонт...)")

    show bg janet_vaginal_behind_up
    with Dissolve(0.5)

    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Ты скользишь на моем пенисе!")
    call process_character (janet, appearance="blush false", text="Это делает движение более легким, [n.say_name]!")
    call process_character (janet, appearance="blush false", text="Пока твой член влажный, ты не будешь иметь проблем со скольжением в моей киске!")

    show bg janet_vaginal_behind_down
    with Dissolve(0.5)

    call process_character (n, appearance="blush false", text="Ах!")
    call process_character (janet, appearance="blush false", text="Я помогу тебе достичь оргазм!")
    call process_character (janet, appearance="blush false", text="Ты готов?")
    call process_character (n, appearance="blush false", text="Я...")
    call process_character (n, appearance="blush false", text="Думаю, да.")
    call process_character (janet, appearance="blush false", text="Я более чем счастлива дать тебе его, [n.say_name]!")
    call process_character (janet, appearance="blush false", text="Я покажу тебе, что значит иметь такую тетю, как я!")

    call static_still_ctc ("bg janet_vaginal_behind_downblur")

    call process_character (janet, appearance="blush false", text="(Мне действительно понравилось это...)")
    call process_character (janet, appearance="blush false", text="(Мое тело просто не останавливается, пока не будет удовлетворено!)")
    call process_character (n, appearance="blush false", text="Ху!")
    call process_character (janet, appearance="blush false", text="(Кого волнует, если что член моего племянника, [n.say_name], именно то, в чём моя киска нуждается!)")
    call process_character (n, appearance="blush false", text="Хррм!")
    call process_character (janet, appearance="blush false", text="Вот он, [n.say_name]!")
    call process_character (janet, appearance="blush false", text="Последний рывок!")
    call process_character (n, appearance="blush false", text="Ладно...")

    show bg janet_vaginal_behind_up
    with Dissolve(0.5)

    call process_character (janet, appearance="blush false", text="На счет три!")
    call process_character (janet, appearance="blush false", text="Один...")
    call process_character (janet, appearance="blush false", text="Двое...")
    call process_character (janet, appearance="blush false", text="Три!")

    show bg janet_vaginal_behind_down
    with Dissolve(0.5)

    call process_character (n, appearance="blush false", text="Йаах!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg janet_vaginal_behind_down_cum")

    call process_character (janet, appearance="blush false", text="Я с удвоенной силой прыгаю!")
    call process_character (janet, appearance="blush false", text="Ааах ебать!")
    call process_character (janet, appearance="blush false", text="Бля, [n.say_name]!")
    call process_character (n, appearance="blush false", text="Хннг, Ммм!")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}.")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Какой превосходный трах!)")
    call process_character (janet, appearance="blush false", text="(Каждый мой дюйм вспотел!)")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (janet, appearance="blush false", text="Какой хороший мальчик, [n.say_name]!")
    call process_character (janet, appearance="blush false", text="Позволь мне поцеловать тебя.")
    "{i}Чмок...{/i}"
    call process_character (n, appearance="blush false", text="Это, {i}фуух.{/i}..")
    call process_character (n, appearance="blush false", text="Это было весело, тетя [janet.say_name].")
    call process_character (janet, appearance="blush false", text="Это совсем другой тип развлечения, не так ли?")
    call process_character (n, appearance="blush false", text="Да...")

    call static_still_ctc ("bg janet_vaginal_behind_up_cum")

    call process_character (janet, appearance="blush false", text="(О, Вау!)")
    call process_character (janet, appearance="blush false", text="(Там много спермы в моей киске!)")
    call process_character (janet, appearance="blush false", text="(Намного больше, чем я думала!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Когда мы можем сделать это снова, тетя [janet.say_name]?")
    call process_character (janet, appearance="blush false", text="Уже интересуешься? Хаха!")
    call process_character (janet, appearance="blush false", text="Когда у тебя будет время прийти.")
    call process_character (janet, appearance="blush false", text="Я всегда буду здесь, когда придет мой любимый племянник.")
    call process_character (n, appearance="blush false", text="Но я твой единственный племянник...")
    call process_character (janet, appearance="blush false", text="Единственный и неповторимый [n.say_name]!")

    python:
        janet.revistable_scenes.add("janet_scene_vaginal_revisit")
        if not dream:
            stats.add_stat("times_seen_vagina", 1)
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_had_vaginal_sex", 1)
            stats.add_stat("times_given_vaginal_creampie", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("janet_scene_vaginal", char=janet, dream=dream)

    return

label janet_scene_vaginal_revisit:
    $ no_bust_art = False

    if "janet_scene_vaginal_revisit" in scenes_completed:
        call janet_scene_vaginal_revisit_2nd_time
    else:
        call janet_scene_vaginal_revisit_1st_time

    return

label janet_scene_vaginal_revisit_1st_time:
    call process_scene_beginning (bg=janet_house, char_tuple_array=[ (janet, "pose handface face curious blush false"), (n, "pose behindhead face neutral") ] )

    call process_character (janet, appearance="pose handface face curious blush false", text="Сесть на тебя?")
    call process_character (janet, appearance="pose handface face curious blush false", text="...")
    call process_character (janet, appearance="pose handface face happy blush false", text="Ну, что как!")
    call process_character (janet, appearance="pose handface face flirt blush false", text="Теперь я понимаю, что ты имел в виду...")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Ты сможешь это сделать?")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Только спроси, и ты это получишь, [n.say_name]!")

    call fade_to_black (1)

    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)
    call static_still_ctc ("bg janet_vaginal_sideview")

    call process_character (janet, appearance="pose handhips face flirt blush false", text="Я никогда не видела, чтобы член становился твердым так быстро, [n.say_name]!")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Ох, ох!")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Я буквально наблюдала, как ты переходишь от мягкой эрекции к полной в считанные секунды!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Я был очень взволнован, думая о том, что мы собираемся сделать...")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Тебя заводит твоя тетя?")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Ты больше никогда не будешь думать обо мне так же как раньше, правда?")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="...")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Что если я приеду к тебе в гости?")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Разве твоя семья не заметит, что ты стукаешь деревяшкой, пока я там?")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="...")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Я сделаю все возможное, чтобы этого не случилось.")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Я бы не рекомендовала носить спортивные штаны, когда я заезжаю, ха-ха!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Мм, Мм!")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Что ты делаешь дома, когда у тебя эрекция, [n.say_name]?")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Ты фантазируешь о том, чтобы быть со мной?")

    menu:
        "Временами...":
            call process_character (janet, appearance="blush false", text="Уверен, я не единственная, о чем ты думаешь...")
            call process_character (janet, appearance="blush false", text="Но это хорошо, что я в твоих мыслях!")
        "Я мастурбирую каждый день думая о тебе, тётя [janet.say_name]!":
            call add_boldness (1, tag="janet_vaginal_revisit_fantasize")
            call process_character (janet, appearance="blush false", text="Каждый день?")
            call process_character (janet, appearance="blush false", text="Твой уровень тестостерона должно быть выше крыши!")
            call process_character (janet, appearance="blush false", text="Все благодаря тому, что ты всегда думаешь обо мне!")
            call process_character (janet, appearance="blush false", text="Я чувствую гордость за это.")

    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Ах, ах...")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Разве не забавно, что мы трахаемся прямо в гостиной?")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="В конце концов, есть некоторые преимущества, что дома никого!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Д-Да...")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Мы бы не смогли сделать это у меня дома.")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="По крайней мере, не так легко!")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Даже если никто не увидит нас, но они могут услышать.")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Слушай как громко бьется моя попка о твои ноги!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="...")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Это довольно громко...")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="...")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="(Это напомнило мне...)")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="(Моя задница не стала больше?)")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="(В последнее время я укрепляла бедра и икры)")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="(Но это может сделать мой зад больше)")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="(Мне, возможно, придется изменить свою диету, чтобы помочь сдержать это...)")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Т-тетя [janet.say_name]...")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Ты собираешься делать эти большие прыжки, как раньше?")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Тебе понравилось, не так ли?")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="Хватайся!")

    call static_still_ctc ("bg janet_vaginal_behind_up")

    call process_character (janet, appearance="blush false", text="А вот и первый, [n.say_name]!")

    call static_still_ctc ("bg janet_vaginal_behind_down")

    call process_character (janet, appearance="blush false", text="Мм, блядь!")
    call process_character (n, appearance="blush false", text="Аах!")
    call process_character (janet, appearance="blush false", text="Мы оба это почувствовали!")

    call static_still_ctc ("bg janet_vaginal_behind_up")

    call process_character (janet, appearance="blush false", text="Кончик твоей головки как раз в моей киске!")
    call process_character (janet, appearance="blush false", text="Я оттолкнусь вниз, чтобы он не выскользнул!")

    show bg janet_vaginal_behind_down
    with Dissolve(0.5)

    call process_character (n, appearance="blush false", text="Оооо!")
    call process_character (janet, appearance="blush false", text="Если это будет продолжаться и дальше, придется встречаться у меня дома, чем у тебя!")
    call process_character (janet, appearance="blush false", text="Ты не получишь такого действия дома в семье!")

    if "kira_scene_vaginal" in scenes_completed or "simone_scene_vaginal" in scenes_completed or "sam_scene_vaginal" in scenes_completed or "julia_scene_vaginal" in scenes_completed:
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Мне все еще нравится жить у себя дома.")
        call process_character (janet, appearance="blush false", text="Ну конечно!")
        call process_character (janet, appearance="blush false", text="Я просто пошутила, преувеличила, [n.say_name].")
        call process_character (n, appearance="blush false", text="...")
        if "kira_scene_vaginal" in scenes_completed:
            call process_character (n, appearance="blush false", text="(Когда я вернусь домой, то хотел бы заняться сексом с [k.say_name]...)")
        elif "simone_scene_vaginal" in scenes_completed:
            call process_character (n, appearance="blush false", text="(Когда я вернусь домой, то хотел бы заняться сексом с [si.say_name]...)")
        elif "sam_scene_vaginal" in scenes_completed:
            call process_character (n, appearance="blush false", text="(Когда я вернусь домой, то хотел бы заняться сексом с [sa.say_name]...)")
        else:
            call process_character (n, appearance="blush false", text="(Когда я вернусь домой, то хотел бы заняться сексом с [julia.say_name]...)")
    else:
        call process_character (n, appearance="blush false", text="Ты права!")
        call process_character (n, appearance="blush false", text="Я хочу приехать как можно скорее!")
        call process_character (janet, appearance="blush false", text="Это значит, что мне придется запастись едой в холодильнике!")
        call process_character (janet, appearance="blush false", text="Ты должен оставить одежду здесь, если хочешь переночевать!")
        call process_character (n, appearance="blush false", text="Попробую взять её в следующий раз.")

    show bg janet_vaginal_behind_up
    with Dissolve(0.5)

    call process_character (janet, appearance="blush false", text="Я собираюсь заставить тебя прийти, [n.say_name]!")
    call process_character (janet, appearance="blush false", text="Я хочу повторить действие!")
    call process_character (n, appearance="blush false", text="Ладно...")

    call static_still_ctc ("bg janet_vaginal_behind_downblur")

    call process_character (janet, appearance="blush false", text="Мм! Мм!")
    call process_character (janet, appearance="blush false", text="{i}Вздох!{/i}")
    call process_character (janet, appearance="blush false", text="Я не собираюсь замедляться!")
    call process_character (n, appearance="blush false", text="Ах! Хах, а!")
    call process_character (n, appearance="blush false", text="(Она двигается быстрее, чем в первый раз, когда мы это сделали?)")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох!{/i}")
    call process_character (n, appearance="blush false", text="(Все мое тело трясется, когда она давит на мой пенис!)")
    call process_character (janet, appearance="blush false", text="Вот оно, вот оно!")
    call process_character (janet, appearance="blush false", text="Твой член красивый и скользкий.")
    call process_character (janet, appearance="blush false", text="Он доволен такой ситуацией!")
    call process_character (n, appearance="blush false", text="Я знаю, моя ситуация...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я готов кончить!")
    call process_character (janet, appearance="blush false", text="Как я и думала, [n.say_name]!")
    call process_character (janet, appearance="blush false", text="Тетушка хочет твою сперму!")
    call process_character (janet, appearance="blush false", text="Дай столько, сколько сможешь!")
    call process_character (n, appearance="blush false", text="Хммн...")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Нннг!")

    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )

    call static_still_ctc ("bg janet_vaginal_behind_down_cum")

    call process_character (janet, appearance="blush false", text="Пусть твой член делает свое дело!")
    call process_character (janet, appearance="blush false", text="Ммм!")
    call process_character (janet, appearance="blush false", text="Чёрт, как это хорошо!")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..{p}{i}Вздох{/i}...")

    call static_still_ctc ("bg janet_vaginal_behind_up_cum")

    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Так хорошо, когда [n.say_name] кончает!)")
    call process_character (janet, appearance="blush false", text="(Я видела впечатляющие оргазмы в свое время...)")
    call process_character (janet, appearance="blush false", text="(Но не как у моего племянника!)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Я чувствую, что много спермы на моем члене, тетя [janet.say_name].")
    call process_character (janet, appearance="blush false", text="Постарайся не упасть на диван!")
    call process_character (janet, appearance="blush false", text="Будет, сука, сложно очистить эту ткань!")

    call janet_scene_vaginal_revisit_end

    return

label janet_scene_vaginal_revisit_2nd_time:
    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    call static_still_ctc ("bg janet_vaginal_behind_down")

    call process_character (janet, appearance="blush false", text="...")

    if 1 == 2:
        call process_character (janet, appearance="blush false", text="(Удивительно думать, что [n.say_name] помог мне загладить вину перед [si.say_name].)")
        call process_character (janet, appearance="blush false", text="(То, что я трахаю её сына, помогло исцелить наши отношения)")
        call process_character (janet, appearance="blush false", text="...")
        call process_character (janet, appearance="blush false", text="(Кто бы мог подумать!)")

        call static_still_ctc ("bg janet_vaginal_behind_up")

        call process_character (janet, appearance="blush false", text="(Я рада, как все получилось)")
        call process_character (janet, appearance="blush false", text="(Теперь [n.say_name] и я можем трахаться вместе, когда захотим...)")

        call static_still_ctc ("bg janet_vaginal_behind_down")

        call process_character (janet, appearance="blush false", text="(И мне не нужно скрывать это от моей сестры)")
        call process_character (janet, appearance="blush false", text="(Дела в нашей семье идут на лад!)")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="(Я беспокоился о том, как мама отреагирует на тетю [janet.say_name] и меня...)")
        call process_character (n, appearance="blush false", text="(На мгновение я подумал, что она собирается драться!)")
        call process_character (n, appearance="blush false", text="(Слава богу, что этого не произошло)")
        call process_character (n, appearance="blush false", text="(Я не думаю, что мама когда-либо намеревалась сделать что-то подобное)")

        call static_still_ctc ("bg janet_vaginal_behind_up")

        call process_character (n, appearance="blush false", text="(Казалось, что она хотела выяснить, что произошло, и хотела услышать, что тетя [janet.say_name] хочет сказать)")
        call process_character (n, appearance="blush false", text="(Я рад, что все еще могу навестить свою тетю!)")
        call process_character (n, appearance="blush false", text="(Она, кажется, очень рада, что наконец-то смогла поговорить с мамой!)")

        call static_still_ctc ("bg janet_vaginal_behind_down")
    else:

        call process_character (janet, appearance="blush false", text="(Я даже не хочу думать, что будет, если моя сестра узнает об этом)")
        call process_character (janet, appearance="blush false", text="(Она нахрен с ума сойдет!)")
        call process_character (janet, appearance="blush false", text="(Я даже не знаю, что она со мной сделает...)")
        call process_character (janet, appearance="blush false", text="...")

        call static_still_ctc ("bg janet_vaginal_behind_up")

        call process_character (janet, appearance="blush false", text="(Я определенно поставила себя в трудное положение)")
        call process_character (janet, appearance="blush false", text="(Единственное, на что я могу надеяться, это то, что [n.say_name] будет молчать об этом как можно дольше)")
        call process_character (janet, appearance="blush false", text="(Но это не гарантирует..)")
        call process_character (janet, appearance="blush false", text="...")
        call process_character (janet, appearance="blush false", text="(Что хуже, если я сама признаюсь [si.say_name], или она узнает это от [n.say_name]?)")

        call static_still_ctc ("bg janet_vaginal_behind_down")

        call process_character (janet, appearance="blush false", text="(Я думаю, что это было бы похоже на выбор топора или меча для казни)")
        call process_character (janet, appearance="blush false", text="...")
        call process_character (janet, appearance="blush false", text="(Опять же, может быть, я слишком беспокоюсь)")
        call process_character (janet, appearance="blush false", text="(Моя сестра всегда лучше понимала ситуации, чем я...)")

    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Интересно, что подумает тетя [janet.say_name] о том чтобы сделать это на пляже!)")
    call process_character (n, appearance="blush false", text="(Хотя мы должны будем убедиться, что никто нас не видит...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Мы могли бы купить один из тех огромных зонтов, которые, как палатка!)")
    call process_character (n, appearance="blush false", text="(Но если будет ветрено, он может опрокинуться...)")

    call static_still_ctc ("bg janet_vaginal_behind_up")

    call process_character (n, appearance="blush false", text="(О, ночью было бы меньше людей вокруг!)")
    call process_character (n, appearance="blush false", text="(Мы могли бы заниматься сексом, а затем плавать, или наоборот!)")
    call process_character (n, appearance="blush false", text="(Это было бы так здорово!)")
    call process_character (n, appearance="blush false", text="(Мне нужно спросить тетю [janet.say_name]!)")

    $ quick_menu = False
    window hide
    call screen progress_button_screen("Кончить!", xalign = 0.99, yalign = 0.1)
    $ quick_menu = True

    call static_still_ctc ("bg janet_vaginal_behind_downblur")

    call process_character (janet, appearance="blush false", text="Твои руки сжимают меня крепче!")
    call process_character (janet, appearance="blush false", text="Есть только одно объяснение...")
    call process_character (n, appearance="blush false", text="Это потому, что я собираюсь...")
    call process_character (n, appearance="blush false", text="Хмм!")


    if persistent.enable_sex_sounds:
        $ renpy.play ( "audio/sounds/DSKB1_Ejaculation_04.ogg" )
    call static_still_ctc ("bg janet_vaginal_behind_down_cum")

    call process_character (n, appearance="blush false", text="Я кончаю, тётя [janet.say_name]!")
    call process_character (n, appearance="blush false", text="Аах!")
    call process_character (janet, appearance="blush false", text="Поверь мне, я бы узнала, даже если бы ты не сказал!")

    call static_still_ctc ("bg janet_vaginal_behind_up_cum")

    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (janet, appearance="blush false", text="…")
    call process_character (janet, appearance="blush false", text="Ты выглядишь усталым после этого, [n.say_name].")
    call process_character (janet, appearance="blush false", text="Я сделаю тебе особый сок.")
    call process_character (janet, appearance="blush false", text="Он даст тебе большой прилив энергии!")

    call janet_scene_vaginal_revisit_end

    return

label janet_scene_vaginal_revisit_end:

    python:
        stats.add_stat("times_seen_vagina", 1)
        stats.add_stat("times_had_erection", 1)
        stats.add_stat("times_had_penis_seen", 1)
        stats.add_stat("times_had_vaginal_sex", 1)
        stats.add_stat("times_given_vaginal_creampie", 1)
        stats.add_stat("times_given_creampie", 1)
        stats.add_stat("times_had_penetrative_sex", 1)
        stats.add_stat("times_had_sex", 1)

    call process_end_of_scene ("janet_scene_vaginal_revisit", char=janet, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return

label janet_scene_anal(dream=False):
    call janet_scene_anal_sex (dream=dream)
    return

label janet_scene_anal_sex(dream=False):
    $ renpy.start_predict("janet_anal_anim")
    call process_scene_beginning (bg="bg janet_house_daytime", char_tuple_array=[ (janet, "outfit swimsuit pose handhips face neutral blush false"), (n, "outfit clothesjacket pose behindhead face neutral blush false") ], dream=dream )


    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false")

    call process_character (n, appearance="outfit clothesjacket pose behindhead face neutral blush false", text="Ты только что вернулась с пляжа, тетя [janet.say_name]?")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Наоборот.")
    call process_character (janet, appearance="outfit swimsuit pose handchest face happy blush false", text="Я собиралась туда пойти!")
    call process_character (janet, appearance="outfit swimsuit pose handchest face happy blush false", text="Ты хочешь пойти со мной?")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Да!")
    call process_character (n, appearance="outfit clothesjacket pose twohandfist face happy blush false", text="Ни за что не пропущу пляж!")
    call process_character (janet, appearance="outfit swimsuit pose handhips face happy blush false", text="Тогда переодень плавки и возьми полотенце!")

    call fade_to_black (1)


    call process_new_location ("bg beach_daytime", dream=dream)

    if had_edna_intro_scene:
        $ display_multiple_characters([ (n, "outfit swimsuit pose handsdown face neutral blush false"), (janet, "outfit swimsuit pose handface face happy blush false") ])
        call process_character (janet, appearance="outfit swimsuit pose handface face happy blush false", text="Я видела тебя, твою маму и твоих сестер здесь на днях!")
        call process_character (janet, appearance="outfit swimsuit pose handface face neutral blush false", text="У всех вас наконец-то появился шанс прийти сюда?")
        call process_character (n, appearance="pose twohandfist face neutral blush false", text="Да!")
        call process_character (n, appearance="pose twohandfist face neutral blush false", text="Мы ездили на квартиру к бабушке.")
        call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Разве не хорошее место?")
        call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Я стараюсь навещать ее раз в неделю.")
        call process_character (janet, appearance="outfit swimsuit pose handhips face happy blush false", text="Она любит общаться со мной во время прогулки по пляжу!")
    else:
        $ display_multiple_characters([ (n, "outfit swimsuit pose handsdown face neutral blush false"), (janet, "outfit swimsuit pose handface face curious blush false") ])
        call process_character (janet, appearance="outfit swimsuit pose handface face curious blush false", text="У твоей мамы и сестер все еще не было возможности сходить на пляж?")
        call process_character (n, appearance="pose behindhead face curious blush false", text="Нет, пока нет...")
        call process_character (janet, appearance="outfit swimsuit pose handhips face happy blush false", text="Нам придется связать их в машине и тащить туда!")
        call process_character (janet, appearance="outfit swimsuit pose handhips face happy blush false", text="Пляжная погода не будет длиться вечно!")

    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false", text="...")
    call process_character (n, appearance="outfit swimsuit pose handsdown face neutral blush false", text="Что это за зонтики и стулья там?")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Ох, те?")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Персонал кондоминиума предоставляет их владельцам, но мы можем использовать их.")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Они хорошего качества, и помогают, когда нужно остыть в тени.")
    call process_character (n, appearance="outfit swimsuit pose behindhead face neutral blush false", text="Никто ими не пользуется.")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="По крайней мере, не сейчас.")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="Думаю, мы приехали сюда во время затишья.")
    call process_character (janet, appearance="outfit swimsuit pose handhips face neutral blush false", text="...")
    call process_character (janet, appearance="outfit swimsuit pose handchest face neutral blush false", text="Ты хотел взять парочку?")
    call process_character (n, appearance="outfit swimsuit pose handfist face neutral blush false", text="Было бы неплохо выбраться от Солнца.")
    call process_character (n, appearance="outfit swimsuit pose handfist face neutral blush false", text="Мне нравится сидеть на песке.")
    call process_character (janet, appearance="outfit swimsuit pose handface face neutral blush false", text="Почему бы тебе не лечь между шезлонгами?")
    call process_character (janet, appearance="outfit swimsuit pose handface face neutral blush false", text="Ты сможешь лечь на полотенце, и мы установим зонтик для себя.")
    call process_character (n, appearance="outfit swimsuit pose twohandfist face happy blush false", text="Хорошая идея!")
    call process_character (janet, appearance="pose handhips face happy blush false", text="Солнце уже на пике.")
    call process_character (janet, appearance="pose handhips face happy blush false", text="Это хорошее время, чтобы загорать!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...{p}...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Тетя [janet.say_name]?")

    call process_character (janet, appearance="pose handhips face neutral blush false")


    call process_character (janet, appearance="pose handhips face neutral blush false")

    call process_character (n, appearance="pose behindhead face concerned blush false", text="Ты собираешься загорать голышом?")
    call process_character (janet, appearance="pose handface face happy blush false", text="Хаха!")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Ну, дело в том, что [n.say_name]...")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Это не нудистский пляж.")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Так что у меня были бы проблемы, если бы я лежала здесь голой.")
    call process_character (n, appearance="pose handsdown face curious blush false", text="Но как насчет того, когда мы были здесь ночью?")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="В это время вокруг никого нет, и темно.")
    call process_character (janet, appearance="pose handhips face happy blush false", text="Нельзя быть выгнанной за непристойное обнажение, если они тебя не видят!")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Ох...")
    call process_character (janet, appearance="pose handface face happy blush false", text="Ты надеялся, что сможешь на меня пялиться?")
    call process_character (janet, appearance="pose handface face happy blush false", text="Хаха!")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Да, мне вроде как понравилось...")
    call process_character (janet, appearance="pose handface face neutral blush false", text="(Посмотрите на это разочарованное лицо...)")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="([n.say_name] действительно ожидал какой-то сексуальной активности)")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="(Он, вероятно, надеялся, что как только я разденусь, он сможет потереть мои сиськи или поиграть с моей киской...)")
    call process_character (janet, appearance="pose handhips face flirt blush false", text="...")
    call process_character (janet, appearance="pose handface face embarrassed blush false", text="(Мы не можем заниматься сексом здесь, на открытом воздухе, хотя...)")
    call process_character (janet, appearance="pose handface face embarrassed blush false", text="...")
    call process_character (janet, appearance="pose handface face curious blush false", text="...")
    call process_character (janet, appearance="pose handhips face curious blush false", text="(Хм...)")
    call process_character (janet, appearance="pose handhips face curious blush false", text="(Или это возможно...{w=1.0}, если мы будем осторожны...)")
    call process_character (n, appearance="pose handsdown face concerned blush false", text="...")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Я знаю, что мы немного нарушаем правила [n.say_name], но почему бы тебе не раздеться?")
    call process_character (n, appearance="pose handsdown face embarrassed blush false", text="Мне?")
    call process_character (n, appearance="pose handsdown face embarrassed blush false", text="Но что, если меня поймают?")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Не беспокойся об этом.")
    call process_character (janet, appearance="pose handhips face neutral blush false", text="Я прослежу, чтобы тебя никто не видел.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Зачем мне раздеваться, тетя [janet.say_name]?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Есть какая-то причина?")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Узнаешь, [n.say_name].")
    call process_character (janet, appearance="pose handchest face neutral blush false", text="Это в твоих интересах, снять плавки.")
    call process_character (n, appearance="pose handsdown face curious blush false", text="...")
    call process_character (n, appearance="pose handsdown face curious blush false", text="В моих интересах?")
    call process_character (janet, appearance="pose handface face flirt blush false", text="Говоря по-другому...")
    call process_character (janet, appearance="pose handface face flirt blush false", text="Это будет в интересах твоего члена.")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Оох!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Теперь я понимаю, что ты имеешь в виду, тетя [janet.say_name]!")

    call character_leave_dissolve (n)
    pause 0.5

    call process_character (n, appearance="outfit nudesoft pose handfist face happy blush false")
    pause 0.5

    call process_character (n, appearance="outfit nudesoft pose handfist face happy blush false", text="Да, я определенно понимаю!")
    call process_character (janet, appearance="pose handhips face shocked blush false", text="Не раздевайся здесь, [n.say_name]!")
    call process_character (janet, appearance="pose handhips face shocked blush false", text="Кто-нибудь тебя увидит!")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="Ой, прости!")
    call process_character (janet, appearance="pose handface face shocked blush false", text="Вставай между шезлонгами, быстро!")
    call process_character (janet, appearance="pose handface face shocked blush false", text="Я буду сидеть перед тобой, чтобы тебя не было видно!")

    call fade_to_black (1)

    call process_character (janet, appearance="pose handface face shocked blush false", text="Опусти свое полотенце...")
    call process_character (janet, appearance="pose handface face shocked blush false", text="...")
    call process_character (janet, appearance="pose handface face shocked blush false", text="Хорошо, хорошо!")
    call process_character (janet, appearance="pose handface face shocked blush false", text="Теперь ложись на него.")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="Вот так?")
    call process_character (janet, appearance="pose handface face shocked blush false", text="Да, это просто замечательно.")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="Кто-нибудь видел меня?")
    call process_character (janet, appearance="pose handface face shocked blush false", text="Мм...{w=1.0}нет, не заметили.")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="{i}Фух.{/i}..")
    call process_character (janet, appearance="pose handface face shocked blush false", text="В любом случае, сесть здесь было хорошей идеей.")
    call process_character (janet, appearance="pose handface face shocked blush false", text="Солнце становится все ярче.")
    call process_character (janet, appearance="pose handface face shocked blush false", text="...")
    call process_character (janet, appearance="pose handface face shocked blush false", text="Эй, можешь подвинуть один из шезлонгов позади себя?")
    call process_character (janet, appearance="pose handface face shocked blush false", text="Тогда никто не увидит тебя, если они выйдут на пляж.")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="Да, я могу это сделать...")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="Мы делаем многое, чтобы никто меня не увидел...")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="Ты уверена, что хочешь, чтобы я остался голым?")
    call process_character (janet, appearance="pose handface face shocked blush false", text="Ах, да, я уверена.")
    call process_character (janet, appearance="pose handface face shocked blush false", text="Поверь мне, это того стоит.")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="...")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="(Что задумала тетя [janet.say_name]?)")
    call process_character (janet, appearance="pose handface face shocked blush false", text="...")
    call process_character (janet, appearance="pose handface face shocked blush false", text="(Побережье пока выглядит чистым)")
    call process_character (janet, appearance="pose handface face shocked blush false", text="...")
    call process_character (janet, appearance="pose handface face shocked blush false", text="(Это будет безумием, если мы сможем сделать это, не будучи замеченными!)")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="тебе что-нибудь нужно, чтобы я сделал, тетя [janet.say_name]?")
    call process_character (janet, appearance="pose handface face shocked blush false", text="Все, что мне нужно, чтобы ты просто оставался там, где ты есть, [n.say_name].")
    call process_character (janet, appearance="pose handface face shocked blush false", text="И постарайся молчать, если сможешь.")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="Молчать?")
    call process_character (n, appearance="outfit nudesoft pose twohandfist face embarrassed blush false", text="{cps=40}Зачем мне молчать-{/cps}{w=0.75}{nw}")

    python hide:
        if not dream or persistent.disable_dream_music:
            play_music("audio/music/Sensual Groove.ogg", fadein = 1.0)

    call static_still_ctc ("bg janet_anal_natesoft")

    call process_character (n, appearance="blush false", text="!!")
    call process_character (janet, appearance="blush false", text="Ты понимаешь, почему мы так пристроились?")
    call process_character (n, appearance="blush false", text="Т-ты трёшься своей попкой о мой пенис.")
    call process_character (janet, appearance="blush false", text="Если ты получишь стояк для меня [n.say_name], тогда будет нечто большее...")
    call process_character (n, appearance="blush false", text="Д-да?")
    call process_character (janet, appearance="blush false", text="Это все, что тебе нужно сделать, [n.say_name].")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Я чувствую, как его член и яйца смещаются)")
    call process_character (janet, appearance="blush false", text="(Я думаю не будет проблем с тем, чтобы у него встал от этого)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Он определенно становится твёрже, тетя [janet.say_name]...")
    call process_character (janet, appearance="blush false", text="Я еще немного пошевелю задницей.")
    call process_character (janet, appearance="blush false", text="Это должно помочь твоему члену расти быстрее.")
    call process_character (n, appearance="blush false", text="Ох!")

    call static_still_ctc ("bg janet_anal_natehard")

    call process_character (janet, appearance="blush false", text="О да, теперь ты совсем одеревенел.")
    call process_character (janet, appearance="blush false", text="Твой член упирается в мою задницу.")
    call process_character (n, appearance="blush false", text="Ах...")
    call process_character (n, appearance="blush false", text="(Мой пенис скользит между ее ягодицами!)")
    call process_character (n, appearance="blush false", text="(Это то, что она хотела сделать со мной на пляже?)")
    call process_character (janet, appearance="blush false", text="Ммм, [n.say_name]...")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="Это заводит меня, быть на виду.")
    call process_character (janet, appearance="blush false", text="Я хочу трахаться прямо здесь и сейчас.")
    call process_character (n, appearance="blush false", text="Ты хочешь трахаться, тетя [janet.say_name]?")
    call process_character (janet, appearance="blush false", text="Я хочу попробовать анальный секс, [n.say_name].")
    call process_character (janet, appearance="blush false", text="Мне давно уже хотелось его попробовать.")
    call process_character (n, appearance="blush false", text="Анальный секс?")

    if stats.stat_value("times_given_anal_sex") > 0 or heard_of_anal:
        call process_character (n, appearance="blush false", text="Ты имеешь в виду, что я засуну свой член тебе в задницу?")
        call process_character (janet, appearance="blush false", text="Да, это верно!")
        call process_character (janet, appearance="blush false", text="Вы, должно быть, уже знаешь об этом.")
        call process_character (n, appearance="blush false", text="...")
        call process_character (n, appearance="blush false", text="Да...")
        call process_character (janet, appearance="blush false", text="Разве это не звучит сексуально, [n.say_name]?")
        call process_character (janet, appearance="blush false", text="Ты можешь засунуть свой член мне в задницу?")
        call process_character (janet, appearance="blush false", text="О, я так сильно хочу попробовать!")
    else:
        call process_character (n, appearance="blush false", text="Что это такое?")
        call process_character (janet, appearance="blush false", text="Это как обычный секс, но ты засовываешь свой член мне в жопу, а не в киску.")
        call process_character (n, appearance="blush false", text="П-правда?")
        call process_character (n, appearance="blush false", text="Мы можем это сделать?")
        call process_character (janet, appearance="blush false", text="Разве это не звучит сексуально [n.say_name]?")
        call process_character (janet, appearance="blush false", text="Засунуть свой член мне в задницу?")
        call process_character (janet, appearance="blush false", text="О, я так сильно хочу попробовать!")

    $ heard_of_anal = True

    call process_character (n, appearance="blush false", text="Но как мы можем сделать это в твоем купальнике?")
    call process_character (janet, appearance="blush false", text="Это легко можно исправить, [n.say_name]...")
    call process_character (janet, appearance="blush false", text="Я просто сдвину часть моего костюма в сторону.")
    call process_character (janet, appearance="blush false", text="И когда я это сделаю, засунь свой член внутрь!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Я начну совершенно новый сексуальный опыт с моим племянником!)")
    call process_character (janet, appearance="blush false", text="(Я надеюсь, что [n.say_name] и я сможем сделать его хорошим!)")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="Ты готов?")
    call process_character (n, appearance="blush false", text="Да...")
    call process_character (n, appearance="blush false", text="Готов.")
    call process_character (janet, appearance="blush false", text="Окей...")
    call process_character (janet, appearance="blush false", text="Вставляй его, вставляй его!")

    call static_still_ctc ("bg janet_anal_nateinsert")

    call process_character (janet, appearance="blush false", text="Ммм!")
    call process_character (janet, appearance="blush false", text="Вот и всё, [n.say_name]...")
    call process_character (n, appearance="blush false", text="М-мой член в твоей заднице, тетя [janet.say_name]!")
    call process_character (janet, appearance="blush false", text="Да, ты сделал это отлично.")
    call process_character (janet, appearance="blush false", text="(Это сильно отличается от всего, что я чувствовала раньше!)")
    call process_character (janet, appearance="blush false", text="(И я даже пока не начала...)")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="Ты знаешь, что делать дальше, [n.say_name]?")

    if stats.stat_value("times_given_anal_sex") > 0:
        call process_character (n, appearance="blush false", text="Ты собираешься двигаться туда-сюда на моем члене?")
        call process_character (janet, appearance="blush false", text="В точку!")
        call process_character (janet, appearance="blush false", text="Я знаю, что ты не хочешь больше ждать.")
        call process_character (janet, appearance="blush false", text="Так почему бы мне не начать?")
        call process_character (n, appearance="blush false", text="Конечно.")
        call process_character (janet, appearance="blush false", text="Тебе понравится, когда я начну подпрыгивать на твоем члене.")
    else:
        call process_character (n, appearance="blush false", text="Это будет как когда мы трахались на диване?")
        call process_character (janet, appearance="blush false", text="Очень близко к этому, да!")
        call process_character (janet, appearance="blush false", text="Тебе понравится, когда я начну подпрыгивать на твоем члене.")
        call process_character (n, appearance="blush false", text="...")

    $ janet_anal_had_slow_speed_message = False
    $ janet_anal_had_normal_speed_message = False
    $ janet_anal_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    $ set_main_animation_speed(1.0)
    show anim_nothing_image as main_animation at main_animation_transform(IA_Animation_Janet_Anal_Info())
    with Dissolve(1.15)
    show bg white

    pause 
    $ quick_menu = True

    call process_character (janet, appearance="blush false", text="Ох!")
    call process_character (janet, appearance="blush false", text="О, да!")
    call process_character (n, appearance="blush false", text="Ха, ах!")
    call process_character (n, appearance="blush false", text="Хрм!")
    call process_character (janet, appearance="blush false", text="{i}Уххх!{/i}")
    call process_character (janet, appearance="blush false", text="Ах, чёрт, ах...")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Это так чертовски хорошо!)")
    call process_character (janet, appearance="blush false", text="(Я не знаю, смогу ли я сохранить нормальное лицо во время этого!)")
    call process_character (janet, appearance="blush false", text="(Мне, возможно, придется закрыть мой рот тоже!)")
    call process_character (janet, appearance="blush false", text="(Но это будет выглядеть странно для любого проходящего мимо!)")
    call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
    call process_character (n, appearance="blush false", text="Ахх, Мм!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я не вижу, идет ли кто-нибудь по пляжу)")
    call process_character (n, appearance="blush false", text="(Я надеюсь, тетя [janet.say_name] следит...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я не хочу, чтобы кто-то пришёл, поэтому ей не нужно останавливаться!)")
    call process_character (n, appearance="blush false", text="Оох!")
    call process_character (janet, appearance="blush false", text="Разве я не говорила, что это будет...{w=1.0}вздох...{w=1.0}в интересах твоего члена [n.say_name]?")
    call process_character (janet, appearance="blush false", text="Мм...")
    call process_character (n, appearance="blush false", text="Да, тетя [janet.say_name]!")
    call process_character (n, appearance="blush false", text="Хаах!")
    call process_character (n, appearance="blush false", text="И ты оказалась права!")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Мне просто нужно держать свое тело в вертикальном положении...)")
    call process_character (janet, appearance="blush false", text="(Это выглядит как будто я просто опускаюсь на колени на мгновение)")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Надеюсь, я не выгляжу слишком подозрительно спереди)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="Пляж по-прежнему чист, тетя [janet.say_name]?")
    call process_character (janet, appearance="blush false", text="До сих пор, так хорошо [n.say_name]...")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="Если ты хочешь, чтобы я двигалась немного быстрее, сейчас самое время спросить.")
    call process_character (janet, appearance="blush false", text="В любом случае, никого не видно.")
    call process_character (janet, appearance="blush false", text="Никакого риска для нас, чтобы получить немного больше этого.")
    call process_character (n, appearance="blush false", text="Ты уверена?")
    call process_character (janet, appearance="blush false", text="Если мы не воспользуемся возможностью сейчас, она может исчезнуть!")
    call process_character (n, appearance="blush false", text="...")

    window hide
    $ quick_menu = False
    show screen janet_anal_speed_settings(False)
    $ renpy.pause(3.0)
    $ renpy.suspend_rollback(True)

    call janet_scene_anal_phase_2 (dream=dream)

    return

label janet_anal_set_speed(speed):
    hide screen janet_anal_speed_settings
    $ set_main_animation_speed(speed)

    return

screen janet_anal_speed_settings(is_revisit=False, dream=False):
    vbox:
        xalign 0.97
        yalign 0.3
        spacing 20

        use main_menu_button(text="Медленно", action=Function(janet_anal_set_speed, "janet_anal_go_slow", is_revisit, dream), enabled=main_animation_speed != janet_anal_slow_speed_multiplier)
        use main_menu_button(text="Нормально", action=Function(janet_anal_set_speed, "janet_anal_go_normal", is_revisit, dream), enabled=main_animation_speed != 1.0)
        use main_menu_button(text="Быстро", action=Function(janet_anal_set_speed, "janet_anal_go_fast", is_revisit, dream), enabled=main_animation_speed != janet_anal_fast_speed_multiplier)


label janet_anal_go_slow(is_revisit, dream=False):
    call janet_anal_set_speed (janet_anal_slow_speed_multiplier)

    if is_revisit:
        if random.randint(0,1) == 0:
            call process_character (janet, appearance="blush false", text="Яркое солнце, не так ли?")
            call process_character (janet, appearance="blush false", text="В следующий раз я куплю солнцезащитные очки.")
        else:
            call process_character (janet, appearance="blush false", text="Интересно, есть ли здесь более уединенная часть пляжа.")
            call process_character (janet, appearance="blush false", text="Может, я осмотрюсь, когда представится возможность.")
    else:

        if random.randint(0,1) == 0:
            call process_character (n, appearance="blush false", text="Ты можешь двигаться немного медленнее, тетя [janet.say_name]?")
            call process_character (janet, appearance="blush false", text="Конечно, без проблем [n.say_name].")
        else:
            call process_character (n, appearance="blush false", text="Я хотел бы трахаться немного медленнее.")
            call process_character (janet, appearance="blush false", text="Мм...")
            call process_character (janet, appearance="blush false", text="(Я чувствую, как его член скользит по моей заднице, когда мы двигаемся медленнее...)")

    window hide
    with None
    $ janet_anal_had_slow_speed_message = True

    if is_revisit:
        $ renpy.call("janet_scene_anal_revisit_phase_2")
    else:
        $ renpy.call("janet_scene_anal_phase_2", dream = dream)

    return

label janet_anal_go_normal(is_revisit, dream=False):
    call janet_anal_set_speed (1.0)

    if is_revisit:
        if random.randint(0,1) == 0:
            call process_character (janet, appearance="blush false", text="Я слышала, что прогноз погоды на следующую неделю обещает много солнца!")
            call process_character (janet, appearance="blush false", text="Отличная новость для нас!")
        else:
            call process_character (janet, appearance="blush false", text="Надеюсь, все это не испортит мой купальник.")
            call process_character (janet, appearance="blush false", text="Мне пришлось много денег выложить за него!")
    else:
        if random.randint(0,1) == 0:
            call process_character (n, appearance="blush false", text="Давайте вернемся к скорости, с которой мы начали.")
            call process_character (janet, appearance="blush false", text="Нет проблем.")
            call process_character (janet, appearance="blush false", text="Это правильный баланс.")
        else:
            call process_character (n, appearance="blush false", text="Мы можем вернуться к нашей обычной скорости?")
            call process_character (janet, appearance="blush false", text="Конечно.")
            call process_character (janet, appearance="blush false", text="Мне нравится, как мы меняем темп!")

    window hide
    with None
    $ janet_anal_had_normal_speed_message = True

    if is_revisit:
        $ renpy.call("janet_scene_anal_revisit_phase_2")
    else:
        $ renpy.call("janet_scene_anal_phase_2", dream = dream)

    return

label janet_anal_go_fast(is_revisit, dream=False):
    call janet_anal_set_speed (janet_anal_fast_speed_multiplier)

    if is_revisit:
        if random.randint(0,1) == 0:
            call process_character (janet, appearance="blush false", text="{i}Уфф,{/i} я вся вспотела!")
            call process_character (janet, appearance="blush false", text="Я искупаюсь после этого, чтобы остыть!")
        else:
            call process_character (janet, appearance="blush false", text="О да, [n.say_name]!")
            call process_character (janet, appearance="blush false", text="Моя задница сжимается вокруг твоего члена!")
    else:
        if random.randint(0,1) == 0:
            call process_character (n, appearance="blush false", text="Прыгай на мне быстрее, тетя [janet.say_name]!")
            call process_character (janet, appearance="blush false", text="Ох, ох!")
            call process_character (janet, appearance="blush false", text="Достаточно ли быстро, [n.say_name]?")
            call process_character (n, appearance="blush false", text="Да, это просто замечательно!")
        else:
            call process_character (n, appearance="blush false", text="Я хочу двигаться быстрее, тетя [janet.say_name]!")
            call process_character (janet, appearance="blush false", text="Я слышу, как моя задница бьется о твое тело, [n.say_name]!")
            call process_character (janet, appearance="blush false", text="Ах, Мм!")

    window hide
    with None
    $ janet_anal_had_fast_speed_message = True

    if is_revisit:
        $ renpy.call("janet_scene_anal_revisit_phase_2")
    else:
        $ renpy.call("janet_scene_anal_phase_2", dream = dream)

    return

label janet_scene_anal_phase_2(dream=dream):
    show screen janet_anal_speed_settings(False, True)
    call screen progress_button_screen("Продолжить")
    $ quick_menu = True
    hide screen janet_anal_speed_settings
    $ renpy.suspend_rollback(False)

    call janet_scene_anal_phase_3 (dream=dream)

    return

label janet_scene_anal_phase_3(dream=dream):
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="Оох [n.say_name], все идет так хорошо.")
    call process_character (janet, appearance="blush false", text="Мой первый раз с аналом становится незабываемым!")
    call process_character (janet, appearance="blush false", text="Спасибо за это, [n.say_name].")
    call process_character (n, appearance="blush false", text="К-круто.")
    call process_character (n, appearance="blush false", text="Я имею в виду, я просто лежала здесь все это время.")
    call process_character (janet, appearance="blush false", text="Эй, это лучше...")
    call process_character (janet, appearance="blush false", text="Чем легче заниматься сексом, тем легче хорошо провести время...")
    call process_character (janet, appearance="blush false", text="Черт!")
    call process_character (n, appearance="blush false", text="А, что?")
    call process_character (janet, appearance="blush false", text="Кто-то идет!")
    call process_character (n, appearance="blush false", text="Д-да?!")
    call process_character (janet, appearance="blush false", text="Я знаю, что это неожиданно, но давай заканчивать, [n.say_name]!")


    call janet_anal_set_speed (janet_anal_fastest_speed_multiplier)

    call process_character (n, appearance="blush false", text="Ха! Ах! Ах!")
    call process_character (janet, appearance="blush false", text="Ты должен кончить, как можно быстрее, [n.say_name]!")
    call process_character (janet, appearance="blush false", text="Ты почти?")
    call process_character (n, appearance="blush false", text="{i}Вздох,{/i} {i}вздох.{/i}..")
    call process_character (n, appearance="blush false", text="Так быстро...")
    call process_character (janet, appearance="blush false", text="(Если он не кончит в ближайшее время, эти люди обязательно нас заметят!)")
    call process_character (janet, appearance="blush false", text="(Он должен быть близко...)")
    call process_character (n, appearance="blush false", text="О, тетя [janet.say_name]!")
    call process_character (n, appearance="blush false", text="Тетя [janet.say_name]!")
    call process_character (janet, appearance="blush false", text="Ммм!")
    call process_character (janet, appearance="blush false", text="(Хер [n.say_name] таранит мою задницу!)")
    call process_character (janet, appearance="blush false", text="(Это гораздо интенсивней, чем я думала!)")
    call process_character (n, appearance="blush false", text="Я кончаю, я кончаю!")

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
    show bg janet_anal_cumshot
    with Dissolve(1.5)

    pause
    $ quick_menu = True

    call process_character (n, appearance="blush false", text="Ааах...")
    call process_character (janet, appearance="blush false", text="Ох, [n.say_name]...")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="Ты, должно быть, много накончал.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="У-у тебя осталось немного на заднице.")
    call process_character (janet, appearance="blush false", text="Все в порядке, я смою её в океане.")
    call process_character (janet, appearance="blush false", text="Надень плавки.")
    call process_character (janet, appearance="blush false", text="Поспеши!")
    call process_character (janet, appearance="blush false", text="Мимо идёт группа людей!")
    call process_character (n, appearance="blush false", text="{i}Угх!{/i}")
    call process_character (janet, appearance="blush false", text="Всё хорошо.")
    call process_character (janet, appearance="blush false", text="Накройся полотенцем, пока одеваешь плавки.")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Это было близко!)")
    call process_character (janet, appearance="blush false", text="(Хотя это был отличный секс!)")
    call process_character (janet, appearance="blush false", text="(Я определенно хочу, чтобы анал был частью моей жизни!)")
    call process_character (janet, appearance="blush false", text="(Ощущения в моей заднице немного чувствительней...)")
    call process_character (janet, appearance="blush false", text="(Но это было после того, как мы поменяли темп!)")

    $ renpy.stop_predict("janet_anal_anim")
    python:
        janet.revistable_scenes.add("janet_scene_anal_revisit")
        if not dream:
            stats.add_stat("times_had_erection", 1)
            stats.add_stat("times_had_penis_seen", 1)
            stats.add_stat("times_seen_butt", 1)
            stats.add_stat("times_seen_butthole", 1)
            stats.add_stat("times_given_anal_sex", 1)
            stats.add_stat("times_given_anal_creampie", 1)
            stats.add_stat("times_given_creampie", 1)
            stats.add_stat("times_had_penetrative_sex", 1)
            stats.add_stat("times_had_sex", 1)
            stats.add_stat("times_had_public_sex", 1)

    call process_end_of_scene ("janet_scene_anal", char=janet, dream=dream)
    return

label janet_scene_anal_revisit:
    $ no_bust_art = False

    if "janet_scene_anal_revisit" in scenes_completed:
        call janet_scene_anal_revisit_2nd_time
    else:
        call janet_scene_anal_revisit_1st_time

    return

label janet_scene_anal_revisit_1st_time:
    $ renpy.start_predict("janet_anal_anim")

    call process_character (janet, appearance="pose handchest face curious blush false", text="Ты хочешь сделать это снова?")
    call process_character (n, appearance="pose handfist face happy blush false", text="Да!")
    call process_character (n, appearance="pose handfist face happy blush false", text="Мне действительно понравилось!")
    call process_character (janet, appearance="pose handface face neutral blush false", text="Давай сначала проверим пляж.")
    call process_character (janet, appearance="pose handface face happy blush false", text="Если там никого нет, значит все хорошо!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="(Пожалуйста, будь безлюден, пожалуйста...)")

    call fade_to_black (1)


    call static_still_ctc ("bg janet_anal_natesoft")

    call process_character (janet, appearance="blush false", text="Удача должна быть на твоей стороне, [n.say_name]!")
    call process_character (janet, appearance="blush false", text="Пляж совершенно пуст!")
    call process_character (n, appearance="blush false", text="Я надеялся, что так и будет!")
    call process_character (janet, appearance="blush false", text="Я тоже.")
    call process_character (janet, appearance="blush false", text="Анальный секс, которым мы занимались раньше...{w=1.0}это было чудесно!")
    call process_character (janet, appearance="blush false", text="Это то, чего ты с нетерпением ждёшь, [n.say_name]?")
    call process_character (n, appearance="blush false", text="Да!")
    call process_character (janet, appearance="blush false", text="Сначала о главном...")
    call process_character (janet, appearance="blush false", text="Твой член нужно разбудить!")
    call process_character (n, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="Мне просто нужно двигать задницей туда-сюда несколько раз...")
    call process_character (janet, appearance="blush false", text="А еще потрись о мой купальник своим членом.")
    call process_character (n, appearance="blush false", text="Это так хорошо, тетя [janet.say_name]...")
    call process_character (janet, appearance="blush false", text="Если он чувствует себя хорошо, то это может означать только...")

    call static_still_ctc ("bg janet_anal_natehard")

    call process_character (janet, appearance="blush false", text="Пора начинать.")
    call process_character (janet, appearance="blush false", text="Это не заняло много времени, чтобы у тебя встал, [n.say_name].")
    call process_character (janet, appearance="blush false", text="Еще одна причина, почему мне нравится быть с тобой.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="Все готово!")
    call process_character (janet, appearance="blush false", text="Засунь свой член мне в задницу, [n.say_name]!")
    call process_character (n, appearance="blush false", text="...{p}...")
    call process_character (janet, appearance="blush false", text="Ты чего-то ждешь?")
    call process_character (n, appearance="blush false", text="Ох...")
    call process_character (n, appearance="blush false", text="Я не услышал.")
    call process_character (janet, appearance="blush false", text="Я краем глаза видела, что ты делаешь...")
    call process_character (janet, appearance="blush false", text="Ты пялился на мою задницу, верно?")
    call process_character (n, appearance="blush false", text="Да...")
    call process_character (n, appearance="blush false", text="Моя вина.")
    call process_character (janet, appearance="blush false", text="Я уверена, что это шикарный вид с того места, где ты лежишь.")
    call process_character (janet, appearance="blush false", text="И ты все еще можешь наслаждаться им, пока твой член в моей заднице.")
    call process_character (n, appearance="blush false", text="...")

    call static_still_ctc ("bg janet_anal_nateinsert")

    call process_character (janet, appearance="blush false", text="Мм, вводи туда...")
    call process_character (janet, appearance="blush false", text="Столько, сколько сможешь.")
    call process_character (janet, appearance="blush false", text="Даа...")
    call process_character (n, appearance="blush false", text="Как быстро ты собираетесь двигаться, тетя [janet.say_name]?")
    call process_character (janet, appearance="blush false", text="Ну, а ты, как хочешь, чтобы я начала?")
    call process_character (janet, appearance="blush false", text="Любой темп для меня приемлем.")

    menu:
        "Медленный":
            $ set_main_animation_speed(janet_anal_slow_speed_multiplier)
            call process_character (janet, appearance="blush false", text="Будет легче, когда начнём медленнее.")
            call process_character (janet, appearance="blush false", text="Тогда мы сможем ускоряться по мере необходимости!")
        "Нормальный":
            $ set_main_animation_speed(1.0)
            call process_character (janet, appearance="blush false", text="Мне понравилась скорость, с которой мы мы впервые попробовали.")
            call process_character (janet, appearance="blush false", text="Не слишком быстро, но и не слишком медленно.")
        "Быстрый":
            $ set_main_animation_speed(janet_anal_fast_speed_multiplier)
            call process_character (janet, appearance="blush false", text="Сразу с места в карьер?")
            call process_character (janet, appearance="blush false", text="Если ты уверен, что справишься, то и я уверена, что справлюсь!")

    $ janet_anal_had_slow_speed_message = False
    $ janet_anal_had_normal_speed_message = False
    $ janet_anal_had_fast_speed_message = False

    $ clear_characters()
    $ quick_menu = False
    window hide
    $ play_sex_sounds = True
    show anim_nothing_image as main_animation at main_animation_transform(IA_Animation_Janet_Anal_Info())
    with Dissolve(1.15)
    show bg white


    pause 
    $ quick_menu = True

    call process_character (n, appearance="blush false", text="Мм, ах.")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Осенью, вероятно, будет слишком холодно, чтобы делать это на пляже...)")
    call process_character (n, appearance="blush false", text="(Отстой, мы сможем трахаться здесь только несколько месяцев...)")
    call process_character (n, appearance="blush false", text="...")
    call process_character (n, appearance="blush false", text="(Я обязательно буду ходить на пляж с тетей [janet.say_name] столько, сколько могу!)")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Ни одно лето не сравнится с этим)")
    call process_character (janet, appearance="blush false", text="(Отношения между [n.say_name] и мной развиваются так быстро...)")
    call process_character (janet, appearance="blush false", text="(Если бы кто-то сказал мне, что я буду встречаться с моим племянником, чтобы трахать его на постоянной основе…)")
    call process_character (janet, appearance="blush false", text="(Я бы назвала этого человека сумасшедшим!)")
    call process_character (janet, appearance="blush false", text="...")
    call process_character (janet, appearance="blush false", text="(Единственное, что [n.say_name] подтвердил для меня, насколько непредсказуемой может быть жизнь)")
    call process_character (janet, appearance="blush false", text="(Я понятия не имею, что произойдет осенью и дальше...{w=1.0}но я знаю, что это затронет меня и [n.say_name]!)")

    call janet_scene_anal_revisit_phase_2
    return

label janet_scene_anal_revisit_phase_2:
    $ quick_menu = False
    window hide
    show screen janet_anal_speed_settings(True, True)
    call screen progress_button_screen("Кончить!")
    $ renpy.scene('screens')
    hide screen janet_anal_speed_settings
    $ renpy.suspend_rollback(False)

    call janet_scene_anal_revisit_phase_3

    return

label janet_scene_anal_revisit_phase_3:
    if "janet_scene_anal_revisit" not in scenes_completed:
        $ quick_menu = True
        call process_character (n, appearance="blush false", text="Я собираюсь кончить, тетя [janet.say_name]!")
        call process_character (janet, appearance="blush false", text="Хорошо, [n.say_name]!")

        call janet_anal_set_speed (janet_anal_fastest_speed_multiplier)
        call process_character (janet, appearance="blush false", text="Кончай в задницу своей тети!")
        call process_character (n, appearance="blush false", text="Ммм...")
        call process_character (n, appearance="blush false", text="Ннгх!")

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
        show bg janet_anal_cumshot
        with Dissolve(1.5)

        pause
        $ quick_menu = True

        call process_character (janet, appearance="blush false", text="Да!")
        call process_character (janet, appearance="blush false", text="Я чувствую твое горячее семя.")
        call process_character (n, appearance="blush false", text="{i}Вздох.{/i}..")
        call process_character (janet, appearance="blush false", text="...")
        call process_character (janet, appearance="blush false", text="(Я должна следить, что моя мама не пройдет мимо...)")
        call process_character (janet, appearance="blush false", text="(Это было бы довольно неловкой ситуацией)")
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
        show bg janet_anal_cumshot
        with Dissolve(1.5)

        pause
        $ quick_menu = True

        call process_character (janet, appearance="blush false", text="Хм, да!")
        call process_character (janet, appearance="blush false", text="У меня такое большое количество спермы в заднице!")
        call process_character (janet, appearance="blush false", text="Вот бы ещё больше!")

    call janet_scene_anal_revisit_end

    return

label janet_scene_anal_revisit_2nd_time:
    python hide:
        play_music("audio/music/Sensual Groove.ogg", fadeout=1.0, fadein = 1.0)

    $ scene_anim = IA_Animation_Janet_Anal_Info()
    $ scene_anim.pause()
    $ no_bust_art = True

    $ janet_anal_had_slow_speed_message = False
    $ janet_anal_had_normal_speed_message = False
    $ janet_anal_had_fast_speed_message = False

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

    call process_character (janet, appearance="blush false", text="Ну что приступим, [n.say_name]?")
    call process_character (janet, appearance="blush false", text="С чего ты хочешь начать?")

    menu:
        "Медленный":
            $ scene_anim.unpause()
            $ set_main_animation_speed(janet_anal_slow_speed_multiplier)
            call janet_anal_go_slow (True, False)
        "Нормальный":
            $ scene_anim.unpause()
            $ set_main_animation_speed(1.0)
            call janet_anal_go_normal (True, False)
        "Быстрый":
            $ scene_anim.unpause()
            $ set_main_animation_speed(janet_anal_fast_speed_multiplier)
            call janet_anal_go_fast (True, False)
    return

label janet_scene_anal_revisit_end:
    $ scene_anim = None
    $ renpy.stop_predict("janet_anal_anim")

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
        stats.add_stat("times_had_public_sex", 1)



    call process_end_of_scene ("janet_scene_anal_revisit", char=janet, reset_prompted_scene=False, force_no_boldness=True, force_not_replayable=True, revisit=True)

    return