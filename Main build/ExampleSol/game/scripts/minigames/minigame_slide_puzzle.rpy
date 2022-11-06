init python:
    def minigame_slide_puzzle_random_picture():
        pictures = []
        pictures.append("images/bg/house/bg backyard_daytime.png")
        pictures.append("images/bg/house/bg kira_room_daytime.png")
        pictures.append("images/bg/house/bg kitchen_daytime.png")
        pictures.append("images/bg/house/bg living_room_daytime.png")
        pictures.append("images/bg/house/bg nate_room_daytime.png")
        pictures.append("images/bg/house/bg sam_room_daytime.png")
        pictures.append("images/bg/house/bg sam_room_evening.png")
        pictures.append("images/bg/house/bg simone_room_daytime.png")
        pictures.append("images/bg/house/bg hallway_daytime.png")
        return random.choice(pictures)

    def minigame_slide_puzzle_perform_swap(old_row, old_col, new_row, new_col, puzzle_piece):
        store.minigame_slide_puzzle_layout[new_row][new_col] = puzzle_piece
        store.minigame_slide_puzzle_layout[old_row][old_col] = None
        puzzle_piece.row = new_row
        puzzle_piece.column = new_col
        
        
        renpy.restart_interaction()
        
        
        if not store.minigame_slide_puzzle_check_for_win:
            return
        
        if minigame_slide_puzzle_test_win():
            renpy.call("minigame_slide_puzzle_win")
        
        return

    def minigame_slide_puzzle_test_win():
        test_index = 0
        
        for row_i in range(0, store.minigame_slide_puzzle_rows):
            for displayable in minigame_slide_puzzle_layout[row_i]:
                if displayable:
                    if displayable.index != test_index:
                        return False
                
                test_index += 1
        
        return True

    class Slide_Puzzle_Piece(renpy.display.behavior.ImageButton):
        def __init__(self, child, index, row = 0, column = 0, **kwargs):
            self.row = row
            self.column = column
            self.index = index
            
            self.crop_x = (self.index % store.minigame_slide_puzzle_rows) * store.minigame_slide_puzzle_piece_width
            self.crop_y = (math.floor(self.index / float( store.minigame_slide_puzzle_rows ) )) * store.minigame_slide_puzzle_piece_height
            self.crop_width = store.minigame_slide_puzzle_piece_width
            self.crop_height = store.minigame_slide_puzzle_piece_height
            
            self.border_color = "#a223cc"
            
            
            t = Transform(child, crop = (self.crop_x, self.crop_y, self.crop_width, self.crop_height ) )
            
            idle_image = t
            
            
            
            super(Slide_Puzzle_Piece, self).__init__(idle_image = idle_image, clicked = self.slide_puzzle_click_function, **kwargs)
        
        
        def slide_puzzle_click_function(self):
            if store.minigame_slide_puzzle_disable_puzzle_interaction:
                return None
            
            old_row = self.row
            old_col = self.column
            should_swap = False
            
            
            if old_row != 0:
                if store.minigame_slide_puzzle_layout[old_row - 1][old_col] is None:
                    self.perform_swap(old_row -1, old_col)
                    return
            
            
            if old_row != store.minigame_slide_puzzle_rows - 1:
                if store.minigame_slide_puzzle_layout[old_row + 1][old_col] is None:
                    self.perform_swap(old_row + 1, old_col)
                    return
            
            
            if old_col != 0:
                if store.minigame_slide_puzzle_layout[old_row][old_col - 1] is None:
                    self.perform_swap(old_row, old_col - 1)
                    return
            
            
            if old_col != store.minigame_slide_puzzle_columns - 1:
                if store.minigame_slide_puzzle_layout[old_row][old_col + 1] is None:
                    self.perform_swap(old_row, old_col + 1)
                    return
            
            return
        
        def perform_swap(self, new_row, new_col):
            minigame_slide_puzzle_perform_swap(self.row, self.column, new_row, new_col, self)
            
            return
        
        def render(self, width, height, st, at):
            render = super(Slide_Puzzle_Piece, self).render(width, height, st, at)
            
            if self.is_focused() and not store.minigame_slide_puzzle_disable_puzzle_interaction:
                if 1 + 1 == 3:
                    hover_black = Solid("#000000", xsize = self.crop_width, ysize = self.crop_height)
                    hover_black_t = Transform(hover_black, alpha = 0.5 )
                    render.blit( renpy.render(hover_black_t, width, height, st, at), ( 0,  0), False)
                else:
                    hover_border_size = 10
                    
                    top_hover_border = Fixed( Solid(self.border_color, xsize = self.crop_width, ysize = hover_border_size, xalign = 0.0, yalign = 0.0), xysize = ( int( render.width ), int( render.height ) ) )
                    bottom_hover_border = Fixed( Solid(self.border_color, xsize = self.crop_width, ysize = hover_border_size, xalign = 0.0, yalign = 1.0), xysize = ( int( render.width ), int( render.height ) ) )
                    
                    left_hover_border = Fixed( Solid(self.border_color, xsize = hover_border_size, ysize = self.crop_height, xalign = 0.0, yalign = 0.0), xysize = ( int( render.width ), int( render.height ) ) )
                    right_hover_border = Fixed( Solid(self.border_color, xsize = hover_border_size, ysize = self.crop_height, xalign = 1.0, yalign = 0.0), xysize = ( int( render.width ), int( render.height ) ) )
                    
                    render.blit( renpy.render(top_hover_border, width, height, st, at), ( 0,  0), False)
                    render.blit( renpy.render(bottom_hover_border, width, height, st, at), ( 0,  0), False)
                    render.blit( renpy.render(left_hover_border, width, height, st, at), ( 0,  0), False)
                    render.blit( renpy.render(right_hover_border, width, height, st, at), ( 0,  0), False)
            
            if store.minigame_slide_puzzle_difficulty != "medium":
                text = Fixed( Text(str(self.index + 1), xalign = 0.5, yalign = 0.5, size = 64), xysize = ( int( render.width ), int( render.height ) ) )
                render.blit(renpy.render( text, width, height, st, at), ( 0,  0), False)
            
            return render

