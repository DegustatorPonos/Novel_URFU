label julia_convo_default:
    call process_conversation_beginning ([ (n, ""), (julia, "") ])

    call debug_message ("Default conversation when none others are available.")
    $ julia.c("Привет " + n.say_name + ".")

    call process_end_of_conversation ("julia_convo_default", julia, priority=False, default=True)

    return

label minigame_julia_book_first_time_intro:
    call process_conversation_beginning ([ (n, "pose behindhead face neutral blush false"), (julia, "pose handface face neutral blush false") ])

    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты читаешь одну из своих книг?")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Ага.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="И как она?")
    call process_character (julia, appearance="pose handup face happy blush false", text="Мне нравится.")
    call process_character (julia, appearance="pose handup face happy blush false", text="Это часть серии.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Я не читаю много.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Моя мама говорит, что я должен читать, чтобы пополнять свой словарный запас.")

    call process_character (julia, appearance="pose handup face neutral blush false")

    call process_character (n, appearance="pose behindhead face neutral blush false", text="Единственные книги, которые я люблю читать, - это фэнтези и научная фантастика.")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Если есть драконы, инопланетяне или ещё какие-нибудь классные штуки, я только за!")
    call process_character (julia, appearance="pose handface face neutral blush false", text="В этой книге много такого.")
    call process_character (julia, appearance="pose handface face happy blush false", text="Фэнтези - один из моих любимых жанров.")
    call process_character (n, appearance="pose handpocket face happy blush false", text="Ох, быть не может!")
    call process_character (n, appearance="pose handpocket face happy blush false", text="Ты не сказала мне, что все твои книги - это фэнтези и прочее!")
    call process_character (julia, appearance="pose handup face curious blush false", text="Я думал, что ты больше любишь видеоигры и фильмы.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ну да, но...")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Я сделаю исключение для таких книг!")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Не стесняйся читать их, если хочешь.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Я уже прочитала большинство из них.")
    call process_character (julia, appearance="pose armcross face happy blush false", text="Было бы здорово, если бы мы могли обсуждать книги вместе.")
    call process_character (n, appearance="pose handfist face happy blush false", text="Я был бы очень рад!")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Некоторые из этих книг довольно сложны.")

    call process_character (n, appearance="pose handpocket face neutral blush false")

    call process_character (julia, appearance="pose handup face neutral blush false", text="У меня есть более легкое чтение, если ты перегружен.")
    call process_character (julia, appearance="pose handup face happy blush false", text="Я буду приятно удивлена, если ты сможешь понять сложные сюжетные линии и персонажей.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Хорошо, спасибо!")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Хм, какую книгу выбрать...")

    call process_end_of_conversation ("minigame_julia_book_first_time_intro", julia, priority=False, considered_scene=True, override_scene_limit=True)

    return

label julia_convo_1:
    call process_conversation_beginning ([(n, "pose handpocket face neutral blush false"), (julia, "pose handup face neutral blush false")])

    call process_character (julia, appearance="pose handup face neutral blush false", text="У вас большой бассейн.")
    call process_character (n, appearance="pose handfist face happy blush false", text="О, да!")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Думаешь сходить к нему?")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Я не очень люблю плавать.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Почему?")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Это просто не в моём вкусе.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Особенно бассейны.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Хлорная вода портит мои волосы.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Хмм...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты всегда можешь посидеть у бассейна.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Честно говоря, мне не очень нравится жара.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Летом я остаюсь в помещении практически двадцать четыре на семь.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Но иногда и это не спасает.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="У меня дома так себе кондиционер.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Не хочешь?")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Нее...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="У нас есть пара кондиционеров.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Но в моей комнате сломался.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Теперь у меня есть только маленький веер.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="В твоей комнате должно быть жарко.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="О, да.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Это жестоко.")

    call process_end_of_conversation ("julia_convo_1", julia, priority=False)

    return

