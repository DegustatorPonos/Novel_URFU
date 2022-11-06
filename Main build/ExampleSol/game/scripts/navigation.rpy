init -90 python:
    def navigation_next_song():
        renpy.music.stop(fadeout=1)
        return

    def location_character_select(char):
        store.last_selected_character = char
        char.select()
        return

    def navigation_button_image(location):
        return location.button_image() + "_idle"

    def navigation_back():
        if store.stats.current_location:
            if store.last_selected_character:
                renpy.call("location_select", store.stats.current_location, preset_location_select_char = store.last_selected_character)
            else:
                store.stats.current_location.start()
        else:
            store.advance_time_return_location.start()

    def navigation_zone_jump(zone):
        renpy.call("navigation_zone_jump", zone)
        return

    class Zone(Location):
        def unfocused_text(self):
            if renpy.get_screen("navigation_zone") and store.stats.current_zone == self:
                return "Вы здесь"
            else:
                return Location.unfocused_text(self)
        
        def base_locations(self):
            place_list = []
            return place_list
        
        def locations(self):
            return [location for location in self.base_locations() if location.should_appear()]
        
        def zone_character_list(self):
            characters = []
            place_list = self.locations()
            
            for place in place_list:
                characters.extend(place.character_list())
            
            return characters
        
        def enabled_action(self):
            if self.boldness_requirement() and self.boldness_requirement() > store.stats.boldness_level:
                return self.perform_boldness_fail_action
            
            return Function(navigation_zone_jump, self)
        
        def reset_locations_and_characters(self):
            chars = self.zone_character_list()
            self.reset_locations()
            
            for char in chars:
                char.reset()
            
            return
        
        def reset_locations(self):
            locations = self.locations()
            
            for location in locations:
                location.reset()
            
            return
        
        def button_image_filename_full_path(self):
            return "images/buttons/navigation_outside_zone.png"
        
        def allow_show_new_scene_notice(self):
            return True

    class ResponsiveButtonWithTextBase(renpy.display.behavior.ImageButton):
        def text(self):
            return self.focused_text if self.is_focused() else self.unfocused_text
        
        def text_xalign(self):
            return self.text_xalign_focused() if self.is_focused() else self.text_xalign_unfocused()
        
        def text_xalign_focused(self):
            return 0.5
        
        def text_xalign_unfocused(self):
            return 0.5
        
        def text_yalign(self):
            return self.text_yalign_focused() if self.is_focused() else self.text_yalign_unfocused()
        
        def text_yalign_unfocused(self):
            return 0.5
        
        def text_yalign_focused(self):
            return 0.5
        
        def text_displayable(self):
            return Text(self.text(), xalign = self.text_xalign(), yalign = self.text_yalign(), size = self.text_size)
        
        def render_focused_text(self, render, width, height, st, at):
            if self.text():
                text = Fixed( self.text_displayable(), xysize = ( int( render.width ), int( render.height ) ) )
                render.blit(renpy.render( text, width, height, st, at), ( 0,  0), False)
            
            return render
        
        def render(self, width, height, st, at):
            render = super(ResponsiveButtonWithTextBase, self).render(width, height, st, at)
            
            render = self.render_focused_text(render, width, height, st, at)
            
            return render


    class ResponsiveTextButton(ResponsiveButtonWithTextBase):
        def __init__(self, 
                     focused_text = "",
                     unfocused_text = "",
                     text_size = 32,
                     **properties):
            
            self.focused_text = focused_text
            self.unfocused_text = unfocused_text
            self.text_size = text_size
            
            focused_text_dummy_render = renpy.render( Text(self.focused_text, size = self.text_size), 1920, 1080, 0, 0)
            unfocused_text_dummy_render = renpy.render( Text(self.unfocused_text, size = self.text_size), 1920, 1080, 0, 0)
            
            null_width = focused_text_dummy_render.width if focused_text_dummy_render.width > unfocused_text_dummy_render.width else unfocused_text_dummy_render.width
            null_height = focused_text_dummy_render.height if focused_text_dummy_render.height > unfocused_text_dummy_render.height else unfocused_text_dummy_render.height
            
            idle_image = Null(width = null_width, height = null_height)
            
            super(ResponsiveTextButton, self).__init__(idle_image = idle_image, **properties)

    class ResponsiveButtonWithText(ResponsiveButtonWithTextBase):
        def __init__(self, idle_image,
                     focused_brightness = -0.15,
                     focused_text = "",
                     unfocused_text = "",
                     text_size = 32,
                     **properties):
            
            self.focused_text = focused_text
            self.unfocused_text = unfocused_text
            self.focused_brightness = focused_brightness
            self.text_size = text_size
            
            idle_image = self.make_idle_image(idle_image)
            hover_image = self.make_hover_image(idle_image)
            
            super(ResponsiveButtonWithText, self).__init__(idle_image = idle_image, hover_image = hover_image, **properties)
        
        def should_desaturate(self):
            return False
        
        def make_idle_image(self, idle_image):
            if self.should_desaturate():
                matrix = im.matrix.desaturate()
                idle_image = im.MatrixColor(idle_image, matrix)
            
            return renpy.easy.displayable(idle_image)
        
        def make_hover_image(self, original_idle_image):
            matrix = im.matrix.brightness( self.focused_brightness )
            
            if self.should_desaturate():
                matrix = matrix.desaturate()
            
            return im.MatrixColor(original_idle_image, matrix)

    class LocationButton(ResponsiveButtonWithText):
        def __init__(self, location, clicked = None, **properties):
            
            self.location = location
            focused_text = self.location.focused_text()
            unfocused_text = self.location.unfocused_text()
            idle_image = self.location.button_image_filename_full_path()
            
            if not clicked:
                clicked = self.location.clicked_action()
            
            super(LocationButton, self).__init__(idle_image = idle_image, focused_text = focused_text, unfocused_text = unfocused_text, clicked = clicked, **properties)
        
        def character_icon_size(self):
            return 120
        
        def should_desaturate(self):
            return self.location.is_disabled()
        
        def render_character_icons(self, render, width, height, st, at):
            characters = self.location.character_list()
            render_width = int(render.width)
            render_height = int(render.height)
            
            for i in range( len(characters) ):
                icon_text = ""
                character = characters[i]
                
                if not character.has_location_navigation_icon():
                    continue
                
                if not character.hide_notifications() and not character.prompted_scene and character.scene and character.scene not in store.scenes_completed and not character.scene_is_low_priority:
                    icon_text = "!"
                
                x = 0
                y = 0
                if i == 1:
                    x = render_width - self.character_icon_size()
                elif i == 2:
                    y = render_height - self.character_icon_size()
                elif i == 3:
                    x = render_width - self.character_icon_size()
                    y = render_height - self.character_icon_size()
                
                character_image = renpy.displayable(character.icon_image())
                t = Transform(child=character_image, size = ( self.character_icon_size(), self.character_icon_size() ) )
                render.blit(renpy.render(t, width, height, st, at),(x, y), False)
                
                if icon_text:
                    
                    
                    text = exclamation_mark_scene_transform(icon_text, self.character_icon_size())
                    render.place(text, x = x, y = y)
            
            return render
        
        def render(self, width, height, st, at):
            render = super(ResponsiveButtonWithText, self).render(width, height, st, at)
            
            if not self.is_focused() and any(not char.hide_notifications() and not char.has_location_navigation_icon() and char.scene for char in self.location.characters):
                text = exclamation_mark_scene_transform("Новое!", int(render.width), xalign = 0.5, yalign = 0.5)
                render.place(text, x = 0, y = 0)
            
            render = self.render_character_icons(render, width, height, st, at)
            render = self.render_focused_text(render, width, height, st, at)
            
            
            return render

    class ZoneButton(LocationButton):
        def render_character_icons(self, render, width, height, st, at):
            return render

    class CharacterButton(renpy.display.behavior.ImageButton):
        def __init__(self,
                     character,
                     idle_image = None,
                     hover_image=None,
                     insensitive_image=None,
                     activate_image=None,
                     selected_idle_image=None,
                     selected_hover_image=None,
                     selected_insensitive_image=None,
                     selected_activate_image=None,
                     style='image_button',
                     clicked=None,
                     hovered=None,
                     **properties):
            
            self.character = character
            
            crop_left = self.character.character_select_button_crop_left()
            crop_right = self.character.character_select_button_crop_right()
            crop_top = self.character.character_select_button_crop_top()
            crop_bottom = self.character.character_select_button_crop_bottom()
            
            crop_width = self.character.image_width() - crop_left - crop_right
            crop_height = self.character.image_height() - crop_top - crop_bottom
            null_image_height = crop_height - self.character.character_select_y()
            
            self.crop = ( crop_left, crop_top,  crop_width, crop_height )
            
            idle_image = Null( width = crop_width, height = null_image_height )
            
            idle_image = Transform( child = idle_image)
            
            super(CharacterButton, self).__init__(idle_image = idle_image,
                     hover_image=hover_image,
                     insensitive_image=insensitive_image,
                     activate_image=activate_image,
                     selected_idle_image=selected_idle_image,
                     selected_hover_image=selected_hover_image,
                     selected_insensitive_image=selected_insensitive_image,
                     selected_activate_image=selected_activate_image,
                     style='image_button',
                     clicked=clicked,
                     hovered=hovered,
                     **properties)
        
        def render(self, width, height, st, at):
            render = super(CharacterButton, self).render(width, height, st, at)
            
            
            self.character.pose = self.character.hovered_pose() if self.is_focused() else self.character.unhovered_pose()
            
            base_image_filename = self.character.hovered_base_image_filename() if self.is_focused() else self.character.unhovered_base_image_filename()
            face_image_filename = self.character.hovered_face_image_filename() if self.is_focused() else self.character.unhovered_face_image_filename()
            
            matrix = im.matrix.brightness( self.character.character_select_focused_brightness()  )
            
            x = 0
            y = 0
            
            character_base = renpy.displayable( base_image_filename )
            
            if self.is_focused() and store.char_select_darken_on_hover:
                character_base = im.MatrixColor(character_base, matrix)
            
            base_t = Transform(child=character_base, crop = self.crop, xzoom = store.store.character_select_xscale )
            
            
            render.blit( renpy.render(base_t, width, height, st, at), (x, y) , False )
            
            character_face = renpy.displayable( face_image_filename )
            
            if self.is_focused() and store.char_select_darken_on_hover:
                character_face = im.MatrixColor(character_face, matrix)
            
            face_t = Transform(child=character_face, crop = self.crop, xzoom = store.store.character_select_xscale )
            render.blit( renpy.render(face_t, width, height, st, at), (x, y) , False )
            
            if self.character.has_separate_mouth():
                character_mouth = renpy.displayable( self.character.mouth_image_filename() )
                
                if self.is_focused() and store.char_select_darken_on_hover:
                    character_face = im.MatrixColor(character_mouth, matrix)
                
                face_t = Transform(child=character_mouth, crop = self.crop, xzoom = store.store.character_select_xscale )
                render.blit( renpy.render(face_t, width, height, st, at), (x, y) , False )
            
            return render

