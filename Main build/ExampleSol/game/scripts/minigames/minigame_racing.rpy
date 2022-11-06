init python:
    def minigame_racing_textbutton_action(letter):
        store.minigame_racing_textbutton_clicked = True
        return letter

    def minigame_racing_player_boost_amount():
        if store.inventory.has_item(1):
            return 1
        return 0

    def get_minigame_racing_buttons_to_press_string():
        array = store.minigame_racing_buttons_to_press
        text = store.minigame_racing_prompt_prefix + " "
        
        for i in range (0, len(array)):
            letter = array[i]
            
            if letter != store.minigame_racing_button_to_press:
                letter = "{color=#808080}" + letter + "{/color}"
            else:
                letter = "{size=+12}" + letter + "{/size}"
            
            text += letter
            
            if (i < len(array) - 1):
                text += " и "
        
        
        text += " быстрее!"
        
        return text

    def generate_list_of_letters_shuffled():
        letters = copy.deepcopy(string.ascii_lowercase)
        letters = list(letters)
        letters.remove('h')
        letters.remove('l')
        random.shuffle(letters)
        
        return letters


    def generate_easy_racing_button_presses():
        store.minigame_racing_buttons_objs = []
        
        store.minigame_racing_buttons_objs.extend( generate_single_button_presses(5) )
        
        random.shuffle(store.minigame_racing_buttons_objs)
        
        return

    def generate_medium_racing_button_presses():
        store.minigame_racing_buttons_objs = []
        
        store.minigame_racing_buttons_objs.extend( generate_single_button_presses(5) )
        store.minigame_racing_buttons_objs.extend( generate_multiple_button_presses(2, 5) )
        
        random.shuffle(store.minigame_racing_buttons_objs)
        
        return

    def generate_hard_racing_button_presses():
        store.minigame_racing_buttons_objs = []
        
        store.minigame_racing_buttons_objs.extend( generate_single_button_presses(2) )
        store.minigame_racing_buttons_objs.extend( generate_multiple_button_presses(2, 3) )
        store.minigame_racing_buttons_objs.extend( generate_multiple_button_presses(3, 5) )
        
        random.shuffle(store.minigame_racing_buttons_objs)
        
        return

    def generate_racing_button_presses():
        if store.minigame_racing_difficulty == "easy":
            generate_easy_racing_button_presses()
        elif store.minigame_racing_difficulty == "medium":
            generate_medium_racing_button_presses()
        else:
            generate_hard_racing_button_presses()
        
        return

    def generate_word_button_presses(num):
        words = ['fast', 'run', 'jog', 'jet', 'bolt', 'go', 'sis', 'bro', 'win', 'zip', 'far']
        button_objs = []
        
        word_bank = copy.deepcopy(words)
        random.shuffle(word_bank)
        prefix = "Нажимайте"
        
        for i in range(0, num):
            if len(word_bank) <= 0:
                word_bank = copy.deepcopy(string.ascii_lowercase)
                random.shuffle(word_bank)
            
            word = word_bank.pop()
            letter_array = list(word)
            letter_count = len(letter_array)
            presses = 15 - (2 * (letter_count - 2) )
            presses = int(presses * minigame_racing_press_multiplier)
            step_amount = store.minigame_racing_kira_step_amount + (letter_count - 0)
            
            button_objs.append({ "letter_array": letter_array, "presses": presses, "step_amount": step_amount, "prefix": prefix })
        
        return button_objs

    def generate_single_button_presses(num):
        button_objs = []
        letters = generate_list_of_letters_shuffled()
        presses = 20
        presses = int(presses * minigame_racing_press_multiplier)
        prefix = "Нажимайте"
        
        step_amount = store.minigame_racing_kira_step_amount + 6
        
        for i in range(0, num):
            if len(letters) <= 0:
                letters = generate_list_of_letters_shuffled()
            
            letter = letters.pop()
            button_objs.append({ "letter_array": [letter], "presses": presses, "step_amount": step_amount, "prefix": prefix })
        
        return button_objs

    def generate_multiple_button_presses(letter_count, num):
        button_objs = []
        letters = generate_list_of_letters_shuffled()
        presses = 15 - (2 * (letter_count - 2) )
        presses = int(presses * minigame_racing_press_multiplier)
        step_amount = store.minigame_racing_kira_step_amount + (letter_count - 0)
        prefix = "Нажимайте"
        
        
        for i in range(0, num):
            letter_array = []
            
            for j in range(0, letter_count):
                if len(letters) <= 0:
                    letters = generate_list_of_letters_shuffled()
                
                letter_array.append(letters.pop())
            
            button_objs.append({ "letter_array": letter_array, "presses": presses, "step_amount": step_amount, "prefix": prefix })
        
        return button_objs

    def set_current_racing_button_obj():
        store.minigame_racing_buttons_obj = store.minigame_racing_buttons_objs[0]
        store.minigame_racing_buttons_to_press = store.minigame_racing_buttons_obj.get("letter_array")
        store.minigame_racing_button_to_press = store.minigame_racing_buttons_to_press[store.minigame_racing_button_index]
        store.minigame_racing_prompt_prefix = store.minigame_racing_buttons_obj.get("prefix")
        
        
        return

