label act1part1:
    scene bg_bbg
    unknown "[NameSpace], вставай!"
    mainChar "Ща, подожди"
    unknown "Вставай, ленивый кусок говна!"
    mainChar "А тазик не подтащишь, раз я так нужен? После вчерашнего чувствую, что может понадобиться."
    scene bg_bedroom
    show blink
    with dissolve
    unknown "Ага, тебе может ещё и завтрак в кровать? Не поплохеет?"
    unknown "Да и не так много ты выжрал, на твои гроши нормально не оторвёшься!"
    hide blink
    with dissolve
    #Polly's apearing on the right
    "Глаза полностью открываются, над Вами стоит Полина"
    polly "Я только Кордон заказать смогла, прикинь! Не Сенеру! Вот до свадьбы ты мне поку…"
    #MC's appearing on the left
    mainChar "Подожди, что ты пила?"
    polly "Кордон. Тоже в шоке? Как в горло только полезла такая отрава!"
    mainChar "Полин, ты чё наделала? Оно ж стоит десятку!"
    polly "Да! И вот это ты мне предлагаешь пить?!"
    mainChar "Я значит водку хлестал, думал, чем ипотеку в этом месяце закрывать будем, а ты влила все наши деньги в шампанское?"
    polly "Ах, ты меня сейчас попрекать будешь? За то, что я хочу в удовольствие жить, а не это всё?"
    polly "Я тебя, значит, вообще не забочу?"
    polly "Действительно, как что так ты в доме мужик, а как до проблем доходит – твоё здоровье меня волновать не должно!"
    "Ты упускаешь нить разговора и не очень-то хочешь вникать в него снова"
    mainChar "(Это ведь моя вина. Хочешь айфон - держи, хочешь машину – выбирай. Разбаловал, [NameSpace], вот и терпи теперь такое чудо.)"
    polly "И вообще, лучше бы я за Макса пошла, жить лучше было бы! Но нет, пожалела бедного! И вот как ты мне отплатил!"
    "Полина выходит и захлопывает за собой дверь"
    "Ты открываешь ноутбук, чтобы проверить почту."
    "До дедлайна ещё далеко, так что можно позволить себе отдохнуть."
    "Ты видишь уведомление и открываешь почту."
    "На экране появляется письмо."
    "Письмо" "Дорогой [NameSpace]. Нам искренне жаль сообщать Вам об этом, но ввиду последних Ваших… выходок мы вынуждены отстранить Вас от работы над проектом."
    "Ты перечитал письмо ещё несколько раз, но тщетно."
    "Это не иллюзия, не результат похмелья."
    "Работы у тебя больше нет."
    "Как и денег."
    "Ты сидишь ещё несколько минут, пытаясь переварить полученную информацию."
    "Больше всего ты боишься того, что ты должен сделать первым, но выбора нет."
    "Надо – значит надо."
    #MC's disappearing
    scene bg_bbg
    with dissolve
    "Ты выходишь на кухню и видишь Полину, болтающую со своей подругой."
    scene bg_kitchen
    with dissolve
    #Polly's appearing
    polly "…ага, и не говори! Уже не знаешь, что ставить! Столько времени на эти фильтры уходит! Что говоришь?"
    "..."
    polly "Ну да, мой – программист, а что?"
    "..."
    polly "Ааа, да не, он не настолько программист. Понимаешь, у этого полена абсолютно отсутствует чувство прекрасного!"
    polly "Хотя даже с таким набором он смог меня выбрать, так что не всё поте…"
    #MC's appearing
    mainChar "Это полено вообще-то здесь и у него есть уши."
    polly "Ой, прости, я тебе перезвоню!"
    polly "(шёпотом) Да, это он, давай!"
    polly "Ну, извиниться пришёл? Поставь чайник, кстати."
    mainChar "Слушай, мне надо тебе кое-что сказать"
    polly "Что-то пока не звучит как извинения."
    menu:
        "Извиниться":
            $politeness += 1
            mainChar "Ладно, Полин, Прости. Виноват, извиняюсь. Но послушай, это реально важно"
            polly "Ладно, будем считать, извинения приняты. Но тебе бы поучиться манерам."
            polly "Так что у тебя там?"
        "Проигнорировать":
            $politeness -= 1
            
        "Жёстко прервать":
            $politeness -= 2
            mainChar "Ага, мне тебе может ноги расцеловать?"
            polly "Ну и пошёл ты! Выкладывай, чё у тебя там! Ток давай это, меня дела ещё."
    
    "Ты закрываешь воду и ставишь чайник на плиту."
    mainChar "Короче, насчёт работы… Наши посиделки в баре не очень высоко оценило начальство, поэтому…"
    polly "Только не говори, что тебя уволили. Только посмей."
    mainChar "Тогда, пожалуй, мне стоит просто помолчать."
    "Вы сидите в тишине и смотрите друг на друга."
    polly "..."
    mainChar "..."
    "Тишину прерывает закипающий чайник."
    #play teapot
    "Полина молча встаёт из-за стола и идёт к себе."
    "Ты следуешь за ней."
    scene bg_pollysroom
    with dissolve
    mainChar "Поль, я понимаю, ты злишься, но…"
    polly "Злюсь? Да я в бешенстве! За кого я вообще вышла?!"
    "Полина начинает запихивать свои вещи в сумку."
    mainChar "Так, давай ты выскажешь мне всё, что ты хочешь и мы поговорим."
    polly "О нет, не выскажу. Если хоть кто-нибудь кроме нас это услышит, то меня закэнселят в секунду!"
    mainChar "Ну и куда ты собралась? Я отель тебе уже не оплачу! Скажи спасибо вчерашнему винцу"
    polly "Ну и больно надо! Я к подруге жить."
    polly "У неё хотя бы деньги есть!"
    mainChar "А эта не та подруга, у которой мужики потоком ходят?"
    polly "Да. И у Оли вообще-то имя есть. И не так уж у неё много парней было!"
    polly "И вообще, если бы я знала, какой ты, я бы лучше вышла за кого-нибудь из них!"
    polly "Или ещё лучше за Макса! Вот он – реальный мужик! Не туфта, как ты!"
    "Полина закрывает сумку и уходит"
    #Polly gone
    polly "Удачи оставаться! Позвоню, когда соскучусь."
    polly "Ну, то есть не жди."
    polly "Пока, зай!"
    "Ты слышишь как закрывается дверь."
    scene bg_bbg
    with dissolve
    #teapot stops
    "Неделю спустя"
    scene bg_toilet_clean
    with dissolve
    "Вас давно не рвёт, но Вы боитесь встать и упасть на унитаз головой."
    mainChar "Ща б не ослепнуть..."
    mainChar "Найду этого барыгу - закопаю нахрен..."
    "Вы слышите звук уведомления на своём телефоне"
    "Вы решаете встать, чтобы проверить телефон."
    show blink
    with dissolve
    with vpunch
    "Ваши ноги не способны держать вес Вашего тела в горизонтальном положении"
    "Вы падаете и ударяетесь об унитаз головой."
    scene bg_bbg
    with dissolve
    with vpunch
    "..."
    mainChar "Зараза…"
    "Вы открываете глаза"
    scene bg_toilet_bloody 
    with fade
    "Из окна падает свет, освещая Вас, лежащего в луже собственной крови."
    mainChar "Ёёёё..."
    mainChar "(И чё меня потянуло вставать?)"
    mainChar "(Как я вообще не умер?)"
    mainChar "(Хотя с такой головой всё ещё впереди…)"
    mainChar "(А, телефон! Что там пришло-то?)"
    mainChar "(Иди сюда, мелкая гадость…)"
    "Вы чувствуете что-то в кармане штанов"
    "Оказывается, всё это время телефон был там."
    "Вы читаете уведомление."
    "Уведомление" "На Ваше резюме откликнулись (1) работодателей!"
    "Вы нажимаете на уведомление"
    "Уведомление" "Сообщение от работодателя:"
    "Уведомление" "Уважаемый [NameSpace]]! Нас заинтересовало Ваше резюме, и мы изъявляем желание пригласить Вас в нашу команду"
    "Уведомление" "Мы занимаемся разработкой приложения для автоматического процедурного улучшения фотографий для социальных сетей."
    "Уведомление" "Требования - навыки IOS-разработки."
    mainChar "(Стоп, а не об этом Полина говорила тогда по телефону?)"
    mainChar "(Если все юзеры будут как она, и во всех будут так же вливать деньги…)"
    mainChar "Да это ж чёртова золотая жила!"
    mainChar "Я БУДУ ЧЕРТОВСКИ БОГАТЫМ, ТЫ СЛЫШИШЬ МЕНЯ, СТЕРВА!"
    mainChar "У МЕНЯ БУДЕТ БОЛЬШЕ ДЕНЕГ, ЧЕМ У ЭТОГО УБЛЮДКА МАКСА!"
    "Вы слышите удары в отопительный стояк."
    scene bg_bbg with dissolve
    jump act1part2
    return
