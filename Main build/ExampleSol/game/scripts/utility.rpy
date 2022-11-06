init python:
    def set_temp_popup_window_text_line(trans, st, at):
        if len(store.temp_popup_window_text_lines) <= 0:
            if store.temp_popup_window_text_repeat:
                store.temp_popup_window_text_lines = eval(store.temp_popup_window_text_eval)
            else:
                store.temp_popup_window_text_line = None
                return None
        
        store.temp_popup_window_text_line = store.temp_popup_window_text_lines.pop(0)
        
        return None

    def temp_window_text_popup_displayable_line_cycler(min_width = 500, max_width = 500, min_height = None, max_height = None, xpos = 0, ypos = 0, xalign = 0.0, yalign = 0.0):
        return temp_window_text_popup_displayable(store.temp_popup_window_text_line, min_width = min_width, max_width = max_width, min_height = min_height, max_height = max_height, xpos = xpos, ypos = ypos, xalign = xalign, yalign = yalign)

    def temp_window_text_popup_displayable(line_obj, min_width = 500, max_width = 500, min_height = None, max_height = None, xpos = 0, ypos = 0, xalign = 0.0, yalign = 0.0):
        if not line_obj:
            return Null()
        
        window_width = 0
        
        name_text_y = 14
        name_text_xpos = 12
        body_text_padding = 20
        body_text_xpos = name_text_xpos + body_text_padding
        
        if max_width:
            text_width = max_width
        elif min_width:
            text_width = 1920
        else:
            text_width = 500
        text_width = text_width - (body_text_padding * 2)
        
        window_height = 97
        
        dummy_text_render = renpy.render( Text( line_obj["text"], size = 33, xsize = text_width, xmaximum = text_width ), 1920, 1080, 0, 0 )
        dummy_width = dummy_text_render.width
        dummy_height = dummy_text_render.height
        
        window_width = body_text_xpos + int(dummy_width) + body_text_xpos
        if min_width:
            window_width = max(window_width, min_width)
        if max_width:
            window_width = min(window_width, max_width)
        
        window_height = window_height + (int(dummy_height) - 6)
        if min_height:
            window_height = max(window_height, min_height)
        if max_height:
            window_height = min(window_height, max_height)
        
        window = Frame(Image("gui/textbox.png"), left = 12, top = 12, right = 12, bottom = 12, xsize = window_width, ysize = window_height) 
        name_text = Text(line_obj["char"].name_string_with_text(), xpos = name_text_xpos, ypos = name_text_y, size = 45)
        
        body_text = Text(line_obj["text"], xpos = body_text_xpos, ypos = 69, size = 33)
        
        fixed = Fixed(window, name_text, body_text, xysize = (window_width, window_height))
        
        return At(fixed, temp_popup_window_text_trans(xpos = xpos, ypos = ypos, xalign = xalign, yalign = yalign))

    def enable_rollback():
        config.rollback_enabled = True
        store.rollback_enabled = True
        return

    def disable_rollback():
        config.rollback_enabled = False
        store.rollback_enabled = False
        return

    def face_equalities(char, face):
        face = char.face_adjustment(face)
        face = face_equalities_special(char, face)
        
        return face

    def daily_random_event_seed(tag):
        return hash( str(store.game_seed) + str(store.week.day) + store.week.time + tag )


    def daily_random_event_coin_toss(tag):
        return daily_random_event_percentage_test(tag, 50)

    def daily_random_event_percentage_test(tag, chance):
        seed = daily_random_event_seed(tag)
        
        random.seed(seed)
        
        value = True if random.randint(1, 100) <= chance else False
        
        
        random.seed()
        
        return value

    def reset_all_characters():
        chars = character_list()
        for char in chars:
            char.reset_appearance(show_bust = False)
        
        return

    def display_multiple_characters(array, reset = False):
        for tuple in array:
            char = tuple[0]
            if reset:
                char.reset_appearance(show_bust = False)
            process_character(char, tuple[1], show_bust = False)
            refresh_character(char, force_no_dissolve = True)
        
        renpy.with_statement(character_dissolve)
        
        return

    def bust_art_background(name, dream = False):
        store.no_bust_art = False
        change_background(name, dream = dream)
        
        return

    def change_background(name, show_dissolve = True, dream = False):
        if persistent.sfw_mode and name != "bg black":
            screen_text = name
            if isinstance(name, Location):
                screen_text = name.background()
            
            name = store.advance_time_return_location
            
            renpy.show_screen("sfw_mode_background_display", screen_text)
        else:
            renpy.hide_screen("sfw_mode_background_display")
        
        if isinstance(name, Location):
            name = name.background()
        
        renpy.scene()
        renpy.show(name)
        
        if dream and not persistent.disable_dream_blur:
            renpy.show_screen("dream_blur")
        
        if show_dissolve:
            if name != store.current_background:
                renpy.with_statement(Dissolve(background_dissolve_speed))
        
        store.current_background = name
        
        return

    def clear_characters(dissolve = None):
        store.characters_shown = set()
        renpy.scene(character_layer())
        
        if dissolve:
            renpy.with_statement(dissolve)
        
        return

    def process_character_replace_utility(char, appearance = "", text = "", show_bust = True, replace = False):
        if replace and store.last_character_that_appeared and store.last_character_that_appeared != char.variable_name:
            character_leave_dissolve(eval(store.last_character_that_appeared))
        
        if appearance and show_bust:
            store.last_character_that_appeared = char.variable_name
        
        process_character(char, appearance, show_bust = show_bust)
        
        if text:
            store.last_say_position = char.position
            char.c(text)
        
        return

    def process_character(char, process_string, show_bust = True):
        should_refresh = False
        changed_something_other_than_exp = False
        force_no_dissolve = False
        
        string_split = process_string.split(" ")
        
        for i in range(len(string_split)):
            split = string_split[i]
            
            if i + 1 < len(string_split):
                next = string_split[i + 1]
            
            if split == "face":
                i = i + 1
                new_face = next
                
                new_face = face_equalities(char, new_face)
                
                if char.face != new_face:
                    should_refresh = True
                
                char.face = new_face
            if split == "pose":
                i = i + 1
                new_pose = next
                
                new_pose = char.pose_adjustment(new_pose)
                
                if char.pose != new_pose:
                    changed_something_other_than_exp = True
                    should_refresh = True
                
                char.pose = new_pose
            elif split == "blush":
                i = i + 1
                
                if next == "true":
                    new_blush_setting = True
                else:
                    new_blush_setting = False
                
                if char.blush != new_blush_setting:
                    changed_something_other_than_exp = True
                    should_refresh = True
                
                char.blush = new_blush_setting
            elif split == "position":
                i = i + 1
                new_position = next
                
                if char.position != new_position:
                    changed_something_other_than_exp = True
                    should_refresh = True 
                
                char.position = new_position
            elif split == "outfit":
                
                i = i + 1
                
                new_outfit = next
                new_outfit = char.outfit_adjustment(new_outfit)
                
                if persistent.sfw_mode:
                    char.non_sfw_outfit = new_outfit
                    new_outfit = char.sfw_outfit()
                
                
                if char.outfit != new_outfit:
                    changed_something_other_than_exp = True
                    should_refresh = True
                
                char.outfit = new_outfit
            elif split == "mouth":
                
                i = i + 1
                
                new_mouth = next
                
                if char.mouth != new_mouth:
                    changed_something_other_than_exp = True
                    should_refresh = True
                
                char.mouth = new_mouth
            elif split == "hat":
                
                i = i + 1
                
                new_hat = next
                
                if char.hat != new_hat:
                    changed_something_other_than_exp = True
                    should_refresh = True
                
                char.hat = new_hat
            elif split == "overlay":
                i = i + 1
                
                new_overlay = next
                old_overlay_size = len(char.overlays)
                char.overlays.add(new_overlay)
                
                if old_overlay_size != len(char.overlays):
                    changed_something_other_than_exp = True
                    should_refresh = True
            elif split == "overlay_remove":
                i = i + 1
                
                overlay_to_remove = next
                old_overlay_size = len(char.overlays)
                char.overlays.remove(overlay_to_remove)
                
                if old_overlay_size != len(char.overlays):
                    changed_something_other_than_exp = True
                    should_refresh = True
        
        char.fix_appearance()
        
        if process_string and char.variable_name in characters_shown and not changed_something_other_than_exp:
            force_no_dissolve = True
        
        if process_string and show_bust:
            refresh_character(char, force_no_dissolve = force_no_dissolve)
        
        return

    def character_leave_dissolve(char):
        base_tag = char.base_tag()
        face_tag = char.face_tag()
        blush_tag = char.blush_tag()
        char_layer = character_layer()
        
        renpy.hide(base_tag, char_layer)
        renpy.hide(face_tag, char_layer)
        renpy.hide(blush_tag, char_layer)
        
        if char.has_separate_mouth():
            renpy.hide(char.mouth_tag(), char_layer)
        
        
        renpy.hide(char.hat_tag(), char_layer)
        
        
        renpy.with_statement(character_leave_dissolve_speed)
        store.characters_shown.discard(char.variable_name)
        
        return

    def refresh_character(char, off_screen = False, on_screen = False, force_no_dissolve = False, force_transition = None):
        if wholesome_mode:
            return
        
        if no_bust_art:
            return
        
        transition = force_transition
        if not force_transition:    
            transition = character_dissolve
        
        if not off_screen:
            store.characters_shown.add(char.variable_name)
        
        transform_array = []
        
        x_destination = 0.0
        
        position = char.position
        y_pos = char.ypos_adjustment()
        y_scale = 1.0
        
        base_tag = char.base_tag()
        face_tag = char.face_tag()
        blush_tag = char.blush_tag()
        
        base_string = char.base_image_filename()
        face_string = char.face_image_filename()
        blush_string = char.blush_image_filename()
        
        layer = character_layer()
        
        x_scale = -1.0
        x_align = 0.0
        x_destination = -1.0
        
        if position == "left":
            x_scale = -1.0
            x_align = 0.0
            x_destination = -1.0
        elif position == "left_mirror":
            x_scale = 1.0
            x_align = 0.0
            x_destination = -1.0
        elif position == "right":
            x_scale = 1.0
            x_align = 1.0
            x_destination = 2.0
        elif position == "right_mirror":
            x_scale = -1.0
            x_align = 1.0
            x_destination = 2.0
        elif position == "center":
            x_scale = store.center_position_xscale
            x_align = 0.5
            x_destination = -1.0
        elif position == "janet_special":
            x_scale = -1.0
            x_align = 0.81
            y_align = 1.5
            x_destination = 2.0
            y_pos = 545
        elif position == "edna_special":
            x_scale = -1.0
            x_align = 0.88
            x_destination = 2.0
            y_pos = 520
        elif position == "edna_special2":
            x_scale = -1.0
            x_align = 0.87
            x_destination = 2.0
        elif position == "edna_special3":
            x_scale = -1.0
            x_align = 1.0
            x_destination = 2.0
            y_pos = 520
        elif position == "nate_more_right":
            x_scale = 1.0
            x_align = 1.12
            x_destination = 2.0
        elif position == "nate2_special":
            x_scale = -1.0
            x_align = -0.16
            x_destination = -1.0
        elif position == "nate3_special":
            x_scale = -1.0
            x_align = -0.03
            x_destination = -1.0
        elif position == "sam_dream_special":
            x_scale = -1.0
            x_align = 0.1
            x_destination = -1.0
        elif position == "nate_simone_tit_level_nate":
            x_scale = 1.0
            x_align = 0.15
            x_destination = -1.0
            y_pos = 100
        elif position == "nate_simone_tit_level_simone":
            x_scale = -1.0
            x_align = -0.1
            x_destination = -1.0
        elif position == "nate_edna_pussy_level_edna":
            x_scale = -1.0
            x_align = -0.08
            x_destination = -1.0
        elif position == "nate_edna_pussy_level_nate":
            x_scale = 1.0
            x_align = 0.11
            x_destination = -1.0
            y_pos = 340
        elif position == "julia_sam_threesome_closer_sam":
            x_scale = -1.0
            x_align = 0.83
            x_destination = 2.0
        elif position == "julia_sam_threesome_closer_julia":
            x_scale = -1.0
            x_align = 0.67
            x_destination = 2.0
        elif position == "three_person_left_2":
            x_scale = -1.0
            x_align = 0.3
        elif position == "three_person_left_3":
            x_scale = -1.0
            x_align = 0.6
        
        
        transform_array.append( Transform(xalign = x_align, xzoom = x_scale, ypos = y_pos, yzoom = y_scale) )
        
        if off_screen:
            transform_array.append( Move( (x_align, 0.0), (x_destination, 0.0), character_slide_speed ) )
        if on_screen:
            transform_array.append( Move( (x_destination, 0.0), (x_align, 0.0), character_slide_speed ) )
        
        if not char.show_face_under_base():
            renpy.show(base_string, transform_array, layer, None, 0, base_tag)
            renpy.show(blush_string, transform_array, layer, None, 0, blush_tag)
            renpy.show(face_string, transform_array, layer, None, 0, face_tag)
            if char.has_separate_mouth():
                renpy.show(char.mouth_image_filename(), transform_array, layer, None, 0, char.mouth_tag())
            if char.has_separate_hat():
                renpy.show(char.hat_image_filename(), transform_array, layer, None, 0, char.hat_tag())
        else:
            renpy.show(face_string, transform_array, layer, None, 0, face_tag)
            renpy.show(blush_string, transform_array, layer, None, 0, blush_tag)
            renpy.show(base_string, transform_array, layer, None, 0, base_tag)
        
        
        
        for overlay_image_name in char.displayed_overlay_filenames:
            renpy.show("invisible_char_part", transform_array, layer, None, 0, overlay_image_name)
            char.reset_displayed_overlay_filenames()
        
        for overlay_name in char.overlays:
            overlay_image_name = char.overlay_image_filename(overlay_name)
            char.displayed_overlay_filenames.add(overlay_image_name)
            renpy.show(overlay_image_name, transform_array, layer, None, 0, overlay_image_name)
        
        if not force_no_dissolve:
            renpy.with_statement(transition)
        
        if persistent.sfw_mode:
            renpy.show_screen("sfw_mode_character_display")
        else:
            renpy.hide_screen("sfw_mode_character_display")
        
        return

    def add_points_and_boldness(char, relationship_points, boldness_points, tag = None, force_no_popup = False, minigame = False, yalign = add_relationship_boldness_points_yalign):
        if tag and tag in store.stats.add_boldness_or_relationship_tags:
            return
        
        if tag:
            store.stats.add_boldness_or_relationship_tags.append(tag)
        
        appear_time = 0
        sound = add_relationship_boldness_points_sound
        
        relationship_array = char.add_points(relationship_points, force_no_popup = True, minigame = minigame)
        text = relationship_array[0]
        rel_leveled_up = relationship_array[1]
        appear_time += relationship_array[2]
        
        text += "\n"
        if rel_leveled_up:
            text += "\n"
        
        boldness_array = store.stats.add_boldness_xp(boldness_points, force_no_popup = True, minigame = minigame, yalign = yalign)
        text += boldness_array[0]
        boldness_leveled_up = boldness_array[1]
        appear_time += boldness_array[2]
        
        if rel_leveled_up or boldness_leveled_up:
            sound = relationship_boldness_level_up_sound
        
        if not force_no_popup:
            renpy.hide_screen("pop_up_general")
            renpy.show_screen("pop_up_general", text, sound, appear_time)
        
        return appear_time