screen minigame_racing_button_prompts:
    hbox:
        xalign 0.5

        if minigame_racing_partner == k:
            yalign 0.2
        else:
            yalign 0.1

        text store.minigame_racing_prompt_prefix + " " size 60

        for i in range (0, len(store.minigame_racing_buttons_to_press)):
            $ letter = store.minigame_racing_buttons_to_press[i]

            $ letter_text = letter
            $ letter_size = 92
            $ letter_y = 24
            if letter != store.minigame_racing_button_to_press:
                $ letter_size -= 24
                $ letter_text = "{color=#808080}" + letter + "{/color}"

            textbutton letter_text action Function(minigame_racing_textbutton_action, letter) text_size letter_size ypos letter_y

            if (i < len(store.minigame_racing_buttons_to_press) - 1):
                text " и " size 60


        text " быстрее!" size 60

screen minigame_racing(partner=k):
    if minigame_racing_started and not minigame_racing_finished:
        timer minigame_racing_update_speed action Return("progress kira") repeat True

        use keymaps










    vbox:
        if partner == k:
            yalign 0.55
            spacing 25
        else:
            spacing 10
            yalign 0.3
        add n.racing_icon(minigame_racing_player_x, minigame_racing_kira_x) xpos minigame_racing_player_x xalign 1.0
        add partner.racing_icon(minigame_racing_kira_x, minigame_racing_player_x) xpos minigame_racing_kira_x xalign 1.0

label minigame_racing_first_time_intro:
    call process_conversation_beginning ([ (n, ""), (k, "pose handhip") ])

    call process_character (k, appearance="pose handhip face neutral", text="Я видела хорошую беговую дорожка поблизости.")
    call process_character (k, appearance="pose armsup face neutral", text="Идеальное место, чтобы позаниматься пока я на улице.")
    call process_character (n, appearance="pose handpocket face neutral", text="Да?")
    call process_character (k, appearance="pose handhip face neutral", text="Ты должен присоединиться ко мне.")
    call process_character (k, appearance="pose armcross face neutral", text="Не могу же я весь день сидеть дома и играть в видеоигры.")
    call process_character (k, appearance="pose armcross face neutral", text="Даже небольшое упражнение может дать хороший результат.")
    call process_character (n, appearance="pose behindhead face neutral", text="Нуу...{p=0.5}Думаю, я попробую как-нибудь.")
    call process_character (k, appearance="pose armsup face neutral", text="Я уверена тебе понравится.")
    call process_character (k, appearance="pose armsup face neutral", text="и это...")
    call process_character (k, appearance="pose armcross face happy", text="Мы могли бы даже повеселиться, соревнуясь друг с другом.")
    call process_character (n, appearance="pose behindhead face embarrassed", text="С-соревноваться с тобой?")
    call process_character (k, appearance="pose handhip face neutral", text="Не волнуйся, я буду с тобой помягче.")
    call process_character (k, appearance="pose handhip face happy", text="По большей части.")
    call process_character (n, appearance="pose handpocket face concerned", text="Думаешь, я смогу бежать так же быстро, как ты?")
    call process_character (k, appearance="pose armcross face neutral", text="Есть только один способ узнать.")
    call process_character (k, appearance="pose armcross face neutral", text="Просто скажи мне, когда захочешь отправиться на беговую дорожку.")
    call process_character (k, appearance="pose armsup face happy", text="Тогда и проверим твою выносливость.")
    call process_character (n, appearance="pose handpocket face curious", text="...")
    call process_character (k, appearance="pose handhip face neutral", text="И мы можем сделать это немного интереснее.")
    call process_character (n, appearance="pose handpocket face concerned", text="Как?")
    call process_character (k, appearance="pose handhip face neutral", text="Мы можем поспорить, кто победит.")
    call process_character (n, appearance="pose handpocket face curious", text="Поспорим?")
    call process_character (k, appearance="pose armcross face neutral", text="Ну знаешь, ставки.")
    call process_character (k, appearance="pose armcross face neutral", text="Я положу пару долларов, ты положишь пару.")
    call process_character (k, appearance="pose armsup face happy", text="И тот, кто выиграет, получит все!")
    call process_character (n, appearance="pose behindhead face concerned", text="Но у меня нет денег.")
    show screen hud
    call process_character (k, appearance="pose handhip face neutral", text="А, точно.")
    $ inventory.add_money(10, tag = "minigame_racing_first_time_intro_money_start")
    call process_character (k, appearance="pose armcross face neutral", text="Вот, десять долларов для начала.")
    hide screen hud
    call process_character (n, appearance="pose twohandfist face neutral", text="О, спасибо!")
    call process_character (k, appearance="pose armcross face neutral", text="Мне самой интересно, сможешь ли ты увеличить эту сумму.")
    call process_character (n, appearance="pose handpocket face neutral")
    call process_character (k, appearance="pose armsup face neutral", text="Но если бы я была тобой,")
    call process_character (k, appearance="pose armsup face neutral", text="Я бы не стала слишком рисковать, пока не будешь уверен, что есть шанс.")
    call process_character (k, appearance="pose armsup face happy", text="(Небольшой шанс...)")

    call process_end_of_conversation ("minigame_racing_first_time_intro", k, priority=False, considered_scene=True, override_scene_limit=True)

    return

