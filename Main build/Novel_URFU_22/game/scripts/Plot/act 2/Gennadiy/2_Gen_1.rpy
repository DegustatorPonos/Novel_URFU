define GenCoffe = False
define GenQuestions = 0

label act2_Gen_meet2:
    "Вы выключаете компьютер."
    "В офисе тихо - все давно закончили рабочий день."
    "Вы смотрите на часы - 21:50."
    "Вы собираетесь домой, но слышите приглушённое, учащённое дыхание."
    "Вы идёте на звук и видите Геннадия БорисовичЪа."
    "Он лежит на стуле и глубоко, болезненно дышит."
    scene GenBG
    show MCIdle at left
    show GenSad:
        xalign 1.0
        xzoom -1.0
    mainChar "Геннадий БорисовичЪ, с Вами всё хорошо?"
    if GenAtt < 0:
        jump Gen_2_BadPath
    else:
        jump Gen_2_GoodPath
    
label Gen_2_BadPath:
    Gennadiy "Не твоё дело."
    Gennadiy "С чего бы тебе волноваться обо мне?"
    Gennadiy "Я б тебя проигнорил, держу в курсе."
    menu:
        "Съязвить":
            $GenAtt -= 1
            mainChar "Да меня и не волнует, но возиться с трупом не хочется"
            Gennadiy "Не, тебе от меня так просто не избавиться."
            Gennadiy "Я вас всех ещё переживу."
            "Геннадий пытается посмеяться, но это выглядит болезненно."
            Gennadiy "Короче сердце у меня немного прихватило..."
            Gennadiy "Ты не подождёшь тут, вдруг всё-таки ошибся?"
        "Ответить нейтрально":
            $GenAtt += 1
            mainChar "А почему меня не должно волновать состояние моего коллеги?"
            Gennadiy "Да, зря я так..."
            Gennadiy "Короче сердце у меня немного прихватило..."
            Gennadiy "Ты не подождёшь тут, вдруг в этот раз помру?"
    menu:
        "Отказаться":
            $GenAtt -= 2
            Gennadiy "Ну ладно, сам разберусь.{w} Удачи, давай."
            mainChar "Давайте..."
            hide MCIdle
            hide GenSad
            scene bg_bbg
            return
        "Сказать, что торопитесь":
            Gennadiy "А, ну раз дела срочные - не держу."
            Gennadiy "Да и, как говорил, моё здоровье - не твои проблемы."
            Gennadiy "Удачи, Давай."
            menu:
                "Уйти":
                    hide MCIdle
                    hide GenSad
                    scene bg_bbg
                    return
                "Передумать":
                    mainChar "А вообще, дела подождут"
                    Gennadiy "Ну, спасибо, полагаю..."
        "Согласиться":
            $GenAtt += 1
            mainChar "Да, почему бы и нет?"
            Gennadiy "Спасибо огромное."
            Gennadiy "Если что, труп можешь тут бросить - не обижусь, слово даю."
            "Геннадий пытается посмеяться, но от этого лишь хватается за грудь."
    "Вы садитесь на соседний стул."
    jump Gen_2_quesions

label Gen_2_GoodPath:
    Gennadiy "Сердце чёт прихватило."
    Gennadiy "Давай, иди домой, всё нормально будет."
    Gennadiy "Если для тебя, конечно, нормально не значит, что я умру..."
    "Геннадий пытается посмеяться, но от этого лишь хватается за грудь."
    Gennadiy "Слушай, тут вот такой моментик..."
    Gennadiy "Ты не подождёшь, пока я отойду?"
    Gennadiy "А то мало ли я очень неудачно пошутил..."
    menu:
        "Отказаться":
            $GenAtt -= 2
            Gennadiy "Ну, дело твоё."
            Gennadiy "Кто я, чтобы тебя заставлять?"
            Gennadiy "Давай, удачи."
            menu:
                "Уйти":
                    mainChar "Давайте..."
                    hide MCIdle
                    hide GenSad
                    scene bg_bbg
                    return
                "Передумать":
                    mainChar "А знаете, я передумал..."
                    hide GenSad
                    show GenIdle:
                        xalign 1.0
                        xzoom -1.0
                    Gennadiy "Ну, спасбо, полагаю..."
        "Согласиться":
            mainChar "Да, почему нет?"
            hide GenSad
            show GenSmile:
                xalign 1.0
                xzoom -1.0
            Gennadiy "Спасибо, парень."
            Gennadiy "Реально благодарен."
        "Вы садитесь на соседний стул."
    if GenAtt < 0:
        jump Gen_2_quesions
        return
    Gennadiy "Слушай, я, может, наглею, но ты не мог бы передать мне телефон?"
    Gennadiy "Я слышал уведомления, но не дотянулся..."
    Gennadiy "Он на столе лежит."
    mainChar "Да, конечно."
    "Вы тянетесь за телефоном и видите пустую банку кофе."
    mainChar "Геннадий, а это не та банка, которую вы у Евгения Викторовича брали недавно?"
    Gennadiy "Нет, это новая."
    Gennadiy "Та на столике с чайником."
    mainChar "То есть Вы покупаете себе отдельно?"
    Gennadiy "Да."
    Gennadiy "Поверь, если бы я каждый раз ходил за кофе к столик, я бы у всех уже в печёнках сидел."
    mainChar "Подождите."
    mainChar "Сколько кофе вы выпили сегодня?"
    Gennadiy "В районе шести кружек, может семь."
    menu:
        "Упрекнуть":
            $GenCoffe = True
            $GenAtt += 1
            mainChar "Ну, неудивительно, что вы сейчас умираете..."
            Gennadiy "Да, есть косячок."
            Gennadiy "Надо бы слезать с кофеина..."
            Gennadiy "Как там мой телефон, кстати?"
            mainChar "А, да"
        "Проигнорировать это":
            $GenAtt -= 1
            mainChar "Ну, надеюсь, Вы знаете, что делаете..."
            Gennadiy "Сам не уверен."
            Gennadiy "Ну, это не важно."
    "Вы берёте телефон Геннадия и передаёте ему."
    "Он проверяет сообщения."
    Gennadiy "Ха, чего я ожидал..."
    Gennadiy "Спам, как всегда."
    "Геннадий выключает телефон и кладёт его на свой стол."
    jump Gen_2_quesions