label julia_convo_2:
    call process_conversation_beginning ([(n, "pose handpocket face neutral blush false"), (julia, "pose handface face curious blush false")])

    call process_character (julia, appearance="pose handface face curious blush false", text="Какой длины волосы твоей сестры?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты имеешь ввиду? [sa.say_name]?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Без понятия...")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Но они довольно длинные!")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Я хотела спросить, чем она моет их и, как ухаживает.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="У тебя тоже длинные волосы!")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Ну да...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Я просто позволяю им расти.")
    call process_character (n, appearance="pose handpocket face neutral blush false")
    call process_character (julia, appearance="pose handface face neutral blush false")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Но с ними становится сложно справляться.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Сушка занимает целую вечность.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="И я должна их расчесывать каждый день, чтобы они не запутывались в узлы.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Узлы?")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Девушки с длинными волосами, как правило, сталкиваются с этой проблемой.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Наши волосы скручиваются и запутываются, их постоянно нужно выпрямлять.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Через некоторое время это становится рутиной.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Почему бы просто не подстричь волосы?")
    call process_character (julia, appearance="pose armcross face angry blush false", text="Это главное, что должна сделать девушка!")
    call process_character (julia, appearance="pose armcross face angry blush false", text="Ты знаешь, сколько времени нужно, чтобы отрастить волосы такой длины?")
    call process_character (julia, appearance="pose handface face angry blush false", text="Я выращивала их в течение многих лет.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Лет?")
    call process_character (julia, appearance="pose armcross face curious blush false", text="Да...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Ничего себе, это сумасшествие.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Кроме того...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Несмотря на мои жалобы, я горжусь своими волосами.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Я могу делать разные причёски.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Типа такой штуки на твоих волосах спереди?")
    call process_character (julia, appearance="blush false", text="Она называются челка, [n.say_name].")
    call process_character (n, appearance="pose handpocket face happy blush false", text="Оой...")
    call process_character (n, appearance="pose handpocket face happy blush false", text="Я не знал, что у них есть такое название!")
    call process_character (julia, appearance="pose armcross face embarrassed blush false", text="(Надеюсь, его сестра знает о волосах больше, чем он!)")

    call process_end_of_conversation ("julia_convo_2", julia, priority=False)

    return