label minigame_racing(partner=k):
    $ renpy.scene('screens')
    $ no_bust_art = False
    $ diceroll = random.randint(1,3)
    $ minigame_racing_partner = partner
    $ exec( "minigame_racing_forced_" + partner.internal_name + "_face = \"\"")

    if partner != janet and partner.outfit != "clothes":
        call character_leave_dissolve (partner)
        $ renpy.pause(1)

    if partner == k:
        if diceroll == 1:
            call process_conversation_beginning ([ (n, "outfit clothesjacket"), (k, "outfit clothes pose armcross face neutral") ])
            call process_character (k, appearance="pose armcross face neutral", text="Так ты хочешь участвовать в гонках?")
            call process_character (k, appearance="pose armcross face neutral", text="Ладно, поехали.")
        elif diceroll == 2:
            call process_conversation_beginning ([ (n, "outfit clothesjacket"), (k, "outfit clothes pose armcross face neutral") ])
            call process_character (k, appearance="pose armcross face neutral", text="Посмотрим, как ты справишься на этот раз.")
        else:
            call process_conversation_beginning ([ (n, "outfit clothesjacket"), (k, "outfit clothes pose armsup face neutral") ])
            call process_character (k, appearance="pose armsup face neutral", text="Сегодня самое то, побегать!")

        $ play_music("audio/music/Fashion.ogg", fadeout=1.0, fadein = 1.0)
        call process_new_location ("bg racing_track", char_tuple_array=[ (n, "outfit clothesjacket"), (k, "outfit clothes") ])
    elif partner == janet:
        if diceroll == 1:
            $ display_multiple_characters([ (n, "outfit clothesjacket"), (janet, "outfit clothes pose handface face neutral blush false") ])
            call process_character (janet, appearance="pose handface face neutral blush false", text="Ничто не сравнится с плаванием!")
            call process_character (janet, appearance="pose handface face neutral blush false", text="Я буду готова, когда ты будешь готов!")
        elif diceroll == 2:
            $ display_multiple_characters([ (n, "outfit clothesjacket"), (janet, "outfit clothes pose handchest face happy blush false") ])
            call process_character (janet, appearance="pose handchest face happy blush false", text="Мне нравится плавать кролем.")
            call process_character (janet, appearance="pose handchest face happy blush false", text="Я чувствую, будто скольжу по волнам!")
        else:
            $ display_multiple_characters([ (n, "outfit clothesjacket"), (janet, "outfit clothes pose handhips face happy blush false") ])
            call process_character (janet, appearance="pose handhips face happy blush false", text="Прямо как рыба в воде!")

        $ play_music("audio/music/Fashion.ogg", fadeout=1.0, fadein = 1.0)
        call process_new_location ("bg swimming_minigame", char_tuple_array=[ (n, "outfit swimsuit"), (janet, "outfit swimsuit") ])





    python:
        minigame_racing_press_multiplier = 1.0
        minigame_racing_update_speed = 0.2
        minigame_racing_finished = False
        minigame_racing_started = False
        minigame_racing_finish_x = 1900
        minigame_racing_difficulty = "easy"
        minigame_racing_forced_nate_face = None
        minigame_racing_forced_kira_face = None
        minigame_racing_win_lose_big_threshold = .30
        minigame_racing_player_boost = minigame_racing_player_boost_amount() + 1
        minigame_racing_textbutton_clicked = False
        minigame_racing_bet_amount = 0

        minigame_racing_system_message = ""
        minigame_racing_button_index = 0
        minigame_racing_buttons_to_press = []
        minigame_racing_buttons_objs = []
        minigame_racing_button_to_press = ""
        minigame_racing_prompt_prefix = "Mash"

    if partner == k:
        menu:
            "Лёгкая":
                call process_character (k, appearance="pose handhip face curious", text="Я тебя и пешком обгоню!")
                call minigame_racing_easy_settings
            "Средняя (Увеличение Смелости)":
                call process_character (k, appearance="pose handhip face neutral", text="Наращиваешь обороты, не плохо!")
                call minigame_racing_medium_settings
            "Тяжёлая (Увеличение Смелости)":
                call process_character (k, appearance="pose armsup face happy", text="Хех, хорошо [n.say_name].")
                call process_character (k, appearance="pose armsup face happy", text="Ты просишь о вызове, я его дам!")
                call minigame_racing_hard_settings
    elif partner == janet:
        menu:
            "Лёгкая":
                $ diceroll = random.randint(1,2)

                if diceroll == 1:
                    call process_character (janet, appearance="pose handchest face neutral blush false", text="Я просто буду бить ногами по воде.")
                    call process_character (janet, appearance="pose handchest face neutral blush false", text="Это будет держать мой темп медленным и устойчивым.")
                else:
                    call process_character (janet, appearance="pose handhips face neutral blush false", text="Чем медленнее, тем лучше тренируешься!")

                call minigame_racing_easy_settings
            "Средняя (Увеличение Смелости)":
                $ diceroll = random.randint(1,2)

                if diceroll == 1:
                    call process_character (janet, appearance="pose handchest face neutral blush false", text="Это средний темп для меня.")
                else:
                    call process_character (janet, appearance="pose handface face neutral blush false", text="Надеюсь, наши брызги не привлекут акул!")
                    call process_character (janet, appearance="pose handface face happy blush false", text="Я просто прикалываюсь!")
                    call process_character (janet, appearance="pose handface face happy blush false", text="Их здесь нет!")

                call minigame_racing_medium_settings
            "Тяжёлая (Увеличение Смелости)":
                $ diceroll = random.randint(1,2)

                if diceroll == 1:
                    call process_character (janet, appearance="pose handface face neutral blush false", text="Наши руки будут свинцовыми!")
                else:
                    call process_character (janet, appearance="pose handhips face happy blush false", text="Кажется, у тебя такой же соревновательный дух, как и у старшей сестры!")

                call minigame_racing_hard_settings

    if partner == k:
        if store.inventory.money >= 2:
            show screen hud
            window hide
            menu:
                "Ничего не ставить":
                    pass
                "Поставить $2" if store.inventory.money >= 2:
                    $ minigame_racing_bet_amount = 2
                "Поставить $3" if store.inventory.money >= 3:
                    $ minigame_racing_bet_amount = 3
                "Поставить $4" if store.inventory.money >= 4 and minigame_racing_difficulty != "easy":
                    $ minigame_racing_bet_amount = 4
                "Поставить $5" if store.inventory.money >= 5 and minigame_racing_difficulty == "hard":
                    $ minigame_racing_bet_amount = 5

            window hide
            if minigame_racing_bet_amount > 0:
                pause 0.75
                $ inventory.add_money(-minigame_racing_bet_amount)
                pause 1.75

            hide screen hud

    python:




        clear_characters()
        quick_menu = False
        generate_racing_button_presses()
        set_current_racing_button_obj()

    window hide
    $ disable_rollback()
    $ disable_saving()
    show screen minigame_racing(partner)
    call minigame_countdown (2.99, "minigame_racing_start", xalign=0.5, yalign=0.5, show_decimal=False, call_instead_of_show=True, addend=1, red_text=False)

    return

