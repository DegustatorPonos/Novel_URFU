image input_caret:
    yoffset -5
    Text("|")
    pause 0.5
    alpha 0.0
    pause 0.5
    alpha 1.0
    repeat

init python:
    preferences.skip_unseen = True
    config.label_overrides['_hide_windows'] = '_hide_windows_with_characters'

    style.input.caret = "input_caret"
    config.layers = [ 'master', 'transient', 'screens', 'cumbox', 'characters', 'overlay', 'scripts' ]


    style.default.outlines = [(2, "#000000", 0, 0)]


    gui.hover_color = "#a223cc" 


    gui.button_text_idle_color = "#ffffff"
    gui.button_text_hover_color = gui.hover_color
    gui.button_text_selected_color = gui.hover_color
    gui.button_text_insensitive_color = "#9e9e9e"


    style.radio_button_text.idle_color = "#9e9e9e"
    style.radio_button_text.selected_color = "#ffffff"
    style.radio_button_text.hover_color = gui.hover_color


    style.check_button_text.idle_color = "#9e9e9e"
    style.check_button_text.selected_color = "#ffffff"
    style.check_button_text.hover_color = gui.hover_color


    gui.quick_button_text_idle_color = "#ffffff"


    gui.check_button_borders = Borders(38, 0, 0, 0)


    gui.name_xpos = 625
    gui.name_xalign = 0.0
    gui.name_ypos = 60
    gui.namebox_width = 9999


    gui.text_xpos = 650
    gui.text_ypos = 120
    gui.text_ypos_no_who = 95
    gui.text_width = 720


    gui.text_padding_review_minigame = 16
    gui.text_xpos_typing_review_minigame = 300 + gui.text_padding_review_minigame
    gui.text_width_typing_review_minigame = 1320 - (gui.text_padding_review_minigame * 2)
    gui.text_ypos_typing_review_minigame = 70


    gui.textbox_yalign = 0.960


    gui.default_font = "fonts/RobotoCondensed-Regular.ttf"


    gui.name_font = "fonts/RobotoCondensed-Regular.ttf"


    gui.interface_font = "fonts/RobotoCondensed-Regular.ttf"

    def main_menu_button_displayable(is_disabled = False, is_hover = False, text = "", text_size = 60):
        button_image = "images/buttons/MenuIcon.png"
        if is_hover:
            button_image = "images/buttons/MenuIconRollover.png"
        if is_disabled:
            button_image = "images/buttons/MenuIcon_disabled.png"
        
        return Fixed(Image(button_image), Text(text, xalign=0.5, yalign = 0.5, size = text_size, yoffset = -5), xysize=(300, 75))

    def character_layer():
        return 'characters'

