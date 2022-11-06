init python:
    def face_equalities_special(char, face):
        if face == "aroused" or face == "flirt":
            face = "flirty"
        
        return face

    def has_seen_big_breasts_other_than_vicky():
        return "simone_scene_undressing" in store.scenes_completed or "kira_scene_6" in store.scenes_completed or "gloryhole_scene_stall" in store.scenes_completed

label update_last_names:
    python hide:
        chars = family_list()
        for char in chars:
            char.update_full_name()

    return

label process_scene_beginning_add_on(dream=False):
    python hide:
        if not dream and not started_main_game and not renpy.music.is_playing():
            advance_time_return_location.decide_and_play_daily_music_queue()

    return

label process_end_of_scene_before_advance_time:
    if is_school_time:
        jump school_leave

    return