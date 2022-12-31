label act2_Gen_meet3:
    "Вы выключаете компьютер."
    "Судя по звукам, точнее их отсутствию, Вы опять задержались."
    "Неожиданно тишина прерывается не самым достойным набором слов."
    "Судя по голосу, они были произнесены Геннадием БорисовичЪем."
    menu:
        "Проигнорировать":
            $GenAtt -= 5
            "Вы уходите домой"
            return
        "Посмотреть, в чём дело":
            "Вы идёте на шум и видите агрессивно печатающего Геннадия БорисовичЪа."
            scene GenBG
            show MCIdle at left
            show GenSad at right:
                xzoom -1.0
    if GenAtt < 0:
        jump Gen_3_badPath
    else:
        jump Gen_3_goodPath


label Gen_3_goodPath:
    Gennadiy "О, привет, [NameSpace]."
    Gennadiy "Слушай, ты не торопишься никуда?"
    Gennadiy "Тут проблемка небольшая, вроде по твоей части."
    Gennadiy "Ты же занимался раньше фронтом?"
    mainChar "Ну было дело..."
    Gennadiy "Отлично, не поможешь?"
    Gennadiy "А то у меня мозг уже взорвался."
    menu:
        "Согласиться":
            $GenAtt += 1
            jump Gen_3_Issue
        "Уточнить задачу":
            $GenAtt += 2
            mainChar "А на чём пишете хоть?"
            Gennadiy "О, деловой подход, мне нравится."
            Gennadiy "Знаешь такое больное зло, ксамарин?"
            mainChar "Так мы же вроде на реакте пишем."
            Gennadiy "Ну я так, для себя."
            Gennadiy "Ну так как?"
            menu:
                "Отказаться ввиду новой информации":
                    $GenAtt -= 2
                    mainChar "Я-то думал по работе что..."
                    Gennadiy "Ну вообще да, надо было сразу уточнить..."
                    Gennadiy "Нагло вышло, прости."
                    Gennadiy "Не держу, разберусь сам."
                    Gennadiy "Давай."
                    mainChar "Давайте."
                    hide MCIdle
                    hide GenSad
                    scene bg_bbg
                    return
                "Продолжить":
                    mainChar "Ну, было дело..."
                    Gennadiy "Ну ничего себе мне везёт.."
                    jump Gen_3_Issue
        "Отказаться":
            $GenAtt -= 2
            mainChar "Простите, тороплюсь.."
            Gennadiy "Ну ладно, коли надо."
            Gennadiy "Давай, удачи."
            mainChar "Давайте."
            hide MCIdle
            hide GenSad
            scene bg_bbg
            return

            
label Gen_3_badPath:
    Gennadiy "А ты чё тут забыл?"
    Gennadiy "Дел больше нет, кроме как подслушивать?"
    mainChar "Да просто пришёл посмотреть, в чём дело..."
    Gennadiy "Вот как пришёл, так и уйдёшь."
    Gennadiy "Давай, кш-кш, отвлекаешь."
    menu:
        "Уйти":
            $GenAtt -= 2
            hide GenSad
            hide MCIdle
            scene bg_bbg
            "Вы решаете последовать совету Геннадия и уйти домой."
            return
        "Настаивать":
            $GenAtt += 1
            mainChar "Ну, я подумал, что у Вас проблема..."
    Gennadiy "Хммм..."
    Gennadiy "Ну вообще да..."
    Gennadiy "Стоп." with vpunch
    Gennadiy "Стой, парень, а ты кем там работал до этого?"
    mainChar "Интерфейсы писал..."
    Gennadiy "О, зашибись."
    Gennadiy "Как ты с этим бредом работать вообще смог?"
    Gennadiy "Это же просто бред сумасшедшего."
    mainChar "Ну, зависит от того, на чём пишешь..."
    Gennadiy "Работал с ксамлом?"
    mainChar "Бывало.."
    Gennadiy "Сочувствую."
    menu:
        "Оставить эту работу на Геннадие":
            $GenAtt -= 1
            mainChar "Ну, удачи повоевать с этим кошмаром..."
            Gennadiy "Вообще я тут подумал..."
            Gennadiy "Ну его нахрен, копаться с этим ужасом."
            Gennadiy "Ты умеешь - ты и возьмёшь."
            Gennadiy "Зачем-то же тебя наняли."
            hide MCIdle
            show MCScream at left
            mainChar "Ну вообщ..."
            hide GenIdle
            show GenSmile at right:
                xzoom -1.0
            Gennadiy "Ну вот и договорились."
            Gennadiy "Увидимся завтра, я домой."
            hide MCScream
            show MCSad at left
            hide GenSmile
            with fade
            "Геннадий БорисовичЪ уходит из офиса."
            "Вы стоите, обескураженный произошедшим."
            hide MCSad
            scene bg_bbg
            return

        "Предложить помощь":
            mainChar "Так это, Вам помочь?"
            Gennadiy "Если что, премию за это я тебе не выпишу, имей ввиду."
            Gennadiy "А вообще, было бы круто."
    jump Gen_3_Issue

