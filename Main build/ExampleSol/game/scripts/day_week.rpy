init -100 python:
    def school_has_started():
        return store.week.days_of_school_passed > 0 or store.week.is_school_day()

    class Week(object):
        def __init__(self):
            self.day = 1
            self.days_passed = 0
            
            
            
            
            self.days_of_school_passed = 0
            self.weeks_passed = 0
            self.time = "day"
            self.characters_had_scene_with_today = set()
        
        def daytime_named(self):
            return "Daytime"
        
        def evening_named(self):
            return "Evening"
        
        def time_named(self):
            if self.time == "day":
                if store.is_school_time:
                    return "Morning"
                elif store.is_school_day:
                    return "After School"
                else:
                    return self.daytime_named()
            
            if self.time == "night":
                return self.evening_named()
        
        def time_named_for_images(self):
            if self.time == "day":
                return self.daytime_named()
            
            return self.evening_named()
        
        def day_named(self):
            if self.day == 1:
                return "Понедельник" 
            if self.day == 2:
                return "Вторник" 
            if self.day == 3:
                return "Среда" 
            if self.day == 4:
                return "Четверг" 
            if self.day == 5:
                return "Пятница" 
            if self.day == 6:
                return "Суббота"
            else:
                return "Воскресенье"
        
        def is_school_day(self):
            return started_school and self.day < 6
        
        def day_named_lower_case(self):
            return self.day_named().lower()
        
        def advance_to_next_day(self):
            self.characters_had_scene_with_today = set()
            self.day += 1
            self.days_passed += 1
            
            if self.day > 7:
                self.weeks_passed += 1
                self.day = 1

label day_next_day:
    $ scenes_completed_today = set()
    $ new_scenes_completed_today = set()
    $ conversations_completed_today = set()
    $ new_conversations_completed_today = set()
    $ priority_conversation_completed_today = False
    $ quick_menu = True
    $ week.advance_to_next_day()
    $ renpy.set_return_stack([])

    call day_start
    return

label reset_locations:
    python hide:
        locations = location_list()

        for location in locations:
            location.reset()

    return

label place_characters:
    python hide:
        chars = npc_list()
        for char in chars:
            char.reset()

    return

label day_dream:
    python:
        choice_list = []

        dream_chars = npc_list()
        for dream_char in dream_chars:
            if dreams_enabled and len(dream_char.replayable_scenes) > 0:
                choice_list.append( ("Сон о " + dream_char.say_name, dream_char.variable_name) )

        if "finale_scene" in scenes_completed:
            choice_list.append( ("Сон о вечеринке у бассейна ", "finale_scene") )

        choice_list.append( ("Назад", "back") )

        chosen_option = renpy.display_menu(choice_list)

    if chosen_option == "back":
        call day_manual_sleep
    elif chosen_option == "finale_scene":
        python hide:
            if not persistent.disable_dream_music:
                music_name = "Dreamland.ogg" if random.randint(1, 2) == 1 else "Dreamland_02.ogg"
                music_name = "audio/music/" + music_name
                
                play_music(music_name, fadeout = 1.0)
            renpy.call(chosen_option + "_sex", dream = True)
    else:
        call character_dream_menu (eval(chosen_option))

    return

label day_manual_sleep:
    python hide:
        choice_list = []
        sleep_callback = "sleep_early"


        sleep_string = "Спать до "
        if store.week.time == "day":
            sleep_string += "вечера"
        else:
            sleep_string += "утра"
            sleep_callback = "day_advance_time"

        choice_list.append( (sleep_string, sleep_callback) )

        if store.replay_scenes_unlocked:
            choice_list = add_dream_option(choice_list)

        choice_list.append( ("Назад", "back") )

        chosen_option = renpy.display_menu(choice_list)

        if chosen_option == "back":
            advance_time_return_location.empty_action()
        else:
            renpy.call(chosen_option)

    return

label day_start:
    $ clear_characters(Dissolve(0.3))
    python:
        stats.current_zone = advance_time_return_location.zone()
        stats.current_location = advance_time_return_location
        week.time = "day"

    call day_start_before_location_reset

    call day_reset_locations_chars

    call day_start_after_location_reset

    return

label night_start:
    python:
        stats.current_zone = advance_time_return_location.zone()
        stats.current_location = advance_time_return_location
        week.time = "night"

    call day_reset_locations_chars

    python:
        advance_time_return_location.start(force_music_change = True)

    return

label sleep_transition:
    call sleep_lines

    call sleep_transition_effect
    return

label sleep_transition_effect:
    $ stop_music(fadeout = 1.0)
    $ renpy.scene('screens')
    call fade_to_black (0.5, do_not_show_quick_menu=False)

    return

label day_sleep(force_bg_change=False):
    call process_new_location (advance_time_return_location, keep_screens=True, force_bg_change=force_bg_change)
    call day_sleep_special_events
    $ player_character.reset_appearance(show_bust = False)

    call sleep_transition

    call day_next_day

    return

label day_reset_locations_chars:
    call reset_locations
    call place_characters

    return

label sleep_early:
    call sleep_transition

    call day_advance_time

    return

label day_advance_time(force_bg_change=False):
    python:
        fix_anim_log_error()
        renpy.scene('screens')
        clear_characters()
        quick_menu = True
        enable_saving()
        enable_rollback()
        advance_time_reinitializations()

    if week.time == "day":
        call night_start
    if week.time == "night":
        call day_sleep (force_bg_change=force_bg_change)

    return