screen slide_puzzle_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        for row_i in range(0, minigame_slide_puzzle_rows):
            hbox:
                for displayable in minigame_slide_puzzle_layout[row_i]:
                    if displayable:
                        add displayable
                    else:
                        null width minigame_slide_puzzle_piece_width height minigame_slide_puzzle_piece_height
                    null width 2
            null height 2

    if not minigame_slide_puzzle_disable_puzzle_interaction:
        textbutton "Give Up" action Jump("minigame_slide_puzzle_too_slow") xalign 0.99 yalign 0.99

label minigame_slide_puzzle(partner=None):
    call process_scene_beginning
    call minigame_slide_puzzle_intro (partner)
    call minigame_slide_puzzle_initialize
    call minigame_slide_puzzle_begin

    return



label minigame_slide_puzzle_initialize:

    python:
        if minigame_slide_puzzle_difficulty == "hard":
            minigame_slide_puzzle_rows = 4
            minigame_slide_puzzle_columns = 4
        else:
            minigame_slide_puzzle_rows = 3
            minigame_slide_puzzle_columns = 3

        if minigame_slide_puzzle_difficulty == "easy":
            minigame_slide_puzzle_time_limit = False
        else:
            minigame_slide_puzzle_time_limit = True

        if minigame_slide_puzzle_difficulty == "medium":
            minigame_countdown_duration = 300
        elif minigame_slide_puzzle_difficulty == "hard":
            minigame_countdown_duration = 600

        minigame_slide_puzzle_gap_row = minigame_slide_puzzle_rows - 1
        minigame_slide_puzzle_gap_column = minigame_slide_puzzle_columns - 1
        minigame_slide_puzzle_layout = []
        minigame_slide_puzzle_layout_slot_index = 0
        minigame_slide_puzzle_layout_width = 1280
        minigame_slide_puzzle_layout_height = 720
        minigame_slide_puzzle_piece_width = int( minigame_slide_puzzle_layout_width / float( minigame_slide_puzzle_rows ) )
        minigame_slide_puzzle_piece_height = int( minigame_slide_puzzle_layout_height / float( minigame_slide_puzzle_columns ) )
        minigame_slide_puzzle_base_displayable_full_path = minigame_slide_puzzle_random_picture()
        minigame_slide_puzzle_check_for_win = False
        minigame_slide_puzzle_disable_puzzle_interaction = False
        minigame_slide_puzzle_scrambled_at_least_once = False
        minigame_slide_puzzle_times_to_scramble = 80

        if config.developer and 1 == 2:
            
            
            minigame_slide_puzzle_times_to_scramble = 1

        minigame_slide_puzzle_base_displayable = Transform(Image(minigame_slide_puzzle_base_displayable_full_path), size = (minigame_slide_puzzle_layout_width, minigame_slide_puzzle_layout_height ))

        for row_i in range(0, minigame_slide_puzzle_rows):
            minigame_slide_puzzle_layout.append([])
            for col_i in range(0, minigame_slide_puzzle_columns):
                if minigame_slide_puzzle_gap_row != row_i or minigame_slide_puzzle_gap_column != col_i:
                    minigame_slide_puzzle_layout[row_i].append(Slide_Puzzle_Piece(minigame_slide_puzzle_base_displayable, minigame_slide_puzzle_layout_slot_index, row = row_i, column = col_i ))
                else:
                    minigame_slide_puzzle_layout[row_i].append(None)
                minigame_slide_puzzle_layout_slot_index += 1

        while not minigame_slide_puzzle_scrambled_at_least_once or minigame_slide_puzzle_test_win():
            minigame_slide_puzzle_scrambled_at_least_once = True
            
            for i in range(0, minigame_slide_puzzle_times_to_scramble):
                candidates =  []
                
                old_row = minigame_slide_puzzle_gap_row
                old_col = minigame_slide_puzzle_gap_column
                
                
                if old_row != 0:
                    candidates.append( (old_row - 1, old_col) )
                
                
                if old_row != store.minigame_slide_puzzle_rows - 1:
                    candidates.append( (old_row + 1, old_col) )
                
                
                if old_col != 0:
                    candidates.append( (old_row, old_col - 1) )
                
                
                if old_col != store.minigame_slide_puzzle_columns - 1:
                    candidates.append( (old_row, old_col + 1) )
                
                
                candidate = random.choice(candidates)
                new_row = candidate[0]
                new_col = candidate[1]
                
                puzzle_piece_to_swap = minigame_slide_puzzle_layout[new_row][new_col]
                minigame_slide_puzzle_perform_swap(new_row, new_col, old_row, old_col, puzzle_piece_to_swap)
                minigame_slide_puzzle_gap_row = new_row
                minigame_slide_puzzle_gap_column = new_col

        minigame_slide_puzzle_check_for_win = True



    return

