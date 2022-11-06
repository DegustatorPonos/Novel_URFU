init python:
    def review_help_item_action():
        store.sa.add_points(2, yalign = 0.025)
        store.minigame_typing_times_succeeded += 1
        store.minigame_typing_times_succeeded_since_last_vicky_meeting += 1
        return

    def uncapitalize(string):
        if len(string) > 0:
            string = string[0].lower() + string[1:]
        
        return string
    def minigame_typing_review_countdown_boost_amount():
        if store.inventory.has_item(2):
            return 5
        
        return 0

    def minigame_typing_review_subjects_singular_list():
        subjects = []
        
        subjects.append("music")
        subjects.append("multiplayer")
        subjects.append("playtime")
        subjects.append("story")
        subjects.append("gameplay")
        subjects.append("learning curve")
        subjects.append("performance")
        subjects.append("presentation")
        subjects.append("experience")
        subjects.append("voice acting")
        subjects.append("single player")
        subjects.append("interface")
        subjects.append("downloadable content")
        subjects.append("cost")
        subjects.append("replay value")
        subjects.append("customization")
        subjects.append("frame rate")
        subjects.append("dialog")
        subjects.append("artificial intelligence")
        subjects.append("design")
        subjects.append("writing")
        subjects.append("exploration")
        subjects.append("combat")
        subjects.append("world map")
        
        random.shuffle(subjects)
        return subjects

    def minigame_typing_review_subjects_plural_list():
        subjects = []
        
        subjects.append("controls")
        subjects.append("graphics")
        subjects.append("sound effects")
        subjects.append("options")
        subjects.append("campaigns")
        subjects.append("servers")
        subjects.append("endings")
        subjects.append("choices")
        subjects.append("levels")
        subjects.append("cutscenes")
        subjects.append("achievements")
        subjects.append("easter eggs")
        subjects.append("rewards")
        subjects.append("unlockables")
        subjects.append("bosses")
        subjects.append("enemies")
        subjects.append("quests")
        subjects.append("characters")
        subjects.append("camera angles")
        subjects.append("collectables")
        subjects.append("environments")
        subjects.append("animations")
        subjects.append("models")
        subjects.append("textures")
        
        random.shuffle(subjects)
        return subjects

    def minigame_typing_edgy_bad_why():
        why = []
        why.append("we can't have nice things")
        why.append("aliens don't visit us")
        why.append("aliens don't talk to us")
        why.append("humanity is doomed")
        why.append("there is no hope for humanity")
        why.append("games were better before")
        why.append("I'm quitting video games forever")
        why.append("this year sucks")
        why.append("games have lower standards today")
        why.append("publishers mess up the final product")
        why.append("game companies end up closing")
        why.append("the sun will implode sooner")
        why.append("asteroids hit the Earth")
        
        random.shuffle(why)
        return why

    def minigame_typing_edgy_bad_adjectives():
        adjectives = []
        adjectives.append("like getting coal for Christmas")
        adjectives.append("like being punched in the face")
        adjectives.append("mind numbing")
        adjectives.append("from hell")
        adjectives.append("cringe worthy")
        adjectives.append("taking years from my life")
        adjectives.append("vomit-inducing")
        adjectives.append("repulsive")
        adjectives.append("abhorrent")
        adjectives.append("revolting")
        adjectives.append("horrendous")
        adjectives.append("obnoxious")
        adjectives.append("agonizing")
        adjectives.append("pitiful")
        adjectives.append("nauseating")
        adjectives.append("a major let down")
        adjectives.append("pure suffering")
        adjectives.append("spirit crushing")
        adjectives.append("useless")
        adjectives.append("hate-inspiring")
        adjectives.append("unforgivable")
        adjectives.append("not worthy of any praise")
        adjectives.append("a let down")
        adjectives.append("amazingly disappointing")
        adjectives.append("causing terminal illness in players")
        adjectives.append("the worst of all time")
        adjectives.append("making me question reality")
        adjectives.append("nightmare-inducing")
        adjectives.append("making me question my life")
        adjectives.append("0/10")
        adjectives.append("giving me an existential crisis")
        adjectives.append("why %why")
        adjectives.append("the reason why %why")
        adjectives.append("only slightly better than %bad_thing")
        adjectives.append("worse than %bad_thing")
        adjectives.append("about as pleasant as %bad_thing")
        adjectives.append("less enjoyable than %bad_thing")
        
        random.shuffle(adjectives)
        return adjectives

    def minigame_typing_edgy_bad_things():
        things = []
        things.append("drowning")
        things.append("eating acorns")
        things.append("like getting set on fire")
        things.append("dipping my hands in acid")
        things.append("having an existential crisis")
        things.append("brushing my teeth and then drinking orange juice")
        things.append("being stuck in an elevator after a fart")
        things.append("supergluing both my hands to my face")
        things.append("writing ten book reports")
        things.append("waiting several hours in a line")
        things.append("having to write in cursive")
        things.append("getting set on fire")
        things.append("stepping on sharp rocks")
        things.append("falling down the stairs")
        things.append("crapping your pants")
        things.append("stubbing your toe")
        things.append("like getting socks for my birthday")
        things.append("like getting socks for my birthday")
        things.append("bashing your head on a wall")
        things.append("chugging vegetable oil")
        things.append("ripping my toenail off")
        
        
        random.shuffle(things)
        return things

    def minigame_typing_edgy_good_adjectives():
        adjectives = []
        adjectives.append("better than you")
        adjectives.append("better than we deserve")
        adjectives.append("better than your favorite game's")
        adjectives.append("the best since sliced bread")
        adjectives.append("11/10")
        adjectives.append("why I keep living")
        adjectives.append("why humanity has a chance")
        
        random.shuffle(adjectives)
        return adjectives

    def minigame_typing_review_bad_adjectives():
        adjectives = []
        adjectives.append("Disappointing")
        adjectives.append("Buggy")
        adjectives.append("Unacceptable")
        adjectives.append("Inferior")
        adjectives.append("Uninspired")
        adjectives.append("Rushed")
        adjectives.append("Unnatural")
        adjectives.append("Rehashed")
        adjectives.append("Abysmal")
        adjectives.append("Dreadful")
        adjectives.append("Unsatisfactory")
        adjectives.append("Bad")
        adjectives.append("Awful")
        adjectives.append("Glitchy")
        adjectives.append("Broken")
        adjectives.append("Atrocious")
        adjectives.append("Disastrous")
        adjectives.append("Low grade")
        adjectives.append("Inadequate")
        adjectives.append("Insufficient")
        adjectives.append("Mediocre")
        adjectives.append("Frustrating")
        adjectives.append("Meager")
        adjectives.append("Paltry")
        adjectives.append("Lacking")
        adjectives.append("Inconsistent")
        adjectives.append("Crummy")
        adjectives.append("Subpar")
        adjectives.append("Trivial")
        adjectives.append("Boring")
        adjectives.append("Tedious")
        adjectives.append("Deficient")
        adjectives.append("Unfortunate")
        adjectives.append("Underwhelming")
        adjectives.append("Stiff")
        
        random.shuffle(adjectives)
        return adjectives

    def minigame_typing_review_neutral_adjectives():
        adjectives = []
        adjectives.append("Acceptable")
        adjectives.append("Average")
        adjectives.append("Okay")
        adjectives.append("Fair")
        adjectives.append("Unexceptional")
        adjectives.append("Sufficient")
        adjectives.append("Conventional")
        adjectives.append("Tolerable")
        adjectives.append("Passable")
        adjectives.append("Typical")
        adjectives.append("Regular")
        adjectives.append("Forgettable")
        adjectives.append("Normal")
        adjectives.append("Generic")
        adjectives.append("Commonplace")
        adjectives.append("Ordinary")
        adjectives.append("Predictable")
        adjectives.append("Familiar")
        adjectives.append("Satisfactory")
        adjectives.append("Reasonable")
        adjectives.append("Bland")
        adjectives.append("Mixed")
        adjectives.append("Standard")
        adjectives.append("Modest")
        adjectives.append("Humble")
        adjectives.append("Alright")
        adjectives.append("Decent")
        adjectives.append("Fine")
        
        random.shuffle(adjectives)
        return adjectives

    def minigame_typing_review_good_adjectives():
        adjectives = []
        adjectives.append("Amazing")
        adjectives.append("Spectacular")
        adjectives.append("Confident")
        adjectives.append("Fitting")
        adjectives.append("Fresh")
        adjectives.append("Varied")
        adjectives.append("Clean")
        adjectives.append("Cool")
        adjectives.append("Good")
        adjectives.append("Outstanding")
        adjectives.append("Remarkable")
        adjectives.append("Cool")
        adjectives.append("Likeable")
        adjectives.append("Interesting")
        adjectives.append("Engrossing")
        adjectives.append("Immersive")
        adjectives.append("Impressive")
        adjectives.append("Awesome")
        adjectives.append("Responsive")
        adjectives.append("Incredible")
        adjectives.append("Sensational")
        adjectives.append("Entertaining")
        adjectives.append("Fun")
        adjectives.append("Enjoyable")
        adjectives.append("Classic")
        adjectives.append("Blissful")
        adjectives.append("Beautiful")
        adjectives.append("Great")
        adjectives.append("Nice")
        adjectives.append("Fantastic")
        adjectives.append("Terrific")
        adjectives.append("Memorable")
        adjectives.append("Admirable")
        
        random.shuffle(adjectives)
        return adjectives

    def minigame_typing_review_short_sentences(num):
        lines = []
        
        for i in range(0, num):
            subject_tag = "%subject_singular"
            
            if random.randint(1,2) == 1:
                subject_tag = "%subject_plural"
            
            lines.append("%Adjective " + subject_tag + ".")
        
        return lines

    def minigame_typing_review_medium_sentences(num, force_the = False):
        lines = []
        
        for i in range(0, num):
            line = ""
            
            if random.randint(1,2) == 1 or force_the:
                line += "The "
                subject_tag = "%subject"
            else:
                subject_tag = "%Subject"
            
            if random.randint(1,2) == 1:
                copula = "is" if random.randint(1,2) == 1 else "was"
                subject_tag += "_singular"
            else:
                copula = "are" if random.randint(1,2) == 1 else "were"
                subject_tag += "_plural"
            
            lines.append(line + subject_tag + " " + copula + " " + "%adjective.")
        
        random.shuffle(lines)
        return lines


    def minigame_typing_review_casual_lines():
        lines = []
        
        single_words_num = store.minigame_typing_lines_number
        for i in range(0, single_words_num):
            lines.append("%Adjective.")
        
        random.shuffle(lines)
        return lines

    def minigame_typing_review_indepth_lines():
        lines = []
        sentence_number = int(store.minigame_typing_lines_number/2)
        sentences = minigame_typing_review_short_sentences(sentence_number)
        
        lines.extend(sentences)
        
        single_words_num = store.minigame_typing_lines_number - sentence_number
        for i in range(0, single_words_num):
            lines.append("%Adjective.")
        
        random.shuffle(lines)
        return lines

    def minigame_typing_review_edgy_lines():
        lines = []
        
        medium_sentences_number = store.minigame_typing_lines_number
        medium_sentences = minigame_typing_review_medium_sentences(medium_sentences_number, force_the = True)
        
        lines.extend(medium_sentences)
        
        random.shuffle(lines)
        return lines

    def minigame_typing_replace_in_lines(lines):
        new_lines = []
        for line in lines:
            if "%Adjective" in line:
                line = line.replace("%Adjective", store.minigame_typing_review_adjectives.pop().capitalize())
            
            if "%adjective" in line:
                line = line.replace("%adjective", uncapitalize(store.minigame_typing_review_adjectives.pop()) )
            
            
            if "%Adverb" in line:
                line = line.replace("%Adverb", store.minigame_typing_review_adverbs.pop().capitalize())
            
            if "%adverb" in line:
                line = line.replace("%adverb", uncapitalize(store.minigame_typing_review_adverbs.pop()) )
            
            if "%Subject_singular" in line:
                line = line.replace("%Subject_singular", store.minigame_typing_review_subjects_singular.pop().capitalize())
            if "%Subject_plural" in line:
                line = line.replace("%Subject_plural", store.minigame_typing_review_subjects_plural.pop().capitalize())
            
            if "%subject_singular" in line:
                line = line.replace("%subject_singular", uncapitalize(store.minigame_typing_review_subjects_singular.pop()) )
            if "%subject_plural" in line:
                line = line.replace("%subject_plural", uncapitalize(store.minigame_typing_review_subjects_plural.pop()) )
            
            if "%bad_thing" in line:
                line = line.replace("%bad_thing", uncapitalize(store.minigame_typing_review_bad_things.pop()) )
            
            if "%why" in line:
                line = line.replace("%why", uncapitalize(store.minigame_typing_review_why.pop()) )
            
            new_lines.append(line)
        
        return new_lines