label Gen_3_Issue:
    Gennadiy "Короче тут такая тема:"
    Gennadiy "У меня есть грид на три строки."
    Gennadiy "Во второй ещё один, квадратный."
    Gennadiy "В каждой ячейке кнопки."
    Gennadiy "На каждой кнопке - паддинг."
    Gennadiy "Так вот, ты его видишь?"
    "Геннадий показывает Вам телефон."
    Gennadiy "На экране находится залитый квадрат."
    mainChar "Дайте угадаю - изменение значения отступов ни на что не влияет?"
    Gennadiy "Именно."
    Gennadiy "И вот что с этим делать я, если честно, без понятия."
    menu:
        "Предложить..."
        "Отказаться от кнопок":
            $GenAtt -= 2
            mainChar "А если отказаться от кнопок и читать координаты нажатия?"
            Gennadiy "Говнокодить изволите, сударь."
            Gennadiy "Кнопки же по сути это и делают."
            Gennadiy "Зачем мне писать то, что уже реализовано?"
            mainChar "Ну, я предложил."
            if GenAtt > 0:
                Gennadiy "Ну по сути, конечно, да..."
                Gennadiy "Но вот не нравится мне этот способ."
                Gennadiy "Поищу ещё в интернете, по-любому инфа есть."
                Gennadiy "Но на будущее - слезай с таких приколов."
                Gennadiy "Работать будет лучше, поверь."
                jump Gen_3_continue
            Gennadiy "И у тебя так все продукты работают?"
            Gennadiy "Не удивлён, что тебя с предыдущей работы выперли."
            hide MCIdle
            show MCScream at left
            mainChar "Откуда Вы?..."
            Gennadiy "Ну я должен знать, чего от сотрудника ожидать."
            hide MCScream
            show MCSad at left
            Gennadiy "Так что давай, делай по-нормальному, а то и отсюда вылетишь."
            Gennadiy "Ферштейн?"
            mainChar "Ферштейн."
            Gennadiy "Дас ист гут."
            Gennadiy "Дуй домой давай, время."
            Gennadiy "Или ты тут ночевать решил?"
            Gennadiy "Так делать не надо, держу в курсе."
            mainChar "Да я как раз собирался..."
            Gennadiy "Ну вот, я тоже."
            Gennadiy "Давай."
            mainChar "Давайте."
            hide MCSad
            hide GenSad
            scene bg_bbg
            return
            
        "Отказаться от сетки":
            $GenAtt -= 1
            mainChar "Грид - вообще гнездо багов, попробуйте абсолютную разметку."
            Gennadiy "Ну вообще тема, но это же, блин, всё с нуля..."
            Gennadiy "Да и считать долго..."
            Gennadiy "Ладно, попробую, но не сейчас."
            Gennadiy "Заманался сегодня..."
            jump Gen_3_continue 

        "Добавить ещё один уровень разметки":
            $GenAtt += 1
            mainChar "Попробуйте кнопки в лэйаут кинуть."
            Gennadiy "Так, сейчас..."
            "Геннадий начинает в спешке печатать код."
            Gennadiy "Ииии.."
            Gennadiy "О, нхрена."
            hide GenSad
            hide GenIdle
            show GenSmile at right:
                xzoom -1.0
            Gennadiy "Реально сработало!"
            Gennadiy "Вот, наконец-то, умный человек."
            jump Gen_3_continue