label minigame_slide_puzzle_begin:
    $ quick_menu = False
    call bust_art_background ("bg black")
    pause 0.5

    show screen slide_puzzle_screen
    with Dissolve(0.75)
    $ quick_menu = True

    if minigame_slide_puzzle_time_limit:
        call minigame_countdown (minigame_countdown_duration, "minigame_slide_puzzle_too_slow")

    call screen hard_block_screen

    return

label minigame_slide_puzzle_intro(partner=None):
    $ no_bust_art = False

    if config.developer and 1 == 2:
        "DEBUG/DEVELOPER MODE: Reduced difficulty."

    if partner:
        $ minigame_slide_puzzle_partner = partner
    else:
        $ minigame_slide_puzzle_partner = si

    if minigame_slide_puzzle_partner == si:
        $ diceroll = random.randint(1,3)

        if diceroll == 1:
            $ display_multiple_characters([ (n, ""), (si, "pose handsup") ], reset = True)
            call process_character (si, appearance="pose handsup", text="Я только что закончила.")
            call process_character (si, appearance="pose handsup", text="Ты должен попробовать.")
        elif diceroll == 2:
            $ display_multiple_characters([ (n, ""), (si, "pose armunder face happy") ], reset = True)
            call process_character (si, appearance="pose armunder face happy", text="Я не знаю, как некоторые люди думают так быстро!")
        else:
            $ display_multiple_characters([ (n, ""), (si, "pose handsfront face neutral") ], reset = True)
            call process_character (si, appearance="pose handsfront face neutral", text="Твой молодой мозг справится с этим.")
            call process_character (si, appearance="pose handsfront face happy", text="В отличие от твоей мамы!")
    elif minigame_slide_puzzle_partner == sa:
        if not minigame_sliding_puzzle_sam_intro_done:
            $ minigame_sliding_puzzle_sam_intro_done = True
            $ display_multiple_characters([ (n, ""), (sa, "pose handsbehind face neutral") ], reset = True)

            if "minigame_slide_puzzle_first_time_intro" in si.conversations_completed:
                call process_character (sa, appearance="pose handsbehind face neutral", text="Я слышал, мама пробует решать эти новые головоломки?")
                call process_character (n, appearance="pose handpocket face neutral", text="Да.")
                call process_character (n, appearance="pose handpocket face neutral", text="Она сказала, что это хорошо для памяти.")
            else:
                call process_character (sa, appearance="pose handsbehind face neutral", text="Мама рассказала мне о головоломках, которые она решала.")
                call process_character (n, appearance="pose handpocket face neutral", text="Да ну?")
                call process_character (n, appearance="pose handpocket face neutral", text="И какие?")
                call process_character (sa, appearance="pose handface face neutral", text="Я думаю они называются \"передвижные\" головоломки?")
                call process_character (sa, appearance="pose handface face neutral", text="Мама говорит, что они улучшают память.")
                call process_character (n, appearance="pose handpocket face neutral", text="Интересно...")

            call process_character (sa, appearance="pose leaning face neutral", text="Я думаю, мы должны попробовать некоторые!")
            call process_character (sa, appearance="pose handface face curious", text="Математика все время поджаривает мой мозг...")
            call process_character (n, appearance="pose handfist face neutral", text="Конечно!")
            call process_character (n, appearance="pose handfist face neutral", text="Я за головоломки!")
            call process_character (sa, appearance="pose leaning face happy", text="Хорошо!")
            call process_character (sa, appearance="pose leaning face happy", text="Давай я научу тебя!")

            call character_leave_dissolve (sa)
            $ renpy.pause(1)

            call process_character (sa, appearance="pose handsbehind face neutral", text="Похоже, что есть различные уровни сложности для них!")
            call process_character (sa, appearance="pose handface face neutral", text="Интересно, с какого уровня мы лучше начать...")
        else:

            $ diceroll = random.randint(1,3)
            if diceroll == 1:
                $ display_multiple_characters([ (n, ""), (sa, "pose handface face neutral") ], reset = True)
                call process_character (sa, appearance="pose handface face neutral", text="Это лучше, чем математика наверняка!")
            elif diceroll == 2:
                $ display_multiple_characters([ (n, ""), (sa, "pose leaning face neutral") ], reset = True)
                call process_character (sa, appearance="pose leaning face neutral", text="Эти головоломки должны быть в видеоигре!")
            else:
                $ display_multiple_characters([ (n, ""), (sa, "pose handsbehind face neutral") ], reset = True)
                call process_character (sa, appearance="pose handsbehind face neutral", text="Интересно, какую головоломку нам стоит попробовать на этот раз?")



    window hide
    menu:
        "Лёгкая":
            $ minigame_slide_puzzle_difficulty = "easy"
        "Средняя (Увеличение Смелости!)":
            $ minigame_slide_puzzle_difficulty = "medium"
        "Тяжёлая (Увеличение Смелости!)":
            $ minigame_slide_puzzle_difficulty = "hard"

    if minigame_slide_puzzle_partner == si:
        if minigame_slide_puzzle_difficulty == "easy":
            call process_character (si, appearance="pose handsfront face neutral", text="Эти головоломки расслабляют.")
        elif minigame_slide_puzzle_difficulty == "medium":
            call process_character (si, appearance="pose handsup face neutral", text="Просто подумай, и ты все решишь.")
        else:
            call process_character (si, appearance="pose armunder face neutral", text="Я бы не торопилась с этим, милый!")
    elif minigame_slide_puzzle_partner == sa:
        if minigame_slide_puzzle_difficulty == "easy":
            call process_character (sa, appearance="pose handsbehind face neutral", text="Давай расслабимся на этот раз!")
        elif minigame_slide_puzzle_difficulty == "medium":
            call process_character (sa, appearance="pose handsbehind face neutral", text="В этом определенно есть стратегия!")
            call process_character (sa, appearance="pose handsbehind face neutral", text="У меня почти получилось!")
        else:
            call process_character (sa, appearance="pose handface face curious", text="Я сосредоточу свои мозги на этом!")


    $ disable_saving()
    $ disable_rollback()
    window hide
    $ clear_characters()

    return