label minigame_typing_too_slow:
    call hide_minigame_countdown
    call minigame_typing_review_result
    return

label minigame_typing_review_set_lines:
    python:
        minigame_typing_lines = []
        minigame_typing_review_game_quality = random.randint(1,3)

        if minigame_typing_review_game_quality == 1:
            
            minigame_typing_review_adjectives = minigame_typing_review_bad_adjectives()
        elif minigame_typing_review_game_quality == 2:
            
            minigame_typing_review_adjectives = minigame_typing_review_neutral_adjectives()
        else:
            
            minigame_typing_review_adjectives = minigame_typing_review_good_adjectives()

    menu:
        "Я напишу обычной обзор.":
            $ minigame_typing_review_difficulty = "easy"
            $ minigame_typing_review_money_reward_sam_points = 1
            $ minigame_countdown_duration = 60
            $ minigame_typing_lines = minigame_typing_review_casual_lines()
        "Я напишу углубленный обзор. (Увеичение Смелости)":
            $ minigame_typing_review_difficulty = "medium"
            $ minigame_typing_review_money_reward_sam_points = 1
            $ minigame_countdown_duration = 70
            $ minigame_typing_lines = minigame_typing_review_indepth_lines()
        "я напишу спорный обзор. (Увеичение Смелости)":
            $ minigame_typing_review_difficulty = "hard"
            $ minigame_typing_review_money_reward_sam_points = 2

            $ minigame_typing_review_game_quality = 1
            $ minigame_typing_review_adjectives = minigame_typing_edgy_bad_adjectives()
            $ minigame_countdown_duration = 95
            $ minigame_typing_lines = minigame_typing_review_edgy_lines()

    $ minigame_countdown_duration += minigame_typing_review_countdown_boost_amount()
    $ minigame_countdown_duration += minigame_typing_review_countdown_addend

    $ disable_saving()

    if config.developer:
        "DEBUG/DEVELOPER MODE: Only one line."

    if minigame_typing_review_game_quality == 1:

        if minigame_typing_review_difficulty == "easy":
            call process_character (n, appearance="pose handpocket face curious", text="(Эта дрянная игра, не нужно много писать про неё)")
        elif minigame_typing_review_difficulty == "medium":
            call process_character (n, appearance="pose handpocket face curious", text="(Это впечатляет, сколько много неправильных вещей в этой последней игрой)")
        else:
            call process_character (n, appearance="pose twohandfist face happy", text="(Этот обзор должен вызвать много дискуссий в интернете!)")

    elif minigame_typing_review_game_quality == 2:

        if minigame_typing_review_difficulty == "easy":
            call process_character (n, appearance="pose handpocket face neutral", text="(Я думаю, что быстрый и легкий обзор отлично подходит для этой игры)")
        elif minigame_typing_review_difficulty == "medium":
            call process_character (n, appearance="pose behindhead face neutral", text="(Эта игра не идеальна, но она заслуживает полного обзора)")
    else:


        if minigame_typing_review_difficulty == "easy":
            call process_character (n, appearance="pose handfist face happy", text="(Ничего, но есть хорошие вещи в этой игре, о которых можно сказать!)")
        elif minigame_typing_review_difficulty == "medium":
            call process_character (n, appearance="pose twohandfist face happy", text="(С чего начать, когда речь идет об этой удивительной игре!)")

    $ clear_characters()
    python:
        minigame_typing_lines = minigame_typing_lines[:minigame_typing_lines_number]
        random.shuffle(minigame_typing_lines)
        minigame_typing_lines = minigame_typing_replace_in_lines(minigame_typing_lines)

    return

