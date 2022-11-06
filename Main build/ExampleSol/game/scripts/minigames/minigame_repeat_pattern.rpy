init python:
    def minigame_repeat_pattern_choose_and_flash_a_button():
        keys = minigame_repeat_pattern_buttons.keys()
        chosen_color = random.choice(keys)
        minigame_repeat_pattern_flash_button(chosen_color)
        minigame_repeat_pattern_puzzle_button_order.append(chosen_color)
        
        
        if len(store.minigame_repeat_pattern_puzzle_button_order) >= store.minigame_repeat_pattern_number_of_buttons_to_match - 1:
            renpy.call("minigame_repeat_pattern_interaction_phase_preparation")
        
        return

    def minigame_repeat_pattern_flash_button(color):
        button = store.minigame_repeat_pattern_buttons[color]
        button.last_transform_st = button.current_st
        button.allow_transform = True
        return

    class Repeat_Pattern_Button(renpy.display.behavior.ImageButton):
        def __init__(self, color = None, flash_color = None, key = None, **kwargs):
            self.width = store.minigame_repeat_pattern_button_width
            self.height = store.minigame_repeat_pattern_button_height
            self.color = color
            self.key = key
            self.flash_color = flash_color
            
            self.border_color = "#a223cc"
            
            idle_image = Null( width = self.width, height = self.height )
            
            self.current_st = 0
            self.last_transform_st = 0
            self.allow_transform = False
            
            
            
            super(Repeat_Pattern_Button, self).__init__(idle_image = idle_image, clicked = self.click_function, **kwargs)
        
        def click_function(self):
            if store.minigame_repeat_pattern_disable_button_interaction:
                if renpy.get_screen("say") or store.minigame_repeat_pattern_correctness_phase:
                    return None
                return
            
            minigame_repeat_pattern_flash_button(self.key)
            
            player_order = store.minigame_repeat_pattern_player_button_order
            index_to_check = len(player_order)
            
            correct_color =  minigame_repeat_pattern_puzzle_button_order[index_to_check]
            
            
            if correct_color != self.key:
                renpy.call("minigame_repeat_pattern_wrong_button")
            else:
                player_order.append(self.color)
                store.minigame_repeat_pattern_display_button_correctness_text = "Правильно! " + str(len(player_order)) + "/" + str(minigame_repeat_pattern_number_of_buttons_to_match)
                
                
                if len(player_order) >= minigame_repeat_pattern_number_of_buttons_to_match:
                    renpy.call("minigame_repeat_pattern_got_all_right")
            
            return
        
        def render(self, width, height, st, at):
            self.current_st = st
            new_transform_st = st - self.last_transform_st
            
            render = super(Repeat_Pattern_Button, self).render(width, height, st, at)
            
            solid = Solid(self.color, xsize = self.width, ysize = self.height)
            
            if self.allow_transform:
                solid = At(solid, repeat_pattern_transform)
            
            render.blit( renpy.render(solid, width, height, new_transform_st, at),(0, 0), False ) 
            
            
            
            if self.is_focused() and not store.minigame_repeat_pattern_disable_button_interaction:
                hover_border_size = 10
                
                top_hover_border = Fixed( Solid(self.border_color, xsize = self.width, ysize = hover_border_size, xalign = 0.0, yalign = 0.0), xysize = ( int( render.width ), int( render.height ) ) )
                bottom_hover_border = Fixed( Solid(self.border_color, xsize = self.width, ysize = hover_border_size, xalign = 0.0, yalign = 1.0), xysize = ( int( render.width ), int( render.height ) ) )
                
                left_hover_border = Fixed( Solid(self.border_color, xsize = hover_border_size, ysize = self.height, xalign = 0.0, yalign = 0.0), xysize = ( int( render.width ), int( render.height ) ) )
                right_hover_border = Fixed( Solid(self.border_color, xsize = hover_border_size, ysize = self.height, xalign = 1.0, yalign = 0.0), xysize = ( int( render.width ), int( render.height ) ) )
                
                render.blit( renpy.render(top_hover_border, width, height, st, at), ( 0,  0), False)
                render.blit( renpy.render(bottom_hover_border, width, height, st, at), ( 0,  0), False)
                render.blit( renpy.render(left_hover_border, width, height, st, at), ( 0,  0), False)
                render.blit( renpy.render(right_hover_border, width, height, st, at), ( 0,  0), False)
            
            if store.minigame_repeat_pattern_display_wrong_text_on_buttons:
                wrong_text = Fixed( Text("X", xalign = 0.5, yalign = 0.5, size = 64), xysize = ( int( self.width ), int( self.height ) ) )
                render.blit( renpy.render(wrong_text, width, height, st, at), ( 0,  0), False)
            
            renpy.redraw(self, 0)
            
            return render