label minigame_racing_start:
    hide countdown
    hide screen minigame_countdown
    show screen minigame_racing_button_prompts

    $ minigame_racing_started = True
    call minigame_stopwatch_start (xalign=0.5)
    call minigame_racing_loop

    return

label minigame_racing_easy_settings:
    python:
        minigame_racing_difficulty = "easy"
        minigame_racing_desired_kira_finish_duration = 45
        minigame_racing_kira_step_amount = 7
        minigame_racing_player_x = 240
        minigame_racing_kira_x = 240

    return

label minigame_racing_medium_settings:
    python:
        minigame_racing_difficulty = "medium"
        minigame_racing_desired_kira_finish_duration = 90
        minigame_racing_kira_step_amount = 6

        minigame_racing_player_x = 240
        minigame_racing_kira_x = 240

    return

label minigame_racing_hard_settings:
    python:
        minigame_racing_press_multiplier = 1.0
        minigame_racing_difficulty = "hard"
        minigame_racing_desired_kira_finish_duration = 90
        minigame_racing_kira_step_amount = 8

        minigame_racing_player_x = 240
        minigame_racing_kira_x = 440

    return

label minigame_racing_loop:
    if minigame_racing_finished:
        return

    python:
        interaction_return = ui.interact()

        if interaction_return == minigame_racing_button_to_press:
            minigame_racing_system_message = ""
            minigame_racing_player_x_addend = minigame_racing_buttons_obj.get("step_amount") + minigame_racing_player_boost
            
            if minigame_racing_textbutton_clicked:
                if len(store.minigame_racing_buttons_to_press) > 1:
                    minigame_racing_textbutton_clicked_multiplier = 1.5
                else:
                    minigame_racing_textbutton_clicked_multiplier = 0
                
                minigame_racing_textbutton_clicked_addend = int(minigame_racing_buttons_obj.get("step_amount") * minigame_racing_textbutton_clicked_multiplier)
                minigame_racing_player_x_addend += minigame_racing_textbutton_clicked_addend
            
            minigame_racing_player_x += min( minigame_racing_player_x_addend, minigame_racing_finish_x - minigame_racing_player_x)
            
            
            
            minigame_racing_button_index += 1
            
            if (minigame_racing_button_index >= len(minigame_racing_buttons_to_press)):
                minigame_racing_buttons_obj["presses"] = minigame_racing_buttons_obj.get("presses") - 1
                minigame_racing_button_index = 0
                
                if minigame_racing_buttons_obj.get("presses") <= 0:
                    minigame_racing_buttons_objs.pop(0)
                    
                    if len(minigame_racing_buttons_objs) <= 0:
                        generate_racing_button_presses()
            
            set_current_racing_button_obj()
            minigame_racing_textbutton_clicked = False

        elif interaction_return == "progress kira":
            minigame_racing_kira_x += min( minigame_racing_kira_step_amount, minigame_racing_finish_x - minigame_racing_kira_x)
        else:
            minigame_racing_system_message = "Неверная кнопка. Вы нажали " + interaction_return

    if minigame_racing_player_x >= minigame_racing_finish_x:
        jump minigame_racing_win
    if minigame_racing_kira_x >= minigame_racing_finish_x:
        jump minigame_racing_lose

    jump minigame_racing_loop
    return

