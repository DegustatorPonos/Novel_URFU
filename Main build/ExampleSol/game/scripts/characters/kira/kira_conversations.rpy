label kira_convo_default:
    call process_conversation_beginning ([ (n, ""), (k, "") ])

    call debug_message ("Default conversation when none others are available.")
    $ k.c("Привет " + n.say_name + ".")

    call process_end_of_conversation ("kira_convo_default", k, priority=False, default=True)

    return

label kira_convo_1:
    call process_conversation_beginning ([ (n, ""), (k, "pose armsup face neutral") ])

    call process_character (k, appearance="pose armsup face neutral", text="Погода здесь почти всегда солнечная.")
    call process_character (n, appearance="pose handpocket face curious", text="Тебе не нравится?")
    call process_character (k, appearance="pose armsup face neutral", text="Ты шутишь?")
    call process_character (k, appearance="pose armsup face happy", text="Какая прекрасная погода!")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (k, appearance="pose armcross face neutral", text="В нашем старом городе вряд ли можно было загореть.")
    call process_character (k, appearance="pose armcross face neutral", text="Только в отпуске я загорала.")
    call process_character (n, appearance="pose handpocket face curious", text="Что правда, то правда.")
    call process_character (n, appearance="pose handfist face neutral", text="Ты загораешь гораздо быстрее по сравнению с остальными.")
    call process_character (k, appearance="pose armcross face neutral", text="Ты просто должен работать над этим, как и над всем остальным.")
    call process_character (k, appearance="pose handhip face neutral", text="Но мама права насчет солнцезащитного крема.{p=1.0}На Солнце можно и обжечься!")

    call process_end_of_conversation ("kira_convo_1", k, priority=False)

    return

label kira_convo_2:
    call process_conversation_beginning ([ (n, ""), (k, "") ])

    call process_character (n, text="Ты скучаешь по старой школе?")
    call process_character (k, appearance="pose handhip", text="Не.")
    call process_character (k, appearance="pose handhip", text="Я имею в виду, там было весело.")
    call process_character (k, appearance="pose handhip face happy", text="Вытирать пол перед другими школьными командами было великолепно.")
    call process_character (k, appearance="pose armcross face neutral", text="Но теперь мне больше не нужно беспокоиться о школьной работе.")
    call process_character (k, appearance="pose armcross face neutral", text="Я могу сосредоточиться на карьере.")
    call process_character (n, appearance="pose handfist face neutral", text="Ты собираешься стать профессиональным инструктором по фитнесу?")
    call process_character (k, appearance="pose armcross face neutral", text="Хм, может быть.")
    call process_character (k, appearance="pose armcross face neutral", text="У меня большой спортивный опыт.")
    call process_character (k, appearance="pose armsup face neutral", text="Я могла бы быть квалифицированным тренером по футболу или баскетболу, если бы захотела.")
    call process_character (n, appearance="pose behindhead face neutral", text="Ты бы меняла игроков на себя, если бы команда начала проигрывать.")
    call process_character (k, appearance="pose armcross face happy", text="Ха, в этом ты прав.")
    call process_character (k, appearance="pose armcross face happy", text="Возможно, я стала бы первым тренером и активным игроком в спорте.")

    call process_end_of_conversation ("kira_convo_2", k, priority=False)

    return

label kira_convo_3:
    call process_conversation_beginning ([ (n, ""), (k, "pose handhip") ])

    call process_character (k, appearance="pose handhip", text="Мама сказала, что ее сад быстро растет.")
    call process_character (n, appearance="pose handpocket face happy", text="Да, я видела!")
    call process_character (k, appearance="pose handhip face concerned", text="Я даже не знаю, как она это делает.")
    call process_character (k, appearance="pose handhip face concerned", text="Она все время им занята.")
    call process_character (n, appearance="pose handpocket face concerned")
    call process_character (k, appearance="pose handhip face concerned", text="И все же ей удается ухаживать за всеми растениями.")
    call process_character (n, appearance="pose behindhead face neutral", text="Я думаю ей не помешала бы помощь.")
    call process_character (k, appearance="pose armcross face neutral", text="Ты всегда можешь спросить.{p=1.0}Может, ты сможешь помочь ей.")

    call process_end_of_conversation ("kira_convo_3", k, priority=False)

    return

label kira_convo_4:
    call process_conversation_beginning ([ (n, ""), (k, "") ])

    call process_character (n, text="Как на работе, много ушло людей после первого занятия?")
    call process_character (k, appearance="pose armsup face neutral", text="А ты как думаешь?{p=1.0}Я пользуюсь своим превосходством.")
    call process_character (k, appearance="pose armsup face neutral", text="Я хожу туда ради бесплатных тренажёров.")
    call process_character (n, appearance="pose handpocket face concerned", text="Тебя не накажут за это?")
    call process_character (k, appearance="pose handhip face neutral", text="Не.")
    call process_character (k, appearance="pose handhip face neutral", text="Остальные рабочие спрашивают у меня советы по правильной технике растяжки и поднятию тяжестей.")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (k, appearance="pose armcross face neutral", text="Некоторые клиенты приходят и даже не тренируются.")
    call process_character (k, appearance="pose armcross face neutral", text="Они просто хотят \"посмотреть\" на мои формы.")
    call process_character (n, appearance="pose handpocket face curious", text="Это странно.")
    call process_character (n, appearance="pose handpocket face curious", text="Приходят просто посмотреть, как ты тренируешься.")
    call process_character (k, appearance="pose handhip face neutral", text="Я уверена, они сами делают упражнения дома.")
    call process_character (k, appearance="pose handhip face concerned", text="Они, скорее всего, тренируют только одну \"мышцу\"... неоднократно.")
    call process_character (n, appearance="pose behindhead face curious")
    $ renpy.pause(1)
    call process_character (n, appearance="pose behindhead face curious", text="Некоторые люди странные.")

    call process_end_of_conversation ("kira_convo_4", k, priority=False)

    return

