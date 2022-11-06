init python:

    class TableTennis(renpy.Displayable):
        
        def __init__(self):
            
            renpy.Displayable.__init__(self)
            
            
            self.player_icon = Image(store.n.icon_image())
            self.opponent_icon = Image(store.minigame_table_tennis_partner.icon_image())
            self.ICON_WIDTH = 220
            self.ICON_HEIGHT = 220
            
            self.paddle = Image("paddle.png")
            self.ball = Image("ping_ball.png")
            self.ctb = Text(_("Нажмитие, чтобы начать"), size=48, xalign = 0.5, yalign = 0.1)
            
            
            
            self.PADDLE_WIDTH = 8
            
            self.PADDLE_HEIGHT = 160
            
            self.BALL_WIDTH = 15
            
            self.BALL_HEIGHT = 23
            self.COURT_LEFT = 447
            self.COURT_TOP = 214
            self.COURT_BOTTOM = config.screen_height - self.COURT_TOP
            self.PLAYER_ICON_X = self.COURT_LEFT - self.ICON_WIDTH - 50
            self.OPPONENT_ICON_X = config.screen_width - self.COURT_LEFT + 50
            
            
            self.PLAYER_X = self.COURT_LEFT + 10
            self.COMPUTER_X = config.screen_width - self.PLAYER_X - 10
            
            
            self.stuck = True
            
            
            self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
            self.computery = self.playery
            
            
            
            
            self.bx = self.PLAYER_X + 20
            self.by = self.playery
            self.bdx = .5
            self.bdy = .5
            
            
            if store.minigame_table_tennis_difficulty == "easy":
                self.original_bspeed = 700.0
                
                
                self.computerspeed = int(self.original_bspeed/2) + 85
                self.max_bspeed = 1200
            
            elif store.minigame_table_tennis_difficulty == "medium":
                self.original_bspeed = 800.0
                
                
                
                self.computerspeed = self.original_bspeed - 150
                self.max_bspeed = 1800
            
            else:
                self.original_bspeed = 900.0
                
                
                
                self.computerspeed = self.original_bspeed
                self.max_bspeed = 2200
            
            if store.minigame_table_tennis_instant_win_mode:
                self.computerspeed = 0
            
            
            self.bspeed = self.original_bspeed
            
            
            self.oldst = None
            
            
            self.winner = None
            
            
            
            self.leeway = 10
        
        def visit(self):
            return [ self.paddle, self.ball, self.ctb ]
        
        
        
        def render(self, width, height, st, at):
            
            
            r = renpy.Render(width, height)
            
            
            if self.oldst is None:
                self.oldst = st
            
            dtime = st - self.oldst
            self.oldst = st
            
            
            speed = dtime * self.bspeed
            oldbx = self.bx
            
            if self.stuck:
                self.by = self.playery
            else:
                self.bx += self.bdx * speed
                self.by += self.bdy * speed
            
            
            
            cspeed = self.computerspeed * dtime
            if abs(self.by - self.computery) <= cspeed:
                self.computery = self.by
            else:
                self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)
            
            
            
            
            ball_top = self.COURT_TOP + self.BALL_HEIGHT / 2
            if self.by < ball_top:
                self.by = ball_top + (ball_top - self.by)
                self.bdy = -self.bdy
            
            
            
            ball_bot = self.COURT_BOTTOM - self.BALL_HEIGHT / 2
            if self.by > ball_bot:
                self.by = ball_bot - (self.by - ball_bot)
                self.bdy = -self.bdy
            
            
            
            def paddle(px, py, hotside, is_player):
                
                
                
                
                
                
                pi = renpy.render(self.paddle, config.screen_width, config.screen_height, st, at)
                
                
                
                r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))
                
                if is_player:
                    hit_leeway = self.leeway
                
                else:
                    hit_leeway = 0
                
                if ( ( py - ( self.PADDLE_HEIGHT / 2 ) - hit_leeway ) ) <= self.by <= ( ( py + ( self.PADDLE_HEIGHT / 2 ) + hit_leeway ) ):
                    
                    hit = False
                    
                    
                    if is_player and self.bdx < 0 and oldbx > self.bx and self.bx <= hotside and oldbx >= px:
                        self.bx = hotside + (hotside - self.bx)
                        self.bdx = -self.bdx
                        hit = True
                    
                    elif not is_player and self.bdx > 0 and oldbx < self.bx and self.bx >= hotside and oldbx <= px + self.PADDLE_WIDTH:
                        self.bx = hotside - (self.bx - hotside)
                        self.bdx = -self.bdx
                        hit = True
                    
                    if hit:
                        
                        self.bspeed *= 1.10
                        self.bspeed = min(self.max_bspeed, self.bspeed)
            
            
            paddle(self.PLAYER_X, self.playery, self.PLAYER_X + self.PADDLE_WIDTH, True)
            paddle(self.COMPUTER_X, self.computery, self.COMPUTER_X, False)
            
            player_icon_render = renpy.render(self.player_icon, config.screen_width, config.screen_height, st, at)
            r.blit(player_icon_render, (self.PLAYER_ICON_X, int(self.playery - self.PADDLE_HEIGHT / 2) - ( int( (self.ICON_HEIGHT - self.PADDLE_HEIGHT) / 2 ) ) ) )
            
            opponent_icon_render = renpy.render(self.opponent_icon, config.screen_width, config.screen_height, st, at)
            r.blit(opponent_icon_render, (self.OPPONENT_ICON_X, int(self.computery - self.PADDLE_HEIGHT / 2) - ( int( (self.ICON_HEIGHT - self.PADDLE_HEIGHT) / 2 ) ) ) )
            
            
            ball = renpy.render(self.ball, config.screen_width, config.screen_height, st, at)
            r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                          int(self.by - self.BALL_HEIGHT / 2)))
            
            
            
            
            
            
            if self.stuck:
                
                ctb = renpy.render(Fixed( self.ctb, xysize = ( config.screen_width, config.screen_height ) ), config.screen_width, config.screen_height, st, at)
                r.blit(ctb, (0, 0))
            
            
            
            if self.bx < -200:
                self.winner = "opponent"
                
                
                
                renpy.timeout(0)
            
            elif self.bx > config.screen_width + 200:
                
                
                
                self.winner = "player"
                renpy.timeout(0)
            
            
            
            renpy.redraw(self, 0)
            
            
            return r
        
        
        def event(self, ev, x, y, st):
            
            import pygame
            
            
            
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                self.stuck = False
            
            if y >= 0 and y <= 1920:
                
                y = max(y, self.COURT_TOP)
                y = min(y, self.COURT_BOTTOM)
                self.playery = y
            
            
            
            if self.winner:
                return self.winner
            else:
                raise renpy.IgnoreEvent()

