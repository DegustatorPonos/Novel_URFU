label edna_convo_default:
    call process_conversation_beginning ([ (n, ""), (edna, "") ])

    call debug_message ("Default conversation when none others are available.")
    $ edna.c("Привет " + n.say_name + ".")

    call process_end_of_conversation ("edna_convo_default", edna, priority=False, default=True)

    return


label edna_convo_1:
    call process_conversation_beginning ([ (n, ""), (edna, "pose handhip face neutral blush false mouth red") ])

    call process_character (edna, appearance="pose handhip face neutral blush false", text="Нельзя ошибаться, изучая математику!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Ты и [sa.say_name] готовитесь к школе?")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Да, мы много занимаемся математикой.")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Она используется по всему миру.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="А как насчёт сочинений?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Мы пишем обзоры видеоигр и фильмов.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Это интересно, и помогает вашим грамматическим навыкам.")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Вот почему ты и твоя сестра получаете такие хорошие оценки!")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Даже во время летних каникул, вы уделяете время, чтобы получать образование самостоятельно.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Не многие дети делают это сегодня.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Да.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Я буду счастлив, когда мне больше не придется ходить в школу...")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Хаха!")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Ну, даже когда ты закончишь школу, ты никогда не перестанешь учиться.")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Это часть роста, как личность!")

    call process_end_of_conversation ("edna_convo_1", edna, priority=False, default=False)


    return

label edna_convo_2:
    call process_conversation_beginning ([ (n, ""), (edna, "pose handclasp face neutral blush false mouth red") ])

    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Так скажите мне [n.say_name], нравится ли тебе какой-либо вид спорта?")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Похоже, тебе нравится играть со мной в теннис.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Я не очень разбираюсь в спорте.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Это удел [k.say_name].")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Я думаю, твоя старшая сестра любит все виды спорта на планете!")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Если это игра, где можно выиграть, то [k.say_name], вероятно, займётся ей.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Еще до твоего рождения она всегда была такой.")
    call process_character (edna, appearance="pose handhip face curious blush false", text="Ты знал, что однажды она пыталась попасть на Олимпиаду?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Да, мама рассказывала мне об этом раньше.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Я все еще думаю, что она могла бы соревноваться в легкой атлетике.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Она бежит, как ветер!")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Хотя в волейболе она тоже очень хороша.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Было страшно смотреть на нее в том матче на днях...")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="У неё действительно сумасшедший взгляд в глазах, когда она хочет выиграть, ха-ха!")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Так что я знаю, что ты имеешь в виду!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Но мне не даётся ни футбол, ни бейсбол или что-то подобное.")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Но мне нравится киберспорт!")
    call process_character (edna, appearance="pose handhip face curious blush false", text="Киберспорт?")
    call process_character (edna, appearance="pose handhip face curious blush false", text="Что это такое?")
    call process_character (n, appearance="pose handfist face happy blush false", text="Это турниры по видеоиграм!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Лучшие игроки в мире учавствуют в них.")
    call process_character (n, appearance="pose handpocket face happy blush false", text="[sa.say_name] хочет поучавствовать когда-нибудь!")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Я никогда не слышала о таком!")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Но я не удивлена, что ты и [sa.say_name] большие поклонники этого!")

    call process_end_of_conversation ("edna_convo_2", edna, priority=False, default=False)


    return

label edna_convo_3:
    call process_conversation_beginning ([ (n, ""), (edna, "pose handclasp face neutral blush false mouth red") ])

    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Ты уже осмотрел весь комплекс [n.say_name]?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Я обычно иду прямо к тебе, Бабушка.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Ты должен осмотреться, когда у будет возможность.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Ты не поверишь, какие мероприятия, которые здесь проходят!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Да?")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Есть танцевальный зал, где люди практикуют чечетку, танцы в линию, кадриль...")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Назови хоть один, и они, вероятно, изучают его там!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Это здорово.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Тогда есть целый театральный клуб.")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Каждые пару месяцев они ставят полноценные постановки.")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Некоторые из участников - актеры на пенсии!")
    call process_character (edna, appearance="pose fisthip face happy blush false", text="Они все очень талантливые.")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Вау, целый театр?")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Именно поэтому многие жители просто живут на территории комплекса.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Здесь практически есть всё!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Есть что-нибудь, чего нет в этом месте?")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Это хороший вопрос, ха-ха!")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Такое чувство, что недочётов нет.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Знаешь, чего на самом деле здесь нет?")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Бассейна.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Нет?")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Был один несколько лет назад, рядом с пляжем.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Но пронеслась буря и уничтожила его.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="С тех пор он закрыт и нуждается в ремонте.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Это очень плохо.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Я надеюсь, что они это исправят в ближайшее время.")
    call process_character (n, appearance="pose handfist face happy blush false", text="Ты всегда можешь поплавать в бассейне у меня дома, если хочешь, Бабушка!")
    call process_character (edna, appearance="pose handhip face happy blush false", text="Это правда!")

    call process_end_of_conversation ("edna_convo_3", edna, priority=False, default=False)


    return

