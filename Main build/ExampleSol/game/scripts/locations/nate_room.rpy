label nate_room_empty:
    $ renpy.set_return_stack([])
    $ renpy.checkpoint()
    $ quick_menu = True
    $ enable_saving()
    $ enable_rollback()
    show screen hud_zone_select
    show screen hud

    python hide:
        renpy.start_predict_screen("gallery")
        for char in npc_list():
            renpy.start_predict_screen("character_gallery", char)

    python:
        choice_list = []

        if not wholesome_mode:
            choice_list.append( ("Спать", "day_manual_sleep") )
            if "finale_scene" in store.scenes_completed:
                if not epilogue_completed:
                    choice_list.append( ("Эпилог (Новое!)", "epilogue") )
                else:
                    choice_list.append( ("Эпилог", "epilogue") )
                
                choice_list.append( ("Устроить Вечеринку у бассейна", "nate_room_finale_scene_revisit_confirm") )
            choice_list.append( ("Мини-игры", "nate_room_minigame") )
            choice_list.append( ("Статы", "nate_room_stats") )
            choice_list.append( ("Магазин", "nate_room_shopping") )
            choice_list.append( ("Переименовать", "nate_room_rename_characters") )

        choice_list.append( ("Галерея", "nate_room_gallery") )
        choice_list.append( ("Изменения", "nate_room_changelog") )

        if config.developer:
            choice_list.append( ("(DEBUG) +2 к Смелости", "debug_boldness_2") )
            choice_list.append( ("(DEBUG) +999 к Смелости", "debug_boldness_999") )
            choice_list.append( ("(DEBUG) Максимум денег", "debug_max_money") )

        choice_list.append( ("Назад", "back") )

        chosen_option = renpy.display_menu(choice_list)

    if chosen_option == "back":
        call navigation_menu ()
    else:
        $ renpy.call(chosen_option)

    return

label nate_room_finale_scene_revisit_confirm:
    "{i}Позвать всех на вечеринку?{/i}"
    menu:
        "Да":
            jump finale_scene_revisit
        "Нет":
            jump nate_room_empty

    return

label nate_room_gallery:
    jump gallery
    return

label nate_room_rename_characters:

    $ renpy.scene('screens')

    $ process_character(si, "position right")
    call change_character_name (si, "Моя Мама")

    $ clear_characters()
    $ process_character(k, "position right")
    call change_character_name (k, "Моя старшая сестра")

    $ clear_characters()
    $ process_character(sa, "position right")
    call change_character_name (sa, "Моя сестра-близнец")

    if had_julia_arrived_scene:
        $ clear_characters()
        $ process_character(julia, "position right")
        call change_character_name (julia, "Моя кузина")

    if had_janet_intro_scene:
        $ clear_characters()
        $ process_character(janet, "position right")
        call change_character_name (janet, "Моя Тётя")

    if had_edna_intro_scene:
        $ clear_characters()
        $ process_character(edna, "position right")
        call change_character_name (edna, "Моя Бабушка")

    $ clear_characters()
    $ process_character(n, "position right")
    call change_character_name (n, "Моё имя")

    python:
        last_name = renpy.input("Моя фамилия", default = last_name, length = 14)

    call update_last_names
    $ clear_characters()

    call nate_room_empty

    return

label nate_room_changelog:
    $ quick_menu = False
    $ renpy.scene('screens')
    show screen changelog
    pause
    $ renpy.scene('screens')
    jump nate_room_empty
    return

label nate_room_shopping:
    menu:
        "Товар":
            call nate_room_shopping_general
        "Назад":
            call nate_room_empty

    return

label nate_room_shopping_general:
    window hide
    call buy_menu (visible_items_with_tag("general"), "nate_room_shopping", "nate_room_shopping_general")
    return

label nate_room_stats:
    call screen stats

    return

label nate_room_minigame:
    menu:
        "Мини-игра Обзор Игр":
            call minigame_typing_review
        "Назад":
            call nate_room_empty
    return

label nate_room_computer_buy:
    $ renpy.call_screen("buy_menu", inventory.store_buy_list_nate_computer(), "nate_room_empty", "nate_room_computer_buy")
    return