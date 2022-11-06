init python:
    def gallery_back():
        clear_characters()
        if store.started_main_game:
            renpy.call("nate_room_empty")
        else:
            renpy.call("debug_menu")
        return

    def gallery_char_select_back():
        clear_characters()
        renpy.call("gallery")
        return

    def gallery_bust_art_back():
        clear_characters()
        renpy.call("gallery_bust_art")
        return

    def char_gallery_back():
        renpy.call("gallery_cg")
        return

    def gallery_char_show(gallery_char):
        renpy.call("gallery_char_show", gallery_char)
        return

    def character_gallery_fullscreen(gallery_image, gallery_char, gallery_char_page):
        renpy.call("character_gallery_fullscreen", gallery_image, gallery_char, gallery_char_page)
        return

    def character_bust_art_gallery_set_face(char, face):
        char.face = face
        renpy.call("gallery_bust_art_char", char)
        return

    def character_bust_art_gallery_set_outfit(char, outfit):
        char.outfit = outfit
        renpy.call("gallery_bust_art_char", char)
        return

    def character_bust_art_gallery_set_pose(char, pose):
        char.pose = pose
        renpy.call("gallery_bust_art_char", char)
        return

    def character_bust_art_gallery_set_blush(char, blush):
        char.blush = blush
        renpy.call("gallery_bust_art_char", char)
        return

    def character_bust_art_gallery_select(char):
        renpy.call("gallery_bust_art_char_setup", char)
        return

image gallery_locked:
    Fixed(Solid("#000", xsize = 495, ysize = 270), Text("Locked", yalign = 0.5, xalign = 0.5, size = 60), xsize = 495, ysize = 270)

screen gallery:
    default gallery_page = 1

    $ gallery_char_arrays = [[]]
    $ gallery_char_array_i = 0

    $ gallery_char_column_max = 3
    $ gallery_char_row_max = 2

    $ gallery_max_chars_per_page = gallery_char_column_max * gallery_char_row_max

    $ gallery_all_chars = [g_char for g_char in npc_list() if g_char.should_appear_in_gallery()]
    $ gallery_char_start_index = (gallery_page - 1) * gallery_max_chars_per_page
    $ gallery_page_chars = gallery_all_chars[gallery_char_start_index:]
    $ gallery_page_amount = int( math.ceil( ( len(gallery_all_chars) ) / float(gallery_max_chars_per_page) ) )

    for gallery_char in gallery_page_chars:
        if gallery_char_array_i < gallery_char_row_max:
            $ gallery_char_arrays[gallery_char_array_i].append(gallery_char)
            if len(gallery_char_arrays[gallery_char_array_i]) >= gallery_char_column_max:
                $ gallery_char_arrays.append([])
                $ gallery_char_array_i += 1

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 50
        for gallery_array in gallery_char_arrays:
            use gallery_row(gallery_array)

    use back_button(gallery_char_select_back, xalign=0.98, yalign=0.98)

    hbox:
        xalign 0.5
        yalign 0.95
        spacing 10

        if len(gallery_all_chars) >= gallery_max_chars_per_page:

            textbutton "<" action If(gallery_page > 1, SetScreenVariable("gallery_page", gallery_page - 1), None)

            for page in range(1, gallery_page_amount + 1):
                textbutton "[page]" action SetScreenVariable("gallery_page", page)

            textbutton ">" action If(gallery_page < gallery_page_amount, SetScreenVariable("gallery_page", gallery_page + 1), None)

screen gallery_row(gallery_chars):
    hbox:
        spacing 50
        for gallery_char in gallery_chars:
            vbox:
                if gallery_char.gallery_unlock_scene_thumbnail_requirement() in scenes_completed:
                    add ResponsiveButtonWithText( idle_image = gallery_char.gallery_thumbnail(), clicked = Function(gallery_char_show, gallery_char)  ) zoom 0.25
                else:
                    add "gallery_locked"

                if gallery_char.gallery_unlock_name_requirement():
                    text gallery_char.say_name xalign 0.5
                else:
                    text "???" xalign 0.5