label julia_convo_3:
    call process_conversation_beginning ([(n, "pose handpocket face neutral blush false"), (julia, "pose handup face neutral blush false")])

    call process_character (julia, appearance="pose handup face neutral blush false", text="Это всё, что у вас есть, как фрукты и овощи?")
    call process_character (julia, appearance="pose handup face neutral blush false", text="А где вся хорошая еда?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Хорошая еда?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Ты имеешь в виду хлопья?")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Нет, я имею в виду...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Шоколад, мороженое, или может арахисовое масло?")
    call process_character (n, appearance="pose behindhead face happy blush false", text="Ооо...")
    call process_character (n, appearance="pose behindhead face happy blush false", text="Ну немного есть этого.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Я знаю, [sa.say_name] любит делать тосты с арахисовым маслом и шоколадной крошкой.")
    call process_character (julia, appearance="pose handface face happy blush false", text="Ммм...")
    call process_character (julia, appearance="pose handface face happy blush false", text="Твоя сестра дала мне хорошую идею.")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Нашей маме обычно не нравится, что у нас слишком много такой еды.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="По крайней мере, твоя Мама время от времени покупает сладости.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Твоя Мама не разрешает тебе есть шоколад или арахисовое масло?")

    call process_character (julia, appearance="pose armcross face angry blush false", text="Черт возьми, нет!")
    call process_character (julia, appearance="pose armcross face angry blush false", text="Она бы совсем взбесилась!")
    call process_character (julia, appearance="pose armcross face angry blush false", text="Если бы мы могли жить только на витаминах, это все, чем она кормила бы меня!")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Но всякий раз, когда мы посещали вас, у нас было много еды.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Это потому, что вы были гостями.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Но когда мы с ней одни, снова приходится жевать энергетические батончики и пить галлон воды в день.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Это отстой...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="...")
    call process_character (n, appearance="pose handfist face happy blush false", text="По крайней мере, здесь есть еда, которая тебе понравится!")

    call process_character (julia, appearance="pose handup face neutral blush false", text="Я знаю одну вещь.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="У меня дома легко сесть на диету...")

    call process_end_of_conversation ("julia_convo_3", julia, priority=False)

    return

label julia_convo_4:
    call process_conversation_beginning ([(n, "pose handpocket face neutral blush false"), (julia, "pose handface face neutral blush false")])

    call process_character (n, appearance="pose behindhead face neutral blush false", text="Я слышал ты пишешь рассказы, [julia.say_name]?")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Да.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Иногда да.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Откуда ты знаешь, что я пишу?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="[k.say_name] сказала мне.")
    call process_character (julia, appearance="pose armcross face curious blush false", text="[k.say_name] сказала?")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="Она прочитала кое-что из твоих вещей.")
    call process_character (julia, appearance="pose handface face curious blush false", text="...")
    call process_character (julia, appearance="pose handface face curious blush false", text="Что она сказала про них?")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Она сказала что-то вроде того, что это было не так уж плохо.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Я надеюсь стать лучше.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Мне сказали, чтобы я стала хорошим писателем, то должна читать и писать всё время.")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Ты определенно много читаешь!")
    call process_character (n, appearance="pose handfist face neutral blush false", text="Ты писала здесь?")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Я работаю над рассказом, да.")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="ой!")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="Могу я почитать?")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="...{p}...")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Конечно.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Вот.")
    call process_character (n, appearance="pose handpocket face neutral blush false", text="...{p}...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="Хм...")
    call process_character (n, appearance="pose behindhead face neutral blush false", text="...{p}...")
    call process_character (n, appearance="pose behindhead face happy blush false", text="Мм!")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (n, appearance="pose behindhead face happy blush false", text="...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="О, это круто...")
    call process_character (n, appearance="pose handfist face neutral blush false", text="...{p}...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="...")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Каково впечатление от этого?")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="Мне понравилось!")
    call process_character (n, appearance="pose twohandfist face neutral blush false", text="У этого волшебника есть несколько классных заклинаний.")
    call process_character (n, appearance="pose twohandfist face happy blush false", text="И эти Парящие Королевства классные!")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Да, я пыталась обратить внимание на классическое фэнтези.")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Хотя...")
    call process_character (n, appearance="pose behindhead face concerned blush false", text="Местами немного трудно понимать текст...")
    call process_character (julia, appearance="pose armcross face curious blush false", text="Что именно?")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Нуу...")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Было трудно понять описания некоторых персонажей и мест.")
    call process_character (n, appearance="pose handpocket face curious blush false", text="Как много сложных слов я не знаю...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Потом найди слова в интернете.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="Все до единого?")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Чтение помогает нам выучить термины, которые не знали.")
    call process_character (julia, appearance="pose handface face neutral blush false", text="Так что я хотела бы, да.")
    call process_character (n, appearance="pose behindhead face curious blush false", text="...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Я чувствую, что все эти слова сделали историю не такой забавной для чтения...")
    call process_character (n, appearance="pose behindhead face curious blush false", text="Мне придется останавливаться каждый раз, когда я вижу слово, которого не знаю.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Это пока мой последний рассказ, так что навык написания книг ещё растёт.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Ты читаешь не так много, как я [n.say_name].")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Таким образом, твой словарный запас более ограничен.")
    call process_character (julia, appearance="pose armcross face neutral blush false", text="Вот почему у тебя возникают трудности.")
    call process_character (n, appearance="pose handpocket face concerned blush false", text="...")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Советую тебе прочитать моё раннее творчество.")
    call process_character (julia, appearance="pose handup face neutral blush false", text="Они должны быть более доступными.")

    call process_end_of_conversation ("julia_convo_4", julia, priority=False)

    return


label julia_convo_5:




    call process_end_of_conversation ("julia_convo_5", julia, priority=True, considered_scene=True)

    return