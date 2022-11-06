init -100 python:

    def stat_screen_back():
        store.advance_time_return_location.start()
        return

    class Stat_Screen_Display_Object(object):
        def __init__(self, name, value):
            self.name = name
            self.value = value

    class Stats(object):
        def __init__(self):
            self.stats = {}
            self.stat_keys = set()
            self.boldness_level = 1
            self.boldness_xp = 0
            self.current_zone = None
            self.current_location = None
            self.add_boldness_or_relationship_tags = []
            self.minigame_boldness_xp = 0
        
        
        
        def boldness_points_between_boldness_levels(self, first_level, second_level):
            return abs(self.boldness_xp_required_for_level(first_level) - self.boldness_xp_required_for_level(second_level) )
        
        def boldness_points_between_current_and_next_level(self):
            return self.boldness_points_between_boldness_levels(self.boldness_level, self.boldness_level + 1)
        
        def stat_screen_boldness_xp_string(self):
            if self.boldness_level_cap() and self.boldness_level >= self.boldness_level_cap():
                return str(self.boldness_xp) + " XP"
            else:
                current_xp = min( self.current_boldness_xp_relative(), self.boldness_xp_required_for_level(self.boldness_level + 1) )
                return str(current_xp) + " / " + str( self.boldness_points_between_current_and_next_level() ) + " XP"
        
        def current_boldness_xp_relative(self):
            return max( self.boldness_xp - self.boldness_xp_required_for_level(self.boldness_level), 0 )
        
        def progress_ratio_to_next_boldness_level_relative(self):
            if self.boldness_level_cap() and self.boldness_level >= self.boldness_level_cap():
                return 1.0
            
            return self.current_boldness_xp_relative() / float(self.boldness_points_between_current_and_next_level())
        
        def stat_screen_boldness_level_string(self):
            text = "Boldness Level: " + str(self.boldness_level)
            if self.boldness_level_cap() and self.boldness_level >= self.boldness_level_cap():
                text += " (Максимум)"
            
            return text
        
        def level_up_text(self):
            
            
            if self.boldness_level_cap() and self.boldness_level >= self.boldness_level_cap():
                text += "\n{b}Максимальный Уровень Смелости!{/b}"
            
            return text
        
        def add_boldness_xp(self, quantity, tag = None, force_no_popup = False, minigame = False, yalign = None):
            if yalign is None:
                yalign = add_relationship_boldness_points_yalign
            
            if tag and tag in self.add_boldness_or_relationship_tags:
                return
            
            if minigame and quantity > 0:
                self.minigame_boldness_xp += quantity
            
            sound = add_boldness_points_sound
            appear_time = add_boldness_points_appear_time
            
            self.boldness_xp += quantity
            
            if self.boldness_xp_cap() and self.boldness_level_cap():
                self.boldness_xp = min( self.boldness_xp, self.xp_required_for_level( self.boldness_level_cap() ) )
            
            leveled_up = self.check_and_set_boldness_level() 
            
            if tag:
                self.add_boldness_or_relationship_tags.append(tag)
            
            text = "+" + str(quantity) + " " + boldness_name + "!"
            
            is_max_level = self.boldness_level_cap() and self.boldness_level >= self.boldness_level_cap()
            
            if leveled_up:
                text += "\n" + boldness_name + " увеличилась!"
                sound = boldness_level_up_sound
                
                if is_max_level:
                    text += "\n{b}" + boldness_name + " Максимальна!{/b}"
            else:
                if is_max_level:
                    text += "\n{b}" + boldness_name + " Максимальна!{/b}"
            
            if not force_no_popup:
                renpy.hide_screen("pop_up_general")
                renpy.show_screen("pop_up_general", text, sound, appear_time, yalign = yalign)
            
            return [text, leveled_up, appear_time]
        
        def boldness_xp_cap(self):
            return False
        
        def boldness_xp_required_for_level(self, level):
            if not level or level == 1:
                return 0
            elif level == 2:
                return 2
            elif level == 3:
                return 4
            elif level == 4:
                return 8
            elif level == 5:
                return 12
            elif level == 6:
                return 16
            elif level == 7:
                return 20
            
            return 999999999
        
        def get_evaluated_boldness_level(self):
            passed_level = self.boldness_level
            i = 1
            
            while True:
                test_level = self.boldness_level + i
                
                required_xp = self.boldness_xp_required_for_level(test_level)
                
                if required_xp > self.boldness_xp:
                    break
                else:
                    passed_level = test_level
                
                i += 1
            
            return passed_level
        
        def boldness_level_cap(self):
            return None
        
        def check_and_set_boldness_level(self):
            old_level = self.boldness_level
            
            new_level = self.get_evaluated_boldness_level()
            
            if self.boldness_level_cap():
                new_level = min(self.boldness_level_cap(), new_level)
            
            if new_level > self.boldness_level:
                self.boldness_level = new_level
            
            return old_level < new_level
        
        def add_stat(self, name, quantity = 1):
            self.stat_keys.add(name)
            if name in self.stats:
                self.stats[name] += quantity
            else:
                self.stats[name] = quantity
            
            return
        
        def stat_value(self, name):
            if name in self.stats:
                return self.stats[name]
            else:
                return 0
        
        def stat_screen_object(self, key, name):
            if key in self.stat_keys:
                return Stat_Screen_Display_Object ( name, str ( self.stat_value( key ) )  )
            else:
                return False
        
        def add_stat_screen_object(self, array, key, name):
            object = self.stat_screen_object(key, name)
            
            if object:
                array.append( object )
            
            return array
        
        def add_boldness_stat(self, array):
            array.append( Stat_Screen_Display_Object( boldness_name + " Level", str( store.stats.boldness_level )  ) )
            
            return array
        
        def add_days_passed_stat(self, array):
            array.append( Stat_Screen_Display_Object( "Days Passed", str( store.week.days_passed )  ) )
            
            return array
        
        def add_dreams_had_stat(self, array):
            array.append( Stat_Screen_Display_Object( "Dreams Had", str( store.dreams_had )  ) )
            
            return array
        
        def add_weeks_passed_stat(self, array):
            array.append( Stat_Screen_Display_Object( "Weeks Passed", str( store.week.weeks_passed )  ) )
            
            return array
        
        def add_scenes_completed_stat(self, array):
            array.append( Stat_Screen_Display_Object( "Scenes Completed", str ( len( store.scenes_completed_for_stats ) )  ) )
            
            return array
        
        def add_character_scenes_stats(self, array):
            stat_chars = fuckable_npc_list()
            for stat_char in stat_chars:
                if stat_char.display_level_stats():
                    array.append( Stat_Screen_Display_Object( stat_char.say_name + " Relationship Level: ", str ( stat_char.relationship_level )  ) )
                
                if stat_char.display_scene_stats():
                    array.append( Stat_Screen_Display_Object( "Scenes Completed With " + stat_char.say_name, str ( stat_char.scenes_completed_unique )  ) )
            
            
            return array
        
        def add_minigame_stats(self, array):
            
            array.append( Stat_Screen_Display_Object( "Minigames Done",  str ( store.minigames_done )  ) )
            
            
            return array
        
        def stat_screen_array(self):
            array = []
            
            return array