transform temp_popup_window_text_trans(xpos=0, ypos=0, xalign=0.0, yalign=0.0):
    xpos xpos
    ypos ypos
    xalign xalign
    yalign yalign

    alpha 0.0
    pause 6.0
    block:

        alpha 0.0
        linear .5 alpha 1.0


        pause 3.0

        linear .5 alpha 0.0

        function set_temp_popup_window_text_line

        pause 6.0

        repeat

screen sfw_mode_background_display(text):
    add text zoom 0.1 xalign 0.5 yalign 0.5
    text "background: " + text

screen sfw_mode_character_display:
    vbox:
        xalign 0.5
        yalign 0.05
        text "Characters: "
        vbox:
            for sfw_mode_display_shown_character in store.characters_shown:

                if getattr(eval(sfw_mode_display_shown_character), 'non_sfw_outfit', False):
                    text "Name: " + eval(sfw_mode_display_shown_character).say_name + ", Outfit: " + eval(sfw_mode_display_shown_character).non_sfw_outfit
                else:
                    text "Name: " + eval(sfw_mode_display_shown_character).say_name + ", Outfit: " + eval(sfw_mode_display_shown_character).outfit

screen progress_button_screen(text="", xalign=0.97, yalign=0.55):
    use main_menu_button(text=text, action=Return(value = None), xalign=xalign, yalign=yalign )

