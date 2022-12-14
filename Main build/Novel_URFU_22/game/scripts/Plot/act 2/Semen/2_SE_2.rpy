label act2_Semen_meet3():
    "Вы заходит в кабинет к Евгению Викторовичу."
    scene EVBG
    show EVcalm at right
    show SemSad
    if EVatt > -0.5: 
        EV "Ты как будто специально портишь себе репутацию в глазах коллектива. Не думайте что Галина сможет вас все время выкручивать, рано или поздно...{w} Здравствуй, [NameSpace]."
        jump Semen_meet3_good
    else:
        EV "Ты как будто специально портишь себе репутацию в глазах коллектива. Не думайте что Галина сможет вас все время выкручивать, рано или поздно...{w} Чего уши греем? Стучаться не учили?"
        jump Semen_meet3_bad
    return

label Semen_meet3_bad():
    menu:
        "Что случилось?":
            jump Semen_meet3_good

        "Зайду позже":
            mainChar "Ладно, я зайду чуть позже."
            if $SAtt < 0.5:
                $SAtt -= 2
            jump Semen_meet3_end
            return

label Semen_meet3_good():
    show MCIdle at left
    mainChar "Добрый день, что то случилось?"
    EV "Да вот товарища вашего отчитываю. сколько это, Семен, будет еще повторяться?"
    Semen "Дак проблема то не во мне! Разве я виноват в том, что кто то просто не может заткнуться когда просят?"
    menu:
        "Саня нарывется":
            jump Semen_meet3_good_1

        "Ну Семен ты тоже хорош...":
            jump Semen_meet3_good_2

        "...":
            jump Semen_meet3_good_3
    return

label Semen_meet3_good_1():
    mainChar "Евгений Викторович, Саня сам нарывается, это ведь ненормально, зная характер Семена, выводить его из себя."
    EV "Я все понимаю, но раз за разом устраивать такие скандалы, это недопустимо! Сроки горят а мы тут отношения выясняем!"
    menu:
        "Вы правы":
            jump Semen_meet3_good_2

        "Может заняться источником проблем?":
            pass
    mainChar "Дак а из-за кого отношения то выясняются? Вы собрались характер Семена менять? Вам не проще заняться источником проблемы?"
    $SAtt += 1
    EV "Хорошо, с Александром я тоже беседу проведу, но вы Семен учтите, что терпение коллектива небезграничное и долго вас терпеть никто не будет. Если вопросов нет - свободен."
    hide SemSad
    EV "По какому вопросу зашел?"
    hide EVcalm
    hide MCIdle
    scene bg_bbg with dissolve
    "Спустя время"
    scene HallBG with dissolve
    show MCIdle at left
    show SemIdle at right
    if SAtt >0:
        Semen "Спасибо тебе конечно, но не стоило уж тебе меня отмазывать, сам бы во всем разобрался."
        mainChar "Да ладно тебе."
        $SAtt += 2
        jump Semen_meet3_end
    else:
        Semen "Не думай что я о тебе теперь лучшего мнения, не встревай не в свои терки, лады?"
        Semen "...Но все равно спасибо, что отмазал."
        $SAtt += 1
        jump Semen_meet3_end
    return

label Semen_meet3_good_2():
    mainChar "Нет ну Семен ты тоже хорош, скандал на ровном месте разводить."
    if SAtt < 0:
        Semen "Ты ведь нарываешься..."
        EV "А ну, замолчали оба! Учтите Семен, что терпение коллектива небезграничное и долго вас здесь терпеть никто не будет. Если вопросов нет - свободен."
        hide SemSad
        EV "По какому вопросу зашел?"
        $SAtt -= 2
        jump Semen_meet3_end
    Semen "..."
    EV "Вот именно, раз за разом устраивать такие скандалы, это недопустимо! Сроки горят а мы тут отношения выясняем!"
    menu:
        "Но не только в нем проблема...":
            jump Semen_meet3_good_1

        "Нужно меняться":
            mainChar "Ты можешь до посинения со всеми спорить, но пока сам не начнешь меняться отношение к тебе не улучшится."
    EV "Учтите Семен, что терпение коллектива небезграничное и долго вас терпеть никто не будет. Если вопросов нет - свободен."
    hide SemSad
    EV "По какому вопросу зашел?"
    hide EVcalm
    hide MCIdle
    scene bg_bbg with dissolve
    "Спустя время"
    scene HallBG with dissolve
    show MCIdle at left
    show SemIdle at right
    Semen "Ну ты и крыса, не ожидал от тебя такого. Еще раз так в разговор встрянешь - влетит конкретно."
    $SAtt -= 2
    jump Semen_meet3_end
    return

label Semen_meet3_good_3():
    mainChar "..."
    EV "Если вы, Семен, дорожите своим местом, то советую вам быть терпимее ко всем членам команды, все отношения мы выясняем во внерабочее время.{w} Учтите Семен, что терпение коллектива небезграничное и долго ваши выгибоны здесь терпеть никто не будет.{w} Если вопросов нет - свободен."
    hide SemSad
    EV "По какому вопросу зашел?"
    if SAtt > 0:
            $SAtt -= 1
    jump Semen_meet3_end
    return

label Semen_meet3_end(): 
    
    return
