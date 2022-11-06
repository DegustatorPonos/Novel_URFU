init -100 python:

    def character_list():
        char_list = [store.player_character]
        char_list.extend(npc_list())
        
        return char_list

    def relationship_screen_characters():
        char_list = [char for char in npc_list() if char.show_on_stat_screen()]
        
        
        return char_list



    def fuckable_npc_list():
        return [char for char in npc_list() if char.is_fuckable()]

    class Actor(object):
        def __init__(self, internal_name, variable_name):
            self.internal_name = internal_name
            
            self.say_name = self.default_say_name()
            
            self.variable_name = variable_name
            
            self.create_renpy_characters()
            
            
            self.scene = ""
            self.scenes_completed_unique = 0
            self.scenes_completed_in_general = 0
            self.revistable_scenes = set()
            self.replayable_scenes = []
            self.prompted_scene = ""
            self.play_scene_even_with_prompted_scene = False
            self.scene_is_low_priority = False
            
            
            self.face = self.default_face()
            self.outfit = self.default_outfit()
            self.pose = self.default_pose()
            self.position = self.default_position()
            self.blush = False
            self.reset_overlays()
            
            
            self.points = 0
            self.relationship_level = 1
            self.add_points_tags = []
            self.minigame_points = 0
            
            self.priority_conversation = ""
            self.conversation = ""
            self.conversation_pool = []
            self.conversations_completed = set()
            self.recently_completed_conversations = set()
            
            self.placed_in_a_location = False
            self.has_tried_to_place_at_least_once = False
            
            self.reset_conversation()
        
        
        def fix_appearance(self):
            return
        
        def hide_notifications(self):
            return False
        
        def use_character_select(self):
            return True
        
        def display_bust_art_in_character_menu(self):
            return True
        
        def hit_build_scene_limit(self, new_scene = None):
            main_scenes = self.list_of_main_scenes()
            
            if len(main_scenes) <= 0:
                return False
            
            if new_scene and new_scene in main_scenes:
                main_scenes.remove(new_scene)
            
            for scene in main_scenes:
                if scene not in store.scenes_completed:
                    return False
            
            return True
        
        def scene_starts_immediately_on_location_enter(self, scene_name):
            return False
        
        def current_scene_starts_immediately_on_location_enter(self):
            return self.scene_starts_immediately_on_location_enter(self.scene)
        
        def list_of_main_scenes(self):
            return []
        
        def face_adjustment(self, face):
            return face
        
        def pose_adjustment(self, pose):
            return pose
        
        def outfit_adjustment(self, outfit):
            return outfit
        
        
        def show_on_stat_screen(self):
            return True
        
        def ypos_adjustment(self):
            return 0
        
        def default_position(self):
            return "left"
        
        def default_face(self):
            return "neutral"
        
        def default_outfit(self):
            return "clothes"
        
        def sfw_outfit(self):
            return self.default_outfit()
        
        def default_pose(self):
            return "default"
        
        def default_say_name(self):
            return "Debug Character"
        
        def update_color(self):
            self.color = self.default_color()
            return
        
        def create_renpy_characters(self):
            self.update_color()
            
            self.c = DynamicCharacter(self.variable_name + ".say_name", color = self.color)
            self.c.actor = self
            
            return
        
        def name_string_with_text(self):
            return "{color=" + self.color + "}" + self.say_name + "{/color}"
        
        def default_color(self):
            return "#ffffff"
        
        def is_fuckable(self):
            return True
        
        def character_select_focused_brightness(self):
            
            return -0.15
        
        def display_scene_stats(self):
            return True
        
        def display_level_stats(self):
            return False
        
        def has_location_navigation_icon(self):
            return True
        
        def points_between_levels(self, first_level, second_level):
            return abs(self.xp_required_for_level(first_level) - self.xp_required_for_level(second_level) )
        
        def points_between_current_and_next_level(self):
            return self.points_between_levels(self.relationship_level, self.relationship_level + 1)
        
        def stat_screen_xp_string(self):
            if self.relationship_level_cap() and self.relationship_level >= self.relationship_level_cap():
                return str(self.points) + " XP"
            else:
                current_xp = min( self.current_xp_relative(), self.xp_required_for_level(self.relationship_level + 1) )
                return str(current_xp) + " / " + str( self.points_between_current_and_next_level() ) + " XP"
        
        def stat_screen_level_string(self):
            text = "Уровень отношений: " + str(self.relationship_level)
            
            if self.relationship_level >= self.relationship_level_cap():
                text += " (Максимальный)"
            
            return text
        
        def total_xp_required_for_next_level(self):
            return self.xp_required_for_level(self.relationship_level + 1)
        
        def xp_required_for_next_level(self):
            return self.xp_required_for_level(self.relationship_level + 1) - self.points
        
        def current_xp_relative(self):
            return max( self.points - self.xp_required_for_level(self.relationship_level), 0 )
        
        def progress_ratio_to_next_level_relative(self):
            if self.relationship_level_cap() and self.relationship_level >= self.relationship_level_cap():
                return 1.0
            
            return self.current_xp_relative() / float(self.points_between_current_and_next_level())
        
        def progress_ratio_to_next_level(self):
            return self.xp_required_for_level(self.relationship_level) / float( self.xp_required_for_level(self.relationship_level + 1) )
        
        def boldness_level_required_for_scene(self, scene_name):
            return 0
        
        def meets_boldness_requirement_for_scene(self, scene_name):
            return store.stats.boldness_level >= self.boldness_level_required_for_scene(scene_name)
        
        def meets_requirement_for_prompt_retry(self, scene_name):
            return self.prompted_scene == scene_name and self.meets_boldness_requirement_for_scene(scene_name)
        
        def place(self):
            self.has_tried_to_place_at_least_once = True
            self.scene_is_low_priority = False
            self.play_scene_even_with_prompted_scene = False
            self.scene = ""
            self.placed_in_a_location = False
            
            self.decide_priority_scene()
            
            if not self.scene:
                self.decide_normal_scene()
            
            if not self.scene:
                self.decide_low_priority_scene()
            
            if not self.placed_in_a_location:
                self.decide_default_location()
            
            return
        
        
        def decide_low_priority_scene(self):
            return
        
        def decide_priority_scene(self):
            return
        
        def decide_normal_scene(self):
            return
        
        def decide_default_location(self):
            return
        
        def add_points(self, quantity, tag = None, force_no_popup = False, minigame = False, yalign = None):
            if yalign is None:
                yalign = add_relationship_boldness_points_yalign
            
            if quantity == 0:
                return
            
            if tag and tag in store.stats.add_boldness_or_relationship_tags:
                return
            
            if minigame and quantity > 0:
                self.minigame_points += quantity
            
            sound = add_relationship_points_sound
            appear_time = add_relationship_points_appear_time
            
            self.points += quantity
            
            if self.relationship_xp_cap() and self.relationship_level_cap():
                self.points = min( self.points, self.xp_required_for_level( self.relationship_level_cap() ) )
            
            leveled_up = self.check_and_set_level()
            
            if tag:
                store.stats.add_boldness_or_relationship_tags.append(tag)
            
            text = "+" + str(quantity) + " к Отношениям с {color=" + self.color + "}" + self.say_name + "{/color}!" 
            
            is_max_level = self.relationship_level_cap() and self.relationship_level >= self.relationship_level_cap()
            
            if leveled_up:
                sound = relationship_level_up_sound
                text += "\nОтношения с {color=" + self.color + "}" + self.say_name + "{/color} перешли на новый Уровень!"
                
                if is_max_level:
                    text += "\n{b}Максимальный Уровень Отношений!{/b}"
            else:
                if is_max_level:
                    text += "\n{b}Максимальный Уровень Отношений!{/b}"
            
            if not force_no_popup:
                renpy.hide_screen("pop_up_general")
                renpy.show_screen("pop_up_general", text, sound, appear_time, yalign = yalign)
            
            return [text, leveled_up, appear_time]
        
        def relationship_xp_cap(self):
            return False
        
        def relationship_level_cap(self):
            return None
        
        def xp_required_for_level(self, level):
            if not level or level == 1:
                return 0
            elif level == 2:
                return 2
            elif level == 3:
                return 7
            elif level == 4:
                return 12
            elif level == 5:
                return 17
            elif level == 6:
                return 99
            elif level == 7:
                return 100
            
            return 999999999
        
        def get_evaluated_level(self):
            passed_level = self.relationship_level
            i = 1
            
            while True:
                test_level = self.relationship_level + i
                
                required_xp = self.xp_required_for_level(test_level)
                
                if required_xp > self.points:
                    break
                else:
                    passed_level = test_level
                
                i += 1
            
            
            return passed_level
        
        def check_and_set_level(self):
            old_level = self.relationship_level
            
            new_level = self.get_evaluated_level()
            
            if self.relationship_level_cap():
                new_level = min(self.relationship_level_cap(), new_level)
            
            if new_level > self.relationship_level:
                self.relationship_level = new_level
            
            return old_level < new_level
        
        def conversation_max(self):
            return 0
        
        def reset(self):
            self.reset_appearance(show_bust = False)
            self.place()
            self.set_conversation()
            
            return
        
        def reset_appearance(self, face = None, pose = None, outfit = None, position = None, show_bust = True):
            self.reset_overlays()
            
            if not face:
                face = self.default_face()
            
            if not pose:
                pose = self.default_pose()
            
            if not position:
                position = self.default_position()
            
            if not outfit:
                outfit = self.default_outfit()
            
            new_appearance = "blush false face " + face + " "
            new_appearance = new_appearance + "pose " + pose + " "
            new_appearance = new_appearance + "position " + position + " "
            new_appearance = new_appearance + "outfit " + outfit
            
            process_character(self, process_string = new_appearance, show_bust = show_bust)
            
            return
        
        def reset_self_and_player(self):
            self.reset_appearance(show_bust = False)
            store.player_character.reset_appearance(show_bust = False)
            return
        
        
        
        def select(self):
            renpy.hide_screen("location_character_select")
            
            
            self.reset_self_and_player()
            
            if self.scene and (not self.prompted_scene or self.play_scene_even_with_prompted_scene):
                renpy.scene('screens')
                if not self.play_scene_even_with_prompted_scene:
                    self.prompted_scene = self.scene
                renpy.call(self.scene)
            else:
                self.display_menu()
            return
        
        def talk(self):
            renpy.call(self.conversation)
            
            return
        
        def display_scene_menu(self):
            self.display_scene_choice_list()
            return
        
        def display_minigame_menu(self):
            renpy.call("character_minigame_menu", self)
            return
        
        def minigame_choice_list(self):
            choice_list = []
            minigames = self.available_minigames()
            
            for minigame in minigames:
                minigame_label = self.minigame_option_label(minigame)
                
                """
                if scene not in store.scenes_completed:
                    minigame_label += " " + self.new_text()
                """
                
                choice_list.append( ( minigame_label, minigame ) )
            
            choice_list.append( ( "Назад", "back" ) )
            
            return choice_list
        
        def scene_choice_list(self):
            choice_list = []
            
            for scene in self.revistable_scenes:
                scene_label = self.revisitable_scene_choice_label(scene)
                
                if not scene_label:
                    continue
                if scene not in store.scenes_completed:
                    scene_label += " " + self.new_text()
                
                choice_list.append( ( scene_label, scene ) )
            
            choice_list.append( ( "Назад", "back" ) )
            
            return choice_list
        
        def display_scene_choice_list(self):
            renpy.call("character_scene_menu", self)
            
            return
        
        def menu_character_select_renpy_label(self):
            return "character_menu"
        
        def revisitable_scene_choice_label(self, scene_name):
            return ""
        
        def menu_character_select_label(self):
            return "Увидеться с " + self.say_name
        
        def display_menu(self):
            renpy.call("character_menu", self)
            return
        
        def available_minigames(self):
            minigame_call_labels = []
            
            return minigame_call_labels
        
        def new_text(self):
            return "(Новое!)"
        
        def has_scene_limit(self):
            return True
        
        def choice_list(self):
            self.reset_appearance(position = store.char_menu_char_position, show_bust = self.display_bust_art_in_character_menu())
            store.player_character.reset_appearance(show_bust = True)
            
            choice_list = []
            
            if self.conversation:
                talk_string = "Говорить"
                
                if self.conversation not in self.conversations_completed:
                    talk_string += " " + self.new_text()
                
                choice_list.append( (talk_string, "talk" ) )
            
            if config.developer:
                choice_list.append( ("(DEBUG) +2 балла и день прогресса", "debug_minigame_instant" ) )
                choice_list.append( ("(DEBUG) +999 баллов и день прогресса", "cheat_points" ) )
            
            if len(self.available_minigames()) > 0:
                choice_list.append( ("Мини-игра", "minigame" ) )
            
            if any(self.revisitable_scene_choice_label(scene_name) for scene_name in self.revistable_scenes):
                revisit_callback = "scene_revisit"
                scene_string = "Повтор сцен"
                if any(self.revisitable_scene_choice_label(scene_name) and scene_name not in store.scenes_completed for scene_name in self.revistable_scenes):
                    scene_string += " " + self.new_text()
                
                if self.has_scene_limit() and self in store.week.characters_had_scene_with_today:
                    scene_string = "{color=f00}" + scene_string + "{/color}" 
                    revisit_callback = "scene_limit_notice"
                
                choice_list.append( (scene_string, revisit_callback ) )
            
            
            choice_list.append( ("Назад", "back" ) )
            
            choice_list = self.add_prompt(choice_list)
            
            return choice_list
        
        def prompt_label(self, scene_name):
            return ""
        
        
        def add_prompt(self, choice_list):
            if self.prompted_scene:
                skip_prompted_scene_option = False
                callback = "retry_prompt_boldness_failure"
                option_label = self.prompt_label(self.prompted_scene)
                
                if self.has_scene_limit() and self in store.week.characters_had_scene_with_today:
                    callback = "scene_limit_notice"
                    option_label = "{color=f00}" + option_label + "{/color}" 
                elif self.meets_requirement_for_prompt_retry(self.prompted_scene):
                    callback = self.prompted_scene + "_sex"
                else:
                    option_label = "{color=f00}" + option_label + "{/color}" 
                
                if len(option_label) == 0:
                    if config.developer and 1 == 2:
                        option_label = "DEBUG MODE: Needs label: " + callback
                    else:
                        self.prompted_scene = ""
                        skip_prompted_scene_option = True
                
                
                if not skip_prompted_scene_option:
                    choice_list.insert(0, ( option_label, callback  ) )
            
            return choice_list
        
        def place_and_set_scene(self, location = None, scene_name = "", level_required = 1, points_required = 0, prerequisite_scene = "", boundary_scene = "", override_scene_limit = False, is_conversation = False, is_low_priority = False):
            if wholesome_mode:
                return
            
            
            if not self.meets_general_prereqs(level_required = level_required, points_required = points_required, prerequisite_scene = prerequisite_scene, boundary_scene = boundary_scene):
                return
            
            if scene_name:
                
                if self.scene:
                    return
                
                
                if self.prompted_scene == scene_name:
                    return
                
                
                if not is_conversation and scene_name in scenes_completed:
                    return
                
                
                if self.has_scene_limit() and not override_scene_limit and self in store.week.characters_had_scene_with_today:
                    return
                
                
                if is_conversation:
                    if scene_name in self.conversations_completed:
                        return
                    
                    self.play_scene_even_with_prompted_scene = True
                
                
                self.scene = scene_name
                
                if is_low_priority:
                    self.scene_is_low_priority = True
            
            if location:
                
                if self.placed_in_a_location:
                    return
                
                self.add_to_location(location)
            
            return
        
        def add_to_location(self, location):
            location.add_character(self)
            self.placed_in_a_location = True
            
            return
        
        
        def meets_general_prereqs(self,  level_required = 1, points_required = 0, prerequisite_scene = "", boundary_scene = ""):
            
            if self.points < points_required:
                return False
            
            if self.relationship_level < level_required:
                return False
            
            
            if prerequisite_scene and prerequisite_scene not in scenes_completed:
                return False
            
            
            if boundary_scene and boundary_scene in scenes_completed:
                return False
            
            return True
        
        
        def reset_conversation(self):
            self.conversation = self.default_conversation()
            self.conversation_pool = []
            self.priority_conversation = ""
            
            return
        
        def default_conversation(self):
            return self.internal_name + "_convo_default"
        
        def test_and_add_conversation_to_pool(self, conversation_name = "", points_required = -1, prerequisite_scene = "", boundary_scene = ""):
            if self.meets_general_prereqs(points_required = points_required, prerequisite_scene = prerequisite_scene, boundary_scene = boundary_scene) and conversation_name not in self.recently_completed_conversations:
                self.conversation_pool.append(conversation_name)
            
            return
        
        def test_and_set_priority_conversation(self, conversation_name = "", points_required = -1, prerequisite_scene = "", boundary_scene = ""):
            if self.priority_conversation:
                return
            
            if self.meets_general_prereqs(points_required = points_required, prerequisite_scene = prerequisite_scene, boundary_scene = boundary_scene) and conversation_name not in self.conversations_completed:
                self.priority_conversation = conversation_name
            
            return
        
        def priority_conversation(self):
            return ""
        
        def set_conversation(self):
            self.reset_conversation()
            self.set_priority_conversation()
            if self.priority_conversation:
                self.conversation = self.priority_conversation
                self.priority_conversation = ""
                
                return
            
            self.set_regular_conversation()
            
            return
        
        def add_conversations_to_pool(self):
            return
        
        def set_priority_conversation(self):
            return
        
        def set_regular_conversation(self):
            self.add_conversations_to_pool()
            self.choose_regular_conversation()
            
            return
        
        def choose_regular_conversation(self):
            if len(self.conversation_pool) > 0:
                self.conversation = random.choice(self.conversation_pool)
            else:
                if len(self.recently_completed_conversations) == 0:
                    self.reset_conversation()
                else:
                    self.recently_completed_conversations = set()
                    self.set_regular_conversation()
            
            return
        
        def is_hidden_on_stat_screen(self):
            return False
        
        def show_scene_completion_only_on_stats(self):
            return False
        
        def num_main_scenes_completed(self):
            def check_main_scene_completed(scene_name):
                return scene_name in store.scenes_completed
            
            return len(filter(check_main_scene_completed, self.list_of_main_scenes()))
        
        
        
        
        def replayable_scene_choice_label(self, scene_name):
            return ""
        
        
        
        
        def image_width(self):
            return 600
        
        def image_height(self):
            return 1080
        
        def icon_image(self, suffix = ""):
            string = "interface/" + self.internal_name.capitalize() + "_Face_Icon" + suffix
            if self.is_hidden_on_stat_screen():
                string = string + "_Hidden"
            string = string + ".png"
            return string
        
        def reset_overlays(self):
            self.overlays = set()
            self.reset_displayed_overlay_filenames()
            return
        
        def reset_displayed_overlay_filenames(self):
            self.displayed_overlay_filenames = set()
            return
        
        def overlay_image_filename(self, overlay_name):
            image_name = self.internal_name + "overlay " + self.overlay_pose(overlay_name) + "_" + self.overlay_outfit(overlay_name) + "_" + overlay_name
            
            return image_name
        
        def overlay_outfit(self, overlay_name):
            return self.outfit
        
        def overlay_pose(self, overlay_name):
            return self.face_pose(self.pose)
        
        def face_pose(self, pose):
            return str(pose)
        
        def blush_pose(self, pose):
            return str(self.face_pose(pose))
        
        def show_face_under_base(self):
            return False
        
        
        def base_image_filename(self):
            return self.internal_name + "base " + str(self.pose) + "_" + self.outfit
        
        def hovered_base_image_filename(self):
            return self.base_image_filename()
        
        def unhovered_base_image_filename(self):
            return self.base_image_filename()
        
        
        def face_image_filename(self):
            return self.internal_name + "face " + self.face_pose(self.pose) + "_" + self.face
        
        
        def blush_image_filename(self):
            if self.blush == True:
                return self.internal_name + "blush " + self.blush_pose(self.pose)
            else:
                return "invisible_char_part"
        
        
        
        def character_select_y(self):
            return 0
        
        def hovered_base_image_filename(self):
            return self.internal_name + "base " + self.hovered_pose() + "_" + self.hovered_outfit()
        
        def unhovered_base_image_filename(self):
            return self.internal_name + "base " + self.unhovered_pose() + "_" + self.unhovered_outfit()
        
        def hovered_face_image_filename(self):
            return self.internal_name + "face " + self.face_pose(self.hovered_pose()) + "_" + self.hovered_face()
        
        def unhovered_face_image_filename(self):
            return self.internal_name + "face " + self.face_pose(self.unhovered_pose()) + "_" + self.unhovered_face()
        
        def hovered_outfit(self):
            return self.default_outfit()
        
        def unhovered_outfit(self):
            return self.default_outfit()
        
        def hovered_pose(self):
            return ""
        
        def unhovered_pose(self):
            return ""
        
        def hovered_face(self):
            return "neutral"
        
        def unhovered_face(self):
            return "neutral"
        
        def character_select_button_crop_left(self):
            return 0
        
        def character_select_button_crop_top(self):
            return 0
        
        def character_select_button_crop_right(self):
            return 0
        
        def character_select_button_crop_bottom(self):
            return 0
        
        
        
        def tag(self):
            return self.internal_name
        
        def base_tag(self):
            return self.tag() + "base"
        
        def face_tag(self):
            return self.tag() + "face"
        
        def blush_tag(self):
            return self.tag() + "blush"
        
        
        def gallery_thumbnail(self):
            return ""
        
        def gallery_bust_art_default_pose(self):
            return ""
        
        def gallery_bust_art_default_face(self):
            return "neutral"
        
        def gallery_bust_art_default_outfit(self):
            return "clothes"
        
        def gallery_bust_art_faces(self):
            return ["neutral"]
        
        def gallery_bust_art_outfits(self):
            return ["clothes"]
        
        def gallery_bust_art_poses(self):
            return []
        
        def gallery_bust_art_has_blush(self):
            return False
        
        def gallery_bust_art_can_be_shown(self):
            return False
        
        def gallery_bust_art_enabled(self):
            return False