screen temp_window_text_popup_screen(xpos=0, ypos=0, xalign=0.0, yalign=0.0, min_width=500, max_width=500):
    add temp_window_text_popup_displayable_line_cycler(xpos = xpos, ypos = ypos, xalign = xalign, yalign = yalign, min_width = min_width, max_width = max_width)

screen temp_window_text_popup_screen_one_off(line_obj, xpos=0, ypos=0, xalign=0.0, yalign=0.0, min_width=500, max_width=500):
    add temp_window_text_popup_displayable(line_obj, xpos = xpos, ypos = ypos, xalign = xalign, yalign = yalign, min_width = min_width, max_width = max_width)

label show_temp_window_text_popup(show_temp_window_text_popup_reset_array_eval, xpos=0, ypos=0, xalign=0.0, yalign=0.0, min_width=500, max_width=500, repeat=False):
    $ store.temp_popup_window_text_eval = show_temp_window_text_popup_reset_array_eval
    $ store.temp_popup_window_text_lines = eval(store.temp_popup_window_text_eval)
    $ store.temp_popup_window_text_line = store.temp_popup_window_text_lines.pop(0)
    $ store.temp_popup_window_text_repeat = repeat

    show screen temp_window_text_popup_screen(xpos = xpos, ypos = ypos, xalign = xalign, yalign = yalign, min_width = min_width, max_width = max_width)
    return