label kira_convo_5:
    call process_conversation_beginning ([ (n, ""), (k, "pose armcross") ])

    call process_character (k, appearance="pose armcross face neutral", text="Каково это - иметь собственную комнату?")
    call process_character (n, appearance="pose handpocket face neutral", text="Не плохо.")
    call process_character (k, appearance="pose armcross face neutral")
    $ k.c("Должно быть, странно больше не делить комнату с " + sa.say_name + ".")
    call process_character (k, appearance="pose armcross face neutral", text="Хотя ваши комнаты находятся рядом друг с другом.")
    call process_character (n, appearance="pose handpocket face neutral", text="Да.")
    call process_character (k, appearance="pose handhip face curious", text="Я слышал, вы двое будете транслировать прямой эфир людям или что-то вроде того?")
    call process_character (n, appearance="pose twohandfist face happy", text="Да!")
    call process_character (n, appearance="pose twohandfist face happy", text="У нас есть наш канал на [video_sharing_site], \"Твинстикс.\"")
    call process_character (n, appearance="pose twohandfist face neutral", text="На нем мы транслируем игры.")
    call process_character (k, appearance="pose armcross face neutral", text="\"Твин\"стикс. Умно.")
    call process_character (k, appearance="pose armcross face neutral", text="Я не успеваю за такими технологиями.")
    call process_character (k, appearance="pose armcross face neutral", text="Я в основном просто ищу вещи в интернете.")
    call process_character (k, appearance="pose armcross face neutral")
    $ k.c("Думаешь, ты и " + sa.say_name + " будете популярными?")
    call process_character (n, appearance="pose handfist face neutral", text="Мы надеемся!")
    call process_character (n, appearance="pose handfist face neutral", text="Мы все еще пытаемся придумать, как привлечь внимание людей.")
    call process_character (k, appearance="pose handhip face neutral", text="Уверен, ты что-нибудь придумаешь.")
    call process_character (k, appearance="pose handhip face neutral", text="Вы вдвоём отлично сработаетесь.")

    call process_end_of_conversation ("kira_convo_5", k, priority=False)

    return


label kira_convo_6:
    call process_conversation_beginning ([ (n, ""), (k, "pose armsup") ])

    call process_character (k, appearance="pose armsup face neutral", text="Итак...{p=1.0}Как тебе испытание?")
    call process_character (k, appearance="pose armsup face neutral", text="Весело было вести счет?")
    call process_character (n, appearance="pose twohandfist face neutral", text="Да!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Это было действительно здорово увидеть, когда я насчитал 150 очков в первый раз!")
    call process_character (k, appearance="pose handhip face neutral", text="А я продолжала приседать.")
    call process_character (k, appearance="pose handhip face neutral", text="Я убедилась, что правильно позиционирую себя для этого.")
    call process_character (k, appearance="pose armcross face neutral", text="Ты думаешь, у меня хорошая форма?")
    call process_character (n, appearance="pose behindhead face neutral", text="Нуу...{p=1.0}По мне отличная!")
    call process_character (k, appearance="pose armcross face neutral", text="Всё было правильно?")
    call process_character (k, appearance="pose armsup face neutral", text="Мои ноги были правильно расставлены.{p=1.0}Спина была выпрямлена.")
    $ renpy.pause(2)
    call process_character (k, appearance="pose armsup face flirty", text="Задница торчала...")
    call process_character (n, appearance="pose behindhead face embarrassed", text="Д-да.")
    call process_character (n, appearance="pose behindhead face embarrassed", text="Всё было замечательно.")
    call process_character (k, appearance="pose handhip face neutral", text="Так моя задница торчала правильно?")
    call process_character (k, appearance="pose handhip face neutral", text="Я не уверен на сто процентов.")
    call process_character (k, appearance="pose handhip face flirty", text="Я подумала, что ты сможешь мне скажешь.")
    call process_character (n, appearance="pose handpocket face embarrassed blush true")
    $ renpy.pause(1)
    call process_character (n, appearance="pose handpocket face embarrassed blush true", text="Она слегка выглядывала..")
    call process_character (k, appearance="pose armcross face neutral", text="То есть она торчала так,{w=1.0} что контур моей задницы можно было увидеть сквозь мои шорты?")
    call process_character (n, appearance="pose handpocket face curious blush true", text="...")
    call process_character (k, appearance="pose handhip face curious")
    $ k.c("Это важно " + n.say_name + ".")
    call process_character (k, appearance="pose handhip face curious", text="Я должна знать, что я правильно приседаю.")
    call process_character (n, appearance="pose behindhead face curious blush true", text="...")
    menu:
        "Я-я видел твою задницу сквозь шорты.":
            call process_character (k, appearance="pose armsup face neutral", text="Это было красиво, заметно и отчётливо?")
        "Т-твоя задница выглядела так, будто сейчас выскочит из твоих шорт.":
            call add_points (k, 1, tag="kira_convo_6_squats")
            call process_character (k, appearance="pose armsup face neutral", text="Неужели?")
            call process_character (k, appearance="pose armsup face neutral", text="Мои шорты довольно тесные.")
            call process_character (k, appearance="pose armsup face neutral", text="Я думал, что они порвутся.")


    call process_character (k, appearance="pose armsup face neutral")
    $ renpy.pause(1)
    call process_character (k, appearance="pose armsup face happy", text="Хорошо.")
    call process_character (k, appearance="pose armsup face happy", text="Просто хотела убедиться.")
    $ k.c("Спасибо, " + n.say_name + "!")


    call process_end_of_conversation ("kira_convo_6", k, priority=True, considered_scene=True)

    return


