init python:
    def fix_edna_save():
        for scene in store.edna.list_of_main_scenes():
            edna.replayable_scenes.append(scene)
        return
    def add_all_main_scenes():
        for char in npc_list():
            for scene in char.list_of_main_scenes():
                scenes_completed.add(scene)
        
        return

    def add_all_main_scenes_for_char(char):
        for scene in char.list_of_main_scenes():
            scenes_completed.add(scene)
        
        return

label debug_menu:
    $ reset_all_characters()
    if wholesome_mode:
        call intro_0
        return

    $ stop_music(fadeout=2)
    call static_still ("bg placeholder_static")

    $ no_bust_art = False
    menu:
        "Интро":
            call initialize_variables (force_reinitialization=True)
            call intro_0
        "Старт Нового Дня":
            call debug_start_new_day
        "Старт Нового Дня (Чит Очки)":
            call debug_start_new_day (cheats=True)
        "Отладка персонажей":
            call debug_character
        "Отладка мини-игр":
            call debug_minigame
        "Отладка Смелости":
            call debug_boldness
        "Групповые сцены":
            call debug_group_scenes
        "Отладка Эпилога":
            jump epilogue_debug
        "Галерея":
            "DEBUG: adding all scenes to completed list and certain plot flags"
            $ had_janet_intro_scene = True
            $ had_vicky_intro_scene = True
            $ had_julia_arrived_scene = True
            $ stats.add_stat("times_had_erection", 1)

            python hide:
                for char in npc_list():
                    for scene in char.list_of_main_scenes():
                        scenes_completed.add(scene)

            jump gallery
        "clear scene history":
            $ scenes_completed = set()
            "cleared scene history"
            call debug_menu
    return

label epilogue_debug:
    menu:
        "Нормальный Эпилог":
            jump epilogue
        "Беременный Эпилог":
            jump epilogue_pregnancy
        "Эпилог с Джулией и Сэм":
            $ finale_scene_completed_with_julia_sam = True
            "set"
        "Назад":
            jump debug_menu

    jump epilogue_debug
    return

label edna_scene_vaginal_anal_debug:
    menu:
        "Edna vaginal anal":
            call edna_scene_vaginal_anal
        "Edna vaginal anal revisit 1st time":
            call edna_scene_vaginal_anal_revisit_1st_time
        "Edna vaginal anal revisit 2nd time":
            call edna_scene_vaginal_anal_revisit_2nd_time
        "add kira anal":
            "added"
            $ scenes_completed.add("kira_scene_anal")
            $ stats.add_stat("times_given_anal_sex", 1)
        "add simone anal":
            "added"
            $ scenes_completed.add("simone_scene_anal")
            $ stats.add_stat("times_given_anal_sex", 1)
        "add anal sex stat":
            "added"
            $ stats.add_stat("times_given_anal_sex", 1)
        "add finale scene":
            "added"
            $ scenes_completed.add("finale_scene")
        "Edna vaginal anal debug":
            call edna_scene_vaginal_anal_debug
        "Back":
            jump debug_menu
    jump edna_scene_vaginal_anal_debug
    return

label finale_debug:
    menu:
        "Финал":
            call finale_scene_sex
        "Повтор Финала":
            call finale_scene_revisit
        "Сцена с Эдной":
            $ edna_finale_vaginal_chosen = True
            "added"
        "Поставить флажок Джулии/Сэм":
            $ scenes_completed.add("julia_scene_anal")
            $ scenes_completed.add("sam_scene_dream")
            $ scenes_completed.add("sam_julia_threesome_scene")
            $ scenes_completed.add("family_foursome_scene")
            $ scenes_completed.add("sam_simone_threesome_scene")
            "added"
        "Назад":
            jump debug_menu

    jump finale_debug
    return