screen minigame_typing_review_info:
    text str(minigame_typing_lines_correct) + "/" + str(minigame_typing_lines_number) size 72 xalign 0.02

label minigame_typing_review_intro:
    call process_character (n, appearance="pose handpocket face neutral", text="(Я должен написать столько обзоров, сколько смогу для канала [video_sharing_site])")
    call process_character (n, appearance="pose handpocket face neutral", text="(Я уверен, {b}что это займет время,{/b} написать его)")
    call process_character (n, appearance="pose handpocket face neutral", text="(Интересно, какой обзор я должен сделать?)")
    call process_character (n, appearance="pose handpocket face neutral", text="(Я мог бы написать {b}обычной обзор{/b}, это будет легко...)")
    call process_character (n, appearance="pose handpocket face neutral", text="(Но, вероятно, он не получит много просмотров или дохода)")
    call process_character (n, appearance="pose handpocket face neutral", text="(Я мог бы написать {b}углубленный обзор{/b} и более подробно)")
    call process_character (n, appearance="pose handpocket face neutral", text="(Что позволит получить больше просмотров и дохода)")
    call process_character (n, appearance="pose handpocket face neutral", text="(Или я мог бы бросить вызов себе и написать {b}спорный{/b} обзор)")
    call process_character (n, appearance="pose handpocket face neutral", text="(Канал обязательно получит от этого внимание и доход!)")
    call process_character (n, appearance="pose handpocket face neutral", text="(Хорошо, время начинать!)")

    return