label kira_convo_7:
    call process_conversation_beginning ([ (n, ""), (k, "pose handhip face happy") ])

    call process_character (k, appearance="pose handhip face happy", text="Хорошо.{p=1.0}У тебя уже вставал?")
    call process_character (n, appearance="pose handpocket face curious", text="Что?")
    call process_character (k, appearance="pose armsup face neutral", text="Твоё полено.")
    call process_character (k, appearance="pose armsup face neutral", text="Как быстро ты кончил?")
    call process_character (n, appearance="pose handpocket face curious blush true", text="Ты говоришь о...")
    call process_character (k, appearance="pose armsup face happy", text="Дрочке?\nДа.")
    call process_character (n, appearance="pose behindhead face curious blush true", text="Нууу...{p=1.0}Я пытался.")
    call process_character (k, appearance="pose armcross face neutral", text="И?")
    call process_character (n, appearance="pose handpocket face flirty blush false", text="Это приятно.")
    call process_character (k, appearance="pose handhip face neutral", text="Сколько ты продержался?")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Ты имеешь в виду, когда...")
    $ renpy.pause(1)
    call process_character (n, appearance="pose handpocket face curious blush true", text="Белая штука вышла наружу?")
    call process_character (k, appearance="pose armcross face happy", text="Да, мужское молоко, хахаха.")
    call process_character (n, appearance="pose behindhead face curious blush true")
    $ renpy.pause(1)
    menu:
        "Это не заняло у меня много времени.":
            $ 1
        "Я думал о девушке, и тогда появилась белая штука.":
            call add_boldness (1, tag="kira_convo_7_manmilk")
            call process_character (k, appearance="pose armsup face happy", text="Ой.")
            call process_character (k, appearance="pose armsup face happy", text="(Бьюсь об заклад, это была я)")
            call process_character (k, appearance="pose armsup face happy", text="(Он просто слишком нервничает, чтобы признать это)")

    call process_character (k, appearance="pose handhip face neutral", text="Это впечатляет, что у тебя встаёт, после того как Мама застукала тебя.")
    call process_character (k, appearance="pose handhip face neutral", text="У большинства бы не встал.")
    call process_character (n, appearance="pose twohandfist face embarrassed blush true", text="Ты знаешь, что случилось?!")
    call process_character (k, appearance="pose armsup face happy", text="Ну, теперь-то точно знаю, ха-ха.")
    call process_character (n, appearance="pose handpocket face concerned blush true", text="...")
    call process_character (k, appearance="pose armsup face neutral", text="Мама этого не говорила об этом,")
    call process_character (k, appearance="pose armsup face neutral", text="но когда её лицо покраснело, это всё выдало.")
    call process_character (k, appearance="pose armsup face neutral", text="И она больше не хотела об этом говорить.")
    call process_character (n, appearance="pose handpocket face concerned blush true", text="...")
    call process_character (k, appearance="pose armcross face neutral", text="Может, твоя одноглазая змея напугала ее.")
    $ renpy.pause(1)
    call process_character (k, appearance="pose armcross face happy", text="Ты чудовище.")
    call process_character (n, appearance="pose twohandfist face embarrassed blush true", text="Ч-что?!")
    call process_character (k, appearance="pose armsup face happy", text="Ха-ха, я просто шучу!")
    call process_character (k, appearance="pose armsup face happy", text="Но в следующий раз запри дверь.")
    $ renpy.pause(1)
    call process_character (k, appearance="pose armsup face happy", text="(Хотя я бы не прочь взглянуть)")

    call process_end_of_conversation ("kira_convo_7", k, priority=True, considered_scene=True)

    return