init:
    screen main_menu_button(text="", action=None, xalign=0.0, yalign=0.0, enabled=True, text_size=60):
        imagebutton idle main_menu_button_displayable(text = text, text_size = text_size) hover main_menu_button_displayable(is_hover = True, text = text, text_size = text_size) insensitive main_menu_button_displayable(is_disabled = True, text = text, text_size = text_size) action If(enabled, Function(action), None) xalign xalign yalign yalign

    style pref_vbox:
        xsize None

    screen keyboard_help():

        hbox:
            label _("Enter")
            text _("Advances dialogue and activates the interface.")

        hbox:
            label _("Space")
            text _("Advances dialogue without selecting choices.")

        hbox:
            label _("WASD, Arrow Keys")
            text _("Navigate the interface.")

        hbox:
            label _("Escape")
            text _("Accesses the game menu.")

        hbox:
            label _("Ctrl")
            text _("Skips dialogue while held down.")

        hbox:
            label _("Tab")
            text _("Toggles dialogue skipping.")

        hbox:
            label _("Q, Page Up")
            text _("Rolls back to earlier dialogue.")

        hbox:
            label _("E, Page Down")
            text _("Rolls forward to later dialogue.")

        hbox:
            label "H"
            text _("Hides the user interface.")

        hbox:
            label "Print Screen"
            text _("Takes a screenshot.")







    screen main_menu() tag menu:




        style_prefix "main_menu"

        if not wholesome_mode:
            if not persistent.sfw_mode:
                add "gui/main_menu.png"
                text config.name style "default" size 120 xalign 0.5
        else:
            text "Bugs have not been patched" xalign 0.5 yalign 0.7 size 92
            text "IA Tech Demo" style "default" size 120 xalign 0.5
            text config.version xalign 0.99 yalign 0.99 size 60


        vbox:
            xalign 0.95
            yalign 0.4
            spacing 30
            use main_menu_button(text="Новая Игра", action=Start )

            if not wholesome_mode:
                use main_menu_button(text="Загрузить", action=ShowMenu("load") )

            use main_menu_button(text="Настройки", action=ShowMenu("preferences") )
            use main_menu_button(text="FAQ", action=Jump("help") )
            use main_menu_button(text="Выход", action=Quit(confirm = not main_menu))

        if not wholesome_mode:
            textbutton "Поддержка Перевода" action OpenURL("http://no-spec.ru/") xalign 0 yalign 0.99
            add ResponsiveTextButton(unfocused_text = "Версия [config.version]", focused_text = "{color=" + gui.hover_color + "}Изменения{/color}", text_size = 40, clicked = OpenURL("https://iathegame.blogspot.com/2018/07/changelog.html")) xalign 0.99 yalign 0.99














    screen say(who, what):
        style_prefix "say"

        window:
            id "window"

            if who is not None:

                window:
                    style "namebox"
                    if not use_namebox or not last_say_position or last_say_position == "left":
                        xpos gui.name_xpos
                    else:
                        xpos 1295

                    text who id "who"

            if who is not None:
                text what id "what"
            else:
                text what id "what" ypos gui.text_ypos_no_who




        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0

    screen file_slots(title):

        default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

        use game_menu(title):

            fixed:



                order_reverse True


                button:
                    style "page_label"

                    key_events True
                    xalign 0.5
                    action page_name_value.Toggle()

                    input:
                        style "page_label_text"
                        value page_name_value


                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"

                    xalign 0.5
                    yalign 0.5

                    spacing gui.slot_spacing

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):

                        $ slot = i + 1

                        button:
                            action FileAction(slot)

                            has vbox

                            add FileScreenshot(slot) xalign 0.5

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            text FileSaveName(slot):
                                style "slot_name_text"

                            key "save_delete" action FileDelete(slot)


                hbox:
                    style_prefix "page"

                    xalign 0.5
                    yalign 1.0

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()



                    textbutton _("{#quick_page}Q") action FilePage("quick")


                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()






    screen navigation():

        vbox:
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5

            spacing gui.navigation_spacing

            if main_menu:

                textbutton _("Start") action Start()

            else:

                textbutton _("История") action ShowMenu("history")

                textbutton _("Сохранение") action If(store.disable_saves, None, ShowMenu("save"))

            if not wholesome_mode:
                textbutton _("Загрузка") action ShowMenu("load")

            if not main_menu:
                if display_new_game_plus_option:
                    textbutton _("Новая Игра+") action Confirm("Новая Игра+ позволяет начать новую игру, сохраняя награды за мини-игры. Любой другой прогресс не будет перенесен. Вы уверены, что хотите это сделать?", Jump("new_game_plus_label"))

            textbutton _("Настройки") action ShowMenu("preferences")

            if _in_replay:

                textbutton _("Закончить повтор") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("Главное Меню") action MainMenu()

            textbutton _("О...") action ShowMenu("about")


            if renpy.variant("pc"):


                textbutton _("Помощь") action ShowMenu("help")


                textbutton _("Выход") action Quit(confirm=not main_menu)






    screen quick_menu():


        zorder 100

        if quick_menu:

            hbox:
                style_prefix "quick"

                xalign 0.5
                yalign 1.0

                textbutton _("Скрыть интерфейс") action HideInterface()

                if config.rollback_enabled:
                    textbutton _("Назад") action Rollback()
                else:
                    textbutton _("Назад")

                textbutton _("История") action ShowMenu('history')
                textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Авто") action Preference("auto-forward", "toggle")

                textbutton _("Сохранение") action If(store.disable_saves, None, ShowMenu("save"))
                textbutton _("Быстрое сохранение") action If(store.disable_saves, None, QuickSave())

                if not wholesome_mode:
                    textbutton _("Быстрая загрузка") action QuickLoad()
                textbutton _("Настройки") action ShowMenu('preferences')








    screen music_disable_vbox(music_disable_array):
        hbox:
            vbox:
                for music_disable_option_name in music_disable_array:
                    textbutton _( music_disable_option_name.get("filename_display_title") ) action InvertSelected( ToggleSetMembership(persistent.disabled_music, music_disable_option_name.get("filename_display_title") ) )
            vbox:
                for music_disable_option_name in music_disable_array:
                    hbox:
                        textbutton "Тест" action Function(sound_test, music_disable_option_name.get("path") )
                        textbutton "Стоп" action Function(stop_music)

    screen preferences() tag menu:



        if renpy.mobile:
            $ cols = 2
        else:
            $ cols = 4

        if not wholesome_mode:
            use game_menu(_("Preferences"), scroll="viewport"):

                vbox:

                    hbox:
                        spacing 50
                        box_wrap True

                        if renpy.variant("pc"):

                            vbox:
                                style_prefix "radio"
                                label _("Настройки экрана")
                                textbutton _("В окне") action Preference("display", "window")
                                textbutton _("Полноэкранно") action Preference("display", "fullscreen")

                        vbox:
                            style_prefix "radio"
                            label _("Сторона Отката")
                            textbutton _("Выключить") action Preference("rollback side", "disable")
                            textbutton _("Слева") action Preference("rollback side", "left")
                            textbutton _("Справа") action Preference("rollback side", "right")

                        vbox:
                            style_prefix "check"
                            label _("Пропуск текста")
                            textbutton _("После выбора") action Preference("after choices", "toggle")
                            textbutton _("Переходы") action InvertSelected(Preference("transitions", "toggle"))

                        vbox:
                            style_prefix "check"
                            label _("Extra")

                            if not wholesome_mode:

                                textbutton _("Отключить Предупреждения") action ToggleField(persistent, 'disable_warning', True, False)
                                textbutton _("Отключить Музыку во сне") action ToggleField(persistent, 'disable_dream_music', True, False)
                                textbutton _("Отключить Размытие Снов") action ToggleField(persistent, 'disable_dream_blur', True, False)
                                textbutton _("Включить звуки секса") action ToggleField(persistent, 'enable_sex_sounds', True, False)
                                textbutton _("Прокрутка выбора колесом мыши") action ToggleField(persistent, 'mouse_wheel_choice_scroll', True, False)
                                textbutton _("Использовать \"Incestral Awakening\" как название") action ToggleField(persistent, 'use_incestral_awakening_name', True, False)

                                if not main_menu:
                                    textbutton _("Скрыть [sa.say_name] ! Уведомление") action ToggleField(persistent, 'hide_sam_notification', True, False)
                                    textbutton _("Скрыть [si.say_name] ! Уведомление") action ToggleField(persistent, 'hide_simone_notification', True, False)
                                    textbutton _("Скрыть [k.say_name] ! Уведомление") action ToggleField(persistent, 'hide_kira_notification', True, False)

                                    if store.had_julia_arrived_scene:
                                        textbutton _("Скрыть [julia.say_name] ! Уведомление") action ToggleField(persistent, 'hide_julia_notification', True, False)

                                    if store.had_janet_intro_scene:
                                        textbutton _("Скрыть [janet.say_name] ! Уведомление") action ToggleField(persistent, 'hide_janet_notification', True, False)

                                    if store.had_edna_intro_scene:
                                        textbutton _("Скрыть [edna.say_name] ! Уведомление") action ToggleField(persistent, 'hide_edna_notification', True, False)

                                    if store.had_vicky_intro_scene:
                                        textbutton _("Скрыть Вики ! Уведомление") action ToggleField(persistent, 'hide_vicky_notification', True, False)

                                    if "gloryhole_handjob_scene" in store.scenes_completed:
                                        textbutton _("Скрыть Кэйси ! Уведомление") action ToggleField(persistent, 'hide_kacey_notification', True, False)
                                    else:
                                        textbutton _("Скрыть Парк ! Уведомление") action ToggleField(persistent, 'hide_kacey_notification', True, False)

                                if config.developer and show_sfw_option:
                                    textbutton _("Режим \"SFW\" Отладки") action ToggleField(persistent, 'sfw_mode', True, False)

                    hbox:
                        style_prefix "slider"
                        box_wrap True

                        vbox:

                            label _("Скорость текста")

                            bar value Preference("text speed")

                            label _("Скорость автоматического пропуска")

                            bar value Preference("auto-forward time")

                        vbox:

                            if config.has_music:
                                label _("Громкость музыки")

                                hbox:
                                    bar value Preference("music volume")

                            if config.has_sound:

                                label _("Громкость звука")

                                hbox:
                                    bar value Preference("sound volume")

                                    if config.sample_sound:
                                        textbutton _("Тест") action Play("sound", config.sample_sound)


                            if config.has_voice:
                                label _("Громкость голоса")

                                hbox:
                                    bar value Preference("voice volume")

                                    if config.sample_voice:
                                        textbutton _("Тест") action Play("voice", config.sample_voice)

                            if config.has_music or config.has_sound or config.has_voice:
                                null height gui.pref_spacing

                                textbutton _("Выключить звук"):
                                    action Preference("all mute", "toggle")
                                    style "mute_all_button"


                    if main_menu:
                        vbox:
                            label _("Дневная (Домашняя) Музыка")
                            style_prefix "check"
                            use music_disable_vbox(disable_audio_filenames( home_daytime_music_list() ) )

                        vbox:
                            label _("Вечерняя (Домашняя) Музыка")
                            style_prefix "check"
                            use music_disable_vbox(disable_audio_filenames( home_evening_music_list() ) )











    screen input(prompt):
        style_prefix "input"

        window:

            if store.name_input_color:
                $ input_color = name_input_color
            else:
                $ input_color = gui.accent_color

            if minigame_typing_review_started:
                $ input_prompt_xpos = gui.text_xpos_typing_review_minigame
                $ input_prompt_xalign = gui.text_xalign
                $ input_prompt_ypos = gui.text_ypos_typing_review_minigame
                $ input_prompt_xmaximum = gui.text_width_typing_review_minigame
            else:
                $ input_prompt_xpos = gui.text_xpos
                $ input_prompt_xalign = gui.text_xalign
                $ input_prompt_ypos = gui.text_ypos_no_who
                $ input_prompt_xmaximum = gui.text_width

            vbox:
                xpos input_prompt_xpos

                xalign input_prompt_xalign

                ypos input_prompt_ypos

                xmaximum input_prompt_xmaximum

                text prompt style "default"

                input id "input" color input_color xmaximum 9999








define gui.choice_button_borders = Borders(175, 8, 175, 8)
screen choice(items):
    style_prefix "choice"

    frame:
        background None
        yalign 0.55
        xalign 0.5
        has side "c r":
            area 0, 0, 1280, 720
        viewport id "choice_screen":
            mousewheel persistent.mouse_wheel_choice_scroll
            has vbox:
                xfill True
                spacing 0

            for i in items:
                textbutton i.caption action i.action xalign 0.5

        vbar value YScrollValue('choice_screen') unscrollable "hide" xsize 36

label _hide_windows_with_characters:

    if renpy.context()._menu:
        return

    if _windows_hidden:
        return

    python hide:
        for char in characters_shown:
            process_character_replace_utility(eval(char), appearance = "yea")

    python:
        _windows_hidden = True
        voice_sustain()
        ui.saybehavior(dismiss=['dismiss', 'hide_windows'])


        ui.interact(suppress_overlay=True, suppress_window=True)
        _windows_hidden = False

    return