transform repeat_pattern_transform:
    linear 0.5 alpha 0.0
    linear 0.5 alpha 1.0

screen repeat_pattern_make_pattern:
    timer 1.0 action Function(minigame_repeat_pattern_choose_and_flash_a_button)
    if len(minigame_repeat_pattern_puzzle_button_order) <= minigame_repeat_pattern_number_of_buttons_to_match - 1:
        timer 1.0 + minigame_repeat_pattern_time_between_flashes action Function(minigame_repeat_pattern_choose_and_flash_a_button) repeat True

screen repeat_pattern_transition_to_interaction_phase:
    timer 2.5 action Jump("minigame_repeat_pattern_interaction_phase_start")

label minigame_repeat_pattern_interaction_phase_preparation:
    call screen repeat_pattern_transition_to_interaction_phase
    return

screen repeat_pattern_screen:
    text minigame_repeat_pattern_instruction_text xalign 0.5 yalign 0.05 size 72

    text "Patterns Solved: " +  str(minigame_repeat_pattern_patterns_solved) + "/" + str(minigame_repeat_pattern_patterns_to_win) xalign 0.95 yalign 0.5 size 72
    vbox:
        xalign 0.5
        yalign 0.4
        spacing 20
        grid 2 2:

            spacing 40
            for minigame_repeat_pattern_button in minigame_repeat_pattern_buttons_array:
                add minigame_repeat_pattern_button

        text minigame_repeat_pattern_display_button_correctness_text xalign 0.5 size 72

    if not minigame_repeat_pattern_disable_button_interaction:
        textbutton "Give Up" action Jump("minigame_repeat_pattern_too_slow") xalign 0.99 yalign 0.99


label minigame_repeat_pattern_wrong_button:
    python:
        minigame_repeat_pattern_instruction_text = ""
        minigame_repeat_pattern_display_button_correctness_text = "Неправильно!"
        minigame_repeat_pattern_display_wrong_text_on_buttons = True
        minigame_repeat_pattern_disable_button_interaction = True
        minigame_repeat_pattern_correctness_phase = True

    pause 2.0
    call minigame_repeat_pattern_interaction_phase

    return

