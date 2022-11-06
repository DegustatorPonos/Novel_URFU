init -90 python:
    def add_dream_option(choice_list):
        choice_list.append( ("Мечтать", "day_dream") )
        
        return choice_list

    def advance_time_reinitializations():
        minigame_typing_review_started = False
        
        return

label day_start_before_location_reset:
    if had_julia_pre_arrival_scene and not had_julia_arrived_scene:
        jump julia_arrival

    if not had_janet_intro_scene and had_julia_arrived_scene and week.days_passed > 10:
        jump janet_intro

    if not had_edna_intro_scene and had_edna_pre_arrival_scene:
        jump edna_arrival_scene

    python:
        if week.is_school_day():
            is_school_time = True
            is_school_day = True
        else:
            is_school_time = False
            is_school_day = False

    return

label day_start_after_location_reset:
    if not had_julia_pre_arrival_scene and week.weeks_passed > 0:
        jump julia_pre_arrival

    if not had_edna_pre_arrival_scene and had_janet_intro_scene and week.days_passed >= 14:
        jump edna_pre_arrival_scene



    if minigame_typing_times_succeeded > 0 and not had_vicky_pre_intro_scene:
        jump vicky_pre_intro

    if minigame_typing_times_succeeded >= 3 and had_vicky_pre_intro_scene and not had_vicky_intro_scene:
        jump vicky_intro



    if week.is_school_day():
        call school_morning_start_wakeup
    else:
        show screen hud
        $ advance_time_return_location.start(force_music_change = True, morning_wake_lines = True)

    return

label school_activate_start:
    if week.day != 5 and week.day != 6:
        call process_character (n, appearance="yes", text="Мне лучше подготовиться к возвращению в школу.")
    else:
        call process_character (n, appearance="yes", text="Мне лучше подготовиться к возвращению в школу на следующей неделе.")

    $ clear_characters(Dissolve(0.3))
    $ started_school = True
    call navigation_menu

    return


label school_morning_start_wakeup:
    window hide
    show screen hud
    $ school_homeroom.decide_and_play_daily_music_queue()
    $ bust_art_background(advance_time_return_location.background())
    call school_morning_wake_lines
    call school_start

    return

label school_start:
    $ bust_art_background(school_homeroom.background())
    call school_start_general_scene
    $ is_school_time = True
    $ is_school_day = True


    $ store.stats.current_location = school_homeroom
    $ store.stats.current_zone = school
    call navigation_menu

    return

label school_leave:
    $ is_school_time = False
    $ clear_characters(Dissolve(0.3))
    $ school.reset_locations_and_characters()
    $ week.days_of_school_passed += 1

    $ advance_time_return_location.start(force_music_change = False)

label school_start_general_scene:
    "Teacher" "Hello Class"

    return

label school_morning_wake_lines:
    $ n.reset_appearance(show_bust = False)
    python:
        random_line_array = []
        random_line_array.append( {"char": n, "appearance": "yea", "text": "Надеюсь, я не опоздал." } )
        random_line_array.append( {"char": n, "appearance": "yea", "text": "Пора в школу." } )

    call random_line (random_line_array)
    $ clear_characters(Dissolve(0.3))

    return

label morning_wake_lines:
    $ n.reset_appearance(show_bust = False)
    if has_fucked_everyone_in_home:
        $ n.outfit = "nudesoft"
    else:
        $ n.outfit = "underwear"

    python:
        random_line_array = []
        random_line_array.append( {"char": n, "appearance": "yea", "text": "{i}Ээ-а{/i}...Начинается новый день!" } )
        random_line_array.append( {"char": n, "appearance": "yea", "text": "Пора вставать и собираться!" } )
        random_line_array.append( {"char": n, "appearance": "yea", "text": "Интересно, что мне сегодня делать?" } )
        random_line_array.append( {"char": n, "appearance": "yea", "text": "Хорошо отдохнул и готов на всё!" } )

    call random_line (random_line_array)
    $ clear_characters(Dissolve(0.3))

    return

label sleep_lines:
    $ n.reset_appearance(show_bust = False)
    python:
        sleep_lines_outfit = "underwear"
        if store.has_fucked_everyone_in_home:
            sleep_lines_outfit = "nudesoft"
        random_line_array = []
        random_line_array.append( {"char": n, "appearance": "outfit " + sleep_lines_outfit + " face flirty", "text": "Спааать..." } )
        random_line_array.append( {"char": n, "appearance": "outfit " + sleep_lines_outfit + " face flirty", "text": "Нужно, как следует, выспаться..." } )
        random_line_array.append( {"char": n, "appearance": "outfit " + sleep_lines_outfit + " face flirty", "text": "Хорошо, время ложиться спать." } )
        random_line_array.append( {"char": n, "appearance": "outfit " + sleep_lines_outfit + " face flirty", "text": "Моя кровать выглядит такой удобной..." } )

    call random_line (random_line_array)

    return

label day_sleep_special_events:

    python:
        if replay_scenes_unlocked and not dream_intro_shown and dreams_had == 0:
            renpy.call("dream_intro")  

        if "finale_scene" not in scenes_completed and "kira_simone_threesome_scene" in scenes_completed and "simone_scene_titfuck" in scenes_completed and "kira_scene_pool_fuck" in scenes_completed and "edna_scene_blowjob" in scenes_completed and "janet_scene_anal" in scenes_completed and "vicky_scene_anal" in scenes_completed and "gloryhole_scene_stall" in scenes_completed and (("sam_scene_dream" in scenes_completed and "julia_scene_anal" in scenes_completed and "family_foursome_scene" in scenes_completed and "sam_simone_threesome_scene" in scenes_completed and "sam_julia_threesome_scene" in scenes_completed) or ("julia_scene_footjob" not in scenes_completed or "sam_scene_3" not in scenes_completed)):
            renpy.call("finale_scene")



        if k.relationship_level >= 10 and "kira_scene_6" in scenes_completed and "kira_scene_7" not in scenes_completed:
            renpy.call("kira_scene_7")

        if "simone_scene_undressing" not in new_scenes_completed_today and not si.prompted_scene and si.relationship_level >= 8 and "simone_scene_undressing" in scenes_completed and "simone_scene_masturbating" not in scenes_completed:
            renpy.call("simone_scene_masturbating")

        if "kira_simone_threesome_scene" not in scenes_completed and "simone_scene_blowjob" in scenes_completed and "simone_scene_blowjob" not in new_scenes_completed_today and "kira_scene_stealth_bj" in scenes_completed and "kira_scene_stealth_bj" not in new_scenes_completed_today:
            renpy.call("kira_simone_threesome_scene")

        if store.had_julia_arrived_scene and "julia_scene_underwear" not in scenes_completed and julia.relationship_level >= 2:
            renpy.call("julia_scene_underwear")

        if store.had_julia_arrived_scene and "julia_scene_bottomless" not in scenes_completed and "julia_scene_topless" in scenes_completed and julia.relationship_level >= 4:
            renpy.call("julia_scene_bottomless")

    return

label dream_intro:
    "Теперь Вы можете помечтать. В мечтах Вы можете повторить сцены. Для мечтания, выберите \"Сон\" в комнате [n.say_name]."

    $ dream_intro_shown = True
    $ player_character.reset_appearance(show_bust = False)

    call sleep_transition

    call day_next_day

    return