label debug_group_scenes:
    menu:
        "Finale Debug":
            call finale_debug
        "sam/nate/simone threesome":
            call sam_simone_threesome_scene
        "sam/nate/simone threesome revisit (ask sam)":
            call sam_simone_threesome_scene_revisit_sam
        "sam/nate/simone threesome revisit (ask simone)":
            call sam_simone_threesome_scene_revisit_simone
        "kira/nate/simone threesome":
            call kira_simone_threesome_scene_sex
        "kira/nate/simone threesome revisit (ask kira)":
            call kira_simone_threesome_scene_revisit_kira
        "kira/nate/simone threesome revisit (ask simone)":
            call kira_simone_threesome_scene_revisit_simone
        "kira_simone_threesome_scene_revisit_1st_time with trigger enabled":
            $ scenes_completed.add("simone_scene_vaginal")
            $ scenes_completed.add("kira_scene_anal")
            call kira_simone_threesome_scene_revisit_1st_time
        "kira_simone_threesome_scene_revisit_2nd_time with trigger enabled":
            $ scenes_completed.add("simone_scene_vaginal")
            $ scenes_completed.add("kira_scene_anal")
            call kira_simone_threesome_scene_revisit_2nd_time
        "kira_simone_threesome_extended_content_1st_time":
            call kira_simone_threesome_extended_content_1st_time
        "kira_simone_threesome_extended_content_2nd_time":
            call kira_simone_threesome_extended_content_2nd_time
        "sam_julia_threesome_scene_sex":
            call sam_julia_threesome_scene_sex
        "sam_julia_threesome_scene_revisit_sam":
            call sam_julia_threesome_scene_revisit_sam
        "sam_julia_threesome_scene_revisit_julia":
            call sam_julia_threesome_scene_revisit_julia
        "family_foursome_scene_sex":
            call family_foursome_scene_sex
        "family_foursome_scene_revisit_kira":
            call family_foursome_scene_revisit_kira
        "family_foursome_scene_revisit_sam":
            call family_foursome_scene_revisit_sam
        "family_foursome_scene_revisit_simone":
            call family_foursome_scene_revisit_simone
        "Назад":

            call debug_menu
    return

label debug_choice:
    menu:
        "1":
            pass
        "2":
            pass
        "3":
            pass
        "4":
            pass
        "5":
            pass
        "6":
            pass
        "7":
            pass
        "8":
            pass
        "9":
            pass
        "10":
            pass
        "11":
            pass
        "12":
            pass
        "13":
            pass
        "14":
            pass
        "15":
            pass
        "16":
            pass
        "17":
            pass
        "18":
            pass
        "19":
            pass

    call debug_menu

    return

label debug_scene:
    call prompt_menu_boldness_check ("Accept Test Scene", "Refuse Test Scene", "debug_scene", debug_character)

    return

label debug_scene_refusal(text, insufficient_points):
    "Тестовая сцена отказа"
    call prompt_refusal_end (debug_character)
    return

label debug_scene_sex:
    "Это тестовая сцена"

    call process_end_of_scene ("debug_scene", debug_character, skip_adding_to_completed_scenes=True, force_not_replayable=True)

    return

label debug_current_build_notes:
    return

label debug_message(message):
    if config.developer:
        $ debug_message = "(DEBUG) " + message
        "[debug_message]"

    return

label debug_max_money:
    $ inventory.add_money(9999)
    "Добавлено максимум денег"
    if started_main_game:
        $ advance_time_return_location.start()
    return

label debug_minigame_instant(char):
    $ char.add_points(2)
    "DEBUG: Добавлено +2 очка [char.say_name]"

    call day_advance_time

    return

label debug_cum_test:
    call process_scene_beginning ("bg nate_room", char_tuple_array=[ (n, "pose behindhead face flirty outfit nudehard blush true"), (k, "pose armcross") ])

    call process_character (n, appearance="overlay cum_dick")
    call process_character (k, appearance="overlay cum_face")

    call process_end_of_scene ("", k)

    return

label debug_start_new_day(cheats=False):
    call initialize_variables (force_reinitialization=True)

    if cheats:
        python hide:
            chars = npc_list()
            for char in chars:
                char.add_points(999, force_no_popup = True)

            inventory.add_money(999)
            stats.add_boldness_xp(999, force_no_popup = True)


        "Добавлено 999 очков каждому персонажу и добавлено 999 xp Смелости и добавлено максимум денег"

    call debug_day

    return

label debug_boldness:
    menu:
        "Значение 1":
            $ stats.boldness_level = 1
            $ stats.boldness_xp = 0
        "Добавить 999 очков":
            call debug_boldness_999
    call debug_menu

    return

label debug_boldness_999:
    $ stats.add_boldness_xp(999)
    "Добавлено 999 очков Смелости"
    if started_main_game:
        $ advance_time_return_location.start()
    return

label debug_boldness_2:
    $ stats.add_boldness_xp(2)
    "Добавлено 2 очка Смелости"
    if started_main_game:
        $ advance_time_return_location.start()
    return

label debug_day:
    $ started_main_game = True
    call day_start

    return