label minigame_repeat_pattern_got_all_right:
    call hide_minigame_countdown
    $ minigame_repeat_pattern_instruction_text = "Правильно!"
    $ minigame_repeat_pattern_patterns_solved += 1
    $ store.minigame_repeat_pattern_disable_button_interaction = True
    $ minigame_repeat_pattern_correctness_phase = True
    pause 1.0

    if minigame_repeat_pattern_patterns_solved >= minigame_repeat_pattern_patterns_to_win:
        $ minigame_repeat_pattern_correctness_phase = False
        $ minigame_repeat_pattern_money = 0
        pause 0.5

        if minigame_repeat_pattern_partner == si:
            if minigame_repeat_pattern_difficulty == "easy":
                $ minigame_repeat_pattern_money = 4
                $ display_multiple_characters([ (n, ""), (si, "pose handsup face happy") ], reset = True)
                $ si.add_points(2, minigame = True)
                call process_character (si, appearance="pose handsup face happy", text="Хорошая работа, [n.say_name]!")
            elif minigame_repeat_pattern_difficulty == "medium":
                $ minigame_repeat_pattern_money = 6
                $ display_multiple_characters([ (n, ""), (si, "") ], reset = True)
                call add_points_and_boldness (si, 3, 1, minigame=True)
                call process_character (si, appearance="pose handsup face happy", text="У тебя хорошо получается!")
            else:
                $ minigame_repeat_pattern_money = 8
                $ display_multiple_characters([ (n, ""), (si, "pose handsup face happy") ], reset = True)
                call add_points_and_boldness (si, 4, 1, minigame=True)
                call process_character (si, appearance="pose handsup face happy", text="Отлично, [n.say_name]! Просто отлично!")

        show screen hud
        python hide:
            inventory.add_money(minigame_repeat_pattern_money, minigame = True)
            narrator("Получите $" + str(minigame_repeat_pattern_money) + " за победу.")

        call minigame_repeat_pattern_end
    else:
        pause 2.0
        call minigame_repeat_round

    return

label minigame_repeat_pattern_too_slow:
    call hide_minigame_countdown
    $ minigame_repeat_pattern_correctness_phase = False
    $ store.minigame_repeat_pattern_disable_button_interaction = True
    pause 0.5

    if minigame_repeat_pattern_partner == si:
        if minigame_repeat_pattern_difficulty == "easy":
            $ display_multiple_characters([ (n, "face curious"), (si, "pose handsup face curious") ])
            call process_character (si, appearance="pose handsup face curious", text="Я надеюсь, что эти видеоигры не делают тебя жестче.")
        else:
            $ display_multiple_characters([ (n, "face curious"), (si, "pose handsfront face neutral") ])
            call process_character (si, appearance="pose handsfront face neutral", text="Ты привыкнешь.")

    call minigame_repeat_pattern_end

    return

label minigame_repeat_pattern_end:
    call hide_minigame_countdown
    $ minigame_repeat_pattern_instruction_text = ""
    $ store.minigame_repeat_pattern_disable_button_interaction = True
    $ renpy.scene('screens')

    $ enable_saving()
    $ renpy.block_rollback()
    $ enable_rollback()

    call process_end_of_minigame ("minigame_repeat_pattern")

    return

label minigame_repeat_pattern_interaction_phase_start:
    $ minigame_repeat_pattern_correctness_phase = False
    $ minigame_repeat_pattern_disable_button_interaction = True
    hide screen repeat_pattern_transition_to_interaction_phase
    if minigame_repeat_pattern_difficulty != "easy":
        call minigame_countdown (minigame_countdown_duration, "minigame_repeat_pattern_too_slow")

    call minigame_repeat_pattern_interaction_phase

    return

label minigame_repeat_pattern_interaction_phase:
    python:
        minigame_repeat_pattern_display_button_correctness_text = ""
        minigame_repeat_pattern_display_wrong_text_on_buttons = False
        minigame_repeat_pattern_player_button_order = []

        minigame_repeat_pattern_instruction_text = "Повтор"
        minigame_repeat_pattern_disable_button_interaction = False

    call screen hard_block_screen

    return

label minigame_repeat_round:
    hide screen repeat_pattern_make_pattern
    python:
        minigame_repeat_pattern_correctness_phase = False
        minigame_repeat_pattern_disable_button_interaction = True
        minigame_repeat_pattern_puzzle_button_order = []
        minigame_repeat_pattern_player_button_order = []
        minigame_repeat_pattern_instruction_text = "Повторить"
        minigame_repeat_pattern_display_button_correctness_text = ""

    show screen repeat_pattern_screen
    show screen repeat_pattern_make_pattern
    with Dissolve(0.75)
    $ quick_menu = True
    call screen hard_block_screen

    return