label minigame_racing_win:
    call minigame_racing_result (won=True)
    return

label minigame_racing_lose:
    call minigame_racing_result (won=False)

    return

label minigame_racing_result(won=False):
    hide screen minigame_racing_button_prompts
    call minigame_stopwatch_stop
    $ minigame_racing_finished = True
    $ enable_saving()



    if won:

        if minigame_racing_partner == k:
            if minigame_racing_difficulty == "easy":
                call add_points (k, 2, minigame=True)
            elif minigame_racing_difficulty == "medium":
                call add_points_and_boldness (k, 3, 1, minigame=True)
            else:
                call add_points_and_boldness (k, 4, 1, minigame=True)

            if minigame_racing_difficulty == "easy" or minigame_racing_difficulty == "medium":
                if minigame_racing_player_x > int( minigame_racing_kira_x + ( minigame_racing_kira_x * minigame_racing_win_lose_big_threshold) ):
                    $ minigame_racing_forced_kira_face = "_Curious"
                    call process_character (k, appearance="", text="Я не могла проиграть!")
                else:
                    $ minigame_racing_forced_kira_face = "_Happy"
                    call process_character (k, appearance="", text="Вот это, да!")
            else:
                if minigame_racing_player_x > int( minigame_racing_kira_x + ( minigame_racing_kira_x * minigame_racing_win_lose_big_threshold) ):
                    $ minigame_racing_forced_kira_face = "_Happy"
                    call process_character (k, appearance="", text="(Похоже, у моего младшего брата больше упорства, чем я думала)")
                else:
                    $ minigame_racing_forced_kira_face = "_Neutral"
                    call process_character (k, appearance="", text="(Ну ты знаешь...)")


            if minigame_racing_bet_amount > 0:
                show screen hud
                window hide
                pause 0.5
                $ inventory.add_money(minigame_racing_bet_amount * 2, minigame = True)
                pause 1.5

        elif minigame_racing_partner == janet:
            if minigame_racing_difficulty == "easy":
                $ minigame_racing_reward = 4
                call process_character (janet, appearance="pose handface face happy blush false", text="Надо было плыть быстрее!")
                call process_character (janet, appearance="pose handface face happy blush false", text="Ты с лёгкостью меня обогнал!")
                call add_points_and_boldness (janet, 2, 1, minigame=True)
            elif minigame_racing_difficulty == "medium":
                $ minigame_racing_reward = 6
                call process_character (janet, appearance="pose handhips face happy blush false", text="Мой племянник настоящий пловец!")
                call add_points_and_boldness (janet, 3, 1, minigame=True)
            else:
                $ minigame_racing_reward = 8
                $ diceroll = random.randint(1,2)

                if diceroll == 1:
                    call process_character (janet, appearance="pose handface face happy blush false", text="Я думаю, ты наполовину дельфин!")
                    call process_character (janet, appearance="pose handface face happy blush false", text="Это единственный способ объяснить твою скорость!")
                else:
                    call process_character (janet, appearance="pose handchest face happy blush false", text="Если бы я могла так плавать, когда была в твоем возрасте...")
                    call process_character (janet, appearance="pose handchest face happy blush false", text="У меня была бы куча трофеев!")

                call add_points_and_boldness (janet, 4, 1, minigame=True)

            show screen hud
            window hide
            pause 0.5
            $ inventory.add_money(minigame_racing_reward, minigame = True)
            pause 1.5
    else:

        if minigame_racing_partner == k:
            if minigame_racing_kira_x > int( minigame_racing_player_x + ( minigame_racing_player_x * minigame_racing_win_lose_big_threshold) ):
                $ minigame_racing_forced_kira_face = "_Curious"
                call process_character (k, appearance="", text="Что это было?")
                call process_character (k, appearance="", text="Я знаю, что ты способен на большее.")
            else:
                $ minigame_racing_forced_kira_face = "_Neutral"
                call process_character (k, appearance="", text="Это было близко, [n.say_name]!")
                call process_character (k, appearance="", text="Просто нужно сильно надавить на последнем участке!")
        elif minigame_racing_partner == janet:
            if minigame_racing_difficulty == "easy":
                call process_character (janet, appearance="pose handface face concerned blush false", text="Ты заблудился?")
            elif minigame_racing_difficulty == "medium":
                call process_character (janet, appearance="pose handhips face neutral blush false", text="Не спи на ходу!")
            else:
                call process_character (janet, appearance="pose handchest face neutral blush false", text="Эй, ты хотя бы пытался!")
                call process_character (janet, appearance="pose handchest face neutral blush false", text="Я успела высохнуть пока тебя ждала!")

    $ renpy.block_rollback()
    $ enable_rollback()
    $ quick_menu = True

    $ renpy.scene('screens')
    call process_end_of_minigame ("minigame_racing")
    return