label debug_minigame:
    menu:
        "Мини-игра Математика":
            call minigame_math
        "Мини-игра набор слов":
            call minigame_typing_review
        "Мини-игра гонки":
            call minigame_racing
        "Мини-игра передвижные головоломки":
            call minigame_slide_puzzle
        "Мини-игра повтор":
            call minigame_repeat_pattern
        "Мини-игра чтение":
            call minigame_reading
        "Мини-игра настольный теннис":


            call minigame_table_tennis (edna)

    return

label debug_character:
    menu:
        "Kira Debug":
            call debug_kira
        "Sam Debug":
            call debug_sam
        "Simone Debug":
            call debug_simone
        "Julia Debug":
            call debug_julia
        "Janet Debug":
            call debug_janet
        "Kacey Debug":
            call debug_kacey
        "Vicky Debug":
            call debug_vicky
        "Edna Debug":
            call debug_edna
        "Назад":
            call debug_menu
    return

label debug_vicky:
    menu:
        "Vicky Scenes":
            call debug_vicky_scenes
        "Back":
            call debug_character
    return

label debug_vicky_scenes:
    menu:
        "vicky_pre_intro":
            call vicky_pre_intro
        "vicky_intro":
            call vicky_intro
        "vicky_tease_scene":
            call vicky_tease_scene
        "vicky_fondle_scene":
            call vicky_fondle_scene_sex
        "vicky_titjob_scene":
            call vicky_titjob_scene_sex
        "vicky_titjob_scene_revisit":
            call vicky_titjob_scene_revisit
        "vicky_scene_blowjob":
            call vicky_scene_blowjob_sex
        "vicky_scene_blowjob_revisit":
            call vicky_scene_blowjob_revisit
        "vicky_scene_vaginal":
            call vicky_scene_vaginal_sex
        "vicky_scene_vaginal_revisit":
            call vicky_scene_vaginal_revisit
        "vicky_scene_anal":
            call vicky_scene_anal
        "vicky_scene_anal_revisit":
            call vicky_scene_anal_revisit
        "Назад":
            call debug_character

    return

label debug_kacey:
    menu:
        "Kacey Scenes":
            call debug_kacey_scenes
        "Назад":
            call debug_character
    return

label debug_kacey_scenes:
    menu:
        "Kacey handjob":
            call gloryhole_handjob_scene_sex
        "Kacey handjob revisit":
            call gloryhole_handjob_scene_revisit
        "Kacey blowjob":
            call gloryhole_scene_blowjob_sex
        "Kacey blowjob revisit":
            call gloryhole_scene_blowjob_revisit
        "Kacey vaginal":
            call gloryhole_scene_vaginal_sex
        "Kacey vaginal revisit":
            call gloryhole_scene_vaginal_revisit
        "Kacey anal":
            call gloryhole_scene_anal_sex
        "Kacey anal revisit":
            call gloryhole_scene_anal_revisit
        "Kacey stall":
            call gloryhole_scene_stall
        "Kacey stall revisit":
            call gloryhole_scene_stall_revisit
        "Назад":
            call debug_character

    return

label debug_character_conversations(char, background="bg nate_room"):
    call reset_all_characters

    python:

        choice_list = []

        for i in range(1, char.conversation_max() + 1):
            choice = char.internal_name + "_convo_" + str(i)
            choice_list.append( ( choice, choice ) )

        chosen_option = renpy.display_menu(choice_list)

    call bust_art_background (background)
    $ renpy.call(chosen_option)
    call debug_menu
    return

label debug_simone:
    menu:
        "Simone Scenes":
            call debug_simone_scenes
        "Simone Conversations":
            call debug_character_conversations (si, simone_room)
    return