label minigame_repeat_pattern(partner=None):
    $ renpy.scene('screens')
    $ no_bust_art = False

    if partner:
        $ minigame_repeat_pattern_partner = partner
    else:
        $ minigame_repeat_pattern_partner = si

    if minigame_repeat_pattern_partner == si:
        $ diceroll = random.randint(1,2)

        if diceroll == 1:
            $ display_multiple_characters([ (n, ""), (si, "pose handsup") ], reset = True)
            call process_character (si, appearance="pose handsup", text="Я только что закончила.")
            call process_character (si, appearance="pose handsup", text="Тебе стоит самому попробовать.")
        elif diceroll == 2:
            $ display_multiple_characters([ (n, ""), (si, "pose handsfront face neutral") ], reset = True)
            call process_character (si, appearance="pose handsfront face neutral", text="Твой молодой мозг справится с этим.")
            call process_character (si, appearance="pose handsfront face happy", text="В отличие от твоей мамы!")


    menu:
        "Легкая":
            $ minigame_repeat_pattern_difficulty = "easy"
            $ minigame_repeat_pattern_number_of_buttons_to_match = 4
        "Средняя (Увеличение Смелости!)":
            $ minigame_repeat_pattern_difficulty = "medium"
            $ minigame_countdown_duration = 45
            $ minigame_repeat_pattern_number_of_buttons_to_match = 5
        "Тяжёлая (Увеличение Смелости!)":
            $ minigame_repeat_pattern_difficulty = "hard"
            $ minigame_countdown_duration = 60
            $ minigame_repeat_pattern_number_of_buttons_to_match = 6

    if minigame_repeat_pattern_partner == si:
        if minigame_repeat_pattern_difficulty == "easy":
            call process_character (si, appearance="pose handsfront face neutral", text="Эти головоломки расслабляют.")
        elif minigame_repeat_pattern_difficulty == "medium":
            call process_character (si, appearance="pose handsup face neutral", text="Просто подумай, и ты все решишь.")
        else:
            call process_character (si, appearance="pose armunder face neutral", text="Я бы не торопилась с этим, милый!")

    $ disable_saving()
    $ disable_rollback()
    window hide
    $ clear_characters()

    python:
        minigame_repeat_pattern_time_between_flashes = 1.5
        minigame_repeat_pattern_patterns_to_win = 3
        minigame_repeat_pattern_buttons = {}
        minigame_repeat_pattern_button_width = 240
        minigame_repeat_pattern_button_height = 240
        minigame_repeat_pattern_instruction_text = "Повторить"
        minigame_repeat_pattern_display_wrong_text_on_buttons = False
        minigame_repeat_pattern_patterns_solved = 0
        minigame_repeat_pattern_correctness_phase = False

        minigame_repeat_pattern_buttons_array = []
        minigame_repeat_pattern_buttons_array.append(Repeat_Pattern_Button(color = "#e10000", flash_color = "#ff6464", key = "red"))
        minigame_repeat_pattern_buttons_array.append(Repeat_Pattern_Button(color = "#0000e1", flash_color = "#6464FF", key = "blue"))
        minigame_repeat_pattern_buttons_array.append(Repeat_Pattern_Button(color = "#00e100", flash_color = "#64FF64", key = "green"))
        minigame_repeat_pattern_buttons_array.append(Repeat_Pattern_Button(color = "#e1e100", flash_color = "#FFFF96", key = "yellow"))

        minigame_repeat_pattern_disable_button_interaction = True

    python hide:
        for button in store.minigame_repeat_pattern_buttons_array:
            store.minigame_repeat_pattern_buttons[button.key] = button

    if config.developer:
        "DEVELOPER MODE: Only one pattern"
        $ minigame_repeat_pattern_number_of_buttons_to_match = 1
        $ minigame_repeat_pattern_patterns_to_win = 1

    call minigame_repeat_round

    return