label kira_convo_8:
    call process_conversation_beginning ([ (n, ""), (k, "pose handhip face happy") ])

    call process_character (k, appearance="pose handhip face happy", text="...")
    call process_character (n, appearance="pose handpocket face curious", text="...")
    call process_character (n, appearance="pose handpocket face curious", text="Что?")
    call process_character (k, appearance="pose armcross face happy", text="У тебя талант.")
    call process_character (n, appearance="pose handpocket face curious", text="Что?")
    call process_character (k, appearance="pose handhip face neutral", text="Ты справился с этим упражнением, как босс!")
    call process_character (n, appearance="pose behindhead face neutral", text="Я?")
    call process_character (k, appearance="pose armsup face neutral", text="В конце концов, ты станешь еще лучше.")
    call process_character (k, appearance="pose armsup face neutral", text="Ты будешь держаться дольше, двигаться быстрее...")
    call process_character (n, appearance="pose handpocket face neutral", text="Думаешь?")
    call process_character (k, appearance="pose handhip face curious", text="С таким руководителем, как я?")
    call process_character (k, appearance="pose handhip face curious", text="Конечно!")
    call process_character (k, appearance="pose armcross face neutral", text="Я тренирую людей, чтобы они выходили за рамки своих возможностей.")
    call process_character (k, appearance="pose armcross face neutral", text="Потому что если вы можете сделать лучше, чем сейчас...")
    call process_character (k, appearance="pose armcross face neutral", text="Тогда это означает, что вы всегда можете улучшить!")
    call process_character (n, appearance="pose handpocket face neutral", text="Д-да...")
    call process_character (n, appearance="pose twohandfist face happy", text="Да!")
    call process_character (n, appearance="pose twohandfist face happy", text="Ты права!")
    call process_character (k, appearance="pose armsup face neutral", text="Конечно...")
    call process_character (n, appearance="pose handfist face neutral", text="Я хочу стать ещё лучше и лучше!")
    call process_character (k, appearance="pose armcross face neutral", text="Хей, в тебе горит огонь, бро!")
    call process_character (k, appearance="pose armcross face neutral", text="Мне нравится!")
    call process_character (k, appearance="pose handhip face neutral", text="В следующий раз я постараюсь выжать всё до последней сочной капли...")
    call process_character (k, appearance="pose handhip face embarrassed", text="О, {w=0.5}придётся попотеть!")
    call process_character (n, appearance="pose handfist face embarrassed", text="{i}Сглатывает слюну{/i}")
    call process_character (n, appearance="pose handfist face embarrassed", text="(Возможно, я немного переборщил...)")

    call process_end_of_conversation ("kira_convo_8", k, priority=True, considered_scene=True)

    return

label kira_convo_9:
    call process_conversation_beginning ([ (n, ""), (k, "pose armsup") ])

    call process_character (k, appearance="pose armsup face neutral", text="Я в лучшей форме, чем когда-либо!")
    call process_character (n, appearance="pose handpocket face neutral", text="Да?")
    call process_character (k, appearance="pose handhip face neutral", text="Я могу посвятить больше времени тренировкам.")
    call process_character (k, appearance="pose handhip face neutral", text="В моей прошлой школе, я не всегда могла это делать.")
    call process_character (k, appearance="pose handhip face neutral", text="Ну, там домашнее задание и всё такое")
    call process_character (k, appearance="pose armsup face happy", text="То, что ты любишь.")
    call process_character (n, appearance="pose handpocket face curious", text="Ухх...")
    $ renpy.pause(1)
    call process_character (n, appearance="pose handpocket face neutral", text="Думаешь, снова будешь участвовать в Олимпийских играх?")
    call process_character (k, appearance="pose armcross face neutral", text="Трудно сказать.")
    call process_character (k, appearance="pose armcross face neutral", text="Хотя я тренировалась больше, чем когда-либо,")
    call process_character (k, appearance="pose armcross face neutral", text="Моя грудь никогда не станет меньше.")
    call process_character (k, appearance="pose handhip face neutral", text="Что, возможно, тебе известно, остановило меня в прошлом.")
    call process_character (n, appearance="pose handfist face neutral", text="Я думаю, у тебя получится!")
    call process_character (k, appearance="pose armsup face neutral", text="Хех...")
    call process_character (k, appearance="pose armsup face neutral", text="Наверное, стоит сначала проверить себя на местных соревнованиях.")
    call process_character (k, appearance="pose armcross face neutral", text="Нужно сделать себе репутацию в этом новом городе.")

    call process_end_of_conversation ("kira_convo_9", k, priority=False)

    return


