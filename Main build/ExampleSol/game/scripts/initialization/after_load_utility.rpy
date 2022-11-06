init python:
    def perform_new_game_plus(restart_label):
        
        new_game_plus_character_xp = {}
        new_game_plus_money = store.inventory.minigame_money
        new_game_plus_boldness = store.stats.minigame_boldness_xp
        for char in npc_list():
            new_game_plus_character_xp[char.variable_name] = char.minigame_points
        
        
        initialize_variables(force_reinitialization = True)
        
        
        for char in npc_list():
            char.add_points(new_game_plus_character_xp[char.variable_name], force_no_popup = True, minigame = True)            
        
        if getattr(store, 'inventory', False):
            store.inventory.add_money(new_game_plus_money, minigame = True)
        
        store.stats.add_boldness_xp(new_game_plus_boldness, minigame = True, force_no_popup = True)
        
        
        after_load_reevaluate_character_levels()
        store.stats.check_and_set_boldness_level()
        
        
        renpy.jump_out_of_context(restart_label)
        
        return

    def after_load_setup():
        initialize_variables()
        set_settings()
        config.rollback_enabled = store.rollback_enabled
        after_load_update_colors()
        after_load_setup_special()
        
        return

    def after_load_reevaluate_character_levels():
        chars = npc_list()
        
        for char in chars:
            char.check_and_set_level()
        return

    def after_load_update_colors():
        chars = npc_list()
        
        for char in chars:
            char.create_renpy_characters()
        
        return

    def place_new_characters():
        chars = npc_list()
        
        for char in chars:
            if not char.has_tried_to_place_at_least_once:
                char.reset()
        
        return

    config.after_load_callbacks = [after_load_setup]

label new_game_plus_label:
    $ renpy.scene('screens')
    $ perform_new_game_plus("intro_0")
    return