label minigame_typing_review:
    call process_scene_beginning (nate_room)

    if "minigame_typing_review" not in minigames_tried:
        call minigame_typing_review_intro

    $ disable_rollback()

    python:
        minigame_typing_lines_correct = 0
        minigame_typing_lines_number = 7

        if config.developer:
            minigame_typing_lines_number = 1

        minigame_typing_review_subjects_singular = minigame_typing_review_subjects_singular_list()
        minigame_typing_review_subjects_plural = minigame_typing_review_subjects_plural_list()

        minigame_typing_review_bad_things = minigame_typing_edgy_bad_things()
        minigame_typing_review_why = minigame_typing_edgy_bad_why()

        minigame_typing_review_adjectives = []
        minigame_typing_review_adverbs = []
        minigame_typing_review_type = ""
        minigame_countdown_duration = 60
        minigame_typing_words_typed = 0
        minigame_typing_review_second_place_threshold = .50
        minigame_typing_review_started = True


        minigame_typing_review_difficulty = "easy"

        minigame_typing_review_controversial = False

    call minigame_typing_review_set_lines
    show screen minigame_typing_review_info
    call minigame_countdown (minigame_countdown_duration, "minigame_typing_too_slow")
    call minigame_typing_round ("minigame_typing_review_result")

    return