label kira_convo_10:
    call process_conversation_beginning ([ (n, "outfit clothesjacket pose handpocket face neutral"), (k, "outfit underwear pose handhip face neutral") ])

    $ kira_convo_10_got_naked = False

    call process_character (n, appearance="pose handpocket face neutral", text="Эй [k.say_name].")
    call process_character (k, appearance="pose armcross face neutral", text="Хорошо выглядишь.")
    call process_character (k, appearance="pose armcross face neutral", text="Чья-то уверенность становится сильнее.")
    call process_character (n, appearance="pose behindhead face neutral", text="Что ты имеешь в виду?")
    call process_character (k, appearance="pose handhip face neutral", text="Ты ведешь себя круто и собранно,")
    call process_character (k, appearance="pose handhip face neutral", text="несмотря на то, что я в лифчике и трусиках.")

    menu:
        "Я начинаю привыкать к этому.":
            call process_character (n, appearance="pose handpocket face neutral")
            call process_character (k, appearance="pose armcross face neutral", text="Ну, в этом есть смысл.")
            call process_character (k, appearance="pose armcross face flirty", text="Ты видел меня какой я дикой могу быть..")
            call process_character (k, appearance="pose armcross face flirty", text="Для тебя это либо всё, либо ничего!")
            call process_character (n, appearance="pose handpocket face curious blush true", text="...")
            pass
        "Ну, если бы ты была голой...":
            call add_boldness (1, tag="kira_convo_10_naked")
            call process_character (n, appearance="pose behindhead face curious")
            call process_character (k, appearance="pose armsup face happy", text="Хо-хо-хо!")
            call process_character (k, appearance="pose armsup face happy", text="Переходишь сразу к делу!")

            call character_leave_dissolve (k)
            $ renpy.pause(1)

            $ kira_convo_10_got_naked = True

            call process_character (k, appearance="outfit nude pose armsup face flirty", text="Как дела, маленький извращенец?")
            call process_character (n, appearance="pose behindhead face embarrassed blush true", text="...")

            call process_character (n, appearance="outfit clothesjacket_hard pose behindhead face embarrassed blush true", show_bust=False)
            $ refresh_character(n, force_transition = Dissolve(1.0))
            pause 0.5

            call process_character (k, appearance="pose handhip face happy", text="Вот румянец, который я хорошо знаю!!")
            call process_character (k, appearance="pose handhip face happy", text="Это потому, что твой член помнит все груди, которые видел..")
            call process_character (n, appearance="pose behindhead face curious blush true", text="...")
            call process_character (n, appearance="pose behindhead face curious blush true", text="Я...")
            call process_character (n, appearance="pose behindhead face curious blush true", text="Держу его под контролем")
            call process_character (k, appearance="pose armcross face happy", text="Конечно, конечно...")

    call process_character (k, appearance="pose handhip face neutral", text="Так теперь я хочу быть уверена, что ты знаешь, к чему всё это.")
    call process_character (n, appearance="pose behindhead face neutral blush true", text="Эмм, ну да, конечно......")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Ты же о новых упражнениях!")
    call process_character (k, appearance="pose handhip face embarrassed", text="(А может быть, нет...)")
    call process_character (k, appearance="pose handhip face embarrassed", text="...")
    call process_character (k, appearance="pose handhip face embarrassed", text="Ну, да {w=1.0}конечно.")
    call process_character (n, appearance="pose handfist face happy", text="Я никогда не делал упражнений, от которых мне так хорошо!")
    call process_character (n, appearance="pose handfist face happy", text="Обычно я чувствую, что всё болит или очень устал после тренировки...")
    call process_character (n, appearance="pose handfist face happy", text="Но те, что ты придумала сестренка, совсем не такие!")
    call process_character (k, appearance="pose armcross face embarrassed", text="(Я думаю, ты даже не понимаешь, что это на самом деле...)")
    call process_character (k, appearance="pose armcross face embarrassed", text="(Должна ли я продолжать обводить вокруг пальца?)")
    call process_character (k, appearance="pose armcross face happy", text="(Я должна сказать ему, что мне нравится играть с его членом...)")
    call process_character (k, appearance="pose armcross face happy", text="...")
    call process_character (k, appearance="pose handhip face curious", text="(Возьми себя в руки [k.say_name]!)")
    call process_character (k, appearance="pose handhip face curious", text="(Я не могу просто сказать ему это!)")
    call process_character (k, appearance="pose handhip face embarrassed", text="(Я оставлю брата в блаженном неведении...)")

    $ quick_menu = False
    window hide
    $ clear_characters()
    show bg white
    with Dissolve(1.0)
    $ renpy.pause(1.0)
    $ renpy.show_screen("dream_blur")

    show bg kitchen_daytime
    with Dissolve(1.0)

    $ display_multiple_characters([ (n, "outfit clothesjacket pose twohandfist face neutral"), (si, "outfit clothes pose handsfront face neutral") ])

    $ quick_menu = True
    call process_character (n, appearance="pose twohandfist face neutral", text="Привет, Мам!")
    call process_character (si, appearance="pose handsfront face neutral", text="Привет [n.say_name].")
    call process_character (si, appearance="pose handsfront face neutral", text="Что ты задумал?")
    call process_character (n, appearance="pose handfist face neutral", text="Нуу, [k.say_name] сказала, чтобы я продолжил играть со своим членом!")
    call process_character (si, appearance="pose armunder face embarrassed blush true", text="Что она?!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Да!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Ты не поверишь, что она со мной сделала!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Это было, как мяч для гольфа через садовый шланг!")
    call process_character (si, appearance="pose handsup face angry blush true")
    $ si.c(k.say_name.upper() + "!!!")

    $ quick_menu = False
    window hide
    $ clear_characters()
    show bg white
    with Dissolve(1.0)
    $ renpy.pause(1.0)
    $ renpy.scene('screens')

    if week.time == "day":
        show bg kira_room_daytime
        with Dissolve(1.0)
    else:
        show bg kira_room_evening
        with Dissolve(1.0)


    if kira_convo_10_got_naked:
        $ display_multiple_characters([ (n, "outfit clothesjacket_hard pose handpocket face neutral"), (k, "outfit nude pose armcross face embarrassed") ])
    else:
        $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral"), (k, "outfit underwear pose armcross face embarrassed") ])

    $ quick_menu = True
    call process_character (k, appearance="pose armcross face embarrassed", text="(Да, это пока не закончится...)")
    call process_character (k, appearance="pose armsup face neutral", text="(По крайней мере, если он скажет про упражнения, я могу ускользнуть от этого)")
    call process_character (k, appearance="pose armsup face neutral", text="(\"О, это [n.say_name] и его больные фантазии!\")")
    call process_character (n, appearance="pose behindhead face concerned", text="[k.say_name], ты в порядке?")
    call process_character (k, appearance="pose handhip face neutral", text="О, прекрасно, бро")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (k, appearance="pose armcross face neutral", text="Я как раз думала о новых упражнениях.")
    call process_character (k, appearance="pose armcross face neutral", text="Ты должен все обдумать, понимаешь?")
    call process_character (n, appearance="pose twohandfist face happy", text="О, круто!!")
    call process_character (n, appearance="pose twohandfist face happy", text="Я не могу дождаться, чтобы попробовать что-то новое!")



    call process_end_of_conversation ("kira_convo_10", k, priority=True, considered_scene=True)

    return



