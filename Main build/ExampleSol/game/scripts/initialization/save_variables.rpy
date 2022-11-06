init python:
    def initialize_variables(force_reinitialization = False):
        initialization_variables = []
        
        
        initialization_variables.append( Save_Variable( "epilogue_completed" , "False" ) ) 
        initialization_variables.append( Save_Variable( "epilogue_pregnancy_completed" , "False" ) ) 
        
        initialization_variables.append( Save_Variable( "has_fucked_everyone_in_home" , "False" ) ) 
        
        initialization_variables.append( Save_Variable( "finale_scene_completed_with_julia_sam" , "False" ) )
        
        
        initialization_variables.append( Save_Variable("no_bust_art" , "False" ) )
        initialization_variables.append( Save_Variable( "one_time_set_variable_tags" , "set()" ) )
        initialization_variables.append( Save_Variable( "last_character_that_appeared" , "\"\"" ) )
        initialization_variables.append( Save_Variable( "characters_shown" , "set()" ) )
        initialization_variables.append( Save_Variable( "current_background" , "\"\"" ) )
        initialization_variables.append( Save_Variable( "last_say_position" , "\"\"" ) )
        initialization_variables.append( Save_Variable( "game_seed" , "random.randint(999, 9999)" ) )
        
        
        initialization_variables.append( Save_Variable( "countdown_length" , "0" ) )
        initialization_variables.append( Save_Variable( "countdown_remaining" , "0" ) )
        initialization_variables.append( Save_Variable( "countdown_elapsed" , "0" ) )
        initialization_variables.append( Save_Variable( "countdown_addend" , "0" ) )
        initialization_variables.append( Save_Variable( "countdown_red_text" , "True" ) )
        initialization_variables.append( Save_Variable( "countdown_show_decimal" , "True" ) )
        initialization_variables.append( Save_Variable( "minigames_tried" , "set()" ) ) 
        initialization_variables.append( Save_Variable( "minigames_done" , "0" ) ) 
        initialization_variables.append( Save_Variable( "minigame_typing_review_started" , "False" ) ) 
        initialization_variables.append( Save_Variable( "minigame_typing_review_countdown_addend" , "0" ) ) 
        initialization_variables.append( Save_Variable( "minigame_racing_forced_nate_face" , "None" ) ) 
        initialization_variables.append( Save_Variable( "minigame_racing_forced_kira_face" , "None" ) ) 
        initialization_variables.append( Save_Variable( "minigame_sliding_puzzle_sam_intro_done" , "False" ) ) 
        initialization_variables.append( Save_Variable( "minigame_typing_times_succeeded" , "0" ) ) 
        initialization_variables.append( Save_Variable( "minigame_typing_money_earned" , "0" ) )
        initialization_variables.append( Save_Variable( "minigame_typing_money_earned_since_last_vicky_meeting" , "0" ) )
        initialization_variables.append( Save_Variable( "minigame_typing_times_succeeded_since_last_vicky_meeting" , "0" ) ) 
        
        
        initialization_variables.append( Save_Variable( "last_name" , "\"Williams\"" ) )
        
        
        initialization_variables.append( Save_Variable( "last_selected_character" , "None" ) )
        initialization_variables.append( Save_Variable( "entered_outside" , "False" ) )
        
        
        initialization_variables.append( Save_Variable( "started_main_game" , "False" ) )
        initialization_variables.append( Save_Variable( "week" , "Week()" ) )
        
        
        initialization_variables.append( Save_Variable( "stats" , "IA_Stats()" ) )
        initialization_variables.append( Save_Variable( "scenes_completed" , "set()" ) )
        initialization_variables.append( Save_Variable( "scenes_completed_for_stats" , "set()" ) )
        initialization_variables.append( Save_Variable( "scenes_completed_today" , "set()" ) )
        initialization_variables.append( Save_Variable( "new_scenes_completed_today" , "set()" ) )
        initialization_variables.append( Save_Variable( "conversations_completed_today" , "set()" ) )
        initialization_variables.append( Save_Variable( "new_conversations_completed_today" , "set()" ) )
        initialization_variables.append( Save_Variable( "priority_conversation_completed_today" , "False" ) )
        
        
        initialization_variables.append( Save_Variable( "home" , "Home()" ) )
        initialization_variables.append( Save_Variable( "nate_room" , "Nate_Room()" ) )
        initialization_variables.append( Save_Variable( "kira_room" , "Kira_Room()" ) )
        initialization_variables.append( Save_Variable( "simone_room" , "Simone_Room()" ) )
        initialization_variables.append( Save_Variable( "sam_room" , "Sam_Room()" ) )
        initialization_variables.append( Save_Variable( "kitchen" , "Kitchen()" ) )
        initialization_variables.append( Save_Variable( "bathroom" , "Bathroom()" ) )
        initialization_variables.append( Save_Variable( "backyard" , "Backyard()" ) )
        initialization_variables.append( Save_Variable( "hallway" , "Hallway()" ) )
        initialization_variables.append( Save_Variable( "living_room" , "Living_Room()" ) )
        
        initialization_variables.append( Save_Variable( "school_start_activation" , "School_Start_Activation()" ) )
        
        
        initialization_variables.append( Save_Variable( "k" , "Kira()" ) )
        initialization_variables.append( Save_Variable( "si" , "Simone()" ) )
        initialization_variables.append( Save_Variable( "sa" , "Sam()" ) )
        initialization_variables.append( Save_Variable( "debug_character" , "Debug_Character()" ) )
        initialization_variables.append( Save_Variable( "gloryhole_girl" , "Gloryhole_Girl()" ) )
        initialization_variables.append( Save_Variable( "julia" , "Julia()" ) )
        initialization_variables.append( Save_Variable( "vicky" , "Vicky()" ) )
        initialization_variables.append( Save_Variable( "janet" , "Janet()" ) )
        initialization_variables.append( Save_Variable( "n" , "Nate()" ) )
        initialization_variables.append( Save_Variable( "edna" , "Edna()" ) )
        
        
        
        initialization_variables.append( Save_Variable( "player_character" , "n" ) )
        initialization_variables.append( Save_Variable( "nate2" , "Nate2()" ) )
        initialization_variables.append( Save_Variable( "nate3" , "Nate3()" ) )
        
        
        
        initialization_variables.append( Save_Variable( "started_school" , "False" ) )
        initialization_variables.append( Save_Variable( "is_school_time" , "False" ) )
        initialization_variables.append( Save_Variable( "is_school_day" , "False" ) )
        
        
        
        initialization_variables.append( Save_Variable( "general_replayable_scenes" , "set()" ) )
        initialization_variables.append( Save_Variable( "replay_scenes_unlocked" , "False" ) )
        initialization_variables.append( Save_Variable( "dream_intro_shown" , "False" ) )
        initialization_variables.append( Save_Variable( "dreams_had" , "0" ) )
        
        
        initialization_variables.append( Save_Variable( "animation_infos" , "{}" ) )
        initialization_variables.append( Save_Variable( "animation_displayables" , "{}" ) )
        
        
        initialization_variables.append( Save_Variable( "last_queued_music" , "None" ) )
        initialization_variables.append( Save_Variable( "current_queued_music" , "None" ) )
        initialization_variables.append( Save_Variable( "faded_out_audio" , "False" ) )
        initialization_variables.append( Save_Variable( "music_is_queued" , "False" ) )
        initialization_variables.append( Save_Variable( "music_playlist" , "[]" ) )
        
        
        initialization_variables.append( Save_Variable( "inventory" , "Inventory()" ) )
        initialization_variables.append( Save_Variable( "replace_position" , "False" ) )
        initialization_variables.append( Save_Variable( "name_input_color" , "gui.accent_color" ) )
        initialization_variables.append( Save_Variable( "disable_saves" , "False" ) ) 
        initialization_variables.append( Save_Variable( "rollback_enabled" , "True" ) ) 
        initialization_variables.append( Save_Variable( "heard_of_ejaculate" , "False" ) ) 
        initialization_variables.append( Save_Variable( "heard_of_horny" , "False" ) ) 
        initialization_variables.append( Save_Variable( "heard_of_boner" , "False" ) ) 
        initialization_variables.append( Save_Variable( "heard_of_handjob" , "False" ) ) 
        initialization_variables.append( Save_Variable( "heard_of_blowjob" , "False" ) ) 
        initialization_variables.append( Save_Variable( "heard_of_anal" , "False" ) ) 
        
        
        initialization_variables.append( Save_Variable( "kira_scene_2_revisit_wanted_to_see_up_close" , "False" ) ) 
        initialization_variables.append( Save_Variable( "kira_3_ready_hot_dog_xray_on" , "False" ) ) 
        initialization_variables.append( Save_Variable( "kira_3_had_slow_speed_message" , "False" ) ) 
        initialization_variables.append( Save_Variable( "kira_3_had_normal_speed_message" , "False" ) ) 
        initialization_variables.append( Save_Variable( "kira_3_had_fast_speed_message" , "False" ) ) 
        initialization_variables.append( Save_Variable( "kira_3_single_smack_sound" , "False" ) ) 
        initialization_variables.append( Save_Variable( "play_sex_sounds" , "True" ) ) 
        initialization_variables.append( Save_Variable( "main_animation_speed" , "1.0" ) ) 
        
        initialization_variables.append( Save_Variable( "kira_titfuck_had_slow_speed_message" , "False" ) ) 
        initialization_variables.append( Save_Variable( "kira_titfuck_had_normal_speed_message" , "False" ) ) 
        initialization_variables.append( Save_Variable( "kira_titfuck_had_fast_speed_message" , "False" ) ) 
        initialization_variables.append( Save_Variable( "gloryhole_handjob_xray_on" , "False" ) ) 
        initialization_variables.append( Save_Variable( "kira_anal_anim_pause" , "False" ) ) 
        initialization_variables.append( Save_Variable( "sam_scene_swimsuit_revisit_nude" , "False" ) ) 
        initialization_variables.append( Save_Variable( "had_julia_pre_arrival_scene" , "False" ) ) 
        initialization_variables.append( Save_Variable( "had_julia_arrived_scene" , "False" ) ) 
        initialization_variables.append( Save_Variable( "has_seen_aunt" , "False" ) ) 
        initialization_variables.append( Save_Variable( "had_vicky_pre_intro_scene" , "False" ) ) 
        initialization_variables.append( Save_Variable( "had_vicky_intro_scene" , "False" ) ) 
        initialization_variables.append( Save_Variable( "had_janet_intro_scene" , "False" ) ) 
        initialization_variables.append( Save_Variable( "janet_vicky_intro_scenes_timing_helper" , "False" ) ) 
        initialization_variables.append( Save_Variable( "did_sam_simone_ff" , "False" ) ) 
        initialization_variables.append( Save_Variable( "did_sam_julia_ff" , "False" ) ) 
        initialization_variables.append( Save_Variable( "had_edna_pre_arrival_scene" , "False" ) ) 
        initialization_variables.append( Save_Variable( "had_edna_intro_scene" , "False" ) ) 
        initialization_variables.append( Save_Variable( "kira_simone_threesome_part_2_done" , "False" ) ) 
        initialization_variables.append( Save_Variable( "kira_impreg" , "False" ) ) 
        initialization_variables.append( Save_Variable( "sam_impreg" , "False" ) ) 
        initialization_variables.append( Save_Variable( "simone_impreg" , "False" ) ) 
        initialization_variables.append( Save_Variable( "did_family_foursome_ff" , "False" ) ) 
        initialization_variables.append( Save_Variable( "family_foursome_revisit_current_partner" , "False" ) ) 
        initialization_variables.append( Save_Variable( "finale_julia_sam" , "False" ) )
        initialization_variables.append( Save_Variable( "finale_chose_edna" , "False" ) )
        initialization_variables.append( Save_Variable( "finale_chose_janet" , "False" ) )
        initialization_variables.append( Save_Variable( "finale_chose_julia" , "False" ) )
        initialization_variables.append( Save_Variable( "finale_chose_sam" , "False" ) )
        initialization_variables.append( Save_Variable( "finale_chose_kira" , "False" ) )
        initialization_variables.append( Save_Variable( "finale_chose_simone" , "False" ) )
        initialization_variables.append( Save_Variable( "finale_chose_kacey" , "False" ) )
        initialization_variables.append( Save_Variable( "finale_chose_vicky" , "False" ) )
        initialization_variables.append( Save_Variable( "finale_kacey_arrived" , "False" ) )
        initialization_variables.append( Save_Variable( "finale_vicky_arrived" , "False" ) )
        initialization_variables.append( Save_Variable( "finale_fucked_amount" , "0" ) )
        initialization_variables.append( Save_Variable( "finale_fucked_amount_goal" , "6" ) )
        initialization_variables.append( Save_Variable( "finale_cum_amount" , "0" ) )
        initialization_variables.append( Save_Variable( "finale_cum_amount_goal" , "6" ) )
        initialization_variables.append( Save_Variable( "edna_finale_positions_chosen" , "0" ) )
        initialization_variables.append( Save_Variable( "edna_finale_vaginal_chosen" , "False" ) )
        initialization_variables.append( Save_Variable( "edna_finale_vaginal_chosen_this_time" , "False" ) )
        initialization_variables.append( Save_Variable( "edna_finale_anal_chosen_this_time" , "False" ) )
        initialization_variables.append( Save_Variable( "edna_finale_analingus_chosen_this_time" , "False" ) )
        
        
        initialization_variables.append( Save_Variable( "outside" , "Outside()" ) )
        initialization_variables.append( Save_Variable( "video_game_store" , "Video_Game_Store()" ) )
        initialization_variables.append( Save_Variable( "fortune_teller" , "Fortune_Teller()" ) )
        initialization_variables.append( Save_Variable( "park" , "Park()" ) )
        initialization_variables.append( Save_Variable( "vicky_apartment" , "Vicky_Apartment()" ) )
        initialization_variables.append( Save_Variable( "janet_house" , "Janet_House()" ) )
        initialization_variables.append( Save_Variable( "edna_house" , "Edna_House()" ) )
        
        
        initialization_variables.append( Save_Variable( "school" , "School()" ) )
        initialization_variables.append( Save_Variable( "school_library" , "School_Library()" ) )
        initialization_variables.append( Save_Variable( "school_bathroom" , "School_Bathroom()" ) )
        initialization_variables.append( Save_Variable( "school_homeroom" , "School_Homeroom()" ) )
        
        initialization_variables.append( Save_Variable( "school_leave_door" , "School_Leave_Door()" ) )
        
        
        initialization_variables.append( Save_Variable( "grandma_house" , "Grandma_House()" ) )
        initialization_variables.append( Save_Variable( "grandma_house_guest_room" , "Grandma_House_Guest_Room()" ) )
        initialization_variables.append( Save_Variable( "grandma_house_bathroom" , "Grandma_House_Bathroom()" ) )
        
        
        
        initialization_variables.append( Save_Variable( "advance_time_return_location" , "nate_room" ) )
        
        initialize_variables_utility(initialization_variables, force_reinitialization = force_reinitialization)
        
        return