init python:
    import pygame

    class MinigameGaugeDisplayable(renpy.Displayable):
        
        def __init__(self, difficulty = "easy", lose_label = None):
            
            renpy.Displayable.__init__(self)
            
            self.difficulty = difficulty
            self.lose_label = lose_label
            
            
            self.vertical_bar_background = Image("vertical_bar_background.png")
            self.tension_bar_background = Image("tension_bar_background.png")
            self.dial = Image("dial.png")
            self.sweet_spot = Image("sweet_spot.png")
            self.tension = Image("tension.png")
            self.tension_text = Text("Времени осталось", size = 60)
            
            
            vertical_bar_dummy_render = renpy.render( self.vertical_bar_background, 1920, 1080, 0, 0)
            self.VERTICAL_BAR_BACKGROUND_WIDTH = int(vertical_bar_dummy_render.width)
            self.VERTICAL_BAR_BACKGROUND_HEIGHT = int(vertical_bar_dummy_render.height)
            
            tension_bar_dummy_render = renpy.render( self.tension_bar_background, 1920, 1080, 0, 0)
            self.TENSION_BAR_BACKGROUND_WIDTH = int(tension_bar_dummy_render.width)
            self.TENSION_BAR_BACKGROUND_HEIGHT = int(tension_bar_dummy_render.height)
            
            dial_dummy_render = renpy.render( self.dial, 1920, 1080, 0, 0)
            self.DIAL_WIDTH = dial_dummy_render.width
            self.DIAL_HEIGHT = dial_dummy_render.height
            
            self.GAUGE_AREA_Y_PADDING = 10
            self.GAUGE_AREA_HEIGHT = self.VERTICAL_BAR_BACKGROUND_HEIGHT - self.GAUGE_AREA_Y_PADDING
            
            self.SWEET_SPOT_LEFT_BORDER = 0
            self.SWEET_SPOT_RIGHT_BORDER = 0
            self.SWEET_SPOT_TOP_BORDER = 10
            self.SWEET_SPOT_BOTTOM_BORDER = 10
            
            self.SWEET_SPOT_WIDTH = self.VERTICAL_BAR_BACKGROUND_WIDTH
            self.sweet_spot_height = 250
            
            self.TENSION_LEFT_BORDER = 0
            self.TENSION_RIGHT_BORDER = 0
            self.TENSION_TOP_BORDER = 0
            self.TENSION_BOTTOM_BORDER = 0
            
            self.TENSION_WIDTH = self.TENSION_BAR_BACKGROUND_WIDTH
            self.tension_height = 2
            
            tension_text_dummy_render = renpy.render( self.tension_text, 1920, 1080, 0, 0)
            self.TENSION_TEXT_WIDTH = int(tension_text_dummy_render.width)
            self.TENSION_TEXT_HEIGHT = int(tension_text_dummy_render.height)
            
            
            self.sweet_spot_frame = Frame(self.sweet_spot, 
                left = self.SWEET_SPOT_LEFT_BORDER, 
                right = self.SWEET_SPOT_RIGHT_BORDER,
                bottom = self.SWEET_SPOT_BOTTOM_BORDER,
                top = self.SWEET_SPOT_TOP_BORDER)
            
            
            self.tension_frame = Frame(self.tension, 
                left = self.TENSION_LEFT_BORDER, 
                right = self.TENSION_RIGHT_BORDER,
                bottom = self.TENSION_BOTTOM_BORDER,
                top = self.TENSION_TOP_BORDER)
            
            
            self.VERTICAL_BAR_BACKGROUND_X = 640
            self.VERTICAL_BAR_BACKGROUND_Y = 10
            
            self.BAR_X_GAP = 20
            self.TENSION_TEXT_GAP = 10
            
            self.DIAL_X = self.VERTICAL_BAR_BACKGROUND_X
            self.dial_y = self.VERTICAL_BAR_BACKGROUND_Y
            self.dial_direction = 1.0
            
            self.GAUGE_AREA_Y = self.VERTICAL_BAR_BACKGROUND_Y + self.GAUGE_AREA_Y_PADDING
            
            self.sweet_spot_center = self.get_new_sweet_spot_center()
            self.sweet_spot_y = self.get_new_sweet_spot_y()
            self.SWEET_SPOT_X = self.VERTICAL_BAR_BACKGROUND_X
            
            self.TENSION_X = self.VERTICAL_BAR_BACKGROUND_X + self.VERTICAL_BAR_BACKGROUND_WIDTH + self.TENSION_TEXT_GAP + self.TENSION_TEXT_HEIGHT + self.TENSION_TEXT_GAP + self.BAR_X_GAP
            self.tension_y = self.VERTICAL_BAR_BACKGROUND_Y
            
            self.TENSION_TEXT_X = self.TENSION_X - 50
            self.TENSION_TEXT_Y = self.VERTICAL_BAR_BACKGROUND_Y
            
            
            self.BOUNDARY_TOP = self.VERTICAL_BAR_BACKGROUND_Y
            self.BOUNDARY_BOTTOM = self.VERTICAL_BAR_BACKGROUND_Y + self.VERTICAL_BAR_BACKGROUND_HEIGHT
            
            
            self.HIT_DIAL_SPEED_MULTIPLIER = 1.10
            self.HIT_SWEET_SPOT_MULTIPLIER = 0.80
            
            
            
            self.oldst = None
            self.elapsed_st = 0
            
            
            if self.difficulty == "easy":
                self.dial_speed = 600
                self.DIAL_MAX_SPEED = 800
                self.hits_to_win = 6
                self.minigame_duration = 12
                self.SWEET_SPOT_MINIMUM_HEIGHT = 125
            elif self.difficulty == "medium":
                self.dial_speed = 650
                self.DIAL_MAX_SPEED = 900
                self.hits_to_win = 7
                self.minigame_duration = 12
                self.SWEET_SPOT_MINIMUM_HEIGHT = 100
            else:
                self.dial_speed = 700
                self.DIAL_MAX_SPEED = 950
                self.hits_to_win = 8
                self.minigame_duration = 15
                self.SWEET_SPOT_MINIMUM_HEIGHT = 90
            
            if store.inventory.has_item(11):
                self.SWEET_SPOT_MINIMUM_HEIGHT += 50
                self.hits_to_win -= 1
                self.dial_speed -= 50
                self.DIAL_MAX_SPEED -= 100
                self.minigame_duration += 5
            
            
            
            self.times_hit = 0
            self.lost = False
            
            
            self.last_press_was_hit = None
        
        def visit(self):
            return [ self.vertical_bar_background, self.dial ]
        
        def get_new_tension_y(self):
            y = self.TENSION_BAR_BACKGROUND_Y + self.TENSION_BAR_BACKGROUND_HEIGHT - self.tension_height
            return y
        
        def get_new_sweet_spot_center(self):
            sweet_spot_half_height = int(self.sweet_spot_height/2)
            center = self.GAUGE_AREA_Y + random.randint( self.GAUGE_AREA_Y + sweet_spot_half_height, ( self.GAUGE_AREA_Y + self.GAUGE_AREA_HEIGHT) - sweet_spot_half_height )
            return center
        
        def get_new_sweet_spot_y(self):
            y = self.sweet_spot_center - int(self.sweet_spot_height/2)
            return y
        
        
        def render(self, width, height, st, at):
            
            
            r = renpy.Render(width, height)
            
            
            if self.oldst is None:
                self.oldst = st
            
            dtime = st - self.oldst
            self.oldst = st
            
            
            dial_speed = dtime * self.dial_speed
            old_dial_y = self.dial_y
            
            if old_dial_y + self.DIAL_HEIGHT >= self.BOUNDARY_BOTTOM:
                
                self.dial_direction= -1.0
            elif old_dial_y <= self.BOUNDARY_TOP:
                
                self.dial_direction = 1.0
            
            self.dial_y += dial_speed * self.dial_direction
            
            
            self.tension_height = int( self.VERTICAL_BAR_BACKGROUND_HEIGHT * ( ( self.minigame_duration - self.elapsed_st ) / self.minigame_duration  ) )
            
            vertical_bar_background_render = renpy.render( self.vertical_bar_background, 1920, 1080, st, at )
            r.blit(vertical_bar_background_render, ( self.VERTICAL_BAR_BACKGROUND_X, self.VERTICAL_BAR_BACKGROUND_Y ) )
            
            sweet_spot_fixed = Fixed(self.sweet_spot_frame, xysize = ( self.SWEET_SPOT_WIDTH, self.sweet_spot_height ) )
            sweet_spot_fixed_render = renpy.render( sweet_spot_fixed, 1920, 1080, st, at )
            r.blit(sweet_spot_fixed_render, ( self.SWEET_SPOT_X, self.sweet_spot_y ) )
            
            tension_transform = Transform(self.tension_frame, yalign = 1.0, size = ( self.TENSION_WIDTH, self.tension_height ) )
            tension_fixed = Fixed(tension_transform, xysize = ( self.TENSION_WIDTH, self.VERTICAL_BAR_BACKGROUND_HEIGHT ) )
            tension_fixed_render = renpy.render( tension_fixed, 1920, 1080, st, at )
            r.blit(tension_fixed_render, ( self.TENSION_X, self.tension_y ) )
            
            dial_render = renpy.render( self.dial, 1920, 1080, st, at )
            r.blit(dial_render, ( self.DIAL_X, self.dial_y ) )
            
            tension_text_transform = Transform(self.tension_text, rotate = -90, yalign = 0.5)
            tension_text_fixed = Fixed(tension_text_transform, xysize = ( 500, self.VERTICAL_BAR_BACKGROUND_HEIGHT) )
            tension_text_render = renpy.render( tension_text_fixed, 1920, 1080, st, at )
            r.blit(tension_text_render , ( self.TENSION_TEXT_X, self.TENSION_TEXT_Y ) )
            
            hit_space_text = Text( "Нажмите Пробел В Отмеченной Области " + str(self.hits_to_win) + " Раз для Победы!", xalign = 0.5, yalign = 0.7, size = 60 )
            hit_space_text_fixed = Fixed( hit_space_text, xysize = ( 1920, 1080 ) )
            hit_space_text_fixed_render = renpy.render( hit_space_text_fixed, 1920, 1080, st, at )
            r.blit(hit_space_text_fixed_render, ( 0, 0 ) )
            
            hit_space_text = Text( "Промахи уменьшают счёт!", xalign = 0.5, yalign = 0.8, size = 60 )
            hit_space_text_fixed = Fixed( hit_space_text, xysize = ( 1920, 1080 ) )
            hit_space_text_fixed_render = renpy.render( hit_space_text_fixed, 1920, 1080, st, at )
            r.blit(hit_space_text_fixed_render, ( 0, 0 ) )
            
            hit_space_text = Text( str(self.times_hit) + "/" + str(self.hits_to_win) + " Hits", xalign = 0.5, yalign = 0.9, size = 60 )
            hit_space_text_fixed = Fixed( hit_space_text, xysize = ( 1920, 1080 ) )
            hit_space_text_fixed_render = renpy.render( hit_space_text_fixed, 1920, 1080, st, at )
            r.blit(hit_space_text_fixed_render, ( 0, 0 ) )
            
            
            self.elapsed_st = self.elapsed_st + dtime
            if self.elapsed_st >= self.minigame_duration:
                renpy.call(self.lose_label)
                renpy.return_statement()
            
            
            
            renpy.redraw(self, 0)
            
            
            return r
        
        def hit_sweet_spot(self, ev, x, y, st):
            hit = False
            
            if self.hit_space(ev):
                if self.dial_on_sweet_spot():
                    hit = True
                    self.last_press_was_hit = True
                else:
                    self.last_press_was_hit = False
            
            return hit
        
        def dial_on_sweet_spot(self):
            touching = False
            
            if self.dial_y + self.DIAL_HEIGHT >= self.sweet_spot_y and self.dial_y < self.sweet_spot_y + self.sweet_spot_height:
                touching = True
            
            return touching
        
        def hit_space(self, ev):
            hit_space = False
            
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                hit_space = True
            
            return hit_space
        
        
        def event(self, ev, x, y, st):
            if self.hit_space(ev):
                if self.dial_on_sweet_spot():
                    self.times_hit += 1
                    self.dial_speed = min(self.dial_speed * self.HIT_DIAL_SPEED_MULTIPLIER, self.DIAL_MAX_SPEED )
                    self.sweet_spot_height = max( self.SWEET_SPOT_MINIMUM_HEIGHT, int(self.sweet_spot_height * self.HIT_SWEET_SPOT_MULTIPLIER) )
                    self.sweet_spot_y = self.get_new_sweet_spot_y()
                else:
                    self.times_hit -= 1
            
            if self.times_hit >= self.hits_to_win:
                return True
            
            raise renpy.IgnoreEvent()