label Gen_3_continue:
    Gennadiy "Так, ладно, на сегодня работы хватит."
    "Геннадий выключает компьютер и идёт к кофейному столику."
    if GenAtt > 0:
        Gennadiy "Смотри, кстати, какую приблуду купил давеча."
        Gennadiy "Как чайник, но температуру постоянно поддерживает."
        Gennadiy "Электричество казённое, почём не жечь?"
        "Геннадий БорисовичЪ насыпает себе в кружку несколько ложек кофе."
        Gennadiy "Будешь?"
    else:
        "Геннадий БорисовичЪ насыпает себе в кружку несколько ложек кофе."
        Gennadiy "Себе сам нальёшь, если надо."

    if GenCoffe:
        mainChar "Кхм, Геннадий..."
        Gennadiy "А, да, я ж обещал..."
        "Геннадий кладёт кружку обратно на столик"
        Gennadiy "Ты-то будешь?"
        mainChar "Не, спасибо."
        if NSFWfilter == 0:
            Gennadiy "Ну, как говорят, пить оному - это как срать в компании."
        else:
            Gennadiy "Ну, дело твоё."

    else:
        menu:
            "Выпить":
                mainChar "Давайте"
                Gennadiy "Ну, вот это по-нашему."
                if GenAtt < 0:
                    Gennadiy "Ладно, давай сюда свою."
                Gennadiy "Тебе сколько?"
                mainChar "Одну."
                Gennadiy "Мхм, принял"
                show bg_bbg with fade
                "Геннадий насыпает в Вашу кружку кофе и заливает в обе кипяток из чайника."
                hide bg_bbg with fade

            "Воздержаться":
                mainChar "Пожалуй, воздержусь"
                Gennadiy "Ну, дело твоё."
                Gennadiy "А я вот не воздержусь."
                show bg_bbg with fade
                "Геннадий заливает кипяток в свою кружку."
                hide bg_bbg with fade
    
    Gennadiy "Слушай, я вот тут задумался."
    Gennadiy "Вот ладно я, ты-то чё тут сидишь?"
    Gennadiy "Почти десять, все свалили давно, а ты тут."
    Gennadiy "Настолько проектом горишь?"
    menu:
        "Ради денег":
            mainChar "Деньги нужны."
            Gennadiy "Ну, а кому не нужны? {w} Проклятый капитализм!"
            Gennadiy "Ладно, не мне тебя судить, сам недалеко ушёл."

        "Ради идеи":
            $GenAtt += 1
            mainChar "Ну мне делать-то особо нечего."
            Gennadiy "Понимаю."
            Gennadiy "Ты же вроде женат? {w} Кольцо на пальце."
            Gennadiy "Она времени не требует?"
            mainChar "Мы не общаемся."
            Gennadiy "Блин, косяк, пардон."

        "(Сарказм)":
            $GenAtt -= 2
            mainChar "А Вы, видимо, нет?"
            hide GenIdle
            hide GenSmile
            hide GenSad
            show GenSad at right:
                xzoom -1.0
            Gennadiy "А я, видимо, нет."
            Gennadiy "Но делать больше нечего."
            Gennadiy "А ты, видать, человек высокой морали."
            Gennadiy "Благородный рыцарь за чёрной клавиатурой."
            Gennadiy "Ну, не важно."
    
    Gennadiy "Ладно, поздно уже."
    Gennadiy "Давай по домам, а то тут прожить можно."
    mainChar "Давайте."
    "Вы с Геннадием БорисовичЪем выходите из офиса."
    hide GenIdle
    hide GenSmile
    hide GenSad
    hide MCIdle
    hide MCSad
    scene bg_bbg
    return