label Gen_2_quesions:
    "В комнате воцриласть тишина."
    while GenQuestions < 2:
        menu:
            "Вы всегда такой недовольный?":
                $GenAtt -= 1
                $GenQuestions += 1
                mainChar "Вы всегда такой недовольный?"
                hide GenIdle
                hide GenSad
                hide GenSmile #блять, обидно, что говнокод, но переделывать уже поздно
                show GenSad:
                    xalign 1.0
                    xzoom -1.0
                Gennadiy "А ты всегда такой наглый?"
                Gennadiy "Короче, дам совет."
                Gennadiy "Если хочешь человека оскорбить - делай это прямо."
            "Не хотите выпить на выходных?":
                $GenAtt -= 2    
                $GenQuestions += 1
                mainChar "Не хотите выпить на выходных?"
                hide GenIdle
                hide GenSad
                hide GenSmile #блять, обидно, что говнокод, но переделывать уже поздно
                show GenSad:
                    xalign 1.0
                    xzoom -1.0
                if GenAtt < 0:
                    Gennadiy "Знаешь, в мире не так много вещей которые у меня вызывают отвращение."
                    Gennadiy "Но одна из них - это пьющие."
                    Gennadiy "Тебе реально доставляет сидеть в бесконтрольном состоянии?"
                    Gennadiy "На это же даже смотреть мерзко."
                    Gennadiy "Так что давай без этого всего."
                else:
                    Gennadiy "Ты сам пьёшь?"
                    mainChar "Ну бывает."
                    Gennadiy "Вот чисто дружеский совет - бросай ты это дерьмо."
                    Gennadiy "Ты, конечно, не пятнадцатилетний пацан, да и я не батя твой..."
                    Gennadiy "Но я могу несколько часов рассказывать тру стори про алкашку."
                    Gennadiy "Но поверь, ты не захочешь сидеть и слушать."
                    Gennadiy "Надеюсь, ты понял."
            "Почему Вы задерживаетесь на работе?":
                mainChar "Почему Вы задерживаетесь на работе?"
                $GenQuestions += 1
                $GenAtt += 1
                hide GenIdle
                hide GenSad
                hide GenSmile #блять, обидно, что говнокод, но переделывать уже поздно
                show GenIdle:
                    xalign 1.0
                    xzoom -1.0
                Gennadiy "А что мне ещё делать?"
                Gennadiy "Бесцельно в экран пялиться я и на рабочем месте могу."
                Gennadiy "А на остальное сил уже не остаётся."
                Gennadiy "Или не хочется."
                Gennadiy "По разному бывает."
            "А чем Вы на досуге занимаетесь?":
                $GenQuestions += 1
                $GenAtt += 1
                mainChar "А чем Вы на досуге занимаетесь?"
                hide GenIdle
                hide GenSad
                hide GenSmile #блять, обидно, что говнокод, но переделывать уже поздно
                show GenIdle:
                    xalign 1.0
                    xzoom -1.0
                Gennadiy "Ну чем обычный человек занят?"
                Gennadiy "Иногда сплю, иногда ем."
                Gennadiy "Музыку ещё люблю, но это так, для души."
                mainChar "То есть постоянных хобби нет?"
                Gennadiy "На них, понимаешь, надо выделять человекочасы."
                Gennadiy "У меня их нет почти."
                Gennadiy "Так что и хобби нет."
            "Сидеть в тишине":
                $GenQuestions += 10
                "Вы решаете просто посидеть."
    #========================================#
    Gennadiy "Фух, ну ладно, вроде получше."
    "Геннадий с трудом встаёт из кресла и протягивает Вам руку."
    Gennadiy "Спасибо, что помог.{w} Реально благодарен."
    mainChar "Да не за что."
    if GenCoffe:
        mainChar "И заканчивайте с кофе в таких объёмах."
        mainChar "Реально ведь окочуритесь."
        Gennadiy "Ладно, посмотрим."
    hide GenIdle
    hide GenSad
    hide GenSmile #блять, обидно, что говнокод, но переделывать уже поздно
    show GenIdle:
        xalign 1.0
        xzoom -1.0
    Gennadiy "Ну, ты как хочешь, но я домой."
    Gennadiy "Давай, удачи."
    mainChar "Давайте."
    hide GenIdle
    hide MCIdle
    scene bg_bbg
    return