label minigame_slide_puzzle_first_time_intro:
    call process_conversation_beginning ([ (n, ""), (si, "pose armunder face neutral") ])

    call process_character (si, appearance="pose armunder face neutral", text="Куда я положила эту перчатку для духовки?...")
    call process_character (n, appearance="pose handpocket face neutral", text="Привет, Мам!")
    call process_character (si, appearance="pose armunder face neutral", text="Привет, милый.")
    call process_character (n, appearance="pose behindhead face neutral", text="Что-то потеряла?")
    call process_character (si, appearance="pose handsfront face neutral", text="Я ищу свою перчатку для духовки.")
    call process_character (si, appearance="pose handsfront face neutral", text="Я совсем забыла, куда ее положила.")
    call process_character (n, appearance="pose twohandfist face happy", text="Я найду её!")
    call process_character (si, appearance="pose handsup face happy", text="О! Спасибо тебе [n.say_name]!")
    call process_character (si, appearance="pose handsup face happy", text="Клянусь, я бы с ума сошла, если она была бы у меня на шее!")
    call process_character (n, appearance="pose handpocket face neutral", text="Что ты имеешь в виду, Мама?")
    call process_character (si, appearance="pose armunder face neutral", text="С момента переезда мне столько всего приходится запоминать.")
    call process_character (si, appearance="pose armunder face neutral", text="Последнее, что мне нужно, это начать забывать, что я должна сделать.")
    call process_character (n, appearance="pose handpocket face concerned", text="Как тебе удается все запоминать?")
    call process_character (si, appearance="pose handsup face neutral", text="Нуу...")
    call process_character (si, appearance="pose handsup face neutral", text="Я смотрю на это, как на головоломку.")
    call process_character (n, appearance="pose behindhead face neutral", text="Головоломка?")
    call process_character (si, appearance="pose handsup face happy", text="Я так и знала, что тебе будет любопытно, когда ты услышишь что-то относящееся к \"играм!\"")
    call process_character (si, appearance="pose armunder face neutral", text="Одна из этих это передвижные головоломки.")
    call process_character (si, appearance="pose armunder face neutral", text="Ты беспорядочно разбрасываешь картинки в воображении.")
    call process_character (si, appearance="pose armunder face neutral", text="И должен составить их обратно.")
    call process_character (n, appearance="pose handpocket face curious", text="Хм, интересно...")
    call process_character (si, appearance="pose armunder face neutral", text="Другая игра - \"Повтор\".")
    call process_character (si, appearance="pose armunder face neutral", text="Представляешь мигающий набор цветов...")
    call process_character (si, appearance="pose armunder face neutral", text="А затем повторяешь.")
    call process_character (si, appearance="pose handsfront face neutral", text="Я слышал, они хороши для памяти.")
    call process_character (si, appearance="pose handsfront face neutral", text="Так что я решила дать тебе попробовать.")
    call process_character (si, appearance="pose handsfront face neutral", text="Кроме того, суть очень проста.")
    call process_character (si, appearance="pose handsfront face happy", text="Вот это мне нравится!")
    call process_character (n, appearance="pose twohandfist face neutral", text="Могу я их попробовать?")
    call process_character (si, appearance="pose handsup face happy", text="Конечно!")
    call process_character (si, appearance="pose handsfront face neutral", text="Я могу предложить передвижные головоломки на несколько уровней сложности.")
    call process_character (si, appearance="pose handsfront face neutral", text="Или можешь потренировать память с головоломками на повтор.")
    call process_character (si, appearance="pose handsfront face happy", text="Некоторые из них являются сложными!")
    call process_character (si, appearance="pose handsup face neutral", text="Но не торопись и подумай, в какую хочешь поиграть!")

    call process_end_of_conversation ("minigame_slide_puzzle_first_time_intro", si, priority=False, considered_scene=True, override_scene_limit=True)

    return