label prompt_menu_boldness_check(yes_text, no_text, scene_name, boldness_char):
    if boldness_char.meets_boldness_requirement_for_scene(scene_name):
        if boldness_char.boldness_level_required_for_scene(scene_name) > 0:
            $ n.c("(Я чувствую себя {b}достаточно смелым{/b} для этого!)")

        window hide
        menu:
            "[yes_text]":
                $ renpy.call(scene_name + "_sex")
            "[no_text]":
                $ renpy.call(scene_name + "_refusal", no_text, False)
    else:
        $ renpy.call(scene_name + "_refusal", no_text, True)

    return

label prompt_refusal_end(char):
    if started_main_game:
        $ char.display_menu()
    else:
        call debug_menu

    return

label process_conversation_beginning(char_tuple_array):
    $ renpy.scene('screens')
    call reset_all_characters
    $ display_multiple_characters(char_tuple_array)

    return

label process_end_of_conversation(conversation_name, char, default=False, priority=False, considered_scene=False, override_scene_limit=False):
    if not default:
        $ char.conversations_completed.add(conversation_name)
        $ char.recently_completed_conversations.add(conversation_name)

        $ conversations_completed_today.add(conversation_name)
        if conversation_name not in char.conversations_completed:
            $ new_conversations_completed_today.add(conversation_name)

    if priority:
        $ priority_conversation_completed_today = True
        $ char.set_conversation()

    if considered_scene:
        python:
            char.scene = ""
            if not override_scene_limit:
                week.characters_had_scene_with_today.add(char)

    if started_main_game:
        $ char.display_menu()
    else:
        call debug_menu

    return