label edna_convo_4:
    call process_conversation_beginning ([ (n, ""), (edna, "pose fisthip face neutral blush false mouth red") ])

    call process_character (edna, appearance="blush false", text="Я взяла мороженое для коктейля в местной молочной.")
    call process_character (edna, appearance="blush false", text="Тебе нужно сходить туда как-нибудь.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="У них действительно хорошее мороженое?")
    call process_character (edna, appearance="pose fisthip face neutral blush false", text="Я слышала, люди все время восторгаются этим местом.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Я лично не могу ручаться за это.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Почему?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Ты никогда не пробовала?")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="У меня непереносимость лактозы.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Я вообще не могу есть молочные продукты.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Нет молока или мороженого для меня.")
    call process_character (n, appearance="pose twohandfist face embarrassed blush false", text="Без мороженого?!")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Да, я знаю, у меня была такая же реакция, когда я узнала, что больше не могу его есть.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="По-видимому, часто возникает непереносимость лактозы, когда ты становишься старше.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Так ты больше никогда не сможешь съесть мороженое?")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Есть лекарства, которые можно принять.")
    call process_character (edna, appearance="pose handhip face neutral blush false", text="Но на мне это никогда не срабатывало.")
    call process_character (edna, appearance="pose handhip face embarrassed blush false", text="Я выпила немного молока, думая, что лекарства помогут, а потом меня раздуло как воздушный шарик.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="...")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="С другой стороны, я начала больше пить сока!")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="И узнала, что некоторые овощи содержат много кальция для моих костей!")

    call process_end_of_conversation ("edna_convo_4", edna, priority=False, default=False)


    return


label edna_convo_5:
    call process_conversation_beginning ([ (n, "pose handpocket face neutral blush false"), (edna, "pose handhip face neutral blush false mouth red") ])

    call process_character (edna, appearance="pose handhip face neutral blush false mouth red", text="Ты часто ходишь в кино, [n.say_name]?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Я в основном смотрю фильмы дома, если это не фильм, который я хочу увидеть сразу.")
    call process_character (edna, appearance="pose handclasp face happy blush false mouth red", text="Ничто не сравнится с киноэкраном!")
    call process_character (edna, appearance="pose handclasp face happy blush false mouth red", text="Я киноман на самом деле.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Ты?")
    call process_character (edna, appearance="pose handclasp face neutral blush false mouth red", text="Я всегда проверяю, что есть новое и грядущее.")
    call process_character (edna, appearance="pose fisthip face neutral blush false mouth red", text="Самая интересная часть - это проверка рейтинга фильма перед его просмотром.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Так ты узнаешь, хороший он или плохой?")
    call process_character (edna, appearance="pose fisthip face neutral blush false mouth red", text="Это большая причина, да.")
    call process_character (edna, appearance="pose handclasp face curious blush false mouth red", text="Но иногда рейтинги критиков не совпадают с моим мнением о фильме.")
    call process_character (edna, appearance="pose handclasp face curious blush false mouth red", text="То же самое происходит и с рейтингами аудитории.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Интересно.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Я никогда об этом так не думал.")
    call process_character (edna, appearance="pose handhip face neutral blush false mouth red", text="Ты когда-нибудь смотрел фильм, который тебе действительно нравится, но многие люди так не считают?")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Ах да, много раз!")
    call process_character (edna, appearance="pose handhip face neutral blush false mouth red", text="Вот почему я читаю отзывы с недоверием.")
    call process_character (edna, appearance="pose fisthip face neutral blush false mouth red", text="Если я хочу посмотреть фильм, который меня интересует, я не позволю низкому рейтингу оттолкнуть меня.")
    call process_character (edna, appearance="pose fisthip face neutral blush false mouth red", text="В конечном итоге, мое мнение о фильме решающее слово.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Я тоже так считаю!")
    call process_character (edna, appearance="pose handclasp face neutral blush false mouth red", text="Есть так много фильмов, которые существуют в настоящее время, они охватывают все уровни качества.")
    call process_character (edna, appearance="pose handclasp face angry blush false mouth red", text="Я видела фильмы настолько ужасные, что хотела лично пнуть режиссера и сценаристов под задницу!")

    call process_character (n, appearance="pose behindhead face curious blush false")

    call process_character (edna, appearance="pose handhip face happy blush false mouth red", text="Но для действительно хороших фильмов я останусь на месте до конца титров.")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Это хорошая идея, бабушка, чтобы остаться до титров.")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Некоторые фильмы имеют дополнительные сцены после них!")
    call process_character (edna, appearance="pose fisthip face curious blush false mouth red", text="Да?")
    call process_character (edna, appearance="pose fisthip face curious blush false mouth red", text="...")
    call process_character (edna, appearance="pose fisthip face curious blush false mouth red", text="Мне нужно будет следить за этим...")

    call process_end_of_conversation ("edna_convo_5", edna, priority=False, default=False)


    return

