screen splash_text:
    vbox:
        xalign 0.5
        yalign 0.5

        text "{b}ТОЛЬКО ДЛЯ ВЗРОСЛЫХ{/b}" size 60 xalign 0.5
        text "Вам должно быть 18 лет или больше, чтобы запускать эту игру!" size 48 xalign 0.5
        text "Все персонажи 18+" size 48 xalign 0.5
        text "" size 48 xalign 0.5

image splash_ctc:
    alpha 0.0
    Text("Кликните в любом месте, чтобы продолжить...", xalign=0.5, yalign = 0.7, size = 48)
    linear 1.0 alpha 1.0
    pause 1.0
    linear 1.0 alpha 0.0
    repeat

default persistent.alpha_037_1_changelog_read = False
default persistent.alpha_038_1_changelog_read = False
default persistent.alpha_039_1_changelog_read = False
default persistent.alpha_040_1_changelog_read = False
default persistent.alpha_041_1_changelog_read = False
default persistent.alpha_042_1_changelog_read = False
default persistent.alpha_043_2_changelog_read = False
default persistent.alpha_044_1_changelog_read = False
default persistent.alpha_044_2_changelog_read = False
default persistent.alpha_045_1_changelog_read = False
default persistent.alpha_046_1_changelog_read = False
default persistent.alpha_047_1_changelog_read = False
default persistent.alpha_047a_1_changelog_read = False
default persistent.alpha_048_1_changelog_read = False
default persistent.alpha_049_1_changelog_read = False
default persistent.alpha_049a_1_changelog_read = False
default persistent.alpha_050_1_changelog_read = False
default persistent.alpha_051_1_changelog_read = False
default persistent.version_1_changelog_read = False


screen changelog:
    frame:
        has viewport:
            mousewheel True
            scrollbars "vertical"

        vbox:
            text "{b}1.0-Изменения (4/29/19)\n\nНовый контент:\n-Добавлена сцена эпилога!{/b} Требуется, чтобы вы завершили финальную сцену. Происходит в спальне игрока.\n-{b} Игра завершена!{/b}  Будущие обновления будут сосредоточены на исправлении ошибок и, возможно, добавлении поддержки модов.\n\n{b}Правки:{/b}\n-Бабушка Эдна теперь появляется перед Кейси и Вики на экране статистики.\n\n{b}Устранение Ошибок:{/b}\n-Исправлена опечатка в одной из сцен бабушки Эдны.\n-Бабушка Эдна больше не надевает одежду в повторной сцене минета.\n{b}0.51 Изменения (3/4/19)\n\nНовый контент:{/b}\n-Добавлена новая сцена с Бабушкой Эдной! Требуется уровень отношений 12.\n\n{b}Правки:{/b}\n\n-Теперь все персонажи отображаются на экране статистики персонажей, если они еще не встречались, их имя и портрет скрыты.\n-Добавлены Кейси и Вики на экран статистики.\n\n{b}Устранение Ошибок:{/b}\n-Исправлена опечатка в повторной финальной групповой сцене.\n-Исправлена опечатка в повторной сцене с тройничком с Мамой Симоной и старшей сестрой Кирой.\n-В групповой сцене в бассейне больше не используется имя игрока по умолчанию.\n\n{b}0.0050-Альфа Изменения (2/7/19)\n\nНовый контент:\n-Добавлена новая сцена с групповушкой!{/b} Происходит ночью, во сне. Требуется, чтобы вы просмотрели весь текущий контент для всех персонажей, кроме сестры-близнеца Сэм и кузины Джулии.  {i}Сэм и Джулия не являются обязательными, но вы получите новый контент для них в этой сцене, если также завершите контент с ними!{/i}\n\nУстранение Ошибок:\n-Исправлены опечатки в семейной групповушке.\n-Исправлена опечатка в повторе сцены с Мамой Симоной и старшей сестрой Кирой.\n-Исправлена опечатка в разговоре с Кузиной Джулией.\n-Исправлены опечатки в сценах с Мамой Симоной.\n-Исправлена опечатка в сцене с Бабушкой Эдной." size 48

            null height 30
            use progress_button_screen("Продолжить", xalign=0.5)
            null height 30


label splashscreen:
    show bg black




    if not persistent.disable_warning:
        show bg warning
        show screen splash_text
        with dissolve
        $ renpy.pause(2)
        show splash_ctc
        $ renpy.pause()

        hide screen splash_text
        hide splash_ctc

        show bg black
        with Dissolve(0.75)

    if not persistent.version_1_changelog_read:
        show screen changelog
        pause
        $ persistent.version_1_changelog_read = True
        hide screen changelog

    return