label process_scene_beginning(bg=False, bust_art=True, ctc=True, char_tuple_array=[], image_predict_array=[], force_bg_change=False, dream=False):
    window hide
    python hide:
        for image in image_predict_array:
            renpy.start_predict(image)

    call process_new_location (bg=bg, bust_art=bust_art, ctc=ctc, char_tuple_array=char_tuple_array, force_bg_change=force_bg_change, dream=dream)

    call process_scene_beginning_add_on (dream=dream)

    return

label process_new_location(bg=False, bust_art=True, ctc=True, char_tuple_array=[], force_bg_change=False, keep_screens=False, dream=False):
    if not keep_screens:
        $ renpy.scene('screens')
    $ should_do_bg_change = True

    if bg and not force_bg_change:
        if isinstance(bg, Location) and bg.background() == store.current_background:
            $ should_do_bg_change = False

    window hide
    call clear_and_reset_characters

    if bg and should_do_bg_change:
        call fade_to_black (0.5)

        if bust_art:
            call bust_art_background (bg, dream=dream)
        else:
            call static_still_ctc (bg, dream=dream)

        $ renpy.pause(0.25)
    elif dream and not persistent.disable_dream_blur:
        show screen dream_blur


    if char_tuple_array:
        call display_multiple_characters (char_tuple_array)

    if bg:
        $ renpy.pause(0.25)

    return