transform exclamation_mark_scene_transform(text, size, xalign=0.08, yalign=0.0):
    Fixed( Text( text, xalign = xalign, yalign = yalign, size = 60), xysize=(size, size) )
    pause 1.0
    linear 1.0 alpha 0.0
    linear 1.0 alpha 1.0
    repeat

screen patreon_logo(xalign=0.01, yalign=0.98):
    add ResponsiveButtonWithText(patreon_logo_filename, text_size = 32, focused_text = patreon_logo_focused_text, clicked = OpenURL(patreon_logo_url)) xalign xalign yalign yalign

screen back_button(function_name=None, xalign=0.5, yalign=0.0, focused_text="Назад", click_action=None):
    if function_name:
        $ back_button_clicked = Function(function_name)
    elif click_action:
        $ back_button_clicked = click_action

    add ResponsiveButtonWithText(back_button_filename, text_size = 32, focused_text = focused_text, clicked = back_button_clicked) xalign xalign yalign yalign

screen navigation_zone(navigation_locations):
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 30

        use location_row(navigation_locations, 0, navigation_location_row_num)
        use location_row(navigation_locations, navigation_location_row_num)
        use back_button(navigation_back, xalign=0.5)

    if show_next_music_track_textbutton:
        textbutton next_music_track_text action Function(navigation_next_song) xalign 0.99 yalign 0.99