screen misc_stats(stat_screen_misc_array, misc_stat_page, ypos=0):
    vbox:
        xalign 0.2
        ypos ypos

        $ stat_screen_misc_array_start_index = 0 + (51 * (misc_stat_page - 1) )
        $ stat_screen_misc_array_end_index = 51 + (51 * (misc_stat_page - 1) )
        $ stat_screen_misc_array_for_columns = stat_screen_misc_array[stat_screen_misc_array_start_index:stat_screen_misc_array_end_index]


        hbox:
            use stats_column(stat_screen_misc_array_for_columns, 0, 17, 0)
            use stats_column(stat_screen_misc_array_for_columns, 17, 34, 1)
            use stats_column(stat_screen_misc_array_for_columns, 34, 51, 2)

screen stats_column(stat_screen_array, start, end, stat_screen_column_i):
    python:
        if not end:
            end = len(stat_screen_array)
        stat_screen_array = stat_screen_array[start:end]

    hbox:
        vbox:
            for stat_screen_object in stat_screen_array:
                text stat_screen_object.name
            null width 500

        vbox:
            for stat_screen_object in stat_screen_array:
                text stat_screen_object.value

            null width 100

screen relationships(relationship_screen_characters):
    for relationship_char in relationship_screen_characters:
        hbox:
            spacing 20
            add relationship_char.icon_image()
            vbox:

                if not relationship_char.is_hidden_on_stat_screen():
                    text relationship_char.say_name

                    if not relationship_char.show_scene_completion_only_on_stats():
                        text relationship_char.stat_screen_level_string()
                        bar value relationship_char.progress_ratio_to_next_level_relative() range 1.0 xmaximum 650
                        text relationship_char.stat_screen_xp_string()
                    else:
                        text str(relationship_char.num_main_scenes_completed()) + "/" + str(len(relationship_char.list_of_main_scenes())) + " Сцены Завершены"

                else:
                    text "???"

