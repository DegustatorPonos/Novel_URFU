init python:
    def fix_anim_log_error():
        try:
            store.anim
        except:
            "hello"
        else:
            del store.anim  
            anim = renpy.display.anim
        
        for log in renpy.game.log.log:
            try:
                log.stores['store']['anim']
            except:
                "hello"
            else:
                del log.stores['store']['anim']
        
        return
    config.python_callbacks = [fix_anim_log_error]

    def after_load_setup_special():
        fix_anim_log_error()
        
        
        for char in character_list():
            if not getattr(char, 'mouth', False):
                char.mouth = char.default_mouth()
            if not getattr(char, 'hat', False):
                char.hat = char.default_hat()
        
        renpy.hide_screen('pop_up_general')
        
        if "kira_scene_1_revisit" in k.replayable_scenes:
            k.replayable_scenes.remove("kira_scene_1_revisit")
        
        if "family_foursome_scene_revisit" in store.scenes_completed:
            scenes_completed.add("family_foursome_scene_revisit_kira")
            scenes_completed.add("family_foursome_scene_revisit_simone")
            scenes_completed.add("family_foursome_scene_revisit_sam")
        
        after_load_reevaluate_character_levels()
        store.stats.check_and_set_boldness_level()
        place_new_characters()
        
        for char in npc_list():
            char.revistable_scenes = set(char.revistable_scenes)
        
        for char in character_list():
            char.revistable_scenes = set(char.revistable_scenes)
        
        return