label kira_convo_11:
    call process_conversation_beginning ([ (n, "outfit clothes pose handsdown face neutral"), (k, "outfit clothes pose armsup face neutral") ])

    call process_character (k, appearance="pose armsup face neutral", text="Фу, сегодня жарковато!")
    call process_character (n, appearance="pose handsdown face neutral", text="Да.")
    call process_character (n, appearance="pose handsdown face neutral", text="Я уже ходил в бассейн несколько раз.")
    call process_character (k, appearance="pose handhip face neutral", text="Я тоже.")
    call process_character (k, appearance="pose handhip face neutral", text="Несмотря на то, что у нас есть кондиционер, он едва помогает.")
    call process_character (n, appearance="pose behindhead face concerned", text="Да, ненавижу чувствовать себя потной дома.")
    call process_character (k, appearance="pose armcross face neutral", text="Если мы пойдем сегодня на пробежку, нам надо будет взять много воды..")
    call character_leave_dissolve (k)
    call process_character (si, appearance="outfit yoga pose handsfront face neutral")
    call process_character (n, appearance="pose behindhead face neutral")

    call process_character (si, appearance="outfit yoga pose handsfront face neutral", text="Эй, дети.")
    "[k.say_name] & [n.say_name]" "Привет, Мама."
    call process_character (si, appearance="outfit yoga pose handsup face neutral", text="Я только что заходила к твоей сестре [sa.say_name].")
    call process_character (si, appearance="outfit yoga pose handsup face happy", text="У нее вентилятор дует на полную.")
    call process_character (si, appearance="outfit yoga pose handsup face happy", text="Она даже не хочет вставать с места, в такую погодой.")
    call character_leave_dissolve (n)
    call process_character (k, appearance="position right pose handhip face neutral", text="Не могу винить ее.")
    call process_character (si, appearance="outfit yoga pose armunder face neutral", text="Так чем вы двое занимались?")
    call process_character (k, appearance="position right pose armsup face neutral", text="Эх, да ни чем.")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose handfist face neutral", text="Мы много бегали и бегали!")
    call process_character (n, appearance="pose handfist face neutral", text="Мы подумывали, что можно ещё сделать сегодня.")
    call process_character (si, appearance="outfit yoga pose armunder face curious", text="Черт возьми, я была бы очень осторожна в такую жару.")
    call process_character (si, appearance="outfit yoga pose armunder face curious", text="Я не хочу, чтобы кто-то из вас получил тепловой удар.")
    call character_leave_dissolve (n)
    call process_character (k, appearance="position right pose armcross face neutral", text="Мы так и не решили...")
    call process_character (k, appearance="position right pose armcross face neutral", text="Можем просто останемся дома.")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose twohandfist face neutral", text="Мы всегда можем сделать упражнения и в доме!")
    call process_character (si, appearance="outfit yoga pose handsup face happy", text="Я никогда не видела, чтобы ты так волновалась об упражнениях, [n.say_name]!")
    call process_character (n, appearance="pose handfist face happy", text="[k.say_name], у нас большая программа упражнений.")
    call process_character (si, appearance="outfit yoga pose handsup face happy", text="Ты - чудо-женщина [k.say_name]!")
    call process_character (si, appearance="outfit yoga pose handsup face happy", text="Чтобы твой брат был так рад тренировкам.")
    call process_character (si, appearance="outfit yoga pose handsfront face neutral", text="Как тебе удалось это?")
    call character_leave_dissolve (n)
    call process_character (k, appearance="position right pose armsup face embarrassed", text="О, ну это...")
    call process_character (k, appearance="position right pose armsup face embarrassed", text="...")
    call process_character (k, appearance="position right pose armsup face embarrassed", text="Они включают в себя {w=1.0}двигательные упражнения.")
    call process_character (k, appearance="position right pose armsup face embarrassed", text="Множество движений вперёд-назад, да [n.say_name]?")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose twohandfist face neutral", text="О, определенно!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Это самая лучшая часть из них!")
    call process_character (si, appearance="outfit yoga pose handsup face happy", text="Ну, я и говорю, так держать!")
    call process_character (si, appearance="outfit yoga pose handsup face happy", text="[n.say_name] нуждается в здоровом перерыве от всех этих видеоигр.")
    call process_character (n, appearance="pose handfist face neutral", text="[k.say_name] сделал мне массаж недавно")
    call process_character (si, appearance="outfit yoga pose handsup face neutral", text="О, твоя сестра - профессионал в этом!")
    call process_character (si, appearance="outfit yoga pose handsup face neutral", text="Всякий раз, когда у меня болит шея или спина, она та, к кому нужно идти за облегчением!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Да, она знает своё дело!")
    call process_character (n, appearance="pose twohandfist face neutral", text="{cps=40}Было здорово, когда она массировала мой п-{/cps}{w=0.75}{nw}")
    call character_leave_dissolve (n)
    call process_character (k, appearance="position right pose armcross face embarrassed blush true", text="Нет необходимости постоянно напоминать мне, как я хороша в этом!")
    call process_character (si, appearance="outfit yoga pose armunder face happy", text="[k.say_name], точно.")
    call process_character (si, appearance="outfit yoga pose armunder face happy", text="Я говорила ей это бесчисленное количество раз!")
    call process_character (k, appearance="position right pose armsup face embarrassed blush true", text="...")
    call process_character (si, appearance="outfit yoga pose handsfront face neutral", text="Ну, а я собираюсь пропотеть сама, с помощью йоги.")
    call process_character (si, appearance="outfit yoga pose handsfront face neutral", text="Просто убедитесь, что пьете много воды.")
    call process_character (si, appearance="outfit yoga pose handsfront face neutral", text="Легко получить обезвоживание!")
    call character_leave_dissolve (k)
    call process_character (n, appearance="pose handsdown face neutral", text="Хорошо, Мам!")
    call character_leave_dissolve (si)
    call process_character (k, appearance="position left pose handhip face embarrassed blush false", text="...")
    call process_character (k, appearance="position left pose handhip face embarrassed blush false", text="(Черт, это было близко)")
    call process_character (k, appearance="position left pose handhip face embarrassed blush false", text="...")
    call process_character (n, appearance="pose behindhead face concerned", text="Ты в порядке [k.say_name]?")
    call process_character (k, appearance="position left pose armcross face embarrassed blush false", text="...")
    call process_character (k, appearance="position left pose armcross face embarrassed blush false", text="Эй...")
    call process_character (k, appearance="position left pose armcross face embarrassed blush false", text="Будь осторожен, когда говоришь о моем...")
    call process_character (k, appearance="position left pose armcross face embarrassed blush false", text="...")
    call process_character (k, appearance="position left pose armcross face embarrassed blush false", text="Супер {w=0.5}секретной {w=0.5}техники массажа.")
    call process_character (n, appearance="pose behindhead face curious", text="Секретная техника массажа?")
    call process_character (k, appearance="position left pose armcross face embarrassed blush false", text="Охх...")
    call process_character (k, appearance="position left pose armcross face neutral blush false", text="Да, да, да, ну ты знаешь...")
    call process_character (k, appearance="position left pose armcross face neutral blush false", text="Эти массажи и упражнения совершенно секретны.")
    call process_character (k, appearance="position left pose armcross face neutral blush false", text="Их нужно держать в секрете.")
    call process_character (n, appearance="pose twohandfist face neutral", text="Совершенно секретно?")
    call process_character (n, appearance="pose twohandfist face neutral", text="Правда?")
    call process_character (k, appearance="position left pose armsup face neutral blush false", text="Вот именно!")
    call process_character (k, appearance="position left pose armsup face neutral blush false", text="Ты единственный, на ком я их тестировала.")
    call process_character (k, appearance="position left pose armsup face neutral blush false", text="И только ты знаешь о них.")
    call process_character (n, appearance="pose behindhead face happy", text="Вау, так круто!")
    call process_character (k, appearance="position left pose armsup face neutral blush false", text="Да! Очень Круто!")
    call process_character (k, appearance="position left pose armsup face neutral blush false", text="Я... {w=1.0}хочу создать самую великую тренировку всех времен!")
    call process_character (k, appearance="position left pose handhip face neutral blush false", text="Но мне нужно, чтобы ты держала это в тайне.")
    call process_character (k, appearance="position left pose handhip face neutral blush false", text="Если кто-нибудь спросит, мама или [sa.say_name]...")
    call process_character (k, appearance="position left pose handhip face neutral blush false", text="Просто скажи им, что ты просто делаешь со мной упражнения.")
    call process_character (k, appearance="position left pose handhip face neutral blush false", text="Но не выдавай никаких подробностей!")
    call process_character (k, appearance="position left pose handhip face neutral blush false", text="...")
    call process_character (k, appearance="position left pose armsup face neutral blush false", text="Могу я тебе доверять, бро?")
    call process_character (k, appearance="position left pose armsup face neutral blush false", text="Ты никогда не расскажешь о моих супер секретных техниках массажа и тренировках?")
    call process_character (n, appearance="pose handfist face happy", text="Рассчитывай на меня!")
    call process_character (k, appearance="position left pose armcross face embarrassed blush false", text="...")
    call process_character (k, appearance="position left pose armcross face embarrassed blush false", text="(Как мне удалось это провернуть?)")
    call process_character (k, appearance="position left pose armcross face embarrassed blush false", text="...")
    call process_character (k, appearance="position left pose armcross face embarrassed blush false", text="(Я надеюсь, что мой брат сдержит свое слово...)")

    call process_end_of_conversation ("kira_convo_11", k, priority=True, considered_scene=True)

    return

