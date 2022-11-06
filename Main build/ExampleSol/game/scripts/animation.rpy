init python:
    def set_main_animation_speed(speed):
        store.main_animation_speed = speed
        return

    class IA_Animation_Info(object):
        def __init__(self):
            
            
            self.paused = False
            self.section = 0
            self.frame = 0
            self.frame_count = 0
            self.frame_duration_multi = 1.0
            self.loop_start = 0
            self.loop_end = 0
            self.last_frame_st = 0
            self.frame_changed_at_least_once = False
        
        def image_base_path(self):
            return "images/animations/"
        
        def image_filename(self):
            if persistent.sfw_mode:
                return "images/bg/bg black.png"
            return self.image_base_path() + self.image_name() + "_" + str( self.frame ) + ".png"
        
        def frame_duration(self):
            durations = self.frame_durations()
            index = self.frame
            
            if self.frame > len(durations) - 1:
                index = 0
            
            duration = durations[index]
            
            return duration * self.frame_duration_multiplier()
        
        def frame_duration_multiplier(self):
            return self.frame_duration_multi
        
        def last_frame(self):
            return 0
        
        def set_section(self, new_section):
            self.section = new_section
        
        def pause(self):
            self.paused = True
        
        def unpause(self):
            self.paused = False
        
        def set_loop_start_end_from_section(self):
            self.loop_start = self.current_section_data()[0]
            self.loop_end = self.current_section_data()[1]
        
        def increment_section(self):
            new_section = self.section + 1
            
            if new_section > len(self.section_data()) - 1:
                self.section = 0
                self.loop_end = self.last_frame()
            else:
                self.section = new_section
                self.set_loop_start_end_from_section()
        
        def increment_section_button_enabled(self):
            if len( self.section_data() ) <= 1:
                return False
            
            data = self.current_section_data()
            loop_start = data[0]
            loop_end = data[1]
            
            return self.loop_start == loop_start and self.loop_end == loop_end and self.frame >= self.loop_start and self.frame <= self.loop_end
        
        def loop_start(self):
            return self.current_section_data()[0]
        
        def loop_end(self):
            return self.current_section_data()[1]
        
        def current_section_data(self):
            return self.section_data()[self.section]
        
        def fast_speed_multiplier(self):
            return 0.5
        
        def slow_speed_multiplier(self):
            return 1.15
        
        def set_to_fast_speed(self):
            self.set_frame_duration_multiplier(self.fast_speed_multiplier())
        
        def set_to_slow_speed(self):
            self.set_frame_duration_multiplier(self.slow_speed_multiplier())
        
        def set_to_normal_speed(self):
            self.set_frame_duration_multiplier(1.0)
        
        def set_frame_duration_multiplier(self, multiplier, practical = True):
            multi = float(multiplier)
            
            if practical:
                multi = 1/float(multi)
            
            self.frame_duration_multi = multi
        
        def image_name(self):
            return ""
        
        def section_data(self):
            return []
        
        def last_frame(self):
            return 0
        
        def frame_durations(self):
            return []
        
        def frame_sounds(self):
            return []
        
        def sounds_enabled(self):
            return False
        
        def play_sounds(self, frame_changed):
            if self.sounds_enabled() and not self.frame_changed_at_least_once or frame_changed:
                if self.frame <= len(self.frame_sounds()) - 1:
                    sounds = self.frame_sounds()[self.frame]
                    if sounds and len(sounds) > 0:
                        renpy.play ( random.choice(sounds) )
            
            return
        
        def displayable(self, st):
            if self.paused:
                return Image(self.image_filename())
            
            relevant_st = st - self.last_frame_st
            
            frame_changed = False
            
            if relevant_st >= self.frame_duration():
                self.frame += 1
                self.last_frame_st = st
                frame_changed = True
                self.frame_changed_at_least_once = True
            
            if self.frame > self.last_frame():
                self.frame = 0
                self.set_loop_start_end_from_section()
            
            if self.frame > self.loop_end:
                self.frame = self.loop_start
                self.set_loop_start_end_from_section()
            
            if self.frame == 0:
                self.set_loop_start_end_from_section()
            
            self.play_sounds(frame_changed)
            
            return Image(self.image_filename())

    class IA_Animation_Anim_Test_Info(IA_Animation_Info):
        def __init__(self):
            super(IA_Animation_Anim_Test_Info, self).__init__()
            store.animation_infos["main_animation"] = self
        
        def displayable(self, st):
            if self.paused:
                return Image(self.image_filename())
            
            relevant_st = st - self.last_frame_st
            
            if relevant_st >= self.frame_duration():
                test_frame = self.frame + 1
                if test_frame > self.last_frame():
                    self.pause()
                    renpy.call("debug_test_anim_dissolve")
                    return Image(self.image_filename())
            
            return super(IA_Animation_Anim_Test_Info, self).displayable(st)
        
        def image_base_path(self):
            return "images/animations/testanim/"
        
        def image_name(self):
            return "testanim"
        
        def section_data(self):
            return [ ( 0 , 16 ), ( 17 , 51 ) ]
        
        def last_frame(self):
            return 51
        
        def frame_durations(self):
            return [0.1]
        
        def frame_duration_multiplier(self):
            return store.main_animation_speed

    class IA_Animation_Kira_3_Buttjob_Info(IA_Animation_Info):
        def image_base_path(self):
            return "images/animations/kira 3/"
        
        def image_name(self):
            return "kira_3_buttjob_anim"
        
        def section_data(self):
            return [ ( 0 , 6 ) ]
        
        def last_frame(self):
            return 6
        
        def frame_durations(self):
            return [0.12, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08]
        
        def frame_duration_multiplier(self):
            return store.main_animation_speed
        
        def sounds_enabled(self):
            return persistent.enable_sex_sounds
        
        def frame_sounds(self):
            if not persistent.enable_sex_sounds:
                return []
            if store.kira_3_single_smack_sound:
                return [None, ["audio/sounds/smack1.ogg"]]
            else:
                return [None, ["audio/sounds/smack1.ogg", "audio/sounds/smack2.ogg", "audio/sounds/smack3.ogg"]]

    class IA_Animation_Sam_Grind_Info(IA_Animation_Info):
        def image_base_path(self):
            return "images/animations/sam grind/"
        
        def image_name(self):
            return "sam_grind_anim"
        
        def section_data(self):
            return [ ( 0 , 10 ) ]
        
        def last_frame(self):
            return 10
        
        def frame_durations(self):
            return [0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08]
        
        def frame_duration_multiplier(self):
            return store.main_animation_speed

    class IA_Animation_Kira_Titfuck_Info(IA_Animation_Info):
        def __init__(self):
            super(IA_Animation_Kira_Titfuck_Info, self).__init__()
            store.animation_infos["main_animation"] = self
        
        def image_base_path(self):
            return "images/animations/kira titfuck/"
        
        def displayable(self, st):
            relevant_st = st - self.last_frame_st
            
            if self.paused:
                return Image(self.image_filename())
            
            if relevant_st >= self.frame_duration():
                test_frame = self.frame + 1
                
                if test_frame >= 9 and self.section == 1:
                    set_main_animation_speed(1.0)
                
                if test_frame >= self.last_frame():
                    self.pause()
                    if store.kira_titfuck_is_revisit:
                        renpy.call(store.kira_titfuck_cum_segment)
                    else:
                        renpy.call(store.kira_titfuck_cum_segment, store.kira_titfuck_is_dream)
                    
                    return Image(self.image_filename())
            
            return super(IA_Animation_Kira_Titfuck_Info, self).displayable(st)
        
        def frame_sounds(self):
            if not persistent.enable_sex_sounds:
                return []
            return [None, ["audio/sounds/smack1.ogg", "audio/sounds/smack2.ogg", "audio/sounds/smack3.ogg"], None, None, None, None, None, None, None, ["audio/sounds/DSKB1_Ejaculation_04.ogg"]]
        
        
        
        
        
        def image_name(self):
            return "kira_titfuck_anim"
        
        def section_data(self):
            return [ ( 0 , 7 ), (8, 33) ]
        
        def last_frame(self):
            return 33
        
        def frame_durations(self):
            return [0.11, 0.11, 0.11, 0.11, 0.11, 0.11, 0.11, 0.11, 1.5, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08]
        
        def frame_duration_multiplier(self):
            return store.main_animation_speed

    class IA_Animation_Kira_Anal_Info(IA_Animation_Info):
        def __init__(self):
            super(IA_Animation_Kira_Anal_Info, self).__init__()
            store.animation_infos["main_animation"] = self
        
        def image_base_path(self):
            return "images/animations/kira anal/"
        
        def image_name(self):
            return "kira_anal_anim"
        
        def section_data(self):
            return [ ( 0 , 6 ), (0, 0) ]
        
        def last_frame(self):
            return 6
        
        def frame_durations(self):
            return [0.11, 0.11, 0.07, 0.07, 0.07, 0.11, 0.07]
        
        def frame_duration_multiplier(self):
            return store.main_animation_speed
        
        def frame_sounds(self):
            if not persistent.enable_sex_sounds:
                return []
            if store.play_sex_sounds:
                return [["audio/sounds/smack1.ogg", "audio/sounds/smack2.ogg", "audio/sounds/smack3.ogg"]]
            return []
        
        def displayable(self, st):
            if self.frame == 0 and store.kira_anal_anim_pause:
                return Image(self.image_filename())
            
            return super(IA_Animation_Kira_Anal_Info, self).displayable(st)

    class IA_Animation_Simone_Vaginal_Info(IA_Animation_Info):
        def image_base_path(self):
            return "images/animations/simone vaginal/"
        
        def image_name(self):
            return "simone_vaginal_anim"
        
        def section_data(self):
            return [ ( 0 , 7 ) ]
        
        def last_frame(self):
            return 7
        
        def frame_durations(self):
            return [0.09]
        
        def frame_duration_multiplier(self):
            return store.main_animation_speed
        
        def frame_sounds(self):
            if not persistent.enable_sex_sounds:
                return []
            if store.play_sex_sounds:
                return [["audio/sounds/smack1.ogg", "audio/sounds/smack2.ogg", "audio/sounds/smack3.ogg"]]
            return []

    class IA_Animation_Sam_Dream_Info(IA_Animation_Info):
        def image_base_path(self):
            return "images/animations/sam dream/"
        
        def image_name(self):
            return "sam_dream_anim"
        
        def section_data(self):
            return [ ( 0 , 5 ) ]
        
        def last_frame(self):
            return 5
        
        def frame_durations(self):
            return [0.17, 0.17, 0.09, 0.17, 0.17, 0.09]
        
        def frame_duration_multiplier(self):
            return store.main_animation_speed
        
        def frame_sounds(self):
            if not persistent.enable_sex_sounds:
                return []
            if store.play_sex_sounds:
                return []
            return []

    class IA_Animation_Janet_Anal_Info(IA_Animation_Info):
        def image_base_path(self):
            return "images/animations/janet anal/"
        
        def image_name(self):
            return "janet_anal_anim"
        
        def section_data(self):
            return [ ( 0 , 7 ) ]
        
        def last_frame(self):
            return 7
        
        def frame_durations(self):
            return [0.11, 0.11, 0.11, 0.11, 0.11, 0.09, 0.09, 0.04]
        
        def frame_duration_multiplier(self):
            return store.main_animation_speed
        
        def frame_sounds(self):
            if not persistent.enable_sex_sounds:
                return []
            if store.play_sex_sounds:
                return [["audio/sounds/smack1.ogg", "audio/sounds/smack2.ogg", "audio/sounds/smack3.ogg"]]
            return []

    class IA_Animation_Edna_Titfuck_Bikini_Info(IA_Animation_Info):
        def image_base_path(self):
            return "images/animations/edna titfuck bikini/"
        
        def image_name(self):
            return "edna_titfuck_anim"
        
        def section_data(self):
            return [ ( 0 , 8 ) ]
        
        def last_frame(self):
            return 8
        
        def frame_durations(self):
            return [0.11]
        
        def frame_duration_multiplier(self):
            return store.main_animation_speed
        
        def frame_sounds(self):
            if not persistent.enable_sex_sounds:
                return []
            if store.play_sex_sounds:
                return [None, None, None, None, ["audio/sounds/smack1.ogg", "audio/sounds/smack2.ogg", "audio/sounds/smack3.ogg"]]
            return []

    class IA_Animation_Edna_Titfuck_Nude_Info(IA_Animation_Edna_Titfuck_Bikini_Info):
        def image_base_path(self):
            return "images/animations/edna titfuck nude/"
        
        def image_name(self):
            return "edna_titfuck_nude_anim"

    class IA_Animation(renpy.display.layout.DynamicDisplayable):
        def __init__(self, anim_info):
            self.anim_info = anim_info
            function = self.anim_function
            super(IA_Animation, self).__init__(function)
        
        def anim_function(self, st, at):
            return self.anim_info.displayable(st), 0.01

screen test_speed_settings_new:
    vbox:
        xalign 0.97
        yalign 0.3
        spacing 20

        use main_menu_button(text="Slow", action=Function(set_main_animation_speed, 1.5), enabled=main_animation_speed != 1.5)
        use main_menu_button(text="Normal", action=Function(set_main_animation_speed, 1.0), enabled=main_animation_speed != 1.0)
        use main_menu_button(text="Fast", action=Function(set_main_animation_speed, 0.5), enabled=main_animation_speed != 0.5)
        use main_menu_button(text="Next", action=Jump("debug_test_anim_next"))

image anim_nothing_image:
    Null(width = 0, height = 0)

transform main_animation_transform(anim_info, xalign=0.0, yalign=0.0):
    xalign xalign yalign yalign
    IA_Animation(anim_info)

label debug_test_anim:
    show anim_nothing_image as main_animation at main_animation_transform(IA_Animation_Anim_Test_Info())
    call screen test_speed_settings_new

    $ renpy.pause(hard = True)

    return

label debug_test_anim_next:
    $ animation_infos["main_animation"].increment_section()
    $ renpy.pause(hard = True)

    return

label debug_test_anim_dissolve:
    hide main_animation
    with Dissolve(1.5)
    call debug_menu

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
