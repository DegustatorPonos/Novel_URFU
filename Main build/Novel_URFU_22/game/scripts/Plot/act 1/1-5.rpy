﻿label act1part5():
    "НА СЛЕДУЮЩИЙ ДЕНЬ"
    scene bg_bedroom
    show blink
    with dissolve
    hide blink
    with dissolve
    "За окном ещё темно."
    "От звука будильника и недосыпа болит голова."
    mainChar "Ааах…"
    mainChar "Полииин?"
    mainChar "А, да..."
    mainChar "(Надо бы позвонить ей, узнать, как там она)"
    "Вы достаёте телефон и набираете жене"
    "*Гудок*"
    "*Гудок*"
    "*Гудок*"
    "Вызываемый абонент не отвечает…"
    mainChar "Ну да, чего я ожидал…"
    mainChar "Пора бы и в офис собираться."
    with dissolve
    scene bg_bbg
    "Вы едете в офис."
    "..."
    "Вы заходите в отдел разработки и садитесь за единственный неподписанный стол."
    scene bg_workplace_gg
    show MCIdle at right
    "К вам подходит мужчина."
    "Вы узнаёте его – он заходил вчера к Евгению Викторовичу."
    show GenIdle at left
    person "Значит, всё-таки он тебя принял. {w}Ну, ладно."
    person "Поздравляю, пионер!"
    "Мужчина протягивает Вам руку."
    person "Геннадий."
    menu: 
        "(Пожать руку)":
            $GenAtt += 1
            "Вы жмёте руки."
        "(Игнор)":
            $GenAtt -= 1
    Gennadiy "Ты, значит, программист новый?"
    Gennadiy "На готовое любишь приходить?"
    menu:
        "А Вы так нет?":
            $GenAtt -= 2
            Gennadiy "Зависит..."
            "Он замолк"
        "Ну типа.":
            $GenAtt += 2
            Gennadiy "Ну, с другой стороны, а кто не любит, согласись?"
    Gennadiy "Так, в общем давай быстро по ролям."
    Gennadiy "С Евгением ты по-любому знаком, я тебя в его кабинете видал."
    Gennadiy "Это директор наш, если нервы у тебя ни к чёрту не ходи к нему."
    mainChar "Почему?"
    Gennadiy "А ты не заметил? {w}На таблетках дед."
    Gennadiy "Так вот, с Галей ты, видимо, тоже познакомился."
    Gennadiy "Стерва редкостная, {w}да и чай у неё говно."
    Gennadiy "Вот твоя карта, кстати."
    "Геннадий протягивает Вам банковскую карту."
    menu:
        "А почему мне её Вы передаёте?":
            $GenAtt -= 2
            Gennadiy "Потому что Галя на больничном. {w}Или тебе не надо?"
            mainChar "Надо."
            Gennadiy "Ну так бери."
        "Спасибо…":
            $GenAtt += 2
    "Вы взяли карту СтрахБанка из рук Геннадия."
    Gennadiy "Так, о чём я…"
    Gennadiy "А, да, Саня. Знаешь его уже?"
    mainChar "Да..."
    Gennadiy "Всё девку найти себе пытается, бедный."
    Gennadiy "Думаю поэтому к Сёме и докапывается. {w}Он у нас бабник лютый..."
    Gennadiy "Как-то притащил деваху одну к нам в офис, прикинь?"
    menu:
        "А что тут такого?":
            Gennadiy "У нас сроки горели, а этот идиот работать не мог – она его так задолбала... {w}Нас всех, кстати тоже."
        "А это не его дело, что он делает?":
            $GenAtt -= 2
            Gennadiy "Так вот в том-то и проблема, что дело его, а задолбались все."
    Gennadiy "Кроме Сани. Ему норм было."
    hide GenIdle
    show GenHappy at left
    Gennadiy "Ну так вот, про мою скромную личность."
    Gennadiy "Я лид, так что код твой сначала будет через меня проходить."
    Gennadiy "Я, если что, требования по тестам не ставлю, это так. {w}А то уверен, тебе уже по ушам поездили."
    mainChar "Да, Семён бесился по поводу их отсутствия."
    hide GenHappy
    show GenIdle at left
    Gennadiy "Слушай больше. Его работа, пусть он и делает."
    Gennadiy "Теперь быстро по твоим обязанностям."
    Gennadiy "График у нас странный, нигде такого не видал. {w}Короче работаешь ты без обеда, но по продолжительности меньше, чем с ним. {w}По любым вопросам – после рабочего дня."
    Gennadiy "Ферштейн?"
    mainChar "Ферштейн."
    Gennadiy "Ну, приступаем. {w} Ща мы сделаем красоту."
    scene bg_bbg with fade
    #jump act2part1
    return