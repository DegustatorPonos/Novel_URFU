label Final_Pt1:
    scene bg_bbg
    play music bassyBGM loop
    unknown "[NameSpace], вставай!"
    mainChar "Ща, подожди "
    scene bg_bedroom
    show blink
    with dissolve
    "Вы просыпаетесь от резкого толчка."
    unknown "Вставай, ленивый кусок говна!"
    "Вы узнаёте голос."
    hide Blink 
    show MCIdle at right
    show pollyIdle at right
    mainChar "Полина?"
    polly "А кто ещё?"
    mainChar "Вот те на! Ты где была? "
    polly "Сначала у Оли, потом у Макса, потом…"
    mainChar "Стоп. У кого?"
    polly "У Оли."
    mainChar "Нет, после."
    polly "У Макса…"
    mainChar "С этого момента поподробнее."
    polly "Да он оказался реальным мудаком!"
    polly "Прикинь, даже посуду за собой в мойку не закинет!"
    polly "Да у него даже мойки не было!"
    polly "Прикинь, а ещё…"
    mainChar "Стоп."
    mainChar "Сколько ты жила у него?"
    polly "Да недолго. Так вот, он один раз вечером…"
    hide MCIdle
    show MCSad at left
    mainChar "Сколько.{w} Ты.{w} Жила.{w} У.{w} Макса?"
    polly "Ну недельки две-три…"
    mainChar "Мхм."
    polly "Ну ты не пойми, я всё поняла!"
    polly "Он реально мудак, [NameSpace]!"
    mainChar "…"
    polly "Ну прости, чё ты."
    polly "Ты же знал, что я вернусь!"
    mainChar "Вон."
    polly "Вот именно! Я точн…{w} Стой, что?"
    mainChar "Вон."
    mainChar "Шагом из моей квартиры."
    polly "Но я же тоя жена!"
    "Вы бросаете кольцо в неё."
    polly "[NameSpace], ты что творишь?"
    polly "Я сейчас обижусь!"
    "Вы встаёте."
    hide MCSad
    show MCScream ar left
    mainChar "ВОН."
    hide MCScream 
    show MCSad at left
    hide pollyIdle
    show pollyAngry at right
    polly "Ну смотри, [NameSpace], ты пожалеешь?"
    "Вы молча смотрите на неё."
    hide pollyAngry 
    with dissolve
    "Полина уходит."
    "Вы слышите, как захлопывается дверь."
    "Вы смотрите на время."
    "До начала рабочего дня 3 часа."
    