label edna_convo_6:
    call process_conversation_beginning ([ (n, "pose handpocket face neutral blush false"), (edna, "pose fisthip face happy blush false mouth red") ])

    call process_character (edna, appearance="pose fisthip face happy blush false mouth red", text="Хотела бы я снова отправиться в плавание.")
    call process_character (edna, appearance="pose fisthip face happy blush false mouth red", text="Но даже маленькая лодка сейчас не в моем бюджете!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты знаешь, как управлять кораблем?")
    call process_character (edna, appearance="pose handhip face neutral blush false mouth red", text="Меня учили с самого раннего возраста.")
    call process_character (edna, appearance="pose handhip face neutral blush false mouth red", text="Я ходила с родителями, и они показывали мне, как ставить мачту.")
    call process_character (edna, appearance="pose handhip face neutral blush false mouth red", text="Это довольно приятное времяпровождение в океане.")
    call process_character (n, appearance="pose handfist face happy blush false", text="Есть ли какие-нибудь крутые места, куда ты можешь уплыть, что никто другой не может?")
    call process_character (edna, appearance="pose handclasp face happy blush false mouth red", text="Это было одно из моих любимых занятий в детстве!")
    call process_character (edna, appearance="pose handclasp face happy blush false mouth red", text="Мы с родителями находили маленькие необитаемые острова и устраивали там пикник.")
    call process_character (edna, appearance="pose handclasp face happy blush false mouth red", text="Это было похоже на маленький кусочек рая!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Звучит так здорово!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Мне нравится находить такие тайные места!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Особенно если это в пустыне!")
    call process_character (edna, appearance="pose handhip face neutral blush false mouth red", text="Я прямо здесь, рядом с тобой.")
    call process_character (edna, appearance="pose handhip face embarrassed blush false mouth red", text="Я никогда не смогу жить в большом городе.")
    call process_character (edna, appearance="pose handhip face embarrassed blush false mouth red", text="Раньше я ездила на свою работу, и всегда боялась.")
    call process_character (edna, appearance="pose fisthip face neutral blush false mouth red", text="Но некоторые люди чувствуют себя менее тревожно в городе.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Что если ты не сможешь жить рядом с океаном, Бабушка?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты хотела бы жить где-нибудь еще?")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Если бы у меня не было океана, я бы жила в горах.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Вау, тебе даже не пришлось об этом думать!")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Горы - следующая лучшая вещь для меня.")
    call process_character (edna, appearance="pose handclasp face neutral blush false", text="Все реки, озера и зеленые деревья скрыты внутри.")
    call process_character (edna, appearance="pose handclasp face happy blush false", text="Я бы без проблем поселилась в таком месте!")

    call process_end_of_conversation ("edna_convo_6", edna, priority=False, default=False)


    return