label kira_convo_12:
    call process_conversation_beginning ([(n, "pose handpocket face neutral blush false"), (k, "pose handhip face neutral blush false")])
    call process_character (k, appearance="pose handhip face neutral blush false", text="Ты был в парке?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Да, я ходил туда ночью.")
    call process_character (k, appearance="pose armcross face neutral blush false", text="Иногда я хожу туда рано утром.")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Там есть хорошие беговые дорожки.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Ты видела весь парк?")
    call process_character (k, appearance="pose handhip face neutral blush false", text="Не уверена")
    call process_character (k, appearance="pose handhip face happy blush false", text="Каждый раз, когда я думаю, что добралась до конца, появляется новая дорожка!")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Как долго бегаешь?")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Ох, наверное, час или около того.")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="Час пробежки?!")
    call process_character (k, appearance="pose armcross face happy blush false", text="Ха-ха, я бегаю там не так быстро как с тобой, [n.say_name]!")
    call process_character (n, appearance="pose behindhead face curious blush false")
    call process_character (k, appearance="pose armcross face neutral blush false", text="Это бег на выносливость.")
    call process_character (k, appearance="pose armcross face neutral blush false", text="В нём меньше скорость, и больше того, чтобы увидеть, как далеко я могу зайти.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="О, хорошо..")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Интересно, смогу ли я это сделать!")
    call process_character (k, appearance="pose handhip face neutral blush false", text="Я уверена, что ты сможешь.")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Но вам придется меньше играть в видеоигры, чтобы больше тренироваться.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Хм, если подумать...")
    call process_character (k, appearance="pose armsup face happy blush false", text="Я думаю, что кратковременные упражнения - это твой стиль.")


    call process_end_of_conversation ("kira_convo_12", k, priority=False)

    return