screen character_gallery(gallery_char, preset_page=1):
    default character_gallery_page = preset_page
    $ char_gallery_images_arrays = [[]]
    $ char_gallery_images_array_i = 0
    $ char_gallery_column_max = 3
    $ char_gallery_row_max = 2
    $ char_gallery_max_images_per_page = char_gallery_column_max * char_gallery_row_max
    $ char_gallery_all_images = gallery_char.gallery_images()
    $ char_gallery_page_images = char_gallery_all_images[(character_gallery_page - 1) * char_gallery_max_images_per_page:]
    $ character_gallery_page_amount = int( math.ceil( ( len(char_gallery_all_images) ) / float(char_gallery_max_images_per_page) ) )

    for gallery_char_image in char_gallery_page_images:
        $ char_gallery_images_arrays[char_gallery_images_array_i].append(gallery_char_image)
        if len(char_gallery_images_arrays[char_gallery_images_array_i]) >= char_gallery_column_max:
            $ char_gallery_images_arrays.append([])
            $ char_gallery_images_array_i += 1

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 50
        for i, gallery_array in enumerate(char_gallery_images_arrays):
            if i < char_gallery_row_max:
                use character_gallery_row(gallery_array, gallery_char, character_gallery_page)

    use back_button(char_gallery_back, xalign=0.98, yalign=0.98)

    hbox:
        xalign 0.5
        yalign 0.95
        spacing 10

        if len(char_gallery_all_images) >= char_gallery_max_images_per_page:

            textbutton "<" action If(character_gallery_page > 1, SetScreenVariable("character_gallery_page", character_gallery_page - 1), None)

            for page in range(1, character_gallery_page_amount + 1):
                textbutton "[page]" action SetScreenVariable("character_gallery_page", page)

            textbutton ">" action If(character_gallery_page < character_gallery_page_amount, SetScreenVariable("character_gallery_page", character_gallery_page + 1), None)


screen character_gallery_row(character_gallery_images, gallery_char, gallery_char_page):
    hbox:
        spacing 50
        for i, gallery_image in enumerate(character_gallery_images):
            vbox:
                add ResponsiveButtonWithText( idle_image = gallery_image, clicked = Function(character_gallery_fullscreen, gallery_image, gallery_char, gallery_char_page)  ) zoom 0.25

screen character_gallery_fullscreen(character_gallery_image):
    add character_gallery_image

screen character_bust_art_gallery(bust_art_gallery_char):
    hbox:
        spacing 20
        vbox:
            text "Faces" xalign 0.5 size 48
            for bust_art_face in bust_art_gallery_char.gallery_bust_art_faces():
                textbutton bust_art_face.capitalize() sensitive bust_art_gallery_char.face != bust_art_face action Function(character_bust_art_gallery_set_face, bust_art_gallery_char, bust_art_face) xalign 0.5
        vbox:
            text "Outfits" xalign 0.5 size 48
            for bust_art_outfit in bust_art_gallery_char.gallery_bust_art_outfits():
                textbutton string.capwords(bust_art_outfit.replace("_", " ")) sensitive bust_art_gallery_char.outfit != bust_art_outfit action Function(character_bust_art_gallery_set_outfit, bust_art_gallery_char, bust_art_outfit) xalign 0.5
        vbox:
            text "Poses" xalign 0.5 size 48
            for bust_art_pose in bust_art_gallery_char.gallery_bust_art_poses():
                textbutton bust_art_pose.capitalize() sensitive bust_art_gallery_char.pose != bust_art_pose action Function(character_bust_art_gallery_set_pose, bust_art_gallery_char, bust_art_pose) xalign 0.5
        vbox:
            text "Blush" xalign 0.5 size 48
            textbutton "Blush" sensitive not bust_art_gallery_char.blush action Function(character_bust_art_gallery_set_blush, bust_art_gallery_char, True) xalign 0.5
            textbutton "No Blush" sensitive bust_art_gallery_char.blush action Function(character_bust_art_gallery_set_blush, bust_art_gallery_char, False) xalign 0.5

    use back_button(gallery_bust_art_back, xalign=0.98, yalign=0.98)