label minigame_table_tennis(partner=k):
    call process_new_location ("bg tennis_field")

    $ no_bust_art = False

    python:
        minigame_table_tennis_player_score = 0
        minigame_table_tennis_partner_score = 0
        minigame_table_tennis_partner_win_threshold = 2

    $ minigame_table_tennis_instant_win_mode = False
    if config.developer:
        "CONFIG/DEVELOPER MODE: Активировать невероятно простой режим (выигрывайте без особых усилий)?"
        menu:
            "Да":
                $ minigame_table_tennis_instant_win_mode = True
            "Нет":
                pass

    if partner:
        $ minigame_table_tennis_partner = partner
    else:
        $ minigame_table_tennis_partner = k

    if minigame_table_tennis_partner == k:
        $ display_multiple_characters([ (n, ""), (k, "") ])
        call process_character (k, appearance="yea", text="Хэй")
    elif minigame_table_tennis_partner == edna:
        $ diceroll = random.randint(1,3)
        if diceroll == 1:
            $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral"), (edna, "outfit clothes pose handclasp face happy blush false") ])
            call process_character (edna, appearance="pose handclasp face happy blush false", text="У меня теннисные ракетки в сумке.")
            call process_character (edna, appearance="pose handclasp face happy blush false", text="Давайте отправимся на корт!")
        elif diceroll == 2:
            $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral"), (edna, "outfit clothes pose handhip face neutral blush false") ])
            call process_character (edna, appearance="pose handhip face neutral blush false", text="Хорошо, у меня есть немного времени поиграть.")
            call process_character (edna, appearance="pose handhip face neutral blush false", text="Не забудь взять с собой много воды.")
        else:
            $ display_multiple_characters([ (n, "outfit clothesjacket pose handpocket face neutral"), (edna, "outfit clothes pose fisthip face happy blush false") ])
            call process_character (edna, appearance="pose fisthip face happy blush false", text="Это становится твоим любимым видом спорта, [n.say_name]?")

    window hide
    menu:
        "Лёгкая":
            $ minigame_table_tennis_difficulty = "easy"
        "Средняя (Увеличение Смелости!)":
            $ minigame_table_tennis_difficulty = "medium"
        "Тяжёлая (Увеличение Смелости!)":
            $ minigame_table_tennis_difficulty = "hard"

    $ diceroll = random.randint(1,2)

    if minigame_table_tennis_partner == k:
        pass
    elif minigame_table_tennis_partner == edna:
        if minigame_table_tennis_difficulty == "easy":
            if diceroll == 1:
                call process_character (edna, appearance="pose handclasp face neutral blush false", text="Лучше начать медленно.")
                call process_character (edna, appearance="pose handclasp face neutral blush false", text="Ты поймёшь, как играть, в кратчайшие сроки!")
            else:
                call process_character (edna, appearance="pose fisthip face neutral blush false", text="Дай мне знать, если я буду бить быстро.")
                call process_character (edna, appearance="pose fisthip face neutral blush false", text="Это сила привычки!")
        elif minigame_table_tennis_difficulty == "medium":
            if diceroll == 1:
                call process_character (edna, appearance="pose handhip face neutral blush false", text="Иногда я буду бить кручённым.")
                call process_character (edna, appearance="pose handhip face neutral blush false", text="Следи за этим!")
            else:
                call process_character (edna, appearance="pose handclasp face neutral blush false", text="С тех пор, как я начала играть, я заметила, что могу лучше двигать ногами.")
                call process_character (edna, appearance="pose handclasp face happy blush false", text="Это должно помогать моим суставам!")
        else:
            if diceroll == 1:
                call process_character (edna, appearance="pose fisthip face neutral blush false", text="Ты почувствуешь это в ногах после!")
                call process_character (edna, appearance="pose fisthip face neutral blush false", text="Я обычно кладу на них лед.")
            else:
                call process_character (edna, appearance="pose handclasp face neutral blush false", text="Я работаю над улучшением подачи.")
                call process_character (edna, appearance="pose handclasp face happy blush false", text="Дай мне посмотреть, что ты об этом думаешь!")

    $ disable_saving()
    $ disable_rollback()
    window hide
    $ clear_characters()

    show screen minigame_table_tennis_score_display

    jump minigame_table_tennis_round

    return

