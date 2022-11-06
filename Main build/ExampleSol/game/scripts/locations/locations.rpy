init -100 python:
    class Location(object):
        def __init__(self):
            self.enabled = self.default_enabled_setting()
            self.hidden = self.default_hidden_setting()
            self.reset()
        
        
        def default_enabled_setting(self):
            return True
        
        def default_hidden_setting(self):
            return False
        
        def set_hidden(self, should_hide):
            self.hidden = should_hide
        
        def is_hidden(self):
            return self.hidden
        
        def should_appear(self):
            return not self.is_hidden()
        
        def is_implemented(self):
            return True
        
        def set_enabled(self, new_is_enabled):
            self.enabled = is_enabled
        
        def enabled_focused_text(self):
            return self.name()
        
        def disabled_focused_text(self):
            if not self.is_implemented():
                return "Coming Soon"
            
            return self.unavailable_focused_text()
        
        def unavailable_focused_text(self):
            return "Unavailable"
        
        def focused_text(self):
            if self.is_enabled():
                return self.enabled_focused_text()
            else:
                return self.disabled_focused_text()
        
        def unfocused_text(self):
            if self.is_enabled():
                return self.enabled_unfocused_text()
            else:
                return self.disabled_unfocused_text()
        
        def enabled_unfocused_text(self):
            return ""
        
        def disabled_unfocused_text(self):
            return ""
        
        def is_enabled(self):
            return self.enabled and self.is_implemented()
        
        def is_disabled(self):
            return not self.is_enabled()
        
        def clicked_action(self):
            if self.is_enabled():
                return self.enabled_action()
            else:
                return self.disabled_action()
        
        def enabled_action(self):
            if self.boldness_requirement() and self.boldness_requirement() > store.stats.boldness_level:
                return self.perform_boldness_fail_action
            
            return self.start
        
        def boldness_requirement(self):
            return None
        
        def perform_boldness_fail_action(self):
            renpy.call(self.boldness_fail_label())
            return
        
        def boldness_fail_label(self):
            return "navigation_boldness_fail"
        
        def disabled_action(self):
            return NullAction()
        
        def reset(self):
            self.characters = []
        
        def start(self, force_music_change = False, morning_wake_lines = False, force_no_music_change = False):
            store.stats.current_location = self
            
            if (store.stats.current_zone != self.zone() and not force_no_music_change) or force_music_change:
                self.decide_and_play_daily_music_queue()
            
            store.stats.current_zone = self.zone()
            
            
            auto_scene_chars = [char for char in self.character_list() if char.current_scene_starts_immediately_on_location_enter()]
            
            if len(auto_scene_chars) > 0:
                auto_scene_chars[0].select()
                return
            
            renpy.call("location_select", self, morning_wake_lines = morning_wake_lines)
            
            return
        
        def empty_action(self):
            renpy.call("empty_location")
            return
        
        def add_character(self, new_character):
            self.characters.append(new_character)
        
        def remove_character(self, new_character):
            self.characters.remove(new_character)
        
        def name(self):
            return ""
        
        def internal_name(self):
            return "placeholder"
        
        def background(self):
            return "bg " + self.internal_name() + "_" + store.week.time_named_for_images().lower()
        
        def background_full_path(self):
            return "images/bg/house/" + self.background() + ".png"
        
        def button_image_filename(self):
            return "navigation_" + self.internal_name()
        
        def button_image_filename_full_path(self):
            return "images/buttons/" + self.button_image_filename() + ".png"
        
        def character_list(self):
            return self.characters
        
        def zone(self):
            return store.home
        
        def day_music_list(self):
            return home_daytime_music_list()
        
        def night_music_list(self):
            return home_evening_music_list()
        
        def decide_and_play_daily_music_queue(self):
            if store.week.time == "day":
                self.play_music_queue(self.day_music_list())
            if store.week.time == "night":
                self.play_music_queue(self.night_music_list())
            
            return
        
        def play_music_queue(self, music_list):
            if music_list:
                play_music_queue(music_valid_candidates(music_list))
            
            return