label debug_simone_scenes:
    menu:
        "simone_swimsuit_scene":
            call simone_scene_swimsuit_sex
        "simone_scene_1_seq_1":
            call simone_scene_1_seq_1_sex
        "simone_scene_1_revisit":
            call simone_scene_1_revisit
        "simone 2 (simone watches nate masturbate 1)":
            call simone_scene_2_sex
        "simone 3 (simone watches nate masturbate 2)":
            call simone_scene_3_sex
        "simone 3 revisit (simone watches nate masturbate revisit)":
            call simone_scene_3_revisit
        "simone yoga 1":
            call simone_scene_yoga_1_sex
        "simone yoga 2":
            call simone_scene_yoga_2_sex
        "simone 4 (underwear)":
            call simone_scene_4
        "simone undressing":
            call simone_scene_undressing
        "simone masturbation":
            call simone_scene_masturbating_sex
        "simone handjob":
            call simone_scene_garden_handjob_sex
        "simone handjob revisit":
            call simone_scene_garden_handjob_revisit
        "simone bares all scene":
            call simone_scene_bares_all_sex
        "simone bares all scene revisit":
            call simone_scene_bares_all_revisit
        "simone blowjob":
            call simone_scene_blowjob_sex
        "simone blowjob revisit":
            call simone_scene_blowjob_revisit
        "simone vaginal":
            call simone_scene_vaginal
        "simone vaginal revisit":
            call simone_scene_vaginal_revisit
        "simone anal":
            call simone_scene_anal
        "simone anal revisit":
            call simone_scene_anal_revisit
        "simone titfuck":
            call simone_scene_titfuck
        "simone titfuck revisit":
            call simone_scene_titfuck_revisit
        "Назад":
            call debug_character
    return

label debug_julia:
    menu:
        "Julia Conversations":
            call debug_character_conversations (julia, living_room)
        "Julia Scenes":
            call debug_julia_scenes
    return

label debug_julia_scenes:
    menu:
        "Julia minigame intro":
            call minigame_julia_book_first_time_intro
        "Julia pre arrival scene":
            call julia_pre_arrival
        "Julia arrives scene":
            call julia_arrival
        "julia underwear":
            call julia_scene_underwear_sex
        "julia topless":
            call julia_scene_topless_sex
        "julia bottomless":
            call julia_scene_bottomless_sex
        "julia nude":
            call julia_scene_nude_sex
        "julia_scene_post_nude":
            call julia_scene_post_nude
        "julia_scene_footjob":
            call julia_scene_footjob
        "julia_scene_footjob_revisit":
            call julia_scene_footjob_revisit
        "julia_scene_blowjob":
            call julia_scene_blowjob
        "julia_scene_blowjob_revisit":
            call julia_scene_blowjob_revisit
        "julia_scene_vaginal":
            call julia_scene_vaginal
        "julia_scene_vaginal revisit":
            call julia_scene_vaginal_revisit
        "julia_scene_post_vaginal":
            call julia_scene_post_vaginal
        "julia_scene_anal":
            call julia_scene_anal
        "julia_scene_anal revisit":
            call julia_scene_anal_revisit
        "Назад":

            call debug_character

    return

label debug_edna:
    menu:
        "edna Scenes":
            call debug_edna_scenes
        "edna Conversations":
            call debug_character_conversations (edna, nate_room)
    return

label debug_edna_scenes:
    menu:
        "edna prearrival scene":
            call edna_pre_arrival_scene
        "edna arrival scene":
            call edna_arrival_scene
        "edna intro 2":
            call edna_scene_intro_2
        "edna minigame intro":
            call edna_scene_minigame_intro
        "edna nate underwear":
            call edna_scene_nate_underwear
        "edna underwear":
            call edna_scene_underwear
        "edna swimsuit":
            call edna_scene_swimsuit
        "edna nate naked":
            call edna_scene_nate_naked
        "edna topless":
            call edna_scene_topless
        "edna bottomless":
            call edna_scene_bottomless
        "edna naked":
            call edna_scene_naked
        "edna_scene_titfuck":
            call edna_scene_titfuck
        "edna_scene_titfuck_revisit":
            call edna_scene_titfuck_revisit
        "edna_scene_handjob":
            call edna_scene_handjob
        "edna_scene_handjob_revisit":
            call edna_scene_handjob_revisit
        "edna_scene_blowjob_revisit":
            call edna_scene_blowjob_revisit
        "edna_scene_blowjob":
            call edna_scene_blowjob
        "Back":
            call debug_character

    return

label debug_janet:
    menu:
        "janet Scenes":
            call debug_janet_scenes
        "janet Conversations":
            call debug_character_conversations (janet, nate_room)
    return

label debug_janet_scenes:
    menu:
        "janet_intro":
            call janet_intro
        "janet_scene_intro_2":
            call janet_scene_intro_2_sex
        "janet_scene_minigame_intro":
            call janet_scene_minigame_intro
        "janet_scene_underwear":
            call janet_scene_underwear
        "janet_scene_topless":
            call janet_scene_topless
        "janet_scene_bottomless":
            call janet_scene_bottomless
        "janet_scene_naked":
            call janet_scene_naked
        "janet_scene_blowjob":
            call janet_scene_blowjob
        "janet_scene_blowjob_revisit":
            call janet_scene_blowjob_revisit
        "janet_scene_vaginal":
            call janet_scene_vaginal
        "janet_scene_vaginal revisit":
            call janet_scene_vaginal_revisit
        "janet_scene_anal_sex":
            call janet_scene_anal_sex
        "janet_scene_anal_revisit":
            call janet_scene_anal_revisit
        "Назад":
            call debug_character
    return

