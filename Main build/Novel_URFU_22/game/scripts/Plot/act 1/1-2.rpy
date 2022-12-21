label act1part2():
    screen bg_office_director
    "Вы зашли в кабинет к директору. {w}На столе стоит табличка с надписью “Евгений Викторович”. {w}Вероятно, это имя владельца кабинета."
    "Из-за стола на тебя смотрит мужчина. {w}На его лице морщины, а под глазами заметные синяки."
    show EVIdle at right
    EV "Итак, Вы, я так понял, [NameSpace]."
    show MCIdle at left
    mainChar "Да, всё верно."
    EV "Отлично, спасибо что откликнулись на наше предложение. {w}Присаживайтесь. {w}Работали, значится, над интерфейсами для игр?"
    mainChar "Да, имел честь."
    EV "Отлично…"
    menu:
        "Продолжать слушать":
            $politeness += 1
            $EVatt += 0.5

        "Попросить побыстрее":
            $EVatt -= 1.5
            mainChar "А можно говорить… {w}ну… {w}побыстрее?"
            EV "Молодой человек, вы меня не торопите. Вы ко мне пришли, не я к вам."
            EV "..."
            EV "Так..."

    EV "А как Вы думаете, Ваш опыт поможет нам в процессе разработки?"
    mainChar "Несомненно"
    EV "А можете описать подробнее?"
    mainChar "Ну смотрите, при разработке интерфейса приходится думать, как он будет работать с техни…"
    "Вы замечаете, как директор побледнел"
    mainChar "Извините{w}, всё хорошо?"
    EV "Ой, простите{w}, продолжайте. Просто я назначил Вам собеседование, не учтя расписание приёма таблеток."
    "Евгений Викторович достал коробку и достал таблетку"
    "Вы не успели прочесть название препарата"
    mainChar "Так вот, дизайн должен быть адекватно реализуемым с техни…"
    "В комнату входит незнакомец"
    hide EVIdle
    show GenIdle at right
    person "Евгений Борисович, у Вас нет кофе? В отделе разработки всё выхле…"
    person "Оо, новый?"
    person "Я надеюсь он успел Вам надоесть?"
    menu:
        "Промолчать":
            pass

        "Ну как, он всегда так медленно говорит?":
            hide GenIdle
            show GenAngry at right
            person "Ну вообще я не с тобой говорил."
            person "Грубый"
            person "Ну, хуже в отделе быть уже не сможет."
            show EVIdle
            EV "Ладно.{w} Сочтём за комплимент, полагаю."
            $EVatt -= 2
            hide GenAngry
            show GenIdle at right

        "Да нет, Вы чего?":
           person "Ну вообще я не с тобой говорил."
           person "Смешной"
           person "Ну, будет не так душно в отделе."
           show EVIdle
           EV "Не обращайте внимания, [NameSpace]. У него просто такой юмор."
           EV "Но сочтём это за комплимент."
           $EVatt += 2

    "Евгений Викторович глотает таблетку"
    person "Ну, не буду вам мешать."
    person "Новый, жду завтра.{w} В 9.{w} Не опоздай в первый же день."
    hide GenIdle
    show EVIdle
    "Незнакомец ушёл"
    EV "Так вот. {w}К Вашему опыту…"
    "Незнакомец возвращается"
    show GenIdle at right
    person "Так кофе-то дадите?"
    EV "Да, простите, сейчас поищу"
    EV "Вот, держите"
    "Евгений Викторович протягивает незнакомцу полную банку кофе.{w} Тот её берёт и уходит."
    hide GenIdle
    EV "Простите его. Вы ещё готовы ответить?"
    menu:
        "Да, почему нет?":
            EV "В таком случае полагаю, что вы знаете, что делаете."
            $EVatt += 2

        "А больше нас никто не прервёт?":
            EV "Очень жаль, что Вы не поняли, что это не от меня зависит."
            $EVatt -= 2
    EV "Прошу простить, но я не настолько квалифицирован, чтобы оценить Ваши технические навыки."
    EV "Я приготовил все необходимые формы. Распишитесь здесь, если готовы начать сотрудничество"
    mainChar "Благодарю"
    "Вы подписываете документы в местах, помеченных галочками"
    EV "Замечательно"
    EV "Кстати, я бы посоветовал поговорить с Александром, найдёшь его в отделе разработки."
    mainChar "Хорошо, спасибо.{w} Хорошего дня!"
    EV "И Вам того же"
    hide EVIdle
    hide MCIdle
    screen bg_development_department
    "Вы заходите в отдел разработки"
    "Вы слышите двух спорящих лиц"
    un1 "Да потому что ты на почте его не прочитаешь!"
    un2 "Я всю твою писанину читаю!"
    un2 "ВСЮ!"
    un2 "Ты сам, кажется, не так много своих стихов читаешь, как я."
    un2 "И ты меня ещё обвиняешь в чём-то?"
    un1 "Да.{w} Потому что ты сейчас типа врёшь."
    un2 "С чего ты так решил?"
    "Вы подходите ближе и видите двух парней лет 20-25."
    show SeAngry at left
    show AlAngry at right
    "Один сидит на столе, второй стоит перед ним почти вплотную"
    un1 "Потому что ты… игноришь короче!"
    un2 "Так мне просто добавить нечего, ты и сам всё понимаешь."
    un2 "Оп, а вот и тот разраб!"
    hide AlAngry
    show AlIdle at right
    hide SeAngry
    show SeIdle at left
    un2 "Ну, посмотрим, что нашу {i}дружную семью{/i} ждёт"
    "Слово “дружную семью” он произнёс с насмешкой"
    mainChar "Простите, что отвлекаю, но мне Евгений Викторович поручил с Александром поговорить."
    un2 "Да мы вроде закончили. Да, Сём?"
    un2 "Я Александр. Свинцов."
    Semen "Да, так что давай дельтуй."
    Alex "Чё?"
    Semen "Ничё. Вали давай, работать мешаешь."
    "Александр уходит"
    hide AlIdle
    menu:
        "(Пойти за Александром)":
            $politeness += 1
            jump act1part3_alex

        "Прости, а о чём вы там спорили?":
            jump act1part3_sema
    return