label minigame_slide_puzzle_win:
    $ minigame_slide_puzzle_disable_puzzle_interaction = True
    call hide_minigame_countdown
    pause 1.0
    hide screen slide_puzzle_screen
    hide screen hard_block_screen

    if minigame_slide_puzzle_difficulty == "easy":
        $ minigame_slide_puzzle_win_money = 4

    elif minigame_slide_puzzle_difficulty == "medium":
        $ minigame_slide_puzzle_win_money = 6
    else:
        $ minigame_slide_puzzle_win_money = 8

    $ renpy.pause(0.25)
    if minigame_slide_puzzle_partner == si:
        if minigame_slide_puzzle_difficulty == "easy":
            $ display_multiple_characters([ (n, ""), (si, "pose handsup face happy") ], reset = True)
            $ si.add_points(3, minigame = True)
            call process_character (si, appearance="pose handsup face happy", text="Хорошая работа, [n.say_name]!")

        elif minigame_slide_puzzle_difficulty == "medium":
            $ display_multiple_characters([ (n, ""), (si, "") ], reset = True)
            call add_points_and_boldness (si, 4, 1, minigame=True)
            call process_character (si, appearance="pose handsup face happy", text="У тебя хорошо получается!")
        else:
            $ display_multiple_characters([ (n, ""), (si, "pose handsup face happy") ], reset = True)
            call add_points_and_boldness (si, 5, 1, minigame=True)
            call process_character (si, appearance="pose handsup face happy", text="Отлично, [n.say_name]! Отлично!")
    elif minigame_slide_puzzle_partner == sa:
        if minigame_slide_puzzle_difficulty == "easy":
            $ display_multiple_characters([ (n, ""), (sa, "pose handface face happy") ])
            $ sa.add_points(3, minigame = True)
            call process_character (sa, appearance="pose handface face happy", text="Эй, неплохо!")
        elif minigame_slide_puzzle_difficulty == "medium":
            $ display_multiple_characters([ (n, ""), (sa, "pose handface face happy") ])
            call add_points_and_boldness (sa, 4, 1, minigame=True)
            call process_character (sa, appearance="pose handface face happy", text="О, так вот как это делается!")
            call process_character (sa, appearance="pose handface face happy", text="Мило, [n.say_name]!")
        else:
            $ display_multiple_characters([ (n, ""), (sa, "pose handface face happy") ])
            call add_points_and_boldness (sa, 5, 1, minigame=True)
            call process_character (sa, appearance="pose handface face happy", text="Уоу!")
            call process_character (sa, appearance="pose handface face happy", text="Я даже не видела такого решения!")
            call process_character (sa, appearance="pose handface face happy", text="Ты мастер головоломок, [n.say_name]!")


    show screen hud
    python hide:
        inventory.add_money(minigame_slide_puzzle_win_money, minigame = True)
        narrator("Получите $" + str(minigame_slide_puzzle_win_money) + " за победу.")

    call minigame_slide_puzzle_end

    return