label add_points_and_boldness(add_points_char, char_points, boldness_points, tag=None, delay=False, force_no_popup=False, clear_screens=False, minigame=False, yalign=add_relationship_boldness_points_yalign):
    $ wait_obj = add_points_and_boldness(add_points_char, char_points, boldness_points, tag = tag, force_no_popup = force_no_popup, minigame = minigame, yalign = yalign)

    if wait_obj and delay:
        call add_points_boldness_delay_utility (wait_obj, not_array=True, clear_screens=clear_screens)

    return

label add_points_multiple_characters(characters, quantities, tag=None, delay=False, force_no_popup=False, clear_screens=False, minigame=False, yalign=add_relationship_boldness_points_yalign):
    if tag and tag in store.stats.add_boldness_or_relationship_tags:
        return

    if tag:
        $ store.stats.add_boldness_or_relationship_tags.append(tag)

    python hide:
        for i in range(0, len(characters)):
            character = characters[i]
            quantity = quantities[i]
            character.add_points(quantity, force_no_popup = force_no_popup, minigame = minigame, yalign = yalign)

    return

label add_points(add_points_char, quantity, tag=None, delay=False, force_no_popup=False, clear_screens=False, minigame=False, yalign=add_relationship_boldness_points_yalign):
    $ wait_obj = add_points_char.add_points(quantity, tag = tag, force_no_popup = force_no_popup, minigame = minigame, yalign = yalign)

    if wait_obj and delay:
        call add_points_boldness_delay_utility (wait_obj, clear_screens=clear_screens)

    return

label add_boldness(quantity, tag=None, delay=False, force_no_popup=False, clear_screens=False, minigame=False, yalign=add_relationship_boldness_points_yalign):
    $ wait_obj = stats.add_boldness_xp(quantity, tag = tag, force_no_popup = force_no_popup, minigame = minigame, yalign = yalign)

    if wait_obj and delay:
        call add_points_boldness_delay_utility (wait_obj, clear_screens=clear_screens)

    return

label add_points_boldness_delay_utility(wait_obj, not_array=False, clear_screens=False):
    $ wait_time = popup_delay + popup_fadein_time + popup_fadeout_time

    if not_array:
        $ wait_time += wait_obj
    else:
        $ wait_time += wait_obj[2]

    $ renpy.pause(wait_time)

    if clear_screens:
        $ renpy.scene('screens')

    return

screen dream_blur:
    add "interface/DreamBlur.png"

label process_end_of_scene(scene_name=False, char=False, scene_for_stats=True, do_not_jump=False, force_not_replayable=False, reset_prompted_scene=True, force_no_boldness=False, force_no_scene_limit=False, skip_adding_to_completed_scenes=False, dream=False, revisit=False):
    hide screen pop_up_general
    window hide

    if char:
        if not dream and reset_prompted_scene:
            $ char.prompted_scene = ""
        if scene_name and not force_not_replayable:
            call add_replayable_scene (scene_name, char)
        if not dream and not force_no_scene_limit:
            $ week.characters_had_scene_with_today.add(char)
        if scene_name:
            $ char.scenes_completed_in_general += 1

            if scene_name not in scenes_completed:
                $ char.scenes_completed_unique += 1

                if not dream and not revisit and char.hit_build_scene_limit(scene_name):
                    "{b}Все сцены с [char.say_name] разблокированы!{/b}"

    if not force_no_boldness:
        call add_boldness (1, tag=scene_name + "_boldness", delay=True, clear_screens=True)

    if scene_name and not skip_adding_to_completed_scenes:
        call add_completed_scene (scene_name, scene_for_stats=scene_for_stats)

    if dream:
        $ dreams_had += 1
        hide screen dream_blur

    call process_end_of_scene_before_advance_time

    if not do_not_jump:
        if started_main_game:
            call day_advance_time (force_bg_change=True)
            return

        call debug_menu

    return