screen location_row(location_array, start, end=False):
    python:
        if not end:
            end = len(location_array)
        location_array = location_array[start:end]

    hbox:
        spacing 40
        for navigation_location in location_array:
            add LocationButton(navigation_location)

screen hud_zone_select:
    hbox:
        xalign 0.01
        yalign 0.01
        spacing 20

        for hud_zone_select_zone in zone_list():
            add ZoneButton(hud_zone_select_zone)

screen hud:
    vbox:
        xalign 0.99
        yalign 0.01

        text week.day_named() style "hud_text" xalign 1.0
        text week.time_named() style "hud_text" size 40

        if show_money_on_hud:
            text inventory.money_string() style "hud_text" xalign 0.6

screen location_character_select(location):
    hbox:
        xalign 0.5
        yalign 1.0
        spacing 50

        for select_char in location.characters:

            add CharacterButton(select_char, clicked = Function(location_character_select, select_char)) yalign 1.0


    use back_button(click_action=Jump('navigation_menu'), xalign=0.98, yalign=0.98)

label location_select(location, morning_wake_lines=False, preset_location_select_char=None):
    $ last_selected_character = None
    $ clear_characters()
    window hide
    show screen hud
    python:
        bust_art_background(location.background())

    if morning_wake_lines:
        call morning_wake_lines

    python hide:
        if preset_location_select_char:
            location_character_select(preset_location_select_char)
        else:
            renpy.show_screen("hud_zone_select")
            if len(location.characters) > 0:
                if any(not char.has_location_navigation_icon() for char in location.characters):
                    renpy.call("menu_character_select", location = location)
                else:
                    renpy.call_screen("location_character_select", location)
            else:
                location.empty_action()

    return

label menu_character_select(location=None):
    python hide:
        choice_list = []

        for char in location.characters:
            title = char.menu_character_select_label()
            choice_list.append( (title, char) )

        choice_list.append( ("Назад", "back") )
        chosen_option = renpy.display_menu(choice_list)

        if chosen_option != "back":
            renpy.call(chosen_option.menu_character_select_renpy_label(), chosen_option)
        else:
            renpy.call("navigation_menu")

    return


label empty_location:
    python:
        choice_list = []
        choice_list.append( ("Назад", "navigation_menu") )

        chosen_option = renpy.display_menu(choice_list)
        renpy.call(chosen_option)

    return

label navigation_zone_jump(zone):
    call navigation_menu (zone.locations())
    return

label navigation_menu(navigation_locations=None):
    python:
        renpy.checkpoint()
        renpy.scene('screens')
        clear_characters()

    show screen hud
    show screen hud_zone_select
    window hide
    if navigation_locations is not None:
        call screen navigation_zone(navigation_locations)
    else:
        if stats.current_zone:
            call screen navigation_zone(stats.current_zone.locations())
        else:
            call screen navigation_zone(home.locations())

    return