screen minigame_table_tennis_score_display:
    text n.say_name + ": " + str(minigame_table_tennis_player_score) xalign 0.05 size 64
    text minigame_table_tennis_partner.say_name + ": " + str(minigame_table_tennis_partner_score) xalign 0.95 size 64

label minigame_table_tennis_round:
    window hide

    python:
        ui.add(TableTennis())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    window show None

    if winner == "opponent":
        $ minigame_table_tennis_partner_score += 1
        "Вы проиграли этот раунд."
    else:

        $ minigame_table_tennis_player_score += 1
        "Вы выиграли этот раунд!"



    if minigame_table_tennis_player_score >= minigame_table_tennis_partner_win_threshold:
        jump minigame_table_tennis_win
    elif minigame_table_tennis_partner_score >= minigame_table_tennis_partner_win_threshold:
        jump minigame_table_tennis_lose
    else:
        jump minigame_table_tennis_round

    return


label minigame_table_tennis_lose:
    if minigame_table_tennis_partner == k:
        $ display_multiple_characters([ (n, "face curious"), (k, "face happy") ])
        call process_character (k, appearance="face happy", text="Да!")
    elif minigame_table_tennis_partner == edna:
        if minigame_table_tennis_difficulty == "easy":
            $ display_multiple_characters([ (n, "outfit clothesjacket face curious"), (edna, "outfit clothes pose handclasp face concerned blush false") ])
            call process_character (edna, appearance="pose handclasp face concerned blush false", text="Возможно, твоя ракетка слишком тяжелая, [n.say_name]?")
        elif minigame_table_tennis_difficulty == "medium":
            $ display_multiple_characters([ (n, "outfit clothesjacket face curious"), (edna, "outfit clothes pose handhip face neutral blush false") ])
            call process_character (edna, appearance="pose handhip face neutral blush false", text="Следи за мячом, как говорится!")
            call process_character (edna, appearance="pose handhip face neutral blush false", text="Не спускай с него глаз!")
        else:
            $ display_multiple_characters([ (n, "outfit clothesjacket face curious"), (edna, "outfit clothes pose fisthip face neutral blush false") ])
            call process_character (edna, appearance="pose fisthip face neutral blush false", text="Почти, [n.say_name]!")
            call process_character (edna, appearance="pose fisthip face neutral blush false", text="Продолжай работать над этим!")

    jump minigame_table_tennis_end

    return