label debug_sam:
    menu:
        "Sam Scenes":
            call debug_sam_scenes
        "Sam Conversations":
            call debug_character_conversations (sa, sam_room)
    return

label debug_sam_scenes:
    menu:
        "sam swimsuit":
            call sam_scene_swimsuit_sex
        "sam swimsuit_revisit":

            call sam_scene_swimsuit_revisit
        "add grinding scene history":

            $ scenes_completed.add("sam_scene_4")
            "added"
            call debug_sam_scenes
        "add vaginal scene history":

            $ scenes_completed.add("sam_scene_vaginal")
            "added"
            call debug_sam_scenes
        "sam_scene_1_seq_1":

            call sam_scene_1_seq_1_sex
        "sam_scene_1_seq_2":
            call sam_scene_1_seq_2_sex
        "sam_scene_1_revisit":

            call sam_scene_1_revisit
        "sam_scene_2_seq_1":

            call sam_scene_2_seq_1_sex
        "sam_scene_2_seq_2":
            call sam_scene_2_seq_2_sex
        "sam_scene_2_revisit":

            call sam_scene_2_revisit
        "sam 3(topless streaming)":

            call sam_scene_3_sex
        "sam 3 revisit (topless streaming)":

            call sam_scene_3_revisit
        "sam 4 (grinding)":

            call sam_scene_4_sex
        "sam_scene_4_revisit":

            call sam_scene_4_revisit
        "sam_scene_vaginal":

            call sam_scene_vaginal_sex
        "sam_scene_vaginal_revisit":

            call sam_scene_vaginal_revisit
        "sam_scene_blowjob":

            call sam_scene_blowjob
        "sam_scene_blowjob_revisit":

            call sam_scene_blowjob_revisit
        "sam_scene_anal":

            call sam_scene_anal
        "sam_scene_anal_revisit":

            call sam_scene_anal_revisit
        "sam_scene_dream":

            call sam_scene_dream
        "Назад":

            call debug_character
    return


label debug_kira:
    menu:
        "Сцены с Кирой":
            call debug_kira_scenes
        "Разговоры с Кирой":

            call debug_character_conversations (k, kira_room)

    return

label debug_kira_scenes:

    menu:
        "kira_scene_1_seq_1":
            call kira_scene_1_seq_1_sex
        "kira_scene_1_seq_2":

            call kira_scene_1_seq_2_sex
        "kira_scene_1_revisit":

            call kira_scene_1_revisit
        "kira_scene_2_seq_1":

            call kira_scene_2_seq_1_sex
        "kira_scene_2_seq_2":

            call kira_scene_2_seq_2_sex
        "kira_scene_2_revisit":

            call kira_scene_2_revisit
        "kira_scene_3":

            call kira_scene_3_sex
        "kira_scene_3 revisit":

            call kira_scene_3_revisit
        "kira 4 (bikini)":

            call kira_scene_4
        "kira 5 (thong)":

            call kira_scene_5
        "kira 6 (topless bikini)":

            call kira_scene_6
        "kira 6 (topless bikini) revisit":

            call kira_scene_6_revisit
        "kira 7 (bottomless)":

            call kira_scene_7
        "kira 8 (titfuck)":

            call kira_scene_8_sex
        "kira 8 (titfuck) revisit":

            call kira_scene_8_revisit
        "kira tip bj":

            call kira_scene_tip_blowjob_sex
        "kira tip bj revisit":

            call kira_scene_tip_blowjob_revisit
        "kira anal":

            call kira_scene_anal
        "kira anal revisit":

            call kira_scene_anal_revisit
        "kira vaginal":

            call kira_scene_vaginal
        "kira vaginal revisit":

            call kira_scene_vaginal_revisit
        "kira stealth bj":

            call kira_scene_stealth_bj_sex
        "kira_scene_pool_fuck":

            call kira_scene_pool_fuck
        "kira_scene_pool_fuck_revisit":

            call kira_scene_pool_fuck_revisit
        "Назад":


            call debug_character

    return