label kira_convo_13:
    call process_conversation_beginning ([(n, " pose handpocket face neutral blush false"), (k, " pose handhip face neutral blush false")])
    call process_character (k, appearance="pose handhip face neutral blush false", text="Однажды я действительно схожу на пляж.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Я тоже..")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Может, мы с тобой найдём морские стекляшки для мамы.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Морские стекляшки?")
    call process_character (k, appearance="pose armcross face neutral blush false", text="Ты никогда не слышал о морских стекляшках?")
    call process_character (k, appearance="pose armcross face neutral blush false", text="Они красивые")
    call process_character (k, appearance="pose handhip face neutral blush false", text="Это красивое, гладкое стекло раскиданное вдоль береговой линии.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Откуда оно все берется?")
    call process_character (k, appearance="pose armsup face happy blush false", text="Наверное, от парней, бросающих бутылки от пива в океан.")
    call process_character (n, appearance="pose handpocket face neutral blush false")
    call process_character (k, appearance="pose armsup face happy blush false", text="Бутылка проходит путь от хранения алкоголя до украшения.")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Думаешь, мы сможем найти какое-нибудь сокровище?")
    call process_character (k, appearance="pose handhip face neutral blush false", text="Кто знает?")
    call process_character (n, appearance="pose twohandfist face neutral blush false")
    call process_character (k, appearance="pose armcross face neutral blush false", text="Может быть, если повезет, ты найдёшь ожерелье или кольцо.")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Да, да!")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Редкий шанс, что ты найдёшь что-то подобное невооруженным глазом.")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Но знаешь...")
    call process_character (k, appearance="pose armsup face happy blush false", text="Было ничьё, стало твоё!")


    call process_end_of_conversation ("kira_convo_13", k, priority=False)

    return

label kira_convo_14:
    call process_conversation_beginning ([(n, " pose handpocket face neutral blush false"), (k, " pose handhip face curious blush false")])
    call process_character (k, appearance="pose handhip face curious blush false", text="[n.say_name], эй...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Что?")
    call process_character (k, appearance="pose armcross face curious blush false", text="Если ты дёргаешь себя за хвост в ванной, хотя бы приберись после этого.")
    call process_character (n, appearance="pose behindhead face embarrassed blush false", text="!")
    call process_character (k, appearance="pose handhip face concerned blush false", text="На полу остались следы спермы.")
    call process_character (k, appearance="pose handhip face concerned blush false", text="Я все ещё чувствую этот запах.")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="П-Прости..")
    call process_character (n, appearance="pose behindhead face concerned blush true", text="В следующий раз уберусь получше.")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Я думаю, было бы проще просто кончить в унитаз.")
    call process_character (k, appearance="pose armsup face neutral blush false", text="И никакой шумихи.")
    call process_character (n, appearance="pose handpocket face curious blush true", text="Я... В следующий раз так и сделаю...")
    call process_character (k, appearance="pose armcross face curious blush false", text="С другой стороны...")
    call process_character (k, appearance="pose armcross face curious blush false", text="Возможно, это не лучшая идея.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Почему?")
    call process_character (k, appearance="pose armcross face embarrassed blush false", text="Если ты забудешь поднять сиденье, и один из нас сядет на него...")
    call process_character (k, appearance="pose armcross face embarrassed blush false", text="Кто-то будет с липкой задницей.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")


    call process_end_of_conversation ("kira_convo_14", k, priority=False)

    return

label kira_convo_15:
    call process_conversation_beginning ([(n, " pose handpocket face neutral blush false"), (k, " pose armcross face neutral blush false")])
    call process_character (k, appearance="pose armcross face neutral blush false", text="Забавно, как часто пялятся на мои сиськи.")
    call process_character (k, appearance="pose armcross face happy blush false", text="И я имею в виду не только тебя.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="О-Ох?")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Когда парни пялятся, всё с ними ясно")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Они просто глазеют и находятся в оцепенении.")
    call process_character (k, appearance="pose armsup face happy blush false", text="Когда девушки смотрят это более забавно.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Девушки тоже смотрят на твою грудь?")
    call process_character (k, appearance="pose handhip face neutral blush false", text="Не таращатся, но смотрят.")
    call process_character (k, appearance="pose handhip face neutral blush false", text="В спортзале, так постоянно.")
    call process_character (k, appearance="pose armcross face neutral blush false", text="Моя теория - девушки думают, что они не настоящие.")
    call process_character (k, appearance="pose armcross face happy blush false", text="Или, может быть, это женская зависть.")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Наверное, они хотят сжать их, чтобы понять настоящие ли.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Ты думаешь, что они это сделают?")
    call process_character (k, appearance="pose armcross face happy blush false", text="Нуу, спроси себя сам, [n.say_name]?")
    call process_character (n, appearance="pose handpocket face embarrassed blush false", text="...")
    call process_character (k, appearance="pose armsup face neutral blush false", text="Ты бы не отказался от такой возможности?.")
    call process_character (k, appearance="pose handhip face neutral blush false", text="Посжимать сиськи случайной девушки??")
    call process_character (k, appearance="pose handhip face happy blush false", text="Я знаю, я бы не отказалась!")


    call process_end_of_conversation ("kira_convo_15", k, priority=False)

    return