label minigame_table_tennis_win:
    $ renpy.scene('screens')
    show screen hud
    $ minigame_table_tennis_win_money = 4
    if minigame_table_tennis_partner == k:
        if minigame_table_tennis_difficulty == "easy":
            $ k.add_points(2, minigame = True)
            $ minigame_table_tennis_win_money = 4
            $ display_multiple_characters([ (n, "face happy"), (k, "face concerned") ])
            call process_character (k, appearance="face concerned", text="Черт")
        elif minigame_table_tennis_difficulty == "medium":
            call add_points_and_boldness (k, 3, 1, minigame=True)
            $ minigame_table_tennis_win_money = 6
            $ display_multiple_characters([ (n, "face happy"), (k, "face concerned") ])
            call process_character (k, appearance="face concerned", text="Черт")
        else:
            call add_points_and_boldness (k, 4, 1, minigame=True)
            $ minigame_table_tennis_win_money = 8
            $ display_multiple_characters([ (n, "face happy"), (k, "face concerned") ])
            call process_character (k, appearance="face concerned", text="Черт")
    elif minigame_table_tennis_partner == edna:
        if minigame_table_tennis_difficulty == "easy":
            $ edna.add_points(2, minigame = True)
            $ minigame_table_tennis_win_money = 4
            $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (edna, "outfit clothes pose fisthip face neutral blush false") ])
            call process_character (edna, appearance="pose fisthip face neutral blush false", text="Ты более чем способен на это, [n.say_name].")
            call process_character (edna, appearance="pose fisthip face neutral blush false", text="Я знаю, что ты справишься со следующим уровнем!")
        elif minigame_table_tennis_difficulty == "medium":
            call add_points_and_boldness (edna, 3, 1, minigame=True)
            $ minigame_table_tennis_win_money = 6
            $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (edna, "outfit clothes pose handclasp face happy blush false") ])
            call process_character (edna, appearance="pose handclasp face happy blush false", text="И мой внук одержал победу!")
        else:
            call add_points_and_boldness (edna, 4, 1, minigame=True)
            $ minigame_table_tennis_win_money = 8
            $ diceroll = random.randint(1,2)
            if diceroll == 1:
                $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (edna, "outfit clothes pose fisthip face shock blush false") ])
                call process_character (edna, appearance="pose fisthip face shock blush false", text="Ты победил меня, [n.say_name]!")
                call process_character (edna, appearance="pose fisthip face shock blush false", text="Довольно скоро ты будешь получать трофеи!")
            else:
                $ display_multiple_characters([ (n, "outfit clothesjacket face happy"), (edna, "outfit clothes pose handhip face happy blush false") ])
                call process_character (edna, appearance="pose handhip face happy blush false", text="У тебя хороший размах, [n.say_name]!")
                call process_character (edna, appearance="pose handhip face happy blush false", text="И ты на ногах!")

    python hide:
        inventory.add_money(minigame_table_tennis_win_money, minigame = True)
        narrator("Получено $" + str(minigame_table_tennis_win_money) + " за победу.")

    jump minigame_table_tennis_end

    return

label minigame_table_tennis_end:
    $ renpy.scene('screens')

    $ enable_saving()
    $ renpy.block_rollback()
    $ enable_rollback()

    call process_end_of_minigame ("minigame_table_tennis")

    return