screen boldness_relationships(stat_screen_characters, stat_screen_characters_page, yalign=0.0, xalign=0.5):

    hbox:
        xalign xalign
        yalign yalign
        spacing 40

        if stat_screen_characters_page == 1:
            vbox:
                hbox:
                    spacing 20

                    add player_character.icon_image()
                    vbox:
                        text player_character.say_name
                        text stats.stat_screen_boldness_level_string()
                        bar value stats.progress_ratio_to_next_boldness_level_relative() range 1.0 xmaximum 650
                        text stats.stat_screen_boldness_xp_string()

                use relationships(stat_screen_characters[:3])

            vbox:
                use relationships(stat_screen_characters[3:7])
        else:
            $ stat_screen_characters_start_row_one = 7 + (8 * (stat_screen_characters_page - 2) )
            $ stat_screen_characters_end_row_one = stat_screen_characters_start_row_one + 4

            $ stat_screen_characters_start_row_two = 11 + (8 * (stat_screen_characters_page - 2) )
            $ stat_screen_characters_end_row_two = stat_screen_characters_start_row_two + 4

            vbox:
                use relationships(stat_screen_characters[stat_screen_characters_start_row_one : stat_screen_characters_end_row_one ] )

            vbox:
                use relationships(stat_screen_characters[stat_screen_characters_start_row_two : stat_screen_characters_end_row_two ] )

screen stats:
    modal True
    if current_background:
        add current_background

    default stat_screen_display_type = "character"
    default stat_screen_character_page = 1

    default stat_screen_misc_stats_page = 1

    $ stat_screen_characters = relationship_screen_characters()
    $ stat_screen_character_page_amount = int( math.ceil( ( len(stat_screen_characters) + 1 ) / float(8) ) )
    $ stat_screen_character_page = min( stat_screen_character_page, stat_screen_character_page_amount )

    $ stat_screen_misc_stats = stats.stat_screen_array()
    $ stat_screen_misc_stats_page_amount = int( math.ceil( ( len(stat_screen_misc_stats) + 1 ) / float(51) ) )
    $ stat_screen_misc_stats_page = min( stat_screen_misc_stats_page, stat_screen_misc_stats_page_amount )

    hbox:
        xalign 0.5
        yalign 0.025

        textbutton _("Characters") action SetScreenVariable("stat_screen_display_type", "character")
        textbutton _("Misc") action SetScreenVariable("stat_screen_display_type", "misc")


    if stat_screen_display_type == "character":
        use boldness_relationships(stat_screen_characters, stat_screen_character_page, yalign=0.45)

        hbox:
            xalign 0.5
            yalign 0.95

            if stat_screen_character_page_amount > 1:

                textbutton "<" action If(stat_screen_character_page > 1, SetScreenVariable("stat_screen_character_page", stat_screen_character_page - 1), None)

                for page in range(1, stat_screen_character_page_amount + 1):
                    textbutton "[page]" action SetScreenVariable("stat_screen_character_page", page)

                textbutton ">" action If(stat_screen_character_page < stat_screen_character_page_amount, SetScreenVariable("stat_screen_character_page", stat_screen_character_page + 1), None)

    elif stat_screen_display_type == "misc":
        use misc_stats(stat_screen_misc_stats, stat_screen_misc_stats_page, ypos=100)

        if stat_screen_misc_stats_page_amount > 1:

            hbox:
                xalign 0.5
                yalign 0.95

                textbutton "<" action If(stat_screen_misc_stats_page > 1, SetScreenVariable("stat_screen_misc_stats_page", stat_screen_misc_stats_page - 1), None)

                for page in range(1, stat_screen_misc_stats_page_amount + 1):
                    textbutton "[page]" action SetScreenVariable("stat_screen_misc_stats_page", page)

                textbutton ">" action If(stat_screen_misc_stats_page < stat_screen_misc_stats_page_amount, SetScreenVariable("stat_screen_misc_stats_page", stat_screen_misc_stats_page + 1), None)

    use back_button(navigation_back, xalign=0.98, yalign=0.98)