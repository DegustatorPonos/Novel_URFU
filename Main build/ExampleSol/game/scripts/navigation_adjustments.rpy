init -80 python:
    def zone_list():
        list = []
        
        list.append(home)
        list.append(outside)
        list.append(school)
        list.append(grandma_house)
        
        return [zone for zone in list if zone.should_appear()]

    class ZoneButton(LocationButton):
        def render_character_icons(self, render, width, height, st, at):
            if self.location.is_implemented() and not self.is_focused() and self.location == store.outside and not store.entered_outside and self.location.boldness_requirement() <= store.stats.boldness_level:
                render_width = int(render.width)
                render_height = int(render.height)
                text = exclamation_mark_scene_transform("Новое!", render_width, xalign = 0.5, yalign = 0.5)
                render.place(text, x = 0, y = 0)
            
            
            return render
        
        def render(self, width, height, st, at):
            render = super(ZoneButton, self).render(width, height, st, at)
            
            if self.location.allow_show_new_scene_notice() and not self.is_focused() and any(char.scene and not char.hide_notifications() for char in self.location.zone_character_list()) and (not renpy.get_screen("navigation_zone") or store.stats.current_zone != self.location):
                text = exclamation_mark_scene_transform("Новое!", int(render.width), xalign = 0.5, yalign = 0.5)
                render.place(text, x = 0, y = 0)
            
            return render

    class Stay_Over_Zone(Zone):
        def return_location(self):
            return None
        
        def stay_over_confirm(self):
            store.advance_time_return_location = self.return_location()
            store.advance_time_return_location.start()
        
        def stay_over_reject(self):
            renpy.call("navigation_menu")
        
        def stay_over_prompt_label(self):
            return "stay_over_prompt"
        
        def stay_over_prompt(self):
            return ""
        
        def stay_over_choice(self):
            renpy.call(self.stay_over_prompt_label(), self)
            
            return
        
        def enabled_action(self):
            if store.advance_time_return_location != self.return_location():
                return self.stay_over_choice
            else:
                return super(Stay_Over_Zone, self).enabled_action() 

    class Home(Stay_Over_Zone):
        
        
        def is_enabled(self):
            return not store.is_school_time and Location.is_enabled(self)
        
        def unavailable_focused_text(self):
            if store.is_school_time:
                return "In School"
            
            return Location.unavailable_focused_text(self)
        
        def base_locations(self):
            place_list = []
            place_list.append(nate_room)
            
            if not wholesome_mode:
                place_list.append(kira_room)
                place_list.append(sam_room)
                place_list.append(simone_room)
                place_list.append(kitchen)
                place_list.append(backyard)
                place_list.append(living_room)
                place_list.append(hallway)
                place_list.append(bathroom)
                place_list.append(school_start_activation)
            
            return place_list
        
        def enabled_focused_text(self):
            return "Мой Дом"
        
        def button_image_filename_full_path(self):
            return "images/buttons/navigation_home_zone.png"
        
        def stay_over_prompt(self):
            return "Should I go back home?"
        
        def return_location(self):
            return store.nate_room

    class Grandma_House(Stay_Over_Zone):
        def is_enabled(self):
            return not store.is_school_time and Location.is_enabled(self)
        
        def should_appear(self):
            return False
        
        def is_implemented(self):
            return False
        
        def base_locations(self):
            place_list = []
            place_list.append(grandma_house_guest_room)
            place_list.append(grandma_house_bathroom)
            
            return place_list
        
        def enabled_focused_text(self):
            return "Grandma's House"
        
        def stay_over_prompt(self):
            return "Should I sleep over at Grandma's house?"
        
        def return_location(self):
            return store.grandma_house_guest_room

    class Outside(Zone):
        def is_enabled(self):
            return not store.is_school_time and Location.is_enabled(self)
        
        def is_implemented(self):
            return True
        
        def boldness_requirement(self):
            return 4
        
        def base_locations(self):
            place_list = []
            place_list.append(park)
            if store.had_vicky_intro_scene:
                place_list.append(vicky_apartment)
            if store.had_janet_intro_scene:
                place_list.append(janet_house)
            if store.had_edna_intro_scene:
                place_list.append(edna_house)
            
            return place_list
        
        def enabled_focused_text(self):
            return "Улица"
        
        def enabled_action(self):
            if self.boldness_requirement() and self.boldness_requirement() > store.stats.boldness_level:
                return self.perform_boldness_fail_action
            
            return Function(self.enter_function)
        
        def enter_function(self):
            store.entered_outside = True
            
            navigation_zone_jump(self)
            
            return
        
        def allow_show_new_scene_notice(self):
            return self.boldness_requirement() <= store.stats.boldness_level

    class School(Zone):
        def should_appear(self):
            return False
        
        def is_implemented(self):
            return False
        
        def is_enabled(self):
            return store.started_school and store.week.time == "day" and Location.is_enabled(self)
        
        def base_locations(self):
            place_list = []
            place_list.append(school_library)
            place_list.append(school_bathroom)
            place_list.append(school_homeroom)
            place_list.append(school_leave_door)
            
            return place_list
        
        def enabled_focused_text(self):
            return "School"

label bathroom_empty:
    python:
        choice_list = []
        if "simone_scene_1_seq_1" in scenes_completed:
            choice_list.append( ("Мастурбировать", "simone_scene_1_revisit") )

        choice_list.append( ("Назад", "navigation_menu") )

        chosen_option = renpy.display_menu(choice_list)
        renpy.call(chosen_option)
    return

label stay_over_prompt(zone):
    hide screen hud_zone_select
    call process_character (n, appearance="outfit clothesjacket pose handpocket face neutral", text=zone.stay_over_prompt())

    window hide
    menu:
        "Да":
            $ zone.stay_over_confirm()
        "Нет":
            $ zone.stay_over_reject()
    return

label navigation_boldness_fail:
    hide screen hud_zone_select
    call process_character (n, appearance="outfit clothesjacket pose handpocket face curious", text="Я не {b}уверен{/b}, что готов пойти туда сейчас.")
    call navigation_menu
    return