label character_menu(char, draw_characters=True):
    window hide
    python:
        if draw_characters:
            if char.display_bust_art_in_character_menu():
                display_multiple_characters([ (player_character, ""), (char, "position " + char_menu_char_position) ] )
            else:
                display_multiple_characters([ (player_character, "") ] )

        renpy.scene('screens')
        renpy.show_screen('hud_zone_select')
        renpy.show_screen('hud')
        chosen_option = renpy.display_menu(char.choice_list())

        if chosen_option == "debug_minigame_instant":
            renpy.call(chosen_option, char)
        elif chosen_option == "cheat_points":
            char.add_points(999, force_no_popup = False)
            narrator("Добавлено 999 очков")
            renpy.call("day_advance_time")
        elif chosen_option == "talk":
            char.talk()
        elif chosen_option == "scene_revisit":
            char.display_scene_menu()
        elif chosen_option == "minigame":
            char.display_minigame_menu()
        elif chosen_option == "retry_prompt_boldness_failure":
            renpy.call(chosen_option, char)
        elif chosen_option == "scene_limit_notice":
            renpy.call(chosen_option, char)
        elif chosen_option == "back":
            renpy.call("location_select", store.stats.current_location)
        else:
            renpy.call(chosen_option)
    return

label character_scene_menu(char):
    python:
        chosen_option = renpy.display_menu(char.scene_choice_list())

    if chosen_option != "back":
        $ renpy.scene('screens')
        $ renpy.call(chosen_option)
    else:
        call character_menu (char, draw_characters=False)

    return

label character_minigame_menu(char):
    python:
        chosen_option = renpy.display_menu(char.minigame_choice_list())

    if chosen_option != "back":
        $ renpy.call(chosen_option, char)
    else:
        call character_menu (char, draw_characters=False)
    return

label character_dream_menu(char):
    python:
        choice_list = []

        for scene in char.replayable_scenes:
            choice_label = char.replayable_scene_choice_label(scene)
            if choice_label:
                choice_list.append( ( choice_label, scene ) )
            elif config.developer:
                choice_list.append( ( "debug mode: needs dream label: " + scene, scene ) )


        choice_list.append( ("Назад", "back") )
        chosen_option = renpy.display_menu(choice_list)

    if chosen_option == "back":
        call day_dream
    else:
        python hide:
            if not persistent.disable_dream_music:
                music_name = "Dreamland.ogg" if random.randint(1, 2) == 1 else "Dreamland_02.ogg"
                music_name = "audio/music/" + music_name
                
                play_music(music_name, fadeout = 1.0)
            renpy.call(chosen_option + "_sex", dream = True)

    return