screen gallery_bust_art_char_select:
    default character_gallery_bust_art_page = 1
    $ bust_art_gallery_char_page_max = 5
    $ bust_art_gallery_chars_start_index = (character_gallery_bust_art_page - 1) * bust_art_gallery_char_page_max
    $ bust_art_gallery_all_chars = [g_char for g_char in character_list() if g_char.gallery_bust_art_can_be_shown()]
    $ bust_art_gallery_page_chars = bust_art_gallery_all_chars[bust_art_gallery_chars_start_index: bust_art_gallery_chars_start_index + bust_art_gallery_char_page_max]
    $ character_gallery_bust_art_page_amount = int( math.ceil( ( len(bust_art_gallery_all_chars) ) / float(bust_art_gallery_char_page_max) ) )

    hbox:
        xalign 0.5
        yalign 1.0
        spacing 0

        for bust_art_gallery_char in bust_art_gallery_page_chars:
            if bust_art_gallery_char.gallery_bust_art_can_be_shown():
                add CharacterButton(bust_art_gallery_char, clicked = Function(character_bust_art_gallery_select, bust_art_gallery_char)) yalign 1.0

    vbox:
        xalign 0.5
        yalign 0.05
        spacing 10

        use back_button(gallery_char_select_back)
        hbox:
            spacing 10

            if len(bust_art_gallery_all_chars) >= bust_art_gallery_char_page_max:

                textbutton "<" action If(character_gallery_bust_art_page > 1, SetScreenVariable("character_gallery_bust_art_page", character_gallery_bust_art_page - 1), None)

                for page in range(1, character_gallery_bust_art_page_amount + 1):
                    textbutton "[page]" action SetScreenVariable("character_gallery_bust_art_page", page)

                textbutton ">" action If(character_gallery_bust_art_page < character_gallery_bust_art_page_amount, SetScreenVariable("character_gallery_bust_art_page", character_gallery_bust_art_page + 1), None)

label gallery:
    menu:
        "Галерея CG":
            jump gallery_cg
        "Галерея персонажей":
            jump gallery_bust_art
        "Назад":
            if started_main_game:
                jump nate_room_empty
            else:
                jump debug_menu

    return

label gallery_bust_art:
    $ renpy.scene('screens')
    call screen gallery_bust_art_char_select
    return

label gallery_bust_art_char_setup(bust_art_gallery_char):
    $ bust_art_gallery_char.position = "right"
    $ bust_art_gallery_char.face = bust_art_gallery_char.gallery_bust_art_default_face()
    $ bust_art_gallery_char.outfit = bust_art_gallery_char.gallery_bust_art_default_outfit()
    $ bust_art_gallery_char.pose = bust_art_gallery_char.gallery_bust_art_default_pose()
    $ bust_art_gallery_char.blush = False

    call gallery_bust_art_char (bust_art_gallery_char)
    return

label gallery_bust_art_char(bust_art_gallery_char):
    window hide
    call process_character (bust_art_gallery_char, appearance="yea", force_no_window=True)
    window hide

    call screen character_bust_art_gallery(bust_art_gallery_char)
    return

label gallery_cg:
    $ renpy.scene('screens')


    hide screen character_gallery_fullscreen
    call screen gallery

    return

label gallery_char_show(shown_gallery_char, preset_page=1):
    call screen character_gallery(shown_gallery_char, preset_page)
    return

label character_gallery_fullscreen(character_gallery_fullscreen_image, gallery_char, gallery_char_page):
    python:
        if "kira_titfuck_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "kira_titfuck_anim_gallery"
        elif "kira_titfuck_anim_20" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "kira_titfuck_anim_cum_gallery"
        elif "kira_3_buttjob_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "kira_3_buttjob_anim"
        elif "kira_anal_anim_2" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "kira_anal_anim"
        elif "simone_vaginal_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "simone_vaginal_anim"
        elif "sam_grind_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "sam_grind_anim"
        elif "sam_dream_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "sam_dream_anim"
        elif "janet_anal_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "janet_anal_anim"
        elif "edna_titfuck_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "edna_titfuck_bikini_anim"
        elif "edna_titfuck_nude_anim_0" in character_gallery_fullscreen_image:
            character_gallery_fullscreen_image = "edna_titfuck_nude_anim"



    show screen character_gallery_fullscreen(character_gallery_fullscreen_image)
    pause
    call gallery_char_show (gallery_char, gallery_char_page)
    return