label minigame_reading(partner=None):
    $ renpy.scene('screens')
    $ diceroll = random.randint(1,3)

    if diceroll == 1:
        $ display_multiple_characters([ (n, ""), (julia, "pose handface face neutral blush false") ], reset = True)
        call process_character (julia, appearance="pose handface face neutral blush false", text="Мне нравится это новая книга.")
        call process_character (julia, appearance="pose handface face neutral blush false", text="Может, и тебе тоже понравится.")
    elif diceroll == 2:
        $ display_multiple_characters([ (n, ""), (julia, "pose handup face happy blush false") ], reset = True)
        call process_character (julia, appearance="pose handup face happy blush false", text="Словарь пригодится для этих книг, [n.say_name].")
    else:
        $ display_multiple_characters([ (n, ""), (julia, "pose handup face happy blush false") ], reset = True)
        call process_character (julia, appearance="pose handup face happy blush false", text="Я только выберу лучшие страницы из книги")

    $ diceroll = random.randint(1,2)
    menu:
        "Лёгкая":
            $ minigame_reading_difficulty = "easy"
            if diceroll == 1:
                call process_character (julia, appearance="pose handface face neutral blush false", text="Полегче, да?")
                call process_character (julia, appearance="pose handface face neutral blush false", text="Я не виню тебя.")
            else:
                call process_character (julia, appearance="pose handface face happy blush false", text="Я просмотрела эту книгу за один день.")
        "Средняя (Увеличение Смелости!)":
            $ minigame_reading_difficulty = "medium"
            if diceroll == 1:
                call process_character (julia, appearance="pose handup face neutral blush false", text="Не плохой выбор.")
            else:
                call process_character (julia, appearance="pose handup face neutral blush false", text="Это добротный рассказ.")
        "Тяжёлая (Увеличение Смелости!)":
            $ minigame_reading_difficulty = "hard"
            if diceroll == 1:
                call process_character (julia, appearance="pose armcross face neutral blush false", text="Удачи тебе.")
                call process_character (julia, appearance="pose armcross face neutral blush false", text="Здесь пять различных сюжетных линий.")
            else:
                call process_character (julia, appearance="pose armcross face neutral blush false", text="Ты уверен, что хочешь это прочитать?")
                call process_character (julia, appearance="pose armcross face neutral blush false", text="Снимаю шляпу перед тобой, если ты запомнишь всё!")


    $ disable_saving()
    $ disable_rollback()
    window hide
    $ clear_characters()
    window hide

    python:
        ui.add(MinigameGaugeDisplayable(difficulty = minigame_reading_difficulty, lose_label = "minigame_reading_lost"))
        won = ui.interact(suppress_overlay=True, suppress_underlay=True)

    call minigame_reading_won



    return

