init python:
    wholesome_mode = False
    def set_settings():
        store.use_namebox = False
        
        store.video_sharing_site = "ReflexViz.HD"
        store.video_sharing_site_simone_wrong = "RejectViz.SV"
        
        store.config.context_clear_layers.append('characters')
        store.config.default_text_cps = 65
        
        store.add_relationship_points_appear_time = 5.0
        store.add_boldness_points_appear_time = 5.0
        
        store.add_relationship_points_sound = "1_Relationship.Boldness.wav"
        store.add_boldness_points_sound = "1_Relationship.Boldness.wav"
        store.add_relationship_boldness_points_sound = "1_Relationship.Boldness.wav"
        
        
        store.add_relationship_boldness_points_yalign = 0.35
        
        store.relationship_level_up_sound = "Level_Up.wav"
        store.boldness_level_up_sound = "Level_Up.wav"
        store.relationship_boldness_level_up_sound = "Level_Up.wav"
        
        store.config.has_autosave = False
        store.config.autosave_on_quit = False
        store.config.autosave_on_choice = False
        store.config.autosave_slots = 0
        
        store.popup_delay = 0.25
        store.popup_fadein_time = 0.5
        store.popup_fadeout_time = 0.75
        
        store.navigation_location_row_num = 5
        
        store.show_next_music_track_textbutton = True
        store.next_music_track_text = "Следующий трек"
        
        store.patreon_logo_filename = "images/buttons/downloads_wordmark_white_on_coral.png"
        store.patreon_logo_focused_text = "Sex Curse\nPatreon"
        store.patreon_logo_url = "http://www.patreon.com/sexcurse"
        
        store.show_money_on_hud = True
        
        store.music_queue_enabled = True
        
        store.boldness_name = "Смелость"
        
        store.back_button_filename = "images/buttons/back_button.png"
        
        store.allow_new_game_plus = False
        store.new_game_plus_mode = False
        
        store.show_sfw_option = True
        
        store.char_select_darken_on_hover = False
        
        store.char_menu_char_position = 'left'
        store.center_position_xscale = 1.0
        store.character_select_xscale = -1.0
        
        store.display_new_game_plus_option = True
        store.dreams_enabled = True
        
        return

    set_settings()

init:
    define config.log = "IALog.txt"