label display_multiple_characters(array):
    python:
        display_multiple_characters(array)

    return

label reset_all_characters:
    python:
        reset_all_characters()

    return

label set_one_time(variable_name, tag_name=False, new_value=False, new_addition=False):
    python:
        if not tag_name:
            tag_name = variable_name

        if tag_name not in one_time_set_variable_tags:
            one_time_set_variable_tags.add(tag_name)
            
            if new_addition:
                old_value = eval(variable_name)
                new_value = new_addition + old_value
            
            if new_value:
                if isinstance(new_value, (str, unicode)):
                    new_value = "\"" + new_value + "\""
                eval_string = variable_name + " = " + str(new_value)
                exec(eval_string)

    return



label add_replayable_scene(scene_name, char=False):
    $ replay_scenes_unlocked = True

    python:
        if char and scene_name not in char.replayable_scenes:
            char.replayable_scenes.append(scene_name)
        else:
            store.general_replayable_scenes.add(scene_name)

    return

label add_completed_scene(scene_name, scene_for_stats=False):
    if scene_name not in scenes_completed:
        $ new_scenes_completed_today.add(scene_name)

    $ scenes_completed_today.add(scene_name)
    $ scenes_completed.add(scene_name)

    if scene_for_stats:
        $ scenes_completed_for_stats.add(scene_name)

    return

label clear_and_reset_characters:
    $ clear_characters()
    call reset_all_characters

    return

label fade_to_black_fade_to_static_ctc(name, pause_duration):
    call fade_to_black (pause_duration, do_not_show_quick_menu=True)
    call static_still_ctc (name)
    return

label fade_to_black(pause_duration, do_not_show_quick_menu=False):
    $ quick_menu = False
    window hide
    call static_still ("bg black")
    $ renpy.pause(pause_duration)

    if not do_not_show_quick_menu:
        $ quick_menu = True
    return

label static_still_ctc(name, show_dissolve=True, dream=False):
    $ name = name.lower()
    $ quick_menu = False
    window hide
    call static_still (name, dissolve, dream=dream)
    $ renpy.pause()
    $ quick_menu = True
    return

label prompt_display_multiple_characters(array):
    python:
        no_bust_art = False
        display_multiple_characters(array)

    return

label static_still(name, show_dissolve=True, dream=False):
    python:
        no_bust_art = True
        clear_characters()
        change_background(name, show_dissolve, dream = dream)

    return

label bust_art_background(name, dream=False):
    $ bust_art_background(name, dream = dream)

    return

label change_character_points(char):
    python hide:
        prompt = "Enter number of points to set " + char.say_name + " to."
        char.points = int( renpy.input(prompt, str( char.points ) ) )
        char.check_and_set_level()

    return

label change_character_name(char, prompt="", length=12):
    python:
        prompt += "\n[[Введите имя]"
        name_input_color = char.color
        char.say_name = renpy.input(prompt, char.say_name, length = length)
        if (len(char.say_name) == 0):
            char.say_name = char.say_name

        store.name_input_color = None

    return

label process_character(char, appearance="", text="", show_bust=True, replace=False, force_no_window=False):
    if not force_no_window:
        window auto

    if replace_position:
        $ replace_position_char = None
        $ replace_position_chars = [r_p_char for r_p_char in store.characters_shown if eval(r_p_char) != char and eval(r_p_char).position == char.position]
        if len(replace_position_chars) > 0:
            $ replace_position_char = replace_position_chars[0]
        if replace_position_char:
            call character_leave_dissolve (eval(replace_position_char))



    $ process_character_replace_utility(char, appearance = appearance, text = text, show_bust = show_bust, replace = replace)

    return

label reset_character_appearance(char, pose="None", position="None", show_bust=True):
    $ char.reset_appearance(pose = pose, position = position, show_bust = show_bust)

    return

label character_leave_dissolve(char):
    $ character_leave_dissolve(char)
    return

label random_line(random_line_array):
    python:
        random_line = random.choice(random_line_array)

        process_character_replace_utility(random_line.get("char"), appearance = random_line.get("appearance"), text = random_line.get("text"))

    return