label minigame_typing_round(end_label="minigame_typing_review_won", prompt=None, default=""):
    python:
        store.name_input_color = None

        if prompt is None:
            prompt = minigame_typing_lines.pop()

        displayed_prompt = prompt

        if "minigame_typing_review" not in minigames_tried:
            displayed_prompt = prompt + "\n(Введите тот же текст, что написан сверху и нажмите Enter.)"

        typed = renpy.input(displayed_prompt, pixel_width = gui.text_width_typing_review_minigame)


    if typed != prompt and (typed + ".") != prompt:
        call minigame_typing_round (end_label, prompt=prompt)
    else:
        $ minigame_typing_words_typed += len ( prompt.split() )
        $ minigame_typing_lines_correct += 1

        if minigame_typing_lines_correct >= minigame_typing_lines_number:
            $ renpy.call(end_label)
        else:
            call minigame_typing_round (end_label)

    return

label minigame_typing_review_result:
    $ minigame_typing_review_started = False
    $ enable_saving()

    call hide_minigame_countdown
    python:
        ratio = minigame_typing_lines_correct/ float(minigame_typing_lines_number)
        mingame_typing_wpm = int( (minigame_typing_words_typed * 60) / countdown_elapsed )
        minigame_typing_review_money_reward = 0
        minigame_typing_review_money_reward_sam_share = 0




    if ratio <= 0.0:
        call process_character (n, appearance="pose behindhead face curious", text="(Чувак, у меня был серьезный творческий кризис)")
    elif ratio < minigame_typing_review_second_place_threshold:
        call process_character (n, appearance="pose behindhead face concerned", text="(Эх, я не думаю, что этот обзор достаточно хорош для публикации)")
    elif ratio < 1.0:
        call process_character (n, appearance="pose handpocket face neutral", text="(Не плохо! Думаю, людям это понравится)")

        if minigame_typing_review_difficulty == "easy":
            $ minigame_typing_review_money_reward = 4
        elif minigame_typing_review_difficulty == "medium":
            $ minigame_typing_review_money_reward = 6
        else:
            $ minigame_typing_review_money_reward = 8
    else:
        call process_character (n, appearance="pose handfist face happy", text="(Этот отзыв получился отличным!)")

        if minigame_typing_review_difficulty == "hard":
            call process_character (n, appearance="pose behindhead face neutral", text="(Это было потрясающе писать так откровенно!)")

        if minigame_typing_review_difficulty == "easy":
            $ minigame_typing_review_money_reward = 1000
        elif minigame_typing_review_difficulty == "medium":
            call add_boldness (1, minigame=True)
            $ minigame_typing_review_money_reward = 8
        else:
            call add_boldness (1, minigame=True)
            $ minigame_typing_review_money_reward = 10

    if minigame_typing_review_money_reward > 0:

        if "vicky_tease_scene" in scenes_completed:
            $ minigame_typing_review_money_reward = int( round( ( minigame_typing_review_money_reward * 2 ) * 0.80 ) )

        $ minigame_typing_times_succeeded += 1
        $ minigame_typing_times_succeeded_since_last_vicky_meeting += 1

        $ minigame_typing_money_earned += minigame_typing_review_money_reward
        $ minigame_typing_money_earned_since_last_vicky_meeting += minigame_typing_review_money_reward

        $ minigame_typing_review_money_reward_sam_share = int( round( minigame_typing_review_money_reward / 2 ) )
        show screen hud
        call process_character (n, appearance="pose twohandfist face neutral", text="(Этот обзор должен принести $[minigame_typing_review_money_reward]!)")
        call process_character (n, appearance="pose handpocket face curious", text="(Я уверен, что разделение дохода с [sa.say_name] могло бы сделать ее счастливой...)")
        menu:
            "Поделиться деньгами с [sa.say_name].":
                $ minigame_typing_review_money_reward -= minigame_typing_review_money_reward_sam_share
                $ inventory.add_money(minigame_typing_review_money_reward, minigame = True)
                call process_character (n, appearance="pose handpocket face happy", text="(Она заслуживает награды за всю свою тяжелую работу на стриме!)")

                call add_points (sa, minigame_typing_review_money_reward_sam_points, delay=True, minigame=True)
            "Оставить деньги себе.":
                $ inventory.add_money(minigame_typing_review_money_reward, minigame = True)
                call process_character (n, appearance="pose handpocket face happy", text="(Я накоплю денег, чтобы купить что-нибудь крутое позже!)")


    $ renpy.block_rollback()
    $ enable_rollback()
    hide screen hud
    hide screen minigame_typing_review_info

    call process_end_of_minigame ("minigame_typing_review")

    return