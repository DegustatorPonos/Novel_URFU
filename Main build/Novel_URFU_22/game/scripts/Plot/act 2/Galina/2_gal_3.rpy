define GalBlueRoot = False

label act2_Gal_meet4:
    if len(GalChoice[0]) < 2:
        $GalChoice[0] = "А как же родня? Неужели вы совсем с ними порвали?"
    else:
        $GalChoice[0] = "А как же родня... А, точно"
    "Вы входите в кабинет Галины Петровны, и застаете ее плачущей за своим столом"
    scene GalBG
    show MCIdle at left
    show GalSad:
        xalign 1.0
        xzoom -1.0
    menu:
        "Поздороваться":
            mainChar "Добрый день, а... боже мой, что случилось?"
        "Поинтересоваться":
            mainChar "Здравствуйте, а... э-эм, чего ревете?"
            if GalAtt < -6:
                hide GalSad
                show GalScream:
                    xalign 1.0
                    xzoom -1.0
                with fade
                Galina "Иди к черту!" with vpunch
                hide MCIdle
                show MCSad at left
                mainChar "Но Галина Пет..."
                Galina "Убирайся!" with vpunch
                hide GalScream
                hide MCSad
                scene bg_bbg
                with fade
                "Вы спешите покинуть кабинет, уворачиваясь от летящей вам в след кружки."
        "Уйти":
            $GalAtt -= 2
            "Вы решаете просто уйти"
            hide GalSad
            hide MCIdle
            scene bg_bbg
            return
    if GalAtt < 0:
        Galina "..."
        menu:
            "Уйти":
                mainChar "Ладно, простите, я, пожалуй, пойду..."
                hide GalSad
                hide MCIdle
                scene bg_bbg
                with fade
                return
            "Настаивать":
                mainChar "Ну Галина Петровна, это ненормально ведь."
    else:
        Galina "Н-ничего, н-не важно."
        mainChar "Ну Галина Петровна, это ненормально ведь."
    Galina "Не уберегла, денег на операцию Марфуше не хватило!"
    mainChar "Марфуше? Вы о ней ничего не рассказывали."
    Galina "Собачка моя, молоденькая такая была, ой."
    menu:
        "Пожалеть":
            $GalAtt += 1
            mainChar "Боже мой, как же так?"
        "Взглянуть рационально":
            $GalAtt -= 1
            mainChar "Ну, у вас же другие есть и так, что париться?"
            hide GalSad
            show GalScream:
                xalign 1.0
                xzoom -1.0
            Galina "Что? Как ты можешь так говорить?"
            menu:
                "Извинится":
                    mainChar "Ох, простите, я не то имел в виду...{w} Ну а как же так?"
                    hide GalScream
                    show GalSad:
                        xalign 1.0
                        xzoom -1.0
                "Настаивать":
                    mainChar "Нет ну правда, еще найдете, че париться..."
                    Galina "Замолчи ирод!{w} Убирайся!{w} Видеть тебя не могу!" with vpunch
                    if GalAtt>0:
                        $GalAtt *= -1
                    $GalAtt *= 2
                    hide GalScream
                    hide MCIdle
                    scene bg_bbg
                    with fade
                    "Вы спешите покинуть кабинет, уворачиваясь от летящей вам в след кружки."
                    return
    Galina "Не смогла накопить ну не смогла!{w} Не у кого было даже взаймы просить."
    menu:
        "Даже у команды?":
            mainChar "Даже у команды?"
            Galina "Уже, уже..."
            menu:
                "Спросить про родню":
                    mainChar "Оу..."
                "Смириться":
                    mainChar "Ох, боже ж мой."
                    Galina "Ладно, не нужно мне тебя грузить, забудем.{w} Зачем заходил?"
                    $GalBlueRoot = True
                    hide GalSad
                    hide MCIdle
                    scene bg_bbg
                    with fade
                    "Вы решаете свои вопросы и расходитесь."
                    $GalAtt -= 1
                    return
        "Даже у родни?":
            mainChar "Хмм..."
    mainChar "[GalChoice[0]]"
    Galina "Поругались мы с ними, давно еще, как раз из-за бездомышей.{w} Сказала я им, что не буду им жить мешать, сниму квартирку и зверями займусь."
    Galina "Так мы больше не созванивались."
    menu:
        "Предложить позвонить самой":
            mainChar "Вы не пытались сами им позвонить?"
            Galina "Нет, я...{w} Я боюсь.{w} Они, может, вообще мой номер заблокировали."
            mainChar "Не верю я этому, как бы вы не ругались раньше - время не стоит на месте.{w} Я уверен они не будут против вновь с вами говорить." #БЯЛТЬ ЭТО ЖЕ РЕАЛЬНО HOME ALONE
            Galina "Но почему же тогда они мне не звонят?" 
            mainChar "По той же причине, по которой боитесь позвонить вы.{w} Они боятся что вы до сих пор на них в обиде." #Надо стоковое имя сделать Макалей Калкин
            Galina "Уф..."
            hide GalSad
            show GalSmile:
                xalign 1.0
                xzoom -1.0
            mainChar "Я думаю вам просто нужно решиться и позвонить им."
            Galina "Возможно ты и прав, но...{w} Мне нужно все обдумать."
            Galina "Ладно, закрыли тему, зачем приходил?.."
            hide GalSmile
            hide MCIdle
            scene bg_bbg
            with fade
            "Вы решаете свои вопросы и расходитесь"
            if GalAtt < 0:
                $GalAtt = 1.5
            return
        "Предложить смириться":
            $GalBlueRoot = True
            mainChar "Ну и черт с ними, раз не ценили вас, и про них забыть можно."
            Galina "Возможно..."
            mainChar "А на счет собаки - поверьте мне, не вы виноваты, просто так сложились обстоятельства."
            mainChar "Судьбу не повернешь."
            Galina "Ладно, спасибо но, закроем тему.{w} Зачем приходил?.."
            $GalAtt += 1
            hide GalSad
            hide MCIdle
            scene bg_bbg
            with fade
            "Вы решаете свои вопросы и расходитесь"
            return