label minigame_reading_won:
    $ diceroll = random.randint(1,4)

    pause 1.0

    $ display_multiple_characters([ (n, "pose handfist face happy blush false"), (julia, "") ], reset = True)

    $ minigame_reading_money = 0

    if minigame_reading_difficulty == "easy":
        call process_character (julia, appearance="pose handup face happy blush false", text="Похоже, ты понимаешь прочитанное.")
        $ julia.add_points(2, minigame = True)
        $ minigame_reading_money = 4
    elif minigame_reading_difficulty == "medium":
        call process_character (julia, appearance="pose armcross face happy blush false", text="Я уже слышу новые слова от тебя!")
        call add_points_and_boldness (julia, 3, 1, minigame=True)
        $ minigame_reading_money = 6
    else:
        call process_character (julia, appearance="pose handup face happy blush false", text="Я думаю, ты поумнел после прочтения этой книги!")

        call add_points_and_boldness (julia, 4, 1, minigame=True)
        $ minigame_reading_money = 8

    show screen hud
    python hide:
        inventory.add_money(minigame_reading_money, minigame = True)
        narrator("Получите $" + str(minigame_reading_money) + " за победу.")


    call minigame_reading_end
    return

label minigame_reading_lost:

    $ diceroll = random.randint(1,4)

    pause 1.0
    $ display_multiple_characters([ (n, "pose behindhead face curious blush false"), (julia, "") ], reset = True)
    pause 0.5

    if minigame_reading_difficulty == "easy":
        call process_character (julia, appearance="pose handface face concerned blush false", text="Уоу, [n.say_name]...")
        call process_character (julia, appearance="pose handface face concerned blush false", text="Думаю, тебе понадобится репетитор.")
    else:
        call process_character (julia, appearance="pose armcross face neutral blush false", text="На твоём месте, я бы прочитал второй раз.")


    call minigame_reading_end

    return

label minigame_reading_end:
    $ enable_saving()
    $ renpy.block_rollback()
    $ enable_rollback()

    call process_end_of_minigame ("minigame_repeat_pattern")

    return