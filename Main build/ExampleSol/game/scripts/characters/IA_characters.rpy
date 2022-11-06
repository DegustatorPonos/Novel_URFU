init python:
    def scenes_had_titsucking_amount():
        amount = 0
        if "gloryhole_scene_stall" in store.scenes_completed:
            amount += 1
        if "sam_simone_threesome_scene" in store.scenes_completed:
            amount += 1
        if "edna_scene_titfuck" in store.scenes_completed:
            amount += 1
        
        return amount
    def girls_fucked_amount():
        amount = 0
        if "kira_scene_anal" in store.scenes_completed:
            amount += 1
        if "sam_scene_vaginal" in store.scenes_completed:
            amount += 1
        if "julia_scene_vaginal" in store.scenes_completed:
            amount += 1
        if "vicky_scene_vaginal" in store.scenes_completed:
            amount += 1
        if "simone_scene_vaginal" in store.scenes_completed:
            amount += 1
        if "janet_scene_vaginal" in store.scenes_completed:
            amount += 1
        if "gloryhole_scene_vaginal" in store.scenes_completed:
            amount += 1
        
        return amount

    def girls_sexually_played_with_amount():
        amount = 0
        if "kira_scene_3" in store.scenes_completed:
            amount += 1
        if "sam_scene_4" in store.scenes_completed:
            amount += 1
        if "julia_scene_footjob" in store.scenes_completed:
            amount += 1
        if "vicky_titjob_scene" in store.scenes_completed:
            amount += 1
        if "simone_scene_vaginal" in store.scenes_completed:
            amount += 1
        if "janet_scene_blowjob" in store.scenes_completed:
            amount += 1
        if "gloryhole_handjob_scene" in store.scenes_completed:
            amount += 1
        if "edna_scene_handjob" in store.scenes_completed:
            amount += 1
        
        return amount


    class IA_Actor(Actor):
        def __init__(self, internal_name, variable_name):
            Actor.__init__(self, internal_name, variable_name)
            self.update_full_name()
            self.mouth = self.default_mouth()
            self.hat = self.default_hat()
            
            return
        
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
                choice_list.append( ("(DEBUG) +2 очка и день прогресса", "debug_minigame_instant" ) )
                choice_list.append( ("(DEBUG) +999 очков и день прогресса", "cheat_points" ) )
            
            if len(self.available_minigames()) > 0:
                choice_list.append( ("Мини-игра", "minigame" ) )
            
            if any(self.revisitable_scene_choice_label(scene_name) for scene_name in self.revistable_scenes):
                revisit_callback = "scene_revisit"
                scene_string = "Повтор Сцены"
                if any(self.revisitable_scene_choice_label(scene_name) and scene_name not in store.scenes_completed for scene_name in self.revistable_scenes):
                    scene_string += " " + self.new_text()
                elif any(self.extra_scene_new_label_reqs(scene_name) for scene_name in self.revistable_scenes):
                    scene_string += " " + self.new_text()
                
                if self.has_scene_limit() and self in store.week.characters_had_scene_with_today:
                    scene_string = "{color=f00}" + scene_string + "{/color}" 
                    revisit_callback = "scene_limit_notice"
                
                choice_list.append( (scene_string, revisit_callback ) )
            
            
            choice_list.append( ("Назад", "back" ) )
            
            choice_list = self.add_prompt(choice_list)
            
            return choice_list
        
        
        def extra_scene_new_label_reqs(self, scene):
            if (scene == "kira_simone_threesome_scene_revisit_kira" or scene == "kira_simone_threesome_scene_revisit_simone") and "simone_scene_vaginal" in store.scenes_completed and not store.kira_simone_threesome_part_2_done:
                return True
            
            return False
        def scene_choice_list(self):
            choice_list = []
            
            for scene in self.revistable_scenes:
                scene_label = self.revisitable_scene_choice_label(scene)
                
                if not scene_label:
                    continue
                if scene not in store.scenes_completed or self.extra_scene_new_label_reqs(scene):
                    scene_label += " " + self.new_text()
                
                choice_list.append( ( scene_label, scene ) )
            
            choice_list.append( ( "Назад", "back" ) )
            
            return choice_list
        
        def hide_notifications(self):
            return False
        
        def sfw_outfit(self):
            return "clothes"
        
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
                return 24
            elif level == 7:
                return 100
            
            return 999999999
        
        def minigame_option_label(self, call_label):
            if call_label == "minigame_math":
                return "Мини-игра Математика"
            elif call_label == "minigame_typing_review":
                return "Мини-игра Обзор"
            elif call_label == "minigame_racing":
                return "Мини-игра Гонка"
            elif call_label == "minigame_slide_puzzle":
                return "Мини-игра Передвижная головоломка"
            elif call_label == "minigame_repeat_pattern":
                return "Мини-игра Повтори цвет"
            elif call_label == "minigame_reading":
                return "Мини-игра Чтение"
            elif call_label == "minigame_table_tennis":
                return "Мини-игра Теннис"
            
            
            return ""
        
        def create_renpy_characters(self):
            super(IA_Actor, self).create_renpy_characters() 
            
            self.create_renpy_full_name_character()
            return
        
        def racing_icon_losing(self):
            return self.icon_image("_Curious")
        
        def racing_icon_losing_bad(self):
            return self.icon_image("_Embarrassed")
        
        def racing_icon_winning(self):
            return self.icon_image("_Happy")
        
        def racing_icon(self, own_x, opponent_x):
            if not store.minigame_racing_started:
                return self.icon_image()
            
            forced_face = eval("store.minigame_racing_forced_" + self.internal_name + "_face")
            if forced_face:
                return self.icon_image(forced_face)
            
            
            if own_x > int( opponent_x + (opponent_x * .10) ) :
                
                return self.racing_icon_winning()
            elif opponent_x > int( own_x + (own_x * .30) ) :
                return self.racing_icon_losing_bad()
            elif opponent_x > int( own_x + (own_x * .10) ) :
                return self.racing_icon_losing()
            
            return self.icon_image()
        
        def create_renpy_full_name_character(self):
            self.c_full = DynamicCharacter(self.variable_name + ".full_name", color = self.color)
            return
        
        def update_full_name(self):
            self.full_name = self.say_name + " " + store.last_name
            return
        
        
        
        def face_adjustment(self, face):
            if face == "surprise" or face == "shocked" or face == "shock":
                face = "surprised"
            return face
        
        def outfit_adjustment(self, outfit):
            if outfit == "naked":
                outfit = "nude"
            return outfit
        
        def has_separate_mouth(self):
            return False
        
        def mouth_tag(self):
            return self.tag() + "lips"
        
        def mouth_image_filename(self):
            if not self.has_separate_mouth() or not self.mouth:
                return "invisible_char_part"
            
            return self.internal_name + "lips_" + self.mouth + " " + self.face_pose(self.pose) + "_" + self.face
        
        def default_mouth(self):
            return ""
        
        def has_separate_hat(self):
            return False
        
        def hat_tag(self):
            return self.tag() + "hat"
        
        def hat_image_filename(self):
            if not self.has_separate_hat() or not self.hat:
                return "invisible_char_part"
            return self.internal_name + "hat_" + self.hat + " " + self.pose
        
        def default_hat(self):
            return ""
        
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
            
            mouth = self.default_mouth()
            hat = self.default_hat()
            
            new_appearance = "blush false face " + face + " "
            new_appearance = new_appearance + "pose " + pose + " "
            new_appearance = new_appearance + "position " + position + " "
            new_appearance = new_appearance + "outfit " + outfit + " "
            new_appearance = new_appearance + "mouth " + mouth + " "
            new_appearance = new_appearance + "hat " + hat
            
            process_character(self, process_string = new_appearance, show_bust = show_bust)
            
            return
        
        
        def gallery_bust_art_faces(self):
            return [ "angry", "concerned", "curious", "embarrassed", "flirty", "happy", "neutral", "sad"  ]
        
        def gallery_thumbnail(self):
            return "images/bg/kira/kira_1/bg kira_1_looks_back.png"
        
        def gallery_images(self):
            return ["images/bg/kira/kira_1/bg kira_1_looks_back.png"]
        
        def gallery_unlock_scene_thumbnail_requirement(self):
            return "gallery_unlock_scene_thumbnail_requirement"
        
        def gallery_unlock_name_requirement(self):
            return True
        
        def should_appear_in_gallery(self):
            return True
        
        def gallery_bust_art_has_blush(self):
            return True
        
        def gallery_bust_art_can_be_shown(self):
            return True
        
        def gallery_bust_art_enabled(self):
            return True
        
        def kira_simone_threesome_images(self):
            images = []
            if "kira_simone_threesome_scene" in store.scenes_completed:
                images.append("images/bg/others/kira_simone_group/bg SimoneKira_3Some_Smile.png")
                images.append("images/bg/others/kira_simone_group/bg SimoneKira_3Some_TitSquish.png")
                images.append("images/bg/others/kira_simone_group/bg SimoneKira_3Some_PantsOn.png")
                images.append("images/bg/others/kira_simone_group/bg SimoneKira_3Some_PantsOff.png")
                images.append("images/bg/others/kira_simone_group/bg SimoneKira_3Some_LiftBro.png")
                images.append("images/bg/others/kira_simone_group/bg SimoneKira_3Some_NoSaliva.png")
                images.append("images/bg/others/kira_simone_group/bg SimoneKira_3Some_Blowjob.png")
                images.append("images/bg/others/kira_simone_group/bg SimoneKira_3Some_Saliva.png")
                images.append("images/bg/others/kira_simone_group/bg SimoneKira_3Some_BlowjobClose.png")
                images.append("images/bg/others/kira_simone_group/bg SimoneKira_3Some_Cumshot.png")
            
            return images
        
        def foursome_images_kira(self):
            images = []
            if store.kira_simone_threesome_part_2_done or "family_foursome_scene" in store.scenes_completed:
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_GroupFuckNoSam.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg KiraAhego_Internal_Cum.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg KiraAhego_Internal_NoCum.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg KiraAhergo_Internal_Cum_Impreg.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg KiraBlowjob_69.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Threesome_KiraFuck_SimoneWatch.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Threesome_SimoneFuck_KiraWatch.png")
            
            if "family_foursome_scene" in store.scenes_completed:
                if store.did_family_foursome_ff:
                    images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_GroupFuck.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_KiraFuck.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SamFuck.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SimoneFuck.png")
            
            
            return images
        def foursome_images_simone(self):
            images = []
            if store.kira_simone_threesome_part_2_done or "family_foursome_scene" in store.scenes_completed:
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_GroupFuckNoSam.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Simone_UnderBlowjob_Clothed.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Simone_UnderBlowjob_Clothed_Sloppy.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Simone_UnderBlowjob_Nude.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Simone_UnderBlowjob_Nude_Sloppy.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg SimoneAhego_Internal_Cum.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg SimoneAhego_Internal_Cum_Impreg.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg SimoneAhego_Internal_NoCum.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Threesome_KiraFuck_SimoneWatch.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Threesome_SimoneFuck_KiraWatch.png")
            
            if "family_foursome_scene" in store.scenes_completed:
                if store.did_family_foursome_ff:
                    images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_GroupFuck.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_KiraFuck.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SamFuck.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SimoneFuck.png")
            
            return images
        
        def foursome_images_sam(self):
            images = []
            
            if "family_foursome_scene" in store.scenes_completed:
                if store.did_family_foursome_ff:
                    images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_GroupFuck.png")
                
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Sam_DeepBlowjob.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg SamAhego_Internal_Cum.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg SamAhego_Internal_Cum_Impreg.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg SamAhego_Internal_NoCum.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_KiraFuck.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SamFuck.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SimoneFuck.png")
            
            return images
        
        
        def foursome_images_all(self):
            images = []
            if "sam_simone_threesome_scene" or "family_foursome_scene" in store.scenes_completed:
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_GroupFuck.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_GroupFuckNoSam.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_KiraFuck.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SamFuck.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Foursome_SimoneFuck.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg KiraAhego_Internal_Cum.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg KiraAhego_Internal_NoCum.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg KiraAhergo_Internal_Cum_Impreg.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg KiraBlowjob_69.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Sam_DeepBlowjob.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg SamAhego_Internal_Cum.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg SamAhego_Internal_Cum_Impreg.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg SamAhego_Internal_NoCum.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Simone_UnderBlowjob_Clothed.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Simone_UnderBlowjob_Clothed_Sloppy.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Simone_UnderBlowjob_Nude.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Simone_UnderBlowjob_Nude_Sloppy.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg SimoneAhego_Internal_Cum.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg SimoneAhego_Internal_Cum_Impreg.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg SimoneAhego_Internal_NoCum.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Threesome_KiraFuck_SimoneWatch.png")
                images.append("images/bg/others/Kira.Sam.Simone_Foursome/bg Threesome_SimoneFuck_KiraWatch.png")
            
            return images
        
        def sam_simone_threesome_images(self):
            images = []
            if "sam_simone_threesome_scene" in store.scenes_completed:
                images.append("images/bg/others/sam_simone_group/bg sam_simone_group_nate_suck.png")
                if store.did_sam_simone_ff:
                    images.append("images/bg/others/sam_simone_group/bg sam_simone_group_nate_sam_suck.png")
                images.append("images/bg/others/sam_simone_group/bg sam_simone_group_titfuck_sam_watches.png")
                images.append("images/bg/others/sam_simone_group/bg sam_simone_group_titfuck_sam_licked.png")
                images.append("images/bg/others/sam_simone_group/bg sam_simone_group_titfuck_sam_rides.png")
                images.append("images/bg/others/sam_simone_group/bg sam_simone_group_sprawl.png")
                images.append("images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_fuck_simone.png")
                images.append("images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_fuck_sam.png")
                images.append("images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_cum_simone.png")
                images.append("images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_cum_sam.png")
                images.append("images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_aftercum_simone.png")
                images.append("images/bg/others/sam_simone_group/bg sam_simone_group_sprawl_aftercum_sam.png")
            
            return images
        
        def sam_julia_threesome_images(self):
            images = []
            if "sam_julia_threesome_scene" in store.scenes_completed:
                
                if store.did_sam_julia_ff:
                    images.append("images/bg/others/sam_julia_group/bg julia_sam_group_kiss.png")
                    images.append("images/bg/others/sam_julia_group/bg julia_sam_group_kiss_pre.png")
                    images.append("images/bg/others/sam_julia_group/bg julia_sam_group_kiss_cum.png")
                    images.append("images/bg/others/sam_julia_group/bg julia_sam_group_kiss_aftercum.png")
                    images.append("images/bg/others/sam_julia_group/bg julia_sam_group_cumkiss.png")
                    images.append("images/bg/others/sam_julia_group/bg julia_sam_group_cumkiss_pre.png")
                    images.append("images/bg/others/sam_julia_group/bg julia_sam_group_cumkiss_cum.png")
                    images.append("images/bg/others/sam_julia_group/bg julia_sam_group_cumkiss_aftercum.png")
                
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_Blowjob.png")
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_Blowjob_pre.png")
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_Blowjob_cum.png")
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_grind.png")
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_JuliaFuck.png")
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_JuliaFuck_cum.png")
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_JuliaFuck_cum_SamCum.png")
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_SamFuck.png")
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_SamFuck_cum.png")
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_SamFuck_cum_JuliaCum.png")
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_stackup.png")
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_stackup_juliacum.png")
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_stackup_samcum.png")
                images.append("images/bg/others/sam_julia_group/bg julia_sam_group_stackup_bothcum.png")
            
            return images
        
        def finale_images(self):
            images = []
            if "finale_scene" in store.scenes_completed:
                images.append("images/bg/others/Finale Scene/bg party_Edna.png")
                images.append("images/bg/others/Finale Scene/bg party_Janet.png")
                images.append("images/bg/others/Finale Scene/bg party_Kacey.png")
                images.append("images/bg/others/Finale Scene/bg party_Kira.png")
                images.append("images/bg/others/Finale Scene/bg party_Simone.png")
                images.append("images/bg/others/Finale Scene/bg party_Vicky.png")
                
                if store.finale_scene_completed_with_julia_sam:
                    images.append("images/bg/others/Finale Scene/bg party_Sam.png")
                    images.append("images/bg/others/Finale Scene/bg party_Julia.png")
                    images.append("images/bg/others/Finale Scene/bg party_Group_NoCum_NoFap.png")
                    images.append("images/bg/others/Finale Scene/bg party_Group_NoCum_NoFap_cum_all_gallery.png")
                
                else:
                    images.append("images/bg/others/Finale Scene/bg party_Group_NoJS_NoCum_NoFap.png")
                    images.append("images/bg/others/Finale Scene/bg party_Group_NoCum_NoFap_cum_all_gallery_no_js.png")
            
            
            return images

    class Kira(IA_Actor):
        def __init__(self, internal_name = "kira", variable_name = "k"):
            IA_Actor.__init__(self, internal_name, variable_name)
        
        def xp_required_for_level(self, level):
            if not level or level == 1:
                return 0
            
            
            elif level == 2:
                return 2
            
            elif level == 3:
                return 4
            
            elif level == 4:
                return 8
            
            elif level == 5:
                return 13
            
            elif level == 6:
                return 17
            
            elif level == 7:
                return 19
            
            elif level == 8:
                return 21
            
            elif level == 9:
                return 23
            
            elif level == 10:
                return 25
            
            elif level == 11:
                return 28
            
            elif level == 12:
                return 32
            
            elif level == 13:
                return 36
            
            elif level == 14:
                return 40
            
            elif level == 15:
                return 44
            
            elif level == 16:
                return 48
            
            return 999999999
        
        def hide_notifications(self):
            return persistent.hide_kira_notification
        
        def relationship_level_cap(self):
            return 16
        
        def default_pose(self):
            return "armcross"
        
        def default_say_name(self):
            return "Kira"
        
        def variable_name(self):
            return "k"
        
        def default_color(self):
            return "#68BA88"
        
        def character_select_button_crop_left(self):
            return 75
        
        def character_select_button_crop_top(self):
            return 95
        
        def character_select_button_crop_right(self):
            return 85
        
        def scene_starts_immediately_on_location_enter(self, scene_name):
            if scene_name == "kira_scene_6":
                return True
            if scene_name == "kira_scene_8":
                return True
            
            return False
        
        def default_outfit(self):
            if store.finale_scene_completed_with_julia_sam:
                return "nude"
            if store.stats.current_zone == store.home and store.has_fucked_everyone_in_home:
                return "nude"
            
            if not self.prompted_scene and self.scene == "kira_scene_anal":
                return "clothes_underwear"
            
            if self.scene == "kira_convo_10":
                return "underwear"
            
            if (not self.scene or self.play_scene_even_with_prompted_scene) and "kira_scene_tip_blowjob" in store.scenes_completed and self in store.kira_room.character_list():
                return "nude"
            
            if (not self.scene or self.play_scene_even_with_prompted_scene) and "kira_scene_pool_fuck" in store.scenes_completed and self in store.backyard.character_list() and len(store.backyard.character_list()) == 1:
                return "nude"
            
            if (not self.scene or self.play_scene_even_with_prompted_scene) and "kira_scene_6" in store.scenes_completed and self in store.backyard.character_list() and len(store.backyard.character_list()) == 1:
                return "topless_bikini"
            
            
            
            if (not self.scene or self.play_scene_even_with_prompted_scene) and "kira_scene_7" in store.scenes_completed and self in store.hallway.character_list() and len(store.hallway.character_list()) == 1:
                return "underwear_bottomless"
            
            if store.week.time == "day" and ( ("kira_scene_4" in store.scenes_completed and (not self.scene or self.play_scene_even_with_prompted_scene)) or (self.scene == "kira_scene_4" or self.scene == "kira_scene_6" or self.scene == "kira_scene_pool_fuck") ) and self in store.backyard.character_list():
                return "bikini"
            
            if (not self.scene or self.play_scene_even_with_prompted_scene) and "kira_scene_6" in store.scenes_completed and self in store.kira_room.character_list():
                return "underwear"
            
            if (not self.scene or self.play_scene_even_with_prompted_scene) and "kira_scene_5" in store.scenes_completed and self in store.kira_room.character_list():
                return "clothes_underwear"
            
            return "clothes"
        
        def hovered_pose(self):
            return "armsup"
        
        def unhovered_pose(self):
            return "armcross"
        
        def priority_conversation(self):
            return ""
        
        def boldness_level_required_for_scene(self, scene_name):
            if scene_name == "kira_scene_2_seq_1":
                return 2
            elif scene_name == "kira_scene_2_seq_2":
                return 3
            elif scene_name == "kira_scene_3":
                return 4
            elif scene_name == "kira_scene_tip_blowjob":
                return 5
            elif scene_name == "kira_scene_anal":
                return 6
            elif scene_name == "kira_scene_stealth_bj":
                return 7
            elif scene_name == "kira_scene_pool_fuck":
                return 8
            
            return 0
        
        def prompt_label(self, scene_name):
            if scene_name == "kira_scene_1_seq_1":
                return "Хорошо, я могу помочь с упражнениями!"
            elif scene_name == "kira_scene_1_seq_2":
                return "Давай побьём Испытание Приседом!"
            elif scene_name == "kira_scene_2_seq_1":
                return "Хочешь поговорить?"
            elif scene_name == "kira_scene_2_seq_2":
                return "Так какими новостями ты хотела поделиться?"
            elif scene_name == "kira_scene_3":
                return "Так что это за новое упражнение, которое ты пытаешься выполнить?"
            elif scene_name == "kira_scene_tip_blowjob":
                return "Ты хотела сделать мне массаж?"
            elif scene_name == "kira_scene_anal":
                return "Я ... Я хочу трахнуть тебя в задницу!"
            elif scene_name == "kira_scene_stealth_bj":
                return "Хочешь посмотреть фильм?"
            elif scene_name == "kira_scene_pool_fuck":
                return "Да, я присоединюсь к тебе!"
            
            return ""
        
        def decide_low_priority_scene(self):
            if "minigame_racing" not in store.minigames_tried:
                self.place_and_set_scene(scene_name = "minigame_racing_first_time_intro", override_scene_limit = True, is_conversation = True, is_low_priority = True)
            return
        
        def decide_priority_scene(self):
            self.place_and_set_scene(scene_name = "kira_convo_6", prerequisite_scene = "kira_scene_1_seq_2", boundary_scene = "kira_scene_2_seq_1", is_conversation = True)
            self.place_and_set_scene(scene_name = "kira_convo_7", prerequisite_scene = "kira_scene_2_seq_2", boundary_scene = "kira_scene_3", is_conversation = True)
            self.place_and_set_scene(scene_name = "kira_convo_8", prerequisite_scene = "kira_scene_3", boundary_scene = "kira_scene_4", is_conversation = True)
            self.place_and_set_scene(scene_name = "kira_convo_10", prerequisite_scene = "kira_scene_8", boundary_scene = "kira_scene_tip_blowjob", location = kira_room, is_conversation = True)
            self.place_and_set_scene(scene_name = "kira_convo_11", prerequisite_scene = "kira_scene_tip_blowjob", boundary_scene = "kira_scene_9", location = living_room, is_conversation = True)
            
            return
        
        def list_of_main_scenes(self):
            scenes = []
            scenes.append("kira_scene_1_seq_1")
            scenes.append("kira_scene_1_seq_2")
            scenes.append("kira_scene_2_seq_1")
            scenes.append("kira_scene_2_seq_2")
            scenes.append("kira_scene_3")
            scenes.append("kira_scene_4")
            scenes.append("kira_scene_5")
            scenes.append("kira_scene_6")
            scenes.append("kira_scene_7")
            scenes.append("kira_scene_8")
            scenes.append("kira_scene_tip_blowjob")
            scenes.append("kira_scene_anal")
            scenes.append("kira_scene_vaginal")
            scenes.append("kira_scene_stealth_bj")
            scenes.append("kira_scene_pool_fuck")
            
            return scenes
        
        def decide_normal_scene(self):
            self.place_and_set_scene(location = living_room, scene_name = "kira_scene_1_seq_1", level_required = 2)
            self.place_and_set_scene(location = living_room, scene_name = "kira_scene_1_seq_2", prerequisite_scene = "kira_scene_1_seq_1", level_required = 3)
            self.place_and_set_scene(location = hallway, scene_name = "kira_scene_2_seq_1", prerequisite_scene = "kira_scene_1_seq_2", level_required = 4)
            self.place_and_set_scene(location = hallway, scene_name = "kira_scene_2_seq_2", prerequisite_scene = "kira_scene_2_seq_1", level_required = 5)
            self.place_and_set_scene(location = kira_room, scene_name = "kira_scene_3", prerequisite_scene = "kira_scene_2_seq_2", level_required = 6)
            
            if store.week.time == "day":
                self.place_and_set_scene(location = backyard, scene_name = "kira_scene_4", prerequisite_scene = "kira_scene_3", level_required = 7)
            
            self.place_and_set_scene(location = hallway, scene_name = "kira_scene_5", prerequisite_scene = "kira_scene_4", level_required = 8)
            
            if store.week.time == "day":
                self.place_and_set_scene(location = backyard, scene_name = "kira_scene_6", prerequisite_scene = "kira_scene_5", level_required = 9)
            
            self.place_and_set_scene(location = bathroom, scene_name = "kira_scene_8", prerequisite_scene = "kira_scene_7", level_required = 11)
            
            self.place_and_set_scene(location = kira_room, scene_name = "kira_scene_tip_blowjob", prerequisite_scene = "kira_scene_8", level_required = 12)
            
            self.place_and_set_scene(location = kitchen, scene_name = "kira_scene_anal", prerequisite_scene = "kira_scene_tip_blowjob", level_required = 13)
            
            self.place_and_set_scene(location = kira_room, scene_name = "kira_scene_vaginal", prerequisite_scene = "kira_scene_anal", level_required = 14)
            
            self.place_and_set_scene(location = living_room, scene_name = "kira_scene_stealth_bj", prerequisite_scene = "kira_scene_vaginal", level_required = 15)
            
            if store.week.time == "day":
                self.place_and_set_scene(location = backyard, scene_name = "kira_scene_pool_fuck", prerequisite_scene = "kira_scene_stealth_bj", level_required = 16)
            
            return
        
        def decide_default_location(self):
            if store.week.time == "night":
                if "kira_scene_7" in store.scenes_completed and len(store.hallway.character_list()) == 0 and daily_random_event_coin_toss("kira_hallway_night"):
                    self.place_and_set_scene(hallway)
                
                self.place_and_set_scene(location = kira_room)
            else:
                if daily_random_event_coin_toss("kira_room_day"):
                    self.place_and_set_scene(kira_room)
                self.place_and_set_scene(location = backyard)
            
            return
        
        def add_conversations_to_pool(self):
            self.test_and_add_conversation_to_pool(conversation_name = "kira_convo_1", boundary_scene = "kira_scene_2_seq_1")
            self.test_and_add_conversation_to_pool(conversation_name = "kira_convo_2", boundary_scene = "kira_scene_2_seq_1")
            self.test_and_add_conversation_to_pool(conversation_name = "kira_convo_3", boundary_scene = "kira_scene_2_seq_1")
            self.test_and_add_conversation_to_pool(conversation_name = "kira_convo_4", boundary_scene = "kira_scene_2_seq_1")
            self.test_and_add_conversation_to_pool(conversation_name = "kira_convo_5", prerequisite_scene = "sam_scene_1_seq_2", boundary_scene = "kira_scene_3")
            self.test_and_add_conversation_to_pool(conversation_name = "kira_convo_9", prerequisite_scene = "kira_scene_1_seq_2")
            self.test_and_add_conversation_to_pool(conversation_name = "kira_convo_12", prerequisite_scene = "gloryhole_handjob_scene")
            self.test_and_add_conversation_to_pool(conversation_name = "kira_convo_13", prerequisite_scene = "kira_scene_4")
            self.test_and_add_conversation_to_pool(conversation_name = "kira_convo_14", prerequisite_scene = "kira_scene_3")
            self.test_and_add_conversation_to_pool(conversation_name = "kira_convo_15", prerequisite_scene = "kira_scene_8")
            
            return
        
        def set_priority_conversation(self):
            return
        
        def revisitable_scene_choice_label(self, scene_name):
            if scene_name == "kira_scene_1_revisit":
                return "Позволь мне снова считать твои приседания!"
            
            if scene_name == "kira_scene_2_revisit":
                return "Я хочу еще раз взглянуть на твою задницу!"
            
            if scene_name == "kira_scene_3_revisit":
                return "Я хочу сделать упражнение с пенисом на твоей заднице!"
            
            if scene_name == "kira_scene_4_revisit":
                return "Могу я снова увидеть тебя в бикини?"
            
            if scene_name == "kira_scene_6_revisit":
                if store.week.time == "night":
                    return "Хочешь потусоваться у бассейна?"
                else:
                    return "Не возражаешь, если я присоединюсь?"
            
            if scene_name == "kira_scene_8_revisit":
                return "Мы можем еще раз сделать упражнение в ванной?"
            
            if scene_name == "kira_scene_tip_blowjob_revisit":
                return "Я хочу еще один массаж, который ты мне делала."
            
            if scene_name == "kira_scene_anal_revisit":
                if "kira_scene_anal_revisit" in store.scenes_completed:
                    return "Можешь снова сесть на мой член?"
                else:
                    return "Можно я опять трахну тебя в задницу, сестренка?"
            
            if scene_name == "kira_scene_vaginal_revisit":
                
                if "kira_scene_vaginal_revisit" in store.scenes_completed:
                    return "Ещё потрахаемся на кровати?"
                else:
                    return "Давай трахаться на кровати снова!"
            
            if scene_name == "kira_simone_threesome_scene_revisit_kira":
                if "kira_simone_threesome_scene_revisit" in scenes_completed:
                    return "Можешь поднять меня, чтобы Мама снова у меня отсосала?"
                else:
                    return "Мы можем попросить Маму снова мне отсосать?"
            
            if store.week.time != "night" and scene_name == "kira_scene_pool_fuck_revisit":
                if "kira_scene_pool_fuck_revisit" in scenes_completed:
                    return "Давай трахаться в бассейне снова!"
                else:
                    return "Мы можем снова трахнуться в бассейне?"
            
            if scene_name == "family_foursome_scene_revisit_kira":
                return "Я хочу трахнуть тебя, Маму, и [sa.say_name]!"
            
            return ""
        
        def replayable_scene_choice_label(self, scene_name):
            if scene_name == "kira_scene_1_seq_1":
                return "Первый раз, когда я тренировался с" + k.say_name + "..."
            
            if scene_name == "kira_scene_1_seq_2":
                return "В тот раз я отключился, глядя, как " + k.say_name + " делает приседания..."
            
            if scene_name == "kira_scene_2_seq_1":
                return "Когда " + k.say_name + " в первый раз показала мне свою задницу..."
            
            if scene_name == "kira_scene_2_seq_2":
                return "Когда " + k.say_name + " показала мне ее анус..."
            
            if scene_name == "kira_scene_3":
                return "Когда я сделал упражнение пениса на заднице " + k.say_name + "..."
            
            if scene_name == "kira_scene_4":
                return "Когда я уставился на [k.say_name] в её бикини..."
            
            if scene_name == "kira_scene_5":
                return "Когда [k.say_name] сняла шорты передо мной в коридоре..."
            
            if scene_name == "kira_scene_6":
                return "Когда я увидел сиськи [k.say_name] в первый раз..."
            
            if scene_name == "kira_scene_7":
                return "Когда я увидел вагину [k.say_name] поздно ночью перед сном..."
            
            if scene_name == "kira_scene_8":
                return "Когда мой пенис терся о сиськи [k.say_name]..."
            
            if scene_name == "kira_scene_tip_blowjob":
                return "Когда [k.say_name] сделала мне массаж пениса..."
            
            if scene_name == "kira_scene_anal":
                return "Когда я засунул свой член в задницу [k.say_name]..."
            
            if scene_name == "kira_scene_vaginal":
                return "Когда я трахнул [k.say_name] на её кровати..."
            
            if scene_name == "kira_scene_stealth_bj":
                return "Когда [k.say_name] отсосала мне на диване..."
            
            if scene_name == "kira_simone_threesome_scene":
                return "Когда [k.say_name] и мама пришли ко мне..."
            
            if scene_name == "kira_scene_pool_fuck":
                return "Когда я трахнул [k.say_name] у бассейна..."
            
            if scene_name == "family_foursome_scene":
                return "Когда [k.say_name], [sa.say_name], и Мама переспали со мной..."
            
            return ""
        
        def conversation_max(self):
            return 15
        
        def available_minigames(self):
            minigame_call_labels = []
            minigame_call_labels.append("minigame_racing")
            
            return minigame_call_labels
        
        
        def gallery_unlock_scene_thumbnail_requirement(self):
            return "kira_scene_1_seq_1"
        
        def gallery_images(self):
            images = []
            if "kira_scene_1_seq_1" in scenes_completed:
                images.append("images/bg/kira/kira_1/bg kira_1_stretching.png")
                images.append("images/bg/kira/kira_1/bg kira_1_watching.png")
            
            if "kira_scene_1_seq_2" in scenes_completed:
                images.append("images/bg/kira/kira_1/bg kira_1_stretching_2.png")
                images.append("images/bg/kira/kira_1/bg kira_1_tight_ass_shot.png")
                images.append("images/bg/kira/kira_1/bg kira_1_looks_back.png")
            
            if "kira_scene_2_seq_1" in scenes_completed:
                images.append("images/bg/kira/kira_2/bg kira_2_thong_peek.png")
                images.append("images/bg/kira/kira_2/bg kira_2_thong_notices.png")
                images.append("images/bg/kira/kira_2/bg kira_2_shows_ass.png")
            
            if "kira_scene_2_seq_2" in scenes_completed:
                images.append("images/bg/kira/kira_2/bg kira_2_shows_ass_2.png")
                images.append("images/bg/kira/kira_2/bg kira_2_shows_asshole.png")
                images.append("images/bg/kira/kira_2/bg kira_2_grabs_dick.png")
            
            
            if "kira_scene_3" in scenes_completed:
                images.append("images/bg/kira/kira_3/bg kira_3_strip.png")
                images.append("images/bg/kira/kira_3/bg kira_3_pull_down.png")
                images.append("images/bg/kira/kira_3/bg kira_3_pull_back_smile.png")
                images.append("images/bg/kira/kira_3/bg kira_3_pull_back_happy.png")
                images.append("images/bg/kira/kira_3/bg kira_3_pull_back_kitty.png")
                images.append("images/bg/kira/kira_3/bg kira_3_foreskin_pull_kitty.png")
                images.append("images/bg/kira/kira_3/bg kira_3_foreskin_pull_smile.png")
                images.append("images/bg/kira/kira_3/bg kira_3_foreskin_pull_happy.png")
                images.append("images/bg/kira/kira_3/bg kira_3_ready_hot_dog.png")
                images.append("images/bg/kira/kira_3/bg kira_3_ready_hot_dog_xray.png")
                images.append("images/animations/kira 3/kira_3_buttjob_anim_0.png")
                images.append("images/bg/kira/kira_3/bg kira_3_cum.png")
                images.append("images/bg/kira/kira_3/bg kira_3_fingers_asshole.png")
            
            if "kira_scene_8" in scenes_completed:
                images.append("images/bg/kira/kira_7/bg kira_7_nipple_pull.png")
                images.append("images/bg/kira/kira_7/bg kira_7_positions_tits.png")
                images.append("images/animations/kira titfuck/kira_titfuck_anim_0.png")
                images.append("images/animations/kira titfuck/kira_titfuck_anim_20.png")
                images.append("images/bg/kira/kira_7/bg kira_7_cum_slap.png")
            
            if "kira_scene_tip_blowjob" in scenes_completed:
                images.append("images/bg/kira/kira_tip_bj/bg kira_tip_bj_fingers_in_foreskin.png")
                images.append("images/bg/kira/kira_tip_bj/bg kira_tip_bj_pulling_foreskin.png")
                images.append("images/bg/kira/kira_tip_bj/bg kira_tip_bj_tongue_in_foreskin.png")
                images.append("images/bg/kira/kira_tip_bj/bg kira_tip_bj_sucking_tip.png")
                images.append("images/bg/kira/kira_tip_bj/bg kira_tip_bj_facial_no_cum.png")
                images.append("images/bg/kira/kira_tip_bj/bg kira_tip_bj_facial.png")
            
            if "kira_scene_anal" in scenes_completed:
                images.append("images/bg/kira/kira_anal/bg kira_anal_before.png")
                images.append("images/animations/kira anal/kira_anal_anim_2.png")
                images.append("images/bg/kira/kira_anal/bg kira_anal_after.png")
            
            if "kira_scene_vaginal" in scenes_completed:
                images.append("images/bg/kira/kira_vaginal/bg kira_vaginal_close_up.png")
                images.append("images/bg/kira/kira_vaginal/bg kira_vaginal_noblur.png")
                images.append("images/bg/kira/kira_vaginal/bg kira_vaginal_blur.png")
                images.append("images/bg/kira/kira_vaginal/bg kira_vaginal_blur_wince.png")
                images.append("images/bg/kira/kira_vaginal/bg kira_vaginal_noblur_cum.png")
            
            if "kira_scene_stealth_bj" in scenes_completed:
                images.append("images/bg/kira/kira_stealth_bj/bg kira_stealth_bj_blowing.png")
                images.append("images/bg/kira/kira_stealth_bj/bg kira_stealth_bj_blowing_cum.png")
                images.append("images/bg/kira/kira_stealth_bj/bg kira_stealth_bj_open_mouth_cum.png")
                images.append("images/bg/kira/kira_stealth_bj/bg kira_stealth_bj_open_mouth.png")
            
            if "kira_scene_pool_fuck" in scenes_completed:
                images.append("images/bg/kira/Kira Pool/bg kira_poolchair_bikini.png")
                images.append("images/bg/kira/Kira Pool/bg kira_poolchair_nude.png")
                images.append("images/bg/kira/Kira Pool/bg kira_poolkama_bikini.png")
                images.append("images/bg/kira/Kira Pool/bg kira_poolkama_nude.png")
                images.append("images/bg/kira/Kira Pool/bg kira_poolkama_bikini_bubbles.png")
                images.append("images/bg/kira/Kira Pool/bg kira_poolkama_nude_bubbles.png")
                images.append("images/bg/kira/Kira Pool/bg kira_pool_nocum_bikini.png")
                images.append("images/bg/kira/Kira Pool/bg kira_pool_nocum_nude.png")
                images.append("images/bg/kira/Kira Pool/bg kira_pool_cumshot_bikini.png")
                images.append("images/bg/kira/Kira Pool/bg kira_pool_cumshot_nude.png")
                images.append("images/bg/kira/Kira Pool/bg kira_pool_aftercum_bikini.png")
                images.append("images/bg/kira/Kira Pool/bg kira_pool_aftercum_nude.png")
            
            images.extend(self.kira_simone_threesome_images())
            images.extend(self.foursome_images_kira())
            images.extend(self.finale_images())
            
            
            return images
        
        def gallery_bust_art_default_pose(self):
            return "handhip"
        
        def gallery_bust_art_poses(self):
            return ["handhip", "armsup", "armcross"]
        
        def gallery_bust_art_faces(self):
            faces = IA_Actor.gallery_bust_art_faces(self)
            faces.extend(["surprised"])
            return faces
        
        def gallery_bust_art_outfits(self):
            outfits = ["clothes", "bikini"]
            
            if "kira_scene_3" in scenes_completed:
                outfits.extend(["underwear"])
            
            if "kira_scene_5" in scenes_completed:
                outfits.extend(["clothes_underwear"])
            
            if "kira_scene_6" in scenes_completed:
                outfits.extend(["topless_bikini"])
            
            if "kira_scene_7" in scenes_completed:
                outfits.extend(["underwear_bottomless"])
            
            if "kira_scene_8" in scenes_completed:
                outfits.extend(["nude"])
            
            return outfits

    class Simone(IA_Actor):
        def __init__(self, internal_name = "simone", variable_name = "si"):
            IA_Actor.__init__(self, internal_name, variable_name)
        
        def xp_required_for_level(self, level):
            if not level or level == 1:
                return 0
            
            
            elif level == 2:
                return 2
            
            elif level == 3:
                return 4
            
            elif level == 4:
                return 6
            
            elif level == 5:
                return 9
            
            elif level == 6:
                return 11
            
            elif level == 7:
                return 15
            
            elif level == 8:
                return 19
            
            elif level == 9:
                return 23
            
            elif level == 10:
                return 25
            
            elif level == 11:
                return 29
            
            elif level == 12:
                return 33
            
            elif level == 13:
                return 37
            
            elif level == 14:
                return 41
            
            return 999999999
        
        def hide_notifications(self):
            return persistent.hide_simone_notification
        
        def default_pose(self):
            return "handsfront"
        
        def default_say_name(self):
            return "Simone"
        
        def default_color(self):
            return "#a61c00"
        
        def relationship_level_cap(self):
            return 14
        
        def character_select_button_crop_left(self):
            return 85
        
        def character_select_button_crop_top(self):
            return 255
        
        def character_select_button_crop_right(self):
            return 140
        
        def hovered_pose(self):
            return "handsup"
        
        def unhovered_pose(self):
            return "handsfront"
        
        def face_pose(self, pose):
            if self.face == "happy" and pose == "armunder":
                return "armunder"
            if self.face == "surprised" and pose == "armunder":
                return "armunder"
            return "handsup"
        
        def available_minigames(self):
            minigame_call_labels = []
            minigame_call_labels.append("minigame_repeat_pattern")
            minigame_call_labels.append("minigame_slide_puzzle")
            
            return minigame_call_labels
        
        def scene_starts_immediately_on_location_enter(self, scene_name):
            if scene_name == "simone_scene_4":
                return True
            if scene_name == "simone_scene_undressing":
                return True
            if scene_name == "simone_scene_bares_all":
                return True
            if scene_name == "simone_scene_blowjob":
                return True
            if scene_name == "sam_simone_threesome_scene":
                return True
            if scene_name == "family_foursome_scene":
                return True
            
            
            return False
        
        def blush_pose(self, pose):
            if pose == "armunder":
                return "handsup"
            
            return str(self.face_pose(pose))
        
        def conversation_max(self):
            return 15
        
        def list_of_main_scenes(self):
            scenes = []
            scenes.append("simone_scene_1_seq_1")
            scenes.append("simone_scene_yoga_1")
            scenes.append("simone_scene_yoga_2")
            scenes.append("simone_scene_2")
            scenes.append("simone_scene_3")
            scenes.append("simone_scene_4")
            scenes.append("simone_scene_undressing")
            scenes.append("simone_scene_masturbating")
            scenes.append("simone_scene_garden_handjob")
            scenes.append("simone_scene_bares_all")
            scenes.append("simone_scene_blowjob")
            scenes.append("simone_scene_vaginal")
            scenes.append("simone_scene_anal")
            scenes.append("simone_scene_titfuck")
            
            return scenes
        
        def boldness_level_required_for_scene(self, scene_name):
            if scene_name == "simone_scene_2":
                return 3
            if scene_name == "simone_scene_3":
                return 4
            if scene_name == "simone_scene_masturbating":
                return 5
            if scene_name == "simone_scene_garden_handjob":
                return 6
            if scene_name == "simone_scene_vaginal":
                return 7
            if scene_name == "simone_scene_anal":
                return 8
            
            return 0
        
        def decide_low_priority_scene(self):
            if "minigame_slide_puzzle" not in store.minigames_tried and "minigame_repeat_pattern" not in store.minigames_tried:
                self.place_and_set_scene(scene_name = "minigame_slide_puzzle_first_time_intro", override_scene_limit = True, is_conversation = True, is_low_priority = True)
            return
        
        def default_outfit(self):
            if store.finale_scene_completed_with_julia_sam:
                return "nude"
            if store.stats.current_zone == store.home and store.has_fucked_everyone_in_home:
                return "nude"
            
            if ((not self.scene or self.play_scene_even_with_prompted_scene) and "simone_scene_vaginal" in store.scenes_completed and self in store.simone_room.character_list()):
                return "nude"
            
            if store.week.time != "night" and ((not self.scene or self.play_scene_even_with_prompted_scene) and "simone_scene_garden_handjob" in store.scenes_completed and self in store.simone_room.character_list()):
                return "underwear"
            
            if self.scene == "simone_scene_yoga_1" or self.scene == "simone_scene_yoga_2" or self.scene == "simone_scene_titfuck":
                return "yoga"
            if store.week.time == "night" and self.scene == "simone_convo_12":
                return "nightgown"
            if store.week.time == "night" and "simone_scene_masturbating" in scenes_completed:
                return "nightgown"
            if self not in store.week.characters_had_scene_with_today and store.week.time == "day" and "simone_scene_swimsuit" in store.scenes_completed and "simone_scene_garden_handjob" in store.scenes_completed and not self.scene and self in store.backyard.character_list():
                return "swimsuit"
            
            return "clothes"
        
        def decide_normal_scene(self):
            
            if "family_foursome_scene" not in store.scenes_completed and "sam_simone_threesome_scene" in store.scenes_completed and "kira_scene_anal" in store.scenes_completed and "kira_simone_threesome_scene" in store.scenes_completed and store.week.time != "night" and "simone_scene_vaginal" in store.scenes_completed:
                self.place_and_set_scene(location = nate_room, scene_name = "family_foursome_scene", is_conversation = True)
            
            if "sam_simone_threesome_scene" not in store.scenes_completed and store.week.time != "night" and "simone_scene_vaginal" in store.scenes_completed and "sam_scene_blowjob" in store.scenes_completed:
                self.place_and_set_scene(location = nate_room, scene_name = "sam_simone_threesome_scene", is_conversation = True)
            
            self.place_and_set_scene(location = simone_room, scene_name = "simone_scene_yoga_1", level_required = 2)
            self.place_and_set_scene(location = simone_room, scene_name = "simone_scene_yoga_2", level_required = 3)
            self.place_and_set_scene(location = hallway, scene_name = "simone_scene_2", prerequisite_scene = "simone_scene_yoga_2",  level_required = 4)
            self.place_and_set_scene(location = hallway, scene_name = "simone_scene_3", prerequisite_scene = "simone_scene_2", level_required = 5)
            self.place_and_set_scene(location = simone_room, scene_name = "simone_scene_4", prerequisite_scene = "simone_scene_3", level_required = 6)
            
            if store.week.time == "night":
                self.place_and_set_scene(location = simone_room, scene_name = "simone_scene_undressing", prerequisite_scene = "simone_scene_4", level_required = 7, override_scene_limit = True)
            
            if store.week.time != "night":
                self.place_and_set_scene(location = backyard, scene_name = "simone_scene_garden_handjob", prerequisite_scene = "simone_scene_masturbating", level_required = 9)
            
            if store.week.time == "night":
                self.place_and_set_scene(location = simone_room, scene_name = "simone_scene_bares_all", prerequisite_scene = "simone_scene_garden_handjob", level_required = 10, override_scene_limit = True)
            
            if store.week.time != "night":
                self.place_and_set_scene(location = simone_room, scene_name = "simone_scene_blowjob", prerequisite_scene = "simone_scene_bares_all", level_required = 11)
            
            if store.week.time == "night":
                self.place_and_set_scene(location = simone_room, scene_name = "simone_scene_vaginal", prerequisite_scene = "simone_scene_blowjob", level_required = 12)
            
            if store.week.time == "night":
                self.place_and_set_scene(location = simone_room, scene_name = "simone_scene_anal", prerequisite_scene = "simone_scene_vaginal", level_required = 13)
            
            self.place_and_set_scene(location = simone_room, scene_name = "simone_scene_titfuck", prerequisite_scene = "simone_scene_anal", level_required = 14)
            
            return
        
        def decide_priority_scene(self):
            self.place_and_set_scene(scene_name = "simone_convo_6", prerequisite_scene = "simone_scene_1_seq_1", boundary_scene = "simone_scene_2", is_conversation = True)
            self.place_and_set_scene(scene_name = "simone_convo_7", prerequisite_scene = "simone_scene_3", boundary_scene = "simone_scene_4", location = kitchen, is_conversation = True)
            self.place_and_set_scene(scene_name = "simone_convo_12", prerequisite_scene = "simone_scene_masturbating", boundary_scene = "simone_scene_garden_handjob", location = simone_room, is_conversation = True)
            self.place_and_set_scene(scene_name = "simone_convo_13", prerequisite_scene = "simone_scene_garden_handjob", boundary_scene = "simone_scene_bares_all", is_conversation = True)
            
            if not store.has_fucked_everyone_in_home and "family_foursome_scene" not in store.scenes_completed:
                self.place_and_set_scene(scene_name = "simone_convo_15", prerequisite_scene = "kira_simone_threesome_scene", is_conversation = True)
            return
        
        def decide_default_location(self):
            
            if store.week.time == "night":
                self.place_and_set_scene(simone_room)
            else:
                if store.week.time == "day" and "simone_scene_swimsuit" in store.scenes_completed and "simone_scene_garden_handjob" in store.scenes_completed and daily_random_event_coin_toss("simone_swimsuit"):
                    self.place_and_set_scene(backyard)
                else:
                    if "simone_scene_bares_all" in store.scenes_completed and daily_random_event_coin_toss("simone_day_room"):
                        self.place_and_set_scene(simone_room)
                    
                    self.place_and_set_scene(kitchen)
            
            return
        
        def add_conversations_to_pool(self):
            if len(self.conversations_completed) == 0 and "simone_scene_2" not in scenes_completed:
                self.test_and_add_conversation_to_pool(conversation_name = "simone_convo_1", boundary_scene = "simone_scene_2")
            else:
                self.test_and_add_conversation_to_pool(conversation_name = "simone_convo_2", boundary_scene = "simone_scene_2")
                self.test_and_add_conversation_to_pool(conversation_name = "simone_convo_3", boundary_scene = "simone_scene_2")
                self.test_and_add_conversation_to_pool(conversation_name = "simone_convo_4", boundary_scene = "simone_scene_2")
                self.test_and_add_conversation_to_pool(conversation_name = "simone_convo_5", boundary_scene = "simone_scene_2")
                self.test_and_add_conversation_to_pool(conversation_name = "simone_convo_8", prerequisite_scene = "kira_scene_2_seq_1")
                self.test_and_add_conversation_to_pool(conversation_name = "simone_convo_9", prerequisite_scene = "simone_scene_1_seq_1")
                self.test_and_add_conversation_to_pool(conversation_name = "simone_convo_11", prerequisite_scene = "gloryhole_handjob_scene")
            
            return
        
        def set_priority_conversation(self):
            return
        
        def replayable_scene_choice_label(self, scene_name):
            if scene_name == "simone_scene_swimsuit":
                return "Когда я купил купальник для мамы..."
            if scene_name == "simone_scene_yoga_1":
                return "Когда я впервые увидел маму, занимающуюся йогой..."
            if scene_name == "simone_scene_yoga_2":
                return "Когда я отключился, глядя на мамины сиськи, пока она занималась йогой..."
            if scene_name == "simone_scene_1_seq_1":
                return "Когда мама увидела, как я трогаю себя в ванной..."
            if scene_name == "simone_scene_2":
                return "Когда мама пыталась научить меня мастурбировать перед сном..."
            if scene_name == "simone_scene_3":
                return "Когда я мастурбировал, глядя на мамины сиськи в лифчике..."
            if scene_name == "simone_scene_4":
                return "Когда я вошел к маме, когда она была в нижнем белье..."
            if scene_name == "simone_scene_undressing":
                return "Когда я увидел, как мама раздевается..."
            if scene_name == "simone_scene_masturbating":
                return "Когда я увидел, как мама мастурбирует..."
            if scene_name == "simone_scene_garden_handjob":
                return "Когда мама трогала мой пенис в саду..."
            if scene_name == "simone_scene_bares_all":
                return "Когда мама показала мне свое обнаженное тело..."
            if scene_name == "simone_scene_blowjob":
                return "Когда мама сосала мой член..."
            if scene_name == "kira_simone_threesome_scene":
                return "Когда [k.say_name] и мама пришли ко мне..."
            if scene_name == "simone_scene_vaginal":
                return "Когда я трахнул маму на ее кровати..."
            if scene_name == "simone_scene_anal":
                return "Когда я трахнул маму по-собачьи..."
            if scene_name == "simone_scene_titfuck":
                return "Когда мама разрешила мне засунуть член ей между сисек..."
            
            if scene_name == "sam_simone_threesome_scene":
                return "Когда у меня был секс с [sa.say_name] и мамой..."
            
            if scene_name == "family_foursome_scene":
                return "Когда [k.say_name], [sa.say_name], и Мама переспали со мной..."
            
            
            
            return ""
        
        def revisitable_scene_choice_label(self, scene_name):
            if scene_name == "simone_scene_yoga_revisit":
                return ""
            if scene_name == "simone_scene_3_revisit":
                return "Можешь проверить еще раз, чтобы убедиться, что я мастурбирую правильно?"
            if scene_name == "simone_scene_garden_handjob_revisit":
                if "simone_scene_garden_handjob_revisit" in scenes_completed:
                    return "Можешь подрочить мне, мама?"
                else:
                    return "Мы можем сделать это снова в саду?"
            if scene_name == "simone_scene_bares_all_revisit" and si.outfit != "nude":
                return "Ничего, если я посмотрю, как ты переодеваешься?"
            if scene_name == "simone_scene_blowjob_revisit":
                return "Мам, можешь сделать мне минет?"
            
            if scene_name == "kira_simone_threesome_scene_revisit_simone":
                if "kira_simone_threesome_scene_revisit" in scenes_completed:
                    return "Можешь ли ты снова отсосать мне мама в то время, как [k.say_name] держит меня?"
                else:
                    return "Может ли [k.say_name] быть с нами снова для минета?"
            
            if scene_name == "simone_scene_vaginal_revisit":
                if "simone_scene_vaginal_revisit" in scenes_completed:
                    return "Мы можем снова трахаться на кровати, мама?"
                else:
                    return "Можно я снова войду в твою киску, мама?"
            
            if scene_name == "simone_scene_anal_revisit":
                if "simone_scene_anal_revisit" in scenes_completed:
                    return "Давай снова сделаем по-собачьи, мама!"
                else:
                    return "Мы можем сделать это снова по-собачьи, мама?"
            
            if scene_name == "sam_simone_threesome_scene_revisit_simone":
                return "Может ли [sa.say_name] присоединиться к нам для секса снова?"
            
            if scene_name == "simone_scene_titfuck_revisit":
                if "simone_scene_titfuck_revisit" in scenes_completed:
                    return "Пожалуйста, дай мне еще один сиськотрах, мама!"
                else:
                    return "Сделай снова сиськотрах, мама?"
            
            
            if scene_name == "family_foursome_scene_revisit_simone":
                return "Можешь ли ты, [sa.say_name], [k.say_name], трахнуться со мной снова?"
            
            
            return ""
        
        def prompt_label(self, scene_name):
            if scene_name == "simone_scene_2":
                return "Ты хотела поговорить со мной, мама?"
            if scene_name == "simone_scene_3":
                return "Я-я хочу попробовать еще раз, мама."
            if scene_name == "simone_scene_masturbating":
                return "(Я должен проверить маму сегодня вечером)"
            if scene_name == "simone_scene_garden_handjob":
                return "Я буду помогать тебе в саду мама!"
            if scene_name == "simone_scene_vaginal":
                return "Можно я проведу ночь с тобой, Мама?"
            if scene_name == "simone_scene_anal":
                return "Думаю, я знаю, как тебя трахну, Мам."
            
            return ""
        
        def gallery_thumbnail(self):
            return "images/bg/simone/simone_1/bg simone_1_what_is_my_life.png"
        
        def gallery_images(self):
            images = []
            if "simone_scene_1_seq_1" in store.scenes_completed:
                images.append("images/bg/simone/simone_1/bg simone_1_grabs_dick.png")
                images.append("images/bg/simone/simone_1/bg simone_1_fapping.png")
                images.append("images/bg/simone/simone_1/bg simone_1_walks_in_a.png")
                images.append("images/bg/simone/simone_1/bg simone_1_walks_in_b.png")
                images.append("images/bg/simone/simone_1/bg simone_1_what_is_my_life.png")
                images.append("images/bg/simone/simone_1/bg simone_1_returns_to_fapping.png")
                images.append("images/bg/simone/simone_1/bg simone_1_cumming.png")
            
            if "simone_scene_3" in store.scenes_completed:
                images.append("images/bg/simone/simone_2/bg simone_2_removes_top.png")
                images.append("images/bg/simone/simone_2/bg simone_2_top_removed.png")
                images.append("images/bg/simone/simone_2/bg simone_2_fapping_to_bra.png")
                images.append("images/bg/simone/simone_2/bg simone_2_cums_on_breasts.png")
                images.append("images/bg/simone/simone_2/bg simone_2_looks_at_cum.png")
            
            if "simone_scene_undressing" in store.scenes_completed:
                images.append("images/bg/simone/simone_undressing/bg simone_undressing.png")
                images.append("images/bg/simone/simone_undressing/bg simone_undressing_mirror.png")
            
            if "simone_scene_masturbating" in store.scenes_completed:
                images.append("images/bg/simone/simone_masturbation/bg simone_masturbation.png")
                images.append("images/bg/simone/simone_masturbation/bg simone_masturbation_grabbing_crotch.png")
                images.append("images/bg/simone/simone_masturbation/bg simone_masturbation_fapping.png")
                images.append("images/bg/simone/simone_masturbation/bg simone_masturbation_fapping_fast.png")
                images.append("images/bg/simone/simone_masturbation/bg simone_masturbation_about_to_cum.png")
                images.append("images/bg/simone/simone_masturbation/bg simone_masturbation_after_cum.png")
                images.append("images/bg/simone/simone_masturbation/bg simone_masturbation_cum_notices.png")
                images.append("images/bg/simone/simone_masturbation/bg simone_masturbation_cum_on_floor.png")
            
            if "simone_scene_garden_handjob" in store.scenes_completed:
                images.append("images/bg/simone/simone_handjob/bg simone_handjob.png")
                images.append("images/bg/simone/simone_handjob/bg simone_handjob_fast.png")
                images.append("images/bg/simone/simone_handjob/bg simone_handjob_about_to_cum.png")
                images.append("images/bg/simone/simone_handjob/bg simone_handjob_cumming.png")
                images.append("images/bg/simone/simone_handjob/bg simone_handjob_after_cum.png")
            
            if "simone_scene_blowjob" in store.scenes_completed:
                images.append("images/bg/simone/simone_blowjob/bg simone_blowjob_staring_clothed.png")
                images.append("images/bg/simone/simone_blowjob/bg simone_blowjob_staring_clothed_smiling.png")
                images.append("images/bg/simone/simone_blowjob/bg simone_blowjob_staring_nude_smiling.png")
                images.append("images/bg/simone/simone_blowjob/bg simone_blowjob_foreskin_play_clothed.png")
                images.append("images/bg/simone/simone_blowjob/bg simone_blowjob_foreskin_play_nude.png")
                images.append("images/bg/simone/simone_blowjob/bg simone_blowjob_clothed.png")
                images.append("images/bg/simone/simone_blowjob/bg simone_blowjob_nude.png")
                images.append("images/bg/simone/simone_blowjob/bg simone_blowjob_cumming_clothed_skin_up.png")
                images.append("images/bg/simone/simone_blowjob/bg simone_blowjob_cumming_nude_skin_up.png")
                images.append("images/bg/simone/simone_blowjob/bg simone_blowjob_facial_clothed_skin_up.png")
                images.append("images/bg/simone/simone_blowjob/bg simone_blowjob_facial_nude_skin_up.png")
            
            if "simone_scene_vaginal" in store.scenes_completed:
                images.append("images/animations/simone vaginal/simone_vaginal_anim_0.png")
                images.append("images/bg/simone/simone_vaginal/bg simone_vaginal_cum.png")
            
            if "simone_scene_anal" in store.scenes_completed:
                images.append("images/bg/simone/simone_anal/bg simone_doggy.png")
                images.append("images/bg/simone/simone_anal/bg simone_doggy_blur.png")
                images.append("images/bg/simone/simone_anal/bg simone_behind_nocum.png")
                images.append("images/bg/simone/simone_anal/bg simone_behind_ballflop_blur.png")
                images.append("images/bg/simone/simone_anal/bg simone_behind_cum.png")
                images.append("images/bg/simone/simone_anal/bg simone_behind_cumaftermath.png")
            
            if "simone_scene_titfuck" in store.scenes_completed:
                images.append("images/bg/simone/Simone Titfuck/bg simone_suck.png")
                images.append("images/bg/simone/Simone Titfuck/bg simone_jerksuck.png")
                images.append("images/bg/simone/Simone Titfuck/bg simone_titfuck_nocum.png")
                images.append("images/bg/simone/Simone Titfuck/bg simone_titfuck_cum.png")
                images.append("images/bg/simone/Simone Titfuck/bg simone_titfuck_aftercum.png")
            
            images.extend(self.kira_simone_threesome_images())
            images.extend(self.sam_simone_threesome_images())
            images.extend(self.foursome_images_simone())
            images.extend(self.finale_images())
            
            return images
        
        def gallery_unlock_scene_thumbnail_requirement(self):
            return "simone_scene_1_seq_1"
        
        def gallery_unlock_name_requirement(self):
            return True
        
        def gallery_bust_art_default_pose(self):
            return "handsfront"
        
        def gallery_bust_art_poses(self):
            return ["handsfront", "handsup", "armunder"]
        
        def gallery_bust_art_faces(self):
            faces = IA_Actor.gallery_bust_art_faces(self)
            faces.extend(["surprised"])
            return faces
        
        def gallery_bust_art_outfits(self):
            outfits = ["clothes"]
            
            if "simone_scene_swimsuit" in scenes_completed:
                outfits.extend(["swimsuit"])
            
            if "simone_scene_yoga_1" in scenes_completed:
                outfits.extend(["yoga"])
            
            if "simone_scene_4" in scenes_completed:
                outfits.extend(["underwear"])
            
            if "simone_scene_masturbating" in scenes_completed:
                outfits.extend(["nightgown"])
            
            if "simone_scene_bares_all" in scenes_completed:
                outfits.extend(["topless_underwear", "underwear_bottomless", "nude"])
            
            return outfits

    class Sam(IA_Actor):
        def __init__(self, internal_name = "sam", variable_name = "sa"):
            IA_Actor.__init__(self, internal_name, variable_name)
        
        def hide_notifications(self):
            return persistent.hide_sam_notification
        
        def fix_appearance(self):
            if self.outfit == "swimsuit":
                self.outfit = "bikini"
            
            return
        
        def default_pose(self):
            return "handface"
        
        def default_say_name(self):
            return "Sam"
        
        def default_color(self):
            return "#9900ff"
        
        def default_outfit(self):
            if store.finale_scene_completed_with_julia_sam:
                return "nude"
            if store.stats.current_zone == store.home and store.has_fucked_everyone_in_home:
                return "nude"
            
            
            
            
            if self.scene == "sam_scene_vaginal":
                return "nude"
            
            if self.scene == "sam_scene_anal":
                return "nude"
            
            if "sam_scene_3" in store.scenes_completed and (not self.scene or self.scene == "sam_convo_10" or self.scene == "sam_convo_12") and store.stats.current_location and store.stats.current_location == store.sam_room:
                return "nude"
            
            if "sam_scene_1_seq_2" in store.scenes_completed and (not self.scene) and store.stats.current_location and store.stats.current_location == store.sam_room:
                return "underwear"
            
            if store.week.time == "day" and "sam_scene_swimsuit" in store.scenes_completed and (not self.scene or self.play_scene_even_with_prompted_scene) and self in store.backyard.character_list():
                return "bikini"
            
            if ((self.scene == "sam_scene_3") or (not self.scene or self.play_scene_even_with_prompted_scene)) and "sam_scene_1_seq_2" in store.scenes_completed and self in store.sam_room.character_list():
                return "underwear"
            
            return "clothes"
        
        def xp_required_for_level(self, level):
            if not level or level == 1:
                return 0
            
            
            elif level == 2:
                return 2
            
            elif level == 3:
                return 4
            
            elif level == 4:
                return 8
            
            elif level == 5:
                return 13
            
            elif level == 6:
                return 15
            
            elif level == 7:
                return 19
            
            elif level == 8:
                return 23
            
            elif level == 9:
                return 27
            
            elif level == 10:
                return 31
            
            elif level == 11:
                return 35
            
            return 999999999
        
        def scene_starts_immediately_on_location_enter(self, scene_name):
            if scene_name == "sam_scene_blowjob":
                return True
            
            return False
        
        def relationship_level_cap(self):
            return 11
        
        def character_select_button_crop_left(self):
            return 160
        
        def character_select_button_crop_top(self):
            return 465
        
        def character_select_button_crop_right(self):
            return 215
        
        def hovered_pose(self):
            return "handface"
        
        def unhovered_pose(self):
            return "handsbehind"
        
        def conversation_max(self):
            return 12
        
        def decide_low_priority_scene(self):
            if "minigame_math" not in store.minigames_tried:
                self.place_and_set_scene(scene_name = "minigame_math_first_time_intro", override_scene_limit = True, is_conversation = True, is_low_priority = True)
            return
        
        def decide_priority_scene(self):
            self.place_and_set_scene(scene_name = "sam_convo_6", prerequisite_scene = "sam_scene_1_seq_2", boundary_scene = "sam_scene_2_seq_1", is_conversation = True)
            self.place_and_set_scene(scene_name = "sam_convo_7", prerequisite_scene = "sam_scene_2_seq_2", boundary_scene = "sam_scene_3", is_conversation = True)
            self.place_and_set_scene(scene_name = "sam_convo_10", prerequisite_scene = "sam_scene_4", boundary_scene = "sam_scene_vaginal", is_conversation = True)
            self.place_and_set_scene(scene_name = "sam_convo_12", prerequisite_scene = "sam_scene_vaginal", boundary_scene = "sam_scene_blowjob", is_conversation = True)
            
            return
        
        def list_of_main_scenes(self):
            scenes = []
            scenes.append("sam_scene_swimsuit")
            scenes.append("sam_scene_1_seq_1")
            scenes.append("sam_scene_1_seq_2")
            scenes.append("sam_scene_2_seq_1")
            scenes.append("sam_scene_2_seq_2")
            scenes.append("sam_scene_3")
            scenes.append("sam_scene_4")
            scenes.append("sam_scene_vaginal")
            scenes.append("sam_scene_blowjob")
            scenes.append("sam_scene_anal")
            scenes.append("sam_scene_dream")
            
            return scenes
        
        def decide_normal_scene(self):
            self.place_and_set_scene(sam_room, scene_name = "sam_scene_1_seq_1", level_required = 2)
            self.place_and_set_scene(sam_room, scene_name = "sam_scene_1_seq_2", prerequisite_scene = "sam_scene_1_seq_1", level_required = 3)
            self.place_and_set_scene(sam_room, scene_name = "sam_scene_2_seq_1", prerequisite_scene = "sam_scene_1_seq_2", level_required = 4)
            self.place_and_set_scene(sam_room, scene_name = "sam_scene_2_seq_2", prerequisite_scene = "sam_scene_2_seq_1", level_required = 5)
            self.place_and_set_scene(sam_room, scene_name = "sam_scene_3", prerequisite_scene = "sam_scene_2_seq_2", level_required = 6)
            self.place_and_set_scene(sam_room, scene_name = "sam_scene_4", prerequisite_scene = "sam_scene_3", level_required = 7)
            
            if store.week.time == "night":
                self.place_and_set_scene(sam_room, scene_name = "sam_scene_vaginal", prerequisite_scene = "sam_scene_4", level_required = 8)
            
            self.place_and_set_scene(nate_room, scene_name = "sam_scene_blowjob", prerequisite_scene = "sam_scene_vaginal", level_required = 9)
            self.place_and_set_scene(sam_room, scene_name = "sam_scene_anal", prerequisite_scene = "sam_scene_blowjob", level_required = 10)
            
            if store.week.time == "night":
                self.place_and_set_scene(sam_room, scene_name = "sam_scene_dream", prerequisite_scene = "sam_scene_vaginal", level_required = 11)
            
            return
        
        def decide_default_location(self):
            if store.week.time == "day" and "sam_scene_swimsuit" in store.scenes_completed and daily_random_event_coin_toss("sam_swimsuit"):
                self.place_and_set_scene(backyard)
            else:
                self.place_and_set_scene(sam_room)
            
            return
        
        def boldness_level_required_for_scene(self, scene_name):
            if scene_name == "sam_scene_2_seq_1":
                return 2
            elif scene_name == "sam_scene_2_seq_2":
                return 3
            elif scene_name == "sam_scene_4":
                return 4
            elif scene_name == "sam_scene_vaginal":
                return 5
            
            return 0
        
        def prompt_label(self, scene_name):
            if scene_name == "sam_scene_1_seq_1":
                return "Я готов к стриму!"
            elif scene_name == "sam_scene_1_seq_2":
                return "Давай снова запустим стрим!"
            elif scene_name == "sam_scene_2_seq_1":
                return "Хорошо, расскажи мне об обновлениях!"
            elif scene_name == "sam_scene_2_seq_2":
                return "Давай снова будем в нижнем белье."
            elif scene_name == "sam_scene_4":
                return "Ч-что ты хотела узнать о моем пенисе?"
            elif scene_name == "sam_scene_vaginal":
                return "Хорошо, я готов к стриму!"
            
            return ""
        
        def add_conversations_to_pool(self):
            if len(self.conversations_completed) == 0 and "sam_scene_1_seq_1" not in scenes_completed:
                self.test_and_add_conversation_to_pool(conversation_name = "sam_convo_1", boundary_scene = "sam_scene_1_seq_1")
            else:
                self.test_and_add_conversation_to_pool(conversation_name = "sam_convo_2", boundary_scene = "sam_scene_3_seq_1")
                self.test_and_add_conversation_to_pool(conversation_name = "sam_convo_3", boundary_scene = "sam_scene_3_seq_1")
                self.test_and_add_conversation_to_pool(conversation_name = "sam_convo_4", boundary_scene = "sam_scene_3_seq_1")
                self.test_and_add_conversation_to_pool(conversation_name = "sam_convo_5", boundary_scene = "sam_scene_3_seq_1")
                self.test_and_add_conversation_to_pool(conversation_name = "sam_convo_8")
                self.test_and_add_conversation_to_pool(conversation_name = "sam_convo_9")
                self.test_and_add_conversation_to_pool(conversation_name = "sam_convo_11", prerequisite_scene = "gloryhole_handjob_scene")
            
            return
        
        def set_priority_conversation(self):
            return
        
        def replayable_scene_choice_label(self, scene_name):
            if scene_name == "sam_scene_swimsuit":
                return "Когда купил купальник для " + sa.say_name + "..."
            if scene_name == "sam_scene_1_seq_1":
                return "Когда я впервые стримил с " + sa.say_name + "..."
            if scene_name == "sam_scene_1_seq_2":
                return "Когда я впервые увидел грудь " + sa.say_name + "..."
            if scene_name == "sam_scene_2_seq_1":
                return "Когда я и " + sa.say_name + " обнимались в нижнем белье..."
            if scene_name == "sam_scene_2_seq_2":
                return "Когда я и " + sa.say_name + " видели друг друга голыми..."
            if scene_name == "sam_scene_3":
                return "Когда я впервые обнажился на стриме..."
            if scene_name == "sam_scene_4":
                return "Когда я и " + sa.say_name + " тёрли наши интимные места вместе..."
            if scene_name == "sam_scene_vaginal":
                return "Когда я трахнул киску [sa .say_name]..."
            if scene_name == "sam_scene_blowjob":
                return "Когда [sa.say_name] хотела взять мой пенис в рот..."
            if scene_name == "sam_scene_anal":
                return "Когда я вставил свой пенис в попу [sa.say_name]..."
            if scene_name == "sam_scene_dream":
                return "Мечта с [sa.say_name], когда меня было 3..."
            if scene_name == "sam_simone_threesome_scene":
                return "Когда у меня был секс с [sa.say_name] и мамой..."
            if scene_name == "sam_julia_threesome_scene":
                return "Когда [julia.say_name] и [sa.say_name] трахнули меня одновременно..."
            
            if scene_name == "family_foursome_scene":
                return "Когда [k.say_name], [sa.say_name], и Мама переспали со мной..."
            
            return ""
        
        def revisitable_scene_choice_label(self, scene_name):
            if scene_name == "sam_scene_1_revisit":
                return "Я готов к стриму!"
            
            if scene_name == "sam_scene_2_revisit":
                return "Хочешь еще раз взглянуть на мой пенис?"
            
            if scene_name == "sam_scene_3_revisit":
                return "Давай стримить для еще нескольких пожертвований!"
            
            if scene_name == "sam_scene_4_revisit":
                return "Ты хочешь… потереться друг о друга снова?"
            
            if scene_name == "sam_scene_vaginal_revisit":
                if "sam_scene_vaginal_revisit" not in scenes_completed:
                    return "Мы будем трахаться снова?"
                else:
                    return "Мы можем трахаться не в стриме?"
            
            if scene_name == "sam_scene_blowjob_revisit":
                if "sam_scene_blowjob_revisit" not in scenes_completed:
                    return "Можешь снова взять в рот мой член?"
                else:
                    return "Можешь еще отсосать?"
            
            if scene_name == "sam_scene_anal_revisit":
                if "sam_scene_anal_revisit" not in scenes_completed:
                    return "Могу я засунуть свой член тебе в задницу [sa.say_name]?"
                else:
                    return "Давай еще раз трахнемся!"
            
            if scene_name == "sam_scene_swimsuit_revisit":
                if "sam_scene_swimsuit_revisit" in scenes_completed:
                    if "sam_scene_swimsuit_revisit_first_time_has_done_vaginal" in scenes_completed:
                        return "Пойдем трахаться сегодня в бассейн!"
                    elif "sam_scene_swimsuit_revisit_first_time_has_done_grinding" in scenes_completed:
                        return "Хочешь снова поплавать голышом?"
                    else:
                        return "Хочешь поплавать в бассейне сегодня?"
                
                return "Хочешь пойти в бассейн сегодня?"
            
            if scene_name == "sam_simone_threesome_scene_revisit_sam":
                return "Мама должна присоединиться к нам для секса снова!"
            
            if scene_name == "sam_julia_threesome_scene_revisit_sam":
                return "[julia.say_name] хочешь присоединиться к [sa.say_name] снова?"
            
            
            if scene_name == "family_foursome_scene_revisit_sam":
                return "Давай позовём [k.say_name] и Маму, чтобы трахнуться вместе!"
            
            return ""
        
        def available_minigames(self):
            minigame_call_labels = []
            minigame_call_labels.append("minigame_math")
            minigame_call_labels.append("minigame_slide_puzzle")
            
            return minigame_call_labels
        
        def gallery_thumbnail(self):
            return "images/bg/sam/sam_1/bg sam_1_sam_playing.png"
        
        def gallery_images(self):
            images = []
            if "sam_scene_1_seq_1" in scenes_completed:
                images.append("images/bg/sam/sam_1/bg sam_1_playing.png")
                images.append("images/bg/sam/sam_1/bg sam_1_sam_playing.png")
                images.append("images/bg/sam/sam_1/bg sam_1_nate_playing.png")
            
            if "sam_scene_1_seq_2" in scenes_completed:
                images.append("images/bg/sam/sam_1/bg sam_1_sam_playing_nip_slip.png")
                images.append("images/bg/sam/sam_1/bg sam_1_sam_playing_nip_zoom.png")
            
            if "sam_scene_1_seq_2" in scenes_completed:
                images.append("images/bg/sam/sam_2/bg sam_2_hug.png")
                images.append("images/bg/sam/sam_2/bg sam_2_pulls_down_nate_underwear.png")
                images.append("images/bg/sam/sam_2/bg sam_2_pets_penis.png")
                images.append("images/bg/sam/sam_2/bg sam_2_pulls_down_sam_underwear.png")
                images.append("images/bg/sam/sam_2/bg sam_2_puss.png")
                images.append("images/bg/sam/sam_2/bg sam_2_almost_pet_puss.png")
            
            if "sam_scene_4" in scenes_completed:
                images.append("images/bg/sam/sam_3/bg sam_3_touch_eachother.png")
                images.append("images/bg/sam/sam_3/bg sam_3_kiss.png")
                images.append("images/bg/sam/sam_3/bg sam_3_going_to_bed.png")
                images.append("images/bg/sam/sam_3/bg sam_3_kiss_on_bed.png")
                images.append("images/bg/sam/sam_3/bg sam_3_grind.png")
                images.append("images/animations/sam grind/sam_grind_anim_0.png")
                images.append("images/bg/sam/sam_3/bg sam_3_cum.png")
                images.append("images/bg/sam/sam_3/bg sam_3_plays_with_cum.png")
            
            if "sam_scene_vaginal" in scenes_completed:
                images.append("images/bg/sam/sam_vaginal/bg sam_vaginal_spread.png")
                images.append("images/bg/sam/sam_vaginal/bg sam_vaginal_spread_cum.png")
                images.append("images/bg/sam/sam_vaginal/bg sam_vaginal_dick_out.png")
                images.append("images/bg/sam/sam_vaginal/bg sam_vaginal_dick_out_eyes_closed.png")
                images.append("images/bg/sam/sam_vaginal/bg sam_vaginal_dick_in_eyes_closed.png")
                images.append("images/bg/sam/sam_vaginal/bg sam_vaginal_dick_in.png")
                images.append("images/bg/sam/sam_vaginal/bg sam_vaginal_xray.png")
                images.append("images/bg/sam/sam_vaginal/bg sam_vaginal_xray_cum.png")
            
            if "sam_scene_blowjob" in scenes_completed:
                images.append("images/bg/sam/sam_bj/bg sam_bj_lick.png")
                images.append("images/bg/sam/sam_bj/bg sam_bj_foreskin_play.png")
                images.append("images/bg/sam/sam_bj/bg sam_bj_suck.png")
                images.append("images/bg/sam/sam_bj/bg sam_bj_cum.png")
            
            if "sam_scene_anal" in scenes_completed:
                images.append("images/bg/sam/sam_anal/bg sam_anal.png")
                images.append("images/bg/sam/sam_anal/bg sam_anal_blur.png")
                images.append("images/bg/sam/sam_anal/bg sam_anal_cum_blur.png")
                images.append("images/bg/sam/sam_anal/bg sam_anal_cum.png")
            
            if "sam_scene_swimsuit" in scenes_completed:
                images.append("images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_jump_in.png")
            
            if "sam_scene_swimsuit" in scenes_completed and "sam_scene_4" in scenes_completed:
                images.append("images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_jump_in_nude.png")
            
            if "sam_scene_swimsuit" in scenes_completed and "sam_scene_vaginal" in scenes_completed:
                images.append("images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_fuck.png")
                images.append("images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_fuck_blur.png")
                images.append("images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_cum_blur.png")
                images.append("images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_cum.png")
                images.append("images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_fuck_nude.png")
                images.append("images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_fuck_nude_blur.png")
                images.append("images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_cum_nude_blur.png")
                images.append("images/bg/sam/sam_swimsuit/bg sam_scene_swimsuit_cum_nude.png")
            
            if "sam_scene_dream" in scenes_completed:
                images.append("images/animations/sam dream/sam_dream_anim_0.png")
                images.append("images/bg/sam/sam_dream/bg sam_dream_Nonates.png")
                images.append("images/bg/sam/sam_dream/bg sam_dream_Nate1_appear.png")
                images.append("images/bg/sam/sam_dream/bg sam_dream_Nate2_appear.png")
                images.append("images/bg/sam/sam_dream/bg sam_dream_Nate3_appear.png")
                images.append("images/bg/sam/sam_dream/bg sam_dream_cumshot_Nate1.png")
                images.append("images/bg/sam/sam_dream/bg sam_dream_aftercum_Nate1.png")
                images.append("images/bg/sam/sam_dream/bg sam_dream_cumshot_Nate2.png")
                images.append("images/bg/sam/sam_dream/bg sam_dream_aftercum_Nate2.png")
                images.append("images/bg/sam/sam_dream/bg sam_dream_cumshot_Nate3.png")
                images.append("images/bg/sam/sam_dream/bg sam_dream_aftercum_Nate3.png")
                images.append("images/bg/sam/sam_dream/bg sam_dream_cumshot_swallow.png")
                images.append("images/bg/sam/sam_dream/bg sam_dream_cumshot_allgone.png")
            
            images.extend(self.sam_simone_threesome_images())
            images.extend(self.sam_julia_threesome_images())
            images.extend(self.foursome_images_sam())
            images.extend(self.finale_images())
            
            
            return images
        
        def gallery_unlock_scene_thumbnail_requirement(self):
            return "sam_scene_1_seq_1"
        
        def gallery_bust_art_default_pose(self):
            return "handsbehind"
        
        def gallery_bust_art_poses(self):
            return ["handsbehind", "handface", "leaning"]
        
        def gallery_bust_art_faces(self):
            faces = IA_Actor.gallery_bust_art_faces(self)
            
            return faces
        
        def gallery_bust_art_outfits(self):
            outfits = ["clothes"]
            
            if "sam_scene_swimsuit" in scenes_completed:
                outfits.extend(["bikini"])
            
            if "sam_scene_1_seq_1" in scenes_completed:
                outfits.extend(["underwear"])
            
            if "sam_scene_2_seq_2" in scenes_completed:
                outfits.extend(["nude"])
            
            if "sam_scene_3" in scenes_completed:
                outfits.extend(["topless", "bra_bottomless"])
            
            return outfits

    class Nate(IA_Actor):
        def __init__(self, internal_name = "nate", variable_name = "n"):
            IA_Actor.__init__(self, internal_name, variable_name)
        
        def character_select_button_crop_left(self):
            return 129
        
        def character_select_button_crop_top(self):
            return 444
        
        def character_select_button_crop_right(self):
            return 144
        
        def hovered_pose(self):
            return "handfist"
        
        def unhovered_pose(self):
            return "behindhead"
        
        def default_position(self):
            return "right"
        
        def default_outfit(self):
            if store.finale_scene_completed_with_julia_sam:
                return "nudesoft"
            if store.stats.current_zone == store.home and store.has_fucked_everyone_in_home:
                return "nudesoft"
            
            
            if store.stats.current_location and store.stats.current_location != store.nate_room and all(char.prompted_scene != "janet_scene_vaginal" and ("nude" in char.default_outfit() or "bottomless" in char.default_outfit()) for char in store.stats.current_location.character_list()):
                return "nudesoft"
            
            if store.stats.current_location and store.stats.current_location == store.sam_room and len(store.stats.current_location.character_list()) == 1 and store.stats.current_location.character_list()[0] == store.sa and store.sa.default_outfit() == "underwear":
                return "underwear"
            
            return "clothesjacket"
        
        def default_pose(self):
            return "handpocket"
        
        def default_say_name(self):
            return "Nate"
        
        def default_color(self):
            return "#3C6E9A"
        
        def show_on_stat_screen(self):
            return False
        
        def face_pose(self, pose):
            if pose == "handfist":
                return "handpocket"
            if pose == "handhip":
                return "handpocket"
            if pose == "handsdown":
                return "handpocket"
            if pose == "behindhead":
                return "handpocket"
            
            return str(pose)
        
        def fix_appearance(self):
            if self.pose == "handsdown" and (self.outfit == "clothesjacket" or self.outfit == "clothesjacket_hard"):
                self.pose = "handpocket"
            
            if self.pose == "handpocket" and self.outfit != "clothesjacket" and self.outfit != "clothesjacket_hard":
                self.pose = "handsdown"
            
            return
        
        def is_fuckable(self):
            return False
        
        def racing_icon_losing(self):
            return self.icon_image("_Flirty")
        
        def racing_icon_winning(self):
            return self.icon_image()
        
        def gallery_bust_art_default_outfit(self):
            return "clothesjacket"
        
        def gallery_bust_art_default_pose(self):
            return "handpocket"
        
        def gallery_bust_art_poses(self):
            poses = []
            if "clothesjacket" in self.outfit:
                poses.append("handpocket")
            else:
                poses.append("handsdown")
            
            poses.extend(["behindhead", "handfist", "twohandfist"])
            
            return poses
        
        def gallery_bust_art_outfits(self):
            outfits = ["clothesjacket", "clothes", "underwear", "swimsuit"]
            
            if stats.stat_value("times_had_erection") > 0:
                outfits.extend(["clothesjacket_hard", "clothes_hard", "underwear_hard", "swimsuit_hard", "nudesoft", "nudehard"])
            
            return outfits

    class Debug_Character(Nate):
        def __init__(self, internal_name = "nate", variable_name = "n"):
            Nate.__init__(self, internal_name, variable_name)
            
            return
        
        def tag(self):
            return "debug"
        
        def hovered_outfit(self):
            return "clothesjacket"
        
        def unhovered_outfit(self):
            return "clothesjacket"
        
        def hovered_pose(self):
            return "behindhead"
        
        def unhovered_pose(self):
            return "handpocket"
        
        def prompt_label(self, scene_name):
            if scene_name == "debug_scene":
                return "debug scene"
            
            return ""
        
        def decide_normal_scene(self):
            if store.is_school_time:
                self.place_and_set_scene(school_homeroom, scene_name = "debug_scene")
            
            return
        
        def default_conversation(self):
            return ""

    class Nate2(Nate):
        def __init__(self, internal_name = "nate", variable_name = "nate2"):
            Nate.__init__(self, internal_name, variable_name)
            
            return
        
        def base_tag(self):
            return self.tag() + "base2"
        
        def face_tag(self):
            return self.tag() + "face2"
        
        def blush_tag(self):
            return self.tag() + "blush2"

    class Nate3(Nate):
        def __init__(self, internal_name = "nate", variable_name = "nate3"):
            Nate.__init__(self, internal_name, variable_name)
            
            return
        
        def base_tag(self):
            return self.tag() + "base3"
        
        def face_tag(self):
            return self.tag() + "face3"
        
        def blush_tag(self):
            return self.tag() + "blush3"

    class Julia(IA_Actor):
        def __init__(self, internal_name = "julia", variable_name = "julia"):
            IA_Actor.__init__(self, internal_name, variable_name)
            return
        
        def hide_notifications(self):
            return persistent.hide_julia_notification
        
        def default_color(self):
            return "#8822e8"
        
        def character_select_button_crop_left(self):
            return 131
        
        def character_select_button_crop_top(self):
            return 489
        
        def character_select_button_crop_right(self):
            return 149
        
        def default_say_name(self):
            return "Julia"
        
        def default_outfit(self):
            if store.finale_scene_completed_with_julia_sam:
                return "nude"
            if store.stats.current_zone == store.home and store.has_fucked_everyone_in_home:
                return "nude"
            
            if (not self.scene or self.play_scene_even_with_prompted_scene) and "julia_scene_anal" in store.scenes_completed and self in store.bathroom.character_list() and len(store.bathroom.character_list()) == 1:
                return "nude"
            
            return "clothes"
        
        def default_pose(self):
            return "handup"
        
        
        def hovered_pose(self):
            return "handface"
        
        def unhovered_pose(self):
            return "handup"
        
        def is_hidden_on_stat_screen(self):
            if not store.had_julia_arrived_scene:
                return True
            
            return False
        
        def show_on_stat_screen(self):
            
            return True
        
        def display_scene_stats(self):
            if not store.had_julia_arrived_scene:
                return False
            
            return True
        
        
        def decide_default_location(self):
            if not store.had_julia_arrived_scene:
                return
            
            if "julia_scene_anal" in store.scenes_completed and daily_random_event_coin_toss("julia_bathroom"):
                self.place_and_set_scene(bathroom)
            
            self.place_and_set_scene(living_room)
            
            return
        
        def conversation_max(self):
            return 4
        
        def add_conversations_to_pool(self):
            self.test_and_add_conversation_to_pool(conversation_name = "julia_convo_1")
            self.test_and_add_conversation_to_pool(conversation_name = "julia_convo_2")
            self.test_and_add_conversation_to_pool(conversation_name = "julia_convo_3")
            self.test_and_add_conversation_to_pool(conversation_name = "julia_convo_4")
            
            return
        
        def decide_priority_scene(self):
            
            return
        
        def xp_required_for_level(self, level):
            if not level or level == 1:
                return 0
            
            
            elif level == 2:
                return 3
            
            elif level == 3:
                return 7
            
            elif level == 4:
                return 11
            
            elif level == 5:
                return 15
            elif level == 6:
                return 19
            elif level == 7:
                return 23
            elif level == 8:
                return 27
            elif level == 9:
                return 31
            
            return 999999999
        
        def relationship_level_cap(self):
            return 9
        
        def available_minigames(self):
            minigame_call_labels = []
            minigame_call_labels.append("minigame_reading")
            
            return minigame_call_labels
        
        def list_of_main_scenes(self):
            scenes = []
            scenes.append("julia_scene_underwear")
            scenes.append("julia_scene_topless")
            scenes.append("julia_scene_bottomless")
            scenes.append("julia_scene_nude")
            scenes.append("julia_scene_post_nude")
            scenes.append("julia_scene_footjob")
            scenes.append("julia_scene_blowjob")
            scenes.append("julia_scene_vaginal")
            scenes.append("julia_scene_post_vaginal")
            scenes.append("julia_scene_anal")
            
            return scenes
        
        def boldness_level_required_for_scene(self, scene_name):
            if scene_name == "julia_scene_footjob":
                return 7
            if scene_name == "julia_scene_vaginal":
                return 8
            
            
            return 0
        
        def prompt_label(self, scene_name):
            if scene_name == "julia_scene_footjob":
                return "Что ты хотела, чтобы я для тебя сделал?"
            if scene_name == "julia_scene_vaginal":
                return "Я знаю, чего бы ты хотела [julia.say_name]!"
            
            return ""
        
        
        
        
        def scene_starts_immediately_on_location_enter(self, scene_name):
            if scene_name == "julia_scene_topless":
                return True
            if scene_name == "julia_scene_bottomless":
                return True
            if scene_name == "julia_scene_nude":
                return True
            if scene_name == "julia_scene_post_nude":
                return True
            if scene_name == "julia_scene_blowjob":
                return True
            if scene_name == "sam_julia_threesome_scene":
                return True
            
            return False
        
        def decide_normal_scene(self):
            if not store.had_julia_arrived_scene:
                return
            
            if "sam_julia_threesome_scene" not in store.scenes_completed and store.week.time != "night" and "julia_scene_post_vaginal" in store.scenes_completed and "sam_scene_blowjob" in store.scenes_completed:
                self.place_and_set_scene(location = nate_room, scene_name = "sam_julia_threesome_scene", is_conversation = True)
            
            if store.week.time == "day":
                self.place_and_set_scene(location = backyard, scene_name = "julia_scene_topless", prerequisite_scene = "julia_scene_underwear", level_required = 3)
            
            if store.week.time != "day":
                self.place_and_set_scene(location = bathroom, scene_name = "julia_scene_nude", prerequisite_scene = "julia_scene_bottomless", level_required = 5)
            
            self.place_and_set_scene(location = nate_room, scene_name = "julia_scene_post_nude", prerequisite_scene = "julia_scene_nude")
            
            self.place_and_set_scene(location = hallway, scene_name = "julia_scene_footjob", prerequisite_scene = "julia_scene_post_nude", level_required = 6)
            self.place_and_set_scene(location = hallway, scene_name = "julia_scene_blowjob", prerequisite_scene = "julia_scene_footjob", level_required = 7)
            self.place_and_set_scene(location = hallway, scene_name = "julia_scene_vaginal", prerequisite_scene = "julia_scene_blowjob", level_required = 8)
            if store.week.time == "day":
                self.place_and_set_scene(location = living_room, scene_name = "julia_scene_post_vaginal", prerequisite_scene = "julia_scene_vaginal", level_required = 8)
            self.place_and_set_scene(location = hallway, scene_name = "julia_scene_anal", prerequisite_scene = "julia_scene_post_vaginal", level_required = 9)
            
            
            return
        
        def revisitable_scene_choice_label(self, scene_name):
            if scene_name == "julia_scene_footjob_revisit":
                if "julia_scene_footjob_revisit" not in scenes_completed:
                    return "Можешь еще раз потереть мой пенис ногами?"
                else:
                    return "Хочешь снова сделать мне футджоб?"
            
            if scene_name == "julia_scene_blowjob_revisit":
                if "julia_scene_blowjob_revisit" not in scenes_completed:
                    return "Не могла бы ты сосать мой член [julia.say_name]?"
                else:
                    return "Хочешь сделать мне еще один минет?"
            
            if scene_name == "julia_scene_vaginal_revisit":
                if "julia_scene_vaginal_revisit" not in scenes_completed:
                    return "Хочешь, чтобы я трахнул тебя снова [julia.say_name]?"
                else:
                    return "Я снова готов трахаться!"
            
            if scene_name == "julia_scene_anal_revisit":
                if "julia_scene_anal_revisit" not in scenes_completed:
                    return "Ты снова за анальный секс [julia.say_name]?"
                else:
                    return "Я готов к еще одному анальному траху с тобой [julia.say_name]!"
            
            if scene_name == "sam_julia_threesome_scene_revisit_julia":
                return "Хочешь присоединиться ко мне и [sa.say_name] для секса [julia.say_name]?"
            
            return ""
        
        def replayable_scene_choice_label(self, scene_name):
            if scene_name == "julia_scene_underwear":
                return "Когда [julia.say_name] вошла в мою комнату, прося подушку..."
            if scene_name == "julia_scene_topless":
                return "Когда я увидел [julia.say_name] без ее топа в комнате [sa.say_name]..."
            if scene_name == "julia_scene_bottomless":
                return "Когда я увидел [julia.say_name] в коридоре без трусиков..."
            if scene_name == "julia_scene_nude":
                return "Когда [julia.say_name] вышла из душа..."
            if scene_name == "julia_scene_footjob":
                return "Когда [julia.say_name] терла мой член её ногами..."
            if scene_name == "julia_scene_blowjob":
                return "Когда [julia.say_name] сосала мой пенис..."
            if scene_name == "julia_scene_vaginal":
                return "На этот раз [julia.say_name] хотела, чтобы я трахнул ее..."
            if scene_name == "julia_scene_anal":
                return "Когда я трахнул [julia.say_name] в жопу..."
            if scene_name == "sam_julia_threesome_scene":
                return "Когда [julia.say_name] и [sa.say_name] трахнули меня одновременно..."
            
            return ""
        
        def face_adjustment(self, face):
            if face == "aroused":
                return "flirty"
            return face
        
        def gallery_thumbnail(self):
            return "images/bg/julia/JuliaFootjob/bg Julia_Footjob_Soft.png"
        
        def gallery_images(self):
            images = []
            
            if "julia_scene_footjob" in store.scenes_completed:
                images.append("images/bg/julia/JuliaFootjob/bg Julia_Footjob_Soft.png")
                images.append("images/bg/julia/JuliaFootjob/bg Julia_Footjob_HardForeskin_NoBlur.png")
                images.append("images/bg/julia/JuliaFootjob/bg Julia_Footjob_HardForeskin_Blur.png")
                images.append("images/bg/julia/JuliaFootjob/bg Julia_Footjob_Hard_NoBlur.png")
                images.append("images/bg/julia/JuliaFootjob/bg Julia_Footjob_Hard_Blur.png")
                images.append("images/bg/julia/JuliaFootjob/bg Julia_FootjobCum_Hard_Blur.png")
                images.append("images/bg/julia/JuliaFootjob/bg Julia_FootjobAfterCum_Hard_NoBlur.png")
            
            if "julia_scene_blowjob" in store.scenes_completed:
                images.append("images/bg/julia/JuliaBlowjob/bg Julia_Blowjob_Table.png")
                images.append("images/bg/julia/JuliaBlowjob/bg Julia_Blowjob_NoCum.png")
                images.append("images/bg/julia/JuliaBlowjob/bg Julia_Blowjob_AlmostCum.png")
                images.append("images/bg/julia/JuliaBlowjob/bg Julia_Blowjob_Cum.png")
                images.append("images/bg/julia/JuliaBlowjob/bg Julia_Blowjob_SwallowCum.png")
                images.append("images/bg/julia/JuliaBlowjob/bg Julia_Blowjob_SwallowNoCum.png")
            
            if "julia_scene_vaginal" in store.scenes_completed:
                images.append("images/bg/julia/Julia Vaginal/bg Julia_Fuck_Lift.png")
                images.append("images/bg/julia/Julia Vaginal/bg Julia_Fuck_Tip.png")
                images.append("images/bg/julia/Julia Vaginal/bg Julia_Fuck_Tip_Xray.png")
                images.append("images/bg/julia/Julia Vaginal/bg Julia_Fuck__XRay_Cum.png")
                images.append("images/bg/julia/Julia Vaginal/bg Julia_Fuck__XRay_NoCum.png")
                images.append("images/bg/julia/Julia Vaginal/bg Julia_Fuck__AfterCum_Nate.png")
                images.append("images/bg/julia/Julia Vaginal/bg Julia_Fuck__AfterCum_Nate_Xray.png")
                images.append("images/bg/julia/Julia Vaginal/bg Julia_Fuck_AfterCum.png")
            
            if "julia_scene_anal" in store.scenes_completed:
                images.append("images/bg/julia/Julia Anal/bg Julia_Anal_Onfloor.png")
                images.append("images/bg/julia/Julia Anal/bg Julia_Anal_Butthole.png")
                images.append("images/bg/julia/Julia Anal/bg Julia_Anal_Butthole_DickTouch.png")
                images.append("images/bg/julia/Julia Anal/bg Julia_Anal_Butthole_PushIn.png")
                images.append("images/bg/julia/Julia Anal/bg Julia_Anal_Butthole_AllIn.png")
                images.append("images/bg/julia/Julia Anal/bg Julia_Anal_Fuck.png")
                images.append("images/bg/julia/Julia Anal/bg Julia_Anal_Fuck_CumInside.png")
                images.append("images/bg/julia/Julia Anal/bg Julia_Anal_Fuck_Cum.png")
                images.append("images/bg/julia/Julia Anal/bg Julia_Anal_AfterCum.png")
            
            
            images.extend(self.sam_julia_threesome_images())
            images.extend(self.finale_images())
            
            return images
        
        def gallery_unlock_scene_thumbnail_requirement(self):
            return "julia_scene_footjob"
        
        def gallery_unlock_name_requirement(self):
            return store.had_julia_arrived_scene
        
        def gallery_bust_art_default_pose(self):
            return "handup"
        
        def gallery_bust_art_poses(self):
            return ["handup", "handface", "armcross"]
        
        def gallery_bust_art_faces(self):
            faces = IA_Actor.gallery_bust_art_faces(self)
            
            return faces
        
        def gallery_bust_art_outfits(self):
            outfits = ["clothes"]
            
            if "julia_scene_underwear" in store.scenes_completed:
                outfits.extend(["underwear"])
            
            if "julia_scene_topless" in store.scenes_completed:
                outfits.extend(["topless"])
            
            if "julia_scene_bottomless" in store.scenes_completed:
                outfits.extend(["bottomless"])
            
            if "julia_scene_nude" in store.scenes_completed:
                outfits.extend(["nude"])
            
            return outfits
        
        def gallery_bust_art_can_be_shown(self):
            return store.had_julia_arrived_scene

    class Gloryhole_Girl(IA_Actor):
        def __init__(self, internal_name = "gloryhole_girl", variable_name = "gloryhole_girl"):
            IA_Actor.__init__(self, internal_name, variable_name)
            return
        
        def has_location_navigation_icon(self):
            return False
        
        def use_character_select(self):
            return False
        
        def default_conversation(self):
            return ""
        
        def decide_default_location(self):
            if store.week.time == "night":
                self.place_and_set_scene(park)
            
            return
        
        def default_say_name(self):
            return "Kacey"
        
        def default_color(self):
            return "#FDDF7D"
        
        def decide_normal_scene(self):
            self.place_and_set_scene(park, scene_name = "gloryhole_handjob_scene")
            
            if store.week.time == "night" and "gloryhole_handjob_scene" in store.scenes_completed and store.stats.boldness_level >= 5:
                self.place_and_set_scene(park, scene_name = "gloryhole_scene_blowjob")
            
            if store.week.time == "night" and "gloryhole_scene_blowjob" in store.scenes_completed and store.stats.boldness_level >= 6:
                self.place_and_set_scene(park, scene_name = "gloryhole_scene_vaginal")
            
            if store.week.time == "night" and "gloryhole_scene_vaginal" in store.scenes_completed and store.stats.boldness_level >= 7:
                self.place_and_set_scene(park, scene_name = "gloryhole_scene_anal")
            
            if store.week.time == "night" and "gloryhole_scene_anal" in store.scenes_completed and store.stats.boldness_level >= 8:
                self.place_and_set_scene(park, scene_name = "gloryhole_scene_stall")
            
            return
        
        def list_of_main_scenes(self):
            scenes = []
            scenes.append("gloryhole_handjob_scene")
            scenes.append("gloryhole_scene_blowjob")
            scenes.append("gloryhole_scene_vaginal")
            scenes.append("gloryhole_scene_anal")
            scenes.append("gloryhole_scene_stall")
            return scenes
        
        def show_scene_completion_only_on_stats(self):
            return True
        
        def show_on_stat_screen(self):
            return True
        
        def is_hidden_on_stat_screen(self):
            if not "gloryhole_handjob_scene" in store.scenes_completed:
                return True
            
            return False
        
        def display_bust_art_in_character_menu(self):
            return False
        
        def scene_starts_immediately_on_location_enter(self, scene_name):
            if scene_name == "gloryhole_handjob_scene":
                return True
            if scene_name == "gloryhole_scene_blowjob":
                return True
            if scene_name == "gloryhole_scene_vaginal":
                return True
            if scene_name == "gloryhole_scene_anal":
                return True
            if scene_name == "gloryhole_scene_stall":
                return True
            
            return False
        
        def display_scene_stats(self):
            return "gloryhole_handjob_scene" in store.scenes_completed
        
        def icon_image(self, suffix = ""):
            string = "interface/" + "Kacey" + "_Face_Icon" + suffix
            if "gloryhole_scene_stall" not in store.scenes_completed:
                string = string + "_Hidden"
            string = string + ".png"
            return string
        
        
        
        def revisitable_scene_choice_label(self, scene_name):
            if scene_name == "gloryhole_handjob_scene_revisit":
                return "Можешь еще раз потрогать мой пенис?"
            if scene_name == "gloryhole_scene_blowjob_revisit":
                return "Можешь отсосать мне еще раз?"
            if scene_name == "gloryhole_scene_vaginal_revisit":
                return "Могу я снова засунуть в тебя свой член?"
            if scene_name == "gloryhole_scene_anal_revisit":
                return "Могу я снова засунуть свой член тебе в задницу?"
            if scene_name == "gloryhole_scene_stall_revisit":
                return "Я снова вхожу в твою кабинку [gloryhole_girl.say_name]!"
            
            return ""
        
        def replayable_scene_choice_label(self, scene_name):
            if scene_name == "gloryhole_handjob_scene":
                return "Когда [gloryhole_girl.say_name] коснулась моего пениса через отверстие в туалете в парке..."
            if scene_name == "gloryhole_scene_blowjob":
                return "Когда [gloryhole_girl.say_name] сосала мне в туалете..."
            if scene_name == "gloryhole_scene_vaginal":
                return "На этот раз я трахнул [gloryhole_girl.say_name] на ее день рождения..."
            if scene_name == "gloryhole_scene_anal":
                return "Когда [gloryhole_girl.say_name] хотела, чтобы я трахнул её в зад..."
            if scene_name == "gloryhole_scene_stall":
                return "На этот раз я пошел в кабинку [gloryhole_girl.say_name]..."
            
            return ""
        
        def menu_character_select_renpy_label(self):
            return "gloryhole_girl_character_menu"
        
        def display_menu(self):
            renpy.call("gloryhole_girl_character_menu")
            return
        
        def gallery_thumbnail(self):
            return "images/bg/others/gloryhole_g/bg gloryhole_handjob_stall_opaque.png"
        
        def gallery_unlock_scene_thumbnail_requirement(self):
            return "gloryhole_handjob_scene"
        
        def gallery_unlock_name_requirement(self):
            return "gloryhole_handjob_scene" in store.scenes_completed
        
        def gallery_images(self):
            images = []
            if "gloryhole_handjob_scene" in scenes_completed:
                images.append("images/bg/others/gloryhole_g/bg gloryhole.png")
                images.append("images/bg/others/gloryhole_g/bg gloryhole_sticks_dick_through.png")
                images.append("images/bg/others/gloryhole_g/bg gloryhole_touches_dick.png")
                images.append("images/bg/others/gloryhole_g/bg gloryhole_handjob.png")
                images.append("images/bg/others/gloryhole_g/bg gloryhole_handjob_stall_opaque.png")
                images.append("images/bg/others/gloryhole_g/bg gloryhole_handjob_stall_transparent.png")
                images.append("images/bg/others/gloryhole_g/bg gloryhole_handjob_cum.png")
            
            if "gloryhole_scene_blowjob" in scenes_completed:
                images.append("images/bg/others/Kacey_Blowjob/bg Kacey_Blowjob_Mouth_NoCum.png")
                images.append("images/bg/others/Kacey_Blowjob/bg Kacey_Blowjob_ThroughWall.png")
                images.append("images/bg/others/Kacey_Blowjob/bg Kacey_Blowjob_ThroughWall_X-Ray.png")
                images.append("images/bg/others/Kacey_Blowjob/bg Kacey_Blowjob_Cumshot_Explode.png")
                images.append("images/bg/others/Kacey_Blowjob/bg Kacey_Blowjob_Cumshot.png")
                images.append("images/bg/others/Kacey_Blowjob/bg Kacey_Blowjob_Mouth_Cum.png")
            
            if "gloryhole_scene_vaginal" in scenes_completed:
                images.append("images/bg/others/Kacey Vaginal/bg Kacey_Vaginal_Penis.png")
                images.append("images/bg/others/Kacey Vaginal/bg kacey_vaginal_tip.png")
                images.append("images/bg/others/Kacey Vaginal/bg kacey_vaginal_nocum.png")
                images.append("images/bg/others/Kacey Vaginal/bg kacey_vaginal_cum.png")
                images.append("images/bg/others/Kacey Vaginal/bg kacey_vaginal_spread_cum.png")
                images.append("images/bg/others/Kacey Vaginal/bg kacey_vaginal_tip_cum.png")
            
            if "gloryhole_scene_anal" in scenes_completed:
                images.append("images/bg/others/Kacey Anal/bg Kacey_Anal_Gloryhole.png")
                images.append("images/bg/others/Kacey Anal/bg Kacey_Anal_Insert.png")
                images.append("images/bg/others/Kacey Anal/bg Kacey_Anal_Insert_naked.png")
                images.append("images/bg/others/Kacey Anal/bg Kacey_Anal_Internal_nocum.png")
                images.append("images/bg/others/Kacey Anal/bg Kacey_Anal_Fuck_clothed_nocum.png")
                images.append("images/bg/others/Kacey Anal/bg Kacey_Anal_Fuck_naked_nocum.png")
                images.append("images/bg/others/Kacey Anal/bg Kacey_Anal_Fuck_clothed_cum.png")
                images.append("images/bg/others/Kacey Anal/bg Kacey_Anal_Fuck_naked_cum.png")
                images.append("images/bg/others/Kacey Anal/bg Kacey_Anal_Internal_cum.png")
                images.append("images/bg/others/Kacey Anal/bg Kacey_Anal_Gloryhole_Cum.png")
            
            if "gloryhole_scene_stall" in scenes_completed:
                images.append("images/bg/others/Kacey_Stall/bg Kacey_Stall_Fuck.png")
                images.append("images/bg/others/Kacey_Stall/bg Kacey_Stall_TitSuck.png")
                images.append("images/bg/others/Kacey_Stall/bg Kacey_Stall_Fuck_NoCum.png")
                images.append("images/bg/others/Kacey_Stall/bg Kacey_Stall_Fuck_Blur_NoCum.png")
                images.append("images/bg/others/Kacey_Stall/bg Kacey_Stall_Fuck_Blur_Cum.png")
                images.append("images/bg/others/Kacey_Stall/bg Kacey_Stall_Fuck_Blur_Cum_Impreg.png")
                images.append("images/bg/others/Kacey_Stall/bg Kacey_Stall_Fuck_Cum.png")
                images.append("images/bg/others/Kacey_Stall/bg Kacey_Stall_Fuck_Cum_Impreg.png")
            
            images.extend(self.finale_images())
            return images
        
        def gallery_bust_art_can_be_shown(self):
            return False
        
        def hide_notifications(self):
            return persistent.hide_kacey_notification


    class Vicky(IA_Actor):
        def __init__(self, internal_name = "vicky", variable_name = "vicky"):
            IA_Actor.__init__(self, internal_name, variable_name)
            return
        
        def has_location_navigation_icon(self):
            return False
        
        def use_character_select(self):
            return False
        
        def default_conversation(self):
            return ""
        
        def decide_default_location(self):
            if "vicky_titjob_scene" in store.scenes_completed:
                self.place_and_set_scene(vicky_apartment)
            
            return
        
        def default_say_name(self):
            return "Vicky"
        
        def default_color(self):
            return "#f9a602"
        
        def decide_normal_scene(self):
            if store.had_vicky_intro_scene:
                self.place_and_set_scene(vicky_apartment, scene_name = "vicky_tease_scene")
            
            if "vicky_tease_scene" in store.scenes_completed and store.stats.boldness_level >= 5:
                self.place_and_set_scene(vicky_apartment, scene_name = "vicky_fondle_scene")
            
            if "vicky_fondle_scene" in store.scenes_completed and store.stats.boldness_level >= 6 and minigame_typing_times_succeeded_since_last_vicky_meeting >= 1:
                self.place_and_set_scene(nate_room, scene_name = "vicky_titjob_scene")
            
            if "vicky_titjob_scene" in store.scenes_completed and store.stats.boldness_level >= 7 and minigame_typing_times_succeeded_since_last_vicky_meeting >= 1 and store.week.time == "day":
                self.place_and_set_scene(nate_room, scene_name = "vicky_scene_blowjob")
            
            if "vicky_scene_blowjob" in store.scenes_completed and store.stats.boldness_level >= 8 and minigame_typing_times_succeeded_since_last_vicky_meeting >= 1:
                self.place_and_set_scene(vicky_apartment, scene_name = "vicky_scene_vaginal")
            
            if "vicky_scene_vaginal" in store.scenes_completed and store.stats.boldness_level >= 8 and minigame_typing_times_succeeded_since_last_vicky_meeting >= 1 and store.week.time == "day":
                self.place_and_set_scene(nate_room, scene_name = "vicky_scene_anal")
            
            return
        
        def list_of_main_scenes(self):
            scenes = []
            scenes.append("vicky_tease_scene")
            scenes.append("vicky_fondle_scene")
            scenes.append("vicky_titjob_scene")
            scenes.append("vicky_scene_blowjob")
            scenes.append("vicky_scene_vaginal")
            scenes.append("vicky_scene_anal")
            
            return scenes
        
        
        def display_scene_stats(self):
            return "vicky_tease_scene" in store.scenes_completed
        
        def display_bust_art_in_character_menu(self):
            return False
        
        def scene_starts_immediately_on_location_enter(self, scene_name):
            if scene_name == "vicky_tease_scene":
                return True
            if scene_name == "vicky_fondle_scene":
                return True
            if scene_name == "vicky_titjob_scene":
                return True
            if scene_name == "vicky_scene_blowjob":
                return True
            if scene_name == "vicky_scene_vaginal":
                return True
            if scene_name == "vicky_scene_anal":
                return True
            
            
            return False
        
        def show_scene_completion_only_on_stats(self):
            return True
        
        def show_on_stat_screen(self):
            return True
        
        def is_hidden_on_stat_screen(self):
            if not "vicky_tease_scene" in store.scenes_completed:
                return True
            
            return False
        
        def revisitable_scene_choice_label(self, scene_name):
            if scene_name == "vicky_titjob_scene_revisit":
                if "vicky_titjob_scene_revisit" in store.scenes_completed:
                    return "Можешь снова обхватить сиськами мой пенис, Вики?"
                else:
                    return "Можно я снова засуну свой пенис между твоих сисек?"
            
            if scene_name == "vicky_scene_blowjob_revisit":
                if "vicky_scene_blowjob_revisit" in store.scenes_completed:
                    return "Может отсосешь еще раз, Вики?"
                else:
                    return "Можешь сделать мне еще один минет?"
            
            if scene_name == "vicky_scene_vaginal_revisit":
                if "vicky_scene_vaginal_revisit" in store.scenes_completed:
                    return "Давай потрахаемся снова, Вики!"
                else:
                    return "Мы можем потрахаться на кровати снова?"
            
            if scene_name == "vicky_scene_anal_revisit":
                if "vicky_scene_anal_revisit" in store.scenes_completed:
                    return "Я хочу снова трахнуть тебя в задницу, Вики!"
                else:
                    return "Мы можем снова потрахаться на твоем столе?"
            
            return ""
        
        def replayable_scene_choice_label(self, scene_name):
            if scene_name == "vicky_tease_scene":
                return "Когда Вики показала мне свои сиськи..."
            if scene_name == "vicky_fondle_scene":
                return "Когда Вики позволила мне подержать ее за сиськи..."
            if scene_name == "vicky_titjob_scene":
                return "Когда Вики позволила мне засунуть свой член ей между сисек..."
            if scene_name == "vicky_scene_blowjob":
                return "Когда Вики сосала мой член..."
            if scene_name == "vicky_scene_vaginal":
                return "Когда Вики хотела трахнуть меня..."
            if scene_name == "vicky_scene_anal":
                return "Когда я трахал Вики в задницу на ее рабочем столе..."
            
            return ""
        
        def menu_character_select_renpy_label(self):
            return "vicky_character_menu"
        
        def display_menu(self):
            renpy.call("vicky_character_menu")
            return
        
        def gallery_thumbnail(self):
            return "images/bg/others/Vicky_Tease_Fondle/bg vicky_sit_smile.png"
        
        def gallery_images(self):
            images = []
            if "vicky_tease_scene" in scenes_completed:
                images.append("images/bg/others/Vicky_Tease_Fondle/bg vicky_sit_smile.png")
                images.append("images/bg/others/Vicky_Tease_Fondle/bg vicky_sit_neutral.png")
                images.append("images/bg/others/Vicky_Tease_Fondle/bg vicky_sit_turn.png")
                images.append("images/bg/others/Vicky_Tease_Fondle/bg vicky_sit_tease.png")
                images.append("images/bg/others/Vicky_Tease_Fondle/bg vicky_fondle_clothed_transparent.png")
            
            if "vicky_fondle_scene" in scenes_completed:
                images.append("images/bg/others/Vicky_Tease_Fondle/bg vicky_fondle_exposed_transparent.png")
            
            if "vicky_titjob_scene" in scenes_completed:
                images.append("images/bg/others/Vicky_Titfuck/bg vicky_titfuck_sideview.png")
                images.append("images/bg/others/Vicky_Titfuck/bg vicky_titfuck_sideview_xray.png")
                
                images.append("images/bg/others/Vicky_Titfuck/bg vicky_titfuck_NoNate.png")
                
                images.append("images/bg/others/Vicky_Titfuck/bg vicky_titfuck_nocum.png")
                images.append("images/bg/others/Vicky_Titfuck/bg vicky_titfuck_nocum_xray.png")
                images.append("images/bg/others/Vicky_Titfuck/bg vicky_titfuck_nocum_penisonly.png")
                
                images.append("images/bg/others/Vicky_Titfuck/bg vicky_titfuck_cum.png")
                images.append("images/bg/others/Vicky_Titfuck/bg vicky_titfuck_cum_xray.png")
                images.append("images/bg/others/Vicky_Titfuck/bg vicky_titfuck_cum_penisonly.png")
                
                images.append("images/bg/others/Vicky_Titfuck/bg vicky_titfuck_aftercum.png")
            
            if "vicky_scene_blowjob" in scenes_completed:
                images.append("images/bg/others/Vicky Blowjob/bg vicky_blowjob_foreskinpull.png")
                images.append("images/bg/others/Vicky Blowjob/bg vicky_blowjob_ballsuck.png")
                images.append("images/bg/others/Vicky Blowjob/bg vicky_blowjob_nocum.png")
                images.append("images/bg/others/Vicky Blowjob/bg vicky_blowjob_cum.png")
                images.append("images/bg/others/Vicky Blowjob/bg vicky_blowjob_aftercum_openmouth.png")
                images.append("images/bg/others/Vicky Blowjob/bg vicky_blowjob_aftercum_closemouth.png")
                images.append("images/bg/others/Vicky Blowjob/bg vicky_blowjob_aftercum_swallow.png")
            
            if "vicky_scene_vaginal" in scenes_completed:
                images.append("images/bg/others/Vicky Vaginal/bg vicky_onbed_clothed_soft.png")
                images.append("images/bg/others/Vicky Vaginal/bg_vicky_onbed_clothed_hard.png")
                images.append("images/bg/others/Vicky Vaginal/bg vicky_onbed_clothed_pen.png")
                images.append("images/bg/others/Vicky Vaginal/bg vicky_vaginal_clothed.png")
                images.append("images/bg/others/Vicky Vaginal/bg vicky_matingpress_clothed.png")
                images.append("images/bg/others/Vicky Vaginal/bg vicky_matingpress_clothed_cum.png")
                images.append("images/bg/others/Vicky Vaginal/bg vicky_matingpress_clothed_cum_impreg.png")
                images.append("images/bg/others/Vicky Vaginal/bg vicky_onbed_naked_soft.png")
                images.append("images/bg/others/Vicky Vaginal/bg vicky_onbed_naked_hard.png")
                images.append("images/bg/others/Vicky Vaginal/bg vicky_onbed_naked_pen.png")
                images.append("images/bg/others/Vicky Vaginal/bg vicky_matingpress_nude.png")
                images.append("images/bg/others/Vicky Vaginal/bg vicky_matingpress_nude_cum.png")
                images.append("images/bg/others/Vicky Vaginal/bg vicky_matingpress_nude_cum_impreg.png")
            
            if "vicky_scene_anal" in scenes_completed:
                images.append("images/bg/others/vicky anal/bg vicky_anal_probe.png")
                images.append("images/bg/others/vicky anal/bg vicky_anal_shirt.png")
                images.append("images/bg/others/vicky anal/bg vicky_anal_shirtpull.png")
                images.append("images/bg/others/vicky anal/bg vicky_anal_fuck.png")
                images.append("images/bg/others/vicky anal/bg vicky_anal_behind.png")
                images.append("images/bg/others/vicky anal/bg vicky_anal_behind_cum.png")
            
            
            images.extend(self.finale_images())
            return images
        
        def gallery_unlock_scene_thumbnail_requirement(self):
            return "vicky_tease_scene"
        
        def gallery_unlock_name_requirement(self):
            return store.had_vicky_intro_scene or self.gallery_unlock_scene_thumbnail_requirement() in store.scenes_completed
        
        def gallery_bust_art_can_be_shown(self):
            return False
        
        def hide_notifications(self):
            return persistent.hide_vicky_notification

    class Janet(IA_Actor):
        def __init__(self, internal_name = "janet", variable_name = "janet"):
            IA_Actor.__init__(self, internal_name, variable_name)
            return
        
        def hide_notifications(self):
            return persistent.hide_janet_notification
        
        def default_color(self):
            return "#8822e8"
        
        def character_select_button_crop_left(self):
            return 76
        
        def character_select_button_crop_top(self):
            return 193
        
        def character_select_button_crop_right(self):
            return 72
        
        def default_say_name(self):
            return "Janet"
        
        def default_outfit(self):
            return "clothes"
        
        def default_pose(self):
            return "handhips"
        
        def hovered_outfit(self):
            return self.default_outfit()
        
        def unhovered_outfit(self):
            return self.default_outfit()
        
        def hovered_pose(self):
            return "handchest"
        
        def unhovered_pose(self):
            return "handhips"
        
        def face_pose(self, pose):
            return "handhips"
        
        def is_hidden_on_stat_screen(self):
            if not store.had_janet_intro_scene:
                return True
            
            return False
        
        def show_on_stat_screen(self):
            return True
        
        def display_scene_stats(self):
            return store.had_janet_intro_scene
        
        def decide_default_location(self):
            if not store.had_janet_intro_scene:
                return
            
            self.place_and_set_scene(janet_house)
            
            return
        
        def conversation_max(self):
            return 0
        
        def add_conversations_to_pool(self):
            self.test_and_add_conversation_to_pool(conversation_name = "janet_convo_1")
            self.test_and_add_conversation_to_pool(conversation_name = "janet_convo_2")
            self.test_and_add_conversation_to_pool(conversation_name = "janet_convo_3")
            self.test_and_add_conversation_to_pool(conversation_name = "janet_convo_4")
            self.test_and_add_conversation_to_pool(conversation_name = "janet_convo_5")
            self.test_and_add_conversation_to_pool(conversation_name = "janet_convo_6")
            self.test_and_add_conversation_to_pool(conversation_name = "janet_convo_7")
            
            return
        
        
        def xp_required_for_level(self, level):
            if not level or level == 1:
                return 0
            elif level == 2:
                return 3
            elif level == 3:
                return 6
            elif level == 4:
                return 9
            elif level == 5:
                return 12
            elif level == 5:
                return 15
            elif level == 6:
                return 18
            elif level == 7:
                return 22
            elif level == 8:
                return 26
            
            
            return 999999999
        
        def relationship_level_cap(self):
            return 8
        
        def list_of_main_scenes(self):
            scenes = []
            scenes.append("janet_scene_underwear")
            scenes.append("janet_scene_bottomless")
            scenes.append("janet_scene_naked")
            scenes.append("janet_scene_blowjob")
            scenes.append("janet_scene_vaginal")
            scenes.append("janet_scene_anal")
            return scenes
        
        def boldness_level_required_for_scene(self, scene_name):
            if scene_name == "janet_scene_blowjob":
                return 6
            if scene_name == "janet_scene_vaginal":
                return 8
            
            return 0
        
        def prompt_label(self, scene_name):
            if scene_name == "janet_scene_blowjob":
                return "Т-ты можешь сфотографировать меня, если хочешь."
            if scene_name == "janet_scene_vaginal":
                return "Я хочу быть голым с тобой тётя [janet.say_name]!"
            
            return ""
        
        def scene_starts_immediately_on_location_enter(self, scene_name):
            if scene_name == "janet_scene_intro_2":
                return True
            if scene_name == "janet_scene_vaginal":
                return True
            if scene_name == "janet_scene_anal":
                return True
            
            return False
        
        def default_outfit(self):
            if store.finale_scene_completed_with_julia_sam:
                return "nude"
            
            if store.week.time == "day" and (self.scene == "janet_scene_vaginal" or "janet_scene_vaginal" in store.scenes_completed) and self in store.janet_house.character_list():
                return "nude"
            
            return "clothes"
        
        def decide_normal_scene(self):
            if not store.had_janet_intro_scene:
                return
            
            self.place_and_set_scene(janet_house, scene_name = "janet_scene_intro_2")
            
            if week.time == "day":
                self.place_and_set_scene(janet_house, scene_name = "janet_scene_minigame_intro", prerequisite_scene = "janet_scene_intro_2")
            
            if week.time == "day":
                self.place_and_set_scene(janet_house, scene_name = "janet_scene_underwear", prerequisite_scene = "janet_scene_minigame_intro", level_required = 2)
            
            self.place_and_set_scene(janet_house, scene_name = "janet_scene_topless", prerequisite_scene = "janet_scene_underwear", level_required = 3)
            self.place_and_set_scene(janet_house, scene_name = "janet_scene_bottomless", prerequisite_scene = "janet_scene_topless", level_required = 4)
            self.place_and_set_scene(janet_house, scene_name = "janet_scene_naked", prerequisite_scene = "janet_scene_bottomless", level_required = 5)
            self.place_and_set_scene(janet_house, scene_name = "janet_scene_blowjob", prerequisite_scene = "janet_scene_naked", level_required = 6)
            
            if week.time == "day":
                self.place_and_set_scene(janet_house, scene_name = "janet_scene_vaginal", prerequisite_scene = "janet_scene_blowjob", level_required = 7)
            
            if week.time == "day":
                self.place_and_set_scene(janet_house, scene_name = "janet_scene_anal", prerequisite_scene = "janet_scene_vaginal", level_required = 8)
            
            return
        
        def available_minigames(self):
            minigame_call_labels = []
            
            if "janet_scene_minigame_intro" in store.scenes_completed:
                minigame_call_labels.append("minigame_racing")
            
            return minigame_call_labels
        
        def revisitable_scene_choice_label(self, scene_name):
            if scene_name == "janet_scene_blowjob_revisit":
                if "janet_scene_blowjob_revisit" not in store.scenes_completed:
                    return "Можешь снова засунуть мой член в рот, тётя [janet.say_name]?"
                else:
                    return "Ты можешь дать мне другой минет, тётя [janet.say_name]?"
            
            if scene_name == "janet_scene_vaginal_revisit":
                if "janet_scene_vaginal_revisit" not in store.scenes_completed:
                    return "Можешь присесть на меня снова, тётя [janet.say_name]?"
                else:
                    return "Давай трахаться на диване снова, тётя [janet.say_name]!"
            
            if scene_name == "janet_scene_anal_revisit":
                if "janet_scene_anal_revisit" not in store.scenes_completed:
                    return "Можем ли мы потрахаться на пляже снова, тётя [janet.say_name]?"
                else:
                    return "Пойдем трахаться на пляже снова, тетя [janet.say_name]!"
            
            return ""
        
        def replayable_scene_choice_label(self, scene_name):
            if scene_name == "janet_scene_underwear":
                return "Когда я увидел тётю " + janet.say_name + " в нижнем белье..."
            
            if scene_name == "janet_scene_topless":
                return "Когда я увидел тётю " + janet.say_name + " заставила меня сфотографировать ее топлесс..."
            
            if scene_name == "janet_scene_bottomless":
                return "Когда я фотографировал промежность тети " + janet.say_name + "..."
            
            if scene_name == "janet_scene_naked":
                return "Когда тётя " + janet.say_name + " была голой на пляже..."
            
            if scene_name == "janet_scene_blowjob":
                return "Когда тётя " + janet.say_name + " первый раз сосала мой член..."
            
            if scene_name == "janet_scene_vaginal":
                return "Когда тётя [janet.say_name] села на мой член..."
            
            if scene_name == "janet_scene_anal":
                return "Когда я трахнул тётю [janet.say_name] в задницу на пляже..."
            
            
            return ""
        
        def gallery_unlock_name_requirement(self):
            return False
        
        def conversation_max(self):
            return 7
        
        def racing_icon_losing(self):
            return self.icon_image("")
        
        def racing_icon_losing_bad(self):
            return self.icon_image("_Surprised")
        
        def racing_icon_winning(self):
            return self.icon_image("_Happy")
        
        def pose_adjustment(self, pose):
            if pose == "handhip":
                return "handhips"
            return pose
        
        def gallery_unlock_name_requirement(self):
            return store.had_janet_intro_scene
        
        def gallery_unlock_scene_thumbnail_requirement(self):
            return "janet_scene_blowjob"
        
        def should_appear_in_gallery(self):
            return True
        
        def gallery_images(self):
            images = []
            if "janet_scene_blowjob" in scenes_completed:
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_tip_lick.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_foreskin_pull.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_deepthroat.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_panties_NateArouse.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_panties_NateOrgasm_aftercum.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_panties_NateOrgasm_cum.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_panties_NateOrgasm_nocum.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_tip_panties_NateArouse.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_tip_panties_NateAroused_cum.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_tip_panties_NateOrgasm_cum.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_nude_foreskin_pull.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_nude_deepthroat.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_nude_NateArouse.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_nude_NateOrgasm_aftercum.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_nude_NateOrgasm_cum.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_nude_NateOrgasm_nocum.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_tip_nude_NateArouse.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_tip_nude_NateAroused_cum.png")
                images.append("images/bg/janet/Aunt Janet Blowjob/bg janet_blowjob_tip_nude_NateOrgasm_cum.png")
            
            if "janet_scene_vaginal" in scenes_completed:
                images.append("images/bg/janet/Janet_Vaginal/bg janet_vaginal_sideview.png")
                images.append("images/bg/janet/Janet_Vaginal/bg janet_vaginal_behind_down.png")
                images.append("images/bg/janet/Janet_Vaginal/bg janet_vaginal_behind_downblur.png")
                images.append("images/bg/janet/Janet_Vaginal/bg janet_vaginal_behind_up.png")
                images.append("images/bg/janet/Janet_Vaginal/bg janet_vaginal_behind_up_cum.png")
                images.append("images/bg/janet/Janet_Vaginal/bg janet_vaginal_behind_down_cum.png")
            
            if "janet_scene_anal" in scenes_completed:
                images.append("images/bg/janet/janet anal/bg janet_anal_NateSoft.png")
                images.append("images/bg/janet/janet anal/bg janet_anal_NateHard.png")
                images.append("images/bg/janet/janet anal/bg janet_anal_NateInsert.png")
                images.append("images/animations/janet anal/janet_anal_anim_0.png")
                images.append("images/bg/janet/janet anal/bg janet_anal_cumshot.png")
            
            
            images.extend(self.finale_images())
            return images
        
        def gallery_thumbnail(self):
            return "images/bg/janet/Aunt Janet Blowjob/bg janet_deepthroat.png"
        
        def gallery_bust_art_default_pose(self):
            return "handhips"
        
        def gallery_bust_art_poses(self):
            return ["handhips", "handchest", "handface"]
        
        def gallery_bust_art_faces(self):
            faces = IA_Actor.gallery_bust_art_faces(self)
            faces.extend(["surprised"])
            return faces
        
        def gallery_bust_art_outfits(self):
            outfits = ["clothes", "swimsuit"]
            
            if "janet_scene_underwear" in scenes_completed:
                outfits.extend(["underwear"])
            
            if "janet_scene_topless" in scenes_completed:
                outfits.extend(["topless"])
            
            if "janet_scene_bottomless" in scenes_completed:
                outfits.extend(["bottomless"])
            
            if "janet_scene_naked" in scenes_completed:
                outfits.extend(["nude"])
            
            return outfits
        
        def gallery_bust_art_can_be_shown(self):
            return store.had_janet_intro_scene

    class Edna(IA_Actor):
        def __init__(self, internal_name = "edna", variable_name = "edna"):
            IA_Actor.__init__(self, internal_name, variable_name)
            return
        
        def default_color(self):
            return "#C0C0C0"
        
        def character_select_button_crop_left(self):
            return 56
        
        def character_select_button_crop_top(self):
            return 159
        
        def character_select_button_crop_right(self):
            return 43
        
        def default_say_name(self):
            return "Edna"
        
        def default_outfit(self):
            return "clothes"
        
        def default_pose(self):
            return "handhip"
        
        def hovered_outfit(self):
            return self.default_outfit()
        
        def unhovered_outfit(self):
            return self.default_outfit()
        
        def hovered_pose(self):
            return "handclasp"
        
        def unhovered_pose(self):
            return "fisthip"
        
        def face_pose(self, pose):
            if pose == "fisthip":
                return "handclasp"
            return pose
        
        def is_hidden_on_stat_screen(self):
            if not store.had_edna_intro_scene:
                return True
            
            return False
        
        def show_on_stat_screen(self):
            return True
        
        def display_scene_stats(self):
            return store.had_edna_intro_scene
        
        def decide_default_location(self):
            if not store.had_edna_intro_scene:
                return
            
            self.place_and_set_scene(edna_house)
            
            return
        
        def add_conversations_to_pool(self):
            self.test_and_add_conversation_to_pool(conversation_name = "edna_convo_1")
            
            if "minigame_table_tennis" in minigames_tried:
                self.test_and_add_conversation_to_pool(conversation_name = "edna_convo_2")
                self.test_and_add_conversation_to_pool(conversation_name = "edna_convo_3")
            
            self.test_and_add_conversation_to_pool(conversation_name = "edna_convo_4")
            self.test_and_add_conversation_to_pool(conversation_name = "edna_convo_5")
            self.test_and_add_conversation_to_pool(conversation_name = "edna_convo_6")
            
            return
        
        
        def xp_required_for_level(self, level):
            if not level or level == 1:
                return 0
            elif level == 2:
                return 3
            elif level == 3:
                return 6
            elif level == 4:
                return 10
            elif level == 5:
                return 14
            elif level == 5:
                return 18
            elif level == 6:
                return 22
            elif level == 7:
                return 26
            elif level == 8:
                return 30
            elif level == 9:
                return 34
            elif level == 10:
                return 38
            elif level == 11:
                return 42
            elif level == 12:
                return 46
            
            return 999999999
        
        def relationship_level_cap(self):
            return 12
        
        def list_of_main_scenes(self):
            scenes = []
            scenes.append("edna_scene_nate_underwear")
            scenes.append("edna_scene_underwear")
            scenes.append("edna_scene_swimsuit")
            scenes.append("edna_scene_nate_naked")
            scenes.append("edna_scene_topless")
            scenes.append("edna_scene_bottomless")
            scenes.append("edna_scene_naked")
            scenes.append("edna_scene_handjob")
            scenes.append("edna_scene_titfuck")
            scenes.append("edna_scene_blowjob")
            scenes.append("edna_scene_vaginal_anal")
            return scenes
        
        def boldness_level_required_for_scene(self, scene_name):
            if scene_name == "edna_scene_handjob":
                return 7
            return 0
        
        def prompt_label(self, scene_name):
            if scene_name == "edna_scene_handjob":
                return "Я бы хотел посидеть с тобой в джакузи, Бабушка..."
            return ""
        
        def scene_starts_immediately_on_location_enter(self, scene_name):
            if scene_name == "edna_scene_intro_2":
                return True
            if scene_name == "edna_scene_nate_underwear":
                return True
            if scene_name == "edna_scene_underwear":
                return True
            if scene_name == "edna_scene_swimsuit":
                return True
            if scene_name == "edna_scene_nate_naked":
                return True
            if scene_name == "edna_scene_bottomless":
                return True
            if scene_name == "edna_scene_handjob":
                return True
            if scene_name == "edna_scene_titfuck":
                return True
            return False
        
        def default_outfit(self):
            if store.finale_scene_completed_with_julia_sam:
                return "nude"
            
            if "finale_scene" in store.scenes_completed and self in store.edna_house.character_list() and len(store.edna_house.character_list()) == 1:
                return "nude"
            
            if "edna_scene_vaginal_anal" in store.scenes_completed and self in store.edna_house.character_list() and len(store.edna_house.character_list()) == 1:
                return "nude"
            
            if (not self.scene or self.play_scene_even_with_prompted_scene) and "edna_scene_blowjob_revisit" in store.scenes_completed and self in store.edna_house.character_list() and len(store.edna_house.character_list()) == 1:
                return "nude"
            
            if (not self.scene or self.play_scene_even_with_prompted_scene) and "edna_scene_blowjob" in store.scenes_completed and self in store.edna_house.character_list() and len(store.edna_house.character_list()) == 1:
                return "topless_underwear"
            
            if (not self.scene or self.play_scene_even_with_prompted_scene) and "edna_scene_bottomless" in store.scenes_completed and self in store.edna_house.character_list() and len(store.edna_house.character_list()) == 1:
                return "underwear"
            
            
            return "clothes"
        
        def decide_normal_scene(self):
            if not store.had_edna_intro_scene:
                return
            self.place_and_set_scene(location = edna_house, scene_name = "edna_scene_intro_2")
            self.place_and_set_scene(location = edna_house, scene_name = "edna_scene_minigame_intro", prerequisite_scene = "edna_scene_intro_2")
            if store.week.time == "day":
                self.place_and_set_scene(location = nate_room, scene_name = "edna_scene_nate_underwear", prerequisite_scene = "edna_scene_minigame_intro", level_required = 2)
            if store.week.time == "day":
                self.place_and_set_scene(location = edna_house, scene_name = "edna_scene_underwear", prerequisite_scene = "edna_scene_nate_underwear", level_required = 3)
            if store.week.time == "day":
                self.place_and_set_scene(location = nate_room, scene_name = "edna_scene_swimsuit", prerequisite_scene = "edna_scene_underwear", level_required = 4)
            self.place_and_set_scene(location = nate_room, scene_name = "edna_scene_nate_naked", prerequisite_scene = "edna_scene_swimsuit", level_required = 5)
            self.place_and_set_scene(location = edna_house, scene_name = "edna_scene_topless", prerequisite_scene = "edna_scene_nate_naked", level_required = 6)
            self.place_and_set_scene(location = edna_house, scene_name = "edna_scene_bottomless", prerequisite_scene = "edna_scene_topless", level_required = 7)
            self.place_and_set_scene(location = edna_house, scene_name = "edna_scene_naked", prerequisite_scene = "edna_scene_bottomless", level_required = 8)
            
            if store.week.time == "day":
                self.place_and_set_scene(location = nate_room, scene_name = "edna_scene_handjob", prerequisite_scene = "edna_scene_naked", level_required = 9)
            
            if store.week.time == "day":
                self.place_and_set_scene(location = edna_house, scene_name = "edna_scene_titfuck", prerequisite_scene = "edna_scene_handjob", level_required = 10)
            
            if store.week.time == "day":
                self.place_and_set_scene(location = edna_house, scene_name = "edna_scene_blowjob", prerequisite_scene = "edna_scene_titfuck", level_required = 11)
            
            if store.week.time == "day":
                self.place_and_set_scene(location = edna_house, scene_name = "edna_scene_vaginal_anal", prerequisite_scene = "edna_scene_blowjob", level_required = 12)
            
            
            return
        
        def available_minigames(self):
            minigame_call_labels = []
            if "edna_scene_minigame_intro" in scenes_completed:
                minigame_call_labels.extend(["minigame_table_tennis"])
            
            return minigame_call_labels
        
        def revisitable_scene_choice_label(self, scene_name):
            if scene_name == "edna_scene_handjob_revisit":
                if "edna_scene_handjob_revisit" not in store.scenes_completed:
                    return "Можешь еще раз потрогать мой член в джакузи, бабушка?"
                else:
                    return "Мы можем снова пойти в джакузи, бабушка?"
            
            if scene_name == "edna_scene_titfuck_revisit":
                if "edna_scene_titfuck_revisit" not in store.scenes_completed:
                    return "Можно я снова засуну свой пенис между твоих сисек, бабушка?"
                else:
                    return "Можно я еще раз трахну твои сиськи, бабушка?"
            
            if scene_name == "edna_scene_blowjob_revisit":
                if "edna_scene_blowjob_revisit" not in store.scenes_completed:
                    return "Пожалуйста, отсоси мне еще раз, бабушка."
                else:
                    return "Можешь еще раз пососать мой член, бабушка?"
            
            if scene_name == "edna_scene_vaginal_anal_revisit":
                if "edna_scene_vaginal_anal_revisit" not in store.scenes_completed:
                    return "Могу я сделать тебе еще один особый массаж, Бабушка?"
                else:
                    return "Давай трахнемся после того, как я сделаю тебе массаж, Бабушка!"
            
            return ""
        
        def replayable_scene_choice_label(self, scene_name):
            if scene_name == "edna_scene_nate_underwear":
                return "Когда я ночевал у Бабушки..."
            if scene_name == "edna_scene_underwear":
                return "Когда я увидел Бабушку в нижнем белье..."
            if scene_name == "edna_scene_swimsuit":
                return "Когда я впервые увидел Бабушку в купальнике..."
            if scene_name == "edna_scene_nate_naked":
                return "Когда Бабушка увидела, как мой пенис становится твердым..."
            if scene_name == "edna_scene_topless":
                return "Когда Бабушка показала мне свои сиськи..."
            if scene_name == "edna_scene_bottomless":
                return "Когда бабушка хотела, чтобы я посмотрел на ее влагалище..."
            if scene_name == "edna_scene_naked":
                return "Когда Бабушка делала стриптиз для меня..."
            if scene_name == "edna_scene_handjob":
                return "Когда бабушка трогала мой член в джакузи..."
            if scene_name == "edna_scene_titfuck":
                return "Когда я тёрся и трахал бабушкины сиськи..."
            if scene_name == "edna_scene_blowjob":
                return "Когда Бабушка сосала мой член..."
            if scene_name == "edna_scene_vaginal_anal":
                return "Когда я трахал бабушку во время массажа..."
            
            return ""
        
        def gallery_unlock_name_requirement(self):
            return False
        
        def conversation_max(self):
            return 6
        
        def racing_icon_losing(self):
            return self.icon_image("")
        
        def racing_icon_losing_bad(self):
            return self.icon_image("_Surprised")
        
        def racing_icon_winning(self):
            return self.icon_image("_Happy")
        
        def gallery_unlock_name_requirement(self):
            return store.had_edna_intro_scene
        
        def gallery_unlock_scene_thumbnail_requirement(self):
            return "edna_scene_handjob"
        
        def should_appear_in_gallery(self):
            return True
        
        def gallery_images(self):
            images = []
            if "edna_scene_handjob" in scenes_completed:
                images.append("images/bg/edna/Edna Handjob/bg edna_hottub.png")
                images.append("images/bg/edna/Edna Handjob/bg edna_NoSimone.png")
                images.append("images/bg/edna/Edna Handjob/bg edna_NoSimone_Aroused.png")
                images.append("images/bg/edna/Edna Handjob/bg edna_SimoneHappy.png")
                images.append("images/bg/edna/Edna Handjob/bg edna_SimoneHappy_Aroused.png")
                images.append("images/bg/edna/Edna Handjob/bg edna_legtouch_soft.png")
                images.append("images/bg/edna/Edna Handjob/bg edna_legtouch_hard.png")
                images.append("images/bg/edna/Edna Handjob/bg edna_underwater_jerk.png")
                images.append("images/bg/edna/Edna Handjob/bg edna_jerk_nocum.png")
                images.append("images/bg/edna/Edna Handjob/bg edna_jerkblur_EyesClosed_cum.png")
                images.append("images/bg/edna/Edna Handjob/bg edna_jerk_aftercum_smile.png")
            
            if "edna_scene_titfuck" in scenes_completed:
                images.append("images/bg/edna/edna titfuck/bg edna_titrub.png")
                images.append("images/bg/edna/edna titfuck/bg edna_titsuck.png")
                images.append("images/bg/edna/edna titfuck/bg edna_titsuck_pull.png")
                images.append("images/bg/edna/edna titfuck/bg edna_beforetitfuck.png")
                images.append("images/bg/edna/edna titfuck/bg edna_bikini_titfuck_nocum_smile.png")
                images.append("images/animations/edna titfuck bikini/edna_titfuck_anim_0.png")
                images.append("images/bg/edna/edna titfuck/bg edna_bikini_titfuck_nocum_surprise.png")
                images.append("images/bg/edna/edna titfuck/bg edna_bikini_titfuck_cumshot_surprise.png")
                images.append("images/bg/edna/edna titfuck/bg edna_bikini_titfuck_aftercum_surprise.png")
                images.append("images/bg/edna/edna titfuck/bg edna_bikini_titfuck_aftercum_smile.png")
                
                if "edna_scene_titfuck_revisit" in scenes_completed:
                    images.append("images/bg/edna/edna titfuck/bg edna_nude_titfuck_nocum_smile.png")
                    images.append("images/animations/edna titfuck nude/edna_titfuck_nude_anim_0.png")
                    images.append("images/bg/edna/edna titfuck/bg edna_nude_titfuck_nocum_surprise.png")
                    images.append("images/bg/edna/edna titfuck/bg edna_nude_titfuck_cumshot_surprise.png")
                    images.append("images/bg/edna/edna titfuck/bg edna_nude_titfuck_aftercum_surprise.png")
                    images.append("images/bg/edna/edna titfuck/bg edna_nude_titfuck_aftercum_smile.png")
            
            if "edna_scene_blowjob" in scenes_completed:
                images.append("images/bg/edna/Edna_Blowjob/bg edna_tipsuck.png")
                images.append("images/bg/edna/Edna_Blowjob/bg edna_blowjob _foreskinplay.png")
                images.append("images/bg/edna/Edna_Blowjob/bg edna_blowjob _nocum.png")
                images.append("images/bg/edna/Edna_Blowjob/bg edna_blowjob _Natetongue_nocum.png")
                images.append("images/bg/edna/Edna_Blowjob/bg edna_blowjob _Natetongue_cum.png")
                images.append("images/bg/edna/Edna_Blowjob/bg edna_blowjob _cum.png")
                images.append("images/bg/edna/Edna_Blowjob/bg edna_blowjob _foreskinplay_cum.png")
            
            if "edna_scene_vaginal_anal" in scenes_completed:
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_laying.png")
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_laying_noNate.png")
                
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_vagfuck.png")
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_analingus.png")
                
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_anal_blur.png")
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_anal_blur_ahego.png")
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_anal_noblur.png")
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_anal__ahego_aftercum.png")
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_anal_aftercum.png")
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_anal_blur_ahego_cum.png")
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_anal_blur_cum.png")
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_nocumass.png")
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_nocumass_nate.png")
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_cumass.png")
                images.append("images/bg/edna/edna vaginal anal/bg edna_vag_anal_cumass_nate.png")
            
            images.extend(self.finale_images())
            return images
        
        def gallery_thumbnail(self):
            return "images/bg/edna/Edna Handjob/bg edna_hottub.png"
        
        def gallery_bust_art_default_pose(self):
            return "handhip"
        
        def gallery_bust_art_poses(self):
            return ["handhip", "handclasp", "fisthip"]
        
        def gallery_bust_art_faces(self):
            faces = IA_Actor.gallery_bust_art_faces(self)
            faces.extend(["surprised"])
            return faces
        
        def gallery_bust_art_outfits(self):
            outfits = ["clothes"]
            if "edna_scene_underwear" in store.scenes_completed: 
                outfits.extend(["underwear"])
            if "edna_scene_swimsuit" in store.scenes_completed: 
                outfits.extend(["swimsuit"])
            if "edna_scene_topless" in store.scenes_completed: 
                outfits.extend(["topless_swimsuit"])
            if "edna_scene_naked" in store.scenes_completed: 
                outfits.extend(["topless_underwear"])
            if "edna_scene_bottomless" in store.scenes_completed: 
                outfits.extend(["underwear_bottomless"])
            if "edna_scene_naked" in store.scenes_completed: 
                outfits.extend(["swimsuit_bottomless"])
            if "edna_scene_naked" in store.scenes_completed: 
                outfits.extend(["nude"])
            
            return outfits
        
        def gallery_bust_art_can_be_shown(self):
            return store.had_edna_intro_scene
        
        def gallery_bust_art_enabled(self):
            return True
        
        def has_separate_mouth(self):
            return True
        
        def default_mouth(self):
            return "natural"
        
        def has_separate_hat(self):
            return True
        
        def hide_notifications(self):
            return persistent.hide_edna_notification

label vicky_character_menu(char=vicky):
    call process_scene_beginning (bg="bg vicky_sit_smile")
    call process_character (vicky, text="Привет [n.say_name]!")
    call process_character (vicky, text="Присаживайся, устраивайся поудобнее!")
    call process_character (vicky, text="Так, что у тебя на уме?")
    $ no_bust_art = True
    call character_menu (vicky, draw_characters=False)
    return

label gloryhole_girl_character_menu(char=gloryhole_girl):
    call process_scene_beginning (bg="bg gloryhole")
    call process_character (n, text="Ты здесь, [gloryhole_girl.say_name]?")
    call process_character (gloryhole_girl, text="[n.say_name]!")
    call process_character (gloryhole_girl, text="Снова вернулся!")
    call process_character (gloryhole_girl, text="Так ты хочешь еще раз повеселиться?")
    $ no_bust_art = True
    call character_menu (gloryhole_girl, draw_characters=False)
    return