label minigame_slide_puzzle_too_slow:
    $ minigame_slide_puzzle_disable_puzzle_interaction = True
    call hide_minigame_countdown
    pause 1.0
    hide screen slide_puzzle_screen
    hide screen hard_block_screen

    if minigame_slide_puzzle_partner == si:
        if minigame_slide_puzzle_difficulty == "easy":
            $ display_multiple_characters([ (n, "face curious"), (si, "pose handsup face curious") ])
            call process_character (si, appearance="pose handsup face curious", text="Я надеюсь, что эти видеоигры не делают тебя жестче.")
        else:
            $ display_multiple_characters([ (n, "face curious"), (si, "pose handsfront face neutral") ])
            call process_character (si, appearance="pose handsfront face neutral", text="Ты привыкнешь.")
    elif minigame_slide_puzzle_partner == sa:
        if minigame_slide_puzzle_difficulty == "easy":
            $ display_multiple_characters([ (n, "face curious"), (sa, "pose handface face curious") ])
            call process_character (sa, appearance="pose handface face curious", text="Похоже, память не слишком хороша, да?")
        else:
            $ display_multiple_characters([ (n, "face curious"), (sa, "pose handface face curious") ])
            call process_character (sa, appearance="pose handface face curious", text="Ой, почти!")

    call minigame_slide_puzzle_end

    return

label minigame_slide_puzzle_end:
    $ renpy.scene('screens')
    $ minigame_slide_puzzle_layout = None
    $ minigame_slide_puzzle_base_displayable = None

    $ enable_saving()
    $ renpy.block_rollback()
    $ enable_rollback()

    call process_end_of_minigame ("minigame_slide_puzzle")

    return